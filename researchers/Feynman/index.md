# Feynman Paper Index

**Researcher**: Richard P. Feynman (+ Schwinger, Dyson, Wilson, Shor)
**Papers**: 14 (1948--1994)
**Primary domain**: Path integrals, QED, renormalization, quantum computing, condensed matter
**Project relevance**: Feynman's path integral formulation underpins the spectral action as a partition function; his liquid helium work provides the BEC/phonon paradigm; quantum simulation connects GPE computation to fundamental physics; renormalization (Wilson) governs the Coleman-Weinberg effective potential.

---

## Dependency Graph

```
Dirac 1933 (Lagrangian in QM)
    |
    v
[01] Path Integral (1948) -----> [05] Superfluid Helium (1954)
    |                                   |
    |                                   +---> GPE / BEC physics
    v
[02] Positrons (1949)
    |
    v
[03] QED Feynman Rules (1949) <-------> [11] Schwinger QED (1948)
    |           |                           |
    |           |                           v
    |           +---> [06] V-A / Weak (1957)
    |           |
    v           v
[04] Math QED (1950) <---------------> [12] Dyson Equivalence (1949)
    |                                       |
    |                                       v
    +---> [07] Quantum Gravity (1963)       BPHZ, 't Hooft-Veltman
    |           |
    |           +---> Faddeev-Popov (1967)
    |
    +---> [13] Wilson RG (1974) <--- Gell-Mann & Low (1954)
              |
              +---> CW potential, universality, lattice QCD

[01] Path Integral
    |
    v
[09] Simulating Physics (1982) ---> [10] Quantum Computers (1986)
                                         |
                                         v
                                    [14] Shor's Algorithm (1994)

[08] Parton Model (1969) <--- [03] Feynman Rules + Bjorken scaling
```

**Core spine**: 01 -> 02 -> 03 -> 04 (the QED arc, each paper builds on the previous)
**Two branches from 01**: statistical mechanics (05) and quantum computing (09 -> 10)
**External contributions feed into the core**: 11 (Schwinger), 12 (Dyson), 13 (Wilson)
**Isolated**: 08 (partons) uses Feynman rules but doesn't feed other papers; 14 (Shor) is downstream endpoint

---

## Topic Map

### A. QED Foundations (Papers 01, 02, 03, 04)
Path integral formulation of quantum mechanics and QED. 01 establishes the sum-over-histories, 02 resolves the positron/antiparticle problem, 03 codifies Feynman diagrams as computational algorithm, 04 derives everything from first principles and systematizes renormalization. **CRITICAL** for the spectral action and the phonon-exflation framework.

### B. Superfluidity and Phonons (Paper 05)
Microscopic derivation of superfluid helium properties via path integral. Phonon-roton spectrum from structure factor, quantized vortices, healing length. **CRITICAL** -- the direct analog of the phonon-exflation hypothesis (particles = phononic excitations of a condensate).

### C. Weak Interactions and Chirality (Paper 06)
V-A structure of weak interactions, maximal parity violation, two-component neutrino. **HIGH** -- chirality is the central constraint that KK geometry must reproduce.

### D. Quantum Gravity (Paper 07)
Perturbative quantization of GR, graviton propagator, ghost fields, non-renormalizability. **MEDIUM** -- relevant for the gravitational sector of the spectral action.

### E. Parton Model (Paper 08)
Deep inelastic scattering, structure functions, Bjorken scaling, factorization. **LOW** -- confined-phase QCD phenomenology, not directly applicable to the KK/NCG framework.

### F. Quantum Computing (Papers 09, 10, 14)
Quantum simulation motivation, gate architecture, Shor's factoring algorithm. **LOW-MEDIUM** -- sign problem constraints on classical MC, future quantum simulation tools.

### G. QED Triad Completion (Papers 11, 12)
Schwinger's operator-based QED with proper-time/heat kernel method (11) and Dyson's equivalence proof with all-orders renormalizability (12). **CRITICAL/HIGH** -- Schwinger's proper-time IS the spectral action computation; Dyson's power counting determines renormalizability.

### H. Renormalization Group (Paper 13)
Wilson's RG transformation, fixed points, universality, epsilon expansion, effective field theory. **CRITICAL** -- CW potential framework, GPE universality justification, spectral action as Wilsonian EFT.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Spectral action Tr(f(D^2/Lambda^2)) | 11, 04, 13, 01 | CRITICAL |
| Coleman-Weinberg V_eff(s) | 13, 11, 04 | CRITICAL |
| GPE simulation, phonon spectrum | 05, 01, 09 | CRITICAL |
| Gauge coupling test g_1/g_2 = e^{-2s} | 03, 12, 13 | HIGH |
| Chirality, fermion generations | 06, 12, 02 | HIGH |
| Feynman rules, SM Lagrangian test | 03, 04, 07, 12 | HIGH |
| Heat kernel, Seeley-DeWitt expansion | 11, 04 | CRITICAL |
| Renormalizability of KK effective theory | 12, 13, 07 | MEDIUM |
| CPT symmetry, Dirac propagator | 02, 03 | HIGH |
| Power counting, divergence structure | 12, 07, 04 | MEDIUM |
| Bell inequality, CHSH target | 09 | MEDIUM |
| Ward identity, gauge invariance | 03, 12, 04 | HIGH |
| Universality class arguments | 13, 05 | CRITICAL |
| Quantum simulation (future) | 09, 10, 14 | LOW |
| Parton model, QCD structure | 08, 13 | LOW |
| Vortex energy, healing length | 05 | CRITICAL |
| Effective field theory framework | 13, 11 | CRITICAL |
| Proper-time representation | 04, 11 | CRITICAL |

