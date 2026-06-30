# Einstein Paper Index

**Researcher**: Einstein (+ collaborators: Will, Touboul/MICROSCOPE, Blanchet, Brunner et al., Bao et al., Sola Peracaula, Capozziello, DESI Collaboration, Giare et al., McAllister-Quevedo, Bronnikov-Rubin, Vacher et al., Bernardo-Brandenberger, Giulini, Chunn et al., King et al., Suzuki-Zurek, Zloshchastiev)
**Papers**: 20 (PDF-backed, 1993-2025) + 16 historical references (pre-arXiv)
**Primary domain**: General relativity experimental tests, equivalence principle, EIH formalism, cosmological constant problem, dark energy dynamics, moduli stabilization, quantum foundations, analog gravity, Kibble-Zurek defect formation
**Project relevance**: These papers define the gravitational, cosmological, and foundational constraints that the M4 x SU(3) phonon-exflation framework must satisfy -- from the MICROSCOPE precision floor (eta < 10^{-15}) through the DESI DR2 dark energy signal (3-4 sigma), the CC problem and its nonlocal resolution, to the analog gravity and KZM physics that underpin the transit mechanism.
**Rebuilt**: 2026-03-27 from arXiv source PDFs. All content traces to source PDFs.

---

## Dependency Graph

```
GR FOUNDATIONS & EQUIVALENCE PRINCIPLE
  01 (Will 2014 Review) ──────> 02 (MICROSCOPE 2022: tightest WEP, eta<10^{-15})
       |                              |
       +────> 03 (Will 2018: Modified EIH, sensitivities)
       |           |
       |           +────> 04 (Blanchet 2025: 3PN structure coefficients, SEP test)
       |
       +────> 14 (Vacher 2023: Runaway dilaton constraints)
                   [uses 01 PPN + 02 MICROSCOPE bounds]

QUANTUM FOUNDATIONS
  05 (Brunner 2014: Bell nonlocality review) ── standalone
  06 (Bao 2024: ER=EPR operational theorem) ── standalone
       [both inform framework GGE entanglement structure]

DARK ENERGY & COSMOLOGICAL CONSTANT
  07 (Sola 2024: Vacuum Energy RVM) <──> 08 (Sola 2022: Running Vacuum review)
       |                                        |
       +──── both cite ───> 10 (DESI DR2 2025: BAO, w_0 w_a)
       |                         |
       |                    11 (Giare 2025: w(z) non-parametric reconstruction)
       |                         [uses 10 as primary dataset]
       |
  09 (Capozziello 2025: Weinberg no-go + IDG nonlocal evasion)
       [addresses same CC problem as 07-08 via nonlocality]

EXTRA DIMENSIONS & MODULI
  12 (McAllister-Quevedo 2023: KKLT/LVS string review)
       |
       +────> 13 (Bronnikov-Rubin 2006: F(R) stabilization, classical)
       |           [same problem, higher-curvature approach]
       |
       +────> 14 (Vacher 2023: Runaway dilaton)
       |           [dilaton = modulus; constrained by 01, 02]
       |
       +────> 15 (Bernardo-Brandenberger 2021: Swampland + string gas)
                   [shape moduli via string gas; swampland compliance]

SUPERSPACE, ANALOG GRAVITY & DEFECTS
  16 (Giulini 1993: WDW metric on superspace) ── standalone
       [mathematical foundation for TT sector stability]
  17 (Chunn 2025: Phonon BEC FLRW) ── standalone
       [direct BEC analog of phonon creation mechanism]
  18 (King 2024: KZM Ising domains)
       |
       +────> 19 (Suzuki-Zurek 2024: Tunable KZM + nucleation)
                   [extends KZM to weakly first-order; both inform transit]
  20 (Zloshchastiev 2020: SVT scale-dependent gravity) ── standalone
       [superfluid vacuum -> emergent multi-scale gravity]

CROSS-GROUP BRIDGES
  01 <-> 14: PPN/Eotvos bounds constrain dilaton/modulus coupling
  02 <-> 14: MICROSCOPE directly bounds alpha_h < 5x10^{-6}
  03 <-> 04: EIH at 1PN (03) vs 3PN structure dependence (04)
  07 <-> 10: RVM predicts w > -1 quintessence; DESI tests it
  09 <-> 07: Nonlocal gravity evades Weinberg no-go; RVM is an example
  12 <-> 13: String vs classical KK moduli stabilization
  17 <-> 20: BEC phonon cosmology from experiment (17) vs theory (20)
  18 <-> 19: KZM for Ising condensed matter (18) extended to first-order (19)
```

---

## Topic Map

### A. GR Foundations & Equivalence Principle
Papers: 01, 02, 03, 04
The experimental and theoretical backbone. Paper 01 (Will 2014) is the definitive review of all GR tests establishing the PPN formalism (10 parameters, all consistent with GR). Paper 02 (MICROSCOPE 2022) provides the tightest WEP test at eta < 10^{-15}. Paper 03 (Will 2018) generalizes EIH to include body-dependent sensitivities s_a and preferred-frame effects. Paper 04 (Blanchet 2025) identifies 40 structure-dependent coefficients at 3PN that may or may not cancel -- a direct test of whether SEP holds at the deepest level.

### B. Quantum Foundations
Papers: 05, 06
Paper 05 (Brunner 2014) is the comprehensive review of Bell nonlocality: local polytope, Tsirelson bound S <= 2sqrt(2), device-independent cryptography, nonlocality vs entanglement inequivalence. Paper 06 (Bao 2024) derives ER = EPR as an operational theorem from LOCC + holographic screens without embedding geometry, showing spacetime topology is observer-relative.

### C. Dark Energy & Cosmological Constant
Papers: 07, 08, 09, 10, 11
Papers 07-08 (Sola 2022, 2024) develop the Running Vacuum Model: rho_vac(H) = rho_0 + nu(H^2-H_0^2) with m^4 terms exactly cancelled by off-shell adiabatic renormalization. Paper 09 (Capozziello 2025) shows nonlocal (IDG) theories evade the Weinberg no-go theorem because infinitely many coupled auxiliary fields prevent independent variation. Papers 10-11 (DESI DR2, Giare 2025) provide 3.1-4.2 sigma evidence for dynamical dark energy with Quintom B behavior (w_0 > -1, w_a < 0).

