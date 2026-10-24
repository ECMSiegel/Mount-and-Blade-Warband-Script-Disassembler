#!/usr/bin/env python3
"""Acceptance tests for wbasm.

The point of these tests is the round-trip: parse every statement block the
module ships, re-emit it, and require the token stream back byte-for-byte. That
check runs purely on numbers, so it needs no opcode-name table to be meaningful
-- if the statement model gets flags, operand counts or block nesting wrong
anywhere in the shipped corpus, it fails here rather than in a save file.

Run:  python3 -m unittest discover -s tests -v
"""
import os
import pathlib
import re
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import wbasm
from wbsd import config
import _support

MODULE = os.path.join(config.MODULES_DIR, os.environ.get("WB_TEST_MODULE", "Native"))

FAILURES = []
CHECKS = [0]


def check(cond, label):
    CHECKS[0] += 1
    if not cond:
        FAILURES.append(label)


def test_operand_encoding():
    """Decode the operands whose meaning was proven from shipped bytecode."""
    # a call_script operand: script index 585
    check(wbasm.opmask(936748722493063753) == 13, "script opmask")
    check(wbasm.opval(936748722493063753) == 585, "script index 585")
    # troop operands: index 270 and index 346
    check(wbasm.opval(360287970189639950) == 270, "troop 270")
    check(wbasm.opval(360287970189640026) == 346, "troop 346")
    # troop_raise_skill(player, skill 15, 1)
    check(wbasm.opmask(1369094286720630799) == 19, "skill opmask")
    check(wbasm.opval(1369094286720630799) == 15, "skill 15")
    check(wbasm.opval(360287970189639680) == 0, "troop 0 = trp_player")
    # local variables and registers
    check(wbasm.opmask(1224979098644774912) == 17, "local var opmask")
    check(wbasm.opval(1224979098644774913) == 1, "local var 1")
    check(wbasm.opmask(72057594037927936) == 1, "register opmask")
    # round-trip the encoder against every constant above
    for v in (936748722493063753, 360287970189639950, 1369094286720630799,
              1224979098644774912, 72057594037927936, 288230376151711825):
        check(wbasm.enc(wbasm.opmask(v), wbasm.opval(v)) == v, "enc/dec %d" % v)
    # bare negative constants must survive untouched
    check(wbasm.opmask(-1) == 0 and wbasm.opval(-1) == -1, "-1 stays plain")


def test_opcode_flags():
    """Flags live in the opcode's high bits; both were seen in real statements."""
    op, flags = wbasm.split_opcode(2147483679)
    check(op == 31 and flags == wbasm.OP_NEG, "neg| flag")
    op, flags = wbasm.split_opcode(1073741977)
    check(op == 153 and flags == wbasm.OP_THIS_OR_NEXT, "this_or_next| flag")
    op, flags = wbasm.split_opcode(3221225503)
    check(op == 31 and flags == (wbasm.OP_NEG | wbasm.OP_THIS_OR_NEXT), "both flags")
    op, flags = wbasm.split_opcode(1521)
    check(op == 1521 and flags == 0, "no flags")
    for raw in (2147483679, 1073741977, 3221225503, 1521):
        check(wbasm.join_opcode(*wbasm.split_opcode(raw)) == raw, "opcode rt %d" % raw)


def _roundtrip_block(tokens, label, declared_count):
    """Parse -> emit must reproduce the token list exactly, and the declared
    statement count must match what the parser actually found."""
    try:
        stmts = wbasm.parse_statements(tokens)
    except Exception as exc:  # noqa: BLE001 - surfaced as a test failure
        FAILURES.append("%s: parse raised %s" % (label, exc))
        CHECKS[0] += 1
        return None
    CHECKS[0] += 1
    if wbasm.emit_statements(stmts) != tokens:
        FAILURES.append("%s: token stream changed" % label)
    CHECKS[0] += 1
    if declared_count is not None and len(stmts) != declared_count:
        FAILURES.append("%s: declared %s statements, parsed %d"
                        % (label, declared_count, len(stmts)))
    return stmts


