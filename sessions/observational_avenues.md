# Observational Avenues Reference -- Phonon-Exflation Framework

**Compiled**: 2026-02-28
**Scope**: `sessions/` (all subdirectories), `tier0-computation/` (.py, .txt, .npz), `researchers/` (.md), `tools/knowledge-index.json`
**Method**: Exhaustive cross-reference of instrument names, observable quantities, gate identifiers, and prediction keywords across all project files

---

## Master Table of Observational Programs

| Program | Type | Sessions | Observable | Framework Prediction | Gate Status |
|:--------|:-----|:---------|:-----------|:--------------------|:------------|
| DESI | Galaxy survey / BAO | 22d, 23c, 24a, 24b, 28, 29Aa | w_0, w_a; P(k) features | w = -1 (frozen modulus); P(k) feature at k_transition | CLOSED (rolling); OPEN conditional (P(k)) |
| Euclid | Galaxy survey / weak lensing | 22d, 28 | P(k), void statistics, sigma_8 | P(k) feature; void size distribution | OPEN conditional |
| SDSS / BOSS | Galaxy survey / BAO | misc/giants-bao | BAO standard ruler T(k) | T(k) reproduction to < 1% | Structural consistency |
| Planck | CMB satellite | 22d, many | Cosmological parameters, sum m_nu | sum m_nu < 0.072 eV; H_0 | OPEN conditional |
| JWST | Space telescope | 23a, 24b, 28 | Early galaxies z > 10, LRDs z ~ 4-9 | Directional consistency with early structure | Speculative |
| KATRIN | Neutrino mass | 16, 19d, 20b, 21c, 22, 28 | m_nu (absolute) | m_nu1 from Dirac spectrum at tau_0 | OPEN conditional |
| JUNO | Reactor neutrino | 19d, 22, 28 | Mass ordering | Normal ordering (bowtie, tau_0 > 0.11) | OPEN conditional |
| DUNE | Accelerator neutrino | 22, 28 | Mass ordering, CP phase | Normal ordering; nu = nu_bar (CPT) | OPEN conditional |
| ALPHA / ALPHA-g | Antihydrogen | 22c, 22d, 23a, 28 | CPT, antimatter gravity | a_g = g; [J, D_K] = 0 | PASS (consistency) |
| BASE | Penning trap | 22c, 22d, 28 | q/m ratio at 16 ppt | m(p) = m(p_bar); [J, D_K] = 0 | PASS (consistency) |
| AEgIS | Positronium / antimatter | 22c | Ps BEC, antimatter gravity | J-even condensate analog | Speculative |
| LIGO / Virgo | GW interferometer | G2, G3, 20b, 28 | GW speed, dispersion | c_GW = c; no Lorentz violation | PASS (consistency) |
| LISA | Space GW detector | G2, G3, 28 | Stochastic GW background | f_peak ~ 10^7-10^9 Hz (KK-scale) | Speculative |
| NANOGrav / IPTA | Pulsar timing array | G2 | Stochastic GW background | SM-like QCD contribution | Consistent |
| Einstein Telescope | Next-gen GW | G1, G2, G3 | Ringdown spectroscopy | eta/s correction to QNM damping | Speculative (20-yr timeline) |
| CMB-S4 | CMB ground | G3 | Damping tail, r | Debye cutoff; r from Weyl curvature | Speculative |
| BICEP / Keck | CMB B-mode | G2 | Tensor-to-scalar ratio r | r from initial |C|^2 = 5/14 | Speculative |
| LiteBIRD | CMB satellite | -- | r measurement | Not explicitly referenced | -- |
| Simons Observatory | CMB ground | -- | CMB lensing | Not explicitly referenced | -- |
| Rubin / LSST | Optical survey | 28 | P(k), voids | Void size distribution | OPEN conditional |
| Roman (WFIRST) | Space telescope | 24b | Dark energy, deceleration | w = -1 | Speculative |
| LHC / ATLAS / CMS | Particle collider | misc/giants | KK gravitons, micro-BH | No KK below ~15 TeV | PASS (null consistency) |
| KamLAND | Reactor neutrino | 22, 28 | CPT test (oscillation) | nu_e = nu_e_bar parameters | PASS (consistency) |
| KamLAND-Zen | Double beta decay | 28 | Majorana vs Dirac | J^2 = +1 permits Majorana; undetermined | OPEN |
| Super-Kamiokande | Atmospheric neutrino | 28 | Mass ordering hint | Normal ordering | OPEN conditional |
| Hyper-K | Next-gen atmospheric | 22, 28 | Mass ordering, CP phase | Normal ordering; delta_CP from eigenspinors | OPEN conditional |
| IceCube | High-energy neutrino | 28 | Flavor ratio | (1:1:1) from 3-generation Z_3 | PASS (consistency) |
| KATRIN-TRISTAN | keV sterile search | 22, 28 | Beta endpoint kink | First KK excitation at lambda_next * M_scale | OPEN conditional |
| LEGEND / nEXO | Majorana search | 28 | m_beta-beta | Determined by spectral action at tau_0 | OPEN |
| Project 8 | Tritium endpoint | 28 | m_nu (absolute), target ~0.04 eV | m_nu1 from Dirac spectrum at tau_0 | OPEN conditional |
| Eot-Wash | Fifth force / gravity | misc/giants | 1/r^2 to 50 um | G_4 = G_12/Vol(K), constant | PASS (consistency) |
| LLR | Gravity test | misc/giants | dG/dt/G < 10^{-12}/yr | G constant (volume-preserving TT) | PASS (consistency) |
| Oklo reactor | Historical | misc/giants | delta-alpha_s < few % over 2 Gyr | alpha constant (frozen modulus) | PASS (consistency if frozen) |
| Quasar absorption | Spectroscopic | misc/giants | delta-alpha/alpha < 4e-7 over 10 Gyr | alpha constant (frozen modulus) | PASS (consistency if frozen) |
| Optical lattice clocks | Atomic clocks | G3, misc/giants | dalpha/alpha < 10^{-16}/yr | Zero drift (frozen modulus) | CLOSED (rolling); Consistent (frozen) |
| ALPHA-2 | Antihydrogen spectroscopy | 22d | 1S-2S at 10^{-15} | No drift (frozen modulus) | OPEN (future) |
| SN1987A | Historical SN | misc/giants | Graviton leakage over 168,000 ly | No KK graviton leakage | PASS (consistency) |
| SKA | Radio telescope | G2, misc/giants | Stochastic GW complement | SM-like QCD/EW fossil | Speculative |
| PIXIE / FIRAS | CMB spectral distortion | misc/giants | Blackbody to 1/100,000 | CMB resonance hypothesis constrained | OPEN challenge |
| SPHEREx | NIR all-sky | -- | -- | Not explicitly referenced | -- |
| FCC-hh | Future collider | misc/giants | 100 TeV KK excitations | KK mass at M_Pl / sqrt(Vol(K, g_{tau_0})) | Speculative (2035+) |
| VIDE pipeline | Void analysis | 28 | Void size distribution | Secondary peak at healing length xi_heal | OPEN conditional |
| SH0ES / distance ladder | Local H_0 | 28 | 73.0 +/- 1.0 km/s/Mpc | H_0 from tau_0 prediction chain | OPEN conditional |
| NuFIT / global fits | Neutrino global fit | 28 | PMNS matrix, ordering | Normal ordering (2.7 sigma current preference) | OPEN conditional |

