"""Tests that run anywhere: they use the invented demo module in tests/fixtures/minimod and the
invented headers in tests/fixtures/headers, so no Warband data and no generated tables are needed.

The wbsd command line runs in a subprocess against a TEMP copy of the toolkit; the real
wbsd/opref_data.py and wbsd/header_tables.py are never touched.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
import wbasm  # noqa: E402

FIXTURES = os.path.join(REPO, "tests", "fixtures")
MINIMOD = os.path.join(FIXTURES, "minimod")
HEADERS = os.path.join(FIXTURES, "headers")
ROUNDTRIP_FILES = ("scripts.txt", "simple_triggers.txt")


def _read(path):
    with open(path, "rb") as fh:
        return fh.read()


class FixtureRoundTrip(unittest.TestCase):
    def test_fixture_files_exist(self):
        for name in ROUNDTRIP_FILES + ("variables.txt", "strings.txt", "troops.txt"):
            self.assertTrue(os.path.isfile(os.path.join(MINIMOD, name)), name)

    def test_scripts_round_trip_byte_for_byte(self):
        path = os.path.join(MINIMOD, "scripts.txt")
        doc = wbasm.load_scripts(path)
        self.assertEqual(len(doc.scripts), 4)
        self.assertEqual(doc.serialize(), _read(path))

    def test_simple_triggers_round_trip_byte_for_byte(self):
        path = os.path.join(MINIMOD, "simple_triggers.txt")
        doc = wbasm.load_simple_triggers(path)
        self.assertEqual(len(doc.triggers), 2)
        self.assertEqual(doc.serialize(), _read(path))

    def test_every_statement_block_round_trips(self):
        doc = wbasm.load_scripts(os.path.join(MINIMOD, "scripts.txt"))
        for s in doc.scripts:
            stmts = s.statements()
            self.assertEqual(len(stmts), s.declared_count, s.name)
            self.assertEqual(wbasm.emit_statements(stmts), s.tokens, s.name)
            self.assertTrue(wbasm.block_depth_ok(stmts), s.name)

    def test_call_and_try_structure(self):
        doc = wbasm.load_scripts(os.path.join(MINIMOD, "scripts.txt"))
        init = doc.by_name("demo_script_init").statements()
        calls = [wbasm.opval(st.operands[0]) for st in init if st.opcode == 1]
        self.assertEqual(calls, [doc.index_of("demo_script_bump")])
        ops = [st.opcode for st in doc.by_name("demo_script_bump").statements()]
        self.assertEqual(ops[0], 4)    # try_begin
        self.assertEqual(ops[-1], 3)   # try_end

    def test_edited_token_is_seen_after_reload(self):
        """Change one statement token on disk: the reloaded document differs from the original
        and still round-trips its own (edited) bytes."""
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "scripts.txt")
            shutil.copy(os.path.join(MINIMOD, "scripts.txt"), path)
            before = wbasm.load_scripts(path)
            lines = _read(path).decode("ascii").split("\r\n")
            # the line after the script name: " <count> <opcode> <n> <operands...> <opcode> ..."
            i = next(k for k, l in enumerate(lines) if l.startswith("demo_script_init")) + 1
            tokens = lines[i].split(" ")
            tokens[2] = str(int(tokens[2]) + 1)           # change the first statement's opcode
            lines[i] = " ".join(tokens)
            with open(path, "wb") as fh:
                fh.write("\r\n".join(lines).encode("ascii"))
            after = wbasm.load_scripts(path)
            first = lambda d: d.by_name("demo_script_init").statements()[0]
            self.assertNotEqual(first(before).opcode, first(after).opcode)
            self.assertEqual(after.serialize(), _read(path))


class FixtureCli(unittest.TestCase):
    """build_tables on the fixture headers, then wbsd queries on the fixture module."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="wbtools-fixture-")
        cls.addClassCleanup(shutil.rmtree, cls.tmp, True)
        tool = os.path.join(cls.tmp, "tool")
        os.makedirs(tool)
        shutil.copytree(os.path.join(REPO, "wbsd"), os.path.join(tool, "wbsd"), ignore=shutil.ignore_patterns(
            "__pycache__", "opref_data.py", "header_tables.py", "*.tmp"))
        for name in os.listdir(REPO):
            if name.endswith(".py"):
                shutil.copy(os.path.join(REPO, name), tool)
        mods = os.path.join(cls.tmp, "modules")
        shutil.copytree(MINIMOD, os.path.join(mods, "demo"))
        target = os.path.join(mods, "native")
        os.makedirs(target)
        with open(os.path.join(target, "scripts.txt"), "w", newline="") as fh:
            # a stand-in for the base game: one script of the same name as the demo's, with a different body
            fh.write("scriptsfile version 1\n1\ndemo_script_bump -1\n 1 2133 2 144115188075855872 5\n")
        with open(os.path.join(target, "variables.txt"), "w", newline="") as fh:
            fh.write("demo_counter\n")
        cls.registry = os.path.join(cls.tmp, "modules.json")
        with open(cls.registry, "w") as fh:
            json.dump({"modules": [
                {"slug": "demo", "label": "Demo module", "path": "demo", "role": "main"},
                {"slug": "native", "label": "Demo native", "path": "native", "role": "native"}]}, fh)
        cls.run_env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", WB_REGISTRY=cls.registry,
                       WB_MODULES_DIR=mods, WB_CACHE_DIR=os.path.join(cls.tmp, "cache"))
        cls.wbsd = os.path.join(tool, "wbsd", "wbsd.py")
        r = subprocess.run([sys.executable, os.path.join(tool, "wbsd", "build_tables.py"), HEADERS],
                           env=cls.run_env, capture_output=True, text=True)
        assert r.returncode == 0, (r.stdout, r.stderr)
        cls.build_out = r.stdout
        cls.tool = tool

    def run_wbsd(self, *args):
        r = subprocess.run([sys.executable, self.wbsd] + list(args), env=self.run_env,
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, (args, r.stdout, r.stderr))
        self.assertNotIn("Traceback", r.stderr)
        return r.stdout

    def test_build_tables_wrote_the_temp_copy_only(self):
        self.assertIn("wrote opref_data.py and header_tables.py", self.build_out)
        for name in ("opref_data.py", "header_tables.py"):
            self.assertTrue(os.path.isfile(os.path.join(self.tool, "wbsd", name)))
        with open(os.path.join(self.tool, "wbsd", "opref_data.py")) as fh:
            raw = fh.read()
        for line in ("1 call_script", "4 try_begin", "500 troop_set_slot", "2133 assign"):
            self.assertIn(line, raw)

    def test_help_flag_prints_usage_and_runs_nothing(self):
        """`<command> --help` / `-h` must show the usage, not run the command."""
        atlas = os.path.join(self.tmp, "help-atlas")
        os.makedirs(os.path.join(atlas, "features"), exist_ok=True)
        shutil.copy(os.path.join(REPO, "examples", "atlas", "features", "acan.json"),
                    os.path.join(atlas, "features", "acan.json"))

        def snapshot():
            return sorted((os.path.join(d, f), _read(os.path.join(d, f)))
                          for d, _, fs in os.walk(atlas) for f in fs)
        before = snapshot()
        env = dict(self.run_env, WB_ATLAS_DIR=atlas)
        for cmd in ("inventory", "overlaps-apply", "export", "batch"):
            for flag in ("--help", "-h"):
                r = subprocess.run([sys.executable, self.wbsd, cmd, flag], env=env,
                                   capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, (cmd, flag, r.stdout, r.stderr))
                self.assertIn("inventory", r.stdout)       # the usage text
                self.assertNotIn("Traceback", r.stderr)
        self.assertEqual(snapshot(), before)
        self.assertFalse(os.path.exists(os.path.join(atlas, "FEATURE_INVENTORY.md")))

    def test_modules_lists_both(self):
        out = self.run_wbsd("modules")
        self.assertIn("scripts=4", out)
        self.assertIn("Demo native", out)

    def test_dis_names_everything(self):
        lines = [l.strip() for l in self.run_wbsd("dis", "demo", "demo_script_bump").splitlines()]
        for want in ("0  (try_begin),", "1    (gt, $demo_counter, 9),", "3  (else_try),",
                     "4    (troop_set_slot, trp_demo_hero, 3, 1),", "5  (try_end),"):
            self.assertIn(want, lines)

    def test_callers(self):
        out = self.run_wbsd("callers", "demo", "demo_script_bump")
        self.assertIn("callers of script:demo_script_bump (2 call sites):", out)
        self.assertIn("  script:demo_script_init @2", out.splitlines())
        self.assertIn("  script:demo_script_read_flag @1", out.splitlines())
        self.assertNotIn("demo_script_unused", out)

    def test_callers_reach_a_simple_trigger(self):
        out = self.run_wbsd("callers", "demo", "demo_script_init")
        self.assertIn("  strig:0 (every 1h) @0", out.splitlines())

    def test_explain(self):
        out = self.run_wbsd("explain", "demo", "demo_script_bump").splitlines()
        self.assertIn("direct callers (2): script:demo_script_init, script:demo_script_read_flag", out)
        self.assertIn("   strig:0 (every 1h)", out)
        self.assertIn("   strig:1 (every 24h)", out)
        self.assertIn("globals written: demo_counter", out)
        self.assertIn("slots touched (closure): troop[3] s1", out)
        self.assertIn("troop refs: trp_demo_hero", out)
        self.assertTrue(any(l.startswith("native: MODIFIED") for l in out), out)

    def test_closure_into_native(self):
        out = self.run_wbsd("closure", "demo", "demo_script_init", "--into", "native")
        lines = out.splitlines()
        self.assertIn("blocks in closure: 2", lines)
        init = [l for l in lines if "demo_script_init" in l and "stmts" in l]
        bump = [l for l in lines if "demo_script_bump" in l and "stmts" in l]
        self.assertEqual(len(init), 1, out)
        self.assertEqual(len(bump), 1, out)
        self.assertIn("ABSENT in target", init[0])
        self.assertIn("DIFFERS in target", bump[0])
        self.assertNotIn("demo_script_unused", out)
        self.assertIn("   troop: 1 used, 1 missing in target: trp_demo_hero", lines)
        self.assertTrue(any("1 also exist by name in target" in l and l.endswith("demo_counter") for l in lines), out)
        self.assertIn("   donor-only globals: demo_flag", lines)


if __name__ == "__main__":
    unittest.main()
