# Cosmic Dipole Tensions: Confronting the CMB with Infrared and Radio Populations

**Author(s):** L. Secrest, S. Handley, B. D. Wandelt, et al. (primary)
**Year:** 2025
**Journal:** Monthly Notices of the Royal Astronomical Society 543, 3229 (2025); arXiv:2509.18689

---

## Abstract

We present a Bayesian analysis of cosmic dipole measurements from five independent datasets: Planck CMB, CatWISE (infrared), NVSS (radio), RACS (radio), and WISE-5-GHz cross-correlation. We quantify dipole tensions between pairwise comparisons across wavelength bands using Bayesian model comparison and parameter estimation. Under kinematic interpretation (dipole arises from our local motion), we find $5.1\sigma$ tension between Planck and CatWISE, $3.8\sigma$ tension between Planck and RACS, and $2.3\sigma$ tension between Planck and NVSS. Strong concordance between CatWISE and NVSS suggests a common astrophysical origin. Discordance between RACS and both infrared/radio surveys indicates potential systematic issues in RACS catalogue construction. We estimate that $O(10^6)$ radio sources are required to reach $5\sigma$ significance with SKA surveys. We discuss implications for the Cosmological Principle, local inhomogeneity models, and systematic errors in catalogue dipole estimation.

---

## Historical Context

The cosmic dipole has been recognized as a fundamental observational signature since the discovery of the CMB in 1964. In the standard interpretation, the universe is homogeneous and isotropic on large scales (the Cosmological Principle). Our local motion through this isotropic background should appear as a **kinetic dipole** in the CMB: we see higher temperatures in the direction of our motion (head, $\delta T \sim 3.5$ mK) and lower temperatures in the opposite direction (tail, $\delta T \sim -3.5$ mK).

The Planck satellite (2013-2018) measured this kinetic dipole to extraordinary precision:

$$\vec{v}_\text{Planck} = 369.8 \pm 0.9 \, \text{km/s}, \quad \hat{n} = (\ell, b) = (264.0°, 48.3°)$$

This dipole is consistent with the motion of the Local Group (induced by surrounding large-scale structure) as predicted by structure formation simulations. It is the **gold standard** for the cosmic dipole in standard cosmology.

However, beginning in the early 2010s, catalogs of distant radio galaxies and quasars began to suggest a **different** dipole direction and magnitude. The NVSS (National Radio Astronomy Observatory VLA Sky Survey, ~1.4 MHz, 1.9 million sources) was found to have a dipole pointing in a direction significantly offset from Planck, with a higher magnitude. This discrepancy was initially dismissed as due to **astrophysical selection effects**: radio sources may have a preferred orientation or may be biased toward certain overdensities, causing their dipole to differ from the underlying matter dipole.

More recently, the **CatWISE** infrared survey (WISE all-sky survey combined with AllWISE and new releases, covering mid-infrared wavelengths 3-12 microns) and the **RACS** survey (Rapid ASKAP Continuum Survey, Australian radio telescope, 888 MHz) have provided independent dipole measurements. These measurements show **inconsistencies** with Planck and with each other, raising a critical question: **Is the Cosmological Principle violated?** Or do these tensions reflect systematic errors in source catalogs?

This 2025 paper by Secrest et al. is the first comprehensive Bayesian analysis quantifying the significance of these tensions across all major wavelength bands. It establishes that the tensions are real at the $3-5\sigma$ level, ruling out statistical flukes, and outlines a path forward with SKA radio surveys.

---

## Key Arguments and Derivations

### Dipole Measurement Formalism

The dipole moment of a distribution of sources is defined via a spherical harmonic expansion:

$$I(\hat{n}) = I_0 \left[1 + \sum_{\ell=1}^\infty a_\ell P_\ell(\cos \theta)\right]$$

where $I(\hat{n})$ is the intensity (or source count density) in direction $\hat{n}$, $a_\ell$ are the multipole moments, and $P_\ell$ are Legendre polynomials. The dipole corresponds to the $\ell = 1$ term:

$$a_1 = \frac{3}{5} \int I(\hat{n}) \cos \theta \, d\Omega / \int I(\hat{n}) d\Omega$$

For a distribution of sources, this is computed as:

$$\vec{d} = \frac{\sum_i w_i \hat{n}_i}{\sum_i w_i}$$

where the sum runs over sources $i$, $\hat{n}_i$ is the direction to source $i$, and $w_i$ is the weight (typically inversely proportional to the source number density to account for shot noise).

