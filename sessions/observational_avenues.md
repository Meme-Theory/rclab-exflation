# Observational Avenues Reference -- Phonon-Exflation Framework

**Compiled**: 2026-04-04 (updated from S28 through S66)
**Scope**: `sessions/` (all subdirectories), `computations/` (.py, .txt, .npz), `researchers/` (.md), `tools/knowledge-index.json`
**Method**: Exhaustive cross-reference of instrument names, observable quantities, gate identifiers, and prediction keywords across all project files
**Major S29–S66 changes**: n_s recovery (S62), CC Volovik reframe (S66), Leggett DM candidate (S58/S66), r prediction (S63–S64), spectral functional crisis (S66), 17 permanent theorems (S63), 112+ proven mathematical results

---

## Master Table of Observational Programs

| Program | Type | Sessions | Observable | Framework Prediction | Gate Status |
|:--------|:-----|:---------|:-----------|:--------------------|:------------|
| DESI | Galaxy survey / BAO | 22d, 23c, 24a, 24b, 28, 29Aa, 63, 65, 66 | w_0, w_a; P(k) features | w_0 = −0.918 (GGE+Josephson); w_a ~ 0; Volovik w(z) tracking | TENSION (2.9σ DR2); DR3 pre-registered |
| Euclid | Galaxy survey / weak lensing | 22d, 28 | P(k), void statistics, sigma_8 | P(k) feature; void size distribution | OPEN conditional |
| SDSS / BOSS | Galaxy survey / BAO | misc/giants-bao | BAO standard ruler T(k) | T(k) reproduction to < 1% | Structural consistency |
| Planck | CMB satellite | 22d, 50, 58, 62, 66, many | n_s, sum m_nu, ΔN_eff, H_0, Ω_DM | n_s = 0.9567 (1.9σ); ΔN_eff = 0.027 (PASS); Ω_DM h² = 0.120 (0.7σ) | Multiple PASS; SCHEME-DEPENDENT (n_s) |
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
| CMB-S4 | CMB ground | G3, 63, 64, 65, 66 | r, α_s, f_NL, damping tail | r = 0.024–0.033 (burst); f_NL^{equil} ~ 1.12; α_s decisive | OPEN (testable 2028+) |
| BICEP / Keck | CMB B-mode | G2, 63, 64 | Tensor-to-scalar ratio r | r = 0.024–0.033 (second-order tensor, burst spectrum) | PASS (r < 0.036 current limit) |
| LiteBIRD | CMB satellite | 63, 64 | r measurement | r = 0.024–0.033; burst (Gaussian in ln k), not scale-invariant | OPEN (testable) |
| Simons Observatory | CMB ground | -- | CMB lensing, f_NL | f_NL^{equil} ~ 1.12 (from c_BLV = 0.485) | OPEN |
| Rubin / LSST | Optical survey | 28 | P(k), voids | Void size distribution | OPEN conditional |
| Roman (WFIRST) | Space telescope | 24b | Dark energy, deceleration | w_0 = −0.918; Volovik tracking | Speculative |
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
**Source files**: Sessions 22d, 23c, 24a, 24b, 28, 29Aa, 58, 63, 65, 66; `researchers/Cosmic-Web/17_2025_DESI_BAO_Cosmological_Constraints.md`

### 1.1 Equation of State Parameters

**S66 state**: The framework equation of state has evolved significantly since S28.

DESI DR2 central values (2026-02): w_0 = −0.752 ± 0.057, w_a = −0.73 ± 0.25.

**w_0**: The frozen modulus prediction (w = −1 exactly) is superseded. The combined GGE + Josephson contribution gives w_0 = −0.918 (S66). This lies 2.9σ from the DESI DR2 central value. The rolling quintessence branch (E-1, Session 22d) remains CLOSED by the clock constraint (15,000x violation, Section 4.1).

**w_a**: The framework predicts w_a ~ 0 (no CPL-parametrized evolution). DESI DR2 measures w_a = −0.73 ± 0.25, producing 2.9σ tension. However, CPL parametrization is structurally inadequate for the framework: the S66 CPL fit yields w_a = +1.121 (wrong sign), confirming that CPL cannot capture Volovik w(z) tracking dynamics. The proper comparison requires the Volovik tracking function w(z) = −1 + δw(H(z)/H_0), not CPL.