### D. Extra Dimensions & Moduli
Papers: 12, 13, 14, 15
Paper 12 (McAllister-Quevedo 2023) reviews KKLT/LVS: flux superpotential fixes complex structure; non-perturbative effects fix Kahler moduli. Paper 13 (Bronnikov-Rubin 2006) demonstrates classical F(R) stabilization -- CC softened by ~30 orders but not solved. Paper 14 (Vacher 2023) constrains runaway dilaton couplings (alpha_{h,0} < 5x10^{-6} from MICROSCOPE). Paper 15 (Bernardo-Brandenberger 2021) shows string gas shape moduli satisfy swampland criteria with c_2 = pi/4.

### E. Superspace, Analog Gravity & Defects
Papers: 16, 17, 18, 19, 20
Paper 16 (Giulini 1993) establishes Lorentzian signature of WDW metric on superspace -- single negative direction is the conformal mode; TT modes positive definite. Paper 17 (Chunn 2025) demonstrates phonon FLRW cosmology in a BEC with Bogoliubov pair creation and entanglement. Papers 18-19 (King 2024, Suzuki-Zurek 2024) verify KZM for Ising domains and extend it to weakly first-order transitions via the combined formula n = f n_nuc + (1-f) n_KZM. Paper 20 (Zloshchastiev 2020) derives seven-term scale-dependent gravity from a logarithmic superfluid vacuum.

---

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| Equivalence principle constraints on tau | Papers 01, 02, 03, 14 | CRITICAL |
| EIH formalism and effacement | Papers 03, 04, 01 | CRITICAL |
| Cosmological constant problem | Papers 07, 08, 09 | CRITICAL |
| DESI dark energy constraints / w(z) | Papers 10, 11 | CRITICAL |
| Moduli stabilization | Papers 12, 13, 14, 15 | HIGH |
| KZM and BCS transit physics | Papers 18, 19, 17 | HIGH |
| Bell nonlocality and EPR | Papers 05, 06 | HIGH |
| Analog gravity / BEC cosmology | Papers 17, 20 | HIGH |
| Superfluid vacuum / DM from substrate | Paper 20 | HIGH |
| Weinberg no-go evasion / nonlocal CC | Paper 09 | HIGH |
| Superspace geometry / WDW metric | Paper 16 | MEDIUM |
| Swampland criteria | Papers 15, 12 | MEDIUM |
| Runaway dilaton / varying constants | Paper 14 | MEDIUM |

---

## Paper Entries

### Paper 01: The Confrontation between General Relativity and Experiment
- **File**: `01_2014_Will_Confrontation_GR_Experiment.md`
- **arXiv**: 1403.7377
- **Year**: 2014
- **Relevance**: CRITICAL
- **Tags**: PPN, EEP, WEP, LLI, LPI, Shapiro delay, perihelion, frame-dragging, gravitational waves, SEP, binary pulsars

**Summary**: The definitive review of all experimental tests of GR. Establishes the three-part EEP (WEP + LLI + LPI), the 10-parameter PPN formalism, and surveys constraints from torsion balances (eta < 2x10^{-13}), Cassini (gamma-1 = 2.1x10^{-5}), lunar laser ranging (eta_N < 4.4x10^{-4}), and binary pulsars (0.2% quadrupole radiation). All PPN parameters consistent with GR.

**Key Results**:
- WEP: eta < 2x10^{-13} (Eot-Wash); LLI: delta < 10^{-26}
- gamma - 1 = (2.1 +/- 2.3)x10^{-5} (Cassini Shapiro delay)
- Gravitational radiation damping verified to 0.2%
- All 10 PPN parameters consistent with GR

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Eotvos ratio | eta = 2\|a_1-a_2\|/\|a_1+a_2\| | Eq. (2) |
| Gravitational redshift | Z = (1+alpha) Delta U/c^2 | Eq. (6) |
| Perihelion advance | Delta omega = (6pi m/p)[1/3(2+2gamma-beta)+...] | Eq. (64) |
| Nordtvedt parameter | eta_N = 4beta-gamma-3-10/3 alpha_1-... | Eq. (65) |
| Sensitivity | s_a = d(ln m_a)/d(ln phi) | Via Will-Yunes |

**Dependencies**: Upstream: none (foundational). Downstream: 02, 03, 04, 14.

---

### Paper 02: MICROSCOPE Final Results -- Equivalence Principle
- **File**: `02_2022_Touboul_MICROSCOPE_Equivalence_Principle.md`
- **arXiv**: 2209.15487
- **Year**: 2022
- **Relevance**: CRITICAL
- **Tags**: WEP, Eotvos ratio, Ti-Pt, drag-free satellite, systematic errors, dilaton

**Summary**: Final MICROSCOPE results: delta(Ti,Pt) = [-1.5 +/- 2.3(stat) +/- 1.5(syst)] x 10^{-15}. No WEP violation. Factor 4.6 improvement. Temperature-dominated systematics. Constrains dilaton and U-boson couplings.

**Key Results**:
- delta(Ti,Pt) = [-1.5 +/- 2.3 +/- 1.5] x 10^{-15}
- Null reference: delta(Pt,Pt) = [0.0 +/- 1.1 +/- 2.3] x 10^{-15}
- Tightest WEP bound as of 2022

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Eotvos ratio | eta = 2(a_A-a_B)/(a_A+a_B) | Eqs. (1)-(2) |
| Measurement equation | Gamma_d = b_0 + delta_x g_x + Delta_x S_xx + n_d | Eq. (4) |
| Final constraint | delta(Ti,Pt) = [-1.5 +/- 2.3 +/- 1.5]x10^{-15} | Eq. (5) |

**Dependencies**: Upstream: 01. Downstream: 14 (dilaton coupling bounds).

---

