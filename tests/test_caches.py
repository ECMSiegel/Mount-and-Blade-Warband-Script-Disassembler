"""Cache correctness: the cached index equals a fresh one, any .txt change rebuilds every cache,
and the `similar` fast-path score equals analyze.jaccard.

Everything happens in temp folders: the Native .txt files are copied into a temp Modules folder,
the registry is a temp file with one entry, and the cache folder is a temp folder (config.CACHE_DIR,
the value of WB_CACHE_DIR).
"""
import glob
import json
import os
import shutil
import sys
import tempfile
import unittest
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _support  # noqa: E402
_support.require_tables()
from wbsd import analyze, config, corpus, queries, registry  # noqa: E402

SLUG = "cachetest"
SRC = os.path.join(config.MODULES_DIR, os.environ.get("WB_TEST_MODULE", "Native"))
_INDEX_ATTRS = ("callers", "global_use", "slot_use", "ref_use", "unknown_ops")
_XREF_ATTRS = ("calls", "refs", "slots", "globals", "unknown", "params", "returns", "opcodes", "strings")


def _index_data(ix):
    """Plain, comparable form of an index's cross-reference structures."""
    d = {a: dict(getattr(ix, a)) for a in _INDEX_ATTRS}
    d["x"] = {bid: tuple(getattr(x, a) for a in _XREF_ATTRS) for bid, x in ix.x.items()}
    return d


