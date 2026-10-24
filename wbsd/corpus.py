"""Read-only, token-stream loaders for every compiled Warband table.

Unlike `wbasm.py` (which round-trips a module's files byte-for-byte so that
tools can WRITE them), these loaders only READ, and they read by token stream
rather than by line pairing, so a module whose script body wraps onto a second
line still parses. Nothing here writes.

A loaded Module exposes:
  names[kind]  -> list of record ids, index == compiled id   (kinds: see TABLES)
  blocks       -> list of Block: every bytecode block in the module, with an
                  owner id such as `script:game_start`, `strig:12`,
                  `mst:lead_charge/t3:conseq`, `menu:town/opt:trade:cond`.
  errors       -> per-table parse problems (never raised; reported)
"""
import gc
import json
import os
import pickle
import re

from . import headers

CACHE_VERSION = 4


class Block(object):
    """One bytecode block. stmts: list of (opcode, flags, operands_tuple)."""
    __slots__ = ("id", "kind", "owner", "part", "stmts", "meta")

    def __init__(self, bid, kind, owner, part, stmts, meta=None):
        self.id = bid
        self.kind = kind          # script strig trig menu mopt dlg prsnt mst spr itm icon tab
        self.owner = owner        # owning record id (script name, menu id, ...)
        self.part = part          # body / cond / conseq / t<k> ...
        self.stmts = stmts
        self.meta = meta or {}


class Tokens(object):
    __slots__ = ("t", "i", "version")

    def __init__(self, data):
        self.t = data.split()
        self.i = 0

    def next(self):
        v = self.t[self.i]
        self.i += 1
        return v

    def int(self):
        return int(self.next())

    def float(self):
        return float(self.next())

    def str(self):
        return self.next().decode("latin-1")

    def done(self):
        return self.i >= len(self.t)

    def stmts(self, n=None):
        if n is None:
            n = self.int()
        out = []
        t = self.t
        i = self.i
        for _ in range(n):
            raw = int(t[i])
            cnt = int(t[i + 1])
            ops = tuple(int(x) for x in t[i + 2:i + 2 + cnt])
            if len(ops) != cnt:
                raise ValueError("truncated statement")
            out.append((raw & 0x3FFFFFFF if raw >= 0 else raw, raw & 0xC0000000 if raw >= 0 else 0, ops))
            i += 2 + cnt
        self.i = i
        return out


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


def _skip_header(tok):
    """Skip a `xxxfile version N` header if present; return declared count.

    The header's version number is kept on tok.version (0 when absent):
    older-format modules (some mods compiled with an older Module System omit type tags) ship
    `dialogsfile version 1` (no voice-over field) and `itemsfile version 2`
    (no per-item faction list)."""
    tok.version = 0
    if tok.t and not tok.t[0].lstrip(b"-").isdigit():
        tok.version = int(tok.t[2])
        tok.i = 3
    return tok.int()


# ---------------------------------------------------------------- names only

def _declared(data):
    t = data.split(None, 4)[:4]
    try:
        return int(t[3]) if not t[0].lstrip(b"-").isdigit() else int(t[0])
    except (IndexError, ValueError):
        return None


def _names_by_regex(data, pattern):
    rx = re.compile(pattern, re.M)
    return [m.group(1).decode("latin-1") for m in rx.finditer(data)]


NAME_PATTERNS = {
    "troop": ("troops.txt", rb"^\s*(trp_\S+)"),
    "party": ("parties.txt", rb"^\s*\d+ \d+ \d+ (p_\S+)"),
    "pt": ("party_templates.txt", rb"^\s*(pt_\S+)"),
    "faction": ("factions.txt", rb"^\s*(?:\d+\s+)?(fac_\S+)"),
    "quest": ("quests.txt", rb"^\s*(qst_\S+)"),
    "string": ("strings.txt", rb"^\s*(str_\S+)"),
    "qstr": ("quick_strings.txt", rb"^\s*(qstr_\S+)"),
    "sound": ("sounds.txt", rb"^\s*(snd_\S+)"),
    "psys": ("particle_systems.txt", rb"^\s*(psys_\S+)"),
    "mesh": ("meshes.txt", rb"^\s*(mesh_\S+)"),
    "skill": ("skills.txt", rb"^\s*(skl_\S+)"),
    "infopage": ("info_pages.txt", rb"^\s*(ip_\S+)"),
    "scene": ("scenes.txt", rb"^\s*(scn_\S+)"),
    "postfx": ("postfx.txt", rb"^\s*(pfx_\S+)"),
    "mt": ("mission_templates.txt", rb"^\s*(mst_\S+)"),
    "menu": ("menus.txt", rb"^\s*(menu_\S+)"),
    "prsnt": ("presentations.txt", rb"^\s*(prsnt_\S+)"),
    "spr": ("scene_props.txt", rb"^\s*(spr_\S+)"),
    "tableau": ("tableau_materials.txt", rb"^\s*(tab_\S+)"),
}


