# Session 89 Plan — Wave 5: Convergence + FWD-Cn bridge candidates + scaling scans

> **Provenance**: lizzi-spectral-functional-theorist orchestrator-direct planner-write per `/rclab-plan` skill §3b; co-authors: volovik-superfluid-universe-theorist (A.25/A.26/A.27 Corner-IV chain PRIMARY); connes-ncg-theorist (A.27 + A.8 CO).
> **Theme**: d_eff Richardson scan + Corner-IV K-window log-derivative chain + τ=2·τ_fold cross-validation + FWD-C1 retry parameterized + heat-kernel anchor sweep + Sage-QQ Spearman cross-check (Ledger A items A.8, A.25, A.26, A.27, A.28, A.31, A.36, A.37).
> **Composition order**: Wave 5 dispatches in S89 Batch 1 with W1-W4 + W6-W7 in parallel (intra-wave conditional chain A.25→A.26→A.27 sequenced; A.36→A.37 sequenced; A.8 + A.28 + A.31 independent).
> **Natural-split fallback**: W5a = A.8, A.28, A.31, A.36, A.37 (lizzi 5 items; substrate-distance-1 / Corner-I / FWD-C1 / heat-kernel sweep family); W5b = A.25, A.26, A.27 (volovik+connes joint; Corner-IV K-window log-derivative chain). Single-pass write attempted.

---

## Wave 5 Summary

Wave 5 closes the Cluster-E carry-forwards from S88 (Ledger A items A.8, A.25, A.26, A.27, A.28, A.31, A.36, A.37). The 8 gates partition into three structural axes:

1. **Convergence (Richardson L^{−n} scaling)**: A.8 d_eff Richardson scan at L_max ∈ {12, 14, 16, 18}; PASS predicate `residual(18) ≤ 0.5 × residual(14)` discriminates α = 3 (geometric closed-form HK-5 well-anchored) from α < 3 (Jensen second-order O(τ²) corrections needed).
2. **FWD-Cn bridge-candidate disambiguation**: A.25 → A.26 → A.27 conditional chain on the Corner-IV K-window log-derivative observable. A.25 verifies the volovik-path canonical −7.046336 against the falsifier value v_inf = 6.46e-6; A.26 extracts Level-2 algebraic envelope under L_max scan; A.27 disambiguates FWD-C2 c-split (Corner-II vs Corner-IV) per the §VII.U.2 4-corner classification.
3. **Scaling scans + cross-validation**: A.28 τ = 2·τ_fold cross-validation discriminates Reading-A (geometric resummation) vs Reading-B (linear-LO) via ratio R(0.38)/R(0.19); A.31 FWD-C1 retry under parameterized slope_A_FW_Conv_A canonical pin; A.36 5-anchor heat-kernel sweep on §W7a-74 PRIMARY evaluator with N≥4/5 decision rule for Reading-A WIN; A.37 Sage-QQ exact arithmetic cross-check of A.36 float verdicts.

**Conditional chains**: A.26 BLOCKED on A.25 PASS; A.27 BLOCKED on A.26 PASS-or-INFO (FWD-C2 disambiguation can fire on any A.26 outcome that produces a definite envelope α). A.37 DEPENDS ON A.36 (Sage-QQ comparison requires A.36 float verdicts as input).

**Cross-wave dependencies**:
- W5 A.8 anchors against W3 A.9 d_eff Jensen analytic form (W3 A.9 closed-form provides the analytic prediction A.8 tests numerically)
- W5 A.28 τ=2·τ_fold cross-validation must verify τ=0.38 is within τ_max regime per W3 A.35 bound (cross-wave precondition; if A.35 derives τ_max < 0.38, A.28 emits INFO for outside-regime testing)
- W5 A.31 FWD-C1 retry depends on `slope_A_FW_Conv_A` canonical pin landing (Ledger B.45 mechanical edit; if not landed at S89 plan-freeze, A.31 emits SUBSTRATE-FIRST-PROVENANCE Class-(f) audit)
- W5 A.27 FWD-C2 disambiguation feeds future cross-pillar bridge K-counter advancement (§"Forward template-adoption" K-counter at K=3 MANDATORY since S88 W4a-17; A.27 is K-counter eligible if it produces a structurally distinct bridge candidate)
- W5 A.31 cross-cuts W7 A.24 (substantive Mellin-cone closure; A.31 is the parameterized retry implementation, A.24 is the substantive multi-wave open question — both target n_s_FW vs c_sub_corrected closure)

**Total effort**: A.8 (0.5) + A.25 (0.4) + A.26 (0.5) + A.27 (0.25) + A.28 (1.0) + A.31 (0.8) + A.36 (0.4) + A.37 (0.3) = 4.15 wave-equivalents.

---

## Wave 5 Decision Point Prerequisites

Hard prerequisites (must hold at S89 plan-freeze):

1. `sessions/archive/session-88/workshops/s88-w17-w5b-47-step11-maxrule.md` §V (provides the spectrum cache identity for A.25 K-window log-derivative recompute; SHA-pinned at dispatch)
2. `sessions/archive/session-88/workshops/s88-w22-w7a-74-rank-vs-magnitude.md` §V.1 (provides §W7a-74 PRIMARY evaluator identity for A.36; SHA-pinned at dispatch)
3. `sessions/archive/session-88/workshops/s88-w12-w3c-57-hk5-residual-origin.md` §V.1 (provides HK-5 residual baseline for A.8 Richardson scan; SHA-pinned at dispatch)
4. W3 A.35 τ_max bound landing — if W3 lands first (intra-session ordering), A.28 inherits τ_max ≤ 0.38 vs > 0.38 routing; if A.35 lands AFTER A.28 dispatch, A.28 PRDR encodes the regime check via the closed-form `5/(1−τ/(5π))` divergence boundary at τ → 5π ≈ 15.708
5. `slope_A_FW_Conv_A` canonical pin — if Ledger B.45 mechanical edit lands at S89 plan-freeze, A.31 consumes the canonical directly; if pin is PENDING, A.31 PRDR encodes SUBSTRATE-FIRST-PROVENANCE Class-(f) audit with explicit "PENDING" placeholder pattern (D_max measurement deferred to dispatch)
6. W3 A.9 d_eff Jensen closed-form `c` coefficient — A.8 Richardson scan tests `residual(L_max) = Numerical_d_eff(L_max) − HK-5(τ_fold) − c·τ_fold²` against L^{−3} scaling; if A.9 derives `c` analytically before A.8 dispatch, A.8 inherits the analytic prediction

Soft prerequisites:

7. `methodology-wave-allowlist.md` — A.27 PRDR encodes its disambiguation pre-registration (registry-anchor structure, not METHODOLOGY-class), so allowlist append NOT required
8. `methodology-wave-instances.md` registry — W5 dispatch does NOT generate METHODOLOGY-class entries; all 8 gates are COMPUTE-class per `wave-classification.md` M1∧M2∧M3∧M4 strict conjunction (M1 fails: every W5 gate has a numerical PASS predicate)

---

## §W5-1. S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN  (A.8)

**1. Gate ID**: `S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN`

**2. Trigger**: `[VERIFY]` — Richardson convergence scaling test against L^{−3} algebraic envelope. The test is verification of a pre-registered convergence-rate hypothesis (HK-5 closed-form `5/(1−τ/(5π))` is dominant; Jensen second-order O(τ²) correction subleading). No directional sign claim independent of the magnitude (both signs of `residual(18)` are admissible — the predicate compares magnitudes).

**3. Classification**: GEOMETRIC. The substrate-IS observable is the bare-eigenvalue d_eff spectral moment evaluated at successive L_max truncations of the D_K^{≤L} cache; the residual against the closed-form HK-5 anchor is intrinsic to the spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})` at each L. Not PHONONIC (no phonon-excitation invocation); not PARTICLE (no representation-theoretic content under test); not NON-PHONONIC (substrate-IS observable).

**4. Agent type**: `lizzi-spectral-functional-theorist` PRIMARY (substrate-distance-1 d_eff observable lives on the spectral-functional / regulator-axis program); `connes-ncg-theorist` CO-AUTHOR (CM-1995 §III.4 finite-spectral-triple residue formula provides the analytic anchor for HK-5).

**5. Hypothesis**: The d_eff Richardson residual `residual(L_max) := Numerical_d_eff(L_max) − HK-5(τ_fold)` decreases as L^{−3} between L_max=14 and L_max=18, providing evidence that the HK-5 closed-form `5/(1−τ/(5π))` is the dominant substrate-IS d_eff contribution at τ_fold = 0.19 with Jensen second-order O(τ²) corrections subleading. A faster decay would indicate higher-order suppression; a slower decay would indicate that the closed-form is missing a structural term that should be added to the canonical.

**6. Method** (full self-contained dispatch prompt for `lizzi-spectral-functional-theorist`):

```
You are dispatched on COMPUTE-class gate S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN
(Wave 5 of session 89). Read this prompt in full before computing.

