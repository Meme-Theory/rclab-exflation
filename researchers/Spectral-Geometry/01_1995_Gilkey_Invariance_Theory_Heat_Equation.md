# Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem

**Author(s):** Peter B. Gilkey

**Year:** 1995 (first edition 1984)

**Journal/Publisher:** CRC Press, Studies in Advanced Mathematics

---

## Abstract

This is the foundational monograph on heat kernel asymptotics and their role in differential geometry and index theory. Gilkey provides the definitive treatment of Seeley-DeWitt heat kernel coefficients (a_0, a_1, a_2, a_3, a_4), their explicit formulas in terms of curvature invariants, and the path integral representation that connects heat kernels to the Atiyah-Singer index theorem. The work is essential for any computation involving the spectral action principle in noncommutative geometry.

---

## Historical Context

By the 1960s-70s, Atiyah and Singer had proven their index theorem, which relates the analytical index of a differential operator to topological invariants. However, the heat kernel method—introduced by McKean and Singer—provided a constructive, computable approach. The key observation is that the trace of the heat kernel $\text{Tr}(e^{-tD^2})$ expands asymptotically as $t \to 0^+$ with coefficients that are local geometric invariants (Seeley-DeWitt coefficients).

Gilkey's 1984 monograph systematized this entire theory, providing explicit formulas for a_k in terms of the Riemann tensor, its contractions, and covariant derivatives. This became the reference standard for all subsequent work in spectral geometry, NCG, and quantum field theory applications (Connes' spectral action, Vassiliev's work, and modern cosmological models).

The second edition (1995) expanded the treatment and remains the definitive source. It is the book that every spectral geometer, NCG physicist, and mathematical physicist keeps within arm's reach.

---

## Key Arguments and Derivations

### Heat Kernel and Asymptotic Expansion

For a differential operator $D$ (typically the Dirac operator or Laplacian) on a compact manifold $M$, the heat kernel $K_t(x, y)$ solves the heat equation:

$$\frac{\partial K_t}{\partial t} + D^2 K_t = 0, \quad K_0(x, y) = \delta(x - y)$$

For the Laplacian $\Delta$ on a compact Riemannian manifold without boundary, the trace of the heat kernel is:

$$\text{Tr}(e^{-t\Delta}) = \int_M K_t(x, x) \, dV_x$$

As $t \to 0^+$, this trace admits an asymptotic expansion:

$$\text{Tr}(e^{-t\Delta}) \sim \sum_{k=0}^{\infty} a_k \, t^{(k-n)/2}$$

where $n = \dim(M)$ and $a_k$ are the Seeley-DeWitt coefficients. Each $a_k$ is a geometric integral:

$$a_k = \int_M a_k(x) \, dV_x$$

where $a_k(x)$ is the local heat kernel coefficient at point $x$.

### Seeley-DeWitt Coefficients: Explicit Formulas

**Coefficient $a_0$**: Independent of curvature.

$$a_0 = (4\pi t)^{-n/2} \text{Vol}(M)$$

More precisely, $a_0 = \text{rank}(E) \cdot (4\pi)^{-n/2} \text{Vol}(M)$ for a vector bundle $E$.

**Coefficient $a_2$**: Linear in Ricci curvature.

$$a_2 = \frac{1}{6} \int_M \text{Ric} \, dV = \frac{1}{6} \int_M R_{\mu\nu} g^{\mu\nu} \, dV$$

For a scalar (0-form), the Laplacian spectrum is affected by Ricci curvature: positive Ricci curvature decreases eigenvalues (raises the heat kernel decay rate).

**Coefficient $a_4$**: Involves quadratic curvature invariants and fourth-order terms.

$$a_4 = \frac{1}{360} \int_M \left[ 5 R^2 - 2 R_{\mu\nu}^2 + 2 R_{\mu\nu\rho\sigma}^2 \right] dV + \text{lower-order terms}$$

More explicitly:

$$a_4(x) = (4\pi)^{-n/2} \left[ \frac{1}{360}(5R^2 - 2\|Rc\|^2 + 2\|Rm\|^2) + \frac{1}{6}\Delta R \right]$$

where $\|Rm\|^2 = R_{\mu\nu\rho\sigma}^2$ and $\|Rc\|^2 = R_{\mu\nu}^2$.

For the Dirac operator, the $a_4$ coefficient carries different coefficients but has the same structure: it involves $R$, $R_{\mu\nu}^2$, and $R_{\mu\nu\rho\sigma}^2$.

### Heat Kernel for Dirac Operator

For a spin manifold with Dirac operator $D = \gamma^\mu (\partial_\mu + \omega_\mu)$, the heat kernel expansion is:

$$\text{Tr}(e^{-tD^2}) = \int_M K_t^{(D)}(x,x) dV_x$$

The key difference: Dirac eigenvalues come in $\pm \lambda$ pairs (when no anomaly), so the heat kernel includes both positive and negative eigenvalues. The trace of the spinor heat kernel gives:

$$\text{Tr}(e^{-tD^2}) = (4\pi t)^{-n/2} \sum_{k=0}^{\infty} a_k^{(D)} t^{(k-n)/2}$$

with:

$$a_0^{(D)} = 2^{n/2} \cdot \text{Vol}(M)$$

$$a_2^{(D)} = -\frac{n}{6} \int_M \text{Ric} \, dV$$

