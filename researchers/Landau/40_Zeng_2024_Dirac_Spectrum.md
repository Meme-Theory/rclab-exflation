# Spectrum of the Dirac Operator on Compact Riemannian Manifolds

**Author(s):** Lingzhong Zeng
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2402.14247
**Relevance:** MEDIUM

---

## Abstract

In this paper, we consider the eigenvalue problem of Dirac operator on a compact Riemannian manifold isometrically immersed into Euclidean space and derive some extrinsic estimates for the sum of arbitrary consecutive eigenvalues of the square of the Dirac operator acting on some Dirac invariant subbundles. As some applications, we deduce some eigenvalue inequalities on the compact submanifolds immersed into Euclidean space, unit sphere or projective spaces and further get some bounds of general Reilly type. In addition, we also establish some universal bounds under certain curvature condition and on the meanwhile provide an alternative proof for Anghel's result. In particular, utilizing Atiyah-Singer index theorem, we drive an upper bound estimate for the sum of the first n nontrivial eigenvalues of Atiyah-Singer Laplacian acting on the spin manifolds without dimensional assumption.

---

## Key Arguments and Derivations

### Setup: Dirac bundles and operators

Let M^n be a compact Riemannian manifold with smooth metric g, /S -> M^n a Dirac bundle, and /D the associated Dirac operator. The Bochner-Lichnerowicz-Weitzenbock formula gives:

/D^2 = nabla* nabla + R

where R is the curvature morphism acting on /S. For the spinor bundle case, R = (1/4)S where S is the scalar curvature. A Dirac invariant subbundle /E is one preserved by both nabla and R, hence by /D^2.

### Prior bounds (context)

- Friedrich (1980s): Gamma^2(/D) >= n/(4(n-1)) S_0 (lower bound from scalar curvature)
- Hijazi: Gamma^2(/D) >= n/(4(n-1)) Gamma_1(L_{M^n}) for n >= 3 (Yamabe operator bound)
- Bar (n=2): Gamma^2(/D) >= 4 pi (1-g_0)/area(M^2)
- Anghel upper bound: Gamma_{k+1} - Gamma_k <= n integral H^2 + (4/kn) sum Gamma_i - (4/kn) sum integral R
- Chen Yang-type: sum_{i=1}^k (Gamma_{k+1} - Gamma_i)^2 <= (4/n) sum (Gamma_{k+1} - Gamma_i)(Gamma_i + n^2/4 integral H^2 - integral R)

### Main theorem (Theorem 2.1)

For a compact Riemannian manifold M^n isometrically embedded in R^{n+p} with mean curvature H, the eigenvalues of /D^2 acting on a Dirac invariant subbundle /E satisfy, for any j in Z+:

sum_{k=1}^n Gamma_{j+k} <= (n+4) Gamma_j + n^2 integral_{M^n} H^2 <s_j, s_j> dv - 4 integral_{M^n} <R s_j, s_j> dv

This generalizes Chen's inequality (which was the j=1 case) to arbitrary starting eigenvalue index j. It is the Dirac operator analog of the Levitin-Parnovski inequality for the Laplacian.

### Proof strategy

The proof uses:
1. Nash embedding theorem to guarantee isometric immersion M^n -> R^{n+p}
2. Coordinate functions x_A of R^{n+p} as test functions
3. An orthogonal rotation P to construct adapted test spinors Phi_A = sum p_{AB} x_B
4. Parseval identity and Bessel inequality applied to the spectral expansion
5. The Bochner-Lichnerowicz-Weitzenbock formula to relate /D^2 to geometric quantities

Key identities used: sum |nabla x_A|^2 = n (from the immersion), sum (Delta x_A)^2 = n^2 H^2, sum Delta x_A nabla x_A = 0.

### Applications

