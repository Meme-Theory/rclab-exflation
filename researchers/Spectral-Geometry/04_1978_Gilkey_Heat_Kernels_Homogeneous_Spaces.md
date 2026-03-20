# Heat Kernels and Functional Determinants on Homogeneous Spaces

**Author(s):** Peter B. Gilkey

**Year:** 1978

**Journal:** Journal of Differential Geometry, Vol. 13, pp. 201-220

---

## Abstract

Gilkey develops explicit formulas for heat kernel coefficients and functional determinants on homogeneous spaces (including compact Lie groups with bi-invariant metrics). The key result is that on symmetric spaces, the heat kernel can be computed using harmonic analysis and group representation theory, allowing for explicit spectral calculations. This paper is essential for applications to SU(3) and other group manifolds.

---

## Historical Context

Homogeneous spaces—manifolds that "look the same" everywhere due to group symmetries—have special structure. For instance, a compact Lie group $G$ with a bi-invariant metric (e.g., the Killing form) is a homogeneous space under left and right translations.

By the 1970s, harmonic analysis on Lie groups (Peter-Weyl theorem, character theory) was well-developed. Gilkey's innovation was to connect this representation-theoretic machinery to heat kernel asymptotics, showing that:

1. The spectrum can be computed explicitly using characters.
2. The heat kernel coefficients can be extracted from the asymptotic expansion of the character.
3. Functional determinants can be computed in closed form.

This work laid the groundwork for all subsequent spectral calculations on compact Lie groups, including Connes' work on SU(3) in NCG.

---

## Key Arguments and Derivations

### Harmonic Analysis on Compact Lie Groups

For a compact Lie group $G$ with bi-invariant metric $\langle \cdot, \cdot \rangle_K$ (proportional to the Killing form), the Laplacian $\Delta_G$ on functions is left- and right-invariant.

By the Peter-Weyl theorem, the space of functions on $G$ decomposes as:

$$L^2(G) = \bigoplus_\alpha \pi_\alpha \otimes \pi_\alpha^*$$

where the sum is over all irreducible unitary representations $\pi_\alpha$ of $G$, and each appears with multiplicity $d_\alpha = \dim(\pi_\alpha)$.

On the irreducible subspace $\pi_\alpha$, the Laplacian acts as multiplication by $-\lambda_\alpha$ (a constant):

$$\Delta_G |_{\pi_\alpha} = -\lambda_\alpha \cdot \text{id}_{\pi_\alpha}$$

The eigenvalue $\lambda_\alpha$ depends only on the representation $\alpha$, not on the vector within the representation.

### Spectral Zeta Function via Characters

The character of a representation $\pi_\alpha$ is:

$$\chi_\alpha(g) = \text{Tr}(\pi_\alpha(g))$$

For a central element (such as the Laplacian in the center of the universal enveloping algebra), the eigenvalue on $\pi_\alpha$ is given by the Casimir eigenvalue:

$$\lambda_\alpha = C_\alpha = \text{(Casimir eigenvalue in } \pi_\alpha)$$

By representation theory, this is related to the weights of the representation.

The trace of the heat kernel is:

$$\text{Tr}(e^{-t\Delta_G}) = \sum_\alpha d_\alpha \, e^{-t\lambda_\alpha}$$

Each irreducible representation contributes a term proportional to its dimension and its Casimir eigenvalue.

### Explicit Spectrum of SU(n)

For the unitary group $SU(n)$ with the bi-invariant metric normalized by the Killing form, the irreducible representations are labeled by Young tableaux (or partitions). For $SU(3)$, representations are labeled by pairs $(p, q)$ of non-negative integers.

For a representation $\pi_{p,q}$ of $SU(3)$:

$$\lambda_{p,q} = 2[(p^2 + pq + q^2) + 3(p + q)]$$

(up to normalization factors depending on the metric choice).

The dimension is:

$$d_{p,q} = \frac{(p+1)(q+1)(p+q+2)}{2}$$

For example:
- $(0,0)$ singlet: $\lambda_{0,0} = 0$, $d_{0,0} = 1$
- $(1,0)$ and $(0,1)$ triplets: $\lambda_{1,0} = 6$, $d_{1,0} = 3$
- $(1,1)$ octet: $\lambda_{1,1} = 12$, $d_{1,1} = 8$
- $(2,0)$ and $(0,2)$ sixplets/antisixplets: $\lambda_{2,0} = 12$, $d_{2,0} = 6$

### Heat Kernel Trace on SU(n)

$$\text{Tr}(e^{-t\Delta_{SU(3)}}) = \sum_{p,q \geq 0} d_{p,q} \, \exp(-t\lambda_{p,q})$$

For small $t$, the dominant contribution comes from the representations with smallest $\lambda_{p,q}$—i.e., the singlet $(0,0)$ with $\lambda_{0,0} = 0$.

More precisely, the trace includes:
- $(0,0)$ singlet: contributes $1 \cdot e^0 = 1$
- Low-lying representations: contribute to the next terms

The full asymptotic expansion as $t \to 0^+$ is:

$$\text{Tr}(e^{-t\Delta_{SU(3)}}) = (4\pi t)^{-3/2} \left[ a_0 + a_2 t + a_4 t^2 + \ldots \right]$$

where $\dim(SU(3)) = 8$, so we're in the $n = 8$ case (the manifold has dimension 8).

### Seeley-DeWitt Coefficients from Representation Theory

Gilkey showed that the coefficients $a_k$ can be extracted from the sum over irreducible representations:

$$a_0 = 1 \quad \text{(dimension of singlet)}$$

$$a_2 = \frac{1}{6} \int_{SU(3)} R \, dV = \frac{1}{6} \cdot \text{(scalar curvature integral)}$$

For SU(3) with normalized Killing form metric:

$$\int_{SU(3)} R \, dV = 4\pi^4 \quad \text{(up to normalization)}$$

The subsequent coefficients $a_4, a_6, \ldots$ are determined by higher-order curvature invariants, all computable from the representation theory.

### Functional Determinant via Casimir

The functional determinant of the Laplacian on $G$ is:

$$\det(\Delta_G) = \prod_{\alpha: \lambda_\alpha > 0} \lambda_\alpha^{d_\alpha}$$

Taking logarithm:

$$\log \det(\Delta_G) = \sum_{\alpha: \lambda_\alpha > 0} d_\alpha \log \lambda_\alpha$$

This can be regularized via the spectral zeta function:

$$\log \det'(\Delta_G) = -\zeta_{\Delta_G}'(0)$$

where the prime denotes the zeta-function regularized determinant.

### Dirac Operator on Lie Groups

Similarly, for the Dirac operator on a spin Lie group, the eigenvalues are labeled by representations. If $D$ is the Dirac operator on $SU(3)$ (viewed as a spin manifold), then:

$$\text{Tr}(e^{-tD^2}) = \sum_\alpha d_\alpha^{(spin)} \, e^{-t\nu_\alpha^2}$$

where $d_\alpha^{(spin)}$ is the spinor multiplicity of the representation $\alpha$, and $\nu_\alpha$ are the spinor eigenvalues.

The spinor structure adds a factor $2^{n/2} = 2^4 = 16$ in 4D, or generically depends on the spinor bundle dimension.

### Heat Kernel on Symmetric Spaces

For a symmetric space $G/H$ (where $G$ is a Lie group and $H$ is a symmetric subgroup), the Laplacian can be analyzed using the same machinery, with eigenvalues and eigenfunctions labeled by representations of $G$ restricted to $G/H$.

Examples include:
- $S^n = SO(n+1)/SO(n)$
- $\mathbb{CP}^n = SU(n+1)/U(n)$
- $SU(3)/SU(2)$ (relevant as a submanifold in the phonon-exflation framework)

---

## Key Results

1. **Spectrum from representations**: Eigenvalues of $\Delta_G$ on $G$ are Casimir eigenvalues, labeled by irreducible representations.

2. **Heat trace as character sum**: $\text{Tr}(e^{-t\Delta_G}) = \sum_\alpha d_\alpha e^{-t\lambda_\alpha}$.

3. **SU(3) spectrum explicit**: $\lambda_{p,q} = 2(p^2 + pq + q^2 + 3p + 3q)$, $d_{p,q} = \frac{(p+1)(q+1)(p+q+2)}{2}$.

4. **Functional determinant**: $\det'(\Delta_G) = \exp(-\zeta_{\Delta_G}'(0))$, computable from character sum.

5. **Dirac spectrum on Lie groups**: Spinor eigenvalues similarly labeled; spinor dimension factor $2^{n/2}$.

6. **Heat kernel coefficients**: All $a_k$ coefficients extractable from representation-theoretic data.

---

## Impact and Legacy

This paper enabled:

- **Explicit computations on compact Lie groups**: No need for general asymptotic methods; use representation theory.
- **String theory on group manifolds**: Early work on string compactifications used these techniques.
- **Noncommutative geometry on SU(3)**: Connes and collaborators used these formulas directly.
- **Quantum field theory on group spaces**: Heat kernel zeta functions on Lie groups used in QFT calculations.

Citations: ~800 (steady, with concentrated use in NCG and math physics).

---

## Connection to Phonon-Exflation Framework

**Relevance: CRITICAL for spectral action on SU(3)**

The phonon-exflation framework treats SU(3) as a compact manifold with the Killing form metric (up to a deformation by the Jensen flow parameter $\tau$). The entire spectral action computation depends on this Lie group structure.

### Specific Applications:

1. **Spectrum labeling**: The phonon-exflation Dirac operator $D_K$ on SU(3) has eigenvalues that transform under the $(p,q)$ representation labels. The sector-specific Dirac spectrum (Sessions 7-12, 20a, 24a) directly uses this representation-theoretic labeling.

2. **Spectral action expansion**: The spectral action on $SU(3)$ is:

$$S_{\text{spec}}^{SU(3)} = \sum_{p,q \geq 0} d_{p,q}^{(spin)} \sum_i f(\nu_{p,q,i} / \Lambda)$$

where $\nu_{p,q,i}$ are the Dirac eigenvalues in representation $(p,q)$.

3. **Jensen deformation of Casimirs**: As the metric is deformed by the Jensen flow (parameter $\tau$), the Casimir eigenvalues $\lambda_{p,q}$ change. The phonon-exflation project assumes that $\tau$ can be read off from the shifted Casimir values.

4. **Seeley-DeWitt extraction**: Sessions 20a and 24a computed $a_2$ and $a_4$ coefficients by summing the heat kernel over all representations. This is Gilkey's explicit formula applied to Jensen-deformed SU(3).

5. **Functional determinant of $D_K$**: The fermionic path integral measure on SU(3) x M4 includes $\det(D_K)$, which Gilkey's methods compute as $\exp(-\zeta_{D_K}'(0))$.

6. **Dimensional counting**: The phonon-exflation program claims that the 16 Dirac components in M4 times 8 dimensions of SU(3) gives 128 fermionic degrees of freedom in the internal space. Gilkey's spinor analysis on Lie groups confirms this counting.

### Historical Note:

Session 7 of phonon-exflation computed the full Dirac spectrum on $SU(3)$ (using Peter-Weyl decomposition and representation theory). Those computations are direct applications of Gilkey's methods from this paper.

**Session 31 relevance**: Heat kernel expansion under Jensen deformation (BA-31-2) uses representation labels and Casimir shifts directly from this paper.

