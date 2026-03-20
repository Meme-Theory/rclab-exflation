# Quantal Phase Factors Accompanying Adiabatic Changes

**Author(s):** Michael V. Berry

**Year:** 1984

**Journal:** Proceedings of the Royal Society of London, Series A, Vol. 392, pp. 45-57

---

## Abstract

When a quantum system governed by a time-dependent Hamiltonian H(R(t)) is subjected to a cyclic adiabatic evolution—where a set of parameters R(t) traces a closed curve in parameter space—the system's state acquires not only the familiar dynamical phase but also an additional geometric phase factor. This geometric phase depends only on the area enclosed in parameter space and is independent of the rate of parameter change. The phase is Berry phase (also called geometric phase), given by:

$\gamma_n(C) = i \oint_C \langle n(R) | \nabla_R n(R) \rangle \cdot dR$

where n(R) is an eigenstate of H(R). The phenomenon has deep roots in molecular physics and classical optics, but Berry's 1984 work provided the general framework unifying these isolated observations.

---

## Historical Context

For nearly a century, the adiabatic theorem—formulated by Born and Fock in 1928—was thought to be complete: a quantum system slowly driven around a closed loop returns to its initial state with a dynamical phase $\phi_{\text{dyn}} = -(1/\hbar) \int_0^T E_n(t) dt$. The adiabatic theorem requires that the system remain in the same eigenstate throughout the evolution, avoiding level crossings.

However, observations in diverse fields hinted at additional structure:
- In 1956, Pancharatnam discovered in classical polarization optics that light propagating around a closed path on the Poincare sphere acquires an extra phase.
- In 1958, Longuet-Higgins observed in molecular spectroscopy that phase ambiguities arise near electronic degeneracies.
- These phenomena were considered unrelated oddities until Berry's unification.

Berry showed that adiabatic evolution in quantum mechanics is fundamentally geometric. The additional phase does not arise from the time-dependent dynamics but from the geometry of the eigenstate manifold in parameter space. This insight was revolutionary: it revealed that quantum systems encode information about their eigenstate geometry, accessible via adiabatic cycling.

---

## Key Arguments and Derivations

### The Adiabatic Approximation

The time-dependent Schrodinger equation is:

$i\hbar \frac{\partial |\psi(t)\rangle}{\partial t} = H(R(t)) |\psi(t)\rangle$

In the adiabatic approximation, we assume that H(R(t)) changes slowly enough that the state remains in the same instantaneous eigenstate:

$H(R) |n(R)\rangle = E_n(R) |n(R)\rangle$

The adiabatic eigenstate can be written as:

$|\psi_n(t)\rangle = e^{i\gamma_n(t)} e^{-i\phi_{\text{dyn}}(t)/\hbar} |n(R(t))\rangle$

