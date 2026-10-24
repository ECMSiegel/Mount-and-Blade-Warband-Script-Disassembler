# Atlas notes (house rules for audits)

Copy this file to `atlas-notes.md` in your atlas folder and fill it in. Audits read it before
comparing any module against your main mod. Leave a heading empty if it does not apply.

## Target mod baseline
<One paragraph: what your main mod is built on (Native, another mod, which versions), and the
main systems it already has, so audits can tell "present" from "absent".>

## Blocked opcodes / platform limits
<Opcode numbers or engine extensions your platform cannot run, and what to do about a feature
that needs them (skip, or rebuild without them). Also any engine limit you hit.>

## Known-used slots and free ranges
<Per object kind (troop, party, faction, item, ...): slot ranges your mod already uses, ranges
verified free, and any slot indexed by an id (not a fixed purpose), which is never free.>

## Scripts not to touch
<Scripts or systems that must stay as they are, and why.>

## Other house rules
<Anything else an auditor should respect: naming, categories to ignore, value judgments.>