### Paper 03: Modified Einstein-Infeld-Hoffmann Framework
- **File**: `03_2018_Will_Yunes_Modified_EIH_Framework.md`
- **arXiv**: 1801.08999
- **Year**: 2018
- **Relevance**: CRITICAL
- **Tags**: EIH, sensitivities, N-body Lagrangian, preferred-frame, Nordtvedt, scalar-tensor, Einstein-Aether, binary pulsars

**Summary**: Generalizes EIH to include body-dependent parameters (sensitivities) and preferred-frame effects. The 1PN N-body Lagrangian uses parameters G_ab, B_ab, C_ab, E_ab, D_abc. GR: all reduce to 1 or 0. Derives parameters for scalar-tensor, Einstein-Aether, Khronometric theories. Binary pulsar bounds: |alpha_hat_1| < 3.4x10^{-5}.

**Key Results**:
- Modified EIH Lagrangian with 6 body-dependent parameter families
- GR values: G_ab = B_ab = D_abc = 1; A_a = C_ab = E_ab = 0
- |alpha_hat_1| < 3.4x10^{-5} (J1738+0333)
- Nordtvedt effect in J0337+1715 parameterized

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Sensitivity | s_a = d(ln m_a)/d(ln psi_A) | Eq. (6) |
| EIH Lagrangian | L = -sum m_a[1-v^2/2-...] + 1/2 sum (m_a m_b/r_ab)[G_ab+...] | Eq. (9) |
| Scalar-tensor G_ab | G_ab = 1 - 2zeta(s_a+s_b-2s_as_b) | Eq. (29) |
| Strong-field alpha_hat_1 | alpha_hat_1 = Delta(C+E) - 6B_- - 2G A^{(2)} | Eq. (50) |
| Nordtvedt parameter | eta_hat_N = G_12 - G_13 | Eq. (63) |

**Dependencies**: Upstream: 01. Downstream: 04.

---

### Paper 04: Compact Binary EOM at 3PN -- Internal Structure?
- **File**: `04_2025_Blanchet_3PN_Internal_Structure.md`
- **arXiv**: 2503.03189
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: 3PN, DIRE, structure coefficients, SEP, EOS, gravitational waves

**Summary**: Identifies 40 structure-dependent coefficients at 3PN via the DIRE approach. These dimensionless integrals (Lambda_1, Lambda_2, ...) depend on NS equation of state but not on mass/radius. At 1PN and 2PN they cancel (SEP verified); at 3PN cancellation is unproven. Could alter waveform coefficients by up to 100%. Would appear 2 PN orders earlier than tidal effects.

**Key Results**:
- 40 distinct structure coefficients at 3PN
- Independent of mass/radius, EOS-dependent
- Could alter 3PN waveforms by up to 100%
- If cancelled: remarkable SEP support. If not: impacts next-gen GW detectors

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Relaxed Einstein equations | Box h^{ab} = -16pi tau^{ab} | Eq. (2.1) |
| Structure coefficient | Lambda_1 = (4pi/m) int rho r^2 U_int dr | Sec. III |
| Continuum EOM | dv^i/dt = U_{,i} + a_PN + a_2PN + a_3PN + ... | Eq. (2.9) |

**Dependencies**: Upstream: 01, 03. Downstream: none (frontier).

---

### Paper 05: Bell Nonlocality (Review)
- **File**: `05_2014_Brunner_Bell_Nonlocality_Review.md`
- **arXiv**: 1303.2849
- **Year**: 2014
- **Relevance**: HIGH
- **Tags**: Bell theorem, CHSH, Tsirelson bound, local polytope, quantum correlations, entanglement, DIQKD, Werner states

**Summary**: Comprehensive review of Bell nonlocality. Develops the hierarchy: local polytope (L) subset quantum (Q) subset no-signaling (NS). CHSH inequality S <= 2 violated by QM at 2sqrt(2). Nonlocality and entanglement are inequivalent. Pure entangled states always nonlocal (Gisin); mixed states may not be. Device-independent QKD and randomness from Bell violation.

**Key Results**:
- CHSH: S <= 2 (local); 2sqrt(2) (quantum); 4 (no-signaling)
- Pure entangled => nonlocal (Gisin); mixed entangled may be local (Werner)
- Detection efficiency threshold eta > 82.8% for CHSH
- Multipartite: Svetlichny S_3 <= 4 (local); 4sqrt(2) (GHZ)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Locality condition | p(ab\|xy) = int q(lambda) p(a\|x,lambda) p(b\|y,lambda) dlambda | Eq. (3) |
| CHSH inequality | S <= 2 | Eq. (4) |
| Quantum violation | S = 2sqrt(2) | Eq. (5) |
| Svetlichny | S_3 <= 4; GHZ achieves 4sqrt(2) | Sec. VI.B.1 |

**Dependencies**: Upstream: none. Downstream: 06.

---

### Paper 06: ER = EPR Is an Operational Theorem
- **File**: `06_2024_Bao_ER_EPR_Operational_Theorem.md`
- **arXiv**: 2410.16496
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: ER=EPR, LOCC, holographic screen, monogamous entanglement, observer-relative topology

**Summary**: Derives ER = EPR operationally: monogamous entanglement is indistinguishable from topological identification of boundary points under LOCC + holographic boundary. No embedding geometry needed. Proves non-traversability without firewalls. Shows spacetime topology is observer/QRF-relative.

**Key Results**:
- ER = EPR from LOCC + holographic principle
- Non-traversability without firewalls
- Spacetime topology is observer-relative

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Hamiltonian decomposition | H_E = H_Q + H_Qbar + H_{Q,Qbar} | Proof of Thm. 1 |
| Decoherence limit | H_{Q,Qbar} -> 0 => Q, Qbar decouple | Proof of Thm. 1 |

**Dependencies**: Upstream: 05. Downstream: none.

---

### Paper 07: Vacuum Energy and CC in QFT in Curved Spacetime
- **File**: `07_2024_Sola_Peracaula_Vacuum_Energy_CC.md`
- **arXiv**: 2411.06582
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: RVM, running vacuum, CC problem, adiabatic regularization, off-shell subtraction, m^4 cancellation, quintessence, DESI