where $\phi_{\text{dyn}}(t) = \int_0^t E_n(R(t')) dt'$ is the dynamical phase.

### Derivation of the Geometric Phase

Taking the time derivative of the adiabatic state and substituting into the Schrodinger equation:

$i\hbar \left[ \dot{\gamma}_n(t) + (-i\phi_{\text{dyn}}/\hbar) \right] |n\rangle + e^{i\gamma_n} e^{-i\phi_{\text{dyn}}/\hbar} \left[ i\hbar \frac{\partial |n\rangle}{\partial t} \right] = 0$

Expanding $\partial |n\rangle / \partial t = (\nabla_R n) \cdot \dot{R}$ and taking the inner product with $\langle n|$:

$\dot{\gamma}_n(t) = i \langle n(R(t)) | \nabla_R n(R(t)) \rangle \cdot \dot{R}(t)$

Integrating around a closed loop C:

$\gamma_n(C) = i \oint_C \langle n(R) | \nabla_R n(R) \rangle \cdot dR$

### Gauge Invariance and the Berry Connection

Define the **Berry connection**:

$\mathcal{A}_n(R) = i \langle n(R) | \nabla_R n(R) \rangle$

Then:

$\gamma_n(C) = \oint_C \mathcal{A}_n(R) \cdot dR$

By Stokes' theorem, this becomes an integral over the enclosed surface:

$\gamma_n(C) = \int_S (\nabla_R \times \mathcal{A}_n) \cdot dS = \int_S \mathcal{B}_n(R) \cdot dS$

where $\mathcal{B}_n(R) = \nabla_R \times \mathcal{A}_n(R)$ is the **Berry curvature**.

The Berry curvature can be written in terms of the complete set of eigenstates:

$\mathcal{B}_n = \nabla_R \times i \langle n | \nabla_R n \rangle = -\text{Im} \sum_{m \neq n} \frac{\langle n | \nabla_R H | m \rangle \times \langle m | \nabla_R H | n \rangle}{(E_n - E_m)^2}$

This shows that the curvature depends on matrix elements of the parameter derivatives of H.

### Physical Interpretation

For a two-level system with an avoided crossing in parameter space, the geometric phase encodes information about the topology of the parameter manifold. The phenomenon is inherently nonlocal in parameter space: the phase depends on the global geometry of the path, not local properties at any single point.

The Berry phase for a closed loop is gauge-invariant (modulo $2\pi$) and is thus a physically observable quantity. In general, the geometric phase takes continuous values; it is quantized to $\pi$ only in special topological cases (e.g., a loop encircling a diabolical point).

---

## Key Results

1. **Geometric phase formula**: For a cyclic adiabatic evolution, $\gamma_n = \int_S \mathcal{B}_n \cdot dS$ where the curvature depends only on the spectrum and eigenstates of H(R).

2. **Gauge structure**: The Berry connection and curvature define a U(1) gauge field on the eigenstate manifold. This is the first appearance of gauge structure emerging from quantum evolution geometry.

3. **Quantization condition**: For a path enclosing an avoided crossing (degeneracy), the phase shift is $\pi$ regardless of the strength of the crossing.

4. **Path independence**: The geometric phase depends only on the enclosed area in parameter space (for simply connected regions), not the specific trajectory.

5. **Generality**: The result applies to any quantum system with time-dependent parameters—atoms in external fields, molecular systems, condensed matter, and cosmological fields.

---

## Impact and Legacy

Berry's 1984 paper has accumulated over 13,500 citations, making it one of the most influential works in 20th-century quantum physics. The discovery revolutionized multiple fields:

- **Quantum mechanics**: Revealed that adiabatic evolution encodes geometric information; led to deeper understanding of phase in quantum theory.
- **Condensed matter physics**: The Berry curvature became central to understanding the quantum Hall effect, topological insulators, and the theory of polarization in crystals.
- **Molecular physics**: Explains the Renner-Teller effect and conical intersections in molecular potential energy surfaces.
- **Optics**: The Pancharatnam-Berry phase (geometric phase in polarization) became practical in designing geometric phase optical elements.
- **Cosmology**: Geometric phases appear in inflation and in the adiabatic evolution of fields.

Berry's work unified previously isolated phenomena and showed that geometric structure is woven into the fabric of quantum mechanics itself. The mathematical framework (connection and curvature on eigenstate manifolds) became the language for modern topological phases.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation framework, adiabatic evolution of the internal compactification modulus $s$ (parameter controlling Jensen deformation of SU(3)) creates a parameter-dependent spectrum: the eigenvalues $\lambda_n(s)$ of the Dirac operator $D_s$ depend explicitly on $s$.

As the universe expands and $s$ evolves, the phonon spectrum undergoes adiabatic changes. If the evolution is sufficiently slow (compatible with the expansion timescale), the phonons acquire geometric phases as they traverse the eigenstate manifold in modulus space. These phases could contribute to:

1. **Spectral phase structure** — The Berry phase modifies the effective action of phonons and could affect the spectral action calculation $S_{\text{spec}} = \text{Tr} f(D^2/\Lambda^2)$.

2. **Level crossings and avoided crossings** — In the Dirac spectrum of the deformed SU(3), avoided crossings appear at critical values of $s$ (e.g., sector crossings). The geometric phase at these avoided crossings encodes topological information about the spectrum.

3. **Adiabatic transport** — Phonons slowly moving through Hilbert space (via $s$ evolution) acquire geometric phases that are gauge-invariant. This connects to the "spinor transport" problem in the Baptista framework.

4. **Topological protection** — Berry phases can provide topological obstruction to level crossings, stabilizing the ground state against perturbations to the compactification geometry.

The Berry phase is most relevant to the noncommutative geometry picture: the connection and curvature on the eigenstate manifold in modulus space mirror the gauge structure on the internal space SU(3).
