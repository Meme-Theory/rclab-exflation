# Spectral-Geometry Paper Index

**Collection**: Spectral Geometry — Heat Kernels, Eigenvalue Estimates, Spectral Invariants, and Noncommutative Geometry
**Papers**: 30 (1996-2025)
**Primary domain**: Heat kernel asymptotics, Seeley-DeWitt coefficients, Dirac eigenvalue estimates, spectral rigidity, analytic torsion, spectral action, cyclic cohomology, spectral dimension
**Project relevance**: The mathematical backbone of the M4 x SU(3) spectral triple. Every computation in the phonon-exflation framework --- from the Dirac spectrum on Jensen-deformed SU(3) through the spectral action expansion to the BDI topological classification --- rests on the spectral geometry results collected here. Papers 01, 02, 04, 10, 11, 16 are directly used in computation computations.
**Indexed**: 2026-03-27

---

## Dependency Graph

```
CORE HEAT KERNEL THEORY (a_0 through a_6, product formulas)
  01 (Vassilevich 2003) <-- definitive reference manual
  02 (Gilkey 2004) <-- handbook chapter, a_0--a_6 with full endomorphism E
  03 (Gusynin-Kornyak 1999) <-- E_4 for NONminimal operators
  01 --> 04 (Hong 2011): applies HK to compact Lie groups via Duflo
  01 --> 05 (Eckstein-Zajac 2014): rigorous Mellin-transform framework
  01 --> 22 (Fathizadeh-Khalkhali 2019): curvature on NC spaces via HK
  01 --> 23 (Fathizadeh et al. 2014): rationality of spectral action coefficients

EIGENVALUE ESTIMATES (Dirac spectral gap bounds)
  07 (Friedrich-Kirchberg 2001a) -- Ricci-dependent Dirac eigenvalue bound
  08 (Friedrich-Kirchberg 2001b) -- Weyl-tensor-dependent Dirac eigenvalue bound
  09 (De Ponti-Mondino 2019) -- sharp Cheeger-Buser for RCD spaces
  12 (Ivrii 2016) -- 100 years of Weyl's law (eigenvalue counting)
  30 (Capoferri-Vassiliev 2022) -- global Dirac propagator, Weyl coefficients
  07 --> 08 (same authors, complementary bounds)
  09 uses 12 (Weyl counting vs isoperimetric estimates)

SPECTRAL RIGIDITY AND INVERSE PROBLEMS
  10 (Gordon-Sutton 2010) -- spectral isolation of naturally reductive metrics on Lie groups
  11 (Kling-Schueth 2022) -- Dirac spectral rigidity on S^3 ~ SU(2)
  13 (Arias-Marco 2025) -- natural reductivity is INAUDIBLE (counterexample)
  10 --> 11 (S^3 inherits from general Lie group theory)
  10 <-> 13 (TENSION: isolation on simple groups vs inaudibility on nilmanifolds)

ANALYTIC TORSION AND ETA INVARIANTS
  14 (Lott 2023) -- Ray-Singer torsion survey, Cheeger-Muller theorem
  15 (Kirk-Lesch 2000) -- eta invariant gluing formula, Maslov index, spectral flow
  06 (Dodziuk-Mathai 1996) -- L^2 invariants, "not feeling the boundary"
  14 --> 15 (torsion -> eta invariant -> spectral flow chain)
  06 supports 14 (L^2 Betti numbers from heat kernel on coverings)

CONNES NCG FOUNDATIONS (reconstruction, cyclic cohomology, spectral standpoint)
  16 (Connes 2008) -- spectral characterization of manifolds (reconstruction theorem)
  17 (Khalkhali 2010) -- cyclic cohomology survey (HC, Chern character, local index)
  18 (Connes 2019) -- NCG from the spectral standpoint (overview)
  20 (Connes 2002) -- local index formula on SU_q(2)
  21 (Ponge-Wang 2014) -- conformal geometry, twisted spectral triples
  16 --> 18 (reconstruction theorem cited and contextualized)
  17 --> 20 (cyclic cohomology applied to quantum groups)
  16 --> 21 (reconstruction generalized to conformal/twisted setting)

NCG SPECTRAL ACTION AND PARTICLE PHYSICS
  19 (Chamseddine-Connes 2010) -- "Uncanny Precision" on S^3 x S^1
  24 (Chamseddine-Iliopoulos-vS 2020) -- spectral action in matrix form, Feynman rules
  25 (van Nuland-van Suijlekom 2022) -- one-loop spectral action renormalizability
  26 (Chamseddine-Connes-Marcolli 2007) -- SM with neutrino mixing from NCG
  27 (Chamseddine-Connes-vS 2013) -- beyond SM: Pati-Salam from relaxing first-order
  22 (Fathizadeh-Khalkhali 2019) -- curvature in NCG
  23 (Fathizadeh et al. 2014) -- rationality of spectral action for Robertson-Walker
  19 --> 24 (precision motivates matrix-form quantization)
  24 --> 25 (matrix form enables one-loop computation)
  26 --> 27 (SM -> Pati-Salam by relaxing order-one condition)

CDT AND SPECTRAL DIMENSION
  28 (Ambjorn-Loll 2024) -- CDT review: de Sitter emergence, d_S: 4 -> 2
  29 (Caceffo-Clemente 2023) -- CDT spectral analysis via FEM vs dual graph
  28 --> 29 (CDT lattice methods compared for spectral dimension)

MAJOR CROSS-TOPIC BRIDGES:
  01 (Vassilevich) bridges HK theory <-> NCG spectral action (a_k formulas)
  04 (Hong) bridges HK theory <-> Lie group spectra (Duflo, exact Lie group HK)
  10 (Gordon-Sutton) bridges rigidity <-> Lie group representation theory
  16 (Connes) bridges NCG foundations <-> reconstruction theorem <-> spectral action
  19 (CC Precision) bridges spectral action <-> physical predictions <-> HK coefficients
  25 (vN-vS) bridges spectral action <-> quantum field theory (one-loop)
  11 (Kling-Schueth) bridges eigenvalue estimates <-> rigidity on homogeneous spaces
```

---

## Topic Map

### A. Heat Kernel Asymptotics and Seeley-DeWitt Coefficients
Papers: 01, 02, 03, 04, 05, 22, 23
The foundational technology for spectral geometry. Papers 01 (Vassilevich) and 02 (Gilkey) provide the complete Seeley-DeWitt coefficients a_0 through a_6 for operators of Laplace type on closed manifolds with and without boundaries. Paper 03 (Gusynin-Kornyak) extends to nonminimal operators. Paper 04 (Hong) gives the exact heat kernel on compact Lie groups via the Duflo isomorphism --- the key result for SU(3). Paper 05 (Eckstein-Zajac) provides the rigorous Mellin-transform framework connecting heat traces to spectral zeta functions. Papers 22, 23 compute curvature and spectral action on noncommutative and Robertson-Walker spaces.

### B. Eigenvalue Estimates and Weyl Asymptotics
Papers: 07, 08, 09, 12, 30
Bounds on the Dirac and Laplace spectra from curvature data. Papers 07-08 (Friedrich-Kirchberg) give lower bounds on Dirac eigenvalues depending on the Ricci and Weyl tensors, generalizing the classical Friedrich and Lichnerowicz bounds used throughout the project. Paper 09 (De Ponti-Mondino) sharpens the Cheeger-Buser inequality with dimension-free constants. Paper 12 (Ivrii) surveys 100 years of Weyl's law. Paper 30 (Capoferri-Vassiliev) constructs the global Dirac propagator and computes third-order Weyl coefficients.

