# Session 70 Synthesis: Exflation vs. Inflation -- A Structural Comparison

**Date**: 2026-04-09
**Agent**: Gen-Physicist
**Source Documents**:
- `sessions/archive/session-70/session-70-results-workingpaper.md` (46 computations across 5 waves)
- `researchers/Inflation/01_2009_Baumann_TASI_Inflation.md` (Baumann -- slow-roll formalism, Mukhanov equation)
- `researchers/Inflation/07_2008_Cheung_et_al_EFT_Inflation.md` (Cheung et al. -- EFT of inflation)
- `researchers/Inflation/16_2020_Planck_2018_X_Inflation.md` (Planck 2018 constraints)
- `researchers/Inflation/10_2018_Burgess_EFT_Inflation.md` (Burgess -- UV sensitivity, GREFT)

---

## I. Session Outcome

S70 produced 46 computations across 5 waves. The session's most consequential result is structural: the spectral action's algebraic dependence on the fiber metric g_K -- which yields c_s^2 = 0 at tree level (Q-SOUND-70 PASS) -- fundamentally distinguishes the exflation framework from all single-field slow-roll inflation models, where c_s^2 = 1 is the default and any departure requires explicit higher-derivative operators. The second major result is a failure: the alpha_s tension (F0-ALPHA-S-70 FAIL) reveals that the CCM matching formula couples the Higgs quartic and gauge coupling through a single degree of freedom g_3^2(M_KK), making simultaneous reproduction of m_H = 125 GeV and alpha_s = 0.118 impossible at tree level. This is the sharpest open quantitative gap in the framework's particle physics sector. The third headline is the Leggett vacuum excitation (LEGGETT-VACUUM-70 PASS, r_L = 0.617), which closes the A_s gap from 0.485 to 0.267 OOM. Taken with the SU(1,1) compound squeeze (W2-D, +1.79 OOM), the amplitude budget now overshoots -- a productive tension that constrains the spatial squeeze parameter.

---

## II. Key Results

### II.1. c_s^2 = 0 from Algebraic q-Variable: The Fundamental Divergence from Inflation

**Result**: c_s^2 = 3.36 x 10^{-4} (tree-level exactly zero; one-loop perturbatively small, physically suppressed by exp(-M_KK/H_0)). Classification: GEOMETRIC.

In standard single-field inflation, the Goldstone boson pi associated with broken time diffeomorphisms propagates with a sound speed determined by the EFT operator content. Cheung et al. (0709.0293) showed that the speed of sound is

c_s^{-2} = 1 - 2M_2^4 / (M_Pl^2 |dot{H}|)     ... (1)

where M_2^4 parametrizes the (g^{00}+1)^2 operator in unitary gauge. Setting M_2 = 0 gives c_s = 1 (standard slow-roll). Departures require explicit higher-derivative operators, and the Cheung et al. bound c_s > 0.028 (from f_NL constraints) restricts how far c_s can be reduced.

The exflation framework arrives at c_s^2 = 0 by a fundamentally different mechanism. The spectral action S = Tr f(D_K^2/Lambda^2) depends on the fiber metric g_K through the eigenvalues of D_K, which are functions of g_K(x) at each spacetime point but NOT of d_mu g_K(x). The heat kernel coefficients a_n(g_K) depend algebraically on the metric. No mixed derivative terms appear in the asymptotic expansion. This places the DE variable q = det(g_K) in Volovik's algebraic class, where the Lagrangian L = -epsilon(q) has no kinetic term. The numerator of c_s^2 vanishes identically at tree level:

c_s^2 = [d^2 L / d(d_mu q)^2] / [d^2 L / dq^2] = 0 / (finite) = 0     ... (2)

This is not an operator choice -- it is a structural consequence of the product geometry M_4 x K. In the EFT language of Cheung et al., the spectral action generates no (g^{00}+1)^2 or higher time-derivative operators for the q-variable, because the spectral data of the internal Dirac operator D_K cannot produce spacetime gradients of g_K.

**Inflation comparison**: In inflation's EFT, c_s is a free parameter (within naturalness bounds). In exflation, c_s^2 = 0 is derived from the spectral triple structure. The CLASS-ISW-70 full Boltzmann computation confirms the observable consequence: a 6.7% ISW auto-power difference between c_s^2 = 0 (framework) and c_s^2 = 1 (quintessence), detectable at 2.6 sigma with 21cm surveys. This is the framework's cleanest discriminant against any w = -0.918 quintessence model.

