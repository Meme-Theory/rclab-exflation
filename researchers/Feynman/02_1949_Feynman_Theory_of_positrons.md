# Theory of Positrons

**Author:** Richard P. Feynman
**Year:** 1949
**Journal:** *Physical Review*, 76(6), 749--759

---

## Abstract

Feynman develops a propagator-based reformulation of relativistic quantum mechanics in which the problem of negative-energy solutions to the Dirac equation is resolved by reinterpreting them as positive-energy particles traveling backward in time. An electron propagator $K_+(2,1)$ is constructed that propagates positive-energy states forward in time and negative-energy states backward in time, unifying electron and positron physics into a single mathematical object. This "Stuckelberg-Feynman interpretation" eliminates the need for Dirac's filled negative-energy sea (the Dirac sea) and provides a spacetime picture of pair creation and annihilation as a single electron worldline that reverses its time direction. The paper establishes the conceptual and mathematical machinery for the subsequent development of Feynman's approach to quantum electrodynamics, including the Feynman propagator and the interpretation of closed loops as vacuum polarization.

---

## Historical Context

### The Negative Energy Problem

The Dirac equation (1928) provided a relativistically covariant wave equation for the electron:

$$(i\gamma^\mu \partial_\mu - m)\psi = 0$$

Its spectacular prediction of spin-1/2 and the electron's magnetic moment was tempered by a persistent difficulty: the equation admitted solutions with negative energy, $E = -\sqrt{|\mathbf{p}|^2 + m^2}$. A free electron in a positive-energy state could, in principle, radiate and cascade down to $E \to -\infty$, rendering matter unstable.

Dirac's resolution (1930) was the "hole theory": all negative-energy states are filled in the vacuum, and the Pauli exclusion principle prevents transitions. A hole in this filled sea behaves as a particle with positive energy and positive charge -- the positron, confirmed experimentally by Anderson in 1932. While successful, hole theory was conceptually baroque: it required an infinite sea of unobservable electrons, it was inherently many-body (even for a "single" electron), and it did not generalize to bosons (which have no exclusion principle).

### The Stuckelberg Precursor

Ernst Stuckelberg had proposed in 1941-42 that negative-energy solutions propagating backward in time could be reinterpreted as antiparticles propagating forward in time. His papers, published in French-language Swiss journals, were largely overlooked by the physics community. Feynman arrived at the same interpretation independently, developing it into a complete computational framework.

### The Immediate Context

By 1949, the renormalization program for QED was being developed simultaneously by Schwinger, Tomonaga, and Feynman. Schwinger and Tomonaga used operator methods and canonical quantization. Feynman needed a spacetime-based approach to pair creation and annihilation that would integrate with his path-integral and diagrammatic methods. The "Theory of Positrons" paper provides this foundation, serving as the bridge between the non-relativistic path integral paper (1948) and the QED calculation papers that followed.

---

## Key Arguments and Derivations

### 1. The Kernel for the Dirac Equation

Feynman defines a kernel $K(2,1)$ that propagates solutions of the Dirac equation from spacetime point 1 to point 2:

$$\psi(2) = \int K(2,1) \gamma^0 \psi(1) \, d^3\mathbf{x}_1$$

For the free Dirac equation, $K$ satisfies:

$$(i\gamma^\mu \partial_\mu^{(2)} - m) K(2,1) = i\delta^{(4)}(2-1)$$

The general solution to this equation is not unique -- it depends on boundary conditions. In the standard retarded prescription, $K_{\text{ret}}(2,1) = 0$ for $t_2 < t_1$, and all positive- and negative-energy components propagate forward in time.

### 2. The Feynman Prescription

Feynman's key innovation is to choose a different boundary condition. He defines $K_+(2,1)$ such that:

- **Positive-energy states propagate forward in time** ($t_2 > t_1$)
- **Negative-energy states propagate backward in time** ($t_2 < t_1$)

In terms of the free-particle solutions $u_n(\mathbf{x})$ with energies $E_n$:

$$K_+(2,1) = \sum_{E_n > 0} u_n(\mathbf{x}_2)\bar{u}_n(\mathbf{x}_1) \, e^{-iE_n(t_2 - t_1)}, \quad t_2 > t_1$$

$$K_+(2,1) = -\sum_{E_n < 0} u_n(\mathbf{x}_2)\bar{u}_n(\mathbf{x}_1) \, e^{-iE_n(t_2 - t_1)}, \quad t_2 < t_1$$

The minus sign for the backward propagation is essential for the interpretation: a negative-energy electron traveling backward in time has positive energy going forward, and the sign ensures the correct charge assignment.

In momentum space, this corresponds to:

$$K_+(2,1) = \int \frac{d^4p}{(2\pi)^4} \frac{i(\gamma^\mu p_\mu + m)}{p^2 - m^2 + i\epsilon} \, e^{-ip\cdot(x_2 - x_1)}$$

where the $+i\epsilon$ prescription in the denominator implements the time-ordering: poles at $p_0 = +E_p$ are displaced below the real axis (propagating forward), while poles at $p_0 = -E_p$ are displaced above (propagating backward). This is the Feynman propagator for the Dirac field.

### 3. Pair Creation and Annihilation as Worldline Reversal

The most striking conceptual result is the reinterpretation of pair processes. Consider an electron worldline in spacetime. At some point, it encounters a sufficiently strong electromagnetic field and reverses its time direction. To an observer at a fixed time:

- **Before the reversal point:** An electron is approaching.
- **At the reversal:** An electron-positron pair is "created" (the backward-going segment is the positron).
- **After the reversal:** An electron and a positron are moving apart.

Feynman writes: "The fundamental idea is that the 'negative energy states' represent the positron...A backward-moving electron when properly regarded is equivalent to a positron."

Mathematically, if $\psi_e(x)$ is an electron solution with momentum $p$ and spin $s$ propagating forward in time, then $\psi_e(-t)$ represents the same solution propagating backward. Under charge conjugation, this becomes a positron solution with momentum $-p$ and opposite spin, propagating forward -- which is exactly the CPT-conjugate state.

### 4. Interaction with an External Field

For an electron in an external electromagnetic potential $A_\mu$, the Dirac equation becomes:

$$(i\gamma^\mu \partial_\mu - e\gamma^\mu A_\mu - m)\psi = 0$$

Feynman treats the interaction perturbatively. The kernel in the presence of the field satisfies:

$$K_+(2,1) = K_+^{(0)}(2,1) - ie\int K_+^{(0)}(2,3)\gamma^\mu A_\mu(3) K_+(3,1) \, d^4x_3$$

This integral equation (a Lippmann-Schwinger equation in 4D spacetime) can be iterated:

$$K_+ = K_+^{(0)} + K_+^{(1)} + K_+^{(2)} + \cdots$$

where:

$$K_+^{(1)}(2,1) = -ie\int K_+^{(0)}(2,3)\gamma^\mu A_\mu(3) K_+^{(0)}(3,1) \, d^4x_3$$

$$K_+^{(2)}(2,1) = (-ie)^2\int\int K_+^{(0)}(2,4)\gamma^\nu A_\nu(4) K_+^{(0)}(4,3)\gamma^\mu A_\mu(3) K_+^{(0)}(3,1) \, d^4x_3 \, d^4x_4$$

Each term has a spacetime interpretation: the electron propagates freely ($K_+^{(0)}$), scatters off the potential at point 3 ($\gamma^\mu A_\mu$), propagates freely again, and so on. When the intermediate propagator $K_+^{(0)}(4,3)$ connects two points with $t_4 < t_3$, the electron is going backward in time between those interactions -- it is a virtual positron.

### 5. Closed Loops and Vacuum Polarization

A particularly important case arises when the electron worldline forms a closed loop: the particle is created from the vacuum, interacts with the external field, and annihilates back into the vacuum. The contribution of a single loop to the vacuum amplitude is:

$$\text{Loop} = -\text{Tr}\int (-ie)^n \prod_{j=1}^{n} \left[K_+^{(0)}(j+1, j)\gamma^{\mu_j} A_{\mu_j}(j)\right] \prod_{j=1}^{n} d^4x_j$$

The trace is over Dirac indices, and the overall minus sign comes from Fermi statistics (the loop represents a virtual fermion-antifermion pair). For $n = 2$, this gives the vacuum polarization:

$$\Pi^{\mu\nu}(q) = -ie^2 \int \frac{d^4k}{(2\pi)^4} \text{Tr}\left[\gamma^\mu \frac{i(\not{k} + m)}{k^2 - m^2 + i\epsilon} \gamma^\nu \frac{i(\not{k} - \not{q} + m)}{(k-q)^2 - m^2 + i\epsilon}\right]$$

This integral is divergent (quadratically in the naive power counting, logarithmically after imposing gauge invariance via Ward identity), foreshadowing the renormalization problem.

### 6. Scattering Cross Sections

For electron scattering from an external field, the transition amplitude from initial state $\phi_i$ to final state $\phi_f$ is:

$$M_{fi} = -ie\int \bar{\phi}_f(2)\gamma^\mu A_\mu(2) K_+^{(0)}(2,1) \gamma^0 \phi_i(1) \, d^4x_2 \, d^3\mathbf{x}_1$$

