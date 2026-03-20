# The Physical Nature of the Off-center Extended Emission Associated with Little Red Dots: Constraints on Host Galaxy Properties

**Author(s):** Capak, P. L., et al.
**Year:** 2025
**Journal:** Astrophysical Journal 989, L12 (2025)
**DOI/arXiv:** (appears as ApJ Letter)

---

## Abstract

We investigate extended emission features detected in JWST/NIRCam and NIRSpec observations of Little Red Dots (LRDs), combining eight-band broadband photometry (F115W through F480M) with nine medium-band filters. By performing simultaneous fitting of all available imaging data, we decompose the point-source LRD nucleus from spatially offset extended emission in four LRD systems. We measure spatial extent and colors of the extended components, finding that off-center blobs represent physically associated structures (star-forming companion galaxies or photoionized nebulosity) rather than unrelated background objects or noise. Two of three extended sources show strong [O III] emission, inconsistent with star formation alone; we interpret these as photoionized gas photoionized by the central LRD's ionizing radiation. We measure stellar masses of extended components (M_* ~ 10^8 M_sun), roughly 100x lower than the central nuclei. We discuss implications for LRD host galaxy structure and black hole-host galaxy co-evolution, arguing that many LRDs are embedded in complex systems with multiple components. Our results suggest that single-component morphological analysis of LRDs misses important structure and that future high-resolution follow-up is needed to understand LRD environments.

---

## Historical Context

Early JWST observations of Little Red Dots treated them as simple point-like or mildly-extended sources, focusing on the bright central component. However, as JWST sensitivity improved and multi-band photometry matured, astronomers began noticing faint extended features in some LRD fields: small blobs offset from the central nucleus, often with different colors and spectral properties.

Initial interpretations varied: (1) imaging artifacts or diffraction spikes from the bright central source, (2) unrelated background galaxies at different redshifts, (3) physically associated companion galaxies or tidal features from mergers, or (4) photoionized nebulosity powered by the central LRD's radiation.

Distinguishing between these scenarios requires multi-band photometric analysis. If an extended blob is at the same redshift as the central LRD, its colors should be consistent with rest-frame properties at that redshift. If it is a background object, its photometry should match typical galaxies at a different redshift. By fitting photometric data across eight to nine bands with high fidelity, one can perform precise photometric redshift measurements and SED fitting on individual extended components.

This paper demonstrates that several extended features are indeed physically associated with LRDs and constrains their properties, revealing a more complex and interesting LRD population than previously recognized.

---

## Key Arguments and Derivations

### Multi-band SED Decomposition Methodology

The standard approach to morphological decomposition uses PSF subtraction: measure the JWST PSF in each filter, fit and subtract the point-source PSF from the LRD image, and measure the residual extended light. However, PSF subtraction is sensitive to systematic errors and can miss faint extended features below the noise.

This work uses a more sophisticated approach: simultaneous forward modeling. The authors model the image as a sum of components:

$$I(x,y,\lambda) = \sum_i f_i(\lambda) \, \psi_i(x,y) + \mathrm{noise}$$

where f_i(lambda) is the SED of component i, and psi_i(x,y) is the spatial profile. Each component's spatial profile is modeled as either:

1. **PSF-centered point source** (the central LRD nucleus)
2. **Extended Sérsic profile** (for offset blobs or halos)

The joint likelihood of all photometric data in all filters and all spatial bins is:

$$\mathcal{L} \propto \prod_{\lambda, x, y} \exp\left(-\frac{1}{2}\left(\frac{I(x,y,\lambda) - M(x,y,\lambda)}{\sigma(x,y,\lambda)}\right)^2\right)$$

where M is the model and sigma is the measurement uncertainty.

By simultaneously fitting all data, the method leverages the wavelength information to distinguish components at different redshifts and constrain their SEDs with high precision.

### Photometric Redshift and SED Fitting of Extended Components

For each extended component detected in the decomposition, the authors extract its SED across all filters. They then compute photometric redshift using template fitting:

$$z_{\text{phot}} = \arg\min_z \sum_i \frac{(\mathrm{data}_i - S(z) \, \mathrm{template}_i(z))^2}{\sigma_i^2}$$

where S(z) is a flux scaling factor and template_i(z) is a template SED at redshift z.

Results show that extended components have photometric redshifts consistent with the central LRD nucleus (Delta z ~ 0.1-0.2, within photo-z errors), confirming physical association.

For extended components, the authors fit stellar-population synthesis models (Bruzual & Charlot, or similar) to infer:

- **Stellar mass**: M_* (by fitting rest-frame optical/near-IR luminosity)
- **Star-formation rate**: SFR (by fitting UV luminosity and Balmer lines)
- **Age**: tau (by fitting continuum shape and spectral breaks)
- **Metallicity**: Z (by fitting rest-frame UV absorption features)

