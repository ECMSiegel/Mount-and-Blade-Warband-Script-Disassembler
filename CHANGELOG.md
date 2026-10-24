# Changelog

## 0.1.0 — initial release

- `wbasm.py` parses a module's compiled `.txt` files and writes them back byte for byte.
- `wbdis.py` turns compiled scripts into readable, named disassembly.
- `wbops.py` lists operations that are known and cited from real data.
- `wbsd` is a read-only command line over every module in your registry: `dis`, `explain`, `callers`, `callees`, `tree`, `roots`.
- Cross-references for globals, slots and resources (`global`, `slot`, `slots`, `refs`), and regex search over names, code and displayed text (`grep`, `text`).
- Cross-module tools: `diff`, `compare`, `similar` (finds renamed copies), `lineage`, and `closure --into` (plans a feature port and lists conflicts).
- A feature atlas (`features`, `feature`) and a per-module auto report (`report`).
- Parse and index caches, so repeat queries are fast; `batch` runs many queries in one process.
- Opcode tables are built from your own Module System with `wbsd/build_tables.py`; none are redistributed.
- `wbport.py`: a safety harness for port scripts (`Port`, `id`, `add_script_once`, `add_simple_trigger_once`, `menu_add_call_once`): backups, round-trip and block-depth checks, idempotent edits, nothing written on failure. `source_doc` and `remap` copy a source statement into the target, translating every referenced record by name.
- `wbsd verify-port` proves a port is append-only, touches only expected files, is reachable and uses known opcodes; `wbsd check-log` scans a game `rgl_log.txt` for script errors, invalid ids and missing files.
- `tools/hollow_check.py` finds tests that can never fail.
- Agent skills in `skills/`: `atlas-add`, `atlas-audit`, `atlas-port`, `port-batch` (many ports onto one target); human guide `docs/PORTING.md`.
- Standard library only; Python 3.9 or newer.

For how this differs from the original private toolkit, see [docs/CLEANUP.md](docs/CLEANUP.md).
