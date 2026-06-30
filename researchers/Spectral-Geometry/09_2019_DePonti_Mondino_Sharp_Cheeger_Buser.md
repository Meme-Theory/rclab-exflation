# Sharp Cheeger-Buser Type Inequalities in RCD(K, infinity) Spaces

**Author(s):** Nicolo De Ponti, Andrea Mondino
**Year:** 2019
**Journal:** arXiv preprint (math.FA)
**arXiv:** 1902.03835
**Relevance:** MEDIUM

---

## Abstract

The goal of the paper is to sharpen and generalise bounds involving Cheeger's isoperimetric constant $h$ and the first eigenvalue $\lambda_1$ of the Laplacian. A celebrated lower bound of $\lambda_1$ in terms of $h$, $\lambda_1 \geq h^2/4$, was proved by Cheeger in 1970 for smooth Riemannian manifolds. An upper bound on $\lambda_1$ in terms of $h$ was established by Buser in 1982 (with dimensional constants) and improved (to a dimension-free estimate) by Ledoux in 2004 for smooth Riemannian manifolds with Ricci curvature bounded below. The goal of the paper is twofold. First: we sharpen the inequalities obtained by Buser and Ledoux obtaining a dimension-free sharp Buser inequality for spaces with (Bakry-Emery weighted) Ricci curvature bounded below by $K \in \mathbb{R}$ (the inequality is sharp for $K > 0$ as equality is obtained on the Gaussian space). Second: all of our results hold in the higher generality of (possibly non-smooth) metric measure spaces with Ricci curvature bounded below in synthetic sense, the so-called RCD(K, infinity) spaces.

---

## Key Arguments and Derivations

### 1. Setting: Metric Measure Spaces and Cheeger Constant

The paper works on complete metric measure spaces $(X, d, m)$. The first eigenvalue is defined variationally:
$$\lambda_1 = \inf\left\{\frac{\int_X |\nabla f|^2\,dm}{\int_X |f|^2\,dm} : 0 \not\equiv f \in \text{Lip}_b(X),\, \int_X f\,dm = 0\right\}$$

The Cheeger constant is $h(X) = \inf\{\text{Per}(A)/m(A) : m(A) \leq m(X)/2\}$.

### 2. Classical Results

- **Cheeger (1970)**: $\lambda_1 \geq \frac{1}{4}h(X)^2$ (sharp constant)
- **Buser (1982)**: $\lambda_1 \leq 2\sqrt{-(n-1)K}\,h + 10h^2$ for $\text{Ric} \geq K \leq 0$ (dimension-dependent)
- **Ledoux (2004)**: $\lambda_1 \leq \max\{6\sqrt{-K}\,h, 36h^2\}$ (dimension-free)

### 3. Main Results

**Theorem 1.1** (Sharp implicit Buser inequality for RCD(K, infinity) spaces): Using the function
$$J_K(t) = \begin{cases}\sqrt{2/(\pi K)}\arctan\sqrt{e^{2Kt}-1} & K > 0 \\ (2/\sqrt{\pi})\sqrt{t} & K = 0 \\ \sqrt{-2/(\pi K)}\text{arctanh}\sqrt{1-e^{2Kt}} & K < 0\end{cases}$$
the Cheeger constant satisfies $h(X) \geq \sup_{t>0} J_K(t)^{-1}(1 - e^{-\lambda_1 t})$ (for $m(X) = 1$).

**Corollary 1.2**: For RCD(K, infinity) with $K \leq 0$:
$$\lambda_1 \leq -K + \frac{\pi}{2}h^2$$
and for $K > 0$:
$$\lambda_1 \leq K + \frac{\pi}{2}h^2$$

The constant $\pi/2$ is optimal (equality on the Gaussian space).

### 4. Key Techniques

- Heat semigroup and its regularizing properties in RCD spaces
- Bakry-Emery calculus ($\Gamma_2$ estimates)
- The Bobkov inequality and its consequences for isoperimetric profiles
- Stability under measured Gromov-Hausdorff convergence

---

## Key Results

1. Sharp dimension-free Buser inequality: $\lambda_1 \leq -K + \frac{\pi}{2}h^2$ for $K \leq 0$ (Corollary 1.2)
2. Sharp for $K > 0$: equality on Gaussian space
3. All results hold for RCD(K, infinity) metric measure spaces (non-smooth generalization)
4. Improvement over Buser's dimensional constant and Ledoux's dimension-free constant
5. Self-contained proof of Cheeger's inequality for general m.m.s. (Appendix)

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Cheeger inequality | $\lambda_1 \geq \frac{1}{4}h(X)^2$ | Eq. (5) |
| Sharp Buser ($K \leq 0$) | $\lambda_1 \leq -K + \frac{\pi}{2}h^2$ | Cor 1.2 |
| Cheeger constant | $h(X) = \inf\{\text{Per}(A)/m(A) : m(A) \leq m(X)/2\}$ | Eq. (4) |
| $\lambda_1$ variational | $\lambda_1 = \inf\frac{\int|\nabla f|^2\,dm}{\int|f|^2\,dm}$, $\int f\,dm = 0$ | Eq. (2) |
| $J_K$ function | $J_0(t) = \frac{2}{\sqrt{\pi}}\sqrt{t}$ | Eq. (8) |
| Buser (1982) | $\lambda_1 \leq 2\sqrt{-(n-1)K}\,h + 10h^2$ | Eq. (6) |
| Ledoux (2004) | $\lambda_1 \leq \max\{6\sqrt{-K}\,h, 36h^2\}$ | Eq. (7) |

---

## Relevance to Phonon-Exflation

The Cheeger-Buser inequalities relate isoperimetric geometry to spectral gaps. For the M4 x SU(3) framework, the Cheeger constant of the internal SU(3) fiber constrains the first nonzero eigenvalue of the Laplacian, which in turn bounds the spectral gap of the Dirac operator via the Lichnerowicz formula. The dimension-free nature of the sharp bound ($\pi/2$ constant) is useful because it applies regardless of how the internal geometry's effective dimension changes during the tau-transit. The RCD generalization is relevant if the internal geometry develops singularities or non-smooth features at the fold.