The contrast with inflation's machinery is stark. In inflation, the sound speed carries information about the UV completion (DBI inflation has c_s << 1 from the brane action; k-inflation has c_s as a function of X = g^{mu nu} d_mu phi d_nu phi). In the substrate picture, c_s^2 = 0 for the vacuum sector is a consequence of the vacuum variable q being non-dynamical -- the spectral action's algebraic dependence on g_K is the microscopic origin. There is no free parameter to adjust.

### II.2. Parametric Resonance FAIL and GGE Formation vs. Reheating

**Result**: PARAMETRIC-GGE-70 FAIL. Physical Floquet exponent mu_phys < 10^{-16} M_KK (machine epsilon). A_s enhancement = 3.86 x 10^{-15} OOM (zero). Classification: PHONONIC.

In standard inflation, reheating proceeds via parametric resonance (Kofman, Linde, Starobinsky 1997). The inflaton oscillates about the minimum of V(phi), driving Mathieu-type instabilities in coupled fields. The resonance parameter q = g^2 Phi^2 / (4 m_phi^2) determines whether the system is in the narrow (q << 1) or broad (q >> 1) resonance regime. Energy transfer occurs through exponential growth of occupation numbers in the unstable Mathieu bands.

The exflation transit is structurally incompatible with this mechanism, for three independent reasons established in S70:

(i) **Frequency mismatch**: The BCS mode frequencies omega_k sit between Mathieu tongues (a_B1 = 1.313, a_B2 = 1.398, a_B3 = 1.872), not on them. No mode overlaps any instability tongue.

(ii) **Hubble overdamping**: The damping ratio zeta = 3H/(2 omega_drive) exceeds 600 for both driving channels. The modulus undergoes monotonic rolloff, not oscillation. There is no periodic driving to create Floquet instability.

(iii) **Weak coupling**: Even at exact resonance, the growth rate mu ~ epsilon omega_drive / 4 would be 3.3 x 10^5 times below H_fold. The q parameter needed for mu > H is q ~ 1641, a shortfall of 3.7 x 10^5 from the physical value.

**Inflation comparison**: Reheating via parametric resonance requires the inflaton to oscillate about a potential minimum. The exflation modulus does not oscillate -- it transits supersonically (Mach 54.73) through a fold. There is no potential minimum to oscillate about (the spectral action is monotone along Jensen, and the fold is a saddle point in the full 35D moduli space). The analog of reheating is GGE formation: 59.8 quasiparticle pairs created via Kibble-Zurek during the single-pass transit, with occupation numbers set by the sudden approximation (not by resonant amplification). The 3He-B analog is established experimentally -- rapid pressure quenches through T_c produce quasiparticle populations set by the single-pass mechanism, not by post-quench oscillatory dynamics.

This structural difference eliminates an entire class of post-inflation phenomenology (preheating, thermalization, defect formation from oscillatory dynamics) and replaces it with a one-shot spectral reorganization.

### II.3. The alpha_s Tension Through the EFT Lens

**Result**: F0-ALPHA-S-70 FAIL. alpha_s = 0.118 requires f_0 = 6.33, where m_H = 190 GeV. m_H = 125 GeV requires f_0 = 1.33, where alpha_s = 0.020. Anti-correlation is structural. Classification: PARTICLE/GEOMETRIC.

The CCM matching formula lambda_CCM(M_KK) = (4/3) g_3^2(M_KK) ratio_gilkey couples the Higgs quartic and the gauge coupling through a single degree of freedom g_3^2(M_KK). Both alpha_s(M_Z) and m_H are monotonically increasing functions of the spectral function normalization f_0, because increasing f_0 increases g_3(M_KK) which simultaneously feeds QCD running (raising alpha_s) and the Higgs quartic (raising m_H).

**Inflation comparison**: In the EFT of inflation (Cheung et al.), different observables are controlled by different operators -- n_s depends on slow-roll parameters, r depends on epsilon, f_NL depends on M_2. The operator expansion provides enough freedom to accommodate observational constraints independently. The spectral action's moment hierarchy (a_0 for CC, a_2 for gravity, a_4 for gauge couplings) structurally constrains the operator content: the coupling constants are DERIVED, not free parameters. This is simultaneously the framework's greatest strength (fewer free parameters means more predictive) and its sharpest vulnerability (when the derived values miss observation, there is no knob to turn).

