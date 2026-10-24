# Port snippets (wbport)

Short, illustrative. Names in angle brackets are yours; write exact compiled names as `wbsd dis` shows them (`script_...`, `trp_...`, `menu_...`, `mno_...`). Run it as `python3 port_<name>.py <target copy>`. Run from the wbtools repo root, on a
copy of the target module folder (`WORK`), never on a module you do not own. By-name lookups need
the generated header tables (`wb-build-tables --download`, once). `wbport` and `verify-port` accept
script names with or without `script_`; a new script is created by its bare name. "Name forms"
below lists every kind.

## Skeleton of a re-runnable port script

```python
import sys
sys.path.insert(0, ".")                       # the wbtools repo root
import wbport
from wbops import CALL_SCRIPT, ASSIGN, SCRIPT, GVAR, V   # see wbops.py for the full cited list

WORK = sys.argv[1]       # the target copy: the integrator passes its own copy here
SRC = "<source module folder, read only>"   # constant, or sys.argv[2]

with wbport.Port("<port_name>", WORK, source=SRC) as p:     # add dry_run=True for a trial run
    gv = p.id("global", "<flag_name>")                       # target number, looked up by name
    host_idx = p.id("script", "<existing_target_script>")    # PortError names close matches
    idx = p.add_script_once("<new_script>", [p.statement(ASSIGN, GVAR(gv), 1)])
    p.add_simple_trigger_once(<interval_in_hours>, [p.statement(CALL_SCRIPT, SCRIPT(idx))],
                              calls="<new_script>")
    p.menu_add_call_once("<menu_name>", "<option_id>", "<new_script>")
    print("\n".join(p.notes) or "changed")                   # "already present" lines on a rerun
```

What `Port` does for you: refuses a target inside the Modules folder, backs each table up once
(`<file>.bak_before_<port_name>`), stops if a table does not round-trip, checks block depth and
line endings before writing, writes nothing if anything fails, and appends a line to
`ports.log.jsonl`. `PortError` is the one exception to catch or let stop the script.

Read `p.id(kind, name)` for the target and `p.source_id(kind, name)` for the source. `p.has_script(name)`
tests presence. The `*_once` helpers are idempotent; a second run changes nothing. `p.source_doc(table)` is a
read-only wbasm document of the source (never saved).

## Name forms

| Kind | Name form `p.id` / `p.source_id` take |
|---|---|
| global | with or without the `$` (`g_x` or `$g_x`) |
| script | with or without `script_` (a new script is created by its bare name) |
| troop, item, menu, menu option, string, quick string, party, party template, faction, quest, scene, skill, and the like | exactly as `wbsd dis` shows them, with the prefix (`trp_`, `itm_`, `menu_`, `mno_`, `str_`, `qstr_`, `p_`, `pt_`, `fac_`, ...) |

A wrong form is a `PortError` that lists the closest matches.

## Operand helpers

`wbops` has `TRP`, `ITM`, `STR`, `QSTR`, `FAC`, `PT`, `PARTY`, `SCENE`, `MENU`, `SKL`, `REG`, `GVAR`,
`SCRIPT`, `V`. They only wrap a number; the number must be the TARGET's, from `p.id(kind, name)`
(or from `p.remap` for a statement copied from the source).
Build statements with `p.statement(opcode, operand, ...)`.

## Append a script, trigger or menu call (all idempotent)

```python
idx = p.add_script_once("<new_script>", body)       # appended at the end; same body again = no-op;
                                                     # different body under that name = PortError
p.add_simple_trigger_once(<hours>, [p.statement(CALL_SCRIPT, SCRIPT(idx))], calls="<new_script>")
p.menu_add_call_once("<menu>", "<option_id>", "<new_script>", where="consequences")
```

`body` is a list of statements; try_begin/try_end must balance or `PortError` is raised.

## Copy a source script, remapping ids by name

```python
src = p.source_doc("scripts").by_name("<source_script>")       # read-only view of the SOURCE
body = [p.remap(s) for s in src.statements()]                   # ids re-looked-up by name in the TARGET
idx = p.add_script_once("<source_script>", body)                # appended at the end; same body again = no-op
```

`remap` returns a new statement with the same opcode and flags. It translates script, global,
string, quick string, troop, item, party, party template, faction, scene, mission template, menu,
quest, skill, sound, particle system, scene prop, mesh, presentation, track, tableau and animation
operands by name, and keeps untagged numbers, registers, locals and icons as they are. A record the
target lacks is a `PortError` naming it: add it first (with another tool) or cut that use.

## Splice one call into an existing host script (no helper: use the document)

```python
host = p.doc("scripts").by_name("<host_script>")
stmts = host.statements()
call = p.statement(CALL_SCRIPT, SCRIPT(idx))
if not any(s.tokens() == call.tokens() for s in stmts):
    stmts.insert(<position>, call)               # no jump offsets to fix
    host.set_statements(stmts)
```

Insert where the block depth is the one you want (not in the middle of an `else_try` chain unless
you mean to). `Port` checks block depth on every changed block before it writes anything.

`wbsd verify-port` needs `--allow-edit <host_script>` for this route.

## Raw wbasm note

`p.doc(table)` returns the plain `wbasm` document (tables: scripts, simple_triggers, triggers, menus,
conversation, presentations, mission_templates, tableau_materials). Use it only for an edit with no
helper above, and edit in place: `Port` still checks and saves it. It cannot add menu options or
any record kind listed as "cannot add" in `SKILL.md`. To copy a statement from the source, build it
from the parsed `Statement` and change only its operands (lessons rule 11).

## After the script

Run it twice: the second run must change nothing (`p.notes` says "already present"). Then
`wbsd verify-port BASE WORK --expect <new_script>` (see `SKILL.md` step 6), and `callers`, `roots`,
`dis` on the work copy once it is registered as its own slug.
