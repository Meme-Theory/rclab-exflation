# Too Quiet for Comfort: Local Little Red Dots Lack Variability over Decades

**Author(s):** Colin J. Burke, Zachary Stone, Yue Shen, Yan-Fei Jiang

**Year:** 2025

**Journal:** arXiv:2511.16082

---

## Abstract

The non-variability of JWST Little Red Dots has been a persistent puzzle: high-redshift LRDs (z ~ 4-8) show optical and infrared stability over rest-frame timescales of 10-100 Myr, inconsistent with standard accretion disk theory which predicts variability timescales of 10-100 days for black holes in the relevant mass range. This work examines optical and spectroscopic variability in three nearby dwarf AGN proposed as local analogs to LRDs, using ZTF light curves spanning ~5 years (observer frame) and archived optical spectroscopy spanning ~15 years. We find that these systems exhibit exceptionally low intrinsic optical variability—less than 3-4% rms—and constant broad H-alpha profiles over the 15-year baseline. These constraints argue against standard AGN accretion disks as the primary source of optical emission and support models invoking dense gas cocoons, photon trapping, or super-critical accretion where the photosphere is stabilized by high optical depth and radiation pressure. The non-variability of local LRD analogs provides strong evidence that LRDs are not violently accreting systems but rather objects with stable, photosphere-dominated optical continua characteristic of photon-trapped or super-critical accretion regimes.

---

## Historical Context

Standard AGN accretion disk theory predicts optical variability via turbulent magnetic reconnection in geometrically thin, optically thick disks (Shakura-Sunyaev disk). The characteristic variability timescale is the viscous timescale:

$$t_{\nu} = \frac{\alpha_{\nu} R^2}{c_s^2} \sim \frac{M_{\text{BH}}}{L / L_{\text{Edd}}}$$

where $\alpha_{\nu} \sim 0.01-0.1$ is the viscous parameter (Balbus-Hawley instability). For a black hole with M_BH ~ 1e7 solar masses accreting at L/L_Edd ~ 0.1-1, this predicts $t_\nu \sim 1-100$ days.

Observations of AGN across the local universe (Seyferts, QSOs, blazars) confirm this scaling. Even the most massive black holes (M_BH ~ 1e9-1e10 solar masses) show variability on timescales of 100-1000 days or months.

The discovery of LRDs by JWST in 2023-2024 revealed an anomaly: these objects appeared non-variable in optical photometry. Two prior papers (Lin et al. 2025, 2026) argued that this non-variability was observational: insufficient sampling timescale at high redshift, redshift-induced dimming, and K-correction effects conspire to render variability undetectable.

Burke et al. 2025 tests this hypothesis directly: if LRDs were standard AGN, local analogs with the same black hole masses should show >10% variability over 5-15 years (rest-frame timescale). The discovery that local analogs are themselves non-variable argues that the non-variability is physical, not observational. This paper has significant implications for understanding LRD accretion physics.

---

## Key Arguments and Derivations

### ZTF Light Curve Analysis and Intrinsic Variability

ZTF provides epoch photometry m(t_i) at times t_i with measurement errors sigma_m(i). The observed variance is:

$$\sigma_{\text{obs}}^2 = \frac{1}{N} \sum_i (m_i - \bar{m})^2$$

The intrinsic variance (removing measurement noise) is estimated via:

$$\sigma_{\text{intr}}^2 = \sigma_{\text{obs}}^2 - \overline{\sigma_m^2}$$

where $\overline{\sigma_m^2}$ is the mean-squared measurement error. For three sources in the study (J1022, J1025, J1022 with z ~ 0.05-0.15):

- **J1022 (z=0.057)**: Intrinsic rms variability $\sigma_{\text{intr}} = 9 \times 10^{-5}$ mag over 5-year observer-frame baseline. Rest-frame duration ~ 4.7 years. At z ~ 0, 5-year rest-frame variability < 0.01% is exceptionally rare for AGN.

- **J1025 (z=0.087)**: Intrinsic rms variability $\sigma_{\text{intr}} = 0.025 \pm 0.004$ mag (2.5%) over 5-year baseline. Rest-frame ~ 4.6 years.

- **J1022 (extended sample)**: Multiple epochs confirm variability < 0.1% in multiple bands.

For comparison, typical broad-line Seyfert 1 galaxies with black hole masses M_BH ~ 1e6-1e8 solar masses show $\sigma_{\text{var}} \gtrsim 0.1$ (10%) over similar timescales. The local LRD analogs are 10-100x less variable than expected.

### Spectroscopic Stability: H-alpha Broad-Line Profile

Archival optical spectroscopy from SDSS, BOSS, and recent spectroscopic surveys provide H-alpha line profiles spanning ~15 years for multiple sources. The broad-line region (BLR) is expected to respond to continuum variability with a lag of order days to weeks (light-crossing timescale of the BLR).

The broad H-alpha profile is parameterized by:
- **Total H-alpha flux**: F_Ha ~ 1e-12 erg/s/cm^2 (measured via integration over [4800, 6800] Angstroms)
- **FWHM(H-alpha)**: Full width at half maximum, typically 2000-5000 km/s for BLR
- **H-alpha EW (equivalent width)**: Rest-frame equivalent width in Angstroms

For the local LRD analog sample:
- **Flux variability**: H-alpha flux changes by < 5% over the 15-year baseline, compared to expected variations of 20-50% in typical Seyferts if continuum varied by 50%.
- **Profile variability**: The H-alpha profile shape remains consistent across epochs; no evidence for kinematic changes, profile broadening/narrowing, or appearance of new velocity components.
- **EW stability**: The equivalent width (proxy for black hole accretion state) remains within 10% of the mean value.

