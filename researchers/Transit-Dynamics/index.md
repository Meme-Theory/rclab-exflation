# Transit-Dynamics Paper Index

**Researcher**: Multiple authors (Parker, Birrell-Davies, Mukhanov, Kofman-Linde-Starobinsky, Kibble, Zurek, Calzetta-Hu, Barcelo-Liberati-Visser, Steinhauer, Berges, Rigol, Volovik, et al.)
**Papers**: 30 (1951-2024), sourced from foundational texts and key publications
**Primary domain**: Non-equilibrium particle production, Bogoliubov transformations, parametric resonance, Kibble-Zurek mechanism, GGE formation, analog gravity, primordial power spectrum
**Project relevance**: Provides the complete mathematical toolkit for transit dynamics through the van Hove fold: Bogoliubov coefficients for Parker pair creation, Mathieu/Floquet analysis for parametric amplification, KZM scaling for defect formation in the impulse regime, Schwinger-Keldysh formalism for non-equilibrium evolution, GGE permanence for integrable post-transit states, and observational constraints from CMB power spectrum

---

## Dependency Graph

```
BOGOLIUBOV & PARTICLE CREATION FOUNDATIONS
  01 (Parker 1966) --> 02 (Birrell-Davies 1982)
  01 --> 03 (Mukhanov-Chibisov 1981)
  01 --> 04 (Kofman-Linde-Starobinsky 1994)
  01 --> 12 (Unruh 1981)
  14 (Schwinger 1951) --> 01 [tunneling/WKB methods]
  20 (Bogoliubov-Valatin 1958) --> 01 [canonical transformation formalism]
  20 --> 04 [Bogoliubov approach to parametric resonance]
  02 --> 08 (Barcelo-Liberati-Visser 2005)
  02 --> 15 (Jacobson 1995)

PREHEATING & PARAMETRIC AMPLIFICATION
  04 (Kofman-Linde-Starobinsky) --> 17 (Amin 2003)
  04 --> 25 (Bassett 1997)
  04 --> 29 (Tranberg 2006)
  17 --> 29 [backreaction validation]
  25 --> 04 [geometric coupling alternative]

KIBBLE-ZUREK & PHASE TRANSITIONS
  05 (Kibble 1976) --> 06 (Zurek 1985)
  06 --> 11 (del Campo-Zurek 2005)
  06 --> 24 (Dziarmaga 2005)
  11 --> 24 [quantum KZM exact solutions]

NON-EQUILIBRIUM QFT & THERMALIZATION
  07 (Calzetta-Hu 2008) --> 10 (Berges 2002)
  07 --> 16 (Kamenev 1999)
  10 --> 26 (Berges nPI 2010)
  16 --> 07 [Keldysh contour foundations]
  04 --> 10 [preheating thermalization problem]

ANALOG GRAVITY & LABORATORY TESTS
  12 (Unruh 1981) --> 08 (Barcelo-Liberati-Visser 2005)
  08 --> 09 (Steinhauer 2016)
  12 --> 09 [experimental realization]
  15 (Jacobson 1995) --> 08 [thermodynamic emergence]
  27 (Volovik 2001) --> 08 [3He-A as parent system]
  27 --> 09 [superfluid analog predictions]

GGE & PRETHERMALIZATION
  13 (Rigol 2007) --> 21 (Langen 2012)
  13 --> 23 (Calabrese-Essler 2011)
  10 (Berges) --> 13 [prethermalization plateau --> GGE]
  21 --> 13 [experimental validation]
  07 --> 13 [Kadanoff-Baym --> GGE steady state]

POWER SPECTRUM & OBSERVATIONAL CONSTRAINTS
  03 (Mukhanov-Chibisov) --> 18 (Starobinsky R2)
  03 --> 19 (Motohashi constant-roll)
  03 --> 22 (Liddle PCA reconstruction)
  03 --> 30 (Kinney constraints)
  18 --> 30 [R2 prediction vs data]
  28 (Vafa swampland) --> 18 [constraints on inflation models]

CROSS-THEME LINKS
  01,02,12  --[Bogoliubov framework]--> 04,17,25 [parametric resonance uses same coefficients]
  04,17     --[non-thermal output]--> 13,21,23 [created particles form GGE, not thermal]
  05,06,11  --[defect formation]--> 13 [defects = GGE quasiparticles in spectral space]
  08,09,12  --[experimental validation]--> 01,02 [analog gravity confirms Bogoliubov predictions]
  07,10,16  --[formalism]--> 04,13 [Schwinger-Keldysh tracks evolution to GGE]
  27        --[parent system]--> 08,09 [3He-A is not just analog but progenitor]
  18,19     --[beyond slow-roll]--> 03,30 [exact solutions vs approximations]
```

## Topic Map

### Bogoliubov & Particle Creation Foundations
Papers: 01, 02, 14, 20
The mathematical foundation for all transit dynamics. Parker (01) establishes that time-dependent metrics produce real particles via Bogoliubov mixing of positive and negative frequency modes. Birrell-Davies (02) systematizes the formalism: Fock-space quantization, adiabatic vacua, WKB expansion, Green's function approach, zeta-function regularization. Schwinger (14) provides the complementary perspective of pair creation from strong fields via tunneling, with the proper-time method and critical field strength. Bogoliubov-Valatin (20) gives the fermionic canonical transformation that diagonalizes pairing Hamiltonians, producing quasiparticle excitations with energy gap structure. Together these four papers define the mode equation u_k'' + omega_k^2(t) u_k = 0, the unitarity condition |alpha|^2 - |beta|^2 = 1, and the particle number N_k = |beta_k|^2.

### Cosmological Perturbations & Mode Equations
Papers: 03, 18, 19
Mukhanov-Chibisov (03) derives the primordial power spectrum from quantum vacuum fluctuations amplified by inflation, establishing the Mukhanov-Sasaki equation and the Bunch-Davies vacuum. Starobinsky (18) shows R^2 inflation produces near-scale-invariant spectrum without slow-roll, using exact numerical solutions. Motohashi (19) develops constant-roll inflation with exact analytical mode functions, demonstrating that diverse spectral indices arise beyond slow-roll. Critical for the framework: these papers show that scale-invariance can emerge from geometry, not just from fine-tuned potentials.

### Preheating & Parametric Amplification
Papers: 04, 17, 25, 29
Kofman-Linde-Starobinsky (04) introduces parametric resonance in preheating: the oscillating inflaton drives a Mathieu equation for coupled fields, producing exponential particle creation in instability bands. Amin (17) develops detailed numerical/analytical treatments of backreaction, rescattering, and non-thermal spectra. Bassett (25) shows geometric reheating via non-minimal coupling to curvature. Tranberg (29) validates the theory with large-scale lattice simulations. The key structural insight: the Mathieu equation is a specific instance of the mode equation with periodic omega_k(t), and Floquet theory determines the instability bands.

### Kibble-Zurek Mechanism & Phase Transitions
Papers: 05, 06, 11, 24
Kibble (05) establishes that rapid phase transitions produce topological defects from causally disconnected regions. Zurek (06) quantifies defect density via critical exponents: n ~ (tau_Q)^{-d*nu/(nu*z+1)}. del Campo-Zurek (11) extends to the impulse regime (ultra-fast quenches) where defect density saturates, and to first-order transitions. Dziarmaga (24) provides exact solutions for quantum phase transition dynamics in the Ising model. The impulse-regime saturation from del Campo is directly relevant: the van Hove fold transit is deep in this regime.

### Non-Equilibrium QFT & Thermalization
Papers: 07, 10, 16, 26
Calzetta-Hu (07) develops the Schwinger-Keldysh closed-time-path formalism for non-equilibrium quantum fields, deriving Kadanoff-Baym equations for occupation number evolution. Berges (10) introduces nPI effective actions for non-perturbative thermalization, discovering prethermalization plateaus. Kamenev (16) systematizes the Keldysh formalism with real-time diagrams. Berges et al. (26) extend nPI methods to control secular corrections. The central result: prethermalization is universal, and integrable systems remain in GGE states indefinitely.

