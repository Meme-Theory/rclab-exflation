# Global Propagator for the Massless Dirac Operator and Spectral Asymptotics

**Author(s):** Capoferri, Vassiliev
**Year:** 2022
**Journal:** Integral Equations and Operator Theory, arXiv:2004.06351

---

## Abstract

We construct propagators for the massless Dirac operator $\mathcal{D}$ on closed Riemannian 3-manifolds using oscillatory integrals that are global in space and time, with distinguished complex-valued phase functions. We derive closed formulas for principal symbols and provide algorithmic methods for computing homogeneous components. Small-time expansions of principal and subprincipal symbols are expressed in terms of geometric invariants, enabling computation of third local Weyl coefficients in eigenvalue counting function asymptotics.

---

## Historical Context

The Dirac operator on curved manifolds is central to quantum geometry and spectral theory. Its propagator—the fundamental solution to the Dirac equation—encodes all information about eigenvalue asymptotics and spectral determinants. Classical approaches to propagator construction (via heat kernels, resolvent regularization) are powerful but often obscure the fine geometric structure.

Vassiliev's pseudodifferential operator theory provides an alternative pathway: representing the propagator as a global oscillatory integral with a phase function adapted to the geometry. This avoids explicit heat kernel calculations and directly accesses the principal and subprincipal symbol structure.

Capoferri and Vassiliev's 2022 work applies this framework to the massless Dirac operator on closed 3-manifolds. The key advance is extracting geometric information through symbol computation rather than heat trace asymptotics, yielding cleaner formulas and algorithmic calculability.

For the phonon-exflation framework, this is relevant because the SU(3) fiber geometry can be treated as a "manifold" with a Dirac operator; Capoferri-Vassiliev techniques offer a systematic way to compute its spectral properties without relying on symmetric space eigenvalue databases.

---

## Key Arguments and Derivations

### Oscillatory Integral Formulation

For a closed Riemannian 3-manifold $(M, g)$, the propagator of the massless Dirac operator satisfies:

$$\left( \partial_t + i\mathcal{D} \right) U(t, x, y) = 0, \quad U(0, x, y) = \delta(x - y) \otimes \mathbb{1}_{\text{spin}}$$

Capoferri-Vassiliev represent this propagator as:

$$U(t, x, y) = (2\pi)^{-n} \int e^{i\theta(x, y, \xi, t)} a(x, y, \xi, t) d\xi$$

where:
- $\theta(x, y, \xi, t)$ is a phase function encoding both spatial and temporal evolution
- $a(x, y, \xi, t)$ is a spinor-valued amplitude
- The integral is over cotangent fiber variables $\xi \in T^*_x M$

### Symbol Decomposition

The amplitude $a$ admits an asymptotic expansion:

$$a(x, y, \xi, t) \sim a_0(x, y, \xi, t) + a_1(x, y, \xi, t) + \cdots$$

where $a_j$ has homogeneity $-j$ in $(|\xi|, t)$.

**Principal symbol $a_0$**: Determined by the leading-order Dirac equation. For the massless operator on a 3-manifold with spinor rank 4, the principal symbol satisfies:

$$a_0(x, x, \xi, 0) = \text{diag}(+1, +1, -1, -1) + O(|\xi|^{-1})$$

encoding the spectral projector onto positive and negative frequency modes.

**Subprincipal symbol $a_1$**: Contains corrections from the spin connection and scalar curvature. It involves:

$$\text{Ric}(x, \xi) = R_{ij}(x) \xi^i \xi^j, \quad \nabla_\xi \cdot \xi = \text{div}_g(\xi)$$

---

### Closed Formulas for Homogeneous Components

The Capoferri-Vassiliev method yields explicit, algorithmic formulas. For instance:

**$a_0$ at the base point** ($x = y$, leading order):

$$a_0^{(0)}(x, x, \xi, t) = \frac{1}{|\xi|} \begin{pmatrix} |\xi| \mathbb{1}_{2\times 2} & \sigma^i \xi_i \\ \sigma^i \xi_i & -|\xi| \mathbb{1}_{2\times 2} \end{pmatrix} + \text{lower order}$$

where $\sigma^i$ are Pauli matrices and $\xi_i = g_{ij} \xi^j$.

**$a_1$ (subprincipal correction)**:

$$a_1^{(0)}(x, x, \xi, t) \sim -\frac{1}{6} R(x) \gamma^5 + O(\xi^{-2})$$

