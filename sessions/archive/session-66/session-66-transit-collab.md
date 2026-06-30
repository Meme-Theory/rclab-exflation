# Transit Dynamics Theorist -- Collaborative Feedback on Session 66

**Author**: Transit Dynamics Theorist
**Date**: 2026-04-04
**Re**: Session 66 Results -- Spectral Ops. Engagement

---

## Section 1: Key Observations

This is my first engagement with the phonon-exflation framework. I come to it as a specialist in Bogoliubov transformations, Kibble-Zurek scaling, parametric resonance, GGE formation, and power spectrum computation from non-equilibrium dynamics. My assessment is grounded in the 30-paper transit dynamics corpus (Parker [01], Birrell-Davies [02], Mukhanov-Chibisov [03], Kofman-Linde-Starobinsky [04], Kibble [05], Zurek [06], del Campo-Zurek [11], Rigol [13], Calabrese-Essler [23], Motohashi [19], Barcelo-Liberati-Visser [08], Volovik [27], and others).

Five structural observations from the session results, assessed through the mode equation framework:

**1. The supersonic transit is deep in the impulse regime, and slow-roll is categorically inapplicable.** The framework reports Mach 13.75, dt_transit = 0.66 e-folds, and eta_H of order unity at the fold. These three numbers place the system so far outside the slow-roll regime that any formula derived under the assumptions eps_H << 1 and eta_H << 1 is not merely inaccurate but structurally wrong. The Mukhanov-Sasaki equation u_k'' + (k^2 - a''/a) u_k = 0 [03, Sec. 2] itself may still apply, but the standard WKB approximation for its solutions does not. The Stokes phenomenon at the turning point (where k^2 ~ a''/a) is not perturbative when eta_H ~ O(1): the Bogoliubov coefficients must be computed by solving the mode equation exactly through the transit, not by applying slow-roll conversion formulas to spectral action derivatives. This observation is central to the alpha_s tension.

**2. The GGE relic formation is the correct post-transit state for an integrable system.** The integrability tower (7 diagnostics, N_pair = 1-4, 36D classical moduli) confirmed in S66 is precisely the condition under which a quantum quench produces a GGE rather than a thermal state. Rigol [13] proves this: for integrable Hamiltonians, the long-time steady state is rho_GGE = exp(-Sum_m lambda_m I_m) / Z, where {I_m} are the conserved charges. The 59.8 quasiparticle pairs from the transit are the Bogoliubov output of a sudden quench, and their distribution is frozen by the Richardson-Gaudin integrals. The Bertini-Essler cross-check (W8-B, t_therm ~ 10^580 t_universe) confirms this is permanent. From the transit dynamics perspective, the Ordered Veil is not a surprise but a necessary consequence of integrability: Calabrese-Essler [23] show that the post-quench state of the transverse-field Ising chain never thermalizes, and the framework's BCS pairing Hamiltonian belongs to the same universality class (integrable Richardson-Gaudin model).

**3. The spectral functional sign flip (eps_H reversal between cutoff classes) has no analog in standard Bogoliubov theory.** In any mode equation u_k'' + omega_k^2(t) u_k = 0, the particle number N_k = |beta_k|^2 depends on the TIME PROFILE of omega_k(t), not on the weighting of modes in a sum. The Bogoliubov coefficients are determined by how fast omega_k changes relative to omega_k itself (the adiabatic parameter |d omega / dt| / omega^2). Whether eps_H is positive or negative is a question about the direction of the spectral action gradient, which determines whether the effective frequency omega_k(t) is increasing or decreasing during the transit. The sign flip between sqrt(x) and zeta cutoffs (W1-B, W2-A) means these two functionals predict OPPOSITE directions of frequency evolution at the fold. From the mode equation perspective, this is equivalent to asking whether the transit is an expansion (frequencies redshift, eps_H > 0) or a contraction (frequencies blueshift, eps_H < 0). Only one of these can be physical.

**4. The 0.66 e-fold transit duration is incompatible with CMB-scale perturbation generation via standard inflation.** The W3-C result (tensor transfer function) correctly identifies this: 0.66 e-folds cannot source perturbations at scales separated by 54 decades from the transit scale. In standard inflationary Bogoliubov theory, each e-fold of inflation generates perturbations at one decade of wavenumber [03]. The framework needs approximately 60 e-folds to source CMB-scale perturbations, but the transit provides only 0.66. This is not a weakness to be fixed; it is a structural feature that demands a fundamentally different perturbation generation mechanism. The acoustic white hole picture (causal disconnection by supersonic flow) may provide this, but the Bogoliubov calculation through the acoustic channel has not been performed.

