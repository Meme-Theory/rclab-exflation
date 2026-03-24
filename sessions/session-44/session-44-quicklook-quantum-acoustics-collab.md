# Quantum Acoustics — Collaborative Feedback on Session 44

**Date**: 2026-03-15
**Reviewer**: quantum-acoustics-theorist
**Scope**: All 31 completed S44 computations, with focus on W1-5 (first-sound imprint), W3-1 (Fisher forecast), W3-2 (Bragg transfer), W5-3 (DOS evolution), W6-2 (second-sound attenuation)

---

## 1. Key Observations Through the Phonon/Acoustic Lens

Session 44 is the most acoustically productive session since S41 established that SU(3) under Jensen IS a phononic crystal. Five of my own computations landed, and the results from other agents intersect acoustic physics at multiple points. The overall picture that emerges:

**The substrate is an acoustically perfect medium.** Four independent results converge on this:

- Second sound undamped (Q_eff = 75,989; l_atten = 1.12e7 Mpc) -- W6-2
- Infinite thermal conductivity confirmed (ballistic transport, no Umklapp) -- inherited from S43 THERM-COND-43
- Domain walls acoustically transparent (|r| = 0.003-0.009 per wall, no Bragg) -- W3-2
- BCS gap stable across full transit (-1.63% variation over tau = 0 to 0.19) -- W5-3

This is not a collection of independent facts. It is a single structural feature: the SU(3) representation lattice is infinite and non-periodic (no reciprocal lattice, no Umklapp), the Jensen deformation preserves the [iK_7, D_K] = 0 symmetry (no intra-branch scattering within B2), and the system sits at T/Theta_D ~ 10^{-22} (zero normal fraction). All four results are different projections of the same algebraic structure.

**The two-sound system is now fully characterized.** First sound at c_1 = c propagates metric perturbations. Second sound at c_2 = c/sqrt(3) carries entropy/temperature oscillations. The coupling chain to 4D observables passes through the spectral action: delta_tau -> S[D_K(tau)] -> a_2(tau) -> G_N(t) -> H(t) -> delta_rho. This is the Landau two-fluid model realized on a Kaluza-Klein substrate, with the spectral action playing the role of the thermodynamic potential.

**Acoustic perfection creates a detection problem.** The very properties that make the substrate theoretically clean -- no damping, no scattering, no disorder -- also mean that the first-sound imprint is a KINEMATIC effect with no enhancement mechanisms. The amplitude is fixed at (c_2/c_1)^2 = 20.4% of BAO by forced-oscillator physics. No resonance, no amplification, no coherent buildup. This is why W3-1 returns SNR = 0.16.

---

## 2. Assessment of Acoustic/Phononic Computations

### W1-5: First-Sound Imprint Mechanism (FIRST-SOUND-IMPRINT-44) — PASS

**What was computed**: The full coupling chain from internal acoustic displacement to 4D density perturbation. The forced-oscillator amplitude A_1/A_BAO = (c_2/c_1)^2 = 0.2045 is derived from first principles: gravitational potential oscillation at omega = k*c_1 forces the baryon fluid at its natural frequency omega_nat = k*c_2.

**Assessment**: The mechanism is clean and the derivation is correct. Three points deserve emphasis:

(a) The amplitude is a RATIO of sound speeds squared. This is the standard result for a forced oscillator below resonance (c_2 < c_1), and it is independent of the absolute coupling strength da_2/dtau. The 2.35% gravitational fraction of dS/dtau is irrelevant to the amplitude ratio -- it only affects the absolute normalization, which cancels in A_1/A_BAO.

(b) The Steinhauer BEC cross-check (Paper [07] in the QA index) is the right analog. Two-speed systems in BEC experiments produce exactly this two-peak structure with the (v_slow/v_fast)^2 ratio. The framework prediction has experimental analog validation at the mechanism level.

(c) The r_1/r_s = c_1/c_2 = sqrt(3(1+R*)) = 2.211 identity is EXACT within the framework. It is not a fit parameter. The only input is R* = 0.63 (baryon-photon ratio at recombination), which is measured. This makes r_1 = 325.3 Mpc a parameter-free prediction.

