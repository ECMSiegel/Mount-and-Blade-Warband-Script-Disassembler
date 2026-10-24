# Hard-won lessons for porting

Thirteen rules that apply to any port between compiled Warband modules. Each has the rule, one line
on why, and how to check it. Commands are `wbsd` subcommands (run `python3 wbsd/wbsd.py --help` for
the list). "(see verify-port)" means that command checks it.

## 1. Presence is not reachability
Why: a script, trigger or menu option can sit in the file and never run, because nothing calls it or
an earlier guard always exits first.
Check: `wbsd roots <mod> <script>` must list at least one entry point; `wbsd callers` must list a
real caller. For a trigger, `wbsd hooks <mod>` shows it with the calls it makes. (see verify-port)

## 2. A late write loses
Why: the last write wins. A value written after its reader has already run is never seen, and a
value you set can be overwritten by a later writer in the same pass.
Check: `wbsd global <mod> <name>` and `wbsd slot <mod> <kind> <n>` list every writer. Confirm yours is
the last one before the reader, in the order the code actually runs.

## 3. A check that never failed is not evidence
Why: a check that has only ever passed may not be able to fail at all.
Check: before trusting a check, break its input on a throwaway copy (remove the thing it guards) and
confirm it reports a failure. Then restore the copy.

## 4. A green check is necessary, never sufficient
Why: static checks prove the files are well formed, not that the game behaves. Only running the game
shows that.
Check: after every passing check, load the module in the game and exercise the feature on a new
game. Your own playtest report outranks any passing tool.

## 5. Compiled records are fixed-width and positional; ids are append-only
Why: records are read by position, and every reference is a number. Code that finds a thing by index
or by a pinned total breaks as soon as one entry is added or removed.
Check: find things by name or by shape (`wbsd refs <mod> <kind> <name>`, `wbsd grep`), never by a
hard-coded index or a remembered count. Add new entries only at the end. (see verify-port)

## 6. Donor ids don't map
Why: the same number means a different thing in another module, and some donors compile untagged
ids, so a bare number cannot be read back to a name.
Check: port names, not numbers. Re-resolve each name in the target with `wbsd dis <mod> <block>` (the
named view, not `--raw`) and rebuild the statement against the target's own tables.

## 7. Check a trigger's leading guard before appending to it
Why: a trigger often starts with a condition or an early exit. Code you append after it runs only
when that guard lets it, which may be rarely or never.
Check: `wbsd dis <mod> trig:<n>:cond` (and the trigger body) and read the first statements before
adding anything. If the guard is wrong for your feature, add a trigger of your own instead.

## 8. Know what a range's bounds are used for
Why: a range such as "troops from A to B" may be used as an index or a modulus (a random pick, an
array offset), not only as a membership test. Widening it then changes results that have nothing to
do with membership.
Check: `wbsd grep` for each use of the range's endpoints and read how each is used before changing
either one.

## 9. Slot collisions are silent
Why: two features writing the same slot number corrupt each other without any error. Slots on some
objects (for example the first slots of a hero's troop record) already hold relations, and
per-faction or per-party arrays overlap as they widen.
Check: `wbsd slots <mod> <kind>` lists the slot map; `wbsd slot <mod> <kind> <n>` lists users of one
slot. Take new slot numbers only from a list you declare in the brief, and check each against
both.

## 10. Confirm the deployed copy is the one you edited
Why: a playtest of a different copy than the one you changed proves nothing. Folder names, copies
and shortcuts make this easy to get wrong.
Check: before testing, compare the file you edited with the file the game loads (byte for byte, or
compare size and modification time), and run the game from that exact folder.

## 11. Copy statements, don't rebuild them
Why: the negation flag and the "this or next" flag are stored inside the opcode number, so a
statement rebuilt from its readable form can silently lose them and invert a condition.
Check: build the new statement from a parsed `Statement` of the source and change only its operands.
`port.remap(statement)` does this for ids: it keeps the opcode and flags and translates every named
operand by name. Compare with `wbsd dis <mod> <block> --raw` before and after.

## 12. Read tables as bytes
Why: the files use Windows line endings (CRLF). Reading as text and writing back changes line
endings and can break the file, even when it looks identical on screen.
Check: read and write with bytes. `wbport.Port` does this round-trip check for you; if you use
`wbasm` directly, confirm the parse and serialize round trip is exact before you edit anything.

## 13. Never read a command's exit status through a pipe
Why: in `cmd | tail`, the status you see is the last command's, so a failing step looks like success.
Check: write the output to a log file, read the status on its own line, then read the log. Or set
`set -o pipefail` first.
