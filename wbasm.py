#!/usr/bin/env python3
"""wbasm -- a minimal assembler/disassembler for Warband compiled module data.

A compiled Warband module ships as text tables (scripts.txt, menus.txt, ...)
holding bytecode, with no Module System source. This module models that
bytecode well enough to read a module's tables back byte-for-byte, which is
what makes writing new code into them safe.

FORMAT (all of it established by decoding statements this module actually ships;
see tests/test_wbasm.py for the evidence assertions)

  A statement is:   <opcode> <operand_count> <operand>...

  The opcode carries flags in its high bits:
      0x80000000  neg|            e.g. 2147483679 = neg|31
      0x40000000  this_or_next|   e.g. 1073741977 = this_or_next|153

  An operand is:    opmask << 56 | value
      1  register        72057594037927936    = reg0
      2  global variable
      3  string
      4  item            288230376151711825   = item 81
      5  troop           360287970189639950   = troop 270
     13  script          936748722493063753   = script 585
     17  local variable  1224979098644774912  = local 0
     19  skill           1369094286720630799  = skill 15
     22  quick string
  Bare constants (including negatives such as -1) carry mask 0 and pass through
  untouched.

  Control flow is structural, not offset-based: try_begin/try_end/else_try
  delimit blocks by sequence alone. That is precisely why inserting well-formed
  statements into an existing block is safe -- there are no jump targets to fix.

SAFETY MODEL
  Records remember their original bytes and re-serialise them verbatim unless
  actually modified, so loading and saving an untouched file is a no-op at the
  byte level. Scripts are referenced by INDEX (call_script takes an index), so
  new scripts must only ever be APPENDED -- never inserted.
"""
import re

# --- opcode flags -----------------------------------------------------------

OP_NEG = 0x80000000
OP_THIS_OR_NEXT = 0x40000000
OP_FLAG_MASK = OP_NEG | OP_THIS_OR_NEXT

# --- control flow opcodes ---------------------------------------------------

TRY_END = 3
TRY_BEGIN = 4
ELSE_TRY = 5
TRY_FOR_RANGE = 6
TRY_FOR_RANGE_BACKWARDS = 7
TRY_FOR_PARTIES = 11
TRY_FOR_AGENTS = 12
TRY_FOR_PROP_INSTANCES = 16
TRY_FOR_PLAYERS = 17

#: Opcodes that open a block and must be closed by TRY_END. Verified by the
#: balance check in the test suite across every block the module ships. 16 and
#: 17 (multiplayer loops) are not in Native data; they are covered by the
#: synthetic test in tests/test_wbsd.py instead.
BLOCK_OPENERS = frozenset((TRY_BEGIN, TRY_FOR_RANGE, TRY_FOR_RANGE_BACKWARDS,
                           TRY_FOR_PARTIES, TRY_FOR_AGENTS,
                           TRY_FOR_PROP_INSTANCES, TRY_FOR_PLAYERS))

# --- operand encoding -------------------------------------------------------

_VALUE_BITS = 56
_VALUE_MASK = (1 << _VALUE_BITS) - 1


def opmask(operand):
    """Return the operand's type mask (0 for bare constants)."""
    if operand < 0:
        return 0
    return operand >> _VALUE_BITS


def opval(operand):
    """Return the operand's value, sign-preserved for bare constants."""
    if operand < 0:
        return operand
    return operand & _VALUE_MASK


def enc(mask, value):
    """Encode a (mask, value) pair back into a raw operand."""
    if mask == 0:
        return value
    return (mask << _VALUE_BITS) | value


def split_opcode(raw):
    """Split a raw opcode token into (base_opcode, flags)."""
    return raw & ~OP_FLAG_MASK, raw & OP_FLAG_MASK


def join_opcode(opcode, flags):
    return opcode | flags


# --- statements -------------------------------------------------------------

class Statement(object):
    __slots__ = ("opcode", "flags", "operands")

    def __init__(self, opcode, operands, flags=0):
        self.opcode = opcode
        self.flags = flags
        self.operands = list(operands)

    def __repr__(self):
        return "Statement(%d, %r, flags=0x%X)" % (
            self.opcode, self.operands, self.flags)

    def tokens(self):
        out = [str(join_opcode(self.opcode, self.flags)), str(len(self.operands))]
        out.extend(str(o) for o in self.operands)
        return out