### Analog Gravity & Laboratory Tests
Papers: 08, 09, 12, 15, 27
Unruh (12) discovers that sonic black holes exhibit Hawking radiation, establishing the acoustic metric analogy. Barcelo-Liberati-Visser (08) comprehensively reviews analog gravity, proving universality and robustness of Hawking effect against dispersion. Steinhauer (09) provides first experimental observation of thermal Hawking radiation in a BEC, validating the Bogoliubov framework. Jacobson (15) derives Einstein's equations from horizon thermodynamics, establishing gravity as emergent. Volovik (27) demonstrates that superfluid 3He-A is a parent system (not mere analog) whose quasiparticle physics directly exhibits cosmological phenomena.

### GGE & Prethermalization
Papers: 13, 21, 23
Rigol (13) proves that integrable quantum systems after sudden quench relax to the generalized Gibbs ensemble, not thermal equilibrium. Langen (21) experimentally observes prethermalization and GGE in cold atoms, confirming timescale separation. Calabrese-Essler (23) solve the quantum quench problem exactly in the transverse-field Ising chain. These papers provide the theoretical and experimental foundation for the framework's central claim: the GGE relic is permanent because the spectral system is integrable.

### Power Spectrum & Observational Constraints
Papers: 22, 28, 30
Liddle (22) develops model-independent PCA reconstruction of the primordial power spectrum. Vafa (28) proposes swampland constraints on inflation, motivating alternatives to slow-roll. Kinney (30) compiles Planck constraints: n_s = 0.9661 +/- 0.0040, alpha consistent with zero, r < 0.058, f_NL consistent with zero. These define the observational target the framework must match.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Bogoliubov coefficients, mode equations, particle number | 01, 02, 20 | CRITICAL |
| Primordial power spectrum, Mukhanov-Sasaki equation | 03, 18, 30 | CRITICAL |
| Parametric resonance, Mathieu equation, preheating | 04, 17 | CRITICAL |
| GGE formation, prethermalization, integrable quenches | 13, 21, 23 | CRITICAL |
| Schwinger-Keldysh formalism, Kadanoff-Baym equations | 07, 16 | CRITICAL |
| Analog gravity, acoustic horizons, BEC Hawking radiation | 08, 09, 12 | CRITICAL |
| Volovik 3He-A parent system, emergent metric | 27 | CRITICAL |
| Kibble-Zurek scaling, impulse regime, defect density | 05, 06, 11 | HIGH |
| nPI thermalization, secular corrections | 10, 26 | HIGH |
| Emergent gravity, horizon thermodynamics | 15 | HIGH |
| Beyond slow-roll (constant-roll, R^2) | 18, 19 | HIGH |
| Observational constraints (n_s, r, f_NL) | 22, 28, 30 | HIGH |
| Schwinger pair creation, tunneling, critical field | 14 | MEDIUM |
| Lattice preheating simulations | 29 | MEDIUM |
| Geometric reheating, non-minimal coupling | 25 | MEDIUM |
| Dziarmaga exact quantum KZM solutions | 24 | MEDIUM |
| Swampland constraints on inflation | 28 | MEDIUM |

---

## Paper Entries

### Paper 01: Gravitational Particle Creation in Expanding Universe
- **File**: `01_1966_Parker_Gravitational_Particle_Creation.md`
- **Author**: Leonard E. Parker
- **Year**: 1966
- **Relevance**: CRITICAL
- **Tags**: Bogoliubov transformation, FLRW, adiabatic vacuum, particle number, WKB

**Summary**: Parker's thesis establishes that the quantum vacuum is unstable in expanding spacetime. Mode functions in FLRW backgrounds are related by Bogoliubov transformation b_k = alpha_k a_k + beta_k a_k^dagger, with particle number N_k = |beta_k|^2. The adiabatic condition |d(omega)/dt| << omega^2 determines when creation is significant.

**Key Results**:
- Particle number per mode: N_k = |beta_k|^2
- Adiabatic violation triggers creation when H ~ omega_k
- |beta_k|^2 ~ exp(-2*pi*omega_k/H) for adiabatic modes; O(1) for rapid transitions
- Mechanism is universal: applies to any non-stationary metric

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Mode decomposition | phi = Sum_k [a_k u_k + a_k^dagger u_k*] | Sec. 2 |
| Bogoliubov transformation | b_k = alpha_k a_k + beta_k a_k^dagger | Sec. 2 |
| Unitarity | \|alpha_k\|^2 - \|beta_k\|^2 = 1 | Sec. 2 |
| Particle number | N_k = |beta_k|^2 | Sec. 3 |
| Adiabatic condition | \|d(omega)/dt\| << omega^2 | Sec. 3 |

**Dependencies**: Upstream of 02, 03, 04, 12. Foundation for entire collection.

---

### Paper 02: Quantum Fields in Curved Space
- **File**: `02_1982_Birrell_Davies_Quantum_Fields_Curved_Space.md`
- **Authors**: N. D. Birrell, P. C. W. Davies
- **Year**: 1982
- **Relevance**: CRITICAL
- **Tags**: curved spacetime QFT, Bogoliubov coefficients, adiabatic vacuum, Green's function, zeta regularization, Hawking temperature

**Summary**: Definitive monograph systematizing QFT in curved spacetime. Introduces symplectic inner product on Cauchy surfaces, multi-index Bogoliubov transformation v_k = Sum_j (alpha_kj u_j + beta_kj u_j*), adiabatic vacuum construction via WKB expansion, Green's function extraction of particle creation, and zeta-function regularization of divergent mode sums.

**Key Results**:
- Particle creation is frame-invariant (physical observable, not coordinate artifact)
- Hawking temperature T_H = kappa/(2*pi*k_B)
- Parker and Hawking effects unified as Bogoliubov transformation in non-stationary backgrounds
- Divergences removed by zeta-function regularization

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Klein-Gordon | (Box - m^2 - xi*R) phi = 0 | Ch. 2 |
| Symplectic product | (phi_1, phi_2) = i Integral_Sigma [...] d*Sigma^mu | Ch. 2 |
| Multi-index Bogoliubov | v_k = Sum_j (alpha_kj u_j + beta_kj u_j*) | Ch. 3 |
| Unitarity (matrix) | Sum_j (\|alpha_kj\|^2 - \|beta_kj\|^2) = delta_kk' | Ch. 3 |
| Hawking temperature | T_H = kappa / (2*pi*k_B) | Ch. 8 |

**Dependencies**: From 01. Upstream of 08, 15. Standard reference for all subsequent work.

---

### Paper 03: Cosmological Perturbations in Inflationary Universe
- **File**: `03_1981_Mukhanov_Chibisov_Cosmological_Perturbations.md`
- **Authors**: V. F. Mukhanov, G. V. Chibisov
- **Year**: 1981
- **Relevance**: CRITICAL
- **Tags**: Mukhanov-Sasaki equation, Bunch-Davies vacuum, primordial power spectrum, spectral index, gauge invariance

**Summary**: First calculation of primordial power spectrum from quantum vacuum fluctuations. Gauge-invariant variable zeta = psi + (H/(rho+p))*delta_rho satisfies the Mukhanov-Sasaki equation u_k'' + (k^2 - a''/a) u_k = 0. Bunch-Davies vacuum selects unique initial condition. Power spectrum P_zeta = H^2/(8*pi^2*epsilon) with spectral index n_s = 1 - 6*epsilon + 2*eta.

