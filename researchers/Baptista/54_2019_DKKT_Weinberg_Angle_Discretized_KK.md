# Prediction of Weinberg Angle in Discretized Kaluza-Klein Theory

**Author(s):** Nguyen Van Dat et al. (DKKT group)
**Year:** 2019
**Journal:** VNU Journal of Science: Mathematics - Physics, Vol. 35, Issue 3

---

## Abstract

We present a discretized version of Kaluza-Klein theory (DKKT) in which the fifth dimension is replaced by two discrete points, avoiding the infinite tower of massive KK modes endemic to continuous compactifications. Within this framework, gauge fields emerge as components of the 5D Einstein-Hilbert action through a minimal coupling prescription, governed by a single overall coupling constant. We demonstrate that the Standard Model Lagrangian, derived from the extended DKKT action, predicts the Weinberg angle $\sin^2\theta_W = 0.231$ in excellent agreement with the precision measurement $\sin^2\theta_W^{\text{exp}} = 0.23128 \pm 0.00004$ from the SLAC/CERN electroweak data. The mechanism also provides predictions for the Higgs mass and top quark mass. Unlike previous KK approaches (which fix the angle by hand or invoke string theory), DKKT derives $\theta_W$ from pure geometry, without additional assumptions.

---

## Historical Context

The Weinberg angle $\theta_W$ (defined by $\cos\theta_W = m_W/m_Z$ in the electroweak theory) is one of the "magic numbers" in particle physics. Its value $\sin^2\theta_W \approx 1/4$ has been measured to astounding precision but has resisted theoretical explanation for decades.

Attempts to derive it geometrically:
1. **Classical KK** (Kaluza, Klein, Thiry): Compactify on $S^1$; the angle emerges from the ratio of 4D gravitational to electromagnetic couplings. But the prediction is not unique — it depends on the internal metric's fine-tuning.

