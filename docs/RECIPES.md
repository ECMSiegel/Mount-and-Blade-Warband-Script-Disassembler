# Recipes

Three worked examples. Every command below was run for real and the excerpts are copied from its output (long outputs are cut to a few lines).
The commands are written as `wbsd ...`; `python3 wbsd/wbsd.py ...` does the same thing.
The module names are registry slugs (`wbsd modules` lists them). `native` is Warband's own Native module;
`vc` is a second module (here TaleWorlds' own DLC).

## A. Who reads and writes this global?

Before you rename or remove a global variable, find everything that touches it.

    wbsd global native '$g_talk_troop'

```
$g_talk_troop (global #115): 7 writer blocks, 906 reader blocks
 WRITERS:
   dlg:0:dlga_start:close_window:cond "{!}Warning:_This_line_is_never_displayed._It_is_just_for_sto"
   dlg:1929:dlga_member_chat:sacrificed_messenger_1:cond "Yes_{sir/madam}?"
   script:npc_decision_checklist_party_ai
 READERS:
   dlg:0:dlga_start:close_window:cond "{!}Warning:_This_line_is_never_displayed._It_is_just_for_sto"
```

(The full output lists every writer and reader; the excerpt keeps three writers and one reader.)
Each line is a block id (`script:`, `dlg:`, `menu:`, `strig:` ...) you can feed to `wbsd dis`, `wbsd explain` or `wbsd roots`.
Quote the `$` so your shell leaves it alone.

## B. Plan a feature port with `closure --into`

You like a feature in a second module and want it in another. `closure` works out what you would have to bring along and what would clash.

    wbsd closure vc add_jetty_system --into native --hooks

`vc` is the module the feature comes from, `--into native` is where it is going (leave it out to use the registry's `main` module),
and `--hooks` also pulls in the triggers and menus that call the feature. The first output line names the two modules and is skipped here.

**The closure** is the feature plus every script, trigger and menu it calls, followed all the way down.
**Entry points** are what makes the feature run in the donor; with `--hooks` they are part of the closure.

```
blocks in closure: 67
entry points the feature hangs off in the donor (2):
   script:game_start
   strig:165 (every -75h)
SCRIPTS:
   abort_quest                                              327 stmts  DIFFERS in target (65% similar) -> merge conflict
   add_jetty_system                                          16 stmts  ABSENT in target (must be rebuilt)
   add_log_entry                                             80 stmts  identical in target
```

The `SCRIPTS:` list is the conflict check. For each script in the closure:
`identical` means the target already has it and nothing is needed; `ABSENT` means you must add it;
`DIFFERS` means both modules have a script of that name with different code, so you have to merge by hand (the percentage says how alike they are).

Next come the resources the feature uses, listed by name because ids differ between modules. `missing in target` is your to-do list of things to add:

```
   icon: 2 used, 1 missing in target: map_flag_extra01
   menu: 3 used, 1 missing in target: menu_reconstruct_pre2049
   skill: 2 used, 0 missing in target
```

Then the globals (names that exist in both may mean the same thing or may collide) and the slots. A slot is a numbered per-object variable, and the same number can mean different things in each module:

```
   faction        13    s6           free in target
   faction        49    s12          USED in target by 2 blocks (writers e.g. script:initialize_faction_troop_types) -- POSSIBLE COLLISION
```

`free in target` means you can keep the number; `POSSIBLE COLLISION` means the target already uses it, so pick a new slot and update every access in the ported code.
Use recipe A on any global the list flags.

## C. Find a renamed copy of a script

Modules often copy a script and rename it slightly. `similar` finds it by what the code does, not by name.

    wbsd similar native appoint_faction_marshall --mods native,vc

```
   named  94%  shape 100%  vc       appoint_faction_marshal                          64 stmts
   named  12%  shape  26%  native   faction_conclude_feast                           90 stmts
```

`named` compares the statements with their names; `shape` compares only the sequence of opcodes, so it still matches when variables were renamed.
Here `vc` has the same script under a one-letter-different name. Follow up with `wbsd dis native appoint_faction_marshall` and `wbsd dis vc appoint_faction_marshal` to see the exact differences.
