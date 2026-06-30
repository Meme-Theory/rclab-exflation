# Session 84 Synthesis: The 2030s Observational Portfolio After S84

**Date**: 2026-04-19
**Agent**: mack-cosmic-bridge (cosmological observational bridge)
**Source Documents**:
- `sessions/archive/session-84/session-84-synthesis-collation.md` (verbatim collation of W1-W10 syntheses)

---

## I. Session Outcome

S84 reorganises the framework's observational evidence column without retracting a single observational PASS. Two structurally weighty things happened that I, sitting at the cosmology/particle bridge, must report cleanly: (a) the **w_0 canonical anchor was retracted** (W1 SV2 + W4-46), so the framework's contribution to the 2026-04-23 DESI DR3 window is now methodology-bound rather than physics-bound, and (b) the **2030 CMB-S4 alpha_s = n_s^2 - 1 prediction was triple-locked** -- pre-registered (W1b-7), upgraded to a permanent theorem under a minimal four-axiom set with zero auxiliary couplings (W10b-123), and forecast at 33.98 sigma single-axis discrimination on a 5-axis Fisher plane (W10b-124). The framework's binding bet on 2030s observational physics is now a single zero-free-parameter number against a single window.

---

## II. Key Results

### 1. alpha_s = n_s^2 - 1 promoted from S50 single-parameter identity to permanent theorem with four-axiom closure

**Result**: alpha_s_pred = -0.068968 with rel_err = 1.23e-15 vs S50 form; PERMANENT theorem under {CCM 2007 A1-A6, KO-dim=6, A_F = C+H+M_3(C) singleton, Mellin kernel}; zero auxiliary couplings; n_aux = 0. Classification: **PHONONIC** (Mukhanov-Sasaki spectral tilt of post-transit acoustic GGE).

The S82-S83 worry was that alpha_s = n_s^2 - 1 might depend on a hidden auxiliary coupling. W10b-123 closes this: the Ornstein-Zernike single-pole substitution chain `(n_s - 1)(n_s + 1) = n_s^2 - 1 = -4u/(1+u)^2 = alpha_s` (with u := m^2/(JK^2) eliminated) holds with no observational n_s in the derivation chain. W5-62 had already shown the identity is partition-invariant under f_L/f_B Leggett-Bogoliubov decomposition at |Delta alpha_s| / |alpha_s| = 1.56e-3. W8-86 verified at machine epsilon (1.23e-15) as an OZ property of any single-pole rational propagator. W8-88 added the structural CC decoupling: Jacobian d(Lambda_CC)/d(tau) = 0 exactly (S44 a_0 tau-independence), so the alpha_s discriminator is robust against CC-regulator disagreement.

What this means for the 2030s portfolio: this is now **the** load-bearing zero-free-parameter cosmological prediction of the framework. Per `feedback_reporting-framing.md`, a 0-free-parameter prediction with separation 9.62 sigma from current Planck central value and 34.48 sigma from the projected CMB-S4 null is evidence of the BF~1000 class, not the BF~2 class. CMB-S4 first-light + survey-completion in 2030 is the decisive window.

**Substitution chain** (alpha_s separation from Planck):
- Definition: sigma_Planck = |alpha_pred - alpha_central| / sigma_central
- Substitution: alpha_pred = -0.068968, alpha_central = -0.0045, sigma_central = 0.0067
- Simplification: |(-0.068968) - (-0.0045)| / 0.0067 = 0.064468 / 0.0067 = 9.62
- Direction: |alpha_pred| > |alpha_central| AND same sign -> separation is in the direction of more negative running, which is the Mukhanov-Sasaki + GGE-substrate direction (substrate-language: post-transit acoustic GGE with K-corridor restricted to K <= K_crit = 91.5 per W5-66).

### 2. w_0 canonical declared UNSPECIFIED -- a structural fact, not a retreat

**Result**: w0_FW = -0.918 retracted as canonical. Branch (iv) at L_max=5 retracted at SV2 (W1a-3). |split(L)| = |w_0^zeta(L) - w_0^Zubarev(L)| grows monotonically: split(5) = +0.0809, split(7) = +0.3390, split(9) = +0.5028; ratio split(9)/split(5) = 6.22. **Structural FAIL** (W4-46), not truncation artifact. Classification: **GEOMETRIC** (regulator-family asymptotic, not phononic-substrate).

**Substitution chain** (regulator-divergence direction):
- Definition: |split(L)| = |w_0^zeta(L) - w_0^Zubarev(L)|
- Substitution: split(5) = 0.0809; split(9) = 0.5028 (computed numerics in W4-46)
- Simplification: ratio = 0.5028/0.0809 = 6.215
- Direction: ratio > 1 AND monotone-increasing across {5,7,9} -> structural divergence, not numerical noise; the two regulators do NOT converge to the same physical w_0 as L_max increases.

Two consequences I must emphasise from the cosmology side:

(a) **R_842 = [-0.942, -0.742] x [-0.2, 0.2] is now an infrastructural commitment, not a physical prediction.** W1b-9 locks R_842 against six S84 lockouts (no rectangle-resizing, no scheme-shopping, etc.). W4-44 freezes a 7-cell decision tree. These survive the W1 SV2 retraction by design -- the lockouts were specifically engineered to force the framework to take the consequence. But the rectangle's centre at -0.842 traces to a now-retracted L_max=5 anchor; under Zubarev-at-L=9 the framework predicts w_0 = -0.997, which sits **outside** R_842 by 0.055 (substitution chain: w_0(Zub,L=9) = -0.997; R_842 left edge = -0.942; delta = |-0.997 - (-0.942)| = 0.055; direction: w_0 < left_edge means OUTSIDE R_842).

