# Van den Dungen Paper Index

**Researcher**: Koen van den Dungen (Universitat Bonn)
**Papers**: 14 (2011-2025)
**Primary domain**: NCG on Riemannian submersions, Kasparov KK-theory, pseudo-Riemannian spectral triples, index theory
**Project relevance**: The ONLY researcher bridging Baptista's Riemannian submersion geometry with Connes' NCG. His Kasparov product on submersions is the mathematical tool for validating the framework's M^4 x SU(3) fiber-base decomposition. His pseudo-Riemannian and Krein space extensions handle the Lorentzian signature of physical spacetime.

---

## Dependency Graph

```
SUBMERSION & FACTORIZATION (core bridge machinery)
  01 (Kasparov Product on Submersions)
    |-- uses perturbation stability from --> 10 (Locally Bounded Perturbations)
    |-- uses group structure from --> 11 (Homotopy Equivalence in KK)
    |-- factorization applied in --> 05 (Globally Non-Trivial ACM)
    |-- factorization applied in --> 02 (Families of Spectral Triples)
  05 (Globally Non-Trivial ACM, with van Suijlekom)
    |-- extends ACM from --> 06 (Particle Physics from ACM, review)
    |-- uses gauge emergence from --> 07 (Electrodynamics from NCG)

PSEUDO-RIEMANNIAN & INDEFINITE (Lorentzian extension)
  04 (Pseudo-Riemannian Spectral Triples, 2012)
    |-- extends to Kasparov theory --> 03 (Indefinite Kasparov Modules, 2015)
    |-- extends to fermionic action --> 08 (Krein Spectral Triples, 2015)
  03 (Indefinite Kasparov Modules, with Rennie & van Suijlekom)
    |-- paired with foliation --> 02 (Families / Lorentzian construction)
    |-- paired with index theory --> 12 (APS Index & Spectral Flow)
  08 (Krein Spectral Triples)
    |-- uses Krein spaces from --> 04
    |-- fermionic action for --> 06 (SM Lagrangian recovery)

SM & GAUGE THEORY (foundational ACM + U(1))
  06 (Particle Physics from ACM, 104pp review, Chamseddine-Connes-Marcolli)
    |-- provides ACM framework for --> 05, 07, 08
    |-- spectral action apparatus for --> 01
  07 (Electrodynamics from NCG, with Marcolli)
    |-- U(1) gauge sector for --> 06

INDEX THEORY & KK INFRASTRUCTURE (technical machinery)
  09 (Index of Dirac-Schrodinger, 2017)
    |-- uses Kasparov product from --> 01
    |-- extended by --> 13 (Callias theorem, 2023)
    |-- pairs with spectral flow --> 12 (APS Index, 2020)
  10 (Locally Bounded Perturbations, 2016)
    |-- stability results used by --> 01, 11
  11 (Homotopy Equivalence in KK, 2019, with Mesland)
    |-- group structure used by --> 01, 09
    |-- extends --> 10
  12 (APS Index & Spectral Flow, 2020, with Ronge)
    |-- extends 09 to boundary conditions
    |-- connects to --> 02 (foliation = family over interval)
  13 (Generalised Callias, 2023)
    |-- extends --> 09 (Dirac-Schrodinger index)
    |-- endpoint dependence generalises --> 12 (APS spectral flow)
  14 (Fredholm Complexes, 2025, with Villegas-Villalpando)
    |-- generalises --> 09, 13 (single operator --> complex)
    |-- K-theory valued index extends --> 11 (group structure)

CHRONOLOGICAL EVOLUTION
  2011: 07 --> 2012: 04, 06 --> 2014: 05 --> 2015: 03, 08
  --> 2016: 10 --> 2017: 02, 09 --> 2018: 01 --> 2019: 11
  --> 2020: 12 --> 2023: 13 --> 2025: 14

KEY CROSS-LINKS TO BAPTISTA
  01 <--[submersion factorization validates]--> Baptista 13 (HD Routes Bosons)
  01 <--[fiber integration = shriek map]--> Baptista 13 eq 3.41
  05 <--[non-trivial ACM = non-trivial KK bundle]--> Baptista 15 (Internal Symmetries)
  02 <--[foliation = time-dependent fiber]--> Baptista 16 (Test Particles)
  06 <--[spectral action = KK spectral action]--> Baptista 19 (Chamseddine-Connes 1996)

K-THEORY CROSS-REFERENCES (researchers/K-Theory/)
  KT-02 (Connes Reconstruction)
    |-- commutative foundation for --> 01 (Kasparov product requires reconstructed manifolds)
    |-- K-theoretic/analytical separation used by --> 06 (scheme-dependent vs permanent partition)
  KT-03 (Cacic Almost-Commutative Reconstruction)
    |-- algebraic twin of --> 01 (tensor product factorization = geometric submersion factorization)
    |-- extended by --> 05 (trivial product --> non-trivial principal bundle)
    |-- fiber stability justifies --> 06 (SM fiber preserved under inner fluctuations)
  KT-05 (Chamseddine-Connes Boundary Terms)
    |-- boundary structure for --> 02 (foliation creates boundaries at leaves)
    |-- boundary conditions connect to --> 12 (APS index under boundary conditions)
  KT-06 (Connes Cyclic Cohomology SUq(2))
    |-- K-theoretic universality supports --> 03 (indefinite pairing preserves index)
    |-- cyclic cohomology infrastructure for --> 11 (group-level isomorphism UKK ~ KK)
  KT-08 (Kitaev Topological Phases)
    |-- classification used by --> 10 (perturbation stability = topological protection)
    |-- particle-hole decomposition parallels --> 04 (pseudo-Riemannian [D_+] - [D_-])
```

## Topic Map

### Submersion Factorization & Kasparov Product
Papers: 01, 02, 05
The mathematical core of the bridge. Paper 01 proves that the fundamental class of a Riemannian submersion factorizes as [D_M] = pi_! tensor [D_B] via the Kasparov product -- decomposing the Dirac operator on the total space into shriek map (encoding fiber geometry) composed with the base Dirac operator. Paper 02 reconstructs spacetime Dirac operators from families of hypersurface operators, enabling foliation-based spectral action computation. Paper 05 extends almost-commutative manifolds to globally non-trivial principal bundles, where gauge modules constrain which bundles admit consistent gauge theories.

