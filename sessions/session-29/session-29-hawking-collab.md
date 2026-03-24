# Hawking -- Collaborative Feedback on Session 29

**Author**: Hawking
**Date**: 2026-02-28
**Re**: Session 29 Results

---

## Section 1: Key Observations

Session 29 is the first session in this program where the mathematics fought back and won. Twenty-one mechanisms were closed by the structural walls of the constraint map -- every one a single-particle spectral functional blocked by A-01, A-04, A-06, or S-01. What survived is a many-body BCS condensation: the one class of physics that lives outside the domain of those walls. This is not a coincidence. It is the proof by exhaustion that the walls were correctly identified.

From my specialist perspective -- semiclassical gravity, particle creation, thermodynamics of spacetime -- several features of Session 29 stand out with particular sharpness.

### 1.1 The Anti-Thermal Spectrum Is the Correct Physics

The 29c-1 computation confirmed what the Bogoliubov formalism demands: parametric particle creation on a compact manifold with discrete eigenvalues produces resonance patterns, not thermal spectra. B_k positively correlated with omega (Pearson r = +0.74 at tau = 0.50) is the signature of the Parker mechanism (Paper 05, eq. for greybody factors, applied to the internal space rather than a black hole horizon). The anti-thermal character -- higher-energy modes more populated than lower-energy modes -- distinguishes this categorically from Gibbons-Hawking radiation (Paper 07, T_dS = H/(2pi)).

This distinction matters for a precise structural reason. The Gibbons-Hawking effect (Paper 07) requires a causal horizon: an observer-dependent thermality arising from tracing over inaccessible degrees of freedom behind the horizon. The Minkowski vacuum appears thermal to a Rindler observer because the Rindler wedge is causally disconnected from its complement (Paper 12, thermofield double construction). SU(3) is compact, has no boundary, no trapped surface, no event horizon. There is no causal structure to generate thermality. The particle creation is kinematic -- driven by the time dependence of the background geometry -- not thermodynamic. The Bogoliubov coefficients (Paper 05, |beta|^2/|alpha|^2 = exp(-2pi*omega/kappa)) reduce to the thermal ratio ONLY when there is a horizon with constant surface gravity kappa. When the geometry is time-dependent and horizonless, the ratio is mode-dependent and non-thermal.

The self-correction on the T_GH formula (replacing e^{-2tau}/pi with H_internal/(2pi) = (4/3)*dtau_dt/(2pi)) is an improvement but does not change the verdict. Even with the corrected formula, the spectrum SHAPE is non-thermal (R^2 = -72.3). A single-point temperature match (T_GH ~ 0.465 vs T_eff ~ 0.469 at tau = 0) is not evidence of thermality -- it is a numerical coincidence between a characteristic geometric frequency and the mean of a non-thermal distribution.

### 1.2 The Entropy Balance Is Genuinely Significant

The K-29b PASS (R_min = 1.53 at tau = 0.20, Delta S_total = +660) resolves what I identified in Session 25 as TH-01: spectral entropy S_spec monotonically decreasing at all temperatures. The particle creation entropy (sum_k B_k * omega_k * ln(1/B_k)) exceeds the spectral entropy cost at every tau, with 53% margin at the tightest point. This is the generalized second law in action -- not the GSL of black hole thermodynamics (which requires a horizon area term), but the ordinary second law applied to the combined system of spectral modes and created particles.

The distinction between ordinary second law and GSL is physically important and I am glad that Einstein's correction from Session 28 (Synthesis B, C-6) was incorporated. There is no horizon on SU(3), so there is no A/(4G) term. The relevant thermodynamic condition is simpler: the entropy of the matter sector must not decrease. It does not. This removes entropy as a potential barrier to modulus evolution.

### 1.3 The Jensen Saddle Is a Pomeranchuk Instability

The B-29d result (2/4 transverse Hessian eigenvalues negative at the BCS minimum) is classified as REDIRECT, not CLOSURE, and I concur with this classification. But the physics deserves emphasis. The BCS condensate prefers a geometry with smaller lambda_min (deeper gap, stronger pairing). The spectral action alone prefers the round metric (tau = 0). These are competing thermodynamic potentials -- precisely the situation that generates a Pomeranchuk instability in condensed matter: the interacting system favors a different configuration than the non-interacting system.

