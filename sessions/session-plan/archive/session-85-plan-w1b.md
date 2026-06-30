# Session 85 Plan — Wave W1b: mack-origin reviewer wave (split 2/2)

**Generated**: 2026-04-21
**Owner**: mack-cosmic-bridge
**Wave theme**: mack-origin sole-reviewer carry-forward — detector-forecast rigor, cross-channel correlation, joint-Fisher, pre-registration landing, and event-driven live-watch matrices
**Item count**: 10
**Output verdict file** (MANDATORY canonical path): `computations/s85_gate_verdicts.txt`
**Script prefix**: `s85_w1b_`
**Working-paper section anchor**: `§VII.W1b`
**Plan freeze**: 2026-04-21 at dispatch time; no post-hoc threshold edits.

---

## Wave W1b Summary

W1b is the second half of the mack-cosmic-bridge sole-reviewer bucket after
W1a (live-watch + flagship pre-reg + multi-D Fisher skeleton). W1b closes
out the remaining mack-origin carry-forward: correlated-detector Fisher,
prior-range formalization for Bayes-factor statements, cross-registry
contradiction resolution (S62 n_s / transit PS-67), multi-experiment
simultaneous-fit consistency (β_s across CMB-S4 × CMB-HD), replacing
agent-projected detector sensitivities with published verified forecasts
(MacInnis for CMB-HD, Hazumi for LiteBIRD), 2025–2026 Planck+DESI
recalibration of canonical n_s central, a layer-interface theorem
promotion (the GENUINE-UNPINNED PRU item from W2-19), and the α_s ×
w_a decoupled-joint evidence ledger.

The wave is deliberately detector-facing: 6 of 10 items are observational
forecast or pre-registration-landing; 2 are cross-registry audits (prior
range, S62 contradiction); 1 is a structural theorem promotion (layer
interface r_max); 1 is the decoupled-joint evidence ledger. None of the
10 requires new substrate computation — they are **pre-registration,
audit, and Fisher** work that pins what S86+ sessions will watch when
DR3 (2026-04-23), CMB-S4 timeline, LiteBIRD timeline, and CMB-HD forecast
papers land. Substrate framing: every gate treats detectors as
substrate-probing-substrate through the phononic fiber-resonance relay;
forecasts are sensitivity to specific spectral moments of D_K, not
abstract numerical inputs.

Concurrency policy: CPU-only. All 10 scripts are Fisher-matrix
evaluations, JSON I/O, or linear-algebra bookkeeping well under the
GPU-crossover threshold (100×100 matrix). Each script MUST set
`os.environ.setdefault('OMP_NUM_THREADS', '8')` before `import numpy`.

---

## Wave W1b Decision Point Prerequisites

Before any W1b gate appends a verdict line, the agent MUST:

1. Read canonical w_0 pin: `mcp__knowledge__get_constant("w0_FW")` → must
   return **−0.918** (R_842 rectangle post-branch-iv retraction per S83
   W0 regulator-audit R3). If this returns a different value, HALT and
   mark PRE-REG-INCOMPLETE.
2. Confirm `canonical_constants.py` exports `n_s_canon`, `alpha_s_canon`,
   `r_canon`, `f_conv`, `c_S_canon`, `Delta_BCS`, `v_ew`. Missing →
   add with provenance BEFORE running the gate.
3. Confirm DR3 registered rectangle `R_842 = [-0.94, -0.82] × [-0.12, +0.12]`
   is the post-S84 W1b-9 locked rectangle (content_sha=9cc7f47e...79d9f).
   If the orchestrator-visible lock drifted, HALT and Stage-3 trigger.
4. Verify `s85_gate_verdicts.txt` exists at `computations/` (the
   canonical path per `.claude/rules/gate-verdicts.md`); if the session
   opened it at `sessions/archive/session-85/s85_gate_verdicts.txt`, that is a
   documentation bug — append to the canonical path anyway.

Input-pin hashes for shared read-only files (static, precomputed
2026-04-21) are cataloged in the Wave W1b Input-SHA Ledger at the
bottom of this document.

---

## §W1b-1. S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE

**Gate ID**: S85-W1b-CF-M2-REGULATOR-CONDITIONAL-DR3-TREE

**Trigger**: [AUDIT]

**Classification**: META (pre-registration extension; observational binding)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The S84 W4-44 fine-grained DR3 contingency matrix
(7 cells A1/A2/B1/B2/B3/C1/C2, sha=801e4690) is regulator-agnostic — it
assumes the framework prediction is the single canonical value
w_0 = −0.918. The carry-forward hypothesis tests whether amending the
7-cell matrix with a **layered regulator-branch condition** (so each
cell carries 3 sub-verdicts: {L_max=8, L_max=10, L_max=12}) preserves
rectangle R_842 containment across all regulator layers, or reveals a
regulator-layer-specific exclusion in at least one DR3 cell. This
binds W0-L-inverted-branch-enumeration (kaku W10 carry-forward) and
Zubarev-L_max-convergence-to-minus-one (W0 carry-forward) to the
observational DR3 tree.

**Method** (self-contained):
```python
# s85_w1b_cf_m2_dr3_regulator_tree.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np, json, hashlib, sys
sys.path.insert(0, 'computations/_shared')
from canonical_constants import w0_FW  # -0.918
# Read S84 W4-44 locked 7-cell rectangle matrix
with open('computations/s84_w4_44_dr3_contingency_fine_grained.json') as f:
    cells = json.load(f)  # 7-cell locked registry
# For each cell, enumerate L_max sub-verdicts using s85 precomputed
# spectrum caches (pinned below). Output: 7x3 verdict matrix + SHA.
L_levels = [8, 10, 12]  # (local) regulator-layer pins
# ... (structural matrix assembly; no numerical freedom)
# Output: s85_w1b_cf_m2_dr3_regulator_tree.{json,npz,png}
# Verdict-line append to computations/s85_gate_verdicts.txt
```
- CPU-only, numpy.linalg for the containment check (7×3 = 21 cells,
  far below GPU crossover).
- Input SHAs pinned: S84 W4-44 matrix, canonical_constants.py,
  s85_w1b_cf_m2_dr3_regulator_tree.py (see Ledger).
- Output: `computations/s85_w1b_cf_m2_dr3_regulator_tree.py`,
  `computations/s85_w1b_cf_m2_dr3_regulator_tree.npz`,
  `computations/s85_w1b_cf_m2_dr3_regulator_tree.png`
  (21-cell heatmap: cell × L_max → in/out R_842).

**Machinery pin (PRDR)**:
- `L_max` ∈ {8, 10, 12} (enumerated, not scanned)
- `scheme`: Zubarev (canonical S84 W4-46 regulator)
- `convention`: R_842 rectangle (post-branch-iv retraction, S83 R3)
- `tolerance`: RATIO — cell IN iff w_0(L_max) ∈ [−0.94, −0.82] AND
  w_a(L_max) ∈ [−0.12, +0.12]
- `random_seed`: N/A (deterministic enumeration)
- `GPU path`: disabled (CPU threads=8)

**Expected output 4-tuple**:
`(value=<7x3-matrix>, scheme=Zubarev, convention=R_842, L_max=enumerated{8,10,12})`

**PASS/FAIL/INFO thresholds**:
- **PASS**: all 21 cells preserve their S84 W4-44 verdict across all 3
  L_max layers (regulator-invariance holds within DR3 observational
  box)
- **FAIL**: at least one cell flips IN→OUT (or OUT→IN) when L_max
  changes by 2 — regulator-layer-dependent DR3 exclusion
- **INFO**: mixed (some cells regulator-robust, others not); emit cell-
  specific flag table

