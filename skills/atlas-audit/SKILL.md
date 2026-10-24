---
name: atlas-audit
description: Audit a registered Warband module for gameplay systems and record them as feature records in the atlas, then group shared mechanics across modules. Use when the user says "atlas-audit", "audit this donor", "find systems worth porting", "what does this mod do", or wants a feature atlas built or refreshed.
---

# Atlas audit

Finds the gameplay and quality-of-life SYSTEMS inside a compiled module, checks whether the
user's main mod already has them, and records each as a feature record plus a plain-English
narrative. Investigation only: nothing here changes any module.

No module source exists for compiled mods; the tool's named disassembly is the decompiled view.
Run commands from the wbtools repo root as `python3 wbsd/wbsd.py ...` (after `pip install -e .`
the same commands also work as `wbsd ...`; the `python3 wbsd/wbsd.py` form always works). Details, limits, the
evidence rubric and a command cheat-sheet are in `references/investigation-guide.md`; read it
before the first audit.

## Setup (once per atlas)
1. The module must be registered (`atlas-add` skill). `python3 wbsd/wbsd.py modules` lists it.
2. `ATLAS_DIR` is env `WB_ATLAS_DIR`, default `out/atlas`. If `ATLAS_DIR/atlas-notes.md` does
   not exist, create it from `references/project-notes.template.md` and ask the user to fill
   the headings in (baseline, blocked opcodes, used slots, scripts not to touch). Open it before
   judging any feature. An empty section means "no house rule", not "nothing is used". If nobody
   is available to fill it in, the audit may proceed with the unfilled file; say so in the
   narrative.
3. The comparison target is the registry entry with role `main`. If none is registered, the audit
   still runs but records FACTS ONLY: omit `target_status`, `target_evidence`, `conflicts`,
   `difficulty`, `risk`, `value` and `recommendation` from every feature (they are optional in
   the schema; never write "absent" for them). State this in the narrative and in your report.
4. Open the module's structural map `ATLAS_DIR/auto/<slug>.md` (made by `atlas-add`, or run
   `python3 wbsd/wbsd.py report <slug>`).
5. Timing: the first query on a module parses and caches it (minutes on a large module), and
   `report` can take about 5 minutes. Run those in the background with a log file; later
   `explain`, `dis` and `batch` calls are fast.

## Auditing one module
Outputs (the only per-module files you write):
- `ATLAS_DIR/features/<slug>.json` = `{"module": "<slug>", "features": [ ... ]}`. Field list and
  allowed values: `docs/ATLAS.md`. Leave `overlaps` as `[]`.
- `ATLAS_DIR/modules/<slug>.md`: the narrative.

Method:
0. **Make sure `ATLAS_DIR/modules/`, `ATLAS_DIR/features/` and `ATLAS_DIR/auto/` exist**; create
   any that is missing (`report` creates `auto/` itself).
1. **Batch first.** Pipe one command per line into `python3 wbsd/wbsd.py batch -` (a heredoc or
   file works well) so indexes are built once; a lone call costs seconds of start-up. Prefer
   `--mods` on any search, because unscoped `grep`, `text` and `similar` scan every module (15 to
   60 seconds). Batch quirks (a `|` splits the line; bare `prsnt:`/`mst:` ids are ambiguous) are
   in the guide's cheat-sheet.
2. **Systems, not content.** Skip troop or item stat changes, textures, models, sounds and
   cosmetic swaps unless they are part of a larger system. To FIND candidates, follow the
   "Finding candidate systems" recipe in the guide; the biggest scripts are often content tables.
3. **Hooks, scripts, state, effect.** Start with `hooks <slug>`, then `explain`, `dis`, `system`,
   `roots`, `tree`, `slot`, `slots`, `global`, `refs`, `text`, `grep`. Infer the system from
   behaviour: trigger or menu or dialog or presentation, to the scripts it calls, to the slots and
   globals they write, to what the player sees. For oddly named scripts use `explain`, `system`,
   `dis` and displayed text.
4. **Lineage.** Near-Native modules hide mechanics in modified Native scripts (see "Modified
   Native scripts" in the map, with a similarity score; `diff <slug>` prints the same list, so use
   the map if it is open and `diff` for a fresh view. `explain <script>` prints the Native status
   of one script, which is the quickest check for engine-hook scripts such as
   `game_get_troop_wage`). For a mod derived from another registered one, run
   `diff <slug> <parent>` and record inherited systems briefly as
   "inherits <parent>.<feature>" instead of re-cataloguing. Use the **shape** score from `compare`
   and `similar` (opcode-sequence match); it sees through renumbered ids and compilers that drop
   type tags, where name-based comparison disagrees. Compare by NAME, never by id.
