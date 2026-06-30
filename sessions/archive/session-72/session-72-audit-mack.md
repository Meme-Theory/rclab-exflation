# Session 72 Project Audit: Observational Status

**Date**: 2026-04-10
**Author**: Katie Mack (Cosmic Bridge)
**Scope**: Exhaustive audit of observational confrontations through S72
**Sources**: pre-registered-observations.md, constraint-mega-matrix.md, evoi-framework.md, atlas-08-open-questions.md, S72 working paper, S72 Mack-VdD workshop, S72 laminar flow workshop, agent memory S57-S72

---

## I. Pre-Registered Predictions Scorecard

### Tested (12)

| # | Observable | Prediction | Data | Tension | Gate | Session | Scheme Layer |
|:--|:-----------|:-----------|:-----|:--------|:-----|:--------|:-------------|
| 1 | n_s | 0.9567 (bare) | 0.9649 +/- 0.0042 (Planck 2018) | 1.95-sig | BCS-DRESSED-SA-72 INFO | S72 | Functional |
| 2 | r (CMB) | 0.024 | < 0.036 (BK18, 95% CL) | PASS (1.49x headroom) | TENSOR-BURST-64 PASS | S64/S66 | Metric |
| 3 | w_0 | -0.918 | -0.752 +/- 0.057 (DESI DR2+DESY5) | 2.91-sig | DESI-VOLOVIK-67 | S67-68 | Topology |
| 4 | w_a | 0 (exactly, four-fold locked) | -0.73 +/- 0.25 (DESI DR2+DESY5) | 2.92-sig | WA-REASSESS-66 INFO | S66/S68 | Topology |
| 5 | Omega_DM h^2 | 0.120 (Leggett-only) | 0.1186 +/- 0.0020 (Planck) | 0.70-sig | Z-EQ-CHECK-66 PASS | S66 | Topology |
| 6 | sin^2(theta_W) at M_KK | 0.5839 | (geometric boundary, no direct test) | -- | PERMANENT | S30Ba | Metric |
| 7 | sin^2(theta_W) at M_Z | 0.229-0.378 (thresh. dep.) | 0.23122 (PDG) | 1.2% (Model A) to 54.5% (pure SM) | WEINBERG-72 FAIL | S72 | Metric+Functional |
| 8 | alpha_s (running) | 0 (tree, trivial bundle) to -0.038 (smooth cutoff) | -0.0045 +/- 0.0067 (Planck) | 0.67-sig (tree) / 5.0-sig (cutoff) | RUNNING-NS-63 PASS (tree) | S63/S66 | Functional |
| 9 | A_s | Gap 0.267 OOM (after all corrections) | 2.1e-9 (Planck) | 44-sig (zero-param) | AS-AMPLITUDE-63 FAIL (reduced) | S63-S72 | Functional |
| 10 | CC (rho_vac/rho_obs) | 1.032 (Volovik Scenario B) | 1.0 | 0.01 OOM | DILUTION-CC-66 PASS | S66 | Topology |
| 11 | Mass ordering | Normal (B1<B2<B3, all tau>0) | NO preferred at 2.5-sig (NuFit-6.0) | Consistent | PERMANENT (BDI symmetry) | S56 | Topology |
| 12 | f_NL (equilateral) | -0.313 (phys.) / 0.853 (S67 GGE) | -26 +/- 47 (Planck) | 0.57-sig | GGE-BISPECTRUM-67 INFO, DECOHERENCE-BISPECTRUM-72 PASS | S67/S72 | Topology |

### Partially Tested (5)

| # | Observable | Prediction | Current Status | What Remains |
|:--|:-----------|:-----------|:---------------|:-------------|
| 13 | ISW tracking (c_s^2=0) | +12.3% vs LCDM, +7.6% vs quintessence | A_ISW = 1.00 +/- 0.25 (Planck, 0.49-sig from LCDM) | Euclid tomographic ISW SNR~1.58, 21cm SNR~7.9 |
| 14 | f*sigma_8 | Specific values from w_0=-0.918 tracking | chi^2/dof=0.761 (9 bins), beats LCDM (0.893) | Euclid full survey, joint w/lensing |
| 15 | sigma_8 | 0.799 (S65) | 0.811+/-0.006 (Planck) / 0.766+/-0.03 (lensing) | Between both; correct direction for S8 tension |
| 16 | BAO D_V(z)/r_d | Computed at 7 bins | chi^2/dof=8.23 (DR3 update); LRG2 z=0.706 bottleneck | DESI DR3 combined +8.53 |
| 17 | SNe Ia (Pantheon+) | chi^2/dof=1.025 (1701 SNe) | Delta chi^2=-7.82 (full cov), FW preferred 2.80-sig | Full covariance validated S70 |

