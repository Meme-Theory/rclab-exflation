# Spectral Isolation of Naturally Reductive Metrics on Simple Lie Groups

**Author(s):** Carolyn S. Gordon, Craig J. Sutton
**Year:** 2010 (v2; original 2007)
**Journal:** arXiv preprint (math.DG)
**arXiv:** 0707.0853
**Relevance:** CRITICAL

---

## Abstract

We show that within the class of left-invariant naturally reductive metrics $\mathcal{M}_{\text{Nat}}(G)$ on a compact simple Lie group $G$, every metric is spectrally isolated. We also observe that any collection of isospectral compact symmetric spaces is finite; this follows from a somewhat stronger statement involving only a finite part of the spectrum.

---

## Key Arguments and Derivations

### 1. Background: Inverse Spectral Geometry

The spectrum $\text{Spec}(M,g) = \{0 = \lambda_0 < \lambda_1 \leq \lambda_2 \leq \ldots\}$ of the Laplacian on a closed Riemannian manifold encodes geometric information. Key questions:
- **Spectral uniqueness**: Is $(M,g)$ determined by its spectrum?
- **Spectral finiteness**: Are isospectral sets finite?
- **Spectral isolation**: Is a punctured neighborhood of $g$ free of isospectral metrics?
- **Spectral rigidity**: Can $g$ be isospectrally deformed?

Known results: round spheres are spectrally isolated (Tanno), flat metrics are spectrally isolated (Kuwabara), constant negative curvature metrics are spectrally isolated (Sharafutdinov), negatively curved metrics are spectrally rigid (Guillemin-Kazhdan, Croke-Sharafutdinov).

### 2. Finiteness of Isospectral Symmetric Spaces (Section 2)

**Theorem 2.3**: Given dimension $n$, volume bound $v > 0$, and fundamental tone $\lambda > 0$, there exists $A > 1$ such that for any finite subset $E \subset [\lambda, A\lambda]$, at most finitely many $n$-dimensional compact symmetric spaces have $\lambda_1 \geq \lambda$, $\text{vol} \geq v$, and $E(M,g) \cap [\lambda, A\lambda] \subset E$.

**Corollary 2.5**: Each compact symmetric space is finitely determined by a lower volume bound and a finite part of its spectrum.

**Corollary 2.6**: A compact symmetric space is finitely determined by its spectrum within the class of compact symmetric spaces.

The proof uses:
- Finiteness of homogeneity types in each dimension (Lemma 2.8)
- For each type $\Gamma \backslash (M_0 \times G_1/K_1 \times \ldots)$, the metric is determined by scaling constants $a_1, \ldots, a_k$ and a flat metric $g_0$
- Finiteness of flat tori with bounded volume and bounded fundamental tone (Mahler compactness)
- Each scaling $a_i$ is determined by a finite part of the spectrum (representation theory of compact Lie groups)

### 3. Naturally Reductive Metrics (Section 3)

A left-invariant metric $g$ on $G$ is naturally reductive if $g([X,Y]_\mathfrak{m}, Z) + g(Y, [X,Z]_\mathfrak{m}) = 0$ for all $X, Y, Z \in \mathfrak{m}$, where $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{m}$ is a reductive decomposition. Equivalently, geodesics through the identity are orbits of one-parameter groups. The D'Atri-Ziller classification describes all naturally reductive left-invariant metrics on compact simple Lie groups.

**Structural result (Proposition 3.6)**: The space $\mathcal{M}_{\text{Nat}}(G)$ of naturally reductive metrics on a simple compact Lie group decomposes into finitely many smooth families, each parameterized by a finite number of real parameters.

### 4. Main Theorem: Spectral Isolation (Section 4)

**Theorem 4.1**: Let $G$ be a compact simple Lie group. Every metric $g \in \mathcal{M}_{\text{Nat}}(G)$ is spectrally isolated within $\mathcal{M}_{\text{Nat}}(G)$. That is, there exists an open neighborhood $U$ of $g$ in $\mathcal{M}_{\text{Nat}}(G)$ such that if $g' \in U$ and $\text{Spec}(G, g') = \text{Spec}(G, g)$, then $(G, g')$ and $(G, g)$ are isometric.

The proof strategy:
1. Each naturally reductive metric has spectrum expressible through representation theory
2. The eigenvalues are algebraic functions of the metric parameters
3. Small perturbations of parameters necessarily change the spectrum (unless the perturbation is by an isometry)
4. Uses the Weyl character formula and Freudenthal's formula for weight multiplicities

### 5. Explicit Spectra (Section 5)

The spectrum of a naturally reductive metric can be computed explicitly using:
- Peter-Weyl decomposition of $L^2(G)$
- Casimir eigenvalues for each irreducible representation
- The naturally reductive Laplacian expressed in terms of Casimir operators for the isotropy representation

---

## Key Results

1. Every naturally reductive metric on a compact simple Lie group is spectrally isolated within the class of naturally reductive metrics (Theorem 4.1)
2. Any collection of isospectral compact symmetric spaces is finite (Corollary 2.6)
3. Compact symmetric spaces are finitely determined by volume + finite spectrum (Corollary 2.5)
4. Finiteness of homogeneity types in each dimension (Lemma 2.8)
5. Bi-invariant metrics are spectrally isolated among all left-invariant metrics (cited from [GSS])
6. Non-trivial isospectral deformations of left-invariant metrics exist on classical groups (Schueth, Proctor) but not among naturally reductive ones

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectrum | $\text{Spec}(M,g) = \{0 = \lambda_0 < \lambda_1 \leq \lambda_2 \leq \ldots\}$ | Section 1 |
| Eigenvalue set | $E(M,g)$ = eigenvalues ignoring multiplicities | Def 2.1 |
| Homothety invariant | $\lambda_1(M,g)^{n/2}\text{vol}(M,g)$ | Remark 2.2 |
| Symmetric metric | $g_i = -a_i B_{\mathfrak{g}_i}$ (multiple of Killing form) | Section 2.7(iii) |
| Natural reductivity | $g([X,Y]_\mathfrak{m}, Z) + g(Y, [X,Z]_\mathfrak{m}) = 0$ | Section 3 |
| Peter-Weyl spectrum | $\Delta_G|_{V_\pi} = -\text{Cas}_\pi \cdot \text{id}$ for each irrep $\pi$ | Section 5 |

---

## Relevance to Phonon-Exflation

This paper is critical because it establishes that the spectrum of the Laplacian (and hence the Dirac operator) on compact Lie groups with naturally reductive metrics is spectrally rigid in a precise sense: small deformations of the metric necessarily change the spectrum. For the M4 x SU(3) framework, this means the Dirac spectrum on the internal SU(3) fiber is a faithful probe of the geometry. If two values of $\tau$ give the same Dirac spectrum, the corresponding metrics must be isometric. This is the mathematical foundation for the claim that the spectral action encodes the full internal geometry. The explicit spectrum computation via Peter-Weyl and Casimir eigenvalues is exactly the method used in the framework's computation computations. The finiteness of isospectral symmetric spaces ensures that the spectral action can distinguish between different internal geometries up to finitely many ambiguities.