$$a_4^{(D)} = \frac{1}{360} \int_M \left[ 5(n-1)R^2 - 2(n+13)R_{\mu\nu}^2 + (n+5)R_{\mu\nu\rho\sigma}^2 \right] dV + \ldots$$

The spinor dimension $2^{n/2}$ appears because spinor representations are larger.

### Index Theorem via Heat Kernel

The Atiyah-Singer index of $D$ is:

$$\text{ind}(D) = \text{dim}(\ker D^+) - \text{dim}(\ker D^-) = \lim_{t \to \infty} \text{Tr}(e^{-tD^2})$$

This limit picks out the zero eigenvalues. By a clever contour deformation, one can relate the heat kernel at finite time to a topological integral. The key is that $a_k(x)$ for $k < n$ gives topological information.

For even-dimensional manifolds, the index is a topological invariant (Chern class, Hirzebruch signature, etc.), and the heat kernel calculation reproduces these invariants exactly.

### Heat Kernel on Symmetric Spaces and Lie Groups

On a compact Lie group $G$ with bi-invariant metric, the heat kernel can be computed explicitly using the Peter-Weyl decomposition. If $\lambda_\alpha$ is an eigenvalue of the Laplacian on an irreducible representation $\pi_\alpha$, then:

$$\text{Tr}(e^{-t\Delta_G}) = \sum_\alpha d_\alpha \, e^{-t\lambda_\alpha}$$

where $d_\alpha = \dim(\pi_\alpha)$. For SU(3) with a naturally reductive metric (e.g., the Killing form), this sum can be evaluated explicitly, and the asymptotic expansion can be extracted.

### Spectral Zeta Function

The spectral zeta function is defined via analytic continuation:

$$\zeta(s) = \text{Tr}(\lambda^{-s}) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} e^{-t\lambda} dt$$

For the spectrum of a differential operator, this becomes:

$$\zeta(s) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} \text{Tr}(e^{-t D^2}) dt$$

The heat kernel expansion allows one to evaluate $\zeta(s)$ by residue calculus at specific values (e.g., $\zeta(0)$ for the determinant, $\zeta'(0)$ for the functional integral weight).

### Path Integral Representation

The path integral representation expresses the heat kernel as a sum over paths:

$$K_t(x, y) = (4\pi t)^{-n/2} \sum_{\text{paths from } x \text{ to } y} \exp\left(-\frac{1}{4t} d(x,y)^2\right) \times (\text{geometric corrections})$$

The corrections involve curvature-dependent factors that give rise to the Seeley-DeWitt coefficients. This path integral viewpoint is essential for the functional integral approach to quantum field theory on curved spaces.

---

## Key Results

1. **Seeley-DeWitt expansion**: For any differential operator on a compact manifold, $\text{Tr}(e^{-tD^2}) \sim \sum_k a_k t^{(k-n)/2}$ as $t \to 0^+$.

2. **Explicit $a_0, a_2, a_4$ formulas**: Gilkey provides the exact formulas in terms of curvature invariants (Ricci, scalar curvature, full Riemann tensor).

3. **Dirac heat kernel**: The spinor heat kernel includes explicit $2^{n/2}$ factors and different curvature coefficient ratios, critical for NCG applications.

4. **Heat kernel on Lie groups**: Explicit computation via Peter-Weyl decomposition; the asymptotic expansion can be extracted from character formulas.

5. **Index theorem**: The analytic index is the residue at $s = 0$ of the spectral zeta function, computed via heat kernel.

6. **Functional determinants**: $\det(\Delta) = \exp(-\zeta'(0))$ can be computed from the heat kernel expansion.

---

## Impact and Legacy

Gilkey's monograph became THE reference for spectral geometry and index theory. Its impact includes:

- **NCG and spectral action**: Connes' spectral action principle is built on heat kernel expansions. The Seeley-DeWitt coefficients are the coefficients in the spectral action.
- **Quantum field theory on curved space**: The effective action in curved spacetime uses heat kernels to compute one-loop contributions.
- **Quantum cosmology**: Vilenkin and others use heat kernel zeta functions for the functional integral in cosmological models.
- **M-theory and string theory**: Heat kernel computations appear in moduli space integrals and partition function calculations.

Gilkey's monograph has over 10,000 citations and remains the standard reference.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: CRITICAL**

The spectral action principle in phonon-exflation is:

$$S_{\text{spec}} = \text{Tr}(f(D/\Lambda)) + \ldots$$

where $D$ is the Dirac operator on M4 x SU(3) and $f$ is a test function. The heat kernel expansion of this trace is:

$$S_{\text{spec}} = \int d^4 x \left[ a_0 + a_2 R + a_4(R^2, \text{Ric}^2, \text{Rm}^2) + \ldots \right]$$

The phonon-exflation Sessions 20a and 24a both computed Seeley-DeWitt coefficients $a_2$ and $a_4$ for the Jensen-deformed SU(3) metric. The coefficient $a_4$ was found to be 1000x larger than $a_2$ at $\tau = 0$, which explains the dominance of the quadratic curvature term in the effective potential.

Moreover, Gilkey's formulas allow one to:

1. Understand why the Starobinsky R^2 inflation fails on positively curved compact manifolds (the a_4 term dominates).
2. Compute the functional determinant of the Dirac operator (relevant for the fermionic measure in the path integral).
3. Extract geometric information from the spectrum (inverse spectral problem, fundamental in "can one hear the shape of a drum").

**Session 31Aa relevance**: The BA-31-2 computation (heat kernel coefficients under SU(3) deformation) is a direct application of Gilkey's formulas.