---

## Paper Entries

---

### Paper 01: Space-Time Approach to Non-Relativistic Quantum Mechanics

- **File**: `researchers/Feynman/01_1948_Feynman_Space_time_approach_to_nonrelativistic_QM.md`
- **arXiv**: (pre-arXiv; Rev. Mod. Phys. 20, 367, 1948)
- **Year**: 1948
- **Authors**: Feynman
- **Relevance**: CRITICAL
- **Tags**: `path-integral`, `propagator`, `action-principle`, `classical-limit`, `stationary-phase`, `sum-over-histories`, `Wick-rotation`

**Summary**: Feynman reformulates non-relativistic quantum mechanics as a sum over all possible spacetime trajectories, each weighted by exp(iS/hbar). The kernel K(b,a) = integral D[x] exp(iS[x]/hbar) is shown equivalent to the Schrodinger equation. Classical mechanics emerges from stationary phase. This is the conceptual foundation for all subsequent path integral methods.

**Key Results**:
1. K(b,a) = integral over all paths with phase exp(iS/hbar) -- the path integral postulate
2. Free particle propagator: K_0 = sqrt(m/2pi*i*hbar*T) * exp(im(x_b-x_a)^2 / 2hbar*T)
3. Composition property: K(c,a) = integral K(c,b)K(b,a) d^3x_b (completeness)
4. Schrodinger equation derived from infinitesimal-time path integral
5. Classical limit from stationary phase: delta_S = 0 gives Euler-Lagrange equations
6. Typical quantum path: continuous but nowhere differentiable, Hausdorff dimension 2
7. Harmonic oscillator: stationary phase is EXACT (action is quadratic)

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| PI-1 | Path integral kernel: K(b,a) = integral D[x] exp(iS[x]/hbar) | Core definition |
| PI-2 | Action functional: S[x(t)] = integral L(x, x_dot, t) dt | Core definition |
| PI-3 | Time-slicing: K = lim A^{-N} integral...integral exp(iS_disc/hbar) prod dx_j | Section on discretization |
| PI-4 | Normalization: A = sqrt(2*pi*i*hbar*epsilon/m) | Section on discretization |
| PI-5 | Stationary phase approximation | Semiclassical limit |
| PI-6 | Brownian scaling: <(Delta x)^2> ~ (hbar/m) * Delta_t | Path properties |

**Dependencies**:
- *Builds on*: Dirac 1933 (Lagrangian in QM)
- *Required by*: 02, 03, 04 (all QED work), 05 (stat mech via Wick rotation), 07 (quantum gravity), 09 (quantum computing motivation)

---

### Paper 02: Theory of Positrons

- **File**: `researchers/Feynman/02_1949_Feynman_Theory_of_positrons.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 76, 749, 1949)
- **Year**: 1949
- **Authors**: Feynman
- **Relevance**: HIGH
- **Tags**: `propagator`, `positron`, `antiparticle`, `CPT`, `Dirac-equation`, `pair-creation`, `vacuum-polarization`, `i-epsilon`

**Summary**: Feynman resolves the negative-energy problem of the Dirac equation by reinterpreting negative-energy solutions as positive-energy particles traveling backward in time. The Feynman propagator K_+(2,1) propagates positive-energy forward and negative-energy backward, unifying electrons and positrons into one mathematical object. Pair creation/annihilation is a worldline reversal in spacetime.

**Key Results**:
1. Feynman propagator K_+(2,1) with i*epsilon prescription: unique boundary condition for causal propagation
2. Positrons = electrons moving backward in time (Stuckelberg-Feynman interpretation)
3. Pair creation/annihilation as worldline kinks in 4D spacetime
4. Perturbative expansion K_+ = K_+^(0) + K_+^(1) + ... for external fields
5. Closed fermion loops = vacuum polarization with (-1) sign from Fermi statistics
6. CPT as viewing same worldline from opposite temporal direction

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| FP-1 | Feynman propagator (momentum): K_+(p) = i(gamma^mu p_mu + m)/(p^2 - m^2 + i*epsilon) | Core definition |
| FP-2 | Positive-energy forward propagation | Boundary conditions |
| FP-3 | Negative-energy backward propagation | Boundary conditions |
| FP-4 | Lippmann-Schwinger (4D): K_+ = K_+^(0) - ie integral K_+^(0) gamma^mu A_mu K_+ d4x | Perturbation theory |
| FP-5 | Vacuum polarization tensor: Pi^{mu nu}(q) | Loop corrections |

**Dependencies**:
- *Builds on*: 01 (path integral), Dirac 1928 (equation)
- *Required by*: 03, 04 (full QED rules)

---

### Paper 03: Space-Time Approach to Quantum Electrodynamics

- **File**: `researchers/Feynman/03_1949_Feynman_Space_time_approach_to_QED.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 76, 769, 1949)
- **Year**: 1949
- **Authors**: Feynman
- **Relevance**: HIGH
- **Tags**: `Feynman-diagrams`, `QED`, `renormalization`, `anomalous-magnetic-moment`, `Ward-identity`, `running-coupling`, `Compton-scattering`, `self-energy`

**Summary**: The central paper establishing Feynman diagrams as a computational algorithm. Codifies the complete Feynman rules for QED: external lines, internal propagators, vertices (-ie*gamma^mu), loop integrals, and combinatorial signs. Demonstrates the method through Compton scattering, Moller scattering, electron self-energy, vacuum polarization, and the vertex correction. Computes the anomalous magnetic moment a_e = alpha/(2*pi).

