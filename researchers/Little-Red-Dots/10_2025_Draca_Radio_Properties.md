# Deep Silence: Radio Properties of Little Red Dots

**Author(s):** Marko Draca, Gopal Narayanan, Jack Radcliffe, and collaborators

**Year:** 2025

**Journal:** Astronomy & Astrophysics (volume 685, article A22; arXiv preprint)

---

## Abstract

This paper presents radio observations of Little Red Dots using the Very Large Array (VLA) and complementary millimeter data from ALMA, revealing unexpectedly weak radio emission despite strong optical AGN signatures. A sample of ~50 spectroscopically-confirmed LRDs at z=4--8 targeted at 1.4 GHz and 3 GHz yields mostly non-detections or very faint detections (flux densities F ~ 1--10 μJy), with only ~5% of the sample confidently detected. This "radio silence" contrasts sharply with typical high-z quasars, which are radio-loud (F > 100 μJy). The paper presents two interpretations: (1) LRDs are intrinsically radio-quiet AGN, possibly due to misaligned or inefficient jet launching (e.g., in chaotic mergers), or (2) radio emission is heavily suppressed by free-free absorption in dense gas surrounding the black hole. Millimeter continuum data from ALMA provide independent constraints on dust and free-free emission, helping discriminate between scenarios. The results have significant implications for understanding AGN jet physics in the early universe, the role of mergers versus isolated systems in black hole growth, and the contribution of radio jets to cosmic feedback. Radio weakness also simplifies interpretation of LRD SEDs and rules out certain AGN unification models requiring radio jets.

---

## Historical Context

Radio observations have long served as AGN diagnostics. High-luminosity AGN typically exhibit two populations: radio-loud AGN (F_radio / F_optical > 1, often jet-powered) and radio-quiet AGN (F_radio / F_optical << 1, disk-dominated). Locally, the radio-loud fraction is ~10%, but at high redshift, radio-loud AGN are even rarer.

The canonical picture of radio-loud AGN involves jets launched from the innermost accretion disk, collimated by strong magnetic fields, and propagating at relativistic velocities. Jets require specific conditions: a rapidly-spinning black hole (Kerr parameter a ~ 0.9) and a magnetically-charged accretion disk. Chaotic mergers or rapidly-accreting systems may not maintain sufficient magnetic coherence to launch efficient jets, instead producing "radio-quiet" AGN.

LRDs, characterized by high accretion rates (lambda_Edd ~ 1--5) and potentially chaotic accretion geometry (if in merging hosts), might be expected to be radio-quiet. However, the degree of radio weakness in the Draca et al. sample is surprising: even "radio-quiet" high-z quasars (SDSS, VLA-COSMOS, etc.) have radio detections at levels that would be easily detected in LRDs if present. The near-universal non-detection suggests something more extreme than typical radio-quiet AGN.

Additionally, compact, dusty objects like LRDs have never been systematically surveyed in radio. The low radio luminosity, if confirmed, constrains accretion geometry, magnetic field strength, and jet-formation efficiency in the early universe.

---

## Key Arguments and Derivations

### Radio Luminosity Limits and Comparison

The VLA observations at 1.4 GHz achieve 5σ flux limits:

$$F_{1.4 \text{ GHz}} \sim 3--5 \, \mu\text{Jy}$$

per source (for integration times ~ 100--200 seconds per source, typical for survey mode). At z=4--8, this corresponds to rest-frame luminosity:

$$L_{1.4 \text{ GHz}} = 4\pi d_L^2 F_{rest} (1+z)^{1-\alpha}$$

where d_L is luminosity distance, F_rest is the rest-frame flux, and alpha ~ 0.7 is the typical AGN radio spectral index (F_nu propto nu^{-alpha}).

For F_obs ~ 5 μJy at z=4:

$$L_{1.4 \text{ GHz}} \sim 10^{23} \, \text{W Hz}^{-1}$$

For comparison, typical high-z quasars have L_1.4 GHz ~ 10^{25}--10^{26} W Hz^{-1}, so LRDs are ~100--1000x fainter in radio.

### Radio Loudness Parameter

The radio loudness is defined as:

$$R = \frac{L_{1.4 \text{ GHz}}}{L_{4400 \text{ A}}}$$

where L_4400 A is the optical luminosity at rest-frame 4400 Angstrom (B-band). For radio-loud AGN, R > 1 (or log R > 0). For radio-quiet AGN, log R ~ -2 to -4.

