# Port brief (template)

Copy this file beside the port script and fill every section. Facts come from `wbsd` output, not
from memory or the atlas record; where they disagree, write both and trust the tool.

## 1. What the player gets
Two or three plain sentences: what they see, what triggers it, what it changes.

## 2. Source blocks
Source module slug, block names (scripts, menus, triggers) and the entry points that run them.
Author and usage terms of the source (or "unknown: ask").

## 3. Closure summary
Paste the key numbers from `closure ... --into <target> --hooks`: blocks in closure; scripts
identical / absent / differs; missing resources; donor-only globals; slot collisions; non-vanilla
opcodes. Note what `--hooks` skipped (`game_*`, hubs over 40 calls, entry points past 30).

## 4. Decisions
One row per closure item.

| Item | Decision (reuse / copy / adapt / cut) | Why |
|---|---|---|

## 5. Id map by name
Every troop, item, script, global, string, menu and slot used, source name -> target name and
target number looked up by `p.id(...)`. Never a donor number.

## 6. Slots and globals chosen
Declare here every new slot and global you will use, each with the free-list entry it came from and the `slot` / `global`
check that showed it unused in the target. In a batch, these come from the shared allocation list.

## 7. Save posture
Pick one and say why: **live** (works on an existing save), **latch** (needs a one-time
initialiser the first time the save loads), or **new game** (old saves misread it).

## 8. Verify plan (fail-first)
- The exact `verify-port BASE WORK --expect ...` command.
- The doctored copy that must FAIL first (for example the hook call removed), and the expected FAIL line.
- Any `--allow-edit` script (an existing script the port edits, such as a spliced host), each with
  the written reason; any `--touched FILE` for files `wbport` does not write.
- Any `--assume-reached` script, with the written reason it is reached only through a computed call (never a new `game_*` script).
- In-game steps for the player and the log file to run `check-log` on.

## 9. STOP AND ASK
Open questions that block building (unknown terms, missing resources that need a decision, a
changed shared script, extension opcodes). Empty only if truly none. Ask before building.

## 10. Mismatches found
Claims in the atlas record or earlier notes that the tools did not confirm.
