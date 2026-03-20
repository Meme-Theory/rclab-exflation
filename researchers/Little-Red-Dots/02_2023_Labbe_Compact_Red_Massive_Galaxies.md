# Sizes and Mass Profiles of Candidate Massive Galaxies Discovered by JWST at 7<z<9: Evidence for Very Early Formation of the Central ~100 pc of Present-day Ellipticals

**Author(s):** Ivo Labbe, Gabriel Brammer, Pieter van Dokkum, Joel Leja, Erica Nelson, Sedona Price, and colleagues

**Year:** 2023

**Journal:** The Astrophysical Journal Letters (volume 951, article L35)

---

## Abstract

This groundbreaking paper reports the discovery of a population of extremely compact, massive galaxies at redshifts z=7--9 using JWST/NIRCam imaging. The authors select 13 candidate galaxies with stellar masses M* ~ 10^10--10^11 M_sun based on photometric redshifts and NIRCam colors. Structural analysis using 2D image modeling reveals effective radii r_e ~ 80--300 pc (mean ~150 pc), making these objects 10--20 times more compact than low-redshift elliptical galaxies of comparable mass. The paper argues that these galaxies represent the early-assembled cores of present-day massive ellipticals, suggesting that galaxy bulges formed extremely rapidly within the first 500--700 Myr after the Big Bang. The discovery challenges conventional hierarchical galaxy formation models and raises the question of whether the assembled stellar mass formed in situ or was assembled through high-redshift mergers within a very short timescale.

---

## Historical Context

Prior to JWST, high-redshift galaxy morphology and structure were accessible only through Hubble Space Telescope (HST) observations, which had limited sensitivity at z>4 and were restricted to rest-frame UV and optical wavelengths. Ground-based spectroscopy of z>6 galaxies was extremely difficult, so photometric redshifts dominated. The conventional picture, grounded in cold dark matter simulations and hierarchical assembly scenarios, predicted that massive ellipticals grew through numerous mergers over cosmic time, gradually assembling their mass. Thus, the most massive objects should be found at low redshift (z<1), not in the early universe.

However, early JWST observations revealed an unexpected surprise: compact, red sources appeared common at z>6. Were these truly massive galaxies at z>8, or were they lower-redshift dusty galaxies that mimicked high-z colors? The answer required detailed morphological analysis and, ideally, spectroscopic confirmation.

Labbe et al., using the first wave of JWST/NIRCam deep imaging from the JWST Advanced Deep Extragalactic Survey (JADES) and other programs, conducted a systematic morphological analysis of photometrically-selected massive candidates. Their work was pivotal in establishing that at least some compact red sources are indeed high-redshift massive galaxies—not lower-z interlopers—and that their sizes are anomalously small.

---

## Key Arguments and Derivations

### Photometric Redshift Estimation

The authors employ multi-band NIRCam photometry spanning from 0.6 μm (F600W) to 5 μm (F480M), supplemented by HST optical data and ground-based longer-wavelength data where available. Photometric redshifts z_phot are derived by fitting observed SEDs to a grid of stellar population synthesis (SPS) models:

$$\chi^2 = \sum_{i=1}^{N_{bands}} \left[ \frac{f_{obs,i} - f_{model,i}(z, M_*, \text{age}, Z, A_V)}{sigma_{f,i}} \right]^2$$

where f_obs,i are observed fluxes, f_model are SPS-predicted fluxes, and sigma_f are flux uncertainties. Models span ages 50 Myr to 13.8 Gyr, metallicities Z = 0.02--2.5 Z_sun, and dust attenuations A_V = 0--4 mag. The resulting photometric redshifts cluster around z~7--9 for the candidate sample.

### Morphological Analysis and Size Measurement

Each galaxy is modeled using 2D image modeling software (e.g., GALFIT or equivalent), fitting Sérsic profiles:

$$I(r) = I_e \, \exp \left[ -b_n \left( \left(\frac{r}{r_e}\right)^{1/n} - 1 \right) \right]$$

where r_e is the effective radius (enclosing half the light), n is the Sérsic index (n=1 for exponential, n=4 for de Vaucouleurs, n>4 for more concentrated profiles), and b_n is a normalization constant depending on n.

Key findings:
- **Effective Radii**: r_e ~ 80--300 pc (mean ~150 pc)
- **Sérsic Indices**: n ~ 3--5, indicating relatively concentrated profiles
- **Stellar Mass Surface Density**: M_*/π r_e^2 ~ 10^{10} M_sun / (π × (150 pc)^2) ~ 1.4 × 10^5 M_sun/pc^2

This surface density is comparable to the nuclei of present-day elliptical galaxies, despite existing at a much earlier epoch.

### Size Evolution Comparison

Comparing with local (z~0) elliptical galaxies of similar mass reveals a dramatic size difference. The mass-size relation at z~0 is approximately:

$$\log(r_e / \text{kpc}) \approx 0.55 \, \log(M_*/M_{\odot}) - 5.0$$

For M_* = 10^{10.5} M_sun (10^10.5 M_sun), this predicts r_e ~ 3 kpc at z=0. At z~8, the measured sizes are ~150 pc = 0.15 kpc, or ~20 times smaller at fixed mass. The implication: either (1) galaxies grew in size as they assembled more stellar mass (size-mass relation evolution), or (2) the earliest massive galaxies formed in very dense environments and have retained compact cores to the present day.

