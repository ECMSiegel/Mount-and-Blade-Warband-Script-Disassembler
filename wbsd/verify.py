"""Verification pack: `wbsd verify-port` and `wbsd check-log`.

verify-port BASE_DIR TARGET_DIR [--expect S,...] [--allow-edit S,...] [--touched FILE,...]
                                [--assume-reached S,...]
    BASE_DIR is the module folder before a port, TARGET_DIR the same module after it.
    Prints one PASS or FAIL line per check, then a summary. Exit 0 only if every check passes.

      append-only  every name list (scripts, troops, items, ...) in TARGET starts with BASE's list, so
                   no id moved; no table has fewer records; the dialogs, triggers and simple
                   triggers of BASE are an ordered, unchanged prefix of TARGET's (an inserted,
                   reordered or edited one fails); the body of every BASE script is unchanged
                   (same statements and flag) unless it is named in --allow-edit. A table that
                   fails to parse, in either folder, also fails this check. Long lists of
                   the same problem print the first few, then "... and N more".
      untouched    every file BASE has is still in TARGET. A file that differs must be one the
                   port may write: the file names in wbport.TABLES (a built-in copy of that list
                   when wbport cannot be imported) plus any --touched FILE names; any other
                   differing file is a FAIL. A file that may be written but whose tokens are all
                   the same (only line endings, spacing or a trailing newline changed) is a FAIL
                   too. wbport leftovers (*.bak_before_*, ports.log.jsonl) are INFO only.
      reachable    every script that is new in TARGET, plus every script named in --expect, has a
                   path from an entry point: a trigger, simple trigger, menu or menu option,
                   dialog line, presentation, mission-template trigger, item, scene-prop or
                   map-icon trigger, or an engine hook. Uses the same caller graph as `wbsd roots`.
                   An engine hook is a game_* script whose name already exists in BASE; a NEW
                   game_* script is not trusted by its name and always fails (--expect and
                   --assume-reached do not rescue it; call it from an existing entry point).
      opcodes      no opcode missing from the opcode reference appears in a block that is new or
                   differs from BASE (blocks are matched by id and occurrence, so repeated ids
                   such as menu options are not mistaken for changes).

    Limitation (also printed): a call_script whose script id sits in a variable cannot be traced.
    A script reached only that way is reported unreachable. --assume-reached S,... waives it
    explicitly; the names are printed on a "WAIVED (assumed reached)" line. --expect only adds
    scripts (new or old) to the set that must be reachable; it never waives anything.
    A name given to --allow-edit or --assume-reached that does not exist prints a WARN line.

check-log RGL_LOG
    Scans a Warband rgl_log.txt. Prints each matching record as `line N [kind] text`. Exit 1 if
    any record is an error kind, else 0. Matching is case-insensitive. A physical line holding
    several glued records is split before each of: SCRIPT ERROR ON OPCODE, "unable to ...",
    "couldn't load", "get_object failed". Each piece is reported under the first kind that matches:

      script-error  script\\s+error\\s+on\\s+opcode         e.g. "SCRIPT ERROR ON OPCODE 506: ..."
      invalid-id    \\binvalid\\b.{0,40}?\\bids?\\b           e.g. "Invalid Troop ID: 912"
      unable-to-map unable\\s+to\\s+map\\b                 e.g. "UNABLE TO MAP GAME PRESENTATION CODE"
      cosmetic      a missing-file pattern (below) on a piece that also names a material, texture
                    or mesh; reported and counted but does NOT set exit 1
      missing-file  unable\\s+to\\s+(?:find|open|load)\\b
                    \\b(?:cannot|can't|could\\s+not|failed\\s+to)\\s+(?:find|open|load)\\b
                    couldn't\\s+load\\b      get_object\\s+failed
                    file\\s+not\\s+found
                    \\bmissing\\s+(?:file|resource|texture|mesh|sound)\\b     (any one of these)

    At most 200 error pieces and 20 cosmetic ones are printed; the totals always cover the log.
"""
import filecmp
import hashlib
import os
import re

_MISSING = re.compile(
    r"unable\s+to\s+(?:find|open|load)\b"
    r"|\b(?:cannot|can't|could\s+not|failed\s+to)\s+(?:find|open|load)\b"
    r"|couldn't\s+load\b|get_object\s+failed"
    r"|file\s+not\s+found"
    r"|\bmissing\s+(?:file|resource|texture|mesh|sound)\b", re.I)
