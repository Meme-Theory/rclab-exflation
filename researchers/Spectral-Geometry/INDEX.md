# Spectral Geometry Paper Index

**Researcher corpus**: Gilkey, Berger, Mueller, Lott, Connes, and applied spectral geometry authors
**Papers**: 35 (1975--2025)
**Primary domain**: Heat kernel asymptotics, spectral characterization, analytic torsion, NCG spectral action, eigenvalue bounds, spectral rigidity
**Project relevance**: Foundational mathematics for D_K spectrum on SU(3), Seeley-DeWitt coefficients, spectral action monotonicity, eigenvalue bounds (Lichnerowicz/Cheeger/Weyl), spectral rigidity of Jensen-deformed metric, BdG spectral triple, functional determinants

---

## Dependency Graph

```
GILKEY HEAT KERNEL FOUNDATIONS (1975-2004)
  01 (monograph) --> 03 (Dirac HK) --> 24 (survey)
  01 --> 02 (spectral geometry)
  01 --> 04 (homogeneous spaces)
  04 --> 25 (Show, Lie groups)
  04 --> 26 (Bytsenko, Lie groups)

BERGER EIGENVALUE THEORY (1975-2003)
  07 (Cheeger constants) --> 06 (isoperimetric bounds) --> 05 (panoramic view)

MUELLER TORSION & FLOW (1978-2002)
  08 (analytic torsion) --> 09 (spectral flow/eta)
  08 --> 14 (heat trace on forms)

CONNES NCG FOUNDATIONS (1986-2008)
  13 (cyclic cohomology) --> 12 (local index formula) --> 11 (spectral characterization)
  10 (Lott, covering spaces) --> 08

HEAT KERNEL MANUALS & APPLIED (2003-2022)
  01 --> 15 (Vassilevich manual)
  01 + 03 --> 16 (Berline-Getzler-Vergne)
  15 + 16 --> 28 (Capoferri-Vassiliev propagator)

SPECTRAL RIGIDITY & ISOSPECTRALITY (2010-2025)
  02 + 05 --> 17 (Gordon-Schueth-Sutton, Laplacian rigidity)
  17 --> 18 (Boldt-Lauret, Dirac rigidity)
  17 --> 31 (Arias-Marco, inaudibility)

NCG PARTICLE PHYSICS & SPECTRAL ACTION (2007-2024)
  11 + 12 --> 19 (uncanny precision)
  12 + 15 --> 20 (Fathizadeh-Khalkhali curvature)
  19 --> 21 (van Suijlekom matrix form)
  19 --> 27 (rationality RW)
  21 --> 29 (one-loop corrections)
  11 + 19 --> 32 (vS textbook 2ed)
  11 + 19 --> 33 (neutrino mass)
  33 --> 34 (Pati-Salam)

CDT & SPECTRAL DIMENSION (2023-2024)
  22 (Ambjorn-Loll CDT) --> 30 (CDT FEM analysis)
  02 + 05 --> 23 (Ivrii, Weyl law)

EIGENVALUE BOUNDS (2001)
  03 + 06 --> 35 (Friedrich-Kirchberg, Weyl tensor)
```

---

## Topic Map

### A. Heat Kernel Asymptotics and Seeley-DeWitt Coefficients
Papers: 01, 03, 14, 15, 16, 24, 25, 26
Explicit formulas for a_0 through a_6 on Riemannian manifolds. Gilkey monograph (01) and survey (24) give scalar and Dirac operator coefficients. Paper 03 specializes to Dirac with spinor-specific prefactors (2^{n/2} rank, sign flip in a_2). Vassilevich (15) is the computational manual with boundary conditions. BGV (16) provides rigorous Lichnerowicz formula D^2 = nabla*nabla + R/4. Show (25) and Bytsenko (26) give explicit character sums on compact Lie groups including SU(3). Mueller-Pflaum (14) extends to Laplacians on forms with degree-dependent coefficients.

### B. Eigenvalue Bounds and Spectral Inequalities
Papers: 02, 05, 06, 07, 23, 35
Weyl's law (02, 05, 23), Lichnerowicz bound (06), Cheeger inequality (07), Friedrich-Kirchberg Weyl tensor bound (35). Ivrii (23) gives sharp remainder estimates for Weyl counting function. Friedrich-Kirchberg (35) proves lambda_1^2 >= R/4 + delta(|W|^2) for manifolds with Weyl curvature.

### C. Spectral Rigidity and Isospectrality
Papers: 17, 18, 31
Gordon-Schueth-Sutton (17): naturally reductive metrics on simple Lie groups are spectrally isolated (Laplacian). Boldt-Lauret (18): Dirac spectral rigidity on SU(2), first rigidity theorem for first-order operators on homogeneous spaces. Arias-Marco (31): natural reductivity is INAUDIBLE -- isospectral pair exists where one is naturally reductive and one is not (9D nilmanifolds).