### Untested (8)

| # | Observable | Prediction | Why Untested | First Test |
|:--|:-----------|:-----------|:-------------|:-----------|
| 18 | f_NL (folded) | 0.129 | No instrument with sensitivity. sigma(fold)=18.9 Euclid, SNR=0.007 | 21cm (2040s), SNR=3.6-sig |
| 19 | n_T (transit scale) | +0.468 (BLUE, 113x above slow-roll) | 10^37 Hz, 34 decades beyond any detector | Inaccessible |
| 20 | n_T (CMB scale) | -3.02e-3 (=-r/8 exactly) | LiteBIRD insufficient lever arm | LiteBIRD marginal (2034) |
| 21 | Omega_GW (domain walls) | ~10^{-10} at LISA frequencies | Not yet measured | LISA (2035+) |
| 22 | 0-nu-beta-beta (seesaw S_F) | 0 identically (BDI symmetry) | No observed 0nubb | LEGEND-1000, nEXO (2030s) |
| 23 | Leggett channel grav. decay | tau > 4.93e82 s (Z_2 structural) | No direct test of DM stability at this level | Indirect: CMB spectral distortions |
| 24 | Lensing power C_l^{kk} | -1.29% suppression from tracking | Euclid CMB-S4 SNR=2.36 | Euclid (2029+) |
| 25 | Galaxy C_l^{gg} | 0.76-sig combined (49 bins) | Indistinguishable from LCDM | Euclid/DESI combined |

### Summary: 12 tested + 5 partial + 8 untested = 25 pre-registered predictions tracked

---

## II. Critical Observational Tensions

### Active Tensions (3)

**TENSION 1: DESI w_0 (2.91-sigma)** -- SCHEME-INDEPENDENT (Topology layer)

Framework predicts w_0 = -0.918 +/- 0.05 (Volovik partition, S58). DESI DR2+DESY5 measures -0.752 +/- 0.057. The 2.91-sigma tension is the framework's most dangerous confrontation. S72 workshop (E1) establishes this as one of two independent failure modes ("Mode A"). The tension is in the "less negative" direction (DESI closer to zero than framework). The CS one-sided asymmetry (S72 W1-D) means scheme variation preferentially pushes w_0 toward -1 (LCDM), not toward DESI. The Volovik partition mechanism is (0,0)-sector-dependent with exponential insensitivity to the spectral functional, giving residual scheme dependence +/- 0.06 (S72 workshop A-Q2). Even at the extreme of this band (w_0 = -0.858), the DESI tension is 1.86-sigma.

Status: LIVE, escalating toward DR3. Survival condition: w_a > -0.35 (S60 DR3-PREREGISTER-60).

**TENSION 2: DESI w_a (2.92-sigma)** -- SCHEME-INDEPENDENT (Topology layer)

Framework predicts w_a = 0 exactly, locked by four independent mechanisms: GGE integrability + Josephson phase + frozen texture + thermalization barrier (59 OOM gap, S68). DESI DR2+DESY5 measures w_a = -0.73 +/- 0.25. The four-fold lock makes w_a the single most rigid prediction: it cannot be adjusted within the framework. S66 WA-REASSESS-66 closed the substrate compaction mechanism (w_a = +1.121, wrong sign). The pure framework (w_0 = -0.918, w_a = 0) remains the only viable configuration.

Status: LIVE, escalating toward DR3. SN calibration systematic (~0.08 in w_0) is significant fraction of total tension. DR3 with improved SN calibration could shift substantially.

**TENSION 3: n_s (1.95-sigma)** -- SCHEME-DEPENDENT (Functional layer)

Framework predicts n_s = 0.9567 (bare, S72 W3-A v2 confirms BCS dressing negligible: delta = 3.8e-6). Planck measures 0.9649 +/- 0.0042. The 1.95-sigma tension is in the "less red" direction (framework more red than data). S72 W2-C establishes that a positive spectral functional f*(x) = 0.912*sqrt + 0.088*exp exists that matches n_s = 0.9649 exactly. However, this is an accommodation (fitting t* to match Planck), not a prediction. The bare n_s = 0.9567 is the zero-parameter prediction. S72 W3-C (entry-horizon tilt delta_n_s = +1.001) moves the prediction redder (AWAY from Planck), though the additive approximation is suspect for r ~ 3 (compound Bogoliubov product needed, S72 workshop D2).

Status: LIVE, tightening with CMB-S4 (sigma ~ 0.002, 2034). Mode B failure mode.

### Resolved Tensions (3)

