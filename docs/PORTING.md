# Porting a feature between compiled Warband mods

This guide explains how to take a gameplay feature from one compiled module (the source) and
build it into another (the target) using this toolkit. The same procedure, in a form an AI coding
agent can follow, is the `atlas-port` skill in `skills/atlas-port/`. The skill that finds the
feature in the first place is `atlas-audit`; the one that registers modules is `atlas-add`. For many ports onto one target, see the `port-batch` skill.

There is no one-command port. A compiled module is a set of numbered tables, and a feature that
works in one mod rarely lands in another by copying. The toolkit gives you four things: tools that
show you what a feature is made of and what would clash (`wbsd`), a lossless writer (`wbasm`), a
safety harness for port scripts (`wbport`), and checks that prove the result is sound (`wbsd
verify-port`, `wbsd check-log`). You make the decisions and write a short Python script.

## What you need first

- **Both modules registered.** Register the source and the target in `modules.json`
  (see the Configuration section of the README, or use the `atlas-add` skill). Give the target the
  role `main`, which makes it the default for `closure --into`; otherwise name it with
  `--into <slug>` each time.
- **The feature's atlas record, if you have one.** `wbsd feature <id>` prints it. A record from
  `atlas-audit` tells you the hooks, scripts, slots and globals the feature touches, how sure the
  auditor was, and what it thought would collide. If there is no record, step 1 below is your own
  small audit.
- **A copy of your target mod folder, and a backup.** `wbport` and `wbasm` save in place, so work on a copy (`wbport` refuses a target inside the Modules folder).
- Python 3.9 or newer, standard library only. Run everything from the repo root.

## The safety rule

Only write into a module you own. A source mod, a donor, and the unmodified base game are read
only: the toolkit never writes into them, and neither should you. Port into your own mod folder or,
better, into a copy of it, check the copy, then replace your folder with it.

If the source mod's author published terms, follow them. Credit the author. If you cannot find
terms, ask before copying: that is an open question, not a blank.

## The procedure

### 1. Read the feature

    wbsd feature <id>
    wbsd explain <src> <block>
    wbsd system <src> <block>

