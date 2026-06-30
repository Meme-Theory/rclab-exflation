# On the Gravitational Field of a Sphere of Incompressible Fluid according to Einstein's Theory

**Author(s):** K. Schwarzschild (translation by S. Antoci)
**Year:** 1916 (translation posted 1999)
**Journal:** Sitzungsberichte der Koniglich Preussischen Akademie der Wissenschaften zu Berlin, Phys.-Math. Klasse 1916, 424-434 (communicated February 24th, 1916)
**arXiv:** physics/9912033
**Relevance:** MEDIUM

---

## Abstract

No formal abstract. The paper extends Schwarzschild's prior "Mass point" memoir (arXiv:physics/9905030) to the interior of a homogeneous sphere of incompressible fluid of finite radius. The adjective "incompressible" is necessary, Schwarzschild notes, because in general relativity gravity depends not only on matter quantity but also on its energy, and a solid body in tension would gravitate differently from a fluid.

---

## Key Arguments and Derivations

**Field equations and matter (§2).** Schwarzschild uses Einstein's 1915 field equations in the form Sum_alpha (partial_alpha Gamma^alpha_{mu nu}) + Sum_{alpha beta} Gamma^alpha_{mu beta} Gamma^beta_{nu alpha} = G_mu_nu (Eq. 1), with G_mu_nu = -kappa (T_mu_nu - (1/2) g_mu_nu T) (Eq. 5) and kappa = 8 pi k^2 (Gauss's gravitational constant k). For an incompressible fluid at rest the mixed energy-momentum tensor has T^1_1 = T^2_2 = T^3_3 = -p, T^4_4 = rho_0 (Eq. 2), with trace T = rho_0 - 3p (Eq. 4).

**Geometric setup (§3).** Using polar-coordinates of determinant 1 (same construction as the "Mass point" paper: x_1 = r^3/3, x_2 = -cos theta, x_3 = phi, x_4 = t), the line element takes the form (Eq. 8):

  ds^2 = f_4 dx_4^2 - f_1 dx_1^2 - f_2 dx_2^2/(1 - x_2^2) - f_2 dx_3^2 (1 - x_2^2)

with f_1 f_2^2 f_4 = 1 (determinant equation, Eq. 9). Outside the sphere the f's take the form (Eq. 9): f_4 = 1 - alpha (3 x_1 + rho)^{-1/3}, f_2 = (3 x_1 + rho)^{2/3}, with alpha, rho constants to be fixed by matching to the interior.

**Interior field equations (§3-§4).** Restricting to the equator x_2 = 0, Schwarzschild writes three field equations (a), (b), (c), the determinant equation (d), and the single equilibrium equation (e) obtained from Sum_alpha partial_alpha T^alpha_sigma + Sum_{mu nu} Gamma^mu_{sigma nu} T^nu_mu = 0. The equilibrium equation combined with (d) gives immediately:

  (rho_0 + p) sqrt(f_4) = const = gamma          (Eq. 10)

Multiplying (a), (b), (c) by appropriate factors and using (d), Schwarzschild produces primed equations (a'), (b'), (c') and their combinations (a' + 2 b' + c', a' + c'). New variables f_2 = eta^{2/3}, f_4 = zeta eta^{-1/3}, f_1 = 1/(zeta eta) (Eq. 13) bring the system to:

  (partial eta/partial x)(partial zeta/partial x) = 3 eta^{-2/3} + 3 kappa gamma zeta^{-1/2} eta^{1/6} - 3 kappa rho_0      (Eq. 16)
  2 zeta (partial^2 eta/partial x^2) = -3 kappa gamma zeta^{-1/2} eta^{1/6}      (Eq. 17)

Adding gives an equation whose integrating factor is partial eta/partial x and yields

  zeta (partial eta/partial x)^2 = 9 eta^{1/3} - 3 kappa rho_0 eta + 9 lambda      (Eq. 18)