### C. Spectral Rigidity and Inverse Spectral Problems
Papers: 10, 11, 13
The question of whether the spectrum determines the geometry. Paper 10 (Gordon-Sutton) proves spectral isolation of naturally reductive metrics on compact simple Lie groups --- the mathematical basis for trusting that the spectral action on SU(3) faithfully encodes the fiber geometry. Paper 11 (Kling-Schueth) proves the stronger result that homogeneous metrics on S^3 are determined up to isometry by the Dirac spectrum. Paper 13 (Arias-Marco 2025) provides a counterexample: natural reductivity is inaudible on nilmanifolds. This tension (isolation on simple groups, inaudibility on nilmanifolds) is a structural boundary of the spectral approach.

### D. Analytic Torsion and Eta Invariants
Papers: 06, 14, 15
Spectral invariants beyond the heat trace. Paper 14 (Lott) surveys Ray-Singer analytic torsion and the Cheeger-Muller theorem equating analytic and combinatorial torsion. Paper 15 (Kirk-Lesch) develops the eta-invariant gluing formula with Maslov triple index and spectral flow. Paper 06 (Dodziuk-Mathai) proves L^2 invariant approximation from exhaustions, relevant to the fabric (spatially extended) limit. These papers underpin the project's eta-invariant computations (S60: eta = 0 exact) and the spectral flow analysis.

### E. Noncommutative Geometry Foundations
Papers: 16, 17, 18, 20, 21
The axiomatic framework. Paper 16 (Connes 2008) is the reconstruction theorem: five axioms on a commutative spectral triple characterize smooth compact manifolds. Paper 17 (Khalkhali) surveys cyclic cohomology and the Chern character. Paper 18 (Connes 2019) updates the NCG program including modular curvature, quantized volume, and the scaling site. Paper 20 (Connes 2002) works out the local index formula on SU_q(2) in full detail. Paper 21 (Ponge-Wang) extends to conformal geometry via twisted spectral triples.

### F. NCG Spectral Action and Particle Physics
Papers: 19, 22, 23, 24, 25, 26, 27
The spectral action principle and its predictions. Paper 19 (Chamseddine-Connes "Uncanny Precision") demonstrates that on S^3 x S^1, the spectral action is determined by a_0 + a_2 to 10^62 decimal places. Paper 24 (Chamseddine-Iliopoulos-vS) derives Feynman rules in matrix form preserving NCG structure. Paper 25 (van Nuland-vS) establishes one-loop renormalizability. Paper 26 (CCM 2007) derives the full SM with neutrino mixing from the spectral triple. Paper 27 (CC-vS 2013) extends to Pati-Salam by relaxing the order-one condition. Papers 22, 23 compute curvature and spectral action on NC spaces and Robertson-Walker metrics.

### G. CDT and Spectral Dimension
Papers: 28, 29
Lattice quantum gravity. Paper 28 (Ambjorn-Loll 2024) reviews CDT: emergence of de Sitter universe and spectral dimension flow d_S: 4 -> 2 from IR to UV. Paper 29 (Caceffo-Clemente 2023) compares dual graph and FEM methods for extracting the Laplace-Beltrami spectrum on simplicial manifolds, finding the dual graph method unreliable.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Seeley-DeWitt coefficients a_0, a_2, a_4 | 01, 02, 22 | CRITICAL |
| a_6 and higher coefficients | 01, 02, 23 | HIGH |
| Heat kernel on compact Lie groups / SU(3) | 04, 01 | CRITICAL |
| Nonminimal operators / gauge-fixing | 03 | HIGH |
| Heat trace convergence / zeta-function framework | 05 | MEDIUM |
| Dirac eigenvalue bounds (Friedrich/Lichnerowicz) | 07, 08 | HIGH |
| Cheeger-Buser inequality / isoperimetric bounds | 09 | MEDIUM |
| Weyl's law / eigenvalue counting | 12, 30 | HIGH |
| Spectral rigidity on Lie groups | 10, 11 | CRITICAL |
| Isospectral counterexamples | 13 | HIGH |
| Analytic torsion / Ray-Singer | 14 | HIGH |
| Eta invariant / spectral flow / gluing formulas | 15 | HIGH |
| L^2 invariants / exhaustion approximation | 06 | MEDIUM |
| Connes reconstruction theorem (5 axioms) | 16 | CRITICAL |
| Cyclic cohomology / Chern character | 17, 20 | MEDIUM |
| NCG overview / spectral standpoint | 18 | MEDIUM |
| Spectral action precision / S^3 x S^1 | 19 | HIGH |
| Local index formula (worked example) | 20 | MEDIUM |
| Twisted spectral triples / conformal invariance | 21 | MEDIUM |
| Curvature in NCG / NC torus | 22 | MEDIUM |
| Spectral action for Robertson-Walker | 23 | MEDIUM |
| Spectral action quantization / matrix Feynman rules | 24 | HIGH |
| One-loop renormalizability of spectral action | 25 | HIGH |
| SM from NCG (KO-dim 6, neutrino mixing) | 26 | MEDIUM |
| Pati-Salam from relaxed order-one condition | 27 | MEDIUM |
| CDT spectral dimension flow d_S: 4 -> 2 | 28 | MEDIUM |
| FEM vs dual-graph spectral methods on lattices | 29 | LOW |
| Dirac propagator / third Weyl coefficient | 30 | LOW |
| BDI classification / eta invariant on SU(3) | 15, 14, 16 | HIGH |
| Spectral action on M4 x F product geometry | 01, 19, 24, 26 | CRITICAL |
| Constant-ratio trap analysis | 12, 01, 02 | HIGH |
| Jensen fold spectral properties | 04, 10, 11, 07, 08 | CRITICAL |

---

## Paper Entries

### Paper 01: Heat kernel expansion: user's manual [CRITICAL]
- **File**: `01_2003_Vassilevich_Heat_Kernel_Expansion_Users_Manual.md`
- **arXiv**: hep-th/0306138
- **Year**: 2003
- **Authors**: D.V. Vassilevich
- **Relevance**: CRITICAL
- **Tags**: heat kernel, Seeley-DeWitt, a_0, a_2, a_4, a_6, boundary conditions, anomalies, Yang-Mills
- **Topic**: A

**Summary**: Definitive reference manual for heat kernel coefficients. Collects explicit formulas for a_0 through a_6 on manifolds with and without boundaries, for scalar, spinor, vector, and graviton fields. Covers Dirichlet, Neumann, Robin, mixed, spectral (APS) boundary conditions, and domain wall singularities. Derives conformal and chiral anomalies from heat kernel.

