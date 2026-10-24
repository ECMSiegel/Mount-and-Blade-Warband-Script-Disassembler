# Contributing

Thanks for helping. This is a small hobby tool, so keep changes small and focused.

## Run the tests

From the `wbtools` folder, standard library only:

    python3 -m unittest discover -s tests -v

Without game data, the tests that need a module or the generated tables are skipped, and the
built-in fixture tests still run. With game data, point `WB_MODULES_DIR` at your Warband `Modules`
folder (Native is the default module under test) and run `python3 wbsd/build_tables.py --download` once.
See [tests/README.md](tests/README.md) for the other switches.

CI also runs `python3 tools/hollow_check.py tests`, which fails on any test that can never fail
(for example an assertion on a constant). Run it before you push.

## Refactoring? Use the golden harness

If you change how the tools work inside, prove the output did not change. `golden/capture.py`
records the output of a list of commands for a reference copy and for your copy, then compares them.
Steps are in [golden/README.md](golden/README.md).

## Rules

- Round-trip output must stay byte-identical: parsing a module file and writing it back must give the same bytes.
- Changes should not alter what `wbsd` commands print unless the change says so.
- Do not put game data or Module System files in a pull request: no module `.txt` files, no Module System headers,
  no generated `opref_data.py` or `header_tables.py`. Tests use small invented fixtures.
- Standard library only; no new dependencies.

Bugs and ideas: use the issue templates.
