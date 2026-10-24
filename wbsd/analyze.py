"""Structural analysis of loaded modules: operand decoding, named disassembly,
cross-references (calls, slots, globals, resources) and fingerprints."""
import hashlib
import os
import pickle
from collections import Counter, defaultdict

from . import corpus, headers
from .opref import OPS, CALL_SCRIPT, TRY_END, ELSE_TRY, BLOCK_OPENERS, NEG, THIS_OR_NEXT, NEG_ALIASES

VALUE_MASK = (1 << 56) - 1
RESOURCE_TAGS = {t: k for t, k in headers.TAGS.items() if k not in ("reg", "global", "local")}

# Opcode-argument roles that name a resource table. Some mods compiled with an
# older Module System omit type tags (ids WITHOUT the type tag); for
# those a bare constant in one of these positions is resolved through the role.
# ("string" is excluded: a bare string_id could be a string or a quick string.)
ROLE_KINDS = {"troop", "party", "faction", "item", "scene", "quest", "pt", "menu",
              "prsnt", "mt", "spr", "sound", "psys", "mesh", "icon", "skill",
              "tableau", "anim", "track"}
SLOT_OBJ_KIND = {"troop": "troop", "party": "party", "faction": "faction", "scene": "scene",
                 "party_template": "pt", "quest": "quest", "item": "item"}


def bare_kind(mod, code, op, i, val):
    """Resource kind of an UNTAGGED constant, judged by its argument role."""
    if val < 0 or op is None:
        return None
    role = _role(op, code, i)
    if role not in ROLE_KINDS:
        if op.slot and ((op.slot[1] == "get" and i == 1) or (op.slot[1] != "get" and i == 0)):
            role = SLOT_OBJ_KIND.get(op.slot[0])
        else:
            return None
    if role and val < len(mod.names.get(role, ())):
        return role
    return None


def decode(o):
    """(tag, value). Bare constants -> tag 0. Out-of-range tags -> tag 0, raw."""
    if o < 0:
        return 0, o
    tag = o >> 56
    if tag in headers.TAGS:
        return tag, o & VALUE_MASK
    return 0, o


def _role(op, code, i):
    if code == CALL_SCRIPT:
        return "script" if i == 0 else "param"
    if op is None:
        return "?"
    if i < len(op.roles):
        return op.roles[i]
    if op.args and "..." in op.args[-1]:
        return "param"
    return "extra"


def operand_text(mod, code, op, i, o):
    tag, val = decode(o)
    if tag == 17:
        return ":l%d" % val
    if tag == 1:
        return "reg%d" % val
    if tag == 2:
        n = mod.name("global", val)
        return "$" + n if n else "$g%d" % val
    if tag:
        kind = headers.TAGS[tag]
        n = mod.name(kind, val)
        return n if n else "%s#%d" % (kind, val)
    role = _role(op, code, i)
    if role == "script":
        n = mod.name("script", val)
        return ("script_%s{bare}" % n) if n else str(val)
    bk = bare_kind(mod, code, op, i, val)
    if bk:
        return mod.name(bk, val)
    if code in headers.KEY_OPS and i == 0 and val in headers.KEYS:
        return headers.KEYS[val]
    if role == "pos":
        return "pos%d" % val
    if role == "sreg":
        return "s%d" % val
    return str(val)


def stmt_text(mod, st):
    code, flags, ops = st
    op = OPS.get(code)
    name = op.name if op else "UNKNOWN_op%d" % code
    if flags & NEG:
        if code in NEG_ALIASES:
            name = NEG_ALIASES[code]
        else:
            name = "neg|" + name
    if flags & THIS_OR_NEXT:
        name = "this_or_next|" + name
    if code == CALL_SCRIPT and ops:
        tag, val = decode(ops[0])
        n = mod.name("script", val) if tag in (0, 13) else None
        head = "call_script, script_%s" % n if n else "call_script, %s" % operand_text(mod, code, op, 0, ops[0])
        if tag == 0 and n:
            head += " {bare-int}"
        rest = [operand_text(mod, code, op, i, o) for i, o in enumerate(ops[1:], 1)]
        return "(%s)" % ", ".join([head] + rest)
    args = [operand_text(mod, code, op, i, o) for i, o in enumerate(ops)]
    return "(%s)" % ", ".join([name] + args)


def disassemble(mod, block, numbered=True):
    out, depth = [], 0
    # statement text depends only on the statement and the module's names, and
    # the same statements recur all over a module, so render each one once
    memo = mod.__dict__.get("_stmt_text")
    if memo is None:
        memo = mod._stmt_text = {}
    for n, st in enumerate(block.stmts):
        code = st[0]
        if code == TRY_END:
            depth = max(depth - 1, 0)
        d = depth - 1 if code == ELSE_TRY and depth else depth
        prefix = "%4d  " % n if numbered else ""
        text = memo.get(st)
        if text is None:
            text = memo[st] = stmt_text(mod, st)
        out.append(prefix + "  " * d + text + ",")
        if code in BLOCK_OPENERS:
            depth += 1
    return out