**Key Results**:
- Complete a_0 through a_6 for Laplace-type operators on closed manifolds (eqs. 4.26-4.29)
- All alpha_I constants are dimension-independent
- Product formula: a_k(D) = sum_{p+q=k} a_p(D_1) a_q(D_2)
- Yang-Mills beta function coefficient 11/3 from a_4
- Eta function eta(0, D-slash) measuring spectral asymmetry

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| a_0 | $(4\pi)^{-n/2}\int \text{tr}\{f\}\,dx$ | 4.26 |
| a_2 | $(4\pi)^{-n/2}\frac{1}{6}\int \text{tr}\{f(6E+R)\}\,dx$ | 4.27 |
| a_4 | $(4\pi)^{-n/2}\frac{1}{360}\int \text{tr}\{f(60E_{;kk}+60RE+180E^2+12R_{;kk}+5R^2-2R_{ij}^2+2R_{ijkl}^2+30\Omega_{ij}^2)\}\,dx$ | 4.28 |
| Product formula | $a_k(x;D)=\sum_{p+q=k}a_p(x_1;D_1)a_q(x_2;D_2)$ | 4.2 |

**Dependencies**: Upstream of nearly all other papers. 04, 19, 22, 23, 24, 25 all build on these formulas.

---

### Paper 02: The spectral geometry of operators of Dirac and Laplace type [CRITICAL]
- **File**: `02_2004_Gilkey_Spectral_Geometry_Dirac_Laplace_Type.md`
- **arXiv**: N/A (handbook chapter)
- **Year**: 2004
- **Authors**: P. Gilkey
- **Relevance**: CRITICAL
- **Tags**: Laplace type, Dirac type, Weitzenbock, Lichnerowicz, a_0-a_6, boundary, isospectrality
- **Topic**: A

**Summary**: Handbook chapter surveying operators of Laplace and Dirac type. Establishes unique decomposition D phi = -phi_{;ii} - E phi. Provides complete a_0 through a_6 (Theorem 3.2) with full E and Omega dependence. Reviews isospectrality: Milnor tori, Vigneras hyperbolic surfaces, spectral determination of constant curvature in dim <= 6. Complete boundary formulas through a_5.

**Key Results**:
- Unique decomposition D = -nabla*nabla - E (Lemma 2.1)
- a_0 through a_6 for general Laplace-type operators (Theorem 3.2)
- Leading behaviour of a_{2n} for all n (Theorem 3.3)
- Patodi formulas for form-valued Laplacians (Theorem 3.4)
- Spectral determination of constant curvature in dim <= 6 (Theorem 4.3)

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Lichnerowicz | $E = -\frac{1}{4}\tau\,\text{id}$ (spin Laplacian) | Sec. 2 |
| Weyl asymptotics | $\lambda_n \sim n^{2/m}$ | Thm 3.1 |
| Weitzenbock | $\Delta_M = \tilde\Delta_M + \frac{1}{2}\gamma(dx^\mu)\gamma(dx^\nu)R_{\mu\nu}$ | Sec. 2.1 |

**Dependencies**: Complements 01. Foundation for 04, 07, 08, 22.

---

### Paper 03: Complete Computation of DeWitt-Seeley-Gilkey E4 for Nonminimal Operator [HIGH]
- **File**: `03_1999_Gusynin_Kornyak_DeWitt_Seeley_Gilkey_E4.md`
- **arXiv**: math/9909145
- **Year**: 1999
- **Authors**: V.P. Gusynin, V.V. Kornyak
- **Relevance**: HIGH
- **Tags**: nonminimal operator, E_4, gauge fixing, hypergeometric, computer algebra
- **Topic**: A

**Summary**: First complete computation of the fourth heat kernel coefficient E_4 for the nonminimal operator A = -g^{mu nu} Box + a D^mu D^nu + X^{mu nu} in arbitrary dimension. Uses Widom's covariant symbolic calculus. The Lorentz trace has 13 invariant structures with rational coefficients depending on the nonminimality parameter a.

**Key Results**:
- Full E_4 for nonminimal operators (73 tensor terms, 43 scalar coefficients)
- tr_L E_4 in arbitrary dimension (13 invariant structures)
- Specialization to n = 4 with explicit coefficients
- Verification: a -> 0 recovers standard minimal operator results

**Dependencies**: Extends 01, 02 to nonminimal operators. Relevant when gauge-fixing terms break minimality.

---

### Paper 04: The Asymptotic Expansion of the Heat Kernel on a Compact Lie Group [CRITICAL]
- **File**: `04_2011_Hong_Heat_Kernel_Compact_Lie_Group.md`
- **arXiv**: 1111.2643
- **Year**: 2011
- **Authors**: Seunghun Hong
- **Relevance**: CRITICAL
- **Tags**: compact Lie group, bi-invariant metric, Duflo isomorphism, Casimir, heat trace, scalar curvature
- **Topic**: A

**Summary**: Computes the complete heat kernel and heat trace on compact Lie groups with bi-invariant metrics using the Duflo isomorphism. The heat kernel is k_t^exp ~ h_t / j * exp(tS/6), and the heat trace has the remarkably simple form Z(t) ~ vol(G) * exp(tS/6). All heat trace coefficients are determined in closed form: a_k = vol(G) * (S/6)^k / k!.

**Key Results**:
- Heat kernel controlled by Duflo j-function: k_t^exp ~ h_t/j * exp(tS/6)
- Heat trace: Z(t) ~ vol(G) * exp(tS/6)
- All coefficients: a_k = vol(G) * (S/6)^k / k!
- Scalar curvature: S = -(1/4) tr_g(Cas)
- Duflo: Duf(Delta_g) = Delta_G - <rho, rho>

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Laplacian = Casimir | $\Delta_G = \text{Cas}$ | 2.14 |
| j-function | $j(X) = \det^{1/2}(\sinh(\text{ad}_X/2)/(\text{ad}_X/2))$ | 2.18 |
| Heat trace | $Z(t) \sim \text{vol}(G)\,e^{tS/6}$ | Cor 3.10 |
| Scalar curvature | $S = -\frac{1}{4}\text{tr}_\mathfrak{g}(\text{Cas})$ | Lem 3.8 |

**Dependencies**: Uses 01, 02. Directly applicable to SU(3) with bi-invariant metric (tau = 0 limit). Essential benchmark for computation computations.

---

### Paper 05: Asymptotic and exact expansions of heat traces [MEDIUM]
- **File**: `05_2014_Eckstein_Zajac_Heat_Trace_Expansions.md`
- **arXiv**: 1412.5100
- **Year**: 2014
- **Authors**: M. Eckstein, A. Zajac
- **Relevance**: MEDIUM
- **Tags**: heat trace, Mellin transform, spectral zeta, convergence, asymptotic expansion
- **Topic**: A

**Summary**: Rigorous framework for heat trace asymptotics via inverse Mellin transform. Establishes necessary conditions for asymptotic expansion existence. Distinguishes asymptotic from convergent expansions. Recovers Seeley-DeWitt coefficients as residues of Gamma(s)*zeta_P(s).

**Key Results**:
- Heat trace decomposition via residues of Gamma(s)*zeta_P(s)
- Sufficient conditions for convergence of asymptotic expansions
- a_k(P) = Res_{s=(d-k)/2} Gamma(s) zeta_P(s)

**Dependencies**: Provides rigorous foundation for the zeta-function methods in 01, 14.

---

### Paper 06: Approximating L2 Invariants of Amenable Covering Spaces [MEDIUM]
- **File**: `06_1996_Dodziuk_Mathai_L2_Invariants_Heat_Kernel.md`
- **arXiv**: dg-ga/9609002
- **Year**: 1996
- **Authors**: J. Dodziuk, V. Mathai
- **Relevance**: MEDIUM
- **Tags**: L^2 Betti numbers, amenable covering, heat kernel, Kac principle, regular exhaustion
- **Topic**: D