### Stellar Mass Estimates

Stellar masses are derived from SED fitting via the stellar mass-to-light ratio:

$$M_* = M/L \cdot L$$

where M/L depends sensitively on age and metallicity. The authors find M* ~ 10^{10}--10^{11} M_sun, higher than the Milky Way (M_* ~ 6 × 10^{10} M_sun) but comparable to M87 or other giant ellipticals.

### Cosmic Context and Lookback Time

At z=8, the cosmic age is:

$$t(z=8) \approx 0.63 \, \text{Gyr}$$

(from numerical integration of the Friedmann equation with Planck 2018 LCDM cosmology; the matter-dominated approximation $t \approx 2/(3 H_0 (1+z)^{3/2})$ gives ~0.35 Gyr, underestimating because $\Omega_m < 1$). Thus, these galaxies have assembled ~10^{10.5} M_sun of stars within ~600 Myr of the Big Bang. The implied star formation rate history is highly compressed and intense.

---

## Key Results

1. **Sample**: 13 spectroscopically unconfirmed but photometrically robust massive galaxy candidates at z_phot ~ 7--9.

2. **Sizes**: Effective radii in range 80--300 pc (mean 150 pc), making them the most compact massive objects known at any redshift.

3. **Stellar Masses**: M* ~ 10^{10}--10^{11} M_sun, comparable to local elliptical giants, but assembled within first 0.6--0.7 Gyr.

4. **Size-Mass Offset**: These galaxies are ~10--20x smaller at fixed mass than their presumed z~0 descendants, implying significant size evolution.

5. **Density Concentration**: Central surface densities comparable to local galaxy nuclei, suggesting early formation of today's densest stellar systems.

6. **Caveats**: Photometric redshifts are degenerate (true redshifts could be z~6--7 or z~10--12). Stellar masses depend on age/metallicity assumptions. JWST PSF effects on morphology partially characterized but not fully understood.

---

## Impact and Legacy

This paper catalyzed intense discussion and follow-up:

1. **Spectroscopic Confirmation Quest**: Triggered multiple NIRSpec and ground-based follow-up campaigns to confirm redshifts and age estimates of Labbe candidates.

2. **Dust Degeneracy Issue**: Subsequent work (Brammer, others, 2023--2024) revealed that some Labbe candidates could be lower-redshift dusty starbursts, not z>7 quiescent galaxies. A fraction of the sample was reclassified.

3. **Formation Mechanism Debate**: Inspired theoretical work on rapid early assembly mechanisms: monolithic collapse, early mergers, or top-heavy initial mass function.

4. **AGN Connection**: Recognition that some apparently compact red sources might harbor AGN (linking to Little Red Dots work), which would inflate bolometric luminosity and invalidate simple stellar mass estimates.

5. **Galaxy Formation Tension**: Intensified discussion of tension between LCDM predictions (which expect hierarchical assembly) and observations suggesting earlier, faster bulge formation.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework, predicting a different expansion history H(z) and density contrast evolution than LCDM, would affect the feasibility of forming massive, compact objects at z~8.

**Key Coupling Points**:

1. **Density Contrast Growth Rate**: The linear growth rate of density perturbations d(delta)/dz depends on the expansion rate H(z) and the background density rho(z). A phonon-exflation model predicting faster early growth would enhance the likelihood of rapid early galaxy assembly.

2. **Reheating and Ionization**: The cosmic ionization history (reionization at z~6--15) and the seed population of sources driving reionization depend on AGN and galaxy demographics. Labbe galaxies, if confirmed at z>8, would contribute to the ionizing photon budget and constrain reionization models.

3. **Early Universe Constraints**: Labbe et al.'s results place a lower bound on the mass assembly rate at z~8. Any alternative cosmology (including phonon-exflation) must accommodate objects of M* ~ 10^{10.5} M_sun by z=8, which constrains the growth rate of structure.

**Intensity**: Medium. Labbe's observations provide phenomenological anchors but do not directly test NCG or spectral-action predictions. The connection is indirect: early structure formation constraints feed into viability assessments of alternative cosmologies.

---

## Key Equations Summary

| Quantity | Equation | Typical Value at z=8 |
|----------|----------|---------------------|
| Photometric SED Fit | Chi-2 minimization over age, Z, A_V | z_phot = 7--9 |
| Sérsic Profile | $I(r) = I_e \exp[-b_n((r/r_e)^{1/n}-1)]$ | n ~ 3--5, r_e ~ 150 pc |
| Size-Mass Relation (z=0) | $\log(r_e/\text{kpc}) \approx 0.55 \log(M_*/M_{\odot}) - 5.0$ | Predicts r_e ~ 3 kpc for M* ~ 10^{10.5} M_sun |
| Measured Size Offset | $r_e(z\sim8) / r_e(z\sim0)$ | ~0.05--0.15 (factor 7--20 smaller) |
| Stellar Mass from SED | $M_* = (M/L) \times L$ | 10^{10}--10^{11} M_sun |
| Cosmic Age at z=8 | $t(z) = 2/(3H_0(1+z)^{3/2})$ | ~630 Myr |
