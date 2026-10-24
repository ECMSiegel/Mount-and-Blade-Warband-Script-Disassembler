---
name: atlas-port
description: Port a gameplay feature from one compiled Warband module into another with the wbtools toolkit (wbsd, wbport), translating every id by name and proving the new code is reached. Use when the user says "atlas-port", "port this feature", "bring X from the donor into my mod", or has chosen a feature record from an audit.
---

# Atlas port

Moves one feature (found by `atlas-audit`) from a source module into a target module you own.
`wbsd` reads modules, `wbport` writes the port (it wraps `wbasm` with backups, round-trip checks
and idempotent helpers), `wbsd verify-port` proves the result. Human version: `docs/PORTING.md`.
Many ports in a row: use the `port-batch` skill, which calls this one per port.

Run commands from the wbtools repo root as `python3 wbsd/wbsd.py ...`. Prefix Python runs with
`PYTHONDONTWRITEBYTECODE=1`. Full command list: `python3 wbsd/wbsd.py --help`.

## Inputs (check first)
- Source and target are registered (`atlas-add`); the target has role `main`, or pass `--into <slug>`.
- The feature record, if any: `python3 wbsd/wbsd.py feature <id>`. Without one, step 0 is the audit.
- A writable copy of the target module folder outside the Modules folder. `wbport.Port` refuses a
  target inside Modules unless told otherwise; do not tell it.
- Read `references/lessons.md` before step 1. It is short and every rule is a past failure.

## Safety rule
Never edit a module you do not own. Sources, donors and the base game are read only. Write only
into a copy of your own mod, then copy the result over once it passes. Never put the registry,
cache or atlas folders inside a module folder.

## Procedure
0. **Facts first.** Before building, re-derive every claim in the brief or atlas record with
   `wbsd`: the block names exist, `explain` and `roots` show the entry points claimed, `slot` and
   `global` show who really uses the numbers, `opcheck --mods <src>` lists the opcodes (without `--mods` it runs on every registered module). Write each
   mismatch in the brief ("record said X, tool shows Y"); the tool output wins. Name lookups in
   `wbport` (`port.id`, `port.source_id`) need the generated header tables: if they are missing,
   run `wb-build-tables --download` once (see the README) before going on.
1. **Read the feature.** `feature <id>`, `explain <src> <block>`, `system <src> <block>`, `dis`.
   You must be able to say what the player gets, what triggers it, and what it stores.
2. **Closure.** `closure <src> <block>... --into <target> --hooks`. Read every section (guide
   below). `--hooks` skips `game_*` roots and hubs over 40 calls, and lists at most 30 entry
   points; check `roots` and `hooks <src>` for what it left out.