| Tension | Resolution | Session |
|:--------|:-----------|:--------|
| r = 0.35 (S62 exclusion risk) | Corrected to r = 0.024 at CMB via tensor transfer function | S66 |
| CC (114 OOM) | Volovik relaxation rho ~ H^2 gives ratio 1.032 (Scenario B) | S66 |
| alpha_s = -0.038 (5.0-sig) | Slow-roll inapplicable at Mach 13.8. alpha_s(CMB) ~ 0 from 56 OOM scale hierarchy. ATDHFB bounds to [-0.019, -0.008]. Full transit PS uncomputed. | S63/S66 |

### Dormant Tensions (2)

| Tension | Status | Why Dormant |
|:--------|:-------|:------------|
| A_s gap (0.267 OOM) | OPEN | Reclassified as normalization (kappa free parameter, standard NCG). S72 E2: gap = pure decoherence timescale problem. 44-sig as zero-param; 0-sig with kappa. |
| sin^2(theta_W) at M_Z (54.5%) | OPEN | Pure SM running excluded. Model A (universal thresh.) gives 1.2%, but undemonstrated at tau_fold. PW-SECTOR-THRESHOLD-73 needed. |

---

## III. Upcoming Data Confrontations (with dates)

### 2026-2027: DESI DR3 (SURVIVAL OR EXCLUSION)

Pre-registered scenarios (S60 DR3-PREREGISTER-60, updated S70 DESI-DR3-UPDATE-70):

| Scenario | DR3 Outcome | FW Tension | LCDM Tension | FW Status |
|:---------|:------------|:----------:|:------------:|:---------:|
| A: confirms DR2 (DESY5) | w_0=-0.75, w_a=-0.73 | 3.91-sig | 6.25-sig | **EXCLUDED** |
| B: toward LCDM | w_0=-0.90, w_a=-0.30 | 2.06-sig (w_a=0.066), 2.14-sig (w_a=0) | 2.12-sig | **SURVIVES** |
| C: more dynamical | w_0=-0.65, w_a=-1.0 | 6.33-sig | 37.1-sig | **EXCLUDED** |

Decision rule: w_a > -0.35 framework survives. w_a < -0.530 framework fails at 3-sigma.

BAO-specific: chi^2/dof = 8.23 (DR3 update, S70). LRG2 z = 0.706 is the bottleneck bin. Combined offset +8.53.

This is the framework's make-or-break confrontation. No other experiment operates on this timescale.

### 2028-2030: JUNO / Hyper-K (Neutrino Mass Ordering)

Framework predicts Normal Ordering (structural: B1<B2<B3 at all tau>0, BDI symmetry). JUNO expected 3-sigma by 2028, 3-sigma+ by 2030. Pre-registered gate: PASS if NO at >3-sigma. FAIL if IO at >3-sigma.

Current status: NO preferred at 2.5-sigma (NuFit-6.0). Consistent.

### 2029-2032: Euclid DR1/DR2

| Observable | FW Prediction | Euclid Precision | SNR |
|:-----------|:-------------|:----------------|:----|
| ISW tracking (c_s^2=0) vs Quint | +7.6% | marginal | 1.58 |
| ISW tracking vs LCDM | +12.3% | marginal | -- |
| f*sigma_8 | chi^2/dof=0.761 | competitive in combination | -- |
| Lensing C_l^{kk} | -1.29% suppression | CMB-S4 cross needed | SNR=2.36 |
| FW vs LCDM joint | 4.05-sig (S69 forecast) | -- | -- |
| FW vs Quintessence joint | 1.72-sig | -- | -- |

The ISW tracking test is the framework's unique observable: c_s^2 = 0 (DE clusters with matter) vs c_s^2 = 1 (quintessence, smooth DE). No other model predicts c_s^2 = 0 with w_0 = -0.918.

### 2032: DUNE (Mass Ordering, 5-sigma)

Definitive NO/IO measurement. Same gate as JUNO but at 5-sigma. Framework prediction: Normal.

### 2034: LiteBIRD + CMB-S4

| Observable | FW Prediction | Precision | Detection Significance |
|:-----------|:-------------|:----------|:----------------------|
| r | 0.024 | sigma=0.001 (LiteBIRD), 0.003 (CMB-S4) | **24-sig (LiteBIRD), 8.1-sig (CMB-S4)** |
| n_s | 0.9567-0.9649 (scheme dep.) | sigma=0.002 (CMB-S4) | 2.94-sig discrimination (S69 pre-reg) |
| alpha_s | 0 (exact, tree) | sigma=0.003 (CMB-S4) | n_s window [0.955, 0.963] contains both bare and f*-fitted |
| f_NL (equil.) | -0.313 to 0.853 | sigma=5.0 (CMB-S4) | Undetectable (0.17-sig) |
| f_NL (folded) | 0.129 | sigma=6.9 (CMB-S4) | Undetectable (0.02-sig) |