### D. Analytic Torsion, Eta Invariants, and Spectral Flow
Papers: 08, 09, 10
Mueller (08): Ray-Singer conjecture proved (analytic = Reidemeister torsion). Mueller (09): spectral flow = change in eta invariant, APS boundary conditions. Lott (10): heat kernels on covering spaces, twisted traces, connection to Peter-Weyl on quotient Lie groups.

### E. Connes NCG Foundations
Papers: 11, 12, 13
Spectral characterization theorem (11): 5 axioms reconstruct spin manifold from spectral triple. Local index formula (12): Connes-Moscovici cyclic cocycle formulation of Atiyah-Singer. Cyclic cohomology (13): non-commutative de Rham cohomology, transverse fundamental class of foliations.

### F. Spectral Action and NCG Particle Physics
Papers: 19, 20, 21, 27, 29, 32, 33, 34
Uncanny precision (19): spectral action truncates exactly at a_2 on Einstein spaces. Fathizadeh-Khalkhali (20): curvature from heat kernel in NCG, Gauss-Bonnet on NC spaces. Matrix form (21): systematic finite spectral triple computation, one-loop corrections. Rationality (27): all a_{2n} coefficients are rational polynomials in scale factor derivatives (RW). One-loop (29): spectral action survives quantum corrections with spectral closure. van Suijlekom textbook (32): comprehensive NCG+particle physics reference including finite-density formalism. Neutrino mass (33): right-handed neutrinos from finite NC geometry, seesaw from spectral action. Pati-Salam (34): relaxing first-order condition gives SU(4)xSU(2)xSU(2).

### G. CDT and Spectral Dimension
Papers: 22, 30
Ambjorn-Loll (22): spectral dimension d_s flows from 2 (UV) to 4 (IR) in CDT. CDT FEM (30): dual graph spectral methods unreliable in >2D; FEM needed for accurate Laplace-Beltrami eigenvalues.

### H. Dirac Propagator Methods
Papers: 28
Capoferri-Vassiliev (28): global oscillatory integral propagator for massless Dirac on 3-manifolds, algorithmic higher Weyl coefficient computation without heat kernels.

---

## Quick Reference

| Paper | Author(s) | Year | Key Result | Relevance |
|:------|:----------|:-----|:-----------|:----------|
| 01 | Gilkey | 1995 | Seeley-DeWitt a_0, a_2, a_4 explicit formulas | CRITICAL |
| 02 | Gilkey | 1975 | Spectral geometry foundations, Weyl's law | HIGH |
| 03 | Gilkey | 1982 | Dirac heat kernel, spinor a_k with 2^{n/2} | CRITICAL |
| 04 | Gilkey | 1978 | Heat kernel on homogeneous spaces via Peter-Weyl | CRITICAL |
| 05 | Berger | 2003 | Panoramic view: spectral characterization, bounds | HIGH |
| 06 | Berger | 1980 | Lichnerowicz bound, Ricci => eigenvalue bounds | CRITICAL |
| 07 | Berger | 1975 | Cheeger inequality: lambda_1 >= h^2/4 | HIGH |
| 08 | Mueller | 1978 | Ray-Singer = Reidemeister torsion | MEDIUM |
| 09 | Mueller | 1983 | Spectral flow, eta invariant, APS | MEDIUM |
| 10 | Lott | 1992 | Heat kernels on covering spaces, twisted traces | MEDIUM |
| 11 | Connes | 2008 | Spectral characterization of manifolds (5 axioms) | CRITICAL |
| 12 | Connes-Moscovici | 1998 | Local index formula in NCG, cyclic cocycles | HIGH |
| 13 | Connes | 1986 | Cyclic cohomology, transverse fundamental class | MEDIUM |
| 14 | Mueller-Pflaum | 2002 | Heat trace for Laplacians on forms | MEDIUM |
| 15 | Vassilevich | 2003 | Heat kernel user's manual, boundary conditions | CRITICAL |
| 16 | Berline-Getzler-Vergne | 2004 | Lichnerowicz D^2=nabla*nabla+R/4, rigorous proofs | CRITICAL |
| 17 | Gordon-Schueth-Sutton | 2010 | Laplacian spectral isolation on simple Lie groups | CRITICAL |
| 18 | Boldt-Lauret | 2022 | Dirac spectral rigidity on SU(2) | CRITICAL |
| 19 | Chamseddine-Connes | 2010 | Uncanny precision: a_4=0 on Einstein spaces | HIGH |
| 20 | Fathizadeh-Khalkhali | 2019 | Curvature in NCG from heat kernel | MEDIUM |
| 21 | van Suijlekom et al. | 2020 | Spectral action in matrix form, one-loop | HIGH |
| 22 | Ambjorn-Loll | 2024 | CDT spectral dimension flow 2->4 | MEDIUM |
| 23 | Ivrii | 2016 | Weyl law: sharp remainder O(lambda^{(d-1)/2}) | HIGH |
| 24 | Gilkey | 2004 | Dirac/Laplace spectral geometry survey | HIGH |
| 25 | Show (Hong) | 2011 | Heat kernel on compact Lie groups, Duflo | CRITICAL |
| 26 | Bytsenko-Elizalde-Odintsov | 2023 | Heat kernel on Lie groups, finite density | HIGH |
| 27 | Fathizadeh-Khalkhali | 2014 | Rationality of spectral action on RW | MEDIUM |
| 28 | Capoferri-Vassiliev | 2022 | Dirac propagator, higher Weyl coefficients | LOW |
| 29 | van Nuland-van Suijlekom | 2022 | One-loop spectral action renormalizability | HIGH |
| 30 | Coumbe et al. | 2023 | CDT FEM vs dual graph spectral analysis | LOW |
| 31 | Arias-Marco et al. | 2025 | Natural reductivity is inaudible | HIGH |
| 32 | van Suijlekom | 2024 | NCG & Particle Physics textbook (2nd ed.) | CRITICAL |
| 33 | Chamseddine-Connes-Marcolli | 2007 | Neutrino mass from spectral action | MEDIUM |
| 34 | Chamseddine-Connes-vS | 2013 | Pati-Salam from relaxed first-order | MEDIUM |
| 35 | Friedrich-Kirchberg | 2001 | Dirac eigenvalue bound with Weyl tensor | HIGH |

