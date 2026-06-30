# Black Holes in Higher Dimensions

**Author(s):** Roberto Emparan, Harvey S. Reall
**Year:** 2008
**Journal:** Living Reviews in Relativity (arXiv preprint v2)
**arXiv:** 0801.3471
**Relevance:** HIGH

---

## Abstract

We review black hole solutions of higher-dimensional vacuum gravity, and of higher-dimensional supergravity theories. The discussion of vacuum gravity is pedagogical, with detailed reviews of Myers-Perry solutions, black rings, and solution-generating techniques. We discuss black hole solutions of maximal supergravity theories, including black holes in anti-de Sitter space. General results and open problems are discussed throughout.

---

## Key Arguments and Derivations

### Why higher-D gravity is richer than 4D

Two structural facts make gravity fundamentally different in d > 4: (i) the rotation group SO(d-1) has Cartan subgroup U(1)^N with N = floor((d-1)/2), so black holes can have up to N independent angular momenta in mutually orthogonal rotation planes; (ii) the Newtonian potential falls as 1/r^{d-3} while the centrifugal barrier J^2/(M^2 r^2) does not depend on d, making the competition between gravity and rotation strongly dimension-dependent. Extended horizons (black strings, black p-branes) exist in any d >= 5 as direct products of a lower-D black hole with flat directions, and bending such objects into compact cycles while balancing tension against rotation gives new horizon topologies (black rings with S^1 x S^{d-3} horizons) unknown in 4D.

### Conserved charges

The Einstein-Hilbert action in d dimensions is I = (1/(16 pi G)) Int d^d x sqrt(-g) R + I_matter, with G defined so that S = A_H/(4G) in every dimension. Linearizing around Minkowski and solving in transverse gauge, the asymptotic metric for a source with mass M and antisymmetric angular-momentum matrix J_{ij} is
  h_tt = (16 pi G / ((d-2) Omega_{d-2})) M / r^{d-3}
  h_{ti} = -(8 pi G / Omega_{d-2}) x^k J_{ki} / r^{d-1}
  h_{ij} = (16 pi G / ((d-2)(d-3) Omega_{d-2})) M / r^{d-3} delta_{ij}
with Omega_{d-2} = 2 pi^{(d-1)/2} / Gamma((d-1)/2). Diagonalizing J_{ij} gives N independent angular momenta J_a.

### Dimensionless phase-space variables

To compare solutions with the same mass, the review introduces dimensionless spin and area parameters j^{d-3}_a = c_J J^{d-3}_a / (G M^{d-2}) and a^{d-3}_H = c_A A^{d-3}_H / (G M)^{d-2}, with specific normalization constants c_J and c_A. Phase diagrams are plotted in (j_1, j_2, ..., j_N) space.

### Schwarzschild-Tangherlini and black p-branes

The higher-D Schwarzschild generalization (Tangherlini 1963) is
  ds^2 = -(1 - mu/r^{d-3}) dt^2 + dr^2/(1 - mu/r^{d-3}) + r^2 dOmega^2_{d-2}
where the mass parameter is mu = 16 pi G M / ((d-2) Omega_{d-2}) and the horizon radius r_0 = mu^{1/(d-3)} coincides with the Michell-Laplace escape-velocity radius. The d > 4 Schwarzschild solution is stable against linearized gravitational perturbations (proved via scalar/vector/tensor Schrodinger-type equations with positive-operator analyses). Black p-branes are obtained as direct products ds^2_{d+p} = ds^2_d(B) + sum_i dx^i dx^i for any vacuum black hole B.

### Gregory-Laflamme instability

Black strings with horizon extent L >> r_0 are unstable to long-wavelength tensor perturbations with k < k_{GL} ~ 1/r_0. The fastest-growing mode has k ~ k_{GL}/2; the instability creates inhomogeneities that may pinch the horizon in finite asymptotic time (a static zero-mode at k = k_{GL} yields new inhomogeneous black-string solutions). For p-branes, perturbations with |k| < k_{GL} along any of the p brane directions are unstable, with k_{GL} depending on codimension but not p.

### Myers-Perry solutions

Myers and Perry (1986) found exact rotating black holes in any d > 4 with rotation in all N planes. The key technical fact enabling the construction is that MP solutions are in the Kerr-Schild class g_{mu nu} = eta_{mu nu} + 2 H(x^rho) k_mu k_nu with k_mu null in both g and eta.