_COSMETIC_WORDS = re.compile(r"\b(?:material|texture|mesh)", re.I)
_SPLIT = re.compile(r"(?=script\s+error\s+on\s+opcode|unable\s+to\s+\w|couldn't\s+load|get_object\s+failed)", re.I)
LOG_PATTERNS = (
    ("script-error", re.compile(r"script\s+error\s+on\s+opcode", re.I)),
    ("invalid-id", re.compile(r"\binvalid\b.{0,40}?\bids?\b", re.I)),
    ("unable-to-map", re.compile(r"unable\s+to\s+map\b", re.I)),
)
LOG_KINDS = ("script-error", "invalid-id", "unable-to-map", "missing-file", "cosmetic")
LOG_LINE_CAP = 200
COSMETIC_CAP = 20
REPEAT_CAP = 10          # same-problem detail lines printed before "... and N more"

DEFAULT_TABLE_FILES = ("scripts.txt", "simple_triggers.txt", "triggers.txt", "menus.txt", "conversation.txt",
                       "presentations.txt", "mission_templates.txt", "tableau_materials.txt")


def _classify(piece):
    for kind, rx in LOG_PATTERNS:
        if rx.search(piece):
            return kind
    if _MISSING.search(piece):
        return "cosmetic" if _COSMETIC_WORDS.search(piece) else "missing-file"
    return None


def check_log(path):
    """(lines, ok). ok is False when the log has any error-kind record (cosmetic ones never fail it)."""
    try:
        with open(path, "rb") as fh:
            data = fh.read()
    except OSError as e:
        raise LookupError("cannot read %s: %s" % (path, e.strerror or e))
    lines = data.decode("latin-1").splitlines()
    hits, totals = [], {k: 0 for k in LOG_KINDS}
    for n, raw in enumerate(lines, 1):
        for piece in _SPLIT.split(raw):
            kind = _classify(piece)
            if kind:
                totals[kind] += 1
                hits.append((n, kind, piece.strip()))
    errors = [h for h in hits if h[1] != "cosmetic"]
    cosmetic = [h for h in hits if h[1] == "cosmetic"]
    out = ["line %d [%s] %s" % (n, kind, text[:240]) for n, kind, text in errors[:LOG_LINE_CAP]]
    if len(errors) > LOG_LINE_CAP:
        out.append("... %d more error lines not shown" % (len(errors) - LOG_LINE_CAP))
    out += ["line %d [%s] %s" % (n, kind, text[:240]) for n, kind, text in cosmetic[:COSMETIC_CAP]]
    if len(cosmetic) > COSMETIC_CAP:
        out.append("... %d more cosmetic lines not shown" % (len(cosmetic) - COSMETIC_CAP))
    totals_text = ", ".join("%s=%d" % (k, totals[k]) for k in LOG_KINDS)
    out.append("check-log %s: %d errors, %d cosmetic (not counted) in %d lines (%s)" % (
        "FAIL" if errors else "OK", len(errors), len(cosmetic), len(lines), totals_text))
    return out, not errors


# ------------------------------------------------------------ verify-port

def _load(folder, tag, cache_dir):
    from . import corpus
    root = os.path.abspath(folder)
    if not os.path.isdir(root):
        raise LookupError("not a folder: %s" % folder)
    slug = "verify-%s-%s" % (tag, hashlib.sha1(root.encode("utf-8", "replace")).hexdigest()[:8])
    return corpus.load(slug, root, os.path.basename(root), cache_dir=cache_dir)


FILE_LIST_CAP = 20


def _short(items, cap=8):
    items = list(items)
    s = ", ".join(str(i) for i in items[:cap])
    return s + (", ... (+%d more)" % (len(items) - cap) if len(items) > cap else "")


def _capped(lines, cap=REPEAT_CAP):
    """First `cap` lines, then one "... and N more" line."""
    lines = list(lines)
    if len(lines) <= cap:
        return lines
    return lines[:cap] + ["... and %d more" % (len(lines) - cap)]


def _script_key(name):
    return name[7:] if name.startswith("script_") else name


def _kind_counts(mod):
    c = {}
    for b in mod.blocks:
        c[b.kind] = c.get(b.kind, 0) + 1
    return c


def _meta_key(b):
    return sorted((k, repr(v)) for k, v in b.meta.items())


