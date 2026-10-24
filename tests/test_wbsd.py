#!/usr/bin/env python3
"""Self-checks for wbsd. Run: python3 -m unittest discover -s tests -v

These guard the toolkit's trust chain:
  1. the token-stream loader reads a module IDENTICALLY to wbasm (the
     byte-round-trip parser the migrations rely on);
  2. the fetched opcode reference agrees with every opcode wbops.py proved
     from the corpus with decoded citations;
  3. global-variable naming from variables.txt is right (a Native-source fact);
  4. the disassembler renders a known script the way Native's source reads.
"""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import _support  # noqa: E402
_support.require_tables()
import wbasm  # noqa: E402
import wbops  # noqa: E402
import gen_evidence  # noqa: E402
from wbsd import analyze, config, headers, opref, registry  # noqa: E402

MODULE = os.path.join(config.MODULES_DIR, os.environ.get("WB_TEST_MODULE", "Native"))
FAIL = []


def _slug():
    """Registry slug of the module under test (WB_TEST_MODULE)."""
    _support.require_module(MODULE)
    want = os.path.abspath(MODULE)
    for e in registry.entries():
        if os.path.abspath(registry.root_of(e)) == want:
            return e["slug"]
    raise unittest.SkipTest("module under test is not in the registry: %s" % MODULE)


def check(cond, label):
    if not cond:
        FAIL.append(label)