**Concern**: The coupling chain has a bottleneck at step 3: da_2/dtau = 1461 with (da_2/dtau)/a_2 = 0.526. This is the fractional gravitational response to internal displacement. If a_2 has nonlinear dependence on tau (beyond the linear expansion used), the amplitude ratio could deviate from the simple (c_2/c_1)^2 formula. The spectral action's a_4/a_2 = 1000:1 hierarchy means the gravitational sector is a small perturbation on the total action -- but the perturbation is what couples to 4D. A second-order correction to the coupling chain should be computed in S45.

### W3-1: Fisher Forecast (FIRST-SOUND-44) — FAIL

**What was computed**: Full Fisher matrix forecast for DESI DR2, Euclid Y5, and combined surveys. The calibration correction is decisive: W1-5 used Eisenstein-Hu BAO amplitude (~25% wiggles in P(k)), while CAMB/CLASS gives ~5%. The true first-sound amplitude is 20.4% of 5% = 1.02% of P_smooth.

**Assessment**: The FAIL verdict is correct and the calibration correction is the key insight. The original SNR = 4.2 (W1-5) was based on an overestimate of the BAO oscillation amplitude by 5x. The corrected SNR = 0.16 is below cosmic variance for all current and planned surveys.

This is NOT a failure of the mechanism -- it is a failure of observability. The distinction matters. The mechanism produces a genuine feature at a predicted location with a predicted amplitude. The feature is simply too small to detect with V_eff < 10^4 Gpc^3.

**Acoustic perspective on the detection problem**: In any two-fluid system, the amplitude of the forced response scales as (omega_nat/omega_drive)^2 when omega_drive >> omega_nat. Here omega_drive/omega_nat = c_1/c_2 = 2.21, so the forced amplitude is suppressed by (1/2.21)^2 = 0.205. This is a KINEMATIC suppression -- there is no knob to turn. The only way to increase the amplitude would be to bring c_1 closer to c_2, which would require breaking Lorentz invariance of the spectral action. Since C-FABRIC-42 proves c_1 = c exactly, this is structurally forbidden.

**Pre-registration note**: The prediction specification (r_1 = 325.3 +/- 3.3 Mpc, A_1/A_BAO = 0.2045, matched filter in [305, 345] Mpc) is precisely what a theorist should do with a sub-threshold prediction. It sits in the archive waiting for a future survey. The V_eff = 8800 Gpc^3 requirement (35x DESI+Euclid) places this in the domain of next-next-generation surveys (post-2040 if at all).

### W3-2: Multi-Wall Bragg Transfer (COHERENT-WALL-44) — PASS (VACUOUS)

**What was computed**: Transfer matrix for 32 KZ domain walls, testing whether Bragg coherence enhances spectral filtration beyond single-wall evanescence.

**Assessment**: The VACUOUS verdict is the correct classification. The structural mismatch k_Bragg = 10.33 M_KK >> k_max ~ 2 M_KK means the Bragg condition is UNREACHABLE for any propagating mode. This is not a numerical accident -- it is the ratio of two independent scales: xi_KZ (set by transit dynamics) and 1/k_max (set by spectral geometry). No tuning can fix this because the scales have independent physical origins.

**Three acoustic lessons from this computation:**

(1) **Impedance matching**: |r| = 0.003-0.009 per wall means the impedance contrast is < 1%. In acoustic engineering, this is what you get when two media have nearly identical elastic moduli and density. The Jensen deformation with delta_tau = 0.01 between domains is a perturbation too small for significant reflection. The domain walls are acoustically invisible.

(2) **Anderson localization absent**: xi_loc/L_total > 1000 in the propagating band. The disorder (random domain sizes and tau values) is far too weak to localize. The mean free path l ~ 1900 M_KK^{-1} vastly exceeds the system size L_total = 4.86 M_KK^{-1}. This is consistent with the Q_eff = 75,989 from W6-2: the system is in the ballistic regime by many orders of magnitude.

