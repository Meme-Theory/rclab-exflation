# Paasch Paper Index

**Researcher**: Klaus Paasch (and related mass quantization / fine structure constant / NCG / flavor symmetry authors)
**Papers**: 46 (1929-2025)
**Primary domain**: Mass quantization, logarithmic potentials, fine structure constant, Koide formula, NCG spectral action, flavor symmetry, DESI/Planck cosmology, varying constants
**Project relevance**: phi_paasch = 1.531580 mass ratio from SU(3) Dirac spectrum at tau=0.15 (S12); alpha derivation from n3=10 (S48 structural identity); spectral action on M4 x SU(3); DESI w(z) as Level 1 observational test; Koide Z_3 from Peter-Weyl triality

---

## Dependency Graph

```
PAASCH CORE & LOGARITHMIC MASS
  05 (Muraki 1978, log mass) --> 02 (Paasch 2009, log spiral)
  13 (Nambu 1952, alpha mass) --> 05
  13 --> 17 (MacGregor 2007, alpha quantization)
  02 --> 03 (Paasch 2016, mass calculation)
  02 --> 04 (Paasch 2016, alpha derivation)
  03 --> 04
  31 (Palazzi 2003, stablines) --> 42 (Giani 2004, mass catalogue)
  42 --> 17

FINE STRUCTURE CONSTANT & GEOMETRIC ALPHA
  14 (Eddington 1929) --> 16 (Wyler 1969)
  14 --> 04
  16 --> 04
  28 (Gsponer-Hurni 1996, Barut extension) --> 04
  28 --> 26 (Kosinov 2024, Koide-alpha)
  46 (Sticker 2024, alpha scaled) --> 43 (Uzan 2024, constants review)

KOIDE FORMULA & MASS RELATIONS
  07 (Koide 1983) --> 47 (Koide 2018, Sumino mechanism)
  07 --> 40 (Liang-Sun 2021, Koide nonets)
  07 --> 26 (Kosinov 2024, Koide-alpha)
  09 (Zenczykowski 2008, Cl(6)) --> 41 (Singh 2022, octonions)
  07 --> 03 [Paasch cites Koide for tau mass comparison]

LARGE NUMBER HYPOTHESIS & VARYING CONSTANTS
  08 (Dirac 1937, original LNH) --> 06 (Dirac 1974, cosmological models)
  06 --> 03 [Paasch cites as [1]]
  06 --> 44 (Ray 2007, LNH review)
  06 --> 38 (Jiang 2025, LNH updated review)
  10 (Williams 2004, LLR) --> 15 (Barrow 2005, varying constants)
  10 --> 43 (Uzan 2024)
  10 --> 39 (March 2025, LLR + evolving DE)
  15 --> 43

NCG & SPECTRAL ACTION
  20 (van Suijlekom 2024, textbook) --> 22 (CCS 2018, entropy-SA)
  22 --> 21 (Dong-Khalkhali-vS 2019, 2nd quantization)
  20 --> 29 (Hitchin 2025, Dirac operator survey)
  24 (Furey 2025, Z2^5 superalgebra) --> 25 (Furey 2024, roadmap)
  41 (Singh 2022, octonions) <--> 24 [both use division algebras]

FLAVOR SYMMETRY & MASS HIERARCHY
  23 (Ibe-Shirai 2025, FN Bayesian) --> 36 (Greljo 2024, FN-ALP)
  23 --> 37 (Babu 2025, gauged U(1)_F)
  34 (Ding-Valle 2025, symmetry approach) --> 35 (EPJ 2025, flavor problem)
  33 (Antusch 2025, running masses) --> 34
  33 --> 23

COSMOLOGICAL OBSERVATIONS
  12 (Planck 2015) --> 18 (DESI DR1 2024)
  18 --> 19 (DESI DR2 2025)
  18 --> 30 (DESI Nature 2025, dynamical DE)
  19 --> 30
  10 (Williams LLR) --> 39 (March 2025, LLR + DESI)
  11 (Coldea 2010, golden ratio E8) --> 03 [Paasch cites for golden ratio]

EMPIRICAL MASS SPECTRA
  32 (PDG 2024) --> 33 [running masses use PDG input]
  42 (Giani 2004) --> 31 (Palazzi 2003)
  27 (Gross-Vitells 2010, LEE) --> 45 (Washburn 2025, harmonic cascade)

CROSS-THEME LINKS
  03 <--> 07  [both predict tau mass from algebraic structure]
  04 <--> 16  [both derive alpha geometrically; Paasch 0.9 ppm, Wyler 0.6 ppm]
  04 <--> 46  [alpha derivability vs domain-specific quantity]
  09 <--> 24  [both derive SM from Clifford algebra]
  11 <--> 03  [golden ratio in quantum criticality and mass ratios]
  20 <--> 41  [NCG and octonionic approaches to mass ratios]
  21,22 <--> 20  [spectral action at finite density]
  27 <--> all mass formulas [look-elsewhere effect must be assessed]
  38,44 <--> 06,08  [LNH reviews vs original Dirac papers]
```

## Topic Map

### Paasch Core & Logarithmic Mass
Papers: 02, 03, 04, 05, 13, 31
The three Paasch papers (02, 03, 04) form the core of the mass quantization program. Paper 02 (2009) derives phi = 1.53158 from x = e^{-x^2} and organizes particles into six sequences on a logarithmic spiral at 45-degree separation. Paper 03 (2016) constructs the exponential mass model spanning Planck mass to observable universe, derives proton mass to 6 digits and neutron to 8, discovers integer mass numbers N(j) = 7n, and finds the golden ratio in successive M-value ratios. Paper 04 (2016) derives alpha = 0.007297359 (0.9 ppm) from n3=10 and f = 0.5671 (solution of ln(x) = -x). Muraki (05) and Nambu (13) are the direct ancestors; Palazzi (31) provides the complementary stabline analysis.

### Fine Structure Constant & Geometric Alpha
Papers: 14, 16, 28, 46
Attempts to derive alpha from mathematical or geometric first principles, spanning nearly a century. Eddington (14, 1929) counted Clifford algebra elements (136+1=137), establishing the tradition. Wyler (16, 1969) computed symmetric-space volumes to achieve sub-ppm accuracy (alpha = 1/137.036082, ~0.6 ppm). Gsponer-Hurni (28, 1996) extended Barut's N^4 lepton formula to quarks via non-linear field theory. Sticker (46, 2024) argues alpha is a domain-specific scaled quantity, not mathematically derivable -- a direct philosophical challenge to the entire program.

