# Trapped surfaces, horizons and exact solutions in higher dimensions

**Author(s):** Jose M. M. Senovilla
**Year:** 2002
**Journal:** arXiv preprint (hep-th/0204005); published in Class. Quantum Grav.
**arXiv:** hep-th/0204005
**Relevance:** MEDIUM

Note: The filename uses "Emparan" from the batch assignment, but the actual author of this arXiv paper is J. M. M. Senovilla (Bilbao).

---

## Abstract

A very simple criterion to ascertain if (D - 2)-surfaces are trapped in arbitrary D-dimensional Lorentzian manifolds is given. The result is purely geometric, independent of the particular gravitational theory, of any field equations or of any other conditions. Many physical applications arise, a few shown here: a definition of general horizon, which reduces to the standard one in black holes/rings and other known cases; the classification of solutions with a (D - 2)-dimensional abelian group of motions and the invariance of the trapping under simple dimensional reductions of the Kaluza-Klein/string/M-theory type. Finally, a stronger result involving closed trapped surfaces is presented. It provides in particular a simple sufficient condition for their absence.

---

## Key Arguments and Derivations

### Geometric setup

A (D-2)-dimensional spacelike surface S is parametrized by intrinsic coordinates lambda^A embedded via x^alpha = Phi^alpha(lambda^A). Its two linearly independent future-directed null normal one-forms k^+, k^- satisfy k^+_mu e^mu_A = 0, (k^+)^2 = (k^-)^2 = 0, and the normalization k^+ . k^- = -1. The two null second fundamental forms K^+_AB, K^-_AB and their traces K^+, K^- give the expansions of the two orthogonal null geodesic families. The trapping scalar is kappa = 2 K^+ K^- = H_mu H^mu where H = -K^- k^+ - K^+ k^- is the mean curvature vector. S is trapped, marginally trapped, or absolutely non-trapped as kappa is positive, zero, or negative everywhere.

### The main formula

For a family of (D-2)-surfaces S_{X^a} = {x^a = X^a = const}, a, b in {0, 1}, writing the line-element as g_{ab} dx^a dx^b + 2 g_{aA} dx^a dx^A + g_{AB} dx^A dx^B and defining G = sqrt(det g_{AB}) = e^U and g_a = g_{aA} dx^A, a direct Christoffel-symbol computation gives the mean curvature one-form
  H_mu = delta^a_mu (U_{,a} - div g_a)
and the trapping scalar kappa_{X^a} = - g^{bc} H_b H_c | S. These formulas are purely geometric, independent of matter, energy conditions, or field equations, and reduce to known results in D=4.

### Horizon definition

The "S_{X^a}-horizon" H is defined by the vanishing of g^{bc} H_b H_c: the locus where H changes causal character. This subsumes marginally trapped surfaces and hypersurfaces where one trace vanishes. In Kerr in Boyer-Lindquist coordinates, the formula recovers sign(kappa_{t,r}) = -sign(Delta) with Delta = r^2 - 2mr + a^2, exactly identifying the classical event and Cauchy horizons. For general spherically symmetric D-dim metrics ds^2 = g_{ab} dx^a dx^b + R^2 dOmega^2_{D-2}, H_a proportional to R_{,a}/R recovers the classical apparent horizon.

### Applications

1. **Reissner-Nordstrom-Tangherlini and Robertson-Walker cosmologies** are recovered as special cases. A generalized "mass function" 2M = R^{D-3} (1 - g^{bc} R_{,b} R_{,c}) arises naturally.
2. **5D rotating black rings** (Emparan-Reall, PRL 88, 101101): using the formula, the horizon at y = xi_4 is identified as a locus of closed marginally trapped 3-surfaces; a second locus Sigma: y + 3x = 4 xi_1 arises where K^+ K^- vanishes because one trace vanishes.
3. **Generalized Weyl solutions** (Emparan-Reall): with gaA = 0 and g_{AB} = diag(e^{2 U_2}, ..., e^{2 U_{D-1}}), the Ricci-flat condition implies g^{ab} G_{;ab} = 0 and g^{ab} (G U_{A,a})_{;b} = 0 -- a wave equation for G and four-dimensional-looking equations for each U_A. Different causal characters of U_{,a} give qualitatively different spacetime classes (cosmology, plane waves, Gowdy, colliding waves).
4. **Kaluza-Klein invariance**: for a reduction ansatz ds^2_D = exp(-sum_i psi_i) ds^2_4 + sum_i e^{2 psi_i} (dx^i)^2, the trapping scalar kappa for observable 2-surfaces in the 4D metric equals the trapping scalar for the full (D-2) surfaces. Hence the horizon H lifts/reduces between D and 4 dimensions invariantly.

### Closed trapped surfaces: bi-tangency argument

