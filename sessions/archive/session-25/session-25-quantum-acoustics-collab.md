# Quantum Acoustics -- Collaborative Feedback on Session 25

**Author**: Quantum-Acoustics-Theorist
**Date**: 2026-02-21
**Re**: Session 25 -- Through the Walls

---

## Section 1: Key Observations

The Session 25 directive is the first document in this project's history that speaks fluently in the phononic language. The four walls (W1-W4) are, from the phonon physicist's perspective, four theorems about the harmonic phononic lattice on SU(3). I will restate them in my native formalism and then explain why the escape routes proposed in the directive are not speculative -- they are the standard next steps in any condensed matter program that has exhausted its harmonic analysis.

**The Four Walls in Phonon Language:**

- **W1 (Perturbative Exhaustion)**: The free energy F = sum_n f(omega_n) of a harmonic phonon crystal is a smooth functional of the mode frequencies. On SU(3), the asymptotic density of states g(omega) ~ omega^7 (Weyl law on an 8-manifold) locks the ratio of fermionic to bosonic contributions at F/B = 16/44 = 0.364 (spectrally weighted: 0.55). No rearrangement of the harmonic spectrum changes this ratio, and therefore no smooth functional of the harmonic frequencies has a minimum in the deformation parameter tau. This is the phononic statement of the equipartition theorem: in a harmonic lattice, each mode carries the same zero-point energy 1/2 * hbar * omega, and the total scales with the mode count, which is topological.

- **W2 (Block-Diagonality)**: The Peter-Weyl decomposition is the Fourier transform on the group manifold. Block-diagonality of D_K means the phonon modes labeled by different crystal momenta (p,q) propagate independently -- they do not scatter off each other. This is the statement that the SU(3) "lattice" is a perfect crystal with no impurities, no anharmonicity, and no Umklapp processes. In a perfect harmonic crystal, phonon branches do not mix.

- **W3 (Spectral Gap)**: The Dirac spectral gap 2*lambda_min = 1.644 is the phononic band gap of the internal crystal. BCS condensation requires a Fermi surface -- a locus of gapless excitations where the density of states is nonzero. The spectral gap means there are zero states at the Fermi level (mu = 0). This is the phononic statement that an insulator cannot superconduct.

- **W4 (V_spec Monotone)**: The heat kernel expansion of the spectral action is the high-temperature expansion of the phonon free energy. The a_4 term dominates a_2 by 1000:1 because dim_spinor = 16 inflates the anharmonic correction relative to the harmonic restoring force. In a crystal where the quartic anharmonic term is 1000x the harmonic term from the start, there is no perturbative lattice stability -- the crystal runs away into decompactification. This is the phononic statement that a lattice with dominant anharmonic repulsion has no equilibrium configuration in the harmonic approximation.

**The critical observation**: All four walls are statements about the HARMONIC lattice. In condensed matter, the harmonic approximation is the starting point, never the final answer. Real crystals are stabilized by the interplay of harmonic and anharmonic forces, quantum fluctuations beyond mean field, topological constraints on the band structure, and collective phenomena (superconductivity, charge density waves, topological insulation) that are invisible in the harmonic spectrum. Session 25 is proposing exactly this progression: having exhausted the harmonic analysis, move to the phenomena that go beyond it.

---

## Section 2: Assessment of Key Findings

### 2.1 Walls W1-W4: The Harmonic Box

The walls are proven. I have no objections to any of them. What I want to emphasize is the STRUCTURE of the box, because its shape tells us where to look.

W1 and W4 are both statements about smooth spectral functionals. They apply to the ASYMPTOTIC regime (many modes, smooth test functions). W2 is a symmetry statement (exact, all orders). W3 is a spectral property (exact at mu = 0 only).

The weakest wall is W3, because it is conditional on mu = 0. In condensed matter, the chemical potential is never exactly zero in a physical system at finite density. The directive's Goal 7 (self-consistent chemical potential) attacks W3 at its weakest point. The strongest wall is W2, because it is a theorem about left-invariant metrics on compact Lie groups -- it holds for ANY metric in the Jensen family, not just at specific tau values.