### Koide Formula & Mass Relations
Papers: 07, 09, 40, 47
The Koide formula Q = (m_e + m_mu + m_tau)/(sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3 holds to 0.001% and successfully predicted m_tau = 1776.97 MeV (confirmed 1992). Paper 07 (1983) establishes the formula from a preon model. Paper 47 (2018) reviews Koide's own field-theoretic derivation from U(3) family symmetry and the Sumino mechanism protecting pole masses from running. Paper 40 (2021) extends the formula to quarks via SU(3) flavor nonets. Zenczykowski (09, 2008) derives one SM generation from Cl(6) phase-space linearization, arguing mass has algebraic origin.

### Large Number Hypothesis & Varying Constants
Papers: 06, 08, 10, 15, 38, 43, 44
Dirac's LNH (08, 1937; 06, 1974) requires G proportional to 1/t, the cosmological premise for Paasch's Paper 03. Williams et al. (10, 2004) constrains |G-dot/G| < 9e-13 yr^{-1}, ruling out Dirac's 1/t by ~100x. Barrow (15, 2005) develops the BSBM varying-alpha theory where Lambda freezes alpha evolution. Uzan (43, 2024) comprehensively reviews all varying-constants constraints and theoretical frameworks. Ray et al. (44, 2007) and Jiang et al. (38, 2025) are LNH-specific reviews connecting to modern cosmology and holographic principles.

### NCG & Spectral Action
Papers: 20, 21, 22, 24, 25, 41
Van Suijlekom (20, 2024) is the definitive textbook on NCG and particle physics: spectral triples, almost-commutative manifolds, SM from geometry, Pati-Salam extensions. Chamseddine-Connes-vS (22, 2018) prove entropy = spectral action and connect heat expansion coefficients to the Riemann zeta function. Dong-Khalkhali-vS (21, 2019) extend to second quantization with chemical potential; all coefficients expressible via Bessel functions. Furey (24, 25) derives SM representations from division algebras (C tensor H tensor O) via Z_2^5-graded Jordan algebra H_16(C). Singh (41, 2022) uses octonionic NCG to predict mass ratios.

### Flavor Symmetry & Mass Hierarchy
Papers: 23, 26, 33, 34, 35, 36, 37
The Froggatt-Nielsen mechanism produces exponential mass hierarchies from O(1) charge differences under a U(1) flavor symmetry. Paper 23 (2025) provides the first comprehensive Bayesian exploration of FN charge assignments. Greljo et al. (36, 2024) discover the FN mechanism generically predicts an axion-like particle. Babu et al. (37, 2025) unify flavor hierarchy, strong CP, dark matter, and baryon asymmetry via gauged U(1)_F. Ding-Valle (34, 2025) review discrete flavor symmetries (A4, S4, modular). Antusch (33, 2025) provides state-of-the-art running Yukawa masses at all scales. Kosinov (26, 2024) connects the Koide formula to alpha explicitly.

### Cosmological Observations (DESI/Planck/LLR)
Papers: 11, 12, 18, 19, 30, 39
Planck (12, 2015) establishes the LCDM baseline: Omega_m = 0.316, H_0 = 67.3, w = -1.02 +/- 0.08. DESI DR1 (18, 2024) hints at dynamical dark energy at 2.5-3.9 sigma. DESI DR2 (19, 2025) strengthens the preference to 3.1-4.2 sigma. The Nature paper (30, 2025) confirms w(z) crossing -1 near z~0.4 using non-parametric reconstruction. March et al. (39, 2025) combine DESI+LLR to constrain nonminimal-coupling gravity. Coldea et al. (11, 2010) observe the golden ratio m2/m1 = 1.618 in E8 quantum critical excitations.

### Statistical Methods & Empirical Mass Spectra
Papers: 17, 27, 29, 32, 35, 42, 45
The look-elsewhere effect (27, Gross-Vitells 2010) is methodologically mandatory for assessing any mass formula's significance. MacGregor (17, 2007) provides the most comprehensive alpha-quantized mass and lifetime analysis. The PDG (32, 2024) is the experimental benchmark. Giani (42, 2004) catalogues ~50 empirical mass patterns. Washburn-Allahyarov (45, 2025) derive all 12 fermion masses from the golden ratio and 3-cube geometry with zero free parameters, verified in Lean 4. Hitchin (29, 2025) surveys the mathematical foundations of the Dirac operator.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Paasch's phi = 1.53158 and spiral structure | 02, 03, 04 | CRITICAL |
| Verifying Paasch mass values against PDG | 32, 03, 33 | CRITICAL |
| DESI w(z) as observational test | 18, 19, 30, 39 | CRITICAL |
| Spectral action coefficients and entropy | 20, 22, 21 | CRITICAL |
| Koide formula and tau mass prediction | 07, 47, 40, 26 | HIGH |
| Alpha derivation attempts (Paasch/Wyler/Eddington) | 04, 16, 14, 46 | HIGH |
| Froggatt-Nielsen mechanism and mass hierarchy | 23, 36, 37, 35 | HIGH |
| Division algebra / octonionic mass ratios | 24, 25, 09, 41 | HIGH |
| Running Yukawa masses at all energy scales | 33, 34 | HIGH |
| G-dot constraints on LNH | 10, 43, 06, 08 | MEDIUM |
| Golden ratio in quantum physics | 11, 03, 45 | MEDIUM |
| Mass quantization: alpha-based (70 MeV quanta) | 17, 13, 42 | MEDIUM |
| Logarithmic mass trajectories | 05, 02, 31 | MEDIUM |
| Look-elsewhere effect / trial factors | 27 | MEDIUM |
| Barut N^4 formula and non-linear field theory | 28 | MEDIUM |
| Dirac operator mathematics | 29 | MEDIUM |
| LNH reviews and modern status | 38, 44, 15 | MEDIUM |
| Planck cosmological parameters | 12 | MEDIUM |
| LLR + evolving dark energy combined | 39 | MEDIUM |

---

## Paper Entries

### Paper 02: The Logarithmic Potential and an Exponential Mass Function for Elementary Particles
- **File**: `02_2009_Logarithmic_potential_exponential_mass_function_elementary_particles.md`
- **arXiv**: N/A (Progress in Physics, Vol. 1, Jan 2009)
- **Year**: 2009
- **Relevance**: CRITICAL
- **Tags**: phi_paasch, logarithmic potential, mass quantization, spiral, exponential mass function

**Summary**: Foundational Paasch paper. Derives the quantization factor phi = 1.53158 from the transcendental equation x = e^{-x^2}, phi = 1/x. Establishes the logarithmic spiral organization of particle masses into six sequences S1-S6 at 45-degree separation. The spiral constant k = (1/2pi) ln phi. All allocations accurate within delta_m/m = 4e-3.

**Key Results**:
- phi = 1.53158 from x = e^{-x^2} (Eq. 2g)
- Logarithmic spiral: m_n = m_0 * e^{k*phi_n} (Eq. 2k)
- Six principal sequences S1-S6 at 45-degree intervals
- Electron at 0 degrees, muon at 182 degrees, proton at 225 degrees
- Changes delta_phi/phi ~ 5e-4 disrupt sequences
- Planck mass falls on sequence S6

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| x = e^{-x^2} | Transcendental equation for quantization factor | Eq. (2f) |
| phi = 1/x = 1.53158 | Mass quantization factor | Eq. (2g) |
| m_n = m_0 * e^{k*phi_n} | Exponential mass function | Eq. (2k) |
| k = (1/2pi) ln phi | Spiral constant | Eq. (2j) |
| E = a1 * ln(R/Ra) | Logarithmic confining potential | Eq. (2a) |

**Dependencies**: Builds on 05 (Muraki), cites PDG 2004. Upstream of 03, 04.

---

### Paper 03: On the Calculation of Elementary Particle Masses
- **File**: `03_2016_On_the_calculation_of_elementary_particle_masses.md`
- **arXiv**: N/A (HAL hal-01368054v3)
- **Year**: 2016
- **Relevance**: CRITICAL
- **Tags**: proton mass, neutron mass, mass numbers, golden ratio, equilibrium mass, LNH

**Summary**: Constructs an exponential model spanning Planck mass to observable universe with G(t) ~ 1/t (Dirac LNH). Introduces the generalized equilibrium mass m*(i,j) = (m_i * m_j)^{1/2}. Derives proton mass to 6 decimal digits (1.67262110e-27 kg), neutron mass to 8 digits (1.67492745e-27 kg), tau mass to 5 digits. Discovers integer mass numbers N(j) = 7n and the golden ratio phi = 0.618 in successive M-value ratios.

**Key Results**:
- m_proton = 1.67262110e-27 kg (measured: 1.67262210e-27, delta_m/m = 6e-7)
- m_neutron = 1.67492745e-27 kg (measured: 1.67492747e-27, delta_m/m ~ 1e-8)
- m_tau = 3.16747e-27 kg (measured: 3.16747e-27, delta_m/m ~ 1e-5)
- Mass numbers: N(mu)=35, N(pi)=42, N(K)=98, N(eta)=105, N(rho,omega)=133, N(K*)=145, N(p,n)=150
- N(j) = 7n for j = mu through rho/omega
- M(i+1)/[2*M(i)] approaches golden ratio 0.618034
- f_N = 2*phi_golden = 1.23607 (exponential scaling factor)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| m*(e,j) = (m_e * m_j)^{1/2} | Generalized equilibrium mass | Eq. (5.0a) |
| N(j) = (m*(e,j)/m_e)^{2/3} | Mass number definition | Eq. (5.1) |
| M(j) = (m_j/m_e)^{1/3} | M-value definition | Eq. (5.4) |
| f_N = M(i+1)/M(i) = 2*phi = 1.23607 | Exponential scaling factor | Eq. (5.5) |
| m_E = (m_e * m_p)^{1/2} | Equilibrium mass | Eq. (3.0) |
| m_p = f(m_e, alpha, N(b)=112, n3=10) | Proton mass formula | Eq. (6.6)-(6.8) |

**Dependencies**: Cites 06 (Dirac LNH) as [1], 07 (Koide) as [2], 11 (Coldea golden ratio) as [7], 09 (Zenczykowski) as [8]. Upstream of 04.

---

### Paper 04: The Derivation of the Fine Structure Constant
- **File**: `04_2016_Derivation_of_the_fine_structure_constant.md`
- **arXiv**: N/A (HAL hal-01375989v3)
- **Year**: 2016
- **Relevance**: CRITICAL
- **Tags**: fine structure constant, alpha derivation, logarithmic potential, n3=10

**Summary**: Derives alpha = 0.007297359 (measured: 0.007297353, delta/alpha = 8e-7 = 0.9 ppm) from the proton mass framework of Paper 03 combined with a logarithmic potential for constituent masses. The result depends solely on n3 = 10 (from the proton mass derivation) and f = 0.5671433 (solution of ln(x) = -x). Independent of epsilon_0, e, hbar, c.

**Key Results**:
- alpha = (1/n3^2) * (f/2)^{1/4} = (1/100) * (0.5671/2)^{1/4} = 0.007297359
- Measured: 0.0072973525693(11), relative deviation 0.9 ppm
- f = 0.5671433 from ln(f) = -f (Eq. 2.6)
- n3 = 10 from proton mass quantization (Paper 03, Eq. 6.4)
- Result independent of epsilon_0, e, hbar, c

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| ln(f) = -f, f = 0.5671433 | Transcendental equation for constituent spacing | Eq. (2.6) |
| alpha = (1/n3^2) * (f/2)^{1/4} | Fine structure constant | Eq. (2.9) |
| E = s1 * ln(R/Ra) | Logarithmic confining potential | Eq. (2.3) |
| E = (n+1)*hbar*omega | Harmonic oscillator quantization | Eq. (2.4) |

**Dependencies**: Depends on 03 for n3=10 and equilibrium mass framework. Cites 03 as [1].

---

### Paper 05: Logarithmic Mass Formulae for Elementary Particles and a New Quantum Number
- **File**: `05_1978_Muraki_Logarithmic_mass_formulae.md`
- **arXiv**: N/A (Lett. Nuovo Cim. 23, 27)
- **Year**: 1978
- **Relevance**: HIGH
- **Tags**: logarithmic mass formula, integer quantum number, mass trajectories

**Summary**: Direct ancestor of Paasch's framework. Proposes ln(m/m_0) = a*n + b, where n is an integer quantum number, demonstrating that hadrons and leptons fall on approximately linear trajectories in log-mass space. Multiple parallel trajectories share a common slope a, suggesting a universal exponential mass-generation scale.

**Key Results**:
- Mass formula: m_i = m_0 * e^{a*n_i + b} (exponential/geometric mass spectrum)
- Multiple trajectories with common slope, different intercepts
- Deviations from integer spacing are few percent or less
- The "new quantum number" n has no SM counterpart

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| ln(m/m_0) = a*n + b | Logarithmic mass formula | Central result |
| m_{n+1}/m_n = e^a | Constant ratio on trajectory | Derived |

**Dependencies**: Builds on 13 (Nambu). Directly cited by 02 (Paasch).

---

### Paper 06: Cosmological Models and the Large Numbers Hypothesis
- **File**: `06_1974_Dirac_LNH_cosmological_models.md`
- **arXiv**: N/A (Proc. Roy. Soc. A 338, 439)
- **Year**: 1974
- **Relevance**: HIGH
- **Tags**: LNH, varying G, matter creation, cosmological models

**Summary**: Dirac's mature presentation of the LNH. Derives G ~ 1/t from requiring N1 ~ N2, yielding G-dot/G ~ -7e-11 yr^{-1}. Two cosmological models: additive creation (R ~ t^{1/3}) and multiplicative creation (R ~ t, individual masses grow). This specific paper is cited as [1] in Paasch's Paper 03.

**Key Results**:
- G ~ 1/t (decreasing gravitational constant)
- G-dot/G ~ -1/t_0 ~ -7e-11 yr^{-1}
- Continuous matter creation required (N ~ t^2)
- Model A: additive creation, R ~ t^{1/3}
- Model B: multiplicative creation, R ~ t

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| N1 = e^2/(4pi*eps0*G*m_p*m_e) ~ 2.3e39 | EM-to-gravitational force ratio | Large number |
| G ~ 1/t | Time variation of G | Core prediction |

**Dependencies**: Extends 08 (Dirac 1937). Cited by 03 as cosmological foundation. Constrained by 10 (LLR).

---

### Paper 07: A Fermion-Boson Composite Model of Quarks and Leptons (Koide Formula)
- **File**: `07_1983_Koide_Lepton_mass_formula.md`
- **arXiv**: N/A (Phys. Lett. B 120, 161)
- **Year**: 1983
- **Relevance**: HIGH
- **Tags**: Koide formula, lepton masses, Q=2/3, tau prediction

**Summary**: Establishes the Koide formula Q = (m_e + m_mu + m_tau)/(sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau))^2 = 2/3, holding to 0.001% accuracy. Q = 2/3 is the midpoint of the allowed range [1/3, 1]. Predicted m_tau = 1776.97 MeV in 1982, confirmed by 1992 remeasurement.