LiteBIRD detection of r = 0.024 at 24-sigma is NECESSARY but NOT SUFFICIENT. The framework gives r + 8*n_T = 0 exactly at CMB scales, indistinguishable from slow-roll inflation with the same r.

CMB-S4 n_s tightening is the metric-layer kill test. If n_s tightens to exclude [0.955, 0.963], the fold curvature is wrong.

### 2035+: LISA

Domain wall GW background at Omega_GW ~ 10^{-10}. Independent of all CMB predictions. Non-detection at Omega_GW < 10^{-11} constrains domain wall dynamics on the CG(24) Cayley graph.

### 2040s: 21cm Intensity Mapping (PURPOSE-BUILT)

| Observable | FW Prediction | SNR |
|:-----------|:-------------|:----|
| f_NL (folded) | 0.129 | 3.6-sig (l_max = 10^5) |
| f_NL (equil.) | 0.853 | 32.8-sig (l_max = 10^5) |
| ISW tracking (c_s^2=0) | +7.6% vs quintessence | 7.9-sig |

The folded bispectrum from Bogoliubov pair creation is the framework's UNIQUE DISCRIMINANT. No single-field inflation model produces the folded shape. This is the only observable that can CONFIRM (not merely not-exclude) the substrate mechanism.

---

## IV. Discriminant Predictions (Framework vs LCDM)

### Strong Discriminants (FW makes qualitatively different prediction)

| # | Observable | FW Prediction | LCDM Prediction | Discrimination | Experiment | Timeline |
|:--|:-----------|:-------------|:----------------|:---------------|:-----------|:---------|
| 1 | c_s^2_DE | 0 (DE clusters) | N/A (Lambda fixed) | Qualitative | 21cm ISW | 2040s |
| 2 | f_NL (folded) | 0.129 (from pair creation) | 0 (single-field) | Shape-specific | 21cm | 2040s |
| 3 | w_0 | -0.918 (Volovik) | -1.000 (Lambda) | 2.0 DESI-sigma | DESI DR3 | 2026 |
| 4 | w_a | 0 (four-fold locked) | 0 (Lambda, but DESI hints non-zero) | 2.92-sig from DESI | DESI DR3 | 2026 |
| 5 | ISW amplitude | +12.3% vs LCDM | 1.000 (by definition) | 0.49-sig (Planck) | Euclid, 21cm | 2030-2040 |
| 6 | f*sigma_8 suppression | -4% vs LCDM (tracking) | Standard | S8 direction correct | Euclid | 2029 |

### Weak Discriminants (FW differs quantitatively but marginally)

| # | Observable | FW | LCDM | Difference | Experiment |
|:--|:-----------|:---|:-----|:-----------|:-----------|
| 7 | r | 0.024 | 0 (or model-dependent) | Detectable by LiteBIRD (24-sig) but degenerate with slow-roll | LiteBIRD 2034 |
| 8 | n_s | 0.957-0.965 | Model-dependent (~0.965 from Starobinsky) | Marginal | CMB-S4 2034 |
| 9 | Lensing C_l^{kk} | -1.29% from tracking | Standard | SNR=2.36 (CMB-S4) | Euclid+CMB-S4 |
| 10 | Galaxy C_l^{gg} | 0.76-sig combined | Standard | Indistinguishable | Euclid |
| 11 | Omega_GW | ~10^{-10} (domain walls) | 0 (no 1st order transition) | Unique if detected | LISA 2035 |

### Non-Discriminants (FW indistinguishable from LCDM with current/near-future data)

BAO D_V(z)/r_d per tracer (dV_FW/dV_LCDM = 0.950-0.967, S69 PVD-NZ-69). Galaxy number counts. CMB-S4 f_NL (both undetectable). Granett anomaly (NOT explained, S69 PVD-ISW-69).

---

## V. Dark Matter Observational Program

### Tested DM Properties

| Property | Prediction | Status | Source |
|:---------|:-----------|:-------|:-------|
| Relic abundance (Leggett-only) | Omega_DM h^2 = 0.120 | 0.70-sig from Planck (0.1186) | Z-EQ-CHECK-66 PASS |
| Self-interaction | sigma/m = 0 exactly (N_pair=1) | Consistent (sigma/m < 1.25 cm^2/g, Bullet Cluster) | S58 |
| Transfer function | T(k)=1.0000 at all observable k | 22 OOM margin from Lyman-alpha | WDM-FRACTION-63 PASS |
| Free-streaming | lambda_fs = 9.85e-23 Mpc | Invisible (1.15% warm fraction) | WDM-FRACTION-63 PASS |
| Gravitational stability | tau = 4.93e82 s (65 OOM > t_univ) | Consistent (no observed DM decay) | DM-PAIR-DECAY-70 PASS |
| Leggett spectral quality | Q=18.6, Z=0.972 | No direct test | LEGGETT-SPECTRAL-66 PASS |
| z_eq (Leggett-only) | 3425 | 0.88-sig from Planck (3402) | Z-EQ-CHECK-66 PASS |

