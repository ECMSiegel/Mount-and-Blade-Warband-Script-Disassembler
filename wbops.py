#!/usr/bin/env python3
"""Named opcodes and operand helpers for wbasm.

HARD RULE: an opcode enters this file only with a decoded in-corpus example in
its comment. Never from memory, never by inference from a name -- a wrong opcode
number produces silently broken game logic rather than an error, so the comment
IS the safety mechanism.

Every example below was produced by `python3 gen_evidence.py`, which
searches scripts.txt and simple_triggers.txt and prints the comment text. Do not
type an example by hand: paste the tool's output. `tests/test_wbops.py` re-reads
these comments and re-derives each cited statement from the corpus, so a
fabricated example fails the suite.

Three opcodes carry no operands and so cannot be cited as a decoded example.
They are marked EVIDENCE-STRUCTURAL and justified by the block-balance check in
tests/test_wbasm.py instead; see the note above their marker.

DISAMBIGUATION CONVENTION: a decoded citation proves an opcode EXISTS with N
operands, but that alone cannot distinguish two opcodes with the same arity
whose meanings differ only in operand order or comparison direction (e.g. `ge`
vs `gt`, or `store_sub(d,a,b)` vs `store_sub(d,b,a)`) -- GT=30 shipped and
passed every existence/citation check while actually meaning `ge`, because
nothing checked that. For opcodes in that risk class (the comparisons: 30-33
here), the evidence citation is followed by a `# DISAMBIGUATES:` comment
pointing at a second corpus site that would read WRONG under the alternative
meaning -- e.g. a value compared against a `store_random_in_range(0,100)`
result only reads as a clean percentage threshold under one of the two
meanings. That second line is documentation only (not machine-checked); when
adding a comparison or order-sensitive opcode, find and record a real site
like this before trusting the arity-only evidence.
"""
from wbasm import (Statement, enc, OP_NEG, OP_THIS_OR_NEXT,  # noqa: F401
                   TRY_END, TRY_BEGIN, ELSE_TRY,
                   TRY_FOR_RANGE, TRY_FOR_RANGE_BACKWARDS)

# --- operand helpers --------------------------------------------------------

def REG(n):    return enc(1, n)    # 72057594037927936 = reg0
def GVAR(n):   return enc(2, n)
def STR(n):    return enc(3, n)
def ITM(n):    return enc(4, n)    # 288230376151711825 = item 81
def TRP(n):    return enc(5, n)    # 360287970189639950 = troop 270
def PARTY(n):  return enc(9, n)    # 648518346341351424 = p_main_party
def SCRIPT(n): return enc(13, n)   # 936748722493063753 = script 585
def V(n):      return enc(17, n)   # 1224979098644774912 = local var 0
def SKL(n):    return enc(19, n)   # 1369094286720630799 = skill 15
def QSTR(n):   return enc(22, n)   # 1585267068834415832 = qstr1240
def FAC(n):    return enc(6, n)    # 432345564227567632 = faction 16
def PT(n):     return enc(8, n)    # 576460752303423551 = party template 63
def SCENE(n):  return enc(10, n)   # 720575940379279598 = scene 238
def MENU(n):   return enc(12, n)   # 864691128455135264 = menu 32

# --- control flow -----------------------------------------------------------

CALL_SCRIPT = 1              # game_start: 1(script227, :v21, :v24)

# try_end/try_begin/else_try take no operands, so there is no decoded example to
# cite and none may be invented. Their proof is structural instead: opcodes
# {4,6,7,11,12} open a block and 3 closes it, and with exactly that assignment
# every one of the 9116 bytecode blocks Native ships balances (counted with the
# wbsd loader), while dropping any one opener from the set leaves between 22 and
# 1297 imbalances. tests/test_wbasm.py::_check_nesting runs the same check over
# the tables it loads on every test run.
# EVIDENCE-STRUCTURAL TRY_END: closes a block in the balance check over all 9116 blocks of Native (test_wbasm.py::_check_nesting)
# EVIDENCE-STRUCTURAL TRY_BEGIN: opens a block in the balance check over all 9116 blocks of Native (test_wbasm.py::_check_nesting)
# EVIDENCE-STRUCTURAL ELSE_TRY: nests inside a balanced block in the check over all 9116 blocks of Native (test_wbasm.py::_check_nesting)