**Key Results**:
- Q = 2/3 to 6e-6 precision (0.0009%)
- m_tau predicted: 1776.97 MeV (measured: 1776.86 +/- 0.12)
- Q is midpoint of allowed range [1/3, 1]
- Trigonometric form: m_k = (M/3)(1 + sqrt(2)*cos(2pi*k/3 + delta))^2 with delta = 2/9

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Q = (m_e+m_mu+m_tau)/(sqrt(m_e)+sqrt(m_mu)+sqrt(m_tau))^2 = 2/3 | Koide formula | Central result |
| m_k = (M/3)(1+sqrt(2)*cos(2pi*k/3+2/9))^2 | Brannen trigonometric form | Brannen 2006 |

**Dependencies**: Cited by 03, 26, 40, 47. Z_3 structure connects to Peter-Weyl triality.

---

### Paper 08: The Cosmological Constants (Dirac 1937)
- **File**: `08_1937_Dirac_Cosmological_constants_LNH.md`
- **arXiv**: N/A (Nature 139, 323)
- **Year**: 1937
- **Relevance**: MEDIUM
- **Tags**: LNH origin, large dimensionless numbers, varying G, Weyl-Eddington ratio

**Summary**: The ORIGINAL paper proposing the LNH. Dirac observes that dimensionless ratios from fundamental constants cluster around 10^{40} and 10^{80}, proposes they are related, which requires G ~ 1/t. Launched the entire varying-constants research program.

**Key Results**:
- N1 ~ N2 ~ 10^{40}, N3 ~ N1^2 ~ 10^{80}
- G ~ 1/t required to maintain N1 ~ N2
- First proposal that "constants" may vary
- Matter creation required for N3 ~ N1^2

**Dependencies**: Precursor to 06. Motivated 10 (LLR experiments), Brans-Dicke theory.

---

### Paper 09: Clifford Algebra of Nonrelativistic Phase Space and the Concept of Mass
- **File**: `09_2015_Zenczykowski_Mass_quantization_algebraic.md`
- **arXiv**: 0806.1823
- **Year**: 2008
- **Relevance**: HIGH
- **Tags**: Clifford algebra, Cl(6), phase space, SM quantum numbers, algebraic mass

**Summary**: Derives one SM generation from Cl(6) via Dirac-like linearization of the phase-space invariant p^2 + x^2. Hypercharge eigenvalues Y = +1/3 (quarks) and Y = -1 (leptons) emerge naturally. Individual quark mass elements are NOT rotationally invariant; rotational invariance is restored upon colour summation. Argues mass has "algebraic origin." Cited by Paasch (Paper 03, [8]).

**Key Results**:
- One SM generation from Cl(6) phase-space linearization
- Hypercharge Y = +1/3 (quarks), Y = -1 (leptons) from algebra
- Colour = three degenerate hypercharge constructions
- Quark mass = rotationally invariant only after colour sum

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| R_z = p^2 + x^2 | Phase-space invariant | Section 1 |
| Y = (1/3) sum_k Y_k | Hypercharge operator | Eqs. (4)-(5) |

**Dependencies**: Connected to 24, 25 (Furey), 41 (Singh). Cited by 03 (Paasch).

---

### Paper 10: Progress in Lunar Laser Ranging Tests of Relativistic Gravity
- **File**: `10_2004_Williams_LLR_varying_G_constraints.md`
- **arXiv**: gr-qc/0411113
- **Year**: 2004
- **Relevance**: MEDIUM
- **Tags**: LLR, G-dot, equivalence principle, PPN parameters

**Summary**: LLR constrains G-dot/G = (4 +/- 9) x 10^{-13} yr^{-1}. This is 83x smaller than 1/t_0, ruling out Dirac's G ~ 1/t by ~100x. Also constrains EP, geodetic precession, and PPN parameter beta.

**Key Results**:
- G-dot/G = (4 +/- 9) x 10^{-13} yr^{-1}
- EP test: Delta(M_G/M_I) = (-1.0 +/- 1.4) x 10^{-13}
- PPN beta - 1 = (1.2 +/- 1.1) x 10^{-4}
- Dirac's G ~ 1/t excluded by factor ~100

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| G-dot/G = (4 +/- 9) x 10^{-13} yr^{-1} | G variation constraint | Eq. (9) |

**Dependencies**: Constrains 06, 08 (Dirac LNH). Feeds into 15, 43 (varying constants reviews).

---

### Paper 11: Quantum Criticality in an Ising Chain: Experimental Evidence for Emergent E8 Symmetry
- **File**: `11_2010_Coldea_Golden_ratio_E8_quantum_criticality.md`
- **arXiv**: 1103.3694
- **Year**: 2010
- **Relevance**: MEDIUM
- **Tags**: E8, golden ratio, quantum criticality, CoNb2O6, Zamolodchikov

**Summary**: First experimental observation of emergent E8 symmetry near a quantum critical point in CoNb2O6. Two excitation modes near criticality have mass ratio approaching golden ratio m2/m1 = 1.618, as predicted by Zamolodchikov. Cited by Paasch (Paper 03, [7]) as evidence for golden ratio in quantum systems.

**Key Results**:
- m2/m1 approaches golden ratio 1.618 near quantum critical point
- E8 spectrum with 8 mesonic bound states predicted by Zamolodchikov
- Five kink-confinement bound states observed (Airy function zeros)
- J = 1.94 meV exchange coupling in CoNb2O6

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| m2/m1 = (1+sqrt(5))/2 = 1.618... | E8 golden ratio prediction | Zamolodchikov |

**Dependencies**: Cited by 03 (Paasch) for golden ratio physics.

---

### Paper 12: Planck 2015 Results. XIII. Cosmological Parameters
- **File**: `12_2015_Planck_Cosmological_parameters.md`
- **arXiv**: 1502.01589
- **Year**: 2015
- **Relevance**: HIGH
- **Tags**: CMB, LCDM, Omega_m, H_0, dark energy, neutrino mass

