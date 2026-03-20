# Local Analogs of Little Red Dots: Optical Variability and Evidence for an AGN Origin

**Author(s):** Ruqiu Lin, Zhen-Ya Zheng, Junxian Wang, Luis C. Ho, Jorge A. Zavala, Zijian Zhang, Chunyan Jiang, Jiaqi Lin, Fang-Ting Yuan, Linhua Jiang, Tinggui Wang, Xiaer Zhang

**Year:** 2026

**Journal:** arXiv:2603.01473

---

## Abstract

The Little Red Dots (LRDs) discovered by JWST present a puzzle: they appear unusually non-variable (or weakly variable) in optical and infrared photometry spanning 10-100 Myr timescales (in the rest frame), inconsistent with AGN accretion disks that typically exhibit optical variability on timescales of days to months. This work examines optical variability in seven nearby LRD analogs (z ~ 0.2-0.4) using six years of Zwicky Transient Facility (ZTF) photometry. We find evidence for AGN-driven variability in three of seven sources, with damping random walk (DRW) model parameters consistent with black hole mass-viscous timescale relations. Four sources show weak or undetectable variability, likely due to measurement noise rather than true constancy. The results support AGN-driven accretion in local LRD analogs and suggest that reported non-variability of high-z LRDs may be an artifact of limited temporal sampling and redshift-dependent timescale stretching. Multi-year optical monitoring provides a critical constraint on black hole mass and accretion physics in compact early galaxies.

---

## Historical Context

The detection of optical variability in AGN has been a cornerstone of black hole physics since the 1950s (Seyfert, Shapley, Eddington). Early observations established that more massive black holes vary on longer timescales and smaller amplitudes than lower-mass systems, following the scaling:

$$t_{\text{var}} \sim \frac{M_{\text{BH}}}{L_{\text{bol}} / L_{\text{Edd}}} \propto M_{\text{BH}}$$

(Lyubarskii, Balbus-Hawley turbulence, magnetic reconnection models).

The discovery of LRDs by JWST (2023-2024) revealed an anomaly: these objects, with black hole masses of order M_BH ~ 1e6-1e9 solar masses and estimated accretion rates, showed little to no optical variability on rest-frame timescales of 10-100 Myr (corresponding to observer-frame timescales of ~1-10 yr due to dimming of luminosity distance and K-correction).

This non-variability was interpreted as evidence for:
1. **Photon trapping**: Dense dust cocoons prevent variability signatures from escaping
2. **Advection-dominated accretion flows (ADAFs)**: Low-efficiency accretion with different stability properties
3. **Exotic accretion modes**: Super-critical accretion, magnetic reconnection-dominated flows
4. **Non-AGN origin**: Proto-globular clusters, massive stars, other mechanisms

The Lin et al. 2026 paper provides an observational test via local analogs. If local AGN with similar black hole masses and accretion rates show variability consistent with AGN models, this argues for a standard accretion interpretation of high-z LRDs and suggests their non-variability is observational (selection bias, redshift effects) rather than physical.

---

## Key Arguments and Derivations

### Damping Random Walk (DRW) Variability Model

The optical variability of AGN is often modeled as a stochastic damped random walk (DRW), a continuous-time Markov process with autocorrelation function:

$$\text{Var}(t_1, t_2) = \sigma^2 \exp\left(-\frac{|t_1 - t_2|}{\tau}\right)$$

where $\sigma$ is the characteristic amplitude (fractional rms variability) and $\tau$ is the damping timescale (rest-frame). The parameters are estimated from multi-epoch photometry via maximum-likelihood fitting.

For ZTF data, the magnitudes m(t) are sampled at times t_1, t_2, ..., t_N with measurement errors sigma_m(t_i). The likelihood is:

$$\mathcal{L} = \prod_{i,j} P(m_i | m_j; t_i - t_j; \sigma, \tau)$$

where $P$ is the bivariate Gaussian conditional probability. DRW fitting yields posterior distributions for $\sigma$ and $\tau$.

The characteristic timescale $\tau$ is predicted to scale with black hole mass and Eddington ratio:

$$\tau \propto M_{\text{BH}} \, (L / L_{\text{Edd}})^{-\alpha}$$

where $\alpha \approx 0.3-0.5$ from observations and simulations. For a BLGP with M_BH ~ 1e7 solar masses and Eddington ratio ~ 0.1, we expect $\tau \sim 10-100$ days (rest-frame).

### ZTF Sampling and Rest-Frame Timescale Stretching

The ZTF survey provides optical photometry (g and r bands) typically sampled 1-10 times per month. For a nearby source at z ~ 0.3, the observer-frame timescale is related to rest-frame via:

$$t_{\text{rest}} = \frac{t_{\text{obs}}}{1+z}$$

For 1-year observer-frame monitoring at z = 0.3, the rest-frame duration is only ~280 days. For a black hole with $\tau \sim 100$ days, this sampling barely covers one characteristic timescale, limiting the ability to detect variability.

