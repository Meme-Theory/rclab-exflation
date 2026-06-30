# A Tropical Geometric Approach to Exceptional Points

**Authors:** Ayan Banerjee, Rimika Jaiswal, Madhusudan Manjunath, and Awadhesh Narayan
**Year:** 2023
**Journal:** arXiv:2301.13485v3 [quant-ph] (August 2023)
**DOI/arXiv:** [arXiv:2301.13485](https://arxiv.org/abs/2301.13485)

---

## Abstract

This paper introduces a unified tropical geometric framework for characterizing exceptional points (EPs) in non-Hermitian systems. Exceptional points are degeneracies where both eigenvalues and eigenvectors coalesce, leading to distinctive fractional-power dependencies on perturbations. Using tropical geometry---specifically valuations, tropical roots, and Newton polygons---the authors develop methods to identify, classify, and tune EPs. Applications include gain-loss models, the non-Hermitian Su-Schrieffer-Heeger (SSH) model, and the Hatano-Nelson model. The framework also captures the non-Hermitian skin effect (NHSE) and demonstrates robustness to disorder.

---

## Historical Context

Non-Hermitian quantum mechanics has gained prominence in photonics, cold atoms, and electronic circuit applications. A defining feature is the exceptional point, where eigenvalues and eigenvectors coalesce simultaneously---a singularity absent in Hermitian systems. Near an N-th order EP, eigenvalues split as $\Delta\lambda \sim \nu^{1/N}$ under perturbation strength $\nu$. This fractional behavior complicates perturbation theory and necessitates new mathematical frameworks.

Tropical geometry, a branch of algebraic geometry that studies piecewise-linear limits via non-Archimedean valuations, provides a tool for characterizing such singularities. By mapping polynomial characteristic equations into piecewise-linear functions via tropical operations (min for addition, + for multiplication), one can read off the Puiseux exponents of roots directly from the "bend loci" of tropical curves. The Banerjee et al. paper adapts this algebraic machinery to non-Hermitian physics, connecting valuation theory to EP classification.

---

## Key Arguments and Derivations

### Tropical Semiring and Valuations

The foundational object is the **tropical semiring** $(R \cup \{\infty\}, \oplus, \odot)$ where:

$$x \oplus y = \min(x, y), \quad x \odot y = x + y$$

This replaces usual arithmetic while preserving ring axioms (except additive inverses). For a field $K$ (typically Puiseux series with complex coefficients $\mathbb{C}\{\{\nu\}\}$), a **valuation** is a function $\text{val}: K \to \mathbb{R} \cup \{\infty\}$ satisfying:

$$\text{val}(ab) = \text{val}(a) + \text{val}(b), \quad \text{val}(a+b) \geq \min\{\text{val}(a), \text{val}(b)\}$$

For Puiseux series, $\text{val}$ returns the exponent of the leading term.

### Tropicalization of Characteristic Polynomials

For a non-Hermitian Hamiltonian $H(\nu)$ with characteristic polynomial $p(\nu, \lambda) \in \mathbb{C}[\nu, \lambda]$, regarded as an element of $\mathbb{C}\{\{\nu\}\}[\lambda]$, the **tropicalization** is:

$$\text{trop}(p(\nu, \lambda))(\omega) = \min_i [\text{val}(a_i) + i \cdot \omega]$$

where $p = \sum_i a_i \lambda^i$ and $\omega \in \mathbb{R}$. A **tropical root** is a point $\omega_0$ where the minimum is attained by at least two distinct monomials---equivalently, where the piecewise-linear function $\text{trop}(p)$ is not differentiable (the "bend locus").

By the fundamental theorem of tropical geometry, tropical roots correspond to valuations of Puiseux roots of $p$.

### Definition 1: Order of an Exceptional Point

Let $p \in \mathbb{C}\{\{\nu\}\}[\lambda]$ with at least one non-zero root. If $p$ has a **non-trivial Puiseux series root** (least exponent nonzero), then the **order of the EP** is the maximum denominator of the fractions $m/n$ (in reduced form) appearing as least exponents among all non-trivial roots. Otherwise the point is degenerate.

Equivalently, if $H(\nu) = H_0 + \nu H_1$ has an EP at $\nu = 0$, and the perturbed eigenvalues behave as $\lambda(\nu) = \gamma_1 \nu^{1/N} + \gamma_2 \nu^{2/N} + \cdots$, then the EP is of **order N**.

### Proposition 2: Tropical Root Characterization of EPs

**Proposition 2**: Let $H(\nu)$ have characteristic polynomial $p(\nu, \lambda)$. Suppose $\text{trop}(p(\nu, \lambda))$ has a non-zero tropical root $\omega_0$. Then the order of the EP at $\nu = 0$ is the maximum absolute value of denominators $n$ of $m/n \in \mathbb{Q}$ (reduced form) taken over all non-zero tropical roots.

This reduces the problem of determining EP order to finding the bend locus of a piecewise-linear function---a purely combinatorial task.

### Example: Two-Site Gain-Loss Model

Consider the Hamiltonian (Eq. 3):

$$H_2 = \begin{pmatrix} \alpha + i\gamma & \kappa \\ \kappa & -\alpha - i\gamma \end{pmatrix}$$

with an EP at $\alpha = 0$ when $\gamma = \kappa$. The characteristic polynomial is:

$$p(\alpha, \lambda) = -2i\kappa\alpha - \alpha^2 + \lambda^2$$

Tropicalization gives:

$$\text{trop}(p(\alpha, \lambda))(\omega) = \min(1, 2\omega)$$

The tropical root (bend locus) occurs where $1 = 2\omega_0$, i.e., $\omega_0 = 1/2$. By the fundamental theorem, the eigenvalues behave as $\lambda \sim \alpha^{1/2}$ near the EP, confirming a **second-order EP (EP-2)**.

### Newton Polygons and Amoebas

For a polynomial $p(x,y) = \sum_{\eta,\zeta} a_{\eta\zeta} x^\eta y^\zeta$, the **Newton polygon** is the convex hull of exponent pairs $(\eta, \zeta)$ of nonzero terms. The **amoeba** is the image of the algebraic variety $V$ under the logarithmic map $\text{Log}(z_1, \ldots, z_n) = (\log|z_1|, \ldots, \log|z_n|)$.

**Proposition 3** (spine-Newton polygon duality): The directions of unbounded rays (tentacles) of the amoeba are precisely the outer normals to the edges of the Newton polygon.

This duality allows visual classification: as parameters vary and EPs transition, the Newton polygon abruptly changes structure, and correspondingly the amoeba develops or loses features (vacuoles, tentacle directions).

### Three-Site Gain-Loss Model (Figure 2)

The Hamiltonian is (Eq. 6):

$$H_3 = \begin{pmatrix} \alpha + i\gamma & \kappa & 0 \\ \kappa & 0 & \kappa \\ 0 & \kappa & \beta - i\gamma \end{pmatrix}$$

with parametrization $\beta = \alpha \tan\phi$. As $\phi$ varies from $-\pi/6$ to $-\pi/4$:
- At $\phi = -\pi/6$: Newton polygon yields EP-3 (third-order exceptional point)
- At $\phi = -\pi/4$: Newton polygon yields EP-2 (second-order)

The tropical roots change from $\omega_0 = 1/3$ to $\omega_0 = 1/2$. The amoeba structure undergoes a drastic transition, with vacuoles appearing and disappearing—a visual signature of the underlying EP transition.

### Non-Hermitian Su-Schrieffer-Heeger Model (NHSE)

The SSH model with non-reciprocal hopping reads (Eq. 7):

$$H_{SSH} = -\sum_i [t_1(c^\dagger_{i,A} c_{i,B} + h.c.) + t_2(c^\dagger_{i+1,A} c_{i,B} + h.c.)] + \sum_i \gamma(c^\dagger_{i,B} c_{i,A} - c^\dagger_{i,A} c_{i,B})$$

The intra-cell hopping $t_1 \to t_1 \pm \gamma$ is non-reciprocal. In the periodic system with weak boundary perturbation $\varepsilon = \sigma t_2$ ($\sigma \in [0,1]$), the characteristic polynomial is:

$$p(\varepsilon, \lambda) = [\text{const}](\gamma^2 - t_1^2)^{N/2} - t_2^{(N-2)/2} (t_1 + \gamma)^{N/2} \varepsilon + \text{(other terms in } \lambda^M)$$

Tropicalization yields:

$$\text{trop}(p(\varepsilon, \lambda))(\omega) = \min\{m, \ldots, (N-2)\omega, N\omega\}$$

**Crucially**, at the transition $t_1 = \gamma$ (where $\gamma = 0$ in the perturbation), the coefficients of all $\lambda^M$ terms vanish except $\lambda^0$ and $\lambda^N$, leaving only:

$$p(\varepsilon, \lambda) \propto \varepsilon^a + \lambda^N$$

with solution $\lambda \propto \varepsilon^{a/N}$, indicating an **N-th order EP**. The tropical root is $\omega_0 = 1/N$.

This EP is the signature of the **non-Hermitian skin effect (NHSE)**: all bulk eigenstates collapse into a single edge state with algebraic multiplicity scaling with system size, while geometric multiplicity remains one.

The Newton polygon at this transition becomes a single line with slope $1/N$, and the amoeba collapses correspondingly.

### Hatano-Nelson Model with Disorder

The Hatano-Nelson model on N sites (Eq. 11) is:

$$H_N = \sum_i [\delta a_i c^\dagger_i c_{i+1} + (\eta b_i c^\dagger_i c_{i-1} + h.c.)]$$

with possible upper-corner coupling (weak horizontal link). Under disorder parametrization $\delta = r\cos\theta\cos\phi$, $\eta = r\cos\theta\sin\phi$, the characteristic polynomial exhibits different EP orders along different directions in parameter space.

**Key result**: The tropicalization of the characteristic equation remains invariant even when disorder coefficients $a, b, c, m, n$ are introduced (Eq. 12). This implies that EP order and structure are **universal** in the presence of disorder—the tropical roots do not change.

This can be verified via holonomy: loops enclosing or touching EPs in parameter space induce cyclic permutations or petal patterns in eigenmode evolution. With disorder, the eigenvalues get rescaled but holonomy properties (number of sheets in the Riemann surface, permutation structures) remain unchanged.

---

## Key Results

1. **Tropical Characterization of EP Order**: The order of an exceptional point can be determined from the tropical roots (bend loci) of the characteristic polynomial's tropicalization (Proposition 2).

2. **Newton Polygon—Amoeba Duality**: The structure of Newton polygons (exponent sets) directly encodes the structure of amoebas (logarithmic images), allowing visual identification of EP transitions.

3. **NHSE Detection**: The non-Hermitian skin effect is characterized by the collapse of the Newton polygon to a single line with slope $1/N$, indicating an N-th order EP.

4. **Universal Disorder Robustness**: Tropicalization is invariant under certain disorder perturbations, implying that EP order and holonomy are universal (not shifted by disorder).

5. **Holonomy via Tropical Roots**: The cyclic permutation of eigenmodes when looping around an EP-N is a topological consequence of the Riemann surface structure encoded in the tropical polynomial (via Puiseux series expansions).

6. **Amoeba Topology Reflects Physics**: The transitions in amoeba structure (vacuoles, tentacle directions) correlate with physical phase transitions (normal to NHSE, EP-order changes).

---

## Impact and Legacy

This paper introduced tropical geometry as a practical tool in non-Hermitian physics, creating a new bridge between algebraic geometry and condensed matter / quantum optics. Subsequent applications include:
- Design of higher-order EPs in coupled resonator arrays and photonic devices
- Understanding of universal EP structures across disorder and parameter variations
- Classification of non-Hermitian topological phases via tropical polytopes
- Extension to random non-Hermitian matrices via tropical limit

The work is cited as a canonical framework for EP characterization and has enabled experimental groups to tune to specific EP orders in photonic and circuit platforms.

---

## Connection to Phonon-Exflation Framework

**POTENTIAL RELEVANCE**: The tropical geometry framework for characterizing degeneracies and phase transitions may apply to the **avoided-crossing structure in the BCS ground-state energy landscape** (how $E_{GS}(N)$ transitions between pairing configurations).

**Analogy:**
- Non-Hermitian EPs are universal degeneracies where metric information collapses ($\lambda = 0$, eigenvectors parallel).
- In BCS, avoided crossings occur when quasi-particle energies approach coalescence, driven by coupling strength and level spacing.
- Both involve fractional-power dependencies: near EP-N, $\Delta\lambda \sim \nu^{1/N}$; near avoided crossings in BCS, gap opening is exponentially small in coupling, effectively smooth.

**Gap:** The paper treats non-Hermitian (non-adjoint) operators; BCS preserves Hermiticity (reality of quasi-particle energies). However, if one views the BCS pairing problem in the generalized eigenvalue formalism (Bogoliubov-de Gennes equations), which are non-Hermitian in a generalized sense, the tropical classification of level-structure transitions might apply.

**Speculation**: If BCS pairings could be viewed tropically (via a change of coordinates or perturbative expansion), one might characterize the "order" of different avoided-crossing structures and predict transitions between different pairing patterns. The paper does not address BCS systems directly, only non-Hermitian quantum mechanics.

**Direct test:** Apply tropical geometry to the characteristic polynomial of the Bogoliubov-de Gennes Hamiltonian in the limit of weak coupling or specific density regimes, and check if Newton polygon transitions correlate with changes in the ground-state pairing structure.