with lambda an integration constant. Dividing (17) by (18)^{3/2} and integrating twice, zeta is eliminated and eta(x) is obtained via the double quadrature

  x = (kappa gamma/18) int d eta int [eta^{1/6} d eta / (eta^{1/3} - (kappa rho_0/3) eta + lambda)^{3/2}]      (Eq. 20)

**Matching conditions (§5).** Let r_a, x_a, eta_a denote surface values. Continuity of eta, zeta, their derivatives at the surface, plus p = 0 at the surface, fix:

  gamma = rho_0 sqrt((f_4)_a)                       (Eq. 22)
  zeta_a = eta_a^{1/3} - (kappa rho_0/3) eta_a + lambda

Requiring eta = 0 at x = 0 (so that f_2 = eta^{2/3} vanishes at the center, giving a smooth origin) yields a condition fixing eta_a (Eq. 25). A careful analysis for small eta of f_4 = lambda/eta^{1/3} [K + (kappa gamma/7) eta^{7/6}/lambda^{3/2}]^2 shows that for both lambda > 0 and lambda < 0 the pressure diverges unless K = 0, which in turn makes f_4 = 0 at eta = 0. The only physically acceptable choice is

  **lambda = 0.**

**Closed-form solution (§6).** With lambda = 0 the integrations become elementary. Introducing chi via sin chi = sqrt(kappa rho_0/3) eta^{1/3} (Eq. 28), the functions take the final form:

  f_2 = (3/(kappa rho_0)) sin^2 chi,  f_4 = ((3 cos chi_a - cos chi)/2)^2,  f_1 f_2^2 f_4 = 1      (Eq. 29)
  rho_0 + p = rho_0 (2 cos chi_a)/(3 cos chi_a - cos chi)      (Eq. 30)
  3 x = r^3 = (kappa rho_0/3)^{-3/2} [(9/4) cos chi_a (chi - (1/2) sin 2 chi) - (1/2) sin^3 chi]      (Eq. 31)

The surface value chi_a is fixed by density and radius via Eq. 32. The exterior constants become:

  rho = (kappa rho_0/3)^{-3/2} [(3/2) sin^3 chi_a - (9/4) cos chi_a (chi_a - (1/2) sin 2 chi_a)]      (Eq. 33)
  alpha = (kappa rho_0/3)^{-1/2} sin^3 chi_a      (Eq. 34)

**Interior line element (§7).** In chi, theta, phi coordinates the interior line element is

  ds^2 = ((3 cos chi_a - cos chi)/2)^2 dt^2 - (3/(kappa rho_0))[d chi^2 + sin^2 chi d theta^2 + sin^2 chi sin^2 theta d phi^2]      (Eq. 35)

The spatial part is the standard metric of the non-Euclidean geometry of the spherical 3-space with curvature radius sqrt(3/(kappa rho_0)). Remarkably, the geometry of spherical 3-space becomes real inside gravitating fluid spheres. For the Sun, this curvature radius is about 500 times the solar radius.

**Geometric and physical consequences (§7).** Schwarzschild defines naturally-measured radii (Eq. 37 ff.):
- P_i = sqrt(3/(kappa rho_0)) chi_a (interior radius, Eq. 38)
- P_o = sqrt(3/(kappa rho_0)) sin chi_a (exterior radius = R_a from outside, Eq. 39)

Relations to alpha include alpha/P_o = sin^2 chi_a and alpha = (kappa rho_0/3) P_o^3 (Eq. 40). The mass M = rho_0 V = (3/(4 k^2)) sqrt(3/(kappa rho_0)) (chi_a - (1/2) sin 2 chi_a) (Eq. 41). The fall velocity from infinity satisfies v_a = sin chi_a (Eq. 42). The gravitational/substantial mass ratio is alpha/(2 k^2 M) = (2/3) sin^3 chi_a/(chi_a - (1/2) sin 2 chi_a) (Eq. 43) and decreases as concentration grows.

