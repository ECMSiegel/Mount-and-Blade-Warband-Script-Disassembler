# Profile of the slow commands (original code, warm cache)

What was profiled: the original code in `<snapshot>/<main mod>/_dev` (Python 3.14, cProfile; "main" is the registry slug of a large total-conversion mod, ~21 MB of compiled text, 16,552 blocks), with the
pickle cache already warm. All file:line values name the ORIGINAL; the copy is identical apart from paths.
Paths below are relative to `_dev/`.

Reading the numbers: the machine was heavily loaded by other sessions, so seconds are unreliable and
cProfile itself roughly doubles runtimes. Trust the percentages (share of total profiled time), not the
seconds. "self" = time inside the function itself; "cum" = including everything it calls.
Raw `.prof` files and logs: `<scratch>/prof/`. Re-run with
`python3 golden/prof.py --tool-dir DIR "<wbsd args>"` or `--test FILE [--cwd MODULE_DIR]`.

| Command | Profiled total | Load avg (1/5/15 min) at start |
|---|---|---|
| `modules` | 12.2 s | 48.9 / 66.2 / 157.8 |
| `explain main game_start` | 19.2 s | 42.0 / 63.4 / 154.6 |
| `callers main game_start` | 17.3 s | 42.5 / 61.7 / 151.4 |
| `similar main game_start` | 57.5 s | 38.7 / 59.7 / 148.6 |
| `grep change_screen_equip_other --mods native` (see note) | 26.9 s | 156 / 108.6 / 128.1 |
| `test_wbasm.py` | 57.4 s | 227.5 / 182.7 / 157.1 |
| `wbsd/test_wbsd.py` | 44.4 s | 353.9 / 184.0 / 155.4 |

