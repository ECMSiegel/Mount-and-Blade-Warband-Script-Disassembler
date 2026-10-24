#!/usr/bin/env python3
"""wbport -- a safety harness for port scripts that copy a feature into a compiled Warband module.

A port script is a short Python file that adds scripts, triggers and menu calls to a TARGET
module folder (always a copy you own). This harness does the chores that every such script must
get right, so the script only says what to add:

    import wbport
    from wbops import CALL_SCRIPT, ASSIGN, SCRIPT, GVAR

    with wbport.Port("my_feature", "/path/to/target_copy", source="/path/to/source_module") as p:
        gv = p.id("global", "my_flag")                       # looked up BY NAME in the target
        idx = p.add_script_once("my_feature_tick", [p.statement(ASSIGN, GVAR(gv), 1)])
        p.add_simple_trigger_once(24.0, [p.statement(CALL_SCRIPT, SCRIPT(idx))],
                                  calls="my_feature_tick")

What it guarantees
  * Refuses a target inside the configured Modules folder (wbsd.config.MODULES_DIR) unless
    allow_modules_dir=True. Work on a copy.
  * Each table is backed up once, to <file>.bak_before_<name>, never over an existing backup.
  * A table that does not round-trip byte-for-byte on load stops the port (the parser does not
    understand that file, so writing would corrupt it).
  * The *_once helpers are idempotent: a second run changes nothing.
  * On a clean exit every loaded table is checked (round trip, line endings, block depth on every
    new or changed block) BEFORE anything is written. If any check fails nothing is written.
  * On an exception nothing is written. (The backup copy, an unchanged copy of the original, may
    already exist.)
  * source_doc(table) is a read-only view of the SOURCE's table, and remap(statement) copies a
    source statement with every named operand translated to the target's id by name.
  * dry_run=True does every check and writes nothing at all (no backup, no log line).
  * A JSON line (name, time, tables, scripts_added, source) is appended to
    <target_dir>/ports.log.jsonl when something actually changed and log=True.

Python standard library only.
"""
import datetime
import difflib
import json
import os
import shutil
import tempfile

import wbasm
from wbasm import Statement, block_depth_ok, opmask, opval, enc
from wbops import CALL_SCRIPT, SCRIPT
from wbsd import config


class PortError(Exception):
    """Anything a port script should stop on: bad target, missing name, failed check."""


#: table name -> (file name, wbasm loader)
TABLES = {
    "scripts": ("scripts.txt", wbasm.load_scripts),
    "simple_triggers": ("simple_triggers.txt", wbasm.load_simple_triggers),
    "triggers": ("triggers.txt", wbasm.load_triggers),
    "menus": ("menus.txt", wbasm.load_menus),
    "conversation": ("conversation.txt", wbasm.load_conversation),
    "presentations": ("presentations.txt", wbasm.load_presentations),
    "mission_templates": ("mission_templates.txt", wbasm.load_mission_templates),
    "tableau_materials": ("tableau_materials.txt", wbasm.load_tableau_materials),
}

LOG_NAME = "ports.log.jsonl"

#: Operand kinds that `Port.remap` translates by name (source id -> name -> target id). They are
#: the tags in the header tables whose records have names in the module. Not remapped: reg, local
#: (registers and locals), icon (no names are listed), and untagged numbers.
REMAP_KINDS = frozenset((
    "global", "string", "item", "troop", "faction", "quest", "pt", "party", "scene", "mt",
    "menu", "script", "psys", "spr", "sound", "skill", "mesh", "prsnt", "qstr", "track",
    "tableau", "anim"))


# --- change tracking: every table is a list of "units" (a script, a menu, a trigger line...) ----

