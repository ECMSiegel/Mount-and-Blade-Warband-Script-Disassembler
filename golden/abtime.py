#!/usr/bin/env python3
"""Paired A/B timing of the original wbsd against the copy (stdlib only).

  abtime.py --orig .../wbsd.py --copy .../wbsd.py --modules-dir SNAP [--rounds 3] "cmd args" ...

For each command: one untimed warm-up run per side, then ROUNDS rounds, each
round running the original then the copy back to back. Reports the minimum
real and minimum user+sys per side (the machine is shared, so single timings
mean nothing) and the change in each, as a markdown table row.
"""
import argparse, os, resource, shlex, subprocess, sys, time


def run(script, args, env):
    r0 = resource.getrusage(resource.RUSAGE_CHILDREN)
    t0 = time.time()
    p = subprocess.run([sys.executable, script] + args, env=env,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    real = time.time() - t0
    r1 = resource.getrusage(resource.RUSAGE_CHILDREN)
    return real, (r1.ru_utime - r0.ru_utime) + (r1.ru_stime - r0.ru_stime), p.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--orig", required=True)
    ap.add_argument("--copy", required=True)
    ap.add_argument("--modules-dir", required=True, help="WB_MODULES_DIR for the copy")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--no-warmup", action="store_true")
    ap.add_argument("cmds", nargs="+")
    a = ap.parse_args()
    base = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0")
    env_o = dict(base)
    env_c = dict(base, WB_MODULES_DIR=a.modules_dir)
    print("| command | before real (min) | before user+sys (min) | after real (min) | after user+sys (min) | change (real / user+sys) |")
    print("|---|---|---|---|---|---|", flush=True)
    for c in a.cmds:
        args = shlex.split(c)
        if not a.no_warmup:
            run(a.orig, args, env_o); run(a.copy, args, env_c)
        o, k = [], []
        for _ in range(a.rounds):
            o.append(run(a.orig, args, env_o))
            k.append(run(a.copy, args, env_c))
        orr, ocpu = min(x[0] for x in o), min(x[1] for x in o)
        krr, kcpu = min(x[0] for x in k), min(x[1] for x in k)
        print("| %s | %.2f | %.2f | %.2f | %.2f | %+.0f%% / %+.0f%% |" % (
            c, orr, ocpu, krr, kcpu, 100 * (krr - orr) / orr, 100 * (kcpu - ocpu) / ocpu), flush=True)
        print("<!-- rounds orig real/cpu: %s | copy: %s ; exits %s/%s -->" % (
            " ".join("%.2f/%.2f" % x[:2] for x in o), " ".join("%.2f/%.2f" % x[:2] for x in k),
            {x[2] for x in o}, {x[2] for x in k}), flush=True)


main()