For first-order scattering (Mott scattering for a Coulomb field), this reduces to:

$$M_{fi} = -ie\bar{u}(p_f, s_f)\gamma^\mu u(p_i, s_i) \tilde{A}_\mu(p_f - p_i)$$

where $\tilde{A}_\mu$ is the Fourier transform of the external potential. The cross section follows from $|M_{fi}|^2$ via the standard relation $d\sigma/d\Omega = |M_{fi}|^2 / |v_{\text{inc}}|$.

---

## Physical Interpretation

### The Spacetime Picture

Feynman's interpretation is fundamentally a spacetime picture rather than a state-at-a-time picture. An electron is a worldline in four-dimensional spacetime that can go forward or backward in time. What we call "pair creation" is a kink in this worldline. What we call "pair annihilation" is two worldlines (forward and backward) meeting and turning around.

This eliminates the Dirac sea entirely. The vacuum is not a filled sea of negative-energy states but simply empty spacetime. Antiparticles are not holes in a sea but particles whose worldlines run backward. The asymmetry between particles and antiparticles is only apparent -- in the spacetime picture, they are the same entity viewed from different temporal perspectives.

### The $i\epsilon$ Prescription

The Feynman propagator's $i\epsilon$ prescription:

$$\frac{1}{p^2 - m^2 + i\epsilon}$$

has a deep physical meaning. It enforces causality in a relativistic-quantum-mechanical sense: positive frequencies (particles) propagate forward in time, negative frequencies (antiparticles) propagate backward. This is distinct from both the retarded propagator (everything forward) and the advanced propagator (everything backward), and is the unique choice compatible with the vacuum being the state of lowest energy.

### Single-Particle Theory

Feynman notes that his approach permits a "single-particle" description of pair processes. Rather than invoking a many-body theory with creation and annihilation operators, one can describe all processes in terms of a single electron worldline that reverses direction. This is not merely a visualization trick: it provides computational simplification and conceptual clarity, particularly for processes involving a small number of particles.

---

## Impact and Legacy

### Feynman Diagrams

The spacetime interpretation of this paper is the conceptual prerequisite for Feynman diagrams. Each diagram is a picture of particle worldlines in spacetime: straight lines for propagation, vertices for interaction, and lines running backward in time for antiparticles. Without the backward-in-time interpretation, diagrams involving virtual pairs would be incoherent.

### The Feynman Propagator in QFT

The propagator $K_+(2,1)$ becomes, in quantum field theory language, the time-ordered two-point function:

$$K_+(x_2, x_1) \sim \langle 0 | T[\psi(x_2)\bar{\psi}(x_1)] | 0 \rangle$$

This object is central to the LSZ reduction formula, the Dyson series, and all perturbative calculations in QFT. The $i\epsilon$ prescription is now standard in every QFT textbook.

### CPT Theorem

Feynman's identification of antiparticles with backward-time-propagating particles provides physical intuition for the CPT theorem: the combined operation of charge conjugation (C), parity (P), and time reversal (T) is equivalent to viewing the same worldline from the opposite temporal direction. The formal CPT theorem (Luders, Pauli, 1954-57) confirms this for all local Lorentz-invariant quantum field theories.

### Schwinger-Dyson Equations

The integral equation for $K_+$ in an external field generalizes to the Schwinger-Dyson equations of quantum field theory, which are the exact equations of motion for the full (dressed) propagators and vertices. These remain central to non-perturbative approaches to QFT.

---

## Connections to Modern Physics

1. **Hawking radiation:** The picture of pair creation at a black hole horizon -- where one partner falls in and the other escapes -- is most naturally understood in Feynman's spacetime framework. The virtual pair becomes real when the horizon separates the partners.

2. **Schwinger effect:** Pair creation in a strong electric field is computed using the Feynman propagator in the field, following exactly the formalism of this paper. The rate per unit volume is $\Gamma \sim (eE)^2 \exp(-\pi m^2/eE)$.

3. **Condensed matter analogs:** In graphene and topological semimetals, the low-energy excitations obey an effective Dirac equation. "Zitterbewegung" (trembling motion from interference of positive and negative energy states) and Klein tunneling are directly understood through Feynman's propagator formalism.

4. **Lattice QCD:** The fermion propagator on the lattice is the discretized version of Feynman's $K_+$, and the treatment of fermion loops (vacuum polarization) follows the closed-loop formalism developed here.

5. **Kaluza-Klein context:** In higher-dimensional theories where the Dirac equation is formulated on $M^4 \times K$, the Feynman propagator factorizes into a four-dimensional part and an internal part. The internal propagator encodes the spectrum of the Dirac operator on $K$, directly connecting particle physics (via the tower of KK modes) to the internal geometry.