def _units(table, doc):
    """The doc's records as (serialized bytes, function returning [(label, token list)])."""
    out = []
    if table == "scripts":
        for s in doc.scripts:
            out.append((s.serialize_name() + s.serialize(), lambda s=s: [("body", s.tokens)]))
    elif table in ("simple_triggers", "tableau_materials"):
        for t in (doc.triggers if table == "simple_triggers" else doc.materials):
            out.append((t.serialize(), lambda t=t: [("body", t.tokens)]))
    elif table in ("triggers", "mission_templates"):
        for t in doc.triggers:
            out.append((t.serialize(), lambda t=t: [("conditions", t.cond_tokens),
                                                    ("consequences", t.conseq_tokens)]))
    elif table == "menus":
        for m in doc.menus:
            def blocks(m=m):
                bl = [("body", m.stmt_tokens)]
                for o in m.options:
                    bl.append((o.name + " conditions", o.cond_tokens))
                    bl.append((o.name + " consequences", o.conseq_tokens))
                return bl
            out.append((m.serialize() + m.serialize_options(), blocks))
    elif table == "conversation":
        for d in doc.dialogs:
            out.append((d.serialize(), lambda d=d: [("conditions", d.cond_tokens),
                                                    ("consequences", d.conseq_tokens)]))
    elif table == "presentations":
        for p in doc.presentations:
            out.append((p.serialize(), lambda p=p: [("trigger %d" % i, t.tokens)
                                                    for i, t in enumerate(p.triggers)]))
    return out


def _snapshot(table, doc):
    return [(b, [tuple(t) for _, t in blocks()]) for b, blocks in _units(table, doc)]


def _unit_name(doc, i):
    for attr in ("scripts", "menus", "dialogs", "presentations", "materials"):
        recs = getattr(doc, attr, None)
        if recs is not None and i < len(recs):
            return getattr(recs[i], "name", "#%d" % i)
    return "#%d" % i


def _eol_style(data):
    """'crlf' if every newline is CRLF, 'lf' if none is, else 'mixed'."""
    crlf = data.count(b"\r\n")
    lf = data.count(b"\n")
    if lf == 0:
        return "none"
    if crlf == lf:
        return "crlf"
    return "lf" if crlf == 0 else "mixed"


def _tokens(stmts):
    return [s.tokens() for s in stmts]


def _calls_script(stmts, script_index):
    target = SCRIPT(script_index)
    return any(s.opcode == CALL_SCRIPT and s.operands[:1] == [target] for s in stmts)


def _script_index(names, name):
    """Index of script `name` in a list of stored names. Accepts the `script_` form that
    `wbsd dis` prints: tried as given first, then without the prefix. -1 if absent."""
    for cand in (name, name[7:] if name.startswith("script_") else None):
        if cand is not None and cand in names:
            return names.index(cand)
    return -1


def _hint(name, choices):
    near = difflib.get_close_matches(name, list(choices), n=5, cutoff=0.5)
    return ". Close matches: " + ", ".join(near) if near else ""


def _inside(path, folder):
    """True if `path` is `folder` or below it. Robust to case-insensitive disks, symlinks,
    '..' and trailing slashes: every ancestor of the path is compared with samefile."""
    if not os.path.exists(folder):
        return False
    for start in (os.path.abspath(path), os.path.realpath(path)):
        cur = start
        while True:
            try:
                if os.path.samefile(cur, folder):
                    return True
            except OSError:
                pass
            parent = os.path.dirname(cur)
            if parent == cur:
                break
            cur = parent
    p, f = os.path.normcase(os.path.realpath(path)).casefold(), os.path.normcase(os.path.realpath(folder)).casefold()
    return p == f or p.startswith(f.rstrip(os.sep) + os.sep)


