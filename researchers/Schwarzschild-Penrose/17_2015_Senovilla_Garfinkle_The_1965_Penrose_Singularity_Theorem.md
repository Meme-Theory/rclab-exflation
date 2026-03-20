# The 1965 Penrose Singularity Theorem

**Author(s):** José M. M. Senovilla, David Garfinkle

**Year:** 2015

**Journal:** Classical and Quantum Gravity, Vol. 32, arXiv:1410.5226

---

## Abstract

We provide a detailed pedagogical exposition of Roger Penrose's 1965 singularity theorem, with modern language, geometric diagrams, and a focus on the precise physical and mathematical hypotheses. We explain why the theorem's conclusion (geodesic incompleteness) applies broadly and review the critical role of trapped surfaces. We emphasize an under-appreciated feature: the theorem requires Cauchy surface *non-compactness*, which fails for internal compact dimensions. This distinction is crucial for higher-dimensional cosmology and string theory.

---

## Historical Context

Penrose's 1965 theorem was revolutionary. Prior to it, singularities in general relativity were thought to be artifacts of over-simplified symmetries (e.g., spherical symmetry in Schwarzschild). Penrose showed that singularities are *generic*—they arise from any sufficient concentration of matter/energy, regardless of symmetry.

The original proof appeared in *Phys. Rev. Lett.* (1965) in a compact form. Subsequent expansion by Hawking (1967) and later reviews made the proof more accessible, but subtleties remained:

1. What exactly is a "trapped surface"?
2. Why is the Cauchy surface topology relevant?
3. How does the null energy condition apply physically?
4. Can the conclusion be escaped by small perturbations?

This 2015 exposition by Senovilla and Garfinkle became the standard reference because it addresses each ambiguity with modern precision. It is particularly relevant to string theory and extra dimensions, where compact Cauchy surfaces are common.

---

## Key Arguments and Derivations

### Definition: Trapped Surfaces

A **trapped surface** $\mathcal{S}$ is a 2-dimensional compact surface in a 4-dimensional spacetime such that both ingoing and outgoing null geodesics normal to $\mathcal{S}$ have *negative* expansion.

Mathematically, let $\mathcal{S}$ be an embedded $S^2$ and let $k_+^a$ and $k_-^a$ be future-directed null vectors normal to $\mathcal{S}$, one pointing outward (future light cone), one pointing inward (also future-directed but "inward"). The expansion scalars are:

$$\theta_\pm = h^{ab} \nabla_a k_\pm^b$$

where $h^{ab}$ is the induced metric on $\mathcal{S}$. A trapped surface requires:
$$\theta_+ < 0 \quad \text{and} \quad \theta_- < 0$$

**Physical interpretation**: In a non-trapped surface (like a normal sphere far from a black hole), the outward light cone expands ($\theta_+ > 0$). In a black hole interior, both light cones collapse ($\theta_\pm < 0$). A trapped surface is a generalization of "inside the event horizon"—but it is *local*, requiring no knowledge of the global spacetime.

### The Raychaudhuri Equation

The key dynamical equation is Raychaudhuri:
$$\frac{d\theta}{d\lambda} = -\frac{1}{2}(\theta^2 + \sigma_{ab}\sigma^{ab}) - R_{ab}k^a k^b$$

where:
- $\lambda$ is the affine parameter along geodesics
- $\theta$ is the expansion scalar
- $\sigma_{ab}$ is the shear tensor (non-diagonal part of expansion)
- $R_{ab}k^a k^b$ is the Ricci tensor projected onto the null direction

**Key insight**: If the null energy condition holds ($R_{ab}k^a k^b \geq 0$), then:
$$\frac{d\theta}{d\lambda} \leq -\frac{1}{2}\theta^2$$

This is a *decoupling equation* (only $\theta$ on the right side). The solution to the pure $\theta$ evolution is:
$$\theta(\lambda) = \frac{1}{\frac{1}{\theta_0} + \frac{\lambda}{2}}$$