### Untested DM Properties (Critical)

| Property | Prediction | Why Untested | Required Computation |
|:---------|:-----------|:-------------|:--------------------|
| **Leggett gravitational decay rate** | Gamma_grav < H_0 (required) | Not computed from first principles | **LEGGETT-GRAV-DECAY-67** (P2, EVOI=17.4%) |
| BA phonon thermalization | Gamma_BA/H(z_eq) > 10 | BA decay channel uncomputed | BA-LIFETIME-FABRIC-67 (P5, EVOI=6.5%) |
| Direct detection cross-section | ~0 (CPT-neutral, non-annihilating) | Structural prediction, no dedicated computation | -- |
| Indirect detection (annihilation) | 0 exactly (non-annihilating) | Structural: Leggett mode is inter-band coherence, not particle-antiparticle | -- |

### DM-Specific Observational Implications

The Leggett-channel DM prediction is structurally clean: the DM candidate is a GGE quasiparticle (inter-band coherence mode between B2 bands), CPT-neutral, non-annihilating, with mass at the KK scale (~10^17 GeV). This immediately implies:

1. **No direct detection signal** in any foreseeable detector. The DM mass exceeds the energy threshold of all planned direct detection experiments by 10+ OOM.
2. **No indirect detection signal** from annihilation. The Leggett mode is a collective excitation, not a particle-antiparticle pair. No annihilation channel exists.
3. **No self-interaction** beyond gravitational. sigma/m = 0 at tree level.
4. **Effectively CDM** for all structure formation purposes. Free-streaming scale 22 OOM below observable.

The CRITICAL untested item is Leggett gravitational decay (LEGGETT-GRAV-DECAY-67). If Gamma_grav > H_0, the DM candidate is unstable and the entire Omega_DM h^2 = 0.120 match is vacuous. S70 DM-PAIR-DECAY-70 established Z_2 structural protection against pair decay (tau = 4.93e82 s, 65 OOM > t_univ), but the gravitational decay channel (Leggett mode radiating gravitationally through the a_2 channel) is computed differently and remains unresolved.

---

## VI. Missing Error Budgets

### Predictions Without Uncertainty Estimates

| Prediction | Current Value | Missing Error Source | Priority |
|:-----------|:-------------|:---------------------|:---------|
| f_NL (equilateral) | 0.853 (S67) / -0.313 (S72) | Sign discrepancy between GGE and Bogoliubov methods; no combined uncertainty | MEDIUM |
| Omega_GW (domain walls) | ~10^{-10} | Order-of-magnitude estimate only; no spectral shape, no bandwidth | HIGH (LISA needs sigma) |
| ISW tracking amplitude | +12.3% vs LCDM | No error from Gamma sensitivity (S68 workshop identified w_0 Gamma sensitivity as bottleneck) | HIGH (Euclid needs sigma) |
| r (CMB) | 0.024 | S71 bounds r_spatial in [0.30, 0.40]; translates to r(CMB) in [0.018, 0.031]. Error bar not propagated. | MEDIUM |
| Lensing suppression | -1.29% | No error from sigma_8 or tracking model uncertainty | MEDIUM |
| n_T (CMB) | -3.02e-3 | Error from n_T = -r/8 propagates from r uncertainty but not explicitly stated | LOW |
| m_H | 127.5-131.8 GeV (Aitken) | Aitken extrapolation from L_max = 3,4,5. Convergence not guaranteed. | MEDIUM |

### Predictions With Adequate Error Budgets

| Prediction | Value | Error | Source |
|:-----------|:------|:------|:-------|
| w_0 | -0.918 | +0.01/-0.04 (S71 band), +/-0.06 (sector scheme dep., S72 A-Q2) | S58, S72 workshop |
| n_s | 0.9567 (bare) | +/-0.0042 (Planck), scheme range [0.957, 0.965] via f* | S62-S72 |
| Omega_DM h^2 | 0.120 | Leggett-only bracket [0.013, 0.143] | S66 |
| alpha_s | 0 to -0.038 | Range from tree (trivial bundle) to smooth cutoff. ATDHFB bounds [-0.019, -0.008] | S63/S66 |
| tau_fold | 0.190 | sigma_tau = 0.011 (n_s binding constraint), S72 W1-E | S72 |
| A_s gap | 0.267 OOM | S70 baseline. With kappa free: 0 by construction. | S70/S72 |

---

## VII. Scheme-Dependent vs Scheme-Independent Classification

The S72 Mack-VdD workshop established a four-layer hierarchy superseding the S71 three-layer version: Topology > Representation > Metric > Functional. Each layer has distinct vulnerability and experimental strategy.

