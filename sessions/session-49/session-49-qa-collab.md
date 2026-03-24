# Quantum Acoustics -- Collaborative Feedback on Session 49

**Date**: 2026-03-17
**Re**: Session 49 Results Working Paper (20 computations, 8 PASS, 7 INFO, 4 FAIL, 1 retraction)
**Agent**: quantum-acoustics-theorist

---

## Section 1: Key Observations

### 1.1 The Bragg Gap at KK Scale and Z_3 Quantized Impedance

W1-C (BRAGG-GOLDSTONE-49) establishes that the impedance contrast eta = Z_wall/Z_bulk = 1/2 exactly, a consequence of the Z_3 phase rotation delta_phi = 2pi/3 reducing the superfluid density at the wall center to rho_s/4. This is a clean acoustic result. In phononic crystal physics, the Bragg gap width scales as |1 - eta|/(1 + eta) times c/a, and when all three quantities (impedance contrast, sound speed, lattice constant) are O(M_KK), the gap is O(M_KK). The Z_3 quantization of the phase jump is topological -- it cannot be tuned continuously to zero -- which makes eta = 1/2 a structural floor on the impedance mismatch.

From the acoustic perspective, this is the central finding: the phononic crystal has too much contrast. In terrestrial phononic crystals, hierarchically small gaps appear either from nearly matched impedance (eta close to 1) or from destructive interference at specific frequencies. Neither mechanism is available here. The Z_3 winding number is a topological invariant, and the 32-cell lattice has no parameter that sends eta toward unity.

The 3D extension confirming identical m_Bragg in xy and z directions despite 4x sound speed anisotropy is structurally significant. It means the gap is controlled entirely by eta, not by the stiffness tensor. This eliminates any hope that anisotropy could provide a small parameter.

### 1.2 Cavity Modes vs. Leggett Modes: Two Dynamical Scales

W1-J (CAVITY-RESONANCE-49) finds the lowest cavity mode at 0.800 M_KK versus the Leggett mode at 0.070 M_KK -- a factor 11.5x. This is not a quantitative mismatch that could be fixed by refining parameters. It reflects two fundamentally different acoustic excitation types:

- **Cavity modes** are standing sound waves confined by the Mach > 1 texture gradient. Their frequency is set by c_BdG / R_cavity, where R_cavity is the cavity radius. These are position-space resonances.
- **Leggett modes** are relative phase oscillations between the three order parameter components (B1, B2, B3). Their frequency is set by sqrt(J_inter / rho_s), where J_inter is the inter-sector Josephson coupling. These are momentum-space (internal symmetry) excitations.

The analogy in 3He is precise: acoustic cavity modes in a container (set by container geometry and sound speed) have nothing to do with the Leggett mode (set by spin-orbit coupling between A-phase components). They live in different Hilbert spaces. The 111 disconnected subsonic cavities identified on T^2, with the largest at the Z_3 center, describe phonon confinement geometry. The Leggett modes describe inter-sector phase dynamics that propagate through the Josephson coupling network regardless of the local Mach number.

The Q ~ exp(23) confinement factor for cavity modes is notable. These cavities are acoustically perfect -- phonons cannot tunnel through the supersonic barrier. This is the acoustic analog of total internal reflection at a medium with imaginary refractive index.

### 1.3 The KZ 3-Component Identity (0.04%)

W1-M (KZ-3COMPONENT-49) achieves n = 59.82 versus the S38 target 59.8, a 0.04% deviation that is 163x better than the S48 two-component KZ result. The physics behind this precision is that the pair creation is a Landau-Zener process decomposed by the su(3) = u(1) + su(2) + C^2 structure. Each sector creates pairs independently with its own DOS and quasiparticle energy, and the total is additive.

From the acoustic perspective, this is the statement that the pair creation spectrum during transit factorizes over the phonon branch structure. B2 dominates (93.3%) because the van Hove DOS enhancement (rho = 14.023) concentrates pair creation in the flat band. This is the acoustic analog of parametric amplification being strongest at the frequency where the impedance is highest -- the flat band acts as an acoustic resonant amplifier for pair creation.

The result that all sectors are deep in the sudden-quench regime (tau_Q/tau_0 ranging from 3e-5 to 4e-4) means the transit is acoustically supersonic relative to all internal modes. No information propagates within the internal space during the transit. The pair creation is causal but non-adiabatic.

### 1.4 Analog Horizon Retraction