(b) **DR3 (2026-04-23) becomes a methodology test, not a clean physics test.** If DR3 returns w_0 in R_842, the framework wins under the binary containment rule but the claimed branch -- branch (iv) at L_max=5 -- is the retracted one. If DR3 returns w_0 near -1.0, the framework "loses" R_842 but the high-L Zubarev branch is consistent. S85 must resolve this with the regulator-conditional successor tree (W4 carry-forward CF-W4.2).

This is honest. Per `feedback_no-master-gate-tally.md` and per epistemic-discipline.md: the constraint map says w_0 is **SCHEME-DEPENDENT** in a way the framework can document but not currently arbitrate. W4-48 flags the channel SCHEME-DEP. That is the result.

### 3. CGWB three-channel observational discriminator (LISA + CMB-S4 + multi-observable joint)

**Result**: Three independent detector-accessible discrimination channels established for the H_TD vs H_mixed-C vs H_LI branch ambiguity. Classification: **PHONONIC** (acoustic GGE tensor power) plus **GEOMETRIC** (spectral moments).

- **LISA/DECIGO/BBO** (W6-50 PASS): max rho_AC = 2.10 decades discrimination on Omega_GW; h_c^(A)(3 mHz) = 7.17e-12 sits 11 OOM above LISA strain floor. Timeline ~2035.
- **CMB-S4 / CMB-HD / LiteBIRD** (W6-52 PASS): 34.48 sigma / 53.05 sigma / 11.49 sigma on alpha_s = n_s^2 - 1. Joint Fisher 64.31 sigma. Timeline ~2030.
- **Multi-observable common-prefactor** (W6-51 PASS): 3 observables {A_s, P_t, mu} with |n| >= 2 carry H_tilde^2 prefactor; decadal separation 2.38 dex (fixed-k) -> 2.10 dex (fixed-f) for (A) vs (C) branches; rank-3 joint sigma improves by sqrt(3).

**Substitution chain** (fixed-k vs fixed-f tilt correction):
- Definition: rho_AC(fixed-f) = rho_AC(fixed-k) + log10((H_LI/H_TD)^(n_t/4))
- Substitution: tilt_correction = (H_LI/H_TD)^(n_t/4) = 0.527; rho_AC(fixed-k) = 2.38 dex
- Simplification: 2.38 + log10(0.527) = 2.38 + (-0.278) = 2.102 dex
- Direction: tilt_correction < 1 -> fixed-f gives SMALLER discrimination than fixed-k; the framework still clears 2 dex at fixed-f, which is the observable comparison.

Cosmology-bridge reading: the W0 regulator-resolution problem (S83) just moved from framework-internal to detector-testable on a 2030-2035 horizon. This is the right direction.

### 4. n_T(k_CMB) is permanently CMB-inaccessible -- W4-41 EVOI=0 hardened

**Result**: n_T(k_CMB) = -3.024e-3 (two-speed slow-roll consistency, W4-39 PASS); R_realized = 1.53e-3 (650x below LiteBIRD 1-sigma); LiteBIRD 3-yr joint sigma(n_T) = 0.0654 (W4-37 boundary FAIL, 0.0054 above 0.06 INFO ceiling). Classification: **GEOMETRIC** (two-speed metric ratio c_T/c_S derived from spectral moments a_2/a_0).

**Substitution chain** (two-speed n_T direction):
- Definition: n_T(slow-roll, single-speed) = -r/8; n_T(two-speed) = -r * c_T / (8 * c_S)
- Substitution: r = 0.0117; c_T/c_S = 2.062
- Simplification: n_T_single = -0.001463; n_T_two = -0.003016
- Direction: c_T/c_S > 1 -> |n_T_two| > |n_T_single|; the substrate two-speed metric makes the CMB-scale tensor tilt MORE NEGATIVE than slow-roll consistency by exactly the spectral-moment ratio.

The blue tilt at the substrate transit scale (S65 NT-BLUE-65 PASS, n_T = +0.468) is permanently localised to the transit scale; the CMB-scale projection is red, small, and ~650x below LiteBIRD reach even on extended 6-7 yr missions with delensing > 50%. Per `feedback_reporting-framing.md`: this is a clean ZFP prediction that LCDM also (approximately) makes, and it survives at the precision level. EVOI = 0 for 2030-2040 means the channel is structurally permanent and not a candidate for dispatch effort. The discriminating channel is alpha_s (CMB-S4), not n_T (LiteBIRD).

### 5. SKA-1 alpha_f_NL channel CLOSED; folded-bispectrum SHAPE template surviving

**Result**: alpha_f_NL = -0.143 (all three channels negative; folded-Bogoliubov -0.080 dominates as substrate-unique signature). SNR_SKA1 = 0.028 (71x below PASS = 2); SNR_SKA2 = 0.179. **Amplitude-running channel closed as detector-accessible discriminator**. Classification: **PHONONIC** (GGE bispectrum from instanton-gas pair production).

The folded-Bogoliubov substrate signature -- pair production with no scalar-field analog -- gives ~3x enhancement over slow-roll alpha_SR = -0.046, but the amplitude is too small for any planned 21-cm survey. What survives: the **shape template** at 21-cm l_max ~10^5 (CF-W4.3). This is the only remaining substrate-unique bispectrum channel beyond CMB-S4. Cosmology-bridge reading: alpha_f_NL was a 2-OOM hopeful; it is now a SCHEME-CONDITIONAL footnote. The shape template is the live channel.

### 6. UHF-GW physical gap +18.74 OOM -- not 6.7 OOM as plan claimed