**5. The Leggett-only DM result (0.6% from Planck) is the most robust observational match because it depends only on Bogoliubov pair production counting, not on the spectral functional.** The 59.8 quasiparticle pairs are produced by the transit through the van Hove fold, and the number of pairs is set by the excitation probability P_exc = 1.000 (saturated Landau-Zener, fully non-adiabatic transit). The partition into Leggett and BA channels depends on the BCS gap structure and the inter-band coupling, both of which are spectral properties of D_K -- FUNCTIONAL-INDEPENDENT. This makes the DM prediction the most structurally sound output of the transit dynamics.

---

## Section 2: Assessment of Key Findings

### 2.1 The alpha_s = -0.038 Tension: A Slow-Roll Mapping Artifact

This is the finding where my expertise is most directly relevant. The session reports alpha_s = -0.038 at 5.0 sigma from Planck, confirmed intrinsic at L_max = 4 and immune to Casimir smoothing. The 10-reviewer synthesis shows 7/10 favor a mapping artifact. I concur with the majority and can make the argument precise.

The slow-roll formula alpha_s = dn_s / d(ln k) requires a specific mapping between the internal deformation parameter tau and the physical wavenumber k. In slow-roll inflation, this mapping is:

    d(ln k) = d(ln a) = H dt = (1 / sqrt(2 eps_H)) dtau        (Eq. 1)

This formula is derived under the assumption that the mode function evolves adiabatically outside the horizon, with corrections suppressed by eps_H and eta_H. When eta_H ~ O(1) -- as it is at the van Hove fold -- the adiabatic approximation breaks down. The mode does NOT freeze out at horizon crossing in the standard way. Instead, the Stokes phenomenon at the turning point produces a Bogoliubov mixing that depends on the FULL profile of omega_k(t) through the non-adiabatic region, not just on the local value of eps_H.

The correct procedure is to solve the mode equation

    u_k'' + omega_k^2(tau) u_k = 0        (Eq. 2)

exactly through the transit region, with omega_k^2(tau) = k^2 - (a''/a)(tau) constructed from the spectral action S(tau) and its derivatives. The Bogoliubov coefficients alpha_k and beta_k are extracted from the asymptotic behavior:

    u_k -> alpha_k e^{-i omega_k tau} + beta_k e^{+i omega_k tau}  as tau -> +infinity        (Eq. 3)

and the power spectrum is P(k) = (k^3 / 2 pi^2) |u_k|^2 evaluated at late times. The spectral index n_s - 1 = d ln P / d ln k and the running alpha_s = d n_s / d ln k follow by differentiation of P(k) -- NOT by applying slow-roll conversion formulas to eps_H(tau).

For the supersonic transit (Mach 13.75, duration 0.66 e-folds), the relevant comparison is the sudden approximation (del Campo-Zurek [11]). In this limit, the Bogoliubov coefficient for a mode with frequency omega is:

    |beta_k|^2 ~ (Delta omega / (2 omega))^2        (Eq. 4)

where Delta omega is the frequency jump across the transit. The power spectrum of the resulting excitations is determined by the RATIO of pre-transit to post-transit frequencies, not by the logarithmic derivative of the spectral action. If all modes experience a similar fractional frequency change (which the W4-F result -- 6% sector variation in d(ln S)/dtau -- suggests), then the sudden-approximation power spectrum is nearly flat, with alpha_s ~ 0. This is the physical mechanism by which the transit could resolve the tension.

The computation that tests this -- solving Eq. 2 numerically through the transit with the framework's S(tau) profile -- is the single most important unperformed calculation in the entire framework. Every reviewer identifies it. I endorse this as the rate-limiting computation.

**Assessment**: The alpha_s = -0.038 is NOT a prediction of the framework's transit dynamics. It is a prediction of the SLOW-ROLL APPROXIMATION applied to a regime where slow-roll is inapplicable. The actual transit dynamics prediction has not been computed. Until it is, the 5-sigma tension is an artifact of methodology, not a falsification signal.

