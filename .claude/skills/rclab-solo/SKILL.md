---
name: rclab-solo
description: Execute a wave plan sequentially in the main agent session — no subagent spawning. Task list is the primary driver: two tasks per gate (compute, update wp) in order.
argument-hint: <wave-plan-file> [--wp <working-paper-path>] [--start <gate-number>]
---

# rclab-solo — Single-agent sequential wave execution

Like `/rclab-coordinate`, but the main agent does every gate itself, in order. No subagent spawning. The task list is the state machine; tasks are executed in sequence and drive progression from one gate to the next.

Use this when:
- Subagent spawning is crashing.
- A single coherent thread through the wave is wanted (one reasoning narrative, not N parallel ones).
- The wave is small or each gate is quick.

Use `/rclab-coordinate` instead when you want per-gate context isolation or parallelism.

## Usage

```
/rclab-solo sessions/session-plan/session-85-plan-w3.md
/rclab-solo sessions/session-plan/session-85-plan-w3.md --start 4     # resume at gate 4
/rclab-solo sessions/session-plan/session-85-plan-w3.md --wp sessions/archive/session-85/session-85-w3-workingpaper.md
```

## Phase 0 — Resolve paths

- Plan: `PLAN = <arg1>` (path to wave-plan file like `session-85-plan-w3.md`).
- Working paper: `WP = <--wp path>` if given, else derive from the plan's session + wave (e.g. `sessions/archive/session-85/session-85-w3-workingpaper.md`).
- Session: parse `{N}` from plan filename. Verdict file: `computations/session-{N}/s{N}_gate_verdicts.txt`.
- Both PLAN and WP must exist. Read both end-to-end.
- Don't read other plan / workingpaper documents.
- Count K = gates in plan (grep `^## §W{i}-[0-9]`).
- If `--start n`: verify §W{i}-1 through §W{i}-(n-1) are already filled (not still in `*(pending ...)*` state). If any earlier gate is still pending, halt and report.

## Phase 1 — Build the task list (the primary driver)

Call TaskCreate with **2K tasks, in this exact order**:

```
1.  compute §W{i}-1         — {GATE_ID_1}
2.  update wp §W{i}-1       — {GATE_ID_1}
3.  compute §W{i}-2         — {GATE_ID_2}
4.  update wp §W{i}-2       — {GATE_ID_2}
...
2K−1. compute §W{i}-K       — {GATE_ID_K}
2K.   update wp §W{i}-K     — {GATE_ID_K}
```

Task titles must be literal: `compute §W{i}-{n}` and `update wp §W{i}-{n}`. The gate ID goes in the description.

**This step is not optional.** Without the task list the agent loses its place between gates. The two-task-per-gate decomposition is load-bearing: it gives the user an interrupt point between a verdict landing and its write-up — if a verdict is surprising, the user can inspect before the write-up goes in.

If `--start n`: skip tasks 1 through 2(n−1); begin the list at `compute §W{i}-n`.

## Phase 2 — Execute in sequence

For each task in the list, in order:

### `compute §W{i}-{n}`

1. TaskUpdate → in_progress.
2. **Agent-ownership-takeover (no agent tasking).** Read the plan's `Agent:` field for §W{i}-{n}. If a specific agent is designated (e.g., `volovik-superfluid-universe-theorist`, `connes-ncg-theorist`, `mack-cosmic-bridge`, `lizzi-spectral-functional-theorist`, `baptista-spacetime-analyst`), the solo runner TAKES OWNERSHIP of the gate — DO NOT spawn the designated agent via the Agent tool. Agent tasking has known breaking-bug modes (parallel-writer races on shared WPs per `feedback_session-process.md`, stuck Edit-retry loops, transcript-resume edge cases) that solo execution avoids by construction; the user has explicitly preferred avoiding agent tasking. To preserve substantive context, perform the corpus-load BEFORE step 3:
   - Read `.claude/agents/<designated-agent>.md` to identify the agent's research-corpus pointers (typically `researchers/<DirectoryName>/` per the project-root `CLAUDE.md ## Project Structure` table — e.g., volovik → `researchers/Volovik/` 37 papers, baptista → `researchers/Baptista/` 18 papers, paasch → `researchers/Paasch/`, hawking → `researchers/Hawking/`, einstein → `researchers/Einstein/`, schwarzschild-penrose → `researchers/Schwarzschild-Penrose/`, sagan → `researchers/Sagan/`, feynman → `researchers/Feynman/`, dirac-antimatter → `researchers/Antimatter/`, kaluza-klein → `researchers/Kaluza-Klein/`).
   - For agents whose corpus is integrated rather than a folder (e.g., connes-ncg-theorist, lizzi-spectral-functional-theorist, mack-cosmic-bridge), the agent definition file's `## Key References` or analogous section lists the canonical reference pins; load 1-3 of those.
   - Read 1-3 directly-relevant papers / index files from the corpus before proceeding to step 3, picking the papers whose abstracts match the gate's hypothesis keywords (the agent definition's `## Domain Specialties` block or its memory pointers will guide this selection).
   - The solo runner remains the SOLE EXECUTOR; the corpus is loaded for CONTEXT only, NOT for delegation. No Agent-tool dispatch under any circumstance during this skill's run.