#: Blocks that are known not to balance, as {label: final depth}. The Module
#: System never validated nesting, so an omitted try_end compiles happily and
#: the engine tolerates it. Native's blocks all balance with the opener set
#: {4,6,7,11,12}, which is what confirms the set. A module with such a defect
#: registers its blocks here from its own local-only modspecific test file.
KNOWN_UNBALANCED = {}


def _check_nesting(stmts, label):
    """try_begin/try_end must balance -- proves the block model, since Warband
    bytecode carries no jump offsets and nesting is purely structural."""
    depth = 0
    for st in stmts:
        if st.opcode in wbasm.BLOCK_OPENERS:
            depth += 1
        elif st.opcode == wbasm.TRY_END:
            depth -= 1
            if depth < 0:
                break
    CHECKS[0] += 1
    if depth != KNOWN_UNBALANCED.get(label, 0):
        FAILURES.append("%s: unbalanced try depth %d" % (label, depth))


def test_simple_triggers_roundtrip():
    path = os.path.join(MODULE, "simple_triggers.txt")
    doc = wbasm.load_simple_triggers(path)
    check(len(doc.triggers) == doc.declared_count,
          "triggers: header says %d, found %d" % (doc.declared_count, len(doc.triggers)))
    for i, trg in enumerate(doc.triggers):
        stmts = _roundtrip_block(trg.tokens, "simple_trigger %d" % i, trg.declared_count)
        if stmts:
            _check_nesting(stmts, "simple_trigger %d" % i)


def test_menus_roundtrip():
    path = os.path.join(MODULE, "menus.txt")
    doc = wbasm.load_menus(path)
    check(len(doc.menus) == doc.declared_count,
          "menus: header says %d, found %d" % (doc.declared_count, len(doc.menus)))
    for menu in doc.menus:
        stmts = _roundtrip_block(menu.stmt_tokens, "menu %s" % menu.name,
                                  menu.declared_stmt_count)
        if stmts:
            _check_nesting(stmts, "menu %s" % menu.name)

        opts = menu.options
        CHECKS[0] += 1
        if len(opts) != menu.declared_option_count:
            FAILURES.append(
                "menu %s: option_count declared %d, parsed %d"
                % (menu.name, menu.declared_option_count, len(opts)))

        # Full options-line reconstruction: proves parse_options/emit_options
        # get field order and boundaries right, not just the statement
        # sub-blocks nested inside each option. Without this, a bug in
        # MenuOption.tokens() field ordering would go undetected (the
        # sub-block checks below would still individually pass, and
        # test_file_bytes_preserved never touches parsed MenuOption objects
        # at all, since MenuOptionsLine.serialize() returns raw bytes
        # verbatim unless dirty). Covers all 290 menus including the 15
        # zero-option ones (empty token list on both sides).
        CHECKS[0] += 1
        if wbasm.emit_options(opts) != menu.option_tokens:
            FAILURES.append(
                "menu %s: options-line token stream changed on re-emit" % menu.name)

        for opt in opts:
            label_c = "menu %s option %s conditions" % (menu.name, opt.name)
            label_q = "menu %s option %s consequences" % (menu.name, opt.name)
            cstmts = _roundtrip_block(opt.cond_tokens, label_c, opt.cond_count)
            if cstmts:
                _check_nesting(cstmts, label_c)
            qstmts = _roundtrip_block(opt.conseq_tokens, label_q, opt.conseq_count)
            if qstmts:
                _check_nesting(qstmts, label_q)


def test_file_bytes_preserved():
    """Loading and re-serialising an untouched file must give back the exact
    original bytes, mixed CRLF/LF endings and all."""
    for name, loader in (("scripts.txt", wbasm.load_scripts),
                         ("simple_triggers.txt", wbasm.load_simple_triggers),
                         ("menus.txt", wbasm.load_menus),
                         ("triggers.txt", wbasm.load_triggers),
                         ("tableau_materials.txt", wbasm.load_tableau_materials),
                         ("conversation.txt", wbasm.load_conversation),
                         ("mission_templates.txt", wbasm.load_mission_templates)):
        path = os.path.join(MODULE, name)
        with open(path, "rb") as fh:
            original = fh.read()
        doc = loader(path)
        check(doc.serialize() == original, "%s: byte-identical re-serialise" % name)