### 2.2 Goal 1: Graded Multi-Sector Spectral Sum

This is the Casimir computation done correctly. The previous Casimir analyses (Sessions 19d, 20b) computed the TOTAL spectral action, which is trapped by W1 (constant F/B ratio). Goal 1 proposes the GRADED sum, where bosonic and fermionic contributions carry opposite signs.

From the phonon perspective, this is the transition from the total phonon free energy F_total = F_acoustic + F_optical to the DIFFERENCE F_acoustic - F_optical, which is the physical quantity controlling the Casimir force between two plates. The Casimir force is attractive precisely because the bosonic (photon) and fermionic (electron) zero-point energies have different boundary-condition dependence. The total zero-point energy is monotone (W1), but the signed difference can have a minimum.

**The grading question** raised in the directive is critical: is the sign alternation from chirality (gamma_9) or from sector weighting? For BDI class with spectral symmetry lambda <-> -lambda, the chirality-graded trace Tr(gamma_9 * f(D_K^2/Lambda^2)) vanishes identically, because each eigenvalue lambda contributes equally from both chirality sectors (this is the content of the BDI pairing). The THERMAL graded sum -- weighting sectors by their representation dimensions with bosonic/fermionic signs from the spin-statistics connection -- is the physically correct quantity. This is NOT a chirality sum; it is a Casimir-type sum where the sign comes from the 4D spin of the KK mode (boson vs fermion).

In phonon physics, the acoustic/optical classification provides a natural grading: acoustic modes (k -> 0 linear dispersion) contribute with one sign, optical modes (k -> 0 finite gap) with the other. The gap-edge separation (bosonic 4/9, fermionic 5/6 at tau = 0) means the two types of modes respond DIFFERENTLY to the Jensen deformation. At low mode count (N < 25,000), the F/B ratio deviates from 0.55 by 10-37% (Session 21a). This deviation is the signal: the graded sum amplifies it.

**My assessment**: Goal 1 has the highest expected value among the Tier 1 computations. P(success) ~ 10-15% is fair. If the graded sum has a minimum, it is a genuine zero-parameter prediction.

### 2.3 Goal 2: Full Spectral Action at Finite Cutoff

This is Claim C in computational form. From the phonon perspective, the distinction between the asymptotic (heat kernel) and finite (eigenvalue sum) spectral action is the distinction between the Debye model and the full lattice dynamics.

The Debye model approximates the phonon density of states as g(omega) ~ omega^{d-1} up to a cutoff omega_D, and zero above. It captures the high-temperature thermodynamics correctly but misses all fine structure: Van Hove singularities, band edges, flat bands, and the exponential Boltzmann tail of high-frequency modes. For thermodynamic quantities that depend on the SHAPE of g(omega) -- specific heat peaks, phase transition signatures, thermal conductivity resonances -- the Debye model is inadequate. You need the full phonon density of states.

W4 (V_spec monotone) is the Debye-model statement: the polynomial approximation (a_2 + rho * a_4) of the spectral action is monotone. Goal 2 asks: does the FULL lattice dynamics -- Tr(f(lambda_n^2/Lambda^2)) computed directly from the eigenvalues -- have structure that the Debye approximation misses?

The Berry curvature peak B = 982.5 at tau = 0.10 is the smoking gun that fine structure exists. Berry curvature measures the rate of change of eigenstates, which is large when eigenvalue gaps are small (near-crossings). A Berry curvature of ~1000 means there are eigenvalue pairs with gaps delta_lambda ~ 1/sqrt(B) ~ 0.03 at tau = 0.10. These near-degenerate pairs create oscillatory features in the spectral zeta function that no polynomial (heat kernel) expansion can reproduce. At finite Lambda, these oscillations can constructively interfere to produce a non-monotone V_full.

