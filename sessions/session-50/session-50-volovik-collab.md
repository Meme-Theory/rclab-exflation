# Volovik -- Collaborative Feedback on Session 50

**Author**: Volovik Superfluid Universe Theorist
**Date**: 2026-03-20
**Re**: Session 50 Results -- The Leggett Propagator

---

## Section 1: Key Observations on My Computations

### W1-C (Bogoliubov Imprint): Trans-Planckian Erasure and the 3He Analog

The FAIL is correct and has a precise analog in superfluid 3He. In 3He-A, the order parameter has 18 real components (d-vector x l-vector x phase). When the superfluid is quenched through T_c into the normal state (Delta -> 0), all information about the d-vector and l-vector orientations is erased -- these are collective degrees of freedom of the condensate, not of the individual quasiparticles. The normal Fermi liquid retains only single-particle quantum numbers (momentum, spin). This is exactly what happens in the framework: the Leggett mode is a collective inter-sector phase oscillation of the BCS condensate. When the transit destroys the condensate (P_exc = 1.000, Delta = 0), the Leggett phase information is erased.

The deeper structural point from Paper 13 (Volovik, 2013): low-energy physics is insensitive to trans-Planckian details because of topological protection. The Leggett frequency omega_L = 0.070 M_KK is a trans-Planckian mode relative to the post-transit effective theory (omega_L/omega_transit = 7.86e-5). The erasure ratio (omega_L/omega_transit)^2 = 6.2e-9 is the information suppression factor, directly analogous to how Lorentz-violating corrections at the Planck scale are suppressed by (E/E_Planck)^n in the low-energy theory. The framework has rediscovered a specific instance of the trans-Planckian protection principle.

One subtlety the Naz deep-dive correctly identified: the sudden approximation for the Leggett mode gives <cos(phi_0)> = 0.828, not zero. But this modifies the B2 amplitude by 1.1e-6 * 0.828 = 9.1e-7. The parametric suppression survives. In 3He-B, the analogous quantity is the longitudinal NMR frequency shift, which persists as a tiny correction (10^{-3}) even when the dipolar coupling is "erased" in the normal state -- the residual is a quasiparticle spectral weight, not a collective mode. The framework's 9.1e-7 is even smaller. This channel is correctly closed.

### W1-D (Leggett Damping): The 3He-B Comparison

The PASS (Q = 6.7e5) is physically expected and matches 3He-B experience. In 3He-B, the longitudinal Leggett mode (the "squashing mode" at frequency sqrt(8/5) * Delta) has Q ~ 10^4 - 10^6 depending on temperature. The mode is sharp because its frequency sits well below 2*Delta (the pair-breaking threshold). In the framework, the analogous protection is stronger: omega_L = 0.070 M_KK vs 2*E_min = 1.800 M_KK (ratio 0.039), whereas in 3He-B the ratio omega_L/(2*Delta) ~ 0.5-0.8. The framework Leggett mode is MORE protected than its 3He counterpart because the quasiparticle gap is dominated by the single-particle energy epsilon_k >> Delta_k, not by the BCS gap alone.

The critical correction from W1-D deserves emphasis: the S49 wayforward confused the order parameter gap Delta_B3 = 0.084 with the quasiparticle gap E_min = 0.900. This is a standard error in BCS physics -- the pair-breaking threshold is 2*E_min, not 2*Delta. In 3He-B, epsilon_k is measured from the Fermi surface, so E_k ~ Delta and the two gaps coincide. In the framework, epsilon_k = |lambda_k| ~ O(1) >> Delta ~ O(0.01-0.7), so the quasiparticle gap and the order parameter gap are parametrically different. The framework is in the "deep BCS" regime where the Leggett mode frequency is a negligible fraction of the true pair-breaking threshold.

### W2-C (Spatial KZ): The Sudden-Quench Universality

The FAIL (delta_n/n = 1.59e-4, featureless) confirms the sudden-quench universality theorem from Paper 27 (Volovik, 2013) and the Kibble-Zurek experiments in 3He.

