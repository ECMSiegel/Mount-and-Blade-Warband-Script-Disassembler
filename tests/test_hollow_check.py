"""Tests for tools/hollow_check.py: it must flag tests that can never fail and leave real ones alone."""
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOL = os.path.join(REPO, "tools", "hollow_check.py")
_spec = importlib.util.spec_from_file_location("hollow_check", TOOL)
hollow_check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hollow_check)

SAMPLE = '''
import unittest

FAILURES = []

def check(cond, label):
    if not cond:
        FAILURES.append(label)

class Sample(unittest.TestCase):
    def test_hollow_no_assert(self):
        x = 1 + 1
        print(x)

    def test_hollow_assert_true(self):
        assert True

    def test_hollow_assert_true_call(self):
        self.assertTrue(True)

    def test_hollow_same_both_sides(self):
        value = [1]
        self.assertEqual(value, value)

    def test_hollow_only_skips(self):
        self.skipTest("later")

    def test_hollow_pass(self):
        pass

    def test_real_assert(self):
        self.assertEqual(1 + 1, 2)

    def test_real_assert_statement(self):
        assert len("ab") == 2

    def test_real_raises_context(self):
        with self.assertRaises(ValueError):
            int("x")

    def test_real_fail(self):
        if len("a") > 5:
            self.fail("never")

    def test_real_check_function(self):
        check(1 == 1, "label")

    def test_real_raise(self):
        if not FAILURES:
            raise RuntimeError("boom")

    def test_real_failures_list(self):
        FAILURES.append("x")

    def test_real_wrapper_requires_empty_failures(self):
        self.assertEqual(FAILURES, [])

    def test_real_via_helper(self):
        self.helper_that_asserts()

    def helper_that_asserts(self):
        self.assertEqual("a", "a".lower())

    def test_hollow_via_helper_that_does_not_assert(self):
        self.helper_quiet()

    def helper_quiet(self):
        return 1

def test_hollow_module_level():
    return None

def test_real_module_level():
    assert sorted([2, 1]) == [1, 2]
'''
HOLLOW = {"Sample.test_hollow_no_assert", "Sample.test_hollow_assert_true", "Sample.test_hollow_assert_true_call",
          "Sample.test_hollow_same_both_sides", "Sample.test_hollow_only_skips", "Sample.test_hollow_pass",
          "Sample.test_hollow_via_helper_that_does_not_assert", "test_hollow_module_level"}


class HollowAnalysis(unittest.TestCase):
    def test_flags_exactly_the_hollow_tests(self):
        found, total = hollow_check.analyse(SAMPLE)
        self.assertEqual({q for _line, q, _why in found}, HOLLOW)
        self.assertEqual(total, 18)

    def test_line_numbers_point_at_the_def(self):
        found, _ = hollow_check.analyse(SAMPLE)
        lines = SAMPLE.splitlines()
        for line, q, _why in found:
            self.assertIn("def " + q.rsplit(".", 1)[-1], lines[line - 1])


def flagged(src, filename="<src>"):
    """{test name: reason} for the problem tests in `src`."""
    return {q: why for _line, q, why in hollow_check.analyse(src, filename)[0]}


