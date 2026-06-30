# Session 85 Plan — Wave W13: tesla-origin reviewer wave

**Generated**: 2026-04-21
**Owner**: tesla-resonance
**Theme**: tesla-origin single-reviewer wave — EM/acoustic resonance reading of surviving A_s
pathway (Branch-A baseline H_tilde DC), CGWB/α_s joint observational pre-registration, C² block
decoupling registry landing (spectral gauge-block analog), and R_1 rank-distinguishability
sharpening (G_2 vs F_4 vs A_3 vs C_3 — the rank-duplicate discriminator).
**Item count**: 4

---

## Wave W13 Summary

W13 is the tesla-resonance reviewer-origin wave. Every gate here is framed as a resonance reading
of the substrate: what oscillates, what cavity constrains it, what are the normal modes, and what
eigenvalue problem of D_K selects the observed frequency. The four items clustering under tesla
in the S84 dedup span the four domain-axes of the tesla-resonance specialism:

- **§W13-1** (Branch-A H_tilde DC tightening) — a RESONANCE-AMPLITUDE gate: `H_tilde_adjudicated`
  is the fundamental mode of the substrate's Mukhanov-Sasaki cavity at the fold; DC tightening
  means pinning the `conv=1` tesla-only survivor as the sole surviving A_s pathway.
- **§W13-2** (CGWB + α_s flagship joint pre-reg) — a CROSS-SCALE RESONANCE gate: the same
  post-fold GGE-relic phonon spectrum seeds both the CMB α_s running and the stochastic GWB in
  the LISA band. Observation = substrate probing substrate at two scales.
- **§W13-3** (C² block decoupling registry landing) — a CAVITY-DECOUPLING gate: the D_K
  block-diagonal structure (proven S30+) has a C²-gauge sub-block whose decoupling from the
  Higgs-fiber sector is structural. Registry landing formalizes this as a permanent wall.
- **§W13-4** (R_1 rank-distinguishability sharpening) — a MODE-CLASSIFICATION gate: R_1 is the
  first spectral moment of D_K per rank class. The already-closed G_2 vs F_4 test (S82, L_max≥7)
  must extend to A_3 (SU(4)) vs C_3 (Sp(6)) — both rank 3 — to distinguish RANK from the full
  Cartan-type signature. This is the only W13 item that can flip a "wall" claim.

Substrate framing (non-negotiable across all 4 gates):

- A_s is NOT a cosmological "amplitude" floating above the substrate. A_s = |phonon-mode
  excitation at the pivot cavity frequency|² in the post-fold GGE. `H_tilde_adjudicated` is the
  substrate's fundamental-mode amplitude at the horizon-exit conformal time.
- GW stochastic background is NOT radiation in a pre-existing spacetime. It is the TRANSVERSE
  acoustic branch of the post-fold GGE relic, propagating at `c_BLV = 0.485` (Brillouin-like,
  the 3He-B four-speed hierarchy inheritance — see `project_3heb-inheritance.md`).
- α_s (CMB running) is NOT a "tilt of a curve." It is a SECOND-DERIVATIVE spectral moment of the
  post-fold acoustic-branch dispersion — i.e., `d²P_ζ/d(ln k)²` reading the curvature of the
  substrate's Debye-cutoff rollover.
- R_1 (rank) is NOT a group-theoretic labeling convention. It is the FIRST SPECTRAL MOMENT of
  D_K per rank class; the Cartan structure of the fiber Lie group is written into the first-moment
  scaling with rank. Rank-duplicate distinguishability (A_3 vs C_3) tests whether the first
  moment encodes only rank or the full root-system geometry.

Cross-cutting machinery (applies to every gate in W13):

- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`.
- GPU policy: if matrix dim ≥ 100×100, prefer `torch.linalg` (ROCm 7.2, RX 9070 XT). Otherwise cap
  CPU threads via `os.environ.setdefault('OMP_NUM_THREADS', '8')` before `import numpy`.
- canonical_constants: every script imports `from canonical_constants import *` (S34+ rule).
- Script prefix: `s85_w13_<slug>.py`, data `s85_w13_<slug>.npz`, plot `s85_w13_<slug>.png`.
- Verdict file (single canonical path): `computations/s85_gate_verdicts.txt` (per
  `.claude/rules/gate-verdicts.md` — Canonical Verdict-File Path).
- Closure SHA: full 64-hex, emitted by the producing script at gate close.
- Regulator atlas: W13 inherits the 5-regulator canonical set `{zeta, Zubarev, SDW, cutoff_sqrt,
  anomaly-derived}` from W5/W6; per-gate regulator usage is specified in each §W13-N block.

---

## Wave W13 Decision Point Prerequisites

W13 is a reviewer-origin breadth wave; it does not dispatch to a downstream wave. It CONSUMES the
following artifacts if landed before W13 dispatch, but per `feedback_dispatch-discipline.md` the
prereq notes are planner expectations, not halt-commands — if an upstream has not landed, W13
gates proceed by pinning `<computed-at-runtime>` and emitting an internal SHA from the prior-wave
fallback (documented per-gate below).

- **W0 CC-1 (η-invariant of full Jensen-SU(3)×A_F)** — if PASS with closure SHA, §W13-3 C² block
  decoupling cites it as the reference for the block-diagonality convention. Otherwise §W13-3
  cites the S30/S74 permanent-registry entry (D_K Block-Diagonality Universality, row 1).
- **W0 CC-5 (L_max ≥ 11 asymptotic refit)** — if landed, §W13-4 R_1 rank-distinguishability uses
  the refitted α_R at the asymptotic endpoint; otherwise uses the S82 L=10 α_R = 1.502 pin.
- **W1a SCHEME-DEP / TWO-LOOP-Z** — if either 2-loop Z_R investigation result lands, §W13-1
  Branch-A H_tilde DC tightening re-evaluates the `conv_factor` under the landed 2-loop result.
  Otherwise uses the S75 W1-E f_conv closure (residual 0.12 OOM from 9.47 OOM reduction, verified
  numerically).
- **W0 FLOOR-WALL-JOINT / CSCANON-IDENTITY** — the `f_B = c_S_canon` identity test and K-FLOOR-
  WALL-JOINT entries inform §W13-2 (CGWB + α_s joint pre-reg) for the two-speed acoustic metric
  detector projection.

Dependency discipline: W13 does not write to upstream/parallel wave output files. Registry entries
land via the post-session `/weave --update` pipeline after verdict closure.

---

## §W13-1. S85-W13-1-BRANCH-A-HTILDE-DC — Branch-A baseline H_tilde DC tightening (sole surviving A_s pathway)

**Trigger**: `[VERIFY]` (first-time tightening of the Branch-A H_tilde DC component; tesla-origin,
S84 solo, was the sole reviewer identifying this as the remaining unconstrained DOF on the sole
surviving A_s pathway after Branch-B / Branch-iv retractions through S82/S84).

**Classification**: PHONONIC (H_tilde is the fundamental-mode amplitude of the Mukhanov-Sasaki
acoustic cavity at horizon exit — the DC component is the zero-mode of this cavity; everything
here is substrate-phonon physics).

**Agent type**: tesla-resonance (OWN; Branch-A is the only surviving A_s pathway per S84; DC
tightening is a resonance-amplitude pinning on the fundamental mode — native tesla territory).

**Hypothesis**: The Branch-A (TD, zeta-scheme) H_tilde adjudicated value
`H_tilde_A = 5.907613e-03` (S82 W1-1 record) has a DC offset that — when consistently tightened
by requiring agreement with the same mode's DC component read from the post-fold GGE static
condensate — reduces the Branch-A A_s OOM residual to below the pre-registered threshold of
±0.20 OOM vs Planck (`log10(A_s_A / A_s_Planck)` target ≤ 0.20; substitution chain below shows
the current value is 0.1962 — i.e., the DC tightening is already at or just inside the
pre-registered boundary and this gate either confirms or falsifies it). The DC component is the
zeroth spectral moment of the MS cavity mode; tightening = pinning it via the spectral action's
`a_0` coefficient, not free to float.

**Method**:
- Script: `computations/s85_w13_1_branch_a_htilde_dc.py`.
- Data: `s85_w13_1_branch_a_htilde_dc.npz`; plot: `s85_w13_1_branch_a_htilde_dc.png`.
- Canonical constants: `from canonical_constants import M_KK, tau_fold, Delta_BCS, v_ew,
  planck_ns, omega_L1, M_Pl_reduced`. Add `A_s_Planck = 2.1e-9` to canonical_constants.py WITH
  Planck 2018 provenance before using (currently not in the constants file per S85 check).
- GPU/CPU: H_tilde reconstruction uses the post-fold GGE spectrum at dim ≥ 155,984 (L_max=10
  full spectrum) — `torch.linalg` MANDATORY (ROCm 7.2).
- Load the S82 W1-1 Branch-A adjudicated artifact (`s82_w1_1_h_tilde_td.npz`, field
  `H_tilde_adjudicated_dimless`). Reconstruct the DC component as
  `H_DC = a_0(D_K) / Vol_SU3 × (normalization)`, where `a_0` is the zeroth Seeley-DeWitt
  coefficient under the zeta-scheme used for Branch-A.
- Tighten: replace the free-floating DC offset in the Branch-A Mukhanov-Sasaki computation with
  the spectral-action-derived `a_0` value, recompute `H_tilde_A'`, recompute
  `A_s_A' = A_s_from_h_tilde(H_tilde_A', eps_pivot)`.