Note on `grep`: the default run (all 19 modules) was started at 03:19 and killed after more than 10
minutes (the brief's stop condition), so it was re-profiled on `--mods native` only. Native has 9,116 of
roughly 340,000 blocks, so the all-module cost is about 35-40x what is shown here.

## modules

Warm run loads all 19 module pickles just to print three numbers each.

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `_pickle.load` (builtin) | called at `wbsd/corpus.py:488` | 60.8 | 60.8 | 19 | Unpickles every module's full parsed corpus (every statement of every block) |
| `load` | `wbsd/corpus.py:478` | 31.4 | 93.1 | 19 | Its own time is almost all garbage-collector passes triggered while the pickle builds millions of tuples (see GC test below); also the `_fingerprint` check |
| `<genexpr>` in `main` | `wbsd/wbsd.py:81` | 2.6 | 3.4 | 324,213 | `sum(len(b.stmts) for b in m.blocks)` walks every block just to count statements |
| `sum` (builtin) | called at `wbsd/wbsd.py:81` | 1.0 | 4.4 | 19 | Same statement count |
| `len` (builtin) | `wbsd/wbsd.py:81` | 0.8 | 0.8 | 326,242 | Same statement count |

Everything else is under 0.5 % each. Import machinery (including building the opcode table at
`wbsd/opref.py:85`) is 0.28 s, about 2.3 %: not significant.

## explain main game_start

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `xref` | `wbsd/analyze.py:152` | 34.8 | 67.2 | 25,668 | Cross-references every block of main and native, though `explain` needs one script's closure |
| `ModuleIndex.__init__` | `wbsd/analyze.py:264` | 10.2 | 80.5 | 2 | Loops over all blocks calling `xref` and building five lookup tables (callers, globals, slots, refs, unknown ops) |
| `decode` | `wbsd/analyze.py:38` | 8.7 | 8.7 | 1,473,027 | Called per operand while cross-referencing; pure Python bit-shifts and a dict lookup |
| `_pickle.load` (builtin) | called at `wbsd/corpus.py:488` | 6.4 | 6.4 | 2 | Unpickles main and native (the "native:" comparison line) |
| `Counter.__init__` | `collections/__init__.py:605` | 4.1 | 5.8 | 51,909 | Each `xref` builds a `Counter` (`x.opcodes`, `x.unknown`) per block |

Next: `bare_kind` `analyze.py:23` (3.7 % self, 364,074 calls), `_role` `analyze.py:48` (3.5 %, 502,615),
`dict.get` (3.4 %, 835,784).

## callers main game_start

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `xref` | `wbsd/analyze.py:152` | 41.7 | 79.1 | 16,552 | Cross-references all 16,552 main blocks to find callers of one script |
| `decode` | `wbsd/analyze.py:38` | 9.7 | 9.7 | 1,214,403 | Per-operand decode inside `xref` |
| `ModuleIndex.__init__` | `wbsd/analyze.py:264` | 9.4 | 91.1 | 1 | The index build is 91 % of the command; the answer itself is trivial (0 callers) |
| `bare_kind` | `wbsd/analyze.py:23` | 4.6 | 8.3 | 299,160 | Classifies bare ids per operand |
| `_pickle.load` (builtin) | called at `wbsd/corpus.py:488` | 4.1 | 4.1 | 1 | Single-module unpickle |

Also `_repr_operand` `analyze.py:145` (4.1 % self, 144,974 calls), `list.append` (3.8 %, 548,574),
`_role` `analyze.py:48` (3.7 %, 421,497).

## similar main game_start

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `_pickle.load` (builtin) | called at `wbsd/corpus.py:488` | 27.6 | 27.6 | 19 | Unpickles every module (20 `registry.load` calls, 19 distinct) |
| `shape_seq` | `wbsd/queries.py:495` | 18.2 | 18.2 | 10 | Builds a list of tuples for a ~7,500-statement block. Only 10 calls yet 18 %: inferred to be garbage-collector passes on the huge heap, not the list comprehension itself (not tested) |
| `corpus.load` | `wbsd/corpus.py:478` | 9.7 | 37.9 | 19 | Own time = GC during unpickling, as in `modules` |
| `named_stmt` | `wbsd/analyze.py:214` | 9.7 | 15.1 | 159,090 | Builds the "named" form of each statement for the Jaccard comparison, recomputed for every candidate block |
| `xref` | `wbsd/analyze.py:152` | 8.2 | 15.8 | 16,552 | Index build for main (`get(slug)` at `queries.py:12`), needed only to resolve the script name |

Also `Counter` counting (`_collections._count_elements`, 4.7 % self, 32 calls).

## grep change_screen_equip_other --mods native

Native only (see note above).

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `xref` | `wbsd/analyze.py:152` | 15.0 | 28.1 | 9,116 | `get()` (`queries.py:12`) builds the full cross-reference index, which `grep` never uses |
| `disassemble` | `wbsd/analyze.py:112` | 14.8 | 47.4 | 9,116 | Renders every block to text lines, one call per block |
| `stmt_text` | `wbsd/analyze.py:89` | 14.7 | 30.3 | 85,326 | Renders each statement (every statement in the module) |
| `decode` | `wbsd/analyze.py:38` | 8.5 | 8.5 | 348,225 | Per-operand decode (index build plus rendering) |
| `operand_text` | `wbsd/analyze.py:60` | 7.2 | 14.7 | 157,456 | Renders operands inside `stmt_text` |

Also `ModuleIndex.__init__` `analyze.py:264` (5.6 % self, 35.7 % cum) and `corpus.load` `corpus.py:478`
(4.5 % self, 7.4 % cum). Of `grep`'s 85,326 statements, all are rendered; the loop at `queries.py:624` builds
the whole line list for a block before searching it, and only then stops at the first matching line.

## test_wbasm.py

Run with cwd = the module folder (the test reads `triggers.txt` etc. from cwd; with cwd = `_dev` it fails
with FileNotFoundError). 25,095 checks, all green.

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `re.Pattern.split` (builtin) | called at `wbasm.py:203` | 18.5 | 18.5 | 32,110 | Regex split of each raw line into tokens and separators |
| `_split_line` | `wbasm.py:198` | 15.7 | 45.3 | 32,110 | Per-line tokenizer: the split plus `fullmatch` checks and `bytes.decode` on every token |
| `parse_statements` | `wbasm.py:120` | 13.4 | 18.5 | 40,879 | Pure-Python parse of the statement stream; the tests parse every block (`test_wbasm.py:73` `_roundtrip_block`) |
| `bytes.decode` (builtin) | called at `wbasm.py:214` | 10.9 | 10.9 | 6,138,687 | One decode call per token (6.1 million) |
| `parse_n_statements` | `wbasm.py:151` | 7.0 | 9.6 | 66,982 | Recursive statement parser |

Also `Statement.tokens` `wbasm.py:114` (4.1 % self, 10.0 % cum, 278,860 calls, called from `emit_statements`
`wbasm.py:143` for the re-emit half of the round-trip), `list.extend` (3.4 %), `Statement.__init__`
`wbasm.py:105` (3.3 %, 1,064,463 calls). `Line.__init__` `wbasm.py:228` is 38.2 % cum. The test is
dominated by the parser it exists to test, so speedups here are in `wbasm.py`, and the brief says not to
change its byte-exact logic: only mechanics (fewer decodes, caching splits) are fair game.

## wbsd/test_wbsd.py

| Function | File:line | Self % | Cum % | ncalls | Why |
|---|---|---|---|---|---|
| `_pickle.load` (builtin) | called at `wbsd/corpus.py:488` | 34.4 | 34.4 | 19 | `test_every_module_loads` (`test_wbsd.py:85`, 61.1 % cum) loads all 19 modules |
| `corpus.load` | `wbsd/corpus.py:478` | 28.9 | 63.8 | 19 | Own time = GC during unpickling |
| `parse_statements` | `wbasm.py:120` | 7.5 | 11.2 | 1,265 | `test_loader_parity` (`test_wbsd.py:32`, 36.3 % cum) parses main with wbasm to compare against the loader |
| `re.Pattern.split` (builtin) | `wbasm.py:203` | 5.2 | 5.2 | 9,004 | Same tokenizer as above |
| `_split_line` | `wbasm.py:198` | 4.1 | 12.5 | 9,004 | Same tokenizer as above |

Also `test_loader_parity` itself (3.3 % self, 1 call) and `bytes.decode` (3.3 %, 1,510,624 calls).

## Hypotheses

**H1: `modules` is dominated by unpickling all modules just to print stats. CONFIRMED.**
`registry.load` accounts for 93 % of the command (11.3 of 12.2 s; 19 calls), and the printed output is
three numbers per module. Inside that, `_pickle.load` is 60.8 % self and `corpus.load`'s own time is another
31.4 %. The extra 31 % is garbage collection: in-process, loading `acan` took 0.84-1.09 s CPU with GC on
and 0.50-0.51 s with `gc.disable()`; `vc` took 0.53-0.58 s versus 0.31-0.33 s (about 40 % saved). The only
other work is the statement count at `wbsd.py:81` (3.4 %). Fix direction: store those counts (scripts,
blocks, statements) in a small sidecar next to the pickle, keyed on the same fingerprint, so `modules`
never unpickles; and disable GC around unpickling anywhere modules are loaded.

**H2: `grep` re-disassembles every block of every module per query. CONFIRMED, with a second cost.**
`disassemble` is called once per block (9,116 calls for native's 9,116 blocks) and is 47.4 % cumulative,
with `stmt_text` rendering all 85,326 statements. The loop is `queries.py:621-628`. It runs for every
module in `registry.slugs()` per query and nothing is cached across runs, so the all-module run is
roughly 35-40x this and took more than 10 minutes under profile (43 s at baseline, unprofiled and on a
quiet machine). Unexpected second cost: `grep` calls `get()` (`queries.py:12`), which builds the full
`ModuleIndex` (`analyze.py:264`, `xref` for every block): 35.7 % cumulative, work `grep` never uses. A
`registry.load` would do. Unpickling is only 7.4 %.

## Other findings for T5

- `explain` and `callers` spend 80-91 % of their time building the whole-module `ModuleIndex`
  (`analyze.py:264`, driven by `xref` at `analyze.py:152` and `decode` at `analyze.py:38`), then use a
  sliver. `similar` builds it too (15.8 %). A persisted index, or a lazy one, is the lever.
- Garbage collection is a hidden cost everywhere modules are unpickled (`modules`, `similar`,
  `test_wbsd`): `corpus.load` shows 29-31 % self time. One `gc.disable()` or `gc.freeze()` around load is
  the cheapest win.
- `decode` (`analyze.py:38`) is called 1.2-1.5 million times per index build; `bare_kind` (`analyze.py:23`)
  and `_role` (`analyze.py:48`) hundreds of thousands. Caching by operand value would cut these.
- Import machinery is not significant (about 2 % of `modules`).