@unittest.skipUnless(os.path.isdir(SRC), "module folder not found: %s" % SRC)
class CacheTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        t = self.tmp.name
        self.root = os.path.join(t, "Modules", "Native")
        os.makedirs(self.root)
        for f in glob.glob(os.path.join(SRC, "*.txt")):
            shutil.copy2(f, self.root)
        self.reg = os.path.join(t, "modules.json")
        with open(self.reg, "w") as fh:
            json.dump({"modules": [{"slug": SLUG, "label": "Cache test", "path": "Native", "role": "native"}]}, fh)
        self.old = (config.MODULES_DIR, config.REGISTRY, config.CACHE_DIR)
        config.MODULES_DIR = os.path.join(t, "Modules")
        config.REGISTRY = self.reg
        config.CACHE_DIR = os.path.join(t, "cache")
        registry._LOADED.clear()
        queries._IX.clear()

    def tearDown(self):
        config.MODULES_DIR, config.REGISTRY, config.CACHE_DIR = self.old
        registry._LOADED.clear()
        queries._IX.clear()
        self.tmp.cleanup()

    def _paths(self):
        c = config.CACHE_DIR
        return {"parse": os.path.join(c, "parsed", SLUG + ".pickle"),
                "stats": os.path.join(c, "parsed", SLUG + ".stats.json"),
                "index": os.path.join(c, "index", SLUG + ".pickle")}

    def _build_all(self):
        registry._LOADED.clear()
        queries._IX.clear()
        queries.get(SLUG)            # parse cache + index cache
        registry.stats(SLUG)         # stats sidecar

    def test_cached_index_equals_fresh(self):
        mod = registry.load(SLUG)
        idx_dir = os.path.join(config.CACHE_DIR, "index")
        built = analyze.cached_index(mod, idx_dir)        # cold: builds and writes
        self.assertTrue(os.path.isfile(self._paths()["index"]))
        from_cache = analyze.cached_index(mod, idx_dir)   # warm: read back from the pickle
        fresh = analyze.ModuleIndex(mod)
        want = _index_data(fresh)
        self.assertTrue(want["x"] and want["callers"])
        self.assertEqual(_index_data(built), want)
        self.assertEqual(_index_data(from_cache), want)

    def test_touching_a_txt_rebuilds_all_caches(self):
        self._build_all()
        paths = self._paths()
        for k, p in paths.items():
            self.assertTrue(os.path.isfile(p), k)
        # backdate the cache files so "rewritten" is visible whatever the clock resolution
        old = 1_000_000_000
        for p in paths.values():
            os.utime(p, (old, old))
        # control: nothing changed, so a second run must not rewrite anything
        self._build_all()
        for k, p in paths.items():
            self.assertEqual(int(os.stat(p).st_mtime), old, "%s cache rewritten with no change" % k)
        # change a source file's mtime
        src = os.path.join(self.root, "scripts.txt")
        st = os.stat(src)
        os.utime(src, (st.st_atime, st.st_mtime + 10))
        self._build_all()
        for k, p in paths.items():
            self.assertGreater(int(os.stat(p).st_mtime), old, "%s cache not rebuilt after touching scripts.txt" % k)
        # change a source file's size (content)
        for p in paths.values():
            os.utime(p, (old, old))
        with open(src, "ab") as fh:
            fh.write(b"\n")
        self._build_all()
        for k, p in paths.items():
            self.assertGreater(int(os.stat(p).st_mtime), old, "%s cache not rebuilt after changing scripts.txt" % k)

    def test_editing_header_tables_rebuilds_all_caches(self):
        # work on a temp copy of the generated tables, never the real file
        fake = os.path.join(self.tmp.name, "header_tables.py")
        shutil.copy2(corpus.HEADER_TABLES, fake)
        corpus.HEADER_TABLES = fake
        try:
            self._build_all()
            paths = self._paths()
            old = 1_000_000_000
            for p in paths.values():
                os.utime(p, (old, old))
            self._build_all()
            for k, p in paths.items():
                self.assertEqual(int(os.stat(p).st_mtime), old, "%s cache rewritten with no change" % k)
            with open(fake, "a") as fh:
                fh.write("\n# edited\n")
            self._build_all()
            for k, p in paths.items():
                self.assertGreater(int(os.stat(p).st_mtime), old,
                                   "%s cache not rebuilt after editing header_tables.py" % k)
        finally:
            corpus.HEADER_TABLES = os.path.join(os.path.dirname(os.path.abspath(corpus.__file__)),
                                                "header_tables.py")

    def test_similar_fast_path_equals_jaccard(self):
        """queries.similar (the real path, with its fast arithmetic) prints the same
        'named' score as analyze.jaccard for every script it lists."""
        import re
        mod = registry.load(SLUG)
        by_owner = {b.owner: b for b in mod.blocks if b.kind == "script" and b.stmts}
        row = re.compile(r"^\s+named\s+(\d+)%\s+shape\s+\d+%\s+" + SLUG + r"\s+(\S+)\s+\d+ stmts$")
        checked = 0
        for base_name in ("game_start", "initialize_banner_info"):
            b0 = by_owner.get(base_name)
            self.assertIsNotNone(b0, base_name)
            base = analyze.named_set(mod, b0)
            lines = queries.similar(SLUG, base_name, top=10 ** 6, slugs=[SLUG], min_sim=0.0)
            self.assertTrue(lines[0].startswith("scripts most similar to %s:" % SLUG))
            self.assertGreater(len(lines), 10)
            for ln in lines[1:]:
                m = row.match(ln)
                self.assertIsNotNone(m, ln)
                want = 100 * analyze.jaccard(base, analyze.named_set(mod, by_owner[m.group(2)]))
                self.assertEqual(m.group(1), "%.0f" % want, "%s vs %s: printed %s%%, jaccard %.2f%%" % (
                    base_name, m.group(2), m.group(1), want))
                checked += int(m.group(1)) > 0
        self.assertGreaterEqual(checked, 3)

    def test_failed_cache_writes_leave_no_tmp_file(self):
        import pickle
        mod = registry.load(SLUG)
        shutil.rmtree(config.CACHE_DIR)
        real_dump = pickle.dump

        def boom(*a, **k):
            raise RuntimeError("disk full")
        # index cache write
        idx_dir = os.path.join(config.CACHE_DIR, "index")
        pickle.dump = boom
        try:
            with self.assertRaises(RuntimeError):
                analyze.cached_index(mod, idx_dir)
            # parse cache write (pickle)
            registry._LOADED.clear()
            with self.assertRaises(RuntimeError):
                corpus.load(SLUG, self.root, "x", cache_dir=os.path.join(config.CACHE_DIR, "parsed"))
        finally:
            pickle.dump = real_dump
        # stats write
        real_json_dump = json.dump
        json.dump = boom
        try:
            with self.assertRaises(RuntimeError):
                corpus._write_stats(os.path.join(config.CACHE_DIR, "parsed", "s.stats.json"), "fp", mod)
        finally:
            json.dump = real_json_dump
        left = [f for d, _, fs in os.walk(config.CACHE_DIR) for f in fs if f.endswith(".tmp")]
        self.assertEqual(left, [])
        # and a good write afterwards still works
        analyze.cached_index(mod, idx_dir)
        self.assertTrue(os.path.isfile(self._paths()["index"]))

    def test_fingerprint_uses_full_mtime_ns(self):
        a = corpus._fingerprint(self.root)
        src = os.path.join(self.root, "scripts.txt")
        st = os.stat(src)
        os.utime(src, ns=(st.st_atime_ns, st.st_mtime_ns + 1000))   # 1 microsecond: same int(mtime)
        self.assertNotEqual(corpus._fingerprint(self.root), a)


if __name__ == "__main__":
    unittest.main()
