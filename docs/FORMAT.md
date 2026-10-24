# Compiled module format

This describes the text files a compiled Mount & Blade: Warband module ships
(`scripts.txt`, `menus.txt`, ...) as `wbasm.py` reads and writes them and as
`wbsd/corpus.py` reads them. Everything here comes from the code and its
docstrings. Anything not stated in the code is marked "(inferred)". All
examples are from the Native module; the commands that produced them are given
so you can reproduce them.

Reproduce with, from the `wbtools` folder:

    WB_MODULE=Native python3 wbdis.py game_start
    python3 wbsd/wbsd.py dis native game_start --raw

`dis --raw` prints an indexed list of statements; the token streams shown below are decoded from that output.

## 1. Files and tables

Each table is one plain text file in the module folder, tokens separated by
whitespace. Native uses CRLF line endings; the tools keep each line's own
separators and line endings untouched (see section 8).

Most tables start with a two-line header: `<name>file version N`, then the
declared record count.

    scriptsfile version 1
    610

Exceptions the code handles:

- `tableau_materials.txt` has no version line; its header is the count alone.
- `simple_triggers.txt` has a differently spelled first line
  (`simple_triggers_file version 1` in Native).
- `mission_templates.txt` is not line-per-record (section 7).
- Older-format modules use older versions of some files. `corpus.py` records the
  header version and skips fields that a version lacks: `dialogsfile version 1`
  has no voice-over field, `itemsfile version 2` has no per-item faction list.

`wbasm.py` is the lossless reader/writer for `scripts.txt`, `simple_triggers.txt`,
`triggers.txt`, `menus.txt`, `presentations.txt`, `conversation.txt`,
`mission_templates.txt` and `tableau_materials.txt`. `corpus.py` is a tolerant
read-only parser that reads by token stream instead of by line, and additionally
covers items, scene props and map icons. A record whose code wraps onto a second
line therefore still parses there. Parse problems are collected per table, not
raised.

## 2. Statements

A statement is:

    <opcode> <operand_count> <operand> ...

All values are decimal integers. A block of code is a sequence of statements
laid back to back with no separator. The block itself is introduced by a
statement count (not a token count), so a reader walks `count` statements, using
each statement's own `operand_count` to find the next one.

Native's `game_start` script, first statements (raw, then decoded):

    675 502 3 432345564227567630 21 2 2133 2 144115188075856755 200 ...
    502(m6_14, 21, 2)
    2133($g883, 200)

`675` is the script's statement count; `502 3 ...` is opcode 502 with three
operands; `2133 2 ...` is opcode 2133 with two. A truncated statement (fewer
tokens than its operand count) or a negative count is an error in `wbasm.py`.

## 3. Opcode flags

Two flags live in the opcode token's high bits:

| Bit         | Name           | Meaning in the disassembly |
|-------------|----------------|----------------------------|
| `0x80000000`| `neg`          | `neg\|<opcode>`            |
| `0x40000000`| `this_or_next` | `this_or_next\|<opcode>`   |

The base opcode is the token with those two bits cleared. `wbasm.py` keeps the
flags separately and rejoins them on output. Native examples:

    2147483678 2 1224979098644774929 20     ->  neg|30(:v17, 20)
    1073741855 2 1224979098644774913 ...    ->  this_or_next|31(:v1, trp0)

(`corpus.py` masks with `0x3FFFFFFF` / `0xC0000000` instead, which also clears
bit 30 and 31 of the opcode, the same two flags.)

## 4. Operands and tags

An operand is a 64-bit value with a type tag in the high bits and an index in the
low 56 bits:

    operand = tag << 56 | index

Bare constants (including negative numbers such as `-1`) have tag 0 and are
passed through unchanged. `wbasm.opmask()` returns the tag, `wbasm.opval()` the
index, `wbasm.enc()` builds one.

Tags that `wbasm.py` and `wbdis.py` name:

| Tag | Disassembler label | Meaning                    |
|-----|--------------------|----------------------------|
| 0   | (none)             | bare constant              |
| 1   | `reg`              | register                   |
| 2   | `$g`               | global variable            |
| 3   | `str`              | string                     |
| 4   | `itm`              | item                       |
| 5   | `trp`              | troop                      |
| 9   | `p`                | (inferred) party           |
| 13  | `script`           | script (by index)          |
| 17  | `:v`               | local variable             |
| 19  | `skl`              | skill                      |
| 22  | `qstr`             | quick string               |

Other tags occur in real data (the disassembler prints them as `m<tag>_<index>`;
`m6_14` above is tag 6). The code does not name them, so this document does not.
The index is a position in the matching table, e.g. troop 463 is the 464th
record of `troops.txt`.

Native examples (all decoded by `opmask`/`opval`):

    1224979098644774912  = 17 << 56 | 0     local variable 0   (:v0)
    360287970189640143   =  5 << 56 | 463   troop 463         (trp463)
    936748722493063651   = 13 << 56 | 483   script 483        (script483)
    144115188075856917   =  2 << 56 | 1045  global var 1045   ($g1045)

Register and variable indices are plain numbers; names such as `trp_...` are
compile-time conveniences and do not appear in the compiled text. Names are
recovered from the other table files (`corpus.py` reads them with line patterns
like `^\s*(trp_\S+)`).

## 5. Structural control flow

Control flow is structural, not offset based. There are no jump targets or
offsets in a block; nesting is expressed by the sequence of statements alone.
Opcodes `wbasm.py` names:

| Opcode | Name                      |
|--------|---------------------------|
| 3      | `try_end`                 |
| 4      | `try_begin`               |
| 5      | `else_try`                |
| 6      | `try_for_range`           |
| 7      | `try_for_range_backwards` |
| 11     | `try_for_parties`         |
| 12     | `try_for_agents`          |
| 16     | `try_for_prop_instances`  |
| 17     | `try_for_players`         |

`try_begin`, `try_for_range`, `try_for_range_backwards`, `try_for_parties`,
`try_for_agents`, `try_for_prop_instances` and `try_for_players` open a block and each must be closed by one `try_end`.
`else_try` continues the enclosing block without changing depth. The
disassembler indents by that depth. Native's `game_enable_cheat_menu`:

    23(:v0, 1)
    4()
      31(:v0, 0)
      2133($g291, 0)
      5()
      31(:v0, 1)
      2133($g291, 1)
    3()

Because nothing refers to a statement's position, inserting a well-formed,
balanced run of statements into an existing block needs no fix-ups.
`wbasm.block_depth_ok()` checks the balance.

Inside a `try_begin`/`else_try` chain, the statements directly after the opener
are conditions: the branch runs only if they succeed (inferred from the opcode
names, not stated in the code). `this_or_next` marks a condition that, if true,
lets the following condition be skipped, i.e. an OR; plain consecutive
conditions are an AND (inferred). Native, from `game_start`:

    6(:v1, 0, trp463)
      this_or_next|31(:v1, trp0)
      33(:v1, trp194, trp463)
      ...
    3()

## 6. Where code lives

Every table below embeds one or more statement blocks. The code reads the
following shapes (`N` = a statement count followed by that many statements).

| Table                  | Record shape |
|------------------------|--------------|
| `scripts.txt`          | name line `<name> -1`, then a body line `N`. Scripts are called by index. |
| `simple_triggers.txt`  | one line: `<interval> N`. |
| `triggers.txt`         | one line: `<check> <delay> <rearm> N(cond) N(conseq)`. |
| `menus.txt`            | per menu, a menu line then an options line (below). |
| `presentations.txt`    | header line, then a trigger line each: `<interval> N`. |
| `conversation.txt`     | one dialog per line (below). |
| `mission_templates.txt`| trigger lines `<check> <delay> <rearm> N(cond) N(conseq)` inside a template (section 7). |
| `tableau_materials.txt`| `<name> <flags> <sampler> <w> <h> <mx> <my> <mw> <mh> N` (9 head tokens). |
| `item_kinds1.txt`, `scene_props.txt`, `map_icons.txt` | per-record trigger lists: `<ntriggers>` then `<interval> N` each (read by `corpus.py` only). |

