# Workshop Document Template

Build the FULL skeleton before launching any agent. Replace variables in braces.
All `*[NOT STARTED]*` placeholders are filled by agents during execution.

```markdown
# Session {session-id} Workshop: {Agent-A-Short} x {Agent-B-Short}

**Date**: {today}
**Format**: Iterative 2-agent workshop ({N} rounds, {N*2} turns)
**Agents**: {agent-a-short} ({agent-a-type}), {agent-b-short} ({agent-b-type})
**Source Documents**:
{bulleted list of source doc paths}

**Focus Topics**:
{numbered list from --context, if provided}

---

## Round 1 — {Agent-A-Short}: Opening Analysis

{For each focus topic, create a labeled subsection:}

### {A-initial}1: {Focus Topic 1}

*[NOT STARTED]*

### {A-initial}2: {Focus Topic 2}

*[NOT STARTED]*

{Continue for all focus topics, then add:}

### {A-initial}N: Cross-Cutting Observations

*[NOT STARTED]*

---

## Round 1 — {Agent-B-Short}: Response & Cross-Synthesis

### Part 1: Response to {Agent-A-Short}'s Sections

{For each of Agent A's sections, create a response subsection:}

#### Re: {A-initial}1 — {Focus Topic 1}

*[NOT STARTED]*

{Continue for all sections.}

### Part 2: Original Analysis

#### {B-initial}1: {Agent B's Perspective Title}

*[NOT STARTED]*

#### {B-initial}2: {Further Analysis}

*[NOT STARTED]*

#### {B-initial}3: Questions for {Agent-A-Short}

*[NOT STARTED]*

---

{For rounds 2+, repeat this pattern per round:}

## Round {r} — {Agent-A-Short}: Follow-up

### CONVERGENCE

*[NOT STARTED]*

### DISSENT

*[NOT STARTED]*

### EMERGENCE

*[NOT STARTED]*

### QUESTIONS

*[NOT STARTED]*

---

## Round {r} — {Agent-B-Short}: Cross-Synthesis

### CONVERGENCE

*[NOT STARTED]*

### DISSENT

*[NOT STARTED]*

### EMERGENCE

*[NOT STARTED]*

{On the FINAL round only, Agent B also fills:}

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | {topic} | {A-initial}1, Re:{A-initial}1 | *pending* | |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

*[To be filled after final round]*

## Wrap-Up — Workshop Impact Summary

{MANDATORY — Agent B fills this in the FINAL round alongside the Verdict table.}

### What Changed
{1-3 bullets: what this workshop CHANGED about the framework's state. New structural results, resolved tensions, revised estimates, discovered signatures.}

### What Holds
{1-3 bullets: what SURVIVED the workshop exchange. Results that were challenged and defended, or confirmed from both perspectives.}

### What Breaks or Strains
{1-3 bullets: what the workshop THREATENS or leaves unresolved. If nothing, say "Nothing identified."}

### Carry-Forward Computations (MATH ONLY — propagate to S{N+1})

**Discriminator (4-field test)**: an item belongs in THIS section iff it satisfies ALL FOUR fields. If ANY field cannot be filled, the item is NOT a math carry-forward — move it to "Effected In-Session" below and execute it NOW.

- **What**: the specific equation / numerical observable / structural theorem to compute
- **Inputs**: the data files, canonical constants, upstream gates needed
- **Gate**: the pre-registered PASS / FAIL / INFO threshold with explicit tolerance
- **Effort**: estimated wave-equivalents (compute time)

{Numbered list — only items satisfying ALL FOUR fields. This list is the PRIMARY input to /rclab-plan for the next session.}

### Effected In-Session (NON-MATH — completed by YOU, the final agent, BEFORE TERMINATING)

**MANDATORY — NON-NEGOTIABLE.** Per CLAUDE.md "No Technical Debt", `feedback_fix-in-session-never-defer.md`, and 50+ sessions of evidence that deferred non-math items become orphans: every non-math item this workshop surfaces MUST be EXECUTED by you (the final agent, R{N} Turn B) NOW, with concrete file edits, BEFORE the workshop document is considered complete.

**Non-math classification covers (non-exhaustive)**:
- Registry edits — status promotions (STAGE-1-CANDIDATE → STAGE-3-PERMANENT, SUGGESTION → MANDATORY), slot allocations, anchor-structure re-tags (PRIMARY+CONFIRMATION → SOURCE-DOUBLE-CITE-CO-PRIMARY), parse-tree expansion declarations, OP-PROJ/STATE-PROJ suffix retrofits, deferred-pending sub-class tags
- Rule-file extensions — new sub-clauses, K-counter advances, calibration corpus entries, sub-class taxonomy additions, audit-script extension queues
- Methodology-wave-allowlist appends with computed sha256_of_plan_block
- canonical_constants.py promotions via `update_constant(...)` (single-value, no sub-keying ambiguity)
- knowledge-MCP additions / updates via `mcp__knowledge__.update_constant` / `update_constant` / entity registration
- Hygiene cleanups — PROVENANCE-dict fixes, missing parse-tree expansions, broken cross-links, stale-pin remediation, anchor-id mismatches
- Framework housekeeping — registry index updates, cross-link pointer rows, "see also" references, registry slot-pointer fixes
- Audit-script extensions — regex pattern additions, new diagnostic flags (when the edit is single-function-scope)

**Procedure**:
1. Enumerate EVERY non-math item surfaced across all rounds (CONVERGENCE / DISSENT / EMERGENCE / QUESTIONS / Wrap-Up sub-sections).
2. For each item, EXECUTE the file edit / Write / registry-write NOW using your Edit / Write tools.
3. Record what you did with a concrete file:line reference and (where applicable) the resulting SHA-short.
4. Check the box ONLY after the edit is on disk.

**Output format** (one row per non-math item):

- [x] {item description} — {action taken} — `{file/path:line-range}` — {sha-short or session anchor}
- [x] {item} — {action} — `{path}` — {anchor}

**FORBIDDEN**:
- Leaving any non-math item UNCHECKED.
- Deferring non-math items to "Carry-Forward Computations".
- Listing non-math items as "next-session" work / "queued" / "TODO" / "deferred".
- Writing placeholder text in lieu of executing the edit.

If you find yourself wanting to write "queued for S{N+1}" on a non-math item: STOP. Execute it now. The project has 50+ sessions of evidence this concept has not been applied; you are the structural fix.

### Closing Line
{One sentence. The single most important thing from this workshop.}
```