The alpha_s tension is analogous to the eta problem in inflation (Burgess, 1711.10592): Planck-suppressed operators generically give Delta eta_v ~ 1, spoiling slow-roll. In inflation, the eta problem is addressed by imposing symmetries (shift symmetry, axion monodromy) that protect the potential. In exflation, the alpha_s tension would require either: (a) an f_0-independent contribution to lambda_CCM (from gravitational threshold corrections or Yukawa sector), (b) a modified KK threshold sum (convergence beyond L = 6), or (c) non-perturbative corrections to the CCM tree-level matching. None of these have been computed.

### II.4. The L_max = 7 Sign Reversal and UV Sensitivity

**Result**: LMAX7-PW-70 INFO. S_7 = 1.637, Delta_7 = -0.716 (sign reversal). r_7 = -1.654 (Gaussian). m_H range widens from [127, 128] to [127, 135] GeV. Classification: GEOMETRIC (PERMANENT finding).

The KK threshold sum S_inf = sum_L S_L, which enters the gauge coupling through 1/g_3^2(M_KK) = 1/g_3^2(tree) + S_inf, was previously extrapolated from L = 0 through L = 6 using Aitken acceleration, giving S_inf = 2.895 (S66). The L = 7 computation reveals that all L = 7 sectors have omega_min > Lambda = 2.048 M_KK, making ln(Lambda^2/omega_min^2) < 0. The Gaussian regulation factor suppresses but cannot prevent the sign flip. The sum is oscillatory, not monotone.

**Inflation comparison**: This is the exflation analog of the eta problem's UV sensitivity. In inflation, the eta problem (Burgess, Sec. 3.2) arises because the inflaton mass receives contributions from all scales up to the UV cutoff: Delta m_phi^2 ~ V/M_Pl^2, giving Delta eta ~ 1. The protection mechanism is symmetry (shift symmetry for axions, conformal coupling for Higgs inflation).

In the spectral action, the UV sensitivity manifests differently. The KK threshold sum is the spectral action's version of radiative corrections from heavy modes -- each L-shell contributes with a sign determined by whether omega_min(L) sits above or below the physical cutoff Lambda. The sign reversal at L = 7 is structurally analogous to a UV threshold correction that changes sign when new heavy states open up. Burgess's power-counting formula (eq. 3.14 of 1711.10592) shows that the loop expansion parameter is (H/(4pi M_Pl))^2 ~ 10^{-10} during inflation, making the derivative expansion extraordinarily well-controlled. In the spectral action, the analogous expansion parameter is (M_KK/Lambda)^{-1} ~ 0.5, which is NOT small -- the spectral action's heat kernel expansion is only marginally convergent at the physical cutoff (5-term HK deviation = 0.08% at Lambda = 2.048, NON-PERT-SA-70 PASS, but 3-term expansion fails everywhere).

The practical consequence: the Higgs mass prediction, previously quoted as m_H = 127.5 GeV (S66), now lies in [127, 135] GeV, reflecting oscillatory convergence uncertainty. The zero-free-parameter prediction remains within 8% of the observed 125.1 GeV, but the precision has degraded. This is a genuine methodological disadvantage relative to inflation, where the Higgs mass is a free parameter (or, in Higgs inflation, depends on the non-minimal coupling xi which is adjusted to match).

### II.5. WKB Breakdown and the Supersonic Transit

**Result**: CHIRP-PENUMBRA-70 FAIL. WKB median error = 84.2%. Adiabaticity parameter gamma > 1 for 93.4% of modes. Classification: GEOMETRIC (PERMANENT).

The Mukhanov-Sasaki equation v_k'' + (k^2 c_s^2 - z''/z) v_k = 0 governs scalar perturbation production in both inflation and exflation. In standard slow-roll inflation, WKB is the default method: modes evolve adiabatically (gamma << 1) until horizon crossing, where they "freeze out." The power spectrum is computed by matching WKB solutions across the turning point k^2 = z''/z.

In the exflation transit, WKB fails catastrophically because:

(a) The adiabaticity parameter gamma = |d(omega^2)/d eta| / (2 omega^2) exceeds 1 for 93.4% of modes. Only modes with k > 33,150 M_KK (16.8 times k_tach at fold) satisfy the adiabatic criterion.

