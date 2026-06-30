# Spectral Analysis of Causal Dynamical Triangulations via Finite Element Method

**Author(s):** Fabio Caceffo, Giuseppe Clemente
**Year:** 2020 (revised 2023)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2010.07179
**Relevance:** LOW

---

## Abstract

We examine the dual graph representation of simplicial manifolds in Causal Dynamical Triangulations (CDT) as a mean to build observables, and propose a new representation based on the Finite Element Methods (FEM). In particular, with the application of FEM techniques, we extract the (low-lying) spectrum of the Laplace-Beltrami (LB) operator on the Sobolev space $H^1$ of scalar functions on piecewise flat manifolds, and compare them with corresponding results obtained by using the dual graph representation. We show that, besides for non-pathological cases in two dimensions, the dual graph spectrum and spectral dimension do not generally agree, neither quantitatively nor qualitatively, with the ones obtained from the LB operator on the continuous space.

---

## Key Arguments and Derivations

**Dual graph vs. continuous spectrum.** Previous CDT spectral studies approximated the Laplace-Beltrami spectrum using the Laplace matrix $L = (d+1)\cdot \mathbf{1} - A$ of the dual graph (where $A$ is the adjacency matrix). This paper shows that this approximation can produce significant discrepancies with the true LB spectrum, especially when simplices are not equilateral.

**Diffusion processes.** The spectral dimension is defined via the return probability $P(t) \approx t^{-d/2} \sum_n A_n t^n$, with scale-dependent dimension $d = -2 \frac{d\log P(t)}{d\log t}$. An alternative definition uses the Weyl theorem: $n(\lambda) \sim \frac{\omega_d}{(2\pi)^d} V \lambda^{d/2}$, giving effective spectral dimension $2/d_{\text{eff}} = \frac{d\log\lambda}{d\log(n/V)}$.

**FEM formulation.** The weak form of the LB eigenproblem $-\Delta f = \lambda f$ on a simplicial manifold is: $\int_M \nabla\phi \cdot \nabla f = \lambda \int_M \phi f$ for test functions $\phi \in H^1(M)$. FEM solves this in finite-dimensional subspaces $V_r$ of $H^1$ with guaranteed convergence. The method uses iterated refinement of the starting triangulation.

**Test comparisons.** On flat tori and other test geometries, FEM converges to the exact LB spectrum, while the dual graph method shows quantitative discrepancies. A pathological toy model demonstrates that dual graph methods can miss even qualitative large-scale features.

## Key Results

1. Dual graph Laplacian does not reliably approximate the LB spectrum on non-equilateral simplicial manifolds
2. FEM provides a convergent approximation to the exact LB spectrum with guaranteed convergence
3. Spectral dimensions computed via dual graph and FEM methods can disagree qualitatively
4. The dual graph method typically undershoots eigenvalues compared to the exact LB spectrum

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Heat equation | $\partial_t u(x,t) = D^\mu D_\mu u(x,t)$ | Eq. (1) |
| Return probability | $P(t) := \frac{1}{V}\int d^dx \sqrt{g}\, u(x,x,t)$ | Eq. (8) |
| Spectral dimension | $d = -2\frac{d\log P(t)}{d\log t}$ | Eq. (11) |
| Weyl's theorem | $n(\lambda) \sim \frac{\omega_d}{(2\pi)^d} V \lambda^{d/2}$ | Eq. (13) |
| Dual graph Laplacian | $-\Delta \to L = (d+1)\cdot \mathbf{1} - A$ | Eq. (20) |

## Relevance to Phonon-Exflation

This paper provides a methodological caution for the project's spectral analysis: when computing Laplace-Beltrami spectra on discretized spaces (as in CDT or lattice approaches to the M4 x SU(3) geometry), the choice of approximation method matters. The FEM approach offers a more reliable tool for extracting the low-lying spectrum that determines the spectral dimension flow. The result that dual graph methods can give qualitatively wrong spectral dimensions is relevant when interpreting CDT results on dimensional reduction ($d_S \approx 4 \to 2$).