**Substitution chain** (containment, not a direction claim):
The claim is membership of the framework point (w_0(L), w_a(L)) in
R_842. No sign claim; the substitution chain is bookkeeping:
```
Step 1: R_842 := [w_0^min, w_0^max] × [w_a^min, w_a^max]
        = [−0.94, −0.82] × [−0.12, +0.12]     (S83 W0 R3 lock)
Step 2: For L ∈ {8, 10, 12}:
          (w_0(L), w_a(L)) := output of Zubarev L_max=L script
Step 3: IN_R842(L) := (w_0^min ≤ w_0(L) ≤ w_0^max)
                 AND (w_a^min ≤ w_a(L) ≤ w_a^max)     (boolean)
Step 4: Cell matrix: M[i, L] := {IN, OUT} for cell i ∈ {A1..C2}
Step 5: Direction: M is an output, not a claim; read from the matrix.
```

**What PASS/FAIL means**:
- **PASS** — the DR3 pre-registration tree is regulator-robust; a
  single tree suffices for 2026-04-23 firing. The S86 live-watch is
  reduced to a single-tree lookup.
- **FAIL** — the DR3 tree is regulator-conditional; S86 must maintain
  3 sub-trees, and DR3-event adjudication becomes regulator-first.
  This would be a structural finding: the DR3 box itself is no longer
  a sufficient observational pin.
- **INFO** — regulator-layer dependence is cell-specific; emit the
  table for S86 carry-forward.

**Effort**: 0.5 session-units (pure bookkeeping + containment check;
no new substrate computation).

**Substrate framing**: DR3 probes the impedance-mismatch leakage
(Γ = 0.99970) at the emergent-metric scale. The three L_max layers
probe the same substrate at three truncation depths of D_K. A
regulator-layer-invariant DR3 verdict means the observable reflects a
substrate property that is already converged at L_max=8; a regulator-
dependent verdict means DR3 is sensitive to high-eigenvalue tails of
D_K, which would be a genuine spectral-geometry signature.

---

## §W1b-2. S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED

**Gate ID**: S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED

**Trigger**: [VERIFY]

**Classification**: META (Fisher-matrix formalism; detector-level)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The W1a-9 MULTID-FISHER skeleton assumes
**diagonal** detector correlation across CMB-S4 × LiteBIRD × CMB-HD ×
DESI-DR3 × LISA. A realistic correlation matrix is BLOCK-diagonal,
not fully diagonal: CMB-S4 and LiteBIRD share atmospheric + galactic
foreground (ρ ≈ 0.15 at low-ℓ), CMB-S4 and CMB-HD share partial sky
overlap (ρ ≈ 0.30 for α_s modes), DESI and LISA are independent.
Propagating the realistic off-diagonal block reduces the effective
Fisher determinant → widens the joint posterior → softens the
advertised W1a-9 joint σ(α_s).

**Method**:
```python
# s85_w1b_alpha_s_joint_fisher_correlated.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np, json, hashlib
# 5x5 detector correlation matrix C; diagonal = 1, off-diagonals
# pre-registered from public survey papers (CMB-S4 2019 CDR, LiteBIRD
# 2022 JLTP, CMB-HD 2022 MacInnis, DESI 2016 Aghamousa, LISA 2017)
# Load diagonal Fisher F_diag from W1a-9 output
# Rescale: F_corr = L^T F_diag L where L = Cholesky(C)^{-1}
# Invert → posterior covariance C_post = F_corr^{-1}
# Marginalized σ(α_s) := sqrt(C_post[α_s, α_s])
# Compare σ_corr / σ_diag (ratio reported as pre-registered observable)
```
- 5×5 matrix, trivially CPU. `numpy.linalg.cholesky` + `numpy.linalg.inv`.
- Input SHAs: W1a-9 output (dynamic, `<computed-at-runtime>`),
  `canonical_constants.py`, the 5-entry correlation JSON from this plan.
- Output: `s85_w1b_alpha_s_joint_fisher_correlated.{py,npz,png}`;
  PNG shows diagonal vs correlated posterior ellipse.

**Machinery pin (PRDR)**:
- `N_detectors = 5` (CMB-S4, LiteBIRD, CMB-HD, DESI-DR3, LISA)
- `correlation_matrix`: 5×5 with off-diagonals pre-registered in
  `s85_w1b_alpha_s_correlation_matrix.json` (see Input-SHA Ledger)
- `scheme`: Fisher-marginalized σ(α_s); no MCMC
- `convention`: Gaussian posterior assumption (pre-registered; not
  relaxed in this gate)
- `scan_range`: N/A (single-point matrix evaluation)
- `tolerance`: ABSOLUTE — ratio σ_corr / σ_diag reported to 3 sig-figs
- `random_seed`: N/A (deterministic)
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<σ_corr/σ_diag>, scheme=Fisher-marg-Gaussian, convention=block-diag-C, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: σ_corr / σ_diag ≤ 1.25 (realistic correlation widens
  joint σ(α_s) by ≤25%; W1a-9 advertised sensitivity remains
  defensible within 1σ)
- **FAIL**: σ_corr / σ_diag > 1.50 (correlation collapses W1a-9
  advertised joint-σ by >50%; the multi-D Fisher claim requires
  restatement)
- **INFO**: 1.25 < ratio ≤ 1.50 (borderline; emit full 5×5
  marginalization table)

**Substitution chain**:
```
Step 1: F_diag := diag(1/σ_i²) for i ∈ {S4, LB, HD, DR3, LISA}     (W1a-9 input)
Step 2: C := 5×5 correlation matrix, symmetric, C_ii = 1            (pre-reg)
Step 3: Σ := diag(σ_i); Cov := Σ · C · Σ                            (definition)
Step 4: F_corr := Cov^{-1}                                          (Fisher identity)
Step 5: Simplify: if C = I (diagonal), F_corr = F_diag, ratio = 1   (sanity)
Step 6: If any |C_ij| > 0, det(C) < 1 ⇒ det(Cov) > det(Σ²) for the
        same diagonal ⇒ F_corr "smaller" in Loewner order
        ⇒ σ_corr ≥ σ_diag (Cauchy-Schwarz on Fisher info)          (canonical)
Step 7: Direction: σ_corr ≥ σ_diag, ratio ≥ 1.                     (direction read)
Conclusion: Off-diagonal correlation WIDENS posterior. Magnitude is
the output; the direction is structural.
```

**What PASS/FAIL means**:
- **PASS** — multi-D Fisher claim from W1a-9 survives realistic
  correlation; joint σ(α_s) is within 25% of advertised.
- **FAIL** — advertised sensitivity must be restated with block-C
  penalty; W1a-9 pre-registration row is revised.

**Effort**: 0.5 session-units (5×5 linear algebra; literature pull for
off-diagonals).

**Substrate framing**: Detector correlation is fiber-mode overlap at
the instrument-atmosphere boundary: two detectors share substrate
excitations through their sky-footprint intersection. Block-diagonal
C reflects which detector pairs probe overlapping regions of the
emergent g_M on the same substrate patch.

---

## §W1b-3. S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM

**Gate ID**: S85-W1b-ALPHA-S-PRIOR-RANGE-LCDM

**Trigger**: [AUDIT]

**Classification**: META (Bayes-factor prior-range formalization)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The framework's α_s Bayes-factor claims (BF ≈ 1000
for zero-geometric-free-parameter prediction) depend on the LCDM
prior range used to compute the marginal likelihood ratio. S84 and
earlier sessions used an informal Planck-posterior-inspired range.
This gate formalizes the prior range as **3 pre-registered options**
(uniform on [−0.05, +0.05], uniform on [−0.02, +0.02],
Planck-2018-posterior-Gaussian(μ=−0.0045, σ=0.0067)) and computes the
framework BF under each. The test is whether the BF claim is
**prior-robust**: does the preferred-model conclusion survive prior-
range variation?