### Topology Layer (SCHEME-INDEPENDENT -- K-homology invariant)

Predictions determined by the K-homology class [D_K]. Invariant under tau shifts, spectral functional choice, and metric deformations. A failure here kills the framework.

| Prediction | Value | Test | Status |
|:-----------|:------|:-----|:-------|
| w_0 | -0.918 +/- 0.06 | DESI DR3 (2026) | 2.91-sig TENSION |
| w_a | 0 (exactly) | DESI DR3 (2026) | 2.92-sig TENSION |
| c_s^2_DE | 0 (tracking vacuum) | Euclid/21cm (2030-2040) | UNTESTED |
| Mass ordering | Normal | JUNO/DUNE (2028-2032) | Consistent (2.5-sig NO) |
| Omega_DM h^2 | 0.120 (Leggett-only) | Planck/CMB-S4 | 0.70-sig PASS |
| CC mechanism | Volovik rho~H^2 | Indirect (w_0 is the test) | 0.01 OOM PASS |
| f_NL suppression | Gaussian (|f_NL| << 1) | CMB-S4/21cm | PASS (Kasparov product) |
| DM self-interaction | sigma/m = 0 | Cluster lensing | Consistent |
| DM stability | tau >> t_univ (Z_2) | CMB spectral distortions | Consistent |

### Representation Layer (SCHEME-INDEPENDENT -- fiber branching invariant)

Predictions from the SU(3) representation theory. Invariant under tau shifts and spectral functional choice. Permanent.

| Prediction | Value | Status |
|:-----------|:------|:-------|
| SM gauge group recovery | SU(3)xSU(2)xU(1) from extended gauge module | PERMANENT (S61) |
| 3 generations | From CG(24) tessellation | PERMANENT |
| G_2 fiber eliminated | a_2/a_4 = 0.049 (gravity too weak) | S72 W4-F |
| KO-dim = 6 | PERMANENT | S7-S8 |
| BDI symmetry class | T^2 = +1 | PERMANENT (S17c) |

### Metric Layer (SCHEME-INDEPENDENT of f(x), DEPENDENT on tau_fold)

Predictions from the fiber Riemannian metric at tau_fold = 0.19. Shift if tau_fold shifts.

| Prediction | Value | tau_dependence | Test |
|:-----------|:------|:---------------|:-----|
| sin^2(theta_W) at M_KK | 0.5839 | exp(-4*tau) | Indirect via RG running |
| g'/g coupling ratio | 0.683 | exp(-2*tau) | Threshold corrections |
| BCS gap Delta | 0.464 M_KK | Via gap equation at fold | Indirect |
| phi_paasch | 1.532 | Eigenvalue ratio | PERMANENT at tau~0.15-0.20 |
| tau_fold consistency | [0.189, 0.191] (3-way overlap) | By definition | S72 W1-E PASS |

### Functional Layer (SCHEME-DEPENDENT -- requires f(x))

Predictions that depend on the spectral functional f(x). A failure here kills f*(x), not the framework.

| Prediction | Value | f*-dependence | Test |
|:-----------|:------|:-------------|:-----|
| n_s | 0.9567 (bare) to 0.9649 (f*-fitted) | delta_t*/delta_n_s ~ 10.7 | CMB-S4 (2034) |
| A_s normalization | kappa = 2.37e-8 (from f*) | Amplitude-only | Decoherence computation |
| alpha_s | 0 (tree) to -0.038 (smooth cutoff) | Sign flip between sqrt and zeta | CMB-S4 (2034) |
| sin^2(theta_W) at M_Z | 0.229 (Model A) to 0.378 (Model D) | Via KK thresholds | PW-SECTOR-THRESHOLD-73 |
| m_H (from spectral action) | 127.5-131.8 GeV | Via RG running from f_4 | LHC precision |

---

## VIII. S72 New Observational Implications

### From 20 Gate Computations

