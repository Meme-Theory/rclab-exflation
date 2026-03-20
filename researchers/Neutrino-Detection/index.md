# Neutrino Detection Paper Index

**Domain**: Neutrino Detection
**Papers**: 12 (1930--2024)
**Primary domain**: Neutrino detection techniques, oscillation phenomenology, mass measurements, flavor physics
**Project relevance**: Neutrino masses are the LIGHTEST eigenvalues of the Dirac operator D_K(s) on deformed SU(3). Oscillation parameters (Delta m^2, mixing angles) directly constrain the low-energy end of the Dirac spectrum. The mass hierarchy (normal vs inverted) is a zero-parameter prediction of the Jensen deformation. PMNS mixing angles arise from spinor harmonic overlaps on the internal space.

---

## Dependency Graph

```
THEORETICAL FOUNDATION              DETECTION ERA              OSCILLATION ERA
========================           =============              ===============

[01] Pauli 1930 ---------+
  Neutrino hypothesis     |
  (spin-1/2, neutral,     |
   small mass)             |
                           v
                        [02] Cowan-Reines 1956 -----+
                          First detection             |
                          (inverse beta decay,        |
                           reactor nu_e_bar)          |
                           |                          |
              +------------+----------+               |
              |                       |               |
              v                       v               |
           [03] Danby 1962     [04] Davis 1968 ------+--------+
             Two neutrinos       Solar neutrino               |
             (nu_e != nu_mu)     deficit (Homestake)          |
              |                       |                       |
              |            +----------+                       |
              |            |                                  |
              |            v                                  v
              |         [05] Pontecorvo 1968          [06] SN1987A 1987
              |           Oscillation theory            Supernova neutrinos
              |           (PMNS, flavor mixing,         (K-II + IMB + Baksan,
              |            Delta m^2, MSW)               m_nu < 16 eV)
              |            |                              |
              +---+--------+-----+---+--------------------+
                  |              |   |
                  v              |   v
               [07] Super-K 1998 | [08] SNO 2002 -----+
                 Atmospheric osc | Solar flavor        |
                 (Delta m^2_atm, | transformation      |
                  theta_23~45)   | (NC = SSM, CC~1/3)  |
                  |              |   |                  |
                  +---------+---+   |                  |
                            |       |                  |
                            v       v                  |
                         [09] KamLAND 2003 -----------+
                           Reactor oscillation         |
                           (LMA confirmed,             |
                            Delta m^2_21)              |
                            |                          |
                  +---------+---------+                |
                  |                   |                |
                  v                   v                v
              [10] Daya Bay 2012  [11] IceCube 2013  [12] KATRIN 2024
                theta_13 != 0       Astrophysical       m_nu < 0.45 eV
                (sin^2 2theta_13    neutrinos            (direct mass,
                 = 0.085, 5.2sig)   (PeV events,         MAC-E filter,
                                     E^-2 spectrum)       259 days data)
```

**Critical chain for this project**: 05 -> 07 -> 08 -> 09 -> 10 -> 12
(Oscillation theory -> atmospheric discovery -> solar proof -> reactor confirmation -> theta_13 -> mass bound)

---

## Topic Map

### A. Neutrino Existence and Properties (Papers 01, 02, 03)
Theoretical prediction and first experimental detections of neutrinos. Establishment of neutrino flavors. Historical foundation for the entire field. **LOW** to **MEDIUM** direct relevance -- historical context, but the key constraints come from later precision experiments.

### B. Solar Neutrino Problem (Papers 04, 08) -- **CRITICAL**
The 30-year solar neutrino deficit and its resolution by SNO. Papers 04 and 08 together establish Delta m^2_21 and theta_12, which constrain the two smallest mass eigenvalues of D_K(s_0). The SNO NC measurement proves total flux = SSM, confirming unitarity of PMNS (= Hermiticity of D_K, verified Session 17b).

### C. Oscillation Theory (Paper 05) -- **CRITICAL**
Pontecorvo's neutrino oscillation framework is the theoretical backbone. The two-flavor and three-flavor oscillation formulae, PMNS matrix parameterization, MSW matter effect, Jarlskog invariant, and CP violation formalism are all directly used to interpret the Dirac spectrum predictions. Every oscillation parameter constrains D_K(s_0).

### D. Atmospheric Oscillations (Paper 07) -- **CRITICAL**
Super-K's discovery of atmospheric nu_mu disappearance established Delta m^2_atm = 2.5 x 10^-3 eV^2 and near-maximal theta_23. This is the LARGEST neutrino mass splitting and the most constraining measurement on the low end of the Dirac spectrum. The near-maximal mixing angle probes the approximate mu-tau symmetry of the deformed SU(3) geometry.

### E. Reactor Oscillation Measurements (Papers 09, 10) -- **CRITICAL**
KamLAND confirmed the LMA solution terrestrially (CPT test: [J, D_K(s)] = 0 from Session 17a). Daya Bay measured theta_13 with highest precision (sin^2 2theta_13 = 0.0851), completing the PMNS matrix and opening CP violation searches. Both directly constrain D_K eigenvalues and eigenvector overlaps.

### F. Direct Mass Measurement (Paper 12) -- **CRITICAL**
KATRIN's model-independent bound m_nu < 0.45 eV constrains the absolute scale of the lightest Dirac eigenvalues. No cosmological model assumptions. The framework must produce eigenvalues small enough at s_0 to satisfy this bound while simultaneously producing MeV-GeV masses for charged fermions.

### G. Astrophysical Neutrinos (Papers 06, 11) -- **MEDIUM**
SN1987A confirmed core-collapse theory and constrained m_nu < 5.7 eV, neutrino lifetime, and speed. IceCube opened high-energy neutrino astronomy, tests the (1:1:1) flavor ratio prediction, and probes neutrino cross sections at TeV center-of-mass energies (relevant for KK resonance bounds). Neither directly constrains oscillation parameters but both test the framework at extreme energy scales.

