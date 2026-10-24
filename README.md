# Mount & Blade Warband Script Disassembler

Read compiled Warband scripts, compare them across mods, and plan a feature port before you touch any code.

[![tests](https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler/actions/workflows/tests.yml/badge.svg)](https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler/actions/workflows/tests.yml)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![MIT](https://img.shields.io/badge/licence-MIT-green)

Status: tested on Native; the author's real-use test is pending. Python 3.9 or newer, standard library only.

## Why this exists

Every Warband mod ships its logic as compiled script files (`scripts.txt`, `triggers.txt`, `conversation.txt` ...), not as the
Module System source it came from. The established tools each cover a different job, and none of them analyses those
compiled scripts across several mods. This one does: it reads the files, names every operation, and answers questions
across all the mods you point it at.

| Tool | What it is for |
|---|---|
| W.R.E.C.K. | compile a module from Module System source |
| Morgh's editor | edit items, troops and similar game data |
| OpenBRF | view and edit meshes and other resources |
| this repo | read, search and compare the compiled scripts of many mods; plan ports between them |

## What only this does

**Plan a port with `closure --into`.** Name a feature in one mod and a target mod. You get everything the feature
drags in, and what would clash in the target ([Recipe B](docs/RECIPES.md)):

    wbsd closure vc add_jetty_system --into native --hooks

    blocks in closure: 67
    entry points the feature hangs off in the donor (2):
       script:game_start
    SCRIPTS:
       abort_quest         327 stmts  DIFFERS in target (65% similar) -> merge conflict
       add_jetty_system     16 stmts  ABSENT in target (must be rebuilt)
       add_log_entry        80 stmts  identical in target

Beyond that:

- **Lineage and similar.** `lineage` shows which mods share identical scripts (module ancestry); `similar` finds a renamed copy of a script by what it does.
- **Call graphs and cross-references.** Callers, callees, trees, entry points, and every reader and writer of a global, slot or resource.
- **A byte-exact parser.** `wbasm` reads a module file and writes it back identical to the byte, so nothing is lost in translation.
- **A port harness.** `wbport` is a safety wrapper for port scripts: backups, round-trip checks, idempotent helpers, nothing written if a check fails. `wbsd verify-port` then proves the result is append-only and reachable (a static call path; guards are not evaluated).
- **A feature atlas.** [examples/atlas/](examples/atlas/README.md) holds 311 records across 15 public mods, plus a fresh audit made with the shipped skills.

## Quick start (about 60 seconds)

1. Install, from a clone of this repo. It must be an editable install, because the tables and caches live in the clone. pip needs normal network access to fetch setuptools.

        pip install -e .

   This gives you the `wbsd`, `wbdis` and `wb-build-tables` commands. (Without installing, `python3 wbsd/wbsd.py ...` works too.)

2. Build the opcode tables:

        wb-build-tables --download

   This fetches TaleWorlds' header files from the TLD mod's public repo; nothing is redistributed here. Already have a Module System, or a mod that ships its source? `wb-build-tables <that folder>` works too.

3. Modules folder. `wbsd` looks for Steam's `Modules` folder and uses the first one that exists: macOS Steam, then
   `%ProgramFiles(x86)%\Steam\...`, `%ProgramFiles%\Steam\...`, `~/.steam/steam/...`, `~/.local/share/Steam/...`.
   Anywhere else, set `WB_MODULES_DIR` to your `Modules` folder (the one holding `Native/`).

4. Try it:

        wbsd explain native game_start

        == EXPLAIN script:game_start in Native
        statements: 675   params: 0   returns: -
        direct callees (39): script:update_party_creation_random_limits, ...
        closure: 114 blocks (this + recursive callees)

The first run on a module builds a cache in `.cache/` (about a second for Native, longer for large mods). Three worked examples: [docs/RECIPES.md](docs/RECIPES.md).

## Do I need an AI agent?

No. The `wbsd` command line, `report`, the atlas commands and the example atlas are ordinary tools you use directly.
Writing new atlas records and porting features are mostly judgement work, and you can do both by hand with [docs/ATLAS.md](docs/ATLAS.md) and [docs/PORTING.md](docs/PORTING.md).
Porting by hand means a short Python script using `wbport`, then `wbsd verify-port` to check it; there is no one-command port.
The skills in `skills/` (`atlas-add`, `atlas-audit`, `atlas-port`, `port-batch`) are optional procedures that let an AI coding agent do those jobs.

## Using the agent skills

Four skills for AI coding agents ship in `skills/`: `atlas-add` (register a module and build its map), `atlas-audit` (audit a module into atlas features) and `atlas-port` (port a feature into your own mod; human version: [docs/PORTING.md](docs/PORTING.md)) and `port-batch` (run many ports onto one target, in waves).
Copy or symlink `skills/atlas-add`, `skills/atlas-audit`, `skills/atlas-port` and `skills/port-batch` into `.claude/skills/` (Claude Code) or `.agents/skills/` (Codex, OpenCode), then type `/atlas-add`.

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
| `WB_MODULES_DIR` | folder holding the module folders | first Steam `Modules` folder found (see Quick start) |
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

## Safety model

- Byte-exact round trip: `wbasm` writes a parsed file back identical to the byte. The tests check this on Native for `scripts.txt`, `simple_triggers.txt`, `menus.txt`, `triggers.txt`, `tableau_materials.txt`, `conversation.txt`, `mission_templates.txt` and `presentations.txt`.
- `wbport` refuses a target inside the Modules folder, backs each table up once, and writes nothing if any check fails.
- Scripts are append-only: new scripts go at the end, so existing script indexes never shift.
- Module folders are used read-only. Caches and reports go under this repo (`.cache/`, `out/`), never into a module folder.

## Performance

Caching and a few query changes cut most commands by 50 to 98 percent with byte-identical output. For example `modules`
went from 4.9 s to 0.12 s and `explain` from 2.1 s to 0.7 s. Method: [docs/PERFORMANCE.md](docs/PERFORMANCE.md). Where the time goes: [docs/PROFILE.md](docs/PROFILE.md).

## Tests

The tests pass without any game data (those that need it are skipped). CI runs on Ubuntu and Windows with Python 3.9, 3.12, 3.13 and 3.14.
Run them with `python3 -m unittest discover -s tests`; `python3 tools/hollow_check.py tests` flags tests that can never fail; details in [tests/README.md](tests/README.md).

## More documentation

- [docs/RECIPES.md](docs/RECIPES.md): three worked examples.
- [docs/PORTING.md](docs/PORTING.md): how to port a feature between mods (`wbport`, `verify-port`, `check-log`).
- [docs/FORMAT.md](docs/FORMAT.md): the compiled bytecode format.
- [docs/ATLAS.md](docs/ATLAS.md): the feature atlas; [examples/atlas/](examples/atlas/README.md): a worked example.
- [CHANGELOG.md](CHANGELOG.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Provenance and licence

The opcode names, ids, signatures, operand tags, trigger-event codes and key codes come from TaleWorlds'
Mount & Blade: Warband Module System, which TaleWorlds publishes for modders. This repository does not redistribute
those tables. `wbsd/build_tables.py` generates them from the Module System headers (your own copy, or fetched with `--download`), writing two local, git-ignored files
(`wbsd/opref_data.py`, `wbsd/header_tables.py`). The headers are read as text; nothing in them is run. Until they exist, `wbsd`
prints a short "run build_tables first" message and the tests that need them are skipped. The repo includes the author's
corrections in `wbsd/table_overlay.py`; see [docs/PROVENANCE.md](docs/PROVENANCE.md).

The MIT licence covers this repo's own code and docs. The Module System itself remains TaleWorlds'. See [LICENSE](LICENSE).