**The Debye cutoff interpretation**: If f is a physical transfer function (not a mathematical regularizer), then Lambda is the Debye frequency of the internal lattice. The spectral action at Lambda = 1 probes the lowest ~10 modes; at Lambda = 5 it probes ~100; at Lambda = 10 it probes the full spectrum. The behavior of V_full(tau; Lambda) as a function of Lambda tells us whether the stabilization (if it exists) is a LOW-energy phenomenon (Lambda ~ 1, few modes, fine structure matters) or a HIGH-energy phenomenon (Lambda >> 10, many modes, Weyl law dominates). If the minimum appears at Lambda ~ 1-2, it would vindicate Claim C: the Debye cutoff is physical and the harmonic-approximation wall W4 does not apply at the physical scale.

**My assessment**: P(success) ~ 8-12% is fair. The comparison criterion (>20% deviation from heat kernel at any tau for Lambda <= 5) is well-calibrated. If the deviation is large, W4 falls and the framework reopens at the finite-cutoff scale.

### 2.4 Goal 3: Berry Phase Accumulation

This is the computation I proposed in the Session 23 Tesla-take collab (Section 3.3). Let me sharpen the physics.

The Berry connection A(tau) = i * <n|d/d tau|n> defines a gauge field on the modulus space. The integrated Berry phase Phi(tau) = integral_0^tau A(tau') d tau' measures the cumulative rotation of the eigenstate in Hilbert space. When Phi reaches pi/2, the state at tau is orthogonal to the state at tau = 0 -- a quantum phase transition has occurred. When Phi reaches pi, the state has returned to its original orientation (up to a sign) -- a full topological cycle.

In phononic crystals, the Berry phase of phonon bands determines the bulk-boundary correspondence: a band with Berry phase pi supports edge states at the domain boundary. These edge states are topologically protected -- they cannot be removed by smooth deformations of the lattice. If the gap-edge mode on SU(3) accumulates Berry phase pi at some finite tau, it means there is a topological obstruction to smooth deformation past that point. The modulus cannot cross the obstruction without a gap closure (topological phase transition), which would change the character of the ground state.

The Berry curvature B = 982.5 at tau = 0.10 sets the scale. If B were constant at ~1000, a phase of pi would accumulate in delta_tau ~ pi/sqrt(B) ~ 0.1. The actual B is non-uniform (peaks at 0.10, dips at 0.30, rises again at 0.50), so the integral requires the actual data. The eigenvectors are available in s23a_kosmann_singlet.npz.

**Resolution concern**: The directive correctly flags that 9 tau points may under-resolve the Berry phase near tau = 0.10. With B ~ 1000, the Berry connection A(tau) ~ sqrt(B) ~ 30, meaning the phase changes by ~3 radians per unit tau. Over 9 points spanning [0, 0.50], the resolution is delta_tau = 0.0625, giving phase resolution ~2 radians. This is adequate for detecting a pi crossing but inadequate for locating it precisely. The directive's suggestion of 5 additional tau values in [0.05, 0.15] is correct.

**My assessment**: P(success) ~ 10-15% is the right range. The Berry phase computation is the one I am most confident SHOULD be run, regardless of outcome, because it characterizes the spectral geometry in a way no other diagnostic does.

### 2.5 Goals 4-8: Tier 2 and 3

**Goal 4 (Spectral Flow)**: This is the eta invariant question I raised in concept during Session 14 (Section 3.1 of my phonon band structure analysis). Spectral flow -- the net number of eigenvalues crossing zero as tau varies -- contributes a topological term to the effective action that is invisible to every perturbative computation. In phonon physics, spectral flow corresponds to a phonon mode softening to zero frequency and then re-hardening with opposite polarization. It signals a structural instability (soft mode) that typically accompanies a phase transition. If ANY sector has a zero-crossing, it changes the problem qualitatively.

**Goal 5 (Gap-Edge Topological Protection)**: This is the Spectral Insulator Hypothesis I formulated in the Session 23 Tesla-take collab (Section 4.2). The four testable predictions I stated there remain valid. The 2x2 Berry connection matrix for the Kramers pair defines a U(2) holonomy. If the holonomy is non-trivial (determinant != 1 around a loop in parameter space), the gap-edge states are topologically protected. This is the ONLY known condensed-matter mechanism that produces a stable ground state without a potential minimum.

**Goal 6 (Spectral Dimension with TT)**: The spectral dimension d_s(sigma, tau) is the phononic analog of the walk dimension in a random medium. Including TT modes (741,636 DOF) changes d_s substantially because the TT modes cluster at low eigenvalues (Session 19d). If d_s = 4 emerges as a fixed point, the "connectivity getting denser" interpretation of expansion becomes quantitative.

**Goal 7 (Self-Consistent mu)**: This is the most physically motivated escape from W3. In any real lattice at finite temperature, there are thermal excitations that populate states above the gap. The chemical potential adjusts self-consistently to match the particle density. The question is whether the 4D radiation energy density creates an effective mu that fills states up to or above the gap edge. At the Planck epoch, mu_eff ~ M_Pl could easily swamp the gap 2*lambda_min = 1.644 (in KK units). This is not speculative -- it is standard thermal field theory applied to the internal space.

**Goal 8 (Higher Heat Kernel)**: The a_6 and a_8 computation tests whether the heat kernel expansion is alternating or same-sign. In phonon physics, the Debye model's heat capacity C(T) = sum_n partial^2 F / partial T^2 is non-monotone even though the individual terms of the high-T expansion are monotone -- because the alternating-sign series converges to an oscillatory function. If a_6 opposes a_4, the same could happen for V_spec.

---

## Section 3: Collaborative Suggestions

### 3.1 The Physical Transfer Function (My Core Domain)

Claim A states: "The spectral action cutoff function f is not a mathematical regularizer -- it is the physical transfer function of the medium." This is the central claim of the phonon paradigm, and it has a precise mathematical formulation.

In acoustic physics, the transfer function H(omega) of a medium relates the input signal to the output signal: output(omega) = H(omega) * input(omega). For a lattice with Debye cutoff omega_D, the transfer function is:

    H(omega) = 1                 for omega < omega_D
    H(omega) = 0                 for omega > omega_D

More realistically, the transfer function has a smooth rolloff:

    H(omega) = f(omega^2 / omega_D^2)

where f is a smooth function satisfying f(0) = 1 and f(x) -> 0 rapidly for x >> 1. The Chamseddine-Connes test function f(x) = x * exp(-x) is one such choice. In phonon physics, the specific form of f encodes the UV behavior of the lattice -- how modes near the Debye cutoff are damped by the finite lattice spacing.

**Concrete proposal**: Compute V_full(tau; Lambda) for THREE physically motivated test functions:

1. **Sharp cutoff**: f(x) = Theta(1 - x). This is the literal Debye model. It counts modes below Lambda.
2. **Smooth Debye**: f(x) = x * exp(-x). The standard Chamseddine-Connes choice. Exponential rolloff.
3. **Lorentzian**: f(x) = 1/(1 + x)^2. Slower rolloff, emphasizes intermediate modes.

If all three give qualitatively similar behavior (all monotone, or all with a minimum at similar tau), the result is robust to the choice of f. If they differ qualitatively (one monotone, one with a minimum), then the f-dependence issue identified in Session 23c is fatal AND informative: it tells us which spectral range (low, intermediate, high) controls the stabilization.

This is a standard procedure in phonon physics: comparing sharp-cutoff, exponential, and Lorentzian response functions to determine which frequency range dominates a physical quantity. It takes three lines of code per test function.

### 3.2 Dispersion Relation Structure on Deformed SU(3)

I proposed in Session 13 (Section 6 of my phonon interpretation document) that the eigenvalue trajectories lambda_n(tau) constitute an internal dispersion relation with the representation labels (p,q) playing the role of crystal momentum. Eighteen sessions later, this framework remains valid and untested.

**Concrete proposal**: Plot omega_n(p,q; tau) = lambda_n(tau) as a 2D dispersion surface, with the horizontal axes being Casimir C_2(p,q) (or equivalently p+q) and the vertical axis being the eigenvalue. At each tau, this gives a "phonon band structure" of the internal space. The features to look for:

1. **Band crossings or near-crossings**: These are where Berry curvature peaks. The B = 982.5 at tau = 0.10 should correspond to a visible near-crossing in the dispersion plot.

2. **Flat bands**: Eigenvalues that are nearly tau-independent signal heavy effective mass modes. In condensed matter, flat bands produce correlated electron physics (Mott insulators, heavy fermions). On SU(3), flat bands would signal modes that resist the Jensen deformation -- these are the most "rigid" internal excitations.

3. **Acoustic vs optical character**: At tau = 0, the lowest branch (from the (0,0) singlet) is the "acoustic" branch. As tau increases, does this branch remain the lowest, or does a mode from another sector cross below it? A branch crossing would change which representation provides the lightest mode -- equivalent to a change in the ground state character.

This visualization is zero-cost from existing eigenvalue data and would provide the most intuitive picture of what the Jensen deformation does to the internal spectrum.

### 3.3 The Tight-Binding Extension: From 3 Sites to the Full Ladder

In the Session 23 Tesla-take collab, I showed that the V_{nm} matrix in the (0,0) singlet defines a tight-binding Hamiltonian on a 3-site chain. With the extended eigenvector data at p+q <= 6 (s23a_eigenvectors_extended.npz), the tight-binding model can be extended to all sectors independently (by W2).

**Concrete proposal**: For each sector (p,q) with p+q <= 6:

1. Extract the N distinct eigenvalue levels and their degeneracies.
2. Compute the Kosmann coupling matrix V_{nm} between levels.
3. Construct the N x N tight-binding Hamiltonian H_TB^{(p,q)}(tau).
4. Diagonalize to get the molecular-orbital spectrum.
5. Compute the Zak phase of each molecular-orbital band.

The TOTAL tight-binding spectrum across all sectors is the multi-sector band structure of the Kosmann Hamiltonian. The graded sum (Goal 1) can then be computed sector by sector in the tight-binding basis, which provides a PHYSICAL decomposition of the contributions (acoustic branch vs optical branches within each sector).

This computation requires the Kosmann matrix elements for sectors beyond (0,0). If those are not yet available in the .npz files, computing them is the rate-limiting step. If they are available (the s23a files contain data at p+q <= 6), the tight-binding analysis is immediate.

### 3.4 Innovation: The Impedance Mismatch Stabilization

In acoustic physics, a waveguide terminated by an impedance mismatch reflects waves. The reflection coefficient R = (Z_2 - Z_1)/(Z_2 + Z_1) depends on the ratio of impedances. When a phonon crystal has a band gap, the impedance is purely imaginary in the gap -- no propagating modes exist. The interface between a phonon crystal and free space has a perfect impedance mismatch in the gap frequency range.

I propose a new stabilization mechanism based on impedance mismatch at the boundary between the internal space and 4D spacetime. As the Jensen parameter tau varies, the impedance of the internal space (determined by the density of states near the gap) changes. At a specific tau_0, the impedance matching condition between 4D and internal modes is satisfied, creating a resonant cavity. Deforming away from tau_0 breaks the resonance, costing energy.

Mathematically, the impedance is:

    Z(tau; omega) = rho(tau) * v_g(tau; omega)

where rho(tau) = 1/Vol(K) is the (constant) mass density and v_g = d omega / d k is the group velocity. At the band gap, v_g = 0 and Z = 0 (perfect mismatch). Just above the gap, v_g is large (steep band edge) and Z is large. The transition from Z = 0 to Z > 0 creates a sharp impedance feature whose tau-position encodes the stabilization.

This mechanism evades W1 (non-perturbative: depends on the SHAPE of the band edge, not a smooth functional), W2 (operates within each sector independently), W4 (not from the heat kernel), and partially evades W3 (does not require BCS; uses the gap as a resource rather than an obstacle).

**Computation**: requires the group velocity v_g(tau; omega) near the band edge, which is obtainable from the eigenvalue slopes d lambda_n / d tau (already computed for Berry curvature).

---

## Section 4: Connections to Framework

### 4.1 Phonon-NCG Dictionary: Status and New Entries

The phonon-NCG dictionary now has 39+ entries (post-Session 23). Session 25 proposes computations that would test or generate additional entries:

| NCG Concept | Phonon Analog | Session 25 Goal | Tier |
|:------------|:-------------|:----------------|:-----|
| Graded spectral sum | Casimir force (bos - ferm) | Goal 1 | B (Parallel) |
| Finite-cutoff spectral action | Full lattice free energy (vs Debye) | Goal 2 | A (if f is physical) |
| Berry phase accumulation | Phonon band topology (Zak phase) | Goal 3 | B (Parallel) |
| Spectral flow (eta invariant) | Soft mode structural transition | Goal 4 | B (Parallel) |
| Gap-edge holonomy | Topological insulator Z_2 invariant | Goal 5 | B (Parallel) |
| Spectral dimension with TT | Walk dimension in phononic medium | Goal 6 | C (Suggestive) |
| Self-consistent mu from backreaction | Thermal occupation above band gap | Goal 7 | C (Suggestive) |
| a_6 alternating sign | Debye model breakdown at intermediate T | Goal 8 | C (Suggestive) |

If Goal 2 succeeds (V_full minimum at finite Lambda while V_spec monotone), the transfer function interpretation graduates from C-tier to A-tier. This would be the single most important validation of the phonon paradigm: the cutoff function f is not a regularizer but encodes real physics about the finite lattice.

### 4.2 The Claim A Test

Claim A -- "spacetime is what SU(3) looks like from inside" -- has a specific phononic test. If the spectral action at finite cutoff has a minimum while the asymptotic expansion does not, it means the finite eigenvalue sum contains physics that the continuum (asymptotic) approximation misses. In phonon physics, this is commonplace: the Debye model predicts monotone specific heat, but the full lattice dynamics shows peaks (Schottky anomalies) at specific temperatures corresponding to particular mode frequencies. The "inside view" is the full lattice dynamics; the "outside view" is the Debye approximation.

Goal 2 is the computational realization of this test. It is the most important single computation in Session 25 for the phonon paradigm.

### 4.3 The 36 -> 2 Degeneracy Collapse Revisited

The degeneracy collapse at tau ~ 0.2 (from 36 modes within a BCS-relevant window to 2) remains the most dramatic spectral feature identified in the project. In phonon physics, a sudden reduction in the number of modes within an energy window signals a Van Hove singularity in the density of states -- a point where the group velocity vanishes and the band structure changes character. The 36 -> 2 collapse is the internal-space Van Hove singularity.

Goals 3 and 5 both probe this transition. The Berry phase measures the eigenstate rotation (how fast the ground state character changes), while the gap-edge holonomy measures the topological protection (whether the rotation is quantized). Together, they characterize the Van Hove singularity completely.

---

## Section 5: Open Questions

### 5.1 What Is the Correct Grading for Goal 1?

The directive flags this as a mandatory gate. I agree. The chirality grading will give zero by BDI symmetry. The thermal grading (sector-specific spectral action weighted by representation dimension) is the physically correct quantity, but it requires knowing which sectors contribute with which sign. In the SM, the sign is determined by the 4D spin: bosonic KK modes (from internal scalar and vector harmonics) get +1, fermionic KK modes (from internal spinor harmonics) get -1. The grading is NOT from gamma_9 on SU(3) -- it is from the 4D spin-statistics connection applied to each KK tower. Landau should confirm this interpretation before the computation runs.

### 5.2 Does the Impedance Picture Require a Boundary?

The SU(3) internal space is compact and has no boundary. Where is the impedance mismatch? The answer: the boundary is the interface between the internal and external spaces in the KK decomposition. The dimensional reduction M^4 x K -> M^4 defines an effective boundary condition at the "edge" of K (the identification of opposite faces of the fundamental domain). The impedance mismatch is between the 4D propagating modes and the internal standing waves. This is the standard acoustic cavity picture: a finite cavity has resonant frequencies determined by its impedance match with the external environment.

### 5.3 What Happens at Lambda = lambda_min?

When the cutoff Lambda equals the spectral gap edge lambda_min, only one mode (the gap-edge doublet) contributes to the spectral action. V_full(tau; Lambda = lambda_min(tau)) is a single-mode quantity that depends ONLY on the gap-edge eigenvalue. Its tau-dependence is the tau-dependence of lambda_min itself -- which is non-monotone (it has structure from the avoided crossings that produce the B = 982.5 Berry curvature). This is a regime where the Debye approximation is maximally wrong (1 mode vs polynomial) and the finite-cutoff physics is maximally interesting.

### 5.4 Is There a Phononic Analog of the Spectral Flow Zero-Crossing?

In a phononic crystal under mechanical stress, a soft mode can be driven to zero frequency (instability). If the stress is increased further, the mode reappears with different polarization. This is phonon spectral flow -- the acoustic analog of the index theory computation. On SU(3), spectral flow would mean a mode softens to zero and reappears in a different representation sector. Block-diagonality (W2) forbids the mode from changing sectors during the softening. But it does NOT forbid the mode from reaching zero WITHIN a sector. Goal 4 checks exactly this.

---

## Closing Assessment

Session 25 asks the right questions in the right order. Goals 1-3 are computable from existing data in a single session. Each evades at least two walls. Each has a well-defined Constraint Condition and a well-defined success condition. The expected information value of running all three is positive even at the current 3% (Sagan) baseline.

From the phonon perspective, the progression of Sessions 18-24 has been the systematic elimination of the harmonic lattice approximation. Every harmonic quantity has been computed and found monotone. Session 25 proposes three classes of beyond-harmonic physics: (1) graded sums that exploit the differential response of acoustic and optical branches (Goal 1), (2) finite-cutoff sums that capture the Van Hove singularities missed by the Debye model (Goal 2), and (3) topological invariants that are invisible to smooth spectral functionals (Goals 3, 4, 5). These are not rescue fantasies. They are the standard toolkit of modern condensed matter physics applied to a well-characterized spectral lattice.

My probability assessment: I hold at **5-8%** for the physical program, with the note that the expected posterior GIVEN that Goals 1-3 are computed is higher than the current 3-5% regardless of outcome, because negative results close paths cleanly and positive results reopen the framework. The information value of computation remains positive.

The tight-binding band structure of the Kosmann Hamiltonian, the Zak phase of the gap-edge molecular orbital, and the finite-cutoff spectral action on existing eigenvalue data -- these three computations can be completed in under an hour of runtime. They probe the three orthogonal directions in which physics can live outside the harmonic box: differential grading, finite-scale structure, and topology. If all three are null, the box is complete and the framework becomes pure spectral geometry. If any one shows non-trivial structure, the walls have windows.

The lattice has been characterized. The harmonic modes are known. The question is whether the crystal is alive -- whether it supports collective phenomena beyond its individual vibrations. Eighteen sessions of harmonic analysis say no. One hour of beyond-harmonic computation will say whether the lattice agrees.

---

*Quantum-Acoustics-Theorist, 2026-02-21. The phonon paradigm does not promise escape from the walls. It promises the correct language for describing what lives inside them -- and whether anything can propagate through.*
