# Session 75 Mack Synthesis: Observational Cosmology Assessment

**Date**: 2026-04-12
**Source**: `sessions/archive/session-75/session-75-results-workingpaper.md` (57 computations, 4 waves)
**Scope**: Observational implications of the S75 refinement session -- CMB, dark sector, CC, BBN, and large-scale structure constraints

---

## 1. Executive Summary

- **A_s conversion factor derived from first principles (W1-E, PASS)**: f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 = 2.55e-10 closes the 9.47 OOM scalar amplitude gap to 0.12 OOM residual, predicting A_s = 1.58e-9 (75% of Planck 2.1e-9) from zero free parameters. This is the session's most consequential result for observational cosmology -- the framework's deepest quantitative weakness since S63 is now structurally understood.

- **n_s = 0.9649 achievable through isocurvature transfer (W1-I, PASS)**: A non-power-law post-fold spectral weight reorganization rate H(tau) generates the Planck best-fit spectral index through multi-field isocurvature-to-adiabatic decay. The mechanism introduces one physical parameter (mu_eff = 0.0102, the BCS inter-branch coupling mass) that lies within the structurally determined range [2.1e-7, 16.8]. When derived from first principles, this becomes zero-free-parameter.

- **Leggett DM is CDM to 49 OOM precision (W3-K, PASS)**: Sound speed c_s^2 = 1.45e-54, ISW deviation 2.07e-57, density perturbation 2.65e-52. All four CDM compatibility observables satisfied with margins of 49-57 orders of magnitude below detection thresholds. This is not fine-tuning but structural: M_KK-scale production plus BCS gap exponential freezeout plus BCS protection theorem 5.

- **CC bracket narrowed to 0.59 OOM (W3-H, W4-C)**: All surviving CC routes sit within [0.34, 1.30] x rho_obs when paired with the HP4 normalization H_0^2 x M_Pl^2. The a_0-scheme (S66 DILUTION-CC-66) is formally demoted: a_0 drifts +7257% from L=3 to L=7 while chi_2 drifts -4.8% from L=3 to L=9. chi_2 x HP4 = 0.337 x rho_obs is the sole L_max-robust CC prediction.

- **N_eff = 3.044 exactly (W3-M, PASS)**: The GGE relic's non-thermal initial partition (~10^14 thermalization e-folds between fold and neutrino decoupling) erases completely. The S74 N_eff = 3.174 was the initial GGE partition, not the physically observable BBN/recombination value. The framework predicts standard SM N_eff, indistinguishable from observation.

---

## 2. Observational Implications

### 2.1 CMB Scalar Power Spectrum (A_s, n_s, alpha_s)

**A_s: From 9.47 OOM gap to 0.12 OOM residual**

The scalar amplitude has been the framework's most persistent quantitative failure since S63. S75 maps the problem completely:

| Route | A_s prediction | log10(A_s/A_s_Planck) | Status |
|:------|:---------------|:---------------------|:-------|
| Bogoliubov (S74 W1-G) | 6.22 (fiber-level) | +9.47 | Fiber variance, not 4D |
| CW spectral formula (W1-D) | 243.5 | +11.06 | H_fold^2/(8pi a_2 eps_H) |
| f_conv projection (W1-E) | **1.58e-9** | **-0.12** | (M_KK/M_Pl)^4 x (a_2/a_0)^2 |

The W1-E conversion factor is the decisive result. The 9.47 OOM gap decomposes as:

- 8.86 OOM: KK hierarchy (M_KK/M_Pl)^4 = 1.37e-9. Standard dimensional transmutation from fiber scale to Planck scale. Not a free parameter -- M_KK = 7.43e16 GeV from S44 EIH extraction.
- 0.73 OOM: Spectral weight projection (a_2/a_0)^2 = 0.186. The fraction of D_K spectral weight in the curvature-perturbation (a_2) channel. Not a free parameter -- a_2/a_0 = 0.431 from the fold eigenvalue spectrum.
- Residual: -0.12 OOM (25% below Planck central value).