3. Read §W{i}-{n} from the plan. Extract: method (Python procedure), machinery pin, input SHA pins, expected 4-tuple, PASS/FAIL/INFO thresholds, substitution chain.
4. **Knowledge MCP pre-compute query (MANDATORY per `.claude/rules/knowledge-index-usage.md`).** Before writing the script, query the MCP:
   - `mcp__knowledge__search_knowledge("<gate topic keywords from the plan>")` — check whether the result is already closed, or a prior session computed it, or the mechanism is eliminated.
   - `mcp__knowledge__get_constant("<constant>")` for every canonical constant named in the plan's substitution chain — confirm value + provenance match what the plan asserts.
   - `mcp__knowledge__trace_entity("<mechanism or theorem>")` if the gate tests a named mechanism or references a theorem 4-tuple.
   Record the queries executed and the salient returns (one line each) in a scratch block — these go into the working-paper entry in step 2 of the `update wp` task (see MCP Pre-Compute Audit block in `.claude/templates/workingpaper.md`).
   **Branch on result**:
   - If a closed result covers the gate → cite the closure, mark the gate PRE-CLOSED in §W{i}-{n}, skip steps 5–8, and move to the `update wp` task.
   - If `get_constant` disagrees with the plan's substitution chain → halt per `knowledge-index-usage.md` §"When the MCP is wrong"; report to user, do NOT proceed until reconciled.
   - Otherwise → proceed to step 5.
5. Write the producing script `computations/session-{N}/s{N}_w{i}_{slug}.py` per the plan's method block. Reuse if already present and matches.
6. Run via canonical Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe" computations/session-{N}/s{N}_w{i}_{slug}.py`. GPU/CPU routing per `.claude/rules/math-scripts.md`.
7. Script PRINTS the verdict payload (`print_verdict_payload`); the agent then `ToolSearch select:mcp__knowledge__emit_verdict` and calls `emit_verdict(**payload)` — the race-safe single writer of `computations/session-{N}/s{N}_gate_verdicts.txt` (canonical line + dual-SHA companion; `.claude/rules/gate-verdicts.md` §"Race-Safe Emission"). The script does NOT open-code a file append.
8. Script exit code reflects script health only — PASS/FAIL/INFO all exit 0 per math-scripts.md §Exit Codes. Non-zero exit means the script broke (traceback, missing input, env error).
9. If script broke: TaskUpdate → blocked, write a one-paragraph diagnostic into the §W{i}-{n} pending block, stop the skill, report to user. Do NOT proceed to the update task.
10. Else: TaskUpdate → completed, move to next task.

### `update wp §W{i}-{n}`

1. TaskUpdate → in_progress.
2. In `WP`, find §W{i}-{n} and replace the two pending blocks (`*(pending agent execution)*` and `*(pending — include: ...)*`) with the completed answer-log entry matching the correct Pattern from `.claude/templates/workingpaper.md`:
   - Numerical PASS/FAIL → Pattern A (subsections a–i)
   - Registration/META → Pattern B (subsections a–l)
   - FAIL with remediation → Pattern C (prose headers)
   - INFO with PRU Class 8 → Pattern D (numbered entries)
   - ABORTED (cascade-failure) → Pattern E (no entry; record state in Constraint-Map table)