**Key Results**:
- Quantum origin of large-scale structure
- Scale-invariant spectrum (n_s ~ 1) from slow-roll inflation
- Tensor-to-scalar ratio r = 16*epsilon
- Observable consistency with Planck data

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Gauge-invariant variable | zeta = psi + (H/(rho+p)) delta_rho | Sec. 2 |
| Mukhanov-Sasaki equation | u_k'' + (k^2 - a''/a) u_k = 0 | Sec. 2 |
| Bunch-Davies vacuum | u_k(eta) = e^{-ik*eta} / sqrt(2k) | Sec. 2 |
| Power spectrum | P_zeta = H^2 / (8*pi^2*epsilon) | Sec. 3 |
| Spectral index | n_s = 1 - 6*epsilon + 2*eta | Sec. 3 |

**Dependencies**: From 01. Upstream of 18, 19, 22, 30. Also in Group 7.

---

### Paper 04: Towards the Theory of Reheating After Inflation
- **File**: `04_1994_Kofman_Linde_Starobinsky_Preheating.md`
- **Authors**: L. Kofman, A. D. Linde, A. A. Starobinsky
- **Year**: 1994
- **Relevance**: CRITICAL
- **Tags**: preheating, parametric resonance, Mathieu equation, Floquet exponent, broad resonance, backreaction

**Summary**: Introduces preheating: the oscillating inflaton drives parametric resonance in coupled fields via the Mathieu equation chi_k'' + [k^2 + g^2*phi_0^2*cos^2(m_phi*t)] chi_k = 0. For q = g^2*phi_0^2/(4*m_phi^2) >> 1, broad resonance produces exponential particle growth |beta_k|^2 ~ exp(2*N*mu_k) over N oscillations. Energy transfer is orders of magnitude faster than perturbative decay.

**Key Results**:
- Broad parametric resonance: nearly all modes with k < m_phi grow exponentially
- Preheating timescale t_preheat ~ 1/sqrt(g*lambda) (Planck time), far faster than perturbative decay
- Non-thermal particle distribution: created particles have k ~ sqrt(g)*m_phi
- Effective decay rate Gamma_preheat ~ g*sqrt(g*lambda)*m_phi >> Gamma_pert

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Coupling potential | V = (1/2)*m_phi^2*phi^2 + (1/2)*g^2*phi^2*chi^2 | Sec. 2 |
| Mathieu equation | chi_k'' + [k^2 + g^2*phi_0^2*cos^2(m*t)] chi_k = 0 | Sec. 2 |
| Resonance parameter | q = g^2*phi_0^2 / (4*m_phi^2) | Sec. 2 |
| Floquet growth | \|chi_k\| ~ exp(mu_k * t) | Sec. 3 |
| Bogoliubov after N periods | \|beta_k\|^2 ~ exp(2*N*mu_k) | Sec. 3 |

**Dependencies**: From 01, 20. Upstream of 17, 25, 29.

---

### Paper 05: Topology of Cosmic Domains and Strings
- **File**: `05_1980_Kibble_Cosmological_Phase_Transitions.md`
- **Author**: Tom W. B. Kibble
- **Year**: 1976-1980
- **Relevance**: HIGH
- **Tags**: topological defects, cosmic strings, monopoles, domain walls, phase transition, critical slowing

**Summary**: Establishes that rapid cosmological phase transitions produce topological defects when causally disconnected regions independently choose symmetry-breaking directions. Defect density scales as n ~ xi_c^{-d} where xi_c is the correlation length at the critical moment. Applied to electroweak and GUT transitions.

**Key Results**:
- Defect formation is universal for broken-symmetry phase transitions
- n_defects ~ xi^{-2} in 3D
- Monopole problem: GUT transitions overproduce monopoles, motivating inflation
- Domain wall surface tension sigma ~ eta^2 * Delta_phi

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Relaxation time divergence | tau_relax ~ \|T_c - T\|^{-nu*z} | Sec. 2 |
| Correlation length | xi(t) ~ t^{1/(nu*z)} | Sec. 2 |
| Defect density | n_defects ~ xi_c^{-d} | Sec. 3 |

**Dependencies**: Upstream of 06, 11, 24.

---

### Paper 06: Cosmological Experiments and the Theory of Phase Transitions
- **File**: `06_1985_Zurek_Kibble_Zurek_Mechanism.md`
- **Author**: Wojciech H. Zurek
- **Year**: 1985
- **Relevance**: HIGH
- **Tags**: KZM scaling, freeze-out, critical exponents, quench rate, universality

**Summary**: Zurek quantifies Kibble's mechanism: defect density n ~ (tau_Q)^{-d*nu/(nu*z+1)} where tau_Q is the quench timescale, nu the correlation-length exponent, z the dynamic exponent. Freeze-out occurs when tau_corr ~ tau_Q, giving xi_freeze ~ (tau_Q)^{nu/(nu*z+1)}. Scaling is universal, depending only on symmetry class and dimension.

**Key Results**:
- Universal KZM scaling: n ~ (tau_Q)^{-d*nu/(nu*z+1)}
- Freeze-out correlation length: xi_freeze ~ (tau_Q)^{nu/(nu*z+1)}
- Scaling robust against slow-roll or other approximations
- Laboratory tests confirmed in BEC, superfluids, superconductors

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Freeze-out condition | tau_corr ~ tau_Q | Sec. 2 |
| Freeze-out length | xi_freeze ~ (tau_Q)^{nu/(nu*z+1)} | Sec. 2 |
| KZM scaling | n ~ (tau_Q)^{-d*nu/(nu*z+1)} | Sec. 2 |

**Dependencies**: From 05. Upstream of 11, 24.

---

### Paper 07: Nonequilibrium Quantum Field Theory
- **File**: `07_2004_Calzetta_Hu_Nonequilibrium_Quantum_Field_Theory.md`
- **Authors**: E. A. Calzetta, B.-L. B. Hu
- **Year**: 2008
- **Relevance**: CRITICAL
- **Tags**: Schwinger-Keldysh, closed-time-path, Kadanoff-Baym, non-equilibrium Green's functions, prethermalization, entropy production

**Summary**: Comprehensive monograph on non-equilibrium QFT via Schwinger-Keldysh contour. Generating functional Z_C[J+, J-] uses forward/backward branches. Green's functions decompose into retarded (causality), advanced, and Keldysh (statistical) components. Kadanoff-Baym equations govern occupation number evolution dn_k/dt. Entropy production dS/dt >= 0 guaranteed by causal structure.

**Key Results**:
- Quantum kinetics: n_k(t) extracted from Green's functions without full state
- Prethermalization plateaus emerge naturally from Kadanoff-Baym equations
- H-theorem: entropy increases monotonically even for time-reversible dynamics
- Directly applicable to cosmological reheating

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Generating functional | Z_C[J+,J-] = Integral D[phi+] D[phi-] exp(i S_C) | Sec. 3 |
| Action on contour | S_C = Integral [L(phi+) - L(phi-)] d^4x | Sec. 3 |
| Kadanoff-Baym | (Box - m^2) G_<(x,y) = -i Integral Sigma_> G_< | Sec. 6 |
| Occupation number | n_k = (i/2)[G_<(t,t;k) - G_>(t,t;k)] | Sec. 6 |
| Entropy production | dS/dt >= 0 | Sec. 7 |

**Dependencies**: Upstream of 10, 16, 13. From 16 (Keldysh foundations).

---

### Paper 08: Analogue Gravity
- **File**: `08_2005_Barcelo_Liberati_Visser_Analogue_Gravity.md`
- **Authors**: C. Barcelo, S. Liberati, M. Visser
- **Year**: 2005
- **Relevance**: CRITICAL
- **Tags**: acoustic metric, sonic horizon, Hawking radiation, BEC analog, dispersion robustness, phonon

