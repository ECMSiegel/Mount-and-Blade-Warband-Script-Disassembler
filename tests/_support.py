"""Glue that lets the script-style tests (check() + FAILURES list) run under unittest."""


def add_tests(cls, funcs, failures, names=None):
    """Add one unittest method per function. Each fails if the function appended
    anything to `failures`. `funcs` take no arguments."""
    def make(fn):
        def test(self):
            before = len(failures)
            fn()
            self.assertEqual(failures[before:], [])
        test.__doc__ = fn.__doc__
        return test
    for fn in funcs:
        setattr(cls, fn.__name__ if fn.__name__.startswith("test") else "test_" + fn.__name__, make(fn))


def require_tables():
    """Call at import time in a test module that needs the generated tables:
    skips the whole module (instead of erroring) until build_tables has run."""
    import importlib.util
    import os
    import unittest
    here = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "wbsd")
    if not all(os.path.isfile(os.path.join(here, f)) for f in ("opref_data.py", "header_tables.py")):
        raise unittest.SkipTest("tables not built: run python3 wbsd/build_tables.py <Module System folder>")


def require_module(path):
    """Call in a test that reads a module folder. A missing folder skips the test, unless
    WB_MODULES_DIR or WB_TEST_MODULE is set: then you asked for real data, so it fails."""
    import os
    import unittest
    if not os.path.isdir(path):
        asked = [v for v in ("WB_MODULES_DIR", "WB_TEST_MODULE") if os.environ.get(v)]
        if asked:
            raise AssertionError("%s is set but there is no module data at %s" % (" and ".join(asked), path))
        raise unittest.SkipTest("no module data at %s; set WB_MODULES_DIR" % path)
