# The dynamics of vortices on S² near the Bradlow limit

**Author(s):** J. M. Baptista, N. S. Manton
**Year:** 2002 (published 2003)
**Journal:** J. Math. Phys. 44, 3495 (2003)
**arXiv:** hep-th/0208001
**Relevance:** LOW (vortex foundations, not directly used in KK program)

---

## Abstract

The explicit solutions of the Bogomolny equations for N vortices on a sphere of radius R²>N are not known. In particular, this has prevented the use of the geodesic approximation to describe the low energy vortex dynamics. In this paper we introduce an approximate general solution of the equations, valid for R²≳N, which has many properties of the true solutions, including the same moduli space CP^N. Within the framework of the geodesic approximation, the metric on the moduli space is then computed to be proportional to the Fubini-Study metric, which leads to a complete description of the particle dynamics.

---

## Key Results

1. **Approximate solutions near Bradlow limit**: For R² slightly greater than N, the authors fix the connection D = D_N and solve the holomorphicity condition D^{0,1}φ = 0 together with an "averaged" version of the second Bogomolny equation, yielding explicit approximate vortex solutions on S².

2. **Moduli space identification**: The moduli space M_N of these approximate ("pseudo-vortex") solutions is CP^N, matching the true moduli space of exact Bogomolny vortices on S².

3. **Fubini-Study metric**: The L² metric on the moduli space M_N is computed to be m = 2π(R² - N) m_{FS}, i.e. proportional to the Fubini-Study metric on CP^N, with a scale factor that vanishes at the Bradlow limit R² → N.

4. **Complete geodesic description**: All geodesics of (CP^N, m_{FS}) are explicitly parametrized as π(sin(ωt)y + cos(ωt)x) for orthonormal x, y in C^{N+1}. All geodesics are periodic with period π/|ω|.

5. **Vortex dynamics from root-finding**: The N-vortex motion is determined by finding the roots of a degree-N polynomial with time-varying coefficients derived from the geodesic on CP^N.

6. **Collision bound**: For N vortices starting at distinct positions with arbitrary initial velocities, there are at most 2N - 2 collisions during one period, proved via intersection with an algebraic hypersurface of degree 2N - 2 in CP^N.

7. **Right-angle scattering**: Head-on collision of two vortices produces 90° scattering, consistent with known results for planar vortices.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Bogomolny eq. 1 | $D^{0,1}\phi = 0$ | Eq. (1) |
| Bogomolny eq. 2 | $F + \frac{1}{2}(|\phi|^2_h - 1)\,\mathrm{vol}_R = 0$ | Eq. (2) |
| Bradlow constraint | $R^2 > N$ (area > 4πN for non-trivial solutions) | Sec. 2 |
| Holomorphic section | $\phi_1(z) = \frac{a_0 z^N + \cdots + a_N}{(1+|z|^2)^{N/2}}$ | Eq. (7) |
| Normalization | $\sum_{k=0}^{N} \frac{k!(N-k)!}{(N+1)!} |a_k|^2 = 1 - \frac{N}{R^2}$ | Sec. 3 |
| Moduli space metric | $m = 2\pi(R^2 - N)\,m_{FS}$ | Sec. 4 |
| Geodesic equation | $\ddot{c} = \frac{2\langle \dot{c}, c\rangle}{1 + \langle c, c\rangle}\,\dot{c}$ | Eq. (12) |
| Vortex polynomial | $w^N + \sum_{k=1}^{N} \binom{N}{k}^{1/2} c_k(t)\,w^{N-k} = \prod_{i=1}^{N}(w - z_i(t))$ | Eq. (18) |

## Relevance to Phonon-Exflation

This is Baptista's PhD-era work with Manton establishing the mathematical infrastructure for vortex moduli spaces on compact surfaces. The Fubini-Study metric on CP^N and the geodesic approximation for soliton dynamics are foundational techniques that recur throughout Baptista's later work on gauged sigma models and Kaluza-Klein geometry. The Bradlow bound (area > 4πN) is an early instance of the interplay between topology, geometry, and field content on compact spaces that becomes central in the KK program.