def parse_statements(tokens):
    """Parse a flat token list into statements, consuming every token."""
    stmts = []
    i = 0
    n = len(tokens)
    while i < n:
        raw = int(tokens[i])
        if i + 1 >= n:
            raise ValueError("truncated statement at token %d: no operand count" % i)
        count = int(tokens[i + 1])
        if count < 0:
            raise ValueError("negative operand count %d at token %d" % (count, i))
        end = i + 2 + count
        if end > n:
            raise ValueError(
                "statement at token %d wants %d operands, only %d tokens remain"
                % (i, count, n - (i + 2)))
        opcode, flags = split_opcode(raw)
        stmts.append(Statement(opcode, [int(t) for t in tokens[i + 2:end]], flags))
        i = end
    return stmts


def emit_statements(stmts):
    """Flatten statements back into a token list."""
    out = []
    for st in stmts:
        out.extend(st.tokens())
    return out


def parse_n_statements(tokens, n):
    """Parse exactly n statements from the front of a token list.

    Unlike parse_statements, this does not require the whole list to be
    consumed -- it's for blocks embedded in a line that carries more data
    after the statement block (e.g. a menu line's trailing option count).
    Returns (statements, remaining_tokens).
    """
    stmts = []
    i = 0
    total = len(tokens)
    for _ in range(n):
        if i + 1 >= total:
            raise ValueError("truncated statement block: expected %d statements" % n)
        raw = int(tokens[i])
        count = int(tokens[i + 1])
        if count < 0:
            raise ValueError("negative operand count %d at token %d" % (count, i))
        end = i + 2 + count
        if end > total:
            raise ValueError(
                "statement at token %d wants %d operands, only %d tokens remain"
                % (i, count, total - (i + 2)))
        opcode, flags = split_opcode(raw)
        stmts.append(Statement(opcode, [int(t) for t in tokens[i + 2:end]], flags))
        i = end
    return stmts, tokens[i:]


def block_depth_ok(stmts):
    """True if try_begin/try_end nest cleanly across the block."""
    depth = 0
    for st in stmts:
        if st.opcode in BLOCK_OPENERS:
            depth += 1
        elif st.opcode == TRY_END:
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


# --- record plumbing --------------------------------------------------------

_SPLIT = re.compile(rb"(\s+)")


def _split_line(raw):
    """Split a raw line into (leading_ws, tokens, separators, trailing_ws).

    Kept as bytes so mixed CRLF/LF line endings survive untouched.
    """
    parts = _SPLIT.split(raw)
    leading = b""
    trailing = b""
    if parts and parts[0] == b"":
        parts = parts[1:]
    if parts and _SPLIT.fullmatch(parts[0]):
        leading = parts.pop(0)
    if parts and parts[-1] == b"":
        parts = parts[:-1]
    if parts and _SPLIT.fullmatch(parts[-1]):
        trailing = parts.pop()
    tokens = [p.decode("ascii") for p in parts[0::2]]
    seps = [p for p in parts[1::2]]
    return leading, tokens, seps, trailing


class _Record(object):
    """A single bytecode-bearing line, able to reproduce itself verbatim."""

    #: number of leading tokens on the line before the statement count
    HEAD_TOKENS = 0
    #: number of fixed trailing tokens AFTER the statement block (not part of
    #: the statement stream itself) -- e.g. a menu line's option count.
    TAIL_TOKENS = 0

    def __init__(self, raw):
        self._raw = raw
        self._leading, all_tokens, self._seps, self._trailing = _split_line(raw)
        h = self.HEAD_TOKENS
        self.head = all_tokens[:h]
        self.declared_count = int(all_tokens[h])
        body = all_tokens[h + 1:]
        t = self.TAIL_TOKENS
        if t:
            self.tokens = body[:-t]
            self.tail = body[-t:]
        else:
            self.tokens = body
            self.tail = []
        self.dirty = False

    def statements(self):
        return parse_statements(self.tokens)

    def set_statements(self, stmts):
        self.tokens = emit_statements(stmts)
        self.declared_count = len(stmts)
        self.dirty = True

    def serialize(self):
        if not self.dirty:
            return self._raw
        head_sep = self._seps[len(self.head)] if len(self._seps) > len(self.head) else b" "
        parts = [self._leading]
        for i, tok in enumerate(self.head):
            parts.append(tok.encode("ascii"))
            parts.append(self._seps[i] if i < len(self._seps) else b" ")
        parts.append(str(self.declared_count).encode("ascii"))
        body_tokens = self.tokens + self.tail
        if body_tokens:
            parts.append(head_sep)
            parts.append(b" ".join(t.encode("ascii") for t in body_tokens))
        parts.append(self._trailing)
        return b"".join(parts)