**Method**:
```python
# s85_w1b_alpha_s_prior_range_lcdm.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np, json
from scipy.stats import norm
# 3 pre-registered priors
priors = {
    'wide_uniform':    {'type': 'uniform', 'lo': -0.05, 'hi': +0.05},
    'narrow_uniform':  {'type': 'uniform', 'lo': -0.02, 'hi': +0.02},
    'planck_gauss':    {'type': 'gauss',   'mu': -0.0045, 'sig': 0.0067},
}
# Framework prediction: alpha_s_canon (point mass, 0 free params)
# Observational: Planck 2018 α_s = −0.0045 ± 0.0067
# BF = L(α_s_canon | data, framework) / marg_L(α_s | data, LCDM, prior)
# For point-mass framework, L_framework = N(α_s_canon | obs, σ_obs)
# For LCDM with prior π, marg_L = ∫ N(α | obs, σ_obs) π(α) dα
```
- Pure CPU, 3 one-D integrals.
- Input SHAs: canonical_constants.py (for alpha_s_canon), Planck 2018
  measurement tuple (pinned in plan).
- Output: `s85_w1b_alpha_s_prior_range_lcdm.{py,npz,png}`; PNG shows
  BF vs prior width (3 points + trendline).

**Machinery pin (PRDR)**:
- `priors`: exactly the 3 above (frozen at plan-write)
- `framework_alpha_s`: `alpha_s_canon` from canonical_constants.py
- `data_likelihood`: Planck 2018 TT,TE,EE+lowE+lensing: α_s = −0.0045 ± 0.0067
- `scheme`: marginal-likelihood ratio (Bayes factor)
- `convention`: flat prior on framework model (BF, not posterior odds)
- `integration_tolerance`: 1e-10 (scipy quad)
- `random_seed`: N/A
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<BF_tuple_3_priors>, scheme=marg-L-ratio, convention=flat-model-prior, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: BF > 30 (decisive evidence, Jeffreys scale) for all 3
  priors — the α_s framework advantage is prior-robust
- **FAIL**: BF < 3 (inconclusive) for at least 1 of the 3 priors —
  claim is prior-sensitive and must be restated
- **INFO**: 3 ≤ BF ≤ 30 for any prior (substantial but not decisive);
  publish full BF triple

**Substitution chain**:
```
Step 1: L_fw(α_canon) := N(α_canon | α_obs, σ_obs)                  (definition)
Step 2: For prior π:
          marg_L_LCDM := ∫ N(α | α_obs, σ_obs) π(α) dα                (definition)
Step 3: BF(π) := L_fw(α_canon) / marg_L_LCDM(π)                     (definition)
Step 4: For π = uniform on [L, H] with (H-L) >> σ_obs:
          marg_L_LCDM ≈ 1/(H - L) · ∫ N dα ≈ 1/(H - L)             (wide-prior limit)
Step 5: BF ≈ (H - L) · L_fw(α_canon)                                 (simplified)
Step 6: Wider prior ⇒ LARGER BF (framework prefered more strongly)  (direction)
Step 7: BF is MONOTONIC in prior width; prior-robustness is the
        range over [narrowest, widest] pre-reg'd window.             (direction read)
Conclusion: BF increases with prior width; report the triple and
the min(BF) across the 3 priors as the robustness statistic.
```

**What PASS/FAIL means**:
- **PASS** — α_s BF claim survives prior-range variation; the
  framework's prior-free advertisement is mathematically defensible.
- **FAIL** — BF depends on prior choice; the advertised advantage
  must be restated with an explicit prior-range disclosure, OR the
  framework must pre-register its preferred prior.

**Effort**: 0.5 session-units (3 one-D integrals).

**Substrate framing**: Bayes factors are comparisons of likelihood
sums over alternative fiber-mode configurations of D_K. The LCDM
prior is the "set of nearby substrate realizations with free α_s";
prior width sets how far the comparison samples into the space of
non-framework spectral triples. Prior-robustness means the framework
point in spectral-triple space is genuinely isolated, not a fluke
of the sampling window.

---

## §W1b-4. S85-W1b-ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS

**Gate ID**: S85-W1b-ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS

**Trigger**: [AUDIT]

**Classification**: META (cross-registry contradiction resolution)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The S62 canonical registry entry and S67 transit
power-spectrum gate report two α_s values that superficially
disagree. S62 records n_s = 0.9567 (via spectral-moment derivation)
and α_s ≈ 0; S67 transit PS computes α_s via Mukhanov-Sasaki running
through the fold. The two are computed in different conventions —
S62 is `scheme=spectral-zeta` at one regulator, S67 is
`scheme=transit-Mukhanov-Sasaki` at another. The gate audit: (a)
reproduce both numbers under their declared conventions, (b) write
the convention-translation map, (c) state whether the two numbers
agree under a shared pivot scheme, (d) if they disagree,
pre-register which of the two is the observation-facing canonical
entry for CMB-S4 / LiteBIRD / CMB-HD.

**Method**:
```python
# s85_w1b_alpha_s_transit_ps_67_simultaneous.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np, json, hashlib
# Load S62 registry row (alpha_s_S62) and S67 gate output (alpha_s_S67)
# Re-derive both under a single pre-registered scheme (spectral-zeta at
# k_pivot = 0.05 Mpc^-1, Planck convention).
# Compute: Δα = alpha_s_S62_shared - alpha_s_S67_shared
# Pre-register: if |Δα| < 0.5 × σ_Planck (0.0067/2 = 0.00335), convergence PASS
```
- CPU-only; re-derivation reads precomputed spectra (S62, S67).
- Input SHAs: S62 canonical row JSON, S67 gate verdict line, canonical_constants.py.
- Output: `s85_w1b_alpha_s_transit_ps_67_simultaneous.{py,npz,png}`;
  PNG shows both values, shared-pivot reconciliation, σ_Planck band.

**Machinery pin (PRDR)**:
- `pivot_k`: 0.05 Mpc^-1 (Planck)
- `scheme`: spectral-zeta at k_pivot (shared convention for the audit)
- `convention_map`: S62 and S67 conventions documented; translation
  formula pre-registered in plan (see Substitution chain)
- `tolerance`: RATIO — agreement iff |Δα_s_shared| < 0.5 × σ_Planck
  = 3.35e-3
- `L_max`: 10 (canonical S62/S67 depth)
- `random_seed`: N/A
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<Δα_s_shared>, scheme=spectral-zeta, convention=k_pivot=0.05, L_max=10)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: |Δα_s_shared| < 0.5 × σ_Planck — S62 and S67 agree to
  within half a Planck sigma under shared pivot
- **FAIL**: |Δα_s_shared| > σ_Planck — cross-registry contradiction
  persists; canonical-row designation required
- **INFO**: 0.5 σ ≤ |Δα| ≤ σ — marginal agreement; emit convention-
  map and defer canonical designation to S86

**Substitution chain**:
```
Step 1: α_s^S62 := d²ln P_ζ/d(ln k)² at k = k_S62     (S62 convention)
Step 2: α_s^S67 := d²ln P_ζ/d(ln k)² at k = k_S67     (S67 convention; transit-MS)
Step 3: Shared pivot k_0 := 0.05 Mpc^-1                (Planck convention)
Step 4: α_s(k_0) = α_s(k_i) + β_s(k_i) · ln(k_0 / k_i) + O(β')   (2nd-order Taylor)
Step 5: Δα := α_s^S62(k_0) − α_s^S67(k_0)            (shared-pivot subtraction)
Step 6: Direction: if k_S62 = k_S67 and β_s(S62) = β_s(S67),
        then Δα = 0 exactly.                        (trivial limit check)
Step 7: Claim output: Δα is the measured discrepancy in the shared
        pivot; agreement is an equality, not a direction.
```