For any closed spacelike (D-2)-surface S~ inside a hypersurface Sigma_f = {f = 0} with df timelike, compactness forces Phi^a to achieve extrema on S~, at which points S~ must be "bi-tangent" to some S_{X^a} family-member. A direct computation gives
  K^+_{S~}|q = K^+_{X^a}|q - k^+_a gamma^{AB}_{S~} d^2 Phi^a/(dmu^A dmu^B)
with the second term spacelike-sign-opposite for the two null directions. This implies that if neither K^+_{X^a} nor K^-_{X^a} changes sign in a region (i.e., S_{X^a} are marginally or absolutely non-trapped throughout), then no closed trapped surface exists in that region.

### Absence theorem

For the general spherically symmetric line-element with R_{,mu} non-timelike everywhere, the (D-2)-spheres are absolutely non-trapped or marginally trapped, and there can be no closed trapped surface at all. This gives an extremely simple sufficient condition forbidding closed trapped surfaces, capturing globally static cases (flat spacetime, Einstein and anti-de Sitter universes) directly -- without invoking geodesic incompleteness arguments.

## Key Results

1. Formulas H_mu = delta^a_mu (U_{,a} - div g_a) and kappa = -g^{bc} H_b H_c give the trapping of (D-2)-surfaces in arbitrary D, purely geometrically.
2. The S_{X^a}-horizon H is defined by g^{bc} H_b H_c = 0 and coincides with classical apparent/event/Cauchy horizons in known cases.
3. In Kerr: sign(kappa_{t,r}) = -sign(Delta) where Delta = r^2 - 2mr + a^2.
4. For generalized Weyl D-dim vacuum, G = e^U satisfies a 2D wave equation and each U_A satisfies the same equation as in D=4.
5. Trapping is invariant under Kaluza-Klein dimensional reduction ds^2_D = exp(-sum psi_i) ds^2_4 + sum e^{2 psi_i} (dx^i)^2.
6. Closed trapped surface bi-tangency: if K^+_{X^a} and K^-_{X^a} do not change sign in a region, no closed trapped surface exists there.
7. Spherically symmetric spacetimes with R_{,mu} non-timelike have no closed trapped surfaces.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| First fundamental form | gamma_{AB} = g_{mu nu}|S (dPhi^mu/dlambda^A)(dPhi^nu/dlambda^B) | Eq. 2 |
| Null normalization | k^+_mu e^mu_A = 0, (k^+)^2 = 0, (k^-)^2 = 0, k^+.k^- = -1 | Eq. 3 |
| Null second fundamental forms | K^+/-_{AB} = -k^+/-_mu e^nu_A nabla_nu e^mu_B | Eq. 5 |
| Trapping scalar | kappa = 2 K^+ K^- = H_mu H^mu | Eq. 7 |
| Coordinate line-element | ds^2 = g_{ab} dx^a dx^b + 2 g_{aA} dx^a dx^A + g_{AB} dx^A dx^B | Eq. 8 |
| Volume element | G = sqrt(det g_{AB}) = e^U | Eq. 11 |
| Trace formula | K^+/-_{X^a} = k^+/-_a [G_{,a}/G - (1/G)(G gamma^{AB} g_{aA})_{,B}] | Eq. 12 |
| Mean curvature one-form | H_mu = delta^a_mu (U_{,a} - div g_a) | Eq. 13 |
| Trapping scalar (coordinate) | kappa_{X^a} = -g^{bc} H_b H_c|_{S_{X^a}} | Eq. 14 |
| Spherically symmetric metric | ds^2 = g_{ab}(x^c) dx^a dx^b + R^2(x^c) dOmega^2_{D-2} | Eq. 15 |
| Weyl-type Ricci-flat | g^{ab} G_{;ab} = 0, g^{ab} (G U_{A,a})_{;b} = 0 | Eq. 16 |
| Closed surface trace correction | K^+/-_{S~}|q = K^+/-_{X^a}|q - k^+/-_a gamma^{AB}_{S~} d^2 Phi^a/dmu^A dmu^B | Eq. 19 |

## Relevance to Phonon-Exflation

The central result that trapping is invariant under Kaluza-Klein dimensional reduction is directly relevant to the M4 x SU(3) framework: whether a surface is trapped in the full 10D substrate picture is equivalent to whether its 4D projection is trapped in the emergent spacetime. This justifies using either the 10D or 4D picture interchangeably when discussing horizons and trapped regions in the phonon-exflation setup. The absence theorem (no closed trapped surfaces when R_{,mu} is non-timelike) is the relevant higher-dimensional analog of how the framework's acoustic white hole -- the fold transit -- avoids singular closed trapped-surface formation: the emergent 4D geometry passes through a region where the analog of R_{,mu} is not timelike, consistent with no true closed trapped surface forming at tau ~ 0.19. The purely geometric (matter-independent) character of the horizon criterion is exactly the property the framework needs, because at the fold the effective stress-energy passes through an NEC violation region (expected at DNP crossing tau ~ 0.285), which would complicate any criterion tied to energy conditions.