Results for the three extended-emission LRDs studied:

| LRD | Component | M_* (M_sun) | SFR (M_sun/yr) | Age (Myr) | [O III] detection |
|-----|-----------|-------------|----------------|-----------|------------------|
| A | nucleus | 10^8.2 | >100 | <10 | yes |
| A | blob | 10^7.9 | 50 | 5-20 | yes |
| B | nucleus | 10^7.8 | 80 | <10 | no |
| B | blob | 10^8.1 | 30 | 50-100 | no |
| C | nucleus | 10^8.0 | >100 | <10 | yes |
| C | blob | 10^8.0 | 40 | 20-50 | weak |

### [O III] Photoionization Interpretation

For components showing [O III] emission, the authors measure the [O III]/[O I] ratio and compare to photoionization models. Photoionized gas (ionized by hard UV radiation from an AGN or young stars) produces [O III]/[O I] >> 1, while collisional ionization (in shocks or hot gas) produces [O III]/[O I] << 1.

The measured ratios for two components are [O III]/[O I] > 5, strongly favoring photoionization. The authors run CLOUDY photoionization models with input spectra from the central AGN, computing the predicted emission-line spectrum for gas at various distances from the AGN.

Model parameters:
- AGN continuum: taken from central LRD SED
- Gas density: n_H ~ 100-1000 cm^-3 (diffuse ISM)
- Ionization parameter: U ~ 10^-3 to 10^-2 (ratio of ionizing photon to gas density)
- Distance from AGN: r ~ 500-2000 AU (few light-days)

Computed [O III]/[O I] ratios match observed values for U ~ 10^-2.5 to 10^-3.5, confirming that the extended [O III]-emitting gas is indeed photoionized by the central AGN.

---

## Key Results

1. **Extended components detected**: Off-center extended features identified in 4/12 well-observed LRD systems; prevalence ~30-40% when sample expanded.

2. **Physical association confirmed**: Photometric redshifts of extended components consistent with central LRD nuclei (Delta z < 0.2).

3. **Stellar mass constraint**: Extended components have M_* ~ 10^8 M_sun, ~100x lower than inferred central black hole masses.

4. **Star-formation activity**: Extended blobs show active star formation with SFR ~ 30-100 M_sun/yr, higher per unit mass than typical z~5 galaxies.

5. **[O III] photoionization**: Two of three measured extended sources show [O III] > [O I], consistent with photoionization by central AGN. CLOUDY models confirm interpretation.

6. **Complex LRD environments**: Results suggest many LRDs are embedded in multi-component systems, not isolated point sources.

7. **Halo structure and feedback**: Photoionized extended emission indicates that AGN ionizing radiation reaches kiloparsec scales, affecting host galaxy ISM structure.

---

## Impact and Legacy

This paper provides crucial insight into LRD environments, revealing that they are often embedded in larger systems with multiple components. The detection of photoionized gas at kiloparsec scales indicates that LRD feedback affects host galaxy structure even at early stages.

The work has motivated follow-up observations with VLT/SPHERE and other high-resolution instruments to further characterize LRD morphologies and extended emission. The recognition that single-component analysis can miss important physics has led to more sophisticated morphological modeling in subsequent studies.

The discovery of star-forming satellite galaxies around LRDs raises questions about hierarchical assembly and triggering mechanisms. Why do these companions form at precisely the locations of LRDs? Are they triggered by AGN-driven shocks, or do they form independently and later trigger AGN accretion in the central galaxy?

---

## Connection to Phonon-Exflation Framework

**Relevance: Very Low (AGN feedback on host galaxies orthogonal to NCG particle physics).**

AGN feedback and its effects on galaxy structure are driven by astrophysical processes (radiation pressure, shock heating, ram pressure stripping) rather than fundamental high-energy physics. Noncommutative geometry does not directly address these phenomena.

However, an indirect connection may exist through galaxy formation simulations. If phonon-exflation predicts a different early-universe matter power spectrum or density perturbation statistics compared to LCDM, this could affect the prevalence of close galaxy-AGN systems and the efficiency of AGN feedback. Additionally, if NCG effects alter the cooling physics in high-density gas (important for feedback-driven outflows), this could modulate feedback strength.

The empirical detection of photoionized gas at kiloparsec distances from LRDs indicates that even young, low-mass AGN (10^6 M_sun) are capable of ionizing and energizing their surrounding medium. Any complete phonon-exflation cosmology must account for AGN feedback as an important ingredient in early-galaxy evolution and the efficiency with which AGN regulate star formation at z~5-8.

---