3. Paste the verdict line VERBATIM from the verdict file — full 64-char content_sha256 and audit_sha256, never truncated.
4. The substitution chain in the WP carries SUBSTITUTED numbers from this run (not the plan's symbolic form) per math-scripts.md §Double-Check Logic.
5. Substrate framing appears inline in the physical reasoning, not as a separate block, per `.claude/rules/phononic-framing.md`.
6. TaskUpdate → completed, move to next task.

## Phase 3 — Wave close

After the 2K-th task:

1. Grep the WP for remaining `*(pending` blocks — there should be zero.
2. Grep the verdict file for the K gate IDs added this wave — there should be K distinct verdict lines with unique `audit_sha256` (duplicate SHAs indicate a hardcoded-literal bug per `.claude/rules/v3-closure-recovery.md` sig_5).
3. Report: gates attempted (K), PASS / FAIL / INFO / ABORTED counts, script/data/plot file paths, any diagnostics.
4. **Write the Wave {W} Synthesis section** with the math-vs-non-math split (MANDATORY structural form):

   ### Carry-Forward Computations (MATH ONLY — propagate to S{N+1})

   **Discriminator (4-field test)**: an item belongs HERE iff it satisfies ALL FOUR fields. If ANY field cannot be filled, the item is NOT a math carry-forward — move it to "Effected In-Session" below and EXECUTE it NOW.
   - **What**: specific equation / numerical observable / structural theorem to compute
   - **Inputs**: data files, canonical constants, upstream gates needed
   - **Gate**: pre-registered PASS / FAIL / INFO threshold with explicit tolerance
   - **Effort**: estimated wave-equivalents

   ### Effected In-Session (NON-MATH — completed by YOU, the orchestrator, BEFORE declaring wave close)

   **MANDATORY — NON-NEGOTIABLE.** You ARE the final agent for this wave. You hold full Edit / Write access on the project tree. Use it.

   **Why this is non-negotiable** (rule substance, inlined so it loads in every session form — orchestrator-launched OR `claude --agent <name>`-launched; project `CLAUDE.md` §"No Technical Debt" carries the same substance and loads in both forms):

   Plan-vs-reality deviations and audit issues surfaced during gate execution must be FIXED in-session, not deferred. Logging-the-deviation-and-moving-on is the lazy half of the punt; carrying-forward as "queued for S{N+1}" is the lazy other half. **Carry-forwards are reserved for GENUINE FUTURE COMPUTATION**: a new gate, a new measurement, a new derivation with pre-registered threshold and machinery pin — items satisfying the 4-field test (what/inputs/gate/effort). Carry-forwards are NEVER for hygiene observations on already-correct artifacts, NEVER for registry-status promotions, NEVER for rule-file extensions, NEVER for registry edits, NEVER for canonical_constants.py single-value promotions, NEVER for cross-link fixes, NEVER for audit-script regex extensions, NEVER for methodology-wave-allowlist appends.

   The wave-synthesis section must DISTINGUISH "process observations (closed in-session, NOT propagating)" from "carry-forward computations (genuine future work, propagating)". Do not merge them. Padding the second with the first inflates the forward queue with non-actionable items that get lost across sessions.

   Technical debt is what lazy programmers accept. The orchestrator does not accept it. When the cost of fixing-now is small (minutes) and the cost of deferring is queue inflation + cross-session ambiguity, fix now. Always.

   Therefore: every non-math item surfaced across the wave's K gates MUST be EXECUTED NOW with concrete file edits, BEFORE you mark the wave-synthesis task complete.

   **Non-math classification** (move ANY item matching to this section and EXECUTE):

   - Registry edits — status promotions (STAGE-1-CANDIDATE → STAGE-3-PERMANENT; SUGGESTION → MANDATORY at K=3), slot allocations, anchor-structure re-tags, parse-tree expansion declarations, OP-PROJ/STATE-PROJ suffix retrofits, deferred-pending sub-class tags
   - Rule-file extensions — new sub-clauses, K-counter advances, calibration corpus entries, sub-class taxonomy additions
   - `methodology-wave-allowlist.md` appends with computed `sha256_of_plan_block` (plus the registry entry per Edit-discipline item 4 of that rule)
   - `canonical_constants.py` promotions via single `update_constant(...)` call (no sub-keying ambiguity)
   - knowledge-MCP entity registrations / updates via `mcp__knowledge__.update_constant` / `update_constant`
   - Hygiene cleanups — PROVENANCE-dict fixes, missing parse-tree expansions, broken cross-links, stale-pin remediation
   - Framework housekeeping — registry index updates, cross-link pointer rows, "see also" references
   - Audit-script extensions — regex pattern additions, single-function-scope diagnostic flags

   **Procedure**: enumerate every non-math item from each gate's WP section + your own observations across the wave; for each, EXECUTE the file edit / Write / registry-write NOW; record the action with concrete `file:line` reference; check the box ONLY after the edit is on disk.

   **Output format** (one row per non-math item):

   - [x] {item description} — {action taken} — `{file/path:line-range}` — {sha-short or session anchor}

   **FORBIDDEN**: leaving any non-math item UNCHECKED; deferring non-math to "Carry-Forward Computations"; writing "queued for S{N+1}" / "TODO" / "deferred" on a non-math item.

5. **Self-audit before wave close.** Grep the WP's "Effected In-Session" subsection for unchecked `- [ ]` items. If ANY remain unchecked, return to step 4, execute them now, then re-grep. Repeat until zero unchecked boxes. Only after `grep -c '^- \[ \]'` on the section returns 0 may you mark the wave-synthesis task complete and report wave close.

6. **Housekeeping ledger write.** Alongside the WP wave-synthesis, write/update `sessions/session-{N}/session-{N}-housekeeping.md` per `.claude/templates/session-housekeeping.md`. You ARE the final agent for this wave — you hold full Edit/Write access; the housekeeping ledger write happens at THIS step. The template specifies the §A-E partition and the dual-write discipline. Effected-In-Session items from step 4 mirror to §A; Q2-class carry-forwards from the WP CF section (per the template's Q2 marker test) mirror to §B/§C/§D with matching `CF-S{N+1}-HK-{n}` identifier; pre-compute shell waves go in §E. Follow the template.

   **FORBIDDEN**: omitting the housekeeping write; breaking the dual-write discipline.

## Safety rules

1. **Task list discipline.** Never skip, reorder, or collapse the compute+update pair. The two-step structure is the skill's primary mechanism.
2. **Single writer.** The main agent is the sole writer for the WP during this skill's run. No concurrent edits from other sessions.
3. **Verdict semantics.** Cross-reference `.claude/rules/math-scripts.md` — exit 0 for PASS/FAIL/INFO, FAIL is a valid scientific result not an agent failure, no iterate-until-PASS.
4. **Verdict file path.** Canonical at `computations/session-{N}/s{N}_gate_verdicts.txt`. Never `computations/_shared/...`, `sessions/session-{N}/...`, or `sessions/session-plan/...`.
5. **No subagent spawning — agent-ownership-takeover discipline (Phase 2 step 2).** Plans designating specific agents (e.g., `Agent: volovik-superfluid-universe-theorist`) DO NOT cause the solo runner to spawn that agent via the Agent tool. The solo runner TAKES OWNERSHIP of every gate; the designated agent's research corpus is loaded for context per Phase 2 step 2, but the agent itself is NEVER invoked through Agent-tool dispatch during this skill's run. Agent tasking has known breaking-bug modes (parallel-writer races on shared WPs, stuck Edit-retry loops, transcript-resume edge cases) that solo execution avoids by construction; the user has explicitly preferred avoiding agent tasking. If a gate genuinely requires isolation or heavy context that solo cannot supply even with corpus-loaded context, halt with diagnostic — the user chose solo deliberately; switching to coordinate mid-run is not the skill's job.
6. **Effected-In-Session is NON-NEGOTIABLE (Phase 3 steps 4-5).** Every non-math item surfaced in the wave MUST be executed by the orchestrator with concrete file edits before the wave-synthesis task is marked complete. Non-math items deferred to the next session are FORBIDDEN per project root `CLAUDE.md` §"No Technical Debt" (the full rule substance is also inlined in Phase 3 step 4 above, so it loads regardless of session-launch form). Only items satisfying the 4-field math test (what/inputs/gate/effort) propagate forward as carry-forwards. Phase 3 step 5 self-audit ENFORCES this: `grep -c '^- \[ \]'` on the "Effected In-Session" subsection must return 0 before wave close. This  sessiond does NOT close until all non-math items are executed with concrete edits, and the wave-synthesis task is marked complete. No housekeeping entries are carried forward or planned - they are taken  care of before this task can be completed.


## Error handling

| Condition | Action |
|:----------|:-------|
| PLAN file missing | Stop, report path |
| WP file missing | Stop, report path |
| `--start n` but earlier gate still pending | Stop, report which gates need filling first |
| Python script crash (non-zero exit) | TaskUpdate → blocked, write diagnostic into pending block, stop |
| Verdict-file append fails | Stop, report, do NOT proceed to update task |
| Update task but §W{i}-{n} pending blocks already gone (gate was filled by another process) | TaskUpdate → completed with a one-line "pre-filled" note, proceed |
| Duplicate `audit_sha256` detected in Phase 3 | Report the duplicate, flag the producing script for hardcoded-SHA bug, do not block wave close |
| User interrupts | Task list persists in TaskList state. Resume via `/rclab-solo <plan> --start <next-pending-n>`. |

## Relationship to other skills

- `/rclab-coordinate` — parallel-subagent variant of the same role. Pick based on whether you want per-gate context isolation (coordinate) or one reasoning thread (solo).
- `/rclab-plan` — produces the wave plans and WP shells this skill consumes.
- `/rclab-investigate` — runs after wave close on the filled WPs to generate the next session's workshop-schedule campaign.