class Script(_Record):
    """One script: a `<name> -1` line plus a statement-bearing body line."""

    HEAD_TOKENS = 0

    def __init__(self, name_line, body_line):
        _Record.__init__(self, body_line)
        self._name_line = name_line
        self.name = _split_line(name_line)[1][0]

    @classmethod
    def new(cls, name, statements, eol=b"\r\n"):
        """Build a brand-new script record from statements."""
        name_line = ("%s -1" % name).encode("ascii") + eol
        body = b" 0" + eol          # placeholder; set_statements rewrites it
        scr = cls(name_line, body)
        scr.name = name
        scr.set_statements(statements)
        return scr

    def serialize_name(self):
        return self._name_line


class SimpleTrigger(_Record):
    """One simple trigger: `<interval> <count> <statements...>` on one line."""

    HEAD_TOKENS = 1

    @property
    def interval(self):
        return self.head[0]


class MenuLine(_Record):
    """A menu's first line:

        menu_<name> <flags> <text> <mesh> <stmt_count> <statements...> <option_count>

    The trailing <option_count> is NOT part of the statement stream -- it's a
    fixed one-token tail describing how many options follow on the next line.
    """

    HEAD_TOKENS = 4
    TAIL_TOKENS = 1

    @property
    def name(self):
        return self.head[0]

    @property
    def flags(self):
        return self.head[1]

    @property
    def text(self):
        return self.head[2]

    @property
    def mesh(self):
        return self.head[3]

    @property
    def option_count(self):
        return int(self.tail[0])


class MenuOption(object):
    """One option record within a menu's options line.

    Grammar, established by decoding menus.txt (see tests/test_wbasm.py):

        mno_<id> <cond_count> <cond stmts...> <text> <conseq_count> <conseq stmts...> <text2>

    repeated back to back with no delimiter between options. `text2` looks
    like a terminator (".") in the common case, but is ordinary option data --
    e.g. a menu option can end in a real string like
    "Door_to_the_town_center." -- so it must be consumed as a field, not
    matched against a literal ".".
    """

    __slots__ = ("name", "cond_count", "cond_tokens", "text",
                 "conseq_count", "conseq_tokens", "text2")

    def __init__(self, name, cond_count, cond_tokens, text,
                 conseq_count, conseq_tokens, text2):
        self.name = name
        self.cond_count = cond_count
        self.cond_tokens = cond_tokens
        self.text = text
        self.conseq_count = conseq_count
        self.conseq_tokens = conseq_tokens
        self.text2 = text2

    def conditions(self):
        return parse_statements(self.cond_tokens)

    def consequences(self):
        return parse_statements(self.conseq_tokens)

    def set_conditions(self, stmts):
        self.cond_tokens = emit_statements(stmts)
        self.cond_count = len(stmts)

    def set_consequences(self, stmts):
        self.conseq_tokens = emit_statements(stmts)
        self.conseq_count = len(stmts)

    def tokens(self):
        """This option's full token sequence, as it appears on the line."""
        out = [self.name, str(self.cond_count)]
        out.extend(self.cond_tokens)
        out.append(self.text)
        out.append(str(self.conseq_count))
        out.extend(self.conseq_tokens)
        out.append(self.text2)
        return out


