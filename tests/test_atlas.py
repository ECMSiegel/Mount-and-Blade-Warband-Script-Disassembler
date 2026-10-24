"""Feature atlas: schema validation, overlaps, inventory, search. Uses a temp ATLAS_DIR with invented records."""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _support  # noqa: E402
_support.require_tables()
from wbsd import atlas, config  # noqa: E402


def _rec(fid, **kw):
    r = {"id": fid, "name": "Name of " + fid, "category": "party-ai", "summary": "s", "mechanics": "m",
         "hooks": [], "scripts": ["script_x"], "slots": [], "globals": [], "native_relation": "new",
         "target_status": "absent", "conflicts": [], "difficulty": "low", "risk": "low", "value": 3,
         "recommendation": "adapt", "confidence": "speculative", "evidence": ["e"]}
    r.update(kw)
    return r


def _write(d, rel, obj):
    p = os.path.join(d, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as fh:
        json.dump(obj, fh)
    return p


class AtlasTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old = config.ATLAS_DIR
        config.ATLAS_DIR = os.path.join(self.tmp.name, "atlas")
        self.a = _rec("examplemod.patrols", category="caravans-patrols")
        self.b = _rec("othermod.raiders", category="bandits-outlaws")
        _write(config.ATLAS_DIR, "features/examplemod.json", {"module": "examplemod", "features": [self.a]})
        _write(config.ATLAS_DIR, "features/othermod.json", {"module": "othermod", "features": [self.b]})

    def tearDown(self):
        config.ATLAS_DIR = self.old
        self.tmp.cleanup()

    def _set(self, **kw):
        bad = copy.deepcopy(self.a)
        bad.update(kw)
        _write(config.ATLAS_DIR, "features/examplemod.json", {"module": "examplemod", "features": [bad]})
        return atlas.validate()

    def test_clean(self):
        self.assertEqual(atlas.validate(), [])
        self.assertEqual(len(atlas.load_all()), 2)

    def test_each_enum_violation_reported(self):
        for k in atlas.ENUMS:
            probs = self._set(**{k: "bogus"})
            self.assertTrue(any("bad %s" % k in p for p in probs), (k, probs))

    def test_bad_category_value_and_missing(self):
        self.assertTrue(any("bad category" in p for p in self._set(category="nope")))
        for v in (0, 6, "3", True):
            self.assertTrue(any("bad value" in p for p in self._set(value=v)), v)
        bad = dict(self.a)
        del bad["summary"]
        _write(config.ATLAS_DIR, "features/examplemod.json", {"module": "examplemod", "features": [bad]})
        self.assertIn("examplemod.patrols missing summary", atlas.validate())

    def test_judgement_fields_optional_but_checked_when_present(self):
        self.assertEqual(sorted(atlas.SCHEMA["judgement"]), sorted(
            ["target_status", "target_evidence", "conflicts", "difficulty", "risk", "value", "recommendation"]))
        facts = {k: v for k, v in self.a.items() if k not in atlas.SCHEMA["judgement"]}
        _write(config.ATLAS_DIR, "features/examplemod.json", {"module": "examplemod", "features": [facts]})
        self.assertEqual(atlas.validate(), [])
        for k, bad in (("difficulty", "bogus"), ("value", 9), ("target_status", "bogus")):
            probs = self._set(**{k: bad})
            self.assertTrue(any("bad " + k in p for p in probs), (k, probs))

    def test_inventory_hides_judgement_columns_when_no_record_has_them(self):
        for n, r in (("examplemod", self.a), ("othermod", self.b)):
            facts = {k: v for k, v in r.items() if k not in atlas.SCHEMA["judgement"]}
            _write(config.ATLAS_DIR, "features/%s.json" % n, {"module": n, "features": [facts]})
        text = atlas.build_inventory()
        self.assertIn("| feature | module | confidence |", text)
        self.assertNotIn("difficulty |", text)
        self.assertNotIn("Columns:", text)

    def test_inventory_shows_dash_for_missing_judgement(self):
        facts = {k: v for k, v in self.a.items() if k not in atlas.SCHEMA["judgement"]}
        _write(config.ATLAS_DIR, "features/examplemod.json", {"module": "examplemod", "features": [facts]})
        text = atlas.build_inventory()      # othermod still has judgement fields
        self.assertIn("| difficulty |", text)
        row = [l for l in text.splitlines() if l.startswith("| [Name of examplemod.patrols]")][0]
        self.assertEqual(row.count("—"), 5, row)

    def test_duplicate_id(self):
        _write(config.ATLAS_DIR, "features/othermod.json", {"module": "othermod", "features": [_rec("examplemod.patrols")]})
        self.assertIn("duplicate id examplemod.patrols", atlas.validate())

    def test_apply_overlaps(self):
        _write(config.ATLAS_DIR, "overlaps.json", {"_doc": "x", "mechanics": {
            "roaming groups": ["examplemod.patrols", "othermod.raiders", "ghost.id"]}})
        probs = atlas.apply_overlaps()
        self.assertEqual(len(probs), 1)
        self.assertIn("ghost.id", probs[0])
        got = {f["id"]: f["overlaps"] for f in atlas.load_all()}
        self.assertEqual(got, {"examplemod.patrols": ["othermod.raiders"], "othermod.raiders": ["examplemod.patrols"]})

    def test_non_string_id_reported_not_crash(self):
        for bad_id in (7, ["x"], None):
            self._set(id=bad_id)
            probs = atlas.validate()
            self.assertTrue(any(p.startswith("examplemod.json: id must be a string") for p in probs), (bad_id, probs))
            self._raw("overlaps.json", json.dumps({"mechanics": {"m": ["othermod.raiders"]}}))
            self.assertEqual(atlas.apply_overlaps(), [])
            for cmd in (["features-check"], ["feature", "x"]):
                self.assertNotIn("Traceback", self._cli(*cmd).stderr, (bad_id, cmd))
            self.assertIn("id must be a string", self._cli("features-check").stdout)

    def test_inventory_skips_non_string_id_with_warning(self):
        for bad_id in (7, ["x"], None):
            self._set(id=bad_id)
            text = atlas.build_inventory()          # must not raise
            self.assertIn("WARNING: skipped a record of module examplemod: id must be a string", text)
            self.assertIn("othermod.raiders", text)
            self.assertIn("1 features across 1 modules", text)
            r = self._cli("inventory")
            self.assertEqual(r.returncode, 0, (bad_id, r.stderr))
            self.assertNotIn("Traceback", r.stderr)
            self.assertNotIn("Traceback", self._cli("features").stderr)

    def test_malformed_registry_names_the_file(self):
        for text in ("{not json", "[1]", '{"modules": 5}', '{"modules": [3]}'):
            reg = self._raw("bad_modules.json", text)
            env = dict(os.environ, WB_REGISTRY=reg, WB_ATLAS_DIR=config.ATLAS_DIR, PYTHONDONTWRITEBYTECODE="1")
            r = subprocess.run([sys.executable, os.path.join(config.REPO, "wbsd", "wbsd.py"), "features-check"],
                               env=env, capture_output=True, text=True)
            self.assertEqual(r.returncode, 1, (text, r.stdout, r.stderr))
            self.assertNotIn("Traceback", r.stderr, text)
            self.assertIn("bad_modules.json", r.stdout, text)
            self.assertTrue(r.stdout.startswith("error: "), r.stdout)
        # a missing registry file is still just "no main module"
        env = dict(os.environ, WB_REGISTRY=os.path.join(self.tmp.name, "nope.json"), WB_ATLAS_DIR=config.ATLAS_DIR,
                   PYTHONDONTWRITEBYTECODE="1")
        r = subprocess.run([sys.executable, "-c", "from wbsd import config; print(config.MAIN)"], cwd=config.REPO,
                           env=env, capture_output=True, text=True)
        self.assertEqual((r.returncode, r.stdout.strip()), (0, "None"), r.stderr)

    def test_bad_regex_is_clean_error(self):
        for cmd in (["features", "("], ["grep", "(", "--mods", "native"], ["text", "[", "--mods", "native"]):
            r = self._cli(*cmd)
            self.assertNotIn("Traceback", r.stderr, cmd)
            self.assertEqual(r.returncode, 1, cmd)
            self.assertTrue(r.stdout.startswith("error: "), (cmd, r.stdout))

    def test_overlaps_missing_file(self):
        self.assertIn("no overlaps.json", atlas.apply_overlaps()[0])

    def test_inventory(self):
        text = atlas.build_inventory()
        self.assertIn("examplemod.patrols", text)
        self.assertIn("othermod.raiders", text)
        self.assertIn("2 features across 2 modules", text)
        path = atlas.write_inventory()
        self.assertEqual(path, os.path.join(config.ATLAS_DIR, "FEATURE_INVENTORY.md"))
        self.assertTrue(os.path.isfile(path))

    def test_search_filters(self):
        self.assertEqual(len(atlas.search()), 2)
        self.assertEqual([f["id"] for f in atlas.search(category="bandits-outlaws")], ["othermod.raiders"])
        self.assertEqual([f["id"] for f in atlas.search(module="examplemod")], ["examplemod.patrols"])
        self.assertEqual([f["id"] for f in atlas.search("raiders")], ["othermod.raiders"])
        self.assertEqual(atlas.search(category="bandits-outlaws", module="examplemod"), [])

    def test_show_uses_target_fields(self):
        lines = atlas.show(_rec("x.y", target_evidence="nothing similar"))
        self.assertTrue(any(l.startswith("target_status:") for l in lines))
        self.assertTrue(any(l.startswith("target_evidence:") for l in lines))

    def _raw(self, rel, text):
        p = os.path.join(config.ATLAS_DIR, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write(text)
        return p

    @staticmethod
    def _read(path):
        with open(path) as fh:
            return fh.read()

    def _cli(self, *args):
        r = subprocess.run([sys.executable, os.path.join(config.REPO, "wbsd", "wbsd.py")] + list(args),
                           env=dict(os.environ, WB_ATLAS_DIR=config.ATLAS_DIR, PYTHONDONTWRITEBYTECODE="1"),
                           capture_output=True, text=True)
        return r

    def test_inventory_failure_keeps_old_file(self):
        path = atlas.write_inventory()
        before = self._read(path)
        self.assertTrue(before)
        self._raw("features/bad.json", "{not json")
        with self.assertRaises(ValueError):
            atlas.write_inventory()
        self.assertEqual(self._read(path), before)
        r = self._cli("inventory")
        self.assertEqual(r.returncode, 1)
        self.assertTrue(r.stdout.startswith("error: "))
        self.assertEqual(self._read(path), before)

    def test_malformed_files_no_traceback(self):
        for text in ("{not json", "[1]", '{"features": [1]}'):
            self._raw("features/bad.json", text)
            probs = atlas.validate()
            self.assertTrue(any(p.startswith("unreadable file:") and "bad.json" in p for p in probs), (text, probs))
            for cmd in (["features-check"], ["features"], ["feature", "x"], ["inventory"]):
                r = self._cli(*cmd)
                self.assertNotIn("Traceback", r.stderr, (text, cmd))
            self.assertEqual(self._cli("features").returncode, 1)
            self.assertEqual(self._cli("features-check").returncode, 0)
        os.remove(os.path.join(config.ATLAS_DIR, "features", "bad.json"))
        for text in ("{oops", "[1]", '{"mechanics": []}', '{"mechanics": {"m": [[1]]}}'):
            self._raw("overlaps.json", text)
            r = self._cli("overlaps-apply")
            self.assertNotIn("Traceback", r.stderr, text)
            self.assertEqual(r.returncode, 1)
            self.assertTrue(r.stdout.startswith("error: "))

    def test_overlaps_all_or_nothing(self):
        self._raw("overlaps.json", json.dumps({"mechanics": {"m": ["examplemod.patrols", "othermod.raiders"]}}))
        self._raw("features/zzz.json", "{bad")
        snap = {n: self._read(os.path.join(config.ATLAS_DIR, "features", n)) for n in ("examplemod.json", "othermod.json")}
        with self.assertRaises(ValueError):
            atlas.apply_overlaps()
        for n, t in snap.items():
            self.assertEqual(self._read(os.path.join(config.ATLAS_DIR, "features", n)), t)

    def test_missing_folder_is_zero_records(self):
        config.ATLAS_DIR = os.path.join(self.tmp.name, "does-not-exist")
        self.assertEqual(atlas.validate(), [])
        self.assertEqual(atlas.load_all(), [])
        self.assertEqual(atlas.search("x"), [])
        out = subprocess.run([sys.executable, os.path.join(config.REPO, "wbsd", "wbsd.py"), "features-check"],
                             env=dict(os.environ, WB_ATLAS_DIR=config.ATLAS_DIR, PYTHONDONTWRITEBYTECODE="1"),
                             capture_output=True, text=True)
        self.assertEqual(out.stdout.strip(), "feature index OK (0 records)")
        self.assertEqual(out.returncode, 0)


if __name__ == "__main__":
    unittest.main()
