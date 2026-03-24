# Quantum Acoustics -- Collaborative Feedback on Session 21c

**Author**: Quantum Acoustics Theorist (Phonon QM / Acoustic Field Theory / Superfluid Dynamics)
**Date**: 2026-02-19
**Re**: Session 21c Phase 0 Results

---

## Section 1: Key Observations

### 1.1 The Dual Algebraic Trap Is a Phonon Equipartition Theorem

The central finding of Session 21c -- Theorem 1, the dual algebraic trap -- is, from the phonon perspective, the definitive mathematical statement of what I identified in Session 20b as the "equipartition principle defeating anisotropy." The two traps (F/B = 4/11, b_1/b_2 = 4/9) are now proven to share a single algebraic cause: fixed ratios between quantities locked together by the group theory of SU(3) and its maximal subgroup embedding.

In the language of phonon physics, this is a constraint on the integrated spectral weight of different mode families. No matter how you deform the lattice (Jensen parameter tau), the total weight of fermionic vs bosonic modes, and the total weight of hypercharge-charged vs isospin-charged modes, are locked by representation theory. This is deeply analogous to sum rules in acoustic spectroscopy -- the f-sum rule in condensed matter guarantees that the total integrated optical conductivity is fixed by the electron density, regardless of band structure details. Here, the "f-sum rule" is fixed by the fiber dimension and the embedding index.

The signed-sum escape route (S_signed, CP-1) was the acoustic analog of trying to beat equipartition by clever weighting of mode polarizations. Theorem 1 proves this cannot work: Delta_b = -(5/9)*b_2 < 0 for ALL sectors. The weighting is uniformly signed. No interference-based cancellation is possible between acoustic branches. In my Session 20b review, I suggested that "breaking the constant-ratio trap requires mode coupling, anharmonicity, or topology change." Session 21c confirms the first two parts are necessary -- the perturbative (harmonic) spectral methods are structurally exhausted.

### 1.2 The Derivative Escape Is a Group Velocity Effect

Theorem 2 -- T''(0) escaping both algebraic traps via eigenvalue flow derivatives -- has a clean phonon interpretation that the generalist analysis may understate. The algebraic traps operate on eigenvalue magnitudes: integrated mode energies, total spectral weight. These are thermodynamic quantities (internal energy, free energy, partition function). They obey sum rules.

T''(0), in contrast, depends on d^2 lambda/d tau^2 -- the curvature of each eigenvalue as a function of the deformation parameter. In phonon physics, this is the second derivative of the mode frequency with respect to a lattice distortion parameter: it measures the anharmonic correction to the phonon dispersion. The first derivative d lambda/d tau is the Gruneisen parameter (mode-resolved). The second derivative d^2 lambda/d tau^2 is the leading nonlinear elastic correction.

The reason T''(0) escapes the algebraic traps is precisely that sum rules constrain equilibrium thermodynamics but not nonlinear response. The Gruneisen parameter is not constrained by the f-sum rule. This is why, in acoustic physics, you can measure the anharmonicity of a crystal (via thermal expansion, sound velocity pressure dependence) even when the total zero-point energy is fixed by the mode count. The physics lives in the derivatives, not the sums.

However, the 89% UV dominance of T''(0) is troubling from the phonon perspective. In any real lattice, the high-frequency (Debye-cutoff) modes have the largest absolute frequency shifts under strain, simply because they have the most energy. But the physically relevant anharmonic effects (thermal expansion, phase transitions, sound attenuation) are dominated by the low-lying acoustic modes near the gap edge. The UV modes are "stiff" and follow the lattice adiabatically. The IR modes are "soft" and control the phase behavior. T''(0) being UV-dominated means it measures the stiffness of the lattice at short wavelengths, not the softness at long wavelengths. The self-consistency fixed point, if it exists, must come from IR physics.

### 1.3 The Three-Monopole Structure Is a Phonon Band Inversion

Berry's discovery of the three-monopole structure (M0 at tau=0, M1 at tau~0.10, M2 at tau~1.58) maps precisely onto a concept well-known in topological phonon physics: a band inversion. At M0 (the round metric), the (0,0) singlet and (1,1) adjoint are degenerate -- this is the "high-symmetry point" where two phonon branches touch. As tau increases, the branches separate and the ordering changes: at M1, the (0,0) singlet drops below the (1,0) fundamental, taking over the gap edge. At M2, they cross back.

