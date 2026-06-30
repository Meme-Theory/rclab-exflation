# Session 77 Synthesis: The A_s Inversion and the Cosmological Constant as Spectral Fill Factor

**Date**: 2026-04-13
**Agent**: mack-cosmic-bridge (mack)
**Source Documents**:
- sessions/archive/session-77/session-77-results-workingpaper.md

---

## I. Session Outcome

Session 77 discovered a normalization error propagating since S73B that inverts the A_s gap from underproduction to overproduction: the CMB pivot mode is SUBhorizon at the fold (k/aH = 14.7), not 57 OOM superhorizon. With corrected normalization, the framework produces P_zeta 9.5 OOM ABOVE Planck at the pivot scale, reframing the central A_s problem from "how to amplify" to "what suppresses." Independently, the cosmological constant story advanced decisively: chi_2 = <sqrt(x)> is proven algebraically exact, proven nonlocal by four independent arguments (formally evading Weinberg's no-go theorem), and the epoch where Omega_Lambda = chi_2 lies only 1.4 Gyr in the future, with the coincidence problem resolved by construction through the analytical formula (a*/a_eq)^3 = chi_2/(1-chi_2). The S65 LISA domain-wall GW prediction is retracted -- Josephson bias annihilates walls 15,000x before reheating.

## II. Key Results

### II.1 The A_s Inversion (W2-A, W3-O, W1-B) -- Observational Status: CRITICAL

This is the session-defining result and it demands careful unpacking from an observational perspective.

**The error**: S73B compared k_pivot = 0.05 Mpc^{-1} (in a_today = 1 convention) against aH from the ODE trajectory (a_fold = 1 convention). These are different normalizations, separated by a factor exp(N_total) = 3.32e57. The correct comoving wavenumber in fold normalization is k_pivot(fold) = 14.31 M_KK, giving k/aH = 14.7 -- the mode is subhorizon by a factor of 15.

**What this changes**:
- k^2/(z''/z) at the fold goes from 1.04e-116 (irrelevant) to 107.6 (dominant). The mode equation's k^2 term matters.
- The pivot mode exits the horizon at N_pivot = 3.12 e-folds after the fold, placing it N_* = 60.3 e-folds before reheating -- consistent with the standard inflationary window of 50-60 e-folds for T_RH ~ 10^{15} GeV.
- The stiff-to-dS transition at N ~ 0-3 directly affects the CMB pivot mode while it is still subhorizon.

**What this means for A_s**: W3-O solves the full Mukhanov-Sasaki mode equation with plane-wave Bunch-Davies initial conditions. The stiff-to-dS transition (eps_H drops from 1.72 to 0.005 in ~1 e-fold) acts as a parametric amplifier: F_amp = 6858 at k_pivot (3.84 OOM enhancement). Combined with P_dS(bare) = 9.8e-4 (already 5.67 OOM above A_s = 2.1e-9 because H_phys = 4.7e16 GeV >> 10^{14} GeV for standard inflation), the total is P_zeta ~ 6.7 at the pivot -- 9.5 OOM above Planck.

**Observational assessment**: The overproduction is severe but its physical meaning depends entirely on the initial conditions at the fold. Plane-wave Bunch-Davies is an assumption, not a derivation. In standard inflationary cosmology, the BD vacuum is selected by the adiabatic theorem -- modes start deep inside the horizon in a quasi-static background. Here, the fold IS the phase transition. There is no "before" in the same sense. The pre-fold vacuum state is the key unknown and must be derived from the phase transition physics in S78.

**PBH constraint**: At the transition scale k_trans = 3.4e-3 Mpc^{-1}, P_zeta = 0.089 exceeds the 10^{-2} PBH threshold. This corresponds to M_PBH ~ 45 M_sun. If confirmed, LIGO/Virgo merger rate constraints and FIRAS spectral distortion bounds become relevant. This is a falsifiable prediction contingent on the IC assumption.

**Prior results invalidated**: W1-B's A_s = 9.11e-13 (gap = 3.36 OOM) used the wrong k. The "superhorizon at the fold" assumption in all prior A_s gap computations (S63, S64, S66, S69, S75, S76) is incorrect. The f_conv story (S75/S76: A_s = 1.585e-9, 0.12 OOM gap) used a formula that assumed the mode was frozen; it was not. The multi-cell coherence E = 29.42 from W3-B (1.47 OOM closure) is real physics but was computed to close a gap in the wrong direction -- it now makes the overproduction worse.

### II.2 Cosmological Constant: Three Interlocking Results (W1-D, W3-K, W3-L)

**chi_2 = <sqrt(x)> is exact** (W1-D PASS). The identity chi_2 = M_1/(N * lambda_max) = <|lambda|>/lambda_max = <sqrt(lambda^2/lambda_max^2)> is algebraic, confirmed to machine precision at all L_max. The physical f* (0.912*sqrt(x) + 0.088*exp(-x)) reproduces chi_2 to 0.95%, with the residual entirely attributable to the 8.8% exponential component.

**chi_2 is provably nonlocal** (W3-K). Four independent proofs: (A) The sign function of D requires a polynomial of degree N-1 = 21 at L=5, making it full-spectrum-dependent. (B) M_1 = Tr(|D|) = Tr((D^2)^{1/2}) involves a square root, not a polynomial -- the moment parity argument. (C) Two flat tori with identical area (hence identical SDW coefficients a_n) have different chi_2 values (4.9% for aspect ratio 2:1) -- direct proof that chi_2 detects global geometry invisible to local curvature invariants. (D) chi_2 = zeta_D(-1)/(N * lambda_max) is a zeta function value at a non-pole point, algebraically independent of the residues that generate SDW coefficients. This formally evades the assumptions of Weinberg's 1989 no-go theorem, which requires the vacuum energy to decompose as a sum of Lambda^4-weighted local operator traces. chi_2 is bounded in [0,1], UV-insensitive (8.5% drift from L=3 to L=9), and a ratio that cancels Weyl-divergent growth.

**Epoch convergence is structural** (W3-L). The analytical formula a*^3 = chi_2 * Omega_m / [Omega_Lambda * (1 - chi_2)] gives a* = 1.097 (z* = -0.088, 1.4 Gyr in the future). Any O(1) spectral fill factor chi_2 guarantees a match epoch a* within O(1) of the matter-Lambda transition era. The coincidence problem is resolved by construction: we observe Omega_Lambda ~ O(1) because chi_2 ~ O(1) and the matter-Lambda transition is happening now.

**CC gap status**: The "Direct" conjecture chi_2 = Omega_Lambda gives 0.034 OOM gap (8.2% overshoot, zero free parameters). The standard Friedmann-normalized Route C (chi_2/3 = Omega_Lambda) gives 0.44 OOM. W2-E confirmed all S76 values to < 0.01 OOM precision but identified a naming disambiguation: "0.034 Route C" in the S76 workshop was actually the direct comparison, not Route C as defined in the S76 computation script. The factor-3 Friedmann normalization remains the sole open physics question. The GGE occupation correction is closed as a resolution channel (W3-G FAIL: delta_chi_2 = 9.6e-6, 150,000x too small, because 8 BCS modes are 6.9e-7 of the total spectral weight).

### II.3 Domain-Wall GW Retraction (W3-H FAIL)

The S65 prediction (Omega_GW ~ 10^{-10}, LISA-detectable) is retracted. The Josephson bias epsilon_bias = J_C2 * Delta_BCS = 0.433 M_KK^4 annihilates domain walls in t_ann = 1.1e-41 s, which is 15,000x shorter than the modulus decay/reheating timescale tau_decay = 1.63e-37 s. By the time the universe reheats, no walls remain. The GW signal peaks at 915 MHz (no detector coverage), with LISA band Omega_GW = 5e-45 (33 OOM below sensitivity).

This is structurally forced: the same Josephson physics that closed Z_2 domain-wall DM in S76 kills the GW signal. The framework no longer has a gravitational-wave prediction accessible to any planned detector. The stochastic GW background from the transit itself (S76: Omega_GW = 2.25e-25, f_peak = 231 MHz) remains 13-16 OOM below all detectors. The 21cm ISW cross-power (S71: +4.0%, SNR = 4.16 ideal) is now the framework's most accessible novel prediction.

### II.4 Modulus Stabilization: BCS 72x Too Weak (W1-A, W1-A Retask)

The bare spectral action V(tau) is monotonically increasing (proven S36). The BCS condensation energy E_cond = -0.137 M_KK is 1.05e-4 of V_bare at the fold. The gradient ratio |dE_cond/dtau| / |dV_bare/dtau| peaks at 0.90 (van Hove enhanced, tau_w = 0.01) but never exceeds 1. No minimum exists in V_eff(tau) for any physically motivated BCS model. The factor of 72x shortfall (at tau_w = 0.05) traces to mode counting: V_bare sums ~31,000 weighted modes while E_cond comes from 8 BCS-active modes.

The R-protected ratio R_1 = a_0*a_4/a_2^2 is stable to 0.39% across [0, 0.5] (W1-A), confirmed by the full tau trajectory (W2-F: 11.1% total variation across [0, 0.5], but only 0.34% L_max drift). This means ratio-of-ratios observables survive regardless of modulus stabilization.

Resolution channels: multi-band BCS (extending pairing beyond the (0,0) sector), spatial Josephson stiffness, tadpole cancellation (V_bare as constraint), and non-perturbative instantons. The multi-band route is most promising -- 0.5% of the spectrum participating in pairing would exceed the 72x threshold.

### II.5 Weinberg Angle: Tree-Level Route Permanently Closed (W2-D, W3-F, W3-N)

Three results jointly close all tree-level KK threshold routes to sin^2(theta_W):

1. **W2-D** (LR-THRESHOLD FAIL): The L-R metric distinction from Paper 13 eq (3.41) gives sin^2(M_Z) = -0.308 (wrong sign). The sign is structural: U(1) is heavy (L_1 > 1 at the fold), so the L-R correction amplifies the U(1) threshold, driving sin^2 negative.

2. **W3-F** (MODE-THRESHOLD PASS): The eigenvalue-resolved computation at L_max = 6 (439,488 PW-weighted modes) confirms Delta_2/Delta_3 = 1.000000 and Delta_1/Delta_3 = 20/9 to machine precision. The Dynkin index ratio is a representation-theoretic identity, independent of eigenvalues, tau, and L_max.

3. **W3-N** (PATI-SALAM INFO): No intermediate Pati-Salam symmetry exists. All Jensen eigenvalue ratios are strictly monotone for tau > 0. Rank obstruction: Pati-Salam (rank 5) and LR-symmetric (rank 3) both exceed SU(3) (rank 2).

The universal threshold model (delta_1 = delta_2 = delta_3 = S_inf) gives sin^2(M_Z) = 0.229 (1.2% from PDG), but this violates the permanent Dynkin theorem delta_1/delta_3 = 20/9. The S72 Model A match was an accident. The empirical formula sin^2 = 3/(8+6*sin^2(2*pi/3)) = 0.2348 (1.55% from PDG) has no derivation -- finding one is an S78 problem.

### II.6 BCS Timing Confirmed (W2-H PASS)

The temporal ordering dt_transit << tau_relax << t_BCS << T_BCS_osc is established by three independent arguments: (1) N_osc = 8.4e-5 BCS oscillation periods fit in the transit (the pairing interaction cannot complete a single cycle), (2) the GL instability growth time is 60x the transit duration, (3) full gap formation time exceeds 100x the transit in all seed models. The BCS gap is absent during the Bogoliubov squeeze. Even in the counterfactual, Landau-Zener analysis gives P_diabatic = 0.9996 -- the transit is sudden even on the BCS energy scale.

This validates the post-transit GGE construction: the squeeze completes, then BCS condensation develops. The Bogoliubov calculation (n_Bog = 0.999) is self-consistent.

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S77-A1-EQUIL-TAU (bare + BCS retask) | FAIL | BCS 72x too weak; |E_cond|/V_bare = 1.05e-4 |
| S77-A2-BOG-FRIED-AS | INFO | A_s = 9.11e-13, gap 3.36 OOM (invalidated by W2-A normalization fix) |
| S77-A3-MU-EFF-B2 | FAIL | mu_eff = 8.58e-4 < 0.001; bottleneck migrates from B1-B3 to B2-B3 |
| S77-A4-DIRECT-SUM-FSTAR | PASS | chi_2 = <sqrt(x)>, f* matches to |delta| = 0.0095 |
| S77-B1-NPIVOT | INFO | k_pivot = 14.31 M_KK SUBHORIZON; N_pivot = 3.12; S73B error identified |
| S77-B2-P-FRIEDMANN | INFO | p_S75 (shape parameter) != p_cosmo (Friedmann); incommensurable |
| S77-B3-FCONV-FSTAR | PASS | f_conv(f*)/f_conv(SDW) = 1.784; exact identity |
| S77-B4-LR-THRESHOLD | FAIL | sin^2(M_Z) = -0.308; L-R correction worsens; Dynkin obstruction permanent |
| S77-B5-ROUTE-C | PASS | S76 values confirmed; naming disambiguation resolved |
| S77-B6-R1-TRAJECTORY | INFO | R_1 monotone increasing; NOT stationary at fold; dR_1/dtau = +0.203 |
| S77-B7-MEAN-EIGEN | INFO | <|lambda|> = 1.581; dS/dt* = +764 (anti-restoring) |
| S77-B8-BCS-TIMING | PASS | t_BCS/dt_transit in [102, 160]; N_osc = 8.4e-5 |
| S77-B9-FRICTION | INFO | N_osc = 0; F_total = 60.33; Hubble friction dominates decay 48x |
| S77-B10-V-TAU-VALID | INFO | Direct computation reliable to tau = 2.0; premise "data only [0,0.5]" false |
| S77-B11-SA-TRUNC | INFO | Residual = 3.76% of a_4 term; a_n are zeta moments, not HK coefficients |
| S77-C1-CMPP-TURN | INFO | Static Type D at all tau; transit-invariant |
| S77-C2-MULTI-CELL | PASS | E = 29.42; 1.47 OOM (now exacerbates overproduction) |
| S77-C3-SPECTRAL-Z | FAIL | z_fw/z_GR = 1.014; z variable NOT source of A_s gap |
| S77-C4-A2-OVERSHOOT | INFO | G_N varies 6.28x during overshoot; a_2 monotone decreasing |
| S77-C5-HESSIAN-OVERSHOOT | PASS | 35/35 negative at tau = 1.614; Jensen ridge persists |
| S77-C6-MODE-THRESHOLD | PASS | Delta_2/Delta_3 = 1.0 exactly; Dynkin permanent |
| S77-C7-GGE-OCC | FAIL | delta_chi_2 = 9.6e-6; 150,000x too small (8/408M modes) |
| S77-C8-DW-GW | FAIL | Omega_GW peak at 915 MHz; LISA 33 OOM below; S65 retracted |
| S77-C9-A4-GILKEY | PASS | R^2 dominance 101.6%; f_conv^{zeta} = 2.258e-10 |
| S77-C10-YUKAWA-PMNS | INFO (NULL) | All cross-sector Yukawa = 0 exactly |
| S77-D1-WEINBERG-LOCAL | INFO (PROVEN) | chi_2 nonlocal by 4 arguments; evades Weinberg no-go |
| S77-D2-EPOCH-CONV | INFO | a* = 1.097 (1.4 Gyr future); coincidence structural |
| S77-D3-R1-UNIVERSAL | INFO | R-protection on SU(3)/SU(4)/Sp(2); higher rank = better |
| S77-D4-PATI-SALAM | INFO | No intermediate symmetry; rank obstruction; SM unique for tau > 0 |
| S77-D5-TRANS-PBH | INFO | F_amp = 6858 at pivot; P_zeta = 6.73; A_s gap = -9.5 OOM (overproduction) |

**Master Gate S77-MASTER**: INFO (2/3 PASS conditions met, 13/30 = 43.3% decisive, below 60% threshold)

## IV. Structural Implications

### IV.1 The A_s Problem Is Now a Suppression Problem

From S63 through S76, the framework's A_s problem was "how to amplify a too-small perturbation spectrum." Every computation -- f_conv, PW selection rules, BCS occupation, Bogoliubov pairs, multi-cell coherence -- was designed to close a gap measured in positive OOM above Planck A_s = 2.1e-9.

S77 shows the gap has the wrong sign. The framework's H_phys ~ 4.7e16 GeV (set by the spectral action scale) produces P_dS(bare) ~ 10^{-3}, already 5.67 OOM above Planck. The stiff-to-dS transition amplifies this by 3.84 OOM. The "amplification" mechanisms (f_conv, multi-cell coherence, Bogoliubov enhancement) all make the problem worse.

The pre-fold vacuum state is the sole remaining degree of freedom. Standard inflation selects Bunch-Davies through the adiabatic theorem. In the substrate picture, the fold IS the phase transition -- there is no adiabatic past. The vacuum state must be derived from the phase transition physics. If it is "squeezed" (a generic expectation for a first-order transition), P_zeta could be either enhanced or suppressed depending on the squeeze direction.

**Observational consequence**: Until the pre-fold vacuum state is determined, the framework cannot make a quantitative A_s prediction. The qualitative features (n_s from spectral geometry, f_NL ~ 1 from GGE, tensor-to-scalar ratio from Bogoliubov) survive because they depend on mode ratios and spectral indices, not absolute normalization. But the absolute power spectrum amplitude -- the single most precisely measured number in CMB physics (A_s = (2.099 +/- 0.014) x 10^{-9}, Planck 2018) -- is now undetermined.

### IV.2 The CC Story Strengthens

The three CC results form a coherent chain:

1. chi_2 IS a spectral fill factor -- exactly <sqrt(x)> weighted by degeneracies (W1-D).
2. chi_2 is nonlocal -- it detects global spectral geometry, not local curvature (W3-K).
3. chi_2 matches Omega_Lambda at an epoch structurally close to the present (W3-L).

The Weinberg evasion is the strongest individual result here. Weinberg's 1989 argument showed that any vacuum energy composed of Lambda^4-weighted local operator traces requires 10^{-120} cancellation. chi_2 evades all three of Weinberg's assumptions: it is bounded [0,1] (no Lambda^4 scaling), UV-insensitive (convergent spectral ratio), and nonlocal (not decomposable into sector-by-sector contributions). This is not a loophole -- it is a structural evasion of the premises.

The 8.2% overshoot (chi_2 = 0.741 vs Omega_Lambda = 0.685) and the factor-3 question remain open. The GGE occupation channel is now closed (W3-G). L_max convergence of chi_2 (~5%/decade drift) is potentially sufficient but unproven. The factor-3 Friedmann normalization is the sole remaining physics question: does chi_2 = Omega_Lambda (direct conjecture, 0.034 OOM), or chi_2/3 = Omega_Lambda (standard Friedmann, 0.44 OOM)?

### IV.3 What Survives as Falsifiable

With the LISA GW prediction retracted, the framework's falsifiable prediction portfolio is:

**Currently testable (existing or near-term data)**:
- w_0 = -0.918 (DESI DR3 pre-registered, S74 falsifier band [-0.94, -0.88])
- n_s = 0.9590 (CMB-S4 pre-registered window [0.955, 0.963], 2.94-sig discrimination)
- r(CMB) = 0.024 (LiteBIRD 24.2-sig detection, n_T = -r/8 exactly at CMB scales)
- f*sigma_8(z): 4% suppression vs LCDM, correct S_8 direction (Euclid)
- ISW tracking: 12.3% FW/LCDM difference (Euclid 2.5-sig, 21cm 7.9-sig)

**Contingent on IC resolution**:
- A_s absolute normalization (currently undetermined)
- PBH at M ~ 45 M_sun from k_trans (LIGO/Virgo merger rate constraints)
- f_NL = 0.853 equilateral, 0.129 folded (CMB-S4 undetectable; 21cm sole channel)

**No longer testable**:
- Domain-wall GW (retracted, Josephson bias kills walls before reheating)
- Transit GW stochastic background (231 MHz, 13-16 OOM below detectors)

### IV.4 Scheme Dependence Remains Central

W2-B revealed that p_S75 = 1.69 (spectral action shape parameter) is not the Friedmann power-law index p_cosmo = 0.58. The n_s computation uses p_S75, which was always a fitted parameter. This does not invalidate the n_s prediction but clarifies its status: n_s = 0.9590 (from BCS + one-loop, S65) is structurally frozen and observationally viable (1.40-sigma from Planck), but the Route 2 prediction (n_s = 0.9649 from isocurvature decay, matching Planck exactly) retains a free parameter. W1-C confirmed that mu_eff = 8.58e-4 from B2 mediation is FAIL -- the target mu_eff = 0.0102 requires J(B1-B3) = 1.90, which is 49.9x the bare coupling. The bottleneck migrates from B1-B3 to B2-B3 when the first is enhanced.

## V. Carry-Forward Computations

### V.1 Critical (S78 Rate-Limiting)

1. **Pre-fold vacuum state**: Derive the Bogoliubov transformation from pre-fold to post-fold vacuum. This is the sole control on A_s normalization. The phase transition that creates the fold must select a specific quantum state. Compute it.

2. **Mode equation with correct k**: Re-solve the Mukhanov-Sasaki equation with k_pivot = 14.31 M_KK (subhorizon at fold) using a second independent method, verifying the W2-A normalization and the W3-O F_amp = 6858 result before building on it.

3. **Multi-band E_cond**: Extend BCS pairing beyond the 8 modes of the (0,0) sector. The 72x shortfall requires ~800 paired modes (0.5% of the 155,984 total). Does inter-band pairing exist in higher Peter-Weyl sectors?

### V.2 High Priority

4. **chi_2 L_max convergence study**: Compute chi_2 at L_max = 10, 12, 15 if computationally accessible. Currently drifting ~5%/decade. Does it converge to 0.685 (Omega_Lambda)? The factor-3 question is secondary if chi_2 converges to the right value.

5. **PBH constraint cross-check**: If the W3-O normalization and IC are confirmed, compute the PBH mass function at k_trans and compare against LIGO/Virgo O3 merger rate constraints for M ~ 45 M_sun. Also check FIRAS spectral distortion bounds (mu-distortion from P_zeta ~ 0.09 at this scale).

6. **DESI DR3 response**: Update the pre-registered decision tree with the W2-A normalization correction. Does the corrected H(z) affect the D_V(z)/r_d predictions? (Likely not -- the distance observables are set by late-time dynamics, not by the fold normalization.)

### V.3 Structural

7. **sin^2(theta_W) cubic formula derivation**: Tree-level threshold routes are permanently closed. The empirical formula sin^2 = 0.2348 (1.55% from PDG) must have a derivation from a different mechanism -- perhaps loop-level running with the spectral-action gauge coupling normalization, or a topological argument.

8. **f_conv reinterpretation**: f_conv was computed as a suppression factor converting fiber-scale perturbations to 4D observables. In the overproduction regime, it becomes part of the problem, not the solution. Reinterpret f_conv in the context of A_s ~ P_dS(bare) * F_amp * f_conv * E_multicell -- the product now exceeds Planck by many OOM. What does the framework predict for f_conv's role when A_s is being suppressed rather than amplified?

9. **Epoch convergence: f*-weighted**: W3-L shows a*(f*) = 1.079 (z* = -0.073, 1.1 Gyr future), closer to the present than a*(chi_2) = 1.097. Track both as L_max increases.

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | k_pivot = 14.31 M_KK SUBHORIZON at fold | GEOMETRIC | INFO (session-defining) | Inverts A_s gap; invalidates all prior superhorizon assumptions since S73B |
| 2 | F_amp = 6858 at k_pivot; P_zeta = 6.73 (9.5 OOM above Planck) | PHONONIC | INFO | A_s is overproduction; pre-fold vacuum state is sole unknown |
| 3 | chi_2 = <sqrt(x)> exact identity | GEOMETRIC | PASS (permanent) | CC concentration = spectral fill factor; algebraic, not approximate |
| 4 | chi_2 provably nonlocal (4 arguments) | GEOMETRIC | INFO (theorem) | Evades Weinberg no-go; CC is global spectral ratio, not local sum |
| 5 | Omega_Lambda = chi_2 at a* = 1.097 (1.4 Gyr future) | GEOMETRIC | INFO | Coincidence problem resolved; (a*/a_eq)^3 = chi_2/(1-chi_2) structural |
| 6 | BCS dressing 72x too weak for modulus stabilization | PHONONIC | FAIL | Multi-band extension (>8 modes) rate-limiting; R_1 protected regardless |
| 7 | Domain-wall GW retracted; LISA band 33 OOM below | PHONONIC | FAIL | S65 prediction retracted; Josephson bias structural |
| 8 | Multi-cell coherence E = 29.42 (1.47 OOM) | PHONONIC | PASS | Real physics but now exacerbates A_s overproduction |
| 9 | sin^2(theta_W, M_Z) = -0.308 (L-R direct) | GEOMETRIC | FAIL (permanent) | Tree-level threshold route closed; Dynkin obstruction |
| 10 | Delta_2/Delta_3 = 1.0 exactly | GEOMETRIC | PASS (permanent) | Eigenvalue-resolved confirms Dynkin; PW-independent |
| 11 | No Pati-Salam intermediate symmetry | GEOMETRIC | INFO (permanent) | SM gauge group unique for tau > 0; rank obstruction |
| 12 | BCS timing: t_BCS/dt_transit in [102, 160] | PHONONIC | PASS | Gap absent during squeeze; GGE construction validated |
| 13 | Jensen ridge: 35/35 negative at tau = 1.614 | GEOMETRIC | PASS (permanent) | Modulus confined to Jensen line through full overshoot |
| 14 | mu_eff = 8.58e-4 (B2 mediation FAIL) | PHONONIC | FAIL | n_s Route 2 retains free parameter; bottleneck migrates to B2-B3 |
| 15 | f_conv(f*)/f_conv(SDW) = 1.784 | GEOMETRIC | PASS | +0.25 OOM; now contextualized by A_s inversion |
| 16 | GGE occupation correction to chi_2: negligible | PHONONIC | FAIL | 8/408M modes; channel closed permanently |
| 17 | R-protection universal (SU(3)/SU(4)/Sp(2)) | GEOMETRIC | INFO (permanent) | Higher rank = better protection; O(L^{-rank}) |
| 18 | Inter-sector Yukawa = 0 exactly | GEOMETRIC | INFO (permanent) | Block-diag + J-conjugation; PMNS requires off-Jensen or Kosmann |
| 19 | a_4 Gilkey: R^2 dominance 101.6% | GEOMETRIC | PASS | f_conv^{zeta} = f_conv(SDW)/R_1; scheme shift 0.053 OOM |
| 20 | Route C CC values confirmed | GEOMETRIC | PASS | Direct: 0.034 OOM; Route C: 0.44 OOM; naming resolved |
