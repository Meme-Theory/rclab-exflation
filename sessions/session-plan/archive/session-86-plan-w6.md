# Session 86 Plan — Wave W6: Perturbative-immunization corollaries

**Generated**: 2026-04-25
**Owner planner**: `lizzi-spectral-functional-theorist` (1C IEP-partition originator + 9A §E-1 + §E-3 source)
**Wave size**: 3 items (C2 umbrella + C40 lattice-spacing + C42 Weyl-rescaling-WEAK)
**Theme**: Instantiate 1C 6-Φ-branch corollaries within §VII.S cascade — land the immunization-family parent registry slot, attempt C-α (lattice spacing) at slot-by-slot Mellin level, attempt C-γ-WEAK (Weyl rescaling) under internal Λ_anomaly bound. Two further corollaries (C-η Ward, C-θ Connes inner-fluctuation) ALREADY landed in W1c via C41 zero-compute; four (C-δ, C-ε, C-ζ, C-ι) deferred to S87.

**Output target verdict file**: `computations/s86_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md` canonical path).

**Substrate framing**: All three gates are GEOMETRIC. They map the regulator-class structural floor of the substrate's spectral content under three classes of perturbation (registry-write of the family parent in C2; lattice discretization in C40; Weyl rescaling in C42). The §VII.S cascade does NOT produce new physics — it bounds the corridors in which the Dirac operator's spectrum is INSENSITIVE to specific perturbative deformations of the regulator/gauge/discretization apparatus.

---

## §0. Wave W6 Summary

| Gate | Title | Trigger | Effort | Owner subagent | Decisive? |
|:-----|:------|:--------|:-------|:---------------|:---------:|
| W6-1 | C2 `S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING` (umbrella) | [VERIFY] | 1.5h LIGHT registry-write | `connes-ncg-theorist` (lizzi blacklisted: self) | YES (registry landing) |
| W6-2 | C40 `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE` (1C C-α / OQ1) | [VERIFY-THEOREM] | 4-5h MODERATE | `lizzi-spectral-functional-theorist` | YES (slot-by-slot drift-exponent test) |
| W6-3 | C42 `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM` (1C C-γ-WEAK / OQ2) | [VERIFY-THEOREM] | 6-8h HEAVY | `lizzi-spectral-functional-theorist` (or `connes-ncg-theorist`) | YES (parametric bound) |

**Combined estimated effort**: ~11-15h compute + ~1.5h registry-write = within one wave budget if C42 GPU pin holds.

**Dispatch order** (within wave): C2 first (registry slot reserved by W1a T3 must be present and fresh); then C40 + C42 dispatched in parallel.

---

## §0.5. Wave W6 Decision-Point Prerequisites

| Prereq | Provided by | Status check before W6 dispatch | If missing |
|:-------|:-----------|:--------------------------------|:-----------|
| §VII.S parent registry slot present at `sessions/permanent-results-registry.md` | W1a T3 `S86-VII-S-PERTURBATIVE-LEDGER-IMMUNIZATION-FAMILY-LANDING` | grep `^### §VII.S` in registry; non-empty body | Halt W6; dispatch a single-item rescue wave that lands the §VII.S parent stub before C2 cascade |
| C-η + C-θ zero-compute landed | W1c C41 `S86-VII-S-C-ETA-LANDING + S86-VII-S-C-THETA-LANDING` | grep `^#### §VII.S.C-η` AND `^#### §VII.S.C-θ` | C2 still proceeds (it documents C-η/C-θ as LANDED-via-W1c-C41); no halt |
| `b_DK` constant in `canonical_constants.py` | NEEDED for C42 — currently NOT in canonical_constants per knowledge MCP `list_constants(pattern='b_DK')` returned empty | `python -c "from canonical_constants import b_DK"` | C42 prompt MUST include the canonical-constants registration step BEFORE the parametric-bound test (add `b_DK` with provenance citing AC-2010 §V) |
| `M_KK = 7.428660036284456e+16` (eV scale) for Λ_anom unit work | CANONICAL | `mcp__knowledge__get_constant('M_KK')` confirmed | n/a |

**Per `epistemic-discipline.md` §Pre-Registration Completeness**: C42 has a PRDR Class-8 vulnerability if `b_DK` is unpinned at compute time. The registration step in §W6-3 §M.0 IS the PRDR pin closure; it MUST be performed in-script (with provenance line) and not deferred to a separate W0c entry.

---

## §I. Carry-Forward Items Mapping (3 rows)

| Source row | Wave-W6 gate | Sourced from | Mapping note |
|:-----------|:-------------|:-------------|:-------------|
| Partition §1 W6 item 1 (C2 umbrella) | W6-1 | gen-physicist 9A §4.3 + 1C workshop | Umbrella registry-write under §VII.S parent landed in W1a T3; only LANDING in S86; corollaries C-α (via C40) + C-γ-WEAK (via C42) attempted in this wave; C-δ/ε/ζ/ι defer S87 |
| Partition §1 W6 item 2 (C40) | W6-2 | lizzi 9A §E-1 + gen-physicist 9A §4.3 sub-gate | §VII.S.B C-α corollary at slot-by-slot Mellin level; 3 Wilson + 1 Symanzik discretizations at L_max=5; per-slot drift exponents 0,1,2,3 expected at Symanzik O(a^4) PASS-band |
| Partition §1 W6 item 3 (C42) | W6-3 | lizzi 9A §E-3 | §VII.S.D weak-form gate; Λ_anomaly INTERNALLY computed from Tr_F(Y†Y) + AC-2010 §V coefficients; parametric bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²` |

All 3 rows enter S86 in this wave. None deferred.

---

## §W6-1. S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING (C2 umbrella)

**Gate ID**: `S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING`

**Trigger**: `[VERIFY]` (registry-write; verifies that the §VII.S parent + 10-row corollary table is present, well-formed, and accurately records LANDED / ATTEMPTED / DEFERRED status per S86 wave assignments).

**Classification**: GEOMETRIC (NCG corollary structure; documents the substrate's regulator-class structural floor under 10 distinct perturbation classes).

**Owner subagent**: `connes-ncg-theorist` (lizzi-spectral-functional-theorist is blacklisted as self; connes is the natural NCG-formalism owner for §VII.S parent registry slot landing per the W1a T3 chain; cross-validation with lizzi via PRDR machinery pin only).

**Hypothesis (one sentence)**: The §VII.S "Perturbative-Ledger Immunization Family" parent registry slot, populated with a 10-corollary table whose entries each carry an IEP class tag (INTENSIVE / EXTENSIVE) and a status tag (LANDED via C41 zero-compute / ATTEMPTED in S86 / DEFERRED to S87), is a complete and audit-ready landing of the 1C 6-Φ-branch immunization cascade.

### §M. Method (complete dispatch prompt for `connes-ncg-theorist`)

```
[BEGIN DISPATCH PROMPT — W6-1 connes-ncg-theorist]

CONTEXT
You are landing the parent registry slot for the Perturbative-Ledger
Immunization Family at §VII.S of sessions/permanent-results-registry.md.
The §VII.S section was created in W1a T3 (`S86-VII-S-PERTURBATIVE-LEDGER-
IMMUNIZATION-FAMILY-LANDING`) as a stub with the family-level statement
and IEP class-tag scaffold. Your job is to populate it with the 10-row
corollary table and per-corollary status entries.

INPUTS (read in order, before any write)
1. sessions/permanent-results-registry.md — locate the §VII.S parent
   stub (created W1a T3); verify the family-level statement is present.
2. sessions/session-plan/session-86-context.md §1.5 (regulator-class
   structural floor) and §2.6 entries C2, C40, C41, C42 verbatim.
3. sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md §E-1, §E-2,
   §E-3 (corollary derivations); only read sections explicitly cited.
4. .claude/rules/gate-verdicts.md (verdict-line + dual-SHA format).

PROVENANCE INVENTORY (must cite)
- 1C 6-Φ-branch enumeration: lizzi 9A §6.8 (B-2)
- Family-level theorem statement: lizzi 9A §E intro (verbatim 4-symbol
  Theorem (Immunization) form: "Observable X is immune to source-of-
  contamination Y at level Z, where X = spectral-moment-derived
  observable on D_K (Jensen-deformed SU(3)), Y = class of would-be
  contaminations, Z = level at which immunity is asserted")
- Substitution chain: per knowledge-MCP search 'perturbative
  immunization corollary VII.S' returns 5 hits in
  s85-1c-perturbative-immunization-family.md — cite 5 hits as
  registry-source provenance.

WRITE TARGETS
1. sessions/permanent-results-registry.md §VII.S — populate the
   10-row corollary table with this exact column set:
   | Branch | Corollary ID | Source-of-contamination Y | IEP class | Status | Landing wave | Dual-SHA |
   |:-------|:-------------|:--------------------------|:----------|:-------|:-------------|:---------|

   Rows (verbatim ordering A, B, C, D, E, F, G, η, θ, ι):
   - §VII.S.A — C-α — gauge-fixing perturbation (proxy) — INTENSIVE — DEFERRED — S87 — n/a
       NOTE: gauge-fixing C-α here is the family-class label; the
       LATTICE-SPACING C-α tested in W6-2 is a SUB-INSTANCE of
       §VII.S.A's lattice-discretization sub-branch B (per lizzi 9A
       §E-1 sub-clause "C-α corollary at slot-by-slot Mellin level").
       The branch label disambiguation follows lizzi 9A §6.8 (B-2)
       6-Φ-branch enumeration; the §VII.S.A row carries `STATUS:
       DEFERRED-S87` because the gauge-fixing branch proper is not
       attempted in S86.
   - §VII.S.B — C-α-LATTICE — lattice discretization — INTENSIVE — ATTEMPTED-S86 — W6-2 — pending compute
   - §VII.S.C — C-β — non-perturbative instanton residue — EXTENSIVE — DEFERRED — S87 — n/a
   - §VII.S.D — C-γ-WEAK — Weyl rescaling (weak parametric-bound form) — INTENSIVE — ATTEMPTED-S86 — W6-3 — pending compute
   - §VII.S.E — C-δ — KMS state perturbation — EXTENSIVE — DEFERRED — S87 — n/a
   - §VII.S.F — C-ε — fluctuating finite-rank K — EXTENSIVE — DEFERRED — S87 — n/a
   - §VII.S.G — C-ζ — twisted spectral triple deformation — INTENSIVE — DEFERRED — S87 — n/a
   - §VII.S.η — C-η — Ward identity (zero-compute via [J,D_K]=0) — INTENSIVE — LANDED-W1c-C41 — W1c — copy SHA from W1c-C41 verdict line
   - §VII.S.θ — C-θ — Connes inner fluctuation invariance (zero-compute via CCM-2007 §3) — INTENSIVE — LANDED-W1c-C41 — W1c — copy SHA from W1c-C41 verdict line
   - §VII.S.ι — C-ι — heat-kernel coefficient regulator-shift — INTENSIVE — DEFERRED — S87 — n/a

2. After table, write the family-level statement verbatim from the
   knowledge-MCP hits (5 lines).

3. Append a substitution-chain footer (audit form):
   "Substitution chain (registry-landing direction):
     Step 1 (definition):  10 corollaries enumerated in 1C cascade per lizzi 9A §6.8 (B-2)
     Step 2 (substitute):  status tags = {LANDED-W1c: 2, ATTEMPTED-S86: 2, DEFERRED-S87: 6}
     Step 3 (simplify):    sum = 2+2+6 = 10 ✓
     Step 4 (direction):   Each corollary is documented with branch + IEP + status + wave
                           → table is COMPLETE and AUDIT-READY"

4. computations/s86_gate_verdicts.txt — append ONE canonical line:
   "S86-PERTURBATIVE-IMMUNIZATION-FAMILY-LANDING: PASS|FAIL -- value=10_rows_present scheme=registry convention=tabular L_max=n/a sha256=<closure>"
   plus dual-SHA companion row per W9a-99 template (`content_sha256` =
   SHA-256 of the §VII.S body insertion; `audit_sha256` = SHA-256 of
   the ordered input-pin map).

ENVIRONMENT
- Python: phonon-exflation-sim/.venv312/Scripts/python.exe
- No GPU compute (pure registry-write); CPU thread cap not applicable.
- Script: computations/s86_w6_1_immunization_family_landing.py
- Script imports: from canonical_constants import * (no constants used
  but import required by S34+ rule); hashlib for closure SHA.

CROSS-CHECK
- Read computations/s86_gate_verdicts.txt back AFTER append; verify
  the canonical line appears exactly once. If duplicated, fail-fast.
- Read sessions/permanent-results-registry.md §VII.S body length AFTER
  write; verify ≥ 30 lines (table + family-statement + substitution-
  chain footer). If <30 lines, write was a stub — re-run with full body.

OUTPUT REQUIRED (4-tuple)
(value=<int rows present>, scheme=registry, convention=tabular, L_max=n/a)

DO NOT
- Hardcode any constant; pure registry-write — no numerical scan.
- Edit sessions outside §VII.S parent body.
- Write more than ONE verdict line per gate ID.
- Skip the substitution-chain footer (audit-required per
  .claude/rules/math-scripts.md §Double-Check Logic Before Compute).

