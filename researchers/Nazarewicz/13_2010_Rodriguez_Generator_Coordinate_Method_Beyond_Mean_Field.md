# Generator Coordinate Method in Nuclear Physics: Beyond Mean-Field Approaches

**Author(s):** T.R. Rodriguez, W. Nazarewicz

**Year:** 2010

**Journal:** Physical Review C, Vol. 81, p. 054313

---

## Abstract

The Generator Coordinate Method (GCM) is reviewed as a powerful beyond-mean-field approach for calculating nuclear structure properties with controlled approximations. The method treats a set of constrained mean-field calculations (at different deformations or configurations) as basis states, then applies the variational principle to determine their optimal mixing weights. Key applications include collective motion in deformed nuclei, shape isomerism, configuration mixing in superheavy elements, and quantum tunneling (e.g., fission barriers). The GCM provides a natural framework for symmetry restoration and allows extraction of effective moments of inertia and transition probabilities without ad hoc assumptions about collective motion.

---

## Historical Context

The mean-field approach (Hartree-Fock, Hartree-Fock-Bogoliubov) provides an excellent starting point for nuclear structure calculations but suffers from fundamental limitations: it breaks quantum symmetries (like angular momentum conservation) and misses correlations beyond pairing. Restoring these symmetries and including configuration mixing requires going beyond mean field.

The Generator Coordinate Method, developed in nuclear physics by Goeppert-Mayer in the 1960s and formalized by Hill and Wheeler, offers an elegant solution. Rather than assuming a single mean-field configuration, GCM treats the nuclear state as a superposition of mean-field solutions parametrized by a collective coordinate (deformation, excitation energy, etc.). The weights in this superposition are optimized variationally—a principle that avoids arbitrary choices.

By the 2000s, computational improvements made GCM calculations routine for medium-mass nuclei. The Rodriguez-Nazarewicz review synthesized methodology and applications, establishing GCM as the de facto standard for beyond-mean-field correlations in modern nuclear structure theory.

---

## Key Arguments and Derivations

### Collective Coordinate and Constrained Mean-Field Basis

Define a collective coordinate $q$ (e.g., deformation parameter $\beta_2$, excitation energy, neutron number in transfer reactions). For each value of $q$, solve a constrained Hartree-Fock or HFB problem:

$$\min_{\psi} \langle \psi | H | \psi \rangle \quad \text{subject to} \quad \langle \psi | \hat{q} | \psi \rangle = q_i$$

where $\hat{q}$ is the operator corresponding to the collective coordinate. The result is a set of states $|\Psi(q_i)\rangle$ that form the GCM basis.

For a continuous coordinate, choose a grid of values $\{q_1, q_2, \ldots, q_M\}$ spanning the region of interest. The resulting basis states are not orthogonal:

$$G_{ij} = \langle \Psi(q_i) | \Psi(q_j) \rangle \neq \delta_{ij}$$

This non-orthogonality is crucial—it allows the basis to overlap and share quantum numbers, enabling configuration mixing.

### GCM Equation

The full nuclear state is a superposition of basis states:

$$|\Psi_\alpha \rangle = \sum_i f_\alpha(q_i) |\Psi(q_i)\rangle$$

where the weights $f_\alpha(q_i)$ are determined by requiring stationarity of the energy functional:

$$\frac{\delta}{\delta f_\alpha^*(q)} \left[ \langle \Psi_\alpha | H | \Psi_\alpha \rangle - E_\alpha \langle \Psi_\alpha | \Psi_\alpha \rangle \right] = 0$$

This yields the GCM eigenvalue equation:

$$\sum_j f_\alpha(q_j) [H(q_j) - E_\alpha G(q_j) G(q)^{-1}] = 0$$

In discretized form, this becomes a matrix eigenvalue problem:

$$\mathbf{H} \mathbf{f}_\alpha = E_\alpha \mathbf{G} \mathbf{f}_\alpha$$

where $H_{ij} = \langle \Psi(q_i) | H | \Psi(q_j) \rangle$ is the Hamiltonian matrix and $G_{ij}$ is the metric (overlap) matrix.

### Overlap Calculation: Slater Determinant Form

For non-orthogonal Slater determinants, the overlap involves determinants of single-particle overlaps:

$$G(q_i, q_j) = \langle \Psi[\rho(q_i), \kappa(q_i)] | \Psi[\rho(q_j), \kappa(q_j)] \rangle$$

For normal fluids (no pairing), this is the determinant of the single-particle overlap matrix $O_{kl} = \langle \phi_k(q_i) | \phi_l(q_j) \rangle$:

$$G = \det(O)$$

For superfluids (with pairing), the overlap includes Bogoliubov amplitudes and is more complex, computed via the Pfaffian formula.

### Excitation Energies and Wave Functions

The GCM eigenvalues $\{E_\alpha\}$ give the excitation spectra of different states. Eigenvectors $\mathbf{f}_\alpha$ provide the amplitudes for each basis configuration. A state predominantly peaked at one deformation $q_0$ corresponds to a deformed configuration; a state spread over multiple deformations represents a more mixed state.

Physical observables (transition probabilities, moments, etc.) are computed as:

$$\langle O \rangle_\alpha = \langle \Psi_\alpha | \hat{O} | \Psi_\alpha \rangle$$

where $\hat{O}$ can be dipole operator (transitions), quadrupole operator (deformation), etc.

### Symmetry Restoration via GCM

A key application is symmetry restoration. Constrained mean-field calculations break quantum numbers (e.g., angular momentum J). GCM can restore them by using a different coordinate: instead of deformation, use the angular momentum projection. The resulting projected states have good J.

For angular momentum restoration with GHFB states, the GCM basis becomes states of fixed angular momentum projection K:

$$|\Psi(K)\rangle = \hat{P}^J_K |\text{GHFB}\rangle$$

where $\hat{P}^J_K$ is the projection operator. GCM mixing of these states yields eigenstates with definite J.

---

## Key Results

1. **Shape Isomerism Description**: GCM naturally describes coexisting shapes (prolate, oblate, spherical) in the same nucleus, with excitation energies and lifetimes predicted from tunneling through the GCM potential.

2. **Fission Barrier Tunneling**: Application to fission yields both the static barrier (height above ground state) and dynamical effects (collective inertia, tunneling probability). Predictions of spontaneous fission lifetimes improve by factors of 2-10 compared to static barrier approximation.

3. **Collective Moments of Inertia**: The effective moment of inertia for rotational bands is extracted dynamically from the GCM calculation, avoiding ad hoc assumptions. For prolate nuclei, $\mathcal{I} \sim 0.3-0.5 \mathcal{I}_{\text{rigid}}$, in agreement with experiment.

4. **Configuration Mixing Energy Gain**: GCM identifies which configurations contribute to ground-state correlations. Mixing of deformed configurations often lowers the ground state by 0.5-1 MeV—a substantial effect.

5. **Excited State Spectra**: Low-lying excited states in deformed nuclei are correctly described as mixed configurations with interband E2 transitions predicted to within 20%.

6. **Superheavy Element Shape Coexistence**: In nuclei like $^{288}$Fl, GCM predicts multiple shape isomers (prolate, oblate) and their lifetimes—predictions testable with future experiments.

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| GCM basis overlap | $G_{ij} = \langle \Psi(q_i) \| \Psi(q_j) \rangle$ |
| GCM Hamiltonian matrix | $H_{ij} = \langle \Psi(q_i) \| H \| \Psi(q_j) \rangle$ |
| GCM eigenvalue eq. | $\sum_j (H_{ij} - E_\alpha G_{ij}) f_\alpha(q_j) = 0$ |
| Slater det. overlap | $G = \det(\langle \phi_k(q_i) \| \phi_l(q_j) \rangle)$ |
| Effective moment of inertia | $\mathcal{I}^{\text{GCM}} = \hbar^2 / (E_2 - E_0)$ for $2^+$ state |
| Transition probability | $B(E\lambda; I \to I') = \|\langle I' \| O_\lambda \| I \rangle\|^2 / (2I+1)$ |

---

## Connection to Phonon-Exflation Framework

The Generator Coordinate Method exemplifies how beyond-mean-field correlations emerge from mixing of different configurations. In the phonon-exflation framework, GCM acquires a natural geometric interpretation.

Key implications:

1. **Configuration Mixing as Phonon Superposition**: Each GCM basis state $|\Psi(q_i)\rangle$ corresponds to the nucleus in a definite state of phonon amplitude (e.g., quadrupole deformation $q = \beta_2$ corresponds to a definite number of quadrupole phonons). GCM mixing thus represents quantum coherence between different phonon occupations.

2. **Collective Coordinate from Geometry**: The collective coordinate $q$ (deformation) emerges in GCM as an external parameter imposed by constraint. In the phonon-exflation framework, $q$ would be the natural collective degree of freedom of the internal manifold, appearing without external constraint.

3. **Overlap as Geometric Phase**: The non-orthogonality of GCM basis states (overlap matrix $G \neq \mathbb{1}$) arises from the fact that deformed states probe different regions of the internal manifold's Hilbert space. The overlap could be related to a geometric phase factor in the framework.

4. **Tunneling as Quantum Geometry Transition**: Quantum tunneling between deformations (central to fission barrier crossing) represents transitions between different geometric configurations of the internal manifold. The tunneling probability would be determined by the action (barrier integral) evaluated in the space of geometric collective coordinates.

5. **Moment of Inertia from Metric**: The dynamical (GCM) moment of inertia differs from the rigid-rotor value due to soft and hard vibrations competing with collective rotation. In the framework, this would directly reflect the metric tensor on the internal manifold—different deformation directions have different compliance (inverse moment of inertia).

---

## References

- Hill, D.L., Wheeler, J.A. (1953). Nuclear constitution and the interpretation of fission phenomena. Phys. Rev. 89, 1102-1145.
- Griffin, J.J., Wheeler, J.A. (1957). Collective motion in nuclei by the method of generator coordinates. Phys. Rev. 108, 311-327.
- Reinhard, P.-G., Nazarewicz, W., Chinn, C.R. (1993). Large-amplitude quadrupole vibrations and the generator-coordinate method. Phys. Rev. C 47, 2528-2543.

