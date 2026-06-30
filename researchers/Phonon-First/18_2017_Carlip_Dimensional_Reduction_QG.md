# Spontaneous Dimensional Reduction in Quantum Gravity

**Author(s):** S. Carlip
**Year:** 2016
**Journal:** Essay written for the Gravity Research Foundation 2016 Awards for Essays on Gravitation
**arXiv:** 1605.05694
**Relevance:** HIGH

---

## Abstract

Hints from a number of different approaches to quantum gravity point to a phenomenon of "spontaneous dimensional reduction" to two spacetime dimensions near the Planck scale. I examine the physical meaning of the term "dimension" in this context, summarize the evidence for dimensional reduction, and discuss possible physical explanations.

---

## Key Arguments and Derivations

### 1. Dimension as an Observable

Carlip opens by noting that while spacetime dimension is unambiguous for smooth manifolds in GR or Kaluza-Klein theory, in quantum gravity dimension must be emergent, since smooth large-scale spacetime itself may be emergent. This requires "dimensional estimators" -- quantum observables with simple dependence on dimension that can be generalized to situations where dimension is unclear. Different estimators need not agree; dimension may depend on the question asked.

**Geometric estimators:**
- Volume of a geodesic ball: if $V \sim r^d$ at some scale, then $d$ measures dimension at that scale.
- Hausdorff dimension $d_H$: counts the number of balls needed to cover a region as a function of $r$.

**Diffusion/random-walk estimators:**
- The heat kernel on a smooth manifold determines effective dimension whenever a random walk can be defined. There are two such dimensions: the walk dimension $d_W$ (from mean distance vs. time) and the spectral dimension $d_S$ (from the return probability $K(x,x;s) \sim (4\pi s)^{-d_S/2}$).
- These assume Riemannian (positive definite) metrics; applying them to spacetimes requires analytic continuation which might distort physics. Lorentzian alternatives exist: the "causal spectral dimension" (exploiting two random walkers moving forward in time), the Myrheim-Meyer dimension (from volumes of causal diamonds), and geodesic behavior analysis (in Kasner-like spacetimes, typical geodesics probe fewer dimensions).

**Thermodynamic estimators:**
- Free energy scales as $F/VT \sim T^{d-1}$, defining a "thermodynamic dimension" $d_T$. Dimensional reduction in quantum gravity was first observed via this quantity (Atick and Witten, string theory).
- Other thermodynamic dimensions from the equation of state parameter and specific heat.