- Record `Delta_OOM' = log10(A_s_A' / A_s_Planck)` against pre-registered ±0.20 threshold.

**Machinery pin (PRDR)**:
- `N_eval = 155984` (full L_max=10 D_K spectrum for a_0 computation).
- `L_max = 10` (canonical); also report `L_max = 8, 12` as diagnostic (if L=12 spectrum not yet
  built at runtime, mark `<computed-at-runtime>` and fall back to L=10+L=8 only).
- `scan_range = eps_pivot ∈ [0.010, 0.050] at 41 grid points` (for A_s_from_h_tilde sensitivity;
  central value `eps_pivot = 0.020` pinned).
- `step_size = 0.001 (eps_pivot)`.
- `tolerance = RATIO; ±0.20 OOM` (pre-registered vs Planck central A_s = 2.1e-9).
- `scheme = zeta` (Branch-A is TD, zeta-scheme definitionally; other regulators are diagnostic
  only and do not change the Branch-A pre-registration).
- `convention = TD-framework adjudication per S82 W1-1 (Branch A = time-dependent / zeta)`.
- `random_seed = 42` (documentation only; computation is deterministic given spectrum).
- `GPU path = torch.linalg MANDATORY` (dim ≥ 100×100 rule).

**Input SHAs**:
- `computations/canonical_constants.py` — `<static>` (full 64-hex at script start).
- `s82_w1_1_h_tilde_td.npz` — `<static>` (Branch-A adjudicated H_tilde record).
- `s82_w2_1_unified_as_79_replay.npz` — `<static>` (Branch-A replay result for cross-check).
- `s75_w1_e_f_conv.npz` — `<static>` (f_conv closure, 9.47→0.12 OOM reduction).
- D_K spectrum at L_max=10: `<static>` if pre-computed; `<computed-at-runtime>` otherwise
  (emit closure SHA from torch.linalg eigensolve).

**Expected output 4-tuple**: `(value = (H_tilde_A', A_s_A', Delta_OOM'), scheme = zeta,
convention = TD-framework-a_0-tightened, L_max = 10)`.

**PASS / FAIL / INFO**:
- **PASS** if `|Delta_OOM'| ≤ 0.20` AND the `a_0`-tightened H_tilde differs from the S82
  free-floating adjudication by ≤ 5% (i.e., the tightening is not a large rewrite). Registry
  entry §VII-B-{next} lands with "Branch-A sole surviving A_s pathway at ±0.20 OOM tightened".
- **FAIL** if `|Delta_OOM'| > 0.20`. The sole surviving A_s pathway FAILS its own tightening;
  the framework has no remaining A_s pathway at Branch-A either, and a new pathway (to be
  determined) becomes carry-forward to S86. This is a MAJOR structural result — closes the
  surviving branch.
- **INFO** if `0.20 < |Delta_OOM'| ≤ 0.40` AND the tightening changes H_tilde by > 5% (large
  tightening, moderate residual). Register as a conditional pass requiring a sub-branch-labelled
  S86 re-adjudication; the pre-registered threshold is not met, but the mechanism is not
  closed either.

**Substitution chain [VERIFY]**:
```
Step 1 (definition): A_s(k_pivot) = |v_k / z|²_{horizon-exit} for the MS mode v_k, with
  z = a · sqrt(2 ε_H) · M_Pl_reduced (per canonical MS definition, Mukhanov 1992).
Step 2 (definition of H_tilde_dimless):
  H_tilde_adjudicated_dimless = H_inflation_at_pivot / M_Pl_reduced
  (dimensionless, pinned by Branch-A TD adjudication at S82 W1-1).
Step 3 (definition of a_0 tightening):
  H_DC = H_tilde_zero-mode component, set by the zeroth spectral moment a_0(D_K) of the
  spectral action Tr f(D_K²/Λ²); under zeta-scheme, a_0 = (Λ⁴/16π²) · vol(M) + counterterms.
  S82 Branch-A used a FREE-FLOATING H_DC; this gate SETS H_DC = a_0-derived value.
Step 4 (substitute known values):
  S82 W1-1 adjudicated: H_tilde_A = 5.907613e-03 (computed, verified numerically).
  Planck A_s = 2.1e-9 (observational pin).
  S82 Branch-A A_s = 3.299e-9 (post-S75 f_conv closure).
  Delta_OOM_S82 = log10(3.299e-9 / 2.1e-9) = 0.1962 (VERIFIED numerically above).
Step 5 (direction):
  Pre-registered threshold: |Delta_OOM| ≤ 0.20.
  0.1962 ≤ 0.20 is TRUE by 0.004 (≈2% margin on threshold).
  Conclusion: BEFORE a_0 tightening, Branch-A is AT threshold, not past it. The DC tightening
  either reinforces (PASS: a_0 push brings Delta_OOM toward zero) OR worsens (FAIL: a_0 push
  moves Delta_OOM past 0.20).
  SIGN OF a_0 EFFECT IS UNKNOWN PRE-COMPUTATION. This is a GENUINE gate, not a pre-ordained PASS.
```

