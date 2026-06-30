# Loop Quantum Gravity Paper Index

**Researcher**: Loop Quantum Gravity (LQG) canonical literature
**Papers**: 18 (1994-2022)
**Primary domain**: Background-independent canonical and covariant quantum gravity; quantum Riemannian geometry; spin networks; spin foams; loop quantum cosmology; black hole entropy from isolated horizons; group field theory; Lorentz covariance; QG phenomenology
**Project relevance**: LQG is a structurally parallel background-independent quantum gravity program to phonon-exflation. Both produce gauge-invariant discrete spectra (area/volume eigenvalues vs $D_K$ eigenvalues) on a finite kinematical Hilbert space from a single dimensionless parameter (Immirzi $\gamma$ vs Jensen $\tau_{\text{fold}}$), both are background-independent, and both treat continuum geometry as emergent. Neither is derived from the other; the comparison is structural at the substrate-IS / sum-over-configurations / single-parameter level. The strongest non-analog is the singularity-resolution mechanism: LQC's quasi-equilibrium polymer-Friedmann bounce vs phonon-exflation's impulsive supersonic transit at $\tau_{\text{fold}} = 0.190$ (Mach 13.75).

---

## Dependency Graph

```
KINEMATIC FOUNDATIONS (1994-2001)
  01 (Rovelli-Smolin discrete area/volume, gr-qc/9411005)
       |
       +--> 02 (ABCK BH entropy LETTER, gr-qc/9710007)
       |
       +--> 03 (ABK isolated horizon BH entropy LONG, gr-qc/0005126)
       |
       +--> 04 (Bojowald LQC singularity absence, gr-qc/0102069)
       |
       +--> 05 (Ashtekar-Lewandowski 2004 status report, gr-qc/0404018) [SYNTHESIS]

DYNAMICS REGULARIZATION (2005-2006)
  05 ---> 06 (Thiemann QSD VIII Master Constraint, gr-qc/0510011)
  04 ---> 08 (Ashtekar-Pawlowski-Singh APS quantum bounce, gr-qc/0602086)
  05 ---> 07 (Oriti GFT sketch, gr-qc/0512048) [GFT genesis]

COVARIANT VERTEX CONSTRUCTION (2007)
  01,02,03 + (BF + Plebanski simplicity)
       --> 09 (EPR vertex LETTER, 0705.2388, May 2007)
       --> 10 (EPR vertex long-form, 0708.1236, Aug 2007)
       --> 11 (EPRL with finite Immirzi gamma, 0711.0146, Nov 2007)
  09,10,11 + 07 --> 12 (Oriti GFT-Plebanski, 0902.3903)

PHENOMENOLOGY + COVARIANCE (2009-2014)
  09,10,11 + 05 --> 14 (Rovelli-Speziale Lorentz covariance, 1012.1739)
  any LQG ground --> 13 (Amelino-Camelia-Smolin QG dispersion / Fermi LAT, 0906.3731)
  07,12 --> 15 (Oriti GFT microscopic dynamics, 1110.5606)
  12,15 --> 16 (Oriti GFT-and-LQG synthesis, 1408.7112)

MODERN SYNTHESIS (2021-2022)
  ALL kinematic + dynamics + LQC + BH entropy --> 17 (Ashtekar-Bianchi short review, 2104.04394)
  ALL conceptual structure (relational space/time, partial observables, boundary amplitude)
       --> 18 (Rovelli-Vidotto philosophical foundations, 2211.06718)

CROSS-THEME LINKS
  01 (discrete area/volume) <-> 17 sec. 2.2 (LOST/F uniqueness + area gap)
  02,03 (Immirzi pinned by S = A/4) <-> 17 sec. 4.2 (CMB cross-check on Delta)
  04,08 (LQC bounce) <-> 17 sec. 4 (bounce review + observational anchors)
  06 (Master Constraint) <-> 17 sec. 5 (Hamiltonian dynamics status)
  07,12,15,16 (GFT line) -- methodological extension of 09-11 dynamics
  09,10,11 (EPRL vertex) <-> 14 (Lorentz covariance) <-> 17 sec. 3 (spinfoam review)
  13 (QG-dispersion phenomenology) -- isolated phenomenological branch, weakly anchored to 01-12 structural core
  18 (philosophical foundations) -- synthesizes the conceptual content of all earlier papers
```

## Topic Map

### Quantum Riemannian Geometry (kinematics)
Papers: 01, 05, 17, 18
Discrete spectra of area and volume operators from Ashtekar-Lewandowski measure on cylindrical functions; the LOST/Fleischhack uniqueness theorem singling out a unique diffeomorphism-covariant representation of the holonomy-flux algebra; spin networks as the kinematical Hilbert-space basis; the area gap $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ as the fundamental microscopic LQG parameter.

### Black Hole Entropy and the Immirzi Parameter
Papers: 02, 03, 05, 17
Isolated-horizon boundary conditions; U(1) Chern-Simons theory on a punctured 2-sphere; counting of spin-network punctures matching Bekenstein-Hawking $S = A/(4\ell_P^2)$; the Immirzi parameter $\gamma$ pinned to $\gamma_0 = \ln 2/(\pi\sqrt{3})$ via this matching (with refinements in SU(2) formulation; the value is convention-dependent at the gauge-group level).

### Hamiltonian Constraint Regularization
Papers: 06, 17
Thiemann's QSD program; the Master Constraint Programme replacing the infinite family $\{H(N)\}$ by a single self-adjoint $\widehat{M}$ via the algebra-functional integral $M = \int H^2/\sqrt{\det q}$; closability theorem (QSD VIII) establishing existence of the physical Hilbert space; ongoing geometric-insight revival via [Alesci-Assanioussi-Lewandowski].

### Loop Quantum Cosmology (LQC)
Papers: 04, 08, 17
Bohr-compactification kinematical Hilbert space for the symmetry-reduced homogeneous-isotropic sector; difference-equation Hamiltonian constraint (Bojowald 2001) propagating through the classical singularity; APS quantum bounce (2006) at $\rho_{\text{sup}} = 18\pi G\hbar^2/\Delta^3 \approx 0.41\,\rho_{\text{Pl}}$ with $\phi$ as emergent internal time; CMB power-suppression alleviation at $\ell \lesssim 30$.

### Spin Foam Vertex Construction (EPRL/FK)
Papers: 09, 10, 11, 14
The EPR vertex (May 2007) replacing Barrett-Crane through weak (not strong) imposition of second-class simplicity constraints; flipped spinfoam vertex long-form (Aug 2007) deriving boundary matching to SO(3) LQG via the linear-map $f$ and the highest-spin Clebsch-Gordan selection $K_{\text{ph}}$; EPRL extension to finite Immirzi $\gamma$ (Nov 2007) in both Euclidean Spin(4) and Lorentzian SL(2,C); Lorentz covariance of LQG kinematics via the Dupuis-Livine map and the boundary space $\mathcal{K}$.

### Group Field Theory (GFT) and Third Quantization
Papers: 07, 12, 15, 16
Combinatorially non-local QFT on $G^{\times d}$ whose Feynman amplitudes are spin foams; Boulatov model (3d, Ponzano-Regge); Ooguri model (4d BF); Oriti's generalized GFT with Lie-algebra simplicity constraints (Plebanski path-integral form, 2009); GFT-as-microscopic-dynamics (60-page review, 2011); GFT-and-LQG synthesis (2014) including condensate cosmology emergent Friedmann equation; non-commutative emergent matter from mean-field perturbations.

### QG Phenomenology / Lorentz Modification
Papers: 13, 17
Three theoretical frameworks (NLSB, LSB-EFT, DSR) producing leading-order modified dispersion $E \simeq p + m^2/(2p) - s_\pm E^{\alpha+1}/(2M_{QG}^\alpha)$; Fermi-LAT GRB bounds from 080916C giving $M_{QG} > 1.3 \times 10^{18}$ GeV ($\sim 0.1 M_P$); LQC pre-inflationary anomaly alleviation as a separate observational channel; the area-gap value cross-checked between BH entropy and CMB.

### Conceptual / Philosophical Foundations
Papers: 18, 17 (intro)
Relational vs Newtonian container space; partial observables and the boundary-amplitude formalism resolving the Dirac-observables construction problem; truncation discipline (lattice-QCD analogy: finite graphs are reliable physics, not approximations); Heisenberg cut as the boundary of a 4d region; the problem of time partitioned into Question 1 (dynamics without a canonical time) and Question 2 (why time flows).

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Discrete area/volume spectra (the central LQG result) | 01, 05 sec. V, 17 sec. 2.2 | CRITICAL |
| Immirzi parameter and BH entropy pinning | 02, 03, 05 sec. VIII, 17 sec. 5 | CRITICAL |
| Hamiltonian constraint / Master Constraint | 06, 05 sec. VI, 17 sec. 5 | HIGH |
| LQC bounce / cosmogenesis singularity-resolution | 04, 08, 05 sec. VII, 17 sec. 4 | CRITICAL |
| EPRL/FK spin foam vertex amplitude | 09, 10, 11, 17 sec. 3 | CRITICAL |
| GFT formalism (second-quantization of spin networks) | 07, 12, 15, 16 | HIGH |
| Lorentz covariance of LQG / boundary state spaces | 14, 11 sec. IV | HIGH |
| QG-dispersion phenomenology (Fermi-LAT, GRB) | 13 | MEDIUM |
| Philosophical / conceptual foundations | 18, 17 sec. 1 | HIGH |
| Modern authoritative review (single document) | 17 | CRITICAL |
| Background independence and uniqueness theorems | 05 sec. III-IV, 17 sec. 2.2 | HIGH |
| Cross-framework comparison with phonon-exflation | 01, 02, 03, 04, 08, 17 | CRITICAL |

---

## Paper Entries

### Paper 01: Discreteness of Area and Volume in Quantum Gravity
- **File**: `01_Rovelli_Smolin_1994_Discreteness_Area_Volume.md`
- **arXiv**: gr-qc/9411005
- **Year**: 1994
- **Relevance**: CRITICAL
- **Tags**: area operator, volume operator, spin networks, loop representation, discrete spectra, Ashtekar variables

**Summary**: Landmark paper establishing that area and volume operators have discrete spectra in non-perturbative canonical quantum gravity. Constructs the volume operator $\hat V$ via a background-decoupled regularization of the three-hands loop observable $T^{abc}$; diagonalizes $\hat V$ on the trivalent spin-network basis explicitly. Completes the area spectrum and shows joint diagonalization with $\hat A$. Establishes spin networks as the kinematical Hilbert-space basis for LQG (subsequently extended to higher valence with intertwiner data).

**Key Results**:
- Trivalent volume spectrum: $V = (l_P^3/4) \sum_i \sqrt{a_ib_ic_i + a_ib_i + a_ic_i + b_ic_i}$
- Full area spectrum: $A = (l_P^2/2) \sum_l \sqrt{p_l^2 + 2p_l} = \sum_l \hbar\sqrt{j_l(j_l+1)}$ with $j_l = p_l/2$
- Joint diagonalization of $\hat V$ and $\hat A$ on spin networks
- Diffeomorphism invariance of $\hat V$: $\hat V$ commutes with $U(\phi)$, descends to knot space
- Physical-vs-kinematical observable matching argument (matter-gauge-fixing)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1/32 | Trivalent volume eigenvalue formula | $V = (l_P^3/4) \sum \sqrt{abc + ab + ac + bc}$ |
| Eq. 2/49-50 | Area eigenvalue formula | $A = \sum_l \hbar\sqrt{j_l(j_l+1)}$ |
| Eq. 5 | Three-hands loop observable $T^{abc}$ | Trace formula on parallel propagator |
| Eq. 10 | Background-decoupled regulator $W_I$ | Cubic-box integral of $T^{abc}$ |
| Eq. 12-13 | Volume from regulated $W_I$ | $\hat V = \lim_L \sum_I \sqrt{W_I / (2^7 \cdot 3!)}$ |
| Eq. 38 | Diffeomorphism invariance of $\hat V$ | $U(\phi)\hat V = \hat V U(\phi)$ |