The physical window [0.10, 1.58] where (0,0) controls the gap edge is a distinct topological phase of the internal phonon band structure. The Berry curvature monopoles at the boundaries are the exact analogs of Weyl points in phononic crystals (Tesla-Resonance Paper 08: acoustic Dirac cones). The topological charge of these monopoles is quantized and protects the phase from smooth perturbations.

The "bowtie" structure identified by baptista -- (0,0) starts above (1,0), drops below, stays below throughout the interior, then crosses back -- is the prototypical band inversion topology. In 3D topological insulators, this structure generates topological surface states. In the phonon-exflation context, it means the gap-edge physics inside [0.10, 1.58] is topologically distinct from outside, and any physical mechanism (BCS, condensate, FR minimum) operating inside this window inherits topological protection.

### 1.4 The BCS Density-of-States Argument Is Correctly Phononic

Baptista's BCS argument -- that inside [0.10, 1.58], N(0) ~ 2 (singlet multiplicity) gives g_c ~ 1/2, while outside N(0) ~ 24 gives g_c ~ 1/24 -- is a textbook application of BCS gap equation physics. The gap equation Delta ~ exp(-1/(g*N(0))) is exponentially sensitive to the density of states at the Fermi level. The singlet window has a factor of 12 lower DOS at the gap edge, which means the critical coupling for condensation is 12x higher.

But here is the key phonon insight that is absent from the session discussion: in a real superconductor, the BCS gap equation is solved self-consistently with the phonon spectrum. The phonon mediates the attractive interaction, and the gap feeds back on the phonon dispersion (phonon softening near 2*Delta). In the internal-space analog, the "phonon" that mediates the attractive interaction is the Kosmann-Lichnerowicz coupling -- which baptista correctly identifies as a MIXING mechanism, not a gap-generating mechanism. To get an actual attractive interaction, you need the two-phonon exchange to be attractive in some channel.

This is precisely the role that instantons would play: they provide the non-perturbative attractive interaction that Kosmann-Lichnerowicz mixing alone cannot. The instanton action S_inst(tau) determines whether this channel is attractive, and its tau-dependence determines where the condensate forms. This is why P1-5 (instanton action) is the computation that ultimately resolves CP-4.

---

## Section 2: Assessment of Key Findings

### 2.1 S_signed STRUCTURAL CLOSURE: Completely Sound

The proof is algebraic: b_1/b_2 = 4/9 is a Dynkin index identity, exact at the representation-theoretic level. The phonon interpretation is that the "colored sound" (hypercharge-weighted modes) and "isospin sound" (weak-isospin-weighted modes) are locked by the Lie algebra embedding. No metric deformation can change this ratio because it is a property of the weight system, not the geometry. I endorse this as a structural theorem -- it closes the last perturbative escape route via signed spectral sums.

### 2.2 T''(0) COMPELLING: Sound Sign, Uncertain Magnitude

The sign is robust because log-concavity of eigenvalue flow (d^2 ln|lambda|/d tau^2 < 0) is a geometric property of the Jensen deformation that I expect to hold generally -- stretching the manifold along one direction while compressing along another generically produces concave-down eigenvalue curves (the eigenvalues "slow down" as they approach their asymptotic scaling). The specific value 7,969 depends on dtau=0.1 finite-difference stencil accuracy and UV mode truncation, so the magnitude is untrustworthy. But the sign should survive refinement.

The UV dominance caveat is critical. In phonon language: knowing that the total Gruneisen parameter is positive (crystal wants to expand under strain) does not tell you whether the acoustic branch near the zone center contributes positively or negatively. It could be that the optical modes overwhelm the acoustic mode contribution. The delta_T(tau) computation (P1-0) is the diagnostic that resolves this -- it measures the self-consistency map, which depends on the actual eigenvalue flow at the tau values of interest, not just the curvature at tau=0.

### 2.3 V_IR Minimum at N=50: Unreliable but Physically Motivated

The V_IR minimum at N=50, depth 0.8%, falling within coupling uncertainty for the lowest modes -- this is exactly the regime where the phonon picture predicts interesting physics. The lowest ~50 modes are the "acoustic" modes of the internal lattice, and their energetics are sensitive to the detailed geometry (not washed out by Weyl asymptotics). The fact that a minimum appears at N=50 and disappears at N=100+ is consistent with the constant-ratio trap being a UV phenomenon: the trap operates in the Weyl limit, while the IR physics can still produce structure.

