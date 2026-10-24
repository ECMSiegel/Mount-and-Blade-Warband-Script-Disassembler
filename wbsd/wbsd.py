#!/usr/bin/env python3
"""wbsd -- WB Script Disasm v2: Warband reverse-engineering & feature-investigation CLI.

Read-only. Works on every module in the registry (modules.json / modules.example.json).
MOD is a registry slug (`wbsd.py modules` lists them). BLOCK is a script name,
or any block id: script:x  strig:12  trig:3:cond  menu:town  menu:town/opt:trade:conseq
mst:lead_charge/t3:conseq  prsnt:battle/t1  dlg:<n>:<id>:cond  spr:<prop>/t0  itm:<item>/t0

  modules                         registry + parse stats
  dis MOD BLOCK [--raw]           named disassembly (--raw = numeric, like wbdis.py)
  explain MOD BLOCK               purpose inference: callers, entry points, closure profile,
                                  slots, globals, resources, displayed text, Native status
  callers|callees MOD BLOCK       direct call graph
  tree MOD BLOCK [--depth N] [--up]   recursive callee (or caller) tree
  roots MOD BLOCK                 triggers/menus/dialogs/presentations/missions reaching it
  global MOD NAME                 readers & writers of a global ($name or gNNN)
  slot MOD OBJ N                  who reads/writes/tests slot N of troop|party|faction|...
  slots MOD OBJ                   slot map for an object kind, Native-shared flag
  refs MOD KIND NAME              who references trp_x / pt_x / menu_x / psys_x ...
  system MOD BLOCK [--fanout N]   grow the subsystem around a block via calls + shared state
  closure MOD BLOCK... [--into M] [--hooks]  transplant closure + conflicts vs target
                                  (default: the registry's "main" module); --hooks folds in the calling triggers
  diff MOD [OTHER]                script-level diff (default vs native)
  compare SCRIPT [--mods a,b]     one script name across modules (variants)
  similar MOD BLOCK [--mods a,b]  most similar scripts anywhere (finds renamed copies)
  lineage [--mods a,b]            identical-script matrix -> module ancestry
  hooks MOD                       every periodic/event entry point and what it calls
  text REGEX [--mods a,b]         search displayed text (strings, quick strings, menus, dialogs)
  grep REGEX [--mods a,b] [--kinds script,mst]   regex over named disassembly
  opcheck [--mods a,b]            validate the opcode reference against all corpora
  report MOD|all                  write ATLAS_DIR/auto/<MOD>.md (auto module report)
  export                          write out/wbsd.sqlite for ad-hoc SQL
  features [REGEX] [--cat C] [--module M]   search the feature atlas (ATLAS_DIR/features/*.json)
  feature ID                      show one feature record in full
  features-check                  validate every feature record against the schema
  overlaps-apply                  copy ATLAS_DIR/overlaps.json into each feature's `overlaps`
  inventory                       regenerate ATLAS_DIR/FEATURE_INVENTORY.md from the JSON
  verify-port BASE_DIR TARGET_DIR [--expect S,...] [--allow-edit S,...] [--touched FILE,...]
              [--assume-reached S,...]
                                  prove a port is append-only, reachable (a static call path; guards
                                  are not evaluated) and uses known opcodes
                                  (exit 1 on any FAIL; details and limits: wbsd/verify.py)
  check-log RGL_LOG               scan a game rgl_log.txt; exit 1 only for script-error, invalid-id,
                                  unable-to-map and missing-file records; cosmetic material/texture
                                  warnings are counted but do not fail (patterns: wbsd/verify.py)
  batch [FILE|-]                  run one command per line (from FILE or stdin) in ONE process --
                                  indexes are built once, so 20 queries cost ~one
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from wbsd import config, queries, registry  # noqa: E402
except ValueError as _e:  # a malformed modules.json: say which file, no traceback
    print("error: %s" % _e)
    sys.exit(1)
except SystemExit as _e:  # generated tables missing: only commands that need them say so (see main)
    if not isinstance(_e.code, str):
        raise
    _TABLES_MSG = _e.code
else:
    _TABLES_MSG = None
_COMMANDS = {"modules", "dis", "explain", "callers", "callees", "tree", "roots", "global", "slot", "slots",
             "refs", "system", "closure", "diff", "compare", "similar", "lineage", "hooks", "text", "grep",
             "opcheck", "report", "export", "batch", "overlaps-apply", "inventory", "features", "feature",
             "features-check", "verify-port", "check-log"}


def _opt(argv, flag, default=None, cast=str):
    if flag in argv:
        i = argv.index(flag)
        v = argv[i + 1]
        del argv[i:i + 2]
        return cast(v)
    return default


def _csv_opt(argv, flag):
    """Value of `flag` split on commas; a missing value is a clean error, not an IndexError."""
    if flag in argv:
        i = argv.index(flag)
        if i + 1 >= len(argv) or argv[i + 1].startswith("--"):
            raise LookupError("%s needs a value" % flag)
        v = argv[i + 1]
        del argv[i:i + 2]
        return [x for x in v.split(",") if x]
    return []


def _flag(argv, flag):
    if flag in argv:
        argv.remove(flag)
        return True
    return False


def main(argv):
    argv = list(argv[1:])
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 0
    mods = _opt(argv, "--mods")
    mods = mods.split(",") if mods else None
    cmd, args = argv[0], argv[1:]
    if "-h" in args or "--help" in args:
        print(__doc__)
        return 0
    if _TABLES_MSG and cmd in _COMMANDS and cmd != "check-log":      # check-log needs no tables
        sys.exit(_TABLES_MSG)
    try:
        if cmd == "modules":
            for e in registry.entries():
                if not os.path.isdir(registry.root_of(e)):
                    print("%-7s %-8s %-52s MISSING: %s" % (
                        e["slug"], e["role"], e["label"][:52], registry.root_of(e)))
                    continue
                n_scripts, n_blocks, ns, errors = registry.stats(e["slug"])
                print("%-7s %-8s %-52s scripts=%-5d blocks=%-6d stmts=%-7d %s" % (
                    e["slug"], e["role"], e["label"][:52], n_scripts,
                    n_blocks, ns, ("ERR " + str(errors)) if errors else ""))
            return 0
        if cmd == "dis":
            raw = _flag(args, "--raw")
            out = queries.dis(args[0], args[1], raw)
        elif cmd == "explain":
            out = queries.explain(args[0], args[1])
        elif cmd == "callers":
            out = queries.callers(args[0], args[1])
        elif cmd == "callees":
            out = queries.callees(args[0], args[1])
        elif cmd == "tree":
            depth = _opt(args, "--depth", 3, int)
            up = _flag(args, "--up")
            out = queries.tree(args[0], args[1], depth, up)
        elif cmd == "roots":
            out = queries.roots(args[0], args[1])
        elif cmd == "global":
            out = queries.global_use(args[0], args[1])
        elif cmd == "slot":
            out = queries.slot_use(args[0], args[1], args[2])
        elif cmd == "slots":
            out = queries.slot_map(args[0], args[1])
        elif cmd == "refs":
            out = queries.ref_use(args[0], args[1], args[2])
        elif cmd == "system":
            fan = _opt(args, "--fanout", 25, int)
            mx = _opt(args, "--max", 120, int)
            out = queries.system(args[0], args[1], fan, mx)
        elif cmd == "closure":
            into = _opt(args, "--into", config.MAIN)
            if into is None:
                raise LookupError("closure needs --into MODULE (no registry entry has role \"main\")")
            wh = _flag(args, "--hooks")
            out = queries.closure(args[0], args[1:], into, wh)
        elif cmd == "diff":
            out = queries.diff(args[0], args[1] if len(args) > 1 else "native")
        elif cmd == "compare":
            out = queries.compare(args[0], mods)
        elif cmd == "similar":
            top = _opt(args, "--top", 12, int)
            out = queries.similar(args[0], args[1], top, mods)
        elif cmd == "lineage":
            out = queries.lineage(mods)
        elif cmd == "hooks":
            out = queries.hooks(args[0])
        elif cmd == "text":
            out = queries.text(args[0], mods)
        elif cmd == "grep":
            kinds = _opt(args, "--kinds")
            out = queries.grep(args[0], mods, kinds.split(",") if kinds else None)
        elif cmd == "opcheck":
            from wbsd import opcheck
            out = [opcheck.render(opcheck.check([registry.load(s) for s in (mods or registry.slugs())]))]
        elif cmd == "report":
            from wbsd import report
            out = report.write_all() if args[0] == "all" else [report.write(args[0])]
        elif cmd == "export":
            from wbsd import export
            out = [export.write(mods)]
        elif cmd in ("verify-port", "check-log"):
            from wbsd import verify
            if cmd == "check-log":
                if len(args) != 1:
                    raise LookupError("usage: check-log RGL_LOG")
                out, ok = verify.check_log(args[0])
            else:
                lists = {f: _csv_opt(args, f) for f in ("--expect", "--allow-edit", "--assume-reached", "--touched")}
                if len(args) != 2:
                    raise LookupError("usage: verify-port BASE_DIR TARGET_DIR [--expect S,...] [--allow-edit S,...] "
                                      "[--assume-reached S,...] [--touched FILE,...]")
                out, ok = verify.verify_port(
                    args[0], args[1], lists["--expect"], lists["--allow-edit"], lists["--assume-reached"],
                    lists["--touched"], cache_dir=os.path.join(config.CACHE_DIR, "parsed"))
            print("\n".join(out))
            return 0 if ok else 1
        elif cmd == "batch":
            src = open(args[0]) if args and args[0] != "-" else sys.stdin
            out = queries.batch(src.read().splitlines())
        elif cmd == "overlaps-apply":
            from wbsd import atlas
            out = atlas.apply_overlaps() or ["overlaps applied"]
        elif cmd == "inventory":
            from wbsd import atlas
            out = [atlas.write_inventory()]
        elif cmd in ("features", "feature", "features-check"):
            from wbsd import atlas
            if cmd == "features-check":
                out = atlas.validate() or ["feature index OK (%d records)" % len(atlas.load_all())]
            elif cmd == "feature":
                hit = [f for f in atlas.load_all() if f.get("id") == args[0]]
                out = atlas.show(hit[0]) if hit else ["no feature %r" % args[0]]
            else:
                cat = _opt(args, "--cat")
                mod = _opt(args, "--module")
                fs = atlas.search(args[0] if args else None, cat, mod)
                out = ["%-45s %-22s %-7s v%s %-9s %-10s %s" % (f.get("id"), f.get("category"), f.get("target_status", "")[:7],
                       f.get("value"), f.get("recommendation"), f.get("confidence"), f.get("name")) for f in fs]
                out.append("(%d features)" % len(fs))
        else:
            print("unknown command %r\n" % cmd)
            print(__doc__)
            return 2
    except (LookupError, IndexError, ValueError, re.error) as e:
        print("error: %s" % e)
        return 1
    try:
        print("\n".join(out))
    except BrokenPipeError:
        pass
    return 0


def cli():
    """Console-script entry point (see pyproject.toml)."""
    sys.exit(main(sys.argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
