# Inaudibility of Naturally Reductive Property

**Author(s):** Arias-Marco, Fernández-Barroso
**Year:** 2025
**Journal:** arXiv:2502.10332 (submitted Feb 2025)

---

## Abstract

We prove that one cannot determine if a closed Riemannian manifold is naturally reductive using the information encoded in the spectrum of the Laplace-Beltrami operator. We construct an isospectral pair of nine-dimensional 2-step nilmanifolds where one is naturally reductive and the other is not, establishing natural reductivity as an inaudible geometric property.

---

## Historical Context

**Inverse Spectral Geometry** asks: given the spectrum of the Laplace-Beltrami operator (the "can you hear it" question, famously posed by Mark Kac), what geometric properties of a manifold can be uniquely determined?

Some properties are **audible** (determinable from spectral data alone):
- Dimension
- Volume
- Total scalar curvature (via heat kernel coefficients $a_0, a_2$)
- Diameter (via spectral gap)

Other properties are **inaudible** (two non-isometric manifolds can share the same spectrum):
- Local curvature at specific points
- Certain topological features
- Kummer surfaces and their isospectral partners (classical examples)

**Naturally reductive manifolds** are a special class of homogeneous Riemannian spaces with a canonical decomposition of the Lie algebra, ensuring geodesic homogeneity and unique canonical connection. They generalize symmetric spaces and include important examples (Einstein homogeneous spaces, principal bundles with invariant metrics, certain supergravity backgrounds).

The question: Is natural reductivity audible? That is, if two manifolds are isospectral, must they share the same natural reductivity property?

Arias-Marco and Fernández-Barroso answer **NO** with a striking counterexample: a pair of isospectral 9D nilmanifolds, one naturally reductive and one not.

For phonon-exflation, this is profound: the framework assumes the SU(3) fiber is a naturally reductive homogeneous space (inherited from its symmetric space structure). This inaudibility result warns that spectral data alone cannot confirm natural reductivity—the assumption must be validated geometrically, not spectral-theoretically.

---

## Key Arguments and Derivations

### Naturally Reductive Homogeneous Spaces

A homogeneous space $G/H$ with Riemannian metric $g$ inherited from an invariant metric on $G$ is **naturally reductive** if there exists a $G$-invariant complement $\mathfrak{m}$ to the Lie algebra $\mathfrak{h}$ of $H$ in $\mathfrak{g}$ (Lie algebra of $G$) such that:

$$\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{m}, \quad [H, \mathfrak{m}] \subseteq \mathfrak{m}$$

The canonical metric on $G/H$ is induced by an inner product on $\mathfrak{m}$ that is:
1. Invariant under $\text{Ad}_H$ (adjoint action of $H$)
2. Extends naturally from the metric on $G$

**Criterion**: A homogeneous space is naturally reductive iff the Levi-Civita connection on $G/H$ is uniquely determined by the metric structure without arbitrary choices.

### Ambrose-Singer Characterization

Arias-Marco and Fernández-Barroso employ the **Ambrose-Singer theorem**: a Riemannian manifold $(M, g)$ is naturally reductive as a homogeneous space of some Lie group iff certain algebraic conditions on the curvature tensor hold.

For 2-step nilpotent Lie groups (relevant to their construction), these conditions simplify: a 2-step nilmanifold $\Gamma \backslash N$ (where $N$ is a 2-step nilpotent Lie group and $\Gamma$ a discrete cocompact subgroup) is naturally reductive iff the structure constants of $N$ satisfy specific symmetry relations.

### Isospectral Nilmanifolds: Construction

**Key insight**: Nilmanifolds admit high degrees of freedom in their spectral data while maintaining distinct geometric structures. Two non-isometric nilmanifolds can be isospectral if their curvature tensors, while different, produce the same spectral asymptotics.

Arias-Marco and Fernández-Barroso construct:

**Manifold 1 ($M_1$)**: A 9-dimensional 2-step nilpotent homogeneous space $G_1/\Gamma_1$ where:
- Structure: $\mathfrak{n}_1 = V_1 \oplus Z_1$, $\dim(V_1) = 6$, $\dim(Z_1) = 3$
- Bracket: $[V_1, V_1] = Z_1$ (defining relation for 2-step)
- **Naturally reductive**: The Ambrose-Singer conditions hold; the metric extends canonically from $G_1$.

**Manifold 2 ($M_2$)**: A 9-dimensional 2-step nilpotent homogeneous space $G_2/\Gamma_2$ where:
- Structure: $\mathfrak{n}_2 = V_2 \oplus Z_2$, $\dim(V_2) = 6$, $\dim(Z_2) = 3$
- Bracket: $[V_2, V_2] = Z_2$
- **Not naturally reductive**: The Ambrose-Singer conditions fail; there is no canonical metric decomposition.
- However, metrics on $M_2$ can be chosen such that the spectrum matches $M_1$'s spectrum.

### Proof of Isospectrality

The spectral zeta function for a compact Riemannian manifold is:

$$\zeta(s) = \sum_k \lambda_k^{-s}$$

Arias-Marco and Fernández-Barroso prove $\zeta_1(s) = \zeta_2(s)$ for all $s$ in the complex plane (after analytic continuation).

