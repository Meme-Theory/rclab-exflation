# PRU Pre-Registration Template

**Purpose**: Prevent Pre-Registration Underspecification (PRU, Class 8 plan-property failure).
Every gate declared in a session plan must fill this block BEFORE the producing script is run.

**Source**: script-review-plan.md §4.3 (W0-10 item 3, S80).

---

## R3 YAML Gate-Block Scaffold (S84+)

**Canonical machinery-pin scaffold**: `.claude/templates/r3-yaml-gate-block.yaml`
(added in S84 W9a-100). The R3 template declares the **8 required checklist items**:

1. `operator`
2. `strict_PASS_boundary`
3. `boundary_reachable_analytically`
4. `reachable_rationals`
5. `machinery_pin_map`
6. `audit_discriminators`
7. `substitution_chain`
8. `input_files`

The legacy prose block below (§"Gate Block") remains valid for markdown plan
files as long as its field set covers the 8 R3 items. S84+ authors SHOULD
prefer the YAML scaffold; legacy plans are accepted via the markdown-to-8-item
key map in `computations/_shared/_yaml_gate_validator.py`.

**Validation rule** (per §W9a-100): a gate block is R3-compliant iff every
one of the 8 checklist items is populated with non-empty content AND the
block declares `schema_version: "R3"` (YAML) OR satisfies the equivalent
markdown field set. **If a gate block is not R3-compliant, it does not count
toward sig_4 of the v3 closure ladder.** The validator is
`computations/_shared/_yaml_gate_validator.py`; it is invoked by the
`_pru_cardinality_audit.py` (W9a-97) tool as its gate-YAML source.

---

## Gate Block

Copy this block into the session plan under each gate.

```
Gate {{GATE_ID}} — {{ONE-LINE HYPOTHESIS}}
==========================================

Trigger:            [SIGN] | [VERIFY] | [AUDIT] | [VERIFY-THEOREM] | [CHAIN]
Classification:     PHONONIC | GEOMETRIC | PARTICLE | NON-PHONONIC
Producing script:   {{computations/_shared/sNN_*.py}}
Session:            S{{NN}} W{{WAVE}}-{{LETTER}}
Dependencies:       {{prior gates or theorems this rests on}}

—— Pre-registered inputs (SHA-256 pins) ——
Input file 1: {{path}}
  expected_sha256 = {{hexdigest or "<computed-at-runtime>"}}
Input file 2: {{path}}
  expected_sha256 = {{hexdigest or "<computed-at-runtime>"}}
…
Import closure hash (canonical_constants.py + all imports): {{hexdigest or "<computed-at-runtime>"}}

—— Pre-registered machinery (PRDR pin — enumerate every free parameter) ——
N_eval        = {{int}}                       # eigenvalue count / sample count / iteration count
L_max         = {{int or N/A}}                # truncation scale (spectral / cutoff / Peter-Weyl band)
scan_range    = [{{min}}, {{max}}]            # any swept parameter
step_size     = {{value or "adaptive"}}
tolerance     = {{ε}}                         # convergence / residual tolerance
scheme        = {{FW|BLV|SA|MS|UNIFIED-AS-79|…}}
convention    = {{ABSOLUTE|RATIO|MIXED|…}}    # W0-9 classification
random_seed   = {{int or "N/A — deterministic"}}
GPU path      = {{torch.linalg|numpy.linalg|cpu-cap-OMP8}}

All other free parameters explicitly pinned: {{YES | list-outstanding-here}}

—— Pre-registered pass/fail criterion ——
PASS iff:   {{quantitative condition, e.g.  |value - target| / target <= 0.005}}
FAIL iff:   {{quantitative condition, e.g.  |value - target| / target >  0.05}}
INFO iff:   {{intermediate regime, between PASS and FAIL thresholds}}

Target value:           {{canonical_constant_name or literal}}
Tolerance policy:       RATIO = 0.5%  |  ABSOLUTE = 5%  |  THEOREM = machine-ε
  (per W0-9 classification; cite the rule used)

—— Pre-registered output 4-tuple ——
Expected form:
  (value=<computed>, scheme={{scheme}}, convention={{convention}}, L_max={{L_max}})

Verdict line format (appended to s{{NN}}_gate_verdicts.txt):
  {{GATE_ID}}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
  # S84+: the single-sha256 line above is the pre-S84 LEGACY shape. Current
  # gates ALSO emit the dual-SHA companion comment row (and, for [SIGN] gates,
  # the SIGN/MAGNITUDE/REGIME 3-tuple row) per gate-verdicts.md §"Schema-v2".
  # Prefer the R3 YAML scaffold's output_artifacts.verdict_line block.

—— Substitution chain (MANDATORY for sign/direction/threshold claims) ——
Step 1 — Definitions:
  {{quantity 1}} = {{definition, cite canonical constant or defining equation}}
  {{quantity 2}} = …

Step 2 — Substitution (plug definitions into target expression, no simplification):
  {{target expression with all symbols expanded}}

Step 3 — Simplification (algebra only, one step per line):
  = {{line 1}}
  = {{line 2}}
  = {{canonical form}}

Step 4 — Direction read-off (from canonical form):
  {{sign/direction/threshold conclusion}}

—— Post-run actions (filled AFTER the script executes) ——
[ ] Verdict line appended to s{{NN}}_gate_verdicts.txt with SHA pin
[ ] Closure SHA logged in first 20 lines of script stdout
[ ] 4-tuple output tag printed as final non-verdict line
[ ] Result added to canonical_constants.py (if it's a reusable constant)
[ ] Result registered via `update_constant(...)` in knowledge MCP (if PASS)
[ ] Theorem row appended to permanent-results-registry.md (if §VII.I claim)
```