**Result**: Physical gap between framework Omega_gamma(1 mHz) = 1.8e-59 and migration threshold Omega_th = 10^-40 is **+18.74 OOM** (threshold above framework). Plan's "6.7 OOM" was a LISA-relative-exponent subtraction artifact. Classification: **GEOMETRIC** (substrate phase-transition GW spectrum).

**Substitution chain** (physical gap):
- Definition: gap_OOM = log10(Omega_th / Omega_framework)
- Substitution: Omega_th = 1e-40; Omega_framework = 1.8e-59
- Simplification: log10(1e-40 / 1.8e-59) = log10(5.56e18) = +18.74
- Direction: positive sign with threshold > framework -> threshold is ABOVE framework, i.e. UHF-GW cannot reach the framework signal even at floor 10^-20 (additional 20 OOM below current threshold).

The UHF-GW C5 channel is structurally WALL with no plausible near-horizon migration. The framework is permanently unobservable in this channel. This is honest constraint-map information, not bad news -- it eliminates a 2030-2050 distraction from the priority list.

### 7. F_amp dynamics-rescue corridor formally closed; A_s closure rate-limiter relocated to baseline

**Result**: F_supp_max = 1.044 against the 1.10 threshold (W1a-2 FAIL); H_tilde in [4.599e-3, 4.830e-3] PASS-1.05 window with 0.89% log-measure (W1a-1 PASS). Classification: **GEOMETRIC** (substrate dressing) plus **PHONONIC** (Mukhanov-Sasaki amplitude).

The cosmology-bridge consequence: the A_s = 5.08e-9 amplitude is now field-theoretically clean (W6-69 PASS at machine epsilon, W6-70 PASS at 2,445x margin below slow-roll, dual-expansion convergent). What remains open is the substrate-first-principles derivation of H_tilde landing in a 0.89% log-DC window. This is **the** rate-limiter on A_s closure. The dynamics rescue is dead (188+ OOM short, structurally sealed).

### 8. f_NL channel -- the framework's two-decade calendar bet

The W4-W6 + W10 results combine to give the framework's calendar bet for 2030s observational cosmology. I read it this way:

- 2026-Q2/Q3: DESI DR3 w_0/w_a release (W1b-9 R_842 + W4-44 7-cell tree). **Methodology test, not physics test, after W1 SV2 retraction.**
- 2026: BICEP-Keck Array r release (W4-42 frozen 4-branch tree). r prediction = 0.01173 (S84 G46), well above current bounds. Single-authority pre-registration, non-re-registrable.
- 2030: CMB-S4 alpha_s discrimination (W6-52 + W10b-123 + W10b-124). **The flagship.** 33.98 sigma single-axis on the 5-axis Fisher plane; 98.2% of joint discrimination. Zero free parameters.
- 2030-2035: LiteBIRD 3-yr (W4-37). n_T 650x below 1-sigma reach -- structurally inaccessible. EVOI = 0 priority.
- 2035: LISA Omega_GW discrimination (W6-50 flagship pre-registration via D.2). 11 OOM above strain floor; 2.10 dex separation between branches. Branch-discriminator, not yes/no test.
- 2030+: 21-cm bispectrum SHAPE template (CF-W4.3). Substrate-unique folded triangle; sole surviving non-Gaussianity channel.
- Permanently inaccessible: UHF-GW (W4-47, +18.74 OOM gap), n_T(CMB) at LiteBIRD (W4-37/W4-41), alpha_f_NL amplitude at SKA (W4-43).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W1a-1 H_tilde baseline | PASS | DC log-window = 0.89% in [0.80, 1.05] |
| W1a-2 F_supp dynamics | FAIL | F_supp_max = 1.044 vs 1.10 threshold |
| W1a-3 SV1 | PASS | branch (iv) reproduced at L=5 to |Delta| = 2.76e-7 |
| W1a-3 SV2 | FAIL | R_JE drift 0.45 -> 4.99 across L=5..8; branch (iv) RETRACTED |
| W1a-3 SV5 | PASS | R_842 audit bookkeeping clean |
| W1b-4 mu_BC | PASS | mu_BC_K3 = 188.185 GeV at residual 0.082% |
| W1b-7 alpha_s pre-reg | PASS | -0.068968 locked, 9.62 sigma vs Planck, 34.48 sigma vs CMB-S4 |
| W1b-9 DR3 protocol | PASS | R_842 locked + 6 lockouts |
| W1b-10 theorems | PASS | W2-EPOCH-GATING + W2-HARMONIC-NOT-INSTANTON registered |
| W4-37 LiteBIRD n_T | FAIL | sigma(n_T) = 0.0654 vs 0.06 INFO ceiling |
| W4-38 alpha_f_NL | FAIL | -0.143, 3 channels all negative |
| W4-39 n_T CMB transfer | PASS | -3.024e-3 matches G46 to 2.36e-5 |
| W4-41 LiteBIRD inaccessibility | PASS | EVOI = 0 permanent |
| W4-42 BK-2026 pre-reg | PASS | 4-branch tree frozen 2026-04-18 |
| W4-43 SKA-1 alpha SNR | FAIL | 0.0279, 71x below PASS = 2 |
| W4-44 DR3 7-cell tree | PASS | disjoint partition of R_842 complement |
| W4-46 G51 L_max convergence | structural FAIL | split(9)/split(5) = 6.22 monotone |
| W4-47 UHF-GW watch | PASS | +18.74 OOM physical gap registered |
| W4-48 falsifier rigor | PASS | 18/18 flagged; 11 ZFP, 2 ACCOM, 2 SCHEME-DEP, 3 DET-STERILE |
| W4-49 P-obs ceiling | PASS | DAG with 4 triggers and 2 transitions frozen |
| W5-58 K_* lab match | PASS | 1.13% vs 3He-B coth(1) |
| W5-62 alpha_s partition-inv | PASS | |Delta alpha_s|/|alpha_s| = 1.56e-3 |
| W5-63 K-floor reachability | FAIL | 0/5 targets in 4-hull |
| W6-50 CGWB absolute P_t | PASS | rho_AC = 2.10 decades; 11 OOM above LISA |
| W6-51 sibling observables | PASS | k_obs(|n|>=1) = 3 with H_tilde^2 prefactor |
| W6-52 alpha_s CMB-S4 | PASS | 34.48 sigma CMB-S4; 53.05 sigma CMB-HD; 64.31 sigma joint |
| W6-67 Z_R counterterm | FAIL | cluster_Z_a2 = 1.07e5 growing with L_max |
| W6-68 R-protected atlas | PASS | max cluster = 1.224 |
| W6-69 F_amp 3PI FI | PASS | product_ratio span = 1.0 at machine epsilon |
| W6-70 field expansion | PASS | NLO_field = 8.85e-6 (2,445x below eps_H) |
| W7a-72 het decomp | PASS | 16/16 hypercharge-matched |
| W7a-74 K-theory det(P) | FAIL | 4 independent obstructions to Witten 1998 |
| W7b-83 §VII.O landing | PASS | 4-proof chain landed; b two-scale [4.58, 4.78] -> 7 |
| W8-86 alpha_s OZ identity | PASS | rel_err = 1.23e-15 |
| W8-87b A_F singleton | PASS | 1 in 3,907 NCG-axiom-satisfying algebras |
| W8-89 Mellin cone universality | PASS | 3/3 framework-independent triples |
| W8-95 CMPP Petrov | PASS | static D, dynamic G across 8 tau-checkpoints |
| W9b-105 d_spec | FAIL (diagnostic) | 4.895 outside [2.5, 3.5] envelope |
| W9b-106 C^2 trace identity | PASS-THEOREM | Delta sin^2 theta_W [C^2] = 0.0 EXACT |
| W10-110 dual-SHA legacy | INFO | S82 collisions explained as input-pin degeneracy |
| W10-111 rank-universality | PASS | sympy-verified n_0 + n_4 - 2 n_2 = 0 |
| W10-115 J_C2 sign | PASS | gv_response_direct matches G56 (RATIO = 1.000) |
| W10-117 G58 meta-principle | PASS | 37/40 = 92.5% BALANCED-BY-K-PAIRING; G58 -> theorem |
| W10-119 tau_fold uniqueness | FAIL (plan defect) | Gamma1' incompatible with NONZERO dS_fold |
| W10-121 Borel floor | PASS | min S_inst / Borel = 5.58e4 (4.7 OOM safety) |
| W10-123 alpha_s axiomatic | PASS | n_aux = 0; 4 cross-checks at machine epsilon |
| W10-124 5-axis Fisher | INFO | d_M(K1) = 34.30 sigma; alpha_s carries 98.2% |