# TRY_FOR_RANGE and TRY_FOR_RANGE_BACKWARDS are imported from wbasm (which
# defines them as 6 and 7), so they have no assignment to hang a comment on;
# their generated evidence is cited here instead.
# EVIDENCE TRY_FOR_RANGE: game_start: 6(:v1, 0, trp463)
# EVIDENCE TRY_FOR_RANGE_BACKWARDS: game_get_troop_note: 7(:v14, p21, p201)

STORE_SCRIPT_PARAM_1 = 21    # game_event_party_encounter: 21($g401)
STORE_SCRIPT_PARAM_2 = 22    # game_event_party_encounter: 22($g914)
STORE_SCRIPT_PARAM = 23      # game_get_use_string: 23(:v0, 1)
# DISAMBIGUATES STORE_SCRIPT_PARAM: 23 is order-sensitive -- (dest, index) vs
#   (index, dest). Every engine callback in the corpus opens with a run of 23s
#   whose SECOND operand counts 1, 2, 3 upward while the first is a fresh local
#   each time: game_get_item_extra_text opens 23(:v0,1) 23(:v1,2) 23(:v2,3), and
#   game_get_skill_modifier_for_troop opens 23(:v0,1) 23(:v1,2). Under the
#   reverse layout the parameter INDEX would be a local and the destination the
#   literal 1, 2, 3 -- i.e. three writes to registers 1, 2 and 3 that no later
#   statement ever reads, while the locals every later statement DOES read would
#   be written by nothing. Its fixed-index siblings 21 and 22 take the
#   destination alone, which is the same operand in the same position.

# --- comparisons ------------------------------------------------------------

GE = 30                       # game_start: 30(:v63, 1)
# DISAMBIGUATES GE: game_start: 2136(:v17, 0, 100) followed by neg|30(:v17, 20)
#   -- store_random_in_range(:v17,0,100) then reject unless :v17 < 20. That is
#   a clean 20% threshold only if neg|30 == lt, i.e. opcode 30 == ge. Under the
#   alternative (30 == gt, so neg|30 == le), every such threshold in the
#   corpus would be off by one (21%, 11%, 6%, ... instead of 20%, 10%, 5%);
#   process_sieges (neg|30 against 10) and spawn_bandits (against 5) follow the
#   same pattern. Self-verifying from the bytes alone: no assumption about
#   engine convention is needed, only that these thresholds are clean round
#   percentages.
EQ = 31                       # game_start: 31(:v10, 1)
# DISAMBIGUATES EQ: center_ambiance_sounds: 2136(:v5, 0, 7) followed by the
#   chain 31(:v5, 1), 31(:v5, 2), ... 31(:v5, 5) -- store_random_in_range(:v5,0,7)
#   then proceed only if :v5 == 1 (or 2, or 3 ...), strictly interior values
#   (0 < 1 < 7). That rules out le/ge readings, which would give a different,
#   boundary-shaped probability instead of the clean 1/8 an exact single-value
#   match gives. (A site that tests the range's own floor, such as
#   2136(:v79,0,5) + 31(:v79,0), does NOT disambiguate anything: eq and le are
#   numerically indistinguishable there.) eq is operand-order-symmetric, so
#   operand order carries no separate risk to check here.
GT = 32                       # game_start: 32(:v44, 63)
# DISAMBIGUATES GT: setup_troop_meeting statements 7-8:
#     7: 4()                 -- try_begin
#     8: 32(:v1, -1)         -- the block's sole, entire condition
#   Structural fact, verified directly from the corpus and not resting on any
#   outside assumption: 32(:v1,-1) is the only statement between this
#   try_begin and the first action (1263, set_visitor), so it IS the block's
#   boolean gate rather than an incidental comparison -- consistent with a real
#   direction-sensitive comparison opcode being used for control flow, as
#   30/31/33 are elsewhere in this file.
#   Corroboration only, not proof of *which* direction: opcode 32 carries a
#   -1 second operand in 59 of 770 two-operand uses (7.7%) vs. 3 of opcode
#   30's 1234 (0.2%), suggestive of the "gt x -1" valid-id idiom (must
#   admit 0). This does NOT by itself establish direction -- it only shows
#   32 is favoured for -1 comparisons. The actual ge/gt direction rests on
#   GE's self-verifying site above, plus 32 being the only opcode in
#   {30,31,32,33} left unassigned once GE=30, EQ=31, and IS_BETWEEN=33 are each
#   independently pinned by their own citations.
IS_BETWEEN = 33               # game_start: 33(:v1, trp194, trp463)
# DISAMBIGUATES IS_BETWEEN: game_start statements 10-12, in context:
#   10: 6(:v1, 0, trp463)              -- try_for_range :v1 = 0 .. trp463
#   11: this_or_next|31(:v1, trp0)     -- :v1 == trp0, or fall through
#   12: 33(:v1, trp194, trp463)        -- citation
#   The loop's own upper bound (trp463) equals the citation's 3rd operand,
#   and the tested value (position 1) is the loop variable rather than a
#   constant -- a reversed layout would need two constants compared against
#   each other, which this loop has no use for. A second site has the same
#   shape: update_trade_good_prices opens 6(:v0, p21, p201) and ends its test
#   with 33(:v0, p91, p201). That is corroborating, read-in-context evidence
#   for operand order (value, low, high) rather than an independent proof.

