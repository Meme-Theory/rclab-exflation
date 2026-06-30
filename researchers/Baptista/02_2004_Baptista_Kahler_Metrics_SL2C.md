# Some special Kahler metrics on SL(2,C) and their holomorphic quantization

**Author(s):** J. M. Baptista
**Year:** 2003 (published 2004)
**Journal:** J. Geom. Phys. 49, 281 (2004)
**arXiv:** math-ph/0306060
**Relevance:** LOW (vortex foundations, not directly used in KK program)

---

## Abstract

The group SU(2) x SU(2) acts naturally on SL(2,C) by simultaneous right and left multiplication. We study the Kahler metrics invariant under this action using a global Kahler potential. The volume growth and various curvature quantities are then explicitly computable. Examples include metrics of positive, negative and zero Ricci curvature, and the 1-lump metric of the CP^1-model on a sphere.

We then look at the holomorphic quantization of these metrics, where some physically satisfactory results on the dimension of the Hilbert space can be obtained. These give rise to an interesting geometrical conjecture, regarding the dimension of this space for general Stein manifolds in the semi-classical limit.

---

## Key Results

1. **Global Kahler potential for SU(2)xSU(2)-invariant metrics**: Every G-invariant Kahler form on M = SL(2,C) can be written as omega = (i/2) d-bar d (f o y), where y(A) = cosh^{-1}[tr(A^dag A)/2] and f is a smooth even function with f' > 0 on (0,+infty) and f'' > 0 on [0,+infty).

2. **Explicit curvature formulas**: The Ricci form, scalar curvature, volume, geodesic distance, and completeness criterion are all expressed in terms of the single function f(y).

3. **Ricci-flat metric**: The Stenzel metric on T*S^3 = SL(2,C) is recovered as a special case, given by d/dy(f')^3 = c(sinh y)^2.

4. **1-lump metric**: The L^2 metric on the moduli space of degree-1 lumps on S^2 (CP^1 sigma model) has Kahler potential f(y) = pi y coth y, positive Ricci curvature, and finite volume Omega = pi^6/6.

5. **Holomorphic quantization**: For SL(2,C) with a finite-volume G-invariant Kahler metric, the polynomial subspace H_poly of the quantum Hilbert space satisfies dim_C H_poly ~ Omega/(2 pi hbar)^3 as hbar -> 0+, matching semi-classical predictions.

6. **Stein manifold conjecture**: The semi-classical dimension formula dim H_poly ~ Omega/(2 pi hbar)^n (for complex dimension n) is conjectured to hold for general Stein manifolds with finite volume and finite-dimensional H_poly.

7. **Moment map**: The explicit moment map for the SU(2)xSU(2) action is mu(a,b) = (i/4) f'(y)/sinh(y) tr(m m^dag a - m^dag m b).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Invariant Kahler form | $\omega = \frac{i}{2}\partial\bar{\partial}(f \circ y)$ | Prop. 2.3 |
| Hermitian metric on Lambda | $H = \frac{f''(y)}{|z_1|^2}dz_1 \otimes d\bar{z}_1 + \frac{f'(y)}{2\sinh y}(dz_2 \otimes d\bar{z}_2 + dz_3 \otimes d\bar{z}_3)$ | Eq. (5) |
| Ricci form potential | $\rho = -i\partial\bar{\partial}\log\left[\left(\frac{f'(y)}{\sinh y}\right)^2 f''(y)\right]$ | Prop. 3.1 |
| Scalar curvature | $s = \frac{2}{f''(f')^2}\frac{d}{dy}\left((f')^2 \frac{d}{dy}\log\frac{\sinh^2 y}{f''(f')^2}\right)$ | Prop. 3.2 |
| Geodesic distance | $D(a,b) = \frac{1}{\sqrt{2}}\int_a^b \sqrt{f''(y)}\,dy$ | Eq. (9) |
| Volume | $\mathrm{vol}(M_r) = \frac{1}{3}(\pi f'(r))^3$ | Cor. 4.2 |
| Lump potential | $f(y) = \pi y \coth y$ | Eq. (14) |
| Hilbert space dimension | $\dim_{\mathbb{C}} H_{\mathrm{poly}} = \frac{1}{6}(m+1)(m+2)(2m+3)$ | Cor. 8.2 |

## Relevance to Phonon-Exflation

This paper develops the Kahler geometry of SL(2,C) with explicit computations of curvature, volume, and completeness using a single potential function. The holomorphic quantization program and the semi-classical dimension conjecture for Stein manifolds provide mathematical context for quantization on non-compact Kahler manifolds. The SU(2)xSU(2) invariance structure and the explicit moment map are precursors to Baptista's later work on gauged nonlinear sigma models and Kaluza-Klein geometry, where similar invariance techniques are applied to higher-dimensional internal spaces.