class Port(object):
    def __init__(self, name, target_dir, source=None, dry_run=False, log=True,
                 allow_modules_dir=False):
        if not name or not all(c.isalnum() or c in "_-" for c in name):
            raise PortError("port name %r must be a short id of letters, digits, _ or -" % (name,))
        self.name = name
        self.target_dir = os.path.abspath(target_dir)
        self.source = os.path.abspath(source) if source else None
        self.dry_run = dry_run
        self.log = log
        if not os.path.isdir(self.target_dir):
            raise PortError("target folder not found: %s" % self.target_dir)
        if self.source is not None and not os.path.isdir(self.source):
            raise PortError("source folder not found: %s" % self.source)
        modules = config.MODULES_DIR
        if not allow_modules_dir and modules and _inside(self.target_dir, modules):
            raise PortError(
                "refusing to port into %s: it is inside the Modules folder (%s). Work on a "
                "copy of the module outside that folder, or pass allow_modules_dir=True if you "
                "really mean to change the live module." % (self.target_dir, modules))
        self._docs = {}
        self._orig = {}        # table -> original file bytes
        self._snap = {}        # table -> [(unit bytes, [block token tuples])] at load
        self._mods = {}        # "target"/"source" -> corpus Module
        self._src_docs = {}    # table -> read-only wbasm document of the source
        self.scripts_added = []
        self.notes = []          # plain-English lines such as "script x already present"
        self.saved_tables = []   # set by save(): the tables that changed

    # -- context manager ---------------------------------------------------
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.save()
        return False

    # -- tables ------------------------------------------------------------
    def _path(self, table, which="target"):
        if table not in TABLES:
            raise PortError("unknown table %r; choose one of: %s" % (table, ", ".join(sorted(TABLES))))
        folder = self.target_dir if which == "target" else self.source
        fname = TABLES[table][0]
        p = os.path.join(folder, fname)
        if os.path.isfile(p):
            return p
        low = fname.lower()
        for f in os.listdir(folder):
            if f.lower() == low:
                return os.path.join(folder, f)
        raise PortError("%s has no %s (looked in %s)" % (which, fname, folder))

    def source_doc(self, table):
        """A read-only wbasm document of the SOURCE module's `table` (same tables as `doc()`).

        Never backed up, never saved, never checked: changes made to it are discarded. Raises
        PortError when no source was given."""
        if self.source is None:
            raise PortError("no source module was given to Port(...)")
        if table not in self._src_docs:
            path = self._path(table, "source")
            try:
                self._src_docs[table] = TABLES[table][1](path)
            except (ValueError, IndexError, KeyError, UnicodeDecodeError) as e:
                raise PortError("source %s cannot be parsed (%s: %s)"
                                % (os.path.basename(path), type(e).__name__, e))
        return self._src_docs[table]

    def doc(self, table):
        """The wbasm document for `table`, loaded once (backed up on its first load)."""
        if table in self._docs:
            return self._docs[table]
        path = self._path(table)
        with open(path, "rb") as fh:
            raw = fh.read()
        try:
            doc = TABLES[table][1](path)
            same = doc.serialize() == raw
        except (ValueError, IndexError, KeyError, UnicodeDecodeError) as e:
            raise PortError("%s cannot be parsed (%s: %s); not safe to write"
                            % (os.path.basename(path), type(e).__name__, e))
        if not same:
            raise PortError("%s does not round-trip byte-for-byte on load; the parser does not "
                            "understand this file, so writing it would corrupt it"
                            % os.path.basename(path))
        if not self.dry_run:
            backup = "%s.bak_before_%s" % (path, self.name)
            if not os.path.exists(backup):
                shutil.copy2(path, backup)
        self._docs[table] = doc
        self._orig[table] = raw
        self._snap[table] = _snapshot(table, doc)
        return doc

    # -- names -------------------------------------------------------------
    def _module(self, which):
        if which not in self._mods:
            from wbsd import corpus      # needs the generated header tables; only name lookups do
            root = self.target_dir if which == "target" else self.source
            self._mods[which] = corpus.load("port-" + which, root)
        return self._mods[which]

    def _lookup(self, which, kind, name):
        names = self._module(which).names
        if kind not in names:
            raise PortError("%s module has no %r names; known kinds: %s"
                            % (which, kind, ", ".join(sorted(names))))
        lst = names[kind]
        if kind == "global" and name.startswith("$"):
            name = name[1:]
        if kind == "script" and which == "target":
            lst = [s.name for s in self.doc("scripts").scripts]   # includes scripts added this run
        if kind == "script":
            i = _script_index(lst, name)
            if i >= 0:
                return i
        elif name in lst:
            return lst.index(name)
        raise PortError("%s module has no %s named %r%s"
                        % (which, kind, name, _hint(name, lst)))

    def id(self, kind, name):
        """The compiled id (table index) of `name` in the TARGET."""
        return self._lookup("target", kind, name)

    def source_id(self, kind, name):
        """The compiled id (table index) of `name` in the SOURCE module."""
        if self.source is None:
            raise PortError("no source module was given to Port(...)")
        return self._lookup("source", kind, name)

    def remap(self, statement):
        """A NEW Statement: same opcode and flags, with every operand that points at a named
        record translated from the SOURCE id to the TARGET id by name.

        Remapped tags: global, string, item, troop, faction, quest, pt (party template), party,
        scene, mt (mission template), menu, script, psys, spr (scene prop), sound, skill, mesh,
        prsnt, qstr, track, tableau, anim. Kept as they are: untagged numbers, registers, local
        variables, icons and any tag this list does not name. Raises PortError naming the record
        when the target lacks it (or the source id is out of range). Needs a source module and
        the generated header tables."""
        if self.source is None:
            raise PortError("no source module was given to Port(...)")
        from wbsd.headers import TAGS
        out = []
        for o in statement.operands:
            kind = TAGS.get(opmask(o)) if isinstance(o, int) and o >= 0 else None
            if kind not in REMAP_KINDS:
                out.append(o)
                continue
            src_names = self._module("source").names.get(kind)
            if src_names is None:
                raise PortError("source module has no %r names to translate operand %d by"
                                % (kind, o))
            sid = opval(o)
            if sid >= len(src_names):
                raise PortError("source %s id %d is out of range (the source has %d)"
                                % (kind, sid, len(src_names)))
            out.append(enc(opmask(o), self._lookup("target", kind, src_names[sid])))
        return Statement(statement.opcode, out, flags=statement.flags)

    def has_script(self, name):
        return _script_index([s.name for s in self.doc("scripts").scripts], name) >= 0

    # -- building ----------------------------------------------------------
    @staticmethod
    def statement(opcode, *operands, **kw):
        """Statement(opcode, [operands]); build operands with the wbops encoders."""
        return Statement(opcode, list(operands), flags=kw.pop("flags", 0))

    # -- idempotent edits --------------------------------------------------
    def add_script_once(self, name, statements):
        """Append script `name` at the end. Returns its index. Same statements already there: no-op."""
        statements = list(statements)
        if name.startswith("script_"):
            raise PortError("script names are stored without the 'script_' prefix; use %r"
                            % name[7:])
        if not block_depth_ok(statements):
            raise PortError("script %s: try_begin/try_end do not balance" % name)
        scripts = self.doc("scripts")
        existing = scripts.by_name(name)
        if existing is not None:
            if _tokens(existing.statements()) == _tokens(statements):
                self.notes.append("script %s already present" % name)
                return scripts.index_of(name)
            raise PortError("script %s already exists with different statements; refusing to "
                            "overwrite it (rename the new one or remove the old by hand)" % name)
        idx = scripts.append_script(name, statements)
        self.scripts_added.append(name)
        return idx

    def add_simple_trigger_once(self, interval, statements, calls=None):
        """Append a simple trigger unless one already calls script `calls`. Returns True if added.

        Without `calls`, an existing trigger with the same interval and statements counts."""
        statements = list(statements)
        if not block_depth_ok(statements):
            raise PortError("simple trigger: try_begin/try_end do not balance")
        scripts = self.doc("scripts")
        doc = self.doc("simple_triggers")
        if calls is not None:
            idx = _script_index([x.name for x in scripts.scripts], calls)
            if idx < 0:
                raise PortError("script %r not found for the trigger%s"
                                % (calls, _hint(calls, [s.name for s in scripts.scripts])))
            if any(_calls_script(t.statements(), idx) for t in doc.triggers):
                self.notes.append("a simple trigger already calls %s" % calls)
                return False
        else:
            want = _tokens(statements)
            if any(float(t.interval) == float(interval) and _tokens(t.statements()) == want
                   for t in doc.triggers):
                self.notes.append("identical simple trigger already present")
                return False
        doc.append_trigger(interval, statements)
        return True

    def menu_add_call_once(self, menu, option, script_name, where="consequences"):
        """Append `call_script script_name` to a menu option's consequences (or conditions),
        unless the call is already there. Returns True if added."""
        if where not in ("consequences", "conditions"):
            raise PortError("where must be 'consequences' or 'conditions', not %r" % (where,))
        scripts = self.doc("scripts")
        idx = _script_index([x.name for x in scripts.scripts], script_name)
        if idx < 0:
            raise PortError("script %r not found%s"
                            % (script_name, _hint(script_name, [s.name for s in scripts.scripts])))
        menus = self.doc("menus")
        m = menus.by_name(menu)
        if m is None:
            raise PortError("menu %r not found%s" % (menu, _hint(menu, [x.name for x in menus.menus])))
        opt = next((o for o in m.options if o.name == option), None)
        if opt is None:
            raise PortError("menu %s has no option %r%s"
                            % (menu, option, _hint(option, [o.name for o in m.options])))
        stmts = opt.consequences() if where == "consequences" else opt.conditions()
        if _calls_script(stmts, idx):
            self.notes.append("%s/%s already calls %s" % (menu, option, script_name))
            return False
        stmts.append(Statement(CALL_SCRIPT, [SCRIPT(idx)]))
        (opt.set_consequences if where == "consequences" else opt.set_conditions)(stmts)
        return True

    # -- checking and saving -------------------------------------------------
    def _check(self):
        """Run every check; return {table: new bytes} for tables that changed."""
        changed = {}
        for table, doc in self._docs.items():
            label = TABLES[table][0]
            new = doc.serialize()
            if new == self._orig[table]:
                continue
            # round trip: what we would write must parse and re-serialize to identical bytes
            with tempfile.TemporaryDirectory() as tmp:
                p = os.path.join(tmp, os.path.basename(self._path(table)))
                with open(p, "wb") as fh:
                    fh.write(new)
                try:
                    again = TABLES[table][1](p).serialize()
                except (ValueError, IndexError, KeyError, UnicodeDecodeError) as e:
                    raise PortError("%s: the edited file does not parse again (%s: %s)"
                                    % (label, type(e).__name__, e))
            if again != new:
                raise PortError("%s: the edited file does not round-trip byte-for-byte" % label)
            before, after = _eol_style(self._orig[table]), _eol_style(new)
            if before not in ("mixed", "none") and after != before:
                raise PortError("%s: line endings changed (%s -> %s)" % (label, before, after))
            snap = self._snap[table]
            for i, (b, blocks) in enumerate(_units(table, doc)):
                old = snap[i] if i < len(snap) else None
                if old is not None and old[0] == b:
                    continue
                for j, (what, toks) in enumerate(blocks()):
                    if old is not None and j < len(old[1]) and old[1][j] == tuple(toks):
                        continue            # this block is as it was on load; not ours to judge
                    try:
                        ok = block_depth_ok(wbasm.parse_statements(toks))
                    except (ValueError, IndexError) as e:
                        raise PortError("%s: %s (%s) does not parse (%s)"
                                        % (label, _unit_name(doc, i), what, e))
                    if not ok:
                        raise PortError("%s: %s (%s) has unbalanced try_begin/try_end"
                                        % (label, _unit_name(doc, i), what))
            changed[table] = new
        return changed

    def save(self):
        """Check every loaded table, then write the changed ones (unless dry_run)."""
        changed = self._check()
        self.saved_tables = sorted(changed)
        if self.dry_run or not changed:
            return self.saved_tables
        for table in changed:
            if os.path.islink(self._path(table)):
                raise PortError("%s is a symlink; saving would replace the link with a regular "
                                "file. Port into a real copy of the module instead."
                                % TABLES[table][0])
        tmps = []
        done = []
        try:
            for table, data in changed.items():
                path = self._path(table)
                tmp = path + ".wbport.tmp"
                with open(tmp, "wb") as fh:
                    fh.write(data)
                shutil.copymode(path, tmp)
                tmps.append((table, tmp, path))
            try:
                for table, tmp, path in tmps:
                    os.replace(tmp, path)
                    done.append((table, path))
            except OSError as e:
                for table, path in done:        # put back what was already replaced
                    with open(path, "wb") as fh:
                        fh.write(self._orig[table])
                raise PortError("could not write all tables (%s); restored the ones already "
                                "written" % e)
        finally:
            for _t, tmp, _p in tmps:
                if os.path.exists(tmp):
                    os.remove(tmp)
        if self.log:
            line = {"name": self.name,
                    "time": datetime.datetime.now().isoformat(timespec="seconds"),
                    "tables": self.saved_tables,
                    "scripts_added": list(self.scripts_added),
                    "source": self.source}
            with open(os.path.join(self.target_dir, LOG_NAME), "a", encoding="utf-8") as fh:
                fh.write(json.dumps(line) + "\n")
        return self.saved_tables
