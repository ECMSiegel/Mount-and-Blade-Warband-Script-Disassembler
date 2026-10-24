#!/usr/bin/env python3
"""Disassemble Warband bytecode into something readable.

Usage:
    python3 wbdis.py <script_name>
    python3 wbdis.py --trigger <index>
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wbasm
try:
    from wbsd import config
except ValueError as _e:  # a malformed modules.json: say which file, no traceback
    print("error: %s" % _e)
    sys.exit(1)

#: module folder to read; WB_MODULE names a folder inside WB_MODULES_DIR
MODULE = os.path.join(config.MODULES_DIR, os.environ.get("WB_MODULE", "Native"))

MASKS = {0: "", 1: "reg", 2: "$g", 3: "str", 4: "itm", 5: "trp",
         9: "p", 13: "script", 17: ":v", 19: "skl", 22: "qstr"}


def fmt_operand(o):
    mask, value = wbasm.opmask(o), wbasm.opval(o)
    if mask == 0:
        return str(value)
    return "%s%s" % (MASKS.get(mask, "m%d_" % mask), value)


def disassemble(statements, indent="  "):
    out, depth = [], 0
    for st in statements:
        if st.opcode == wbasm.TRY_END:
            depth = max(depth - 1, 0)
        prefix = "neg|" if st.flags & wbasm.OP_NEG else ""
        if st.flags & wbasm.OP_THIS_OR_NEXT:
            prefix = "this_or_next|" + prefix
        out.append("%s%s%d(%s)" % (indent * depth, prefix, st.opcode,
                                   ", ".join(fmt_operand(o) for o in st.operands)))
        if st.opcode in wbasm.BLOCK_OPENERS:
            depth += 1
    return out


def _missing(fname):
    """Clean error for a module folder that lacks the table (no traceback)."""
    path = os.path.join(MODULE, fname)
    if os.path.isfile(path):
        return None
    print("error: %s not found; set WB_MODULES_DIR (and WB_MODULE) to a module folder" % path)
    return 1


def main(argv):
    if len(argv) >= 3 and argv[1] == "--trigger":
        if _missing("simple_triggers.txt"):
            return 1
        doc = wbasm.load_simple_triggers(os.path.join(MODULE, "simple_triggers.txt"))
        if not re.fullmatch(r"-?\d+", argv[2]):
            print("no such trigger: %s" % argv[2])
            return 1
        idx = int(argv[2])
        if idx < 0 or idx >= len(doc.triggers):
            print("no such trigger: %s" % argv[2])
            return 1
        trg = doc.triggers[idx]
        print("=== simple_trigger %s (interval %s) ===" % (argv[2], trg.interval))
        print("\n".join(disassemble(trg.statements())))
        return 0
    if len(argv) >= 2 and argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(argv) < 2:
        print(__doc__)
        return 2
    if _missing("scripts.txt"):
        return 1
    doc = wbasm.load_scripts(os.path.join(MODULE, "scripts.txt"))
    scr = doc.by_name(argv[1])
    if scr is None:
        print("no such script: %s" % argv[1])
        return 1
    print("=== %s (index %d) ===" % (scr.name, doc.index_of(scr.name)))
    print("\n".join(disassemble(scr.statements())))
    return 0


def cli():
    """Console-script entry point (see pyproject.toml)."""
    sys.exit(main(sys.argv))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