class HollowRules(unittest.TestCase):
    def test_failures_append_needs_an_assert_on_the_list_or_support(self):
        body = "FAILURES = []\n\ndef test_x():\n    FAILURES.append('x')\n"
        self.assertIn("test_x", flagged(body))                                   # nobody ever checks the list
        self.assertEqual(flagged(body + "\ndef test_all():\n    assert FAILURES == []\n"), {})
        self.assertEqual(flagged("import _support\n" + body), {})
        self.assertEqual(flagged(body + "\nclass T:\n    def test_all(self):\n"
                                 "        self.assertEqual(FAILURES, [])\n"), {})

    def test_assertion_under_a_constant_false_condition_never_runs(self):
        for cond in ("False", "0"):
            why = flagged("def test_a():\n    if %s:\n        assert 1 + 1 == 3\n" % cond)
            self.assertIn("can never run", why["test_a"], cond)
        self.assertIn("can never run", flagged(
            "def test_b():\n    if True:\n        pass\n    else:\n        assert 1 + 1 == 3\n")["test_b"])
        self.assertEqual(flagged("def test_c():\n    if True:\n        assert len('a') == 1\n"), {})

    def test_assertion_after_return_never_runs(self):
        why = flagged("def test_a():\n    x = 1\n    return\n    assert x == 2\n")
        self.assertIn("can never run", why["test_a"])
        self.assertEqual(flagged("def test_b():\n    assert len('a') == 1\n    return\n"), {})
        self.assertIn("can never run", flagged(
            "def test_c():\n    for i in range(2):\n        continue\n        assert i == 5\n")["test_c"])

    def test_assertion_in_a_nested_def_needs_a_call(self):
        never = "def test_a():\n    def inner():\n        assert len('a') == 2\n    return None\n"
        self.assertIn("can never run", flagged(never)["test_a"])
        called = "def test_b():\n    def inner():\n        assert len('a') == 2\n    inner()\n"
        self.assertEqual(flagged(called), {})

    def test_tuple_assert_is_flagged_even_next_to_a_real_one(self):
        why = flagged("def test_a():\n    assert len('a') == 1\n    assert (len('a') == 2, 'message')\n")
        self.assertIn("tuple", why["test_a"])
        self.assertEqual(flagged("def test_b():\n    assert len('a') == 1, 'message'\n"), {})

    def test_check_style_names_need_a_source(self):
        # called but defined nowhere in the file or imports: not trusted
        self.assertIn("test_a", flagged("def test_a():\n    check_thing(1)\n    expect_x(2)\n"))
        # defined in the file with an assert inside
        self.assertEqual(flagged("def check_thing(x):\n    assert x\n\ndef test_a():\n    check_thing(1)\n"), {})
        # defined in the file but it cannot fail
        self.assertIn("test_a", flagged("def check_thing(x):\n    return x\n\ndef test_a():\n    check_thing(1)\n"))
        # imported from _support
        self.assertEqual(flagged("from _support import verify_it\n\ndef test_a():\n    verify_it(1)\n"), {})
        # a raise inside the helper counts
        self.assertEqual(flagged("def ensure_ok(x):\n    raise ValueError(x)\n\ndef test_a():\n    ensure_ok(1)\n"), {})

    def test_helper_imported_from_a_sibling_test_module(self):
        d = tempfile.mkdtemp(prefix="wbtools-hollow-sib-")
        self.addCleanup(shutil.rmtree, d, True)
        with open(os.path.join(d, "test_base.py"), "w") as fh:
            fh.write("import _support\nFAILURES = []\n\ndef check(c, label):\n    if not c:\n        FAILURES.append(label)\n\n"
                     "def noop(x):\n    return x\n")
        user = os.path.join(d, "test_user.py")
        src = "from test_base import check, noop\n\ndef test_a():\n    check(1 == 1, 'ok')\n\ndef test_b():\n    noop(1)\n"
        with open(user, "w") as fh:
            fh.write(src)
        self.assertEqual(set(flagged(src, user)), {"test_b"})


class HollowCli(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="wbtools-hollow-")
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def write(self, name, text):
        p = os.path.join(self.tmp, name)
        with open(p, "w") as fh:
            fh.write(text)
        return p

    def run_tool(self, *paths):
        r = subprocess.run([sys.executable, TOOL] + list(paths), capture_output=True, text=True,
                           env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
        self.assertNotIn("Traceback", r.stderr)
        return r.returncode, r.stdout

    def test_hollow_sample_exits_1_and_lists_it(self):
        p = self.write("test_sample.py", SAMPLE)
        rc, out = self.run_tool(p)
        self.assertEqual(rc, 1, out)
        self.assertIn("Sample.test_hollow_no_assert has no assert, check, fail or raise path", out)
        self.assertNotIn("test_real_assert", out)
        self.assertIn("8 hollow", out)

    def test_clean_file_exits_0(self):
        p = self.write("test_ok.py", "def test_a():\n    assert 1 + 1 == 2\n")
        rc, out = self.run_tool(p)
        self.assertEqual(rc, 0, out)
        self.assertIn("1 tests in 1 files, 0 hollow", out)

    def test_folder_is_searched_for_test_files_only(self):
        self.write("test_bad.py", "def test_a():\n    pass\n")
        self.write("helper.py", "def test_not_scanned():\n    pass\n")
        rc, out = self.run_tool(self.tmp)
        self.assertEqual(rc, 1, out)
        self.assertIn("test_bad.py", out)
        self.assertNotIn("helper.py", out)

    def test_bad_path_and_syntax_error_exit_2(self):
        rc, out = self.run_tool(os.path.join(self.tmp, "missing"))
        self.assertEqual(rc, 2, out)
        rc, out = self.run_tool(self.write("test_broken.py", "def test_a(:\n"))
        self.assertEqual(rc, 2, out)

    def test_the_repos_own_tests_are_not_hollow(self):
        rc, out = self.run_tool(os.path.join(REPO, "tests"))
        self.assertEqual(rc, 0, out)

    def test_hollowing_a_real_test_file_is_caught(self):
        """Doctored copy: turn every assertion call in a real test file into print(); the tool must object."""
        with open(os.path.join(REPO, "tests", "test_config.py"), encoding="utf-8") as fh:
            src = fh.read()
        self.assertRegex(src, r"self\.assert\w+\(")
        doctored = self.write("test_config_doctored.py", re.sub(r"self\.assert\w+\(", "print(", src))
        rc, out = self.run_tool(doctored)
        self.assertEqual(rc, 1, out)
        rc, out = self.run_tool(self.write("test_config_original.py", src))
        self.assertEqual(rc, 0, out)


if __name__ == "__main__":
    unittest.main()