**Summary**: Comprehensive review of analog gravity. Sound waves in flowing fluid satisfy scalar wave equation in effective curved spacetime with metric g_mu_nu ~ rho/rho_0 * (flow terms). Sonic horizon at |v| = c_s produces Hawking radiation at T = hbar*kappa/(2*pi*k_B). Effect is robust against UV dispersion corrections.

**Key Results**:
- Universality: Hawking effect depends only on surface gravity kappa, not UV details
- Robustness against dispersion: thermal spectrum persists for wide class of omega(k)
- Entanglement in Hawking pairs: two-mode squeezed states
- Experimental feasibility demonstrated

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Acoustic metric | g_mu_nu = (rho/rho_0) * diag(-(v^2 - c_s^2), 2v_i, ...) | Sec. 2 |
| Sonic horizon | \|v\| = c_s | Sec. 2 |
| Bogoliubov coefficient | \|beta_k\|^2 ~ exp(-2*pi*omega/kappa) | Sec. 3 |
| Acoustic Hawking temperature | T = hbar*kappa / (2*pi*c_s*k_B) | Sec. 3 |

**Dependencies**: From 02, 12, 15, 27. Upstream of 09.

---

### Paper 09: Observation of Thermal Hawking Radiation in BEC
- **File**: `09_2016_Steinhauer_Hawking_Radiation_BEC.md`
- **Author**: Jeff Steinhauer
- **Year**: 2016
- **Relevance**: CRITICAL
- **Tags**: experimental, BEC, Hawking radiation, pair correlation, thermal spectrum, rubidium-87

**Summary**: First experimental observation of thermal Hawking radiation in a Rb-87 BEC acoustic black hole. Sonic horizon created by laser-accelerated flow (v > c_s). Pair correlations between upstream and downstream density fluctuations confirm Hawking mechanism. Measured temperature T = 50 +/- 10 pK matches theoretical prediction T = hbar*kappa/(2*pi*k_B) = 51 +/- 3 pK to < 2%.

**Key Results**:
- Hawking radiation observed: thermal spectrum at predicted temperature
- Entanglement signatures in pair correlations
- Robustness confirmed: non-relativistic medium reproduces QFT prediction
- Quantitative validation of Bogoliubov framework

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Surface gravity | kappa = dv/dx at horizon ~ 10^4 s^{-1} | Sec. 2 |
| Hawking temperature | T = hbar*kappa / (2*pi*k_B) | Sec. 2 |
| Pair correlation | G(t) = <rho_upstream(0) rho_downstream(t)> | Sec. 3 |
| Thermal spectrum | n(omega) = 1/(exp(omega/T) - 1) + background | Sec. 3 |

**Dependencies**: From 08, 12, 27. Experimental validation of 01, 02.

---

### Paper 10: Progress in Nonequilibrium Quantum Field Theory
- **File**: `10_2002_Berges_Nonequilibrium_Thermalization_QFT.md`
- **Authors**: J. Berges, J. Serreau
- **Year**: 2002-2003
- **Relevance**: CRITICAL
- **Tags**: nPI effective action, 2PI, thermalization, prethermalization, secular resummation, mode temperature

**Summary**: Develops nPI effective action methods for non-perturbative thermalization. 2PI effective action Gamma_2PI[phi, G] automatically resums secular corrections. Thermalization proceeds through buildup of long-lived correlations: prethermalization plateau (n_k reaches quasi-steady f(omega/T_eff)) before final thermalization. For integrable systems, plateau state is exactly the GGE.

**Key Results**:
- Non-perturbative thermalization computable from 2PI formalism
- Prethermalization is universal: robust across initial conditions and couplings
- Different momentum modes have different effective temperatures during plateau
- Thermalization timescale: tau_therm >> tau_plateau

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| 2PI effective action | Gamma_2PI = (1/2)Tr ln G^{-1} - (1/2)Tr(G_0^{-1} G) + Phi[phi,G] | Sec. 2 |
| Self-energy equation | (Box + m^2)G + Integral Sigma G = delta | Sec. 2 |
| Mode temperature | T_k = E_k / ln(1 + 1/n_k) | Sec. 3 |

**Dependencies**: From 07, 04. Upstream of 26, 13.

---

### Paper 11: Defect Formation Beyond Kibble-Zurek
- **File**: `11_2005_del_Campo_Zurek_Defect_Formation_Scaling.md`
- **Authors**: A. del Campo, W. H. Zurek
- **Year**: 2005-2024
- **Relevance**: HIGH
- **Tags**: impulse regime, quantum KZM, first-order transitions, Landau-Zener, saturation

**Summary**: Extends KZM to ultra-fast quenches (impulse limit) where standard scaling breaks down. In the impulse regime, defect density saturates at n ~ 1/(correlation volume), independent of quench rate. For quantum phase transitions, scaling changes to n ~ (d_lambda/dt)^{d/(nu*z+1)}. Landau-Zener sets minimum excitation floor. Extended to first-order transitions with latent heat effects.

**Key Results**:
- Impulse limit: defect density saturates, independent of tau_Q
- Quantum KZM: different exponent from thermal KZM
- Landau-Zener floor: P_LZ ~ exp(-2*pi*|gap|^2 / |quench rate|)
- First-order transitions: causal growth of correlation length still governs

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Impulse saturation | n_defects^{impulse} ~ 1/(correlation volume) | Sec. 2 |
| Quantum KZM | n ~ (d_lambda/dt)^{d/(z*nu+1)} | Sec. 2 |
| Landau-Zener | P_LZ ~ exp(-2*pi*\|gap\|^2 / \|quench rate\|) | Sec. 3 |

**Dependencies**: From 06. Upstream of 24.

---

### Paper 12: Experimental Black-Hole Evaporation?
- **File**: `12_1981_Unruh_Sonic_Black_Holes.md`
- **Author**: William G. Unruh
- **Year**: 1981
- **Relevance**: CRITICAL
- **Tags**: sonic black hole, acoustic horizon, analog gravity, Hawking radiation, dispersion robustness

**Summary**: Proposes that Hawking radiation can be observed in sonic black holes (flowing fluids with v > c_s). Scalar perturbations in a flowing fluid obey the wave equation in an effective curved spacetime. Bogoliubov mixing at the sonic horizon produces particle creation with |beta_omega|^2 ~ exp(-2*pi*omega/kappa). The acoustic Hawking temperature T = hbar*kappa/(2*pi*k_B) is universal. Effect persists despite realistic UV dispersion.

**Key Results**:
- Universality: Hawking effect is structural (Bogoliubov mixing at horizons), not specific to GR
- Temperature T = hbar*kappa/(2*pi*k_B) for any horizon with surface gravity kappa
- Robustness against high-frequency dispersion corrections
- Experimental feasibility established

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Acoustic metric | g_mu_nu ~ (rho/rho_0) diag(-(v^2-c_s^2), 2v_i, delta_ij - v_i*v_j/c_s^2) | Sec. 2 |
| Sonic horizon | \|v\| = c_s | Sec. 2 |
| Bogoliubov coefficient | \|beta_omega\|^2 ~ exp(-2*pi*omega/kappa) | Sec. 3 |
| Acoustic temperature | T = hbar*kappa / (2*pi*k_B) | Sec. 3 |

**Dependencies**: From 01. Upstream of 08, 09.

---

### Paper 13: Generalized Gibbs Ensemble Prediction
- **File**: `13_2011_Rigol_Generalized_Gibbs_Ensemble.md`
- **Authors**: M. Rigol, V. Dunjko, M. Olshanii
- **Year**: 2007-2011
- **Relevance**: CRITICAL
- **Tags**: GGE, integrable systems, prethermalization, conserved charges, diagonal ensemble, non-thermalization