In 3He experiments (Paper 14, Volovik 2011), the KZ defect density n ~ xi^{-d} does NOT depend on quench inhomogeneity in the sudden limit. The Lancaster and Helsinki experiments on 3He-B vortex nucleation by neutron irradiation show that the defect density depends only on the local correlation length xi at the transition, not on the spatial profile of the quench. The framework is 79,932x deeper into the sudden regime than any laboratory quench, so the spatial KZ is maximally featureless. This is the 13th n_s route closed.

In the 3He experiments, the KZ exponent DOES depend on the quench rate (slow vs fast), but not on spatial inhomogeneity at fixed quench rate. The spatial variation enters only through the correlation length xi, which depends on T-T_c(x). If T_c varies spatially (e.g., from pressure gradients), the defect density modulates. But in the framework, the "quench rate" v_terminal = 26.5 M_KK is set by the gradient energy and is the same everywhere on the fabric. Cell-to-cell volume variations (sigma_V = 10%) produce sub-leading corrections of order |ln P_LZ| * delta_rate/rate = 1e-4. The physics is correct: homogeneous sudden quench = featureless defect density.

---

## Section 2: Assessment of Key Findings

### The SA Correlator and the Multi-Component Order Parameter

The cross-domain finding that the spectral action correlator chi_SA(K) breaks the alpha_s = n_s^2 - 1 identity is structurally significant, and I can sharpen it using the 3He analogy.

In superfluid 3He-A, the order parameter is A_{mu,i} = Delta_0 * d_mu * (m_i + i*n_i), with 18 real components. Different experimental probes couple to different projections of this order parameter:

- **NMR spin-spin correlator**: couples to d-vector dynamics, probes the spin-orbit (dipolar) energy. This gives the longitudinal NMR frequency Omega_B ~ sqrt(lambda_D * Delta^2 / chi_N).
- **Sound attenuation**: couples to the amplitude |A|^2, probes the density of states and gap structure.
- **Superfluid density**: couples to the phase gradient nabla*theta, probes the K^2 Goldstone spectrum.

These three probes give three different K-dependences at the same temperature, because they project onto different components of the same order parameter. The Goldstone (phase) correlator gives K^{-2}. The amplitude (Higgs) correlator gives K^{-2} with a different mass. The spin-orbit correlator gives a gapped response at omega_B.

The framework's distinction between the Josephson propagator P(K) = T/(JK^2 + m^2) and the spectral action correlator chi_SA(K) = sum W_{pq}/(K^2 + C_2(p,q)) is the SAME phenomenon. The Josephson propagator is the phase-phase correlator (Goldstone sector). The SA correlator involves the FULL spectral response -- all eigenvalues of D_K, not just the Goldstone. These are different projections of the same underlying geometry, just as NMR and sound attenuation probe different components of A_{mu,i} in 3He.

The structural content: Goldstone's theorem protects K^2 ONLY for the phase-phase correlator. The spectral action is not a symmetry-breaking correlator and is not protected. Its pole structure (C_2 from 1.33 to 9.33, spread 110%) gives genuinely different K-dependence. The identity alpha_s = n_s^2 - 1 is a theorem of the phase sector, not of the geometry.

This is a significant finding. The question "which correlator does the CMB measure?" is the framework-internal version of the condensed matter question "which probe couples to which order parameter component?" In 3He, the answer depends on the experimental setup. In cosmology, it depends on the mechanism that converts modulus perturbations delta_tau into metric perturbations delta_g. This coupling has not been computed.

### q-Theory and the Framework's q Variable

The cross-domain Route 2 (R-G integral variation) was closed by factorization: delta_I_alpha(x) = (dI/dtau) * delta_tau(x), so the K-dependence is purely from delta_tau. This is correct within the R-G integrable system.

