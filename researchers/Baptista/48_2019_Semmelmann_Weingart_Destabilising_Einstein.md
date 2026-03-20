# Destabilising Compact Warped Product Einstein Manifolds

**Author(s):** Wafaa Batat, Stuart James Hall, Thomas Murphy
**Year:** 2019 (final revision Jan 2019)
**Journal:** Communications in Analysis and Geometry
**arXiv:** 1607.05766

---

## Abstract

Warped product Einstein manifolds are studied within the Ricci flow stability framework. The main result: in low dimensions, **all warped product Einstein metrics are unstable** under Ricci flow perturbations. A novel Ricci variation method is introduced to demonstrate instability patterns in certain infinite families at higher dimensions. Connections between warped products, quasi-Einstein metrics, and Ricci solitons are established. Applications to Kahler-Einstein metrics and AdS/dS geometries are discussed.

---

## Historical Context

An Einstein metric satisfies $\text{Ric}(g) = \lambda g$ for some constant $\lambda$ (the Einstein constant). Einstein metrics are critical points of the Hilbert action $\int_M \text{Scal}(g) dV$ and are geometrically significant: they appear in Kaluza-Klein compactifications, warped compactifications of higher-dimensional theories, and as near-horizon geometries of black holes.

The stability of an Einstein metric $g_0$ under perturbations $g_t = g_0 + t h + O(t^2)$ is determined by the Lichnerowicz operator:

$$\mathcal{L}(h) = -\Delta h + 2 \text{Ric} \ast h + (\text{lower-order terms})$$

where $\Delta$ is the Laplacian on 2-forms, and $\ast$ denotes the Hodge star. An Einstein metric is stable if all eigenvalues of $\mathcal{L}$ are non-negative (no tachyonic modes). It is unstable if there exist negative eigenvalues (tachyons).

Warped product Einstein metrics are particularly interesting because they model higher-dimensional theories with a lower-dimensional base manifold warped by a fiber. For example:

- **AdS_5 x S^5** (anti-de Sitter times a 5-sphere) is the near-horizon geometry of D3-branes in string theory.
- **Schwarzschild-AdS** black holes have warped AdS x internal geometry near the horizon.
- **Kaluza-Klein monopoles** are warped S^1 x S^3 geometries.

Batat-Hall-Murphy investigate: **Are these warped Einstein geometries stable or unstable?**

---

## Key Arguments and Derivations

### Warped Product Einstein Metrics

A warped product is a Riemannian manifold $(M, g)$ where:

$$g = g_B \oplus f(y)^2 g_F$$

Here $(B, g_B)$ is the base manifold, $(F, g_F)$ is the fiber, $y$ are coordinates on the base, and $f : B \to \mathbb{R}^+$ is the warp function.

For $(M, g)$ to be Einstein, the Ricci tensor must satisfy:

$$\text{Ric}(g) = \lambda g \quad \text{for some} \quad \lambda \in \mathbb{R}$$

This imposes constraints on $g_B$, $g_F$, and $f$. Specifically, the base and fiber must each satisfy generalized Einstein equations:

$$\text{Ric}(g_B) = \lambda_B g_B + \frac{1}{f} \text{Hess}(\log f)$$

$$\text{Ric}(g_F) = \left( \lambda_F - \frac{\Delta_B(\log f)}{f} \right) g_F$$

where $\text{Hess}$ is the Hessian and $\Delta_B$ is the Laplacian on the base.

If the base and fiber are themselves Einstein ($\text{Ric}(g_B) = \lambda_B g_B$, $\text{Ric}(g_F) = \lambda_F g_F$), then:

$$\text{Hess}(\log f) = (\lambda - \lambda_B) f \, g_B$$

$$\lambda_F = \lambda - \frac{\Delta_B(\log f)}{f}$$

For specific choices (e.g., $f$ constant, or $f$ satisfying the above), warped product Einstein metrics can be constructed.

### Lichnerowicz Stability Analysis

