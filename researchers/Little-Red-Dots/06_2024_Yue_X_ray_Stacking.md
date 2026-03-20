# Stacking X-Ray Observations of Little Red Dots: Implications for Their AGN Properties

**Author(s):** Minghao Yue, Adi Zitrin, Anna-Christina Eilers, and collaborators

**Year:** 2024

**Journal:** The Astrophysical Journal Letters (volume 974, article L26; arXiv:2404.13290)

---

## Abstract

This paper presents X-ray stacking analysis of 34 spectroscopically-confirmed Little Red Dots using archival Chandra observations. Despite individual X-ray non-detections, stacking of the sample yields tentative detections in soft (0.5--2 keV) and hard (2--8 keV) bands with 2.9σ and 3.2σ significance, strengthening to 4.1σ when combining both bands. However, critical comparison with standard AGN X-ray--optical correlations reveals that LRDs are substantially X-ray underluminous. The observed X-ray luminosity is ~1 dex (soft band) to ~0.3 dex (hard band) lower than predicted by the L_X--L_Hα scaling relation typical of local Type I AGN. This X-ray weakness challenges the simplest interpretation of LRDs as standard accreting black holes and suggests either (1) extreme dust obscuration with complete Compton-thick absorption, (2) intrinsically weak X-ray emission from super-Eddington accretion, or (3) contamination of the optical emission lines by stellar or shock ionization. The paper constraints highlight the need for multi-wavelength characterization to understand LRD AGN nature and accretion physics.

---

## Historical Context

X-ray observations have long served as a primary AGN diagnostic, complementary to optical spectroscopy. The X-ray--optical flux ratio (quantified by, e.g., the X-ray--to--Hα luminosity ratio, L_X/L_Hα) is relatively constant for AGN, reflecting the broad-line region ionization and accretion physics. Local Type I AGN (unobscured quasars) follow a well-established L_X--L_Hα relation:

$$\log(L_X / L_{H\alpha}) \approx \text{constant} \approx 2.0--2.5$$

By contrast, Type II (obscured) AGN typically have lower L_X due to dust and gas absorption. The ratio L_X/L_Hα thus serves as an obscuration diagnostic.

Early claims that Little Red Dots host accreting black holes rested on broad Hα detections (Greene et al., Matthee et al.). However, the optical emission lines alone do not uniquely establish AGN identity—stellar ionization from massive O/B stars or shock ionization in galaxy collisions can produce broad lines. X-ray observations provide an independent, high-energy diagnostic.

Chandra's archival data, accumulated over decades, includes many fields containing LRDs. Yue et al. recognized an opportunity to perform X-ray stacking: combining weak signals from multiple sources to achieve sufficient SNR for statistical constraints. This approach, common in mm-wave and infrared astronomy, was newly applied to constrain X-ray properties of faint high-z objects.

---

## Key Arguments and Derivations

### X-Ray Stacking Methodology

X-ray stacking averages signal across multiple sources to enhance detection significance. For each LRD with known position, Chandra X-ray photometry at the source location is extracted. The methodology involves:

1. **Image Extraction**: For each source, extract a small cutout (e.g., 30" x 30") centered on the position, from the full Chandra image in soft (0.5--2 keV) and hard (2--8 keV) bands.

2. **PSF Normalization**: Normalize to Chandra's point-spread function (PSF) such that a perfect point source would have unit counts. This corrects for off-axis PSF degradation.

3. **Median Stacking**: To minimize impact of bright contaminating sources or instrumental artifacts, stack using the median (rather than mean) of the normalized images.

4. **Significance Assessment**: The stacked image is analyzed to derive flux and significance (in units of sigma). Significance is estimated via:

$$\sigma = \frac{\langle F_{source} \rangle}{\sqrt{\langle \sigma_F^2 \rangle}}$$

where the sum is over all stacked images.

### Soft and Hard Band Detection

Results show:

- **Soft (0.5--2 keV)**: 2.9σ detection → flux F_soft ~ 10^{-16} erg cm^{-2} s^{-1}
- **Hard (2--8 keV)**: 3.2σ detection → flux F_hard ~ 10^{-17} erg cm^{-2} s^{-1}
- **Combined**: 4.1σ detection → enhanced significance

At z~4, these rest-frame fluxes correspond to luminosities:

$$L_X = 4 \pi d_L^2 \times f \times (1+z)^{\Gamma - 2}$$

where d_L is luminosity distance, f is observed flux, and the (1+z) factor accounts for redshift dimming and cosmological bandpass shift (with spectral index Gamma typically ~ 1.8--2.0 for AGN).

For a z=4 source with F_soft ~ 10^{-16} erg cm^{-2} s^{-1}:

$$L_{X,soft} \approx 10^{42}--10^{43} \, \text{erg/s}$$

### Comparison with L_X--L_Hα Relation

The standard AGN L_X--L_Hα relation (derived from local Type I AGN) is:

$$\log(L_X) = \alpha \, \log(L_{H\alpha}) + \beta$$

with typical values alpha ~ 1.0, beta ~ -5.0, yielding log(L_X/L_Hα) ~ 2.0--2.5.

For LRDs with measured L_Hα ~ 10^{43}--10^{44} erg/s, the local relation predicts:

$$L_{X,predicted} \sim 10^{45}--10^{47} \, \text{erg/s}$$

However, the observed stacked X-ray luminosity is:

$$L_{X,observed} \sim 10^{42}--10^{43} \, \text{erg/s}$$

The ratio is:

$$\frac{L_{X,observed}}{L_{X,predicted}} \sim 10^{-2}--10^{-4}$$

or roughly 100--10,000 times fainter than expected. This extreme X-ray weakness is the key result.

### Upper Limits and Obscuration Constraints