**Key Results**:
1. Complete QED Feynman rules: propagators, vertices, loop integration, signs
2. Compton scattering: reproduces Klein-Nishina formula from 2 tree-level diagrams
3. Moller scattering: relative minus sign from fermion exchange (Pauli principle)
4. Electron self-energy: delta_m = (3*alpha/2*pi) * m * ln(Lambda/m) -- logarithmic divergence
5. Vacuum polarization: transverse by Ward identity, gives running coupling e^2_eff(q^2)
6. Anomalous magnetic moment: a_e = F_2(0) = alpha/(2*pi) -- agrees with Schwinger and experiment
7. Ward identity: dSigma/dp^mu = Lambda^mu(p,p) -- gauge invariance constraint
8. Charge screening: e^2_eff ~ e^2(1 + alpha/(3*pi) * ln(q^2/m^2))

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| QED-1 | Electron propagator: i/(p_slash - m + i*epsilon) | Feynman rules |
| QED-2 | Photon propagator (Feynman gauge): -i*g_{mu nu}/(q^2 + i*epsilon) | Feynman rules |
| QED-3 | Vertex factor: -ie*gamma^mu | Feynman rules |
| QED-4 | Self-energy: Sigma(p) integral expression | Loop corrections |
| QED-5 | Anomalous magnetic moment: a_e = alpha/(2*pi) = 0.001162 | Vertex correction |
| QED-6 | Vacuum polarization (running): e^2_eff(q^2) = e^2/(1 - Pi(q^2)) | Charge renormalization |
| QED-7 | Klein-Nishina cross section | Compton scattering |
| QED-8 | Ward identity: dSigma/dp^mu = Lambda^mu(p,p) | Gauge invariance |

**Dependencies**:
- *Builds on*: 01, 02
- *Required by*: 04 (systematic derivation), 06 (weak processes), 08 (partonic cross sections), 12 (Dyson equivalence proof)
- *Parallel*: 11 (Schwinger's independent derivation)

---

### Paper 04: Mathematical Formulation of the Quantum Theory of Electromagnetic Interaction

- **File**: `researchers/Feynman/04_1950_Feynman_Mathematical_formulation_of_QED.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 80, 440, 1950)
- **Year**: 1950
- **Authors**: Feynman
- **Relevance**: CRITICAL
- **Tags**: `Feynman-parameters`, `renormalization`, `proper-time`, `heat-kernel`, `Lamb-shift`, `systematic-QFT`, `worldline`, `Wick-rotation`

**Summary**: Feynman derives all QED rules from first principles via the path integral, closing the logical gap in his earlier papers. Introduces Feynman parametrization for loop integrals, presents the systematic renormalization algorithm (regularize, compute, identify divergences, renormalize, remove regulator), and completes the Lamb shift calculation. The proper-time representation connects to heat kernel methods.

**Key Results**:
1. Path integral for charged scalar particle: K = integral D[x] exp(i*integral [m/2 * x_dot^2 + e*x_dot^mu A_mu] ds)
2. Dirac propagator via proper-time: S_F(p) = (p_slash + m) integral_0^inf ds exp(-is(p^2-m^2+i*eps))
3. Photon field integrated out: effective non-local action with J^mu D_F J_mu coupling
4. Feynman parametrization: 1/(AB) = integral_0^1 dx / [Ax + B(1-x)]^2
5. Systematic renormalization: only delta_m and Z_3 are independent (Ward: Z_1 = Z_2)
6. Anomalous magnetic moment: a_e = alpha/(2*pi) derived from first principles
7. Lamb shift: 1052 MHz + corrections -> ~1057 MHz, agrees with experiment
8. Proper-time method: connects to heat kernel, Schwinger formalism, worldline QFT

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| MF-1 | Proper-time propagator: 1/(p^2-m^2+i*eps) = -i integral ds exp(is(p^2-m^2+i*eps)) | Proper-time formalism |
| MF-2 | Feynman parameter (2-body): 1/(AB) = integral dx/[Ax+B(1-x)]^2 | Loop integrals |
| MF-3 | Feynman parameter (n-body): (n-1)! integral with delta-function constraint | Loop integrals |
| MF-4 | Renormalization constants: m_0, e_0, psi_0 relations | Renormalization |
| MF-5 | Lamb shift: Delta E(2S-2P) ~ 1052 MHz | Precision test |
| MF-6 | Effective action (photon integrated out) | Effective theory |

**Dependencies**:
- *Builds on*: 01, 02, 03
- *Required by*: 07 (gravity Feynman rules), 13 (Wilson RG extends this)
- *Parallel*: 11 (Schwinger), 12 (Dyson equivalence)

---

### Paper 05: Atomic Theory of the Two-Fluid Model of Liquid Helium

- **File**: `researchers/Feynman/05_1954_Feynman_Atomic_theory_of_two_fluid_model_liquid_helium.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 94, 262, 1954)
- **Year**: 1954
- **Authors**: Feynman
- **Relevance**: CRITICAL
- **Tags**: `superfluidity`, `phonon-roton`, `path-integral`, `structure-factor`, `quantized-vortices`, `healing-length`, `BEC`, `Landau-criterion`, `GPE`

**Summary**: Feynman derives the macroscopic properties of superfluid helium-4 from microscopic physics via the path integral. Permutation cycles of atomic worldlines in imaginary time explain the lambda transition. The excitation spectrum epsilon(k) = hbar^2 k^2/(2mS(k)) is derived variationally from the structure factor S(k), producing the phonon-roton spectrum without adjustable parameters. Quantized vortices with circulation h/m are predicted.