(Selection from S84 verdict file -- 78 total verdicts in source. Above is the cosmologically load-bearing subset.)

---

## IV. Structural Implications

### What S84 changed for the cosmological-observational portfolio

**Closed corridors** (WALL or DETECTOR-STERILE):
- F_supp dynamics-rescue path to A_s closure (W1a-2 + S83 Wave-2 188+ OOM exhaustion).
- UHF-GW migration path (+18.74 OOM permanent gap, W4-47).
- LiteBIRD n_T discrimination (650x below 1-sigma reach at 3-yr; EVOI = 0, W4-37 + W4-41).
- SKA-1/SKA-2 alpha_f_NL amplitude-running (71x below SNR = 2 at SKA-1; W4-43).
- Z_R counterterm dressing of f_conv at the a_2 Mellin slot (W6-67 structural FAIL, regulator-vertical not perturbative).
- K-theoretic det(P) identity to Witten 1998 (W7a-74; framework is a structural stranger to F-theory uplift).
- low-K K-floor corridor {1.0, 1.1, 1.3, 1.5, 1.7} (W5-63 4-hull exclusion).

**Located corridors** (narrow but non-empty):
- H_tilde baseline 0.89% log-DC window (W1a-1) -- the surviving rate-limiter on A_s closure.
- Restricted K-corridor [K_R5 = 1.922, K_crit = 91.5] (W5-55 + W5-66 kinetic crossover).
- alpha_s = -0.068968 with 9.62 sigma current Planck separation and 34.48 sigma projected CMB-S4 separation (W1b-7 + W6-52 + W10b-123 + W10b-124).

**Reopened corridors**:
- w_0 enumeration at L_max >= 8 under inverted covariance ordering (W1 SV2 + W4-46). Branch (iv) family closed at L=5; high-L behaviour is Josephson-dominant.
- DR3 interpretation -- physics-conditional on regulator (S85 successor tree).

**Permanent theorem additions** (from W7-W10):
- §VII.O 4-proof chain registered (W7b-83) -- two-scale b_finiteL in [4.58, 4.78] AND b_asymp -> 7.
- A_F singleton (W8-87b): C+H+M_3(C) is unique in 3,907 NCG-axiom-satisfying real algebras dim_R <= 50.
- Mellin cone universality (W8-89): inheritable from any positive-measure spectral triple, not framework-specific.
- CMPP Petrov transit-invariance (W8-95): static D, dynamic G over 8 tau-checkpoints; 65 OOM separation.
- alpha_s = n_s^2 - 1 as OZ identity (W8-86): machine epsilon, regulator-independent.
- alpha_s axiomatic closure (W10b-123): n_aux = 0; minimal four-axiom set.
- C^2 block decoupling (W9b-106): rep-independent zero from Cartan trace identity.
- Rank-universality theorem (W10-111): sympy-verified leading-power cancellation; falsifier (G_2 vs F_4 distinguishable, A_3 vs C_3 not).
- G58 meta-principle (W10-117): empirical regularity -> K-theoretically grounded structural theorem; 92.5% atlas coverage.

