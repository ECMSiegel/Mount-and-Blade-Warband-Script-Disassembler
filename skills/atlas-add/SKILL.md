---
name: atlas-add
description: Register a Warband module in the wbtools registry, confirm it parses, check it for non-vanilla opcodes, and write its structural map. Use when the user wants to add a module to the atlas, register a donor or main mod, or says "atlas-add", "add this module", or "new donor".
---

# Atlas add

Brings one compiled Warband module into the toolkit so it can be investigated. This skill only
reads the module. It never writes inside a module folder.

Run every command from the wbtools repo root as `python3 wbsd/wbsd.py ...`. The full command
list is in `python3 wbsd/wbsd.py --help`. After `pip install -e .` the same commands also work as
`wbsd ...`; the `python3 wbsd/wbsd.py` form always works.

Module data is private to the person who made it. The registry entry, the map and the opcode result contain
the module folder name, so keep them out of anything that is published; only the generic
sample under `examples/atlas/` is meant for publishing.

## First run on a fresh clone
The opcode and operand tables are not in the repo. If any command stops with "run python3
wbsd/build_tables.py --download first", run `python3 wbsd/build_tables.py --download` once
(it fetches the header files from the TLD mod's public repo), then retry. If the user already has a Module
System folder (the one holding `header_operations*.py`, `header_common.py`, `header_triggers*.py`), they can
pass its path instead: `python3 wbsd/build_tables.py "<that folder>"`. The generator reads the headers
as text and writes only inside `wbsd/`.

## Where things live
There are four knobs, all environment variables with defaults:
- Registry (`WB_REGISTRY`): path to the registry JSON. Default `modules.json` at the repo root,
  else `modules.example.json`. If you use the default and it is missing, copy
  `modules.example.json` to `modules.json` and edit the copy. Set `WB_REGISTRY` to use a
  separate (for example staging) registry file; then edit that file instead.
- Modules folder (`WB_MODULES_DIR`): the Warband `Modules` folder or a folder of copies.
  Registry paths are relative to it. Read-only for this skill.
- Atlas folder (`WB_ATLAS_DIR`, called `ATLAS_DIR` below): default `out/atlas` in the repo.
  All generated output goes there, never into a module.
- Cache folder (`WB_CACHE_DIR`): parse cache, default `.cache` in the repo. Point it somewhere
  outside any module folder if you must move it.

## Procedure
1. Get the module folder name (as it appears under the Modules folder) and its role. If the
   request or brief already states them, that is the answer; ask only when one is missing and a
   person is available. Roles:
   - `main`: the user's own mod, the comparison target for audits (only one).
   - `native`: the unmodified base game module.
   - `lineage`: an ancestor or sibling of the main mod, kept for family comparison.
   - `donor`: any other mod to mine for systems.
2. Pick a short lowercase `slug` (letters and digits, unique in the registry) and a readable
   `label`. Open the registry file first and refuse a slug that is already taken.
3. Confirm the module folder exists under the Modules folder and holds the compiled `.txt` data
   files. If the folder is missing or empty, stop and tell the user; do not guess a path.
4. Add one entry to the registry file (edit only that file):
   `{"slug": "...", "label": "...", "path": "<folder relative to the Modules folder>", "role": "..."}`
   If the user sets role `main` and another entry already has it, ask which one keeps it.
5. Confirm it parses: run `python3 wbsd/wbsd.py modules` and look at the NEW SLUG's line only
   (other registered modules may be absent; that is not your failure). It must show counts and
   no `MISSING`. `modules` lists every registered module and the first call can take about a
   minute. If the new line says `MISSING` or shows zero scripts, fix the registry path or
   report the problem.
   Timing: `modules`, `opcheck`, `report` all parse and cache modules.
   `report` took about 5 minutes on a module with 300k statements and `opcheck` is also slow,
   so run all of them in the background with a log file (`nohup ... > log 2>&1 &`) and read the
   whole log; a foreground call can die at a 2-minute tool limit. Later queries are fast.
6. Check for non-vanilla opcodes: `python3 wbsd/wbsd.py opcheck --mods <slug>`. The output starts
   with long ARITY MISMATCHES and TAG MISMATCHES blocks; they are noise for this purpose. The
   answer is the short section headed UNKNOWN OPCODES at the very end: record those opcode
   numbers and use counts (or "none"). They matter when the user's platform cannot run
   extension opcodes; see `atlas-audit` and its `references/investigation-guide.md`.
7. Generate the structural map: `python3 wbsd/wbsd.py report <slug>`. It creates `ATLAS_DIR/auto/`
   if needed and writes `ATLAS_DIR/auto/<slug>.md`. The file can exceed 1,000 lines on a large
   module; read these sections first: Basics, the Scripts-vs-Native counts, the scripts sorted by
   size, Periodic & event entry points, Menus/Presentations not in Native, then theme hits.
   The map does not name a module kind; judge it from the counts and the lineage line. Rule of
   thumb: most Native scripts identical and few new ones means near-Native; many modified
   Native scripts plus a large new-script count means a derived mod; few identical Native scripts
   means a total conversion. State it as your judgement.
8. Tell the user, in plain words: what was registered, that it parses, any non-vanilla opcodes
   (or "none found"), where the map is, and the three or four most notable things in it. Offer
   to run `atlas-audit` on the module next.

## Rules
- Change only the registry file and files under `ATLAS_DIR`. If a command would write inside a
  module folder, stop and report.
- Never point `WB_ATLAS_DIR`, `WB_CACHE_DIR` or `WB_REGISTRY` inside a module folder.
- Do not run `report all` or `opcheck` without `--mods` while any audit is running in parallel;
  they rewrite shared files and scan every module.
- Modules that ship only compiled tables (no source) are normal; the named disassembly is the
  decompiled view. Say so in the summary.

## Exit criteria
- The registry file has the new entry and no duplicate slug.
- `python3 wbsd/wbsd.py modules` shows the new slug's line with parse counts and no `MISSING`.
- The UNKNOWN OPCODES section of `opcheck --mods <slug>` is recorded (opcode numbers, or none).
- `ATLAS_DIR/auto/<slug>.md` exists and was read.
- The requester has been told the findings (a delegated run states them in its report) and nothing inside any module folder was changed.

## When uncertain
- Unsure of the role: ask one short question if a person is available; otherwise use `donor` and say so.
- Unsure where the module sits under the Modules folder: list that folder and ask; do not guess.
- A command fails or the module will not parse: stop, show the error, and leave the registry
  entry out (or mark the problem in your report) rather than continuing.