**Single-spin MP metric:**
  ds^2 = -dt^2 + (mu / (r^{d-5} Sigma))(dt - a sin^2 theta dphi)^2 + (Sigma/Delta) dr^2 + Sigma dtheta^2 + (r^2 + a^2) sin^2 theta dphi^2 + r^2 cos^2 theta dOmega^2_{(d-4)}
with Sigma = r^2 + a^2 cos^2 theta and Delta = r^2 + a^2 - mu/r^{d-5}. The mass and angular momentum are M = (d-2) Omega_{d-2} mu / (16 pi G) and J = 2 M a / (d-2). The horizon at the largest root of Delta exists for:
- d = 4: regular up to Kerr bound a = mu/2
- d = 5: extremal at mu = a^2 with zero-area naked ring singularity
- d >= 6: **arbitrarily large a**, no extremality bound; defines the "ultra-spinning" regime

In the ultra-spinning limit (a >> r_0) for d >= 6, the horizon flattens along the rotation plane and approaches a black membrane of topology R^2 x S^{d-4}. The transition occurs at (a/r_0)_{mem} = sqrt((d-3)/(d-5)), where the Hawking temperature T_H = (1/(4 pi))(2 r_0/(r_0^2 + a^2) + (d-5)/r_0) reaches a minimum.

**General-rotation MP metric (odd d):**
  ds^2 = -dt^2 + (r^2 + a_i^2)(dmu_i^2 + mu_i^2 dphi_i^2) + (mu r^2 / (Pi F))(dt - a_i mu_i^2 dphi_i)^2 + (Pi F/(Pi - mu r^2)) dr^2
with sum mu_i^2 = 1, F = 1 - sum a_i^2 mu_i^2/(r^2 + a_i^2), Pi = prod_i (r^2 + a_i^2). For even d a slight modification with r^2 dalpha^2 and mu r in the mass term appears.

**MP phase space:** in d = 5, black holes exist in |j_1| + |j_2| <= 1 (square, no ultra-spinning); in d = 6 the extremal curve is |j_1| = (pi/(2 sqrt(3)))^{1/3} sqrt((1 - 4 nu^3 +/- sqrt(1 - 16 nu^3))/(4 nu)), |j_2| analog with minus sign, 0 <= nu <= 2^{-4/3} -- with two ultra-spinning prongs. In d = 7, 8 the phase space is a 3D "star" with ultra-spinning directions for each j_i independently. In a direction along which one spin becomes large, the phase-space cross-section reduces dimensionally, mimicking the (d-2)-dim phase diagram.

### MP stability and the ultra-spinning instability

In the ultra-spinning regime the horizon becomes brane-like, so Gregory-Laflamme-style instabilities are expected. The entropy argument of [9] shows that fragmentation into smaller black holes is thermodynamically preferred whenever a_i >~ r_0, suggesting an instability sets in near (39). Scalar-field perturbations remain stable even ultra-spinning, but gravitational perturbations have not been fully analyzed except for equal-angular-momentum cases in 2N+1 dimensions (cohomogeneity-1 MP solutions), where tensor perturbations are numerically stable.

### Five-dimensional black rings

Black rings with horizon topology S^1 x S^2 exist in 5D asymptotically flat space, stabilized against S^1 collapse by rotation (Emparan-Reall 2002). The Pomeransky-Sen'kov form:
  ds^2 = -(F(y)/F(x))(dt - C R (1+y)/F(y) dpsi)^2 + (R^2/((x-y)^2)) F(x) [-(G(y)/F(y)) dpsi^2 - dy^2/G(y) + dx^2/G(x) + (G(x)/F(x)) dphi^2]
with F(xi) = 1 + lambda xi, G(xi) = (1 - xi^2)(1 + nu xi), C = sqrt(lambda (lambda - nu) (1+lambda)/(1-lambda)). Elimination of conical singularities on the plane of the ring requires lambda = 2 nu/(1 + nu^2) and angular periodicity 2 pi sqrt(1 - lambda)/(1 - nu), leaving a 2-parameter (nu, R) family with nu interpretable as "thickness."

**Phase curve:** in dimensionless (j, a_H) variables, equilibrium single-spin rings have a_H = 2 sqrt(nu(1-nu)), j = sqrt((1+nu)^3/(8 nu)), with a cusp at nu = 1/2 (minimum j = sqrt(27/32), maximum a_H = 1). The **thin black ring branch** (nu < 1/2) extends to j -> infinity with a_H -> 0; the **fat black ring branch** (nu > 1/2) extends to j -> 1 with a_H -> 0. Both branches coexist with the MP black hole in sqrt(27/32) <= j < 1, giving **triple non-uniqueness** -- proving that 4D uniqueness theorems do not extend to 5D.

