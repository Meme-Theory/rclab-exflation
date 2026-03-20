# Meeting-Minutes Format Generations

**Generated**: 2026-02-21
**Source**: Exploration agents scanning all 80+ files in `sessions/` and `tier0-computation/`
**Purpose**: Complete inventory of markdown header patterns and content formats used across the project, organized by entity type and chronological generation. Reference for extractor regex maintenance.

---

## Table of Contents

1. [Closed Mechanism / Closure Registries](#1-closed-mechanisms--closure-registries)
2. [Gate Verdicts](#2-gate-verdicts)
3. [Proven Theorems / Permanent Results](#3-proven-theorems--permanent-results)
4. [Open Channels / Escape Routes](#4-open-channels--escape-routes)
5. [Probability Trajectory](#5-probability-trajectory)
6. [Content Format Types](#6-content-format-types)

---

## 1. Closed Mechanism / Closure Registries

### Generation 1 — Sessions 1-17 (2026-02-11 to 2026-02-14)

Informal narrative. Closure vocabulary not yet systematized.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `### Volume Exflation: Closed Cleanly` | giants-planck-geometry.md | Narrative prose |
| `### Sagan's Coupling Drift Channel — Closed` | giants-planck-geometry.md | Narrative prose |
| `### VI. Binding Thermodynamic Failure Criteria` | session-16-round-1e-hawking-sagan.md | Numbered list + table `\|Verdict\|Condition\|Weight\|` |
| `### Binding Failure Criteria for Round 2 Computations` | session-16-round-1e-hawking-sagan.md | Numbered list with BF/prob-shift |
| `# V. PRE-REGISTRATION DOCUMENT (Binding Failure Criteria)` | session-16-final.md | Numbered criteria sections with pass/fail tier tables |
| `### Pass/Fail Criteria` | session-16-round-2d-giants-eval-ii.md | Table `\|Verdict\|Condition\|Weight\|` |
| `## Gate Status Summary` | session-17b-verification.md | Table `\|Gate\|Status\|Checks\|Verdict\|` |
| `### Gate Verdicts` | session-17b-verification.md | Bullets: `**SP-2**: CLEARED`, `**D-2**: CLEARED` |

**Pattern**: H3 headers with colon + status label appended ("Closed Cleanly", "— Closed"). No "CLOSED" keyword. Tables use "Verdict/Condition/Weight" columns.

---

### Generation 2 — Session 18 (2026-02-15)

First formal closure assessment.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `## Constraint Condition Assessment` | session-18-veff-convergence.md | Table `\|Condition\|Result\|Status\|` with FATAL/PASS |
| `### What is NOT closed` | session-18-veff-convergence.md | Bullet list (3 items) |
| `### What is NOT closed` | session-18-veff-convergence.md | Bullet list (3 items) |

**Pattern**: First use of `## Constraint Condition Assessment`. Status column uses `**DECISIVE CLOSURE**` for closes. NOT yet using "CLOSED."

---

### Generation 3 — Session 19d (2026-02-15)

Closure verdict appended directly to headers.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `### D-1: Boson/Fermion E_proxy Separation Gate (sim + kk/tesla validation) -- CLOSED` | session-19d-casimir-energy.md | Table `\|Quantity\|Value\|CLOSURE threshold\|` + narrative |
| `## I. WHAT HAPPENED: THE CLOSED AND THE LOOPHOLE` | session-19d-synthesis.md | Narrative prose |
| `### The Three Failures Were One Failure` | session-19d-synthesis.md | Narrative prose |
| `### Original Closure/Confirm Conditions (from Session Prompt)` | session-19a-spectral-diagnostics.md | Numbered list with PASS/CLOSURE labels |

**Pattern**: First use of `-- CLOSED` suffix on H3 headers. H3 format: `### [Gate-ID]: [Description] -- CLOSED`.

---

### Generation 4 — Sessions 20a/20b/20c (2026-02-19)

Canonical Constraint Tables introduced. Researchers comment on closes.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `## I. VERDICT: CLOSED` | session-20b-lichnerowicz.md | Bold statement + pipeline table |
| `## VII. MINIMUM SEARCH RESULT: CLOSED` | session-20b-lichnerowicz.md | Table of tau vs V_total values |
| `### Combined 20a/20b Verdict` | session-20c-synthesis.md | **First canonical Constraint Table**: `\|Session\|Mechanism\|Result\|` with "CLOSED —" in Result column |

**Researcher collab pattern** (all 15 session-20b-*-collab.md files):

| Header pattern | Content Format |
|:---------------|:---------------|
| `### 2.1 The CLOSURE Verdict Is Sound` | Narrative prose |
| `### 2.1 Verdict on Perturbative Stabilization: Definitive Closure` | Narrative prose |
| `### 2.1 The CLOSURE Verdict Is Correct for Perturbative Stabilization` | Narrative prose |
| `### 2.2 The CLOSURE Verdict Does Not Apply to Non-Perturbative Mechanisms` | Narrative prose |
| `### 2.2 What the CLOSED Does NOT Closure` | Narrative prose |
| `### 2.2 What the CLOSED Does NOT Invalidate` | Narrative prose |

**Pattern**: 3-column table `Session | Mechanism | Result` with "CLOSED —" in Result. This is the canonical Session 20c format. Collab files use prose commentary only.

---

### Generation 5 — Sessions 21b/21c (2026-02-19 to 2026-02-20)

Tiered Constraint Gate tables. Structural closes as H3 commentary.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `### IV.5 DESI Constraint Gates (pre-registered)` | session-21b-valar-plan.md | 5-column table `\|Outcome\|Criterion\|BF\|Action\|` |
| `### IV.6 Additional Constraint Gates (einstein addenda)` | session-21b-valar-plan.md | Bullet list: `- **K-FR-1**: ...` |
| `## VI. B-5: Constraint Gate REGISTRY + BAYESIAN FRAMEWORK` | session-21b-valar-plan.md | Section header |
| `### VI.1 Complete Closure Gate Registry` | session-21b-valar-plan.md | Per-computation `#### Computation N:` with 4-column tables |
| `### XI.8 BCS Constraint Gates K-BCS-1 and K-BCS-2` | session-21b-valar-plan.md | Narrative prose |
| `### XI.9 Updated Constraint Gate Registry` | session-21b-valar-plan.md | Amendment bullets |
| `### II.1 Nominal Constraint Gate Classification` | session-21c-phase0-synthesis.md | Table `\|Computation\|Result\|Nominal Verdict\|BF\|Prob Shift\|` |
| `### II.2 Coupling-Adjusted Classifications (baptista uncertainty quantification)` | session-21c-phase0-synthesis.md | Table `\|Computation\|Coupling Impact\|Adjusted Verdict\|` |

**Researcher collab pattern** (all session-21c-*-collab.md files):

| Header pattern | Content Format |
|:---------------|:---------------|
| `### 2.1 S_signed Structural Closure: SOUND` | Narrative prose |
| `### 2.1 S_signed STRUCTURAL CLOSURE: Correct and Irreversible` | Narrative prose |
| `### 2.1 S_signed STRUCTURAL CLOSURE: Sound and Permanent` | Narrative prose |
| `### 2.1 S_signed STRUCTURAL CLOSURE: Sound and Final` | Narrative prose |
| `### P0-3: S_signed STRUCTURAL CLOSURE` | Narrative prose |
| `### 2.3 What Is Closed: All Perturbative Spectral Routes` | **Bullet list** of closed mechanisms |
| `### 2.3 Pre-Registered Constraint Gate Accounting` | Table |

**Pattern**: Tiered `Tier | Criterion | BF | Prob shift` tables per computation. Collab files use "STRUCTURAL CLOSURE" in H3 headers.

---

### Generation 6 — Session 22 Arc (2026-02-20)

Definitive Constraint Gate Registry. PROVEN/CLOSED/OPEN triptych.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `### II.1 Constraint Gate Verdicts` | session-22a-synthesis.md | 6-column table `\|Computation\|Numerical Result\|Constraint Gate Criterion\|Verdict\|BF\|Prob Shift\|` |
| `### PA-2: Kosmann-Lichnerowicz Coupling Matrix Elements (baptista) — STRUCTURAL CLOSURE` | session-22b-synthesis.md | Narrative prose |
| `### III.4 PB-2 and PB-3 Gate Verdicts` | session-22b-synthesis.md | Table `\|Gate\|Result\|Verdict\|BF\|Prob shift\|` |
| `### VIII.3 Stokes Mechanism closed by Block-Diagonality` | session-22b/22c-synthesis.md | Narrative prose |
| `## II. Definitive Constraint Gate Registry (All Sessions)` | session-22d-synthesis.md | Major section header |
| `### Perturbative Gates (Sessions 17-22b) — ALL CLOSED` | session-22d-synthesis.md | Table `\|Gate\|Session\|Result\|Status\|` with "CLOSED" in Status column |
| `### Non-Perturbative Gates (Sessions 22c-22d)` | session-22d-synthesis.md | Table `\|Gate\|Session\|Result\|Status\|BF (panel)\|BF (Sagan)\|` |
| `### Pre-Registered Constraint Conditions — Status` | session-22d-synthesis.md | Bullet checklist under `**HARD CLOSES**`, `**CONDITIONAL CLOSES**`, `**DECISIVE OPENS**` |
| `### What Is Definitively Closed` | session-22d-synthesis.md | Narrative prose |
| `### CLOSED (perturbative, closed gates — algebraic theorem or decisive closure)` | session-22d-synthesis.md | Bullet list |
| `## VI. Complete Closure Gate Registry` | session-22-master-synthesis.md | Section header |
| `### Perturbative Mechanisms (all sessions) — ALL CLOSED` | session-22-master-synthesis.md | 3-column table `\|Mechanism\|Session\|closure reason\|` (CLOSED implicit in header) |
| `### Session 22 Constraint Gate Verdicts (pre-registered)` | session-22-master-synthesis.md | 6-column table |
| `### CLOSED (perturbative, closed by theorem or decisive closure)` | session-22-master-synthesis.md | Bullet list |
| `### III.4 The Higgs-Sigma Closure (C-1): STRUCTURAL CLOSURE, Trap 3 Discovered` | session-22-master-synthesis.md | Narrative prose |

**Sagan verdict pattern**:

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `### Session 22b: Coupled Diagonalization (2 gate verdicts)` | session-22-sagan-verdict.md | Bullet list of verdicts |
| `### Scenario F: Everything fails (hard-closure case)` | session-22-sagan-verdict.md | Narrative scenario analysis |

**Pattern**: 4-column `Gate | Session | Result | Status` table with "CLOSED" in Status. First use of the PROVEN/CLOSED/OPEN triptych as `### PROVEN ...` / `### CLOSED ...` / `### OPEN ...` subsections.

---

### Generation 7 — Session 23 Arc (2026-02-20)

Narrative gate headers with verdict inline. Numbered closure registries.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `## II. Constraint Gate Verdicts` | session-23a-synthesis.md | Section containing narrative subsection per gate |
| `### II.1 K-0: Kosmann Matrix Elements Nonzero — PASS` | session-23a-synthesis.md | Bullet list of numbers |
| `### II.2 K-1e: Gap Equation Trivial at mu = 0 — DECISIVE CLOSURE` | session-23a-synthesis.md | Table `\|Criterion\|M_max range\|Factor below critical\|Verdict\|` + narrative |
| `### II.3 K-2: Basis Convergence — N/A` | session-23a-synthesis.md | Narrative prose |
| `### II.4 Self-Doping Energy Balance — NOT FAVORABLE` | session-23a-synthesis.md | Narrative prose |
| `## VI. Why the BCS Mechanism Failed` | session-23a-synthesis.md | Narrative prose |
| `## XI. The Venus Rule` | session-23a-synthesis.md | Narrative prose |
| `## I. The K-1e Closure: Verified and Final` | session-23b-synthesis.md | Narrative prose |
| `### I.3 Why BCS Failed: The Spectral Gap Problem` | session-23b-synthesis.md | Narrative prose |
| `### III.1 Complete Closure Registry (17 Mechanisms Closed)` | session-23b-synthesis.md | **Numbered table**: `\|#\|Mechanism\|Session\|closure reason\|` (4 columns) |
| `## V. Constraint Gate Registry (Updated)` | session-23b-synthesis.md | Table `\|Gate\|Result\|Verdict\|BF\|Session\|` (5 columns) |
| `### Pre-Registered Constraint Gates for 23c` | session-23b-synthesis.md | Table `\|Gate\|Threshold\|Closure\|Pass\|` |
| `### III.1 Closed Mechanism: Complete Registry (Post-K-1e)` | session-23-sagan-verdict.md | Numbered table `\|#\|Mechanism\|Session\|closure reason\|` |
| `## VIII. PRE-REGISTERED Constraint GateS: UPDATED REGISTRY` | session-23-sagan-verdict.md | Table `\|Gate\|Result\|Verdict\|Session\|` (BF in Verdict cell) |
| `### III.2 The Scenario Constraint Chain (Post-Synthesis Collaboration)` | session-23c-synthesis.md | Narrative — "Scenario C: CLOSED" as inline bold |
| `### III.3 Final BF Table` | session-23c-synthesis.md | Table `\|Scenario\|Mechanism\|BF\|Status\|` with "CLOSED" in Status |
| `### IX.3 Pre-Registered Constraint Gates for Session 24` | session-23c-synthesis.md | Table of future gates |

**Pattern**: Individual gates presented as `### II.N [Gate-ID]: [Description] — [VERDICT]` narrative subsections (not table rows). Closure registries use numbered 4-column tables with boldened newest entries. First use of `Complete Closure Registry (N Mechanisms Closed)` header.

---

### Generation 8 — Session 24 (2026-02-21)

Canonical final format. Sagan adjudication column.

| Header (verbatim) | File | Content Format |
|:-------------------|:-----|:---------------|
| `## I. Gate Table` | session-24a-synthesis.md | Table `\|Gate\|Condition\|Result\|Verdict\|` |
| `## I. Gate Table (24a Results with Sagan Adjudication)` | session-24b-synthesis.md | 6-column table adding Sagan adjudication + BF |
| `### II.5 Constraint Registry: 18 Closed Mechanism, 8:1 Closure-to-pass ratio` | session-24b-synthesis.md | **Numbered table**: `\|#\|Mechanism\|Session\|Closure Reason\|BF\|` (5 columns) |
| `### II.6 Baloney Detection Kit: Lakatos Warning` | session-24b-synthesis.md | Table `\|Session\|Failed Mechanism\|Post-Hoc Reinterpretation\|` |
| `## VI. UPDATED Constraint Registry` | session-24-sagan-verdict.md | Section header |
| `### VI.1 Complete Closure Table (Post-Session 24a)` | session-24-sagan-verdict.md | Numbered table `\|#\|Mechanism\|Session\|closure reason\|BF\|` (5 columns) |
| `### VI.2 Pre-Registered Gate Tally (Updated)` | session-24-sagan-verdict.md | Table `\|Gate\|Result\|Verdict\|Session\|BF\|` with boldened newest |
| `### I.1 Gate-by-Gate Verification` | session-24-sagan-verdict.md | 7-column compliance table |

**Pattern**: Numbered 5-column Constraint Registry `# | Mechanism | Session | Closure Reason | BF` is the canonical final format. Gate tables gain Sagan adjudication and compliance columns. Latest closure always boldened.

---

## 2. Gate Verdicts

### Format A — `.txt` GATE blocks (tier0-computation)

```
GATE V-1: V_spec Monotone — Constraint Condition: No minimum at any rho in [0.001, 0.5]
  Closes if: V_spec monotonically increasing for all rho
  Result: Monotonically increasing for ALL 50 rho values tested
  VERDICT: **CLOSED**
```

**Files**: `s24a_gate_verdicts.txt`
**Gate IDs**: V-1, V-3, R-1, AC-1

### Format B — `.txt` inline verdicts (tier0-computation)

| Pattern | File | Gate IDs |
|:--------|:-----|:---------|
| `VERDICT: PASS` | s21c_gauss_bonnet.txt | P0-5 |
| `VERDICT: COMPELLING` | s21c_T_double_prime_result.txt | P0-2 |
| `*** VERDICT: INTERESTING ***` | s22a_euclidean_action.txt | QA-5 |
| `GATE VERDICT: COMPELLING (BF=8, +4-6 pp)` | s22c_bcs_channel_scan.txt | F-1 |
| `GATE VERDICT: INTERESTING (+2-3 pp)` | s22c_instanton_action.txt | L-1 |
| `OVERALL VERDICT:` | s23a_gap_equation_results.txt | K-1e |

**Section headers in .txt files**:
- `PART N: PRE-REGISTERED GATE VERDICTS`
- `N. Constraint Gate VERDICTS` / `N. Constraint Gate VERDICT`
- `--- Gate L-1a: [description] ---`

### Format C — Narrative headers with gate ID + verdict (synthesis .md)

```
### II.1 K-0: Kosmann Matrix Elements Nonzero — PASS
### II.2 K-1e: Gap Equation Trivial at mu = 0 — DECISIVE CLOSURE
### D-1: Boson/Fermion E_proxy Separation Gate -- CLOSED
### PA-2: Kosmann-Lichnerowicz Coupling Matrix Elements — STRUCTURAL CLOSURE
```

**Sessions**: 19d, 22b, 23a

### Format D — 4-column gate tables (synthesis .md)

```
| Gate | Condition | Result | Verdict |
| **V-1** (V_spec Monotone) | No minimum at any rho | Monotonically increasing | **CLOSED** |
```

**Variants**:
- 4-column: `Gate | Condition | Result | Verdict` (24a)
- 5-column: `Gate | Result | Verdict | BF | Session` (23b)
- 6-column: `Gate | Pre-Registered Threshold | 24a Result | Classification | Sagan Adjudication | BF` (24b)
- 6-column: `Computation | Numerical Result | Constraint Gate Criterion | Verdict | BF | Prob Shift` (22a)
- 7-column: with Compliance column (24-sagan-verdict)

### Format E — Per-computation tiered tables (21b Valar plan)

```
#### Computation 1: V_IR(tau) for p+q <= 2 (A5)
| Tier | Criterion | BF | Prob shift |
| INTERESTING | ... | 3 | +3 pp |
| COMPELLING | ... | 10 | +8-10 pp |
| DECISIVE | ... | 50 | +15-20 pp |
| CLOSED | ... | 0.3 | -8-10 pp |
```

### Format F — Gate status tables (17b, 21c)

```
| Gate | Status | Checks | Verdict |
| B-2 -> SP-2 | CLEARED | 24/24 PASS | SP-2 proceeds |
```

### Verdict Vocabulary (all formats)

`CLOSED`, `DECISIVE CLOSURE`, `STRUCTURAL CLOSURE`, `MARGINAL CLOSURE`, `CLOSED`, `PASS`, `TRIVIAL PASS`, `FAIL`, `DOES NOT CLOSE`, `INCONCLUSIVE`, `COMPELLING`, `INTERESTING`, `NEUTRAL`, `CONDITIONAL`, `UNCERTAIN`, `CLEARED`, `CLOSED`, `OPEN`, `FATAL`, `NOT FAVORABLE`, `N/A`, `ROBUST`

### Known Gate ID Patterns

| Sessions | ID format | Examples |
|:---------|:----------|:---------|
| 17a-17c | `[BSD]-\d+` | B-2, B-3, SP-2, SP-4, D-2 |
| 18 | descriptive | "FATAL" status in table |
| 19d | `D-\d+` | D-1 |
| 20a-20b | `SD-\d+`, `L-\d+` | SD-1, L-3, L-4 |
| 21a-21c | `P0-\d+`, `A\d+` | P0-1 through P0-5, A5, A6 |
| 22a | `SP-\d+`, `QA-\d+` | SP-1 through SP-5, QA-1 through QA-5 |
| 22b | `PB-\d+`, `PA-\d+` | PB-2, PB-3, PA-2 |
| 22c | `[FLCLE]-\d+` | F-1, F-2, C-1, C-2, L-1, L-2 |
| 22d | `E-\d+` | E-1, E-2, E-3 |
| 23a | `K-\d+[a-e]?` | K-0, K-1e, K-2 |
| 24a | `[VRA]C?-\d+` | V-1, V-3, R-1, AC-1 |

---

## 3. Proven Theorems / Permanent Results

### Header Patterns (chronological)

| Header (verbatim) | File | Gen | Content Format |
|:-------------------|:-----|:----|:---------------|
| `### Clean Results (Machine Epsilon Precision)` | session-8-phase2-32dim.md | 1 | Bullet list |
| `## WHAT SURVIVES (CONFIRMED AT MACHINE EPSILON)` | session-10-phase2b-2.5.md, session-11-chirality.md | 1 | Numbered bold-bullet list |
| `### Validation (ALL PASS at machine epsilon)` | session-12-tier1-dirac.md | 1 | Bullet list |
| `## I. PROVEN RESULTS (Machine Epsilon / Parameter-Free)` | session-15-formalization.md | 1 | Numbered bullet list |
| `# VI. WHAT WE PROVED (11 Results at Machine Epsilon)` | session-16-final.md | 2 | Numbered list |
| `### TIER S: ALREADY COMPUTED (Machine Epsilon Results)` | session-16-round-2d-giants-eval.md | 2 | Prose |
| `## III. PROVEN (Machine Epsilon or Exact)` | session-17-final.md | 3 | Numbered list with inline precision values |
| `### D-1: J-Compatibility Audit — PROVEN (dirac)` | session-17a-foundation.md | 3 | Per-deliverable H3 with PROVEN tag |
| `### D-3: Mass Spectrum J-Symmetry — PROVEN (dirac)` | session-17a-foundation.md | 3 | Per-deliverable H3 with PROVEN tag |
| `## III. STRUCTURAL RESULTS (Non-Gate, Session-Permanent)` | session-22a-synthesis.md | 6 | Prose + inline quantitative |
| `## X. STRUCTURAL THEOREMS (Permanent)` | session-22b-synthesis.md | 6 | Named theorems with proof sketches |
| `## VIII. NEW STRUCTURAL THEOREMS (Permanent)` | session-22c-synthesis.md | 6 | Named theorems with corollaries |
| `### III.1 The Three Algebraic Traps (Permanent Structural Theorems)` | session-22c-synthesis.md | 6 | Table `\|Trap\|Ratio\|Origin\|Affected\|` |
| `### Structural Theorems (Permanent)` | session-22d-synthesis.md | 6 | Table `\|Theorem\|Session\|Statement\|` |
| `### PROVEN (machine epsilon or better, unaffected by any closure)` | session-22d-synthesis.md, session-22-master-synthesis.md | 6 | Bullet list |
| `## III. STRUCTURAL THEOREMS (New, Proven This Session)` | session-21c-phase0-synthesis.md | 5 | Theorem-proof format |
| `## III. Structural Findings (Permanent, Independent of Closure)` | session-23a-synthesis.md | 7 | Numbered subsections III.1-III.4 |
| `### I.4 Structural Findings (Permanent)` | session-23b-synthesis.md | 7 | Numbered bold-bullet list |
| `### III.2 Permanent Mathematical Achievements (Unaffected by K-1e)` | session-23b-synthesis.md | 7 | Table `\|Result\|Session\|Status\|` |
| `### III.2 Permanent Mathematical Achievements (Unaffected)` | session-23-sagan-verdict.md | 7 | Table (mirrors 23b) |
| `### III.1 E-6: Permanent Results -- Publishable as Standalone Mathematical Physics` | session-24b-synthesis.md | 8 | Two subcategory lists |
| `## XI. Structural Findings (Permanent, Independent of P2a Outcome)` | session-23c-synthesis.md | 7 | Named subsections, prose |

### Researcher Collab Patterns (commentary, not primary registries)

All prose narrative, no tables:
- `### 4.3 The Structural Results Are Untouched` (20b collabs)
- `### 4.2 What the Structural Results Tell Us` (20b-baptista)
- `### 2.1 Block-Diagonality: Sound, Permanent, and Devastating` (22-berry)
- `### 2.1 Trap 3 (C-1: Higgs-Sigma Portal Closure): SOUND and PERMANENT` (22-connes)
- `### Theme 2: The Block-Diagonality Theorem Is the Strongest Structural Result Since KO-dim = 6` (22-master-collab)
- `### What the framework has proven` / `### What the framework has not proven` (18-wrapup)

### Precision Values in Theorem Entries

| Precision format | Example | Sessions |
|:-----------------|:--------|:---------|
| `machine epsilon` | KO-dim = 6 | 7-8, 10, 11, 15, 17 |
| Scientific notation | `8.4e-15`, `3.29e-13`, `6.58e-16` | 17, 22b |
| `0.0000%` | A_b1/A_b2 = 4/9 deviation | 22a |
| `~10^{-29}` | Selection rule V(gap,gap)=0 | 23a |
| `exact` / `EXACTLY` | Trap 3, block-diagonality | 22b, 22c |

---

## 4. Open Channels / Escape Routes

### Header Patterns (chronological)

| Header (verbatim) | File | Gen | Content Format |
|:-------------------|:-----|:----|:---------------|
| `## WHAT'S OPEN` | session-10-phase2b-2.5.md, session-11-chirality.md | 1 | Bullet list |
| `### OPEN (requires further computation)` | session-22-master-synthesis.md, session-22d-synthesis.md | 6 | Table `\|Channel\|Priority\|Cost\|Decision criterion\|` |
| `### Open Channels (priority order for Session 23+)` | session-22d-synthesis.md | 6 | Table `\|Channel\|Status\|Cost\|What positive result means\|` |
| `## VII. Escape Routes (for Session 23b/c consideration)` | session-23a-synthesis.md | 7 | Subsections + "Other Routes" table `\|Route\|Description\|Estimated BF\|` |
| `### P2: Finite-Density Spectral Action (Primary Rescue)` | session-23a-synthesis.md | 7 | Prose + conditional probability |
| `## VIII. What Survives` | session-23a-synthesis.md | 7 | Table `\|Result\|Session\|Status\|` |
| `## III. Post-Mortem: What Survives and What Died` | session-23b-synthesis.md | 7 | Constraint Registry table + permanent achievements table |
| `### IV.2 P2a: beta/alpha from 12D Baptista Spectral Action` | session-23b-synthesis.md, session-23-sagan-verdict.md | 7 | Prose with conditional probability table |
| `### IV.3 P2b: Finite-Density Spectral Action (mu != 0)` | session-23b-synthesis.md, session-23-sagan-verdict.md | 7 | Prose with conditional probability table |
| `### IV.5 P2a/P2b Status (Post-V-1)` | session-24b-synthesis.md | 8 | Prose paragraphs |
| `### IV.6 Evidence Hierarchy (Updated)` | session-24b-synthesis.md | 8 | Contextual |
| `### III.2 E-7: Surviving Claim Set` | session-24b-synthesis.md | 8 | Block-quoted minimal statement |
| `## III. Non-Perturbative Physics — What Survives` | session-22-master-synthesis.md | 6 | He-3 analogy table + named subsections |
| `## V. B-4: OFF-DIAGONAL COUPLING ESCAPE ROUTE` | session-21b-valar-plan.md | 5 | Mechanism + quantitative table |
| `## XI. Structural Findings (Permanent, Independent of P2a Outcome)` | session-23c-synthesis.md | 7 | Named subsections |

### Researcher "Open Questions" Pattern (recurring in all collab files)

Standard section in every collab file: `## 5. Open Questions` or `## Section 5: Open Questions`

Variants: `## 5. Open Questions: What I Would Compute`, `## 5. Open Questions: What Geometry Demands to Know`, `## 5. Open Questions: What Would Sagan Ask?`

Format: Bullet list of 3-8 items. Not rescue routes — research questions.

---

## 5. Probability Trajectory

### Format 1 — Code-Block Trajectory (canonical, Sessions 23+)

```
Prior (theoretical):                    2-5%
After KO-dim=6 (Session 7-8):          10-15%
After SM quantum numbers (Session 7):   25-35%
...
=== K-1e DECISIVE CLOSURE ===
After Session 23a:                      5% (Sagan), 8% (Panel)
```

| Header (verbatim) | File |
|:-------------------|:-----|
| `## IX. PROBABILITY TRAJECTORY (Complete)` | session-23-sagan-verdict.md |
| `## VI. Probability Trajectory (Complete Through 23a)` | session-23b-synthesis.md |
| `### IV.3 Probability Trajectory (Complete Through 24b)` | session-24b-synthesis.md |
| `## X. PROBABILITY TRAJECTORY (Complete)` | session-24-sagan-verdict.md |

Features: Fenced code block, `=== CLOSED MARKER ===` delimiters, `<-- PEAK` annotations, 13-14 rows.

### Format 2 — Per-Agent Probability Tables

```
| Agent | Range | Median | Key Rationale |
| gen-physicist | 38-42% | 40% | V-1 closed... |
```

| Header (verbatim) | File | Rows |
|:-------------------|:-----|:-----|
| `## Per-Agent Estimates` | session-16-final.md | 8 |
| `### Agent Assessments` | session-20c-synthesis.md | 2 |
| `### 15-Researcher Master Collab Medians (Session 20b)` | session-20c-synthesis.md | 15 |
| `## VII. Per-Agent Probability Assessments` | session-21a-ainur-synthesis.md | 6 |
| `## IX. PROBABILITY TABLE` | session-20c-synthesis.md | 18 |
| `### Per-Agent Summary` | session-22d-synthesis.md | 4 |
| `### VIII.1 Per-agent` | session-22b-synthesis.md | 3 |

### Format 3 — Bayesian Log-Odds Calculation (Sagan Standard)

Fenced code blocks showing sequential BF updates:

```
PRE-SESSION-22 PROBABILITY: ...
SESSION 22 BAYES FACTOR UPDATES (SAGAN STANDARD):
===================================================
Session 22a (10 computations, correlation-adjusted):
  Correlated set {...}: BF = ... log-BF = ...
```

| Header (verbatim) | File |
|:-------------------|:-----|
| `## II. DEFINITIVE S-2: Full Bayes Factor Update` | session-22-sagan-verdict.md |
| `## II. BAYES FACTOR COMPUTATION` | session-23-sagan-verdict.md |
| `## VII. POSTERIOR COMPUTATION` | session-24-sagan-verdict.md |
| `## IV. Combined Probability Update` | session-24b-synthesis.md |
| `## V. Full Bayes Factor Update (Sagan Standard)` | session-22d-synthesis.md |

### Format 4 — Pre-Registered Outcome Tables

```
| Outcome | Pre-registered scenario | Actual result | Panel posterior | Sagan posterior |
| K-1e CLOSED | 5-8% | M_max 7-13x below | 8% | 5% |
```

| Header (verbatim) | File |
|:-------------------|:-----|
| `## V. Pre-Registered Probability Update` | session-23a-synthesis.md |
| `### III.1 Pre-Registered Outcome` | session-24a-synthesis.md |

### Format 5 — Adopted Posterior Tables

```
| Assessor | Mechanical | Structural floor | Adopted | Range |
| Sagan | 1.6% | 3% | 3% | 2-4% |
```

| Header (verbatim) | File |
|:-------------------|:-----|
| `### II.3 Adopted Posteriors` | session-23-sagan-verdict.md |
| `### VII.3 Adopted Posteriors` | session-24-sagan-verdict.md |
| `### IV.2 Convergence Assessment` | session-24b-synthesis.md |

### Format 6 — Simple Prose Updates (early sessions)

Bullet lists of per-agent ranges with no table structure:

| Header pattern | Sessions |
|:---------------|:---------|
| `## PROBABILITY ESTIMATES` | 10, 12, 14 |
| `## REVISED PROBABILITY ESTIMATES` | 13, 14 |
| `## UPDATED PROBABILITY ESTIMATES` | 9 |
| `## PROBABILITY ESTIMATES (Session N Consensus)` | 8 |
| `## X. FRAMEWORK PROBABILITY (Agent Consensus)` | 15 |
| `# III. UPDATED FRAMEWORK PROBABILITY` | 16-final |
| `## VIII. Framework Probability Assessment` | 17-final, 18-wrapup |
| `## Framework Probability Update` | 18-veff-convergence |
| `## VI. FRAMEWORK PROBABILITY` | 19d-synthesis |
| `## III. UPDATED FRAMEWORK PROBABILITY` | 20c-synthesis |
| `## VI. UPDATED PROBABILITY ASSESSMENT` | 22a-synthesis |

### Format 7 — Per-Researcher Probability Updates (Session 21c R2 collabs only)

All 16 `session-21c-r2-*-collab.md` files have:
- `## Section 6: Probability Update` or `## 6. Probability Update`
- Format: Prose or short table, personal estimate with rationale

---

## 6. Content Format Types

Summary of how entities are presented **within** sections.

### Type A — Numbered Constraint Registry Table (Sessions 23b+, canonical)
```
| # | Mechanism | Session | closure reason | BF |
| 1 | V_tree minimum | 17a SP-4 | Monotonically decreasing | 0.5 |
| **18** | **V_spec monotone** | **24a V-1** | **Monotonically increasing** | **0.35** |
```
Newest items bolded. BF column present in 24x, absent in 22d/23b.

### Type B — Status Table (Session 22d)
```
| Gate | Session | Result | Status |
| V_tree minimum | 17a SP-4 | Monotonically decreasing | CLOSED |
```

### Type C — 3-Column with "CLOSED —" in Result (Session 20c, first canonical)
```
| Session | Mechanism | Result |
| 17a SP-4 | V_tree minimum | CLOSED — monotonic, V'''(0) = -7.2 |
```

### Type D — H3 Header with Verdict Suffix
```
### D-1: Boson/Fermion E_proxy Separation Gate -- CLOSED
### II.2 K-1e: Gap Equation Trivial at mu = 0 — DECISIVE CLOSURE
### PA-2: Kosmann-Lichnerowicz Coupling — STRUCTURAL CLOSURE
```

### Type E — Bullet List (CLOSED/OPEN sections in 22d triptych)
```
- ALL perturbative spectral mechanisms (V_tree, CW 1-loop, ...)
- Higgs-sigma portal lambda_{H,sigma} (Trap 3: exactly constant)
- Rolling modulus quintessence (atomic clock bound: 15,000x violation)
```

### Type F — Researcher Commentary ("The CLOSURE Verdict Is...")
All prose. 15 variants across 20b collab files, 12 variants across 21c collab files.

### Type G — Tiered Criterion Tables (21b Valar plan)
```
| Tier | Criterion | BF | Prob shift |
| INTERESTING | ... | 3 | +3 pp |
| CLOSED | ... | 0.3 | -8-10 pp |
```

### Type H — Code-Block Trajectory
```
Prior (theoretical):                    2-5%
=== K-1e DECISIVE CLOSURE ===
After Session 23a:                      5% (Sagan), 8% (Panel)
```

### Type I — Bayesian Log-Odds Code Block
```
O_sagan = ln(prior_odds) + ln(BF_combined)
        = ln(0.05/0.95) + ln(0.31) = -4.115
p_sagan = 1 / (1 + exp(4.115)) = 1.6%
```
