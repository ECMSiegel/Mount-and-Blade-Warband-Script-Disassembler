"""Build wbsd's opcode and operand tables from YOUR OWN Module System headers.

    python3 wbsd/build_tables.py <Module System folder>
    python3 wbsd/build_tables.py --download

With --download the three header files are fetched from the TLD mod's public
GitHub repo (pinned to one commit, see HEADERS_SHA) instead of read from a folder.

The folder is the one that holds header_operations*.py, header_common.py and
header_triggers*.py (the Python Module System that ships with Warband, or a
mod's own copy). The headers are only READ AS TEXT -- nothing in them is
imported or run. Two files are written next to this script:

    opref_data.py     opcode names + argument signatures (RAW, CAN_FAIL, ...)
    header_tables.py  operand tags, trigger event codes, key codes

Both are generated, git-ignored, and never published: the headers are
TaleWorlds' work, so only this generator and table_overlay.py (the author's own
corrections) ship with the toolkit.
"""
import ast
import difflib
import glob
import os
import re
import shutil
import sys
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
if __package__ in (None, ""):
    sys.path.insert(0, HERE)
    import table_overlay
else:
    from . import table_overlay

# --download source: the TLD mod (github.com/tldmod/tldmod) publishes TaleWorlds'
# Module System headers openly. Pinned to one commit so the tables are reproducible.
HEADERS_SHA = "561ceaf04e12ec1fba19cf39aad07a2981f14910"
HEADERS_BASE = ("https://raw.githubusercontent.com/tldmod/tldmod/%s/ModuleSystem/Header/"
                % HEADERS_SHA)
HEADER_FILES = ("header_operations_wb.py", "header_common.py", "header_triggers_wb.py")
HEADER_URLS = tuple(HEADERS_BASE + n for n in HEADER_FILES)
DOWNLOAD_TIMEOUT = 30

_DEF = re.compile(r"^([A-Za-z_]\w*)\s*=\s*(-?(?:0[xX][0-9a-fA-F]+|\d+(?:\.\d*)?))\s*(?:#(.*))?$")

# Operand tag names in header_common.py -> the table kind wbsd uses for them.
TAG_KINDS = {
    "tag_register": "reg", "tag_variable": "global", "tag_string": "string",
    "tag_item": "item", "tag_troop": "troop", "tag_faction": "faction",
    "tag_quest": "quest", "tag_party_tpl": "pt", "tag_party": "party",
    "tag_scene": "scene", "tag_mission_tpl": "mt", "tag_menu": "menu",
    "tag_script": "script", "tag_particle_sys": "psys", "tag_scene_prop": "spr",
    "tag_sound": "sound", "tag_local_variable": "local", "tag_map_icon": "icon",
    "tag_skill": "skill", "tag_mesh": "mesh", "tag_presentation": "prsnt",
    "tag_quick_string": "qstr", "tag_track": "track", "tag_tableau": "tableau",
    "tag_animation": "anim",
}
# header_operations lists the generator copies into opref_data.
OP_LISTS = (("can_fail_operations", "CAN_FAIL"), ("depth_operations", "DEPTH"),
            ("global_lhs_operations", "GLOBAL_LHS"))


class TableError(Exception):
    pass


