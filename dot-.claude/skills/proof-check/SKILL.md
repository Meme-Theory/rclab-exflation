---
name: proof-check
description: Structural review of a proof or derivation — checks step justification, variable definitions, limiting cases, dimensional consistency, and canonical-source traceability
argument-hint: <path-to-proof-file> | --section <file>:<section-heading> | --inline
---

# /proof-check — Structural Proof Review

This skill performs a **structural** audit of a proof or derivation. It does not prove new theorems. It flags weaknesses in existing proofs so you can remediate them before the result is registered as canonical.

## Usage

```
/proof-check sessions/archive/session-84/session-84-w1-workingpaper.md
/proof-check --section sessions/archive/session-74/session-74-mack-landau-workshop.md:III.B
/proof-check --inline
```

- `<path>`: read the whole file and extract every claimed proof/derivation block.
- `--section <path>:<heading>`: audit one section only (heading matched case-insensitive, prefix OK).
- `--inline`: the proof text is included later in the same user prompt.

## What this skill checks

For every step of the proof (numbered lines, bullet points, or equation-labeled blocks):

| Check | Pass condition | Fail message |
|:------|:---------------|:-------------|
| **S1. Step justification** | Each step cites (a) a prior step number, (b) a named theorem/lemma, or (c) a definition/axiom. | `"Step N has no justification"` |
| **S2. Variable scope** | Every symbol introduced before first use, with a declaration or citation to canonical constants. | `"Symbol X used before definition"` |
| **S3. Limiting cases** | For any inequality, monotonicity, or bound: degenerate limits (zero, infinity, boundary) are checked or explicitly excluded. | `"Limiting case not verified: X → 0/∞"` |
| **S4. Dimensional consistency** | Every equation's LHS and RHS have the same units (mass, length, time, dimensionless). | `"Dimension mismatch at step N"` |
| **S5. Canonical constants** | Every named constant (`M_KK`, `tau_fold`, etc.) is pulled from `canonical_constants.py` via the `knowledge` MCP, not hardcoded. | `"Constant X not in canonical_constants.py"` |
| **S6. Substitution chain** | Any sign/direction/threshold claim has an explicit substitution chain (definition → substitution → simplification → direction) per `.claude/rules/math-scripts.md`. | `"Sign claim at step N lacks substitution chain"` |
| **S7. Sole-source avoidance** | The proof doesn't rely on an agent-memory or a single unpublished working paper; if it does, flag as PROVISIONAL. | `"Evidence chain rests solely on agent memory"` |

## How to execute this skill

1. **Read the target file**. If `--section` was given, locate the heading with Grep and read that slice only.

2. **Locate proof blocks**. Look for these markers:
   - Explicit `Proof.` / `Q.E.D.` delimiters
   - `Lemma`, `Theorem`, `Proposition`, `Claim` headings followed by a derivation
   - Equation chains where successive lines derive from predecessors
   - Gate-verdict `Substitution chain:` blocks (project-specific pattern)

3. **Enumerate steps**. Split each block into ordered steps. Each equation, sentence, or bullet is a step.

4. **Run the 7 checks**. For each step, emit one row per failing check. PASS steps need no row.

5. **Cross-check constants**. For every named constant you find, call the knowledge MCP:
   ```
   mcp__knowledge__get_constant(name=<constant>)
   ```
   If the constant doesn't exist in `canonical_constants.py`, flag S5.

6. **Produce the report**. Single markdown output with this structure:

   ```
   # Proof check: <file/section>
   
   ## Summary
   - Steps audited: N
   - Issues found: K  (by severity: BLOCKER=x, MAJOR=y, MINOR=z)
   - Overall verdict: CLEAN | MINOR | MAJOR | BLOCKER
   
   ## Step-by-step
   
   | # | Step (first 80 chars) | Check | Severity | Finding |
   |--:|:----------------------|:------|:---------|:--------|
   | 3 | "By monotonicity of a_2…" | S1 | MINOR | No citation for "monotonicity of a_2" |
   | 7 | "tau → 0 gives Delta = 0"  | S3 | BLOCKER | Limit tau → 0 not verified — proof needs finite-bound |
   
   ## Recommended actions
   1. <specific remediation for each BLOCKER/MAJOR>
   2. …
   ```

## Severity rubric

- **BLOCKER**: the step is wrong OR the proof fails without it. Proof cannot be registered.
- **MAJOR**: the step is plausibly wrong, the justification is circular, or a case is missing. Proof is PROVISIONAL pending rework.
- **MINOR**: cosmetic — missing citation for a standard result, unclear notation, a "clearly" that isn't clear. Proof stands but should be tightened.

## Severity guidance when the substrate picture is relevant

Per `.claude/rules/phononic-framing.md`: a proof that explains a substrate result by invoking GR (container thinking) is at least **MAJOR**. The direction of explanation must flow FROM the substrate TOWARD emergent physics, never the reverse. If you detect container-thinking, note it explicitly in the finding column.

## Do NOT do

- Do NOT try to fix the proof. Only report.
- Do NOT re-derive the substantive math yourself. The check is structural.
- Do NOT run numerical computations unless needed for S3 (limiting cases).
- Do NOT defer a finding with "probably fine". Either call it PASS or flag it with a severity.