| S72 Gate | Observational Implication | Layer |
|:---------|:------------------------|:------|
| **KAPPA-DELTA-72** (W1-A, INFO) | Gap curvature channel for A_s DEAD. t_dec/t_transit = 5.5e9, far too slow. Gap varies only 0.5% through transit. Phase dynamics, not amplitude dynamics, must close A_s. | Functional |
| **GILKEY-REEVAL-72** (W1-B, INFO) | a_6 correction to lambda_CCM reduced from 26.9% to 13.3%. Original S71 PASS downgraded to INFO. MAXIMALLY scheme-dependent (0% zeta, 13% cutoff/Gilkey, 27% cutoff/spectral-zeta). | Functional |
| **ZETA-RATIO-CONVERGENCE-72** (W1-C, PASS) | Spectral zeta ratio converges monotonically (0.567 at L=3 to 0.223 at L=7). Finite-spectrum contamination confirmed and quantified. S71 value was truncation artifact. | Metric |
| **CAUCHY-SCHWARZ-W0-72** (W1-D, FAIL) | CS formula gives w_0 = -0.687, NOT -0.918. Category error (S72 workshop C1). Constructive: one-sided asymmetry constrains scheme variation. Easier to push w_0 toward LCDM than toward DESI. | Topology |
| **TAU-FOLD-CONSISTENCY-72** (W1-E, PASS) | Three-way overlap at [0.189, 0.191]. n_s is binding constraint (sigma_tau = 0.011). tau_fold = 0.19 at 1.8-sigma edge of Planck n_s band. | Metric |
| **DUAL-DECOHERENCE-72** (W2-A, INFO) | A_s gap = BCS decoherence budget. Cell-crossing gives delta_OOM = 1.69 (9.4x too slow). Target requires t_dec/t_transit = 0.716 (sub-transit). BCS channel 99.8%. | Functional |
| **WEINBERG-72** (W2-B, FAIL) | Pure SM running: 54.5% off. Model A (universal thresh.): 1.2% match. 34.6% gap between RG and Baptista boundary quantifies unknown KK threshold correction. | Metric+Functional |
| **SPECTRAL-FUNCTIONAL-FIT-72** (W2-C, PASS) | f*(x) = 0.912*sqrt + 0.088*exp exists, matches (n_s, A_s) jointly. w_0 is FUNCTIONAL-INDEPENDENT (Volovik partition). f* is non-perturbative (divergent SDW moments). SDW expansion unavailable for physical functional. | Functional |
| **INSTANTON-KAPPA-72** (W2-D, INFO) | Three-regime landscape: obstructed (rho<1.06/M_KK), marginal (1.06-1.80), compatible (rho>1.80). Dominant instanton at Kato-Rellich boundary. Non-trivial bundle exists but dynamically suppressed at fold. | Metric |
| **BCS-DRESSED-SA-72** (W3-A v2, INFO) | BCS dressing of n_s is PERMANENTLY NEGLIGIBLE (delta = 3.8e-6). Only 16/155,984 weighted modes participate. Kasparov-validated: (0,0) sector suppression factor 1/N_weighted. | Topology (structural bound) |
| **BLUESHIFT-TILT-72** (W3-C, PASS) | Entry horizon contributes O(1) tilt correction (delta_n_s = +1.001). Direction: redder (AWAY from Planck). Additive approximation suspect for r~3 (S72 workshop D2). | Functional |
| **TAU-EQUILIBRIUM-72** (W3-D, INFO) | Post-transit equilibrium = spectral moduli stabilization. BCS is 10^{-5} perturbation. Equilibrium controlled by S(tau) shape. Quartic models generically produce stable minima. | Metric |
| **DECOHERENCE-BISPECTRUM-72** (W4-A, PASS) | f_NL = -0.313 (phys.), flat across all decoherence timescales. Spectrum intrinsically Gaussian. GGE + Kasparov product suppress connected 3-point by 1/sqrt(N). | Topology |
| **G2-CONSTANCY-72** (W4-F, FAIL) | G_2 is 34% MORE constant than SU(3). a_2/a_4 constancy is universal for rank-2 groups. Fiber selection requires coupling ratio MAGNITUDE, not stability. | Representation |

### From S72 Workshops (3 workshops, 10+ emergences)

| Emergence | Observational Consequence |
|:----------|:------------------------|
| **E1: Dual vulnerability** (Mack-VdD) | Framework has exactly two independent failure modes: Mode A (w_a from DESI, topology layer) and Mode B (n_s from CMB-S4, functional layer). Independent experimental strategies. |
| **E2: A_s = decoherence** (Mack-VdD) | A_s gap reduced to single unknown: t_dec/t_transit. With kappa as normalization, framework functions. Shape predictions (n_s, r, f_NL) carry predictive content. |
| **E3: Temporal instanton landscape** (Mack-VdD) | Instanton density and Kasparov reliability move OPPOSITE with tau. Potential topological transition at post-transit tau values. |
| **E4: Moduli stabilization = three-in-one** (Mack-VdD) | S(tau) simultaneously determines equilibrium, CC, and w(z). SPECTRAL-ACTION-PROFILE-73 needed. |
| **Four-layer hierarchy** (Mack-VdD) | Topology > Representation > Metric > Functional. Four independent scorecards. Supersedes S71 three-layer. |
| **f_NL sign discrepancy** (S67 vs S72) | S67: +0.853 (equil., GGE). S72: -0.313 (equil., Bogoliubov w/decoherence). Convention/methodology difference. Both O(1), both 80x below Planck. Resolution: compound computation needed. |

---

