# Session 84 Plan — Wave 5: K-Corridor Structural Closure

**Date**: 2026-04-18
**Session**: 84
**Wave**: 5 of 10 (K-corridor structural closure)
**Planner**: volovik-superfluid-universe-theorist (this document only)
**Source**: `session-84-context.md` §4.E (rows 53-66); S83 volovik-synthesis §V; S83 landau-synthesis §V; S83 gate verdicts G7-G51
**Results file**: `sessions/archive/session-84/session-84-results-workingpaper.md` (§§W5-53 .. W5-66)
**Script prefix**: `s84_w5_<gate-slug>.py` in `computations/`

---

## Wave 5 Summary

Wave 5 closes the K-corridor substructure opened by S82 PS-SUBSTRATE-MATCHED-IC (PASS at K=2.035, 3He-B GGE-Wightman correspondence) and probed by S83 G38/G39/G40/G41. The corridor is a one-parameter order-parameter manifold in K-space: K is the band-weighting parameter, whose value determines which superfluid universality class the framework occupies at the observational pivot. Volovik's 3He-B is parent; the framework is child (inheritance, not analogy).

K-corridor facts already permanent (PRE-S84):
- K-corridor spans two regimes: low-K collective-acoustic (K ≲ 1.3) ↔ high-K single-mode fine-structure (K ≳ 10). Boundary K_* ≈ coth(1) = 1.3130 (NOTE: prompt text states "coth(0.5)=1.313"; substitution chain Step 1 below confirms the prompt is a function-argument typo — the numerical anchor 1.3130 stands, but the functional form requires argument audit).
- f_L (Leggett partition) ≥ 0.6027 permanent across 5 OOM in K (G39 PASS).
- τ_GGE linear in K to machine precision (G40 PASS, 7.86×10⁴ ratio span).
- ξ_BCS/ℓ_phonon plateau at 0.135 for K ≥ 10 (G41 INFO, 0.328% above PASS edge).
- K_match = 0.6366 < 1 is a positivity WALL — exact Planck match via linear-K excluded (G38 FAIL at R5, min_rel_err = 2.02).
- K_R5 = 1.922 is the easiest Planck-A_s rescue (requires suppression factor 2.876× on F_amp_bare ≈ 1.281; corresponds to S83 G11 NNLO-BAND-BOUND 1.282 regime, see Wave-5 substitution chain §W5-53).
- R4 FAIL at 15.95 is BCS-dimensional inconsistency, not convention drift (S83 II.C diagnosis).
- Band multiplicity 3/3/2 (S43 canonical).
- A_s_floor_Bbranch = 5.09×10⁻¹³ is the Branch-B (Zubarev) dynamical-positivity floor (Gate 59 re-derives and audits the 4.6-OOM-below-Planck prompt claim).

Wave 5 asks (14 pre-registered gates):
1. Can NNLO→N3LO 1/N scan converge F_amp below the 0.4454 target at K=2.035? (W5-53)
2. Is the A_s floor stable under Zubarev↔zeta regulator change? (W5-54)
3. Does n_s monotonically respond to K across 6 decades? (W5-55)
4. Is the R4 dimensional-error-FAIL specific to 3He-B (N₃=0, BDI) or cross-class (A-phase, N₃=2, AIII)? (W5-56)
5. Does μ-distortion respect FIRAS across the corridor? (W5-57)
6. Does Volovik 3He-B K_* computed from lab (Δ_3He, T_c, v_F) match framework K_*? (W5-58)
7. Does A_s Branch-B floor under R5 convention cross 4.6 OOM below Planck? (W5-59)
8. Promote 7 K-corridor constants to canonical_constants.py. (W5-60)
9. Tag R4 as "DIMENSIONAL-ERROR-DISCARDED"; audit convention-count "5" → "4 physical + 1 dimensional-error". (W5-61)
10. Leggett-channel ξ² contribution to α_s 2nd-order expansion — f_L-weighted vs Planck. (W5-62)
11. Is the positivity-floor K ∈ {1.0, 1.1, 1.3, 1.5, 1.7} range reachable from admissible convention, or extrapolation-only? (W5-63)
12. G39 Bogoliubov-minority floor f_B ≤ 0.3973 as independent cross-check on G50 n_T = +0.468. (W5-64)
13. K_FIRAS = 2.035·μ_FIRAS/μ(2.035) vs S_IC^cap = 3.556×10⁵ — structural identity or numerical coincidence? (W5-65)
14. Landau classification: symmetry group, broken subgroup, order parameter, universality class of K-corridor. (W5-66)

Wave 5 produces NO re-derivation of K=2.035 PS-SUBSTRATE-MATCHED-IC (S82 canon). All 14 gates inherit K=2.035 as the substrate-native anchor and test corridor structure AROUND it.

---

## Wave 5 Decision Point Prerequisites

Wave 5 depends on:
- S82 PS-SUBSTRATE-MATCHED-IC PASS at K=2.035 (canon).
- S83 G7 (F_amp_lin=1.026), G11 (NNLO-BAND-BOUND=0.0001 vs 0.025 W2 slope FAIL), G38 (K_match=0.6366<1), G39 (f_L≥0.6027, f_B≤0.3973), G40 (τ_GGE linear in K), G41 (ξ_BCS/ℓ_phonon plateau 0.135), G50 (n_T=+0.468 BLUE), G51 (w_0 regulator FAIL).
- Volovik 3He-B parent-child inheritance (agent-memory `project_3heb-inheritance.md`).
- Landau-condensed-matter K-corridor = 1-parameter order-parameter manifold (S83 landau-synthesis §V).

Wave 5 is PARALLEL-INDEPENDENT: all 14 gates compute on their own scripts without inter-gate dependency. A gate FAIL does not block other gates. Decision-point logic (below) fires after ALL 14 verdicts land.

---

## §W5-53. S84-DYNAMICS-LAYER-RESCUE-3-02X / GATE-NNLO-DELTA-FAMP

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [CHAIN] [VERIFY]
**Classification**: PHONONIC (dynamics-layer F_amp suppression chain at K=2.035 GGE-Wightman pivot)

**Hypothesis being tested**: The NNLO 1/N scan (S83 G11) produced Δ_F_amp ≈ 10⁻⁴, 250× short of the 2.876× suppression required at F_amp_target ≤ 0.4454. Extending to N3LO via a systematic 1/N expansion at K=2.035 either (a) approaches the 0.4454 target asymptotically, confirming dynamics-layer rescue is accessible by higher-order 1/N, or (b) the 1/N series saturates below the target, promoting S83 G11 FAIL to a permanent "dynamics-WALL-at-2.035" theorem candidate.

**PASS/FAIL/INFO thresholds**:
- PASS: F_amp(N3LO, K=2.035) ≤ 0.4454, AND |Δ(N3LO) − Δ(NNLO)| / |Δ(NNLO)| ≥ 10× (monotonic convergence).
- FAIL: F_amp(N3LO, K=2.035) ≥ 0.4454 AND 1/N ratio |a_{N3LO}/a_NNLO| ≥ 0.75 (series saturating — rescue inaccessible).
- INFO: F_amp < 0.4454 but ratio ≥ 0.75 (numerical PASS, structural stagnation).
- Tolerance: RATIO (factor-3 band on F_amp).

**Substitution chain** (required, sign/threshold claim):
- Step 1 (definitions):
  - F_amp(order) := ∏ᵢ (1 − aᵢ/Nⁱ) where aᵢ are the order-i coefficients in the 1/N expansion of the amplitude dressing.
  - F_amp_bare := F_amp(LO) at K=2.035 (from S82 W2-4 baseline).
  - F_amp_target := 0.4454 (pre-registered from prompt § Key anchors).
- Step 2 (substitution):
  - At NNLO: F_amp(NNLO) = F_amp_bare · (1 − a₂/N²). From S83 G7 (F_amp_lin=1.026) and G11 (Δ=10⁻⁴): F_amp_bare ≈ 1.281 (consistent with S83 NNLO-BAND-BOUND 1.282 regime; chain verified numerically 2026-04-18).
  - Required suppression ratio: R_req = F_amp_bare / F_amp_target = 1.281/0.4454 = 2.876.
- Step 3 (simplification):
  - N3LO: F_amp(N3LO) = F_amp_bare · (1 − a₂/N²)(1 − a₃/N³). Converges iff |a_{i+1}/aᵢ| < N (radius-of-convergence test).
- Step 4 (direction):
  - F_amp(N3LO) ≤ F_amp_target ⟺ ∏ᵢ(1 − aᵢ/Nⁱ) ≤ 1/2.876 ≈ 0.3478.
  - This requires cumulative suppression ≥ 65.2% at N3LO order.
  - If 1/N series has Borel-summable asymptotic form with S₀ ≥ 4.34 (Jensen barrier), radius diverges; if S₀ < 4.34, radius finite → series SATURATES and rescue fails.