**Cosmological constant**: The CC problem is reframed by DILUTION-CC-66. Volovik Scenario B (q-theory relaxation: ρ_vac ~ M_Pl² H²) lands at ρ_vac(today)/ρ_obs = 1.032 — within 0.01 OOM of observation. The 114 OOM raw gap IS exflation itself (the expansion history), not a fine-tuning problem. Standard inflation carries an equivalent ~111 OOM gap. Conservative stackable corrections reach only 6.84 OOM (insufficient without Volovik relaxation). The a_0 topological obstruction (a_0 = 6440 is an integer mode count) remains the sole structural issue for the Volovik mechanism; the zeta action avoids it by excluding a_0 from the noncommutative integral.

**Pre-registered DESI DR3 decision rules (S63)**:
- If DR3 w_0 shifts toward −1.0 (within 1σ of framework): PASS — GGE+Josephson mechanism confirmed
- If DR3 w_a remains negative at > 3σ: framework must deliver Volovik w(z) tracking prediction or FAIL
- If DR3 w_0 shifts further from −1.0 (toward −0.7): 4σ+ tension — framework under severe pressure

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

### 1.4 σ_8 Tension

**S50 update**: σ_8 = 0.799 confirmed viable (S50, within 2σ of both Planck 0.811 ± 0.006 and lensing 0.777 ± 0.020). The Leggett DM candidate (Section 8a) reproduces the correct matter density, and σ_8 follows from standard structure growth with Ω_DM h² = 0.120. No anomalous growth rate is required. Euclid tomographic weak lensing (2027+) will test at 2.96σ discriminant reach.

### 1.5 Gate Verdicts

| Gate | Condition | Result | Session |
|:-----|:----------|:-------|:--------|
| E-1 (decisive) | w_0 in [-0.9, -0.75], w_a in [-0.8, -0.2] | CLOSED (rolling excluded) | 22d |
| E-1 (compelling) | w_0 in [-0.95, -0.65], w_a in [-1.2, -0.1] | CLOSED | 22d |
| E-1 (marginal) | w_0 = -1 | Superseded by w_0 = −0.918 (GGE+Josephson) | 22d→66 |
| DILUTION-CC-66 | Volovik Scenario B: ρ_vac/ρ_obs ~ 1 | PASS (1.032, 0.01 OOM) | 66 |
| QTHEORY-NPAIR-66 | Discrete q-theory self-tuning | FAIL (min|P_vac| = 2.34e-7 M_Pl⁴, 113.5 OOM) | 66 |
| P(k) feature | Sub-percent feature in DESI/Euclid range | OPEN conditional | 28/29 |
| P-29f | f_peak in LISA range + multi-peaked GW | OPEN | 28/29 |
| K-29e | delta(r_s)/r_s < 0.5% if t_BCS in recombination window | OPEN | 29 (plan) |
| DR3 decision | Pre-registered w_0/w_a decision rules | OPEN (awaiting DR3 2026–2027) | 63 |

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

If the Pfaffian of D_total changes sign at some tau_c, topological protection produces a massless or near-massless fermion. The D_K Pfaffian is trivially +1 (Session 17c, D-2). The D_total Pfaffian has not been computed (Level C computation, prerequisites ~3 weeks as of Session 16).

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

### 2.10 ΔN_eff

**S66 update**: The framework predicts ΔN_eff = 0.027 from GGE relic quasiparticles (Leggett channel excitations contributing subdominant radiation density). Observed: ΔN_eff = 0.15 ± 0.23 (Planck). Tension: 0.5σ. Verdict: PASS. This is FUNCTIONAL-INDEPENDENT (holds across all cutoff families).

### 2.11 Gate Verdicts

| Gate | Condition | Result | Session |
|:-----|:----------|:-------|:--------|
| R-1 | R = (m3^2 - m2^2)/(m2^2 - m1^2) in [17, 66] | FAIL (R ~ 10^{14} Kramers; K_a cross-check R = 5.68) | 24a |
| D-1 | [J, D_K] = 0 | PROVEN | 17a |
| Ordering (structural) | NO from bowtie for tau_0 in [0.11, 1.58] | OPEN conditional (JUNO) | 22b |
| ΔN_eff | 0.027 vs 0.15 ± 0.23 | PASS (0.5σ) | 66 |