The connection to black hole thermodynamics is structural. A Schwarzschild black hole has negative heat capacity (Paper 04: C = -8pi G M^2 k_B / (hbar c)). The round-metric SU(3) also has negative specific heat (TH-02: I_E monotonically decreasing). In both cases, the system is thermodynamically unstable to spontaneous formation of a condensed phase -- the black hole forms from gravitational collapse, the BCS condensate forms from the modulus instability. The Jensen saddle says that once the condensate forms, it redirects the geometry toward the U(2)-invariant family where condensation is deeper. This is the BCS condensate carving out its own potential well -- a bootstrapping mechanism where the order parameter reshapes the geometry that supports it.

### 1.4 The Scale Bridge Problem Is Universal

The k_transition = 9.4e+23 h/Mpc result (29c-2) and f_peak = 1.3e+12 Hz result (29c-4) are not failures of the phonon-exflation framework. They are structural properties of ANY Kaluza-Klein compactification at M_KK >> eV. The scale bridge problem -- that GUT-epoch transitions imprint at microscopic comoving distances because the Hubble horizon at GUT energies is microscopically small -- is the same reason we cannot directly observe Hawking radiation from stellar-mass black holes (Paper 04: T_H ~ 6e-8 K for M_sun, below the CMB). The theory is calculationally correct; the signal is structurally inaccessible. This is a limitation of the observation channel, not the physics.

The M_KK-independence of f_peak is a genuine structural result that deserves attention. The GW peak frequency is set by the Planck scale, not the KK scale, because the product (beta/H) * T_* is M_KK-independent. This is analogous to the universality of Hawking radiation: T = kappa/(2pi) depends only on the surface gravity, not on the details of the collapsing matter (Paper 05, universality). Here, f_peak depends only on the Planck mass, not on the KK mass.

---

## Section 2: Assessment of Key Findings

### 2.1 The Constraint Chain: Sound, With One Sensitivity

KC-1 through KC-5 all pass. The weakest link is the trapping margin: E_mult <= ~1.5 for capture by L-9 latent heat, with 20% sensitivity between not-trapped (1.0x) and trapped (1.2x). This is genuinely marginal. The CDL tunneling backup does not exist (V_eff monotone, CDL inapplicable -- my computation 29c-3 confirmed this after the bug fix retracted the initial PASS). Overshooting trajectories are not recaptured.

Whether the DNP instability (D-03) launches the modulus within the trapping window is the principal remaining unknown. This is not a fine-tuning problem -- E_crit/V(0) = 1.52 is order-unity -- but it is a sensitivity that the current 1D backreaction ODE does not resolve. The dissipative trajectory computation (Session 30 Thread 5 in the wrapup) is the correct diagnostic.

### 2.2 The Gaussian Correction: Reassuring

Gi = 0.36 (singlet), 0.014-0.028 (multi-sector). The ~13% one-loop correction with no sign reversal confirms mean-field reliability. This is the BCS analog of the statement that the semiclassical approximation works when the entropy is large (Paper 05, discussion of back-reaction). Here the "entropy" is the number of gap-edge modes (n_gap = 37.3), which plays the role of the Bekenstein-Hawking entropy in controlling the validity of the mean-field approximation.

### 2.3 The PMNS Extraction: Partial Contact

sin^2(theta_13) = 0.027 (PDG: 0.022, 23%) is a partial success. The tridiagonal texture with V(L1,L3) = 0 exactly (selection rule from Kosmann anti-Hermiticity) is a structural prediction: the Dirac operator forces nearest-neighbor coupling in the eigenvalue ladder, which automatically generates theta_12 >> theta_13. This is the correct qualitative hierarchy. But theta_23 = 14 degrees (PDG: 49.1 degrees, factor 3.5x off) and R = 0.29 (PDG: 32.6, 112x shortfall) show that the singlet-sector effective mass matrix is insufficient. The escape route -- mode-dependent BCS dressing -- is physically well-motivated (non-uniform Delta_n breaks the constraint that theta_13 and theta_23 cannot be independently tuned) but untested.

### 2.4 The Weinberg Angle Convergence: Conditional and Pre-Registered