**Method**:
1. Compute the heat kernel expansion on both manifolds using the nilpotent structure.
2. For 2-step nilmanifolds, the heat kernel $K_t(x, x)$ admits a closed-form expression in terms of structure constants.
3. Show that, although $M_1$ and $M_2$ have different structure constants, the sum $\int_M K_t(x, x) dV$ (trace of heat kernel) is identical for both at all times $t > 0$.
4. Laplace transform inversion recovers the spectral counting function $N(\lambda)$, proving isospectrality.

**No acoustic isothermic**: The heat kernel traces agree despite the two manifolds having genuinely different geometric structures. The cancellations are highly non-trivial, demonstrating that spectra can be "deceived" about underlying structure.

---

## Key Results

1. **Natural Reductivity is INAUDIBLE**: The first explicit proof that two isospectral Riemannian manifolds can differ in their naturally reductive status.

2. **9D Nilmanifold Counterexample**: Provides a concrete isospectral pair where $M_1$ is naturally reductive (Ambrose-Singer conditions hold) and $M_2$ is not (conditions fail).

3. **Spectral Limitation Identified**: The spectrum encodes heat kernel coefficients $a_0, a_2, a_4, \ldots$ but **not** the fine algebraic structure of the manifold's homogeneous decomposition $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{m}$.

4. **Geometric Invariants Insufficient**: The classical geometric invariants (scalar curvature, Ricci tensor, Weyl tensor) can be identical between $M_1$ and $M_2$ (as verified by the authors), yet they exhibit different natural reductivity.

5. **Implications for Uniqueness**: The inverse spectral problem for homogeneous spaces is fundamentally underdetermined: spectral data alone cannot reconstruct the homogeneous structure uniquely.

---

## Impact and Legacy

Arias-Marco and Fernández-Barroso's work contributes to the ongoing map of "what the spectrum can and cannot hear." It joins a growing catalogue of inaudible properties:
- Isospectral pairs of metrics (Kummer surfaces, Sunada's theorem)
- Non-isometric Ricci-flat Calabi-Yau manifolds with same Hodge diamonds
- Spin structure (Schrödinger-Pauli Laplacian vs. standard Laplacian)

The result has implications for spectral geometry algorithms that attempt to recover manifold structure from spectral data alone. Such algorithms must accept a fundamental limitation: for homogeneous spaces, additional information (curvature tensor coefficients, symmetry group structure) is required beyond the spectrum.

In quantum gravity contexts (CDT, loop quantum gravity), where spectral dimension and heat kernel asymptotics are key observables, the work cautions against assuming that a manifold's symmetry properties can be read off from spectral observables alone.

---

## Framework Relevance

**Critical Limitation**: The phonon-exflation framework assumes SU(3) is a naturally reductive symmetric space. The spectral action principle computes the vacuum energy from heat kernel coefficients:

$$S[\mathcal{D}] = \text{Tr}\, f\left(\frac{\mathcal{D}^2}{\Lambda^2}\right) \sim \sum_n a_n$$

Arias-Marco and Fernández-Barroso prove that these heat kernel coefficients $a_n$—the only spectral data available—**cannot determine whether the underlying geometry is naturally reductive**.

**Implication**:
- The framework's predictions (mass ratios, coupling constants, cosmological parameters) depend on assuming SU(3) is naturally reductive.
- These predictions are spectral (encoded in $a_n$).
- But by the inaudibility result, two non-isometric manifolds—one naturally reductive, one not—could share identical spectra and thus produce identical spectral action values.
- Therefore, **the framework's predictions are not uniquely determined by spectral data alone**.

**Rescue Path (not yet taken)**:
1. Provide non-spectral geometric evidence that SU(3) fiber IS naturally reductive (e.g., explicit connection form, homogeneous structure constants).
2. Accept that the framework predicts one of a degeneracy set of isospectral geometries, each producing the same phenomenology.
3. Distinguish between "spectral predictions" (verified by Arias-Marco inaudibility to be ambiguous) and "geometric predictions" (requiring independent geometric input).

**Current Status**: The framework relies implicitly on assuming natural reductivity. Arias-Marco and Fernández-Barroso's result flags this assumption as **not spectral-theoretically justified**. The assumption must be validated geometrically (via Ambrose-Singer criteria or explicit homogeneous structure) or abandoned.

**Action Item** (future work): Verify explicitly that the framework's SU(3) fiber satisfies Ambrose-Singer conditions for natural reductivity. If not, reevaluate which geometric structures are actually constrained by spectral data.

---

## Connection to Phonon-Exflation Framework

The inaudibility of natural reductivity is both a **warning and an opportunity**:

**Warning**: Do not assume spectral consistency ensures geometric consistency. Two different geometries can produce the same spectral predictions.

**Opportunity**: If the framework's phenomenological predictions (masses, couplings, cosmology) are robust even across a family of isospectral geometries, then the framework has discovered a **spectral stability principle**—a prediction that transcends the specific geometry, depending only on spectral data (heat kernel coefficients) and homogeneous group structure.

This distinction—between spectral predictions (robust) and geometric predictions (ambiguous)—should be explicitly drawn in future framework papers.

**Constraint Status**: EPISTEMIC. Arias-Marco and Fernández-Barroso establish a fundamental limit on inverse spectral geometry. The framework must operate within this limit or provide non-spectral geometric input to lift the ambiguity.