# --- party predicates -------------------------------------------------------

PARTY_IS_ACTIVE = 132        # game_event_simulate_battle: 132(:v0)
# DISAMBIGUATES PARTY_IS_ACTIVE: opcode 132 takes one operand in 135 of its 137
#   uses, so arity carries no order risk; what needs support is the MEANING.
#   Four scripts (add_routed_party, count_parties_of_faction_and_party_type,
#   let_nearby_parties_join_current_battle,
#   set_parties_around_player_ignore_player) read `11(:vN)` immediately
#   followed by `132(:vN)` -- try_for_parties binding a variable, then this
#   opcode applied to that same variable as the loop body's first statement.
#   That is the try_for_parties/party_is_active prologue, and it is the only
#   reading under which the statement is not dead: the loop has just produced
#   the value, so no comparison against it could be meaningful, while an
#   active/valid test on an enumeration that includes destroyed party slots is
#   exactly what a loop prologue is for.

# --- slots ------------------------------------------------------------------

TROOP_SET_SLOT = 500         # game_start: 500(trp0, 2, 2)
PARTY_SET_SLOT = 501         # game_start: 501(:v15, :v14, 1000)
TROOP_GET_SLOT = 520         # game_start: 520(:v47, :v39, 18)
PARTY_GET_SLOT = 521         # game_start: 521(:v63, :v15, 7)
# DISAMBIGUATES PARTY_GET_SLOT: 521 is order-sensitive -- (dest, party, slot)
#   vs (party, slot, dest). game_event_simulate_battle reads
#   `521(:v29, :v16, 0)` and then compares :v29 against the small constants 3
#   and 2 (this_or_next|31(:v29, 3) / 31(:v29, 2)); game_start sets
#   501(:v15, 53, :v62) and reads 521(:v63, :v15, 7) on the same variable :v15.
#   Under the reversed layout the middle operand would be a slot INDEX and the
#   third a destination, so the tested value would be a slot number and the
#   constant 0 or 7 a destination register. Neither reads. Its setter twin 501
#   carries (party, slot, value).
TROOP_SLOT_EQ = 540          # game_start: 540(trp5, :v11, :v9)
ITEM_SET_SLOT = 507          # game_quick_start: 507(:v0, :v2, 100)
# DISAMBIGUATES ITEM_SET_SLOT: 507 is order-sensitive -- (object, slot, value)
#   vs (object, value, slot). simple_trigger 79, the book-reading trigger, reads
#   a book's accrued progress with `527(:v2, $g307, 2)`, adds 7 to it with
#   `2105(:v2, 7)` and writes it back with `507($g307, 2, :v2)`. The constant 2
#   holds the SAME position in the getter and the setter while the value is the
#   local that was just incremented, so 2 is the slot and :v2 the value; the
#   reverse layout would make the trigger read slot 2 and write slot :v2, a
#   different slot every hour. Its getter twin 527 carries (dest, object, slot).
ITEM_GET_SLOT = 527          # game_receive_network_message: 527(:v7, :v3, :v6)
# DISAMBIGUATES ITEM_GET_SLOT: the setter twin's citation above IS this one's --
#   simple_trigger 79 reads a book's progress with 527(:v2, $g307, 2), adds 7 and
#   writes it back with 507($g307, 2, :v2). The constant 2 holds the same
#   position in both, the object holds the same position in both, and only the
#   destination moves -- first operand on the getter, last on the setter. So 527
#   is (dest, object, slot).

