# Tests

Run from the repo root:

    python3 -m unittest discover -s tests -v
    python3 -m unittest tests.test_wbops        # one file

`tests/` is a package, so both forms work. Python 3.9 or newer.

The tests read a module folder from `WB_MODULES_DIR` (default: the Steam Modules folder).
They default to the `Native` module; set `WB_TEST_MODULE` to a folder name to test another one.
The tests only read the module; anything they write goes to temporary folders.

Other settings:

- `WB_TEST_ALL_MODULES=1`: `test_every_module_loads` loads every module in the registry instead of just the one under test (slow).
- `WB_HEADERS_DIR=<Module System folder>`: runs the table-reproduction test in `test_build_tables.py`, which rebuilds the tables from your headers and compares them with the generated files. Skipped when unset.
- Tests that need the generated tables (`wbsd/opref_data.py`, `wbsd/header_tables.py`) are skipped until you run `python3 wbsd/build_tables.py --download`.

## Tests for one specific mod

Some tests check facts about one specific mod's data rather than Native's. They live in local-only files
`tests/test_*_modspecific.py` (git-ignored) and run only when `WB_TEST_MODULE` names that mod:

    WB_TEST_MODULE="<mod folder name>" python3 -m unittest discover -s tests -v

On Native they are simply absent, so a normal run never fails on them.

## Which tests need data

Run anywhere, with no Warband data and no generated tables (this is what CI runs):

- `test_fixture_module.py`: uses the invented demo module in `tests/fixtures/minimod/` and the invented headers in `tests/fixtures/headers/`. It checks that `wbasm` round-trips the fixture files byte for byte, builds the tables from the fixture headers into a temporary copy of `wbsd/` (your real generated tables are never touched), and runs `wbsd dis`, `callers`, `explain` and `closure --into` on the fixture in a subprocess with its own temporary registry, modules folder and cache.
- `test_wbport.py`: the `wbport` harness (backups, idempotence, refusals, nothing written on failure) on temporary copies of the demo module.
- `test_verify.py`: `wbsd verify-port` and `wbsd check-log` on doctored copies of the demo module and invented log text.
- `test_hollow_check.py`: `tools/hollow_check.py` flags tests that can never fail and leaves real ones alone.
- `test_build_tables.py`, `test_cli_registry.py`, `test_config.py`, and the parts of `test_wbops.py` / `test_wbsd.py` that do not read a module.

Need a real module folder (skipped with "no module data at ...; set WB_MODULES_DIR" when it is missing): `test_wbasm.py`, `test_wbdis.py`, the corpus tests in `test_wbops.py` and `test_wbsd.py`.

Need the generated tables (skipped until you run `build_tables.py`): `test_wbsd.py`, `test_atlas.py`, `test_caches.py`, and the by-name tests in `test_wbport.py` (the `Lookups` and `Remap` classes: `id`, `source_id`, `source_doc`, `remap`).

CI also runs `python3 tools/hollow_check.py tests`, which exits 1 if any test can never fail.

## Generic tests (must pass on Native)

`test_wbasm.py`, `test_wbdis.py`, `test_wbops.py`, `test_wbsd.py`, `test_atlas.py`, `test_caches.py`. `test_wbsd.py` finds the registry
slug of the module under test; if that module is not in the registry its tests are skipped.