The T2 instability direction simultaneously deepens BCS and moves sin^2(theta_W) toward the SM value (0.198 -> 0.231 at eps_T2 = 0.049). This is structurally suggestive -- two independent physics requirements aligning along one geometric direction -- but correctly flagged as conditional on the V_total landscape. P-30w (sin^2(theta_W) in [0.20, 0.25] at the off-Jensen minimum) is the pre-registered gate. I endorse this gate as the decisive next test.

---

## Section 3: Collaborative Suggestions

### 3.1 Sector-Resolved Adiabaticity Map on Fine Grid

The 29c-1 computation lumped 11,424 modes from 10 Peter-Weyl sectors into a single Bose-Einstein fit. This obscured the real physics. The sector-resolved data showed that (3,0)/(0,3) sectors have the least negative R^2 -- precisely the BCS-active sectors from L-9.

**Proposed computation**: For each Peter-Weyl sector (p,q), compute the mode-resolved adiabaticity parameter

    eta_n(tau) = lambda_n(tau) / |d(lambda_n)/d(tau)| * (1/v_modulus)

where v_modulus = d(tau)/dt from the 29b-2 ODE solution. Map the tau values where eta_n < 1 for each mode. Overlay with the BCS transition point tau ~ 0.35-0.50.

The modes where eta_n < 1 are the "resonantly amplified" modes. If these cluster at the gap edge in the (3,0)/(0,3) sectors, the Parker injection is PRECISELY targeted at the BCS-relevant modes. This would upgrade KC-1 from "injection occurs" to "injection is spectrally optimized for BCS."

**Data**: Already exists in s28a_bogoliubov_coefficients.npz (omega, B_k at 21 tau points) and s23a_eigenvectors_extended.npz (eigenvalues at 9 finer tau points). Interpolation on the fine grid gives ~0.025 tau resolution in the BCS window.

**Connection to my papers**: This is the direct application of Paper 05 (Bogoliubov transformation) to the internal space. The mode-resolved adiabaticity parameter is the internal-space analog of the greybody factor Gamma_l(omega) (Paper 05, effective potential V_l(r)): it determines which modes escape the adiabatic regime and are produced as particles.

### 3.2 Thermodynamic Partition Function on U(2)-Invariant Surface

In Session 16 (Round 2a), I identified the mathematical identity V_CW = Helmholtz free energy F = U - TS. The spectral action Tr f(D^2/Lambda^2) on a compact geometry IS the Euclidean path integral (Paper 07, Gibbons-Hawking: I_E = -pi r_H^2/G for de Sitter) evaluated on that geometry. The spectral action is the partition function.

**Proposed computation**: On the 2D U(2)-invariant grid search (Session 30 Thread 1), compute not just V_total but also the thermodynamic decomposition: U(tau, eps_T2) and T*S(tau, eps_T2) separately. The minimum of F = U - TS occurs where dU/d(tau) = T * dS/d(tau) -- entropy maximization subject to the energy constraint. If the U(2)-invariant minimum coincides with a local entropy maximum in the S landscape, the thermodynamic interpretation of the BCS condensation becomes fully self-consistent.

This is zero additional computational cost on top of Thread 1: the eigenvalues are already being computed, and U and S are simple sums over the spectrum with different weighting functions.

**Connection to my papers**: Paper 03 (Bardeen-Carter-Hawking: first law dM = (kappa/8pi)dA + Omega_H dJ + Phi_H dQ). In the KK context, the modulus tau is an additional thermodynamic variable and the first law acquires a moduli work term: dM = (kappa/8pi)dA + ... + P_tau d(tau), where P_tau = -dF/d(tau) is the "pressure" conjugate to the modulus. At the BCS minimum, P_tau = 0 -- thermodynamic equilibrium. The off-Jensen deformation adds further work terms.

### 3.3 Information Content of the Frozen BCS State

The framework's testable content lives in the frozen BCS ground state. From the information-theoretic perspective (Papers 06, 10, 13, 14), the BCS condensation is an information-theoretic event: the modulus degrees of freedom (which carry information about the initial conditions) are entangled with the condensate degrees of freedom (which determine the frozen observables). The question "does the frozen state uniquely encode the initial conditions?" is the internal-space version of the information paradox.

**Proposed analysis**: Compute the entanglement entropy between the modulus trajectory and the BCS condensate at the trapping point. Specifically: treat the 3-sector BCS state |Psi> as a bipartite system with the modulus in subsystem A and the condensate order parameters (Delta_1, Delta_2, Delta_3) in subsystem B. The reduced density matrix rho_B = Tr_A |Psi><Psi| has an entropy S_ent that quantifies how much information about the initial conditions is encoded in the frozen state.

