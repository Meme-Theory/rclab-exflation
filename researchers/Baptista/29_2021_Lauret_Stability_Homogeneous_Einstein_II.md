# On the Stability of Homogeneous Einstein Manifolds II

**Author(s):** Jorge Lauret and Cynthia Will
**Year:** 2021 (revised 2022)
**Journal:** [Not stated in PDF]
**arXiv:** 2107.00354
**Relevance:** CRITICAL (Explicit Lichnerowicz Laplacian computation for generalized Wallach spaces and flag manifolds; direct framework input)

---

## Abstract

For any G-invariant metric on a compact homogeneous space M = G/K, we give a formula for the Lichnerowicz Laplacian restricted to the space of all G-invariant symmetric 2-tensors in terms of the structural constants of G/K. As an application, we compute the G-invariant spectrum of the Lichnerowicz Laplacian for all the Einstein metrics on most generalized Wallach spaces and any flag manifold with b_2(M) = 1. This allows to deduce the G-stability and critical point types of each of such Einstein metrics as a critical point of the scalar curvature functional.

---

## Key Arguments and Derivations

### 1. General Formula for L_p (Section 3, Theorem 3.1)

The paper extends Part I by giving an explicit formula for the Lichnerowicz Laplacian L_p in terms of structural constants for **any** G-invariant metric (not just naturally reductive). For p = p_1 + ... + p_r with Ad(H)-irreducible pairwise inequivalent summands and metric g = (x_1, ..., x_r):

**Theorem 3.1:**
[L_p]_{kk} = (1/d_k) sum_{i,j != k} (x_k / x_i x_j) [ijk] + (1/d_k) sum_{i != k} (x_i / x_k^2) [ikk]

[L_p]_{km} = (1/sqrt{d_k d_m}) sum_i ((x_i^2 - x_k^2 - x_m^2) / (x_i x_k x_m)) [ikm]    (k != m)

This generalizes the naturally reductive case from Part I where all metric coefficients x_i are equal.

### 2. Ricci Curvature and Einstein Equations (Section 2.5)

The Ricci operator eigenvalues on each irreducible summand p_k are:

lambda_k = b_k/(2x_k) - (1/4d_k) sum_{i,j} ((x_i^2 + x_j^2 - x_k^2)/(x_i x_j x_k)) [ijk]

and the Einstein equations are lambda_k = rho for all k = 1,...,r.

### 3. Scalar Curvature (Section 2.6)

Sc(g) = (1/2) sum_k (b_k d_k / x_k) - (1/4) sum_{i,j,k} (x_k / x_i x_j) [ijk]

The volume-normalized scalar curvature Sc_N(g) = (det_Q g)^{1/n} Sc(g) is a homothety invariant.

### 4. Generalized Wallach Spaces (Section 4)

Generalized Wallach spaces G/K with G simple have isotropy decomposition p = p_1 + p_2 + p_3 with dim M_1^G = 2 (after scaling). The paper computes L_p for all Einstein metrics on:

**5 infinite families:**
- SU(n)/S(U(a)U(b)U(c)), a+b+c = n
- SO(a+b+c)/SO(a)SO(b)SO(c)
- Sp(a+b+c)/Sp(a)Sp(b)Sp(c)
- SU(2n)/Sp(n)
- SU(n)/SO(n)

**10 exceptional examples** including E_6/SU(3)^3, E_7/SU(3)A_5, E_8/A_7A_1, etc.

**Key findings:**
- The only local maxima of Sc|_{M_1^G} are the standard metrics on SU(2), E_7/SO(8), and E_8/Spin(8)xSpin(8), plus the Kahler metrics on flag manifolds with b_2(M) = 1.
- Any standard Einstein metric on a generalized Wallach space is either a local maximum or a local minimum.
- A generalized Wallach space admits a local minimum if and only if it admits four Einstein metrics.

### 5. Flag Manifolds with b_2(M) = 1 (Section 5)

Thirteen exceptional flag manifolds with b_2(M) = 1, each admitting between 3 and 6 Einstein metrics. All non-Kahler Einstein metrics are saddle points of coindex 1, except for three metrics on E_8 quotients which have coindex 2.

### 6. Full Flag SU(n)/T Example (Example 3.6)

For the full flag manifold SU(n)/T (diagonal maximal torus), the L_p matrix is:

[L_p] = (1/2n) (2(n-2)I - Adj(X))

where X = J(n,2,1) is the Johnson graph. The spectrum of Adj(X) is {2(n-2), n-4, -2} with multiplicities 1, n-1, n(n-3)/2.

**Result:** The standard metric on SU(n)/T is always G-unstable with coindex n-1. It is a local minimum for n=3, G-degenerate for n=4, and a saddle point for n >= 5.

### 7. Prescribed Ricci Curvature Problem (Section 4.4)