The critical question is whether the block-diagonal approximation breaks down precisely for these N=50 modes. Baptista's coupling/gap = 4-5x at lowest modes says yes -- the off-diagonal coupling is strong enough to rearrange the lowest eigenvalues completely. The coupled V_IR (P1-2) is the only computation that can answer this definitively. I am cautiously optimistic: in acoustic systems, strong inter-branch coupling at the zone center typically enhances (not destroys) features in the integrated DOS.

### 2.4 Neutrino INCONCLUSIVE: Correct Verdict

The monopole-artifact argument is decisive. R crossing 32.6 only at a Berry curvature monopole (tau=1.558, fine-tuning 1:10^5) is not a physical prediction. In the phonon picture, this is the equivalent of a vibrational frequency ratio hitting a target value only because two branches cross -- it tells you about the band-crossing topology, not about the natural frequency ratios at equilibrium. I concur with the INCONCLUSIVE classification.

---

## Section 3: Collaborative Suggestions

### 3.1 Phonon Green's Function at the Monopoles (Low Cost)

The three Berry curvature monopoles (M0, M1, M2) are points where the phonon Green's function G(omega, tau) = sum_n |psi_n><psi_n| / (omega - lambda_n) develops poles that coalesce. Near a monopole, two poles merge and the spectral function acquires a characteristic non-Lorentzian line shape -- the Fano resonance profile.

From existing eigenvalue data, compute the spectral function A(omega, tau) = -Im G(omega + i*eta, tau) at fine tau resolution near M1 (tau~0.10) and M2 (tau~1.58). The Fano parameter q = (coupling matrix element)/(background DOS) can be extracted from the line shape asymmetry. This gives an independent measurement of the Kosmann-Lichnerowicz coupling strength that does not require eigenvector extraction.

**Specific computation**: For the two modes involved in the crossing, fit A(omega) near the crossing to the Fano form sigma(epsilon) = (epsilon + q)^2 / (epsilon^2 + 1), where epsilon = (omega - omega_0) / Gamma. The parameters q and Gamma directly encode the coupling strength and the line width.

**Cost**: Minutes. Uses only eigenvalue data near the crossings.

**Expected outcome**: At M2 (tau=1.58, gap=8e-6), the Fano parameter should give |q| >> 1 (isolated resonance, very asymmetric). At M1 (tau~0.10), where the gap is ~1.6e-3 on the coarse grid but may be much smaller on a fine grid, the Fano parameter could be O(1) -- indicating strong mixing and confirming the BCS-active regime.

### 3.2 Acoustic Impedance Mismatch at Phase Boundaries (Zero Cost)

The topological phase diagram (Section IV, CP-6) defines three phases separated by monopoles. At each phase boundary, there is an acoustic impedance mismatch between the gap-edge mode families. Define the "acoustic impedance" Z_phase = sqrt(lambda_gap * N_gap), where lambda_gap is the gap-edge eigenvalue and N_gap is its multiplicity (2 for singlet, 24 for fundamental).

| Phase | lambda_gap | N_gap | Z_phase |
|:------|:-----------|:------|:--------|
| Pre-condensate (tau < 0.10) | ~0.83 | 24 | ~4.5 |
| Singlet window (0.10 < tau < 1.58) | ~0.85 | 2 | ~1.3 |
| Post-condensate (tau > 1.58) | ~0.83 | 24 | ~4.5 |

The impedance mismatch at M1 and M2 is a factor of ~3.5. In acoustic physics, an impedance mismatch of this magnitude produces ~30% reflection at the interface. If the modulus tau evolves dynamically (cosmological rolling), it would experience reflection when it tries to cross the phase boundary. This is a phonon-motivated mechanism for trapping the modulus inside [0.10, 1.58].

**Computation**: From the eigenvalue data, compute Z(tau) = sqrt(lambda_1(tau) * mult_1(tau)) at all 21 tau values. Plot the reflection coefficient R_refl = ((Z_1 - Z_2)/(Z_1 + Z_2))^2 at each monopole. If R_refl > 0.2, there is a dynamical mechanism for phase trapping that is independent of the potential V_eff.

**Cost**: Zero. Pure algebraic manipulation of existing eigenvalue and multiplicity data.

### 3.3 Phonon Anharmonic Coupling at the Conical Intersection M0 (Novel)