But q-theory (Papers 15-16, 35) has a DIFFERENT variable from the R-G integrals. In q-theory, q is the vacuum variable -- a spacetime-constant field whose equilibrium value self-tunes to make rho_vac = 0. Perturbations delta_q behave as pressureless dust (DM). The question "what IS q in the framework?" has a specific answer that I have been refining across sessions:

q is NOT tau. Tau is the Jensen deformation parameter -- it describes the internal geometry. q must be a conserved charge density or a 4-form field strength that can self-tune.

q is NOT |Delta|. The BCS gap is a many-body quantity that varies with tau, but it is not a spacetime field. Post-transit, Delta = 0 everywhere.

The most natural identification, which I proposed in S43 and have refined since: **q = det(e) restricted to the SU(3) fiber**, where e is the tetrad. This connects to Paper 23 (Nissinen-Volovik, 2023): the volume-preserving condition det(e) = const IS the q-theory equation d(rho)/dq = 0. The framework's volume-preserving TT deformation (S12, proven) is the structural implementation of q-theory self-tuning.

The residual CC (113 orders above observation in QFIELD-43) then arises from the species-counting hierarchy: the q-theory self-tuning cancels the microscopic vacuum energy, but the residual CC is proportional to perturbation scales (Paper 5). With 992 Peter-Weyl modes and the Hausdorff impossibility (CUTOFF-F-44), the framework cannot simultaneously tune both G_N (set by f_2) and Lambda (set by f_4) with a single cutoff function. This is the CC problem = moment problem (S44 permanent result), and q-theory resolves it by making Lambda = 0 at equilibrium while G_N is set by the Sakharov mechanism independently.

---

## Section 3: Collaborative Suggestions

### The Goldstone Mass from Gravitational Response

Paper 30 (Volovik, 2022) derives G_N ~ c_s^2 / rho_0 from superfluid parameters. The emergent Newton constant depends on the gap Delta, the Fermi velocity v_F, and the density of states N(E_F). In the framework, G_Sak = 2.29 * G_obs (S44 SAKHAROV-GN-44, corrected), with the effective Planck mass M_Pl_eff = 99 GeV from 6440 PW modes.

Could the Goldstone mass emerge from the gravitational sector? In the Sakharov mechanism, G_N^{-1} ~ sum_n lambda_n^2 * f'(lambda_n^2/Lambda^2). The spectral response to a metric perturbation involves the SAME eigenvalue sum as the SA correlator. If the gravitational coupling is K-dependent (running G_N), the effective mass in the gravitational propagator could be different from the Josephson mass.

However, RUNNING-GN-45 showed G_Sak(tau) is MONOTONE with only 2.5% variation over [0, 0.5]. The gravitational coupling is topologically protected (a_0 = 6440 is constant). This means the gravitational sector does not introduce new K-dependence at the level of the effective Newton constant. The Goldstone mass cannot come from G_N running.

The deeper issue is the mass problem identified by the cross-domain synthesis: m_required = 11.85 M_KK vs m_Leggett = 0.070 M_KK. In the superfluid analogy, this is the hierarchy between the dipolar interaction energy (which sets the Leggett frequency) and the Fermi energy (which sets the overall scale). In 3He, omega_L / E_F ~ 10^{-3}. The framework ratio is 0.070/11.85 = 0.006. The mass hierarchy IS the analog of the weak-to-Fermi energy hierarchy in 3He.

### Trans-Planckian Protection and the Mass Problem

Paper 13 resolves the trans-Planckian paradox: low-energy physics is insensitive to UV details because the linearized dispersion near a Fermi point is topologically protected. The corrections scale as (E/E_Planck)^n with n >= 2.

The mass problem (requiring m = 12 M_KK for n_s = 0.965) means the observable IS UV-sensitive -- the required mass is at the spectral edge of D_K at high Peter-Weyl truncation. Does this violate trans-Planckian protection?

