"""wbport harness tests. Everything runs on temp copies of the invented demo module
(tests/fixtures/minimod); no Warband data is needed and nothing is written outside temp folders."""
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wbasm  # noqa: E402
import wbport  # noqa: E402
from wbops import ASSIGN, CALL_SCRIPT, GVAR, SCRIPT, V  # noqa: E402
from wbasm import TRY_BEGIN, TRY_END  # noqa: E402
from wbsd import config  # noqa: E402

MINIMOD = os.path.join(REPO, "tests", "fixtures", "minimod")

# A tiny menus.txt (one menu, two options) written into the temp copy; minimod has none.
MENUS = (b"menusfile version 1\r\n 1\r\n"
         b"menu_demo_start 0 Welcome none 0 2\r\n"
         b" mno_demo_go 0 Go 1 2133 2 144115188075855872 1 . mno_demo_back 0 Back 0 .\r\n")


def symlinks_work():
    """True if this machine can create a symlink (Windows without the privilege cannot)."""
    if not hasattr(os, "symlink"):
        return False
    with tempfile.TemporaryDirectory() as d:
        try:
            os.symlink(d, os.path.join(d, "probe"))
        except (OSError, NotImplementedError):
            return False
    return True


NEEDS_SYMLINKS = unittest.skipUnless(symlinks_work(), "symlinks are unavailable or not permitted")


def read(path):
    with open(path, "rb") as fh:
        return fh.read()


def snapshot(folder):
    """{relative path: bytes} of every file under folder."""
    out = {}
    for root, _dirs, files in os.walk(folder):
        for f in files:
            p = os.path.join(root, f)
            out[os.path.relpath(p, folder)] = read(p)
    return out


class PortCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="wbport-test-")
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.modules = os.path.join(self.tmp, "Modules")      # stands in for the Steam folder
        os.makedirs(self.modules)
        work = os.path.join(self.tmp, "work")
        os.makedirs(work)
        self.target = os.path.join(work, "target")
        self.source = os.path.join(work, "source")
        shutil.copytree(MINIMOD, self.target)
        shutil.copytree(MINIMOD, self.source)
        with open(os.path.join(self.target, "menus.txt"), "wb") as fh:
            fh.write(MENUS)
        with open(os.path.join(self.source, "variables.txt"), "wb") as fh:
            fh.write(b"demo_flag\ndemo_counter\n")             # reversed, so ids differ
        patcher = mock.patch.object(config, "MODULES_DIR", self.modules)
        patcher.start()
        self.addCleanup(patcher.stop)

    def port(self, **kw):
        kw.setdefault("source", self.source)
        return wbport.Port("demo", self.target, **kw)

    def feature(self, p):
        """A small complete port: a script, a trigger and a menu call."""
        body = [p.statement(TRY_BEGIN), p.statement(ASSIGN, GVAR(1), 1), p.statement(TRY_END)]
        idx = p.add_script_once("demo_script_new", body)
        p.add_simple_trigger_once(12.0, [p.statement(CALL_SCRIPT, SCRIPT(idx))], calls="demo_script_new")
        p.menu_add_call_once("menu_demo_start", "mno_demo_go", "demo_script_new")

    def path(self, name):
        return os.path.join(self.target, name)