def test_loader_parity():
    m = registry.load(_slug())
    doc = wbasm.load_scripts(os.path.join(MODULE, "scripts.txt"))
    for i, sc in enumerate(doc.scripts):
        b = m.script_block(i)
        mine = [(c, f, list(o)) for c, f, o in b.stmts]
        theirs = [(s.opcode, s.flags, s.operands) for s in sc.statements()]
        check(mine == theirs, "script %d %s parses identically to wbasm" % (i, sc.name))
    tr = wbasm.load_simple_triggers(os.path.join(MODULE, "simple_triggers.txt"))
    for i, t in enumerate(tr.triggers):
        mine = [(c, f, list(o)) for c, f, o in m.block("strig:%d" % i).stmts]
        check(mine == [(s.opcode, s.flags, s.operands) for s in t.statements()], "simple trigger %d identical" % i)
    cv = wbasm.load_conversation(os.path.join(MODULE, "conversation.txt"))
    check(len(cv.dialogs) == sum(1 for b in m.blocks if b.kind == "dlg") // 2, "dialog count matches wbasm")
    mt = wbasm.load_mission_templates(os.path.join(MODULE, "mission_templates.txt"))
    check(len(mt.triggers) == sum(1 for b in m.blocks if b.kind == "mst") // 2, "mission-template trigger count matches wbasm")
    mn = wbasm.load_menus(os.path.join(MODULE, "menus.txt"))
    check(sum(len(x.options) for x in mn.menus) == sum(1 for b in m.blocks if b.kind == "mopt") // 2,
          "menu option count matches wbasm")


def test_duplicate_constants_agree():
    """wbasm/wbops/gen_evidence and wbsd (headers, opref) each define the same
    format constants, because the two parsers are kept independent so that
    test_loader_parity can cross-check them. Where a value is copied, it must
    be identical."""
    check(wbasm.OP_NEG == opref.NEG, "neg| flag: wbasm %#x vs opref %#x" % (wbasm.OP_NEG, opref.NEG))
    check(wbasm.OP_THIS_OR_NEXT == opref.THIS_OR_NEXT,
          "this_or_next| flag: wbasm %#x vs opref %#x" % (wbasm.OP_THIS_OR_NEXT, opref.THIS_OR_NEXT))
    check((wbasm.TRY_END, wbasm.TRY_BEGIN, wbasm.ELSE_TRY) == (opref.TRY_END, opref.TRY_BEGIN, opref.ELSE_TRY),
          "try_end/try_begin/else_try codes differ between wbasm and opref")
    check(wbops.CALL_SCRIPT == opref.CALL_SCRIPT, "call_script code differs between wbops and opref")
    for const, name in ((wbasm.TRY_FOR_RANGE, "try_for_range"),
                        (wbasm.TRY_FOR_RANGE_BACKWARDS, "try_for_range_backwards"),
                        (wbasm.TRY_FOR_PARTIES, "try_for_parties"),
                        (wbasm.TRY_FOR_AGENTS, "try_for_agents"),
                        (wbasm.TRY_FOR_PROP_INSTANCES, "try_for_prop_instances"),
                        (wbasm.TRY_FOR_PLAYERS, "try_for_players")):
        check(opref.OPS[const].name == name, "wbasm code %d is %s in the reference" % (const, opref.OPS[const].name))
    check(set(wbasm.BLOCK_OPENERS) == set(opref.BLOCK_OPENERS),
          "wbasm and opref block openers differ: %s" % sorted(set(wbasm.BLOCK_OPENERS) ^ set(opref.BLOCK_OPENERS)))
    # The multiplayer loops must balance against try_end (they did not before).
    for opener in (wbasm.TRY_FOR_PLAYERS, wbasm.TRY_FOR_PROP_INSTANCES):
        check(wbasm.block_depth_ok([wbasm.Statement(opener, [1]), wbasm.Statement(wbasm.TRY_END, [])]),
              "opcode %d ... try_end does not balance in wbasm.block_depth_ok" % opener)
    helpers = (("REG", "reg"), ("GVAR", "global"), ("STR", "string"), ("ITM", "item"), ("TRP", "troop"),
               ("PARTY", "party"), ("SCRIPT", "script"), ("V", "local"), ("SKL", "skill"), ("QSTR", "qstr"),
               ("FAC", "faction"), ("PT", "pt"), ("SCENE", "scene"), ("MENU", "menu"))
    kind_of = {}
    for helper, kind in helpers:
        mask = wbasm.opmask(getattr(wbops, helper)(0))
        kind_of[mask] = kind
        check(headers.TAGS.get(mask) == kind,
              "wbops.%s uses operand mask %d, but headers.TAGS[%d] is %r" % (helper, mask, mask, headers.TAGS.get(mask)))
    # gen_evidence's printed prefix must name the same kind as headers.TAGS for that mask
    kind_of_prefix = {"reg": "reg", "$g": "global", "str": "string", "itm": "item", "trp": "troop", "p": "party",
                      "script": "script", ":v": "local", "skl": "skill", "qstr": "qstr"}
    for mask, prefix in gen_evidence.MASK_PREFIX.items():
        check(mask in headers.TAGS, "gen_evidence mask %d (%s) is not in headers.TAGS" % (mask, prefix))
        check(prefix in kind_of_prefix, "gen_evidence prefix %r (mask %d) has no expected kind in this test" % (prefix, mask))
        check(headers.TAGS.get(mask) == kind_of_prefix.get(prefix),
              "gen_evidence mask %d prefix %r means %r but headers.TAGS[%d] is %r" % (
                  mask, prefix, kind_of_prefix.get(prefix), mask, headers.TAGS.get(mask)))


# wbops names whose corpus-proven opcode is the same engine op under another name.
WBOPS_ALIASES = {"TROOP_ADD_MERCHANDISE": "troop_add_item", "STORE_TROOP_FACTION": "store_troop_faction"}


def test_opref_agrees_with_wbops():
    for name, (code, arity) in wbops.EVIDENCE.items():
        op = opref.OPS.get(code)
        check(op is not None, "wbops %s=%d present in reference" % (name, code))
        if op is None:
            continue
        want = WBOPS_ALIASES.get(name, name.lower())
        check(op.name == want, "wbops %s=%d is named %s in reference (expected %s)" % (name, code, op.name, want))
        check(op.min_arity <= arity <= op.max_arity, "wbops %s arity %d within reference %d..%d"
              % (name, arity, op.min_arity, op.max_arity))


def test_global_names():
    m = registry.load(_slug())
    check(m.name("global", 401) == "g_encountered_party", "$g401 is g_encountered_party (Native source)")
    check(m.name("global", 914) == "g_encountered_party_2", "$g914 is g_encountered_party_2")


def test_named_disassembly():
    m = registry.load(_slug())
    text = "\n".join(analyze.disassemble(m, m.block("script:game_event_party_encounter")))
    check("(store_script_param_1, $g_encountered_party)" in text, "named param store rendered")
    check("(call_script, script_party_count_fit_regulars, p_main_party)" in text, "named call rendered")
    text = "\n".join(analyze.disassemble(m, m.block("script:party_remove_all_companions")))
    check("neq" in text or "neg|" in text, "negated comparison rendered")


def test_every_module_loads():
    """Loads the module under test; every registered module only with WB_TEST_ALL_MODULES=1."""
    slugs = registry.slugs() if os.environ.get("WB_TEST_ALL_MODULES") == "1" else [_slug()]
    for s in slugs:
        m = registry.load(s)
        check(not m.errors, "%s loads without table errors: %s" % (s, m.errors))
        check(len(m.names.get("script", [])) > 100, "%s has scripts" % s)


def main():
    for t in TESTS:
        t()
    if FAIL:
        print("FAILED: %d" % len(FAIL))
        for f in FAIL[:50]:
            print("  - " + f)
        return 1
    print("all green")
    return 0


def test_commands_set_matches_dispatch():
    """wbsd.py's _COMMANDS (the names that need the generated tables) must equal the command
    names its dispatch handles: a command added to one and not the other would skip the
    'run build_tables first' message or be rejected."""
    import ast
    import re
    path = os.path.join(ROOT, "wbsd", "wbsd.py")
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    declared = None
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == "_COMMANDS" for t in node.targets):
            declared = set(ast.literal_eval(node.value))
    check(declared is not None, "no _COMMANDS set found in wbsd.py")
    body = src[src.index("    cmd, args = argv[0], argv[1:]"):]
    handled = set(re.findall(r'cmd == "([^"]+)"', body))
    for group in re.findall(r'cmd in \(([^)]*)\)', body):
        handled |= set(re.findall(r'"([^"]+)"', group))
    check(declared == handled, "_COMMANDS differs from the dispatch: only in _COMMANDS %s, only in dispatch %s"
          % (sorted((declared or set()) - handled), sorted(handled - (declared or set()))))


TESTS = (test_loader_parity, test_opref_agrees_with_wbops, test_duplicate_constants_agree, test_global_names,
         test_named_disassembly, test_every_module_loads, test_commands_set_matches_dispatch)


class WbsdTests(unittest.TestCase):
    pass


_support.add_tests(WbsdTests, TESTS, FAIL)


if __name__ == "__main__":
    sys.exit(main())