If S_ent is large (comparable to n_gap * ln(2) ~ 5 bits), the frozen state retains significant information about the pre-BCS trajectory. If S_ent is small, the BCS transition is a thermodynamic eraser -- it produces a frozen state independent of initial conditions. The latter would be more predictive (fewer initial-condition dependencies in the observables) but raises a version of the information paradox: where did the modulus information go?

**Connection to my papers**: Paper 13 (Page: the Page curve benchmark). The relevant analog is: does the "radiation" (the frozen observables like g_1/g_2, sin^2(theta_W), mass ratios) carry enough information to reconstruct the "black hole interior" (the initial conditions at tau = 0)? If the BCS transition is first-order, there is a sense in which the Page time is zero -- all information is released instantaneously at the transition, not gradually. This would be the opposite of the Hawking radiation scenario where information leaks out slowly over a scrambling time.

### 3.4 Internal-Space Penrose Diagram (Modulus Mini-Superspace)

I proposed in the 29Ac workshop the concept of a "modulus mini-superspace diagram" (distinct from a Penrose diagram, since there is no causal structure being modified). The idea is to represent the modulus trajectory in a conformal diagram where the tau axis is the internal geometry and the t axis is cosmic time.

**Proposed visualization**: Plot the (tau, t) trajectory with the following features marked:
- The DNP instability at tau < 0.285 (the "initial singularity" analog -- replaced by the round metric as the no-boundary proposal replaces the Big Bang singularity, cf. Paper 09)
- The BCS transition surface at tau ~ 0.35-0.50 (the "phase boundary" -- analog of the black hole event horizon, but a phase boundary rather than a causal boundary)
- The trapping region (KE < L for E_mult <= 1.5)
- The decompactification region (KE > L, modulus escapes)

This diagram would provide geometric intuition for the trapping margin sensitivity -- the 20% window between trapped and untrapped trajectories would be visible as the narrow neck between the trapping region and the escape cone.

**Connection to my papers**: Paper 09 (Hartle-Hawking: no-boundary proposal). The round metric tau = 0 is triple-selected as the initial condition (Weyl curvature hypothesis + J-maximality + DNP instability). The no-boundary proposal says the universe has "no boundary" -- the South Pole of the Euclidean cap. In the phonon-exflation framework, tau = 0 (the round metric) plays the same role: it is the maximally symmetric initial condition from which the modulus is expelled by instability, not arrived at from some prior state.

### 3.5 Recompute 29c-3 (CDL) as Arrhenius Thermal Stability

The CDL computation was correctly identified as inapplicable (no barrier, V_eff monotone). But the physical question it was trying to answer -- "is the BCS condensate stable against thermal fluctuations?" -- is still valid. The correct formalism is not CDL tunneling but Arrhenius thermal activation:

    Gamma_escape = omega_0 * exp(-Delta F / T_eff)

where Delta F is the free energy barrier for destroying the BCS condensate and T_eff is the effective temperature of the system post-transition.

**Proposed computation**: At the BCS minimum (tau ~ 0.35, mu/lambda_min ~ 1.20), compute:
1. The BCS free energy depth |F_BCS| = 5.63 (from 29b-1)
2. The effective post-transition temperature T_eff from the latent heat distributed among radiation degrees of freedom (g_* = 106.75)
3. The Arrhenius suppression factor exp(-|F_BCS|/T_eff)

If |F_BCS|/T_eff >> 1, the condensate is thermally stable. The CDL computation inadvertently computed something close to this (B ~ 1.5e+11 implies enormous suppression), but the correct framework is thermal activation in the BCS phase, not quantum tunneling through a non-existent barrier.

---

## Section 4: Connections to Framework

### 4.1 Spectral Action = Euclidean Path Integral = Thermodynamic Partition Function

This three-way identity, first articulated in Giants G3 (three-way identity: S_CC ~ I_E, I_E[saddle] = -S_dS), is now computationally confirmed at every level of Session 29:
- The spectral action Tr f(D_K^2/Lambda^2) gives V_eff (29b-1)
- The Euclidean action I_E is monotonically decreasing (TH-02, confirmed by 29b-1 extension to BCS)
- The BCS free energy F_BCS = U - TS is the condensate contribution (29Ab)
- The total V_total = V_spec + F_BCS is the full partition function

