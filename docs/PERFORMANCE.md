# Performance

## Before / After (T5, paired A/B)

Method: `golden/abtime.py` runs the original (`snapshot/.../_dev/wbsd/wbsd.py`, unchanged) and the copy
(`wbsd/wbsd.py`, `WB_MODULES_DIR` = the snapshot) alternately, one untimed warm-up each, then 3 rounds,
back to back, with all caches warm. The table gives the minimum real and minimum user+sys per side.
The machine was quiet during these runs (load average about 1-3). Output of every command is
byte-identical to the original (`capture.py --compare golden/original golden/t5` exits 0, 17 commands).

| command | before real (min) | before user+sys (min) | after real (min) | after user+sys (min) | change |
|---|---|---|---|---|---|
| wbsd.py modules | 4.90 | 4.89 | 0.12 | 0.11 | -98% (stats sidecar; no module is unpickled) |
| wbsd.py explain main game_start | 2.11 | 2.10 | 0.72 | 0.71 | -66% |
| wbsd.py callers main game_start | 1.61 | 1.60 | 0.56 | 0.56 | -65% |
| wbsd.py grep change_screen_equip_other --mods native | 0.70 | 0.69 | 0.34 | 0.33 | -52% |
| wbsd.py grep change_screen_equip_other --mods native,vc,tld | 4.84 | 4.82 | 1.56 | 1.55 | -68% |
| wbsd.py grep change_screen_equip_other (all 19 modules, 2 rounds, no warm-up) | 29.66 | 29.39 | 8.91 | 8.83 | -70% |
| wbsd.py similar main game_start | 6.77 | 6.75 | 2.48 | 2.47 | -63% |
| wbsd.py similar native initialize_banner_info (new golden 17) | 8.11 | 8.08 | 3.03 | 3.01 | -63% |

Not timed against the original: `test_wbasm.py`, `test_wbdis.py`, `test_wbops.py` (code unchanged; see
"left" below) and `test_wbsd.py` (the copy's test is a different, Native-based test, so a pair would
not compare like with like; the copy's runs in about 2.8 s).

### Kept optimizations (each ablated: remove only that change, paired against the full copy)

| change | where | ablation result |
|---|---|---|
| Pause the garbage collector while unpickling a module, then `gc.freeze()` | `corpus.read_pickle` | without it: `modules` 4.88 vs 2.31 user+sys, `similar main game_start` 5.01 vs 2.49 |
| Persist the cross-reference index per module (`.cache/index/<slug>.pickle`) | `analyze.cached_index`, used by `queries.get` | without it: `explain` 1.65 vs 0.71, `callers` 1.33 vs 0.57 |
| `similar` builds the named form only for statements that could match the base script (same opcode, flags, operand count) and takes the intersection directly | `queries.similar` | without it: `similar main game_start` 2.76 vs 2.48 (-10%), `similar native initialize_banner_info` 4.84 vs 2.99 (-38%) |
| `similar`, `explain` and `grep` no longer build the cross-reference index when they only need the module (`_bare`, `registry.load`) | `queries.similar`, `native_status`, `grep` | part of the totals above |
| `disassemble` renders each distinct statement once per module (memo) | `analyze.disassemble` | part of the `grep` totals above |
| Per-module stats sidecar (`<slug>.stats.json`, scripts / blocks / statements / errors) written with the parse cache | `corpus.stats`, `corpus._write_stats` | read by `modules` (see "Left") |

New caches carry a version constant and the same fingerprint as `corpus.load` (the sha1 of the loader source,
`headers.py` and `header_tables.py`, plus each `.txt`'s size and mtime_ns). The index cache also hashes
`analyze.py`, `headers.py`, `header_tables.py`, `opref.py` and `opref_data.py`, so editing any of them rebuilds it. Disk use: `.cache/index` about 120 MB and `.cache/parsed` about 150 MB for 19 large modules.

First-run cost: the first command on a module parses it and builds its index (one cold run), then writes both
caches. For Native that is about 0.8 s (a warm run is about 0.25 s) and its `.cache` is about 7 MB (measured
on a temp cache folder, `WB_CACHE_DIR`); for the 19 large modules a cold run is tens of seconds.

### Fail-first for the new caches

Temp copy of Native under `<scratch>/ff/Modules`, its own `modules.json` via `WB_REGISTRY`, slug `fftest`
(so the real caches are not touched). `wbsd.py explain fftest game_start`:

| step | parse cache | index cache | stats sidecar |
|---|---|---|---|
| run 1 (cold) | written 04:21:37 | written 04:21:37 | written 04:21:37 |
| run 2 (warm) | unchanged | unchanged | unchanged |
| `touch scripts.txt`, run 3 | rewritten 04:21:42 | rewritten 04:21:42 | rewritten 04:21:42 |

`corpus.stats()` also returned the cached numbers on a hit and rewrote its sidecar after the touch.

### Tried, rejected

None rejected; every change above passed the 10 % rule on user+sys without a worse real time.

### Left

- `test_wbasm.py` hot spots (`wbasm._split_line`, `parse_statements`): the byte-exact round-trip code, left alone on purpose.
- `callers` (1.6 s before) and `grep --mods native` (0.7 s) were already under the 2 s stop line; they were
  sped up anyway as a side effect of the shared changes.
- `similar` still spends its time unpickling 19 modules and in `difflib.SequenceMatcher.ratio()` (shape match);
  the latter must keep exact results, so it is untouched.
- `modules` now reads the stats sidecar (`registry.stats`); fail-first for that path: temp Native copy, `wbsd.py modules` rewrote the sidecar only after `touch scripts.txt` (warm run left it unchanged).