---

## 1. Dark Energy and Equation of State

**Programs**: DESI, Euclid, Roman, Rubin/LSST
**Source files**: Sessions 22d, 23c, 24a, 24b, 28, 29Aa; `researchers/Cosmic-Web/17_2025_DESI_BAO_Cosmological_Constraints.md`

### 1.1 Equation of State Parameters

DESI DR2 central values (2026-02): w_0 = -0.83 +/- 0.09, w_a = -0.45 +/- 0.31.

The rolling quintessence branch (E-1, Session 22d) produces w_0 in the DESI range. The clock constraint (E-3, Session 22d) excludes all rolling scenarios: dalpha/alpha = -3.08 * tau_dot violates atomic clock bounds (|dalpha/alpha| < 10^{-16}/yr) by a factor of 15,000 for minimum plausible rolling rates (tau_dot ~ 0.007 H_0). The frozen modulus (tau_dot = 0) predicts w = -1 exactly. This lies 1.9 sigma from the DESI central value. Bayesian factor: BF = 0.5 (marginal closure).

### 1.2 P(k) Feature from BCS Transition

If the BCS condensation at tau_0 imprints a feature in the matter power spectrum at k_transition = a(t_BCS) * H(t_BCS), this feature is absent in LCDM. DESI achieves sub-percent precision at k ~ 0.05-0.15 h/Mpc. A feature with amplitude > 1% at these scales is detectable at > 3 sigma (Session 28, cosmic-web-collab). The feature must not coincide with BAO wiggles at k_BAO ~ 0.04 h/Mpc (Session 29 plan, K-29e gate).

k_transition depends on the epoch of the BCS transition, which requires the tau-to-cosmic-time backreaction calculation. This calculation is a Session 29 priority (computations 29Ab-2, 29Ab-3). Status: OPEN conditional on backreaction.

Scenario mapping for k_transition (Session 29 plan):

