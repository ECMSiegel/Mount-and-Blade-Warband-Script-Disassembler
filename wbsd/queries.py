"""Investigation queries. Every function returns plain text lines (or data)
so the CLI, reports and future agents can share them."""
import os
import re
import types
from collections import Counter, defaultdict

from . import analyze, categories, config, registry
from .analyze import decode

_IX = {}


def get(slug):
    if slug not in _IX:
        m = registry.load(slug)
        _IX[slug] = analyze.cached_index(m, os.path.join(config.CACHE_DIR, "index"))
    return _IX[slug]


def _bare(slug):
    """Stand-in for get(slug) for callers that only touch `.mod` (no xref index)."""
    return types.SimpleNamespace(mod=registry.load(slug))


# ------------------------------------------------------------ resolution

def resolve(ix, spec):
    """Block id from a user spec: script name, `script_x`, or any block id."""
    m = ix.mod
    if m.block(spec):
        return spec
    for cand in ("script:" + spec, "script:" + spec[7:] if spec.startswith("script_") else None,
                 "menu:" + spec[5:] if spec.startswith("menu_") else None,
                 "menu:" + spec):
        if cand and m.block(cand):
            return cand
    if re.search(r"/t\d+$", spec) and m.block(spec + ":conseq"):
        return spec + ":conseq"       # mission-template trigger: default to its consequences
    if spec.isdigit() and m.script_block(int(spec)):
        return m.script_block(int(spec)).id
    hits = [b.id for b in m.blocks if spec in b.id]
    if len(hits) == 1:
        return hits[0]
    raise LookupError("no unique block for %r in %s; candidates: %s"
                      % (spec, m.slug, ", ".join(hits[:25]) or "none"))


def describe_bid(ix, bid):
    b = ix.mod.block(bid)
    if b is None:
        return bid
    meta = b.meta
    if b.kind == "strig":
        return "%s (every %sh)" % (bid, _fmt_num(meta.get("interval")))
    if b.kind in ("trig",):
        return "%s (check %sh)" % (bid, _fmt_num(meta.get("check")))
    if b.kind == "mst":
        ev = meta.get("event") or "every %ss" % _fmt_num(meta.get("check"))
        return "%s [%s]" % (bid, ev)
    if b.kind in ("prsnt", "spr", "itm", "icon"):
        return "%s [%s]" % (bid, meta.get("event") or meta.get("interval"))
    if b.kind in ("mopt", "menu", "dlg"):
        t = meta.get("text", "")
        return "%s \"%s\"" % (bid, t[:60])
    return bid


def _fmt_num(v):
    if v is None:
        return "?"
    return ("%g" % v)


# ------------------------------------------------------------ disassembly

def dis(slug, spec, raw=False):
    ix = get(slug)
    bid = resolve(ix, spec)
    b = ix.mod.block(bid)
    out = ["== %s  [%s, %d statements] %s" % (bid, ix.mod.label, len(b.stmts), _meta_line(b))]
    if raw:
        out += ["%4d  %s%d %r" % (n, ("neg|" if f & 0x80000000 else "") + ("or|" if f & 0x40000000 else ""), c, list(o))
                for n, (c, f, o) in enumerate(b.stmts)]
    else:
        out += analyze.disassemble(ix.mod, b)
    return out


def _meta_line(b):
    keep = {k: v for k, v in b.meta.items() if k in ("interval", "event", "check", "delay", "rearm", "text", "index", "desc")}
    return str(keep) if keep else ""


# ------------------------------------------------------------ call graph

def callers(slug, spec):
    ix = get(slug)
    bid = resolve(ix, spec)
    rows = ix.callers_of(bid)
    out = ["callers of %s (%d call sites):" % (bid, len(rows))]
    for src, n, bare in sorted(rows):
        out.append("  %s @%d%s" % (describe_bid(ix, src), n, " {bare-int call}" if bare else ""))
    return out


def callees(slug, spec):
    ix = get(slug)
    bid = resolve(ix, spec)
    out = ["callees of %s:" % bid]
    for dst, n, bare in ix.callees(bid):
        out.append("  @%d %s%s" % (n, dst, " {bare-int}" if bare else ""))
    return out