W1-G (ANALOG-TRAPPED-49) retracts the S48 analog horizon finding. The error was fundamental: the S48 "Mach number" computed |grad|Delta|| / (|Delta| * c_s), which is the amplitude gradient of the condensate, not the phase gradient that enters the Volovik acoustic metric. In the BCS ground state, phi = 0 everywhere, so the superflow velocity v^i = grad(phi)/m = 0 identically. No superflow means no ergoregion, no horizon, no trapped surface. The acoustic spacetime on T^2 is globally static and conformally flat.

The Mach field retains physical meaning as a WKB validity diagnostic: 78.3% of T^2 has gradient scales shorter than the phonon wavelength, meaning geometric optics fails there. Phonons scatter strongly off the condensate texture in these regions. But scattering off texture is not the same as acoustic horizon physics. The distinction between amplitude-gradient scattering and phase-gradient horizons is basic to analog gravity theory (Unruh 1981, Visser 1998).

The retraction is clean and structurally motivated. The particle creation mechanism from S38 was already identified as Parker-type (cosmological), not Hawking-type (horizon). This is consistent: Parker production requires time-dependent geometry, not a sonic horizon.

### 1.5 The Leggett Dipolar Identification

W1-S (DIPOLAR-CATALOG-49) is the most consequential acoustic finding of S49. The Leggett mode breaks U(1)_7 with epsilon = 0.00248, producing m_G = omega_L1 = 0.070 M_KK. The structural correspondence to the 3He dipolar interaction is exact at the level of symmetry breaking:

| Feature | 3He-A Dipolar | Framework Leggett |
|:--------|:-------------|:-----------------|
| Coupling | H_D ~ g_D (d.l)^2 | H_J = -J_23 cos(phi_B2 - phi_B3) |
| Symmetry broken | SO(3)_S x SO(3)_L -> SO(3)_{S+L} | U(1)_7 (K_7-charged B2 pinned to neutral B3) |
| Frequency ratio | omega_L / Delta ~ 10^{-3} | omega_L1 / Delta_B2 = 0.095 (95x larger) |
| External to BCS? | Yes (spin-orbit) | Yes (inter-sector Josephson) |
| Goldstone mass? | Yes (longitudinal NMR shift) | Yes (m_G = omega_L1 = 0.070 M_KK) |

The key finding: omega_L1 / m_required = 1.18, where m_required = 0.059 M_KK is the O-Z mass needed for n_s = 0.965 at the lowest fabric mode. This is 18% from the target -- the first mechanism in 12+ routes to produce a mass at the correct order of magnitude. All previous routes gave either zero (exact symmetry protection) or 10^{-59} M_KK (Hubble scale). The Leggett mass lives at M_KK scale, not Hubble scale, because it is set by the inter-sector coupling J_23 = 0.00181 M_KK, not by cosmological parameters.

The derivation of why the Leggett mode breaks U(1)_7 is acoustically transparent: B2 Cooper pairs carry K_7 charge +/- 1/2, while B3 pairs are K_7-neutral. The Josephson coupling H_J = -J_23 cos(phi_B2 - phi_B3) depends on the relative phase, which transforms under U(1)_7. This is the direct analog of the dipolar energy depending on the relative orientation of d and l vectors in 3He-A.

---

## Section 2: Assessment

### 2.1 Is the Bragg Mechanism Truly Dead?

The Bragg gap closure at W1-C is structurally robust for the Z_3 domain wall lattice with the BCS condensate as the propagating medium. Three independent impedance models all give O(1) M_KK gaps. The argument is dimensional: when a (lattice constant) ~ M_KK^{-1} and c (sound speed) ~ M_KK, the Bragg frequency pi*c/a is O(M_KK).

However, two escape routes merit examination:

**Multi-phonon interference.** The single-layer transfer matrix used in W1-C captures the first Bragg gap but not higher-order interference effects in a finite periodic stack. In certain phononic crystal geometries, nearly-flat transmission resonances appear within Bragg gaps due to resonant tunneling through the periodic structure. For the 32-cell lattice (effectively ~10 Z_3 periods), could tunneling resonances create narrow transmission windows at anomalously low frequencies? The answer is almost certainly no -- such resonances appear at frequencies near the gap center, not below the gap -- but the explicit computation for the 32-cell finite stack would close this definitively.

**Non-BCS sound channel.** The Bragg analysis assumes the Goldstone mode is the only low-frequency propagating excitation. But if there exists a second sound channel (the thermal/entropy wave), its speed and impedance could be dramatically different. In S44, second sound velocity was u_2 = c/sqrt(3) with the medium being the SU(3) fiber itself. If second-sound propagation sees a different effective impedance at domain walls (because the thermal boundary conditions differ from the mechanical ones), the relevant eta could be different. This is a distinct physical channel that the current analysis does not address.