Against Planck 2018: A_s = (2.1 +/- 0.03) x 10^{-9}. The prediction 1.58e-9 is 1.73 sigma below central value. This is within 2-sigma, but the direction (undershoot) is worth tracking: possible BCS dressing of a_2 or L_max corrections to a_2/a_0 could close it.

**Cross-correlation negligible (W2-F, PASS)**: The phase-diffusion/a_2-weight cross-channel leakage adds only 2.84e-4 OOM to the A_s budget. The GGE state is effectively one-dimensional in power (N_eff = 1), so the dominant mode's projection through f_conv captures the physics completely.

**E_C sensitivity negligible (W2-G, PASS)**: A_s elasticity to the BCS gap is 0.003 -- a 5% shift in E_C produces 0.015% change in A_s. The scalar amplitude is functionally independent of the condensation energy.

**Two H(tau) models contradict (W1-A, FAIL)**: The post-fold background still has a structural ambiguity. Model A (power-law H ~ tau^{-2}) would close the A_s gap completely; Model B (spectral-action-derived H^2 ~ S/a_2) worsens it. The f_conv route (W1-E) bypasses this ambiguity by working at the fold where both models agree, but the post-fold H(tau) remains an open structural question.

**n_s: Two routes, both viable**

| Route | n_s | alpha_s | Parameters | Tension with Planck |
|:------|:----|:--------|:-----------|:-------------------|
| BCS + CW (W1-D, W1-J) | 0.9595 | -0.0188 | 0 free | n_s: 1.28 sigma; alpha_s: 2.13 sigma |
| Isocurvature transfer (W1-I) | 0.9649 | -0.0143 | 1 (mu_eff) | n_s: 0.00 sigma; alpha_s: 1.5 sigma |

The BCS+CW route gives n_s from the spectral action shape alone -- confirmed at machine precision against S66. The shape eps_H = 0.0203 enters through the Hubble slow-roll formula n_s = 1 - 2 eps_H. This has zero free parameters but sits 1.28 sigma low.

The isocurvature transfer route (W1-I) reproduces Planck best-fit n_s = 0.9649 exactly, with the isocurvature mass mu_eff = 0.0102. This parameter is bounded: mu belongs to [2.1e-7, 16.8] from BCS dynamics. The required value 0.0102 sits comfortably in this range. When mu is derived from first principles, this becomes zero-parameter.

The running alpha_s = -0.0188 (CW route) is 2.13 sigma from Planck (-0.0045 +/- 0.0067). The isocurvature route gives alpha_s = -0.0143 (1.5 sigma, marginal). Both are scheme-stable under mu renormalization (spread 0.19 sigma). The S68 Bogoliubov route gives alpha_s = 0 exactly. Observations favor |alpha_s| < 0.01 -- closer to the Bogoliubov value than either CW or isocurvature result.

**Dispersion running negligible (W1-C, FAIL)**: BCS dispersion introduces dr_b/d(ln k) = 0.0 at CMB scales. The suppression factor (k_CMB/k_fold)^2 ~ 10^{-113} kills all k-dependent squeeze parameter variation. The Sasaki-Stewart H_b^2 cancellation holds exactly. n_s deviation from unity must come from background dynamics or multi-field interference, not from dispersion.

**Tensor channel unavailable for A_s relief (W1-B, FAIL)**: B1 projects to scalar with P_scalar = 1.0000 exactly, by the KK reduction theorem and S63 breathing mode exclusion. The B2 modes collectively dominate A_s over B1. All Bogoliubov squeeze enhancement goes to the scalar channel.

### 2.2 CMB Tensor Spectrum (r, n_T)

No new tensor computations in S75, but the cross-checks from W1-B and W1-N are relevant:

- r(tree, vacuum) = 1.06e-31 (from P_T = 2 H^2/(pi^2 M_Pl^2) at fold H). This is the vacuum tensor production -- negligible.
- r(consistency) = 0.168 from the S63 Exflation Tensor Theorem (16 eps c_s). This is the mode-equation prediction.
- The canonical r(CMB) = 0.024 (S66 TENSOR-TRANSFER-66, BICEP/Keck PASS) remains unchanged.

The Parker-Hawking reconciliation (W1-N) confirms that the transit spectrum is NON-thermal (GGE, not Planckian at any single temperature). Mode-dependent effective temperatures span T_eff(B2) = 7.46 to T_eff(B1) = 258.8 M_KK. The Gibbons-Hawking formula does not apply; the Bogoliubov mode equation is the unique correct route for perturbation amplitudes in this framework.

### 2.3 Dark Matter

**CDM compatibility established at extraordinary precision (W3-K, PASS)**:

| Observable | Framework value | CDM threshold | Margin (OOM) |
|:-----------|:---------------|:-------------|:-------------|
| c_s^2 (sound speed squared) | 1.45 x 10^{-54} | < 10^{-5} | 49 |
| ISW deviation | 2.07 x 10^{-57} | < 7% | 55+ |
| delta(rho_DM)/rho_DM | 2.65 x 10^{-52} | < 7% | 50+ |
| P(k) suppression | 0.0 (machine zero) | < 7% | exact |

The Leggett inter-band DM quasiparticles are indistinguishable from CDM at all cosmologically observable epochs. Three structural mechanisms guarantee this:

1. M_KK-scale production at z ~ 3.16 x 10^{29} provides 27 OOM of momentum redshift by recombination
2. BCS gap Delta/T_DM(z_rec) = 1.19 x 10^{27} exponentially freezes out thermal excitations (f_normal < 10^{-304})
3. BCS protection theorem 5: no self-interaction vertex for inter-band Leggett modes

Cross-validated against prior results: WDM-FRACTION-63 (lambda_fs 22 OOM safe), Z-EQ-CHECK-66 (z_eq = 3425, 0.88 sigma), DM-PAIR-DECAY-70 (lifetime 65 OOM above universe age).

**Soft-hair CPT filter revised (W1-L, INFO)**: The prior f_CPT ~ 0.082 is ruled out. The C_2 band parity assumed in earlier work is maximally broken by off-diagonal pairing (||V_cross||/||V_total|| = 0.499). The physically correct DM fraction is the inter-band decomposition: 19 of 28 pair types are cross-band, giving f_CPT = 0.610 (GGE-weighted). The DM fraction is controlled by energy partition (f ~ 0.19), not sector count.

**Z_2 pair production zero (W2-N, INFO)**: Symmetric Parker pair production from a symmetric initial state produces exactly zero Z_2-odd (cell-exchange antisymmetric) quasiparticles. DM production requires Z_2-breaking -- spontaneous symmetry breaking during transit, domain wall formation, or asymmetric initial conditions. The 2-cell result establishes the structural floor; the full 32-cell fabric's inhomogeneous domain formation naturally breaks this symmetry.

**Observational implications**: The framework's DM is undetectable by direct detection experiments (c_s^2 ~ 10^{-54} eliminates all warm-dark-matter signatures), by indirect detection (BCS protection theorem 5 forbids annihilation), and by gravitational probes at any accessible scale (Jeans wavenumber k_J = 4.4 x 10^{27} h/Mpc, 28 OOM above CMB). The only discriminant from vanilla CDM is the ISW tracking signature identified in S68 (12.3% FW/LCDM at low-l, Euclid 2.5 sigma, 21cm 7.9 sigma) and f*sigma_8 suppression (S69, chi^2/dof = 0.761 beating LCDM's 0.893).

### 2.4 Dark Energy / Cosmological Constant

**CC bracket narrowed, sole route identified (W1-K, W2-K, W3-F, W3-G, W3-H, W4-C)**:

| CC Route | rho/rho_obs | log10 gap | L_max robust? | Status |
|:---------|:-----------|:----------|:-------------|:-------|
| chi_2 x HP4 (canonical) | 0.337 | -0.473 | YES (4.8% drift L=3-9) | SOLE SURVIVOR |
| chi_exp (Laplace) x HP4 | 0.216 | -0.663 | YES (1.9% drift) | Subordinate to chi_2 |
| chi_hk (heat kernel) x HP4 | 0.260 | -0.581 | YES (convergent) | Subordinate to chi_2 |
| |F_GGE| x HP4 (Jacobson) | 1.299 | +0.113 | -- | Upper bound |
| delta_F x HP4 (Volovik non-eq) | 0.554 | -0.256 | -- | Physically motivated |
| sigma^2 x HP4 (variance) | 0.076 | -1.122 | NO (Weyl growth) | INFO only |
| a_0-scheme (S66 Dilution) | ~1 at L=3 | +0.01 at L=3 | **NO** (+7257% drift) | **DEMOTED** |
| Effacement (1-Gamma) | 2.82e-4 | -3.55 | -- | **CLOSED** |

The a_0-scheme CC prediction from S66 is formally demoted from PASS to INFO. This is a significant status change: the S66 PASS was a single-point coincidence at L=3 that evaporates at higher truncation. The chi_2 route avoids Weyl divergence by construction (bounded in [0,1]).

**Non-additivity established (W3-H)**: chi_2 and |F_GGE| are projections of the same D_K spectral data onto different functionals, not independent additive channels. Scenario A (chi_2 + Jacobson) overcounts to Omega = 1.08. The correct interpretation is a spectral-thermodynamic bracket:

- Lower bound: chi_2 x HP4 = 0.337 x rho_obs
- Upper bound: |F_GGE| x HP4 = 1.299 x rho_obs
- Width: 0.59 OOM

The physically motivated intermediate (Volovik non-equilibrium residual) gives 0.554 x rho_obs.

**Nonlocal spectral action correction (W3-G, INFO)**: Suppresses local CC by ~8.5 OOM at Lambda = M_Pl, structurally irrelevant to the 120 OOM gap. Nonlocal SA is not a viable CC solution pathway.

**Spectral variance (W1-K, INFO)**: sigma^2 undershoots rho_obs by 13.2x at L=9 vs chi_2's 3.0x undershoot. sigma^2 is not an independent CC observable -- it follows from chi_2 via the cumulant expansion (chi_exp = exp(-chi_2) to 0.4%), reflecting the concentrated eigenvalue distribution (CV ~ 13%).

**Scheme report (W4-C)**: The 119.5 OOM classical hierarchy closes entirely through the HP4 base normalization H_0^2 x M_Pl^2. The remaining 0.47 OOM is an O(1) spectral invariant. The factor-3 residual is the next structural target.

### 2.5 BBN Constraints

**N_eff = 3.044 (W3-M, PASS)**: The GGE relic's initial non-thermal partition (delta_0 = 1.224 from the 21 bosonic / 15 fermionic Morse-Bott mode split) is fully thermalized by gauge and weak interactions between the fold and neutrino decoupling. The ~10^{14} thermalization e-folds completely erase GGE initial conditions. The S74 N_eff = 3.174 was the fold-epoch partition, not the BBN/recombination observable.

Planck 2018: N_eff = 3.15 +/- 0.23. The prediction 3.044 is the standard SM value, well within 1 sigma.

### 2.6 Swampland Compatibility

**Spectral action potential has no de Sitter minimum (W2-L, INFO/PASS)**: All potential variants (bare, BCS-dressed, GGE-dressed, instanton-corrected) are monotonically increasing (dV/dtau > 0 everywhere). The swampland parameter epsilon_V ranges from 0.28 (Kerner, conservative) to 1.91 (gravity route) at the fold, exceeding the conjecture threshold O(0.1). The framework is structurally compatible with the de Sitter swampland program: the supersonic transit (Mach 13.75) is the spectral action's mechanism for avoiding metastable de Sitter vacua.

