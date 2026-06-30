# Approximating L2 Invariants of Amenable Covering Spaces: A Heat Kernel Approach

**Author(s):** Jozef Dodziuk, Varghese Mathai
**Year:** 1996
**Journal:** arXiv preprint (dg-ga)
**arXiv:** dg-ga/9609002
**Relevance:** MEDIUM

---

## Abstract

In this paper, we prove that the L2 Betti numbers of an amenable covering space can be approximated by the average Betti numbers of a regular exhaustion, under some hypotheses. We also prove that some L2 spectral invariants can be approximated by the corresponding average spectral invariants of a regular exhaustion. The main tool which is used is a generalisation of the "principle of not feeling the boundary" (due to M. Kac), for heat kernels associated to boundary value problems.

---

## Key Arguments and Derivations

### 1. Setting

Let $(M, g)$ be a compact Riemannian manifold and $\Gamma \to \tilde{M} \to M$ be a Galois covering space. The covering is amenable if Cheeger's isoperimetric constant $h(\tilde{M}, g) = \inf\{\text{vol}_{n-1}(\partial D)/\text{vol}_n(D)\} = 0$. Examples of amenable groups include abelian, nilpotent, solvable groups, groups of subexponential growth, and their extensions.

A regular exhaustion $\{D_k\}$ of $\tilde{M}$ satisfies: (1) $\text{vol}(\partial_\delta D_k)/\text{vol}(D_k) \to 0$, (2) uniformly bounded second fundamental forms, (3) uniformly collared boundaries.

### 2. Main Results

**Theorem 0.1**: For an amenable covering with regular exhaustion:
$$\limsup_{k\to\infty} \frac{\text{vol}(M)}{\text{vol}(D_k)} b_j(D_k, \partial D_k) \leq b_j^{(2)}(\tilde{M}, \Gamma)$$
and the same with absolute Betti numbers. Equality holds when $b_j^{(2)}(\tilde{M}, \Gamma) = 0$.

**Conjecture**: Equality always holds (proved in dimensions 2, 3, 4 under mild hypotheses in Theorem 0.2).

### 3. Heat Kernel Method

The key technique is the "principle of not feeling the boundary": the heat kernel on $D_k$ (with Dirichlet or Neumann conditions) converges to the heat kernel on $\tilde{M}$ uniformly on compact subsets as $k \to \infty$. This is a generalization of Kac's principle to the covering space setting.

The heat trace on $D_k$ with boundary conditions $B$ satisfies:
$$\text{Tr}(e^{-t\Delta_j^B(D_k)}) = \sum_\lambda e^{-t\lambda} \cdot m_\lambda$$
and the averaged trace converges to the von Neumann trace on $\tilde{M}$.

### 4. Spectral Invariants

More generally, for spectral functions $F(\Delta)$, the averaged versions on exhaustions approximate the $L^2$ versions. This includes not just Betti numbers but also torsion and eta invariants.

---

## Key Results

1. $L^2$ Betti numbers of amenable coverings are approximated from above by averaged Betti numbers of regular exhaustions (Theorem 0.1)
2. Conjecture of exact equality, proved in dimensions $\leq 4$ (Theorem 0.2)
3. Generalization of Kac's "not feeling the boundary" principle to Galois coverings
4. Approximation extends to general spectral invariants, not just Betti numbers
5. Alternating sum version gives exact equality for the Euler characteristic

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Cheeger constant | $h(\tilde{M},g) = \inf\left\{\frac{\text{vol}_{n-1}(\partial D)}{\text{vol}_n(D)}\right\}$ | Introduction |
| Betti approximation | $\limsup \frac{\text{vol}(M)}{\text{vol}(D_k)} b_j(D_k, \partial D_k) \leq b_j^{(2)}(\tilde{M}, \Gamma)$ | Thm 0.1(a) |
| Euler equality | $\sum_{j=0}^n (-1)^{n-j} b_j(D_k)/\text{vol}(D_k) \to \sum (-1)^{n-j} b_j^{(2)}$ | Thm 0.1(b) |
| Regular exhaustion | $\lim_{k\to\infty} \text{vol}(\partial_\delta D_k)/\text{vol}(D_k) = 0$ | Eq. (0.1) |
| Heat kernel principle | $\|e^{-t\Delta(D_k)} - e^{-t\Delta(\tilde{M})}\|_{\text{loc}} \to 0$ | Section 1 |

---

## Relevance to Phonon-Exflation

This paper is relevant to the framework's treatment of the spatially extended SU(3) fabric. The "principle of not feeling the boundary" for heat kernels is the mathematical justification for computing spectral invariants on finite approximations to the full M4 x SU(3) geometry and expecting convergence to the true values. The $L^2$ Betti number approximation scheme is the rigorous version of the intuition that local spectral data on a large domain approximates global spectral data. The amenability condition (Cheeger constant = 0) is automatically satisfied for compact Lie groups like SU(3).