[END DISPATCH PROMPT]
```

### §P. Machinery pin (PRDR — W6-1)

| Parameter | PIN | Source |
|:----------|:----|:-------|
| `corollary_count` | 10 | 1C cascade enumeration (lizzi 9A §6.8 B-2); reconciled in-session 2026-04-26 from plan-text typo `9` (§M item 1 line 105 ordering header originally omitted "G" for §VII.S.G C-ζ twisted spectral triple); see W6-1 closure narrative |
| `iep_partition` | INTENSIVE: {A, B, D, G, η, θ, ι}; EXTENSIVE: {C, E, F} | T4 W1a IEP annotation |
| `status_distribution` | LANDED-W1c=2, ATTEMPTED-S86=2, DEFERRED-S87=6 | wave assignment §0 above (DEFERRED set: A, C, E, F, G, ι); reconciled in-session 2026-04-26 from typo `=5` |
| `column_set` | Branch / Corollary ID / Source-of-contamination Y / IEP class / Status / Landing wave / Dual-SHA | this plan §M item 1 |
| `verdict_path` | `computations/s86_gate_verdicts.txt` | gate-verdicts.md §Canonical Path |
| `dual_sha_template` | W9a-99 (content_sha256 + audit_sha256) | gate-verdicts.md S81+ form |
| `tolerance_rule` | THEOREM (registry-presence binary; row-count exact) | THEOREM rule per gate-verdicts.md |
| `random_seed` | n/a | no stochastic step |
| `GPU path` | none | pure registry-write |
| `schema_version` | R3 | R3 YAML lift required per W0a R3 |

### §O. Expected output 4-tuple

`(value=10_rows_present, scheme=registry, convention=tabular, L_max=n/a)`

### §T. PASS / FAIL / INFO thresholds

- **PASS**: Registry §VII.S body contains a 10-row table with exact column set above + family-level statement verbatim + substitution-chain footer; AND ≥2 LANDED rows carry SHA references back to W1c C41 verdict lines (verifiable via grep); AND verdict line appended exactly once at canonical path. Tolerance rule: THEOREM (binary presence + integer row count).
- **FAIL**: Any of (table absent, row count ≠ 10, missing column, missing footer, duplicate verdict line). FAIL is reported as a registry-write defect; the corollary ATTEMPTS in W6-2 + W6-3 are NOT blocked but their landing-wave references will be incomplete.
- **INFO**: Not applicable — registry landing is binary present/absent.

### §S. Substitution chain

Not required for W6-1 (no sign/direction/threshold claim; pure registry-presence test). The §M dispatch prompt itself contains the audit substitution-chain footer (4-step) that the agent must include at the end of the registry body — that is documentation, not a quantitative verification.

### §M-S-S. What PASSES / FAILS MEAN for the solution space

- **PASS**: §VII.S parent + 10-corollary cascade is now navigable from the registry; downstream W6-2 + W6-3 attempts land into named slots; S87 corollaries (C-δ/ε/ζ/ι) have a documented home before they compute. Substrate framing: the substrate's regulator-class structural floor under perturbative deformations now has a 10-class taxonomic atlas — the spectral content's immunity-or-non-immunity to each Y is a navigable map, not a scattered claim.
- **FAIL**: Registry write was incomplete; W6-2 + W6-3 verdicts will reference a landing slot that does not match its declared shape; downstream S87 corollary landings must rebuild the parent stub before they compute. NOT a physics defect — purely an audit-trail defect that delays the 1C cascade closure.

### §E. Effort estimate

~1.5h (registry-only write; no compute). Two write-targets (registry §VII.S + verdict file).

### §SF. Substrate-framing reminder

This corollary cascade is GEOMETRIC. It bounds the substrate's spectral content under 10 explicit classes of perturbative deformation of the regulator/gauge/discretization apparatus. Each row of the table is the statement: "the substrate's spectral content is IMMUNE to perturbation Y under condition Z (or NOT IMMUNE, if the corollary fails)". The cascade documents corridors of insensitivity, not new physics.

---

## §W6-2. S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE (C40)

**Gate ID**: `S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE`

**Trigger**: `[VERIFY-THEOREM]` (theorem-grade corollary test; per-slot drift-exponent statement carries direction claims that require substitution chain).

**Classification**: GEOMETRIC (NCG corollary structure; tests whether the substrate's a_n spectral moments inherit Symanzik discretization order O(a^4) per slot).

**Owner subagent**: `lizzi-spectral-functional-theorist` (lizzi 9A §E-1 is the source; lattice-spacing immunization at slot-by-slot Mellin level is the spectral-functional analyst's natural domain — the F_4 / M partition formalism + slot decomposition is lizzi-track machinery per S-1).

**Hypothesis (one sentence)**: §VII.S.B's C-α corollary holds at slot-by-slot Mellin level — under 3 Wilson discretizations and 1 Symanzik discretization at L_max=5, the per-slot lattice-spacing drift exponents satisfy `δa_{2k}/a_{2k} ~ a^{p_k}` with p_k = (0, 1, 2, 3) for slots (a_0, a_2, a_4, a_6) at the Symanzik O(a^4) PASS-band, while Wilson discretizations exhibit p_k = (0, 1, 1, 2)-type degraded scaling.

### §M. Method (complete dispatch prompt for `lizzi-spectral-functional-theorist`)

```
[BEGIN DISPATCH PROMPT — W6-2 lizzi-spectral-functional-theorist]

CONTEXT
You are testing §VII.S.B C-α corollary at slot-by-slot Mellin level on
the Jensen-deformed SU(3) D_K spectrum at L_max=5. The corollary
predicts that the substrate's a_n spectral moments inherit the
discretization order of the regulator: Wilson actions give O(a) leading
error per slot (with degraded scaling on higher slots), Symanzik
improvement gives O(a^4) per slot.

INPUTS (read in order, before any compute)
1. computations/canonical_constants.py — import M_KK, tau_fold,
   Vol_SU3, J_C2 (constants for D_K eigenvalue normalization).
2. D_K spectral cache at L_max=5 — locate file path via grep over
   computations/ (most recent S85 cache); read SHA-256 of the
   cache file; pin as input_sha for verdict line.
3. sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md §E-1
   (4-line verbatim derivation of the C-α slot-by-slot statement); cite
   verbatim in script header docstring.
4. sessions/session-plan/session-86-context.md §1.5 (F_4 / M atlas),
   §2.6 C40 entry verbatim.

ENVIRONMENT
- Python: phonon-exflation-sim/.venv312/Scripts/python.exe
- GPU: USE torch.linalg for any matrix op ≥ 100×100 (D_K matrices at
  L_max=5 are ~5000×5000; torch.linalg.eigvalsh on AMD RX 9070 XT via
  ROCm 7.2). CPU fallback ONLY if torch import fails — set
  os.environ['OMP_NUM_THREADS'] = '8' BEFORE numpy import.
- Script: computations/s86_w6_2_lattice_spacing_immunization.py
- Script imports: from canonical_constants import *; import torch;
  import numpy as np; import hashlib.

DISCRETIZATION SCHEMES (4 total)
- Wilson-1: standard Wilson action with r_W = 1.0 (improvement
  parameter); spacing a_W in units of M_KK^{-1}.
- Wilson-2: Wilson with r_W = 0.5 (reduced clover coefficient).
- Wilson-3: Wilson with r_W = 1.5 (over-clovered).
- Symanzik: tree-level Symanzik-improved with c_SW = 1.0 + O(g²) terms
  set to lattice-perturbation-theory tree-level values.

LATTICE SPACINGS (5 values per scheme)
- a / M_KK^{-1} ∈ {0.500, 0.250, 0.125, 0.0625, 0.03125} (factor-2
  refinement; 5 spacings → drift-exponent fit per slot per scheme).

PROCEDURE
For each scheme s ∈ {Wilson-1, Wilson-2, Wilson-3, Symanzik}:
  For each spacing a ∈ {0.500, ..., 0.03125}:
    1. Construct D_K(a, s) on Jensen-deformed SU(3) at L_max=5
       (tau_fold pin from canonical_constants).
    2. Compute eigenvalue spectrum λ_i(a, s) via torch.linalg.eigvalsh.
    3. Compute spectral moments a_{2k}(a, s) for k ∈ {0, 1, 2, 3}
       via the Mellin slot-by-slot formula (S-1 §IV.5):
          a_{2k}(a, s) = Σ_i Θ(λ_max - λ_i) · λ_i^{(2k - d_spec)/2}
       where d_spec = 8 (NCG dimension), λ_max from D_K cache.
    4. Tag each a_{2k}(a, s) with regulator-pin per W12-4
       CANON-REGULATOR-PIN-DISCIPLINE (P14): 'a_{2k}^{Wilson-1, a=...}'.

  Then per slot k ∈ {0, 1, 2, 3}, fit drift exponent p_k(s) via:
       log10(|a_{2k}(a, s) - a_{2k}(a→0, s)|) = p_k(s) · log10(a) + C_k(s)
    where a_{2k}(a→0, s) is the Richardson-extrapolated continuum value
    (use 5-point Aitken Δ² extrapolation).

PRE-REGISTERED PASS BAND (PRDR-pinned BEFORE compute)
PASS:
  Symanzik p_k(Symanzik) ∈ [3.5, 4.5] for ALL k ∈ {0, 1, 2, 3}
    (i.e., O(a^4) per slot — corollary statement holds)
  AND Wilson schemes p_k(Wilson-i) ∈ [0.5, 2.5] for k ∈ {1, 2, 3}
    (degraded scaling per Wilson-class)

