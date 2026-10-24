# Golden harness (developer tools)

These scripts check that a changed copy of wbsd still prints exactly what a reference copy prints.
You need a reference copy of the tool (an untouched checkout to compare against).

Capture and compare (run from the `wbtools` folder, with `WB_MODULES_DIR` pointing at the same
module data for both runs):

    python3 golden/capture.py --tool-dir <reference tool dir> --out golden/ref
    python3 golden/capture.py --tool-dir .                     --out golden/new
    python3 golden/capture.py --compare golden/ref golden/new      # exit 0 = every .out identical

`capture.py` runs each line of `golden/commands.txt` (your own local list, git-ignored) or, if that
file is missing, `golden/commands.example.txt` (Native-only commands). Output goes to `NN.out` files.
The output folders and `.out` files are git-ignored.

- `--seed N` sets `PYTHONHASHSEED` for the runs (default 0). Output should be the same for every seed.
- `golden/expected/NN.out` (optional, git-ignored like the other output) replaces `NN.out` of the
  folder `golden/original` in `--compare`, only when side A is that folder; the compare output
  names each file taken from there. Use it where the original's output is known to be wrong or
  unstable, for example output that depends on set order. Keep a note beside it saying why.
- `--only N [N ...]` re-runs just those commands. Every number is checked first; if one is out of
  range, or its `NN.out` already exists in `--out` (without `--force`), nothing is written.
- Commands run with `wbtools/` as their working directory, wherever you start `capture.py` from;
  `--tool-dir`, `--out` and the `--compare` folders are taken relative to where you start it.
- `--compare` exits 1 when either folder is missing or has no `.out` files.
- `abtime.py` times the reference tool against this one, alternating runs; it needs `--orig` (the
  reference `wbsd.py`) and `--copy` (this repo's `wbsd/wbsd.py`).
- `prof.py` profiles one command with cProfile; it only needs `--tool-dir`.