# ---------------------------------------------------------------- xrefs

class XRef(object):
    """Everything one block touches."""
    __slots__ = ("calls", "refs", "slots", "globals", "unknown", "params",
                 "returns", "opcodes", "strings")

    def __init__(self):
        self.calls = []      # (script_idx, bare_bool, stmt_no)
        self.refs = []       # (kind, idx, role, stmt_no)
        self.slots = []      # (objkind, access, slot, obj_repr, value_repr, value_kind, stmt_no)
        self.globals = []    # (gidx, 'r'|'w', stmt_no)
        self.unknown = Counter()
        self.params = 0
        self.returns = set()
        self.opcodes = Counter()
        self.strings = []    # (kind, idx)


def _repr_operand(mod, o):
    tag, val = decode(o)
    if tag == 0:
        return str(val), "const"
    return operand_text(mod, None, None, 0, o), headers.TAGS[tag]


def xref(mod, block):
    x = XRef()
    for n, (code, flags, ops) in enumerate(block.stmts):
        op = OPS.get(code)
        x.opcodes[code] += 1
        if op is None:
            x.unknown[code] += 1
        if code == CALL_SCRIPT and ops:
            tag, val = decode(ops[0])
            if tag == 13 or (tag == 0 and 0 <= val < len(mod.names.get("script", []))):
                x.calls.append((val, tag == 0, n))
        if code in (21, 22):
            x.params = max(x.params, code - 20)
        elif code == 23 and len(ops) > 1:
            t, v = decode(ops[1])
            if t == 0 and 0 < v < 20:
                x.params = max(x.params, v)
        if code == 2075:
            x.returns.add("trigger_result")
        if code == 60:
            x.returns.add("result_string")
        for i, o in enumerate(ops):
            tag, val = decode(o)
            if tag == 2:
                w = i == 0 and op is not None and op.writes_first
                x.globals.append((val, "w" if w else "r", n))
            elif tag == 1 and val == 0 and i == 0 and op is not None and op.writes_first:
                x.returns.add("reg0")
            elif tag in RESOURCE_TAGS:
                kind = RESOURCE_TAGS[tag]
                if code == CALL_SCRIPT and i == 0:
                    continue
                x.refs.append((kind, val, _role(op, code, i), n))
                if kind in ("string", "qstr"):
                    x.strings.append((kind, val))
            elif tag == 0 and code != CALL_SCRIPT:
                bk = bare_kind(mod, code, op, i, val)
                if bk:
                    x.refs.append((bk, val, _role(op, code, i) + "{bare}", n))
        if op is not None and op.slot and len(ops) >= 3:
            objkind, access = op.slot
            if access == "get":
                obj, slot, val = ops[1], ops[2], ops[0]
            else:
                obj, slot, val = ops[0], ops[1], ops[2]
            st, sv = decode(slot)
            slot_no = sv if st == 0 else None
            orep, _ = _repr_operand(mod, obj)
            ot, ov = decode(obj)
            if ot == 0 and ov >= 0 and SLOT_OBJ_KIND.get(objkind) and ov < len(mod.names.get(SLOT_OBJ_KIND[objkind], ())):
                orep = mod.name(SLOT_OBJ_KIND[objkind], ov)
            vrep, vkind = _repr_operand(mod, val)
            x.slots.append((objkind, access, slot_no, orep, vrep, vkind, n))
    return x


# ---------------------------------------------------------- fingerprints

def _h(items):
    return hashlib.sha1(repr(items).encode()).hexdigest()[:16]


def named_stmt(mod, st):
    """Statement with resource ids replaced by NAMES (index-shift tolerant).

    Untagged ids in typed argument positions are resolved by role too, so
    tag-less compilers (BI, TLD, NW, SW) hash the same as tagged ones."""
    code, flags, ops = st
    op = OPS.get(code)
    out = []
    for i, o in enumerate(ops):
        tag, val = decode(o)
        if tag == 0 and not (code == CALL_SCRIPT and i == 0):
            bk = bare_kind(mod, code, op, i, val)
            if bk:
                out.append(mod.name(bk, val))
                continue
        if tag in RESOURCE_TAGS or tag == 2 or (code == CALL_SCRIPT and i == 0):
            kind = "script" if code == CALL_SCRIPT and i == 0 else (headers.TAGS.get(tag))
            n = mod.name(kind, val) if kind != "global" else mod.name("global", val)
            out.append(n if n else (tag, val))
        else:
            out.append((tag, val))
    return (code, flags, tuple(out))


def fingerprints(mod, block):
    exact = _h(block.stmts)
    named = _h([named_stmt(mod, s) for s in block.stmts])
    shape = _h([(c, f, tuple(decode(o)[0] for o in ops)) for c, f, ops in block.stmts])
    return exact, named, shape


