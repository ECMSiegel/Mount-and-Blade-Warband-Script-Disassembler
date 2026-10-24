import importlib
import os
import unittest
from unittest import mock

from wbsd import config

TAIL = ("steamapps", "common", "MountBlade Warband", "Modules")


class ConfigTests(unittest.TestCase):
    def tearDown(self):
        importlib.reload(config)

    def test_candidate_order(self):
        env = {"ProgramFiles(x86)": "/pf86", "ProgramFiles": "/pf"}
        with mock.patch.dict(os.environ, env):
            dirs = config.default_modules_dirs()
        self.assertEqual(dirs, [
            os.path.expanduser(os.path.join("~/Library/Application Support/Steam", *TAIL)),
            os.path.join("/pf86", "Steam", *TAIL),
            os.path.join("/pf", "Steam", *TAIL),
            os.path.expanduser(os.path.join("~/.steam/steam", *TAIL)),
            os.path.expanduser(os.path.join("~/.local/share/Steam", *TAIL)),
        ])

    def test_windows_vars_skipped_when_unset(self):
        with mock.patch.dict(os.environ, clear=False):
            os.environ.pop("ProgramFiles(x86)", None)
            os.environ.pop("ProgramFiles", None)
            self.assertEqual(len(config.default_modules_dirs()), 3)

    def _reload(self, env, isdir):
        with mock.patch.dict(os.environ, env), mock.patch("os.path.isdir", isdir):
            if "WB_MODULES_DIR" not in env:
                os.environ.pop("WB_MODULES_DIR", None)
            importlib.reload(config)
            return config.MODULES_DIR

    def test_override_wins(self):
        self.assertEqual(self._reload({"WB_MODULES_DIR": "/custom"}, lambda p: True), "/custom")

    def test_first_existing_directory(self):
        want = config.default_modules_dirs()[-2]
        got = self._reload({}, lambda p: p == want)
        self.assertEqual(got, want)

    def test_fallback_to_first_candidate(self):
        first = config.default_modules_dirs()[0]
        self.assertEqual(self._reload({}, lambda p: False), first)


class RequireModuleTests(unittest.TestCase):
    def test_missing_folder_skips_when_no_env_is_set(self):
        import sys
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import _support
        with mock.patch.dict(os.environ):
            os.environ.pop("WB_MODULES_DIR", None)
            os.environ.pop("WB_TEST_MODULE", None)
            with self.assertRaises(unittest.SkipTest):
                _support.require_module("/no/such/folder")

    def test_missing_folder_fails_when_env_is_set(self):
        import sys
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import _support
        for var in ("WB_MODULES_DIR", "WB_TEST_MODULE"):
            with mock.patch.dict(os.environ, {var: "x"}):
                with self.assertRaises(AssertionError) as cm:
                    _support.require_module("/no/such/folder")
                self.assertIn(var, str(cm.exception))


if __name__ == "__main__":
    unittest.main()
