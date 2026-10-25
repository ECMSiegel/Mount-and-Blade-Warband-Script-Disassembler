# Mount & Blade: Warband Script Disassembler

**Explore Warband’s compiled scripts without the original source.**

Find the logic behind a feature, trace its dependencies, and compare implementations across mods. This Python toolkit reads the compiled `.txt` files shipped with Warband modules and turns numeric instructions into named operations, call graphs, and reports.

## Quick start

You need **Python 3.9+**, a local copy of **Mount & Blade: Warband** with its `Native` module, and Git if you use the clone command below. The toolkit has no third-party runtime dependencies. An AI coding agent is optional.

### 1. Get the toolkit

```sh
git clone https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler.git
cd Mount-and-Blade-Warband-Script-Disassembler
```

Alternatively, use GitHub’s **Code → Download ZIP**, extract it, and open a terminal in the extracted folder.

### 2. Install and run your first query

Run the commands for your operating system, one line at a time, from the downloaded folder.

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -e .
.venv\Scripts\wb-build-tables.exe --download
.venv\Scripts\wbsd.exe explain native game_start
```

**macOS / Linux:**

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/wb-build-tables --download
.venv/bin/wbsd explain native game_start
```

Use an editable install (`-e .`): generated tables and caches live in your checkout. `--download` fetches Module System headers from a pinned public source and builds the operation-name tables locally; it reads the headers as text without executing them. To use headers you already have, replace `--download` with the quoted path to your Module System folder. See [provenance](docs/PROVENANCE.md).

If setup worked, the final command prints a report beginning with `EXPLAIN script:game_start in Native`. It shows the calls and dependencies of the script that starts a new game. Example output, abbreviated:

```text
== EXPLAIN script:game_start in Native
statements: 675   params: 0   returns: -
direct callees (39): script:update_party_creation_random_limits, ...
closure: 114 blocks (this + recursive callees)
```

Here, *closure* means the script plus the blocks reached by following its calls. The first query builds a local cache; later queries reuse it.

### 3. If the tool cannot find Warband

The tool checks common Steam locations on Windows, macOS, and Linux. If Native is missing, set `WB_MODULES_DIR` to the folder **containing `Native`**, then rerun the final command above:

```powershell
# Windows PowerShell — replace this example path
$env:WB_MODULES_DIR = 'D:\SteamLibrary\steamapps\common\MountBlade Warband\Modules'
```

```sh
# macOS / Linux — replace this example path
export WB_MODULES_DIR='/path/to/MountBlade Warband/Modules'
```

Native is registered by default through `modules.example.json`. To add another mod, copy that file to `modules.json` if you do not already have one, then add an entry with its folder path and a short `slug`. Use the slug in commands. [Configuration reference →](docs/REFERENCE.md)

The examples below use `wbsd` as shorthand. With the environment above, use `.venv\Scripts\wbsd.exe` on Windows or `.venv/bin/wbsd` on macOS/Linux.

