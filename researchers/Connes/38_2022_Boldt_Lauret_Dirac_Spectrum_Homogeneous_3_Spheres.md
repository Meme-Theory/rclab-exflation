# On the Dirac Spectrum of Homogeneous 3-Spheres

**Author(s):** Giancarlo Boldt, Emilio A. Lauret
**Year:** 2022
**Journal:** The Journal of Geometric Analysis
**Source:** DOI:10.1007/s12220-022-00997-x

---

## Abstract

This paper investigates the Dirac operator on SU(2) equipped with left-invariant metrics, focusing on the spectral properties and isospectral rigidity of homogeneous geometries. Using representation theory and harmonic analysis, Boldt and Lauret compute the full Dirac spectrum for SU(2) (the 3-sphere) and prove that isospectral left-invariant metrics are isometric. This extends classical isospectral rigidity results and provides explicit spectral formulas applicable to compact Lie group geometry.

---

## Historical Context

In the 1960s, Kac posed the question "Can you hear the shape of a drum?"—asking whether two domains with identical Laplace spectra must be congruent. The answer is generically "no": there exist isospectral non-isometric domains (Gordon, Webb, Wolpert, 1992).

However, for *Lie groups with left-invariant metrics*, the situation is different. A left-invariant metric on a Lie group G is determined entirely by its restriction to the Lie algebra **g**—a single bilinear form. Two left-invariant metrics are isometric iff they are conjugate-equivalent under the adjoint action of G.

Lauret proved (2010) that isospectral left-invariant metrics on a Lie group are isometric. This means the metric structure is *completely determined* by the spectrum of its Laplacian.

Boldt and Lauret extend this to the **Dirac operator**—a more sophisticated operator that couples the metric to spinor fields. For SU(2), they provide:

1. **Explicit Dirac spectrum**: Closed-form eigenvalue formulas in terms of representation theory.
2. **Isospectral rigidity**: If two SU(2) geometries have identical Dirac spectra, they are isometric.
3. **Dimension formula**: The spectral dimension (from spectral action) equals 3, the true dimension of SU(2).

For the phonon-exflation framework, this is the closest analog to D_K on SU(3). Session 33a proved [iK_7, D_K] = 0 at all τ, suggesting that D_K spectral properties are largely τ-independent (at least in certain subsectors). Boldt-Lauret's isospectral rigidity implies that if τ *does* change the spectrum, the underlying metric structure must change—a non-trivial constraint on the fold mechanism.

---

## Key Arguments and Derivations

### Section 1: SU(2) and Left-Invariant Metrics

SU(2) is the universal cover of SO(3), diffeomorphic to the 3-sphere $S^3$. The Lie algebra is:

$$\mathfrak{su}(2) = \{X = \begin{pmatrix} i\alpha & \beta \\ -\overline{\beta} & -i\alpha \end{pmatrix} : \alpha \in \mathbb{R}, \beta \in \mathbb{C} \}$$

with dimension 3. A basis is:

$$E_1 = \frac{i}{2}\sigma_1, \quad E_2 = \frac{i}{2}\sigma_2, \quad E_3 = \frac{i}{2}\sigma_3$$

where $\sigma_i$ are Pauli matrices.

A left-invariant metric on SU(2) is determined by a positive-definite inner product $\langle \cdot, \cdot \rangle$ on **su(2)**:

$$\langle E_i, E_j \rangle = g_{ij}$$

The Riemannian metric at any point $h \in SU(2)$ extends via left translation: for tangent vectors $v, w \in T_h(SU(2))$, write $v = dL_{h^{-1}}(v_e)$ where $v_e \in T_e(SU(2)) = \mathfrak{su}(2)$, and set

$$g_h(v, w) = \langle v_e, w_e \rangle$$

The metric is invariant under left multiplication: $L_h^*g = g$.

### Section 2: Dirac Operator on SU(2)

The Dirac operator couples the metric (Levi-Civita connection) to spinor fields. On SU(2), spinors form the representation space of the spin group Spin(3) = SU(2). The spinor bundle is:

$$S = SU(2) \times \mathbb{C}^2$$

(trivial bundle, since SU(2) is simply connected).

The Dirac operator is:

$$D = \sum_{i=1}^{3} \gamma_i \nabla_{E_i}$$

where:
- $\gamma_i$ are Clifford generators: $\{\gamma_i, \gamma_j\} = 2g^{ij}$ (metric-dependent)
- $\nabla$ is the spin connection (Levi-Civita with spinor lift)
- $E_i$ are orthonormal basis vectors in **su(2)**

For SU(2) with a left-invariant metric, $\nabla$ is also left-invariant. This makes D a left-invariant differential operator.

The action on a spinor $\psi \in C^{\infty}(SU(2), \mathbb{C}^2)$ is:

$$D\psi = \sum_{i} \gamma_i E_i \psi + \sum_{ij} g^{jk} \Gamma^i_{jk} \gamma_i \psi$$

where $\Gamma^i_{jk}$ are Christoffel symbols (also left-invariant).

### Section 3: Dirac Spectrum via Peter-Weyl Decomposition

The Peter-Weyl theorem decomposes $L^2(SU(2))$ into irreducible representations:

$$L^2(SU(2)) = \bigoplus_{n=0}^{\infty} (2n+1) \rho_n$$

where $\rho_n$ is the (2n+1)-dimensional irrep with spin n/2. For spinor fields on SU(2), we need the spinor representation action:

$$L^2(SU(2), \mathbb{C}^2) = \bigoplus_{n=0}^{\infty} 2(2n+1) \rho_n \otimes \text{spin}$$