| Transition Epoch | Cosmic Time | k_transition (h/Mpc) | Observational Window |
|:-----------------|:------------|:---------------------|:---------------------|
| GUT-scale | ~10^{-36} s | ~10^{26} | Unobservable |
| Electroweak | ~10^{-12} s | ~10^{16} | Unobservable |
| QCD | ~10^{-6} s | ~10^{8} | CMB spectral distortions only |
| Recombination | ~10^{5} yr | ~0.01-0.1 | DESI/Euclid sensitivity range |

If k_transition falls in the recombination-era range, BAO compatibility requires delta(r_s)/r_s < 0.5% (gate K-29e, Session 29 plan).

### 1.3 Void Size Distribution

If the BCS condensate has a characteristic coherence length (healing length xi_heal), void sizes below xi_heal are suppressed, producing a secondary peak in the void size distribution. Testable with the VIDE pipeline applied to SDSS and DESI void catalogs. Status: OPEN conditional.

### 1.4 S8 Tension

DESI: sigma_8 = 0.777 +/- 0.020. Planck: sigma_8 = 0.811 +/- 0.006. A modified growth rate at z < 1 from the framework would be tested by Euclid tomographic weak lensing. No growth rate prediction has been computed. Status: speculative.

### 1.5 Gate Verdicts

| Gate | Condition | Result | Session |
|:-----|:----------|:-------|:--------|
| E-1 (decisive) | w_0 in [-0.9, -0.75], w_a in [-0.8, -0.2] | CLOSED (rolling excluded) | 22d |
| E-1 (compelling) | w_0 in [-0.95, -0.65], w_a in [-1.2, -0.1] | CLOSED | 22d |
| E-1 (marginal) | w_0 = -1 | BF = 0.5 | 22d |
| P(k) feature | Sub-percent feature in DESI/Euclid range | OPEN conditional | 28/29 |
| P-29f | f_peak in LISA range + multi-peaked GW | OPEN | 28/29 |
| K-29e | delta(r_s)/r_s < 0.5% if t_BCS in recombination window | OPEN | 29 (plan) |

---

## 2. Neutrino Masses and Oscillations

**Programs**: KATRIN, JUNO, DUNE, Super-K, Hyper-K, IceCube, KamLAND, KamLAND-Zen, Project 8, KATRIN-TRISTAN, LEGEND, nEXO
**Source files**: Sessions 16, 19d, 20b, 21c, 22, 22b, 24a, 28

### 2.1 Prediction Pipeline

All neutrino mass predictions require tau_0 (modulus stabilization value).

```
tau_0 (from BCS gap equation)
  -> D_K eigenvalues at tau_0
  -> lightest three eigenvalues = neutrino mass eigenstates
  -> mass ratios (zero-parameter prediction)
  -> mass ordering (zero-parameter prediction)
  -> absolute scale requires M_scale (one parameter)
```

### 2.2 Mass Ordering

The bowtie eigenvalue structure places the (0,0) singlet sector as lightest throughout tau in [0.11, 1.58] (Session 22b). Stabilization at any tau_0 in this range gives Normal Ordering. This is topologically protected within the bowtie structure.

Experimental status:
- **JUNO** (53 km reactor baseline, expected ~2028, 3-4 sigma): Spectral distortion from solar-atmospheric interference determines ordering.
- **DUNE** (1300 km accelerator baseline, 2028-2035, > 5 sigma): MSW matter effects. Independent determination.
- **Atmospheric** (Super-K, IceCube-Upgrade, Hyper-K): Current preference for NO at ~2-3 sigma.
- **NuFIT global fit**: NO preferred at 2.7 sigma.

Gate condition: If JUNO finds IO and tau_0 lies outside [0.15, 1.55], the prediction fails.

### 2.3 Absolute Mass Scale

KATRIN current bound: m_nu < 0.45 eV. Final sensitivity: ~0.2 eV. Project 8 (cyclotron radiation emission spectroscopy) target: ~0.04 eV. Cosmological bound (Planck + DESI): sum m_i < 0.072 eV.

Without M_scale, no comparison is possible. Once tau_0 is fixed, the absolute mass is a zero-parameter prediction (Session 16 pipeline).

### 2.4 Massless Lightest Neutrino

If the Pfaffian of D_total changes sign at some tau_c, topological protection produces a massless or near-massless fermion. The D_K Pfaffian is trivially +1 (Session 17c, D-2). The D_total Pfaffian has not been computed (Tier C computation, prerequisites ~3 weeks as of Session 16).

Cosmological bound sum m_i < 0.072 eV is consistent with NO minimum sum ~0.06 eV, inconsistent with IO minimum sum ~0.10 eV.

### 2.5 CPT Equality

[J, D_K(tau)] = 0 for all tau (algebraic theorem, Session 17a). Neutrino-antineutrino mass equality is exact.