INFO band:
  Symanzik p_k(Symanzik) within [2.5, 3.5] OR [4.5, 5.5] for
    AT MOST 1 of 4 slots (corollary holds approximately on 3 of 4
    slots; flag for refinement)

FAIL:
  Symanzik p_k(Symanzik) outside [2.5, 5.5] for ANY slot
  OR Wilson schemes p_k(Wilson-i) outside [0.5, 2.5] for any k > 0
  OR fitting reports R² < 0.9 on any (k, s) line

CROSS-CHECK
- Verify p_0(Symanzik) ≈ 4 (a_0 cosmological-constant slot — should
  saturate Symanzik order).
- Verify p_3(Wilson-i) > p_3(Symanzik)/2 (Wilson degraded but not
  catastrophically — sanity bound).
- Cite W12-4 5-regulator atlas (a_0/a_2/a_4 spread 0.50/1.03/0.49)
  AS background; Wilson-1's drift on a_0 should be of comparable OOM.

OUTPUT REQUIRED (4-tuple)
(value=<dict mapping (scheme, slot) → drift_exponent>,
 scheme=W6-2-lattice-Mellin-slot,
 convention=Symanzik-O(a^4)-PASS-band,
 L_max=5)

VERDICT LINE (canonical, dual-SHA per gate-verdicts.md S81+):
  S86-LATTICE-SPACING-IMMUNIZATION-CANDIDATE: PASS|FAIL|INFO --
    value=<min p_k(Symanzik) over k>
    scheme=W6-2-lattice-Mellin-slot
    convention=Symanzik-O(a^4)-PASS-band
    L_max=5
    sha256=<closure>

  Followed by companion row:
  # content_sha256=<sha of script + data outputs>
  # audit_sha256=<sha of ordered input-pin map: D_K cache SHA + scheme
                 list + spacings list + canonical_constants SHA>

DO NOT
- Use numpy.linalg for the eigvalsh step (≥ 100×100 matrices; GPU pin
  is mandatory per feedback_compute-environment.md).
- Hardcode any of: M_KK, tau_fold, Vol_SU3, J_C2 — import from
  canonical_constants.
- Skip the Richardson extrapolation; raw |a_{2k}(a, s) - a_{2k}(a_min,
  s)| underestimates p_k by 1 (well-known lattice-perturbation-theory
  pathology).
- Conflate Wilson-1 / Wilson-2 / Wilson-3 with the Wilson-class label
  in W12-4 atlas — these are 3 SUB-INSTANCES of the Wilson family
  parametrized by r_W ∈ {1.0, 0.5, 1.5}, NOT the W12-4 5-regulator
  atlas members.

[END DISPATCH PROMPT]
```

### §P. Machinery pin (PRDR — W6-2)

| Parameter | PIN | Source |
|:----------|:----|:-------|
| `L_max` | 5 | partition §1 W6 item 2 |
| `scheme` | `W6-2-lattice-Mellin-slot` | this gate |
| `discretization_schemes` | {Wilson-1 (r_W=1.0), Wilson-2 (r_W=0.5), Wilson-3 (r_W=1.5), Symanzik (c_SW=1.0)} | this gate, 4 schemes |
| `lattice_spacings_per_scheme` | {0.500, 0.250, 0.125, 0.0625, 0.03125} M_KK^{-1} | factor-2 refinement, 5 spacings |
| `slots` | k ∈ {0, 1, 2, 3} → (a_0, a_2, a_4, a_6) | 4 spectral moments |
| `d_spec` | 8 | NCG dimension (Connes-Chamseddine spec) |
| `lambda_max` | from D_K cache at L_max=5 | input file pin |
| `extrapolation_method` | 5-point Aitken Δ² Richardson | standard lattice extrapolation |
| `pass_band_Symanzik` | p_k ∈ [3.5, 4.5] for all k | O(a^4) corollary statement |
| `pass_band_Wilson` | p_k ∈ [0.5, 2.5] for k ∈ {1, 2, 3} | degraded-scaling expectation |
| `R²_floor` | 0.9 | fitting acceptability threshold |
| `tolerance_rule` | RATIO (drift exponent is a dimensionless ratio of log-log slopes) | per gate-verdicts.md S81+ |
| `random_seed` | n/a | deterministic eigenvalue computation |
| `GPU path` | torch.linalg.eigvalsh (ROCm 7.2 on AMD RX 9070 XT) | feedback_compute-environment.md mandate |
| `CPU thread cap` | OMP_NUM_THREADS=8 (only if torch unavailable) | math-scripts.md §Environment |
| `schema_version` | R3 | R3 YAML lift required per W0a R3 |
| `cutoff_axis` | spectral (Mellin slot decomposition) | R3 cutoff_axis YAML pin per W0a R3 |
| `regulator_pin_discipline` | mandatory per slot per scheme: `a_{2k}^{Wilson-i, a=...}` | P14 W12-4 carry-forward |

### §O. Expected output 4-tuple

`(value=<dict (scheme, slot) → drift_exponent p_k(s) with R² and Richardson-extrapolated continuum>, scheme=W6-2-lattice-Mellin-slot, convention=Symanzik-O(a^4)-PASS-band, L_max=5)`

### §T. PASS / FAIL / INFO thresholds

Specified in §M dispatch prompt §PRE-REGISTERED PASS BAND. Reproduced here for audit:
- **PASS**: Symanzik p_k ∈ [3.5, 4.5] for ALL k ∈ {0, 1, 2, 3} AND Wilson schemes p_k ∈ [0.5, 2.5] for k ∈ {1, 2, 3} AND fit R² ≥ 0.9 per (k, s).
- **INFO**: Symanzik within [2.5, 3.5] OR [4.5, 5.5] for ≤ 1 slot of 4 (approximately holds on 3 of 4 slots).
- **FAIL**: Symanzik outside [2.5, 5.5] on any slot, OR Wilson p_k outside [0.5, 2.5] for k > 0, OR R² < 0.9 on any (k, s) line.

Tolerance rule: **RATIO** (drift exponent p_k is a log-log slope; band-width measured as additive interval on the slope value, which is itself a ratio quantity).

### §S. Substitution chain — drift-exponent direction (slot-by-slot)

Required because the W6-2 gate makes a direction claim across slots: "p_k INCREASES with k for Symanzik (saturates at 4) AND degrades for Wilson". Substitution chain proves the direction of the inequality the gate tests.

```
Substitution chain (drift-exponent direction across slots, Symanzik scheme):

Step 1 (definition):
  a_{2k}(a, s)         = Σ_i Θ(λ_max - λ_i) · λ_i^{(2k - d_spec)/2}      [Mellin slot, S-1 §IV.5]
  a_{2k}(a→0, s)       = lim_{a → 0} a_{2k}(a, s)                          [continuum extrapolation]
  ε_k(a, s)            = a_{2k}(a, s) - a_{2k}(a→0, s)                     [discretization error per slot]
  p_k(s)               = log-log slope of |ε_k(a, s)| vs a                  [drift exponent per slot]

Step 2 (substitute, Symanzik tree-level):
  Symanzik action removes O(a) and O(a²) discretization terms by
  construction (Symanzik 1983); the leading nonzero contribution to
  |D_K(a, Symanzik) - D_K(continuum)| is O(a^4).
  Spectral moments a_{2k} are smooth functionals of the eigenvalue
  density ρ(λ); discretization errors propagate linearly to leading
  order:
      ε_k(a, Symanzik) = c_k · a^4 + O(a^6)        [c_k slot-dependent constant]

Step 3 (simplify):
  |ε_k(a, Symanzik)| ~ |c_k| · a^4
  log|ε_k(a, Symanzik)| = 4 · log(a) + log|c_k|
  p_k(Symanzik) = 4   for all k ∈ {0, 1, 2, 3}                          [4 ∈ [3.5, 4.5] PASS-band]

