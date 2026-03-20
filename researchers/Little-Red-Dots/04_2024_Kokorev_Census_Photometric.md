# A Census of Photometrically Selected Little Red Dots at 4 < z < 9 in JWST Blank Fields

**Author(s):** Vasily Kokorev, Gabriel Brammer, Ivo Labbe, Erica Nelson, and collaborators

**Year:** 2024

**Journal:** The Astrophysical Journal (volume 962, article 129; arXiv:2401.09981)

---

## Abstract

This comprehensive census identifies and characterizes 260 candidate Little Red Dots (LRDs) selected photometrically from JWST/NIRCam deep-field imaging covering approximately 640 square arcminutes of blank sky. Unlike spectroscopic surveys limited to small, confirmed samples, this photometric approach yields large statistical samples enabling robust demographic studies. The selection exploits the distinctive V-shaped spectral energy distribution (SED) characteristic of LRDs: blue rest-frame UV continua (m_UV ~ -18 to -22) combined with red rest-frame optical slopes and compact morphologies (r_e < 500 pc). Quasar model fitting reveals moderate dust extinction (A_V ~ 1.6 mag) and bolometric luminosities L_bol ~ 10^{44}--10^{47} erg/s. The derived space density of dusty AGN candidates reaches approximately 10^{-5}--10^{-4} cMpc^{-3} at z=4--9, roughly 100 times higher than the comoving density of optically-selected quasars of comparable luminosity at similar redshifts. This 100x abundance enhancement fundamentally revises AGN demographics in the early universe and demonstrates that dust-enshrouded black hole growth dominates over optically-unobscured accretion in the first billion years after the Big Bang.

---

## Historical Context

Prior to JWST, AGN census at high redshift relied primarily on three detection channels: (1) optical/UV selection from broad-band photometry (SDSS, BOSS, etc.), (2) X-ray selection from Chandra and XMM-Newton surveys, and (3) mid-infrared selection from Spitzer and later WISE. Each method has inherent biases.

Optical selection (method 1) is insensitive to heavily dust-obscured AGN. X-ray selection (method 2) misses Compton-thick sources and AGN with intrinsically weak X-ray emission. Mid-IR selection (method 3) partially overcomes optical bias but was limited to brighter objects by Spitzer's modest sensitivity.

JWST, with its superior infrared sensitivity and high angular resolution, enabled a new selection channel: rest-frame optical/near-infrared colors sensitive to dust attenuation and AGN continuum shape. Kokorev et al. recognized that the distinctive V-shaped SED of LRDs—blue UV, red optical, compact—provides a powerful photometric diagnostic. Unlike spectroscopy (which confirms a handful of objects at high SNR) or X-ray data (which has limited sky coverage and sensitivity), NIRCam multi-band photometry allows statistical selection of hundreds of candidates across deep JWST fields.

The team conducted a systematic study of multiple deep JWST/NIRCam fields (GOODS-S, GOODS-N, COSMOS, and others) with depths reaching 29--31 AB magnitude in multiple bands. The resulting sample is the largest photometrically-defined LRD census to date.

---

## Key Arguments and Derivations

### Photometric Selection Criteria

The LRD selection relies on specific color cuts designed to isolate the V-shaped SED:

**Color Criteria**:
1. **Blue UV**: Rest-frame UV colors consistent with recent star formation or AGN continuum. Typically, selection requires F150W or F200W magnitude sufficiently bright relative to longer-wavelength bands.
2. **Red Optical**: A sharp drop in flux between ~1000 nm and ~2500 nm (rest-frame at z~5) indicates dust reddening. Selection requires, e.g., F277W > F444W or equivalent color.
3. **Compact Morphology**: Effective radii measured from 2D image modeling must satisfy r_e < 500 pc to exclude extended galaxies.
4. **Photometric Redshift Range**: 4 < z_phot < 9, ensuring objects are in the z>4 epoch of interest.