(3) **Filtration mechanism confirmed as BCS gap**: All 431 decades of dynamic range come from evanescent decay in the BCS gap. This closes the multi-wall coherence route permanently and confirms that the BCS gap hardness (S43 DOS-43) is the SOLE filtration mechanism. For future work, the gap stability result from W5-3 (gap varies only -1.63% across the full transit) means this filtration is robust.

### W5-3: Phonon DOS at 5 tau Values (DOS-TAU-44) — INFO

**What was computed**: Full density of states evolution from tau = 0.00 (round SU(3)) to tau = 0.19 (near fold), tracking gap, bandwidth, van Hove singularities, degeneracy structure, and per-sector bandwidths.

**Assessment**: This is the most information-dense computation of the five acoustic tasks. Key structural features:

(a) **Degeneracy jump**: 62:1 -> 8.27:1 at tau = 0+. This is the acoustic signature of SU(3) -> U(1)_7 symmetry breaking. The jump is DISCONTINUOUS -- any nonzero Jensen deformation lifts the full SO(8) tangent-space symmetry down to U(1)_7, with the residual 8.27:1 ratio reflecting surviving Kramers-type degeneracies. In a phononic crystal, this is a crystallographic phase transition: from an isotropic medium (round metric, all directions equivalent) to a uniaxial crystal (Jensen metric, K_7 direction privileged).

(b) **Per-sector bandwidth hierarchy**: dBW/dtau follows C_2(p,q). This is the spectral statement that higher-Casimir representations couple more strongly to the Jensen deformation. Physically: modes with larger angular momentum on SU(3) are more sensitive to the anisotropy. This is analogous to how higher-order spherical harmonics on a sphere are more sensitive to oblateness.

(c) **Gap stability**: -1.63% over the full transit range. The gap floor is set by the (1,0)+(0,1) sector at tau > 0.05 (crossing from the (0,0) sector). This is a Lifshitz transition at the gap edge. The GAPPED nature is permanent -- no acoustic branch exists in the bare spectrum at any tau. The NG mode (acoustic branch) is a BCS condensate effect only, absent before and after the transit.

(d) **Van Hove count**: 9 -> 12 at tau = 0+. The three new singularities are created by the Jensen symmetry breaking. Combined with W6-8 (Van Hove tracking), the 12 trajectories show 8 rising, 4 falling, with a near-crossing at tau = 0.19 (T3-T5 approach within delta = 0.0008). This near-crossing is a potential second Lifshitz transition at tau ~ 0.20 -- this should be tracked with finer tau resolution in S45.

**Unresolved issue**: The n_vH = 12 at tau = 0.19 versus n_vH = 13 at tau = 0.20 (S43). One singularity emerges between tau = 0.19 and 0.20. This is consistent with the T3-T5 near-crossing: if two trajectories cross at tau ~ 0.195, a new van Hove singularity is created. Fine tau sampling in [0.19, 0.21] would resolve this.

### W6-2: Second-Sound Attenuation (2ND-SOUND-ATTEN-44) — INFO

**What was computed**: Effective quality factor and attenuation length for second sound (u_2 = c/sqrt(3)) at cosmological scales, with four independent arguments for undamped propagation.

**Assessment**: This is the computation I am most confident in from this session. The Q_eff = 75,989 and l_atten = 1.12e7 Mpc are built on four independent pillars, each of which would suffice alone:

(1) **Spatial separation** (l_mfp/L_SU(3) = 7.6): Internal phonons wrap the SU(3) manifold ~7.6 times before scattering. This is the INTERNAL quality factor. The coupling to 4D observables goes through the spectral action, a GLOBAL SU(3) integral. Mode redistribution within the internal space changes the spectral action only at O((V_3/E)^2) ~ 10^{-4}. This two-step argument (internal Q times spectral-action invariance) gives Q_eff = 7.6 / 10^{-4} ~ 76,000.

(2) **Spectral action invariance**: Normal scattering conserves total energy. The spectral action S = Tr f(D_K^2/Lambda^2) is a sum over ALL modes. Energy-conserving redistribution changes S at second order in the perturbation V_3. This is the acoustic analog of why the index of a Dirac operator is insensitive to smooth perturbations.