5. **Status against the target.** With a `main` module, set `target_status` for every feature
   from tool output, not by assumption: `closure <slug> <block> --into <main-slug> --hooks`, `compare <script>`,
   `similar <slug> <block> --mods <main-slug>,<parent>` (the target may hold a renamed copy),
   `slot <main-slug> <object> <n>`, `global <main-slug> <name>`. Put concrete slot, global,
   script-name, trigger and menu collisions in `conflicts`. Check `atlas-notes.md` for used slots
   before calling a slot free.
   With NO target, omit all judgement fields (Setup 3) and gather evidence with the commands that
   need no target: `explain`, `dis`, `global`, `slot`, `slots`, `refs`, `text`, `hooks`, `diff`
   against native, and `similar --mods` against other registered modules. `closure --into`,
   `compare` and `similar --mods <main>` need a main.
6. **Confidence.** `confirmed` needs at least two independent kinds of evidence (call graph, slot
   writers, global writers, displayed text, Native diff, shape match, trigger or menu wiring).
   Menu or trigger wiring (`refs`, `hooks`) plus displayed text (`text`) count as two kinds;
   `refs` plus `explain` alone is one kind (call graph). One solid line plus consistent context is
   `strongly-inferred`; a plausible untraced reading is `speculative`. Cite block ids in every
   feature. Never invent; keep the uncertainty.
7. **Non-vanilla opcodes.** `opcheck --mods <slug>` shows opcodes outside the vanilla set. If
   `atlas-notes.md` says the platform cannot run them, a feature touching them is
   `recommendation: skip`, or note "must be rebuilt without op N".
8. **Save incrementally.** Save the JSON every 3 to 5 features and run
   `python3 wbsd/wbsd.py features-check`. That is a schema check only: it does not verify the
   slot format (`object:slot`), that evidence strings are true, or that blocks exist. Aim for
   about 10 to 25 features per module, ordered by code volume (the map) then theme hits. Use
   the category list in `docs/ATLAS.md`.
9. **Narrative.** `ATLAS_DIR/modules/<slug>.md`, plain English: kind of mod; compiled tables only
   and whether that was enough; analysis limits; systems found, ranked by value to the target
   (by general value if there is none); bugs and oddities; relation to Native and to the
   target; a "Tool notes" heading for tool problems. Say what each system does for the player.
10. **Inventory.** Even for a single module, run `python3 wbsd/wbsd.py inventory` at the end
   (it works without `overlaps.json`) and read `ATLAS_DIR/FEATURE_INVENTORY.md` back.
11. Finish with: features written (count), top five by value, anything blocked.

## Parallel runs
Several audits may run at once (one helper agent each) when helper agents exist. While they do, do not
run `report all`, `opcheck` without `--mods`, or `lineage`, and never edit tool code. They rewrite
shared files or scan every module. Record tool problems under "Tool notes" and work around them.
A lone auditor may run them.

## Coordinator (several modules)
1. Confirm each module is registered. Save a short checkpoint of the plan (modules, order, who
   does what) to a file in `ATLAS_DIR` first. Give every auditor: the module slug, the exact
   output files, "touch nothing else", and "done" (count, top five, blockers). If sub-agents
   exist, run audits in parallel; otherwise run them one after another yourself.
2. After all finish: run `features-check`; read the narratives and the top features.
3. Find mechanics that several modules implement (use `features`, `features --cat C`). Save
   `ATLAS_DIR/overlaps.json` grouping their feature ids; format in `references/investigation-guide.md`.
4. Run `python3 wbsd/wbsd.py overlaps-apply`, then `python3 wbsd/wbsd.py inventory`. This writes
   `ATLAS_DIR/FEATURE_INVENTORY.md`. Report the best candidates and the overlaps to the user.

## Porting a chosen feature
Out of scope here. Generic approach: take the feature's `closure ... --into <main-slug>`
output, read the donor mechanism end to end, copy behaviour into the target with a note of where
it came from, and prove the new code is reached. If the `donor-feature-port` skill exists, use it.

## Exit criteria
- `ATLAS_DIR/features/<slug>.json` exists and `features-check` reports it clean.
- Every feature has block-id evidence and a confidence label that follows the rubric. With a
  target, each has a `target_status` set from tool output; with none, the judgement fields are
  omitted (not set to "absent") and the narrative says so.
- `ATLAS_DIR/modules/<slug>.md` exists and is non-empty.
- `inventory` was run and `FEATURE_INVENTORY.md` read; for a coordinated run also
  `overlaps.json` written and `overlaps-apply` run.
- Nothing inside any module folder or any tool source file was changed.
- The requester has the feature count, top five and blockers (a delegated run states them in its report).

## When uncertain
- A needed house rule is missing from `atlas-notes.md`: ask one short question if a person is
  available; otherwise treat the slot as unverified and the opcode as unrunnable, and say so.
- A system is ambiguous: write it as `speculative`, say what you could not trace.
- The tool misbehaves: note it under "Tool notes", work around it, never edit tool code.
- No sub-agents available: run the audits in sequence and tell the user it will take longer.