### 2.2 Volovik CC Relaxation (W1-A): Structurally Sound from the Bogoliubov Perspective

The Volovik result rho_vac ~ M_Pl^2 H_0^2 = 1.23e-47 GeV^4 (0.01 OOM from observation) is the most striking quantitative result of S66. From the transit dynamics perspective, this mechanism is consistent with the Bogoliubov framework in the following sense.

The post-transit GGE state has rho_GGE ~ 10^{115} rho_obs. The Volovik relaxation does NOT require the GGE to relax (it cannot -- the Richardson-Gaudin integrals prevent it). Instead, it requires the vacuum variable q to track the Hubble rate through the Gibbs-Duhem relation. In the superfluid analog (Volovik [27], Paper 04), this is the statement that the superfluid vacuum adjusts its chemical potential to cancel the cosmological constant in the thermodynamic limit. The GGE excitations sit ON TOP of this relaxing vacuum, carrying their conserved charges. The two coexist because they operate on different degrees of freedom: q is the macroscopic vacuum variable (related to the condensate), while the GGE charges are the microscopic quasiparticle occupations.

The critical test flagged by 9/10 reviewers is the BBN constraint (rho_vac/rho_rad = 0.67 at BBN). From the Bogoliubov perspective, the question is whether the Volovik tracking vacuum contributes as additional relativistic species (additive, giving delta_N_eff = 1.34, excluded) or modifies the equation of state of the existing radiation (non-additive, potentially consistent). In the superfluid 3He analog, the vacuum energy is NOT additive -- it is part of the condensate's equation of state, and the total pressure P = P_normal + P_vacuum integrates to zero in equilibrium (Volovik [27], equilibrium theorem). The BBN computation is straightforward and must be performed.

### 2.3 GGE Relic Formation: Correctly Identified as Permanent

The integrability closure (W6-A/B/C, W8-B) is the most complete I have seen in any framework, and it directly maps onto the Calabrese-Cardy / Rigol classification scheme [13, 23]. The diagnostics used -- SFF ramp slope, OEE saturation fraction, Lyapunov spectrum, Bertini-Essler timescale -- are the correct battery for determining whether a post-quench state thermalizes. The results are unambiguous:

- SFF: no ramp at any filling (N_pair = 1-4). This rules out RMT-level spectral rigidity [W6-C].
- OEE: saturation at 49% of S_max. In a chaotic system, this would be ~100% [W6-A]. The 49% is consistent with approximately half the operator Hilbert space being accessible after GGE equilibration.
- Lyapunov: lambda_chaos = 0 in the 36D classical moduli space [W6-B]. The potential is quadratic to 5 significant figures, with cubic anharmonicity vanishing by U(2) symmetry.
- Bertini-Essler: t_therm ~ 10^580 t_universe [W8-B], consistent with ADH to 1 OOM.

The connection to transit dynamics is direct. The Bogoliubov transformation that produces the 59.8 quasiparticle pairs generates a squeezed state. In an integrable system, this squeezed state relaxes to the GGE (Rigol [13]). In a chaotic system, it would thermalize to the canonical ensemble (Berges [10]). The framework is integrable, so the GGE is the correct asymptotic state. The Bogoliubov occupation numbers N_k = |beta_k|^2 are the inputs to the GGE: each conserved charge I_m constrains the distribution, and the GGE Lagrange multipliers lambda_m are fixed by <I_m>_GGE = <I_m>_initial.

### 2.4 Power Spectrum from an Impulsive Transit: What the Correct Computation Looks Like

The framework's transit through the van Hove fold lasts 0.66 e-folds at Mach 13.75. This places it in the sudden-quench regime of the Kibble-Zurek classification [06, 11]. For a quench that is fast compared to the system's internal response time (tau_quench << tau_relax), the defect density saturates at the impulse-regime value:

    n_defect ~ xi_0^{-d}        (Eq. 5)

where xi_0 is the microscopic correlation length, independent of the quench rate (del Campo-Zurek [11]). The analogous statement for the power spectrum is: in the sudden limit, the Bogoliubov occupation N_k = |beta_k|^2 approaches a UNIVERSAL form that depends only on the ratio of pre-transit to post-transit frequencies, not on the rate of change:

    |beta_k|^2 = (omega_k^{after} - omega_k^{before})^2 / (4 omega_k^{before} omega_k^{after})        (Eq. 6)