(b) The transit duration is shorter than one Hubble time: dt_transit * H_fold = 0.663. The system is in the sudden (impulsive) regime, not the quasi-static regime.

(c) z''/z is always positive in the transit window -- there are no turning points. Every mode with k < 21,552 M_KK is tachyonic at SOME point. WKB requires exactly two turning points per mode.

This is the most fundamental methodological difference between inflation and exflation. In inflation, perturbation production is an adiabatic process (modes slowly cross the horizon). In exflation, it is an impulsive process (the horizon sweeps through k-space supersonically). The correct method is the sudden approximation or full Bogoliubov mode integration, not WKB.

**Physical consequence**: The consistency relation r = -8 n_t of single-field slow-roll inflation (Baumann, eq. (214)) is structurally inapplicable to the supersonic transit. The exflation transit produces perturbations through a fundamentally different kinematic process (Bogoliubov transformation across a sudden quench, not adiabatic horizon crossing), and the relationship between n_s, r, n_T, and f_NL takes the form of impulsive Bogoliubov kinematics (CONSISTENCY-FI-MAP-70). Five independent arguments establishing the inapplicability of r = 16 epsilon were consolidated in the VdD-Hawking workshop (S64).

### II.6. Observational Scorecard: Where Exflation Meets Data

**Result**: Across S69-S70, the observational scorecard shows a split verdict.

| Observable | FW vs LCDM | Method |
|:-----------|:-----------|:-------|
| Pantheon+ SNe (1701, full cov) | FW preferred, Delta chi^2 = -7.82 (2.80 sigma) | W2-A |
| f*sigma_8 (RSD, 9 bins, full cov) | FW preferred, Delta chi^2 = -0.609 | W2-B |
| D_M/r_d (BAO, 7 bins) | LCDM better, Delta chi^2 = +4.79 | S69 |
| Void size function | Both pass, diff ~ 1% | W2-E |
| Cluster mass function | LCDM better, Delta chi^2 ~ -2.5 | W4-A |
| ISW auto-power | FW/Quint = +6.7% (Boltzmann) | W2-C |
| sigma_8 tension | FW eases S_8 (2.1 -> 1.2 sigma) | W4-A |

**Inflation comparison**: Standard inflation (implemented via LCDM with n_s, r as outputs of a chosen potential) has six free parameters in the base model (Omega_b h^2, Omega_c h^2, H_0, tau, A_s, n_s), with r and running as additional parameters for extended models. The exflation framework predicts w_0 = -0.918 (from Zubarev/effacement), sigma_8 = 0.793 (from suppressed growth), and n_s = 0.9561 (from eps_H at the fold) with zero free cosmological parameters. Every observational match therefore carries more evidential weight (Bayes factor ~ prediction_range / posterior_width) than in a model with adjustable parameters.

However, the BAO tension (chi^2/dof = 2.076 for D_M/r_d, with LRG2 z = 0.706 pulling at -2.26 sigma) is the framework's weakest point. DESI DR3 will sharpen this decisively: if the LRG2 residual persists and sharpens to 4.2 sigma, the BAO channel overwhelms the growth-rate and SNe advantages (combined Delta chi^2 = +8.53, LCDM preferred at 2.92 sigma). The framework's observational fate is controlled by a single redshift bin.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| LEGGETT-VACUUM-70 | PASS | r_L = 0.617, eta = 1.56e-4 (sudden quench, 6412x below adiabatic) |
| F0-ALPHA-S-70 | FAIL | Anti-correlated: alpha_s = 0.118 at f_0 = 6.33, m_H = 125 at f_0 = 1.33 |
| Q-SOUND-70 | PASS | c_s^2 = 3.36e-4 (tree = 0 exact) |
| BELL-GGE-70 | PASS | S_min = 2.351 (all 8 modes violate Bell) |
| NON-PERT-SA-70 | PASS | 0.080% HK deviation at Lambda = 2.048 |
| PARAMETRIC-GGE-70 | FAIL | mu_phys < 10^{-16} (machine zero) |
| TRAPPED-ACOUSTIC-70 | PASS | theta_+ min = 585 > 0 (no trapped surfaces) |
| LMAX7-PW-70 | INFO | r_7 = -1.654 (sign reversal, PERMANENT) |
| FULL-COV-PANTHEON-70 | INFO | Delta chi^2 = -7.82 (2.80 sigma FW preferred) |
| FULL-COV-RSD-70 | INFO | Delta chi^2 = -0.609 (FW preferred, halved by cov) |
| CLASS-ISW-70 | PASS | ISW auto 6.72% FW/Quint at l = 2 |
| VOID-SIZE-70 | PASS | chi^2/dof = 0.935 (FW), diff ~ 1% |
| BERRY-DENNIS-GGE-70 | FAIL | chi^2/ndof = 2552 (5 k-shells insufficient) |
| SUPERLUMINAL-FRACTION-70 | FAIL | F_Leggett = 0.6% < 30% (multi-speed hierarchy) |
| DISCRETE-BERRY-DENNIS-70 | FAIL | chi^2/ndof = 329 (no convergence to BD) |
| CHIRP-PENUMBRA-70 | FAIL | WKB error = 84.2% (gamma > 1 for 93.4% modes) |
| DM-PAIR-DECAY-70 | PASS | tau_DM = 4.93e82 s (57 OOM margin vs FIRAS) |
| KURAMOTO-SYNC-70 | PASS | K_c = 1.052 < 3.60 (synchronized) |
| OFF-JENSEN-HESS-70 | INFO | All 35 VP eigenvalues positive (PERMANENT) |
| BCS-PROXIMITY-70 | INFO | Delta_ind = 0 exactly (SU(3) selection rule, PERMANENT) |