def tree(slug, spec, depth=3, up=False):
    ix = get(slug)
    root = resolve(ix, spec)
    out = []
    seen = set()

    def walk(bid, d, prefix):
        mark = " (seen)" if bid in seen else ""
        out.append("%s%s%s" % (prefix, describe_bid(ix, bid) if up else bid, mark))
        if bid in seen or d >= depth:
            return
        seen.add(bid)
        nxt = sorted({s for s, _n, _b in ix.callers_of(bid)}) if up else \
            [x for x in dict.fromkeys(d2 for d2, _n, _b in ix.callees(bid)) if x]
        for child in nxt:
            walk(child, d + 1, prefix + "  ")

    walk(root, 0, "")
    return out


def roots(slug, spec):
    ix = get(slug)
    bid = resolve(ix, spec)
    rs = ix.roots_of(bid)
    out = ["entry points that reach %s (%d):" % (bid, len(rs))]
    out += ["  " + describe_bid(ix, r) for r in rs]
    return out


# ------------------------------------------------------------ state

def global_use(slug, name):
    ix = get(slug)
    names = ix.mod.names.get("global", [])
    n = name.lstrip("$")
    if n in names:
        g = names.index(n)
    elif re.fullmatch(r"g\d+", n):
        g = int(n[1:])
    else:
        hits = [x for x in names if n in x]
        return ["no global %r; similar: %s" % (name, ", ".join(hits[:30]))]
    rows = ix.global_use.get(g, [])
    w = sorted({b for b, rw, _ in rows if rw == "w"})
    r = sorted({b for b, rw, _ in rows if rw == "r"})
    out = ["$%s (global #%d): %d writer blocks, %d reader blocks" % (ix.mod.name("global", g), g, len(w), len(r))]
    out.append(" WRITERS:")
    out += ["   " + describe_bid(ix, b) for b in w]
    out.append(" READERS:")
    out += ["   " + describe_bid(ix, b) for b in r]
    return out


OBJ_ALIASES = {"pt": "party_template", "prop": "scene_prop", "spr": "scene_prop"}


def slot_use(slug, objkind, slot):
    objkind = OBJ_ALIASES.get(objkind, objkind)
    ix = get(slug)
    rows = ix.slot_use.get((objkind, int(slot)), [])
    by = defaultdict(Counter)
    vals = Counter()
    for bid, access, orep, vrep, vkind, n in rows:
        by[bid][access] += 1
        if access in ("set", "eq", "ge"):
            vals[vkind if vkind != "const" else "const:" + vrep] += 1
    out = ["%s slot %s in %s: %d accesses in %d blocks" % (objkind, slot, ix.mod.label, len(rows), len(by))]
    out.append(" values written/tested: %s" % dict(vals.most_common(12)))
    for bid, c in sorted(by.items(), key=lambda kv: (-kv[1]["set"], kv[0])):
        out.append("   %-6s %s" % ("".join("%s%d " % (k[0], v) for k, v in sorted(c.items())), describe_bid(ix, bid)))
    if slug != "native":
        nrows = get("native").slot_use.get((objkind, int(slot)), [])
        out.append(" Native uses this slot: %s" % ("yes, %d accesses (e.g. %s)" % (
            len(nrows), ", ".join(sorted({r[0] for r in nrows})[:4])) if nrows else "NO (module-specific slot)"))
    return out


def slot_map(slug, objkind):
    objkind = OBJ_ALIASES.get(objkind, objkind)
    ix = get(slug)
    nat = get("native") if slug != "native" else None
    out = ["%s slots used by %s (r=get w=set t=test; N=also used by Native):" % (objkind, ix.mod.label)]
    if objkind == "troop":
        out.append("  WARNING: Native-lineage modules store troop-to-troop relations on heroes at slot = "
                   "(relations base + other troop's index), written with COMPUTED slot numbers, so low/mid "
                   "slot numbers that look free here may be live relation slots on lords/companions "
                   "(see `troop_get_relation_with_troop`).")
    slots = sorted(s for (k, s) in ix.slot_use if k == objkind and s is not None)
    for s in slots:
        rows = ix.slot_use[(objkind, s)]
        c = Counter(a for _b, a, *_ in rows)
        writers = sorted({b for b, a, *_ in rows if a == "set"})
        native = nat is not None and (objkind, s) in nat.slot_use
        out.append("  %4d %s r%-4d w%-4d t%-4d blocks=%-4d e.g. %s" % (
            s, "N" if native else " ", c["get"], c["set"], c["eq"] + c["ge"],
            len({r[0] for r in rows}), ", ".join(writers[:3])))
    dyn = ix.slot_use.get((objkind, None), [])
    if dyn:
        out.append("  computed slot numbers (variable operand): %d accesses in %d blocks" % (len(dyn), len({r[0] for r in dyn})))
    return out


