# Quantum Geometric Tensor (Fubini-Study Metric) in Simple Quantum System: A pedagogical Introduction

**Author(s):** Ran Cheng
**Year:** 2010 (revised 2013)
**Journal:** arXiv preprint (quant-ph)
**arXiv:** 1012.1337
**Relevance:** HIGH

---

## Abstract

Geometric Quantum Mechanics is a novel and prospecting approach motivated by the belief that our world is ultimately geometrical. At the heart of that is a quantity called Quantum Geometric Tensor (or Fubini-Study metric), which is a complex tensor with the real part serving as the Riemannian metric that measures the 'quantum distance', and the imaginary part being the Berry curvature. Following a physical introduction of the basic formalism, we illustrate its physical significance in both the adiabatic and non-adiabatic systems.

---

## Key Arguments and Derivations

### Introduction: Gauge Structures in Quantum Mechanics

The paper motivates the QGT through the parallel between fundamental physics (gravity as spacetime symmetry, Yang-Mills as internal symmetry) and emergent gauge structures in quantum mechanics. When states differing only by a local phase factor are identified, the Hilbert space $\mathcal{H}$ reduces to the Projected Hilbert space $\mathcal{PH}$, and quantum states become "Rays." The QGT emerges as the natural metric on this projected space.

The key insight: taking the inner product between two quantum states requires two pieces of information -- the overlap (measured by the symmetric real part, the quantum metric) and the relative phase (measured by the antisymmetric imaginary part, the Berry curvature).

### Formalism

For a parameter-dependent Hamiltonian $H(\lambda)$ with eigenstates $|\phi_n(\lambda)\rangle$, the quantum distance upon infinitesimal parameter variation $d\lambda$ is:

$$ds^2 = \|\psi(\lambda + d\lambda) - \psi(\lambda)\|^2 = \langle\partial_\mu\psi|\partial_\nu\psi\rangle d\lambda^\mu d\lambda^\nu = (\gamma_{\mu\nu} + i\sigma_{\mu\nu})d\lambda^\mu d\lambda^\nu$$

The real part $\gamma_{\mu\nu}$ is symmetric and the imaginary part $\sigma_{\mu\nu}$ is antisymmetric. However, $\gamma_{\mu\nu}$ is NOT gauge invariant. The gauge-invariant metric is:

$$g_{\mu\nu}(\lambda) = \gamma_{\mu\nu}(\lambda) - \beta_\mu(\lambda)\beta_\nu(\lambda)$$

where $\beta_\mu = i\langle\psi|\partial_\mu\psi\rangle$ is the Berry connection. The full QGT is then defined as:

$$Q_{\mu\nu}(\lambda) = \langle\partial_\mu\psi|\partial_\nu\psi\rangle - \langle\partial_\mu\psi|\psi\rangle\langle\psi|\partial_\nu\psi\rangle$$

with $g_{\mu\nu} = \mathrm{Re}\,Q_{\mu\nu}$ (quantum metric) and $\sigma_{\mu\nu} = \mathrm{Im}\,Q_{\mu\nu}$ (related to Berry curvature).

The geodesic quantum distance between states is:

$$|\langle\psi(\lambda_F)|\psi(\lambda_I)\rangle| = 1 - \frac{1}{2}\int_{\lambda_I}^{\lambda_F} g_{\mu\nu}(\lambda)d\lambda^\mu d\lambda^\nu$$

### Case One: Adiabatic System

For a system confined to a single energy level (e.g., the ground state $|\phi_0(\lambda)\rangle$), the QGT is expressed via the Feynman-Hellman relations:

$$Q_{\mu\nu} = \sum_{n\neq 0}\frac{\langle\phi_0|\partial_\mu H|\phi_n\rangle\langle\phi_n|\partial_\nu H|\phi_0\rangle}{(E_0 - E_n)^2}$$

This form is explicitly gauge-invariant and computationally advantageous (avoids phase ambiguity in numerical eigenstates). The relation to Berry curvature is:

$$Q_{\mu\nu} = g_{\mu\nu} - \frac{i}{2}F_{\mu\nu}$$

For a spin-1/2 in a magnetic field $H = \mu\vec{\sigma}\cdot\vec{B}$, the metric is the round metric on $S^2$ and the Berry curvature corresponds to a magnetic monopole of charge 1/2.

For degenerate ground states, the QGT generalizes to a non-Abelian matrix form.

### Case Two: Non-Adiabatic System

For general time evolution, the quantum distance gives the Anandan-Aharonov theorem:

$$\frac{d\theta}{dt} = \frac{2|\Delta E|}{\hbar}$$

relating the "quantum velocity" (rate of state evolution) to the energy uncertainty $\Delta E$. The connection to the QGT is:

$$|\Delta E| = \hbar\sqrt{|g_{\mu\nu}\dot{\lambda}^\mu\dot{\lambda}^\nu|}$$

This provides a criterion for adiabaticity: the slower the parameter varies, the smaller the energy uncertainty, and the better the system stays on a single level.

---

## Key Results