The BCS minimum in V_total is thermodynamic equilibrium: the point where the system's free energy is minimized, entropy is maximized subject to the energy constraint, and no spontaneous evolution occurs. This is exactly the first law of black hole mechanics (Paper 03) with the modulus replacing the horizon area as the thermodynamic variable.

### 4.2 Parker Creation = KC-1 = Bogoliubov Universality

The Bogoliubov transformation connecting "in" and "out" vacua (Paper 05, the founding derivation) is the SAME mathematical structure as KC-1's parametric injection. The key result from Paper 05 -- that the thermal ratio |beta|^2/|alpha|^2 = exp(-2pi*omega/kappa) depends only on the surface gravity kappa and spin, not on collapse details -- has an internal-space analog: the Bogoliubov coefficients on Jensen-deformed SU(3) depend only on the eigenvalue trajectory lambda_n(tau) and the modulus velocity, not on the microscopic details of the spectral triple.

This is precisely what H-5 (trans-Planckian universality, confirmed at Spearman rho >= 0.93 in Session 25) established: modified UV cutoffs do not change the particle creation spectrum. The universality that protects Hawking radiation from trans-Planckian corrections also protects the phonon-exflation particle creation mechanism.

### 4.3 First-Order Trapping = Hawking-Page Analog

The L-9 first-order BCS transition is the condensed-matter analog of the Hawking-Page transition (Paper 10: the exchange of dominant saddle points in the Euclidean path integral). In the Hawking-Page transition, thermal AdS (no black hole) dominates at T < T_c, while the black hole geometry dominates at T > T_c. In the phonon-exflation transition, the uncondensed phase (modulus rolling) dominates at tau < tau_BCS, while the condensed phase (BCS ground state) dominates at tau > tau_BCS.

The parallel is not exact -- I retracted the "identity" claim in Session 26 and downgraded to "partial structural parallel" after finding that b = +0.41 (second-order in the single-sector GL expansion, first-order only through the L-9 cubic invariant). But the structural resemblance persists: both transitions involve a discontinuous change in the dominant saddle of the partition function, with latent heat release and irreversible trapping. The BCS condensate is more stable than the uncondensed modulus rolling, just as the large black hole is more stable than thermal AdS above T_c.

### 4.4 The Information Question for Frozen-State Predictions

From my information-theoretic perspective (Papers 06, 10, 13, 14), the frozen BCS state is an "information endpoint." The modulus trajectory -- which carries information about the initial conditions (round metric, DNP instability, modulus velocity) -- terminates at the BCS transition. The observables (g_1/g_2, sin^2(theta_W), mass ratios) are determined by the frozen geometry. The question is: how much of the initial-condition information survives in these observables?

If the BCS transition is first-order and unique (one minimum in the 3D U(2)-invariant space), then the frozen-state observables are INDEPENDENT of initial conditions -- they depend only on the condensate minimum. This would be the ideal scenario for predictivity: the framework makes zero-parameter predictions from geometry alone. The off-Jensen minimum search (Session 30 Thread 1) directly tests this.

If the U(2)-invariant landscape has multiple local minima, initial conditions determine which minimum the modulus falls into -- and the predictions become conditional on the trapping basin. This would be the "landscape problem" analog, requiring either a selection principle or a statistical approach.

---

## Section 5: Open Questions

### 5.1 Where Does the Spectral Entropy Go?

TH-01 establishes that S_spec is monotonically decreasing. K-29b establishes that particle creation compensates. But the question remains: at the BCS transition, where does the spectral entropy go? The modulus freezes, the eigenvalue spectrum stops evolving, and the BCS condensate locks in a specific configuration. Is the entropy stored in the condensate's phase fluctuations? In the Goldstone modes? In the quasiparticle excitations above the gap? A complete thermodynamic accounting of the BCS transition -- not just the free energy but the full entropy budget -- would determine whether the transition is entropy-preserving (second-order-like) or entropy-releasing (first-order, with latent heat).

### 5.2 Is There an Internal-Space Page Curve?