This is the standard sudden-approximation result (Parker [01], Sec. 3; Birrell-Davies [02], Ch. 3). The power spectrum that follows from Eq. 6 has a spectral index determined by the DISPERSION RELATION omega_k, not by the time derivative of the spectral action. If all modes experience the same fractional frequency jump (which the 6% sector uniformity from W4-F strongly suggests), the resulting spectrum is nearly scale-invariant with:

    n_s - 1 ~ d ln(Delta omega / omega) / d ln k        (Eq. 7)

The running alpha_s = d(n_s - 1) / d ln k then depends on how the fractional frequency jump varies with wavenumber. For a transit through a van Hove singularity (where the density of states diverges), the frequency jump has a universal form dictated by the singularity type. The van Hove fold (d^2 omega / dk^2 = 0) gives a square-root singularity in the density of states, which translates to a specific k-dependence of the Bogoliubov coefficients.

This computation has not been performed. It requires:
1. The full dispersion relation omega_k(tau) across the transit, for each PW sector.
2. Numerical solution of the mode equation (Eq. 2) through the fold for a grid of k values.
3. Extraction of |beta_k|^2 from the asymptotic form (Eq. 3).
4. Construction of P(k) = (k^3 / 2 pi^2) * |beta_k|^2.
5. Numerical differentiation to obtain n_s(k) and alpha_s(k).

Until this is done, all statements about the framework's power spectrum are provisional.

### 2.5 Preheating Literature Tools the Framework Should Adopt

The framework's transit dynamics shares structural features with preheating after inflation (Kofman-Linde-Starobinsky [04], Amin [17]). In preheating, the oscillating inflaton drives a Mathieu equation for coupled fields:

    chi_k'' + [k^2 + g^2 phi_0^2 cos^2(m t)] chi_k = 0        (Eq. 8)

with exponential particle production in instability bands determined by the Floquet exponent mu_k. The framework's transit is not periodic (it is a single impulsive event), but the mathematical structure is identical: a mode equation with time-dependent frequency. The tools of the preheating literature that are directly applicable include:

- **Transfer matrix methods**: For piecewise analytic omega_k(t), the Bogoliubov coefficients can be computed exactly by matching WKB solutions across regions [04, Sec. 3]. The transit can be approximated as a piecewise profile: adiabatic (pre-fold) -> impulsive (fold) -> adiabatic (post-fold), with transfer matrices connecting each region.
- **Backreaction estimates**: Kofman-Linde-Starobinsky [04] and Amin [17] develop self-consistent treatments where the produced particles backreact on the background. For the framework, the 59.8 quasiparticle pairs represent a specific energy extraction from the spectral action gradient, and the backreaction is encoded in the settling time of tau (10^{-47} yr from S65 EP-65).
- **Non-thermal spectra**: Preheating produces non-thermal particle distributions [04, Sec. 4]. The framework's GGE relic is the exact analog: the post-transit occupation numbers are non-thermal, with mode-dependent occupations set by the Bogoliubov coefficients. The preheating literature provides extensive numerical tools for computing these distributions.

---

## Section 3: Collaborative Suggestions

### 3.1 Full Bogoliubov Calculation Through the Transit (HIGHEST PRIORITY)

Solve the mode equation u_k'' + omega_k^2(tau) u_k = 0 numerically through the van Hove fold, using the spectral action S(tau) at the 16 available tau values. Extract |beta_k|^2 for a grid of k values spanning the range from k_transit down to k_CMB (if the acoustic white hole mechanism provides the bridge). Compute P(k), n_s(k), and alpha_s(k) directly. This computation replaces the slow-roll conversion formula with the exact mode-equation solution and is the definitive test of the alpha_s tension.

**Input**: S(tau), dS/dtau, d^2S/dtau^2 at 16 tau values; Mach number; transit duration.
**Output**: |beta_k|^2, P(k), n_s, alpha_s from exact mode-equation solution.
**Gate**: PASS if |alpha_s| < 0.015 from exact solution; FAIL if > 0.030.

### 3.2 Sudden-Approximation Cross-Check

Independently compute |beta_k|^2 from the sudden-approximation formula (Eq. 6), using the pre-fold and post-fold frequencies from the D_K spectrum. This provides an analytic upper bound on the Bogoliubov occupation and an independent estimate of the power spectrum shape. The sudden approximation is exact in the Mach -> infinity limit and provides a benchmark for the numerical mode-equation solution.