1. The QGT $Q_{\mu\nu}$ is the Fubini-Study metric on quantum rays, with $\mathrm{Re}\,Q = g_{\mu\nu}$ (quantum metric) and $\mathrm{Im}\,Q = \sigma_{\mu\nu} = -F_{\mu\nu}/2$ (Berry curvature).
2. The quantum metric $g_{\mu\nu}$ measures geodesic distance in the projected Hilbert space $\mathcal{PH} = \mathcal{H}/U(1)$.
3. The gauge-invariant form $Q_{\mu\nu} = \langle\partial_\mu\psi|(1-|\psi\rangle\langle\psi|)|\partial_\nu\psi\rangle$ removes phase ambiguity.
4. The Feynman-Hellman representation $Q_{\mu\nu} = \sum_{n\neq 0}\langle\phi_0|\partial_\mu H|\phi_n\rangle\langle\phi_n|\partial_\nu H|\phi_0\rangle/(E_0-E_n)^2$ is numerically stable.
5. For spin-1/2 in a magnetic field: $g_{\mu\nu} = \mathrm{diag}(1, \sin^2\theta)$ (round $S^2$), $F_{\theta\phi} = \sin\theta/2$ (monopole).
6. The Anandan-Aharonov theorem $d\theta/dt = 2|\Delta E|/\hbar$ relates quantum velocity to energy uncertainty.
7. The QGT singularity at degeneracy points ($(E_0-E_n)^2$ denominator) signals quantum phase transitions.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Quantum distance | $ds^2 = \langle\partial_\mu\psi\|\partial_\nu\psi\rangle d\lambda^\mu d\lambda^\nu = (\gamma_{\mu\nu} + i\sigma_{\mu\nu})d\lambda^\mu d\lambda^\nu$ | Eq. (1) |
| Symmetry properties | $\gamma_{\mu\nu} = \gamma_{\nu\mu}$, $\sigma_{\mu\nu} = -\sigma_{\nu\mu}$ | Eq. (2) |
| Gauge-invariant metric | $g_{\mu\nu}(\lambda) = \gamma_{\mu\nu}(\lambda) - \beta_\mu(\lambda)\beta_\nu(\lambda)$ | Eq. (4) |
| QGT definition | $Q_{\mu\nu}(\lambda) = \langle\partial_\mu\psi\|\partial_\nu\psi\rangle - \langle\partial_\mu\psi\|\psi\rangle\langle\psi\|\partial_\nu\psi\rangle$ | Eq. (5) |
| Decomposition | $g_{\mu\nu} = \mathrm{Re}\,Q_{\mu\nu}$; $\sigma_{\mu\nu} = \mathrm{Im}\,Q_{\mu\nu}$ | Eq. (6) |
| Overlap formula | $\|\langle\psi(\lambda)\|\psi(\lambda+d\lambda)\rangle\| = 1 - \frac{1}{2}g_{\mu\nu}d\lambda^\mu d\lambda^\nu$ | Eq. (8) |
| Geodesic distance | $\|\langle\psi(\lambda_F)\|\psi(\lambda_I)\rangle\| = 1 - \frac{1}{2}\int g_{\mu\nu}d\lambda^\mu d\lambda^\nu$ | Eq. (9) |
| Feynman-Hellman QGT | $Q_{\mu\nu} = \sum_{n\neq 0}\frac{\langle\phi_0\|\partial_\mu H\|\phi_n\rangle\langle\phi_n\|\partial_\nu H\|\phi_0\rangle}{(E_0-E_n)^2}$ | Eq. (11) |
| Berry curvature relation | $F_{\mu\nu} = -2\,\mathrm{Im}\,Q_{\mu\nu}$ | Eq. (12) |
| QGT decomposition | $Q_{\mu\nu} = g_{\mu\nu} - \frac{i}{2}F_{\mu\nu}$ | Eq. (13) |
| Non-Abelian QGT | $[Q_{\mu\nu}]_{ij} = \sum_{n\neq 0,k(n)}\frac{\langle\phi_{0i}\|\partial_\mu H\|\phi_{nk}\rangle\langle\phi_{nk}\|\partial_\nu H\|\phi_{0j}\rangle}{(E_0-E_n)^2}$ | Eq. (14) |
| Anandan-Aharonov | $d\theta/dt = 2\|\Delta E\|/\hbar$ | Eq. (20) |
| Energy uncertainty | $\|\Delta E\| = \hbar\sqrt{\|g_{\mu\nu}\dot{\lambda}^\mu\dot{\lambda}^\nu\|}$ | Eq. (21) |

---

## Relevance to Phonon-Exflation

This pedagogical paper provides the foundational formalism for the quantum geometric tensor that is central to the phonon-exflation framework. The decomposition $Q_{\mu\nu} = g_{\mu\nu} - (i/2)F_{\mu\nu}$ into quantum metric (Re) and Berry curvature (Im) is precisely the structure computed in the framework's ERRATUM, which found $\mathrm{Im}(Q) = 0$ (vanishing Berry curvature) while $\mathrm{Re}(Q) = g = 982.5$ (large quantum metric). Cheng's Feynman-Hellman representation (Eq. 11) with the $(E_0 - E_n)^2$ denominator explains why the QGT diverges at degeneracy points -- directly relevant to the framework's BCS transition at $S_{\mathrm{inst}} = 0.069$ where levels approach degeneracy. The Anandan-Aharonov theorem ($d\theta/dt = 2|\Delta E|/\hbar$) provides the physical interpretation: the large quantum metric means the system's "quantum velocity" through parameter space is high, even though the Berry curvature (and hence topological protection) vanishes.
