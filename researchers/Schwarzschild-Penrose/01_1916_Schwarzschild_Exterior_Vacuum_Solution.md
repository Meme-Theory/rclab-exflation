# On the Gravitational Field of a Mass Point according to Einstein's Theory

**Author(s):** K. Schwarzschild (translation and foreword by S. Antoci and A. Loinger)
**Year:** 1916 (translation posted 1999)
**Journal:** Sitzungsberichte der Koniglich Preussischen Akademie der Wissenschaften zu Berlin, Phys.-Math. Klasse 1916, 189-196 (communicated January 13th, 1916)
**arXiv:** physics/9905030
**Relevance:** HIGH

---

## Abstract

No formal abstract. The memoir derives the exact spherically symmetric vacuum solution of Einstein's gravitational field equations for the field of a point mass, starting from the requirement that the determinant |g_mu_nu| = -1 and that the solution be static, spherically symmetric, and approach Minkowski at infinity. The foreword (by translators Antoci and Loinger) asserts that this is the original form of Schwarzschild's solution and that it "leaves no room for the science fiction of the black holes" because the only singularity lies at the origin of spatial coordinates.

---

## Key Arguments and Derivations

**Problem statement (§1).** Schwarzschild recalls Einstein's prescription for the motion of a massless point along a geodesic of a manifold with line element ds = sqrt(Sum g_mu_nu dx_mu dx_nu). The equations of motion are

  d^2 x_alpha/ds^2 = Sum_{mu,nu} Gamma^alpha_{mu nu} (dx_mu/ds)(dx_nu/ds)

with Christoffel-like coefficients Gamma^alpha_{mu nu} defined in Eq. (3). The "field equations" in the form used (Eq. 4) together with the "equation of the determinant" |g_mu_nu| = -1 (Eq. 5) are taken to be preserved under coordinate substitutions of unit determinant. Four boundary conditions are imposed: (1) time-independence, (2) g_rho 4 = g_4 rho = 0 for rho = 1,2,3, (3) spatial rotational symmetry about the origin, (4) at infinity g_44 = 1 and g_11 = g_22 = g_33 = -1.

**Ansatz (§3).** The most general line element satisfying rotational symmetry and time-independence is written

  ds^2 = F dt^2 - G(dx^2 + dy^2 + dz^2) - H(x dx + y dy + z dz)^2

with F, G, H functions of r. To preserve the "determinant = 1" form of the field equations, Schwarzschild introduces the "polar coordinates of determinant 1":

  x_1 = r^3/3, x_2 = -cos theta, x_3 = phi, x_4 = t          (Eq. 7)

so that r^2 sin theta dr dtheta dphi = dx_1 dx_2 dx_3. In these coordinates the line element takes the form (Eq. 9):

  ds^2 = f_4 dx_4^2 - f_1 dx_1^2 - f_2 dx_2^2/(1 - x_2^2) - f_3 dx_3^2 (1 - x_2^2)

with f_1, f_2 = f_3, f_4 functions of x_1 only, subject to f_1 f_2^2 f_4 = 1 (the determinant equation) and appropriate limits at infinity.

**Field equations for the f's (§4).** Schwarzschild reads off the Gamma^alpha_{mu nu} from the geodesic equations, restricts to the equator x_2 = 0, and obtains three field equations (a), (b), (c) plus the determinant equation (d). He integrates (c) to get (c''): (1/f_4)(df_4/dx_1) = alpha f_1 with alpha an integration constant. Combining with (a) and (d) he obtains -2 d/dx_1 [(1/f_2) df_2/dx_1] = 3 [(1/f_2) df_2/dx_1]^2, which integrates to

  f_2 = (3 x_1 + rho)^{2/3}      (Eq. 10)

Using (c'') and (d) he then gets

  f_4 = 1 - alpha (3 x_1 + rho)^{-1/3}      (Eq. 11)
  f_1 = (3 x_1 + rho)^{-4/3} / [1 - alpha (3 x_1 + rho)^{-1/3}]      (Eq. 12)

The "condition of continuity" — that f_1 be discontinuous only at the origin of r — forces

  rho = alpha^3      (Eq. 13)

thereby reducing two integration constants (alpha, rho) to the single physical constant alpha related to the mass.

**The exact solution (§5).** Introducing the auxiliary radial variable R = (r^3 + alpha^3)^{1/3}, the line element becomes

  ds^2 = (1 - alpha/R) dt^2 - dR^2/(1 - alpha/R) - R^2 (dtheta^2 + sin^2 theta dphi^2)      (Eq. 14)

with R = (r^3 + alpha^3)^{1/3}. Schwarzschild emphasizes the uniqueness of the solution and notes that approximation methods alone would have left the ambiguity between alpha and rho unresolved.