- **KamLAND**: nu_e and nu_e_bar oscillation parameters agree (CPT consistency).
- **DUNE**: nu/nu_bar comparison at accelerator energies.

### 2.6 Number of Generations

Z_3 = (p - q) mod 3 grading gives exactly 3 generations (Session 7). IceCube astrophysical neutrino flavor ratio consistent with (1:1:1) from 3-flavor oscillation (1:2:0 source). KATRIN: no 4th mass eigenstate detected.

### 2.7 Sterile Neutrinos

First KK excitation of the neutrino has mass lambda_next * M_scale. If M_scale places this in the 1-100 keV range, KATRIN-TRISTAN probes it via a kink in the beta endpoint spectrum (Sessions 22, 28). Status: OPEN conditional on M_scale.

### 2.8 Dirac vs. Majorana

J^2 = +1 at KO-dimension 6 permits Majorana mass terms. Whether they are generated depends on the spectral action at tau_0. KamLAND-Zen current bound: m_beta-beta < 0.036-0.156 eV (nuclear matrix element uncertainty). LEGEND and nEXO will improve sensitivity. Status: OPEN.

### 2.9 CP Violation Phase

delta_CP from eigenspinor overlaps at tau_0. The Z_3 x Z_3 geometry (Baptista Paper 18) qualitatively predicts near-maximal CP violation. No computed value exists. DUNE/Hyper-K target 10-20 degree precision. Status: qualitative prediction only.

### 2.10 Gate Verdicts

| Gate | Condition | Result | Session |
|:-----|:----------|:-------|:--------|
| R-1 | R = (m3^2 - m2^2)/(m2^2 - m1^2) in [17, 66] | FAIL (R ~ 10^{14} Kramers; K_a cross-check R = 5.68) | 24a |
| D-1 | [J, D_K] = 0 | PROVEN | 17a |
| Ordering (structural) | NO from bowtie for tau_0 in [0.11, 1.58] | OPEN conditional (JUNO) | 22b |

---

## 3. Precision Antimatter Tests

**Programs**: ALPHA, ALPHA-g, ALPHA-2, BASE, AEgIS
**Source files**: Sessions 17a, 22c, 22d, 23a, 28; `researchers/Antimatter/`

### 3.1 CPT from [J, D_K] = 0

Session 17a: [J, D_K(tau)] = 0 is an algebraic theorem. Particle-antiparticle mass equality holds for all tau regardless of stabilization mechanism.

### 3.2 BASE

Antiproton-to-proton charge-to-mass ratio measured at 16 ppt. Any J-odd condensate component produces m(particle) != m(antiparticle). BASE bounds J-odd component to < 10^{-12}. The framework guarantees zero J-odd component.

### 3.3 ALPHA

1S-2S antihydrogen at 2 ppt. From E-3 (Session 22d): dalpha/alpha = -3.08 * tau_dot. ALPHA at 2 ppt constrains tau_dot. Frozen modulus satisfies automatically. ALPHA-2 targets 10^{-15} sensitivity, detectable if tau_dot > 10^{-18}/yr.

### 3.4 ALPHA-g

a_g/g = 0.75 +/- 0.29 (current). J-even BCS condensate (K-0 PASS, Session 23a: Delta is J-even) predicts a_g = g exactly. Current 25% uncertainty does not constrain Planck-suppressed scalar forces. Future 1% WEP test (2026-2028) begins probing scalar forces from the radion/sigma field.

### 3.5 AEgIS

First laser-cooled Ps (2024, 380 K to 170 K). Long-term target: Ps BEC at T < 15 mK. A self-conjugate (J-even) Ps BEC is the laboratory analog of the J-even condensate required by the framework. Status: speculative (structural analog).

---

## 4. Coupling Constant Variation

**Programs**: Optical lattice clocks, quasar absorption spectroscopy, LLR, Oklo reactor
**Source files**: Sessions 22d, misc/giants-planck-geometry, framework-mechanism-discussion

### 4.1 Clock Constraint (E-3)

dalpha/alpha = -3.08 * tau_dot (derived from g_1/g_2 = e^{-2tau}, Session 17a identity).

Atomic clock bound: |dalpha/alpha| < 10^{-16}/yr. Minimum plausible rolling (tau_dot ~ 0.007 H_0) produces |dalpha/alpha| ~ 1.5 * 10^{-12}/yr, exceeding the bound by a factor of 15,000. This excludes all rolling modulus scenarios at 5 orders of magnitude (Session 22d).

### 4.2 Quasar Absorption

delta-alpha/alpha < 4 * 10^{-7} over 10 Gyr. Rolling at H_0 rate produces 155% change over 10 Gyr (violation by 10^4). Frozen condensate (tau_dot = 0) satisfies trivially.

### 4.3 Oklo Reactor

