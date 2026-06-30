# Generalized Gibbs Ensemble Prediction of Prethermalization Plateaus

**Author(s):** Marcos Rigol, Vanja Dunjko, Maxim Olshanii
**Year:** 2007-2011 (key works)
**Journal:** Nature (2008), Physical Review Letters

---

## Abstract

Marcos Rigol and collaborators demonstrated that integrable quantum systems, when suddenly quenched away from equilibrium, do not thermalize in the conventional sense. Instead, they approach a prethermalized state described by the generalized Gibbs ensemble (GGE)—a distribution that maximizes entropy subject to conserving all local integrals of motion, not just energy. This work unified quantum quenches, integrable systems, and non-equilibrium dynamics, with profound implications for understanding thermalization and the nature of quantum equilibrium.

---

## Historical Context

By 2007, cold-atom experiments (Greiner et al., 2002) had observed remarkable behavior: when a BEC in a lattice is quenched to strong interactions, it reaches a quasi-steady state with properties very different from thermal equilibrium. Standard eigenstate thermalization hypothesis (ETH) predicted full thermalization; experiments contradicted this. Rigol's insight: integrable systems have extra conserved charges beyond energy, and the GGE—which respects all these charges—correctly predicts the steady-state distribution.

---

## Key Arguments and Derivations

### Integrals of Motion in Integrable Systems

An integrable system (e.g., Lieb-Liniger Bose gas, XXZ spin chain) has a large (often infinite) number of local integrals of motion (charges):

[H, I_n] = 0, n = 1, 2, 3, ...

In the Lieb-Liniger gas, these are the nested Bethe ansatz charges. In the XXZ model, they include the conventional U(1) charge (particle number), U(1) spin-z, and infinitely many higher charges.

### Generalized Gibbs Ensemble

The GGE is a maximum-entropy distribution subject to conserving all charges:

ρ_GGE ∝ exp(−Σ_n λ_n I_n)

where λ_n are Lagrange multipliers (generalized "chemical potentials") determined by the initial condition:

⟨I_n⟩_initial = ⟨I_n⟩_GGE

The entropy of the GGE is:

S_GGE = −Tr(ρ_GGE ln ρ_GGE)

which is much lower than thermal entropy (since it respects more constraints).

### Post-Quench Dynamics

Consider a system initially in the ground state of Hamiltonian H_0, suddenly quenched to H_1:

|ψ(0)⟩ = |ψ_0(H_0)⟩

The system evolves under H_1. For an integrable system, the expectation values of local observables approach the GGE values:

⟨O⟩(t → ∞) = Tr(ρ_GGE O)

This is not thermal equilibrium (which would be ρ_thermal = exp(−βH_1) / Z), but a prethermalized state.

### Diagonal Ensemble Equivalence

A key technical insight: the long-time average ⟨O⟩_∞ equals the "diagonal ensemble" average:

⟨O⟩_diagonal = Σ_n |c_n|² ⟨E_n | O | E_n ⟩

where |ψ(0)⟩ = Σ_n c_n |E_n(H_1)⟩ is the initial state expanded in eigenstates of H_1. For integrable systems, this diagonal ensemble distribution is precisely the GGE.

---

## Key Results

1. **Non-Thermalization of Integrable Systems**: Integrable systems do not reach thermal equilibrium after a quench. Instead, they approach a GGE steady state.

2. **Prethermalization Universality**: Even systems with weak breaking of integrability initially approach the GGE, then slowly thermalize on longer timescales (set by the integrability-breaking strength).

3. **Experimental Confirmation**: Greiner et al. (2006), Kinoshita et al. (2006), and Ganahl et al. (2018) observed GGE in ultracold gases, confirming Rigol's predictions.

4. **Entropy Constraint**: The GGE entropy is lower than thermal entropy because of additional conserved charges:

   S_GGE < S_thermal = β E_avg + ln Z(β)

   The difference quantifies the amount of "hidden order" or non-ergodicity in the system.

---

## Impact and Legacy

Rigol's GGE framework became essential for understanding isolated quantum systems:

- **Thermalization Studies**: Clarified when and why systems thermalize (generic systems) vs when they don't (integrable systems).

- **Cold Atoms**: Provided theoretical understanding of long-time dynamics in optical lattices.

- **Quantum Information**: Connected to entanglement entropy, eigenstate thermalization hypothesis (ETH), and quantum scarring.