class Harness(PortCase):
    def test_backup_made_once_and_never_overwritten(self):
        before = read(self.path("scripts.txt"))
        with self.port() as p:
            self.feature(p)
        bak = self.path("scripts.txt.bak_before_demo")
        self.assertEqual(read(bak), before)
        self.assertNotEqual(read(self.path("scripts.txt")), before)
        with open(bak, "wb") as fh:                 # a hand-made backup must survive another run
            fh.write(b"mine")
        with self.port() as p:
            p.doc("scripts")
        self.assertEqual(read(bak), b"mine")

    def test_second_run_changes_nothing(self):
        with self.port() as p:
            self.feature(p)
        first = snapshot(self.target)
        with self.port() as p:
            self.feature(p)
            self.assertEqual(len(p.notes), 3)
        self.assertEqual(snapshot(self.target), first)

    def test_written_scripts_and_calls(self):
        with self.port() as p:
            self.feature(p)
        scripts = wbasm.load_scripts(self.path("scripts.txt"))
        self.assertEqual(scripts.index_of("demo_script_new"), 4)
        self.assertTrue(read(self.path("scripts.txt")).endswith(b"\r\n"))
        st = wbasm.load_simple_triggers(self.path("simple_triggers.txt"))
        self.assertEqual(len(st.triggers), 3)
        opt = wbasm.load_menus(self.path("menus.txt")).by_name("menu_demo_start").options[0]
        self.assertEqual(opt.consequences()[-1].operands, [SCRIPT(4)])

    def test_changed_script_raises_and_writes_nothing(self):
        with self.port() as p:
            p.add_script_once("demo_script_new", [p.statement(ASSIGN, GVAR(0), 1)])
        first = snapshot(self.target)
        with self.assertRaises(wbport.PortError):
            with self.port() as p:
                p.add_script_once("demo_script_new", [p.statement(ASSIGN, GVAR(0), 2)])
        self.assertEqual(snapshot(self.target), first)

    def test_dry_run_writes_nothing(self):
        first = snapshot(self.target)
        with self.port(dry_run=True) as p:
            self.feature(p)
        self.assertEqual(p.saved_tables, ["menus", "scripts", "simple_triggers"])
        self.assertEqual(snapshot(self.target), first)           # no backup, no log, no table change

    def test_exception_writes_nothing(self):
        class Boom(Exception):
            pass
        with self.assertRaises(Boom):
            with self.port() as p:
                self.feature(p)
                raise Boom("boom")
        self.assertEqual(read(self.path("scripts.txt")), read(os.path.join(MINIMOD, "scripts.txt")))
        self.assertEqual(read(self.path("simple_triggers.txt")),
                         read(os.path.join(MINIMOD, "simple_triggers.txt")))
        self.assertEqual(read(self.path("menus.txt")), MENUS)
        self.assertFalse(os.path.exists(self.path(wbport.LOG_NAME)))

    def test_refuses_target_inside_modules_folder(self):
        inside = os.path.join(self.modules, "Copy")
        shutil.copytree(self.target, inside)
        with self.assertRaises(wbport.PortError) as cm:
            wbport.Port("demo", inside)
        self.assertIn("copy", str(cm.exception).lower())
        with wbport.Port("demo", inside, allow_modules_dir=True) as p:
            p.add_script_once("demo_script_new", [])
        self.assertIn(b"demo_script_new", read(os.path.join(inside, "scripts.txt")))

    def test_env_modules_dir_is_what_the_refusal_uses(self):
        # config reads WB_MODULES_DIR at import; prove the check reads config.MODULES_DIR live
        with mock.patch.object(config, "MODULES_DIR", self.tmp):
            with self.assertRaises(wbport.PortError):
                wbport.Port("demo", self.target)

    def test_log_line(self):
        with self.port() as p:
            self.feature(p)
        lines = read(self.path(wbport.LOG_NAME)).decode().splitlines()
        self.assertEqual(len(lines), 1)
        rec = json.loads(lines[0])
        self.assertEqual(rec["name"], "demo")
        self.assertEqual(rec["tables"], ["menus", "scripts", "simple_triggers"])
        self.assertEqual(rec["scripts_added"], ["demo_script_new"])
        self.assertEqual(rec["source"], self.source)
        self.assertIn("time", rec)

    def test_log_false_writes_no_log(self):
        with self.port(log=False) as p:
            self.feature(p)
        self.assertFalse(os.path.exists(self.path(wbport.LOG_NAME)))

    def test_unbalanced_block_is_refused_before_anything_is_written(self):
        first = snapshot(self.target)
        with self.assertRaises(wbport.PortError):
            with self.port() as p:
                p.add_script_once("demo_script_bad", [p.statement(TRY_BEGIN)])
        self.assertEqual(snapshot(self.target), first)

    def test_unbalanced_edit_of_existing_script_is_caught_at_save(self):
        first = read(self.path("scripts.txt"))
        with self.assertRaises(wbport.PortError) as cm:
            with self.port() as p:
                s = p.doc("scripts").by_name("demo_script_unused")
                s.set_statements(s.statements() + [p.statement(TRY_BEGIN)])
        self.assertIn("demo_script_unused", str(cm.exception))
        self.assertEqual(read(self.path("scripts.txt")), first)

    def test_table_that_does_not_round_trip_is_refused(self):
        with open(self.path("simple_triggers.txt"), "ab") as fh:
            fh.write(b"\n\n")                   # blank trailer lines the parser drops
        with self.assertRaises(wbport.PortError):
            with self.port() as p:
                p.doc("simple_triggers")

    def test_save_check_catches_line_ending_change(self):
        with self.assertRaises(wbport.PortError) as cm:
            with self.port() as p:
                self.feature(p)
                scripts = p.doc("scripts")
                scripts.scripts[-1]._name_line = b"demo_script_new -1\n"   # LF line in a CRLF file
        self.assertIn("line endings", str(cm.exception))

    def test_save_check_catches_roundtrip_failure(self):
        real = wbasm.ScriptsDoc.serialize
        target = self.target

        def unstable(doc):          # a parser that does not reproduce what it wrote, once re-read
            data = real(doc)
            return data if doc.path.startswith(target) else data + b"\r\n"
        with mock.patch.object(wbasm.ScriptsDoc, "serialize", unstable):
            with self.assertRaises(wbport.PortError) as cm:
                with self.port() as p:
                    self.feature(p)
        self.assertIn("round-trip", str(cm.exception))
        self.assertNotIn(b"demo_script_new", read(self.path("scripts.txt")))

    def test_unknown_table_and_missing_file(self):
        with self.port() as p:
            with self.assertRaises(wbport.PortError):
                p.doc("nope")
            with self.assertRaises(wbport.PortError):
                p.doc("conversation")           # the demo module has no conversation.txt

    def test_missing_menu_option_lists_close_matches(self):
        with self.port() as p:
            with self.assertRaises(wbport.PortError) as cm:
                p.menu_add_call_once("menu_demo_start", "mno_demo_gp", "demo_script_bump")
            self.assertIn("mno_demo_go", str(cm.exception))

    def test_source_id_needs_a_source(self):
        with wbport.Port("demo", self.target) as p:
            with self.assertRaises(wbport.PortError):
                p.source_id("global", "demo_flag")

    def test_statement_helper(self):
        st = wbport.Port.statement(ASSIGN, V(0), 5)
        self.assertEqual((st.opcode, st.operands), (ASSIGN, [V(0), 5]))

    def test_trigger_without_script_name_raises(self):
        with self.assertRaises(wbport.PortError):
            with self.port() as p:
                p.add_simple_trigger_once(1.0, [], calls="demo_script_missing")

    def test_menu_call_in_conditions(self):
        with self.port() as p:
            self.assertTrue(p.menu_add_call_once("menu_demo_start", "mno_demo_back", "demo_script_bump",
                                                 where="conditions"))
            self.assertFalse(p.menu_add_call_once("menu_demo_start", "mno_demo_back", "demo_script_bump",
                                                  where="conditions"))
            with self.assertRaises(wbport.PortError):
                p.menu_add_call_once("menu_demo_start", "mno_demo_back", "demo_script_bump", where="x")


    # --- reviewer fix round 1 ---------------------------------------------------------
    def _inside_copy(self):
        inside = os.path.join(self.modules, "Copy")
        shutil.copytree(self.target, inside)
        return inside

    def test_refuses_case_variant_path(self):
        inside = self._inside_copy()
        variant = os.path.join(os.path.dirname(self.modules), "modules", "Copy")
        if not os.path.exists(variant):
            self.skipTest("temp filesystem is case-sensitive")
        with self.assertRaises(wbport.PortError):
            wbport.Port("demo", variant)

    @NEEDS_SYMLINKS
    def test_refuses_trailing_slash_dotdot_and_symlink(self):
        inside = self._inside_copy()
        os.makedirs(os.path.join(self.modules, "Other"))
        link = os.path.join(self.tmp, "link")
        os.symlink(inside, link)
        for spelled in (inside + os.sep, os.path.join(self.modules, "Other", "..", "Copy"), link,
                        self.modules):
            with self.assertRaises(wbport.PortError, msg=spelled):
                wbport.Port("demo", spelled)

    def test_unbalanced_block_elsewhere_in_unit_is_not_blamed(self):
        menus = (b"menusfile version 1\r\n 1\r\n"
                 b"menu_demo_start 0 Welcome none 0 2\r\n"
                 b" mno_bad 0 Bad 1 4 0 . mno_ok 0 Ok 0 .\r\n")
        with open(self.path("menus.txt"), "wb") as fh:
            fh.write(menus)
        with self.port() as p:
            idx = p.add_script_once("demo_script_new", [])
            self.assertTrue(p.menu_add_call_once("menu_demo_start", "mno_ok", "demo_script_new"))
        opt = wbasm.load_menus(self.path("menus.txt")).by_name("menu_demo_start").options[1]
        self.assertEqual(opt.consequences()[-1].operands, [SCRIPT(idx)])
        with self.assertRaises(wbport.PortError):       # but editing the bad option itself is caught
            with self.port() as p:
                p.menu_add_call_once("menu_demo_start", "mno_bad", "demo_script_new")

    @NEEDS_SYMLINKS
    def test_symlinked_table_is_refused(self):
        real = os.path.join(self.tmp, "real_scripts.txt")
        shutil.move(self.path("scripts.txt"), real)
        os.symlink(real, self.path("scripts.txt"))
        before = read(real)
        with self.assertRaises(wbport.PortError) as cm:
            with self.port() as p:
                p.add_script_once("demo_script_new", [])
        self.assertIn("symlink", str(cm.exception))
        self.assertTrue(os.path.islink(self.path("scripts.txt")))
        self.assertEqual(read(real), before)

    def test_partial_replace_failure_restores_tables(self):
        first = snapshot(self.target)
        real_replace = os.replace
        calls = []

        def flaky(src, dst):
            calls.append(dst)
            if len(calls) == 2:
                raise OSError("disk full")
            return real_replace(src, dst)
        with mock.patch.object(os, "replace", flaky):
            with self.assertRaises(wbport.PortError):
                with self.port() as p:
                    self.feature(p)
        after = snapshot(self.target)
        for name, data in first.items():
            self.assertEqual(after[name], data, name)
        self.assertEqual(set(after) - set(first), {n for n in after if n.endswith(".bak_before_demo")})

    def test_existing_call_not_first_statement_is_found(self):
        with self.port() as p:
            idx = p.add_script_once("demo_script_new", [])
            body = [p.statement(ASSIGN, GVAR(1), 1), p.statement(CALL_SCRIPT, SCRIPT(idx))]
            self.assertTrue(p.add_simple_trigger_once(5.0, body, calls="demo_script_new"))
        with self.port() as p:
            self.assertFalse(p.add_simple_trigger_once(5.0, body, calls="demo_script_new"))
            self.assertTrue(p.menu_add_call_once("menu_demo_start", "mno_demo_go", "demo_script_new"))
        with self.port() as p:      # the menu call now sits after the original first statement
            self.assertFalse(p.menu_add_call_once("menu_demo_start", "mno_demo_go", "demo_script_new"))
            opt = p.doc("menus").by_name("menu_demo_start").options[0]
            self.assertEqual(len(opt.consequences()), 2)

    def test_flag_only_difference_counts_as_different(self):
        with self.port() as p:
            p.add_script_once("demo_script_new", [p.statement(ASSIGN, GVAR(1), 1)])
        with self.assertRaises(wbport.PortError):
            with self.port() as p:
                p.add_script_once("demo_script_new", [p.statement(ASSIGN, GVAR(1), 1, flags=wbasm.OP_NEG)])

    # --- script_ prefix handling (ruling R3-2) ------------------------------------------
    def test_script_prefix_accepted_by_has_script_and_once_helpers(self):
        with self.port() as p:
            self.assertTrue(p.has_script("script_demo_script_bump"))
            self.assertTrue(p.has_script("demo_script_bump"))
            self.assertFalse(p.has_script("script_demo_script_nope"))
            idx = p.add_script_once("demo_script_new", [])
            self.assertTrue(p.add_simple_trigger_once(
                3.0, [p.statement(CALL_SCRIPT, SCRIPT(idx))], calls="script_demo_script_new"))
            self.assertFalse(p.add_simple_trigger_once(
                3.0, [p.statement(CALL_SCRIPT, SCRIPT(idx))], calls="demo_script_new"))
            self.assertTrue(p.menu_add_call_once("menu_demo_start", "mno_demo_go", "script_demo_script_new"))
            self.assertFalse(p.menu_add_call_once("menu_demo_start", "mno_demo_go", "demo_script_new"))

    def test_add_script_once_refuses_prefixed_name(self):
        first = snapshot(self.target)
        with self.assertRaises(wbport.PortError) as cm:
            with self.port() as p:
                p.add_script_once("script_demo_new", [])
        self.assertIn("without the 'script_' prefix", str(cm.exception))
        self.assertIn("demo_new", str(cm.exception))
        self.assertEqual(snapshot(self.target), first)