def _plain_lines(data):
    return [ln.strip().decode("latin-1") for ln in data.splitlines() if ln.strip()]


# ------------------------------------------------------------ block loaders

def _load_scripts(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    names = []
    seen = set()
    for _rec in range(count):
        name = tok.str()
        flag = tok.next()
        names.append(name)
        st = tok.stmts()
        # Duplicate script names exist in real modules (call_script is by
        # index, so both copies can be live); the second gets a #index id.
        bid = "script:" + name
        if name in seen:
            bid = "script:%s#%d" % (name, len(names) - 1)
        seen.add(name)
        mod.blocks.append(Block(bid, "script", name, "body", st,
                                {"index": len(names) - 1, "flag": flag.decode()}))
    mod.names["script"] = names


def _load_simple_triggers(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    k = 0
    for _rec in range(count):
        interval = tok.float()
        st = tok.stmts()
        mod.blocks.append(Block("strig:%d" % k, "strig", str(k), "body", st,
                                {"interval": interval}))
        k += 1


def _load_triggers(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    k = 0
    for _rec in range(count):
        check, delay, rearm = tok.float(), tok.float(), tok.float()
        c = tok.stmts()
        q = tok.stmts()
        meta = {"check": check, "delay": delay, "rearm": rearm}
        mod.blocks.append(Block("trig:%d:cond" % k, "trig", str(k), "cond", c, meta))
        mod.blocks.append(Block("trig:%d:conseq" % k, "trig", str(k), "conseq", q, meta))
        k += 1


def _load_menus(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    names = []
    texts = {}
    for _rec in range(count):
        mid = tok.str()
        flags = tok.next()
        text = tok.str()
        mesh = tok.str()
        st = tok.stmts()
        names.append(mid)
        texts[mid] = text
        mod.blocks.append(Block(mid.replace("menu_", "menu:", 1), "menu", mid, "body", st,
                                {"text": text, "index": len(names) - 1}))
        nopt = tok.int()
        for _ in range(nopt):
            oid = tok.str()
            c = tok.stmts()
            otext = tok.str()
            q = tok.stmts()
            door = tok.str()
            base = "%s/opt:%s" % (mid.replace("menu_", "menu:", 1), oid.replace("mno_", "", 1))
            meta = {"text": otext, "door": door}
            mod.blocks.append(Block(base + ":cond", "mopt", mid, oid + ":cond", c, meta))
            mod.blocks.append(Block(base + ":conseq", "mopt", mid, oid + ":conseq", q, meta))
    mod.names["menu"] = names
    mod.texts["menu"] = texts


def _load_presentations(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    names = []
    for _rec in range(count):
        pid = tok.str()
        tok.next()           # flags
        tok.next()           # mesh
        n = tok.int()
        names.append(pid)
        for k in range(n):
            interval = tok.float()
            st = tok.stmts()
            ev = headers.TRIGGER_EVENTS.get(interval)
            mod.blocks.append(Block("%s/t%d" % (pid.replace("prsnt_", "prsnt:", 1), k), "prsnt",
                                    pid, "t%d" % k, st, {"interval": interval, "event": ev}))
    mod.names["prsnt"] = names


def _load_mission_templates(mod, data):
    lines = data.split(b"\n")
    starts = [i for i, ln in enumerate(lines) if ln.startswith(b"mst_")]
    names = []
    for n, s in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        head = lines[s].split()
        mid = head[0].decode("latin-1")
        names.append(mid)
        desc = lines[s + 1].strip().decode("latin-1") if s + 1 < end else ""
        tok = Tokens(b"\n".join(lines[s + 2:end]))
        nent = tok.int()
        for _ in range(nent):
            for _f in range(5):
                tok.next()
            nitems = tok.int()
            tok.i += nitems
        ntrig = tok.int()
        base = mid.replace("mst_", "mst:", 1)
        for k in range(ntrig):
            check, delay, rearm = tok.float(), tok.float(), tok.float()
            c = tok.stmts()
            q = tok.stmts()
            meta = {"check": check, "delay": delay, "rearm": rearm,
                    "event": headers.TRIGGER_EVENTS.get(check), "desc": desc}
            mod.blocks.append(Block("%s/t%d:cond" % (base, k), "mst", mid, "t%d:cond" % k, c, meta))
            mod.blocks.append(Block("%s/t%d:conseq" % (base, k), "mst", mid, "t%d:conseq" % k, q, meta))
    mod.names["mt"] = names


def _load_conversation(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    k = 0
    for _rec in range(count):
        did = tok.str()
        partner = tok.int()
        start = tok.int()
        c = tok.stmts()
        text = tok.str()
        end = tok.int()
        q = tok.stmts()
        if tok.version >= 2:
            tok.next()      # voice-over (dialogsfile version 2+)
        meta = {"text": text, "partner": partner, "start": start, "end": end}
        mod.blocks.append(Block("dlg:%d:%s:cond" % (k, did), "dlg", did, "cond", c, meta))
        mod.blocks.append(Block("dlg:%d:%s:conseq" % (k, did), "dlg", did, "conseq", q, meta))
        k += 1


def _load_triggered_records(mod, data, kind, read_head):
    """scene_props / map_icons: <head...> <ntriggers> (<interval> <stmts>)*"""
    tok = Tokens(data)
    count = _skip_header(tok)
    names = []
    for _rec in range(count):
        rid = read_head(tok)
        names.append(rid)
        n = tok.int()
        for k in range(n):
            interval = tok.float()
            st = tok.stmts()
            mod.blocks.append(Block("%s:%s/t%d" % (kind, rid, k), kind, rid, "t%d" % k, st,
                                    {"interval": interval,
                                     "event": headers.TRIGGER_EVENTS.get(interval)}))
    return names


def _spr_head(tok):
    rid = tok.str()
    tok.i += 4       # flags hit_points mesh physics
    return rid


def _icon_head(tok):
    rid = tok.str()
    tok.i += 7       # flags mesh scale sound offx offy offz
    return rid


def _load_items(mod, data):
    tok = Tokens(data)
    count = _skip_header(tok)
    names = []
    for _rec in range(count):
        rid = tok.str()
        tok.i += 2                       # name, plural
        nmesh = tok.int()
        tok.i += 2 * nmesh
        tok.i += 17                      # flags caps price modbits weight abundance + 11 stats
        if tok.version >= 3:
            nfac = tok.int()        # faction list (itemsfile version 3+)
            tok.i += nfac
        names.append(rid)
        n = tok.int()
        for k in range(n):
            interval = tok.float()
            st = tok.stmts()
            mod.blocks.append(Block("itm:%s/t%d" % (rid, k), "itm", rid, "t%d" % k, st,
                                    {"interval": interval,
                                     "event": headers.TRIGGER_EVENTS.get(interval)}))
    mod.names["item"] = names


def _load_tableaus(mod, data):
    names = []
    for ln in data.splitlines()[1:]:
        if not ln.strip():
            continue
        tok = Tokens(ln)
        rid = tok.str()
        tok.i += 8
        st = tok.stmts()
        names.append(rid)
        mod.blocks.append(Block("tab:" + rid, "tab", rid, "body", st, {}))
    mod.names["tableau"] = names


def _anim_names(data):
    out = []
    for ln in data.splitlines()[1:]:
        t = ln.split()
        if len(t) == 4 and b"." not in t[0] and t[3].isdigit():
            out.append(t[0].decode("latin-1"))
    return out


def _music_names(data):
    out = []
    for ln in data.splitlines()[1:]:
        t = ln.split()
        if t:
            out.append(os.path.splitext(t[0].decode("latin-1"))[0])
    return out


def _quick_string_texts(data):
    out = {}
    for ln in data.splitlines()[1:]:
        t = ln.split(None, 1)
        if t and t[0].startswith(b"qstr_"):
            out[t[0].decode("latin-1")] = t[1].strip().decode("latin-1") if len(t) > 1 else ""
    return out


def _string_texts(data):
    out = {}
    for ln in data.splitlines():
        t = ln.split(None, 1)
        if t and t[0].startswith(b"str_"):
            out[t[0].decode("latin-1")] = t[1].strip().decode("latin-1") if len(t) > 1 else ""
    return out


BLOCK_TABLES = [
    ("scripts.txt", _load_scripts),
    ("simple_triggers.txt", _load_simple_triggers),
    ("triggers.txt", _load_triggers),
    ("menus.txt", _load_menus),
    ("presentations.txt", _load_presentations),
    ("mission_templates.txt", _load_mission_templates),
    ("conversation.txt", _load_conversation),
    ("item_kinds1.txt", _load_items),
    ("tableau_materials.txt", _load_tableaus),
    ("scene_props.txt", lambda m, d: m.names.__setitem__(
        "spr", _load_triggered_records(m, d, "spr", _spr_head))),
    ("map_icons.txt", lambda m, d: m.names.__setitem__(
        "icon", _load_triggered_records(m, d, "icon", _icon_head))),
]


class Module(object):
    def __init__(self, slug, root, label=None):
        self.slug = slug
        self.root = root
        self.label = label or slug
        self.names = {}
        self.texts = {}
        self.blocks = []
        self.errors = {}
        self.notes = []

    # -- lookups ---------------------------------------------------------
    def name(self, kind, idx):
        lst = self.names.get(kind)
        if lst is not None and 0 <= idx < len(lst):
            return lst[idx]
        return None

    def index(self, kind, name):
        lst = self.names.get(kind) or []
        try:
            return lst.index(name)
        except ValueError:
            return -1

    def block(self, bid):
        idx = self.__dict__.get("_bidx")
        if idx is None:
            idx = self._bidx = {b.id: b for b in self.blocks}
        return idx.get(bid)

    def script_block(self, idx):
        """Block of script number `idx` (handles duplicate names)."""
        sb = self.__dict__.get("_sidx")
        if sb is None:
            sb = self._sidx = {b.meta["index"]: b for b in self.blocks if b.kind == "script"}
        return sb.get(idx)

    def script(self, name):
        if not name.startswith("script:"):
            name = "script:" + (name[7:] if name.startswith("script_") else name)
        return self.block(name)


def _path(root, fname):
    p = os.path.join(root, fname)
    if os.path.isfile(p):
        return p
    # case-insensitive fallback (some mods ship Scripts.txt etc.)
    low = fname.lower()
    for f in os.listdir(root):
        if f.lower() == low:
            return os.path.join(root, f)
    return None


HEADER_TABLES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "header_tables.py")


def _fingerprint(root):
    # The loader's own source is part of the key, so editing this file
    # (or headers.py) invalidates every cached parse automatically.
    import hashlib
    # headers.py and the generated header_tables.py (TRIGGER_EVENTS, operand
    # tags) feed the parse too.
    parts = []
    for src in (os.path.abspath(__file__), os.path.abspath(headers.__file__),
                HEADER_TABLES):
        with open(src, "rb") as fh:
            parts.append(hashlib.sha1(fh.read()).hexdigest()[:12])
    for f in sorted(os.listdir(root)):
        if f.endswith(".txt"):
            st = os.stat(os.path.join(root, f))
            parts.append("%s:%d:%d" % (f, st.st_size, st.st_mtime_ns))
    return "|".join(parts)


def remove_quietly(path):
    """Delete a leftover temp file after a failed cache write (never raises)."""
    try:
        os.remove(path)
    except OSError:
        pass


def read_pickle(path):
    """Unpickle `path` with the garbage collector paused (it otherwise re-scans
    the millions of tuples being built, about a third of the load time), then
    freeze the result so later collections skip it."""
    was = gc.isenabled()
    gc.disable()
    try:
        with open(path, "rb") as fh:
            return pickle.load(fh)
    finally:
        if was:
            gc.enable()
        gc.freeze()


def stats_path(slug, cache_dir):
    return os.path.join(cache_dir, slug + ".stats.json")


def stats(slug, root, label=None, cache_dir=None):
    """(scripts, blocks, statements, errors) of a module without unpickling it.

    A small sidecar next to the parse cache holds the numbers, keyed on the same
    fingerprint as the pickle; if it is missing or stale the module is loaded
    (which rewrites it)."""
    fp = _fingerprint(root)
    sp = stats_path(slug, cache_dir) if cache_dir else None
    if sp and os.path.isfile(sp):
        try:
            with open(sp, encoding="utf-8") as fh:
                d = json.load(fh)
            if d.get("version") == CACHE_VERSION and d.get("fingerprint") == fp:
                return d["scripts"], d["blocks"], d["stmts"], d["errors"]
        except Exception:
            pass
    m = load(slug, root, label, cache_dir=cache_dir)
    if sp:
        _write_stats(sp, fp, m)
    return (len(m.names.get("script", [])), len(m.blocks),
            sum(len(b.stmts) for b in m.blocks), m.errors)


def _write_stats(sp, fp, mod):
    d = {"version": CACHE_VERSION, "fingerprint": fp,
         "scripts": len(mod.names.get("script", [])), "blocks": len(mod.blocks),
         "stmts": sum(len(b.stmts) for b in mod.blocks), "errors": mod.errors}
    tmp = "%s.%d.tmp" % (sp, os.getpid())
    try:
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(d, fh)
        os.replace(tmp, sp)
    except BaseException:
        remove_quietly(tmp)
        raise


def load(slug, root, label=None, cache_dir=None):
    """Load a module, using a pickle cache keyed on the .txt files' size+mtime."""
    fp = _fingerprint(root)
    cache = None
    if cache_dir:
        os.makedirs(cache_dir, exist_ok=True)
        cache = os.path.join(cache_dir, slug + ".pickle")
        if os.path.isfile(cache):
            try:
                ver, cfp, mod = read_pickle(cache)
                if ver == CACHE_VERSION and cfp == fp:
                    return mod
            except Exception:
                pass
    mod = Module(slug, root, label)
    for kind, (fname, pat) in NAME_PATTERNS.items():
        p = _path(root, fname)
        if p:
            try:
                data = _read(p)
                found = _names_by_regex(data, pat)
                declared = _declared(data)
                if kind not in ("sound", "mt") and declared is not None and len(found) > declared:
                    mod.notes.append("%s: %d records present but %d declared; the engine "
                                     "reads only the declared count" % (fname, len(found), declared))
                    found = found[:declared]
                mod.names[kind] = found
            except Exception as e:  # pragma: no cover - reported, not raised
                mod.errors[fname] = repr(e)
    for kind, fname, fn in (("global", "variables.txt", _plain_lines),
                            ("dstate", "dialog_states.txt", _plain_lines),
                            ("anim", "actions.txt", _anim_names),
                            ("track", "music.txt", _music_names)):
        p = _path(root, fname)
        if p:
            mod.names[kind] = fn(_read(p))
    p = _path(root, "quick_strings.txt")
    if p:
        mod.texts["qstr"] = _quick_string_texts(_read(p))
    p = _path(root, "strings.txt")
    if p:
        mod.texts["string"] = _string_texts(_read(p))
    for fname, fn in BLOCK_TABLES:
        p = _path(root, fname)
        if not p:
            continue
        try:
            fn(mod, _read(p))
        except Exception as e:
            mod.errors[fname] = "%s: %r" % (type(e).__name__, e)
    if cache:
        # atomic write: concurrent readers never see a half-written pickle
        tmp = "%s.%d.tmp" % (cache, os.getpid())
        try:
            with open(tmp, "wb") as fh:
                pickle.dump((CACHE_VERSION, fp, mod), fh, protocol=pickle.HIGHEST_PROTOCOL)
            os.replace(tmp, cache)
        except BaseException:
            remove_quietly(tmp)
            raise
        _write_stats(stats_path(slug, cache_dir), fp, mod)
    return mod
