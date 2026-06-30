# Baptista Paper Index

**Researcher**: Joao Baptista (and related KK-NCG bridge authors)
**Papers**: 46 (1996-2026), all sourced from arXiv PDFs
**Primary domain**: Vortex moduli, Kaluza-Klein geometry on SU(3), NCG spectral action, Lichnerowicz stability, KK spectrometry
**Project relevance**: Core KK geometry for M4 x SU(3), spectral action bridge to NCG, gauge coupling extraction, Lichnerowicz stability of Einstein metrics, BCS on curved spaces, DESI w(z) observational test

---

## Dependency Graph

```
VORTEX FOUNDATIONS (Baptista 2003-2014)
  01 (Vortices S2) --> 03 (Topological gauged sigma)
  01 --> 04 (Abelian vortex eqs)
  02 (Kahler SL2C) --> 06 (Quantum equivariant cohomology)
  03 --> 05 (Twisting gauged sigma)
  04 --> 07 (Non-abelian vortices)
  04 --> 09 (L2 metric vortex moduli)
  04 --> 11 (Moduli abelian vortices Kahler)
  07 --> 08 (Hecke modifications, monopoles)
  07 --> 10 (Singular vortices, with Biswas)
  09 --> 12 (Vortices as degenerate metrics)
  11 --> 12

KK STANDARD MODEL GEOMETRY (Baptista 2021-2026) -- CRITICAL
  13 (HD Routes Bosons) --> 14 (HD Routes Fermions)
  13 --> 15 (Internal Symmetries KK)
  14 --> 15
  15 --> 16 (Test Particles KK)
  15 --> 17 (Chiral Interactions KK)
  16 --> 17
  17 --> 18 (CP Violation KK)

NCG SPECTRAL ACTION & KK-NCG BRIDGE
  19 (Chamseddine-Connes 1996) --> 21 (Entropy Spectral Action)
  19 --> 23 (Spectral Pati-Salam)
  19 --> 26 (Aydemir NCG-PS)
  20 (Brain-Mesland-vS Gauge Spectral) --> 21
  21 --> 31 (Dong-Khalkhali-vS Second Quantization)
  23 --> 26
  19 --> 27 (Barbier Exceptional Symmetries)

  13 <--> 19  [KK and NCG both produce SM from geometry]
  15 <--> 22  [Gauge thresholds in KK]
  15 <--> 24  [Gauge coupling evolution in 5D SU(3)]
  13 <--> 25  [Explicit KK reduction on S2 as simple analog]

STABILITY, SPECTROMETRY, HOLOGRAPHIC KK
  28 (Lauret Stability I) --> 29 (Lauret-Will Stability II)
  28 --> 30 (Schwahn Lichnerowicz Casimir)
  29 --> 30
  32 (Duboeuf-Malek Holographic RG S7) --> 33 (Duboeuf-Malek KK Spectrometry S7)
  33 --> 34 (Karlsson-Nilsson Complete S7 Spectra)
  33 --> 41 (Cesaro-Larios-Varela KK Spectroscopy)
  42 (Duff-Pope KK Supergravity Review) --> 34

GEOMETRIC ANALYSIS & DESI OBSERVATIONAL
  35 (Ricci Flow SU(3)/T) --> 36 (Cheeger Deformations Fiber Bundles)
  38 (Destabilising Warped Einstein) --> 28 [both use Lichnerowicz]
  39 (DESI DR1) --> 40 (DESI DR2)

SUPPLEMENTARY
  44 (Fatibene Lie Derivative Spinors) --> 17 [Kosmann lift foundation]
  45 (Derdzinski-Gal Indefinite Einstein) --> 46 (Derdzinski-Gal Curvature Spectra)
  45 <--> 28 [Einstein metric isolation and stability]
  37 (Hyperbolic BCS) --> 13 [BCS on curved internal space]
  43 (de Saxce Geometric Charge) --> 16 [test particle/charge in KK]

CROSS-THEME LINKS
  13,14,15 --[fiber geometry]--> 28,29,30 [stability of that geometry]
  13,14,15 --[spectral action]--> 19,21,31 [NCG functional on that geometry]
  15,16    --[dynamics]--> 32,33,34,41 [KK spectral evolution during deformation]
  17,18    --[fermion sector]--> 44 [Kosmann lift for spinors]
  39,40    --[observational]--> 13,15 [w(z) test of framework predictions]
```

## Topic Map

### Vortex Theory on Compact Surfaces
Papers: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12
Baptista's early program (2003-2014) developing the mathematical theory of vortex moduli spaces on compact Kahler manifolds. Covers abelian and non-abelian vortices, gauged sigma models, topological field theories, L2 metrics, singular vortices, and the reinterpretation of vortices as degenerate metrics. Establishes the gauge-theoretic toolkit later applied to Kaluza-Klein geometry.

### Kaluza-Klein Standard Model from SU(3) Geometry
Papers: 13, 14, 15, 16, 17, 18
The CRITICAL core of the collection. Baptista's KK program (2021-2026) showing that the Einstein-Hilbert action on M4 x SU(3) with left-invariant metrics produces the full Standard Model: gauge bosons, Higgs mechanism, fermionic generations, chiral interactions, CP violation. Paper 13 derives the bosonic sector. Paper 14 encodes one generation in a single 12D spinor. Papers 15-18 develop massive gauge bosons from non-Killing fields, geodesic mass/charge variation, chiral fermion interactions via Kosmann-Lichnerowicz, and geometric CP violation.

### NCG Spectral Action Principle
Papers: 19, 21, 31
The spectral action Tr(chi(D/Lambda)) from Chamseddine-Connes (1996) through entropy-spectral action duality (2018) to second quantization with chemical potential (2019). Paper 19 establishes the spectral action and derives the SM coupled to gravity. Paper 21 identifies entropy as a spectral action with test function related to the Riemann zeta function. Paper 31 extends to both bosonic and fermionic second quantization with Bessel function coefficients.

### Gauge Theory from Noncommutative Geometry
Papers: 20, 23, 26, 27
Connecting gauge fields to spectral triples. Paper 20: unbounded Kasparov product for KK-factorization. Paper 23: spectral Pati-Salam gauge coupling unification. Paper 26: NCG-PS phenomenology and leptoquark. Paper 27: nonassociative spectral geometry with exceptional G2 x G2 symmetry.

### KK Threshold Corrections and Gauge Coupling Evolution
Papers: 22, 24, 25
Paper 22: one-loop KK thresholds on warped AdS5. Paper 24: gauge coupling evolution for 5D SU(3) on S1/Z2, with sin^2(theta_W) = 3/4 from group theory. Paper 25: explicit 6D gravity reduction on M4 x S2, revealing rank-2 gauge kinetic matrix from coset structure.