---

## IV. Structural Implications

### IV.1. Where Exflation Is Structurally Stronger Than Inflation

**(a) Parameter count.** The exflation framework operates with zero adjustable cosmological parameters. The spectral triple (M_4 x SU(3)_Jensen, D_K, gamma) determines: n_s = 0.9561 (from eps_H = 0.02163), r = 0.033 (from Bogoliubov kinematics), w_0 = -0.918 (from Zubarev effacement), sigma_8 = 0.793 (from growth suppression), c_s^2 = 0 (from algebraic q), and f_NL^equil = 0.853 (from BCS sound speed). Standard slow-roll inflation has at minimum one free function V(phi), requiring specification of the potential to predict n_s and r. Even the most constrained inflationary models (Starobinsky R^2, Higgs inflation) have at least one free parameter (M in R + R^2/(6M^2), or the non-minimal coupling xi).

**(b) Swampland compliance.** The transit traverses sub-Planckian distance in moduli space (Delta phi / M_Pl = 0.425, GEODESIC-MODULI-70), satisfying both the de Sitter Swampland Conjecture (c = 3.44 >> 1) and the Distance Conjecture (lambda_SDC = 0.447 ~ O(1)). Large-field inflation models (V ~ phi^p) require super-Planckian excursions (Lyth bound: Delta phi / M_Pl ~ (r/0.01)^{1/2}), which are in tension with the SDC. The Planck 2018 exclusion of V ~ phi^2 already disfavors the simplest large-field models. The spectral action, by construction, has no trans-Planckian problem because the modulus tau traverses a finite range [0, 0.19] in a compact space.

**(c) Reheating/thermalization.** Inflation requires a separate reheating mechanism (parametric resonance, perturbative decay, or instant preheating), and the reheating temperature T_RH is essentially a free parameter that sets the number of e-folds. Exflation produces its post-transit state (GGE relic of 59.8 quasiparticle pairs) in a single computation from the Kibble-Zurek mechanism. There is no separate reheating epoch. The GGE is a permanent non-thermal state (prethermalization timescale ~ 10^{580} t_universe from ADH, S65), maintained by Richardson-Gaudin integrability.

**(d) Dark matter candidate.** Inflation is silent on dark matter -- it provides no candidate. The exflation framework predicts Leggett-channel GGE quasiparticles with Z_2 stability (S67 PASS), lifetime tau_DM = 4.93 x 10^{82} s (DM-PAIR-DECAY-70 PASS, 65 OOM beyond age of universe), and spectral sharpness Q = 18.6 (S66 PASS). The DM candidate is a structural byproduct of the same BCS condensation that terminates the transit. The naive gravitational decay is suppressed by 114 OOM through five layered protections (Z_2, pair annihilation, epsilon^4, KK volume, phase space).

### IV.2. Where Inflation's Machinery Is More Developed