Mathematical expression (illustrative):

$$\text{LRD Candidate if:} \quad m_{UV} < 23, \, m_{opt} - m_{IR} > 0.5, \, r_e < 500 \, \text{pc}, \, 4 < z_{phot} < 9$$

Specific values vary by author and field depth, but the essence is color contrast across the Balmer break region.

### SED Fitting and Property Extraction

For each photometric candidate, the observed SED is fitted to composite models consisting of:
1. **Stellar continuum**: From stellar population synthesis (SPS) codes (e.g., FSPS, BC03)
2. **AGN continuum**: Power-law component representing the accretion disk and other emission
3. **Dust attenuation**: Using a reddening law, typically characterized by A_V or equivalent E(B-V)

The combined model is:

$$f_\lambda = a \cdot f_\lambda^{SPS}(M_*, \text{age}, Z) + (1-a) \cdot f_\lambda^{AGN} \, \times \, A(\lambda, A_V)$$

where a is the fractional contribution of stellar versus AGN light, A(lambda, A_V) is the dust attenuation factor (e.g., Calzetti law), and other parameters are fitted via chi-2 minimization.

Typical best-fit results:
- **Dust Extinction**: A_V ~ 1.6 mag (range 1.0--2.5)
- **AGN Fraction**: AGN dominates optical/near-IR, contributing 50--90% of restframe optical flux
- **Stellar Mass**: M_* ~ 10^9--10^{11} M_sun
- **Bolometric Luminosity**: L_bol ~ 10^{44}--10^{47} erg/s

### Number Density Calculation

The comoving number density is estimated via:

$$n(z, L_{bol}) = \frac{N(z, L_{bol}, \Delta L)}{V_{comoving}}$$

where N is the observed count in a luminosity interval Delta L within a redshift bin Delta z, and V_comoving is the comoving volume surveyed:

$$V_{comoving}(z_1, z_2, \Omega) = \frac{c}{H_0} \int_{z_1}^{z_2} \frac{d\chi}{dz} \, \Omega \, dz$$

where d chi/dz is the comoving distance element and Omega is the survey solid angle in steradians.

For the Kokorev survey, Omega ~ 1.5 x 10^{-5} steradians (640 arcmin^2) across z=4--9 yields:

$$V_{comoving} \sim 10^6 \, \text{Mpc}^3$$

With N ~ 260 LRD candidates across multiple redshift bins, the number density is approximately:

$$n_{LRD} \sim 10^{-5} \text{ to } 10^{-4} \, \text{cMpc}^{-3}$$

(the exact value depends on the redshift bin and completeness corrections applied)

### Comparison with UV-Selected Quasars

The space density of UV-selected quasars at z~5 of comparable bolometric luminosity (L_bol ~ 10^{45}--10^{46} erg/s) is:

$$n_{UV-qso} \sim 10^{-6}--10^{-5} \, \text{cMpc}^{-3}$$

Thus the ratio is:

$$\frac{n_{LRD}}{n_{UV-qso}} \sim 1--10$$

However, when restricting to dusty AGN (A_V > 1), the gap widens to a factor of ~100, establishing LRDs as 100x more abundant than similarly dusty optically-selected AGN.

### Cumulative Number Density

The integrated number density (summed over all luminosities) at z~4--9 is:

$$n_{LRD, total} \sim 10^{-4}--10^{-3} \, \text{cMpc}^{-3}$$

suggesting that dusty AGN broadly define the AGN census in the early universe, not the optically-bright quasars familiar from SDSS.

---

## Key Results

1. **Large Statistical Sample**: 260 photometrically-selected LRD candidates, enabling robust demographic analysis (versus spectroscopic samples of ~20--50 objects).

2. **Spatial Distribution**: LRDs are found across the surveyed fields with no obvious clustering, suggesting they are distributed throughout cosmic structures at z~4--9.