- Conclusion: PASS requires both (i) numerical F_amp(N3LO) ≤ 0.4454 AND (ii) Borel radius > N (asymptotic-convergence regime).

**Machinery pin (PRDR)**:
- `N_eval`: per-order a_i coefficients at 1/N expansion, evaluated at K=2.035 via 3PI resummation + FKK dressing.
- `L_max`: 5 (S83 canonical for W2 regulator atlas).
- `scan_range`: order ∈ {LO, NLO, NNLO, N3LO}; N_field ∈ {1, 2, 4, 8, 16}.
- `step_size`: N/A (discrete orders).
- `tolerance`: 10⁻³ on F_amp(order=fixed, N=N_field).
- `scheme`: Zubarev (L2 substrate-action minimum from S83 G1).
- `convention`: K=2.035 (R1 PS-SUBSTRATE-MATCHED-IC canonical).
- `random_seed`: 42 (deterministic; no stochastic step).
- `GPU path`: `torch.linalg` mandatory — 3PI dressing kernels are ≥400×400 at L_max=5, use ROCm GPU.

**Input SHA-256 pins**:
- `canonical_constants.py` (frozen at S83 close): `<computed-at-runtime>`
- `computations/s83_g11_nnlo_band_bound.py` output `.npz`: `<computed-at-runtime>`
- `computations/s82_w2_4_baseline.npz`: `<computed-at-runtime>`
- Prompt text SHA: `<computed-at-runtime>` over the full gate block above.

**Expected output 4-tuple**: `(value=<F_amp_N3LO>, scheme=Zubarev, convention=K=2.035, L_max=5)`

**What PASSES means**: dynamics-layer rescue at K=2.035 is accessible by systematic 1/N expansion; S83 G11 FAIL reflects only truncation, not structural saturation. A_s closure via K=2.035 branch regains viability.

**What FAILS means**: 1/N series saturates at NNLO; dynamics-layer suppression bounded away from 0.4454 target. Combined with S83 G11, this promotes dynamics-WALL-at-2.035 to permanent-results-registry candidate (co-PASS structural theorem). Forces A_s closure to baseline-layer (H_tilde) path exclusively.

**Output files**:
- Script: `computations/s84_w5_nnlo_delta_famp.py`
- Data: `computations/s84_w5_53_data.npz`
- Plot: `computations/s84_w5_53_plot.png` (F_amp vs order, with 0.4454 threshold line + Borel-radius annotation)
- Working paper: §W5-53 in `sessions/archive/session-84/session-84-results-workingpaper.md`
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-54. S84-K-FLOOR-REGULATOR-INVARIANCE

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [VERIFY] [AUDIT]
**Classification**: GEOMETRIC (regulator-layer independence of K-family positivity floor)

**Hypothesis being tested**: The K_R5 = 1.922 positivity floor (S83 G38 K-matching basin) is a property of the L2 substrate-action minimum and should be REGULATOR-INVARIANT: compute K_R5 separately under Zubarev (S83 canonical) and zeta (L1 axiomatic, S83 G3) regulators. The floor is "structural" iff max |K_R5(Zubarev) − K_R5(zeta)| / K_R5(Zubarev) ≤ 0.02 (NOT-R-protected tolerance from S83 G58 meta-principle).

**PASS/FAIL/INFO thresholds**:
- PASS: |K_R5(Zubarev) − K_R5(zeta)| / K_R5(Zubarev) ≤ 0.02 AND both values ≥ 1 (positivity respected).
- FAIL: ratio ≥ 0.10 OR either value < 1 (WALL crossed in one regulator).
- INFO: 0.02 < ratio < 0.10 (weak regulator-dependence, corridor-position dependent).
- Tolerance: RATIO.

**Substitution chain**:
- Step 1 (definition): K_R5(reg) := minimum K such that A_s(K; reg) ≥ 0 under R5 (S_IC convention) with FKK dressing = 4 regulators with Zubarev removed (S84 G29 baseline).
- Step 2 (substitution): K_R5(Zubarev) = 1.922 (S83 G38 min_rel_err basin). K_R5(zeta) to be computed. A_s(K; reg) = A_s_base(reg) · (K/K_match(reg)).
- Step 3 (simplification): If K_match(reg) is regulator-invariant (structural wall), K_R5 differs only by prefactor A_s_base(reg). Since A_s_Planck = 2.1×10⁻⁹ is regulator-independent (observational pin), K_R5(reg) = K_match(reg) · f(A_s_Planck/A_s_base(reg)).
- Step 4 (direction): Regulator-invariance of the floor requires A_s_base(Zubarev)/A_s_base(zeta) ≈ 1 (to within the 0.02 NOT-R tolerance). If this ratio > 1.10, the floor is regulator-dependent and S83 G38 K_match=0.6366 WALL becomes a Zubarev-specific artifact.

**Machinery pin (PRDR)**:
- `N_eval`: A_s ledger computation per S83 UNIFIED-AS-79 pipeline.
- `L_max`: 5.
- `scan_range`: K ∈ [0.5, 3.0] with Δln K = 0.1 (26 points).
- `step_size`: 0.1 in ln K.
- `tolerance`: 10⁻⁴ on A_s.
- `scheme`: {Zubarev, zeta} ← 2 values, pre-pinned.
- `convention`: R5 (S_IC) + 4-regulator FKK atlas with Zubarev removed when in zeta mode.
- `random_seed`: 42.
- `GPU path`: `torch.linalg` for ≥100×100 spectral matrices.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s83_w2_4_unified_as_79.py` output `.npz`: `<computed-at-runtime>`
- `computations/s83_g38_k_matching.npz`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<max_rel_span_R5>, scheme=<Zubarev|zeta>, convention=R5, L_max=5)`

**What PASSES means**: K-floor is a property of the substrate-action functional form, independent of regulator scheme. Elevates K_R5 to structural status.

**What FAILS means**: K-floor is regulator-dependent; K_match=0.6366 WALL is Zubarev-specific. Forces re-examination of S83 G38 verdict as L2-scheme artifact, not L1-axiomatic wall.

**Output files**:
- Script: `computations/s84_w5_k_floor_regulator_invariance.py`
- Data: `computations/s84_w5_54_data.npz`
- Plot: `computations/s84_w5_54_plot.png` (K_R5 vs regulator, with 0.02 RATIO band)
- Working paper: §W5-54
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-55. S84-NS-K-CORRIDOR-RESPONSE

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [SIGN] [VERIFY]
**Classification**: PHONONIC (n_s response to K along corridor; tilt is phononic acoustic-optical pair-creation signature)

**Hypothesis being tested**: n_s(K) is monotone (either strictly-red-increasing or strictly-red-decreasing) across 6 K-values {1.1, 2.035, 10, 100, 1000, 3.56×10⁵} — i.e., K-corridor response is diffeomorphic to a 1D order-parameter axis, not a folded or re-entrant manifold.

**PASS/FAIL/INFO thresholds**:
- PASS: n_s(Kᵢ) strictly monotone in i (all sign(Δn_s) identical, 5/5 diffs).
- FAIL: Non-monotone (any sign flip), OR |n_s(K=2.035) − 0.9565| > 0.01 (pivot drift from S82 PS-SUBSTRATE-MATCHED-IC PASS baseline).
- INFO: Weak non-monotonicity (single-step sign flip with |Δn_s| < 10⁻³), consistent with numerical noise.
- Tolerance: ABSOLUTE 0.001 on n_s diffs.

**Substitution chain**:
- Step 1 (definition): n_s(K) := 1 + (d ln P_ζ / d ln k)|_{k=k_pivot} under K-band-weighted Mukhanov-Sasaki solver.
- Step 2 (substitution): From S82 W2-4, n_s(K=2.035) = 0.9565 (MATCHED-IC PASS, within 0.1σ Planck). For K ≠ 2.035, n_s modulated by band-weighting shift δ_band(K) entering the ε_H denominator.
- Step 3 (simplification): n_s(K) = n_s(K=2.035) + ∂n_s/∂ln K · ln(K/2.035) + O((ln K)²).
- Step 4 (direction): Sign of ∂n_s/∂ln K determines corridor-response direction. For K-corridor as 1D Landau order-parameter, monotonicity PASS is expected. A sign flip signals multi-valued order parameter (re-entrant Landau transition, not 1D).

