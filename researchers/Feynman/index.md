# Feynman Paper Index

**Researcher**: Richard Feynman (+ related: Schwinger, Dyson, Wilson, Gell-Mann, Parker, Chamseddine-Connes, Vassilevich, van Nuland-van Suijlekom, Hong, Dukelsky-Pittel-Sierra, Vidmar-Rigol, Claeys, Franchino-Vinas et al., Kaushal-Singh, Garcia-Consuegra-Maleknejad, D'Angelo, Pawlowski-Reichert-Wessely, Shor, Beggs-Smith)
**Papers**: 30 (1948-2026)
**Primary domain**: Path-integral QED, renormalization, spectral action / heat kernel machinery, cosmological particle creation, Richardson-Gaudin integrability, Lorentzian quantum gravity
**Project relevance**: Supplies the computational backbone for every computation artifact that evaluates the Chamseddine-Connes spectral action Tr f(D_K/Lambda) on Jensen-deformed SU(3). Papers 15-19 are the heat-kernel / Seeley-DeWitt toolchain from which a_0 (CC moment), a_2 (Einstein-Hilbert), a_4 (Yang-Mills + Higgs) are extracted; Papers 20-26 ground the Parker-Schwinger pair production calculations at the van Hove fold; Papers 27-30 underwrite the S38 paradigm shift to integrability-protected GGE relic (the Ordered Veil); Papers 31-32 provide Lorentzian-QFT benchmarks against which the emergent graviton of the spectral triple must be compared.

---

## Dependency Graph

```
QED FOUNDATIONS (1948-1950)
  01 (Path integral, non-rel QM) --> 02 (Positrons / K_+)
  01 --> 03 (Space-time QED + diagrams)
  01 --> 04 (Math formulation; oscillator elimination; proper-time KG)
  05 (Schwinger QED-I covariant) --> 06 (Dyson unification)
  03 --> 06
  02 --> 06
  04 --> 15 [proper-time kernel root of heat kernel]

BROAD PHYSICS + RG (1954-1974)
  10 (Feynman, two-fluid He-II) --> 07 [collective modes, universality]
  10 --> "Feynman-Cohen backflow" (not in index)
  08 (Feynman-Gell-Mann, V-A Fermi)  [independent of path integral chain]
  09 (Feynman, quantum gravity) --> 31 [asymptotic safety picks up the thread]
  09 --> 32 [graviton spectral function]
  11 (Feynman, parton model) --> "DGLAP" (not in index)
  07 (Wilson-Kogut, RG + epsilon) --> 15 [power counting in heat kernel]
  07 --> 16 [RG running of SM couplings under spectral-action GUT-boundary]

QUANTUM COMPUTATION (1982-1996)
  12 (Feynman, simulating physics) --> 13 (Feynman, QM computers)
  12 --> 14 (Shor, polynomial-time factoring)
  13 --> 14

HEAT-KERNEL + SPECTRAL-ACTION TOOLCHAIN (1996-2022) -- CRITICAL
  04 [proper-time root] --> 15 (Vassilevich manual)
  15 --> 16 (Chamseddine-Connes spectral action principle)
  15 --> 17 (van Nuland-van Suijlekom one-loop)
  15 --> 19 (Hong, heat kernel on compact Lie group)
  16 --> 17 [perturbative quantization of spectral action]
  16 --> 18 (Beggs-Smith, NC complex differential geometry)
  19 --> 16 [SU(3) bi-invariant heat kernel enters a_2]

COSMOLOGICAL PARTICLE CREATION + SCHWINGER (1966-2026)
  04 [proper-time] --> 20 (Parker thesis, KG + Dirac in FLRW)
  20 --> 21 (Parker + Navarro-Salas 50-year review)
  20 --> 24 (conformally flat gravitational Schwinger analogues)
  20 --> 25 (backreaction Schwinger dS)
  20 --> 26 (stochastic Schwinger)
  15 --> 24 [resummed heat kernel for pair creation]
  24 <--> 25 [complementary: closed-form vs backreaction-dynamical]
  24 <--> 26 [complementary: coherent vs stochastic drivers]

RICHARDSON-GAUDIN + GGE (2004-2019)
  27 (Dukelsky-Pittel-Sierra, R-G review) --> 28 (Vidmar-Rigol, GGE review)
  27 --> 29 (Claeys thesis, R-G + broken integrability)
  29 --> 30 (Claeys quench dynamics -- filename mismatch noted)
  28 <--> 29 [integrability conserved charges -> GGE relic]

LORENTZIAN QUANTUM GRAVITY (2023-2025)
  09 [Feynman QG seed] --> 31 (D'Angelo, asymptotic safety Lorentzian)
  31 --> 32 (Pawlowski-Reichert-Wessely, graviton spectral function)
  16 <--> 31 [adversarial UV completions: spectral action vs AS]
  16 <--> 32

CROSS-THEME BRIDGES
  01, 04 --[path integral]--> 16 [spectral action as sum over metrics]
  01, 04 --[path integral]--> 20 [KG in FLRW; Bogoliubov]
  06 --[diagrammatics]--> 17 [one-loop spectral action via cyclic cocycles]
  07 --[RG]--> 31 [functional RG in Lorentzian QG]
  10 --[phonons / collective modes]--> 27-30 [pairing, R-G, GGE]
  12, 13 --[quantum simulation]--> 28 [integrable systems as quantum simulators]
```

## Topic Map

### QED Foundations (path integrals + diagrams + renormalization)
Papers: 01, 02, 03, 04, 05, 06
Feynman's 1948 path integral formulation of non-relativistic QM; the 1949 pair (positrons via K_+ and space-time QED with the full diagrammatic apparatus); the 1950 mathematical formulation with explicit oscillator elimination and the proper-time representation of the Klein-Gordon propagator (the direct ancestor of the heat kernel); Schwinger's covariant formulation with the interaction representation and S = (1-iK)/(1+iK); Dyson's unification proof showing all three formulations give identical S-matrix elements. Together these establish the action-first, amplitude-first, renormalization-first methodology that the Feynman-Theorist agent applies to every framework.

### Broad Physics, Fermi Interaction, RG (condensed matter, weak interactions, gravity, partons, critical phenomena)
Papers: 07, 08, 09, 10, 11
Feynman's two-fluid model of He-II via path-integral permutation cycles (the template for all collective-mode / phononic-excitation pictures); Feynman-Gell-Mann V-A Fermi interaction (chirality as organizing principle of weak force); Feynman's 1963 approach to quantum gravity (discovery of ghost fields, non-renormalizability at 2-loop); Feynman's parton model for deep inelastic scattering (factorization, Bjorken scaling); Wilson-Kogut RG + epsilon expansion (universality, fixed points, relevant/irrelevant operators, the 4D triviality of phi^4).

### Quantum Computation
Papers: 12, 13, 14
Feynman's 1982 argument that quantum systems cannot be efficiently simulated classically (negative probabilities, Bell-type bound); Feynman's 1986 explicit Hamiltonian for a reversible quantum computer with program-counter cursor construction; Shor's polynomial-time factoring via quantum Fourier transform + order finding. Together these frame the framework's "substrate IS a quantum simulator" claim and bound what classical GPE simulations can and cannot capture.

### Heat Kernel + Spectral Action (CRITICAL toolchain)
Papers: 15, 16, 17, 18, 19
Vassilevich's comprehensive user's manual for heat-kernel expansions with explicit Seeley-DeWitt coefficients a_0, a_2, a_4, a_6 for Laplace-type operators with arbitrary bundle connections and boundary conditions; Chamseddine-Connes 1996 spectral-action principle Tr f(D/Lambda) + <psi, D psi> with explicit heat-kernel computation yielding SM + Einstein-Hilbert + Weyl^2 plus the GUT-boundary condition alpha_3 = alpha_2 = (5/3) alpha_1 and m_H ~ 160-180 GeV; van Nuland-van Suijlekom 2022 one-loop spectral action via cyclic-cocycle expansion with bounded divided-difference propagator G_{kl} = 1/f'[lambda_k, lambda_l] and quantum Ward identity (the first genuinely spectral renormalization at one loop); Beggs-Smith noncommutative complex differential geometry providing the bigraded Omega^{p,q} structure for holomorphic sheaves on the fibre; Hong's 2011 closed-form heat kernel on compact connected Lie groups with bi-invariant metric via Duflo isomorphism, yielding Z(t) ~ vol(G) exp(tS/6) and scalar curvature S = -(1/4) tr_g Cas. Papers 15, 16, 19 collectively determine every coefficient in the bare spectral action on Jensen-deformed SU(3).

### Cosmological Particle Creation + Schwinger Effect
Papers: 20, 21, 24, 25, 26
Parker's 1966 Harvard thesis establishing spontaneous pair creation in expanding FLRW spacetimes via Bogoliubov mixing between in/out Minkowski vacua, with upper bounds on present-day creation rates and the conformal-invariance no-creation theorem for massless nonzero-spin fields; Parker-Navarro-Salas 50-year retrospective with the Ford-Parker 1977 Lifshitz-gauge graviton-creation extension (what BICEP2/Planck search for); Franchino-Vinas-Mazzitelli-Pla 2026 resummed heat-kernel calculation of pair-creation in conformally flat spacetimes via Yukawa-analog in Minkowski (including radiation-dominated closed forms and Gaussian-scale-factor Schwinger analogues); Kaushal-Singh 2024 self-consistent Maxwell-Schrodinger semiclassical dynamics for backreaction-inclusive Schwinger effect in flat and de Sitter backgrounds; Garcia-Consuegra-Maleknejad 2025 stochastic Schwinger effect for statistically fluctuating gauge-field backgrounds with kinematic threshold omega^2 > |q|^2 + 4m^2.

### Richardson-Gaudin Integrability + Generalized Gibbs Ensemble
Papers: 27, 28, 29, 30
Dukelsky-Pittel-Sierra Colloquium on exactly solvable R-G models with rational, trigonometric, hyperbolic families, electrostatic mapping, and BCS emergence in the large-N limit; Vidmar-Rigol review of the generalized Gibbs ensemble rho_GGE = Z^{-1} exp(-sum lambda_k I_k) with the Lagrange-multiplier matching <psi_0| I_k |psi_0> = Tr[rho_GGE I_k], proving GGE describes integrable systems after equilibration and demonstrating generalized eigenstate thermalization in XX and TFI models; Claeys 2018 thesis with eigenvalue-based framework for R-G, Dicke-model contraction limit, Read-Green resonances in p+ip topological superconductor, and broken-integrability techniques (Floquet resonances, periodic driving, RG-CI for nuclear pairing); [Paper 30 filename mismatch note: file contains a 2018 Kuramoto synchronization paper by Faggian et al., not a Claeys quench-dynamics paper].

### Lorentzian Quantum Gravity (modern)
Papers: 31, 32
D'Angelo 2024 Lorentzian Wetterich-type FRGE with covariant formalism on globally hyperbolic spacetimes, yielding a non-trivial Asymptotic Safety fixed point (g*, lambda*) = (1.15, 0.42) with complex-conjugate critical exponents theta_{1,2} = 5.11 +/- 11.59 i; Pawlowski-Reichert-Wessely 2025 first self-consistent graviton spectral function in Lorentzian QG via spectral RG with on-shell renormalization, obtaining a positive spectral function with massless one-graviton peak + multi-graviton continuum, UV decay f_h(lambda) ~ 1/[lambda^2 log^3 lambda^2], total spectral weight z_spec ~ 1.486, and unit physical sum rule. Together these provide adversarial UV-completion benchmarks for the spectral-action approach.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Spectral action derivation | Papers 15, 16, 17, 18, 19 | CRITICAL |
| Seeley-DeWitt coefficients a_0, a_2, a_4 | Papers 15, 16 | CRITICAL |
| Bare spectral action on Jensen-deformed SU(3) | Papers 16, 19 | CRITICAL |
| Quantum spectral action / one-loop within NCG | Paper 17 | CRITICAL |
| Parker pair production in expanding spacetime | Papers 20, 21 | CRITICAL |
| Schwinger effect / gravitational analogues (transit) | Papers 24, 25, 26 | HIGH |
| GGE relic formation / Ordered Veil permanence | Papers 28, 29 | CRITICAL |
| Richardson-Gaudin integrability on Dirac spectrum | Papers 27, 29 | CRITICAL |
| Path-integral methodology | Papers 01, 04 | CRITICAL |
| Feynman rules / diagrammatic apparatus | Papers 02, 03, 06 | HIGH |
| Covariant QED / interaction picture | Papers 05, 06 | HIGH |
| Renormalizability power counting | Papers 06, 07 | HIGH |
| Proper-time / heat-kernel bridge | Papers 04, 15 | CRITICAL |
| Heat kernel on compact Lie groups (SU(3)) | Paper 19 | HIGH |
| Universality / RG flow / critical exponents | Paper 07 | HIGH |
| Yang-Mills renormalization in spectral action | Papers 17, 18 | MEDIUM |
| Weak interactions / V-A / chirality | Paper 08 | MEDIUM |
| Quantum gravity (perturbative) | Paper 09 | MEDIUM |
| Lorentzian QG / asymptotic safety | Papers 31, 32 | MEDIUM |
| Graviton unitarity / spectral function | Paper 32 | MEDIUM |
| Two-fluid superfluid / phonon-roton | Paper 10 | HIGH |
| Quantum computing as framework test | Papers 12, 13, 14 | LOW-MEDIUM |
| Parton model / deep inelastic scattering | Paper 11 | LOW |
| Stochastic gauge backgrounds | Paper 26 | MEDIUM |
| Backreaction in particle creation | Paper 25 | HIGH |
| Cosmological graviton creation (Ford-Parker) | Paper 21 | HIGH |

---

## Paper Entries

### Paper 01: Space-Time Approach to Non-Relativistic Quantum Mechanics
- **File**: `01_1948_Feynman_Space_time_approach_nonrelativistic_QM.md`
- **arXiv**: N/A (Rev. Mod. Phys. 20, 367)
- **Year**: 1948
- **Relevance**: CRITICAL
- **Tags**: path integral, sum over histories, Lagrangian QM, oscillator elimination

**Summary**: Feynman's foundational paper establishing a third formulation of quantum mechanics: the wave function as a sum over space-time paths weighted by exp(iS/hbar). Postulate I (sum rule) and Postulate II (action as phase) are shown equivalent to Schrodinger's equation for quadratic Lagrangians. The paper also introduces the oscillator-elimination technique (integrating out linearly-coupled harmonic oscillators exactly via Gaussian integration), which is the prototype for all functional-integration manipulations on coupled gauge fields.

**Key Results**:
- Path integral equivalent to Schrodinger equation for quadratic L
- Dominant paths are Brownian-like (continuous, nowhere differentiable)
- Classical limit recovered via stationary phase as hbar -> 0
- Exact elimination of harmonic oscillator coordinates yields bi-local effective action
- Generalization to non-Lagrangian actions (Wheeler-Feynman absorber theory)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| phi = int D[x] exp(iS/hbar) | Path amplitude postulate | Postulate II, Sec. 4 |
| phi(R) = lim_{eps->0} int_R exp(i sum S/hbar) prod dx_i/A | Discretized path integral | Eq. 12 |
| A = (2 pi i hbar eps/m)^{1/2} | Gaussian normalization | Eq. 28 |
| psi(x_{k+1}, t+eps) = int exp(iS(x_{k+1},x_k)/hbar) psi(x_k,t) dx_k/A | Wave-function recursion | Eq. 18 |
| G_{mn} | Oscillator-elimination G factor | Sec. 13 |

**Dependencies**: Upstream root. Downstream: 02, 03, 04 directly; 15, 16, 20 via proper-time and heat-kernel bridge; 12, 13 as template for quantum computation.

---

### Paper 02: The Theory of Positrons
- **File**: `02_1949_Feynman_Theory_of_positrons.md`
- **arXiv**: N/A (Phys. Rev. 76, 749)
- **Year**: 1949
- **Relevance**: CRITICAL
- **Tags**: propagator K_+, Stuckelberg time reversal, vacuum loop, CPT

**Summary**: Replaces Dirac's hole theory with a reinterpretation: positrons are electrons with world-lines reversed in time. Introduces the central propagator K_+(2,1) with iepsilon prescription and shows that the one-particle reinterpretation is equivalent to second quantization. The vacuum persistence amplitude C_v = exp(-L) with L a closed-fermion loop is derived, with Pauli sign structure (-L) vs Bose (+L).

**Key Results**:
- Propagator K_+(2,1) with iepsilon: positive-energy forward, negative-energy backward
- Perturbation series in external A with standard diagrammatic structure
- Antisymmetrization only on external states (intermediate states auto-handled by K_+)
- Vacuum persistence C_v = exp(-L); one-loop L is UV-divergent (awaiting renormalization)
- Framework map: Feynman's iepsilon <-> NCG's [J, D_K] = 0 (KO-dim 6)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| K_+^(A) = K_+ - i int K_+ A K_+ + ... | Perturbation expansion | Eqs. 13-16 |
| K_+(2,1) = (i/4pi^2) int (pslash-m+i delta)^{-1} exp(-ip.x_{21}) d^4p | Momentum-space propagator | Eqs. 31-32 |
| K(3,4;1,2) = K_+a(3,1) K_+b(4,2) - K_+a(4,1) K_+b(3,2) | Many-particle amplitude | Eq. 27 |
| C_v = exp(-L); L^(1) = -(1/2) int int Sp[K_+ A K_+ A] | Vacuum-to-vacuum amplitude | Eq. 30 |

**Dependencies**: Depends on 01 (path integral). Companion to 03 (QED diagrams) and 04 (math formulation). Framework map to NCG: [J, D_K]=0 permanent result (S34+).

---

### Paper 03: Space-Time Approach to Quantum Electrodynamics
- **File**: `03_1949_Feynman_Space_time_approach_QED.md`
- **arXiv**: N/A (Phys. Rev. 76, 769)
- **Year**: 1949
- **Relevance**: CRITICAL
- **Tags**: Feynman rules, diagrams, self-energy, vacuum polarization, anomalous moment, Lamb shift

**Summary**: Establishes the complete Feynman-rule machinery for QED. Electron propagator (pslash - m)^{-1}, photon propagator k^{-2}, vertex gamma_mu, with factor e^2/(pi i) per virtual quantum. Self-energy mass shift, anomalous magnetic moment (Schwinger's alpha/2 pi), Lamb shift contribution, and vacuum polarization with Bethe-Pauli gauge-invariant subtraction. The appendix introduces Feynman parameters and the Wick-rotation-style evaluation of loop integrals.

**Key Results**:
- Feynman rules in momentum space (propagators, vertices, loop integration)
- Compton scattering amplitude as sum of two diagrams (Klein-Nishina)
- Mass shift Delta m = (3 alpha/2 pi) m ln(Lambda/m) + finite
- Anomalous moment (q-slash a - a q-slash)/(2m) piece = alpha/2 pi
- Lamb shift from (4 q^2/3 m^2)(ln(m/lambda_min) - 3/8)
- Charge renormalization Delta e^2/e^2 = -(2 alpha/3 pi) ln(Lambda/m) -- logarithmic only, not quadratic
- Feynman-parameter a^{-1} b^{-1} = int_0^1 dx (ax + b(1-x))^{-2}

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| delta_+(x) = int_0^inf exp(-i omega x) d omega / pi | Positive-frequency delta | Eq. 3 |
| K^(1)(2,1) = -ie^2 int int K_+ gamma K_+ gamma K_+ delta_+ | One-loop electron self-energy | Eq. 6 |
| Sigma(p) = (e^2/pi i) int gamma_mu (pslash-kslash-m)^{-1} gamma_mu k^{-2} d^4k | Self-energy momentum-space | Eq. 11 |
| Delta m = m(e^2/2 pi)(3 ln(Lambda/m) + 3/4) | Electron mass renormalization | Eq. 21 |
| delta M = (e^2/4 pi)[(1/2m)(q-slash a - a q-slash) + ...] | Anomalous moment + Lamb shift | Eq. 24 |
| J_{mu nu}^P = -(e^2/pi)(q_mu q_nu - delta_{mu nu} q^2) [...] | Gauge-invariant vacuum polarization | Eq. 33 |

**Dependencies**: Builds on 02 (K_+). Unified with 05 (Schwinger) and 06 (Dyson). Framework: translation layer from spectral action (16) to measurable cross-sections.

---

### Paper 04: Mathematical Formulation of the Quantum Theory of Electromagnetic Interaction
- **File**: `04_1950_Feynman_Mathematical_formulation_QED.md`
- **arXiv**: N/A (Phys. Rev. 80, 440)
- **Year**: 1950
- **Relevance**: CRITICAL
- **Tags**: proper time, oscillator elimination, KG propagator, generating functional, fifth parameter

**Summary**: Establishes validity of Feynman rules by deriving them from Fermi's oscillator expansion of the EM field. Integrating out the oscillators in Lagrangian form gives a complex bi-local self-action R (Eq. 24) containing all virtual photon effects to all orders. Appendix A introduces the proper-time (fifth-parameter) formulation of the Klein-Gordon equation, giving the propagator as 2iI_+(x,x') = int_0^inf du_0 k^(0)(x,u_0; x',0) exp(-i m^2 u_0/2) -- the direct Lorentzian ancestor of the Schwinger-DeWitt heat-kernel representation used throughout the spectral-action program.

**Key Results**:
- Exact elimination of transverse EM oscillators yields the all-orders self-action R
- Exact cancellation of instantaneous Coulomb term, restoring Lorentz invariance
- All-orders generating functional T_{e^2}[B]
- Proper-time representation of KG propagator (Eq. A9) -- root of the heat kernel
- Bose statistics + photon combinatorics emerge from exp(i R_{ac})
- Self-interacting KG amplitude as single exponential of proper-time action plus bi-local delta_+

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| R = -(1/2) sum int int e_n e_m (1 - v_n.v_m) delta_+((t-s)^2 - (x-y)^2) ds dt | All-orders photon action | Eq. 24 |
| T_{e^2}[B] = exp[-(ie^2/2) int int j_mu(1) j^mu(2) delta_+(s_{12}^2) dtau_1 dtau_2] exp[-i int j_nu B^nu dtau] | Generating functional | Eq. 54 |
| i d phi/du = -(1/2)(i d_mu - A_mu)^2 phi | KG proper-time Schrodinger | Eq. A2 |
| 2 i I_+(x,x') = int_0^inf du_0 k^(0)(x,u_0; x',0) exp(-i m^2 u_0/2) | KG propagator as proper-time integral | Eq. A9 |
| k^(0)(x, u_0; x', 0) = (4 pi^2 u_0^2 i)^{-1} exp[-i(x-x')^2/(2 u_0)] | Free KG kernel | Eq. A8 |

**Dependencies**: Depends on 01 (path integral), 03 (QED rules). Upstream to 15 (heat kernel), 16 (spectral action), 20 (Parker). The proper-time kernel is THE bridge between Lorentzian QFT and Euclidean spectral action.

---

### Paper 05: Quantum Electrodynamics. I. A Covariant Formulation
- **File**: `05_1948_Schwinger_QED_I_Covariant_formulation.md`
- **arXiv**: N/A (Phys. Rev. 74, 1439)
- **Year**: 1948
- **Relevance**: CRITICAL
- **Tags**: interaction representation, space-like surface, Tomonaga-Schwinger, S-matrix, variational principle

**Summary**: Schwinger's foundational covariant QED. Replaces equal-time canonical commutators with arbitrary space-like surfaces sigma, introduces the interaction representation i hbar c delta Psi/delta sigma(x) = H(x) Psi (Tomonaga-Schwinger equation), and builds invariant D(x) and Delta(x) functions. The collision operator S is expressed via the Hermitian reaction operator K: S = (1-iK)/(1+iK), with a variational principle delta K = 0 at the integral-equation solution. Translation invariance gives [S, P_mu^(0)] = 0.

**Key Results**:
- Space-like-surface quantization with covariant commutators
- Interaction-representation canonical transformation to free-field equations
- Invariant propagation functions D(x), Delta(x)
- Covariant longitudinal elimination + Coulomb kernel
- Cayley form S = (1 - iK)/(1 + iK)
- Variational principle delta K = 0
- Energy-momentum conservation [S, P_mu^(0)] = 0

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| i hbar c delta U/delta sigma(x) = H(x) U | Tomonaga-Schwinger equation for U | Eq. 2.5 |
| H(x) = -(1/c) j_mu(x) A_mu(x) | Interaction Hamiltonian density | Eq. 2.7 |
| [A_mu(x), A_nu(x')] = i hbar c delta_{mu nu} D(x-x') | Free-field photon commutator | Eq. 2.28 |
| S = (1 - iK)/(1 + iK) | Cayley form of unitary S | Eq. 4.16 |
| delta K = 0 | Variational principle | Eq. 4.22-4.23 |

**Dependencies**: Independent covariant formulation; unified with 03 by Dyson (06). Upstream to 15 via proper-time in Schwinger's QED-II sequel. Framework: S38 Schwinger-instanton duality.

---

### Paper 06: The Radiation Theories of Tomonaga, Schwinger, and Feynman
- **File**: `06_1949_Dyson_Radiation_theories_of_Tomonaga_Schwinger_Feynman.md`
- **arXiv**: N/A (Phys. Rev. 75, 486)
- **Year**: 1949
- **Relevance**: CRITICAL
- **Tags**: Dyson unification, S-matrix, Wick theorem, renormalization, power counting, Ward identity

**Summary**: Dyson proves the mathematical equivalence of Tomonaga's, Schwinger's, and Feynman's formulations of QED, showing that all three give identical S-matrix elements to every order of perturbation theory. Establishes Wick's theorem for time-ordered products as Feynman propagators + normal ordering, derives the linked-cluster theorem (S = exp(sum connected)), provides the power-counting classification of divergences D = 4 - (3/2)E_e - E_gamma, and demonstrates renormalizability to all orders via systematic subtraction + Ward identity Z_1 = Z_2.

**Key Results**:
- Equivalence of three QED formulations proved to all orders
- Wick theorem: time-ordered = normal-ordered + all contractions (= Feynman propagators)
- Linked-cluster theorem: S = exp(sum connected diagrams)
- Power-counting: D = 4 - (3/2) E_e - E_gamma
- Only three primitive divergences in QED: electron self-energy, vacuum polarization, vertex
- Ward identity Z_1 = Z_2 from U(1) gauge invariance
- Renormalizability to all orders (outline; BPHZ completed this)
- Perturbation series is asymptotic, not convergent (1952 follow-up)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| S = T exp(-i int H_I(t) dt) | S-matrix in interaction representation | Sec. 1 |
| overline{phi(x) phi(y)} = i S_F(x-y) or i D_F(x-y) | Wick contraction | Sec. 2 |
| D = 4 - (3/2) E_e - E_gamma | Superficial degree of divergence | Sec. 5 |
| q_mu Gamma^mu(p+q, p) = S_F^{-1}(p+q) - S_F^{-1}(p) | Ward identity | Sec. 6 |
| S = exp(sum connected) | Linked-cluster theorem | Sec. 4 |

**Dependencies**: Unifies 02, 03, 04, 05. Foundation for all subsequent perturbative QFT; template for the Standard Model and ultimately for the spectral action's power-counting structure.

---

### Paper 07: The Renormalization Group and the Epsilon Expansion
- **File**: `07_1974_Wilson_Kogut_RG_and_epsilon_expansion.md`
- **arXiv**: N/A (Phys. Reports 12, 75)
- **Year**: 1974
- **Relevance**: CRITICAL
- **Tags**: renormalization group, universality, epsilon expansion, fixed points, critical exponents, triviality

**Summary**: Wilson-Kogut's systematic RG formulation. The RG is a map tau on the space of local Hamiltonians whose fixed points tau(H*) = H* define universality classes. The epsilon = 4-d expansion places the phi^4 Wilson-Fisher fixed point at u* = O(epsilon), yielding critical exponents as power series in epsilon (e.g., nu = 1/2 + epsilon/12 + ...). Irrelevant operators drop out; relevant and marginal ones control low-energy physics. 4D phi^4 is trivial (only the Gaussian fixed point).

**Key Results**:
- RG as map on Hamiltonian space with fixed points = universality classes
- Gaussian model: r' = 4r, nu = 1/2 from eigenvalue = 4
- phi^4 coupling has scaling dimension 4-d: marginal in d=4, relevant for d<4
- Wilson-Fisher fixed point at u* = O(epsilon); nu = 1/2 + epsilon/12 + ...
- QFT <-> stat mech equivalence at criticality
- 4D phi^4 triviality (Higgs mass requires compositeness or compactification)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| tau(H*) = H* | Fixed-point condition | Eq. 1.2 |
| H = -(1/2) int_q (q^2 + r) sigma_q sigma_{-q} | Gaussian model | Eq. 3.15 |
| r' = 4 r | Gaussian RG recursion | Eq. 3.35 |
| nu = ln 2 / ln lambda | Critical exponent | Eq. 3.42 |
| [u] = 4 - d = epsilon | Scaling dimension of phi^4 | Sec. 4 |
| nu = 1/2 + epsilon/12 + O(epsilon^2) | Wilson-Fisher nu | Sec. 8 |

**Dependencies**: Historical roots in Gell-Mann-Low and Kadanoff. Upstream to 15 (heat kernel power counting), 16 (spectral action RG running), 31 (functional RG in Lorentzian QG).

---

### Paper 08: Theory of the Fermi Interaction
- **File**: `08_1958_Feynman_Gell_Mann_Theory_of_Fermi_interaction.md`
- **arXiv**: N/A (Phys. Rev. 109, 193)
- **Year**: 1958
- **Relevance**: MEDIUM
- **Tags**: V-A, weak interactions, parity violation, two-component neutrino, CVC

**Summary**: Proposes the V-A form of the weak current: J^mu = psibar gamma^mu (1 - gamma^5) psi, coupled current-current via H = G_F/sqrt(2) J^mu J_mu^dagger. Parity violation is maximal: only left-handed fermions couple. Predictions include Michel parameters in muon decay, pion decay ratio Gamma(pi -> e nu)/Gamma(pi -> mu nu) ~ (m_e/m_mu)^2 (m_pi^2 - m_e^2)^2/(m_pi^2 - m_mu^2)^2, and the CVC hypothesis relating the weak vector current to the electromagnetic isospin current.

**Key Results**:
- V-A structure: weak current projects onto left-handed fermions
- Maximal parity violation (inherent to V-A)
- Two-component neutrino: m_nu = 0 implies Weyl spinor
- Michel parameter rho = 3/4, asymmetry xi = 1 in muon decay
- Pion decay ratio ~ 1.28 x 10^{-4} (agrees with data)
- CVC: g_V = 1 exactly (unrenormalized by strong interaction)
- Precursor to electroweak gauge theory SU(2)_L x U(1)_Y

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| J^mu = psibar_1 gamma^mu (1 - gamma^5) psi_2 | V-A current | Sec. 3 |
| H_weak = (G_F/sqrt(2)) J^mu J_mu^dagger | Universal Fermi interaction | Sec. 3 |
| Gamma(pi->e nu)/Gamma(pi->mu nu) ~ (m_e/m_mu)^2 x ... ~ 1.28e-4 | Pion decay ratio | Sec. 5 |
| V^mu_weak = V^mu_{1+i2} | CVC identification | Sec. 6 |

**Dependencies**: Independent of path-integral chain. Framework relevance: the V-A chirality structure must be reproduced by the spectral-action decomposition of D_K (not directly testable in the heat-kernel coefficients but a constraint on the fibre geometry).

---

### Paper 09: Quantum Theory of Gravitation
- **File**: `09_1963_Feynman_Quantum_theory_of_gravitation.md`
- **arXiv**: N/A (Acta Physica Polonica 24, 697)
- **Year**: 1963 (1957 Chapel Hill talk)
- **Relevance**: MEDIUM
- **Tags**: perturbative gravity, graviton propagator, Faddeev-Popov ghosts, non-renormalizability

**Summary**: Feynman's seminal attempt to quantize gravity as a spin-2 field on flat background, g_{mu nu} = eta_{mu nu} + kappa h_{mu nu} with kappa = sqrt(32 pi G). Derives the graviton propagator in harmonic gauge, identifies the cubic and higher self-interaction vertices, and discovers ghost fields: loop calculations violate unitarity unless fictitious anti-commuting vector particles are added to cancel unphysical longitudinal and trace-mode contributions. Power-counting foreshadows non-renormalizability (2 + 2L divergences at L loops); 't Hooft-Veltman 1974 showed 1-loop vanishes on shell, but Goroff-Sagnotti 1986 showed 2-loop has a non-removable R^3 divergence.

**Key Results**:
- Graviton propagator in Feynman gauge: (1/k^2)[symmetric projector - (1/2) eta eta]
- Tree-level graviton exchange reproduces Newton's law
- Ghost fields required for unitarity in non-Abelian gauge loops (predecessor of Faddeev-Popov 1967)
- Power counting: D = 2L + 2 (non-renormalizable at 2-loop)
- Gravity as effective field theory below Planck scale

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| g_{mu nu} = eta_{mu nu} + kappa h_{mu nu}, kappa = sqrt(32 pi G) | Linearized expansion | Sec. 1 |
| h_{mu nu} -> h_{mu nu} + d_mu xi_nu + d_nu xi_mu | Gauge transformation | Sec. 1 |
| D(k) = (i/k^2)[(1/2)(eta eta + eta eta) - (1/2) eta eta] | Graviton propagator | Sec. 2 |
| D = 2 + 2L | Power counting for gravity | Sec. 7 |

**Dependencies**: Independent of path-integral chain. Upstream to 31, 32 (Lorentzian quantum gravity). Framework: adversarial UV completion to spectral action.

---

### Paper 10: Atomic Theory of the Two-Fluid Model of Liquid Helium
- **File**: `10_1954_Feynman_Atomic_theory_of_two_fluid_model_liquid_helium.md`
- **arXiv**: N/A (Phys. Rev. 94, 262)
- **Year**: 1954
- **Relevance**: HIGH
- **Tags**: superfluidity, phonons, rotons, permutation cycles, BEC, quantized vortices, path integral

**Summary**: Feynman derives superfluidity of He-II from first-principles atomic physics via the path integral. Permutation cycles of particle worldlines (required for Bose statistics) dominate below the lambda transition when thermal wavelength approaches interparticle spacing. Variational excitation spectrum epsilon(k) = hbar^2 k^2/(2 m S(k)) (where S(k) is the static structure factor) reproduces the phonon-roton spectrum. The Landau critical velocity v_c = min[epsilon(p)/p] equals the roton gap divided by the roton momentum. Quantized vortices with circulation oint v_s dot dl = n h/m arise from the single-valuedness of the condensate phase.

**Key Results**:
- Superfluidity from Bose-statistics permutation cycles in path integral
- Excitation spectrum epsilon(k) = hbar^2 k^2 / (2 m S(k)): phonons at small k, rotons at k_0
- Landau critical velocity v_c = min[epsilon(p)/p] ~ 58 m/s
- Quantized vortex circulation oint v_s dot dl = n h/m
- Framework template: particles as collective excitations of a strongly-interacting condensate

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Z = (1/N!) sum_P int prod dr_i rho(R; R_P; beta) | Partition function with permutations | Sec. 1 |
| epsilon(k) = hbar^2 k^2 / (2 m S(k)) | Feynman excitation spectrum | Sec. 3 |
| v_c = min[epsilon(p)/p] = Delta/p_0 | Landau critical velocity | Sec. 5 |
| oint v_s.dl = n h/m | Quantized circulation | Sec. 6 |

**Dependencies**: Independent technical development; links to Wilson RG (07) via collective-mode / universality picture. Framework: template for phonon-exflation substrate; template for R-G / GGE sessions (27-30).

---

### Paper 11: Very High-Energy Collisions of Hadrons
- **File**: `11_1969_Feynman_Very_high_energy_collisions_of_hadrons.md`
- **arXiv**: N/A (Phys. Rev. Lett. 23, 1415)
- **Year**: 1969
- **Relevance**: LOW
- **Tags**: parton model, Bjorken scaling, infinite momentum frame, factorization

**Summary**: Feynman's parton model for high-energy hadronic collisions. In the infinite-momentum frame, a hadron is a collection of point-like constituents each carrying a fraction x of the hadron's momentum. Virtual-photon scattering reduces to incoherent elastic scattering off partons, explaining Bjorken scaling F_2(x) = sum e_i^2 x f_i(x) and the Callan-Gross relation F_2 = 2 x F_1. Foundational for factorization in QCD and all LHC physics.

**Key Results**:
- Partons as point-like hadronic constituents
- Bjorken scaling explained: F_2(x) = sum e_i^2 x f_i(x)
- Callan-Gross relation F_2 = 2 x F_1 (spin-1/2 partons)
- Momentum sum rule: sum int x f_i(x) dx = 1 (gluons carry ~50%)
- Factorization formula for hadronic cross sections
- DGLAP evolution (later)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| x = Q^2/(2 M nu) | Bjorken variable = parton momentum fraction | Sec. 2 |
| F_2(x) = sum_i e_i^2 x f_i(x) | DIS structure function | Sec. 2 |
| F_1 = F_2/(2x) | Callan-Gross relation | Sec. 2 |
| sigma(A+B->X) = sum int dx1 dx2 f_i^A f_j^B hat sigma | Factorization formula | Sec. 4 |

**Dependencies**: Independent line of development. Low priority for phonon-exflation (not directly connected to framework mechanisms).

---

### Paper 12: Simulating Physics with Computers
- **File**: `12_1982_Feynman_Simulating_physics_with_computers.md`
- **arXiv**: N/A (Int. J. Theor. Phys. 21, 467)
- **Year**: 1982
- **Relevance**: MEDIUM
- **Tags**: quantum simulation, negative probabilities, Bell inequality, quantum computer

**Summary**: Feynman's keynote arguing that quantum systems cannot be efficiently simulated by classical probabilistic computers. The Wigner-function "probabilities" take negative values, which no local classical probabilistic automaton can sample from. The two-photon EPR correlation cos^2(30 deg) = 3/4 exceeds the classical local-hidden-variable bound 2/3 (Bell-type inequality). Proposes that a genuinely quantum computer built from 2-state elements (sigma_x, sigma_y, sigma_z algebra, a = (sigma_x - i sigma_y)/2) can serve as a universal simulator of quantum physics.

**Key Results**:
- Local probabilistic automaton simulates classical stochastic physics
- Classical probabilistic computer CANNOT simulate quantum physics (negative probabilities)
- Two-photon EPR: cos^2(30 deg) = 3/4 > 2/3 (classical bound)
- Quantum computer as universal quantum simulator (Bose sector; Fermi left open)
- 2-state operator algebra isomorphic to spin-1/2 building blocks

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| P_{t+1}({s}) = sum Pi m(s_i \| neighbors) P_t({s'}) | Classical stochastic update | p. 473 |
| W(x,p) = int rho(x+y/2, x-y/2) exp(ipy) dy | Wigner function | p. 478 |
| a = (sigma_x - i sigma_y)/2, a* = (sigma_x + i sigma_y)/2 | 2-state creation/annihilation | p. 475 |
| P_match(30 deg) <= 2/3 (classical) vs cos^2(30) = 3/4 (QM) | Bell-type bound violation | p. 484-485 |

**Dependencies**: Framework: relevant to assessing what classical GPE simulations can and cannot capture about substrate quantum dynamics.

---

### Paper 13: Quantum Mechanical Computers
- **File**: `13_1986_Feynman_Quantum_mechanical_computers.md`
- **arXiv**: N/A (Optics News Feb 1986)
- **Year**: 1986
- **Relevance**: MEDIUM
- **Tags**: quantum computer, Toffoli gate, reversible logic, cursor Hamiltonian

**Summary**: Feynman exhibits an explicit Hamiltonian for a quantum mechanical computer. Two-state atoms represent bits; reversible logic primitives (NOT, C-NOT, Toffoli) are realized as unitary matrices built from a, a* with aa*+a*a=1. A (k+1)-site program counter implements any gate sequence M = A_k ... A_1 via H = sum q_{i+1}^* q_i A_{i+1} + h.c.; the cursor propagation is tight-binding / spin-wave dynamics. Free energy dissipation per step is bounded by kT p (t_min/t_actual), with no uncertainty-principle penalty.

**Key Results**:
- Explicit H for universal reversible quantum computer
- NOT + Toffoli (or NOT + SWITCH) is universal
- Cursor dynamics = 1D tight-binding / spin-wave propagation
- Free energy per step: kT p (t_min/t_actual), can go to zero
- Ballistic step time ~ 6e-15 s for 0.1 eV couplings

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| a a* + a* a = 1 | Two-state CCR | p. 14 |
| A_{ab,c} = 1 + a*a b*b (c + c* - 1) | Toffoli (CC-NOT) gate | p. 14 |
| H = sum q_{i+1}^* q_i A_{i+1} + h.c. | Program-counter Hamiltonian | p. 15 |
| Delta F/step = kT p (t_min/t_actual) | Free-energy dissipation | p. 16 |

**Dependencies**: Depends on 12. Framework: template for substrate computational capacity.

---

### Paper 14: Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer
- **File**: `14_1994_Shor_Polynomial_time_algorithms_factoring.md`
- **arXiv**: quant-ph/9508027 (SIAM J. Computing 26, 1484)
- **Year**: 1994 (full 1996)
- **Relevance**: LOW
- **Tags**: Shor's algorithm, QFT, order finding, quantum complexity (BQP)

**Summary**: Shor gives quantum polynomial-time algorithms for factoring integers and discrete logarithm. Reduction of factoring to order-finding (Miller 1976); quantum Fourier transform A_q (built from O(l^2) Hadamard + controlled-phase gates); modular exponentiation in quantum superposition; continued-fraction recovery of the period r from measured c/q. Success probability >= 4/(pi^2 r^2) per run; O(log log r) repetitions suffice.

**Key Results**:
- Factoring in O(l^2 log l log log l) quantum steps (exponentially faster than classical)
- Discrete logarithm same complexity
- QFT on 2^l in O(l^2) local gates
- Establishes BQP as a proper complexity class
- Negative implication: either QM is classically hard to simulate OR factoring is classically easy

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| A_q \|a> = (1/sqrt q) sum_c exp(2 pi i a c / q) \|c> | Quantum Fourier transform | Eq. 4.1 |
| (1/q) sum_{a,c} exp(2 pi i a c / q) \|c> \|x^a mod n> | Order-finding state | Eq. 5.4 |
| \|c/q - d/r\| <= 1/(2 q), q > n^2 | Continued-fraction condition | Eq. 5.13 |

**Dependencies**: Depends on 12, 13. Framework (LOW): phase-estimation primitive applied to exp(i D_K t) could extract spectral data, but not a current project computation.

---

### Paper 15: Heat Kernel Expansion: User's Manual
- **File**: `15_2003_Vassilevich_Heat_kernel_expansion_users_manual.md`
- **arXiv**: hep-th/0306138
- **Year**: 2003
- **Relevance**: CRITICAL
- **Tags**: heat kernel, Seeley-DeWitt, Laplace-type operator, Gilkey coefficients, one-loop effective action, zeta regularization

**Summary**: Vassilevich's comprehensive reference for heat-kernel techniques. Heat kernel K(t;x,y;D) of a Laplace-type operator D = -(g^{mu nu} nabla_mu nabla_nu + E) expands as a power series in t with Seeley-DeWitt/Gilkey coefficients a_k built from universal local invariants of R_{mu nu rho sigma}, E, Omega_{mu nu}. Provides closed-form a_0 = int tr(I), a_2 = (1/6) int tr(6 E + R), a_4 = (1/360) int tr(60 E_{;kk} + 60 R E + 180 E^2 + 12 R_{;kk} + 5 R^2 - 2 R_{ij} R^{ij} + 2 R_{ijkl} R^{ijkl} + 30 Omega_{ij} Omega^{ij}). The zeta-regularized effective action W^ren = -(1/2) zeta'(0) - (1/2) ln(mu^2) zeta(0) is the master formula for one-loop physics.

**Key Results**:
- Heat-kernel coefficients a_k on closed manifolds (a_0 through a_4 explicit)
- Operator-specific endomorphisms E for scalars (E = -U''/2 - xi R), spinors (E = -R/4 + (1/4)[gamma,gamma] F_{mu nu} + ...), vectors, gravitons
- Conformal anomaly <T^mu_mu> ~ a_n at coincidence: n=4 gives bC^2 + b' E_4
- Boundary heat kernels with Dirichlet, Neumann/Robin, mixed conditions
- R-summed low-energy expansion: K(x,x;s) = (4 pi s)^{-n/2} e^{Rs/6} (bar-a_0 + bar-a_1 s + ...)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| (d_t + D_x) K(t;x,y;D) = 0 | Heat equation | Eq. 1.10-1.11 |
| Tr(f e^{-tD}) ~ sum t^{(k-n)/2} a_k(f,D) | Heat-trace expansion | Eq. 2.21 |
| a_0 = (4 pi)^{-n/2} int sqrt g tr(f) | Zeroth SDW coefficient | Eq. 4.26 |
| a_2 = (4 pi)^{-n/2} (1/6) int sqrt g tr(f(6 E + R)) | Second SDW coefficient | Eq. 4.27 |
| a_4 = (4 pi)^{-n/2} (1/360) int sqrt g tr(f * [60 E_{;kk}+60RE+180E^2+...]) | Fourth SDW coefficient | Eq. 4.28 |
| W^ren = -(1/2) zeta'(0) - (1/2) ln(mu^2) zeta(0) | Zeta-regularized effective action | Eq. 2.32 |
| K(x,x;s) = (4 pi s)^{-n/2} e^{Rs/6}(bar-a_0 + bar-a_1 s + ...) | R-summed expansion | Sec. 8 |

**Dependencies**: Historical roots in 04 (proper time), 05 (Schwinger). Essential for 16, 17, 19, 24. Framework: master reference for every computation SDW coefficient calculation.

---

### Paper 16: The Spectral Action Principle
- **File**: `16_1996_Chamseddine_Connes_Spectral_action_principle.md`
- **arXiv**: hep-th/9606001
- **Year**: 1996
- **Relevance**: CRITICAL
- **Tags**: spectral action, noncommutative geometry, SM from geometry, GUT boundary, Higgs mass

**Summary**: Chamseddine-Connes founding paper on the spectral action principle. The universal action S = Tr chi(D/Lambda) + <psi, D psi> on a spectral triple (A, H, D) reproduces the Standard Model coupled to Einstein + Weyl gravity when A = C^inf(M) (x) A_F with A_F = C + H + M_3(C) (the Standard Model algebra). Heat-kernel computation of Tr chi(D^2/Lambda^2) yields a_0 (cosmological constant), a_2 (Einstein-Hilbert / Newton's constant), a_4 (Yang-Mills + Weyl^2 + Higgs quartic + -(1/6) R |H|^2). Gives the SU(5)-type GUT boundary condition alpha_3 = alpha_2 = (5/3) alpha_1 at Lambda ~ 10^{15} GeV and predicts sin^2 theta_W ~ 0.21 (10% low) and m_H ~ 160-180 GeV (from lambda(Lambda) = (16 pi/3) alpha_3(Lambda) ~ 0.402).

**Key Results**:
- Universal formula S = Tr chi(D/Lambda) + <psi, D psi>
- Inner fluctuations D -> D + A + JAJ^{-1} reproduce SM bosons
- SDW a_0 -> CC moment; a_2 -> Einstein-Hilbert; a_4 -> YM + Higgs + -(1/6) R|H|^2
- SU(5) boundary: alpha_3 = alpha_2 = (5/3) alpha_1 at Lambda ~ 10^{15} GeV
- sin^2 theta_W ~ 0.21; m_H ~ 160-180 GeV
- Bare CC relation: e_0 = e + Lambda^4 (62/32 pi^2) + ... (62 = 90 fermionic - 28 bosonic dof)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| S = Tr chi(D/Lambda) + <psi, D psi> | Universal spectral action | Eq. 1.28 |
| D -> D_0 + A + JAJ^{-1}, A = sum a_i[D_0, b_i] | Inner fluctuations | Eq. 1.23 |
| Tr chi(P) ~ sum f_n a_n(P) | Heat-trace expansion | Eq. 2.14 |
| f_0 = int chi(u) u du; f_2 = int chi(u) du; f_{2(n+2)} = (-1)^n chi^{(n)}(0) | Chi moments | Eq. 2.15 |
| a_0 ~ -3N/(80 g_0^2); c_0 = -(2/3) a_0; d_0 = -(11/3) a_0 | Bare constants (EYM test) | Eq. 2.29 |
| alpha_3 = alpha_2 = (5/3) alpha_1 at Lambda | GUT boundary condition | Eq. 3.26 |
| lambda(Lambda) = (16 pi/3) alpha_3(Lambda) ~ 0.402; 160 < m_H < 200 GeV | Higgs prediction | Eq. 3.30-3.34 |

**Dependencies**: Depends on 15 (heat kernel). Upstream to 17 (one-loop), 18 (NCG differential geometry), 19 (heat kernel on Lie group -- SU(3) case). Framework: founding paper for the entire project.

---

### Paper 17: One-Loop Corrections to the Spectral Action
- **File**: `17_2022_vanNuland_vanSuijlekom_One_loop_spectral_action.md`
- **arXiv**: 2107.08485
- **Year**: 2021/2022
- **Relevance**: CRITICAL
- **Tags**: quantum spectral action, cyclic cocycles, Ward identity, divided differences, higher Chern-Simons

**Summary**: First construction of a one-loop quantum spectral action that stays within the noncommutative-geometry framework. The classical spectral action expands as S_D[V] = sum [int_{psi_{2k-1}} cs_{2k-1}(A) + (1/2k) int_{phi_{2k}} F^k] with higher Chern-Simons forms. Background-field method over hermitian matrix fluctuations: bounded gauge propagator G_{kl} = 1/f'[lambda_k, lambda_l] from divided differences. Quantum Ward identity extends the classical one, ensuring the one-loop divergent part takes the same cyclic-cocycle form as the classical action with shifted cocycles phi -> phi - tilde phi, psi -> psi - tilde psi (generalized one-loop renormalizability in the Gomis-Weinberg sense).

**Key Results**:
- Classical spectral-action expansion in higher Chern-Simons + Yang-Mills forms
- Bounded gauge propagator G_{kl} = 1/f'[lambda_k, lambda_l] (a regularising property absent from local QFT)
- Quantum Ward identity from divided-difference identity for f'
- One-loop divergent part preserves cyclic-cocycle structure
- Generalized one-loop renormalizability within the spectral framework

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| S_D[V] = Tr[f(D+V) - f(D)] = sum (1/n) <V, ..., V> | Spectral action expansion | Eq. 1 |
| <V_1,...,V_n> = Tr oint (dz/2 pi i) f'(z) V_1 (z-D)^{-1} ... V_n (z-D)^{-1} | Cyclic bracket | Eq. 2 |
| (z-D)^{-1} a - a (z-D)^{-1} = (z-D)^{-1} [D,a] (z-D)^{-1} | Fermion Ward identity | Eq. 3 |
| G_{kl} = 1/f'[lambda_k, lambda_l] | Bounded gauge propagator | Sec. 3 |
| S_D[V] = sum [int_{psi_{2k-1}} cs_{2k-1}(A) + (1/2k) int_{phi_{2k}} F^k] | Classical expansion | Eq. 7 |

**Dependencies**: Depends on 15 (heat kernel), 16 (spectral action). Framework: key reference for Computation C (quantum spectral action on Jensen-deformed SU(3)).

---

### Paper 18: Noncommutative Complex Differential Geometry
- **File**: `18_2012_vanSuijlekom_Renormalization_YM_spectral_action.md` (note: filename assigned by orchestrator; actual content is Beggs-Smith 2012 on NC complex differential geometry)
- **arXiv**: 1209.3595
- **Year**: 2012
- **Relevance**: HIGH (NC complex structure toolkit)
- **Tags**: noncommutative geometry, almost complex structure, bigraded forms, holomorphic modules, Koszul-Malgrange

**Summary**: Beggs-Smith define noncommutative analogues of almost complex structures, integrable complex structures, holomorphic curvature and cohomology, and holomorphic modules. An almost complex structure on a *-calculus (Omega^bullet A, d, *) is a degree-zero derivation J with J^2 = -1 on Omega^1 A, giving bigraded decomposition Omega^{p,q} A. Integrability (NC Newlander-Nirenberg): d Omega^{1,0} subset Omega^{2,0} + Omega^{1,1} <=> bar-d^2 = 0 on A <=> d = d + bar-d on Omega^1. Holomorphic modules (E, bar-nabla) with bar-nabla^2 = 0 form a category Hol(A) abelian when Omega^{0,1} A is right-flat; cohomology H^bullet(E, bar-nabla). Worked examples: CP^n_theta, CP^n_q, quantum flag manifolds.

**Key Results**:
- Almost-complex derivation J on *-calculus; bigraded Omega^{p,q}
- NC Newlander-Nirenberg theorem (integrability equivalences)
- Holomorphic modules and their cohomology
- Examples from quantum projective spaces and flag manifolds

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| (d xi)^* = d(xi^*), (xi wedge eta)^* = (-1)^{\|xi\| \|eta\|} eta^* wedge xi^* | *-calculus | Def 2.3 |
| J : Omega^bullet A -> Omega^bullet A, J^2 = -1 on Omega^1 | Almost complex structure | Def 2.6 |
| Omega^n A = oplus Omega^{p,q} A (p+q=n) | Bigraded decomposition | Lemma 2.10 |
| d Omega^{1,0} subset Omega^{2,0} + Omega^{1,1} <=> bar-d^2 = 0 | NC Newlander-Nirenberg | Lemma 3.2 |
| bar-nabla(ae) = bar-d a (x) e + a bar-nabla e | Bar-nabla connection | Def 4.1 |

**Dependencies**: Framework: provides rigorous NC-geometric language for the fibre data on Jensen-deformed SU(3), including compatibility with *-structure and [J, D_K] = 0.

---

### Paper 19: The Asymptotic Expansion of the Heat Kernel on a Compact Lie Group
- **File**: `19_2011_Heat_kernel_compact_Lie_group.md`
- **arXiv**: 1111.2643
- **Year**: 2011
- **Relevance**: HIGH
- **Tags**: heat kernel, compact Lie group, Duflo isomorphism, bi-invariant metric, SU(3)

**Summary**: Hong's closed-form heat kernel on a compact connected Lie group G with a bi-invariant metric. The Duflo isomorphism Duf: S(g)^g -> Z(g) realized as j . exp_* with j(X) = det^{1/2}(sinh(ad_X/2)/(ad_X/2)) maps the flat Lie-algebra Laplacian onto the Casimir plus a shift: Duf(Delta_g) = Cas + (1/24) tr_g(Cas) = Delta_G - <rho, rho>. The heat kernel on G in the exponential chart is k_t^{exp}(X) ~ h_t(X) j(X)^{-1} exp(tS/6) where h_t is the flat Gaussian and S = -(1/4) tr_g(Cas) is the scalar curvature. The heat-trace is Z(t) ~ vol(G) exp(tS/6) -- all Minakshisundaram-Pleijel coefficients in closed form.

**Key Results**:
- Closed-form heat kernel on any compact connected Lie group with bi-invariant metric
- Duflo isomorphism: Duf(Delta_g) = Cas + (1/24) tr_g(Cas) = Delta_G - <rho, rho>
- Scalar curvature S = -(1/4) tr_g(Cas)
- Heat kernel: k_t ~ h_t j^{-1} exp(tS/6)
- Heat trace: Z(t) ~ vol(G) exp(tS/6)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Delta_G = sum tilde X_i tilde X_i <-> Cas = sum X_i X_i in Z(g) | Laplacian = Casimir | Eq. 2.14 |
| Duf(Delta_g) = Cas + (1/24) tr_g(Cas) | Duflo image of flat Laplacian | Eq. 3.2 |
| (1/24) tr_g(Cas) = -<rho, rho> | Kostant identity | Eq. 3.3 |
| j(X) = det^{1/2}(sinh(ad_X/2)/(ad_X/2)) | Duflo Jacobian | Lemma 3.5 |
| S = -(1/4) tr_g(Cas) | Scalar curvature | Lemma 3.8 |
| k_t^{exp}(X) ~ h_t(X) j(X)^{-1} exp(tS/6) | Closed-form heat kernel | Theorem 3.9 |
| Z(t) ~ vol(G) exp(tS/6) | Heat trace | Corollary 3.10 |

**Dependencies**: Depends on 15 (heat kernel). Directly applicable to Jensen-deformed SU(3) fibre: short-circuits SDW series for the unperturbed piece.

---

### Paper 20: The Creation of Particles in an Expanding Universe (Parker Thesis)
- **File**: `20_1966_Parker_Cosmological_particle_creation_thesis.md`
- **arXiv**: 2507.05372 (repost)
- **Year**: 1966 (original thesis)
- **Relevance**: HIGH
- **Tags**: QFT in curved spacetime, cosmological particle creation, Bogoliubov transformation, FLRW

**Summary**: Parker's Harvard thesis -- foundational paper establishing QFT in curved spacetime. Smooth evolution of free scalar or spinor fields in an FLRW background from an in-Minkowski to an out-Minkowski era produces Bogoliubov mixing of positive- and negative-frequency parts: A_out = alpha A_in + beta* A_in^dagger with |alpha|^2 - |beta|^2 = 1, so real particles appear in the out vacuum. Adiabatic particle-number operator resolves UV divergences. Creation is always in particle-antiparticle pairs (equal matter and antimatter). Upper bounds on present-day creation rates: pi-mesons 10^{-105}, electrons 10^{-69}, protons 10^{-64} gm cm^{-3} sec^{-1}. Conformally invariant massless fields (photons, neutrinos) are not produced (Penrose); gravitons are produced (Ford-Parker 1977 extension because Einstein graviton in Lifshitz gauge is minimally coupled).

**Key Results**:
- Bogoliubov transformation as mechanism for gravitational particle creation
- Adiabatic particle number operator (UV-finite)
- Particle-antiparticle pair production (always in pairs; equal matter/antimatter)
- Upper bounds on present-day cosmological creation rates (unobservably small)
- Conformal invariance theorem: isotropic 3-flat expansion does not create photons/massless fermions
- Graviton creation (Ford-Parker 1977) -- Einstein graviton not conformally invariant

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| (Box + m^2 + xi R) phi = 0 | General-relativistic KG | Chap. 2 |
| ds^2 = -dt^2 + a(t)^2 delta_{ij} dx^i dx^j | FLRW 3-flat metric | Chap. 2 |
| A_out = alpha A_in + beta* A_in^dagger, \|alpha\|^2 - \|beta\|^2 = 1 | Bogoliubov transformation | Chap. 3 |
| <N_k>_{in-vac} = \|beta_k\|^2 | Particle-number expectation | Chap. 3 |

**Dependencies**: Depends on 04 (proper-time KG) conceptually. Upstream to 21, 24, 25, 26. Framework: foundational for S38 cosmogenesis / GGE relic formation.

---

### Paper 21: Fifty Years of Cosmological Particle Creation
- **File**: `21_2017_Parker_NavarroSalas_Fifty_years_cosmological_particle_creation.md`
- **arXiv**: 1702.07132
- **Year**: 2017
- **Relevance**: HIGH
- **Tags**: Parker mechanism, Ford-Parker gravitons, inflation anticipation, BICEP2

**Summary**: Historical interview-review framing Parker's mechanism, Hawking-radiation connection, Ford-Parker 1977 graviton production, Glenz-Parker 2009 smooth Minkowski-to-de-Sitter vacuum evolution, and the 1975 anticipation of inflationary reheating. Clarifies that the Einstein graviton is NOT conformally invariant (Lifshitz gauge reduces linearized Einstein to minimally coupled massless scalars for each polarization) -- so cosmological gravitons ARE produced, and their CMB B-mode polarization signature is what BICEP2/Planck target.

**Key Results**:
- Historical reconstruction of QFT-in-curved-spacetime origins
- Bogoliubov transformation as gravitational creation mechanism
- Ford-Parker 1977: graviton production in isotropic expansion
- Glenz-Parker 2009: Minkowski -> Bunch-Davies smooth vacuum evolution over 60 e-folds
- Sakharov's 1990 memoirs credit Parker's work

**Key Equations**:

Recalled from paper 20; no new equations.

**Dependencies**: Historical companion to 20. Cites/motivates 24, 25 (Schwinger analogues in dS). Framework: validates the substrate-framing picture (first-order transit, not singularity).

---

### Paper 24: Conformally Flat Gravitational Analogues to the Schwinger Effect
- **File**: `24_2025_Conformally_flat_gravitational_Schwinger_analogues.md`
- **arXiv**: 2602.18578
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: resummed heat kernel, Schwinger analogue, radiation-dominated cosmology, pair production

**Summary**: Franchino-Vinas-Mazzitelli-Pla develop heat-kernel resummed pair-creation calculations in conformally flat spacetimes. Weyl rescaling phi -> Omega^{(d-2)/2} phi maps the problem to a Minkowski scalar with Yukawa-type potential V = m^2 Omega^2 + (xi - xi_d) R Omega^2. For radiation-dominated cosmology (m^2 a^2 = b_0^2 tau^2, xi = xi_d), the heat kernel has an explicit form with poles at s = pi n / b_0 whose imaginary contributions give the decay probability P/2 = -V_0/[2(2 pi)^{d-1}] b_0^{(d-1)/2} (1 - 2^{(1-d)/2}) zeta_R((d+1)/2). Bogoliubov coefficients from parabolic cylinder functions confirm the heat-kernel calculation.

**Key Results**:
- Exact equivalence: scalar QFT in conformally flat spacetime <=> Yukawa in Minkowski (at effective-action level)
- Closed-form pair-creation probability in radiation-dominated universe (arbitrary d)
- Heat-kernel method matches Bogoliubov coefficient calculation
- New Schwinger-like gravitational analogues with Gaussian scale factor
- No mass-exponential suppression in radiation-dominated cosmology (contrast SQED)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| \|<out\|in>\|^2 = exp(-P), P = 2 Im Gamma | Vacuum persistence | Eq. 1 |
| V(tau, x) = m^2 Omega^2 + (xi - xi_d) R Omega^2 | Yukawa potential (gravitational) | Eq. 6 |
| K(x,x;s) = (4 pi s)^{-d/2} sqrt(b_0 s / (cos(b_0 s) sin(b_0 s))) exp(-b_0 tau^2 tan(b_0 s)) | Rad-dom heat kernel | Eq. 12 |
| P/2 = -V_0 / [2 (2 pi)^{d-1}] b_0^{(d-1)/2} (1 - 2^{(1-d)/2}) zeta_R((d+1)/2) | Closed-form pair probability | Eq. 15 |
| \|alpha_k\|^2 = 1 + exp(-4 pi kappa), kappa = k^2/(4 b_0) | Bogoliubov (rad-dom) | Eq. 26 |

**Dependencies**: Depends on 15 (heat kernel), 20 (Parker). Framework: directly relevant to S38 Schwinger-instanton duality and transit pair-creation.

---

### Paper 25: Backreaction-Inclusive Schwinger Effect in Flat and de Sitter Spacetimes
- **File**: `25_2024_Backreaction_Schwinger_effect_dS.md`
- **arXiv**: 2412.09436
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: Schwinger backreaction, Maxwell-Schrodinger, Gaussian state, plasma oscillations

**Summary**: Kaushal-Singh self-consistent semiclassical framework: classical electric field (C) + quantum complex scalar (Q) coupled via TDSE + Poisson bracket with effective Hamiltonian H_eff = H_1(C) + <psi| hat-H_2(Q,C) |psi>. Gaussian state ansatz psi_k = beta_k exp(-alpha_k |phi_k|^2) gives dot-alpha_k = -i alpha_k^2/2 + i omega_k^2(t)/2. Particle number <n_k> = |z_k|^2/(1-|z_k|^2) with z_k = (omega_k - alpha_k)/(omega_k + alpha_k). Backreaction yields immediate plasma-like oscillations in E-field and current; time-averaged particle number stays essentially constant. Extends to (1+3) dimensions and de Sitter backgrounds.

**Key Results**:
- Self-consistent Maxwell-Schrodinger semiclassical framework
- Immediate plasma oscillations with backreaction (contrast adiabatic methods)
- Time-averaged particle number constant despite oscillations
- (1+1) and (1+3) dimensions; Minkowski and de Sitter
- No need for adiabatic regularization; lattice UV cutoff handles normal ordering

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| hat-H_2 psi = i hbar d_t psi | TDSE for matter | Eq. 1 |
| dot-C = {C, H_eff} | Classical field evolution | Eq. 2 |
| dot-alpha_k = -i alpha_k^2/2 + i omega_k^2(t)/2 | Gaussian-state equation | Eq. 20 |
| <n_k> = \|z_k\|^2 / (1 - \|z_k\|^2) | Instantaneous particle number | Eq. 26 |
| -dE/dt = <hat-J^mu_Q> | Backreaction equation | Eq. 29 |

**Dependencies**: Depends on 20 (Parker), 24 (heat kernel Schwinger analogues). Framework: direct tool for Feynman Test Step 6 (unitarity/backreaction consistency) in the transit-cosmogenesis calculation.

---

### Paper 26: The Stochastic Schwinger Effect
- **File**: `26_2025_Stochastic_Schwinger_effect.md`
- **arXiv**: 2510.14468
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: stochastic gauge fields, pair production, preheating, magnetogenesis

**Summary**: Garcia-Consuegra-Maleknejad extend the Schwinger mechanism to statistically fluctuating gauge-field backgrounds. Gauge field promoted to operator-valued Gaussian stochastic process with <A_mu> = 0 and correlator <A_mu(x) A_nu(y)>_s = G_{mu nu}(x-y). Combined quantum + stochastic average <...> = int D[A] P[A] <0_in|...|0_in>_A. Closed-form analytic expressions for vacuum decay rate and number density of charged pairs, for both scalar and fermionic matter. Kinematic threshold omega^2 > |q|^2 + 4 m^2: only background modes above twice the rest mass contribute. Applications to astrophysical plasmas, dark photon DM, axion-gauge reheating.

**Key Results**:
- Stochastic Schwinger mechanism with vanishing mean field <A_mu> = 0
- Closed-form analytic expressions for decay rate and number density
- Kinematic threshold omega^2 > |q|^2 + 4 m^2
- Framework applies to stationary and non-stationary (windowed Fourier) backgrounds
- Perturbative contribution vanishes for strictly constant EM field (as expected)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| P_decay = 1 - P ~ 2 Im Gamma = 2 int d^4x w(x) | Decay probability | Eq. 2.10 |
| <A_mu(x)>_s = 0, <A_mu(x) A_nu(y)>_s = G_{mu nu}(x-y) | Stochastic mean + correlator | Eq. 3.1 |
| P^b_decay = (g^2 Q^2 pi/3) int_q Theta(-q^2 - 4 m^2)(1 + 4m^2/q^2)^{3/2} <-F_{mu nu}(q) F^{mu nu}(-q)> | Stationary scalar probability | Eq. 3.16 |

**Dependencies**: Depends on 20 (Parker), 24 (heat-kernel Schwinger). Framework: relevant to computing pair-production rates in stochastic substrate gauge-field environments.

---

### Paper 27: Exactly Solvable Richardson-Gaudin Models
- **File**: `27_2004_Dukelsky_Pittel_Sierra_Richardson_Gaudin_exactly_solvable.md`
- **arXiv**: nucl-th/0405011
- **Year**: 2004
- **Relevance**: CRITICAL
- **Tags**: Richardson-Gaudin, Bethe ansatz, pairing model, BCS, electrostatic mapping

**Summary**: Dukelsky-Pittel-Sierra Colloquium on R-G integrable models. The Richardson ansatz |Psi> = B_1^dagger ... B_M^dagger |nu> with B_alpha^dagger = sum_l (2 epsilon_l - E_alpha)^{-1} A_l^dagger diagonalizes the pairing Hamiltonian H_P = sum epsilon_l n_l + (g/2) sum A^dagger A; the Richardson equations determine E_alpha. Cambiaggio-Rivas-Saraceno provide L commuting conserved charges R_l confirming integrability. Three Gaudin families (rational, trigonometric, hyperbolic) are unified via X_{ij} = gamma/sin[gamma(eta_i - eta_j)]. Richardson equations map to 2D classical electrostatics; large-N limit recovers BCS.

**Key Results**:
- Richardson's exact solution for general pairing Hamiltonian
- Integrability: L commuting charges R_l (Cambiaggio-Rivas-Saraceno)
- Three families: rational (gamma=0), trigonometric (gamma=1), hyperbolic (gamma=i)
- Electrostatic mapping: Richardson equations = 2D charge equilibrium
- BCS emerges in large-N limit of exact solution
- Extension to bosons (SU(1,1))

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| H_P = sum epsilon_l n_l + (g/2) sum A^dagger A | Pairing Hamiltonian | Eq. 4 |
| \|Psi> = B_1^dagger ... B_M^dagger \|nu>, B_alpha^dagger = sum_l (2 epsilon_l - E_alpha)^{-1} A_l^dagger | Richardson eigenstate | Eqs. 7, 8 |
| 1 - 4g sum d_l/(2 epsilon_l - E_alpha) + 4g sum 1/(E_alpha - E_beta) = 0 | Richardson equations | Eq. 9 |
| R_l = K^0_l + 2g sum (epsilon_l - epsilon_{l'})^{-1} [...] | CRS conserved charges | Eq. 24 |
| X_{ij} = gamma/sin[gamma(eta_i - eta_j)], Y_{ij} = gamma cot[gamma(eta_i - eta_j)] | Unified Gaudin solutions | Eq. 30 |

**Dependencies**: Foundation for 28 (GGE), 29 (Claeys), 30. Framework: central to S38 GGE permanence claim; 8 conserved charges on Dirac spectrum.

---

### Paper 28: Generalized Gibbs Ensemble in Integrable Lattice Models
- **File**: `28_2016_Vidmar_Rigol_GGE_integrable_lattice.md`
- **arXiv**: 1604.03990
- **Year**: 2016
- **Relevance**: CRITICAL
- **Tags**: GGE, integrability, thermalization, XX model, transverse-field Ising

**Summary**: Vidmar-Rigol review of 10 years of GGE research. The generalized Gibbs ensemble rho_GGE = Z_GGE^{-1} exp(-sum_k lambda_k I_k) maximizes entropy subject to the extensive set of integrability-protected conserved charges I_k. Lagrange multipliers are fixed by matching: <psi_0| I_k |psi_0> = Tr[rho_GGE I_k]. GGE successfully describes equilibrated observables in XX, TFI, XXZ, Lieb-Liniger, Luttinger, sine-Gordon. New result (this review): GGE describes TFI spin-spin correlations over the entire system without real-space tracing. Generalized eigenstate thermalization in both XX and TFI (eigenstates with similar conserved-quantity distributions have similar few-body observables).

**Key Results**:
- GGE prediction works for integrable systems after equilibration
- Lagrange multipliers fixed by matching initial-state charge expectations
- GGE works without real-space subsystem tracing (new TFI result)
- Generalized eigenstate thermalization in XX and TFI
- Distinction: hard-core bosons (interacting, equilibrate to GGE) vs noninteracting fermions

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| rho_GGE = Z_GGE^{-1} exp(-sum_k lambda_k I_k) | GGE density matrix | Eq. 18 |
| <psi_0| I_k |psi_0> = Tr[rho_GGE I_k] | Matching condition | Sec. 2.3 |
| rho_DE = sum_n \|c_n\|^2 \|n><n\| | Diagonal ensemble | Eq. 15 |
| epsilon_k = sqrt(h^2 + 2 h J cos k + J^2) | TFI Bogoliubov energy | Eq. 9 |

**Dependencies**: Depends on 27 (R-G integrability). Framework: CRITICAL for S38 Ordered Veil claim (integrability-protected non-thermal relic).

---

### Paper 29: Richardson-Gaudin Models and Broken Integrability (Claeys Thesis)
- **File**: `29_2018_Claeys_Richardson_Gaudin_broken_integrability_thesis.md`
- **arXiv**: 1809.04447
- **Year**: 2018
- **Relevance**: CRITICAL
- **Tags**: Richardson-Gaudin, eigenvalue-based framework, Read-Green resonances, Floquet, p+ip

**Summary**: Claeys PhD thesis compiling 12 papers on R-G integrable models and their breaking. Builds R-G models from non-interacting su(2) chains via conserved charges Q_i = S^z_i + g sum[X_{ij}(S^+ S^- + S^- S^+) + Z_{ij} S^z S^z]; Gaudin integrability equations; XXZ constraint X^2 - Z^2 = Gamma. Eigenvalue-based framework avoids Bethe-root singularities. Physical realizations: central spin model, reduced BCS, p_x + i p_y-wave topological superconductor (Read-Green resonances). Part III: variational methods for broken integrability (periodic driving, Floquet resonances, RG-Configuration Interaction for nuclear pairing).

**Key Results**:
- Eigenvalue-based framework for R-G (no rapidity singularities)
- Determinant structures for inner products and form factors
- Dicke model as contraction limit of pseudo-deformed R-G
- Read-Green resonances in p+ip topological superconductor
- Variational GCI for integrability-breaking
- Floquet resonances in driven Heisenberg / central spin models
- Pre-thermalization regime preserved by near-integrable structure

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Q_i = S^z_i + g sum [X_{ij}(S^+ S^- + S^- S^+) + Z_{ij} S^z S^z] | R-G conserved charges | Eq. 2.12 |
| X_{ij} + X_{ji} = 0, Z_{ij} + Z_{ji} = 0; X_{ij} X_{jk} - X_{ik}(Z_{ij} + Z_{jk}) = 0 | Gaudin equations | Eqs. 2.13-2.14 |
| [S^alpha(u), S^beta(v)] = i(...) | GGA commutators | Eqs. 2.18-2.21 |
| X(u,v)^2 - Z(u,v)^2 = Gamma | XXZ constraint | Eq. 2.26 |
| \|v_1...v_N> = prod S^+(v_a) \|0> | Bethe state | Eq. 2.32 |

**Dependencies**: Depends on 27 (R-G review), 28 (GGE). Framework: CRITICAL for S38 eight-conserved-charges picture and broken-integrability analysis of transit perturbations.

---

### Paper 30: Synchronization in Time-Varying Random Networks (filename mismatch)
- **File**: `30_2019_Claeys_Quench_dynamics_nonintegrable_pairing.md`
- **arXiv**: 1811.09591 (Faggian et al. Kuramoto paper -- NOT the intended Claeys quench-dynamics content)
- **Year**: 2018
- **Relevance**: HIGH (as proxy; actual framework-relevant Claeys content still in 29)
- **Tags**: Kuramoto model, time-varying network, timescale analysis, synchronization

**Summary**: Note: the filename assigned by the orchestrator maps to a Kuramoto/synchronization paper (Faggian-Ginelli-Rosas-Levnajic 2018), not a Claeys quench-dynamics paper. Actual content: Kuramoto oscillators on Erdos-Renyi networks with random rewiring; partial synchronization at vanishing connectivity when coupling is strong and rewiring is fast. Three-timescale analysis (local sync tau_LS ~ 1/(2 epsilon); local desynch tau_LD ~ pi/(2 sqrt(2) sigma); effective rewiring tau_ER ~ T/q) predicts the transition line T_c(q) ~ pi q/(2 sqrt(2) sigma). Fast-switching limit recovers globally coupled Kuramoto with effective coupling epsilon(1 - e^{-q}).

**Key Results**:
- Partial synchronization achievable in vanishing-connectivity networks with fast rewiring
- Three-timescale framework for dynamical consistency
- Fast-switching limit -> globally coupled Kuramoto
- Mean-field critical exponent beta = 1/2

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| dot-phi_i = omega_i + (epsilon/m^t_i) sum A^t_{ij} sin(phi_j - phi_i) | Kuramoto dynamics on time-varying graph | Eq. 1 |
| tau_LD ~ pi/(2 sqrt(2) sigma) | Local desynch time | Eq. 9 |
| tau_ER ~ T/q | Effective rewiring time | Eq. 13 |
| T_c(q) ~ pi q/(2 sqrt(2) sigma) | Transition line | Eq. 14 |

**Dependencies**: Orchestrator action recommended: re-assign the intended arXiv ID (Claeys-Caux 1708.07324 or Claeys et al. 1712.03117). Framework relevance via timescale-analysis analogy to transit dynamics.

---

### Paper 31: Asymptotic Safety in Lorentzian Quantum Gravity
- **File**: `31_2023_Lorentzian_asymptotic_safety.md`
- **arXiv**: 2310.20603
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: asymptotic safety, Lorentzian FRGE, fixed point, BV formalism, Hadamard state

**Summary**: D'Angelo's first Lorentzian FRGE demonstration of a non-trivial UV fixed point for quantum gravity in the Einstein-Hilbert truncation. Wetterich-type flow on globally hyperbolic spacetimes with BV formalism and local mass-type regulator preserving Lorentz invariance and causality. UV finiteness via Hadamard subtraction. State dependence tracked; universal (state-independent) terms alone produce a Reuter-type fixed point (g*, lambda*) = (1.15, 0.42) with complex-conjugate critical exponents theta_{1,2} = 5.11 +/- 11.59 i (two relevant directions).

**Key Results**:
- First Lorentzian FRGE fixed point in gravity
- Covariant formalism on globally hyperbolic spacetimes
- UV finite via Hadamard parametrix subtraction
- (g*, lambda*) = (1.15, 0.42), theta_{1,2} = 5.11 +/- 11.59 i
- Different numerical values from ADM/Euclidean frameworks (state-dependent)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| I = I_EH + I_af + gamma Psi, I_EH = 2 zeta^2 int sqrt(-g) (R - 2 Lambda) | Classical action | Eq. 1 |
| d_k Gamma_k = (i/2) int Tr[d_k q_k : G_k :] | Lorentzian FRGE | Eq. 7 |
| k d_k g_k = (eta_N + 2) g_k | Beta function for g | Eq. 25 |
| (g*, lambda*) = (1.15, 0.42); theta_{1,2} = 5.11 +/- 11.59 i | Fixed point + critical exponents | Phase diagram |

**Dependencies**: Depends on 07 (RG), 09 (perturbative QG). Framework: adversarial UV completion to the spectral-action approach.

---

### Paper 32: Self-Consistent Graviton Spectral Function in Lorentzian Quantum Gravity
- **File**: `32_2025_Graviton_spectral_function_Lorentzian_QG.md`
- **arXiv**: 2507.22169
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: spectral function, Kallen-Lehmann, unitarity, asymptotic safety, on-shell RG

**Summary**: Pawlowski-Reichert-Wessely first fully self-consistent Lorentzian graviton spectral function in quantum gravity. Spectral RG with on-shell renormalization (m_h^2 = k^2, Z_h = 1) feeds full spectral function (including scattering continuum) into diagrams. Kallen-Lehmann representation G_{hh}(p^2) = int rho_h(lambda)/(lambda^2 + p^2); parametrization rho_h(lambda) = 2 pi delta(lambda^2 - m_h^2) + theta(lambda^2 - 4 m_h^2) f_h(lambda) -- massless one-graviton peak + multi-graviton continuum. Positive spectral function; UV decay f_h(lambda) ~ 1/[lambda^2 log^3 lambda^2] (integrable). Total spectral weight z_spec ~ 1.486; after physical rescaling rho^(ph) = rho/z_spec, unit sum rule int rho^(ph) = 1 is satisfied. Newton-coupling UV fixed point g* = 760 pi/2499 ~ 0.955. IR coefficient A_h = 61/(60 pi) ~ 0.32.

**Key Results**:
- First self-consistent Lorentzian graviton spectral function
- Positive spectral function (unitarity-compatible)
- UV decay 1/[lambda^2 log^3 lambda^2] (finite spectral weight)
- On-shell renormalization gives unit physical sum rule
- UV fixed point g* ~ 0.955 (harmonic gauge)
- IR coefficient A_h = 61/(60 pi)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| G_{hh}(p^2) = int rho_h(lambda)/(lambda^2 + p^2) | Kallen-Lehmann representation | Eq. 12 |
| rho_h(lambda) = (1/Z_h)[2 pi delta(lambda^2 - m_h^2) + theta(lambda^2 - 4 m_h^2) f_h(lambda)] | Parametrization | Eq. 14 |
| int rho(lambda) = 1 | Sum rule | Eq. 15 |
| d_t g = 2 g - (2499/380 pi) g^2; g* = 760 pi/2499 ~ 0.955 | Newton beta function + UV fixed point | Eqs. 23-24 |
| f_h(lambda -> infty) = c^UV/[lambda^2 log^3 lambda^2] | UV decay | Eq. 29 |
| z_spec = 1 + int lambda f_h(lambda) ~ 1.486; int rho^(ph) = 1 | Spectral weight + physical sum rule | Eqs. 30, 32 |
| A_h = 61/(60 pi) ~ 0.32 | IR coefficient | Eq. 33 |

**Dependencies**: Depends on 31 (Lorentzian FRGE). Framework: benchmark for any emergent graviton derived from D_K spectral data.

---

## Cross-Paper Equation Concordance

### Proper Time / Heat Kernel Bridge
The Schwinger-DeWitt proper-time representation appears in 04 (Eq. A9, Lorentzian), 15 (Sec. 1, Euclidean), 16 (Eq. 2.14, spectral action moments), 19 (Theorem 3.9, closed-form on compact Lie groups), 24 (Eq. 12, resummed in conformally-flat), with the identification u_0 -> -i s converting Feynman's fifth-parameter integral to the Euclidean heat-kernel integral. All spectral-action computations on Jensen-deformed SU(3) inherit this bridge.

### Seeley-DeWitt Coefficients a_0, a_2, a_4
Appear in 15 (Eqs. 4.26-4.28, master reference), 16 (Eqs. 2.14-2.16, applied to SM spectral triple), 19 (Theorem 3.9, resummed e^{tS/6} on compact Lie groups), 24 (Eq. 12, resummed in conformally flat backgrounds). Normalization: all use (4 pi)^{-n/2} prefactor with Gilkey coefficients. Framework rule: import from 15; apply via 16; short-circuit SU(3) piece via 19; check against 24 for cosmological backgrounds.

### Bogoliubov Coefficients
Appear in 20 (Chap. 3, FLRW spacetime), 21 (recall of Parker 1969 result), 24 (Eq. 26, parabolic cylinder functions in radiation-dominated), 28 (Eq. 8, quantum quench between pre/post Hamiltonians). The relation |alpha|^2 - |beta|^2 = 1 (unitarity) is universal; particle-number expectation <N> = |beta|^2 in the in-vacuum is the standard extraction formula. Framework: at the fold, 59.8 quasiparticle pairs correspond to sum of |beta_k|^2 over the relevant mode spectrum.

### Richardson Equations
Appear in 27 (Eq. 9, pairing model), 29 (Eqs. 2.12-2.14, broken-integrability generalization). Eigenvalue form: 1 - 4g sum d_l/(2 epsilon_l - E_alpha) + 4g sum 1/(E_alpha - E_beta) = 0. Electrostatic mapping (Table I in 27) provides a 2D visualization tool.

### GGE Density Matrix
Appears in 28 (Eq. 18): rho_GGE = Z^{-1} exp(-sum lambda_k I_k) with matching <psi_0 | I_k | psi_0> = Tr[rho_GGE I_k]. This is the master object for the Ordered Veil / S38 paradigm. The conserved charges I_k are the R_l of 27 (Eq. 24) and the Q_i of 29 (Eq. 2.12).

### Vacuum Decay Probability (Schwinger-type)
Appears in 02 (Eq. 30, one-loop L), 24 (Eqs. 14-15, radiation-dominated closed form), 25 (Eq. 29, backreaction-inclusive), 26 (Eqs. 3.16-3.17, stochastic). Common form: P_decay = 1 - exp(-2 Im Gamma) ~ 2 Im Gamma in the weak-field regime.

### Kallen-Lehmann Spectral Representation
Appears in 06 (Sec. 7, Dyson unitarity), 32 (Eq. 12, graviton self-consistency). Framework: any emergent graviton from D_K spectral moments must admit a positive, normalizable spectral function.

### One-Loop Ward / Gauge Invariance Identities
Appear in 03 (Eq. 34, fermion Ward identity in QED), 06 (Sec. 6, Dyson's Z_1 = Z_2), 17 (Eq. 3, fermion Ward; Eq. 9, quantum gauge Ward via divided differences). The spectral-action analog (17) is structurally distinct from local QFT (03, 06) because the gauge propagator 1/f'[lambda_k, lambda_l] is bounded (no UV divergence from the propagator alone).

## Notation Conventions

- **tau**: Jensen deformation parameter (not proper time). Proper time in 04, 15 denoted u_0, s respectively.
- **D**: Dirac operator (generic); D_K: Jensen-deformed SU(3) Dirac operator (155,984 eigenvalues at L_max=10)
- **a_n**: Seeley-DeWitt coefficients (Gilkey normalization with (4 pi)^{-n/2} prefactor)
- **K(t; x, y; D)**: heat kernel; K_+(2, 1): Feynman propagator (different object, same symbol across papers; context disambiguates)
- **Omega_{mu nu}**: bundle curvature (15, 16), also conformal factor (24, 25) -- disambiguate by context
- **beta_k, alpha_k**: Bogoliubov coefficients with |alpha|^2 - |beta|^2 = 1
- **G_F**: Fermi coupling (08); G_{kl}: gauge propagator in spectral action (17); G_N: Newton's constant (09, 31, 32)
- **xi**: scalar-curvature coupling (conformal value xi_d = (n-2)/[4(n-1)]); not to be confused with gauge parameter
- **E**: endomorphism in Laplace-type operator D = -nabla^2 - E (15, 16); electric field (25, 26); often context-clear
- **rho, rho_h, rho_GGE**: matter density; graviton spectral function; GGE density matrix respectively
- **<V_1,..., V_n>**: cyclic bracket in spectral action (17)
- **I_k**: conserved charge in GGE (28); not to be confused with I_+ Feynman propagator (04)
- **S**: action (everywhere); scalar curvature (19); S-matrix (05, 06) -- context-clear
- **f'[lambda_k, lambda_l]**: divided difference of f' (17); central to bounded propagator

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 15 | Seeley-DeWitt a_0, a_2 coefficients on D_K | Yes (bare) | computations (S11+, S36+) |
| 16 | Spectral action -> bare Einstein-Hilbert via a_2 | Yes | computation (D_K spectrum, S11+); two-layer gravity S50-S51 |
| 16 | SU(5) GUT boundary alpha_3 = alpha_2 = (5/3) alpha_1 | Structural | Computation identified at Jensen fold |
| 16 | m_H ~ 160-180 GeV (CC original bound) | Superseded | Project predicts 131.8 GeV (S42, KK threshold correction) |
| 17 | Cyclic-cocycle expansion + quantum Ward identity | Not yet | Pending Computation C (quantum spectral action) |
| 19 | Heat kernel on compact Lie group via Duflo | Not yet | Pending application to Jensen-deformed SU(3) |
| 20 | Parker Bogoliubov coefficients in FLRW | Partial | computation transit-einstein S64+ |
| 21 | Ford-Parker graviton creation | Not yet | Pending for LISA GW estimate |
| 24 | Resummed heat kernel (radiation-dominated) | Not yet | Pending; relevant to S38 |
| 25 | Self-consistent backreaction | Not yet | Pending for transit dynamics |
| 27 | Richardson-Gaudin R_l conserved charges | Yes (N=8) | S38 (8 conserved charges on Dirac spectrum) |
| 28 | GGE density matrix rho_GGE | Structural | S38 Ordered Veil claim |
| 29 | Eigenvalue-based R-G framework | Not yet | Pending; useful for L_max = 10 spectrum |
| 32 | Graviton spectral function + sum rule | Not yet | Benchmark for emergent graviton from D_K |
| 06 | Power counting D = 4 - (3/2) E_e - E_gamma | Standard | Applied as background |
| 07 | Wilson-Fisher fixed point nu = 1/2 + epsilon/12 | Standard | Applied as background |
| 02 | [J, D_K] = 0 (CPT from real structure) | Yes (machine eps) | Permanent result (pre-S34) |
| 03 | Anomalous moment + Lamb shift | Standard | Applied as background |
| 10 | Superfluidity from permutation cycles | Structural | Template for framework substrate |
| 12 | Bell-type bound (classical HV) | Standard | Background constraint |
