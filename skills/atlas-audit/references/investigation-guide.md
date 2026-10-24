# Investigation guide (read once before the first audit)

## Command cheat-sheet (`python3 wbsd/wbsd.py ...`)
Run `--help` for the exact list. Most useful:
- `modules`: registry and parse stats.
- `hooks MOD`: every periodic and event entry point and what it calls.
- `explain MOD BLOCK`: callers, entry points, slots, globals, displayed text, Native status.
- `dis MOD BLOCK`: named disassembly (`--raw` for numeric).
- `system MOD BLOCK`: grow the subsystem around a block via calls and shared state.
- `roots`, `tree`, `callers`, `callees`: how a block is reached.
- `slot MOD OBJ N`, `slots MOD OBJ`, `global MOD NAME`, `refs MOD KIND NAME`: state.
- `text REGEX --mods M`, `grep REGEX --mods M`: search displayed text or disassembly.
- `diff MOD [OTHER]` (default vs native), `compare SCRIPT`, `similar MOD BLOCK --mods a,b`,
  `lineage`: ancestry and renamed copies.
- `closure MOD BLOCK... --into TARGET --hooks`: what a transplant needs and what collides.
- `opcheck --mods M`: opcodes outside the vanilla set.
- `report MOD`: writes `ATLAS_DIR/auto/<slug>.md`.
- `features [REGEX] [--cat C] [--module M]`, `feature ID`, `features-check`, `overlaps-apply`,
  `inventory`: the feature index.
- `batch -`: one command per line from standard input, one process. Use it first.
Batch quirks: a line is split on `|`, so a regex such as `text (a|b)` fails with "missing )";
run alternations as separate lines or as a direct (non-batch) call. Bare `prsnt:name` and
`mst:name` ids are rejected as ambiguous; add the trigger suffix (`prsnt:name/t0`,
`mst:name/t0:conseq`; the error lists the candidates). Example:

    python3 wbsd/wbsd.py batch - <<'EOF'
    hooks mymod
    explain mymod some_script
    refs mymod menu some_menu
    EOF

BLOCK is a script name or a block id such as `script:x`, `menu:town`, `mst:name/t3:conseq`,
`dlg:<n>:<id>:cond`.

## Finding candidate systems
The map lists scripts, but the largest are usually content tables (item scores, difficulties),
not systems. Recipe:
1. Take the biggest scripts by statement count from the map and discard pure data tables.
2. Read "Periodic & event entry points" (`hooks <slug>`): hourly and daily triggers with large
   call fan-outs are usually the live systems.
3. Run `refs` on presentations, menus and mission templates that are not in Native; who opens
   them shows the player-facing features.
4. For each candidate, `explain` it and note the slots, globals and text it touches.
5. Many "systems" are shared code imported from other mods. Check with `similar <slug> <block>
   --mods <other>`: a high shape score against another registered module means inherited code;
   record it as "inherits" instead of a new system.
6. Enough is usually two or three `explain`/`dis` calls per system, until you can state the
   trigger, the state it writes and what the player sees.

## Without a target module
With no `main` registered, `closure --into`, `compare` and `similar --mods <main>` cannot be
used. Still useful: `explain`, `dis`, `global`, `slot`, `slots`, `refs`, `text`, `hooks`, `diff`
against native, and `similar` against other registered modules.

## Known tool limits
- The first query on a module parses and caches it and can take minutes; `report` and `opcheck`
  are slow too. Run them in the background. Later queries are fast.
- `opcheck` prints long arity and tag mismatch blocks first; the answer is the UNKNOWN OPCODES
  section at the end.
- `explain` of an engine-hook script lists the script itself as its own only entry point. That is
  expected.
- `features-check` is a schema check only (enums, required keys); it does not check slot format
  or that evidence is true.
- Compilers that drop type tags (several total conversions): the tool resolves ids by argument
  role, but ids in untyped positions (for example a troop id inside an `eq`) stay plain numbers.
- Computed slot numbers print as `?`. Resolve with `dis` when it matters.
- `call_script` through a variable is not traced.
- Engine-called scripts are recognised only by the `game_*` prefix.
- `[every 0s]` means the block runs every frame.
- Ids differ per module, so compare by name. Some mods call scripts by bare integer; the tool
  marks those `{bare-int}` and does trace them.
- Static analysis never proves in-game behaviour. Only the user's own playtests do.

## Evidence and confidence rubric
Evidence kinds: call graph, slot writers and readers, global writers and readers, displayed text,
Native diff, shape match, trigger or menu wiring.
- `confirmed`: at least two independent kinds agree.
- `strongly-inferred`: one solid kind plus consistent context.
- `speculative`: plausible, not traced.
Menu or trigger wiring plus displayed text count as two kinds; `refs` plus `explain` alone is
one (call graph).
Each `evidence` entry is short: the command run or block id, and what it showed, for example
`"hooks mymod: strig:12 hourly calls script:foo_update"` or
`"slot mymod party 44: written only by foo_update, read by menu:town"`. See
`examples/atlas/features/` for complete records.

## Target status values
`absent`, `partial`, `present`, `different-implementation`. Judge it from `closure --into`,
`compare`, `similar` (renamed variants), `slot`, `global`. With no `main` module registered, omit
`target_status`, `target_evidence`, `conflicts`, `difficulty`, `risk`, `value` and
`recommendation` entirely; they are optional. Do not write "absent".

## Platform and slot notes
- Opcodes outside the vanilla set are a hard blocker if the user's platform cannot run an
  extension engine (they say so in `atlas-notes.md`). Check each new module with
  `opcheck --mods <slug>`. Some hits are harmless (a typo, or an opcode that is a no-op without
  the extension); say which. Features touching real extension use: `skip`, or "must be rebuilt
  without op N".
- Heroes often store relations with every troop at slot = that troop's index, so apparently free
  troop slots on lords and companions are NOT free. Check `slots` and `atlas-notes.md`.

## overlaps.json format
One JSON object: `{"mechanics": {"<mechanic-name>": ["<module>.<feature>", "<module>.<feature>", ...]}}`.
Each key is a mechanic implemented by several modules; each list holds the feature ids that
implement it (include the main mod's feature if it has one). An optional `"_doc"` string may sit
beside `mechanics`. `overlaps-apply` writes each feature's other listed ids into its `overlaps`
field and reports ids that do not exist; edit `overlaps.json`, then re-apply.
