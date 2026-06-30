# Working Paper Template

The working paper is the answer log. The runtime agent writes its gate's completed entry into this file using the same structure as the S84 examples below.

## At dispatch (orchestrator)

Canonical shell shape: `.claude/templates/examples/workingpaper-shell-example.md` (frozen; 10-gate dispatch shell, does not get filled in by runtime).

Write `sessions/session-{N}/session-{N}-w{W}-workingpaper.md`:

```markdown
# Session {N} Wave {W} — {WAVE_TITLE} (Results Working Paper)

**Session**: {N} | **Wave**: {W} | **Plan**: session-{N}-plan-w{W}.md | **Theme**: {THEME}

## Gate Sections

### §W{W}-1. {GATE_ID_1} ({agent-type})

**Status**: NOT STARTED
**Gate ID**: `{GATE_ID_1}`
**Trigger**: `{TRIGGER}`
**Classification**: **{CLASS}**
**Agent**: `{agent-type}`
**Hypothesis**: {one-line paraphrase from plan}

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
*(pending — for each entry in the plan's `output_artifacts:` block: confirm file exists (`ls <path>`) AND paste `grep -E '<must_contain>' <path>` output for every must_contain pattern in the entry. This block IS the per-gate completion checklist that the agent bash-verifies before TaskUpdate per `.claude/skills/rclab-coordinate/skill.md` COMPLETION CHECKLIST clause; an entry with file missing OR any must_contain regex returning empty means the gate did not properly close — orchestrator MUST then SendMessage continuation to the same agentId per `feedback_dispatch-discipline.md`. NO length or size targets per `feedback_max-effort-full-fidelity.md` — verification is purely by content presence (regex match), never by line/byte counts.)*

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: {comma-separated list of plan deliverables})*

### §W{W}-2. ...
(Repeat per gate.)

## Wave {W} Synthesis (team-lead)

## Carry-Forward Computations

## Constraint-Map Updates

## Files Produced
```

## At gate completion (runtime agent)

Replace your gate's `*(pending ...)*` blocks with the completed entry. Match the example that fits your gate type:

| Gate type | S84 example | Lines |
|:----------|:------------|:------|
| Numerical PASS / FAIL | `sessions/archive/session-84/session-84-w1-workingpaper.md` §W1-1 | 38–205 |
| Registration / META | `sessions/archive/session-84/session-84-w1-workingpaper.md` §W1-6 | 780–981 |
| FAIL with remediation | `sessions/archive/session-84/session-84-w2-workingpaper.md` §W2-11 | 24–138 |
| INFO (PRU Class 8) | `sessions/archive/session-84/session-84-w10-workingpaper.md` §W10-110 | 54–106 |
| ABORTED (cascade) | no gate entry; record state change in Constraint-Map table | — |

## At wave close (team-lead)

Write the Wave {W} Synthesis section. Structure: `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`.

Write the **Carry-Forward Computations** section: one `### {CF-ID} — {one-line title}` sub-heading per genuine future-work item, each with a 4-field-spec table (What / Inputs / Gate / Effort). Reference example: `sessions/archive/session-89/session-89-w2-workingpaper.md` §"Carry-Forward Computations" (4 CFs; CF-W2-1-RETRY / CF-W2-2-DEFERRED / CF-W2-4-DEFERRED / CF-A40-FAIL-ALTERNATIVE-CHIRALITY). Per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`: this section is the canonical CF source consumed by `/rclab-plan` for next-session planning per `.claude/rules/Investigating-Workshops.md`. Process observations go in Constraint-Map Updates. In-session hygiene closures go in `sessions/session-{N}/session-{N}-housekeeping.md §A` (the per-session canonical Q2 ledger; see next paragraph) — neither belongs in this CF section per `feedback_fix-in-session-never-defer.md`.

Write/update **`sessions/session-{N}/session-{N}-housekeeping.md`** per `.claude/templates/session-housekeeping.md`. The template specifies the §A-E partition and the dual-write discipline. In-session fixes effected this wave mirror to §A; Q2-class carry-forwards from this WP's "Carry-Forward Computations" section mirror to §B/§C/§D with matching `CF-S{N+1}-HK-{n}` identifier; pre-compute shell waves go in §E. Follow the template.

Append the session-level Constraint-Map Updates and Files Produced tables: same file, lines 1098–1134.

## Rules

1. Verdict line is canonical at `computations/session-{N}/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md`; the working paper mirrors it.
2. One writer per gate. Team-lead writes synthesis + carry-forward-computations + constraint-map + files-produced sections only.
3. Every completed gate entry includes the **MCP Pre-Compute Audit** block listing the `mcp__knowledge__*` queries executed before compute and their salient returns, per `.claude/rules/knowledge-index-usage.md`. An entry without this block is incomplete — the MCP query is the compute procedure's first action (see rclab-solo Phase 2 step 3), not a post-hoc citation.
4. **Every wave-close MUST produce a `## Carry-Forward Computations` section** with one 4-field spec (What / Inputs / Gate / Effort) per genuine future-work item, per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md` + `.claude/rules/Investigating-Workshops.md` §"Cross-references". The section is the canonical CF source consumed by `/rclab-plan`; it MUST be a top-level `## ` heading (not embedded inside synthesis prose or scattered across gate sections), so `/rclab-plan` can grep for it as a distinct block. Process observations and in-session hygiene DO NOT belong here per `CLAUDE.md` Wave-synthesis-discipline clause ("Do not merge the two sections"). Empty CF section is acceptable IFF the wave produced zero genuine future-work items; in that case write a single line stating "No carry-forwards: all wave outcomes closed in-session" so the absence is intentional rather than an oversight.

## Anti-pattern

Do not use `<!-- Runtime agent fills: ... -->` stubs — they survive into the final document and turn the paper into a plan-echo instead of an answer log. Observed failure mode in the initial S85 dispatch shells (pre-2026-04-23 rebuild): 40+ stub comments per wave survived runtime dispatch because agents read them as permanent scaffolding rather than placeholders. The pending-block pattern (`*(pending — include: ...)*`) replaces the whole block on completion; stub comments ask the agent to fill in-place around them, which consistently fails.