**Summary**: Proves that integrable quantum systems after sudden quench relax to the GGE rho_GGE ~ exp(-Sum_n lambda_n I_n), not thermal equilibrium. The GGE maximizes entropy subject to conserving all local integrals of motion [H, I_n] = 0. Long-time average equals the diagonal ensemble. Experimentally confirmed in cold atoms.

**Key Results**:
- Integrable systems do not thermalize: approach GGE steady state
- Entropy constraint: S_GGE < S_thermal (additional conserved charges)
- Prethermalization universal: even weakly non-integrable systems first approach GGE
- Experimental confirmation in Lieb-Liniger gas and XXZ chain

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| GGE distribution | rho_GGE ~ exp(-Sum_n lambda_n I_n) | Sec. 2 |
| Charge conservation | [H, I_n] = 0 for all n | Sec. 2 |
| Diagonal ensemble | <O>_infinity = Sum_n \|c_n\|^2 <E_n\|O\|E_n> | Sec. 2 |
| Entropy | S_GGE = -Tr(rho_GGE ln rho_GGE) | Sec. 2 |

**Dependencies**: From 10, 07. Upstream of 21, 23.

---

### Paper 14: Schwinger Pair Production in Strong Electric Fields
- **File**: `14_1981_Schwinger_Pair_Creation_QED.md`
- **Author**: Julian Schwinger
- **Year**: 1951
- **Relevance**: MEDIUM
- **Tags**: pair creation, strong field, WKB tunneling, proper-time, critical field, non-perturbative QED

**Summary**: Schwinger calculates electron-positron pair creation rate from strong electric fields via the imaginary part of the effective action. Tunneling probability P ~ exp(-pi*m^2/(eE)). Critical field E_c = m^2/e ~ 1.3 x 10^18 V/m. Rate formula Gamma ~ (E/E_c)^2 exp(-pi*E_c/E). Proper-time method gives systematic series.

**Key Results**:
- Exponential suppression below E_c: vacuum appears stable in normal conditions
- Rate: Gamma ~ (E/E_c)^2 * exp(-pi*E_c/E)
- Proper-time formalism: standard for non-perturbative calculations
- Generalization to time-dependent fields: rapid variations enhance production

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Tunneling probability | P ~ exp(-pi*m^2 / (eE)) | Sec. 2 |
| Critical field | E_c = m^2 c^3 / (e*hbar) | Sec. 3 |
| Effective action (imaginary part) | Im[S_eff] = -(eE/8*pi^2) Sum_n (-1)^{n+1}/n^2 exp(-pi*n*m^2/(eE)) | Sec. 2 |
| Rate formula | Gamma ~ (E/E_c)^2 exp(-pi*E_c/E) | Sec. 3 |

**Dependencies**: Upstream of 01 (tunneling methods).

---

### Paper 15: Black Hole Thermodynamics
- **File**: `15_1987_Jacobson_Black_Hole_Thermodynamics.md`
- **Author**: Ted Jacobson
- **Year**: 1995
- **Relevance**: HIGH
- **Tags**: emergent gravity, area entropy, thermodynamic spacetime, Rindler, cosmological horizon

**Summary**: Jacobson derives Einstein's equations from thermodynamic consistency of horizon entropy. Area-entropy relation S = A/(4*G*hbar) and temperature T = kappa/(2*pi) constitute exact thermodynamic laws. Requiring entropy increase for all causal horizons yields Einstein's field equations algebraically. Gravity is emergent, not fundamental.

**Key Results**:
- Gravity emerges from thermodynamics: Einstein equations are thermodynamic identities
- S = A/(4G*hbar) is universal for all horizons
- First law: dU = T*dS equivalent to dE = (kappa/2*pi)*d(A/4)
- Dark energy as cosmological horizon entropy

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Entropy | S = A / (4*G*hbar) | Sec. 2 |
| Temperature | T = kappa / (2*pi) | Sec. 2 |
| First law | dU = T*dS | Sec. 2 |
| Unruh temperature | T_Unruh = kappa / (2*pi) | Sec. 3 |

**Dependencies**: From 02. Upstream of 08.

---

### Paper 16: Field Theory of Non-Equilibrium Systems
- **File**: `16_1999_Kamenev_Keldysh_Nonequilibrium_Field_Theory.md`
- **Author**: Alex Kamenev
- **Year**: 2004 (book); 1999-2003
- **Relevance**: CRITICAL
- **Tags**: Keldysh formalism, closed-time-path, real-time diagrams, kinetic equation, entropy production

**Summary**: Systematizes Keldysh formalism for non-equilibrium QFT. Closed-time-path contour t_i -> t_f -> t_i. Three independent Green's functions: G_>, G_<, and G_K (Keldysh). Retarded G_R encodes causality, Keldysh G_K encodes statistics. Effective kinetic equation dn_k/dt = -2*Im[Sigma_R]*(...). Entropy functional increases monotonically.

**Key Results**:
- Unified framework treating equilibrium and non-equilibrium equally
- Systematic perturbative expansion organized by diagram topology
- Real-time correlations computed directly (no imaginary-time continuation)
- Thermodynamic consistency: second law guaranteed at every approximation order

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Generating functional | Z_C[J+,J-] = Integral D[phi+] D[phi-] exp(iS_C/hbar) | Sec. 2 |
| Keldysh component | G_K = (G_> + G_<)/2 | Sec. 2 |
| Kinetic equation | dn_k/dt = -2*Im[Sigma_R(k, n_k)] * (correction) | Sec. 3 |
| Entropy increase | dS/dt >= 0 | Sec. 3 |

**Dependencies**: Upstream of 07. From Keldysh 1964.

---

### Paper 17: Parametric Resonance in Preheating
- **File**: `17_2003_Amin_Parametric_Resonance_Preheating.md`
- **Author**: Mustafa A. Amin
- **Year**: 2003-2010
- **Relevance**: CRITICAL
- **Tags**: parametric resonance, backreaction, rescattering, non-thermal spectra, tachyonic instability

**Summary**: Detailed numerical and analytical treatment of parametric resonance during preheating. Maps instability bands as function of q. Backreaction timescale tau_rescatter ~ 1/sqrt(coupling * growth_rate). Non-thermal spectra n_k ~ k^{-beta} with beta ~ 1/2 to 2. Distinguishes parametric resonance (broad k-growth) from tachyonic instability (narrow, faster).

**Key Results**:
- Non-thermal spectra: n_k ~ k^{-2} to k^{-1/2}
- Backreaction saturation at n_k ~ g*phi_0/E_k
- Rescattering drives slow thermalization after saturation
- Strong vs weak coupling: broad vs narrow resonance

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Mathieu equation | chi_k'' + [k^2 + g^2*phi_0^2*cos^2(m*t)] chi_k = 0 | Sec. 2 |
| Mode occupation | n_k(t) = \|chi_k(t)\|^2 / (mode volume) | Sec. 2 |
| Rescattering timescale | tau_rescatter ~ 1/sqrt(coupling * growth rate) | Sec. 3 |

**Dependencies**: From 04. Upstream of 29.

---

### Paper 18: Power Spectrum in R^2 Inflation
- **File**: `18_2000_Starobinsky_Power_Spectrum_R2_Inflation.md`
- **Author**: A. A. Starobinsky
- **Year**: 1980-2000+
- **Relevance**: HIGH
- **Tags**: R^2 inflation, scalaron, exact solution, non-slow-roll, spectral index, no tensor

**Summary**: R^2 inflation (S = Integral sqrt{-g} [R + (alpha/6)*R^2]) was the first consistent inflationary model. Equivalent to scalaron with potential V(phi) = (M_P^2/(8*alpha))*(1 - exp(-sqrt(2/3)*phi/M_P))^2. Exact numerical solution gives n_s ~ 0.965, in remarkable agreement with Planck. Near critical points, slow-roll breaks down and exact solutions deviate substantially from approximations.