### H. Historical Foundation (Papers 01, 02, 03) -- **LOW**
Pauli's hypothesis, Cowan-Reines detection, and the two-neutrino discovery established neutrinos as real particles with distinct flavors. Essential historical context but the quantitative constraints come from later experiments.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Neutrino mass eigenvalues of D_K(s) | 12, 07, 08, 09 | CRITICAL |
| PMNS mixing angles from geometry | 05, 10, 07, 08 | CRITICAL |
| Delta m^2_21 (solar splitting) | 04, 08, 09, 05 | CRITICAL |
| Delta m^2_32 (atmospheric splitting) | 07, 10, 05 | CRITICAL |
| theta_12 (solar angle) | 08, 09, 04 | CRITICAL |
| theta_23 (atmospheric angle) | 07, 05 | CRITICAL |
| theta_13 (reactor angle) | 10, 05 | CRITICAL |
| CP violation, delta_CP | 05, 10 | CRITICAL |
| Absolute neutrino mass scale | 12, 06 | CRITICAL |
| Mass hierarchy (normal vs inverted) | 12, 07, 09, 05 | CRITICAL |
| MSW matter effect | 05, 04, 08 | HIGH |
| Neutrino cross sections | 02, 11 | HIGH |
| CPT invariance test | 09, 05 | HIGH |
| Lepton flavor conservation | 03, 05 | MEDIUM |
| Fermi theory / weak interaction | 01, 02 | MEDIUM |
| Neutrino mass from time-of-flight | 06, 11 | MEDIUM |
| Inverse beta decay technique | 02, 09, 10 | MEDIUM |
| Water Cherenkov technique | 07, 08, 06 | MEDIUM |
| Sterile neutrino constraints | 12, 11 | MEDIUM |
| Three-generation structure, N_nu = 3 | 03, 05, 11 | MEDIUM |
| Neutrino astronomy | 06, 11 | LOW |
| Beta spectrum endpoint method | 01, 12 | MEDIUM |
| Radiochemical detection | 04 | LOW |
| Historical development | 01, 02, 03 | LOW |

---

## Paper Entries

---

### Paper 01: Pauli's Neutrino Hypothesis

- **File**: `researchers/Neutrino-Detection/01_1930_Pauli_Neutrino_hypothesis_letter.md`
- **Journal**: Open letter to Tubingen conference, December 4, 1930; Solvay Conference 1933
- **Year**: 1930
- **Authors**: Wolfgang Pauli
- **Relevance**: LOW
- **Tags**: `neutrino-hypothesis` `beta-decay` `energy-conservation` `Fermi-theory` `mass-bound`

**Summary**: Pauli proposed a neutral spin-1/2 particle (originally called "neutron," later "neutrino") emitted alongside the electron in beta decay, saving energy conservation from Bohr's radical suggestion of statistical violation. The paper also covers Fermi's 1934 four-fermion interaction theory, the Kurie plot linearization, and the Bethe-Peierls cross-section estimate of ~10^-44 cm^2 that suggested the neutrino was undetectable. Establishes the endpoint method for neutrino mass measurement.

**Key Results**:
1. Neutrino proposed with spin-1/2, mass < 0.01 proton masses, electrically neutral
2. Three-body kinematics naturally explain the continuous beta spectrum
3. Fermi theory: H_int = (G_F/sqrt(2)) [psi_p gamma^mu psi_n][psi_e gamma_mu psi_nu]
4. Bethe-Peierls cross section: sigma ~ G_F^2 E_nu^2 / pi ~ 10^-44 cm^2
5. Kurie plot: K(T_e) = C sqrt((Q - T_e)^2 - m_nu^2) -- endpoint sensitive to m_nu
6. Historical mass bounds from ~511 keV (1934) to 0.45 eV (KATRIN 2024)

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Beta spectrum | dN/dT_e = C F(Z,T_e) p_e E_e (Q-T_e)^2 | Sec 2.3 |
| Fermi interaction | H_int = (G_F/sqrt(2)) [bar psi_p gamma^mu psi_n][bar psi_e gamma_mu psi_nu] | Sec 4.1 |
| Fermi decay rate | dGamma/dT_e propto F(Z,E_e) p_e E_e p_nu E_nu | Sec 4.2 |
| Kurie plot | K(T_e) = sqrt(dGamma/[F p_e E_e]) = C(Q-T_e) for m_nu=0 | Sec 4.3 |
| Cross section | sigma ~ G_F^2 E_nu^2 / pi ~ 10^-44 cm^2 | Sec 4.4 |
| Endpoint sensitivity | dGamma/dT_e propto (Q-T_e) sqrt((Q-T_e)^2 - m_nu^2) | Sec 5.1 |

**Dependencies**:
- *Builds on*: None (foundational)
- *Required by*: 02, 04, 05, 12

---

### Paper 02: Detection of the Free Neutrino (Cowan-Reines)

- **File**: `researchers/Neutrino-Detection/02_1956_Cowan_Reines_Detection_of_the_free_neutrino.md`
- **Journal**: *Science* 124, 103-104 (1956); *Phys. Rev.* 113, 273-279 (1959)
- **Year**: 1956
- **Authors**: Clyde L. Cowan, Jr., Frederick Reines, F.B. Harrison, H.W. Kruse, A.D. McGuire
- **Relevance**: MEDIUM
- **Tags**: `inverse-beta-decay` `reactor-neutrino` `delayed-coincidence` `cross-section` `first-detection`

**Summary**: First direct detection of the (anti)neutrino using inverse beta decay (nu_e_bar + p -> n + e+) at the Savannah River reactor, 26 years after Pauli's prediction. The experiment pioneered the delayed-coincidence technique (prompt positron annihilation + delayed neutron capture on cadmium), achieving a signal of 3.0 +/- 0.2 events/hour above background. The measured cross section of (11 +/- 2.6) x 10^-44 cm^2 was consistent with Fermi theory.

