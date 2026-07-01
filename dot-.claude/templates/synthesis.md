# Synthesis Report Template

```markdown
# Session {session-id} Synthesis: {Title}

**Date**: {today}
**Agent**: {agent-type} ({short-name})
**Source Documents**:
{bulleted list of source doc paths}

---

## I. Session Outcome

{2-3 sentence verdict. Lead with the most consequential result. State gate pass/fail if applicable.}

---

## II. Key Results

{For each major finding, one subsection:}

### {Result Title}

**Result**: {the number or theorem, then classification: PHONONIC / GEOMETRIC / PARTICLE / NON-PHONONIC}

{2-3 paragraphs: what was computed, what it means, structural implications.}

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|

{If no gates in source docs, omit this section.}

---

## IV. Structural Implications

{What these results mean for the framework. Constraint map updates. What opened, closed, shifted.}

---

## V. Carry-Forward Computations

**MANDATORY — this section is the PRIMARY input to the next session's planning. Narrative recommendations ("further work needed") are NOT acceptable.** Produce a numbered list where EVERY entry has all four fields:

```
V.N. <One-line title>
   - **What**: specific computation (equation, method, output variable)
   - **Inputs**: data/constants/files needed to run (cite canonical_constants names where applicable)
   - **Gate**: which pre-registered gate it feeds, or the new gate ID it creates with PASS/FAIL/INFO thresholds
   - **Effort**: hours or agent-session count (e.g., "2-3 hours, 1 agent session")
```

At minimum: one entry per finding / eliminated mechanism / untested adjacency identified in Sections II-IV. An entry without all four fields fails the synthesis contract.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
```