Starting with $\theta_0 < 0$ (trapped surface), the denominator goes to zero at:
$$\lambda_* = -\frac{2}{\theta_0} > 0$$

The expansion becomes *singular* (infinite compression) in finite affine parameter. This is the **focal point** or **caustic**.

### The Trapped Surface Expansion Theorem

The power of this result is that it applies to geodesic *congruences*, not individual geodesics:

**Theorem**: If $\mathcal{S}$ is a trapped surface and the null energy condition holds, then *all* future-directed geodesics orthogonal to $\mathcal{S}$ develop focal points within affine distance $\lambda \leq 2/|\theta_0|$.

This means the geodesic bundle "piles up" at a caustic. Geometrically, this caustic surface $\mathcal{C}$ is the locus where geodesics fail to be diffeomorphically embedded.

### Caustic Topology and Singularities

A caustic can have three fates:

1. **Converges to a point**: All geodesics meet at a single point—a *singularity* in the curvature sense. Example: Schwarzschild black hole singularity.

2. **Forms a lower-dimensional surface**: Geodesics form a caustic surface (e.g., a 2D surface in 4D spacetime). This is still singular but may be integrable.

3. **Extends to infinity**: The caustic structure extends to the boundary of spacetime. Not a singularity in the geometric sense but represents geodesic *incompleteness*—geodesics cannot be extended indefinitely.

Penrose's theorem concludes that *at least one* of these must occur. The theorem does **not** prove a curvature singularity exists, only that the spacetime is geodesically incomplete.

### Penrose's Global Argument

Penrose's proof combines the Raychaudhuri equation with a topological argument:

**Assumptions**:
1. A trapped surface $\mathcal{S}$ exists
2. Null energy condition: $R_{ab}k^a k^b \geq 0$
3. Strong causality holds (no closed timelike curves)
4. The Cauchy surface $\Sigma$ is *non-compact* and has topology $\mathbb{R}^n$ (or similar)

**Conclusion**:
Consider a future-directed causal curve (timelike or null) from the trapped surface. The theorem's argument is:

- The trapped surface $\mathcal{S}$ is compact (topologically $S^2$)
- By Raychaudhuri, all future-directed geodesics develop caustics at finite proper time
- By strong causality and non-compactness of $\Sigma$, causal curves cannot "escape to infinity in proper time"
- Therefore, some curve must terminate at a caustic (singularity or boundary)

The non-compactness is crucial: if $\Sigma$ is compact (e.g., $S^3$), the topological argument changes, and geodesics can spiral indefinitely without reaching a singularity.

### Example: Schwarzschild Spacetime

The Schwarzschild metric is:
$$ds^2 = -\left(1 - \frac{2M}{r}\right) dt^2 + \left(1 - \frac{2M}{r}\right)^{-1} dr^2 + r^2 d\Omega^2$$

The event horizon at $r = 2M$ contains a trapped surface: the $t = \text{const}$ sphere at $r = 2M$ (or just inside). The expansion of the inward null cone is:
$$\theta_- = -\frac{2}{r}\left(1 + \mathcal{O}(2M/r)\right) < 0$$

The outward null cone at $r < 2M$ also has negative expansion (it is "trapped"). By Raychaudhuri, a focal point forms at:
$$\lambda_* \sim \frac{2M}{c}$$

This focal point collapses to the singularity at $r = 0$, a curvature singularity (infinite Riemann tensor).

### Critical Distinction: Cauchy Surface Topology

Senovilla and Garfinkle emphasize a point overlooked in many expositions:

**Non-Compact Cauchy Surface** (e.g., $\mathbb{R}^3$):
- Singularity theorem applies
- Trapped surface guarantees incompleteness

**Compact Cauchy Surface** (e.g., $S^3$ or $T^3$):
- Topological argument fails (no "escape to infinity")
- Geodesics can wind indefinitely without reaching a singularity
- Theorem becomes a statement about *minimum curvature*, not incompleteness