**Key Results**:
1. Neutrino detected via inverse beta decay at Savannah River reactor
2. Delayed coincidence: prompt 511 keV gammas + delayed ~9 MeV Cd capture gammas at ~5 us
3. Signal rate: 3.0 +/- 0.2 events/hour (reactor ON minus OFF)
4. Measured cross section: (11 +/- 2.6) x 10^-44 cm^2 (predicted ~6 x 10^-44)
5. Reactor flux: ~1.3 x 10^13 nu_e_bar/cm^2/s at 11 m from core
6. Established inverse beta decay as standard neutrino detection technique

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Inverse beta decay | nu_e_bar + p -> n + e+ | Sec 2.1 |
| Threshold energy | E_th = 1.806 MeV | Sec 2.1 |
| IBD cross section | sigma(E_nu) = (G_F^2 cos^2 theta_C / pi)(1 + 3g_A^2) p_e E_e | Sec 6.1 |
| Reactor flux | Phi ~ 2 x 10^20 nu_e_bar/s per GW_th | Sec 1.2 |
| Prompt energy | E_prompt = E_nu - 0.782 MeV | Sec 2.2 |

**Dependencies**:
- *Builds on*: 01
- *Required by*: 03, 04, 06, 09, 10

---

### Paper 03: Observation of the Muon Neutrino (Danby et al.)

- **File**: `researchers/Neutrino-Detection/03_1962_Danby_et_al_Observation_of_muon_neutrino.md`
- **Journal**: *Physical Review Letters* 9, 36-44 (1962)
- **Year**: 1962
- **Authors**: G. Danby, J-M. Gaillard, K. Goulianos, L.M. Lederman, N. Mistry, M. Schwartz, J. Steinberger
- **Relevance**: MEDIUM
- **Tags**: `two-neutrinos` `muon-neutrino` `lepton-flavor` `neutrino-beam` `doublet-structure`

**Summary**: Demonstrated that the neutrino associated with muon processes (from pion decay) is distinct from the electron neutrino. Using the first accelerator neutrino beam (15 GeV protons at Brookhaven AGS, through 13.5 m of steel shielding), the experiment observed 29 muon events versus 6 electron events (consistent with ~5 background), excluding the one-neutrino hypothesis at better than 10^-6 probability. Established lepton flavor as a conserved quantum number and the generational doublet structure of leptons.

**Key Results**:
1. 29 muon events, 6 electron events (5 expected from background) -- two neutrinos confirmed
2. One-neutrino hypothesis excluded at > 10^-6 probability
3. Lepton flavor conservation established: L_e and L_mu separately conserved
4. Leptonic doublet structure: (nu_e, e)_L and (nu_mu, mu)_L confirmed
5. LEP later measured N_nu = 2.9840 +/- 0.0082 (exactly 3 light species)
6. DONUT (2000) completed the picture with direct nu_tau detection

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Pion decay | pi+ -> mu+ + nu_mu (BR = 99.99%) | Sec 2.1 |
| One-neutrino test | N_mu/N_e should be ~1 if nu_e = nu_mu | Sec 4.2 |
| Two-neutrino test | N_mu/N_e >> 1 if nu_e != nu_mu | Sec 4.2 |
| LEP invisible width | Gamma_inv = N_nu Gamma_nu_nubar, N_nu = 2.984 | Sec 6.3 |
| Anomaly cancellation | sum_f Q_f = 0 per generation | Sec 5.3 |

**Dependencies**:
- *Builds on*: 01, 02
- *Required by*: 05, 07

---

### Paper 04: Search for Neutrinos from the Sun (Davis, Harmer, Hoffman)

- **File**: `researchers/Neutrino-Detection/04_1968_Davis_Harmer_Hoffman_Search_for_neutrinos_from_the_Sun.md`
- **Journal**: *Physical Review Letters* 20, 1205-1209 (1968)
- **Year**: 1968
- **Authors**: Raymond Davis, Jr., Don S. Harmer, Kenneth C. Hoffman
- **Relevance**: HIGH
- **Tags**: `solar-neutrino` `Homestake` `radiochemical` `chlorine-37` `neutrino-deficit` `solar-model`

**Summary**: The Homestake experiment measured solar neutrinos via nu_e + Cl-37 -> Ar-37 + e- using 615 tonnes of perchloroethylene 4,850 feet underground for 30 years (1968-1994). Observed 2.56 +/- 0.23 SNU against a Standard Solar Model prediction of 7.6 SNU, detecting only ~1/3 of the expected electron neutrino flux. This "solar neutrino problem" persisted for three decades and was ultimately explained by neutrino flavor oscillation (confirmed by SNO in 2002). Established the field of neutrino astronomy and provided the first evidence (in hindsight) for neutrino mass.

**Key Results**:
1. Measured rate: 2.56 +/- 0.16(stat) +/- 0.16(syst) SNU
2. SSM prediction: 7.6 +1.3/-1.1 SNU (Bahcall-Pinsonneault 2000)
3. Ratio: R_meas/R_SSM = 0.34 +/- 0.06 -- only 1/3 of expected nu_e detected
4. 108 extractions over 1970-1994, extracting ~15 Ar-37 atoms per run from 10^30 Cl-37 atoms
5. Energy-dependent deficit across experiments: 56% (Ga), 34% (Cl), 46% (water Cherenkov)
6. Resolution: MSW-enhanced oscillation, confirmed by SNO

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Detection reaction | nu_e + Cl-37 -> Ar-37 + e- (threshold 0.814 MeV) | Sec 1.2 |
| SNU definition | 1 SNU = 10^-36 captures/(target atom * second) | Sec 1.3 |
| Ar-37 production | N_Ar(t) = (R/lambda_Ar)(1 - exp(-lambda_Ar t)) | Sec 3.1 |
| Ar-37 half-life | T_1/2 = 35.04 days (electron capture, 2.82 keV Auger) | Sec 3.3 |
| B-8 flux dependence | Phi(B-8) propto T_c^18 | Sec 5.1 |

**Dependencies**:
- *Builds on*: 01, 02
- *Required by*: 05, 07, 08, 09

---

### Paper 05: Neutrino Experiments and Conservation of Leptonic Charge (Pontecorvo)

- **File**: `researchers/Neutrino-Detection/05_1968_Pontecorvo_Neutrino_experiments_lepton_charge.md`
- **Journal**: *Soviet Physics JETP* 26, 984-988 (1968); *Zh. Eksp. Teor. Fiz.* 53, 1717-1725 (1967)
- **Year**: 1968
- **Authors**: Bruno Pontecorvo
- **Relevance**: CRITICAL
- **Tags**: `oscillation-theory` `PMNS-matrix` `mixing-angles` `Delta-m-squared` `MSW-effect` `CP-violation` `mass-hierarchy` `Jarlskog`