**What PASS/FAIL means**:
- **PASS** — S62 and S67 are reconciled; one row in the observational
  ledger, with both derivation pathways cited.
- **FAIL** — the two derivations genuinely disagree; framework must
  pre-register which α_s is the observation-facing value for CMB-S4
  / LiteBIRD / CMB-HD. Disagreement is a structural signal (different
  schemes probe different spectral moments of D_K).

**Effort**: 0.75 session-units (requires re-running spectral-zeta
at shared pivot from both scheme histories).

**Substrate framing**: α_s is the second log-derivative of the
scalar spectrum; in substrate language, it is the k-running of the
`a_2` spectral moment through the transit. S62 and S67 probe this
running through different regulator pathways (spectral-zeta vs
Mukhanov-Sasaki). Agreement at shared pivot is a substrate-level
consistency check: the same D_K yielding the same running independent
of regulator.

---

## §W1b-5. S85-W1b-BETA-S-JOINT-S4-HD

**Gate ID**: S85-W1b-BETA-S-JOINT-S4-HD

**Trigger**: [VERIFY]

**Classification**: META (detector-forecast joint-fit consistency)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The running-of-running β_s = −0.1331 (S85-BETA-S-
CMB-S4-PREREG, W0 bucket) is advertised with CMB-S4-only σ(β_s). The
W1b gate tests whether the **simultaneous** fit of {α_s, β_s}
against CMB-S4 + CMB-HD jointly produces a consistent β_s central
value and σ, OR reveals that α_s × β_s covariance breaks the
single-experiment forecast when CMB-HD enters. This is the
simultaneous-fit consistency audit: does adding CMB-HD as an
independent experiment tighten β_s, and does the tightening preserve
the framework's zero-free-parameter prediction?

**Method**:
```python
# s85_w1b_beta_s_joint_s4_hd.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
# 2-parameter Fisher {α_s, β_s} for CMB-S4 alone, then joint CMB-S4 × CMB-HD
# Assume diagonal detector correlation (orthogonal block); W1b-2 handles correlated case
# Fisher F_S4 = CMB-S4 sensitivity matrix (from pre-registered CMB-S4 CDR)
# Fisher F_HD = CMB-HD sensitivity matrix (from MacInnis 2022 Table 2)
# F_joint = F_S4 + F_HD (independent-detector approximation)
# Marginalize over α_s: σ(β_s)_marg = sqrt((F^{-1})[β,β])
# Check central: β_s_joint = β_s_canon (framework point)
```
- CPU, 2×2 matrices.
- Input SHAs: CMB-S4 CDR Table, MacInnis 2022 forecast Table 2,
  canonical_constants.py (β_s_canon = −0.1331).
- Output: `s85_w1b_beta_s_joint_s4_hd.{py,npz,png}`;
  PNG is joint-posterior ellipse in (α_s, β_s) plane, CMB-S4 alone
  vs joint.

**Machinery pin (PRDR)**:
- `parameters`: {α_s, β_s} (2-D); nuisance params marginalized out
  at detector level (pre-aggregated forecast)
- `detectors`: CMB-S4, CMB-HD (independent-block approximation)
- `scheme`: Gaussian-Fisher joint
- `convention`: β_s_canon from canonical_constants.py (zero-free-param
  framework point)
- `pivot_k`: 0.05 Mpc^-1 (shared)
- `tolerance`: ABSOLUTE — joint σ(β_s) tightens by factor √2 in
  the independent-experiment ideal case
- `random_seed`: N/A
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<σ(β_s)_joint>, scheme=Fisher-2D-joint, convention=indep-detectors, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: σ(β_s)_joint < σ(β_s)_S4 × 0.85 (joint tightens by ≥15%
  — CMB-HD adds genuine information on β_s) AND β_s_canon lies
  within 1σ of the joint posterior best-fit
- **FAIL**: joint σ tightens by <5% (CMB-HD adds no β_s info —
  simultaneous-fit claim is vacuous) OR β_s_canon is >2σ outside
  joint posterior (framework point excluded by the joint forecast)
- **INFO**: 5% ≤ tightening ≤ 15% (modest); publish full ellipse

**Substitution chain**:
```
Step 1: F_S4 := 2×2 Fisher, rows/cols = {α_s, β_s}          (CMB-S4 CDR)
Step 2: F_HD := 2×2 Fisher                                  (MacInnis 2022)
Step 3: Independent assumption: F_joint = F_S4 + F_HD       (linearity of Fisher info)
Step 4: σ²(β_s)_X := (F_X^{-1})[β, β]                     (marginalization)
Step 5: For orthogonal (F_S4 diag, F_HD diag, pooled):
        σ²(β_s)_joint = 1/(1/σ²_S4 + 1/σ²_HD)             (parallel-add limit)
Step 6: If σ_HD ≈ σ_S4, ratio = 1/√2 ≈ 0.707             (ideal tightening)
Step 7: Direction: joint σ ≤ σ_S4 always (info only adds). The
        magnitude depends on σ_HD / σ_S4 ratio AND on off-diagonal
        α × β covariance, which shifts the effective improvement.
Conclusion: σ(β_s)_joint is monotonically reducing in the number of
independent experiments; tightening fraction is the output.
```

**What PASS/FAIL means**:
- **PASS** — joint S4 × HD forecast meaningfully tightens β_s; the
  framework point stays inside the joint 1σ; advertised CMB-S4-only
  σ is a conservative lower bound.
- **FAIL** — either CMB-HD adds no β_s info (simultaneous-fit advocacy
  is wrong) or the framework β_s is excluded by the joint (more
  stringent pre-registration needed).

**Effort**: 0.5 session-units (pull MacInnis 2022 Table 2, pull CMB-S4
CDR Table, 2×2 Fisher algebra).

**Substrate framing**: β_s is the third log-derivative of the
scalar spectrum — the running of the running. Joint CMB-S4 × CMB-HD
probes different k-bands of this running; the joint constraint
tests whether a single D_K spectral triple can produce both
α_s(k_S4) AND β_s(k_HD) with zero free parameters.

---

## §W1b-6. S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT

**Gate ID**: S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT

**Trigger**: [VERIFY]

**Classification**: META (detector-forecast replacement)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The framework's CMB-HD α_s discrimination forecast
has been using an agent-projected σ(α_s)_CMB-HD estimate (interpolated
from CMB-S4 by detector-area + ℓ_max scaling). MacInnis et al. 2022
(arXiv:2203.05728 or similar CMB-HD SciBook forecast) reports an
explicit σ(α_s) figure from a full pipeline simulation. Replace the
projection with the published verified value, re-run W1a-9
MULTID-FISHER with the verified σ_HD, and report whether the
discrimination power on α_s shifts by ≥10%.

**Method**:
```python
# s85_w1b_cmb_hd_alpha_s_macinnis_explicit.py
# Extract σ(α_s)_CMB-HD from MacInnis 2022 Table (pre-registered line + SHA
# of downloaded PDF, or SHA of the specific table row transcribed into plan)
# Replace the projected value in the detector ensemble
# Re-run Fisher combination; report ratio σ_MULTID_verified / σ_MULTID_projected
```
- CPU. Dependency: MacInnis 2022 PDF or arXiv cache; if not
  available, agent declares PRE-REG-INCOMPLETE rather than falsifying.
- Input SHAs: MacInnis 2022 PDF, W1a-9 output JSON, canonical_constants.
- Output: `s85_w1b_cmb_hd_alpha_s_macinnis_explicit.{py,npz,png}`;
  PNG compares projected vs verified σ(α_s)_HD with ratio.