**Summary**: Proves L^2 Betti numbers of amenable coverings are approximated from above by averaged Betti numbers of regular exhaustions. Uses generalization of Kac's "not feeling the boundary" principle. Extends to general spectral invariants including torsion and eta invariants.

**Key Results**:
- L^2 Betti approximation from regular exhaustions
- Generalized Kac "not feeling the boundary" principle
- Extends to torsion and eta invariants

**Dependencies**: Supports 14. Relevant to spatially extended fabric limit of SU(3) fiber.

---

### Paper 07: Eigenvalue estimates of the Dirac operator depending on the Ricci tensor [HIGH]
- **File**: `07_2001_Friedrich_Dirac_Eigenvalue_Ricci_Tensor.md`
- **arXiv**: math/0104121
- **Year**: 2001
- **Authors**: T. Friedrich, K.-D. Kirchberg
- **Relevance**: HIGH
- **Tags**: Dirac eigenvalue, Ricci tensor, Friedrich bound, Weitzenbock, harmonic curvature
- **Topic**: B

**Summary**: Proves new lower bound for Dirac eigenvalues depending on the Ricci tensor, not just scalar curvature. The one-parameter family Q^t provides refined Weitzenbock formulas. For harmonic curvature, the classical Friedrich bound lambda^2 >= nR_0/(4(n-1)) is improved by Ricci-dependent corrections.

**Key Results**:
- Ricci-dependent Dirac eigenvalue lower bound
- Recovery of Friedrich bound in Einstein case
- For R = 0, Ricci curvature alone bounds Dirac eigenvalues

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Friedrich bound | $\lambda^2 \geq \frac{nR_0}{4(n-1)}$ | Eq. 1 |
| Schrodinger-Lichnerowicz | $\nabla^*\nabla = D^2 - \frac{1}{4}R$ | Eq. 11 |

**Dependencies**: Extends 02. Companion to 08. Used in project's Kirchberg bound analysis (S52).

---

### Paper 08: Eigenvalue estimates for the Dirac operator depending on the Weyl tensor [HIGH]
- **File**: `08_2001_Friedrich_Kirchberg_Eigenvalue_Weyl_Tensor.md`
- **arXiv**: math/0105055
- **Year**: 2001
- **Authors**: T. Friedrich, K.-D. Kirchberg
- **Relevance**: HIGH
- **Tags**: Dirac eigenvalue, Weyl tensor, divergence-free, Einstein manifolds, symmetric spaces
- **Topic**: B

**Summary**: Proves Dirac eigenvalue bounds depending on the Weyl tensor for manifolds with divergence-free Weyl tensor. On Einstein manifolds (where div W = 0 automatically), gives explicit improvement over Friedrich bound. For symmetric spaces: nu_0 = (1/8)|W|^2. Combined Ricci+Weyl estimates for harmonic curvature.

**Key Results**:
- Weyl-tensor-dependent Dirac eigenvalue bound (Theorem 3.1)
- On symmetric spaces: nu_0 = (1/8)|W|^2
- Obstructs harmonic spinors when nu_0 > 0 on conformally Ricci-flat manifolds

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Main bound | $\lambda^2 \geq \frac{nR_0}{4(n-1)} + \frac{2\nu_0^2}{n\mu_0^2(R_0+\sqrt{R_0^2+\frac{n-1}{n}(4\nu_0/\mu_0)^2})}$ | Eq. 25 |

**Dependencies**: Companion to 07. Uses 02 (Weitzenbock formulas). Applied to SU(3) internal geometry.

---

### Paper 09: Sharp Cheeger-Buser Type Inequalities in RCD(K, infinity) Spaces [MEDIUM]
- **File**: `09_2019_DePonti_Mondino_Sharp_Cheeger_Buser.md`
- **arXiv**: 1902.03835
- **Year**: 2019
- **Authors**: N. De Ponti, A. Mondino
- **Relevance**: MEDIUM
- **Tags**: Cheeger constant, Buser inequality, spectral gap, RCD spaces, dimension-free
- **Topic**: B

**Summary**: Sharpens and generalizes the Cheeger-Buser inequalities relating the isoperimetric constant h to the first Laplacian eigenvalue lambda_1. Proves dimension-free sharp Buser inequality: lambda_1 <= -K + (pi/2)h^2 for RCD(K,infinity) spaces, with optimal constant pi/2 (equality on Gaussian space).

**Key Results**:
- Sharp dimension-free Buser: lambda_1 <= -K + (pi/2)h^2
- Cheeger: lambda_1 >= h^2/4
- Valid for non-smooth RCD spaces

**Dependencies**: Uses 12 (Weyl counting). Independent of Dirac-specific papers.

---

### Paper 10: Spectral Isolation of Naturally Reductive Metrics on Simple Lie Groups [CRITICAL]
- **File**: `10_2010_Gordon_Schueth_Sutton_Spectral_Isolation.md`
- **arXiv**: 0707.0853
- **Year**: 2010
- **Authors**: C.S. Gordon, C.J. Sutton
- **Relevance**: CRITICAL
- **Tags**: spectral isolation, naturally reductive, compact Lie group, isospectrality, Peter-Weyl, Casimir
- **Topic**: C

**Summary**: Proves every naturally reductive metric on a compact simple Lie group is spectrally isolated within the class of naturally reductive metrics (Theorem 4.1). Also proves finiteness of isospectral compact symmetric spaces (Corollary 2.6). Uses Peter-Weyl decomposition and Casimir eigenvalues. The proof exploits algebraic dependence of eigenvalues on metric parameters via the Weyl character formula.

**Key Results**:
- Spectral isolation of naturally reductive metrics on compact simple Lie groups
- Finiteness of isospectral compact symmetric spaces
- Bi-invariant metrics spectrally isolated among all left-invariant metrics
- Compact symmetric spaces finitely determined by volume + finite spectrum

**Dependencies**: Uses representation theory (Peter-Weyl, Weyl character formula). Foundation for 11. In TENSION with 13.

---

### Paper 11: On the Dirac Spectrum of Homogeneous 3-Spheres [CRITICAL]
- **File**: `11_2022_Boldt_Lauret_Dirac_Spectrum_Homogeneous.md`
- **arXiv**: 2204.12990
- **Year**: 2022
- **Authors**: J. Kling, D. Schueth
- **Relevance**: CRITICAL
- **Tags**: S^3, SU(2), Dirac spectrum, spectral rigidity, homogeneous metrics, Gershgorin, Frobenius
- **Topic**: C

**Summary**: Proves Dirac spectral rigidity for homogeneous metrics on S^3 ~ SU(2): the Dirac spectrum determines g_{abc} up to isometry (Theorem 1.2). Computes the fundamental tone explicitly: mu = a+b+c - C where C = (1/2)(ab/c + bc/a + ca/b). Uses Frobenius reciprocity decomposition and Gershgorin circle technique on pentadiagonal D_n^2 matrices.

**Key Results**:
- Dirac spectrum determines homogeneous metric on S^3 up to isometry
- Fundamental tone: mu = a+b+c - C for scal > 0
- Triangle Induction Lemma for Gershgorin estimates
- Explicit Frobenius decomposition of L^2(S^3, Sigma)

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Dirac operator | $(D\varphi)(x) = \sum e_\ell \cdot X_\ell(\varphi) + C\,e_1 e_2 e_3 \cdot\varphi$ | Eq. 1 |
| C definition | $C = \frac{1}{2}(ab/c + bc/a + ca/b)$ | Eq. 3 |
| Scalar curvature | $\text{scal} = 8(a^2+b^2+c^2-C^2)$ | Prop 2.11 |

