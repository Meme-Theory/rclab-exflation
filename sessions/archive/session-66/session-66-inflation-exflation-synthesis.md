# Session 66: Inflation-Exflation Deep Synthesis

**Date**: 2026-04-04
**Author**: Katie Mack (Cosmic Bridge Agent)
**Source Documents**: All 16 papers in `researchers/Inflation/`, plus S66 working paper, agent memory, phononic framing rules
**Framing**: The 114 OOM between spectral action fold energy and today's CC is not a "gap to close" -- it is the observed consequence of the transit (exflation). Standard LCDM carries an equivalent ~120 OOM between inflaton V and today's CC and universally accepts it as "inflation happened." The Volovik relaxation landing at 0.01 OOM from observation is the thermodynamic endpoint, not a gap-closing mechanism.

---

## I. The Master Correspondence Table

The exflation transit is not inflation viewed through a different lens. It is the fundamental process; inflation is the effective field theory that emerges when one forgets the substrate and projects onto a 4D scalar field language. Every inflation concept has a substrate-level origin. The table below maps them exhaustively.

### I.A. Dynamical Variables

| Inflation Concept | Mathematical Form (Inflation) | Exflation Counterpart | Mathematical Form (Exflation) | Source |
|:---|:---|:---|:---|:---|
| Inflaton field phi | Fundamental scalar on M^4 | Jensen deformation parameter tau | Geometric parameter of spectral triple, NOT a quantum field | Baumann Eq. (61) vs spectral action S(tau) |
| Inflaton potential V(phi) | Free function, model-dependent | Spectral action S(tau) = Tr f(D_K^2/Lambda^2) | Determined uniquely by D_K spectrum; zero free parameters | Baumann Eq. (74)-(75) vs S66 W1-B |
| Slow-roll parameter eps | eps = (M_Pl^2/2)(V'/V)^2 << 1 | Transit speed parameter | eps_H = (dS/dtau)^2 / (2 S^2), eps_H = 0.022 at fold | Baumann Eq. (70) vs S64 TENSOR-BURST-64 |
| Slow-roll parameter eta | eta = M_Pl^2 V''/V << 1 | Spectral curvature at fold | eta_H = d^2S/dtau^2 / S, eta_H = 0.96 at fold -- NOT small | Baumann Eq. (75) vs S64 |
| Field velocity dphi/dt | dphi/dt = -V'/(3H) in slow-roll | Spectral action gradient | dS/dtau = +58,673 at fold (driving force for transit) | Lyth-Riotto Eq. (35) |
| e-fold number N | N = integral(V/(M_Pl^2 V') dphi), N >= 60 | Physical transit e-folds | N_e = 3.73e-3 (supersonic transit, 5 methods agree) | Baumann Eq. (83) vs S64 |
| Field excursion Delta phi | Lyth bound: Delta phi / M_Pl ~ sqrt(r/0.01) | tau excursion through fold | Delta tau ~ 0.05 across van Hove fold; NO Lyth bound applies | Baumann Eq. (221) |
| Inflaton mass m_phi | Model-dependent; eta problem: m_phi ~ H generically | Spectral gap at fold | m_B2(fold) = 0.723 M_KK; determined by D_K eigenvalue crossing | Lyth-Riotto Sec. 5 |

### I.B. Perturbation Generation

| Inflation Concept | Mathematical Form | Exflation Counterpart | Mathematical Form | Source |
|:---|:---|:---|:---|:---|
| Quantum vacuum fluctuations | Bunch-Davies vacuum: v_k -> e^{-ik tau}/sqrt(2k) | Bogoliubov pair creation | Parker mechanism at supersonic transit: P_exc = 1.000, 59.8 pairs | Baumann Eq. (192) vs S52 |
| Mukhanov equation | v_k'' + (k^2 - z''/z)v_k = 0 | GGE mode equation | Bogoliubov-de Gennes equation for quasiparticle excitations of D_K | Baumann Eq. (185), Brandenberger Sec. 3 |
| Horizon crossing k = aH | Modes freeze when wavelength exceeds Hubble radius | Acoustic white hole boundary | Causal disconnection at Mach = 13.8; pre/post transit causally severed | Baumann Sec. 2 |
| Curvature perturbation R | R = Psi + (H/dphi) delta phi, conserved superhorizon | GGE acoustic excitations | Interference pattern of post-transit quasiparticle pairs, non-thermal | Maldacena Eq. (2.8) |
| Scalar power spectrum | Delta_s^2 = H^2/(8 pi^2 M_Pl^2 eps) at k=aH | GGE occupation spectrum | From Bogoliubov coefficients |beta_k|^2; A_s gap = 3.15 OOM (Route A) | Baumann Eq. (222) vs S66 W1-C |
| Tensor power spectrum | Delta_t^2 = 2H^2/(pi^2 M_Pl^2) | Second-order tensor from transit | r = 0.024 at CMB scale (BICEP/Keck PASS); H2 theorem kills 1st order | Baumann Eq. (223) vs S66 TENSOR-TRANSFER-66 |
| Spectral index n_s | n_s - 1 = 2 eta - 6 eps (slow-roll) | Spectral geometry tilt | n_s = 0.9590 (BCS + one-loop, zero free parameters) | Baumann Eq. (236) vs S65 |
| Consistency relation r = -8 n_t | Single-field slow-roll identity | INAPPLICABLE | Transit is impulsive (Mach 13.8), not quasi-static; 5 independent proofs | Baumann Eq. (239); VdD-Hawking workshop |
| Running alpha_s | alpha_s = 16 eps eta - 24 eps^2 - 2 xi^2 | Spectral geometry running | alpha_s = -0.038 at L_max=4 (5.0-sigma FAIL), intrinsic to D_K spectrum | Lyth-Riotto Sec. 3.2.2 vs S66 |

### I.C. Energy Transfer and Late-Time Physics

| Inflation Concept | Mathematical Form | Exflation Counterpart | Mathematical Form | Source |
|:---|:---|:---|:---|:---|
| Reheating / preheating | Parametric resonance: chi_k'' + (A_k - 2q cos 2z)chi_k = 0 | GGE relic formation | Parker pair creation at fold; 59.8 pairs, non-thermal (GGE) | Kofman-Linde-Starobinsky Eq. (23) |
| Inflaton oscillation decay | phi(t) = Phi(t) sin(mt), Phi ~ 1/t | NO oscillation -- single transit | Supersonic passage through fold; impulsive, irreversible | Kofman-Linde-Starobinsky Eq. (4) |
| Thermalization | Produced particles rescatter -> thermal bath | Ordered Veil -- NO thermalization | GGE integrability conserves N_pair; Richardson-Gaudin integrable | Kofman-Linde-Starobinsky Sec. VIII |
| Reheating temperature T_r | T_r ~ 0.2 sqrt(Gamma M_Pl) | Transit energy scale T_init | T_init = 8.32 x 10^15 GeV (from fold spectral action) | Kofman-Linde-Starobinsky Eq. (19) |
| Cosmological constant today | Lambda_obs ~ 10^{-120} M_Pl^4 (accepted as given) | Volovik relaxation endpoint | rho_vac ~ H^2 M_Pl^2, landing at 0.01 OOM from obs (S66 DILUTION-CC PASS) | Weinberg Sec. 1 vs S66 W1-A |
| Dark energy w = -1 | Lambda CDM: pure CC, no dynamics | Effacement residual + Josephson | w_0 = -0.918 from combined GGE + Josephson channels | Padmanabhan Eq. (7) vs S65 |
| Dark matter (CDM) | Cold, collisionless, unknown particle | Leggett-channel GGE quasiparticle | CPT-neutral, non-annihilating; Omega_DM h^2 = 0.120 (Leggett-only) | S66 Z-EQ-CHECK-66 |
| EFT operator hierarchy | M_2, M_3, M-bar operators in unitary gauge | Spectral action moment hierarchy | a_0 (CC), a_2 (gravity), a_4 (Yang-Mills): Seeley-DeWitt coefficients | Cheung et al. Eq. (10) |
| Speed of sound c_s | c_s^{-2} = 1 - 2M_2^4/(M_Pl^2 dH/dt) | Fabric sound speed c_BLV | c_BLV = 0.485, Mach = 13.8 at transit | Cheung et al. Eq. (38) vs S64 |
| Goldstone boson pi | Broken time-diff mode: zeta = -H pi | Phononic excitation of substrate | Relay pattern propagating through gauge connection between fibers | Cheung et al. Eq. (30) |

### I.D. UV Sensitivity

| Inflation Problem | Nature | Exflation Status | Source |
|:---|:---|:---|:---|
| Eta problem: m_phi^2 ~ H^2 generically | UV sensitivity of inflaton mass to Planck-suppressed operators | ABSENT: tau is geometric, not a quantum field; no radiative mass correction | Lyth-Riotto Sec. 5; Burgess Sec. 3 |
| Trans-Planckian problem | Modes start sub-Planckian if inflation lasted long enough | ABSENT: spectral triple provides natural UV cutoff; no sub-Planckian wavelengths | Brandenberger Sec. 5 |
| CC radiative instability | Each loop order requires retuning to 10^{-60} | STRUCTURAL: a_0, a_2 are different moments of same D_K; Volovik relaxation is functional-independent | Padilla Sec. 2; Weinberg Sec. 1 |
| Landscape / discretuum | ~10^{100} vacua needed for statistical CC cancellation | NO LANDSCAPE: single internal geometry (SU(3) fiber); CC from one spectral triple | Bousso-Polchinski Sec. 2.4 |

---

## II. Paper-by-Paper Analysis

### II.1. Baumann -- TASI Lectures on Inflation [01]

**What inflation math this paper develops**: The complete slow-roll perturbation formalism from first principles. The Mukhanov-Sasaki equation v_k'' + (k^2 - z''/z)v_k = 0, the scalar power spectrum Delta_s^2 = H^2/(8 pi^2 M_Pl^2 eps), the tensor spectrum Delta_t^2 = 2H^2/(pi^2 M_Pl^2), spectral indices n_s - 1 = 2 eta - 6 eps and n_t = -2 eps, the consistency relation r = -8 n_t, and the Lyth bound Delta phi / M_Pl ~ sqrt(r/0.01).

**Exflation counterpart**: The Mukhanov equation maps to the Bogoliubov-de Gennes equation for GGE excitations, with z''/z replaced by the time-dependent effective mass from the spectral gap evolution at the fold. The critical difference: Baumann's Bunch-Davies vacuum initial condition (modes start in Minkowski ground state) corresponds to choosing the pre-transit state of D_K as the initial "vacuum." But the transit is supersonic (Mach 13.8), meaning the WKB approximation underlying the Bunch-Davies choice breaks down catastrophically at the fold -- the adiabaticity parameter changes by O(1) over a single oscillation period. This is exactly the regime where Bogoliubov pair creation is maximal (P_exc = 1.000), and the resulting GGE excitation spectrum is fundamentally different from the gentle slow-roll amplification.

**Tools we should adopt**: Baumann's systematic treatment of the transfer function (Lecture 3, eq. for C_l^XY as integrals over P(k) with line-of-sight projection) should be applied to the GGE acoustic spectrum. The framework has NOT yet computed the angular power spectrum C_l from the GGE excitation pattern. This is a missing computation.

**Key equation mapping**: Baumann Eq. (222) -- the scalar amplitude Delta_s^2 = H^2/(8 pi^2 M_Pl^2 eps) -- maps to the framework's Route B formula A_s = (delta rho / rho_0)^2 from Bogoliubov variance. The 3.15 OOM gap (S66 W1-C) arises because the Garriga-Mukhanov mapping assumes slow-roll mode functions, while the actual transit produces a different occupation spectrum. The transfer function is WHERE the gap lives.

### II.2. Lyth & Riotto -- Particle Physics Models of Inflation [02]

**What inflation math this paper develops**: Systematic classification of inflation models by potential shape, with COBE normalizations and n_s predictions for each. The eta problem in supergravity: generic F-term gives m_phi^2 ~ H^2, violating slow-roll. Hybrid inflation as the sub-Planckian escape route.

**Exflation counterpart**: The eta problem is the central illness of inflation model-building: any scalar field coupled to gravity generically picks up a mass of order H from Planck-suppressed dimension-6 operators. The exflation framework sidesteps this entirely because the tau parameter is NOT a quantum field -- it is a geometric deformation parameter of the spectral triple. There is no radiative correction to its "mass" because it does not propagate. The spectral action S(tau) is computed exactly from the D_K eigenvalue spectrum at each tau value, with no perturbative expansion in tau.

**Tools we should adopt**: Lyth-Riotto's running formula alpha_s = -2 eps eta - 24 eps^2 - 2 xi^2 (where xi^2 = M_Pl^4 V'V'''/V^2) should be compared to the framework's alpha_s = -0.038 (S66 RUNNING-NS-66 FAIL). In slow-roll, alpha_s ~ O(eps^2) ~ 10^{-4}, but the framework predicts alpha_s two orders of magnitude larger. This is a discriminant: if CMB-S4 measures |alpha_s| > 0.01, slow-roll inflation is excluded but exflation survives. If alpha_s is confirmed consistent with zero, the framework's L_max=4 value must be an artifact of truncation (and the L->infinity Richardson extrapolation giving -0.037 would need to be wrong).

**Key equation mapping**: Lyth-Riotto Eq. (45) -- V^{1/4}/eps^{1/4} = 6.7 x 10^16 GeV -- constrains the inflation energy scale. The exflation analog is T_init = 8.32 x 10^15 GeV from the fold spectral action. These are the same order of magnitude (within a factor of 8), confirming the energy scales match.

### II.3. Maldacena -- Non-Gaussianity [03]

**What inflation math this paper develops**: The three-point function of primordial perturbations in single-field slow-roll. The ADM decomposition, third-order action in zeta and gamma, the in-in formalism for computing correlators, and the Maldacena consistency relation: f_NL^local = (5/12)(1 - n_s) for single-field slow-roll, giving f_NL ~ O(eps, eta) ~ 0.01.

**Exflation counterpart**: The exflation transit is NOT a single-field slow-roll scenario. The GGE relic contains 59.8 quasiparticle pairs across multiple branches of the D_K spectrum. This is inherently a multi-field situation (in the inflation language), meaning the Maldacena consistency relation is generically violated. The non-Gaussianity from GGE pair creation could be orders of magnitude larger than the slow-roll value.

**Tools we should adopt -- CRITICAL**: Maldacena's in-in formalism (computing expectation values of field operators using the time-evolution operator and its adjoint) is the correct tool for computing the bispectrum from GGE excitations. The framework has not done this computation. The key adaption: replace Maldacena's cubic interaction Hamiltonian (which comes from expanding V(phi) to third order) with the third-order spectral action S_3(tau) evaluated at the fold. The transit is impulsive, so the in-in integral will be dominated by a narrow tau interval around the fold, qualitatively different from the slow-roll case where the integral extends over many e-folds.

**Specific equation**: Maldacena Eq. (2.12) -- the second-order action S_2 = (1/2) integral (dphi^2/drho^2) [e^{3rho} dzeta^2 - e^rho (partial zeta)^2] -- is suppressed by slow-roll because zeta is pure gauge in exact de Sitter. In exflation, zeta gains dynamics from the spectral reorganization at the fold, not from a slowly varying H. The suppression factor is NOT eps_H but rather the Bogoliubov coefficient |beta_k|^2, which is O(1) at the fold. This could explain the A_s normalization gap: if the mode-to-zeta conversion is not suppressed by eps, the raw amplitude is larger.

### II.4. Brandenberger -- Perturbation Theory Lectures [04]

**What inflation math this paper develops**: Classical and quantum cosmological perturbation theory from Newtonian first principles through full GR. The Jeans instability, scale-invariant spectra, the trans-Planckian problem, and back-reaction of long-wavelength fluctuations.

**Exflation counterpart**: Brandenberger's Jeans instability analysis (modes with k > k_J oscillate, k < k_J collapse) maps directly onto the post-transit GGE acoustic spectrum. The Jeans wavenumber k_J = (4 pi G rho_0 / c_s^2)^{1/2} evaluated with the BLV fabric sound speed c_BLV = 0.485 and the post-transit energy density gives the scale separating acoustic oscillations from gravitational collapse in the GGE relic.

**Tools we should adopt**: Brandenberger's discussion of back-reaction (Sec. 6) -- that long-wavelength fluctuations generate an effective NEGATIVE cosmological constant contribution -- is directly relevant. In the exflation framework, the GGE relic's long-wavelength modes would contribute a back-reaction term that could partially cancel the spectral action's a_0 vacuum energy. This has NOT been computed. The back-reaction energy-momentum tensor from the GGE occupation spectrum could provide a physical mechanism for the CC reduction that is currently attributed entirely to Volovik relaxation.

**Trans-Planckian resolution**: Brandenberger identifies the trans-Planckian problem (modes observed in CMB had sub-Planckian wavelengths early in inflation). The spectral triple resolves this by construction: the Dirac operator D_K has a discrete spectrum with maximum eigenvalue Lambda_max at any finite L_max truncation. There are no modes with wavelengths below 1/Lambda_max. The modified dispersion relation approach Brandenberger discusses (where omega(k) deviates from k at high k) is automatically realized in the spectral action, where the cutoff function f(x) = sqrt(x) modifies the contribution of high-eigenvalue modes.

### II.5. Martin, Ringeval, Vennin -- Encyclopaedia Inflationaris [05]

**What inflation math this paper develops**: Systematic computation of n_s, r, and alpha_s for 74 single-field inflationary potentials. Bayesian model comparison against Planck data. The reheating temperature introduces uncertainty in N_* and hence in observational predictions.

**Exflation counterpart**: The encyclopaedia's main result -- that Planck data favor concave potentials (V'' < 0) -- is structurally interesting for exflation. The spectral action S(tau) near the fold has a MAXIMUM (fold SA Hessian: 0+, 3-; S60), meaning S''(tau) < 0 at the fold. This is exactly the "concave potential" class. However, the exflation transit is NOT slow-roll (eta_H = 0.96 ~ O(1), far from the << 1 regime), so the mapping is formal rather than dynamical.

**Tools we should adopt**: The Bayesian model comparison machinery is directly applicable. The 74 models each predict a point in (n_s, r, alpha_s) space as a function of N_*. The exflation framework predicts a FIXED point: (n_s = 0.9590, r = 0.024, alpha_s = -0.038) with zero free parameters. A proper Bayesian comparison of the exflation point against the 74-model prior would yield a definitive likelihood ratio. This has NOT been done.

**Key equation mapping**: The Starobinsky prediction n_s ~ 1 - 2/N_* with N_* ~ 55 gives n_s ~ 0.964, close to Planck. The exflation prediction n_s = 0.9590 differs from Starobinsky by 0.005, which is distinguishable by CMB-S4 (projected sigma(n_s) ~ 0.002). A precision measurement of n_s could separate exflation from the Starobinsky class.

### II.6. Kofman, Linde, Starobinsky -- Reheating [06]

**What inflation math this paper develops**: Preheating via parametric resonance after inflation ends. The Mathieu equation for chi fluctuations coupled to the oscillating inflaton. Broad resonance (q >> 1), stochastic resonance in expanding universe, backreaction, and rescattering.

**Exflation counterpart**: This is the closest structural parallel in the entire inflation library. The reheating process (converting inflaton coherent energy into particles) maps onto GGE relic formation (converting transit kinetic energy into quasiparticle pairs). But the differences are fundamental:

1. **Inflation**: The inflaton OSCILLATES around V_min, producing repeated kicks to chi. Each zero-crossing creates particles (broad resonance). Production is stochastic because expansion randomizes phases.
2. **Exflation**: The substrate passes through the fold ONCE. There is no oscillation, no repeated kicks. The pair creation happens in a single impulsive event. The Bogoliubov coefficient is |beta|^2 = sinh^2(pi gamma) where gamma is the Landau-Zener parameter.

The Kofman-Linde-Starobinsky occupation number n_k (Eq. 25) as an adiabatic invariant maps directly onto the GGE Bogoliubov occupation numbers. The key insight: in both cases, the proper variable is the occupation number, not the field amplitude. The framework already uses this (GGE is described by {n_k}).

**Tools we should adopt -- CRITICAL**: The Mathieu equation analysis (instability bands, Floquet exponents) could be applied to the post-transit era. If the substrate undergoes ANY oscillation or ringing after the transit, there will be secondary parametric resonance amplifying specific k-modes of the GGE relic. The framework has NOT checked for post-transit ringing of tau. The spectral action S(tau) is a maximum at the fold, so tau settles quickly (10^{-47} yr per S65), but ANY ringing during that settling could parametrically amplify perturbations. This is the exflation analog of preheating, and it might affect the A_s normalization.

**Key equation**: Kofman-Linde-Starobinsky Eq. (27) -- the resonance condition q^2 m >> H -- translates to the exflation question: is the spectral action curvature d^2S/dtau^2 at the fold large enough that post-transit oscillations of tau couple resonantly to GGE modes? Given d^2S/dtau^2 ~ 10^5 (S60 Hessian) and H ~ T_init^2/M_Pl, this should be computed.

### II.7. Cheung et al. -- EFT of Inflation [07]

**What inflation math this paper develops**: The most general effective field theory for fluctuations around a quasi-de Sitter background, in unitary gauge. The building blocks: polynomials of g^{00}, extrinsic curvature K_{mu nu}, and the Riemann tensor. The Goldstone boson pi (from Stuckelberg trick) with speed of sound c_s, and the forced connection between c_s < 1 and equilateral non-Gaussianity f_NL ~ 1/c_s^2.

**Exflation counterpart -- THIS IS THE KEY PAPER**: The EFT of inflation organizes all single-field models by their operator content. The spectral action's Seeley-DeWitt expansion IS such an operator expansion:
- a_0 corresponds to Lambda(t) in Cheung et al. Eq. (10)
- a_2 corresponds to (M_Pl^2/2) R
- a_4 corresponds to the R^2 + R_{mu nu} R^{mu nu} operators
- Higher a_{2k} correspond to higher-derivative operators

The CRUCIAL identification: Cheung et al. show that the background evolution H(t) fixes ONLY the first two operators (c(t) and Lambda(t)), while ALL higher operators are free parameters encoding "the theory of perturbations." In the spectral action framework, ALL operators (a_0, a_2, a_4, ...) are determined by a SINGLE input -- the D_K spectrum. There are NO free parameters for the perturbation sector. This is the deepest difference between exflation and inflation: the spectral triple uniquely determines both the background AND the perturbations.

**Tools we should adopt -- CRITICAL**: The speed of sound formula c_s^{-2} = 1 - 2M_2^4/(M_Pl^2 dH/dt) (Eq. 38) maps onto the framework's four-speed hierarchy. The EFT identification is:

M_2^4 ~ (a_4 - a_4^{slow-roll contribution}), encoding the deviation of the spectral action's quartic term from the pure slow-roll value. The framework's c_BLV = 0.485 should be derivable from this identification, giving M_2^4/M_Pl^2 |dH/dt| = (1 - c_BLV^2)/(2 c_BLV^2) ~ 1.63. This has NOT been checked.

The non-Gaussianity prediction f_NL^equil ~ 85/324 * 1/c_s^2 evaluated at c_BLV = 0.485 gives f_NL^equil ~ 1.12. This is within Planck bounds (f_NL^equil = -26 +/- 47) and would be a testable prediction for future surveys. This has NOT been computed.

**Key equation mapping**: Cheung et al. Eq. (41) gives the general spectral tilt: n_s - 1 = 4 dH/dt / H^2 - dH-double-dot / (dH/dt * H) - dc_s/dt / (c_s * H). In slow-roll the last two terms are negligible, but in exflation where the transit is impulsive, dc_s/dt / (c_s H) could be O(1), providing a CORRECTION to n_s beyond the simple 1 - 2 eps_H formula. This additional term from the time-variation of c_s has not been evaluated for the exflation transit.

### II.8. Senatore & Zaldarriaga -- Multifield EFT [08]

**What inflation math this paper develops**: Extension of the EFT of inflation to include additional light scalar fields sigma_I (Goldstone bosons of broken global symmetries or SUSY-protected). The multifield operator enumeration, new non-Gaussian shapes, and the finding that approximate symmetries can suppress the bispectrum while leaving the trispectrum large.

**Exflation counterpart**: The GGE relic contains multiple quasi-particle branches (acoustic, optical, Leggett mode). In the EFT language, these are the sigma_I fields. The SU(3) fiber's non-Abelian structure means Section 3.2 (non-Abelian Goldstone coset construction G/H) is directly applicable: the quasiparticle excitations of the Jensen-deformed SU(3) fiber transform under the residual symmetry group after the transit, and their interactions are constrained by the coset G/H structure.

**Tools we should adopt**: The conversion mechanism (Sec. 4) -- how sigma fluctuations become curvature perturbations -- is the missing piece of the exflation amplitude calculation. The framework's GGE excitations must be converted into curvature perturbations via the delta-N formalism or its analog. The framework currently uses the Garriga-Mukhanov relation (which assumes single-field), and this mismatch could explain part of the 3.15 OOM A_s gap.

The paper's Eq. (61) -- zeta(x) = -H pi(x) + (partial zeta / partial sigma_I) sigma_I + ... -- shows that multifield contributions can ENHANCE A_s above the single-field value. If the GGE's Leggett and optical modes contribute to zeta through the second term, the raw amplitude could be increased, potentially closing the A_s gap.

### II.9. Lopez Nacir et al. -- Dissipative EFT [09]

**What inflation math this paper develops**: Extension of inflation EFT to include dissipative effects (friction and noise from additional degrees of freedom). The Langevin equation for pi, the fluctuation-dissipation relation, noise-dominated power spectrum, and the main result: |f_NL| ~ gamma / (c_s^2 H) >> 1 for strong dissipation.

**Exflation counterpart**: The exflation transit IS a strongly dissipative event. The Parker pair creation at the fold (P_exc = 1.000) means ALL available modes are excited -- the "friction" from pair production is maximal. The acoustic impedance mismatch Gamma = 0.99970 at the fold boundary is the dissipation coefficient. In the notation of this paper:
- gamma (friction coefficient) <--> Gamma_transit ~ M_KK * (impedance mismatch factor)
- c_s <--> c_BLV = 0.485
- H <--> H_fold ~ T_init^2/M_Pl

**Tools we should adopt -- HIGHEST PRIORITY**: The noise-dominated power spectrum formula (Eq. 43-44) should be evaluated for the exflation transit. If the transit is strongly dissipative (gamma >> H, which is likely since M_KK >> H), then the Bunch-Davies (homogeneous) contribution to the power spectrum is exponentially suppressed, and the spectrum is dominated by the noise from pair creation. This would give a DIFFERENT normalization formula for A_s than the standard Garriga-Mukhanov relation -- potentially resolving the 3.15 OOM gap.

The main result f_NL ~ gamma / (c_s^2 H) gives a concrete non-Gaussianity prediction. With gamma ~ M_KK ~ 10^17 GeV and c_s = 0.485 and H_fold ~ 10^14 GeV, this gives f_NL ~ 10^3 / 0.235 ~ 4000 -- far above current bounds. However, this applies only if the transit lasts many Hubble times; for an impulsive transit (N_e = 3.73e-3), the effective gamma is reduced by the duty cycle.

**Specific computation**: Evaluate the effective dissipation parameter gamma_eff = gamma * (Delta t_transit / H^{-1}) = gamma * N_e / (2 pi). If gamma = M_KK = 4.33 x 10^17 GeV and N_e = 3.73e-3, then gamma_eff ~ M_KK * 6e-4 ~ 2.6 x 10^14 GeV, comparable to H_fold. The dissipative correction to A_s would then be O(1), not O(10^3).

### II.10. Burgess -- EFT and Inflation [10]

**What inflation math this paper develops**: The GREFT (General Relativity EFT) framework. GR as the leading term in a derivative expansion. The semiclassical expansion parameter (H / 4 pi M_Pl)^2 ~ 10^{-10}. The result that trans-Planckian field values do NOT invalidate the EFT. Power counting for scalar-tensor theories in inflationary backgrounds.

**Exflation counterpart**: The GREFT Lagrangian (Eq. 3.4) is structurally identical to the spectral action's Seeley-DeWitt expansion:

| GREFT term | Spectral action moment | Coefficient source |
|:---|:---|:---|
| lambda (cosmological constant) | a_0 * Lambda^4 | Sum over D_K eigenvalues (zeroth moment) |
| (M_Pl^2/2) R | a_2 * Lambda^2 | Second spectral moment of D_K |
| c_{41} R_{mu nu} R^{mu nu} + c_{42} R^2 | a_4 | Fourth spectral moment of D_K |
| c_{61}/M^2 R^3 + ... | a_6 / Lambda^2 | Sixth spectral moment (suppressed) |

The spectral action IS a GREFT with all coefficients determined by D_K. This is not an analogy -- it is a mathematical identity (the Seeley-DeWitt expansion IS the derivative expansion of the spectral action).

**Tools we should adopt**: Burgess's power-counting formula (Eq. 3.14) should be applied to verify that the spectral action's perturbative expansion is under control at the transit energy scale. The relevant parameter is (H_fold / 4 pi M_Pl)^2 ~ (10^14 / 10^19)^2 ~ 10^{-10}. This is tiny, confirming that the Seeley-DeWitt expansion is well-controlled during the transit. Quantum gravitational corrections to the spectral action's cosmological predictions are of order 10^{-10} -- negligible.

### II.11. Achucarro & Palma -- Inflation Theory & Observations [11]

**What inflation math this paper develops**: Snowmass 2021 overview of three observational targets: primordial gravitational waves (r), non-Gaussianity (f_NL), and primordial features. Current constraints and future experimental thresholds.

**Exflation counterpart**: The three observational targets map to specific exflation predictions:

1. **Tensor modes**: r = 0.024 at CMB (S66 TENSOR-TRANSFER-66). CMB-S4 targets sigma(r) ~ 5 x 10^{-4}, so this is a 48-sigma detection prediction. Current BICEP/Keck r < 0.036 is consistent. A definitive test is imminent.

2. **Non-Gaussianity**: The exflation transit produces GGE excitations that generically violate the single-field consistency relation. The Maldacena consistency relation f_NL^local = (5/12)(1 - n_s) ~ 0.02 does NOT apply to exflation. The exflation f_NL has not been computed, but the dissipative EFT analysis (Paper 09) suggests it could be O(1) to O(10^3) depending on the effective dissipation at the fold.

3. **Features**: The D_K eigenvalue spectrum has discrete structure (155,984 eigenvalues at L_max=10). If this imprints on the perturbation spectrum, there would be features at specific k-values set by the eigenvalue spacings. Planck finds no features above ~1% of A_s. The framework should compute the expected feature amplitude from eigenvalue discreteness.

### II.12. Weinberg -- The Cosmological Constant Problems [12]

**What inflation math this paper develops**: Formulation of the old (120 OOM) and new (coincidence) CC problems. Weinberg's no-go theorem for self-adjustment mechanisms. Critique of quintessence. Anthropic considerations.

**Exflation counterpart -- THE CENTRAL PAPER FOR THE OOM REFRAME**: Weinberg's 120 OOM is the same number as the framework's 114 OOM. The difference (120 vs 114) arises because Weinberg estimates from the Planck scale (rho ~ M_Pl^4), while the framework computes from the spectral action a_0 at the fold (rho ~ Lambda_fold^4 with Lambda_fold ~ 10^{17.6} GeV). The 6 OOM difference is (M_Pl / Lambda_fold)^4 ~ (10^{19}/10^{17.6})^4 ~ 10^{5.6}.

The critical reframe: In LCDM, the inflaton potential V_inflation ~ (10^16 GeV)^4 ~ 10^{64} GeV^4, while the observed CC is Lambda_obs ~ 10^{-47} GeV^4. That is a ratio of 10^{111}. Nobody in the inflation community calls this a "problem with inflation." They call it "inflation happened, and then the CC relaxed to its current value through some mechanism (we don't know which one)."

The exflation framework's spectral action fold energy S(tau_fold) ~ 10^{67} GeV^4, and the observed CC is Lambda_obs ~ 10^{-47} GeV^4. That is a ratio of 10^{114}. This is the SAME type of ratio, from the SAME type of physics (energy scale at the epoch of rapid expansion vs. today's vacuum energy). The Volovik relaxation (rho_vac ~ H^2 M_Pl^2) provides the dynamical mechanism, landing at 0.01 OOM from observation (S66 DILUTION-CC PASS).

Weinberg's no-go theorem assumes: (i) field content is g_{mu nu} plus self-adjusting fields, (ii) translationally invariant vacuum, (iii) general Lagrangian. The spectral triple evades assumption (ii): the exflation transit at the van Hove fold explicitly breaks translational invariance. It also evades assumption (i) in a deeper sense: the D_K spectrum is not "a field on spacetime" but the internal structure FROM WHICH spacetime emerges.

### II.13. Bousso & Polchinski -- Four-form Fluxes [13]

**What inflation math this paper develops**: The string landscape solution to the CC problem. Four-form flux quantization, the "gap problem" for a single flux, and the "discretuum" from ~100 incommensurate fluxes providing a dense enough spectrum to land near Lambda_obs.

**Exflation counterpart**: The framework has NO analog of the Bousso-Polchinski mechanism. There is one SU(3) fiber, one spectral triple, one vacuum. There is no landscape of 10^{100} vacua. This is simultaneously the framework's greatest strength (uniqueness, predictivity) and its greatest challenge (no statistical escape hatch for the CC).

**Tools we should adopt**: The BP discretuum condition (Eq. 2.25-2.26) provides a useful negative result: it tells us exactly HOW MANY degrees of freedom would be needed for a statistical CC cancellation. The framework's 155,984 D_K eigenvalues provide many "charges" (eigenvalue spacings), but the q-theory self-tuning FAIL (S66 W1-D) shows these charges are TOO DEGENERATE (9 Kramers pairs at identical omega = 0.841 M_KK) to form a dense discretuum. The effective number of independent "fluxes" is not 155,984 but rather ~17,000 distinct eigenvalue values, which is enough by BP's counting (they need ~100) -- BUT the q-theory vacuum equation P_vac = epsilon - N d(epsilon)/dN does not have the right structure. The BP mechanism requires independent, incommensurate charges; the D_K eigenvalues are organized by SU(3) representation theory with systematic degeneracies.

### II.14. Padmanabhan -- CC Weight of the Vacuum [14]

**What inflation math this paper develops**: The dual matter/geometry interpretations of the CC. Zeldovich's rho ~ G E^6 estimate. Unimodular gravity (CC as integration constant). Padmanabhan's stochastic proposal: Delta Lambda ~ H_0^2 from Poisson fluctuations in discrete spacetime.

**Exflation counterpart**: Padmanabhan's stochastic CC proposal -- Delta Lambda ~ 8 pi L_P^2 / sqrt(V) where V is the spacetime 4-volume -- has a direct spectral analog. The spectral action is a sum over 155,984 eigenvalues. If the sum has Poisson-type fluctuations (standard deviation ~ sqrt(N) / N), the fractional fluctuation is ~ 1/sqrt(155984) ~ 0.25%. Applied to the vacuum energy: Delta rho / rho ~ 0.0025, giving Delta rho ~ 0.0025 * rho_fold. This does NOT solve the CC problem (0.0025 * 10^67 ~ 10^{64.4}, still 111 OOM too large). The fluctuation approach fails because the eigenvalue sum is NOT random -- it is determined by the SU(3) representation theory with high degeneracy.

**Tools we should adopt**: Padmanabhan's Eq. (8) -- the gravitational acceleration equation nabla.g = -4 pi G (rho + 3P) -- is useful for checking the framework's w(z) predictions. The "repulsive gravity" condition rho + 3P < 0 requires w < -1/3. The framework's w_0 = -0.918 satisfies this comfortably.

### II.15. Padilla -- CC Lectures [15]

**What inflation math this paper develops**: The radiative instability argument (the REAL CC problem is that cancellation must be re-done at every loop order). Weinberg's no-go theorem worked through in detail. The Kaloper-Padilla sequestering mechanism.

**Exflation counterpart**: The sequestering mechanism is the most structurally analogous CC solution to the exflation framework's Volovik relaxation. Both are GLOBAL modifications:
- Sequestering: Lambda = (1/4) <T^alpha_alpha> (spacetime average of local stress-energy)
- Volovik: rho_vac ~ H(t)^2 M_Pl^2 (vacuum tracks expansion rate via Gibbs-Duhem)

The sequestering requires: (a) spatially closed universe, (b) finite spacetime volume, (c) w != -1 exactly. The exflation framework provides (c) naturally (w_0 = -0.918). Whether the spectral triple implies (a) and (b) is an open structural question.

**Tools we should adopt**: Padilla's radiative instability criterion (Sec. 2) provides the sharpest test: is the Volovik relaxation mechanism rho_vac ~ H^2 stable under loop corrections to the matter sector living on the spectral triple? Since the Volovik mechanism is FUNCTIONAL-INDEPENDENT (S66 W1-A classification), it does not depend on the matter loop structure -- it depends only on the existence of a conserved vacuum variable q with positive compressibility. This is a thermodynamic argument, not a perturbative one, and therefore is plausibly immune to the radiative instability that kills perturbative CC solutions.

### II.16. Planck 2018 X -- Constraints on Inflation [16]

**What inflation math this paper develops**: The definitive observational constraints. n_s = 0.9649 +/- 0.0042, r < 0.056 (with BK15), alpha_s = -0.0045 +/- 0.0067, Omega_K = 0.0007 +/- 0.0019. Pure power-law confirmed over 0.005 < k < 0.2 Mpc^{-1}. No features. Non-adiabatic fraction < 1.7%.

**Exflation counterpart -- THE BENCHMARK**: Every framework prediction must be compared to this paper.

| Observable | Planck 2018 | Exflation Prediction | Tension | Source |
|:---|:---|:---|:---|:---|
| n_s | 0.9649 +/- 0.0042 | 0.9590 (BCS + one-loop) | 1.40 sigma | S65 |
| r | < 0.056 (Planck+BK15) | 0.024 (CMB scale) | CONSISTENT | S66 |
| alpha_s | -0.0045 +/- 0.0067 | -0.038 (L_max=4) | 5.0 sigma FAIL | S66 |
| Omega_K | 0.0007 +/- 0.0019 | 0 (flat) | CONSISTENT | -- |
| Non-adiabatic | < 1.7% (95% CL) | NOT COMPUTED | -- | -- |
| Features | < 1% A_s | NOT COMPUTED | -- | -- |

The 5.0-sigma tension on alpha_s is the most severe. The framework's defense is that alpha_s = -0.038 is a truncation artifact at L_max = 4, and the Richardson extrapolation to L->infinity gives -0.037, essentially the same value. If the true alpha_s is ~ -0.04, the framework is in severe tension with Planck. If truncation effects are more severe than estimated, alpha_s could be closer to zero.

---

## III. The OOM "Problem" Reframed

### III.A. Inflation's Own OOM Gap

Consider the standard inflationary picture. The inflaton potential during inflation has characteristic energy density:

V_inflation ~ (10^16 GeV)^4 = 10^64 GeV^4 (Baumann Eq. 218, for r ~ 0.01)

The observed cosmological constant today:

Lambda_obs = 2.846 x 10^{-47} GeV^4

The ratio: V_inflation / Lambda_obs ~ 10^{111}.

In the LCDM paradigm, this 111 OOM ratio is universally accepted as "inflation happened, and then the vacuum energy somehow relaxed to its present value." The entire Weinberg paper (Paper 12) is about WHY this relaxation happens, not whether it is a problem WITH inflation. The CC problem is treated as independent of inflation -- it is about the final value, not the initial value.

### III.B. Exflation's OOM Gap

The spectral action at the van Hove fold:

S(tau_fold) ~ 10^67 GeV^4 (from a_0 * Lambda^4 at the fold)

The observed CC:

Lambda_obs = 2.846 x 10^{-47} GeV^4

The ratio: S(tau_fold) / Lambda_obs ~ 10^{114}.

This is 3 OOM larger than inflation's gap because the spectral action includes contributions from the FULL internal geometry (all 155,984 D_K eigenvalues), not just a single inflaton field.

### III.C. The Structural Equivalence

Both gaps have the same origin: the energy scale at the epoch of rapid expansion is ~10^{16} GeV, and the CC today is ~10^{-47} GeV^4. The number 120 (Weinberg), 111 (inflation), or 114 (exflation) differs only in the precise accounting of which degrees of freedom contribute.

In inflation: the 111 OOM gap is "explained" by saying inflation happened (the inflaton rolled from V_high to V_low), and whatever mechanism sets the CC (unknown) does so independently. The gap is the expansion history.

In exflation: the 114 OOM gap is "explained" by the supersonic transit through the fold (the substrate reorganized its spectral weight from high-energy to low-energy), and the Volovik relaxation (rho_vac ~ H^2) provides the dynamical mechanism for the CC to track the expansion rate. The gap IS the expansion history, and the Volovik relaxation IS the mechanism that inflation leaves unspecified.

### III.D. What Volovik Relaxation Actually Does

The Volovik relaxation (S66 DILUTION-CC PASS, Scenario B) works as follows:

1. At the fold: rho_vac(fold) ~ M_Pl^2 H_fold^2 ~ (10^{19})^2 (10^{14})^2 ~ 10^{66} GeV^4
2. During radiation era: rho_vac tracks rho_rad ~ a^{-4}, so rho_vac ~ H^2 ~ a^{-4}
3. During matter era: rho_vac tracks rho_matter ~ a^{-3}, so rho_vac ~ H^2 ~ a^{-3}
4. Today: rho_vac(today) ~ M_Pl^2 H_0^2 ~ (10^{19})^2 (10^{-33})^2 ~ 10^{-28} GeV^2 -> 10^{-47} GeV^4

The relaxation from 10^66 to 10^{-47} is 113 OOM, accomplished by 68 e-folds of expansion (each reducing rho_vac by a factor of e^4 ~ 55 per e-fold for radiation, less during matter domination).

This is NOT a "closing" of a "gap." It is the same physics that standard cosmology uses to evolve the energy density from the inflation scale to today. The 114 OOM IS the expansion history. The Volovik mechanism provides the equation of state (rho_vac ~ H^2) that governs the relaxation, landing at rho_vac(today)/rho_obs = 1.032 (0.01 OOM).

### III.E. Why Exflation is Actually Better Than Inflation Here

Standard inflation has NO mechanism for the CC relaxation. It simply assumes the CC is what it is (fine-tuned, anthropic, or unknown). The 111 OOM gap between V_inflation and Lambda_obs is left as two separate problems: "why did inflation happen?" and "why is the CC small?"

Exflation provides a unified answer: the transit (exflation) happened because the spectral action S(tau) has a fold at tau = 0.190, and the CC relaxed to its present value because the Volovik Gibbs-Duhem relation forces rho_vac ~ H^2 in a self-sustained vacuum. The 114 OOM is not a problem -- it is the prediction. The remaining 0.01 OOM discrepancy is the actual precision of the mechanism.

---

## IV. Missing Tools

The inflation literature contains mathematical techniques that the exflation framework has not yet adopted. These are ranked by expected impact.

### IV.A. CRITICAL: In-In Formalism for GGE Bispectrum

**Source**: Maldacena [03], Cheung et al. [07]
**What it does**: Computes n-point functions of primordial perturbations using the interaction Hamiltonian and time-ordered products.
**Why exflation needs it**: The framework has not computed the bispectrum (three-point function) of the GGE relic. The Maldacena consistency relation (f_NL = (5/12)(1-n_s) for single-field) does NOT apply because exflation is inherently multifield. The actual f_NL could be O(1) to O(10^3) from the dissipative transit physics. This is a TESTABLE PREDICTION that the framework is leaving on the table.
**Input data needed**: The third-order spectral action S_3(tau) at the fold, or equivalently the GGE cubic interaction vertex.
**Expected result**: An f_NL prediction that either confirms or excludes the framework against Planck bounds.

### IV.B. CRITICAL: Dissipative Power Spectrum Normalization

**Source**: Lopez Nacir et al. [09]
**What it does**: Computes the noise-dominated power spectrum when dissipation is strong (gamma >> H).
**Why exflation needs it**: The 3.15 OOM A_s gap may arise because the current computation uses the Garriga-Mukhanov normalization (designed for slow-roll vacuum fluctuations), while the actual transit is a strongly dissipative event where the power spectrum is dominated by pair-creation noise. The dissipative formula would give a different A_s normalization.
**Input data needed**: The effective friction coefficient gamma_eff at the fold, the noise power spectrum nu from Parker pair creation, and the fabric sound speed c_BLV.
**Expected result**: A revised A_s that may be closer to the Planck value.

### IV.C. HIGH: Multifield Delta-N for GGE Conversion

**Source**: Senatore & Zaldarriaga [08], Lyth & Riotto [02]
**What it does**: Converts fluctuations of multiple light fields into the curvature perturbation zeta via the delta-N formalism.
**Why exflation needs it**: The GGE relic has multiple quasiparticle branches (acoustic, optical, Leggett). Each contributes to zeta through different coupling strengths. The current single-field conversion misses the multifield contributions, which could enhance or suppress A_s.
**Input data needed**: The zeta-sigma_I conversion coefficients for each GGE branch.
**Expected result**: A multifield A_s that accounts for all GGE branches.

### IV.D. HIGH: EFT Operator Matching

**Source**: Cheung et al. [07], Burgess [10]
**What it does**: Maps the spectral action moments onto the EFT operator coefficients (M_2, M_3, M-bar).
**Why exflation needs it**: This would connect the spectral action's Seeley-DeWitt expansion to the standard EFT parametrization, enabling direct comparison with all inflation models simultaneously.
**Input data needed**: a_0, a_2, a_4 at the fold, plus their tau-derivatives.
**Expected result**: Values for M_2, M_3, and the M-bar parameters, determining c_s, f_NL, and the tensor modification.

### IV.E. MEDIUM: Post-Transit Parametric Resonance

**Source**: Kofman, Linde, Starobinsky [06]
**What it does**: Analyzes whether post-transit oscillations of tau can parametrically amplify specific GGE modes.
**Why exflation needs it**: If tau undergoes any ringing after settling from the fold, this would create a secondary preheating epoch that could modify the GGE occupation spectrum. The settling time is 10^{-47} yr (instantaneous), but the question is whether the settling is monotonic or oscillatory.
**Input data needed**: The spectral action S(tau) as a function of tau in the vicinity of the post-fold settling point, including its third and fourth derivatives.
**Expected result**: Either confirmation that settling is monotonic (no post-transit resonance) or identification of amplified k-modes.

### IV.F. MEDIUM: Bayesian Model Comparison

**Source**: Martin, Ringeval, Vennin [05], Planck 2018 [16]
**What it does**: Computes the Bayesian evidence for the exflation prediction (n_s, r, alpha_s) against the 74-model inflation prior.
**Why exflation needs it**: This would give a single number quantifying how well exflation competes against inflation models as an explanation for Planck data.
**Input data needed**: The exflation predictions (n_s = 0.9590, r = 0.024, alpha_s = -0.038) plus the Planck likelihood function.
**Expected result**: A Bayes factor ranking exflation against Starobinsky, phi^2, natural inflation, etc.

### IV.G. MEDIUM: Angular Power Spectrum C_l from GGE

**Source**: Baumann [01] Lecture 3, Brandenberger [04]
**What it does**: Computes the CMB angular power spectrum C_l from the primordial perturbation spectrum using transfer functions.
**Why exflation needs it**: The framework has n_s and A_s predictions but has not computed the full C_l spectrum. Features from the D_K eigenvalue discreteness would appear as oscillations in C_l.
**Input data needed**: The GGE perturbation spectrum P(k), transfer functions, and line-of-sight integrals.
**Expected result**: A full TT/TE/EE angular power spectrum for comparison with Planck data.

### IV.H. LOW: Sequestering-Spectral Hybrid

**Source**: Padilla [15]
**What it does**: Explores whether the spectral triple contains an analog of the sequestering global constraint.
**Why exflation needs it**: The Kaloper-Padilla sequestering mechanism cancels SM vacuum energy through global dynamical variables. The spectral action's trace formula is already a global quantity (sum over ALL eigenvalues). If the trace constraint can be decomposed into a "bulk" piece (absorbed) and a "fluctuation" piece (residual CC), this would provide a second CC reduction mechanism beyond Volovik.
**Input data needed**: The algebraic structure of the spectral action trace, decomposed by representation.
**Expected result**: Either a sequestering-like constraint from the spectral triple, or a proof that no such constraint exists.

---

## V. The Exflation Advantage

### V.A. Zero Free Parameters

Every inflation model requires at least one free parameter (the potential V(phi) or its coefficients), and most require N_* (number of e-folds, set by the unknown reheating temperature) as an additional input. The Encyclopaedia Inflationaris [05] catalogs 74 models, each with 1-3 free parameters, yielding a sprawling n_s-r plane.

Exflation has zero free parameters. The spectral triple (M^4 x SU(3), Jensen deformation, Dirac operator D_K) uniquely determines:
- n_s = 0.9590 (from the spectral action curvature at the fold)
- r = 0.024 (from second-order tensor mode amplitude)
- n_T = +0.468 at transit scale (blue, from spectral gap dynamics)
- n_T = -3.02e-3 at CMB scale (red, standard transfer)
- Omega_DM h^2 = 0.120 (Leggett-only, 0.6% from Planck)
- w_0 = -0.918 (combined GGE + Josephson)

These are not fits. They are outputs of a single eigenvalue problem. The probability that a random geometry produces this cluster of near-observational values is the product of individual probabilities, not the arithmetic mean.

### V.B. No Eta Problem

The eta problem (Lyth-Riotto [02] Sec. 5, Burgess [10] Sec. 3) is the central sickness of inflation model-building: generic supergravity gives the inflaton a mass m_phi ~ H, violating slow-roll. Every inflation model must explain why its inflaton is unnaturally light.

Exflation has no inflaton. The Jensen parameter tau is a geometric coordinate of the spectral triple, not a quantum field. It does not receive radiative mass corrections. The spectral action S(tau) is computed exactly from D_K, with no perturbative expansion in tau. The "eta problem" does not arise.

### V.C. No Trans-Planckian Problem

Brandenberger [04] Sec. 5 identifies the trans-Planckian problem: if inflation lasted sufficiently long, observed CMB modes had sub-Planckian wavelengths at the onset. The spectral triple has a natural UV cutoff (the maximum D_K eigenvalue at any finite L_max). Modes cannot have wavelengths shorter than the spectral resolution. The trans-Planckian problem is absent by construction.

### V.D. No Landscape

Bousso-Polchinski [13] requires ~10^{100} string vacua to solve the CC problem statistically. Exflation has one vacuum, one spectral triple, one internal geometry. The CC problem is solved dynamically (Volovik relaxation) rather than statistically (landscape scanning).

### V.E. Unified Dark Sector

In LCDM, dark matter and dark energy are unrelated: CDM is a new particle, Lambda is a constant. In exflation, both emerge from the same GGE relic:
- Dark matter = Leggett-channel quasiparticle (inter-band coherence mode)
- Dark energy = effacement residual (0.03% leakage through impedance mismatch) + Josephson contribution

This unification from a single spectral triple is structurally distinct from any inflation model.

### V.F. GGE Permanence vs. Thermal Reheating

In standard inflation, reheating produces a thermal bath (KLS [06]). The thermal distribution erases information about the inflationary epoch. Only n_s, r, and f_NL survive as observable relics.

In exflation, the GGE relic never thermalizes (Ordered Veil). The quasiparticle occupation numbers {n_k} are conserved integrals of motion (Richardson-Gaudin integrability). The ENTIRE occupation spectrum is in principle observable, not just its low-order moments. This is a dramatically richer observational target.

---

## VI. Computation Suggestions

The following computations arise directly from the inflation-exflation comparison. They are ordered by EVOI (expected value of information).

| # | Computation | Input | Expected Output | Priority | Source Paper |
|:---|:---|:---|:---|:---|:---|
| 1 | **DISSIPATIVE-AS**: Noise-dominated A_s normalization | gamma_eff at fold, nu from Parker pairs, c_BLV | Revised A_s (may close 3.15 OOM gap) | CRITICAL | Lopez Nacir [09] |
| 2 | **GGE-BISPECTRUM**: In-in f_NL from transit | S_3(tau) at fold, GGE cubic vertex | f_NL prediction (testable against Planck bounds) | CRITICAL | Maldacena [03] |
| 3 | **EFT-MATCHING**: Spectral moments to EFT operators | a_0, a_2, a_4 + tau-derivatives at fold | M_2, M_3, M-bar values; c_s(EFT); consistency check | HIGH | Cheung et al. [07] |
| 4 | **MULTIFIELD-AS**: Delta-N conversion for GGE branches | zeta-sigma conversion coefficients per branch | Multifield A_s (tests single-field assumption) | HIGH | Senatore-Zaldarriaga [08] |
| 5 | **NS-CORRECTION-CS**: c_s time-derivative correction to n_s | dc_{BLV}/dtau at fold, H at fold | Corrected n_s (additional term from Cheung et al. Eq. 41) | HIGH | Cheung et al. [07] |
| 6 | **POST-TRANSIT-RESONANCE**: Parametric amplification check | S(tau) 3rd and 4th derivatives post-fold | Resonance bands (or confirmation of monotonic settling) | MEDIUM | Kofman-Linde-Starobinsky [06] |
| 7 | **BAYESIAN-NS-R**: Model comparison vs 74 inflation models | (n_s, r, alpha_s) + Planck likelihood | Bayes factor ranking vs Starobinsky, etc. | MEDIUM | Encyclopaedia [05] |
| 8 | **CL-SPECTRUM**: Full angular power spectrum C_l from GGE | P(k) from GGE, transfer functions | TT/TE/EE spectrum for Planck comparison | MEDIUM | Baumann [01] |
| 9 | **BACK-REACTION-CC**: Long-wavelength GGE back-reaction | GGE occupation spectrum, energy-momentum tensor | Effective CC contribution from back-reaction | MEDIUM | Brandenberger [04] |
| 10 | **SEQUESTER-SPECTRAL**: Global constraint from spectral trace | Algebraic decomposition of Tr f(D_K^2) | Whether spectral triple contains sequestering analog | LOW | Padilla [15] |
| 11 | **NON-ADIABATIC**: Isocurvature fraction from GGE branches | Branch-by-branch perturbation spectra | Non-adiabatic fraction (must be < 1.7%) | LOW | Planck [16] |
| 12 | **FEATURE-AMPLITUDE**: Discreteness features in P(k) | D_K eigenvalue spacings | Feature amplitude (must be < 1% of A_s) | LOW | Planck [16] |

### Computation Dependencies

- DISSIPATIVE-AS (1) is independent and should be computed first. If it closes the A_s gap, this is a major breakthrough.
- GGE-BISPECTRUM (2) requires the in-in formalism setup, which is independent of other computations.
- EFT-MATCHING (3) provides input for NS-CORRECTION-CS (5) -- the EFT identification determines which terms contribute to the generalized n_s formula.
- MULTIFIELD-AS (4) is independent but may be partially superseded by DISSIPATIVE-AS if the dissipative formula already accounts for multifield effects.
- POST-TRANSIT-RESONANCE (6) feeds into the A_s normalization if resonance bands exist.

---

## Summary

The inflation literature contains a complete mathematical toolkit for computing perturbation spectra, non-Gaussianities, and energy transfer during and after a period of rapid expansion. The exflation framework reproduces many of the same observational effects (n_s, r, dark matter, dark energy) from a fundamentally different mechanism (supersonic spectral transit rather than slow scalar field roll). The 114 OOM between fold energy and today's CC is not a "problem" -- it is the expansion history, exactly as inflation's 111 OOM gap is universally accepted as "inflation happened."

The most productive tools the framework has not yet adopted are:
1. The dissipative EFT normalization (Lopez Nacir et al.), which may resolve the A_s gap
2. The in-in formalism for non-Gaussianity (Maldacena), which gives a testable f_NL prediction
3. The EFT operator matching (Cheung et al.), which connects spectral moments to the standard parametrization

The framework's structural advantages (zero parameters, no eta problem, no trans-Planckian problem, no landscape, unified dark sector, GGE permanence) are real and not shared by any of the 74+ inflation models cataloged in the literature. Its structural challenges (alpha_s = -0.038 at 5-sigma tension with Planck, A_s gap of 3.15 OOM, scheme dependence of eps_H sign) are equally real. The inflation mathematics provides specific tools to address these challenges, and this synthesis identifies 12 computations that would bring the framework's observational predictions to the precision required for definitive comparison with CMB data.