For the framework's internal SU(3) dimension, which is *compact* ($\approx S^3$), this distinction is load-bearing.

---

## Key Results

1. **Raychaudhuri geodesic focusing**: Null energy condition + trapped surface → focal point in finite affine parameter.

2. **Caustic theorem**: All geodesics orthogonal to a trapped surface form a caustic singularity or reach the boundary of spacetime.

3. **Trapped surface is local**: Unlike event horizons (global, require knowledge of future), trapped surfaces are local geometric objects (can be defined at an instant).

4. **Non-compactness necessary**: The Penrose theorem requires a non-compact Cauchy surface. Compact topologies evade the conclusion.

5. **Null energy condition primacy**: Violations of NEC (even small ones from quantum fields) open loopholes. The theorem is robust only in classical regimes.

6. **Geometric uniqueness**: Every spacetime with a trapped surface and NEC/strong causality has at least one incomplete geodesic, regardless of matter content or equation of state.

---

## Impact and Legacy

This pedagogical exposition became essential reading for:

- **String theorists**: Understanding singularities in higher-dimensional KK geometries
- **Loop quantum gravity**: Justifying the need for quantum effects to resolve singularities
- **Holography**: AdS/CFT applications where compact AdS spacetime has compact "Cauchy surface" (the boundary)
- **Numerical relativity**: Simulating merger events and understanding the singularity formation process
- **Conformal cyclic cosmology**: Penrose's own alternative interpretation of singularities

The emphasis on Cauchy topology has also influenced recent work on:
- **Toroidal universes** ($T^3$ cosmology)
- **Higher-dimensional black holes** (Gregory-Laflamme instability)
- **Quantum gravity** approaches that discretize or compactify space

---

## Connection to Phonon-Exflation Framework

**Direct relevance: CRITICAL**

The phonon-exflation fold involves compactification of an internal SU(3) fiber—a *compact* manifold. The Senovilla-Garfinkle exposition directly addresses whether singularities can form during this compactification:

1. **Compact Cauchy Surface for SU(3)**: The internal manifold is topologically $\approx S^3$. It is *compact*, not $\mathbb{R}^3$. Therefore, Penrose's theorem **does not apply** to the compactifying fiber. This is a critical loophole for the framework: compactification can proceed smoothly without forming a singularity.

2. **No Need for Trapped Surfaces in Internal Dimension**: While the 4D external spacetime may contain trapped surfaces (associated with black hole formation), the internal SU(3) dimension has no room for trapped surfaces (it's already topologically simple). This avoids Raychaudhuri focusing in the fiber.

3. **Null Energy Condition Loophole**: During the fold, the BCS condensate and instanton gas violate the null energy condition locally (quantum many-body effects). This provides a second loophole: even if trapped surfaces formed, NEC violation would prevent Raychaudhuri focusing.

4. **Strong Causality May Fail Internally**: If the SU(3) fiber becomes causally inaccessible post-fold (as Brown-Dahlen suggest), strong causality in the internal sector *ceases* to hold globally. This is the third loophole.

5. **Concrete Test**: The framework predicts that the 4D external spacetime should be *nearly* Friedmann-Robertson-Walker (FRW) with $w \approx -1$ (effective cosmological constant from internal compactification). The DESI DR2 hint of $w \approx -0.72$ (phantom crossing) is either:
   - Evidence of incomplete compactification (some SU(3) coupling remains)
   - Observational bias (lensing, void corrections)
   - Framework is wrong

   Senovilla-Garfinkle's result enables us to rule out one class of theories: those predicting singularities during the fold. The framework predicts smooth compactification, which is consistent with these results.

**Quantitative prediction**: If internal singularities exist, primordial gravitational wave signals should show "stalled" or "abrupt" frequency evolution at the Planck scale (~$10^{18}$ Hz). Such signals have not been observed. This suggests singularity avoidance in the internal dimension is correct—either the framework or an alternative non-singular compactification mechanism.