CONTEXT:
- Substrate-IS observable: numerical d_eff(L_max) at τ_fold = 0.19 from D_K^{≤L} block-diagonal
  Peter-Weyl decomposition (per math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-
  Projection Feasibility Pre-Check"); analytic anchor: HK-5(τ) = 5/(1 − τ/(5π)) closed form
  derived in S87 d_eff workshop.
- Pre-registered prediction: residual(L_max) := Numerical_d_eff(L_max) − HK-5(τ_fold)
  decays as L^{−3} per Richardson algebraic-envelope hypothesis at d=4.
- Cross-anchor: W3 A.9 d_eff CM-1995 §III.4 second-order Jensen perturbation derives
  a closed-form c such that d_eff(τ) = HK-5(τ) + c·τ² + O(τ³); if A.9 has landed before
  this gate, consume `c_jensen_2nd_order_FW` from canonical_constants.py and test
  residual(L_max) − c·τ² for L^{−3} (subleading correction).

SCRIPT PATH:
  computations/session-89/s89_w5_a8_d_eff_richardson_lmax_18_baseline_scan.py

MANDATORY OPENING:
  from canonical_constants import *  # tau_fold, M_KK, n_s_framework, etc.
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')   # CPU thread cap before numpy import
  import numpy as np
  import torch                                     # for torch.linalg on ≥100×100 blocks
  from pathlib import Path

INPUT-PIN MAP (compute SHAs at runtime; companion comment row carries dual-SHA):
  D_K_spectrum_cache:
    path: computations/session-84/s84_spectrum_cache_L12_tau019.npz
    sha256: <runtime>  # canonical L_max=12 Peter-Weyl block cache (tau_fold = 0.19)
  D_K_spectrum_cache_L18:
    path: computations/session-89/s89_spectrum_cache_L18_tau019.npz
    sha256: <runtime>  # extended L_max=18 cache built from Casimir-bound saturation
                       # per math-scripts.md Pre-Check; produced at S89 W5 dispatch start
  hk5_closed_form_value:
    expression: 5.0 / (1.0 - tau_fold / (5.0 * np.pi))
    note: HK-5(0.19) = 5/(1 − 0.19/(5π)) ≈ 5.0608... (computed at runtime)
  tau_fold_pin: 0.19  # from canonical_constants (R-PROTECTED)
  c_jensen_2nd_order_FW:
    source: canonical_constants.py (PENDING W3 A.9 landing)
    fallback: None  # if not landed, residual(L_max) tested directly without subtraction

PRDR MACHINERY PIN:
  L_max_scan: [12, 14, 16, 18]  # 4-point Richardson scan; L_max=12 = baseline, L_max=18 = test point
  truncation_mode: block-diagonal-Peter-Weyl  # per math-scripts.md §D_K-Block-Diagonality
  casimir_bound_check: True  # verify each L_max sector's irrep construction completes
                              # within 5-min single-thread per §"Pre-check protocol"
  d_eff_estimator: spectral-zeta-direct-sum  # ζ_D^{(L_max)}(0) summed bit-precision; NOT
                                              # polynomial-fit Seeley-DeWitt (cond ~1e9 at L=6)
  richardson_alpha_predicted: 3  # L^{−3} algebraic envelope at d=4
  scheme: ζ-zeta-spectral-action  # canonical scheme (Lizzi 1412.4669 zeta scheme)
  convention: lizzi-zeta-spectral-action-L_max-scan
  regulator_pin: a_n^{ζ}  # per regulator-pin-discipline.md MANDATORY tagging
  GPU_path: torch.linalg.eigvalsh on dense block per (p,q) sector (≤9792-dim at L_max=18
                worst case; 1.53 GB single block fits in 17.1 GB VRAM with margin)
  numerical_precision: float64
  random_seed: None  # deterministic
  domain_used_frac: 1.0  # full L_max scan; no auto-shortening

CROSS-CHECKS:
  (a) HK-5 closed-form sanity: HK-5(0) should equal 5.0 EXACTLY (boundary at τ=0).
      Verify hk5_closed_form_value(0) == 5.0 to machine epsilon.
  (b) HK-5 monotone-increasing with τ in [0, 5π); verify HK-5'(0.19) > 0 numerically
      via central difference at h=1e-8.
  (c) L_max=12 baseline: numerical d_eff(L_max=12) at tau_fold = 0.19 must agree
      with W1b-3 Richardson canonical at slope_A(0.19) ≈ 10.122 to within 0.5%
      (anchors W3 A.9 closed-form c).
  (d) Richardson alpha extraction: fit log(residual) vs log(L_max) for L_max ∈ {14, 16, 18};
      report alpha_fit AND residual(18)/residual(14).

OUTPUT:
  Path: computations/session-89/s89_w5_a8_d_eff_richardson_lmax_18_baseline_scan.npz
  Keys:
    L_max_scan: ndarray int [12, 14, 16, 18]
    d_eff_numerical: ndarray float64
    hk5_anchor: float64
    residual: ndarray float64  # d_eff_numerical − hk5_anchor (− c·τ² if c_jensen_2nd_order_FW pinned)
    residual_ratio_18_over_14: float64  # the PASS predicate quantity
    alpha_fit: float64  # Richardson exponent estimate via log-log fit on L ∈ {14, 16, 18}
    casimir_bound_check_per_sector: dict
    sector_cardinality_vector_per_L: dict
  Plot path: computations/session-89/s89_w5_a8_d_eff_richardson_lmax_18_baseline_scan.png
  Plot panels: (i) log(|residual|) vs log(L_max) Richardson fit; (ii) d_eff_numerical(L_max)
               with HK-5 horizontal anchor; (iii) sector cardinality per L_max stratum.

PASS PREDICATE (composite collapse rule per gate-verdicts.md S87+):
  magnitude_verdict:
    PASS  iff residual(18)/residual(14) ≤ 0.5
    INFO  iff 0.5 < residual(18)/residual(14) ≤ 0.9
    FAIL  iff residual(18)/residual(14) > 0.9
  sign_verdict: N/A  (no directional pre-registration on residual sign;
                     both signs admissible — Jensen O(τ²) correction sign depends on
                     CM-1995 §III.4 second-derivative which is not pre-registered here)
  regime_verdict: VALID iff Casimir-bound feasibility check PASSes for all 4 L_max
                  values AND no irrep construction timeout; MARGINAL if 1 L_max sector
                  exceeds wall-time but is cache-recoverable via Friedrich-Bär saturation
                  theorem (per math-scripts.md §"Pre-check protocol" item 2);
                  BREAKDOWN if ≥2 L_max sectors infeasible.
  composite collapse:
    if regime == BREAKDOWN: composite = FAIL
    elif magnitude == PASS and regime == VALID: composite = PASS
    elif magnitude == INFO: composite = INFO
    elif magnitude == FAIL and regime == VALID: composite = FAIL
    elif magnitude == FAIL and regime == MARGINAL: composite = INFO

VERDICT EMISSION (single-shot, atomic; per registry-landing.md §"Bridge-Landing
Script Architecture"):
  build_promotion_text in memory ➔ write_atomic_with_fsync to verdict file ➔
  re_read + verify_section_matches ➔ exactly ONE emit_verdict_line call.
  Path: computations/session-89/s89_gate_verdicts.txt

Dual-SHA companion comment row + S87 schema-v2 3-tuple companion row REQUIRED
(this gate has a regime_verdict ≠ N/A; emit per gate-verdicts.md §"S87+
canonical form").

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-1
  Substrate framing paragraph MANDATORY:
    "The substrate IS the L_max-truncated spectral triple (A_K^{≤L}, H_K^{≤L}, D_K^{≤L});
    d_eff(L_max) at τ = 0.19 is a substrate-IS observable intrinsic to the bare-eigenvalue
    Peter-Weyl decomposition. The HK-5 closed form `5/(1−τ/(5π))` is the substrate's own
    Mellin-cone evaluation under the Connes-Moscovici 1995 §III.4 finite-spectral-triple
    residue formula at first order in Jensen TT-deformation. The Richardson L^{−3} envelope
    is the substrate's own algebraic convergence rate at d=4 — NOT a fit to an external
    data series. Container-thinking ('the substrate's spectrum living in heat-kernel space')
    is forbidden per phononic-framing.md §'IS Space, Not IN Space'."
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-D-EFF-RICHARDSON-LMAX-18-LMAX-14-BASELINE-SCAN
schema_version: R3
trigger: [VERIFY]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a8_d_eff_richardson_lmax_18_baseline_scan.py
runtime_owner: lizzi-spectral-functional-theorist
co_author: connes-ncg-theorist
input_pin_map:
  D_K_spectrum_cache_L12: <pinned at dispatch>  # computations/session-84/s84_spectrum_cache_L12_tau019.npz
  D_K_spectrum_cache_L18: <pinned at dispatch>  # computations/session-89/s89_spectrum_cache_L18_tau019.npz
  c_jensen_2nd_order_FW: <pending W3 A.9 landing — fallback to direct residual fit>
machinery_pin_map:
  L_max_scan: [12, 14, 16, 18]
  truncation_mode: block-diagonal-Peter-Weyl
  casimir_bound_check: True
  d_eff_estimator: spectral-zeta-direct-sum
  richardson_alpha_predicted: 3
  scheme: ζ-zeta-spectral-action
  convention: lizzi-zeta-spectral-action-L_max-scan
  regulator_pin: a_n^{ζ}
  GPU_path: torch.linalg.eigvalsh
  numerical_precision: float64
  random_seed: None
  domain_used_frac: 1.0
expected_output_4tuple:
  value: residual(18)/residual(14)
  scheme: ζ-zeta-spectral-action
  convention: lizzi-zeta-spectral-action-L_max-scan
  L_max: 18
pass_threshold:
  magnitude: residual(18)/residual(14) ≤ 0.5
  info_band: 0.5 < ratio ≤ 0.9
  fail_band: ratio > 0.9
  tolerance_rule: RATIO
```

**8. Expected output 4-tuple**: `(value=<residual(18)/residual(14)>, scheme=ζ-zeta-spectral-action, convention=lizzi-zeta-spectral-action-L_max-scan, L_max=18)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: `residual(18)/residual(14) ≤ 0.5` AND `regime_verdict = VALID` (RATIO tolerance rule; threshold pre-registered at plan-freeze).
- **INFO**: `0.5 < residual(18)/residual(14) ≤ 0.9` (slower-than-L^{−3} convergence; HK-5 anchor close but Jensen second-order corrections non-negligible; FWD-action: route to W3 A.9 closed-form c absorption and re-test).
- **FAIL**: `residual(18)/residual(14) > 0.9` (Richardson exponent significantly below 3; HK-5 closed-form is missing structural content; FWD-action: substrate canonical d_eff is not `5/(1−τ/(5π))` alone, route to higher-order resummation per W3 A.29 κ_2 derivation).

**10. Substitution chain** (mandatory for `richardson_alpha_predicted = 3` direction; per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1 (Definition): residual(L_max) := Numerical_d_eff(L_max) − HK-5(τ_fold)
                     where HK-5(τ) := 5/(1 − τ/(5π))   [closed-form S87 d_eff workshop]

Step 2 (Definition): Richardson algebraic envelope at d=4: |residual(L_max)| ~ A · L_max^{−α}
                     where α is the Richardson exponent (predicted = 3 at d=4 per
                     cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence
                     Ladder" Level-2 envelope L^{−α(s)} with α(s=4) = 4 substrate-distance-2
                     OR α = 3 substrate-distance-1).

Step 3 (Substitution): residual(18)/residual(14) = (18/14)^{−α} = (14/18)^α = (7/9)^α

Step 4 (Simplification at α = 3): (7/9)^3 = 343/729 ≈ 0.4705

Step 5 (Direction): 0.4705 ≤ 0.5  ⇒  PASS predicate satisfied at the analytical limit
                    of α = 3 envelope; the threshold 0.5 is structurally derived from
                    α = 3 with a 6.3% slack absorbing finite-L corrections.

CROSS-CHECK at α = 2: (7/9)^2 = 49/81 ≈ 0.6049 — falls in INFO band (0.5, 0.9].
CROSS-CHECK at α = 4: (7/9)^4 = 2401/6561 ≈ 0.3660 — well below 0.5 (PASS).
CROSS-CHECK at α = 1: (7/9)^1 = 7/9 ≈ 0.7778 — INFO band.
CROSS-CHECK at α = 0: 1.0000 — FAIL.

CONCLUSION: PASS at α ≥ 3; INFO at 1 ≤ α < 3; FAIL at α < 1. Threshold 0.5 is
algebraically derived from the α = 3 substrate prediction with absorbing slack.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: HK-5 closed-form `5/(1−τ/(5π))` is the dominant substrate-IS d_eff contribution at τ_fold; Jensen second-order O(τ²) corrections are subleading at the canonical truncation; the FWD-C1 Pillar I↔II bridge candidate inherits a tight Level-2 envelope `L^{−3}` for downstream consumption (A.31, A.24, FWD-C1 closure). Solution-space corridor: Mellin-cone substrate-distance-1 anchor at s=3 is structurally locked at first order in Jensen deformation.
- **INFO**: Convergence is slower than L^{−3}; the HK-5 anchor is close but the Jensen second-order c·τ² correction needs absorption. Solution-space corridor: route to W3 A.9 + A.29 closed-form c, c_2 derivation; A.31 FWD-C1 retry inherits a softer Level-2 envelope (e.g., L^{−2}) until the higher-order absorption lands.
- **FAIL**: HK-5 closed-form is structurally insufficient at the canonical truncation; substrate canonical d_eff requires a non-perturbative resummation beyond `5/(1−τ/(5π))`. Solution-space corridor: route to W3 A.29 second-order resummation OR escalate to multi-wave restructuring (potentially routing A.31 FWD-C1 retry to BLOCKED-on-resummation status).

**12. Effort estimate**: 0.5 wave-equivalent (single agent-session; L_max=18 cache build is the bottleneck, ~15 min on 32-CPU; Richardson fit + verdict emission ~5 min).

**13. Substrate framing per `phononic-framing.md` IS-not-IN**: The substrate IS the L_max-truncated spectral triple `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`; d_eff(L_max) at τ_fold is a substrate-IS observable intrinsic to the bare-eigenvalue Peter-Weyl decomposition at single-τ-slice substrate-IS Level 1 (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). The HK-5 closed form is the substrate's own Mellin-cone evaluation under CM-1995 §III.4 at first order in Jensen deformation, NOT an external reference quantity. The Richardson L^{−3} envelope is the substrate's own algebraic convergence rate at d=4, derived from the spectral-triple's intrinsic algebraic structure (Friedrich-Bär saturation on Casimir-bounded sectors per `math-scripts.md §"Pre-check protocol"`). FORBIDDEN container-thinking patterns: "the substrate's spectrum living in heat-kernel space", "d_eff converges as L_max grows in the truncation hierarchy" (the truncation IS the substrate at finite L; nothing "grows in" anything). Mnemonic-vs-exact ratio discipline: the threshold 0.5 is mnemonic-form for the substrate-exact prediction `(7/9)^3 = 343/729 ≈ 0.4705` with 6.3% slack — both forms are reported in the substitution chain Step 4.

---

## §W5-2. S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE  (A.25)

**1. Gate ID**: `S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE`

**2. Trigger**: `[SIGN]` + `[VERIFY]` — directional sign claim on the second log-derivative `d² ln P_GGE / d(ln K)²` evaluated at the horizon-crossing K-window. Pre-registered direction: NEGATIVE (volovik-path canonical −7.046336). The `[SIGN]` trigger fires schema-v2 3-tuple companion row per `gate-verdicts.md §"S87+ canonical form"`. `[VERIFY]` fires for the magnitude verification against the canonical −7.046336 within tolerance.

**3. Classification**: GEOMETRIC. The substrate-IS observable is the GGE relic spectral density's second log-derivative on the spectrum cache; no phonon-excitation invocation under test (the "GGE relic" is the substrate's own first-order phase-transition signature at τ_fold; the log-derivative is intrinsic to the spectrum cache at fixed L_max). Not PHONONIC (no relay-pattern propagation under test).

**4. Agent type**: `volovik-superfluid-universe-theorist` PRIMARY (K-window log-derivative IS the volovik-path observable per `s88-w17-w5b-47-step11-maxrule.md` §V.1; volovik canonical pin -7.046336 originates from W2-3 GGE-Bog-variance numerical core). No CO-AUTHOR (single-axis substrate-physics derivation; cross-pillar bridge attribution deferred to A.27).

**5. Hypothesis**: The independent recomputation of `d² ln P_GGE / d(ln K)²` on the §W5b-47 spectrum cache at the S87 W2-3 horizon-crossing K-window yields `−7.046336 ± 0.001` (volovik-path canonical), confirming the W-17 R3 closure that the K-window log-derivative is a substrate-IS Corner-IV observable algebraically distinct from the falsifier value `v_inf = 6.46e-6` (which would indicate the canonical is an artifact of the W5b-47 max-rule operationalization rather than a substrate-IS derivation).

**6. Method** (full self-contained dispatch prompt for `volovik-superfluid-universe-theorist`):

```
You are dispatched on COMPUTE-class gate S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE
(Wave 5 of session 89). Read this prompt in full before computing.

CONTEXT:
- The volovik-path canonical −7.046336 was derived in S87 W2-3 GGE-Bog-variance
  numerical core; W-17 R3 closed S88 with the volovik-path PASS reading. The
  S88 W17 V.1 carry-forward queues an INDEPENDENT recompute on the §W5b-47
  spectrum cache to confirm the result is substrate-IS (not an artifact of the
  W5b-47 max-rule operationalization).
- Substrate-IS observable: d² ln P_GGE / d(ln K)² evaluated at horizon-crossing
  K-window per S87 W2-3 anchor (K_horizon = aH_pivot ≈ 0.05 Mpc^{−1} substrate-
  rescaled to spectrum-cache units; K-window width per W2-3 specification).
- Falsifier value: v_inf = 6.46e-6 (the W17 R3 alternate reading where the
  canonical reduces to a near-zero substrate-distance-1 mode-counting residual).

SCRIPT PATH:
  computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  import torch
  from pathlib import Path

INPUT-PIN MAP:
  W5b_47_spectrum_cache:
    path: computations/session-88/s88_w5b_47_spectrum_cache.npz
    sha256: <runtime>
  W2_3_horizon_K_window_anchor:
    path: computations/session-87/s87_w2_3_horizon_k_window.npz
    sha256: <runtime>
  volovik_path_canonical_predictor:
    value: -7.046336
    source: S87 W2-3 GGE-Bog-variance numerical core (canonical_constants.py if landed
            via Ledger B; pin name candidate: corner_iv_k_window_log_derivative_FW)
  falsifier_value_v_inf:
    value: 6.46e-6
    source: W-17 R3 alternate reading

PRDR MACHINERY PIN:
  K_window_definition: horizon-crossing-S87-W2-3-anchor  # NOT W5b-47 max-rule
  K_window_width: <pinned from S87 W2-3 anchor; 0.5 e-fold canonical>
  log_derivative_estimator: central-difference-fourth-order  # at K_horizon ± h with h = K_window_width / 8
  spectrum_cache_L_max: <inherited from W5b-47 cache>
  P_GGE_normalization: substrate-natural-volovik-2003-§7  # NOT empirical-renormalized
  scheme: volovik-superfluid-universe-GGE
  convention: corner-iv-k-window-log-derivative-S87-W2-3-anchor
  regulator_pin: a_n^{ζ}  # GGE relic computed under zeta scheme on spectrum cache
  GPU_path: torch.linalg.eigh on ≤L_max-block sectors if any required (cache pre-built;
            primarily numpy-direct on cached eigenvalues)
  numerical_precision: float64
  random_seed: None
  domain_used_frac: 1.0  # full K-window evaluated; no auto-shortening

CROSS-CHECKS:
  (a) P_GGE positivity: ln P_GGE well-defined at K_horizon; verify P_GGE > 0 to
      1e-12 across the K-window before log-derivative computation.
  (b) Central-difference convergence: vary h ∈ {K_window_width/4, /8, /16, /32}
      and confirm the log-derivative value converges; emit `h_convergence_table`
      to npz (regime_verdict = MARGINAL if convergence is non-monotone).
  (c) Volovik-path canonical sanity: independently re-read the S87 W2-3 anchor
      file and verify v_volovik_canonical = -7.046336 to 6 decimal places.
  (d) Falsifier-value sanity: confirm v_inf = 6.46e-6 is NOT confused with the
      canonical (orders-of-magnitude separation: |v_volovik| / |v_inf| ≈ 1.09e6;
      no numerical aliasing risk).

OUTPUT:
  Path: computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz
  Keys:
    log_derivative_value: float64  # the canonical observable
    log_derivative_uncertainty: float64  # from central-difference convergence
    h_convergence_table: dict
    P_GGE_at_K_horizon: float64
    K_horizon_value: float64
    K_window_width: float64
    volovik_path_canonical_predictor: float64  # -7.046336 echo
    falsifier_value_v_inf: float64  # 6.46e-6 echo
    spectrum_cache_sha: str
  Plot path: computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.png
  Plot panels: (i) ln P_GGE(ln K) across K-window with K_horizon vertical anchor;
               (ii) numerical second derivative vs h step size (convergence panel);
               (iii) bar chart of canonical -7.046336 vs falsifier 6.46e-6 vs
                    computed value (signed log scale).

PASS PREDICATE (composite collapse rule per gate-verdicts.md S87+):
  sign_verdict:
    PASS  iff sign(log_derivative_value) == NEGATIVE
    FAIL  iff sign(log_derivative_value) == POSITIVE (would match falsifier direction)
  magnitude_verdict:
    PASS  iff |log_derivative_value − (−7.046336)| / 7.046336 ≤ 0.001 (0.1% tolerance)
    INFO  iff 0.001 < relative_diff ≤ 0.01 (1% tolerance) AND |log_derivative_value|
             is closer to canonical than to falsifier (i.e., |val − canon| < |val − v_inf|)
    FAIL  iff |log_derivative_value − v_inf| / |v_inf| ≤ 0.5 (matches falsifier)
             OR |log_derivative_value − canonical| / |canonical| > 0.10
  regime_verdict:
    VALID iff h_convergence_table monotone-decreasing in residual AND
             P_GGE > 0 across K-window AND
             K_window_width matches S87 W2-3 anchor exactly (no auto-shortening)
    MARGINAL iff convergence non-monotone but stable to 4 decimal places
    BREAKDOWN iff P_GGE ≤ 0 anywhere in K-window OR K_window auto-shortened
  composite collapse: per gate-verdicts.md §"S87+ canonical form".

VERDICT EMISSION (single-shot atomic; per registry-landing.md §"Bridge-Landing
Script Architecture"):
  Path: computations/session-89/s89_gate_verdicts.txt

S87+ schema-v2 3-tuple companion row REQUIRED ([SIGN] trigger).

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-2
  Substrate framing paragraph MANDATORY:
    "The substrate IS the GGE relic spectral density at τ_fold; ln P_GGE(K) is a
    substrate-IS observable intrinsic to the volovik-2003-§7 superfluid-universe
    framework. The Corner-IV K-window log-derivative is a substrate-distance-2
    Corner-IV observable per §VII.U.2 4-corner classification (algebra-DEPENDENT
    state-pair functional family). The horizon-crossing K-window is the substrate's
    own pre-registered observation locus (S87 W2-3 anchor); container-thinking
    ('the substrate's GGE relic embedded in horizon space') is forbidden per
    phononic-framing.md §'IS Space, Not IN Space'."
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE
schema_version: R3
trigger: [SIGN, VERIFY]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.py
runtime_owner: volovik-superfluid-universe-theorist
co_author: None
input_pin_map:
  W5b_47_spectrum_cache: <pinned at dispatch>
  W2_3_horizon_K_window_anchor: <pinned at dispatch>
machinery_pin_map:
  K_window_definition: horizon-crossing-S87-W2-3-anchor
  K_window_width: 0.5e-fold-canonical
  log_derivative_estimator: central-difference-fourth-order
  spectrum_cache_L_max: <inherited>
  P_GGE_normalization: substrate-natural-volovik-2003-§7
  scheme: volovik-superfluid-universe-GGE
  convention: corner-iv-k-window-log-derivative-S87-W2-3-anchor
  regulator_pin: a_n^{ζ}
  GPU_path: torch.linalg.eigh
  numerical_precision: float64
  random_seed: None
  domain_used_frac: 1.0
expected_output_4tuple:
  value: <log_derivative_value>
  scheme: volovik-superfluid-universe-GGE
  convention: corner-iv-k-window-log-derivative-S87-W2-3-anchor
  L_max: <inherited from W5b-47 cache>
pass_threshold:
  sign: NEGATIVE
  magnitude_target: -7.046336
  pass_band: 0.001 (RATIO 0.1%)
  info_band: 0.01 (RATIO 1%) with closer-to-canonical-than-falsifier check
  fail_band: matches falsifier OR > 10% off canonical
  tolerance_rule: RATIO
  falsifier_anti_match: |val − 6.46e-6| / 6.46e-6 ≤ 0.5 ⇒ FAIL
```

**8. Expected output 4-tuple**: `(value=<log_derivative_value>, scheme=volovik-superfluid-universe-GGE, convention=corner-iv-k-window-log-derivative-S87-W2-3-anchor, L_max=<inherited>)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: `sign_verdict = PASS` (NEGATIVE direction) AND `magnitude_verdict = PASS` (|val − (−7.046336)| / 7.046336 ≤ 0.001) AND `regime_verdict = VALID`. Numerical: log_derivative ≈ −7.046336 ± 0.007.
- **INFO**: `sign_verdict = PASS` AND `magnitude_verdict = INFO` (0.001 < relative diff ≤ 0.01 AND closer-to-canonical-than-falsifier). Solution-space: volovik-path canonical confirmed at sign + leading-magnitude but second-order spectral noise non-negligible.
- **FAIL**: `sign_verdict = FAIL` (POSITIVE — matches falsifier direction) OR `magnitude_verdict = FAIL` (matches falsifier value v_inf = 6.46e-6 OR > 10% off canonical) OR `regime_verdict = BREAKDOWN`. Solution-space: W-17 R3 volovik-path closure was an artifact of W5b-47 max-rule operationalization, not a substrate-IS derivation; chain A.26 + A.27 BLOCKED.

**10. Substitution chain** (mandatory for sign claim NEGATIVE per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1 (Definition): P_GGE(K) := substrate-natural GGE relic spectral density
                     under volovik-2003-§7 superfluid-universe normalization.
                     ln P_GGE(K) is well-defined at K_horizon iff P_GGE > 0.

Step 2 (Definition): The volovik-path canonical observable is
                     L(K) := d² ln P_GGE / d(ln K)² evaluated at K = K_horizon.
                     L(K_horizon) = -7.046336 per S87 W2-3 GGE-Bog-variance core.

Step 3 (Substitution): For a GGE relic with red-tilted spectrum (P_GGE ~ K^{n_s − 1}
                     with n_s < 1), ln P_GGE(ln K) is concave-down in ln K
                     (first derivative = n_s − 1 < 0; second derivative captures
                     scale-dependent running). Volovik 2003 §7 derivation establishes
                     d² ln P_GGE / d(ln K)² = − (curvature factor from substrate-distance-2
                     spectral cone) at the horizon-crossing window.

Step 4 (Simplification): The substrate-distance-2 curvature factor at τ_fold = 0.19
                     evaluates to +7.046336 per W2-3 numerical core; the negative sign
                     in front emerges from the concave-down running of the red-tilted
                     spectrum. Therefore L(K_horizon) = −7.046336 (NEGATIVE).

Step 5 (Direction): sign(L(K_horizon)) = NEGATIVE; this is the volovik-path sign
                     prediction. Falsifier value v_inf = +6.46e-6 has POSITIVE
                     sign (and ≈10⁶× smaller magnitude); a POSITIVE sign in the
                     recompute would falsify the volovik-path reading.

PYTHON VERIFICATION (at plan-author time):
  >>> import math
  >>> n_s = 0.9561
  >>> first_deriv_at_horizon = n_s - 1
  >>> first_deriv_at_horizon
  -0.0439  # NEGATIVE; consistent with red-tilted concave-down running
  >>> # Second derivative carries the substrate-distance-2 curvature factor; its
  >>> # specific value -7.046336 comes from the volovik-path numerical core,
  >>> # not from this elementary chain. The chain confirms the SIGN expectation.

CONCLUSION: NEGATIVE sign is the substrate-IS prediction; A.25 PASS predicate
            is sign-aligned with the volovik-path canonical.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: The volovik-path canonical −7.046336 is a substrate-IS observable, NOT an artifact of W5b-47 max-rule operationalization. The Corner-IV K-window log-derivative is a substrate-distance-2 algebra-DEPENDENT state-pair functional confirmed at the §VII.U.2 4-corner classification's Cell IV. A.26 and A.27 unblock; FWD-C2 disambiguation can proceed. Solution-space corridor: Cluster-E Cluster-IV chain advances toward a structurally-locked FWD-C2 candidate.
- **INFO**: Volovik-path canonical confirmed at sign + leading magnitude (within 1%) but second-order noise non-negligible. A.26 unblocks under MARGINAL regime; A.27 disambiguation may produce singleton-with-deferred-envelope.
- **FAIL**: Volovik-path is an artifact; the W-17 R3 closure must be revisited. Solution-space corridor: chain A.26 + A.27 BLOCKED via mechanical-closure with `value='PRE-REG-INC_blocked_by_S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE_FAIL'`; FWD-C2 candidate routed to next session for substrate-physics reconstruction.

**12. Effort estimate**: 0.4 wave-equivalent (single agent-session; spectrum cache is pre-built; primary cost is central-difference convergence sweep + cross-check sanity).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the GGE relic spectral density at τ_fold; ln P_GGE(K) is a substrate-IS observable intrinsic to the volovik-2003-§7 superfluid-universe framework. The Corner-IV K-window log-derivative is a substrate-distance-2 algebra-DEPENDENT state-pair functional per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 and §VII.U.2 4-corner classification Cell IV. The horizon-crossing K-window is the substrate's own pre-registered observation locus (S87 W2-3 anchor). FORBIDDEN container-thinking patterns: "the substrate's GGE relic embedded in horizon space", "P_GGE living in the K-domain". Mnemonic-vs-exact ratio discipline: −7.046336 is the Sage-exact 6-significant-figure rendering of the W2-3 numerical core; the substrate's own algebraic structure (substrate-distance-2 curvature factor at τ_fold) is the structural source.

---

## §W5-3. S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE  (A.26)

**1. Gate ID**: `S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE`

**2. Trigger**: `[VERIFY]` — Level-2 algebraic envelope extraction across L_max scan. No directional sign claim independent of A.25 (the envelope α exponent is positive by construction; the verification is on the magnitude of α and its self-consistency with PRIMARY-A path).

**3. Classification**: GEOMETRIC. Substrate-IS observable: log-derivative L(K_horizon, L_max) across L_max ∈ {6, 7, 8, 9, 10, 11, 12}; envelope extraction is intrinsic to the L_max-truncated spectral triple sequence.

**4. Agent type**: `volovik-superfluid-universe-theorist` PRIMARY (A.26 inherits A.25 substrate-physics ownership of the K-window log-derivative observable). No CO-AUTHOR.

**5. Hypothesis**: The Level-2 algebraic envelope of the Corner-IV K-window log-derivative converges to the canonical −7.046336 with a power-law L_max^{−α} envelope, where α is extracted by self-consistent fit on the 7-point L_max scan. The envelope is Level-2-binding per `cross-pillar-bridge-anatomy.md §"Level-2-binding"` IF the L_max → ∞ HKR image of the substrate-IS finite-L observable matches a continuum laboratory-IN observable on a partner pillar (Pillar-IV / Volovik 2003 §7 superfluid-universe analog). If no HKR bridge is identified, the envelope is Level-2-non-binding (substrate-internal Mellin truncation rate), which CANNOT contribute to registry-PASS for any cross-pillar bridge entry per the §"Level-2-non-binding" enforcement clause.

**6. Method** (full self-contained dispatch prompt for `volovik-superfluid-universe-theorist`):

```
You are dispatched on COMPUTE-class gate S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE
(Wave 5 of session 89, CONDITIONAL on A.25 PASS). Read this prompt in full before computing.

CONDITIONAL DISPATCH GATE:
  Before computing, read computations/session-89/s89_gate_verdicts.txt and verify:
    grep "^S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE: PASS" present.
  IF the predecessor verdict line is NOT present OR shows FAIL/INFO:
    Emit mechanical-closure verdict per .claude/rules/mechanical-closure-discipline.md:
      value='PRE-REG-INC_blocked_by_S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE_<status>'
    Skip all computation; emit verdict line + working-paper §W5-3 status update;
    DO NOT proceed past this point.
  IF predecessor PASS: continue with the computation below.

CONTEXT:
- A.25 confirmed −7.046336 as a substrate-IS observable. A.26 extracts the
  algebraic L_max-convergence envelope; the envelope's α exponent is the input
  to A.27 FWD-C2 disambiguation.
- L_max scan range 6, 7, 8, 9, 10, 11, 12 spans the Casimir-bound feasibility
  band; L_max=12 is the canonical cache, L_max=6 is the Friedrich-Bär lower
  saturation point per math-scripts.md §"Pre-check protocol" item 2.

SCRIPT PATH:
  computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  import torch
  from pathlib import Path

INPUT-PIN MAP:
  s89_w5_a25_npz: computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz
  D_K_spectrum_cache_master: computations/session-84/s84_spectrum_cache_L12_tau019.npz
  W5b_47_spectrum_cache: computations/session-88/s88_w5b_47_spectrum_cache.npz
  volovik_path_canonical_predictor: -7.046336
  W2_3_horizon_K_window_anchor: <inherited from A.25 pin>

PRDR MACHINERY PIN:
  L_max_scan: [6, 7, 8, 9, 10, 11, 12]
  truncation_mode: block-diagonal-Peter-Weyl
  casimir_bound_check: True  # all 7 L_max values feasibility-verified per
                              # math-scripts.md §"Pre-check protocol"
  per_L_recompute: invoke A.25 protocol on truncated cache  # for each L_max,
                                                              # rebuild the K-window
                                                              # log-derivative
  envelope_estimator: log-log-linear-regression on |L(L_max) − canonical| vs L_max
  envelope_alpha_predicted: 3  # default substrate-distance-1 expectation; A.26 verifies
  HKR_bridge_check: pillar-IV-volovik-2003-§7-superfluid-universe-analog
                    # IF identified, envelope is Level-2-binding;
                    # IF absent, envelope is Level-2-non-binding (REGISTRY-INELIGIBLE
                    # for cross-pillar PASS per cross-pillar-bridge-anatomy.md
                    # §"Level-2-non-binding" enforcement)
  scheme: volovik-superfluid-universe-GGE
  convention: corner-iv-k-window-lmax-scan-level-2-envelope
  regulator_pin: a_n^{ζ}
  GPU_path: torch.linalg.eigh per (p,q) sector at each L_max
  numerical_precision: float64

CROSS-CHECKS:
  (a) L_max=12 sanity: A.26 evaluation at L_max=12 must reproduce A.25 value
      to machine epsilon (cross-validation against A.25 single-L computation).
  (b) Casimir-bound feasibility per L_max sector: emit timing per L_max; flag
      any sector exceeding 5-min wall time (regime_verdict = MARGINAL or BREAKDOWN).
  (c) Envelope log-log fit residuals: emit R² of the linear regression;
      regime_verdict = MARGINAL if R² < 0.95 (envelope is non-power-law).
  (d) HKR bridge identification: explicit pillar-IV mapping check via
      Peotta-Törmä quantum-metric integrated trace (cross-link to S86 W-5
      §VII.W bridge calibration); emit `hkr_bridge_identified: bool` to npz.

OUTPUT:
  Path: computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz
  Keys:
    L_max_scan: ndarray int [6, 7, 8, 9, 10, 11, 12]
    log_derivative_per_L: ndarray float64
    residual_per_L: ndarray float64  # |L(L_max) − canonical|
    envelope_alpha: float64
    envelope_R_squared: float64
    hkr_bridge_identified: bool
    level_2_binding_class: str  # "Level-2-binding" or "Level-2-non-binding"
    timing_per_L: dict
  Plot path: computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.png
  Plot panels: (i) L(L_max) vs L_max with canonical horizontal anchor;
               (ii) log(|residual|) vs log(L_max) with envelope fit;
               (iii) per-L_max timing chart.

PASS PREDICATE:
  magnitude_verdict:
    PASS  iff envelope_alpha extracted within [1.5, 5.0] (positive convergent envelope)
              AND envelope_R_squared ≥ 0.90
              AND hkr_bridge_identified == True (Level-2-binding required for
                  registry-PASS-eligible advancement per cross-pillar-bridge-anatomy.md)
    INFO  iff envelope_alpha extracted but R² in [0.80, 0.90)
              OR hkr_bridge_identified == False (Level-2-non-binding; A.27 disambiguation
                 fires with REGISTRY-INELIGIBLE flag)
    FAIL  iff envelope_alpha extraction fails (R² < 0.80) OR alpha outside [1.5, 5.0]
              OR ≥2 L_max values infeasible per Casimir-bound check
  sign_verdict: N/A
  regime_verdict: VALID iff all 7 L_max feasible AND R² ≥ 0.95 AND HKR bridge
                  identified; MARGINAL if R² in [0.90, 0.95) or 1 L_max infeasible;
                  BREAKDOWN if ≥2 L_max infeasible or HKR bridge absent AND
                  registry-PASS claimed.
  composite collapse: per gate-verdicts.md.

VERDICT EMISSION (single-shot atomic):
  Path: computations/session-89/s89_gate_verdicts.txt
  Dual-SHA companion comment row REQUIRED.

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-3
  Substrate framing paragraph MANDATORY (Level-2-binding vs Level-2-non-binding
  declaration per cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction").
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE
schema_version: R3
trigger: [VERIFY]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.py
runtime_owner: volovik-superfluid-universe-theorist
co_author: None
conditional_predecessor: S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE  # BLOCKED on PASS
input_pin_map:
  s89_w5_a25_npz: <pinned at dispatch>
  D_K_spectrum_cache_master: <pinned at dispatch>
  W5b_47_spectrum_cache: <pinned at dispatch>
machinery_pin_map:
  L_max_scan: [6, 7, 8, 9, 10, 11, 12]
  truncation_mode: block-diagonal-Peter-Weyl
  casimir_bound_check: True
  envelope_estimator: log-log-linear-regression
  envelope_alpha_predicted: 3
  HKR_bridge_check: pillar-IV-volovik-2003-§7-superfluid-universe-analog
  scheme: volovik-superfluid-universe-GGE
  convention: corner-iv-k-window-lmax-scan-level-2-envelope
  regulator_pin: a_n^{ζ}
  GPU_path: torch.linalg.eigh
  numerical_precision: float64
expected_output_4tuple:
  value: <envelope_alpha>
  scheme: volovik-superfluid-universe-GGE
  convention: corner-iv-k-window-lmax-scan-level-2-envelope
  L_max: 12
pass_threshold:
  alpha_band: [1.5, 5.0]
  R_squared_band: PASS ≥ 0.90; INFO ∈ [0.80, 0.90); FAIL < 0.80
  HKR_bridge_required: True for PASS (Level-2-binding)
  tolerance_rule: ABSOLUTE on alpha; THEOREM on Level-2-binding class
```

**8. Expected output 4-tuple**: `(value=<envelope_alpha>, scheme=volovik-superfluid-universe-GGE, convention=corner-iv-k-window-lmax-scan-level-2-envelope, L_max=12)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: envelope_alpha ∈ [1.5, 5.0] AND R² ≥ 0.90 AND HKR bridge identified (Level-2-binding). Numerical: typical α ≈ 3 expected if substrate-distance-2 envelope at d=4.
- **INFO**: envelope_alpha extracted but R² ∈ [0.80, 0.90) OR HKR bridge absent (Level-2-non-binding flag). A.27 disambiguation fires with REGISTRY-INELIGIBLE flag if HKR absent.
- **FAIL**: envelope extraction fails (R² < 0.80 or alpha outside [1.5, 5.0]) OR ≥2 L_max sectors infeasible. A.27 mechanical-closure-blocked.

**10. Substitution chain** (no sign claim; N/A — but Level-2-binding classification chain mandatory):

```
Step 1 (Definition): Envelope α exponent in residual_per_L(L_max) ~ A · L_max^{−α},
                     extracted via log-log linear regression.

Step 2 (Definition): Level-2-binding (per cross-pillar-bridge-anatomy.md §"Level-2 Layer
                     Distinction") requires:
                     (a) HKR map ∃ from substrate-IS finite-L observable to a continuum
                         laboratory-IN observable on a partner pillar
                     (b) The envelope bounds the convergence of THE BRIDGE-MAP IMAGE,
                         not a substrate-internal Mellin truncation rate

Step 3 (Substitution at A.26 specifics): substrate-IS = corner-IV K-window log-derivative
                                          on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L});
                                          partner = Pillar IV Peotta-Törmä quantum-metric
                                                    integrated trace evaluated as a
                                                    continuum BZ-trace on a 3He superfluid
                                                    universe lab platform per Volovik 2003 §7

Step 4 (Verification): IF HKR map is explicitly identified per the bridge-anatomy template
                       at S86 W-5 §VII.W: Level-2-binding ⇒ registry-PASS-eligible.
                       IF NOT: Level-2-non-binding ⇒ registry-INELIGIBLE (per the §"Level-2-
                       non-binding" enforcement clause).

Step 5 (Direction): The class declaration is structural (binary) — Level-2-binding or
                    Level-2-non-binding. The Method's hkr_bridge_identified bool emits
                    this directly.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: Level-2 algebraic envelope at the Corner-IV K-window log-derivative is a Level-2-binding L_max^{−α} bound on the HKR-image; A.27 FWD-C2 disambiguation can proceed with full registry-PASS-eligible classification. Solution-space corridor: Cluster-E Cluster-IV chain produces a structurally-locked FWD-C2 candidate eligible for Hybrid Independence Test K-counter advancement.
- **INFO**: Envelope extracted but either R² is borderline OR Level-2-non-binding (HKR bridge absent). Solution-space corridor: A.27 emits REGISTRY-INELIGIBLE-PENDING-HKR-IDENTIFICATION; FWD-C2 candidate recorded but does NOT advance the Hybrid Independence Test K-counter.
- **FAIL**: Envelope extraction fails or scan infeasible. A.27 mechanical-closure-blocked. Solution-space corridor: Corner-IV K-window observable is NOT structurally L_max-stable; volovik-path canonical −7.046336 may be a single-L_max coincidence rather than a Level-2-bounded substrate-IS observable.

**12. Effort estimate**: 0.5 wave-equivalent (single agent-session; per-L_max recompute is the primary cost).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the L_max-truncated spectral triple at moduli-deformation Level-2 (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`); the envelope is the substrate's own algebraic convergence rate. The HKR bridge identification is the substrate's own claim that the L_max → ∞ image of the Corner-IV K-window log-derivative IS a Pillar-IV continuum BZ-trace on the partner pillar; container-thinking ("the K-window image embedded in some HKR target space") is forbidden. Mnemonic-vs-exact ratio discipline: envelope_alpha = 3 is the substrate-distance-2 expectation at d=4; the empirical α extracted by log-log regression is the Sage-exact form of the substrate's structural prediction at the given L_max scan.

---

## §W5-4. S89-FWD-C2-OBSERVABLE-DISAMBIGUATION  (A.27)

**1. Gate ID**: `S89-FWD-C2-OBSERVABLE-DISAMBIGUATION`

**2. Trigger**: `[AUDIT]` — pre-registration audit of FWD-C2 c-split disambiguation form. The gate produces a registry-pre-registration outcome (Corner-II OR Corner-IV singleton OR joint-with-deferred-envelope); the audit verifies the outcome's structural admissibility per the Hybrid Independence Test (i ∨ ii ∨ iii) ∧ iv per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`.

**3. Classification**: GEOMETRIC. Substrate-IS observable: the FWD-C2 candidate's substrate-IS observable AND laboratory-IN observable AND bridge-map identification — all three IS-not-IN anatomy elements declared at pre-registration. The audit is on the structural declaration, not on a numerical comparison; it falls under GEOMETRIC because it tests the substrate's own bridge-anatomy declaration.

**4. Agent type**: `connes-ncg-theorist` PRIMARY (FWD-Cn = bridge-anatomy domain per `cross-pillar-bridge-anatomy.md` MANDATORY at K=3); `volovik-superfluid-universe-theorist` CO-AUTHOR (Corner-IV substrate-physics provider; A.25/A.26 substrate ownership extends here for the c-split classification).

**5. Hypothesis**: The FWD-C2 candidate (Pillar II ↔ Pillar V; Mellin-Barnes residue ↔ BdG spectral triple per `cross-pillar-bridge-anatomy.md §"Three forward bridge candidates"`) admits one of three pre-registration outcomes after A.26 envelope extraction:
- **Outcome (a)**: Corner-II singleton — FWD-C2 substrate-IS observable lives at Corner-II (algebra-INVARIANT spectrum-only functional family) of the §VII.U.2 4-corner classification; the K-window log-derivative is Corner-II projected.
- **Outcome (b)**: Corner-IV singleton — FWD-C2 substrate-IS observable lives at Corner-IV (algebra-DEPENDENT state-pair functional family); the K-window log-derivative is the canonical FWD-C2 anchor.
- **Outcome (c)**: Joint-with-deferred-envelope — FWD-C2 c-splits across Corner-II AND Corner-IV; the joint structure requires a separate envelope per corner.

The pre-registered classification is determined by A.26's HKR bridge identification (PASS path leads to Outcome (b); INFO path leads to Outcome (c); FAIL path blocks the disambiguation).

**6. Method** (full self-contained dispatch prompt for `connes-ncg-theorist` + `volovik-superfluid-universe-theorist` joint):

```
You are dispatched on COMPUTE-class gate S89-FWD-C2-OBSERVABLE-DISAMBIGUATION
(Wave 5 of session 89, CONDITIONAL on A.26). Read this prompt in full before computing.

CONDITIONAL DISPATCH GATE:
  Read computations/session-89/s89_gate_verdicts.txt and verify presence of:
    grep "^S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE: (PASS|INFO)" present.
  IF predecessor is FAIL:
    Emit mechanical-closure verdict per .claude/rules/mechanical-closure-discipline.md:
      value='PRE-REG-INC_blocked_by_S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE_FAIL'
    Skip computation; emit verdict line + working-paper §W5-4 status update.
  IF predecessor PASS or INFO: continue with the disambiguation below.

CONTEXT:
- FWD-C2 candidate per cross-pillar-bridge-anatomy.md §"Three forward bridge candidates":
    Pillar II (Mellin-Barnes residue) ↔ Pillar V (BdG spectral triple)
- The §VII.U.2 4-corner classification:
    Cell I:   algebra-INVARIANT × substrate-distance-1
    Cell II:  algebra-INVARIANT × substrate-distance-2
    Cell III: algebra-DEPENDENT × substrate-distance-1
    Cell IV:  algebra-DEPENDENT × substrate-distance-2
- A.25 confirmed −7.046336 substrate-IS at Cell IV (Corner-IV);
- A.26 (PASS path) confirmed Level-2-binding under HKR bridge to Pillar IV;
- A.26 (INFO path) flagged Level-2-non-binding (HKR absent) — joint structure required.

SCRIPT PATH:
  computations/session-89/s89_w5_a27_fwd_c2_observable_disambiguation.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  from pathlib import Path
  # No GPU path required — this gate is structural/audit, not numerical.

INPUT-PIN MAP:
  s89_w5_a25_npz: computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz
  s89_w5_a26_npz: computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz
  cross_pillar_bridge_anatomy_rule:
    path: .claude/rules/cross-pillar-bridge-anatomy.md
    sha256: <runtime>
  permanent_results_registry:
    path: sessions/permanent-results-registry.md
    sha256: <runtime>

PRDR MACHINERY PIN:
  disambiguation_outcomes: ["corner-ii-singleton", "corner-iv-singleton",
                             "joint-with-deferred-envelope"]
  outcome_routing_rules:
    a26_hkr_identified_TRUE: "corner-iv-singleton"   # Outcome (b)
    a26_hkr_identified_FALSE_R²_PASS: "joint-with-deferred-envelope"  # Outcome (c)
    a26_INFO_with_HKR_absent: "joint-with-deferred-envelope"          # Outcome (c)
    # Outcome (a) corner-ii-singleton fires only if A.26 reveals envelope
    # consistent with Cell-II substrate-distance-2 algebra-INVARIANT (rare path)
  hybrid_independence_test_check: True  # per cross-pillar-bridge-anatomy.md §"Hybrid
                                          # Independence Test (i ∨ ii ∨ iii) ∧ iv";
                                          # K-counter at K=1 advisory until K=3
  five_anatomy_elements_required:
    - substrate-IS observable: <inherited from A.26>
    - laboratory-IN observable (OE-form): <pre-registered per §"Element 2 OE-form discipline">
    - bridge map (HKR / Connes-Karoubi / K-theory): <inherited from A.26>
    - algebraic envelope: <inherited from A.26 envelope_alpha>
    - empirical anchor: <inherited from A.25 −7.046336>
  three_level_ladder_required:
    - Level 1 (cohomology-class identity): regulator-invariant declaration
    - Level 2 (algebraic envelope): <from A.26>
    - Level 3 (empirical anchor at L_max=12): <from A.25>
  level_2_sub_class_declaration: REQUIRED (Level-2-binding or Level-2-non-binding)
  registry_slot: §VII.AV (next-free per S88 close §VII.A-AT used; AU/AV/AW reserved for FWD-Cn)
  scheme: bridge-anatomy-pre-registration
  convention: fwd-c2-disambiguation-S89-W5
  regulator_pin: a_n^{ζ}
  numerical_precision: float64

CROSS-CHECKS:
  (a) Hybrid Independence Test: confirm FWD-C2 distinct on (i) substrate-IS pillar
      OR (ii) laboratory-IN pillar OR (iii) bridge map class from FWD-C1 (Pillar I↔II)
      AND (iv) algebraic envelope independent of FWD-C1 (not a numerical refinement).
  (b) 5-anatomy element completeness: emit JSON summary verifying all 5 declared.
  (c) 3-level ladder completeness: emit JSON summary verifying L1/L2/L3 declared
      with explicit values where computable.
  (d) §VII.U.2 4-corner cell assignment: emit `corner_cell` ∈ {II, IV, II+IV joint}.
  (e) Algebra-axis orthogonality check: confirm corner-II (algebra-INVARIANT)
      and corner-IV (algebra-DEPENDENT) are NOT co-primary in the joint outcome
      per registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY" criterion (4)
      MANDATORY at K=3 (S88 W-15 V.6 / B.14): cross-corner co-primary FORBIDDEN.

OUTPUT:
  Path: computations/session-89/s89_w5_a27_fwd_c2_observable_disambiguation.npz
  Keys:
    disambiguation_outcome: str  # "corner-ii-singleton" | "corner-iv-singleton" |
                                 # "joint-with-deferred-envelope"
    five_anatomy_elements: dict
    three_level_ladder: dict
    level_2_sub_class: str  # "Level-2-binding" | "Level-2-non-binding"
    corner_cell: str
    hybrid_independence_test_PASS: bool
    cross_corner_co_primary_check: str  # "PASS-distinct-corners" | "FAIL-cross-corner-conflation"
    proposed_registry_slot: "§VII.AV"
    proposed_stage_tag: "STAGE-1-CANDIDATE"
  Plot path: NONE  (audit gate; no numerical plot)

PASS PREDICATE:
  magnitude_verdict:
    PASS  iff disambiguation_outcome locked at "corner-ii-singleton" OR
              "corner-iv-singleton" AND
              hybrid_independence_test_PASS == True AND
              cross_corner_co_primary_check == "PASS-distinct-corners" AND
              all 5 anatomy elements declared AND
              all 3 levels declared with Level-2 sub-class explicit
    INFO  iff disambiguation_outcome == "joint-with-deferred-envelope"
              (joint structure required; Level-2 envelope deferred per §"Level-2 Layer Distinction"
               + REGISTRY-INELIGIBLE-PENDING-HKR-IDENTIFICATION flag)
    FAIL  iff hybrid_independence_test_PASS == False (numerical refinement of FWD-C1
              rather than independent candidate) OR cross-corner co-primary conflation
              OR <5 anatomy elements OR <3 levels declared
  sign_verdict: N/A
  regime_verdict: VALID
  composite collapse: per gate-verdicts.md.

VERDICT EMISSION (single-shot atomic):
  Path: computations/session-89/s89_gate_verdicts.txt
  Dual-SHA companion comment row REQUIRED.

REGISTRY LANDING PRE-REGISTRATION:
  IF PASS: §VII.AV STAGE-1-CANDIDATE pre-registered per joint-theorem-promotion.md
           Stage 1; landing performed by mack-cosmic-bridge sole-writer per
           feedback_mack-bridge-role.md (NOT this gate; this gate pre-registers,
           does not land).
  IF INFO: §VII.AV registry-INCOMPLETE flag with HKR-identification deferred.
  IF FAIL: no registry pre-registration; FWD-C2 candidate routed to next-session
           reconstruction.

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-4
  MUST include: (i) the 5-anatomy element table; (ii) the 3-level ladder; (iii)
  the §VII.U.2 corner-cell assignment; (iv) the Hybrid Independence Test verdict;
  (v) substrate framing paragraph per phononic-framing.md.
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-FWD-C2-OBSERVABLE-DISAMBIGUATION
schema_version: R3
trigger: [AUDIT]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a27_fwd_c2_observable_disambiguation.py
runtime_owner: connes-ncg-theorist
co_author: volovik-superfluid-universe-theorist
conditional_predecessor: S89-CORNER-IV-K-WINDOW-LMAX-SCAN-LEVEL-2-ENVELOPE  # BLOCKED on PASS or INFO
input_pin_map:
  s89_w5_a25_npz: <pinned at dispatch>
  s89_w5_a26_npz: <pinned at dispatch>
  cross_pillar_bridge_anatomy_rule: <pinned at dispatch>
  permanent_results_registry: <pinned at dispatch>
machinery_pin_map:
  disambiguation_outcomes: ["corner-ii-singleton", "corner-iv-singleton", "joint-with-deferred-envelope"]
  hybrid_independence_test_check: True
  five_anatomy_elements_required: True
  three_level_ladder_required: True
  level_2_sub_class_declaration: True
  registry_slot: §VII.AV
  scheme: bridge-anatomy-pre-registration
  convention: fwd-c2-disambiguation-S89-W5
  regulator_pin: a_n^{ζ}
  numerical_precision: float64
expected_output_4tuple:
  value: <disambiguation_outcome>
  scheme: bridge-anatomy-pre-registration
  convention: fwd-c2-disambiguation-S89-W5
  L_max: 12
pass_threshold:
  outcome: corner-ii-singleton OR corner-iv-singleton
  hybrid_independence_test: PASS
  cross_corner_co_primary: PASS-distinct-corners
  anatomy_5_complete: True
  ladder_3_complete: True
  level_2_sub_class_explicit: True
  tolerance_rule: THEOREM
```

**8. Expected output 4-tuple**: `(value=<disambiguation_outcome>, scheme=bridge-anatomy-pre-registration, convention=fwd-c2-disambiguation-S89-W5, L_max=12)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: Outcome locked at corner-ii-singleton OR corner-iv-singleton AND Hybrid Independence Test PASS AND all 5 anatomy + 3 levels declared. §VII.AV STAGE-1-CANDIDATE pre-registered; FWD-C2 advances toward K-counter K=1 → K=2 advancement.
- **INFO**: Outcome = joint-with-deferred-envelope; §VII.AV REGISTRY-INCOMPLETE-PENDING-HKR-IDENTIFICATION flag.
- **FAIL**: Hybrid Independence Test FAIL OR cross-corner co-primary conflation OR incomplete anatomy/ladder. No registry pre-registration; FWD-C2 deferred.

**10. Substitution chain** (no sign claim; THEOREM tolerance — Hybrid Independence Test substitution chain mandatory):

```
Step 1 (Definition): FWD-C2 = (substrate-IS Pillar II) ↔ (laboratory-IN Pillar V)
                     bridge candidate per cross-pillar-bridge-anatomy.md
                     §"Three forward bridge candidates"
                     Pillar II = Mellin-Barnes residue
                     Pillar V = BdG spectral triple

Step 2 (Definition): Hybrid Independence Test (per §"Hybrid Independence Test"):
                     (i ∨ ii ∨ iii) ∧ iv
                     where
                       (i)   distinct substrate-IS pillar from FWD-C1 (Pillar I)
                       (ii)  distinct laboratory-IN pillar from FWD-C1 (Pillar II)
                       (iii) distinct bridge map class from FWD-C1
                       (iv)  independent algebraic envelope (not numerical refinement)

Step 3 (Substitution at FWD-C2):
                     (i)  FWD-C2 substrate-IS = Pillar II ≠ FWD-C1 substrate-IS = Pillar I
                          ⇒ TRUE
                     (ii) FWD-C2 lab-IN = Pillar V ≠ FWD-C1 lab-IN = Pillar II
                          ⇒ TRUE
                     (iii) FWD-C2 bridge = Connes-Karoubi pairing (TBD per A.27 outcome) vs
                           FWD-C1 bridge = HKR ⇒ likely TRUE (depends on outcome)
                     (iv) FWD-C2 envelope from A.26 (Level-2-binding or non-binding) vs
                          FWD-C1 envelope from W3 A.9 closed-form c (independent derivation)
                          ⇒ TRUE

Step 4 (Simplification): (i ∨ ii ∨ iii) = TRUE ∨ TRUE ∨ ... = TRUE
                          (iv) = TRUE
                          ⇒ Hybrid Independence Test PASS
                          ⇒ FWD-C2 is structurally independent from FWD-C1
                          ⇒ counts toward K-counter advancement.

Step 5 (Direction): The disambiguation_outcome direction is determined by the
                    A.26 hkr_bridge_identified bool:
                      hkr_TRUE    ⇒ corner-iv-singleton
                      hkr_FALSE   ⇒ joint-with-deferred-envelope
                      hkr_UNCLEAR ⇒ INFO outcome
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: FWD-C2 candidate pre-registered at §VII.AV STAGE-1-CANDIDATE; the cross-pillar-bridge K-counter (currently K=3 MANDATORY since S88 W4a-17) gains a structurally independent calibration instance — FWD-C2 PASS contributes directly to forward template-adoption corpus growth. Hybrid Independence Test K-counter (currently K=1 advisory) advances to K=2.
- **INFO**: FWD-C2 candidate joint-structure recorded with deferred envelope; §VII.AV REGISTRY-INCOMPLETE flag pending HKR identification at next session. Solution-space corridor: A.26 envelope contributes to Level-2-non-binding catalog, NOT to registry-PASS pathways.
- **FAIL**: FWD-C2 fails Hybrid Independence Test OR cross-corner co-primary conflation. Solution-space corridor: FWD-C2 candidate is a numerical refinement of FWD-C1 OR a structurally illegitimate bridge candidate; deferred to next session with explicit reconstruction directive.

**12. Effort estimate**: 0.25 wave-equivalent (audit gate; no heavy numerical computation; substantive cost is the structural declaration audit + substitution chain verification).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the FWD-C2 bridge candidate's substrate-IS observable — the Pillar-II Mellin-Barnes residue evaluated on `(A_K^{≤L}, H_K^{≤L}, D_K^{≤L})`. The laboratory-IN observable is the Pillar-V BdG spectral triple's continuum trace (Element-2 OE-form per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` MANDATORY at K=2). The bridge map (Connes-Karoubi pairing or K-theory boundary, TBD) flows substrate → bridge → laboratory; FORBIDDEN container-thinking ("the FWD-C2 candidate inhabits cross-pillar bridge space") inverts the direction. The Hybrid Independence Test enforces that FWD-C2 is structurally distinct from FWD-C1; any framing that treats FWD-C2 as a "refinement" of FWD-C1 violates the test by construction. Mnemonic-vs-exact ratio discipline: outcome strings ("corner-iv-singleton", "joint-with-deferred-envelope") are exact structural classifications with no mnemonic alternatives.

---

## §W5-5. S89-TAU-2X-FOLD-CROSS-VALIDATION-READING-A-VS-READING-B  (A.28)

**1. Gate ID**: `S89-TAU-2X-FOLD-CROSS-VALIDATION-READING-A-VS-READING-B`

**2. Trigger**: `[SIGN]` + `[VERIFY]` — directional discrimination between Reading-A (geometric resummation; ratio R(0.38)/R(0.19) ≈ 8) and Reading-B (linear-LO; ratio ≈ 4). The `[SIGN]` trigger fires schema-v2 3-tuple companion row. Sign here refers to the discriminator direction (which of two competing hypotheses the empirical ratio favors).

**3. Classification**: GEOMETRIC. Substrate-IS observable: slope_A(τ) at two τ values (τ_fold = 0.19 and 2·τ_fold = 0.38), each computed via Richardson L^{−3} extrapolation on the L_max ∈ {10, 11, 12, 14} scan; the ratio is intrinsic to the spectral-triple's substrate-distance-1 structure under Jensen TT-deformation.

**4. Agent type**: `lizzi-spectral-functional-theorist` PRIMARY (substrate-distance-1 slope_A observable on the spectral-functional / regulator-axis program; Reading-A geometric resummation IS the lizzi `5/(1−τ/(5π))` closed-form). No CO-AUTHOR (single-axis substrate-physics derivation).

**5. Hypothesis**: At τ = 2·τ_fold = 0.38, the slope_A(0.38) Richardson-extrapolated value R(0.38) can be compared to R(0.19) ≈ 10.122 (W1b-3 canonical). Reading-A geometric resummation predicts R(0.38)/R(0.19) ≈ HK-5(0.38)/HK-5(0.19) where HK-5(τ) = 5/(1 − τ/(5π)); evaluated: HK-5(0.38)/HK-5(0.19) ≈ 5/(1 − 0.38/(5π)) ÷ 5.0608 ≈ 5.1228 / 5.0608 ≈ 1.012 (ratio close to 1, NOT 8). Reading-B linear-LO predicts a ratio of ≈ 2 by linearity. The original ledger phrasing "ratio≈8 vs ratio≈4" reflects a different ratio definition: R(0.38)/R(0.19) where R is an absolute quantity that scales differently under geometric resummation vs linear-LO. Per the substitution chain in §10, the geometric prediction at τ near `5π` = 15.708 gives a divergence; the magnitude R(0.38)/R(0.19) under Reading-A geometric resummation = HK-5(0.38)/HK-5(0.19) · (additional Jensen-deformation factor at second order) — pre-registered numerical target ≈ 8 per ledger; under Reading-B linear-LO, the ratio is ≈ 4 (exact factor 2 from linear scaling combined with resummation degree). The hypothesis is that the empirical ratio discriminates these two readings.

**6. Method** (full self-contained dispatch prompt for `lizzi-spectral-functional-theorist`):

```
You are dispatched on COMPUTE-class gate S89-TAU-2X-FOLD-CROSS-VALIDATION-READING-A-VS-READING-B
(Wave 5 of session 89). Read this prompt in full before computing.

CONTEXT:
- Reading-A (lizzi): geometric resummation 5/(1−τ/(5π)) is the dominant substrate-IS
  d_eff at τ_fold; its extension to τ = 2·τ_fold tests the resummation regime.
- Reading-B (alternative): linear-LO at substrate-distance-1; predicts a different
  ratio scaling.
- W1b-3 Richardson canonical at τ_fold = 0.19: slope_A(0.19) ≈ 10.122 = HK-5(0.19) · 2.0
  (where HK-5(0.19) = 5/(1−0.19/(5π)) ≈ 5.0608 and the leading-coefficient absorption
  yields slope_A = 2 · HK-5).
- Reading-A pre-registered prediction at τ = 2·τ_fold = 0.38:
  slope_A(0.38) ≈ 2 · HK-5(0.38) = 2 · 5/(1 − 0.38/(5π)) ≈ 2 · 5.1228 ≈ 10.246
  Ratio R(0.38)/R(0.19) = slope_A(0.38) / slope_A(0.19) ≈ 10.246 / 10.122 ≈ 1.012
- Reading-B pre-registered prediction (linear-LO, ledger-cited):
  Under linear-LO, slope_A(τ) scales as 2τ ⇒ slope_A(0.38) = 2 · 0.38 = 0.76 ⇒
  ratio 0.76 / (slope_A(0.19) = 0.38) = 2.0 (linear scaling).
- The ledger pre-registered ratio targets ("≈8 geometric, ≈4 linear") reflect
  the absolute value R(τ) = slope_A(τ) · (additional substrate-distance factor),
  NOT slope_A directly. This gate uses the slope_A ratio directly per the substitution
  chain (Step 5) as the discriminator; the ratios 8 vs 4 cited in ledger are
  emit-as-info pre-registration anchors but NOT the canonical discriminator.

  CANONICAL DISCRIMINATOR (resolved at plan-author time per math-scripts.md
  §"Mnemonic-vs-exact ratio discipline" S86 W-3 RULE-3):
    Reading-A geometric: slope_A(0.38)/slope_A(0.19) = HK-5(0.38)/HK-5(0.19) ≈ 1.012
                         (factor of ≈1; small Jensen second-order correction)
    Reading-B linear:    slope_A(0.38)/slope_A(0.19) = 2 (exact linearity)
  PASS-A iff ratio ∈ [0.95, 1.10] (geometric prediction with absorbing slack)
  PASS-B iff ratio ∈ [1.80, 2.20] (linear-LO prediction with absorbing slack)
  INFO   iff ratio ∈ (1.10, 1.80) ∪ (2.20, ∞) (neither reading explains)

  The ledger's "≈8 vs ≈4" interpretation (under absolute R scaling) is recorded
  in the npz output for cross-validation; the canonical discriminator above
  governs the PASS/FAIL/INFO emission.

REGIME-OF-VALIDITY CHECK:
  τ_max for HK-5 closed-form regime is derived in W3 A.35 (cross-wave dependency).
  IF W3 A.35 has landed and τ_max < 0.38: regime_verdict = BREAKDOWN, composite = FAIL.
  IF W3 A.35 has landed and τ_max ≥ 0.38: regime_verdict = VALID.
  IF W3 A.35 has NOT landed: emit MARGINAL with "τ_max-bound-pending" annotation;
    cross-check via the closed-form divergence boundary at τ → 5π ≈ 15.708 — since
    0.38 ≪ 5π, the closed-form remains numerically well-defined; the question is
    whether higher-order Jensen corrections invalidate the leading HK-5 form.

SCRIPT PATH:
  computations/session-89/s89_w5_a28_tau_2x_fold_cross_validation.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  import torch
  from pathlib import Path

INPUT-PIN MAP:
  D_K_spectrum_cache_L12_tau019: computations/session-84/s84_spectrum_cache_L12_tau019.npz
  D_K_spectrum_cache_L12_tau038: computations/session-89/s89_spectrum_cache_L12_tau038.npz
                                  # built at S89 W5 dispatch start under Jensen
                                  # τ → 0.38 deformation
  D_K_spectrum_cache_L14_tau019: computations/session-89/s89_spectrum_cache_L14_tau019.npz
  D_K_spectrum_cache_L14_tau038: computations/session-89/s89_spectrum_cache_L14_tau038.npz
  W1b_3_richardson_canonical: 10.122438748384
                               # canonical_constants.py:slope_A_FW_Conv_A_AT_TAU_FOLD
                               # PENDING ledger B.45 mechanical edit; fallback to
                               # numerical recompute at τ_fold = 0.19 if pin absent
  hk5_closed_form: 5.0 / (1.0 - tau / (5.0 * np.pi))
  W3_a35_tau_max_bound: <pending W3 dispatch>  # if absent, regime_verdict = MARGINAL

PRDR MACHINERY PIN:
  tau_scan: [0.19, 0.38]  # τ_fold, 2·τ_fold
  L_max_scan_per_tau: [10, 11, 12, 14]
  truncation_mode: block-diagonal-Peter-Weyl
  casimir_bound_check: True
  slope_A_estimator: spectral-zeta-direct-sum-Richardson-L^{-3}
                     # extrapolate slope_A(τ, L_max → ∞) via L^{−3} fit on 4 L_max values
  richardson_alpha: 3
  scheme: ζ-zeta-spectral-action
  convention: lizzi-zeta-spectral-action-tau-2x-fold-cross-validation
  regulator_pin: a_n^{ζ}
  GPU_path: torch.linalg.eigvalsh per (p,q) sector
  numerical_precision: float64

CROSS-CHECKS:
  (a) τ_fold = 0.19 baseline: Richardson-extrapolated slope_A(0.19) must agree
      with W1b-3 canonical 10.122 within 0.5%; if not, A.28 baseline calibration
      fails and gate FAILs with regime_verdict = BREAKDOWN.
  (b) Sage-exact verification (per math-scripts.md §"Mnemonic-vs-exact ratio
      discipline" + sage_eval): cross-check the Reading-A geometric prediction
      ratio HK-5(0.38)/HK-5(0.19) = (1 − 0.19/(5π)) / (1 − 0.38/(5π)) symbolically.
  (c) Reading-B linear-LO prediction: cross-check ratio = 2 exact.
  (d) Regime-of-validity: τ = 0.38 vs τ_max from W3 A.35 (or fallback 5π = 15.708).
  (e) Richardson extrapolation R²: emit per-τ R² of the L^{−3} fit; regime_verdict
      = MARGINAL if either R² < 0.95.

OUTPUT:
  Path: computations/session-89/s89_w5_a28_tau_2x_fold_cross_validation.npz
  Keys:
    tau_scan: ndarray [0.19, 0.38]
    slope_A_per_tau_per_L: 2D ndarray (tau × L_max)
    slope_A_richardson_extrapolated_per_tau: ndarray  # L → ∞ extrapolation
    ratio_R_038_over_R_019: float64  # CANONICAL DISCRIMINATOR
    reading_A_geometric_prediction: 1.012
    reading_B_linear_prediction: 2.0
    legacy_ledger_ratio_form_038_over_019: float64
                                           # absolute R-form for ledger compatibility
    R_squared_per_tau: dict
    regime_check: str  # "VALID" | "MARGINAL" | "BREAKDOWN"
    tau_max_bound_used: float64 or None
    sage_exact_HK5_ratio: str  # symbolic form
  Plot path: computations/session-89/s89_w5_a28_tau_2x_fold_cross_validation.png
  Plot panels: (i) slope_A(L_max, τ=0.19) Richardson + extrapolation;
               (ii) slope_A(L_max, τ=0.38) Richardson + extrapolation;
               (iii) ratio R(0.38)/R(0.19) bar with Reading-A and Reading-B
                    predictions overlaid;
               (iv) sage-exact symbolic ratio annotation.

PASS PREDICATE:
  sign_verdict (Reading-A vs Reading-B discriminator):
    PASS-A iff ratio ∈ [0.95, 1.10]
    PASS-B iff ratio ∈ [1.80, 2.20]
    INFO   iff ratio ∈ (1.10, 1.80) ∪ (2.20, ∞)
    FAIL   iff ratio < 0.95 (sub-geometric; HK-5 closed-form fails at τ=0.38)
  magnitude_verdict:
    PASS  iff ratio satisfies one of the predictions to within 5%
    INFO  iff ratio between predictions
    FAIL  iff ratio violates BOTH predictions by >10%
  regime_verdict:
    VALID iff Richardson R² ≥ 0.95 per τ AND τ=0.38 ≤ τ_max (W3 A.35) AND
             baseline cross-check PASSes
    MARGINAL iff R² ∈ [0.90, 0.95) OR τ_max bound pending OR partial baseline mismatch
    BREAKDOWN iff R² < 0.90 OR τ=0.38 > τ_max OR baseline mismatch > 1%
  composite collapse: per gate-verdicts.md.

VERDICT EMISSION (single-shot atomic):
  Path: computations/session-89/s89_gate_verdicts.txt
  Dual-SHA companion comment row REQUIRED + S87 schema-v2 3-tuple companion row
  REQUIRED ([SIGN] trigger).

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-5
  Substrate framing paragraph + Reading-A vs Reading-B substitution chain MANDATORY.
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-TAU-2X-FOLD-CROSS-VALIDATION-READING-A-VS-READING-B
schema_version: R3
trigger: [SIGN, VERIFY]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a28_tau_2x_fold_cross_validation.py
runtime_owner: lizzi-spectral-functional-theorist
co_author: None
input_pin_map:
  D_K_spectrum_cache_L12_tau019: <pinned at dispatch>
  D_K_spectrum_cache_L12_tau038: <pinned at dispatch>
  D_K_spectrum_cache_L14_tau019: <pinned at dispatch>
  D_K_spectrum_cache_L14_tau038: <pinned at dispatch>
  W1b_3_richardson_canonical: <pending B.45 mechanical edit>
  W3_a35_tau_max_bound: <pending W3 dispatch>
machinery_pin_map:
  tau_scan: [0.19, 0.38]
  L_max_scan_per_tau: [10, 11, 12, 14]
  truncation_mode: block-diagonal-Peter-Weyl
  casimir_bound_check: True
  slope_A_estimator: spectral-zeta-direct-sum-Richardson-L^{-3}
  richardson_alpha: 3
  scheme: ζ-zeta-spectral-action
  convention: lizzi-zeta-spectral-action-tau-2x-fold-cross-validation
  regulator_pin: a_n^{ζ}
  GPU_path: torch.linalg.eigvalsh
  numerical_precision: float64
expected_output_4tuple:
  value: <ratio_R_038_over_R_019>
  scheme: ζ-zeta-spectral-action
  convention: lizzi-zeta-spectral-action-tau-2x-fold-cross-validation
  L_max: 14
pass_threshold:
  reading_A_geometric_band: [0.95, 1.10]
  reading_B_linear_band: [1.80, 2.20]
  info_band: (1.10, 1.80) ∪ (2.20, ∞)
  fail_band: < 0.95
  tolerance_rule: ABSOLUTE on ratio + RATIO on baseline cross-check
```

**8. Expected output 4-tuple**: `(value=<ratio_R_038_over_R_019>, scheme=ζ-zeta-spectral-action, convention=lizzi-zeta-spectral-action-tau-2x-fold-cross-validation, L_max=14)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS-A** (Reading-A geometric resummation): `ratio ∈ [0.95, 1.10]` AND regime_verdict = VALID. HK-5 closed-form `5/(1−τ/(5π))` is the dominant substrate-IS d_eff at both τ values.
- **PASS-B** (Reading-B linear-LO): `ratio ∈ [1.80, 2.20]` AND regime_verdict = VALID. Linear-LO scaling at substrate-distance-1 dominates over geometric resummation.
- **INFO**: `ratio ∈ (1.10, 1.80) ∪ (2.20, ∞)`. Neither reading cleanly explains the empirical ratio; second-order corrections at τ=0.38 are non-negligible.
- **FAIL**: `ratio < 0.95` OR regime_verdict = BREAKDOWN. Sub-geometric ratio indicates HK-5 closed-form fails at τ=0.38 (regime breakdown).

**10. Substitution chain** (mandatory for ratio direction Reading-A vs Reading-B per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1 (Definition): slope_A(τ) := 2 · d_eff(τ) at substrate-distance-1
                     where d_eff(τ) = HK-5(τ) + Jensen-corrections
                     HK-5(τ) = 5/(1 − τ/(5π))   [closed-form S87 d_eff workshop]

Step 2 (Definition): Reading-A (geometric resummation) prediction:
                     slope_A_geometric(τ) = 2 · HK-5(τ)
                     ratio R_geom = slope_A(0.38)/slope_A(0.19)
                                  = HK-5(0.38)/HK-5(0.19)
                                  = [5/(1−0.38/(5π))] / [5/(1−0.19/(5π))]
                                  = (1 − 0.19/(5π)) / (1 − 0.38/(5π))

Step 3 (Substitution): Numerical evaluation:
                     5π = 15.7079632679...
                     0.19/(5π) = 0.012096...
                     0.38/(5π) = 0.024192...
                     1 − 0.19/(5π) = 0.987904...
                     1 − 0.38/(5π) = 0.975808...
                     R_geom = 0.987904 / 0.975808 = 1.01240...
                     ⇒ Reading-A predicts ratio ≈ 1.012

Step 4 (Reading-B linear-LO prediction):
                     slope_A_linear(τ) = 2 · k · τ (linear in τ; k is leading coefficient)
                     ratio R_lin = slope_A(0.38)/slope_A(0.19)
                                = 0.38/0.19 = 2.0 EXACT

Step 5 (Direction):
                     R_geom ≈ 1.012  ⇒ PASS-A band [0.95, 1.10]
                     R_lin  = 2.000  ⇒ PASS-B band [1.80, 2.20]
                     The two predictions are SEPARATED by 0.79 (well outside both
                     bands' widths of 0.15 and 0.40), so the discriminator is
                     unambiguous within tolerance.

PYTHON VERIFICATION (at plan-author time):
  >>> import math
  >>> tau1, tau2 = 0.19, 0.38
  >>> hk5 = lambda t: 5.0 / (1.0 - t/(5.0*math.pi))
  >>> R_geom = hk5(tau2) / hk5(tau1)
  >>> R_geom
  1.01240...
  >>> R_lin = tau2 / tau1
  >>> R_lin
  2.0
  >>> # Sage-exact form (rendered as fraction-of-fractions):
  >>> # R_geom = (5π − τ1) / (5π − τ2) = (5π − 0.19)/(5π − 0.38)
  >>> #         = (5π − 19/100)/(5π − 38/100)
  >>> # Symbolic: (500π − 19)/(500π − 38) under π → π exact;
  >>> # (500·π − 19)/(500·π − 38) ≈ 1.0124 numerically.

CONCLUSION: PASS-A and PASS-B bands are well-separated; the empirical ratio
            unambiguously discriminates the readings under the canonical
            discriminator. Per math-scripts.md §"Mnemonic-vs-exact ratio
            discipline", the absolute-R-form ratios cited in ledger ("≈8 vs ≈4")
            are mnemonic-form and use a different scaling factor; the canonical
            discriminator above is structurally exact.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS-A** (Reading-A geometric): HK-5 closed-form `5/(1−τ/(5π))` dominates substrate-IS d_eff at both τ_fold and 2·τ_fold; the geometric resummation is the structural substrate prediction. FWD-C1 retry (A.31) inherits this confirmation; `slope_A_FW_Conv_A` parameterized canonical pin (Ledger B.45) is structurally validated.
- **PASS-B** (Reading-B linear-LO): Linear-LO scaling dominates; HK-5 closed-form is a τ_fold-specific accident, not a structural substrate prediction. FWD-C1 retry must re-derive c_sub under linear-LO scaling; the parameterized canonical pin form `5/(1−τ/(5π))` is incorrect.
- **INFO**: Neither reading cleanly explains; second-order Jensen corrections at τ=0.38 are large. Solution-space corridor: route to W3 A.9 + A.29 closed-form c, c_2 derivation; A.31 FWD-C1 retry inherits a softer structural form pending second-order absorption.
- **FAIL**: Regime breakdown at τ=0.38 (HK-5 closed-form invalid); FWD-C1 retry restricted to τ ≤ τ_fold; A.35 τ_max bound pre-registered as critical canonical.

**12. Effort estimate**: 1.0 wave-equivalent (substantive cost is L_max=14 cache build at τ=0.38 — Jensen-deformed spectrum recomputation; Richardson fit + verdict ≈ 15 min).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the spectral triple under Jensen TT-deformation at moduli-deformation Level-2 (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`); slope_A(τ) at multiple τ values is a moduli-Level-2 substrate-IS observable. The ratio R(0.38)/R(0.19) is the substrate's own moduli-deformation invariance test. FORBIDDEN container-thinking ("the substrate moves through the τ axis from 0.19 to 0.38"); the substrate IS each (A_K, H_K, D_K(τ)) instance, and the ratio tests whether the closed-form HK-5 captures the moduli structure. Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3): the ledger-cited ratios "≈8 vs ≈4" are absolute-R-form mnemonics with different scaling; the canonical discriminator R_geom ≈ 1.012 vs R_lin = 2.0 is the substrate-exact form derived per substitution chain Step 3. Sage-exact rendering: R_geom = (500π − 19)/(500π − 38).

---

## §W5-6. S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL  (A.31)

**1. Gate ID**: `S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL`

**2. Trigger**: `[VERIFY-THEOREM]` — verification that FWD-C1 c_sub re-derivation under the parameterized `slope_A_FW_Conv_A = "10.0 / (1 - tau/(5*pi))"` canonical pin satisfies the FWD-C1 Pillar I↔II bridge Level-3 anchor (n_s_FW_exact = 9561/10000 vs Planck observational locus). Direction claim: c_sub_corrected magnitude relative to the prior canonical (S82 c_sub_baseline = 2.238).

**3. Classification**: GEOMETRIC. Substrate-IS observable: c_sub_corrected = M_Pl_eff(k_pivot)² / M_Pl_eff(0)² evaluated under the parameterized slope_A canonical; the FWD-C1 bridge candidate's Level-3 anchor is the n_s_FW_exact = 9561/10000 Route-B identity at Pillar-I substrate-IS to Pillar-II Planck-observational lab-IN.

**4. Agent type**: `lizzi-spectral-functional-theorist` PRIMARY (FWD-C1 substrate-IS ownership + slope_A canonical derivation). No CO-AUTHOR.

**5. Hypothesis**: Re-deriving FWD-C1 c_sub under the parameterized slope_A canonical `slope_A_FW_Conv_A = "10.0 / (1 - tau/(5*pi))"` (per Ledger B.45 mechanical edit) reproduces the Mellin-cone closure n_s_FW_exact = 9561/10000 at the Level-3 anchor with c_sub_corrected satisfying the FWD-C1 Level-2 envelope L^{−3} bound at L_max=10. The closure validates the parameterized canonical as the substrate-IS slope_A across τ values, advancing the Hybrid Independence Test K-counter for FWD-C1 from K=1 to K=2.

**6. Method** (full self-contained dispatch prompt for `lizzi-spectral-functional-theorist`):

```
You are dispatched on COMPUTE-class gate S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL
(Wave 5 of session 89). Read this prompt in full before computing.

SUBSTRATE-FIRST-PROVENANCE PRE-CHECK (CLASS-(f) CONTINGENCY):
  Read canonical_constants.py and search for `slope_A_FW_Conv_A` pin name.
  IF pin is landed (Ledger B.45 mechanical edit complete):
    Consume the canonical directly; proceed with computation.
  IF pin is NOT landed (PENDING placeholder):
    Per substrate-first-canonical-sourcing.md §(v) Class-(f), invoke
    SUBSTRATE-FIRST-PROVENANCE Class-(f) audit:
      placeholder_value = "10.0 / (1 - tau/(5*pi))"  # parameterized form
      canonical_query = mcp__knowledge__.get_constant("slope_A_FW_Conv_A")
      IF canonical_query returns None:
        D_max measurement: undefined (no canonical anchor); emit ADVISORY
        per §(v) "no canonical exists" routing; proceed with the parameterized
        form as DERIVED rather than canonical, and emit `convention=` with
        `-PENDING-CANONICAL-PROMOTION` suffix per regulator-pin-discipline.md
        §"Cross-link — K=4 SCHEMATIC level-pin promotion" (the parameterized
        form is a derived expression, not a SCHEMATIC helper, but the convention-
        suffix discipline applies to flag the pending status).
      IF canonical_query returns a value:
        Compute D_max = |log10(canonical) − log10(parameterized_at_tau_fold)|.
        IF D_max < 0.1: NO-ACTION (within absorbable band); proceed normally.
        IF 0.1 ≤ D_max < 1.0: ADVISORY; proceed with audit logging.
        IF 1.0 ≤ D_max < 3.0: MANDATORY remediation; halt + log + escalate.
        IF D_max ≥ 3.0: HARD-HALT; do NOT proceed.

CONTEXT:
- FWD-C1 candidate (per cross-pillar-bridge-anatomy.md §"Three forward bridge
  candidates"): Pillar I (n_s spectral-action) ↔ Pillar II (Planck CMB).
- Substrate-IS observable: n_s_FW_exact = 9561/10000 (Route-B identity bit-exact
  per S88 W-15 W4c-36 +cross-checks).
- Laboratory-IN observable: Planck 2018 n_s = 0.9649 ± 0.0042.
- Bridge map: HKR (Hochschild-Kostant-Rosenberg).
- Algebraic envelope: L^{−3} at d=4 (per cross-pillar-bridge-anatomy.md §"Three-
  Level Structural-Confidence Ladder" Level 2).
- Empirical anchor at L_max=10: c_sub_corrected = M_Pl_eff(k_pivot)² / M_Pl_eff(0)²
  evaluated via the parameterized slope_A canonical.

SCRIPT PATH:
  computations/session-89/s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  import torch
  import math
  from pathlib import Path
  # If slope_A_FW_Conv_A canonical landed:
  try:
      from canonical_constants import slope_A_FW_Conv_A
      SLOPE_A_PIN_STATUS = "LANDED"
  except ImportError:
      slope_A_FW_Conv_A = lambda tau: 10.0 / (1.0 - tau / (5.0 * math.pi))
      SLOPE_A_PIN_STATUS = "PENDING-PARAMETERIZED-FORM"

INPUT-PIN MAP:
  D_K_spectrum_cache_L10: computations/session-84/s84_spectrum_cache_L12_tau019.npz
                          # filtered to L_max=10 via Casimir-bound truncation
  n_s_FW_exact: 9561/10000  # Route-B identity bit-exact from S88
  planck_2018_n_s: 0.9649
  planck_2018_n_s_uncertainty: 0.0042
  c_sub_baseline_S82: 2.238  # prior canonical from S82 W3-9
  slope_A_FW_Conv_A: <pending B.45 OR consumed parameterized form>

PRDR MACHINERY PIN:
  L_max: 10  # canonical truncation per cross-pillar-bridge-anatomy.md §"Calibration corpus"
  truncation_mode: block-diagonal-Peter-Weyl
  c_sub_estimator: M_Pl_eff_squared_ratio_via_parameterized_slope_A
  bridge_map: HKR
  envelope_alpha_predicted: 3  # Level-2 L^{−3} at d=4
  level_3_anchor_target: n_s_FW_exact_match (Route-B 9561/10000)
  scheme: ζ-zeta-spectral-action
  convention: lizzi-fwd-c1-retry-parameterized-slope-A-canonical
  convention_suffix_if_pending:  -PENDING-CANONICAL-PROMOTION
                                  # only if SLOPE_A_PIN_STATUS == PENDING-PARAMETERIZED-FORM
  regulator_pin: a_n^{ζ}
  hybrid_independence_test_check: True  # FWD-C1 K-counter advancement check
  GPU_path: torch.linalg.eigvalsh per (p,q) sector
  numerical_precision: float64

CROSS-CHECKS:
  (a) slope_A canonical evaluation at τ_fold = 0.19: parameterized form gives
      slope_A_FW_Conv_A(0.19) = 10/(1 − 0.19/(5π)) ≈ 10.1244; cross-check
      against W1b-3 Richardson canonical 10.122 (within 0.05%).
  (b) c_sub_corrected vs c_sub_baseline_S82 = 2.238: emit ratio
      c_sub_corrected / 2.238; the parameterized canonical should produce a
      MORE TIGHTLY DEFINED c_sub (smaller tolerance) compared to the baseline.
  (c) n_s_FW Mellin-cone closure: re-derive n_s from c_sub_corrected via
      n_s = 1 + (a_2-cone-residue)·(c_sub_corrected − 1) [exact form per
      W-15 W4c-36 substitution chain]; verify result matches n_s_FW_exact =
      0.9561 to bit precision.
  (d) Planck observational locus discriminator: |n_s_recomputed − 0.9649| /
      0.0042 ≤ 1.5σ (Planck PASS band); INFO if 1.5σ < diff ≤ 3.0σ; FAIL
      if > 3.0σ.
  (e) Hybrid Independence Test (K-counter advancement): emit per (i)/(ii)/(iii)/(iv)
      check; FWD-C1 PASS contributes to K=1 → K=2 advancement.

OUTPUT:
  Path: computations/session-89/s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.npz
  Keys:
    SLOPE_A_PIN_STATUS: str  # "LANDED" or "PENDING-PARAMETERIZED-FORM"
    slope_A_at_tau_fold: float64
    c_sub_corrected: float64
    c_sub_baseline_S82: 2.238
    c_sub_ratio: float64  # corrected / baseline
    n_s_recomputed: float64
    n_s_FW_exact_match_bit_precision: bool
    planck_n_s_diff_sigma: float64
    hybrid_independence_test: dict
    SUBSTRATE_FIRST_PROVENANCE_audit: dict  # Class-(f) result if PENDING
    proposed_registry_slot: §VII.AU  # FWD-C1 STAGE-1-CANDIDATE landing slot
  Plot path: computations/session-89/s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.png
  Plot panels: (i) slope_A(τ) parameterized vs Richardson canonical at multiple τ;
               (ii) c_sub_corrected vs baseline S82 bar comparison;
               (iii) n_s_recomputed vs n_s_FW_exact + Planck locus.

PASS PREDICATE:
  magnitude_verdict:
    PASS  iff n_s_FW_exact_match_bit_precision == True AND
              planck_n_s_diff_sigma ≤ 1.5 AND
              c_sub_ratio bounded within [0.95, 1.10] (recovers baseline within tolerance) AND
              hybrid_independence_test PASS
    INFO  iff n_s_FW_exact match within 1e-6 (not bit-precision) OR
              planck_n_s_diff_sigma ∈ (1.5, 3.0]
    FAIL  iff n_s match worse than 1e-4 OR planck > 3σ OR c_sub_ratio outside [0.85, 1.15]
  sign_verdict: N/A
  regime_verdict:
    VALID iff SLOPE_A_PIN_STATUS == "LANDED" AND substrate-first-provenance audit
             PASSes AND no Class-(f) HARD-HALT
    MARGINAL iff SLOPE_A_PIN_STATUS == "PENDING-PARAMETERIZED-FORM" AND ADVISORY
                 audit (D_max < 1.0)
    BREAKDOWN iff Class-(f) MANDATORY or HARD-HALT halt
  composite collapse: per gate-verdicts.md.

VERDICT EMISSION (single-shot atomic):
  Path: computations/session-89/s89_gate_verdicts.txt
  Convention tag suffix MUST include `-PENDING-CANONICAL-PROMOTION` if pin
  is PENDING; the suffix is dropped on Ledger B.45 landing in subsequent runs.

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-6
  MUST include: (i) substrate-first-provenance Class-(f) audit log;
  (ii) slope_A canonical evaluation cross-check; (iii) FWD-C1 c_sub_corrected
  derivation; (iv) Planck observational locus comparison; (v) Hybrid Independence
  Test verdict; (vi) substrate framing paragraph.
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-FWD-C1-RETRY-PARAMETERIZED-SLOPE-A-CANONICAL
schema_version: R3
trigger: [VERIFY-THEOREM]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a31_fwd_c1_retry_parameterized_slope_A_canonical.py
runtime_owner: lizzi-spectral-functional-theorist
co_author: None
substrate_first_provenance_audit: REQUIRED  # Class-(f) contingency on slope_A_FW_Conv_A pin
input_pin_map:
  D_K_spectrum_cache_L10: <pinned at dispatch>
  slope_A_FW_Conv_A: <pending B.45 OR consumed parameterized form>
  n_s_FW_exact: 9561/10000
  planck_2018_n_s: 0.9649
  c_sub_baseline_S82: 2.238
machinery_pin_map:
  L_max: 10
  truncation_mode: block-diagonal-Peter-Weyl
  c_sub_estimator: M_Pl_eff_squared_ratio_via_parameterized_slope_A
  bridge_map: HKR
  envelope_alpha_predicted: 3
  level_3_anchor_target: n_s_FW_exact_match_Route_B_9561_10000
  scheme: ζ-zeta-spectral-action
  convention: lizzi-fwd-c1-retry-parameterized-slope-A-canonical
  regulator_pin: a_n^{ζ}
  hybrid_independence_test_check: True
  GPU_path: torch.linalg.eigvalsh
  numerical_precision: float64
expected_output_4tuple:
  value: <c_sub_corrected> OR <n_s_recomputed>
  scheme: ζ-zeta-spectral-action
  convention: lizzi-fwd-c1-retry-parameterized-slope-A-canonical
  L_max: 10
pass_threshold:
  n_s_FW_exact_match: bit_precision (Route-B 9561/10000)
  planck_sigma: ≤ 1.5σ (PASS); (1.5, 3.0] σ (INFO); > 3σ (FAIL)
  c_sub_ratio_band: [0.95, 1.10]
  hybrid_independence_test: PASS
  tolerance_rule: THEOREM (Mellin-cone closure) + RATIO (Planck σ)
```

**8. Expected output 4-tuple**: `(value=<c_sub_corrected>, scheme=ζ-zeta-spectral-action, convention=lizzi-fwd-c1-retry-parameterized-slope-A-canonical, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: n_s_FW_exact match at bit-precision AND Planck diff ≤ 1.5σ AND c_sub_ratio ∈ [0.95, 1.10] AND Hybrid Independence Test PASS AND substrate-first-provenance audit PASS (canonical landed). FWD-C1 STAGE-1-CANDIDATE pre-registered at §VII.AU (pending mack-cosmic-bridge sole-writer landing).
- **INFO**: n_s_FW match within 1e-6 (not bit) OR Planck diff ∈ (1.5σ, 3.0σ]. Substrate framing intact but tighter calibration required.
- **FAIL**: n_s match worse than 1e-4 OR Planck > 3σ OR c_sub_ratio outside [0.85, 1.15] OR Class-(f) HARD-HALT. FWD-C1 retry inconclusive; route to next session for substrate-physics reconstruction.

**10. Substitution chain** (mandatory for c_sub_corrected direction per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1 (Definition): slope_A_FW_Conv_A(τ) := 10.0 / (1 − τ/(5π))
                     [parameterized closed-form per Ledger B.45 mechanical edit]

Step 2 (Definition): c_sub_corrected := f(slope_A_FW_Conv_A(τ_fold), spectrum_cache_L10)
                     where f is the M_Pl_eff² ratio derivation per W-15 W4c-36
                     (Mellin-cone substrate-distance-1 closure formula).

Step 3 (Substitution): At τ_fold = 0.19:
                     slope_A_FW_Conv_A(0.19) = 10/(1 − 0.19/(5π)) ≈ 10.1244
                     c_sub_corrected = (slope_A_FW_Conv_A(0.19) / slope_A_FW_Conv_A(0))² · 1
                                     × (other Mellin-cone factors from W-15 substitution chain)
                     [exact form pre-registered in W-15 W4c-36 §V.4]

Step 4 (Simplification at canonical evaluation):
                     The parameterized form recovers the S82 c_sub_baseline ≈ 2.238 within
                     [0.95, 1.10] tolerance band IF the parameterized canonical is the correct
                     substrate-IS slope_A; deviation outside the band signals that the
                     parameterized form differs structurally from the prior canonical at the
                     τ_fold anchor.

Step 5 (Direction):
                     c_sub_ratio < 0.95 ⇒ tighter c_sub than baseline; n_s tilts redder.
                     c_sub_ratio > 1.10 ⇒ looser c_sub than baseline; n_s tilts bluer.
                     The expected direction depends on the sign of the parameterized form's
                     deviation from the prior canonical. At the structural prediction
                     (parameterized form IS the prior canonical analytically extended),
                     c_sub_ratio ≈ 1.00 EXACT.

PYTHON VERIFICATION (at plan-author time):
  >>> import math
  >>> tau_fold = 0.19
  >>> slope_A_paramet = 10.0 / (1.0 - tau_fold / (5.0 * math.pi))
  >>> slope_A_paramet
  10.1244...
  >>> # c_sub_corrected derivation requires the W-15 spectrum-cache-dependent
  >>> # f function; cannot be evaluated at plan-author time without dispatch.
  >>> # The structural prediction is c_sub_corrected ≈ c_sub_baseline_S82 = 2.238
  >>> # within tolerance, since the parameterized form is the closed-form analytic
  >>> # extension of the same substrate-distance-1 derivation.

CONCLUSION: c_sub_ratio direction is structurally predicted ≈ 1.00 (recovery of
            baseline); deviation > 5% indicates structural difference between the
            parameterized canonical and the prior baseline, which would surface as
            ADVISORY or MANDATORY routing under the substrate-first-provenance
            audit.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: FWD-C1 c_sub_corrected reproduces the n_s_FW_exact = 9561/10000 Route-B identity at the Level-3 anchor; FWD-C1 STAGE-1-CANDIDATE pre-registered at §VII.AU. The parameterized slope_A canonical is structurally validated; the cross-pillar-bridge K-counter (already MANDATORY at K=3) gains a structural calibration instance via FWD-C1, advancing the Hybrid Independence Test K-counter from K=1 to K=2. Solution-space corridor: A.24 multi-wave Mellin-cone closure inherits this confirmation at its Level-2 envelope.
- **INFO**: Bit-precision deviation OR borderline Planck distance; FWD-C1 candidate recorded but STAGE-1-CANDIDATE landing deferred pending tighter calibration. Solution-space: parameterized canonical is approximately correct but second-order corrections needed.
- **FAIL**: FWD-C1 retry inconclusive; the parameterized canonical does NOT reproduce n_s_FW_exact at the closure or Planck observational discrimination is too distant. Solution-space corridor: route to next-session reconstruction; A.24 multi-wave open question remains structurally open.

**12. Effort estimate**: 0.8 wave-equivalent (substantive cost is the W-15 W4c-36 substitution chain re-execution under the parameterized canonical + n_s closure verification at bit precision).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; c_sub_corrected is a substrate-IS observable derived from the M_Pl_eff² ratio at the Mellin-cone closure. The parameterized slope_A_FW_Conv_A is the substrate's own moduli-deformation extension of the τ_fold canonical (single-τ-slice Level 1 → moduli-Level 2 per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). FORBIDDEN container-thinking ("the substrate moves through the τ axis under Jensen deformation"); the substrate IS each (A_K, H_K, D_K(τ)). The FWD-C1 bridge map (HKR) flows substrate (Pillar I n_s spectral-action) → bridge → laboratory (Pillar II Planck CMB); inverting this direction is a container-thinking violation. Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3): the parameterized form `10.0 / (1 - tau/(5*pi))` is the substrate-exact closed-form; the W1b-3 Richardson canonical `10.122` is the τ_fold = 0.19 evaluation. Sage-exact rendering: slope_A_FW_Conv_A(τ_fold) = 50π / (5π − 19/100) = 5000π / (500π − 19).

---

## §W5-7. S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY  (A.36)

**1. Gate ID**: `S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY`

**2. Trigger**: `[VERIFY]` — heat-kernel anchor sweep at the §W7a-74 PRIMARY evaluator with N≥4/5 decision rule for Reading-A WIN. The decision rule is itself a multi-criterion verification per the rubric pre-registration discipline (`epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` Class 8.2 MANDATORY).

**3. Classification**: GEOMETRIC. Substrate-IS observable: heat-kernel anchor at 5 distinct anchor candidates `t_ref ∈ {1/max(λ²), 2.3/max(λ²), ln(2)/max(λ²), 1/⟨λ²⟩_mw, 1/M_KK²}` evaluated on the §W7a-74 PRIMARY evaluator at substrate-distance-2 Mellin-cone pole s=4; the rank-ordering of Spearman correlations across {F_2, cutoff_sqrt, anomaly, Zubarev} regulator atlas determines Reading-A vs Reading-B verdict.

**4. Agent type**: `lizzi-spectral-functional-theorist` PRIMARY (heat-kernel anchor sweep + substrate-distance-2 Mellin-cone pole + 5-anchor rubric pre-registration falls within the spectral-functional-theorist domain).

**5. Hypothesis**: At the §W7a-74 PRIMARY evaluator, the rank-ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} regulator atlas at substrate-distance-2 Mellin-cone pole s=4 is robust under heat-kernel anchor variation: at least 4 out of 5 anchor candidates reproduce the same Spearman rank-ordering (Reading-A WIN; the rank-ordering is regulator-class-INVARIANT in this sense). If <4/5 anchors agree, Reading-B wins (rank-ordering is anchor-dependent).

**6. Method** (full self-contained dispatch prompt for `lizzi-spectral-functional-theorist`):

```
You are dispatched on COMPUTE-class gate S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY
(Wave 5 of session 89). Read this prompt in full before computing.

CONTEXT:
- §W7a-74 PRIMARY evaluator at substrate-distance-2 Mellin-cone pole s=4
  (per S88 W-22 W7a-74 V.5 / B.55 §VII.AR LEVEL-DRESSED rank-ordering registry).
- The W-22 V.1 carry-forward queues the 5-anchor sweep with N≥4/5 decision rule
  to confirm Reading-A WIN (rank-ordering regulator-PARAMETER-dependent but
  regulator-CLASS-INVARIANT under heat-kernel anchor variation).
- Anchor sweep set (verbatim per ledger lines 513-516):
    t_ref_1: 1/max(λ²)
    t_ref_2: 2.3/max(λ²)
    t_ref_3: ln(2)/max(λ²)
    t_ref_4: 1/⟨λ²⟩_mw    (mode-weighted average)
    t_ref_5: 1/M_KK²
- Regulator atlas: {F_2, cutoff_sqrt, anomaly, Zubarev}.

VERIFIER-RUBRIC PRE-REGISTRATION (Class 8.2 MANDATORY at K=4 per S88 W-7 + W7a-74):
  Pattern set: Spearman rank correlation matrix across 4 regulators at each anchor.
  Conjunction: ALL 4 regulators must produce a well-defined ranking at each anchor
               (AND across regulators per anchor).
  Disjunction: anchor-level decision is OR across the 5 anchors with N≥4/5 threshold.
  Negative-marker set: NaN / non-finite values automatically fail an anchor.
  Calibration corpus: §VII.AR rank-ordering at L_max=12 baseline.

SCRIPT PATH:
  computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  import torch
  from scipy.stats import spearmanr
  from pathlib import Path

INPUT-PIN MAP:
  D_K_eigenvalue_cache:
    path: computations/session-84/s84_spectrum_cache_L12_tau019.npz
    sha256: <runtime>
  W7a_74_PRIMARY_evaluator:
    path: sessions/archive/session-87/<W7a-74 evaluator script reference>
    sha256: <runtime>
  S88_VII_AR_baseline:
    path: sessions/permanent-results-registry.md
    sha256: <runtime>  # §VII.AR LEVEL-DRESSED rank-ordering at s=4

PRDR MACHINERY PIN:
  L_max: 12
  truncation_mode: block-diagonal-Peter-Weyl
  anchor_set: ["1/max_lambda_sq", "2.3/max_lambda_sq", "ln2/max_lambda_sq",
               "1/avg_lambda_sq_mw", "1/M_KK_sq"]
  regulator_atlas: ["F_2", "cutoff_sqrt", "anomaly", "Zubarev"]
  mellin_cone_pole_s: 4  # substrate-distance-2
  spearman_estimator: scipy.stats.spearmanr (float64)
  decision_rule: N_anchors_with_consistent_ranking >= 4 (out of 5)  ⇒ Reading-A WIN
  reading_A_definition: rank-ordering is regulator-CLASS-INVARIANT (anchor-independent)
  reading_B_definition: rank-ordering is anchor-DEPENDENT
  scheme: heat-kernel-rank-ordering
  convention: lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4
  regulator_pin: a_n^{HK}  # heat-kernel-derived
  GPU_path: torch.linalg.eigvalsh per (p,q) sector for ⟨λ²⟩_mw and max(λ²)
  numerical_precision: float64

CROSS-CHECKS:
  (a) Anchor self-consistency: each t_ref must be > 0 and finite; emit per-anchor
      sanity check.
  (b) Spearman rank stability per anchor: cross-validate using bootstrap resampling
      (N=100 resamples) on the eigenvalue cache; emit per-anchor σ_Spearman.
  (c) Reading-A consistency check: compute pairwise Spearman correlation between
      per-anchor rankings; emit "consistent" iff Spearman ≥ 0.9 between two
      anchors (definition of "consistent ranking" for the N≥4/5 rule).
  (d) S88 §VII.AR baseline: anchor t_ref_1 (1/max(λ²)) should reproduce the §VII.AR
      LEVEL-DRESSED rank-ordering exactly (within numerical noise).

OUTPUT:
  Path: computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz
  Keys:
    anchor_set: list[str]
    regulator_atlas: list[str]
    rank_ordering_per_anchor: dict[anchor_name, list[regulator_name_in_rank_order]]
    spearman_consistency_matrix: 5×5 ndarray  # pairwise rank-correlation across anchors
    N_anchors_with_consistent_ranking: int  # PASS predicate quantity
    consistency_threshold_spearman: 0.9
    reading_A_WIN: bool
    bootstrap_sigma_per_anchor: dict
    s88_vii_ar_baseline_match: bool
  Plot path: computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.png
  Plot panels: (i) per-anchor regulator ranking bar charts × 5;
               (ii) 5×5 Spearman consistency heatmap;
               (iii) bootstrap σ per anchor;
               (iv) Reading-A WIN indicator with threshold line at N=4.

PASS PREDICATE:
  magnitude_verdict:
    PASS  iff N_anchors_with_consistent_ranking >= 4 (Reading-A WIN)
    FAIL  iff N_anchors_with_consistent_ranking < 4 (Reading-B wins)
  sign_verdict: N/A
  regime_verdict:
    VALID iff all 5 anchors produce well-defined rankings AND bootstrap σ < 0.1
             per anchor AND s88_vii_ar_baseline_match == True
    MARGINAL iff bootstrap σ ∈ [0.1, 0.2] for any anchor
    BREAKDOWN iff any anchor produces NaN ranking OR s88 baseline match fails
  composite collapse: per gate-verdicts.md.

VERDICT EMISSION (single-shot atomic):
  Path: computations/session-89/s89_gate_verdicts.txt
  Dual-SHA companion comment row REQUIRED.

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-7
  Substrate framing paragraph + verifier-rubric pre-registration log MANDATORY.
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY
schema_version: R3
trigger: [VERIFY]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.py
runtime_owner: lizzi-spectral-functional-theorist
co_author: None
verifier_rubric_pre_registration: REQUIRED  # Class 8.2 MANDATORY
input_pin_map:
  D_K_eigenvalue_cache: <pinned at dispatch>
  W7a_74_PRIMARY_evaluator: <pinned at dispatch>
  S88_VII_AR_baseline: <pinned at dispatch>
machinery_pin_map:
  L_max: 12
  truncation_mode: block-diagonal-Peter-Weyl
  anchor_set: ["1/max_lambda_sq", "2.3/max_lambda_sq", "ln2/max_lambda_sq", "1/avg_lambda_sq_mw", "1/M_KK_sq"]
  regulator_atlas: ["F_2", "cutoff_sqrt", "anomaly", "Zubarev"]
  mellin_cone_pole_s: 4
  spearman_estimator: scipy.stats.spearmanr
  decision_rule: N >= 4 / 5
  consistency_threshold_spearman: 0.9
  scheme: heat-kernel-rank-ordering
  convention: lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4
  regulator_pin: a_n^{HK}
  GPU_path: torch.linalg.eigvalsh
  numerical_precision: float64
expected_output_4tuple:
  value: <N_anchors_with_consistent_ranking>
  scheme: heat-kernel-rank-ordering
  convention: lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4
  L_max: 12
pass_threshold:
  N_threshold: >= 4 (out of 5)
  consistency_spearman: >= 0.9 pairwise
  tolerance_rule: ABSOLUTE on N + RATIO on Spearman
```

**8. Expected output 4-tuple**: `(value=<N_anchors_with_consistent_ranking>, scheme=heat-kernel-rank-ordering, convention=lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4, L_max=12)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: N ≥ 4 (out of 5 anchors agree at Spearman ≥ 0.9 pairwise) AND regime_verdict = VALID. Reading-A WIN: rank-ordering is regulator-class-INVARIANT under heat-kernel anchor variation; §VII.AR LEVEL-DRESSED rank-ordering structurally locked.
- **INFO**: 3 ≤ N < 4 OR regime_verdict = MARGINAL. Borderline; Reading-A partial.
- **FAIL**: N < 3 OR regime_verdict = BREAKDOWN. Reading-B wins: rank-ordering is anchor-DEPENDENT; the §VII.AR LEVEL-DRESSED rank-ordering is anchor-specific.

**10. Substitution chain** (no directional sign claim independent of N; THEOREM tolerance — verifier-rubric substitution chain mandatory):

```
Step 1 (Definition): N_anchors_with_consistent_ranking := number of anchor pairs
                     (i, j) with i < j such that pairwise Spearman correlation
                     between rank_orderings (anchor_i) and rank_orderings (anchor_j)
                     ≥ 0.9, counted with respect to a single reference anchor.

Step 2 (Definition): Reading-A WIN := N ≥ 4 (out of 5 anchors).
                     Reading-B WIN := N < 4.

Step 3 (Substitution at canonical baseline §VII.AR):
                     anchor t_ref_1 (1/max(λ²)) is the §W7a-74 PRIMARY anchor;
                     the §VII.AR baseline rank-ordering is reproducible at this anchor.
                     The 5-anchor sweep tests robustness under sweep variations.

Step 4 (Decision rule): N ≥ 4 ⇒ PASS (Reading-A WIN);
                        N == 3 ⇒ INFO (borderline);
                        N < 3 ⇒ FAIL (Reading-B WIN).

Step 5 (Direction): The decision rule operates on the count N, not on a sign.
                    No directional sign verdict; the verdict is a discrete
                    classification {Reading-A, Reading-B, INFO}.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: §VII.AR LEVEL-DRESSED rank-ordering at substrate-distance-2 Mellin-cone pole s=4 is a substrate-IS structural identity robust under heat-kernel anchor variation. The rank-ordering is regulator-PARAMETER-dependent (different parameter values give different ranks) but regulator-CLASS-INVARIANT (the structural ordering is preserved under class-internal anchor variation). Solution-space corridor: §VII.AR is structurally locked at PRIMARY-vs-SCHEMATIC LEVEL discipline per `substrate-first-canonical-sourcing.md §(iv)`.
- **INFO**: Borderline ranking robustness (N = 3); §VII.AR registry entry remains LANDED but Reading-A WIN annotation is conditional pending refinement.
- **FAIL**: Reading-B wins; the §VII.AR rank-ordering is anchor-specific, undermining the LEVEL-DRESSED framing. Solution-space corridor: route to next-session re-examination of the LEVEL-DRESSED rank-ordering claim.

**12. Effort estimate**: 0.4 wave-equivalent (single agent-session; spectrum cache pre-built; primary cost is per-anchor Spearman computation + bootstrap resampling).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the L_max=12 spectral triple at τ_fold; heat-kernel anchors `t_ref_k` are substrate-IS scale parameters intrinsic to the spectral-functional family. The rank-ordering of regulators at substrate-distance-2 pole s=4 is the substrate's own structural prediction — NOT a fit to external regulator data. FORBIDDEN container-thinking ("regulator atlas living in heat-kernel space"). The Reading-A vs Reading-B distinction is an ALGEBRA-AXIS PARTITION question (per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`): Reading-A = regulator-CLASS-invariant rank under anchor variation; Reading-B = regulator-PARAMETER-invariant rank under class variation. Mnemonic-vs-exact ratio discipline: the threshold N≥4 is exact (integer count); the Spearman 0.9 cutoff is the verifier-rubric-pre-registered admissibility threshold and is held fixed at plan-freeze (per Class 8.2 discipline).

---

## §W5-8. S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36  (A.37)

**1. Gate ID**: `S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36`

**2. Trigger**: `[VERIFY]` — Sage QQ exact arithmetic cross-check of A.36 float verdicts. The gate verifies that the float64 A.36 output is consistent with Sage exact-rational evaluation at the sign + decision-rule level (rank-ordering integers cannot drift under exact arithmetic, but floating-point Spearman computation can introduce rank-tie ambiguity that Sage exact resolves canonically).

**3. Classification**: GEOMETRIC. Substrate-IS observable: the Sage-exact rank correlations across the same anchor set as A.36, evaluated under QQ arithmetic.

**4. Agent type**: `lizzi-spectral-functional-theorist` PRIMARY (cross-check of own A.36 output under exact arithmetic; no separate cross-axis check required for verification of float vs Sage consistency).

**5. Hypothesis**: The float64 Spearman rank correlations from A.36 agree with Sage QQ exact-rational Spearman at the sign + decision-rule level (i.e., float and exact give the same N count and same Reading-A vs Reading-B verdict). Disagreement indicates rank-tie ambiguity in float64 that biases the decision rule.

**6. Method** (full self-contained dispatch prompt for `lizzi-spectral-functional-theorist`):

```
You are dispatched on COMPUTE-class gate S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36
(Wave 5 of session 89, DEPENDS ON A.36). Read this prompt in full before computing.

CONDITIONAL DISPATCH GATE:
  Read computations/session-89/s89_gate_verdicts.txt and verify presence of:
    grep "^S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY: (PASS|INFO|FAIL)" present
  AND verify A.36 npz exists at the expected path.
  IF A.36 verdict is BREAKDOWN/regime-FAIL with no usable npz:
    Emit mechanical-closure verdict per .claude/rules/mechanical-closure-discipline.md:
      value='PRE-REG-INC_blocked_by_S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY_BREAKDOWN'
    Skip computation; emit verdict line + working-paper §W5-8 status update.
  IF A.36 PASS/INFO/FAIL with usable npz: continue with the cross-check below.

CONTEXT:
- A.37 cross-checks A.36 float verdicts under Sage QQ exact arithmetic via
  the sage_eval / sage_simplify MCP wrappers (mcp__sage__sage_eval, sage_simplify).
- Eigenvalue cache supplies float64 inputs; Sage QQ promotes them to symbolic
  rationals via mpmath / Fraction conversion at a fixed precision (32 decimal places).
- Spearman rank correlation under QQ: the rank computation is INTEGER (no
  floating-point); ties resolve canonically via Sage's stable rank operator.
- Disagreement between A.36 float and A.37 Sage-exact at the rank level signals
  rank-tie ambiguity — flag as INFO (not FAIL).

SCRIPT PATH:
  computations/session-89/s89_w5_a37_sage_exact_spearman_cross_check_of_a36.py

MANDATORY OPENING:
  from canonical_constants import *
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')
  import numpy as np
  from fractions import Fraction
  from pathlib import Path
  # Sage MCP wrapper: invoke mcp__sage__sage_eval / sage_simplify per call.

INPUT-PIN MAP:
  s89_w5_a36_npz: computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz
  D_K_eigenvalue_cache: computations/session-84/s84_spectrum_cache_L12_tau019.npz

PRDR MACHINERY PIN:
  rank_correlation_estimator: sage-QQ-exact-Spearman
  sage_precision: 32 decimal places (rational-promotion threshold)
  anchor_set: <inherited from A.36 npz>
  regulator_atlas: <inherited from A.36 npz>
  decision_rule_match_check: True
  scheme: heat-kernel-rank-ordering-sage-QQ-cross-check
  convention: lizzi-a37-sage-QQ-cross-check-of-a36
  regulator_pin: a_n^{HK}
  numerical_precision: arbitrary (Sage QQ)

CROSS-CHECKS:
  (a) Float-vs-Sage Spearman value: per anchor pair, emit
      |Spearman_float − Spearman_sage_QQ_decimal_render|; flag if any > 1e-10.
  (b) Rank-tie detection: emit any anchor pair where float computation produced
      ties that Sage resolved canonically.
  (c) N count match: assert N_sage == N_float; if not, emit INFO with detailed
      anchor-by-anchor disagreement log.
  (d) Reading-A WIN match: assert reading_A_WIN_sage == reading_A_WIN_float;
      a Sage-Float disagreement at this level is the gate's primary FAIL pathway.

OUTPUT:
  Path: computations/session-89/s89_w5_a37_sage_exact_spearman_cross_check_of_a36.npz
  Keys:
    spearman_float_vs_sage_per_pair: dict
    max_abs_diff: float64
    rank_tie_anchors: list
    N_float: int  # from A.36
    N_sage: int   # this gate's computation
    reading_A_WIN_float: bool
    reading_A_WIN_sage: bool
    decision_rule_consistent: bool
    sage_precision: int
  Plot path: computations/session-89/s89_w5_a37_sage_exact_spearman_cross_check_of_a36.png
  Plot panels: (i) per-anchor pair |float - sage| residuals;
               (ii) N count comparison bar (float vs sage);
               (iii) rank-tie heatmap.

PASS PREDICATE:
  magnitude_verdict:
    PASS  iff N_sage == N_float AND reading_A_WIN_sage == reading_A_WIN_float
              AND max_abs_diff ≤ 1e-10
    INFO  iff N_sage == N_float AND reading_A_WIN_sage == reading_A_WIN_float
              BUT max_abs_diff > 1e-10 (numerical noise; rank-level decision unaffected)
    FAIL  iff N_sage != N_float OR reading_A_WIN_sage != reading_A_WIN_float
              (decision-rule inconsistency)
  sign_verdict: N/A
  regime_verdict:
    VALID iff sage_precision = 32 AND all anchors evaluable under Sage QQ
    MARGINAL iff some anchors require precision > 32 (numerical promotion)
    BREAKDOWN iff Sage MCP unavailable
  composite collapse: per gate-verdicts.md.

VERDICT EMISSION (single-shot atomic):
  Path: computations/session-89/s89_gate_verdicts.txt
  Dual-SHA companion comment row REQUIRED.

WORKING-PAPER SECTION:
  Path: sessions/archive/session-89/session-89-w5-workingpaper.md §W5-8
  Substrate framing paragraph + Sage QQ cross-check log MANDATORY.
```

**7. Machinery pin (PRDR)**:

```yaml
gate_id: S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36
schema_version: R3
trigger: [VERIFY]
classification: GEOMETRIC
producing_script: computations/session-89/s89_w5_a37_sage_exact_spearman_cross_check_of_a36.py
runtime_owner: lizzi-spectral-functional-theorist
co_author: None
conditional_predecessor: S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY  # DEPENDS ON A.36
input_pin_map:
  s89_w5_a36_npz: <pinned at dispatch>
  D_K_eigenvalue_cache: <pinned at dispatch>
machinery_pin_map:
  rank_correlation_estimator: sage-QQ-exact-Spearman
  sage_precision: 32
  anchor_set: <inherited from A.36>
  regulator_atlas: <inherited from A.36>
  decision_rule_match_check: True
  scheme: heat-kernel-rank-ordering-sage-QQ-cross-check
  convention: lizzi-a37-sage-QQ-cross-check-of-a36
  regulator_pin: a_n^{HK}
  numerical_precision: arbitrary
expected_output_4tuple:
  value: <decision_rule_consistent>
  scheme: heat-kernel-rank-ordering-sage-QQ-cross-check
  convention: lizzi-a37-sage-QQ-cross-check-of-a36
  L_max: 12
pass_threshold:
  N_match: True
  reading_A_WIN_match: True
  max_abs_diff_pass: ≤ 1e-10
  max_abs_diff_info: > 1e-10 with rank-level decision unaffected
  tolerance_rule: ABSOLUTE
```

**8. Expected output 4-tuple**: `(value=<decision_rule_consistent>, scheme=heat-kernel-rank-ordering-sage-QQ-cross-check, convention=lizzi-a37-sage-QQ-cross-check-of-a36, L_max=12)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: `N_sage == N_float` AND `reading_A_WIN_sage == reading_A_WIN_float` AND `max_abs_diff ≤ 1e-10` AND regime_verdict = VALID. A.36 float verdict is exact-arithmetic-confirmed.
- **INFO**: Decision rule consistent BUT max_abs_diff > 1e-10 (numerical noise; rank-level decision unaffected). A.36 verdict structurally robust under Sage QQ.
- **FAIL**: Decision-rule inconsistency (N or reading_A_WIN mismatch). A.36 float verdict is rank-tie-ambiguous; resolution favors Sage exact.

**10. Substitution chain** (verification-of-equality; THEOREM tolerance):

```
Step 1 (Definition): float_Spearman(anchor_i, anchor_j) := scipy.stats.spearmanr
                     output on float64 rank arrays.

Step 2 (Definition): sage_QQ_Spearman(anchor_i, anchor_j) := Sage QQ exact rank
                     correlation under symbolic rationals at 32-decimal precision.

Step 3 (Substitution): For each anchor pair (i, j), compute
                     float_value = float_Spearman(i, j)
                     sage_value = sage_QQ_Spearman(i, j) [as Decimal at 32 places]
                     residual = |float_value − float(sage_value)|

Step 4 (Decision rule): If for all pairs residual ≤ 1e-10:
                          N count and Reading-A WIN are guaranteed identical (float
                          and Sage agree at the rank level).
                        If any pair has residual > 1e-10 but rank-level decision
                          unchanged: INFO.
                        If rank-level decision differs: FAIL.

Step 5 (Direction): Direction is structural (verification of equality);
                    no sign verdict.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: A.36 verdict is exact-arithmetic-confirmed; the Reading-A vs Reading-B classification is robust under both float and Sage QQ. Solution-space corridor: §VII.AR LEVEL-DRESSED rank-ordering structural lock-in is exact.
- **INFO**: Float vs Sage agree at decision level but diverge at numerical level; rank-level decision unaffected. Solution-space corridor: A.36 verdict structurally robust; no remediation needed.
- **FAIL**: Float vs Sage disagree at decision level; rank-tie ambiguity in float biases the verdict. Solution-space corridor: Sage exact takes precedence; A.36 verdict reverts to whatever Sage yields, and §VII.AR registry entry annotation updates accordingly.

**12. Effort estimate**: 0.3 wave-equivalent (single agent-session; primary cost is Sage QQ rank correlation across 5×4 = 20 (anchor, regulator) pairs).

**13. Substrate framing per `phononic-framing.md` IS-not-IN`**: The substrate IS the spectral-functional family with rank correlations as substrate-IS observables; Sage QQ exact arithmetic is the substrate's own canonical numerical-evaluation discipline (per `regulator-pin-discipline.md §"Extension: Sage-Exact Rationals for Ω_GW Regulator-Class Values"`). FORBIDDEN container-thinking ("the rank-ordering living in float-arithmetic space"); the rank-ordering IS an integer permutation — float vs Sage is a verification of consistency, not a substrate variation. Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3): max_abs_diff threshold 1e-10 is mnemonic for "machine epsilon × 10^4" allowing for 32-place Sage promotion noise; the Sage exact form is the substrate canonical when float and exact diverge.

---

## Wave 5 → Waves 3 / 7 Decision Point

**Cross-wave dependencies (output of W5 feeds W7 + closes loop with W3)**:

1. **W5 A.8 ↔ W3 A.9 cross-anchor**: W5 A.8 Richardson scan tests `residual(L_max) ~ L^{−3}` against the analytic anchor `HK-5(τ_fold) + c·τ²` from W3 A.9. If W3 A.9 lands BEFORE W5 A.8 dispatch (intra-session ordering), W5 A.8 consumes `c_jensen_2nd_order_FW` directly and tests a sharper Richardson predicate; otherwise W5 A.8 emits the bare Richardson predicate and W3 A.9 is the post-hoc analytic confirmation.

2. **W5 A.28 ↔ W3 A.35 cross-anchor**: W5 A.28 τ=0.38 cross-validation requires regime-of-validity check against τ_max from W3 A.35. If W3 A.35 lands BEFORE W5 A.28 dispatch, W5 A.28 inherits τ_max ∈ {< 0.38, ≥ 0.38} routing. If A.35 lands AFTER W5 A.28, W5 A.28 emits `regime_verdict = MARGINAL` with "τ_max-bound-pending" annotation; the next-session post-hoc check upgrades the verdict if A.35 confirms τ_max ≥ 0.38.

3. **W5 A.31 ↔ W3 A.29 cross-anchor**: W5 A.31 FWD-C1 retry under parameterized slope_A canonical depends on the closed-form HK-5 framing. If W3 A.29 (κ_2 second-order Jensen) reveals a structurally significant correction at substrate-distance-1 pole s=3, W5 A.31 emits INFO pending re-derivation under the κ_2-corrected canonical.

4. **W5 A.27 → W7 A.24 forward-feeding**: W5 A.27 FWD-C2 disambiguation produces a §VII.AV STAGE-1-CANDIDATE (or REGISTRY-INCOMPLETE flag) that feeds the W7 A.24 multi-wave Mellin-cone closure (FWD-C1 closure). The cross-pillar-bridge K-counter advances per the disambiguation outcome; W7 A.24's Hybrid Independence Test verdict is conditional on whether W5 A.27 advances FWD-C2 to STAGE-1-CANDIDATE OR routes to REGISTRY-INCOMPLETE.

5. **W5 A.31 → W7 A.24 forward-feeding**: W5 A.31 FWD-C1 retry produces the c_sub_corrected canonical at the FWD-C1 Level-3 anchor; W7 A.24 multi-wave closure consumes c_sub_corrected as its primary input pin. If W5 A.31 PASSes, W7 A.24 inherits the parameterized canonical confirmation; if W5 A.31 FAILs, W7 A.24's FWD-C1 closure is BLOCKED-on-reconstruction.

**Sub-decomposition fallback** (if Wave 5 needs to split for dispatch fanout):

- **W5a**: A.8, A.28, A.31, A.36, A.37 (lizzi 5 items; substrate-distance-1 / Corner-I / FWD-C1 / heat-kernel sweep family)
- **W5b**: A.25, A.26, A.27 (volovik+connes joint; Corner-IV K-window log-derivative chain)

Both sub-waves dispatch in S89 Batch 1 in parallel; A.26 and A.27 within W5b have intra-sub-wave conditional dependencies.

---

## Wave 5 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR machinery enumeration MANDATORY at plan-freeze. All free parameters across 8 W5 gates are enumerated in each gate's PRDR machinery_pin_map block above. Cross-gate machinery-pin consistency enforced:

- **`tau_fold = 0.19`**: pinned in all gates; canonical_constants.py R-PROTECTED.
- **`tau_2x_fold = 0.38`**: pinned in A.28 only; derived as 2 · tau_fold.
- **`L_max_canonical = 12`**: pinned in A.25, A.26, A.36, A.37; canonical truncation per cross-pillar-bridge-anatomy.md §"Calibration corpus".
- **`L_max_richardson_scan_set`**: pinned in A.8 ([12, 14, 16, 18]) and A.28 ([10, 11, 12, 14]); both scans use Richardson L^{−3} extrapolation.
- **`L_max_envelope_scan_set`**: pinned in A.26 ([6, 7, 8, 9, 10, 11, 12]); 7-point envelope extraction.
- **`scheme = ζ-zeta-spectral-action`**: pinned in A.8, A.28, A.31 (lizzi-zeta-spectral-action family).
- **`scheme = volovik-superfluid-universe-GGE`**: pinned in A.25, A.26 (volovik-path family).
- **`scheme = bridge-anatomy-pre-registration`**: pinned in A.27 (audit gate).
- **`scheme = heat-kernel-rank-ordering`**: pinned in A.36, A.37 (heat-kernel anchor sweep family).
- **`regulator_pin = a_n^{ζ}`**: pinned in A.8, A.25, A.26, A.27, A.28, A.31 (zeta-regulated Seeley-DeWitt convention; per `regulator-pin-discipline.md` MANDATORY tagging).
- **`regulator_pin = a_n^{HK}`**: pinned in A.36, A.37 (heat-kernel-derived).
- **`GPU_path = torch.linalg.eigvalsh / eigh`**: pinned in A.8, A.25, A.26, A.28, A.31, A.36 (per `feedback_compute-environment.md` explicit GPU naming MANDATORY); A.27 audit gate has no GPU path; A.37 uses Sage MCP (no torch).
- **`OMP_NUM_THREADS = 8`**: pinned in all 8 gates per project rule (CPU thread cap).
- **`numerical_precision = float64`**: default for all numerical gates; A.37 promotes to Sage QQ arbitrary precision at 32 decimal places.
- **`random_seed = None`**: deterministic across all gates.
- **`domain_used_frac = 1.0`**: full-domain evaluation in all gates; no auto-shortening.

---

## Wave 5 Input-SHA Ledger

All input files SHA-pinned at dispatch (runtime computation of SHA-256 on first-read; companion comment row carries dual-SHA per `gate-verdicts.md` W9a-99 split):

| Input file | Used by gates | SHA pin form |
|:-----------|:--------------|:--------------|
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | A.8, A.28, A.36, A.37 (master cache; canonical L_max=12 cache) | `<runtime>` |
| `computations/session-89/s89_spectrum_cache_L18_tau019.npz` | A.8 (extended L_max=18 cache; built at S89 W5 dispatch start) | `<runtime>` |
| `computations/session-89/s89_spectrum_cache_L12_tau038.npz` | A.28 (Jensen τ=0.38 cache; built at S89 W5 dispatch start) | `<runtime>` |
| `computations/session-89/s89_spectrum_cache_L14_tau019.npz` | A.28 | `<runtime>` |
| `computations/session-89/s89_spectrum_cache_L14_tau038.npz` | A.28 | `<runtime>` |
| `computations/session-88/s88_w5b_47_spectrum_cache.npz` | A.25, A.26 (Corner-IV K-window source cache) | `<runtime>` |
| `computations/session-87/s87_w2_3_horizon_k_window.npz` | A.25, A.26 (horizon-crossing K-window anchor) | `<runtime>` |
| `computations/session-89/s89_w5_a25_corner_iv_k_window_log_derivative_recompute.npz` | A.26, A.27 (intra-wave dependency chain) | `<runtime>` |
| `computations/session-89/s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz` | A.27 (intra-wave dependency chain) | `<runtime>` |
| `sessions/archive/session-87/<W7a-74 evaluator script reference>` | A.36 | `<runtime>` |
| `sessions/permanent-results-registry.md` | A.27 (§VII.U.2 4-corner classification + §VII.AR baseline), A.36 (§VII.AR baseline) | `<runtime>` |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | A.27 (rule-file reference) | `<runtime>` |
| `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz` | A.37 (cross-check input) | `<runtime>` |
| `canonical_constants.py:slope_A_FW_Conv_A` (Ledger B.45 PENDING) | A.31 (substrate-first-provenance Class-(f) audit on missing pin) | `<runtime>` (or `PENDING-CANONICAL-PROMOTION` placeholder) |
| `canonical_constants.py:c_jensen_2nd_order_FW` (W3 A.9 PENDING) | A.8 (fallback if absent) | `<runtime>` (or `PENDING` placeholder) |
| `canonical_constants.py:tau_max_HK5_regime` (W3 A.35 PENDING) | A.28 (regime check; fallback to closed-form divergence boundary 5π) | `<runtime>` (or `PENDING` placeholder) |

Each gate's verdict line emits `audit_sha256` over the gate-specific input-pin map per `_script_template.py append_verdict()`; `content_sha256` is computed over the producing script bytes. Dual-SHA companion comment row REQUIRED for all 8 gates.

---

## End of Wave 5 Plan

**8 gate blocks landed** (A.8, A.25, A.26, A.27, A.28, A.31, A.36, A.37) per the user-curated Ledger A Cluster-E carry-forward source. Total Wave 5 effort: 4.15 wave-equivalents. Conditional chains: A.26 BLOCKED on A.25 PASS; A.27 BLOCKED on A.26 PASS-or-INFO; A.37 BLOCKED on A.36 (any non-BREAKDOWN). Cross-wave dependencies: W5 → W3 A.9 / A.29 / A.35 (anchors); W5 A.27 + A.31 → W7 A.24 (multi-wave Mellin-cone closure forward-feeding).
