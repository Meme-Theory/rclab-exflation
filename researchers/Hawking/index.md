# Hawking Paper Index

**Researcher**: Hawking (+ Bekenstein, Unruh, Page, Parker, Penington, Jacobson, AMPS, Wald, Verlinde, Witten, et al.)
**Papers**: 45 (1969--2024)
**Primary domain**: Black hole thermodynamics, Hawking radiation, information paradox, cosmological particle creation, entropy, analog gravity, contemporary reviews
**Project relevance**: Framework transit = Parker-type particle creation. Spectral action = entropy (Paper 20). No horizon = no information paradox. GGE relic = permanent non-thermal state.
**Source**: 32 PDF-sourced + 13 pre-arXiv stubs. Rebuilt 2026-03-23.

---

## Dependency Graph

```
SINGULARITY & AREA THEOREMS
  01 (Hawking-Penrose 1970 Singularities)
    |-> 02 (Hawking 1971 Area Theorem)
    |-> 03 (Bardeen-Carter-Hawking 1973 Four Laws)
  02 -> 03
  03 -> 04 (Hawking 1974 BH Explosions)
  04 -> 05 (Hawking 1975 Particle Creation) [full derivation of 04's announcement]
  05 -> 06 (Hawking 1976 Information Loss) [consequence of 05]
  05 -> 07 (Gibbons-Hawking 1977 Cosmological Horizons) [extends 05 to dS]

  11 (Bekenstein 1973 Entropy) -> 03 [entropy-area identification]
  11 -> 05 [fixes S = A/4 coefficient]

PARTICLE CREATION (PARKER)
  15 (Parker 1969 Part I) -> 16 (Parker 1971 Part II: fermions)
  15 -> 05 [Hawking used Parker's Bogoliubov framework]
  15 -> 19 (Ford 2021 Review) [comprehensive review of 15-16]
  15,16 -> 25 (Parker-Navarro-Salas 2017 50 Years) [historical review]
  15,16 -> 27 (Kolb-Long 2023 CGPP) [modern catalog of gravitational production]

UNRUH EFFECT & MOVING MIRRORS
  12 (Unruh 1976) -- parallel to 05, uses same Bogoliubov mechanism
  12 -> 38 (Crispino-Higuchi-Matsas 2008 Review) [comprehensive review of 12]
  29 (Fulling-Davies 1976 Moving Mirror) -- flat-space analog of 05
  29 -> 45 (Dodonov 2010 Dynamical Casimir) [extends moving mirror to DCE]

BLACK HOLE THERMODYNAMICS & ENTROPY
  03 -> 22 (Wald 1993 Noether Charge) [generalizes first law to arbitrary gravity]
  03 -> 35 (Hawking-Page 1983 Phase Transition) [BH thermodynamics in AdS]
  11 -> 22 [generalizes S = A/4 to Wald entropy]
  17 (Jacobson 1995) <- 03, 11, 12 [DERIVES Einstein eqs FROM thermodynamics]
  32 (Verlinde 2010 Entropic Gravity) <- 17 [extends Jacobson's program]
  40 (Wall 2009 Ten Proofs GSL) <- 03, 11, 22 [systematic GSL analysis]

SPECTRAL ACTION = ENTROPY (NCG BRIDGE)
  20 (CCS 2019 Entropy Spectral Action) <- 11, 17 [S_vN = Tr(h(beta D))]

INFORMATION PARADOX ARC
  06 (Hawking 1976 Info Loss) -> 13 (Page 1993 Page Curve)
  06 -> 10 (Hawking 2005 Info Recovery) [Hawking reverses position]
  06 -> 18 (AMPS 2013 Firewalls) [sharpens paradox]
  18 -> 36 (AMPS 2013 Apologia) [defends firewall]
  13 -> 14 (Penington 2019 Entanglement Wedge) [derives Page curve from RT]
  14 -> 21 (AHMST 2020 Replica Wormholes) [gravitational path integral derivation]
  14 -> 44 (Almheiri+ 2020 Review) [comprehensive review of 14, 21]
  24 (Engelhardt-Wall 2014 QES) -> 14, 21, 44 [foundational QES concept]

ISLANDS IN COSMOLOGY & KK
  14, 21 -> 23 (Hartman-Jiang-Shaghoulian 2020 Islands Cosmology)
  14, 21 -> 28 (Hung-Nam 2023 KK Entanglement Island)
  14, 21 -> 30 (Teresi 2022 Islands dS)
  14, 21 -> 31 (Kames-King+ 2021 No Page Curves dS)

KK COSMOLOGY & SCHWINGER
  34 (Darabi 2003 Dynamical Compactification) [direct KK exflation precursor]
  33 (Yamada 2024 KK Schwinger) <- 15, 05 [KK particle production]

HOLOGRAPHY
  35 (Hawking-Page 1983) -> 42 (Witten 1998 AdS Holography)
  42 -> 10, 14, 21, 39 [AdS/CFT as framework for info paradox]

CONTEMPORARY REVIEWS (reproduce originals)
  37 (Traschen 2000) reproduces: 03, 05, 12 [step-by-step Hawking calc]
  38 (Crispino+ 2008) reproduces: 12 [complete Unruh derivation]
  39 (Harlow 2014) reproduces: 05, 06, 13, 18 [full info paradox arc]
  40 (Wall 2009) reproduces: 02, 03, 11 [GSL proofs]
  41 (Wald 2009) reproduces: 15, 12 [QFT in curved spacetime foundations]
  43 (Baumann 2009) reproduces: 08 [inflationary perturbation theory]
  44 (Almheiri+ 2020) reproduces: 05, 06, 13, 14, 21 [full island/Page review]
  45 (Dodonov 2010) reproduces: 29 [DCE/moving mirror review]
```

## Topic Map

### Singularity Theorems & Causal Structure
Papers: 01
The Hawking-Penrose singularity theorem: geodesic incompleteness under the energy condition, generality condition, and trapped surface/cosmological/reconvergence condition. Foundation for all subsequent black hole physics.

### Black Hole Mechanics & Thermodynamics
Papers: 02, 03, 04, 05, 07, 11, 22, 35, 40
The four laws of black hole mechanics (03), area theorem (02), Hawking temperature (04, 05), Bekenstein-Hawking entropy (11), Gibbons-Hawking cosmological temperature (07), Wald entropy as Noether charge (22), Hawking-Page phase transition (35), and generalized second law proofs (40).

### Hawking Radiation & Bogoliubov Formalism
Papers: 04, 05, 12, 29, 37, 38
Particle creation by black holes (05), the Unruh effect (12), and the moving mirror analog (29). The Bogoliubov transformation is the unifying mathematical tool. Reviews 37 and 38 reproduce the full derivations.

### Cosmological Particle Creation (Parker)
Papers: 15, 16, 19, 25, 27, 33, 45
Parker's foundational discovery (15, 16) of gravitational particle creation in expanding universes. Modern reviews (19, 25, 27) catalog results for all spins. The KK Schwinger effect (33) extends to compact dimensions. The dynamical Casimir effect (45) provides experimental analogs.

### Information Paradox & Its Resolution
Papers: 06, 10, 13, 14, 18, 21, 24, 36, 39, 44
Hawking's information loss argument (06), the Page curve (13), the firewall paradox (18, 36), Hawking's reversal (10), the quantum extremal surface (24), Penington's island formula (14), replica wormholes (21), and comprehensive reviews (39, 44).

### Islands, Entropy Bounds & Cosmological Applications
Papers: 23, 28, 30, 31
Islands in cosmology (23), KK entanglement islands (28), islands and dS entropy (30), and no Page curves for dS (31). These extend the island program beyond black holes.

### Thermodynamic Gravity & Emergent Spacetime
Papers: 17, 20, 32
Jacobson's derivation of Einstein equations from thermodynamics (17), CCS entropy = spectral action identity (20), and Verlinde's entropic gravity (32). Paper 20 is THE critical paper for the framework.

### Kaluza-Klein Cosmology & Dynamical Compactification
Papers: 28, 33, 34
Direct KK cosmology (34), KK Schwinger effect (33), and KK entanglement islands (28). These are the most directly relevant to the M4 x SU(3) framework geometry.

### Holography, AdS/CFT & Phase Transitions
Papers: 35, 42
The Hawking-Page phase transition (35) and Witten's AdS/CFT dictionary (42). Structural context for the framework but not directly applicable (framework is not holographic).

### QFT in Curved Spacetime Foundations
Papers: 41, 43
Wald's algebraic formulation of QFT in curved spacetime (41) and Baumann's TASI inflation lectures (43). Foundational framework papers.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Bogoliubov coefficients, particle creation formalism | 05, 15, 16, 37, 38, 41 | CRITICAL |
| Hawking temperature, black hole radiation | 04, 05, 07, 37, 44 | CRITICAL |
| Spectral action = entropy identity | 20 | CRITICAL |
| Information paradox, Page curve, unitarity | 06, 13, 14, 21, 39, 44 | CRITICAL |
| Bekenstein-Hawking entropy, GSL | 11, 22, 40 | CRITICAL |
| Einstein equations from thermodynamics | 17, 32 | CRITICAL |
| KK particle creation, Schwinger in compact spaces | 33, 34, 27 | HIGH |
| Unruh effect, Rindler quantization | 12, 38 | HIGH |
| Firewalls, AMPS paradox | 18, 36, 39 | HIGH |
| Islands in cosmology / de Sitter | 23, 28, 30, 31 | MEDIUM |
| Analog Hawking radiation (BEC experiment) | 26 | HIGH |
| Inflationary perturbation spectrum | 08, 43 | MEDIUM |
| No-boundary proposal, Wheeler-DeWitt | 09 | HIGH |
| Moving mirror, dynamical Casimir | 29, 45 | MEDIUM |
| AdS/CFT, holography, HP transition | 35, 42 | MEDIUM |

---

## Paper Entries