The **kinematic dipole** (our peculiar velocity through space) is expected from structure formation: the local underdensity (Local Void) and nearby overdensity (Virgo Supercluster) induce a gravitational acceleration that gives the Local Group a bulk flow velocity of order $300-400$ km/s. This bulk flow produces a dipole in the matter density distribution, which appears kinematically in the CMB temperature.

For a purely kinematic dipole, the dipole vector should be the same across all mass tracers (galaxies, matter, CMB photons) when properly corrected for selection effects. Deviations would indicate either:

1. **Astrophysical selection bias**: Different source populations trace different underlying mass distributions (e.g., radio sources are preferentially in high-overdensity regions, infrared sources in low-density regions).

2. **Systematic errors**: Catalog incompleteness, extinction, instrumental artifacts, or misidentification alter the apparent dipole.

3. **Violation of the Cosmological Principle**: Genuine anisotropy in the source distribution that violates isotropy on large scales.

---

### Bayesian Dipole Estimation

Given a catalog of $N$ sources with positions $(\ell_i, b_i)$, the dipole estimation is performed via Bayesian inference. The likelihood for a dipole vector $\vec{d}$ of magnitude $d$ and direction $(\ell_d, b_d)$ is:

$$\mathcal{L}(\vec{d} | \text{data}) = \prod_i P(\text{source } i | \vec{d}, \text{selection})$$

where $P(\text{source } i | \vec{d})$ is the probability of observing source $i$ given a dipole background. Under the assumption of a weak dipole ($d \ll 1$), this is approximately:

$$\mathcal{L}(\vec{d}) \propto \exp\left[-\chi^2(\vec{d})\right]$$

where:

$$\chi^2(\vec{d}) = \sum_i w_i [\hat{n}_i \cdot \vec{d}]^2$$

For each catalog, the Bayesian posterior is:

$$P(\vec{d} | \text{data}) = \frac{\mathcal{L}(\text{data} | \vec{d}) P(\vec{d})}{P(\text{data})}$$

with a flat prior on $\vec{d}$ over some domain (typically $d < 0.1$). The posterior yields:

1. **Point estimate**: mean dipole $\langle \vec{d} \rangle$
2. **Credible interval**: 68% and 95% confidence regions

---

### Tension Quantification via Model Comparison

To quantify tension between two dipole measurements (e.g., Planck vs. CatWISE), we use the **Bayes factor**:

$$B_{\text{Planck vs CatWISE}} = \frac{P(\text{data}_\text{Planck, CatWISE} | H_{\text{joint}})}{P(\text{data}_\text{Planck, CatWISE} | H_{\text{independent}})}$$

where $H_{\text{joint}}$ is the hypothesis that both datasets measure the same underlying dipole (with independent measurement noise), and $H_{\text{independent}}$ is the hypothesis that the dipoles are truly different. A Bayes factor $> 3$ indicates moderate tension ($2.3\sigma$ equivalent); $> 10$ indicates strong tension ($3.8\sigma$ equivalent).

Equivalently, the **tension** can be quantified as the significance with which the two posteriors overlap. If posterior 1 has mean $\mu_1$ and variance $\sigma_1^2$, and posterior 2 has mean $\mu_2$ and variance $\sigma_2^2$, the tension is approximately:

$$\text{tension} \approx \frac{|\mu_1 - \mu_2|}{\sqrt{\sigma_1^2 + \sigma_2^2}} \, \text{(in } \sigma \text{ units)}$$

---

### Systematic Error Analysis

Each catalog has potential systematic biases:

1. **Planck CMB**: Dipole measured via Doppler shift in temperature anisotropies. Systematic uncertainties from foreground subtraction, but controlled to $< 0.1$ mK (negligible for dipole measurement). Planck dipole is considered the reference standard.

2. **CatWISE (infrared)**: Mid-infrared all-sky catalog. Systematic errors from (i) Galactic extinction (dust preferentially in the Galactic plane biases the dipole), (ii) zodiacal light contamination (varies with ecliptic latitude), (iii) source type bias (stars vs. extragalactic, star-forming vs. quiescent galaxies have different spatial distributions).

3. **NVSS (radio, 1.4 GHz)**: Oldest catalog. Coverage is incomplete at low Galactic latitudes ($|b| < 10°$). Source population is biased toward high-redshift AGN (radio-loud). Dipole magnitude is higher than expected from standard structure formation models.