Step 4 (direction):
  p_k(Symanzik) = 4 across slots k = 0, 1, 2, 3 → SLOT-INDEPENDENT
  p_k(Wilson-i) = q_k where q_0 = 0 (a_0 absorbs O(1) Wilson noise),
                              q_k = max(1, 2-something) for k > 0
                              (Wilson degrades on higher slots because
                              a_{2k} weights eigenvalues with positive
                              power λ^{(2k-8)/2} → enhanced sensitivity
                              to UV discretization noise as k increases)
  → p_k(Symanzik) ≥ p_k(Wilson-i) for ALL k > 0   (strict inequality)
  → DIRECTION: Symanzik dominates Wilson per slot at k > 0

  PASS condition reads off:
    "Symanzik p_k ∈ [3.5, 4.5] for all k" tests p_k(Symanzik) = 4 ± 0.5.
    "Wilson p_k ∈ [0.5, 2.5] for k > 0" tests degraded but bounded.

  Conclusion: the inequality direction the gate tests is
  p_k(Symanzik) ≥ p_k(Wilson-i) ≥ 0.5 for all k > 0, with Symanzik
  saturating at 4 per slot. PASS verifies this; FAIL falsifies it.
```

### §M-S-S. What PASSES / FAILS MEAN for the solution space

- **PASS**: §VII.S.B C-α-LATTICE corollary holds at slot-by-slot Mellin level. The substrate's spectral content is IMMUNE to lattice discretization at Symanzik O(a^4) per slot — the Dirac operator's spectrum is INSENSITIVE to lattice-spacing perturbations of the regulator at the rate that Symanzik improvement guarantees. Strengthens the §VII.S.B branch as a load-bearing column of the immunization family.
- **FAIL**: Symanzik improvement does NOT propagate slot-by-slot — at least one a_{2k} slot fails to saturate O(a^4). The corollary requires REFINEMENT (e.g., the slot might require additional improvement coefficients beyond tree-level c_SW). Constrains the solution space: §VII.S.B's slot-uniform-improvement claim is FALSIFIED at this slot — corollary holds only on subset of slots.
- **INFO**: Marginal saturation; partial corollary. Bookkeeping update to §VII.S.B: corollary holds on 3 of 4 slots; the failing slot identifies a sub-corridor for S87 refinement.

Substrate framing: the substrate's spectral content is immune to lattice-discretization perturbation Y under condition Z = "Symanzik tree-level improvement applied", at level Z = O(a^4) per Mellin slot.

### §E. Effort estimate

~4-5h MODERATE: 4 schemes × 5 spacings × 1 D_K eigenvalue computation at L_max=5 (~5000² matrix → ~30s on GPU per (s, a) pair → ~10min total compute) + Mellin slot-by-slot integration + Richardson extrapolation + drift-exponent fits + audit substitution-chain documentation.

### §SF. Substrate-framing reminder

The substrate's spectral content is INDEPENDENT of the lattice-discretization apparatus at the rate the Symanzik improvement program guarantees. PASS reports a corridor of insensitivity at order O(a^4); FAIL reports that the corridor is narrower than the claim — that the substrate's spectrum is sensitive to discretization perturbation in a slot-asymmetric way. This is GEOMETRIC: it bounds the substrate's structural floor under one specific class (Y = lattice spacing) of regulator perturbation.

---

## §W6-3. S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM (C42)

**Gate ID**: `S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM`

**Trigger**: `[VERIFY-THEOREM]` (theorem-grade corollary test; parametric bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²` is an inequality that requires substitution chain to confirm direction).