**Summary**: The definitive theoretical formulation of neutrino flavor oscillation, extending Pontecorvo's earlier (1957-1958) neutrino-antineutrino oscillation ideas to include nu_e <-> nu_mu transitions. Establishes that if mass eigenstates differ from flavor eigenstates, the transition probability is P(nu_e -> nu_mu) = sin^2(2theta) sin^2(Delta m^2 L / 4E). Includes the three-flavor PMNS parameterization, MSW matter effect, Jarlskog invariant for CP violation, and the mass hierarchy problem. This paper (together with Maki-Nakagawa-Sakata 1962) is the theoretical foundation for all neutrino oscillation physics.

**Key Results**:
1. Two-flavor oscillation: P = sin^2(2theta) sin^2(Delta m^2 L / 4E)
2. PMNS matrix: U = R_23 * R_13(delta) * R_12 with three angles + CP phase
3. Three-flavor probability with CP-violating term proportional to sin(delta_CP)
4. MSW resonance condition: 2EV = Delta m^2 cos(2theta), maximal mixing in matter
5. Jarlskog invariant: J = (1/8) c_13 sin(2theta_12) sin(2theta_23) sin(2theta_13) sin(delta)
6. Current best-fit values: theta_12=33.4, theta_23=49.1, theta_13=8.54, Delta m^2_21=7.41e-5, |Delta m^2_31|=2.507e-3

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Two-flavor oscillation | P(nu_e->nu_mu) = sin^2(2theta) sin^2(Delta m^2 L / 4E) | Sec: Two-Flavor |
| Practical units | P = sin^2(2theta) sin^2(1.27 Delta m^2[eV^2] L[km] / E[GeV]) | Sec: Practical |
| PMNS matrix | U = R_23 * Rtilde_13(delta) * R_12 | Sec: Three-Flavor |
| Three-flavor P | P = delta_ab - 4 sum Re(U*Ui...) sin^2(...) + 2 sum Im(...) sin(...) | Sec: Three-Flavor |
| MSW potential | V_CC = sqrt(2) G_F n_e | Sec: MSW |
| MSW resonance | n_e^res = Delta m^2 cos(2theta) / (2 sqrt(2) G_F E) | Sec: MSW |
| Jarlskog invariant | J = (1/8) c_13 sin(2theta_12) sin(2theta_23) sin(2theta_13) sin(delta) | Sec: CP Violation |

**Dependencies**:
- *Builds on*: 01, 03, 04
- *Required by*: 07, 08, 09, 10, 11, 12

---

### Paper 06: Observation of Neutrinos from Supernova SN1987A (Hirata et al.)

- **File**: `researchers/Neutrino-Detection/06_1987_Hirata_et_al_Observation_of_neutrinos_from_SN1987A.md`
- **Journal**: *Physical Review Letters* 58, 1490-1493 (1987)
- **Year**: 1987
- **Authors**: K. Hirata, T. Kajita, M. Koshiba et al. (Kamiokande-II Collaboration)
- **Relevance**: MEDIUM
- **Tags**: `supernova` `SN1987A` `neutrino-astronomy` `mass-bound` `time-of-flight` `core-collapse` `multi-messenger`

**Summary**: First detection of neutrinos from an identified astrophysical source beyond the Sun. Kamiokande-II recorded 11 events in 13 seconds from SN1987A in the Large Magellanic Cloud (51.4 kpc), with IMB recording 8 events and Baksan 5 events. Total of 24 neutrino events across three detectors confirmed core-collapse supernova theory (99% of energy in neutrinos, ~3 x 10^53 erg), established neutrino astronomy, and provided mass/lifetime/speed constraints. Inaugurated the multi-messenger astronomy paradigm.

**Key Results**:
1. 11 events at Kamiokande-II (6.3-35.4 MeV), 8 at IMB, 5 at Baksan -- 24 total in ~13 s
2. Total energy ~4 x 10^53 erg, consistent with gravitational binding energy of neutron star
3. Mass bound: m_nu < 16 eV (K-II, 90% CL); later refined to < 5.7 eV (combined)
4. Speed constraint: |v_nu - c|/c < 2 x 10^-9
5. Lifetime constraint: tau/m > 5.7 x 10^5 s/eV
6. Electric charge constraint: |q_nu| < 3 x 10^-17 e

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Binding energy | E_bind = 3 G M_NS^2 / 5 R_NS ~ 3 x 10^53 erg | Sec: Physics |
| Time-of-flight delay | Delta t = (d/c) m^2 c^4 / 2E^2 | Sec: Physics |
| Differential delay | Delta t_12 = d m^2 c^4 / 2c (1/E_1^2 - 1/E_2^2) | Sec: Physics |
| Fluence at Earth | Phi = N_det / (N_p <sigma>) ~ 3.1 x 10^10 cm^-2 | Sec: Physics |
| Detection reaction | nu_e_bar + p -> e+ + n (threshold 1.8 MeV) | Sec: Detection |

**Dependencies**:
- *Builds on*: 02, 04
- *Required by*: 07, 11

---

### Paper 07: Evidence for Oscillation of Atmospheric Neutrinos (Super-Kamiokande)

- **File**: `researchers/Neutrino-Detection/07_1998_Fukuda_et_al_Evidence_for_oscillation_atmospheric_neutrinos.md`
- **Journal**: *Physical Review Letters* 81, 1562-1567 (1998)
- **Year**: 1998
- **Authors**: Y. Fukuda, T. Kajita et al. (Super-Kamiokande Collaboration)
- **Relevance**: CRITICAL
- **Tags**: `atmospheric-neutrino` `oscillation-discovery` `Super-K` `theta_23` `Delta-m-squared-atm` `zenith-angle` `water-Cherenkov`

**Summary**: First definitive evidence for neutrino oscillation. Super-Kamiokande (50 kton water Cherenkov, 11,146 PMTs) observed a zenith-angle-dependent deficit of muon neutrinos: upward-going nu_mu (L ~ 13,000 km) were depleted by ~50% relative to downward-going (L ~ 15 km), while electron neutrinos showed no asymmetry. The up/down asymmetry A_mu = -0.296 +/- 0.048 rejected no-oscillation at > 6 sigma. Best fit: Delta m^2_atm = 2.2 x 10^-3 eV^2, sin^2(2theta_23) = 1.0. The subsequent L/E analysis (2004) showed the characteristic sinusoidal dip, excluding neutrino decay and decoherence.