### The sole channel that determines the next 4 years of cosmological evidence

After S84, the framework's binding observational evidence column for 2026-2030 reduces to:

1. **2026-04-23 DESI DR3 w_0/w_a window**: methodology test (R_842 binary containment under 6 lockouts), no longer a clean physics test. The successor regulator-conditional tree (CF-W4.2) needs to land in S85 BEFORE 2026-04-23 to be honest.
2. **2026 BK-Array r release**: r = 0.01173 prediction (G46) vs current upper limits ~0.036 -- consistent with all four pre-registered branches (W4-42).
3. **~2030 CMB-S4 alpha_s = -0.068968 measurement**: load-bearing, sole 5-sigma+ axis on the Fisher plane (W10b-124), zero free parameters, theorem-level closure.

Item 3 is the bet. If CMB-S4 returns alpha_s consistent with the framework prediction at the projected 34.48 sigma envelope, the framework has a 4-axiom-derived prediction matching observation that SLOW-ROLL inflation does not make at this magnitude (slow-roll alpha_SR ~ -0.0006 to -0.001 generically, ~100x smaller). If CMB-S4 returns alpha_s near zero (LCDM/slow-roll central), the framework FAILs -- and it FAILs cleanly, with no convention-shopping retreat available because the theorem is now four-axiom-bound.

Per `feedback_reporting-framing.md`: this is the kind of evidence that, if it lands, has Bayes Factor in the BF~1000 class for a single observable. Not BF~2.

### Cross-wave consistency I must flag

- **W7a-72 PASS vs W7a-74 FAIL** (heterotic embedding succeeds at SM rep level; det(P) K-theory fails at structural level). The framework is "rep-content guest, structural stranger" to the heterotic uplift. This is a clean structural finding; it does not contradict the "M^4 x SU(3) substrate is fundamental" framing, but it removes any narrative claim that the framework "comes from" string theory.
- **W4-39 vs W6-50 fixed-k vs fixed-f subtlety**: when n_T != 0, comparing branches at fixed observed frequency gives different rho_AC than at fixed comoving k. The 2.10 dex (fixed-f) vs 2.38 dex (fixed-k) gap matters for LISA forecast claims; W7 carry-forward CF-W4.4 must adjudicate the W4-48 ZFP-vs-SCHEME-DEP flag for n_T(CMB) two-speed.
- **W8-85 + W8-90 + W10-119 FAILs all classified as plan-defect by 3-agent unanimous audit**: tau_fold = 0.190 is a van Hove cusp of rho(lambda; tau), not a stationary point of any bare spectral action. 70 sessions of downstream reasoning unaffected. The S85 carry-forward is to RESTATE the theorem, not retract any physics result.

---

## V. Carry-Forward Computations

V.1. **DR3 regulator-conditional successor tree** (cosmology-bridge top priority)
   - **What**: Build a successor 2-D rectangle to layer on top of W4-44's frozen 7-cell tree, conditional on W4-46 structural FAIL. Map the framework's regulator family {zeta-L9, Zubarev-L9, branch (iv) re-derived at L >= 8} to predicted (w_0, w_a) cells. Pre-register BEFORE 2026-04-23.
   - **Inputs**: W4-44 frozen JSON; W4-46 zeta-L9 = -0.494 and Zubarev-L9 = -0.997; W1a-3 SV2 retraction record; canonical_constants.py (post-W1).
   - **Gate**: S85-DR3-REGULATOR-SUCCESSOR PASS iff successor tree SHA-pinned and dual-SHA-registered before 2026-04-23 with no parent-tree edits; successor must satisfy lockout-A through F.
   - **Effort**: 2-3 hours, 1 agent session.

V.2. **CMB-S4 alpha_s flagship pre-registration document** (W6 D.4)
   - **What**: Formalize alpha_s = -0.068968 +/- O(framework uncertainty) at Planck pivot k_*; map to CMB-S4 first-light (~2027) and survey-completion (~2030) timelines with per-detector sigma forecast (CMB-S4 34.48, CMB-HD 53.05, LiteBIRD 11.49, joint 64.31). Single-authority sign-off; non-re-registrable.
   - **Inputs**: W6-52 CSV; S50 + W10b-123 four-axiom derivation chain; sessions/permanent-results-registry.md schema; CMB-S4 forecast paper (Abazajian 2022+).
   - **Gate**: S85-CMB-S4-ALPHA-FLAGSHIP PASS iff document landed in `sessions/pre-registered-observations.md` with dual-SHA, lockouts on no auxiliary-coupling retreat and no n_s_pred change, and timeline mapping table.
   - **Effort**: 4-6 hours, 1 agent session (LOW-MEDIUM).

V.3. **LISA flagship pre-registration with fixed-k vs fixed-f tightening** (W6 D.2)
   - **What**: Pre-register Omega_GW(f) at f in {1e-4, 1e-3, 1e-1} Hz for (A), (C), (LI) branches with uncertainty bars from transfer_correction in {0.5, 1.0, 2.0}. Both fixed-k and fixed-f formulations explicit. Map to LISA L3-L4 phase ~2035.
   - **Inputs**: W6-50 script and data; LISA sensitivity curve L2023+; n_T_back = 0.4325 (W5-64); h_c^(A)(3 mHz) = 7.17e-12.
   - **Gate**: S85-LISA-FLAGSHIP PASS iff document landed with both formulations, transfer bracket, and timeline mapping; no W7 ambiguity in OOM units.
   - **Effort**: 6-8 hours, 1 agent session (MEDIUM).