**(a) Full CMB power spectrum.** Inflation can compute C_l^{TT,TE,EE} from first principles via the Mukhanov-Sasaki equation through CAMB/CLASS (Baumann, Lecture 3). The exflation framework can predict n_s and r but has not yet computed the full transfer function from the spectral action to C_l. The S70 CLASS-ISW-70 computation uses CAMB with exflation's w_0 and c_s^2 as inputs but does not derive these from a first-principles Boltzmann solver coupled to the spectral action dynamics. The WKB failure (CHIRP-PENUMBRA-70) means the standard inflationary pipeline (mode evolution through horizon crossing) cannot be applied -- a dedicated Bogoliubov solver must be built.

**(b) Tensor modes.** Inflation's consistency relation r = -8 n_t provides a sharp prediction for the tensor spectrum. Exflation has r = 0.033 from Bogoliubov kinematics (S64), below the BICEP/Keck bound of 0.036, but the n_T prediction depends on the scheme-dependent eps_H (CONSISTENCY-FI-MAP-70: r is SD, with sign flip between cutoff and zeta). The framework lacks a first-principles computation of the tensor power spectrum from the 12D Weyl tensor (NP scalars, W5-C, show bw+/-2 = 3.82% in the dynamic case, confirming tensor production, but the mapping to 4D gravitational wave spectrum is not yet done).

**(c) Non-Gaussianity shapes.** Maldacena's theorem (single-field slow-roll: f_NL ~ O(epsilon, eta)) provides a sharp prediction for inflation. The Cheung et al. EFT systematically parametrizes departures from Gaussianity through the operator hierarchy. Exflation predicts f_NL^equil = 0.853 and f_NL^folded = 0.129 (S69), but the full bispectrum shape function B(k_1, k_2, k_3) has not been computed from the Bogoliubov coefficients of the impulsive transit. The equilateral and folded components are extracted from c_BLV, but the complete shape decomposition -- required for comparison with Planck bispectrum constraints -- remains uncomputed.

**(d) Model flexibility.** The EFT of inflation (Cheung et al.) provides a systematic parametrization of ALL single-field models through operator coefficients {M_2, M_3, bar{M}_1, ...}. This flexibility allows inflation to accommodate a wide range of observations. Exflation has no such flexibility -- the spectral triple is fixed, and the predictions follow. This is a strength when predictions match (fewer parameters = higher Bayes factor) but a weakness when they do not (the alpha_s tension has no obvious resolution within the current framework).

### IV.3. Constraint Map Updates

| Region | Prior S69 State | S70 State | Mechanism |
|:-------|:----------------|:----------|:----------|
| c_s^2 = 0 for DE | Assumed (from q-theory analogy) | DERIVED (Q-SOUND-70 PASS) | Algebraic g_K dependence in SA |
| Parametric resonance | Untested | CLOSED (W1-H FAIL) | Overdamped, off-tongue, weak coupling |
| WKB for power spectrum | Assumed usable | CLOSED (W4-B FAIL, PERMANENT) | Mach 54.73, gamma > 1 for 93.4% |
| alpha_s normalization | f_0 untested | Anti-correlated, no joint window (W1-B FAIL) | Single g_3^2(M_KK) controls both |
| KK threshold convergence | Monotone (S66) | Oscillatory (W1-J, PERMANENT) | L = 7 sectors above Lambda |
| Leggett vacuum | Untested | Sudden quench (W1-A PASS, r_L = 0.617) | eta = 1.56e-4, KZ maximally excited |
| BCS shell completeness | Assumed 8/992 | EXACT (W4-I, selection rule) | Self-conjugate under SU(3) |
| 35D fold stability | 36D tested (S69) | All 35 VP eigenvalues positive (W4-G, PERMANENT) | Jensen = genuine local minimum |
| Berry-Dennis universality | Expected on CG(24) | FAILS (W3-A/E) | 5 k-shells insufficient for continuous limit |
| Leggett DM stability | S67 Z_2 rule | PASS vs FIRAS/PIXIE (W5-A, 57 OOM) | 10^{82} s lifetime |

---

## V. Forward Projection

### V.1. The Three Decisive Next Computations

**(1) SPECTRAL-ZETA-THRESHOLD**: The L_max = 7 sign reversal (PERMANENT) means the Aitken extrapolation is unreliable. The threshold sum must be computed as a spectral zeta function without PW truncation, bypassing the oscillatory convergence. This directly controls m_H and alpha_s(M_Z) predictions. GATE: S_inf in [2.0, 2.9] (bracketed by oscillation). This is the highest-EVOI computation for the particle physics sector.