def _check_append_only(base, target, allow_edit):
    bad, warn = [], []
    for label, m in (("BASE", base), ("TARGET", target)):
        for fname, err in sorted(m.errors.items()):
            bad.append("%s table %s did not parse (%s); nothing about it can be proved" % (label, fname, err))
    for kind, bl in sorted(base.names.items()):
        tl = target.names.get(kind, [])
        if len(tl) < len(bl):
            bad.append("%s: TARGET has %d records, BASE has %d" % (kind, len(tl), len(bl)))
        diffs = [i for i, (a, b) in enumerate(zip(bl, tl)) if a != b]
        if diffs:
            i = diffs[0]
            bad.append("%s #%d: BASE has %s, TARGET has %s (an id moved or was renamed)" % (kind, i, bl[i], tl[i]))
            if len(diffs) > 1:
                bad.append("... and %d more differing positions in %s" % (len(diffs) - 1, kind))
    bc, tc = _kind_counts(base), _kind_counts(target)
    for kind, n in sorted(bc.items()):
        if tc.get(kind, 0) < n:
            bad.append("%s blocks: TARGET has %d, BASE has %d" % (kind, tc.get(kind, 0), n))
    # order matters for dialogs, triggers and simple triggers: BASE's must be an unchanged prefix
    for kind in ("dlg", "trig", "strig"):
        bb = [b for b in base.blocks if b.kind == kind]
        tb = [b for b in target.blocks if b.kind == kind]
        diffs = [(x, y) for x, y in zip(bb, tb)
                 if (x.id, x.stmts, _meta_key(x)) != (y.id, y.stmts, _meta_key(y))]
        if diffs:
            x, y = diffs[0]
            bad.append("%s order/content: BASE has %s, TARGET has %s at the same position (inserted, "
                       "reordered or edited)" % (kind, x.id, y.id))
            if len(diffs) > 1:
                bad.append("... and %d more differing %s blocks" % (len(diffs) - 1, kind))
    base_names = base.names.get("script", [])
    allow = set()
    for a in allow_edit:
        k = _script_key(a)
        if k not in base_names:
            warn.append("WARN --allow-edit names %s, which is not a script in BASE (ignored)" % a)
        allow.add(k)
    edited, body = [], []
    for i, name in enumerate(base_names):
        bb, tb = base.script_block(i), target.script_block(i)
        if bb is None or tb is None:
            continue            # already reported as a shorter list
        if bb.stmts != tb.stmts or bb.meta.get("flag") != tb.meta.get("flag"):
            if name in allow:
                edited.append(name)
            else:
                body.append("script #%d %s: body differs from BASE (%d -> %d statements)" % (
                    i, name, len(bb.stmts), len(tb.stmts)))
    bad += _capped(body)
    detail = []
    if edited:
        detail.append("edited as allowed by --allow-edit: %s" % _short(edited))
    n_new = max(len(target.names.get("script", [])) - len(base_names), 0)
    head = "%d BASE scripts kept in place, %d new scripts appended" % (len(base_names), n_new)
    return not bad, head, bad + detail + warn


def _walk_files(root):
    out = {}
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x != "__pycache__"]
        for f in files:
            if f != ".DS_Store":
                p = os.path.join(d, f)
                out[os.path.relpath(p, root).replace(os.sep, "/")] = p
    return out


def _writable_files(extra):
    """File names a port may change: wbport.TABLES' (or the built-in copy of that list) plus --touched."""
    try:
        import wbport
        names = [v[0] for v in wbport.TABLES.values()]
    except Exception:
        names = list(DEFAULT_TABLE_FILES)
    return {n.lower() for n in names} | {x.lower() for x in extra}


def _is_port_leftover(rel):
    base = rel.rsplit("/", 1)[-1].lower()
    return ".bak_before_" in base or base == "ports.log.jsonl"


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


def _check_untouched(base_dir, target_dir, touched):
    allowed = _writable_files(touched)
    bf, tf = _walk_files(base_dir), _walk_files(target_dir)
    bad, written, leftovers, other = [], [], [], []
    for rel, bp in sorted(bf.items()):
        tp = tf.get(rel)
        if tp is None:
            bad.append("%s exists in BASE but not in TARGET" % rel)
            continue
        if os.path.getsize(bp) == os.path.getsize(tp) and filecmp.cmp(bp, tp, shallow=False):
            continue
        if _is_port_leftover(rel):
            leftovers.append(rel)
        elif rel.lower() in allowed:
            if _read(bp).split() == _read(tp).split():
                bad.append("%s differs byte-for-byte but every token is the same "
                           "(line endings, spacing or a trailing newline changed)" % rel)
            else:
                written.append(rel)
        else:
            other.append(rel)
    bad = _capped(bad) + _capped(["%s changed but is not a file a port may write "
                                  "(allow it with --touched)" % r for r in other])
    detail = []
    if written:
        detail.append("INFO %d files changed, as a port may: %s" % (len(written), _short(written, FILE_LIST_CAP)))
    added = sorted(set(tf) - set(bf))
    added_left = [r for r in added if _is_port_leftover(r)]
    added = [r for r in added if not _is_port_leftover(r)]
    leftovers += added_left
    if leftovers:
        detail.append("INFO %d wbport leftovers (backups, log): %s" % (len(leftovers), _short(leftovers, FILE_LIST_CAP)))
    if added:
        detail.append("INFO %d files exist only in TARGET: %s" % (len(added), _short(added, FILE_LIST_CAP)))
    return not bad, "%d BASE files compared" % len(bf), bad + detail


def _keyed(mod):
    """Blocks keyed by (id, occurrence number among blocks of that id): ids repeat in real modules."""
    seen, out = {}, {}
    for b in mod.blocks:
        k = seen.get(b.id, 0)
        seen[b.id] = k + 1
        out[(b.id, k)] = b
    return out