class Lookups(PortCase):
    """By-name lookups go through wbsd.corpus, which needs the generated header tables."""

    def setUp(self):
        import _support
        _support.require_tables()
        PortCase.setUp(self)

    def test_lookup_by_name_target_and_source(self):
        with self.port() as p:
            self.assertEqual(p.id("global", "demo_flag"), 1)
            self.assertEqual(p.source_id("global", "demo_flag"), 0)
            self.assertEqual(p.id("script", "demo_script_bump"), 1)
            self.assertEqual(p.id("script", "script_demo_script_bump"), 1)
            self.assertEqual(p.source_id("script", "script_demo_script_bump"), 1)
            self.assertEqual(p.source_id("script", "demo_script_bump"), 1)
            idx = p.add_script_once("demo_script_new", [])
            self.assertEqual(p.id("script", "demo_script_new"), idx)   # sees scripts added this run
            self.assertTrue(p.has_script("demo_script_new"))
            self.assertFalse(p.has_script("demo_script_nope"))

    def test_missing_name_lists_close_matches(self):
        with self.port() as p:
            with self.assertRaises(wbport.PortError) as cm:
                p.id("global", "demo_flg")
            self.assertIn("demo_flag", str(cm.exception))
            with self.assertRaises(wbport.PortError):
                p.source_id("global", "nothing_like_it_zzz")
            with self.assertRaises(wbport.PortError):
                p.id("no_such_kind", "x")

    def test_name_forms_for_each_kind(self):
        with self.port() as p:
            # global: with or without the $
            self.assertEqual(p.id("global", "$demo_flag"), 1)
            self.assertEqual(p.id("global", "demo_flag"), 1)
            self.assertEqual(p.source_id("global", "$demo_flag"), 0)
            self.assertEqual(p.source_id("global", "demo_flag"), 0)
            # script: with or without script_
            self.assertEqual(p.id("script", "script_demo_script_bump"), p.id("script", "demo_script_bump"))
            # troop, string and the like: exactly as shown, with the prefix
            self.assertEqual(p.id("troop", "trp_demo_hero"), 0)
            self.assertEqual(p.id("string", "str_demo_hello"), 1)
            for kind, bare in (("troop", "demo_hero"), ("string", "demo_hello")):
                with self.assertRaises(wbport.PortError):
                    p.id(kind, bare)