**Summary**: Establishes the LCDM baseline from full Planck mission data. Six-parameter LCDM provides excellent fit. H_0 = 67.27 +/- 0.66, Omega_m = 0.3156, w = -1.019 +/- 0.08. Neutrino mass sum < 0.23 eV.

**Key Results**:
- H_0 = 67.27 +/- 0.66 km/s/Mpc (3.4 sigma tension with local measurement)
- Omega_m = 0.3156 +/- 0.0091
- w = -1.019 +/- 0.08 (consistent with cosmological constant)
- N_eff = 3.13 +/- 0.32
- Sum m_nu < 0.23 eV (95% CL)

**Dependencies**: Baseline for 18, 19, 30 (DESI). Cited by 03 (Paasch) as [4].

---

### Paper 13: An Empirical Mass Spectrum of Elementary Particles
- **File**: `13_1952_Nambu_Empirical_mass_spectrum.md`
- **arXiv**: N/A (Prog. Theor. Phys. 7, 595)
- **Year**: 1952
- **Relevance**: HIGH
- **Tags**: Nambu, mass quantization, alpha, m_mu/m_e, 70 MeV

**Summary**: The founding paper of empirical mass quantization. Nambu observes m_mu/m_e ~ 3/(2*alpha) = 205.5 (0.6% accuracy) and that particle masses are approximately integer multiples of m_e/alpha ~ 70 MeV. Established the tradition that Muraki, MacGregor, and Paasch continued.

**Key Results**:
- m_mu/m_e ~ 3/(2*alpha) = 205.5 (measured: 206.768, 0.6% agreement)
- Mass quantum: m_0 = m_e/alpha ~ 70 MeV
- Pion: m_pi ~ 2*m_0, Kaon: m_K ~ 7*m_0
- Purely empirical; no dynamical model

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| m_mu/m_e ~ 3/(2*alpha) | Muon-electron mass relation | Central result |
| m_0 = m_e/alpha ~ 70 MeV | Fundamental mass unit | Derived |

**Dependencies**: Ancestor of 05, 17, and ultimately 02-04 (Paasch).

---

### Paper 14: The Charge of an Electron (Eddington 1929)
- **File**: `14_1929_Eddington_Fine_structure_constant_derivation.md`
- **arXiv**: N/A (Proc. Roy. Soc. A 122, 358)
- **Year**: 1929
- **Relevance**: MEDIUM
- **Tags**: alpha derivation, Clifford algebra, 136+1=137, Eddington number

**Summary**: First attempt to derive alpha from pure algebra. Eddington counts symmetric combinations of two-electron Dirac algebra elements: 16*17/2 = 136, then adds +1 for exclusion principle to get alpha^{-1} = 137. Universally considered a failure, but established the question "is alpha derivable?" that remains open.

**Key Results**:
- alpha^{-1} = 136 from symmetric tensor counting (wrong)
- Revised to 137 with ad hoc +1 correction
- m_p/m_e "derived" as 1847.6 (actual: 1836.2, 0.6% error)
- Cautionary example of numerological physics

**Dependencies**: Precursor to 16 (Wyler), 04 (Paasch alpha derivation).

---

### Paper 15: Varying Constants (Barrow 2005)
- **File**: `15_2005_Barrow_Varying_constants_review.md`
- **arXiv**: astro-ph/0511440
- **Year**: 2005
- **Relevance**: MEDIUM
- **Tags**: varying alpha, BSBM theory, cosmological constant, virialisation

**Summary**: Reviews varying-constants theories. Develops the BSBM theory where alpha varies logarithmically during dust era but freezes when Lambda dominates (z ~ 0.7). Key insight: local observations are inside gravitational overdensities 10^{30}x denser than background; laboratory bounds on alpha may not track cosmological evolution.

**Key Results**:
- BSBM: alpha ~ 2N*log(t) during dust era
- Lambda freezes alpha variation at z ~ 0.7
- Virialisation problem: local != cosmological alpha variation
- WEP violations predicted at ~10^{-13} level

**Dependencies**: Builds on 10 (LLR constraints), 08 (Dirac). Feeds into 43 (Uzan review).

---

### Paper 16: L'espace symetrique du groupe des equations de Maxwell (Wyler 1969)
- **File**: `16_1969_Wyler_Geometric_alpha_derivation.md`
- **arXiv**: N/A (C. R. Acad. Sci. Paris 269, A743)
- **Year**: 1969
- **Relevance**: HIGH
- **Tags**: alpha derivation, symmetric space, Shilov boundary, conformal group

**Summary**: Most numerically accurate "derivation" of alpha. Computes alpha from the volume of the Shilov boundary of D5 = SO(5,2)/(SO(5) x SO(2)): alpha_W = (9/8pi^4)(pi^5/1920)^{1/4} = 1/137.0360824. Agreement with CODATA 2018: ~0.6 ppm. Called "a number in search of a theory" (Adler 1972).

**Key Results**:
- alpha_W = (9/8pi^4)(pi^5/(2^4*5!))^{1/4} = 0.00729735253
- Agreement: ~0.6 ppm vs CODATA 2018
- Uses conformal group SO(4,2) / symmetric space D5
- No dynamical framework provided

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| alpha_W = (9/8pi^4)(pi^5/1920)^{1/4} | Wyler's constant | Main result |

**Dependencies**: Extends 14 (Eddington tradition). Compare with 04 (Paasch: 0.9 ppm).

---

### Paper 17: The Power of Alpha
- **File**: `17_2007_MacGregor_Power_of_alpha_mass_quantization.md`
- **arXiv**: N/A (World Scientific, 2007)
- **Year**: 2007
- **Relevance**: MEDIUM
- **Tags**: alpha quantization, 70 MeV, lifetime grid, relativistic spinning sphere

**Summary**: Most comprehensive compilation of alpha-quantized mass and lifetime patterns. Masses quantized in units of m_e/alpha ~ 70 MeV (and 3*m_e/(2*alpha) = 105 MeV). Lifetimes cluster at tau ~ tau_0 * alpha^n. Mass-interval agreements at 5-10% level. Proposes relativistic spinning sphere model.

**Key Results**:
- Mass quantum: m_e/alpha ~ 70 MeV
- Secondary quantum: 3*m_e/(2*alpha) = 105 MeV = m_mu
- Lifetime grid: tau ~ alpha^n (factor ~137 between levels)
- ~5-10% mass-interval agreements
- Connects mass AND lifetime patterns via alpha

**Dependencies**: Builds on 13 (Nambu). Parallel to 02-04 (Paasch uses phi, MacGregor uses alpha).

---

### Paper 18: DESI 2024 VI: Cosmological Constraints from BAO
- **File**: `18_2024_DESI_VI_BAO_Cosmological_Constraints.md`
- **arXiv**: 2404.03002
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: DESI, BAO, dark energy, w0-wa, dynamical DE

**Summary**: DESI DR1 BAO measurements across 0.1 < z < 4.2. Combined with CMB+SN, preference for dynamical dark energy at 2.5-3.9 sigma (depending on SN dataset). w_0 > -1, w_a < 0.

**Key Results**:
- DESI+CMB: Omega_m = 0.307 +/- 0.005, H_0 = 67.97 +/- 0.38
- w_0 = -0.45 +/- 0.21 (Pantheon+), w_a = -1.79
- LCDM preference: 2.5 sigma (Pantheon+), 3.9 sigma (Union3)
- Sum m_nu < 0.072 eV (95% CL, flat LCDM)

**Dependencies**: Uses 12 (Planck) as CMB prior. Extended by 19, 30.

---

### Paper 19: DESI DR2 Results II: BAO and Cosmological Constraints
- **File**: `19_2025_DESI_DR2_BAO_Dark_Energy_Evolution.md`
- **arXiv**: 2503.14738
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: DESI DR2, dynamical dark energy, w crossing -1, phantom divide

**Summary**: DESI DR2 (~3x DR1 statistical power). Strengthens dynamical DE preference to 3.1-4.2 sigma. w(z) crosses -1 at intermediate redshift. Signal persists from DR1 to DR2 -- not a fluctuation.

**Key Results**:
- w_0 = -0.752 +/- 0.154 (DESI+CMB+DESY5)
- w_a = -0.86 (+0.43/-0.38)
- Preference over LCDM: 3.1-4.2 sigma
- w = -1 crossing robust across SN datasets and non-parametric methods

**Dependencies**: Updates 18 (DESI DR1). Analyzed in 30.

---

### Paper 20: Noncommutative Geometry and Particle Physics (2nd Edition)
- **File**: `20_2024_van_Suijlekom_NCG_Particle_Physics_2ed.md`
- **arXiv**: N/A (Springer, 2024)
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: NCG, spectral triple, spectral action, almost-commutative, SM from geometry, KO-dimension

**Summary**: Definitive textbook. Spectral triple (A, H, D) encodes geometry. Inner fluctuations give gauge fields. Spectral action Tr(f(D/Lambda)) produces SM Lagrangian coupled to gravity from almost-commutative manifold M x F_SM. KO-dimension 6 for SM. Covers finite NCG, Morita equivalence, Connes distance formula, spectral invariants, electrodynamics, Yang-Mills, full SM, Pati-Salam, and second quantization.