---

## How to Use

### At plan-write time (PRDR — Pre-Registration Dry-Run)

1. **Enumerate every free parameter in the producing script**. Use `ast` static
   analysis: walk the script, collect every `name = <number>` assignment that
   is NOT imported from `canonical_constants`, and NOT tagged `# (local)`. Each
   one is a free parameter. Pin it or declare it as diagnostic.

2. **Compute expected input SHAs where possible**. Any static input file (e.g.
   a prior session's `.npz`) has a fixed SHA; paste it into the block. For
   runtime-generated inputs (e.g. `canonical_constants.py` after recent
   edits), leave as `<computed-at-runtime>` and check the verdict line.

3. **Write the substitution chain for every sign/direction claim**. Without it,
   the plan is PRU-vulnerable: the gate's verdict might hinge on a direction
   the plan didn't pin.

4. **Select convention + scheme explicitly**. The framework has multiple
   competing schemes (FW, BLV, SA, MS, UNIFIED-AS-79, …); a gate that says
   "c_sub > 1" without naming the scheme is underspecified.

### At execution time

1. Script reads inputs, logs SHA-256 of each, prints closure SHA.
2. Script runs the computation.
3. Script emits 4-tuple output tag.
4. Script appends verdict line to `s{NN}_gate_verdicts.txt` with SHA pin.
5. The canonical-import audit (`_canonical_audit.py`) picks up the new pin on its next run.

### At audit time

- `s80_pru_audit.py` confirms:
  - Input-pin fields are filled
  - 4-tuple output tag exists
  - SHA pin appears in the verdict line
- Any gate block missing fields is PRU-vulnerable and gets flagged in the
  weekly/session audit.

---

## Class 8 Failure Mode (PRU)

PRU = *plan-property* failure, structurally distinct from the 7 execution-property failures:

| # | Failure | Type | Prevented by |
|:--|:--------|:-----|:-------------|
| 1 | Convention-shopping | execution | Pre-registered scheme field |
| 2 | Ansatz-forced PASSes | execution | Pre-registered threshold |
| 3 | Vacuous-margin | execution | Pre-registered convention + tolerance |
| 4 | Load-and-compare-to-self | execution | Independent target value |
| 5 | Linear-rescale-as-cross-check | execution | Pre-registered cross-check method |
| 6 | Iterate-until-PASS | execution | One-shot execution + verdict |
| 7 | False cross-checks | execution | Pre-registered cross-check criterion |
| **8** | **PRU (machinery unpinned)** | **plan-property** | **This template + PRDR** |

A scrubbed plan that prevents all 7 execution failures but does not pin every
free parameter via PRDR remains PRU-vulnerable and will produce multi-iteration
verdict-log floatation (as observed in S78 scrubbed re-run W1-B, W2-C, W3-L).

---

## References

- `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" + §"Source Reconciliation" (Class 8.1)
- `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" + §"Machinery-Feasibility Audit"
- `.claude/rules/gate-verdicts.md`
- `computations/session-80/s80_pru_audit.py` — audit tool
- `computations/_shared/_source_reconciliation_audit.py` — Class 8.1 audit (S86 W0a-2)
- `computations/_shared/_pru_keyword_classifier.py` — 8-key K disambiguation classifier (S86 W0a-4)
- `computations/_shared/_yaml_gate_validator.py` — `cutoff_axis` schema enforcement (S86 W0a-3)
- `script-review-plan.md` §4.3 — origin of this template

---

## PRU Class 8.1 — Source-Reconciliation 5-Class Taxonomy (S86 W0a-2)

> **Rule-File v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)** — provenance: lizzi 9A §7.2 sub-diff A + S85 5A workshop. Canonical home for the 5-class taxonomy; the runtime audit (`_source_reconciliation_audit.py`) classifies every plan pin into one of these classes.