delta-alpha_s < few % over 1.8 Gyr. Consistent with frozen modulus.

### 4.4 LLR

dG/dt/G < 10^{-12}/yr. G_4 = G_12/Vol(K). Volume is preserved by TT constraint (proven, Session 12). G_4 constant by construction.

### 4.5 Opposite-Drift Prediction

U(1) and SU(2) gauge couplings drift in opposite directions as tau changes, with ratio fixed by the Weinberg angle (from g_1/g_2 = e^{-2tau}). This discriminates Jensen TT-deformation from isotropic compactification, ADD, and Randall-Sundrum models. Detection of decorrelated coupling variation (delta-mu/mu != 0 with delta-alpha/alpha = 0, or vice versa) would be a distinctive signature.

Next-generation optical lattice clocks target 10^{-20}/yr sensitivity. The prediction requires the modulus not to be fully frozen. If frozen, both couplings are exactly constant. If the condensate oscillates around tau_0, the amplitude is constrained to < 25 ppm by the clock bound.

### 4.6 Gate Verdicts

| Gate | Condition | Result | Session |
|:-----|:----------|:-------|:--------|
| E-3 | dalpha/alpha = -3.08 * tau_dot | CLOSED (rolling, 15000x violation); Consistent (frozen) | 22d |

---

## 5. Large-Scale Structure and Cosmic Web

**Programs**: DESI, Euclid, SDSS/BOSS, Rubin/LSST, VIDE
**Source files**: Session 28 cosmic-web-collab; `researchers/Cosmic-Web/`; misc/giants-bao

### 5.1 BAO Scale

BAO standard ruler: ~150 Mpc comoving. The framework in frozen state (w = -1) reproduces LCDM expansion history and is structurally consistent with BAO measurements. Predicted transfer function T(k) must match to < 1% across ~2500 CMB multipoles.

### 5.2 P(k) Feature from BCS Transition

The van Hove singularity at the D_K band gap edge (KC-5 PASS: 43-51x enhancement, Session 28c) converts to a feature in P(k) at k_transition via the BCS condensation (Session 28 cosmic-web-collab). The feature shape (step or oscillation) depends on the order parameter and backreaction (Session 29 computation priority).

DESI sensitivity: sub-percent precision at k ~ 0.05-0.15 h/Mpc. Feature amplitude > 1% is detectable at > 3 sigma. Feature must not coincide with BAO wiggles (k_BAO ~ 0.04 h/Mpc).

Bogoliubov dispersion (BK18-E6, Session 29 plan item 29c-5) determines the sound speed c_s^{BCS} in the condensed phase. P(k) shape computation (29c-6) requires both the order parameter profile alpha(tau) and the nucleation rate beta/H.

### 5.3 Void Size Distribution

If condensate coherence length xi_heal falls in the range of observed void sizes, the void size distribution develops a secondary peak or shoulder at xi_heal. The VIDE pipeline (van de Weygaert formalism, Papers 03, 04, 12) applied to SDSS/DESI void catalogs is the appropriate test.

### 5.4 Topological Signatures

Betti numbers (beta_0, beta_1, beta_2) and persistent homology of the cosmic web at the predicted k_transition scale can distinguish the framework from LCDM N-body simulations. Applicable tools: persistent homology (Papers 03, 04), Minkowski functionals, genus statistics. Requires k_transition to be known.

### 5.5 Bulk Flows

Coherent bulk flow measurements at > 100 Mpc/h exceed LCDM expectations in some analyses. If substrate modes produce preferred scales with enhanced power, coherent motions at those scales follow. No quantitative prediction has been computed.

---

## 6. Gravitational Waves

**Programs**: LIGO/Virgo, LISA, NANOGrav/IPTA, Einstein Telescope, Cosmic Explorer
**Source files**: Sessions G1, G2, G3, 20b, 28; cosmic-web-collab

### 6.1 GW Speed

|c_GW - c|/c < 10^{-15} (GW170817 + GRB timing). TT modes of the external 4D metric propagate at c by construction. Constraint satisfied.

### 6.2 Dispersion

delta_v/c < 10^{-19} (LIGO). No dispersion detected. Consistent with emergent Lorentz invariance at low energy.

### 6.3 Stochastic GW Background from BCS Transition

L-9 (Session 28b): first-order BCS transition in (3,0)/(0,3) sectors (cubic invariants c = 0.0055, 0.0072). First-order transitions produce GWs from bubble-wall collisions.

Peak frequency:

    f_peak ~ (beta/H) * (T_*/100 GeV) * 1.65e-5 Hz

For KK-scale transition (T_* ~ 10^{14}-10^{16} GeV): f_peak ~ 10^7-10^9 Hz (above LISA/LIGO sensitivity).