(3) **Vanishing Landau-Khalatnikov viscosities**: At T/Theta_D ~ 10^{-22}, the normal fraction rho_n/rho ~ exp(-Delta/T) ~ 10^{-88}. All five LK viscosity coefficients (eta, zeta_1, zeta_2, zeta_3, kappa) vanish. This is the superfluid He-4 story taken to its logical extreme: at temperatures 22 orders below the Debye temperature, the normal fluid simply does not exist.

(4) **GGE permanence**: The post-transit state is a generalized Gibbs ensemble with 8 Richardson-Gaudin conserved quantities. Integrability forbids thermalization. The source of second sound (the non-thermal GGE excitation spectrum) never degrades.

**The key lesson** (recorded in agent memory, S44): internal and external second sound are SEPARATE systems. The internal second sound on SU(3) is a thermal wave in the internal degrees of freedom. The external second sound (BAO) is a photon-baryon acoustic oscillation in 4D spacetime. They couple ONLY through the spectral action. Damping of the internal mode does not directly damp the external mode -- it changes the spectral action at second order, which then changes the 4D gravitational potential at second order. Two layers of quadratic suppression give (10^{-4})^1 ~ 10^{-4}, hence Q_eff ~ 10^4 not Q_internal ~ 10.

**Consequence**: Silk damping of the photon-baryon plasma remains the SOLE source of BAO damping. The framework predicts IDENTICAL BAO damping to LCDM. This is a necessary condition for viability -- any additional damping channel would be in tension with the precisely measured BAO scale.

---

## 3. Collaborative Suggestions

### 3.1 Acoustic Diagnostics for S45

**DOS fine scan at the Lifshitz transition**: The T3-T5 near-crossing at tau = 0.19 (W6-8) and the 12->13 van Hove count change between tau = 0.19 and 0.20 suggest a second Lifshitz transition at tau ~ 0.195. A fine tau scan in [0.19, 0.21] at 20 points would resolve the crossing topology (avoided vs true crossing). If it is a true crossing, it creates a new van Hove singularity with a specific DOS exponent that affects the Strutinsky shell correction.

**Nonlinear coupling correction**: W1-5 derives A_1/A_BAO = (c_2/c_1)^2 from a LINEAR forced-oscillator model. The spectral action a_2(tau) is computed at 7 tau values and the derivative da_2/dtau = 1461 is extracted by spline interpolation. If a_2(tau) has significant curvature (d^2a_2/dtau^2 != 0), the forced response acquires a correction of order (delta_tau/tau)^2 * (d^2a_2/dtau^2)/(da_2/dtau). This correction is probably small (the spectral action is smooth in tau) but should be computed to close the loop.

**Phonon-polariton coupling at the fold**: W6-6 (SPECTRAL-DIM-BAND-44) finds d_s(polariton) = 1.54 vs d_s(D_K) = 4.133 at sigma = 1.0. The polariton spectral dimension is structurally distinct from the geometric spectral dimension. This means low-energy quasiparticle physics and high-energy geometry decouple at a specific crossover scale. Identifying this scale precisely (where d_s(polariton) = d_s(D_K)) would pin the UV/IR crossover. From the comparison table in W6-6, the crossover is at sigma ~ 10 (d_s = 13.4 vs 15.4). This should be extracted with higher sigma resolution.

### 3.2 Papers to Cite

- **Steinhauer 2019** (QA Paper [07]): Experimental observation of Hawking radiation in BEC. The two-speed structure (condensate speed vs phonon speed) producing two correlation peaks is the direct experimental analog of c_1 vs c_2 in the framework. The (v_slow/v_fast)^2 amplitude ratio is confirmed.

- **Barcelo-Liberati-Visser 2011** (QA Paper [02]): The analogue gravity review. Section on two-fluid systems and acoustic metrics provides the mathematical framework for the first-sound/second-sound distinction. The effective metric g_{mu nu}^eff = (rho/c) * diag(-c^2, 1, 1, 1) is what the spectral action computes internally.