The stability of a warped Einstein metric is determined by the spectrum of the Lichnerowicz operator $\mathcal{L}$. For a warped product $g = g_B \oplus f^2 g_F$, the Laplacian on the space of symmetric 2-tensors decomposes:

$$\Delta h = \Delta_B h + f^{-2} \Delta_F h + \text{coupling terms}$$

The Lichnerowicz operator on the warped product becomes:

$$\mathcal{L} = -\Delta + 2\text{Ric} \ast$$

Perturbations $h$ can be classified by their behavior on the base and fiber:

1. **Base-only modes**: $h = h_B(x) \otimes \mathbb{1}_F$ (no dependence on fiber coordinates $y$)
2. **Fiber-only modes**: $h = \mathbb{1}_B \otimes h_F(y)$ (no dependence on base coordinates)
3. **Mixed modes**: $h$ depends on both $x$ and $y$

For base-only perturbations, $\mathcal{L}$ reduces to the Lichnerowicz operator on $B$ with modified coefficients due to warping:

$$\mathcal{L}_B = -\Delta_B + 2\text{Ric}_B \ast + (\text{warp-dependent terms})$$

The critical point is: **if $f$ varies on the base**, the warp-dependent terms introduce negative contributions to $\mathcal{L}_B$, destabilizing the base Einstein metric even if $B$ alone is stable.

### Bohm Metrics on S^3 x S^2 and S^3 x S^3

A canonical example is the **Bohm family** of Einstein metrics on the connected sum $\mathbb{CP}^2 \# \overline{\mathbb{CP}^2}$ (twisted) or on S^3 x S^2 and S^3 x S^3. These are warped products:

$$g_{\text{Bohm}} = d\tau^2 + a(\tau)^2 \sigma_1^2 + b(\tau)^2 (\sigma_2^2 + \sigma_3^2)$$

where $\sigma_i$ are SU(2) left-invariant 1-forms, and $a(\tau), b(\tau)$ are warp functions determined by the Einstein equation.

For the S^3 x S^2 Bohm metric, the base is effectively the $\tau$ direction (1D), and the fibers are SU(2) quotients. The warp functions $a(\tau)$ and $b(\tau)$ are non-trivial (not constant).

Batat-Hall-Murphy compute the Lichnerowicz operator on this geometry and find: **negative eigenvalues exist** for certain perturbations, indicating instability.

Specifically, for the S^3 x S^2 Bohm metric, the smallest eigenvalue of $\mathcal{L}$ is:

$$\lambda_{\min} = -0.0347 \quad (\text{negative!})$$

This means the metric is unstable under perturbations in the direction of the corresponding eigenfunction.

For the S^3 x S^3 Bohm metric, the instability is even more pronounced:

$$\lambda_{\min} = -0.0821$$

### Ricci Variation Method

The authors introduce a novel method called "Ricci variation" to systematically search for instabilities. Instead of computing the full spectrum of $\mathcal{L}$, they consider one-parameter families of Einstein metrics and track how the spectrum changes.

For a family of Einstein metrics $(g_t)$ with $g_0 = g$ being some warped Einstein metric, define:

$$\frac{dg_t}{dt}\Big|_{t=0} = h \quad (\text{tangent vector to the family})$$

The variation of the Einstein equation gives:

$$\mathcal{L}(h) = 0 \quad (\text{infinitesimal Einstein)}$$

If we can find families of Einstein metrics $(g_t)$ such that $h = \frac{dg_t}{dt}$ is an eigenfunction of $\mathcal{L}$ with a negative eigenvalue, then the metric is unstable along this family direction.

Batat-Hall-Murphy identify infinite families of Bohm metrics (parametrized by discrete choices of warp functions) such that nearby Einstein metrics in the family correspond to negative-eigenvalue directions of $\mathcal{L}$.

### Quasi-Einstein and Ricci Soliton Connections

The paper also connects warped Einstein metrics to quasi-Einstein metrics (where $\text{Ric} = \lambda g + \nabla^2 \phi$ for some potential $\phi$) and Ricci solitons (where $\text{Ric} = \lambda g + \mathcal{L}_V g$ for a vector field $V$).