**Key Results**:
1. Mu-like up/down asymmetry: A_mu = -0.296 +/- 0.048 (no-osc predicts ~0)
2. E-like asymmetry: A_e = -0.036 +/- 0.067 (consistent with zero -- no nu_e oscillation)
3. No-oscillation excluded at > 6 sigma (chi^2 difference > 40 for 2 d.o.f.)
4. Best-fit (1998): Delta m^2_atm = 2.2 x 10^-3 eV^2, sin^2(2theta_23) = 1.0
5. Modern values: |Delta m^2_32| = 2.507 x 10^-3 eV^2, sin^2 theta_23 = 0.546
6. L/E sinusoidal pattern confirmed oscillation, excluded decay and decoherence

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Atmospheric flux ratio | R = N(nu_mu)/N(nu_e) ~ 2 (naive) | Sec: Context |
| Up/down asymmetry | A_mu = (N_up - N_down)/(N_up + N_down) | Sec: Data |
| Survival probability | P(nu_mu->nu_mu) = 1 - sin^2(2theta_23) sin^2(1.27 Dm^2 L/E) | Sec: Fit |
| Oscillation length | L_osc = 4pi E / Delta m^2 ~ 1000 km at 1 GeV | Sec: Key Observable |
| First minimum | L/E ~ 500 km/GeV for Delta m^2 ~ 2.5 x 10^-3 | Sec: L/E Analysis |

**Dependencies**:
- *Builds on*: 03, 04, 05, 06
- *Required by*: 08, 09, 10, 11

---

### Paper 08: Direct Evidence for Neutrino Flavor Transformation from SNO

- **File**: `researchers/Neutrino-Detection/08_2002_Ahmad_et_al_SNO_Direct_evidence_neutrino_flavor_transformation.md`
- **Journal**: *Physical Review Letters* 89, 011301 (2002)
- **Year**: 2002
- **Authors**: Q.R. Ahmad, A.B. McDonald et al. (SNO Collaboration)
- **Relevance**: CRITICAL
- **Tags**: `SNO` `solar-neutrino` `flavor-transformation` `neutral-current` `heavy-water` `theta_12` `Delta-m-squared-21` `MSW`

**Summary**: Definitive resolution of the 30-year solar neutrino problem using the Sudbury Neutrino Observatory (1000 tonnes D2O, 2092 m underground). SNO measured three reactions: CC (nu_e only), NC (all flavors), and ES (nu_e enhanced). The NC flux Phi_NC = 5.09 x 10^6 cm^-2 s^-1 matched the SSM prediction exactly, while Phi_CC = 1.76 x 10^6 -- only ~1/3 of the total. The non-nu_e component was detected at 5.3 sigma: Phi(nu_mu,tau) = 3.41 x 10^6. This proved neutrinos oscillate, the SSM is correct, and combined with KamLAND established Delta m^2_21 = 7.53 x 10^-5 eV^2, theta_12 = 33.4 degrees (LMA solution).

**Key Results**:
1. NC flux: Phi_NC = 5.09 +0.44/-0.43 x 10^6 cm^-2 s^-1 = SSM prediction (total flux conserved)
2. CC flux: Phi_CC = 1.76 +0.06/-0.05 x 10^6 cm^-2 s^-1 (~1/3 of NC)
3. Non-nu_e component: Phi(nu_mu,tau) = 3.41 +/- 0.66 x 10^6, nonzero at 5.3 sigma
4. Phi_CC/Phi_NC = 0.346 +/- 0.029 -- two-thirds of solar neutrinos oscillated
5. MSW survival probability: P(nu_e -> nu_e) ~ sin^2 theta_12 ~ 0.30 for B-8 neutrinos
6. Combined parameters: Delta m^2_21 = 7.53 x 10^-5 eV^2, theta_12 = 33.4 degrees (LMA)

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| CC reaction | nu_e + d -> p + p + e- (nu_e only) | Sec: Three Channels |
| NC reaction | nu_x + d -> p + n + nu_x (all flavors) | Sec: Three Channels |
| ES reaction | nu_x + e- -> nu_x + e- (Phi_e + 0.154 Phi_mu,tau) | Sec: Three Channels |
| NC cross section | sigma_NC ~ 0.3 x 10^-42 (E_nu/10 MeV)^2 cm^2 | Sec: Three Channels |
| MSW survival | P(nu_e->nu_e) ~ sin^2 theta_12 ~ 0.30 (adiabatic, B-8) | Sec: Resolution |
| Mass-squared ratio | Dm^2_21/Dm^2_31 ~ 1:33 | Sec: Framework |

**Dependencies**:
- *Builds on*: 04, 05, 07
- *Required by*: 09, 10, 12

---

### Paper 09: First Results from KamLAND -- Reactor Antineutrino Disappearance

- **File**: `researchers/Neutrino-Detection/09_2003_Eguchi_et_al_KamLAND_First_results.md`
- **Journal**: *Physical Review Letters* 90, 021802 (2003)
- **Year**: 2003
- **Authors**: K. Eguchi et al. (KamLAND Collaboration)
- **Relevance**: CRITICAL
- **Tags**: `KamLAND` `reactor-neutrino` `LMA-confirmation` `Delta-m-squared-21` `theta_12` `CPT-test` `spectral-distortion`

**Summary**: First terrestrial confirmation of the LMA solution to the solar neutrino problem. KamLAND (1 kton liquid scintillator in Kamioka mine) detected reactor antineutrinos at average baseline ~180 km from Japan's nuclear reactors. Observed 54 events where 86.8 +/- 5.6 expected without oscillation (ratio 0.611 +/- 0.085 +/- 0.041), excluding no-disappearance at 99.95% CL. Combined with solar data: Delta m^2_21 = 7.9 x 10^-5 eV^2, tan^2 theta_12 = 0.40. Excluded all non-LMA solutions. Under CPT invariance (tested by comparing nu and nu_bar oscillation), this provides a model-independent confirmation independent of solar model uncertainties.