- **Volovik 2003** (QA Paper [03], Chapter 32): Two-fluid hydrodynamics in superfluid He-3/He-4. The Landau two-fluid model that the framework realizes. Specifically: the superfluid component (tau = condensate) carries the metric (first sound), while the normal component (quasiparticle excitations) carries entropy (second sound). The Q_eff = 75,989 comparison to He-4 Q ~ 3000 is the right benchmark.

- **Volovik 2023** (QA Paper [04]): Acoustic metric and emergent Planck constant. The c_s = c identification for the substrate speed of sound is derived independently by Volovik from the Akama-Diakonov-Wetterich tetrad approach. C-FABRIC-42 confirms this from the spectral action side.

- **Claeys et al. 2024** (QA Paper [09]): Integrability and decoherence in many-body systems. Directly relevant to the GGE permanence argument in W6-2. The Richardson-Gaudin integrability of the BCS sector maps onto their framework for understanding when and how integrable systems fail to thermalize.

- **Pellitteri et al. 2024** (QA Paper [08]): Phononic Casimir effect. The spectral-action-as-Casimir-energy interpretation is strengthened by their explicit calculation. The W1-4 trace-log CC result (5.11 orders transit suppression) has a direct analog in their phononic framework.

### 3.3 Phonon Computations for S45

1. **Phonon Green's function on SU(3)**: Compute G(omega, (p,q), (p',q')) -- the phonon propagator between irreps. This would give the FULL scattering matrix for internal acoustic modes, superseding the FGR-based estimates. The phonon self-energy Sigma(omega) from this propagator determines the true linewidth and level repulsion, resolving the FGR breakdown issue flagged in S43 (|V_rem|^2*rho/DeltaE^2 ~ 10^9 for B2-B2 scattering).

2. **Acoustic Casimir force between domain walls**: Two KZ domain walls separated by distance d experience a phononic Casimir attraction/repulsion. The W3-2 result (walls are acoustically transparent) means the Casimir force is small, but it should be computed: it determines whether the 32-cell tessellation is mechanically stable or tends to coarsen. Pellitteri et al. (QA Paper [08]) provide the formalism.

3. **Phonon contribution to G_N**: W1-1 (Sakharov) and W4-2 (bosonic induced G_N) both compute G_N from spectral sums. The PHONONIC contribution (quantized acoustic fluctuations about the Jensen metric) is a zero-point motion correction to the spectral action. This is the Debye-Waller factor for the phononic crystal. If the Debye-Waller factor DW = exp(-2W) deviates significantly from 1, the spectral action (which assumes a static metric) needs correction.

---

## 4. Framework Connections

### 4.1 Sakharov-Spectral Convergence (W1-1 + W4-2)

The most significant result of S44 from the acoustic perspective is the three-way G_N consistency: Sakharov induced gravity (W1-1, ratio 2.29), bosonic spectral action (W4-2, a_2^bos/a_2^Dirac = 61/20), and observation all agree within a factor of 3. This means the phononic crystal's spectral geometry, when fed through either the polynomial or logarithmic functional, produces the correct gravitational constant to within half an order of magnitude.

In phononic language: the elastic moduli of the SU(3) crystal, as encoded in the Dirac spectrum, produce the correct gravitational stiffness. The 992 KK modes are sufficient -- the Weyl asymptotics that Sakharov's formula relies on are already converged at max_pq_sum = 6. This is the analog of a phonon sum rule: the first spectral moment (a_2 coefficient) saturates at modest truncation because the high-energy tail contributes only power-law corrections.

### 4.2 CC Fine-Tuning Theorem and the CC (W5-5 + W6-3, CORRECTED)

The CC fine-tuning theorem (W5-5, corrected from "242-order Hausdorff impossibility" -- see Addendum below) establishes that no NATURAL (O(1)-width) cutoff function can give both G_N and Lambda_obs from the spectral action. A spike solution exists mathematically (width ~10^{-121}), but this IS the CC fine-tuning problem in functional-analytic form. The qualitative conclusion stands: the polynomial spectral action is wrong for the CC problem -- a result the acoustic perspective has been pointing toward since S41 (spectral action = phonon free energy, and the free energy of a phononic crystal with a hard gap is dominated by the gap energy, not the vacuum fluctuations).