**Anomalous scaling dimensions:**
- In field-theoretic approaches (asymptotic safety), anomalous scaling dimensions of operators change under RG flow and determine spacetime dimension. Massless Green's functions $G(x,x')$ scale as $\sigma(x,x')^{-(d-2)/2}$ in $d$ dimensions, so quantum corrections make $d$ scale-dependent.

### 2. Evidence for Dimensional Reduction

Carlip surveys evidence from many independent approaches:

- **String theory**: Atick and Witten found the thermodynamic dimension drops to $d_T = 2$ at high temperatures, leading them to postulate "a lattice theory with a $(1+1)$-dimensional field theory on each lattice site."
- **Causal dynamical triangulations (CDT)**: Ambjorn, Jurkiewicz, and Loll found a phase that is four-dimensional at large scales but two-dimensional at small scales (spectral dimension). This was the result that catalyzed the field.
- **Asymptotic safety**: Percacci and Perini showed that at a UV fixed point, scaling dimensions of fields are necessarily those of a two-dimensional field theory. Confirmed for spectral and walk dimensions by Reuter and Saueressig.
- **Loop quantum gravity and spin foams**: Geometric and spectral dimension fall to two at small scales.
- **Minimum-length models**: Both geometric and spectral dimension reduce to two at short distances.
- **Noncommutative geometry**: For Snyder space, thermodynamic dimensions show short-distance reduction. For other noncommutative models, spectral dimension decreases (Laplacian-dependent).
- **Generalized uncertainty principle**: Thermodynamic dimension reduces to $d_T = 2.5$.
- **Wheeler-DeWitt equation**: Short-distance approximation dominated by spacetimes where typical geodesics probe only two dimensions.
- **Causal set theory**: With improved Laplacian, $d_S = 2$. Myrheim-Meyer dimension also falls to approximately two for small causal sets.
- **Horava-Lifshitz gravity and higher curvature models**: Generalized spectral dimension falls to $d_S = 2$.

### 3. Extracting the Physics: Two Proposed Mechanisms

Carlip identifies two candidate physical explanations:

**Scale invariance (asymptotic safety):** An ultraviolet fixed point of the RG flow is by definition scale-invariant, and this invariance guarantees effective two-dimensional behavior for any theory including general relativity. The underlying reason: only in two dimensions is Newton's constant $G_N$ dimensionless and thus scale-free. This does not explain why such a fixed point should exist, but if one defines the theory at high energy, a high degree of symmetry that breaks at lower energies is natural.

**Asymptotic silence:** Near a spacelike singularity, classical GR exhibits "asymptotic silence": light cones shrink to lines, nearby points become causally disconnected. This leads to BKL behavior where the metric is locally Kasner with chaotically varying axes of anisotropy. Each point has a "preferred" spatial direction and geodesics effectively see only $1+1$ dimensions. Quantum fluctuations near the Planck scale may lead to short-distance asymptotic silence everywhere. The small-scale metric develops two length scales, and the Einstein-Hilbert action becomes that of a two-dimensional CFT for the transverse metric. This could physically explain the asymptotic safety fixed point.

---

## Key Results

1. Dimensional reduction to $d_S \approx 2$ at the Planck scale appears universally across quantum gravity approaches: CDT, asymptotic safety, LQG, spin foams, causal sets, Horava-Lifshitz gravity, minimum-length models, noncommutative geometry, string theory thermodynamics, and the Wheeler-DeWitt equation.
2. Different dimensional estimators (spectral, Hausdorff, thermodynamic, walk, Myrheim-Meyer, geodesic) can disagree, meaning "dimension" is genuinely question-dependent.
3. Like spontaneous symmetry breaking, dimensional reduction needs no explicit external mechanism -- it is "spontaneous dimensional reduction."
4. Two proposed physical mechanisms are scale invariance at a UV fixed point (asymptotic safety) and asymptotic silence (BKL behavior with quantum fluctuations).
5. The asymptotic silence mechanism predicts a metric with two length scales and a near-2D CFT structure for the transverse metric, which could provide the physical basis for the asymptotic safety fixed point.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Heat kernel | $K(x, x'; s) \sim (4\pi s)^{-d/2} e^{-\sigma(x,x')/2s} (1 + \mathcal{O}(s))$ | Eq. (1) |
| Asymptotic silence metric | $ds^2 = \ell_\parallel^2 g_{\mu\nu} dx^\mu dx^\nu + \ell_\perp^2 h_{ij} dx^i dx^j$ | Eq. (2) |
| Spectral dimension (return probability) | $K(x, x; s) \sim (4\pi s)^{-d_S/2}$ | p. 1 |
| Thermodynamic dimension | $F/VT \sim T^{d-1}$, defining $d = d_T$ | p. 2 |
| Green's function scaling | $G(x, x') \sim \sigma(x, x')^{-(d-2)/2}$ (or $\ln \sigma$ in $d=2$) | p. 2 |
| Volume scaling | $V \sim r^d$ | p. 1 |

---

## Relevance to Phonon-Exflation

Carlip's survey establishes that dimensional reduction $d_S: 4 \to 2$ near the Planck scale is a universal feature across quantum gravity programs, independent of their specific microscopic construction. For the phonon-exflation framework, where spacetime emerges from a discrete M4 x SU(3) substrate, this universality is directly relevant: the framework's emergent spectral geometry (Dirac operator on SU(3) fiber) must exhibit the same dimensional flow if it makes contact with quantum gravity. The two proposed mechanisms -- scale invariance at a UV fixed point and asymptotic silence -- both suggest that the 4D continuum is an IR phenomenon emerging from a simpler UV structure, consistent with the bottom-up emergence paradigm of phonon-exflation.