def ref_use(slug, kind, name):
    ix = get(slug)
    idx = ix.mod.index(kind, name)
    if idx < 0:
        hits = [n for n in ix.mod.names.get(kind, []) if name in n]
        return ["no %s named %r; similar: %s" % (kind, name, ", ".join(hits[:30]))]
    rows = ix.ref_use.get((kind, idx), [])
    out = ["%s %s (#%d): %d references" % (kind, name, idx, len(rows))]
    for bid, role, n in sorted(rows):
        out.append("  %s @%d as %s" % (describe_bid(ix, bid), n, role))
    return out


# ------------------------------------------------------------ explain

def _closure_stats(ix, bids):
    slots, globs, res, cats, unknown, strings = Counter(), Counter(), defaultdict(Counter), Counter(), Counter(), []
    for bid in bids:
        x = ix.x[bid]
        for objkind, access, slot, orep, vrep, vkind, n in x.slots:
            slots[(objkind, slot, access)] += 1
        for g, rw, n in x.globals:
            globs[(ix.mod.name("global", g) or "g%d" % g, rw)] += 1
        for kind, idx, role, n in x.refs:
            res[kind][ix.mod.name(kind, idx) or "%s#%d" % (kind, idx)] += 1
        cats.update(categories.profile(ix.mod.block(bid)))
        unknown.update(x.unknown)
        strings += x.strings
    return slots, globs, res, cats, unknown, strings


def texts_of(ix, strings, limit=10):
    out = []
    for kind, idx in strings:
        n = ix.mod.name(kind, idx)
        t = ix.mod.texts.get(kind, {}).get(n)
        if t and t not in out:
            out.append(t)
        if len(out) >= limit:
            break
    return out


def native_status(ix, bid):
    b = ix.mod.block(bid)
    if b.kind != "script" or ix.mod.slug == "native":
        return None
    nat = _bare("native")
    nb = nat.mod.block("script:" + b.owner)
    if nb is None:
        return "NEW (no Native script of this name)"
    a = analyze.fingerprints(ix.mod, b)[1]
    c = analyze.fingerprints(nat.mod, nb)[1]
    if a == c:
        return "IDENTICAL to Native (by named statements)"
    sim = analyze.jaccard(analyze.named_set(ix.mod, b), analyze.named_set(nat.mod, nb))
    return "MODIFIED Native script: %d stmts vs Native %d, similarity %.0f%%" % (len(b.stmts), len(nb.stmts), 100 * sim)


