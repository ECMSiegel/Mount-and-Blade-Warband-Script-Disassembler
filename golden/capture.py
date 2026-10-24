#!/usr/bin/env python3
"""Run wbsd commands and save their output, or compare two saved output folders.

  capture.py --tool-dir DIR --out DIR     run each line of commands.txt
                                  (commands.example.txt when commands.txt is absent)
  capture.py --compare A B                exit 1 if any .out file differs; where
                                  golden/expected/NN.out exists and A is golden/original it replaces A's NN.out
  --seed N                        PYTHONHASHSEED for the runs (default 0)

--only N [N ...] re-runs just those commands. It checks every number first, and refuses
(writing nothing) if one is out of range or its NN.out already exists in --out, unless --force.
Commands run with the repo folder (wbtools/) as the working directory; --tool-dir, --out and
the --compare folders are taken relative to where you run capture.py.
--compare also exits 1 when either folder is missing or has no .out files.
"""
import argparse, os, shlex, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)  # wbtools/; commands run from here whatever the caller's cwd


def read_commands():
    cmds = os.path.join(HERE, "commands.txt")
    if not os.path.isfile(cmds):  # commands.txt is local-only; the example list ships with the repo
        cmds = os.path.join(HERE, "commands.example.txt")
    with open(cmds, encoding="utf-8") as f:
        lines = [l.strip() for l in f]
    return [l for l in lines if l and not l.startswith("#")]


def capture(tool_dir, out_dir, only=None, force=False, seed=0):
    # paths given on the command line are taken relative to where the user ran this; fix them now
    # because the commands run with the repo (the folder above golden/) as their working directory
    tool_dir, out_dir = os.path.abspath(tool_dir), os.path.abspath(out_dir)
    wbsd = os.path.join(tool_dir, "wbsd", "wbsd.py")
    commands = read_commands()
    if only:
        # check every --only target before writing anything
        bad = sorted(n for n in only if not 1 <= n <= len(commands))
        if bad:
            sys.exit("no such command number(s): %s (there are %d)" % (" ".join(map(str, bad)), len(commands)))
        clash = [os.path.join(out_dir, "%02d.out" % n) for n in sorted(only)
                 if os.path.exists(os.path.join(out_dir, "%02d.out" % n))]
        if clash and not force:
            sys.exit("refusing to overwrite %s (use --force)" % ", ".join(clash))
    os.makedirs(out_dir, exist_ok=True)
    # PYTHONHASHSEED pinned (default 0) so set-order differences cannot cause false diffs; --seed N picks another
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED=str(seed))
    for n, line in enumerate(commands, 1):
        if only and n not in only:
            continue
        target = os.path.join(out_dir, "%02d.out" % n)
        p = subprocess.run([sys.executable, wbsd] + shlex.split(line), env=env, cwd=REPO,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        with open(target, "wb") as o:
            o.write(p.stdout)
            if p.stdout and not p.stdout.endswith(b"\n"):
                o.write(b"\n")
            o.write(("exit=%d\n" % p.returncode).encode())
        print("%02d exit=%d %s" % (n, p.returncode, line), flush=True)


def compare(a, b):
    def names(d):
        try:
            return {x for x in os.listdir(d) if x.endswith(".out")}
        except OSError as e:
            print("cannot read %s: %s" % (d, e.strerror))
            return set()
    na, nb = names(a), names(b)
    bad = 0
    for d, n in ((a, na), (b, nb)):
        if not n:
            print("no .out files in %s" % d); bad = 1
    expected = os.path.join(HERE, "expected")  # golden/expected/NN.out overrides golden/original's NN.out
    use_expected = os.path.realpath(a) == os.path.realpath(os.path.join(HERE, "original"))
    for name in sorted(na | nb):
        pa, pb = os.path.join(a, name), os.path.join(b, name)
        pe = os.path.join(expected, name)
        swapped = use_expected and os.path.isfile(pe) and os.path.exists(pa)
        if swapped:
            pa = pe
        if not (os.path.exists(pa) and os.path.exists(pb)):
            print("missing:", name); bad = 1
            continue
        if swapped:
            print("using expected/%s instead of %s" % (name, a))
        with open(pa, "rb") as fa, open(pb, "rb") as fb:
            if fa.read() != fb.read():
                print("differs:", name); bad = 1
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--tool-dir"); ap.add_argument("--out")
    ap.add_argument("--compare", nargs=2, metavar=("A", "B"))
    ap.add_argument("--only", type=int, nargs="+", help="run only these command numbers")
    ap.add_argument("--seed", type=int, default=0, help="PYTHONHASHSEED for the runs (default 0)")
    ap.add_argument("--force", action="store_true", help="with --only: overwrite existing .out files")
    a = ap.parse_args()
    if a.compare:
        sys.exit(compare(*a.compare))
    if not (a.tool_dir and a.out):
        ap.error("need --tool-dir and --out, or --compare A B")
    capture(a.tool_dir, a.out, set(a.only) if a.only else None, a.force, a.seed)
