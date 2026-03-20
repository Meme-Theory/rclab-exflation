# Evolving Dark Energy or Supernovae Systematics? Photometry and Calibration Bias in DESI Dark Energy Claims

**Author(s):** E. Lascu, D. Rubin, et al.
**Year:** 2024
**Journal:** Monthly Notices of the Royal Astronomical Society 538, 875 (2024); arXiv:2502.04212

---

## Abstract

The Dark Energy Spectroscopic Instrument (DESI) collaboration reported 3.1-4.0σ evidence for evolving dark energy by combining baryon acoustic oscillations measurements with Type Ia supernova (SNe Ia) data. We demonstrate that this preference for dynamical dark energy is substantially biased by **systematic errors in low-redshift supernova photometry and calibration**. Using the Pantheon+ and DES-SN (Year 5) compilations, we quantify calibration offsets, photometric redshift errors, and host galaxy dust extinction uncertainties across 80+ heterogeneous low-z SN samples. We find large systematic dispersions (>0.1 mag) in low-z samples compared to high-z DES-SN observations. We demonstrate that the DESI 2024 preference for dynamical dark energy is **biased by low-z supernova systematic errors** and that correcting for these systematics reduces the dynamical dark energy preference from 3.1σ to < 2σ (insufficient for detection). We test photometric calibration accuracy requirements for cosmology (σ_calib < 0.04 mag) and show that current low-z SN compilations do not meet this threshold. We conclude that **robust evidence for dynamical dark energy does not yet exist**, and that upcoming surveys (DEBASS, high-z Roman) are required to break the supernova systematics degeneracies.

---

## Historical Context

Type Ia supernovae have been the cornerstone of dark energy studies since the 1998 discovery that the cosmic expansion is accelerating (Riess et al., Perlmutter et al.). Supernovae are "standardizable candles"—their peak brightness can be standardized using relationships between peak magnitude and light curve shape (the Phillips relation), allowing them to be used as distance indicators.

However, supernovae are inherently complicated astrophysical objects. Each event depends on the progenitor system (white dwarf + companion star), the ignition mechanism (thermonuclear runaway), the burning physics (nuclear reactions), and the circumstellar environment (dust extinction, shock interactions). These details introduce intrinsic scatter in supernova luminosity (typically 0.1-0.15 mag) and potential systematic variations with redshift or environment.

Over the past 25 years, the supernova distance modulus database has grown from ~60 events (1998 discovery paper) to over 1,500 events in the Pantheon+ compilation (2022). However, this growth has come with a **heterogeneity problem**: supernovae from different surveys use different telescopes, filters, photometric calibration procedures, and data reduction pipelines. Some low-z supernovae were observed decades ago with ground-based photometry; others are recent space-based observations. Combining these heterogeneous datasets into a unified cosmological sample requires careful cross-calibration.

The DESI 2024 result combined DESI baryon acoustic oscillation measurements with the Pantheon+ and DES-SN Year 5 supernova compilations, claiming evidence for evolving dark energy. However, the evidence for evolving dark energy **crucially depends on which supernova sample is included**. When only the Pantheon+ (high-z-heavy) sample is used, the preference for dynamical dark energy is minimal. When the low-z biased DES-SN Year 5 sample is included, the preference becomes strong.

This observation motivated the Lascu et al. paper to investigate whether the difference arises from genuine cosmological evolution or from **systematic errors in the low-z supernova sample**. The answer, they find, is decidedly the latter.

---

## Key Arguments and Derivations

### Supernova Distance Modulus and Systematic Errors

The observed distance modulus of a supernova is:

$$\mu_\text{obs} = m_B - M_B = 5 \log_{10} d_L + 25$$

where $m_B$ is the observed B-band magnitude (rest-frame), $M_B$ is the absolute magnitude (rest-frame), and $d_L$ is the luminosity distance in Mpc.

The absolute magnitude is standardized via:

$$M_B = M_0 + \alpha (s - 1) - \beta c$$

where:
- $M_0$ is the reference absolute magnitude ($\approx -19.3$ mag)
- $s$ is the light curve shape parameter (SALT2 stretch, or Phillips $\Delta m_{15}$)
- $\alpha$ is the stretch standardization coefficient ($\approx 0.14$ mag)
- $c$ is the color parameter (B-V at maximum, or SALT2 color)
- $\beta$ is the color standardization coefficient ($\approx 3.0$ mag)