def parse_options(tokens):
    """Parse a flat options-line token list into MenuOption records,
    consuming every token."""
    opts = []
    i = 0
    n = len(tokens)
    while i < n:
        if i + 1 >= n:
            raise ValueError("truncated option at token %d" % i)
        name = tokens[i]
        cond_count = int(tokens[i + 1])
        cond_stmts, rem = parse_n_statements(tokens[i + 2:], cond_count)
        consumed = len(tokens[i + 2:]) - len(rem)
        cond_tokens = tokens[i + 2:i + 2 + consumed]
        j = i + 2 + consumed
        if j >= n:
            raise ValueError("option %s missing text token" % name)
        text = tokens[j]
        j += 1
        if j >= n:
            raise ValueError("option %s missing conseq_count" % name)
        conseq_count = int(tokens[j])
        j += 1
        conseq_stmts, rem2 = parse_n_statements(tokens[j:], conseq_count)
        consumed2 = len(tokens[j:]) - len(rem2)
        conseq_tokens = tokens[j:j + consumed2]
        j += consumed2
        if j >= n:
            raise ValueError("option %s missing text2 token" % name)
        text2 = tokens[j]
        j += 1
        opts.append(MenuOption(name, cond_count, cond_tokens, text,
                                conseq_count, conseq_tokens, text2))
        i = j
    return opts


def emit_options(opts):
    out = []
    for o in opts:
        out.extend(o.tokens())
    return out


class MenuOptionsLine(object):
    """A menu's second line: its option records, back to back, no header.

    NOTE for whoever wires up option insertion (Task 9): appending an option
    here is not just `self.options.append(...)` + `self.dirty = True`. The
    menu line's trailing option-count token (`MenuLine.tail[0]`, exposed as
    `Menu.declared_option_count`) is a SEPARATE field on a separate line/
    object with no automatic coupling to `self.options`. Script/SimpleTrigger
    append methods only ever touch one record's own declared_count; a menu
    option append must ALSO explicitly rewrite the sibling MenuLine's tail
    token (and mark IT dirty too), or the file will end up with an options
    line whose option count silently disagrees with what the menu line
    declares. There is no append method here yet -- add one alongside that
    cross-object bookkeeping, not instead of it.
    """

    def __init__(self, raw):
        self._raw = raw
        self._leading, tokens, self._seps, self._trailing = _split_line(raw)
        self.tokens = tokens
        self.options = parse_options(tokens)
        self.dirty = False

    def serialize(self):
        # Re-emit whenever the options no longer match the tokens we parsed,
        # rather than trusting a `dirty` flag. MenuOption.set_conditions /
        # set_consequences mutate the OPTION, which has no back-reference to
        # this line and so could never set that flag -- a menu edit reported
        # success and wrote nothing. Comparing tokens is self-correcting and
        # still returns the original bytes verbatim for an untouched file,
        # which is what keeps the round-trip byte-identical.
        tokens = emit_options(self.options)
        if not self.dirty and tokens == self.tokens:
            return self._raw
        if not tokens:
            return self._leading + self._trailing
        body = b" ".join(t.encode("ascii") for t in tokens)
        return self._leading + body + self._trailing


class Menu(object):
    """One menu: a MenuLine plus its MenuOptionsLine."""

    def __init__(self, menu_line_raw, options_line_raw):
        self._line = MenuLine(menu_line_raw)
        self._options_line = MenuOptionsLine(options_line_raw)

    @property
    def name(self):
        return self._line.name

    @property
    def flags(self):
        return self._line.flags

    @property
    def text(self):
        return self._line.text

    @property
    def mesh(self):
        return self._line.mesh

    @property
    def declared_stmt_count(self):
        return self._line.declared_count

    @property
    def declared_option_count(self):
        return self._line.option_count

    @property
    def stmt_tokens(self):
        return self._line.tokens

    @property
    def options(self):
        return self._options_line.options

    @property
    def option_tokens(self):
        """The original options-line token stream, for round-trip proofs."""
        return self._options_line.tokens

    def statements(self):
        return self._line.statements()

    def set_statements(self, stmts):
        self._line.set_statements(stmts)

    def serialize(self):
        return self._line.serialize()

    def serialize_options(self):
        return self._options_line.serialize()


# --- containers -------------------------------------------------------------

def _read_lines(path):
    with open(path, "rb") as fh:
        data = fh.read()
    return data.splitlines(keepends=True)