### Lichnerowicz Stability of Einstein Metrics
Papers: 28, 29, 30, 38
The stability trilogy plus warped product destabilization. Papers 28-29 derive the Lichnerowicz Laplacian on G-invariant TT-tensors via moment maps and structural constants. Paper 30 gives an exact Casimir formula, producing 107 new stable Einstein metrics. Paper 38 proves all warped products in dim <= 6 are unstable.

### KK Spectrometry on Squashed S7
Papers: 32, 33, 34, 41, 42
Full KK spectral analysis of squashed S7 using Exceptional Field Theory. Papers 32-33: holographic RG flow and universal conformal dimension formula. Paper 34: complete spectrum with spin-3/2 and supermultiplet assignment. Paper 41: five N=1 solutions on S7 and S6. Paper 42: 40-year review of KK supergravity.

### Einstein Metric Isolation on SU(n)
Papers: 45, 46
Derdzinski-Gal: positive-definite Killing form multiples are isolated among Riemannian Einstein metrics on SU(n). Paper 46: curvature operator spectrum for SU(3) is {2, 1, -2/3} with multiplicities {1, 8, 18}. Eigenvalue 1 produces only indefinite deformations.

### Ricci Flow and Cheeger Deformations
Papers: 35, 36
Ricci flow on SU(3)/T (four Einstein attractors, bi-invariant is global attractor) and Cheeger deformation theory on fiber bundles (convergence to totally geodesic fibers).

### BCS on Curved Spaces, DESI Observations, Miscellaneous
Papers: 37 (BCS on hyperbolic spaces), 39-40 (DESI DR1/DR2 BAO), 43 (geometric charge from coadjoint orbits), 44 (Lie derivative for spinors via Kosmann lift)

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Dirac operator D_K on SU(3), Jensen deformation, tau-evolution | 13, 14, 15, 17 | CRITICAL |
| Gauge boson masses, Higgs mechanism from geometry | 13, 15, 16 | CRITICAL |
| Fermionic sector, chiral interactions, CP violation | 14, 17, 18 | CRITICAL |
| Spectral action Tr chi(D/Lambda), heat kernel coefficients | 19, 21, 31 | CRITICAL |
| Lichnerowicz stability of Einstein metrics on SU(3) | 28, 29, 30 | CRITICAL |
| Kosmann-Lichnerowicz derivative of spinors | 17, 18, 44 | CRITICAL |
| Einstein metric isolation/rigidity on SU(n) | 45, 46 | HIGH |
| KK spectrometry, ExFT mass operators, squashed S7 | 32, 33, 34, 41, 42 | HIGH |
| NCG gauge fields, Kasparov product, Pati-Salam | 20, 23, 26, 27 | HIGH |
| Gauge coupling running, threshold corrections | 22, 24, 25 | HIGH |
| DESI w(z) constraints, dynamical dark energy | 39, 40 | HIGH |
| BCS on curved space, gap equation from DOS | 37 | MEDIUM |
| Ricci flow, Cheeger deformations, geometric charge | 35, 36, 43 | MEDIUM |
| Vortex moduli spaces, gauged sigma models | 01-12 | LOW |

---

## Paper Entries

### Paper 01: The dynamics of vortices on S2 near the Bradlow limit
- **File**: `01_2003_Baptista_Manton_Vortices_S2_Bradlow.md`
- **arXiv**: hep-th/0208001
- **Year**: 2003
- **Relevance**: LOW
- **Tags**: vortex, S2, Bradlow limit, Fubini-Study, geodesic approximation, CP^N

**Summary**: Constructs approximate vortex solutions on S2 near the Bradlow limit R^2 ~ N. The moduli space is CP^N with L2 metric proportional to Fubini-Study. All geodesics explicitly parametrized with at most 2N-2 collisions per period.

**Key Results**:
- Moduli space metric: m = 2pi(R^2 - N) m_FS
- Collision bound: at most 2N-2 per period via intersection theory
- Right-angle scattering for head-on 2-vortex collision

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (2) | Bogomolny equations | Sec. 2 |
| Sec. 4 | m = 2pi(R^2-N) m_FS | Sec. 4 |

**Dependencies**: Upstream of 03, 04

---

### Paper 02: Some special Kahler metrics on SL(2,C)
- **File**: `02_2004_Baptista_Kahler_Metrics_SL2C.md`
- **arXiv**: math-ph/0306060
- **Year**: 2004
- **Relevance**: LOW
- **Tags**: Kahler, SL(2,C), Stenzel, holomorphic quantization, Stein manifold

**Summary**: Studies SU(2)xSU(2)-invariant Kahler metrics on SL(2,C) via global potential f(y). Recovers Stenzel and 1-lump metrics. Holomorphic quantization dimension matches semiclassical predictions.