### Pseudo-Riemannian Extension & Krein Spaces
Papers: 03, 04, 08
Extension of spectral triple theory to indefinite metric signatures (Lorentzian spacetime). Paper 04 defines pseudo-Riemannian spectral triples via Krein space indefiniteness and proves they connect to genuine spectral triples via [D]_pseudo = [D_+] - [D_-]. Paper 03 extends this to Kasparov modules, enabling KK-theoretic pairings for hyperbolic operators. Paper 08 applies Krein spaces to the fermionic action, recovering the Standard Model Lagrangian without requiring a real structure (except for Majorana masses).

### Standard Model from Almost-Commutative Geometry
Papers: 06, 07
Foundational references for the NCG approach to particle physics. Paper 06 is the canonical 104-page review (Chamseddine-Connes-Marcolli) showing how the spectral action on M^4 x F_finite generates Einstein gravity + full Standard Model gauge theory + Higgs mechanism. Paper 07 resolves the long-standing puzzle of how abelian U(1) gauge theory arises in NCG via the two-point space construction with off-diagonal Dirac fluctuations.

### Index Theory & KK Infrastructure
Papers: 09, 10, 11, 12, 13, 14
The technical machinery underlying the factorization theorems. Paper 09 establishes Fredholm properties and index formulas for Dirac-Schrodinger operators (D + V(t)) via the Kasparov product. Paper 10 proves stability of K-homology classes under locally bounded perturbations. Paper 11 (with Mesland) shows unbounded KK-theory forms an abelian group isomorphic to classical KK-theory. Paper 12 (with Ronge) proves APS index = spectral flow in both Riemannian and Lorentzian settings. Paper 13 extends the Callias index theorem to generalized Dirac-Schrodinger operators with endpoint dependence. Paper 14 (with Villegas-Villalpando, 2025) generalizes from single operators to Fredholm complexes of Hilbert C*-modules with K-theory valued indices.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Validating M^4 x SU(3) fiber-base decomposition | Paper 01, 02 | CRITICAL |
| Spectral action on submersions, shriek map | Paper 01 | CRITICAL |
| Almost-commutative manifold structure, SM Lagrangian | Paper 06, 05 | CRITICAL |
| Lorentzian signature on M^4, Wick rotation | Paper 03, 04, 02 | HIGH |
| Fermionic action, BCS in Krein space | Paper 08, 04 | HIGH |
| Non-trivial bundle topology, instantons in NCG | Paper 05 | HIGH |
| U(1) gauge emergence in NCG | Paper 07 | HIGH |
| Stability of spectral geometry under deformation | Paper 10 | HIGH |
| Index of BdG operator, topological charge | Paper 09, 13 | HIGH |
| Spectral flow along BCS evolution path | Paper 12, 09 | HIGH |
| KK-theory group structure, homotopy | Paper 11 | MEDIUM |
| Fredholm complexes, higher-order corrections | Paper 14 | MEDIUM |
| K-theoretic vs scheme-dependent partition | Paper 10 + KT-02, KT-03, KT-08 | HIGH |
| Jensen deformation stability (K-theory protection) | Paper 10 + KT-03, KT-08 | HIGH |
| Boundary terms at fold transition | Paper 02, 12 + KT-05 | HIGH |
| Index formula on deformed fiber (cyclic cohomology) | Paper 03, 11 + KT-06 | MEDIUM |

---

## Paper Entries

### Paper 01: The Kasparov Product on Submersions of Open Manifolds
- **File**: `01_2018_van_den_Dungen_Kasparov_Submersions.md`
- **arXiv**: 1811.07824
- **Year**: 2018 (published J. Topol. Anal. 14, 2022)
- **Authors**: van den Dungen
- **Relevance**: CRITICAL
- **Tags**: Kasparov product, Riemannian submersion, fundamental class, shriek map, vertical ellipticity, factorization, KK-theory

**Summary**: Proves the factorization theorem for Riemannian submersions in unbounded KK-theory. On a submersion pi: E -> B, the tensor sum D_E tensor 1 + 1 tensor D_B represents the Kasparov product [D_E] tensor [D_B]. The fundamental class of the total space factors as [D_M] = pi_! tensor [D_B], where pi_! is the shriek map. Works for non-compact, incomplete manifolds, requiring only symmetric (not self-adjoint) operators.

**Key Results**:
- Main Theorem: tensor sum on submersions represents the Kasparov product in KK-theory
- Fundamental class factorization: [D_M] = pi_! tensor [D_B]
- Regularity criterion: vertical ellipticity + geometric conditions; explicit counterexamples when regularity fails
- Extension to non-compact geometry via C*-modules and unbounded KK-theory
- Self-adjointness not required; symmetric operators suffice via bounded transform

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Bounded transform | F_D = D(1 + D*D)^{-1/2} | Maps unbounded to bounded K-homology class |
| Kasparov product | [D_E tensor 1 + 1 tensor D_B] = [D_E] tensor_{C_0(E)} [D_B] | Main factorization theorem |
| Fundamental class | [D_M] = pi_! tensor [D_B] | Shriek map decomposition |

**Dependencies**: Upstream: 10 (perturbation stability), 11 (group structure). Downstream: 02 (foliation application), 05 (non-trivial bundles). Bridge to Baptista 13 (fiber integration eq 3.41).

---

### Paper 02: Families of Spectral Triples and Foliations of Space(time)
- **File**: `02_2017_van_den_Dungen_Families_Spectral_Triples.md`
- **arXiv**: 1711.07299
- **Year**: 2018 (published J. Math. Phys. 59, 2018)
- **Authors**: van den Dungen
- **Relevance**: CRITICAL
- **Tags**: foliation, product spectral triple, Lorentzian, reverse Wick rotation, Krein space, ADM, time-dependent geometry

**Summary**: Constructs spectral triples on foliated spacetimes from families of spectral triples on constituent hypersurfaces. In the Riemannian case this yields a product spectral triple with D = d/dt tensor 1 + 1 tensor D_t. In the Lorentzian case, the construction produces a Lorentzian spectral triple via reverse Wick rotation in Krein space, with D_Lor = -i(d/dt tensor J) + 1 tensor D_t. Formalizes the algebraic structure of foliations in NCG without requiring topological leaf structure a priori.

**Key Results**:
- Product Spectral Triple Theorem: families {(A_t, H_t, D_t)} yield spectral triple on L^2([0,T]) tensor H_t
- Riemannian reconstruction of Dirac operator from hypersurface family
- Lorentzian spectral triple via reverse Wick rotation in Krein space
- Spectral action factorization as integral over time-slices: Tr(f(D)) integrates over Tr(f(D_t))
- Foliation formalized purely algebraically (no topological leaf structure needed a priori)

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Product Dirac | D = d/dt tensor 1 + 1 tensor D_t | Riemannian foliation reconstruction |
| Lorentzian Dirac | D_Lor = -i(d/dt tensor J) + 1 tensor D_t | Krein space Lorentzian construction |
| Krein metric | <psi, phi>_J = <psi, J phi>_Hilbert | Indefinite inner product with J^2 = 1 |