Native examples, raw:

    scripts.txt (name line, then body):
      game_start -1
       675 502 3 432345564227567630 21 2 2133 2 ...
    simple_triggers.txt (one trigger):
      1.000000  2 37 0 1 2 936748722493063651 65536
      -> 37()  and  1(script483, 65536)

In `simple_triggers.txt` the example above is `call_script`-style: opcode 1 with
a script operand first, followed by its arguments (the toolkit itself treats
opcode 1 as a script call when it searches for triggers calling a script).

**Menus.** The menu line is

    menu_<name> <flags> <text> <mesh> N <statements...> <option_count>

where the trailing `option_count` is not part of the statement stream. The
options line then repeats, with no delimiter between options:

    mno_<id> N(cond) <text> N(conseq) <text2>

`text2` is ordinary option data (sometimes a real string, not a terminator) and is
read by position, never matched against a literal. Native `menu_tutorial`:

    menu_tutorial 512 You_approach_a_field_... none 7 4 0 31 2 ... 3 0 2
    ... mno_continue  0  Continue...  42 1261 1 ...

Seven statements, then option count 2. `mno_continue` has zero conditions
(`0`), the text `Continue...`, and 42 consequence statements.

**Dialogs.** One line each:

    dlga_<state>:<next> <flags> <partner> N(cond) <text> <next_token> N(conseq) <voiceover>

`text` and `voiceover` are positional fields. Native:

    dlga_start:fighter_chamber_warn 4095 0  2 33 3 ... {!}TODO:_What_are_you_... 35  1 2133 2 144115188075856904 0 NO_VOICEOVER

## 7. Mission templates

`mission_templates.txt` is not one record per line. Each template has a
`mst_<name>` line, a description line, then entry-point records (bare integers in
fixed-width columns) and a trigger count. `wbasm.py` models only the trigger
lines and keeps every other line as raw bytes, because only triggers carry
bytecode. Trigger lines are found by shape: three leading floats (which contain
a `.`, unlike entry-point integers), then two statement blocks that consume the
line exactly. A template with no entry points puts the entry count and the
trigger count on one line, which is why a line-by-line walk is wrong. `corpus.py`
instead walks the token stream per template. Native trigger line (cut):

    1.000000 0.000000 100000000.000000  0  11 2211 1 1224979098644774912 503 3 ...

check interval 1.0, delay 0.0, rearm 100000000.0, zero condition statements, 11
consequence statements.

## 8. Round-trip guarantee and the append-only rule

Records keep their original bytes (leading and trailing whitespace, token
separators, line endings, even mixed CRLF/LF) and re-emit them verbatim unless
the record was modified. Loading and saving an untouched file is a no-op at the
byte level. Checked read-only against Native's own files, `serialize()` equals
the file bytes for scripts, simple triggers, triggers, menus, conversation,
mission templates, presentations and tableau materials. A modified record is
rewritten as the normalised token stream with its count updated; a header count
is rewritten only if the number of records changed.

Scripts are referenced by index (the operand of tag 13), so new scripts may only
be **appended**, never inserted or reordered: inserting anywhere else silently
repoints every later script call. `ScriptsDoc.append_script()` appends and
returns the new index; `remove_trailing_script()` refuses to remove anything but
the final entry. The corpus loader keeps duplicate script names as separate
entries (`script:<name>#<index>`), since calls are by index and both copies can be
live.

Menu option edits carry one extra duty: the menu line's trailing option count is a
separate field on a separate line, so adding an option must update it as well
(see the note on `MenuOptionsLine` in `wbasm.py`).