Five cusps in d^3F/dtau^3 at sector boundaries (jumps 168k-452k, Session 28b) indicate a cascade of sector-by-sector transitions. If these occur at different cosmic times, the superposition produces a multi-peaked stochastic GW background. This signature is absent in LCDM, which predicts at most one cosmological phase transition GW signal.

If the BCS transition occurs at a later cosmological epoch (lower T_*), f_peak shifts into the LISA band (10^{-4}-10^{-1} Hz). This depends on the backreaction calculation (Session 29).

Gate P-29f: f_peak in LISA range + multi-peaked spectrum.

### 6.4 Ringdown Spectroscopy

The membrane paradigm gives eta/s = hbar/(4 pi k_B) (KSS bound). If spacetime is a fluid, excess dissipation in GW ringdown appears as corrections to quasinormal mode damping times. Target precision: 0.1-1% correction. Requires next-generation detectors (Einstein Telescope, Cosmic Explorer). Timeline: 10-20 years.

### 6.5 NANOGrav / PTA

QCD acoustic fossils at f ~ 10^{-8} Hz. SM crossover gives Omega_GW ~ 10^{-12}; BSM first-order transitions up to 10^{-9}. NANOGrav excess is power-law (consistent with SMBHBs). The framework's QCD-scale prediction is SM-like.

---

## 7. CMB Power Spectrum and Polarization

**Programs**: Planck, CMB-S4, BICEP/Keck, LiteBIRD, Simons Observatory
**Source files**: misc/giants-bao, misc/giants-planck-geometry, `researchers/Cosmic-Web/`

### 7.1 Power Spectrum Reproduction

CMB power spectrum (7 acoustic peaks) and BAO scale (150 Mpc) must be reproduced to < 1% precision. Frozen modulus (w = -1) is consistent with Planck parameters.

### 7.2 CMB Resonance Hypothesis

Alternative interpretation: CMB as primordial substrate resonance rather than thermal relic. Observational constraints:

| Constraint | Source | Requirement |
|:-----------|:-------|:------------|
| Blackbody spectrum | FIRAS | Planck distribution to 1/100,000 |
| T(z) scaling | Multi-z SZ | T(z) = T_0 * (1 + z) from substrate dynamics |
| SZ null at 217 GHz | Planck SZ | Compton scattering kinematics |
| E-mode polarization | Planck/WMAP | Recombination-epoch scattering |

No current mechanism addresses constraints (b)-(d). Status: OPEN challenge.

### 7.3 Damping Tail (CMB-S4)

If the substrate has a UV cutoff at k_substrate, the Silk damping tail is modified: exp(-(k/k_D)^2) * [1 + (k/k_substrate)^n * correction]. CMB-S4 measures damping tail to l ~ 5000. If k_substrate > 10 Mpc^{-1}, the substrate modification is undetectable. Status: speculative diagnostic.

### 7.4 Tensor-to-Scalar Ratio

BICEP/Keck: r < 0.036. CMB-S4 target: r ~ 0.001. The framework's initial Weyl curvature at tau = 0 is |C|^2 = 5/14 (topological obstruction, Session 20b). This potentially maps to a specific initial GW spectrum and hence a specific r value. Not yet computed.

### 7.5 N_eff at BBN

N_eff = 2.99 +/- 0.17 (measured). Extra dynamical dimensions at BBN produce extra energy density (higher N_eff). Constraint: segregation of internal geometry must be complete by t ~ 1 s. The ~35 decades between symmetry-breaking and BBN are sufficient. Status: constraint satisfied qualitatively.

---

## 8. Hubble Tension

**Programs**: SH0ES, Planck, DESI
**Source files**: Sessions 24b, 28; misc/giants-bao

### 8.1 Prediction Chain

```
tau_0 -> g_1/g_2 = e^{-2*tau_0} -> mass ratios -> CMB recombination surface -> H_0 (CMB)
```

SH0ES: H_0 = 73.0 +/- 1.0 km/s/Mpc. Planck: H_0 = 67.4 +/- 0.5 km/s/Mpc. If the prediction chain produces a natural ~5 km/s/Mpc divergence between early-universe and late-universe H_0, the framework makes a zero-parameter prediction of the tension.

The prediction chain requires tau_0. Status: OPEN conditional.

### 8.2 Alternative (CMB Resonance)

In the phononic interpretation (CMB as substrate resonance), early-universe and late-universe measurements probe different physics. This depends on the CMB resonance hypothesis, which faces independent observational constraints (Section 7.2).

---

## 9. Lorentz Violation and Planck-Scale Physics

**Programs**: Fermi LAT (GRB timing), LIGO (GW dispersion), cosmic ray detectors
**Source files**: Sessions 16, misc/giants-planck-geometry