**Geodesics and Mercury perihelion (§6).** Three first integrals of the geodesic equation give constants h, c, 1 (Eqs. 15-17). Reducing to the equatorial plane and setting x = 1/R, the orbit equation becomes

  (dx/dphi)^2 = (1-h)/c^2 + (h alpha/c^2) x - x^2 + alpha x^3      (Eq. 18)

which, with B = c^2/h and 2A = (1-h)/h, reproduces Einstein's equation (11) for the Mercury perihelion anomaly. The correspondence r -> R = r(1 + alpha^3/r^3)^{1/3} differs from r by ~10^{-12} at Mercury.

**Third Kepler law and limiting frequency.** For circular orbits Schwarzschild derives n^2 = alpha/[2(r^3 + alpha^3)] and notes that as R shrinks the angular velocity approaches a finite limit n_0 = 1/(alpha sqrt(2)) (for the Sun's mass about 10^4 per second), unlike Newtonian theory where n diverges.

## Key Results

1. **Unique exact spherically symmetric vacuum solution.** Under the four boundary conditions plus the determinant equation, there is a one-parameter family of solutions with parameter alpha.
2. **Line element (Eq. 14):** ds^2 = (1 - alpha/R) dt^2 - dR^2/(1 - alpha/R) - R^2 d Omega^2, with R = (r^3 + alpha^3)^{1/3}.
3. **Continuity condition rho = alpha^3 (Eq. 13)** reduces the two integration constants to one physical parameter.
4. **Mercury perihelion:** the geodesic equation (18) reproduces Einstein's prior approximate result, confirming exactness at second order.
5. **Limiting circular-orbit frequency n_0 = 1/(alpha sqrt(2))**, finite as R -> 0, unlike Newtonian theory.
6. **No horizon in the original variables.** In Schwarzschild's original coordinates, the only discontinuity of f_1 lies at r = 0 (equivalently R = alpha, since r = 0 gives R = alpha).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Polar coords det 1 | x_1 = r^3/3, x_2 = -cos theta, x_3 = phi | Eq. 7 |
| Line element (reduced) | ds^2 = f_4 dx_4^2 - f_1 dx_1^2 - f_2 dx_2^2/(1-x_2^2) - f_3 dx_3^2 (1-x_2^2) | Eq. 9 |
| Integrated f_2 | f_2 = (3 x_1 + rho)^{2/3} | Eq. 10 |
| Integrated f_4 | f_4 = 1 - alpha (3 x_1 + rho)^{-1/3} | Eq. 11 |
| Integrated f_1 | f_1 = (3 x_1 + rho)^{-4/3} / [1 - alpha (3 x_1 + rho)^{-1/3}] | Eq. 12 |
| Continuity condition | rho = alpha^3 | Eq. 13 |
| Exact line element | ds^2 = (1 - alpha/R) dt^2 - dR^2/(1 - alpha/R) - R^2 (dtheta^2 + sin^2 theta dphi^2), R = (r^3 + alpha^3)^{1/3} | Eq. 14 |
| Geodesic first integrals | (1 - alpha/R)(dt/ds)^2 - (dR/ds)^2/(1-alpha/R) - R^2 (dphi/ds)^2 = h | Eq. 15 |
| Angular momentum | R^2 dphi/ds = c | Eq. 16 |
| Time normalization | (1 - alpha/R) dt/ds = 1 | Eq. 17 |
| Orbit equation | (dx/dphi)^2 = (1-h)/c^2 + (h alpha/c^2) x - x^2 + alpha x^3 | Eq. 18 |
| Limiting frequency | n_0 = 1/(alpha sqrt(2)) | §6 |

## Relevance to Phonon-Exflation

Schwarzschild's 1916 exterior vacuum solution is the foundational example of a static spherically symmetric metric in general relativity. In the phonon-exflation framework, GR is an emergent Level-3 consequence of the spectral action derived from the Dirac operator D_K on Jensen-deformed SU(3); in particular the a_2 Seeley-DeWitt coefficient generates the Einstein-Hilbert action, so Schwarzschild-type solutions arise as an asymptotic description of the M4 factor once the fiber is held fixed. The metric is most directly relevant when comparing the framework's block-diagonality theorem for D_K (an analog of Birkhoff rigidity) against the classical statement that the exterior of any spherically symmetric vacuum source is unique. Schwarzschild's own variable R = (r^3 + alpha^3)^{1/3} and his contention that the horizon at R = alpha is an artifact of coordinates (translators' foreword notwithstanding) is historically important context for how the framework treats emergent horizons derived from substrate spectral data.