def explain(slug, spec, deep=True):
    ix = get(slug)
    bid = resolve(ix, spec)
    b = ix.mod.block(bid)
    x = ix.x[bid]
    out = ["== EXPLAIN %s in %s" % (describe_bid(ix, bid), ix.mod.label)]
    out.append("statements: %d   params: %d   returns: %s" % (len(b.stmts), x.params, ", ".join(sorted(x.returns)) or "-"))
    ns = native_status(ix, bid)
    if ns:
        out.append("native: " + ns)
    if b.kind == "script":
        cs = ix.callers_of(bid)
        out.append("direct callers (%d): %s" % (len(cs), ", ".join(sorted({c[0] for c in cs})[:15])))
        rs = ix.roots_of(bid)
        out.append("entry points reaching it (%d):" % len(rs))
        out += ["   " + describe_bid(ix, r) for r in rs[:20]]
        if len(rs) > 20:
            out.append("   ... %d more" % (len(rs) - 20))
        if not rs:
            out.append("   NONE found -> unreachable by static call graph (dead, engine-named, or called by computed id)")
    if b.kind == "menu":
        opts = [o for o in ix.mod.blocks if o.kind == "mopt" and o.owner == b.owner]
        out.append("menu options (%d blocks; the work usually lives here): %s" % (
            len(opts), ", ".join("%s[%d]" % (o.id.split("/opt:", 1)[1], len(o.stmts)) for o in opts if o.stmts)))
    callees_ = [d for d, _n, _b in ix.callees(bid)]
    out.append("direct callees (%d): %s" % (len(set(callees_)), ", ".join(dict.fromkeys(c for c in callees_ if c))))
    clo = ix.closure([bid]) if deep else {bid}
    # sorted(): the closure is a set, so its order changed with PYTHONHASHSEED. The Counters below
    # keep insertion order, which decides ties: top-N lists (most_common) list tied names in
    # ascending block-id order of first use (count descending, ties by first use, not by name),
    # and "text shown/built" lists texts in that same first-use order.
    slots, globs, res, cats, unknown, strings = _closure_stats(ix, sorted(clo))
    out.append("closure: %d blocks (this + recursive callees)" % len(clo))
    out.append("behaviour profile (closure): %s" % categories.summary(cats, 8))
    agg = defaultdict(Counter)
    for (objkind, slot, access), n in slots.items():
        agg[(objkind, slot)][access] += n
    if agg:
        out.append("slots touched (closure): " + "; ".join(
            "%s[%s] %s" % (k[0], k[1] if k[1] is not None else "?", "".join("%s%d" % (a[0], v) for a, v in sorted(c.items())))
            for k, c in sorted(agg.items(), key=lambda kv: (kv[0][0], kv[0][1] if kv[0][1] is not None else -1))[:60]))
    gw = sorted({g for (g, rw) in globs if rw == "w"})
    gr = sorted({g for (g, rw) in globs if rw == "r"} - set(gw))
    out.append("globals written: %s" % ", ".join(gw[:40]))
    out.append("globals read-only: %s" % ", ".join(gr[:40]))
    for kind in sorted(res):
        if kind in ("string", "qstr"):
            continue
        names = res[kind]
        out.append("%s refs: %s%s" % (kind, ", ".join(n for n, _ in names.most_common(12)),
                                     " (+%d more)" % (len(names) - 12) if len(names) > 12 else ""))
    tx = texts_of(ix, strings, 8)
    if tx:
        out.append("text shown/built: " + " | ".join(t[:70] for t in tx))
    if unknown:
        out.append("NON-VANILLA OPCODES: %s  -> engine-extension dependency" % dict(unknown))
    return out


# ------------------------------------------------------------ systems

def system(slug, spec, max_fanout=25, max_blocks=120):
    """Grow a subsystem from a seed through calls AND shared state.

    Shared state links a writer of a global/slot to its readers, skipping
    hub state touched by more than `max_fanout` blocks (it couples everything
    and would swallow the module)."""
    ix = get(slug)
    seed = resolve(ix, spec)
    users_g = defaultdict(set)
    for g, rows in ix.global_use.items():
        for bid, rw, n in rows:
            users_g[g].add(bid)
    users_s = defaultdict(set)
    for key, rows in ix.slot_use.items():
        if key[1] is None:
            continue
        for r in rows:
            users_s[key].add(r[0])
    comp, frontier, why = {seed}, [seed], {seed: "seed"}
    while frontier and len(comp) < max_blocks:
        cur = frontier.pop(0)
        x = ix.x[cur]
        links = []
        links += [(d, "called by %s" % cur) for d, _n, _b in ix.callees(cur) if d]
        links += [(s, "calls %s" % cur) for s, _n, _b in ix.callers_of(cur)]
        for g, rw, n in x.globals:
            if rw == "w" and len(users_g[g]) <= max_fanout:
                links += [(o, "shares $%s" % ix.mod.name("global", g)) for o in users_g[g]]
        for objkind, access, slot, *_ in x.slots:
            key = (objkind, slot)
            if access == "set" and slot is not None and len(users_s[key]) <= max_fanout:
                links += [(o, "shares %s slot %d" % key) for o in users_s[key]]
        for nb, reason in links:
            if nb not in comp and len(comp) < max_blocks:
                comp.add(nb)
                why[nb] = reason
                frontier.append(nb)
    out = ["SYSTEM around %s in %s: %d blocks (fanout cap %d)" % (seed, ix.mod.label, len(comp), max_fanout)]
    cats = Counter()
    for bid in comp:
        cats.update(categories.profile(ix.mod.block(bid)))
    out.append("behaviour profile: " + categories.summary(cats, 8))
    for bid in sorted(comp, key=lambda b: (ix.mod.block(b).kind != "strig", b)):
        out.append("  %-70s <- %s" % (describe_bid(ix, bid)[:70], why[bid]))
    return out


# ------------------------------------------------------------ transplant closure