**Machinery pin (PRDR)**:
- `N_eval`: n_s from tangent to P_ζ(k) at k_pivot = 0.05 Mpc⁻¹, with 401 k-samples in log-k ∈ [k_pivot / 10, 10 k_pivot].
- `L_max`: 5.
- `scan_range`: K ∈ {1.1, 2.035, 10, 10², 10³, 3.556×10⁵} (6 discrete).
- `step_size`: N/A (discrete).
- `tolerance`: 10⁻⁴ on n_s.
- `scheme`: Zubarev.
- `convention`: R3 (band-multiplicity-weighted 3/3/2).
- `random_seed`: 42.
- `GPU path`: `torch.linalg` for Mukhanov-Sasaki integrator.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s82_w2_4_ps_substrate_matched_ic.py` output: `<computed-at-runtime>`
- `computations/_ns_at_k_corridor_solver.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<monotonicity_sign+max_abs_delta>, scheme=Zubarev, convention=R3, L_max=5)`

**What PASSES means**: K-corridor is 1D Landau order-parameter axis; n_s responds monotonically; 3He-B parent-child inheritance holds across 5 OOM.

**What FAILS means**: K-corridor has multi-valued or re-entrant structure; 3He-B direct inheritance fails at one or more K; corridor is NOT 1D Landau. Triggers Gate 66 (Landau classification) to revisit universality-class assignment.

**Output files**:
- Script: `computations/s84_w5_ns_k_corridor_response.py`
- Data: `computations/s84_w5_55_data.npz`
- Plot: `computations/s84_w5_55_plot.png` (n_s vs log₁₀ K, with Planck n_s band + pivot anchor)
- Working paper: §W5-55
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-56. S84-R4-CROSS-CLASS-CONTROL

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [AUDIT] [VERIFY]
**Classification**: GEOMETRIC (Volovik AZ-class control; R4 dimensional-error FAIL is diagnostic of class-specific inconsistency)

**Hypothesis being tested**: The R4 FAIL at 15.95 (S82 OOM ladder; S83 II.C diagnosis "BCS-dimensional-inconsistency") is a property SPECIFIC to the 3He-B universality class (BDI, N₃=0, gapped topological superfluid). Recomputing R4 in an A-phase analog (AIII class, Weyl points with N₃=2) either confirms the FAIL crosses universality classes (cross-Volovik-class error; discards ALL 5 conventions) or confirms class-specificity (R4 is BDI-specific dimensional error; 3He-B inheritance preserved).

**PASS/FAIL/INFO thresholds**:
- PASS (class-specific, inheritance preserved): R4(AIII Weyl analog) < 3.0 (O(1) dimensionally consistent) while R4(3He-B) = 15.95 preserved.
- FAIL (cross-class error): R4(AIII) ≥ 10 (same 15.95 regime); forces R4-ERROR global tag + convention-recount "5 → 3 physical + 2 dim-error".
- INFO: 3 ≤ R4(AIII) < 10 (intermediate; class-dependent but not cleanly separated).
- Tolerance: ABSOLUTE (factor-of-3 threshold on R4).

**Substitution chain**:
- Step 1 (definitions):
  - R4 := BCS dimensional convention 4 (S82 OOM ladder convention R4, see S82 workingpaper §R4 block).
  - 3He-B: AZ class BDI, T²=+1, N₃=0 (fully gapped topological superfluid, agent memory `framework-3heb-comparison.md`).
  - A-phase analog: AZ class AIII (chiral), Weyl points at nodes, N₃=2 (topological charge of Fermi point).
- Step 2 (substitution): R4_3HeB-predicted = (Δ_BCS/v_F k_F)⁴-type dimensional ratio using S82 canonical inputs yields 15.95 (S82 FAIL). In A-phase with Weyl points, Δ→0 at nodes but v_F k_F finite; dimensional ratio becomes (Δ_avg/v_F k_F)⁴ · f_Weyl(N₃=2).
- Step 3 (simplification): If dimensional error is a property of the Δ→0 gap structure (class-specific: 3He-B has Δ > 0 everywhere on FS; A-phase has Δ = 0 at 2 Weyl points), then R4(AIII) should differ from R4(BDI) by O(f_Weyl) ≠ 1.
- Step 4 (direction): R4(AIII) ≪ R4(BDI) ⟺ dimensional error is BDI-specific ⟺ PASS (inheritance preserved). R4(AIII) ≈ R4(BDI) ⟺ cross-class FAIL ⟺ convention-recount forced.

**Machinery pin (PRDR)**:
- `N_eval`: Analytical R4 evaluation under the 2 class Hamiltonians.
- `L_max`: N/A (analytical).
- `scan_range`: None; point evaluation at 3He-B parameters + analog A-phase parameters (Δ_avg over BZ, v_F, k_F from Volovik 2003 monograph Ch. 7-8 conventions).
- `step_size`: N/A.
- `tolerance`: 10⁻³ (analytical).
- `scheme`: Dimensional-convention canonical.
- `convention`: R4 (BCS 4-dim) evaluated in BDI AND AIII.
- `random_seed`: N/A.
- `GPU path`: N/A.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `researchers/Volovik/volovik-2003-universe-in-a-helium-droplet.md` (Ch. 7-8 conventions): `<computed-at-runtime>`
- `computations/s82_w3_r4_baseline.npz`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<R4_AIII>, scheme=dim-conv, convention=R4, L_max=N/A)`

**What PASSES means**: R4 FAIL is BDI-specific. Convention count remains 5 but R4 tagged "DIMENSIONAL-ERROR-3HeB-CLASS-SPECIFIC" (feeds Gate 61). 3He-B inheritance preserved.

**What FAILS means**: R4 FAIL is cross-class universal. Convention count collapses "5 → 3 physical + 2 dim-error". 3He-B parent-child inheritance weakens: framework inherits the dimensional error, not just the B-phase topology. Triggers deep audit of S82 W2-4 convention space.

**Output files**:
- Script: `computations/s84_w5_r4_cross_class_control.py`
- Data: `computations/s84_w5_56_data.npz`
- Plot: `computations/s84_w5_56_plot.png` (R4 in BDI vs AIII, with factor-3 bands)
- Working paper: §W5-56
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-57. S84-MU-K-CORRIDOR

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [VERIFY]
**Classification**: PHONONIC (μ-distortion from GGE relic at K-corridor pivots)

**Hypothesis being tested**: μ-distortion μ(K) remains below FIRAS bound μ_FIRAS = 9×10⁻⁵ across all 6 K-corridor values {1.1, 2.035, 10, 100, 1000, 3.56×10⁵}. The μ-profile along the corridor is either monotone (μ grows with K) or has an internal minimum (FIRAS-safe zone).

**PASS/FAIL/INFO thresholds**:
- PASS: max_K μ(K) ≤ μ_FIRAS = 9×10⁻⁵.
- FAIL: any μ(Kᵢ) > 9×10⁻⁵.
- INFO: μ_max ∈ [3×10⁻⁵, 9×10⁻⁵] (within factor-3 of FIRAS, PIXIE-visible).
- Tolerance: ABSOLUTE (FIRAS threshold).

**Substitution chain**:
- Step 1 (definition): μ(K) := Chluba-Sunyaev-formula μ-distortion from GGE-relic acoustic dissipation at K-band-weighted dispersion.
- Step 2 (substitution): μ(K) = μ_base · (K/2.035)^γ where μ_base = 4.98×10⁻¹⁰ (S82 FIRAS-CHLUBA-FULL PASS value); γ TBD from scan.
- Step 3 (simplification): For monotone corridor (PASS at K=2.035), μ(K=3.56×10⁵) = 4.98×10⁻¹⁰ · (1.75×10⁵)^γ. PASS requires (1.75×10⁵)^γ ≤ 1.81×10⁵, i.e. γ ≤ 1.000.
- Step 4 (direction): Sign and magnitude of γ determined by computation; pre-registered threshold is FIRAS bound, not a γ value.