### 3.3 Transfer Matrix Decomposition of the Transit

Decompose the transit into three regions: pre-fold adiabatic (tau < 0.15), impulsive fold (0.15 < tau < 0.25), post-fold adiabatic (tau > 0.25). Use WKB solutions in the adiabatic regions and numerical integration through the fold. Connect with 2x2 transfer matrices [04]. This provides a semi-analytic understanding of which features of the transit profile control n_s and alpha_s, and identifies whether the van Hove singularity is the dominant source of spectral running.

### 3.4 Kibble-Zurek Frozen-In Spectrum

Compute the Kibble-Zurek frozen-in correlation length xi_freeze from the dynamic exponent z = 2 (S63 exact) and the quench rate Mach 13.75. The KZ power spectrum P(k) ~ k^{-d + 2/nu_z} (where nu_z = nu * z is the combined KZ exponent) provides a fundamentally different scaling from the slow-roll formula. This has been proposed by multiple reviewers (Phonon-First, Tesla in the master synthesis) and is the most direct route to testing whether the non-equilibrium dynamics resolve the alpha_s tension.

### 3.5 BBN Constraint Computation for Volovik Scenario B

Compute delta_N_eff at T_BBN from the Volovik tracking vacuum. The distinction between additive (delta_N_eff = 1.34, excluded) and non-additive (modified Friedmann equation normalization, potentially consistent) is a straightforward calculation from the q-theory field equations. This gates the sole surviving CC mechanism.

---

## Section 4: Connections to Framework

### 4.1 The Transit IS a Bogoliubov Problem

The framework's cosmogenesis -- a supersonic transit through the van Hove fold in the spectral action -- maps directly onto the standard Bogoliubov particle creation problem (Parker [01], Birrell-Davies [02]). The time-dependent frequency omega_k(tau) is provided by the spectral action's tau-dependence. The Bogoliubov transformation connects the pre-transit vacuum (adiabatic ground state at tau < tau_fold) to the post-transit excited state (GGE relic at tau > tau_fold). The particle number N_k = |beta_k|^2 determines the GGE occupation numbers. The power spectrum of the produced excitations determines the primordial perturbation spectrum. This is the universal structure underlying all transit dynamics, whether in cosmological particle production, BEC quench dynamics, or the framework's spectral transit.

### 4.2 The Acoustic White Hole as Sonic Horizon

The framework's acoustic white hole (pre/post-transit causally disconnected by supersonic flow) is precisely the construction of Unruh [12] and Barcelo-Liberati-Visser [08]. In a flowing superfluid, when the flow velocity exceeds the sound speed, a sonic horizon forms. The framework's Mach 13.75 transit creates an acoustic white hole: perturbations generated inside the transit region cannot propagate upstream against the supersonic flow. The Hawking temperature of this acoustic horizon is T = hbar * kappa / (2 pi k_B), where kappa is the surface gravity (rate of change of flow velocity at the horizon). Steinhauer [09] has experimentally validated this in BEC. The framework's acoustic white hole is a specific instance of the Barcelo-Liberati-Visser universality class.

### 4.3 GGE Permanence as Prethermalization Plateau

The framework's Ordered Veil (GGE relic that never thermalizes) is the permanent prethermalization plateau of Berges [10] in the integrable limit. In non-integrable systems, the prethermalization plateau is a transient that eventually decays to thermal equilibrium on a timescale t_therm ~ exp(c/eps^2) (Bertini-Essler, W8-B). In integrable systems, the plateau IS the final state -- the GGE (Rigol [13]). The framework's BCS pairing Hamiltonian is integrable (Richardson-Gaudin), so the prethermalization plateau is permanent. The 10^580 t_universe thermalization time confirms this: the system will never reach thermal equilibrium. The GGE relic is the universe's permanent non-equilibrium state.

### 4.4 Volovik [27] as Parent System, Not Analog

Volovik's superfluid 3He [27] is the parent system for the framework's transit dynamics. The framework inherits the structure: BCS pairing (gap equation), Bogoliubov quasiparticles (excitations above the condensate), acoustic metric (emergent from condensate flow), and GGE formation (integrable quasiparticle dynamics). The Volovik CC relaxation (rho ~ M_Pl^2 H^2) is the superfluid's thermodynamic approach to equilibrium, transferred to the fabric. This is not analogy -- it is inheritance (3He-B is the parent; the fabric is the child).