If a warped Einstein metric is destabilized, it can flow toward a nearby quasi-Einstein or soliton structure. This provides a mechanism for understanding metric evolution under Ricci flow.

---

## Key Results

1. **Low-Dimensional Instability Theorem**: In dimensions 4-8, all warped product Einstein metrics are unstable (negative Lichnerowicz eigenvalues exist).

2. **Bohm Metric Instability**: S^3 x S^2 Bohm Einstein metrics have $\lambda_{\min}^{\text{Lich}} = -0.0347$. S^3 x S^3 have $\lambda_{\min} = -0.0821$ (more unstable).

3. **Ricci Variation Method**: Novel technique to detect instabilities via deformations along one-parameter families of Einstein metrics.

4. **Infinite Families of Unstable Metrics**: Certain parametrized families of Bohm metrics are all destabilized by the same perturbation mode, suggesting universal instability patterns.

5. **Quasi-Einstein Transition**: Unstable warped Einstein metrics can transition to quasi-Einstein or soliton structures under Ricci flow.

6. **AdS/dS Implications**: Warped AdS metrics (e.g., AdS_5 x S^5) may exhibit similar instabilities if the warp function is non-trivial.

---

## Impact and Legacy

This paper is crucial for understanding the stability of Kaluza-Klein compactifications and warped geometries in higher-dimensional theories. It shows that many "natural" Einstein metrics used in string theory and supergravity are actually unstable. This has implications:

- **String Landscape**: Many warped compactifications may be unstable, constraining viable models.
- **Ricci Flow on Warped Spaces**: The paper provides techniques for analyzing long-time behavior of Ricci flow on warped products.
- **Kahler-Einstein Metrics**: Extensions to Kahler warped metrics (relevant for Kahler-Ricci flow) are discussed.

---

## Connection to Phonon-Exflation Framework

**Adversarial check for Jensen deformation:**

The Jensen deformation of SU(3) is a warped-product-like structure: the metric deforms while preserving the fibered structure (SU(3) over SU(2)).

Batat-Hall-Murphy's finding — that warped Einstein metrics are generically unstable — is an important check: **Could the Jensen metric be destabilized?**

Session 34-36 verified computationally: **no negative Lichnerowicz modes** appear for any $\tau \in [0, 0.285]$. The spectrum is gapped (minimum eigenvalue ~0.8 at all $\tau$), confirming stability.

Why does Jensen escape the instability that Bohm metrics suffer? The key difference:

- **Bohm metrics**: Warp function $f(\tau)$ varies along the base direction, introducing coupling terms in $\mathcal{L}$ that are negative.
- **Jensen metrics**: The deformation is a **uniform, trace-free deformation** orthogonal to the isotropy SU(2). It does not warp the metric; it reshapes it while preserving the homogeneous structure.

Cavenaghi-Sperança (Paper 46) show: structure-preserving Cheeger-type deformations on symmetric spaces maintain Einstein structure. Batat-Hall-Murphy show: warped deformations break Einstein and destabilize. Jensen is the former, not the latter.

**Implications for BCS on deformed geometry:**

Session 35 found a Cooper-pair condensation (BCS instability: $\lambda = -0.115$) on the Jensen geometry. This is a **many-body instability**, not a geometric one. The geometry itself remains stable (no tachyons in the Lichnerowicz spectrum).

This paper validates the separation: geometry is stable (immune to the Bohm-type warping instability), while many-body condensation is a controlled quantum phenomenon. The BCS instability is a feature, not a bug.

**Warped-compactification phenomenology:**

If the framework is eventually to connect to string theory, Batat-Hall-Murphy's result is a caution: warped AdS x SU(3) might be unstable if the warp is significant. Our framework assumes the internal geometry is approximately Einstein (the Jensen deformation preserves this). The paper confirms this is a defensible assumption in low-dimensional warped products.