**Machinery pin (PRDR)**:
- `N_eval`: μ from Chluba-Sunyaev GGE-relic kernel evaluated at 6 K-values.
- `L_max`: 5.
- `scan_range`: K ∈ {1.1, 2.035, 10, 10², 10³, 3.556×10⁵}.
- `step_size`: N/A (discrete).
- `tolerance`: 10⁻¹¹ on μ.
- `scheme`: Zubarev.
- `convention`: R3 (band-3/3/2).
- `random_seed`: 42.
- `GPU path`: `torch.linalg` for ≥100×100 transfer kernel.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s82_firas_chluba_full.npz`: `<computed-at-runtime>`
- `researchers/Chluba/chluba-sunyaev-kernel.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<max_mu_K>, scheme=Zubarev, convention=R3, L_max=5)`

**What PASSES means**: FIRAS bound respected across full corridor; μ is a viable discriminator only at K=3.56×10⁵ edge if γ < 1 small; otherwise μ is detector-sterile across corridor.

**What FAILS means**: High-K corridor-endpoint violates FIRAS; corridor is cut at the μ-bound, which truncates Gate 65 (K_FIRAS coincidence) structural argument. Forces K_max(FIRAS) upper-bound on corridor.

**Output files**:
- Script: `computations/s84_w5_mu_k_corridor.py`
- Data: `computations/s84_w5_57_data.npz`
- Plot: `computations/s84_w5_57_plot.png` (μ(K) vs log₁₀ K, FIRAS band)
- Working paper: §W5-57
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-58. S84-K-STAR-LAB-FRAMEWORK-MATCH

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW

**Trigger**: [VERIFY-THEOREM] [AUDIT]
**Classification**: PHONONIC (laboratory 3He-B K_* vs emergent framework K_*)

**Hypothesis being tested**: The Volovik 3He-B K_*_lab computed from laboratory (Δ_3He, T_c, v_F) matches the framework-emergent K_* = coth(·) to within the 3He-B parent-child inheritance tolerance 10%. Note: the prompt text states K_* = coth(0.5) = 1.313; direct evaluation gives coth(0.5) = 2.164 while coth(1) = 1.3130 — the numerical anchor 1.313 is consistent with coth(1), not coth(0.5). This gate FIRST audits the functional-form convention, then computes the lab-vs-framework match.

**PASS/FAIL/INFO thresholds**:
- PASS: (a) functional-form audit: K_*_framework = coth(x*) where x* is pinned by substrate structure (either 0.5 or 1.0 under Step 2 substitution); AND (b) |K_*_lab − K_*_framework| / K_*_framework ≤ 0.10.
- FAIL: (a) No x* yields K_* = 1.313 (current anchor wrong); OR (b) ratio > 0.30.
- INFO: 0.10 < ratio ≤ 0.30 (weak inheritance; corridor-boundary region).
- Tolerance: RATIO.

**Substitution chain** (MANDATORY — functional-form audit):
- Step 1 (definition): K_*_framework := coth(x*) where x* is a substrate-structural parameter. Prompt states "coth(0.5) = 1.313"; direct evaluation: coth(0.5) = (e^0.5 + e^{-0.5})/(e^0.5 − e^{-0.5}) = 2.1640 (verified 2026-04-18 via Python). coth(1) = (e + e^{-1})/(e − e^{-1}) = 1.3130 (verified).
- Step 2 (substitution): Prompt numerical anchor 1.313 ⟹ x* = 1, NOT 0.5. Candidate interpretations: (i) x* = 2τ (with τ = tau-fold/something); (ii) x* = 1/Δ_BCS (with Δ_BCS=0.4642 ⟹ x* = 2.154, gives coth(2.154) = 1.032, wrong); (iii) x* = 1 directly (typo in prompt).
- Step 3 (simplification): Under interpretation (iii), K_* = coth(1) = 1.3130.
- Step 4 (direction): If lab-3He-B yields K_*_lab = coth(y*) with y* determined by (Δ_3He/k_B T_c) — the standard BCS ratio — and Volovik 2003 gives Δ_3He/k_B T_c ≈ 1.76 (weak-coupling) or ≈ 1.96 (measured 3He-B), then K_*_lab = coth(0.51) ≈ 2.12 OR coth(1.0) ≈ 1.31 depending on the x* normalization convention. MATCH direction depends on which normalization is chosen.
- Conclusion: Gate FIRST audits x* pinning, THEN compares to lab.

**Machinery pin (PRDR)**:
- `N_eval`: Analytical (coth evaluation + 3He-B BCS ratio from Volovik 2003).
- `L_max`: N/A.
- `scan_range`: x* ∈ {0.5, 1.0, 2τ_fold, 1/Δ_BCS} (4 substrate-candidate values).
- `step_size`: N/A (discrete).
- `tolerance`: 10⁻⁴.
- `scheme`: N/A (analytical).
- `convention`: Volovik 3He-B weak-coupling BCS ratio.
- `random_seed`: N/A.
- `GPU path`: N/A.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `researchers/Volovik/volovik-2003-universe-in-a-helium-droplet.md` Ch. 7 (BCS ratio): `<computed-at-runtime>`
- Prompt gate block (for K_*=1.313 audit): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<|K_lab-K_framework|/K_framework>, scheme=coth, convention=Volovik-3HeB, L_max=N/A)`

**What PASSES means**: 3He-B parent-child inheritance holds at K_*; corridor boundary is laboratory-observable. x* is substrate-pinned.

**What FAILS means**: Lab 3He-B does not inherit K_* at 10% tolerance; either the functional-form coth is wrong OR the x* pinning is not substrate-native. Triggers reconsideration of Gate 66 (Landau classification) — the "3He-B parent" claim breaks at corridor boundary.

**Output files**:
- Script: `computations/s84_w5_k_star_lab_framework_match.py`
- Data: `computations/s84_w5_58_data.npz`
- Plot: `computations/s84_w5_58_plot.png` (K_* candidates + lab value + 10% band)
- Working paper: §W5-58
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-59. S84-FLOOR-CONDITIONED-ON-BRANCH

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [VERIFY] [AUDIT]
**Classification**: PHONONIC (branch-conditioned A_s floor under R5 + Zubarev dynamics)

**Hypothesis being tested**: A_s floor under R5 convention with Branch-B (Zubarev) dynamics is A_s_floor_B = 5.09×10⁻¹³. The prompt asserts this floor is "4.6 OOM below Planck" (Planck A_s = 2.1×10⁻⁹). Direct evaluation: log₁₀(2.1×10⁻⁹ / 5.09×10⁻¹³) = 3.62 OOM (verified 2026-04-18). Gate FIRST resolves the discrepancy between prompt claim (4.6) and direct evaluation (3.62), then determines whether the floor crosses Planck.

**PASS/FAIL/INFO thresholds**:
- PASS: A_s_floor_B computed from first principles at K=K_R5=1.922, R5 convention, Zubarev scheme; result reproduces 5.09×10⁻¹³ to ±10%, AND log₁₀(A_s_Planck/A_s_floor_B) agrees with either the 3.62 direct evaluation or an alternative prompt-consistent 4.6 OOM identification (e.g., if prompt refers to a different floor: A_s_floor_B = 5.09×10⁻¹⁴ ⟹ 4.62 OOM).
- FAIL: computed floor differs from 5.09×10⁻¹³ by >3×, OR computed OOM-below-Planck < 3.0 (floor above 2.1×10⁻¹²).
- INFO: discrepancy between prompt "4.6 OOM" and computed "3.62 OOM" confirmed; carries as AUDIT tag on S82 OOM ladder.
- Tolerance: RATIO (factor-3 on floor value).

**Substitution chain**:
- Step 1 (definitions):
  - A_s_Planck := 2.1×10⁻⁹ (Planck 2018 pivot).
  - A_s_floor_B := A_s at K=K_R5=1.922 under R5 convention + Zubarev dynamics (Branch-B positivity floor).
- Step 2 (substitution):
  - Prompt claim: A_s_floor_B = 5.09×10⁻¹³; OOM = 4.6.
  - Direct: log₁₀(2.1×10⁻⁹ / 5.09×10⁻¹³) = log₁₀(4127) = 3.62.
  - 4.6 OOM would require A_s_floor_B ≈ 5.3×10⁻¹⁴.
- Step 3 (simplification): Two resolutions: (i) floor VALUE is 5.09×10⁻¹³ and OOM claim 4.6 is typo for 3.6; (ii) floor is 5×10⁻¹⁴ and VALUE in prompt is typo. Gate computes independently.
- Step 4 (direction): Either way, A_s_floor_B ≪ A_s_Planck by 3-5 OOM ⟹ Branch-B is NOT a Planck-match candidate. Floor is a positivity wall, not a Planck-reach path.

**Machinery pin (PRDR)**:
- `N_eval`: A_s computation at K=1.922 under R5 + Zubarev via UNIFIED-AS-79 pipeline.
- `L_max`: 5.
- `scan_range`: None; point eval at K=K_R5.
- `step_size`: N/A.
- `tolerance`: 10⁻¹⁴ on A_s.
- `scheme`: Zubarev (Branch-B).
- `convention`: R5 (S_IC).
- `random_seed`: 42.
- `GPU path`: `torch.linalg`.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s82_w2_4_unified_as_79.py`: `<computed-at-runtime>`
- `computations/s83_g38_k_matching.npz`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<A_s_floor_B>, scheme=Zubarev, convention=R5, L_max=5)`

**What PASSES means**: Branch-B floor is structurally below Planck by 3.5–4.6 OOM (reconciles prompt text + direct eval). Forces A_s_Planck-match to Branch-A path exclusively.

**What FAILS means**: Floor is higher than claimed OR cannot be computed reproducibly; Branch-B path either viable OR indeterminate, forcing deeper audit of S83 G51 w_0 regulator FAIL.

