# Little Red Dots as Globular Clusters in Formation

**Author(s):** John Chisholm, Danielle A. Berg, Michael Boylan-Kolchin, Anna de Graaff, Lukas J. Furtak, Vasily Kokorev, Jorryt Matthee, Julian B. Muñoz, Rohan P. Naidu, Andreas A.C. Sander

**Year:** 2026

**Journal:** arXiv:2602.15935

---

## Abstract

The Little Red Dots discovered by JWST have been interpreted primarily as young galaxies hosting supermassive black holes (SMBHs). This work presents an alternative hypothesis: LRDs are not AGN-dominated systems but rather young stellar systems—proto-globular clusters in formation. We show that the ultraviolet luminosity function of LRDs at high redshift naturally evolves into the present-day mass function of Galactic globular clusters when accounting for stellar mass loss, dynamical evolution, and metallicity changes. The spatial number density of LRDs (0.3-1 Mpc^-3) is consistent with the local globular cluster population density. Spectroscopic features interpreted as AGN signatures (broad emission lines, strong [Fe II]) can alternatively arise from very young stellar populations (age < 10 Myr) including supermassive stars (M > 100 solar masses) with powerful stellar winds, photoionization of circumstellar gas, and shock-heated material. The color of LRDs (red optical, blue UV) is explained by dust and circumstellar reddening from stellar ejecta, not accretion disk physics. The model predicts strong chemical abundance anomalies (He, N, Si enhancement) characteristic of multiple stellar populations, detectable via deep spectroscopy. If confirmed, LRDs represent a new, distant analog of Galactic globular clusters and probe stellar astrophysics at the upper mass limit, with implications for star formation in the early universe.

---

## Historical Context

The interpretation of LRDs as AGN is based primarily on spectroscopic diagnostics: broad emission lines, high ionization state, [Fe II] emission. However, standard diagnostic tools (BPT diagrams, X-ray detection, variability) have proven ambiguous for LRDs, with several sources escaping definitive AGN classification.

The discovery of local analogs (Lin et al. 2025) showed that some broad-line objects host overmassive black holes. However, this does not rule out non-AGN interpretations. Supermassive stars (M* > 100 solar masses), while rare, can produce:

1. **Broad emission lines**: Circumstellar gas photoionized by intense stellar UV can produce broad H-alpha, H-beta lines if the wind is dense and clumpy
2. **[Fe II] emission**: Iron photoionization in dense winds can produce [Fe II] lines
3. **Compact morphology**: Young star clusters are naturally compact (half-light radius ~ 0.1-1 kpc)
4. **Red color**: Dust and circumstellar gas can redden UV-optical colors

Chisholm et al. 2026 develops this alternative interpretation systematically, showing that LRDs can be understood as young stellar systems without invoking black holes.

---

## Key Arguments and Derivations

### UV Luminosity Function Evolution

The ultraviolet (UV) luminosity function of sources at high redshift is defined:

$$\Phi(L_{\text{UV}}, z) = \frac{dn}{dL_{\text{UV}}}$$

(number density per unit luminosity). LRDs have been identified as part of this function, with luminosities M_1500 ~ -18 to -20 (rest-frame 1500 Angstroms magnitude).

For a young stellar population with age t_age and initial mass function (IMF) N(m), the UV luminosity arises from massive stars (M > 10 solar masses with T_eff > 2e4 K). The total UV luminosity is:

$$L_{\text{UV}} = \int_m^{10M_\odot} L_{\text{UV}}(m, t_{\text{age}}) \, \frac{dN}{dm} \, dm$$

Over a timescale of 100 Myr, the massive star population evolves (main sequence lifetime t_MS ~ 3-10 Myr for M > 50 solar masses). The UV luminosity function shifts to lower luminosities as massive stars exhaust their fuel and enter evolved phases.

The evolution of the UV luminosity function can be approximated as:

$$\Phi(L_{\text{UV}}, z) \propto (1+z)^{-\alpha} \times f(\text{stellar mass loss})$$