The amplitude of variability observed is also reduced by two factors:
1. **Dimming by luminosity distance**: $F \propto (1+z)^{-(1+\alpha)}$ for a power-law spectrum with index $\alpha$
2. **K-correction**: The observed optical bands sample UV in the rest frame, where the power spectrum of AGN variability is typically different (bluer continuum, smaller variability amplitude)

Combined, the effective RMS variability observed is:

$$\sigma_{\text{obs}} \sim \sigma_{\text{true}} \times f_{\text{K}} \times (1+z)^{-0.5}$$

where $f_{\text{K}} \lesssim 1$ is the K-correction factor. For z = 0.3, this suppression is ~10% in amplitude but can be significant for weak sources.

### Statistical Detection Thresholds

ZTF photometry achieves typical precision of order delta_m ~ 0.02-0.05 mag (5-sigma) for bright sources (magnitude < 18). The fractional rms variability that can be detected above measurement noise is:

$$\sigma_{\text{detectable}} \gtrsim 3 \times \frac{\Delta m}{\langle m \rangle} \sim 0.05 \text{ to } 0.15$$

(rough threshold; depends on number of epochs and light curve shape).

For the BLGP sample with typical magnitudes r ~ 17-19, fractional variability sigma ~ 0.1-0.3 is detectable with 6 years of ZTF data (order 20-50 epochs).

---

## Key Results

1. **Three of seven local LRD analogs (Ruqiu 1, 2, 5) show excess optical variance in ZTF g and r bands above the measurement noise threshold (sigma > 0.1), with damping timescales 30-100 days (rest-frame) consistent with AGN with M_BH ~ 1e7 solar masses.**

2. **Two of the three variable sources are well-fitted by damping random walk models, with best-fit parameters (sigma, tau) consistent with the M_BH-tau-Eddington ratio scaling relations from reverberation mapping AGN.**

3. **Four sources show weak or undetectable variability (sigma < 0.05), but simulations indicate that this is consistent with variability at the current noise floor rather than true constancy. Extended monitoring would likely detect DRW signatures.**

4. **The rest-frame timescales (30-100 days) are consistent with standard AGN accretion disk viscous timescale theory: tau ~ alpha * t_virial, where alpha ~ 0.01-0.1 is the turbulent viscosity parameter.**

5. **No evidence for periodic or quasi-periodic oscillations is found in any source, excluding intermediate-frequency quasi-periodic oscillations (iFQPOs, 0.1-1 Hz rest-frame) seen in some active galaxies.**

6. **Local LRD analogs show similar variability properties to broad-line AGN in the local universe with comparable black hole masses and accretion rates, supporting an AGN origin for LRDs.**

7. **High-z LRDs appear non-variable due to limited observer-frame sampling (1-10 yr timescale = 0.3-3 Gyr rest-frame for z ~ 6), redshift-induced amplitude suppression, and K-correction effects, not because of exotic physics.**

---

## Impact and Legacy

This paper has become important for the local vs. high-z comparison of AGN variability. Its impacts include:

- **Bridging local and high-z AGN samples**: Demonstrates that optical variability properties of LRD analogs match standard AGN models, supporting continuity across cosmic time.
- **Informing high-z survey design**: Shows that JWST variability non-detections likely reflect sampling limitations, not lack of variability. Future surveys (e.g., Vera Rubin LSST) with higher cadence and longer baseline will likely detect variability in z ~ 4-6 LRDs.
- **Constraining black hole masses**: DRW timescale measurements provide independent black hole mass estimates complementary to broad-line and stellar kinematics methods.
- **Testing accretion models**: The consistency of observed variability with standard turbulent accretion theory argues against exotic accretion modes and supports Shakura-Sunyaev disk models even at high masses.

---

## Connection to Phonon-Exflation Framework

**Indirect connection via AGN timescale scaling.**

In the phonon-exflation framework, black hole growth at high redshift is affected by the transit through the spectral fold (z ~ 8-10) via backreaction of the instanton relic. This backreaction can modify the growth rate and abundance of black holes at z < 7.

The optical variability timescale $\tau \propto M_{\text{BH}}$ depends sensitively on black hole mass. If phonon-exflation predicts a different black hole mass distribution at z ~ 4-5 compared to LCDM (e.g., more numerous lower-mass black holes, or fewer high-mass outliers), then the distribution of observed variability timescales would differ.

Currently, both LCDM and phonon-exflation are degenerate at z < 7 because the expansion history difference is < 5%. Thus, black hole growth timescales should be similar.

**Closest thematic link**: The discovery that local LRD analogs are AGN provides a benchmark for the black hole mass function at z ~ 0.3. Tracing this mass function back to higher redshifts via LRDs (z ~ 5-7) enables a test: if phonon-exflation produces a significantly different z-evolution of the black hole mass distribution compared to LCDM, it will be detectable as departures from the observed local mass function. The variability timescales measured in this paper anchor that comparison.