---

## Section 5: Open Questions

### 5.1 What is the Correct Mode Equation Through the Van Hove Fold?

The standard Mukhanov-Sasaki equation u_k'' + (k^2 - a''/a) u_k = 0 assumes a single scalar field driving the expansion, with a(tau) determined by the Friedmann equation. In the framework, the expansion is not geometric volume change but spectral complexity growth. The effective "scale factor" is determined by the spectral action S(tau), not by the standard Friedmann equation. What is the correct mode equation? If it is the Mukhanov-Sasaki equation with a(tau) replaced by an effective scale factor from S(tau), the computation is straightforward. If the spectral action's non-standard kinetic structure modifies the mode equation itself, the problem is more involved.

### 5.2 Does the Acoustic White Hole Transfer Perturbations Across the Scale Gap?

The 54-decade gap between k_transit and k_CMB cannot be bridged by the 0.66 e-fold transit. The acoustic white hole resolves the horizon problem for scalar perturbations through GGE acoustic correlations. But does this mechanism also transfer TENSOR perturbations? The W3-C result shows that the blue tensor tilt does not reach CMB scales through the standard transfer function. Does the acoustic channel provide an alternative? This requires computing the tensor Bogoliubov coefficients in the acoustic metric, not just the scalar ones.

### 5.3 What Determines the Bogoliubov Coefficients' k-Dependence?

In standard inflation, the k-dependence of |beta_k|^2 is set by the slow-roll parameters at horizon crossing. In the framework's impulsive transit, the k-dependence is set by the transit profile: the functional form of omega_k(tau) through the fold. The van Hove singularity (divergent density of states) introduces a specific k-dependence that has not been computed. The mode equation through a van Hove fold is a well-defined mathematical problem -- it is the same problem as computing the tunneling probability through a classically forbidden region with a critical point (Schwinger [14], proper-time method). The WKB connection formula across the turning point determines |beta_k|^2.

### 5.4 Is the P_exc = 1.000 Saturation Exact or Approximate?

The Landau-Zener excitation probability P_exc = 1 - exp(-2 pi delta^2 / (hbar v)) saturates to 1.000 at Mach 13.75. This means EVERY mode is fully excited -- the sudden-quench limit. But the Landau-Zener formula is derived for a two-level system with linear sweep. The framework's transit through the van Hove fold is NOT a linear sweep (the density of states diverges at the fold). The multi-level Landau-Zener problem through a singularity may produce different occupation numbers. This needs verification through the exact mode equation.

### 5.5 Can Parametric Resonance Enhance or Modify the GGE Relic?

In preheating [04], the oscillating inflaton drives parametric resonance that exponentially amplifies certain modes. If the framework's post-transit state has ANY oscillatory component (e.g., oscillations of tau around the equilibrium), the mode equation acquires a Mathieu-type structure and Floquet instability bands could appear. The Bertini-Essler result (no Lyapunov divergence, quadratic potential) suggests this does not happen -- the potential is harmonic, not anharmonic. But the 27 unstable TT directions at the fold could, in principle, produce oscillations whose decay drives parametric amplification. The timescale comparison (tau settling in 10^{-47} yr vs. Hubble time) suggests this is negligible, but the Floquet analysis has not been performed.

---

## Section 6: Computation Suggestions Summary

