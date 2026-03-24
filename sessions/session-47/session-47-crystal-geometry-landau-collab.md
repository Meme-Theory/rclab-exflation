# Landau -- Collaborative Feedback on Session 47 Crystal Geometry

**Author**: Landau (Condensed Matter Theorist)
**Date**: 2026-03-16
**Re**: Session 47 Wave 2 Crystal Geometry Synthesis (Tesla)

---

## Section 1: Key Observations

### The Condensate as a Ginzburg-Landau Order Parameter

Tesla computes |Delta(theta_1, theta_2)|^2 on the maximal torus T^2 and obtains a contrast ratio of 3.14 x 10^6 peaked at the identity. This object is not yet a Ginzburg-Landau order parameter in the technical sense. It is a squared character sum weighted by BCS gaps. The distinction matters.

A proper GL order parameter field psi(x) on SU(3) would satisfy the Euler-Lagrange equation

    delta F / delta psi*(x) = alpha(tau) psi + beta |psi|^2 psi + (1/2m*) D^2 psi = 0

where D is the gauge-covariant derivative on SU(3) and alpha, beta are Landau coefficients determined by the BCS pairing interaction (Paper 08, eq. 2.1; Paper 04, Section 4). The object Tesla computed is the BCS-weighted coherent sum of characters, which corresponds to the mean-field order parameter ONLY if one identifies the character expansion coefficients with the GL amplitudes in each representation channel. This identification is correct in the 0D limit (L/xi_GL = 0.031, Session 38), where gradient terms are negligible and the order parameter is spatially uniform within each representation sector. In this regime, the GL free energy reduces to

    F[{Delta_s}] = sum_s [ a_s(tau) |Delta_s|^2 + b_s |Delta_s|^4 ] + sum_{s != s'} g_{ss'} |Delta_s|^2 |Delta_s'|^2     (1)