For each Kahler-Einstein metric on generalized Wallach spaces that are flag manifolds, the kernel of Delta_L|_{TT_g^G} is non-trivial. This implies failure of either existence or local uniqueness for the prescribed Ricci curvature problem Rc(g') = cT near these metrics.

---

## Key Results

1. **Theorem 3.1**: Universal formula for L_p matrix entries in terms of structural constants [ijk] and metric coefficients x_i, valid for any G-invariant metric (not just naturally reductive).

2. **All Einstein metrics are G-non-degenerate** on generalized Wallach spaces and flag manifolds with b_2(M) = 1 (hence G-rigid).

3. **Local maxima classification**: Only standard metrics on SU(2), E_7/SO(8), E_8/Spin(8)^2, and Kahler metrics on 13 flag manifolds are G-stable.

4. **SU(n)/T standard metric**: G-unstable with coindex n-1 for all n >= 3. Local minimum for SU(3)/T^2.

5. **Kahler-Einstein Lichnerowicz kernel**: Non-trivial on all Kahler-Einstein metrics of Wallach-type flag manifolds, obstructing prescribed Ricci problem.

6. **Black hole instability criterion** (Remark 1.3): The Einstein-Kahler metric on SU(3)/S(U(1)^3) is the only metric studied satisfying Lambda_L^G < (9 - n)/4, giving an unstable 8-dimensional generalized Schwarzschild black hole.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| L_p diagonal | $[L_p]_{kk} = \frac{1}{d_k}\sum_{i,j\neq k}\frac{x_k}{x_i x_j}[ijk] + \frac{1}{d_k}\sum_{i\neq k}\frac{x_i}{x_k^2}[ikk]$ | Thm 3.1 |
| L_p off-diagonal | $[L_p]_{km} = \frac{1}{\sqrt{d_k d_m}}\sum_i \frac{x_i^2 - x_k^2 - x_m^2}{x_i x_k x_m}[ikm]$ | Thm 3.1 |
| Ricci eigenvalue | $\lambda_k = \frac{b_k}{2x_k} - \frac{1}{4d_k}\sum_{i,j}\frac{x_i^2+x_j^2-x_k^2}{x_i x_j x_k}[ijk]$ | Eq. (18) |
| Einstein equation | $\lambda_k = \rho$ for all $k = 1, \ldots, r$ | Sec. 2.5 |
| Scalar curvature | $\mathrm{Sc}(g) = \frac{1}{2}\sum_k \frac{b_k d_k}{x_k} - \frac{1}{4}\sum_{i,j,k}\frac{x_k}{x_i x_j}[ijk]$ | Eq. (19) |
| Structural constants | $[ijk] = \sum_{\alpha,\beta,\gamma} Q([e^i_\alpha, e^j_\beta], e^k_\gamma)^2$ | Eq. (14) |
| Volume-normalized Sc | $\mathrm{Sc}_N(g) = (x_1^{d_1}\cdots x_r^{d_r})^{1/n}\,\mathrm{Sc}(g)$ | Eq. (20) |
| Moment map | $\langle M_{\mu_p}, A\rangle = \frac{1}{4}\langle\theta(A)\mu_p, \mu_p\rangle$ | Eq. (7) |
| L_p definition | $\langle L_p A, B\rangle = \frac{1}{2}\langle\theta(A)\mu_p, \theta(B)\mu_p\rangle + 2\,\mathrm{tr}(M_{\mu_p}AB)$ | Eq. (12) |
| SU(n)/T spectrum | $\lambda_p = 1/2$, $\lambda_p^{\max} = (n-1)/n$ for $n \geq 4$ | Example 3.6 |

---

## Relevance to Phonon-Exflation

This paper is **directly computational** for the framework's internal geometry:

1. **SU(3)/T^2 = full flag manifold**: The standard metric on SU(3)/T^2 has Lambda_p = Lambda_p^max = 1/2, is G-unstable with coindex 2, and is a **local minimum** of Sc. This is the full flag manifold that arises when SU(3) is maximally broken. The fact that it is a local minimum (not maximum) means the scalar curvature functional drives the Ricci flow away from this configuration.

2. **Theorem 3.1 as computational tool**: The formula gives the exact L_p matrix for any metric g = (x_1, ..., x_r) on SU(3)/K quotients in terms of the structural constants [ijk]. This can be directly evaluated numerically for the Jensen deformation family parameterized by tau, giving the full Lichnerowicz spectrum as a function of the deformation parameter.

3. **Black hole instability criterion**: The connection to Freund-Rubin compactification stability (Remark 1.3) is directly relevant to the M4 x SU(3) Kaluza-Klein setting. The instability criterion Lambda_L < (9 - n)/4 applies to the AdS stability analysis of the framework's compactification.

4. **Kahler-Einstein obstructions**: The non-trivial Lichnerowicz kernel on Kahler-Einstein metrics of flag manifolds constrains which geometric configurations can serve as rigid endpoints for the compactification.