**Note on R-1**: R-1 remains a FAIL, but the framework makes a structural normal ordering prediction from the bowtie eigenvalue topology that is independent of the mass ratio computation. The Kramers degeneracy that produces R ~ 10^{14} may be an artifact of the degenerate perturbation treatment (K_a cross-check gives R = 5.68, still outside [17, 66]).

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

**S66 status**: Unchanged. Rolling CLOSED at 15,000x. The clock constraint is now part of the Permanent Results Registry (Clock constraint, proven).

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

BAO standard ruler: ~150 Mpc comoving. The framework with w_0 = −0.918 (GGE+Josephson, S66) is structurally consistent with BAO measurements. Predicted transfer function T(k) must match to < 1% across ~2500 CMB multipoles.

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
**Source files**: misc/giants-bao, misc/giants-planck-geometry, `researchers/Cosmic-Web/`; Sessions 50, 57, 62, 63, 64, 65, 66

### 7.1 Power Spectrum Reproduction

CMB power spectrum (7 acoustic peaks) and BAO scale (150 Mpc) must be reproduced to < 1% precision. The framework with w_0 = −0.918 is consistent with Planck parameters at the background level. The spectral tilt n_s is now a computed prediction (Section 7.2).

### 7.2 Spectral Tilt n_s (S62 Recovery)

**S62 breakthrough**: n_s = 0.9567 from the Hubble spectral action (SA) route, with zero free geometric parameters. Observed: n_s = 0.9649 ± 0.0042 (Planck). Tension: 1.9σ. Verdict: CONDITIONAL PASS.

Alternative route: BCS + Coleman-Weinberg corrections give n_s = 0.9595 (1.3σ, INFO).

**SCHEME-DEPENDENT (S66)**: The Hubble slow-roll parameter ε_H changes SIGN between cutoff families:
- sqrt(x) cutoff: ε_H = +0.02163 → n_s = 0.9567 (red tilt, Planck-compatible)
- Zeta / exponential cutoff: ε_H < 0 → n_s > 1 (blue tilt, excluded)
- n_s spread across functionals: 0.164 (39× Planck error bar)

The spectral functional crisis (Section 7.2a below) must be resolved before n_s is a genuine prediction.

**Structural result**: The mode-independent occupation theorem (S57/S62) proves n_s is independent of Bogoliubov |β|². The tilt comes from spectral geometry only — not from occupation numbers.

**Gauge invariance**: T7 (S63) proves ε_BLV = 2 − 1/ε_SA exactly. The BLV and SA formulations give identical n_s. This is structural.

#### 7.2a Spectral Functional Crisis

The spectral action depends on the cutoff function f(x). Different choices yield different ε_H at the sign level. Resolution path: the anomaly + conservation hierarchy constrains f to a one-parameter dilaton family c_k(φ) = (−1)^k φ^k/k. Bayesian evidence collapses model space: exp(−x) excluded at 15.5σ, compact at 36.9σ. Only sqrt(x) and anomaly(φ) survive. The Higgs mass discriminant breaks the residual degeneracy: m_H^{zeta} ~ 174 GeV vs m_H^{cutoff} ~ 127.5 GeV. Observation at 125.1 GeV selects the cutoff family at percent level. FUNCTIONAL-SELECT-67 is a CRITICAL S67 gate.

### 7.3 Running of the Spectral Index α_s

**S66 state**: α_s = −0.038 at 5.0σ FAIL from Planck (observed: −0.0045 ± 0.0067). The slow-roll formula is suspect at Mach 13.8 (deeply supersonic transit). The structural identity α_s = n_s² − 1 (T15, S50, five proofs) holds for any K² propagator on a compact Josephson lattice, but applies to the spectral action running, not the CMB observable directly.

Two resolution paths:
- **ATDHFB calibration** (nuclear fission analog): factor 2–5× reduction, saturates at deeply diabatic limit. Pre-registered range: [−0.019, −0.008].
- **Acoustic prediction** (QA, S66): α_s(CMB) ~ 0 from 56 OOM scale hierarchy between fold and CMB (sinc² spectral envelope). The acoustic power spectrum at CMB scales is dominated by the envelope of the GGE relic, not the local fold curvature.