**Output files**:
- Script: `computations/s84_w5_floor_conditioned_on_branch.py`
- Data: `computations/s84_w5_59_data.npz`
- Plot: `computations/s84_w5_59_plot.png` (A_s floor vs Planck, OOM annotation)
- Working paper: §W5-59
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-60. S84-KCORRIDOR-CANONICAL-PROMOTION

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW

**Trigger**: [AUDIT]
**Classification**: NON-PHONONIC (infrastructure; canonical_constants.py promotion with provenance)

**Hypothesis being tested**: 7 K-corridor constants {K_R3, K_match_need, A_s_floor_5conv, b_LB_ratio, tau_GGE_K_unit, xi_ell_plateau, K_star} currently floating across S82/S83 scripts as repeated literals. Promoting them to canonical_constants.py with full provenance eliminates hard-code drift; the `/weave --update` audit reports "Potential = 0" for K-corridor literals post-promotion.

**PASS/FAIL/INFO thresholds**:
- PASS: 7 constants added to canonical_constants.py with full 7-field provenance (name, value, unit, session-of-origin, source-document, derivation-pin, gate-id); `/weave --update` Potential count for K-corridor literals = 0.
- FAIL: fewer than 7 promoted, or any promotion missing provenance field.
- INFO: 7 promoted but 1-2 provenance fields thin (partial; would need W6 top-up).
- Tolerance: ABSOLUTE (count).

**Substitution chain**: N/A (bookkeeping gate; no direction/sign claim).

**Machinery pin (PRDR)**:
- `N_eval`: Static analysis of computations/ for K-corridor literal occurrences.
- `L_max`: N/A.
- `scan_range`: all files in computations/ matching `*s8{2,3,4}*.py`.
- `step_size`: N/A.
- `tolerance`: grep-count on each of 7 literals.
- `scheme`: N/A.
- `convention`: canonical_constants.py provenance template.
- `random_seed`: N/A.
- `GPU path`: N/A.

**Values and pre-registered provenance** (for the writer to commit):

| Constant | Value | Unit | Origin Session | Gate | Derivation |
|:--|:--|:--|:--|:--|:--|
| `K_R3` | 2.035 | dimensionless | S82 | W2-4 PS-SUBSTRATE-MATCHED-IC | Multiplicity-weighted (3/3/2) band-weight |
| `K_match_need` | 0.6366 | dimensionless | S83 | G38 K-MATCHING-5-CONVENTIONS | min K needed for Planck-match (positivity WALL) |
| `A_s_floor_5conv` | see Gate 59 | dimensionless | S83/S84 | W5-59 FLOOR-CONDITIONED-ON-BRANCH | Branch-B under R5 + Zubarev |
| `b_LB_ratio` | f_L ≥ 0.6027 | dimensionless | S83 | G39 LEGGETT-BOGOLIUBOV-PARTITION | Permanent floor across 5 OOM in K |
| `tau_GGE_K_unit` | 7.86×10⁴ (span) | τ-units | S83 | G40 TAU-GGE-AT-K | τ_GGE linear in K, machine-ε |
| `xi_ell_plateau` | 0.135 | dimensionless | S83 | G41 XI-BCS-VS-L-PHONON | K ≥ 10 plateau |
| `K_star` | 1.3130 (coth(1)) | dimensionless | S84 | W5-58 K-STAR-LAB-FRAMEWORK-MATCH | Functional-form audit resolves x* |

**Input SHA-256 pins**:
- `computations/canonical_constants.py` (current): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<promoted_count=7>, scheme=N/A, convention=canonical_constants, L_max=N/A)`

**What PASSES means**: K-corridor constants locked into canonical ledger with provenance; S85+ scripts inherit without drift.

**What FAILS means**: Promotion incomplete; K-corridor hardcode drift persists; S85 scripts re-instantiate values.

**Output files**:
- Edit: `computations/canonical_constants.py` (append 7 entries with provenance)
- Audit: `computations/s84_w5_60_kcorridor_promotion_audit.txt`
- Script: `computations/s84_w5_kcorridor_canonical_promotion.py` (dry-run promotion + audit)
- Working paper: §W5-60
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-61. GATE-R4-DISCARD-AUDIT

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: LOW

**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (convention-count audit; labels R4 as dimensional-error)

**Hypothesis being tested**: Apply the "DIMENSIONAL-ERROR-DISCARDED" tag to R4 in the S82/S83 OOM ladder and working-paper convention count. The claim "5 physical conventions" in S82 W2-4 should be relabeled to "4 physical + 1 dimensional-error (R4)". All downstream cluster-tests (S83 G15, G28, G34, G38) recomputed with 4-regulator atlas + explicit R4-excluded tag. Resolution of Gate 56 (R4-cross-class-control) feeds this: if R4 FAIL is BDI-specific (PASS W5-56), the tag is "DIMENSIONAL-ERROR-3HeB-CLASS-SPECIFIC"; if cross-class (FAIL W5-56), tag is "DIMENSIONAL-ERROR-CROSS-CLASS".

**PASS/FAIL/INFO thresholds**:
- PASS: S82 OOM ladder file updated with R4 tag; convention count updated "5 → 4 + 1 dim-err" in S82 + S83 workingpapers + S84 carry-forward.
- FAIL: S82/S83 workingpapers left with "5 conventions" unaudited.
- INFO: Tag applied but S82/S83 workingpapers not updated (audit partial).
- Tolerance: ABSOLUTE (bookkeeping).

**Substitution chain**: N/A (audit).

**Machinery pin (PRDR)**:
- `N_eval`: Grep for "5 conventions" / "5-regulator" / "R4" in S82/S83 workingpapers + OOM ladder.
- `L_max`: N/A.
- `scan_range`: `sessions/archive/session-82/`, `sessions/archive/session-83/`, `computations/s8{2,3}_*.py`.
- `step_size`: N/A.
- `tolerance`: count of un-tagged occurrences.
- `scheme`: N/A.
- `convention`: 4 physical + 1 dim-error (target).
- `random_seed`: N/A.
- `GPU path`: N/A.

**Input SHA-256 pins**:
- `sessions/archive/session-82/session-82-results-workingpaper.md`: `<computed-at-runtime>`
- `sessions/archive/session-83/session-83-results-workingpaper.md`: `<computed-at-runtime>`
- `computations/s82_oom_ladder.txt`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<untagged_count=0>, scheme=R4-audit, convention=4+1, L_max=N/A)`

**What PASSES means**: Framework convention count is honestly reported as "4 physical + 1 dim-error"; downstream cluster-test verdicts carry dim-error disclaimer.

**What FAILS means**: Untagged R4 occurrences persist; convention-count inflation continues to prop up S83 G38 K-matching FAIL at min-over-5 rather than min-over-4.

**Output files**:
- Script: `computations/s84_w5_r4_discard_audit.py`
- Audit report: `computations/s84_w5_61_r4_audit_report.txt`
- Edits: append R4 tag in S82/S83 workingpaper closures
- Working paper: §W5-61
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-62. GATE-ALPHA-S-PARTITION

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [VERIFY] [SIGN]
**Classification**: PHONONIC (Leggett-channel ξ² contribution to α_s 2nd-order)

**Hypothesis being tested**: The Leggett-channel (relative-phase mode) contributes to the 2nd-order term in the n_s−1 power expansion ln P_ζ(k) = A + (n_s−1)ln k + ((n_s−1)²/2)(ln k)² + ξ² · (ln k)² term-from-Leggett. The α_s = n_s² − 1 = −0.068968 single-parameter result (S50 permanent, S84 Gate 86) survives the f_L-weighted Leggett partition iff the Leggett contribution renormalizes INTO the n_s−1 coefficient (not as independent running). Gate computes f_L-weighted α_s and checks Planck consistency (Planck α_s = −0.0045 ± 0.0067 at k_pivot = 0.05 Mpc⁻¹).

**PASS/FAIL/INFO thresholds**:
- PASS: α_s (f_L-weighted) within 1σ of α_s (un-weighted) = −0.068968, i.e. |Δα_s|/|α_s| ≤ 0.05. AND both within 9.62σ of Planck (current α_s = n_s² − 1 distance, S84 Gate 86).
- FAIL: |Δα_s|/|α_s| > 0.20 (Leggett partition shifts α_s OOM).
- INFO: 0.05 < |Δα_s|/|α_s| ≤ 0.20.
- Tolerance: RATIO.

**Substitution chain**:
- Step 1 (definitions):
  - α_s := d n_s / d ln k at k_pivot.
  - f_L := Leggett-channel partition fraction (S83 G39 ≥ 0.6027 permanent).
  - f_B := Bogoliubov-minority partition fraction (S83 G39 ≤ 0.3973).
