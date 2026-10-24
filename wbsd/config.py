"""Where things live. Everything here can be overridden with an environment variable.

  WB_MODULES_DIR   folder holding the Warband module folders (default: the first Steam Modules folder found, see default_modules_dirs)
  WB_REGISTRY      module registry JSON (default: <repo>/modules.json, else <repo>/modules.example.json)
  WB_ATLAS_DIR     feature atlas folder (default: <repo>/out/atlas)
  WB_CACHE_DIR     parse / index cache folder (default: <repo>/.cache)
"""
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_TAIL = ("steamapps", "common", "MountBlade Warband", "Modules")


def default_modules_dirs():
    """Where Steam usually puts the Modules folder, in the order they are tried."""
    dirs = [os.path.expanduser(os.path.join(
        "~/Library/Application Support/Steam", *_TAIL))]
    for var in ("ProgramFiles(x86)", "ProgramFiles"):
        base = os.environ.get(var)
        if base:
            dirs.append(os.path.join(base, "Steam", *_TAIL))
    dirs.append(os.path.expanduser(os.path.join("~/.steam/steam", *_TAIL)))
    dirs.append(os.path.expanduser(os.path.join("~/.local/share/Steam", *_TAIL)))
    return dirs


def _modules_dir():
    env = os.environ.get("WB_MODULES_DIR")
    if env:
        return env
    cands = default_modules_dirs()
    for d in cands:
        if os.path.isdir(d):
            return d
    return cands[0]


MODULES_DIR = _modules_dir()


def _registry_path():
    env = os.environ.get("WB_REGISTRY")
    if env:
        return env
    local = os.path.join(REPO, "modules.json")
    return local if os.path.isfile(local) else os.path.join(REPO, "modules.example.json")


REGISTRY = _registry_path()
CACHE_DIR = os.environ.get("WB_CACHE_DIR") or os.path.join(REPO, ".cache")
OUT_DIR = os.path.join(REPO, "out")
ATLAS_DIR = os.environ.get("WB_ATLAS_DIR") or os.path.join(OUT_DIR, "atlas")


def _main_slug():
    try:
        with open(REGISTRY, encoding="utf-8") as fh:
            mods = json.load(fh)["modules"]
        for e in mods:
            if e.get("role") == "main":
                return e["slug"]
    except IsADirectoryError:
        raise ValueError('%s: is a folder, not a module registry file' % REGISTRY)
    except OSError:
        return None          # no registry file: no main module
    except (ValueError, KeyError, TypeError, AttributeError) as e:
        raise ValueError('%s: not a valid module registry (expected {"modules": [ {"slug": ..., '
                         '"role": ...}, ... ]}): %s: %s' % (REGISTRY, type(e).__name__, e))
    return None


MAIN = _main_slug()
