"""build_tables: the generator parses a small SYNTHETIC header (no TaleWorlds
text), applies the author's overlay, never runs the header, and a missing
generated table gives the clean 'run build_tables first' message."""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True

from wbsd import build_tables, table_overlay  # noqa: E402

OPS = """\
# a made-up header
alpha_op      = 9001  # (alpha_op, <destination>, <thing_id>, [<extra>]),
beta_end      = 9003  # deprecated
beta_op       = 9003  # (beta_op),
gamma_op      = 9009  # (gamma_op,<position_no_1>, <position_no_2>),
neg           = 0x80000000
can_fail_operations = [alpha_op,
                       neg]
depth_operations = [beta_op]
global_lhs_operations = [gamma_op]
"""
COMMON = "tag_register = 1\ntag_variable = 2\ntag_troop = 5\n"
TRIGGERS = "ti_a_event = -5.0\nti_alias = ti_a_event\nti_b_event = -6.0 # x\nkey_q = 0x10\nkey_w = 0x11\n"


def _folder(root, evil_marker=None):
    ops_name = "header_operations_wb.py" if evil_marker else "header_operations.py"
    ops = OPS
    if evil_marker:    # real definitions PLUS code that would leave a marker if executed
        ops += "open(%r, 'w').write('executed')\nraise SystemExit('executed!')\n" % evil_marker
    for name, text in ((ops_name, ops), ("header_common.py", COMMON),
                       ("header_triggers.py", TRIGGERS)):
        with open(os.path.join(root, name), "w") as fh:
            fh.write(text)


class ParserTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        _folder(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_synthetic_header_parses(self):
        opdata, tables, summary = build_tables.build(self.tmp.name)
        ns, tb = {}, {}
        exec(opdata, ns)
        exec(tables, tb)
        lines = ns["RAW"].strip().splitlines()
        self.assertEqual(lines, ["9001 alpha_op <destination>,<thing_id>,[extra]",
                                 "9003 beta_op",
                                 "9009 gamma_op <position_no>,<position_no_2>"])
        self.assertEqual(ns["CAN_FAIL"], ["alpha_op"])    # 'neg' is a modifier, not an opcode
        self.assertEqual(ns["DEPTH"], ["beta_op"])
        self.assertEqual(ns["GLOBAL_LHS"], ["gamma_op"])
        self.assertEqual(tb["TAGS"], {1: "reg", 2: "global", 5: "troop"})
        self.assertEqual({k: v for k, v in tb["TRIGGER_EVENTS"].items() if k not in table_overlay.EVENT_FIXES},
                         {-5.0: "ti_a_event", -6.0: "ti_b_event"})
        self.assertEqual(tb["KEYS"], {0x10: "key_q", 0x11: "key_w"})

    def test_overlay_applies(self):
        old = dict(table_overlay.OP_SIGNATURES)
        table_overlay.OP_SIGNATURES[9009] = "<destination>"
        try:
            opdata, _, _ = build_tables.build(self.tmp.name)
        finally:
            table_overlay.OP_SIGNATURES.clear()
            table_overlay.OP_SIGNATURES.update(old)
        self.assertIn("9009 gamma_op <destination>\n", opdata)

    def test_headers_are_read_as_text_not_run(self):
        marker = os.path.join(self.tmp.name, "MARKER")
        _folder(self.tmp.name, evil_marker=marker)
        opdata, _, _ = build_tables.build(self.tmp.name)
        self.assertIn("9001 alpha_op <destination>,<thing_id>,[extra]", opdata)
        self.assertFalse(os.path.exists(marker), "the header was executed")

    def test_missing_headers_is_a_clean_error(self):
        with tempfile.TemporaryDirectory() as empty:
            with self.assertRaises(build_tables.TableError):
                build_tables.build(empty)
            r = subprocess.run([sys.executable, "-B", os.path.join(HERE, "wbsd", "build_tables.py"), empty],
                               capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertNotIn("Traceback", r.stderr + r.stdout)


class IoErrorTest(unittest.TestCase):
    def run_main(self, folder):
        import contextlib
        import io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = build_tables.main(["build_tables.py", folder])
        return rc, buf.getvalue()

    def test_read_error_is_clean(self):
        with tempfile.TemporaryDirectory() as t:
            _folder(t)
            os.remove(os.path.join(t, "header_common.py"))
            os.mkdir(os.path.join(t, "header_common.py"))  # reading a folder raises OSError
            rc, out = self.run_main(t)
        self.assertEqual(rc, 1)
        self.assertTrue(out.startswith("error: "), out)

    def test_write_error_is_clean_and_leaves_no_partial_files(self):
        import unittest.mock
        with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as out_dir:
            _folder(t)
            os.chmod(out_dir, 0o500)
            try:
                with unittest.mock.patch.object(build_tables, "HERE", os.path.join(out_dir, "nope")):
                    rc, out = self.run_main(t)
            finally:
                os.chmod(out_dir, 0o700)
            self.assertEqual(os.listdir(out_dir), [])
        self.assertEqual(rc, 1)
        self.assertTrue(out.startswith("error: "), out)

    def test_second_replace_failure_restores_both_files(self):
        import unittest.mock
        real = os.replace
        calls = []

        def flaky(src, dst):
            calls.append(dst)
            if len(calls) == 2:
                raise OSError("disk full")
            return real(src, dst)

        with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as out_dir:
            _folder(t)
            old = {"opref_data.py": "OLD OPDATA\n", "header_tables.py": "OLD TABLES\n"}
            for name, text in old.items():
                with open(os.path.join(out_dir, name), "w") as fh:
                    fh.write(text)
            with unittest.mock.patch.object(build_tables, "HERE", out_dir), \
                    unittest.mock.patch.object(os, "replace", flaky):
                rc, out = self.run_main(t)
            self.assertEqual(len(calls), 2)  # the first replace went through, the second failed
            for name, text in old.items():
                with open(os.path.join(out_dir, name)) as fh:
                    self.assertEqual(fh.read(), text)
            self.assertEqual(sorted(os.listdir(out_dir)), ["header_tables.py", "opref_data.py"])
        self.assertEqual(rc, 1)
        self.assertTrue(out.startswith("error: "), out)

    def test_keyboard_interrupt_cleans_up_and_propagates(self):
        import unittest.mock
        with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as out_dir:
            _folder(t)
            with unittest.mock.patch.object(build_tables, "HERE", out_dir), \
                    unittest.mock.patch.object(os, "replace", side_effect=KeyboardInterrupt):
                with self.assertRaises(KeyboardInterrupt):
                    self.run_main(t)
            self.assertEqual(os.listdir(out_dir), [])

    def test_outputs_written_through_temp_files(self):
        import unittest.mock
        with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as out_dir:
            _folder(t)
            with unittest.mock.patch.object(build_tables, "HERE", out_dir):
                rc, out = self.run_main(t)
            self.assertEqual(sorted(os.listdir(out_dir)), ["header_tables.py", "opref_data.py"])
        self.assertEqual(rc, 0, out)


class MissingTableTest(unittest.TestCase):
    def test_missing_tables_give_the_clean_message(self):
        # a copy of the package WITHOUT the generated files
        import shutil
        with tempfile.TemporaryDirectory() as t:
            pkg = os.path.join(t, "wbsd")
            shutil.copytree(os.path.join(HERE, "wbsd"), pkg,
                            ignore=shutil.ignore_patterns("__pycache__", "header_tables.py", "opref_data.py"))
            for mod in ("headers", "opref"):
                r = subprocess.run([sys.executable, "-B", "-c", "import wbsd.%s" % mod],
                                   cwd=t, capture_output=True, text=True)
                self.assertNotEqual(r.returncode, 0, mod)
                self.assertIn("run `python3 wbsd/build_tables.py --download` (or `wb-build-tables --download`) first",
                              r.stderr, mod)
                self.assertNotIn("Traceback", r.stderr, mod)

    def test_usage_without_tables(self):
        # usage text for help and unknown commands; the build_tables message only for commands that need tables
        import shutil
        with tempfile.TemporaryDirectory() as t:
            shutil.copytree(os.path.join(HERE, "wbsd"), os.path.join(t, "wbsd"),
                            ignore=shutil.ignore_patterns("__pycache__", "header_tables.py", "opref_data.py"))
            run = lambda *a: subprocess.run([sys.executable, "-B", os.path.join(t, "wbsd", "wbsd.py")] + list(a),
                                            cwd=t, capture_output=True, text=True)
            for args in ((), ("--help",), ("help",), ("nonsense",)):
                r = run(*args)
                self.assertIn("wbsd -- WB Script Disasm", r.stdout, args)
                self.assertNotIn("build_tables", r.stdout + r.stderr, args)
                self.assertNotIn("Traceback", r.stderr, args)
            r = run("modules")
            self.assertEqual(r.returncode, 1)
            self.assertIn("run `python3 wbsd/build_tables.py --download` (or `wb-build-tables --download`) first", r.stderr)
            self.assertNotIn("Traceback", r.stderr)


class DownloadTest(unittest.TestCase):
    """--download, with urllib patched: CI never touches the network."""
    FIX = os.path.join(HERE, "tests", "fixtures", "headers")

    def setUp(self):
        import io
        import urllib.error
        import urllib.request
        self._io, self._err, self._req = io, urllib.error, urllib.request
        self.out = tempfile.TemporaryDirectory()
        self._here = build_tables.HERE
        build_tables.HERE = self.out.name
        self._urlopen = urllib.request.urlopen
        self.asked = []

    def tearDown(self):
        build_tables.HERE = self._here
        self._req.urlopen = self._urlopen
        self.out.cleanup()

    def _run(self):
        import contextlib
        buf = self._io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = build_tables.main(["build_tables.py", "--download"])
        return rc, buf.getvalue()

    def test_download_builds_tables(self):
        def fake(url, timeout=None):
            self.asked.append((url, timeout))
            name = url.rsplit("/", 1)[1].replace("_wb", "")
            with open(os.path.join(self.FIX, name), "rb") as fh:
                return self._io.BytesIO(fh.read())
        self._req.urlopen = fake
        rc, out = self._run()
        self.assertEqual(rc, 0, out)
        self.assertEqual([u.rsplit("/", 1)[1] for u, _ in self.asked],
                         ["header_operations_wb.py", "header_common.py", "header_triggers_wb.py"])
        self.assertTrue(all(u.startswith("https://raw.githubusercontent.com/tldmod/tldmod/"
                                         + build_tables.HEADERS_SHA + "/") and t for u, t in self.asked))
        self.assertTrue(os.path.isfile(os.path.join(self.out.name, "opref_data.py")))
        self.assertTrue(os.path.isfile(os.path.join(self.out.name, "header_tables.py")))

    def test_network_failure_is_a_clean_error(self):
        def boom(url, timeout=None):
            raise self._err.URLError("no network")
        self._req.urlopen = boom
        rc, out = self._run()
        self.assertEqual(rc, 1)
        self.assertEqual(out.strip(), "error: could not download the Module System headers "
                         "(no network); download them yourself or pass a Module System folder")
        self.assertFalse(os.path.exists(os.path.join(self.out.name, "opref_data.py")))


@unittest.skipUnless(os.environ.get("WB_HEADERS_DIR"),
                     "set WB_HEADERS_DIR to a Module System folder to check the generator "
                     "reproduces the installed tables")
class ReproductionTest(unittest.TestCase):
    def test_generated_equals_installed(self):
        opdata, tables, _ = build_tables.build(os.environ["WB_HEADERS_DIR"])
        try:
            from wbsd import opref_data, header_tables
        except ImportError:
            self.skipTest("tables not built: run python3 wbsd/build_tables.py <Module System folder>")
        ns, tb = {}, {}
        exec(opdata, ns)
        exec(tables, tb)
        self.assertEqual(ns["RAW"], opref_data.RAW)
        for k in ("CAN_FAIL", "DEPTH", "GLOBAL_LHS"):
            self.assertEqual(ns[k], getattr(opref_data, k), k)
        for k in ("TAGS", "TRIGGER_EVENTS", "KEYS"):
            self.assertEqual(tb[k], getattr(header_tables, k), k)


if __name__ == "__main__":
    unittest.main()