**Key Results**:
- Global Kahler potential: omega = (i/2) d-bar d(f o y)
- Volume: vol(M_r) = (1/3)(pi f'(r))^3
- Conjectural dim_C H_poly ~ Omega/(2pi hbar)^3

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Prop 2.3 | Invariant Kahler form | Prop 2.3 |
| Prop 3.2 | Scalar curvature from f | Prop 3.2 |

**Dependencies**: Upstream of 06

---

### Paper 03: A topological gauged sigma-model
- **File**: `03_2005_Baptista_Topological_Gauged_Sigma.md`
- **arXiv**: hep-th/0502152
- **Year**: 2005
- **Relevance**: LOW
- **Tags**: topological field theory, gauged sigma model, Hamiltonian GW invariants

**Summary**: Cohomological TFT for gauged nonlinear sigma models, unifying topological sigma-model and topological Yang-Mills. Localizes to vortex moduli; computes Hamiltonian Gromov-Witten invariants.

**Key Results**:
- Gauged A-model localizes to vortex moduli space
- Adiabatic limit connects to GW invariants on X//G

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (8a-c) | Vortex equations | Sec. 2 |

**Dependencies**: From 01; upstream of 05

---

### Paper 04: Vortex equations in abelian gauged sigma-models
- **File**: `04_2006_Baptista_Vortex_Abelian_Gauged_Sigma.md`
- **arXiv**: math/0411517
- **Year**: 2006
- **Relevance**: LOW
- **Tags**: vortex, abelian, torus action, moment polytope, Bradlow bound

**Summary**: Complete moduli space and energy spectrum for vortex equations with torus gauge group on C^n and CP^n targets. Solution space interplays with moment polytope geometry.

**Key Results**:
- Complete solution space for T^n on C^n and CP^n
- Energy topological: E = T[phi] at vortex solutions

**Dependencies**: From 01; upstream of 07, 09, 11

---

### Paper 05: Twisting gauged non-linear sigma-models
- **File**: `05_2008_Baptista_Twisting_Gauged_Sigma.md`
- **arXiv**: 0707.2786
- **Year**: 2008
- **Relevance**: LOW
- **Tags**: gauged A-model, gauged B-model, equivariant CY, mirror symmetry

**Summary**: A and B twists of N=2 gauged sigma models. B-model exists when c_1^G(X)=0 and localizes to X//G. Connects to gauged CY/LG correspondence.

**Key Results**:
- Gauged B-model requires equivariantly CY condition
- Localizes to Kahler quotient X//G

**Dependencies**: From 03

---

### Paper 06: Quantum equivariant cohomology of toric manifolds
- **File**: `06_2009_Baptista_Quantum_Equivariant_Cohomology.md`
- **arXiv**: 0806.2091
- **Year**: 2009
- **Relevance**: LOW
- **Tags**: quantum equivariant cohomology, toric, Hori-Vafa mirror symmetry

**Summary**: Computes QH*_T(X) for toric manifolds via Hori-Vafa mirror symmetry. Toric flop invariance.

**Dependencies**: From 02

---

### Paper 07: Non-abelian vortices on compact Riemann surfaces
- **File**: `07_2009_Baptista_Non_Abelian_Vortices_Riemann.md`
- **arXiv**: 0810.3220
- **Year**: 2009
- **Relevance**: LOW
- **Tags**: non-abelian vortex, U(N), factorization, internal structure

**Summary**: Characterizes U(N) vortex solutions via local factorization theorem. Internal structures I_N (sequences of subspaces) parametrize solutions. Spaces I_{N,k} are compact and connected.

**Key Results**:
- Theorem 1.3: bijection between vortex solutions and {(z_j, I^j_N)}
- I_{N,1} = CP^{N-1}

**Dependencies**: From 04; upstream of 08, 10

---

### Paper 08: Non-abelian vortices, Hecke modifications and singular monopoles
- **File**: `08_2010_Baptista_Hecke_Modifications_Monopoles.md`
- **arXiv**: 0907.1752
- **Year**: 2010
- **Relevance**: LOW
- **Tags**: Hecke modification, Kapustin-Witten, singular monopole

**Summary**: Vortex internal structures = Hecke modifications of vector bundles. Through Kapustin-Witten, vortex moduli isomorphic to singular monopole moduli on I x C.

**Dependencies**: From 07

---

### Paper 09: On the L2-metric of vortex moduli spaces
- **File**: `09_2011_Baptista_L2_Metric_Vortex_Moduli.md`
- **arXiv**: 1003.1296
- **Year**: 2011
- **Relevance**: LOW
- **Tags**: L2 metric, Kahler class, Samols localization

**Summary**: Kahler form of L2 metric on vortex moduli. Explicit Kahler class for abelian GLSM. Extends Samols localization to toric sigma models. Conjectural volume formulae for holomorphic map spaces.

**Dependencies**: From 04; upstream of 12

---

### Paper 10: Abelian vortices with singularities
- **File**: `10_2013_Baptista_Biswas_Singular_Vortices.md`
- **arXiv**: 1207.0863
- **Year**: 2013
- **Relevance**: LOW
- **Tags**: singular vortex, parabolic structure, conical singularity

**Summary**: Vortex equations on line bundles with parabolic structure over singular Riemann surfaces. Moduli space preserved (same as regular case). Explicit solutions on thrice-punctured sphere.

**Dependencies**: From 07

---

### Paper 11: Moduli Spaces of Abelian Vortices on Kahler Manifolds
- **File**: `11_2012_Baptista_Moduli_Abelian_Vortices_Kahler.md`
- **arXiv**: 1211.0012
- **Year**: 2012
- **Relevance**: LOW
- **Tags**: Kahler, higher-dimensional, Hitchin-Kobayashi, GLSM, Fourier-Mukai

**Summary**: Most complete treatment of abelian vortex moduli on higher-dimensional Kahler manifolds. Establishes Hitchin-Kobayashi for general abelian GLSM. GLSM moduli compactifies holomorphic map spaces.

**Dependencies**: From 04; upstream of 12

---

### Paper 12: Vortices as degenerate metrics
- **File**: `12_2014_Baptista_Vortices_Degenerate_Metrics.md`
- **arXiv**: 1212.3561
- **Year**: 2014
- **Relevance**: LOW
- **Tags**: degenerate metric, Hermitian-Einstein, superposition, constant scalar curvature

**Summary**: Abelian vortices reinterpreted as degenerate Kahler metrics satisfying a curvature equation. Nonlinear superposition rule. Modified vortex equation = constant scalar curvature condition. Higher-dimensional extension to Hermitian-Einstein invariance.

**Key Results**:
- omega' = tau^{-1}|phi|^2 omega preserves curvature equation
- Volume reduction: Vol' = Vol - 2pi/(e^2 tau) sum n_j

**Dependencies**: From 09, 11

---

### Paper 13: Higher-dimensional routes to the Standard Model bosons
- **File**: `13_2021_Baptista_HD_Routes_SM_Bosons.md`
- **arXiv**: 2105.02899
- **Year**: 2021
- **Relevance**: CRITICAL
- **Tags**: Kaluza-Klein, SU(3), left-invariant metric, Higgs, Yang-Mills, gauge coupling, spontaneous symmetry breaking

**Summary**: Einstein-Hilbert action on M4 x SU(3) with phi-deformed left-invariant metric produces after fiber integration: Yang-Mills terms, Higgs covariant derivative |d_A phi|^2, and double-well potential V(|phi|^2). The Higgs field phi in C^2 is the metric deformation parameter with correct U(2) representation. Generalized model with lambda_1, lambda_2, lambda_3 gives M_Z/M_W = sqrt(1 + 3 lambda_2/lambda_1).

**Key Results**:
- 4D Lagrangian: R_M f - (1/4)B|F|^2 - C|d_A phi|^2 - V(|phi|^2)
- R_{g_phi} = 3(4-25|phi|^2+33|phi|^4-8|phi|^6)/[lambda(1-|phi|^2)^2(1-4|phi|^2)]
- vol_{g_phi} = (1-|phi|^2)sqrt(1-4|phi|^2) vol_beta
- g'/2 = sqrt(3/lambda_1), g/2 = 1/sqrt(lambda_2), g_s from lambda_1+3lambda_2+4lambda_3
- d_A phi couples to electroweak A_L but NOT strong A_R

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (2.25) | Deformed metric g_phi on SU(3) | Eq. (2.25) |
| eq (2.37) | Volume form ratio | Eq. (2.37) |
| eq (2.40) | Scalar curvature R_{g_phi} | Eq. (2.40) |
| eq (3.41) | Full 4D Lagrangian | Eq. (3.41) |
| eq (5.21) | Gauge coupling constants | Eq. (5.21) |
| eq (5.25) | Z/W mass ratio | Eq. (5.25) |
| eq (5.27) | |S|^2 from Lie derivatives of fiber metric | Eq. (5.27) |

**Dependencies**: Foundational for 14, 15

---

### Paper 14: Higher-dimensional routes to the Standard Model fermions
- **File**: `14_2021_Baptista_HD_Routes_SM_Fermions.md`
- **arXiv**: 2105.02901
- **Year**: 2021
- **Relevance**: CRITICAL
- **Tags**: spinor, 12D, fermion generation, chiral, gauge representation, Dirac operator

**Summary**: One generation of SM fermions (16 Weyl spinors) in a single 64-component 12D spinor (8x8 matrix). Vertical behavior S(h) produces exact chiral SM gauge representations after fiber integration. Right-handed neutrino decouples from all gauge fields. Closure defect: rho^L not a homomorphism on su(3), only on u(2)+su(3).

**Key Results**:
- Delta_12 = M_{8x8}(C): complete generation in 8x8 matrix
- S(h) = [[s(h),0],[0,h]] with s(h) = sqrt(2)(h^T h)_{11}
- D: quarks (SU(3) fundamental); b: leptons (no color); c: u_R; a: nu_R (sterile)
- Normalization zeta = 4/3

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (2.15)-(2.16) | Vertical transformation S(h) | Eqs. (2.15)-(2.16) |
| eq (2.62) | Gauge representations rho^L, rho^R | Eq. (2.62) |
| eq (2.65) | Closure defect | Eq. (2.65) |
| eq (2.66) | Full fermion identification matrix | Eq. (2.66) |
| eq (3.6) | Internal Dirac operator D_K | Eq. (3.6) |

**Dependencies**: From 13; upstream of 15

---

### Paper 15: Internal symmetries in Kaluza-Klein models
- **File**: `15_2024_Baptista_Internal_Symmetries_KK.md`
- **arXiv**: 2306.01049
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: gauge boson mass, Lie derivative, Einstein instability, Jensen deformation, sigma model, universal spinor

**Summary**: Gauge fields from non-isometric diffeomorphisms produce massive bosons with mass^2 ~ ||L_e g_K||^2. Product Einstein metrics with positive curvature ALWAYS unstable. For K = SU(3): Jensen TT-deformation breaks SU(3)xSU(3) -> SU(3)xSU(2)xU(1). Internal metric g_K = gauged sigma-model field.

**Key Results**:
- Mass formula: (Mass A^a)^2 ~ integral <L_{e_a} g_K, L_{e_a} g_K> / (2 integral g_K(e_a,e_a))
- Product Einstein metrics always unstable
- Jensen breaks SU(3)xSU(3)/Z_3 -> SU(3)xSU(2)xU(1)/Z_6
- Non-Killing gauge fields evade Atiyah-Hirzebruch no-go

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (3.7) | Gauge boson mass from Lie derivative | Eq. (3.7) |
| eq (1.5) | Action: R_M + R_K - |F|^2/4 - |d_A g_K|^2/4 | Eq. (1.5) |
| eq (3.19) | TT-tensor and scalar mode masses | Eq. (3.19) |

**Dependencies**: From 13, 14; upstream of 16, 17

---

### Paper 16: Test particles in Kaluza-Klein models
- **File**: `16_2024_Baptista_Test_Particles_KK.md`
- **arXiv**: 2406.09503
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: geodesic, mass variation, charge variation, null geodesic, submersion

**Summary**: Geodesic motion on M4 x K: rest mass varies when traversing regions with massive gauge fields (dm^2/ds = -(d_A g_K)(p_V,p_V)). Charge conserved only in massless-gauge sectors. Null geodesic interpretation: mass = internal kinetic energy.

**Key Results**:
- Mass variation: dm^2/ds = -(d_A g_K)(p_V, p_V)
- Charge: dq_xi/ds = A^a g_P([xi, e_a], p)
- Massless 4D particles cannot interact with gauge fields

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (1.2) | Mass variation formula | Eq. (1.2) |
| eq (1.6) | Charge definition q_xi | Eq. (1.6) |
| Sec. 9 | Null geodesic condition | Sec. 9 |

**Dependencies**: From 15; upstream of 17

---

### Paper 17: Chiral interactions of fermions and massive gauge fields in KK
- **File**: `17_2025_Baptista_Chiral_Interactions_KK.md`
- **arXiv**: 2506.09126
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: Dirac operator, Kosmann-Lichnerowicz, chirality, massive gauge boson, anomaly-free

**Summary**: Non-Killing gauge fields automatically produce: massive bosons, mass mixing, chiral couplings. 4D Dirac equation involves Kosmann-Lichnerowicz derivative L_X. The commutator [/D_K, L_X] != 0 for non-Killing X is the chirality mechanism. Representations always anomaly-free.

**Key Results**:
- /D_P = kinetic + gauge via L_{e_a} + D_K + Pauli term
- [/D, L_X] != 0 for non-Killing X produces chirality
- Anomaly-free: conjugate pairs have equal multiplicity

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (3.8) | Dirac operator on P decomposition | Eq. (3.8) |
| eq (4.1) | Kosmann-Lichnerowicz derivative | Eq. (4.1) |
| eq (4.7) | Commutator [/D, L_X] | Eq. (4.7) |
| eq (6.6) | Chiral asymmetry formula | Eq. (6.6) |

**Dependencies**: From 15, 16, 44; upstream of 18

---

### Paper 18: The geometry of CP violation in Kaluza-Klein models
- **File**: `18_2026_Baptista_CP_Violation_KK.md`
- **arXiv**: 2601.08902
- **Year**: 2026
- **Relevance**: CRITICAL
- **Tags**: CP violation, misalignment, tau-correction, Pauli term, new Lie derivative, fermion generations

**Summary**: Three geometric CP violation sources: (1) /D-eigenspinor vs representation basis misalignment, (2) tau-correction from non-isometric action, (3) non-abelian Pauli term. New Lie derivative L_V satisfying closure for non-isometric actions. Fermion generations from splitting degenerate /D-eigenspaces.

**Key Results**:
- New L_V = L_V + (1/4) correction via averaged metric g_hat
- Closure: [L_U, L_V] = L_{[U,V]}
- Generations from symmetry breaking of degenerate /D eigenspaces
- Anomaly-free: n_{m,pi} = n_{m,pi_bar}

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (1.4)/(5.10) | New Lie derivative L_V | Eqs. (1.4), (5.10) |
| eq (5.5) | Closure relation | Eq. (5.5) |
| eq (5.6) | Averaged metric g_hat | Eq. (5.6) |
| eq (6.4) | Chiral decomposition | Eq. (6.4) |

**Dependencies**: From 17

---

### Paper 19: The Spectral Action Principle
- **File**: `19_1996_Chamseddine_Connes_Spectral_Action.md`
- **arXiv**: hep-th/9606001
- **Year**: 1996
- **Relevance**: CRITICAL
- **Tags**: spectral action, NCG, Standard Model, gravity, heat kernel, gauge unification

**Summary**: Tr chi(D/Lambda) + (psi, D psi) as universal action for NCG. Applied to M x F with A_F = C + H + M_3(C), reproduces SM + Einstein-Weyl gravity. Unification: g_3^2 = g_2^2 = (5/3)g_1^2. Higgs mass 160-180 GeV.

**Key Results**:
- Spectral action reproduces SM + gravity
- Heat expansion: Tr chi(P) ~ f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4
- Conformal Higgs coupling xi_0 = 1/6; bare R^2 coupling b_0 = 0

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (1.28) | Spectral action | Eq. (1.28) |
| eq (2.14)-(2.16) | Heat expansion and Seeley-DeWitt a_0, a_2, a_4 | Eqs. (2.14)-(2.16) |
| eq (3.18) | Gauge unification | Eq. (3.18) |

**Dependencies**: Upstream of 21, 23, 26, 27

---

### Paper 20: Gauge Theory for Spectral Triples and the Unbounded Kasparov Product
- **File**: `20_2016_Brain_Mesland_vS_Gauge_Spectral_Triples.md`
- **arXiv**: 1306.1951
- **Year**: 2016
- **Relevance**: HIGH
- **Tags**: Kasparov product, Hilbert bundle, inner fluctuations, gauge group

**Summary**: Gauge group of spectral triple = unitary endomorphisms of Hilbert bundle when factored over commutative base via unbounded Kasparov product. Inner fluctuations split into connections + endomorphisms.

**Dependencies**: Upstream of 21

---

### Paper 21: Entropy and the Spectral Action
- **File**: `21_2018_Chamseddine_Connes_vS_Entropy_Spectral_Action.md`
- **arXiv**: 1809.02944
- **Year**: 2018
- **Relevance**: CRITICAL
- **Tags**: von Neumann entropy, spectral action, Riemann zeta, KMS state

**Summary**: Von Neumann entropy of fermionic second quantization IS a spectral action: S = Tr(h(beta D)) with h(x) = x/(1+e^x) + log(1+e^{-x}). Coefficients gamma(a) = (1-2^{-2a})/a pi^{-a} xi(2a). Dimension 4: a_2 involves zeta(3), a_4 involves zeta(5).

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Thm 3.4 | Entropy = spectral action | Thm. 3.4 |
| Lemma 4.6 | gamma(a) via Riemann xi | Lemma 4.6 |

**Dependencies**: From 19, 20; upstream of 31

---

### Paper 22: Gauge Threshold Corrections in Warped Geometry
- **File**: `22_2010_Choi_Kim_Shin_Warped_Thresholds.md`
- **arXiv**: 1001.1473
- **Year**: 2010
- **Relevance**: HIGH
- **Tags**: warped, KK thresholds, AdS5, orbifold

**Summary**: Complete one-loop KK thresholds for 5D on AdS5 slice. All field types, arbitrary boundary conditions. Warped enhancement ~ pi k R.

**Dependencies**: Related to 15, 24

---

### Paper 23: Grand Unification in the Spectral Pati-Salam Model
- **File**: `23_2015_Spectral_Pati_Salam.md`
- **arXiv**: 1507.08161
- **Year**: 2015
- **Relevance**: HIGH
- **Tags**: Pati-Salam, NCG, gauge unification, scalar content

**Summary**: Three NCG Pati-Salam variants all achieve gauge coupling unification. Scalar content determined by D, not freely chosen. 16 Weyl fermions per family.

**Dependencies**: From 19

---

### Paper 24: Gauge Coupling Evolution in 5D SU(3)
- **File**: `24_2016_Gauge_Coupling_5D_Weinberg.md`
- **arXiv**: 1602.07441
- **Year**: 2016
- **Relevance**: HIGH
- **Tags**: SU(3), gauge-Higgs, orbifold, Weinberg angle

**Summary**: 5D SU(3) on S1/Z2. Orbifold breaks SU(3)->SU(2)xU(1). Higgs from A^a_5. sin^2(theta_W) = 3/4 from group theory.

**Dependencies**: Related to 15, 22

---

### Paper 25: Explicit KK Reduction of Einstein Gravity on S2
- **File**: `25_2026_KK_Reduction_Einstein_S2.md`
- **arXiv**: 2601.08443
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: M4 x S2, gauge kinetic matrix, coset, breathing mode

**Summary**: 6D Einstein gravity on M4 x S2. Only 2 of 3 gauge fields propagate (rank-2 kinetic matrix from SO(3)/SO(2) coset). Scalar breathing mode with positive kinetic term.

**Dependencies**: Related to 13 (simple analog)

---

### Paper 26: Unified Pati-Salam from NCG
- **File**: `26_2025_Aydemir_Pati_Salam_NCG.md`
- **arXiv**: 2511.07672
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: Pati-Salam, leptoquark, proton stability

**Summary**: NCG-PS models require gauge unification. S1 leptoquark has no diquark couplings (proton stable from geometry). Restricted scalar content.

**Dependencies**: From 19, 23

---

### Paper 27: Spectral Geometry with Exceptional Symmetries
- **File**: `27_2025_Barbier_Exceptional_Symmetries_Spectral.md`
- **arXiv**: 2506.21496
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: nonassociative, G2, octonion, charged Higgs, bimodule

**Summary**: Constructs spectral geometries with G2 x G2 symmetry using octonion algebras. Novel "reconstituted derivation bimodule" produces charged Higgs via specialization identity L_{ab} = L_a L_b + [L_a, R_b].

**Dependencies**: From 19 (extending NCG beyond associative)

---

### Paper 28: On the Stability of Homogeneous Einstein Manifolds (Part I)
- **File**: `28_2021_Lauret_Stability_Homogeneous_Einstein_I.md`
- **arXiv**: 2105.06336
- **Year**: 2021
- **Relevance**: CRITICAL
- **Tags**: Lichnerowicz Laplacian, moment map, GIT, Jensen G-unstable

**Summary**: Universal L_p formula via moment map for G-invariant TT-tensors. Killing metrics: all G-stable except SU(n>=3) (neutrally stable) and Sp(n>=2) (G-unstable). All Jensen Einstein metrics are G-unstable with coindex r.

**Key Results**:
- <L_p A, A> = (1/2)|theta(A) mu_p|^2 + 2 tr(M_{mu_p} A^2)
- Matrix formula [L_p]_{kk}, [L_p]_{jk} from structural constants [ijk]
- Jensen metrics: G-unstable, local minima of Sc

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (1) | Main L_p formula | Eq. (1) |
| eq (2) | Naturally reductive L_p as Casimir | Eq. (2) |
| eq (3) | Matrix formula from [ijk] | Eq. (3) |

**Dependencies**: Upstream of 29, 30

---

### Paper 29: On the Stability of Homogeneous Einstein Manifolds (Part II)
- **File**: `29_2021_Lauret_Stability_Homogeneous_Einstein_II.md`
- **arXiv**: 2107.00354
- **Year**: 2021
- **Relevance**: CRITICAL
- **Tags**: Wallach space, flag manifold, structural constants, SU(n)/T

**Summary**: Explicit L_p formula for ANY G-invariant metric via structural constants and metric coefficients x_i. Computes Lichnerowicz spectrum for all Einstein metrics on generalized Wallach spaces and flag manifolds with b_2=1. SU(3)/T: G-unstable, coindex 2, local minimum.

**Key Results**:
- Theorem 3.1: universal L_p for any metric
- SU(3)/T standard metric: coindex 2, local minimum
- All Einstein metrics are G-non-degenerate (G-rigid)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Thm 3.1 | L_p diagonal/off-diagonal from [ijk] and x_i | Thm. 3.1 |
| eq (18) | Ricci eigenvalue formula | Eq. (18) |
| eq (19) | Scalar curvature | Eq. (19) |

**Dependencies**: From 28; upstream of 30

---

### Paper 30: The Lichnerowicz Laplacian on Normal Homogeneous Spaces
- **File**: `30_2023_Schwahn_Lichnerowicz_Laplacian_Homogeneous.md`
- **arXiv**: 2304.10607
- **Year**: 2023
- **Relevance**: CRITICAL
- **Tags**: exact Casimir formula, 107 stable examples, crude estimate

**Summary**: Exact Casimir formula for Delta_L on normal homogeneous spaces (representation theory only). Crude and refined estimates guarantee finitely many candidate destabilizing modes. 107 new stable positive-curvature Einstein metrics.

**Key Results**:
- Delta_L = (3/2)Cas^g_ell + corrections (Cor. 3.5)
- Crude estimate: finitely many destabilizing candidates (Thm 3.6)
- 107 new stable Einstein metrics

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Cor. 3.5 | Main Casimir formula for Delta_L | Cor. 3.5 |
| Thm 3.6 | Crude estimate lower bound | Thm. 3.6 |

**Dependencies**: From 28, 29

---

### Paper 31: Second Quantization and the Spectral Action
- **File**: `31_2019_Dong_Khalkhali_vS_Second_Quantization_Spectral.md`
- **arXiv**: 1903.09624
- **Year**: 2019
- **Relevance**: HIGH
- **Tags**: second quantization, chemical potential, Bessel functions, entropy

**Summary**: Bosonic and fermionic entropy/energy from second-quantized spectral triples are spectral actions with modified Bessel function coefficients. mu->0 recovers CCS zeta function result. Chemical potential essential for bosonic case.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Prop 3.4 | gamma_mu(a) via Bessel K_nu | Prop. 3.4 |
| Lemma 3.6 | mu->0 recovery of CCS | Lemma 3.6 |

**Dependencies**: From 21

---

### Paper 32: Holographic RG Flow from Squashed to Round S7
- **File**: `32_2023_Duboeuf_Holographic_RG_Squashed_S7.md`
- **arXiv**: 2306.11789
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: domain wall, squashed S7, ExFT, KK couplings, RG flow

**Summary**: Domain wall in D=11 SUGRA connecting N=1 squashed (UV) to N=8 round (IR) S7. No superpotential for full flow. ExFT quadratic KK couplings along domain wall. Universal conformal dimension formula.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (2.4) | D=4 potential V(u,v) | Eq. (2.4) |
| eq (4.3) | Universal Delta formula | Eq. (4.3) |

**Dependencies**: Upstream of 33

---

### Paper 33: KK Spectrometry beyond Consistent Truncations: Squashed S7
- **File**: `33_2022_Duboeuf_Malek_KK_Spectrometry_S7.md`
- **arXiv**: 2212.01135
- **Year**: 2022
- **Relevance**: HIGH
- **Tags**: ExFT, universal formula, beyond consistent truncation

**Summary**: First full KK spectrum beyond consistent truncations. Universal formula: Delta = 1 + (5/3)s + (1/3)sqrt{(3J+2s^2)^2 + 5C_3}. Complete N=1 and N=0 spectra. Marginal operators eliminated by boundary conditions.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (1.1) | Universal conformal dimension formula | Eq. (1.1) |
| eq (3.11) | Spin-0 mass operator | Eq. (3.11) |

**Dependencies**: From 32; upstream of 34

---

### Paper 34: Complete KK Spectra on Squashed S7
- **File**: `34_2023_Malek_Nicolai_Complete_KK_Spectra_S7.md`
- **arXiv**: 2305.00916
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: spin-3/2, supermultiplets, boundary conditions, swampland

**Summary**: Completes squashed S7 spectrum with spin-3/2 eigenvalues. Novel algebraic approach via weak G_2 holonomy. N=1 supermultiplet content: 1 graviton + 6 gravitino + 6 vector B + 8 vector A + 14 WZ towers.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (2.9) | Universal Laplacian | Eq. (2.9) |
| eq (2.15) | Coset master equation | Eq. (2.15) |

**Dependencies**: From 33

---

### Paper 35: Ricci Flow on SU(3)/T Flag Manifold
- **File**: `35_2009_Martins_Grama_Ricci_Flow_SU3_Flag.md`
- **arXiv**: 0903.2761
- **Year**: 2009
- **Relevance**: MEDIUM
- **Tags**: Ricci flow, SU(3)/T, flag manifold, Einstein attractor, Lyapunov

**Summary**: Four invariant lines for Ricci flow on SU(3)/T, each with an Einstein attractor. Bi-invariant metric is global attractor. All Lyapunov exponents negative. No finite-time singularities.

**Dependencies**: Related to 36

---

### Paper 36: Cheeger Deformations on Fiber Bundles
- **File**: `36_2018_Cavenaghi_Cheeger_Deformations_Fiber_Bundles.md`
- **arXiv**: 1801.06576
- **Year**: 2018
- **Relevance**: MEDIUM
- **Tags**: Cheeger deformation, fiber bundle, sectional curvature, regularization

**Summary**: Sectional curvature = base Cheeger + fiber + non-negative remainder. Convergence to totally geodesic fibers after rescaling. Re-proves Schwachhofer-Tuschmann and Fukaya-Yamaguchi results.

**Dependencies**: Related to 35

---

### Paper 37: Superconductivity in Hyperbolic Spaces
- **File**: `37_2025_Hyperbolic_BCS_Curved_Space.md`
- **arXiv**: 2510.26528
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: BCS, hyperbolic, Cayley tree, boundary superconductivity, two T_c

**Summary**: BCS on negatively curved geometries. Two critical temperatures: T_c^edge > T_c^bulk from boundary LDOS enhancement. Curvature enters gap equation solely through DOS.

**Dependencies**: Related to 13 (BCS on curved internal space)

---

### Paper 38: Destabilising Compact Warped Product Einstein Manifolds
- **File**: `38_2016_Semmelmann_Weingart_Destabilising_Einstein.md`
- **arXiv**: 1607.05766
- **Year**: 2016
- **Relevance**: HIGH
- **Tags**: warped product, Ricci-flow unstable, GHP variation, fiber instability

**Summary**: All warped products in dim <= 6 are Ricci flow unstable (Thm A). Ricci variation destabilizes when quasi-Einstein converges to soliton (Thm B). Fiber with Lichnerowicz eigentensor kappa < mu makes warped product unstable (Thm C). Product fibers and Kahler-Einstein with h^{1,1}>1 always unstable.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (4.1) | GHP variation | Eq. (4.1) |
| Prop 2.5 | Black hole instability criterion | Prop. 2.5 |

**Dependencies**: Related to 28

---

### Paper 39: DESI DR1 BAO Cosmological Constraints
- **File**: `39_2024_DESI_DR1_BAO_Cosmological_Constraints.md`
- **arXiv**: 2404.03002
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: DESI, BAO, dark energy, w0wa, neutrino mass

**Summary**: DESI DR1 from 6+ million objects. LCDM: Omega_m = 0.295+/-0.015. In w0waCDM: w0>-1, wa<0 (Quintom B) at 2.5-3.9 sigma. sum m_nu < 0.072 eV.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Sec. 5.2 | CPL: w(a) = w0 + wa(1-a) | Sec. 5.2 |
| Table 3 | Best fit w0, wa values | Table 3 |

**Dependencies**: Upstream of 40

---

### Paper 40: DESI DR2 Dynamical Dark Energy
- **File**: `40_2025_DESI_DR2_Dynamical_Dark_Energy.md`
- **arXiv**: 2504.06118
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: DR2, non-parametric w(z), Bayesian evidence, Quintom B

**Summary**: DR2 does not diminish dynamical DE signal. w(z) varies: w>-1 at z<0.2, w<-1 at z~0.75. Bayesian evidence: Delta ln E = 5.2+/-0.7 (moderate support). SNR = 4.5. Three PCA degrees of freedom.

**Dependencies**: From 39

---

### Paper 41: Supersymmetric Spectroscopy on S7 and S6
- **File**: `41_2021_Cesaro_Larios_Varela_KK_Spectroscopy_S7_S6.md`
- **arXiv**: 2103.13408
- **Year**: 2021
- **Relevance**: HIGH
- **Tags**: ExFT, KK spectrum, N=1, AdS4, supermultiplet

**Summary**: Complete KK spectra for five N=1 AdS4 solutions via ExFT. No master formula for N=1 spectra. Non-monotonic minimal scalar dimensions in some spectra.

**Dependencies**: From 33

---

### Paper 42: Kaluza-Klein Supergravity 2025 (Review)
- **File**: `42_2025_Duff_Pope_KK_Supergravity_Review.md`
- **arXiv**: 2502.07710
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: KK SUGRA, holonomy, skew-whiffing, stability, consistent truncation, ExFT

**Summary**: 40-year review: round S7 (N=8), squashed (N=1), skew-whiffed (N=0). Holonomy determines SUSY. Stability: Delta_L >= 3m^2. Product manifolds always unstable. Right-squashed S7 not proven unstable.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (20) | Stability mass M^2 = Delta_L - 4m^2 | Eq. (20) |
| eq (39) | Universal Laplacian on squashed S7 | Eq. (39) |

**Dependencies**: From 34

---

### Paper 43: Electric? Then it is geometric
- **File**: `43_2025_de_Saxce_Geometric_Charge_KK.md`
- **arXiv**: 2503.08718
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: coadjoint orbit, Souriau, geometric charge, 4+1 symmetry breaking

**Summary**: KK from coadjoint orbit method. Charge NOT invariant in SO(1,4); IS invariant in degenerate G0 (shrunk fifth dimension). Lorentz force from parallel transport; Maxwell from 5D Palatini.

**Dependencies**: Related to 16

---

### Paper 44: Geometric definition of Lie derivative for Spinor Fields
- **File**: `44_1996_Fatibene_Lie_Derivative_Spinors.md`
- **arXiv**: gr-qc/9608003
- **Year**: 1996
- **Relevance**: MEDIUM
- **Tags**: Kosmann lift, Lie derivative, spinor, gauge-natural bundle

**Summary**: Rigorous Lie derivative for spinors via gauge-natural bundles. Kosmann lift is unique but NOT a Lie algebra homomorphism (discrepancy involves L_xi g, vanishes for Killing).

**Key Results**:
- L_xi psi = xi^a nabla_a psi - (1/4) nabla_{[a}xi_{b]} gamma^a gamma^b psi
- Non-homomorphism: [xi,zeta]_K != [xi_K, zeta_K] unless Killing

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (3.19) | Kosmann Lie derivative | Eq. (3.19) |
| eq (3.18) | Non-homomorphism relation | Eq. (3.18) |

**Dependencies**: Foundational for 17

---

### Paper 45: Indefinite Einstein Metrics on Simple Lie Groups
- **File**: `45_2012_Derdzinski_Gal_Indefinite_Einstein_Metrics.md`
- **arXiv**: 1209.6084
- **Year**: 2012
- **Relevance**: MEDIUM-HIGH
- **Tags**: Einstein metric, isolation, SU(n), Killing form

**Summary**: On SU(n): positive-definite Killing form multiples are ISOLATED among left-invariant Riemannian Einstein metrics (dim C = 0). For SU(l,j) with j>=1: moduli dim = 2lj (indefinite only). All other simple groups: D isolated.

**Key Results**:
- Theorem 22.3: Killing form isolated on SU(n) (dim C = 0)
- Einstein family: C = D + pi_S({I_a[u] : a^2 = 0}); for SU(n), a^2=0 => a=0

**Dependencies**: Upstream of 46; related to 28

---

### Paper 46: Curvature Spectra of Simple Lie Groups
- **File**: `46_2013_Derdzinski_Gal_Curvature_Spectra_Lie_Groups.md`
- **arXiv**: 1304.2801
- **Year**: 2013
- **Relevance**: MEDIUM-HIGH
- **Tags**: curvature operator, Meyberg theorem, SU(3) spectrum, Cartan three-form

**Summary**: Curvature operator Omega spectrum for all simple Lie groups via Meyberg's theorem. For SU(3): eigenvalues {2, 1, -2/3}, multiplicities {1, 8, 18}. Eigenvalue 1 only for sl(n)-type; produces indefinite deformations only. Cartan three-form determines su(n).

**Key Results**:
- SU(3): Omega eigenvalues {2, 1, -2/3} with multiplicities {1, 8, 18}
- Theorem A: 2 Pi Lambda = -(Omega + Id)(Omega - 2 Id)
- Cartan three-form rigidity for dim > 6

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq (1.2) | Curvature operator Omega | Eq. (1.2) |
| eq (7.3) | Meyberg exceptional spectrum | Eq. (7.3) |
| Thm A | 2 Pi Lambda = -(Omega+Id)(Omega-2Id) | Theorem A |

**Dependencies**: From 45

---

## Cross-Paper Equation Concordance

### The Scalar Curvature of Left-Invariant Metrics on SU(3)
- **Paper 13 eq (2.40)**: R_{g_phi} = 3(4-25|phi|^2+33|phi|^4-8|phi|^6)/[lambda(1-|phi|^2)^2(1-4|phi|^2)]
- **Paper 15 eq (3.70)**: R_{beta_tilde} = 3(1/lambda_2 + 4/lambda_3 - (lambda_1+lambda_2)/(2 lambda_3^2)) -- three-parameter generalization
- **Paper 29 eq (19)**: Sc(g) = (1/2) sum b_k d_k/x_k - (1/4) sum [ijk] x_k/(x_i x_j) -- universal structural constants formula

### The Gauge Boson Mass Formula
- **Paper 13 eq (4.11)**: M_W^2 specific to phi-deformation
- **Paper 15 eq (3.7)**: (Mass A^a)^2 = integral <L_{e_a} g_K, L_{e_a} g_K> / (2 integral g_K(e_a,e_a)) -- general formula
- **Papers 16 eq (1.4), 17 eq (1.2), 18 eq (1.2)**: same general formula reaffirmed in successive contexts

### The Covariant Derivative d_A g_K
- **Paper 13 eq (5.27)**: |S|^2 = (1/4)<L_{X_mu} g_phi, L_{X_nu} g_phi> + gauge terms
- **Paper 15 below eq (1.5)**: (d_A g_K)_X(U,V) = (L_X g_K)(U,V) + A^a(X)(L_{e_a} g_K)(U,V)
- **Paper 16 eq (1.3)**: same definition; drives mass variation dm^2/ds

### The Kosmann-Lichnerowicz Derivative
- **Paper 17 eq (4.1)**: L_X psi = nabla_X psi - (1/8)[g(nabla_{v_r}X,v_s)-g(nabla_{v_s}X,v_r)] v_i.v_j.psi
- **Paper 18 eq (1.3)**: same, plus new L_V with closure correction
- **Paper 44 eq (3.19)**: L_xi psi = xi^a nabla_a psi - (1/4) nabla_{[a}xi_{b]} gamma^a gamma^b psi (original derivation)
- **Closure defect**: Paper 14 eq (2.65) and Paper 17 eq (4.11) give the same algebraic obstruction; Paper 18 resolves it via averaged metric g_hat

### The Spectral Action Heat Kernel Expansion
- **Paper 19 eq (2.14)-(2.16)**: Tr chi(P) ~ f_0 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_4 a_4
- **Paper 21 Thm 3.4**: entropy test function h(x) = E(e^{-x}) -- canonical choice
- **Paper 31 Prop 3.4**: gamma_mu(a) via modified Bessel K_nu -- chemical potential extension
- **Paper 33 eq (3.11)**: mass operator for ExFT KK fluctuations -- ExFT analog of heat kernel

### The Lichnerowicz Laplacian
- **Paper 28 eq (1)**: <L_p A,A> = (1/2)|theta(A)mu_p|^2 + 2 tr(M_{mu_p} A^2) -- moment map formula
- **Paper 29 Thm 3.1**: [L_p]_{kk}, [L_p]_{km} from [ijk] and x_i -- explicit matrix
- **Paper 30 Cor 3.5**: Delta_L = (3/2)Cas^g_ell + corrections -- exact Casimir
- **Paper 42 eq (20)**: M^2 = Delta_L - 4m^2 -- Freund-Rubin stability mass
- **Paper 38 eq (2.5)**: Delta_L in warped product destabilization context

### The Curvature Operator Omega on SU(3)
- **Paper 46 eq (1.2)**: [Omega sigma](x,y) = 2 tr[(Ad_x)(Ad_y) Sigma]
- Spectrum on SU(3): {2, 1, -2/3} with multiplicities {1, 8, 18}
- **Paper 45 Thm 22.3**: eigenvalue 1 produces only indefinite deformations; dim C = 0

## Notation Conventions

| Symbol | Meaning | Papers |
|:---|:---|:---|
| tau or s | Jensen deformation parameter (project: tau; Baptista: s or \|phi\|^2) | 13-18, project |
| D_K | Internal Dirac operator on K = SU(3) | 14, 17, 18 |
| g_phi, g_K | Left-invariant metric on SU(3), deformed by phi | 13, 15, 16 |
| beta, beta_0 | Bi-invariant (Killing) metric, beta(u,v) = lambda Tr(u^dag v) | 13, 28, 45, 46 |
| lambda_1, lambda_2, lambda_3 | Metric parameters for u(1), su(2), C^2 directions | 13, 15 |
| L_X, L_V | Kosmann-Lichnerowicz derivative | 17, 18, 44 |
| L_V | New (averaged) Lie derivative satisfying closure | 18 |
| R_P, R_M, R_K | Scalar curvature of total space, base, fiber | 13, 15 |
| F_A | Gauge field strength on M4 | 13, 15, 17 |
| d_A g_K | Covariant derivative of internal metric | 15, 16 |
| [ijk] | Structural constants: sum Q([e_i,e_j],e_k)^2 | 28, 29 |
| Omega | Curvature operator on symmetric 2-tensors | 45, 46 |
| Delta_L | Lichnerowicz Laplacian | 28-30, 34, 38, 42 |
| chi, h | Test function for spectral action (general: chi; entropy: h) | 19, 21 |
| gamma(a) | Heat expansion coefficient | 21, 31 |

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 13 | Scalar curvature R_{g_phi} eq (2.40) | Yes | S7, S17b (67/67 checks) |
| 13 | Volume form eq (2.37) | Yes | S7 |
| 13 | Gauge couplings eq (5.21) | Yes | S17a (g1/g2 = e^{-2tau}) |
| 14 | SM quantum numbers from Psi_+ = C^16 | Yes | S7-S8 (KO-dim=6) |
| 14 | Closure defect eq (2.65) | Yes | S34 ([iK_7, D_K]=0) |
| 15 | Gauge boson mass eq (3.7) | Yes | S56, S57 |
| 15 | Einstein instability (f_0 mode) | Yes | S20b (TT stability) |
| 15 | Jensen TT-deformation | Yes | S12, S20a (Riemann 147/147) |
| 15 | Scalar curvature eq (3.70) | Yes | S54, S55 (machine epsilon) |
| 16 | Mass variation eq (7.1) | Yes | S56, S58 (tr=0 exact; per-rep shifts computed) |
| 17 | /D_P decomposition eq (3.8) | Yes | S12+ (Dirac spectrum) |
| 17 | [/D, L_X] != 0 for non-Killing | Yes | S34 ([iK_7,D_K]=0) |
| 19 | Heat kernel a_0, a_2, a_4 | Partial | S19d, S20a, S24a |
| 28-30 | Lichnerowicz stability at fold | Yes | S55 (all 31 TT evals positive) |
| 29 | L_p matrix from structural constants | Yes | S55 (LICHNEROWICZ-55) |
| 45-46 | Killing form isolation on SU(3) | Yes | Structural (Jensen non-Einstein) |
| 39-40 | DESI w0, wa values | N/A | Observational benchmark |