**Upper concentration limit.** The velocity of light inside the sphere is v = 2/(3 cos chi_a - cos chi) (Eq. 44). At the center (chi = 0) v and p both diverge when cos chi_a = 1/3, at which point the fall velocity reaches sqrt(8/9) of the naturally-measured light speed. Hence there is a critical concentration above which a sphere of incompressible fluid cannot exist. Equivalently, a sphere of given gravitational mass alpha/(2 k^2) cannot have external radius smaller than

  **P_o >= (9/8) alpha**   (for incompressible fluid; for a mass point P_o = alpha)

For the Sun, alpha ~ 3 km; for 1 g, alpha ~ 1.5 * 10^{-28} cm.

## Key Results

1. **Exact interior solution for an incompressible fluid sphere (Eq. 35)**, matching the exterior vacuum solution of "Mass point" at r = r_a with lambda = 0 forced by regularity.
2. **Spatial interior geometry is that of a portion of a 3-sphere** with curvature radius sqrt(3/(kappa rho_0)).
3. **Pressure equation** (rho_0 + p) sqrt(f_4) = gamma (Eq. 10), giving rho_0 + p = rho_0 (2 cos chi_a)/(3 cos chi_a - cos chi).
4. **Maximum compactness** cos chi_a = 1/3 at which central pressure diverges; equivalently P_o >= (9/8) alpha for the incompressible fluid.
5. **Minimum exterior radius** P_o = alpha for a point mass (mass point limit), derived as the limit lambda > 0 or lambda < 0 with K = 0.
6. **Mass formula** M = (3/(4 k^2)) sqrt(3/(kappa rho_0)) (chi_a - (1/2) sin 2 chi_a) (Eq. 41).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Matter tensor | T^1_1 = T^2_2 = T^3_3 = -p, T^4_4 = rho_0 | Eq. 2 |
| Field-equation RHS | G_mu_nu = -kappa (T_mu_nu - (1/2) g_mu_nu T), kappa = 8 pi k^2 | Eq. 5 |
| Equilibrium integral | (rho_0 + p) sqrt(f_4) = gamma | Eq. 10 |
| Variable change | f_2 = eta^{2/3}, f_4 = zeta eta^{-1/3}, f_1 = 1/(zeta eta) | Eq. 13 |
| Key ODE | zeta (partial eta/partial x)^2 = 9 eta^{1/3} - 3 kappa rho_0 eta + 9 lambda | Eq. 18 |
| chi substitution | sin chi = sqrt(kappa rho_0/3) eta^{1/3} | Eq. 28 |
| Final f's | f_2 = (3/(kappa rho_0)) sin^2 chi, f_4 = ((3 cos chi_a - cos chi)/2)^2 | Eq. 29 |
| Pressure | rho_0 + p = rho_0 (2 cos chi_a)/(3 cos chi_a - cos chi) | Eq. 30 |
| Interior line element | ds^2 = ((3 cos chi_a - cos chi)/2)^2 dt^2 - (3/(kappa rho_0)) d Omega_3^2 | Eq. 35 |
| Exterior matching | alpha = (kappa rho_0/3)^{-1/2} sin^3 chi_a | Eq. 34 |
| Mass formula | M = (3/(4 k^2)) sqrt(3/(kappa rho_0)) (chi_a - (1/2) sin 2 chi_a) | Eq. 41 |
| Light speed | v = 2/(3 cos chi_a - cos chi) | Eq. 44 |

## Relevance to Phonon-Exflation

The interior Schwarzschild solution shows that a finite-radius incompressible mass is bounded in compactness: at cos chi_a = 1/3 the pressure and internal light speed diverge, and the exterior radius is bounded below by (9/8) alpha. In the phonon-exflation framework this kind of bound on emergent GR solutions is significant only as a consistency check at Level 3, since the fundamental description is spectral rather than geometric. The paper's observation that interior geometry is literally a piece of a 3-sphere is interesting when compared with SU(3) fiber geometry in the substrate picture — both are compact, positive-curvature manifolds serving as carriers of internal structure — but the analogy is superficial and the connection to D_K eigenvalue content is indirect.