The Chandra 3σ X-ray upper limits (from non-detected individual sources) are:

- **Soft**: ~3 × 10^{-17} erg cm^{-2} s^{-1} per source (for 100 ks exposure)
- **Hard**: ~2 × 10^{-17} erg cm^{-2} s^{-1} per source

If LRDs were heavily Compton-thick (N_H > 10^{24} cm^{-2}), X-rays would be severely suppressed. The column density required to suppress the 2--8 keV flux by a factor of 100 is estimated via X-ray radiative transfer models:

$$N_H > 10^{24} \, \text{cm}^{-2}$$

This extreme obscuration is plausible for some AGN but would be detectable in submillimeter and far-infrared (thermal dust reradiation). Yet LRDs do not show extreme far-IR luminosity, creating tension.

### Alternative Explanations

1. **Super-Eddington Accretion**: Theory predicts that at lambda_Edd >> 1 (super-Eddington), the accretion disk structure differs from standard thin-disk geometry. A geometrically thick, radiatively inefficient accretion flow (RIAF) can intrinsically produce weaker X-rays relative to optical/UV continuum. X-ray weakness is then not obscuration but a genuine accretion physics effect.

2. **Non-AGN Origin of Broad Lines**: If broad Hα (and other lines) originate from stellar populations or shocks rather than black hole accretion, the lines would not correlate with X-ray output, explaining the L_X--L_Hα discrepancy.

3. **Measurement Systematics**: Possible contamination, redshift uncertainty, or SED modeling errors could inflate inferred L_Hα or underestimate L_X.

---

## Key Results

1. **Stacking Detection**: Soft and hard X-ray bands individually detected at 2.9--3.2σ, combined 4.1σ.

2. **X-Ray Luminosity**: L_X ~ 10^{42}--10^{43} erg/s (rest-frame, stacked sample average).

3. **X-Ray Weakness**: Observed X-ray flux is 100--10,000x fainter than predicted by local L_X--L_Hα relations.

4. **Spectral Hardness**: Soft-to-hard ratio suggests relatively hard spectrum (typical of absorbed AGN or hot accretion flows).

5. **Upper Limits**: Individual source upper limits consistent with stacked detection (~3σ), validating the stacking approach.

6. **Implications**: Rules out standard Type I AGN geometry; favors either extreme obscuration or super-Eddington accretion physics.

---

## Impact and Legacy

This X-ray stacking study catalyzed debate about LRD nature:

1. **AGN or Not?**: The X-ray weakness raised questions about whether all LRDs genuinely host AGN or if some broad-line detections stem from other ionization mechanisms.

2. **Obscuration Models**: Motivated development of extreme-obscuration models for high-z AGN, including geometrically thick accretion flows and dusty tori with high covering fractions.

3. **Super-Eddington Accretion Renewed Interest**: Revived theoretical and observational study of super-Eddington accretion, including its X-ray signatures.

4. **Multi-Wavelength Follow-up**: Sparked observational campaigns with ALMA, XMM-Newton, VLA, and others to obtain independent constraints on LRD properties.

5. **X-ray Stacking as Technique**: Validated X-ray stacking for constraining faint high-z populations, opening new methodological avenues.

---

## Connection to Phonon-Exflation Framework

X-ray observations of high-z AGN probe early-universe conditions including ionization state, accretion physics, and AGN demographics. The phonon-exflation framework predicts early-universe parameters (H(z), rho(z), T(z)) that would affect AGN formation and observable properties.

**Connections**:

1. **AGN Demographics**: The number and X-ray properties of z~4 AGN depend on black hole formation efficiency, which is sensitive to structure growth rates predicted by the cosmological model. Phonon-exflation's H(z) and d(delta)/dz would affect AGN abundance.

2. **Ionization and Reionization**: X-ray output from AGN contributes to the ionizing photon budget and soft-X-ray background. The phonon-exflation model's prediction of ionization history would constrain the required AGN X-ray output.

3. **Accretion Physics at High-z**: If LRD X-ray weakness is due to super-Eddington accretion (rather than obscuration), the prevalence of super-Eddington accretion at z~4 constrains black hole growth mechanisms and gas accretion rates—sensitive to the early-universe environment predicted by the cosmological model.

4. **Reheating Temperature**: The ionization parameter (ratio of ionizing photon flux to gas density) inferred from X-ray observations constrains the early-universe ionization state, which depends on reheating processes.

**Intensity**: Medium. X-ray properties of z~4 AGN provide constraints on AGN demographics and accretion physics that any cosmological framework must accommodate, but the connection is indirect (through AGN formation rates rather than fundamental NCG physics).

---

## Key Equations Summary

| Quantity | Equation | Value for LRDs |
|----------|----------|---|
| Soft X-ray Detection | Stacked flux, 0.5--2 keV | 2.9σ, F ~ 10^{-16} erg cm^{-2} s^{-1} |
| Hard X-ray Detection | Stacked flux, 2--8 keV | 3.2σ, F ~ 10^{-17} erg cm^{-2} s^{-1} |
| Rest-frame X-ray Luminosity | $L_X = 4\pi d_L^2 f (1+z)^{\Gamma - 2}$ | ~ 10^{42}--10^{43} erg/s |
| Local L_X--L_Hα Relation | $\log(L_X) = \alpha \log(L_Halpha) + \beta$ | alpha ~ 1.0, beta ~ -5.0 |
| Expected vs Observed | $L_{X,obs} / L_{X,pred}$ | ~ 10^{-2}--10^{-4} (100x--10,000x weak) |
| Compton-Thick Column | N_H for 100x suppression | > 10^{24} cm^{-2} |
| Significance (stacked) | $\sigma = \langle F \rangle / \sqrt{\langle \sigma_F^2 \rangle}$ | 4.1σ combined |