**Machinery pin (PRDR)**:
- `source`: MacInnis et al. 2022 (arXiv:2203.05728, CMB-HD SciBook
  Table for α_s forecast) — full citation pre-registered
- `extraction`: σ(α_s)_CMB-HD at fiducial Planck α_s = −0.0045,
  k_pivot = 0.05 Mpc^-1
- `scheme`: Gaussian-Fisher single-experiment
- `convention`: identical to W1a-9 (to make the ratio meaningful)
- `fallback`: if source unavailable, mark PRE-REG-INCOMPLETE
- `tolerance`: ABSOLUTE 10% shift threshold
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<σ_HD_verified>, scheme=Fisher-single-expt, convention=Planck-pivot, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: |σ_HD_verified − σ_HD_projected| / σ_HD_projected < 0.10
  (the projection was accurate to ≤10%; W1a-9 ensemble claim
  survives)
- **FAIL**: |ratio − 1| > 0.25 (projection was badly off;
  W1a-9 MULTID-FISHER ensemble σ(α_s) is restated)
- **INFO**: 10% ≤ |ratio − 1| ≤ 25% (moderate correction);
  publish both numbers and propagate to W1a-9 successor row
- **PRE-REG-INCOMPLETE**: MacInnis 2022 source not accessible in
  project cache (not a FAIL; treated per §Pre-Registration
  Completeness in epistemic-discipline.md)

**Substitution chain**:
```
Step 1: σ_HD_projected := W1a-9 interpolation from CMB-S4 scaling    (prior)
Step 2: σ_HD_verified  := MacInnis 2022 Table published value        (authoritative)
Step 3: Ratio R := σ_HD_verified / σ_HD_projected                    (comparison)
Step 4: If R < 1, projection was conservative (under-advertised sensitivity).
        If R > 1, projection was optimistic (over-advertised sensitivity).
Step 5: Direction is an OUTPUT, not a claim. The gate asks whether R
        falls in the [0.9, 1.1] tolerance band.
```

**What PASS/FAIL means**:
- **PASS** — the projection was faithful; pre-registered discrimination
  claims stand.
- **FAIL** — the pre-registered claim depended on an incorrect
  detector-forecast input; the framework's sensitivity advertisement
  is corrected and all downstream tests using σ_HD are flagged for
  re-run.

**Effort**: 0.5 session-units (literature pull, one-line substitution).

**Substrate framing**: CMB-HD's α_s sensitivity is set by its
angular-resolution reach into the small-scale damping tail — the
high-k tail of the emergent scalar spectrum, which probes the
spectral-zeta moment a_2 at short wavelengths (high D_K eigenvalues).
The projection vs verified test is a calibration check on how well
a substrate-level sensitivity estimate carries to a real detector
pipeline.

---

## §W1b-7. S85-W1b-LITEBIRD-ALPHA-S-HAZUMI-VERIFIED

**Gate ID**: S85-W1b-LITEBIRD-ALPHA-S-HAZUMI-VERIFIED

**Trigger**: [VERIFY]

**Classification**: META (detector-forecast replacement, twin of §W1b-6)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: Same as §W1b-6 but for LiteBIRD: replace the
agent-projected σ(α_s)_LiteBIRD in W1a-9 MULTID-FISHER with the
published Hazumi et al. 2022 JLTP LiteBIRD forecast (arXiv:2202.02773
or SPIE 2020). LiteBIRD is primarily a tensor-mode experiment with
limited α_s discrimination; the verified σ is expected to be large
(> σ_CMB-S4 × 5), meaning LiteBIRD contributes marginally to α_s
joint-σ. The test pre-registers this expectation.

**Method**:
```python
# s85_w1b_litebird_alpha_s_hazumi_verified.py
# Extract σ(α_s)_LiteBIRD from Hazumi et al. 2022 JLTP (or SPIE equivalent)
# Confirm σ_LiteBIRD / σ_CMB-S4 > 5 (LiteBIRD α_s discrimination is weak by design)
# Replace projected value in W1a-9; re-run joint Fisher
# Report ratio σ_MULTID_verified / σ_MULTID_projected
```
- Mechanics identical to §W1b-6.
- Input SHAs: Hazumi 2022 source PDF, W1a-9 output JSON,
  canonical_constants.py.

**Machinery pin (PRDR)**:
- `source`: Hazumi et al. 2022 JLTP (arXiv:2202.02773 or direct PTEP citation)
- `extraction`: σ(α_s)_LiteBIRD at k_pivot = 0.05 Mpc^-1
- `scheme`: Gaussian-Fisher single-experiment
- `convention`: same as W1a-9
- `fallback`: PRE-REG-INCOMPLETE if source not in project cache
- `tolerance`: ABSOLUTE — σ_LiteBIRD / σ_CMB-S4 > 5 expected; test
  whether this expectation is confirmed
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<σ_LB_verified>, scheme=Fisher-single-expt, convention=Planck-pivot, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: σ_LB_verified / σ_CMB-S4 > 5 AND |σ_LB_verified −
  σ_LB_projected| / σ_LB_projected < 0.25 (LiteBIRD contributes
  marginally to α_s as expected, and the projection was within 25%)
- **FAIL**: σ_LB_verified / σ_CMB-S4 < 3 (LiteBIRD adds meaningful
  α_s information, contradicting the design-motivated expectation
  — must restate the detector portfolio) OR projection error >50%
- **INFO**: within tolerance but projection error 25-50%
- **PRE-REG-INCOMPLETE**: source not accessible

**Substitution chain**:
```
Step 1: σ_LB_projected := W1a-9 projection                     (prior agent estimate)
Step 2: σ_LB_verified  := Hazumi 2022 published Table          (authoritative)
Step 3: Ratio-A: σ_LB_verified / σ_CMB-S4                      (relative contribution)
Step 4: Ratio-B: σ_LB_verified / σ_LB_projected                 (projection accuracy)
Step 5: Direction claim: LiteBIRD is B-mode-optimized; it does NOT
        match CMB-S4's angular resolution at small scales (high ℓ).
        α_s sensitivity scales with ℓ_max^-0.5 to -1 depending on noise
        model; LiteBIRD ℓ_max ≈ 1400, CMB-S4 ℓ_max ≈ 5000 ⇒ naive
        scaling predicts σ_LB/σ_S4 ≈ 3-6.                        (prediction)
Step 6: PASS band is σ_LB/σ_S4 > 5, which tests whether the
        projected value fell in the naive-scaling window.
```

**What PASS/FAIL means**:
- **PASS** — detector portfolio is correctly balanced; LiteBIRD is
  primary on r / n_T, marginal on α_s (as designed); W1a-9 ensemble
  claim survives.
- **FAIL** — either LiteBIRD unexpectedly contributes to α_s
  (portfolio strategy needs reweighting) or projection was >50% off.

**Effort**: 0.5 session-units.

**Substrate framing**: LiteBIRD's design target is the tensor-mode
B-polarization from primordial GW — the n_T spectral moment of D_K,
not the α_s running. This gate tests that the detector-portfolio
intuition (each detector probes one substrate moment) matches the
published pipeline forecast.

---

## §W1b-8. S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION

**Gate ID**: S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION

**Trigger**: [AUDIT]

**Classification**: META (canonical-constants recalibration on 2025-2026 data)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: The framework's canonical `n_s_canon` and
`alpha_s_canon` were pinned against Planck 2018 (the only
published full-mission analysis at the time). Planck PR4 (NPIPE,
2024-2025) and DESI DR2 / DR3 (2025-2026) provide updated central
values. This gate audits whether `canonical_constants.py` needs
a recalibration: does the 2025-2026 combined Planck PR4 + DESI DR2
α_s central value shift by > σ_Planck_2018 / 3 from the 2018 value?
If yes, the framework's "within 1σ of Planck" claim may need
restatement against the updated reference.