**Key Results**:
1. Lambda transition from macroscopic permutation cycles: T_lambda ~ 2pi*hbar^2/(mk_B*d^2) ~ 3.1 K (exp: 2.17 K)
2. Phonon-roton spectrum: epsilon(k) = hbar^2 k^2/(2mS(k)) -- parameter-free from measured S(k)
3. Phonon limit: epsilon -> hbar*c_s*k for small k (from compressibility sum rule)
4. Roton minimum: Delta/k_B ~ 11.5 K variational (exp: 8.65 K), improved to 9.6 K with backflow
5. Landau critical velocity: v_c = min_p epsilon(p)/p ~ 58 m/s (at roton minimum)
6. Quantized circulation: oint v_s . dl = (h/m)*n
7. Superfluid velocity: v_s = (hbar/m) grad(theta) -- irrotational
8. Vortex energy: E/L = pi*rho_s*(hbar^2/m^2)*ln(R/xi)

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| He-1 | Partition function (bosons): Z = (1/N!) sum_P integral prod dr_i rho(R; R_P; beta) | Statistical mechanics |
| He-2 | Excitation spectrum: epsilon(k) = hbar^2 k^2 / (2m S(k)) | Main result |
| He-3 | Structure factor phonon limit: S(k) -> hbar k/(2mc_s) as k->0 | Phonon regime |
| He-4 | Landau criterion: v_c = min_p [epsilon(p)/p] | Critical velocity |
| He-5 | Quantized circulation: oint v_s . dl = (h/m)n | Vortex quantization |
| He-6 | Vortex energy per length: E/L = pi rho_s (hbar/m)^2 ln(R/xi) | Vortex energetics |

**Dependencies**:
- *Builds on*: 01 (path integral applied to statistical mechanics via Wick rotation)
- *Required by*: GPE/BEC simulation physics (phonon-exflation-sim/)

---

### Paper 06: Theory of the Fermi Interaction