**Dependencies**: Upstream: 01 (factorization), 03 (indefinite modules), 04 (Krein spaces). Downstream: framework's time-dependent spectral triple D(tau(t)).

---

### Paper 03: Indefinite Kasparov Modules and Pseudo-Riemannian Manifolds
- **File**: `03_2015_van_den_Dungen_Indefinite_Kasparov_Modules.md`
- **arXiv**: 1503.06916
- **Year**: 2015 (published Ann. Henri Poincare 17, 2016)
- **Authors**: van den Dungen, Rennie, van Suijlekom
- **Relevance**: HIGH
- **Tags**: indefinite Kasparov module, Krein space, hyperbolic operator, pseudo-Riemannian, pairing theorem, globally hyperbolic

**Summary**: Defines indefinite Kasparov modules (E, phi, F, J) generalizing unbounded Kasparov modules to non-self-adjoint and hyperbolic operators via Krein involutions. Proves a pairing reversibility theorem: each indefinite module canonically corresponds to a pair of classical Kasparov modules, and the pairing formula is the difference of classical pairings on E_+ and E_- sectors. Applied to Dirac operators on pseudo-Riemannian manifolds, harmonic oscillators, and globally hyperbolic spacetimes.

**Key Results**:
- Indefinite Kasparov Module definition: (E, phi, F, J) with Krein involution J, J^2 = 1
- Pairing Reversibility: indefinite module <--> pair of classical modules, no information loss
- Pairing Formula: <indef, classical> = <E_+, classical> - <E_-, classical>
- Dirac on pseudo-Riemannian manifolds fits indefinite framework
- Index formula for hyperbolic operators as difference of elliptic indices
- Globally hyperbolic spacetimes admit indefinite Kasparov module formulation

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Indefinite pairing | <(E,F,J), (E',F')> = <(E_+,F_+),(E',F')> - <(E_-,F_-),(E',F')> | Decomposes hyperbolic index into elliptic pieces |
| Krein inner product | <psi,phi>_J = <psi, J phi> | J self-adjoint, J^2 = 1 |

**Dependencies**: Upstream: 04 (pseudo-Riemannian triples). Downstream: 02 (Lorentzian foliation), 12 (APS index in Lorentzian).

---

### Paper 04: Pseudo-Riemannian Spectral Triples and the Harmonic Oscillator
- **File**: `04_2012_van_den_Dungen_Pseudo_Riemannian_Spectral_Triples.md`
- **arXiv**: 1207.2112
- **Year**: 2012 (published J. Geom. Phys. 73, 2013)
- **Authors**: van den Dungen, Paschke, Rennie
- **Relevance**: HIGH
- **Tags**: pseudo-Riemannian, spectral triple, Krein space, indefinite metric, harmonic oscillator, local index theorem, K-homology

**Summary**: Introduces pseudo-Riemannian spectral triples (A, (H_+, H_-), D, J) as an analytic framework for pseudo-Riemannian manifolds and their noncommutative generalizations. Proves connection to genuine spectral triples via [D]_pseudo = [D_+] - [D_-], enabling application of the local index theorem. The harmonic oscillator serves as a key example demonstrating the framework's applicability beyond traditional differential geometry.

**Key Results**:
- Pseudo-Riemannian spectral triple definition with Krein space structure
- Connection theorem: [D]_pseudo = [D_+]_Riem - [D_-]_Riem
- K-homology class computable via classical methods on +/- decomposition
- Local index theorem extends to pseudo-Riemannian setting: ind(D) = integral of curvature form
- Functional calculus Tr(f(D)) rigorously defined despite indefiniteness via bounded transform
- Harmonic oscillator fits framework: non-geometric, operator-algebraic example

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Pseudo-Riemannian decomposition | [D]_pseudo = [D_+] - [D_-] | Reduces indefinite to definite K-homology |
| Bounded transform (Krein) | F_D = D(1 + D*_J D)^{-1/2} | Krein-adjoint version |
| Clifford relation | {gamma^mu, gamma^nu} = 2g^{mu nu} | g^{mu nu} has mixed signs for signature (p,q) |

**Dependencies**: Upstream: none (foundational, earliest in pseudo-Riemannian line). Downstream: 03 (Kasparov extension), 08 (Krein fermionic action), 02 (Lorentzian foliation).

---

### Paper 05: On Globally Non-Trivial Almost-Commutative Manifolds
- **File**: `05_2014_van_den_Dungen_Globally_Non_Trivial_ACM.md`
- **arXiv**: 1405.5368
- **Year**: 2014 (published J. Math. Phys. 55, 2014)
- **Authors**: van den Dungen, van Suijlekom
- **Relevance**: HIGH
- **Tags**: almost-commutative manifold, principal bundle, gauge module, non-trivial topology, instanton, Chern class, anomaly cancellation

**Summary**: Extends Connes' almost-commutative geometry to globally non-trivial principal fiber bundles. Introduces gauge modules as a proper subset of principal modules with additional compatibility constraints ensuring physical consistency (anomaly avoidance). The almost-commutative manifold for a non-trivial bundle pi: P -> M^4 has algebra A = C_0(P) rtimes G. The spectral action on non-trivial bundles gains topological contributions (Chern classes, instanton numbers). Explicit U(1) monopole and SU(2) instanton examples provided.

**Key Results**:
- Globally non-trivial ACM framework with principal bundle structure
- Gauge modules as proper subset of principal modules: ensures anomaly-free gauge theory
- Spectral action gains topological terms from bundle non-triviality
- Index of Dirac on non-trivial bundle = topological charge
- Explicit examples: U(1) monopole (charge q), SU(2) instanton (number nu)
- Gauge field arises from geometry, not imposed ad hoc

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Non-trivial ACM algebra | A = C_0(P) rtimes G | Crossed product encodes bundle topology |
| Spectral action with topology | S_spec includes integral of topological charge density | Non-trivial bundle contribution |

**Dependencies**: Upstream: 06 (ACM framework), 07 (gauge field emergence), 01 (factorization). Downstream: framework's instanton physics (S37-38).

---