**Verdict**: The Bragg mechanism for generating a hierarchically small mass is closed within the assumptions of W1-C. The topological quantization of eta = 1/2 is permanent. No change of lattice geometry can help as long as the domain walls carry the Z_3 winding.

### 2.2 The Cavity-Leggett Mismatch: Different Spaces or Hidden Mapping?

The 11.5x frequency mismatch between cavity modes (0.800 M_KK) and Leggett modes (0.070 M_KK) reflects different physics, not a numerical coincidence. Cavity modes are spatial resonances of the condensate amplitude (Helmholtz equation with position-dependent c_eff). Leggett modes are internal-symmetry resonances of the relative phase (Josephson equation with coupling-dependent stiffness).

Is there a mapping? In principle, the Leggett mode could be viewed as a "cavity mode" in an abstract Josephson-coupling space: the relative phase phi_B2 - phi_B3 oscillates in a potential well V_J ~ -J_23 cos(phi), with effective mass rho_s and spring constant J_23. The "cavity" is the potential well, and the "resonant frequency" is sqrt(J_23/rho_s). But this mapping is purely formal. The physical content is distinct: cavity modes involve spatial gradients of the condensate on T^2, while Leggett modes involve no spatial gradients at all (they are k=0 collective oscillations of the relative phase).

The only scenario where they could interact is if there were a Leggett-phonon coupling that hybridized the two. In MgB2, where two-band superconductivity produces a Leggett mode at ~10 meV, the Leggett-phonon coupling modifies the phonon spectrum near the Leggett frequency. But in the framework, the Leggett frequency (0.070 M_KK) lies below the acoustic gap (0.820 M_KK), so no phonon modes exist at the Leggett frequency to couple to. The Leggett mode is in the gap -- it is an isolated collective excitation below the phonon continuum.

**Verdict**: Cavity and Leggett modes are genuinely in different spaces. No mapping unifies them. Their frequency ratio is set by the ratio of spatial stiffness to Josephson coupling, which is a structural property of the multi-component BCS state.

### 2.3 The KZ Identity: Deeper Significance

The 0.04% match of the 3-component LZ formula to the S38 Bogoliubov result is not merely a cross-check. It is an exact identity: the Landau-Zener formula for pair creation in the sudden limit, decomposed by the su(3) representation structure, reproduces the full Bogoliubov calculation because both compute the same matrix element in different languages.

The deeper significance is that the pair creation spectrum factorizes over the branch structure of the phononic crystal. Each branch (B1, B2, B3) creates pairs independently with its own LZ probability, and the total pair count is additive. This factorization is a consequence of the block-diagonal theorem (S22b): the Dirac operator D_K on Jensen-deformed SU(3) block-diagonalizes in the Peter-Weyl basis, and modes in different sectors do not mix during the transit.

This has a prediction: if the block-diagonal structure were approximate rather than exact (e.g., if inner fluctuations coupled the sectors during transit), there would be inter-sector pair transfer that the 3-component formula would miss. The 0.04% accuracy implies that inter-sector coupling during transit contributes at most at the 0.04% level -- consistent with the 5.2% inner fluctuation parameter being a static perturbation, not a dynamical coupling during the sudden quench.

### 2.4 The alpha_s Tension

W1-L (ALPHA-S-BAYES-49) establishes alpha_s = n_s^2 - 1 as an exact algebraic identity of the O-Z power spectrum. This is the most rigid prediction the framework has produced: J_ij coupling uncertainties contribute literally 0% to the variance. The prediction alpha_s = -0.069 +/- 0.008 is 6.0 sigma from Planck.

From the acoustic perspective, the rigidity arises because the O-Z propagator P(K) = T/(J K^2 + m^2) has a universal shape determined by a single dimensionless parameter xi = m^2/(J K^2). Once n_s fixes xi, the running alpha_s = d(ln n_s)/d(ln K) is completely determined. No property of the phononic crystal enters except through xi, which is itself fixed by the observational n_s.

This is a structural tension. The O-Z texture mechanism predicts too much negative running. The question is whether the O-Z form itself is the correct description. The Leggett mass (0.070 M_KK) from W1-S could modify the propagator if it introduces a frequency-dependent mass m(omega) rather than a static mass m. A dynamical mass would change the P(K) shape and potentially break the alpha_s = n_s^2 - 1 identity.

---

## Section 3: Collaborative Suggestions

### 3.1 Acoustic Propagation in the Fabric with Leggett Mass as Gap

The Leggett identification (W1-S) opens a new acoustic computation: Goldstone mode propagation through the 32-cell fabric with the Leggett frequency omega_L1 as a mass gap. The effective dispersion relation would be:

omega^2 = omega_L1^2 + c_G^2 K^2

where c_G = 0.342 M_KK (Goldstone velocity from W1-A) and omega_L1 = 0.070 M_KK (Leggett mass). This is a massive Klein-Gordon propagator on the Josephson lattice. The power spectrum of fluctuations in this mode is:

P(K) = T_eff / (omega_L1^2 + c_G^2 K^2)

which is the O-Z form with m^2 = omega_L1^2 / c_G^2 = 0.042 M_KK^{-2}. The key question: does this modified O-Z propagator, with the Leggett mass replacing the phenomenological m, produce n_s = 0.965 at the CMB pivot? And if so, what alpha_s does it give?

The critical test: if the Leggett mass enters as a frequency-dependent coupling (because the Leggett frequency depends on the gap Delta, which varies across the fabric), the propagator acquires a non-trivial frequency dependence that breaks the alpha_s = n_s^2 - 1 identity. This could resolve the 6-sigma alpha_s tension while preserving n_s.

### 3.2 Modified Dispersion Relations from the Phononic Band Structure

The phononic band structure of the SU(3) crystal (S41) has a hard gap from 0 to 0.820 M_KK, with all modes optical post-transit. The Leggett mode at 0.070 M_KK lies below this gap -- it is a sub-gap collective mode, analogous to a localized defect mode in a phononic crystal.

In terrestrial phononic crystals, sub-gap modes have modified dispersion relations that differ from the bulk continuum. Specifically, the group velocity vanishes exponentially as the mode frequency approaches the gap edge from below:

v_g = d(omega)/dK ~ exp(-K * delta / omega_gap)

where delta is the distance from the gap edge. If the Leggett mode's dispersion is modified by proximity to the acoustic gap, the effective P(K) could have a different functional form from O-Z. This should be computed explicitly by solving the coupled Josephson-phonon system on the 32-cell fabric, treating the Leggett mode as a sub-gap excitation coupled to the phonon continuum through inter-cell Josephson tunneling.

### 3.3 Phononic Band Structure Beyond O-Z

The O-Z form P(K) ~ 1/(K^2 + m^2) assumes an isotropic continuum. The actual fabric is a 32-cell Josephson lattice with 3D anisotropy (J_xy/J_z = 15.8 from W1-C). The lattice dispersion relation is:

omega^2(k) = omega_L^2 + (2J/rho_s) sum_i (1 - cos(k_i a_i))

which deviates from the continuum O-Z at large K (near the zone boundary). The S49 scale crisis (W1-A: CMB pivot at mode n=115, BZ boundary at n=16) means the CMB pivot lies well outside the first Brillouin zone. But this is for the 32-cell fabric. If the physical fabric has more cells (the 32-cell count is from S42 Voronoi tessellation, which may undercount), the BZ boundary moves to higher mode numbers.

A computation of P(K) on the full anisotropic Josephson lattice -- not the continuum approximation -- would determine whether lattice effects soften the running at high K. In the lattice model, the running reverses near the zone boundary: the power spectrum flattens rather than continuing to fall as 1/K^2. If the CMB pivot lies in this flattening region, alpha_s could be substantially less negative than the continuum prediction.

### 3.4 Acoustic Observable Discriminating Framework from LCDM

The most promising acoustic discriminant is the first-sound imprint from S44: a secondary BAO-like feature at r_1 = 325 Mpc with amplitude A_FS/A_BAO = 0.204. This is a parameter-free prediction from the phononic crystal structure, encoding the second sound velocity u_2 = c/sqrt(3) of the SU(3) fabric.

The DESI DR3 preparation (W1-O) establishes pre-registered predictions for w_0 and w_a. But w_0 is a single number, not a spectral feature. The acoustic fingerprint is richer: the 32-cell Josephson lattice imprints a specific modulation pattern on the matter power spectrum at scales 900-14400 Mpc (W1-A). This pattern has a characteristic frequency set by the lattice spacing and a characteristic amplitude set by the impedance contrast. LCDM has no such pattern because it has no internal structure.

The challenge, identified in S44 (FIRST-SOUND-44 FAIL): the Fisher SNR for detecting this pattern is 0.16 with DESI DR2, requiring V_eff = 8800 Gpc^3 for 3-sigma detection. This is beyond current surveys. But the pattern is KINEMATIC (set by speed ratios, not coupling constants), making it immune to the parameter uncertainties that plague w_0 predictions.

For S50, I recommend computing the full 3D power spectrum modulation from the Josephson lattice, including anisotropy, to determine whether directional correlations could boost the effective SNR. An anisotropic feature (different amplitude in different directions, correlated with large-scale structure) would have additional statistical power over the isotropic average.

