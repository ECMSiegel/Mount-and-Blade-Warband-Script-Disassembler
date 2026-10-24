# Mount & Blade Warband Script Disassembler

Look inside any Mount & Blade: Warband mod, even without its source code: see how its features work, compare mods, and bring features into your own mod safely.

[![tests](https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler/actions/workflows/tests.yml/badge.svg)](https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler/actions/workflows/tests.yml)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![MIT](https://img.shields.io/badge/licence-MIT-green)

## What can I do with it?

- **Find the script behind a feature.** Which script makes caravans travel? `wbsd grep`, `wbsd text`, `wbsd explain`
- **See which mods copied from each other.** Mods that share identical scripts share ancestry. `wbsd lineage`, `wbsd similar`
- **Get a shopping list before you copy a feature.** Everything it needs, and what would clash in your mod. `wbsd closure ... --into`
- **Copy a feature into your mod, with a safety check.** The tool proves nothing existing was changed and the new code is actually reachable. `wbport` + `wbsd verify-port`
- **Browse a catalogue of features.** 311 records from 15 public mods. [examples/atlas](examples/atlas/README.md), `wbsd features`
- **Read a game log for you.** Spots script errors and missing files. `wbsd check-log`

## How this was made

This was built by someone with no programming background, just by describing what they wanted to do in Warband to AI coding agents. The agents wrote the code, the tests and the docs. Nothing was kept on trust: every change was checked against the output of the original tool, and reviewed by separate agents before it stayed. The author used this approach to build a large Warband mod of their own. You can do the same. You do not need to read code: the files in [skills/](skills) are the step-by-step procedures the agents follow, and you can read them like a checklist.

## Two ways to use it

### (a) With an AI coding agent (easiest)

Open this repo in an agent such as Claude Code or Codex, copy the skills in, and ask in plain words.

- Claude Code: copy the folders in `skills/` into `.claude/skills/`
- Codex or OpenCode: copy the folders in `skills/` into `.agents/skills/`

Example requests:

- "Audit the mod in folder X and add it to the atlas."
- "Find how mod X does caravans."
- "Port the feature X from mod A into my mod in folder B."

The four skills are `atlas-add` (register a mod), `atlas-audit` (write up its features), `atlas-port` (copy one feature into your mod) and `port-batch` (many ports onto one mod, in waves). You can also type `/atlas-add` and so on. Setup (steps 1 to 5 below) still applies; the agent can do those for you if you ask.

### (b) Yourself

You do not need an agent. The `wbsd` command, reports and the example atlas are ordinary tools. Writing atlas records and porting are mostly judgement work, but you can do both by hand: [docs/ATLAS.md](docs/ATLAS.md) and [docs/PORTING.md](docs/PORTING.md). A by-hand port is a short Python script using `wbport`, checked with `wbsd verify-port`; there is no one-command port.

1. **Install Python 3.9 or newer.** Nothing else is needed; the tool uses only what Python ships with.
2. **Clone this repo** (download it with git) and open a terminal in that folder.
3. **Install it:** `pip install -e .` This adds the `wbsd`, `wbdis` and `wb-build-tables` commands. It must be an editable install, because the tables and caches live in your clone. (Without installing, `python3 wbsd/wbsd.py ...` works too.)
4. **Build the opcode tables:** `wb-build-tables --download` Opcodes are the little instructions scripts are made of. This fetches TaleWorlds' public header files; nothing is redistributed here. If you already have a Module System, `wb-build-tables <that folder>` works too.
5. **Point it at your mods.** It looks for Steam's `Modules` folder by itself: macOS Steam, then `%ProgramFiles(x86)%\Steam\...`, `%ProgramFiles%\Steam\...`, `~/.steam/steam/...`, `~/.local/share/Steam/...`. Anywhere else, set `WB_MODULES_DIR` to your `Modules` folder (the one holding `Native/`).
6. **Try it:**

        wbsd explain native game_start

        == EXPLAIN script:game_start in Native
        statements: 675   params: 0   returns: -
        direct callees (39): script:update_party_creation_random_limits, ...
        closure: 114 blocks (this + recursive callees)

   That says what the script that starts a new game does. The first run on a mod builds a cache in `.cache/` (about a second for Native, longer for big mods).

Three worked examples: [docs/RECIPES.md](docs/RECIPES.md).

## Words you'll see

- **Module / mod:** one folder under `Modules/`, a game or add-on such as Native.
- **Module System:** the Python source modders use to build a mod. Most mods do not ship it.
- **Compiled files:** the `.txt` files (`scripts.txt`, `triggers.txt`, ...) the game actually reads. This tool reads those.
- **Script:** a named routine of game logic that other scripts, menus and triggers can call.
- **Trigger:** logic that runs on a timer or an event.
- **Global:** a named variable shared by the whole game.
- **Slot:** a numbered storage cell attached to a troop, party, faction and so on.
- **Closure:** a feature plus everything it calls or depends on.
- **Atlas:** a catalogue of features found in mods, one record per feature.
- **Port:** copying a feature from one mod into another.

# Reference

## Why this exists

Every Warband mod ships its logic as compiled script files, not as the Module System source it came from. The established tools each cover a different job, and none analyses those compiled scripts across several mods. This one reads the files, names every operation, and answers questions across all the mods you point it at.

| Tool | What it is for |
|---|---|
| W.R.E.C.K. | compile a module from Module System source |
| Morgh's editor | edit items, troops and similar game data |
| OpenBRF | view and edit meshes and other resources |
| this repo | read, search and compare the compiled scripts of many mods; plan ports between them |

## What only this does

**Plan a port with `closure --into`.** Name a feature in one mod and a target mod. You get everything the feature drags in, and what would clash in the target ([Recipe B](docs/RECIPES.md)):

    wbsd closure vc add_jetty_system --into native --hooks

    blocks in closure: 67
    entry points the feature hangs off in the donor (2):
       script:game_start
    SCRIPTS:
       abort_quest         327 stmts  DIFFERS in target (65% similar) -> merge conflict
       add_jetty_system     16 stmts  ABSENT in target (must be rebuilt)
       add_log_entry        80 stmts  identical in target

- **Lineage and similar.** `lineage` shows which mods share identical scripts; `similar` finds a renamed copy of a script by what it does.
- **Call graphs and cross-references.** Callers, callees, trees, entry points, and every reader and writer of a global, slot or resource.
- **A byte-exact parser.** `wbasm` reads a module file and writes it back identical to the byte, so nothing is lost in translation.
- **A port harness.** `wbport` is a safety wrapper for port scripts: backups, round-trip checks, idempotent helpers, nothing written if a check fails. `wbsd verify-port` then proves the result is append-only and reachable (a static call path; guards are not evaluated).
- **A feature atlas.** [examples/atlas/](examples/atlas/README.md) holds 311 records across 15 public mods, plus a fresh audit made with the shipped skills.

## Commands and configuration

`wbsd help` prints the full command list; every command, flag and environment variable (`WB_MODULES_DIR`, `WB_REGISTRY`, `WB_ATLAS_DIR`, `WB_CACHE_DIR`, ...) is in [docs/REFERENCE.md](docs/REFERENCE.md). The registry file `modules.json` (git-ignored) lists the modules `wbsd` knows; copy `modules.example.json` and add entries. `.cache/` is safe to delete; it is rebuilt when a module's `.txt` files change.

## Safety model

- Byte-exact round trip: `wbasm` writes a parsed file back identical to the byte. The tests check this on Native for `scripts.txt`, `simple_triggers.txt`, `menus.txt`, `triggers.txt`, `tableau_materials.txt`, `conversation.txt`, `mission_templates.txt` and `presentations.txt`.
- `wbport` refuses a target inside the Modules folder, backs each table up once, and writes nothing if any check fails.
- Scripts are append-only: new scripts go at the end, so existing script indexes never shift.
- Module folders are used read-only. Caches and reports go under this repo (`.cache/`, `out/`), never into a module folder.

## Performance

Caching and a few query changes cut most commands by 50 to 98 percent with byte-identical output. For example `modules` went from 4.9 s to 0.12 s and `explain` from 2.1 s to 0.7 s. Method: [docs/PERFORMANCE.md](docs/PERFORMANCE.md). Where the time goes: [docs/PROFILE.md](docs/PROFILE.md).

## Tests

The tests pass without any game data (those that need it are skipped). CI runs on Ubuntu and Windows with Python 3.9, 3.12, 3.13 and 3.14. Run them with `python3 -m unittest discover -s tests`; `python3 tools/hollow_check.py tests` flags tests that can never fail; details in [tests/README.md](tests/README.md).

## More documentation

- [docs/REFERENCE.md](docs/REFERENCE.md): all commands and settings.
- [docs/RECIPES.md](docs/RECIPES.md): three worked examples.
- [docs/PORTING.md](docs/PORTING.md): how to port a feature between mods (`wbport`, `verify-port`, `check-log`).
- [docs/FORMAT.md](docs/FORMAT.md): the compiled bytecode format.
- [docs/ATLAS.md](docs/ATLAS.md): the feature atlas; [examples/atlas/](examples/atlas/README.md): a worked example.
- [CHANGELOG.md](CHANGELOG.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Provenance and licence

The opcode names, ids, signatures, operand tags, trigger-event codes and key codes come from TaleWorlds' Mount & Blade: Warband Module System, which TaleWorlds publishes for modders. This repository does not redistribute those tables. `wbsd/build_tables.py` generates them from the Module System headers (your own copy, or fetched with `--download`), writing two local, git-ignored files (`wbsd/opref_data.py`, `wbsd/header_tables.py`). The headers are read as text; nothing in them is run. Until they exist, `wbsd` prints a short "run build_tables first" message and the tests that need them are skipped. The repo includes the author's corrections in `wbsd/table_overlay.py`; see [docs/PROVENANCE.md](docs/PROVENANCE.md).

The MIT licence covers this repo's own code and docs. The Module System itself remains TaleWorlds'. See [LICENSE](LICENSE).
