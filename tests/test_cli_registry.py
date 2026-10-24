"""wbdis.py and gen_evidence.py report a malformed modules.json as 'error: <msg>', exit 1, no traceback."""
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class BadRegistry(unittest.TestCase):
    def test_clean_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            reg = os.path.join(tmp, "bad_modules.json")
            with open(reg, "w") as f:
                f.write("{not json")
            env = dict(os.environ, WB_REGISTRY=reg, PYTHONDONTWRITEBYTECODE="1")
            for script, args in (("wbdis.py", ["x"]), ("gen_evidence.py", [])):
                self.check(script, args, env, "bad_modules.json")
            env = dict(env, WB_REGISTRY=tmp)  # a folder, not a file
            for script, args in (("wbdis.py", ["x"]), ("gen_evidence.py", [])):
                self.check(script, args, env, os.path.basename(tmp))
        r = subprocess.run([sys.executable, os.path.join(REPO, "gen_evidence.py"), "abc"],
                           env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"), capture_output=True, text=True)
        self.assertEqual((r.returncode, r.stdout.startswith("error: "), "Traceback" in r.stderr), (1, True, False), r)

    def check(self, script, args, env, name):
        r = subprocess.run([sys.executable, os.path.join(REPO, script)] + args,
                           env=env, capture_output=True, text=True)
        self.assertEqual(r.returncode, 1, (script, r.stdout, r.stderr))
        self.assertNotIn("Traceback", r.stderr, script)
        self.assertTrue(r.stdout.startswith("error: "), (script, r.stdout))
        self.assertIn(name, r.stdout, script)


if __name__ == "__main__":
    unittest.main()