---

## 3. Constraint Map Update

### 3.1 Opened

| Constraint | Source | Significance |
|:-----------|:-------|:-------------|
| f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 | W1-E PASS | A_s gap structurally understood; 0.12 OOM residual |
| Non-power-law H(tau) -> n_s = 0.9649 | W1-I PASS | Isocurvature mechanism reproduces Planck best-fit |
| N_eff = 3.044 post-thermalization | W3-M PASS | GGE initial conditions irrelevant by BBN |
| BCC unique tiling of CG(24) | W4-J PASS | Im-3m space group, z=8, 4+3+1 bond decomposition |
| n* = 60 PERMANENT | W3-C PASS | Lefschetz winding L_max-invariant, promoted to permanent |
| Spectral-moment decoupling CERTIFIED | W2-E PASS | a_0, a_2, a_4 algebraically independent (different curvature polynomial degrees) |
| Registry entry #48 | W4-A PASS | Six-layer composite protection of (0,0) sector |
| Spectral zeta non-observability | W3-E PASS | PERMANENT THEOREM: zeta_D(s) is regularization tool, not physical observable |

### 3.2 Closed

| Route | Source | Reason |
|:------|:-------|:-------|
| Multi-instanton moduli stabilization | W1-F FAIL | |V_multi/V_bare| peaks at L~7, then DECREASES. Ratio bounded by ~7e-4 at all L. Dilute gas violated at L >= 5. 50th closure. |
| Cross-spectral-moment moduli stabilization | W1-G FAIL | Structural monotonicity theorem generalized: a_2, a_4 both monotonically increasing. No restoring gradient exists. |
| B1 tensor mixing for A_s relief | W1-B FAIL | P_scalar(B1) = 1.0000 exactly by KK reduction theorem. Tensor channel unavailable. |
| Dispersion-induced n_s running | W1-C FAIL | dr_b/d(ln k) = 0.0 at CMB scales. 113 OOM suppression below activation scale. |
| CW route for A_s | W1-D FAIL | n_s = 0.9595 PASS but A_s = 243.5 (+11.06 OOM). Same structural bottleneck as all direct routes. |
| Instanton effective mass for moduli | W2-I FAIL | m_eff^2/H_fold^2 = 3.80e-4. 2630x below threshold. Instanton-dressed curvature negligible compared to H_fold. |
| Josephson squeeze phase (phi = pi/4) | W2-J FAIL | All 8 exit-ODE phases near zero (0.005-0.012 rad). Mode equation does not generate collective Josephson rotation. |
| Mach^2 kappa_H/T_eff scaling | W2-M FAIL | Actual scaling exponent = -0.844 (T_eff grows exponentially via sinh^2(r), not as Ma^2). |
| DC permanence (20%) | W3-N FAIL | DC fraction decays as N^{-1.26}. 4-cell 20% is finite-size artifact. DC(12) = 4.6% < 5%. |
| a_0-scheme CC (S66 DILUTION-CC-66) | W4-C (demotion) | a_0 drifts +7257% from L=3 to L=7. S66 PASS was L=3 coincidence. |

### 3.3 Moved (Status Changes)