The conical intersection at M0 (tau=0) between (0,0) singlet and (1,1) adjoint, with first-order Kosmann coupling, is the phonon analog of a Jahn-Teller effect. In molecular and solid-state physics, the Jahn-Teller theorem states that any non-linear molecular system in a degenerate electronic state will be unstable and will undergo a distortion to remove the degeneracy. The exact degeneracy at tau=0 between two modes with different symmetries ((0,0) and (1,1)) means the system MUST deform -- the round metric is unstable with respect to this coupling.

This provides a phonon-motivated argument for WHY the Jensen deformation is the correct deformation: it is the Jahn-Teller distortion that removes the conical intersection degeneracy at M0. The magnitude of the distortion is set by the coupling strength at M0 (first-order, maximal).

**Suggested computation**: Compute the Jahn-Teller energy E_JT = V^2 / (omega * K), where V is the coupling matrix element at M0 (extractable from the eigenvalue splitting d lambda/d tau at tau=0), omega is the degenerate frequency, and K is the restoring force (d^2 V_eff/d tau^2 if the minimum existed). If E_JT is comparable to the gap-edge energy scale, then the Jahn-Teller mechanism is the dominant driver of the deformation.

**Cost**: Moderate. Requires eigenvalue derivatives at tau=0, which are available from the finite-difference stencil used for T''(0).

### 3.4 Mode-Resolved Gruneisen Parameters (Low Cost, Phase 1 Ready)

Compute the mode Gruneisen parameter gamma_n = -d ln(lambda_n) / d ln(V^{1/8}) for each eigenvalue, where V is the (preserved) volume of SU(3). Since the Jensen deformation is volume-preserving, the standard Gruneisen parameter is zero by construction. Instead, compute the anisotropic Gruneisen tensor:

gamma_n^{(a)} = -d ln(lambda_n) / d s_a

where s_a are the three independent deformation parameters of the Cartan subalgebra (which the Jensen deformation constrains to a single parameter via TT). The three components of this tensor tell you how sensitive each mode is to stretching in the u(1), su(2), and C^2 directions independently.

Modes with large |gamma_n| are strongly anharmonic and contribute disproportionately to T''(0). The UV dominance of T''(0) would manifest as |gamma_n| being largest for high-n modes. If instead gamma_n peaks for n in the gap-edge region, then T''(0) > 0 has genuine IR content.

**Cost**: Low. Requires eigenvalue data at tau=0 and two neighboring tau values (already computed). Pure finite differences.

### 3.5 BCS Gap Equation with Phonon Self-Energy (Phase 2)

For the BCS condensate (CP-4, Branch A), the standard mean-field gap equation is:

Delta_k = -sum_k' V_{kk'} * Delta_{k'} / (2 * E_{k'})