**Dependencies**: Uses techniques from 10. Directly relevant to SU(3) Dirac spectrum at finite tau.

---

### Paper 12: 100 Years of Weyl's Law [HIGH]
- **File**: `12_2016_Ivrii_100_Years_Weyl_Law.md`
- **arXiv**: 1608.03963
- **Year**: 2016
- **Authors**: V. Ivrii
- **Relevance**: HIGH
- **Tags**: Weyl's law, eigenvalue asymptotics, sharp remainder, microlocal analysis, Dirac, magnetic Schrodinger
- **Topic**: B

**Summary**: Comprehensive survey of eigenvalue counting asymptotics from Weyl (1911) through Duistermaat-Guillemin sharp remainder (1975) to modern semiclassical microlocal analysis. Covers Weyl's law, Weyl's conjecture (boundary correction), Ivrii's theorem (periodic geodesic billiards), magnetic Schrodinger and Dirac operators, and applications to heavy atom ground states.

**Key Results**:
- N(lambda) = (2pi)^{-d} omega_d vol(X) lambda^{d/2} (1 + o(1))
- Weyl conjecture with boundary correction
- Duistermaat-Guillemin: o(lambda^{(d-1)/2}) remainder under non-periodicity
- Ivrii's theorem: Weyl conjecture holds under measure-zero periodic billiards

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Weyl's law | $N(\lambda) = (2\pi)^{-d}\omega_d\text{vol}(X)\lambda^{d/2}(1+o(1))$ | 1.1.1 |

**Dependencies**: Foundational for 09, 30. The constant-ratio trap (F/B = 0.55) is a direct consequence.

---

### Paper 13: Inaudibility of Naturally Reductive Property [HIGH]
- **File**: `13_2025_Arias_Marco_Inaudibility_Naturally_Reductive.md`
- **arXiv**: 2502.10332
- **Year**: 2025
- **Authors**: T. Arias-Marco, J.-M. Fernandez-Barroso
- **Relevance**: HIGH
- **Tags**: inaudible, naturally reductive, nilmanifold, isospectral, Ambrose-Singer
- **Topic**: C

**Summary**: Constructs an isospectral pair of 9-dimensional nilmanifolds where one is naturally reductive and the other is not, proving the naturally reductive property is inaudible to the Laplace spectrum. Uses Ambrose-Singer homogeneous structures and the Gordon-Wilson construction.

**Key Results**:
- Natural reductivity is inaudible (cannot be heard from the Laplace spectrum)
- Characterization of naturally reductive 2-step nilpotent Lie groups via Ambrose-Singer
- Type A characterization: J . j_{X^z} skew-symmetric

**Dependencies**: Structural tension with 10 (isolation on simple groups vs inaudibility on nilmanifolds). Relevant caveat for spectral approach.

---

### Paper 14: The Ray-Singer Torsion [HIGH]
- **File**: `14_2023_Lott_Ray_Singer_Torsion.md`
- **arXiv**: 2309.05688
- **Year**: 2023
- **Authors**: J. Lott
- **Relevance**: HIGH
- **Tags**: analytic torsion, Ray-Singer, Cheeger-Muller, zeta regularization, R-torsion, lens spaces
- **Topic**: D

**Summary**: Survey of Ray-Singer analytic torsion from R-torsion through the Cheeger-Muller theorem to modern developments. R-torsion classifies lens spaces; analytic torsion uses zeta-regularized determinants of Hodge Laplacians. Cheeger-Muller proves equality. Covers the determinant line bundle (Quillen) and holomorphic torsion forms.

**Key Results**:
- Ray-Singer torsion: T_RS = exp((1/2) sum (-1)^{q+1} q log det(Delta_q))
- Cheeger-Muller theorem: T_RS = T_{R-torsion}
- Minakshisundaram-Pleijel: zeta_Delta(s) meromorphic with poles at d/2 - j

**Dependencies**: Uses 05 (zeta-Mellin framework). Connects to 15 (eta invariant). Project's torsion computation (S52: T_singlet = 0.147).

---

### Paper 15: The Eta-Invariant, Maslov Index, and Spectral Flow [HIGH]
- **File**: `15_2000_Kirk_Lesch_Eta_Invariant_Spectral_Flow.md`
- **arXiv**: math/0012123
- **Year**: 2000
- **Authors**: P. Kirk, M. Lesch
- **Relevance**: HIGH
- **Tags**: eta invariant, Maslov index, spectral flow, gluing formula, APS, Calderon projector, Dirac
- **Topic**: D

**Summary**: Complete gluing formula for the eta invariant including the integer contribution via Maslov triple index. Proves spectral flow = Maslov index. Develops Calderon projector framework. Extends APS rho-invariant to manifolds with boundary. Non-additivity formula for signatures.

**Key Results**:
- Gluing formula: tilde{eta}(D,M) = tilde{eta}(D_P,M_+) + tilde{eta}(D_{I-P},M_-) - tau_mu(...)
- Spectral flow = Maslov index of Calderon projector path
- Extension of APS rho-invariant to manifolds with boundary

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Gluing formula | $\tilde\eta(D,M) = \tilde\eta(D_P,M_+) + \tilde\eta(D_{I-P},M_-) - \tau_\mu(I-P_{M_-},P,P_{M_+})$ | Thm 5.9 |

**Dependencies**: Uses 14 (torsion/zeta framework). Directly relevant to S60 eta invariant computation (eta = 0 exact).

---

### Paper 16: On the Spectral Characterization of Manifolds [CRITICAL]
- **File**: `16_2008_Connes_Spectral_Characterization_Manifolds.md`
- **arXiv**: 0810.2088
- **Year**: 2008
- **Authors**: A. Connes
- **Relevance**: CRITICAL
- **Tags**: reconstruction theorem, spectral triple, five axioms, smooth manifold, spin^c, Dixmier trace
- **Topic**: E

**Summary**: Proves the reconstruction theorem: five axioms (dimension, order one, regularity, orientability, finiteness/absolute continuity) on a commutative spectral triple characterize smooth compact oriented manifolds. With multiplicity 2^{p/2}, manifold is spin^c and D is of Dirac type. The proof uses exponentiation of dissipative derivations, Voiculescu obstruction, and the implicit function theorem.

**Key Results**:
- Reconstruction theorem: 5 axioms characterize smooth compact manifolds
- Spin^c characterization with multiplicity 2^{p/2}
- A is a Frechet pre-C*-algebra, separable nuclear space
- Smooth functional calculus stability

**Dependencies**: Foundation for 18, 21, 26, 27. The reconstruction theorem underpins the entire NCG approach.

---

### Paper 17: A Short Survey of Cyclic Cohomology [MEDIUM]
- **File**: `17_2010_Khalkhali_Short_Survey_Cyclic_Cohomology.md`
- **arXiv**: 1008.1212
- **Year**: 2010
- **Authors**: M. Khalkhali
- **Relevance**: MEDIUM
- **Tags**: cyclic cohomology, Hochschild, Chern character, K-homology, Fredholm module, local index
- **Topic**: E