class Remap(PortCase):
    """source_doc and remap. The source gets one extra script in front, so its script ids differ
    from the target's, and its globals are already reversed (see PortCase.setUp)."""

    FRONT = b"demo_script_front -1\r\n 1 1000 1 216172782113783809\r\n"

    def setUp(self):
        import _support
        _support.require_tables()
        PortCase.setUp(self)
        sp = os.path.join(self.source, "scripts.txt")
        data = read(sp)
        head = b"scriptsfile version 1\r\n4\r\n"
        self.assertTrue(data.startswith(head))
        with open(sp, "wb") as fh:
            fh.write(b"scriptsfile version 1\r\n5\r\n" + self.FRONT + data[len(head):])

    def test_source_doc_is_the_source_and_read_only(self):
        before_src, before_tgt = snapshot(self.source), snapshot(self.target)
        with self.port() as p:
            doc = p.source_doc("scripts")
            self.assertEqual(doc.scripts[0].name, "demo_script_front")
            self.assertIs(p.source_doc("scripts"), doc)
            doc.append_script("demo_scratch", [])          # edits to it are discarded
        self.assertEqual(snapshot(self.source), before_src)
        self.assertEqual(snapshot(self.target), before_tgt)    # nothing saved, no backup either
        with self.assertRaises(wbport.PortError):
            wbport.Port("demo", self.target).source_doc("scripts")

    def test_remap_translates_by_name_and_keeps_the_rest(self):
        with self.port() as p:
            src_bump = p.source_id("script", "demo_script_bump")
            self.assertNotEqual(src_bump, p.id("script", "demo_script_bump"))
            self.assertNotEqual(p.source_id("global", "demo_flag"), p.id("global", "demo_flag"))
            st = p.statement(CALL_SCRIPT, SCRIPT(src_bump), GVAR(p.source_id("global", "demo_flag")),
                             V(3), 7, -2, flags=wbasm.OP_NEG)
            new = p.remap(st)
            self.assertIsNot(new, st)
            self.assertEqual(new.opcode, CALL_SCRIPT)
            self.assertEqual(new.flags, wbasm.OP_NEG)
            self.assertEqual(new.operands, [SCRIPT(p.id("script", "demo_script_bump")),
                                            GVAR(p.id("global", "demo_flag")), V(3), 7, -2])
            self.assertEqual(st.operands[0], SCRIPT(src_bump))     # the original is untouched

    def test_remap_missing_record_raises_naming_it(self):
        with self.port() as p:
            front = p.source_id("script", "demo_script_front")
            with self.assertRaises(wbport.PortError) as cm:
                p.remap(p.statement(CALL_SCRIPT, SCRIPT(front)))
            self.assertIn("demo_script_front", str(cm.exception))
            with self.assertRaises(wbport.PortError):
                p.remap(p.statement(ASSIGN, GVAR(99), 1))          # source id out of range

    def test_remap_needs_a_source(self):
        with wbport.Port("demo", self.target) as p:
            with self.assertRaises(wbport.PortError):
                p.remap(p.statement(ASSIGN, GVAR(0), 1))

    def test_copy_a_source_script_with_remap(self):
        with self.port() as p:
            src = p.source_doc("scripts").by_name("demo_script_read_flag")
            body = [p.remap(s) for s in src.statements()]
            idx = p.add_script_once("demo_copied", body)
            self.assertEqual(idx, 4)
        again = wbasm.load_scripts(self.path("scripts.txt")).by_name("demo_copied")
        dest = [o for st in again.statements() for o in st.operands]
        self.assertIn(GVAR(0), dest)          # the script reads demo_counter: id 1 in the source, 0 here
        self.assertNotIn(GVAR(1), dest)
        with self.port() as p:                # second run: no change
            before = snapshot(self.target)
            body = [p.remap(s) for s in p.source_doc("scripts").by_name("demo_script_read_flag").statements()]
            p.add_script_once("demo_copied", body)
        self.assertEqual(snapshot(self.target), before)


if __name__ == "__main__":
    unittest.main()