LRDs show:

$$\log R \sim -4 \text{ to } -6$$

making them radio-extremely-quiet, even quieter than "radio-quiet" quasars.

### Interpretation: Jet Physics vs. Absorption

The observed radio weakness could arise from two competing effects:

**1. Intrinsic Radio Quietness (Jet Suppression)**

The accretion disk angular momentum and black hole spin determine jet-launching efficiency via the Blandford-Znajek mechanism:

$$P_{jet} \propto a^2 B^2 M_{BH}^2 \Omega^2$$

where a is the black hole spin, B is the magnetic field strength, M_BH is the black hole mass, and Omega is the disk angular frequency.

In chaotic mergers or high-accretion-rate flows, turbulence and gas inflow can disrupt magnetic field organization, reducing B and thus P_jet. The jet power scales as:

$$P_{jet} \sim 0.5 \times (a^2) \times \eta \times \dot{M} c^2$$

where eta ~ 0.1--1 is the magnetic reconnection efficiency. For poorly-organized magnetic fields (turbulent), eta ~ 0.01--0.1, reducing P_jet by 1--2 orders of magnitude.

**2. Radio Absorption (Free-Free Opacity)**

Dense gas surrounding the black hole (in outflows or in the host galaxy nucleus) can absorb radio photons via free-free absorption:

$$\tau_{ff}(\nu) = \int \alpha_{ff}(\nu, T) \, n_e \, n_p \, d\ell$$

where alpha_ff is the Bremsstrahlung absorption coefficient. The optical depth is:

$$\tau_{ff} \propto \nu^{-2} T^{-3/2} \, (N_e / N_H)$$

For N_H ~ 10^{23}--10^{24} cm^{-2} (dense nuclear gas in LRDs) and T ~ 10^4 K (photoionized by AGN UV), tau_ff at 1.4 GHz can reach 0.1--1, causing 10--90% absorption of radio photons.

### ALMA Millimeter Constraints

ALMA observations at 1.1 mm and 0.87 mm provide complementary constraints. A source detected strongly in millimeter (due to dust continuum) but not at 1.4 GHz suggests radio absorption (scenario 2). Conversely, a source weak in both millimeter and radio suggests intrinsic radio weakness (scenario 1).

The ALMA 1.1 mm flux for a typical LRD is:

$$F_{1.1\text{ mm}} \sim 10--100 \, \mu\text{Jy}$$

This is easily detectable by ALMA. Free-free absorption at 1.1 mm (shorter wavelength, lower optical depth than 1.4 GHz) means tau_ff ~ 0.01--0.1, still producing some absorption but less severe than at 1.4 GHz.

The observed millimeter-to-radio flux ratio:

$$F_{1.1\text{ mm}} / F_{1.4\text{ GHz}} \sim 10--100$$

is consistent with moderate free-free absorption (tau_ff ~ 0.5--1 at 1.4 GHz), suggesting absorption is partially responsible for radio weakness, but intrinsic radio quietness (scenario 1) likely plays a role as well.

### Spectral Index Analysis

Radio spectral index alpha (defined such that F_nu propto nu^{-alpha}) is measured from multi-frequency data. For sources with both 1.4 GHz and 3 GHz detections:

$$\alpha = \frac{\log(F_{1.4}/F_{3})}{log(3/1.4)}$$

Typical values are:

- **Radio-loud quasar jets**: alpha ~ 0.5--1.0 (flat or slightly steep)
- **Radio-quiet AGN**: alpha ~ 1.5--2.0 (steep, indicating spectral curvature)
- **Free-free absorption**: alpha becomes frequency-dependent, with steepening at low frequencies (alpha increases toward lower nu)

LRDs with detections show:

$$\alpha \sim 1.5--2.5$$

and evidence for steepening below 1.4 GHz, consistent with free-free absorption.

---

## Key Results

1. **Radio Non-Detection**: ~95% of the LRD sample undetected at 1.4 and 3 GHz, with 5σ limits F < 3--5 μJy.

2. **Radio Loudness**: log R ~ -4 to -6, radio-extremely-quiet, far below typical AGN.

3. **Millimeter Detection**: Most sources detected by ALMA at 1.1--0.87 mm, F ~ 10--100 μJy.