- Step 2 (substitution):
  - α_s_full = f_L · α_s_Leggett + f_B · α_s_Bog.
  - If α_s_Leggett = α_s_Bog = α_s_mean (channels symmetric), α_s_full = α_s_mean.
  - If channels asymmetric, α_s_full differs by Δ = f_L(α_s_Leggett − α_s_mean) + f_B(α_s_Bog − α_s_mean).
- Step 3 (simplification):
  - For ξ²-contribution specific to Leggett: α_s_Leggett = α_s_mean + ξ² · (dual scaling factor).
  - ξ := (relative-phase-mode stiffness)/(common-phase-mode stiffness) at fold. ξ² is the 2nd-order correction.
- Step 4 (direction):
  - α_s_full > α_s_mean ⟺ ξ² > 0 AND f_L > f_B (which holds permanently from G39).
  - α_s_full < α_s_mean ⟺ ξ² < 0.
  - Sign of ξ² determined by Leggett-mode Jensen curvature sign at fold (S83 G50 n_T BLUE implies convex fold, sign(ξ²) > 0 expected).

**Machinery pin (PRDR)**:
- `N_eval`: α_s via Mukhanov-Sasaki solver with explicit Leggett-Bogoliubov channel separation.
- `L_max`: 5.
- `scan_range`: k ∈ [0.005, 0.5] Mpc⁻¹, pivot at 0.05.
- `step_size`: Δln k = 0.01.
- `tolerance`: 10⁻⁴ on α_s.
- `scheme`: Zubarev.
- `convention`: R3 (band-3/3/2) + f_L/f_B partition.
- `random_seed`: 42.
- `GPU path`: `torch.linalg`.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s50_alpha_s_ns_squared.py`: `<computed-at-runtime>`
- `computations/s83_g39_leggett_bog_partition.npz`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<|Δα_s|/|α_s|>, scheme=Zubarev, convention=R3+partition, L_max=5)`

**What PASSES means**: f_L-weighted α_s is consistent with α_s = n_s²−1 single-parameter result; S50 permanent result preserved; S84 Gate 86 derivation robust.

**What FAILS means**: Leggett partition shifts α_s OOM; S50 single-parameter derivation is f_L-dependent, not unconditional. Forces audit of S50 permanence status.

**Output files**:
- Script: `computations/s84_w5_alpha_s_partition.py`
- Data: `computations/s84_w5_62_data.npz`
- Plot: `computations/s84_w5_62_plot.png` (α_s: full vs weighted vs Planck)
- Working paper: §W5-62
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-63. GATE-K-FLOOR-REACHABLE

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW-MEDIUM

**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (floor-reachability from admissible convention set)