## IX. Priority-Ordered Observational Agenda

### Level 1: CRITICAL (gates framework survival)

| # | Computation | What It Tests | EVOI | Experiment | Timeline |
|:--|:-----------|:-------------|:-----|:-----------|:---------|
| 1 | **DESI DR3 response** | w_0=-0.918, w_a=0 against DR3 data | -- (data-driven) | DESI DR3 | **2026** |
| 2 | **LEGGETT-GRAV-DECAY** (P2) | DM stability: Gamma_grav < H_0 | 17.4% | If FAIL: Omega_DM = 0 | Now |
| 3 | **TRANSIT-PS** (P1) | alpha_s(k_CMB), A_s, n_s(k) simultaneously | 22.5% | CMB-S4 alpha_s (2034) | Now |
| 4 | **BBN-VOLOVIK** (P4) | Volovik tracking EOS at T_BBN | 14.0% | BBN constraints | Now |

### Level 2: HIGH (sharpens predictions for upcoming data)

| # | Computation | What It Tests | Experiment | Timeline |
|:--|:-----------|:-------------|:-----------|:---------|
| 5 | PW-SECTOR-THRESHOLD-73 | sin^2(theta_W) at M_Z: Model A or not? | LHC precision | Now |
| 6 | SPECTRAL-ACTION-PROFILE-73 | S(tau) for tau in [0,2]: equilibrium, CC, w(z) | DESI w(z) shape | Now |
| 7 | RE-COMPOUND-TILT-73 | Compound Bogoliubov n_s through full transit | CMB-S4 n_s (2034) | Now |
| 8 | RE-DECOHERENCE-73 | Physical justification for kappa = 2.37e-8 | Planck A_s | Now |
| 9 | FUNCTIONAL-SELECT (P3) | Unique f(x) with n_s AND m_H in range | CMB-S4 + LHC | Now |
| 10 | Omega_GW error budget | Spectral shape and bandwidth for LISA | LISA (2035) | Before 2033 |
| 11 | ISW tracking error budget | Gamma sensitivity, w_0 systematic | Euclid (2029) | Before 2028 |

### Level 3: MEDIUM (pre-registration for future data)

| # | Computation | Experiment | Timeline |
|:--|:-----------|:-----------|:---------|
| 12 | 21cm ISW cross-power pre-registration | 21cm intensity mapping | Before 2035 |
| 13 | f_NL sign resolution (GGE vs Bogoliubov) | CMB-S4 (undetectable) / 21cm | Before 2035 |
| 14 | INSTANTON-LANDSCAPE-73 | alpha_s at late times | LHC QCD | Now |
| 15 | Cluster hydrostatic mass bias with FW | Euclid/eROSITA | Before 2030 |
| 16 | ZETA-FSTAR-RATIO-73 | Scheme convergence test | Internal | Now |

### Level 4: LONG-TERM (purpose-built experiments)

| # | Observable | Instrument | Timeline |
|:--|:-----------|:-----------|:---------|
| 17 | f_NL (folded) = 0.129 | Purpose-built 21cm (l_max ~ 10^5) | 2040s |
| 18 | ISW tracking (c_s^2 = 0) | 21cm intensity mapping | 2040s |
| 19 | Domain wall GW spectrum | LISA / successor | 2035-2050 |

---

## Summary Statistics

| Category | Count |
|:---------|:------|
| Pre-registered predictions tracked | 25 |
| Tested | 12 |
| Partially tested | 5 |
| Untested | 8 |
| Active tensions (> 2-sigma) | 3 (w_0, w_a, n_s) |
| Scheme-independent tensions | 2 (w_0, w_a -- both topology layer) |
| Scheme-dependent tensions | 1 (n_s -- functional layer, resolvable via f*) |
| PASS results (framework matches data) | 10+ (Omega_DM, CC, r, mass ordering, sigma_8 direction, T(k), f_NL, DM stability, z_eq, sin^2 at M_KK) |
| FW beats LCDM (Delta chi^2 < 0) | 2 (f*sigma_8: -1.19; Pantheon+ SNe: -7.82 full cov) |
| Unique discriminant predictions | 2 (folded f_NL, ISW c_s^2 = 0) -- both require 21cm (2040s) |
| First decisive experiment | DESI DR3 (2026) |
| Framework survival condition | w_a > -0.35 |

**The observational program is front-loaded to DESI DR3. The framework's fate on the topology layer is decided within 1 year. Everything after that either sharpens the picture (Euclid, CMB-S4) or waits for purpose-built 21cm tomography for the unique confirmation signal.**

---

*This audit is the canonical reference for the project's observational status as of S72. Gate verdicts are permanent. Layer classifications follow the four-layer hierarchy (Mack-VdD S72 workshop). All numbers from source computations.*