def named_set(mod, block):
    """Multiset of named statements -> for Jaccard similarity across modules."""
    c = Counter(named_stmt(mod, s) for s in block.stmts)
    return c


def jaccard(a, b):
    if not a and not b:
        return 1.0
    inter = sum((a & b).values())
    union = sum((a | b).values())
    return inter / float(union) if union else 0.0


# ------------------------------------------------------------- module view

class ModuleIndex(object):
    """In-memory xref index of one module (built in a few seconds)."""

    def __init__(self, mod):
        self.mod = mod
        self.x = {}
        self.callers = defaultdict(list)      # script_idx -> [(bid, stmt, bare)]
        self.global_use = defaultdict(list)   # gidx -> [(bid, rw, stmt)]
        self.slot_use = defaultdict(list)     # (objkind, slot) -> [(bid, access, obj, val, vkind, stmt)]
        self.ref_use = defaultdict(list)      # (kind, idx) -> [(bid, role, stmt)]
        self.unknown_ops = Counter()
        for b in mod.blocks:
            x = xref(mod, b)
            self.x[b.id] = x
            for idx, bare, n in x.calls:
                self.callers[idx].append((b.id, n, bare))
            for g, rw, n in x.globals:
                self.global_use[g].append((b.id, rw, n))
            for objkind, access, slot, orep, vrep, vkind, n in x.slots:
                self.slot_use[(objkind, slot)].append((b.id, access, orep, vrep, vkind, n))
            for kind, idx, role, n in x.refs:
                self.ref_use[(kind, idx)].append((b.id, role, n))
            self.unknown_ops.update(x.unknown)

    def script_bid(self, idx):
        b = self.mod.script_block(idx)
        return b.id if b else None

    def callees(self, bid):
        return [(self.script_bid(i), n, bare) for i, bare, n in self.x[bid].calls]

    def callers_of(self, bid):
        b = self.mod.block(bid)
        if b is None or b.kind != "script":
            return []
        return self.callers.get(b.meta["index"], [])

    def roots_of(self, bid, limit=4000):
        """Non-script entry points (triggers, menus, dialogs, presentations,
        mission templates, engine callbacks) that transitively reach `bid`."""
        seen, roots, stack = {bid}, set(), [bid]
        while stack and len(seen) < limit:
            cur = stack.pop()
            b = self.mod.block(cur)
            if b.kind != "script":
                roots.add(cur)
                continue
            if b.owner.startswith("game_"):
                roots.add(cur)          # engine callback (called by name)
            cs = self.callers_of(cur)
            for src, _n, _bare in cs:
                if src not in seen:
                    seen.add(src)
                    stack.append(src)
        return sorted(roots)

    def closure(self, bids, limit=5000):
        """Recursive callees of the seed blocks."""
        seen, stack = set(bids), list(bids)
        while stack and len(seen) < limit:
            cur = stack.pop()
            for dst, _n, _bare in self.callees(cur):
                if dst and dst not in seen:
                    seen.add(dst)
                    stack.append(dst)
        return seen


# ------------------------------------------------------------ index cache

INDEX_VERSION = 1
_INDEX_FIELDS = ("x", "callers", "global_use", "slot_use", "ref_use", "unknown_ops")


def _index_fingerprint(mod):
    """Module fingerprint (loader source + .txt sizes/mtimes) plus the source of
    everything the index is derived with, so editing any of it rebuilds."""
    here = os.path.dirname(os.path.abspath(__file__))
    parts = [corpus._fingerprint(mod.root)]
    for f in ("analyze.py", "headers.py", "header_tables.py", "opref.py", "opref_data.py"):
        with open(os.path.join(here, f), "rb") as fh:
            parts.append(hashlib.sha1(fh.read()).hexdigest()[:12])
    return "|".join(parts)


def cached_index(mod, cache_dir):
    """ModuleIndex(mod), read from `cache_dir/<slug>.pickle` when its fingerprint
    still matches, else built and written there."""
    fp = _index_fingerprint(mod)
    path = os.path.join(cache_dir, mod.slug + ".pickle")
    if os.path.isfile(path):
        try:
            ver, cfp, data = corpus.read_pickle(path)
            if ver == INDEX_VERSION and cfp == fp:
                ix = ModuleIndex.__new__(ModuleIndex)
                ix.mod = mod
                ix.__dict__.update(data)
                return ix
        except Exception:
            pass
    ix = ModuleIndex(mod)
    os.makedirs(cache_dir, exist_ok=True)
    tmp = "%s.%d.tmp" % (path, os.getpid())
    try:
        with open(tmp, "wb") as fh:
            pickle.dump((INDEX_VERSION, fp, {k: getattr(ix, k) for k in _INDEX_FIELDS}), fh,
                        protocol=pickle.HIGHEST_PROTOCOL)
        os.replace(tmp, path)
    except BaseException:
        corpus.remove_quietly(tmp)
        raise
    return ix
