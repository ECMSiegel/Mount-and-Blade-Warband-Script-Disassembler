# Reference: commands and configuration

Moved out of the main [README](../README.md) to keep it short.

## Commands

`wbsd help` prints the full list. MOD is a registry slug (see `modules`). BLOCK is a script name or a block id such as
`script:x`, `trig:3:cond`, `menu:town`, `dlg:<n>:<id>:cond`.

    modules                         registry + parse stats
    dis MOD BLOCK [--raw]           named disassembly (--raw = numeric, like wbdis.py)
    explain MOD BLOCK               purpose inference: callers, entry points, closure profile, slots, globals
    callers|callees MOD BLOCK       direct call graph
    tree MOD BLOCK [--depth N] [--up]   recursive callee (or caller) tree
    roots MOD BLOCK                 triggers/menus/dialogs/presentations/missions reaching it
    global MOD NAME                 readers and writers of a global
    slot MOD OBJ N                  who reads/writes/tests slot N of troop|party|faction|...
    slots MOD OBJ                   slot map for an object kind, Native-shared flag
    refs MOD KIND NAME              who references trp_x / pt_x / menu_x / psys_x ...
    system MOD BLOCK [--fanout N]   grow the subsystem around a block via calls + shared state
    closure MOD BLOCK... [--into M] [--hooks]   transplant closure + conflicts vs target
    diff MOD [OTHER]                script-level diff (default vs native)
    compare SCRIPT [--mods a,b]     one script name across modules (variants)
    similar MOD BLOCK [--mods a,b]  most similar scripts anywhere (finds renamed copies)
    lineage [--mods a,b]            identical-script matrix -> module ancestry
    hooks MOD                       every periodic/event entry point and what it calls
    text REGEX [--mods a,b]         search displayed text
    grep REGEX [--mods a,b] [--kinds script,mst]   regex over named disassembly
    opcheck [--mods a,b]            validate the opcode reference against all corpora
    report MOD|all                  write ATLAS_DIR/auto/<MOD>.md (auto module report)
    export                          write out/wbsd.sqlite for ad-hoc SQL
    features [REGEX] [--cat C] [--module M]   search the feature atlas
    feature ID                      show one feature record in full
    features-check                  validate every feature record against the schema
    overlaps-apply                  copy ATLAS_DIR/overlaps.json into each feature's `overlaps`
    inventory                       regenerate ATLAS_DIR/FEATURE_INVENTORY.md from the JSON
    verify-port BASE TARGET [--expect S,..] [--allow-edit S,..] [--touched F,..] [--assume-reached S,..]
                                    prove a port is append-only, reachable (static call path; guards
                                    are not evaluated) and uses known opcodes
    check-log RGL_LOG               scan a game rgl_log.txt for script errors, invalid ids, missing files
    batch [FILE|-]                  run one command per line in ONE process (indexes built once)

## Configuration

Environment variables, except the registry file contents.

| Setting | Meaning | Default |
|---|---|---|
| `WB_MODULES_DIR` | folder holding the module folders | first Steam `Modules` folder found (see the README quick start) |
| `WB_REGISTRY` | path to a module registry JSON | `modules.json` if present, else `modules.example.json` |
| `WB_ATLAS_DIR` | feature atlas folder | `out/atlas` |
| `WB_CACHE_DIR` | parse / index cache folder | `.cache` in this repo |
| `WB_MODULE` | module folder `wbdis.py` and `gen_evidence.py` read | `Native` |
| `WB_TEST_MODULE` | module folder the tests read | `Native` |
| `WB_TEST_ALL_MODULES` | `1` makes `test_every_module_loads` load every registered module | off |
| `WB_HEADERS_DIR` | Module System folder; turns on the table-reproduction test | off |

`modules.json` (git-ignored) lists the modules `wbsd` knows. Copy `modules.example.json` and add entries: `slug`, `label`,
`path` (relative to `WB_MODULES_DIR`, or `cache:<name>` for a folder under `.cache/archives/`), and `role` (`main`, `native`,
`lineage` or `donor`). The `main` module is the default target for `closure --into`.
`.cache/` is safe to delete; it is rebuilt when a module's `.txt` files change.