where $R(x)$ is scalar curvature and $\gamma^5 = i\gamma_0\gamma_1\gamma_2\gamma_3$ is the chirality operator.

---

### Small-Time Expansion and Weyl Coefficients

For small times $t \to 0^+$, the propagator admits:

$$U(t, x, x) = (4\pi t)^{-3/2} \sum_{k=0}^{\infty} w_k(x) t^k$$

where $w_k$ are local geometric invariants (Weyl coefficients).

For the Dirac operator on a 3-manifold:

- **$w_0$**: Constant (volume dimension).
- **$w_1$**: Proportional to scalar curvature $R(x)$.
- **$w_2$**: Involves Ricci and Weyl tensor components. **Third local Weyl coefficient** computed by Capoferri-Vassiliev.

The eigenvalue counting function $N(\lambda)$ (number of eigenvalues $\leq \lambda$) asymptotically follows:

$$N(\lambda) = \frac{\text{Vol}(M)}{(2\pi)^3} \lambda^3 + c_1 \lambda + c_2 + o(1)$$

where $c_1, c_2$ are geometric integrals involving $w_1, w_2$.

---

### Algorithm for Computing $a_j$

The method proceeds iteratively:

1. **Input**: Metric $g_{ij}$ on $M$, spin connection $\omega$.
2. **Solve transport equations** for $a_0, a_1, \ldots$ at increasing homogeneity order.
3. **Extract symbols** using pseudodifferential calculus (no explicit heat kernels needed).
4. **Output**: Closed formulas for $a_j$, directly usable in spectral asymptotics computations.

This avoids the traditional "guess + verify" approach to heat kernel coefficients, offering a systematic, generalizable framework.

---

## Key Results

1. **Global Propagator Construction**: Massless Dirac operator on closed 3-manifolds admits a fully explicit oscillatory integral representation with global phase function.

2. **Closed Formulas for Symbols**: Principal and subprincipal symbols expressed in closed form, algorithmic in geometric invariants.

3. **Third Weyl Coefficient Computed**: The $w_2$ term, appearing in the spectral asymptotics, is explicitly determined. This is a new result (prior work often stopped at $w_1$).

4. **Calculability Confirmed**: The method is systematic and scalable to higher homogeneity orders without conceptual obstruction.

5. **Geometric Information Recovery**: Eigenvalue asymptotics now directly encode Ricci tensor, Weyl tensor, and scalar curvature, enabling inverse spectral problems (determining geometry from spectra).

---

## Impact and Legacy

Capoferri-Vassiliev's work elevated pseudodifferential methods as a primary tool for spectral geometry on curved manifolds. By avoiding heat kernels altogether, they showed that oscillatory integral techniques offer superior computational control and geometric transparency.

The explicit formulae for higher Weyl coefficients have applications in:
- **Spectral dimension counting** (dimensionality of manifold from spectral behavior)
- **Inverse spectral geometry** (reconstructing metric from eigenvalue data)
- **Dirac operator renormalization** in field theory

For finite-density applications (as in the phonon-exflation framework's BdG spectral triple), analogous techniques can be adapted to compute corrections to the thermal Dirac operator structure, enabling precise tracking of how the pairing field modifies spectral properties.

---

## Framework Relevance

**Direct Connection**: The framework employs a deformed SU(3) Dirac operator coupled to BCS pairing (van Suijlekom finite-density setup). The spectral density and its asymptotics determine the vacuum energy and back-reaction. Capoferri-Vassiliev techniques offer a pathway to compute higher Weyl coefficients for the SU(3) fiber Dirac operator without relying on symmetric space eigenvalue tables.

Specifically:
- The $w_2$ coefficient (now accessible via Capoferri-Vassiliev) enters the spectral action at order $a_4$, directly affecting the "effective potential" $V(\tau)$.
- For deformed or partially broken SU(3), the algorithm remains valid, only requiring the metric $g_{ij}$ and spin connection as input.

**Computational Advantage**: The oscillatory integral method sidesteps the "constant-ratio trap" (observed in Sessions 22c-24a where low-mode vs. high-mode heat kernel coefficients differ by orders of magnitude). By computing $w_k$ globally, one avoids mode-by-mode approximations and captures the full spectrum structure.

**Status**: METHODOLOGICAL. Capoferri-Vassiliev provides a scalable, systematic framework for computing spectral properties of curved Dirac operators—a foundational tool for the framework's spectral action calculations.
