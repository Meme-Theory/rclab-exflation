# Session 85 Plan — Wave W0: Cross-reviewer high-convergence (conv ≥ 2)

**Wave ID**: W0
**Owner**: gen-physicist (breadth workhorse)
**Item count**: 24
**Concurrency cap**: self-imposed ≤ 8 dispatches live at any moment
**Output script prefix**: `computations/s85_w0_<slug>.py`
**Verdict file (canonical)**: `computations/s85_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md`)
**Plan generated**: 2026-04-21

## Wave W0 Summary

Wave W0 is the cross-reviewer high-convergence wave of Session 85: 24 carry-forward items that ≥ 2 S84 reviewers independently pre-registered. These are the HIGHEST-PRIORITY of S85 because they are the only items whose demand is ratified by multiple independent review lenses. Headline items are `S85-BETA-S-CMB-S4-PREREG` (conv = 6: all of connes / feynman / landau / mack / tesla / transit pre-registered β_s = −0.1331 as the single most important CMB-S4 flagship gate in S84) and `FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE` (conv = 5: little-red-dots / mack / tesla / transit plus the feynman DETECTOR-STERILE carry-forward, the sole surviving non-Gaussianity channel after S83 elimination). The wave also contains CC-series closure computations (CC-1 η-invariant, CC-2 Spin(8) triality, CC-3 Connes-Moscovici signed-residue, CC-4 Dai-Freed, CC-5 L_max≥11 refit), infrastructure hardening (HOOK-WIRING + R3 YAML normalization), and PRDR-lineage audits (PLAN-DISCIPLINE-VAN-HOVE-CHECK).

Every gate in this wave follows the 13-field structure per `/rclab-plan` §3b: Gate ID → Trigger → Classification → Agent → Hypothesis → Method (self-contained dispatch prompt) → Machinery pin (PRDR) → Expected output 4-tuple → Thresholds → Substitution chain (for [SIGN]/[VERIFY]) → Implications → Effort → Substrate-framing reminder. Substrate framing is mandatory in every dispatch prompt: particles are phononic excitations of D_K on Jensen-SU(3); space emerges from a_2 Seeley-DeWitt; geometry is derived from the spectral moments, never vice versa.

## Wave W0 Decision Point Prerequisites

W0 is the first wave of Session 85 and has no W-wave prerequisites. However, several W0 outputs feed downstream waves:

- **W0-1 (BETA-S-CMB-S4-PREREG)** → W1a/W1b (mack alpha-s preregistrations), W4 (little-red-dots independence augment)
- **W0-2 (FOLDED-BISPECTRUM-21CM-SHAPE)** → W9 (feynman DETECTOR-STERILE sibling gate)
- **W0-3 (CC-5)** → W5 (lizzi HP^0 comparison), W11 (van-den-dungen structural audit)
- **W0-4 (DR3-REGULATOR-SUCCESSOR)** → W1a-M4 (LISA CGWB), W10 (kaku R_842 reaudit)
- **W0-6 (VAN-HOVE-CUSP-THEOREM)** → W0-22 (PLAN-DISCIPLINE-VAN-HOVE-CHECK), W10 (TAU-FOLD-UNIQUENESS)
- **W0-22 (PLAN-DISCIPLINE-VAN-HOVE-CHECK)** → feeds the v3-closure-audit at session close

Downstream waves are cleared to dispatch when their specific W0 prerequisite lands a verdict line; they should not block on the full W0 batch completion.

---

## §W0-1. S85-BETA-S-CMB-S4-PREREG

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge
**Hypothesis**: The framework-predicted running-of-the-running β_s = −0.1331 (derived from spectral moments of D_K at the electroweak τ_fold slice of Jensen flow) is observationally pre-registered against CMB-S4's forecast σ(β_s) ≈ 2.2 × 10⁻³, yielding a 60σ discriminator for the substrate's second-derivative spectral prediction.
**Method**: Write `s85_w0_beta_s_cmb_s4_prereg.py` that (a) imports β_s from `canonical_constants.py` (add `beta_s = -0.1331` with source "S84-W6 beta_s closure, BETA-S-CMB-S4-PREREG, sha256 pinned to S84-W6 verdict" via `update_constant(...)` if not present); (b) loads the CMB-S4 forecast covariance matrix for (α_s, β_s) from the CMB-S4 Science Book, with σ(β_s) = 2.2e-3 as published; (c) computes the pull p = |β_s_framework − 0| / σ(β_s_forecast) under LCDM null; (d) emits a canonical verdict line + dual-SHA audit row; (e) writes `s85_w0_beta_s_cmb_s4_prereg.npz` with `(beta_s_framework, sigma_forecast, pull, threshold_list)` and `.png` showing the β_s posterior band against LCDM zero. Substrate framing: β_s is NOT a parameter of an inflaton potential — it is the second spectral moment of D_K's Mellin-balance structure at the τ_fold slice; LCDM's β_s ≈ 0 is the substrate's absence-of-curvature prediction in a field-theoretic limit.
**Machinery pin (PRDR)**: L_max=8 (canonical); scheme=MS-bar mellin-balance; convention=Planck-central (n_s=0.9649); σ(β_s) source=CMB-S4-Science-Book-v2-2022-Table-6.1; random_seed=42; GPU path=none (scalar pull); numpy thread cap OMP_NUM_THREADS=8.
**Input SHA pins**: S84 W6 β_s closure verdict line SHA (computed-at-runtime); canonical_constants.py SHA; CMB-S4 Table 6.1 cached values (static hash).
**Expected output 4-tuple**: (value=60.5, scheme=MS-bar, convention=Planck-central, L_max=8)
**Thresholds**: PASS if pull ≥ 5 (5σ discriminator floor); INFO if 2 ≤ pull < 5 (observable but sub-decisive); FAIL if pull < 2 (registration useless). RATIO tolerance ±2% on σ_forecast.
**Substitution chain**:
  Step 1: β_s_framework = −0.1331 [def., S84 W6 closure]
  Step 2: σ_forecast = 2.2 × 10⁻³ [def., CMB-S4 Science Book Table 6.1]
  Step 3: H_0 (LCDM null): β_s = 0
  Step 4: pull = |β_s_framework − 0| / σ_forecast
  Step 5: Substitute: pull = |−0.1331| / 2.2e-3 = 0.1331 / 0.0022
  Step 6: Simplify: pull = 60.5
  Step 7: Direction: pull ≫ 5 ⇒ PASS regime; CMB-S4 measurement of β_s will discriminate framework from LCDM at ≥ 60σ.
**Implications**: PASS ⇒ CMB-S4 (launch 2028) becomes a decisive falsifier of the framework's second-spectral-moment prediction; observation delivers the single-largest-EVOI measurement in the S85+ landscape. FAIL (pull < 2) ⇒ the β_s value from S84 W6 is not observationally distinguishable from LCDM null at CMB-S4 — the framework's β_s corridor must be tightened or the gate reclassified as structural-only.
**Effort**: 1 hour (scalar computation + pre-registration write-up); CPU-only.
**Substrate-framing reminder in dispatch**: β_s is the second spectral moment at the τ_fold slice of the Jensen flow — IS space, not IN space. The LCDM "running-of-running" is a field-theoretic projection of the substrate's Mellin-cone geometry; we are pre-registering the substrate's inevitable consequence, not fitting a parameter to data.

---

## §W0-2. S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: transit-dynamics-theorist
**Hypothesis**: The framework's folded-triangle 21-cm bispectrum SHAPE template (B_fold ∝ k₃² / (k₁ k₂)) is distinguishable from LCDM's equilateral/local templates at l_max = 10⁵ with sufficient SKA-Phase-2 sensitivity (σ(f_NL^fold) ≈ 0.1) to constitute the sole surviving non-Gaussianity discriminator after the S83 non-Gaussianity elimination.
**Method**: Write `s85_w0_folded_bispectrum_21cm_shape.py` that (a) constructs the folded-triangle SHAPE kernel S_fold(k₁, k₂, k₃) from the transit acoustic-folding geometry (pre-post-transit k-correlations of the GGE relic), (b) computes the cosine-similarity inner product ⟨S_fold, S_equil⟩ / (‖S_fold‖ ‖S_equil‖) and ⟨S_fold, S_local⟩ in the l_max = 10⁵ Fisher-weighted basis, (c) computes the detectability σ(f_NL^fold) at SKA-Phase-2 and CMB-S4 via the Fisher matrix, (d) emits canonical verdict + dual-SHA. Use torch.linalg on GPU for the Fisher matrix construction at l_max = 10⁵ (matrices ≈ 10³ × 10³ in multipole-binned basis).
**Machinery pin (PRDR)**: l_max=1e5, l_min=10, k_grid_N=512, k_binning=logarithmic, detector_noise_model=SKA-Phase-2-fiducial-2030 (σ_21cm_per_pixel from Cohen et al. 2017), cosine_similarity_convention=Babich+Creminelli 2004 Eq. 29, f_NL^fold_reference=1.0 (unit normalization), Fisher_rank_floor=0.9 (min condition), L_max_spectral=8, GPU=torch 2.9.1+rocm, device=cuda:0.
**Input SHA pins**: canonical_constants.py SHA; SKA Phase-2 noise model file hash; Cohen 2017 template library hash (static).
**Expected output 4-tuple**: (value=σ(f_NL^fold)=0.08, scheme=Babich-Creminelli-2004, convention=Fisher-cosine, L_max=8)
**Thresholds**: PASS if σ(f_NL^fold) ≤ 0.2 AND cosine-overlap with (equilateral, local) both < 0.3 (template orthogonality) AND SKA-Phase-2 detectability at ≥ 3σ for |f_NL^fold| ≥ 1; INFO if PASS-detectability but overlap ∈ [0.3, 0.5]; FAIL if overlap > 0.5 (template is a linear combination of existing LCDM shapes, not sole-surviving).
**Substitution chain**:
  Step 1: S_fold(k₁, k₂, k₃) = k₃² / (k₁ k₂) with k₃ = k₁ + k₂ folded limit [def., transit acoustic geometry]
  Step 2: S_equil, S_local from Babich-Creminelli [def., standard templates]
  Step 3: overlap(A, B) = ⟨A, B⟩_Fisher / (‖A‖_Fisher · ‖B‖_Fisher) [def.]
  Step 4: σ(f_NL^fold) = (F_Fisher^{-1})_{ff}^{1/2} under the full template basis [def.]
  Step 5: Direction: the folded template is sole-surviving iff overlap-with-LCDM-basis < 0.3 AND detectability σ(f_NL^fold) ≤ 0.2 at SKA-2 [criterion from S83 post-mortem].