# --- messages ---------------------------------------------------------------

DISPLAY_MESSAGE = 1106       # game_start: 1106(qstr63)
SET_RESULT_STRING = 60       # game_get_statistics_line: 60(1)
# EVIDENCE OF MEANING: opcode 60 takes one operand at all 10 corpus sites, so
#   there is no operand order to get wrong. What it MEANS is fixed by
#   game_get_item_extra_text, which is the callback whose whole job is to return
#   a string: its arms end 60(<quick string>) immediately followed by
#   2075(<colour>). 2075 is already established as the callback's value
#   channel; 60 is the string channel beside it. In game_get_statistics_line
#   each arm fills string register s1 with 2320(1, <string>) and then applies
#   60(1), so the bare 1 is s1, the register 2320 fills.
STR_STORE_ITEM_NAME = 2325   # town_walker_occupation_string_to_s14: 2325(9, :v6)
# DISAMBIGUATES STR_STORE_ITEM_NAME: 2325 is order-sensitive -- (slot, item) vs
#   (item, slot). simple_trigger 79 ends a finished read with 2325(1, $g307),
#   2319(2) and then, per book, 2320(2, <grant string>); $g307 is the book being
#   read, and 2320's own citation already establishes that ITS first operand is
#   the string slot. Same first-operand role, same two slots, one message
#   naming both. The reverse layout would make a book out of the constant 1.
STR_STORE_STRING = 2320      # game_get_use_string: 2320(0, str1801)
# DISAMBIGUATES STR_STORE_STRING: 2320 is order-sensitive -- (slot, string) vs
#   (string, slot). simple_trigger 79 fills s1 with the book's name
#   (`2325(1, $g307)`), clears s2 (`2319(2)`) and sets s2 from the grant's own
#   quick string in each chain arm (`2320(2, qstr562)`), so the first position
#   carries the slot numbers 1 and 2 in every statement that fills a string.
#   The reverse layout would make qstr562 the slot number.

# --- troops -----------------------------------------------------------------

TROOP_IS_HERO = 1507         # game_event_simulate_battle: 1507(:v23)
TROOP_RAISE_ATTRIBUTE = 1520 # age_troop_one_year: 1520(:v0, 0, -1)
TROOP_RAISE_SKILL = 1521     # simple_trigger 79: 1521(trp0, skl15, 1)
TROOP_RAISE_PROFICIENCY = 1522 # cf_training_ground_sub_routine_for_training_result: 1522(:v0, $g941, :v13)

# --- parties ----------------------------------------------------------------

TROOP_ADD_MERCHANDISE = 1530 # mp_spawn_coop_companion: 1530(:v1, :v8)