def test_append_and_remove_script():
    """Appending a script must land at the end, bump the count, and be
    removable without disturbing any existing script."""
    path = os.path.join(MODULE, "scripts.txt")
    doc = wbasm.load_scripts(path)
    before_count = len(doc.scripts)
    before_bytes = doc.serialize()

    stmts = [wbasm.Statement(4, []), wbasm.Statement(31, [1, 1]), wbasm.Statement(3, [])]
    idx = doc.append_script("rg_test_scratch", stmts)
    check(idx == before_count, "append returns the new index")
    check(len(doc.scripts) == before_count + 1, "script count grew by one")
    check(doc.scripts[-1].name == "rg_test_scratch", "appended script is last")
    check(doc.by_name("rg_test_scratch").statements()[1].opcode == 31,
          "appended statements survive a re-parse")

    header_count = int(doc.serialize().splitlines()[1].split()[0])
    check(header_count == before_count + 1, "header count rewritten")

    check(doc.remove_trailing_script("rg_test_scratch") is True, "removal reports success")
    check(doc.serialize() == before_bytes, "remove restores the original bytes exactly")


def test_remove_trailing_script_refuses_non_final():
    """Removing a non-final script would silently repoint every later
    call_script index, so it must be refused outright."""
    doc = wbasm.load_scripts(os.path.join(MODULE, "scripts.txt"))
    name = doc.scripts[10].name
    raised = False
    try:
        doc.remove_trailing_script(name)
    except ValueError:
        raised = True
    check(raised, "refuses to remove a non-final script")


def test_append_trigger():
    path = os.path.join(MODULE, "simple_triggers.txt")
    doc = wbasm.load_simple_triggers(path)
    before = doc.serialize()
    n = len(doc.triggers)
    doc.append_trigger("24.000000", [wbasm.Statement(1, [wbasm.enc(13, 999)])])
    check(len(doc.triggers) == n + 1, "trigger count grew")
    check(int(doc.serialize().splitlines()[1].split()[0]) == n + 1, "trigger header bumped")
    check(doc.triggers[-1].statements()[0].opcode == 1, "trigger body re-parses")
    check(doc.remove_triggers_calling(999) == 1, "removed our trigger")
    check(doc.serialize() == before, "remove restores original bytes")