Not necessarily. Trans-Planckian protection applies to the FORM of the low-energy theory (Lorentz invariance, K^2 dispersion). It does NOT protect the VALUES of parameters. In 3He, the speed of sound c_s depends on microscopic parameters (interaction potential, density), but its existence as a linear dispersion is topologically guaranteed. Similarly, the O-Z form P(K) = T/(JK^2 + m^2) is protected, but the VALUE of m is UV-sensitive. The n_s tilt, being controlled by m, is a UV-sensitive quantity.

This is the superfluid universe perspective on the mass problem: the STRUCTURE of the power spectrum (near-scale-invariant, red-tilted, Gaussian) is topologically robust. The TILT parameter n_s is UV-sensitive because it depends on the mass gap, which is determined by the microscopic Hamiltonian. This is why n_s has been the hardest observable for the framework -- it requires knowing the UV completion (the full spectral action at high cutoff Lambda ~ 12 M_KK), which is precisely the regime where the effective theory is least reliable.

### What Observable of the Non-Equilibrium Vacuum Determines n_s?

Paper 27 frames cosmology as relaxation of a non-equilibrium superfluid. The GGE is the framework's non-equilibrium quantum vacuum. The equilibrium correlator (O-Z) fails to give n_s. The Bogoliubov spectrum is erased. What is left?

In a quenched superfluid, the observable power spectrum is determined by the RESPONSE FUNCTION, not by the equilibrium propagator. The response function chi(K, omega) of the non-equilibrium state involves the full time-dependent dynamics of the quench. In 3He rapid quenches, the post-quench state has correlations set by the QUENCH PROTOCOL (how fast, from which initial state) rather than by the equilibrium order parameter.

For the framework, this suggests the SA-Goldstone mixing (cross-domain Route 1) is the right direction. The quench protocol IS the transit through the Jensen deformation. The modulus perturbation delta_tau(x) couples to BOTH the spectral action (through d(lambda_n)/d(tau)) and the Josephson sector (through delta_Delta and delta_J). The physical power spectrum is the response of the COMBINED system to the quench.

The cross-domain finding that the SA correlator has alpha_eff = 1.21 (sub-quadratic) is a concrete realization of this principle. The quench couples to the non-Goldstone sector (all 992 eigenvalues), and this sector has K-dependence not protected by Goldstone's theorem. The key computation for S51 is SA-GOLDSTONE-MIXING-51: compute the ADDITIVE (not multiplicative) contribution of chi_SA to the physical power spectrum through the delta_tau -> delta_Delta -> delta_J coupling chain.

### The Volovik Dilution Model (W2-E)

The W2-E computation noted that if quasiparticles diluted as a^{-3} per comoving volume, the framework would give w_a = -0.735 (matching DESI). This was dismissed because "quasiparticles are per-fiber excitations; fiber density in comoving coordinates is constant."

I will defend the dismissal but note a subtlety. In q-theory (Paper 35), the perturbation delta_q dilutes as a^{-3} BECAUSE it has spatial gradients in the 4D spacetime. The kinetic energy (1/2)(nabla delta_q)^2 redshifts with expansion. But the framework's quasiparticles are in the INTERNAL fiber, with no 4D spatial gradients. Their "density" is a fiber quantity, not a 4D volume quantity. The dilution model incorrectly promotes fiber energy to 4D kinetic energy.

However, there IS a channel that could produce effective dilution: if the fiber volume changes with expansion (which it does if tau evolves), then the effective 4D energy density rho_4D = rho_fiber * V_fiber / V_4D could evolve. But the frozen-modulus dichotomy (TAU-STAB-36 FAIL) means either tau is frozen (V_fiber constant, no dilution) or tau runs away (framework excluded). The triple-lock on w_a = 0 is genuine.

---

## Section 4: Framework-Superfluid Correspondence Updates

The S50 results modify the correspondence table established in prior sessions:

| # | Framework Object | 3He Analog | Status | S50 Update |
|:--|:----------------|:-----------|:-------|:-----------|
| 1 | BCS on SU(3) | 3He-B pairing | CONFIRMED | Q = 670,000 (sharper than 3He) |
| 2 | GGE relic | Non-equilibrium superfluid | CONFIRMED | Triple-locked w_a = 0 |
| 3 | Leggett mode | Dipolar oscillation | CONFIRMED | 25.9x below pair-breaking |
| 4 | Bogoliubov erasure | Trans-Planckian protection | **NEW** | omega_L/omega_transit = 10^{-5} |
| 5 | SA vs Josephson correlators | NMR vs sound probes | **NEW** | Different K-dependence, same geometry |
| 6 | Sudden-quench universality | KZ homogeneous limit | CONFIRMED | 13th n_s route closed |
| 7 | Mass problem (170x) | omega_L/E_F ~ 10^{-3} | IDENTIFIED | Analog of weak/Fermi hierarchy |
| 8 | q = det(e) | Volume-preserving | UNCHANGED | CC = moment problem |
| 9 | Analog horizons | PG black hole | **RETRACTED (S49)** | No superflow |
| 10 | Alpha_s identity | K^2 from Goldstone theorem | **NEW** | 5 independent proofs |

---

## Section 5: Open Questions and Closing

### Open Questions for S51

1. **SA-Goldstone mixing coefficient**: The SA correlator breaks the identity but gives n_s = 0.2 standalone. The Josephson gives n_s = 0.965 but with wrong alpha_s. What MIXING RATIO produces both n_s and alpha_s simultaneously? This is a single-parameter problem (the coupling a/b) computable from the delta_tau response chain.

2. **The mass problem as Sakharov vs Josephson**: The required mass 12 M_KK is at the spectral edge of D_K. Is this a SPECTRAL ACTION observable rather than a Josephson one? In the superfluid analogy, the Sakharov mechanism and the sound-wave propagator involve different sums over the spectrum. The spectral cutoff Lambda determines one; the gap equation determines the other.

3. **BAO exclusion severity**: The chi^2/N = 23.2 against BAO is devastating for w_0 = -0.509. But the GGE alpha = 1.327 giving w_0 = -0.430 is computed from the single-cell BCS spectrum. The 32-cell fabric with inter-cell coupling could modify alpha through collective effects (screening, pair transfer). The RPA correction to alpha_s was negligible (W2-B FAIL), but the RPA correction to w_0 involves a DIFFERENT sum (energy over pressure, not spectral tilt). This has not been computed.

4. **n_s as a dynamical observable**: All 13 closed n_s routes treated n_s as an equilibrium or post-transit property. Paper 27 suggests it should be a quench-protocol property -- set during the transit, not after. The SA-Goldstone mixing is the first approach that computes n_s from the transit dynamics rather than the post-transit correlator.

### Assessment

Session 50 produced the deepest structural characterization of the framework's observational interface. The O-Z identity (5 proofs), the mass problem (170x), and the BAO exclusion (chi^2 = 23) are serious constraints. The Leggett damping PASS, phi crossing PASS, and sigma_8 PASS demonstrate that the internal BCS physics is mathematically rich and correct on its own terms.

From the superfluid universe perspective, the most significant S50 finding is the SA correlator. It confirms that the framework, like 3He, has MULTIPLE correlators with different K-dependences, only one of which is protected by Goldstone's theorem. The n_s problem may not be a failure of the framework but a misidentification of which correlator the CMB measures. In 3He, NMR experimentalists knew which probe they were using. The framework has not yet identified which "probe" the CMB expansion-history constitutes.

The probability floor at 3-5% is set by the mathematical structure (publishable independently of cosmology) and the open SA-Goldstone channel. The superfluid analog program continues to provide the correct structural framework: the system is 3He-B class (not A-class, N_3 = 0), the Leggett mode is the dipolar analog, the GGE is the non-equilibrium vacuum, and the trans-Planckian protection explains why collective mode information is erased in the post-transit spectrum.

The microscopic theory is known. The computation of the correct correlator is what remains.