**TRANSIT-PS-67 is the decisive gate**: must deliver α_s as a function of k. If |α_s(k_CMB)| < 0.015: PASS. If > 0.019: FAIL.

### 7.4 CMB Resonance Hypothesis

Alternative interpretation: CMB as primordial substrate resonance rather than thermal relic. Observational constraints:

| Constraint | Source | Requirement |
|:-----------|:-------|:------------|
| Blackbody spectrum | FIRAS | Planck distribution to 1/100,000 |
| T(z) scaling | Multi-z SZ | T(z) = T_0 * (1 + z) from substrate dynamics |
| SZ null at 217 GHz | Planck SZ | Compton scattering kinematics |
| E-mode polarization | Planck/WMAP | Recombination-epoch scattering |

No current mechanism addresses constraints (b)-(d). Status: OPEN challenge.

### 7.5 Damping Tail (CMB-S4)

If the substrate has a UV cutoff at k_substrate, the Silk damping tail is modified: exp(-(k/k_D)^2) * [1 + (k/k_substrate)^n * correction]. CMB-S4 measures damping tail to l ~ 5000. If k_substrate > 10 Mpc^{-1}, the substrate modification is undetectable. Status: speculative diagnostic.

### 7.6 Tensor-to-Scalar Ratio r (S63–S64)

**S63–S64 breakthrough**: r = 0.024–0.033 from second-order tensor production. First-order tensor production is killed by the H2 theorem (T1–T3, S63; H2, S64): five independent proofs establish that homogeneous transit on M⁴ × K produces π_{ij} = 0 at linear order. Volume-preserving (traceless transverse) deformation cannot source first-order gravitational waves.

**The tensor spectrum is a BURST** (Gaussian in ln k), not scale-invariant. This is a distinctive signature: no single-field slow-roll model produces a burst tensor spectrum. The burst shape follows from the impulsive (Mach 13.8) transit through the van Hove fold.

r depends on exactly 3 numbers (Exflation Tensor Theorem T4, S63): ε(0.0216), c_s(0.485), N_e. This is FUNCTIONAL-INDEPENDENT — holds across all cutoff families.

Current observational status: BICEP/Keck r < 0.036. The framework prediction r = 0.024–0.033 is consistent with the current upper bound and testable by CMB-S4 (σ_r ~ 0.001, 2028+) and LiteBIRD (σ_r ~ 0.002).

### 7.7 Non-Gaussianity f_NL (S65–S66)

**S66 predictions**:

| Type | Value | Source | Status |
|:-----|:------|:-------|:-------|
| f_NL^{equilateral} | ~1.12 | c_BLV = 0.485 (subluminal fabric sound speed) | CMB-S4 testable |
| f_NL^{GGE diagonal} | ~0.13 | Diagonal GGE state occupation | Prediction |
| f_NL shape | Folded triangles (k_1 + k_2 = k_3) | Unique to GGE (no single-field model produces it) | Novel signature |

Current Planck bound: f_NL^{equil} = −26 ± 47. The prediction at ~1.12 is consistent. CMB-S4 sensitivity (σ ~ 5) will probe this at ~0.2σ per measurement, but the distinctive folded triangle shape provides a qualitative discriminant.

The Bogoliubov gaussianity preservation theorem (S65) proves f_NL = O(ε) regardless of squeezing, confirming the small amplitude prediction structurally.

GGE-BISPECTRUM-67 is the S67 computation that will sharpen the f_NL prediction from the in-in formalism on the GGE relic.

### 7.8 ΔN_eff

**S66**: ΔN_eff = 0.027 from Leggett-channel GGE quasiparticles. Observed: 0.15 ± 0.23. Tension: 0.5σ. PASS. FUNCTIONAL-INDEPENDENT.

N_eff = 2.99 ± 0.17 (measured). The ~35 decades between symmetry-breaking and BBN ensure segregation of internal geometry is complete by t ~ 1 s. Status: constraint satisfied both qualitatively and quantitatively.

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