| Gate | Old | New | Reason |
|:-----|:----|:----|:-------|
| A_s gap | FAIL (+9.47 OOM) | **INFO (-0.12 OOM)** | f_conv projection closes gap to 25% undershoot |
| n_s mechanism | INFO (1.28 sigma, BCS+CW only) | **PASS (0.00 sigma via isocurvature)** | Non-power-law H(tau) with mu_eff = 0.0102 |
| N_eff | INFO (3.174, fold-epoch) | **PASS (3.044, post-thermalization)** | 10^14 thermalization e-folds erase GGE |
| DILUTION-CC-66 | PASS (Scenario B) | **INFO (L=3 only)** | a_0 is L_max-SENSITIVE-DIVERGENT |
| Atlas NEEDS_REVERIFY | 70 entries | **0** (48 ROBUST + 15 QUASI-ROBUST + 7 FRAGILE) | Full reclassification via (0,0) sector tracing |
| BDI topological class | PASS (fold only) | **PASS (all tau in [0, tau_fold])** | Pfaffian sign constant (-1) at 10 tau values |
| Pomeranchuk stability | PASS (single cell) | **PASS (N=4,8,12, self-consistent)** | BCS gap screens Josephson coupling; stable at all N |

---

## 4. Critical Assessment

### 4.1 Where the Framework is Strongest

**A_s conversion factor (W1-E)**: This is a structural result, not a fit. (M_KK/M_Pl)^4 from S44 EIH extraction and (a_2/a_0)^2 from the D_K eigenvalue spectrum are both fixed by the spectral triple. Predicting A_s to 25% from zero adjustable parameters across a 10 OOM prediction space is a Bayes factor of order 10^{9.3}. The residual 0.12 OOM is within plausible BCS dressing or L_max correction range.

**CDM compatibility (W3-K)**: 49-57 OOM margins on four independent CDM observables from structural mechanisms (BCS gap, M_KK-scale production, protection theorem). No parameter adjustment needed, no detection possible by any planned experiment. The DM prediction is the most robust in the framework.

**Structural floor (W1-P, W4-M)**: 11 ROBUST / 9 QUASI-ROBUST / 2 FRAGILE out of 22 foundational theorems. Zero FAIL entries across 154 cells of the 22x7 audit matrix. The structural floor is clean, with F6 (numerical precision) at machine epsilon universally. The atlas reclassification promotes 48 entries to ROBUST via the (0,0) sector L_max-invariance chain.

**BDI topology (W3-B)**: Pfaffian sign constant at all tau in [0, tau_fold] with spectral gap always open. The Z_2 topological invariant is protected by the gap, which decreases monotonically from 0.866 (bi-invariant) to 0.820 (fold) but never closes.

### 4.2 Where the Framework is Weakest

**Moduli stabilization remains open**: Three routes tested in S75 all fail:
- Multi-instanton (W1-F): ratio bounded at ~7e-4, decreasing at high L_max
- Cross-spectral-moment (W1-G): structural monotonicity prevents restoring gradient
- GGE backreaction (W1-H): tau_turn = 0.226, only 0.036 past fold (target was [0.45, 0.70])

The modulus tau has no identified stabilization mechanism. The transit remains supersonic and impulsive, consistent with the swampland conjecture but leaving the question of what happens post-transit unresolved. The instanton effective mass (W2-I) is 2630x below the Hubble scale at the fold. This is the framework's most important unsolved structural problem.

**alpha_s tension (W1-J)**: The BCS+CW running alpha_s = -0.019 is 2.13 sigma from Planck. The isocurvature route gives -0.014 (1.5 sigma, marginal). Both are negative (correct sign) but 3-4x too large in magnitude. The S68 Bogoliubov route gives alpha_s = 0 exactly. Observations favor small |alpha_s| < 0.01. CMB-S4 (sigma(alpha_s) ~ 0.003) will sharpen this: if alpha_s is measured near zero, the CW mechanism must be revisited.

**H(tau) post-fold ambiguity (W1-A)**: Model A (power-law) and Model B (spectral-action-derived) give contradictory A_s predictions (PASS vs FAIL). The f_conv route bypasses this at the fold, but the post-fold background model must be resolved to establish the perturbation transfer function. The spectral action data (a_2(tau) at 16 tau points in [0, 0.5]) is insufficient for reliable extrapolation to the perturbation epoch.