**Key Results**:
- SM Lagrangian from spectral action on M x F_SM
- KO-dimension k=6 determines sign table for J, D, gamma
- Finite spectral triple classification via Krajewski diagrams
- Gauge couplings from spectral action coefficients
- Higgs mechanism from inner fluctuations

**Dependencies**: Foundation for 21, 22. Parallel to 24, 25 (Furey division algebras).

---

### Paper 21: Second Quantization and the Spectral Action
- **File**: `21_2019_Dong_Khalkhali_vS_Second_Quantization_Spectral_Action.md`
- **arXiv**: 1903.09624
- **Year**: 2019
- **Relevance**: CRITICAL
- **Tags**: spectral action, second quantization, chemical potential, Bessel functions, grand partition

**Summary**: Constructs bosonic and fermionic second quantization of spectral triples with chemical potential mu. Von Neumann entropy and average energy of Gibbs state are spectral actions. All coefficients expressible in terms of modified Bessel functions K_nu. Recovers Chamseddine-Connes-vS result at mu = 0.

**Key Results**:
- Fermionic partition: Z_f = det(1 + exp(-beta(|D|-mu)))
- Bosonic partition: Z_b = det(1 - exp(-beta(|D|-mu)))^{-1}
- All spectral action coefficients = modified Bessel functions
- At mu = 0: recovers Riemann zeta function coefficients (Paper 22)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Z_f = det(1+exp(-beta(|D|-mu))) | Fermionic grand partition | Theorem |
| gamma_f(a,y) = (2/Gamma(a)) sum (-1)^{n+1} (ny)^a K_a(ny)/n | Fermionic spectral coefficient | Main result |

**Dependencies**: Extends 22 (CCS entropy). Uses framework from 20.

---

### Paper 22: Entropy and the Spectral Action
- **File**: `22_2019_Chamseddine_Connes_vS_Entropy_Spectral_Action.md`
- **arXiv**: 1809.02944
- **Year**: 2018
- **Relevance**: CRITICAL
- **Tags**: entropy, spectral action, Riemann zeta, heat expansion, KMS state

**Summary**: Proves the von Neumann entropy of the fermionic KMS state equals the spectral action Tr(h(beta*D)) with test function h(x) = E(e^{-x}). Heat expansion coefficients are products of Riemann xi function and elementary expressions: c(4) ~ zeta(5), c(2) ~ zeta(3). Functional equation gives duality between positive and negative dimensions.

**Key Results**:
- Entropy = spectral action (Theorem 3.4)
- h(x) = E(e^{-x}), E(t) = log(1+t) - t*log(t)/(1+t)
- gamma(a) = (1-2^{-2a})/a * pi^{-a} * xi(2a)
- c(4) = (225/4)*zeta(5), c(2) = (9/2)*zeta(3)
- Dimension duality from Riemann functional equation

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| S = Tr(h(beta*D)) | Entropy as spectral action | Theorem 3.4 |
| gamma(a) = (1-2^{-2a})/a * pi^{-a} * xi(2a) | Heat expansion coefficient | Main result |

**Dependencies**: Extended by 21 (with chemical potential). Foundation in 20.

---

### Paper 23: Comprehensive Bayesian Exploration of Froggatt-Nielsen Mechanism
- **File**: `23_2025_Bauer_Froggatt_Nielsen_Mechanism_Bayesian.md`
- **arXiv**: 2412.19484
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: Froggatt-Nielsen, Bayesian, flavor hierarchy, neutrino mass, nucleon decay

**Summary**: First systematic Bayesian exploration of FN charge assignments covering both quark and lepton sectors. Negative FN charges found viable. Both seesaw and dim-5 neutrino scenarios equally preferred. Predictions for lightest neutrino mass and neutrinoless double-beta decay presented.

**Key Results**:
- Wide range of FN charges consistent with observed masses/mixings
- Negative charges and large generational differences viable
- No strong seesaw vs dim-5 preference
- Nucleon decay lifetime/branching ratios differentiate FN models

**Dependencies**: Related to 36 (FN-ALP), 37 (gauged U(1)_F). Uses 33 (running masses).

---

### Paper 24: A Superalgebra Within: Z_2^5-Graded Algebra from SM Representations
- **File**: `24_2025_Furey_Superalgebra_Within_Z2_Graded.md`
- **arXiv**: 2505.07923
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: division algebras, Jordan algebra, H_16(C), Z_2^5 grading, Bott periodicity, top quark

**Summary**: SM particle representations (minus top quark) collectively form H_16(C), a 256-dimensional Euclidean Jordan algebra generated by C tensor H tensor O. The Z_2^5 grading produces su(3)_C + su(2)_L + u(1)_Y as internal symmetry. Three fermion generations arise from 3*64 partition. Top quark exclusion suggests compositeness.

**Key Results**:
- SM = H_16(C) Jordan algebra (256_R dimensions)
- Z_2^5 grading yields SM gauge algebra
- Three generations from 3*64 partition
- Top quark excluded (compositeness hint)
- Connects to Bott periodicity / AZ class BDI

**Dependencies**: Part of Furey program with 25. Parallel to 09 (Zenczykowski Cl(6)), 41 (Singh octonions).

---

### Paper 25: An Algebraic Roadmap of Particle Theories, Part I
- **File**: `25_2025_Furey_Algebraic_Roadmap_Particle_Theories.md`
- **arXiv**: 2312.12377
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: division algebras, Spin(10), Pati-Salam, SU(5), algebraic symmetry breaking

**Summary**: Maps network of algebraic connections between six particle theories (Spin(10), Georgi-Glashow, Pati-Salam, Left-Right Symmetric, SM pre/post-Higgs). All arise from division algebra operator spaces. SM gauge group = intersection of SU(5) and Pati-Salam (Baez-Huerta). Quaternionic reflection differentiates W+/- from Z0.

**Key Results**:
- Nine algebraic models form a connected network
- SM gauge group = SU(5) intersect Pati-Salam within Spin(10)
- Symmetry breaking driven by algebraic constraints, not arbitrary Higgs
- One generation from Cl(6); three from Cl(8) via C tensor H tensor O

**Dependencies**: Foundation for 24. Uses Baez-Huerta intersection theorem.

---

### Paper 26: Koide Formula and the Connection to the Fine-Structure Constant alpha
- **File**: `26_2024_Kosinov_Koide_Formula_Fine_Structure_Constant.md`
- **arXiv**: N/A (SSRN:4992875)
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: Koide, alpha, tau prediction, Nambu-Barut-Paasch tradition

**Summary**: Proposes an extended Koide formula incorporating the proton mass and alpha. Predicts m_tau = 1776.7586 MeV (PDG: 1776.86 +/- 0.12). Extends the Nambu-Barut-Paasch tradition of relating particle masses to alpha. Comparable precision to original Koide formula.

**Key Results**:
- m_tau predicted: 1776.7586 MeV via alpha-extended formula
- Connects Koide (lepton algebraic) and Paasch (alpha quantization) programs
- Incorporates proton mass and alpha as fundamental parameters

**Dependencies**: Extends 07 (Koide), 28 (Barut/Gsponer), 04 (Paasch alpha).

---

### Paper 27: Trial Factors for the Look Elsewhere Effect in High Energy Physics
- **File**: `27_2010_Gross_Vitells_Trial_Factors_Look_Elsewhere_Effect.md`
- **arXiv**: 1005.1891
- **Year**: 2010
- **Relevance**: MEDIUM
- **Tags**: look-elsewhere effect, trial factors, statistical methods, Davies bound

**Summary**: Provides efficient method for estimating the look-elsewhere effect (LEE) when searching for signals over a mass range. Trial factor ~ 1 + sqrt(pi/2) * N * Z_fix for 1 DOF. Methodologically mandatory for evaluating any mass-formula claim. Session 48 computed the trial factor for phi_paasch: P ~ 15% after tau-scan correction.

**Key Results**:
- Trial factor = ratio of global to local p-value
- Trial# ~ 1 + sqrt(pi/2) * N * Z_fix for s=1
- N estimated from upcrossings at low reference level
- Applied to phi_paasch in S48: N_ratios = 32,385, P(0.5 ppm match) = 3%, adjusted ~15%

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| trial# = P_global / P_local | Trial factor definition | Section 2.1 |
| P(q>c) <= P(chi^2>c) + <N(c)> | Davies' bound | Eq. (1) |

**Dependencies**: Must be applied to 02, 03, 04 (Paasch mass relations).

---

### Paper 28: Non-Linear Field Theory for Lepton and Quark Masses
- **File**: `28_1996_Gsponer_Hurni_Nonlinear_Field_Theory_Lepton_Quark_Masses.md`
- **arXiv**: hep-ph/0201193
- **Year**: 1996
- **Relevance**: MEDIUM
- **Tags**: Barut formula, N^4 power law, elliptic functions, quark masses, barybag

**Summary**: Extends Barut's N^4 lepton mass formula to quarks using a non-linear scalar field model with F^4 term (barybag). Jacobi elliptic function solutions produce N^4 mass scaling. Harmonic modulus (k = sin(pi/4)) for leptons, equianharmonic (k = sin(pi/12)) for quarks, with mass ratio ~7.24. Cut-off at alpha^{-2}*m_e ~ 9.6 GeV limits leptons to 3 and quarks to 5.