class ScriptsDoc(object):
    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:2]
        self.declared_count = int(lines[1].split()[0])
        self.scripts = []
        rest = lines[2:]
        for i in range(0, len(rest) - 1, 2):
            self.scripts.append(Script(rest[i], rest[i + 1]))
        self.trailer = rest[len(self.scripts) * 2:]

    def by_name(self, name):
        for s in self.scripts:
            if s.name == name:
                return s
        return None

    def index_of(self, name):
        for i, s in enumerate(self.scripts):
            if s.name == name:
                return i
        return -1

    def _eol(self):
        return b"\r\n" if self.header[1].endswith(b"\r\n") else b"\n"

    def append_script(self, name, statements):
        """Append a new script and return its index.

        Append-only is a hard rule: call_script refers to scripts by index, so
        inserting anywhere else silently repoints every later call.
        """
        if self.by_name(name) is not None:
            raise ValueError("script %r already exists" % name)
        self.scripts.append(Script.new(name, statements, self._eol()))
        return len(self.scripts) - 1

    def remove_trailing_script(self, name):
        """Remove one of our own scripts, only if it is the final entry."""
        idx = self.index_of(name)
        if idx < 0:
            return False
        if idx != len(self.scripts) - 1:
            raise ValueError(
                "refusing to remove %r at index %d: not the final script, "
                "removal would repoint every later call_script index"
                % (name, idx))
        self.scripts.pop()
        return True

    def serialize(self):
        out = list(self.header)
        # the count line is rewritten only if the script total actually changed
        if len(self.scripts) != self.declared_count:
            eol = b"\r\n" if self.header[1].endswith(b"\r\n") else b"\n"
            out[1] = str(len(self.scripts)).encode("ascii") + eol
        for s in self.scripts:
            out.append(s.serialize_name())
            out.append(s.serialize())
        out.extend(self.trailer)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


class SimpleTriggersDoc(object):
    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:2]
        self.declared_count = int(lines[1].split()[0])
        self.triggers = [SimpleTrigger(ln) for ln in lines[2:] if ln.strip()]
        self.trailer = []

    def _eol(self):
        return b"\r\n" if self.header[1].endswith(b"\r\n") else b"\n"

    def append_trigger(self, interval, statements):
        raw = ("%s  0" % interval).encode("ascii") + self._eol()
        trg = SimpleTrigger(raw)
        trg.set_statements(statements)
        self.triggers.append(trg)
        return len(self.triggers) - 1

    def remove_triggers_calling(self, script_index):
        """Drop every trigger whose body calls the given script index."""
        target = enc(13, script_index)
        keep, removed = [], 0
        for trg in self.triggers:
            calls = any(st.opcode == 1 and st.operands and st.operands[0] == target
                        for st in trg.statements())
            if calls:
                removed += 1
            else:
                keep.append(trg)
        self.triggers = keep
        return removed

    def serialize(self):
        out = list(self.header)
        if len(self.triggers) != self.declared_count:
            eol = b"\r\n" if self.header[1].endswith(b"\r\n") else b"\n"
            out[1] = str(len(self.triggers)).encode("ascii") + eol
        for t in self.triggers:
            out.append(t.serialize())
        out.extend(self.trailer)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


class MenusDoc(object):
    """menus.txt: `menusfile version 1` header, a declared menu count, then
    two lines per menu (the menu line, then its options line)."""

    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:2]
        self.declared_count = int(lines[1].split()[0])
        self.menus = []
        rest = lines[2:]
        for i in range(0, len(rest) - 1, 2):
            self.menus.append(Menu(rest[i], rest[i + 1]))
        self.trailer = rest[len(self.menus) * 2:]

    def by_name(self, name):
        for m in self.menus:
            if m.name == name:
                return m
        return None

    def serialize(self):
        out = list(self.header)
        if len(self.menus) != self.declared_count:
            eol = b"\r\n" if self.header[1].endswith(b"\r\n") else b"\n"
            out[1] = str(len(self.menus)).encode("ascii") + eol
        for m in self.menus:
            out.append(m.serialize())
            out.append(m.serialize_options())
        out.extend(self.trailer)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())



class PresentationTrigger(SimpleTrigger):
    """One presentation trigger line: `<interval> <count> <statements...>`.

    Byte-identical in shape to a simple trigger, so the parsing and
    re-serialisation are inherited unchanged.
    """


