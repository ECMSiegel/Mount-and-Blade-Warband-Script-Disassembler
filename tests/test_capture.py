"""golden/capture.py: --compare rules, --only checked before writing, cwd independence, --seed.

Each test runs a copy of capture.py inside a throw-away 'repo' (tmp/repo/golden/) with its own
three-line commands.txt and a fake wbsd that prints its working directory and PYTHONHASHSEED."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "golden", "capture.py")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(text)


def read(path):
    with open(path) as f:
        return f.read()


class Capture(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.t = tmp.name
        self.repo = os.path.join(self.t, "repo")
        self.golden = os.path.join(self.repo, "golden")
        os.makedirs(self.golden)
        shutil.copy(SRC, self.golden)
        write(os.path.join(self.golden, "commands.txt"), "one\ntwo\nthree\n")
        write(os.path.join(self.t, "tool", "wbsd", "wbsd.py"),
              "import os\nprint(os.getcwd(), os.environ.get('PYTHONHASHSEED'))\n")

    def run_cap(self, args, cwd=None):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run([sys.executable, os.path.join(self.golden, "capture.py")] + args,
                              cwd=cwd or self.t, env=env, capture_output=True, text=True)

    def out(self, name, text):
        write(os.path.join(self.t, name), text)

    def test_compare_needs_out_files_on_both_sides(self):
        for d in ("a", "b"):
            os.makedirs(os.path.join(self.t, d))
        r = self.run_cap(["--compare", "a", "b"])
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("no .out files", r.stdout)
        self.out("a/99.out", "x\n")
        self.assertEqual(self.run_cap(["--compare", "a", "b"]).returncode, 1)  # b still empty
        self.assertEqual(self.run_cap(["--compare", "a", "nope"]).returncode, 1)  # b missing

    def test_only_checks_every_target_before_writing(self):
        out = os.path.join(self.t, "out")
        r = self.run_cap(["--tool-dir", "tool", "--out", "out", "--only", "1", "9999"])
        self.assertNotEqual(r.returncode, 0)
        self.assertFalse(os.path.exists(os.path.join(out, "01.out")), r.stdout)
        self.out("out/02.out", "old\n")
        r = self.run_cap(["--tool-dir", "tool", "--out", "out", "--only", "1", "2"])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("refusing to overwrite", r.stderr)
        self.assertFalse(os.path.exists(os.path.join(out, "01.out")))
        self.assertEqual(read(os.path.join(out, "02.out")), "old\n")

    def test_commands_run_from_the_repo_whatever_the_cwd(self):
        r = self.run_cap(["--tool-dir", "tool", "--out", "out", "--only", "1"])
        self.assertEqual(r.returncode, 0, r.stderr)
        got = read(os.path.join(self.t, "out", "01.out")).split()[0]
        self.assertEqual(os.path.realpath(got), os.path.realpath(self.repo))

    def test_seed_reaches_the_child(self):
        for args, want in (([], "0"), (["--seed", "7"], "7")):
            r = self.run_cap(["--tool-dir", "tool", "--out", "out" + want, "--only", "1"] + args)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(read(os.path.join(self.t, "out" + want, "01.out")).split()[1], want)

    def test_expected_overrides_only_the_golden_original(self):
        write(os.path.join(self.golden, "expected", "01.out"), "E\nexit=0\n")
        original = os.path.join(self.golden, "original")
        self.out("new/01.out", "E\nexit=0\n")
        write(os.path.join(original, "01.out"), "O\nexit=0\n")
        # matches expected, not the original -> 0, and says so
        r = self.run_cap(["--compare", original, "new"])
        self.assertEqual((r.returncode, "using expected/01.out" in r.stdout), (0, True), r.stdout)
        # matches only the original -> 1
        self.out("new/01.out", "O\nexit=0\n")
        self.assertEqual(self.run_cap(["--compare", original, "new"]).returncode, 1)
        # matches neither -> 1
        self.out("new/01.out", "Z\nexit=0\n")
        self.assertEqual(self.run_cap(["--compare", original, "new"]).returncode, 1)
        # any other side A: expected/ is not used and not announced
        self.out("other/01.out", "O\nexit=0\n")
        self.out("new/01.out", "E\nexit=0\n")
        r = self.run_cap(["--compare", "other", "new"])
        self.assertEqual((r.returncode, "using expected" in r.stdout), (1, False), r.stdout)
        self.out("new/01.out", "O\nexit=0\n")
        r = self.run_cap(["--compare", "other", "new"])
        self.assertEqual((r.returncode, "using expected" in r.stdout), (0, False), r.stdout)


if __name__ == "__main__":
    unittest.main()
