"""Module registry: where each registered module lives and how to load it."""
import json
import os

from . import config, corpus


def entries():
    with open(config.REGISTRY) as fh:
        return json.load(fh)["modules"]


def entry(slug):
    for e in entries():
        if e["slug"] == slug:
            return e
    raise KeyError("unknown module slug %r (see %s)" % (slug, config.REGISTRY))


def root_of(e):
    p = e["path"]
    if p.startswith("cache:"):
        return os.path.join(config.CACHE_DIR, "archives", p[len("cache:"):])
    return os.path.join(config.MODULES_DIR, p)


def slugs(role=None):
    """Registered slugs whose module folder exists (a module folder that
    was removed is skipped, not fatal; `wbsd.py modules` lists it as MISSING)."""
    return [e["slug"] for e in entries()
            if (role is None or e["role"] == role) and os.path.isdir(root_of(e))]


_LOADED = {}


def load(slug):
    if slug not in _LOADED:
        e = entry(slug)
        _LOADED[slug] = corpus.load(slug, root_of(e), e["label"],
                                    cache_dir=os.path.join(config.CACHE_DIR, "parsed"))
    return _LOADED[slug]


def stats(slug):
    """(scripts, blocks, statements, errors) of a module without unpickling it."""
    e = entry(slug)
    return corpus.stats(slug, root_of(e), e["label"], cache_dir=os.path.join(config.CACHE_DIR, "parsed"))