class Presentation(object):
    """A presentation: a header line plus its trigger lines.

    Header is `prsnt_<name> <flags> <mesh> <trigger_count>`; the declared
    trigger count is followed by exactly that many trigger lines. Blank
    separator lines between records are preserved verbatim in the doc.
    """

    def __init__(self, header_line, trigger_lines):
        self._header_raw = header_line
        tokens = header_line.split()
        self.name = tokens[0].decode("ascii")
        self.declared_triggers = int(tokens[3])
        self.triggers = [PresentationTrigger(ln) for ln in trigger_lines]

    def serialize(self):
        return b"".join([self._header_raw] + [t.serialize() for t in self.triggers])


class PresentationsDoc(object):
    """presentations.txt — the report, notes and UI screens.

    This file carries bytecode, so it needs a parser: a scan that skips it
    misses every operand inside the report, notes and UI screens.
    """

    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:2]
        self.declared_count = int(lines[1].split()[0])
        self.presentations = []
        self._gaps = {}
        i, body = 2, lines[2:]
        index = 0
        while index < len(body):
            line = body[index]
            if not line.split() or not line.split()[0].startswith(b"prsnt_"):
                self._gaps.setdefault(len(self.presentations), []).append(line)
                index += 1
                continue
            count = int(line.split()[3])
            triggers = body[index + 1:index + 1 + count]
            self.presentations.append(Presentation(line, triggers))
            index += 1 + count

    def by_name(self, name):
        for p in self.presentations:
            if p.name == name:
                return p
        raise KeyError(name)

    def serialize(self):
        out = list(self.header)
        for n, presentation in enumerate(self.presentations):
            out.extend(self._gaps.get(n, []))
            out.append(presentation.serialize())
        out.extend(self._gaps.get(len(self.presentations), []))
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


# --- two-block records -------------------------------------------------------

class _TwoBlockRecord(object):
    """A line carrying two count-prefixed statement blocks back to back.

        <head tokens...> <cond_count> <conds...> <conseq_count> <conseqs...>

    This is triggers.txt's shape and, identically, a mission template's trigger
    line. It cannot reuse _Record, which models exactly ONE declared count.
    Like every other record here it re-serialises verbatim unless modified.
    """

    #: fixed tokens before the first count (three floats for both users)
    HEAD_TOKENS = 0

    def __init__(self, raw):
        self._raw = raw
        self._leading, tokens, self._seps, self._trailing = _split_line(raw)
        h = self.HEAD_TOKENS
        self.head = tokens[:h]
        rest = tokens[h:]
        if not rest:
            raise ValueError("record has no condition count")
        self.cond_count = int(rest[0])
        _, remainder = parse_n_statements(rest[1:], self.cond_count)
        used = len(rest[1:]) - len(remainder)
        self.cond_tokens = rest[1:1 + used]
        j = 1 + used
        if j >= len(rest):
            raise ValueError("record has no consequence count")
        self.conseq_count = int(rest[j])
        _, remainder2 = parse_n_statements(rest[j + 1:], self.conseq_count)
        used2 = len(rest[j + 1:]) - len(remainder2)
        self.conseq_tokens = rest[j + 1:j + 1 + used2]
        self.tail = rest[j + 1 + used2:]
        self.dirty = False

    def conditions(self):
        return parse_statements(self.cond_tokens)

    def consequences(self):
        return parse_statements(self.conseq_tokens)

    def set_conditions(self, stmts):
        self.cond_tokens = emit_statements(stmts)
        self.cond_count = len(stmts)
        self.dirty = True

    def set_consequences(self, stmts):
        self.conseq_tokens = emit_statements(stmts)
        self.conseq_count = len(stmts)
        self.dirty = True

    def tokens(self):
        out = list(self.head)
        out.append(str(self.cond_count))
        out.extend(self.cond_tokens)
        out.append(str(self.conseq_count))
        out.extend(self.conseq_tokens)
        out.extend(self.tail)
        return out

    def serialize(self):
        if not self.dirty:
            return self._raw
        body = b" ".join(t.encode("ascii") for t in self.tokens())
        return self._leading + body + self._trailing