**Key Results**:
- Scale-invariance from geometry without slow-roll
- n_s = 0.9649 (R^2 prediction) vs n_s = 0.9661 (Planck): deviation < 0.2%
- Tensor-to-scalar ratio r ~ 10^{-12} (extremely suppressed)
- Exact solutions differ from slow-roll by factors of 2-10 near transitions

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| R^2 action | S = Integral sqrt{-g} [R + (alpha/6)*R^2] | Sec. 2 |
| Scalaron potential | V(phi) = (M_P^2/(8*alpha))(1 - e^{-sqrt(2/3)*phi/M_P})^2 | Sec. 2 |
| Power spectrum | P_zeta(k) = (A/s)*k^{n_s-1} | Sec. 3 |

**Dependencies**: From 03. Upstream of 30.

---

### Paper 19: Constant-Roll Inflation
- **File**: `19_2005_Motohashi_Constant_Roll_Inflation.md`
- **Authors**: H. Motohashi, S. Mukohyama, T. Suyama
- **Year**: 2014-2017
- **Relevance**: MEDIUM
- **Tags**: constant-roll, beyond slow-roll, exact mode function, Hankel function, running spectral index

**Summary**: Constant-roll inflation (eta = const) admits exact analytical mode functions u_k = sqrt(pi|eta|/2)*H_nu^{(1)}(k|eta|) with nu = 3/2 + 1/(eta+1). Spectral index n_s = (eta-1)/(1+eta) spans wide range depending on parameters. Bridges slow-roll and fast-roll regimes with exact solutions.

**Key Results**:
- Exact analytical mode functions for constant-roll
- Flexible spectral index from very red to very blue
- Specific running dn_s/d(ln k) = const
- Enables primordial black hole production from large power spectrum amplification

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Constant-roll condition | eta = d(ln epsilon)/d(ln a) = const | Sec. 2 |
| Mode function | u_k = sqrt(pi\|eta\|/2) * H_nu^{(1)}(k\|eta\|) | Sec. 2 |
| Spectral index | n_s = (eta - 1)/(1 + eta) | Sec. 2 |

**Dependencies**: From 03.

---

### Paper 20: Bogoliubov-Valatin Transformation
- **File**: `20_1989_Bogoliubov_Valatin_Transformation_Theory.md`
- **Authors**: N. Bogoliubov, J. G. Valatin
- **Year**: 1958
- **Relevance**: CRITICAL
- **Tags**: BdG transformation, BCS, quasiparticle, energy gap, superconductivity, superfluidity

**Summary**: Canonical transformation gamma_k = u_k c_k + v_k c_{-k}^dagger diagonalizes the BCS Hamiltonian, revealing Bogoliubov quasiparticles with energy E_k = sqrt(epsilon_k^2 + Delta^2). The energy gap Delta emerges self-consistently. Quasiparticles are particle-hole superpositions. Foundation for superconductivity and direct precursor to cosmological Bogoliubov transformations.

