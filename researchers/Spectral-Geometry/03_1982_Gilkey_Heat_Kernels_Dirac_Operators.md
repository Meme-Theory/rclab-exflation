# Heat Kernels for Dirac Operators on Riemannian Manifolds

**Author(s):** Peter B. Gilkey

**Year:** 1982

**Journal:** Advances in Mathematics, Vol. 45, pp. 35-78

---

## Abstract

Gilkey extends his heat kernel theory specifically to Dirac operators on spin manifolds. The key results are explicit formulas for the Seeley-DeWitt coefficients a_k for twisted Dirac operators, detailed analysis of the spinor heat kernel structure, and applications to index theory and quantum field theory on curved space. This paper is essential for understanding how spectral action principles work for fermions.

---

## Historical Context

While the heat kernel theory for scalar Laplacians was well-developed by 1975, the case of Dirac operators presented new subtleties:

1. Dirac eigenvalues come in $\pm \lambda$ pairs (for chiral structures without anomaly).
2. The spinor representation is larger than the scalar representation by a factor $2^{n/2}$.
3. The curvature coupling is more intricate because of the spin structure.

Gilkey's 1982 paper provided the definitive treatment, giving explicit a_k formulas and showing how to compute functional determinants of Dirac operators—critical for one-loop quantum field theory on curved space.

This work also motivated later papers by Branson, Ørsted, and others on the differential geometry of Dirac operators.

---

## Key Arguments and Derivations

### Spinor Heat Kernel Setup

On a compact spin manifold $(M, g)$ of dimension $n$, the Dirac operator is:

$$D = \gamma^\mu \nabla_\mu = \gamma^\mu (\partial_\mu + \omega_\mu)$$

where $\gamma^\mu$ are Clifford algebra generators satisfying:

$$\{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}$$

and $\omega_\mu$ is the spin connection:

$$\omega_\mu = \frac{1}{4} \omega_{\mu,ab} \sigma^{ab}$$

with $\sigma^{ab} = \frac{1}{2}[\gamma^a, \gamma^b]$.

The heat kernel for the Dirac Laplacian $D^2$ is:

$$K_t^{(D)}(x, y) : \Sigma_x \to \Sigma_y$$

where $\Sigma$ is the spinor bundle, and the heat equation is:

$$\frac{\partial K_t^{(D)}}{\partial t} + D^2 K_t^{(D)} = 0, \quad K_0^{(D)} = \delta(x - y) \otimes \text{id}_{\Sigma}$$

### Seeley-DeWitt Coefficients for Dirac

The trace of the spinor heat kernel expands as:

$$\text{Tr}(e^{-tD^2}) = \int_M K_t^{(D)}(x,x) \, dV_x = (4\pi t)^{-n/2} \sum_{k=0}^{\infty} a_k^{(D)} t^{(k-n)/2}$$

**Coefficient $a_0^{(D)}$**: Spinor dimension factor.

$$a_0^{(D)} = 2^{n/2} \cdot \text{rank}(\Sigma) = 2^{n/2}$$

This is the total number of spin components (e.g., for $n = 4$, we have $2^4 = 16$ Dirac components in 4D).

**Coefficient $a_2^{(D)}$**: Ricci curvature coupling.

$$a_2^{(D)} = -\frac{n}{6} \int_M R \, dV = -\frac{n}{6} \int_M R_{\mu\nu} g^{\mu\nu} \, dV$$

For $n = 4$: $a_2^{(D)} = -\frac{2}{3} \int_M R \, dV$.

Note the negative sign (opposite to scalars) and the factor $n/6$. This reflects the fact that positive Ricci curvature *raises* the Dirac eigenvalues (opposite to scalars, which are lowered).

**Coefficient $a_4^{(D)}$**: Quadratic curvature invariants.

$$a_4^{(D)} = \frac{1}{360} \int_M \left[ c_0 R^2 + c_1 R_{\mu\nu}^2 + c_2 R_{\mu\nu\rho\sigma}^2 + c_3 \Box R \right] dV$$

where the coefficients $c_i$ are:

$$c_0 = 5(n-1), \quad c_1 = -2(n+13), \quad c_2 = n+5$$

For $n = 4$:

$$c_0 = 15, \quad c_1 = -34, \quad c_2 = 9$$

### Chiral Structure and $\zeta$-Function Determinant

For even-dimensional spin manifolds, the Dirac operator has a natural $\mathbb{Z}_2$ grading: $D = \begin{pmatrix} 0 & D_- \\ D_+ & 0 \end{pmatrix}$.

The two halves $D_\pm$ are called the **chiral halves**. The spectrum comes in pairs $(\lambda, -\lambda)$ except for zero modes.

The functional determinant of $D^2$ is related to the spectral zeta function:

$$\det(D^2) = \exp(-\zeta_{D^2}'(0))$$

This can be computed from the heat kernel:

$$\zeta_{D^2}(s) = \frac{1}{\Gamma(s)} \int_0^\infty t^{s-1} \left[ \text{Tr}(e^{-tD^2}) - \text{# of zero modes} \right] dt$$

### Spin Connection Curvature

The spin connection two-form is $\Omega_\mu{}^\nu = d\omega^\mu{}_\nu + \omega^\mu{}_\rho \wedge \omega^\rho{}_\nu$, and it relates to the Riemann curvature.

For the spinor heat kernel, the coupling of the Dirac operator to curvature is through the spin curvature $R^{\mu\nu} = \frac{1}{4}R^{\mu\nu}{}_{ab}\sigma^{ab}$.

The commutator relation:

$$[D, R^{\mu\nu}] = \text{curvature contributions to spin structure}$$

feeds into the a_k coefficients.

### Heat Kernel Expansion for Twisted Dirac

If the Dirac operator is coupled to a gauge field (or, more generally, twisted by a vector bundle connection), the heat kernel expansion generalizes:

$$D_A = D + A$$

where $A$ is a zero-th order operator (e.g., curvature from an internal bundle connection). Then:

$$a_2^{(D_A)} = a_2^{(D)} + \text{Tr}(A)$$

$$a_4^{(D_A)} = a_4^{(D)} + \text{Tr}([D, A]^2) + \ldots$$

This is crucial for noncommutative geometry: the Dirac operator $D_K$ on M4 x SU(3) is twisted by the geometry of the internal space, and the a_k coefficients pick up contributions from both the external (M4) and internal (SU(3)) curvatures.

### Spectral Asymptotics for Spinors

From the heat kernel, one derives the eigenvalue asymptotics. For a spin manifold of dimension $n$, the number of eigenvalues $|\lambda|$ less than $\Lambda$ satisfies:

$$N(\Lambda) = 2^{n/2} \frac{\text{Vol}(M)}{(4\pi)^{n/2} \Gamma(n/2 + 1)} \Lambda^{n/2} + O(\Lambda^{(n-1)/2})$$

The factor $2^{n/2}$ reflects the spinor dimension. For $n = 4$, this is a factor of 16.

### Index Formula via Heat Kernel

For the chiral Dirac operator $D_+$ on an even-dimensional spin manifold, the analytical index is:

$$\text{ind}(D_+) = \text{dim}(\ker D_+) - \text{dim}(\ker D_-) = \int_M \hat{A}(M) \cdot \text{ch}(E)$$

where $\hat{A}(M)$ is the A-genus and $\text{ch}(E)$ is the Chern character of the coupling bundle.

The heat kernel trace formula recovers this:

$$\text{ind}(D_+) = \lim_{\epsilon \to 0^+} \text{Tr}\left( e^{-\epsilon D_+^* D_+} - e^{-\epsilon D_+ D_+^*} \right)$$

---

## Key Results

1. **Spinor $a_0$ factor**: $2^{n/2}$ always, independent of metric or curvature.

2. **Dirac $a_2$ negative**: Positive Ricci curvature raises Dirac eigenvalues (opposite to scalars).

3. **$a_4$ for Dirac**: Explicit formula with dimension-dependent coefficients. At $n=4$: $c_0=15, c_1=-34, c_2=9$.

4. **Functional determinant**: $\det(D^2) = \exp(-\zeta_{D^2}'(0))$ computed from heat kernel residues.

5. **Spectral dimension**: The Hausdorff dimension of the spectrum is $n$ (the dimension of the manifold), controlled by $a_0$.

6. **Index from zero modes**: The analytical index of $D_+$ is the number of zero modes modulo the winding of the eigenvalue density.

---

## Impact and Legacy

This paper established the definitive framework for Dirac operator heat kernels and has been cited extensively in:

- **Quantum field theory on curved space** (Birrell-Davies, Wald)
- **One-loop effective actions** (Weinberg, Hawking)
- **Noncommutative geometry** (Connes, spectral action computations)
- **Supergravity and string theory** (Dirac operator on Calabi-Yau, etc.)
- **Mathematical physics** (Yang-Mills functional integrals, Donaldson theory)

Gilkey's results are standard in quantum field theory courses.

---

## Connection to Phonon-Exflation Framework

**Relevance: CRITICAL for NCG spectral action**

The entire phonon-exflation framework depends on the spectral action principle applied to the Dirac operator $D_K$ on M4 x SU(3). The spectral action is:

$$S_{\text{spec}} = \text{Tr}(f(D_K / \Lambda))$$

where $f$ is a cutoff function and $\Lambda$ is a scale. The expansion in powers of curvature is:

$$S_{\text{spec}} = \int d^4x \left[ a_0^{(D)} + a_2^{(D)} R + a_4^{(D)} (\text{curvature}^2 \text{ terms}) + \ldots \right]$$

The key insights from Gilkey's paper applied to phonon-exflation:

1. **Spinor dimension in M4**: $a_0^{(D)} = 2^4 = 16$ in 4D, which accounts for the 16-component Dirac spinor in M4. Session 7 confirmed that the full quantum numbers of the Standard Model emerge from $C^{16}$, the rank-16 spinor bundle.

2. **Ricci coupling**: The $a_2$ coefficient (negative sign, $-n/6$ factor) means that the compact space SU(3) with its Ricci geometry directly affects the effective mass of particles in M4.

3. **Quadratic curvature dominance**: The $a_4$ coefficient in Sessions 20a and 24a was found to be 1000x larger than $a_2$ at $\tau = 0$ on Jensen-deformed SU(3). Gilkey's dimensional analysis explains why: the $R^2$ term in $a_4$ picks up powers of the inverse scale of SU(3), making it large.

4. **Functional determinant of fermions**: The path integral measure for fermions is $\sqrt{\det(D_K D_K^\dagger)}$, computed via $\exp(-\zeta_{D_K}(0)/2)$. This is essential for computing the one-loop fermion contribution to the effective action.

5. **Index theorem on the product**: $M4 \times SU(3)$ is a spin manifold, so the index of $D_K$ restricted to M4 is the product of indices: $\text{ind}(D_K|_{M4}) = 3 \times \text{ind}(D_K|_{SU(3)})$ (three families from three colors of quarks). This is a direct application of Gilkey's index formula.

**Session 31 relevance**: All heat kernel coefficients (BA-31-2, BA-31-3) use Gilkey's formulas directly. The return probability (BA-31-1) uses spinor asymptotics from this paper.

