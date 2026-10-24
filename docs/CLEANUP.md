# Changes from the original toolkit

This toolkit started as a set of private helper scripts for one mod. For publishing it was copied,
cleaned up and sped up. This is the short list of what changed and why. The behaviour of the tools
is the same: for the commands that were compared, output is byte-identical to the original, except as listed below.

## Opcode and operand tables are generated, not shipped

The opcode names, ids, signatures and key codes come from TaleWorlds' Module System, which this
repository does not redistribute. `python3 wbsd/build_tables.py
--download` (or `... <Module System folder>` for your own copy) reads the Module System headers and writes two local, git-ignored files,
`wbsd/opref_data.py` and `wbsd/header_tables.py`. Without them the `wbsd` command line prints a short
"run build_tables first" message and the tests that need them are skipped. The author's own corrections
are shipped as `wbsd/table_overlay.py`; see [PROVENANCE.md](PROVENANCE.md).

## Faster

Parse and index results are cached, and a few queries were reworked. Most commands are 50 to 98
percent faster. Details: [PERFORMANCE.md](PERFORMANCE.md) and [PROFILE.md](PROFILE.md).

## Fixes and small changes

- `wbasm` now treats opcodes 16 (`try_for_prop_instances`) and 17 (`try_for_players`) as block
  openers, like `wbsd` already did. Native does not use them; some mods do. A test requires the two
  tools' lists of openers to stay equal.
- `explain` output is deterministic: ties are ordered by count (highest first), then by first use.
- A bad `modules.json` now gives a one-line `error: ...` and exit code 1 instead of a traceback.
- `overlaps.json` with a malformed member now gives a clear error instead of a crash.
- `wbops.py`: removed `TROOP_RAISE_PROFICIENCY_LINEAR` (opcode 1523), which Native never uses and so
  could not be backed by real data. Every citation comment was regenerated from Native with
  `gen_evidence.py`. The check that cited statements really exist was not weakened.
- Removed a few unused helpers (`KIND_TAG`, `PREFIX`, `name_of`). Kept `wbasm.block_depth_ok()` and the
  unused `wbops` constants, which are part of the documented vocabulary.
- Removed hard-coded paths and mod-specific wording from code, comments and tests.
- `golden/profile.py` was renamed `golden/prof.py` because it shadowed Python's `profile` module.
- `golden/capture.py --only` refuses to overwrite an existing output unless `--force` is given.

## Duplicated constants are on purpose

`wbasm`/`wbops`/`gen_evidence` and `wbsd` each define the same format constants. `wbsd` is an
independent reader that must run without `wbasm`, and a parity test cross-checks the two. A test
(`test_duplicate_constants_agree`) pins the shared values equal.

## Tests

- `tests/` is a package; `python3 -m unittest discover -s tests` and `python3 -m unittest tests.test_wbops` both work.
- Tests that assert facts about one particular mod live in local-only `tests/test_*_modspecific.py`
  files and are skipped unless `WB_TEST_MODULE` names that mod. See [../tests/README.md](../tests/README.md).
- The suite passes on Python 3.9, 3.12 and 3.14.
