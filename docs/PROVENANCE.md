# Provenance of the opcode and operand tables

The opcode and operand tables come from TaleWorlds' Mount & Blade: Warband Module System
(`header_operations*.py`, `header_common.py`, `header_triggers*.py`), which TaleWorlds publishes for
modders. The Module System remains TaleWorlds'. It is widely redistributed in mod source releases.

## What this repo does with it
This repo does not redistribute those tables. `wbsd/build_tables.py` reads your own copy of the Module
System headers as text (`python3 wbsd/build_tables.py <Module System folder>`) and writes
`wbsd/opref_data.py` and `wbsd/header_tables.py`. Both are git-ignored. Because they are generated from
your copy, the tools work with whatever Module System variant you have.

`wb-build-tables --download` does the same from a public source: it fetches `header_operations_wb.py`,
`header_common.py` and `header_triggers_wb.py` from the TLD mod's public repo
(github.com/tldmod/tldmod, `ModuleSystem/Header/`), pinned to commit
`561ceaf04e12ec1fba19cf39aad07a2981f14910`, into a temporary folder, builds the tables from them as text and
deletes them. Nothing is stored in this repo. At that commit the files are byte-identical to the ones the
shipped tables were built from.

## What the repo does include
- `wbsd/table_overlay.py`, the author's corrections: 118 argument-name lists keyed by opcode number
  (`OP_SIGNATURES`, 300 argument names in all), 20 argument-spelling aliases (`ARG_ALIASES`), the fallback
  lists `LIST_DEFAULTS` (7 `DEPTH` and 9 `GLOBAL_LHS` opcode names), and one trigger-event name,
  `ti_on_switch_to_map`.
- The short opcode names used by `wbops.py` (about 57 opcode constants), `wbasm.py` (the `TRY_*` names),
  `wbsd/analyze.py` (the hard-coded `call_script`), `wbsd/build_tables.py` (`TAG_KINDS`, 25 `tag_*` names)
  and `docs/FORMAT.md`. These are functional identifiers needed to read and write the file format.

## Licence
The MIT licence ([LICENSE](../LICENSE)) covers this repo's own code and docs.