**Dependencies**: Foundational paper -- no upstream dependencies in this corpus. Downstream: 02, 03, 04, 05 (status report), 17 (modern review), 18 (foundational citation).

---

### Paper 02: Quantum Geometry and Black Hole Entropy
- **File**: `02_Ashtekar_1997_QuantumGeometry_BHEntropy.md`
- **arXiv**: gr-qc/9710007
- **Year**: 1997
- **Relevance**: CRITICAL
- **Tags**: black hole entropy, isolated horizons (precursor), U(1) Chern-Simons, Immirzi parameter, Barbero-Immirzi pinning, puncture counting

**Summary**: Letter introducing the LQG black hole sector and deriving the Bekenstein-Hawking area-law $S = A/(4\ell_P^2)$ from quantized spin-network surface states. Identifies the gravitational boundary symplectic structure on an isolated non-rotating horizon as exactly the U(1) Chern-Simons structure. The Immirzi parameter $\gamma$ is fixed to $\gamma_0 = \ln 2/(\pi\sqrt{3})$ by matching the entropy coefficient; the same $\gamma_0$ universally reproduces Bekenstein-Hawking for Reissner-Nordstrom and dilatonic black holes.

**Key Results**:
- Boundary symplectic structure of GR on isolated horizon = U(1) Chern-Simons symplectic structure at level $k = A_S/(8\pi\gamma G)$
- Polymer geometry: surface states have support on flat-except-at-punctures generalized connections
- Surface-state dimension grows as $\prod_{j_p}(2j_p + 1)$; large-$A_S$ asymptotic counting
- $S_{bh} = (\gamma_0/(4\ell_P^2 \gamma)) A_S$ with $\gamma_0 = \ln 2/(\pi\sqrt{3})$
- Universality: $\gamma_0$ fixed once reproduces $S = A/(4\ell_P^2)$ for charged and dilatonic BHs

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | Self-dual action with horizon Chern-Simons surface term | Bulk + boundary action |
| Eq. 2 | Real-form pull-back boundary condition | $\gamma F_{ab} = -(2\pi\gamma/A_S) \gamma \Sigma_{ab}$ |
| Eq. 4 | Chern-Simons level | $k = A_S/(8\pi\gamma G)$ |
| Eq. 5 | Quantum boundary condition | Coupled $\Psi_V \otimes \Psi_S$ equation |
| Eq. 7 | Area eigenvalue with Immirzi | $A = 8\pi\gamma\ell_P^2 \sum_p \sqrt{j_p(j_p+1)}$ |
| Eq. 8 | Surface-state dimension asymptotic | $\dim \mathcal{H}_S \sim \prod(2j_p+1)$ |
| Eq. 9 | Entropy formula and $\gamma_0$ pinning | $S = (\ln 2/(\pi\sqrt{3} \cdot 4\gamma\ell_P^2)) A_S$ |

**Dependencies**: Upstream: 01 (discrete area spectrum). Downstream: 03 (long-form derivation), 05 (review), 17 (modern review).

---

### Paper 03: Quantum Geometry of Isolated Horizons and Black Hole Entropy
- **File**: `03_Ashtekar_Baez_Krasnov_2000_IsolatedHorizons_BHEntropy.md`
- **arXiv**: gr-qc/0005126
- **Year**: 2000
- **Relevance**: CRITICAL
- **Tags**: isolated horizons, U(1) Chern-Simons, theta functions, BH entropy, partition-function pole counting, deficit angles, Wheeler "It from Bit"

**Summary**: Long-form (~60 pages) derivation completing the canonical-LQG BH entropy program initiated by Krasnov 1996 and ABCK letter (Paper 02). Constructs the full non-perturbative quantization of the sector of GR coupled to matter admitting non-rotating isolated horizons as inner boundaries. The U(1) Chern-Simons phase space at $n$ punctures is shown to be a $2(n-1)$-torus (Theorem 1) with theta-function geometric quantization. The entropy counting via partition-function meromorphy yields the same $\gamma_0 = \ln 2/(\pi\sqrt{3})$ at leading order.

**Key Results**:
- Theorem 1: $\mathcal{X}_\mathcal{P} \cong \mathbb{C}^{n-1}/\Lambda$ is a $2(n-1)$-torus (geometric quantization yields theta-function basis)
- Operator-equation imposition of horizon boundary condition (Eq. 12, exponentiated form)
- Spectral matching theorem: $\exp(-i 2\pi\gamma \hat\Sigma \cdot r/a_0)$ and $\exp(i\hat F)$ spectra coincide at integer Chern-Simons level $k = a_0/(4\pi\gamma\ell_P^2)$
- Entropy upper bound via partition function $Z(\alpha) = \prod_l 1/(1-(2l+1)e^{-\alpha 8\pi\gamma\ell_P^2 \sqrt{l(l+1)}})$ with leading pole at $\alpha_0 = \ln 2/(4\pi\sqrt{3}\gamma\ell_P^2)$
- "It from Bit" entropy: dominant punctures have $j = 1/2$, $a_i = \pm 1$, each contributing $\ln 2$
- Charged-BH universality: same $\gamma_0$ extends to RN, dilatonic, cosmological horizons

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 3 | Barbero-Immirzi-rescaled connection | $^\gamma A = \Gamma - \gamma K$ |
| Eq. 7 | Symplectic structure with U(1) CS surface term | Bulk + horizon boundary form |
| Eq. 12 | Quantum boundary condition (exponentiated) | Operator equation on $\mathcal{H}_V \otimes \mathcal{H}_S$ |
| Eq. 16 | Gauss-Bonnet-style closure | $\sum a_i \equiv 0 \pmod k$ |
| Eq. 20 | Area eigenvalue formula | $\hat A_S \psi = 8\pi\gamma\ell_P^2 \sum_i \sqrt{j_i(j_i+1)} \psi$ |
| Eq. 46 | Lower entropy bound (j = 1/2 ladder) | $S_{bh} \geq (\ln 2/(4\pi\sqrt{3}\gamma\ell_P^2)) a_0$ |
| Eq. 50 | Partition function | $Z(\alpha) = \prod_l 1/(1 - (2l+1)e^{-\alpha 8\pi\gamma\ell_P^2\sqrt{l(l+1)}})$ |
| Eq. 52 | $\gamma_0$ fixed by BH-Hawking | $\gamma_0 = \ln 2/(\pi\sqrt{3})$ |

**Dependencies**: Upstream: 01, 02 (letter). Downstream: 05, 17 (modern review treatments).

---

### Paper 04: Absence of Singularity in Loop Quantum Cosmology
- **File**: `04_Bojowald_2001_AbsenceOfSingularity_LQC.md`
- **arXiv**: gr-qc/0102069
- **Year**: 2001
- **Relevance**: CRITICAL
- **Tags**: loop quantum cosmology, LQC, singularity removal, difference equation, bounded inverse scale factor, Thiemann regularization, discrete-time evolution

**Summary**: Founding paper of Loop Quantum Cosmology (LQC). Demonstrates that the classical cosmological singularity in isotropic minisuperspace is naturally removed by quantum geometry. At the kinematical level, the inverse scale factor is bounded by a Thiemann-regularized operator. At the dynamical level, the Hamiltonian constraint becomes a difference equation (not differential), and the evolution propagates through the classical singularity $n = 0$ because the volume-difference coefficient vanishes and the matter Hamiltonian annihilates $s_0$. The pre-singularity contracting branch joins the post-singularity expanding branch.

**Key Results**:
- $\mathcal{H}_{\text{kin}} = L^2(SU(2), d\mu_H)$ as kinematical Hilbert space; orthonormal volume basis $\chi_j, \zeta_j$ and triad basis $|n\rangle$ with $n \in \mathbb{Z}$ (including negative)
- Discrete volume spectrum: $V_j = (\gamma l_P^2)^{3/2} \sqrt{j(j+1/2)(j+1)/27}$
- Inverse-scale-factor operator $\hat m_{IJ}$ is BOUNDED despite classical $1/a$ divergence (Thiemann commutator trick)
- Discrete-time difference evolution equation propagating through $n = 0$ (Eq. 7)
- Semiclassical limit: $\hat m_{IJ,j} \sim V_j^{-1/3}(\delta_{IJ} + O((\gamma l_P^2/a^2)^2))$ for large $j$ -- classical limit preserved
- Wheeler-DeWitt approximation recovered at large $|n|$; non-perturbative effects essential for singularity removal

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | Volume basis $\chi_j$, $\zeta_j$ | $\chi_j = \sin((j+1/2)c)/\sin(c/2)$ |
| Eq. 2 | Volume spectrum | $V_j = (\gamma l_P^2)^{3/2}\sqrt{j(j+1/2)(j+1)/27}$ |
| Eq. 3 | Triad basis | $|n\rangle = e^{inc/2}/(\sqrt{2}\sin(c/2))$ |
| Eq. 4 | Bounded inverse-scale-factor operator eigenvalues | Explicit closed form |
| Eq. 6 | Euclidean Hamiltonian constraint action | $\hat H^{(E)}|n\rangle = -(3/\gamma\kappa l_P^2)(V_{|n|/2} - V_{|n|/2-1})(|n+4\rangle - 2|n\rangle + |n-4\rangle)$ |
| Eq. 7 | Discrete-time difference evolution | The central singularity-resolution equation |
| Eq. 8 | Explicit Euclidean ground state | $\psi(c) = \sum_j (2j+1)/(V_{j+1/2} - V_{j-1/2}) \chi_j(c)$ |

**Dependencies**: Upstream: 01 (discrete volume spectrum), Thiemann QSD regularization (ref). Downstream: 08 (APS bounce sharpening), 05 (LQC section), 17 (modern review).

---

### Paper 05: Background Independent Quantum Gravity: A Status Report
- **File**: `05_Ashtekar_Lewandowski_2004_BackgroundIndependentQG_StatusReport.md`
- **arXiv**: gr-qc/0404018
- **Year**: 2004
- **Relevance**: CRITICAL
- **Tags**: status report, Holst action, Ashtekar-Lewandowski measure, LOST-Fleischhack uniqueness, cylindrical functions, spin networks, area operator, volume operator, Thiemann constraint, LQC, isolated horizons, spin foams