**Key Results**:
1. Observed/expected ratio: 0.611 +/- 0.085(stat) +/- 0.041(syst) -- 99.95% CL exclusion of no-oscillation
2. Combined Delta m^2_21 = (7.9 +0.6/-0.5) x 10^-5 eV^2
3. Combined tan^2 theta_12 = 0.40 +0.10/-0.07
4. All non-LMA solutions excluded
5. Spectral distortion (2004): L/E dip at ~50 km/MeV confirmed oscillation vs decay/decoherence
6. Precision (2008): Delta m^2_21 = (7.59 +/- 0.21) x 10^-5 eV^2

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Survival probability | P(nu_e_bar->nu_e_bar) = 1 - sin^2(2theta_12) sin^2(Dm^2_21 L / 4E) | Sec: II |
| Practical formula | Phase = 1.267 Dm^2[eV^2] L[m] / E[MeV] | Sec: II |
| Reactor flux | dN/dE = sum_i f_i phi_i(E_nu) | Sec: I |
| IBD cross section | sigma ~ 9.52 x 10^-44 (E_nu/MeV)^2 cm^2 | Sec: IV |
| Neutron capture | n + p -> d + gamma (2.225 MeV, tau ~ 210 us) | Sec: IV |
| First osc minimum | L/E = pi/(2 * 1.267 * Dm^2_21) ~ 15.7 km/MeV | Sec: Spectral |

**Dependencies**:
- *Builds on*: 02, 04, 05, 07, 08
- *Required by*: 10, 12

---

### Paper 10: Observation of Electron-Antineutrino Disappearance at Daya Bay

- **File**: `researchers/Neutrino-Detection/10_2012_An_et_al_Daya_Bay_theta13_measurement.md`
- **Journal**: *Physical Review Letters* 108, 171803 (2012)
- **Year**: 2012
- **Authors**: F.P. An et al. (Daya Bay Collaboration)
- **Relevance**: CRITICAL
- **Tags**: `Daya-Bay` `theta_13` `reactor-neutrino` `PMNS-complete` `CP-violation-gateway` `near-far` `gadolinium`

**Summary**: First definitive measurement of the last unknown PMNS mixing angle theta_13. Using six identical Gd-doped liquid scintillator detectors at near (0.5 km) and far (1.6 km) sites from six reactor cores at Daya Bay (17.4 GW_th total), the near/far relative measurement strategy reduced systematic uncertainty to ~0.2%. In 55 days of data: sin^2(2theta_13) = 0.092 +/- 0.016(stat) +/- 0.005(syst), excluding theta_13 = 0 at 5.2 sigma. Final result (2022): sin^2(2theta_13) = 0.0851 +/- 0.0024 -- the most precisely known neutrino mixing parameter. This ruled out tri-bimaximal mixing and opened the door to CP violation and mass hierarchy measurements.

**Key Results**:
1. sin^2(2theta_13) = 0.092 +/- 0.016(stat) +/- 0.005(syst) -- theta_13 != 0 at 5.2 sigma
2. Final result (2022): sin^2(2theta_13) = 0.0851 +/- 0.0024 (2.8% precision)
3. |Delta m^2_32| = (2.466 +/- 0.060) x 10^-3 eV^2 (normal ordering)
4. Tri-bimaximal mixing (theta_13 = 0 exactly) definitively ruled out
5. Jarlskog invariant J_CP ~ 0.033 sin(delta_CP) -- CP violation now experimentally accessible
6. Near/far ratio: R = 0.940 +/- 0.011(stat) +/- 0.004(syst)

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Short-baseline survival | P ~ 1 - sin^2(2theta_13) sin^2(Dm^2_32 L / 4E) | Sec: I |
| First osc maximum | L ~ 2pi E / Dm^2_32 ~ 1750 m at 3.5 MeV | Sec: I |
| Jarlskog invariant | J_CP = (1/8) sin(2theta_12)sin(2theta_23)sin(2theta_13)cos(theta_13)sin(delta) | Sec: Interpretation |
| Near/far ratio | R_far/R_near * L_far^2/L_near^2 = <P_surv> | Sec: IV |
| PMNS element | U_e3 = sin(theta_13) exp(-i delta_CP) ~ 0.15 exp(-i delta) | Sec: Interpretation |
| Gd neutron capture | n + Gd -> Gd* -> Gd + gammas (~8 MeV total, tau ~ 28 us) | Sec: III |

**Dependencies**:
- *Builds on*: 02, 05, 07, 08, 09
- *Required by*: 12

---

### Paper 11: Evidence for High-Energy Astrophysical Neutrinos at IceCube

- **File**: `researchers/Neutrino-Detection/11_2013_IceCube_Evidence_astrophysical_neutrinos.md`
- **Journal**: *PRL* 111, 021103 (2013); *Science* 342, 1242856 (2013)
- **Year**: 2013
- **Authors**: M.G. Aartsen et al. (IceCube Collaboration)
- **Relevance**: MEDIUM
- **Tags**: `IceCube` `astrophysical-neutrinos` `PeV` `neutrino-astronomy` `flavor-ratio` `Fermi-acceleration` `multi-messenger`

**Summary**: First observation of high-energy neutrinos of astrophysical origin. IceCube (1 km^3 Antarctic ice Cherenkov, 5160 DOMs) detected two PeV cascade events ("Bert" and "Ernie," 1.04 and 1.14 PeV) at 2.8 sigma. A subsequent HESE analysis found 28 events above 30 TeV against 10.6 expected background (4.1 sigma). The energy spectrum followed E^-2.2, consistent with Fermi acceleration at cosmic sources. Flavor ratio consistent with (1:1:1) at Earth (from (1:2:0) at source after oscillation). Later identified TXS 0506+056 blazar (2018) and NGC 1068 (2022) as neutrino point sources.

