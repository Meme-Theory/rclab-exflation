# One-Loop Corrections to the Spectral Action

**Author(s):** Teun D.H. van Nuland and Walter D. van Suijlekom
**Year:** 2021 (published 2022)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2107.08485
**Relevance:** HIGH

---

## Abstract

We analyze the perturbative quantization of the spectral action in noncommutative geometry and establish its one-loop renormalizability in a generalized sense, while staying within the spectral framework of noncommutative geometry. Our result is based on the perturbative expansion of the spectral action in terms of higher Yang-Mills and Chern-Simons forms. In the spirit of random noncommutative geometries, we consider the path integral over matrix fluctuations around a fixed noncommutative gauge background and show that the corresponding one-loop counterterms are of the same form so that they can be safely subtracted from the spectral action. A crucial role will be played by the appropriate Ward identities, allowing for a fully spectral formulation of the quantum theory at one loop.

---

## Key Arguments and Derivations

**Diagrammatic expansion of spectral action.** The spectral action $\text{Tr}\, f(D)$ for perturbations $D \to D + V$ with gauge fields $V = a_j[D, b_j]$ is expanded as $S_D[V] = \sum_{n=1}^{\infty} \frac{1}{n} \langle V, \ldots, V \rangle$, where the brackets are contour integrals representable as loop Feynman diagrams. Two key properties: cyclicity $\langle V_1, \ldots, V_n \rangle = \langle V_n, V_1, \ldots, V_{n-1} \rangle$ and the Ward identity $(z-D)^{-1}a - a(z-D)^{-1} = (z-D)^{-1}[D,a](z-D)^{-1}$.

**Yang-Mills-Chern-Simons structure.** By introducing the universal gauge form $A = a_j db_j$, curvature $F = dA + A^2$, and noncommutative integrals $\int_{\phi_n}$ and $\int_{\psi_{2k-1}}$, the spectral action expansion takes the form:
$$S_D[V] = \sum_{k=1}^{\infty} \left( \int_{\psi_{2k-1}} \text{cs}_{2k-1}(A) + \frac{1}{2k} \int_{\phi_{2k}} F^k \right)$$
with higher Chern-Simons forms $\text{cs}_{2k-1}(A) := \int_0^1 A(tdA + t^2 A^2)^{k-1} dt$.

**Background field method.** For quantization, the path integral is over all finite-size hermitian matrices (random NCG), with the divided difference propagator $G_{kl} = 1/f'[\lambda_k, \lambda_l]$. The inverse propagator $f'[\lambda_k, \lambda_l]$ is bounded (in contrast to ordinary QFT), reflecting the regularizing nature of the spectral action.

**One-loop two-point functions.** Three two-point graphs at one loop are computed. The first (two separate vertices) has no running loop index and remains finite as $N \to \infty$. The second and third are potentially divergent and require subtraction. The quantum Ward identity for the gauge propagator is proven diagrammatically.

**One-loop renormalizability.** The divergent part of the one-loop quantum effective spectral action has exactly the same Yang-Mills-Chern-Simons form as the classical action:
$$\sum_n \frac{1}{n} \langle\langle V, \ldots, V \rangle\rangle^{1L}_\infty = \sum_{k=1}^{\infty} \left( \int_{\tilde{\psi}_{2k-1}} \text{cs}_{2k-1}(A) + \frac{1}{2k} \int_{\tilde{\phi}_{2k}} F^k \right)$$
Renormalization is achieved by the transformation $\phi \mapsto \phi - \tilde{\phi}$, $\psi \mapsto \psi - \tilde{\psi}$ in the space of noncommutative integrals. This establishes one-loop renormalizability in the generalized sense of Gomis-Weinberg.

## Key Results

1. The spectral action admits a perturbative expansion in terms of higher Yang-Mills and Chern-Simons forms (Eq. 7)
2. One-loop renormalizability of the spectral action is established within the spectral framework
3. Ward identities hold for both the fermion propagator (Eq. 3) and the gauge propagator (Eq. 9)
4. The gauge propagator $G_{kl} = 1/f'[\lambda_k, \lambda_l]$ is bounded, unlike ordinary QFT
5. One-loop counterterms have the same Yang-Mills-Chern-Simons form as the classical action
6. The first two-point diagram (separate vertices) is finite -- no running loop index

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Spectral action | $\text{Tr}\, f(D) = \sum_k f(\lambda_k)$ | Sec. 2 |
| Perturbative expansion | $S_D[V] = \sum_{n=1}^{\infty} \frac{1}{n} \langle V, \ldots, V \rangle$ | Eq. (1) |
| Bracket (contour integral) | $\langle V_1, \ldots, V_n \rangle = \text{Tr} \oint \frac{dz}{2\pi i} f'(z) V_1(z-D)^{-1} \cdots V_n(z-D)^{-1}$ | Sec. 2 |
| Ward identity | $(z-D)^{-1}a - a(z-D)^{-1} = (z-D)^{-1}[D,a](z-D)^{-1}$ | Eq. (3) |
| NC integral | $\int_{\phi_n} a_0 da_1 \cdots da_n$ (defined via loop diagrams with $[D, a_j]$ insertions) | Eq. (4) |
| YM-CS expansion | $S_D[V] = \sum_{k=1}^{\infty} \left(\int_{\psi_{2k-1}} \text{cs}_{2k-1}(A) + \frac{1}{2k}\int_{\phi_{2k}} F^k\right)$ | Eq. (7) |
| Higher Chern-Simons | $\text{cs}_{2k-1}(A) := \int_0^1 A(tdA + t^2 A^2)^{k-1} dt$ | Eq. (8) |
| Gauge propagator | $G_{kl} = 1/f'[\lambda_k, \lambda_l]$ | Sec. 3 |
| Two-point amplitude | $\sum_{i,j,k} (V_1)_{ij}(V_2)_{ji} G_{ik} G_{kj} f'[\lambda_i, \lambda_j, \lambda_k]^2$ | Eq. (11) |
| Quantum Ward identity | $\langle\langle V_1, \ldots, aV_j, \ldots, V_n \rangle\rangle - \langle\langle V_1, \ldots, V_{j-1}a, \ldots, V_n \rangle\rangle = \langle\langle V_1, \ldots, [D,a], V_j, \ldots, V_n \rangle\rangle$ | Sec. 3.3 |

## Relevance to Phonon-Exflation

This is a foundational paper for the project. The one-loop renormalizability of the spectral action within the NCG framework validates the use of the spectral action as a quantum effective action, not just a bare classical action. The bounded gauge propagator $G_{kl} = 1/f'[\lambda_k, \lambda_l]$ is directly relevant to the regularizing properties observed in the project's spectral action computations. The Yang-Mills-Chern-Simons structure of the expansion connects to the project's analysis of the spectral action on the M4 x SU(3) product geometry, and the Ward identities underpin the gauge invariance that protects the framework's predictions at quantum level. The result that spectral renormalization stays within the spectral framework (rather than requiring external RG methods) supports the coherence of the NCG approach to particle physics adopted by the project.