## 8a. Dark Matter (S58/S66 — New Section)

**Programs**: Planck (Ω_DM h²), Euclid (lensing), LUX-ZEPLIN/XENONnT (direct detection), Fermi-LAT (annihilation), DESI (z_eq)
**Source files**: Sessions 42–44, 50, 57, 58, 66

### 8a.1 Leggett-Channel GGE Quasiparticle (S58/S66)

The framework dark matter candidate is the Leggett-channel GGE quasiparticle — an inter-band coherence mode of the post-transit Generalized Gibbs Ensemble relic. This is NOT a new particle added to the model. It is a necessary consequence of the supersonic transit through the van Hove fold: any first-order transition on the SU(3) fiber produces 59.8 quasiparticle pairs (P_exc = 1.000, deeply diabatic), and the Leggett channel carries the inter-band component.

Key properties:
- **CPT-neutral** (J-even, follows from [J, D_K] = 0)
- **Non-annihilating** (GGE diagonal ensemble; off-diagonal coherences dephase, diagonal occupations are conserved)
- **Collisionless** (σ/m = 0: no point-particle scattering vertex exists)
- **λ_fs = 9.85 × 10⁻²³ Mpc** (free-streaming length, 22 OOM below WDM bound of 0.1 Mpc — CDM-like)

### 8a.2 Observational Predictions

| Observable | Framework | Observed | Tension | Verdict |
|:-----------|:----------|:---------|:--------|:--------|
| Ω_DM h² | 0.120 (Leggett-only) | 0.1186 ± 0.0020 | 0.7σ | PASS |
| z_eq | 3425 | 3402 ± 26 | 0.88σ | PASS |
| σ/m | 0 | < 1.25 cm²/g | — | PASS |
| Direct detection cross-section | 0 | null (LZ, XENONnT) | — | PASS |
| Annihilation cross-section | 0 | null (Fermi-LAT) | — | PASS |
| λ_fs | 9.85e-23 Mpc | < 0.1 Mpc (Lyman-α) | 22 OOM safe | PASS |

The Ω_DM h² = 0.120 result is FUNCTIONAL-INDEPENDENT (holds across all cutoff families). The Volovik partition (S58) cleanly separates F_Josephson = −336.6 M_KK (95.9% → vacuum) from F_BCS + F_BA + F_Leggett = 14.411 M_KK (→ matter).

### 8a.3 Critical Open: LEGGETT-GRAV-DECAY-67

**CRITICAL S67 gate**: The gravitational decay channel Γ_grav(4D) ~ 1.4 × 10⁻¹³ GeV (29 OOM above H_0). If no selection rule forbids this decay, the Leggett quasiparticle is unstable on cosmological timescales and the DM sector collapses entirely (Ω_DM h² = 0.120 becomes meaningless).

Gate condition: PASS if Γ_grav < H_0; FAIL if Γ_grav > H_0. A symmetry-based selection rule (e.g., from GGE integrability or Leggett mode quantum numbers) could forbid the decay. This computation is the single highest-stakes gate for the DM sector.

### 8a.4 What This Is NOT

- NOT a WIMP (no electroweak coupling, no annihilation, direct detection is exactly zero)
- NOT an axion (no U(1)_PQ, no θ-vacuum)
- NOT a sterile neutrino (not a fermion mass eigenstate)
- NOT warm DM (λ_fs is 22 OOM below the warm threshold)
- IS a collective mode of the substrate's post-transit state — CDM-like phenomenologically, substrate-native ontologically

### 8a.5 Gate Verdicts

| Gate | Condition | Result | Session |
|:-----|:----------|:-------|:--------|
| Ω_DM (Leggett) | h² = 0.120 vs 0.1186 ± 0.0020 | PASS (0.7σ) | 58/66 |
| z_eq (Leggett) | 3425 vs 3402 ± 26 | PASS (0.88σ) | 66 |
| σ/m | 0 vs < 1.25 cm²/g | PASS | 58 |
| LEGGETT-GRAV-DECAY-67 | Γ_grav < H_0 | OPEN (CRITICAL) | 67 (planned) |

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

**S62–S66 particle physics predictions**:

| Observable | Framework | Observed | Tension | Verdict | Session |
|:-----------|:----------|:---------|:--------|:--------|:--------|
| m_H (Gaussian, L=6) | 131.8 GeV | 125.1 GeV | 5.4% | CONDITIONAL PASS | 62 |
| m_H (Aitken extrapolation) | 127.5 GeV | 125.1 GeV | 1.9% | CONVERGING | 66 |
| sin²θ_W | 0.2307 | 0.2312 | 0.2% | PASS | 62 |
| M_W | 80.41 GeV | 80.38 GeV | 0.05% | PASS | 62 |
| Yukawa rank | 2 | 3 | rank deficient | OPEN | — |

m_H is filter-independent across all 6 cutoff families at tree level (134 GeV, Filter-Independence Theorem S62). KK threshold corrections bring it to 131.8 GeV (Gaussian L=6). The Aitken extrapolation to L→∞ gives 127.5 GeV (1.9% from observation). The m_H discriminant selects the cutoff family: m_H^{zeta} ~ 174 GeV vs m_H^{cutoff} ~ 127.5 GeV, with observation at 125.1 GeV selecting cutoff at percent level.

### 10.2 FCC-hh

If KK mass scale is accessible at 100 TeV: KK excitations predicted at M_KK = M_Pl / sqrt(Vol(K, g_{tau_0})). Requires tau_0. Timeline: 2035+.

### 10.3 Proton Decay

Super-Kamiokande: τ > 10³⁴ yr (p → e⁺ π⁰). **S63 update**: τ_p = 6.26 × 10³⁹ yr (T17, S63). Tree-level proton decay is exactly zero by Peter-Weyl orthogonality on SU(3). The computed lifetime (from loop-level processes) exceeds the current bound by 5 orders of magnitude. PASS with large margin. Hyper-K (2028+) will improve the bound to ~10³⁵ yr, still 4 OOM below the prediction.

---

## 11. JWST and Early Universe Structure

**Programs**: JWST, HST
**Source files**: Sessions 23a, 24b, 28; `researchers/Little-Red-Dots/`

### 11.1 Early Galaxies

Galaxies at z > 10 with stellar masses ~10^9-10^10 M_sun challenge hierarchical structure formation timing. The framework's phononic structure formation is directionally consistent with early massive galaxies. No quantitative structure formation rate has been computed.

### 11.2 Little Red Dots

LRDs at z ~ 4-9: compact, overmassive AGN with number densities ~100x UV-selected quasars (24-paper corpus in `researchers/Little-Red-Dots/`). Two indirect connections:

1. LRD demographics constrain H(z) and rho(z) at z ~ 4. The framework with w_0 = −0.918 predicts a specific H(z) that must be consistent.
2. LRD black hole masses (10^6-10^9 M_sun within 1 Gyr) constrain density contrast growth. No framework prediction for growth rate exists.

Status: indirect constraint.

---

## 12. Novel Predictions Beyond the Standard Model

Predictions qualifying as genuinely novel (Level 4: not contained in the Standard Model, pre-registered, measurable).