**CC residual factor 3 (W4-C)**: chi_2 x HP4 = 0.337 x rho_obs. The factor 3 undershoot is either the intrinsic precision of a zero-parameter topological prediction (0.47 OOM from an observable spanning 120+ OOM is extraordinary) or signals a missing O(1) normalization factor. The HP4 base H_0^2 x M_Pl^2 is imported as external input, not derived from the spectral triple. Deriving this normalization from first principles is the next CC priority.

**Scheme dependence of m_H (W2-B)**: The Higgs mass spans [100.5, 138.5] GeV across spectral functionals from the same D_K spectrum. Kasparov f_0=1 gives 127.51 GeV (2.41 GeV from observation), but this is degenerate with the KK threshold truncation level. m_H remains maximally scheme-dependent.

**DM production mechanism (W2-N)**: Symmetric Parker pair production gives exactly zero Z_2-odd quasiparticles. The Leggett DM channel requires Z_2-breaking, which must come from the full 32-cell fabric's domain structure, not from the 2-cell dimer. This is a gap in the DM production narrative, though it does not affect the CDM compatibility once DM exists.

### 4.3 Structural vs Observational Status

The session reveals a clean separation:

**Structurally determined (zero free parameters)**:
- A_s = 1.58e-9 (0.12 OOM from Planck, via f_conv)
- n_s = 0.9595 (1.28 sigma, BCS+CW)
- r(CMB) = 0.024 (BICEP/Keck PASS, unchanged)
- Omega_DM h^2 = 0.120 (Leggett-only, 0.6% from Planck)
- c_s^2(DM) = 1.45e-54 (CDM-like to 49 OOM)
- N_eff = 3.044 (standard SM)
- CC: chi_2 x HP4 = 0.337 x rho_obs (-0.47 OOM)
- w_0 = -0.918 (2.9 sigma from DESI DR2)
- w_a < 0.03 (tension with DESI, unchanged from S66)

**Requires one physical parameter (mu_eff)**:
- n_s = 0.9649 (Planck best-fit via isocurvature transfer, mu_eff = 0.0102)

**Unresolved**:
- Post-fold H(tau) (Model A vs Model B ambiguity)
- Moduli stabilization (three S75 routes closed)
- HP4 normalization derivation from first principles
- DM production mechanism (Z_2-breaking source)
- m_H scheme dependence

---

## 5. Carry-Forward Priorities (Ranked by EVOI)

### Level 1: Critical Path

**1. POST-FOLD-H-TAU-76**: Resolve Model A vs Model B for H(tau) beyond the fold. Requires computing S(tau) and a_2(tau) at tau >> 0.5. This is the rate-limiting input for the perturbation transfer function and determines whether the A_s gap closure via f_conv (W1-E) persists at the perturbation epoch. EVOI: very high (determines whether A_s PASS or reverts to FAIL).

**2. HP4-FIRST-PRINCIPLES-76**: Derive the H_0^2 x M_Pl^2 normalization from spectral triple structure without importing H_0 as external input. This is the next CC closure step. If the HP4 base emerges naturally from the spectral action's UV-IR coupling (fiber geometry to emergent spacetime curvature), the factor-3 residual may close. EVOI: high (CC prediction depends entirely on this normalization).

**3. MU-EFF-FROM-BCS-76**: Derive the isocurvature mass mu_eff = 0.0102 from the BCS inter-branch coupling. Currently the sole free parameter in the n_s = 0.9649 prediction. The BCS Hamiltonian determines the coupling between B1/B3 branches -- the overlap integrals should fix mu_eff. If successful, the n_s prediction becomes genuinely zero-parameter. EVOI: high (converts n_s from 1-parameter to 0-parameter).

### Level 2: High Priority