### 9.1 Phonon vs. KK Distinction

Standard KK predicts exact Lorentz invariance at all energies. Phonon-exflation predicts emergent Lorentz invariance with Planck-scale breaking: Delta_v/c ~ (E/M_Pl)^n, where n is determined by internal geometry.

Fermi LAT: M_QG > 1.2 M_Pl at sigma = 1. For sigma = 2 (expected for phonon dispersion), current sensitivity is insufficient. The value of n has not been computed from the geometry.

### 9.2 GW Polarization

GR predicts 2 tensor polarizations. LIGO observes 2. The framework predicts exactly 2 at low energy (standard 4D GR recovery).

---

## 10. Colliders and Proton Decay

**Programs**: LHC/ATLAS/CMS, FCC-hh, Super-Kamiokande
**Source files**: misc/giants-planck-geometry, Session 16

### 10.1 LHC

No KK gravitons below ~15 TeV. No micro-BH. No supersymmetry. Consistent with KK compactification at SU(3) scale (far above LHC reach).

### 10.2 FCC-hh

If KK mass scale is accessible at 100 TeV: KK excitations predicted at M_KK = M_Pl / sqrt(Vol(K, g_{tau_0})). Requires tau_0. Timeline: 2035+.

### 10.3 Proton Decay

Super-Kamiokande: tau > 10^{34} yr (p -> e+ pi0). GUT-scale proton decay is not a prediction of this framework.

---

## 11. JWST and Early Universe Structure

**Programs**: JWST, HST
**Source files**: Sessions 23a, 24b, 28; `researchers/Little-Red-Dots/`

### 11.1 Early Galaxies

Galaxies at z > 10 with stellar masses ~10^9-10^10 M_sun challenge hierarchical structure formation timing. The framework's phononic structure formation is directionally consistent with early massive galaxies. No quantitative structure formation rate has been computed.

### 11.2 Little Red Dots

LRDs at z ~ 4-9: compact, overmassive AGN with number densities ~100x UV-selected quasars (24-paper corpus in `researchers/Little-Red-Dots/`). Two indirect connections:

1. LRD demographics constrain H(z) and rho(z) at z ~ 4. The frozen modulus (w = -1) predicts a specific H(z) that must be consistent.
2. LRD black hole masses (10^6-10^9 M_sun within 1 Gyr) constrain density contrast growth. No framework prediction for growth rate exists.

Status: indirect constraint.

---

## 12. Novel Predictions Beyond the Standard Model

Predictions qualifying as genuinely novel (Level 4: not contained in the Standard Model, pre-registered, measurable).

| Prediction | Condition | Instrument | Timeline | Gate Status |
|:-----------|:----------|:-----------|:---------|:------------|
| m_nu1 = 0 (massless lightest neutrino) | Pfaffian sign change at tau_c | KATRIN, Planck+DESI | 2025-2028 | Conditional (Pfaffian not computed; D_K Pfaffian = +1) |
| Normal mass ordering | tau_0 in [0.11, 1.58] | JUNO, DUNE | 2026-2030 | OPEN conditional on tau_0 |
| P(k) feature at k_transition | BCS backreaction computed | DESI, Euclid | After backreaction | OPEN conditional |
| Multi-peaked stochastic GW background | First-order BCS cascade (L-9) | LISA, Einstein Telescope | 10-20 yr | Speculative (f_peak likely above detector band) |
| Decorrelated coupling drift (U(1)/SU(2)) | Condensate oscillation around tau_0 | Optical lattice clocks 10^{-20}/yr | 2030s | OPEN (conflicts with frozen prediction if tau_dot = 0) |
| Hubble tension zero-parameter resolution | tau_0 fixed from dynamics | SH0ES + Planck | After tau_0 | OPEN conditional |
| Weinberg angle from dynamics | sin^2 theta_W = e^{-4tau_0}/(1 + e^{-4tau_0}) | Precision electroweak | After tau_0 | OPEN conditional (currently fitted, not derived) |
| Fine structure constant from geometry | beta/alpha = 0.28 from 12D | Precision QED | After beta/alpha | OPEN conditional (currently fitted) |

Consistency checks (not novel predictions):

| Result | Instrument | Status |
|:-------|:-----------|:-------|
| a_g = g exactly | ALPHA-g | PASS (consistency; follows from [J, D_K] = 0) |
| CPT equality nu = nu_bar | KamLAND, DUNE | PASS (algebraic theorem) |
| w = -1 (frozen modulus) | DESI | Marginal (BF = 0.5, 1.9 sigma from central value) |
| No 4th generation | IceCube, KATRIN | PASS (Z_3 grading) |
| G constant | LLR | PASS (volume-preserving TT) |
| c_GW = c | LIGO | PASS (construction) |
| No KK graviton leakage | SN1987A | PASS (SU(3) compactification) |
| LHC null results | LHC | PASS (null consistency) |

