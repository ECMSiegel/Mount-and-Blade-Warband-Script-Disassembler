#!/usr/bin/env python3
"""Profile one wbsd command or one test script with cProfile (stdlib only).

  prof.py --tool-dir DIR "<wbsd args>"     e.g. "explain native game_start"
  prof.py --tool-dir DIR --test FILE       FILE is relative to DIR, e.g. test_wbasm.py

Prints the top 25 by cumulative time and the top 25 by self time, with each
function's share of the total. Saves the raw stats to --prof if given.
"""
import os, sys

import argparse, cProfile, pstats, runpy, shlex


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tool-dir", required=True)
    ap.add_argument("--test")
    ap.add_argument("--cwd", help="working directory for the run (default: --tool-dir). test_wbasm.py reads the module's .txt files from cwd, so give it the module folder")
    ap.add_argument("--prof", help="save raw .prof here")
    ap.add_argument("args", nargs="?", default="")
    a = ap.parse_args()
    d = os.path.abspath(a.tool_dir)
    sys.path.insert(0, d)
    os.chdir(os.path.abspath(a.cwd) if a.cwd else d)
    if a.test:
        target = os.path.join(d, a.test)
        argv = [target]
    else:
        target = os.path.join(d, "wbsd", "wbsd.py")
        argv = [target] + shlex.split(a.args)
    sys.argv = argv
    sys.path.insert(0, os.path.dirname(target))
    pr = cProfile.Profile()
    pr.enable()
    try:
        runpy.run_path(target, run_name="__main__")
    except SystemExit:
        pass
    finally:
        pr.disable()
        sys.stdout.flush()
    if a.prof:
        pr.dump_stats(a.prof)
    st = pstats.Stats(pr, stream=sys.stdout)
    print("\n=== PROFILE total %.2fs (profiler on) ===" % st.total_tt)
    st.strip_dirs = None  # keep full paths so file:line is unambiguous
    for key in ("cumulative", "tottime"):
        print("\n=== top 25 by %s ===" % key)
        st.sort_stats(key).print_stats(25)


if __name__ == "__main__":
    main()