`explain` tells you who calls a block, what entry points reach it, which slots and globals it
touches, what text the player sees, and whether it is a modified Native script. `system` grows the
whole subsystem around a block through calls and shared state, which is how you find the helper
scripts that never appear in the entry point's own code. Read the actual code too: `wbsd dis <src>
<block>` prints named disassembly. You want to be able to say, in plain words, what the player sees,
what triggers it, and what it stores.

Also run `wbsd opcheck --mods <src>` and look at the UNKNOWN OPCODES section at the end. Those are
operations outside the standard set (typically from a script extension). If the feature uses one,
see "Extension opcodes" under Traps.

### 2. Run the closure

    wbsd closure <src> <block> --into <target> --hooks

The closure is the feature plus everything it needs, followed all the way down. `--hooks` also
folds in the triggers and menus that call the feature. Pass several blocks in one call if the
feature has more than one root. Read **every** section, in the order it prints.

**What `--hooks` skips.** It adds the calling triggers and menus, but silently leaves out
`game_*` engine callbacks and any hub that makes more than 40 calls (a `game_start`-style script
would otherwise drag in half the module). The entry-point list is also cut at 30 lines. So an
empty or short list does not mean there are no other hooks: run `wbsd roots <src> <block>` and
`wbsd hooks <src>` to see what was left out, and decide yourself whether the feature needs one of
those hubs.

**Header and entry points.** `blocks in closure: N` is the size of the job. Then come the entry
points: the triggers, menus, dialogs or scripts that make the feature run in the source. You need
an equivalent in the target; step 5 shows how to bind one. A line such as `strig:165 (every -75h)`
names a trigger and its interval.

**SCRIPTS.** One line per script in the closure, with its statement count and a status:

- `identical in target`: the target already has the same code. Reuse it.
- `ABSENT in target (must be rebuilt)`: the target has no such script. You add it.
- `DIFFERS in target (N% similar) -> merge conflict`: both modules have a script of that name
  with different code. The percentage says how alike they are. This needs a human decision (step 3).

**RESOURCES.** Per kind (items, troops, factions, party templates, quests, menus, icons, skills ...),
by name because the numbers differ between modules: `N used, M missing in target: names`. The
missing names are your to-do list: each must be added to the target before the feature can refer to
it, or the feature must stop using it. Strings and quick strings are different: they print only
`N distinct`, with no missing list. Find which ones matter with `wbsd dis <src> <block>` (it shows
the text) and `wbsd text`.

**GLOBALS.** First, how many globals the closure uses and which of them also exist by name in the
target. A shared name may mean the same thing or may collide: check each with
`wbsd global <target> <name>`. Then `donor-only globals`: the ones the target lacks, which you will
have to create.

**SLOTS.** A slot is a numbered per-object variable (for example "party slot 44"); the same number
means different things in different mods. Each line gives the object, the slot number, how the
feature accesses it, and the target's usage:

- `free in target`: unused there, so the number can stay;
- `USED in target by N blocks ... -- POSSIBLE COLLISION`: the target uses it for something else.
  Confirm with `wbsd slot <target> <object> <n>`, choose a different number, and change every access
  in the ported code;
- `... same-named writers, likely same meaning`: the target writes it from a script of the same
  name, so it is probably the same thing. Verify before relying on it.

**NON-VANILLA OPCODES.** Printed only if the closure uses operations outside the standard set, with
counts, flagged `BLOCKER for a vanilla-engine target`. See "Extension opcodes" under Traps.

**behaviour profile.** A one-line summary of what kind of code this is (for example how much of it
is economy, AI or display). Use it as a sanity check that the closure is the feature you meant.

The closure follows direct `call_script` calls. It cannot see a call whose script number is
computed at run time, or a slot number held in a variable. Treat its list as a minimum (Traps).

### 3. Decide each item

Make a short table of every item in the closure and write one decision beside each.

| Situation | Decision |
|---|---|
| identical in target | **Reuse.** Copy nothing. |
| absent | **Copy** the logic: add a new script. |
| differs | **Adapt.** Read both versions side by side (`wbsd compare <script>`, `wbsd dis` on each). Either merge the source's change into the target's version, or leave the target's script alone and add a new script next to it. Look at the target script's callers (`wbsd callers`) before changing it: other features depend on it. |
| missing resource | **Add it first** (troop, item, string, ...), or cut the part of the feature that uses it. |
| collision | **Choose a free slot or global** in the target and use it everywhere. |
| uses an unsupported opcode | **Skip** the feature, or **rebuild** that part. |

Check whether the target already has a renamed copy of the feature or one of its scripts:
`wbsd similar <src> <block> --mods <target>` matches by what the code does, not by name.

### 4. Translate every id by name

In a compiled module, troops, items, scripts, globals, strings, quick strings, factions, menus and
slots are plain numbers. Script 585 in one mod is not script 585 in another. Copying numbers
across does not fail loudly: the game runs and quietly does the wrong thing.

For every operand in the source code:

1. Read its name from the named disassembly (`wbsd dis <src> <block>`).
2. Find the **target's** number for that same name.
3. Write the target's number.

In a `wbport` script step 2 is one call: `p.id(kind, name)` returns the target's number for a name
(`p.source_id(kind, name)` does the same for the source). These lookups need the generated header
tables, so run `wb-build-tables --download` once first (see the README). A missing name stops the
script and lists the closest matches. The name form each kind takes:

| Kind | Name form `p.id` / `p.source_id` take |
|---|---|
| global | with or without the `$` (`g_x` or `$g_x`) |
| script | with or without `script_` (a new script is created by its bare name) |
| troop, item, menu, menu option, string, quick string, party, party template, faction, quest, scene, skill, and the like | exactly as `wbsd dis` shows them, with the prefix (`trp_`, `itm_`, `menu_`, `mno_`, `str_`, `qstr_`, `p_`, `pt_`, `fac_`, ...) |

To copy code from the source, do not retype its operands: `p.source_doc("scripts")` is a read-only
view of the source's table, and `p.remap(statement)` returns a new statement with the same opcode
and flags and every named operand translated from the source id to the target id by name:

    src = p.source_doc("scripts").by_name("source_script")
    idx = p.add_script_once("source_script", [p.remap(s) for s in src.statements()])

`remap` returns a new statement with the same opcode and flags. It translates script, global,
string, quick string, troop, item, party, party template, faction, scene, mission template, menu,
quest, skill, sound, particle system, scene prop, mesh, presentation, track, tableau and animation
operands by name, and keeps untagged numbers, registers, locals and icons as they are. A record the
target lacks is a `PortError` naming it: add it first (with another tool) or cut that use.

`wbport` can read and rewrite the code tables (scripts, simple triggers, triggers, menus,
presentations, conversation, mission templates, tableau materials). It cannot add troops, items,
strings, quick strings, factions, icons or menus, so a missing resource of those kinds is a job for
your usual editor for that table (see the list in step 5). When you have written the new code,
`wbsd dis` on the patched copy must show the target's own names on every operand; if you see a
wrong name, you wrote a wrong number.

### 5. Write the port script

Keep an untouched copy of the target (call it BASE) and make a second copy to work on (WORK).
Write a short Python script that uses `wbport`, which wraps `wbasm` and does the chores every port
script must get right:

    import sys
    sys.path.insert(0, ".")                      # the repo root
    import wbport
    from wbops import CALL_SCRIPT, ASSIGN, SCRIPT, GVAR

    with wbport.Port("my_feature", sys.argv[1], source="/path/to/source_module") as p:
        gv  = p.id("global", "my_flag")                         # target's number, by name
        idx = p.add_script_once("my_feature_tick", [p.statement(ASSIGN, GVAR(gv), 1)])
        p.add_simple_trigger_once(24.0, [p.statement(CALL_SCRIPT, SCRIPT(idx))],
                                  calls="my_feature_tick")
        p.menu_add_call_once("menu_name", "option_id", "my_feature_tick")
        print("\n".join(p.notes) or "changed")

What `Port` does for you:

- **Refuses the live folder.** A target inside the configured Modules folder is rejected. Work on a
  copy.
- **Backs up once.** Each table is copied to `<file>.bak_before_<name>` the first time; an existing
  backup is never overwritten.
- **Checks the round trip.** A table that does not serialize back to the bytes it was read from
  stops the port: the parser does not understand that file.
- **Is idempotent.** The `*_once` helpers (`add_script_once`, `add_simple_trigger_once`,
  `menu_add_call_once`) do nothing on a second run and say so in `p.notes`. Run the script twice:
  the second run must change nothing.
- **Checks before it writes.** On a clean exit every loaded table is checked (round trip, line
  endings, try/end balance on every new or changed block). If any check fails, or the script raised
  an exception, nothing is written. `dry_run=True` does all the checks and writes nothing.
- **Logs.** A line is appended to `ports.log.jsonl` in the target when something changed.

`PortError` is the one exception a port script should let stop it. Other points:

- **Append new scripts at the end.** `add_script_once` appends and returns the index. A script with
  that name but different statements is refused, not overwritten.
- **Build statements from cited opcodes.** `wbops.py` holds named opcodes (`CALL_SCRIPT`, `ASSIGN`,
  `GVAR`, `V`, ...), each with a decoded example from real data in its comment. Build with
  `p.statement(opcode, operand, ...)`. Do not invent an opcode number: a wrong number gives silently
  broken logic, not an error. If the one you need is not in `wbops.py`, find a script that uses it
  (`wbsd grep`) and read what its operands do first.
- **Bind it.** The feature must be called from somewhere: `add_simple_trigger_once` for a periodic
  call, `menu_add_call_once` to add a call to an **existing** menu option, or splice a
  `call_script` into an existing script through `p.doc("scripts")` (a list from
  `script.statements()`, then `script.set_statements(list)`; there are no jump offsets in this
  format, so inserting well-formed statements is safe). `wbport` has no helper to add a new menu
  option, because the menu's option count must change too; prefer reusing an existing option or
  cutting the menu part.
- **Other edits.** `p.doc(table)` returns the plain `wbasm` document for any of the eight tables.
  Edit it in place; `Port` still checks and saves it.

**What `wbasm` and `wbport` can write.**

| | |
|---|---|
| Can **append** | new scripts (`append_script`, `add_script_once`); new simple triggers (`append_trigger`, `add_simple_trigger_once`) |
| Can only **edit** | the body of an existing script; existing entries in `triggers.txt`; existing menus and their options (conditions and consequences, `menu_add_call_once`); dialogs; presentations; mission templates; tableau materials |
| Cannot add at all | troops, items, strings, quick strings, menus, menu options, `triggers.txt` entries, icons (also factions, party templates, quests) |

Snippets for each step, with the guards, are in `skills/atlas-port/references/port-snippets.md`;
the brief to fill in before you start is `skills/atlas-port/references/port-brief.md`.

### 6. Verify

Static checks cannot prove the game works, but they catch the common failures. One command runs
the main ones:

    python3 wbsd/wbsd.py verify-port BASE WORK --expect my_feature_tick

It prints one PASS or FAIL line per check and exits 1 on any FAIL:

- **append-only:** no name list lost or moved an entry, no table shrank, existing dialogs,
  triggers and simple triggers are an unchanged prefix, and no existing script body changed
  unless you allowed it. Only script bodies are gated by `--allow-edit`. Edits to menus and
  menu options, presentations, mission templates and the like are not flagged by append-only at
  all (look at them yourself); edits to dialogs, triggers and simple triggers always fail it, and
  `--allow-edit` does not rescue them.
- **untouched:** every file in BASE is still in WORK, and the only files that differ are tables
  `wbport` may write (or files you list with `--touched`). A table that was rewritten with no
  real change fails too. Extra files that exist only in TARGET are INFO, not a FAIL.
- **reachable:** every new script, plus every script named in `--expect`, has a path from a
  trigger, menu, dialog, presentation, mission template or an engine hook. This is the same
  caller graph as `wbsd roots`. "Reachable" means a static call path: guards (conditions that may
  always exit early) are not evaluated. A script that exists but that nothing calls is not a port.
- **opcodes:** no opcode outside the opcode reference appears in a new or changed block.

Flags:

| Flag | Use it when |
|---|---|
| `--expect S,...` | you want these scripts (new or old) proven reachable. It adds checks, never waives one. |
| `--allow-edit S,...` | the port changes the body of an existing script, such as a host you spliced a call into. Write down why for each name. |
| `--touched FILE,...` | the port changes a file `wbport` does not write. |
| `--assume-reached S,...` | the only way to a script is a `call_script` whose script id sits in a variable, which the tool cannot trace. It is printed as WAIVED. Write down why. It does not apply to a new `game_*` script: that must be an existing engine hook, or the check fails. |

Show that the check can fail: run it once on a doctored copy (for example WORK without the hook
call) and see the FAIL, then restore. Also run:

1. **Names.** `wbsd dis <slug> <new_script>` shows the target's names on every operand (register
   WORK in `modules.json` as its own slug; the entry's `path` is joined onto `WB_MODULES_DIR`, so
   an absolute path to a copy outside the Modules folder works).
2. **Re-run the port script.** It must print "already present" lines and change no file.

### 7. Test in the game

A static check proves the file is well formed, not that the feature works. Load the patched mod,
start a new game, trigger the feature the way a player would, and compare it with what you saw in
the source mod. Then load an older save and see what happens (Traps, first item). Keep the backup so
you can roll back. If your in-game result disagrees with a check, trust the game and debug from what
you saw.

Then scan the game's log:

    python3 wbsd/wbsd.py check-log <path to rgl_log.txt>

It prints each problem record as `line N [kind] text` and exits 1 for script errors, invalid ids,
"unable to map" records and missing-file records. **Any line that names a material, texture or mesh
is treated as cosmetic: it is counted and shown but never fails the run.** So a clean exit does not
mean nothing is missing. If a model, picture or surface is missing in game, read those cosmetic
lines yourself.

### 8. Record provenance

Compiled files cannot hold comments, so keep the record beside your port script and in your mod's
credits file if it has one:

- the source mod (name and version);
- the block ids you took (`script:...`, `strig:...`, `menu:...`);
- the author of the source mod, credited by name;
- its usage terms, or "terms not found, asked on <date>".

## Traps

**Saved games.** A new script is code, and code is not stored in a save. The risks are new global
variables, new troops and items, and state that an old save never initialised: values the feature
sets only once (for example in `game_start`), or slots it expects to be filled already. A save made
before the port may load with those empty or misread. Test on a new game, state this to whoever uses
the mod, and do not promise old saves keep working.

**Script indexes shift.** A `call_script` holds a script's position in the list. Inserting a script
anywhere except the end changes the position of every later script, and every call to them now
points at the wrong code. `append_script` only appends; `remove_trailing_script` only removes the
last entry. Do not work around either.

**Computed slots.** If the slot number is in a variable (`troop_set_slot` with a local as the slot),
`wbsd slot` and the closure's slot list cannot see it. Search the source code for the slot setters
(`wbsd grep`), and read the code that sets the variable.

**Calls through variables.** A script number that is computed, not written, makes the call graph
blind: the callee shows no callers, and the closure may miss the callee entirely. Check
`wbsd hooks` and read the code around any `call_script` whose operand is a variable.

**Engine-called `game_*` scripts.** The game itself calls a set of scripts by name, with a fixed
parameter list and a fixed meaning for the return value. If the feature changes one of these in the
source (`wbsd explain` shows its Native status), changing the target's copy changes the behaviour of
the whole game. Port the change carefully, and never rename or reorder these.

**Extension opcodes.** Some mods use operations from a script extension such as WSE. The target's
platform may not run them. If `opcheck` lists them for the source and the feature uses them, either
skip the feature or rebuild that part with the standard operations. Never guess a replacement
opcode.

**Text.** Strings carry the source's setting, names and tone. Re-theme them for your mod and add
them as strings of your own (add new strings with another tool; `wbport` can't); do not point at the source's string numbers.

**Another writer wins.** If the target already writes the same variable later in the same pass, your
addition is overwritten. Find the later writer (`wbsd global`, `wbsd slot`) and place your call after
it, or change that site.

## If something goes wrong

Restore the `*.bak_before_<name>` files `wbport` made (or the copy you worked on is untouched, so discard it).
Nothing in the source module or in your registry was changed except the extra slug, which you can
remove. Then rerun from step 3 with the failing item decided differently.

## Hard-won lessons

Thirteen rules that hold for any port. The full list, each with a reason and a way to check it, is
in `skills/atlas-port/references/lessons.md`.

1. Presence is not reachability: confirm something actually calls what you added.
2. A late write loses: the last write wins, and a value written after its reader is never seen.
3. A check that never failed is not evidence: break it once and watch it fail.
4. A green check is necessary, never sufficient: test in the game.
5. Compiled records are fixed-width and positional, and ids are append-only: find things by name or
   shape, never by index or a pinned total.
6. Donor ids do not map: port names and rebuild. Some donors compile untagged ids.
7. Check a trigger's leading guard before appending to it.
8. Know what a range's bounds are used for (an index or modulus, not just membership) before
   widening it.
9. Slot collisions are silent: take new slots from a declared list.
10. Confirm the deployed copy is the one you edited before trusting a playtest.
11. Copy statements, do not rebuild them: the negation and this-or-next flags live in the opcode.
12. Read tables as bytes (CRLF).
13. Never read a command's exit status through a pipe.