**Summary**: The Running Vacuum Model derived from off-shell adiabatic regularization. m^4 terms cancel exactly. VED runs as rho_vac(H) = rho_0 + (3nu/8piG)(H^2-H_0^2) with nu ~ 10^{-3}. RVM-inflation via H^6. Vacuum EoS mimics quintessence (w > -1), consistent with DESI.

**Key Results**:
- m^4 fine-tuning cancelled by off-shell subtraction (no free parameters)
- nu_eff ~ 10^{-5} to 10^{-3} for GUT-scale particles
- RVM-inflation from H^6 provides graceful exit without inflaton
- Vacuum EoS: w > -1 (quintessence-like)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Canonical RVM | rho_vac(H) = rho_0 + (3nu_eff/8piG)(H^2-H_0^2) | Eq. (27) |
| Running parameter | nu_eff ~ (1/2)(xi-1/6)(m^2/m_Pl^2) ln(m^2/H_0^2) | Eq. (28) |
| Running VED (no m^4) | rho_vac(M,H) = rho_vac(M_0,H) + (3xi_bar/16pi^2)H^2[...] | Eq. (24) |
| RVM-inflation | rho_vac(a) = rho_I(1+(a/a_*)^8)^{-3/2} | Eq. (30) |

**Dependencies**: Upstream: none. Downstream: 08, 10.

---

### Paper 08: Running Vacuum Cosmology (Review)
- **File**: `08_2022_Sola_Peracaula_Running_Vacuum_Cosmology.md`
- **arXiv**: 2203.13757
- **Year**: 2022
- **Relevance**: HIGH
- **Tags**: running vacuum, CC problem, effective action, RVM-inflation, H_0 tension, sigma_8 tension, Type-II RRVM

**Summary**: Comprehensive review of the RVM program. Derives running VED from both adiabatic regularization and effective action. Type-II RRVM (evolving G_eff) alleviates H_0 and sigma_8 tensions (H_0 = 70.93, DIC = +5.5). Beta-function for VED running derived.