3. **Dust Properties**: Typical A_V ~ 1.6 mag, consistent with significant dust in nuclear regions or extended circumnuclear envelopes.

4. **Bolometric Luminosity Range**: L_bol ~ 10^{44}--10^{47} erg/s spans from sub-Eddington to super-Eddington accretion for plausible black hole masses.

5. **Number Density**: n_LRD ~ 10^{-5}--10^{-4} cMpc^{-3}, roughly 100x higher than UV-selected quasars of matched luminosity.

6. **AGN Fraction**: Most LRDs show AGN dominance in optical-NIR (AGN contributes 50--90% of continuum).

7. **Photometric Completeness**: Sample is limited by survey depth (m_limit ~ 30 AB); fainter populations remain undetected.

---

## Impact and Legacy

The Kokorev census fundamentally changed AGN demographic understanding:

1. **Dust Obscuration Essential**: Established that accounting for dust-obscured AGN increases the z>4 AGN density by an order of magnitude, making obscured accretion the dominant mode in the early universe.

2. **Reionization Implications**: The high number density of LRDs, if they are predominantly AGN, means the AGN contribution to ionizing photons during reionization is higher than previously thought.

3. **Black Hole Growth Dominantly Obscured**: Suggests that most early black hole growth occurred in dusty environments, consistent with "obscured growth" phase models.

4. **Formation Mechanism Pressure**: The abundance of z~4--9 LRDs creates tension with many proposed formation mechanisms (direct collapse black holes, stellar-mass black hole seeds). The high number density must be accommodated by formation theories.

5. **Photometric Selection Viability**: Demonstrated that photometric methods can identify large AGN populations reliably, opening new discovery avenues for future surveys.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework predicts a specific expansion history H(z) and structure growth rate. The LRD census—measuring AGN number density and luminosity distribution at z=4--9—provides empirical constraints on early-universe AGN formation rates.

**Connections**:

1. **AGN Production Rate**: The phonon-exflation model's prediction of density contrast growth d(delta)/dz affects the rate at which overdensities sufficient to trigger black hole formation emerge. The observed LRD abundance would constrain this growth rate.

2. **Black Hole Seeding Efficiency**: Different cosmologies predict different seeding efficiencies (fraction of halos that host black holes). The LRD number density constrains seeding efficiency as a function of halo mass and redshift.

3. **Dust and Metallicity Evolution**: The prevalence of dust in LRDs (A_V ~ 1.6 mag) is related to metallicity and star formation history, which depend on the early-universe star formation rate history—sensitive to H(z) and structure growth.

4. **Ionizing Photon Budget**: The LRD census contributes to the cosmic ionizing photon budget, affecting reionization history predicted by the phonon-exflation model.

**Intensity**: Medium--High. The LRD number density at z~4--9 is a direct, quantitative constraint on early-universe AGN formation that any cosmological framework must reproduce. The connection is primarily demographic and structural rather than fundamental physics, but it is measurable and testable.

---

## Key Equations Summary

| Quantity | Equation | Typical Value |
|----------|----------|---|
| LRD Selection (colors) | Blue UV, red optical, compact morphology | See selection criteria |
| SED Model | $f_\lambda = a \cdot f^{SPS} + (1-a) \cdot f^{AGN} \cdot A(\lambda, A_V)$ | A_V ~ 1.6 mag |
| Number Density (single z-bin) | $n = N / V_{comoving}$ | 10^{-5}--10^{-4} cMpc^{-3} |
| Ratio (LRD to UV-qso) | $n_{LRD} / n_{UV-qso}$ | ~ 10--100 |
| Comoving Volume | $V = \frac{c}{H_0} \int \frac{d\chi}{dz} \Omega \, dz$ | ~ 10^6 Mpc^3 for 640 arcmin^2 survey |
| Bolometric Luminosity | L_bol (from SED fitting) | 10^{44}--10^{47} erg/s |
| Dust Extinction | A_V | 1.6 mag (range 1.0--2.5) |