**Summary**: Survey of cyclic cohomology: definition via cyclic subcomplex of Hochschild complex, Connes' long exact sequence (I, B, S operators), periodic cyclic cohomology HP^i, Connes-Chern character from K-homology, Fredholm index pairing, cyclic category Lambda, local index formula, Hopf cyclic cohomology.

**Key Results**:
- Cyclic cohomology as NC analog of de Rham homology
- Connes long exact sequence: HC^n -> HH^n -> HC^{n-1} -> HC^{n+1}
- Connes-Chern character: K-homology -> periodic cyclic cohomology
- For C^infty(V): cyclic cohomology recovers de Rham homology

**Dependencies**: Foundation for 20. Framework for Chern character in the project's BDI classification.

---

### Paper 18: Noncommutative Geometry, the Spectral Standpoint [MEDIUM]
- **File**: `18_2019_Connes_NCG_Spectral_Standpoint.md`
- **arXiv**: 1910.10407
- **Year**: 2019
- **Authors**: A. Connes
- **Relevance**: MEDIUM
- **Tags**: NCG overview, spectral paradigm, distance formula, inner fluctuations, modular curvature, quantized volume
- **Topic**: E

**Summary**: Updated overview of NCG from the spectral standpoint. Covers reconstruction theorem, Standard Model from A_F = M_2(H) + M_4(C) with KO-dimension 6, inner fluctuations D -> D + A + JAJ^{-1}, spectral action expansion, modular curvature on NC torus, quantized volume in dimension 4, and the scaling site for Riemann zeta zeros.

**Key Results**:
- SM from NCG: A_F = M_2(H) + M_4(C) with KO-dim 6
- Inner fluctuations generate gauge + Higgs
- Spectral action: Tr(f(D/Lambda)) ~ 2*Lambda^4*f_4*a_0 + 2*Lambda^2*f_2*a_2 + f_0*a_4
- Quantized volume: dimension 4 from simple equation

**Dependencies**: Builds on 16. Contextualizes 19, 26, 27.

---

### Paper 19: The Uncanny Precision of the Spectral Action [HIGH]
- **File**: `19_2010_Chamseddine_Connes_Uncanny_Precision.md`
- **arXiv**: 0812.0165
- **Year**: 2010
- **Authors**: A.H. Chamseddine, A. Connes
- **Relevance**: HIGH
- **Tags**: spectral action, S^3, S^3 x S^1, precision, vanishing coefficients, SM predictions, Higgs mass
- **Topic**: F

**Summary**: Demonstrates that on S^3 x S^1, the spectral action is determined by the first two terms (cosmological constant + scalar curvature) with an astronomically small correction (~10^{-62} precision). All higher Seeley-DeWitt coefficients a_{2n} (n >= 2) vanish, confirmed by local heat kernel computation. Derives full SM from A_F = M_2(H) + M_4(C) with Yukawa constraint Y^2 = 4g^2 at unification.

**Key Results**:
- Spectral action on S^3 x S^1: a_0 + a_2 gives full result to 10^62 places
- a_4 = a_6 = ... = 0 on S^3 x S^1 (remarkable cancellations)
- SM predictions: sin^2(theta_W) = 3/8, Yukawa Y^2 = 4g^2
- Higgs mass ~170 GeV (excluded, indicating new physics)

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Spectral action | $\text{Tr}(f(D/\Lambda)) \sim 2\Lambda^4 f_4 a_0 + 2\Lambda^2 f_2 a_2 + f_0 a_4$ | Eq. 8 |
| S^4 zeta | $\text{Tr}(\|D\|^{-s}) = \frac{4}{3}(\zeta(s-3)-\zeta(s-1))$ | Eq. 27 |

**Dependencies**: Uses 01, 02. Benchmark for project's spectral action computations on M4 x SU(3).

---

### Paper 20: Cyclic Cohomology, Quantum Group Symmetries and the Local Index Formula for SU_q(2) [MEDIUM]
- **File**: `20_2002_Connes_Cyclic_Cohomology_Local_Index_SUq2.md`
- **arXiv**: math/0209142
- **Year**: 2002
- **Authors**: A. Connes
- **Relevance**: MEDIUM
- **Tags**: SU_q(2), local index formula, cyclic cohomology, dimension spectrum, pseudodifferential, Dedekind eta
- **Topic**: E

**Summary**: Applies the Connes-Moscovici local index theorem to the Chakraborty-Pal spectral triple on SU_q(2). Computes the dimension spectrum ({1,2,3}, all simple), the local cyclic cocycle, and the eta-cochain via Dedekind eta function remainders. Develops the cosphere bundle, geodesic flow, and invariant cyclic cohomology for quantum group symmetries.

**Key Results**:
- Dimension spectrum of SU_q(2): {1, 2, 3}, simple
- Local index formula: explicit phi_1 and phi_3 components
- Cosphere bundle with geodesic flow
- Eta-cochain from Dedekind eta function

**Dependencies**: Uses 17 (cyclic cohomology). Structural analog of SU(3) computation.

---

### Paper 21: NCG and Conformal Geometry: Local Index Formula and Conformal Invariants [MEDIUM]
- **File**: `21_2014_Ponge_NCG_Conformal_Geometry_Local_Index.md`
- **arXiv**: 1411.3701
- **Year**: 2014
- **Authors**: R. Ponge, H. Wang
- **Relevance**: MEDIUM
- **Tags**: twisted spectral triple, conformal geometry, Connes-Chern character, conformal invariants, equivariant index
- **Topic**: E

**Summary**: Reformulates the local index formula for conformal geometry using twisted spectral triples. Proves the Connes-Chern character of the conformal Dirac spectral triple is an invariant of the conformal class (Theorem 7.7). Constructs new geometric conformal invariants from equivariant characteristic classes.

**Key Results**:
- Conformal invariance of Connes-Chern character
- Twisted commutator: [D, a]_sigma = Da - sigma(a)D
- sigma-connection formalism for conformal perturbations
- New conformal invariants from equivariant cycles

**Dependencies**: Extends 16 to conformal/twisted setting. Relevant to tau-dependent conformal-type deformations.

---

### Paper 22: Curvature in Noncommutative Geometry [MEDIUM]
- **File**: `22_2019_Fathizadeh_Khalkhali_Curvature_NCG.md`
- **arXiv**: 1901.07438
- **Year**: 2019
- **Authors**: F. Fathizadeh, M. Khalkhali
- **Relevance**: MEDIUM
- **Tags**: curvature, NC torus, Gauss-Bonnet, scalar curvature, modular automorphism, a_4
- **Topic**: F

**Summary**: Reviews computation of curvature invariants on noncommutative spaces via heat kernel asymptotics. Gauss-Bonnet theorem for NC 2-torus. Scalar curvature formulas involving modular automorphisms and divided differences. Extension to NC 4-tori (a_4 with Riemann tensor analogue), Ricci curvature, and matrix-valued metrics.

**Key Results**:
- Gauss-Bonnet for NC 2-torus with general conformal structures
- Scalar curvature involving modular automorphisms
- a_4 for NC 4-tori with Riemann tensor analogue
- Ricci curvature as spectral functional

**Dependencies**: Uses 01, 02 (Gilkey coefficients). Supports 23 (spectral action computations on curved NC spaces).

---