---

## Gate-to-Observable Cross-Reference

| Gate | Condition | Verdict | Session | Linked Observational Programs |
|:-----|:----------|:--------|:--------|:------------------------------|
| E-1 | w_0/w_a in DESI range (rolling) | CLOSED | 22d | DESI, Euclid, Roman |
| E-3 | dalpha/alpha = -3.08 * tau_dot | CLOSED (rolling) | 22d | Optical lattice clocks, quasar absorption, Oklo, LLR |
| V-1 | V_spec monotone (no Starobinsky) | CLOSED | 24a | -- (internal) |
| K-1e | BCS gap at mu = 0 | CLOSED (M_max = 0.077-0.149) | 23a | -- (internal) |
| R-1 | Neutrino R in [17, 66] | FAIL | 24a | KATRIN, JUNO, DUNE, Project 8 |
| D-1 | [J, D_K] = 0 (CPT) | PROVEN | 17a | ALPHA, BASE, KamLAND, DUNE |
| KC-1 | Parametric injection B_k(gap) | PASS (0.023) | 28a | -- (internal, feeds P(k) prediction) |
| KC-2 | Phonon scattering W/Gamma | PASS (0.52 at tau = 0.15) | 28c | -- (internal) |
| KC-3 | Steady-state mu_eff | PASS (n_gap = 37.3 at tau = 0.50) | 29Aa | -- (internal, feeds BCS transition epoch) |
| KC-4 | Attractive regime K < 1 | PASS (21/24 combinations) | 28c | -- (internal) |
| KC-5 | Van Hove BCS enhancement | PASS (43-51x, Delta/lambda_min = 0.84) | 28c | -- (internal, feeds P(k) feature amplitude) |
| K-29a | T-matrix at tau >= 0.50 | PASS (W/Gamma = 0.148) | 29Aa | -- (internal) |
| K-29b | Second law entropy | PASS (R_min = 1.53) | 29Aa | -- (internal) |
| G-29a | Drive rate natural | PASS (E_crit/V(0) = 1.52) | 29Aa | -- (internal) |
| G-29b | Inter-sector coupling | PASS (J_perp/Delta = 1.39) | 29Aa | -- (internal) |
| P-29f | GW multi-peaked spectrum | OPEN | 28/29 | LISA, Einstein Telescope |
| K-29e | BAO compatibility | OPEN | 29 (plan) | DESI, Euclid |
| Ordering | NO from bowtie | OPEN conditional | 22b | JUNO, DUNE, Super-K, Hyper-K |

---

## Quantitative Predictions Summary

### Computed (tau_0-independent)

| Quantity | Value | Source | Instrument |
|:---------|:------|:-------|:-----------|
| w (frozen modulus) | -1 exactly | E-3 closure, Session 22d | DESI |
| [J, D_K] | 0 (algebraic) | Session 17a | ALPHA, BASE |
| Number of generations | 3 (Z_3) | Session 7 | IceCube, KATRIN |
| G_4 drift | 0 (TT volume-preserving) | Session 12 | LLR |
| c_GW | c (4D GR recovery) | Construction | LIGO |
| J-even condensate | K-0 PASS | Session 23a | ALPHA-g |

### Awaiting tau_0

| Quantity | Expression | Source | Instrument |
|:---------|:-----------|:-------|:-----------|
| Neutrino mass ratios | D_K eigenvalue ratios at tau_0 | Session 16 pipeline | KATRIN, JUNO, DUNE |
| sin^2 theta_W | e^{-4tau_0}/(1 + e^{-4tau_0}) | Session 17a identity | Precision electroweak |
| H_0 (CMB) | tau_0 -> mass ratios -> recombination | Session 28 | SH0ES, Planck |
| KK excitation mass | lambda_next * M_scale | Session 22 | KATRIN-TRISTAN, FCC-hh |
| P(k) feature | k_transition = a(t_BCS) * H(t_BCS) | Session 28 cosmic-web-collab | DESI, Euclid |
| GW peak frequency | f_peak from backreaction | Session 28b (L-9) | LISA |

### Awaiting Further Computation

| Quantity | Prerequisite | Source |
|:---------|:-------------|:-------|
| Pfaffian sign (massless neutrino) | D_total Pfaffian computation | Session 16, 17c |
| delta_CP | Eigenspinor overlaps at tau_0 | Baptista Paper 18 |
| r (tensor-to-scalar) | Map |C|^2 = 5/14 to GW spectrum | Session 20b |
| n (LIV exponent) | Phonon dispersion from internal geometry | Session 16 |
| Void size distribution | xi_heal from BCS coherence length | Session 28 cosmic-web-collab |