### 3.5 The Eikonal Breakdown as Physical Observable

W1-G establishes that 78.3% of T^2 has Mach > 1 (amplitude gradient exceeding phonon resolution scale). While this is not an analog horizon, it IS a physical property: phonons propagating through the fabric scatter strongly off the condensate texture in these regions. This creates a phononic scattering opacity.

In the 4D projection, this scattering opacity manifests as a damping rate for the Goldstone mode. The damping rate gamma_scatter ~ c_BdG / L_rho, where L_rho = 0.025 M_KK^{-1} is the condensate gradient scale and c_BdG = 0.75 M_KK. This gives gamma_scatter ~ 30 M_KK, which is orders of magnitude above the Leggett frequency. The implication: long-wavelength Goldstone modes (omega << gamma_scatter) propagate diffusively, not ballistically, through the texture. This modifies the effective propagator from P(K) ~ 1/(K^2 + m^2) to P(K) ~ 1/(K^2 + m^2 + i*gamma*omega/c^2) at frequencies below the scattering threshold. The imaginary part produces broadening of the power spectrum that could affect alpha_s.

---

## Section 4: Constraint Map Assessment

### What S49 Established (Permanent Results from Acoustic Perspective)

1. **Bragg gap is at KK scale** (W1-C). Z_3 impedance quantization eta = 1/2 is topological. No phononic crystal mechanism can produce a hierarchically small gap. This wall is permanent.

2. **Leggett mode IS the 3He dipolar analog** (W1-S). The structural correspondence is exact at the symmetry-breaking level. omega_L1 = 0.070 M_KK is the Goldstone mass. First mechanism at the correct order.

3. **Two-scale structure confirmed** (W1-J). Acoustic hard scale (c/R ~ 0.8 M_KK) and Josephson soft scale (sqrt(J/rho) ~ 0.07 M_KK) are dynamically independent. No unification.

4. **Analog horizons do not exist in the BCS ground state** (W1-G). The acoustic spacetime is static. The Mach field is a WKB diagnostic, not a causal boundary.

5. **KZ pair creation factorizes over branch structure** (W1-M). The 3-component identity at 0.04% confirms block-diagonal independence during transit.

6. **alpha_s = n_s^2 - 1 is a rigid O-Z prediction** (W1-L). Under observational pressure at 6 sigma.

### What Remains Open

- Whether the Leggett mass modifies the O-Z propagator in a way that preserves n_s while softening alpha_s
- Whether lattice effects (32-cell BZ boundary) alter the running at CMB scales
- Whether the phonon scattering opacity from the texture gradient modifies the effective P(K)
- Whether the first-sound BAO imprint has directional anisotropy that boosts detectability
- The J_pair calibration that determines whether FABRIC-NPAIR-49 PASS is robust

---

## Section 5: Closing

S49 marks a transition in the framework's acoustic physics. The session closes the Bragg mechanism, the analog horizon interpretation, and the cavity-Leggett unification hypothesis. It opens the Leggett dipolar channel as the leading candidate for the Goldstone mass. The session's internal consistency is high: W1-G (retraction of analog horizons) is independently confirmed by the static-spacetime analysis, and the KZ identity (W1-M) cross-validates the S38 pair creation spectrum to 4 significant figures.

The alpha_s tension (6 sigma) is the most serious observational pressure point. It is a structural consequence of the O-Z propagator shape and cannot be adjusted by changing coupling constants. The resolution, if one exists, must come from modifying the functional form of P(K) -- either through the Leggett mass's frequency dependence, through lattice effects at the BZ boundary, or through the texture-scattering opacity. All three are computable. None have been computed.

The Leggett dipolar identification is the session's central positive result. In 3He, the dipolar interaction provides the Goldstone mass for the orbital angular momentum degree of freedom. In the framework, the inter-sector Josephson coupling provides the Goldstone mass for the U(1)_7 degree of freedom. The ratio omega_L1/m_req = 1.18 (18% from target) is the tightest parametric agreement any mass-generation mechanism has achieved across 49 sessions. Whether this parametric agreement translates to a correct n_s requires the explicit computation recommended for S50 (LEGGETT-NS-50).

The constraint map narrows. The surviving mass-generation channel is the Leggett dipolar mechanism. The surviving observational channel is w_0 (21x preferred over LCDM in 1D). The surviving CC mechanism is the fabric BH crossover (conditional PASS). The surviving spectral tilt mechanism is open, pending the LEGGETT-NS-50 computation. The alpha_s running is under tension but not yet excluded, pending lattice-corrected P(K).