### Paper 06: Particle Physics from Almost Commutative Spacetimes
- **File**: `06_2012_Chamseddine_Marcolli_Particle_Physics_ACM.md`
- **arXiv**: 1204.0328
- **Year**: 2012 (published Rev. Math. Phys. 24, 2012)
- **Authors**: Chamseddine, Connes, Marcolli (van den Dungen co-author of review)
- **Relevance**: CRITICAL
- **Tags**: spectral action, Standard Model, almost-commutative, Higgs, Yukawa, Einstein gravity, gauge-gravity unification, 104-page review

**Summary**: The canonical 104-page pedagogical review of Connes' NCG applied to particle physics. Progressively builds from electrodynamics through the electroweak model to the full Standard Model. The almost-commutative product M^4 x F_finite with algebra A_F = C + H + M_3(C) and Hilbert space H_F = C^16 per generation generates: Einstein gravity from a_2 coefficient, Yang-Mills gauge theory from a_4, Higgs mechanism from finite Dirac operator fluctuations, Yukawa couplings from D_F mass matrix. Spectral action Tr(f(D/Lambda)) unifies gravity and gauge theory from a single geometric source.

**Key Results**:
- Full SM Lagrangian from spectral action on M^4 x F_finite
- Algebra A_F = C + H + M_3(C); Hilbert space 16 x 3 = 48 dimensions
- Gauge fields emerge from inner automorphisms: commutator [D, a] produces covariant derivative
- Higgs field = distance between sheets of finite noncommutative space
- Einstein-Hilbert action from a_2 Seeley-DeWitt coefficient
- Yang-Mills + Higgs potential from a_4 coefficient
- Product Dirac: D = D_{M^4} tensor 1 + gamma_5 tensor D_F
- Coupling constant predictions at unification scale (corrected by RG flow)

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Almost-commutative Dirac | D = D_{M^4} tensor 1 + gamma_5 tensor D_F | Product structure with chiral grading |
| Spectral action | S = Tr(f(D/Lambda)) + <Psi, D Psi> | Bosonic + fermionic terms |
| Seeley-DeWitt expansion | S ~ sum_n f_n a_n(D^2) | f_n = moments of test function f |
| Finite algebra | A_F = C + H + M_3(C) | Standard Model gauge structure |
| Finite Dirac | D_F = (0, Y^dag; Y, 0) | Yukawa coupling matrix |

**Dependencies**: Upstream: none (foundational reference). Downstream: 05 (non-trivial extension), 07 (U(1) sector), 08 (fermionic action). Bridge to Baptista 19 (Chamseddine-Connes 1996 original).

---

### Paper 07: Electrodynamics from Noncommutative Geometry
- **File**: `07_2011_van_den_Dungen_Electrodynamics_NCG.md`
- **arXiv**: 1103.2928
- **Year**: 2011 (published J. Noncommut. Geom. 7, 2013)
- **Authors**: van den Dungen, Marcolli
- **Relevance**: HIGH
- **Tags**: U(1) gauge theory, two-point space, abelian, electrodynamics, inner automorphism, fluctuation, Maxwell

**Summary**: Resolves the puzzle of how abelian U(1) gauge theory emerges in NCG. The two-point space X_2 with algebra A_F = C + C, combined with M^4 in the almost-commutative product, yields U(1) gauge theory via off-diagonal fluctuations in the finite Dirac operator D_F(A). The covariant derivative and gauge field arise from inner automorphisms: gauge transformations a -> uau^dag automatically generate A_mu -> A_mu + d_mu theta. The spectral action yields Maxwell electrodynamics on curved spacetime.

**Key Results**:
- Abelian gauge theories arise naturally in NCG from simple (C + C) algebras
- U(1) gauge field from off-diagonal fluctuations in finite Dirac operator
- Inner automorphism principle: gauge transformations = algebra automorphisms
- Spectral action on M^4 x X_2 produces Maxwell + Einstein
- Completes NCG description of all SM gauge groups
- U(1) identified with hypercharge U(1)_Y in Standard Model

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Fluctuated Dirac | D_F(A) = (m_0, A; A^dag, m_1) | Off-diagonal A gives gauge field |
| Covariant derivative | nabla^A f = d f + i A f | Emerges from [D, a] commutator |
| Maxwell from spectral action | S includes integral (nabla A)^2 | EM kinetic term from Seeley-DeWitt a_4 |

**Dependencies**: Upstream: none (earliest paper in corpus). Downstream: 06 (SM context), 05 (non-trivial extension).

---

### Paper 08: Krein Spectral Triples and the Fermionic Action
- **File**: `08_2015_van_den_Dungen_Krein_Spectral_Triples.md`
- **arXiv**: 1505.01939
- **Year**: 2015 (published Math. Phys. Anal. Geom. 19, 2016)
- **Authors**: van den Dungen
- **Relevance**: HIGH
- **Tags**: Krein spectral triple, fermionic action, real structure, chirality, BCS, particle-hole, Majorana