TROOP_GET_INVENTORY_SLOT = 1541   # cf_multiplayer_is_item_default_for_troop: 1541(:v5, :v1, :v4)
# DISAMBIGUATES TROOP_GET_INVENTORY_SLOT: loot_player_items runs a loop
# 6(:v2, 0, :v1) and reads 1541(:v3, trp0, :v2) -- the destination first, a
# constant troop second, the loop's slot index last;
# multiplayer_set_default_item_selections_for_troop does the same with its
# troop parameter (23(:v0, 1)) second: 1541(:v5, :v0, :v4).
# Only (dest, troop, slot) reads correctly; the reverse order would make a
# troop id out of the loop counter.

ITEM_GET_TYPE = 1570         # start_training_at_training_ground: 1570(:v8, :v7)
# DISAMBIGUATES ITEM_GET_TYPE: cf_multiplayer_upgrade_companion_equipment
# range-tests :v13 against item constants (33(:v13, itm603, itm619)) and then
# reads 1570(:v14, :v13). A (dest, item) read is the only order under which
# the operand that was just range-tested as an ITEM is the input.

PARTY_GET_NUM_COMPANION_STACKS = 1650  # game_event_simulate_battle: 1650(:v21, :v17)
PARTY_STACK_GET_TROOP_ID = 1652        # game_event_simulate_battle: 1652(:v23, :v17, :v22)
PARTY_GET_NUM_PRISONER_STACKS = 1651   # game_event_simulate_battle: 1651(:v21, :v17)
PARTY_PRISONER_STACK_GET_TROOP_ID = 1656  # game_event_simulate_battle: 1656(:v23, :v17, :v22)
PARTY_GET_NUM_COMPANIONS = 1601        # collect_prisoners_from_empty_parties: 1601(:v2, :v0)
# DISAMBIGUATES PARTY_GET_NUM_COMPANIONS: collect_prisoners_from_empty_parties
# reads 1601(:v2, :v0) from its first script parameter :v0 (21(:v0)), and the
# cited read is followed by 4() and 31(:v2, 0), the "party is empty" gate the
# script is named for, so the destination is the first operand and the party
# the second.
PARTY_GET_NUM_PRISONERS = 1602         # npc_decision_checklist_party_ai: 1602(:v9, :v1)
# DISAMBIGUATES PARTY_GET_NUM_PRISONERS: simple_trigger 56 pairs this opcode
# with the 1601 read on the SAME party one statement earlier (1601(:v3, p0) /
# 1602(:v4, p0)) and adds the two into a single count (2105(:v3, :v4)).

# THE MEMBER/PRISONER FAMILY IS ORDER- AND TYPE-AMBIGUOUS BY ARITY ALONE.
# `move_members_with_ratio` is the decisive site: it runs two structurally
# identical loops over the same party, one across the PRISONER accessors and one
# across the MEMBER accessors, and each loop removes from the source and adds to
# the destination with its own pair of opcodes.
#     prisoners: 1651 -> 1656 -> 1657 -> 1616 (remove) -> 1611 (add)
#     members:   1650 -> 1652 -> 1653 -> 1615 (remove) -> 1610 (add)
# Corroborated by Native's transfer scripts, which cross the two types and so
# cannot be explained by any other assignment:
#   party_add_party_companions: member accessors -> 1610, so 1610 adds
#     MEMBERS; its wounded tail 1654 -> 1618 fixes 1618 as party_wound_members.
#   party_prisoners_add_party_companions: MEMBER accessors -> 1611, i.e.
#     it reads companions and files them as prisoners, so 1611 adds PRISONERS.
#   party_remove_all_companions: 1652/1653 -> 1615.
#   party_remove_all_prisoners: 1656/1657 -> 1616.
PARTY_STACK_GET_SIZE = 1653            # game_event_simulate_battle: 1653(:v39, :v36, :v38)
PARTY_PRISONER_STACK_GET_SIZE = 1657   # party_remove_all_prisoners: 1657(:v4, :v0, :v2)
PARTY_ADD_MEMBERS = 1610               # game_event_simulate_battle: 1610(:v0, :v45, :v39)
PARTY_ADD_PRISONERS = 1611             # game_event_simulate_battle: 1611(:v18, :v23, 1)
PARTY_REMOVE_MEMBERS = 1615            # game_event_simulate_battle: 1615(:v36, :v45, :v39)
PARTY_REMOVE_PRISONERS = 1616          # party_remove_all_prisoners: 1616(:v0, :v3, :v4)
PARTY_WOUND_MEMBERS = 1618             # party_add_party_companions: 1618(:v0, :v4, :v6)

