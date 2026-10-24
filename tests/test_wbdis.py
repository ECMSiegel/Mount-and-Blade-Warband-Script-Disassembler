#!/usr/bin/env python3
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import wbasm
import wbdis
from wbsd import config
import _support

MODULE = os.path.join(config.MODULES_DIR, os.environ.get("WB_TEST_MODULE", "Native"))
FAILURES = []


def check(cond, label):
    if not cond:
        FAILURES.append(label)


def test_neg_flag_rendered():
    doc = wbasm.load_scripts(os.path.join(MODULE, "scripts.txt"))
    lines = wbdis.disassemble(doc.by_name("party_remove_all_companions").statements())
    check(any("neg|31(:v3, trp0)" in l for l in lines), "neg| prefix rendered")


def check_trigger_arg_handled(value, label):
    """Call wbdis.main directly and require a clean non-zero exit for a bad
    --trigger value. Any exception is recorded as a normal FAILURES entry
    instead of tearing down the whole test run, so a regression reports
    cleanly and test order doesn't matter."""
    try:
        rc = wbdis.main(["wbdis.py", "--trigger", value])
    except Exception as e:
        FAILURES.append("%s (raised %r instead of returning non-zero)" % (label, e))
        return
    check(rc != 0, label)


def test_trigger_index_out_of_range_is_handled():
    check_trigger_arg_handled("999999", "out-of-range trigger index returns non-zero exit")


def test_trigger_index_non_numeric_is_handled():
    check_trigger_arg_handled("abc", "non-numeric trigger index returns non-zero exit")


def test_trigger_index_negative_is_handled():
    check_trigger_arg_handled("-1", "negative trigger index returns non-zero exit, not wraparound")


def test_trigger_index_multi_dash_is_handled():
    check_trigger_arg_handled("--5", "multi-dash trigger index ('--5') returns non-zero exit")
    check_trigger_arg_handled("---3", "multi-dash trigger index ('---3') returns non-zero exit")


def main():
    test_neg_flag_rendered()
    test_trigger_index_out_of_range_is_handled()
    test_trigger_index_non_numeric_is_handled()
    test_trigger_index_negative_is_handled()
    test_trigger_index_multi_dash_is_handled()
    if FAILURES:
        print("FAILED: %d" % len(FAILURES))
        for f in FAILURES:
            print("  - %s" % f)
        return 1
    print("all green")
    return 0


TESTS = [test_neg_flag_rendered,
         test_trigger_index_out_of_range_is_handled, test_trigger_index_non_numeric_is_handled,
         test_trigger_index_negative_is_handled, test_trigger_index_multi_dash_is_handled]


class WbdisTests(unittest.TestCase):
    def setUp(self):
        _support.require_module(MODULE)


_support.add_tests(WbdisTests, TESTS, FAILURES)


if __name__ == "__main__":
    sys.exit(main())