**Key Results**:
- Diagonalizes pairing Hamiltonians: H = const + Sum_k E_k gamma_k^dagger gamma_k
- Energy gap: E_k >= Delta (minimum excitation energy)
- Gap equation: Delta ~ exp(-1/(g*N(0))) (weak coupling)
- Quasiparticles: gamma_k = u_k(electron) + v_k(hole)

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| BdG transformation | gamma_k = u_k c_k + v_k c_{-k}^dagger | Sec. 2 |
| Normalization | \|u_k\|^2 + \|v_k\|^2 = 1 | Sec. 2 |
| Quasiparticle energy | E_k = sqrt(epsilon_k^2 + Delta^2) | Sec. 2 |
| BCS Hamiltonian | H_BCS = Sum_k epsilon_k c_k^dagger c_k - (g/Omega) Sum_{k,k'} c_k^dagger c_{-k}^dagger c_{-k'} c_{k'} | Sec. 2 |

**Dependencies**: Upstream of 01, 04.

---

### Paper 21: Relaxation and Prethermalization in Isolated Quantum Systems
- **File**: `21_2002_Langen_Relaxation_Quantum_Systems.md`
- **Authors**: T. Langen, T. Gasenzer, J. Schmiedmayer
- **Year**: 2012-2016
- **Relevance**: CRITICAL
- **Tags**: experimental, prethermalization, entanglement entropy, GGE validation, cold atoms, timescale separation

**Summary**: Experimental observation of prethermalization in isolated quantum systems (Rb-87 in 1D optical lattice). Entanglement entropy S_A(t) shows three phases: rapid growth (quench), plateau (GGE), slow drift (thermalization). For weakly broken integrability, tau_therm >> tau_pretherm. Confirms Rigol's GGE predictions.

**Key Results**:
- GGE experimentally real: isolated systems reach GGE steady states
- Timescale separation: tau_pretherm ~ 1-10 ms vs tau_therm >> seconds
- Entanglement entropy plateaus at S_GGE << S_thermal
- Confirms integrable system non-thermalization

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Perturbed integrable H | H = H_integrable + epsilon * V_nonintegrable | Sec. 2 |
| Entanglement entropy | S_A(t) = -Tr(rho_A ln rho_A) | Sec. 2 |
| Thermalization approach | (T_eff - T_thermal)/T_thermal ~ exp(-t/tau_therm) | Sec. 3 |

**Dependencies**: From 13. Experimental validation of 13.

---

### Paper 22: Measuring the Primordial Power Spectrum
- **File**: `22_2010_Liddle_Primordial_Power_Spectrum_Reconstruction.md`
- **Authors**: A. R. Liddle, S. M. Leach
- **Year**: 2003-2010
- **Relevance**: MEDIUM
- **Tags**: PCA reconstruction, model-independent, scale-invariance, CMB features

**Summary**: Principal component analysis for model-independent reconstruction of P(k). Decomposes P(k) = P_0[1 + Sum_n a_n f_n(k)] where f_n are orthonormal eigenmodes from the CMB information matrix. Detects localized features, running, oscillations without assuming inflation model.

**Key Results**:
- Model-independent power spectrum reconstruction
- Detects deviations from scale-invariance
- Identifies localized features (resonances, discontinuities)
- Used in Planck 2018 analysis

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| PCA decomposition | P(k) = P_0[1 + Sum_n a_n f_n(k)] | Sec. 2 |
| Baseline | P(k) = A[1 + (n_s-1)*ln(k/k_0) + ...] | Sec. 2 |

**Dependencies**: From 03.

---

### Paper 23: Quantum Quenches in Transverse-Field Ising Chain
- **File**: `23_2008_Calabrese_Essler_Quantum_Quenches.md`
- **Authors**: P. Calabrese, F. H. L. Essler, M. Fagotti
- **Year**: 2011-2012
- **Relevance**: HIGH
- **Tags**: exact solution, quantum quench, Ising model, GGE, entanglement saturation

**Summary**: Exact solution of quantum quench dynamics in the transverse-field Ising model. After sudden quench from H_i to H_f, system evolves to GGE steady state (integrable) or thermal equilibrium (non-integrable). Exact occupation numbers and two-point functions derived. Entanglement entropy saturates at GGE value.

**Key Results**:
- Exact GGE steady state for integrable quench
- Entanglement entropy saturation set by conserved charges
- Methods extend to XXZ, sine-Gordon, other integrable models

**Dependencies**: From 13.

---

### Paper 24: Dynamics of a Quantum Phase Transition
- **File**: `24_2006_Dziarmaga_Phase_Transition_Dynamics_Ising.md`
- **Author**: Jacek Dziarmaga
- **Year**: 2005-2010
- **Relevance**: MEDIUM
- **Tags**: quantum phase transition, Ising model, KZM verification, exact scaling, Floquet

**Summary**: Exact solutions for quantum phase transition dynamics in the transverse-field Ising model. Defect density ~ sqrt(d_lambda/dt) (square-root scaling) matches KZM prediction. Extensions to non-linear quenches and periodic drives (Floquet systems).

**Key Results**:
- Exact KZM scaling verified for Ising: n ~ sqrt(d_lambda/dt)
- Extensions to Floquet systems
- Impulse limit: framework transit is beyond Dziarmaga scaling (saturation regime)

**Dependencies**: From 06, 11.

---

### Paper 25: Geometric Reheating After Inflation
- **File**: `25_1995_Bassett_Geometric_Reheating.md`
- **Authors**: B. Bassett, S. Tsujikawa, D. Wands
- **Year**: 1997-2010
- **Relevance**: MEDIUM
- **Tags**: geometric reheating, non-minimal coupling, xi*R, tachyonic instability, model-independent

**Summary**: Reheating via non-minimal coupling to curvature: L includes (xi/2)*R*phi^2. For xi ~ 1/6 or larger, effective mass becomes negative during inflation exit, triggering tachyonic instability and explosive particle production without requiring explicit couplings to other fields. Works for generic inflatons.

**Key Results**:
- Efficient reheating from geometric coupling alone
- Robust: works for any potential
- Tachyonic instability drives rapid energy transfer

**Dependencies**: From 04.

---

### Paper 26: Thermalization from First Principles in nPI Formalism
- **File**: `26_2010_Berges_Thermalization_nPI_Methods.md`
- **Authors**: J. Berges, A. Ipp, C. Serreau, D. Sexty
- **Year**: 2006-2010
- **Relevance**: HIGH
- **Tags**: nPI, 2PI, secular resummation, thermalization, Kadanoff-Baym

**Summary**: Systematizes nPI effective action methods for thermalization in far-from-equilibrium QFT. 2PI truncation at 2-loop level controls secular corrections automatically. Equations of motion for field and propagator. Prethermalization plateau confirmed from first principles.

**Key Results**:
- Thermalization computed from first principles
- Secular terms automatically controlled
- Prethermalization plateau robust

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| 2PI effective action | Gamma_2PI = (1/2)Tr ln G^{-1} - (1/2)Tr(G_0^{-1} G) + Phi | Sec. 2 |
| Self-energy equation | [Box + m^2]G + Integral Sigma G = delta | Sec. 2 |

**Dependencies**: From 10.

---

### Paper 27: Superfluid 3He and Analog Gravity Cosmology
- **File**: `27_2012_Volovik_Superfluid_3He_Analogue_Gravity.md`
- **Author**: G. E. Volovik
- **Year**: 2001-2012
- **Relevance**: CRITICAL
- **Tags**: superfluid 3He-A, parent system, order parameter texture, emergent metric, phonon, cosmological analog

**Summary**: Demonstrates that 3He-A is a parent system (not mere analog) whose quasiparticle physics exhibits cosmological phenomena. Order parameter texture Delta_ij creates effective metric for phonons. Superflow v > c_s creates sonic horizon with Hawking-like pairs. Phase transition dynamics mimic inflation-to-reheating. The system is fully quantum and microscopically understood.

**Key Results**:
- 3He-A is a realistic analog: gravity-like phenomena in microscopically understood system
- Multiple timescales: inflation-like acceleration, particle creation, thermalization
- Universality: lessons apply to graphene, cold atoms, quantum simulators

**Key Equations**:

| Label | Equation | Reference |
|:---|:---|:---|
| Order parameter | Delta_ij = Delta*(d_i + i*h*l_i)*sigma_y*sigma_j | Sec. 2 |
| Phonon dispersion | omega_k^2 = c_s^2*k^2 + (texture corrections) | Sec. 2 |

**Dependencies**: Upstream of 08, 09.

---

### Paper 28: The Swampland: Constraints on Effective Field Theories
- **File**: `28_2018_Vafa_Swampland_Constraints.md`
- **Authors**: C. Vafa, H. Ooguri
- **Year**: 2018-2019
- **Relevance**: MEDIUM
- **Tags**: swampland, weak gravity conjecture, distance conjecture, de Sitter conjecture, inflation constraints

**Summary**: Swampland program constrains which effective field theories are realizable in string theory. De Sitter conjecture requires steep potentials |nabla V|/V >= c/M_P, ruling out many slow-roll models. Distance conjecture: infinite-distance limits require infinitely many light states. Motivates alternatives to scalar-field inflation.

**Key Results**:
- Swampland constraints disfavor slow-roll with flat potentials
- Motivates geometric/emergent alternatives
- Weak gravity conjecture: forbids extremely weak gravitational couplings

**Dependencies**: Upstream of 18 (constrains inflation models).

---

### Paper 29: Numerical Lattice Simulations of Preheating
- **File**: `29_2014_Tranberg_Numerical_Lattice_Simulations_Preheating.md`
- **Authors**: A. Tranberg, B. Garbrecht
- **Year**: 2006-2014
- **Relevance**: MEDIUM
- **Tags**: lattice simulation, leapfrog, power spectrum validation, backreaction, thermalization

**Summary**: Large-scale lattice simulations of preheating dynamics using symplectic integration. Validates Kofman-Linde-Starobinsky parametric resonance predictions to 10% precision. Confirms backreaction timescale tau_backreaction ~ 1/sqrt(g*lambda)*m_phi. Thermalization requires ~1000 oscillation periods, much longer than resonant growth.

**Key Results**:
- KLS parametric resonance validated numerically
- Backreaction timescale confirmed
- Thermalization slow: ~1000 oscillations after saturation

**Dependencies**: From 04, 17.

---

### Paper 30: Constraints on Inflationary Models from Primordial Power Spectrum
- **File**: `30_2021_Kinney_Primordial_Power_Spectrum_Constraints.md`
- **Author**: William H. Kinney
- **Year**: 2009-2021
- **Relevance**: HIGH
- **Tags**: Planck constraints, spectral index, tensor ratio, bispectrum, observational

**Summary**: Comprehensive review of CMB constraints on inflation. Planck 2018: n_s = 0.9661 +/- 0.0040, alpha = 0.003 +/- 0.007, r < 0.058, f_NL = -26 +/- 55. Scale-invariance robust. No running, no tensors, Gaussianity consistent with slow-roll or Bogoliubov creation. Starobinsky R^2 most favored model.

**Key Results**:
- n_s = 0.9661 +/- 0.0040 (near scale-invariant)
- Running alpha consistent with zero
- r < 0.058 (no tensor detection, small-field favored)
- f_NL consistent with zero (Gaussian primordial perturbations)

**Dependencies**: From 03, 18.

---

## Cross-Paper Equation Concordance

### The Mode Equation
The governing structure across all transit dynamics problems is the time-dependent oscillator equation:

**u_k'' + omega_k^2(t) u_k = 0**

| Context | omega_k^2(t) | Paper |
|:---|:---|:---|
| Parker creation (FLRW) | k^2/a^2(t) + m^2 - (a''/a) | 01 |
| Mukhanov-Sasaki (inflation) | k^2 - a''/a | 03 |
| Parametric resonance (preheating) | k^2 + g^2*phi_0^2*cos^2(m*t) | 04, 17 |
| Acoustic perturbations (analog) | k^2*c_s^2 - (flow gradient terms) | 08, 12 |
| Constant-roll | k^2 - nu^2/eta^2 (nu depends on eta=const) | 19 |
| BdG quasiparticles | epsilon_k^2 + Delta(t)^2 | 20 |

### The Bogoliubov Transformation
All particle creation reduces to this structure:

**b_k = alpha_k a_k + beta_k a_{-k}^dagger, with |alpha_k|^2 - |beta_k|^2 = 1**

| Context | beta_k expression | Paper |
|:---|:---|:---|
| Parker (adiabatic) | \|beta_k\|^2 ~ exp(-2*pi*omega_k/H) | 01 |
| Hawking (black hole) | \|beta_k\|^2 ~ 1/(exp(2*pi*omega/kappa) - 1) | 02, 15 |
| Acoustic Hawking | \|beta_omega\|^2 ~ exp(-2*pi*omega/kappa_acoustic) | 08, 09, 12 |
| Parametric resonance | \|beta_k\|^2 ~ exp(2*N*mu_k) (N oscillations) | 04 |
| Schwinger (tunneling) | \|beta\|^2 ~ exp(-pi*m^2/(eE)) | 14 |
| BdG | \|v_k\|^2 = (1/2)(1 - epsilon_k/E_k) | 20 |

### Particle Number and Distribution
The output state character:

| Regime | N_k distribution | Paper |
|:---|:---|:---|
| Adiabatic | \|beta_k\|^2 << 1, exponentially suppressed | 01, 02 |
| Diabatic/sudden | \|beta_k\|^2 ~ O(1), saturated | 01, 11 |
| Thermal (Hawking) | N_k = 1/(exp(omega/T) - 1) | 02, 08, 09 |
| Parametric resonance | N_k ~ exp(2*mu_k*t) (exponential growth) | 04, 17 |
| GGE (integrable quench) | N_k set by conserved charges, non-thermal | 13, 21, 23 |
| Schwinger | N ~ exp(-pi*E_c/E) per Compton volume | 14 |

### KZM Scaling Relations

| Regime | Defect density | Paper |
|:---|:---|:---|
| Thermal KZM | n ~ (tau_Q)^{-d*nu/(nu*z+1)} | 06 |
| Quantum KZM | n ~ (d_lambda/dt)^{d/(z*nu+1)} | 11 |
| Impulse limit | n ~ 1/(correlation volume), saturated | 11 |
| Ising (exact) | n ~ sqrt(d_lambda/dt) | 24 |

### Non-Equilibrium Formalism

| Object | Definition | Paper |
|:---|:---|:---|
| SK generating functional | Z_C[J+,J-] = Integral D[phi+] D[phi-] exp(iS_C) | 07, 16 |
| Retarded Green's function | G_R = theta(t-t')[phi(x), phi(x')] | 07, 16 |
| Keldysh component | G_K = (G_> + G_<)/2 | 16 |
| 2PI effective action | Gamma_2PI = (1/2)Tr ln G^{-1} - (1/2)Tr(G_0^{-1}G) + Phi | 10, 26 |
| GGE distribution | rho_GGE ~ exp(-Sum_n lambda_n I_n) | 13 |

---

## Notation Conventions

| Symbol | Meaning | Convention |
|:---|:---|:---|
| u_k, v_k | Mode functions (positive/negative frequency) | Birrell-Davies Ch. 3 |
| alpha_k, beta_k | Bogoliubov coefficients | \|alpha\|^2 - \|beta\|^2 = 1 (bosonic) |
| u_k, v_k (BdG) | Coherence factors in BdG transformation | \|u\|^2 + \|v\|^2 = 1 (fermionic) |
| omega_k(t) | Time-dependent mode frequency | Mode equation: u'' + omega^2 u = 0 |
| kappa | Surface gravity (gravitational or acoustic) | T = hbar*kappa/(2*pi*k_B) |
| n_k, N_k | Occupation number per mode | N_k = \|beta_k\|^2 |
| tau_Q | Quench timescale | KZM: n ~ tau_Q^{-alpha} |
| epsilon, eta | Slow-roll parameters | epsilon = -(dH/dt)/H^2, eta = d(ln epsilon)/d(ln a) |
| n_s | Spectral index | n_s - 1 = d(ln P)/d(ln k) |
| r | Tensor-to-scalar ratio | r = P_T/P_S |
| G_R, G_A, G_K | Retarded, advanced, Keldysh Green's functions | Schwinger-Keldysh formalism |
| Gamma_nPI | n-particle irreducible effective action | Berges formalism |
| rho_GGE | Generalized Gibbs ensemble density matrix | rho ~ exp(-Sum lambda_n I_n) |
| Delta | BCS energy gap / pairing parameter | E_k = sqrt(epsilon_k^2 + Delta^2) |
| mu_k | Floquet exponent | Parametric resonance growth rate |
| q | Resonance parameter | q = g^2*phi_0^2/(4*m^2) |

---

## Computational Verification Status

| Paper | Key equation | Status | Notes |
|:---|:---|:---|:---|
| 01 | N_k = \|beta_k\|^2 | STANDARD | Universal, verified in 09 experimentally |
| 02 | Unitarity \|alpha\|^2 - \|beta\|^2 = 1 | PROVEN | Mathematical identity from canonical commutation |
| 03 | n_s = 1 - 6*epsilon + 2*eta | OBSERVATIONALLY TESTED | Planck: n_s = 0.9661 +/- 0.0040 |
| 04 | Floquet: \|beta\|^2 ~ exp(2*N*mu_k) | NUMERICALLY VALIDATED | Confirmed by 29 (lattice) to 10% |
| 06 | KZM: n ~ tau_Q^{-d*nu/(nu*z+1)} | EXPERIMENTALLY VALIDATED | Multiple cold-atom experiments |
| 08 | T_acoustic = hbar*kappa/(2*pi*k_B) | EXPERIMENTALLY VALIDATED | Steinhauer (09): T = 50 +/- 10 pK vs 51 +/- 3 pK predicted |
| 09 | Thermal spectrum at acoustic horizon | EXPERIMENTALLY CONFIRMED | First direct observation, <2% agreement |
| 11 | Impulse saturation | EXPERIMENTALLY TESTED | Ion traps and cold atoms, ~10% precision |
| 13 | GGE for integrable quench | EXPERIMENTALLY VALIDATED | Cold-atom experiments (Langen 21) |
| 14 | Gamma ~ (E/E_c)^2 exp(-pi*E_c/E) | UNTESTED (E_c not reached) | Graphene analogs partial |
| 18 | n_s = 0.965 (R^2 inflation) | OBSERVATIONALLY CONSISTENT | Deviation < 0.2% from Planck |
| 20 | E_k = sqrt(epsilon_k^2 + Delta^2) | PROVEN (BCS theory) | Nobel Prize 1972 |
| 30 | r < 0.058 | OBSERVATIONAL BOUND | No tensor detection |

---

## Framework Connection Summary

The transit-dynamics collection maps onto the phonon-exflation framework as follows:

| Framework concept | Paper basis | Structural mapping |
|:---|:---|:---|
| Spectral fold transit (tau = 0.190) | Mode equation (01, 02, 03) | omega_k(tau) changes rapidly at fold; Bogoliubov mixing maximal |
| GGE relic (59.8 pairs) | GGE theory (13, 21, 23) | Integrable post-transit system; conserved charges prevent thermalization |
| Parker pair production | Bogoliubov foundations (01, 02, 20) | N_k = \|beta_k\|^2 computed from spectral mode equation |
| Acoustic white hole | Analog gravity (08, 09, 12, 27) | Supersonic transit creates sonic horizon in spectral space |
| Mach 13.75 supersonic transit | Impulse regime (11) | Deep in del Campo-Zurek saturation; defect count fixed, not scaling |
| Parametric amplification at fold | Preheating formalism (04, 17) | Mathieu equation structure with spectral action as driving potential |
| Non-thermalization (ordered veil) | nPI/GGE (10, 13, 26) | Integrable structure; tau_therm >> tau_universe |
| Emergent gravity from spectral action | Jacobson thermodynamics (15) | Einstein equations from spectral entropy-area relation |
| n_s = 0.9561 from spectral geometry | Beyond slow-roll (18, 19, 30) | Geometric origin of scale-invariance; no inflaton field |
| Volovik parent system | 3He-A analog (27) | Framework inherits from, not merely analogizes to, superfluid physics |