| Class | Name | Definition |
|:------|:-----|:-----------|
| **A** | PINNED-AND-MATCHED | declared pin SHA == on-disk SHA; no defect |
| **B** | PINNED-BUT-DRIFTED | declared pin SHA != on-disk SHA; on-disk file modified after pin |
| **C** | UNPINNED-BUT-REFERENCED | script reads file with no SHA pin in input map; PRU Class 8.1 defect |
| **D** | PINNED-BUT-MISSING | declared pin SHA references nonexistent file; broken pin |
| **E** | PINNED-MULTIPLE-DIVERGENT | same logical input pinned with two different SHAs across two scripts; cross-script source contradiction |

Severity calibration (Lyapunov-band per kitaev K2):

- `D_max < 0.1` → no rule-file action
- `0.1 ≤ D_max < 1.0` → SOURCE-RECONCILIATION advisory (S2)
- `1.0 ≤ D_max < 3.0` → SOURCE-RECONCILIATION MANDATORY (S1); halts plan-freeze
- `D_max ≥ 3.0` → hard plan-freeze halt; manual review required

S85 W6-W13 historical measurement: `D_max = 5.6726` at site #10 (GPU L=12), well above the 3.0 hard-halt threshold — establishes the audit's empirical calibration.

---

## PRDR Keyword Window — Explicit Atomic Enumeration (S85 W6-W13 extension; landed S86 W0a-4)