def closure(slug, specs, target, with_hooks=False):
    """Everything a transplant of `specs` would drag along.

    with_hooks=True also folds the entry-point blocks (the triggers / menus /
    mission-template triggers that call the seeds) into the closure, since
    their own condition and consequence code is usually part of the feature."""
    ix = get(slug)
    seeds = [resolve(ix, s) for s in specs]
    if with_hooks:
        # fold in the calling triggers/menus/etc., but not engine callbacks
        # (game_*) or game_start-style hubs, which would pull in half the module
        for s in list(seeds):
            for r in ix.roots_of(s):
                if r in seeds or r.startswith("script:game_"):
                    continue
                if len(ix.x[r].calls) > 40:
                    continue
                seeds.append(r)
    clo = ix.closure(seeds)
    t = get(target)
    out = ["TRANSPLANT CLOSURE of %s from %s into %s" % (", ".join(seeds), ix.mod.label, t.mod.label)]
    out.append("blocks in closure: %d" % len(clo))
    entry = set()
    for s in seeds:
        entry.update(ix.roots_of(s))
    out.append("entry points the feature hangs off in the donor (%d):" % len(entry))
    out += ["   " + describe_bid(ix, e) for e in sorted(entry)[:30]]
    out.append("SCRIPTS:")
    for bid in sorted(clo):
        b = ix.mod.block(bid)
        if b.kind != "script":
            continue
        tb = t.mod.block("script:" + b.owner)
        if tb is None:
            status = "ABSENT in target (must be rebuilt)"
        elif analyze.fingerprints(ix.mod, b)[1] == analyze.fingerprints(t.mod, tb)[1]:
            status = "identical in target"
        else:
            sim = analyze.jaccard(analyze.named_set(ix.mod, b), analyze.named_set(t.mod, tb))
            status = "DIFFERS in target (%.0f%% similar) -> merge conflict" % (100 * sim)
        out.append("   %-55s %4d stmts  %s" % (b.owner, len(b.stmts), status))
    # sorted(): same reason as in explain above; the set's order changed with PYTHONHASHSEED, which
    # reordered the "missing in target" lists.
    slots, globs, res, cats, unknown, strings = _closure_stats(ix, sorted(clo))
    out.append("RESOURCES (by name; ids differ per module):")
    for kind in sorted(res):
        if kind in ("string", "qstr"):
            out.append("   %s: %d distinct" % (kind, len(res[kind])))
            continue
        tnames = set(t.mod.names.get(kind, []))
        missing = [n for n in res[kind] if n not in tnames]
        out.append("   %s: %d used, %d missing in target%s" % (
            kind, len(res[kind]), len(missing), (": " + ", ".join(missing[:20]) + (" ..." if len(missing) > 20 else "")) if missing else ""))
    tg = set(t.mod.names.get("global", []))
    gnames = sorted({g for g, rw in globs})
    shared = [g for g in gnames if g in tg]
    out.append("GLOBALS: %d used; %d also exist by name in target (shared meaning OR collision -- check): %s"
               % (len(gnames), len(shared), ", ".join(shared[:40])))
    out.append("   donor-only globals: %s" % ", ".join([g for g in gnames if g not in tg][:60]))
    out.append("SLOTS (object, slot): donor access -> target usage")
    keys = sorted({(o, s) for (o, s, a) in slots if s is not None})
    for o, s in keys:
        acc = "".join("%s%d" % (a[0], slots[(o, s, a)]) for a in ("set", "get", "eq", "ge") if slots[(o, s, a)])
        trows = t.slot_use.get((o, s), [])
        if not trows:
            st = "free in target"
        else:
            twriters = sorted({r[0] for r in trows if r[1] == "set"})
            dw = sorted({bid for bid in clo for r in ix.x[bid].slots if r[0] == o and r[2] == s and r[1] == "set"})
            same = set(w.split(":", 1)[1] for w in twriters) & set(w.split(":", 1)[1] for w in dw)
            st = "USED in target by %d blocks (writers e.g. %s)%s" % (
                len({r[0] for r in trows}), ", ".join(twriters[:3]),
                " -- same-named writers, likely same meaning" if same else " -- POSSIBLE COLLISION")
        out.append("   %-14s %-5d %-12s %s" % (o, s, acc, st))
    if unknown:
        out.append("NON-VANILLA OPCODES: %s -> BLOCKER for a vanilla-engine target" % dict(unknown))
    out.append("behaviour profile: " + categories.summary(cats, 8))
    return out


# ------------------------------------------------------------ comparison