The q-theory route (Volovik Papers 15-16) remains the only open CC mechanism. In acoustic language: the vacuum energy is not the zero-point sum of phonon modes (that gives M_KK^4 ~ 10^{120} Lambda_obs), but the thermodynamic response of the system to a constraint (Gibbs-Duhem relation). The trace-log functional (W1-4) is a step in this direction: it gives 5.11 orders of suppression during transit and rho_residual = 0 post-transit. Combined with the EIH singlet projection (W2-3, 4.25 orders) and the DM/DE thermodynamic ratio (W6-4, factor 2.7 from observed), the pieces are assembling.

### 4.3 CDM by Construction (W1-2)

The T^{0i} = 0 result for homogeneous GGE creation is an acoustic theorem: Schwinger pair creation at k_4D = 0 produces excitations with zero group velocity in the 4D directions. In phononic language: the KK quasiparticles are created at the Gamma point of the 4D Brillouin zone. They carry energy (T^{00} != 0) but no momentum (T^{0i} = 0). This is cold dark matter by construction -- no velocity dispersion, no free-streaming.

The domain wall correction v_eff = 3.48e-6 c comes from the finite spatial extent of the KZ domains. Quasiparticles created near domain walls have a small residual velocity from boundary effects. This is analogous to phonon scattering at grain boundaries in a polycrystalline solid -- it gives a tiny correction to the otherwise perfect CDM behavior.

### 4.4 Spectral Triple Emergence (W6-7)

The dissolution scaling epsilon_c ~ N^{-0.457} ~ 1/sqrt(N) -> 0 means the NCG spectral triple is an EFFECTIVE description valid at finite truncation. In the continuum limit (N -> infinity), any nonzero noise dissolves the spectral geometry. This is the acoustic statement that the phononic crystal is a regularization -- the discrete lattice (finite N) defines a spectral triple, but the continuum elastic medium (N -> infinity) does not. The spectral action is the finite-N effective theory, analogous to lattice QCD being the finite-N regularization of the continuum theory.

---

## 5. Open Questions

### 5.1 Is the Coupling Chain Complete?

The first-sound imprint chain (delta_tau -> S -> a_2 -> G_N -> H -> delta_rho) has six links. Each is derived from known physics (spectral geometry, Seeley-DeWitt, linearized GR). But the chain assumes LINEAR response at each step. The spectral action is nonlinear in tau (the eigenvalues are complicated functions of the Jensen parameter). The gravitational coupling (a_2 sector) is only 2.35% of the total dS/dtau. What is the second-order correction? Does the nonlinearity of S(tau) introduce higher harmonics in the first-sound spectrum that could be detectable even if the fundamental is below cosmic variance?

### 5.2 What Sets the Scale of the Normal Fraction?

The rho_n/rho ~ 10^{-88} estimate (W6-2) uses the thermal Boltzmann factor at T/Theta_D ~ 10^{-22}. But the GGE is NOT thermal -- it has 8 independent temperatures (W6-5). The effective normal fraction should be computed from the GGE occupation numbers, not from a single Boltzmann factor. If any of the 8 GGE temperatures is significantly higher than the CMB temperature (which is possible -- the GGE is non-thermal), the normal fraction could be larger than 10^{-88}. This would not change the qualitative conclusion (second sound undamped) but would change Q_eff quantitatively.

### 5.3 Can the Near-Crossing at tau = 0.19 Produce Observable Signatures?

The T3-T5 near-crossing (W6-8, delta = 0.0008) is a potential Lifshitz transition. If the crossing is AVOIDED (as generically expected from level repulsion), it creates a new topological feature: a van Hove singularity pair (one creation, one annihilation) that sweeps through the DOS as tau varies. This would produce a resonance in the pairing susceptibility chi_pp(omega) at the crossing frequency. Given that chi_pp already has the GPV pole (S37), a new resonance could modify the instanton dynamics. This is speculative but testable with a fine tau scan.