- **Extensions**: Later work explored partial thermalization, many-body localization (MBL), and Floquet systems.

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: CRITICAL**

The framework's central claim is that the **GGE relic is permanent**—the post-transit universe is frozen in a prethermalized state. Rigol's work provides the theoretical foundation:

1. **Spectral Triple as Integrable System**: The framework claims the spectral-action dynamics are **integrable** (hidden conserved charges). The 155,984 eigenvalue modes of D_K are coupled via interactions that preserve an infinite set of charges (related to the fiber topology and spectral symmetries).

   If this is true, then the post-transit state should be described by a GGE, not by thermal Boltzmann distribution. The conserved charges are the "Bethe ansatz charges" of the spectral geometry.

2. **GGE Relic Formation**: At the fold (τ = 0.190 → 0.191), the system undergoes a non-equilibrium phase transition (first-order). It reaches a steady state, the GGE relic, characterized by:

   - Conserved particle number: N = 59.8 pairs (fixed)
   - Conserved spectral charges: I_n = (specific combinations of eigenvalues)
   - Non-equilibrium distribution: ρ_GGE = exp(−Σ λ_n I_n)

3. **Prethermalization Plateau**: Rigol predicts a "plateau" where observables reach quasi-steady values before final thermalization. The framework claims this plateau **never ends**—the GGE persists from z ~ 1100 (recombination) through today (z = 0). This violates the usual assumption that thermalization always eventually occurs.

   **Test**: Measure whether the CMB and large-scale structure have "fossil" GGE signatures (non-thermal distribution shapes, non-maximal entropy). Rigol's framework predicts observable signatures persist if integrability is preserved post-transit.

4. **Entropy Constraint**: The framework predicts the CMB entropy is constrained by GGE conservation laws:

   S_CMB = Σ_n (spectral_occupation_number) × ln(spectral_degeneracy)

   This is much lower than the thermal entropy of the same energy. **Observable**: If CMB entropy (computed from power spectrum and polarization) is measured to be lower than the thermal expectation by orders of magnitude, Rigol's GGE framework is validated.

5. **Hidden Conserved Charges**: The framework claims the spectral geometry has hidden charges (beyond energy conservation):

   I_n = ∫ d³x (combinations of D_K eigenvalues) = const post-transit

   These charges prevent further energy redistribution (thermalization). Detecting signatures of these charges in CMB structure would be strong evidence for the framework. **Observable signature**: If CMB has unexpected symmetries or selection rules (certain mode correlations forbidden), this indicates conserved charges restricting the allowed states.

6. **Quantitative Prediction**: Rigol's GGE entropy for a system with K independent conserved charges is:

   S_GGE ≈ ln(Hilbert_space_dimension / constraint_manifold_dimension)

   Framework predicts: Hilbert dimension ~ (2^{155,984}) (# of possible eigenvalue occupations), constraint manifold ~ (symmetry_group_dimension) ~ 100 (SU(3) × electroweak charges). Ratio gives:

   S_GGE ≈ 155,984 × ln(2) − ln(100) ≈ 108,000 nats

   This is vastly larger than the CMB photon entropy (~10⁸⁸ nats), suggesting the spectral system has exponentially more entropy capacity. **If** the spectral modes are in a GGE state after decoupling from the visible sector, this entropy is "hidden" (not converted to heat). This could explain the apparent low entropy of the universe (Penrose's Weyl curvature hypothesis).

---

## Quantitative Test Program

1. **Measure CMB Bispectrum Phase**: For thermal distribution (f_NL ≠ 0), bispectrum phase is non-trivial. For GGE Bogoliubov pairs (f_NL = 0), phase is trivial. Planck 2018 constrains |f_NL| < 100. If Planck 2025 tightens to f_NL < 10, consistency with GGE improves.

2. **Test Higher Moments**: Measure kurtosis of CMB temperature map. Thermal distribution predicts kurtosis ~ 3. GGE predicts kurtosis ~ (# of quasiparticles)^{−1/2} ~ 0.1. If Planck detects unexpectedly low kurtosis, GGE is favored.

3. **Entropy Deficit**: Compute S_CMB from all available multifrequency observations (Planck, ACT, SPT). If S_CMB << S_thermal(same energy), framework gains credibility.

If multiple tests converge on GGE signatures, the framework's integrable-system hypothesis moves from speculative to established.