| Prediction | Condition | Instrument | Timeline | Gate Status |
|:-----------|:----------|:-----------|:---------|:------------|
| r = 0.024–0.033 (burst tensor spectrum) | Structural (T4, 3 numbers: ε, c_s, N_e) | CMB-S4, LiteBIRD, BICEP | 2028+ | PASS (r < 0.036 current); testable at σ_r ~ 0.001 |
| f_NL^{equil} ~ 1.12 | c_BLV = 0.485 | CMB-S4 | 2028+ | CONSISTENT (Planck: −26 ± 47) |
| GGE folded bispectrum shape (k_1+k_2=k_3) | GGE diagonal relic | CMB-S4 | 2028+ | Novel (no single-field model produces this) |
| Volovik w(z) tracking (ρ_vac ~ H² M_Pl²) | Scenario B PASS | DESI DR3 | 2026–2027 | Pre-registered decision rules (S63) |
| Ω_DM h² = 0.120 (Leggett quasiparticle) | LEGGETT-GRAV-DECAY-67 PASS needed | Planck | — | PASS (0.7σ); stability gate OPEN |
| τ_p = 6.26 × 10³⁹ yr | PW orthogonality (T17) | Hyper-K | 2028+ | PASS (5 OOM margin) |
| m_H = 127.5 GeV (Aitken extrap.) | Filter-independence theorem | LHC | — | 1.9% from observation |
| n_s = 0.9567 (Hubble SA) | FUNCTIONAL-SELECT-67 | Planck | — | CONDITIONAL PASS (1.9σ, scheme-dependent) |
| ΔN_eff = 0.027 | GGE relic | Planck, CMB-S4 | — | PASS (0.5σ) |
| m_nu1 = 0 (massless lightest neutrino) | Pfaffian sign change at tau_c | KATRIN, Planck+DESI | 2025-2028 | Conditional (Pfaffian not computed; D_K Pfaffian = +1) |
| Normal mass ordering | tau_0 in [0.11, 1.58] | JUNO, DUNE | 2026-2030 | OPEN conditional on tau_0 |
| P(k) feature at k_transition | BCS backreaction computed | DESI, Euclid | After backreaction | OPEN conditional |
| Multi-peaked stochastic GW background | First-order BCS cascade (L-9) | LISA, Einstein Telescope | 10-20 yr | Speculative (f_peak likely above detector band) |
| Decorrelated coupling drift (U(1)/SU(2)) | Condensate oscillation around tau_0 | Optical lattice clocks 10^{-20}/yr | 2030s | OPEN (conflicts with frozen prediction if tau_dot = 0) |
| Hubble tension zero-parameter resolution | tau_0 fixed from dynamics | SH0ES + Planck | After tau_0 | OPEN conditional |
| Weinberg angle from dynamics | sin²θ_W = e^{-4τ_0}/(1 + e^{-4τ_0}) | Precision electroweak | After tau_0 | OPEN conditional (currently fitted, not derived) |
| Fine structure constant from geometry | beta/alpha = 0.28 from 12D | Precision QED | After beta/alpha | OPEN conditional (currently fitted) |

Consistency checks (not novel predictions):

| Result | Instrument | Status |
|:-------|:-----------|:-------|
| a_g = g exactly | ALPHA-g | PASS (consistency; follows from [J, D_K] = 0) |
| CPT equality nu = nu_bar | KamLAND, DUNE | PASS (algebraic theorem) |
| sin²θ_W = 0.2307 | Precision electroweak | PASS (0.2% from obs) |
| M_W = 80.41 GeV | LHC/LEP | PASS (0.05% from obs) |
| σ_8 = 0.799 | Euclid, DES | PASS (within 2σ of both Planck and lensing) |
| z_eq = 3425 (Leggett) | Planck/DESI | PASS (0.88σ) |
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
| KZ-NS-62 | n_s = 0.9567 (1.9σ) | CONDITIONAL PASS (scheme-dependent) | 62 | Planck, CMB-S4 |
| DILUTION-CC-66 | Volovik Scenario B ρ_vac/ρ_obs = 1.032 | PASS (0.01 OOM) | 66 | DESI DR3, Euclid |
| TENSOR-BURST-64 | r = 0.024–0.033 (second-order, burst) | PASS (r < 0.036) | 63–64 | BICEP/Keck, CMB-S4, LiteBIRD |
| ZETA-SA-66 | ε_H sign reversal between cutoffs | INFO (spectral functional crisis) | 66 | Planck (n_s), CMB-S4 (α_s) |
| AMPLITUDE-NORM-66 | A_s gap 3.15 OOM (Route B) | FAIL (marginal) | 66 | Planck (A_s normalization) |
| QTHEORY-NPAIR-66 | Discrete q-theory self-tuning | FAIL (113.5 OOM) | 66 | -- (internal CC mechanism) |
| LEGGETT-GRAV-DECAY-67 | Γ_grav < H_0 | OPEN (CRITICAL) | 67 (planned) | Planck (Ω_DM), Euclid, direct detection |
| TRANSIT-PS-67 | α_s(k_CMB) < 0.015 | OPEN (CRITICAL) | 67 (planned) | CMB-S4 (α_s), Planck (n_s) |
| FUNCTIONAL-SELECT-67 | Unique φ: n_s ∩ m_H | OPEN (CRITICAL) | 67 (planned) | Planck (n_s), LHC (m_H) |
| BBN-VOLOVIK-67 | |w_vac − 1/3| < 0.03 at T_BBN | OPEN (CRITICAL) | 67 (planned) | BBN abundances |