**Doubly-spinning rings** (Pomeransky-Sen'kov 2006): impose a Kerr-like bound lambda >= 2 sqrt(nu) and 0 <= nu < 1. The second angular momentum is bounded by |j_2| < |j_1|/3, saturated at j_1 = 3/4, j_2 = 1/4. The full 5D phase space (MP + rings) has a central "dome" (MP, |j_1|+|j_2| <= 1) with "romanesque vault" black-ring extensions protruding from its corners.

### Weyl and inverse-scattering solution-generating techniques

For stationary solutions with d-3 commuting U(1) symmetries (only compatible with global asymptotic flatness in d = 4, 5 because the constraint d - 3 <= N = floor((d-1)/2) fails for d >= 6), the vacuum Einstein equations reduce to an integrable 2D GL(d-2, R) sigma-model. Solutions are characterized by rod structures: intervals along the z-axis where one Killing vector degenerates. For orthogonal Killing vectors (Weyl solutions), the potentials U_a(r, z) satisfy a flat-space axisymmetric Laplace equation with constraint sum_{a=0}^{d-3} U_a = log r, and rods of density 1/2 along the z-axis give regular solutions. The Schwarzschild and Tangherlini black holes correspond to simple rod configurations; more complex rod structures give new black holes.

### Multi-black hole solutions

Combined Myers-Perry + black ring + inverse-scattering techniques have produced (in 5D): Black Saturn (a central MP black hole surrounded by a concentric black ring), di-rings (two concentric black rings), and bicycling black rings (two orthogonal rings). These demonstrate extreme non-uniqueness: multiple topologically distinct solutions at the same (M, J_1, J_2).

### General results in higher dimensions

- **Black hole topology (Sec 8.2):** in higher dimensions, horizon topologies are less restricted than 4D. Galloway-Schoen (2006) showed horizons must be of "positive Yamabe type" but this still allows many topologies. Known 5D: S^3 and S^1 x S^2; higher dimensions likely admit more.
- **Uniqueness (Sec 8.3):** MP is unique among asymptotically flat non-extremal vacuum black holes of spherical topology with N rotational isometries. In d = 5 with two U(1) symmetries, solutions are uniquely characterized by (M, J_a, rod structure). Full d = 5 classification remains open due to the open question of whether only one rotational symmetry may exist.
- **Stationary black holes (Sec 8.4):** in 4D, stationarity implies axisymmetry (Hawking's rigidity theorem); in d > 4, stationarity implies at least one U(1) rotational isometry (Hollands-Ishibashi-Wald), but whether more rotational isometries must exist is open.
- **Supersymmetric black holes (Sec 8.5):** in 5D minimal supergravity, near-horizon geometries of BPS black holes must be locally isometric to BMPV near-horizon, AdS_3 x S^2 (supersymmetric black ring), or flat. BMPV and BPS black rings are the known representatives.
- **Algebraic classification (Sec 8.6):** MP solutions are type D in the higher-D classification; black rings are algebraically special but not as special as MP.

### Laws of black hole mechanics

The standard laws extend to d > 4, with two notable extensions:

1. **Dipole contribution:** black rings with dipole charge q (not a conserved charge but a Wilson line on the S^2 fiber) satisfy dM = (kappa/(8 pi)) dA_H + Omega_H dJ + Phi dQ + phi dq.

2. **Multi-black-hole first law:** for solutions with disconnected horizon components labeled by i,
  dM = sum_i ((kappa^{(i)}/(8 pi)) dA^{(i)}_H + Omega^{(i)}_j dJ^{(i)}_j + Phi^{(i)} dQ^{(i)}).

### Hawking radiation

Extends to higher-D black holes: temperature T = kappa/(2 pi), Planckian spectrum with greybody corrections. Technical difficulties in separating wave equations are confined to MP solutions. Multi-black-hole thermodynamics requires (T^{(i)}, Omega^{(i)}, Phi^{(i)}) equal across components for genuine thermal equilibrium.

### AdS black holes

Schwarzschild-AdS: ds^2 = -U(r) dt^2 + dr^2/U(r) + r^2 dOmega^2_{d-2} with U(r) = 1 - mu/r^{d-3} + r^2/ell^2. Thermodynamics shows small-r_+ behaves negative-specific-heat (like Schwarzschild); at r_+ ~ ell there is a Hawking-Page phase transition T_{HP} above which large black holes dominate and are stable in the canonical ensemble (dual CFT thermal phase transition). Kerr-MP-AdS solutions exhibit super-radiant instabilities when Omega_i ell > 1 (no Killing field timelike everywhere outside the horizon). Charged AdS black holes in gauged supergravity have distinct structure: extremal Reissner-Nordstrom-AdS is not BPS; BPS limit gives a naked singularity.

## Key Results

1. Schwarzschild-Tangherlini black holes exist in any d >= 4 with horizon radius r_0 = mu^{1/(d-3)} and are stable against linearized gravitational perturbations.
2. Myers-Perry solutions in the Kerr-Schild class give rotating black holes in any d > 4 with up to N = floor((d-1)/2) independent angular momenta.
3. For d >= 6, MP black holes have no upper extremality bound on angular momentum (ultra-spinning regime), flattening into a black-membrane geometry with expected Gregory-Laflamme-type instability.
4. The Gregory-Laflamme instability affects black p-branes in any d; k_{GL} depends on codimension but not p; k = k_{GL} supplies a static zero-mode leading to a branch of inhomogeneous black strings.
5. 5D vacuum black rings with S^1 x S^2 horizons exist in two branches (thin, fat), exhibiting triple non-uniqueness with MP black holes in sqrt(27/32) <= j < 1. Black hole uniqueness does not hold in 5D.
6. Doubly-spinning black rings exist with the Kerr-like bound lambda >= 2 sqrt(nu), |j_2| < |j_1|/3.
7. Stationary 5D solutions with two U(1) rotational symmetries reduce to an integrable 2D GL(3, R) sigma-model, characterized by rod structures; uniqueness theorems exist for this sector.
8. Inverse-scattering techniques generate 5D multi-black-hole solutions: Black Saturn, di-rings, bicycling rings, demonstrating extreme non-uniqueness.
9. No higher-dim extension of 4D axisymmetric solution-generating exists for d >= 6 in globally asymptotically flat space because d - 3 <= floor((d-1)/2) requires d <= 5.
10. Black-hole mechanics laws extend to higher-D, with new dipole work terms (black rings) and multi-component first laws.
11. Hawking-Page phase transition extends to d >= 4 Schwarzschild-AdS; AdS rotating black holes are super-radiantly unstable for Omega_i ell > 1.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Einstein-Hilbert action | I = (1/(16 pi G)) Int d^d x sqrt(-g) R + I_matter | Eq. 5 |
| Bekenstein-Hawking | S = A_H / (4 G) | Eq. 7 |
| Asymptotic h_tt | h_tt = (16 pi G / ((d-2) Omega_{d-2})) M / r^{d-3} | Eq. 14 |
| Asymptotic h_{t phi_a} | h_{t phi_a} = -(8 pi G J_a / Omega_{d-2}) mu_a^2 / r^{d-3} | Eq. 19 |
| Dimensionless spin | j^{d-3}_a = c_J J^{d-3}_a / (G M^{d-2}) | Eq. 21 |
| Sphere volume | Omega_{d-2} = 2 pi^{(d-1)/2} / Gamma((d-1)/2) | in-text |
| Number of rotation planes | N = floor((d-1)/2) | Eq. 1 |
| Tangherlini metric | ds^2 = -(1 - mu/r^{d-3}) dt^2 + dr^2/(1 - mu/r^{d-3}) + r^2 dOmega^2_{d-2} | Eq. 29 |
| Mass parameter | mu = 16 pi G M / ((d-2) Omega_{d-2}) | Eq. 28 |
| Single-spin MP metric | ds^2 = -dt^2 + (mu/(r^{d-5} Sigma))(dt - a sin^2 theta dphi)^2 + (Sigma/Delta) dr^2 + ... | Eq. 32 |
| MP Sigma, Delta | Sigma = r^2 + a^2 cos^2 theta, Delta = r^2 + a^2 - mu/r^{d-5} | Eq. 33 |
| MP mass and J | M = (d-2) Omega_{d-2} mu / (16 pi G), J = 2 M a / (d-2) | Eq. 34 |
| Single-spin Hawking T | T_H = (1/(4 pi))(2 r_0/(r_0^2 + a^2) + (d-5)/r_0) | Eq. 38 |
| Membrane transition | (a/r_0)_{mem} = sqrt((d-3)/(d-5)) | Eq. 39 |
| General MP (odd d) | ds^2 = -dt^2 + (r^2 + a_i^2)(dmu_i^2 + mu_i^2 dphi_i^2) + (mu r^2/(Pi F))(dt - a_i mu_i^2 dphi_i)^2 + (Pi F/(Pi - mu r^2)) dr^2 | Eq. 42 |
| MP Pi function | Pi(r) = prod_i (r^2 + a_i^2) | Eq. 44 |
| 5D MP phase space | |j_1| + |j_2| <= 1 | Eq. 48 |
| 6D extremal curve | |j_1|, |j_2| = (pi/(2 sqrt(3)))^{1/3} sqrt((1 - 4 nu^3 +/- sqrt(1 - 16 nu^3))/(4 nu)) | Eq. 49 |
| Black ring metric | ds^2 = -(F(y)/F(x))(dt - C R (1+y)/F(y) dpsi)^2 + (R^2/(x-y)^2) F(x) [...] | Eq. 50 |
| Black ring F, G | F(xi) = 1 + lambda xi, G(xi) = (1 - xi^2)(1 + nu xi) | Eq. 51 |
| Black ring equilibrium | lambda = 2 nu/(1 + nu^2) | Eq. 55 |
| Black ring phase curve | a_H = 2 sqrt(nu(1-nu)), j = sqrt((1+nu)^3/(8 nu)) | Eq. 56 |
| Double ring Kerr bound | 0 <= nu < 1, 2 sqrt(nu) <= lambda < 1 + nu | Eq. 60 |
| Second-spin bound | |j_2| < |j_1|/3 | Eq. 64 |
| Weyl solution metric | ds^2 = -e^{2 U_0} dt^2 + sum_a e^{2 U_a} (dx^a)^2 + e^{2 nu} (dr^2 + dz^2) | Eq. 71 |
| Weyl constraint | sum_{a=0}^{d-3} U_a = log r | Eq. 76 |
| Dipole first law | dM = (kappa/(8 pi)) dA_H + Omega_H dJ + Phi dQ + phi dq | Eq. 115 |
| Multi-BH first law | dM = sum_i ((kappa^{(i)}/(8 pi)) dA^{(i)}_H + Omega^{(i)}_j dJ^{(i)}_j + Phi^{(i)} dQ^{(i)}) | Eq. 116 |
| Schwarzschild-AdS | ds^2 = -U dt^2 + dr^2/U + r^2 dOmega^2_{d-2}, U = 1 - mu/r^{d-3} + r^2/ell^2 | Eq. 117 |

## Relevance to Phonon-Exflation

This review is the canonical reference for the higher-D black hole landscape in the spacetime dimensionality D = 10 that the phonon-exflation framework operates in (M4 x SU(3)). Several specific results are directly relevant: (1) Myers-Perry ultra-spinning instabilities for d >= 6 are the immediate GR-language precursor to the framework's GL-CUBIC-36 wall-as-kink interpretation, showing that rotational degrees of freedom in higher dimensions destabilize compact horizons in exactly the regime where the framework's Jensen-deformed fiber operates. (2) The Kerr-Schild structure g_{mu nu} = eta_{mu nu} + 2 H k_mu k_nu enabling exact MP solutions is a structural feature worth noting when deriving effective 4D geometries from the M4 x SU(3) substrate -- the framework's "space is emergent" picture should inherit the algebraic simplifications that Kerr-Schild form provides. (3) The non-uniqueness of 5D vacuum black holes (thin/fat rings + MP all coexisting at the same (M, J)) shows that conserved charges are insufficient to specify a higher-D black hole, providing a direct GR-level precedent for the framework's requirement that spectral-triple parameters beyond conserved charges are needed to fully specify a substrate configuration. (4) The Weyl-solution integrability limit d - 3 <= N = floor((d-1)/2) requiring d <= 5 for global asymptotic flatness explains structurally why the framework's D = 10 substrate cannot be treated with direct sigma-model integrability in 4D-asymptotic language -- the substrate picture is needed precisely where GR-level sigma-model techniques fail. (5) The Gregory-Laflamme instability of black p-branes, with k_{GL} depending on codimension but not p, parallels the framework's fold transit at tau ~ 0.19 where the Jensen deformation parameter drives a universal instability independent of SU(3) fiber details. (6) Multi-black-hole first laws (Eq. 116) are the direct analog of the framework's need for separate thermodynamic treatment of the fiber excitation spectrum and the emergent-4D black hole spectrum. (7) The AdS Hawking-Page transition and the rigid co-rotation condition Omega ell <= 1 provide the GR-language analogs of the framework's substrate-compaction timescape picture and its constraints on spectral reorganization near the fold.
