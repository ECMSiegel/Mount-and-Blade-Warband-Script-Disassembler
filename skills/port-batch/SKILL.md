---
name: port-batch
description: Run many Warband feature ports as one managed batch with builder and integrator roles, dependency waves, shared slot and global allocation, and a strict "delivered" test. Use when the user says "port-batch", "port several features", "port these N features", or wants a queue of ports applied onto one target.
---

# Port batch

A runbook for N ports using the wbtools toolkit. Each single port follows the `atlas-port` skill;
this skill adds the ordering, the roles and the shared bookkeeping. Run commands from the wbtools
repo root as `python3 wbsd/wbsd.py ...`. Use the brief template `atlas-port/references/port-brief.md`.

## Roles
- **Controller** (you, or the user): picks and ranks, owns the shared allocation list, decides
  waves, dispatches builders, runs the integrator.
- **Builder**: one port, one working copy. Writes the brief and the port script, runs `verify-port`
  on its own copy, reports. Never runs the whole-suite check, never touches another builder's copy
  or the target.
- **Integrator**: applies finished ports onto one target copy, wave by wave.

If no sub-agents exist, one agent plays each role in turn, one port at a time.

## Procedure
1. **Pick and rank.** `python3 wbsd/wbsd.py features [REGEX]` lists atlas records; add any
   briefs the user has. Rank by value to the player, small closure first, fewest unknowns. Drop
   candidates whose source terms are unknown until the user answers. Write the ranked list to a
   batch file (`references/batch-files.md` has the layout).
2. **Allocate once.** Build the shared list of free slots and globals in the target (from `slots`
   and `global`), and assign each port its numbers up front. Builders may not pick their own.
3. **Facts-first per port.** Each builder runs `atlas-port` step 0 and fills the brief. Ports
   with an open STOP AND ASK item wait; do not build around it.
4. **Make waves.** Port B depends on A if B calls, edits or shares a slot or global with anything
   A adds or changes. Independent ports share a wave. Record the waves in the batch file.
5. **Build per port.** One working copy of the target per port, never shared (a copy of the
   current integrated target for its wave). The builder writes the port script with `wbport`
   (`atlas-port` step 4), runs it on its copy, and runs
   `wbsd verify-port BASE COPY --expect ...` with a fail-first demonstration. `--assume-reached`
   only with a written reason in the brief, and never for a new `game_*` script (it must be an
   existing engine hook). `--allow-edit <host>` likewise, one written reason per name. Report: brief path, script path, verify output, open issues.
6. **Integrate by wave.** The integrator copies the target to a fresh integration copy, runs each
   wave's port scripts in order against it (`python3 port_<name>.py <integration copy>`; the
   scripts are re-runnable and take the target folder as their first argument), then runs
   `verify-port BASE_OF_WAVE INTEGRATED` with the union of the builders' `--allow-edit`,
   `--touched` and `--assume-reached` lists (and the union of `--expect`), after every wave and stops on the first FAIL. A FAIL goes
   back to the builder of the port that caused it; do not patch around it in the integrator.
   Slot or global clashes the integrator finds are fixed in the shared list and the affected
   builders re-run.
7. **Delivered test.** A port is delivered only when all hold: the brief is complete with no open
   STOP AND ASK; `verify-port` printed PASS on the integrated copy, and the failing run on a
   doctored copy was shown; provenance is recorded. Anything less is "built" or "claimed", not delivered.
8. **Playtest handoff.** Give the user one list: the integrated copy path, the backup, per port the
   in-game steps and expected result, and the save posture of each. After they play, run
   `wbsd check-log <rgl_log.txt>` (material, texture and mesh warnings are only counted as
   cosmetic, so check them yourself). Their report outranks every check; reopen a port on their word.
9. **Close.** Update the batch file with delivered / claimed / failed per port. Only the user
   moves a port to confirmed.

## Limits
- Concurrency cap: at most 4 builders at once. Each one loads module indexes, and the machine is
  often busy; more builders slow everything and risk timeouts.
- Run anything that may take over two minutes in the background with a log file, and read the
  whole log. Never rerun a command just because a foreground wait timed out.
- Before starting a wave, write the batch file to disk so a killed run loses nothing. If a builder
  dies from a usage or API limit, record where it stopped in the batch file and tell the user.
- When copying to the live target, copy only changed tables, never `*.bak_before_*` or `ports.log.jsonl`.
- Only the integrator writes the integration copy. Nobody writes a source, donor, base module or
  the live target until the user approves the final copy-over.

## Exit criteria
- The batch file lists every port with its wave, builder, and status (delivered, claimed, failed, cut).
- Each delivered port meets the delivered test in step 7.
- The shared allocation list matches what is in the integrated copy.
- The user has the playtest handoff list; `check-log` was run after their play session if a log exists.
- Nothing outside the working copies was written.

## When uncertain
- Dependency between ports unclear: put them in different waves, earlier one first.
- A builder and the integrator disagree on a number: the shared list wins; fix the list, rebuild.
- Unsure a port is safe to include: leave it out of the wave and ask the user.
- A check fails and the cause is not clear: stop the wave, report the FAIL output, do not retry blindly.