| # | Computation | Method | Input | Gate | Priority |
|:--|:-----------|:-------|:------|:-----|:---------|
| 1 | **TRANSIT-MODE-EQ-67**: Solve mode equation through van Hove fold | Numerical ODE (RK4/5) through fold region, extract beta_k | S(tau) at 16 points, Mach 13.75, omega_k(tau) per sector | PASS: |alpha_s| < 0.015. FAIL: > 0.030 | CRITICAL |
| 2 | **SUDDEN-APPROX-SPECTRUM-67**: Sudden-approximation power spectrum | Analytic: Eq. 6 with pre/post frequencies from D_K spectrum | omega_k^{before}, omega_k^{after} for all PW sectors | INFO: cross-check of computation 1 | HIGH |
| 3 | **TRANSFER-MATRIX-TRANSIT-67**: Transfer matrix decomposition | WKB in adiabatic regions, numerical through fold, 2x2 matching | S(tau) profile, turning point locations | INFO: semi-analytic understanding of n_s, alpha_s drivers | HIGH |
| 4 | **KZ-FROZEN-SPECTRUM-67**: Kibble-Zurek frozen-in power spectrum | KZ formula with z=2, Mach 13.75, CG(24) dispersion | Dynamic exponent z=2 (S63), quench rate, dispersion | PASS: |alpha_s^KZ| < 0.015. FAIL: > 0.030 | HIGH |
| 5 | **BBN-VOLOVIK-67**: Volovik delta_N_eff at BBN | q-theory Friedmann equation at T_BBN | W1-A rho_vac(T), BBN constraints | PASS: delta_N_eff < 0.4. FAIL: > 1.0 | CRITICAL |
| 6 | **FLOQUET-POST-TRANSIT-67**: Floquet analysis of post-transit oscillations | Mathieu/Hill equation for tau oscillations coupling to modes | S62 Hessian, TT directions, tau settling rate | PASS: no instability bands above Hubble rate | MEDIUM |
| 7 | **ACOUSTIC-TENSOR-TRANSFER-67**: Tensor Bogoliubov coefficients through acoustic white hole | Mode equation in BLV acoustic metric for GW modes | Acoustic metric parameters, GGE dispersion | INFO: does blue tilt propagate acoustically? | MEDIUM |
| 8 | **MULTI-LEVEL-LZ-67**: Multi-level Landau-Zener through van Hove singularity | Exact numerical solution of coupled-level system through fold | D_K spectrum at fold, transit velocity profile | INFO: verify P_exc saturation in multi-level case | LOW |

---

## Closing Assessment

The phonon-exflation framework is, from the transit dynamics perspective, a well-posed Bogoliubov problem that has not yet been fully solved. The structural ingredients are all present: a time-dependent frequency omega_k(tau) from the spectral action, a supersonic transit through a van Hove singularity, Bogoliubov pair production with P_exc = 1.000, an integrable post-transit Hamiltonian producing a permanent GGE relic, and a Volovik-type vacuum relaxation mechanism for the cosmological constant. The integrability tower is the most complete I have encountered in any framework, and the Leggett-only DM result (0.6% from Planck, z_eq confirmation at 0.88 sigma) is a genuine zero-parameter match that survives independently of the spectral functional choice.

The critical gap is the COMPUTATION of the power spectrum from the exact mode equation. Every observable that the framework is being tested against -- n_s, alpha_s, r, the tensor tilt -- follows from the Bogoliubov coefficients of the transit. The slow-roll formulas used to date are not merely approximate; they are categorically inapplicable at Mach 13.75 with eta_H ~ O(1). The 5-sigma alpha_s tension is most likely an artifact of this misapplication, but "most likely" is not "proven." The proof requires solving the mode equation. This is the single computation that will either validate or falsify the framework's CMB predictions.

The FUNCTIONAL-INDEPENDENT results (Volovik CC, Leggett DM, integrability, BCS-Sakharov decoupling, Higgs mass convergence) constitute a structurally rich skeleton that does not depend on the spectral functional choice. The SCHEME-DEPENDENT results (n_s, alpha_s, eps_H sign) await resolution through the spectral functional selection problem. From my perspective, the most promising route to selecting the functional is the BCS free energy approach (Volovik, Phonon-First in the master synthesis): the microscopic BCS partition function F(tau) = -T ln Tr exp(-beta H_BCS) determines eps_H without ambiguity, bypassing the cutoff function entirely. This is how superfluid 3He works -- the effective Lagrangian is derived from the microscopic BCS theory, and no spectral functional ambiguity exists.

The framework's transit dynamics is structurally identical to Bogoliubov pair creation in analog gravity (Barcelo-Liberati-Visser [08]), Kibble-Zurek defect formation in rapid quenches (del Campo-Zurek [11]), and GGE formation in integrable quantum systems (Rigol [13]). These are not analogies -- they are the same mathematics. The mode equation, the Bogoliubov coefficients, and the GGE relic are universal structures that the framework inherits from its integrable BCS dynamics. The framework's transit through the van Hove fold is a specific instance of a well-understood universality class. The tools to solve it exist. The computation must now be performed.
