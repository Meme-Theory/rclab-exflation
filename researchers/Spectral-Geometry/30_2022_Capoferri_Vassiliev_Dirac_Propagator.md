# Global Propagator for the Massless Dirac Operator and Spectral Asymptotics

**Author(s):** Matteo Capoferri, Dmitri Vassiliev
**Year:** 2020 (revised 2022)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2004.06351
**Relevance:** LOW

---

## Abstract

We construct the propagator of the massless Dirac operator $W$ on a closed Riemannian 3-manifold as the sum of two invariantly defined oscillatory integrals, global in space and in time, with distinguished complex-valued phase functions. The two oscillatory integrals -- the positive and the negative propagators -- correspond to positive and negative eigenvalues of $W$, respectively. This enables us to provide a global invariant definition of the full symbols of the propagators (scalar matrix-functions on the cotangent bundle), a closed formula for the principal symbols and an algorithm for the explicit calculation of all their homogeneous components. Furthermore, we obtain small time expansions for principal and subprincipal symbols of the propagators in terms of geometric invariants. Lastly, we use our results to compute the third local Weyl coefficients in the asymptotic expansion of the eigenvalue counting functions of $W$.

---

## Key Arguments and Derivations

**The massless Dirac operator.** On a closed oriented Riemannian 3-manifold $(M, g)$ with framing $e_j$, the massless Dirac operator is $W = -i\sigma^\alpha(\partial_\alpha + \frac{1}{4}\sigma^\beta \partial_\beta\sigma_\alpha + \Gamma^\beta_{\alpha\gamma}\sigma^\gamma)$ acting on $H^1(M; \mathbb{C}^2) \to L^2(M; \mathbb{C}^2)$, where $\sigma^\alpha = s_j e_j^\alpha$ are Pauli matrices projected along the framing. The analysis is restricted to 3 dimensions because the method requires simple eigenvalues of the principal symbol.

**Propagator decomposition.** The Dirac propagator $U(t) = e^{-itW}$ splits as $U(t) = U_+(t) + U_0 + U_-(t)$ corresponding to positive, zero, and negative eigenvalues. Each $U_\pm$ is constructed as a single global oscillatory integral with complex-valued phase function, circumventing caustic obstructions.

**Weyl coefficients.** The mollified counting function derivative admits the expansion $(N'_\pm * \mu)(y, \lambda) = c_2^\pm(y)\lambda^2 + c_1^\pm(y)\lambda + c_0^\pm(y) + \ldots$ as $\lambda \to +\infty$. Known: $c_2^\pm = 1/(2\pi^2)$ and $c_1^\pm = 0$. The paper computes $c_0^\pm$ (the third Weyl coefficient) for the first time.

**Key technique.** The use of complex-valued phase functions (following Laptev-Safarov-Vassiliev) allows the propagator to be a single global FIO, avoiding the need for compositions of local-in-time propagators. Small-time expansions of principal and subprincipal symbols are expressed in terms of Levi-Civita curvature and Weitzenbock torsion.

**Examples.** Explicit computations for $M = S^3$ (isotropic in momentum) and $M = S^2 \times S^1$ (anisotropic).

## Key Results

1. Global construction of $U_\pm(t)$ as invariantly defined oscillatory integrals with complex-valued phase
2. Closed formula for the principal symbols of the propagators (Theorem 6.1)
3. Algorithm for computing all homogeneous components of the full symbol
4. Small time expansion of principal and subprincipal symbols in geometric invariants (Theorem 7.13)
5. Third local Weyl coefficients $c_0^\pm(y)$ computed for the massless Dirac operator (Theorem 8.1)

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Massless Dirac operator | $W = -i\sigma^\alpha(\partial_\alpha + \frac{1}{4}\sigma^\beta\partial_\beta\sigma_\alpha + \Gamma^\beta_{\alpha\gamma}\sigma^\gamma)$ | Eq. (1.4) |
| Dirac propagator | $U(t) = e^{-itW}$ | Eq. (1.9) |
| Propagator decomposition | $U(t) = U_+(t) + U_0 + U_-(t)$ | Sec. 1 |
| Counting function | $N_\pm(y;\lambda) = \sum_{0 < \pm\lambda_k < \lambda} [v_k(y)]^* v_k(y)$ | Eq. (1.13) |
| Weyl expansion | $(N'_\pm * \mu)(y,\lambda) = c_2^\pm \lambda^2 + c_1^\pm \lambda + c_0^\pm + \ldots$ | Eq. (1.17) |
| Leading Weyl coeff. | $c_2^\pm(y) = 1/(2\pi^2),\quad c_1^\pm(y) = 0$ | Eq. (1.19) |

## Relevance to Phonon-Exflation

The global propagator construction for the massless Dirac operator on 3-manifolds provides rigorous spectral asymptotic machinery relevant to the project's analysis of the Dirac spectrum on compact internal spaces. The Weyl coefficient computation connects to the Seeley-DeWitt coefficients that enter the spectral action. The SU(3) manifold of the internal fiber is a compact 3-manifold (in the sense of its group manifold structure), and the spectral asymptotics of the Dirac operator on such spaces determine the high-energy behavior of the spectral action.