### Paper 23: Rationality of Spectral Action for Robertson-Walker Metrics [MEDIUM]
- **File**: `23_2014_Fathizadeh_Khalkhali_Rationality_Spectral_Action.md`
- **arXiv**: 1407.5972
- **Year**: 2014
- **Authors**: F. Fathizadeh, A. Ghorbanpour, M. Khalkhali
- **Relevance**: MEDIUM
- **Tags**: Robertson-Walker, spectral action, rationality, a_{12}, pseudodifferential, Hopf coordinates
- **Topic**: F

**Summary**: Proves the Chamseddine-Connes conjecture that all coefficients in a_{2n} for Robertson-Walker metrics are rational polynomials in the scale factor a(t) and its derivatives. Computes a_{12} for the first time and verifies a_8, a_{10} against earlier results. Derives recursive formula for leading derivative coefficient.

**Key Results**:
- Rationality theorem: a_{2n} = Q_{2n}(a, a', ..., a^{(2n)}) / a^{2n-3}, Q rational
- Computation of a_{12} for Robertson-Walker
- Recursive formula for highest-order derivative term

**Dependencies**: Uses 01 (heat kernel formulas). Extends 19 (spectral action computations).

---

### Paper 24: Spectral action in matrix form [HIGH]
- **File**: `24_2020_van_Suijlekom_Spectral_Action_Matrix_Form.md`
- **arXiv**: 2009.03367
- **Year**: 2020
- **Authors**: A.H. Chamseddine, J. Iliopoulos, W.D. van Suijlekom
- **Relevance**: HIGH
- **Tags**: spectral action, matrix form, Feynman rules, ribbon graphs, Yang-Mills, propagator, quantization
- **Topic**: F

**Summary**: Derives Feynman rules for the spectral action in matrix form, preserving the full NCG structure (Clifford and algebra indices). The unified propagator, cubic/quartic vertices, and ghost sector are expressed as ribbon graphs in one-to-one correspondence with Yang-Mills theory. Applied to a toy electroweak model yielding sin^2(theta_W) = 1/4 and lambda = g^2/12.

**Key Results**:
- Spectral action in unexpanded matrix form (Eq. 2)
- Unified matrix propagator via Gamma matrices encoding Clifford + algebra
- Feynman rules as ribbon graphs
- Cubic terms vanish up to total divergence
- Electroweak predictions from geometric constraints

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| Spectral data product | $D = i\gamma^\mu\partial_\mu \otimes 1 + \gamma_5 \otimes D_F$ | Eq. 1 |
| Unified propagator | $\langle A A\rangle = (\Gamma^{\tau I})(\Gamma^{\tau I})/p^2$ | Eq. 3 |

**Dependencies**: Uses 01, 19. Foundation for 25.

---

### Paper 25: One-Loop Corrections to the Spectral Action [HIGH]
- **File**: `25_2022_van_Nuland_van_Suijlekom_One_Loop_Spectral_Action.md`
- **arXiv**: 2107.08485
- **Year**: 2021
- **Authors**: T.D.H. van Nuland, W.D. van Suijlekom
- **Relevance**: HIGH
- **Tags**: one-loop, spectral action, renormalizability, Ward identity, Yang-Mills-Chern-Simons, random NCG
- **Topic**: F

**Summary**: Establishes one-loop renormalizability of the spectral action within the NCG framework. Perturbative expansion in terms of higher Yang-Mills and Chern-Simons forms. The gauge propagator G_{kl} = 1/f'[lambda_k, lambda_l] is bounded (unlike ordinary QFT). One-loop counterterms have the same YM-CS form as the classical action, enabling renormalization by transformation in the space of NC integrals.

**Key Results**:
- Spectral action expansion in higher YM-CS forms
- One-loop renormalizability within NCG framework
- Bounded gauge propagator (spectral regularization)
- Ward identities for both fermion and gauge propagators
- Counterterms have same form as classical action

**Key Equations**:

| Label | Equation | Ref |
|:---|:---|:---|
| YM-CS expansion | $S_D[V] = \sum_k(\int_{\psi_{2k-1}}\text{cs}_{2k-1}(A) + \frac{1}{2k}\int_{\phi_{2k}}F^k)$ | Eq. 7 |
| Gauge propagator | $G_{kl} = 1/f'[\lambda_k, \lambda_l]$ | Sec. 3 |

**Dependencies**: Builds on 24. Validates spectral action as quantum effective action.

---

### Paper 26: Gravity and the Standard Model with Neutrino Mixing [MEDIUM]
- **File**: `26_2007_Chamseddine_Connes_Marcolli_Neutrino_Mass.md`
- **arXiv**: hep-th/0610241
- **Year**: 2006
- **Authors**: A.H. Chamseddine, A. Connes, M. Marcolli
- **Relevance**: MEDIUM
- **Tags**: SM, neutrino mixing, KO-dim 6, see-saw, 31 parameters, A_F, spectral action
- **Topic**: F

**Summary**: Derives the full Standard Model with neutrino mixing from the spectral action on M x F with F of KO-dimension 6. The left-right algebra A_LR = C + H_L + H_R + M_3(C) reduces to A_F = C + H + M_3(C) via geometric constraints. 16 physical fermions per generation, see-saw mechanism, 31 real parameters in the Dirac operator.

**Key Results**:
- KO-dimension 6: J^2 = 1, JD = DJ, J gamma = -gamma J
- A_F = C + H + M_3(C) is unique maximal subalgebra
- 31 parameters in the finite Dirac operator
- Fermion-boson mass relation at unification

**Dependencies**: Uses 16 (reconstruction theorem). Foundation for 27.

---

### Paper 27: Beyond the Spectral Standard Model: Emergence of Pati-Salam Unification [MEDIUM]
- **File**: `27_2013_Chamseddine_Connes_vS_Pati_Salam.md`
- **arXiv**: 1304.8050
- **Year**: 2013
- **Authors**: A.H. Chamseddine, A. Connes, W.D. van Suijlekom
- **Relevance**: MEDIUM
- **Tags**: Pati-Salam, first order condition, quadratic fluctuations, SU(2)_R x SU(2)_L x SU(4), Higgs
- **Topic**: F

**Summary**: Relaxing the first order condition [[D,a],b^0]=0 in NCG leads to the Pati-Salam algebra H_R + H_L + M_4(C). Inner fluctuations acquire quadratic corrections forming a perturbation semigroup. Gauge group SU(2)_R x SU(2)_L x SU(4) with fundamental Higgs in (2,2,1), (2,1,4), (1,1,1+15).

**Key Results**:
- First-order relaxation uniquely gives Pati-Salam
- Quadratic inner fluctuations: D' = D + A^{(1)} + tilde{A}^{(1)} + A^{(2)}
- 16 fermions in (2,1,4) + (1,2,4)
- Correct truncation to SM

**Dependencies**: Extends 26. Relevant to early-universe (tau -> 0) physics.

---

### Paper 28: Causal Dynamical Triangulations: Gateway to Nonperturbative Quantum Gravity [MEDIUM]
- **File**: `28_2024_Ambjorn_Loll_CDT_Spectral_Dimension.md`
- **arXiv**: 2401.09399
- **Year**: 2024
- **Authors**: J. Ambjorn, R. Loll
- **Relevance**: MEDIUM
- **Tags**: CDT, spectral dimension, de Sitter, phase diagram, dimensional reduction, UV fixed point
- **Topic**: G

**Summary**: Review of CDT quantum gravity. Minkowskian building blocks with causal structure produce a nonperturbative path integral that yields an emergent de Sitter-like universe. Key discovery: spectral dimension flows from d_S ~ 4 at large scales to d_S ~ 2 at Planckian scales. Four-phase structure with second-order C_dS - C_b transition as UV fixed point candidate.

**Key Results**:
- Emergent 4D de Sitter universe
- Spectral dimension flow: d_S ~ 4 -> 2 from IR to UV
- Lorentzian and Euclidean path integrals are inequivalent
- Volume profile matches round S^4

**Dependencies**: Independent. Provides benchmark for spectral dimension predictions.

---

### Paper 29: Spectral Analysis of CDT via Finite Element Method [LOW]
- **File**: `29_2023_Coumbe_CDT_FEM_Spectral_Analysis.md`
- **arXiv**: 2010.07179
- **Year**: 2020
- **Authors**: F. Caceffo, G. Clemente
- **Relevance**: LOW
- **Tags**: CDT, FEM, dual graph, Laplace-Beltrami, spectral dimension, convergence
- **Topic**: G

**Summary**: Compares dual graph and FEM methods for extracting the Laplace-Beltrami spectrum on CDT simplicial manifolds. Shows dual graph Laplacian can give qualitatively wrong spectral dimensions on non-equilateral simplices. FEM provides convergent approximation with guaranteed convergence.

**Key Results**:
- Dual graph method unreliable on non-equilateral simplices
- FEM converges to exact LB spectrum
- Spectral dimensions from dual graph and FEM can disagree qualitatively

**Dependencies**: Uses 28 (CDT framework). Methodological caution.

---

### Paper 30: Global Propagator for the Massless Dirac Operator [LOW]
- **File**: `30_2022_Capoferri_Vassiliev_Dirac_Propagator.md`
- **arXiv**: 2004.06351
- **Year**: 2020
- **Authors**: M. Capoferri, D. Vassiliev
- **Relevance**: LOW
- **Tags**: Dirac propagator, oscillatory integral, Weyl coefficients, 3-manifold, complex-valued phase
- **Topic**: B

**Summary**: Constructs the global propagator for the massless Dirac operator on closed Riemannian 3-manifolds as a sum of two oscillatory integrals with complex-valued phase functions. Computes the third local Weyl coefficient c_0^{+/-} for the first time. Examples on S^3 and S^2 x S^1.

**Key Results**:
- Global U_pm(t) as invariantly defined oscillatory integrals
- Closed formula for principal symbols (Theorem 6.1)
- Third Weyl coefficient c_0^pm computed
- Small-time expansion in geometric invariants

**Dependencies**: Uses Weyl asymptotics (12). Specialized to 3-manifolds.

---

## Cross-Paper Equation Concordance

| Object | Vassilevich (01) | Gilkey (02) | Hong (04) | CC Precision (19) |
|:---|:---|:---|:---|:---|
| a_0 | Eq. 4.26 | Thm 3.2(1) | Cor 3.10 (vol(G)) | below Eq. 8 |
| a_2 | Eq. 4.27 | Thm 3.2(2) | a_1 = vol(G)*S/6 | below Eq. 8 |
| a_4 | Eq. 4.28 | Thm 3.2(3) | a_2 = vol(G)*(S/6)^2/2 | = 0 on S^3 x S^1 |
| Product formula | Eq. 4.2 | -- | -- | used implicitly |
| Spectral action | -- | -- | -- | Eq. 8 |

| Object | Friedrich-K (07) | Friedrich-K (08) | Kling-Schueth (11) |
|:---|:---|:---|:---|
| Dirac bound | lambda^2 >= nR_0/(4(n-1)) | + Weyl correction | mu = a+b+c-C |
| Lichnerowicz | Eq. 11 | via F decomposition | Sec. 1 |
| Harmonic curv. | required | div W = 0 | not needed |

| Object | Kirk-Lesch (15) | Lott (14) | Eckstein-Zajac (05) |
|:---|:---|:---|:---|
| Eta invariant | Thm 5.9 (gluing) | Sec. 4 (survey) | -- |
| Zeta function | via Calderon proj. | M-P zeta | Lemma 3.1 |
| Torsion | -- | Eq. 2.5, 2.8 | -- |
| Mellin relation | -- | Eq. 3.5 | Eq. 8 |

---

## Notation Conventions

| Symbol | Meaning | Conventions |
|:---|:---|:---|
| $(4\pi)^{-n/2}$ | Universal heat kernel prefactor | n = manifold dimension; d = 8 for SU(3) |
| $E$ | Bundle endomorphism | $D = -(g^{\mu\nu}\nabla_\mu\nabla_\nu + E)$ |
| $\Omega_{ij}$ | Bundle curvature | $\Omega_{ij} = \partial_i\omega_j - \partial_j\omega_i + [\omega_i,\omega_j]$ |
| $R, \tau$ | Scalar curvature | R (Vassilevich/FK), tau (Gilkey) -- SAME QUANTITY, different letters |
| $\rho, \text{Ric}$ | Ricci tensor | |Ric|^2 = R_{ij}R^{ij} |
| Cas | Casimir element | Delta_G = Cas for bi-invariant metrics (Hong) |
| $j(X)$ | Duflo j-function | $\det^{1/2}(\sinh(\text{ad}_X/2)/(\text{ad}_X/2))$ |
| $\tilde\eta$ | Reduced eta | $(\eta + \dim\ker D)/2$ |
| $f_k$ | Spectral action moments | $f_4 = \int_0^\infty f(u)u^3\,du$, etc. |
| KO-dim | KO-dimension | 6 for the finite geometry F; 10 = 4+6 for M x F |

**Sign convention warning**: Gilkey uses tau for scalar curvature where Vassilevich uses R. Both write a_2 = (1/6)(6E + R), but E has OPPOSITE SIGN in some conventions. Always check whether E = -R/4 or E = +R/4 for the spin Laplacian.

---

## Computational Verification Status

| Paper | Key formula | Verified in project? | Session |
|:---|:---|:---|:---|
| 01 | a_0, a_2, a_4 on SU(3) | YES | S20, S36-37 |
| 02 | Lichnerowicz E = -R/4 | YES | S48-49 (TT Lichnerowicz all positive) |
| 04 | Z(t) ~ vol(G)*exp(tS/6) for bi-invariant | YES (tau=0 limit) | S34 |
| 07 | Friedrich bound lambda^2 >= nR/(4(n-1)) | YES | S46, S52 (Kirchberg 5R/16 tighter) |
| 10 | Spectral isolation of bi-invariant SU(3) | CONSISTENT (no isospectral found) | S34 |
| 11 | Dirac rigidity on S^3 ~ SU(2) | ANALOG (SU(3) Frobenius decomposition matches) | S22b, S34 |
| 12 | Weyl's law N(lambda) ~ lambda^{d/2} | YES (d_Weyl = 6.81 at max_pq_sum=5) | S46 |
| 14 | Ray-Singer torsion | YES (T_singlet = 0.147, large T = artifact) | S45, S52 |
| 15 | Eta invariant | YES (eta = 0 exact, pair_err 2.22e-14) | S60 |
| 19 | a_4 = 0 on S^3 x S^1 | N/A (SU(3) has a_4 != 0) | -- |
| 28 | d_S: 4 -> 2 flow | PARTIAL (d_S = 1.73 peak on 32-cell TB) | S56, S59 |