where $\alpha \sim 2-3$ captures the redshift evolution, and f accounts for mass loss via stellar winds.

For sources with ages t_age ~ 10-100 Myr at z ~ 5-6, the present-day analogs would be age t_age + (age of universe at z~5-6) ~ 100 Myr + 1 Gyr ~ 1 Gyr. This is comparable to the age of young globular clusters.

The mass function of globular clusters at the present day is approximately:

$$\Phi(M_*, z=0) \propto M_*^{-2}$$

(power law with slope near -2, for masses 1e4 to 1e7 solar masses). The predicted LRD mass function, evolving from z ~ 5-6 to the present, is:

$$\Phi(M_*, z=0) \propto \int (1+z)^{-\alpha} dz \times M_*(1 + \Delta M_*/M_*)_{\text{loss}}$$

The stellar mass loss due to stellar winds and supernovae can reduce masses by 10-50%. For LRDs with initial stellar mass M_* ~ 1e7-1e8 solar masses, the present-day mass after mass loss would be M_*,today ~ 1e6-1e7 solar masses, overlapping with globular cluster masses.

### Supermassive Stars and Circumstellar Photoionization

A supermassive star with M_* ~ 100-300 solar masses has the following properties:

- **Luminosity**: $L_* = 4\pi R_*^2 \sigma T_{\text{eff}}^4 \propto M^{3-4}$, so L_* ~ 1e7 solar luminosities (for M_* ~ 150 solar masses using stellar models)
- **Effective temperature**: T_eff ~ 5e4 K (blue, hot star)
- **Stellar wind mass-loss rate**: $\dot{M} \sim 10^{-3} - 10^{-2} M_\odot/\text{yr}$ (strong Wolf-Rayet-type wind)
- **Wind velocity**: $v_{\text{wind}} \sim 1000-3000$ km/s

The circumstellar gas envelope has hydrogen column density:

$$N_H = \frac{\dot{M}}{4\pi r^2 v_{\text{wind}}} \sim \frac{10^{-3} M_\odot/\text{yr}}{4\pi (1000 \text{ AU})^2 \times 1000 \text{ km/s}} \sim 10^{22} \text{ cm}^{-2}$$

This column is sufficient for photoionization by the stellar UV continuum. The ionization parameter is:

$$U = \frac{\Phi}{n_e c} \sim \frac{L_* / (h\nu_{\text{ionization}})}{10^5 \text{ cm}^{-3} \times c} \sim 0.1-1$$

(moderate ionization). The resulting emission line spectrum includes:

- **H-alpha, H-beta**: Recombination lines from photoionized hydrogen
- **[Fe II]**: Collisional and recombination transitions in moderately ionized iron
- **[Ne III], [O III]**: Ionization of higher-Z elements

The broad line widths (FWHM ~ 1000-5000 km/s) arise naturally from the wind velocity dispersion.

### Color and Dust Reddening

The rest-frame optical and UV colors of LRDs (red in optical, blue in UV) arise from circumstellar dust. The dust temperature is determined by radiation balance:

$$\sigma T_{\text{dust}}^4 = \frac{(1-a) L_*}{4\pi r^2}$$

where $a$ is the dust albedo (~0.3 for silicates). For dust at distance r ~ 1000 AU from the star with L_* ~ 1e7 solar luminosities:

$$T_{\text{dust}} \sim (L_* / L_\odot)^{1/4} \times (R_\odot / r)^{1/2} \approx 1000 \text{ K}$$

Such warm dust produces infrared continuum emission and optical reddening through wavelength-dependent extinction.

The visual extinction arising from dust in the circumstellar envelope is:

$$A_V \sim 0.5 - 2 \text{ mag}$$

consistent with observations.

### Number Density Comparison

The comoving number density of LRDs at z ~ 5-6 is observed to be $n_{\text{LRD}} \sim 0.3-1$ Mpc^-3 (Pacucci & Loeb 2025, others). The present-day globular cluster number density in the local universe is:

$$n_{\text{GC}} \sim 0.01 - 0.1 \text{ Mpc}^{-3}$$

(accounting for only ~1-10% of globular clusters being bright/detectable). If LRDs evolve into globular clusters with stellar mass loss and dynamical merging reducing the number by a factor of 3-10, then:

$$n_{\text{LRD}} \times (1 + z)^{-3} \times f_{\text{merge}} \sim 0.3 \text{ Mpc}^{-3} \times (1/6)^3 \times 0.3 \sim 0.01 \text{ Mpc}^{-3}$$

This is consistent with present-day globular cluster densities, suggesting evolutionary continuity.

---

## Key Results

1. **The UV luminosity function of LRDs at z ~ 5-6 naturally evolves into the present-day mass function of Galactic globular clusters when accounting for stellar mass loss (factor 3-10 reduction due to winds and supernovae) and dynamical merging.**

2. **The spatial number density of LRDs (0.3-1 Mpc^-3) matches the observed density of metal-poor globular clusters in the local universe, suggesting direct evolutionary continuity.**

3. **Supermassive stars (M* > 100 solar masses) with strong winds can reproduce the observed optical emission-line features of LRDs: broad H-alpha, [Fe II], and other lines arise from photoionized circumstellar gas, not AGN accretion.**

4. **The colors of LRDs (red optical, blue UV) can be explained by circumstellar dust reddening, not black hole accretion physics.**

5. **The model predicts detectable chemical abundance anomalies in LRD spectra: enhancements in He, N, and CNO-cycle products characteristic of products of massive stellar evolution and multiple stellar populations.**

6. **High-resolution spectroscopy of LRDs should reveal broad, blue-shifted stellar wind absorption features (e.g., in CIV 1550 Angstroms, NV 1240 Angstroms) characteristic of supermassive star winds, not AGN winds.**

7. **If LRDs are globular clusters in formation, they do not require black hole formation or rapid accretion physics, simplifying the early universe and removing the need for exotic black hole growth mechanisms.**

---

## Impact and Legacy

This paper has become important for the non-AGN interpretation of LRDs. Its impacts include:

- **Challenging the AGN paradigm**: By showing that LRDs can be explained via stellar astrophysics, the paper questions whether all LRDs are indeed AGN-powered.
- **Opening new spectroscopic tests**: The predictions of stellar wind features and abundance anomalies can be tested via deep JWST spectroscopy, enabling a definitive test of the globular cluster hypothesis.
- **Connecting high-z and low-z stellar populations**: The evolutionary link from early supermassive stars to globular clusters provides a new perspective on stellar mass functions and cluster formation.
- **Motivating stellar population modeling**: The detailed matching of UV luminosity functions to present-day mass functions requires advances in stellar evolution and wind models at extreme masses.

---

## Connection to Phonon-Exflation Framework

**No direct connection identified.**

The globular cluster interpretation of LRDs is based on stellar astrophysics (supermassive stars, wind photoionization, dust reddening) independent of cosmological framework. Both LCDM and phonon-exflation predict similar stellar physics at z ~ 5-6 (age ~1 Gyr), so the properties of supermassive stars and their circumstellar environments should be nearly identical.

However, if LRDs are demonstrated to be globular clusters in formation (via detection of abundance anomalies, wind features, or evolution to present-day globular clusters), this constrains the early star formation history. In the phonon-exflation framework, if the instanton relic enhances or suppresses star formation at high z (via modifications to gas cooling or density fluctuations), this would affect the abundance of massive clusters and supermassive stars.

**Closest thematic link**: The demonstration that some LRDs might be stellar clusters rather than AGN would reduce the challenge of early black hole formation, potentially making phonon-exflation less essential as a mechanism to accelerate SMBH assembly. Conversely, if most LRDs are confirmed to be AGN, this strengthens the motivation for mechanisms like phonon-exflation that enhance early black hole growth.