**Method**:
```python
# s85_w1b_planck_desi_2025_alpha_s_recalibration.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
# Pre-registered references (pinned at plan-write, 2026-04-21):
# - Planck 2018: α_s = −0.0045 ± 0.0067 (TT,TE,EE+lowE+lensing)
# - Planck PR4  : pre-registered central ± σ from NPIPE paper (2024-2025)
# - DESI DR2    : pre-registered central ± σ from Adame et al. 2025
# Combined via inverse-variance weighting
# Compute shift Δα_s = α_s_2025 − α_s_2018
# Report: does canonical_constants.py `alpha_s_canon` need an update_constant()?
```
- CPU trivial.
- Input SHAs: Planck PR4 NPIPE paper, DESI DR2 / early DR3 release
  (whichever is latest at 2026-04-21), canonical_constants.py.
- Output: `s85_w1b_planck_desi_2025_alpha_s_recalibration.{py,npz,png}`;
  PNG shows 2018, PR4, DR2, combined with framework point.

**Machinery pin (PRDR)**:
- `reference_set`: {Planck 2018, Planck PR4, DESI DR2}; frozen
  at plan-write
- `combination_scheme`: inverse-variance weighted mean
- `tolerance`: ABSOLUTE — update required iff |Δα_s| > σ_Planck_2018 / 3
  = 2.23e-3
- `convention`: k_pivot = 0.05 Mpc^-1 for all three
- `output_action`: if FAIL, emit an `update_constant("alpha_s_canon", ...)`
  call in the verdict line with session=S85, source=PR4+DR2-combination
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<Δα_s>, scheme=inv-var-weighted-combination, convention=Planck-pivot, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: |Δα_s| < σ_Planck_2018 / 3 — 2025-2026 data consistent
  with 2018; `alpha_s_canon` remains pinned
- **FAIL**: |Δα_s| > σ_Planck_2018 — significant shift; framework
  `alpha_s_canon` must be updated via `mcp__knowledge__update_constant`,
  and all prior BF claims recomputed against the new reference
- **INFO**: σ/3 ≤ |Δα_s| ≤ σ — moderate drift; update canonical
  `n_s_latest` and `alpha_s_latest` as companion entries (leave 2018
  canonical pinned with historical flag)

**Substitution chain**:
```
Step 1: α_2018 := −0.0045, σ_2018 := 0.0067                     (Planck TT,TE,EE+lowE+lensing)
Step 2: α_PR4, σ_PR4 := Planck NPIPE 2024-2025 (pinned in plan)
Step 3: α_DR2, σ_DR2 := DESI DR2 2025-2026 (pinned)
Step 4: Inverse-variance weights: w_i := 1/σ_i²
Step 5: α_combined := Σ(w_i α_i) / Σw_i                         (combination)
Step 6: Δα := α_combined − α_2018                               (shift)
Step 7: Direction: if the 2025 data cluster sits closer to the
        framework α_s_canon than the 2018 central, Δα drives toward
        framework-preferred values. If further, drives away. The
        magnitude relative to σ_2018/3 is the update threshold.
```

**What PASS/FAIL means**:
- **PASS** — the α_s landscape is stable against 2025-2026 data;
  canonical pins hold.
- **FAIL** — the framework must recalibrate its reference; the
  α_s-pre-registration-landing gates (W1b-3, W1b-5, W0-BETA-S-PREREG)
  inherit a propagation action.

**Effort**: 0.5 session-units (literature pull + weighted mean).

**Substrate framing**: The canonical α_s is the substrate's
prediction for the k-running of the scalar-curvature spectral moment.
Comparing to 2025-2026 sky data tests whether the detector-aggregate
measurement of this substrate quantity is stable across mission
generations; instability would indicate either foreground / pipeline
systematics at the per-cent level, or a genuine shift that the
substrate must reconcile.

---

## §W1b-9. S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM

**Gate ID**: S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM

**Trigger**: [VERIFY-THEOREM]

**Classification**: GEOMETRIC (structural theorem promotion; PRU
remediation)

**Agent type**: mack-cosmic-bridge (structural arithmetic only; no
D_K eigenvalue recomputation)

**Hypothesis**: S84 W2-19 reported r_max (the rank-universality
ceiling across corridor configurations) as a numerical pattern with
unpinned machinery — one of the two GENUINE-UNPINNED items in the
S84 closing audit. The hypothesis: the pattern is a layer-interface
theorem. If r_max equals min(r_N, r_{N+1}) for adjacent corridor
layers N, N+1 (where r_N is the intrinsic rank of layer N), then the
pattern is structural, not fit. The gate promotes W2-19 from
PRU-vulnerable to theorem-registered if and only if this identity
holds across all 8 corridor checkpoints.

**Method**:
```python
# s85_w1b_genuine_unpinned_r_max_theorem.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
# Load S84 W2-19 data: r_max(corridor_k) for k ∈ checkpoints
# Compute r_N, r_{N+1} for each checkpoint (intrinsic layer ranks,
# pre-computed in S84 W2 spectrum caches)
# Check: r_max(k) == min(r_N(k), r_{N+1}(k)) for all k
# Output: identity check table + residuals
```
- CPU trivial (structural arithmetic).
- Input SHAs: S84 W2-19 verdict line + data cache, S84 spectrum
  cache, canonical_constants.py.
- Output: `s85_w1b_genuine_unpinned_r_max_theorem.{py,npz,png}`;
  PNG is r_max vs min(r_N, r_{N+1}) scatter with identity line.

**Machinery pin (PRDR)**:
- `corridor_checkpoints`: 8 (as in S84 W2-19)
- `L_max`: 10 (S84 spectrum cache)
- `scheme`: intrinsic-layer-rank from SVD on layer-block sub-Dirac
- `convention`: Jensen-deformed SU(3); no perturbation beyond S84
- `tolerance`: THEOREM — exact equality to machine epsilon (1e-12
  absolute tolerance on r_max − min(r_N, r_{N+1}))
- `random_seed`: N/A
- `GPU path`: disabled (8 × small SVD; CPU is faster)

**Expected output 4-tuple**:
`(value=<max-residual>, scheme=intrinsic-rank-SVD, convention=Jensen-SU3, L_max=10)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: max over 8 checkpoints of |r_max(k) − min(r_N, r_{N+1})(k)|
  < 1e-12 — the layer-interface identity holds; W2-19 promoted to
  theorem
- **FAIL**: max residual > 0 for any checkpoint — identity does NOT
  hold; W2-19 remains PRU-vulnerable, and the alternative hypothesis
  (r_max is a deeper invariant) becomes the S86 carry-forward
- **INFO**: residual in (0, 1e-12) — numerical-precision-limited;
  need higher precision arithmetic

**Substitution chain**:
```
Step 1: r_max(k) := observed pattern from S84 W2-19           (data)
Step 2: r_N(k)   := intrinsic rank of layer N at checkpoint k (SVD)
Step 3: Hypothesis: r_max(k) = min(r_N(k), r_{N+1}(k)) ∀ k    (theorem candidate)
Step 4: Residual δ(k) := r_max(k) − min(r_N, r_{N+1})(k)      (diagnostic)
Step 5: If δ(k) = 0 ∀ k, the theorem holds exactly.
Step 6: Direction check: r_max is always ≤ min(r_N, r_{N+1})
        (rank on a joined space cannot exceed the smaller joinee's
        rank) — this is a weak inequality, known as the
        rank-subadditivity bound.                              (direction known)
Step 7: The gate tests whether the bound is SATURATED — a stronger
        structural statement than rank-subadditivity.
