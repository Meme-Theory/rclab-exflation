# Berry Paper Index

**Researcher**: Sir Michael Victor Berry, FRS (and contemporary authors in Berry's domain)
**Papers**: 22 (1980-2025)
**Primary domain**: Geometric phase, quantum geometry, spectral statistics, topological classification
**Project relevance**: The phonon-exflation M4 x SU(3) framework has vanishing Berry curvature (Im(QGT)=0) but large quantum metric (Re(QGT)=982.5) on the Jensen-deformed fiber. This corpus provides the complete mathematical language for the "metrically rich, topologically trivial" regime: QGT decomposition (12, 14, 15), spectral statistics (08, 10), catastrophe structure (09), BCS Berry phase (18), topological classification (19, 20), and the sole surviving route to nontrivial geometry via Wilczek-Zee holonomy (02) at the P-30w gate.

---

## Dependency Graph

```
GEOMETRIC PHASE FOUNDATIONS
  Paper 01 (Review: AB->PB) -----> Paper 02 (QI / non-Abelian)
       |          |                      |
       |          v                      v
       |     Paper 03 (Diabolical)  [P-30w gate: Wilczek-Zee]
       |          |
       v          v
  Paper 04 (Hannay/KvN)        Paper 05 (Open systems)
                                     |
                                     v
                                Paper 06 (Superadiabatic LZ)

SPECTRAL STATISTICS & SEMICLASSICAL
  Paper 08 (RMT/Chaos) ---------> Paper 10 (N-body Berry-Tabor)
       |         |                      |
       |         v                      v
       |    Paper 11 (Gutzwiller)  [Poisson -> GGE integrability]
       v
  Paper 09 (Catastrophe optics)
       |
       v
  [Fold A_2 at tau_fold = 0.190158]

QUANTUM GEOMETRIC TENSOR
  Paper 12 (QGT pedagogical) ----> Paper 14 (Orbital susceptibility)
       |                                |
       v                                v
  Paper 13 (Beam shift)           Paper 15 (Metric era, 2025)
                                        |
                                        v
                                  [ERRATUM: g=982.5, Omega=0]

CONDENSED MATTER BERRY PHASE
  Paper 16 (Xiao-Chang-Niu) ------> Paper 17 (Geometry of QPTs)
       |          |                       |
       v          v                       v
  Paper 21 (Polarization)          Paper 18 (BCS Berry phase)
                                        |
                                        v
                                  [BCS mechanism chain]

TOPOLOGICAL CLASSIFICATION
  Paper 19 (Topological SC) ------> Paper 20 (Topological TI)
       |
       v
  Paper 22 (Equivariant spectral flow)

CROSS-GROUP CONNECTIONS
  01 --> 16  (Berry curvature formalism -> Bloch band applications)
  12 --> 14  (QGT theory -> observable: orbital susceptibility with Omega=0)
  12 --> 17  (QGT theory -> QPT diagnostics: fidelity susceptibility)
  08 --> 10  (RMT review -> many-body Berry-Tabor extension)
  03 --> 09  (Diabolical points -> catastrophe classification)
  14 --> 15  (metric without curvature -> 2025 experimental verification)
  18 --> 19  (BCS Berry phase -> topological SC classification)
  16 --> 20  (Berry in bands -> Z2 topological insulators)
  06 --> 05  (LZ transitions -> open-system geometric magnetism)
```

**Logical chains for project:**
- ERRATUM chain: 12 (QGT) -> 14 (metric w/o curvature) -> 15 (experiments) -> 16 (review)
- P-30w chain: 01 (abelian) -> 02 (non-abelian / Wilczek-Zee) -> 03 (diabolical points)
- Transit chain: 01 (adiabatic) -> 06 (superadiabatic / LZ) -> 05 (geometric magnetism)
- Integrability chain: 08 (RMT) -> 10 (Berry-Tabor N-body) -> 11 (trace formula)
- BCS chain: 18 (BCS Berry) -> 19 (topological SC) -> 20 (topological TI)
- Catastrophe chain: 09 (Thom classification) -> 03 (diabolical points) -> 06 (LZ at crossings)

---

## Topic Map

### A. Geometric Phase Foundations
Papers: 01, 02, 03, 04, 05, 06
Core theory from Berry 1984 through non-Abelian (Wilczek-Zee), non-adiabatic (Aharonov-Anandan), open-system, and classical (Hannay angle) generalizations. Paper 01 is the master review. Paper 02 covers non-Abelian holonomic computation (highest priority for P-30w). Paper 06 discovers superadiabatic LZ transitions where eigenvector geometry, not eigenvalues, controls transition probability.

### B. Spectral Statistics and Semiclassical Methods
Papers: 07, 08, 09, 10, 11
Random matrix theory (08), catastrophe optics (09), Berry-Tabor trace formula extended to many-body Bethe-integrable systems (10), Gutzwiller trace formula with Maslov index (11), and optical vortices (07). BGS conjecture (chaos -> GOE/GUE) and Berry-Tabor theorem (integrability -> Poisson) form the diagnostic backbone for the framework's spectral analysis.

### C. Quantum Geometric Tensor
Papers: 12, 14, 15
The QGT Q = g - (i/2)F decomposes into quantum metric (Re) and Berry curvature (Im). Paper 12 provides the pedagogical foundation with the Feynman-Hellman representation. Paper 14 proves that orbital susceptibility depends on quantum metric even when Berry curvature vanishes identically -- the theoretical explanation for the framework's ERRATUM regime. Paper 15 reviews 2025 ARPES measurement of full QGT in real solids (black phosphorus: F=0, g large).

### D. Berry Phase in Condensed Matter
Papers: 13, 16, 17, 18, 21
Berry curvature in Bloch bands (16 is the canonical RMP review), anomalous velocity, Hall effects, orbital magnetism. Paper 17 uses QGT singularities to detect quantum phase transitions without order parameters. Paper 18 derives the Berry phase for BCS superconductors across the BCS-BEC crossover. Paper 21 explains electric polarization as Berry phase. Paper 13 shows optical beam shifts as geometric phase.

### E. Topological Classification and Extensions
Papers: 19, 20, 22
The 10-fold AZ classification of topological phases (19 for superconductors, 20 for insulators). Z2 invariants, bulk-boundary correspondence, Majorana fermions. Paper 22 provides equivariant spectral flow theory for Dirac operators under group actions -- applicable to the framework's SU(3)-equivariant eigenvalue flow.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| P-30w gate (non-Abelian Berry phase, U(2)-breaking) | 01, **02**, 03 | CRITICAL |
| ERRATUM regime (large g, zero Omega) | **12**, **14**, 15, 16 | CRITICAL |
| Poisson statistics / integrability (B2-INTEG, GGE) | **08**, **10**, 11 | CRITICAL |
| BCS Berry phase (mechanism chain, BDI class) | **18**, 19, 20 | CRITICAL |
| QPT geometry (BCS transition, fidelity susceptibility) | **17**, 12, 14 | CRITICAL |
| Berry curvature in Bloch bands / anomalous velocity | **16**, 01 | CRITICAL |
| Transit physics (superadiabatic, LZ, non-adiabatic) | 01, **06**, 05 | HIGH |
| Topological classification (BDI, WIND-36, Majorana) | **19**, **20** | HIGH |
| Fold catastrophe / avoided crossings | **09**, 03, 06 | HIGH |
| Trace formula (Gutzwiller, Maslov, semiclassical density) | **11**, 10, 08 | MEDIUM |
| Electric polarization (Berry phase as observable) | **21**, 16 | MEDIUM |
| Spectral flow (Dirac operator, Jensen deformation) | **22** | MEDIUM |

---

## Paper Entries

### Paper 01: Geometric Phase from Aharonov-Bohm to Pancharatnam-Berry and Beyond
- **File**: `01_2019_Geometric_Phase_AB_to_PB.md`
- **arXiv**: 1912.12596
- **Year**: 2019
- **Authors**: Cohen, Larocque, Bouchard, Nejadsattari, Gefen, Karimi
- **Relevance**: CRITICAL
- **Tags**: Berry phase, Aharonov-Bohm, Pancharatnam, fiber bundle, holonomy, Chern number, Zak phase, TKNN, anomalous velocity, anyons, Wilczek-Zee, geometric dephasing

**Summary**: Comprehensive review tracing geometric phase from the Aharonov-Bohm effect through Berry's 1984 discovery and all major generalizations. Covers fiber bundle formulation (connection, curvature, holonomy, Chern number), optics (Pancharatnam phase, q-plates, spin-orbit coupling), condensed matter (Zak phase, TKNN Hall conductance, electric polarization, anyons), and quantum information (holonomic computation). Open-system geometric dephasing from complex geometric phase.

**Key Results**:
- AB phase phi_AB = e*Phi/hbar as special case of geometric phase (topological)
- Berry phase gamma[C] = i oint <n|grad_R|n> . dR is holonomy in line bundle over parameter space
- Chern number = integer from integral of Berry curvature over closed 2D surface
- TKNN: sigma_xy = (e^2/h) sum_n int (dk/2pi) Omega_z^n (quantized by Chern numbers)
- Polarization-Zak relation: Delta P = (e/2pi) sum_n gamma_n
- Open systems: geometric dephasing from imaginary part of complex geometric phase
- Exchange statistics in 2D: anyonic phases with arbitrary theta_ij
- Wilczek-Zee non-Abelian phases enable fault-tolerant holonomic QC

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 1.1 | AB phase phi_AB = e*Phi/hbar | Eq. (1) |
| eq 1.2 | Berry phase gamma = i oint <n|grad_R|n> . dR | Eq. (2) |
| eq 1.7 | TKNN Hall conductance sigma_xy | Eq. (7) |
| eq 1.11 | Polarization-Zak relation Delta P = (e/2pi) sum gamma_n | Eq. (11) |
| eq 1.SEM | Semiclassical EOM with Berry curvature | Sec. 4 |

**Dependencies**: Foundation for all other papers. Direct upstream of 02, 03, 16.

---

### Paper 02: Geometric Phases in Quantum Information
- **File**: `02_2015_Sjoqvist_Geometric_Phases_QI.md`
- **arXiv**: 1503.04847
- **Year**: 2015
- **Authors**: Sjoqvist
- **Relevance**: HIGH
- **Tags**: holonomic QC, Wilczek-Zee, non-Abelian, Wilson loop, pi-pulse, geometric gate, mixed states, Uhlmann phase, entanglement

**Summary**: Reviews geometric phase applications in quantum information. Abelian GP on Bloch sphere = -Omega/2 (half solid angle). Non-Abelian GP: matrix-valued holonomy U[C], with Wilson loop Tr U[C] gauge-invariant. Holonomic QC: adiabatic (tripod dark states) and non-adiabatic (Lambda systems, pi-pulse criterion). Experimental realizations in superconducting transmon (97-99%), NMR, NV centers. Extensions to mixed states (Uhlmann phase) and entanglement-induced topological phases.

**Key Results**:
- Qubit GP: Phi[C] = -Omega/2 (half enclosed solid angle on Bloch sphere)
- Non-Abelian GP: U[C] = matrix-valued holonomy, Wilson loop Tr U[C] gauge-invariant
- Adiabatic holonomic QC via tripod dark states (degenerate manifold)
- Non-adiabatic holonomic QC: pi-pulse criterion, U[C] = n . sigma
- Two sequential gates: U(C')U[C] = n'.n + i sigma.(n' x n) (universal SU(2))
- Experimental: transmon 97-99% one-qubit, NV-center CNOT concurrence 0.85

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 2.10 | Abelian GP (general) | Eq. (10) |
| eq 2.16 | Qubit GP: Phi = -Omega/2 | Eq. (16) |
| eq 2.18 | Non-Abelian GP: U[C] (Wilson loop) | Eq. (18) |
| eq 2.36 | Non-adiabatic geometric gate: U[C] = n . sigma | Eq. (36) |
| eq 2.37 | Universal SU(2): U(C')U[C] = n'.n + i sigma.(n' x n) | Eq. (37) |

**Dependencies**: Builds on Paper 01 (Berry phase foundations). Directly relevant to P-30w gate (Wilczek-Zee holonomy). Wilson loop connects to s48_wilson_loop.py verification.

---

### Paper 03: Berry Phase, Topology, and Diabolicity in Quantum Nano-Magnets
- **File**: `03_2005_Berry_Phase_Diabolicity_Nanomagnets.md`
- **arXiv**: quant-ph/0511186
- **Year**: 2005
- **Authors**: Bruno
- **Relevance**: MEDIUM
- **Tags**: diabolical points, degeneracy, monopole, Chern number, topological charge, Fe8, Wess-Zumino, Berry phase interference

**Summary**: Topological theory of diabolical points (parameter-space degeneracies acting as Berry curvature monopoles) in quantum magnets. Defines diabolicity index with sum rules. Resolves the Fe8 "missing diabolical points" paradox: higher-order anisotropy C(J_+^4 + J_-^4) displaces degeneracies, preserving topological constraints. Berry phase interference interpretation via enlarged Hilbert space and Wess-Zumino action.

**Key Results**:
- Diabolical points = Berry curvature monopoles in parameter space (codimension 3)
- Topological charge (Chern number): Q_i(mu) = (1/2pi) oint B . dS
- Sum rule: sum_i Q_i(mu) = 2*mu
- Total diabolicity: D = 2J(J+1)(2J+1)/3
- Fe8 missing points: displaced by perturbation, not destroyed (topology preserved)
- Conjecture: spin Hamiltonian determined by its diabolical points + indices (+ trace)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 3.1 | Diabolical point locations (z and x axes) | Eqs. (1a-b) |
| eq 3.2 | Sum rule for diabolicity | Eqs. (2a-b) |
| eq 3.B | Berry curvature near degeneracy | Sec. 2 |
| eq 3.WZ | Wess-Zumino action S_WZ = i M_tilde int (1-cos theta) d*phi | Sec. 4 |

**Dependencies**: Builds on Paper 01 (Berry curvature monopole). Connects to Paper 09 (catastrophe classification of degeneracies).

---

### Paper 04: Adiabatic Driving and Geometric Phases in Classical Systems
- **File**: `04_2023_Hannay_Angles_Classical_Systems.md`
- **arXiv**: 2305.14511
- **Year**: 2023
- **Authors**: Bermudez Manjarres
- **Relevance**: MEDIUM
- **Tags**: Hannay angle, Koopman-von Neumann, classical Berry phase, Yang-Mills curvature, Lie-Deprit, adiabatic gauge potential

**Summary**: Derives classical geometric phases via the Koopman-von Neumann (KvN) formalism, placing classical mechanics in a Hilbert space framework. KvN eigenstates acquire geometric phase exp(in*Phi) where Phi = -Delta phi_Hannay. The Wilczek-Zee potential is diagonal (states stay on their tori). The classical adiabatic gauge potential maps to Lie-Deprit perturbation theory. Yang-Mills curvature reproduces Hannay curvature.

**Key Results**:
- KvN geometric phase = negative Hannay angle: Phi = -oint <d_lambda phi>
- Wilczek-Zee potential diagonal for KvN states (classical adiabatic theorem)
- Adiabatic gauge potential A_hat = -i{., W} maps to Lie-Deprit generating function
- Yang-Mills curvature reproduces known Hannay curvature for generalized oscillator
- Unifies quantum Berry and classical Hannay in single Hilbert space framework

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 4.3 | KvN Schrodinger equation: i d_t psi = L_hat psi | Eq. (3) |
| eq 4.25 | Classical geometric phase: Phi = -Delta phi_Hannay | Eq. (25) |
| eq 4.33 | Adiabatic gauge potential: A_hat = -i{., W} | Eq. (33) |
| eq 4.40 | Yang-Mills curvature | Eq. (40) |
| eq 4.48 | Hannay curvature (oscillator) | Eq. (48) |

**Dependencies**: Builds on Paper 01 (Berry phase). Connects to Paper 10 (periodic orbit theory, integrable systems).

---

### Paper 05: Geometric Magnetism in Open Quantum Systems
- **File**: `05_2012_Geometric_Magnetism_Open_QS.md`
- **arXiv**: 1206.0671
- **Year**: 2012
- **Authors**: Campisi, Denisov, Hanggi
- **Relevance**: HIGH
- **Tags**: open systems, geometric magnetism, geometric friction, Berry curvature, fluctuation relations, thermal bath, Caldeira-Leggett, adiabatic linear response

**Summary**: Extends Berry curvature to open quantum systems via quantum work fluctuation relations. A slowly-driven system coupled to a thermal bath experiences geometric magnetism (antisymmetric response, Lorentz-like force B x R_dot) and geometric friction (symmetric response). Key result: for damped charged harmonic oscillator, geometric magnetism B = qB is unaffected by bath. No assumption of chaotic dynamics needed; the bath provides relaxation.

**Key Results**:
- Geometric magnetism and friction extend to open quantum systems with arbitrary coupling
- B(R) = (1/2) int_0^infty dt int_0^beta du <nabla H x nabla H>_eq (Eq. 21)
- Bath-independence: B = qB for charged harmonic oscillator regardless of spectral density
- Geometric magnetism vanishes with time-reversal invariance (Onsager-Casimir)
- Berry phase of open system: gamma = int B . dSigma
- Distinction from Kubo LRT: this is canonical adiabatic linear response

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 5.19 | Force response: <Delta Q> = -K^S . R_dot - B x R_dot | Eq. (19) |
| eq 5.21 | Geometric magnetism (open QS) | Eq. (21) |
| eq 5.40 | Damped oscillator: B = qB | Eq. (40) |
| eq 5.43 | Berry phase (open system): gamma = int B . dSigma | Eq. (43) |

**Dependencies**: Builds on Paper 01 (Berry curvature). Extends to non-equilibrium regime relevant to transit physics.

---

### Paper 06: Partial Landau-Zener Transitions and Applications to Qubit Shuttling
- **File**: `06_2024_Superadiabatic_LZ_Transitions.md`
- **arXiv**: 2408.03173
- **Year**: 2024
- **Authors**: Lima, Burkard
- **Relevance**: HIGH
- **Tags**: Landau-Zener, superadiabatic, eigenvector rotation, Bloch sphere, DDP failure, adiabaticity condition, valley transition, shuttling fidelity

**Summary**: Generalizes the Landau-Zener problem: different Hamiltonian curves in the xz plane (identical eigenvalue landscape) produce fundamentally different transition probabilities. Discovers superadiabatic regime (0 < beta < 2*alpha) where P < P_LZ, with P = 0 unconditionally at beta = alpha. Proves LZ transitions can occur without avoided crossings (purely from eigenvector rotation). DDP formula fails. Application to electron shuttling in Si/SiGe quantum dots achieves fidelity > 99.99%.

**Key Results**:
- Superadiabatic regime: P = 0 at beta = alpha regardless of gap and driving speed
- Modified adiabaticity condition: Delta_0^2 / hbar|alpha - beta| >> 1
- LZ transitions without anticrossing (alpha = 0, beta > 0): pure eigenvector rotation
- DDP formula fails: cannot distinguish different Hamiltonian curves with same eigenvalues
- Symmetry: P(alpha, beta) = P(beta, alpha)
- Angular velocity at crossing: theta_dot(0) = |alpha - beta|/Delta_0 determines adiabaticity
- Shuttling fidelity > 99.99% at v = 0.5 m/s by controlling theta_dot

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 6.LZ | LZ formula: P_LZ = exp(-2pi*Delta_0^2 / hbar*alpha) | Sec. I |
| eq 6.2 | Generalized Hamiltonian | Eq. (2) |
| eq 6.3 | Angle theta(t) in xz plane | Eq. (3) |
| eq 6.mod | Modified adiabaticity: Delta_0^2 / hbar|alpha-beta| >> 1 | Sec. III |
| eq 6.ang | Angular velocity at crossing: theta_dot(0) = |alpha-beta|/Delta_0 | Sec. III |

**Dependencies**: Builds on Paper 01 (adiabatic theory). Connects to Paper 09 (fold catastrophe at avoided crossings). Transit physics: framework's tau_Q/tau_0 = 8.71e-4 (deeply non-adiabatic).

---

### Paper 07: Optical Vortices and Wavefront Dislocations
- **File**: `07_1998_Berry_Optical_Vortices.md`
- **Year**: 1998
- **Authors**: Berry (conference proceedings; foundational: Nye & Berry 1974)
- **Relevance**: LOW
- **Tags**: phase singularity, optical vortex, topological charge, winding number, orbital angular momentum, singular optics

**Summary**: Phase singularities in light fields where amplitude vanishes and phase is undefined. Topological charge m = (1/2pi) oint grad phi . dl is an integer winding number. Optical vortices are generic in random wave fields with density ~1/(pi^2 lambda^2). Each charge-m vortex carries OAM = m*hbar per photon. Birth of singular optics as a subfield.

**Key Results**:
- Optical vortices are generic: density ~1/(pi^2 lambda^2) in random wave fields
- Topological charge conservation under smooth deformations
- OAM quantization: L_z = m*hbar per photon for charge-m vortex
- Phase circulation = 2*pi*m (analog of Aharonov-Bohm)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 7.m | Topological charge: m = (1/2pi) oint grad phi . dl | Definition |
| eq 7.n | Dislocation density: n = 1/(pi^2 lambda^2) | Nye-Berry |
| eq 7.L | OAM per photon: L_z = m*hbar | Paraxial |

**Dependencies**: Connects to Paper 09 (singularity classification). Conceptual analog for spectral singularities.

---

### Paper 08: Quantum Chaotic Systems and Random Matrix Theory
- **File**: `08_2019_Quantum_Chaos_RMT.md`
- **arXiv**: 1905.10596
- **Year**: 2019
- **Authors**: Pandey, Kumar, Puri
- **Relevance**: CRITICAL
- **Tags**: RMT, GOE, GUE, GSE, Wigner surmise, Poisson, BGS conjecture, Berry-Tabor, spectral rigidity, level repulsion, quantum chaos, Porter-Thomas, transition ensembles, FRCG, UCF

**Summary**: Comprehensive RMT review. Dyson's threefold way (GOE/GUE/GSE by time-reversal and spin-rotation invariance). Level repulsion p_0(s) ~ s^beta. Spectral rigidity Sigma^2 ~ (2/beta*pi^2) ln r (RMT) vs Sigma^2 = r (Poisson). BGS conjecture: chaos -> RMT statistics. Berry-Tabor: integrability -> Poisson. Quantum kicked rotor as paradigm. GOE-GUE transition with exact solution (Lambda = alpha^2 v^2 / D^2). Universal conductance fluctuations. Finite-range Coulomb gas models.

**Key Results**:
- Dyson's threefold way: beta = 1 (GOE), 2 (GUE), 4 (GSE)
- Level repulsion: p_0(s) ~ s^beta for small s
- Spectral rigidity: Sigma^2(r) ~ (2/beta*pi^2) ln r vs Sigma^2 = r (Poisson)
- Wigner surmise (GOE): p_0(s) = (pi/2)s exp(-pi*s^2/4)
- BGS conjecture: quantum chaotic -> RMT statistics
- Berry-Tabor: quantum integrable -> Poisson statistics
- GOE-GUE transition: exact cluster function with Lambda
- UCF: var(g) = 1/(8*beta) for quantum dots
- Porter-Thomas distribution for eigenvector components
- FRCG: xi = beta*d + 1 interpolates Poisson and RMT

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 8.4 | Eigenvalue jpd (Coulomb gas) | Eq. (4) |
| eq 8.16 | Number variance (log): Sigma^2 = (2/beta*pi^2) ln r + C_beta | Eq. (16) |
| eq 8.20 | Wigner surmise (GOE): p_0(s) = (pi/2)s exp(-pi*s^2/4) | Eq. (20) |
| eq 8.21 | Wigner surmise (GUE) | Eq. (21) |
| eq 8.55 | GOE-GUE transition cluster function | Eq. (55) |
| eq 8.56 | Transition parameter Lambda = alpha^2 v^2 / D^2 | Eq. (56) |
| eq 8.67 | UCF: var(g) = 1/(8*beta) | Eq. (67) |

**Dependencies**: Foundation for Paper 10 (many-body BT). BGS/BT conjectures used in all spectral diagnostics.

---

### Paper 09: Catastrophe Optics and Optical Caustics
- **File**: `09_1980_Berry_Catastrophe_Optics.md`
- **Year**: 1980
- **Authors**: Berry, Upstill
- **Relevance**: HIGH
- **Tags**: catastrophe theory, Thom classification, fold A_2, cusp A_3, swallowtail A_4, umbilic, Airy function, Pearcey function, caustic, rainbow, glory, topological transition

**Summary**: Classification of optical caustics using Thom's catastrophe theory. Fold (A_2), cusp (A_3), swallowtail (A_4), hyperbolic umbilic (D_4^+) produce universal diffraction patterns. Fold intensity diverges as |x|^{-1/2} (geometric); wave-corrected form |Ai(k^{2/3} x)|^2. Cusp diffraction via Pearcey function. Applied to rainbow (fold) and glory (cusp). Topological transitions under parameter variation follow catastrophe bifurcation rules. Only these types appear generically in 3D.

**Key Results**:
- All optical caustics are Thom elementary catastrophes (for up to 4 control parameters)
- Universal diffraction: Airy (fold), Pearcey (cusp), swallowtail and umbilic integrals
- Fold: I ~ |x|^{-1/2} (geometric), |Ai(k^{2/3} x)|^2 (wave), fringe spacing ~ k^{-1/3}
- Caustic topological transitions follow bifurcation rules of catastrophe theory
- Caustic classification is structure-independent (universal, like RMT)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 9.A2 | Fold generating function: x^3 + lambda*x | Classification |
| eq 9.A3 | Cusp generating function: x^4 + lambda*x^2 + mu*x | Classification |
| eq 9.Ai | Fold diffraction: I ~ |Ai(k^{2/3} x)|^2 | Diffraction |
| eq 9.Pe | Pearcey function: Pe(x,y) = int exp(i(t^4+xt^2+yt)) dt | Cusp diffraction |
| eq 9.J | Caustic condition: det(dr/d*xi) = 0 | Geometric optics |

**Dependencies**: Connects to Paper 03 (diabolical points as catastrophes). Directly relevant to framework fold at tau_fold = 0.190158 (A_2, Thom-stable).

---

### Paper 10: Periodic Orbit Theory of Bethe-Integrable Quantum Systems: An N-Particle Berry-Tabor Trace Formula
- **File**: `10_2024_Berry_Tabor_Trace_Formula.md`
- **arXiv**: 2401.17891
- **Year**: 2024
- **Authors**: Urbina, Kelly, Richter
- **Relevance**: HIGH
- **Tags**: Berry-Tabor, trace formula, Bethe ansatz, Lieb-Liniger, many-body, periodic orbits, EBK, Poisson summation, resurgence, Robin boundary

**Summary**: Extends the Berry-Tabor trace formula to Bethe-ansatz-integrable many-body systems (Lieb-Liniger model). Combinatorial identity converts ordered Bethe quantum number sums to unordered sums amenable to Poisson summation. Stationary phase yields the periodic orbit condition. N-particle trace formula has semiclassical amplitudes and actions involving scattering phases and Bethe Jacobians. Resurgence demonstrated for N = 2, 3, 4. N=2 maps to 2D billiard with Robin boundary conditions.

**Key Results**:
- N-particle Berry-Tabor trace formula for Lieb-Liniger (Eqs. 25-28)
- Combinatorial identity (Eq. 12) for ordered-to-unordered sum conversion
- Smooth DOS via Bethe-equation Jacobian (equivalent to thermodynamic Bethe ansatz)
- Semiclassical resurgence: oscillatory terms cancel smooth Weyl background
- N=2 correspondence: Lieb-Liniger <-> 2D square billiard with Robin BC
- Excellent agreement with exact quantum results (N = 2, 3, 4 at g = 10, 100)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 10.8 | Bethe equations for Lieb-Liniger | Eq. (8) |
| eq 10.12 | Partition coefficients C_a | Eq. (12) |
| eq 10.20 | Smooth DOS via Jacobian | Eq. (20) |
| eq 10.25 | Oscillatory density (N-particle BT) | Eq. (25) |
| eq 10.27 | Semiclassical actions R_M | Eq. (27) |
| eq 10.28 | Scattering phases Phi_M | Eq. (28) |

**Dependencies**: Extends Paper 08 (Berry-Tabor conjecture) to many-body. Uses Paper 11 (trace formula methods). Directly relevant: framework's BCS Fock space is integrable (Ordered Veil).

---

### Paper 11: Gutzwiller's Semiclassical Trace Formula and Maslov-Type Index Theory for Symplectic Paths
- **File**: `11_2016_Gutzwiller_Trace_Formula_Maslov.md`
- **arXiv**: 1608.08294
- **Year**: 2016
- **Authors**: Sun
- **Relevance**: MEDIUM
- **Tags**: Gutzwiller trace formula, Maslov index, Conley-Zehnder, symplectic path, Lagrangian Grassmannian, Selberg, WKB, Van Vleck, periodic orbits

**Summary**: Mathematical review of the Gutzwiller trace formula. Derives via WKB ansatz, Hamilton-Jacobi equation, Van Vleck propagator, stationary phase. Clarifies Maslov phase = Conley-Zehnder index (Meinrenken). Five-axiom characterization of Maslov-type index (Long): homotopy invariance, symplectic additivity, clockwise continuity, counterclockwise jumping, normality. Bott iteration formula. Selberg trace formula for constant negative curvature as exact special case.

**Key Results**:
- Gutzwiller trace formula: rho_osc = sum_gamma T_gamma A_gamma exp(i S_gamma/hbar - i pi i_gamma/2)
- Maslov phase = Conley-Zehnder index (Meinrenken identification)
- Five-axiom characterization of Maslov-type index (Long)
- Bott iteration: i_z(gamma, m) = sum_{omega^m=z} i_omega(gamma)
- Morse-Maslov: m^-(z) = d + i_1(x)
- Selberg: exact trace formula for constant negative curvature surfaces
- Basic normal form decomposition reduces to 2x2 and 4x4 symplectic matrices

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 11.GTF | Gutzwiller trace formula | Sec. 1 |
| eq 11.VV | Van Vleck propagator | Sec. 5.1 |
| eq 11.Bott | Bott iteration formula | Thm. 22 |
| eq 11.Sel | Selberg trace formula | Thm. 32 |
| eq 11.MZ | Maslov = Conley-Zehnder index | Sec. 5.4 |

**Dependencies**: Foundation for Paper 10 (trace formula extension). Connects to Paper 08 (BGS via periodic orbits).

---

### Paper 12: Quantum Geometric Tensor (Fubini-Study Metric) in Simple Quantum Systems: A Pedagogical Introduction
- **File**: `12_2010_Gu_QGT_Pedagogical.md`
- **arXiv**: 1012.1337
- **Year**: 2010 (revised 2013)
- **Authors**: Cheng
- **Relevance**: HIGH
- **Tags**: QGT, quantum metric, Fubini-Study, Berry curvature, projected Hilbert space, Feynman-Hellman, Anandan-Aharonov, spin-1/2 monopole

**Summary**: Pedagogical foundation for the quantum geometric tensor Q = g - (i/2)F. The gauge-invariant form Q = <d psi|(1-P)|d psi> decomposes into quantum metric g (symmetric, real) and Berry curvature F (antisymmetric, imaginary). Feynman-Hellman representation: Q = sum |<0|dH|n><n|dH|0>|/(E_0-E_n)^2. For spin-1/2 in B: metric = round S^2, curvature = monopole charge 1/2. Anandan-Aharonov theorem: d*theta/dt = 2|Delta E|/hbar relates quantum velocity to energy uncertainty.

**Key Results**:
- QGT: Q = g - (i/2)F (real part = metric, imaginary part = curvature)
- Gauge-invariant form: Q = <d psi|(1 - |psi><psi|)|d psi>
- Feynman-Hellman: Q = sum_n <0|dH|n><n|dH|0>/(E_0-E_n)^2
- QGT singular at degeneracies (1/gap^2 denominator)
- Spin-1/2: g = round S^2 metric, F = monopole of charge 1/2
- Anandan-Aharonov: d*theta/dt = 2|Delta E|/hbar
- Energy uncertainty: |Delta E| = hbar * sqrt(g_mn lambda_dot^m lambda_dot^n)
- Non-Abelian QGT for degenerate ground states

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 12.5 | QGT definition: Q = <d psi|(1-P)|d psi> | Eq. (5) |
| eq 12.11 | Feynman-Hellman QGT | Eq. (11) |
| eq 12.13 | QGT decomposition: Q = g - (i/2)F | Eq. (13) |
| eq 12.14 | Non-Abelian QGT | Eq. (14) |
| eq 12.20 | Anandan-Aharonov: d*theta/dt = 2|Delta E|/hbar | Eq. (20) |
| eq 12.21 | Energy uncertainty from metric | Eq. (21) |

**Dependencies**: Foundation for Papers 14, 15, 17 (all build on QGT). Central to ERRATUM interpretation.

---

### Paper 13: The Optical Beam Shift and Geometric Phase in Reflection
- **File**: `13_1990_Berry_Optical_Beam_Shift.md`
- **Year**: 1990
- **Authors**: Berry, Balazs
- **Relevance**: LOW
- **Tags**: Goos-Hanchen, Imbert-Fedorov, beam shift, reflection phase, anomalous velocity, spin-orbit coupling, topological robustness

**Summary**: Optical beam shifts upon reflection (Goos-Hanchen, Imbert-Fedorov) are manifestations of geometric phase. The lateral shift Delta x = (1/2k_perp) d*delta/dk_parallel arises from reflection phase gradient (Berry connection). Unifies disparate beam-shift phenomena. The shift is topologically robust and shows spin-orbit coupling for polarized beams.

**Key Results**:
- GH shift = geometric phase from reflection phase variation with k_parallel
- Unified framework for Goos-Hanchen, Imbert-Fedorov, Artmann shifts
- Topological robustness: depends on global phase, not microscopic details
- Anomalous velocity analog: v_perp ~ d*phi_geom/dk_parallel

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 13.GH | GH shift: Delta x = (1/2k_perp) d*delta/dk_parallel | Main result |
| eq 13.IF | IF shift for circularly polarized light | Sec. on IF |
| eq 13.geom | Geometric phase: phi_geom = oint A . dr | Sec. on GP |

**Dependencies**: Builds on Paper 01 (GP in optics). Anomalous velocity analog connects to Paper 16.

---

### Paper 14: Geometric Orbital Susceptibility: Quantum Metric Without Berry Curvature
- **File**: `14_2016_Orbital_Susceptibility_Metric.md`
- **arXiv**: 1605.01258
- **Year**: 2016
- **Authors**: Piechon, Raoux, Fuchs, Montambaux
- **Relevance**: CRITICAL
- **Tags**: quantum metric, orbital susceptibility, Berry curvature, interband, flat band, paramagnetism, two-band model, curvature-metric identity

**Summary**: Proves that orbital magnetic susceptibility depends on quantum metric even when Berry curvature vanishes identically. Four-term decomposition: chi_orb = chi_LP + chi_Omega + chi_g + chi_tilde_g. The metric contribution chi_g is the "most fundamental" interband term, surviving under both inversion and particle-hole symmetry. Key identity: Omega^2 = 4 det g (metric determines curvature magnitude). Square-to-honeycomb interpolation: at square lattice (Omega = 0), chi_g gives paramagnetic plateau. Flat band (Mielke checkerboard): diverging paramagnetism from metric alone.

**Key Results**:
- chi_orb = chi_LP + chi_Omega + chi_g + chi_tilde_g (four-term decomposition)
- chi_g (metric-only) is most fundamental interband contribution
- Omega^2 = 4(g_ii g_jj - g_ij^2) = 4 det g (curvature-metric identity)
- Square lattice: Omega = 0 identically, yet chi_g produces paramagnetic gap plateau
- Flat band: diverging paramagnetism from quantum metric alone
- Each term independently satisfies sum rule: int d*mu chi = 0
- Dirac model identity: 3H = M^2 = Z_g
- chi_g requires full BZ integration (not just Dirac point vicinity)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 14.4 | QGT definition T = <d u|(1-P)|d u> | Eq. (4) |
| eq 14.8 | Two-band: Omega = (1/2)(dn x dn).n, g = (1/4) dn.dn | Eq. (8) |
| eq 14.9 | Curvature-metric identity: Omega^2 = 4 det g | Eq. (9) |
| eq 14.14 | Total susceptibility decomposition | Eq. (14) |
| eq 14.20 | Metric contribution chi_g with Z_g = (1/2) d_j(epsilon^2 d_i g^ij) | Eq. (20) |
| eq 14.31 | Field-induced curvature from metric: Omega_g = -d_i d_j g^ij / 2 | Eq. (31) |

**Dependencies**: Builds on Paper 12 (QGT decomposition). Directly explains framework ERRATUM: physical response from g=982.5 even when Omega=0.

---

### Paper 15: From Berry Curvature to Quantum Metric: A New Era of Quantum Geometry Metrology
- **File**: `15_2025_Quantum_Metric_Era_Review.md`
- **arXiv**: 2512.24553
- **Year**: 2025
- **Authors**: Yang
- **Relevance**: HIGH
- **Tags**: quantum metric, ARPES, quasi-QGT, pseudospin tomography, black phosphorus, CoSn, flat band, experimental QGT

**Summary**: Reviews 2025 breakthroughs in direct ARPES measurement of full QGT. Kang et al.: quasi-QGT in kagome metal CoSn via band Drude weight + OAM. Kim et al.: full quantum metric in black phosphorus via pseudospin tomography. Key: in black phosphorus, Berry curvature vanishes identically (space-time inversion) while quantum metric is large and anisotropic. Lists physical effects requiring quantum metric: flat-band Landau levels, geometric superconductivity, nonlinear Hall, excitonic Lamb shift.

**Key Results**:
- QGT directly measurable by ARPES (two independent methods, 2025)
- Black phosphorus: F_ij = 0 identically, g_ij large and anisotropic
- Quantum metric anisotropy exceeds energy dispersion anisotropy
- Quantum metric controls superfluid stiffness in flat bands
- Quasi-QGT applicable to multiband crystalline systems

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 15.Q | QGT: Q_ij = <d_i u|(1-P)|d_j u> | Fig. 1 |
| eq 15.F | Berry curvature: F_ij = -2 Im Q_ij | Fig. 1 |
| eq 15.g | Quantum metric: g_ij = Re Q_ij | Fig. 1 |
| eq 15.ps | Pseudospin: g_ij = (1/4) d_i d_hat . d_j d_hat | Fig. 1 |

**Dependencies**: Builds on Papers 12, 14 (QGT theory). Experimental validation of Omega=0, g>0 regime (exactly the framework's ERRATUM situation).

---

### Paper 16: Berry Phase Effects on Electronic Properties
- **File**: `16_2010_Xiao_Berry_Phase_Effects.md`
- **arXiv**: 0907.2021
- **Year**: 2010
- **Authors**: Xiao, Chang, Niu
- **Relevance**: CRITICAL
- **Tags**: anomalous velocity, Berry curvature, Bloch bands, Hall effect, TKNN, Zak phase, polarization, orbital magnetism, wave packet, semiclassical EOM, Chern number, modified DOS

**Summary**: The canonical RMP review of Berry phase in condensed matter. Berry curvature as "magnetic field in parameter space." Anomalous velocity dot r = d*epsilon/(hbar dk) + (1/hbar) dk_dot x Omega. TKNN = Chern number x e^2/h. Polarization = Berry phase across BZ. Orbital magnetization with Berry curvature contribution. Modified DOS: D ~ (1 + (e/hbar)B.Omega). Conservation law: sum_n Omega^n = 0. Non-Abelian extension for degenerate bands. Re-quantization method for effective quantum theory.

**Key Results**:
- Berry curvature: local, gauge-invariant "magnetic field in parameter space"
- Anomalous velocity: dot r = d*epsilon/(hbar dk) + (1/hbar) dk_dot x Omega
- TKNN: sigma_xy = (e^2/h) sum_n c_n (quantized by Chern numbers)
- Polarization = Berry phase (Zak phase) across BZ
- Conservation: sum_n Omega^n = 0 (total curvature summed over bands vanishes)
- Degeneracy points = monopole sources/drains of Berry curvature
- Modified DOS: D ~ (1 + (e/hbar)B.Omega)
- Orbital moment: m_n = -(e/2hbar) Im <grad u| x (H-epsilon) |grad u>
- Quantized adiabatic transport = first Chern number (integer)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 16.1.6 | Berry connection A = i<n|d/dR|n> | Eq. (1.6) |
| eq 16.1.13 | Berry curvature (summation formula) | Eq. (1.13) |
| eq 16.1.14 | Conservation: sum_n Omega^n = 0 | Eq. (1.14) |
| eq 16.1.20 | Two-level monopole: Omega = h/(2h^3) | Eq. (1.20) |
| eq 16.2.5 | Anomalous velocity | Eq. (2.5) |
| eq 16.2.7 | Quantized transport: c_n = Chern number | Eq. (2.7) |
| eq 16.V | Semiclassical EOM (full set) | Sec. V.A |

**Dependencies**: Builds on Paper 01 (foundations). Upstream of Papers 17, 21. Canonical reference for Bloch-band Berry phase.

---

### Paper 17: Geometry of Quantum Phase Transitions
- **File**: `17_2020_Carollo_Geometry_QPTs.md`
- **arXiv**: 1911.10196
- **Year**: 2020
- **Authors**: Carollo, Valenti, Spagnolo
- **Relevance**: CRITICAL
- **Tags**: quantum phase transition, fidelity susceptibility, Berry curvature singularity, QGT scaling, Uhlmann phase, XY model, mixed states, NESS-QPT, critical exponents

**Summary**: Berry curvature singularities and QGT divergence detect quantum phase transitions without order parameters or symmetry-breaking knowledge. Fidelity susceptibility chi_F ~ L^{2/nu} diverges at critical points. "Singular curvature and singular metric are complementary manifestations of exceptional state behavior across QPTs." In 1D XY model, nontrivial GP requires circulating a critical region (topological origin). Uhlmann phase extends to mixed-state and non-equilibrium steady-state QPTs.

**Key Results**:
- QGT super-extensive at QPTs: Re(Q) ~ L^{2/nu}
- Berry curvature singularities = order-parameter-free QPT detectors
- Complementarity: singular curvature + singular metric at same degeneracy
- Gap scaling: Delta ~ J|lambda - lambda_c|^{nu*z}
- Correlation length divergence: xi ~ |lambda - lambda_c|^{-nu}
- XY model: nontrivial GP if and only if loop encircles critical region
- Uhlmann phase for mixed-state and NESS-QPTs
- Fidelity susceptibility: chi_F ~ L^{2/nu}

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 17.2 | Gap scaling: Delta ~ J|lambda-lambda_c|^{nu*z} | Eq. (2) |
| eq 17.4 | Correlation length: xi ~ |lambda-lambda_c|^{-nu} | Eq. (4) |
| eq 17.5 | Critical time: tau_c ~ Delta^{-1} ~ xi^z | Eq. (5) |
| eq 17.14 | Berry curvature F^B | Eq. (14) |
| eq 17.FS | Fubini-Study metric ds^2 | Sec. 6.1 |
| eq 17.chi | Fidelity susceptibility: chi_F = lim (-2 ln F)/delta^2 | Sec. 6.3 |

**Dependencies**: Builds on Papers 12 (QGT), 16 (Berry curvature). Connects to Paper 18 (BCS transition).

---

### Paper 18: Dynamic Properties of Superconductors: Anderson-Bogoliubov Mode and Berry Phase in BCS and BEC Regimes
- **File**: `18_2019_Marciani_BCS_Berry_Phase.md`
- **arXiv**: 1902.04588
- **Year**: 2019
- **Authors**: Mozyrsky, Chubukov
- **Relevance**: CRITICAL
- **Tags**: BCS, BEC crossover, Berry phase, vortex dynamics, Magnus force, Wess-Zumino, Anderson-Bogoliubov, Goldstone mode, superfluid stiffness, impurity robustness

**Summary**: Microscopic derivation of Berry phase in BCS superconductors across the BCS-BEC crossover. Long-wavelength action for phase fluctuations is universal: Anderson-Bogoliubov mode velocity v_F/sqrt(2), unchanged through crossover. Bulk Berry phase prefactor A = n/2 (full fermion density). For moving vortex: A_vort = (n-n_0)/2 where n/2 is hydrodynamic (Magnus) and -n_0/2 is core reaction. BCS: near-cancellation (A_vort = N_0 E_0). BEC: pure Magnus (A_vort = n/2). Core contribution impurity-independent.

**Key Results**:
- Anderson-Bogoliubov mode: v = v_F/sqrt(2), universal across BCS-BEC
- Condensation energy E_cond = -S N_0 Delta_0^2/2, independent of E_0/E_F
- Bulk Berry phase prefactor: A = n/2
- Vortex Berry phase: A_vort = (n-n_0)/2
- BCS limit: A_vort = N_0 E_0 (near-cancellation of Magnus + core)
- BEC limit: A_vort = n/2 (pure Magnus, no normal core fermions)
- Core contribution A_vort,2 = -n_0/2 is impurity-independent
- Gap equation: mu = E_F - E_0, Delta_0 = 2*sqrt(E_F E_0)
- Galilean invariance: v_vort = v_s

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 18.14 | Effective action S[Delta] | Eq. (14) |
| eq 18.81 | Berry term S_1 = i int (n-n_0)/2 dot phi | Eq. (81) |
| eq 18.89 | Combined Berry: S_1 + S_norm | Eq. (89) |
| eq 18.104 | Full phase action S_reg | Eq. (104) |
| eq 18.106 | Berry prefactor: A = n/2 | Eq. (106) |
| eq 18.157 | Vortex core identity (delta function localization) | Eq. (157) |
| eq 18.167 | Vortex Berry total: A_vort = (n-n_0)/2 | Eq. (167) |

**Dependencies**: Builds on Paper 01 (Berry phase). Connects to Papers 19 (topological SC), 16 (Berry in bands). Bridge to Volovik (superfluid universe).

---

### Paper 19: Topological Superconductors: A Review
- **File**: `19_2017_Sato_Ando_Topological_SC.md`
- **arXiv**: 1608.03395
- **Year**: 2017
- **Authors**: Sato, Ando
- **Relevance**: HIGH
- **Tags**: topological superconductor, AZ classification, 10-fold way, BDI, Majorana, BdG, particle-hole symmetry, Z2, winding number, He-3 B-phase, spin-orbit

**Summary**: Comprehensive review of topological superconductors. Altland-Zirnbauer 10-fold classification: BDI class (T^2=+1, C^2=+1, chiral) has Z winding number in 1D. BdG Hamiltonian with particle-hole symmetry C*H(k)*C^{-1} = -H(-k). Majorana fermions at E=0 obey non-Abelian statistics. Routes: odd-parity pairing, SC topological insulators, spin-orbit + s-wave. He-3 B-phase as prototype topological superfluid.

**Key Results**:
- AZ 10-fold way: complete classification of topological phases by symmetry
- BDI class: T^2=+1, C^2=+1, chiral symmetry, Z winding number in 1D
- PH symmetry: C*H(k)*C^{-1} = -H(-k) (intrinsic to BdG framework)
- Majorana zero modes at vortex cores/edges with non-Abelian statistics
- Z2 requires T^2 = -1 (not available in BDI, which has T^2 = +1)
- Spin-orbit coupling enables topological SC even with s-wave pairing
- He-3 B-phase: prototype 3D topological superfluid

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 19.2 | Berry connection A^(n)(k) | Eq. (2) |
| eq 19.5 | Berry curvature F^(n)_ij | Eq. (5) |
| eq 19.9 | Chern number Ch^(n) | Eq. (9) |
| eq 19.72 | BdG Hamiltonian | Eq. (72) |
| eq 19.74 | Particle-hole symmetry | Eq. (74) |
| eq 19.34 | Z2 index (parity eigenvalues at TRIM) | Eq. (34) |

**Dependencies**: Builds on Papers 01, 16 (Berry curvature, Chern). Connects to Paper 20 (TI classification). Directly classifies framework's BDI class (WIND-36=0).

---

### Paper 20: Colloquium: Topological Insulators
- **File**: `20_2010_Hasan_Kane_Topological_Insulators.md`
- **arXiv**: 1002.3895
- **Year**: 2010
- **Authors**: Hasan, Kane
- **Relevance**: HIGH
- **Tags**: topological insulator, Z2 invariant, quantum spin Hall, bulk-boundary correspondence, surface Dirac cone, Kramers, Fu-Kane formula, Bi2Se3, ARPES

**Summary**: Foundational review of topological insulators. Z2 invariants (nu_0; nu_1 nu_2 nu_3) classify TRS-invariant band insulators. Fu-Kane parity criterion: (-1)^{nu_0} = prod delta_i. Strong TI: odd number of surface Dirac cones, protected by TRS. Berry phase pi around surface Fermi surface -> anti-localization. Materials: Bi2Se3, Bi2Te3, HgTe. Kramers theorem: T^2 = -1 implies two-fold degeneracy at TRIM.

**Key Results**:
- Z2 invariants classify TRS-invariant band insulators
- Fu-Kane: (-1)^{nu_0} = prod_{TRIM} delta_i (parity eigenvalues)
- Strong TI: odd number of surface Dirac cones, robust against TRS-preserving perturbations
- Berry phase pi around Dirac point -> anti-localization (absence of backscattering)
- Kramers theorem: T^2 = -1 implies two-fold degeneracy at TRIM
- Bulk-boundary correspondence: nontrivial Z2 guarantees gapless surface states

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 20.FK | Fu-Kane parity formula: (-1)^{nu_0} = prod xi(TRIM) | Main result |
| eq 20.surf | Surface Dirac cone: H_surf = hbar v_F (sigma_x k_y - sigma_y k_x) | Surface states |
| eq 20.pi | Berry phase pi around Dirac point | Transport |
| eq 20.KM | Kane-Mele Hamiltonian (graphene + SOC) | QSH section |

**Dependencies**: Builds on Paper 16 (Berry in bands), Paper 19 (AZ classification). Z2 vs BDI comparison for framework (Z2 requires T^2=-1, BDI has T^2=+1).

---

### Paper 21: A Beginner's Guide to the Modern Theory of Polarization
- **File**: `21_2012_Spaldin_Polarization_Guide.md`
- **arXiv**: 1202.1831
- **Year**: 2012
- **Authors**: Spaldin
- **Relevance**: MEDIUM
- **Tags**: electric polarization, Berry phase, Zak phase, Wannier center, adiabatic current, quantum of polarization, King-Smith-Vanderbilt

**Summary**: Pedagogical introduction to polarization as Berry phase. Classical definition (dipole/volume) fails for extended systems (polarization paradox). Resolution: P = (e/(2pi)^3) sum int <u|i grad_k|u> dk (Zak phase). Only changes Delta P are physical (defined mod eR/V). Wannier center interpretation: bar x_n = (a/2pi) gamma_n. Adiabatic current = integrated Berry curvature (Thouless pump).

**Key Results**:
- Bulk polarization = Berry phase (Zak phase), not expectation value
- Only polarization differences physical (mod quantum eR/V)
- Zak phase quantized to 0 or pi with inversion symmetry
- Wannier center: bar x_n = (a/2pi) gamma_n (real-space interpretation)
- Adiabatic current j = -sum int (dq/2pi) Omega_qt

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 21.P | Berry phase polarization P = (e/(2pi)^3) sum int <u|i grad_k|u> dk | KSV formula |
| eq 21.Zak | Zak phase gamma_n = int <u|i d_k|u> dk | 1D form |
| eq 21.QP | Quantum of polarization: Delta P = eR/V | Resta |
| eq 21.WC | Wannier center: bar x_n = (a/2pi) gamma_n | Real-space |

**Dependencies**: Builds on Papers 01, 16 (Berry phase in bands). Concrete application showing Berry phase has macroscopic observable consequences even when individual curvature terms are small.

---

### Paper 22: Equivariant Spectral Flow and Collective Spectral Flow
- **File**: `22_2024_Equivariant_Spectral_Flow.md`
- **arXiv**: 2403.00575
- **Year**: 2024
- **Authors**: [incomplete extraction]
- **Relevance**: MEDIUM
- **Tags**: spectral flow, equivariant, Dirac operator, group action, irreducible representation, index theory, APS theorem, Fredholm

**Summary**: Theory of equivariant spectral flow for families of self-adjoint Fredholm operators under group actions. Spectral flow (net eigenvalue crossings through zero) decomposes into irreducible representation sectors of the symmetry group G. Collective spectral flow provides refined topological invariants. Index-spectral flow correspondence: sf(D_0, D_1) = index(d_t + D_t) on cylinder (APS theorem).

**Key Results**:
- Equivariant spectral flow decomposes by irreps: sf_G = sum sf|V_rho [rho]
- Collective spectral flow gives refined invariants beyond ordinary sf
- sf = index of associated operator on cylinder (APS theorem)
- Applies to Dirac operator families under G-equivariant deformations

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| eq 22.sf | Spectral flow: sf = #(upward crossings) - #(downward crossings) | Sec. 1 |
| eq 22.eq | Equivariant decomposition: sf_G = sum sf|V_rho [rho] | Main result |
| eq 22.APS | Index-spectral flow: sf = index(d_t + D_t) | APS theorem |

**Dependencies**: Connects to Paper 11 (Maslov/index theory). Directly applicable to framework's SU(3)-equivariant Dirac operator under Jensen deformation.

---

## Cross-Paper Equation Concordance

### Berry Connection A_n = i<n|grad|n>
Appears in Papers 01 (Eq. 2), 02 (Eq. 10), 16 (Eq. 1.6), 17 (Eq. 11), 19 (Eq. 2), 21 (Zak formula). Convention variations:
- Papers 01, 16, 17, 19: A = i<n|d/dR|n> (connection on general parameter space)
- Paper 21: A = i<u|d/dk|u> (connection on Brillouin zone)
- Paper 02: Aharonov-Anandan form (dynamical phase subtracted first)
All agree on the gauge transformation: A -> A + d*chi under |n> -> e^{i chi} |n>.

### Berry Curvature Omega = dA
Appears in Papers 01 (Eq. 7), 03 (Sec. 2), 05 (Eq. 21), 12 (Eq. 12), 14 (Eq. 8), 16 (Eq. 1.13), 17 (Eq. 14), 19 (Eq. 5). Two computational forms used:
- Differential: Omega_mn = d_m A_n - d_n A_m (Papers 16, 19)
- Summation: Omega = -Im sum_{m!=n} <n|dH|m><m|dH|n>/(E_n-E_m)^2 (Papers 01, 12, 16)
The summation form is computationally preferred (avoids phase ambiguity in eigenstates). In the framework, the summation form was used to prove Omega = 0 identically (ERRATUM, S25).

### Quantum Geometric Tensor Q_ij
Appears in Papers 12 (Eq. 5), 14 (Eq. 4), 15 (Fig. 1), 17 (Sec. 6.1). Decomposition:
- Q = g - (i/2)F where g = Re(Q) = quantum metric, F = -2 Im(Q) = Berry curvature
- Feynman-Hellman: Q = sum_{n!=0} <0|d_mu H|n><n|d_nu H|0>/(E_0-E_n)^2 (Papers 12, 14)
- Two-band identity: Omega^2 = 4 det g (Paper 14, Eq. 9) -- metric determines curvature magnitude
- Framework result: Re(Q) = 982.5, Im(Q) = 0 identically. "Sensitivity without protection."

### Chern Number / Hall Conductance
The first Chern number C_n = (1/2pi) int Omega d^2k appears in Papers 01 (Eq. 7), 16 (Eq. 2.7), 19 (Eq. 9), 20 (Fu-Kane formula). TKNN formula: sigma_xy = (e^2/h) sum_n C_n. Guaranteed integer by bundle topology over closed 2D manifold (BZ torus). Framework verification: C = 0 on Jensen line (S25, from Omega = 0).

### Level Spacing Distributions
Wigner surmise P(s) = (pi/2)s exp(-pi s^2/4) for GOE appears in Paper 08 (Eq. 20). Poisson P(s) = exp(-s) for integrable systems (Papers 08, 10). BGS conjecture + Berry-Tabor theorem form the diagnostic pair:
- Chaotic classical limit -> GOE/GUE statistics (BGS)
- Integrable classical limit -> Poisson statistics (BT)
Framework: Poisson confirmed (B2-INTEG-40 PASS, <r>=0.401). Structural theorem: Poisson from Schur orthogonality (not action-angle, not Anderson).

### Trace Formulas
Density of states rho(E) = rho_smooth + rho_osc appears in Papers 10 (Eqs. 1-2), 11 (Sec. 1). Three versions:
- Gutzwiller (chaotic): sum over isolated periodic orbits with action S, period T, monodromy M, Maslov index i (Paper 11)
- Berry-Tabor (integrable): sum over tori with winding numbers M (Paper 10, single-particle, 1976-77)
- N-particle Berry-Tabor (Bethe): sum over many-body winding numbers (Paper 10, Eqs. 25-28, 2024)

### BCS Berry Phase
Paper 18: S_1 = i int (n-n_0)/2 * dot phi, giving A = n/2 (bulk), A_vort = (n-n_0)/2 (vortex). Connects to Paper 19's particle-hole symmetry C*H*C^{-1} = -H(-k) constraining BdG topology.

### Catastrophe Classification
Thom's hierarchy from Paper 09: A_2 (fold), A_3 (cusp), A_4 (swallowtail), D_4 (umbilic). Universal diffraction patterns: Airy (fold), Pearcey (cusp). Framework: fold A_2 at tau_fold = 0.190158, kappa = 1.1757 (Thom-stable, Mather-stable).

## Notation Conventions

| Symbol | Meaning | Primary papers |
|:---|:---|:---|
| gamma, Phi, phi^B | Berry phase (geometric phase) | 01, 02, 16, 17 |
| A, A_n, A^B | Berry connection | 01, 02, 16, 17, 19 |
| Omega, F, F^B | Berry curvature (2-form) | 01, 12, 14, 16, 17, 19 |
| g, g_ij | Quantum metric (real part of QGT) | 12, 14, 15 |
| Q, T | Quantum geometric tensor (full) | 12, 14, 15 |
| C_n, Ch | Chern number (first) | 01, 16, 19, 20 |
| sigma_xy | Hall conductance | 01, 16, 19, 20 |
| P(s), p_0(s) | Nearest-neighbor spacing distribution | 08 |
| Sigma^2(r) | Number variance | 08 |
| Delta_3(r) | Spectral rigidity (Dyson-Mehta) | 08 |
| beta | Dyson index (1=GOE, 2=GUE, 4=GSE) | 08 |
| rho(E) | Density of states (smooth + oscillatory) | 10, 11 |
| i_gamma | Maslov / Conley-Zehnder index | 11 |
| A_vort | Berry phase prefactor for vortex dynamics | 18 |
| nu, nu_0 | BDI winding number / Z2 invariant | 19, 20 |
| sf | Spectral flow | 22 |
| U[C] | Non-Abelian geometric phase (holonomy matrix) | 02 |
| chi_orb | Orbital magnetic susceptibility | 14 |
| chi_F | Fidelity susceptibility | 17 |
| Lambda | GOE-GUE transition parameter | 08 |
| D | Total diabolicity | 03 |

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 01, 16 | Berry curvature Omega = 0 on Jensen SU(3) | Yes (max\|Omega\| < 4e-14) | `computations/_shared/s24a_berry.py`, `s25_berry_results.py` |
| 01, 16, 19 | Chern number = 0 on Jensen line | Yes | `computations/_shared/s25_berry_results.py` |
| 12 | QGT: Re(Q) = 982.5 (quantum metric) | Yes | `computations/_shared/s24a_berry.py` (ERRATUM: B=982 is metric, not curvature) |
| 12 | QGT: Im(Q) = 0 (Berry curvature) | Yes | `computations/_shared/s24a_berry.py` |
| 12 | Fubini-Study distance d_FS = 0 for all tau > 0 | Yes | `computations/_shared/s25_berry_results.py` |
| 14 | Observable response with Omega=0, g>0 | Confirmed (structural) | Framework matches: chi_g channel active, chi_Omega = 0 |
| 08 | Poisson spacing statistics (Berry-Tabor) | Yes (<r>=0.401) | `computations/_shared/s22a_level_stats.py`, `s61_level_spacing.py` |
| 08 | B2 Fock space Poisson (many-body BT) | Yes | `computations/_shared/s40_b2_integrability.py` (B2-INTEG-40 PASS) |
| 09 | Fold catastrophe A_2 at tau_fold = 0.190158 | Yes (kappa=1.1757) | `computations/_shared/s34a_dphys_fold.py`, `s54_massey_fold.py` |
| 02 | Wilson loop (non-Abelian holonomy) | Trivial (KS p=0.52) | `computations/_shared/s48_wilson_loop.py` |
| 01 | Zak phase on Jensen line | ARTIFACT (retracted S48) | `computations/_shared/s48_dissolution_berry.py` |
| 01 | Closed-loop Berry phase | Zero (max 1.02e-14) | `computations/_shared/s48_berry_complete.py` (CLOSED-LOOP-48 PASS) |
| 09, 01 | Berry phase around fold = 0 | Yes (gamma/pi = 0.0000) | `computations/_shared/s55_berry_fold.py` (BERRY-FOLD-55) |
| 16 | GL band Zak phase = 0 all 6 bands | Yes | `computations/_shared/s53_berry_anticrossing.py` |
| 19 | BDI winding number nu = 0 | Yes | `computations/_shared/s36_bdi_winding.py` (WIND-36) |
| 19 | E_B2/Delta = 33.4x from transition | Yes | `computations/_shared/s36_bdi_winding.py` |
| 18 | BCS Berry phase diagnostic | Partial (gamma/pi not quantized) | `computations/_shared/s28c_berry_bcs.py` |
| 22 | Equivariant spectral flow decomposition | Not computed | Awaits P-30w off-Jensen computation |
| 10 | N-particle trace formula for framework | Not computed | Candidate for future resurgence test |
| 06 | Superadiabatic regime identification | Not computed | LZ retraction (S28d) makes this MOOT on Jensen line |

---

## Source Notes

| Source | Papers |
|:---|:---|
| **arXiv PDF (direct)** | 01, 02, 03, 04, 05, 06, 08, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22 |
| **Retained prior transcription** | 07, 09, 13 (pre-arXiv, LOW priority) |