def _read(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read().splitlines()


def _numdefs(lines):
    out = []
    for i, line in enumerate(lines):
        m = _DEF.match(line)
        if m:
            out.append((i, m.group(1), ast.literal_eval(m.group(2)), m.group(3) or ""))
    return out


def _best(folder, pattern):
    """Of the files matching `pattern`, the one with the most numeric definitions
    (a header may be a small stub that just imports a _wb / _mb variant)."""
    best, best_n = None, 0
    for path in sorted(glob.glob(os.path.join(folder, pattern))):
        n = len(_numdefs(_read(path)))
        if n > best_n:
            best, best_n = path, n
    if best is None:
        raise TableError("no %s with definitions found in %s" % (pattern, folder))
    return best


# ---------------------------------------------------------------- signatures
def _split_args(text):
    """'a, [b], <c>' -> ['a', ...] split on top-level commas only."""
    out, depth, cur = [], 0, ""
    for ch in text:
        if ch in "[<(":
            depth += 1
        elif ch in "]>)":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [a.strip() for a in out if a.strip()]


def _canon(a, opname):
    """One header argument -> (is_optional, canonical name)."""
    a = a.strip()
    opt = a.startswith("[")
    a = re.sub(r"[\[\]<>]", "", a).strip().split("#")[0].strip()
    a = re.split(r"[-_]in[-_]\d", a)[0]
    a = re.sub(r"[\s\-/]+", "_", a)
    a = re.sub(r"_?\(.*\)$", "", a)
    a = re.sub(r"^(destination)_\w+$", r"\1", a)
    a = re.sub(r"^(value_[xyz])_fixed_point$", r"\1", a)
    a = re.sub(r"_times_1000$", "", a)
    a = re.sub(r"_1$", "", a)
    a = table_overlay.ARG_ALIASES.get(a, a)
    if opname.startswith(("prop_instance_", "scene_prop_")) and a == "scene_prop_id":
        a = "prop_instance_id"
    return opt, a


def _norm_args(args, opname):
    seen, out = {}, []
    for a in args:
        opt, name = _canon(a, opname)
        seen[name] = seen.get(name, 0) + 1
        if seen[name] > 1:
            name = "%s_%d" % (name, seen[name])
        out.append(("[%s]" if opt else "<%s>") % name)
    return out


def _signature(comment_lines, names):
    """Arguments of the first '(name, args...)' in the comment text, or None."""
    text = " ".join(comment_lines)
    for m in re.finditer(r"\(\s*(\w+)\s*([,)])", text):
        if m.group(1) not in names and not any(
                difflib.SequenceMatcher(None, m.group(1), n).ratio() >= 0.8
                for n in names):
            continue
        if m.group(2) == ")":
            return []
        depth, j = 1, m.end()
        while j < len(text) and depth:
            depth += {"(": 1, ")": -1}.get(text[j], 0)
            j += 1
        return _split_args(text[m.end():j - 1])
    return None


def parse_operations(lines):
    """Opcode table from header_operations text: {code: (name, [args])}."""
    defs = _numdefs(lines)
    by_code = {}
    for i, name, code, comment in defs:
        if isinstance(code, int) and 0 <= code < 0x10000:
            by_code.setdefault(code, []).append((i, name, comment))
    ops = {}
    for code, group in by_code.items():
        sigs = []
        for i, name, comment in group:
            text = [comment]
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith("#"):
                text.append(lines[j].lstrip()[1:])
                j += 1
            sigs.append((name, _signature(text, [g[1] for g in group])))
        # Prefer the alias whose own signature names it (the others are
        # deprecated spellings); else the last one listed.
        pick = None
        for name, sg in sigs:
            if sg is not None and _signature_names(lines, group, name):
                pick = (name, sg)
        if pick is None:
            pick = sigs[-1]
        ops[code] = (pick[0], _norm_args(pick[1] or [], pick[0]))
    return ops


def _signature_names(lines, group, name):
    for i, n, comment in group:
        if n == name:
            text = [comment]
            j = i + 1
            while j < len(lines) and lines[j].lstrip().startswith("#"):
                text.append(lines[j].lstrip()[1:])
                j += 1
            m = re.search(r"\(\s*(\w+)\s*[,)]", " ".join(text))
            return bool(m) and _signature(text, [name]) is not None
    return False


def parse_name_list(lines, var):
    """Members of `var = [a, b, c]` in header_operations text."""
    for i, line in enumerate(lines):
        if re.match(r"^%s\s*=\s*\[" % var, line):
            body, j = line.split("[", 1)[1], i
            while "]" not in body and j + 1 < len(lines):
                j += 1
                body += " " + lines[j]
            body = body.split("]", 1)[0]
            body = re.sub(r"#[^\n]*", "", body)
            return [n.strip() for n in body.split(",") if n.strip()]
    raise TableError("%s not found in header_operations" % var)


def make_raw(ops):
    out = []
    for code in sorted(ops):
        name, args = ops[code]
        out.append(("%d %s %s" % (code, name, ",".join(args))).rstrip())
    return "\n".join(out)


def wrap_names(names, width=79):
    lines, cur = [], ""
    for n in names:
        if cur and len(cur) + 1 + len(n) > width:
            lines.append(cur)
            cur = n
        else:
            cur = (cur + " " + n) if cur else n
    lines.append(cur)
    return "\n".join(lines)


# ------------------------------------------------------------ header tables
def parse_tags(lines):
    vals = {n: v for _, n, v, _ in _numdefs(lines)}
    tags = {}
    for name, kind in TAG_KINDS.items():
        if name in vals:
            tags[vals[name]] = kind
    return tags


def parse_triggers(lines):
    ev = {}
    for _, n, v, _ in _numdefs(lines):
        if n.startswith("ti_") and n not in table_overlay.TRIGGER_SKIP:
            ev.setdefault(float(v), n)
    return ev


def parse_keys(lines):
    return {v: n for _, n, v, _ in _numdefs(lines)
            if n.startswith("key_") and isinstance(v, int)}


# -------------------------------------------------------------------- build
def build(folder):
    """Return (opref_data_source, header_tables_source, summary)."""
    ops_path = _best(folder, "header_operations*.py")
    common_path = _best(folder, "header_common*.py")
    trig_path = _best(folder, "header_triggers*.py")
    oplines = _read(ops_path)
    ops = parse_operations(oplines)
    table_overlay.apply_ops(ops)
    known = {d[1] for d in _numdefs(oplines) if 0 <= d[2] < 0x10000}
    lists, notes = {}, []
    for var, out in OP_LISTS:
        try:
            lists[out] = [n for n in parse_name_list(oplines, var) if n in known]
        except TableError:
            # some Module System copies do not carry this list
            lists[out] = list(table_overlay.LIST_DEFAULTS.get(out, []))
            notes.append("%s missing in %s, used %s" % (
                var, os.path.basename(ops_path),
                "the built-in default" if lists[out] else "an empty list"))
    tlines = _read(trig_path)
    tags = parse_tags(_read(common_path))
    events = parse_triggers(tlines)
    keys = parse_keys(tlines)
    table_overlay.apply_tables(tags, events, keys)

    opdata = ['"""GENERATED by wbsd/build_tables.py from your own Module System'
              ' headers.\nDo not edit or publish: re-run the generator instead.'
              '\n"""\n\nRAW = r"""\n' + make_raw(ops) + '\n"""\n']
    for _, out in OP_LISTS:
        opdata.append('\n%s = """%s""".split()\n' % (out, wrap_names(lists[out])))
    tables = ('"""GENERATED by wbsd/build_tables.py from your own Module System'
              ' headers.\nDo not edit or publish: re-run the generator instead.'
              '\n"""\n\n'
              "TAGS = %r\n\nTRIGGER_EVENTS = %r\n\nKEYS = %r\n"
              % (tags, events, keys))
    summary = "%d opcodes, %d tags, %d trigger events, %d keys (from %s, %s, %s)" % (
        len(ops), len(tags), len(events), len(keys),
        os.path.basename(ops_path), os.path.basename(common_path),
        os.path.basename(trig_path))
    if notes:
        summary += "\nnote: " + "; ".join(notes)
    return "".join(opdata), tables, summary


def download_headers(dest):
    """Fetch the pinned header files into `dest` (saved as text, never run)."""
    for url in HEADER_URLS:
        with urllib.request.urlopen(url, timeout=DOWNLOAD_TIMEOUT) as resp:
            data = resp.read()
        with open(os.path.join(dest, url.rsplit("/", 1)[1]), "wb") as fh:
            fh.write(data)


def main(argv):
    if len(argv) == 2 and argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 2
    tmpdir = None
    if argv[1] == "--download":
        tmpdir = tempfile.mkdtemp(prefix="wb_headers_")
        try:
            download_headers(tmpdir)
        except Exception as e:  # URLError, HTTPError, timeout, OSError, ...
            shutil.rmtree(tmpdir, ignore_errors=True)
            reason = getattr(e, "reason", None) or e
            print("error: could not download the Module System headers (%s); "
                  "download them yourself or pass a Module System folder" % reason)
            return 1
        folder = tmpdir
    else:
        folder = os.path.abspath(os.path.expanduser(argv[1]))
        if not os.path.isdir(folder):
            print("not a folder: %s" % folder)
            return 2
    try:
        try:
            opdata, tables, summary = build(folder)
        finally:
            if tmpdir:
                shutil.rmtree(tmpdir, ignore_errors=True)
    except TableError as e:
        print("build_tables: %s" % e)
        return 1
    except OSError as e:
        print("error: %s" % e)
        return 1
    tmps = []
    backups = []  # (dest, old bytes or None) for each file already replaced
    try:
        for name, text in (("opref_data.py", opdata), ("header_tables.py", tables)):
            tmp = os.path.join(HERE, name + ".tmp")
            tmps.append((tmp, os.path.join(HERE, name)))
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(text)
        for tmp, dest in tmps:
            try:
                with open(dest, "rb") as fh:
                    old = fh.read()
            except FileNotFoundError:
                old = None
            os.replace(tmp, dest)
            backups.append((dest, old))
    except BaseException as e:  # KeyboardInterrupt too: no half-replaced pair, no stray .tmp files
        for tmp, _dest in tmps:
            try:
                os.remove(tmp)
            except OSError:
                pass
        for dest, old in backups:
            try:
                if old is None:
                    os.remove(dest)
                else:
                    with open(dest, "wb") as fh:
                        fh.write(old)
            except OSError:
                pass
        if not isinstance(e, OSError):
            raise
        print("error: %s" % e)
        return 1
    print("wrote opref_data.py and header_tables.py: " + summary)
    return 0


def cli():
    """Console-script entry point (see pyproject.toml)."""
    sys.exit(main(sys.argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