---

## Quantitative Predictions Summary

### Computed (tau_0-independent, S66 state)

| Quantity | Value | Source | Instrument |
|:---------|:------|:-------|:-----------|
| n_s (Hubble SA) | 0.9567 | S62, KZ-NS-62 | Planck (1.9σ, scheme-dependent) |
| r (second-order tensor) | 0.024–0.033 | S63–S64, TENSOR-BURST-64 | BICEP/Keck, CMB-S4 |
| ΔN_eff | 0.027 | S66 | Planck (0.5σ PASS) |
| f_NL^{equil} | ~1.12 | S65–S66, c_BLV = 0.485 | CMB-S4 |
| Ω_DM h² (Leggett) | 0.120 | S58/S66 | Planck (0.7σ PASS) |
| z_eq (Leggett) | 3425 | S66 | Planck (0.88σ PASS) |
| w_0 (GGE+Josephson) | −0.918 | S66 | DESI (2.9σ tension) |
| CC (Volovik Scenario B) | ρ_obs × 1.032 | S66, DILUTION-CC-66 | 0.01 OOM PASS |
| m_H (Aitken extrap.) | 127.5 GeV | S66 | LHC (1.9%) |
| sin²θ_W | 0.2307 | S62 | 0.2% PASS |
| M_W | 80.41 GeV | S62 | 0.05% PASS |
| τ_p | 6.26 × 10³⁹ yr | S63, T17 | 5 OOM margin |
| σ_8 | 0.799 | S50 | Within 2σ of both |
| [J, D_K] | 0 (algebraic) | Session 17a | ALPHA, BASE |
| Number of generations | 3 (Z_3) | Session 7 | IceCube, KATRIN |
| G_4 drift | 0 (TT volume-preserving) | Session 12 | LLR |
| c_GW | c (4D GR recovery) | Construction | LIGO |
| J-even condensate | K-0 PASS | Session 23a | ALPHA-g |

### Awaiting tau_0

| Quantity | Expression | Source | Instrument |
|:---------|:-----------|:-------|:-----------|
| Neutrino mass ratios | D_K eigenvalue ratios at tau_0 | Session 16 pipeline | KATRIN, JUNO, DUNE |
| sin²θ_W (derived) | e^{-4τ_0}/(1 + e^{-4τ_0}) | Session 17a identity | Precision electroweak |
| H_0 (CMB) | tau_0 → mass ratios → recombination | Session 28 | SH0ES, Planck |
| KK excitation mass | lambda_next * M_scale | Session 22 | KATRIN-TRISTAN, FCC-hh |
| P(k) feature | k_transition = a(t_BCS) * H(t_BCS) | Session 28 cosmic-web-collab | DESI, Euclid |
| GW peak frequency | f_peak from backreaction | Session 28b (L-9) | LISA |

### Awaiting S67 Computations

| Quantity | Prerequisite | Source |
|:---------|:-------------|:-------|
| α_s(k_CMB) | TRANSIT-PS-67 (full Bogoliubov power spectrum) | S66 |
| A_s (amplitude normalization) | TRANSIT-PS-67 (occupied-state, not vacuum) | S66 |
| Leggett DM stability | LEGGETT-GRAV-DECAY-67 (selection rule) | S66 |
| Spectral functional selection | FUNCTIONAL-SELECT-67 (dilaton φ) | S66 |
| BBN Volovik tracking | BBN-VOLOVIK-67 (w_vac at T_BBN) | S66 |
| GGE bispectrum shape | GGE-BISPECTRUM-67 (in-in formalism) | S66 |

### Awaiting Further Computation

| Quantity | Prerequisite | Source |
|:---------|:-------------|:-------|
| Pfaffian sign (massless neutrino) | D_total Pfaffian computation | Session 16, 17c |
| delta_CP | Eigenspinor overlaps at tau_0 | Baptista Paper 18 |
| n (LIV exponent) | Phonon dispersion from internal geometry | Session 16 |
| Void size distribution | xi_heal from BCS coherence length | Session 28 cosmic-web-collab |