def _named_hashes(ix_or_mod):
    """script name -> named hash. Accepts a ModuleIndex or a bare Module, so
    comparisons never need to build a full xref index."""
    mod = getattr(ix_or_mod, "mod", ix_or_mod)
    h = mod.__dict__.get("_nh")
    if h is None:
        h = {}
        for b in mod.blocks:
            if b.kind == "script" and "#" not in b.id:
                h[b.owner] = analyze.fingerprints(mod, b)[1]
        mod._nh = h
    return h


def diff(a, b="native"):
    A, B = get(a), get(b)
    ha, hb = _named_hashes(A), _named_hashes(B)
    same = sorted(n for n in ha if n in hb and ha[n] == hb[n])
    changed = sorted(n for n in ha if n in hb and ha[n] != hb[n])
    only_a = sorted(n for n in ha if n not in hb)
    only_b = sorted(n for n in hb if n not in ha)
    out = ["SCRIPT DIFF %s vs %s: identical %d, modified %d, only in %s %d, only in %s %d" % (
        A.mod.label, B.mod.label, len(same), len(changed), a, len(only_a), b, len(only_b))]
    out.append("MODIFIED (stmts %s/%s, similarity):" % (a, b))
    rows = []
    for n in changed:
        ba, bb = A.mod.block("script:" + n), B.mod.block("script:" + n)
        sim = analyze.jaccard(analyze.named_set(A.mod, ba), analyze.named_set(B.mod, bb))
        rows.append((sim, n, len(ba.stmts), len(bb.stmts)))
    for sim, n, la, lb in sorted(rows):
        out.append("   %-55s %5d/%-5d %3.0f%%" % (n, la, lb, 100 * sim))
    out.append("ONLY IN %s:" % a)
    out += ["   %-55s %5d stmts  %s" % (n, len(A.mod.block("script:" + n).stmts),
                                         categories.summary(categories.profile(A.mod.block("script:" + n)), 3)) for n in only_a]
    out.append("ONLY IN %s: %s" % (b, ", ".join(only_b)))
    return out


def shape_seq(block):
    """Opcode sequence (opcode, flags, arity): survives id renumbering, local
    renumbering AND tagged-vs-untagged compilers."""
    return [(c, f, len(o)) for c, f, o in block.stmts]


def shape_ratio(a, b):
    import difflib
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    if sm.real_quick_ratio() < 0.5 or sm.quick_ratio() < 0.5:
        return sm.quick_ratio() * 0.5
    return sm.ratio()


def compare(script, slugs=None):
    slugs = slugs or registry.slugs()
    groups = defaultdict(list)
    first = None
    out = ["script %s across modules:" % script]
    for s in slugs:
        m = registry.load(s)
        b = m.block("script:" + script)
        if b is None:
            out.append("   %-8s absent" % s)
            continue
        h = analyze.fingerprints(m, b)[1]
        groups[h].append(s)
        if first is None:
            first = (s, shape_seq(b))
            shape = "reference"
        else:
            shape = "shape %3.0f%% vs %s" % (100 * shape_ratio(first[1], shape_seq(b)), first[0])
        out.append("   %-8s %5d stmts  variant %s  %s" % (s, len(b.stmts), h[:6], shape))
    out.append("variants (identical by named statements): " + "; ".join("%s" % ",".join(v) for v in groups.values()))
    out.append("(shape = opcode-sequence similarity; ~100% with different variants means the same code "
               "with different ids, e.g. a tag-less compiler or renumbered content)")
    return out


def similar(slug, spec, top=12, slugs=None, min_sim=0.25):
    ix = _bare(slug)
    bid = resolve(ix, spec)
    b0 = ix.mod.block(bid)
    base = analyze.named_set(ix.mod, b0)
    base_total = len(b0.stmts)
    # a statement can only equal a base statement if code, flags and operand
    # count match, so the (costly) named form is built only for those
    base_keys = {(c, f, len(o)) for c, f, o in b0.stmts}
    seq0 = shape_seq(b0)
    res = []
    for s in (slugs or registry.slugs()):
        om = registry.load(s)
        for b in om.blocks:
            if b.kind != "script" or (s == slug and b.id == bid):
                continue
            nb = len(b.stmts)
            if abs(nb - base_total) > 3 * max(nb, 10):
                continue
            if base_total and nb:
                cnt = Counter(analyze.named_stmt(om, st) for st in b.stmts
                              if (st[0], st[1], len(st[2])) in base_keys)
                inter = sum(min(v, base[k]) for k, v in cnt.items())
                sim = inter / float(base_total + nb - inter)
            else:
                sim = analyze.jaccard(base, analyze.named_set(om, b))
            shp = 0.0
            n0, n1 = len(seq0), nb
            if min(n0, n1) >= 0.6 * max(n0, n1):
                shp = shape_ratio(seq0, shape_seq(b))
            if max(sim, shp) >= min_sim:
                res.append((max(sim, shp), sim, shp, s, b.owner, nb))
    res.sort(reverse=True)
    out = ["scripts most similar to %s:%s (named = named-statement Jaccard; shape = opcode-sequence match):" % (slug, bid)]
    out += ["   named %3.0f%%  shape %3.0f%%  %-8s %-48s %d stmts" % (100 * a, 100 * b_, s, n, l)
            for _m, a, b_, s, n, l in res[:top]]
    return out