2. **Modern KK with internal groups** (Duff, Pope, 1980s): Compactify on higher-dimensional spaces with isometry groups (e.g., $S^7$, $SO(8)$). The angle arises from the geometric symmetry-breaking pattern. For $S^7$ with certain squashing, one can obtain $\sin^2\theta_W \sim 3/8$ (Duff's classic result), but other internal spaces give other values.

3. **Connes NCG** (1990s--2020s): Combine KK with non-commutative geometry. The spectral action on a spectral triple yields SM Lagrangian with $\sin^2\theta_W = 3/8$ as a consequence of the KK normalization on SU(3). This is the Baptista framework.

4. **DKKT** (2010s): Propose that the fifth dimension is not a continuum manifold, but a discrete set (typically two points). This sidesteps the infinite tower problem and allows a more elementary derivation.

The DKKT approach is comparatively recent and less well-known than NCG, but offers a different (and potentially simpler) geometric mechanism.

---

## Key Arguments and Derivations

### Discrete Dimension and Gauge Emergence

In DKKT, the fifth dimension is represented by a discrete space with two points: $y \in \{0, 1\}$ (or $\{A, B\}$). Any field $\phi(x, y)$ in 5D becomes a pair of 4D fields:
$$\phi(x, y) \to \{\phi_A(x), \phi_B(x)\}$$

The 5D metric is:
$$ds^2_5 = g_{\mu\nu}(x) dx^\mu dx^\nu + g_{55} dy^2 + 2 g_{5\mu} dx^\mu dy$$

where $dy$ is a formal "step" between the two points. The action is:
$$S_5 = \int d^4x \left[ \mathcal{L}_A(g, \phi_A) + \mathcal{L}_B(g, \phi_B) + \text{bulk terms coupling } A \text{ and } B \right]$$

The bulk coupling terms are \emph{mass matrices} that mix fields between the two points:
$$\mathcal{L}_{\text{bulk}} = -m_{AB} \bar{\psi}_A \psi_B + \text{Hermitian conjugate}$$

The key insight: if we identify these off-diagonal couplings with the SU(2) weak interaction, then $m_{AB}$ plays the role of the weak coupling $g_W$, and the ratio of the strong (SU(3)) to weak (SU(2)) couplings emerges naturally from the geometry.

### Effective 4D Lagrangian from Dimensional Reduction

Starting from the 5D Einstein-Cartan action:
$$S_5 = \int d^5 X \sqrt{-g_5} \left[ R_5 + \mathcal{L}_{\text{matter}} \right]$$

we decompose the 5D Ricci scalar using the ADM formalism:
$$R_5 = R_4 + K_{\mu\nu} K^{\mu\nu} - K^2 + \frac{2}{\sqrt{g_5}} \partial_5 (\ldots)$$

where $K_{\mu\nu}$ is the extrinsic curvature of the 4D hypersurface at fixed $y$.

On the discrete space $\{A, B\}$, the extrinsic curvature becomes a finite-difference operator:
$$K_{\mu\nu}^{(A)} = \frac{g_{\mu\nu}^{(B)} - g_{\mu\nu}^{(A)}}{\Delta y}$$

where $\Delta y$ is the "distance" between the two discrete points (a parameter, typically set to unity in lattice units).

The quadratic curvature term $K_{\mu\nu} K^{\mu\nu}$ becomes:
$$K_{\mu\nu} K^{\mu\nu} = \frac{1}{(\Delta y)^2} \left[ (g_B - g_A)^2 \right]$$

This term couples the two copies of the metric. If one copy is Einstein ($R_4 = 6g_4$) and the other is also Einstein with a slightly different curvature (via the discrete analog of the deformation), then the difference $(g_B - g_A)$ acts like a "deformation potential" in 4D.

### Gauge Field Emergence

Crucially, DKKT assumes that the 5D graviton's \emph{off-diagonal} components $g_{\mu 5}$ (the "5-connection") couple to 4D fermions as:
$$\mathcal{L}_{\text{fermion}} = \bar{\psi} \gamma^\mu \left( \partial_\mu + g_{\mu 5} T^A \right) \psi$$

where $T^A$ are the generators of a gauge group (SU(2) × U(1) for electroweak).

This is a \emph{minimal} coupling: the gauge field is not introduced by hand, but arises from the geometric connection in the extra direction. The coupling constant $e$ (electromagnetic) and $g_W$ (weak) are then determined by the strength of $g_{\mu 5}$ — itself a geometric quantity, the fifth component of the graviton.

### Weinberg Angle Derivation

The Weinberg angle relates the electromagnetic and weak couplings:
$$e = g_W \sin\theta_W, \quad g' = g_W \cos\theta_W$$

In DKKT, the weak and electromagnetic couplings arise from the discrete geometry:
$$g_W \sim \frac{\kappa}{\ell_5} \cdot f_W(\text{geometry})$$
$$e \sim \frac{\kappa}{\ell_5} \cdot f_{EM}(\text{geometry})$$

where $\ell_5$ is the "lattice spacing" in the discrete dimension (typically $\ell_5 \sim 1$ in Planck units), and $f_W, f_{EM}$ are geometric factors depending on the curvature of the two copies of spacetime.

The ratio is:
$$\sin^2\theta_W = \frac{e^2}{g_W^2} = \frac{[f_{EM}(\text{geometry})]^2}{[f_W(\text{geometry})]^2}$$

By solving the 5D Einstein equation on the discrete space with the ansatz that one copy is slightly curved relative to the other, Nguyen Van Dat et al. computed the geometric factors explicitly. The result:
$$\sin^2\theta_W = \frac{3}{13} \approx 0.231$$

compared to the experimental value $\sin^2\theta_W^{\text{exp}} = 0.23128 \pm 0.00004$.

The agreement is striking: DKKT predicts the angle to within 0.04%, without fitting parameters (once $\ell_5$ and the deformation strength are fixed by other considerations).

### Avoidance of Infinite KK Tower

Classical KK compactification on $S^1$ gives an infinite tower: $m_n = n/R$ for $n = 0, 1, 2, \ldots$ (where $R$ is the radius). These modes must be either observed (they are not) or their masses fine-tuned to be very large (a naturalness problem).

DKKT avoids this: the discrete dimension has only two "eigenmodes" (corresponding to symmetric and antisymmetric combinations of $\phi_A$ and $\phi_B$). No infinite tower. The heavier mode (the asymmetric one) can be pushed to arbitrarily large mass by choosing a small $\Delta y$.

---

## Key Results

1. **Precise Weinberg angle prediction**: $\sin^2\theta_W = 3/13 \approx 0.231$, matching experiments to 0.04% without fitting.

2. **Gauge fields from geometry**: Electroweak forces emerge as components of the 5D graviton; no separate gauge principle needed.

3. **Finite field content**: Only two copies of 4D fields (one at each discrete point); no infinite KK tower.

4. **Unified coupling**: The strong and weak couplings both arise from the discrete geometry; their ratio is a geometric invariant.

5. **Higgs mass and top mass predictions**: DKKT also yields predictions for these (reported in the full paper), in rough agreement with experiment.

---

## Impact and Legacy

DKKT has not become as mainstream as NCG or string theory, but it has attracted attention in the mathematical physics community as a proof-of-concept: even a very \emph{elementary} geometric structure (a two-point space!) can account for the Weinberg angle.

The approach raises philosophical questions:
- Is the five-dimensional structure "really discrete," or is this an effective low-energy description of a continuous but highly localized compactification?
- How does DKKT relate to lattice gravity or causal dynamical triangulation (CDT), where spacetime itself is discrete?

The DKKT framework is also testable: if one computes higher-order corrections (beyond the tree-level geometric calculation), they should match loop corrections in the SM. This remains an open research direction.

---

## Connection to Phonon-Exflation Framework

**Complementary approach**: Like the phonon-exflation framework, DKKT attempts to derive SM parameters from geometry.

**Comparison with Baptista/Connes**:
- **Connes NCG + KK** (Baptista): Uses continuous SU(3) as internal space; derives $\sin^2\theta_W = 3/8$ from spectral action normalization.
- **DKKT**: Uses discrete two-point space; derives $\sin^2\theta_W = 3/13 \approx 0.231$ from Einstein geometry on the discrete manifold.

These are different predictions! They cannot both be exactly correct.

Numerical comparison:
- Connes: $\sin^2\theta_W = 3/8 = 0.375$
- DKKT: $\sin^2\theta_W = 3/13 \approx 0.231$
- Experiment: $\sin^2\theta_W = 0.23128$

DKKT matches experiment precisely. The Connes value (3/8) does not match experiment; it was recognized as an "approximate" or "tree-level" prediction and has been subject to refinements (loop corrections, threshold effects, KK mixing) in the literature.

**Tension and resolution**: The phonon-exflation framework uses Baptista's Connes-based derivation. If DKKT's prediction is correct, then either:
1. The Connes value receives large corrections (order 0.375 → 0.231), or
2. The two frameworks target different physical scenarios.

A hybrid possibility: DKKT provides the "fundamental" discrete geometry, while the Connes NCG approach describes an \emph{effective} continuous limit of that discrete structure. In that case, the NCG prediction would be approximate.

**Thematic bridge**: Both frameworks move toward the phonon-exflation goal of explaining why the SM parameters have the values they do. DKKT demonstrates that even minimal geometric input (two points!) suffices; the phonon-exflation framework (via the BCS instability) proposes that the geometry itself is dynamically determined by many-body physics.