- **File**: `researchers/Feynman/06_1957_Feynman_Gell_Mann_Theory_of_Fermi_interaction.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 109, 193, 1958)
- **Year**: 1957/1958
- **Authors**: Feynman, Gell-Mann
- **Relevance**: HIGH
- **Tags**: `V-A`, `chirality`, `parity-violation`, `weak-interaction`, `CVC`, `neutrino`, `electroweak`, `Standard-Model-structure`

**Summary**: Feynman and Gell-Mann propose the V-A (vector minus axial-vector) structure for weak interactions. The weak current J^mu = psi_bar gamma^mu (1-gamma^5) psi couples only to left-handed fermions, giving maximal parity violation. The universal Fermi interaction H = G_F/sqrt(2) J^mu J_mu_dagger unifies all weak processes. The two-component neutrino and CVC hypothesis are established.

**Key Results**:
1. V-A current: J^mu = psi_bar gamma^mu (1-gamma^5) psi -- only left-handed fermions
2. Universal weak Hamiltonian: H = (G_F/sqrt(2)) J^mu J_mu_dagger
3. Maximal parity violation: (1-gamma^5) projects out right-handed components entirely
4. Two-component neutrino: nu_L = (1/2)(1-gamma^5)nu, helicity h = -1
5. Pion decay ratio: Gamma(pi->e nu)/Gamma(pi->mu nu) ~ 1.28e-4 confirmed
6. Michel parameter rho = 3/4 for muon decay
7. CVC: vector weak current = isospin current, g_V = 1 exact
8. Precursor to electroweak theory: G_F/sqrt(2) = g^2/(8M_W^2)

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| VA-1 | V-A current: J^mu = psi_bar gamma^mu (1-gamma^5) psi | Core structure |
| VA-2 | Weak Hamiltonian: H = (G_F/sqrt(2)) J^mu J_mu_dagger | Universal coupling |
| VA-3 | Left-handed projection: nu_L = (1/2)(1-gamma^5) nu | Chirality |
| VA-4 | Pion decay ratio | Precision test |
| VA-5 | Muon decay spectrum | Angular distribution |
| VA-6 | G_F to W mass: G_F/sqrt(2) = g^2/(8M_W^2) | Electroweak connection |

**Dependencies**:
- *Builds on*: 03 (Feynman rules applied to weak processes)
- *Required by*: Electroweak theory (Glashow-Weinberg-Salam)
- *Parallel*: Marshak-Sudarshan (independent V-A discovery)

---

### Paper 07: Quantum Theory of Gravitation

- **File**: `researchers/Feynman/07_1963_Feynman_Quantum_theory_of_gravitation.md`
- **arXiv**: (pre-arXiv; Acta Physica Polonica 24, 697, 1963)
- **Year**: 1963
- **Authors**: Feynman
- **Relevance**: MEDIUM
- **Tags**: `quantum-gravity`, `graviton`, `ghost-fields`, `Faddeev-Popov`, `non-renormalizability`, `power-counting`, `effective-field-theory`, `spin-2`

**Summary**: Feynman applies QFT perturbation theory to general relativity, treating gravity as a spin-2 field h_{mu nu} on flat Minkowski background. Derives the graviton propagator, gravitational Feynman rules, and discovers ghost fields needed for unitarity in loop calculations. One-loop divergences are analyzed. The paper anticipates non-renormalizability and the Faddeev-Popov procedure.

**Key Results**:
1. Graviton propagator: D_{mu nu; alpha beta}(k) with standard tensor structure
2. Graviton = massless spin-2, 2 physical DOF (helicity +/-2)
3. Coupling to matter: L_int = -(kappa/2) h_{mu nu} T^{mu nu}, kappa = sqrt(32 pi G)
4. Tree-level exchange -> Newton's law: V(r) = -Gm_1 m_2/r
5. GHOST FIELDS DISCOVERED: fictitious particles needed in loops to maintain unitarity
6. Power counting: superficial divergence D = 2 + 2L for L loops
7. One-loop pure gravity: divergences vanish on-shell (Gauss-Bonnet accident)
8. Non-renormalizability at two loops

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| QG-1 | Metric expansion: g_{mu nu} = eta_{mu nu} + kappa h_{mu nu} | Weak-field limit |
| QG-2 | Graviton propagator | Feynman rules |
| QG-3 | Gauge transformation: h -> h + d_mu xi_nu + d_nu xi_mu | Gauge symmetry |
| QG-4 | Matter coupling: L_int = -(kappa/2) h_{mu nu} T^{mu nu} | Interaction |
| QG-5 | Power counting: D_div = 2 + 2L | Loop divergences |
| QG-6 | One-loop on-shell divergences | Gauss-Bonnet |
| QG-7 | Path integral with ghosts | Unitarity |

**Dependencies**:
- *Builds on*: 01, 03 (path integral + Feynman rules extended to spin-2)
- *Required by*: Faddeev-Popov (1967), 't Hooft-Veltman (1974)

---

### Paper 08: Very High-Energy Collisions of Hadrons

- **File**: `researchers/Feynman/08_1969_Feynman_Very_high_energy_collisions_of_hadrons.md`
- **arXiv**: (pre-arXiv; Phys. Rev. Lett. 23, 1415, 1969)
- **Year**: 1969
- **Authors**: Feynman
- **Relevance**: LOW
- **Tags**: `parton-model`, `deep-inelastic-scattering`, `Bjorken-scaling`, `QCD`, `structure-functions`, `factorization`

**Summary**: Feynman proposes the parton model for deep inelastic scattering. In the infinite-momentum frame, hadrons are collections of point-like partons carrying momentum fraction x. Structure functions F_1(x), F_2(x) are sums over parton distributions weighted by charge-squared. Bjorken scaling follows from partons being point-like. The momentum sum rule reveals that gluons carry ~50% of the proton's momentum.

**Key Results**:
1. F_2(x) = sum_i e_i^2 x f_i(x) -- structure function from parton distributions
2. Callan-Gross relation F_2 = 2xF_1 -- confirms spin-1/2 partons
3. Bjorken variable x = Q^2/(2M*nu) = momentum fraction
4. Momentum sum rule: quarks carry ~50%, gluons ~50%
5. Factorization: sigma = sum integral f_i f_j sigma_hat
6. DGLAP evolution: d f/d ln Q^2 = (alpha_s/2pi) P * f

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| PM-1 | Structure function: F_2(x) = sum_i e_i^2 x f_i(x) | Main result |
| PM-2 | Callan-Gross: F_2 = 2x F_1 | Spin-1/2 test |
| PM-3 | Bjorken x: x = Q^2/(2M nu) | Kinematic variable |
| PM-4 | Momentum sum rule | Conservation law |
| PM-5 | Factorization theorem | Cross section decomposition |
| PM-6 | DGLAP evolution | Scale dependence |

**Dependencies**:
- *Builds on*: 03 (Feynman rules for computing partonic cross sections)
- *Required by*: QCD (asymptotic freedom connects partons to quarks)

---

### Paper 09: Simulating Physics with Computers

- **File**: `researchers/Feynman/09_1982_Feynman_Simulating_physics_with_computers.md`
- **arXiv**: (pre-arXiv; Int. J. Theor. Phys. 21, 467, 1982)
- **Year**: 1982
- **Authors**: Feynman
- **Relevance**: MEDIUM
- **Tags**: `quantum-computing`, `exponential-blowup`, `sign-problem`, `Bell-inequality`, `CHSH`, `Trotter`, `simulation`

**Summary**: Feynman argues that quantum systems cannot be efficiently simulated on classical computers due to the exponential growth of Hilbert space with particle number. Classical Monte Carlo fails for quantum systems due to the sign problem. Bell inequality violations prove that local classical hidden variable simulations cannot reproduce quantum correlations. The solution: build quantum computers that are themselves quantum mechanical.

**Key Results**:
1. Exponential explosion: n qubits require 2^n amplitudes
2. Sign problem: quantum path integral weights are complex, preventing positive-definite MC sampling
3. Bell inequalities: CHSH <= 2 (classical), 2*sqrt(2) (quantum)
4. Quantum computer proposal: simulate quantum systems with quantum hardware
5. Trotter decomposition: e^{-iHt} ~ (prod_k e^{-iH_k*t/r})^r + O(t^2/r)
6. "Nature isn't classical, dammit"

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| QC-1 | Hilbert space dimension: dim = 2^n for n qubits | Exponential blowup |
| QC-2 | Time evolution: psi(t) = e^{-iHt/hbar} psi(0) | Unitary dynamics |
| QC-3 | CHSH inequality: \|S\| <= 2 | Bell test |
| QC-4 | Trotter decomposition | Simulation algorithm |
| QC-5 | Interference: P(A or B) != \|c_A\|^2 + \|c_B\|^2 | Quantum signature |

**Dependencies**:
- *Builds on*: 01 (path integral), Bell 1964 (inequalities)
- *Required by*: 10 (quantum gates), 14 (Shor's algorithm)

---

### Paper 10: Quantum Mechanical Computers

- **File**: `researchers/Feynman/10_1986_Feynman_Quantum_mechanical_computers.md`
- **arXiv**: (pre-arXiv; Found. Phys. 16, 507, 1986)
- **Year**: 1986
- **Authors**: Feynman
- **Relevance**: LOW
- **Tags**: `quantum-gates`, `CNOT`, `universality`, `quantum-parallelism`, `Trotter`, `decoherence`, `error-propagation`

**Summary**: Feynman develops concrete quantum computing architecture. Defines qubits, quantum gates (X, H, S, CNOT), and proves universality: any n-qubit unitary decomposes into single-qubit rotations + CNOT gates. Quantum parallelism: one application of U_f evaluates f on all 2^n inputs simultaneously. Hamiltonian simulation made concrete with gate-count estimates.

**Key Results**:
1. Qubit: |psi> = alpha|0> + beta|1>, |alpha|^2+|beta|^2 = 1
2. Universal gate set: {single-qubit rotations, CNOT} suffices for any unitary
3. CNOT creates entanglement: CNOT(H|0> x |0>) = (|00>+|11>)/sqrt(2)
4. Quantum parallelism: evaluates f on all inputs at once
5. Trotter gate count: N = O(m^2 t^2/epsilon) first order
6. Error propagation: total error ~ d*epsilon for depth-d circuit

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| QMC-1 | Qubit state: psi = alpha\|0> + beta\|1> | Definition |
| QMC-2 | CNOT gate: \|0><0\| x I + \|1><1\| x X | Universal gate |
| QMC-3 | Hadamard: H = (1/sqrt(2))[[1,1],[1,-1]] | Single-qubit gate |
| QMC-4 | Quantum parallelism: U_f sum_x \|x>\|0> = sum_x \|x>\|f(x)> | Superposition |
| QMC-5 | Trotter gate count: N_gates = O(m^2 t^2 / epsilon) | Complexity |
| QMC-6 | Error bound: P_error ~ d * epsilon | Error propagation |

**Dependencies**:
- *Builds on*: 09 (motivation), Deutsch 1985 (quantum Turing machine)
- *Required by*: 14 (Shor uses these gates)

---

### Paper 11: Quantum Electrodynamics. I. A Covariant Formulation (Schwinger)

- **File**: `researchers/Feynman/11_1948_Schwinger_Quantum_electrodynamics_I.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 74, 1439, 1948)
- **Year**: 1948
- **Authors**: Schwinger
- **Relevance**: CRITICAL
- **Tags**: `proper-time`, `effective-action`, `heat-kernel`, `Schwinger-pair-production`, `Euler-Heisenberg`, `renormalization`, `spectral-action`