**Implications**: PASS ⇒ SKA-Phase-2 21-cm is the unique observational falsifier of the framework's non-Gaussianity channel; this becomes the ~2035 flagship prediction. FAIL (overlap-dominated) ⇒ the folded template is degenerate with existing LCDM primordial NG and provides no independent constraint; the framework's non-Gaussianity channel is observationally closed (non-distinguishable).
**Effort**: 4 hours (SHAPE construction + Fisher matrix build + SKA-2 noise modeling); GPU.
**Substrate-framing reminder**: The folded triangle is NOT a perturbative expansion around a field background — it is the k-space signature of pre/post-transit acoustic causal disconnection. Think "interference pattern of GGE excitations across the fold", not "squeezed-limit inflaton NG".

---

## §W0-3. S85-CC-5-LMAX-ASYMPTOTIC-REFIT

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The CC-5 cluster-span multiplicative constant — whose L_max=8 value fell short of the conjectured closed form — converges under L_max ≥ 11 asymptotic refit to within the target band derived from the multiplicative spectral-triple identity, closing W3-31's unresolved corridor.
**Method**: Write `s85_w0_cc5_lmax_refit.py` that (a) loads the D_K eigenvalue spectrum at L_max ∈ {8, 9, 10, 11, 12} (build via `_build_DK.py` helper; cache hashes); (b) computes the CC-5 cluster spans at each L_max, extracts the span-weighted multiplicative constant C_5(L); (c) fits the 1/L²-asymptotic model C_5(L) = C_5^∞ + α/L² + β/L⁴ via weighted least squares; (d) emits the extrapolated C_5^∞ with uncertainty and compares to the conjectured closed-form target from W3-31. Use torch.linalg.eigh on GPU for L_max ≥ 9 (matrices > 10⁴ × 10⁴).
**Machinery pin (PRDR)**: L_max ∈ {8, 9, 10, 11, 12}; cluster-span definition=W3-31 canonical (spans over triality orbits of 2.7% chi_2 shells); fit_model_per_series=span_k(L) = A_k · L^(b_pow_k) + α_k/L² (Zubarev sub-leading correction); fit_weights=inverse variance from diagonal Hessian; structural_identity_target=b_pow(span_2) / b_pow(span_3) = 2.000 exactly (W3-31 machine-precision finding, S84 session-84-w3-workingpaper.md §W3-31 PASS); identity_tolerance_RATIO=1e-3 (W3-31 observed 0.1% match at L∈{3,5,7,9}, must survive extension to L∈{8..12}); second_identity_target=b_pow(span_3) / b_pow(span_1) = 3/2 (S83 G4 Mellin-linear anchor, cross-check only); GPU path=torch.linalg.eigh on cuda:0; eigensolver_tol=1e-10.
**Input SHA pins**: D_K eigenvalue caches at each L_max (static hashes); S84 W3-31 NPZ sha=06ffd14b8827861781e17565b9db4e2b63cadb98836a04a5cb814758cd178d30 (for L∈{3,5,7,9} baseline b_pow values).
**Expected output 4-tuple**: (value=|b_pow(span_2)/b_pow(span_3) − 2.000|, scheme=triality-orbit-cluster, convention=multiplicative, L_max=12)
**Thresholds**: PASS if |b_pow(span_2)/b_pow(span_3) − 2.000| ≤ 1e-3 AND fit R² ≥ 0.99 for all three span series AND b_pow values monotonic-convergent across L∈{8..12} (drift < 5% from L=10 to L=12); INFO if structural identity holds at 1e-3 < tol ≤ 1e-2 (converging but not yet at machine-precision asymptote); FAIL if |ratio − 2.000| > 1e-2 OR R² < 0.99 on any series OR b_pow non-convergent on L∈{8..12}. RATIO tolerance explicit.
**Substitution chain**: This is [VERIFY-THEOREM] — the chain is the L_max asymptotic expansion derivation, written in the working paper §VI.
**Implications**: PASS ⇒ CC-5 conjecture is theorem-grade; closes W3-31 carry-forward and promotes the multiplicative identity to the permanent results registry. FAIL ⇒ either the conjectured closed form is wrong, or a higher-order L term is missed; triggers a carry-forward re-audit of the cluster-span definition under a different triality-orbit truncation.
**Effort**: 6 hours (eigenvalue builds at L=9-12 dominate runtime; L=12 is ~45 minutes on the RX 9070 XT); GPU.
**Substrate-framing reminder**: CC-5 cluster spans are substrate-geometric: they are the triality-orbit-weighted moments of the D_K spectrum, with no field-theoretic analog. "Cluster" means eigenvalue cluster within the Jensen deformation; "span" means the multiplicative structure of the NCG cohomology.

---

## §W0-4. S85-DR3-REGULATOR-SUCCESSOR-TREE

**Trigger**: [VERIFY]
**Classification**: META
**Agent**: mack-cosmic-bridge
**Hypothesis**: The DR3 regulator-conditional successor tree — a branched decision map where each DESI-DR3 ring-down outcome (accept/reject of binary R_842 containment firing on 2026-04-23) selects one branch of the 5-regulator atlas as the live predictor — is complete, covers the full regulator space, and pre-registers the W3+ iteration path with zero free parameters per branch.
**Method**: Write `s85_w0_dr3_regulator_successor.py` that (a) enumerates the 5-regulator atlas from W4-44 (cache pinned to S84), (b) constructs the branch tree: for each of {accept_R842, reject_R842, indeterminate} outcomes, map which regulators survive, which are eliminated, and which forecast remains live; (c) verifies the tree is exhaustive (covers all 3 × 5 = 15 leaf states), (d) pre-registers each leaf's S85+ prediction as a canonical entry, (e) emits the tree structure as JSON with per-leaf verdicts and an overall verdict line for the tree's completeness.
**Machinery pin (PRDR)**: regulator_atlas_source=W4-44 canonical 5-regulator list; dr3_firing_date=2026-04-23 (hard-pinned from canonical_constants or project state); outcome_set={accept, reject, indeterminate}; containment_threshold=R_842 binary from canonical_constants; tree_completeness_rule=every leaf has a forecast OR an explicit "regulator eliminated" flag; GPU path=none.
**Input SHA pins**: W4-44 regulator atlas file; S84 CF-M1 DR3 live-watch spec.
**Expected output 4-tuple**: (value=tree_leaves=15, scheme=regulator-tree, convention=DR3-conditional, L_max=8)
**Thresholds**: PASS if tree covers 15/15 leaves AND each leaf has a deterministic forecast (no "TBD" labels); INFO if 12-14/15 covered; FAIL if < 12/15.
**Substitution chain**: [VERIFY] — chain is the enumeration and exhaustive proof in the working paper §VII.
**Implications**: PASS ⇒ DR3 2026-04-23 firing has a pre-registered decision framework, eliminating post-hoc regulator-shopping on the DESI release. FAIL ⇒ the atlas is incomplete or the branch map has ambiguities; triggers a W1a-M2 carry-forward re-dispatch.
**Effort**: 2 hours; CPU-only.
**Substrate-framing reminder**: Regulators are parametrizations of the substrate's Mellin-cone truncation; DESI-DR3 is a substrate probing substrate event (acoustic perturbation from observation). Each regulator branch corresponds to a different projection of the D_K spectral action's renormalization flow at the τ_fold slice.

---

## §W0-5. S85-F_CONV-TWO-LOOP-Z_R-INVESTIGATION

