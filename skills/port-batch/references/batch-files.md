# Batch file layout

Keep one plain-text file per batch next to the briefs, updated at every state change.

```
BATCH: <short name>      TARGET: <slug>      BASE copy: <path>      INTEGRATED copy: <path>

Shared allocation (the only source of new numbers)
  slots:   <object kind> <n> -> <port>   (checked free with `slot` on <date>)
  globals: <name> -> <port>

Ports
  # | port | brief | wave | builder copy | status | verify-port | notes
  1 | <name> | <path> | 1 | <path> | delivered / claimed / built / failed / cut | PASS+fail-first / FAIL | ...

Waves
  1: ports 1, 3     2: port 2 (depends on 1)

Playtest list: per port, steps, expected result, save posture, backup path.
```

Statuses: `built` (script written), `claimed` (verify PASS, fail-first shown, not yet played),
`delivered` (the step 7 test in `SKILL.md`), `failed`, `cut`. Confirmed in real use is the user's word only.