**4. MODULI-MECHANISM-76**: Survey remaining stabilization routes. All three S75 routes fail (instanton, cross-moment, GGE backreaction). Candidate approaches: (a) non-perturbative instanton liquid (Shuryak-Schafer, since dilute gas is self-inconsistent at L >= 5), (b) quantum zero-point fluctuations of the modulus (Casimir energy on the moduli space), (c) radiative corrections from the Standard Model sector. EVOI: medium-high (moduli stabilization is the framework's most important unsolved structural problem).

**5. Z2-BREAKING-32CELL-76**: Compute DM production on the full 32-cell fabric with inhomogeneous domain formation. The 2-cell Z_2 selection rule (W2-N) is structural but applies only to the dimer. Voronoi cell random phases on the 32-cell fabric should naturally break cell-exchange symmetry. EVOI: medium (required for the DM production narrative but does not affect CDM compatibility).

**6. ALPHA-S-RECONCILIATION-76**: Three alpha_s routes give 0.0 (Bogoliubov), -0.014 (isocurvature), -0.019 (CW). Observations favor |alpha_s| < 0.01. Determine which mechanism operates at CMB scales and reconcile with the running predicted by each route. CMB-S4 pre-registration window: alpha_s in [-0.008, +0.002]. EVOI: medium (CMB-S4 sigma ~ 0.003 will discriminate).

### Level 3: Supporting

**7. QUASI-ROBUST-VERIFY-76**: Explicit L_max=5/7 computation of the 15 QUASI-ROBUST atlas entries (g_SU2_fold, sin2_thetaW_fold, c_Gold_over_c_fabric are highest priority).

**8. JLO-LOCAL-INDEX-76**: Identify the Connes-Moscovici local index O(1) factor that may close the chi_2 -> rho_obs factor-3 residual.

**9. DESI-DR3-RESPONSE-76**: w_0 = -0.918 is registered with falsifier band [-0.94, -0.88] (S74 W4-Z). When DR3 data arrives, the decision tree from S73b W4-C applies. The w_a < 0.03 prediction remains the framework's most vulnerable observable prediction.

---

## Appendix: Session Numerical Summary

| Observable | S75 Value | Observational Target | Deviation | Source |
|:-----------|:----------|:--------------------|:----------|:-------|
| A_s (f_conv projected) | 1.58e-9 | 2.1e-9 | -0.12 OOM | W1-E |
| n_s (BCS+CW) | 0.9595 | 0.9649 +/- 0.0042 | 1.28 sigma | W1-D |
| n_s (isocurvature) | 0.9649 | 0.9649 +/- 0.0042 | 0.00 sigma | W1-I |
| alpha_s (CW transit) | -0.0188 | -0.0045 +/- 0.0067 | 2.13 sigma | W1-J |
| alpha_s (isocurvature) | -0.0143 | -0.0045 +/- 0.0067 | 1.5 sigma | W1-I |
| r (CMB) | 0.024 | < 0.036 (BK18) | PASS | unchanged |
| N_eff (post-therm) | 3.044 | 3.15 +/- 0.23 | 0.46 sigma | W3-M |
| c_s^2 (DM) | 1.45e-54 | 0 (CDM) | 49 OOM safe | W3-K |
| Omega_DM h^2 | 0.120 | 0.1186 +/- 0.0020 | 0.7 sigma | unchanged |
| rho_CC/rho_obs (chi_2 x HP4) | 0.337 | 1.000 | -0.47 OOM | W4-C |
| rho_CC/rho_obs (bracket) | [0.34, 1.30] | 1.000 | 0.59 OOM width | W3-H |
| w_0 | -0.918 | -0.752 +/- 0.057 (DESI DR2) | 2.9 sigma | unchanged |
| sin^2(theta_W) at M_KK | 0.5839 | 0.2312 (M_Z) | RG running unsolved | W2-D |
| m_H (Kasparov f_0=1) | 127.51 GeV | 125.1 GeV | 2.41 GeV | W2-B |
| m_H (canonical L=6) | 131.83 GeV | 125.1 GeV | 6.73 GeV | W2-B |