# NOT SIZE READS, AND DELIBERATELY LEFT UNNAMED: opcode 1655 sits one past its
# type's size read (1653) and is easy to mistake for it. It is pinned by its
# consumer: setup_party_meeting reads 1652(:v2, :v0, 0) then 1655(:v3, :v0, 0)
# and feeds both straight into 1263(17, :v2, :v3) (set_visitor), whose optional
# last operand is the dna argument. A stack SIZE in that slot would be meaningless, so
# 1655 is a *_stack_get_troop_dna. 1658 has no site in Native's scripts, so
# nothing here may name it.

# --- arithmetic and stores --------------------------------------------------

VAL_ADD = 2105               # game_start: 2105(:v7, 1)
VAL_DIV = 2108               # game_start: 2108(:v46, 4)
# DISAMBIGUATES VAL_DIV: 2108 is order-sensitive -- (dest, divisor) vs
#   (dividend, dest). game_get_item_extra_text's ordinary-book arm reads a
#   book's accrued progress with 527(:v5, :v0, 2), applies 2108(:v5, 10), and
#   prints :v5 (2133(reg1, :v5)) through a quick string. simple_trigger 79
#   finishes that same book at 30(:v2, 1000). A percentage of 1000 is the value
#   divided by 10 and nothing else, so 10 is the divisor and :v5 both dividend
#   and destination; the reverse layout would make the literal 10 the
#   destination register. Corroboration from a second site: game_start copies
#   2133(:v62, reg0), divides 2108(:v62, 2) and stores :v62 -- a value divided
#   in place by a literal.
STORE_SUB = 2121             # game_start: 2121(:v5, p43, p21)
ASSIGN = 2133                # game_start: 2133($g883, 200)
STORE_RANDOM_IN_RANGE = 2136  # game_start: 2136(:v0, p207, p212)
STORE_TROOP_FACTION = 2173   # game_start: 2173(:v40, :v39)
# DISAMBIGUATES STORE_TROOP_FACTION: game_start reads 6(:v54, trp210, trp342) /
# 2173(:v55, :v54) / 33(:v55, m6:14, m6:21), i.e. the result of the citation is
# immediately range-tested against FACTION constants while its input is the
# loop's TROOP variable. Only (dest, troop) reads correctly; the reverse order
# would compare a troop id against faction bounds.
STORE_FACTION_OF_PARTY = 2204  # game_start: 2204(:v24, :v19)
FACTION_GET_SLOT = 522       # game_start: 522(:v34, :v33, 11)
SET_TRIGGER_RESULT = 2075    # game_event_simulate_battle: 2075(:v5)
# EVIDENCE OF MEANING: every one of the 56 corpus sites of this opcode is
# inside a script whose name begins `game_`, i.e. an engine callback. It is the
# channel by which such a callback returns a value; reg0 is not read back.
VAL_CLAMP = 2112             # game_get_troop_note: 2112(:v17, 0, 20)
# DISAMBIGUATES: the upper bound is EXCLUSIVE. troop_get_player_relation and
# change_player_relation_with_troop clamp a relation with 2112(:v, -100, 101),
# and relations run -100..100, so 101 (not 100) is the first rejected value.
STORE_SKILL_LEVEL = 2170     # game_get_troop_wage: 2170(:v4, skl1, trp0)
STORE_CHARACTER_LEVEL = 2171 # game_start: 2171(:v45, :v39)
STORE_ATTRIBUTE_LEVEL = 2172 # game_get_party_companion_limit: 2172(:v3, :v0, 3)
STR_STORE_TROOP_NAME = 2322  # game_start: 2322(5, trp0)