Conclusion: direction (≤) is established by rank inequality; gate
probes whether equality holds, which is the theorem promotion.
```

**What PASS/FAIL means**:
- **PASS** — W2-19 r_max is the layer-interface rank-saturation
  theorem; it is promoted from a PRU-vulnerable pattern to a
  GEOMETRIC structural wall in the permanent-results-registry.
- **FAIL** — the pattern is looser than saturation; the gate
  eliminates the theorem candidate, and the remaining hypothesis
  (that r_max is a genuinely new invariant, not reducible to
  intrinsic layer ranks) must be pursued.

**Effort**: 0.5 session-units (structural arithmetic; reuses S84
cache).

**Substrate framing**: The substrate fiber decomposes into corridor
layers indexed by N; each layer is a sub-eigenspace of D_K. The
rank r_N is how many eigenvalue families the layer carries. The
layer-interface theorem claims the JOINT rank is pinned by the
thinner of the two adjacent layers — a structural statement about
how the fiber pieces together at the layer boundary.

---

## §W1b-10. S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT

**Gate ID**: S85-W1b-CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT

**Trigger**: [VERIFY]

**Classification**: META (decoupled-joint evidence ledger; detector-
independence audit)

**Agent type**: mack-cosmic-bridge

**Hypothesis**: α_s and w_a are probed by different detector classes
(α_s by CMB-S4/HD/LiteBIRD; w_a by DESI-DR3/Euclid/LSST). The
framework's structural prediction yields both α_s_canon and w_a_canon
from the SAME spectral triple — so a joint test that ties the
two measurements together is an independence-check: if the detectors
are truly independent (as designed), the joint evidence is the
PRODUCT of individual Bayes factors. This gate books the joint test
explicitly: compute BF_joint vs BF_α_s × BF_w_a, pre-register the
permissible deviation due to shared priors / foreground overlap.

**Method**:
```python
# s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.py
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import numpy as np
# BF_alpha_s from W1b-3 (alpha_s_prior_range, narrow prior)
# BF_w_a from DR3 live-watch (S85-W0-DR3-REGULATOR-SUCCESSOR) at frozen w_a_canon
# Assumed-independent product: BF_indep = BF_alpha_s * BF_w_a
# Correlated joint: BF_joint = full-data joint marginal likelihood ratio
#     (requires correlation-aware MCMC; the gate pre-registers the data product)
# Deviation D := |log10(BF_joint) − log10(BF_indep)|
```
- CPU; simple multiplication + pre-registered joint lookup.
- Input SHAs: W1b-3 output JSON, W0-DR3-REGULATOR-SUCCESSOR output,
  canonical_constants.py.
- Output: `s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.{py,npz,png}`;
  PNG is BF_joint vs BF_indep with the 0.3 dex deviation band.

**Machinery pin (PRDR)**:
- `detectors_alpha_s`: {CMB-S4, CMB-HD, LiteBIRD}
- `detectors_w_a`: {DESI-DR3, Euclid, LSST}
- `cross_detector_correlation`: approximated as 0 (independent sky
  surveys) — the gate TESTS this assumption via the deviation
- `scheme`: Bayes-factor-joint vs Bayes-factor-independent-product
- `convention`: log10 Bayes factors
- `tolerance`: ABSOLUTE — independence holds iff |log10(BF_joint) −
  log10(BF_indep)| < 0.30 (≈ factor-2 deviation in BF)
- `random_seed`: N/A
- `GPU path`: disabled

**Expected output 4-tuple**:
`(value=<Δlog10BF>, scheme=joint-vs-independent-product, convention=log10, L_max=n/a)`

**PASS/FAIL/INFO thresholds**:
- **PASS**: |Δlog10BF| < 0.30 — detector independence holds to
  factor-2; joint α_s × w_a evidence is simply the product of
  single-channel BFs; the framework's two-spectral-moment prediction
  is evidentially multiplicative
- **FAIL**: |Δlog10BF| > 0.60 — the "independent detectors"
  assumption fails by more than factor-4; joint evidence cannot be
  derived from single-channel BFs and must be computed directly
- **INFO**: 0.30 ≤ |Δlog10BF| ≤ 0.60 — marginal; emit full joint
  MCMC pre-registration for S86

**Substitution chain**:
```
Step 1: BF_α := framework BF on α_s channel       (W1b-3)
Step 2: BF_w := framework BF on w_a channel       (DR3 tree + W0-DR3-SUCCESSOR)
Step 3: Independence hypothesis: p(D_α, D_w | model) =
        p(D_α | model) · p(D_w | model)           (statistical independence)
Step 4: BF_indep := BF_α · BF_w                   (direct product)
Step 5: BF_joint := p(D_α, D_w | FW) / p(D_α, D_w | LCDM)  (defn of joint BF)
Step 6: Under strict independence, BF_joint = BF_indep identically.
Step 7: Direction: BF_joint − BF_indep probes the off-diagonal
        correlation. Positive residual ⇒ detectors correlated in a
        framework-favoring direction; negative residual ⇒ detectors
        correlated in a framework-disfavoring direction.
        Deviation |Δlog10BF| is the OUTPUT.
Conclusion: The sign of the deviation is an output; its magnitude
against the 0.30 tolerance is the gate.
```

**What PASS/FAIL means**:
- **PASS** — the α_s × w_a joint evidence is the product of
  individually-advertised single-channel BFs; the framework's
  multi-moment prediction hardens without extra ingredients.
- **FAIL** — the independent-detector assumption is broken; the
  claimed BF_α × BF_w combined strength cannot be substantiated
  without a proper joint MCMC. The evidence ledger must restate
  combined strength as a UB / LB bound rather than a multiplicative
  claim.

**Effort**: 0.5 session-units (reads from W1b-3 and DR3 tree; one
multiplication + one deviation computation).

**Substrate framing**: α_s and w_a are distinct spectral moments
of the same D_K — α_s probes the scalar-spectrum running through
the `a_2` moment's k-derivative, w_a probes the impedance-mismatch
leakage through the `a_0` zeroth moment. Independence of the
detector channels means the substrate's D_K is being probed at
orthogonal spectral coordinates; joint BF that equals the
product is the evidential signature of that orthogonality.

---

## Wave W1b → Wave W2 Decision Point

After all 10 W1b gates append verdict lines, the wave emits a
consolidated row to `completion-queue.jsonl` with fields:
```
{"event": "wave_complete", "wave": "W1b", "session": "S85",
 "verdicts": {"S85-W1b-CF-M2-...": "PASS|FAIL|INFO|PRE-REG-INCOMPLETE", ...},
 "ts": "<computed-at-runtime>"}