3. **Fill the port brief** from `references/port-brief.md` (a file beside the port script). Its
   sections: what the player gets, source blocks, closure summary, decisions (reuse, copy, adapt),
   id map by name, slots and globals chosen, save posture (live, latch or new game), verify plan
   (fail-first), STOP AND ASK. Decide every closure item:
   - identical in target: reuse; absent: copy the logic; differs: open both (`compare`, `dis`) and
     adapt, or add a new script beside the target's. Never overwrite a script other features use
     without reading its callers;
   - missing resource (troop, item, faction, menu, icon ...): `wbport` cannot add it (see "What can
     be written"); add it with your usual editor first, or cut that part;
   - names: write exact compiled names as `wbsd dis` shows them (`script_...`, `trp_...`, `menu_...`,
     `mno_...`), not shortened ones. `wbport` and `verify-port` accept script names with or
     without `script_`; new scripts are created by their bare name (`add_script_once("x")`);
   - slot or global collision: take numbers only from a free list you write in the brief, each
     checked with `slot` / `global` against the target.
   Stop at any STOP AND ASK item and ask the user before building.
4. **Write the port script** with `wbport` (skeleton in `references/port-snippets.md`). Look up
   every id by name in the target (`p.id(kind, name)`); never copy a donor number. To copy source
   code, use `p.source_doc(table)` and `p.remap(statement)` (ids translated by name, flags kept;
   the snippet is "Copy a source script, remapping ids by name"). Name forms per kind are in
   `port-snippets.md`. Use the `*_once` helpers so a second run reports "already present" and
   changes nothing. Re-theme strings as new target strings (add new strings with another tool;
   `wbport` can't).
5. **Run it on a copy.** Keep an untouched BASE copy of the target, copy it to WORK, run the
   script (`python3 port_<name>.py WORK`) with `dry_run=True` first, then for real. Run any Python that may exceed ~2 minutes in
   the background with a log.
6. **Verify (fail-first).** `python3 wbsd/wbsd.py verify-port BASE WORK --expect <script>,...`
   (checks append-only, untouched files, reachable, opcodes; exit 1 on any FAIL). `--expect`
   adds scripts that must be reachable. Scripts reached only through a computed `call_script`
   cannot be traced: waive them with `--assume-reached <script>,...` (explicit, printed in the
   report), and only with a reason written in the brief. It never applies to a new `game_*`
   script: that must be an existing engine hook. If the port edits an existing script (a
   spliced host), pass `--allow-edit <host_script>,...`, each name with a written reason in
   the brief. If it changes files `wbport` does not write, list them with `--touched FILE,...`. Show the check can fail first: run
   it on a doctored copy (for example without the hook call) and see the FAIL, then restore.
   "Reachable" is a static call path; guards are not evaluated. Only script bodies are gated by
   `--allow-edit`; menu, dialog and presentation edits are not flagged by append-only, so read
   them yourself. Extra files that exist only in TARGET are INFO.
7. **Test in game.** Give the user exact steps: new game or load save, the entry point to
   trigger, what they should see, and that the backup allows rollback. Then
   `python3 wbsd/wbsd.py check-log <rgl_log.txt>` on the game's log (script errors, invalid ids,
   missing files; exit 1 if any). Material, texture and mesh warnings are only counted as
   cosmetic, so check them yourself. Their report outranks every static check.
8. **Record provenance.** Source module, block ids taken, source author (credit them), usage
   terms. `wbport` appends a line to `ports.log.jsonl` in the target; also write a note beside the
   script and update the project credits file if any. When copying the result into the live
   module, copy only the changed tables; never the `*.bak_before_<name>` backups or `ports.log.jsonl`. Unknown terms: ask before copying.

## What can be written
- `wbport` helpers: `add_script_once` (append at the end), `add_simple_trigger_once`,
  `menu_add_call_once` (add a call to an existing option's consequences or conditions).
- Other edits (a call spliced into a host script, a trigger or dialog body): `p.doc(table)` gives
  the `wbasm` document; edit it, and the exit checks still run. Tables: scripts, simple_triggers,
  triggers, menus, conversation, presentations, mission_templates, tableau_materials.
- Cannot add: troops, items, strings, quick strings, menus, menu options, icons, factions, party
  templates, quests. Add them with another tool, or cut the feature's use of them.

## Reading the closure output
Long guide in `docs/PORTING.md`. In print order:
- `blocks in closure` and `entry points`: the feature plus what it calls, and what runs it.
- `SCRIPTS`: `identical in target` (nothing to do), `ABSENT` (add it), `DIFFERS (N% similar)` (decide).
- `RESOURCES`: per kind `N used, M missing in target: names`; the names are your to-do list.
  Strings print only a count: find them with `dis` and `text`.
- `GLOBALS`: same name may mean the same or collide (`global`); donor-only globals must be created.
- `SLOTS`: `free in target`, or `USED ... POSSIBLE COLLISION` (pick another number).
- `NON-VANILLA OPCODES ... BLOCKER` only if present: see Traps. Closure follows direct `call_script` only.

## Traps
- **Existing saves.** New scripts are code, not save data. New globals, troops, items and state an
  old save never initialised can load empty or misread. Say so; also test a new game.
- **Script indexes.** Append only; never insert or reorder.
- **Computed slots and calls.** A slot or script index held in a variable is invisible to `slot`
  and `callers`. Search with `wbsd grep`; read `explain` for "Native status".
- **Engine-called scripts.** `game_*` scripts have fixed parameters; changing one changes the game.
- **Extension opcodes.** If `opcheck --mods <src>` lists opcodes the target cannot run, skip or
  rebuild with vanilla ops. Never guess an opcode: `wbops` holds only cited ones.
- **Several writers.** A later write in the same pass overrides yours; place the call after it.
- **Raw wbasm.** Only for an edit `wbport` has no helper for, via `p.doc(...)`. Do not build a
  second parallel writer.

## Exit criteria
- Only a copy or your own mod folder was written; no source, donor or base module changed.
- The brief is filled, every closure item has a recorded decision, every id was looked up by name.
- The port script is re-runnable (second run says already present) and `verify-port` printed PASS
  after a fail-first demonstration; any `--assume-reached` has a written reason.
- The user has in-game test steps, the save posture, and a backup; `check-log` was run if a log exists.
- Provenance is recorded. The port is called CLAIMED until the user confirms it in game.

## When uncertain
- Terms of the source mod unclear or forbid reuse: stop and ask before copying.
- A name has no match in the target and cannot be added: report it, ask whether to cut that part.
- Unsure whether the target has a renamed copy: `similar <src> <block> --mods <target>`, then ask.
- `verify-port` shows FAIL on reachable: report the port unfinished, not done.
- Unsure a file is yours to edit: treat it as not yours and work on a copy.
- Unsure how a `wbport` method behaves: read its docstring in `wbport.py` and try `dry_run=True`.