[![tests](https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler/actions/workflows/tests.yml/badge.svg)](https://github.com/ECMSiegel/Mount-and-Blade-Warband-Script-Disassembler/actions/workflows/tests.yml)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue)
![MIT](https://img.shields.io/badge/licence-MIT-green)

**For modders:** [Quick start](#quick-start) · [Modding workflows](#modding-workflows) · [Command reference](docs/REFERENCE.md)

**For technical reviewers:** [Engineering highlights](#engineering-highlights) · [Evidence and limitations](#evidence-and-limitations) · [Project authorship](#project-authorship)

## See what it answers

“Which parts of the mod depend on this variable?”

```sh
wbsd global native '$g_talk_troop'
```

Excerpt from the [worked example](docs/RECIPES.md):

```text
$g_talk_troop (global #115): 7 writer blocks, 906 reader blocks
 WRITERS:
   dlg:0:dlga_start:close_window:cond "{!}Warning:_This_line_is_never_displayed._It_is_just_for_sto"
   dlg:1929:dlga_member_chat:sacrificed_messenger_1:cond "Yes_{sir/madam}?"
   script:npc_decision_checklist_party_ai
```

Before changing a shared variable, you can identify the scripts and dialogue blocks that use it. The full report lists readers too; each block ID can be inspected with `wbsd dis` or `wbsd explain`. Counts depend on the module version.

## Modding workflows

| I want to… | Start here |
|---|---|
| Read a script as named operations | `wbsd dis native game_start` |
| Find who calls it | `wbsd callers native game_start` |
| Find entry points that lead to it | `wbsd roots native game_start` |
| Find readers and writers of a global | `wbsd global native '$g_talk_troop'` |
| Compare a feature’s dependencies with another mod | `wbsd closure DONOR SCRIPT --into TARGET --hooks` |
| Find similar scripts, including renamed candidates | `wbsd similar MOD SCRIPT` |
| Explore documented features | [Example feature atlas](examples/atlas/README.md) |

`DONOR`, `TARGET`, and `MOD` are registered module slugs; `SCRIPT` is a script name. Keep the single quotes around `$g_talk_troop` so your shell does not expand it.

**Planning a port?** The closure report identifies script differences, missing resources, and possible slot collisions. Porting still requires judgement and a Python port script; there is no one-command feature transplant. Start with the [worked port-analysis example](docs/RECIPES.md), then the [porting guide](docs/PORTING.md). Work on a separate copy of the target mod and respect the source mod’s permissions.

**Prefer an agent-assisted workflow?** The optional [skills](skills) cover registering mods, auditing features, and planning and applying ports. The same CLI and reports are usable by hand. See the [atlas guide](docs/ATLAS.md) for the catalogue format and workflow.

<details>
<summary>Terms used in reports</summary>

- **Module:** a game/mod folder, such as `Native`.
- **Module System:** the source framework used to build Warband modules; it is not required to inspect a mod’s compiled scripts.
- **Trigger:** logic invoked by a timer or event.
- **Global:** a variable shared across game logic.
- **Slot:** a numbered storage cell attached to a troop, party, faction, or other game object.
- **Atlas:** a catalogue of investigated mod features.

</details>

## Engineering highlights

The engineering problem is to make compiled game logic inspectable while preserving its representation and identifying dependencies across independently built modules.

```text
Compiled module files → parsed blocks and operands → named operations and indexes
                                                   ↓
                              disassembly · call graphs · comparisons · port reports
```

| Component | Responsibility | Implementation / evidence |
|---|---|---|
| Parser and serializer | Preserve supported tables byte for byte through an unedited round trip | [wbasm.py](wbasm.py), [format notes](docs/FORMAT.md) |
| Analysis CLI | Resolve names, trace calls, and find references across modules | [wbsd](wbsd), [worked queries](docs/RECIPES.md) |
| Cache and query optimization | Reuse parsed modules and reference indexes, and avoid unnecessary analysis | [benchmark methodology](docs/PERFORMANCE.md), [profiling notes](docs/PROFILE.md) |
| Port harness | Translate named operands, back up target tables, and validate edits before writing | [wbport.py](wbport.py), [porting guide](docs/PORTING.md) |
| Test fixtures | Exercise parsing, CLI queries, and port failure cases without redistributing game data | [test documentation](tests/README.md), [CI workflow](.github/workflows/tests.yml) |

### Recorded performance

The documented paired comparison used warm caches, an untimed warm-up, and three alternating rounds; these are recorded results, not a guarantee for another machine or module set.

| Command | Before | After |
|---|---:|---:|
| `modules` | 4.90 s | 0.12 s |
| `explain main game_start` | 2.11 s | 0.72 s |
| `similar main game_start` | 6.77 s | 2.48 s |

The benchmark notes report byte-identical output across 17 comparison commands and include cache-invalidation checks and measurements with individual optimizations removed. [Read the method and trade-offs →](docs/PERFORMANCE.md)

## Evidence and limitations

- **Inspection and editing are distinct.** Analysis reads module data and uses local caches. The port harness edits a target copy; by default, it refuses targets inside the configured game Modules folder.
- **Round trips protect representation.** Byte-preserving serialization and pre-write checks catch structural problems. They do not establish that edited gameplay is correct.
- **Reachability is static.** `verify-port` checks structural properties, including append-only script changes and call paths. It does not evaluate runtime guards or replace an in-game playtest.
- **Similarity is a lead, not attribution.** Shared scripts can reflect common Native code or another shared source. Similarity alone does not establish authorship or copying direction.
- **Test coverage depends on available data.** CI is configured for Ubuntu and Windows with Python 3.9, 3.12, 3.13, and 3.14. Fixture tests run without game data; tests requiring real modules or generated tables are skipped when those inputs are absent.

Run the suite from the repository root using your environment’s Python:

```sh
python -m unittest discover -s tests -v
```

See [tests/README.md](tests/README.md) for data-dependent checks and configuration. A passing fixture suite is not evidence that every third-party mod is supported.

## Project authorship

This project grew out of my Warband modding work. I described the workflows I needed and directed AI coding agents, which wrote the implementation, tests, and documentation. I’ve documented the technical approach and supporting evidence in this repository so you can inspect how it works and what has been checked.

For a technical review, start with the [parser](wbasm.py), [performance experiments](docs/PERFORMANCE.md), and [fixture tests](tests/README.md). These make the implementation choices and the limits of the checks concrete.

## Documentation and licence

- [Command reference](docs/REFERENCE.md) — commands, flags, and environment variables.
- [Worked examples](docs/RECIPES.md) — variable references, port planning, and script similarity.
- [Porting guide](docs/PORTING.md) — target copies, remapping, validation, and logs.
- [Feature atlas](docs/ATLAS.md) and [example catalogue](examples/atlas/README.md).
- [Compiled format](docs/FORMAT.md), [provenance](docs/PROVENANCE.md), [changelog](CHANGELOG.md), and [contributing](CONTRIBUTING.md).

The [MIT licence](LICENSE) covers this repository’s own code and documentation. TaleWorlds’ Module System remains TaleWorlds’ material. Operation tables are generated locally from Module System headers and are not redistributed here; see [provenance](docs/PROVENANCE.md) for the source and generation process.