def test_menu_option_edits_persist():
    """A menu option's condition/consequence edits must survive a save.

    MenuOption.set_conditions / set_consequences mutate the OPTION, which has no
    back-reference to its MenuOptionsLine and so could never set that line's
    `dirty` flag. serialize() trusted the flag, returned the pristine bytes, and
    a menu edit reported success while writing nothing. Menus therefore had to
    be edited by raw token surgery.

    Both halves matter: the edit must persist, AND an untouched document must
    still serialise byte-identically (test_menus_roundtrip covers that on the
    real file; here we re-check it on the copy we are about to mutate).

    THE COPY LIVES IN A TEMPORARY DIRECTORY, NOT BESIDE THE TABLES. It used to
    be written as `<module>/menus.txt.test_option_edit`: two gate runs at once
    raced on one path, and a crash left a full copy of `menus.txt` stranded
    beside the compiled tables, where `.gitignore:15` (`*.bak_*`) does not
    match it. Nothing here needs the copy to sit next to the real file -- the
    loaders take a path.
    """
    src = os.path.join(MODULE, "menus.txt")
    work = tempfile.mkdtemp(prefix="wbasm_menu_option_edit_")
    tmp = os.path.join(work, "menus.txt")
    shutil.copyfile(src, tmp)
    try:
        doc = wbasm.load_menus(tmp)
        check(doc.serialize() == pathlib.Path(src).read_bytes(),
              "menus.txt copy round-trip not byte-identical before mutation")

        target = next(m for m in doc.menus if m.options)
        option = target.options[0]
        n_cond = len(option.conditions())
        n_conseq = len(option.consequences())
        marker = wbasm.enc(6, 35)
        option.set_conditions(option.conditions()
                              + [wbasm.Statement(31, [wbasm.enc(17, 99), marker])])
        option.set_consequences(option.consequences()
                                + [wbasm.Statement(2133, [wbasm.enc(17, 99), marker])])
        doc.save()

        reloaded = wbasm.load_menus(tmp)
        opt = reloaded.by_name(target.name).options[0]
        check(len(opt.conditions()) == n_cond + 1,
              "set_conditions did not persist through save/reload")
        check(len(opt.consequences()) == n_conseq + 1,
              "set_consequences did not persist through save/reload")
        check(opt.conditions()[-1].operands[1] == marker,
              "persisted condition lost its faction operand")
        check(opt.consequences()[-1].operands[1] == marker,
              "persisted consequence lost its faction operand")
        check(opt.cond_count == n_cond + 1, "option cond_count not rewritten")
        check(opt.conseq_count == n_conseq + 1, "option conseq_count not rewritten")
        check(reloaded.by_name(target.name).declared_option_count
              == target.declared_option_count,
              "menu option count drifted during a conditions-only edit")
        raw = pathlib.Path(tmp).read_bytes()
        check(raw.count(b"\n") - raw.count(b"\r\n") == 0,
              "menu save introduced LF-only line endings")
    finally:
        shutil.rmtree(work, ignore_errors=True)


FACTION_LO, FACTION_HI = 6 << 56, 7 << 56


def _raw_faction_operands(path):
    """Count tagged faction operands by scanning BYTES, not parsed statements.

    Deliberately parser-independent: this is the check that decides whether a
    parser can see everything the file holds. The menu-line blind spot survived
    because every check ran through the same parser that could not see it.
    """
    total = 0
    for token in pathlib.Path(path).read_bytes().split():
        if token.isdigit() and FACTION_LO <= int(token) < FACTION_HI:
            total += 1
    return total


def _parsed_faction_operands(blocks):
    total = 0
    for statements in blocks:
        for statement in statements:
            for operand in statement.operands:
                if isinstance(operand, int) and operand > 0 \
                        and FACTION_LO <= operand < FACTION_HI:
                    total += 1
    return total


def _check_new_table(path, loader, records_of, blocks_of, declared, baseline_operands):
    """Round-trip, record count, and the blind-spot check.

    `baseline_operands` is the count measured when the parser was written. It is
    asserted as a FLOOR, not an equality: editing a module can legitimately add
    faction operands, and pinning the exact number would be an over-tight
    assertion that fails on correct data.

    The equality that matters and never drifts is parsed == raw: whatever the
    file holds, the parser must be able to see all of it.
    """
    original = pathlib.Path(os.path.join(MODULE, path)).read_bytes()
    doc = loader(os.path.join(MODULE, path))
    check(doc.serialize() == original, "%s round-trip not byte-identical" % path)
    records = records_of(doc)
    expected = doc.declared_count if declared is None else declared
    check(len(records) == expected,
          "%s: %d records, header declares %d" % (path, len(records), expected))
    blocks = [b for r in records for b in blocks_of(r)]
    seen = _parsed_faction_operands(blocks)
    raw = _raw_faction_operands(os.path.join(MODULE, path))
    check(raw >= baseline_operands,
          "%s: raw scan found %d faction operands, fewer than the %d measured "
          "before any expansion -- operands were LOST"
          % (path, raw, baseline_operands))
    check(seen == raw,
          "%s: parser sees %d faction operands but the bytes hold %d -- "
          "the parser has a blind spot" % (path, seen, raw))
    return doc