**Hypothesis being tested**: K ∈ {1.0, 1.1, 1.3, 1.5, 1.7} from the W2-4 A_s = A_s_base · K formula covers a range that either (a) sits WITHIN the 4-admissible convention set {R1, R2, R3, R5} (all values reachable by interpolation between convention-induced K-values) or (b) is EXTRAPOLATION-ONLY (requires K-values outside any admissible convention's range, hence fundamentally unreachable).

**PASS/FAIL/INFO thresholds**:
- PASS (reachable): at least 4 of the 5 K-values {1.0, 1.1, 1.3, 1.5, 1.7} lie within the convex hull of K-values admitted by {R1, R2, R3, R5}.
- FAIL (extrapolation-only): 3 or more of 5 K-values lie outside admissible convention hull.
- INFO: 4 of 5 reachable, 1 at boundary (corridor-edge case).
- Tolerance: ABSOLUTE (count).

**Substitution chain**:
- Step 1 (definitions):
  - K_i := K-value emergent under convention R_i (i ∈ {1,2,3,5}, R4 discarded per Gate 61).
  - Admissible hull := conv{K₁, K₂, K₃, K₅} = [min K_i, max K_i].
- Step 2 (substitution):
  - From S82 W2-4: K_R3 = 2.035 (canonical). K_R1, K_R2, K_R5 TBD from convention-specific baselines. K_R5 ≈ 1.922 (S83 G38 basin).
  - Hull = [min{K_R1, K_R2, K_R5}, max{K_R1, K_R2, K_R3}].
- Step 3 (simplification):
  - Test set {1.0, 1.1, 1.3, 1.5, 1.7} membership: if hull ⊃ [1.0, 1.7], all 5 in hull ⟹ PASS.
  - If hull ⊂ [1.5, 2.5] (example), only {1.5, 1.7} in hull ⟹ FAIL.
- Step 4 (direction): Location of lower hull edge determines reachability.

**Machinery pin (PRDR)**:
- `N_eval`: K_R1, K_R2, K_R5 computation per convention (K_R3 inherited).
- `L_max`: 5.
- `scan_range`: conventions {R1, R2, R3, R5} × K ∈ [0.5, 3.0].
- `step_size`: Δ K = 0.05.
- `tolerance`: 10⁻³.
- `scheme`: Zubarev.
- `convention`: per-R; aggregate hull.
- `random_seed`: 42.
- `GPU path`: `torch.linalg`.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s82_w2_4_unified_as_79.py`: `<computed-at-runtime>`
- `computations/s83_g38_k_matching.npz`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<reachable_count/5>, scheme=Zubarev, convention=4-hull, L_max=5)`

**What PASSES means**: {1.0, 1.1, 1.3, 1.5, 1.7} is reachable interpolation-space; K-corridor low-end is physically populated by admissible conventions.

**What FAILS means**: Low-K corridor (K < 1.5) is extrapolation-only; K-corridor WALL at K_match=0.6366 is interpolation-excluded too; S83 G38 FAIL is structurally trapped.

**Output files**:
- Script: `computations/s84_w5_k_floor_reachable.py`
- Data: `computations/s84_w5_63_data.npz`
- Plot: `computations/s84_w5_63_plot.png` (K convention hull + 5-target K-values)
- Working paper: §W5-63
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-64. GATE-T-S-PARTITION-CONSISTENCY

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW-MEDIUM

**Trigger**: [VERIFY]
**Classification**: PHONONIC (Bogoliubov-minority floor × n_T cross-check)

**Hypothesis being tested**: The G39 Bogoliubov-minority floor f_B ≤ 0.3973 is an independent constraint on the G50 n_T = +0.468 BLUE prediction. Joint consistency: if n_T (tensor tilt) is driven predominantly by the Bogoliubov-channel phonon pair-creation, then the Bogoliubov-weighted n_T ≤ f_B · n_T_max must be consistent with the observed +0.468 value, AND r (tensor-to-scalar) derived from the joint partition must be consistent with S83 G46 r_CMB = 0.0117.

**PASS/FAIL/INFO thresholds**:
- PASS: n_T_computed(f_B, f_L from G39) = +0.468 ± 0.05 AND r_computed within 15% of S83 G46 r_CMB = 0.0117.
- FAIL: |n_T_computed − 0.468| > 0.2 (structural inconsistency), OR r_computed differs from 0.0117 by > 50%.
- INFO: n_T within tolerance, r within factor-3 but outside 15%.
- Tolerance: ABSOLUTE on n_T, RATIO on r.

**Substitution chain**:
- Step 1 (definitions):
  - n_T := d ln P_t / d ln k, tensor spectral tilt.
  - r := P_t/P_ζ, tensor-to-scalar ratio.
  - f_B := Bogoliubov-channel partition (G39 ≤ 0.3973).
  - f_L := Leggett-channel partition (G39 ≥ 0.6027). f_B + f_L = 1.
- Step 2 (substitution):
  - n_T_full = f_L · n_T_Leggett + f_B · n_T_Bog. From G50, n_T_full = +0.468.
  - If n_T_Leggett = 0 (Leggett mode is relative-phase, doesn't couple to transverse graviton at leading order):
    n_T_full = f_B · n_T_Bog ⟹ n_T_Bog = 0.468 / f_B.
  - With f_B = 0.3973 (upper bound): n_T_Bog_min = 0.468/0.3973 = 1.178.
  - With f_B = 0.25 (plausible mid): n_T_Bog_mid = 1.872.
- Step 3 (simplification):
  - r = 16 ε_H · (P_t/P_t_inflaton) · f_B where f_B enters because only Bogoliubov-channel sources transverse gravitons at leading order.
  - S83 G46 r_CMB = 0.0117 at ε_H = 0.02163.
  - r_computed = 16 · 0.02163 · f_B · (transfer factor).
- Step 4 (direction):
  - If f_B_inferred_from_n_T matches f_B from G39 within factor-2, consistency PASSES. If f_B_inferred > 1 (unphysical) or < 0, FAIL.

**Machinery pin (PRDR)**:
- `N_eval`: f_B inversion from n_T + r joint observables via 2-parameter fit.
- `L_max`: 5.
- `scan_range`: f_B ∈ [0.1, 0.4] (within G39 ≤ 0.3973 floor + margin).
- `step_size`: Δ f_B = 0.01.
- `tolerance`: 10⁻³ on n_T, 5×10⁻⁴ on r.
- `scheme`: Zubarev.
- `convention`: R3 + G39 partition.
- `random_seed`: 42.
- `GPU path`: `torch.linalg`.

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s83_g39_leggett_bog_partition.npz`: `<computed-at-runtime>`
- `computations/s83_g50_n_T_magnitude.npz`: `<computed-at-runtime>`
- `computations/s83_g46_tensor_transfer_k_cmb.npz`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<|f_B_inferred - f_B_G39|/f_B_G39>, scheme=Zubarev, convention=R3+partition, L_max=5)`

**What PASSES means**: G39 f_B floor, G50 n_T magnitude, G46 r_CMB form a closed triangle — joint consistency confirmed; tensor-sector is Bogoliubov-channel-dominated.

**What FAILS means**: One of {G39, G50, G46} is inconsistent with the other two under joint partition; forces re-audit of one verdict.

**Output files**:
- Script: `computations/s84_w5_t_s_partition_consistency.py`
- Data: `computations/s84_w5_64_data.npz`
- Plot: `computations/s84_w5_64_plot.png` (f_B inferred from n_T/r vs G39 floor)
- Working paper: §W5-64
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-65. GATE-K-FIRAS-COINCIDENCE

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [VERIFY-THEOREM] [AUDIT]
**Classification**: PHONONIC (structural vs numerical identity test for K_FIRAS)

**Hypothesis being tested**: The quantity K_FIRAS := 2.035 · μ_FIRAS / μ(K=2.035) and the quantity S_IC^cap = 3.556×10⁵ either (a) satisfy a structural identity (within 1% at L_max=5 and consistent to higher L_max), making K_FIRAS = S_IC^cap a closed-form relation between FIRAS bound + GGE-relic k-scale + substrate-native IC saturation, or (b) are numerically coincident at 1% but derivatively uncorrelated (coincidence).

**PASS/FAIL/INFO thresholds**:
- PASS (structural): |K_FIRAS − S_IC^cap| / S_IC^cap ≤ 0.01 AND ratio stable under L_max scan {5, 7, 9} (drift ≤ 0.5% per L-step).
- FAIL (not coincident): |K_FIRAS − S_IC^cap| / S_IC^cap ≥ 0.10 — the quantities are not even numerically close.
- INFO (coincidence, not structural): ratio ≤ 0.01 at L_max=5 but drift > 5% under L_max scan (numerical coincidence, not structural identity).
- Tolerance: RATIO + stability.

**Substitution chain**:
- Step 1 (definitions):
  - μ_FIRAS := 9×10⁻⁵ (FIRAS 2σ bound).
  - μ(K=2.035) := μ-distortion at K=2.035 (from S82 FIRAS-CHLUBA-FULL PASS, 4.98×10⁻¹⁰).
  - K_FIRAS := 2.035 · μ_FIRAS / μ(K=2.035) = 2.035 · 9×10⁻⁵ / 4.98×10⁻¹⁰.
  - S_IC^cap := 3.556×10⁵ (substrate-native IC saturation cap).
- Step 2 (substitution):
  - K_FIRAS = 2.035 · 9×10⁻⁵ / 4.98×10⁻¹⁰ = 2.035 · 1.807×10⁵ = 3.678×10⁵.
  - S_IC^cap = 3.556×10⁵.
  - Ratio |3.678 − 3.556|/3.556 = 0.0343 (3.43%). At L_max=5, within ~3.5% — INFO boundary; structural iff this tightens under L_max scan.
  - (Arithmetic verified at plan-write time: (2.035 × 9×10⁻⁵)/(4.98×10⁻¹⁰) = 1.8315×10⁻⁴/4.98×10⁻¹⁰ = 3.677×10⁵. Ratio = 0.0341.)
- Step 3 (simplification): If the identity is structural, there exists a closed-form K_FIRAS = f(L_max) · S_IC^cap with f → 1 as L_max → ∞; the 3.4% residual at L_max=5 is a truncation signature.
- Step 4 (direction): Direction of residual under L_max = {5, 7, 9} scan determines structure:
  - Monotone decrease to <1% ⟹ structural identity (PASS at L_max → ∞).
  - Flat residual ~3% across L_max ⟹ numerical coincidence (INFO).
  - Increasing residual ⟹ FAIL.

**Machinery pin (PRDR)**:
- `N_eval`: μ(K=2.035) recomputed at L_max ∈ {5, 7, 9}. S_IC^cap reconstructed at each L_max.
- `L_max`: {5, 7, 9}.
- `scan_range`: N/A (point eval at each L).
- `step_size`: N/A.
- `tolerance`: 10⁻⁴ on μ; 10⁻³ on S_IC^cap.
- `scheme`: Zubarev.
- `convention`: R3 (band-3/3/2).
- `random_seed`: 42.
- `GPU path`: `torch.linalg` mandatory at L_max=9 (matrices ≥1000×1000).

**Input SHA-256 pins**:
- `canonical_constants.py`: `<computed-at-runtime>`
- `computations/s82_firas_chluba_full.npz`: `<computed-at-runtime>`
- `computations/s82_w2_4_ps_substrate_matched_ic.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<ratio_and_drift>, scheme=Zubarev, convention=R3, L_max={5,7,9})`

**What PASSES means**: K_FIRAS = S_IC^cap is a closed-form identity; FIRAS bound IS the substrate-native IC saturation cap translated to K-scale; new permanent theorem candidate for §VII registry.

**What FAILS means**: 3.4% residual is not structural; K_FIRAS and S_IC^cap are disconnected quantities with a numerical coincidence at 2 significant figures.

**Output files**:
- Script: `computations/s84_w5_k_firas_coincidence.py`
- Data: `computations/s84_w5_65_data.npz`
- Plot: `computations/s84_w5_65_plot.png` (ratio vs L_max)
- Working paper: §W5-65
- Verdict line: `s84_gate_verdicts.txt`

---

## §W5-66. GATE-LANDAU-SYMMETRY-CLASS

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC (Landau classification: symmetry group, broken subgroup, order parameter, universality class of K-corridor)

**Hypothesis being tested**: The K-corridor is a 1-parameter order-parameter manifold admitting a Landau classification with:
- **Symmetry group G** (unbroken): at K → ∞ single-mode fine-structure limit.
- **Broken subgroup H** (at finite K): substrate band-mixing reduces G → H.
- **Order parameter φ**: coset G/H elements parameterized by K.
- **Universality class**: matches known 3He-B parent (BDI, O(N) for N=5 order-parameter components).

**PASS/FAIL/INFO thresholds**:
- PASS: All 4 Landau invariants identified; universality class matches 3He-B BDI with correct N (5-component order parameter for 3He-B per Volovik 2003 Ch. 7).
- FAIL: No consistent G/H decomposition exists (corridor is not 1D OP manifold); or universality class incompatible with 3He-B BDI.
- INFO: G/H identified but N mismatch (e.g., N=4 or N=6 instead of 5) — inheritance partial.
- Tolerance: STRUCTURAL (theorem-level).

**Substitution chain**:
- Step 1 (definitions):
  - G (unbroken) = symmetry group of substrate at K → ∞.
  - H ⊂ G = stabilizer of K-finite band-weighting.
  - Order parameter φ ∈ G/H.
  - Universality class = (AZ class, order-parameter dimension N, spatial dimension d).
- Step 2 (substitution):
  - Framework substrate: SU(3) gauge × O(3) rotational × T (time-reversal) × (U(1) × U(1)_rel) phase symmetries at generic fiber.
  - At K → ∞ (fine-structure limit): single-mode excitation preserves SU(3) × O(3) × T. Broken: (U(1) × U(1)_rel) phase → ℤ₂ relative-phase locked.
  - At K finite: band-mixing breaks SU(3) → SU(2)×U(1) residual; O(3) → O(2) axial; T preserved (BDI T²=+1).
  - Coset G/H = SU(3)/SU(2)×U(1) × O(3)/O(2) × U(1)_rel/ℤ₂ × K (dilation).
  - dim(G/H) = 4 (SU(3)/SU(2)xU(1)) + 2 (O(3)/O(2)) + 1 (U(1)_rel/ℤ₂) + 1 (K) − (discrete) = 8 real components? Substrate confirmation needed.
- Step 3 (simplification):
  - 3He-B has 5-component order parameter (Volovik 2003 Ch. 7 + 8): 3 rotations + 1 relative phase + 1 ℤ₂ (+ mass gap modulus).
  - Framework's dim(G/H) must be compared: if 5 ⟹ match; if 8 ⟹ over-inheritance (framework has more components than 3He-B parent, inheritance partial-INFO).
- Step 4 (direction): Result of dim(G/H) = N determines Landau-class match.

**Machinery pin (PRDR)**:
- `N_eval`: Representation-theoretic decomposition of SU(3) × O(3) × U(1)² under band-weighting + T.
- `L_max`: N/A (representation-theoretic).
- `scan_range`: None (symbolic + numerical rep check).
- `step_size`: N/A.
- `tolerance`: ABSOLUTE (integer N).
- `scheme`: Landau-Ginzburg effective functional.
- `convention`: Volovik 2003 Ch. 7 3He-B order-parameter convention.
- `random_seed`: N/A.
- `GPU path`: N/A (analytical).

**Input SHA-256 pins**:
- `researchers/Volovik/volovik-2003-universe-in-a-helium-droplet.md` Ch. 7: `<computed-at-runtime>`
- `sessions/archive/session-83/session-83-landau-synthesis.md` §V: `<computed-at-runtime>`
- `.claude/agent-memory/volovik-superfluid-universe-theorist/framework-3heb-comparison.md`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<(G_symbol, H_symbol, N_OP, class)>, scheme=Landau-Ginzburg, convention=Volovik-2003-Ch7, L_max=N/A)`

**What PASSES means**: K-corridor is a Landau 1-parameter OP manifold with 3He-B BDI universality; parent-child inheritance holds at the symmetry-classification level. Feeds Gate 56 (cross-class control) interpretation.

**What FAILS means**: No consistent G/H decomposition, or universality class is NOT BDI. Forces reinterpretation of 3He-B inheritance as analogy (not parent-child).

**Output files**:
- Script: `computations/s84_w5_landau_symmetry_class.py`
- Data: `computations/s84_w5_66_data.npz` (contains G, H symbols, N, class)
- Plot: `computations/s84_w5_66_plot.png` (G/H decomposition diagram)
- Working paper: §W5-66
- Verdict line: `s84_gate_verdicts.txt`

---

## Wave 5 → Wave 6 Decision Point

**After all 14 Wave-5 verdicts land**:

1. **If W5-53 PASS AND W5-54 PASS** (dynamics-layer rescue accessible + regulator-invariant):
   - K-corridor is a viable A_s_Planck-match path via NNLO→N3LO; forward to Wave 6 a dedicated "K=2.035 baseline-layer tightening" gate, even though S83 G11 NNLO was 250× short.

2. **If W5-53 FAIL AND W5-54 PASS** (dynamics saturates, floor regulator-invariant):
   - Promote "dynamics-WALL-at-2.035" to permanent-results-registry; A_s closure forced to baseline-layer (H_tilde DC path) exclusively. Wave 6 opens H_tilde sensitivity-refinement gate.

3. **If W5-55 FAIL** (n_s non-monotone across K):
   - K-corridor is NOT 1D Landau OP manifold; invalidate Gate 66 PASS presumption; escalate to W6 full Landau-class re-derivation with multi-valued OP.

4. **If W5-56 FAIL** (R4 cross-class):
   - 3He-B inheritance is weaker than assumed; Gate 66 class assignment may be BDI → AIII crossover; escalate to W6 universality-class boundary gate.

5. **If W5-58 FAIL OR Gate 66 FAIL**:
   - 3He-B parent-child inheritance breaks at corridor boundary; agent memory `project_3heb-inheritance.md` requires update to "analogy, not inheritance"; full framework-level re-audit of all 3He-B-derived conclusions.

6. **If W5-65 PASS** (K_FIRAS = S_IC^cap structural):
   - New permanent theorem candidate (FIRAS-IC-IDENTITY) for §VII registry; Wave 6 formalization gate.

7. **If W5-63 FAIL** (K-floor extrapolation-only):
   - S83 G38 K_match WALL is interpolation-exclusion-reinforced; combine with W5-59 floor-under-R5 to promote "K-floor-WALL" as joint permanent result.

8. **If W5-60 FAIL** (canonical promotion incomplete):
   - Block W6 K-corridor gates until provenance is complete (pre-registration bookkeeping).

9. **Default (mixed)**: Retain K-corridor as open structural theme; carry mixed verdicts to W6 as per-gate decision rules.

---

## Wave 5 Machinery-Enumeration Pin (§0.11)

Per the PRDR requirement (`.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness), every Wave-5 gate pre-registers its machinery above. Consolidated enumeration:

| Gate | N_eval | L_max | scan | scheme | convention | GPU | SHA-pinned inputs |
|:--|:--|:--|:--|:--|:--|:--|:--|
| W5-53 | 1/N orders LO..N3LO | 5 | N_field ∈ {1,2,4,8,16} | Zubarev | R1 (K=2.035) | torch.linalg | canonical_constants, G7, G11, S82-W2-4 |
| W5-54 | A_s(K;reg) | 5 | K ∈ [0.5,3.0], Δln K=0.1 | Zubarev, zeta | R5, 4-reg atlas | torch.linalg | canonical_constants, UNIFIED-AS-79, G38 |
| W5-55 | n_s(K) | 5 | K ∈ {1.1, 2.035, 10, 100, 1e3, 3.556e5} | Zubarev | R3 | torch.linalg | canonical_constants, MATCHED-IC, MS-solver |
| W5-56 | R4 in 2 classes | N/A | point | dim-conv | R4 BDI+AIII | — | canonical_constants, Volovik-2003, S82-R4 |
| W5-57 | μ(K) | 5 | K ∈ {1.1, 2.035, 10, 100, 1e3, 3.556e5} | Zubarev | R3 | torch.linalg | canonical_constants, FIRAS-CHLUBA, Chluba-kernel |
| W5-58 | K_* audit | N/A | x* ∈ {0.5, 1.0, 2τ_fold, 1/Δ_BCS} | N/A | Volovik-3HeB | — | canonical_constants, Volovik-2003, prompt |
| W5-59 | A_s at K_R5 | 5 | point | Zubarev | R5 | torch.linalg | canonical_constants, UNIFIED-AS-79, G38 |
| W5-60 | static grep | N/A | computation/s8{2,3,4}*.py | N/A | canonical_constants provenance | — | canonical_constants |
| W5-61 | grep | N/A | S82, S83 WPs + OOM ladder | N/A | 4+1 convention | — | S82-WP, S83-WP, OOM-ladder |
| W5-62 | α_s(f_L,f_B) | 5 | k ∈ [0.005, 0.5] Mpc⁻¹, Δln k=0.01 | Zubarev | R3+partition | torch.linalg | canonical_constants, S50, G39 |
| W5-63 | K_R1/R2/R5 hull | 5 | {R1,R2,R3,R5} × K ∈ [0.5,3.0] | Zubarev | 4-hull | torch.linalg | canonical_constants, UNIFIED-AS-79, G38 |
| W5-64 | f_B inversion | 5 | f_B ∈ [0.1, 0.4], Δ=0.01 | Zubarev | R3+partition | torch.linalg | canonical_constants, G39, G50, G46 |
| W5-65 | ratio + drift | {5,7,9} | point at each L | Zubarev | R3 | torch.linalg (L=9) | canonical_constants, FIRAS-CHLUBA, MATCHED-IC |
| W5-66 | rep-theory decomp | N/A | symbolic | Landau-Ginzburg | Volovik-3HeB Ch.7 | — | Volovik-2003, S83-landau §V, agent-memory |

All 14 gates have no unpinned machinery parameters (PRU Class-8-compliant).

---

## Wave 5 Input-SHA Ledger

Every Wave-5 script logs SHA-256 of every input file in its first 20 stdout lines and emits a single closure hash (per `.claude/rules/gate-verdicts.md` S81+ canonical form). Closure hash = SHA-256 of the ordered input-pin map (name → content-hash concatenation).

Common inputs (most gates):
- `canonical_constants.py` (frozen at S83-close): `<content-hash at runtime>`
- `researchers/Volovik/volovik-2003-universe-in-a-helium-droplet.md`: `<runtime>`

Gate-specific inputs listed in each §W5-N block above.

S84 schema_version 2 introduces dual-SHA (`audit_sha256` + `content_sha256`) per S83 G99 (CF-SHA-SPLIT), landing in W1 of Wave 1; W5 gates inherit the dual-SHA schema once Wave 1 infrastructure completes.

Verdict-line format (per gate):

```
W5-{53..66}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<64-char-closure>
```

Appended to `computations/s84_gate_verdicts.txt`.

---

**End of Wave 5 Plan.**

14 gate blocks above; no gate ID collides with S83 IDs (all prefixed `S84-` or `GATE-` per prompt-assigned IDs; internal §W5-NN references are Wave-5-local identifiers for working paper cross-reference). Gates are parallel-independent; no intra-wave dependency. Verdict-convergence feeds Wave-5→Wave-6 decision point above.
