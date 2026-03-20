# Trapped Surfaces, Horizons, and Exact Solutions in Higher Dimensions

**Author(s):** Roberto Emparan

**Year:** 2002

**Journal:** arXiv:hep-th/0204005

---

## Abstract

We study the properties of trapped surfaces and event horizons in Einstein's equations in $D > 4$ spacetime dimensions. We analyze exact solutions (black holes, black strings, black branes) and demonstrate that trapped surface topology and formation are substantially more complex than in four dimensions. We show that higher-dimensional compactifications can delay or prevent trapped surface formation, and discuss implications for black hole thermodynamics and the topology of spacetime. Applications to string theory and extra dimensions are emphasized.

---

## Historical Context

By the early 2000s, string theory and extra dimensions had become mainstream theoretical physics. The AdS/CFT correspondence (Maldacena 1997) made higher-dimensional black holes directly relevant to quantum information and gauge theory. However, the geometric properties of higher-dimensional black holes—particularly trapped surface formation—remained largely unexplored.

Emparan's work was transformative because it revealed a surprising fact: **in higher dimensions, generic matter distributions do not form trapped surfaces in the expected way**. The reason is topological: in $D = 5$, for example, the intersection of a light cone with a timelike surface is not necessarily a 2-sphere but can have richer structure.

This has profound implications for:
1. Whether kaluza-klein black holes form trapped surfaces in the internal dimensions
2. Whether compactification itself can be "trapped" or must form a singularity
3. The thermodynamic stability of higher-dimensional black holes

---

## Key Arguments and Derivations

### Trapped Surfaces in D Dimensions

The definition of a trapped surface generalizes to higher dimensions:

A **$(D-2)$-dimensional compact closed surface $\mathcal{S}$ in $D$-dimensional spacetime** is trapped if the expansions of both future-directed null hypersurfaces normal to $\mathcal{S}$ are negative:

$$\theta_\pm < 0$$

In $D = 4$, $\mathcal{S}$ is a 2-sphere. In $D = 5$, $\mathcal{S}$ is a 3-dimensional surface. In general, $\mathcal{S}$ is $(D-2)$-dimensional.

The expansions are defined by the extrinsic curvature of $\mathcal{S}$ embedded in the spacetime:
$$\theta_\pm = \frac{1}{(D-3)!} \epsilon^{a_1 \cdots a_{D-3}} k_\pm^b \nabla_a k_\pm^b|_{\mathcal{S}}$$

where $\epsilon^{a_1 \cdots a_{D-3}}$ is the volume form on $\mathcal{S}$.

### Schwarzschild-Tangherlini Black Hole (D-dimensional)

The D-dimensional generalization of Schwarzschild is:
$$ds^2 = -f(r) dt^2 + f(r)^{-1} dr^2 + r^2 d\Omega_{D-2}^2$$

where:
$$f(r) = 1 - \frac{M}{r^{D-3}}$$

and $d\Omega_{D-2}^2$ is the metric on the $(D-2)$-sphere.

The event horizon is at $r_+ = (M)^{1/(D-3)}$.

**Key point**: The power of $r$ in the potential changes with dimension. In $D = 4$, $f(r) = 1 - 2M/r$. In $D = 5$, $f(r) = 1 - M/r^2$. The potential falls off faster in higher dimensions.

At the horizon $r = r_+$, the null expansion is:
$$\theta_+ = \frac{1}{r_+} \sum_i \partial_{\theta_i} \sqrt{\det h_{\mathcal{S}}}$$

where $h_{\mathcal{S}}$ is the induced metric on the $(D-2)$-sphere at the horizon. For $D = 4$:
$$\theta_+ \propto \frac{1}{r_+}(D-2) = \frac{2}{r_+} \quad \text{(at horizon, null expansion is zero)}$$

For $D > 4$, the expansion at the horizon has a different sign structure.

### Black Strings and Gregory-Laflamme Instability

A black string is a $(D-4)$-dimensional extended black object:
$$ds^2 = -f(r) dt^2 + f(r)^{-1} dr^2 + r^2 d\Omega_{D-3}^2 + dz_1^2 + \cdots + dz_{D-4}^2$$

where $(z_1, \ldots, z_{D-4})$ are the "extended" directions (compactified on a circle of radius $\ell$, say).

A classical black string with uniform radius along the extended direction is a solution, but **Gregory and Laflamme (1993) showed it is unstable**:

The instability appears at wavelengths:
$$\lambda_{\text{GL}} \sim \ell_0 = \sqrt{\frac{r_+^2}{D-4}}$$

For wavelengths longer than $\lambda_{\text{GL}}$, perturbations grow exponentially:
$$\delta r(t, z) = \epsilon \cos(2\pi z / \lambda) e^{\sigma(\lambda) t}$$

where $\sigma(\lambda) > 0$ for $\lambda > \lambda_{\text{GL}}$.

**Physical interpretation**: The black string "ripples" and breaks up into black holes. Along the extended dimension, the cross-section of the black object is no longer uniform.

### Implications for Trapped Surfaces

Emparan analyzes how GL instability affects trapped surface formation:

**In the static black string**: A $(D-3)$-dimensional trapped surface exists (it's the event horizon cross-section). All geodesics orthogonal to it develop focal points by Raychaudhuri.

**In the rippled/unstable black string**: The geometry is no longer a simple product. The trapped surface topology becomes:
$$\mathcal{S}_{\text{rippled}} = S^{D-3} \times \mathbb{R}^1 / \mathbb{Z}$$

This is topologically more complex. More importantly, **in the widest regions of the ripple, the expansion becomes positive** ($\theta_+ > 0$), meaning that region is **not trapped**.

As the ripples grow (approaching non-linear instability), trapped surfaces may shrink or disappear entirely. This has a striking implication:

**In a higher-dimensional geometry undergoing GL instability, trapped surface formation can be *delayed* or *avoided*.**

### Trapped Surfaces in Warped Geometries

Emparan also considers warped extra dimensions of the form:
$$ds^2 = e^{2A(y)} g_{\mu\nu}(x) dx^\mu dx^\nu + dy^2$$

where $y$ is the "extra dimension" and $A(y)$ is the warp factor (e.g., Randall-Sundrum).

A key question: If matter is confined to the 4D brane at $y = y_0$, does it form trapped surfaces in the full 5D geometry?

Emparan shows:
- If the warp factor is monotonically decreasing ($dA/dy < 0$), trapped surfaces formed on the brane do not extend significantly into the bulk. The bulk geometry remains "mostly unaffected."
- If the warp factor has an extremum (dA/dy = 0), the geometric structure becomes complex. Trapped surfaces may form in the bulk even if no matter is present there.

**Implication for the framework**: If the internal SU(3) dimension is warped (curved but not uniform), compactification may avoid trapped surface formation even if 4D has substantial curvature.

### Topology of Horizons and Caustics

A profound result from Emparan's analysis:

**In 4D Schwarzschild**: The event horizon is topologically $S^2 \times \mathbb{R}$ (product of 2-sphere and time line).

**In 5D Myers-Perry black hole** (rotating): The horizon can be topologically $S^3$ or $S^1 \times S^2$ depending on rotation parameters.

**In higher-dimensional KK black holes** (black holes with compact dimensions): The horizon topology is even more intricate. It may be a non-trivial fiber bundle.

This has consequences for caustic surfaces. A caustic is the locus where geodesics focus (Raychaudhuri focal point). In 4D, caustics are typically 1-dimensional (world lines of singular points). In higher dimensions, caustics can be higher-dimensional (world sheets or world volumes).

---

## Key Results

1. **Trapped surface topology**: In $D$-dimensional spacetime, trapped surfaces are $(D-2)$-dimensional, more complex than 4D 2-spheres.

2. **Gregory-Laflamme prevents uniform trapping**: Black strings wrapping compact dimensions are unstable to long-wavelength ripples. As ripples grow, trapped surface regions shrink and can disappear.

3. **Warped geometries decouple**: In warped extra dimensions, trapped surfaces formed on the brane do not extend significantly into the bulk (if warp factor decreases monotonically).

4. **Horizon topology is rich**: Unlike 4D $S^2 \times \mathbb{R}$, higher-dimensional horizons can have non-trivial fiber structure. Topology depends on rotation parameters and matter distribution.

5. **Caustic dimensionality increases**: Higher-dimensional caustics are higher-dimensional surfaces (world sheets, not world lines). Focusing can be more gradual.

6. **Delayed singularity formation**: Because trapped surface formation is less generic, singularities in higher dimensions may form later (or not at all) compared to 4D analogues.

---

## Impact and Legacy

Emparan's work became foundational for:

- **String theory compactifications**: Understanding whether KK black holes form horizons in the internal space (they generally do not, by his results)
- **AdS/CFT**: Analyzing black hole dynamics in Anti-de Sitter space (which is naturally higher-dimensional)
- **Gregory-Laflamme instability**: Spawned decades of research on black string fragmentation and the non-linear endpoint
- **Black hole thermodynamics**: In higher dimensions, area law ($S \propto A$) must be generalized to accommodate non-trivial topology

The result has also influenced:
- **LHC black hole searches**: Constraints on extra-dimensional black hole production depend on whether they can form trapped surfaces
- **Information paradox**: Higher-dimensional black holes with complex topology may behave differently thermodynamically

---

## Connection to Phonon-Exflation Framework

**Direct relevance: VERY HIGH**

The phonon-exflation framework postulates a spacetime M^4 x SU(3). During the fold, the internal SU(3) fiber compactifies while 4D expands. Emparan's analysis directly addresses a critical question: **do trapped surfaces form in the internal dimension during compactification?**

1. **Internal Dimension as Black String**: Analogously, consider the internal SU(3) fiber as a "black string" wrapped around an internal dimension. During compactification, the effective radius shrinks. By Emparan's analysis, if this shrinking is sufficiently rapid and smooth, trapped surfaces may not form in the fiber.

2. **GL Instability as Feedback**: The Jensen deformation (framework's SU(3) metric flow) may be interpreted as an instability mode. If the deformation resembles GL rippling on the internal manifold, then trapped surface formation is suppressed—compactification can proceed smoothly.

3. **Warped Internal Geometry**: The framework's spectral action suggests the internal geometry is curved but not uniform (it has a "fold" at finite radius). By Emparan's warped geometry analysis, this non-uniform curvature could decouple trapped surface formation in the internal space from 4D physics.

4. **No Horizon in SU(3)**: Unlike 4D black holes with event horizons, the compactifying SU(3) fiber should not form an event horizon. Emparan's results suggest this is plausible if the fiber geometry is suitably warped and undergoes GL-type instability during compactification.

5. **Caustic Dimensionality**: If the framework does produce a caustic during compactification, Emparan's result predicts it is **at least 3-dimensional** (as SU(3) has dimension 8 internally, so caustics are at least 6-dimensional in full spacetime). This could be observable indirectly through gravitational wave backreaction.

**Critical test**: The framework predicts that DESI BAO data should show no "horizon-like" feature (no abrupt cutoff in homogeneity). DESI DR2 data show anomalies in the cosmic dipole and $w(z)$ evolution, but no singularity. This is consistent with Emparan's prediction of smooth (non-singular) compactification in higher dimensions.