def test_new_table_edits_persist():
    """Each new record type must actually write its edits back.

    Same rule as `test_menu_option_edits_persist`: the mutable copy goes to a
    temporary directory. These three used to be `<module>/<table>.test_edit`,
    with the same concurrent-run race and the same unignored stray on a crash.
    """
    marker = wbasm.enc(6, 35)
    cases = [
        ("triggers.txt", wbasm.load_triggers, lambda d: d.triggers[0]),
        ("conversation.txt", wbasm.load_conversation, lambda d: d.dialogs[0]),
        ("mission_templates.txt", wbasm.load_mission_templates,
         lambda d: d.triggers[0]),
    ]
    for name, loader, pick in cases:
        src = os.path.join(MODULE, name)
        work = tempfile.mkdtemp(prefix="wbasm_table_edit_")
        tmp = os.path.join(work, name)
        shutil.copyfile(src, tmp)
        try:
            doc = loader(tmp)
            rec = pick(doc)
            n = len(rec.conditions())
            rec.set_conditions(rec.conditions()
                               + [wbasm.Statement(31, [wbasm.enc(17, 99), marker])])
            doc.save()
            back = pick(loader(tmp))
            check(len(back.conditions()) == n + 1,
                  "%s: set_conditions did not persist" % name)
            check(back.conditions()[-1].operands[1] == marker,
                  "%s: persisted condition lost its faction operand" % name)
            raw = pathlib.Path(tmp).read_bytes()
            check(raw.count(b"\n") - raw.count(b"\r\n") == 0,
                  "%s: save introduced LF-only line endings" % name)
        finally:
            shutil.rmtree(work, ignore_errors=True)


def main():
    for fn in TESTS:
        fn()
    print("checks run: %d" % CHECKS[0])
    if FAILURES:
        print("FAILED: %d" % len(FAILURES))
        for f in FAILURES[:25]:
            print("  - %s" % f)
        if len(FAILURES) > 25:
            print("  ... and %d more" % (len(FAILURES) - 25))
        return 1
    print("all green")
    return 0



#: A presentation trigger record is one line opening with its check period,
#: e.g. "-60.000000  21 2133 ...". Presentation headers open with "prsnt_".
TRIGGER_LINE = re.compile(r"^-?\d+\.\d+\s")


def test_presentations_round_trip():
    """presentations.txt must re-serialise byte-identically.

    This file carries bytecode, so any edit here is only safe if an untouched
    load/save is a no-op.
    """
    path = os.path.join(MODULE, "presentations.txt")
    doc = wbasm.load_presentations(path)
    original = pathlib.Path(path).read_bytes()
    check(doc.serialize() == original, "presentations.txt round-trip not byte-identical")
    check(len(doc.presentations) == doc.declared_count,
          "presentation count disagrees with the declared header count")
    total = 0
    for presentation in doc.presentations:
        check(len(presentation.triggers) == presentation.declared_triggers,
              f"{presentation.name}: trigger count disagrees with its header")
        for trigger in presentation.triggers:
            statements = trigger.statements()
            check(len(statements) == trigger.declared_count,
                  f"{presentation.name}: statement count disagrees with its header")
            total += 1
    # This counted coverage: that the walk above actually visited every trigger
    # line the file holds. Pinning it to 181 broke on every appended trigger, so
    # assert the relation instead -- recount the trigger records straight from
    # the raw text, independently of the headers the parser itself read.
    raw_triggers = sum(1 for line in original.decode("utf-8").splitlines()
                       if TRIGGER_LINE.match(line))
    check(raw_triggers > 0 and total == raw_triggers,
          f"walked {total} presentation trigger lines but presentations.txt "
          f"holds {raw_triggers}")

TESTS = (test_operand_encoding, test_opcode_flags,
         test_simple_triggers_roundtrip, test_menus_roundtrip,
         test_file_bytes_preserved,
         test_append_and_remove_script,
         test_remove_trailing_script_refuses_non_final,
         test_append_trigger,
         test_menu_option_edits_persist,
         test_presentations_round_trip,
         test_new_table_edits_persist)


class WbasmTests(unittest.TestCase):
    def setUp(self):
        _support.require_module(MODULE)


_support.add_tests(WbasmTests, TESTS, FAILURES)


if __name__ == "__main__":
    sys.exit(main())
