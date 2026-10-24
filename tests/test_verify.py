"""Tests for `wbsd verify-port` and `wbsd check-log`.

They need no Warband data and no generated tables: the demo module in tests/fixtures/minimod is
copied into temp folders and doctored there, and the wbsd command line runs in a subprocess
against a TEMP copy of the toolkit whose tables were built from the invented fixture headers.
The repo's own tables and .cache are never touched.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from wbsd import verify  # noqa: E402  (importing it needs no tables)

FIXTURES = os.path.join(REPO, "tests", "fixtures")
MINIMOD = os.path.join(FIXTURES, "minimod")
HEADERS = os.path.join(FIXTURES, "headers")
SCRIPT_TAG = 13 << 56          # operand tag of "script id"


def call(idx):
    """One call_script statement as scripts.txt tokens."""
    return "1 1 %d" % (SCRIPT_TAG + idx)


def append_scripts(path, new):
    """Append (name, [statement token strings]) scripts to a scripts.txt (CRLF, one body line each)."""
    with open(path, "rb") as fh:
        lines = fh.read().decode("ascii").split("\r\n")
    lines[1] = str(int(lines[1]) + len(new))
    tail = lines[-1] == ""
    body = lines[:-1] if tail else lines
    for name, stmts in new:
        body.append("%s -1" % name)
        body.append(" %d %s" % (len(stmts), " ".join(stmts)))
    with open(path, "wb") as fh:
        fh.write(("\r\n".join(body) + "\r\n").encode("ascii"))


def append_simple_trigger(path, stmt):
    with open(path, "rb") as fh:
        lines = fh.read().decode("ascii").split("\n")
    lines[1] = str(int(lines[1]) + 1)
    lines.insert(len(lines) - 1, "1.000000  1 %s" % stmt)
    with open(path, "wb") as fh:
        fh.write("\n".join(lines).encode("ascii"))


def write_text(path, text):
    with open(path, "wb") as fh:
        fh.write(text.encode("ascii"))


def read_text(path):
    with open(path, "rb") as fh:
        return fh.read().decode("ascii")


class VerifyPortCli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="wbtools-verify-")
        cls.addClassCleanup(shutil.rmtree, cls.tmp, True)
        cls.tool = os.path.join(cls.tmp, "tool")
        os.makedirs(cls.tool)
        shutil.copytree(os.path.join(REPO, "wbsd"), os.path.join(cls.tool, "wbsd"), ignore=shutil.ignore_patterns(
            "__pycache__", "opref_data.py", "header_tables.py", "*.tmp"))
        for name in os.listdir(REPO):
            if name.endswith(".py"):
                shutil.copy(os.path.join(REPO, name), cls.tool)
        cls.run_env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", WB_MODULES_DIR=os.path.join(cls.tmp, "none"),
                       WB_CACHE_DIR=os.path.join(cls.tmp, "cache"))
        cls.wbsd = os.path.join(cls.tool, "wbsd", "wbsd.py")
        r = subprocess.run([sys.executable, os.path.join(cls.tool, "wbsd", "build_tables.py"), HEADERS],
                           env=cls.run_env, capture_output=True, text=True)
        assert r.returncode == 0, (r.stdout, r.stderr)
        cls.base = cls.copy_module("base")

    @classmethod
    def copy_module(cls, name):
        dest = os.path.join(cls.tmp, name)
        shutil.copytree(MINIMOD, dest)
        return dest

    def run_cmd(self, *args):
        r = subprocess.run([sys.executable, self.wbsd] + list(args), env=self.run_env, capture_output=True, text=True)
        self.assertNotIn("Traceback", r.stderr)
        return r.returncode, r.stdout

    def good_target(self, name):
        """BASE plus a new simple trigger that calls new script A, which calls new script B."""
        t = self.copy_module(name)
        append_scripts(os.path.join(t, "scripts.txt"), [
            ("demo_new_a", [call(5)]),                       # script 4, calls script 5
            ("demo_new_b", ["2133 2 144115188075855872 7"]),    # script 5 (assign $demo_counter, 7)
        ])
        append_simple_trigger(os.path.join(t, "simple_triggers.txt"), call(4))
        return t

    def line_for(self, out, check):
        return next(l for l in out.splitlines() if l[5:].startswith(check))

    # ---- the passing port
    def test_good_port_passes_every_check(self):
        t = self.good_target("good")
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 0, out)
        for check in ("append-only", "untouched", "reachable", "opcodes"):
            self.assertTrue(self.line_for(out, check).startswith("PASS"), out)
        self.assertIn("2 new scripts appended", out)
        self.assertIn("3 new or changed blocks scanned", out)     # 2 scripts + the new simple trigger, nothing else
        self.assertIn("script_demo_new_a <- strig:2", out)
        self.assertIn("script_demo_new_b <- strig:2", out)       # reached through A
        self.assertIn("limitation: a call_script that takes its script id from a variable", out)
        self.assertTrue(out.rstrip().endswith("verify-port OK"))

    def test_identical_folders_pass(self):
        rc, out = self.run_cmd("verify-port", self.base, self.copy_module("same"))
        self.assertEqual(rc, 0, out)
        self.assertIn("0 new scripts appended", out)

    # ---- append-only
    def test_edited_base_script_fails_append_only(self):
        t = self.good_target("edited")
        path = os.path.join(t, "scripts.txt")
        with open(path, "rb") as fh:
            text = fh.read().decode("ascii")
        self.assertIn("500 3 360287970189639680 3 1 3 0", text)
        with open(path, "wb") as fh:
            fh.write(text.replace("500 3 360287970189639680 3 1 3 0", "500 3 360287970189639680 3 2 3 0").encode("ascii"))
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertTrue(self.line_for(out, "append-only").startswith("FAIL"), out)
        self.assertIn("script #1 demo_script_bump: body differs from BASE", out)
        self.assertTrue(self.line_for(out, "reachable").startswith("PASS"), out)
        # the same edit is accepted when it is declared
        rc, out = self.run_cmd("verify-port", self.base, t, "--allow-edit", "script_demo_script_bump")
        self.assertEqual(rc, 0, out)
        self.assertIn("edited as allowed by --allow-edit: demo_script_bump", out)

    def test_allow_edit_of_unknown_script_warns(self):
        rc, out = self.run_cmd("verify-port", self.base, self.good_target("allow-typo"), "--allow-edit", "demo_typo")
        self.assertEqual(rc, 0, out)         # a warning, not a failure
        self.assertIn("WARN --allow-edit names demo_typo, which is not a script in BASE", out)

    def test_script_inserted_before_existing_ones_fails(self):
        t = self.copy_module("inserted")
        path = os.path.join(t, "scripts.txt")
        with open(path, "rb") as fh:
            lines = fh.read().decode("ascii").split("\r\n")
        lines[1] = "5"
        lines[2:2] = ["demo_first -1", " 1 2133 2 144115188075855872 1"]
        with open(path, "wb") as fh:
            fh.write("\r\n".join(lines).encode("ascii"))
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("script #0: BASE has demo_script_init, TARGET has demo_first (an id moved or was renamed)", out)
        self.assertIn("... and 3 more differing positions in script", out)       # first mismatch, then a count

    def test_removed_record_fails_append_only(self):
        t = self.copy_module("shrunk")
        path = os.path.join(t, "simple_triggers.txt")
        with open(path, "wb") as fh:
            fh.write(b"simple_triggers_file version 1\n1\n1.000000  1 1 1 936748722493063168\n")
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("strig blocks: TARGET has 1, BASE has 2", out)

    def test_unparseable_target_table_fails(self):
        t = self.copy_module("garbled")
        with open(os.path.join(t, "scripts.txt"), "wb") as fh:
            fh.write(b"scriptsfile version 1\r\n4\r\ndemo_script_init -1\r\n 9 1\r\n")
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("TARGET table scripts.txt did not parse", out)

    # ---- untouched files
    def test_reformatted_untouched_table_fails(self):
        """Same content, different line endings: a pointless rewrite of a table the port did not change."""
        t = self.good_target("churn")
        with open(os.path.join(t, "simple_triggers.txt"), "wb") as fh:
            fh.write(b"simple_triggers_file version 1\r\n2\r\n1.000000  1 1 1 936748722493063168\r\n"
                     b"24.000000  1 1 1 936748722493063170\r\n")
        t_ok = self.copy_module("churn-ok")
        rc, out = self.run_cmd("verify-port", self.base, t_ok)       # control: untouched copy passes
        self.assertEqual(rc, 0, out)
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertTrue(self.line_for(out, "untouched").startswith("FAIL"), out)
        self.assertIn("simple_triggers.txt differs byte-for-byte but every token is the same", out)

    def test_deleted_file_fails(self):
        t = self.copy_module("lost-file")
        os.remove(os.path.join(t, "variables.txt"))
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("variables.txt exists in BASE but not in TARGET", out)

    def test_file_a_port_may_not_write_fails_unless_touched(self):
        t = self.good_target("strings-edit")
        write_text(os.path.join(t, "strings.txt"), "stringsfile version 1\n2\nstr_demo_empty _\nstr_demo_hello Changed.\n")
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("strings.txt changed but is not a file a port may write", out)
        rc, out = self.run_cmd("verify-port", self.base, t, "--touched", "strings.txt")
        self.assertEqual(rc, 0, out)
        self.assertIn("INFO", out)

    def test_port_tables_may_change_and_leftovers_are_info(self):
        t = self.good_target("leftovers")
        write_text(os.path.join(t, "scripts.txt.bak_before_demo"), "backup")
        write_text(os.path.join(t, "ports.log.jsonl"), "{}\n")
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 0, out)
        self.assertIn("INFO 2 files changed, as a port may: scripts.txt, simple_triggers.txt", out)
        self.assertIn("INFO 2 wbport leftovers", out)

    def test_menus_file_with_an_extra_newline_fails(self):
        menus = "menusfile version 1\n1\nmenu_demo 0 Demo none 0 1 mno_go 0 Go 0 none\n"
        base = self.copy_module("menu-base")
        write_text(os.path.join(base, "menus.txt"), menus)
        t = self.copy_module("menu-newline")
        write_text(os.path.join(t, "menus.txt"), menus + "\n")
        rc, out = self.run_cmd("verify-port", base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("menus.txt differs byte-for-byte but every token is the same", out)
        t2 = self.copy_module("menu-same")
        write_text(os.path.join(t2, "menus.txt"), menus)
        rc, out = self.run_cmd("verify-port", base, t2)
        self.assertEqual(rc, 0, out)

    def test_repeated_block_ids_are_matched_by_occurrence(self):
        """Two options with the same id and different bodies: an appended menu is the only new block."""
        base = self.copy_module("dup-base")
        two = ("menu_demo 0 Demo none 0 2 mno_go 0 Go 1 1 1 %d none mno_go 0 Go2 0 none\n" % (SCRIPT_TAG + 0))
        write_text(os.path.join(base, "menus.txt"), "menusfile version 1\n1\n" + two)
        t = self.copy_module("dup-target")
        write_text(os.path.join(t, "menus.txt"), "menusfile version 1\n2\n" + two + "menu_demo2 0 Demo2 none 0 0\n")
        rc, out = self.run_cmd("verify-port", base, t)
        self.assertEqual(rc, 0, out)
        self.assertIn("1 new or changed blocks scanned", out)

    # ---- order of dialogs and triggers
    def test_inserted_simple_trigger_fails_but_appended_one_passes(self):
        t = self.copy_module("strig-insert")
        write_text(os.path.join(t, "simple_triggers.txt"),
                   "simple_triggers_file version 1\n3\n5.000000  1 1 1 936748722493063168\n"
                   "1.000000  1 1 1 936748722493063168\n24.000000  1 1 1 936748722493063170\n")
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("strig order/content: BASE has strig:0, TARGET has strig:0 at the same position", out)
        self.assertIn("... and 1 more differing strig blocks", out)
        rc, out = self.run_cmd("verify-port", self.base, self.good_target("strig-append"))
        self.assertEqual(rc, 0, out)

    def test_inserted_dialog_fails_but_appended_one_passes(self):
        d1 = "dlga_a 1 2 0 Hi 3 0 NO_VOICE\n"
        d2 = "dlga_b 1 2 0 Bye 3 0 NO_VOICE\n"
        d3 = "dlga_c 1 2 0 Yo 3 0 NO_VOICE\n"
        head = lambda n: "dialogsfile version 2\n%d\n" % n
        base = self.copy_module("dlg-base")
        write_text(os.path.join(base, "conversation.txt"), head(2) + d1 + d2)
        for name, text, want in (("dlg-append", head(3) + d1 + d2 + d3, 0), ("dlg-insert", head(3) + d1 + d3 + d2, 1),
                                 ("dlg-swap", head(2) + d2 + d1, 1)):
            t = self.copy_module(name)
            write_text(os.path.join(t, "conversation.txt"), text)
            rc, out = self.run_cmd("verify-port", base, t)
            self.assertEqual(rc, want, (name, out))
            if want:
                self.assertIn("dlg order/content: BASE has dlg:1:dlga_b:cond" if name == "dlg-insert"
                              else "dlg order/content: BASE has dlg:0:dlga_a:cond", out)

    # ---- reachability
    def test_unreachable_new_script_fails(self):
        t = self.good_target("orphan")
        append_scripts(os.path.join(t, "scripts.txt"), [("demo_new_orphan", ["2133 2 144115188075855872 3"])])
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertTrue(self.line_for(out, "reachable").startswith("FAIL"), out)
        self.assertIn("script_demo_new_orphan has no path from any trigger", out)
        self.assertNotIn("script_demo_new_a has no path", out)
        self.assertTrue(self.line_for(out, "append-only").startswith("PASS"), out)

    def test_script_called_only_by_unreachable_script_fails(self):
        t = self.copy_module("dead-chain")
        append_scripts(os.path.join(t, "scripts.txt"), [
            ("demo_dead_top", [call(5)]),                   # script 4 calls 5, nobody calls 4
            ("demo_dead_leaf", ["2133 2 144115188075855872 3"]),
        ])
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("script_demo_dead_top has no path", out)
        self.assertIn("script_demo_dead_leaf has no path", out)

    def test_expect_adds_existing_scripts_to_the_check(self):
        t = self.good_target("expect")
        rc, out = self.run_cmd("verify-port", self.base, t, "--expect", "demo_script_bump")
        self.assertEqual(rc, 0, out)
        self.assertIn("3 scripts checked (2 new, 1 added by --expect)", out)
        rc, out = self.run_cmd("verify-port", self.base, t, "--expect", "script_demo_script_unused")
        self.assertEqual(rc, 1, out)
        self.assertIn("script_demo_script_unused has no path", out)
        rc, out = self.run_cmd("verify-port", self.base, t, "--expect", "demo_nonexistent")
        self.assertEqual(rc, 1, out)
        self.assertIn("--expect names demo_nonexistent, which is not a script in TARGET", out)

    def test_new_game_script_is_not_trusted_by_its_name(self):
        t = self.good_target("new-hook")
        append_scripts(os.path.join(t, "scripts.txt"), [("game_demo_hook", ["2133 2 144115188075855872 1"])])
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        msg = "new game_* script is not an engine hook; engine hooks must already exist in BASE"
        self.assertIn(msg, out)
        for flag in ("--expect", "--assume-reached"):        # neither flag can bless a new hook
            rc, out = self.run_cmd("verify-port", self.base, t, flag, "game_demo_hook")
            self.assertEqual(rc, 1, out)
            self.assertIn(msg, out)
            self.assertNotIn("WAIVED", out)

    def test_script_called_only_from_a_new_game_script_fails(self):
        t = self.copy_module("new-hook-chain")
        append_scripts(os.path.join(t, "scripts.txt"), [
            ("game_demo_hook", [call(5)]),
            ("demo_behind_hook", ["2133 2 144115188075855872 1"])])
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("script_demo_behind_hook has no path", out)
        self.assertIn("only reached from the new game_* script game_demo_hook", out)

    def test_game_script_that_exists_in_base_is_an_engine_hook(self):
        base = self.copy_module("hook-base")
        append_scripts(os.path.join(base, "scripts.txt"), [("game_demo_hook", ["2133 2 144115188075855872 1"])])
        t = self.copy_module("hook-target")
        append_scripts(os.path.join(t, "scripts.txt"), [("game_demo_hook", [call(5)]),
                                                         ("demo_hooked", ["2133 2 144115188075855872 2"])])
        rc, out = self.run_cmd("verify-port", base, t, "--allow-edit", "game_demo_hook")
        self.assertEqual(rc, 0, out)
        self.assertIn("script_demo_hooked <- script:game_demo_hook", out)

    def test_computed_call_is_reported_as_a_limit(self):
        t = self.copy_module("computed")
        # call_script with the script id taken from local variable :l0 (tag 17): cannot be traced
        append_scripts(os.path.join(t, "scripts.txt"), [
            ("demo_dyn_caller", ["1 1 %d" % ((17 << 56) + 0)]),
            ("demo_dyn_target", ["2133 2 144115188075855872 3"]),
        ])
        append_simple_trigger(os.path.join(t, "simple_triggers.txt"), call(4))
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertIn("script_demo_dyn_target has no path", out)
        self.assertIn("it may be called through one of the 1 computed call_script sites", out)
        self.assertIn("(1 such call sites in new or changed blocks)", out)
        # an explicit waiver is the only way past it, and it is printed
        rc, out = self.run_cmd("verify-port", self.base, t, "--assume-reached", "script_demo_dyn_target,demo_typo")
        self.assertEqual(rc, 0, out)
        self.assertIn("WAIVED (assumed reached): script_demo_dyn_target", out)
        self.assertIn("WARN --assume-reached names demo_typo, which is not a script in TARGET (ignored)", out)
        rc, out = self.run_cmd("verify-port", self.base, t, "--expect", "demo_dyn_target")      # --expect never waives
        self.assertEqual(rc, 1, out)

    # ---- opcodes
    def test_unknown_opcode_in_new_script_fails(self):
        t = self.good_target("badop")
        append_scripts(os.path.join(t, "scripts.txt"), [("demo_new_badop", ["7777 0"])])
        append_simple_trigger(os.path.join(t, "simple_triggers.txt"), call(6))
        rc, out = self.run_cmd("verify-port", self.base, t)
        self.assertEqual(rc, 1, out)
        self.assertTrue(self.line_for(out, "opcodes").startswith("FAIL"), out)
        self.assertIn("script:demo_new_badop uses unknown opcode 7777", out)
        self.assertTrue(self.line_for(out, "reachable").startswith("PASS"), out)

    # ---- options
    def test_option_without_a_value_is_a_clean_error(self):
        for flag in ("--expect", "--allow-edit", "--touched", "--assume-reached"):
            rc, out = self.run_cmd("verify-port", self.base, self.base, flag)
            self.assertEqual(rc, 1, flag)
            self.assertEqual(out.strip(), "error: %s needs a value" % flag)
        rc, out = self.run_cmd("verify-port", self.base, self.base, "--expect", "--touched", "x")
        self.assertEqual(out.strip(), "error: --expect needs a value")

    # ---- usage
    def test_usage_and_missing_folder_exit_1(self):
        rc, out = self.run_cmd("verify-port", self.base)
        self.assertEqual(rc, 1)
        self.assertIn("usage: verify-port", out)
        rc, out = self.run_cmd("verify-port", self.base, os.path.join(self.tmp, "no-such-folder"))
        self.assertEqual(rc, 1)
        self.assertIn("not a folder", out)


CLEAN_LOG = """Warband log
Loading module
Everything loaded fine
"""

BAD_LOG = """Initializing
SCRIPT ERROR ON OPCODE 506: Invalid Troop ID: 912; LINE: 4
fine line
Invalid party template id 77 in set slot
Unable to find texture ui_mod.dds
script error on opcode 12 (lowercase)
Unable to open file ui.csv
UNABLE TO MAP GAME PRESENTATION CODE 14
couldn't load sound.wav
get_object failed for id 5
"""


class CheckLog(unittest.TestCase):
    def write(self, text):
        d = tempfile.mkdtemp(prefix="wbtools-log-")
        self.addCleanup(shutil.rmtree, d, True)
        p = os.path.join(d, "rgl_log.txt")
        with open(p, "wb") as fh:
            fh.write(text.encode("latin-1"))
        return p

    def test_clean_log_is_ok(self):
        out, ok = verify.check_log(self.write(CLEAN_LOG))
        self.assertTrue(ok)
        self.assertEqual(len(out), 1)
        self.assertIn("check-log OK: 0 errors, 0 cosmetic (not counted) in 3 lines", out[0])

    def test_error_lines_are_listed_by_kind(self):
        out, ok = verify.check_log(self.write(BAD_LOG))
        self.assertFalse(ok)
        self.assertEqual(out[0], "line 2 [script-error] SCRIPT ERROR ON OPCODE 506: Invalid Troop ID: 912; LINE: 4")
        self.assertIn("line 4 [invalid-id] Invalid party template id 77 in set slot", out)
        self.assertIn("line 6 [script-error] script error on opcode 12 (lowercase)", out)
        self.assertIn("line 7 [missing-file] Unable to open file ui.csv", out)
        self.assertIn("line 8 [unable-to-map] UNABLE TO MAP GAME PRESENTATION CODE 14", out)
        self.assertIn("line 9 [missing-file] couldn't load sound.wav", out)
        self.assertIn("line 10 [missing-file] get_object failed for id 5", out)
        self.assertNotIn("line 3", " ".join(out))
        self.assertIn("script-error=2, invalid-id=1, unable-to-map=1, missing-file=3, cosmetic=1", out[-1])
        self.assertTrue(out[-1].startswith("check-log FAIL: 7 errors, 1 cosmetic (not counted) in 10 lines"))

    def test_cosmetic_warnings_are_counted_but_do_not_fail(self):
        text = "Unable to find material m_x\nUnable to find texture t.dds\nmissing mesh brf_a\nFailed to load mesh brf_b\n"
        out, ok = verify.check_log(self.write(text))
        self.assertTrue(ok)
        self.assertEqual(out[0], "line 1 [cosmetic] Unable to find material m_x")
        self.assertIn("check-log OK: 0 errors, 4 cosmetic (not counted) in 4 lines", out[-1])
        out, ok = verify.check_log(self.write(text + "Unable to find sound s.wav\n"))
        self.assertFalse(ok)
        self.assertIn("line 5 [missing-file] Unable to find sound s.wav", out)

    def test_glued_records_are_split(self):
        glued = "SCRIPT ERROR ON OPCODE 1: bad idUnable to find texture a.ddsSCRIPT ERROR ON OPCODE 2: xUNABLE TO MAP THING 3"
        out, ok = verify.check_log(self.write("noise\n" + glued + "\n"))
        self.assertFalse(ok)
        self.assertIn("line 2 [script-error] SCRIPT ERROR ON OPCODE 1: bad id", out)
        self.assertIn("line 2 [script-error] SCRIPT ERROR ON OPCODE 2: x", out)
        self.assertIn("line 2 [unable-to-map] UNABLE TO MAP THING 3", out)
        self.assertIn("line 2 [cosmetic] Unable to find texture a.dds", out)
        self.assertIn("script-error=2, invalid-id=0, unable-to-map=1, missing-file=0, cosmetic=1", out[-1])

    def test_each_pattern_alone(self):
        for text, kind in (("SCRIPT ERROR ON OPCODE 1", "script-error"), ("invalid ID", "invalid-id"),
                           ("Invalid scene prop id", "invalid-id"), ("File not found: x.brf", "missing-file"),
                           ("Cannot open file", "missing-file"), ("missing texture foo", "cosmetic"),
                           ("unable   to map x", "unable-to-map"), ("get_object failed", "missing-file")):
            out, ok = verify.check_log(self.write(text + "\n"))
            self.assertEqual(ok, kind == "cosmetic", text)
            self.assertIn("[%s]" % kind, out[0], text)
        for text in ("invalidated cache", "the idea was valid", "Loaded 3 scripts"):
            self.assertTrue(verify.check_log(self.write(text + "\n"))[1], text)

    def test_output_is_capped_but_totals_are_not(self):
        out, ok = verify.check_log(self.write("SCRIPT ERROR ON OPCODE 1\n" * 250))
        self.assertFalse(ok)
        self.assertEqual(len(out), 202)
        self.assertEqual(out[200], "... 50 more error lines not shown")
        self.assertIn("script-error=250", out[-1])

    def test_unreadable_log_raises(self):
        with self.assertRaises(LookupError):
            verify.check_log(os.path.join(tempfile.gettempdir(), "wbtools-no-such-dir", "rgl_log.txt"))

    def test_cli_exit_codes_without_any_tables(self):
        """check-log works on a toolkit copy that has no generated tables."""
        tool = tempfile.mkdtemp(prefix="wbtools-notables-")
        self.addCleanup(shutil.rmtree, tool, True)
        shutil.copytree(os.path.join(REPO, "wbsd"), os.path.join(tool, "wbsd"), ignore=shutil.ignore_patterns(
            "__pycache__", "opref_data.py", "header_tables.py", "*.tmp"))
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        script = os.path.join(tool, "wbsd", "wbsd.py")

        def run(*args):
            r = subprocess.run([sys.executable, script] + list(args), env=env, capture_output=True, text=True)
            self.assertNotIn("Traceback", r.stderr)
            return r.returncode, r.stdout
        rc, out = run("check-log", self.write(CLEAN_LOG))
        self.assertEqual(rc, 0, out)
        rc, out = run("check-log", self.write(BAD_LOG))
        self.assertEqual(rc, 1, out)
        self.assertIn("line 2 [script-error]", out)
        rc, out = run("check-log")
        self.assertEqual(rc, 1)
        self.assertIn("usage: check-log RGL_LOG", out)
        rc, out = run("check-log", os.path.join(tool, "nope.txt"))
        self.assertEqual(rc, 1)
        self.assertIn("cannot read", out)
        rc, out = run("verify-port", tool, tool)           # needs tables: says so instead of a traceback
        self.assertNotEqual(rc, 0)


if __name__ == "__main__":
    unittest.main()