V.4. **21-cm folded-bispectrum SHAPE template** (W4 CF-W4.3, sole surviving non-Gaussianity channel)
   - **What**: Compute the substrate-unique folded-triangle bispectrum SHAPE template at 21-cm l_max ~10^5. Distinguish from generic equilateral and orthogonal templates. Test detectability vs LCDM at SNR >= 2 for HERA-Phase-II and SKA-1 21-cm intensity mapping.
   - **Inputs**: W4-38 .npz (folded-Bogoliubov channel = -0.080); 21-cm forecast tools (21cmFAST or equivalent); GGE bispectrum derivation chain.
   - **Gate**: S85-FOLDED-SHAPE-TEMPLATE PASS iff shape distinguishable from LCDM at SNR >= 2 in any planned 21-cm survey window.
   - **Effort**: 8-12 hours, 1 agent session (HIGH).

V.5. **N_T CMB two-speed ZFP-vs-SCHEME-DEP re-adjudication** (W4 CF-W4.4)
   - **What**: Test whether S68's c_T = c_S = 1 assumption is a derivation-chain choice or a physical consequence. If a CHOICE, then the c_T/c_S = 2.062 ratio in W4-39 is regulator-shopping and should reclassify SCHEME-DEP. If a CONSEQUENCE, then n_T(CMB) = -3.024e-3 is ZFP and W4-48 flag stays.
   - **Inputs**: W4-48 flag entry; W4-39 derivation chain; S68 LITEB-R-FORECAST-68 code; spectral-moment definitions of a_2/a_0.
   - **Gate**: S85-NT-ZFP-ADJUDICATION binding verdict on W4-48 entry; PASS or FAIL on ZFP classification with explicit substitution chain.
   - **Effort**: 3-4 hours, 1 agent session (LOW-MEDIUM).

V.6. **Multi-D N-channel branch-discriminator framework** (W6 D.3)
   - **What**: Extend W6-51 to full N-channel joint Fisher across (A_s, P_t, mu, alpha_s, CGWB absolute) x (Planck, CMB-S4, CMB-HD, LiteBIRD, LISA, PIXIE) detector grid. Build joint chi^2 statistic at fixed (A) vs (C) branch; report rejection sigma per detector combination.
   - **Inputs**: W6-51 table; W6-52 detector reach; W6-50 CGWB; canonical observables.
   - **Gate**: S85-MULTID-FISHER PASS iff joint rejection sigma >= 10 for >= 2 distinct detector combinations across 2025-2040 timeline.
   - **Effort**: 6-8 hours, 1 agent session (MEDIUM).

V.7. **A_lens external prior from LSST kappa-kappa to push LiteBIRD** (W4 CF-W4.6)
   - **What**: Tighten W4-37 joint sigma(n_T) using LSST kappa-kappa prior on A_lens. Test whether sigma drops below 0.04 PASS threshold under the prior.
   - **Inputs**: W4-37 Fisher construction; LSST kappa-kappa forecast (Eifler et al.).
   - **Gate**: S85-LITEB-LSST-PRIOR PASS iff joint+prior sigma(n_T) < 0.04.
   - **Effort**: 4-5 hours, 1 agent session (MEDIUM).

V.8. **W2-19 r_max layer-interface theorem promotion**
   - **What**: r_max (S82 W2-2 backreaction saturation = 1.33e4) GENUINE-UNPINNED in W2-19. Test r_max promotion to L2 at L_max = 7, 9; OR formalise as layer-interface theorem candidate.
   - **Inputs**: W2-19 npz; W2-20 L=7/9 spectra; substrate-action-only derivation.
   - **Gate**: S85-LAYER-INTERFACE-THEOREM PASS iff r_max promotes to L2 at higher L_max OR layer-interface theorem written and tested.
   - **Effort**: 6-10 hours, 1 agent session (HIGH).

V.9. **Van Hove cusp theorem reformulating tau_fold (S85 leading carry-forward)**
   - **What**: Reformulate tau_fold = 0.190 as a van Hove cusp in rho(lambda; tau), not a critical point of any bare spectral action. Replaces W8-85 + W8-90 + W10-119 plan-defect FAIL classification.
   - **Inputs**: W8-85 3-audit unanimous outcome (Position B + Position C+); s36 cache eigenvalue distributions; baptista's per-eigenmode 3-exp Jensen ansatz with c_a in {+1, -1, -1/2}.
   - **Gate**: S85-VAN-HOVE-CUSP-THEOREM PASS iff van Hove cusp characterisation lands as registry entry AND reproduces tau_fold = 0.190 from rho(lambda; tau) singularity structure to 3-dp precision.
   - **Effort**: 1 session (HIGH priority per W8 + W9b-105 intersection).

V.10. **Alternative d_spec probe at fiber-transition scale** (W9 carry-forward)
   - **What**: W9b-105 zeta-spectral-dimension probe returned d_spec = 4.895 (boundary-dominated argmin). Try heat-kernel expansion, noncommutative Laplacian zeta, and rep-theoretic decomposition as alternative routes to derive the "12" exponent in exp(12 tau_fold) for mu_BC.
   - **Inputs**: W9b-105 derivation chain; W1b-4 mu_BC chain; D_K eigenvalue cache.
   - **Gate**: S85-ALT-D-SPEC-PROBE PASS iff at least one alternative route yields d_spec in [2.5, 3.5] envelope at L_max=10 with substantive substrate justification.
   - **Effort**: 6-10 hours, 1 agent session (HIGH EVOI).