---

## Paper Entries

### Paper 01: Gilkey -- Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem (1995)
- **Type**: Monograph (CRC Press, 2nd ed.)
- **Key content**: Definitive reference for Seeley-DeWitt coefficients a_0 through a_4. Explicit formulas: a_0 = rank(E)(4pi)^{-n/2}Vol(M), a_2 = (1/6)int R dV, a_4 = (1/360)int[5R^2 - 2|Ric|^2 + 2|Rm|^2]dV. Dirac heat kernel with spinor rank 2^{n/2}. Path integral representation. Index theorem via heat kernel. Peter-Weyl on Lie groups.
- **Framework use**: All spectral action computations (S20a, S24a, S33-S37). Direct source for a_k formulas on Jensen-deformed SU(3).
- **Relevance**: CRITICAL

### Paper 02: Gilkey -- The Spectral Geometry of a Riemannian Manifold (1975)
- **Key content**: Launched spectral geometry. Weyl's law N(lambda) ~ C_n Vol lambda^{n/2}. Heat trace expansion. Spectral zeta function. Isospectrality examples (tori). Local vs global spectral information.
- **Framework use**: Weyl counting of Dirac eigenvalues on SU(3). Inverse spectral problem formulation.
- **Relevance**: HIGH

### Paper 03: Gilkey -- Heat Kernels for Dirac Operators (1982)
- **Key content**: Spinor heat kernel with a_0^{(D)} = 2^{n/2}. Dirac a_2^{(D)} = -(n/6) int R dV (negative sign vs scalars). a_4^{(D)} with coefficients c_0=5(n-1), c_1=-2(n+13), c_2=n+5. At n=4: c_0=15, c_1=-34, c_2=9. Twisted Dirac. Functional determinant det(D^2)=exp(-zeta'(0)).
- **Framework use**: Spinor prefactors in spectral action on M4 x SU(3). Dirac a_k formulas for all sessions.
- **Relevance**: CRITICAL

### Paper 04: Gilkey -- Heat Kernels on Homogeneous Spaces (1978)
- **Key content**: Spectrum from representations: lambda_{p,q} = 2(p^2+pq+q^2+3p+3q) on SU(3). Dimension d_{p,q} = (p+1)(q+1)(p+q+2)/2. Heat trace = sum d_rho^2 exp(-t lambda_rho). Seeley-DeWitt from representation theory. Functional determinant via Casimir.
- **Framework use**: Direct source for SU(3) eigenvalue labeling in Sessions 7-35. Peter-Weyl decomposition of D_K spectrum.
- **Relevance**: CRITICAL

### Paper 05: Berger -- A Panoramic View of Riemannian Geometry (2003)
- **Key content**: Comprehensive survey. Weyl asymptotics with curvature corrections. Spectral rigidity for round sphere. Sunada's isospectrality theorem. Spectral dimension from return probability. Quantum ergodicity.
- **Framework use**: Inverse spectral problem context. Spectral dimension diagnostic.
- **Relevance**: HIGH

### Paper 06: Berger -- Spectral Characterization and Isoperimetric Bounds (1980)
- **Key content**: Lichnerowicz theorem: Ric >= (n-1)k => lambda_1 >= (n-1)k. Scalar curvature bound: R >= c => lambda_1 >= nc/(n-1). Diameter-eigenvalue tradeoff. Bonnet-Myers. Volume comparison from positive Ricci.
- **Framework use**: Bounding Ricci curvature from Dirac spectrum on SU(3). Constraining Jensen deformation range.
- **Relevance**: CRITICAL

### Paper 07: Berger -- Eigenvalue Inequalities and Cheeger Constants (1975)
- **Key content**: Cheeger bound lambda_1 >= h(M)^2/4 (optimal constant). Diameter bound lambda_1 <= pi^2/diam^2. Thin manifold spectral gap vanishing. Nodal domain bounds.
- **Framework use**: Product space isoperimetric analysis for M4 x SU(3). Spectral gap interpretation for BCS condensation threshold.
- **Relevance**: HIGH

### Paper 08: Mueller -- Analytic Torsion and R-Torsion (1978)
- **Key content**: Ray-Singer conjecture proved: |tau_RS| = |tau_Reidemeister|. Torsion from zeta functions: log tau = sum (-1)^p p zeta_p'(0). Functional determinant formulas. Variation under metric change involves Ricci. Lens space explicit computation.
- **Framework use**: Analytic torsion T(tau) is UV-finite spectral invariant (uncomputed priority gate). Functional determinant of D_K.
- **Relevance**: MEDIUM

### Paper 09: Mueller -- Spectral Flow and Eta Invariants (1983)
- **Key content**: Eta invariant eta(D) = sum sign(lambda)|lambda|^{-s} at s=0. Spectral flow SF(D_0,D_1) = eta(D_0) - eta(D_1). Heat kernel representation. APS boundary conditions. Variation formula under metric deformation.
- **Framework use**: eta(D_BdG) = 0 at mu=0 (S35). Spectral flow = 0 during Jensen deformation (gap open throughout, S35).
- **Relevance**: MEDIUM

### Paper 10: Lott -- Heat Kernels on Covering Spaces (1992)
- **Key content**: Trace formula on covers with deck transformations. Twisted heat kernels. SU(3) as Spin(6)/Z_3 quotient. Peter-Weyl from covering space formula. Analytic torsion on covers.
- **Framework use**: SU(3) spectrum from universal cover. Consistency check on Peter-Weyl decomposition.
- **Relevance**: MEDIUM

### Paper 11: Connes -- Spectral Characterization of Manifolds (2008)
- **Key content**: Reconstruction theorem: commutative spectral triple satisfying 5 axioms reconstructs a spin manifold. Metric from Dirac commutators: d(x,y) = sup{|[D,f]|^{-1}}. Dimension from heat kernel exponent. Spectral action principle S = Tr(f(|D|/Lambda)).
- **Framework use**: THE overarching framework. D_K spectrum determines geometry. SM quantum numbers from C^16 (S7). CPT from reality structure J (S17a).
- **Relevance**: CRITICAL

### Paper 12: Connes-Moscovici -- Local Index Formula in NCG (1998)
- **Key content**: Index as integral of local density: ind(D) = int rho_ind dV. Cyclic cocycle formulation. a_d coefficient = topological invariant. Explicit 4D formula with curvature coefficients. Non-commutative generalization via cyclic cohomology.
- **Framework use**: a_4 on SU(3) contains topological information. Anomaly cancellation verification. Chern character from spectral data.
- **Relevance**: HIGH

### Paper 13: Connes -- Cyclic Cohomology and Transverse Fundamental Class (1986)
- **Key content**: Cyclic cohomology as NC analog of de Rham. Chern character as cyclic cocycle. Transverse fundamental class for foliations. K-theory pairing.
- **Framework use**: Algebraic foundation for spectral triple consistency. Anomaly cancellation.
- **Relevance**: MEDIUM

### Paper 14: Mueller-Pflaum -- Heat Trace for Laplacians on Forms (2002)
- **Key content**: Form-degree-dependent Seeley-DeWitt coefficients. Recursive formulas via representation theory. Coupled systems with gauge fields. Functional determinant: log|det(D)| = sum (-1)^p p zeta_p'(0). Kahler manifold special structure.
- **Framework use**: Boson vs fermion determinant ratio. Form Laplacian on SU(3).
- **Relevance**: MEDIUM

### Paper 15: Vassilevich -- Heat Kernel Expansion: User's Manual (2003)
- **Key content**: 113-page review. Explicit a_0 through a_6 with boundary conditions (Dirichlet/Neumann/Robin). Spinor and Yang-Mills generalizations. Product manifold formula: a_n(M1xM2) = sum_{i+j=n} a_i(M1) x a_j(M2). One-loop effective action. Spectral action connection.
- **Framework use**: Product space factorization for M4 x SU(3). Boundary condition treatment. Computational reference for all heat kernel coefficients.
- **Relevance**: CRITICAL

### Paper 16: Berline-Getzler-Vergne -- Heat Kernels and Dirac Operators (2004)
- **Key content**: Definitive monograph. Lichnerowicz formula D^2 = nabla*nabla + R/4 with rigorous proof. Equivariant index theorem. Stochastic interpretation (Bismut). Functional determinant via zeta regularization. All heat kernel coefficients are smooth in metric/connection.
- **Framework use**: Lichnerowicz bound on SU(3). Equivariant heat kernel under SU(3) action. Spectral action asymptotics foundation.
- **Relevance**: CRITICAL

### Paper 17: Gordon-Schueth-Sutton -- Spectral Isolation of Naturally Reductive Metrics (2010)
- **Key content**: THEOREM: Every naturally reductive metric on a compact simple Lie group is spectrally isolated within all left-invariant metrics. No isospectral twins in this class. Finiteness of isospectral sets. For SU(3): spectrum determines metric uniquely.
- **Framework use**: tau -> Spec(D_K(tau)) is INJECTIVE for naturally reductive Jensen deformation. No spectral degeneracy during fold. Validates spectral action as unique geometry encoder.
- **Relevance**: CRITICAL

### Paper 18: Boldt-Lauret -- Dirac Spectrum on Homogeneous 3-Spheres (2022)
- **Key content**: THEOREM: Dirac spectral rigidity on SU(2) -- isospectral Dirac implies isometric. Extends to SO(3) for both spin structures. Dirac spectrum determines scalar curvature pointwise (sharper than Laplacian). Metric recovery algorithm from full Dirac spectrum. First rigidity theorem for first-order operators on homogeneous spaces.
- **Framework use**: Strong hint that Dirac spectral rigidity extends to SU(3). Template for proving D_K spectral rigidity. Spectral monitor of internal geometry changes.
- **Relevance**: CRITICAL

### Paper 19: Chamseddine-Connes -- The Uncanny Precision of the Spectral Action (2010)
- **Key content**: On S^3: a_4 = a_6 = ... = 0 EXACTLY (Einstein space). On S^3 x S^1: corrections < 10^{-100}. Smooth cutoffs give exponential suppression. Truncation at a_2 is essentially exact. Higgs potential emerges exactly.
- **Framework use**: Justifies truncation at a_2 in spectral action computations. Einstein internal geometry has vanishing higher coefficients. Session 33+ truncation validated.
- **Relevance**: HIGH

### Paper 20: Fathizadeh-Khalkhali -- Curvature in NCG (2019)
- **Key content**: Scalar curvature recovery from heat kernel limit in NCG. Gauss-Bonnet for NC spaces. Heat kernel on compact groups via Weyl character formula. Internal curvature contributions to spectral action coefficients.
- **Framework use**: Extracting R_internal(tau) from Dirac spectrum. Verifying external/internal curvature separation.
- **Relevance**: MEDIUM

### Paper 21: van Suijlekom et al. -- Spectral Action in Matrix Form (2020)
- **Key content**: Finite spectral triple computation via eigenvalue decomposition. Quantization rules explicit. One-loop corrections: delta log det(D)/delta W. Renormalization finite after minimal subtraction. Tree-level results stable at weak coupling.
- **Framework use**: Matrix representation of SU(3) fiber (32x32 D_K). One-loop BCS corrections via functional determinant. Session 33-35 computation methods.
- **Relevance**: HIGH

### Paper 22: Ambjorn-Loll -- CDT Spectral Dimension (2024)
- **Key content**: Spectral dimension d_s(T) = -2 d(log P)/d(log T). CDT: d_s flows from ~2 (UV) to 4 (IR). Causality essential for emergence. Planck scale is natural cutoff.
- **Framework use**: Comparison framework for internal spectral dimension d_s(K). Open gate: d_s^{internal}(tau) flow.
- **Relevance**: MEDIUM

### Paper 23: Ivrii -- 100 Years of Weyl's Law (2016)
- **Key content**: Sharp remainder: N(lambda) = C_d V lambda^{d/2} + O(lambda^{(d-1)/2}). Semiclassical phase-space quantization. Magnetic field non-Weyl behavior. Microlocal analysis and wave front sets.
- **Framework use**: Sharp eigenvalue counting for Dirac spectrum on SU(3). Remainder bounds for spectral action truncation. Weyl counting verification (S24a, S35).
- **Relevance**: HIGH

### Paper 24: Gilkey -- Spectral Geometry of Dirac and Laplace Type (2004)
- **Key content**: Algorithmic survey. Computational formulas for a_k. Index theorem as heat kernel limit. Coupled systems (gravity + gauge). Practical algorithms for implementing heat kernel computations.
- **Framework use**: Computational reference for tier0 scripts. Step-by-step algorithm for Seeley-DeWitt on deformed SU(3).
- **Relevance**: HIGH

### Paper 25: Show (Hong) -- Heat Kernel on Compact Lie Groups (2011)
- **Key content**: Explicit heat trace via Peter-Weyl: Tr(exp(-t Delta_G)) = sum d_rho^2 exp(-t lambda_rho). Duflo isomorphism gives a_k from Casimir invariants. SU(3) Casimir from root system. Character sum evaluation via Weyl formula. Analytic torsion on groups.
- **Framework use**: PRIMARY tool for SU(3) heat kernel computation. Casimir eigenvalues, dimensions via hook-length. Sessions 7-35 spectral action evaluation.
- **Relevance**: CRITICAL

### Paper 26: Bytsenko-Elizalde-Odintsov -- Heat Kernel on Lie Groups (2023)
- **Key content**: Functional determinants on Lie groups. Symmetric spaces G/H heat kernels. Finite-density heat kernels (chemical potential/gap parameter). SU(3) explicit coefficients tabulated. Thermal properties and free energy asymptotics.
- **Framework use**: Finite-density spectral action with BCS gap Delta. BdG Hamiltonian heat kernel. Analytic torsion on deformed SU(3). SU(3) numerical coefficients for rapid computation.
- **Relevance**: HIGH

### Paper 27: Fathizadeh-Khalkhali -- Rationality of Spectral Action for RW (2014)
- **Key content**: Proved Chamseddine-Connes conjecture: all a_{2n} on Robertson-Walker are rational polynomials in scale factor derivatives. Extended explicit computation through a_{12}. Pseudodifferential operator algebra method.
- **Framework use**: Rationality ensures algebraic control of vacuum coefficients V(tau). No transcendental divergences from higher heat kernel orders.
- **Relevance**: MEDIUM

### Paper 28: Capoferri-Vassiliev -- Dirac Propagator on 3-Manifolds (2022)
- **Key content**: Global oscillatory integral propagator for massless Dirac. Algorithmic higher Weyl coefficient computation. Third local Weyl coefficient w_2 computed. No heat kernels needed.
- **Framework use**: Alternative method for computing spectral properties of deformed SU(3) Dirac operator. Bypasses mode-by-mode approximations.
- **Relevance**: LOW

### Paper 29: van Nuland-van Suijlekom -- One-Loop Corrections to Spectral Action (2022)
- **Key content**: THEOREM: One-loop renormalizability of spectral action. Ward identities enforce spectral closure (no non-spectral counterterms). Coupling constants run via standard SM beta functions. Monotonicity preserved under quantum corrections. Heat kernel coefficients renormalize but remain geometric.
- **Framework use**: Validates spectral action at quantum level. Monotonicity of S_full(tau) survives one-loop. F.5 wrong-sign result is stable under quantum corrections.
- **Relevance**: HIGH

### Paper 30: Coumbe et al. -- CDT Spectral Analysis via FEM (2023)
- **Key content**: Dual graph spectral methods unreliable in >2D (20-50% error, wrong spectral dimension). FEM gives correct Laplace-Beltrami eigenvalues. Spectral dimension discrepancy: graph gives d_s~2 vs FEM d_s~4 in 4D CDT.
- **Framework use**: Methodological warning for any future lattice discretization of SU(3) geometry.
- **Relevance**: LOW

### Paper 31: Arias-Marco -- Inaudibility of Naturally Reductive Property (2025)
- **Key content**: THEOREM: Natural reductivity is spectrally inaudible. Isospectral pair of 9D nilmanifolds where one is naturally reductive and one is not. Spectrum cannot determine homogeneous decomposition. Heat kernel coefficients a_n do not encode algebraic structure of g = h + m.
- **Framework use**: WARNING: SU(3) natural reductivity assumption cannot be verified from spectral data alone. Must be validated geometrically (Ambrose-Singer). Predictions robust across isospectral class if spectral stability holds.
- **Relevance**: HIGH

### Paper 32: van Suijlekom -- NCG and Particle Physics, 2nd Edition (2024)
- **Key content**: Comprehensive textbook. Spectral triples, heat kernels, spectral action. Finite-density formalism (Chapter 7): D(mu), effective potential, KMS. Pati-Salam (Chapter 8). One-loop renormalizability integrated. SM reconstruction from NCG.
- **Framework use**: PRIMARY reference for finite-density spectral action formalism. Chemical potential coupling to SU(3) deformation. BCS gap equation infrastructure. Pati-Salam extension path.
- **Relevance**: CRITICAL

### Paper 33: Chamseddine-Connes-Marcolli -- Neutrino Mass and Spectral Action (2007)
- **Key content**: Right-handed neutrinos as singlet fields in finite NC geometry. Seesaw mechanism from spectral action: m_nu = m_D^2/M_R. Unified Yukawa couplings in single Dirac matrix D_F. Majorana mass M_R ~ 10^{13}-10^{15} GeV from spectral action.
- **Framework use**: Blueprint for singlet fields in spectral triples. Structural parallel with BCS Cooper pair mass generation. Neutrino sector architecture.
- **Relevance**: MEDIUM

### Paper 34: Chamseddine-Connes-van Suijlekom -- Pati-Salam Beyond SM (2013)
- **Key content**: Relaxing first-order condition [[D,a],b]=0 gives Pati-Salam SU(4)xSU(2)_LxSU(2)_R. GUT scale M_X ~ 10^{14.5} GeV as prediction. Proton decay tau_p ~ 10^{34-35} yr. Right-handed W_R, Z_R bosons. All SM physics recovered at low energies.
- **Framework use**: Natural extension path if SU(3) fiber generalized to SU(4). Leptoquark channels. Exploratory.
- **Relevance**: MEDIUM

### Paper 35: Friedrich-Kirchberg -- Eigenvalue Estimates with Weyl Tensor (2001)
- **Key content**: Dirac eigenvalue bound: lambda_1^2 >= R/4 + delta(|W|^2). Weyl curvature is REPULSIVE (increases spectral gap). Nearly-Kahler bound: lambda_1^2 >= (3/2)rho_max + |W|^2/4. Equality characterizes geometry. Stronger than Lichnerowicz for non-Einstein spaces.
- **Framework use**: Bounding spectral gap under Jensen deformation (non-Einstein). Weyl tensor grows with tau (anisotropy). Spectral stability criterion: BCS stable iff lambda_1(tau) > critical value. Cross-check of numerical spectrum.
- **Relevance**: HIGH

---

## Cross-Paper Equation Concordance

### Heat Kernel Trace Expansion
- **Standard form**: Tr(exp(-tP)) ~ (4pi t)^{-d/2} sum_k a_k t^k
- Papers 01 (eq defining), 02, 03, 05, 14, 15 (comprehensive), 16 (rigorous), 24, 25, 26
- Convention: a_k INCLUDES the (4pi)^{-d/2} prefactor in Papers 01, 03, 15, 16
- Convention: a_k EXCLUDES it in Papers 02, 05 (integral form: a_k = int a_k(x) dV)
- **CAUTION**: Always verify which convention. Framework uses the integral form (Papers 02, 05 style)

### Lichnerowicz Formula
- D^2 = nabla* nabla + R/4 (scalar curvature, Dirac on spinors)
- Papers 03 (original for Dirac), 16 (rigorous proof), 35 (generalized with Weyl), 06 (eigenvalue consequence)
- For Dirac on general bundle: D^2 = nabla*nabla + R/4 + F (endomorphism from bundle curvature)
- Papers 15 (Vassilevich: D^2 = -(g^{ij}nabla_i nabla_j + E)), 16 (BGV)

### Weyl's Law
- N(lambda) = C_d Vol(M) lambda^{d/2} + O(lambda^{(d-1)/2})
- Papers 02 (original statement), 05 (with corrections), 23 (sharp remainder, comprehensive)
- For spinors: multiply by 2^{n/2} (Paper 03)
- C_d = (2pi)^{-d} omega_d / Gamma(d/2+1) = 1/[(4pi)^{d/2} Gamma(d/2+1)]

### Spectral Action
- S = Tr(f(D/Lambda)) ~ sum_k f_k Lambda^{d-k} a_k(D^2)
- Papers 11 (principle), 19 (precision), 15 (expansion), 21 (matrix form), 27 (rationality), 29 (one-loop), 32 (comprehensive)
- f_k = int_0^inf f(v) v^{k-1} dv (moments of cutoff function)

### SU(3) Casimir and Eigenvalues
- Laplacian: lambda_{p,q} = 2(p^2+pq+q^2+3p+3q) (bi-invariant metric)
- Dimension: d_{p,q} = (p+1)(q+1)(p+q+2)/2
- Papers 04 (explicit), 25 (Duflo derivation), 26 (numerical tables)

### Eta Invariant and Spectral Flow
- eta(D) = sum sign(lambda_i)|lambda_i|^{-s} at s=0
- SF(D_0,D_1) = eta(D_0) - eta(D_1)
- Papers 09 (defining), 16 (equivariant version), 12 (in index formula)

### Ray-Singer Torsion
- log tau_RS = -sum_p (-1)^p p zeta_p'(0)
- Paper 08 (theorem: equals Reidemeister), 10 (on covers), 26 (on Lie groups)

### Spectral Rigidity
- Laplacian rigidity on simple Lie groups (naturally reductive): Paper 17
- Dirac rigidity on SU(2): Paper 18
- Inaudibility of natural reductivity: Paper 31 (COUNTEREXAMPLE)
- Tension: 17 proves rigidity WITHIN naturally reductive class; 31 shows you cannot tell from spectrum WHETHER you are in that class

---

## Notation Conventions

| Symbol | Meaning | Papers using |
|:-------|:--------|:-------------|
| a_k | Seeley-DeWitt coefficient (k-th order) | All heat kernel papers |
| D | Dirac operator | 01, 03, 11, 16, 18 |
| D_K | Dirac on M4 x SU(3) (Jensen-deformed) | Framework convention |
| R | Scalar curvature | All |
| Ric, R_{ij} | Ricci tensor | 01, 06, 08, 35 |
| Rm, R_{ijkl} | Riemann tensor | 01, 15, 16 |
| W | Weyl tensor (trace-free Riemann) | 35, 19 |
| eta(D) | Eta invariant | 09, 16 |
| tau_RS | Ray-Singer analytic torsion | 08, 10, 26 |
| zeta_P(s) | Spectral zeta function | 01, 02, 08, 14 |
| h(M) | Cheeger isoperimetric constant | 07 |
| d_s(t) | Spectral dimension | 22, 30 |
| C_2, lambda_rho | Casimir eigenvalue | 04, 25, 26 |
| d_rho | Representation dimension | 04, 25 |
| f_k | Cutoff function moments | 19, 21, 29, 32 |
| Lambda | Energy/UV cutoff scale | 11, 19, 21, 32 |

---

## Computational Verification Status

| Equation/Result | Paper Source | Verified in Framework | Session |
|:----------------|:------------|:---------------------|:--------|
| a_0 = Vol x spinor_rank | 01, 03 | YES (machine epsilon) | S20a |
| a_2 from scalar curvature | 01, 02, 15 | YES | S20a, S24a |
| a_4 quadratic curvature | 01, 03, 15 | YES (a_4/a_2 ~ 1000:1) | S20a, S24a |
| SU(3) Casimir lambda_{p,q} | 04, 25 | YES | S7-S12 |
| Weyl law on SU(3) spectrum | 02, 23 | YES (C_Weyl=42.80) | S36 |
| Spectral action monotonicity | 19, 29 | YES (structural theorem) | S37 |
| D^2 = nabla*nabla + R/4 | 16 | YES (Lichnerowicz check) | S35 |
| Cheeger bound lambda_1 >= h^2/4 | 07 | NOT YET COMPUTED | -- |
| eta(D_BdG) = 0 at mu=0 | 09 | YES (PH symmetry) | S35 |
| Spectral flow = 0 | 09 | YES (gap open) | S35 |
| Dirac rigidity on SU(3) | 17, 18 | OPEN (conjectured from SU(2)) | -- |
| Analytic torsion T(tau) | 08, 26 | OPEN (priority gate) | -- |
| Friedrich-Kirchberg bound | 35 | OPEN (need |W(tau)|^2) | -- |

---

## Key Structural Tensions

1. **Rigidity vs Inaudibility**: Papers 17-18 prove spectral rigidity for naturally reductive metrics on simple Lie groups (Laplacian and Dirac). Paper 31 proves natural reductivity itself is inaudible. Resolution: the framework's SU(3) IS naturally reductive by construction (left-invariant Jensen deformation), so rigidity applies. But this geometric fact cannot be read from the spectrum alone.

2. **Uncanny Precision vs Monotonicity**: Paper 19 shows a_4 = 0 on Einstein spaces, suggesting truncation at a_2 suffices. But Session 37 proved a_6 term (da_6/dtau = -1058) dominates the gradient for ALL smooth cutoffs. Resolution: precision holds for fixed geometry; monotonicity is about how coefficients vary with tau.

3. **Product Formula vs Jensen Deformation**: Paper 15 gives a_n(M1xM2) = sum a_i(M1)a_j(M2). But Jensen deformation breaks the product structure. The deformed D_K is NOT simply D_M4 tensor 1 + 1 tensor D_{SU(3)}, because the Jensen metric couples the two factors through the Kosmann lift. This tension is fundamental and unresolved.