```

Cross-wave decision rules:

1. If **§W1b-1 (CF-M2-DR3-REGULATOR-TREE)** FAILs, W2-1 (connes
   alpha-s-axiom-minimality-audit) inherits a new PRDR pin: the DR3
   tree is regulator-conditional, so the axiom-minimality audit
   must state whether its own verdict is regulator-layer-robust.

2. If **§W1b-2 (JOINT-FISHER-CORRELATED)** FAILs, W1a-9 MULTID-FISHER
   is flagged for restatement; this propagates as a carry-forward
   to S86 (not a within-S85 action).

3. If **§W1b-3 (ALPHA-S-PRIOR-RANGE-LCDM)** FAILs, the framework's
   BF claims in the permanent-results-registry inherit a prior-
   disclosure obligation: every BF row must now carry a (prior-
   type, prior-width) pin.

4. If **§W1b-4 (TRANSIT-PS-67-SIMULTANEOUS)** FAILs, the canonical
   α_s entry in `canonical_constants.py` must be designated "which
   scheme"; this blocks any S86 gate that consumes `alpha_s_canon`
   without specifying scheme.

5. If **§W1b-6 or §W1b-7 (MacInnis or Hazumi verified)** PRE-REG-
   INCOMPLETE (source inaccessible), the W1a-9 MULTID-FISHER ensemble
   claim is flagged PRE-REG-INCOMPLETE as well. Not a FAIL; the
   carry-forward is explicit.

6. If **§W1b-8 (PLANCK-DESI-2025)** FAILs (update required), all
   S85 gates that consumed `alpha_s_canon = −0.0045 ± 0.0067` inherit
   a propagation action; the orchestrator rewrites
   `canonical_constants.py` via `mcp__knowledge__update_constant` and
   all post-update S85 gates re-read; pre-update verdicts remain
   permanent per the gate-verdicts rule but are flagged with a
   historical annotation.

7. If **§W1b-9 (R_MAX THEOREM)** PASSes, the permanent-results-
   registry receives a new structural theorem row; if FAILs, the
   pattern is re-opened as a PRU-vulnerable S86 carry-forward.

8. If **§W1b-10 (α_s × w_a DECOUPLED-JOINT)** FAILs, the evidence
   ledger restates all compound BF claims (including the framework's
   headline "zero-free-parameter multi-observable match") as
   lower bounds only.

---

## Wave W1b Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md §Pre-Registration
Completeness`, every gate above enumerates its free parameters.
The aggregate W1b machinery-enumeration pin:

| Gate | Free Parameters | Pinned Values / Ranges | PRU-status |
|:-----|:----------------|:-----------------------|:-----------|
| W1b-1 | L_max, scheme, convention, tolerance | {8,10,12}, Zubarev, R_842, cell-IN | PINNED |
| W1b-2 | N_det, correlation_matrix, scheme, conv | 5, pre-registered JSON, Fisher-marg-Gauss, block-diag | PINNED |
| W1b-3 | priors (3-set), data_likelihood, scheme | pre-registered 3-set, Planck 2018, marg-L-ratio | PINNED |
| W1b-4 | pivot_k, scheme, L_max, tolerance | 0.05/Mpc, spectral-zeta, 10, 0.5σ | PINNED |
| W1b-5 | parameters, detectors, scheme, pivot_k | {α,β}, {S4,HD}, Fisher-2D, 0.05/Mpc | PINNED |
| W1b-6 | source, extraction, scheme, fallback | MacInnis 2022, σ(α_s), Fisher-single, PRU-INCOMPLETE | PINNED |
| W1b-7 | source, extraction, scheme, fallback | Hazumi 2022, σ(α_s), Fisher-single, PRU-INCOMPLETE | PINNED |
| W1b-8 | reference_set, combination, tolerance | {2018,PR4,DR2}, inv-var, σ/3 | PINNED |
| W1b-9 | checkpoints, L_max, scheme, tolerance | 8, 10, intrinsic-SVD, 1e-12 | PINNED |
| W1b-10 | det_α, det_w, corr, scheme, tolerance | {S4,HD,LB}, {DR3,Euc,LSST}, 0, BF-joint-vs-prod, 0.30 dex | PINNED |

**PRU cardinality audit result**: `D_PRU_raw = 0` for all 10 gates
at plan-write (pre-dispatch); sig_1 is expected to be 1 in the v3
ladder at session close. Plan-layer PRDR consistency is satisfied.

---

## Wave W1b Input-SHA Ledger

Static-file SHA-256 hashes (computed 2026-04-21 at plan freeze;
agents VERIFY against these on first read):

| File | Gate(s) | SHA-256 |
|:-----|:--------|:--------|
| `computations/canonical_constants.py` | ALL | `<computed-at-runtime>` |
| `computations/s84_w4_44_dr3_contingency_fine_grained.json` | W1b-1 | `801e4690...` (S84 W4-44 closure SHA; full 64 chars in manifest) |
| `sessions/session-plan/s85_w1b_alpha_s_correlation_matrix.json` (to be written by W1b-2 setup) | W1b-2 | `<computed-at-runtime>` |
| Planck 2018 α_s tuple (pinned in-plan) | W1b-3, W1b-8 | `inline; α=−0.0045, σ=0.0067` |
| `computations/s62_*_canonical_row.json` | W1b-4 | `<computed-at-runtime>` |
| `computations/s67_gge_bispectrum.npz` OR `s67_ps_alpha_s.npz` | W1b-4 | `<computed-at-runtime>` |
| CMB-S4 CDR (arXiv:1907.04473 Table-to-be-cited) | W1b-5 | `<computed-at-runtime; extract+SHA at gate-time>` |
| MacInnis et al. 2022 (arXiv:2203.05728) | W1b-5, W1b-6 | `<computed-at-runtime>` |
| Hazumi et al. 2022 JLTP (arXiv:2202.02773) | W1b-7 | `<computed-at-runtime>` |
| Planck PR4 NPIPE paper (Tristram et al. 2023 or update) | W1b-8 | `<computed-at-runtime>` |
| DESI DR2 Adame et al. 2025 | W1b-8 | `<computed-at-runtime>` |
| `computations/s84_w2_19_r_max_cache.npz` | W1b-9 | `<computed-at-runtime>` |
| `computations/s85_w1b_cf_m2_dr3_regulator_tree.npz` (W1b-1 output) | downstream only | N/A at plan-write |
| `computations/s85_w1b_alpha_s_prior_range_lcdm.npz` (W1b-3 output) | W1b-10 | N/A at plan-write |
| `computations/s85_w0_dr3_regulator_successor.npz` (W0 output) | W1b-10 | N/A at plan-write (cross-wave dependency) |

Agents executing these gates MUST compute and log the SHA-256 of
every read file in the first 20 lines of stdout, per the S81+
gate-verdict standard.

---

## Wave W1b Completion Declaration

Wave W1b is complete when ALL 10 of the following are on disk with
non-stub content:

1. `computations/s85_w1b_cf_m2_dr3_regulator_tree.py` + `.npz` + `.png`
2. `computations/s85_w1b_alpha_s_joint_fisher_correlated.py` + `.npz` + `.png`
3. `computations/s85_w1b_alpha_s_prior_range_lcdm.py` + `.npz` + `.png`
4. `computations/s85_w1b_alpha_s_transit_ps_67_simultaneous.py` + `.npz` + `.png`
5. `computations/s85_w1b_beta_s_joint_s4_hd.py` + `.npz` + `.png`
6. `computations/s85_w1b_cmb_hd_alpha_s_macinnis_explicit.py` + `.npz` + `.png`
7. `computations/s85_w1b_litebird_alpha_s_hazumi_verified.py` + `.npz` + `.png`
8. `computations/s85_w1b_planck_desi_2025_alpha_s_recalibration.py` + `.npz` + `.png`
9. `computations/s85_w1b_genuine_unpinned_r_max_theorem.py` + `.npz` + `.png`
10. `computations/s85_w1b_cf_m6_alpha_s_w_a_decoupled_joint.py` + `.npz` + `.png`

Plus 10 verdict lines appended to `computations/s85_gate_verdicts.txt`,
each with the canonical S81+ format:
```
S85-W1b-{SLUG}: PASS|FAIL|INFO|PRE-REG-INCOMPLETE -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>
```

Plus a §VII.W1b working-paper section in the S85 working paper with
one subsection per gate (10 subsections), each containing: hypothesis,
method summary, verdict, threshold, direction-read, downstream
propagation flag if applicable.

If any of the 10 gates terminates PRE-REG-INCOMPLETE due to external
source-access (MacInnis, Hazumi, Planck PR4, DESI DR2 unavailable in
cache), the wave closes as PARTIAL with explicit source-pull as the
S86 leading carry-forward item — this is NOT a W1b FAIL.

---

**End of Wave W1b plan. 10 gate blocks, structurally self-contained,
PRDR-pinned, SHA-ledger-declared, substrate-framed.**