**Summary**: The canonical 2004 status report (~100 pages, Class. Quantum Grav. 21:R53-R152) codifying the LQG framework. Self-contained pedagogical synthesis of connection variables (Holst action with Barbero-Immirzi parameter), background-independent quantum kinematics (Ashtekar-Lewandowski measure on cylindrical functions, LOST-Fleischhack uniqueness theorem), quantum Riemannian geometry (area/volume operators with discrete spectra, area gap), quantum dynamics (Gauss, diffeomorphism, scalar constraints via Thiemann's regularization), LQC, isolated-horizon BH entropy, and a survey of low-energy / spin-foam directions (treats Barrett-Crane as the then-current vertex, soon superseded by EPRL/FK).

**Key Results**:
- Holst action $S^{(H)}$ produces the Ashtekar-Barbero connection $A^i_a = \Gamma^i_a - \sigma\gamma K^i_a$
- Ashtekar-Lewandowski measure $\mu_o$ on the space $\bar{\mathcal{A}}$ of generalized connections is unique under background independence (LOST-Fleischhack)
- Area operator eigenvalues with area gap $\Delta a_S = 4\pi\gamma\ell_P^2 \cdot \sqrt{3}/2$
- Non-commutativity of $\hat A_S, \hat A_{S'}$ when surfaces intersect (no metric representation)
- Volume operator vanishes at bivalent or trivalent gauge-invariant vertices (Jacobi identity)
- Thiemann's scalar-constraint regularization: regulator parameter $\epsilon$ disappears in quantum limit
- LQC Bohr-compactification structure with bounded curvature; singularity-avoiding difference equation
- BH entropy with $\gamma_0 = \ln 2/(\pi\sqrt{3})$; matched across all isolated horizons
- "It from Bit" emergence from quantum-geometric first principles
- Spin-foam Barrett-Crane model + GFT perturbative finiteness summary

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 2.6 | Holst action | Palatini + Holst topological term, coefficient $1/(2k\gamma)$ |
| Eq. 2.20 | Ashtekar-Barbero connection | $A^i_a = \Gamma^i_a - \sigma\gamma K^i_a$ |
| Eq. 4.43 | Generalized connection | $\bar A(e) \in G$ for every edge |
| Eq. 5.4 | Area operator | $\hat A_{S,\alpha} = 4\pi\gamma\ell_P^2 \sum_v \sqrt{-\Delta_{S,v,\alpha}}$ |
| Eq. 5.14 | General area eigenvalue | With $j^{(u)}, j^{(d)}, j^{(u+d)}$ from angular-momentum addition |
| Eq. 5.15 | Area gap | $\Delta a_S = 4\pi\gamma\ell_P^2 \cdot \sqrt{3}/2$ |
| Eq. 5.21 | Volume operator | $\hat V_{R,\alpha} = \kappa_o \sum_v \sqrt{\hat q_{v,\alpha}}$ |
| Eq. 6.16 | Thiemann's co-triad trick | $e^i_a = (2/(k\gamma))\{A^i_a, V\}$ |
| Eq. 7.19 | Bounded LQC triad operator | $|p|^{-1/2}_{max} = \sqrt{12/(8\pi\gamma)} \ell_P^{-1}$ |
| Eq. 8.10 | LQG BH entropy | $S_\Delta = (\gamma_o/\gamma)(a_o/(4\ell_P^2)) + o(\ell_P^2/a_o)$ |

**Dependencies**: Upstream: 01-04 (foundational results synthesized). Downstream: anchor reference for 06, 07, 08, 09-11 (vertex constructions), 13 (phenomenology), 14 (covariance), 17 (modern review).

---

### Paper 06: Quantum Spin Dynamics VIII. The Master Constraint
- **File**: `06_Thiemann_2005_Master_Constraint.md`
- **arXiv**: gr-qc/0510011
- **Year**: 2005
- **Relevance**: HIGH
- **Tags**: Hamiltonian constraint, Master Constraint Programme, Dirac algebra, structure functions, closability, Friedrichs extension, physical Hilbert space, anomaly-free constraint algebra

**Summary**: Eighth paper in Thiemann's QSD series, closing the structural gap in the Master Constraint Programme (MCP) for LQG. Replaces the infinite family of Hamiltonian constraints $\{H(N)\}$ (which form a Dirac algebra with structure FUNCTIONS, not constants -- obstructing standard group-averaging) with a single Master Constraint $M = \int H^2/\sqrt{\det q}$. Proves that the positive quadratic form $Q_M$ on $H_{\text{diff}}$ is closable and induces a unique self-adjoint $\widehat{M}$ via the Friedrichs extension; zero lies in the point spectrum, so the physical Hilbert space exists by standard spectral analysis. The combinatorial finiteness bound is universal across matter content and signatures.

**Key Results**:
- Master Constraint $M = \int_\sigma d^3 x \, H(x)^2/\sqrt{\det q(x)}$ replaces structure-function $D$ algebra
- New inner product on the algebraic dual $D^*$ (Eq. 2.13) -- first such proposal
- Quadratic form $Q_M$ derived systematically via $V(\Delta) \to \sqrt{V(\Delta)}$ substitution (Eq. 2.6)
- Theorem 3.2: $Q_M$ closable; induces unique positive self-adjoint $\widehat{M}$; zero in point spectrum
- Combinatorial finiteness bound: at most $4^{16} N_2^8 |V(\gamma(s_0([s_2])))|^2$ classes contribute (proof step 1)
- Universality across matter coupling + signature
- Theorem 4.1: $\theta$-classification yields separable $\widehat{M}$-invariant subspaces $H^\theta_{\text{diff}}$; physical Hilbert space is the $\lambda = 0$ slice of a direct-integral decomposition
- Master Equation well-defined under asymptotic flatness without boundary corrections (more regular than the Hamiltonian constraint)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 2.1 | Lorentzian Hamiltonian constraint | $H = aH_E + bK$, Immirzi-parameter coefficients |
| Eq. 2.4 | Classical Master Constraint | $M = \int H^2/\sqrt{\det q}$ |
| Eq. 2.6 | Substitution $V \to \sqrt{V}$ | $C(\Delta) = H(\Delta)/\sqrt{V(\Delta)}$ |
| Eq. 2.13 | New inner product on $D^*$ | $\langle l, l'\rangle_* = \sum c_s \overline{c'_s} \eta_{[s]}/\aleph([s])$ |
| Eq. 2.27 | Final form of $Q_M$ | Finite sum over $[s]$, $v$ |
| Thm 3.2 | $Q_M$ closability + zero in spectrum | Existence of physical Hilbert space |
| Eq. 3.4 | Extended Master Constraint | $M_E$, $M_{EE}$ including diffeo + Gauss |
| Thm 4.1 | Direct-integral decomposition | $H^\theta_{\text{diff}} \cong \int^\oplus d\mu(\lambda) H^\theta_{\text{diff}}(\lambda)$ |

**Dependencies**: Upstream: Thiemann QSD I-VII (refs), Phoenix Project (Thiemann 2003), Dittrich-Thiemann tests. Downstream: 05 (cited in status report), 17 (modern Hamiltonian-dynamics review).

---

### Paper 07: Quantum Gravity as a Group Field Theory: A Sketch
- **File**: `07_Oriti_2005_GroupFieldTheorySketch.md`
- **arXiv**: gr-qc/0512048
- **Year**: 2005
- **Relevance**: MEDIUM
- **Tags**: group field theory, GFT, third quantization, Boulatov model, Ponzano-Regge, fat graphs, simplicial gravity, matrix models extension

**Summary**: Short conceptual sketch positioning GFT as a unifying framework subsuming canonical LQG, spin-foam covariant amplitudes, dynamical triangulations, and Regge calculus. The action for a scalar field on $G^{\times D}$ with combinatorial-non-local interaction has Feynman amplitudes dual to simplicial complexes; expanded in irreps of $G$ they reproduce spin-foam models. The Boulatov 3d Riemannian model produces the Ponzano-Regge spin foam exactly. Frank about the limitations: no rigorous foundation, classical solutions unknown, no diffeomorphism analog, continuum limit unstudied.

**Key Results**:
- 3rd-quantization motivation: scalar field $\phi(^3h)$ on superspace with action $\phi\Delta\phi + \lambda V(\phi)$; perturbative vacuum is "no spacetime"
- Matrix-model precedent: $N \times N$ Hermitian matrix; $Z = \sum_T \lambda^{n_2}/sym(T) \cdot N^{\chi(T)}$
- General GFT action on $G^{\times D}$ with right-translation and permutation symmetries
- Feynman amplitudes = spin foams when field expanded in irreps
- Tree-level GFT amplitudes = canonical-theory inner product (projection onto physical states)
- Boulatov 3d model exactly reproduces Ponzano-Regge model with 6j-symbol vertex weights
- Explicit identification: 3d GFT = simplicial third quantization of gravity

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | Formal quantum-gravity transition | $Z_{QG} = \int Dg\, e^{iS_{GR}}$ |
| Eq. 2 | 3rd-quantization action | $S(\phi) = \int \phi\Delta\phi + \lambda V(\phi)$ |
| Eq. 3-4 | Matrix-model action + expansion | $Z = \sum_T \lambda^{n_2}/sym(T) N^{\chi(T)}$ |
| Eq. 5 | Dynamical triangulations | $Z = \sum_T 1/sym(T) e^{iS_R}$ |
| -- | Boulatov GFT action | Tetrahedral interaction over $(SU(2))^3$ |
| -- | Boulatov amplitude | $Z(\Gamma) = \prod_e \int dg_e \prod_f \delta(\prod g_e)$ |
| -- | Ponzano-Regge form | $Z = \sum_j \prod \Delta_j \prod_v 6j$ |

**Dependencies**: Upstream: matrix models (Witt-Maharana, Gross-Migdal), Boulatov 1992 (foundational GFT), Ooguri 1992 (4d BF), Freidel-Louapre. Downstream: 12, 15, 16 (Oriti GFT line).

---

### Paper 08: Quantum Nature of the Big Bang
- **File**: `08_Ashtekar_2006_QuantumNatureBigBang.md`
- **arXiv**: gr-qc/0602086
- **Year**: 2006
- **Relevance**: CRITICAL
- **Tags**: APS bounce, LQC, big bounce, emergent time, deterministic Planck-regime evolution, Bohr compactification, semiclassical states, numerical quantum cosmology

**Summary**: Landmark APS letter establishing the LQC quantum bounce. Improves Bojowald 2001 by incorporating quantum-geometry corrections in the gravitational Hamiltonian (not just the matter Hamiltonian), constructing a rigorous physical Hilbert space, Dirac observables, and semi-classical states, then numerically evolving the Hamiltonian constraint. The scalar field $\phi$ serves as emergent internal time; the quantum evolution is deterministic across the deep Planck regime; the big bang is replaced by a big bounce at a critical density $\rho_{\text{crit}}$ depending on $p_\phi^*$. Sharply peaked semi-classical states tracking the classical trajectory bounce and connect to the past portion of a classically-headed-to-big-crunch trajectory.

**Key Results**:
- $\mathcal{H}_{\text{kin}}$ on the Bohr compactification of $\mathbb{R}$: inequivalent to Wheeler-DeWitt at the kinematical level
- Hamiltonian-constraint difference equation (Eq. 1) replaces the Wheeler-DeWitt differential equation; the difference is set by $\mu_o$ determined by the area gap
- Emergent time: $\phi$ as globally monotonic clock; $\Theta$ on the RHS of Eq. 1 is $\phi$-independent, self-adjoint, positive-definite
- Superselection sectors $\mathcal{H}_\epsilon$ ($\epsilon \in [0, 2\mu_o]$) parameterize physical states
- Numerical evolution of semi-classical state $\Psi(\mu, \phi)$ peaked at classical trajectory: bounce visible in figures 1, 2
- Bounce mechanism is quantum-geometric (NOT energy-condition violation); curvature bounded above by area-gap discreteness
- Quantum bridge: deterministic LQC evolution connects contracting + expanding classical large-universe branches
- Robustness: extensions to anisotropies, scalar-field potentials begun; inhomogeneity an open frontier

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | LQC self-adjoint Hamiltonian constraint | $\partial^2_\phi \Psi = B(\mu)^{-1}[C^+\Psi(\mu+4\mu_o) + C^o\Psi(\mu) + C^-\Psi(\mu-4\mu_o)] = -\Theta\Psi$ |
| -- | Area-gap pin | $(8\pi\gamma/6)\mu_o\ell_P^2 = \Delta$ |
| Eq. 2 | Positive-frequency square-root | $-i\partial_\phi\Psi = \sqrt{\Theta}\Psi$ |
| Eq. 3 | Physical inner product | $\sum_\mu B(\mu) \overline\Psi_1\Psi_2$ |
| Eq. 4a,4b | Dirac observables | $\hat p_\phi$ and $\hat\mu|_{\phi_o}$ |
| Eq. 5 | Wheeler-DeWitt large-$\mu$ approximant | $(\underline\Theta f)(\mu) = (16\pi G/3)\mu^{3/2}(\sqrt{\mu}f')'$ |
| Eq. 7 | Physical-state expansion | $\Psi(\mu,\phi) = \int dk \tilde\Psi(k) e^{(s)}_k(\mu) e^{i\omega(k)\phi}$ |

**Dependencies**: Upstream: 04 (Bojowald LQC), 05 (canonical methods). Downstream: 17 sec. 4 (modern LQC review), 18 (philosophical foundations cosmology applications).

---

### Paper 09: The Loop-Quantum-Gravity Vertex-Amplitude (EPR Letter)
- **File**: `09_Engle_Pereira_Rovelli_2007_LQG_Vertex_Amplitude.md`
- **arXiv**: 0705.2388
- **Year**: 2007 (May)
- **Relevance**: CRITICAL
- **Tags**: EPR vertex, spin foam, Barrett-Crane critique, second-class constraints, weak imposition, SO(4) -> SU(2) boundary matching, 15j symbol

**Summary**: Letter introducing the EPR vertex amplitude as the replacement for Barrett-Crane (BC) in 4d Euclidean spin foams. Diagnoses three BC problems: (i) over-imposition of second-class simplicity constraints kills physical degrees of freedom (Dirac), (ii) BC boundary state space mismatches SO(3) LQG kinematics, (iii) BC gives wrong tensor structure for the low-energy graviton propagator. The remedy is weak imposition $\langle\phi|C_n|\psi\rangle = 0$ instead of strong $C_n|\psi\rangle = 0$. The resulting vertex amplitude uses a non-trivial subspace $K_e \subset H_e$ of SO(4) intertwiners (with free intertwiner-degrees of freedom retained), matching the SO(3) LQG kinematical Hilbert space exactly.

**Key Results**:
- Diagnosis: BC vertex amplitude $A_{BC}(j_f) = 15j_{SO(4)}(j_f, j_f; i_{BC})$ locks all intertwiner degrees of freedom to a single vector
- New EPR vertex $A(j_f, i_e) = \sum 15j_{SO(4)} \cdot \prod f^{i_e}_{i^+i^-}$ retains intertwiner content
- Linear "boost map" $f$: $H_{SO(3)} \to H_{SO(4)}$ via spin-network evaluation on the trivial connection
- Correctly-ordered weak constraint: $C = \sqrt{C_3 + \hbar^2/4} - \sqrt{2C_4 + \hbar^2} + \hbar/2 = 0$ solved by the highest-$SO(3)$-irrep component of $(j,j)$
- Derivation from Regge discretization of Plebanski Euclidean GR; classical Hamiltonian closure constraint $\sum B_f(t) = 0$
- Boundary state space matches SO(3) LQG kinematical Hilbert space (long-sought identification)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | EPR partition function | $Z = \sum_{j,i} \prod_f ((\dim j_f)/2)^2 \prod_v A(j_f, i_e)$ |
| Eq. 2 | EPR vertex amplitude | $A(j_f, i_e) = \sum 15j_{SO(4)} \cdot \prod f^{i_e}_{i^+ i^-}$ |
| Eq. 3 | SO(4) 15j factorization | $15j_{SO(4)} = 15j(j^+,i^+) \cdot 15j(j^-,i^-)$ |
| Eq. 6 | Integral form of $A$ | $\int dV \prod D(V) \otimes i_e$ over $SU(2)^5$ |
| Eq. 9 | Unconstrained intertwiner space | $H_e = \text{Inv}(H_{(j,j)} \otimes \cdots)$ |
| Eq. 11 | Off-diagonal simplicity (operator form) | $C_{ff'} = \epsilon B^{IJ}_f B^{KL}_{f'}$ |
| Eq. 12 | Correctly-ordered weak constraint | $C = \sqrt{C_3 + \hbar^2/4} - \sqrt{2C_4 + \hbar^2} + \hbar/2$ |
| Eq. 19 | $SO(4)$ vertex from Fourier | $A = 15j_{SO(4)}(j^\pm_{tt'}, i^\pm_t)$ |

**Dependencies**: Upstream: 01 (discrete spectra), Barrett-Crane 1998 (predecessor model, refuted here), Alesci-Rovelli BC propagator failure. Downstream: 10 (long-form), 11 (EPRL with Immirzi), 14 (Lorentz covariance), 17 (modern review).

---

### Paper 10: Flipped Spinfoam Vertex and Loop Gravity (EPR Long-Form)
- **File**: `10_Engle_Pereira_Rovelli_2007_FlippedSpinfoamVertex.md`
- **arXiv**: 0708.1236
- **Year**: 2007 (August)
- **Relevance**: CRITICAL
- **Tags**: flipped vertex, EPR vertex long-form, Regge discretization, Plebanski action, simplicity constraints, K_ph projection, SO(4) <-> SU(2) boundary matching, Wieland reality conditions

**Summary**: 37-page long-form derivation of the EPR vertex from a Regge discretization of Euclidean GR in Plebanski form. The classical phase-space analysis identifies two natural symplectic structures (flipped vs unflipped) related by sign-flip of the anti-self-dual part; the unflipped (standard BF) structure gives BC, while a Hostl-action variation in conjugate variable $\Pi = B + (1/\gamma)\star B$ gives the flipped structure required for the EPR boundary matching. The physical intertwiner space $K_{\text{ph}}$ (selected by the highest-spin Clebsch-Gordan component of $(j,j) = j \otimes j$, i.e., $J^{0i} = 0$ as a quantum-Casimir relation) is isomorphic to the SO(3) intertwiner space. SU(2) spin networks of canonical LQG ARE the boundary states of the spinfoam sum -- the long-standing canonical/covariant gap is closed.

**Key Results**:
- Plebanski action $S[e,\omega] = (1/2)\int \epsilon \Sigma \wedge F = \int B \wedge F$
- Simplicity constraint: $\Sigma^{IJ} \wedge \Sigma^{KL} = V\epsilon^{IJKL}$ (Eq. 14); three component constraints (Eqs. 16-18)
- Two sectors of solutions: physical ($\Sigma = e \wedge e$, recovers GR) vs dual ($\Sigma = \star(e\wedge e)$); selected by the stronger off-diagonal simplicity $n_I\Sigma^{IJ} = 0$
- Two symplectic structures on $T^*(SO(4)^L)$ -- flipped vs unflipped; Holst topological term + $\gamma << 1$ selects flipped (the EPR case)
- Physical intertwiner space $K_{\text{ph}}$: $J^{0i} = 0$ on the spin-$2j$ component of $(j,j)$; constraint (12) $C = \sqrt{C_3 + \hbar^2/4} - \sqrt{2C_4 + \hbar^2} + \hbar/2 = 0$
- SU(2) <-> SO(4) maps: projection $\pi$ (highest-spin selection) and embedding $f$ (Clebsch-Gordan composition)
- EPR vertex amplitude: $A({j_{ab}}, {i^a}) = \sum 15j_{SO(4)} \cdot \prod f^{i^a}_{i^a_+ i^a_-}$ (Eq. 122)
- Boundary state space of EPR spinfoam $=$ SO(3) LQG canonical kinematical Hilbert space (Eq. 123 partition function)
- Companion paper (Wieland 2010): same $\mathcal{K}$ from canonical quantization of Holst action via reality conditions

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 5 | Plebanski two-form | $\Sigma^{IJ} = e^I \wedge e^J$ |
| Eq. 7 | Dual two-form | $B^{IJ} = \star\Sigma^{IJ}$ |
| Eq. 14 | Simplicity constraint | $\Sigma^{IJ} \wedge \Sigma^{KL} = V\epsilon^{IJKL}$ |
| Eq. 24-27 | Casimir relation defining K_ph | $\sqrt{C_3 + 1/4} - \sqrt{2C_4 + 1} + 1/2 = 0$ |
| Eq. 51,52 | Two simplicity sectors | $\Sigma = e \wedge e$ vs $\Sigma = \star(e \wedge e)$ |
| Eq. 78 | Holst topological term | $(1/\gamma)\sum_f \text{Tr}(\Sigma_f U_f)$ |
| Eq. 109 | Embedding $f$ in spinor form | $f(i) = \int dV \otimes_l D^{(\lambda_l)}(V) \cdot e(i)$ |
| Eq. 122 | EPR vertex amplitude | $A = \sum 15j_{SO(4)} \cdot \prod f^{i^a}_{i^a_+ i^a_-}$ |
| Eq. 170 | Holst-modified simplicity | $(1+1/\gamma^2)\star\Pi\cdot\Pi - (2/\gamma)\Pi\cdot\Pi = 0$ |

**Dependencies**: Upstream: 09 (letter), 01 (discrete area spectrum), Plebanski, Holst, Barrett-Crane. Downstream: 11 (EPRL with Immirzi), 14 (Lorentz covariance), 17 (modern review).

---

### Paper 11: LQG Vertex with Finite Immirzi Parameter (EPRL Vertex)
- **File**: `11_Engle_Livine_Pereira_Rovelli_2007_LQG_Vertex_Finite_Immirzi.md`
- **arXiv**: 0711.0146
- **Year**: 2007 (November)
- **Relevance**: CRITICAL
- **Tags**: EPRL vertex, finite Immirzi, Lorentzian SL(2,C), Euclidean Spin(4), master constraint, simplicity constraints, area spectrum match, continuous-to-discrete reduction

**Summary**: Defines the EPRL vertex amplitude for both Euclidean ($G = \text{Spin}(4)$) and Lorentzian ($G = SL(2,\mathbb{C})$) signatures at finite Immirzi parameter $\gamma$, becoming (with parallel FK) the standard 4d LQG spin-foam vertex. Key result: the boundary Hilbert space of the new spin-foam model is isomorphic to the canonical-LQG $SU(2)$ spin-network Hilbert space, AND the area operator $A_3$ has spectrum $\text{Area} = 8\pi\hbar G\gamma\sqrt{k(k+1)}$ -- the Rovelli-Smolin LQG spectrum, including the $\gamma$-dependence, holding even in the Lorentzian case despite $SL(2,\mathbb{C})$ having continuous representation labels. The simplicity constraints reduce the continuous covariant pre-constraint area spectrum (Eq. 49) to the discrete LQG spectrum (Eq. 48). The "flip" of the symplectic structure required in EPR is unnecessary at finite $\gamma$.

**Key Results**:
- Boundary Hilbert space match for both signatures and all finite $\gamma$
- Area spectrum (Eq. 48): $\text{Area} = 8\pi\hbar G \gamma \sqrt{k(k+1)}$ in BOTH signatures
- Continuous-to-discrete reduction theorem: covariant-LQG pre-constraint area $\text{Area} \sim (1/2)\sqrt{4k(k+1) - n^2 + \rho^2 + 4}$ (Eq. 49, continuous in $\rho$) collapses to discrete LQG (48) under simplicity (17, 22)
- Master constraint (Eq. 20): $M_f = \sum_i (L^i - (s/\gamma)K^i)^2$; equivalent to (14) classically; strong-imposable quantum-mechanically
- Euclidean vertex (Eq. 31): two $SU(2)$ 15j-symbols with $\gamma$-rescaled spins $(1+\gamma)j/2$ and $|1-\gamma|j/2$, glued by fusion coefficients $f^i_{i^+i^-}$
- Lorentzian vertex (Eq. 40): one $SL(2,\mathbb{C})$ 15j-symbol with arguments $(2j_{ab}, 2j_{ab}\gamma); (n_a, \rho_a)$
- Euclidean: requires rational $\gamma$ (quantization condition $(j^+)^2 = ((\gamma+1)/(\gamma-1))^2 (j^-)^2$); discrete spectrum at $k = j^+ + j^-$ for $\gamma < 1$
- Lorentzian: $\rho = \gamma n$ and $k = n/2$ selected by simplicity from the continuous $(n, \rho)$ principal-series labels
- Relation to Freidel-Krasnov: FK $\equiv$ EPRL $\gamma < 1$ case with $\gamma \mapsto 1/\gamma$

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | Bivector field | $B_f(t)^{IJ} = \int_f \star(e^I \wedge e^J)$ |
| Eq. 8 | Strengthened off-diagonal simplicity | $n_I(\star B_f)^{IJ} = 0$ -- selects $B = \star e \wedge e$ sector |
| Eq. 9 | Discrete Holst action | $S = -(1/2k)\sum \text{Tr}(BU + (1/\gamma)\star BU) +$ boundary |
| Eq. 10 | Conjugate variable | $J_f = (1/k)(B + (1/\gamma)\star B)$ |
| Eq. 12 | Diagonal simplicity in $J$-variables | $\star J \cdot J(1+s/\gamma^2) - (2s/\gamma)J\cdot J = 0$ |
| Eq. 20 | Master constraint | $M_f = \sum_i (L^i - (s/\gamma)K^i)^2$ |
| Eq. 22 | Simplified master constraint | $C_2 = 4\gamma L^2$ |
| Eq. 31 | Euclidean vertex amplitude | $A = \sum_{i^\pm} 15j(\frac{(1+\gamma)j}{2}; i^+) \cdot 15j(\frac{|1-\gamma|j}{2}; i^-) \cdot \prod f$ |
| Eq. 40 | Lorentzian vertex amplitude | $A = \sum_{n_a}\int d\rho_a (n_a^2 + \rho_a^2) \cdot \prod f \cdot 15j_{SL(2,\mathbb{C})}$ |
| Eq. 48 | Discrete area spectrum (BOTH signatures) | $\text{Area} = 8\pi\hbar G\gamma\sqrt{k(k+1)}$ |
| Eq. 49 | Pre-constraint covariant area | $\text{Area} \sim (1/2)\sqrt{4k(k+1) - n^2 + \rho^2 + 4}$ |

**Dependencies**: Upstream: 09, 10 (EPR Euclidean), Freidel-Krasnov 2007 (parallel FK construction), Holst 1996, Thiemann Master Constraint. Downstream: 14 (Lorentz covariance), 15, 16 (GFT formalization), 17 (modern review).

---

### Paper 12: Group Field Theory and Simplicial Quantum Gravity
- **File**: `12_Oriti_2009_GFT_Simplicial_QuantumGravity.md`
- **arXiv**: 0902.3903
- **Year**: 2009
- **Relevance**: HIGH
- **Tags**: generalized GFT, Lie-algebra simplicity, Plebanski path integral, Regge action recovery, dynamical triangulations bridge, Bonzom constraints, edge simplicity

**Summary**: New constructive 4d GFT model whose Feynman amplitudes are explicit simplicial path integrals for 1st-order gravity (Regge-type action) with manifest geometric interpretation. Extends the standard GFT formalism to a "generalized GFT" with fields depending on BOTH group elements $g_i$ and Lie-algebra elements $B_i$, allowing simplicity constraints to be imposed at the path-integral classical level on independent $B$ variables -- side-stepping the coherent-state-parameter ambiguities of the standard spin-foam route. Shows dynamical triangulations correspond to a simple restriction of the model.

**Key Results**:
- Field $\phi(x_1, b_1^+; \ldots; x_4, b_4^+)$ on $(S^3 \times \mathfrak{su}(2))^4$ via projectors $P_B$ (simplicity), $P_g$ (covariance), $P_h$ (homogeneous-space reduction)
- Klein-Gordon-like kinetic operator with $B^2$-dependent mass; vertex term encodes 4-simplex combinatorics
- Feynman amplitudes split into Regge action term $S_R^f = |B_f| \cdot |[\theta_f(H_f)]|$ + simplicity constraint + compatibility delta + quantum corrections $S_c$
- Full amplitude: simplicial path integral for discrete Plebanski formulation of 4d gravity as constrained BF theory
- Dynamical triangulations as restriction: fix $|B|$ and dihedral holonomy $h = e^{i\phi} \in U(1)$
- Compatibility constraints (Eq. 10) reduce BF gauge invariance to $B \to GBG^{-1}, H \to GHG^{-1}$ -- equivalent to ordinary Regge calculus at the classical level (Bonzom 2009)
- Pre-causality condition $\text{Tr}(B_f F_f) > 0$ enforced
- Two classes of simplicity solutions: weak (per Barrett-Crane / EPRL-like) vs strong (Bonzom edge simplicity / Dittrich-Ryan)
- Stage-set for non-commutative GFT via the Baratin-Oriti star-product Fourier transform

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | Plebanski-form partition function | $Z = \int Dg \, DB \prod_e C(B) e^{i\sum \text{Tr}(BF)}$ |
| Eq. 3 | Kinetic operator | $K = \prod (B_i^2 + \Box_{G_i} - m^2/4)$ |
| Eq. 6 | Simplicity projector $P_B$ | $C(B) = \int dN_t \prod \delta(b^- \mp Nb^+N^{-1}) \delta(\sum b^+)$ |
| Eq. 8 | Feynman amplitude | $Z_\Gamma = \prod\int dg\,db \prod C \prod A[B,g]$ |
| Eq. 9 | Per-face amplitude | $A = \mu(H, B) \cdot \mathcal{W} \cdot e^{iS_R^f} \cdot e^{iS_c^f}$ |
| -- | Regge action contribution | $S_R^f = |B_f| \cdot |[\theta_f(H_f)]|$ |
| Eq. 10 | Compatibility constraint | $\delta(B_1 - H_f \triangleright B_1)$ |

**Dependencies**: Upstream: 07 (GFT sketch), Boulatov 1992, Ooguri 1992, Oriti-Tlas 2008, 09 (EPR), 11 (EPRL). Downstream: 15, 16 (Oriti GFT reviews).

---

### Paper 13: Prospects for Constraining Quantum Gravity Dispersion with Near Term Observations
- **File**: `13_Amelino-Camelia_Smolin_2009_QGDispersionFermiGRB.md`
- **arXiv**: 0906.3731
- **Year**: 2009
- **Relevance**: MEDIUM
- **Tags**: QG phenomenology, Lorentz modification, Fermi LAT, GRB 080916C, NLSB, LSB-EFT, DSR, Myers-Pospelov, modified dispersion, M_QG bounds

**Summary**: QG phenomenology paper using Fermi LAT GRB observations to bound modified-dispersion frameworks (NLSB / LSB-EFT / DSR). Reviews three testable scenarios for in-vacuo dispersion at leading order $\alpha = 1$ (one-parameter $M_{QG}$); compiles the first eight Fermi-LAT GRBs with $> 100$ MeV photons; analyzes GRB 080916C in detail. Derives conservative bound $M_{QG} > 1.3 \times 10^{18}$ GeV $\approx 0.1 M_P$ from the 13.6 GeV photon arrival; less-conservative bound $> 1.8 \times 10^{18}$ GeV using the second GBM peak; superluminal bound $> 3.2 \times 10^{17}$ GeV. Proposes forward observational program at $10^{14}$ to $10^{17}$ eV with day-to-month delays from GRBs to cleanly separate astrophysical from QG effects. Includes discussion of Immirzi-parameter-induced mixed-parity dispersion as LQG-specific motivation.

**Key Results**:
- Three frameworks: NLSB (broken Lorentz, no birefringence, no EFT), LSB-EFT (Myers-Pospelov, predicts birefringence), DSR (deformed Lorentz, modified energy-momentum conservation)
- Leading-order modified dispersion: $E \simeq p + m^2/(2p) - s_\pm E^{\alpha+1}/(2M_{QG}^\alpha)$
- Arrival-time relation: $\Delta t = (\Delta E/M_{QG})L$ (cosmological-corrected form Eq. 14)
- Fermi-LAT 8-GRB compilation (Table 1)
- Subluminal bound from 080916C: $M_{QG} > 1.3 \times 10^{18}$ GeV (conservative); $> 1.8 \times 10^{18}$ GeV (second-peak)
- Superluminal bound: $M_{QG}^{[s_\pm = -1]} > 3.2 \times 10^{17}$ GeV
- "Conspiracy" caveat for superluminal bounds at $\sim 4 \times 10^{17}$ GeV
- Forward program: TeV photons, $10^{14}$-$10^{17}$ eV neutrinos at ICECUBE / Auger, expecting day-to-month delays at $M_P$
- Two-parameter models: fuzzy dispersion (Eq. 21) and mixed-parity (Eq. 22) from LQG Immirzi-parameter chirality
- LQG context: Gambini-Pullin LSB-EFT not a definite LQG prediction (depends on non-physical ground state); DSR connection to LQG only heuristic in 3+1d (proven only in 2+1d)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 3 | Modified dispersion | $E = p + m^2/(2p) - s_\pm E^{\alpha+1}/(2M_{QG}^\alpha)$ |
| Eq. 6 | Myers-Pospelov LSB-EFT Lagrangian | Adds $(1/M_{Planck}) n^\alpha F_{\alpha\delta} n^\sigma \partial_\sigma(n_\beta \varepsilon^{\beta\delta\gamma\lambda} F_{\gamma\lambda})$ |
| Eq. 8 | DSR dispersion | $0 = 8M_{dsr}^2[\cosh(E/2M_{dsr}) - \cosh(m/2M_{dsr})] - p^2 e^{s_\pm E/(2M_{dsr})}$ |
| Eq. 13 | Arrival-time relation | $\Delta t = s_\pm (\Delta E/M_{QG}) L$ |
| Eq. 15 | Conservative Fermi bound | $M_{QG} > 1.3 \cdot 10^{18}$ GeV |
| Eq. 17 | Superluminal bound | $M_{QG}^{[s_\pm = -1]} > 3.2 \cdot 10^{17}$ GeV |
| Eq. 21 | Fuzzy dispersion two-parameter | $v(E) = 1 - \eta E/M_P \pm \eta/(M_P \Delta t^*) \pm \eta_f E/M_P$ |
| Eq. 22 | Mixed-parity dispersion | $\delta v = -(\alpha + \beta\langle s \rangle) E/M_{QG}$ |

**Dependencies**: Upstream: Gambini-Pullin LSB-EFT (LQG-rooted), Amelino-Camelia DSR foundations, Myers-Pospelov framework. Cross-link: 17 sec. 4.2 (CMB observational anchor as parallel channel). Downstream: standard reference for LQG phenomenology.

---

### Paper 14: Lorentz Covariance of Loop Quantum Gravity
- **File**: `14_Rovelli_Speziale_2011_LorentzCovariance_LQG.md`
- **arXiv**: 1012.1739
- **Year**: 2011
- **Relevance**: HIGH
- **Tags**: Lorentz covariance, Dupuis-Livine map, SL(2,C) projected functions, K space, simplicity constraints, Gupta-Bleuler analogy, bulk invariance, boundary covariance

**Summary**: Resolves the long-standing tension between canonical LQG ($SU(2)$ time-gauge, breaking manifest local Lorentz covariance) and spin-foam dynamics ($SL(2,\mathbb{C})$-covariant EPRL/FK vertex). Constructs a linear subspace $\mathcal{K}$ of $SL(2,\mathbb{C})$ functions with degree $p(j) = \gamma j$ (image of the Dupuis-Livine map $f$) that is linearly isomorphic to the canonical LQG Hilbert space $\mathcal{H}_{SU(2)}$. $\mathcal{K}$-elements are NOT square-integrable in the $SL(2,\mathbb{C})$ Haar measure (they are discrete linear combinations of distributions, structurally parallel to LQC's Bohr-compactification states) but are well-defined in the induced $SU(2)$ inner product. Theorem 2 (bulk $SL(2,\mathbb{C})$-invariance of spinfoam amplitudes) and Theorem 3 (boundary $SL(2,\mathbb{C})$-covariance) establish that local Lorentz transformations act as a gauge symmetry of the bulk dynamics and as a covariance property of boundary data -- mirroring the classical situation in GR. The Gupta-Bleuler-style framework is invoked as conceptual analogy: $\mathcal{K}$ is a Lorentz-covariant function space without positive-definite Lorentz-invariant inner product. Companion paper (Wieland 2010) derives $\mathcal{K}$ from canonical Holst-action quantization via reality conditions.

**Key Results**:
- Dupuis-Livine map $f: \psi(h) \mapsto \tilde\psi(g)$ (Eq. 1) from $SU(2)$ to $SL(2,\mathbb{C})$ functions with kernel (Eq. 2)
- Projected functions: $\mathcal{K}$-elements fully determined by their restriction to $SU(2)$ (Eq. 6, 7)
- Non-square-integrability in $L^2[SL(2,\mathbb{C})]$ (Eq. 12); fixed relation $p = \gamma k$ forces discrete-delta structure
- Well-behaved $SU(2)$-induced scalar product (Eq. 13)
- Degree fixed by linear simplicity constraints: $\vec K + \gamma \vec L = 0$ (Eq. 15), gauge-invariant Casimir form (Eq. 16); strong form on $\mathcal{K}$ (Eq. 17); weak form in $j \to \infty$ limit (Eq. 18)
- Ashtekar-Barbero connection correspondence: $\omega|_\mathcal{K} = A^i L_i$, $A^i = \omega^i + \gamma\omega^{0i}$
- Theorem 1: spinfoam boundary states lie in $\mathcal{K}$ (Eq. 25)
- Theorem 2: bulk $SL(2,\mathbb{C})$ invariance -- amplitudes independent of internal-edge $x_e$
- Theorem 3: boundary $SL(2,\mathbb{C})$ covariance: $\tilde Z_{\Lambda_n x_n}(g_l) = \tilde Z_{x_n}(\Lambda_{s_l} g_l \Lambda_{t_l})$ (Eq. 34)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1-2 | Dupuis-Livine map | $\tilde\psi(g) = \int dh K(g,h)\psi(h)$ |
| Eq. 12 | Non-square-integrability | $\psi_{kjmj'm'}(p) = \delta(p - p(k))/(p^2 + k^2) \cdot \ldots$ |
| Eq. 13 | $SU(2)$-induced scalar product on $\mathcal{K}$ | Kronecker delta replacement |
| Eq. 14 | Degree pin | $p(j) = \gamma j$ |
| Eq. 15 | Linear simplicity in time gauge | $\vec K + \gamma\vec L = 0$ |
| Eq. 16 | Gauge-invariant form | $2\gamma C_1 - (\gamma^2 - 1) C_2 = 0$ |
| Eq. 21 | $SL(2,\mathbb{C})$ holonomy from SU(2) restriction | $g\|_\mathcal{K} = D^{\gamma j, j}_{jm,jn}(g)$ |
| Eq. 22 | EPRL/FK partition function | $Z_\mathcal{C}(h_l) = \int dg\, dh \sum_j \prod d_j \chi^{\gamma j_f, j_f}(\cdots)$ |
| Eq. 34 | Boundary Lorentz covariance | $\tilde Z_{\Lambda_n x_n}(g_l) = \tilde Z_{x_n}(\Lambda_{s_l} g_l \Lambda_{t_l})$ |

**Dependencies**: Upstream: 09, 10, 11 (EPR/EPRL vertex); Livine projected spin networks; Alexandrov-Livine covariant LQG; Dupuis-Livine 2010 lifting map; Wieland 2010 (companion). Downstream: 17 (modern review boundary-amplitude formalism), 18 (philosophical foundations).

---

### Paper 15: The Microscopic Dynamics of Quantum Space as a Group Field Theory
- **File**: `15_Oriti_2011_GFT_MicroscopicDynamicsQuantumSpace.md`
- **arXiv**: 1110.5606
- **Year**: 2011
- **Relevance**: HIGH
- **Tags**: GFT review, Boulatov model, Ooguri model, Plebanski, EPRL via GFT, FK via GFT, BC model, BO model, colored GFT, large-N theorem, kappa-Minkowski, geometrogenesis, condensate cosmology

**Summary**: 60-page review of group field theory by its principal architect. Comprehensive coverage of: (i) GFT formalism, combinatorial non-locality, and its perturbative spin-foam expansion; (ii) the Boulatov 3d Riemannian model (Ponzano-Regge equivalence; Lie-algebra Fourier transform); (iii) the Ooguri 4d BF model and constrained-BF strategies (state-sum / spin-foam: BC, EPR, EPRL, FK; non-commutative geometric / Lie-algebra: Baratin-Oriti); (iv) the colored GFT and Gurau large-N theorem dominating manifold topology over pseudo-manifolds; (v) renormalization landmarks and FRG analyses; (vi) emergent kappa-Minkowski non-commutative QFT from mean-field perturbations around flat-class solutions (DSR field theory); (vii) GFT condensate cosmology and the geometrogenesis hypothesis replacing the big bang with a phase transition. Includes a detailed list of open issues across all subprograms.

**Key Results**:
- Three equivalent representations of GFT Feynman amplitudes: group, Lie-algebra (simplicial-gravity path integral), spin-foam (Ponzano-Regge / EPRL / FK)
- Boulatov amplitude $Z(\Gamma) = \sum_j \prod \Delta_j \prod_v 6j$ = Ponzano-Regge
- Constrained-BF strategies for 4d gravity: (1) state-sum imposes Plebanski constraints as operator equations on BF spin networks (yields BC, FK, EPR, EPRL); (2) non-commutative geometric imposes constraints directly in Lie-algebra rep via non-commutative delta projector (yields BO variants and alternative finite-Immirzi)
- Two structural properties of modern 4d models: (i) boundary spin networks match canonical LQG kinematics with same area/volume spectra (Ding-Rovelli 2010); (ii) vertex amplitudes -> cosine of Regge action in semiclassical large-$j$ limit (Barrett et al.)
- Colored GFT (Gurau 2009): only orientable simplicial complexes; bubbles defined; cellular homology computable
- Gurau's 1/N theorem: large-$N$ limit dominated by trivial-topology manifolds (melonic dominance)
- Mean-field perturbations around flat solutions: emergent kappa-Minkowski non-commutative scalar field theory with deformed Poincare symmetry
- Symmetry identification: translation symmetry of 3d BF $\equiv$ simplicial diffeomorphism (Baratin-Girelli-Oriti 2011); broken by simplicity in 4d
- Geometrogenesis hypothesis: spacetime is a condensate of GFT quanta; phase transition replaces big bang

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 14 | Closure / Gauss constraint | $\phi = P\phi = \int dh \phi(hg_1,\ldots)$ |
| Eq. 15 | Spin-network expansion of $\phi$ | $\phi = \sum \phi^{jjj}_{mmm} D D D C$ |
| Eq. 18 | Boulatov 3d action | $S = (1/2)\int\phi^2 - (\lambda/4!)\int \phi\phi\phi\phi$ |
| Eq. 20 | Lie-algebra Feynman amplitude | $Z = \int prod dh dx exp(i\sum\text{Tr}(xH))$ |
| Eq. 22 | Ooguri 4d action | 5-valent vertex over $SO(4)^4$ |
| Eq. 23 | 4d BF spin foam | $Z = \sum \prod (2j+1)(2j+1) \prod 15j_+ 15j_-$ |
| Eq. 24-25 | Discrete simplicity | $(\star B_f)^{IJ} n_{tJ} = 0$ |
| Eq. 28 | Colored GFT action | 4 complex fields, one per color |
| Eq. 37 | kappa-Minkowski algebra | $[X_0, X_k] = -i X_k/\kappa$ |
| Eq. 43 | Emergent NC matter QFT | Standard kappa-deformed scalar field action |

**Dependencies**: Upstream: 07 (GFT sketch), 12 (Oriti 2009 GFT), Boulatov 1992, Ooguri 1992, 09-11 (EPR/EPRL); Gurau colored GFT. Downstream: 16 (Oriti 2014 synthesis).

---

### Paper 16: Group Field Theory and Loop Quantum Gravity
- **File**: `16_Oriti_2014_GroupFieldTheory_LQG.md`
- **arXiv**: 1408.7112
- **Year**: 2014
- **Relevance**: HIGH
- **Tags**: GFT-LQG synthesis, Fock structure over single-vertex Hilbert space, tensor-invariant interactions, EPRL kernel, BO model, FRG renormalization, condensate cosmology, emergent Friedmann equation

**Summary**: 23-page chapter introducing GFT from the LQG perspective. Presents GFT as a methodological reformulation that unifies (i) canonical LQG kinematics (same spin-network single-vertex Hilbert spaces; Fock structure over $\mathcal{H}_v$), (ii) covariant spin-foam dynamics (vertex amplitudes as GFT interaction kernels = matrix elements of the LQG projector operator), (iii) simplicial gravity (Feynman diagrams = cellular complexes dual to triangulations), and (iv) tensor models (tensorial axiomatics give crystallization-theorem-controlled diagrams). Three dynamics strategies: from canonical LQG, from spin foams / lattice gravity, from tensorial axiomatics. Emphasizes the continuum-limit problem (renormalization, phase structure, constructive definition, effective continuum) and develops GFT condensate cosmology with Gross-Pitaevskii ansatz yielding a non-linear extension of the Wheeler-DeWitt equation -- specifically of LQC. Derives effective Friedmann equation with built-in holonomy corrections.

**Key Results**:
- Fock space over $\mathcal{H}_v = L^2(G^{\times d})$ with bosonic statistics (Eq. 3)
- Spin-network embedding into Fock space (Eq. 5) via group-averaging
- Comparison: GFT Hilbert space vs LQG $\mathcal{H}^1, \mathcal{H}^2$ (direct sum vs projective limit); GFT differences (abstract graphs, no diffeo action, no cylindrical equivalence, $N$-graded orthogonality, $\hat N$ as observable)
- Strategy 1: GFT dynamics from canonical LQG via 2nd-quantized projector $\hat F$; interaction kernel = matrix elements of $P$
- Strategy 2: EPRL kernel (rational $\gamma$, Spin(4) self/anti-self-dual decomposition); BO kernel (Lie-algebra normal $k_i$)
- Strategy 3: Tensorial axiomatics; crystallization theorem giving one-to-one correspondence between $(d+1)$-coloured graphs and simplicial pseudo-manifolds
- Renormalization landmarks: colors give topology control, large-$N$ dominated by melonic spheres, Laplace-Beltrami kinetic term necessary for renormalizability, non-abelian gauge GFT renormalizable to order six (Carrozza-Oriti-Rivasseau 2014)
- GFT condensate ansatz (Eq. 9) yields classical EOM of original GFT model (Eq. 10) = non-linear extension of Wheeler-DeWitt for LQC
- Effective semiclassical Friedmann equation with holonomy corrections encoded in sine functions -- LQC structural form recovered; $N$-dependence derived (not assumed) from the number of fundamental cells

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | GFT action | $S = \int \phi^* K \phi + \sum \lambda V \cdots$ |
| Eq. 2 | Partition function | $Z = \sum_\Gamma \lambda^n/sym(\Gamma) \cdot \mathcal{A}_\Gamma$ |
| Eq. 3 | Fock bosonic algebra | $[\hat\phi, \hat\phi^\dagger] = \mathbb{I}_G$ |
| Eq. 5 | Spin-network embedding | $\Psi_\Gamma = \int d\alpha \phi(\cdots g\alpha \cdots)$ |
| Eq. 6 | Spin-network basis | $\psi_{\vec\chi}(\vec g) = \prod D^{J_a}_{m_a n_a}(g_a) C_n^{\mathcal I}$ |
| Eq. 7 | Dynamics from canonical | $S = m^2\int\phi^\dagger\phi - \sum\lambda V \cdots$ |
| Eq. 8 | Tensorial action | $S = \int\phi^*\mathcal{K}\phi^* + \sum t_b I_b$ |
| Eq. 9 | Condensate ansatz | $|\sigma\rangle = \mathcal{N} \exp(\hat\sigma)|0\rangle$ |
| Eq. 10 | Effective collective EOM | $\int \tilde{\mathcal{K}}\sigma + \lambda \delta\tilde{\mathcal{V}}/\delta\bar\phi = 0$ |

**Dependencies**: Upstream: 07, 12, 15 (Oriti GFT line), 09-11 (EPRL/FK), Gielen-Oriti-Sindoni 2013 (condensate cosmology landmark). Downstream: cited in 17 (modern review).

---

### Paper 17: A Short Review of Loop Quantum Gravity
- **File**: `17_Ashtekar_Bianchi_2021_Short_Review_LQG.md`
- **arXiv**: 2104.04394
- **Year**: 2021
- **Relevance**: CRITICAL
- **Tags**: modern LQG review, key-issue review, kinematics + dynamics + LQC + BH, area gap, EPRL vertex, big bounce, CMB power suppression alleviation, lensing anomaly

**Summary**: Modern authoritative review of LQG (35 pages, ~160 refs), addressed to non-experts. Covers (i) quantum Riemannian geometry: Ashtekar-Sen variables, LOST/F uniqueness theorem, spin networks, area gap $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ as fundamental microscopic parameter; (ii) quantum dynamics: BF + simplicity constraint, EPRL vertex, semiclassical Regge-action reconstruction via boundary amplitude formalism; (iii) Loop quantum cosmology: big bounce at $\rho_{\text{sup}} \approx 0.41\,\rho_{\text{Pl}}$, effective Friedmann equation, alleviation of CMB anomalies (power suppression at $\ell \lesssim 30$; lensing amplitude $A_L$; hemispherical anisotropy); (iv) Discussion section: Hamiltonian dynamics (Thiemann), black hole entropy, comparison with string theory and asymptotic safety. Bidirectional inference: the area gap can be inferred independently from BH entropy and from CMB observations -- two independent quantum-gravity constraints on the same microscopic parameter.

**Key Results**:
- Holst-action discretized form (Eq. 14): GR = BF + Plebanski simplicity, with Immirzi $\gamma$ coupling Holst term
- LOST/F uniqueness theorem: background independence singles out unique representation of $\mathfrak{A}$ -- "vastly stronger than Poincare invariance"
- Spin-network decomposition (Eq. 9): $\mathcal{H}_{\text{grav}}^{\text{kin}} = \bigoplus_{\Gamma, j_\ell, i_n} \mathcal{H}_{\Gamma, j_\ell, i_n}$ in finite-dim subspaces
- Area gap $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ "subsumes Immirzi $\gamma$ as the fundamental physical parameter"
- EPRL vertex amplitude (Eq. 17): $W_\Delta[s,s'] = \sum \prod A_f A_v^{(\gamma)}(j_f, i_e)$ built from $\gamma$-simple SO(3,1) reps
- Semiclassical reconstruction: $\langle W_\Delta | \Psi \rangle \sim e^{iS_{GR}/\hbar} +$ c.c. (4D Lorentzian generalization of Ponzano-Regge)
- LQC effective Friedmann: $(\dot a/a)^2 = (8\pi G\rho/3)(1 - \rho/\rho_{\text{sup}})$ with $\rho_{\text{sup}} = 18\pi G\hbar^2/\Delta^3 \approx 0.41 \rho_{\text{Pl}}$
- CMB anomaly alleviation: LQC predicts power suppression at $\ell \lesssim 30$; cuts $S_{1/2}$ discrepancy by factor of 3; brings $A_L = 1$ inside 1-sigma; explains hemispherical anisotropy [refs 139-141]
- Bidirectional area-gap determination: BH-entropy fixed $\Delta$ value within 68% confidence of CMB-inferred posterior

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | ADM constraints (geometrodynamics) | $C_a = -2q_{ac}D_b p^{ac}$, etc. |
| Eq. 4 | Three gauge-theory constraints | Gauss, vector, scalar |
| Eq. 5 | Seven first-class constraints | Match GR's 2 dof |
| Eq. 9 | Spin-network decomposition | $\mathcal{H}^{\text{kin}}_{\text{grav}} = \bigoplus_{\Gamma, j_\ell} \mathcal{H}_{\Gamma, j_\ell}$ |
| -- | Area gap | $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ |
| Eq. 14 | GR Einstein-Cartan + Holst | Holst term coefficient $-1/\gamma$ |
| Eq. 17 | EPRL transition amplitude | $W_\Delta = \sum \prod A_f A_v^{(\gamma)}$ |
| -- | Critical density | $\rho_{\text{sup}} = 18\pi G\hbar^2/\Delta^3 \approx 0.41 \rho_{\text{Pl}}$ |
| Eq. 19 | Effective Friedmann | $(\dot a/a)^2 = (8\pi G\rho/3)(1 - \rho/\rho_{\text{sup}})$ |

**Dependencies**: Upstream: 01-16 in this corpus -- this paper synthesizes the entire LQG arc. Downstream: 18 (philosophical companion).

---

### Paper 18: Philosophical Foundations of Loop Quantum Gravity
- **File**: `18_Rovelli_Vidotto_2022_Philosophical_Foundations_LQG.md`
- **arXiv**: 2211.06718
- **Year**: 2022
- **Relevance**: HIGH
- **Tags**: philosophical foundations, relational space, partial observables, boundary amplitude, Heisenberg cut, truncation discipline, emergent time, problem of time, classical limit, Ditt-invariance

**Summary**: 27-page chapter in the Springer Handbook of Quantum Gravity (2023), synthesizing the conceptual structure of LQG. Distinguishes relational space (contiguity relations between physical entities; non-metric; survives QG) from Newtonian container space (emerges only as approximation). Develops the partial-observables formalism (Rovelli) and the boundary-amplitude formalism (Conrady-Doplicher-Oeckl-Rovelli-Testa) where the Heisenberg cut is identified with the boundary of a 4d spacetime region. Defends finite-graph truncation calculations as analogous to lattice QCD ("conceptually ill-founded" to suggest finite-graph calculations are unreliable). Articulates three notions of time (relational / Newtonian / experienced) and partitions the "problem of time" into Question 1 (dynamics without canonical time -- answered by partial observables) and Question 2 (why time flows -- answered via Newtonian-limit + entropy gradient + brain functioning, references to Rovelli's broader work on the arrow of time).

**Key Results**:
- Relational space vs Newtonian container space distinction; three-step emergence chain (Newtonian -> Minkowski -> Riemannian -> quantum)
- Three quantum-Riemannian features: granularity (discrete spectrum), superposition of geometries, short-scale fuzziness (non-commutativity)
- Intrinsic / extrinsic coherent states $|\psi_g\rangle, |\psi_{g,k}\rangle$ on $\mathcal{H}_\Gamma$ minimally-spread on metric data
- Three readings of GR gauge degrees of freedom: (1) diffeomorphism-invariant only, (2) gauge-fixed, (3) relational coupling to external reference -- all three localizations are relative
- Partial observables: variables that can be measured but cannot individually be predicted; theory predicts relations among them
- Extended phase space $\Gamma_{ex}$ + constraint $C$: motions are null directions of induced presymplectic form on $C = 0$
- Boundary amplitude formalism: Heisenberg cut = 3-surface $\Sigma$ bounding compact 4-region $\mathcal{R}$; $W(b, t'; a, t) = \langle W | b, t'; a, t\rangle$
- Semiclassical recovery: $\langle W | \Psi_g \rangle \sim \sum_n e^{-i S_n[g]/\hbar}$ with Hamilton function $S_n[g] = \int \sqrt{-g_4} R$
- Truncation discipline: finite-graph spinfoam analogous to lattice QCD with finite size + finite resolution
- Physical Planck-scale discreteness vs truncation discreteness distinction
- Classical limit requires joint continuum + large-spin limits taken together (Ditt-invariance subtlety)
- Three notions of time (relational / Newtonian / experienced); change vs time distinction
- Problem of time partitioned: dynamics-without-canonical-time (partial observables) vs why-time-flows (Newtonian-limit + entropy + brain)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Eq. 1 | Regge polyhedral metric | $G_n^{\ell\ell'} = A_\ell A_{\ell'} \vec n_\ell \cdot \vec n_{\ell'}$ |
| Eq. 3 | Coherent state expectation | $\langle\psi_g|\hat G_n^{\ell\ell'}|\psi_g\rangle = G_n^{\ell\ell'} + O(\hbar)$ |
| Eq. 6 | Transition amplitude via projector | $W(a,b) = \langle a|P|b\rangle$ on $\ker C$ |
| Eq. 11 | GR transition amplitude | $W(b,t';a,t) = \langle b,t'|P|a,t\rangle$ |
| Eq. 13 | Boundary bra form | $\langle W|\psi\rangle = \langle\Psi_+|P|\Psi_-\rangle$ |
| Eq. 14 | Wheeler-Misner functional integral | $\langle W|\Psi_g\rangle = \int_{\partial g_4 = g} Dg_4 e^{-iS/\hbar}$ |
| Eq. 15-16 | Semiclassical recovery + Hamilton function | $\langle W|\Psi_g\rangle \sim \sum e^{-iS_n[g]/\hbar}$, $S_n[g] = \int \sqrt{-g_4} R$ |

**Dependencies**: Upstream: foundational LQG textbooks (Rovelli 2004; Rovelli-Vidotto 2015; Thiemann; Gambini-Pullin) + 01-17 in this corpus. Cited prominently: 01, 02, 03 (BH entropy and discrete spectra), 04, 08 (LQC bounce), 09-11 (EPR/EPRL vertex), 14 (Lorentz covariance), 17 (modern review).

---

## Cross-Paper Equation Concordance

### Area gap and area spectrum
The area gap appears with consistent normalization across Papers 01, 02, 03, 05, 11, 17.

- **Paper 01 (1994 original)**: $A = (1/2) l_P^2 \sum_l \sqrt{p_l^2 + 2 p_l} = \sum_l \hbar\sqrt{j_l(j_l+1)}$ with $j_l = p_l/2$. No Immirzi parameter (pre-1996).
- **Paper 02 (1997 introduces Immirzi)**: $A = 8\pi\gamma\ell_P^2 \sum_p \sqrt{j_p(j_p+1)}$ (Eq. 7).
- **Paper 03 (2000 long-form)**: Same form (Eq. 20). Establishes universality across charged horizons.
- **Paper 05 (2004 status report, general 3-valent form)**: $a_S = 4\pi\gamma\ell_P^2 \sum_I \sqrt{2j^{(u)}(j^{(u)}+1) + 2j^{(d)}(j^{(d)}+1) - j^{(u+d)}(j^{(u+d)}+1)}$ (Eq. 5.14) with the special case for surfaces with no edges lying within reducing to the Paper 02 form. Area gap: $\Delta a_S = 4\pi\gamma\ell_P^2 \cdot \sqrt{3}/2$ (Eq. 5.15) -- corresponds to $j = 1/2$ link puncture.
- **Paper 11 (2007 EPRL)**: Lorentzian + Euclidean area spectrum match: $\text{Area} = 8\pi\hbar G\gamma\sqrt{k(k+1)}$ (Eq. 48) on the simplicity-constrained boundary.
- **Paper 17 (2021 modern review)**: $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ -- consolidates Paper 05's $\sqrt{3}/2$ factor with the $j = 1/2$ puncture. "Subsumes Immirzi $\gamma$ as the fundamental physical parameter."

**Convention notes**: Paper 01 uses $G = 1$ so $\ell_P^2 = \hbar$. Papers 02, 03, 05, 11, 17 restore $G$ and $\hbar$. Papers 11, 17 absorb $G\hbar$ into $\ell_P^2$. The Immirzi parameter convention is $\gamma > 0$ real throughout (SU(2) gauge group); the BH-entropy-pinned value $\gamma_0 = \ln 2/(\pi\sqrt{3}) \approx 0.127$ (Papers 02, 03) is convention-dependent at the SU(2) vs U(1) Chern-Simons gauge-group choice (later SU(2) refinements give $\gamma_0 \approx 0.2375$, mentioned in Paper 03 §VII).

### Immirzi parameter and BH entropy
Papers 02, 03 derive $\gamma_0 = \ln 2/(\pi\sqrt{3})$ from matching Bekenstein-Hawking. Paper 05 sec. VIII gives the same. Paper 17 sec. 5 cross-checks against CMB observations (sec. 4.2).

The entropy formula $S_\Delta = (\gamma_0/\gamma)(a_o/(4\ell_P^2)) + o(\ell_P^2/a_o)$ (Eq. 8.10 of Paper 05) reduces to $S = A/(4\ell_P^2)$ at $\gamma = \gamma_0$. Paper 03's partition-function derivation (Eq. 50, leading pole at $\alpha_0 = \ln 2/(4\pi\sqrt{3}\gamma\ell_P^2)$) gives the same prefactor.

### LQC critical density
- **Paper 04 (Bojowald 2001)**: Singularity removal via difference equation propagation through $n = 0$. No explicit critical density; the bounce is implicit in the structure.
- **Paper 08 (APS 2006)**: Explicit critical density $\rho_{\text{crit}}$ depending on $p_\phi^*$; bounce mechanism numerically demonstrated.
- **Paper 17 (modern form)**: $\rho_{\text{sup}} = 18\pi G\hbar^2/\Delta^3 \approx 0.41\,\rho_{\text{Pl}}$ as a universal LQC bounce density derived from the area gap.

### Spinfoam vertex amplitude
- **Paper 09 (EPR letter, Euclidean only, no Immirzi)**: $A(j_f, i_e) = \sum 15j_{SO(4)} \cdot \prod f^{i_e}_{i^+i^-}$ (Eq. 2). Face weight $((\dim j_f)/2)^2$.
- **Paper 10 (EPR long-form)**: Same with full derivation; partition function (Eq. 123).
- **Paper 11 (EPRL with Immirzi)**: Euclidean vertex (Eq. 31) factorizes into two $SU(2)$ 15j's at $(1+\gamma)j/2$ and $|1-\gamma|j/2$ spins; Lorentzian vertex (Eq. 40) uses $SL(2,\mathbb{C})$ 15j with continuous label $\rho = \gamma n$.
- **Paper 14 (Lorentz covariance)**: Same EPRL partition function in covariant form (Eq. 22), now boundary-covariance-explicit.
- **Paper 17 (modern review)**: EPRL transition amplitude (Eq. 17) $W_\Delta = \sum \prod A_f A_v^{(\gamma)}$.

### Plebanski simplicity constraint
- **Paper 09, 10 (EPR)**: $\Sigma^{IJ} \wedge \Sigma^{KL} = V\epsilon^{IJKL}$ (Eq. 14 of Paper 10); component form: diagonal $\star\Sigma_{ab}\cdot\Sigma_{ab} = 0$, off-diagonal $\star\Sigma_{ab}\cdot\Sigma_{ac} = 0$.
- **Paper 11 (EPRL)**: Reformulated as $J$-variable constraints (Eqs. 12-14); master constraint $M_f = \sum_i (L^i - (s/\gamma)K^i)^2$ (Eq. 20).
- **Paper 12 (Oriti GFT)**: Discrete simplicity via $\exists N_t \in S^3$ such that $B_f^{IJ}n_{tJ} = 0$; weakly imposed via $P_B$ projector (Eq. 6 of Paper 12) at each tetrahedron.
- **Paper 14 (covariance)**: Linear simplicity $\vec K + \gamma \vec L = 0$ (Eq. 15); strong form on $\mathcal{K}$.
- **Paper 17 (modern review)**: $B_{IJ} = (1/(16\pi G))[(1/2)\epsilon_{IJKL} e^K\wedge e^L - (1/\gamma)e_I\wedge e_J]$ (Eq. 16) -- "$\gamma$-simple" BF reduction.

## Notation Conventions

| Symbol | Meaning |
|:-------|:--------|
| $\gamma$ | Barbero-Immirzi parameter (real, positive); appears in connection $A^i_a = \Gamma^i_a - \gamma K^i_a$, area spectrum, and Holst action |
| $\gamma_0$ | BH-entropy-pinned value $\ln 2/(\pi\sqrt{3})$ (Papers 02, 03, 05; convention-dependent at gauge-group level) |
| $\Delta$ | area gap = $4\sqrt{3}\pi\gamma\ell_P^2$ (Paper 17 convention) or $4\pi\gamma\ell_P^2 \cdot \sqrt{3}/2$ (Paper 05 convention; identical) |
| $\ell_P$ | Planck length $= \sqrt{\hbar G/c^3}$; convention: $\ell_P^2 = \hbar G$ |
| $j$, $j_\ell$, $j_f$ | half-integer SU(2) spin label on link or face; $j \in \mathbb{N}/2$ |
| $i_e$, $i_n$ | intertwiner at edge or node (SU(2)-invariant subspace of tensor product of edge irreps) |
| $h_\ell(A)$ | holonomy / Wilson line along curve $\ell$ |
| $E_{f,S}$ | electric flux smeared over 2-surface $S$ with test function $f$ |
| $\mathcal{H}_{\text{kin}}, \mathcal{H}_{\text{grav}}^{\text{kin}}$ | kinematical Hilbert space (Ashtekar-Lewandowski) |
| $\mathcal{H}_{\text{diff}}$ | diffeomorphism-invariant Hilbert space |
| $\mathcal{H}_{\text{phys}}$ | physical Hilbert space (constraint solutions) |
| $\bar{\mathcal{A}}$ | space of generalized SU(2) connections |
| $\mu_o$ (or $d\mu_{\text{AL}}$) | Ashtekar-Lewandowski measure on $\bar{\mathcal{A}}$ |
| $|\Gamma, j_\ell, i_n\rangle$ | spin-network state (graph + spins + intertwiners) |
| $\hat A_S$, $\hat V_R$ | area and volume operators |
| $C$ or $\widehat{M}$ | Hamiltonian or Master constraint |
| $W[s, s']$ | spinfoam transition amplitude |
| $A_v^{(\gamma)}$, $A_f$ | EPRL vertex and face amplitudes |
| $15j$ | Wigner 15j-symbol of $SO(4)$ or $SL(2,\mathbb{C})$ |
| $K_e$, $K_{\text{ph}}$, $\mathcal{K}$ | physical intertwiner / projected-function subspace (EPR / EPRL / Rovelli-Speziale) |
| $f$ | linear "boost map" (EPR) / Dupuis-Livine map (Paper 14) from $SU(2)$ to $SL(2,\mathbb{C})$ |
| $c$, $p$ | LQC reduced connection and triad variables ($\{c, p\} = \kappa\gamma/3$) |
| $\rho_{\text{sup}}$, $\rho_{\text{crit}}$ | LQC bounce critical density $\approx 0.41 \rho_{\text{Pl}}$ |
| $\bar{\mathbb{R}}_{\text{Bohr}}$ | Bohr compactification of the real line (LQC kinematical space) |
| $M_{QG}$ | quantum-gravity scale for modified dispersion (Paper 13); $\sim 10^{18}$ GeV ($\sim 0.1 M_P$) |

### Cross-framework reference (phonon-exflation)
For substrate-first comparisons:

| LQG concept | Phonon-exflation analog | Structural / analogical? |
|:---|:---|:---|
| Discrete spectrum of $\hat A_S$ on spin networks | Discrete spectrum of $D_K$ on $(A_K, H_K, D_K)$, $A_K = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ | STRUCTURAL: gauge-invariant discrete operator spectra on finite kinematical Hilbert space, both from representation theory |
| Area gap $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ | $D_K$ spectral gap / Friedrich-Bar saturation bound | STRUCTURAL parallel; different role (Planck-scale UV cutoff vs spectral floor at $M_{KK}$ scale) |
| Immirzi parameter $\gamma$ (single dimensionless input fixed by BH entropy) | Jensen-deformation $\tau_{\text{fold}} = 0.190$ (single dimensionless parameter fixed by van Hove fold / Mach 13.75) | STRUCTURAL: single-parameter pinning of substrate; ANALOGICAL at role-level (UV-anchoring vs fold-anchoring) |
| Spinfoam sum over labelled 2-complexes with EPRL vertex | Spectral action $\text{Tr}\, f(D_K/\Lambda)$ via Seeley-DeWitt expansion | STRUCTURAL: sum over substrate configurations; ANALOGICAL at machinery-level (combinatorial 15j-symbol vs heat-kernel asymptotic) |
| EPRL asymptotic Regge action at large $j$ (semiclassical limit) | $a_2$ Seeley-DeWitt coefficient generates Einstein-Hilbert action | STRUCTURAL: both yield Einstein-Hilbert as derived effective action; ANALOGICAL at recovery mechanism |
| LQC big bounce at $\rho_{\text{sup}} \approx 0.41 \rho_{\text{Pl}}$ (quasi-equilibrium polymer-Friedmann) | Supersonic transit at $\tau_{\text{fold}} = 0.190$ (Mach 13.75, impulsive non-equilibrium GGE relic) | NON-ANALOG mechanism: equilibrium-polymer-Friedmann bounce vs impulsive supersonic acoustic-white-hole transit. Same problem (Big Bang resolution); structurally distinct dynamics |
| BH entropy $S = A/(4\ell_P^2)$ from puncture counting (Wheeler "It from Bit") | BH entropy from substrate spectral monotonicity / horizon $a_2$ Seeley-DeWitt | STRUCTURAL parallel; different intermediate machinery (Chern-Simons surface theory vs spectral action restricted to horizon) |
| LOST-Fleischhack uniqueness of holonomy-flux representation | NCG spectral-triple axioms (KO-dim=6, $[J,D_K]=0$, etc.) | STRUCTURAL: both single out a unique structure under background-independence; ANALOGICAL at axiomatic-content level |
| GFT condensate cosmology emergent Friedmann | Acoustic emergent cosmological hydrodynamics from substrate dynamics | STRUCTURAL: both treat continuum spacetime as a many-atom condensate / hydrodynamic limit |
| Modified dispersion at $M_{QG} \sim M_P$ (Paper 13 phenomenology) | Substrate is c-bounded for propagation; no in-vacuo dispersion at observable scales | NON-ANALOG: LQG (via Gambini-Pullin / DSR) predicts dispersion; phonon-exflation does not. Observational discriminator |

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 01 | Trivalent volume eigenvalue formula (Eq. 1/32) | Cited as canonical | Standard reference; no project-side verification script |
| 02 | $\gamma_0 = \ln 2/(\pi\sqrt{3})$ from BH-Hawking | Cited as canonical | Standard reference |
| 03 | Partition-function pole at $\alpha_0 = \ln 2/(4\pi\sqrt{3}\gamma\ell_P^2)$ | Cited as canonical | Standard reference |
| 04 | Volume spectrum $V_j = (\gamma l_P^2)^{3/2}\sqrt{j(j+1/2)(j+1)/27}$ | Cited as canonical | Standard reference |
| 05 | Area gap $\Delta a_S = 4\pi\gamma\ell_P^2 \cdot \sqrt{3}/2$ | Cited as canonical | Standard reference; cross-checked against Paper 17's $\Delta = 4\sqrt{3}\pi\gamma\ell_P^2$ |
| 06 | $Q_M$ closability + Friedrichs extension | Cited as canonical | Standard reference; project-side has no master-constraint computation |
| 08 | LQC bounce density $\rho_{\text{sup}} \approx 0.41 \rho_{\text{Pl}}$ | Cited as canonical | Standard reference |
| 09 | EPR vertex amplitude $A(j_f, i_e) = \sum 15j \cdot \prod f$ | Cited as canonical | Standard reference; project-side has no spinfoam computation |
| 10 | $K_{\text{ph}}$ projection to highest-$SO(3)$-irrep | Cited as canonical | Standard reference |
| 11 | EPRL area spectrum match $\text{Area} = 8\pi\hbar G\gamma\sqrt{k(k+1)}$ | Cited as canonical | Standard reference |
| 12 | Regge action $S_R^f = |B_f| \cdot |[\theta_f(H_f)]|$ from GFT | Cited as canonical | Standard reference; project-side has no GFT computation |
| 13 | Fermi-LAT GRB bound $M_{QG} > 1.3 \times 10^{18}$ GeV | Observational data | External (Fermi collaboration); not project-side computed |
| 14 | $\mathcal{K}$ space, $p(j) = \gamma\, j$ | Cited as canonical | Standard reference |
| 17 | Area gap + LQC bounce density + EPRL vertex | Synthesizes prior | Modern review; uses canonical values |
| 18 | Boundary amplitude formalism, partial observables | Conceptual / structural | Foundational synthesis; no equation requires numerical verification |

**Status note**: This corpus is consulted by the loop-quantum-gravity-theorist agent for structural reference. Numerical results in LQG (area spectra, area gap, $\gamma_0$, $\rho_{\text{sup}}$, EPRL vertex amplitudes) are NOT independently computed in the phonon-exflation project's computation scripts -- they are cited as canonical results from the literature. Cross-framework comparisons (e.g., LQG discrete spectra vs phonon-exflation $D_K$ spectrum) are conducted at the structural level, not via shared numerical scripts.