# --- menus and player inventory ---------------------------------------------

JUMP_TO_MENU = 2060          # game_event_party_encounter: 2060(m12:61)
# EVIDENCE OF MEANING: 2060 takes one operand at every corpus site and that
#   operand carries mask 12 (a menu) at all but one of them (simple_trigger 4
#   passes a global variable instead), a mask no other opcode in this file
#   uses. game_event_party_encounter dispatches on 541($g401, 0, <n>) tests, each
#   followed by 2060(m12:<menu>). There is no operand order to get wrong and
#   nothing else a single menu-masked argument could name.
PLAYER_HAS_ITEM = 150        # cf_player_has_item_without_modifier: 150(:v0)
# EVIDENCE OF MEANING: the cited script is NAMED for the predicate, takes the
#   item as its first script parameter and applies 150 to it as the statement
#   immediately after the two store_script_param reads -- the failing-condition
#   prologue of a cf_ script. simple_trigger 79 applies it to $g307, the book
#   currently being read, one statement after 32($g307, 0), so a read stops the
#   moment the book leaves the player's inventory.
ITEM_SLOT_EQ = 547           # multiplayer_get_previous_item_for_item_and_troop: 547(:v7, 60, :v2)
# DISAMBIGUATES ITEM_SLOT_EQ: 547 is order-sensitive -- (object, slot, value) vs
#   (object, value, slot). It is the conditional twin of ITEM_SET_SLOT (507),
#   whose citation above pins (object, slot, value) from trigger 79's
#   getter/setter pair, and the seven read-a-book options of the
#   camp_action_read_book menu each condition on 547(<book>, 3, 0) for the same
#   slot 3 that trigger 79 writes 1 into with 507($g307, 3, 1) when the read
#   finishes. Slot 3 holds the same position in the test and the write; only
#   the value moves. The reverse layout would have the options testing slot 0
#   of a book against the value 3, which nothing ever writes.