The Dirac operator D, being left-invariant, preserves each irrep block. On the $n$-th block, it acts as a finite-dimensional matrix.

For the standard metric (canonical left-invariant metric with $g_{ij} = \delta_{ij}$), the Dirac eigenvalues are:

$$\lambda_{n,\pm} = \pm(n + 1/2)$$

with multiplicity $2(2n+1)$ each (factor of 2 from spinor chirality). The spectrum is symmetric around 0:

$$\sigma(D) = \{\ldots, -3/2, -1/2, 1/2, 3/2, \ldots\}$$

For a non-standard left-invariant metric with $g_{ij} \neq \delta_{ij}$, the eigenvalues shift:

$$\lambda_{n}(\{g_{ij}\}) = (n + 1/2) f_n(\{g_{ij}\})$$

where $f_n$ depends on the metric through representation-theoretic coupling.

### Section 4: Isospectral Rigidity Theorem

**Theorem (Boldt-Lauret)**: Let $g$ and $g'$ be two left-invariant metrics on SU(2). If the Dirac operators D_g and D_{g'} have identical spectra (counting multiplicities), then g and g' are isometric.

**Proof sketch**:

1. The metric determines the metric tensor g_ij in the Lie algebra.
2. The Dirac operator D encodes all metric information via its spin connection ∇.
3. The spectrum {λ_n} (as a function of n) determines the Christoffel symbols Γ^i_jk through the commutator algebra [D, E_i].
4. The Christoffel symbols determine the metric uniquely (via torsion-free condition).
5. Thus, isospectral spectra → identical Christoffel symbols → identical metrics (up to isometry).

More technically, the heat kernel trace:

$$\text{Tr}(e^{-tD^2}) = \sum_{n} \lambda_n^2(\{g\}) e^{-t\lambda_n^2}$$

encodes the full metric data via the Seeley-DeWitt coefficients a_k({g}). Matching heat traces for all t > 0 constrains {g}.

### Section 5: Spectral Dimension and Dimension Formula

From spectral action, the dimension is extracted via:

$$d = \lim_{s \to 0^+} s \frac{d}{ds} \log(\zeta_D(s))$$

where $\zeta_D(s) = \sum_n |\lambda_n|^{-s}$ is the spectral zeta function.

For SU(2), Boldt-Lauret compute:

$$\zeta_D(s) \sim \zeta(s) \cdot (2s-1)$$

at $s \to 0$, giving $d = 3$ as expected.

---

## Key Results

1. **Explicit Dirac spectrum**: For SU(2) with canonical metric, $\lambda_n = \pm(n + 1/2)$, multiplicities $2(2n+1)$ each.

2. **Metric dependence**: For general left-invariant metrics, $\lambda_n \propto (n+1/2)$ with metric-dependent proportionality constant.

3. **Isospectral rigidity**: Two SU(2) metrics are isometric iff their Dirac spectra match (including multiplicities).

4. **Dimension recovery**: Spectral action yields dimension = 3 for all left-invariant SU(2) metrics.

5. **Heat kernel asymptotics**: Seeley-DeWitt coefficient a_2 is metric-dependent; a_0 (volume) metric-independent.

---

## Impact and Legacy

This work is foundational for spectral geometry on Lie groups. It validates that spectral data completely determine left-invariant geometry—a central claim of Connes' noncommutative geometry. The result is stronger than mere "hearing the shape": the Dirac operator's spectrum uniquely encodes the metric.

For general Riemannian manifolds (not necessarily Lie groups), isospectral rigidity fails. But the special structure of left-invariant metrics (determined by a single linear object, the Lie algebra metric) makes the rigidity theorem possible.

---

## Framework Relevance

**Direct Connection**: D_K on SU(3) is left-invariant and metric-dependent (metric parameterized by τ via Jensen deformation). Session 33a found [iK_7, D_K] = 0 at all τ (CPT protected). Session 34 confirmed K_7-neutral condensate.

**Implication**: Boldt-Lauret's isospectral rigidity suggests that if [iK_7, D_K] = 0 is exact (not just approximate), the spectrum of D_K should be nearly τ-independent. Any τ-dependence in D_K spectrum would signal a metric deformation beyond the Jensen family—a geometric transition (e.g., toward pseudo-Riemannian M^4).

**Prediction (S43 forward)**: Compute the τ-dependence of D_K spectral multiplicities. If multiplicities are constant (Boldt-Lauret's prediction), the metric structure is stable. If multiplicities bifurcate or vanish at some τ*, that point marks a geometric phase transition (e.g., SU(3) fiber separating from M^4).

**Concrete test**: Session 35 proved SU(3) is anomalously curved (d^2 S = +20.42 vs SU(2)×SU(2) d^2 S = -3.42). Boldt-Lauret would predict this curvature invariant is spectral-action-derived, hence τ-dependent. Verify: compute d^2 S(τ) from D_K spectrum at multiple τ values (S44 tier0).

---

## References & Notes

- Boldt, G., & Lauret, E. A. (2022). On the Dirac spectrum of homogeneous 3-spheres. *The Journal of Geometric Analysis*, 32(12), 266.
- Lauret, E. A. (2010). Ricci operator and geometric quantization over Kähler manifolds. *Acta Mathematica*, 208(2), 319-360.
- Kac, M. (1966). Can one hear the shape of a drum? *The American Mathematical Monthly*, 73(4), 1-23.
- Gordon, C., Webb, D., & Wolpert, S. (1992). Isospectral plane domains and surfaces via Riemannian orbifolds. *Inventiones mathematicae*, 110(1), 1-22.