4. **Millimeter-to-Radio Ratio**: F_mm / F_radio ~ 10--100, consistent with moderate free-free absorption.

5. **Spectral Index (when detected)**: alpha ~ 1.5--2.5, steep and showing low-frequency steepening indicative of absorption.

6. **Interpretation**: Radio weakness results from combination of intrinsic radio quietness (jet suppression due to chaotic accretion geometry) and free-free absorption in dense nuclear gas. Scenario 2 (absorption) contributes factor of 3--10x suppression; scenario 1 (intrinsic quietness) accounts for remaining 10--100x.

---

## Impact and Legacy

1. **Jet Physics Constraint**: Demonstrated that rapid accretion and/or chaotic mergers suppress jet launching, with implications for AGN feedback mechanisms.

2. **Radio-Quiet AGN in Early Universe**: Established that the early universe hosts abundant radio-quiet AGN, distinct from the canonical "radio-loud" population that dominates jet-feedback models.

3. **AGN Feedback Reassessment**: If LRDs represent a significant AGN population at z~4--8, and most are radio-quiet, then radio jets (traditional jet-feedback) may be less important for early-universe galaxy evolution than radiative/wind feedback.

4. **Free-Free Absorption at High-z**: Highlighted importance of free-free absorption in dense nuclear gas for interpreting high-z radio observations.

5. **Multi-Wavelength Consistency**: Validated the need for coordinated radio, millimeter, optical, and X-ray observations to construct coherent physical models of high-z AGN.

---

## Connection to Phonon-Exflation Framework

Radio properties of AGN depend on accretion disk physics, magnetic field amplification, and jet launching efficiency. These processes operate in the early-universe environment characterized by the phonon-exflation framework's predictions of H(z), rho(z), and T(z).

**Connections**:

1. **Merger Rates and Chaotic Accretion**: The prevalence of chaotic accretion (and thus radio-quiet AGN) depends on the merger rate, which is sensitive to structure clustering and growth rates. Phonon-exflation's prediction of d(delta)/dz affects merger frequency at z~4--8.

2. **Jet Feedback Efficiency**: If radio jets are suppressed in LRD-like objects, the AGN feedback budget is dominated by radiative winds and outflows rather than mechanical jets. The efficiency of these alternative feedback channels depends on gas properties (density, temperature, velocity), all affected by H(z).

3. **AGN Feedback and Galaxy Quenching**: Radio-quiet AGN may have different feedback impact on star formation than radio-loud AGN. The prevalence of radio-quiet AGN (as implied by LRD observations) affects the predicted star formation histories and galaxy evolution in the early universe—a key test of cosmological models.

4. **Magnetohydrodynamic Evolution**: Magnetic field amplification and jet launching depend on accretion disk turbulence and dynamo processes. The early-universe gas properties (temperature, density, ionization) predicted by phonon-exflation would affect magnetic field evolution.

**Intensity**: Medium. Radio properties of z~4--8 AGN provide constraints on AGN feedback modes and accretion physics that differentiate cosmological models, but the connection is primarily demographic (feedback role in galaxy evolution) rather than fundamental.

---

## Key Equations Summary

| Quantity | Equation | Value for LRDs |
|----------|----------|---|
| VLA 1.4 GHz Limit | 5-sigma detection threshold | F_limit ~ 3--5 μJy |
| Rest-frame 1.4 GHz Luminosity | $L = 4\pi d_L^2 F (1+z)^{1-\alpha}$ | ~ 10^{23} W Hz^{-1} |
| Radio Loudness Parameter | $R = L_{1.4\text{ GHz}} / L_{4400 A}$ | log R ~ -4 to -6 (radio-quiet) |
| Radio Spectral Index | $\alpha = \log(F_1 / F_2) / \log(\nu_2 / \nu_1)$ | ~ 1.5--2.5 (LRDs, steep) |
| Free-Free Absorption | $\tau_{ff} \propto \nu^{-2} T^{-3/2} N_e N_p$ | 0.1--1.0 at 1.4 GHz (moderate) |
| Jet Power (Blandford-Znajek) | $P_{jet} \propto a^2 B^2 M^2 \Omega^2$ | Suppressed for poorly-organized B |
| Millimeter Flux (ALMA 1.1 mm) | Dust continuum | ~ 10--100 μJy |
| Millimeter-to-Radio Ratio | $F_{mm} / F_{radio}$ | ~ 10--100 |