The BCS condensation entangles the modulus with the condensate order parameters. As the modulus approaches the transition, the entanglement entropy between "modulus" and "condensate" subsystems should grow (like the early phase of the Page curve, Paper 13). At the transition, one of two things happens:
- The entanglement entropy jumps to zero (the condensate is a pure state, independent of the modulus -- the "information is returned" scenario).
- The entanglement entropy saturates (the condensate retains memory of the modulus trajectory -- the "information is stored" scenario).

Computing this internal-space Page curve would determine whether the BCS transition is more like evaporation (information gradually released) or more like a measurement (information suddenly localized). The island formula (Paper 14: S_rad = min_I ext[A(dI)/(4G) + S_bulk(I+R)]) might have an analog here, with the BCS phase boundary playing the role of the quantum extremal surface.

### 5.3 What Sets the Modulus Velocity at the BCS Transition?

The trapping margin (E_mult <= ~1.5) depends on the modulus kinetic energy at the transition point. The DNP instability (D-03) launches the modulus, but the velocity at tau ~ 0.35-0.50 depends on the integrated friction from Parker back-reaction (KC-1) and Hubble damping (< 1% from 29b-2). The question is whether the combination of these dissipative effects naturally places the modulus in the trapping window, or whether trapping requires a specific initial condition that is not guaranteed.

This is the framework's version of the flatness problem: why is the modulus velocity at the transition "just right" for trapping? The answer might be that it is not fine-tuned -- E_crit/V(0) = 1.52 is order-unity, and the DNP instability provides E_total ~ 2V(0), placing the system naturally at E_mult ~ 1.3-1.5. But this needs to be verified by the dissipative trajectory computation.

### 5.4 Can the Multi-Peak GW Spectrum Serve as a Structural Fingerprint?

The GW spectrum from the L-9 first-order transition has 5 cusps corresponding to 5 irreducible representations entering the supercritical regime at different tau values. The relative spacing and amplitudes of these peaks are parameter-free structural predictions of the Peter-Weyl decomposition on Jensen-deformed SU(3). Even though the absolute frequency (f_peak ~ 10^12 Hz) is unobservable, the RELATIVE peak structure is a unique fingerprint.

If future technology (perhaps tabletop high-frequency GW detectors, or analog gravity experiments simulating the multi-sector BCS transition) ever reaches these frequencies, the 5-peak structure would be an unambiguous test. More immediately: can the peak structure be related to any LOW-energy observable through selection rules or sum rules? If the 5 sector-specific latent heats satisfy an identity that constrains the frozen-state gauge couplings, the GW spectrum would be indirectly testable through particle physics.

---

## Closing Assessment

Session 29 accomplished what the previous 28 sessions established was necessary: the confrontation of a many-body mechanism with the full spectral data, and its survival. The Constraint Chain passes. The backreaction is computed. The mean-field is reliable. The trapping is marginal but physically natural.

From my perspective, the deepest result is not any single gate verdict but the structural fact that the Bogoliubov particle creation spectrum is anti-thermal and sector-dependent. This is not a failure of the Gibbons-Hawking comparison -- it is the CORRECT physics of parametric amplification on a compact manifold with discrete eigenvalues. The Jensen-deformed SU(3) is a phononic crystal, and the particles are the sand grains at the antinodes. The BCS condensation is the moment the plate cracks.

The framework's observational content now lives in the frozen BCS ground state: gauge couplings, mass ratios, the Weinberg angle at the off-Jensen minimum. P-30w is the right next gate. If sin^2(theta_W) lands in [0.20, 0.25] at the thermodynamically selected minimum of the U(2)-invariant surface -- with no parameters adjusted -- then two completely independent physics requirements (condensed matter energetics and electroweak gauge structure) will have converged on the same point in moduli space.

The universe does not produce thermal spectra from parametric amplification on a compact manifold. It produces resonance patterns. The question is whether the particular pattern frozen by BCS condensation on Jensen-deformed SU(3) happens to be the one we observe.

The faucet does not negotiate. The mathematics falls where it falls.

---

*Filed by Hawking-Theorist. 14 papers consulted (Papers 03, 04, 05, 06, 07, 09, 10, 12, 13, 14 cited directly). Key computations reviewed: 29a-3 (entropy balance, authored), 29c-1 (Bogoliubov spectrum), 29c-2 (k_transition), 29c-3 (CDL bounce, bug-fixed), 29c-4 (GW spectrum). Five collaborative suggestions proposed, all grounded in existing data and zero/low computational cost.*