def lineage(slugs=None):
    slugs = slugs or registry.slugs()
    hs = {s: _named_hashes(registry.load(s)) for s in slugs}
    out = ["LINEAGE: % of ROW module's scripts that are byte-identical (named) in COLUMN module"]
    out.append("         " + " ".join("%7s" % s for s in slugs))
    for a in slugs:
        row = []
        for b in slugs:
            ha, hb = hs[a], set(hs[b].values())
            row.append(100.0 * sum(1 for v in ha.values() if v in hb) / max(len(ha), 1))
        out.append("%-8s " % a + " ".join("%7.0f" % v for v in row))
    return out


# ------------------------------------------------------------ hooks / entry points

def hooks(slug, kinds=("strig", "trig", "mst", "prsnt")):
    ix = get(slug)
    out = ["ENTRY POINTS in %s (callees shown)" % ix.mod.label]
    for b in ix.mod.blocks:
        if b.kind not in kinds or not b.stmts:
            continue
        cs = [d.split(":", 1)[1] for d, _n, _b in ix.callees(b.id) if d]
        prof = categories.summary(categories.profile(b), 3)
        out.append("  %-60s %3d stmts  calls: %s  | %s" % (describe_bid(ix, b.id)[:60], len(b.stmts),
                                                          ", ".join(dict.fromkeys(cs)) or "-", prof))
    return out


# ------------------------------------------------------------ text & grep

def text(query, slugs=None, limit=40):
    rx = re.compile(query, re.I)
    out = []
    for s in (slugs or registry.slugs()):
        ix = get(s)
        hits = []
        for kind in ("string", "qstr"):
            for name, t in ix.mod.texts.get(kind, {}).items():
                if rx.search(t) or rx.search(name):
                    idx = ix.mod.index(kind, name)
                    users = sorted({r[0] for r in ix.ref_use.get((kind, idx), [])})
                    hits.append("%s %s \"%s\" used by: %s" % (kind, name, t[:80], ", ".join(users[:4]) or "-"))
        for b in ix.mod.blocks:
            if b.kind in ("menu", "mopt") and b.part.endswith((":cond",)) is False and rx.search(b.meta.get("text", "")):
                hits.append("%s \"%s\"" % (b.id, b.meta["text"][:80]))
            elif b.kind == "dlg" and b.part == "conseq" and rx.search(b.meta.get("text", "")):
                hits.append("%s \"%s\"" % (b.id, b.meta["text"][:80]))
        if hits:
            out.append("== %s: %d hits" % (s, len(hits)))
            out += ["   " + h for h in hits[:limit]]
    return out


def grep(pattern, slugs=None, kinds=None, limit=60):
    rx = re.compile(pattern)
    out = []
    for s in (slugs or registry.slugs()):
        mod = registry.load(s)
        n = 0
        for b in mod.blocks:
            if kinds and b.kind not in kinds:
                continue
            for line in analyze.disassemble(mod, b, numbered=True):
                if rx.search(line):
                    out.append("%s  %s  %s" % (s, b.id, line.strip()))
                    n += 1
                    break
            if n >= limit:
                out.append("%s  ... (limit %d blocks)" % (s, limit))
                break
    return out


def batch(lines):
    """Run many CLI lines in ONE process (indexes built once). Each line is a
    normal wbsd command, e.g. `explain vc spawn_bandits`."""
    import shlex
    from . import wbsd as cli
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        print("\n>>> " + line)
        cli.main(["wbsd.py"] + shlex.split(line))
    return []