> **Rule-File v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)** — provenance: lizzi 9A §7.4 sub-diff C + gen-physicist G4a/G4b/G4c; PARENT/CHILD xref to W-3 §G2 (g) keyword-context audit framework (the 5A G4a 8-K-atom enumeration is the K-family specialization of W-3's general framework).

The PRDR static analyzer's keyword window MUST enumerate the framework's
canonical-constants atoms explicitly, NOT collapse them into single-letter
buckets. For framework K-quantities the **8-atom enumeration** is:

| Sub-key | Definition (one-line) | Canonical source |
|:--------|:----------------------|:-----------------|
| `K_base` | Substrate base coherence wavenumber (canonical alias triple `K_base = K_R3 = K_substrate = 2.035`) | `canonical_constants.py` |
| `K_corridor` | Corridor-extension wavenumber for K ∈ [K_R5, K_crit] | gen-physicist S-7 §V.4 |
| `K_R5` | Inflationary-corridor lower edge (regulator family R5; value = 1.9222) | S85 W5 D.4 |
| `K_crit` | Inflationary critical wavenumber (= 91.5) | `canonical_constants.py` |
| `K_substrate` | Substrate intrinsic K (substrate-distance-1 quantity per P5) | gen-physicist 9A §4.5b |
| `K_R3` | R3 schema-validator K (regulator family R3) | gen-physicist S-7 §V.15 |
| `K_FIRAS` | FIRAS-anchored K (post-fold Riemann cover upper edge; value = 355600) | gen-physicist S-7 §V.4 |
| `K_pivot` | Pivot K at N_pivot for SR-flow integration | mack 9A §VI.3 |

**Disambiguation pin**: `K_crit = 91.5` (inflationary) and `K_crit_BdG = 2.035` (BdG; W0c C17 future-landing) are DISTINCT observables. Future plan-authors must reference whichever sub-key applies; bare `K` is forbidden.

Every plan-layer keyword must declare:

```
granularity: atomic | grouped
```

Grouped keywords MUST list their constituent atomic sub-keys.

The classifier is `computations/_shared/_pru_keyword_classifier.py`. Open carry-forward to S87: `S87-PRDR-K-NEGATION-AWARE` extends the regex preprocessor with negation-window guards (W0a-4 closed 13/14 historical false-positives; the residual is a downstream regex-design defect surfaced by — not masked by — disambiguation).

### v3-recovery sig_2 cross-check scope (debt class 6)

The sig_2 SHA-cross-check must be **scoped** to the gate's plan-required
cross-references ONLY, NOT extended to diagnostic citations. Per W11-2
first-run FAIL (W11 WP §W11-2(e) line 323): the script over-constrained
the SHA-mismatch rule by including W10-115 (connes deferred SHA citation)
in the blocking set; W10-114 + S82 W2-3 are the only plan-required
cross-references. **Sig_2 scope must respect the plan §6 explicit list.**

### 5B-class scan-as-robustness INFO-mode (debt class 7)

When a gate's pre-registered scan parameter (L_max range, ε scan, etc.)
is declared as a NUMERICAL-ROBUSTNESS DIAGNOSTIC rather than a
PASS-condition input, the gate's verdict 4-tuple must carry the flag:

```
scan_role: diagnostic | primary
```

Diagnostic-only scans automatically map PASS-by-algebraic-identity to
INFO under the algebraically-forced INFO-mode rule (G2). This prevents
inflation of structural identities into apparent computational PASSes.

---

## Cutoff Axis YAML Pin (S86 W0a-3)

> **Rule-File v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)** — provenance: gen-physicist S-7 §V.9 + S86 plan W0a-3. Validator: `computations/_shared/_yaml_gate_validator.py`.

A gate block whose machinery pin invokes a cutoff (`Λ_cut`, `K_cut`,
`K_R5`, `K_crit`, `K_FIRAS`, `K_floor`, `K_wall`, `cutoff_sqrt` — the
8 keyword triggers) MUST declare:

```
cutoff_axis: spectral | coherence | both
```

Semantics:

- `spectral` — cutoff acts on D_K eigenvalues (Λ on the spectrum)
- `coherence` — cutoff acts on substrate dispersion / corridor length (K on momentum-shell)
- `both` — gate references both axes (must justify in gate block)

Absence on a cutoff-invoking gate is a PRDR Class 8 PRE-REG-INC at plan-freeze.

---

## Changelog v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)

- W-3 v2: §G2 (g) keyword-context audit clause — full text in `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` §G2 (g).
- 5A v2 sub-diff A: 5-class taxonomy (above).
- 5A v2 sub-diff C: PRDR keyword window 8-K-atom enumeration + sig_2 scope-correction + 5B-class scan-as-robustness INFO-mode (above).
- PARENT/CHILD xref: W-3 §G2 (g) ↔ 5A G4a (above).
- S86 W0a-3: `cutoff_axis` YAML schema field (above).
- Source: lizzi 9A §7.2 + §7.4 + S85 5A workshop, consolidated per S85 closeout §3.5 R1 + §6.5 + S86 plan W0a-1 + W0a-2 + W0a-3 + W0a-4.