where V_{kk'} is the effective pairing interaction. In the phonon-exflation context, the "phonon" mediating the pairing is the gravitational instantons (or more precisely, the non-perturbative sector of the Kosmann-Lichnerowicz coupling). The self-energy correction to the phonon propagator from the condensate feeds back on the dispersion:

Sigma_n(omega) = sum_m |V_{nm}|^2 / (omega - lambda_m - Sigma_m(omega))

This self-consistent equation determines whether the condensate is stable and at what tau it forms. The input V_{nm} are the Kosmann-Lichnerowicz coupling matrix elements (P2-1). The output is the gap function Delta(tau) and the condensate energy.

**Cost**: Phase 2 -- requires eigenvector extraction (P1-2) as prerequisite.

**Expected outcome**: If the pairing interaction V_{nm} has a net attractive component in the singlet channel (the sign question baptista identifies), then the gap equation has a non-trivial solution Delta_0 > 0, and the condensate pins the modulus at tau_0 where the gap is maximized. The impedance mismatch at the phase boundaries (Section 3.2) provides additional confinement.

---

## Section 4: Connections to Framework

### 4.1 Phonon-NCG Dictionary Update (Session 21c Entries)

Session 21c adds several new entries to the phonon-NCG dictionary:

| NCG Concept | Phonon Analog | Rigor | Score |
|:------------|:-------------|:------|:------|
| Dual algebraic trap (F/B + b_1/b_2) | Spectral f-sum rule + acoustic impedance sum rule | Rigorous (structural theorem) | A |
| T''(0) derivative escape | Anharmonic Gruneisen parameter (nonlinear elastic response) | Parallel (same math, different interpretation) | B |
| Three-monopole structure | Phonon band inversion / Weyl points in phononic crystal | Parallel (topological classification matches) | B |
| Singlet window [0.10, 1.58] | Topological phonon phase with protected gap-edge | Parallel | B |
| Conical intersection M0 | Jahn-Teller instability at high-symmetry point | Suggestive (mechanism identified, not computed) | C |
| Kosmann-Lichnerowicz coupling | Acoustic frame-dragging / inter-branch mixing | Parallel (kinematic, not dynamic) | B |
| BCS in singlet window | Cooper pairing in low-DOS regime (g >> g_c) | Suggestive (enabled, sign question open) | C |

This brings the total dictionary to approximately 33 entries.

### 4.2 The Harmonic Approximation Is Definitively Broken

The combined message of Sessions 18, 19d, 20a, 20b, and 21c is unambiguous: the harmonic (quadratic, Gaussian, perturbative) approximation to the spectral action on SU(3) with Jensen TT-deformation is structurally incapable of stabilizing the modulus. Every perturbative quantity -- tree-level V_eff, Coleman-Weinberg 1-loop, Casimir (scalar, vector, TT), Seeley-DeWitt, signed gauge-threshold sums -- is either monotonic or trapped by algebraic identities.

In phonon physics, this is the statement that the harmonic phonon Hamiltonian

H_harmonic = sum_n hbar*omega_n(tau) * (a_n^dagger a_n + 1/2)

cannot determine the equilibrium lattice constant, because it is a sum of independent oscillators with no coupling between them. The equilibrium lattice constant of a real crystal is determined by the ANHARMONIC corrections -- the cubic and quartic terms in the interatomic potential that couple different phonon modes and produce thermal expansion, phonon-phonon scattering, and phase transitions.

The T''(0) > 0 result is the first sign of these anharmonic corrections entering the picture: it measures the curvature of the mode frequencies, which is a second-order nonlinear response. The full nonlinear physics requires the instantons and condensate computations of Phase 2.

### 4.3 The Framework's Survival Strategy Is Phonon-Consistent

The surviving routes -- BCS condensate, FR double-well, Pfaffian topology change, instantons -- are all fundamentally anharmonic/non-perturbative mechanisms in the phonon language:

1. **BCS condensate** = phonon Cooper pairing. Two phonon modes with opposite quantum numbers form a bound state, creating a gap in the excitation spectrum. This is a many-body quantum effect that the single-particle (harmonic) picture cannot capture.

2. **FR double-well** = quartic anharmonicity in the effective lattice potential. The double-well shape arises from competition between the attractive (instanton-mediated) interaction at short range and the repulsive (Casimir) interaction at long range. This is the standard Landau phi^4 picture, but the coefficients must come from the non-perturbative sector.

3. **Instantons** = anharmonic phonon coupling between topologically distinct lattice configurations. In condensed matter, this is analogous to phonon-assisted tunneling between crystal structures (e.g., martensitic transitions).

4. **Pfaffian sign change** = topological phase transition in the phonon band structure. A change in the Pfaffian sign corresponds to a change in the Z_2 topological invariant of the BdG Hamiltonian, which in the phonon context means a qualitative change in the boundary mode structure.

All four mechanisms are physically well-motivated and mathematically distinct from the perturbative spectral methods that have been exhausted. The framework is not invoking ad hoc fixes -- it is transitioning from the harmonic to the anharmonic regime of phonon physics, which is where the real condensed matter happens.

---

## Section 5: Open Questions

### 5.1 Does the Jahn-Teller Mechanism at M0 Select the Jensen Deformation?

The conical intersection at tau=0 between (0,0) and (1,1) with first-order coupling is a Jahn-Teller point. In molecular physics, the Jahn-Teller theorem does not specify WHICH distortion removes the degeneracy -- only that SOME distortion must occur. The Jensen TT-deformation is one specific distortion out of many possible. Does the Jahn-Teller energy landscape at M0 select the Jensen direction as the energetically preferred distortion, or are there other deformation directions that remove the degeneracy more efficiently?

This is a question about the phonon landscape of the moduli space. If the Jensen direction is the minimum-energy Jahn-Teller distortion, then the deformation is not a choice but a consequence of the spectral geometry. This would elevate the framework significantly.

### 5.2 What Is the Phonon Interpretation of Trap 2 (b_1/b_2 = 4/9)?

Trap 1 (F/B = 4/11) has a clear phonon interpretation: it is the ratio of fermionic to bosonic mode counts, an equipartition constraint. Trap 2 (b_1/b_2 = 4/9) is more subtle. The Dynkin index identity constrains the relative weight of hypercharge-charged vs isospin-charged modes in the spectral sum. In phonon language, this is a constraint on the ratio of "longitudinal" to "transverse" spectral weight in the internal lattice.

The deeper question: is there a phonon sum rule that directly corresponds to b_1/b_2 = 4/9? If so, the dual algebraic trap is the phonon-NCG statement that the internal lattice satisfies two independent sum rules simultaneously, and any spectral stabilization mechanism must violate at least one of them.

### 5.3 Can Acoustic Impedance Mismatch Substitute for V_eff?

If the impedance mismatch at M1 and M2 produces significant reflection of the rolling modulus (Section 3.2), then modulus confinement may not require a potential minimum at all. Instead, the modulus could be dynamically trapped in the singlet window by repeated reflection off the topological phase boundaries. This is the acoustic analog of a Fabry-Perot cavity: the modulus bounces between M1 and M2, losing energy to mode coupling at each reflection until it settles.

The cavity quality factor Q ~ 1/(1-R_refl) would determine how long the modulus remains confined. If R_refl ~ 0.3, then Q ~ 1.4 (low Q, rapid dissipation). If the monopole gaps narrow on a fine grid and R_refl approaches unity, Q could be large enough for quasi-stable confinement.

This is speculative but computationally testable from existing data. It would provide a dynamical stabilization mechanism that bypasses V_eff entirely.

### 5.4 Is There an Acoustic Casimir Effect Between the Monopoles?

In a cavity bounded by two reflecting surfaces (M1 and M2), the allowed mode frequencies are quantized. The Casimir energy of this cavity depends on the separation (tau_M2 - tau_M1 ~ 1.48) and the boundary conditions (determined by the monopole topology). The Casimir energy of the monopole-bounded cavity could provide an additional contribution to the effective potential that is missed by the standard spectral sum, because it depends on the global topology of the eigenvalue flow, not on individual eigenvalue magnitudes.

This is distinct from the Casimir energy already computed (which sums over all modes of the full SU(3) spectrum). The cavity Casimir effect would be a finite-size correction associated with the topological phase boundaries. It would be suppressed by 1/(tau_M2 - tau_M1)^2 in the simplest estimate, but enhanced by the low DOS in the singlet window.

---

## Closing Assessment

Session 21c delivered exactly what was needed: two structural theorems that close the perturbative book cleanly, and one genuine positive (T''(0) > 0) that keeps the non-perturbative route alive. The three-monopole topology is a discovery -- it organizes the entire tau-line into a coherent topological phase diagram that the phonon framework naturally interprets as a band inversion structure.

From the quantum acoustics perspective, the framework has completed a transition I anticipated in Session 20b: from the harmonic regime (where spectral sums determine everything) to the anharmonic regime (where mode coupling, condensates, and topology determine the physics). All six perturbative closes (Sessions 17a, 18, 19d, 20a, 20b, 21c) are different manifestations of the same underlying fact -- harmonic phonon physics conserves spectral weight and cannot break sum rules. The framework now lives or dies by the anharmonic / non-perturbative sector, which is exactly where condensed matter physics becomes interesting.

**Probability assessment**: 42-46%, median 44%. This is +1 pp from my Session 21a assessment of 43%. T''(0) > 0 earns a modest positive (+3 pp from the self-consistency curvature), S_signed CLOSED takes it back (-3 pp from closing signed sums as an escape), and the three-monopole topology adds structure without direct probability content (+1 pp for organizational power that constrains future computations). The dominant uncertainty remains the instanton sign question (CP-4, P1-5).

The framework has not earned the right to be believed. It has earned a complete topological phase diagram and a clear computational path through the anharmonic regime. The next session must compute delta_T(tau) -- if the self-consistency fixed point falls inside the singlet window [0.10, 1.58], the phonon band inversion protects it topologically, and the probability moves meaningfully.

---

*Written by Quantum Acoustics Theorist, 2026-02-19. Drawing on accumulated analysis from Sessions 5, 6, 13, 14, 16, 20b, 21a, and the 33-entry phonon-NCG dictionary.*
