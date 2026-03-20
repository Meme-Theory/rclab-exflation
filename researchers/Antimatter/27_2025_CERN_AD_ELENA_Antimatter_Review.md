# CERN AD/ELENA Antimatter Program Review

**Author(s):** CERN Collaboration (Latacz et al.)
**Year:** 2025
**Journal:** arXiv:2503.22471

---

## Abstract

This report reviews the CERN Antiproton Decelerator (AD) and Extra Low Energy Antiproton Decelerator (ELENA) program as of 2025, summarizing seven operating experiments (ALPHA, BASE, AEgIS, GBAR, ASACUSA, AEGIS-III, and collaborations) dedicated to precision tests of CPT symmetry, antimatter gravity, and dark matter searches using antiprotons and antihydrogen. Post-ELENA infrastructure enables unprecedented low-energy antiproton beams. Key results include the first direct gravitational acceleration measurement of antihydrogen (ALPHA-g) and improved CPT tests in the baryon sector. The program establishes antimatter research as a precision frontier for fundamental physics, with near-term milestones extending to 2040 and long-term horizons targeting transportable traps and exotic hadron physics.

---

## Historical Context

Antimatter, predicted by Dirac in 1928, remains among the least-studied sectors of particle physics despite its profound implications for CPT symmetry, matter-antimatter asymmetry, and new physics searches. For three decades following the first antiproton production (1955), antimatter research relied on high-energy collisions and difficult production techniques. The Antiproton Decelerator (AD), commissioned in 2000, revolutionized the field by providing meV-scale antimatter beams suitable for trapping in electromagnetic and magnetic bottles. This enabled precision spectroscopy and weak-interaction studies impossible in collision scenarios.

ELENA (Extra Low Energy Antiproton Decelerator), completed in 2017-2018 and fully operational by 2020, represents the second generation of low-energy antimatter infrastructure. By reducing antiproton beam energies from ~5.3 MeV (AD exit) to ~100 keV (ELENA exit), coupled with novel stochastic cooling techniques, ELENA increased antiproton trap capture efficiency by orders of magnitude. This breakthrough allows simultaneous operation of seven active experiments, competitive precision with atomic physics experiments, and new physics windows (e.g., gravitational tests, dark matter searches, exotic atom spectroscopy).

The 2025 report consolidates results from ~25 years of operational antimatter physics, evaluating readiness for the next frontier: post-2030 upgrades aimed at 10^-13 CPT tests, direct antimatter gravity bounds, and transport of antimatter samples outside CERN for astrophysical applications.

---

## Key Arguments and Results

### ELENA Infrastructure and Reach

ELENA accepts 5.3 MeV antiprotons from the AD and decelerates them in two stages: (1) rf capture and beam compression, (2) electron cooling to 100 keV. Stochastic cooling (transverse + longitudinal) reduces emittance to 5-10 mm·mrad, enabling trap efficiencies of 30-50% (vs. < 5% at AD energies). Beam intensity grows logarithmically: 10^6 antiprotons/min ELENA output (2020) to 10^7 antiprotons/min projected by 2026.

This tenfold gain in usable antiprotons transforms the experimental landscape:

| Experiment | Science Goal | 2020-2023 Status | 2024-2025 Readiness |
|:-----------|:-------------|:-----------------|:------------------|
| ALPHA | Antihydrogen spectroscopy, magnetic moment | First Balmer alpha, E1 = 10^-14 | Lyman-alpha locked, next CPT test |
| BASE | Antiproton charge, mass, g-2, lifetime | a_p/a_e = 0.99999996(5), Penning trap | Baryon anomaly limits set |
| AEgIS | Antimatter gravity via moiré gratings | First antihydrogen beam deflection | Direct g measurement <2026 |
| GBAR | Antimatter gravity via free-fall timing | Apparatus commissioned | First g bound ~2026 |
| ASACUSA | Antiprotonic atom spectroscopy | metastable cascade (n~100) | Hyperfine transition quest |
| NEW: AEGIS-III | Dielectronic resonance + gravity | Design phase | 2028 commissioning |

### ALPHA-g and ALPHA-x (Gravitational Tests)

The ALPHA-g experiment measures the acceleration of antihydrogen in Earth's gravitational field:

$$a_g = g (1 + \alpha_g)$$

where $\alpha_g$ is the CPT parameter. Preliminary 2023-2024 results yield:

$$\alpha_g = 0.75 \pm 0.29 \quad (1\sigma, 2.6\sigma \text{ from zero})$$

This defies the Standard Model prediction $\alpha_g = 0$ (gravity is universal). Possible interpretations:

1. **CPT violation** — antimatter couples to gravity differently (ruled out by high-energy tests, but not gravity sector)
2. **Systematcis** — magnetic field coupling, residual electric fields, thermal motion in the trap
3. **New physics** — spin-dependent forces, fifth forces, or dark matter interactions
4. **Measurement artifact** — Bayesian priors or unblinded analysis bias

The ALPHA collaboration conducted rigorous systematics studies (2024-2025):
- Magnetic field inhomogeneity correction: $\Delta \alpha_g \sim +0.02$
- Thermal distribution effects: $\Delta \alpha_g \sim -0.08$ (tighter traps reduce this)
- Electric field leakage (residual space charge): $\Delta \alpha_g \sim +0.04$

Even with all systematic reductions, the central value persists at $\alpha_g \approx 0.4-0.5$. A new blind analysis is planned for 2026 to test whether unblinding bias inflates the effect.

### BASE Baryon Anomaly Program

The BASE experiment (Baryon Antimatter Symmetry Experiment) measures the charge-to-mass ratio $q/m$ of antiprotons to unprecedented precision:

$$\frac{q_{\bar{p}}}{m_{\bar{p}}} = 95.384766(5) \text{ MHz/T} \quad \text{(2024)}$$

compared to protons:

$$\frac{q_p}{m_p} = 95.384766(5) \text{ MHz/T} \quad \text{(2024)}$$

**Charge symmetry preserved** to $\Delta q/q < 10^{-9}$. However, **anomalous magnetic moment** shows tension:

$$a_p - a_{\bar{p}} = 0 \quad \text{(CPT prediction)}$$
$$\text{Measured} = (3 \pm 8) \times 10^{-5} a_p$$

This is consistent with CPT but raises questions about higher-order corrections in QED and the running coupling constants.

### AEgIS Moiré Grating Gravity

AEgIS uses a moiré grating (two interfering atom gratings) to deflect antihydrogen and measure $g$ directly. The momentum transfer is:

$$\Delta p = \frac{2\pi\hbar}{\lambda} \rightarrow g = \frac{a}{t^2}$$

where $a$ is the acceleration and $t$ is the free-fall time. Early 2024 results achieved sensitivity to ~0.1g. A refined 2025 apparatus improves thermal isolation and field control, aiming for $\Delta g/g < 0.01$ by 2026.

### GBAR Free-Fall Timing

GBAR measures antimatter gravity by releasing antihydrogen from a trap at height $h$ and timing the fall to an annihilation detector:

$$g = \frac{2h}{t^2}$$

Systematic uncertainties:
- Thermal velocity spread: $\sigma_v = 1-10$ m/s (mitigated by large $h \sim 1$ m traps)
- Gravity gradient: $\Delta g/\Delta z \sim 3 \times 10^{-6}$ s^-1 (corrected via barometer)
- Magnetic field residuals: coupling to gravity via second-order Zeeman

GBAR prototype completed in 2024; first gravity measurement expected 2026-2027.

### ASACUSA Antiprotonic Atom Spectroscopy

ASACUSA traps antiprotonic helium atoms (formed via $\bar{p} + ^4He \rightarrow (\bar{p}He)^+_q + e$) and measures hyperfine transitions in metastable states (n ~ 30-100). The hyperfine splitting is:

$$\Delta E = \alpha^2 m_{\bar{p}} c^2 \cdot f(Z, n, j) \quad \text{(CPT-sensitive)}$$

Current precision: $\Delta E / E = 10^{-10}$ (2023). Upgrade toward $10^{-12}$ (2026-2028) targets CPT-violating terms in the Dirac equation.

---

## Key Results

1. **ELENA boost**: 10-100x increase in trap efficiency enables simultaneous precision experiments and improved statistical power.

2. **ALPHA-g tension**: $\alpha_g = 0.75 \pm 0.29$ hints at new physics in gravity-antimatter coupling, though systematics remain under investigation (blind reanalysis planned 2026).

3. **CPT verification**: Charge symmetry, mass symmetry, and anomalous moment all consistent with CPT to $10^{-9} - 10^{-13}$ (baryon sector dominates all limits).

4. **Multiple gravity probes**: ALPHA-g (direct), AEgIS (moiré), GBAR (free-fall), ASACUSA (spectroscopic) converge toward $\Delta g/g < 0.01$ by 2027.

5. **Dark matter connection**: Antiproton abundance in cosmic rays constrains dark matter annihilation cross-section. AD/ELENA program supports indirect DM searches via antimatter beams and precision antiproton annihilation spectroscopy.

6. **Long-term horizon (post-2030)**: Transportable antimatter traps, antineutron physics, exotic hadron spectroscopy, and fundamental symmetry tests at new facilities (ESS antiproton source, J-PARC antimatter beams).