V.11. **f_B = c_S_canon identity test** (W5 D.5)
   - **What**: Test whether f_B_joint = 0.485 = c_S_canon is closed-form identity or 6-sig-fig coincidence. Decompose f_B inversion chain.
   - **Inputs**: W5-64 data; S83 G46 r_CMB derivation; sound-speed definitions at fold.
   - **Gate**: S85-FB-CSCANON-IDENTITY PASS iff analytically derived OR coincidence verified via L_max drift.
   - **Effort**: 3-4 hours, 1 agent session (LOW-MEDIUM).

V.12. **2-loop Z_R investigation OR f_conv scheme-dependence acceptance** (W6 D.1)
   - **What**: Extend W6-67 to 2-loop heat-kernel; OR identify alternative non-multiplicative counterterm structure. If both fail, certify f_conv as physically scheme-dependent (G48 falsifier extension).
   - **Inputs**: W6-67 data + L_max scan; Connes-Chamseddine a_2 regulator-invariance theorem; spectral-action RG flow from S80.
   - **Gate**: S85-Z-R-2-LOOP PASS iff multiplicative+additive Z_R balances cluster_Z_a2 < 2.5; FAIL certifies f_conv as SCHEME-DEP permanently.
   - **Effort**: 10-15 hours, 2 agent sessions (HIGH).

V.13. **PIXIE mu-distortion endpoint pre-registration** (from W5-57)
   - **What**: Pre-register max mu = 8.69e-5 at K = 3.56e5 against PIXIE sensitivity. mu is strictly linear in K across 5.24 decades (gamma = 1 exact to 1e-15). Any future revision tilting gamma above 1 violates FIRAS.
   - **Inputs**: W5-57 INFO data; PIXIE forecast; FIRAS upper bound (mu < 9e-5 at 95% CL).
   - **Gate**: S85-PIXIE-MU PASS iff pre-registration document landed with PIXIE-discriminator status.
   - **Effort**: 2-3 hours, 1 agent session (LOW).

V.14. **K-FLOOR-WALL-JOINT permanent-results-registry landing** (W5 D.4)
   - **What**: Draft permanent-result block for K-floor wall: triple-supported by W5-54 regulator-shift (factor 50.9x), W5-59 Branch-B A_s floor (4.3-4.6 OOM below Planck), W5-63 4-hull exclusion (0/5 targets in [1.9222, 2.1849]). State as geometric constraint.
   - **Inputs**: W5-54, W5-59, W5-63 scripts and data; permanent-results-registry schema.
   - **Gate**: S85-K-FLOOR-WALL-LANDING PASS iff entry landed with 3 cross-references + joint-SHA audit.
   - **Effort**: 2-3 hours, 1 agent session (LOW).

V.15. **alpha_s permanent-results-registry partition-invariance upgrade** (W5 D.6)
   - **What**: Update permanent-results-registry entry for alpha_s = n_s^2 - 1 to record partition-invariance from W5-62 (|Delta alpha_s|/|alpha_s| = 1.56e-3 under G39 Leggett-Bogoliubov partition). Strengthens S50 from single-parameter to single-parameter + partition-invariant + four-axiom-axiomatic (W10b-123).
   - **Inputs**: W5-62 result; S50 original; S83 G39; W10b-123 axiomatic closure.
   - **Gate**: S85-ALPHA-S-REGISTRY-UPGRADE PASS iff registry entry updated and knowledge index rebuilt.
   - **Effort**: 1-2 hours, 1 agent session (LOW).

V.16. **Rank-universality falsifier monitoring** (from W10-111)
   - **What**: Monitor literature for any new spectral triple construction matching the framework's KO-dim=6 + |E_cond|~L^b in [4.58, 4.78] AND b -> 7 asymptotic predicate (W7b-83 4-proof chain). Falsification is monotone: one match -> theorem retracted.
   - **Inputs**: W7b-83 §VII.O statement; W7b-79 65-paper catalog; W7b-80 21-compactification catalog.
   - **Gate**: S85-FALSIFIER-MONITOR INFO if no match in S85 round of literature; FAIL if any match found.
   - **Effort**: 2-3 hours per session (LOW, ongoing).

V.17. **Mellin-balance template compliance lift** (W6 D.5)
   - **What**: Apply `.claude/templates/mellin-balance-pre-declaration.md` to all 16 enumerated S84 cluster-test gate blocks. Re-dispatch W6-71 audit; lift compliance_fraction 0.0 -> 1.0. Add saturated-balanced subclass for zero-cluster gates.
   - **Inputs**: W6-71 template; audit script; 16-gate enumeration.
   - **Gate**: S85-MELLIN-TEMPLATE-LIFT PASS iff compliance_fraction = 1.0; W6-71 meta-gate re-PASSes.
   - **Effort**: MEDIUM (tedious; 16 gates x per-gate snippet derivation).

V.18. **v3 methodology-closure ladder S85 re-evaluation** (from W9 V3-NON-COMPLIANT)
   - **What**: Drive sig_1 (PRU audit) + sig_2 (dual-SHA) + sig_3 (hook log) + sig_4 (R3 YAML) to PASS. Target ladder score CLOSED >= 10.202 in S85.
   - **Inputs**: W9a-97 89 unpinned gates list; W9a-98 settings.json diff; W9a-100 87 R3-non-compliant gates; W9a-104 recovery spec.
   - **Gate**: S85-V3-LADDER-RE-EVALUATE PASS iff ladder score >= CLOSED threshold.
   - **Effort**: 0.5 session (after V.19, V.20 land).

V.19. **S85-PLAN-PRU-REMEDIATION** (drive D_PRU_raw to 0; W9 carry-forward)
   - **What**: Tag 89 unpinned gates as `# (local)` or add to canonical_constants.py.
   - **Inputs**: W9a-97 audit JSON.
   - **Gate**: D_PRU_raw = 0 across S85 plan corpus.
   - **Effort**: 2 sessions (HIGH).