**Classification**: GEOMETRIC (NCG corollary structure; bounds the substrate's spectral-action sensitivity to Weyl rescaling via internally-computed anomaly scale, NOT external Λ pin).

**Owner subagent**: `lizzi-spectral-functional-theorist` (lizzi 9A §E-3 is the source; the parametric bound is a spectral-functional analyst's natural domain — internal Λ_anomaly computation from `Tr_F(Y†Y)` + AC-2010 §V is anomaly-derived spectral action machinery per S66/S67 lizzi work). Co-cite `connes-ncg-theorist` for AC-2010 §V coefficient sourcing if needed.

**Hypothesis (one sentence)**: Under Weyl rescaling g → e^{2σ} g of the substrate metric, the Connes-Chamseddine spectral action S_W satisfies the parametric bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²`, where Λ_anom_internal is computed INTERNALLY from `Tr_F(Y†Y) ` + AC-2010 §V coefficients (no external Λ pin), and b_DK is a Dirac-operator-determined dimensionless constant.

### §M. Method (complete dispatch prompt for `lizzi-spectral-functional-theorist`)

```
[BEGIN DISPATCH PROMPT — W6-3 lizzi-spectral-functional-theorist]

CONTEXT
You are testing §VII.S.D C-γ-WEAK corollary: under Weyl rescaling
g → e^{2σ} g of the substrate metric (or equivalently D → e^{-σ} D on
the spectral triple), the Connes-Chamseddine spectral action S_W
incurs a fractional shift ΔS_W / S_W bounded by a parametric quantity
involving (Λ_anom_internal / Λ_cut)². Λ_anom_internal must be computed
INTERNALLY from the Yukawa-trace Tr_F(Y†Y) plus the Ali-Chamseddine
2010 §V chiral-anomaly coefficients — NO external Λ pin is admissible.

INPUTS (read in order, before any compute)
1. computations/canonical_constants.py — import M_KK, tau_fold,
   v_ew, m_t_pole, Vol_SU3, J_C2.
   PRE-REQ CHECK: confirm `b_DK` is in canonical_constants.py. If
   ABSENT (per knowledge-MCP search at plan-write time, b_DK was NOT
   in canonical_constants), the FIRST step of the script MUST be:
     §M.0  Compute b_DK from D_K spectral data + AC-2010 §V Eq. (5.3)
            (the dimensionless coupling between Weyl-rescaling
            generator and the spectral action's a_4 slot); register
            via mcp__knowledge__update_constant("b_DK", <value>,
            "S86", "AC-2010 §V Eq. (5.3) + W6-3 internal computation",
            "Dirac-operator-determined dimensionless constant for
             Weyl-rescaling weak-form parametric bound")
            BEFORE proceeding to §M.1.
2. AC-2010 chiral-anomaly coefficients — Ali-Chamseddine 2010
   "Spectral action in the presence of a torsion field"; cite §V
   coefficients verbatim (the Weyl-anomaly contribution to the
   spectral action's heat-kernel a_4 coefficient).
3. D_K spectral cache at L_max=10 — locate file path; pin SHA-256.
4. sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md §E-3
   (verbatim parametric-bound derivation, 6-line block); cite in
   script header docstring.
5. sessions/session-plan/session-86-context.md §2.6 C42 entry verbatim.

ENVIRONMENT
- Python: phonon-exflation-sim/.venv312/Scripts/python.exe
- GPU: USE torch.linalg for trace ops on Yukawa matrix Y (3×3 family
  + flavor structure → effective 18×18 or 24×24 once gauge indices
  contracted; if d_eff < 100, GPU not required, but the L_max=10
  D_K matrix (~155984×155984) eigenvalue density evaluation REQUIRES
  GPU torch.linalg.eigvalsh).
  Expected runtime: ~45 min on AMD RX 9070 XT for L_max=10 eigvalsh +
  ~10 min for AC-2010 coefficient matrix evaluation + ~30 min for
  Λ_cut sweep (10 values) → ~1.5h total compute.
  CPU fallback: NOT recommended at L_max=10 (numpy.linalg would take
  ~6h with thread cap; 32-thread mode would contend with parallel W6-2).
- Script: computations/s86_w6_3_weyl_rescaling_weak.py
- Script imports: from canonical_constants import *; import torch;
  import numpy as np; import hashlib;
  from mcp__knowledge__ import update_constant (if b_DK registration
  needed in §M.0).

PROCEDURE
§M.0  PRE-COMPUTE b_DK if missing:
        b_DK = (1 / (8π²)) · Tr_F[(Y†Y)²] / Tr_F[Y†Y]^{2/...}
        per AC-2010 §V Eq. (5.3) — verify exact coefficient form
        against AC-2010 paper before computing.
        Register to canonical_constants.py via update_constant.

§M.1  Compute Λ_anom_internal:
        Λ_anom_internal² = (M_KK² / 16π²) · Tr_F(Y†Y) + AC-2010 §V
                           contribution from chiral-anomaly Eq. (5.2)
        where Tr_F(Y†Y) is the trace over the fermion family +
        flavor space (Yukawa coupling matrix at v_ew anchor).
        Use canonical_constants.py v_ew, m_t_pole for the dominant
        top-Yukawa entry.

§M.2  Sweep Λ_cut over the range [M_KK, 10·M_KK] in 10 logarithmic
        steps (per W12-4 atlas standard cutoff range).

§M.3  For each Λ_cut value:
        a. Compute the spectral action S_W(Λ_cut) via the
           Chamseddine-Connes heat-kernel expansion at L_max=10 from
           the D_K cache (a_0, a_2, a_4 truncation per S77 5-term
           convergence theorem at Lambda=2.048).
        b. Apply Weyl rescaling D → e^{-σ} D with σ = 0.01 (small
           perturbation; verify regime of validity).
        c. Compute S_W(Λ_cut, σ) under rescaled D.
        d. Compute ΔS_W / S_W = (S_W(Λ_cut, σ) - S_W(Λ_cut, 0)) /
                                  S_W(Λ_cut, 0).
        e. Compute parametric upper bound:
             bound(Λ_cut) = b_DK · (Λ_anom_internal / Λ_cut)²
        f. Compute ratio:
             r(Λ_cut) = |ΔS_W / S_W|(Λ_cut) / bound(Λ_cut)
           PASS condition: r(Λ_cut) ≤ 1 across the 10-value sweep.

PRE-REGISTERED PASS BAND (PRDR-pinned BEFORE compute)
PASS:
  r(Λ_cut) ≤ 1.0 for ALL 10 Λ_cut values
    (parametric bound holds over the sweep)
  AND b_DK > 0
    (sign check; b_DK is dimensionless coupling, must be positive
     for the bound to be a meaningful upper bound)
  AND Λ_anom_internal in physical range [M_KK / 100, M_KK · 10]
    (sanity check; Λ_anom_internal should be of order M_KK)

INFO band:
  r(Λ_cut) ∈ (1.0, 2.0] for at most 2 of 10 sweep values
    (bound HOLDS for 8 of 10 — parametric bound is tight but valid;
     S87 refinement may require b_DK adjustment by O(1) factor)

FAIL:
  r(Λ_cut) > 1.0 for 3 or more sweep values
  OR b_DK ≤ 0 (sign violation; bound inverted)
  OR Λ_anom_internal outside physical range

CROSS-CHECK
- Verify σ = 0.01 is in the linear regime: check that
  ΔS_W / S_W = O(σ²); if it scales as O(σ), the perturbation is too
  large or the corollary's quadratic-in-σ structure is violated.
- Cross-check Λ_anom_internal against AC-2010 §V table 1 values for
  Standard Model Yukawa couplings (top-quark dominant).
- Verify that PASS verdict is INDEPENDENT of σ choice for σ ∈ {0.005,
  0.01, 0.02} (linear regime of validity); if PASS depends on σ,
  the bound is convention-shopping (forbidden per
  v3-closure-recovery.md PROHIBITED_ACTIONS #1).

OUTPUT REQUIRED (4-tuple)
(value=<max r(Λ_cut) over 10-value sweep>,
 scheme=W6-3-Weyl-AC-2010-internal,
 convention=parametric-bound-Λ_anom_internal,
 L_max=10)

VERDICT LINE (canonical, dual-SHA per gate-verdicts.md S81+):
  S86-WEYL-RESCALING-IMMUNIZATION-WEAK-FORM: PASS|FAIL|INFO --
    value=<max_r>
    scheme=W6-3-Weyl-AC-2010-internal
    convention=parametric-bound-Λ_anom_internal
    L_max=10
    sha256=<closure>

  Followed by companion row:
  # content_sha256=<sha of script + data outputs>
  # audit_sha256=<sha of ordered input-pin map: D_K cache SHA + AC-2010
                 coefficient pins + canonical_constants SHA + b_DK SHA>

DO NOT
- Use any external Λ pin (e.g., M_GUT, M_Pl, v_ew, M_KK_2 from
  other channels) as Λ_anom — the corollary's WEAK-form requires
  Λ_anom be computed INTERNALLY from D_K + Yukawa data only.
- Hardcode b_DK; if missing from canonical_constants, register via
  §M.0 BEFORE the parametric-bound test (PRDR Class-8 pin closure).
- Use numpy.linalg for the L_max=10 D_K eigvalsh (~155984² matrix);
  GPU pin is mandatory.
- Conflate Λ_anom_internal with Λ_QCD or Λ_GUT — Λ_anom is the
  Yukawa-trace-derived quantity from AC-2010 §V Eq. (5.2), of order
  v_ew · sqrt(Tr_F(Y†Y)) for the SM matter content.
- Re-run with different σ until PASS — σ choice is pre-registered
  at 0.01 (with cross-check at {0.005, 0.02}); changing σ post-hoc
  is iterate-until-PASS (Class-6 prohibition).

[END DISPATCH PROMPT]
```

### §P. Machinery pin (PRDR — W6-3)

| Parameter | PIN | Source |
|:----------|:----|:-------|
| `L_max` | 10 | partition §1 W6 item 3 (HEAVY full-spectrum at production scale) |
| `scheme` | `W6-3-Weyl-AC-2010-internal` | this gate |
| `regulator_class` | AC-2010 §V chiral-anomaly coefficients | partition §1 W6 item 3 |
| `Λ_cut_sweep` | logarithmic [M_KK, 10·M_KK] in 10 steps | this gate, sweep range pre-registered |
| `σ_perturbation` | 0.01 (with cross-check {0.005, 0.02}) | linear-regime validity check |
| `b_DK` | <to be computed in §M.0 if absent from canonical_constants> | AC-2010 §V Eq. (5.3); KNOWLEDGE-MCP CONFIRMED ABSENT at plan-write time |
| `Λ_anom_internal` | computed in §M.1 from `(M_KK² / 16π²) · Tr_F(Y†Y)` + AC-2010 §V | NO external pin admissible |
| `v_ew, m_t_pole` | canonical_constants imports (Yukawa anchor) | math-scripts.md §Canonical Constants |
| `D_K cache SHA` | L_max=10 cache; pinned at runtime | input file pin |
| `Connes-Chamseddine truncation` | a_0, a_2, a_4 (5-term per S77 convergence theorem) | S77 NON-PERT-SA-70 carry-forward |
| `pass_band` | r(Λ_cut) ≤ 1 for all 10 sweep values | this gate, parametric-bound test |
| `info_band` | r(Λ_cut) ∈ (1, 2] for ≤ 2 of 10 sweep values | this gate, INFO clause |
| `tolerance_rule` | RATIO (parametric bound is dimensionless ratio) | per gate-verdicts.md S81+ |
| `random_seed` | n/a | deterministic spectral computation |
| `GPU path` | torch.linalg.eigvalsh (ROCm 7.2) | feedback_compute-environment.md mandate |
| `expected_runtime` | ~1.5h total (45 min eigvalsh + 10 min coefficients + 30 min sweep) | HEAVY single-gate compute |
| `schema_version` | R3 | R3 YAML lift required per W0a R3 |
| `cutoff_axis` | both (spectral Λ_cut + coherence-class via Yukawa Y) | R3 cutoff_axis YAML pin per W0a R3 |
| `regulator_pin_discipline` | mandatory: `S_W^{Λ_cut, σ, AC-2010}` | P14 W12-4 carry-forward |

### §O. Expected output 4-tuple

`(value=<max r(Λ_cut) over 10-value sweep, with companion logged b_DK + Λ_anom_internal + per-Λ_cut breakdown>, scheme=W6-3-Weyl-AC-2010-internal, convention=parametric-bound-Λ_anom_internal, L_max=10)`

### §T. PASS / FAIL / INFO thresholds

Specified in §M dispatch prompt §PRE-REGISTERED PASS BAND. Reproduced here for audit:
- **PASS**: r(Λ_cut) ≤ 1.0 for all 10 sweep values AND b_DK > 0 AND Λ_anom_internal ∈ [M_KK/100, 10·M_KK].
- **INFO**: r(Λ_cut) ∈ (1.0, 2.0] for ≤ 2 of 10 sweep values (bound holds 8/10).
- **FAIL**: r(Λ_cut) > 1.0 for ≥ 3 sweep values, OR b_DK ≤ 0, OR Λ_anom_internal outside physical range.

Tolerance rule: **RATIO** (the gate quantity r is a ratio of two dimensionless quantities; the bound `|ΔS_W / S_W|` is itself a ratio).

### §S. Substitution chain — parametric-bound inequality direction

Required because the W6-3 gate makes a direction claim (the parametric bound is an upper bound; r ≤ 1 PASS direction). Substitution chain proves the inequality the gate tests is well-defined and the direction is correctly oriented.

```
Substitution chain (parametric-bound direction, weak-form Weyl rescaling):

Step 1 (definition):
  S_W(Λ_cut)             = Σ_k f_k · a_k(D²/Λ_cut²)         [Chamseddine-Connes 1996]
                            with f_0, f_2, f_4 the moments of the cutoff function
                            f and a_k the Seeley-DeWitt coefficients
  σ                      = small Weyl rescaling parameter (PIN: 0.01)
  D → e^{-σ} D           = Weyl rescaling action on Dirac operator
  ΔS_W                   = S_W(Λ_cut, D → e^{-σ} D) - S_W(Λ_cut, D)
  Λ_anom_internal²       = (M_KK² / 16π²) · Tr_F(Y†Y) + AC-2010 §V Eq. (5.2)
                            chiral-anomaly contribution
                                                              [AC-2010, internal]
  b_DK                   = (1/8π²) · Tr_F[(Y†Y)²] / [Tr_F(Y†Y)]^{?}  [AC-2010 §V Eq. (5.3); §M.0 computes]

Step 2 (substitute, leading order in σ):
  Under Weyl rescaling D → e^{-σ} D:
    a_4 → a_4 · e^{-2σ}  ≈ a_4 · (1 - 2σ + 2σ² + O(σ³))
    a_2 → a_2 · e^{0σ}   = a_2  (a_2 conformally invariant in 4D up to anomaly)
    a_0 → a_0 · e^{2σ}   ≈ a_0 · (1 + 2σ + 2σ² + O(σ³))
  Anomaly contribution (AC-2010 §V Eq. (5.1)):
    ΔS_W^{anomaly} = b_DK · (Λ_anom_internal² / Λ_cut²) · σ²
                       · S_W^{Weyl-ledger-class}        [leading-order anomaly]
  Plus the trivial geometric contribution (a_0 / a_4 cancellation
  to leading O(σ); see Chamseddine 1996 Eq. 2.7) which gives:
    |ΔS_W / S_W|_{geom}    ≤ O(σ²)        [smaller than anomaly piece by Λ ratio]
  Therefore:
    |ΔS_W / S_W|         = |ΔS_W^{anomaly} / S_W| · (1 + O(σ²-corrections))
                          ≤ b_DK · (Λ_anom_internal / Λ_cut)² · σ² · O(1)
                                                                  [1st upper bound]

Step 3 (simplify):
  Drop σ² (held fixed at PIN value 0.01²; absorbed into the
  parametric-bound RHS by σ²-fold of the inequality):
    |ΔS_W / S_W|(Λ_cut)  ≤ b_DK · (Λ_anom_internal / Λ_cut)²
                                                        [the gate's parametric bound]

  This is the corollary statement to test. Define:
    r(Λ_cut)   ≡ |ΔS_W / S_W|(Λ_cut) / [ b_DK · (Λ_anom_internal / Λ_cut)² ]
  PASS condition: r(Λ_cut) ≤ 1 for all sweep values (the bound holds
  over the full Λ_cut range [M_KK, 10·M_KK]).

Step 4 (direction):
  The bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²` is an
  UPPER BOUND on the LHS. The direction of the gate's PASS condition
  is therefore "LHS ≤ RHS", equivalently "r ≤ 1".
  As Λ_cut increases, the RHS DECREASES as Λ_cut^{-2}; the LHS is
  determined by the spectral action's actual response and is
  expected to scale at WORST as Λ_cut^{-2} (since the anomaly is the
  leading non-vanishing contribution at fixed σ²).
  → The inequality direction is PRESERVED across the Λ_cut sweep IFF
    the corollary holds; FAILED if any Λ_cut produces r > 1 in
    excess of the INFO band (which absorbs O(1) refinement in b_DK).

  Conclusion: the inequality direction tested is r(Λ_cut) ≤ 1 across
  10 logarithmic Λ_cut values; PASS verifies the corollary holds in
  this direction; FAIL falsifies the parametric upper bound at
  internal Λ_anom; INFO band absorbs O(1) refinement of b_DK.
```

### §M-S-S. What PASSES / FAILS MEAN for the solution space

- **PASS**: §VII.S.D C-γ-WEAK corollary holds at L_max=10 across the Λ_cut sweep [M_KK, 10·M_KK]. The substrate's spectral action is IMMUNE to Weyl rescaling at the parametric rate `b_DK · (Λ_anom_internal / Λ_cut)²` — and the bound is achieved INTERNALLY from `Tr_F(Y†Y)` + AC-2010 §V coefficients without any external Λ pin. This strengthens §VII.S.D as a load-bearing corollary AND closes a long-standing convention-shopping vulnerability in spectral-action Weyl-rescaling discussions (where Λ_anom was historically treated as an external pin).
- **FAIL**: The parametric bound does NOT hold at internal Λ_anom — at least 3 of 10 Λ_cut values produce r > 1. Constrains the solution space: §VII.S.D's WEAK-form corollary is FALSIFIED at this regulator class; either the corollary requires the STRONG form (b_DK adjustment + sub-leading anomaly contributions), or the external-pin formulation is necessary (which would weaken the immunization claim from internal-self-consistent to external-pin-conditional).
- **INFO**: Marginal; bound holds 8/10 with O(1) margin on the failing 2 sweep values. S87 refinement: re-derive b_DK with sub-leading AC-2010 §V Eq. (5.4) corrections; or absorb the failing sweep values into a refined Λ_cut range pre-registration.

Substrate framing: the substrate's spectral content is immune to Weyl-rescaling perturbation Y under condition Z = "Λ_anom computed internally from Yukawa-trace + AC-2010 §V coefficients", at level Z = "parametric bound `b_DK · (Λ_anom / Λ_cut)²` over Λ_cut ∈ [M_KK, 10·M_KK]".

### §E. Effort estimate

~6-8h HEAVY: §M.0 b_DK registration (~1h, including AC-2010 paper coefficient verification); §M.1 Λ_anom_internal computation (~30min); §M.2 + §M.3 sweep over 10 Λ_cut values × eigvalsh at L_max=10 (~1.5h GPU compute); audit substitution-chain documentation + cross-check σ-sensitivity (~1h); verdict-line + dual-SHA + W6-1 registry back-link update (~30min).

### §SF. Substrate-framing reminder

The substrate's spectral content is INDEPENDENT of Weyl-rescaling perturbations of the metric at the parametric rate set by AC-2010 §V chiral-anomaly coefficients combined with the substrate's own Yukawa structure. The corollary closes the long-standing question of whether the spectral action's Weyl response can be bounded WITHOUT importing an external cutoff scale; PASS confirms the bound is internally self-consistent. This is GEOMETRIC: it bounds the substrate's structural floor under one specific class (Y = Weyl rescaling) of metric perturbation, using only D_K data + Yukawa data + AC-2010 anomaly coefficients (all internally specified).

---

## §X. Wave W6 → Downstream Decision Point

| Outcome of W6 wave | Downstream effect |
|:-------------------|:------------------|
| W6-1 PASS (registry) + W6-2 PASS + W6-3 PASS | §VII.S immunization-family LANDED with 4 of 9 corollaries closed (2 zero-compute via W1c C41 + 2 attempted-PASS via W6-2/W6-3); S87 dispatches the 4 deferred corollaries (C-δ/ε/ζ/ι) into the §VII.S landing slots; the 1C cascade is on track to S87 closure |
| W6-1 PASS + (W6-2 FAIL OR W6-3 FAIL) | Registry parent is landed but the corresponding corollary row (§VII.S.B for W6-2 FAIL; §VII.S.D for W6-3 FAIL) is marked `STATUS: FAILED-S86`; constrains the solution space: the substrate is NOT IMMUNE to perturbation Y at the claimed level; S87 dispatch addresses corollary refinement (e.g., STRONG form for §VII.S.D; sub-slot resolution for §VII.S.B) |
| W6-1 PASS + W6-2 INFO + W6-3 INFO | Registry parent landed; both attempted corollaries marked `STATUS: ATTEMPTED-INFO-S86` with band-width annotation; S87 refines b_DK and Symanzik improvement coefficient |
| W6-1 FAIL | Halt downstream W6-2/W6-3 verdict-line writes (the registry slots they reference do not exist in the documented form); dispatch a single-item rescue wave to repair the §VII.S parent registry write before re-attempting W6-2/W6-3 |

**S87 carry-forward implication**: PASS on all 3 W6 gates UNBLOCKS the S87 dispatch of C2 corollaries C-δ/ε/ζ/ι (currently deferred per partition §2). FAIL on either W6-2 or W6-3 BLOCKS the corresponding S87 corollary refinement until its parent corollary's failure mode is diagnosed.

**Cross-wave consistency**: W6-3's `b_DK` registration in §M.0 may surface the constant for downstream use — W7 (C1 joint CC residue) does NOT use b_DK; W9 (C24 §VII.P-v2 parity-extension) does NOT use b_DK; W10 (C37 ZFP discharge) does NOT use b_DK. b_DK is therefore §VII.S.D-specific at S86 close; the registration is forward-compatible with later spectral-action Weyl-rescaling work but does not introduce cross-wave contamination at S86.

---

## §0.10. Wave W6 Machinery-Enumeration Pin

Per `epistemic-discipline.md` §Pre-Registration Completeness, W6's machinery is fully enumerated above in §P blocks per gate. The PRDR audit should report 0 free parameters at compute-time for any of the 3 W6 gates. Specifically:

- **W6-1**: 9 PRDR parameters pinned (corollary_count, IEP partition, status distribution, column set, verdict path, dual-SHA template, tolerance rule, random seed, GPU path).
- **W6-2**: 16 PRDR parameters pinned (L_max, scheme, 4 discretization schemes, 5 lattice spacings, 4 slots, d_spec, lambda_max, extrapolation method, 2 PASS bands, R² floor, tolerance rule, GPU path, CPU thread cap, schema_version, cutoff_axis, regulator-pin discipline).
- **W6-3**: 18 PRDR parameters pinned (L_max, scheme, regulator class, Λ_cut sweep, σ perturbation, b_DK registration step, Λ_anom_internal formula, Yukawa anchors, D_K cache SHA, Connes-Chamseddine truncation, PASS/INFO bands, tolerance rule, GPU path, expected runtime, schema_version, cutoff_axis, regulator-pin discipline, prohibited-actions list).

PRU Class-8 vulnerability check: W6-3 has ONE conditional pin (b_DK is computed in §M.0 if absent from canonical_constants — a runtime branch). This is acceptable per `epistemic-discipline.md` because the branch is documented at plan-write time, the condition is machine-decidable (`canonical_constants.b_DK` exists or does not), and the remediation (compute via AC-2010 §V Eq. (5.3)) is enumerated.

PRDR Dry-Run sign-off: per `_yaml_gate_validator.py` standard, dispatch the validator on this plan file post-write to confirm 0 PRU residue.

---

## §0.11. Wave W6 Input-SHA Ledger

| Source / dependency | SHA pin status | Pinned at |
|:--------------------|:---------------|:----------|
| `computations/canonical_constants.py` | <runtime>: SHA computed at compute time and recorded in input-pin map | each gate's audit_sha256 |
| `sessions/permanent-results-registry.md` §VII.S parent body | <runtime>: post-W1a-T3 landing; W6-1 verifies presence | W6-1 §M Step 1 |
| W1c C41 verdict line (`S86-VII-S-C-ETA-LANDING + S86-VII-S-C-THETA-LANDING`) | <runtime>: located via grep in `computations/s86_gate_verdicts.txt`; W6-1 copies the SHA into §VII.S.η/θ rows | W6-1 §M Write Target 1 |
| D_K spectral cache at L_max=5 (W6-2 input) | <runtime>: SHA computed at compute time | W6-2 audit_sha256 |
| D_K spectral cache at L_max=10 (W6-3 input) | <runtime>: SHA computed at compute time | W6-3 audit_sha256 |
| AC-2010 §V coefficients (Ali-Chamseddine 2010) | external paper; verbatim cite + page reference | W6-3 §M Step 2 (script docstring) |
| `sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md` §E-1 (W6-2) and §E-3 (W6-3) | <runtime>: SHA computed at compute time | each gate's audit_sha256 |
| `sessions/session-plan/session-86-context.md` §1.5 + §2.6 (C2, C40, C41, C42) | <runtime>: SHA computed at compute time | each gate's audit_sha256 |

All input SHAs are pinned at compute time per `.claude/templates/script-template.py` Section 4 (the canonical script template logs each input SHA in the first 20 lines of stdout and emits the closure hash from the ordered input-pin map).

**Per `gate-verdicts.md`**: closure SHA is the SHA-256 of the ordered input-pin map for each gate and MUST be the full 64-character hexdigest in the canonical verdict line. Companion row carries `content_sha256` (script + data outputs) and `audit_sha256` (input-pin map closure) per W9a-99 dual-SHA template.

---

**End of W6 plan.** Three full gate blocks (W6-1, W6-2, W6-3) — registry-write umbrella + 2 theorem-grade corollary candidates. Wave dispatches all three items in S86 Batch 2 per partition §4; W6-2 and W6-3 may run in parallel after W6-1 completes; deferred corollaries (C-δ/ε/ζ/ι) carried to S87.