### Paper 01: The Singularities of Gravitational Collapse and Cosmology
- **File**: `01_Hawking_Penrose_1970_Singularities.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1970
- **Relevance**: MEDIUM
- **Tags**: singularity theorem, Raychaudhuri equation, energy conditions, geodesic incompleteness, trapped surface
- **Source**: pre-arXiv stub (detailed reconstruction from published record)

**Summary**: Unified singularity theorem subsuming five prior results (Penrose I, Hawking II-V). Proves geodesic incompleteness under the strong energy condition, generality condition, and existence of a trapped set, without requiring a global Cauchy hypersurface. Applied to the observed universe via the 2.7 K CMB.

**Key Results**:
- Unified theorem: space-time singularities are generic under physically reasonable conditions
- Three scenarios: gravitational collapse (trapped surface), cosmological (compact spatial hypersurface), observational (past null cone reconvergence)
- Energy condition: epsilon + Sum p_i >= 0 and epsilon + p_i >= 0

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 3.4 | Energy condition: R_ab t^a t^b >= 0 for unit timelike t^a | Eq. (3.4) |
| eq 3.17 | Raychaudhuri: D theta + theta^2/3 + sigma^2 + R_ab k^a k^b = 0 | Eq. (3.17) |
| eq 3.10 | Generality condition on curvature alignment | Eq. (3.10) |

**Dependencies**: Upstream of 02, 03. Foundation for all subsequent BH physics.
**Proxy**: Paper 37 (Traschen) reviews the causal structure and energy conditions.

---

### Paper 02: Gravitational Radiation from Colliding Black Holes
- **File**: `02_Hawking_1971_Area_Theorem.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1971
- **Relevance**: MEDIUM
- **Tags**: area theorem, second law, irreducible mass, gravitational wave emission
- **Source**: pre-arXiv stub

**Summary**: Proved the area theorem (delta A >= 0) assuming the weak energy condition and cosmic censorship. Applied to constrain gravitational wave emission from black hole collisions: maximum 29% mass radiated for equal-mass Schwarzschild mergers.

**Key Results**:
- Area theorem: total event horizon area never decreases classically
- Irreducible mass: M_irr^2 = A/(16 pi)
- Maximum radiation for equal-mass collision: Delta E/(2M) <= 1 - 1/sqrt(2)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Area theorem | delta A >= 0 | Main result |
| Schwarzschild area | A = 16 pi M^2 | Definition |
| Irreducible mass | M_irr^2 = A/(16 pi) | Definition |

**Dependencies**: Downstream of 01. Upstream of 03.
**Proxy**: Paper 40 (Wall) reproduces the Raychaudhuri-based proof.

---

### Paper 03: The Four Laws of Black Hole Mechanics
- **File**: `03_Bardeen_Carter_Hawking_1973_Four_Laws.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1973
- **Relevance**: CRITICAL
- **Tags**: four laws, surface gravity, first law, Smarr formula, thermodynamic analogy
- **Source**: pre-arXiv stub

**Summary**: Established the four laws of black hole mechanics in precise analogy with thermodynamics. The first law delta M = (kappa/8 pi) delta A + Omega_H delta J + Phi_H delta Q defines the thermodynamic structure. At the time, the analogy was regarded as purely formal; Hawking 1975 promoted it to identity.

**Key Results**:
- Zeroth law: kappa constant on stationary horizon
- First law: delta M = (kappa/8 pi) delta A + Omega_H delta J + Phi_H delta Q
- Second law: delta A >= 0 (area theorem)
- Third law: impossible to reduce kappa to zero by finite operations
- Smarr formula: M = kappa A/(4 pi) + 2 Omega_H J + Phi_H Q

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| First law | delta M = (kappa/8 pi) delta A + Omega_H delta J + Phi_H delta Q | Main theorem |
| Smarr formula | M = kappa A/(4 pi) + 2 Omega_H J + Phi_H Q | Integral mass formula |
| Thermodynamic map | T <-> kappa/(2 pi), S <-> A/4 | Analogy (promoted by 05) |

**Dependencies**: Downstream of 01, 02, 11. Upstream of 04, 05, 07, 22, 35, 37, 40.
**Proxy**: Papers 37, 40 reproduce the four laws and their derivations.

---

### Paper 04: Black Hole Explosions?
- **File**: `04_Hawking_1974_BH_Explosions.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1974
- **Relevance**: CRITICAL
- **Tags**: Hawking radiation, black hole temperature, evaporation, primordial black holes
- **Source**: pre-arXiv stub

**Summary**: Brief Nature letter announcing that black holes radiate thermally at T = hbar c^3/(8 pi G M k_B). Promoted the BCH thermodynamic analogy to physical identity. Raised the information problem for the first time.

**Key Results**:
- Hawking temperature: T_H = hbar kappa/(2 pi k_B)
- Small BHs (M < 10^15 g) produce observable explosions
- Information question raised

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Hawking temperature | T_H = hbar c^3/(8 pi G M k_B) | Main result |
| Evaporation time | t_evap ~ G^2 M^3/(hbar c^4) | Order of magnitude |

**Dependencies**: Downstream of 03. Upstream of 05. Announcement preceding full derivation.
**Proxy**: Papers 37, 39, 44 reproduce the full calculation.

---

### Paper 05: Particle Creation by Black Holes
- **File**: `05_Hawking_1975_Particle_Creation.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1975
- **Relevance**: CRITICAL
- **Tags**: Bogoliubov coefficients, Hawking radiation, thermal spectrum, greybody factors, particle creation
- **Source**: pre-arXiv stub

**Summary**: Complete derivation of black hole radiation via Bogoliubov transformations. Traces positive-frequency modes at I+ back through the collapsing geometry to I-. The Bogoliubov relation |alpha|^2 = e^{2 pi omega/kappa}|beta|^2 yields a thermal spectrum with T = hbar kappa/(2 pi). Greybody factors modify the pure Planck spectrum.

**Key Results**:
- Full Bogoliubov derivation of Hawking radiation
- |alpha|^2 = e^{2 pi omega/kappa} |beta|^2 (thermal spectrum)
- <N_omega> = Gamma_omega/(e^{2 pi omega/kappa} - 1) (Planck with greybody)
- Fermions: Fermi-Dirac spectrum
- Back-reaction identified but unsolved

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Bogoliubov transformation | phi^out = alpha phi^in + beta phi_bar^in | Mode decomposition |
| Thermal relation | |alpha|^2 = e^{2 pi omega/kappa}|beta|^2 | Thermal spectrum condition |
| Hawking temperature | T_H = hbar kappa/(2 pi) | Main result |
| Planck spectrum | <N_omega> = Gamma_omega/(e^{2 pi omega/kappa} - 1) | Particle number |
| Surface gravity (Schw.) | kappa = 1/(4M) | G = c = 1 |

**Dependencies**: Downstream of 03, 04, 15. Upstream of 06, 07, 12. Foundation for all QFT-in-curved-spacetime.
**Proxy**: Paper 37 (Traschen) reproduces the entire calculation step-by-step. Paper 39 (Harlow) gives a concise version.

---

### Paper 06: Breakdown of Predictability in Gravitational Collapse
- **File**: `06_Hawking_1976_Breakdown_Predictability.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1976
- **Relevance**: CRITICAL
- **Tags**: information paradox, superscattering operator, unitarity, pure-to-mixed evolution
- **Source**: pre-arXiv stub

**Summary**: Argued that black hole formation + evaporation causes pure-to-mixed state evolution, violating unitarity. Introduced the superscattering operator $. Identified three options: (a) information lost, (b) subtle correlations in radiation, (c) remnants. Originally advocated (a); reversed in 2005 (Paper 10).

**Key Results**:
- Information paradox explicitly formulated
- Superscattering operator $ replaces S-matrix when unitarity fails
- Three logical resolutions identified
- Thermal density matrix rho_out = Z^{-1} e^{-beta H}

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Superscattering | rho_out = $ . rho_in | Central formalism |
| Unitary factorization | $_{AB,CD} = S_{AC} S*_{BD} (only if unitary) | Diagnostic |

**Dependencies**: Downstream of 05. Upstream of 10, 13, 18, 39, 44.
**Proxy**: Paper 39 (Harlow) gives the full information problem context.

---

### Paper 07: Cosmological Event Horizons, Thermodynamics and Particle Creation
- **File**: `07_Gibbons_Hawking_1977_Cosmological_Horizons.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1977
- **Relevance**: CRITICAL
- **Tags**: de Sitter, Gibbons-Hawking temperature, cosmological horizon entropy, Euclidean path integral
- **Source**: pre-arXiv stub

**Summary**: Extended Hawking radiation to cosmological horizons. De Sitter observers perceive thermal radiation at T = H/(2 pi). Derived via Euclidean path integral (4-sphere periodicity beta = 2 pi/H). Assigned entropy S_dS = pi/(G H^2) to the cosmological horizon.

**Key Results**:
- Gibbons-Hawking temperature: T_GH = H/(2 pi)
- De Sitter entropy: S_dS = A_H/(4G) = pi/(G H^2)
- Euclidean action: I_E = -pi/(G H^2)
- First law for cosmological horizons

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| GH temperature | T_GH = H/(2 pi) = (1/2 pi) sqrt(Lambda/3) | Main result |
| dS entropy | S_dS = pi/(G H^2) = 3 pi/(G Lambda) | BH entropy for cosmological horizon |
| Euclidean action | I_E = -pi/(G H^2) | 4-sphere saddle |
| Periodicity | beta = 2 pi/H | Euclidean regularity |

**Dependencies**: Downstream of 05. Upstream of 30, 31.
**Proxy**: No dedicated review; Paper 44 briefly covers dS thermodynamics.

---

### Paper 08: The Development of Irregularities in a Single Bubble Inflationary Universe
- **File**: `08_Hawking_1982_Inflation_Perturbations.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1982
- **Relevance**: MEDIUM
- **Tags**: inflation, perturbation spectrum, scale invariance, Harrison-Zeldovich
- **Source**: pre-arXiv stub