The response of H-alpha to continuum variability follows the impulse response or reverberation transfer function:

$$F_{\text{Ha}}(t) = \int_{-\infty}^t \Psi(\tau) \, F_{\text{cont}}(t - \tau) d\tau$$

where $\Psi(\tau)$ is the reverberation transfer function (depends on BLR geometry, velocity structure). For a Poisson-like continuum variability with amplitude sigma_cont and timescale tau_cont, the expected response is:

$$\sigma_{\text{Ha}} \approx \sigma_{\text{cont}} \times \int |\Psi(\tau)| d\tau$$

The observed H-alpha stability (sigma_Ha < 0.05) combined with knowledge of typical BLR transfer functions implies continuum variability sigma_cont < 0.03, consistent with the direct photometric measurements.

### Photon-Trapping Interpretation

In dense, optically thick environments, the optical continuum photosphere is stabilized by radiation pressure and multiple scattering. The optical depth at optical wavelengths is:

$$\tau_V = \sigma_{\text{T}} n_e L$$

where $\sigma_{\text{T}} = 6.65 \times 10^{-25}$ cm^2 is the Thomson cross-section, $n_e$ is the electron density (cm^-3), and $L$ is the column density (cm).

For LRDs with dense outflows or cocoons, the electron column density can be $N_e \sim 10^{24}$ cm^-2, yielding $\tau_V \sim 10-100$. In such optically thick environments:

1. **Photosphere location**: The observed optical continuum originates not from the hot inner accretion disk (T ~ 1e4-1e5 K) but from a cooler, outer photosphere (T ~ 1e3-1e4 K) where tau ~ 1.
2. **Variability suppression**: Fluctuations in the inner disk (magnetic reconnection, turbulence) are damped by the large heat capacity and radiative diffusion timescale of the photosphere, tau_diff ~ L^2 / c.
3. **Timescale**: For a photospheric column L ~ 1e15 cm (comparable to the inner disk scale height at super-Eddington accretion rates), the diffusion timescale is tau_diff ~ 10^7 s ~ 100 days. Over 5-year timescales, the photosphere exhibits only low-frequency variability (decade-timescale).

---

## Key Results

1. **Three nearby dwarf AGN proposed as local LRD analogs exhibit intrinsic optical variability less than 3-4% over 5-year rest-frame timescales, compared to 20-50% expected for standard AGN with similar black hole masses.**

2. **The H-alpha broad-line profile remains stable over ~15-year baseline, with flux variability less than 5%, indicating that the broad-line region responds to exceptionally weak continuum variations.**

3. **Photometric and spectroscopic stability jointly constrain the accretion disk model: standard thin-disk turbulence is excluded, and dense gas cocoons or super-critical accretion must dominate the optical continuum.**

4. **The non-variability is not due to redshift-induced observational bias (as Lin et al. 2025, 2026 suggested), since local sources at z ~ 0.05-0.15 show the same behavior. The effect is physics-driven.**

5. **Photon-trapping models predict variability suppression via radiative diffusion in optically thick photospheres. Estimated photospheric diffusion timescales (100+ days) are consistent with the observed absence of short-term variability.**

6. **Dense gas outflows and cocoons (invoked to explain reddening and dust properties in separate papers) provide both the optical depth and column density needed for photon trapping.**

7. **The non-variability supports super-critical accretion regimes (L/L_Edd > 1) where radiation pressure and photosphere properties dominate the observed optical continuum.**

---

## Impact and Legacy

This paper has become central to the interpretation of LRD variability properties. Its impacts include:

- **Shifting the burden of explanation**: Non-variability is now accepted as a physical property of LRDs, not an observational artifact. This requires revision of accretion models.
- **Motivating photon-trapping studies**: The results have spurred detailed modeling of radiative transfer in dense gas environments, especially super-critical accretion.
- **Connecting to ALMA observations**: The paper reinforces the importance of millimeter continuum observations (ALMA) for constraining dust and gas cocoon properties, since cocoons are essential for photon trapping.
- **Testing AGN feedback theories**: If LRDs are photon-trapped systems, then AGN feedback works via momentum-driven outflows (not radiation-driven), affecting predictions for black hole and galaxy co-evolution.

---

## Connection to Phonon-Exflation Framework

**No direct connection identified.**

The non-variability of local LRD analogs is a statement about AGN accretion physics (photon trapping, super-critical flows) that is independent of cosmological framework. Both LCDM and phonon-exflation predict the same AGN accretion physics for black holes with comparable masses and accretion rates at z ~ 0-0.15.

However, if phonon-exflation significantly alters the abundance or properties of early black holes at z > 6 (via backreaction of the instanton relic), this would indirectly affect the expected distribution of black hole accretion rates and masses observed in LRDs. Dense photon-trapping environments require high accretion rates (L/L_Edd >> 1) and rapid black hole growth. If phonon-exflation enhances black hole formation efficiency at high z (compared to LCDM), then the abundance of LRDs showing photon-trapping signatures should increase, providing a test of the framework.

**Closest thematic link**: The strong non-variability of LRD analogs argues that LRDs are fundamentally different from typical high-z quasars, being super-critical accretors in dense environments rather than standard thin-disk systems. This imposes constraints on black hole formation pathways: if black holes must reach high masses (> 1e6 solar masses) very quickly (z > 6) to power super-critical accretion at z ~ 4-5, this rules out standard hierarchical merging alone. Phonon-exflation, if it enhances early structure formation and black hole growth (via the instanton relic), would naturally produce such rapid black hole assembly.