**Trigger**: [VERIFY]
**Classification**: GEOMETRIC
**Agent**: feynman-theorist
**Hypothesis**: The two-loop Z_R correction to f_conv at the fiber-transition scale is either (a) identically zero by a spectral-triple identity, (b) numerically sub-dominant to the 1-loop value by ≥ factor 100 (scheme-independent), or (c) finite and large enough to re-open the W6 D.1 scheme-dependence concern — and the case must be decided from first principles by direct two-loop computation, not convention.
**Method**: Write `s85_w0_two_loop_z_r.py` that (a) sets up the two-loop Z_R Feynman integrand in the MS-bar scheme for the Jensen-SU(3) fiber sector, (b) evaluates via Mellin-Barnes reduction and zeta-regularization (use sympy/mpmath for analytic; fall back to torch.quad for numerical), (c) compares Z_R^(2-loop) / Z_R^(1-loop), (d) cross-checks against the lattice-scheme (t'Hooft) to confirm scheme-independence of the ratio direction, (e) emits verdict + dual-SHA.
**Machinery pin (PRDR)**: scheme_primary=MS-bar; scheme_cross_check=t'Hooft-lattice; integrand_representation=Mellin-Barnes; regularization=zeta; precision=mpmath.mp.dps=50; numerical_fallback_N=1e6; L_max=8; GPU path=none (scalar integral); seed=42.
**Input SHA pins**: canonical_constants.py; W6 D.1 1-loop Z_R reference verdict; Jensen-SU(3) fiber Lagrangian file.
**Expected output 4-tuple**: (value=Z_R^(2)/Z_R^(1), scheme=MS-bar, convention=zeta-reg, L_max=8)
**Thresholds**: PASS-(a) if |Z_R^(2)/Z_R^(1)| < 1e-10 (identically-zero test); PASS-(b) if |ratio| < 0.01 (sub-dominant) AND cross-check ratio differs by < 10% (scheme-independent direction); INFO if 0.01 ≤ |ratio| < 0.1; FAIL if |ratio| ≥ 0.1 (re-opens scheme dependence).
**Substitution chain**:
  Step 1: Z_R^(n-loop) = integrand with n loop momenta in the fiber sector [def.]
  Step 2: ratio = Z_R^(2) / Z_R^(1) [def.]
  Step 3: scheme-independence direction: if |ratio_MS − ratio_tHooft| / ratio_MS < 10%, direction is scheme-independent.
  Step 4: Plug in computed numerical values from the script (post-compute; direction claim is the OUTPUT, not a pre-claim).
**Implications**: PASS-(a) ⇒ a new spectral-triple identity was discovered; promote to registry. PASS-(b) ⇒ f_conv 1-loop is the canonical value, scheme-dependence is closed. FAIL ⇒ W6 D.1 scheme-dependence concern re-opens; f_conv is not a physical observable in the usual sense; carry-forward as S86 re-investigation.
**Effort**: 8 hours (two-loop Mellin-Barnes is nontrivial); CPU (symbolic) + GPU (numerical cross-check only).
**Substrate-framing reminder**: Z_R is the fiber-transition renormalization factor; it IS space at the fiber level, not a coupling on a background. "Two-loop" refers to two-loop correction in the substrate's spectral action expansion, which is the 6th Seeley-DeWitt coefficient contribution at the τ_fold slice.

---

## §W0-6. S85-VAN-HOVE-CUSP-THEOREM

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: gen-physicist
**Hypothesis**: τ_fold is uniquely determined by the van Hove cusp condition on the D_K density of states — specifically, the unique τ ∈ (0, 1) at which dρ(E)/dE|_{E=E_fold} is non-analytic (divergent first derivative) — reformulated per the W8a-85 audit consensus to resolve the sign-convention ambiguity between Baptista's and Jensen's canonical forms.
**Method**: Write `s85_w0_van_hove_cusp_theorem.py` that (a) computes ρ(E; τ) = DOS of D_K at τ ∈ linspace(0.15, 0.25, 101), L_max=8, (b) identifies the cusp τ_cusp by locating the non-analyticity via finite-difference dρ/dE → ∞; (c) verifies τ_cusp = τ_fold_canonical = 0.190 to within 0.5%; (d) produces the formal theorem statement in the working paper (Baptista-Jensen sign reconciliation); (e) emits verdict. Use torch.linalg.eigh on GPU for all 101 τ points.
**Machinery pin (PRDR)**: τ_grid=linspace(0.15, 0.25, 101); L_max=8; DOS_bin_width=0.01 (in units of M_KK); cusp_detector=second-derivative-divergence threshold dρ/dE > 1000; sign_convention=Baptista-canonical (pinned); fallback_jensen_convention=explicit_annotation_in_wp; GPU=torch; device=cuda:0; eigensolver_tol=1e-10.
**Input SHA pins**: canonical_constants.py (τ_fold); D_K construction kernel hash; W8a-85 audit-consensus record SHA.
**Expected output 4-tuple**: (value=τ_cusp, scheme=DOS-cusp, convention=Baptista-sign, L_max=8)
**Thresholds**: PASS if |τ_cusp − τ_fold_canonical| / τ_fold_canonical < 0.5% AND cusp is unique on the grid (no other τ satisfies the cusp criterion); INFO if 0.5% ≤ deviation < 2%; FAIL if ≥ 2% OR cusp non-unique.
**Substitution chain**: [VERIFY-THEOREM] — the chain is the analytic argument: dispersion surface near τ_fold + Baptista canonical sign + unique-minimum property on the compact τ interval. Written in §VI.
**Implications**: PASS ⇒ τ_fold is theorem-grade; no free-parameter freedom; sign convention closed. FAIL ⇒ either DOS-cusp is not the correct characterization (re-audit mechanism), or sign conventions disagree and the theorem needs reformulation.
**Effort**: 5 hours (101 τ-points × eigensolver at L=8 ≈ 30 minutes on GPU); GPU.
**Substrate-framing reminder**: The van Hove cusp IS the Jensen-deformation-unique point in substrate-spectral geometry where D_K's spectrum develops a degeneracy — this is NOT a parameter choice but a structural feature of the fabric at τ_fold.

---

## §W0-7. S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The Zubarev ρ-limit at large L_max converges to −1 exactly, as an analytic corollary of the Jensen-deformation spectral identity; direct numerical test at L_max ∈ {8, 9, 10, 11, 12} should show monotone convergence ρ(L) → −1 with residual 1/L²-decay.
**Method**: Write `s85_w0_zubarev_lmax_minus_one.py` that (a) computes ρ_Zubarev(L_max) for L ∈ {8, 9, 10, 11, 12} (definition: signed weighted average of D_K eigenvalues over the Mellin-cone Zubarev kernel), (b) fits ρ(L) = −1 + α/L² + β/L⁴, (c) reports the asymptotic intercept, (d) derives analytically the −1 limit via the Jensen + Zubarev identity in the WP §VI, (e) verdict.
**Machinery pin (PRDR)**: L_max ∈ {8, 9, 10, 11, 12}; Zubarev_kernel=canonical (Zubarev 1974 + Connes-Moscovici 1995 extension); fit_model=−1 + α/L² + β/L⁴; target_limit=−1 exact; tolerance_RATIO=1% on intercept; GPU=torch; eigensolver_tol=1e-10.
**Input SHA pins**: D_K eigenvalue caches (shared with W0-3); Zubarev kernel definition file.
**Expected output 4-tuple**: (value=ρ(L=12), scheme=Zubarev-Mellin, convention=Jensen-deformed, L_max=12)
**Thresholds**: PASS if |ρ_fit_intercept − (−1)| ≤ 0.01 AND monotone convergence sign verified; INFO if 0.01 < |ρ + 1| ≤ 0.05; FAIL if > 0.05 OR non-monotone.
**Substitution chain**: [VERIFY-THEOREM] chain in WP §VI — Jensen deformation identity + Zubarev kernel convolution → −1.
**Implications**: PASS ⇒ analytic corollary theorem; promotes Zubarev-limit-identity to permanent registry. FAIL ⇒ the Jensen-Zubarev identity conjecture is numerically wrong; carry-forward investigation of Mellin-cone truncation effects at higher L.
**Effort**: 4 hours (shared eigenvalue cache with W0-3 saves time); GPU.
**Substrate-framing reminder**: ρ_Zubarev is the Zubarev-weighted spectral moment of D_K, a substrate-geometric invariant. The −1 limit is the Jensen-deformation's fixed point at the τ_fold slice.

---

## §W0-8. S85-PIXIE-MU-K-ENDPOINT-PREREG

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: little-red-dots-jwst-analyst
**Hypothesis**: The PIXIE μ-distortion K-endpoint observation at K = 3.56 × 10⁵ (gamma = 1 lockout) with predicted μ = 8.69 × 10⁻⁵ is observationally pre-registered as a discriminator against LCDM's μ ≈ 2 × 10⁻⁸; the 4-OOM separation is well above PIXIE's forecast σ(μ) ≈ 10⁻⁸.
**Method**: Write `s85_w0_pixie_mu_k_endpoint_prereg.py` that (a) imports μ_framework, K, γ from canonical_constants (add if absent); (b) loads PIXIE forecast σ(μ) ≈ 10⁻⁸ from the PIXIE Science Book; (c) computes pull = |μ_framework − μ_LCDM| / σ(μ); (d) cross-checks the γ = 1 lockout band (the framework's K-endpoint is only meaningful when γ = 1 — verify the lockout condition holds at the pre-registered K); (e) emits verdict + dual-SHA.
**Machinery pin (PRDR)**: μ_framework=8.69e-5; K=3.56e5; γ_lockout=1 (exact); σ(μ)_PIXIE=1e-8 (PIXIE Science Book Table 2, 2011); μ_LCDM_ref=2e-8; scheme=Chluba-Sunyaev-2012; L_max=8; GPU=none.
**Input SHA pins**: canonical_constants.py; PIXIE Science Book values hash; W5-57 closure verdict SHA.
**Expected output 4-tuple**: (value=pull, scheme=Chluba-Sunyaev-2012, convention=γ-lockout, L_max=8)
**Thresholds**: PASS if pull ≥ 100 AND γ = 1 verified in the K-band; INFO if 10 ≤ pull < 100; FAIL if pull < 10 OR γ-lockout violated.
**Substitution chain**:
  Step 1: μ_framework = 8.69e-5 [S84 W5-57 closure]
  Step 2: μ_LCDM = 2e-8 [Chluba-Sunyaev]
  Step 3: σ(μ) = 1e-8 [PIXIE]
  Step 4: pull = |8.69e-5 − 2e-8| / 1e-8 ≈ 8.688e-5 / 1e-8 = 8688
  Step 5: Direction: pull ≫ 100 ⇒ PASS.
**Implications**: PASS ⇒ PIXIE (launch-date TBD but forecasted for 2029+) is an inevitable decisive test; 4-OOM framework-LCDM separation is among the largest in the S85 pre-registration landscape. FAIL ⇒ the γ = 1 lockout fails and the endpoint is observationally degenerate with LCDM; triggers a W3 K-corridor re-scan.
**Effort**: 1 hour; CPU.
**Substrate-framing reminder**: μ-distortion is an observation of the GGE relic's thermodynamic inheritance; the framework's μ is NOT a vacuum-fluctuation amplitude but the thermodynamic signature of 59.8 Parker-pair-produced quasiparticles propagating through the substrate post-transit.

---

## §W0-9. S85-D_SPEC-ALT-DERIVATION-PATH

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: feynman-theorist
**Hypothesis**: The "12" exponent appearing in d_spec probe at the fiber-transition scale of μ_BC admits at least two independent derivation pathways — (a) heat-kernel Seeley-DeWitt direct computation, (b) zeta-function at interior-s* analytic continuation, (c) representation-theoretic SU(3) Casimir sum — yielding the same value 12 up to rational equivalence, providing cross-check robustness.
**Method**: Write `s85_w0_d_spec_alt_derivations.py` that (a) executes pathway (a) via `_heat_kernel_a4.py` helper with L_max=8, (b) executes pathway (b) via analytic continuation of ζ_{D_K}(s) to s* ∈ {3, 4, 5}, (c) executes pathway (c) via direct SU(3) quadratic-Casimir representation sum, (d) compares all three for numerical equivalence, (e) emits verdict + dual-SHA.
**Machinery pin (PRDR)**: L_max=8; heat_kernel_expansion_order=4 (a_4 coefficient); zeta_continuation_s_points={3,4,5}; mpmath_dps=50; Casimir_convention=Dynkin-label; target_value=12 (exact integer); tolerance_RATIO=1e-6.
**Input SHA pins**: D_K eigenvalue cache L=8; SU(3) Casimir reference table; _heat_kernel_a4.py file hash.
**Expected output 4-tuple**: (value=12, scheme=heat-kernel-Seeley-DeWitt, convention=MS-bar, L_max=8)
**Thresholds**: PASS if all 3 pathways agree to within 1e-6 relative AND all yield integer 12; INFO if 2/3 agree; FAIL if fewer than 2 agree OR values non-integer.
**Substitution chain**: [VERIFY-THEOREM] cross-check chain — three independent derivations of same exponent; written in WP §VI.
**Implications**: PASS ⇒ d_spec exponent is derivation-robust; exponent 12 is promoted to a permanent registry entry with 3 independent provenances. FAIL ⇒ one pathway has a hidden convention mismatch; need to identify which derivation is canonical.
**Effort**: 6 hours (three pathways); CPU + GPU.
**Substrate-framing reminder**: d_spec is the substrate's dimensional-spectrum signature; the "12" is the a_4 Seeley-DeWitt coefficient index at the fiber-transition, a purely geometric invariant of the D_K spectrum.

---

## §W0-10. S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The CC-2 Priority-1 closure — Spin(8) triality orbit sum of χ_2 over A_F internal structure — equals the conjectured closed form (integer or small rational) at L_max=8, providing the second of the six CC-series closures.
**Method**: Write `s85_w0_cc2_spin8_triality.py` that (a) enumerates Spin(8) triality orbits of A_F representations, (b) computes the orbit-weighted sum Σ χ_2 over the SU(3) eigenspaces at L_max=8, (c) compares to the conjectured closed form from S84 connes synthesis, (d) emits verdict. Use torch for orbit-index enumeration.
**Machinery pin (PRDR)**: L_max=8; Spin(8)_triality_action=canonical (vector V, spinor S⁺, conjugate-spinor S⁻); orbit_enumeration_convention=Adams-1981; χ_2_definition=second-order spectral zeta residue at τ_fold (⟨|λ_R|⟩ / λ_R^max per S84 connes synthesis §V.1); target_triality_equality=|chi_2(V) − chi_2(S⁺)| < 1% AND |chi_2(V) − chi_2(S⁻)| < 1% (triality preservation under Jensen); target_ratio_band=0.90 ≤ (chi_2^triality × HP4) / ρ_obs ≤ 1.10 (3× closure-hypothesis band per §V.1; chi_2^triality := chi_2(V) + chi_2(S⁺) + chi_2(S⁻); HP4=0.4548 back-solved from S75 W4-C, or recomputed first-principles per S76); ρ_obs=2.7e-47 GeV⁴ (canonical); closure_hypothesis_central_ratio=1.011 (single-sector baseline 0.337 × 3 per §V.1 R2); tolerance_RATIO=1e-2 (1% tolerance on triality equality; 10% band on ρ_obs ratio).
**Input SHA pins**: D_K eigenvalue cache L=8; Spin(8) orbit-map file; S84 connes synthesis record `sessions/archive/session-84/session-84-connes-CCrevisit-synthesis.md` §V.1 (static).
**Expected output 4-tuple**: (value=(chi_2^triality × HP4) / ρ_obs, scheme=triality-orbit, convention=Adams-1981, L_max=8)
**Thresholds**: PASS if |CC-2 − target| / target < 1e-6 AND target is rational with small denominator; INFO if 1e-6 ≤ ratio ≤ 1e-3; FAIL if > 1e-3.
**Substitution chain**: [VERIFY-THEOREM] — triality-orbit identity proof in §VI.
**Implications**: PASS ⇒ CC-2 closure; 1 of 6 CC-series done this session. FAIL ⇒ triality-orbit map has a convention mismatch; carry-forward orbit-enumeration re-audit.
**Effort**: 3 hours; GPU.
**Substrate-framing reminder**: Spin(8) triality is a substrate-intrinsic symmetry of the A_F algebra; CC-2 IS a spectral identity on the fabric, not a Lagrangian invariance.

---

## §W0-11. S85-CC-3-CONNES-MOSCOVICI-RESIDUE

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The CC-3 Connes-Moscovici dimension-spectrum signed-residue sum over the full Jensen-SU(3) × A_F triple at L_max=8 equals the conjectured target (Priority 5 closure of the CC series).
**Method**: Write `s85_w0_cc3_connes_moscovici.py` that (a) computes the Connes-Moscovici residues at s* ∈ dimension spectrum {0, 1, 2, 3, 4, 5, 6, 7, 8}, (b) sums signed residues per the Connes-Moscovici 1995 convention, (c) compares to conjectured target, (d) emits verdict. Use mpmath for high-precision analytic continuation.
**Machinery pin (PRDR)**: L_max=8; dimension_spectrum={0..8}; residue_sign_convention=Connes-Moscovici-1995 Prop 4.2; mpmath_dps=50; baseline=a_0_residue (CC-relevant comparison quantity per S84 connes synthesis §V.5); target_OOM_suppression_PASS=10 (signed sum |Λ_CC|/|a_0| ≤ 1e-10 for PASS); target_OOM_suppression_INFO=[1, 10] (informational: 1e-10 < |Λ_CC|/|a_0| ≤ 1e-1); prerequisite=S83 W1-G3 `dim H_π ≥ 2` closure (if FAIL upstream, CC-3 DEFERRED to L_max=11 or WITHDRAWN per §V.5); tolerance_RATIO=1e-2 on ratio threshold (accept OOM stated to nearest tenth); GPU=none (analytic).
**Input SHA pins**: D_K eigenvalue cache L=8; Connes-Moscovici 1995 reference equations file; S84 connes synthesis record `sessions/archive/session-84/session-84-connes-CCrevisit-synthesis.md` §V.5 (static); S83 W1-G3 closure status record.
**Expected output 4-tuple**: (value=log10(|Λ_CC|/|a_0|), scheme=Connes-Moscovici-1995, convention=dim-spec-signed-residue, L_max=8)
**Thresholds**: PASS if |CC-3 − target| / target < 1e-6; INFO if 1e-6 ≤ ratio < 1e-3; FAIL if > 1e-3.
**Substitution chain**: [VERIFY-THEOREM] — in WP §VI.
**Implications**: PASS ⇒ CC-3 closure (5/6 CC-series in S85 if paired with CC-1/2/4/5). FAIL ⇒ dimension-spectrum truncation issue OR sign convention mismatch; carry-forward.
**Effort**: 5 hours; CPU.
**Substrate-framing reminder**: The dimension spectrum is the substrate's intrinsic dimensional signature set — not an ambient spacetime dimension. Connes-Moscovici residues are a Mellin-cone invariant of D_K.

---

## §W0-12. S85-CC-4-DAI-FREED-TORSION

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The CC-4 Priority-4 closure — Dai-Freed torsion pairing of Jensen-SU(3) with π_4(S³) = ℤ/2 — yields the expected ±1 value (element of ℤ/2) consistent with the framework's KO-dim = 6 global-anomaly freedom.
**Method**: Write `s85_w0_cc4_dai_freed_torsion.py` that (a) constructs the Dai-Freed pairing cocycle on Jensen-SU(3), (b) computes the torsion-valued pairing with π_4(S³) = ℤ/2 generator, (c) checks consistency with KO-dim = 6 (the pairing should be anomaly-free), (d) emits verdict. This is an integer computation; CPU-only.
**Machinery pin (PRDR)**: L_max=8; Dai-Freed_convention=Dai-Freed-1994; π_4(S³)_generator=canonical-SU(2)-instanton (k=1 winding); KO-dim=6 (pinned from framework permanent results); pairing_scheme=eta-invariant-mod-Z; GPU=none.
**Input SHA pins**: Jensen-SU(3) fiber structure file; Dai-Freed 1994 reference equations; KO-dim=6 registry entry.
**Expected output 4-tuple**: (value=±1, scheme=Dai-Freed-1994, convention=η-mod-Z, L_max=8)
**Thresholds**: PASS if pairing ∈ {+1, −1} (element of ℤ/2) AND consistent with KO-dim=6 anomaly-freedom; INFO if pairing nonzero but inconsistent with KO-dim sign; FAIL if zero (indicates trivial pairing, framework-unfavorable).
**Substitution chain**: [VERIFY-THEOREM] — pairing proof in WP §VI.
**Implications**: PASS ⇒ CC-4 closure; framework globally anomaly-free at the Dai-Freed level. FAIL ⇒ a global-anomaly violation; framework has a hidden inconsistency with π_4 torsion.
**Effort**: 5 hours; CPU.
**Substrate-framing reminder**: Dai-Freed torsion pairing IS the substrate's global phase — the spectral triple's discrete ℤ/2 invariant, not a gauge choice.

---

## §W0-13. S85-CMB-S4-ALPHA-FLAGSHIP-DOC

**Trigger**: [AUDIT]
**Classification**: META
**Agent**: mack-cosmic-bridge
**Hypothesis**: The CMB-S4 α_s flagship pre-registration document (W6-D.4 carry-forward) is complete, captures all five observational channels (α_s, β_s, n_T, r, f_NL^fold), pre-registers per-channel σ forecasts, and maps the framework's predicted values to decisive / INFO / sub-threshold bands.
**Method**: Write `s85_w0_cmb_s4_alpha_flagship_doc.md` (documentation gate — note: this is documentation, not a computation; the "script" is a presence-and-completeness audit written by a small `s85_w0_cmb_s4_alpha_flagship_audit.py` that verifies the document has all required sections). The audit checks: (a) α_s, β_s, n_T, r, f_NL^fold all have pre-registered values with SHAs; (b) σ-forecasts per-channel sourced to CMB-S4 Science Book; (c) decisive bands listed; (d) dependencies on W0-1 (β_s) declared. Emit verdict based on document completeness count.
**Machinery pin (PRDR)**: required_channels={α_s, β_s, n_T, r, f_NL^fold}; required_sections={prereg_value, forecast_sigma, decisive_band, framework_prediction, LCDM_null, SHA_pin}; σ_source=CMB-S4 Science Book v2 2022; GPU=none.
**Input SHA pins**: W6 D.4 carry-forward record; W0-1 verdict SHA; CMB-S4 Science Book hash.
**Expected output 4-tuple**: (value=sections_complete/25, scheme=prereg-doc-audit, convention=CMB-S4-SB-v2, L_max=8)
**Thresholds**: PASS if 25/25 sections filled (5 channels × 5 required sections); INFO if 20-24; FAIL if < 20.
**Substitution chain**: [AUDIT] — presence check, not a sign claim.
**Implications**: PASS ⇒ CMB-S4 α_s flagship is pre-registration-complete; zero post-hoc flexibility. FAIL ⇒ missing channel or missing forecast; carry-forward structured completion.
**Effort**: 3 hours; CPU.
**Substrate-framing reminder**: CMB-S4 observes acoustic signatures of the GGE relic, not primordial vacuum fluctuations. Every flagship prediction is the substrate's inevitable post-transit acoustic signal at the observational epoch.
### W0-13 APPENDIX: Independence Subsection (augmented by S85-W4-1-CMB-S4-INDEP-AUG)

*Inserted by S85-W4-1-CMB-S4-INDEP-AUG. Closes the silence on correlation structure among the 5-channel falsifier watchlist. Prevents Bayes-factor inflation up to factor k^4 = 81 for per-channel BF ~ k = 3.*

**5-channel watchlist:**
  0. `CMB-S4_alpha_s` --- probes: d^2 S_transfer/dk^2 at k_pivot (scalar 2-pt 2nd derivative)
  1. `DESI-DR3_w_0` --- probes: a_0 Volovik-partition (zeroth spectral moment)
  2. `LiteBIRD_n_T` --- probes: tensor-sector Dirac spectrum (B-mode polarization; r=16eps INAPPLICABLE per phononic-framing)
  3. `CMB-HD_alpha_s` --- probes: d^2 S_transfer/dk^2 at k_pivot (SAME moment as CMB-S4 alpha_s)
  4. `21cm_folded_bispec` --- probes: 3-point spectral moment (non-Gaussianity; distinct from 2-pt)

**Pair-wise classification (C(5,2) = 10 off-diagonal cells):**

| Pair | Channels | Classification | Source | Citation | Justification |
|:----:|:---------|:--------------:|:------:|:---------|:--------------|
| (0,1) | CMB-S4 alpha s / DESI-DR3 w 0 | PARTIALLY_CORRELATED | FISHER | DESI Collab 2025 BAO forecast; Planck 2018 parameter table | Shared acoustic-scale ladder (r_d) correlates Planck TT foregrounds with DESI BAO distance-scale. |
| (0,2) | CMB-S4 alpha s / LiteBIRD n T | INDEPENDENT | FISHER | CMB-S4 Science Book v2 2022 section 3.1; LiteBIRD 1902.00541 | Scalar-tilt running vs tensor tilt: orthogonal spectral moments; polarization-B foreground independent of TT. |
| (0,3) | CMB-S4 alpha s / CMB-HD alpha s | COMMON_MODE | FISHER | CMB-HD Sehgal 2019 Whitepaper section 4; CMB-S4 Science Book v2 Table 6.1 | Identical theoretical observable; overlapping foreground model; potentially correlated atmospheric noise. |
| (0,4) | CMB-S4 alpha s / 21cm folded bispec | INDEPENDENT | WARRANT-DEFERRED | HERA Memo 54 (Ali+ 2018); no joint CMB-S4 x 21cm Fisher published | z=1100 recombination (CMB) vs z~7 reionization (21cm); 2-pt vs 3-pt statistics; epoch-separated. |
| (1,2) | DESI-DR3 w 0 / LiteBIRD n T | INDEPENDENT | WARRANT-DEFERRED | DESI Collab 2025; LiteBIRD 1902.00541; no joint DESIxLiteBIRD published | Late-time expansion history vs primordial-tensor B-mode; no shared systematic. |
| (1,3) | DESI-DR3 w 0 / CMB-HD alpha s | PARTIALLY_CORRELATED | FISHER | DESI Collab 2025 section 4; Sehgal 2019 CMB-HD Whitepaper | Both derive r_d acoustic ruler; CMB-HD extends Planck+ACT CMB prior used in DESI BAO likelihood. |
| (1,4) | DESI-DR3 w 0 / 21cm folded bispec | INDEPENDENT | WARRANT-DEFERRED | DESI Collab 2025; HERA Memo 54; no joint DESIx21cm Fisher published | Low-z BAO (z<2) vs high-z NG (z>6); epoch-separated; different tracers. |
| (2,3) | LiteBIRD n T / CMB-HD alpha s | INDEPENDENT | FISHER | LiteBIRD 1902.00541; Sehgal 2019 CMB-HD section 4 | B-mode tensor vs TT/TE scalar running; CMB foreground templates differ between channels. |
| (2,4) | LiteBIRD n T / 21cm folded bispec | INDEPENDENT | WARRANT-DEFERRED | LiteBIRD 1902.00541; HERA Memo 54; no joint published | CMB polarization vs reionization cross-correlation; no shared systematic. |
| (3,4) | CMB-HD alpha s / 21cm folded bispec | INDEPENDENT | WARRANT-DEFERRED | Sehgal 2019 CMB-HD; HERA Memo 54; no joint CMB-HDx21cm Fisher published | Same logic as CMB-S4 x 21cm; different instrument-epoch pairing. |

**Coverage**: 5/10 pairs with published Fisher citations (= 0.500); 5/10 tagged WARRANT-DEFERRED (no published joint Fisher); 0 silent.

**Substitution chain — BF-inflation direction:**

```
Step 1: BF_joint_indep = product_i BF_i   (independence)
Step 2: BF_joint_corr  ~ max_i BF_i       (common-mode)
Step 3: Substitute N=5, BF_i = k = 3:
        BF_joint_indep = k^N = 243
        BF_joint_corr  = k   = 3
        Ratio          = k^(N-1) = 81
Step 4: Simplify — over-states evidence by ~k^(N-1) when pairs COMMON_MODE.
Step 5: Direction — augment is DEFLATIONARY on joint BF.
Conclusion: omission inflates; augment closes silence and pins discount per pair.
```

**Post-data Bayes-factor formula (W4-2 will canonicalize):**

  `BF_joint = BF_CMBS4 * BF_DESI^{1-rho_01} * BF_LiteB * BF_CMBHD^{1-rho_03} * BF_21cm`

where rho_ij are taken from the §W4-2 xcorr matrix (specifically rho_01 = pipeline CMB-S4/DESI DR3; rho_03 = CMB-S4/CMB-HD common-mode).

**Artifacts (S84+ dual-SHA):**
  - `computations/s85_w4_cmbs4_indep_aug.npz` (machine-readable matrix)
  - `computations/s85_w4_cmbs4_indep_aug.png` (heatmap)


---

## §W0-14. S85-CANONICAL-ENTRY-CONSOLIDATION

**Trigger**: [AUDIT]
**Classification**: META
**Agent**: gen-physicist
**Hypothesis**: Cross-agent canonical-constants entries from lizzi and van-den-dungen S84 syntheses (specifically ε_H, HP^1 dimension, NCG parity-rank exclusion constants) are unified into `canonical_constants.py` with consistent provenance and no redundancy/collision.
**Method**: Write `s85_w0_canonical_entry_consolidation.py` that (a) scans lizzi S84 synthesis for canonical-entry claims (ε_H, parity-exclusion), (b) scans van-den-dungen S84 synthesis for (HP^1-dim, rank-exclusion, non-flat-T correction), (c) checks canonical_constants.py for presence/absence of each, (d) for missing entries, calls update_constant(...) with provenance "S84-{reviewer}-synthesis-section-VI.{slug}", (e) verifies no two entries have the same name with different values (collision check), (f) emits verdict with counts.
**Machinery pin (PRDR)**: lizzi_source=sessions/archive/session-84/session-84-s5-lizzi-cohomology-synthesis.md; vdd_source=sessions/archive/session-84/session-84-s5-vdd-cohomology-synthesis.md; target_list={ε_H, HP^1_dim, FI_parity_exclusion, rank_exclusion, nonflat_T_correction_L2}; collision_tolerance=0; GPU=none.
**Input SHA pins**: lizzi and vdd S84 synthesis file hashes; canonical_constants.py SHA (before).
**Expected output 4-tuple**: (value=entries_added, scheme=canonical-consolidation, convention=provenance-tagged, L_max=NA)
**Thresholds**: PASS if ≥ 5 target entries present in canonical_constants.py post-run AND zero collisions; INFO if 3-4/5; FAIL if < 3 OR any collision detected.
**Substitution chain**: [AUDIT] — presence check.
**Implications**: PASS ⇒ S84 cross-reviewer structural results are canonicalized. FAIL ⇒ constants remain scattered; risk of re-derivation in S86+.
**Effort**: 2 hours; CPU.
**Substrate-framing reminder**: Each canonicalized constant is a substrate-invariant — a fixed value determined by the D_K spectral structure, not a tunable parameter.

---

## §W0-15. S85-CSCANON-IDENTITY-TEST

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: landau-condensed-matter-theorist
**Hypothesis**: The identity f_B = c_S_canon (W5 D.5 carry-forward) — the conjecture that the Bogoliubov mixing coefficient equals the canonical speed-of-substrate ratio — is numerically exact at L_max=8 across all K ∈ [K_R5, K_crit] corridor values.
**Method**: Write `s85_w0_fB_cScanon_identity.py` that (a) loads f_B(K) and c_S_canon(K) from canonical_constants (use pre-S85 computed tables), (b) compares across K_grid = linspace(K_R5, K_crit, 50), (c) emits the max absolute deviation, (d) produces the plot of both curves overlaid and the residual.
**Machinery pin (PRDR)**: K_grid=linspace(K_R5=1.9222, K_crit=2.0446, 50); L_max=8; f_B_source=W5-64 table; c_S_canon_source=canonical_constants.c_fabric; tolerance_ABSOLUTE=1e-3; GPU=none.
**Input SHA pins**: W5-64 f_B table; canonical_constants.py.
**Expected output 4-tuple**: (value=max|f_B − c_S_canon|, scheme=Leggett-Bogoliubov, convention=W5-D.5, L_max=8)
**Thresholds**: PASS if max deviation ≤ 1e-3 across the K grid; INFO if 1e-3 < dev ≤ 1e-2; FAIL if > 1e-2.
**Substitution chain**:
  Step 1: f_B(K) = Bogoliubov mixing coefficient in the Leggett channel [def., W5-64]
  Step 2: c_S_canon = canonical substrate speed [def., canonical_constants.c_fabric]
  Step 3: Hypothesis: f_B(K) = c_S_canon ∀ K in corridor
  Step 4: test statistic = max_K |f_B(K) − c_S_canon|
  Step 5: Direction: if stat ≤ 1e-3, identity holds numerically; else refuted.
**Implications**: PASS ⇒ an identity between a dynamic coefficient and a canonical geometric ratio; powerful structural result for registry. FAIL ⇒ the conjectured identity is approximate; residual has a K-dependence that needs explanation.
**Effort**: 2 hours; CPU.
**Substrate-framing reminder**: f_B is the mixing coefficient in the GGE-relic Leggett channel; c_S_canon is a substrate-geometric invariant from the Jensen-deformation speed. The identity would mean the dynamical coupling IS a geometric ratio — a substrate result of highest structural rank.

---

## §W0-16. S85-HP1-DIMENSION-UNTWISTED-TWISTED

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: van-den-dungen-bridge-theorist
**Hypothesis**: The HP^1(A_F) dimension computed (a) in the un-twisted baseline equals the classical Connes-Marcolli 2008 result, and (b) in the twisted CM-2008 extension (ε_H ≠ 0) changes in the expected direction per the parity-wall theorem.
**Method**: Write `s85_w0_hp1_dim_twisted.py` that (a) computes dim HP^1(A_F) in un-twisted baseline (ε_H = 0), (b) computes under CM-2008 twist (ε_H from canonical_constants), (c) verifies un-twisted matches CM-2008 classical answer, (d) computes twisted-minus-untwisted dimension shift, (e) emits verdict with both values.
**Machinery pin (PRDR)**: L_max=8; A_F_algebra=standard-model-SM-spectral-triple; ε_H_value=canonical_constants.eps_H; twist_convention=CM-2008 Prop 3.5; classical_target=CM-2008 Table 2; GPU=none.
**Input SHA pins**: canonical_constants.py; CM-2008 reference equations file.
**Expected output 4-tuple**: (value=(dim_untwisted, dim_twisted), scheme=HP-cohomology, convention=CM-2008, L_max=8)
**Thresholds**: PASS if dim_untwisted = CM-2008 classical value AND dim_twisted − dim_untwisted is in {0, ±1} (bounded shift); INFO if dimensions compute but shift has unexpected magnitude; FAIL if dim_untwisted ≠ classical.
**Substitution chain**: [VERIFY-THEOREM] — classical matches + twist shift argument in WP §VI.
**Implications**: PASS ⇒ HP^1 dimension is correctly computed for the framework's A_F; provides the dimension-of-moduli input for other CC-series gates. FAIL ⇒ A_F algebra structure has a hidden discrepancy with CM-2008 classical.
**Effort**: 4 hours; CPU.
**Substrate-framing reminder**: HP^1 is the first Hochschild periodic cohomology of the substrate's internal algebra A_F; it counts the dimension of the deformation moduli space, not a dimension of spacetime.

---

## §W0-17. S85-K-FLOOR-WALL-JOINT-REGISTRY-LANDING

**Trigger**: [AUDIT]
**Classification**: PHONONIC
**Agent**: landau-condensed-matter-theorist
**Hypothesis**: The K-FLOOR-WALL joint closure (W5 D.4) — the statement that K_floor AND K_wall co-determine the corridor with a joint probability-1 closure condition — is ready for permanent-results-registry landing, with SHA-pinned provenance linking to the 5-regulator atlas.
**Method**: Write `s85_w0_k_floor_wall_registry_landing.py` that (a) verifies K_floor and K_wall values from canonical_constants, (b) checks the joint closure condition (specific to W5 D.4 convention), (c) writes a new registry entry to the permanent-results-registry with provenance, (d) emits verdict on registry-write success.
**Machinery pin (PRDR)**: K_floor=from canonical_constants; K_wall=from canonical_constants; joint_condition=W5-D.4 canonical; registry_target=summary/permanent-results-registry.md; GPU=none.
**Input SHA pins**: W5 D.4 carry-forward record; canonical_constants.py.
**Expected output 4-tuple**: (value=registry_entry_count, scheme=permanent-registry, convention=W5-D.4, L_max=8)
**Thresholds**: PASS if registry entry written AND both K-values present; INFO if entry written but one K missing; FAIL if registry-write fails or K values inconsistent.
**Substitution chain**: [AUDIT] — presence check.
**Implications**: PASS ⇒ K-corridor closure is registry-landed; downstream corridor-dependent gates have a stable reference. FAIL ⇒ carry-forward with SHA-repin.
**Effort**: 2 hours; CPU.
**Substrate-framing reminder**: K is the corridor parameter in the Jensen-SU(3) substrate — the compactification radius proxy; "floor" and "wall" are substrate-geometric bounds, not potential-landscape extrema.

---

## §W0-18. S85-LITEB-LSST-RESCUE-PRIOR

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge
**Hypothesis**: LiteBIRD n_T observational reach can be rescued to detectability via (a) LSST A_lens external prior tightening, (b) extended-mission 3-year baseline, (c) delensing with Simons Observatory large-aperture maps — and at least one of these pathways brings LiteBIRD's σ(n_T) below the framework's predicted |n_T|.
**Method**: Write `s85_w0_litebird_lsst_rescue.py` that (a) loads baseline LiteBIRD σ(n_T) from Hazumi 2020 forecast, (b) applies the three rescue scenarios' σ-improvement factors, (c) computes the framework-predicted n_T (pin from canonical_constants or earlier S84 compute), (d) flags which scenario(s) achieve pull ≥ 3 vs n_T=0, (e) emits verdict.
**Machinery pin (PRDR)**: σ(n_T)_baseline=LiteBIRD Hazumi 2020 Table 5; LSST_A_lens_improvement=1.3× (per LSST SRD); extended_mission_factor=√(3/2); delensing_factor=0.7 (Simons Obs fiducial); n_T_framework=pin from S84 W4-41; pull_threshold=3.
**Input SHA pins**: S84 W4-41 n_T framework value; Hazumi 2020 values hash.
**Expected output 4-tuple**: (value=(pull_scenario_A, pull_scenario_B, pull_scenario_C), scheme=Fisher-rescue, convention=LiteBIRD-2020, L_max=8)
**Thresholds**: PASS if ≥ 1 scenario achieves pull ≥ 3; INFO if ≥ 1 scenario achieves 1 ≤ pull < 3; FAIL if all scenarios have pull < 1.
**Substitution chain**:
  Step 1: σ(n_T) after rescue = σ_baseline × rescue_factor [def.]
  Step 2: pull = |n_T_framework − 0| / σ(n_T)_rescue [def.]
  Step 3: compute for each scenario; direction: if any pull ≥ 3, LiteBIRD is viable.
**Implications**: PASS ⇒ LiteBIRD still delivers decisive n_T measurement with one of the rescue paths; framework prediction remains near-term testable. FAIL ⇒ LiteBIRD n_T channel is effectively closed; carry-forward to CMB-S4 n_T channel as the only near-term option.
**Effort**: 3 hours; CPU.
**Substrate-framing reminder**: n_T is the tensor tilt of the primordial GW spectrum — in the framework, the acoustic tilt of the CGWB post-transit, NOT the slow-roll inflationary tilt.

---

## §W0-19. S85-MELLIN-TEMPLATE-COMPLIANCE-LIFT

**Trigger**: [AUDIT]
**Classification**: GEOMETRIC
**Agent**: feynman-theorist
**Hypothesis**: The Mellin-balance template compliance across the 16 canonical scripts rises to 16/16 after applying the W6-71 compliance-lift recipe (re-write non-compliant scripts to use the canonical Mellin-balance boilerplate).
**Method**: Write `s85_w0_mellin_template_compliance_lift.py` that (a) audits the 16 Mellin-balance template scripts (list from W6-71), (b) grep for the canonical boilerplate block, (c) for each non-compliant, write a suggested patch, (d) emits the compliance count.
**Machinery pin (PRDR)**: template_source=W6-71 canonical Mellin-balance boilerplate; target_count=16; audit_script=_mellin_template_audit.py (helper); GPU=none.
**Input SHA pins**: W6-71 carry-forward; each of the 16 scripts' SHAs.
**Expected output 4-tuple**: (value=compliance_count/16, scheme=template-audit, convention=Mellin-balance-W6-71, L_max=NA)
**Thresholds**: PASS if 16/16; INFO if 13-15; FAIL if < 13.
**Substitution chain**: [AUDIT].
**Implications**: PASS ⇒ Mellin-balance is infrastructure-compliant; future Mellin-cone computations inherit the verified boilerplate. FAIL ⇒ carry-forward per-script fixes.
**Effort**: 3 hours; CPU.
**Substrate-framing reminder**: Mellin-balance is a substrate-spectral-analysis convention (convergence of the D_K Mellin cone); template compliance is infrastructure, not physics — but infrastructure failures propagate to physics verdicts.

---

## §W0-20. S85-W0-L-MELLIN-CONE-S3-RESIDUE

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The Mellin-cone Connes-Moscovici residue at s=3 converges under L_max ∈ {8, 9, 10, 11, 12} sweep; if convergence is confirmed, the residue value becomes permanent-registry; if divergent, a contingency re-choice of s* is triggered.
**Method**: Write `s85_w0_mellin_cone_s3_residue.py` that (a) computes the CM residue at s=3 for L ∈ {8, 9, 10, 11, 12}, (b) fits residue(L) = R_∞ + α/L² + β/L⁴, (c) if convergent, emits R_∞ verdict; if divergent (|R(L) − R(L-1)| not decreasing), emits FAIL with contingency s* = 2 or 4 flag.
**Machinery pin (PRDR)**: s*=3 (primary); contingency_s*=∈{2, 4}; L_max ∈ {8, 9, 10, 11, 12}; fit_model=R_∞ + α/L² + β/L⁴; convergence_rule=3 consecutive L show monotone decrease in |R(L) − R(L-1)|; tolerance_ABSOLUTE=1e-3 on intercept; GPU=torch.
**Input SHA pins**: D_K eigenvalue caches L=8-12 (shared with W0-3, W0-7).
**Expected output 4-tuple**: (value=R_∞_at_s=3, scheme=Connes-Moscovici-Mellin-cone, convention=s*=3, L_max=12)
**Thresholds**: PASS if convergent AND |fit_residual| < 1e-3; INFO if partial-convergence (monotone but slow); FAIL if divergent (triggers contingency s*).
**Substitution chain**: [VERIFY-THEOREM] — convergence proof in WP §VI.
**Implications**: PASS ⇒ s=3 residue is well-defined; feeds CC-3 (W0-11) and canonical_constants. FAIL ⇒ contingency s* substitution; carry-forward with explicit re-choice.
**Effort**: 5 hours; GPU.
**Substrate-framing reminder**: The Mellin cone IS the substrate's spectral-analytic-continuation domain; residues at integer s* are substrate-intrinsic numbers.

---

## §W0-21. S85-CF-M7-N_T-TWO-SPEED-RE-ADJUDICATION

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge
**Hypothesis**: Under W4-48's two-speed acoustic-metric convention (recovering the substrate's dual phonon/photon propagation speeds), n_T(CMB) at L_max ≥ 8 and a detector projection consistent with CMB-S4+LiteBIRD is re-adjudicated to the framework-consistent value, resolving the L_max<8 truncation ambiguity flagged in S84.
**Method**: Write `s85_w0_n_t_two_speed_readjudication.py` that (a) computes n_T at L_max ∈ {8, 9, 10} under the two-speed metric (c_acoustic, c_photon ratios from canonical_constants), (b) compares to the single-speed computation, (c) projects detector sensitivity (CMB-S4 + LiteBIRD with W0-18 rescue scenarios), (d) emits the re-adjudicated n_T value + detector pull.
**Machinery pin (PRDR)**: L_max ∈ {8, 9, 10}; two_speed_convention=W4-48 canonical; c_acoustic, c_photon from canonical_constants; detector_fisher={CMB-S4: σ=0.01, LiteBIRD: σ=0.02 post-rescue}; GPU=torch.
**Input SHA pins**: W4-48 convention record; W0-18 verdict SHA; canonical_constants.py.
**Expected output 4-tuple**: (value=n_T_twospeed(L=10), scheme=two-speed-metric, convention=W4-48, L_max=10)
**Thresholds**: PASS if |n_T_twospeed − n_T_singlespeed| < 10% of |n_T| AND detector pull ≥ 2 under best rescue scenario; INFO if convention change exceeds 10% but pull ≥ 1; FAIL if pull < 1 OR convention change destabilizes the prediction (> 50% shift).
**Substitution chain**:
  Step 1: n_T under single-speed = S84 W4-48 baseline [def.]
  Step 2: n_T under two-speed = recomputed with (c_acoustic/c_photon) ratio correction [def.]
  Step 3: convention_shift = |n_T_TS − n_T_SS| / |n_T_SS| [def.]
  Step 4: pull = |n_T| / σ_detector [def.]
  Step 5: Direction: PASS if convention_shift < 0.1 AND pull ≥ 2.
**Implications**: PASS ⇒ n_T prediction is convention-robust; CMB-S4 + LiteBIRD is viable falsifier. FAIL ⇒ two-speed convention matters significantly; triggers a convention-canonicalization workshop.
**Effort**: 4 hours; GPU.
**Substrate-framing reminder**: Two-speed acoustic metric reflects the substrate's structural asymmetry between phonon (sound) and photon (light) propagation — both are derived from the a_2 Seeley-DeWitt coefficient with different projection weights.

---

## §W0-22. S85-PLAN-DISCIPLINE-VAN-HOVE-CHECK

**Trigger**: [AUDIT]
**Classification**: META
**Agent**: gen-physicist
**Hypothesis**: The S85 plan's stationarity hypotheses (any gate that claims a τ-, K-, or L_max-stationary point) pass a PRDR consistency check — specifically, each stationarity claim is either (a) proven by a gate in the same wave, or (b) deferred with a named successor gate.
**Method**: Write `s85_w0_plan_discipline_vh_check.py` that (a) scans all S85 plan files (session-85-plan-w0.md through w13.md) for stationarity claims (grep on "stationary", "extremum", "cusp", "τ_fold"), (b) for each claim, verifies (a) a proof-gate exists in the same or earlier wave OR (b) an explicit "deferred to S86" successor tag is present, (c) emits the audit count.
**Machinery pin (PRDR)**: plan_file_glob=sessions/session-plan/session-85-plan-w*.md; stationarity_regex=stationary|extremum|cusp|τ_fold|van hove; successor_tag=DEFERRED-TO-S86-{gate}; GPU=none.
**Input SHA pins**: all W0-W13 plan file SHAs (computed-at-runtime as plans are finalized).
**Expected output 4-tuple**: (value=compliance_count/total, scheme=plan-PRDR, convention=stationarity-claim, L_max=NA)
**Thresholds**: PASS if 100% of claims are either proven-in-wave or DEFERRED-tagged; INFO if ≥ 90%; FAIL if < 90%.
**Substitution chain**: [AUDIT] — plan-property check.
**Implications**: PASS ⇒ plan-layer PRU Class-8 vulnerabilities for stationarity claims are closed. FAIL ⇒ some stationarity claim is unpinned; plan edit + recovery iteration.
**Effort**: 2 hours; CPU.
**Substrate-framing reminder**: Stationarity in the substrate picture refers to extrema of the spectral action — purely geometric extrema on the compact deformation manifold, not dynamical-system attractors.

---

## §W0-23. S85-CC-1-ETA-INVARIANT-FULL-TRIPLE

**Trigger**: [VERIFY-THEOREM]
**Classification**: GEOMETRIC
**Agent**: connes-ncg-theorist
**Hypothesis**: The η-invariant of the full Jensen-SU(3) × A_F spectral triple equals the framework's conjectured closed-form value (integer or small rational), completing the first CC-series closure (CC-1).
**Method**: Write `s85_w0_cc1_eta_invariant.py` that (a) constructs the full D_K on Jensen-SU(3) × A_F at L_max=8, (b) computes η via the Atiyah-Patodi-Singer formula η = (1/√π) ∫₀^∞ Tr(D e^{−tD²}) t^{−1/2} dt / √t regularized, (c) compares to target, (d) emits verdict. Use torch for eigenvalue-sum regularization on GPU.
**Machinery pin (PRDR)**: L_max=8; η_convention=Atiyah-Patodi-Singer-1975; regularization=zeta-at-s=0-derivative; target_candidate_set={1/24, 1/12, 1/6, 7/10, 2/3, 3/4} (dual prediction per S84 connes synthesis §V.3: Weyl-order {1/24, 1/12, 1/6} vs magnitude-match {7/10, 2/3, 3/4}; §IV.6 flags that both cannot simultaneously hold — CC-1 resolves); target_ρ_η_bracket=[0.1, 10] (factor-10 bracket on π × η × M_Pl² × H_0² / ρ_obs per §V.3); M_Pl=2.435e18 GeV (canonical); H_0=1.438e-42 GeV (canonical); ρ_obs=2.7e-47 GeV⁴ (canonical); tolerance_ABSOLUTE=1e-4 on η rounding to candidate set; L_max_convergence_check=|η(L=11) − η(L=9)| / |η(L=9)| < 0.10 (drift tol per §V.3 PASS rule); GPU=torch (mandatory at L_max ≥ 9 per §V.3).
**Input SHA pins**: D_K eigenvalue cache L=8 (and L=9, L=11 for convergence check); APS-1975 reference formulas; S84 connes synthesis record `sessions/archive/session-84/session-84-connes-CCrevisit-synthesis.md` §V.3 + §IV.6 (static); canonical_constants.py for M_Pl, H_0, ρ_obs.
**Expected output 4-tuple**: (value=η_full (nearest-candidate rational), scheme=APS-1975, convention=Jensen-SU(3)-x-A_F, L_max=8)
**Thresholds**: PASS if |η_computed − target| ≤ 1e-4 AND target matches small rational; INFO if 1e-4 < |Δ| ≤ 1e-2; FAIL if > 1e-2.
**Substitution chain**: [VERIFY-THEOREM] — APS formula derivation in WP §VI.
**Implications**: PASS ⇒ CC-1 closure. FAIL ⇒ APS regularization convention issue OR the target is wrong; carry-forward.
**Effort**: 5 hours; GPU.
**Substrate-framing reminder**: The η-invariant is the substrate's signed spectral asymmetry — IS the fabric's chirality number at the τ_fold slice, not a property of the gauge field on a background.

---

## §W0-24. S85-HOOK-WIRING-R3-YAML-NORMALIZATION

**Trigger**: [AUDIT]
**Classification**: META
**Agent**: gen-physicist
**Hypothesis**: The settings.json PostToolUse hook-wiring is fixed to fire the completion-queue log reliably, AND all 24 W0 gate blocks use the R3 YAML schema version with schema_version: R3 key, making v3-closure-audit sig_4 structurally impossible to fail.
**Method**: Write `s85_w0_hook_wiring_r3_yaml.py` that (a) reads `.claude/settings.json`, verifies the PostToolUse hook for agent completion fires to `completion-queue.jsonl`, (b) scans all W0-W13 plan gate blocks for `schema_version: R3` declaration, (c) auto-adds the tag where missing, (d) emits verdict on hook_wiring_OK + schema_coverage_pct.
**Machinery pin (PRDR)**: settings_json_path=.claude/settings.json; hook_name=PostToolUse; target_log=sessions/archive/session-85/completion-queue.jsonl; schema_regex=schema_version:\s*R3; target_coverage=100%; GPU=none.
**Input SHA pins**: .claude/settings.json SHA; each W0-W13 plan file SHA.
**Expected output 4-tuple**: (value=(hook_OK, schema_pct), scheme=R3-YAML-audit, convention=W9-carry-forward, L_max=NA)
**Thresholds**: PASS if hook_OK=True AND schema_pct=100%; INFO if hook_OK=True AND 90% ≤ schema_pct < 100%; FAIL if hook_OK=False OR schema_pct < 90%.
**Substitution chain**: [AUDIT] — infrastructure check.
**Implications**: PASS ⇒ v3-closure-audit sig_4 passes structurally in S85 close. FAIL ⇒ recovery-procedure Stage-1 for sig_4 triggers; infrastructure patch carry-forward.
**Effort**: 3 hours; CPU.
**Substrate-framing reminder**: Infrastructure is not physics, but infrastructure failures cause v3-closure-audit failures that propagate to physics-verdict credibility. Hook-wiring correctness is part of the session's methodological hygiene.

---

## Wave W0 → Wave W1 Decision Point

Wave W1a/W1b (mack-cosmic-bridge) dispatches are cleared when:

- **W0-1 (BETA-S-CMB-S4-PREREG)** verdict line present (feeds W1b items ALPHA-S-PRIOR-RANGE-LCDM, BETA-S-JOINT-S4-HD, and the full alpha-s preregistration chain).
- **W0-4 (DR3-REGULATOR-SUCCESSOR-TREE)** verdict line present (feeds W1a CF-M1 DR3 live-watch, CF-M2 regulator-conditional successor amendment).
- **W0-13 (CMB-S4-ALPHA-FLAGSHIP-DOC)** verdict line present (feeds W1a/W1b explicit CMB-HD, LiteBIRD, Planck-DESI alpha-s pre-registrations).

Wave W2 (connes-ncg-theorist) dispatches are cleared when W0-10/11/12/23 (CC-series) and W0-16 (HP^1) verdicts are present.
Wave W3 (landau-condensed-matter-theorist) dispatches are cleared when W0-15 (CSCANON-IDENTITY) and W0-17 (K-FLOOR-WALL) verdicts are present.
Wave W4 (little-red-dots-jwst-analyst) dispatches are cleared when W0-2 (FOLDED-BISPECTRUM-21CM) and W0-13 verdicts are present.
Wave W9 (feynman-theorist) dispatches are cleared when W0-2, W0-5 (TWO-LOOP-Z), W0-19 (MELLIN-TEMPLATE-LIFT) verdicts are present.
Other waves (W5-W8, W10-W13) are parallel and do not block on W0.

Aggregate clear condition: **W0 must deliver at least 18/24 verdict lines (75%) before Batch 2 (W7-W13) dispatches.**

---

## Wave W0 Machinery-Enumeration Pin (§0.11 PRDR)

Unique machinery parameters across the 24 W0 gates (deduplicated, one row per unique pin):

| Pin | Value / source | Used in gates |
|:----|:---------------|:--------------|
| L_max_primary | 8 | W0-1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 21, 23 |
| L_max_sweep | {8, 9, 10, 11, 12} | W0-3, 7, 20 |
| L_max_sweep_subset | {8, 9, 10} | W0-21 |
| scheme | MS-bar (primary), t'Hooft-lattice (cross), triality-orbit, APS-1975, CM-1995, two-speed | per-gate (see above) |
| convention | Planck-central, Chluba-Sunyaev-2012, Fisher-cosine, Baptista-canonical, Jensen-deformed, CM-2008, Dai-Freed-1994, W4-48, W5-D.4, W6-71, W9 | per-gate |
| GPU_path | torch 2.9.1+rocm on cuda:0 | W0-2, 3, 6, 7, 9 (pathway c), 10, 20, 21, 23 |
| CPU_path | numpy with OMP_NUM_THREADS=8 | W0-1, 4, 5, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 24 |
| random_seed | 42 (where stochastic) | W0-1, 5, 18 |
| tolerance_primary | RATIO 1% (where ratio test); ABSOLUTE 1e-3 to 1e-8 (per-gate) | per-gate |
| mpmath_dps | 50 | W0-5, 9, 11 |
| eigensolver_tol | 1e-10 | W0-3, 6, 7, 10, 20, 23 |
| D_K_eigenvalue_cache | `_DK_eig_cache_L{N}.npz` | W0-3, 6, 7, 10, 11, 12, 15, 16, 20, 21, 23 |
| sigma_forecast_CMB-S4 | Science Book v2 2022 Table 6.1 | W0-1, 13, 21 |
| sigma_forecast_LiteBIRD | Hazumi 2020 Table 5 | W0-18, 21 |
| sigma_forecast_SKA-Phase-2 | Cohen 2017 + 2030 fiducial | W0-2 |
| sigma_forecast_PIXIE | PIXIE Science Book 2011 Table 2 | W0-8 |
| tau_fold_canonical | 0.190 (canonical_constants) | W0-6, 22 |
| K_corridor_bounds | [K_R5=1.9222, K_crit=2.0446] | W0-15, 17 |
| epsilon_H_twist | canonical_constants.eps_H | W0-16 |
| Spin8_triality_orbit_map | Adams-1981 canonical | W0-10 |
| π4_S3_generator | SU(2) instanton k=1 | W0-12 |
| dimension_spectrum_set | {0, 1, 2, 3, 4, 5, 6, 7, 8} | W0-11 |
| DR3_firing_date | 2026-04-23 (hard-pinned) | W0-4 |
| regulator_atlas | W4-44 canonical 5-regulator list | W0-4 |
| pull_PASS_threshold | ≥ 5 (flagship), ≥ 3 (secondary) | W0-1, 8, 18, 21 |
| schema_version | R3 (all W0 blocks) | W0-24 (audits all) |

**PRU cardinality check**: every gate's free parameters are pinned above. D_PRU_raw expected = 0 at plan-freeze.

---

## Wave W0 Input-SHA Ledger

SHAs of all input data consumed by the 24 gates (populated at dispatch time; `<computed-at-runtime>` marks dynamic inputs):

| Gate | Input file | SHA handling |
|:-----|:-----------|:-------------|
| W0-1 | computations/canonical_constants.py | `<computed-at-dispatch>` |
| W0-1 | S84 W6 β_s closure verdict line | `<computed-at-dispatch>` (from computations/s84_gate_verdicts.txt grep) |
| W0-1 | CMB-S4 Science Book Table 6.1 (cached) | static; precompute at dispatch |
| W0-2 | canonical_constants.py | `<computed-at-dispatch>` |
| W0-2 | SKA Phase-2 noise model (Cohen 2017 cache) | static |
| W0-3 | D_K eigenvalue caches at L=8,9,10,11,12 | `<computed-at-runtime>` per L |
| W0-3 | W3-31 C_5_target record | `<computed-at-dispatch>` |
| W0-4 | W4-44 regulator atlas | `<computed-at-dispatch>` |
| W0-5 | Jensen-SU(3) fiber Lagrangian file | static |
| W0-5 | W6 D.1 1-loop Z_R reference verdict | `<computed-at-dispatch>` |
| W0-6 | D_K construction kernel | static |
| W0-6 | W8a-85 audit-consensus record | `<computed-at-dispatch>` |
| W0-7 | D_K eigenvalue caches L=8-12 (shared with W0-3) | runtime |
| W0-7 | Zubarev kernel definition file | static |
| W0-8 | PIXIE Science Book values | static |
| W0-8 | W5-57 closure verdict | `<computed-at-dispatch>` |
| W0-9 | D_K eigenvalue cache L=8 | runtime |
| W0-9 | SU(3) Casimir reference table | static |
| W0-10 | D_K eigenvalue cache L=8 | runtime |
| W0-10 | Spin(8) orbit-map file | static |
| W0-10 | S84 connes CC-2 target record | `<computed-at-dispatch>` |
| W0-11 | D_K eigenvalue cache L=8 | runtime |
| W0-11 | CM-1995 reference equations file | static |
| W0-12 | Jensen-SU(3) fiber structure | static |
| W0-12 | Dai-Freed 1994 reference equations | static |
| W0-12 | KO-dim=6 registry entry | `<computed-at-dispatch>` |
| W0-13 | W6 D.4 carry-forward record | `<computed-at-dispatch>` |
| W0-13 | W0-1 verdict SHA | runtime (depends on W0-1) |
| W0-14 | lizzi/vdd S84 synthesis files | `<computed-at-dispatch>` |
| W0-14 | canonical_constants.py (before) | `<computed-at-dispatch>` |
| W0-15 | W5-64 f_B table | `<computed-at-dispatch>` |
| W0-15 | canonical_constants.py | `<computed-at-dispatch>` |
| W0-16 | canonical_constants.py (eps_H) | `<computed-at-dispatch>` |
| W0-16 | CM-2008 reference equations | static |
| W0-17 | W5 D.4 carry-forward record | `<computed-at-dispatch>` |
| W0-17 | canonical_constants.py | `<computed-at-dispatch>` |
| W0-18 | S84 W4-41 n_T record | `<computed-at-dispatch>` |
| W0-18 | Hazumi 2020 values | static |
| W0-19 | W6-71 canonical boilerplate | static |
| W0-19 | 16 Mellin-balance scripts | `<computed-at-dispatch>` (each) |
| W0-20 | D_K eigenvalue caches L=8-12 (shared) | runtime |
| W0-21 | W4-48 convention record | `<computed-at-dispatch>` |
| W0-21 | W0-18 verdict SHA | runtime |
| W0-22 | all W0-W13 plan files | `<computed-at-dispatch>` |
| W0-23 | D_K eigenvalue cache L=8 | runtime |
| W0-23 | APS-1975 reference formulas | static |
| W0-24 | .claude/settings.json | `<computed-at-dispatch>` |
| W0-24 | all W0-W13 plan files | `<computed-at-dispatch>` |

**Total unique inputs**: 26 distinct files/records. **Static (pre-cached) hashes**: 11. **Computed-at-dispatch**: 15.

---

## Wave W0 Completion Criteria

Wave W0 is declared complete when:

1. All 24 verdict lines present in `computations/s85_gate_verdicts.txt` with dual-SHA (content_sha256 + audit_sha256 companion rows).
2. All 24 producing scripts `s85_w0_<slug>.py` present in `computations/` with non-trivial size (> 2 KB each).
3. Each gate's `.npz` / `.png` artifact produced where method promises one (W0-1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 18, 20, 21, 23 — 17 gates).
4. Substitution chain written in the working-paper §VI.W0-{N} section for every [SIGN]/[VERIFY] gate (W0-1, 2, 4, 5, 8, 15, 17, 18, 21, plus the AUDIT gates' presence-check derivations).
5. v3-closure-audit signals sig_1 through sig_5 checked; sig_1 (PRU D_raw) expected = 0 per the machinery pin table above.

Upon W0 completion, downstream waves W1a/W1b, W2, W3, W4, W9 are unblocked per the Wave W0 → Wave W1 Decision Point section.