**Summary**: Schwinger develops the operator-based, covariant formulation of QED using the interaction representation. Introduces the proper-time method for propagators, derives the anomalous magnetic moment a_e = alpha/(2*pi), computes the Euler-Heisenberg effective Lagrangian for vacuum polarization in constant fields, and establishes systematic renormalization with counterterms. The effective action Gamma[A] = -i*hbar*Tr ln(D_slash + m) becomes a central object of modern QFT.

**Key Results**:
1. Tomonaga-Schwinger equation for covariant interaction picture
2. Proper-time representation: 1/(p^2-m^2+i*eps) = -i integral ds exp(is(p^2-m^2+i*eps))
3. Anomalous magnetic moment: a_e = alpha/(2*pi) (independent of Feynman)
4. Euler-Heisenberg Lagrangian: L_EH = -(1/4)F^2 + (2*alpha^2/45*m^4)[(FF)^2 + (7/4)(F*F_dual)^2]
5. Schwinger pair production: Gamma ~ (alpha*E^2/pi^2) exp(-pi*E_c/E)
6. Effective action: Gamma^(1)[A] = i*hbar integral ds/s * exp(-is*m^2) * Tr exp(is*(D_slash)^2)
7. Ward identity: Z_1 = Z_2

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| SW-1 | Tomonaga-Schwinger equation | Covariant QFT |
| SW-2 | Proper-time propagator: 1/(p^2-m^2) = -i integral ds exp(is(p^2-m^2)) | Heat kernel |
| SW-3 | Effective action (1-loop): Gamma = i*hbar integral ds/s exp(-ism^2) Tr exp(is(D_slash)^2) | Spectral action |
| SW-4 | Euler-Heisenberg effective Lagrangian | Vacuum polarization |
| SW-5 | Schwinger pair production rate | Strong-field QED |
| SW-6 | Anomalous magnetic moment: a_e = alpha/(2pi) | Precision test |