- Submanifolds of unit sphere S^{n+1}: adds curvature contribution from ambient space
- Submanifolds of projective spaces: additional topological contributions
- Reilly-type bounds: upper bounds on eigenvalues in terms of mean curvature
- Universal bounds under curvature conditions (e.g., non-negative scalar curvature)
- Upper bound for sum of first n eigenvalues of Atiyah-Singer Laplacian on spin manifolds (no dimensional restriction)

---

## Key Results

1. For any j >= 1: sum_{k=1}^n Gamma_{j+k} <= (n+4) Gamma_j + n^2 integral H^2 <s_j, s_j> dv - 4 integral <R s_j, s_j> dv
2. When j=1, this reduces to Chen's known inequality
3. For submanifolds of R^{n+p} with S_0 = 0 and zero eigenvalue: Gamma_1 <= (n/vol(M^n)) integral H^2 dv
4. For submanifolds of S^{n+1}: Gamma_1^2 <= n^2/4 + (n^2/4 vol) integral H_tilde^2 dv
5. For submanifolds of H^{n+1}(-1): Gamma_1^2 <= (n^2/4)(inf max |H_bar|^2 - 1)
6. Universal bounds established without dimensional assumption using Atiyah-Singer index theorem

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| BLW formula | $/D^2 = \nabla^*\nabla + \mathcal{R}$ | Eq. (2.7) |
| Clifford relations | $X \cdot Y \cdot s + Y \cdot X \cdot s + 2\langle X, Y\rangle s = 0$ | Eq. (2.1) |
| Main theorem | $\sum_{k=1}^n \Gamma_{j+k} \leq (n+4)\Gamma_j + n^2\int_{M^n} H^2\langle s_j, s_j\rangle\, dv - 4\int_{M^n}\langle\mathcal{R}s_j, s_j\rangle\, dv$ | Eq. (2.26) |
| Friedrich bound | $\Gamma^2(/D) \geq \frac{n}{4(n-1)}S_0$ | Eq. (1.1) |
| Hijazi bound | $\Gamma^2(/D) \geq \frac{n}{4(n-1)}\Gamma_1(L_{M^n})$ | Eq. (1.2) |
| Anghel bound | $\bar{\Gamma}_1 \leq \frac{n}{\text{vol}(M^n)}\int_M H^2\, dv$ | Eq. (1.5) |
| Chen Yang-type | $\sum_{i=1}^k (\Gamma_{k+1}-\Gamma_i)^2 \leq \frac{4}{n}\sum_{i=1}^k (\Gamma_{k+1}-\Gamma_i)[\Gamma_i + \frac{n^2}{4}\int H^2\langle s_i,s_i\rangle - \int\langle\mathcal{R}s_i,s_i\rangle]$ | Eq. (1.11) |
| Scalar curvature | $S = n^2 H^2 - |B|^2$ | Eq. (2.13) |
| Gauss equation | $R_{ijkl} = \sum_\alpha (h^\alpha_{ik}h^\alpha_{jl} - h^\alpha_{il}h^\alpha_{jk})$ | Eq. (2.11) |
| Laplacian-Parnovski | $\lambda_{j+1} + \cdots + \lambda_{j+n} \leq (n+4)\lambda_j$ (for Laplacian on $\Omega \subset \mathbb{R}^n$) | Eq. (2.24) |

## Relevance to Phonon-Exflation

This paper provides rigorous spectral bounds for the Dirac operator on compact Riemannian manifolds, directly applicable to the framework's D_K operator on M^4 x SU(3). The main inequality (Theorem 2.1) bounds sums of consecutive eigenvalues of /D^2 in terms of the mean curvature and curvature morphism -- quantities that are tau-dependent in the framework. The Ashbaugh-Benguria-type bound sum_{k=1}^n Gamma_{j+k} <= (n+4) Gamma_j constrains how the Dirac spectrum can spread during the tau-transit, providing rigorous limits on spectral gap evolution and eigenvalue ratio phi. The extrinsic approach (using the Nash embedding into Euclidean space) may offer an alternative to the Peter-Weyl intrinsic computation currently used.