#: name -> (opcode, operand count) used by the corpus corroboration test
EVIDENCE = {
    "CALL_SCRIPT": (CALL_SCRIPT, 3),
    "TRY_END": (TRY_END, 0),
    "TRY_BEGIN": (TRY_BEGIN, 0),
    "ELSE_TRY": (ELSE_TRY, 0),
    "TRY_FOR_RANGE": (TRY_FOR_RANGE, 3),
    "TRY_FOR_RANGE_BACKWARDS": (TRY_FOR_RANGE_BACKWARDS, 3),
    "STORE_SCRIPT_PARAM_1": (STORE_SCRIPT_PARAM_1, 1),
    "STORE_SCRIPT_PARAM_2": (STORE_SCRIPT_PARAM_2, 1),
    "STORE_SCRIPT_PARAM": (STORE_SCRIPT_PARAM, 2),
    "GE": (GE, 2),
    "EQ": (EQ, 2),
    "GT": (GT, 2),
    "IS_BETWEEN": (IS_BETWEEN, 3),
    "PARTY_IS_ACTIVE": (PARTY_IS_ACTIVE, 1),
    "TROOP_SET_SLOT": (TROOP_SET_SLOT, 3),
    "PARTY_SET_SLOT": (PARTY_SET_SLOT, 3),
    "PARTY_GET_SLOT": (PARTY_GET_SLOT, 3),
    "TROOP_GET_SLOT": (TROOP_GET_SLOT, 3),
    "TROOP_SLOT_EQ": (TROOP_SLOT_EQ, 3),
    "ITEM_SET_SLOT": (ITEM_SET_SLOT, 3),
    "ITEM_GET_SLOT": (ITEM_GET_SLOT, 3),
    "DISPLAY_MESSAGE": (DISPLAY_MESSAGE, 1),
    "SET_RESULT_STRING": (SET_RESULT_STRING, 1),
    "STR_STORE_ITEM_NAME": (STR_STORE_ITEM_NAME, 2),
    "STR_STORE_STRING": (STR_STORE_STRING, 2),
    "TROOP_IS_HERO": (TROOP_IS_HERO, 1),
    "TROOP_RAISE_ATTRIBUTE": (TROOP_RAISE_ATTRIBUTE, 3),
    "TROOP_RAISE_SKILL": (TROOP_RAISE_SKILL, 3),
    "TROOP_RAISE_PROFICIENCY": (TROOP_RAISE_PROFICIENCY, 3),
    "TROOP_ADD_MERCHANDISE": (TROOP_ADD_MERCHANDISE, 2),
    "TROOP_GET_INVENTORY_SLOT": (TROOP_GET_INVENTORY_SLOT, 3),
    "ITEM_GET_TYPE": (ITEM_GET_TYPE, 2),
    "PARTY_GET_NUM_COMPANION_STACKS": (PARTY_GET_NUM_COMPANION_STACKS, 2),
    "PARTY_STACK_GET_TROOP_ID": (PARTY_STACK_GET_TROOP_ID, 3),
    "PARTY_GET_NUM_PRISONER_STACKS": (PARTY_GET_NUM_PRISONER_STACKS, 2),
    "PARTY_PRISONER_STACK_GET_TROOP_ID": (PARTY_PRISONER_STACK_GET_TROOP_ID, 3),
    "PARTY_GET_NUM_COMPANIONS": (PARTY_GET_NUM_COMPANIONS, 2),
    "PARTY_GET_NUM_PRISONERS": (PARTY_GET_NUM_PRISONERS, 2),
    "PARTY_STACK_GET_SIZE": (PARTY_STACK_GET_SIZE, 3),
    "PARTY_PRISONER_STACK_GET_SIZE": (PARTY_PRISONER_STACK_GET_SIZE, 3),
    "PARTY_ADD_MEMBERS": (PARTY_ADD_MEMBERS, 3),
    "PARTY_ADD_PRISONERS": (PARTY_ADD_PRISONERS, 3),
    "PARTY_REMOVE_MEMBERS": (PARTY_REMOVE_MEMBERS, 3),
    "PARTY_REMOVE_PRISONERS": (PARTY_REMOVE_PRISONERS, 3),
    "PARTY_WOUND_MEMBERS": (PARTY_WOUND_MEMBERS, 3),
    "VAL_ADD": (VAL_ADD, 2),
    "VAL_DIV": (VAL_DIV, 2),
    "STORE_SUB": (STORE_SUB, 3),
    "ASSIGN": (ASSIGN, 2),
    "SET_TRIGGER_RESULT": (SET_TRIGGER_RESULT, 1),
    "VAL_CLAMP": (VAL_CLAMP, 3),
    "STORE_SKILL_LEVEL": (STORE_SKILL_LEVEL, 3),
    "STORE_CHARACTER_LEVEL": (STORE_CHARACTER_LEVEL, 2),
    "STORE_ATTRIBUTE_LEVEL": (STORE_ATTRIBUTE_LEVEL, 3),
    "STR_STORE_TROOP_NAME": (STR_STORE_TROOP_NAME, 2),
    "JUMP_TO_MENU": (JUMP_TO_MENU, 1),
    "PLAYER_HAS_ITEM": (PLAYER_HAS_ITEM, 1),
    "ITEM_SLOT_EQ": (ITEM_SLOT_EQ, 3),
}

#: Names whose evidence is structural rather than a decoded example. These take
#: no operands, so there is nothing to decode; test_wbops.py requires them to
#: carry an EVIDENCE-STRUCTURAL marker and exempts only these from the
#: decoded-citation check.
STRUCTURAL = frozenset(("TRY_END", "TRY_BEGIN", "ELSE_TRY"))


def S(op, *operands, **kwargs):
    """Build a Statement. `flags=OP_NEG` applies the neg| prefix."""
    return Statement(op, list(operands), kwargs.get("flags", 0))