**Key Results**:
1. Two PeV events: 1.04 +/- 0.16 PeV and 1.14 +/- 0.17 PeV (2.8 sigma vs background)
2. HESE sample: 28 events above 30 TeV, background 10.6 -- 4.1 sigma astrophysical excess
3. Spectral index: gamma = 2.2 +/- 0.4 (consistent with E^-2 Fermi acceleration)
4. Per-flavor flux at 100 TeV: ~1.2 x 10^-8 GeV cm^-2 s^-1 sr^-1 (near Waxman-Bahcall bound)
5. Flavor ratio at Earth consistent with (1:1:1) -- supports three-flavor oscillation
6. Center-of-mass energy sqrt(s) ~ 1.4 TeV at 1 PeV -- probes TeV-scale physics

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Cherenkov angle | cos(theta_C) = 1/(n beta), theta_C ~ 41 deg in ice | Sec: I |
| Conventional atm flux | dPhi/dE ~ E^-(gamma+1) ~ E^-3.7 | Sec: IV |
| Astrophysical flux | dPhi/dE = Phi_0 (E/100 TeV)^-gamma, gamma ~ 2.2 | Sec: VII |
| Flavor at source | (nu_e : nu_mu : nu_tau)_source = (1 : 2 : 0) | Sec: VIII |
| Flavor at Earth | (nu_e : nu_mu : nu_tau)_Earth ~ (1 : 1 : 1) after oscillation | Sec: VIII |
| Center-of-mass energy | sqrt(s) = sqrt(2 m_N E_nu) ~ 1.4 TeV at 1 PeV | Sec: V |

**Dependencies**:
- *Builds on*: 05, 06, 07
- *Required by*: None (frontier)

---

### Paper 12: Direct Neutrino-Mass Measurement from KATRIN

- **File**: `researchers/Neutrino-Detection/12_2024_KATRIN_Direct_neutrino_mass_measurement.md`
- **Journal**: *Science* 386, eadq9592 (2024)
- **Year**: 2024
- **Authors**: M. Aker et al. (KATRIN Collaboration)
- **Relevance**: CRITICAL
- **Tags**: `KATRIN` `neutrino-mass` `tritium` `beta-endpoint` `MAC-E-filter` `model-independent` `mass-hierarchy` `sterile-search`

**Summary**: Most stringent model-independent bound on the neutrino mass: m_nu < 0.45 eV (90% CL) from 259 days of tritium beta decay endpoint spectroscopy with 36 million electrons. The MAC-E filter (70 m spectrometer, sub-eV resolution at 18.6 keV) measures the integral beta spectrum near the endpoint where the shape is sensitive to m_nu^2. Result: m_nu^2 = -0.14 +0.13/-0.15 eV^2 (Feldman-Cousins upper limit). Independent of Dirac/Majorana nature and cosmological model. Also constrains sterile neutrinos: no evidence for m_4 in 1-100 eV^2 range. Complements cosmological bounds (Planck sum m_i < 0.12 eV, model-dependent).

**Key Results**:
1. m_nu < 0.45 eV (90% CL) -- most stringent model-independent bound
2. m_nu^2 = -0.14 +0.13/-0.15 eV^2 (consistent with zero, Feldman-Cousins)
3. 259 measurement days, 36 million beta electrons, 5 campaigns (KNM1-KNM5)
4. MAC-E filter resolution: Delta E ~ 0.93 eV at E = 18.6 keV (resolving power ~20,000)
5. Sterile neutrino search: |U_e4|^2 < 0.01-0.1 for m_4^2 in 1-100 eV^2
6. Normal ordering minimum: sum m_i ~ 0.06 eV; inverted: sum m_i ~ 0.10 eV

**Key Equations**:
| Label | Description | Location |
|:---|:---|:---|
| Tritium decay | H-3 -> He-3+ + e- + nu_e_bar (Q = 18.574 keV) | Sec: II |
| Endpoint spectrum | dGamma/dE propto (E_0-E) sqrt((E_0-E)^2 - m_nu^2) Theta(E_0-E-m_nu) | Sec: II |
| MAC-E resolution | Delta E = (B_min/B_max) E_kin ~ 0.93 eV | Sec: I |
| Effective mass | m_nu^eff = sqrt(sum_i |U_ei|^2 m_i^2) | Sec: Context |
| Seesaw mass | m_nu ~ m_D^2 / M_R ~ (100 GeV)^2 / 10^14 GeV ~ 0.1 eV | Sec: Interpretation |
| Endpoint fraction | f(1 eV) = (2/3)(1/Q)^3 ~ 10^-13 | Sec: IV |

**Dependencies**:
- *Builds on*: 01, 05, 07, 08, 09, 10
- *Required by*: None (frontier)

---

## Cross-Paper Equation Concordance

### Mass-Squared Differences

| Parameter | Paper(s) | Value | Notes |
|:---|:---|:---|:---|
| Delta m^2_21 | 04, 08, 09 | (7.53 +/- 0.18) x 10^-5 eV^2 | Solar + KamLAND combined |
| |Delta m^2_32| | 07, 10 | (2.507 +/- 0.026) x 10^-3 eV^2 | Atmospheric + reactor |
| Dm^2_32/Dm^2_21 | 05, 08 | ~33 | Hierarchy of eigenvalue spacings |

### Mixing Angles

| Parameter | Paper(s) | Value | Notes |
|:---|:---|:---|:---|
| theta_12 | 08, 09 | 33.4 +/- 0.8 deg | Solar angle (LMA) |
| theta_23 | 07 | 49.1 deg (best fit) | Atmospheric angle (near-maximal) |
| theta_13 | 10 | 8.6 +/- 0.1 deg | Reactor angle (Daya Bay final) |
| sin^2(2theta_12) | 08, 09 | ~0.86 | |
| sin^2(2theta_23) | 07 | ~1.0 (1998 best-fit) | |
| sin^2(theta_23) | 07 | 0.546 (modern, upper octant) | |
| sin^2(2theta_13) | 10 | 0.0851 +/- 0.0024 | Most precise oscillation parameter |

### CP Violation

| Parameter | Paper(s) | Value | Notes |
|:---|:---|:---|:---|
| delta_CP | 05 | ~197 deg (hints) | 108-404 deg (3sigma) |
| J_CP | 05, 10 | ~0.033 sin(delta_CP) | ~1000x larger than J_CKM |

### Neutrino Mass Bounds