where s indexes spinor sectors B1, B2, B3. The coefficients are: a_s(tau) = 1/V_ss - N_s(E_F), b_s = N_s/(2 Delta_s^2), and g_{ss'} encodes inter-sector coupling. With V(B1,B1) = 0 (Trap 1), the B1 sector enters only through the cross-coupling g_{B1,B2}. With V(B3,B3) = 0.003 << V(B2,B2) = 0.256, the B3 sector is a spectator. The GL free energy is effectively single-component, centered on B2.

The identity-peaked profile is then a statement about the SPATIAL STRUCTURE of the B2 order parameter within the 0D coherent patch, resolved by the character decomposition. This is physically analogous to the gap function symmetry in unconventional superconductors: the gap magnitude varies across the Fermi surface (e.g., d-wave nodes), and here |Delta|^2 varies across the internal manifold SU(3). The identity peak is the analog of gap maxima along the Fermi surface.

### Phase Transition Classification of the Identity Peak

The identity-peaked condensate with Haar repulsion is a well-defined condensed matter phenomenon: it is an ORIENTATIONAL ordering transition on a compact group manifold. The order parameter space is SU(3) itself. The disordered phase has Delta(g) = const for all g in SU(3) (uniform on the group, respected by Haar measure). The ordered phase has Delta(g) peaked at g = e (the identity). The symmetry breaking pattern is:

    SU(3)_L x SU(3)_R --> SU(3)_diag                                           (2)

where SU(3)_L acts by left multiplication and SU(3)_R by right. The condensate centered at the identity is invariant under diagonal conjugation g --> h g h^{-1}, preserving SU(3)_diag. This is precisely the symmetry breaking of a Heisenberg ferromagnet on a group manifold (Paper 04, Section 5.1), with the identity element playing the role of the magnetization direction.

The contrast ratio of 3 million indicates extreme ordering. In Landau language, the reduced temperature is deep in the ordered phase: |alpha|/beta >> 1. The 0D limit confirms this: L/xi_GL = 0.031 means the entire system is within one coherence volume. There are no spatial fluctuations, no domain structure, no Goldstone modes -- the condensate is a single coherent object. This is the ultrasmall-grain limit of BCS theory (Paper 17, DPS review, Section on mesoscopic systems). The GL parameter kappa is meaningless in 0D because there is no distinction between penetration depth and coherence length when the system fits inside both.

### Curvature Branches as Spring Constants

Tesla's identification of the 6 curvature branches as "spring constants" is exactly correct in the Landau framework. The sectional curvature K(e_a, e_b) in direction (a,b) determines the restoring force for fluctuations of the metric in that plane. In a GL expansion around the bi-invariant point (tau = 0), the free energy cost of a deformation delta g_{ab} is

    delta F ~ sum_{a<b} K(e_a, e_b; tau=0) * (delta g_{ab})^2                  (3)

The curvature IS the harmonic spring constant. Soft modes (small K) cost less energy to excite; they are the first to become unstable under cooling (Paper 04, Section 4.2). The Jensen deformation is a specific deformation path that selectively softens the su(2)-C^2 cross-planes (K drops from 0.021 to 0.010) while stiffening the su(2)-su(2) planes (K rises from 0.083 to 0.122). This is a textbook example of MODE SOFTENING preceding a structural instability -- the 12 soft directions are the precursors of the transition (Paper 09, Landau-Khalatnikov relaxation near soft modes).

### The B2 Funnel: Progressive Concentration

The sequence 50% (modes) --> 62% (topology) --> 91% (pairing) in B2 has a precise condensed matter analog: it is the progressive SELECTION of the active channel through successive energy scales, identical to what happens in multi-band superconductors.

In MgB2, the sigma band carries ~75% of the total electron count but ~95% of the superconducting gap weight. The mechanism: phonon coupling is stronger in the sigma band, so BCS dynamics amplifies the modest mode-count advantage into near-total pairing dominance. Here, the B2 sector carries 50% of modes. The pi-phase topology (a measure of which states participate in the transit) enhances this to 62% -- topology selects the responsive sector. Then BCS dynamics, with V(B2,B2) = 0.256 dominating V(B3,B3) = 0.003 by a factor of 85, amplifies this to 91%.

Each stage acts as a filter. The product of filter selectivities is 91/50 = 1.82, which in a multi-band system would correspond to a coupling anisotropy ratio lambda_strong/lambda_weak ~ 5-10 (comparable to MgB2's sigma/pi ratio of ~7). This is not exotic. It is normal multi-band BCS physics made geometric.

### Soft-Pairing Anti-Correlation

The observation that the softest curvature branch hosts the strongest pairing (K = 0.010, V = 0.256 for B2) while the hardest hosts the weakest (K = 0.122, V = 0.003 for B3) is a direct manifestation of the PHONON SOFTENING mechanism in condensed matter. In conventional superconductors, soft phonons provide the strongest pairing attraction (Papers 15, 08). Here, the "phonons" are fluctuations of the Jensen metric, and the "soft modes" are the su(2)-C^2 cross-plane deformations. The same physics operates: geometrically compliant directions support stronger collective instabilities.

The quantitative mismatch (curvature ratio 12.5x vs pairing ratio 85x) indicates that the relationship is not simple proportionality K^{-1} ~ V. This is expected: the pairing matrix element V depends on the OVERLAP of wavefunctions on the soft geometric directions, not just the curvature itself. The enhancement from 12.5x to 85x comes from the coherent constructive interference of all 12 soft planes contributing to B2 pairing, while only 3 hard planes contribute to B3.

---

## Section 2: Assessment of Key Findings

### Resonance 5.1: The Protected Chain q_7^2 = K = 1/16

This is the strongest result in the synthesis and it is representation-theoretic, not numerical. Let me state it precisely.

The K_7 operator has eigenvalue q_7 = 1/4 on B2 states in the (0,0) sector (Session 34: [iK_7, D_K] = 0 at all tau). The square q_7^2 = 1/16. The sectional curvature K(u(1), C^2) = 1/16 at all tau (Theorem 2, verified to 10^{-15}). The Ricci eigenvalue Ric(u(1)) = 4 * 1/16 = 1/4 at all tau.

In condensed matter language, this is a PROTECTED QUANTUM NUMBER locked to a PROTECTED GEOMETRIC INVARIANT. The pairing channel (B2) carries a charge whose square equals the curvature of the direction along which that charge is defined. This is analogous to flux quantization in a superconductor (Paper 08): the flux quantum Phi_0 = h/(2e) is set by the charge of the Cooper pair, and the vortex core geometry is set by the same charge through the penetration depth. Here, the "flux quantum" is 1/16 = q_7^2, and it controls both the pairing selection rule and the geometric rigidity.

Tesla's assessment is correct: this is not a coincidence. It is the same Lie algebra structure constants determining both the spinor representation eigenvalues and the sectional curvatures. The fact that BCS selects EXACTLY this sector is the non-trivial content -- the algebra provides the equality, but the dynamics select which sector is active.

### Resonance 5.4: The Haar-Condensate Shell

The superfluid vortex analog is correct but should be stated more carefully. In a superfluid vortex (Paper 13, Abrikosov), the ORDER PARAMETER AMPLITUDE |psi| vanishes at the vortex core and recovers at r ~ xi. The density of states does not vanish at the core. Here, the situation is INVERTED: the order parameter amplitude |Delta| is maximal at the identity, but the MEASURE (Haar density) vanishes there. The physically observable quantity (|Delta|^2 * Haar) peaks at a finite shell radius.

The closer analog is not a vortex but the density profile of a BEC in a harmonic trap, where the condensate density peaks at the trap center but the radial probability density r^2 |psi(r)|^2 peaks at r > 0 due to the geometric factor. The shell at r = 0.85 rad is the 8D version of this effect, with the Weyl denominator |Delta_W|^2 playing the role of r^{d-1} in the radial Jacobian.

The FWHM of 0.59 rad = 0.19*pi defines the physically accessible condensate width. This is a well-defined observable: any coupling to 4D physics that integrates over SU(3) with the Haar measure will sample this shell, not the identity peak itself.

### Resonance 5.6: C^2 Isotropization

The convergence of within-doublet and cross-doublet C^2-C^2 curvatures (ratio dropping from 4.0 to 1.17) as tau increases is a FLOW TOWARD ISOTROPY in the coset sector. In Landau theory, isotropization of an order parameter subspace corresponds to an emergent continuous symmetry. As the C^2 sector becomes internally isotropic, the effective symmetry of the coset approaches SU(2) x SU(2) (the double cover of SO(4), the isometry group of S^3). This is significant because the universality class depends on the symmetry of the order parameter space. If the coset isotropizes completely, the effective dimensionality of the order parameter changes, potentially altering the critical exponents.

However, the isotropization is INCOMPLETE at the fold (ratio 1.48, not 1.00). The question of universality class is already settled at 3D Ising (Session 43, BCS-CLASS-43), which assumes Z_2 symmetry of the real gap |Delta|. The C^2 isotropization trend is a geometric sub-structure within the fixed universality class -- it modifies the non-universal amplitude ratios, not the universal exponents.

### Resonance 5.5: The 1/e^2 Radius = pi/4 Coincidence

Tesla is correct to flag this and correct to be skeptical. A 0.7% near-miss between a spectral observable (condensate 1/e^2 radius) and a representation-theoretic quantity (q_7 = 1/4) is interesting but not evidential until tested at higher truncation. The test is clean: compute at max_pq_sum = 4, 5, 6 and check convergence. If it converges to pi/4, the equality would imply a sum rule relating BCS weights across all representations. If it drifts, it is an artifact of truncation at max_pq_sum = 3. I endorse the computation (O-2 in the synthesis) without predicting the outcome.

---

## Section 3: Collaborative Suggestions

### S-1: Explicit GL Free Energy on SU(3) with Jensen Metric

The 0D GL free energy (equation 1 above) can be written explicitly from the computed data. The ingredients are all available:

- a_B2(tau) = 1/V(B2,B2) - rho_B2(E_F) = 1/0.256 - 14.67 = -10.76 (at fold)
- b_B2 from the self-consistent gap equation: b_B2 = rho_B2 / (2 Delta_B2^2) = 14.67 / (2 * 0.732^2) = 13.7
- g_{B1,B2} from V(B1,B2) = 0.080
- g_{B2,B3} from V(B2,B3) = 0.027

This gives the full landscape F(Delta_B1, Delta_B2, Delta_B3; tau) as a function of tau. The computation: evaluate F along the Jensen trajectory for tau in [0, 0.50] and determine whether F_GL has a minimum distinct from the spectral action. The spectral action is the one-body part; F_GL is the many-body correction. They have different functional forms, and their sum may have structure that neither has alone. This was proposed in Session 28 (F-1: V_total = S_spectral + F_BCS) but never fully computed with the corrected parameters from Sessions 34-35.

**What to compute**: F_GL(tau) using the tau-dependent spectrum from s44_dos_tau.npz with the corrected V matrix from s35_thouless_multiband.npz. Plot S_spectral(tau) + F_GL(tau) and check for local extrema.

**Expected outcome**: Likely monotone (OCC-SPEC-45 found F_total monotone with scale separation 5.5 x 10^{-7}). But the S47 curvature anatomy data provides the explicit curvature-dependent coefficients that may modify the conclusion.

### S-2: Collective Modes of the Condensate

In a multi-band superconductor, the order parameter supports three types of collective excitation (Paper 08; MgB2 literature):

1. **Goldstone mode**: Phase fluctuation of the total condensate. In the framework, this is the U(1)_7 phase mode. Session 38 showed this mode ceases to exist post-transit (no condensate = no phase).
2. **Higgs (amplitude) mode**: Oscillation of |Delta| about equilibrium. Energy ~ 2 Delta_B2 = 1.464. This mode IS the pair vibration (omega_att = 1.430, Session 37).
3. **Leggett mode**: Relative phase oscillation between bands. Energy ~ sqrt(Delta_B2^2 * g_{B2,B3} / rho_B3). With the numbers above: omega_L ~ sqrt(0.732^2 * 0.027 / 0.48) ~ 0.18.

**What to compute**: The Leggett mode frequency from the inter-sector coupling matrix. The BdG Hamiltonian in the (B2, B3) sector gives the collective mode spectrum. If omega_L < 2 Delta_B3 = 0.168, the Leggett mode is below the B3 pair-breaking threshold and represents a sharp resonance. If omega_L > 2 Delta_B3, it decays into B3 quasiparticles and broadens.

**Why it matters**: The Leggett mode, if present, would be a NEW collective excitation of the crystal not previously identified. It couples geometry (through the curvature-dependent V matrix) to inter-band dynamics. The curvature anti-correlation (Section 5.2) predicts that the Leggett mode frequency should decrease as tau increases (softer curvature = weaker restoring force), potentially reaching zero at a critical tau. A zero-frequency Leggett mode signals a new instability: relative-phase unlocking between B2 and B3.

### S-3: Topological Defect Classification

The order parameter manifold for the K_7 BCS condensate is U(1) (the phase of the complex gap function Delta_B2). The relevant homotopy groups are:

- pi_0(U(1)) = 0: no domain walls from U(1) breaking alone.
- pi_1(U(1)) = Z: vortex lines (quantized circulation). These are the K_7 vortices.
- pi_2(U(1)) = 0: no monopoles.

BUT: the Z_3 center symmetry of SU(3) imposes additional structure. The condensate at the Z_3 center (2pi/3, 2pi/3) has |Delta|^2 = 1/8, which is nonzero but reduced. The Z_3 symmetry means the full order parameter space is U(1) x Z_3, with homotopy:

- pi_0(U(1) x Z_3) = Z_3: three-fold domain walls (Z_3 Potts walls, Session 33).
- pi_1(U(1) x Z_3) = Z: standard vortices, but with Z_3 fractionalization of the winding number.

**What to compute**: The Z_3 domain wall energy from the condensate profile. The wall interpolates between identity-centered and Z_3-centered condensates. The wall width is set by the condensate 1/e^2 radius (~0.78 rad). The wall energy per unit area is sigma ~ integral of gradient term across the wall, which in 0D is just the energy difference times the coherence volume.

### S-4: Superfluid Density Tensor

The superfluid density rho_s is the second derivative of the free energy with respect to a phase twist (Paper 08, London equation):

    rho_s^{ab} = d^2 F / d(nabla_a phi) d(nabla_b phi)                         (4)

In a multi-band system on a non-isotropic manifold, rho_s is a tensor. The 8 directions of SU(3) yield an 8x8 superfluid density tensor. This tensor inherits the block structure of the Jensen metric: u(1) x su(2) x C^2. Its eigenvalues in each block determine the superfluid stiffness along each geometric direction.

**What to compute**: Using the Peotta-Torma formula (Session 32, CT-1: D_s = 2 g_B2 from geometric weight), compute the full rho_s tensor. The diagonal elements give the superfluid stiffness along each Lie algebra direction. The off-diagonal elements measure the anisotropic superfluid response.

**Prediction**: rho_s should be ZERO along the flat u(1)-su(2) directions (no curvature = no restoring force for phase gradients in those planes) and maximal along the hard su(2)-su(2) directions (strongest curvature = strongest phase stiffness). This would confirm that the "hard directions" of the crystal are also the "stiff superfluid directions."

### S-5: Critical Behavior Near the Fold

The fold at tau = 0.19 is a point where the BCS gap is finite (2 Delta_B2 = 1.464) and the system is in the 0D limit. There is no continuous phase transition at the fold in the thermodynamic sense -- the system is too small for spontaneous symmetry breaking. Instead, the relevant question is: what happens when tau is tuned through the fold?

The answer is the Kibble-Zurek quench (Session 37-38). The "critical behavior" is the KZ scaling of defect production. But the curvature anatomy from Session 47 adds new content: the curvature anisotropy K_max/K_min grows from 4.0 at tau = 0 to 12.5 at the fold and continues growing. This means the "crystal" becomes increasingly anisotropic during transit. In KZ language, the correlation length xi(tau) is itself anisotropic: it is longer along the soft directions and shorter along the hard directions. The post-transit defect density should reflect this anisotropy.

**What to compute**: Anisotropic KZ scaling. The defect density in the soft su(2)-C^2 sector should follow n_soft ~ (tau_Q)^{-12 nu / (12 nu + z)} (12 soft modes), while the hard su(2)-su(2) sector gives n_hard ~ (tau_Q)^{-3 nu / (3 nu + z)} (3 hard modes). The TOTAL defect density is the sum, but the ANISOTROPY of defect production is a prediction: more defects in the soft directions. This is testable against the 59.8 quasiparticle pairs from Session 38.

---

## Section 4: Connections to Framework

### "The Crystal IS the Physics" in Landau Language

In the Landau theory of phase transitions, the physical system is characterized entirely by its symmetry group, order parameter, and the most general free energy consistent with both (Paper 04). The microscopic Hamiltonian is irrelevant for universal properties. What matters is:

1. What is the symmetry group? **SU(3)_L x SU(3)_R / Z_3, breaking to U(2) under Jensen deformation.**
2. What is the order parameter? **The Jensen deformation parameter tau (geometry) and the BCS gap Delta_B2 (pairing).**
3. What is the free energy? **S_spectral(tau) + F_GL(Delta; tau) -- the spectral action for geometry, the GL functional for pairing.**

In this language, "the crystal IS the physics" translates to: the Landau free energy landscape on the space of Jensen metrics, decorated by the BCS instability on each metric, determines all thermodynamic properties. The curvature branches are the harmonic expansion coefficients of this landscape. The condensate is the order parameter field evaluated at the minimum. The spectrum is the set of normal mode frequencies. Everything Tesla describes in the synthesis IS the Landau theory of the Jensen crystal.

The Session 38 Ordered Veil result -- that the substrate is integrable and the transit produces a permanent non-thermal GGE relic -- is Landau theory applied to the quench dynamics. The GGE is the Landau equilibrium state subject to the constraints imposed by the 8 Richardson-Gaudin integrals (Paper 20, Rigol). The GL-GGE stability analysis from Session 45 (the GGE is a Morse-index-3 saddle, stabilized by integrability) is the Landau stability analysis of this constrained equilibrium.

### The Condensate Geometry and the Ordered Veil

The identity-peaked condensate profile provides the spatial resolution of what the Ordered Veil looks like. The Cooper pairs are concentrated within 1/e^2 radius = pi/4 of the identity on SU(3). Post-transit, when the condensate is destroyed (P_exc = 1.000), the quasiparticle excitations are born in this same region of SU(3). The GGE relic state is therefore NOT uniformly distributed on the internal manifold -- it carries the imprint of the identity-peaked pre-transit condensate.

This is the condensed matter analog of the CMB temperature anisotropy pattern: the post-recombination photon distribution reflects the pre-recombination acoustic oscillation pattern. Here, the post-transit quasiparticle distribution on SU(3) reflects the pre-transit condensate pattern. The Haar-weighted shell at r = 0.85 rad is the "last scattering surface" of the internal manifold.

---

## Section 5: Open Questions

**Q-1**: Does the C^2 isotropization trend continue beyond tau = 0.25, and if so, does the curvature ratio within-doublet/cross-doublet reach exactly 1.0 at some tau_iso? If it does, the SU(3) coset acquires an emergent SO(4) symmetry at tau_iso, with potential consequences for the universality class of fluctuations in the coset sector. This is a purely geometric question answerable from the Riemann tensor formulas.

**Q-2**: Is there a Pomeranchuk instability in the CURVATURE channel? Session 22c found f_{0,0} = -4.687 < -3 in the pairing channel. The curvature anatomy now provides the stiffness tensor. A Pomeranchuk instability in curvature would mean that the Jensen crystal spontaneously distorts away from the one-parameter Jensen family into a more general left-invariant metric. The Session 29b transverse Hessian (B-29d) found 2/4 negative eigenvalues, confirming that the Jensen trajectory is a saddle, not a minimum, in the full metric space. The curvature branches provide the eigenvalues of the fluctuation operator that determines WHICH directions are unstable.

**Q-3**: What is the CONDENSATE CONTRIBUTION to the cosmological constant? In Volovik's framework (Paper 19, Section on Lambda from gap energy), Lambda ~ Delta^4. Here, Delta_B2 = 0.732 M_KK. The condensation energy is E_cond = -0.115 M_KK (Session 35). The cosmological constant receives a contribution from the difference between the vacuum energy WITH and WITHOUT the condensate. In the GGE relic state (condensate destroyed), the vacuum energy changes by exactly |E_cond|. Is this the residual cosmological constant?

**Q-4**: The protected chain q_7^2 = K = 1/16 is exact in the (0,0) sector. Does it survive at the level of EFFECTIVE quantities when summed over all Peter-Weyl sectors? The K_7 mixing in higher reps (9.5-13.4%, Session 47 W1-2) means the effective q_7 is no longer exactly 1/4 in those sectors. Does the BCS-weighted effective q_7^2, averaged over all representations, remain close to 1/16? Or does the protected chain break when non-trivial PW sectors are included?

---

## Closing Assessment

Tesla's synthesis is the most structurally complete description of the Jensen crystal produced in 47 sessions. It achieves what a Landau classification demands: the identification of all symmetry-allowed structures (6 curvature branches, 3 spinor sectors, 2 protected invariants), the order parameter profile (identity-peaked condensate), and the soft-mode structure that determines the dynamics (su(2)-C^2 softening driving B2 pairing). The protected chain q_7^2 = K(u(1), C^2) = 1/16 is a structural theorem connecting the pairing quantum number to the geometric invariant. The B2 funnel (50% to 91%) is normal multi-band BCS physics, not a mystery.

What remains is the fourth view: the Dirac eigenfunctions. Eigenvalues tell you the frequencies of the crystal's normal modes. Eigenfunctions tell you their shapes. Without shapes, the connection between "where the condensate lives" (identity peak) and "which modes the condensate is made of" (B2 spectrum) remains inferential. The computation is concrete, the data infrastructure exists, and the result would close the loop between spectrum, condensate, and geometry.

The crystal has spoken in three voices -- condensate, curvature, spectrum. They say the same thing. A condensed matter theorist recognizes this convergence: it is a well-ordered system telling you its symmetry, its soft modes, and its ground state. The task now is to listen precisely enough to extract quantitative predictions.