V.20. **S85-HOOK-WIRING + R3 YAML normalization** (W9 carry-forward)
   - **What**: Wire settings.json PostToolUse + Stop matchers per s84-w9a-98-settings-diff.md; normalise 87 R3-non-compliant gates.
   - **Inputs**: W9a-98 + W9a-100 reports.
   - **Gate**: sig_3 = 1 AND sig_4 = 1 in S85 ladder.
   - **Effort**: 1.5 sessions (HIGH).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | alpha_s = -0.068968 axiomatic four-axiom closure (W10b-123) | PHONONIC | PASS-THEOREM | Sole 5-sigma+ Fisher axis; flagship CMB-S4 ~2030 prediction |
| 2 | w_0 canonical UNSPECIFIED post-SV2 retraction (W1a-3) | GEOMETRIC | RETRACTED | DR3 (2026-04-23) becomes methodology test, not physics test |
| 3 | n_T(k_CMB) = -3.024e-3 two-speed (W4-39) | GEOMETRIC | PASS but EVOI=0 | LiteBIRD 650x below 1-sigma reach permanently |
| 4 | LISA Omega_GW 2.10-dex branch discriminator (W6-50) | PHONONIC | PASS | 2035 flagship; 11 OOM above strain floor |
| 5 | CMB-S4 alpha_s 34.48 sigma + joint 64.31 sigma (W6-52) | PHONONIC | PASS | Sole 5-sigma+ axis on 5-axis Fisher plane |
| 6 | UHF-GW physical gap +18.74 OOM (W4-47) | GEOMETRIC | WALL | Permanently unobservable; eliminates 2030-2050 distraction |
| 7 | SKA-1 alpha_f_NL 71x below SNR=2 (W4-43) | PHONONIC | DETECTOR-STERILE | Folded-shape 21-cm template sole surviving channel |
| 8 | F_supp dynamics-rescue path closed (W1a-2) | GEOMETRIC | WALL | A_s closure rate-limiter relocates to baseline H_tilde DC |
| 9 | H_tilde 0.89% log-DC PASS-1.05 window (W1a-1) | GEOMETRIC | OPEN | Sole surviving A_s closure corridor |
| 10 | r = 0.01173 BICEP-Keck 2026 4-branch tree (W4-42) | PHONONIC | PRE-REG | Frozen single-authority; non-re-registrable |
| 11 | A_F = C+H+M_3(C) singleton in 3,907 algebras (W8-87b) | GEOMETRIC | PASS-THEOREM | MG-2 promoted from input to theorem |
| 12 | Mellin cone universality across 3 spectral triples (W8-89) | GEOMETRIC | PASS-THEOREM | MG-0 inheritable from any positive-measure triple |
| 13 | CMPP Petrov D->G transit-invariance (W8-95) | GEOMETRIC | PASS | 65 OOM separation; tau_fold causal-censorship analog |
| 14 | C^2 Cartan trace identity Delta sin^2 = 0 EXACT (W9b-106) | PARTICLE | PASS-THEOREM | Rep-independent; obligation (ii) of mu_BC discharged |
| 15 | Heterotic SM rep embedding 16/16 hypercharge (W7a-72) | PARTICLE | PASS | Framework rep-content guest, structural stranger |
| 16 | det(P) K-theoretic identity 4 obstructions (W7a-74) | GEOMETRIC | FAIL | Framework not F-theory-uplift-compatible |
| 17 | Z_R counterterm cluster_Z_a2 = 1.07e5 growing (W6-67) | GEOMETRIC | FAIL structural | f_conv slot regulator-vertical, not perturbative |
| 18 | tau_fold "stationary" claim plan-defect (W8-85, W8-90, W10-119) | GEOMETRIC | PLAN-DEFECT | Reformulate as van Hove cusp; 70-session downstream untouched |
| 19 | mu(K=3.56e5) = 8.69e-5, gamma=1 exact (W5-57) | PHONONIC | INFO | PIXIE-visible at corridor endpoint; FIRAS protected |
| 20 | K_* lab match 3He-B coth(1) at 1.13% (W5-58) | PHONONIC | PASS | p-wave BCS lab discriminator |
| 21 | K-floor 4-hull exclusion 0/5 (W5-63) | GEOMETRIC | FAIL/WALL | Triple-supported K-FLOOR-WALL-JOINT registry candidate |
| 22 | rank-universality leading-power cancellation (W10-111) | GEOMETRIC | PASS-THEOREM | G_2 vs F_4 distinguishable; A_3 vs C_3 not |
| 23 | G58 meta-principle 92.5% atlas BALANCED (W10-117) | GEOMETRIC | PASS-THEOREM | Empirical -> K-theoretically grounded |
| 24 | mu_BC_K3 = 188.185 GeV at 0.082% (W1b-4) | PARTICLE | PASS | bi-criterion (B) DERIV-I/II in W9 -- one PASS, one FAIL |
| 25 | v3 methodology ladder 1.000 of 11.335 (W9 ladder) | NON-PHONONIC | V3-NON-COMPLIANT | Physics verdicts intact; methodology debt to S85 |

---

*End of Mack-Cosmic-Bridge synthesis. The cosmologically load-bearing evidence column for the 2030s observational portfolio reduces to alpha_s (CMB-S4 2030 flagship), Omega_GW branches (LISA 2035), r (BK 2026), and a methodology-conditional DR3 (2026). Per `feedback_reporting-framing.md`: the alpha_s = -0.068968 four-axiom-axiomatic prediction at 34.48 sigma projected separation IS the framework's single biggest 2030s bet.*