### 5.4 Does the Phonon Debye-Waller Factor Correct the Spectral Action?

The spectral action S[D_K(tau)] is computed at a FIXED metric (specific tau value). But the metric fluctuates -- the internal acoustic modes are quantized oscillations about the equilibrium geometry. The zero-point motion gives a Debye-Waller factor DW = exp(-2W) where 2W = <u^2> * k^2 is the mean-square displacement times the wavevector squared. If 2W is not negligible, the effective spectral action is S_eff = DW * S[D_K(tau)] + corrections. The Sakharov G_N (W1-1) and bosonic G_N (W4-2) both assume DW = 1 implicitly. Computing 2W from the phonon spectrum would quantify this correction.

### 5.5 The n_s Problem Remains Open

The acoustic computations do not address the spectral index problem. Lifshitz eta (W1-3) is CLOSED (eta_eff = 3.77, geometric not critical). Spectral dimension flow (W2-2) survives at sigma = 1.10 but has zero predictive dimension without a scale selection principle. Friedmann-BCS (W4-3) has epsilon_H = 2.999, structurally invariant. The first-sound mechanism provides no help: it predicts a feature at 325 Mpc but says nothing about the SLOPE of the primordial power spectrum.

From the acoustic perspective, n_s requires understanding HOW FAST modes are populated during the transit, not WHICH modes exist (W1-3 lesson F5). This is Bogoliubov coefficient physics, not equilibrium DOS physics. The Schwinger-instanton duality (S38) and the Parker-type cosmological particle creation picture should be the starting point for an n_s computation. The Bogoliubov coefficients beta_k for each KK mode, evaluated through the transit, give the primordial spectrum directly: P(k) ~ |beta_k|^2.

---

## 6. Closing Assessment

Session 44 advances the acoustic characterization of the SU(3) substrate from "phononic crystal identified" (S41) through "acoustic properties computed" (S42-S43) to "observational predictions fully derived and calibrated" (S44). The two-sound system is now complete: first sound at c (metric perturbations), second sound at c/sqrt(3) (entropy oscillations), with the coupling chain to 4D observables explicitly traced through the spectral action.

The honest assessment: the framework's most distinctive acoustic prediction (325 Mpc first-sound ring) is below the detection threshold of all current and planned surveys by a factor of ~20 in SNR. The amplitude is kinematically fixed at 1% of P_smooth and cannot be enhanced without breaking Lorentz invariance. This is a prediction that must wait for future observational capabilities.

The structural results are more durable. The CC fine-tuning theorem (W5-5, corrected) eliminates the polynomial spectral action route to the CC for any natural cutoff. The CDM-by-construction result (W1-2) makes the dark matter prediction unfalsifiable within the framework (T^{0i} = 0 is algebraic). The Sakharov G_N convergence (W1-1 + W4-2) demonstrates that the phononic crystal produces the correct gravitational constant from either functional form.

The constraint map after S44: G_N is explained (factor 2-3), DM is CDM by construction, the BAO damping matches LCDM, the tensor-to-scalar ratio is predicted below all foreseeable limits, and f_NL is safely Gaussian. The CC remains at 100+ orders from resolution, and n_s has no identified mechanism. These two problems -- the cosmological constant and the spectral index -- are where the next physics must come from. Neither is an acoustic problem; both require new dynamical input beyond the equilibrium phonon spectrum.

From the quantum-acoustics perspective, the SU(3) phononic crystal is now well-characterized. The next frontier is the DYNAMICS: how do the phonon modes evolve during the transit? What is the Bogoliubov transformation that connects the pre-transit vacuum to the post-transit GGE? What is the phonon self-energy in the interacting system? These are the computations that connect to n_s and to the CC through q-theory.

---

### Addendum: W5-5 Hausdorff Correction

**Date**: 2026-03-15 (post-collab audit)