**Summary**: Introduces Krein spectral triples generalizing standard spectral triples from Hilbert to Krein spaces for improved formulation of the fermionic action in almost-commutative manifolds. Recovers correct Lagrangians for electrodynamics, electroweak theory, and the Standard Model. The formulation does not require a real structure (Connes' J) unless Majorana masses are included. Naturally separates left/right-handed fermions, correctly implementing parity violation.

**Key Results**:
- Krein spectral triple definition: spectral triple on Krein space (indefinite inner product)
- Correct fermionic kinetic terms: minimal coupling of fermions to gauge fields recovered
- No real structure required (except for Majorana/CP-invariant terms)
- Correct chirality handling: left/right fermion separation
- Full SM fermionic sector recovery: Dirac leptons, Weyl neutrinos, CKM mixing

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Fermionic action | S_ferm = integral bar{psi} (i gamma^mu D_mu) psi | Recovered from Krein spectral triple |
| Krein inner product | <psi, phi>_J = <psi, J phi> | J = Krein fundamental symmetry, J^2 = 1 |

**Dependencies**: Upstream: 04 (Krein spaces), 06 (SM Lagrangian to recover). Downstream: framework's BCS pairing in Krein space (particle-hole mixing).

---

### Paper 09: The Index of Generalised Dirac-Schrodinger Operators
- **File**: `09_2017_van_den_Dungen_Index_Dirac_Schrodinger.md`
- **arXiv**: 1710.09206
- **Year**: 2017 (published J. Spectral Theory 9, 2019)
- **Authors**: van den Dungen
- **Relevance**: HIGH
- **Tags**: Dirac-Schrodinger, Fredholm, relative index, Kasparov product, spectral flow, cutting-pasting, BdG

**Summary**: Studies self-adjoint elliptic D with skew-adjoint potential V(t) (a family of unbounded operators on an auxiliary Hilbert module). Proves the generalized Dirac-Schrodinger operators D + V(t) are Fredholm despite V being non-self-adjoint. Establishes a relative index theorem enabling cutting and pasting on compact hypersurfaces, reducing high-dimensional index problems to lower-dimensional ones. The index equals the Kasparov product <[V], [D]>. In 1D, the index reduces to the spectral flow.

**Key Results**:
- Fredholm property for D + V(t) with unbounded skew-adjoint V
- Relative index theorem: compute on compact hypersurface (dimension reduction)
- Index = Kasparov product <[V], [D]> (K-theory x K-homology pairing)
- Spectral flow recovery in 1D (counting eigenvalue sign changes)
- Weaker regularity: only requires V variation near infinity to be small

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Dirac-Schrodinger form | D + V(t) | D self-adjoint elliptic, V skew-adjoint |
| Index as Kasparov product | ind(D+V) = <[V], [D]> | K-theory/K-homology pairing |

**Dependencies**: Upstream: 01 (Kasparov product). Downstream: 12 (APS boundary conditions), 13 (Callias extension), 14 (complex generalization).

---

### Paper 10: Locally Bounded Perturbations of Unbounded Operators
- **File**: `10_2016_van_den_Dungen_Locally_Bounded_Perturbations.md`
- **arXiv**: 1608.02506
- **Year**: 2016 (published J. Noncommut. Geom. 12, 2018)
- **Authors**: van den Dungen
- **Relevance**: HIGH
- **Tags**: perturbation, regularity, self-adjointness, Kasparov class, stability, doubling, approximate identity

**Summary**: Establishes that regularity and self-adjointness of unbounded operators on Hilbert modules are preserved under locally bounded symmetric perturbations. The Kasparov class [D] from an unbounded Kasparov module remains unchanged under such perturbations. Provides a converse to the standard doubling procedure for odd unbounded Kasparov modules. This is a foundational stability result ensuring that small geometric deformations do not alter the topological content.

**Key Results**:
- Regularity + self-adjointness preserved under locally bounded symmetric perturbation
- K-homology class [D] invariant under locally bounded perturbation
- Converse to doubling for odd unbounded Kasparov modules
- Spectral action topologically robust against small deformations

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Perturbation stability | [D + V] = [D] in KK(A, C) | V locally bounded symmetric |

**Dependencies**: Upstream: none (foundational stability result). Downstream: 01 (submersion regularity), 11 (homotopy invariance).

---

### Paper 11: Homotopy Equivalence in Unbounded KK-Theory
- **File**: `11_2019_van_den_Dungen_Homotopy_Equivalence_KK.md`
- **arXiv**: 1907.04049
- **Year**: 2019 (published Ann. K-Theory 5, 2020)
- **Authors**: van den Dungen, Mesland
- **Relevance**: MEDIUM
- **Tags**: unbounded KK-cycle, homotopy, abelian group, sigma-unital, bounded transform, isomorphism, direct sum

**Summary**: Introduces a generalized unbounded KK-cycle concept extending Kasparov modules with well-defined direct sums. Proves homotopy equivalence classes form an abelian group UKK(A,B) for sigma-unital C*-algebras. For separable algebras, UKK(A,B) is isomorphic to Kasparov's classical KK(A,B) via the bounded transform. This validates that computations in unbounded KK-theory (operator-level, where van den Dungen works) are equivalent to classical KK-theory (bounded transform level).

**Key Results**:
- Generalized unbounded KK-cycle with well-defined direct sum
- Homotopy classes form abelian group UKK(A,B)
- For separable algebras: UKK(A,B) isomorphic to KK(A,B) via bounded transform
- Homotopy = operator-homotopy + degenerate cycles

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Isomorphism | UKK(A,B) ~ KK(A,B) | For separable C*-algebras |

**Dependencies**: Upstream: 10 (perturbation stability). Downstream: 01 (group structure for Kasparov product), 14 (K-theory valued index).

---

### Paper 12: The APS-Index and the Spectral Flow
- **File**: `12_2020_van_den_Dungen_APS_Index_Spectral_Flow.md`
- **arXiv**: 2004.01085
- **Year**: 2020 (published Oper. Matrices 15, 2021)
- **Authors**: van den Dungen, Ronge
- **Relevance**: HIGH
- **Tags**: APS index, spectral flow, boundary conditions, Fredholm, Riemannian, Lorentzian, eta invariant

**Summary**: Proves equality between the Atiyah-Patodi-Singer index and spectral flow in a functional analytic framework. For families A(t) of self-adjoint Fredholm operators on [0,T], the Fredholm index of D = d/dt + A (Riemannian) or D = d/dt - iA (Lorentzian) with APS boundary conditions equals the spectral flow of A(t). The APS eta-invariant boundary term exactly cancels when computing indices.

**Key Results**:
- APS index = spectral flow (both Riemannian and Lorentzian settings)
- Lorentzian extension: generalizes Bar-Strohmaier results to indefinite signature
- Eta-invariant boundary term cancellation
- Topological charge quantized as integer via spectral flow

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Riemannian APS | ind(d/dt + A) = sf(A(t)) | APS boundary conditions |
| Lorentzian APS | ind(d/dt - iA) = sf(A(t)) | Indefinite extension |

**Dependencies**: Upstream: 09 (Dirac-Schrodinger index), 03 (indefinite extension). Downstream: 13 (endpoint dependence generalization).

---

### Paper 13: Generalised Dirac-Schrodinger Operators and the Callias Index Theorem
- **File**: `13_2023_van_den_Dungen_Generalised_Dirac_Callias.md`
- **arXiv**: 2312.17600
- **Year**: 2023 (accepted Forum Math. Sigma, 2024)
- **Authors**: van den Dungen
- **Relevance**: HIGH
- **Tags**: Callias theorem, Dirac-Schrodinger, compact hypersurface, endpoint dependence, Kasparov product, spectral flow

**Summary**: Generalizes the classical Callias index theorem to generalized Dirac-Schrodinger operators. The index of D + V is computable on a suitable compact hypersurface, reducing non-compact domain problems to compact ones. Spectral flow along paths of relatively compact perturbations depends exclusively on endpoint data. The index equals the Kasparov product <[V], [D]>. This is the strongest localization result in the corpus: topological invariants are boundary-determined.

**Key Results**:
- Callias theorem for generalized Dirac-Schrodinger operators
- Index computable on compact hypersurface (non-compact domain reduction)
- Endpoint dependence: spectral flow depends only on initial and final states, not path
- Index = Kasparov product <[V], [D]>

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Callias index | ind(D+V) = index computed on compact hypersurface Sigma | Localization to boundary |
| Kasparov product | ind(D+V) = <[V], [D]> | Same pairing as Paper 09, stronger hypotheses |

**Dependencies**: Upstream: 09 (Dirac-Schrodinger), 12 (APS spectral flow). Downstream: 14 (complex generalization).

---

### Paper 14: Fredholm Complexes of Hilbert C*-modules
- **File**: `14_2025_Villegas_van_den_Dungen_Fredholm_Complexes.md`
- **arXiv**: 2505.07568
- **Year**: 2025 (submitted)
- **Authors**: Villegas-Villalpando, van den Dungen
- **Relevance**: MEDIUM
- **Tags**: Fredholm complex, cochain complex, Hilbert C*-module, K-theory index, Hodge decomposition, perturbation stability

**Summary**: Extends Fredholm theory from single operators to cochain complexes of Hilbert C*-modules with unbounded regular operators as differentials. Provides equivalent characterizations of the Fredholm property for complexes and establishes a Fredholm index valued in K_0(A). The index is stable under small and relatively compact perturbations. When Hodge decomposition exists (harmonic + exact + coexact), the index computes via kernel/cokernel of the harmonic operator.

**Key Results**:
- Fredholm property defined for unbounded operator complexes on C*-modules
- Index valued in K_0(A) of underlying C*-algebra (topological invariant)
- Stability under small and relatively compact perturbations
- Hodge decomposition: index via ker/coker of harmonic operator
- Generalizes Papers 09, 13 from single operators to chain complexes

**Key Equations**:

| Label | Equation | Context |
|:---|:---|:---|
| Complex index | ind(complex) in K_0(A) | K-theory valued Fredholm index |
| Hodge formula | ind = [ker(Laplacian)] | When Hodge decomposition exists |

**Dependencies**: Upstream: 09 (single operator case), 13 (Callias), 11 (K-theory groups). Most recent paper (2025).

---

## Cross-Paper Equation Concordance

The central equations across the corpus form a coherent factorization chain. Here we trace how key structures transform from paper to paper.

### The Bounded Transform

| Paper | Form | Notes |
|:---|:---|:---|
| 01 | F_D = D(1 + D*D)^{-1/2} | Standard Hilbert space, maps unbounded to K-homology class |
| 04 | F_D = D(1 + D*_J D)^{-1/2} | Krein-adjoint version for pseudo-Riemannian |
| 11 | Bounded transform induces UKK(A,B) ~ KK(A,B) | Group-level isomorphism statement |

### The Kasparov Product / Factorization

| Paper | Form | Notes |
|:---|:---|:---|
| 01 | [D_E tensor 1 + 1 tensor D_B] = [D_E] tensor [D_B] | Submersion factorization (main theorem) |
| 01 | [D_M] = pi_! tensor [D_B] | Fundamental class = shriek map x base class |
| 06 | D = D_{M^4} tensor 1 + gamma_5 tensor D_F | ACM product Dirac (special case with grading) |
| 09 | ind(D+V) = <[V], [D]> | Index as Kasparov pairing |
| 13 | ind(D+V) = <[V], [D]> computed on Sigma | Callias localization of same pairing |

### The Indefinite / Krein Decomposition

| Paper | Form | Notes |
|:---|:---|:---|
| 04 | [D]_pseudo = [D_+] - [D_-] | Pseudo-Riemannian spectral triple to classical pair |
| 03 | <indef, classical> = <E_+, classical> - <E_-, classical> | Kasparov module level pairing |
| 02 | D_Lor = -i(d/dt tensor J) + 1 tensor D_t | Lorentzian from Riemannian family |
| 08 | S_ferm from Krein spectral triple | Fermionic action without real structure |

### Spectral Action Expansion

| Paper | Form | Notes |
|:---|:---|:---|
| 06 | S = Tr(f(D/Lambda)) ~ sum f_n a_n(D^2) | Seeley-DeWitt heat kernel expansion |
| 06 | a_0, a_2 (gravity), a_4 (YM + Higgs) | Physical content of each coefficient |
| 05 | S gains topological charge terms for non-trivial bundles | Non-trivial topology extension |
| 07 | S includes Maxwell (nabla A)^2 for U(1) | Abelian gauge sector from two-point space |

### Index = Spectral Flow

| Paper | Form | Notes |
|:---|:---|:---|
| 12 | ind(d/dt + A) = sf(A(t)) with APS BC | Riemannian case |
| 12 | ind(d/dt - iA) = sf(A(t)) with APS BC | Lorentzian extension |
| 09 | In 1D: index = spectral flow | Special case |
| 13 | Spectral flow depends only on endpoints | Callias strengthening |

### Perturbation and Stability

| Paper | Form | Notes |
|:---|:---|:---|
| 10 | [D + V] = [D] for V locally bounded symmetric | K-homology class invariance |
| 14 | ind(complex) stable under small/relatively compact perturbations | Extension to complexes |

---

## Notation Conventions

### Van den Dungen vs Connes vs Baptista

| Symbol | Van den Dungen | Connes (Paper 06) | Baptista (Papers 13-18) | Notes |
|:---|:---|:---|:---|:---|
| Spectral triple | (A, H, D) | (A, H, D) | not used directly | Same notation |
| Dirac operator | D (self-adjoint or symmetric) | D (self-adjoint) | D-slash or nabla-slash | VdD allows symmetric; Baptista uses slash notation |
| Krein involution | J (with J^2 = 1) | -- | -- | VdD-specific; NOT Connes' real structure |
| Real structure | J_0 or J (context-dependent) | J (with J^2 = +/-1) | -- | CRITICAL: J in VdD Papers 03,04 = Krein involution, distinct from Connes' J |
| Kasparov product | tensor_{C_0(E)} | tensor_B | -- | Module tensor product over C*-algebra |
| Shriek map | pi_! | pi_! or pi^! | fiber integration | Same concept, different realization (algebraic vs analytic) |
| Gauge field | A (fluctuation of D_F) | A = sum a_i [D, b_i] | A_mu (connection) | VdD/Connes: inner fluctuation; Baptista: classical connection |
| K-homology class | [D] or [F_D] | [D] | -- | Same |
| Seeley-DeWitt coeffs | a_n(D^2) | a_n(D^2/Lambda^2) | -- | Baptista uses curvature invariants directly |
| Metric signature | (p,q) general | (-,+,+,+) assumed | (+,...,+) Riemannian on SU(3) | VdD handles general (p,q); project has mixed |
| Fiber Dirac | D_E (vertically elliptic) | D_F (finite Dirac) | D_K (on SU(3)) | Three distinct notations for fiber operator |
| Base Dirac | D_B | D_{M^4} | D_{M^4} | Consistent across sources |

### Critical Convention Warnings

1. **J ambiguity**: In Papers 03, 04, 08, J denotes the Krein fundamental symmetry (J^2 = 1, defines indefinite inner product). In Connes' NCG (Paper 06), J denotes the real structure (charge conjugation) with J^2 = +/-1 depending on KO-dimension. These are DIFFERENT operators. The framework's J (Session 17a CPT result) is Connes' real structure, not VdD's Krein involution.

2. **Shriek map vs fiber integration**: VdD's pi_! (Paper 01) and Baptista's fiber integration (Paper 13, eq 3.41) implement the same mathematical operation (pushforward along fibers) but in different languages. VdD works in KK-theory (algebraic, C*-modules); Baptista works in differential geometry (analytic, differential forms). Verifying their equivalence is a key open task.

3. **Vertical ellipticity vs fiber Dirac**: VdD's "vertically elliptic" (Paper 01) means the operator's principal symbol is invertible in fiber directions. This is a WEAKER condition than requiring a full self-adjoint Dirac operator on each fiber. The framework's D_K on SU(3) is self-adjoint by construction, so it satisfies vertical ellipticity automatically, but not vice versa.

4. **Product Dirac grading**: Paper 06 writes D = D_{M^4} tensor 1 + gamma_5 tensor D_F with the gamma_5 chiral grading. Paper 01 writes the tensor sum without gamma_5 because it operates in general (ungraded) KK-theory. For even-dimensional M^4, these are compatible via the grading operator. The framework uses gamma_5 grading (matching Paper 06).

5. **Regularity**: Paper 01 shows regularity (closure of symmetric operator is self-adjoint) is NOT automatic for vertically elliptic operators on non-compact submersions. For the framework's case (SU(3) fiber is compact), regularity is expected but should be verified explicitly against VdD's geometric conditions.

---

## Computational Verification Status

| Paper | Key Result | Verified in Framework? | Session | Status |
|:---|:---|:---|:---|:---|
| 01 | Kasparov product on submersions | Partially: fiber D_K eigenvalues computed | S7-S35 | NEEDS: full factorization check with O'Neill tensors |
| 01 | Fundamental class factorization | Not yet verified computationally | -- | OPEN: requires Kasparov product computation |
| 02 | Product spectral triple from family | Conceptually used (tau(t) evolution) | S38 | NEEDS: explicit spectral action integral over time-slices |
| 03 | Indefinite Kasparov pairing | Not yet applied | -- | OPEN: relevant if Lorentzian M^4 treated explicitly |
| 04 | Pseudo-Riemannian spectral triple decomposition | Not yet applied | -- | OPEN: project works in Euclidean signature currently |
| 05 | Non-trivial bundle topology | Instanton number computed | S37-38 | PARTIAL: S_inst=0.069 but not framed as bundle topology |
| 06 | SM from spectral action | KO-dim=6, SM quantum numbers verified | S7-8 | VERIFIED: 67/67 Baptista geometry checks (S17b) |
| 06 | Product Dirac D = D_M tensor 1 + gamma_5 tensor D_F | D_K eigenvalues computed | S7-35 | VERIFIED: block-diagonal theorem (S22b), 8.4e-15 |
| 07 | U(1) from two-point space | Not separately verified | -- | LOW priority (absorbed into SM verification) |
| 08 | Fermionic action from Krein triple | BCS formulated in framework | S34-38 | PARTIAL: Krein structure implicit in BdG formulation |
| 09 | BdG index = Kasparov product | Not yet computed | -- | OPEN: would validate instanton number |
| 10 | Stability under perturbation | Implicitly assumed | S37-38 | NEEDS: verify Jensen deformation is locally bounded |
| 12 | APS index = spectral flow | Spectral flow along tau not computed | -- | OPEN: would give instanton number directly |
| 13 | Callias endpoint dependence | Not yet applied | -- | OPEN: boundary-only computation possible |
| 14 | Fredholm complex index | Not yet applied | -- | FUTURE: higher-order spectral action corrections |

### Priority Verification Tasks

1. **CRITICAL**: Verify that the Kasparov product [D_E] tensor [D_B] on M^4 x SU(3) correctly decomposes the spectral action into base + fiber + cross-terms. Does Baptista's fiber integration (Paper 13 eq 3.41) implement the shriek map pi_! from Paper 01?

2. **CRITICAL**: Check whether O'Neill's A-tensor and T-tensor (integrability obstructions for the submersion M^4 x SU(3) -> M^4) produce cross-terms in the spectral action that the current framework neglects.

3. **HIGH**: Compute the spectral flow of D_K(tau) as tau varies from 0 to tau_fold to verify it equals the instanton number from S37-38 (S_inst = 0.069).

4. **HIGH**: Verify that Jensen deformation of SU(3) is a locally bounded perturbation of D_K in the sense of Paper 10, ensuring K-homology class stability across the deformation.

5. **MEDIUM**: Apply the Callias endpoint dependence (Paper 13) to determine which topological invariants of the BCS evolution are fixed solely by initial (tau=0) and final (tau=tau_fold) boundary data.

---

## K-Theory Cross-References

Van den Dungen's program -- factorizing spectral triples on total spaces of Riemannian submersions via the Kasparov product -- rests on foundational K-theoretic infrastructure that is catalogued separately in `researchers/K-Theory/`. Five papers in that collection have direct structural connections to the VdD corpus. The connections fall into three categories: (i) the reconstruction theorems that underpin VdD's factorization (KT-02, KT-03), (ii) the spectral action boundary structure that governs the fold transition (KT-05), (iii) the K-theoretic stability and classification machinery that guarantees topological protection (KT-06, KT-08).

### Cross-Reference Map

| K-Theory Paper | VdD Paper(s) | Connection | Structural Role |
|:---|:---|:---|:---|
| KT-02 (Connes 2008, Spectral Characterization of Manifolds) | Paper 01 (Kasparov Product on Submersions), Paper 06 (Particle Physics from ACM) | Connes' reconstruction theorem proves that commutative spectral triples satisfying the five axioms uniquely determine Riemannian manifolds. This is the **commutative foundation** for VdD's Kasparov product: Paper 01's factorization [D_M] = pi_! tensor [D_B] requires that both the base B and total space M reconstruct as manifolds via KT-02, so that the submersion pi: M -> B is genuinely geometric. KT-02's separation of K-theoretic invariants (index, Chern character) from analytical quantities (Seeley-DeWitt coefficients) is the origin of the scheme-dependent/independent partition that the framework inherits through Paper 06's spectral action. | Foundation for the geometric side of the Kasparov product. Without KT-02, the factorization theorem in Paper 01 would be purely algebraic with no geometric content. |
| KT-03 (Cacic 2011, Almost-Commutative Reconstruction) | Paper 05 (Globally Non-Trivial ACM), Paper 06 (Particle Physics from ACM) | Cacic extends the reconstruction theorem to product geometries A = C(M) tensor A_f -- precisely the almost-commutative manifolds that Papers 05 and 06 use. Cacic proves: (i) the heat kernel factors as Tr(e^{-tD^2}) = Tr(e^{-tD_M^2}) * Tr(e^{-tD_f^2}), enabling independent reconstruction of spacetime and fiber; (ii) inner-fluctuation stability -- gauge transformations preserve K-theoretic invariants while modifying Seeley-DeWitt coefficients; (iii) the fiber algebra A_f is preserved up to unitary equivalence under perturbation. This is the **algebraic analog** of VdD's submersion factorization in Paper 01: where Paper 01 proves factorization geometrically (Kasparov product on submersions), KT-03 proves it algebraically (tensor product reconstruction). Paper 05's globally non-trivial extension generalizes KT-03 from trivial products to principal bundles. | Algebraic twin of Paper 01's geometric factorization. KT-03 proves fiber stability under perturbation; Paper 05 extends to non-trivial topology. |
| KT-05 (Chamseddine-Connes 2007, Boundary Terms from Spectral Action) | Paper 02 (Families of Spectral Triples), Paper 12 (APS Index and Spectral Flow) | KT-05 proves the spectral action automatically predicts the Gibbons-Hawking-York boundary term with correct sign and coefficient. Paper 02 constructs spectral triples on foliated spacetimes, which naturally create boundaries at the foliation leaves. Paper 12 proves APS index = spectral flow under APS boundary conditions. The boundary terms from KT-05 are exactly the boundary contributions that must be accounted for in Paper 02's foliation construction and Paper 12's APS index formula. For the framework: the fold transition (tau = 0.190) creates an effective boundary; KT-05 ensures the spectral action's boundary contribution is geometrically determined, not tuned. | Boundary structure for foliation-based spectral triples. Links spectral action boundary terms to APS boundary conditions. |
| KT-06 (Connes 2002, Cyclic Cohomology and SUq(2) Index) | Paper 03 (Indefinite Kasparov Modules), Paper 11 (Homotopy Equivalence in KK) | KT-06 extends the Atiyah-Singer index theorem to quantum groups via cyclic cohomology, proving the index is determined by topological data independent of the deformation parameter q. Paper 03 extends Kasparov modules to indefinite (Krein) settings, proving the pairing formula decomposes into classical pieces: <indef, classical> = <E_+, classical> - <E_-, classical>. Both papers demonstrate K-theoretic universality -- the index is platform-independent, surviving passage from commutative to noncommutative algebras (KT-06) and from definite to indefinite inner products (Paper 03). Paper 11's isomorphism UKK(A,B) ~ KK(A,B) ensures this stability holds at the group level. For the framework: KT-06's result that the Chern character is deformation-independent supports the claim that KO-dimension and quantum numbers survive Jensen deformation. | K-theoretic universality across deformations. Cyclic cohomology provides the index formula infrastructure for Papers 03 and 11. |
| KT-08 (Kitaev-Laumann 2009, Topological Phases and Quantum Computation) | Paper 10 (Locally Bounded Perturbations), Paper 04 (Pseudo-Riemannian Spectral Triples) | KT-08 introduces the K-theory classification of topological phases: gapped systems with symmetry are classified by K-groups, and topological invariants (edge states, winding numbers) are protected against local perturbations preserving the gap and symmetry. Paper 10 proves the analogous statement for spectral triples: the K-homology class [D] is invariant under locally bounded symmetric perturbations. The framework's D_K is classified as BDI (integer Z index) by KT-08's periodic table, with TRS (T^2=+1), PHS (C), and chiral symmetry. Paper 10 guarantees this classification is stable under Jensen deformation (a locally bounded perturbation of the fiber Dirac operator). Paper 04's pseudo-Riemannian decomposition [D]_pseudo = [D_+] - [D_-] parallels KT-08's decomposition of topological phases into particle-hole sectors. | Topological classification + perturbation stability. KT-08 classifies D_K; Paper 10 guarantees classification stability. |

### K-Theory and Jensen Deformation Stability

The S71 workshop established that K-theoretic properties of the fiber (KO-dimension = 6, quantum numbers, CPT symmetry, BDI classification) are preserved under Jensen deformation. The K-Theory collection provides the mathematical foundation for this claim through a chain of three results:

1. **KT-03 (Cacic reconstruction)**: For almost-commutative spectral triples, the fiber algebra A_f and its K-theoretic content are preserved (up to unitary equivalence) under inner fluctuations and metric perturbations. Jensen deformation is a metric perturbation of the SU(3) fiber, so KT-03 applies directly: the K-theory of the fiber is deformation-invariant.

2. **KT-02 (Connes reconstruction)**: The K-theoretic/analytical separation -- index and Chern character are topologically protected while Seeley-DeWitt coefficients are analytically contingent -- provides the structural reason WHY some framework predictions are permanent and others are scheme-dependent. The Jensen deformation changes the metric (and thus Seeley-DeWitt coefficients a_n), but cannot change the index.

3. **KT-08 (Kitaev classification)**: The BDI topological class of D_K is protected by the gap and symmetry structure. As long as the Jensen deformation does not close the spectral gap or break TRS/PHS/chiral symmetry, the topological classification is invariant. Paper 10 (locally bounded perturbations) provides the precise condition: Jensen deformation is locally bounded, so [D_K] is invariant in K-homology.

Together, these establish a three-layer protection hierarchy for the fiber:
- **Representation-theoretic** (KT-03 + Paper 05): fiber algebra structure preserved under gauge and metric perturbations
- **Topological** (KT-08 + Paper 10): K-homology class [D_K] invariant under locally bounded deformations
- **Index-theoretic** (KT-06 + KT-02): Chern character and index determined by cyclic cohomology, independent of deformation parameters

This hierarchy aligns precisely with the framework's S69 protection hierarchy: representation-theoretic (10^13x margin) > topological > BCS-specific (1.7x).