**Key Results**:
- m^4 cancellation confirmed via two independent methods
- Beta-function: beta_vac = (xi-1/6)(3H^2/8pi^2)(M^2-m^2)
- Type-II RRVM: H_0 = 70.93 +/- 0.90 km/s/Mpc

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Generalized RVM | rho_vac = (3/8piG)[c_0 + nu H^2 + nu_tilde Hdot] | Eq. 8.1 |
| Beta-function | beta_vac = (xi-1/6)(3H^2/8pi^2)(M^2-m^2) | Eq. 6.13 |
| Quartic cancellation | Delta Lambda + (1/128pi^2)[-M^4+M'^4+...] = 0 | Eq. 5.8 |

**Dependencies**: Upstream: 07. Downstream: 10, 11.

---

### Paper 09: Weinberg No-Go Theorem and Nonlocal Gravity
- **File**: `09_2025_Capozziello_Weinberg_Nonlocal_Gravity.md`
- **arXiv**: 2502.07321
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: Weinberg no-go, CC, nonlocal gravity, IDG, auxiliary fields, recurrence relation

**Summary**: Shows IDG theories evade the Weinberg no-go theorem. The theorem requires independent variation of all fields; IDG's auxiliary fields phi_n = Box^{-n} R are coupled by recurrence phi_n = Box^{-1} phi_{n-1}, preventing independent variation. The transverse hypersurface construction fails. Nonlocal terms can reproduce cosmic acceleration without fine-tuning Lambda.

**Key Results**:
- Weinberg no-go relies crucially on locality
- IDG fields coupled by recurrence: no independent variation
- Nonlocal terms reproduce cosmic acceleration without Lambda
- Ghost-free under specific propagator conditions

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Weinberg constraint | L = e^{4phi} sqrt(-g) L_0(sigma_j) | Eq. (9) |
| IDG series | R sum f_{1-n} Box^{-n} R | Eq. (12) |
| Recurrence | phi_n = Box^{-1} phi_{n-1} | Eq. (14) |

**Dependencies**: Upstream: Weinberg (1989). Downstream: connects to 07-08.

---

### Paper 10: DESI DR2 BAO Cosmological Constraints
- **File**: `10_2025_DESI_DR2_BAO_Cosmological_Constraints.md`
- **arXiv**: 2503.14738
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: DESI, DR2, BAO, dark energy, w_0 w_a, LCDM tension, neutrino mass, Quintom B

**Summary**: DESI DR2 BAO from 14+ million tracers. Strongest BAO detection at 14.7 sigma. Flat LCDM: 2.3 sigma tension with CMB. Dynamical DE preferred at 3.1 sigma (DESI+CMB) to 4.2 sigma (DESI+CMB+DESY5). Quintom B: w_0 > -1, w_a < 0. Neutrino mass < 0.064 eV (LCDM), tight against oscillation minimum.

**Key Results**:
- 3.1-4.2 sigma preference for dynamical DE over LCDM
- Quintom B quadrant: w_0 > -1, w_a < 0
- sum m_nu < 0.064 eV (LCDM, 95% CL)
- Signal does not diminish from DR1 to DR2

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| CPL parametrization | w(a) = w_0 + w_a(1-a) | Eq. (9) |
| Sound horizon | r_d = 147.05 Mpc x (...) | Eq. (2) |
| Friedmann equation | H(z)/H_0 = [Omega_bc(1+z)^3 + ...]^{1/2} | Eq. (6) |
| BAO scaling | alpha_par = D_H r_d^fid / (D_H^fid r_d) | Eq. (11) |

**Dependencies**: Upstream: Planck CMB, SNe compilations. Downstream: 11.

---

### Paper 11: Dynamical Dark Energy in Light of DESI DR2
- **File**: `11_2025_Giare_Dynamical_Dark_Energy_DESI_DR2.md`
- **arXiv**: 2504.06118
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: w(z), shape functions, non-parametric, Horndeski, Bayesian evidence, PCA

**Summary**: Non-parametric w(z) reconstruction from DESI DR2: oscillatory pattern with w > -1 at z < 0.2, w < -1 at z ~ 0.75. SNR for w != -1 reaches 4.5 sigma (DR2+DESY5). Bayesian evidence: Delta ln E = 5.2 (moderate). ~3 PCA degrees of freedom. Pattern stable across all datasets and not producible by known systematics.

**Key Results**:
- Oscillatory w(z) stable across all datasets
- SNR up to 4.5 sigma for w != -1
- Bayesian evidence moderate: Delta ln E = 5.2
- ~3 effective DOF in w(z)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| SNR definition | SNR^2 = (w-w_mod)^T C_w^{-1} (w-w_mod) | Eq. (1) |
| Shape function S_2 | S_2(a) = w(a) - w'(a)/(3w(a)) | Eq. (5) |
| Horndeski prior | C(a) = 0.05+0.8a^2; R = exp[-(\|ln a-ln a'\|/0.3)^{1.2}] | Eq. (7) |

**Dependencies**: Upstream: 10. Downstream: none (frontier).

---

### Paper 12: Moduli Stabilization in String Theory
- **File**: `12_2023_McAllister_Quevedo_Moduli_Stabilization.md`
- **arXiv**: 2310.20559
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: KKLT, LVS, flux, Calabi-Yau, Kahler moduli, GVW superpotential, de Sitter uplift, swampland

**Summary**: Comprehensive review of string moduli stabilization. Flux superpotential W_flux fixes complex structure; non-perturbative effects (ED3/gaugino condensation) fix Kahler moduli. KKLT: AdS + uplift. LVS: exponentially large volume V ~ e^{a tau_s}. Discusses de Sitter challenges, swampland conjectures, and cosmological moduli problem (m > 30 TeV).

**Key Results**:
- W_flux fixes complex structure + axiodilaton; Kahler requires NP effects
- KKLT: AdS + uplift; LVS: V ~ e^{a tau_s}
- Peccei-Quinn symmetry protects superpotential to all orders
- Cosmological moduli problem: m > 30 TeV for BBN

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| GVW superpotential | W_flux = sqrt(2/pi) int G_3 wedge Omega | Eq. (27) |
| F-term potential | V_F = e^K[K^{MN} D_MW D_NW-bar - 3\|W\|^2] | Eq. (21) |
| LVS volume | V = tau_b^{3/2} - tau_s^{3/2} | Sec. 4.2 |

**Dependencies**: Upstream: none (review). Downstream: 13, 14, 15.

---

### Paper 13: Self-Stabilization of Extra Dimensions
- **File**: `13_2006_Bronnikov_Rubin_Self_Stabilization_Extra_Dimensions.md`
- **arXiv**: gr-qc/0510107
- **Year**: 2006
- **Relevance**: HIGH
- **Tags**: F(R) gravity, extra dimensions, KK, Einstein frame, conformal transformation, slow-change, de Sitter minimum

**Summary**: Higher-curvature F(R) Lagrangians (quadratic, cubic, R_AB R^AB, Kretschner) generate effective potentials with positive minima stabilizing extra dimensions. Quadratic: de Sitter only in F' < 0. Cubic: de Sitter in F' > 0. CC softened by ~30 orders from geometry, not fully solved.

**Key Results**:
- F(R) generates nontrivial minima for extra-dimension stabilization
- Cubic gravity: de Sitter in conventional regime
- CC softened ~30 orders, not solved
- Higher-curvature corrections add stabilization freedom

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Einstein-frame potential | V_Ein = -(sign F')[\|phi\|/(d_1(d_1-1))]^{d_1/2} F/F'^2 | Eq. (17) |
| Conformal mapping | g_tilde = \|f(phi)\| g, f = e^{d_1 beta} F' | Eq. (11) |

**Dependencies**: Upstream: 12 (context). Downstream: framework a_4/a_2 hierarchy.

---

### Paper 14: Runaway Dilaton: Improved Constraints
- **File**: `14_2023_Martinelli_Runaway_Dilaton.md`
- **arXiv**: 2301.13500
- **Year**: 2023
- **Relevance**: MEDIUM
- **Tags**: dilaton, fine-structure variation, MICROSCOPE, attractor, quintessence, Hubble tension

**Summary**: Full self-consistent constraints on the Damour-Piazza-Veneziano runaway dilaton including CMB. Order-unity couplings ruled out. \|alpha_{h,0}\| < 5x10^{-6} (MICROSCOPE). Attractor behavior: initial velocity irrelevant. Coupled to DE: H_0 = 68.2 partially addresses tension. With exponential potential: H_0 can only decrease.

**Key Results**:
- \|alpha_{h,0}\| < ~5x10^{-6}; order-unity couplings excluded
- Attractor mechanism operates for wide initial conditions
- Delta alpha/alpha = (alpha_{h,0}/40)[1 - e^{-(phi-phi_0)}]

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Klein-Gordon source | phi-ddot+3H phi-dot = -4piG dV/dphi + sum alpha_i(3P_i-rho_i) | Eq. (6) |
| Fine-structure variation | Delta alpha/alpha_0 = (alpha_{h,0}/40)[1-e^{-(phi-phi_0)}] | Eq. (10) |
| Eotvos from dilaton | eta ~ 5.2x10^{-5} alpha_{h,0}^2 | Eq. (12a) |

**Dependencies**: Upstream: 01, 02. Downstream: framework clock constraint.

---

### Paper 15: Shape Moduli Stabilization, String Gas, Swampland
- **File**: `15_2021_Bernardo_Brandenberger_Swampland_String_Gas.md`
- **arXiv**: 2008.13251
- **Year**: 2020
- **Relevance**: MEDIUM
- **Tags**: string gas cosmology, shape moduli, swampland, winding modes, T-duality

**Summary**: Shape moduli stabilized at the rectangular torus by winding + momentum modes. V(phi) ~ sqrt(p_nc^2+phi^2), quadratic near minimum. de Sitter conjecture satisfied with c_2 = pi/4. Distance conjecture satisfied (Delta phi < pi M_Pl/2). Stabilization requires stringy (winding) physics.

**Key Results**:
- Shape moduli stable at theta=0, R=1 (self-dual)
- de Sitter conjecture: c_2 = pi/4 (automatic)
- Stabilization inherently stringy (winding modes)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| de Sitter conjecture | \|V'/V\| < c_2/m_Pl | Eq. (1) |
| Modulus potential | V = e^{-2Phi} n sqrt(p_nc^2+phi^2) | Eq. (16) |
| de Sitter ratio | V'/V = phi/[sqrt(2) sqrt(p_nc^2+phi^2)] | Eq. (17) |

**Dependencies**: Upstream: 12. Downstream: framework swampland (S43).

---

### Paper 16: What Is the Geometry of Superspace?
- **File**: `16_1993_Giulini_Geometry_of_Superspace.md`
- **arXiv**: gr-qc/9311017
- **Year**: 1993
- **Relevance**: MEDIUM
- **Tags**: Wheeler-DeWitt metric, superspace, ultralocal, warped product, conformal mode, Lorentzian, ellipticity

**Summary**: WDW metric (beta=1) on superspace has Lorentzian signature (-,+,+,...). Single negative direction = conformal (trace) mode; shape deformations (TT modes) positive definite. At flat geometries the WDW metric fails (V cap H nonempty). beta=1 sits at the boundary of ellipticity. For round S^3: exactly one negative direction in horizontal subspace.

**Key Results**:
- WDW metric: Lorentzian on superspace
- Conformal mode negative; TT modes positive definite
- Fails at flat geometries
- beta=1 is degenerate elliptic (boundary)

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Ultralocal family | G_beta = (sqrt(g)/2)(g^ac g^bd + g^ad g^bc - 2beta g^ab g^cd) | Eq. (6) |
| Warped product | G_beta = -epsilon dtau^2 + (tau^2/c^2) tr(r^{-1}dr r^{-1}dr) | Eq. (10) |
| Operator D_beta | D_beta = delta d + 2(1-beta)d delta - 2Ric | Eq. (15) |

**Dependencies**: Upstream: none. Downstream: framework TT sector (Sessions 12, 20b).

---

### Paper 17: Phonon Dynamics in Curved Analog-Gravity BEC
- **File**: `17_2025_Barral_Phonon_Dynamics_Analog_Gravity_BEC.md`
- **arXiv**: 2508.03683
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: BEC, analog gravity, FLRW, phonon creation, Bogoliubov, two-mode squeezing, entanglement, de Sitter

**Summary**: 2D BEC with engineered density n_0 = n_bar(1+r^2/R^2)^2 realizes spherical FLRW metric (kappa=4/R^2) for phonons. Sudden scale-factor change creates backward-propagating ripples and entangled phonon pairs via Bogoliubov mixing (N = |beta_k|^2, maximal at l=1). Logarithmic negativity E_N quantifies entanglement. Experimentally accessible with K-39 BEC.

**Key Results**:
- Engineered BEC density -> spherical FLRW for phonons
- Bogoliubov pair creation: maximal at l=1
- Backward-propagating ripples from scale-factor discontinuities
- Entanglement suppressed by thermal noise

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| FLRW metric | ds^2=-dt^2+a^2[du^2/(1-kappa u^2)+u^2 dphi^2] | Eq. (15) |
| Mode equation | v-ddot_k + 2(a-dot/a)v-dot_k + (\|h\|/a^2)v_k = 0 | Eq. (44) |
| Bogoliubov mixing | b_km = alpha*_k a_km + beta*_k a-dag_{km-bar} | Eq. (53) |
| Particle number | N = \|beta_k\|^2 | Eq. (54) |
| Log negativity | E_N = max{0,-log_2[(1+2n_B)(sqrt(1+\|beta\|^2)-\|beta\|)^2]} | Eq. (64) |

**Dependencies**: Upstream: Unruh (1981), BLV. Downstream: framework phonon creation (S38).

---

### Paper 18: Kibble-Zurek Mechanism of Ising Domains
- **File**: `18_2024_King_Kibble_Zurek_Ising_Domains.md`
- **arXiv**: 2306.15821
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: KZM, Ising, NiTiO3, BiTeI, ferro-rotational, polar, dynamical exponent, long-range interactions

**Summary**: First KZM verification for topologically-trivial 3D Ising domains. NiTiO3 ferro-rotational: beta_KZM ~ 0.85 (consistent with 3D Ising ~0.81). BiTeI polar: anomalous beta ~ 1.1, implying z ~ 1.14 (vs 2.12), from long-range dipolar interactions. Topological defects immune to dipolar modification; Ising domains are not.

**Key Results**:
- KZM valid for topologically-trivial Ising domains
- NiTiO3: beta ~ 0.85 (agrees with theory ~0.81)
- BiTeI: anomalous beta ~ 1.1, z ~ 1.14
- Long-range interactions steepen KZM for non-topological defects

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| KZM exponent | beta_KZM = D nu / (1+nu z) | Eq. (1) |
| 3D Ising exponents | nu ~ 0.63, z ~ 2.12 | Fig. 2b |

**Dependencies**: Upstream: Kibble-Zurek theory. Downstream: 19.

---

### Paper 19: Topological Defects in Tunable Phase Transitions
- **File**: `19_2024_Suzuki_Zurek_Topological_Defect_Tunable_Transition.md`
- **arXiv**: 2312.01259
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: KZM, first-order, nucleation, Avrami, tunable order, Langevin, bounce action

**Summary**: Extends KZM to weakly first-order transitions. Modified LG potential V = (phi^4-2epsilon phi^2)/8 - c|phi|^3/3 tunes transition order. Combined formula n = f n_nuc + (1-f) n_KZM interpolates using the Avrami fraction f. Fast quenches preserve KZM even for c > 0. For c=0: n_KZM ~ tau_Q^{-1/4} confirmed.

**Key Results**:
- Combined KZM + nucleation: n = f n_nuc + (1-f) n_KZM
- Avrami fraction f diagnoses regime
- Fast quenches preserve KZM for weakly first-order
- c=0: n_KZM ~ tau_Q^{-1/4} confirmed

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Modified LG | V = (phi^4-2epsilon phi^2)/8 - c\|phi\|^3/3 | Eq. (1) |
| Avrami equation | f = 1 - exp(-Omega) | Eq. (7) |
| Combined formula | n = f n_nuc + (1-f) n_KZM | Eq. (10) |
| Nucleation rate | Gamma = A exp[-B(epsilon)/theta] | Eq. (5) |

**Dependencies**: Upstream: 18, Kibble-Zurek. Downstream: framework BCS transit (S36 Z_2).

---

### Paper 20: Scale-Dependent Gravity in Superfluid Vacuum Theory
- **File**: `20_2020_Zloshchastiev_Scale_Dependent_Gravity_SVT.md`
- **arXiv**: 2011.12565
- **Year**: 2020
- **Relevance**: HIGH
- **Tags**: superfluid vacuum, logarithmic BEC, multi-scale gravity, rotation curves, DM, DE, Hubble tension, Mach principle

**Summary**: Logarithmic superfluid vacuum generates seven-term gravitational potential spanning sub-Newtonian to cosmological scales. Logarithmic nonlinearity F(rho)=-b ln(rho/rho_bar) uniquely selected by density-independent c_s (Lorentz symmetry). Flat rotation curves from Phi_gal ~ ln(r). Cosmic acceleration from Phi_dS ~ r^2. Two expansion mechanisms may explain Hubble tension. DM and DE from same superfluid resolve cosmological coincidence.

**Key Results**:
- Seven-term gravitational potential from sub-Newtonian to cosmological
- Flat rotation curves: Phi_gal = c_b^2 chi ln(r)
- de Sitter: Phi_dS = -c_b^2 r^2/L_dS^2
- Emergent mass: M = a_1 q/(m l_bar) (quantum Mach)
- Two expansion mechanisms -> Hubble tension resolution
- Running G_eff = G[1 + zeta L_chi ln(r)/r]

**Key Equations**:
| Label | Description | Reference |
|:---|:---|:---|
| Log-Schrodinger | i hbar d_t Psi = [-hbar^2/(2m) nabla^2 + V - b ln(\|Psi\|^2/rho_bar)] Psi | Eq. (9) |
| Seven-term potential | Phi = Phi_smi + Phi_RN + Phi_N + Phi_gal + Phi_mgl + Phi_dS + Phi_0 | Eq. (20) |
| Newtonian | Phi_N = -GM/r, GM = a_1 q/(m l_bar) | Eq. (23) |
| Galactic flat | Phi_gal = chi b_0 ln(r/l_bar)/m | Eq. (24) |
| Rotation curve | v = sqrt(GM/R + chi b_0/m + a_1 b_0 R/(m l_bar)) | Eq. (63) |

**Dependencies**: Upstream: Volovik program. Downstream: framework PI-fabric prediction.

---

## Historical References (No PDF Available)

| # | Paper | Year | Modern Coverage |
|:--|:------|:-----|:----------------|
| H1 | Einstein, "On the Electrodynamics of Moving Bodies" (SR) | 1905 | Paper 01 |
| H2 | Einstein, "Does the Inertia of a Body Depend on Its Energy Content?" (E=mc^2) | 1905 | Paper 01 |
| H3 | Einstein, "On a Heuristic Viewpoint Concerning Light" (photoelectric) | 1905 | Paper 05 |
| H4 | Einstein, "On the Movement of Small Particles" (Brownian motion) | 1905 | -- (LOW) |
| H5 | Einstein, "The Field Equations of Gravitation" | 1915 | Paper 01 |
| H6 | Einstein, "The Foundation of the General Theory of Relativity" | 1916 | Paper 01 |
| H7 | Einstein, "Cosmological Considerations in GR" (Lambda) | 1917 | Papers 07, 08, 09 |
| H8 | Einstein, "Quantum Theory of the Monoatomic Ideal Gas" (BEC) | 1924 | Papers 17, 20 |
| H9 | Einstein, Podolsky, Rosen, "Can QM Be Considered Complete?" (EPR) | 1935 | Paper 05 |
| H10 | Einstein, Infeld, Hoffmann, "Gravitational Equations and Problem of Motion" | 1938 | Papers 01, 03, 04 |
| H11 | Dyson, Eddington, Davidson, "Deflection of Light During Solar Eclipse" | 1919 | Paper 01 |
| H12 | Oppenheimer, Snyder, "On Continued Gravitational Contraction" | 1939 | -- (LOW) |
| H13 | Bell, "On the Einstein Podolsky Rosen Paradox" | 1964 | Paper 05 |
| H14 | Pound, Rebka, "Apparent Weight of Photons" | 1959 | Papers 01, 02 |
| H15 | Peldan, "On the DeWitt Metric" | 1987 | Paper 16 |
| H16 | PDG, "Extra Dimensions Review" | 2025 | Paper 12 |

---

## Cross-Paper Equation Concordance

### Eotvos Ratio (eta)
- Paper 01 Eq. (2): eta = 2|a_1-a_2|/|a_1+a_2| -- general definition
- Paper 02 Eqs. (1-2): eta = (m_g/m_i)_A - (m_g/m_i)_B -- MICROSCOPE measurement
- Paper 14 Eq. (12a): eta ~ 5.2x10^{-5} alpha_{h,0}^2 -- dilaton-induced WEP violation

### Sensitivity (Structure Dependence)
- Paper 01 via Will-Yunes: s_a = d(ln m_a)/d(ln phi) -- PPN context
- Paper 03 Eq. (6): s_a^{(A)} = partial(ln m_a)/partial(ln psi_A) -- generalized EIH
- Paper 03 Eq. (29): G_ab = 1 - 2zeta(s_a+s_b-2s_as_b) -- scalar-tensor

### Nordtvedt Parameter
- Paper 01 Eq. (65): eta_N = 4beta-gamma-3-... -- PPN (weak field)
- Paper 03 Eq. (63): eta_hat_N = G_12 - G_13 -- modified EIH (strong field)

### Vacuum Energy Density (Running)
- Paper 07 Eq. (27): rho_vac(H) = rho_0 + (3nu/8piG)(H^2-H_0^2) -- RVM canonical
- Paper 08 Eq. 5.10: same formula, extended derivation
- Paper 08 Eq. 8.1: rho_vac = (3/8piG)[c_0 + nu H^2 + nu_tilde Hdot] -- generalized RVM

### Dark Energy Equation of State
- Paper 07 Sec. 9: w_vac(z) ~ -1 + nu_eff[...] -- RVM prediction
- Paper 10 Eq. (9): w(a) = w_0 + w_a(1-a) -- CPL parametrization
- Paper 11 Eq. (5): Shape functions S_0, S_1, S_2 -- model-independent diagnosis

### Bogoliubov Transformation (Particle Creation)
- Paper 17 Eq. (53): b_km = alpha*_k a_km + beta*_k a-dag_{km-bar}
- Paper 17 Eq. (54): N = |beta_k|^2
- Paper 17 Eq. (64): Entanglement via logarithmic negativity E_N

### KZM Universal Scaling
- Paper 18 Eq. (1): beta_KZM = D nu / (1+nu z) -- pure second-order
- Paper 19 Eq. (10): n = f n_nuc + (1-f) n_KZM -- combined with nucleation

### FLRW Metric (Real and Analog)
- Paper 10 Eq. (6): H(z)/H_0 = [...] -- cosmological Friedmann equation
- Paper 17 Eq. (15): ds^2 = -dt^2 + a^2[du^2/(1-kappa u^2)+u^2 dphi^2] -- BEC analog
- Paper 20 Eq. (5): emergent metric from superfluid condensate

### Moduli / Scalar Field Potential
- Paper 12 Eq. (21): V_F = e^K[K^{MN} D_MW D_NW-bar - 3|W|^2] -- string F-term
- Paper 13 Eq. (17): V_Ein = -(sign F')[|phi|/(d_1(d_1-1))]^{d_1/2} F/F'^2 -- KK F(R)
- Paper 15 Eq. (16): V = e^{-2Phi} n sqrt(p_nc^2+phi^2) -- string gas
- Paper 20 Eq. (15): Phi = (1/m)(b_0-q/r^2) ln(|Psi|^2/rho_bar) -- SVT

---

## Notation Conventions

| Symbol | Meaning | Papers |
|:---|:---|:---|
| eta | Eotvos ratio (WEP violation parameter) | 01, 02, 14 |
| gamma, beta | PPN parameters (GR: both = 1) | 01, 03 |
| s_a | Sensitivity (d ln m_a / d ln psi) | 01, 03 |
| G_ab, B_ab, C_ab, E_ab, D_abc | Modified EIH Lagrangian parameters | 03 |
| eta_N, eta_hat_N | Nordtvedt parameter (PPN vs strong-field) | 01, 03 |
| rho_vac | Vacuum energy density | 07, 08 |
| nu_eff | RVM running parameter (~10^{-3}) | 07, 08 |
| w_0, w_a | CPL DE equation of state parameters | 10, 11 |
| alpha_k, beta_k | Bogoliubov coefficients | 17 |
| beta_KZM | KZM universal defect exponent | 18, 19 |
| nu, z | Critical exponents (spatial, dynamical) | 18, 19 |
| f | Avrami fraction (nucleated volume) | 19 |
| c_s | Sound speed (BEC, superfluid) | 17, 20 |
| G_beta | Ultralocal metric on Riem(Sigma) | 16 |
| tau_a, theta_a | Kahler modulus (volume, axion) | 12 |
| phi, alpha_i | Dilaton field, coupling functions | 14 |
| Psi | Superfluid condensate wavefunction | 20 |
| xi, xi_bar | Non-minimal coupling (xi_bar = xi - 1/6) | 07, 08 |

---

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 01 | PPN parameters consistent with GR | Yes (experiments surveyed) | Will 2014 Tables |
| 02 | delta(Ti,Pt) < 10^{-15} | Yes (MICROSCOPE final) | Paper 02 |
| 03 | GR: G_ab=B_ab=D_abc=1 | Yes (analytic) | Paper 03 below Eq. (11) |
| 04 | 40 structure coefficients at 3PN | Identified, not resolved | Paper 04 Table I |
| 05 | Tsirelson bound S <= 2sqrt(2) | Yes (proven theorem) | Tsirelson 1980 |
| 07-08 | m^4 cancellation in RVM | Yes (two methods) | Papers 07, 08 |
| 07 | nu_eff ~ 10^{-3} | Estimated (model-dependent) | Paper 07 Eq. (28) |
| 10 | DESI DR2 BAO 14.7 sigma | Yes (data) | Paper 10 Sec. III |
| 10 | 3.1-4.2 sigma w != -1 | Yes (DESI+CMB+SNe) | Paper 10 Sec. VII |
| 13 | V_Ein minima for cubic F(R) | Yes (numerical) | Paper 13 Figs. 3-4 |
| 15 | de Sitter c_2 = pi/4 | Yes (analytic) | Paper 15 Eq. (17) |
| 17 | Bogoliubov N = \|beta\|^2 | Yes (analytic + numerical) | Paper 17 Figs. 6-7 |
| 18 | beta_KZM ~ 0.85 (NiTiO3) | Yes (experimental) | Paper 18 Fig. 2a |
| 18 | beta_KZM ~ 1.1 (BiTeI) | Yes (experimental) | Paper 18 Fig. 4c |
| 19 | n = f n_nuc + (1-f) n_KZM | Yes (Langevin numerics) | Paper 19 Figs. 3-5 |
| 20 | Flat rotation curves from ln(r) | Yes (analytic) | Paper 20 Eq. (63) |
| Framework | Effacement: s_a(tau)=0 | Structural (block-diagonal thm) | Session 22b |
| Framework | Clock dalpha/alpha=-3.08 tau_dot | Yes (computation) | Session 22d |
| Framework | Swampland \|V'\|/V=7.67 M_Pl | Yes (computation) | Session 43 |
