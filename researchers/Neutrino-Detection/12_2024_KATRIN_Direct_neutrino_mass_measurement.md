# Direct Neutrino-Mass Measurement Based on 259 Days of KATRIN Data

**Authors:** M. Aker et al. (KATRIN Collaboration)
**Year:** 2024
**Journal:** *Science*, **386**(6723), eadq9592

---

## Abstract

The Karlsruhe Tritium Neutrino (KATRIN) experiment measured the effective electron antineutrino mass by precision spectroscopy of the tritium beta decay endpoint. Using 259 measurement days of data collected between 2019 and 2021 with an integrated dataset of 36 million beta electrons, KATRIN obtained an upper limit of $m_\nu < 0.45\;\text{eV}/c^2$ at 90% confidence level -- the most stringent model-independent bound on the neutrino mass from a direct kinematic measurement, improving the previous KATRIN limit by nearly a factor of two. The measurement was achieved with the MAC-E filter (Magnetic Adiabatic Collimation with Electrostatic filter), a 70-meter spectrometer that analyzes the electron energy spectrum within the last $\sim$40 eV of the tritium endpoint at $Q = 18.574$ keV. The result is independent of whether neutrinos are Dirac or Majorana particles and does not rely on cosmological model assumptions.

---

## Historical Context

### The Neutrino Mass Problem

The question of whether neutrinos have mass has been central to particle physics since Pauli postulated the neutrino in 1930. In the original Standard Model, neutrinos are exactly massless -- there are no right-handed neutrino fields, and the Higgs mechanism cannot generate a Dirac mass term. The discovery of neutrino oscillation (Super-Kamiokande 1998, SNO 2001-2002, KamLAND 2003) established that neutrinos have non-zero masses, but oscillation experiments measure only mass-squared differences, not absolute masses:

$$\Delta m^2_{21} = m_2^2 - m_1^2 = (7.53 \pm 0.18) \times 10^{-5}\;\text{eV}^2$$
$$|\Delta m^2_{32}| = |m_3^2 - m_2^2| = (2.453 \pm 0.033) \times 10^{-3}\;\text{eV}^2$$

These determine the mass splittings but leave the absolute mass scale undetermined. Three complementary approaches constrain the absolute mass:

1. **Direct kinematic measurement** (beta decay endpoint): Model-independent, measures $m_\nu^{eff} = \sqrt{\sum_i |U_{ei}|^2 m_i^2}$.
2. **Neutrinoless double beta decay** ($0\nu\beta\beta$): Measures $m_{\beta\beta} = |\sum_i U_{ei}^2 m_i|$, but only if neutrinos are Majorana particles.
3. **Cosmological bounds**: The CMB and large-scale structure constrain $\sum m_i$, but the result depends on the cosmological model assumed.

### Beta Decay Endpoint: The Fermi Approach

Enrico Fermi's theory of beta decay (1934) predicts that the electron energy spectrum near the endpoint is sensitive to the neutrino mass. For tritium beta decay:

$$^3\text{H} \to ^3\text{He}^+ + e^- + \bar{\nu}_e$$

The differential decay rate as a function of the electron kinetic energy $E$ is:

$$\frac{d\Gamma}{dE} = C \cdot F(Z', E) \cdot p \cdot (E + m_e) \cdot (E_0 - E) \cdot \sqrt{(E_0 - E)^2 - m_\nu^2} \cdot \Theta(E_0 - E - m_\nu)$$

where $C$ is a constant containing the nuclear matrix element and $G_F$, $F(Z', E)$ is the Fermi function (Coulomb correction for the daughter nucleus $^3$He with $Z' = 2$), $p$ is the electron momentum, $E_0 = Q - m_\nu$ is the endpoint energy for $m_\nu = 0$, and $\Theta$ is the Heaviside step function enforcing energy conservation.

The key feature is the behavior near the endpoint ($E \to E_0$):

$$\frac{d\Gamma}{dE}\bigg|_{E \approx E_0} \propto (E_0 - E)\sqrt{(E_0 - E)^2 - m_\nu^2}$$

For $m_\nu = 0$, the spectrum vanishes as $(E_0 - E)^2$ at the endpoint. For $m_\nu > 0$, the spectrum terminates at $E_{max} = E_0 - m_\nu$ and the shape near the endpoint is modified. The signature of a non-zero neutrino mass is:

1. **A shift of the endpoint** from $E_0$ to $E_0 - m_\nu$.
2. **A kink in the spectrum** at $E = E_0 - m_\nu$ where the spectrum abruptly goes to zero.
3. **A deficit of events** in the last $\sim m_\nu$ eV of the spectrum, with the spectral shape distorted.

### Why Tritium?

Tritium is the isotope of choice for neutrino mass measurements for several reasons:

**Low Q-value:** $Q = 18.574$ keV is one of the lowest beta decay endpoints, meaning a larger fraction of decays occur near the endpoint (the sensitive region). The fraction of decays in the last $\Delta E$ eV of the spectrum is $f \propto (\Delta E / Q)^3$, so low $Q$ maximizes $f$.

**Simple nuclear structure:** The $^3$H $\to$ $^3$He transition is a superallowed Gamow-Teller decay between mirror nuclei with a simple nuclear matrix element that is well understood theoretically.

**Short half-life:** $T_{1/2} = 12.32$ years gives a specific activity of $3.57 \times 10^{14}$ Bq/g, providing a high count rate.

**Low Z:** The low nuclear charge ($Z = 1$) means the Fermi function correction is small and well-controlled.

### Previous Direct Measurements

The history of direct neutrino mass measurements from tritium beta decay:

| Experiment | Year | Result | Technique |
|:-----------|:-----|:-------|:----------|
| ITEP (Moscow) | 1980 | $m_\nu \approx 30$ eV (later retracted) | Magnetic spectrometer |
| LANL | 1991 | $m_\nu < 9.3$ eV | Magnetic spectrometer |
| Mainz | 2005 | $m_\nu < 2.3$ eV | MAC-E filter |
| Troitsk | 2011 | $m_\nu < 2.05$ eV | MAC-E filter |
| KATRIN (first) | 2019 | $m_\nu < 1.1$ eV | MAC-E filter |
| KATRIN (improved) | 2022 | $m_\nu < 0.8$ eV | MAC-E filter |
| **KATRIN (final)** | **2024** | $m_\nu < 0.45$ eV | **MAC-E filter** |

The ITEP claim of a 30 eV neutrino mass generated enormous excitement in the 1980s but was eventually traced to systematic errors in the energy loss correction. This cautionary tale underscores the importance of systematic error control in endpoint measurements.

---

## Key Arguments and Derivations

### I. The MAC-E Filter Principle

KATRIN's spectrometer is based on the MAC-E (Magnetic Adiabatic Collimation with Electrostatic filter) principle, which combines magnetic and electrostatic fields to achieve extremely high energy resolution.

**Magnetic adiabatic collimation:** The electron is born in a strong magnetic field ($B_s \sim 3.6$ T at the source) and travels toward the spectrometer, where the field drops to a very weak minimum ($B_{min} \sim 0.3$ mT at the analyzing plane). The magnetic moment of the electron's cyclotron motion is an adiabatic invariant:

$$\mu = \frac{E_\perp}{B} = \text{const}$$

where $E_\perp$ is the kinetic energy of the transverse (cyclotron) component. As $B$ decreases by a factor of $\sim 10^4$, $E_\perp$ decreases by the same factor, and the corresponding energy is transferred to the longitudinal component $E_\parallel$. At the analyzing plane, essentially all the kinetic energy is in the forward direction:

$$E_\parallel \approx E_{kin} - E_\perp^0 \cdot \frac{B_{min}}{B_s} \approx E_{kin}\left(1 - \frac{B_{min}}{B_s}\right)$$

This "magnetic collimation" converts an isotropically emitted electron into a forward-moving one, regardless of its initial emission angle.

**Electrostatic filter:** At the analyzing plane, a retarding electrostatic potential $U_0$ is applied. Only electrons with $E_\parallel > eU_0$ pass through. The energy resolution is:

$$\Delta E = \frac{B_{min}}{B_{max}} \cdot E_{kin} \approx \frac{0.3 \times 10^{-3}}{6} \times 18574 \approx 0.93\;\text{eV}$$

This sub-eV resolution at 18.6 keV represents a resolving power of $E/\Delta E \approx 20{,}000$ -- achieved without any slit or collimator, with the full $2\pi$ solid angle of forward emission accepted.

### II. The KATRIN Beamline

The full KATRIN apparatus extends approximately 70 meters and consists of five major components:

**1. Windowless Gaseous Tritium Source (WGTS):** A 10-meter long tube of 90 mm diameter, cooled to 30 K and stabilized to $\pm$30 mK, through which molecular tritium ($T_2$) is injected at the center and pumped out at both ends. The column density is $5 \times 10^{17}$ molecules/cm$^2$, producing a beta decay rate of $\sim 10^{11}$ per second. The gaseous source avoids the solid-state final-state effects that plagued earlier experiments.

**2. Differential Pumping Section (DPS):** A series of turbomolecular pumps reduces the tritium flow by a factor of $> 10^7$, preventing tritium from reaching the spectrometer.

**3. Cryogenic Pumping Section (CPS):** A liquid helium-cooled section with argon frost on the walls traps the remaining tritium by a further factor of $> 10^7$, achieving a total tritium suppression of $> 10^{14}$.

**4. Pre-spectrometer:** A smaller MAC-E filter ($L = 3.4$ m, $D = 1.7$ m) that rejects electrons more than $\sim$300 eV below the endpoint, reducing the electron flux entering the main spectrometer by a factor of $\sim 10^6$ and thus reducing backgrounds from ionization of residual gas.

**5. Main spectrometer:** The central instrument, a stainless steel vessel 23.3 m long and 10 m in diameter (the world's largest ultra-high vacuum vessel, $P < 10^{-11}$ mbar). Two superconducting solenoids at either end produce the maximum field ($B_{max} = 6$ T at the entrance, $B_s = 3.6$ T at the exit/pinch), while the field at the analyzing plane drops to $B_{min} = 0.3$ mT. A system of wire electrodes on the inner wall shapes the retarding potential and suppresses secondary electrons from the vessel wall.

**6. Focal Plane Detector (FPD):** A 148-pixel silicon PIN diode array (wafer diameter 90 mm) that counts the transmitted electrons with >95% efficiency and $\sim$1.5 keV energy resolution (sufficient to distinguish signal from background).

### III. The Integral Spectrum Measurement

KATRIN operates as an integrating high-pass filter: at retarding voltage $U_0$, it counts all electrons with $E > eU_0$. The measured count rate as a function of $U_0$ is:

$$R(U_0) = A_{sig} \int_0^\infty \frac{d\Gamma}{dE}(E; m_\nu^2) \cdot T(E, U_0) \cdot \epsilon(E)\;dE + R_{bkg}$$

where $T(E, U_0)$ is the transmission function of the MAC-E filter:

$$T(E, U_0) = \begin{cases} 0 & E < eU_0 \\ \frac{1 - \sqrt{1 - (E - eU_0)/E \cdot B_s/B_{max}}}{1 - \sqrt{1 - B_s/B_{max}}} & eU_0 \leq E \leq eU_0 + \Delta E \\ 1 & E > eU_0 + \Delta E \end{cases}$$

$\epsilon(E)$ is the detection efficiency, $A_{sig}$ is the signal amplitude, and $R_{bkg}$ is the background rate.

The integral spectrum is scanned by stepping $U_0$ through a set of retarding voltages in the last $\sim$40 eV below the endpoint, spending more time at voltages near the endpoint where the sensitivity to $m_\nu^2$ is greatest.

### IV. Statistical Sensitivity

The number of beta decay events in the last $\Delta E$ eV below the endpoint is:

$$N(\Delta E) \approx N_{total} \times \frac{2}{3}\left(\frac{\Delta E}{Q}\right)^3$$

For $\Delta E = 1$ eV (the region most sensitive to $m_\nu$):

$$f(1\;\text{eV}) = \frac{2}{3}\left(\frac{1}{18574}\right)^3 \approx 1.0 \times 10^{-13}$$

This means only about 1 in $10^{13}$ decays produces an electron in the last eV -- the region where the neutrino mass signature lives. At KATRIN's decay rate of $\sim 10^{11}$/s, this gives $\sim 10^{-2}$ events per second in the last eV, or about 1000 events per day. This explains why KATRIN needed 259 measurement days and 36 million total electrons to achieve sub-eV sensitivity.

The statistical sensitivity to $m_\nu^2$ scales as:

$$\sigma(m_\nu^2) \propto \frac{1}{\sqrt{N}} \cdot \frac{\Delta E^{5/2}}{Q^{3/2}} \cdot \frac{1}{(\Delta E)^{1/2}}$$

where $N$ is the total number of detected electrons and $\Delta E$ is the measurement interval below the endpoint.

### V. Systematic Uncertainties

The major sources of systematic uncertainty in KATRIN are:

**Final-state distribution (FSD):** After beta decay, the $^3$He$^+$ daughter ion (and its molecular partner in $T_2$) can be left in excited electronic, rotational, or vibrational states. Each final state $f$ shifts the effective endpoint:

$$\frac{d\Gamma}{dE} = \sum_f P_f \cdot \frac{d\Gamma_f}{dE}(E; Q - V_f, m_\nu^2)$$

where $P_f$ is the probability of final state $f$ and $V_f$ is its excitation energy. The FSD was calculated ab initio by Saenz et al. with an uncertainty of $\sim$0.1 eV on the mean excitation energy.

**Energy loss in the source:** Electrons produced in the interior of the WGTS may scatter off tritium molecules before exiting, losing energy. The energy loss function was measured in situ using a monoenergetic electron gun (e-gun) and deconvolved from the spectrum.

**Background:** The background rate in the signal region was $\sim$0.1 counts per second, dominated by:
- Radon decays in the spectrometer volume (mitigated by liquid nitrogen baffles).
- Secondary electrons from the spectrometer wall (suppressed by wire electrode shielding).
- Penning traps in the inter-spectrometer region.

The 2024 analysis achieved a substantial background reduction compared to earlier campaigns.

**Magnetic field inhomogeneity:** Variations in $B$ across the analyzing plane produce pixel-to-pixel variations in the energy resolution and transmission function. These were mapped using the e-gun and incorporated in the pixel-by-pixel fit.

### VI. The 2024 Result

The combined analysis of five measurement campaigns (KNM1-KNM5, 259 days) yielded:

$$m_\nu^2 = -0.14^{+0.13}_{-0.15}\;\text{eV}^2$$

The central value is unphysical (negative $m_\nu^2$), which can occur as a statistical fluctuation. Converting to an upper limit using the Feldman-Cousins (frequentist) method:

$$m_\nu < 0.45\;\text{eV}/c^2\quad(90\%\;\text{CL})$$

This improves on the previous KATRIN result ($m_\nu < 0.8$ eV) by nearly a factor of two, driven by:
- Doubled statistics (259 vs 82 measurement days).
- Reduced background (improved radon mitigation, optimized magnetic fields).
- Better systematic understanding (refined FSD, improved energy loss model).

### VII. Comparison with Other Constraints

| Method | Bound | Assumptions |
|:-------|:------|:------------|
| **KATRIN (direct)** | $m_\nu < 0.45$ eV | Model-independent |
| Planck CMB | $\sum m_i < 0.12$ eV | $\Lambda$CDM cosmology |
| DESI + CMB (2024) | $\sum m_i < 0.072$ eV | $\Lambda$CDM + BAO |
| $0\nu\beta\beta$ (KamLAND-Zen) | $m_{\beta\beta} < 0.036-0.156$ eV | Majorana only |

The cosmological bounds are much tighter but model-dependent -- they assume the standard $\Lambda$CDM framework with its six parameters. The KATRIN bound is the tightest model-independent constraint.

If we assume the cosmological bound $\sum m_i < 0.12$ eV and the measured mass splittings, the individual masses are:

**Normal ordering ($m_1 < m_2 < m_3$):**
$$m_1 \lesssim 0.02\;\text{eV},\quad m_2 \approx \sqrt{\Delta m^2_{21} + m_1^2} \approx 0.009\;\text{eV},\quad m_3 \approx \sqrt{|\Delta m^2_{32}|} \approx 0.05\;\text{eV}$$
$$\sum m_i \approx 0.06\;\text{eV}$$

**Inverted ordering ($m_3 < m_1 < m_2$):**
$$m_3 \lesssim 0.01\;\text{eV},\quad m_1 \approx m_2 \approx \sqrt{|\Delta m^2_{32}|} \approx 0.05\;\text{eV}$$
$$\sum m_i \approx 0.10\;\text{eV}$$

The cosmological bound is beginning to disfavor the inverted ordering.

---

## Sterile Neutrino Search

### The Reactor Antineutrino Anomaly

In 2011, Mention et al. reported that the predicted reactor $\bar{\nu}_e$ flux (using updated nuclear data) exceeded the observed flux at short baselines by $\sim$6%, suggesting a possible sterile neutrino with $\Delta m^2_{41} \sim 1\;\text{eV}^2$ that would cause rapid oscillation at $L \sim 10$ m.

### KATRIN's Sterile Search

KATRIN can search for sterile neutrinos with $m_4^2$ in the range $1-1000\;\text{eV}^2$ by looking for a kink in the beta spectrum at $E = Q - m_4$. A sterile neutrino with mixing $|U_{e4}|^2$ would distort the spectrum:

$$\frac{d\Gamma}{dE} = (1 - |U_{e4}|^2)\frac{d\Gamma}{dE}(m_\nu) + |U_{e4}|^2\frac{d\Gamma}{dE}(m_4)$$

Using the full 259-day dataset, KATRIN found no evidence for sterile neutrinos and set limits of $|U_{e4}|^2 < 0.01-0.1$ for $m_4^2$ in the range $1-100\;\text{eV}^2$, disfavoring the reactor anomaly interpretation and consistent with the null results from other short-baseline experiments.

### The TRISTAN Upgrade

KATRIN is being upgraded with the TRISTAN (TRItium Spectrum To search for sterile neutrinos using a New detector) focal plane detector -- a multi-pixel silicon drift detector array with improved energy resolution and count rate capability. TRISTAN will extend the search for sterile neutrinos to the full tritium spectrum (not just the endpoint), probing $|U_{e4}|^2 > 10^{-6}$ for $m_4$ in the keV range. This is the mass range relevant for sterile neutrino dark matter candidates.

---

## Physical Interpretation

### The Neutrino Mass Scale

The KATRIN result, combined with oscillation data, establishes that the heaviest neutrino mass eigenstate has a mass:

$$m_{heaviest} \geq \sqrt{|\Delta m^2_{32}|} \approx 0.050\;\text{eV}$$

and the effective electron neutrino mass measured by KATRIN is:

$$m_\nu^{eff} = \sqrt{\sum_i |U_{ei}|^2 m_i^2} < 0.45\;\text{eV}$$

The gap between the lower bound (0.05 eV) and the upper limit (0.45 eV) will be closed by KATRIN's final analysis and its successor, Project 8.

### Dirac vs Majorana

KATRIN's measurement is the same regardless of whether neutrinos are Dirac or Majorana particles -- the endpoint measurement is sensitive only to the kinematic mass. This model-independence is a strength: the KATRIN bound applies regardless of the mass generation mechanism.

In contrast, neutrinoless double beta decay ($0\nu\beta\beta$) occurs only if neutrinos are Majorana particles and measures a different effective mass $m_{\beta\beta}$. If $0\nu\beta\beta$ is observed, the comparison of $m_{\beta\beta}$ with $m_\nu^{eff}$ (KATRIN) constrains the Majorana phases in the PMNS matrix.

### Why Are Neutrinos So Light?

The smallness of neutrino masses -- at least 6 orders of magnitude lighter than the electron -- is one of the deepest puzzles in particle physics. The seesaw mechanism provides a natural explanation: if neutrinos have both Dirac masses $m_D$ (of order the electroweak scale) and large Majorana masses $M_R$ (of order the GUT scale), the light neutrino masses are:

$$m_\nu \approx \frac{m_D^2}{M_R} \sim \frac{(100\;\text{GeV})^2}{10^{14}\;\text{GeV}} \sim 0.1\;\text{eV}$$

This elegantly explains the mass scale but introduces new high-energy parameters that are not directly testable.

---

## Connection to Phonon-Exflation Framework

### Neutrino Masses from the Dirac Spectrum

In the phonon-exflation framework, neutrino masses arise from the lightest eigenvalues of the internal Dirac operator $D_K(s)$ on the compactification manifold $K = \text{SU}(3)$. Unlike the Standard Model, where neutrino masses are free parameters (Yukawa couplings), the framework predicts neutrino masses from the geometry of $K$ with the Jensen deformation parameter $s$ as the sole input:

$$m_{\nu_i} = \lambda_i(s_0) \cdot M_{scale}$$

where $\lambda_i(s_0)$ are the lightest positive eigenvalues of $D_K(s_0)$ at the stabilized deformation, and $M_{scale}$ is set by the compactification radius.

KATRIN's upper bound $m_\nu < 0.45\;\text{eV}$ directly constrains the smallest eigenvalue spacing:

$$\lambda_1(s_0) \cdot M_{scale} < 0.45\;\text{eV}$$

Combined with the requirement that the same $D_K(s_0)$ produces the correct charged lepton and quark masses (at $\sim$MeV-GeV scale), this constrains the spectrum of $D_K(s_0)$ to span at least 10 orders of magnitude -- from the neutrino mass scale ($\sim 0.05$ eV) to the top quark mass ($\sim 170$ GeV). The Tier 1 Dirac spectrum computation (Session 12) found eigenvalue ratios spanning 3-4 orders of magnitude at $s \approx 1$, suggesting that the full physical spectrum may require higher $(p,q)$ irreducible representations than currently computed (max $p+q = 6$).

### No Free Yukawa Couplings

The crucial distinction from the Standard Model is that the phonon-exflation framework has NO free Yukawa couplings for neutrinos. In the SM, the neutrino mass is $m_\nu = y_\nu v / \sqrt{2}$, where $y_\nu$ is the Yukawa coupling -- a free parameter that must be set to $y_\nu \sim 10^{-12}$ (absurdly small) to match observation. In the framework, the "Yukawa coupling" is a matrix element of $D_K(s)$ between specific $(p,q)$ representations, computed from the geometry. The smallness of neutrino masses must emerge naturally from the spectrum of $D_K(s)$, not from fine-tuning.

Session 12 established that the eigenvalues of $D_K(s)$ are not uniformly spaced but cluster in sector-specific patterns. The lightest eigenvalues (in the $(0,0)$ and $(1,0)$ sectors at small $s$) are well-separated from the heavier sectors, providing a geometric mechanism for the neutrino-charged lepton mass hierarchy -- analogous to how the seesaw mechanism separates scales, but without introducing new parameters.

### Normal vs Inverted Hierarchy as a Prediction

The neutrino mass ordering (normal: $m_1 < m_2 < m_3$, or inverted: $m_3 < m_1 < m_2$) is a prediction of the framework, not an input. The ordering of the lightest eigenvalues of $D_K(s_0)$ determines whether the electron-neutrino-dominated mass eigenstate ($\nu_1$) is lighter or heavier than the muon- and tau-dominated eigenstates ($\nu_2, \nu_3$). Current Tier 1 computations have not yet resolved this -- the lightest eigenvalues at $p + q \leq 6$ are in the $(0,0)$, $(1,0)$, and $(0,1)$ sectors, but the assignment to physical neutrino species requires the full spinor transport calculation (Baptista Paper 14, Section 3.2), which is a Tier 2 deliverable.

The cosmological constraint $\sum m_i < 0.12$ eV is beginning to disfavor the inverted ordering independently. If the framework predicts normal ordering, this is a consistency check; if it predicts inverted ordering, the framework faces increasing tension with cosmological data.

### Cosmological Sum Constraint and the Internal Spectrum

The Planck CMB constraint $\sum m_i < 0.12$ eV is an even tighter bound on the Dirac spectrum than KATRIN's single-neutrino limit. Translating to eigenvalues:

$$\sum_{i=1}^3 \lambda_i(s_0) \cdot M_{scale} < 0.12\;\text{eV}$$

This constrains the sum of the three lightest positive eigenvalues of $D_K(s_0)$. However, this bound assumes $\Lambda$CDM cosmology. In the phonon-exflation framework, the expansion history differs from $\Lambda$CDM (expansion is driven by internal compactification, not a cosmological constant), and the relationship between $\sum m_i$ and the CMB power spectrum may be modified. Whether this relaxes or tightens the bound is an open question that depends on the detailed expansion history -- a Tier 3 computation.

### The NCG Spectral Triple and Neutrino Counting

The NCG spectral triple structure $(A, H, D; J, \gamma)$ determines the number of neutrino mass eigenstates. Session 17a result B-4 established the $Z_3 = (p-q)\;\text{mod}\;3$ grading of the 28 irreps, which if identified with generation number gives exactly three generations. KATRIN's sterile neutrino search (finding no evidence for $m_4$ in the eV-keV range) is consistent with this three-generation prediction. The TRISTAN upgrade, probing $|U_{e4}|^2 > 10^{-6}$ for keV-scale sterile neutrinos, will provide an even more stringent test.

If the framework predicts additional KK excitations of the neutrino above the keV scale, these would appear as kinks in the tritium spectrum that TRISTAN could detect. The mass of the first KK neutrino excitation is set by the compactification scale, providing a direct experimental window into the geometry of the internal space.

### KATRIN as a Constraint on the Stabilization Point

Ultimately, KATRIN's precision measurement constrains the stabilization point $s_0$ of the Jensen deformation. If the effective potential $V_{eff}(s)$ stabilizes at a specific $s_0$, then $D_K(s_0)$ has a definite spectrum, and the lightest eigenvalues must satisfy KATRIN's bound. The Session 14 Coleman-Weinberg analysis found $s_0 \sim 0.3-0.6$, and the Session 17a gauge coupling derivation found $s_0 = 0.2994$ from $\sin^2\theta_W$. At these values, the Tier 1 spectrum shows eigenvalues that span the right order of magnitude for the charged fermion masses. Whether the lightest eigenvalues at $s_0 \approx 0.3$ are small enough to match the neutrino mass scale ($\lesssim 0.45$ eV when scaled to physical units) is one of the decisive tests of the framework.