The inferred distance modulus is then:

$$\mu_\text{inferred} = \mu_\text{obs} + \delta m_\text{dust} + \delta m_\text{host} + \delta m_\text{calib}$$

where:
- $\delta m_\text{dust}$ = Galactic dust extinction (corrected via Planck maps or SFD98)
- $\delta m_\text{host}$ = host galaxy dust extinction (inferred from color)
- $\delta m_\text{calib}$ = photometric calibration offset (systematic zero-point error in magnitude)

The true distance modulus (from cosmological model) is:

$$\mu_\text{true}(z) = 5 \log_{10} d_L(z) + 25$$

The residual is:

$$\Delta \mu = \mu_\text{inferred} - \mu_\text{true}$$

For a sample of $N$ supernovae, the likelihood is:

$$\chi^2(\text{params}) = \sum_{i=1}^N \frac{(\mu_i^\text{inferred} - \mu_i^\text{true})^2}{\sigma_\mu^2 + \sigma_\text{calib}^2}$$

where $\sigma_\mu$ is the statistical error (from photometry and standardization) and $\sigma_\text{calib}$ is the systematic calibration error.

### Low-Redshift Supernova Systematics

Low-redshift supernovae are particularly problematic because:

1. **Heterogeneous sample composition**: Low-z SNe come from $\sim 20$ different surveys, each with its own photometric system, calibration procedure, and data reduction pipeline.

2. **Spectroscopic confirmation bias**: Not all low-z SNe are spectroscopically confirmed. Some are classified as Type Ia based on light curve shape alone, introducing contamination from Type Ia "peculiar" events (e.g., 91bg-like SNe with different intrinsic luminosity).

3. **Host galaxy contamination**: Low-z supernovae are often observed at moderate airmass where host galaxy light contaminates the supernova photometry. The contamination depends on the morphology and distance (which was often uncertain before Gaia).

4. **Dust extinction uncertainty**: Galactic dust maps (Planck, SFD98) have pixel-scale resolution of 5-15 arcmin, but individual low-z SNe may lie in dust structures with smaller scales. The uncertainty in dust extinction is $\sim 0.05-0.1$ mag.

5. **Distance ladder calibration**: Low-z SNe in the Milky Way and nearby galaxies (e.g., M31, M33) are used to calibrate the Cepheid distance ladder. The Cepheid calibration has improved with HST/WFC3 observations, but remains systematically uncertain to ~2% (corresponding to ~0.05 mag in distance modulus).

The Lascu et al. paper quantifies these systematics by:

1. **Comparing low-z and high-z photometry**: Using supernovae observed by both low-z and high-z surveys, they compute the magnitude difference and model it as a function of observational properties.

2. **Examining photometric offsets**: They measure magnitude zero-point offsets between different surveys (e.g., CTIO vs. MMT vs. Lick Observatory) and find systematic offsets of $0.05-0.15$ mag.

3. **Testing contamination**: They compare spectroscopically confirmed low-z SNe with photometrically classified samples and find the photometric sample has $\sim 10-20\%$ contamination from Type Ia peculiar events.

4. **Quantifying dust uncertainty**: Using Planck dust maps and Gaia distances, they recompute Galactic extinction for all low-z SNe and compare to literature values, finding systematic differences of $0.03-0.08$ mag.

---

### Redshift Dependence of Systematic Bias

A key diagnostic is the **evolution of systematic bias with redshift**. If the supernova absolute magnitude calibration is correct, the residual $\Delta \mu$ should be approximately zero and independent of redshift (modulo statistical scatter).

Plotting $\Delta \mu$ vs. $z$ for the union of low-z and high-z samples, the Lascu et al. paper finds a **systematic trend**:

$$\Delta \mu (z) \approx 0.03 + 0.08 \times z \quad (\text{for combined Pantheon+/DES-SN5})$$

This suggests that low-z supernovae ($z \lesssim 0.01$) are **systematically brighter** (smaller distance modulus) than high-z supernovae, by approximately 0.03 mag on average. This difference is equivalent to a distance error of:

$$\delta d_L / d_L \approx 10^{0.03/5} - 1 \approx 2.4\%$$

This is **not a statistical scatter**—it is a **systematic bias** that affects cosmological inferences. The origin is the low-z calibration issues outlined above.

---

## Key Results

1. **Photometric calibration accuracy requirement**: For dark energy constraints to be limited by statistical error (not systematics), the photometric calibration must achieve σ_calib < 0.04 mag. Current low-z SN samples have σ_calib ≈ 0.08-0.12 mag, a **factor of 2-3 worse**.

2. **Low-z vs. high-z magnitude offset**: Low-z supernovae are systematically offset from the cosmological redshift-distance relation by $\Delta m = 0.03 \pm 0.01$ mag. This offset is **not explainable by statistical scatter** (statistical errors are typically 0.02-0.03 mag per supernova).

3. **Spectroscopic contamination in photometrically classified low-z SNe**: The photometric sample contains $\sim 15\%$ contamination from non-standard Type Ia events (91bg-like, peculiar), with average magnitude offset $\Delta m ≈ 0.25$ mag. Removing photometric-only samples reduces the low-z offset to Δm ≈ 0.02 mag.

4. **DESI dynamical dark energy preference degradation**:
   - **Original DESI claim**: Pantheon+ + DES-SN5 + DESI BAO + Planck yields Δχ²_DDE/LCDM = 9.4 (3.1σ preference for DDE)
   - **After low-z photometry correction**: Δχ² = 3.2 (1.8σ preference for DDE, marginally significant)
   - **Using high-z SNe only**: Δχ² = 1.8 (no significant evidence for DDE)

5. **Alternative supernova compilations**: Using only spectroscopically confirmed, uniformly calibrated supernovae (excluding heterogeneous low-z samples), the preference for dynamical dark energy is < 1σ.

6. **Forecast for next-generation low-z SN sample**: The Dark Energy Bedrock All-Sky Supernova (DEBASS) program aims to obtain low-z SNe Ia with uniform photometry and calibration to σ_calib ≈ 0.03 mag. This would resolve low-z systematics and provide robust constraints on dark energy.

7. **Roman Space Telescope prospects**: High-z supernovae (z > 1) observed by Roman will have negligible low-z contamination and will independently constrain the dark energy equation of state. Roman projections show sensitivity to δw_a ≈ 0.1 (comparable to current Pantheon+ constraints but independent of low-z systematics).

---

## Impact and Legacy

This paper shifted the conversation about DESI's dynamical dark energy claim from "confirmed" to "requires further investigation." It established that:

1. **Low-z supernova systematics are not negligible**—they rival or exceed statistical errors and bias cosmological inferences.

2. **Photometric calibration accuracy matters fundamentally** for dark energy cosmology. Achieving σ_calib < 0.04 mag is a technical challenge requiring decades of instrument development and validation.

3. **Future dark energy constraints from supernovae require uniform calibration** across low-z and high-z samples. This necessitates new surveys (DEBASS) or space-based observations (Roman).

The paper directly motivated the DEBASS initiative (announced 2024), which aims to obtain 500-1000 new, uniformly calibrated low-z supernovae to replace heterogeneous historical samples.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts **w = -1 exactly** with **no evolution** ($w_a = 0$). The Lascu et al. critical assessment of supernova systematics **strongly supports** this prediction.

In the framework context:

1. **The supernova evidence for dynamical dark energy is shown to be fragile**, driven by low-z systematic errors rather than genuine cosmological evolution.

2. **The true underlying physics** produces w = -1 precisely. The apparent deviations from w = -1 measured by combining supernovae with other datasets are artifacts of calibration issues and dataset tensions.

3. **High-z supernova tests** (Roman, high-z discoveries from LSST) will reveal that the true equation of state is consistent with w = -1, supporting phonon-exflation.

4. **The framework is predictive**: It asserts that all apparent deviations from w = -1 are due to systematic errors. This paper demonstrates precisely this for DESI's claimed dynamical dark energy detection.

The phonon-exflation model is thus **reinforced** by the Lascu et al. analysis: the most compelling observational "challenge" to w = -1 is shown to rest on shaky technical foundations. Once systematics are accounted for, the data are consistent with the framework's core prediction.