| Method | Paper | Bound | Model dependence |
|:---|:---|:---|:---|
| Direct (KATRIN) | 12 | m_nu < 0.45 eV (90% CL) | Model-independent |
| Time-of-flight (SN1987A) | 06 | m_nu < 5.7 eV (combined) | Model-independent |
| Cosmological (Planck) | 12 (cited) | sum m_i < 0.12 eV | Lambda CDM dependent |
| Oscillation lower bound | 07, 08 | m_heaviest >= 0.05 eV | From sqrt(|Dm^2_32|) |

### Cross Sections

| Reaction | Paper(s) | Value | Notes |
|:---|:---|:---|:---|
| IBD (nu_e_bar + p) | 01, 02 | ~9.5 x 10^-44 (E_nu/MeV)^2 cm^2 | Standard detection reaction |
| CC on deuterium | 08 | ~1.0 x 10^-42 (E/10 MeV)^2 cm^2 | SNO CC channel |
| NC on deuterium | 08 | ~0.3 x 10^-42 (E/10 MeV)^2 cm^2 | SNO NC channel |
| Cl-37 capture | 04 | SNU-based; threshold 0.814 MeV | Homestake |

### Flavor Ratios

| Observable | Paper(s) | Value | Notes |
|:---|:---|:---|:---|
| Solar nu_e survival | 04, 08 | ~0.34 (Homestake); ~0.30 (SNO B-8) | MSW-enhanced |
| Atmospheric nu_mu survival | 07 | ~0.50 (upward, multi-GeV) | Averaged over many cycles |
| Reactor nu_e_bar survival | 09 | ~0.61 (KamLAND, L~180 km) | Vacuum oscillation |
| Reactor nu_e_bar survival | 10 | ~0.94 (Daya Bay, L~1.6 km) | theta_13 oscillation |
| Astrophysical flavor | 11 | ~(1:1:1) at Earth | From (1:2:0) at source |

---

## Notation Conventions

| Symbol | Meaning | Standard usage |
|:---|:---|:---|
| nu_e, nu_mu, nu_tau | Electron, muon, tau neutrino (flavor eigenstates) | All papers |
| nu_1, nu_2, nu_3 | Mass eigenstates (m_1, m_2, m_3) | Papers 05, 07-12 |
| nu_e_bar | Electron antineutrino | Papers 02, 09, 10, 12 |
| U_PMNS | Pontecorvo-Maki-Nakagawa-Sakata mixing matrix | Papers 05, 07-12 |
| theta_12, theta_23, theta_13 | PMNS mixing angles | Papers 05, 07-10 |
| delta_CP | CP-violating Dirac phase | Papers 05, 10 |
| Delta m^2_ij | m_i^2 - m_j^2 (mass-squared difference) | Papers 05, 07-12 |
| Delta m^2_21 | "Solar" mass splitting (~7.5 x 10^-5 eV^2) | Papers 04, 05, 08, 09 |
| Delta m^2_32 | "Atmospheric" mass splitting (~2.5 x 10^-3 eV^2) | Papers 05, 07, 10 |
| G_F | Fermi coupling constant (1.166 x 10^-5 GeV^-2) | Papers 01, 02, 05 |
| SNU | Solar Neutrino Unit (10^-36 captures/atom/s) | Paper 04 |
| IBD | Inverse beta decay (nu_e_bar + p -> n + e+) | Papers 02, 06, 09, 10 |
| CC | Charged-current interaction | Paper 08 |
| NC | Neutral-current interaction | Paper 08 |
| ES | Elastic scattering (nu + e- -> nu + e-) | Paper 08 |
| MSW | Mikheyev-Smirnov-Wolfenstein (matter) effect | Papers 04, 05, 08 |
| LMA | Large Mixing Angle solution | Papers 08, 09 |
| SSM | Standard Solar Model (Bahcall) | Papers 04, 08 |
| MAC-E | Magnetic Adiabatic Collimation with Electrostatic filter | Paper 12 |
| HESE | High-Energy Starting Event (IceCube selection) | Paper 11 |
| NO / IO | Normal ordering / Inverted ordering | Papers 05, 10, 12 |
| J_CP | Jarlskog invariant for CP violation | Papers 05, 10 |

---

## Computational Verification Status

The following scripts in `tier0-computation/` are indirectly relevant to the neutrino detection corpus:

- **`tier0-computation/tier1_dirac_spectrum.py`** (~1580 lines): Computes eigenvalues of D_K(s) on Jensen-deformed SU(3) via Peter-Weyl decomposition. The lightest eigenvalues of this spectrum correspond to neutrino masses. Session 12 found 147 eigenvalue pairs within 1% of phi_paasch (= 1.53158) at s ~ 1.14. The eigenvalue spacings at specific s values are the quantities that must match the measured Delta m^2_21 and Delta m^2_32 from this corpus.

- **`tier0-computation/z3_triality_labeling.py`**: Verifies Z_3 = (p-q) mod 3 partition of 28 irreps into three generation classes (Session 17a, B-4). The three-generation structure established by Paper 03 (two-neutrino discovery) and confirmed by LEP (N_nu = 3) must match this geometric Z_3 grading.

- **`tier0-computation/d1_d3_j_compatibility.py`**: Verifies [J, D_K(s)] = 0 identically (Session 17a, D-1) and eigenvalue pairing to machine precision (D-3). The CPT invariance tested by KamLAND (Paper 09) -- that nu and nu_bar oscillate with the same parameters -- is guaranteed by this algebraic identity.

- **`tier0-computation/gauge_coupling_derivation.py`**: Derives g_1/g_2 = e^{-2s} and s_0 = 0.2994 from sin^2 theta_W (Session 17a, B-1). The Fermi constant G_F = g_2^2 / (4 sqrt(2) M_W^2), which determines all neutrino cross sections in Papers 01, 02, 06, 09, and 10, is a geometric output of this derivation.

No scripts directly compute neutrino oscillation parameters (Delta m^2, mixing angles, PMNS matrix elements) from the Dirac spectrum. This is a Tier 2 deliverable requiring the full spinor transport calculation (Baptista Paper 14, Section 3.2) to assign mass eigenvalues to specific neutrino species and compute the overlap integrals that determine PMNS angles.