def _changed_blocks(base, target):
    bk = _keyed(base)
    out = []
    for key, b in _keyed(target).items():
        ob = bk.get(key)
        if ob is None or ob.stmts != b.stmts:
            out.append(b)
    return out


def _check_reachable(base, target, changed, expect, assume):
    from . import analyze
    names = target.names.get("script", [])
    base_names = set(base.names.get("script", []))
    new_idx = range(len(base.names.get("script", [])), len(names))
    todo = [(names[i], target.script_block(i)) for i in new_idx]
    bad, warn = [], []
    assume_keys = {_script_key(a) for a in assume}
    for e in expect:
        b = target.script(e)
        if b is None:
            bad.append("--expect names %s, which is not a script in TARGET" % e)
        elif all(b is not x for _n, x in todo):
            todo.append((b.owner, b))
    for a in assume:
        if target.script(a) is None:
            warn.append("WARN --assume-reached names %s, which is not a script in TARGET (ignored)" % a)
    ix = analyze.ModuleIndex(target)
    computed = 0
    for b in changed:
        x = ix.x[b.id]
        computed += x.opcodes.get(1, 0) - len(x.calls)

    def trusted(root):
        rb = target.block(root)
        # a game_* script is an engine hook only if BASE already had that name
        return not (rb is not None and rb.kind == "script" and rb.owner.startswith("game_")
                    and rb.owner not in base_names)
    ok_lines, waived, fails = [], [], []
    for name, b in todo:
        all_roots = ix.roots_of(b.id)
        roots = [r for r in all_roots if trusted(r)]
        new_hook = name.startswith("game_") and name not in base_names
        if roots:
            ok_lines.append("script_%s <- %s%s" % (
                name, roots[0], " (+%d more)" % (len(roots) - 1) if len(roots) > 1 else ""))
        elif new_hook:
            fails.append("script_%s: new game_* script is not an engine hook; engine hooks must "
                         "already exist in BASE (call it from a trigger, menu or other existing "
                         "script instead)" % name)
        elif name in assume_keys:
            waived.append(name)
        else:
            via = [r for r in all_roots if not trusted(r)]
            fails.append("script_%s has no path from any trigger, menu, dialog, presentation, mission "
                         "template, item or prop trigger, or existing game_* hook%s%s" % (
                             name,
                             " (only reached from the new game_* script %s)" % target.block(via[0]).owner if via else "",
                             " (it may be called through one of the %d computed call_script sites)" % computed
                             if computed else ""))
    bad += _capped(fails)
    if len(ok_lines) > 15:
        ok_lines = ok_lines[:15] + ["... (+%d more reachable)" % (len(ok_lines) - 15)]
    if waived:
        ok_lines.append("WAIVED (assumed reached): %s" % ", ".join("script_" + w for w in waived))
    note = ("limitation: a call_script that takes its script id from a variable cannot be traced "
            "(%d such call sites in new or changed blocks); a script reached only that way shows "
            "as unreachable unless you waive it with --assume-reached" % computed)
    head = "%d scripts checked (%d new, %d added by --expect)" % (len(todo), len(new_idx), len(todo) - len(new_idx))
    return not bad, head, bad + ok_lines + warn, note


def _check_opcodes(changed):
    from .opref import OPS
    bad, seen = [], set()
    for b in changed:
        for code, _f, _o in b.stmts:
            if code not in OPS and (b.id, code) not in seen:
                seen.add((b.id, code))
                bad.append("%s uses unknown opcode %d" % (b.id, code))
    return not bad, "%d new or changed blocks scanned" % len(changed), _capped(bad)


def verify_port(base_dir, target_dir, expect=(), allow_edit=(), assume_reached=(), touched=(), cache_dir=None):
    """(lines, ok). Raises LookupError for a folder that does not exist.
    cache_dir=None loads without writing any parse cache."""
    base = _load(base_dir, "base", cache_dir)
    target = _load(target_dir, "target", cache_dir)
    changed = _changed_blocks(base, target)
    out, results = [], []

    def add(name, passed, head, details):
        results.append(passed)
        out.append("%s %-11s %s" % ("PASS" if passed else "FAIL", name, head))
        out.extend("    " + d for d in details)

    add("append-only", *_check_append_only(base, target, list(allow_edit)))
    add("untouched", *_check_untouched(base_dir, target_dir, list(touched)))
    passed, head, details, note = _check_reachable(base, target, changed, list(expect), list(assume_reached))
    add("reachable", passed, head, details)
    add("opcodes", *_check_opcodes(changed))
    out.append("NOTE " + note)
    ok = all(results)
    out.append("verify-port %s" % ("OK" if ok else "FAILED"))
    return out, ok
