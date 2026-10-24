# Perisno 1.5.0 (slug `perisno`, role donor)

## What kind of mod it is
A large total-conversion-style mod: its own world (Perisno, with its own kingdoms, races such as dwarves and giants, and a Zann invasion storyline), but built on Native's engine scripts. Against Native: 1113 scripts, of which 202 are identical to Native, 282 are modified Native scripts, 629 are new, and 126 Native scripts are absent. 26,878 code blocks and 312,219 statements: roughly 3.5x Native by statement count. It shares a lot of code with several other registered modules (diplomacy/"dplmc" scripts, Freelancer, auto-loot, trade-ledger style helpers), so many "systems" here are imported rather than original.

## Tables only, and was that enough
Only the compiled `.txt` tables exist; no source. The tool's named disassembly was enough to follow every system below: call graphs, slot and global writers, and displayed text all resolve. The weak spots are presentations and long input handlers (key bindings, UI layout), which can be read but are expensive to understand statement by statement.

## Limits of this audit
- No target ("main") module is registered, so nothing here says whether a system is missing from anyone's mod; the judgement fields are left out on purpose. `atlas-notes.md` was not filled in (no house rules were supplied).
- Static analysis only. Nothing was played.
- 19 systems out of a mod with several hundred scripts' worth of content. Not covered in depth: ~19 companion backstory/dialog systems, the culture troop-tree and character-rankings presentations, the key-configuration screen, minimap/world-map presentations, cheat menus, banner assignment, weddings/love-interest logic, quests (199), the many scenes, and the many dozens of mission templates besides hunting.
- One non-vanilla opcode: 575, used once (`trig:98:conseq`). It is the only extension-engine hit; the rest of the `opcheck` output is arity and tag-type noise (see Tool notes).

## Systems found
1. Faction strategic AI (`decide_faction_ai_dk2`): a full periodic rethink per kingdom. Heavy closure (89 blocks).
2. Formation and battle-group AI for field battles: sizeable (many hundreds of statements) and reached from three mission templates; it uses team and agent slots.
3. Chamberlain, constable recruiters and retainer training: gives the player a delegated economy and a recruiting pipeline; one hourly scanner script drives it.
4. Hourly budget processing, patrol wages and budget report.
5. Custom troop re-equip with a quality score, and companion auto-loot gear upgrade.
6. Item equip bonuses with tooltips (skill bonuses from named items).
7. Rebels, named outlaw leaders and unemployed-mercenary warbands.
8. Freelancer service (player enlists under a lord) and the Freelancer Guild contracts. The mod itself warns the Freelancer minimod was reported buggy.
9. Smaller QoL: exchange-screen hotkeys, trade ledger, bank/gambling, start-of-game hard mode and fog of war, starting-orders screen.
10. Flavour: fire-arrow explosions, hunting herds, enterable inn.

What each does for the player is in the feature records.

## Bugs and oddities
- 126 Native scripts are absent from the module, so scripts that Native calls may be missing or replaced (engine `game_*` hooks are still defined).
- Many scripts are never reached by the static call graph (all of `array_*` beyond a handful, `order_skirmish_begin_end`, `cf_infantry_aggresive_ai`, `add_wood_and_water_to_villages`). They may be dead, called by computed id, or called from outside the tables.
- Several tag-type mismatches (a troop passed where a party is expected, etc.) appear in `opcheck`, probably sloppy scripting or a compiler that drops tags; not proven bugs.
- Leftover debug text (`DEBUG`, `ERROR_IN_THE_...`) in the faction AI and budget scripts.
- Debug and cheat menus (`menu_et_cheats`, `camp_cheat_*`) are reachable from normal menus.

## Relation to Native and to the target
Relation to Native: heavily modified (`diff perisno` vs Native). Highest-impact Native scripts are rewritten: `game_get_troop_wage` (114 vs 43 stmts), `game_get_item_extra_text` (593 vs 54). Relation to a target: not assessed, none registered.

## Tool notes
- `opcheck --mods perisno` prints a long list of arity and tag mismatches before the short UNKNOWN OPCODES section; the useful result (opcode 575) is at the very end.
- `batch` splits a line on `|`, so regexes with alternation (`text (a|b) ...`) fail with "missing )". Use separate lines.
- Block ids for presentations and mission templates need a trigger suffix (`prsnt:bank/t0`, `mst:deer_hunting/t0:conseq`); the bare form errors with a candidate list.
- `explain` on an engine hook script like `game_get_item_extra_text` shows itself as its own entry point.
- `report perisno` took about 5 minutes the first time (parse and cache plus report); `modules` about 1 minute.
