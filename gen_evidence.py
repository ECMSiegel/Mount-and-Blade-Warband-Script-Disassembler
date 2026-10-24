#!/usr/bin/env python3
"""Generate evidence comments for wbops.py from a module's shipped corpus.

wbops.py's HARD RULE is that an opcode may only be named there alongside a
DECODED IN-CORPUS EXAMPLE. A hand-typed example defeats the rule silently: the
number can be wrong and the comment still looks like proof. So the examples are
not typed at all -- this tool searches scripts.txt and simple_triggers.txt,
decodes a real statement, and prints the comment text verbatim for pasting.

Usage:
    python3 gen_evidence.py            # regenerate every wbops EVIDENCE entry
    python3 gen_evidence.py 520 3      # one opcode, given arity
    python3 gen_evidence.py 2105       # one opcode, any arity

The module searched is WB_MODULE (a folder name under the modules folder;
default Native).

Operand rendering matches wbasm's operand model (opmask << 56 | value):
    1 reg   2 $g   3 str   4 itm   5 trp   9 p   13 script   17 :v   19 skl
    22 qstr;  bare constants print as plain integers.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wbasm
try:
    from wbsd import config
except ValueError as _e:  # a malformed modules.json: say which file, no traceback
    print("error: %s" % _e)
    sys.exit(1)

MODULE = os.path.join(config.MODULES_DIR, os.environ.get("WB_MODULE", "Native"))

#: operand type mask -> textual prefix. Masks are those wbasm documents from
#: decoded shipped bytecode; anything else renders as "m<mask>:" so an unknown
#: mask is visible rather than silently mislabelled.
MASK_PREFIX = {
    1: "reg",
    2: "$g",
    3: "str",
    4: "itm",
    5: "trp",
    9: "p",
    13: "script",
    17: ":v",
    19: "skl",
    22: "qstr",
}


def render_operand(operand):
    mask = wbasm.opmask(operand)
    value = wbasm.opval(operand)
    if mask == 0:
        return str(value)
    return "%s%d" % (MASK_PREFIX.get(mask, "m%d:" % mask), value)


def render_statement(st):
    """Render a Statement the way an evidence comment cites it."""
    prefix = ""
    if st.flags & wbasm.OP_NEG:
        prefix += "neg|"
    if st.flags & wbasm.OP_THIS_OR_NEXT:
        prefix += "this_or_next|"
    return "%s%d(%s)" % (prefix, st.opcode,
                         ", ".join(render_operand(o) for o in st.operands))


def corpus(module=MODULE):
    """Yield (source_label, [Statement, ...]) for every shipped block.

    scripts.txt first, then simple_triggers.txt, so evidence prefers the named
    scripts that are easier for a human to go and re-check by hand.
    """
    doc = wbasm.load_scripts(os.path.join(module, "scripts.txt"))
    for scr in doc.scripts:
        yield scr.name, scr.statements()
    trg_doc = wbasm.load_simple_triggers(os.path.join(module, "simple_triggers.txt"))
    for i, trg in enumerate(trg_doc.triggers):
        yield "simple_trigger %d" % i, trg.statements()


def find(opcode, arity=None, blocks=None):
    """Return (source_label, rendered_text) for a real occurrence, or None.

    Unflagged statements win over flagged ones so the citation reads as the
    plain form of the opcode; both are equally real.
    """
    fallback = None
    for label, stmts in (blocks if blocks is not None else corpus()):
        for st in stmts:
            if st.opcode != opcode:
                continue
            if arity is not None and len(st.operands) != arity:
                continue
            if st.flags == 0:
                return label, render_statement(st)
            if fallback is None:
                fallback = (label, render_statement(st))
    return fallback


def comment(opcode, arity=None, blocks=None):
    """The evidence comment body for an opcode, or None if it is not shipped."""
    hit = find(opcode, arity, blocks)
    if hit is None:
        return None
    return "%s: %s" % hit


def main(argv):
    if len(argv) > 1:
        try:
            opcode = int(argv[1])
            arity = int(argv[2]) if len(argv) > 2 else None
        except ValueError:
            print("error: opcode and arity must be whole numbers (got %s)" % " ".join(argv[1:3]))
            return 1
        body = comment(opcode, arity)
        if body is None:
            print("NO IN-CORPUS EXAMPLE for opcode %d arity %s" % (opcode, arity))
            return 1
        print("# " + body)
        return 0

    # Whole-table mode: cache the corpus once, then emit one line per entry.
    import wbops
    blocks = list(corpus())
    missing = 0
    for name, (opcode, arity) in wbops.EVIDENCE.items():
        body = comment(opcode, arity, blocks)
        if body is None:
            print("%-30s NO IN-CORPUS EXAMPLE (op %d, arity %d)" % (name, opcode, arity))
            missing += 1
        else:
            print("%-30s # %s" % (name, body))
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