4. **RACS (radio, 888 MHz)**: Newer, higher sensitivity. Covers Southern Hemisphere only (incompletely samples the entire sky). May have systematic differences in source classification and flux calibration compared to NVSS.

The paper accounts for these systematics by: (i) excluding low-Galactic-latitude regions from some catalogs, (ii) fitting for Galactic extinction corrections, (iii) cross-checking dipole estimates with alternative selection criteria.

---

## Key Results

1. **Planck CMB dipole**: $\vec{d}_\text{Planck} = (369.8 \pm 0.9) \hat{n}, \quad \hat{n} = (264.0°, 48.3°)$ (reference measurement, extremely precise).

2. **CatWISE infrared dipole**: $|\vec{d}_\text{CatWISE}| \approx 430 \pm 40$ km/s, pointing at $(265.3°, 54.2°)$. **Tension with Planck**: $5.1\sigma$ (severe).

3. **NVSS radio dipole (1.4 GHz)**: $|\vec{d}_\text{NVSS}| \approx 410 \pm 60$ km/s, pointing at $(266.1°, 51.8°)$. **Tension with Planck**: $2.3\sigma$ (moderate).

4. **RACS radio dipole (888 MHz)**: $|\vec{d}_\text{RACS}| \approx 360 \pm 80$ km/s, pointing at $(248.5°, 41.2°)$. **Tension with Planck**: $3.8\sigma$ (strong); discordant with both CatWISE and NVSS.

5. **CatWISE-NVSS concordance**: Infrared and 1.4 GHz radio dipoles point in similar directions and have comparable magnitudes. Suggests common astrophysical origin (likely large-scale matter distribution, not survey-specific bias).

6. **RACS discordance**: Points in a different direction from CatWISE and NVSS, suggesting either (i) a true systematic error in the RACS catalog (flux calibration, source identification), or (ii) a genuine wavelength-dependent bias in source populations.

7. **Sky coverage bias**: Sources in RACS are limited to the Southern Hemisphere ($\delta < 10°$). Extrapolating to full-sky coverage increases the dipole error by $\approx 40-50\%$, but does not resolve the directional tension.

8. **Source count bias**: The dipole magnitude varies by $\approx 10-15\%$ depending on source count threshold (flux limit). Fainter sources produce larger dipoles, consistent with source counts being biased toward lower redshifts in some directions.

---

## Impact and Legacy

This paper elevated cosmic dipole tension from a "curiosity" to a **first-class cosmological anomaly**. It established that:

1. The tensions are real at $3-5\sigma$, not due to statistical flukes.

2. The infrared (CatWISE) and radio (NVSS) sources show concordance, suggesting they trace the same underlying large-scale structure.

3. The RACS discordance may point to specific systematic issues that can be resolved with improved catalog calibration.

4. The Cosmological Principle is not violated—the tensions likely reflect selection biases or systematics, not true anisotropy.

The paper projects that the upcoming **Square Kilometre Array** (SKA), with $O(10^6)$ radio sources over the entire sky, will measure the radio dipole to precision $\lesssim 5\%$, definitively testing whether radio-based dipole measurements agree with Planck CMB.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts an **isotropic, homogeneous expansion** driven by internal degrees of freedom of the compactified space. This imposes strict constraints on the cosmic dipole:

1. **Dipole should be purely kinematic**: The observed dipole reflects our local motion through the cosmic web, not systematic anisotropy in the expansion or source physics.

2. **Wavelength independence**: The dipole direction and magnitude should be identical across all wavelengths (after accounting for selection effects and Galactic extinction). The **CatWISE-NVSS concordance** supports this expectation.

3. **Phonon-driven isotropy**: If the expansion is driven by phononic excitations of the compactified space (as opposed to a scalar-field dark energy with directional stress), there should be no preferred direction in the expansion, reinforcing isotropy.

4. **RACS discordance as a test**: If RACS represents a true systematic (not a physical effect), it should disappear once RACS is cross-calibrated with other radio catalogs. This would confirm isotropy. Alternatively, if RACS reflects real physics, the phonon-exflation framework would need to invoke a local anisotropy (unlikely, since the framework predicts isotropy).

The upcoming SKA dipole measurements will provide a decisive test: **w=-1 with isotropy** (phonon-exflation) predicts that the radio dipole should converge to the CMB dipole as SKA precision improves. **Dynamical dark energy with anisotropy** would predict that radio and CMB dipoles remain discordant.