**Dependencies**:
- *Builds on*: Dirac, Tomonaga (interaction picture)
- *Parallel*: 01-04 (Feynman's independent approach)
- *Required by*: 12 (Dyson equivalence proof)

---

### Paper 12: The Radiation Theories of Tomonaga, Schwinger, and Feynman (Dyson)

- **File**: `researchers/Feynman/12_1949_Dyson_Radiation_theories_of_Tomonaga_Schwinger_Feynman.md`
- **arXiv**: (pre-arXiv; Phys. Rev. 75, 486, 1949)
- **Year**: 1949
- **Authors**: Dyson
- **Relevance**: HIGH
- **Tags**: `equivalence-proof`, `Wick-theorem`, `power-counting`, `renormalizability`, `Ward-identity`, `linked-cluster`, `BPHZ`, `unitarity`

**Summary**: Dyson proves the mathematical equivalence of all three QED formulations. Shows that Wick's theorem connects time-ordered operator products to Feynman propagators/diagrams. Establishes renormalization to ALL orders via power-counting: D = 4 - (3/2)E_e - E_gamma (only 3 primitive divergences). Proves the linked-cluster theorem and demonstrates unitarity order by order.

**Key Results**:
1. Equivalence of Tomonaga/Schwinger/Feynman: same S-matrix to all orders
2. Wick's theorem: T[phi_1...phi_n] = :phi_1...phi_n: + all contractions
3. Contractions = Feynman propagators
4. Power counting: D = 4 - (3/2)E_e - E_gamma (only 3 divergent structures)
5. Renormalizability to all orders: mass, charge, wave-function renormalization suffice
6. Linked-cluster theorem: S = exp(sum connected diagrams)
7. Ward identity from gauge invariance
8. Unitarity: optical theorem

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| DY-1 | S-matrix expansion: S = sum (-i)^n/n! integral T[H_I...H_I] d4x_1...d4x_n | Perturbation theory |
| DY-2 | Power counting (QED): D = 4 - (3/2)E_e - E_gamma | Renormalizability |
| DY-3 | Ward identity: q_mu Gamma^mu = S_F^{-1}(p+q) - S_F^{-1}(p) | Gauge invariance |
| DY-4 | Linked-cluster: S = exp(sum_connected iM_c) | Vacuum diagrams |
| DY-5 | Optical theorem: Im(M_ii) = 1/2 sum_f \|M_fi\|^2 | Unitarity |

**Dependencies**:
- *Builds on*: 01-04 (Feynman), 11 (Schwinger), Tomonaga
- *Required by*: BPHZ theorem, 't Hooft-Veltman, Standard Model

---

### Paper 13: The Renormalization Group and Critical Phenomena (Wilson)

- **File**: `researchers/Feynman/13_1974_Wilson_Renormalization_group_and_critical_phenomena.md`
- **arXiv**: (pre-arXiv; Rev. Mod. Phys. 55, 583, 1983 (Nobel Lecture); key papers: Phys. Rev. B 4, 3174, 1971; Phys. Rev. Lett. 28, 240, 1972)
- **Year**: 1971--1974
- **Authors**: Wilson
- **Relevance**: CRITICAL
- **Tags**: `renormalization-group`, `universality`, `fixed-point`, `critical-exponents`, `epsilon-expansion`, `effective-field-theory`, `Wilson-Fisher`, `asymptotic-freedom`, `lattice-gauge-theory`, `Coleman-Weinberg`

**Summary**: Wilson develops the RG as a transformation in Hamiltonian space. Fixed points correspond to critical points (scale invariance). Universality classes = basins of attraction. Relevant/irrelevant/marginal operators classified by RG eigenvalues. The epsilon expansion computes critical exponents perturbatively around d=4. Deep connection: QFT renormalization = integrating out short-distance modes. Asymptotic freedom of QCD explained. Lattice gauge theory proposed.

**Key Results**:
1. RG transformation: H -> H' = R_b[H] (integrate out high-k modes, rescale)
2. Fixed point: R_b[H*] = H* (scale invariance = critical point)
3. Eigenvalue classification: relevant (y>0), irrelevant (y<0), marginal (y=0)
4. Critical exponents from RG eigenvalues: nu = 1/y_t
5. Wilson-Fisher fixed point: u* = 2*epsilon/(3*K_4^{-1}) at d = 4-epsilon
6. Epsilon expansion: nu = 1/2 + epsilon/12 + 7*epsilon^2/162 + O(epsilon^3)
7. QFT = effective theory valid below cutoff Lambda
8. QCD beta function: beta(g) = -(g^3/16pi^2)(11-2N_f/3) (asymptotic freedom)
9. Lattice gauge theory: non-perturbative QCD on discrete spacetime

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| WI-1 | RG transformation: H' = R_b[H] | Core definition |
| WI-2 | Fixed point condition: R_b[H*] = H* | Scale invariance |
| WI-3 | Linearized RG: delta g_i' = b^{y_i} delta g_i | Operator classification |
| WI-4 | Critical exponent: nu = 1/y_t | Observable prediction |
| WI-5 | Wilson-Fisher fixed point | d = 4-epsilon |
| WI-6 | Epsilon expansion for nu | Perturbative exponents |
| WI-7 | QCD beta function: beta(g) = -(g^3/16pi^2)(11-2N_f/3) | Asymptotic freedom |
| WI-8 | phi^4 action: H = integral [1/2(grad phi)^2 + r/2 phi^2 + u/4! phi^4] | Ising universality |

**Dependencies**:
- *Builds on*: 03-04 (Feynman renormalization), Gell-Mann & Low (1954), Kadanoff block spins (1966)
- *Required by*: Asymptotic safety, lattice QCD, conformal bootstrap

---

### Paper 14: Algorithms for Quantum Computation: Discrete Logarithms and Factoring (Shor)

- **File**: `researchers/Feynman/14_1994_Shor_Algorithms_for_quantum_computation.md`
- **arXiv**: quant-ph/9508027 (1995 preprint; original FOCS 1994)
- **Year**: 1994
- **Authors**: Shor
- **Relevance**: LOW
- **Tags**: `quantum-algorithm`, `factoring`, `QFT`, `period-finding`, `RSA`, `BQP`, `continued-fractions`

**Summary**: Shor gives a polynomial-time quantum algorithm for integer factoring and discrete logarithms. Reduces factoring to period-finding of f(x) = a^x mod N. Uses quantum Fourier transform (O(n^2) gates on n qubits) to detect periodicity in superposition. Total complexity: O(n^2 log n log log n) quantum gates with O(n) qubits. Breaks RSA cryptography. Direct realization of Feynman's 1982 vision.

**Key Results**:
1. Factoring -> period finding: r = period of a^x mod N
2. Quantum Fourier transform: O(n^2) gates
3. Period-finding algorithm: Hadamard + modular exponentiation + QFT + measurement
4. Complexity: O(n^2 log n log log n) gates, O(n) qubits
5. Continued fraction extraction for period recovery
6. RSA (2048-bit) breakable with ~4000 logical qubits

**Key Equations**:

| Label | Description | Location |
|:---|:---|:---|
| SH-1 | QFT: QFT\|j> = (1/sqrt(2^n)) sum_k exp(2pi ijk/2^n)\|k> | Core subroutine |
| SH-2 | Period condition: a^r = 1 mod N | Number theory |
| SH-3 | Factoring reduction: gcd(a^{r/2} - 1, N) = non-trivial factor | Algorithm |
| SH-4 | Measurement probability distribution | Interference pattern |
| SH-5 | Gate complexity: O(n^2 log n log log n) | Polynomial bound |
| SH-6 | QFT circuit depth: O(n^2) gates | Implementation |

**Dependencies**:
- *Builds on*: 09 (Feynman's QC motivation), 10 (quantum gates), Simon 1994 (period finding precursor)
- *Required by*: Post-quantum cryptography, quantum error correction

---

## Cross-Paper Equation Concordance

| Equation / Object | Appears In | Notes |
|:---|:---|:---|
| Path integral K = integral D[x] exp(iS/hbar) | 01, 04, 05, 07, 09 | Foundation of entire collection |
| Proper-time 1/(p^2-m^2) = -i integral ds exp(...) | 04 (MF-1), 11 (SW-2) | Feynman and Schwinger versions; both = heat kernel |
| Anomalous magnetic moment a_e = alpha/(2pi) | 03 (QED-5), 04, 11 (SW-6) | Three independent derivations, same result |
| Ward identity | 03 (QED-8), 04, 11, 12 (DY-3) | Gauge invariance constraint across all formulations |
| Feynman propagator | 02 (FP-1), 03 (QED-1,2), 07 (QG-2), 11 | Spin-0, spin-1/2, spin-1, spin-2 versions |
| Power counting formula | 04, 07 (QG-5), 12 (DY-2) | QED: D=4-3/2 E_e-E_gamma; Gravity: D=2+2L |
| Effective action / Lagrangian | 04 (MF-6), 11 (SW-3,4), 13 | Schwinger 1-loop -> CW -> Wilsonian EFT |
| Quantized circulation | 05 (He-5) | oint v_s . dl = (h/m)n -- unique to condensed matter |
| CHSH inequality | 09 (QC-3) | \|S\| <= 2 (classical), 2*sqrt(2) (quantum) |
| Trotter decomposition | 09 (QC-4), 10 (QMC-5) | Quantum simulation algorithm |
| RG beta function | 13 (WI-7) | QCD: beta = -(g^3/16pi^2)(11-2N_f/3) |

---

## Notation Conventions

| Symbol | Meaning | Used In |
|:---|:---|:---|
| K(b,a), K_+ | Propagator / kernel | 01, 02, 03, 04 |
| S[x], S_eff | Action functional / effective action | 01, 04, 11 |
| D_slash = gamma^mu D_mu | Dirac operator (slashed) | 02, 03, 04, 11 |
| alpha = e^2/(4pi) ~ 1/137 | Fine structure constant | 03, 04, 11 |
| G_F | Fermi coupling constant | 06 |
| kappa = sqrt(32pi G) | Gravitational coupling | 07 |
| S(k) | Structure factor | 05 |
| xi | Healing length (condensed matter) / gauge parameter (QFT) | 05 / 07 |
| epsilon | d = 4-epsilon (Wilson) / infinitesimal time slice (Feynman) / i*epsilon prescription | Context-dependent |
| Lambda | UV cutoff / RG scale | 04, 11, 13 |
| Gamma[A] | Effective action (1PI) | 11, 13 |

---

## Computational Verification Status

| Paper | Equation | Verified? | Script | Session |
|:---|:---|:---|:---|:---|
| 01 (PI) | Path integral = spectral action identity | Conceptual (used throughout) | tier1_spectral_action.py | 14 |
| 04 (MF-1) | Proper-time = heat kernel | Used in Seeley-DeWitt expansion | tier1_spectral_action.py | 14 |
| 05 (He-2) | epsilon(k) phonon spectrum | GPE simulation reproduces | phonon-exflation-sim/ | 3 |
| 05 (He-5,6) | Quantized vortices, healing length | D/H = 2.737e-5 (8% match) | phonon-exflation-sim/ | 3 |
| 11 (SW-3) | 1-loop effective action | Spectral action r=0.96 with V_eff | tier1_spectral_action.py | 14 |
| 13 (WI) | Coleman-Weinberg mechanism | CW s_0 ~ 0.3-0.6 (soft fail) | tier1_coleman_weinberg.py | 17a |
| 03 (QED-6) | Running coupling | g_1/g_2 = e^{-2s} derived | gauge_coupling_derivation.py | 17a |

---

## Relevance Summary

| Rating | Count | Papers |
|:---|:---|:---|
| CRITICAL | 5 | 01, 04, 05, 11, 13 |
| HIGH | 4 | 02, 03, 06, 12 |
| MEDIUM | 2 | 07, 09 |
| LOW | 3 | 08, 10, 14 |

**Citation layers for the project**:
- **Layer 1** (must cite): 01, 04, 05, 11, 13 -- path integral, heat kernel, phonons, effective action, RG
- **Layer 2** (should cite): 02, 03, 06, 12 -- propagator, Feynman rules, chirality, renormalizability
- **Layer 3** (context only): 07, 08, 09, 10, 14 -- gravity, partons, quantum computing