class Trigger(_TwoBlockRecord):
    """One triggers.txt line: `<interval> <delay> <rearm> <conds> <conseqs>`."""

    HEAD_TOKENS = 3

    @property
    def check_interval(self):
        return self.head[0]

    @property
    def delay_interval(self):
        return self.head[1]

    @property
    def rearm_interval(self):
        return self.head[2]


class TriggersDoc(object):
    """triggers.txt: `triggersfile version 1`, a count, then one line each."""

    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:2]
        self.declared_count = int(lines[1].split()[0])
        self.triggers = [Trigger(ln) for ln in lines[2:] if ln.strip()]
        self.trailer = []

    def serialize(self):
        out = list(self.header)
        for t in self.triggers:
            out.append(t.serialize())
        out.extend(self.trailer)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


# --- conversation ------------------------------------------------------------

class Dialog(object):
    """One conversation.txt line.

        dlga_<state>:<next> <flags> <partner>
            <cond_count> <conds...> <text> <next_token>
            <conseq_count> <conseqs...> <voiceover>

    `text` and `voiceover` are consumed POSITIONALLY, never matched against a
    literal. That is the menus `text2` lesson: option text looked like a "."
    terminator in the common case but carries real strings, so anything matched
    by value eventually meets a record that breaks it.
    """

    HEAD_TOKENS = 3

    __slots__ = ("_raw", "_leading", "_seps", "_trailing", "head",
                 "cond_count", "cond_tokens", "text", "next_token",
                 "conseq_count", "conseq_tokens", "voiceover", "dirty")

    def __init__(self, raw):
        self._raw = raw
        self._leading, tokens, self._seps, self._trailing = _split_line(raw)
        self.head = tokens[:self.HEAD_TOKENS]
        rest = tokens[self.HEAD_TOKENS:]
        self.cond_count = int(rest[0])
        _, remainder = parse_n_statements(rest[1:], self.cond_count)
        used = len(rest[1:]) - len(remainder)
        self.cond_tokens = rest[1:1 + used]
        j = 1 + used
        self.text = rest[j]
        self.next_token = rest[j + 1]
        j += 2
        self.conseq_count = int(rest[j])
        _, remainder2 = parse_n_statements(rest[j + 1:], self.conseq_count)
        used2 = len(rest[j + 1:]) - len(remainder2)
        self.conseq_tokens = rest[j + 1:j + 1 + used2]
        j += 1 + used2
        self.voiceover = rest[j]
        if j + 1 != len(rest):
            raise ValueError("dialog %s has %d unconsumed trailing tokens"
                             % (self.head[0], len(rest) - (j + 1)))
        self.dirty = False

    @property
    def name(self):
        return self.head[0]

    @property
    def flags(self):
        return self.head[1]

    @property
    def partner(self):
        return self.head[2]

    def conditions(self):
        return parse_statements(self.cond_tokens)

    def consequences(self):
        return parse_statements(self.conseq_tokens)

    def set_conditions(self, stmts):
        self.cond_tokens = emit_statements(stmts)
        self.cond_count = len(stmts)
        self.dirty = True

    def set_consequences(self, stmts):
        self.conseq_tokens = emit_statements(stmts)
        self.conseq_count = len(stmts)
        self.dirty = True

    def tokens(self):
        out = list(self.head)
        out.append(str(self.cond_count))
        out.extend(self.cond_tokens)
        out.append(self.text)
        out.append(self.next_token)
        out.append(str(self.conseq_count))
        out.extend(self.conseq_tokens)
        out.append(self.voiceover)
        return out

    def serialize(self):
        if not self.dirty:
            return self._raw
        body = b" ".join(t.encode("ascii") for t in self.tokens())
        return self._leading + body + self._trailing


class ConversationDoc(object):
    """conversation.txt — the largest table, and full of faction operands.

    Dialogue records embed condition and consequence bytecode, so those are real
    operands. Without a parser here, any audit of faction references would be
    blind to them and its totals would cover only the parsed subset.
    """

    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:2]
        self.declared_count = int(lines[1].split()[0])
        self.dialogs = [Dialog(ln) for ln in lines[2:] if ln.strip()]
        self.trailer = []

    def by_name(self, name):
        for d in self.dialogs:
            if d.name == name:
                return d
        return None

    def serialize(self):
        out = list(self.header)
        for d in self.dialogs:
            out.append(d.serialize())
        out.extend(self.trailer)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


