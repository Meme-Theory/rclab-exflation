# Vortices as degenerate metrics

**Author(s):** J. M. Baptista
**Year:** 2013 (published 2014)
**Journal:** Lett. Math. Phys. 104, 731 (2014)
**arXiv:** 1212.3561
**Relevance:** LOW (vortex foundations, not directly used in KK program)

---

## Abstract

We note that the Bogomolny equation for abelian vortices is precisely the condition for invariance of the Hermitian-Einstein equation under a degenerate conformal transformation. This leads to a natural interpretation of vortices as degenerate hermitian metrics that satisfy a certain curvature equation. Using this viewpoint, we rephrase standard results about vortices and make new observations. We note the existence of a conceptually simple, non-linear rule for superposing vortex solutions, and we describe the natural behaviour of the L2-metric on the moduli space upon restriction to a class of submanifolds.

---

## Key Results

1. **Vortices as degenerate metrics**: The abelian vortex equation is precisely the condition for the degenerate conformal transformation omega' = tau^{-1}|phi|^2 omega to preserve the form (i Lambda_omega F_omega + e^2 tau) omega. Vortex solutions correspond to degenerate Kahler metrics satisfying the curvature equation i F_{omega'} + e^2 tau omega' = i F_omega + e^2 tau omega.

2. **Vortex superposition rule**: A conceptually simple, non-linear rule for superposing vortex solutions is discovered. If (A_1, phi_1) is a vortex on (M, omega) and (A_2, phi_2) is a vortex on the deformed background (M, tau^{-1}|phi_1|^2 omega), then the tensor product (A_1 + A_2, tau^{-1/2} phi_1 phi_2) is a vortex on the original (M, omega).

3. **Hyperbolic surface vortices**: On hyperbolic surfaces (constant curvature -e^2 tau), the curvature equation reduces to i F_{omega'} + e^2 tau omega' = 0, meaning each vortex defines a degenerate hyperbolic metric with the same curvature. All vortex solutions are quotients of hyperbolic metrics.

4. **Minimal volume bound**: Each vortex reduces the volume by 2 pi/(e^2 tau), giving Vol(M, omega') = Vol(M, omega) - (2 pi)/(e^2 tau) sum_j n_j. Existence requires 2 pi sum_j n_j < e^2 tau Vol(M, omega).

5. **Moduli space metric and submanifold restriction**: Fixing one vortex at position p deforms the background metric to omega'' (degenerate at p), and the remaining (d-1) vortices on this deformed background reproduce exactly the induced L2-metric on the submanifold M^d_p of the d-vortex moduli space (Theorem 2.2).

6. **Higher-dimensional extension (Theorem 3.1)**: For vortices on arbitrary Hermitian manifolds M, the vortex equation is the condition for invariance of the Hermitian-Einstein equation (i Lambda_{omega'} F_{f'} + e^2 alpha tau) omega' = (i Lambda_omega F_f + e^2 alpha tau) omega under the conformal transformation f' = tau'^{-1} |phi|^{2 alpha} f, omega' = tau^{-1} |phi|^2 omega.

7. **Modified vortex and constant scalar curvature**: The modified vortex equation (equivalent to perturbed Seiberg-Witten on Kahler surfaces) is precisely the condition for constant scalar curvature of the deformed metric tau^{-1}|phi|^2 omega.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Degenerate metric | $\omega' := \frac{1}{\tau}|\phi|^2 \omega$ | Eq. (5) |
| Curvature equation | $iF_{\omega'} + e^2\tau\,\omega' = iF_\omega + e^2\tau\,\omega$ | Eq. (6) |
| Volume reduction | $\mathrm{Vol}(M,\omega') = \mathrm{Vol}(M,\omega) - \frac{2\pi}{e^2\tau}\sum_j n_j$ | Sec. 2 |
| Superposition identity | $iF_{A_2+A_1} + e^2(\tau^{-1}|\phi_1\phi_2|^2 - \tau)\omega = [iF_{A_2} + e^2(|\phi_2|^2 - \tau)]\omega' + [iF_{A_1} + e^2(|\phi_1|^2 - \tau)]\omega$ | Sec. 2 |
| Energy density | $\mathcal{E}(\omega') := \frac{1}{2e^2}|F_{\omega'} - F_\omega|^2 + 2\tau|d\sqrt{\omega'/\omega}|^2 + \frac{e^2\tau^2}{2}|\omega' - \omega|^2$ | Eq. (12) |
| HE invariance (general) | $\left(i\Lambda_{\omega'}F_{f'} + e^2\alpha\tau\right)\omega' = \left(i\Lambda_\omega F_f + e^2\alpha\tau\right)\omega$ | Eq. (16) |
| Curvature with current | $iF_{\omega'} + e^2\tau\,\omega' = iF_\omega + e^2\tau\,\omega - 2\pi\sum_j n_j\,\delta(q_j)$ | Eq. (11) |

## Relevance to Phonon-Exflation

This paper provides a beautiful reinterpretation of abelian vortices as degenerate Riemannian metrics satisfying curvature equations, connecting vortex theory to problems of prescribed curvature (Kazdan-Warner). The vortex superposition rule and the invariance of the Hermitian-Einstein equation under degenerate conformal transformations are elegant structural results. The connection between modified vortex equations and constant scalar curvature metrics, including the link to Seiberg-Witten equations on Kahler surfaces, provides deep geometric context. The higher-dimensional extension (Theorem 3.1) relating vortex equations to Hermitian-Einstein invariance is part of the mathematical framework that Baptista brings to his later work on Kaluza-Klein geometry and gauge field reductions on compact manifolds.