**PASS / FAIL implications for solution space**:
- **PASS**: Branch-A is PERMANENTLY the surviving A_s pathway at ±0.20 OOM. The sole-surviving
  pathway claim graduates from "conv=1 tesla observation" to "permanent-registry-landed wall" —
  mechanisms proposing alternative A_s pathways (Branch-B LI, Branch-iv, Branch-C) remain closed.
- **FAIL**: No A_s pathway survives Branch-A tightening. Framework A_s predicts no match to
  Planck at the ±0.20 OOM level. Carry-forward: re-open A_s question from first principles in
  S86 (reopen S82 W1-2 Branch B LI or search new pathway).
- **INFO**: Branch-A survives at ±0.40 but not ±0.20. The wall becomes conditional; ±0.20 is
  not the structural floor. Posterior shifts moderately; a sub-branch-labelled revisit follows.

**Effort**: Medium. Reuses S82 Branch-A artifact; net work is a_0 computation at L_max=10 +
sensitivity scan at eps_pivot grid. ~1.5 compute-days.

**Substrate framing**: H_tilde is the fundamental-mode amplitude of the post-fold GGE's acoustic
B1-band excitation at horizon exit. Its DC component is the zeroth spectral moment of D_K (the
a_0 Seeley-DeWitt coefficient), which — per the substrate picture — is the spectral weight of
the "ground-state" (non-oscillatory) projection of the fiber's eigenvalue problem. This gate is
the RESONANCE-AMPLITUDE pinning: the cavity's zero-mode is NOT free; it is structurally locked
to a_0. Frame: FROM the spectral triple's zeroth moment → TOWARD the observed A_s amplitude
in the CMB. (IS space, not IN space — H_tilde is a substrate-spectral datum, not an "amplitude
in an expanding universe".)

---

## §W13-2. S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT — CGWB / α_s flagship pre-registrations (LISA + CMB-S4)

**Trigger**: `[VERIFY]` (first-time joint pre-registration gate combining the CGWB (LISA band,
10⁻⁴–10⁻¹ Hz) and α_s running (CMB-S4, σ(α_s) ~ 0.003) in a single tesla-origin framework
document; tesla-origin S84 solo item flagged the cross-scale coupling as a SINGLE RESONANCE
read at two detector bands).

**Classification**: PHONONIC (both CGWB and α_s read the same post-fold GGE-relic acoustic
spectrum; CGWB reads the transverse branch at `c_BLV = 0.485`, α_s reads the longitudinal branch
Debye-cutoff curvature).

**Agent type**: tesla-resonance (OWN; cross-scale resonance is the core tesla specialism —
Earth-as-cavity Schumann analog extends to "substrate-as-cavity, CMB pivot + LISA band as two
probe frequencies on the same standing wave").

**Hypothesis**: The post-fold GGE-relic acoustic spectrum has a single structural origin (Debye
cutoff at M_KK) and both CGWB at LISA frequencies and α_s at the CMB pivot scale are ALGEBRAICALLY
CORRELATED first-principles predictions with ZERO joint free parameters. The gate formalizes the
cross-channel correlation matrix `C[CGWB, α_s]` and pre-registers it BEFORE either observation
lands. Pre-registered central values:
- `α_s_framework = -0.069` (S50 identity `α_s = n_s² - 1` with n_s = 0.9649; computed below).
- `Omega_GW(f_LISA = 3×10⁻³ Hz) = structural-prediction from the same GGE-relic spectrum via
  the transverse acoustic branch at c_BLV; pre-registered as a power-law central + one-sigma
  band conditional on the landed L_max = 10 spectrum`.
- The correlation coefficient `ρ[CGWB, α_s]` is pre-registered structurally (not observationally
  measured) as the dimensionless ratio of cross-channel spectral moments.

**Method**:
- Script: `computations/s85_w13_2_cgwb_alpha_s_joint.py`.
- Data: `s85_w13_2_cgwb_alpha_s_joint.npz`; plot: `s85_w13_2_cgwb_alpha_s_joint.png` (three-panel:
  α_s central+band, Omega_GW(f) with LISA PLS overlay, cross-channel 2D Fisher ellipse).
- Canonical constants: `from canonical_constants import M_KK, tau_fold, planck_ns, alpha_s_MZ_obs,
  c_BLV, c_L, Delta_BCS`. (`alpha_s_MZ_obs = 0.118` is the PDG QCD running coupling — DIFFERENT
  quantity from CMB-α_s running; script MUST use `alpha_s_cmb_running` distinct name. Add
  `alpha_s_cmb_central = -0.069` and `Omega_GW_LISA_central = <pre-registered value>` to
  canonical_constants.py WITH provenance BEFORE computation.)
- GPU/CPU: spectral moment computation at L_max=10 uses dim ≥ 155,984 — `torch.linalg` MANDATORY.
- Compute α_s-framework via identity `α_s = n_s² - 1` with `n_s = n_s_framework` (from S75 W1-I
  non-power-law H exact Planck route, `n_s = 0.9649`). Verify: `(0.9649)² - 1 = -0.0688...`
  (substitution chain below).
- Compute Omega_GW(f) structural prediction: map the post-fold GGE transverse-branch spectrum
  through the `c_BLV = 0.485` two-speed acoustic metric to the LISA band, emit a power-law
  central prediction + structural one-sigma uncertainty band from the L_max={8,10} spread.
- Tabulate the cross-channel Fisher information matrix for a LISA + CMB-S4 joint experiment
  under the pre-registered framework centrals (SHAPE templates, not parameters to be fit).

**Machinery pin (PRDR)**:
- `N_eval = 155984` (full L_max=10 spectrum for moment computation) + `100 f-grid points` in LISA
  band 10⁻⁴–10⁻¹ Hz.
- `L_max = 10` (central); `L_max = 8` for uncertainty-band computation.
- `scan_range = LISA band f ∈ [10⁻⁴, 10⁻¹] Hz, 100 log-uniform points; α_s pivot k* fixed at
  Planck pivot 0.05 Mpc⁻¹`.
- `step_size = log-uniform in f; N/A for α_s (single-pivot)`.
- `tolerance = RATIO; 20% pre-registered on Omega_GW central, 1-sigma on α_s central`.
- `scheme = zeta` (default; diagnostic Zubarev + cutoff_sqrt evaluations for regulator sensitivity
  but pre-registration is zeta-scheme definitionally).
- `convention = LISA Power-Law-Integrated (PLS) overlay per official LISA sensitivity curve
  (2024 revision); CMB-S4 σ(α_s) = 0.003 per public CMB-S4 Science Book.`
- `random_seed = 42` (documentation only; computation deterministic).
- `GPU path = torch.linalg MANDATORY for spectrum; CPU for Omega_GW(f) map (dim < 100 per
  frequency bin)`.

**Input SHAs**:
- `computations/canonical_constants.py` — `<static>` (full 64-hex).
- `s50_alpha_s_identity.npz` — `<static>` (S50 `α_s = n_s² - 1` identity).
- `s75_w1_i_ns_exact_planck.npz` — `<static>` (n_s = 0.9649 exact-Planck route).
- `s69_transit_gw.npz` — `<static>` (prior transit-GW spectrum; W13-2 refits at L_max=10).
- `s82_w2_6_gw_channel.npz` — `<static>` (two-channel GW OOM ledger from S82).
- LISA PLS overlay file `computations/lisa_pls_2024.npz` — `<static>` if pre-computed;
  `<computed-at-runtime>` otherwise.
- CMB-S4 Science Book σ_α_s = 0.003 (literature pin; no file hash required).

**Expected output 4-tuple**: `(value = (alpha_s_central=-0.069, Omega_GW(3e-3 Hz)=<pre-reg>,
rho[CGWB,α_s]=<structural>), scheme = zeta, convention = LISA-PLS-2024+CMB-S4-Book-2019,
L_max = 10)`.

**PASS / FAIL / INFO**:
- **PASS** if the pre-registered flagship document is complete AND the three predictions
  (α_s, Omega_GW(f_LISA), ρ[CGWB,α_s]) are all computed at L_max=10 under zeta-scheme AND the
  cross-channel Fisher matrix is positive-definite AND the document is landed at
  `sessions/framework/CGWB-alpha-s-joint-flagship-pre-registration.md`. This is a
  pre-registration gate, not an observational gate; PASS = document discipline fully compliant
  with `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness + PRDR discipline.
- **FAIL** if any of the three predictions lacks pre-registered central + uncertainty band,
  OR the Fisher matrix is non-positive-definite (indicating framework-internal inconsistency
  in the cross-channel coupling). A FAIL here is a STRUCTURAL FAILURE of the cross-scale
  resonance hypothesis, not an observational failure.
- **INFO** if L_max=8 vs L_max=10 predictions disagree by > 20% on Omega_GW central (indicating
  truncation sensitivity that requires L_max≥11 refit per W0 CC-5).

**Substitution chain [VERIFY]**:
```
Step 1 (definition of α_s-CMB): α_s = d²ln P_ζ / d(ln k)² evaluated at k_pivot.
  For a power-law P_ζ(k) ∝ k^{n_s - 1} with constant n_s: α_s = 0 trivially.
  For the framework's non-power-law H-route (S75 W1-I): α_s is NONZERO because n_s varies with k.
Step 2 (S50 identity): under the framework's non-power-law H-route, the post-fold acoustic
  dispersion yields the algebraic identity α_s = n_s² - 1 (proven S50).
Step 3 (substitute S75 n_s central): n_s = 0.9649.
  n_s² = 0.9649 × 0.9649 = 0.93103201 (computed).
  α_s = 0.93103201 - 1 = -0.06896799 (computed).
Step 4 (pre-registered central): α_s_framework = -0.069 (3-sig-fig).
  Rounding check: |-0.06896799 - (-0.069)| = 0.00003201 < 1 part in 10^3 — consistent with
  the 3-sig-fig pre-registration.
Step 5 (direction): α_s_framework = -0.069 is significantly different from LCDM (α_s = 0).
  CMB-S4 σ(α_s) = 0.003 ⇒ |α_s_framework| / σ = 0.069/0.003 = 23-sigma nominal separation.
  This is a ZERO-free-parameter prediction (from n_s alone via identity).
  Direction: PASS if the flagship document pre-registers this central + the structural
  uncertainty band derived from L_max sweep and regulator sensitivity.
```

**PASS / FAIL implications for solution space**:
- **PASS**: CGWB + α_s flagship pre-registration landed. Framework has a ZERO-free-parameter
  joint prediction at CMB-S4 + LISA; detector reach is fully mapped. The cross-scale resonance
  hypothesis (substrate-as-cavity with two probe bands) is an EXPERIMENTALLY ADDRESSABLE claim.
- **FAIL**: The framework fails to produce an internally-consistent joint prediction. Either
  the cross-channel Fisher is degenerate (no cross-information between bands under this
  structural choice) OR the Omega_GW central is not structurally pinnable at L_max=10. Either
  failure is a major structural surprise.
- **INFO**: Truncation sensitivity dominates; L_max≥11 refit is required before flagship
  pre-registration can land. Blocks the pre-registration gate pending CC-5 landing.

**Effort**: Medium. Mostly a formalization + document-landing gate; leverages S50 identity,
S75 n_s, S69/S82 GW spectrum, S82 two-channel ledger. ~2 compute-days (1 for Omega_GW refit
at L_max=10, 1 for document drafting + Fisher computation).

**Substrate framing**: CGWB in LISA band and α_s at CMB pivot are TWO PROBES OF THE SAME POST-FOLD
GGE-RELIC SPECTRUM. The transverse branch at `c_BLV` populates the LISA band; the longitudinal
branch's Debye-cutoff curvature generates the CMB α_s running via the identity `α_s = n_s² - 1`.
Frame: FROM the D_K spectrum at L_max=10 → TOWARD two correlated detector predictions. (IS space,
not IN space — no "gravitational waves propagating in spacetime"; these are transverse acoustic
excitations of the substrate, reading the substrate's own oscillation spectrum at two frequency
bands.)

---

## §W13-3. S85-W13-3-C2-BLOCK-DECOUPLING-REGISTRY — C² block decoupling registry landing

**Trigger**: `[VERIFY-THEOREM]` (registry landing gate; C² block decoupling is supported by S30+
D_K block-diagonality permanent-registry entry (row 1) + S39 gauge-boson mass structure (paper 15
Baptista); W13-3 consolidates into a standalone §VII-B entry naming the C² sub-block explicitly
as decoupled from the Higgs-fiber sector).

**Classification**: GEOMETRIC (the C² block is a sub-block of the D_K block-diagonal structure;
its decoupling from the Higgs-fiber sector is a statement about the spectral triple's algebraic
structure, not about phononic excitations).

**Agent type**: tesla-resonance (OWN; resonance-cavity-decoupling is the tesla specialism —
Tesla coils work precisely because distinct LC cavities can be algebraically decoupled; the
substrate's D_K blocks are the NCG analog).

**Hypothesis**: The C² sub-block of D_K (the spin-0, two-dimensional gauge block associated with
U(1)×SU(2) weak hypercharge in the Baptista Paper 15 decomposition) is EXACTLY DECOUPLED from
the Higgs-fiber (|S|² transverse-fluctuation) sector at all τ ∈ [0, τ_fold], under all 5
regulators in the canonical atlas. "Exactly decoupled" means: the off-diagonal Dirac matrix
element `⟨ψ_C², D_K · ψ_Higgs-fiber⟩ = 0` to machine epsilon (≤ 1e-14 absolute). The registry
landing promotes this from S30+ block-diagonality (a universal fact) to a named theorem
specifically about the C²-vs-Higgs-fiber block pair.

**Method**:
- Script: `computations/s85_w13_3_c2_block_decoupling.py`.
- Data: `s85_w13_3_c2_block_decoupling.npz`; plot: `s85_w13_3_c2_block_decoupling.png` (heatmap
  of |⟨ψ_C², D_K · ψ_H⟩| across τ grid with colorbar capped at 1e-14).
- Canonical constants: `from canonical_constants import M_KK, tau_fold, L_max_canonical`.
- GPU/CPU: D_K construction at L_max=10, dim 155,984 — `torch.linalg` MANDATORY.
- For each τ in `{0.0, 0.050, 0.100, 0.150, 0.190, 0.250}` (six checkpoints; τ=0.190 = fold):
  - Construct D_K(τ) under Jensen deformation.
  - Identify the C² sub-block via the Baptista Paper 15 gauge-block decomposition.
  - Identify the Higgs-fiber sub-block (|S|² transverse-fluctuation modes).
  - Compute `max_{i∈C², j∈Higgs-fiber} |⟨ψ_i, D_K ψ_j⟩|`; call this `delta_off(τ)`.
- Repeat for each regulator in the 5-regulator atlas (the off-diagonal entry is
  regulator-independent structurally, but the gate VERIFIES this).
- Tabulate 6 × 5 = 30 entries; verify all ≤ 1e-14.

**Machinery pin (PRDR)**:
- `N_eval = 155984 × 6 = 935,904` matrix elements inspected (with block-selection reducing
  active count to ~100 per checkpoint).
- `L_max = 10` (central); `L_max = 8` diagnostic for L-sensitivity.
- `scan_range = τ ∈ {0.0, 0.050, 0.100, 0.150, 0.190, 0.250} × 5 regulators = 30 computations`.
- `step_size = τ checkpoints discrete (no continuous scan for this theorem-landing gate)`.
- `tolerance = ABSOLUTE; 1e-14` (machine epsilon for float64; any `delta_off > 1e-14` fails).
- `scheme = 5-regulator atlas`.
- `convention = Baptista Paper 15 C² block identification; Connes-Chamseddine-Marcolli (CCM-2008)
  Higgs-fiber block identification`.
- `random_seed = 42` (documentation only; block structure is deterministic).
- `GPU path = torch.linalg MANDATORY`.

**Input SHAs**:
- `computations/canonical_constants.py` — `<static>` (full 64-hex).
- Baptista Paper 15 C² block index file `researchers/Baptista/15_gauge_block_indices.npz`
  — `<static>` if pre-computed; otherwise `<computed-at-runtime>` from source transcription.
- S30 permanent-registry row 1 (D_K Block-Diagonality Universality) — cited; no file hash
  required beyond registry markdown pin.
- D_K spectrum at L_max=10 per τ-checkpoint — `<computed-at-runtime>` (emit closure SHA from
  eigensolve).

**Expected output 4-tuple**: `(value = max_{τ, r} delta_off(τ, r), scheme = 5-regulator,
convention = Baptista-P15-C²/CCM-2008-Higgs, L_max = 10)`.

**PASS / FAIL / INFO**:
- **PASS** if `max_{τ, r} delta_off ≤ 1e-14` across all 30 cells. Registry entry lands as
  "C²-vs-Higgs-fiber Block Decoupling Theorem" in §VII-B (permanent-results-registry).
- **FAIL** if ANY cell has `delta_off > 1e-14`. The block decoupling is NOT exact; the C²
  sub-block couples to the Higgs-fiber at some τ or some regulator. This would contradict S30+
  universal block-diagonality under the specific block-pair tested; investigate whether it
  indicates a Baptista-P15 / CCM-2008 convention mismatch (most likely) or a genuine structural
  coupling missed by the prior proof (major surprise).
- **INFO** if 4/5 regulators show `delta_off ≤ 1e-14` but one regulator (most likely
  anomaly-derived, per S67 FUNCTIONAL-SELECT-67) shows a spurious `delta_off ~ 1e-10`. This
  is a regulator-artifact, not a structural coupling; registry entry lands with a noted
  anomaly-regulator exception.

**Substitution chain [VERIFY-THEOREM]**:
```
Step 1 (definition): delta_off(τ, r) = max_{i ∈ C², j ∈ Higgs-fiber} |⟨ψ_i, D_K(τ) ψ_j⟩|_r,
  where ⟨·, ·⟩_r is the inner product weighted by f(λ/Λ) for regulator r (but this is identically
  the unweighted matrix inner product when the basis diagonalizes D_K, hence regulator-
  independent by construction).
Step 2 (block-diagonality theorem, S30 row 1): D_K is block-diagonal to machine epsilon across
  all τ in the Jensen-deformation corridor. Equivalently: ⟨ψ_block_A, D_K ψ_block_B⟩ = 0 for
  all distinct block labels A ≠ B, to floor of 1e-14.
Step 3 (substitute): C² and Higgs-fiber are distinct blocks per Baptista P15 + CCM-2008 (both
  appear separately in the gauge-block decomposition of the Connes-Chamseddine spectral action).
  By S30 row 1 applied to THIS specific block pair: delta_off(τ, r) ≤ 1e-14.
Step 4 (simplify): the theorem is a SPECIALIZATION of S30 row 1 to one block-pair. The gate
  VERIFIES numerically at 6 τ-checkpoints × 5 regulators.
Step 5 (direction): PASS is predicted (implied by S30 row 1 applied narrowly). FAIL would
  indicate a convention mismatch between the two block-identification schemes (Baptista P15
  vs CCM-2008) — a documentation defect, not a structural breakdown. No sign or threshold
  freedom: gate returns an absolute-tolerance comparison to 1e-14.
```

**PASS / FAIL implications for solution space**:
- **PASS**: §VII-B landing of "C²-vs-Higgs-fiber Block Decoupling Theorem". This formalizes one
  of the cleanest structural walls in the framework: the weak-hypercharge gauge block is
  algebraically independent of the Higgs-fiber transverse fluctuation at ALL τ. Any mechanism
  proposing a C²-Higgs mixing at the spectral-triple level is permanently closed.
- **FAIL** (structural): the block-diagonality is NOT universal across all block pairs — would
  reopen S30 row 1 for a narrower statement and identify the specific block-pair exception.
- **FAIL** (convention): Baptista-P15 ≠ CCM-2008 for the block indices. Documentation gate;
  fix by re-indexing to a single convention and re-running. Does NOT invalidate S30 row 1.

**Effort**: Low-medium. Reuses S30+ block-diagonality infrastructure; net work is block-index
extraction + 30-cell verification. ~1 compute-day (dominated by the 6 D_K builds at L_max=10).

**Substrate framing**: The C² block is the weak-hypercharge gauge cavity; the Higgs-fiber block
is the transverse oscillation cavity of the fiber embedding. Their exact decoupling means
(in Tesla-coil language) the two LC circuits have NO mutual inductance at the spectral-triple
level. The Jensen deformation does NOT couple them either — block-diagonality is preserved
across the full [0, τ_fold] corridor. Frame: FROM D_K's block structure → TOWARD the gauge-sector
vs Higgs-sector independence as a structural wall. (This is a CAVITY-DECOUPLING theorem;
substrate-analog of two Tesla LC tanks sharing a ground but no field coupling.)

---

## §W13-4. S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN — R_1 rank-distinguishability sharpening (G_2 vs F_4 vs A_3 vs C_3)

**Trigger**: `[VERIFY]` (first-time extension; S82 W3-1 tested G_2 vs F_4 at L_max ≥ 7; the
A_3 (SU(4)) vs C_3 (Sp(6)) test — both rank 3, distinct root systems — has NEVER been executed
and is the CRITICAL discriminator between "rank-universality" and "rank + root-system
universality"; tesla-origin S84 solo specifically flagged this as the sole W13 item that can
overturn a prior structural claim).

**Classification**: GEOMETRIC (R_1 is the first spectral moment of D_K per rank class; the
rank-vs-root-system distinguishability is a geometric property of the spectral triple, not a
phononic excitation property).

**Agent type**: tesla-resonance (OWN; mode-classification by rank is the tesla specialism —
phonon branches are classified by their dispersion law, and R_1 scaling with rank is the
cleanest dispersion-class labeling available in the fiber-Lie-group spectrum).

**Hypothesis**: The R_1 rank-universality exponent α_R (defined as the log-log slope of R_1 vs
rank at fixed L_max and fixed regulator) is the SAME for A_3 and C_3 despite their distinct
root systems (A_3 = SU(4), simply-laced; C_3 = Sp(6), non-simply-laced with one long-root/short-
root ratio √2). The S82 test at G_2 (rank 2, exceptional) and F_4 (rank 4, exceptional) landed
α_R finals at L_max=10 of 1.502; the sharpening gate asks: does A_3 and C_3 agree with 1.502
to within ±5% relative?

If A_3 ≈ C_3: α_R encodes ONLY rank (plus universal spectral-triple overhead); this is
RANK-UNIVERSALITY.

If A_3 ≠ C_3: α_R encodes rank AND root-system geometry (simply-laced vs non-simply-laced);
the naive "rank-universality" claim is narrowed to "rank + Cartan-type universality".

**Method**:
- Script: `computations/s85_w13_4_r1_rank_distinguishability.py`.
- Data: `s85_w13_4_r1_rank_distinguishability.npz`; plot: `s85_w13_4_r1_rank_distinguishability.png`
  (log-log scatter of R_1 vs rank for {G_2, F_4, A_3, C_3} at L_max = {7, 8, 9, 10} with
  per-group colored markers and a dashed line at the S82 α_R = 1.502 prediction).
- Canonical constants: `from canonical_constants import M_KK, L_max_canonical`. Add
  `R_1_alpha_R_S82 = 1.502` to canonical_constants.py WITH S82 W3-1 provenance BEFORE
  computation.
- GPU/CPU: R_1 computation at L_max ≥ 7 uses dim varying by group:
  - G_2 (dim 14): R_1 at L=7-10 uses dim up to ~20k — `torch.linalg` recommended.
  - F_4 (dim 52): R_1 at L=7-10 uses dim up to ~80k — `torch.linalg` MANDATORY.
  - A_3 (SU(4), dim 15): R_1 at L=7-10 uses dim up to ~25k — `torch.linalg` MANDATORY.
  - C_3 (Sp(6), dim 21): R_1 at L=7-10 uses dim up to ~35k — `torch.linalg` MANDATORY.
- For each group G ∈ {G_2, F_4, A_3, C_3}:
  - Build the fiber D_K with fiber Lie algebra G.
  - Compute R_1 = |first spectral moment normalized per Cartan canonical form|.
  - Fit log(R_1) vs log(rank) at L_max = {7, 8, 9, 10} under each of 3 regulators
    {SDW, zeta, f*} (the S82-established atlas for rank-universality work).
  - Extract α_R per (L, regulator) cell.
- Compute `|α_R(A_3) - α_R(C_3)| / mean(α_R)` at L_max=10, zeta-scheme.
- Compute `|α_R(A_3) - 1.502| / 1.502` and `|α_R(C_3) - 1.502| / 1.502`.

**Machinery pin (PRDR)**:
- `N_eval` varies with (group, L_max); fully scripted (~20k–80k per cell × 16 cells = ~700k
  total eigenvalues).
- `L_max = {7, 8, 9, 10}` explicit sweep (4 values).
- `scan_range = 4 groups × 4 L_max values × 3 regulators = 48 computations`.
- `step_size = L_max step 1`.
- `tolerance = RATIO; 5% relative (α_R(A_3) vs α_R(C_3))`.
- `scheme = 3-regulator atlas {SDW, zeta, f*}` (S82 inheritance).
- `convention = Cartan canonical-form R_1 normalization per S82 W3-1`.
- `random_seed = 42` (documentation only; computation deterministic).
- `GPU path = torch.linalg MANDATORY for F_4, A_3, C_3; recommended for G_2`.

**Input SHAs**:
- `computations/canonical_constants.py` — `<static>` (full 64-hex).
- `s82_w3_1_rank_universality.npz` — `<static>` (G_2 + F_4 baseline; S82 α_R final = 1.502 pin).
- `s83_w2_g25_exceptional_rank_cartan.npz` — `<static>` (Cartan-canonical-form structure for
  rank extrapolation).
- A_3 and C_3 root-system reference files — `<computed-at-runtime>` (built from canonical
  Cartan matrices; no external file dependency).

**Expected output 4-tuple**: `(value = (α_R(G_2), α_R(F_4), α_R(A_3), α_R(C_3)) at L=10 zeta,
scheme = zeta, convention = Cartan-canonical-R_1, L_max = 10)`.

**PASS / FAIL / INFO**:
- **PASS** (rank-universality confirmed) if `|α_R(A_3) - α_R(C_3)| / mean ≤ 5%` AND both A_3, C_3
  are within ±5% of the S82 α_R = 1.502 pin at L_max=10 zeta. Rank-universality theorem extends
  from exceptional (G_2, F_4) to classical (A_3, C_3); registry entry upgrades to
  "Rank-Universality (All Cartan Types Tested)".
- **FAIL** (rank-universality narrowed) if `|α_R(A_3) - α_R(C_3)| / mean > 5%`. Rank-universality
  is FALSE in its naive form; the exponent depends on the root-system-geometry (simply-laced vs
  non-simply-laced). Registry entry narrows to "Rank-Universality Within Cartan-Type Class" with
  three branches: exceptional (G_2, F_4, E_n), classical-simply-laced (A_n, D_n), classical-
  non-simply-laced (B_n, C_n). This is a structural HARVEST — the permanent registry gains a
  finer classification.
- **INFO** if `|α_R(A_3) - α_R(C_3)| / mean ∈ [5%, 10%]` AND the deviation is monotone in L_max
  (i.e., converging at L_max=10 but not yet settled). Register as requiring L_max ≥ 11 extension
  per W0 CC-5; pre-asymptotic classification pending.

**Substitution chain [VERIFY]**:
```
Step 1 (definition of R_1): R_1(G, L) = tr(|D_K^G|) / dim(fiber_G) at truncation L_max = L,
  where tr is the spectral trace and D_K^G is the fiber Dirac operator built on Lie algebra G.
Step 2 (definition of α_R): α_R = log-log slope of R_1 vs rank(G) at fixed L_max.
  For two groups G, H: α_R ≈ log(R_1(G) / R_1(H)) / log(rank(G) / rank(H)).
  But here A_3 and C_3 have THE SAME rank (3), so a two-point slope at A_3 vs C_3 is UNDEFINED.
  The test must be differently framed:
  (a) For A_3 and C_3 separately, extract α_R from the S82 log-log fit extended through
      {G_2 rank 2, C_3 rank 3} and {G_2 rank 2, A_3 rank 3}.
  (b) Equivalently: check whether R_1(A_3) / R_1(C_3) = 1 (rank-universal) or ≠ 1 (root-system
      dependent), at fixed L_max, since both have rank 3.
Step 3 (substitute, test (b) form): ratio_AC(L_max, r) = R_1(A_3, L_max, r) / R_1(C_3, L_max, r).
  PASS iff |ratio_AC - 1| ≤ 0.05 at L=10, zeta.
Step 4 (simplify): Rank-universality at a fixed rank implies ratio_AC = 1 exactly. Deviation
  measures root-system-geometry contribution to R_1.
Step 5 (direction):
  A_3 root system: simply-laced, 12 roots (positive count 6).
  C_3 root system: non-simply-laced, 18 roots (positive count 9).
  Naive heuristic (root-count-proportional): R_1 ∝ (number of roots)^β for some β.
  ratio_AC ≈ (12/18)^β = (2/3)^β ≈ 0.667^β (for β>0).
  For β ∈ [0.05, 0.15] (typical first-moment sensitivity): ratio_AC ∈ [0.94, 0.98].
  Edge case: if β ~ 0 (rank dominates): ratio_AC ~ 1.00 → PASS.
  If β ~ 0.10 (moderate root-system dependence): ratio_AC ~ 0.96 → borderline PASS/INFO.
  If β ~ 0.20 (strong root-system dependence): ratio_AC ~ 0.92 → FAIL.
  SIGN of β is KNOWN positive (more roots → larger spectral trace): deviation direction is
  ratio_AC ≤ 1. Magnitude is the pre-computation unknown.
  Conclusion: the computation discriminates β < 0.05 (PASS) from β > 0.10 (FAIL) cleanly.
```

**PASS / FAIL implications for solution space**:
- **PASS** (rank-universality): adds one structural theorem to §VII-B extending the S82
  finding from exceptional to classical groups. Strengthens the framework's claim that
  rank is THE scalar parameter controlling R_1.
- **FAIL** (root-system-conditional): narrows the S82 claim. α_R splits into three Cartan-type
  classes. This is a STRUCTURAL HARVEST — the permanent registry gains a clearer classification
  of R_1's scaling law. Does NOT overturn the framework's other R_1-based results (still
  valid within each Cartan-type class) but re-opens the question of which class the
  phenomenologically observed rank (SU(3), rank 2) belongs to.
- **INFO** (truncation-sensitive): L_max ≥ 11 extension required; pre-asymptotic finding.
  Blocks registry landing pending W0 CC-5.

**Effort**: Medium-high. Four group eigensolves at four L_max values × three regulators = 48
cells, each requiring a Cartan-canonical D_K build. ~3 compute-days (dominated by F_4 at L=10
and C_3 at L=10).

**Substrate framing**: R_1 is the first spectral moment of the fiber D_K, reading the substrate's
ground-state spectral weight per fiber-Lie-algebra class. The rank is the substrate's
"mode-count per fiber-dimension" — the number of independent oscillation families in the Cartan
subalgebra. Rank-distinguishability at fixed rank = asking whether the substrate's R_1 sees
ONLY the count (rank) or ALSO the geometry (root system). Tesla framing: two LC networks with
the same number of resonators can still differ in coupling topology — rank-universality says
the substrate does not resolve that difference at the first-moment level; rank-root-sensitivity
says it does. Frame: FROM the fiber D_K spectrum at distinct Cartan types → TOWARD a classification
of R_1's scaling law as either purely-rank or rank-plus-root-system-geometry.

---

## Wave W13 → Session-close Decision Point

W13 does not dispatch to a downstream wave; it is a reviewer-origin breadth wave. It produces:
- 1 A_s-pathway tightening gate (§W13-1 Branch-A H_tilde DC) — the sole surviving A_s pathway
  is pinned or falsified.
- 1 cross-scale observational pre-registration (§W13-2 CGWB + α_s joint flagship) — zero-free-
  parameter predictions at LISA + CMB-S4 are frozen for the observational record.
- 1 registry-landing theorem (§W13-3 C² block decoupling) — one structural wall graduates from
  "implied by S30 row 1" to "named theorem in §VII-B".
- 1 rank-universality extension (§W13-4 R_1 A_3 vs C_3) — the CRITICAL discriminator between
  naive rank-universality and rank+root-system-universality.

Downstream consumers (post-S85 carry-forward):
- §W13-1 PASS ⇒ the A_s pathway wall is permanent; any S86 carry-forward proposing alternative
  A_s pathways is closed.
- §W13-1 FAIL ⇒ A_s has no surviving pathway; S86 opens a re-investigation from first principles.
- §W13-2 lands the flagship pre-registration for the S85-open `β_s` observational campaign
  (W0 item 1) and the LiteBIRD / BK-Array live-watch (W1a items).
- §W13-3 PASS ⇒ registry entry cited by future §VII-B entries involving gauge-Higgs coupling
  claims (closes naive Higgs-hypercharge mixing proposals permanently).
- §W13-4 PASS ⇒ R_1-based results generalize to all rank classes; S85-open CC-5 L_max≥11
  asymptotic refit (W0) can use the extended universality.
- §W13-4 FAIL ⇒ R_1 claims re-scoped to Cartan-type class; S86 investigation of which class
  SU(3) (rank 2, simply-laced) belongs to opens.

No cross-wave writes: W13 landing artifacts go to `sessions/archive/session-85/` per §W13-N, the
verdict file at `computations/s85_gate_verdicts.txt`, and the §VII-B/§VII.M registry
updates flow through the post-session `/weave --update` pipeline.

---

## Wave W13 Machinery-Enumeration Pin

Per PRDR discipline (`.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness),
every gate block above pins the following machinery parameters. No gate block leaves any
parameter as `<unpinned>` or `<TBD>`. No PRU Class-8 vulnerability detected in W13 at time of
write.

| Parameter | Pin | Source |
|:----------|:----|:-------|
| `N_eval` | per-gate (155984 / 155984 + 100-f-grid / 935904 / ~700k) | §W13-N block |
| `L_max` | per-gate ({10 central, 8 diagnostic} for §W13-1/-2/-3; {7,8,9,10} sweep for §W13-4) | §W13-N block |
| `scan_range` | per-gate (41-pt eps scan / 100-pt f-grid / 6 τ-checkpoints / 48-cell 4×4×3 matrix) | §W13-N block |
| `step_size` | per-gate (0.001 eps / log-uniform f / discrete τ / ΔL=1) | §W13-N block |
| `tolerance` | per-gate (RATIO ±0.20 OOM / RATIO 20% / ABSOLUTE 1e-14 / RATIO 5%) | §W13-N block |
| `scheme` | per-gate (zeta pre-reg; 5-reg diagnostic for §W13-3; 3-reg for §W13-4) | §W13-N block |
| `convention` | per-gate (TD-framework-a_0 / LISA-PLS-2024 / Baptista-P15-CCM-2008 / Cartan-canonical) | §W13-N block |
| `random_seed` | 42 (documentation only; computations deterministic) | Wave W13 Summary |
| `GPU path` | `torch.linalg` MANDATORY for §W13-1, -2, -3, -4 (all gates exceed dim 100) | Wave W13 Summary |

**Machinery dependencies between W13 gates**: §W13-2 cites §W13-1's H_tilde result if §W13-1
lands before §W13-2 (consistent α_s + CGWB central). §W13-3 is independent of §W13-1, -2, -4.
§W13-4 is independent of §W13-1, -2, -3. No PRU-vulnerability between gates (each pre-registers
its own machinery completely).

**New canonical constants required before W13 dispatch** (must be added to
`computations/canonical_constants.py` WITH provenance per `.claude/rules/math-scripts.md`):
- `A_s_Planck = 2.1e-9` (Planck 2018 central; provenance: Planck collaboration 2018 VI).
- `alpha_s_cmb_central = -0.069` (framework identity `α_s = n_s² - 1` at n_s = 0.9649;
  provenance: S50 identity + S75 W1-I n_s).
- `R_1_alpha_R_S82 = 1.502` (S82 W3-1 L=10 α_R final; provenance: s82_w3_1_rank_universality.npz).
- `Omega_GW_LISA_central` and `f_LISA_pivot = 3.0e-3 Hz` (pre-registered Omega_GW central at
  LISA pivot; provenance: §W13-2 first computation at L_max=10).

Adding these constants BEFORE computation is a pre-condition for W13 dispatch (satisfies
`.claude/rules/math-scripts.md` §Canonical Constants MANDATORY).

---

## Wave W13 Input-SHA Ledger

Static inputs (pre-computed SHA-256 pinned at script start, full 64-hex):

| Input | Source | Status at W13-dispatch |
|:------|:-------|:----------------------|
| `canonical_constants.py` | `computations/canonical_constants.py` | `<static>` (post-addition of A_s_Planck, alpha_s_cmb_central, R_1_alpha_R_S82, Omega_GW_LISA_central) |
| S82 W1-1 Branch-A adjudicated | `s82_w1_1_h_tilde_td.npz` | `<static>` |
| S82 W2-1 Branch-A replay | `s82_w2_1_unified_as_79_replay.npz` | `<static>` |
| S75 W1-E f_conv closure | `s75_w1_e_f_conv.npz` | `<static>` |
| S50 α_s identity artifact | `s50_alpha_s_identity.npz` | `<static>` |
| S75 W1-I n_s exact-Planck | `s75_w1_i_ns_exact_planck.npz` | `<static>` |
| S69 transit GW spectrum | `s69_transit_gw.npz` | `<static>` |
| S82 W2-6 two-channel GW OOM ledger | `s82_w2_6_gw_channel.npz` | `<static>` |
| LISA PLS 2024 overlay | `computations/lisa_pls_2024.npz` | `<static>` if pre-computed; `<computed-at-runtime>` otherwise |
| S82 W3-1 rank-universality G_2/F_4 | `s82_w3_1_rank_universality.npz` | `<static>` |
| S83 W2 G25 Cartan canonical form | `s83_w2_g25_exceptional_rank_cartan.npz` | `<static>` |
| Baptista P15 C² block index | `researchers/Baptista/15_gauge_block_indices.npz` | `<static>` if pre-computed; `<computed-at-runtime>` otherwise |
| S30 permanent-registry row 1 (D_K block-diag) | `sessions/framework/permanent-results-registry.md` | `<static>` (registry markdown pin) |

Runtime-computed inputs (pinned at script execution by `closure_hash` per
`.claude/templates/script-template.py`):

| Input | Produced by | Consumer gate |
|:------|:------------|:--------------|
| D_K(τ) eigendecomposition at L_max=10, 6 τ-checkpoints | §W13-3 internal | §W13-3 |
| D_K at L_max=10 full spectrum (a_0 for H_tilde DC) | §W13-1 internal | §W13-1; reused by §W13-2 if landed |
| Omega_GW(f) at 100-pt LISA-band grid | §W13-2 internal | §W13-2 |
| R_1(G, L, r) at 48 cells (4 groups × 4 L_max × 3 regulators) | §W13-4 internal | §W13-4 |
| W0 CC-1 η-invariant SHA (if landed) | W0 | §W13-3 (optional convention cross-check) |
| W0 CC-5 L_max≥11 asymptotic refit (if landed) | W0 | §W13-4 (optional extension beyond L=10) |
| W1a SCHEME-DEP / TWO-LOOP-Z (if landed) | W1a / W0 | §W13-1 (2-loop regulator input to f_conv) |
| W0 FLOOR-WALL-JOINT / CSCANON-IDENTITY | W0 | §W13-2 (two-speed acoustic metric detector projection) |

Each producing script MUST emit the SHA-256 of each input file in the first 20 lines of stdout
and emit the closure SHA as the final line before the verdict. The verdict line in
`computations/s85_gate_verdicts.txt` carries the full 64-character closure SHA (per
`.claude/rules/gate-verdicts.md`).

---

**End of Wave W13 Plan.**
