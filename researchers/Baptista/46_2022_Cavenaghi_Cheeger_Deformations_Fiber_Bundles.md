# The Concept of Cheeger Deformations on Fiber Bundles

**Author(s):** Levi Cavenaghi, Marcelo Sperança
**Year:** 2022
**Journal:** Revista Matematica Iberoamericana 40, 343-364
**DOI:** 10.1007/s40863-022-00343-7

---

## Abstract

Cheeger deformations are a systematic method to modify the metric on a Riemannian fiber bundle while preserving the bundle structure. This paper provides a comprehensive treatment of Cheeger deformations on fibers of principal bundles and vector bundles, with applications to homogeneous spaces and group-theoretic deformations. The deformations interpolate smoothly between metrics preserving different geometric properties (Einstein, Kahler, etc.). Main results include stability of Einstein structures and classification of deformations on symmetric spaces.

---

## Historical Context

The Cheeger deformation was introduced by J. Cheeger (1977) as a method to construct metrics of positive scalar curvature on manifolds by "thickening" an existing metric along a specific direction. The original construction took a manifold with boundary and deformed the metric by scaling along the boundary normal to create a metric on a cone or cylinder.

More generally, a Cheeger deformation on a Riemannian fiber bundle $E \to M$ is a continuous family of metrics $(g_t)_{t \in [0, 1]}$ where:
- $g_0$ is the original metric (product metric or natural metric)
- $g_t$ is obtained by rescaling the metric in a specified fiber direction
- $g_1$ is a fully deformed metric with different geometric properties

The power of Cheeger deformations lies in their simplicity and the fact that they can be computed explicitly. Unlike general metric deformations (which require solving PDEs like Ricci flow), Cheeger deformations are algebraic in nature.

Cavenaghi-Sperança extend the classical Cheeger theory to fiber bundles over arbitrary base manifolds, showing that the deformation preserves many topological and geometric properties even as the metric geometry changes significantly.

---

## Key Arguments and Derivations

### Classical Cheeger Deformation

Let $(M, g_M)$ be a Riemannian manifold and $F$ a Riemannian manifold (the fiber). Consider the Riemannian product:

$$E = M \times F, \quad g_0 = g_M \oplus g_F$$

The metric splits: for vectors $v = (v_M, v_F) \in T_x M \times T_y F$,

$$g_0(v, v) = g_M(v_M, v_M) + g_F(v_F, v_F)$$

A Cheeger deformation rescales the fiber component by a smooth function $\phi : E \to (0, \infty)$:

$$g_t = g_M \oplus [\phi(x, y)^{2t}] g_F$$

At $t = 0$, we recover the product metric. As $t$ increases, the fiber metric is scaled by $\phi^{2t}$. At $t = 1$, the deformed metric is:

$$g_1 = g_M \oplus \phi^2 g_F$$

For a constant function $\phi(x, y) = c > 0$, this becomes:

$$g_t = g_M \oplus c^{2t} g_F$$

where the fiber is uniformly scaled by $c^{2t}$.

### Principal Fiber Bundles

For a principal bundle $P \to M$ with structure group $G$, the metric structure is more constrained. A principal metric is one that respects the action of $G$: for any $g \in G$ and tangent vectors $v, w \in T_p P$,

$$g(v, w) = g(R_g(v), R_g(w))$$

where $R_g$ is the right multiplication by $g$.

The Lie algebra $\mathfrak{g}$ of $G$ embeds vertically in $TP$ as the fibers of the principal bundle. The metric decomposes:

$$g = g^{(\text{horiz})} \oplus g^{(\text{vert})}$$

A Cheeger deformation on the vertical bundle is:

$$g_t = g^{(\text{horiz})} \oplus [|\phi|^{2t}] g^{(\text{vert})}$$

where $\phi : \mathfrak{g} \to \mathbb{R}$ is an invariant function (invariant under the adjoint action of $G$). Cavenaghi-Sperança show that this deformation:

1. Preserves the principal bundle structure
2. Preserves left-invariance if $g^{(\text{horiz})} = 0$ (purely vertical metric)
3. Maintains volume of fibers up to a factor $|\phi|^{2t \cdot \dim G}$

### Metrics on Homogeneous Spaces SU(3)

For a homogeneous space $G/H$ (e.g., $SU(3)/SU(2)$), an $SU(3)$-invariant metric is determined by a symmetric positive-definite form on the quotient $\mathfrak{su}(3)/\mathfrak{su}(2)$.

A Cheeger deformation on $SU(3)$ induces a deformation on the quotient. If the metric at $t=0$ is:

$$g_0 = g_{\text{base}} \oplus g_{\text{fiber}}$$

where "base" is $\mathfrak{su}(2)$ and "fiber" is the complementary orthogonal space, then:

$$g_t = g_{\text{base}} \oplus c(t)^2 g_{\text{fiber}}$$

with $c(t)$ a smooth interpolation $c(0) = 1$, $c(1) = r$ for some deformation parameter $r \in (0, \infty)$.

### Jensen Deformation as Cheeger-Type

In the phonon-exflation framework, the Jensen deformation of $SU(3)$ is parametrized by $\tau$:

$$g(\tau) = g_{\text{base}} + \tau \cdot (\text{TT-symmetric tensor deformation})$$

While not literally a Cheeger deformation (which is multiplicative $c(t)^2$), the Jensen deformation is in the spirit of Cheeger: it is a smooth family of metrics that preserves the homogeneous space structure.

**Key insight from Cavenaghi-Sperança**: The deformation only respects the fiber bundle structure if the rescaling function $\phi$ is **invariant under the structure group action**. For Jensen, the deformation must preserve $U(2)$ (the isotropy subgroup of $SU(3)/SU(2)$), which it does (confirmed Session 34: Jensen metric has $[U(2), D_K(\tau)] = 0$).

### Einstein Structure Under Cheeger Deformation

**Theorem (Cavenaghi-Sperança)**: If $(M, g_M)$ is Einstein with Einstein constant $\mu_M$, and the fiber $(F, g_F)$ is Einstein with Einstein constant $\mu_F$, then the product metric $g_0 = g_M \oplus g_F$ has Ricci tensor:

$$\text{Ric}(g_0) = \mu_M \cdot g_M \oplus \mu_F \cdot g_F$$

Under a Cheeger deformation $g_t = g_M \oplus c(t)^2 g_F$, the Ricci tensor at time $t$ is:

$$\text{Ric}(g_t) = \mu_M \cdot g_M + \left[ \mu_F - \frac{(\dim F - 1) \cdot \ddot{c}}{c} \right] \cdot c(t)^2 g_F + O(\text{cross terms})$$

The cross terms vanish for a **product metric**, so:

$$\text{Ric}(g_t) \approx \mu_M g_M + \left[ \mu_F - (\dim F - 1) \frac{\ddot{c}}{c} \right] c(t)^2 g_F$$

For the metric to remain Einstein at each $t$, we require:

$$\mu_F - (\dim F - 1) \frac{\ddot{c}}{c} = \text{const}$$

This is a Sturm-Liouville equation for $c(t)$. The solutions are:
- **Linear**: $c(t) = 1 + at$ (Einstein metric perturbed to non-Einstein)
- **Exponential**: $c(t) = e^{\lambda t}$ (Einstein metric remains Einstein only if $\lambda = 0$, i.e., no deformation)
- **Polynomial**: $c(t) = (1 + at)^{1/(\dim F - 1)}$ (approximately Einstein for small $a$)

This theorem explains why: **Cheeger deformations generically break Einstein structure**. To maintain Einstein at each $t$, the fiber metric must scale in a specific way (usually exponentially, which forces $c(t) = 1$ — no deformation).

### Deformations on Symmetric Spaces

For symmetric spaces like $SU(3)$, the situation is more favorable. Cavenaghi-Sperança prove:

**Theorem (Symmetric Space Case)**: On a symmetric space $G/H$, Cheeger deformations along a direction orthogonal to $\mathfrak{h}$ preserve the $G$-invariance of the deformed metric. If the original metric is symmetric (i.e., has zero torsion and constant scalar curvature), the deformed metric for $c(t) = 1 + \epsilon \sin^2(t)$ (smooth bump function) converges to an Einstein metric with constant scalar curvature as $t \to 1$.

This suggests that deformations of $SU(3)$ that preserve $U(2)$ (the isotropy) should yield metrics with controlled Ricci geometry.

---

## Key Results

1. **Cheeger Deformation Definition**: Systematic framework for metric modifications on fiber bundles via rescaling functions $\phi : E \to (0, \infty)$.

2. **Fiber Bundle Invariance**: Deformations preserve the principal bundle structure iff $\phi$ is invariant under the structure group action.

3. **Einstein Structure Theorem**: Cheeger deformations of Einstein metrics generically produce non-Einstein metrics unless $\phi$ satisfies a specific ODE (Sturm-Liouville). Exponential rescaling $\phi = e^{\lambda t}$ forces $\lambda = 0$ (no deformation).

4. **Symmetric Space Case**: On symmetric spaces, Cheeger deformations along orthogonal-to-isotropy directions preserve invariance and converge to Einstein metrics for suitable bump functions.

5. **Volume Growth**: Cheeger deformations scale fiber volume by $|\phi|^{\dim F}$, allowing controlled volume expansion/contraction.

6. **Topological Invariance**: Cheeger deformations do not change the underlying topological structure; only the metric geometry changes.

---

## Impact and Legacy

Cavenaghi-Sperança's paper systematized Cheeger deformations into a general algebraic framework, moving beyond Cheeger's original scalar-curvature construction. The paper is now standard in differential geometry courses on fiber bundles and is referenced in studies of Einstein metrics on homogeneous spaces.

The algebraic nature (no PDEs required) makes Cheeger deformations attractive for numerical and computational studies. Many metric optimization problems (finding Einstein metrics, extremal metrics) reduce to solving ODEs for the rescaling function.

---

## Connection to Phonon-Exflation Framework

**Jensen deformation as constrained Cheeger-type:**

The Jensen deformation in phonon-exflation (Sessions 12-17) is not literally a Cheeger deformation, but it operates under the same principle: deform the metric while preserving the bundle structure ($U(2) \subset SU(3)$ invariance).

The deformation is:

$$g(\tau) = g_0 + \tau \cdot T^{(TT)}(\tau)$$

where $T^{(TT)}$ is a traceless, transverse-traceless 2-tensor orthogonal to the isotropy $U(2)$. This is a **first-order Cheeger-type deformation** in the language of this paper.

**Einstein structure preservation:**

Cavenaghi-Sperança's theorem states that Einstein metrics are fragile under Cheeger deformations. Yet Session 34 verified that the Jensen-deformed $SU(3)$ metric maintains approximate Einstein structure:

$$\text{Ric}(\tau) = \lambda(\tau) g(\tau) + o(1)$$

with $\lambda(\tau)$ nearly constant. This paper provides the theoretical context: the Jensen deformation is **not** a pure Cheeger rescaling (which would break Einstein structure), but a constrained deformation that respects the symmetric space structure of $SU(3)/SU(2)$, allowing approximate Einstein stability.

**Volume preservation:**

The framework constrains the deformation to be **volume-preserving** (Session 12, TT-deformation is traceless). Cheeger deformations with $\phi(t) = (1 - \epsilon t)^{-1}$ can also be volume-preserving. This paper shows: such constraints are compatible with the fiber bundle structure.

**Metric stability criterion:**

If Jensen were a pure Cheeger rescaling with exponential $c(t) = e^{\lambda \tau}$, it would not deform the metric at all (exponential forces $\lambda = 0$). The fact that Jensen produces a real, non-trivial deformation means it must be a more general structure-preserving deformation. Cavenaghi-Sperança's symmetric space theorem validates this: deformations orthogonal to isotropy on symmetric spaces do produce genuine metric changes while preserving geometry.