**(2) INTER-SITE-ENTANGLE-71**: The SU(1,1) compound squeeze (W2-D) yields +1.79 OOM correction to A_s, but the spatial squeeze parameter r_spatial has a factor-of-2 ambiguity (arctanh route: 1.098 vs Josephson route: 0.551). Computing the inter-site entanglement entropy and comparing to 2 r_spatial^2 / ln(2) resolves whether the full SU(1,1) interpretation applies. GATE: agreement within 20%.

**(3) FULL-BOGOLIUBOV-SPECTRUM**: The WKB FAIL (PERMANENT) mandates building a dedicated Bogoliubov mode integration solver for the supersonic transit. This would produce the first full P(k) from the spectral action, enabling direct comparison with the Planck C_l data rather than relying on n_s and r as proxy observables. The sudden approximation provides the leading-order result; the full integration captures corrections at k ~ k_tach.

### V.2. The DESI DR3 Fork

DESI-DR3-UPDATE-70 identifies the framework's observational fate as controlled by LRG2 z = 0.706:
- If the -2.26 sigma pull resolves (noise): FW survives with net preference from SNe + RSD
- If it persists and sharpens to 4.2 sigma: BAO overwhelms growth-rate advantage

This is an external constraint with no framework-internal resolution -- the data will decide.

### V.3. The alpha_s Resolution Path

The F0-ALPHA-S-70 FAIL identifies three mathematical routes to decoupling m_H from alpha_s:
- Modified threshold sum (SPECTRAL-ZETA-THRESHOLD above)
- f_0-independent lambda_CCM contribution (requires gravitational threshold corrections or Yukawa sector)
- Non-perturbative CCM corrections

The first is computable in the next session. The second and third require new theoretical development.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | c_s^2 = 0 derived from algebraic q | GEOMETRIC | PASS (PERMANENT) | Cleanest discriminant vs quintessence; ISW prediction confirmed by Boltzmann |
| 2 | Parametric resonance excluded | PHONONIC | FAIL (PERMANENT) | GGE formation is single-pass KZ, not oscillatory amplification |
| 3 | alpha_s-m_H anti-correlation | PARTICLE/GEOMETRIC | FAIL | Structural: single g_3^2 couples both; no f_0 rescues both |
| 4 | L = 7 sign reversal | GEOMETRIC | INFO (PERMANENT) | Oscillatory convergence; m_H widened to [127, 135] GeV |
| 5 | WKB inapplicable to transit | GEOMETRIC | FAIL (PERMANENT) | Sudden approximation mandatory; inflation pipeline inapplicable |
| 6 | Leggett vacuum excited | PHONONIC | PASS | r_L = 0.617; A_s gap 0.485 -> 0.267 OOM |
| 7 | Pantheon+ full cov strengthens FW | PHONONIC | INFO | Delta chi^2 = -7.82 (2.80 sigma) |
| 8 | ISW Boltzmann confirms tracking | PHONONIC | PASS | 6.7% ISW auto, Limber overpredicted 1.9x |
| 9 | SU(1,1) compound squeeze | PHONONIC | INFO | +1.79 OOM (overclosure tension constrains r_spatial) |
| 10 | 35D Hessian all positive | GEOMETRIC | INFO (PERMANENT) | Jensen fold is genuine local minimum |
| 11 | BCS shell self-conjugate | GEOMETRIC | INFO (PERMANENT) | 8/992 truncation is EXACT by representation theory |
| 12 | Leggett DM stable vs FIRAS | PHONONIC | PASS | 57 OOM safety margin; 65 OOM beyond age of universe |
| 13 | Berry-Dennis fails on CG(24) | GEOMETRIC | FAIL | Finite-size: 5 k-shells insufficient; not physics failure |
| 14 | Non-pert SA converges at Lambda | GEOMETRIC | PASS | 0.08% at Lambda = 2.048 (5-term HK) |
| 15 | Trapped surfaces absent | GEOMETRIC | PASS | theta_+ > 585 everywhere; white hole topology |
| 16 | alpha_s = 0: functional-independent | GEOMETRIC | INFO (PERMANENT) | Strongest FI prediction; falsifiable by CMB-S4 |
| 17 | eps_H sensitivity to spectral functional | GEOMETRIC | INFO | Planck-compatible window: alpha in [0.67, 1.10] |
| 18 | DESI DR3 decision tree | NON-PHONONIC | INFO | LRG2 z = 0.706 is sole bottleneck |