**What changed.** The original W5-5 result claimed a "242-order Hausdorff impossibility theorem" -- that no positive decreasing cutoff function f could simultaneously yield f_2 ~ O(1) (for G_N) and f_4 ~ 10^{-121} (for the CC). The proof relied on a Hankel determinant condition from the Stieltjes moment problem. Team-lead audit found the moment ordering was wrong: the agent applied the Cauchy-Schwarz bound mu_0 * mu_2 >= mu_1^2 with the CC moment as mu_0 and the G_N moment as mu_1, but the natural Stieltjes ordering (dmu = f(u) du) places mu_0 = integral f du = f_2 ~ O(1) and mu_1 = integral f*u du = f_4 ~ 10^{-121}. In this correct ordering, mu_0 * mu_2 >= mu_1^2 gives mu_2 >= 10^{-242}/O(1), which is trivially satisfied. The impossibility evaporates.

**What survives.** A spike function with width epsilon ~ 10^{-121} and height M ~ 10^{+121} satisfies both moment constraints. This is a valid mathematical solution. But it IS the CC fine-tuning: the function f must be concentrated in an interval of measure 10^{-121} in dimensionless spectral variable space. No natural (O(1)-width) cutoff works. The verdict downgrades from "structural wall" to "fine-tuning theorem." The qualitative conclusion -- spectral action wrong for CC, q-theory needed -- is unchanged.

**Corrections to this review.** Section 4.2 has been updated inline. The original language ("structural wall," "definitive proof," "permanently eliminates") was too strong for a fine-tuning result. The correct framing: the polynomial spectral action route to the CC requires a cutoff function tuned to 121 digits. This is not an impossibility -- it is a naturalness problem. The distinction matters because fine-tuning problems can in principle be resolved by UV completion (the microscopic theory might PREDICT the spike), while impossibility theorems cannot.

**Acoustic analog of the spike cutoff.** The spike function f(u) ~ M * delta(u - u_0) with width epsilon ~ 10^{-121} has a direct acoustic interpretation: it is a phonon density of states consisting of a single mode at one specific frequency, with zero spectral weight everywhere else. In a phononic crystal, this corresponds to a PERFECTLY FLAT band -- a mode with identically zero group velocity at every wavevector, completely decoupled from all other modes. The SU(3) phononic crystal actually has such a structure: the B2 flat-band quartet (W = 0.058, ||V||/W = 2.59) is the closest physical realization. But the B2 band has finite width W/E_gap ~ 0.07, not 10^{-121}. The spike cutoff demands a band 10^{119} times flatter than B2.

This connects to a known result in phononic metamaterial engineering: acoustic systems with near-delta-function DOS require infinite-Q resonators (zero dissipation, zero coupling to the continuum). The SU(3) substrate satisfies the first condition (Q_eff = 75,989, ballistic transport, no Umklapp) but not the second -- the B2 modes couple to B1 and B3 through the 3-phonon near-resonance (omega_B2 ~ 2*omega_B1, 0.6% detuning, S43). To achieve width 10^{-121}, the B2 band would need to be a true bound state in the continuum (BIC) with coupling matrix element |V| < 10^{-121} M_KK. The actual coupling is |V|/W = 2.59 -- strong, not vanishing. The spike cutoff is as far from the physical phonon spectrum as possible while remaining mathematically legal.

**Volovik interpretation (unchanged).** In 3He-B, the analog of G_N (superfluid stiffness) and the analog of rho_Lambda (vacuum energy) arise from different thermodynamic derivatives of the partition function -- they are NOT moments of a single spectral cutoff. The superfluid stiffness is a second derivative (compressibility), while the vacuum energy vanishes by the Gibbs-Duhem identity (a zeroth-order thermodynamic statement). The spike cutoff is the spectral action's attempt to force two independent thermodynamic quantities into a single-function moment hierarchy. It works only if the function has no structure -- a delta function has no internal degrees of freedom to conflict. This is the functional-analytic shadow of the q-theory resolution: the vacuum energy is thermodynamic, not spectral.

**Constraint map update.** W5-5 moves from "structural wall (impossibility)" to "naturalness constraint (fine-tuning)." The polynomial spectral action route to the CC is not CLOSED but requires 121-digit tuning of the cutoff function shape. The q-theory route (Volovik Papers 15-16) remains the only natural CC mechanism. No other aspect of the S44 constraint map is affected.