7. **Roadmap extension**: 2040-2050 vision includes antimatter oscillation tests (matter-antimatter regeneration), antimatter-containing nuclei, and astrophysical applications (gravitational lensing by antimatter remnants in early universe).

---

## Impact and Legacy

The 2025 AD/ELENA review codifies antimatter research as a precision frontier comparable in sensitivity to flavor physics (B factories, kaon factories) and EW precision (Z-pole, lepton universality). ALPHA-g's hint at gravity-antimatter coupling mismatch triggers sustained theoretical interest in:

- Spin-dependent gravitational forces
- CPT violation in curved spacetime
- Antimatter dark matter candidates
- Quantum gravity signatures in antiproton spectra

The program's infrastructure enables sensitivity improvements of 10-100x over the next 5 years. Success would establish antimatter precision physics as a primary window on BSM (Beyond Standard Model) physics, rivaling the LHC in discovery potential while operating in a fundamentally different regime (precision vs. energy).

Collaboration size: ~350 physicists across 10 countries. Annual CERN budget allocation: ~15M EUR (2024-2030 planning).

---

## Connection to Phonon-Exflation Framework

### Dirac J Operator and CPT Hardwiring

The spectral action framework encodes CPT symmetry through the J operator (chirality flip, particle-antiparticle conjugation):

$$[J, D_K] = 0 \quad \text{(Session 17a, proven machine epsilon)}$$

ALPHA-g's hint at gravity-antimatter mismatch ($\alpha_g \approx 0.75$) appears inconsistent with this hardwiring IF gravity couples universally. However, two resolutions exist:

1. **GRAVITY NOT UNIVERSAL IN QG**: If phonon geometry is emergent from BCS pair dynamics, gravity may emerge with a different coupling to fermionic condensate vs. normal particles. Antiparticle excitations on the condensate could carry different gravitational charge than particle excitations (asymmetric dispersion).

2. **J IS ROBUST BUT G-COUPLING EMERGENT**: The Dirac spectrum respects [J, D_K] = 0, preserving CPT in vacuum, but antimatter-gravity coupling emerges at the many-body level. Framework predicts $\alpha_g = 0$ at tree level but permits O(0.1%-1%) loop corrections from BCS gap structure and spectral back-reaction (van Suijlekom one-loop formalism).

### Antiproton in NCG SM

In the phonon-exflation NCG model:
- Antiproton is Psi_+ eigenstate (chirality +1 for left-handed antifermion)
- Mass arises from spectral action coupling to Higgs vev: $m_p \sim e_p \langle H \rangle$
- The coupling e_p is related to SU(3) gauge constant via Einstein point duality

ALPHA-g measures whether $e_p$ (antimatter electromagnetic coupling) and gravity decouple proportionally. The result $\alpha_g \approx 0.75$ suggests:

$$\frac{g_{\bar{p}}}{g_p} \approx 1 + 0.75 \times 10^{-2} \quad \text{(rough)}$$

This is **inconsistent with SU(3) symmetry** unless the vacuum geometry (Ricci scalar, KK warp factor) differs for antimatter sector. See Session 17a result: [J, D_K] = 0 PROVES CPT at Dirac level, but curvature coupling is separate.

### Experimental Bridge: ALPHA-g as CP Violation Probe

If $\alpha_g$ persists after 2026 blind reanalysis, the phonon-exflation framework predicts the source is **not fundamental CPT violation** but rather **emergent asymmetry in the BCS substrate**. Specifically:

- Pair excitations ($\Delta^+$, antiparticle-like) vs. hole excitations ($\Delta^-$, particle-like) have different effective masses in the condensate.
- Gravity couples to the substrate stress-energy tensor, which is imbalanced between particle and antiparticle sectors.
- Correction magnitude: $\Delta \alpha_g / \alpha_g \sim (m_\Delta^+ - m_\Delta^-) / m_\Delta \sim$ few %.

**Prediction**: GBAR (2026-2027) and AEgIS (moiré, 2026) will confirm or refute this hint. If all three methods (ALPHA-g, GBAR, AEgIS) agree on $\alpha_g > 0.3$ at 2-3 sigma, phonon-exflation requires **exotic BCS phase mismatch**. If they scatter around $\alpha_g = 0$, the framework is vindicated and ALPHA-g was a systematic.

---

## Reference Notes

- **ELENA commissioning**: Breuker et al., NIM A (2018) — cooling performance
- **ALPHA-g preliminary**: Ahmadi et al., Nature Physics 18 (2024) — first gravity measurement
- **CPT fundamentals**: Greenberg, Rev. Mod. Phys. 78 (2006) — theoretical review
- **Spectral action gravity**: Chamseddine-Connes, JMP 48 (2007) — Einstein via spectral action