**Summary**: Computed the spectrum of density perturbations from quantum fluctuations during slow-roll inflation: delta rho/rho ~ H^2/phi_dot at horizon crossing. One of the first inflationary perturbation calculations.

**Key Results**:
- delta rho/rho ~ H^2/phi_dot ~ V^{3/2}/(M_P^3 V')
- Approximately scale-invariant (Harrison-Zeldovich) spectrum

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Perturbation amplitude | delta rho/rho ~ H^2/phi_dot | Main result |
| Scale invariance | n_s ~ 1 | Approximate |

**Dependencies**: Independent of BH thermodynamics line. Upstream of inflationary cosmology.
**Proxy**: Paper 43 (Baumann) reproduces the full calculation with modern formalism.

---

### Paper 09: Wave Function of the Universe
- **File**: `09_Hartle_Hawking_1983_Wave_Function.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1983
- **Relevance**: HIGH
- **Tags**: no-boundary proposal, Euclidean path integral, Wheeler-DeWitt, quantum cosmology
- **Source**: pre-arXiv stub

**Summary**: Proposed the no-boundary wave function: Psi[h_ij, phi] = integral over compact 4-geometries with a single boundary, weighted by e^{-I_E}. Replaces the initial singularity with smooth closure. The wave function satisfies the Wheeler-DeWitt equation and predicts inflation.

**Key Results**:
- No-boundary proposal: initial condition from Euclidean path integral
- Wave function satisfies Wheeler-DeWitt: H-hat Psi = 0
- Predicts inflationary phase from minisuperspace model
- No free parameters for initial conditions

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| No-boundary wave function | Psi = integral Dg DPhi e^{-I_E} over compact geometries | Main proposal |
| Wheeler-DeWitt | H-hat Psi = 0 | Constraint equation |
| Saddle-point (dS) | Psi ~ e^{3 pi/(G Lambda)} | WKB approximation |

**Dependencies**: Uses Euclidean methods from 07. Connected to 10 via path integral methods.
**Proxy**: No dedicated review. Harlow (39) discusses briefly.

---

### Paper 10: Information Loss in Black Holes
- **File**: `10_Hawking_2005_Information_Loss.md`
- **arXiv**: hep-th/0507171
- **Year**: 2005
- **Relevance**: HIGH
- **Tags**: information recovery, Euclidean path integral, topology, unitarity, AdS
- **Source**: PDF-sourced (full content available)

**Summary**: Hawking reverses his 1976 position. Argues quantum gravity is unitary: the path integral over trivially-topological metrics (S^1 x D^3) is unitary; over non-trivial topologies (S^2 x D^2) it loses information; but the total sum is unitary because at late times only trivial topology contributes. The "two-slit analogy" for spacetime topology.

**Key Results**:
- Euclidean path integral over trivial topology is unitary (by time-slicing)
- Non-trivial topology loses information but becomes subdominant
- Total path integral is unitary: information preserved
- Well-defined only in asymptotically AdS spacetimes
- Concedes bet to Preskill

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Partition function | Z(beta) = integral Dg Dphi e^{-I} = Tr(e^{-beta H}) | Eq. (2) |
| Microcanonical | Z(E_0) = integral d beta Z(beta) e^{beta E_0} | Eq. (3) |
| Trivial topology | S^1 x D^3 (periodically identified AdS) | Unitary sector |
| Non-trivial topology | S^2 x D^2 (Schwarzschild-AdS) | Info-losing sector |

**Dependencies**: Downstream of 06. Influenced by AdS/CFT (42).
**Proxy**: None needed (full PDF content available).

---

### Paper 11: Black Holes and Entropy
- **File**: `11_Bekenstein_1973_BH_Entropy.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1973
- **Relevance**: CRITICAL
- **Tags**: Bekenstein-Hawking entropy, generalized second law, Bekenstein bound, holographic
- **Source**: pre-arXiv stub

**Summary**: Proposed black hole entropy S_BH = eta (k_B c^3 / hbar G) A, with coefficient eta fixed to 1/4 by Hawking 1975. Established the generalized second law (GSL): total entropy S_ordinary + S_BH never decreases. Argued on information-theoretic grounds that entropy scales with area (holographic).

**Key Results**:
- Bekenstein-Hawking entropy: S = A/(4 l_P^2)
- GSL: delta(S_ordinary + S_BH) >= 0
- Bekenstein bound: S <= 2 pi k_B R E/(hbar c)
- Entropy scales with area, not volume (holographic)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| BH entropy | S_BH = A/(4 l_P^2) | Main result (coefficient from 05) |
| GSL | delta(S_ord + S_BH) >= 0 | Central proposal |
| Bekenstein bound | S <= 2 pi k_B R E/(hbar c) | Upper bound on entropy |
| Planck area | l_P^2 = hbar G/c^3 | Natural unit |

**Dependencies**: Upstream of 03, 05, 22, 40. Foundation for all gravitational entropy.
**Proxy**: Paper 40 (Wall) gives systematic GSL analysis. Paper 44 (Almheiri+) reviews entropy.

---

### Paper 12: Notes on Black-Hole Evaporation
- **File**: `12_Unruh_1976_BH_Evaporation.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1976
- **Relevance**: CRITICAL
- **Tags**: Unruh effect, Rindler observers, thermal vacuum, observer-dependent particles
- **Source**: pre-arXiv stub

**Summary**: Discovered the Unruh effect: a uniformly accelerated observer perceives the Minkowski vacuum as a thermal bath at T_U = hbar a/(2 pi c k_B). Demonstrated observer-dependence of particle number. The Rindler/Minkowski mode mixing is the same Bogoliubov mechanism as Hawking radiation, with kappa replaced by acceleration a.

**Key Results**:
- Unruh temperature: T_U = hbar a/(2 pi c k_B)
- Particle concept is observer-dependent
- Minkowski vacuum = thermal state for Rindler observer (from tracing over left wedge)
- Hawking-Unruh correspondence: kappa <-> a

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Unruh temperature | T_U = hbar a/(2 pi c k_B) | Main result |
| Rindler metric | ds^2 = -rho^2 d eta^2 + d rho^2 + dy^2 + dz^2 | Accelerated frame |
| Thermal density matrix | rho_R = Z^{-1} e^{-2 pi H_R/a} | Tracing left Rindler wedge |

**Dependencies**: Parallel to 05 (same mechanism, different geometry). Upstream of 38.
**Proxy**: Paper 38 (Crispino+) is a comprehensive review of the Unruh effect.

---

### Paper 13: Information in Black Hole Radiation
- **File**: `13_Page_1993_Information_BH_Radiation.md`
- **arXiv**: hep-th/9306083
- **Year**: 1993
- **Relevance**: CRITICAL
- **Tags**: Page curve, Page time, entanglement entropy, non-perturbative information, random state
- **Source**: PDF-sourced (full content available)

**Summary**: Defined the Page curve: entanglement entropy of Hawking radiation rises then falls, with turnover at the Page time when half the entropy has been radiated. Information escapes at non-perturbatively small rate ~e^{-4 pi/y^2}, invisible to finite-order perturbation theory.

**Key Results**:
- Page curve defines expected entanglement entropy trajectory
- Information rate: dI/dt ~ e^{-4 pi/y^2} (non-perturbative in M_Pl/M)
- Random pure state model: I_{m,n} = ln m + (m-1)/(2n) - Sum 1/k
- Page time divides evaporation into two phases

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Page information | I_{m,n} = ln m + (m-1)/(2n) - Sum_{k=n+1}^{mn} 1/k | Eq. (6) |
| For m <= n | I_{m,n} ~ m/(2n) ~ e^{s_r - s_h} | Eq. (7) |
| Information rate | I_r ~ exp(-4 pi E_0^2(3-8x)/(3+8x)) | Eq. (16) |
| Non-perturbative | dI/dt ~ e^{-4 pi/y^2}, y = M_Pl/E_0 | Eq. (19) |

**Dependencies**: Downstream of 06. Upstream of 14, 21, 39, 44.
**Proxy**: Paper 39 (Harlow) and Paper 44 (Almheiri+) review the Page curve extensively.

---

### Paper 14: Entanglement Wedge Reconstruction and the Information Problem
- **File**: `14_Penington_2019_Entanglement_Wedge.md`
- **arXiv**: 1905.08255
- **Year**: 2019
- **Relevance**: CRITICAL
- **Tags**: island formula, quantum RT surface, Page curve, entanglement wedge, scrambling time
- **Source**: PDF-sourced (full content available)

**Summary**: Shows a phase transition in the quantum RT surface at the Page time. The new surface lies slightly inside the horizon, and the entanglement wedge of the radiation includes part of the interior. Derives the Page curve from the RT formula and the Hayden-Preskill decoding criterion from entanglement wedge reconstruction.

**Key Results**:
- Quantum RT surface phase transition at Page time
- Island formula: S(R) = min{ext_I[Area(dI)/(4G) + S_bulk(R union I)]}
- Hayden-Preskill decoding from entanglement wedge reconstruction
- Interior operators are state-dependent near Page time
- No firewall (avoids AMPSS)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Island formula | S(R) = min{ext_I[Area(dI)/(4G) + S_bulk(R union I)]} | Eq. (1.1) |
| Scrambling time | t_scr = beta/(2 pi) log S_BH | Sec. 1 |
| Diary decoding | S_rad >= S_BH + S_d - E_d/T_H | Sec. 4 |

**Dependencies**: Downstream of 06, 13, 24. Upstream of 21, 23, 28, 30, 31, 44.
**Proxy**: Paper 44 (Almheiri+) is the comprehensive review.

---

### Paper 15: Quantized Fields and Particle Creation in Expanding Universes. I
- **File**: `15_Parker_1969_Particle_Creation_I.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1969
- **Relevance**: CRITICAL
- **Tags**: cosmological particle creation, Bogoliubov transformation, adiabatic vacuum, conformal coupling
- **Source**: pre-arXiv stub (key results reconstructed)

**Summary**: Parker's foundational discovery: expansion of the universe creates particles from the vacuum via Bogoliubov transformations. Particle number N_k = |beta_k|^2. Introduced the adiabatic vacuum (WKB-type mode functions). Massless conformally coupled scalars are NOT created in conformally flat spacetimes.

**Key Results**:
- Particle creation by expanding universe: N_k = |beta_k|^2
- Bosonic normalization: |alpha_k|^2 - |beta_k|^2 = 1
- Adiabatic vacuum: WKB mode functions minimize creation
- Conformal invariance: xi = 1/6 gives no creation for m = 0

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Bogoliubov | f_k^out = alpha_k f_k^in + beta_k f_k^{in*} | Sec. II |
| Normalization | |alpha_k|^2 - |beta_k|^2 = 1 | Sec. II |
| Particle number | N_k = |beta_k|^2 | Sec. II |
| Mode equation | chi_k'' + (k^2 + m^2 a^2 - a''/a) chi_k = 0 | Sec. II |

**Dependencies**: Upstream of 05, 16, 19, 25, 27. Foundation for all cosmological particle creation.
**Proxy**: Papers 19 (Ford), 25 (Parker-NS), 27 (Kolb-Long) review comprehensively. Paper 41 (Wald) covers foundations.

---

### Paper 16: Quantized Fields and Particle Creation in Expanding Universes. II
- **File**: `16_Parker_1971_Particle_Creation_II.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1971
- **Relevance**: CRITICAL
- **Tags**: fermionic particle creation, Pauli exclusion, spin-statistics, Dirac in FRW
- **Source**: pre-arXiv stub (key results reconstructed)

**Summary**: Extends Parker I to spin-1/2 fields. Fermionic Bogoliubov coefficients satisfy |alpha|^2 + |beta|^2 = 1 (plus sign, not minus), enforcing Pauli exclusion N_k <= 1. Spin-statistics connection essential for consistency. Massless fermions conformally invariant (no creation).

**Key Results**:
- Fermionic normalization: |alpha_k|^2 + |beta_k|^2 = 1
- Pauli exclusion: N_k <= 1 per mode
- Spin-statistics essential for consistency of particle creation
- Massless fermions: no creation in conformally flat spacetimes

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Fermionic Bogoliubov | u_k^out = alpha_k u_k^in + beta_k v_{-k}^in | Sec. II |
| Fermionic normalization | |alpha_k|^2 + |beta_k|^2 = 1 | Sec. II |
| Fermionic particle number | N_k = |beta_k|^2 <= 1 | Sec. II |

**Dependencies**: Downstream of 15. Upstream of 19, 25, 27.
**Proxy**: Papers 19, 25, 27.

---

### Paper 17: Thermodynamics of Spacetime: The Einstein Equation of State
- **File**: `17_Jacobson_1995_Thermodynamics_Spacetime.md`
- **arXiv**: gr-qc/9504004
- **Year**: 1995
- **Relevance**: CRITICAL
- **Tags**: Einstein equations from thermodynamics, Clausius relation, local Rindler horizon, equation of state
- **Source**: PDF-sourced (full content available)

**Summary**: Derives the Einstein equation from delta Q = T dS applied to local Rindler horizons, with S proportional to A and T = hbar kappa/(2 pi). Newton's constant emerges from the entropy-area proportionality. The cosmological constant appears as an integration constant. Argues gravity should not be canonically quantized -- it is an equation of state.

**Key Results**:
- Einstein equation derived from delta Q = T dS on all local Rindler horizons
- Newton's constant: G = (4 hbar eta)^{-1}
- Cosmological constant Lambda as integration constant
- Gravity is an equation of state, not a fundamental interaction

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Clausius relation | delta Q = T dS | Central thesis |
| Heat flux | delta Q = -kappa integral lambda T_ab k^a k^b d lambda dA | Eq. (2) |
| Area variation | delta A = -integral lambda R_ab k^a k^b d lambda dA | Eq. (5) |
| Einstein equation | R_ab - (1/2) R g_ab + Lambda g_ab = (2 pi / hbar eta) T_ab | Eq. (6) |

**Dependencies**: Downstream of 03, 11, 12. Upstream of 20, 32.
**Proxy**: None needed (full PDF content available).

---

### Paper 18: Black Holes: Complementarity vs. Firewalls
- **File**: `18_AMPS_2013_Firewalls.md`
- **arXiv**: 1207.3123
- **Year**: 2013
- **Relevance**: HIGH
- **Tags**: firewall paradox, entanglement monogamy, strong subadditivity, black hole complementarity
- **Source**: PDF-sourced (full content available)

**Summary**: Shows the three postulates of black hole complementarity (unitarity, EFT outside horizon, no drama at horizon) are mutually inconsistent after the Page time. Strong subadditivity forbids a mode being maximally entangled with two independent systems. The "most conservative" resolution is a firewall at the horizon.

**Key Results**:
- Three BHC postulates are mutually inconsistent
- Strong subadditivity: S(B) + S(ABR_B) <= S(AB) + S(BR_B)
- Firewall resolution: give up equivalence principle at horizon
- Mining experiments extend argument to all modes

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Strong subadditivity | S(B) + S(ABR_B) <= S(AB) + S(BR_B) | Sec. 2 |
| Contradiction | S(B) <= 0 (impossible) | Sec. 2 |

**Dependencies**: Downstream of 06, 13. Upstream of 36.
**Proxy**: Paper 39 (Harlow) and Paper 44 (Almheiri+) cover the firewall argument.

---

### Paper 19: Cosmological Particle Production: A Review
- **File**: `19_Ford_2021_Cosmological_Particle_Production.md`
- **arXiv**: 2112.02444
- **Year**: 2021
- **Relevance**: HIGH
- **Tags**: particle creation review, Bogoliubov, adiabatic, sudden transition, analog models
- **Source**: PDF-sourced (full content available)

**Summary**: Comprehensive review of quantum particle creation in expanding universes. Covers the full Bogoliubov formalism, adiabatic vs. sudden limits, conformal coupling, applications to inflation, and analog models (BEC, dynamical Casimir, superconducting circuits).

**Key Results**:
- Complete Bogoliubov formalism for FRW spacetimes
- Adiabatic suppression: |beta_k|^2 ~ exp(-pi omega^2/omega_dot)
- Sudden transition: |beta_k|^2 approx (omega^in - omega^out)^2/(4 omega^in omega^out)
- Analog models validate the mechanism experimentally

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Mode equation | chi_k'' + [k^2 + m^2 a^2 - (1-6 xi) a''/a] chi_k = 0 | Sec. II |
| Adiabatic suppression | |beta_k|^2 ~ exp(-pi omega_k^2/omega_dot_k) | Sec. III |
| Sudden transition | |beta_k|^2 approx (omega^in - omega^out)^2/(4 omega^in omega^out) | Sec. III |
| Number density | n = (2 pi)^{-3} integral d^3k |beta_k|^2 | Sec. II |

**Dependencies**: Downstream of 15, 16. Reviews and extends 15, 16.
**Proxy**: N/A (this IS the review).

---

### Paper 20: Entropy and the Spectral Action
- **File**: `20_Chamseddine_Connes_vS_2019_Entropy_Spectral_Action.md`
- **arXiv**: 1809.02944
- **Year**: 2019
- **Relevance**: CRITICAL
- **Tags**: spectral action, von Neumann entropy, KMS state, Riemann zeta function, NCG
- **Source**: PDF-sourced (full content available)

**Summary**: THE critical paper for the framework. Proves that the von Neumann entropy of the fermionic second quantization of a spectral triple equals the spectral action for the universal function h(x) = x/(1+e^x) + log(1+e^{-x}). The heat expansion coefficients involve the Riemann xi function: c(4) ~ zeta(5), c(2) ~ zeta(3). Functional equation gives UV/IR duality.

**Key Results**:
- S_vN = Tr(h(beta D)) -- entropy IS the spectral action
- h(x) = x/(1+e^x) + log(1+e^{-x}) is the universal entropy function
- Heat coefficients: gamma(a) = (1-2^{-2a})/a pi^{-a} xi(2a)
- c(4) = 225 zeta(5)/4, c(2) = 9 zeta(3)/2
- Entropy is additive for direct sums of spectral triples

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Entropy = Spectral Action | S(phi_beta) = Tr(h(beta D)) | Theorem 3.4 |
| Entropy function | h(x) = x/(1+e^x) + log(1+e^{-x}) | Sec. 4 |
| Binary entropy | E(x) = (log(x+1) - x log x)/(x+1) | Lemma 3.1 |
| Moments | integral_0^inf h(x) x^alpha dx = (1-2^{-alpha-1})/(alpha+1) Gamma(alpha+3) zeta(alpha+2) | Lemma 4.5 |
| Heat coefficient | gamma(a) = (1-2^{-2a})/a pi^{-a} xi(2a) | Lemma 4.6 |

**Dependencies**: Downstream of 11, 17 (conceptually). Bridge paper connecting NCG to BH thermodynamics.
**Proxy**: None needed (full PDF content available).

---

### Paper 21: Replica Wormholes and the Entropy of Hawking Radiation
- **File**: `21_AHMST_2020_Replica_Wormholes.md`
- **arXiv**: 1911.12333
- **Year**: 2020
- **Relevance**: HIGH
- **Tags**: replica wormholes, island rule, Page curve, JT gravity, gravitational path integral
- **Source**: PDF-sourced (full content available)

**Summary**: Derives the island rule from replica wormholes in the gravitational path integral. Replica wormholes are new saddles connecting n copies of the spacetime. In the n->1 limit, they produce the island contribution. The Page curve is reproduced by competition between the no-island (growing) and island (decreasing) saddles.

**Key Results**:
- Replica wormholes resolve the information paradox via the gravitational path integral
- Island rule emerges from n->1 limit of replica wormholes
- Page curve from two competing saddles
- First gravitational path integral derivation of the Page curve

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Island rule | S(R) = min{ext_I[Area(dI)/(4G) + S_bulk(R union I)]} | Eq. (1.2) |
| Replica trick | S = -lim_{n->1} d/dn Tr(rho^n) | Sec. 2 |
| Wormhole weight | ~ e^{(1-n) S_0} | Sec. 2 |

**Dependencies**: Downstream of 13, 14, 24. Parallel to 14.
**Proxy**: Paper 44 (Almheiri+) is the comprehensive review.

---

### Paper 22: Black Hole Entropy is the Noether Charge
- **File**: `22_Wald_1993_BH_Entropy_Noether.md`
- **arXiv**: gr-qc/9307038
- **Year**: 1993
- **Relevance**: HIGH
- **Tags**: Wald entropy, Noether charge, first law, diffeomorphism invariance, higher-derivative gravity
- **Source**: PDF-sourced (full content available)

**Summary**: In any diffeomorphism-invariant gravity theory, the first law holds with entropy S = 2 pi integral_Sigma Q-tilde, the Noether charge of the horizon Killing field on the bifurcation surface. For GR this gives A/(4G). For higher-derivative theories, the Wald formula generalizes Bekenstein-Hawking.

**Key Results**:
- S = 2 pi integral_Sigma Q-tilde for any diffeomorphism-invariant Lagrangian
- First law (kappa/2 pi) delta S = delta E - Omega_H delta J holds universally
- Entropy is a local geometrical quantity on the horizon
- Euclidean and Noether charge approaches give identical results

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Wald entropy | S = 2 pi integral_Sigma Q-tilde | Eq. (26) |
| First law | (kappa/2 pi) delta S = delta E - Omega_H delta J | Eq. (25) |
| Noether current | j = Theta(phi, L_xi phi) - xi . L | Eq. (7) |

**Dependencies**: Downstream of 03, 11. Upstream of 40.
**Proxy**: None needed (full PDF content available).

---

### Paper 23: Islands in Cosmology
- **File**: `23_Hartman_Jiang_Shaghoulian_2020_Islands_Cosmology.md`
- **arXiv**: 2008.01022
- **Year**: 2020
- **Relevance**: MEDIUM
- **Tags**: islands, cosmology, Bekenstein bound, crunching universe, FRW, tensor networks
- **Source**: PDF-sourced (full content available)

**Summary**: Studies conditions for islands in cosmological settings. Three necessary conditions: Bekenstein bound violation, quantum normality of island and complement. Islands appear in crunching universes (FRW with Lambda < 0 near turning point) but NOT in eternally expanding (dS) spacetimes.

**Key Results**:
- Three necessary conditions for islands derived
- Islands exist in crunching cosmologies near turning point
- No islands in eternally expanding universes
- Tensor network models illustrate island emergence

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Island rule | S(R) = min{ext_I[Area(dI)/(4G) + S_bulk(R union I)]} | Sec. 2 |
| Bekenstein violation | S_bulk(I) > Area(dI)/(4G) | Condition 1 |

**Dependencies**: Downstream of 14, 21.
**Proxy**: None needed (full PDF content available).

---

### Paper 24: Quantum Extremal Surfaces
- **File**: `24_Engelhardt_Wall_2014_QES.md`
- **arXiv**: 1408.3203
- **Year**: 2015
- **Relevance**: HIGH
- **Tags**: quantum extremal surface, generalized entropy, holographic entanglement, quantum focussing
- **Source**: PDF-sourced (full content available)

**Summary**: Proposes the quantum extremal surface (QES): a surface extremizing the generalized entropy S_gen = Area/(4G) + S_bulk. Provides an all-orders prescription for holographic entanglement entropy. QES lie deeper than causal surfaces. Barriers to QES exist.

**Key Results**:
- QES: extremizes generalized entropy (area + bulk entanglement)
- Agrees with FLM formula at O(G^0)
- QES lies deeper than causal surfaces
- Quantum focussing conjecture

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Generalized entropy | S_gen(X) = Area(X)/(4G) + S_bulk(Sigma_X) | Eq. (1) |
| QES condition | delta S_gen / delta X = 0 | Definition |
| Quantum focussing | d^2 S_gen/(dV_1 dV_2) <= 0 | Sec. 4 |

**Dependencies**: Upstream of 14, 21, 23, 28, 30, 31, 44.
**Proxy**: Paper 44 (Almheiri+) reviews in full context.

---

### Paper 25: Fifty Years of Cosmological Particle Creation
- **File**: `25_Parker_Navarro-Salas_2017_Fifty_Years.md`
- **arXiv**: 1702.07132
- **Year**: 2017
- **Relevance**: HIGH
- **Tags**: historical review, particle creation, graviton creation, conformal invariance, Bunch-Davies
- **Source**: PDF-sourced (full content available)

**Summary**: Historical review (interview format) of Parker's discovery. Covers conformal invariance, graviton creation (not conformally invariant), deep consistency between GR and QFT, and trans-Planckian universality. The initial Minkowski vacuum evolves into the Bunch-Davies vacuum to 200+ digit accuracy.

**Key Results**:
- Conformally invariant massless fields produce zero particles in isotropic expansion
- Gravitons ARE created (linearized gravity not conformal)
- Deep consistency: created spectrum self-consistent with producing spacetime
- Trans-Planckian universality confirmed

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Bogoliubov | a-hat_out = alpha a-hat_in + beta a-hat-dagger_in | Sec. II |
| Conformal scalar | (Box - R/6) phi = 0 | Penrose equation |

**Dependencies**: Downstream of 15, 16. Reviews the Parker program.
**Proxy**: N/A (this IS the historical review).

---

### Paper 26: Observation of Thermal Hawking Radiation in an Analogue Black Hole
- **File**: `26_Steinhauer_2019_Analog_Hawking_BEC.md`
- **arXiv**: 1809.00913
- **Year**: 2019
- **Relevance**: HIGH
- **Tags**: analog black hole, BEC, Hawking temperature measurement, thermal spectrum, no firewall
- **Source**: PDF-sourced (full content available)

**Summary**: First quantitative experimental confirmation of the Hawking temperature. BEC of Rb-87 atoms creates a sonic horizon; the measured correlation spectrum is thermal (Planckian) at T_H = 0.35 nK with no free parameters. No analog firewall observed.

**Key Results**:
- Measured T_H = 0.35 nK (agrees with surface gravity prediction)
- Thermal spectrum with no free parameters
- Radiation in linear-dispersion regime
- No analog firewall at horizon

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Hawking T (BEC) | k_B T_H = -(hbar/2 pi)(c/n dn/dx + dc/dx)|_{x=0} | Eq. (1) |
| Planck spectrum | |beta|^2 = 1/(e^{hbar omega / k_B T_H} - 1) | Below Eq. (1) |

**Dependencies**: Experimental validation of 05 and 12.
**Proxy**: None needed (full PDF content available).

---

### Paper 27: Cosmological Gravitational Particle Production
- **File**: `27_Kolb_Long_2023_CGPP.md`
- **arXiv**: 2312.09042
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: CGPP review, all spins, dark matter, WIMPzilla, gravitational reheating
- **Source**: PDF-sourced (full content available)

**Summary**: Comprehensive modern review of CGPP. Catalogs results for spins 0 through 2. Production requires broken conformal symmetry. CGPP can produce superheavy dark matter (WIMPzillas) and reheat the universe purely through gravitational production.

**Key Results**:
- CGPP universal for any species with broken conformal invariance
- Higher-spin particles have enhanced production (longitudinal modes)
- CGPP can produce particles with m up to ~H_end ~ 10^14 GeV
- Superheavy dark matter from pure gravitational production

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Mode equation | v_k'' + [k^2 + m^2 a^2 - (xi-1/6) a^2 R] v_k = 0 | Sec. III.A |
| Abundance | Omega_chi h^2 proportional to (m/H_end)(H_end/M_Pl)^2 | Sec. IV.C |

**Dependencies**: Downstream of 15, 16. Modern catalog extending the Parker program.
**Proxy**: N/A (this IS the modern review).

---

### Paper 28: Compactified Extra Dimension and Entanglement Island
- **File**: `28_Hung_Nam_2023_KK_Entanglement_Island.md`
- **arXiv**: 2303.00348
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: KK, extra dimensions, entanglement island, black string, double Wick rotation
- **Source**: PDF-sourced (full content available)

**Summary**: Shows compactified extra dimensions + islands resolve the deepest BH puzzles. Double Wick rotation between time and compact dimension removes the singularity. Smooth bubbles serve as entropy microstates. Island slightly outside event horizon of black string; Page curve reproduced.

**Key Results**:
- Double Wick rotation removes singularity (smooth bubble behind horizon)
- Smooth bubbles = entropy microstates
- Island slightly outside event horizon of black string
- Page curve reproduced: S saturates at 2 S_BH

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Double Wick metric | h(r) = (1-r_S/r)(1-r_B/r) | Eq. (7) |
| Island formula | S(R) = min ext_I[A(dI)/(4G) + S_mat(R union I)] | Eq. (1) |

**Dependencies**: Downstream of 14, 21. Applies islands to KK geometry.
**Proxy**: None needed (full PDF content available).

---

### Paper 29: Radiation from a Moving Mirror
- **File**: `29_Fulling_Davies_1976_Moving_Mirror.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1976
- **Relevance**: MEDIUM
- **Tags**: moving mirror, Schwarzian derivative, conformal anomaly, 1+1D, particle creation
- **Source**: pre-arXiv stub

**Summary**: Moving mirror in (1+1)D flat spacetime creates particles via time-dependent boundary conditions. Energy flux proportional to the Schwarzian derivative. Exponentially receding mirror produces thermal spectrum. Simplest exactly solvable model of particle creation without curvature.

**Key Results**:
- Energy flux: <T_uu> = -(1/24 pi){p(u), u}
- Exponential trajectory gives thermal radiation at Hawking T
- Conformal anomaly is mathematical origin

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Energy flux | <T_uu> = -(1/24 pi){p(u), u} | Main result |
| Schwarzian | {f,u} = f'''/f' - (3/2)(f''/f')^2 | Definition |

**Dependencies**: Parallel to 05, 12 (flat-space analog). Upstream of 45.
**Proxy**: Paper 45 (Dodonov) reviews in DCE context.

---

### Paper 30: Islands and the de Sitter Entropy Bound
- **File**: `30_Teresi_2022_Islands_dS_Entropy.md`
- **arXiv**: 2112.03922
- **Year**: 2022
- **Relevance**: MEDIUM
- **Tags**: de Sitter, entropy bound, islands, Page curve, JT gravity
- **Source**: PDF-sourced (full content available)

**Summary**: Uses the island formula to compute fine-grained entropy for a Minkowskian observer after inflation in 2D JT gravity. Entropy follows a Page-like curve, never exceeding S_dS. Suggests the dS entropy bound may not exist.

**Key Results**:
- Fine-grained entropy follows Page-like curve in dS
- Entropy never exceeds thermodynamic dS entropy
- Dominant island in distant past

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| JT action | S_JT = (1/16 pi G) integral [phi_0 R + phi(R - 2H^2)] | Eq. (1) |
| Island entropy | S = 2 phi_0 + 2 phi_r tan sigma_I + S_semi(R union I) | Eq. (14) |

**Dependencies**: Downstream of 14, 21. In tension with 31.
**Proxy**: None needed.

---

### Paper 31: No Page Curves for the de Sitter Horizon
- **File**: `31_Shaghoulian_2021_No_Page_Curves_dS.md`
- **arXiv**: 2108.09318
- **Year**: 2021
- **Relevance**: MEDIUM
- **Tags**: de Sitter, Page curve, backreaction, catastrophic, static patch
- **Source**: PDF-sourced (full content available)

**Summary**: Catastrophic backreaction at the Page time forms a trapped region, preventing either the static patch observer or the meta-observer from seeing unitary evaporation. In tension with Paper 30.

**Key Results**:
- Meta-observer at I+ sees pure state
- Catastrophic backreaction at Page time: t_Page = t_trapped = 6 ell/(c G)
- Neither observer sees unitary evaporation in practice

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Page time | t_Page = 6 ell/(c G) | Eq. (3.18) |
| Trapped condition | d_+/- Phi < 0 | Eq. (5.11) |

**Dependencies**: Downstream of 14, 21. In tension with 30.
**Proxy**: None needed.

---

### Paper 32: On the Origin of Gravity and the Laws of Newton
- **File**: `32_Verlinde_2010_Entropic_Gravity.md`
- **arXiv**: 1001.0785
- **Year**: 2010
- **Relevance**: MEDIUM
- **Tags**: entropic gravity, holographic screens, emergent gravity, Newton's law
- **Source**: PDF-sourced (full content available)

**Summary**: Derives Newton's laws from entropic force F Delta x = T Delta S on holographic screens. Uses Unruh temperature and equipartition to recover F = GMm/R^2. Relativistic generalization gives Einstein equations. Argues gravity is emergent.

**Key Results**:
- F = ma from Unruh temperature + entropy postulate
- F = GMm/R^2 from holographic screen area + equipartition
- Einstein equations from first law on general screens

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Entropic force | F Delta x = T Delta S | Sec. 2 |
| Entropy postulate | Delta S = 2 pi k_B (mc/hbar) Delta x | Eq. (3.6) |
| Equipartition | E = (1/2) N k_B T | Eq. (3.11) |

**Dependencies**: Downstream of 17. Extends Jacobson's program.
**Proxy**: None needed.

---

### Paper 33: Kaluza-Klein Schwinger Effect
- **File**: `33_Yamada_2024_KK_Schwinger.md`
- **arXiv**: 2403.13451
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: KK Schwinger, compact dimensions, non-perturbative production, modulus trapping
- **Source**: PDF-sourced (full content available)

**Summary**: Electric fields in compact spaces produce KK particles non-perturbatively even when E << M_KK^2. Production condition: |Delta zeta| > M_KK. Each KK mode crossing zero mass is produced at Schwinger rate. Backreaction traps the gauge potential. 4D EFT truncated at KK scale fails.

**Key Results**:
- KK particles produced non-perturbatively when |Delta zeta| > M_KK
- Schwinger rate: <N_{n,k}> = exp(-pi k^2/(qE))
- Parametric amplification in oscillatory models
- Backreaction causes modulus trapping
- 4D EFT fails during KK Schwinger effect

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| KK mass | M_n^2(t) = (n + q zeta(t))^2/(2 pi R)^2 | Eq. (5) |
| Mode equation | f-double-dot_{n,k} + (k^2 + M_n^2(t)) f_{n,k} = 0 | Eq. (8) |
| Schwinger rate | <N_{n,k}> = exp(-pi k^2/(qE)) | Eq. (15) |
| Backreaction | zeta-double-dot_c + Sum_n 2q(n M_KK + q zeta_c)<|phi-hat_n|^2>_ren = 0 | Eq. (16) |

**Dependencies**: Extends 15 to compact dimensions. Directly relevant to Schwinger-instanton duality.
**Proxy**: None needed.

---

### Paper 34: An Accelerating Universe from Dynamical Compactification
- **File**: `34_Darabi_2003_Dynamical_Compactification.md`
- **arXiv**: gr-qc/0301075
- **Year**: 2003
- **Relevance**: HIGH
- **Tags**: KK cosmology, dynamical compactification, decaying Lambda, Wheeler-DeWitt, exflation precursor
- **Source**: PDF-sourced (full content available)

**Summary**: Direct KK cosmology precursor to exflation. Coupled (4+D)-dimensional metric gives exponential solutions: R(t) ~ e^{Ht} (4D expansion) and a(t) ~ e^{beta t} (internal compactification). Hamiltonian constraint requires opposite signs for expansion and compactification. Decaying Lambda ~ R^{-2}. WDW wave functions peak on classical trajectories.

**Key Results**:
- Exponential solutions: expanding 4D + compactifying internal space
- Hamiltonian constraint links expansion and compactification rates
- Dimension-dependent compactification: higher D means slower compactification
- WDW solutions match classical trajectories

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Solutions | R = l_P e^{Ht}, a = l_P e^{beta t} | Eqs. (29-30) |
| Hamiltonian constraint | (1/2) alpha^2 + D(D-1) beta^2/12 + D alpha beta/2 = 0 | Eq. (24) |
| Decaying Lambda | Lambda(R) = 3/R^2 | Eq. (10) |

**Dependencies**: Independent KK cosmology. Direct precursor to the framework.
**Proxy**: None needed.

---

### Paper 35: Thermodynamics of Black Holes in Anti-de Sitter Space
- **File**: `35_Hawking_Page_1983_AdS_Phase_Transition.md`
- **arXiv**: N/A (pre-arXiv)
- **Year**: 1983
- **Relevance**: HIGH
- **Tags**: Hawking-Page transition, AdS black hole, phase transition, free energy, Euclidean path integral
- **Source**: pre-arXiv stub

**Summary**: First-order phase transition between thermal AdS and large Schwarzschild-AdS black hole at T_HP = 1/(pi ell). Large AdS BHs have positive specific heat (stable); small ones have negative (unstable). Later reinterpreted by Witten as confinement-deconfinement in dual gauge theory.

**Key Results**:
- HP transition at T_HP = 1/(pi ell)
- Large AdS BHs: positive specific heat
- Euclidean saddle-point change at transition
- Reinterpreted as confinement-deconfinement in AdS/CFT

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| HP temperature | T_HP = 1/(pi ell) | Main result |
| Free energy | F = r_+/4 (1 - r_+^2/ell^2) | Main result |
| Transition | F = 0 implies r_+ = ell | Phase boundary |

**Dependencies**: Downstream of 03. Upstream of 42.
**Proxy**: Paper 42 (Witten) covers the AdS/CFT reinterpretation.

---

### Paper 36: An Apologia for Firewalls
- **File**: `36_AMPS_2013_Apologia_Firewalls.md`
- **arXiv**: 1304.6483
- **Year**: 2013
- **Relevance**: MEDIUM
- **Tags**: firewall defense, interior embedding, nonlocality, mining, AdS black holes
- **Source**: PDF-sourced (full content available)

**Summary**: Defends the firewall argument. Shows embedding interior modes in early radiation is inconsistent. Nonlocal theories must be dramatically nonlocal. Mining experiments extend the argument to all modes. Even eternal AdS BHs have interior problems after scrambling time.

**Key Results**:
- Embedding B-tilde in E is inconsistent
- Nonlocality must be dramatic to avoid firewalls
- Mining experiments sharpen argument
- Eternal AdS BHs also have problems after t_scr

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Scrambling time | t_scr ~ beta log S_BH | Sec. 5 |

**Dependencies**: Downstream of 18. Defends and extends AMPS.
**Proxy**: Paper 39 covers the full firewall arc.

---

### Paper 37: An Introduction to Black Hole Evaporation
- **File**: `37_Traschen_2000_Intro_BH_Evaporation.md`
- **arXiv**: gr-qc/0010055
- **Year**: 2000
- **Relevance**: HIGH
- **Tags**: review, Bogoliubov derivation, Rindler, Hawking calculation, RNdS, BPS
- **Source**: PDF-sourced (full content available)

**Summary**: Step-by-step reproduction of Hawking's calculation. Develops the full Bogoliubov formalism from scratch, then applies it to accelerated observers (Rindler/Unruh), gravitational collapse (Hawking 1975), eternal Schwarzschild, and charged BHs in dS. Also covers BPS stability.

**Key Results**:
- Complete step-by-step Hawking calculation reproduced
- Key geometric optics relation: v_0 - v = C^2 e^{-kappa u}
- Generalized spectrum: <N> = Gamma/(e^{2 pi(omega - mu)/kappa} +/- 1)
- Extremal BHs are stable endpoints of evaporation

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| KG inner product | (f,h) = -i integral d^3x sqrt(-g) (f h-dot* - f-dot h*) | Eq. 2.5 |
| Key relation | v_0 - v = C^2 e^{-kappa u} | Eq. 5.57 |
| Hawking spectrum | <N> = Gamma_omega/(e^{2 pi omega/kappa} - 1) | Eq. 5.65 |

**Dependencies**: Reviews 03, 05, 12. **Covers originals**: 03, 05, 11, 12.
**Proxy**: N/A (this IS the review).

---

### Paper 38: The Unruh Effect and its Applications
- **File**: `38_Crispino_Higuchi_Matsas_2008_Unruh_Effect.md`
- **arXiv**: 0710.5373
- **Year**: 2008
- **Relevance**: HIGH
- **Tags**: Unruh effect review, Rindler, Bogoliubov, detectors, proton decay, Bisognano-Wichmann
- **Source**: PDF-sourced (full content available)

**Summary**: Comprehensive 30-year review of the Unruh effect. Complete Bogoliubov coefficient derivation. The Minkowski vacuum as entangled thermal state over Rindler Fock spaces. Applications: Unruh-DeWitt detectors, weak decay of accelerated protons, bremsstrahlung. Bisognano-Wichmann theorem: thermality holds for any Wightman QFT.

**Key Results**:
- Complete derivation of Minkowski vacuum as entangled Rindler thermal state
- Bisognano-Wichmann: thermality holds for arbitrary Wightman QFTs
- Accelerated proton beta decay as physical consequence
- Required acceleration ~10^25 m/s^2 for T ~ 1 K

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Crucial Bogoliubov | beta^L_{omega k} = -e^{-pi omega/a} alpha^{R*}_{omega k} | Eq. 2.60 |
| Vacuum annihilation | (a^R_{+omega} - e^{-pi omega/a} a^{L dag}_{+omega})|0_M> = 0 | Eq. 2.66 |
| Entangled vacuum | |0_M> = Prod C_i Sum e^{-pi n omega/a}|n,R> tensor |n,L> | Eq. 2.76 |

**Dependencies**: Reviews 12. **Covers original**: 12.
**Proxy**: N/A (this IS the review).

---

### Paper 39: Jerusalem Lectures on Black Holes and Quantum Information
- **File**: `39_Harlow_2014_Jerusalem_Lectures_BH_QI.md`
- **arXiv**: 1409.1231
- **Year**: 2014
- **Relevance**: HIGH
- **Tags**: lectures, information problem, Page curve, AMPS, scrambling, complementarity, RT formula
- **Source**: PDF-sourced (full content available)

**Summary**: Comprehensive lectures covering the full black hole information problem arc. Reproduces Hawking's calculation, Page curve, scrambling, AMPS, Harlow-Hayden computational complexity, and RT formula. The most pedagogically complete single reference for the information paradox.

**Key Results**:
- Full information problem arc reproduced
- Page curve: S_rad(t) = min(S_rad^thermal, S_BH)
- Scrambling time: t_scr ~ M log M
- Harlow-Hayden computational complexity argument
- RT formula: S(A) = Area(gamma_A)/(4G)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Hawking temperature | T_H = 1/(8 pi G M) | Sec. 4.3 |
| Page curve | S_rad = min(S_rad^therm, S_BH) | Sec. 5.2 |
| Scrambling time | t_scr ~ M log M | Sec. 5.6 |
| RT formula | S(A) = Area(gamma_A)/(4G) | Sec. 6.10 |

**Dependencies**: Reviews 05, 06, 13, 18. **Covers originals**: 05, 06, 11, 12, 13, 18, 35.
**Proxy**: N/A (this IS the review).

---

### Paper 40: Ten Proofs of the Generalized Second Law
- **File**: `40_Wall_2009_Ten_Proofs_GSL.md`
- **arXiv**: 0901.3865
- **Year**: 2009
- **Relevance**: HIGH
- **Tags**: GSL, ten proofs, Raychaudhuri, relative entropy, quasi-stationary, Gibbs vs Boltzmann
- **Source**: PDF-sourced (full content available)

**Summary**: Systematic examination of ten distinct proof strategies for the GSL. Covers classical, hydrodynamic, semiclassical, and full QG regimes. The monotonicity of relative entropy is the most rigorous backbone. Distinguishes quasi-stationary from quasi-steady regimes. No fully satisfactory proof in all regimes.

**Key Results**:
- S_gen = A/(4G) + S_out (generalized entropy)
- Ten proof strategies classified by regime and limitations
- Monotonicity of relative entropy: key mathematical tool
- GSL applies to event horizons, not arbitrary null surfaces

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Generalized entropy | S_gen = k A/(4 G hbar) + S_out | Eq. 1 |
| Raychaudhuri | -d theta/d lambda = theta^2/2 + sigma^2 + 8 pi G T_ab k^a k^b | Eq. 11 |
| First law (compact) | dE' = T dS_BH | Eq. 9 |

**Dependencies**: Downstream of 02, 03, 11, 22. **Covers originals**: 02, 03, 11.
**Proxy**: N/A (this IS the review).

---

### Paper 41: The Formulation of Quantum Field Theory in Curved Spacetime
- **File**: `41_Wald_2009_QFT_Curved_Spacetime.md`
- **arXiv**: 0907.0416
- **Year**: 2009
- **Relevance**: HIGH
- **Tags**: algebraic QFT, microlocal spectrum condition, Hadamard states, OPE, local covariance
- **Source**: PDF-sourced (full content available)

**Summary**: Addresses fundamental obstacles to QFT in curved spacetime. Resolutions: algebraic approach (*-algebra + GNS), microlocal spectrum condition (Hadamard states), local covariance (replaces Poincare), OPE (replaces vacuum axiom). Normal ordering fails. PCT theorem in curved spacetime.

**Key Results**:
- Only spacelike commutativity generalizes from Wightman axioms
- Algebraic approach resolves Hilbert space ambiguity
- Microlocal spectrum condition replaces positivity of energy
- OPE replaces Poincare-invariant vacuum axiom
- Normal ordering fails in curved spacetime

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| State (algebraic) | omega(A) = <Psi|pi(A)|Psi> | Eq. 10 |
| GNS inner product | (A_1, A_2) = omega(A_1* A_2) | Eq. 11 |
| OPE | phi(x_1) phi(x_2) = H(x_1,x_2) 1 + phi^2(y) + ... | Eq. 13 |

**Dependencies**: Foundational formalism. **Covers foundations**: 12, 15.
**Proxy**: N/A (this IS the review).

---

### Paper 42: Anti de Sitter Space and Holography
- **File**: `42_Witten_1998_AdS_Holography.md`
- **arXiv**: hep-th/9802150
- **Year**: 1998
- **Relevance**: HIGH
- **Tags**: AdS/CFT, holographic dictionary, mass-dimension, KK spectrum, Hawking-Page, Wilson loops
- **Source**: PDF-sourced (full content available)

**Summary**: Established the precise AdS/CFT dictionary: CFT correlators = dependence of supergravity action on boundary data. Mass-dimension relation Delta(Delta-d) = m^2. Matched full KK spectrum of Type IIB on AdS_5 x S^5 with chiral operators of N=4 SYM. Identified HP transition as confinement-deconfinement.

**Key Results**:
- AdS/CFT dictionary: <e^{integral phi_0 O}>_CFT = Z_S(phi_0)
- Mass-dimension: Delta(Delta-d) = m^2
- KK spectrum matches chiral operators
- HP transition = confinement-deconfinement
- Breitenlohner-Freedman bound: m^2 >= -d^2/4

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| AdS/CFT ansatz | <e^{integral phi_0 O}> = exp(-I_S(phi)) | Eq. (2.11) |
| Mass-dimension | Delta(Delta-d) = m^2 | Eq. (2.43) |
| Operator dimension | Delta = (1/2)(d + sqrt(d^2 + 4m^2)) | Eq. (2.44) |

**Dependencies**: Downstream of 35. Upstream of 10, 14, 21, 39.
**Proxy**: None needed.

---

### Paper 43: TASI Lectures on Inflation
- **File**: `43_Baumann_2009_TASI_Inflation.md`
- **arXiv**: 0907.5424
- **Year**: 2009
- **Relevance**: MEDIUM
- **Tags**: inflation lectures, perturbation theory, slow-roll, n_s, r, non-Gaussianity, eta problem
- **Source**: PDF-sourced (full content available)

**Summary**: Comprehensive pedagogical treatment of inflationary cosmology. Full derivation of scalar and tensor perturbation spectra. Slow-roll parameters, spectral indices, Lyth bound, Maldacena theorem on non-Gaussianity, and the eta problem. The benchmark for comparing alternative mechanisms.

**Key Results**:
- Scalar spectrum: Delta_s^2 = H^2/(8 pi^2 epsilon M_Pl^2)
- Spectral index: n_s - 1 = -6 epsilon + 2 eta
- Consistency relation: r = -8 n_t
- Lyth bound: Delta phi/M_Pl >= (r/0.01)^{1/2}
- Maldacena: f_NL ~ O(epsilon, eta) for single-field slow-roll

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Mukhanov-Sasaki | v'' + (k^2 - z''/z) v = 0 | Lecture 2 |
| Scalar spectrum | Delta_s^2 = H^2/(8 pi^2 epsilon M_Pl^2) | Lecture 2 |
| Spectral index | n_s - 1 = -6 epsilon + 2 eta | Lecture 2 |
| Tensor-to-scalar | r = 16 epsilon | Lecture 2 |

**Dependencies**: Extends 08. **Covers original**: 08.
**Proxy**: N/A (this IS the review).

---

### Paper 44: The Entropy of Hawking Radiation
- **File**: `44_Almheiri_2020_Entropy_Hawking_Radiation.md`
- **arXiv**: 2006.06872
- **Year**: 2020
- **Relevance**: CRITICAL
- **Tags**: comprehensive review, QES, island formula, Page curve, replica wormholes, information paradox
- **Source**: PDF-sourced (full content available)

**Summary**: THE comprehensive review of the modern information paradox resolution. Covers BH thermodynamics, Hawking radiation, the paradox, fine-grained vs coarse-grained entropy, the QES formula, the Page curve from semiclassical gravity, the island formula, entanglement wedge, and replica wormholes. Results apply to ANY semiclassical gravity (no AdS/CFT required).

**Key Results**:
- QES formula: fine-grained entropy from semiclassical gravity
- Page curve reproduced without UV-complete theory
- Island formula: interior islands encode information in radiation
- Replica wormholes derive the island formula
- Entanglement wedge of radiation includes deep interior after Page time
- Results universal (no AdS/CFT required)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| QES formula | S = min_X{ext_X[Area(X)/(4G) + S_semi-cl(Sigma_X)]} | Eq. (6.2) |
| Island formula | S_Rad = min_X{ext_X[Area(X)/(4G) + S_semi-cl(Rad union Island)]} | Eq. (8.2) |
| Generalized entropy | S_gen = Area/(4 hbar G) + S_outside | Eq. (2.4) |
| Entropy from Z | S = (1 - beta d/d beta) log Z | Eq. (2.19) |

**Dependencies**: Reviews 05, 06, 13, 14, 21, 24. **Covers originals**: 05, 06, 11, 12, 13, 14, 21, 24.
**Proxy**: N/A (this IS the comprehensive review).

---

### Paper 45: Current Status of the Dynamical Casimir Effect
- **File**: `45_Dodonov_2010_Dynamical_Casimir_Effect.md`
- **arXiv**: 1004.3301
- **Year**: 2010
- **Relevance**: MEDIUM
- **Tags**: dynamical Casimir effect, parametric amplification, squeezed vacuum, experimental proposals, SQUID
- **Source**: PDF-sourced (full content available)

**Summary**: Review of the dynamical Casimir effect. Single-mode: N ~ (v/c)^2 (second-order relativistic). Parametric resonance: N = sinh^2(omega kappa t). Multi-mode effective Hamiltonian. SQUID approach identified as most promising (confirmed by Wilson et al. 2011). DCE, Unruh, and Hawking radiation unified.

**Key Results**:
- DCE is second-order relativistic: N ~ (v/c)^2
- Parametric resonance: exponential growth when 2Q kappa > 1
- SQUID approach subsequently confirmed experimentally (2011)
- DCE/Unruh/Hawking unified through same physics

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Parametric oscillator | epsilon-double-dot + omega^2(t) epsilon = 0 | Eq. (2) |
| Parametric resonance | <N> = sinh^2(omega_0 kappa t) | Eq. (4) |
| Effective Hamiltonian | H = (1/2) Sum [p^2 + omega^2 q^2] + Sum (L-dot/L) Sum p m q | Eq. (5) |
| DCE velocity bound | N_max ~ (v/c)^2 | Sec. 2 |

**Dependencies**: Extends 29. **Covers original**: 29.
**Proxy**: N/A (this IS the review).

---

## Cross-Paper Equation Concordance

### Hawking Temperature
**T = hbar kappa/(2 pi)** -- Papers: 03 (as analogy), 04 (announced), 05 (derived), 07 (cosmological form T=H/2pi), 37 (reproduced), 38 (Unruh form T=a/2pi), 39 (reproduced), 44 (reviewed)

### Bekenstein-Hawking Entropy
**S = A/(4 l_P^2) = A/(4 G hbar)** -- Papers: 11 (proposed, coefficient unset), 03 (thermodynamic correspondence), 05 (coefficient fixed), 07 (cosmological: S=pi/GH^2), 22 (generalized to Wald entropy), 40 (in GSL), 44 (throughout)

### Bogoliubov Transformation
**phi^out = alpha phi^in + beta phi-bar^in with |alpha|^2 - |beta|^2 = 1 (bosonic) or |alpha|^2 + |beta|^2 = 1 (fermionic)** -- Papers: 05 (BH radiation), 12 (Unruh), 15 (cosmological, bosonic), 16 (fermionic), 19 (review), 25 (historical), 26 (BEC experiment), 27 (modern catalog), 33 (KK Schwinger), 37 (step-by-step), 38 (comprehensive), 41 (foundations)

### Particle Number
**N_k = |beta_k|^2** -- Papers: 05, 12, 15, 16, 19, 25, 27, 33, 37, 38, 41

### Generalized Entropy / GSL
**S_gen = Area/(4G) + S_outside; delta S_gen >= 0** -- Papers: 11 (proposed), 40 (ten proofs), 44 (reviewed), 24 (QES extremization)

### Island Formula / QES
**S(R) = min{ext_I[Area(dI)/(4G) + S_bulk(R union I)]}** -- Papers: 14 (introduced), 21 (derived from replica wormholes), 23 (cosmological), 28 (KK), 30 (dS), 31 (dS with backreaction), 44 (comprehensive review)

### Raychaudhuri Equation
**d theta/d lambda = -theta^2/2 - sigma^2 - R_ab k^a k^b** -- Papers: 01 (drives singularity theorem), 17 (drives area variation to derive Einstein eq), 40 (drives area theorem/GSL)

### First Law of Black Hole Mechanics
**delta M = (kappa/8 pi) delta A + Omega_H delta J + Phi_H delta Q** -- Papers: 03 (original), 22 (generalized via Noether charge), 37 (reproduced), 40 (in GSL context), 44 (reviewed)

### Page Curve
**S_rad(t) = min(S_rad^thermal(t), S_BH(t))** -- Papers: 13 (defined), 14 (derived from RT), 21 (from replica wormholes), 39 (reviewed), 44 (comprehensive)

### Smarr Formula
**M = kappa A/(4 pi) + 2 Omega_H J + Phi_H Q** -- Papers: 03 (original), 37 (reproduced)

### Clausius Relation to Einstein Equations
**delta Q = T dS on local Rindler horizons yields R_ab - (1/2) R g_ab + Lambda g_ab = 8 pi G T_ab** -- Papers: 17 (original), 32 (extended), 44 (noted)

### Entropy = Spectral Action
**S(phi_beta) = Tr(h(beta D)) with h(x) = x/(1+e^x) + log(1+e^{-x})** -- Paper: 20 (unique)

### Schwarzian Derivative Energy Flux
**<T_uu> = -(1/24 pi){p(u), u}** -- Papers: 29 (original), 45 (DCE context)

### KK Mass Formula
**M_n^2(t) = (n + q zeta(t))^2/(2 pi R)^2** -- Paper: 33 (KK Schwinger)

### Scrambling Time
**t_scr ~ beta log S_BH** -- Papers: 14, 28, 36, 39, 44

## Notation Conventions

| Symbol | Meaning | Used in |
|:---|:---|:---|
| kappa | Surface gravity of black hole | 03-07, 22, 35, 37, 40, 44 |
| T_H | Hawking temperature: hbar kappa/(2 pi) | 04, 05, 07, 37, 38, 39, 44 |
| T_U | Unruh temperature: hbar a/(2 pi) | 12, 38 |
| T_GH | Gibbons-Hawking temperature: H/(2 pi) | 07 |
| alpha, beta | Bogoliubov coefficients | 05, 12, 15, 16, 19, 26, 27, 33, 37, 38, 41 |
| Gamma_omega | Greybody factor (absorption probability) | 05, 37 |
| S_gen | Generalized entropy: A/(4G) + S_out | 11, 14, 21, 24, 40, 44 |
| S_BH | Bekenstein-Hawking entropy: A/(4 l_P^2) | 11, 13, 14, 22, 39, 44 |
| I_E | Euclidean action | 07, 09, 10, 22, 35, 44 |
| $ | Superscattering operator | 06 |
| xi | Non-minimal coupling to curvature | 15, 19, 27, 43 |
| xi_c | Conformal coupling: 1/6 in 4D | 15, 16, 19, 27 |
| X_QES | Quantum extremal surface | 14, 21, 24, 44 |
| I | Island (in entropy calculation) | 14, 21, 23, 28, 30, 31, 44 |
| theta | Expansion scalar (null congruence) | 01, 17, 40 |
| sigma_ab | Shear tensor (null congruence) | 01, 17, 40 |
| eta | Entropy-area proportionality constant | 11, 17 |
| h(x) | Entropy function: x/(1+e^x) + log(1+e^{-x}) | 20 |
| l_P | Planck length: sqrt(hbar G/c^3) | 11, 44 |

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 20 | Spectral action = entropy (S = Tr(h(beta D))) | Yes | Sessions 37-38, spectral action computations |
| 17 | delta Q = T dS gives Einstein equations | Partial | Framework spectral action as free energy |
| 05 | Trans-Planckian universality of Bogoliubov mechanism | Yes | H-5 gate PASS (Session 25) |
| 05 | |beta|^2 thermal relation | Used | Framework Bogoliubov coefficients in transit |
| 15, 16 | Parker particle creation formalism | Yes | Transit mechanism (Session 38): 59.8 pairs, P_exc=1.000 |
| 11 | GSL (generalized second law) | Yes | GSL-40 PASS (structural), GSL-QTHEORY-46 PASS |
| 07 | Gibbons-Hawking T = H/(2 pi) | Tested | T-ACOUSTIC-40: T_a/T_Gibbs = 0.993 |
| 03 | First law structure | Tested | FIRSTLAW-43 PASS (1.26e-7 precision) |
| 33 | KK Schwinger mode equation | Used | Schwinger-instanton duality S38 (S_Schwinger = 0.070) |
| 13 | Page curve | Tested | PAGE-40: FAIL (S_ent max = 0.422, 18.5% of Page). Framework has no horizon. |
| 18 | AMPS postulates | Evaded | Framework has no horizon: all three simultaneously satisfied |
| 34 | KK cosmology coupled dynamics | Tested | FRIED-39: FAIL (shortfall ~114,000x). Classical version insufficient |
| 43 | Inflationary n_s prediction | Tested | NS-TILT-42: n_s = 0.746 (52 sigma FAIL). Framework is not slow-roll |
