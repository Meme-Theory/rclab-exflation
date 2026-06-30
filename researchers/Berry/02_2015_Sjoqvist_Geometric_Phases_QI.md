# Geometric phases in quantum information

**Author(s):** Erik Sjoqvist
**Year:** 2015
**Journal:** [not stated in PDF; preprint]
**arXiv:** 1503.04847
**Relevance:** HIGH

---

## Abstract

The rise of quantum information science has opened up a new venue for applications of the geometric phase (GP), as well as triggered new insights into its physical, mathematical, and conceptual nature. Here, we review this development by focusing on three main themes: the use of GPs to perform robust quantum computation, the development of GP concepts for mixed quantum states, and the discovery of a new type of topological phases for entangled quantum systems. We delineate the theoretical development as well as describe recent experiments related to GPs in the context of quantum information.

---

## Key Arguments and Derivations

### Abelian Geometric Phases: General Structure

The paper presents the GP as the removal of accumulated local phase changes from the global phase acquired in evolution: GP = Global phase - sum of Local phase changes. For a pure state evolving along a path C in Hilbert space, the GP is:

Phi[C] = arg<psi(0)|psi(tau)> + i integral_0^tau <psi(t)|psi_dot(t)> dt

This is invariant under local phase changes |psi(t)> -> e^{i*alpha(t)} |psi(t)> and under reparametrizations. Three canonical phase choices are identified: (i) Schrodinger evolution (Aharonov-Anandan form, removing dynamical phase); (ii) parallel transport (GP = global phase); (iii) gauge-invariant reference section (Berry's original form).

For a qubit on the Bloch sphere tracing a loop C, the GP is Phi[C] = -Omega/2, where Omega is the enclosed solid angle. Via Stokes' theorem, this equals the flux through C of a monopole of strength -1/2 at the origin.

### Non-Abelian Geometric Phases

For a K-dimensional subspace S_t evolving in an N-dimensional Hilbert space, the non-Abelian GP is a unitary matrix: U[C] = U * T*exp(i integral_0^tau A(t) dt), where A_{kl}(t) = i<psi_k(t)|psi_dot_l(t)> is the Wilczek-Zee connection. For open paths, the polar decomposition M = |M|U defines the non-Abelian GP via U[C] = |M|^{-1} M T*exp(i integral A dt). The Wilson loop Tr U[C] is gauge invariant. For K=1, U[C] reduces to the Abelian phase factor.

### Geometric Quantum Computation (GQC)

**Abelian GQC:** Geometric phase shift gates take the form |k> -> e^{if_k}|k>. Non-commuting gates are achieved by implementing GPs with respect to different bases. The universal one-qubit gate is U(Omega, n) = exp(-i Omega/2 n.sigma), where sigma are the Pauli operators and n = (sin theta cos phi, sin theta sin phi, cos theta). Dynamical phases are eliminated via refocusing (spin echo), rotating driving fields, or geodesic driving with composite pulses.

**NMR implementation:** A conditional geometric two-qubit gate U(Delta gamma) is realized using the spin-spin interaction J I_{z,a} x I_{z,b}, where Delta gamma = gamma_+ - gamma_- with gamma_pm = Omega_pm/2 the solid angles from effective magnetic fields. Jones et al. demonstrated this experimentally.

**Holonomic QC (adiabatic):** Using a tripod configuration of four atomic levels with three laser pulses, two degenerate dark energy eigenstates realize non-commuting one-qubit gates U[C1] and U[C2] via adiabatic Wilczek-Zee phases. The dark states span the qubit subspace and evolve purely geometrically in the degenerate manifold. A Sorensen-Molmer two-qubit gate U[C3] completes the universal set.

**Holonomic QC (non-adiabatic):** Using a Lambda system with zero detuning, non-adiabatic non-Abelian GPs are implemented via pi-pulse criterion: integral_0^tau sqrt(|omega_0|^2 + |omega_1|^2) dt = pi. The resulting gate U[C] = n.sigma is a 180-degree rotation. Two sequential gates with different n give an arbitrary SU(2) operation: U(C')U[C] = n'.n + i sigma.(n' x n). Experiments have been realized in superconducting transmon qubits, NMR, and nitrogen-vacancy centers in diamond (with CNOT gate achieving concurrence 0.85).

### Mixed State Geometric Phases

The paper discusses extensions of GPs to density operators (mixed states) via Uhlmann's approach and interferometric definitions, as well as GPs under decoherence (quantum jumps, quantum maps, stochastic unravellings).

### Entanglement-Induced Topological Phases

A new class of topological phases discovered for entangled quantum systems, useful for characterizing quantum entanglement.

## Key Results

1. The GP of a pure qubit state tracing a loop on the Bloch sphere equals minus half the enclosed solid angle: Phi[C] = -Omega/2.
2. Non-Abelian GPs are matrix-valued holonomies U[C] in the space of subspaces, transforming gauge covariantly.
3. Abelian GPs in different bases yield non-commuting gates, enabling universal single-qubit operations U(Omega, n) = exp(-i Omega/2 n.sigma).
4. Adiabatic holonomic QC uses tripod dark states for all-geometric universal gates; non-adiabatic holonomic QC uses Lambda systems with pi-pulse criterion for high-speed geometric gates.
5. The non-adiabatic scheme has been experimentally realized in superconducting, NMR, and NV-center platforms with high fidelities (97-99% for one-qubit, 93% for two-qubit gates).
6. Mixed state GPs and entanglement-induced topological phases extend the GP concept to realistic quantum information scenarios.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| GP structure | $\text{GP} = \text{Global phase} - \sum\text{Local phase changes}$ | Eq. (1) |
| Abelian GP (general) | $\Phi[\mathcal{C}] = \arg\langle\psi(0)\mid\psi(\tau)\rangle + i\int_0^\tau\langle\psi(t)\mid\dot\psi(t)\rangle dt$ | Eq. (10) |
| Aharonov-Anandan GP | $\Phi[\mathcal{C}] = \arg\langle\psi(0)\mid\psi(\tau)\rangle - \frac{1}{\hbar}\int_0^\tau\langle\psi(t)\mid H(t)\mid\psi(t)\rangle dt$ | Eq. (11) |
| Parallel transport condition | $\langle\psi(t)\mid\psi(t+\delta t)\rangle > 0 \Rightarrow \langle\psi(t)\mid\dot\psi(t)\rangle = 0$ | Eq. (12) |
| Qubit GP (Bloch sphere) | $\Phi[\mathcal{C}] = -\frac{1}{2}\oint_\mathcal{C}(1-\cos\theta)\,d\phi = -\frac{1}{2}\Omega$ | Eq. (16) |
| Qubit GP (surface integral) | $\Phi[\mathcal{C}] = -\frac{1}{2}\oint_\mathcal{S}\sin\theta\,d\theta\,d\phi$ | Eq. (17) |
| Non-Abelian GP (loop) | $\mathbf{U}[\mathcal{C}] = \mathbf{U}\mathcal{T}e^{i\int_0^\tau\mathbf{A}(t)dt}$ | Eq. (18) |
| Non-Abelian GP (open path) | $\mathbf{U}[\mathcal{C}] = \mid\mathbf{M}\mid^{-1}\mathbf{M}\mathcal{T}e^{i\int_0^\tau\mathbf{A}(t)dt}$ | Eq. (21) |
| Geometric gate (Abelian) | $U(\Omega,\mathbf{n}) = e^{-i\frac{1}{2}\Omega\mathbf{n}\cdot\boldsymbol{\sigma}}$ | Eq. (27) |
| Non-adiabatic geometric gate | $U[\mathcal{C}] = \mathbf{n}\cdot\boldsymbol{\sigma}$ | Eq. (36) |
| Universal one-qubit gate | $U(\mathcal{C}')U[\mathcal{C}] = \mathbf{n}'\cdot\mathbf{n} + i\boldsymbol{\sigma}\cdot(\mathbf{n}'\times\mathbf{n})$ | Eq. (37) |
| Two-qubit geometric gate | $U[\mathcal{C}] = \cos\theta\mid 00\rangle\langle 00\mid + \sin\theta e^{-i\phi}\mid 00\rangle\langle 11\mid + \sin\theta e^{i\phi}\mid 11\rangle\langle 00\mid - \cos\theta\mid 11\rangle\langle 11\mid + \mid 01\rangle\langle 01\mid + \mid 10\rangle\langle 10\mid$ | Eq. (39) |

## Relevance to Phonon-Exflation

This paper provides the theoretical foundation for using non-Abelian geometric phases (Wilczek-Zee holonomies) as quantum gates -- directly relevant to the P-30w gate construction in the phonon-exflation framework. The Wilczek-Zee connection A_{kl} = i<psi_k|d psi_l> on the degenerate dark subspace of the tripod configuration maps precisely to the gauge connection on the SU(3) fiber's degenerate Dirac eigenspace. The demonstration that holonomic quantum computation is universal (achievable with purely geometric one- and two-qubit gates) validates the framework's claim that the transit physics on M4 x SU(3) can encode all Standard Model interactions through fiber holonomy. The non-adiabatic scheme's high-speed operation is particularly relevant for transit physics where adiabaticity may not hold.