# --- tableau materials -------------------------------------------------------

class TableauMaterial(_Record):
    """One tableau_materials.txt line.

        <name> <flags> <sampler> <w> <h> <mx> <my> <mw> <mh> <count> <stmts...>
    """

    HEAD_TOKENS = 9

    @property
    def name(self):
        return self.head[0]


class TableauMaterialsDoc(object):
    """tableau_materials.txt.

    NOTE: this file has NO `...file version N` line. Its header is the record
    count alone, so the header slice is lines[:1] rather than lines[:2] as in
    every other document here.
    """

    def __init__(self, path):
        self.path = path
        lines = _read_lines(path)
        self.header = lines[:1]
        self.declared_count = int(lines[0].split()[0])
        self.materials = [TableauMaterial(ln) for ln in lines[1:] if ln.strip()]
        self.trailer = []

    def by_name(self, name):
        for m in self.materials:
            if m.name == name:
                return m
        return None

    def serialize(self):
        out = list(self.header)
        for m in self.materials:
            out.append(m.serialize())
        out.extend(self.trailer)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


# --- mission templates -------------------------------------------------------

def _looks_like_trigger_line(raw):
    """True when a line is a mission-template trigger record.

    Detected by SHAPE rather than by walking the file's structure. The
    structural walk is not line-oriented: a template's entry-point count shares
    its line with the first entry point, and a template with ZERO entry points
    (mst_camera_test) puts the entry count and the trigger count on the SAME
    line, which silently orphaned 14 trigger lines.

    The three leading floats are the discriminator -- they always carry a '.',
    while entry-point records are bare integers -- and the record must then
    consume exactly as two statement blocks with nothing left over.
    """
    tokens = raw.split()
    if len(tokens) < 5 or not all(b"." in t for t in tokens[:3]):
        return False
    try:
        for t in tokens[:3]:
            float(t)
        rest = [t.decode("ascii") for t in tokens[3:]]
        _, remainder = parse_n_statements(rest[1:], int(rest[0]))
        used = len(rest[1:]) - len(remainder)
        j = 1 + used
        _, remainder2 = parse_n_statements(rest[j + 1:], int(rest[j]))
        return not remainder2
    except (ValueError, IndexError, UnicodeDecodeError):
        return False


class MissionTemplatesDoc(object):
    """mission_templates.txt — trigger bytecode parsed, everything else opaque.

    Header, description, entry-point and count lines are kept as raw bytes and
    re-emitted verbatim. Only trigger lines are modelled, because only they
    carry bytecode: every faction operand in the file lives inside them,
    verified by a raw byte scan in the test suite. Entry-point records are bare
    integers in fixed-width columns -- a different kind of data from bytecode,
    where a bad value can crash the game at new-game start -- and are
    deliberately not modelled.
    """

    def __init__(self, path):
        self.path = path
        self.lines = _read_lines(path)
        self.header = self.lines[:2]
        self.declared_count = int(self.lines[1].split()[0])
        self._triggers = {}
        for index, raw in enumerate(self.lines):
            if index >= 2 and _looks_like_trigger_line(raw):
                self._triggers[index] = Trigger(raw)

    @property
    def triggers(self):
        return [self._triggers[i] for i in sorted(self._triggers)]

    @property
    def template_names(self):
        return [ln.split()[0].decode("ascii") for ln in self.lines
                if ln.split() and ln.split()[0].startswith(b"mst_")]

    def serialize(self):
        out = []
        for index, raw in enumerate(self.lines):
            trigger = self._triggers.get(index)
            out.append(trigger.serialize() if trigger is not None else raw)
        return b"".join(out)

    def save(self):
        with open(self.path, "wb") as fh:
            fh.write(self.serialize())


def load_triggers(path):
    return TriggersDoc(path)


def load_conversation(path):
    return ConversationDoc(path)


def load_tableau_materials(path):
    return TableauMaterialsDoc(path)


def load_mission_templates(path):
    return MissionTemplatesDoc(path)


def load_presentations(path):
    return PresentationsDoc(path)


def load_scripts(path):
    return ScriptsDoc(path)


def load_simple_triggers(path):
    return SimpleTriggersDoc(path)


def load_menus(path):
    return MenusDoc(path)