**Key Results**:
- Barut N^4 extended: M(N) = M_e(1 + (3/2)*alpha^{-1} * sum n^4)
- Quark reference mass M_u = M_e/7.25
- Cut-off at alpha^{-2}*m_e ~ 9.6 GeV (uncertainty principle)
- Harmonic/equianharmonic moduli distinguish leptons from quarks

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| M(N) = M_e(1+(3/2)*alpha^{-1}*sum n^4) | Barut formula | Eq. (1) |
| Cut-off: E ~ (3/4)*alpha^{-2}*M_e*c^2 | Generation limit | Eq. (7) |

**Dependencies**: Extends Barut (1979). Connected to 26 (Kosinov).

---

### Paper 29: The Dirac Operator (Survey Article)
- **File**: `29_2025_Hitchin_Dirac_Operator_Survey.md`
- **arXiv**: N/A (Bull. AMS 62(1), 2025)
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: Dirac operator, Atiyah-Singer, index theorem, spinor bundles, instantons

**Summary**: Hitchin's personal survey of the Dirac operator from quantum mechanics to modern geometry. Traces development through Atiyah-Singer index theorem, applications to conformal geometry, Yang-Mills, moduli spaces, and instanton physics. Emphasizes how spectral properties of D encode geometric information.

**Key Results**:
- Dirac operator index = topological invariant (Atiyah-Singer)
- Spin structure requires w_2(M) = 0
- Spectral data of D encodes geometry (Connes' program)
- Applications to instanton moduli spaces

**Dependencies**: Mathematical foundation for 20 (van Suijlekom NCG), 22 (spectral action).

---

### Paper 30: Dynamical Dark Energy in light of DESI DR2 BAO
- **File**: `30_2025_DESI_Dynamical_Dark_Energy_Nature_Astronomy.md`
- **arXiv**: 2504.06118
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: DESI, dynamical dark energy, w(z) crossing, phantom divide, non-parametric reconstruction

**Summary**: Nature Astronomy paper analyzing DESI DR1+DR2. Shape-function and non-parametric reconstructions confirm w(z) crosses -1 near z ~ 0.4-0.5: phantom (w < -1) at low z, quintessence (w > -1) at high z. Signal robust across SN datasets and analysis methods.

**Key Results**:
- w(z) crosses -1 at z ~ 0.4-0.5 (robust)
- Phantom at low z, quintessence at high z
- Not an artifact of CPL parameterization
- Preference persists DR1 to DR2
- Challenges single-field quintessence models

**Dependencies**: Analyzes data from 18, 19 (DESI DR1, DR2).

---

### Paper 31: Particles and Shells
- **File**: `31_2003_Palazzi_Particles_Shells_Stablines.md`
- **arXiv**: physics/0301074
- **Year**: 2003
- **Relevance**: MEDIUM
- **Tags**: stablines, shell structure, cube root, meson, baryon, mass prediction

**Summary**: CERN analysis finding that cube roots of particle masses at stability peaks fall on linear "stablines," analogous to atomic/nuclear shell structure. Meson stabline: m^{1/3} = 0.237*N + 0.289. Baryon stabline: m^{1/3} = 0.198*N + 0.382. Predicts Bc mass at 7.4 +/- 0.2 GeV. Implies particles consist of fixed-mass constituents.

**Key Results**:
- m^{1/3} linear in shell number for stable particles
- Meson and baryon stablines with different slopes
- Bc predicted: 7.41 +/- 0.19 GeV (measured: 6.4 +/- 0.4)
- Baryon predictions at 3.9 and 7.6 GeV

**Dependencies**: Complementary to 42 (Giani mass catalogue), 17 (MacGregor).

---

### Paper 32: Review of Particle Physics (PDG 2024)
- **File**: `32_2024_PDG_Review_Particle_Physics_Navas.md`
- **arXiv**: N/A (Phys. Rev. D 110, 030001)
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: PDG, experimental masses, benchmark, CODATA, weighted averages

**Summary**: The authoritative experimental reference for all particle properties. 2024 edition uses 2,717 new measurements from 869 papers. Provides masses, lifetimes, quantum numbers, and couplings for all known particles. Essential benchmark for testing any mass formula.

**Key Results**:
- All particle masses with current best uncertainties
- alpha^{-1} = 137.035999084(51)
- m_e = 0.51099895000(15) MeV
- m_mu = 105.6583755(23) MeV
- m_tau = 1776.86(12) MeV
- m_p = 938.27208816(29) MeV

**Dependencies**: Input for 33 (running masses), benchmark for 02-04 (Paasch), 07 (Koide).

---

### Paper 33: Updated Running Quark and Lepton Parameters at Various Scales
- **File**: `33_2025_Antusch_Updated_Running_Yukawa_Masses.md`
- **arXiv**: 2510.01312
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: running masses, Yukawa couplings, RGE, GUT scale, MSSM

**Summary**: State-of-the-art running fermion masses from M_Z to 10^{16} GeV using 2024 PDG values (dramatically reduced uncertainties). SM and MSSM results at 9 benchmark scales. Bottom quark uncertainty reduced from 0.7% to 0.09%. Essential for testing mass predictions at any scale.

**Key Results**:
- Running Yukawa at M_Z through 10^{16} GeV (9 scales)
- 2024 PDG: m_b uncertainty 0.7% -> 0.09%
- Mass ratios at M_Z: m_u/m_d = 0.474, m_s/m_d = 20.2, m_c/m_s = 11.8
- MSSM results for tan(beta) = 5, 10, 30, 50

**Dependencies**: Uses 32 (PDG 2024). Feeds into 34 (flavor symmetry tests), 23 (FN Bayesian).

---

### Paper 34: The Symmetry Approach to Quark and Lepton Masses and Mixing
- **File**: `34_2025_Ding_Valle_Symmetry_Approach_Quark_Lepton_Masses.md`
- **arXiv**: 2402.16963
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: flavor symmetry, A4, S4, modular, seesaw, PMNS, neutrino mixing

**Summary**: Comprehensive review of discrete flavor symmetry approaches to the mass and mixing problem. Covers seesaw/scotogenic mechanisms, residual symmetry predictions, A4/S4/T' models, 5D warped models, 6D orbifold models, and modular symmetries. The "golden" quark-lepton mass relation is predicted by a specific orbifold model.

**Key Results**:
- SM has 22 free flavor parameters
- Residual symmetry predictions for mixing angles and CP phases
- Warped T' model: TM1 mixing + excellent global fit
- 6D orbifold: "golden" quark-lepton relation + stringent oscillation predictions
- Modular symmetries: Yukawa = modular forms of complex modulus tau

**Dependencies**: Uses 33 (running masses). Related to 23 (FN Bayesian), 35 (flavor problem review).

---

### Paper 35: The Problem of Flavour
- **File**: `35_2025_EPJ_Problem_of_Flavour.md`
- **arXiv**: N/A (EPJ Plus 140, 73)
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: flavor problem, Froggatt-Nielsen, dark technicolor, flavonic dark matter

**Summary**: Reviews 60+ years of the flavor problem: why three families, why 9 orders of magnitude in mass, why different quark/lepton mixing patterns. Introduces dark-technicolor paradigm unifying FN mechanism with Z_N x Z_M discrete symmetries. Novel "flavonic dark matter" concept where DM stability is protected by flavor symmetries.

**Key Results**:
- FN mechanism with discrete Z_N x Z_M symmetries
- Dark-technicolor paradigm unifies flavor and dark sectors
- Flavonic dark matter: DM protected by flavor symmetry
- Connection between mass hierarchy and dark matter

**Dependencies**: Related to 23 (FN Bayesian), 36 (FN-ALP), 34 (symmetry approach).

---

### Paper 36: Froggatt-Nielsen ALP
- **File**: `36_2024_Greljo_Froggatt_Nielsen_ALP.md`
- **arXiv**: 2407.02998
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: Froggatt-Nielsen, ALP, Z_N, UV completion, flavor hierarchy

**Summary**: Shows FN mechanism generically predicts an axion-like particle. Z_4 is simplest consistent non-SUSY model. Z_8 realizes U(2) flavor structure. "Wheel" diagram topology generates both flavor hierarchies and ALP mass. FN scale can be as low as a few TeV.

**Key Results**:
- FN mechanism generically produces an ALP
- Z_4: simplest non-SUSY FN model; no light ALP
- Z_8: light ALP with mass >= GeV
- FN scale can be as low as a few TeV
- Comprehensive phenomenological analysis (meson mixing, rare decays, LHC)

**Dependencies**: Related to 23 (FN Bayesian), 37 (gauged U(1)_F).

---

### Paper 37: Fermion Mass Hierarchy from Gauged U(1) Flavor Symmetry
- **File**: `37_2025_Babu_Chandra_Tavartkiladze_Gauged_U1_Flavor.md`
- **arXiv**: 2602.24253
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: gauged U(1)_F, axion, PQ symmetry, leptogenesis, dark matter

**Summary**: Unifies four BSM problems via gauged U(1)_F: fermion mass hierarchy (FN), strong CP (accidental PQ), dark matter (axion), baryon asymmetry (leptogenesis). Three explicit DFSZ-type models with UV completions. Right-handed neutrino scale = FN scale.

**Key Results**:
- Accidental PQ symmetry from gauged U(1)_F
- High-quality axion protected by gauge symmetry
- Axion = dark matter with correct relic abundance
- Leptogenesis at right order of magnitude
- Flavor-violating axion couplings testable in meson decays

**Dependencies**: Related to 23 (FN Bayesian), 36 (FN-ALP).

---

### Paper 38: Dirac's Large Number Hypothesis: An Updated Review
- **File**: `38_2025_Jiang_Dirac_Large_Number_Hypothesis_Review.md`
- **arXiv**: N/A (Qeios, 2025)
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: LNH, holographic, varying G, anthropic principle, modern cosmology

**Summary**: Modern review of LNH connecting to holographic principles, quantum gravity, and fine-tuning. Examines G(t) constraints, continuous creation, and connections to dark energy. Concludes LNH remains unproven but offers insights into dimensional analysis and anthropic reasoning.

**Key Results**:
- LNH dimensionless ratios still cluster around 10^{40}
- Connection to holographic principle and AdS/CFT
- Variable Lambda models parallel LNH
- Modern LLR/binary pulsar constraints exclude original 1/t form

**Dependencies**: Updates 06, 08 (Dirac). Uses 10 (LLR). Parallel to 44 (Ray review).

---

### Paper 39: Cosmological and LLR Constraints on Evolving Dark Energy
- **File**: `39_2025_Cosmological_LLR_Evolving_Dark_Energy.md`
- **arXiv**: 2512.10530
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: nonminimal coupling gravity, evolving dark energy, LLR, equivalence principle, fifth force

**Summary**: Nonminimal curvature-matter coupling (f2(R) = mu*R^m) produces effective evolving dark energy consistent with DESI, combined with LLR equivalence principle constraints. A chameleon screening mechanism operates in the Solar System.

**Key Results**:
- NMC gravity can mimic dynamical DE consistent with DESI
- Tracking solution produces w(z) evolution
- LLR EP tests provide independent constraints
- Viable parameter space satisfies both cosmological and LLR constraints

**Dependencies**: Combines 10 (LLR) with 18, 19 (DESI).

---

### Paper 40: A Modified Version of the Koide Formula from Flavor Nonets
- **File**: `40_2021_Luhn_Koide_Flavor_Nonets.md`
- **arXiv**: 2007.05878
- **Year**: 2021
- **Relevance**: HIGH
- **Tags**: Koide, SU(3) flavor, nonet, Yukawaon, scalar potential, quark masses

**Summary**: Derives modified Koide formula from SU(3) flavor symmetry via scalar potential or Yukawaon model. Nonet scalar field Phi has VEV satisfying K = 2/3 when a specific potential parameter relation holds. Extended to quarks: K_up = 0.888 = (2/3)*1.332, K_down = 0.749 = (2/3)*1.124. Two effective parameters fit all three sectors.

**Key Results**:
- K = 2/3 derived from dV/dPhi = 0 for SU(3)-invariant potential
- Charged leptons: K = (2/3)*0.999991 (exact)
- Up quarks: K = (2/3)*1.332
- Down quarks: K = (2/3)*1.124
- Two-parameter modified formula fits all sectors

**Dependencies**: Extends 07 (Koide). Related to 47 (Koide's own derivation).

---

### Paper 41: Why Do Elementary Particles Have Such Strange Mass Ratios?
- **File**: `41_2022_Singh_Octonionic_NCG_Mass_Ratios.md`
- **arXiv**: 2209.03205
- **Year**: 2022
- **Relevance**: HIGH
- **Tags**: octonions, NCG, trace dynamics, quantum gravity, mass ratios, alpha

**Summary**: Uses octonionic NCG to derive mass ratios and alpha. Argues quantum gravity is relevant at low energies when all subsystems are quantum. Adler's trace dynamics with octonionic coordinates produces SU(3) x SU(2) x U(1), three generations, and electric charge quantization. Mass ratios ~ alpha^n emerge from the algebraic structure.

**Key Results**:
- SM from octonionic 8D space coordinates
- Three generations from algebraic structure
- Electric charge quantization from geometry
- Mass ratios determined by octonionic algebra
- alpha ~ 1/137 is quantum-gravitational in origin (order unity in Planck units)

**Dependencies**: Connected to 09 (Zenczykowski Cl(6)), 24 (Furey). Parallel to 20 (NCG).

---

### Paper 42: Particle Mass-Formulae (Giani 2004)
- **File**: `42_2004_Giani_Particle_Mass_Formulae.md`
- **arXiv**: N/A (CERN-OPEN-2004-004)
- **Year**: 2004
- **Relevance**: MEDIUM
- **Tags**: mass formulae, Gell-Mann-Okubo, empirical patterns, CERN, catalogue

**Summary**: CERN technical review cataloguing ~50 empirical mass patterns across baryons, mesons, and leptons. Documents Gell-Mann-Okubo relations (0.1% precision), eta'/eta mass ratios, and cross-sector dimensionless combinations. Comprehensive benchmark for theoretical mass-generation mechanisms.

**Key Results**:
- ~50 distinct empirical mass patterns catalogued
- Linear baryon mass relations: 0.25 MeV precision
- Gell-Mann-Okubo: better than 0.1% accuracy
- Many patterns unexplained by SM

**Dependencies**: Related to 31 (Palazzi), 17 (MacGregor).

---

### Paper 43: Fundamental Constants: From Measurement to the Universe
- **File**: `43_2024_Uzan_Fundamental_Constants_Review.md`
- **arXiv**: 2410.07281
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: fundamental constants, varying constants, equivalence principle, KK, string theory, comprehensive review

**Summary**: Comprehensive review (updated Living Reviews in Relativity article) covering roles of constants, SI system, LPI/UFF connections, scalar-tensor and KK theoretical frameworks, and all experimental constraints. Any constant variation implies EP violation and new coupled fields. Kaluza-Klein: 3D constants vary with internal space size.

**Key Results**:
- Distinguishes fundamental units (c, hbar) from fundamental parameters (alpha, m_e/m_p)
- Varying constants implies EP violation + new fields
- KK: constants vary with extra dimension size
- Comprehensive constraint tables for all methods
- (R, S) parameterization for observables vs primary varying parameters

**Dependencies**: Subsumes 10 (LLR), 15 (Barrow). Foundation for framework's clock constraint.

---

### Paper 44: Large Number Hypothesis: A Review
- **File**: `44_2007_LNH_Review.md`
- **arXiv**: 0705.1836
- **Year**: 2007
- **Relevance**: MEDIUM
- **Tags**: LNH review, Brans-Dicke, varying G, dark energy connection

**Summary**: Reviews LNH from Weyl (1919) through Dirac (1937, 1974) to modern constraints. Covers Brans-Dicke, Hoyle-Narlikar, scale-covariant theories. Notes parallel between LNH (varying G) and variable Lambda models (both involve particle creation). Connects LNH to dark energy.

**Key Results**:
- Historical development from Weyl to modern era
- Modifications of GR to accommodate G(t): BD, Hoyle-Narlikar, Canuto
- BBN, LLR, binary pulsar constraints
- Connection between LNH and dark energy models

**Dependencies**: Extends 06, 08 (Dirac). Parallel to 38 (Jiang modern review).

---

### Paper 45: Particle Masses from First Principles: Complete Fermion Spectrum from Recognition Composition Law
- **File**: `45_2025_Harmonic_Cascade_Mass_Spectrum.md`
- **arXiv**: 2506.12859
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: golden ratio, 3-cube, fermion masses, alpha derivation, Lean 4, zero free parameters

**Summary**: Derives all 12 fermion masses and alpha^{-1} from a single discrete functional equation (RCL) with zero free parameters (beyond m_e calibration). Golden ratio phi = (1+sqrt(5))/2 emerges as unique hierarchy base. 8-step period from 3-cube Hamiltonian cycle. All integers from 3-cube combinatorial invariants. Muon to sub-ppm, quarks to 1-16%. Machine-verified in Lean 4 (179 files, 0 sorry).

**Key Results**:
- All 12 fermion masses from one equation + 4 regularity conditions + 8 theorems
- Golden ratio phi as hierarchy base (Theorem T6)
- 8-step period from 3-cube Q3 (Theorem T7)
- D = 3 from unique combinatorial identity (Theorem T8)
- Muon: sub-ppm; tau: ~10^{-4}; quarks: 1-16%
- alpha^{-1} from curvature tuple
- Lean 4 verified (179 files, zero sorry)
- Neutrino mass-squared splittings within 1-2 sigma of NuFIT 5.3

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| m_n = M_sector * phi^{Z(n)} * Delta(n; Z) | Master mass law | Section 5 |
| phi = (1+sqrt(5))/2 | Unique hierarchy base | Theorem T6 |

**Dependencies**: Related to all mass-quantization papers. Lean 4 verification is novel.

---

### Paper 46: The Fine-Structure Constant as a Scaled Quantity
- **File**: `46_2024_Fine_Structure_Constant_Scaled.md`
- **arXiv**: 2512.07027
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: alpha philosophy, scaled quantity, domain-specific, against derivability

**Summary**: Philosophical argument that alpha is a domain-specific scaled quantity (like Reynolds number), not a fundamental derivable constant. Requires joint presence of EM, QM, and SR structures. Running of alpha in QED confirms scale-dependence. Challenges Duff's dimensionless-only thesis. Direct counterargument to derivation programs (Eddington, Wyler, Paasch).

**Key Results**:
- Alpha is a scaled quantity, not fundamental
- Requires intersection of three frameworks (EM, QM, SR)
- Running confirms scale-dependence
- Mathematical derivation is "category mistake"
- Dimensionlessness does not imply fundamentality

**Dependencies**: Counterpoint to 04 (Paasch), 14 (Eddington), 16 (Wyler). Related to 43 (Uzan).

---

### Paper 47: What Physics Does The Charged Lepton Mass Relation Tell Us?
- **File**: `47_2018_Koide_Charged_Lepton_Physics.md`
- **arXiv**: 1809.00425
- **Year**: 2018
- **Relevance**: HIGH
- **Tags**: Koide formula, U(3) family symmetry, Sumino mechanism, pole mass, running mass

**Summary**: Koide's own review of his formula at FLASY 2018. Derives K = 2/3 from U(3) family symmetry: V = mu^2[PhiPhi] + lambda[PhiPhiPhiPhi] + lambda'[...] gives dV/dPhi = 0 which is K = 2/3, independent of potential parameters. Running-mass problem: K(m_run) = (2/3)*1.00189 at M_Z (0.2% deviation). Sumino mechanism: family gauge bosons cancel QED log corrections, restoring K = 2/3 for pole masses.

**Key Results**:
- K = 2/3 from vacuum condition of U(3)-invariant potential
- K(pole) = (2/3)*0.999989; K(running) = (2/3)*1.00189
- Sumino mechanism: FGB masses ~ (m_i + m_j) cancel QED logs
- Modified Sumino: FGB masses ~ m_i^{-1} with inverted hierarchy
- Second formula: det(Phi)/[Phi]^3 = 1/486

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| dV/dPhi = 0 => K = 2/3 | Vacuum condition gives Koide | Section 2 |
| kappa = det(Phi)/[Phi]^3 = 1/486 | Second Koide relation | Section 2 |

**Dependencies**: Updates 07. Related to 40 (nonet extension), 26 (alpha connection).

---

## Cross-Paper Equation Concordance

### Mass Quantization Formulas

| Formula | Paper | Precision | Scale |
|:---|:---|:---|:---|
| m_n = m_0 * e^{k*phi_n}, phi = 1.53158 | 02 (Paasch) | delta_m/m < 4e-3 | All particles |
| m*(e,j) = (m_e*m_j)^{1/2}, N(j) = 7n | 03 (Paasch) | N(p)=150, exact integers | e to n |
| m_p = f(m_e, alpha, N(b)=112, n3=10) | 03 (Paasch) | 6 digits (6e-7) | Proton |
| ln(m/m_0) = a*n + b | 05 (Muraki) | Few percent | Hadrons/leptons |
| m_n ~ n * m_e/alpha ~ n * 70 MeV | 13 (Nambu) | ~0.6-5% | All particles |
| M(N) = M_e(1+(3/2)*alpha^{-1}*sum n^4) | 28 (Gsponer-Hurni) | ~0.1% leptons, ~1% quarks | Leptons + quarks |
| m^{1/3} = a*N_shell + b | 31 (Palazzi) | Linear fit | Stable particles |
| m_n = M * phi^{Z(n)} * Delta | 45 (Washburn) | Sub-ppm (muon) to 16% | All 12 fermions |

### Alpha Derivation Formulas

| Formula | Paper | Value | Deviation from CODATA |
|:---|:---|:---|:---|
| alpha = (1/n3^2)*(f/2)^{1/4}, f=0.5671 | 04 (Paasch) | 0.007297359 | 0.9 ppm |
| alpha_W = (9/8pi^4)(pi^5/1920)^{1/4} | 16 (Wyler) | 0.00729735253 | 0.6 ppm |
| alpha^{-1} = 136+1 = 137 | 14 (Eddington) | 137 | 0.03% (crude) |
| alpha^{-1} from curvature tuple | 45 (Washburn) | Not explicitly stated | Claimed agreement |

### Koide-Type Relations

| Formula | Paper | Precision |
|:---|:---|:---|
| Q = (sum m_i)/(sum sqrt(m_i))^2 = 2/3 | 07, 47 (Koide) | 6e-6 |
| K = (2/3) * modified, 2 params | 40 (Liang-Sun) | Fits all 3 sectors |
| m_tau = f(m_e, m_mu, m_p; alpha) | 26 (Kosinov) | 1776.76 vs 1776.86 |

### Spectral Action Coefficients

| Coefficient | Paper | Expression |
|:---|:---|:---|
| gamma(a) | 22 (CCS) | (1-2^{-2a})/a * pi^{-a} * xi(2a) |
| gamma_f(a,y) | 21 (DKvS) | (2/Gamma(a)) * sum (-1)^{n+1}(ny)^a K_a(ny)/n |
| c(4) | 22 | (225/4)*zeta(5) |
| c(2) | 22 | (9/2)*zeta(3) |

## Notation Conventions

| Symbol | Meaning | Papers |
|:---|:---|:---|
| phi (= 1.53158) | Paasch mass quantization factor, from x = e^{-x^2} | 02, 03, 04 |
| phi (= 0.618034) | Golden ratio reciprocal 1/phi_golden (Paasch's notation in Paper 03) | 03 |
| phi_golden (= 1.618034) | Golden ratio (1+sqrt(5))/2 | 11, 45 |
| alpha | Fine structure constant ~1/137.036 | All |
| N(j) | Mass number = (m*(e,j)/m_e)^{2/3} | 03 |
| M(j) | = (m_j/m_e)^{1/3} = sqrt(N(j)) | 03 |
| f_N | Exponential scaling = 2*phi_golden = 1.23607 | 03 |
| n3 | Integer from proton mass derivation = 10 | 03, 04 |
| f | Solution of ln(f) = -f = 0.5671433 | 04 |
| Q or K | Koide ratio = 2/3 | 07, 40, 47 |
| D | Dirac operator | 20, 22, 29 |
| (A, H, D) | Spectral triple | 20 |
| Tr(f(D/Lambda)) | Spectral action | 20, 22 |
| w(z), w_0, w_a | Dark energy equation of state (CPL) | 18, 19, 30 |
| G-dot/G | Time variation of gravitational constant | 06, 08, 10 |

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 02 | phi = 1.53158 from x = e^{-x^2} | YES (exact) | S12, all sessions |
| 02 | phi_paasch in Dirac spectrum | YES: m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 | S12 (MC p<0.01) |
| 02 | Six-sequence spiral structure | FAIL: uniform distribution in full spectrum | S48 (PAASCH-SPIRAL-47, SIX-SEQ-48) |
| 03 | N(p) = 150, N(mu) = 35, etc. | Checked against PDG | S44, agent memory |
| 03 | Golden ratio in M-ratios | YES: M(i)/[2M(i-1)] -> 0.618 | Paper 03 Fig. 2, verified |
| 03 | m_proton to 6 digits | YES: 1.67262110 vs 1.67262210 e-27 kg | Paper 03 Eq. (6.8) |
| 03 | m_neutron to 8 digits | YES: 1.67492745 vs 1.67492747 e-27 kg | Paper 03 Eq. (7.2) |
| 04 | alpha = 0.007297359 | YES: 0.9 ppm from CODATA | Paper 04 Eq. (2.9) |
| 04 | n3 = 10 = dim(3,0) = #sectors(pq<=3) | STRUCTURAL IDENTITY | S48 (N3-DIM-48) |
| 04 | f = 0.5671433 from ln(f) = -f | YES (exact) | Verified numerically |
| 07 | Q = 2/3 for charged leptons | YES: Q = 0.666661 (PDG 2024) | Standard verification |
| 10 | G-dot/G = (4+/-9)e-13 yr^{-1} | Observational result | Williams et al. 2004 |
| 16 | Wyler alpha = 0.00729735253 | YES: 0.6 ppm from CODATA | Numerical |
| 18 | DESI w_0 = -0.45 (Pantheon+) | Observational result | DESI DR1 |
| -- | phi ratio under BCS dressing | FAIL: R_dressed < phi at all tau | S47 (PHI-BDG-47) |
| -- | Paasch spiral in eigenvalue phases | FAIL: uniform, no clustering | S47 (PAASCH-SPIRAL-47) |
| -- | f_N in pair-transfer centroids | FAIL: closest = 1.194, 3.4% off | S48 (FN-CENTROID-47) |
| -- | Golden ratio in eigenvalue ratios | FAIL: (2,2)/(0,0) = 1.680, 3.8% off | S48 (PHI-GOLDEN-22) |
| -- | Look-elsewhere correction | INFO: P ~ 15% after tau-scan | S48 (TRIAL-FACTOR) |
| -- | Paasch-CC logarithmic connection | CLOSED at mass quantization level | S56 |
| -- | n3 = 10 shared identity | STRUCTURAL: sole surviving bridge Paasch<->framework | S48, S56 |
