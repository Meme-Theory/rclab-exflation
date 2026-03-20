# Analysis of Multi-epoch JWST Images of ~300 Little Red Dots: Tentative Detection of Variability in a Minority of Sources

**Author(s):** Zijian Zhang, Linhua Jiang, Weiyang Liu, Luis C. Ho
**Year:** 2024 (submitted November 5, 2024; revised April 17, 2025)
**Journal:** The Astrophysical Journal, Volume 985, Article 119 (2025)
**arXiv:** 2411.02729

---

## Abstract

The authors analyze multi-epoch JWST NIRCam photometry of 314 little red dots (LRDs) drawn
from five deep extragalactic fields (UNCOVER, CEERS, JADES, PRIMER-COSMOS, PRIMER-UDS),
searching for photometric variability on timescales of months to years in the rest-frame.
The LRD population as a whole shows no statistically significant average variability,
inconsistent with predictions of standard sub-Eddington AGN variability models at the
$> 3\sigma$ level. However, eight LRDs exhibit individually significant variability with
amplitudes of 0.24--0.82 magnitudes, indicating a genuine AGN contribution to their optical
emission in this minority subset. The results support super-Eddington accretion as the
dominant accretion mode for most LRDs, in which damped variability is a natural consequence.
The eight variable sources provide the cleanest sample for AGN-focused follow-up spectroscopy.

---

## Historical Context

### Variability as an AGN Diagnostic

Stochastic photometric variability is a hallmark of AGN activity: the optical-UV emission
from accretion disks varies by 0.1--0.5 mag on timescales of months to years, driven by
instabilities in the magnetorotational turbulence of the disk. The variability amplitude
increases with decreasing luminosity and wavelength, described by the damped random walk
(DRW) model (Kelly et al. 2009; MacLeod et al. 2010):

$$SF(\Delta t) = SF_\infty \left[1 - \exp\!\left(-\frac{|\Delta t|}{\tau_{\rm DRW}}\right)\right]^{1/2}$$

where $SF_\infty$ is the asymptotic structure function amplitude and $\tau_{\rm DRW}$ is the
characteristic decorrelation timescale (typically 100--300 days in the rest frame). For a
standard Shakura-Sunyaev thin disk, variability is expected at the few-percent to 30% level
on the observed timescales.

LRDs were discovered showing broad emission lines (classically an AGN signature) but several
puzzling non-AGN properties: lack of X-ray emission, lack of radio emission, and a red
continuum that could be dust-reddened AGN or a Balmer break from dense stellar populations.
Variability offers an independent test: if LRDs are AGN-dominated, they should vary; if they
are galaxy-dominated (with broad lines from shock or dense-gas emission), they should not.

### Previous Variability Studies

Prior to this paper, variability searches for LRDs were limited to small samples. Some reports
of individual variable LRDs existed (e.g., through serendipitous overlap of JWST programs),
but a systematic study of the full photometric population was lacking. This paper represents
the first large-scale, systematic photometric variability analysis of LRDs.

---

## Key Arguments and Derivations

### 1. Sample Construction and Field Coverage

The 314 LRDs are selected from five JWST fields:
- UNCOVER (Abell 2744 lensing field): 47 LRDs at $z \sim 3$--$8$
- CEERS: 62 LRDs at $z \sim 4$--$7$
- JADES: 89 LRDs at $z \sim 3$--$9$
- PRIMER-COSMOS: 73 LRDs at $z \sim 4$--$7$
- PRIMER-UDS: 43 LRDs at $z \sim 4$--$7$

Selection criteria follow the "V-shape SED + compactness" criteria established by Matthee
et al. (2024), requiring: (1) red $F277W - F444W > 1.0$ mag; (2) blue $F115W - F200W < 0.5$
mag; (3) half-light radius $< 2$ FWHM of the PSF; (4) photometric or spectroscopic redshift
$z > 3$.

### 2. Multi-epoch Photometric Measurement Strategy

The authors use all publicly available JWST NIRCam imaging with multi-epoch coverage.
Each field has 2--4 visits separated by 3--18 months in the observer frame (0.5--3 years in
the rest frame at $z \sim 5$). Photometry is performed consistently across epochs by:

- Using a fixed aperture (0.15 arcsec radius) centered on the PSF centroid
- Applying aperture corrections derived from isolated point sources in each epoch
- Computing an epoch-to-epoch systematic noise floor from a control sample of isolated
  point sources with similar magnitudes but lacking the LRD color selection

The variability significance for each LRD is quantified by:

$$V_{\rm sig} = \frac{|\Delta m|}{\sqrt{\sigma_1^2 + \sigma_2^2 + \sigma_{\rm sys}^2}}$$

where $\Delta m$ is the magnitude difference between epochs, $\sigma_{1,2}$ are the individual
epoch photometric uncertainties, and $\sigma_{\rm sys}$ is the systematic floor measured
from the control sample.

### 3. Population-Level Non-Detection

For the full sample of 314 LRDs, the distribution of $V_{\rm sig}$ values is consistent with
a Gaussian centered at zero with unit width -- i.e., no excess variance above the measurement
noise. The mean variability amplitude $\langle |\Delta m| \rangle = 0.04 \pm 0.01$ mag is
a factor of 5--10 below what standard DRW models predict for sub-Eddington AGN at the same
luminosities.

This non-detection is interpreted as evidence for super-Eddington accretion. In the slim-disk
(super-Eddington) regime, photon trapping at the trapping radius:

$$r_{\rm trap} = \frac{\dot{M}}{8\pi \rho_{\rm out} c} \sim \frac{\dot{M}}{\dot{M}_{\rm Edd}} r_S$$

suppresses short-timescale thermal instabilities because the radiation is advected inward
before it can produce observable flux changes. The super-Eddington disk has a much longer
effective thermal timescale than the sub-Eddington thin disk:

$$t_{\rm th,slim} \sim \frac{r_{\rm trap}}{c_s} \gg t_{\rm th,thin} \sim \frac{H}{c_s}$$

where $H \sim r_S$ for thin disk and $H \sim r_{\rm trap} \gg r_S$ for slim disk. Thus variability
is suppressed by the ratio $r_{\rm trap}/r_S = \dot{m}$ where $\dot{m} = \dot{M}/\dot{M}_{\rm Edd}$.

### 4. The Eight Variable Outliers

Eight LRDs (2.5% of the sample) show $V_{\rm sig} > 3$ and $|\Delta m| > 0.24$ mag,
inconsistent with non-variability at the $> 3\sigma$ level. These objects have:

- Variability amplitudes: 0.24, 0.31, 0.37, 0.41, 0.48, 0.53, 0.71, 0.82 mag
- Redshifts: $z \sim 3.5$--$6.5$
- Rest-frame wavelengths probed: $\sim 0.5$--$0.7$ micron (optical continuum)
- Timescales: 0.5--2 years in the rest frame

These amplitudes and timescales are consistent with DRW variability from a standard AGN disk.
The inference is that these eight LRDs are genuinely AGN-dominated -- the broad lines reflect
true BLR velocities, not gas-scattering artifacts. Black hole mass estimates from the virial
method applied to FWHM(H-alpha) yield $M_{\rm BH} \sim 10^7$--$10^9 M_\odot$, in the
range of standard broad-line AGN.

### 5. Implications for the LRD Population

The finding that only 2.5% of LRDs show clear AGN-like variability while the rest do not
implies that the majority of LRDs are either: (a) super-Eddington AGN with damped variability,
or (b) compact galaxies without significant AGN contribution. Both interpretations are
consistent with weak X-ray and radio emission. The eight variable LRDs provide a clean,
AGN-confirmed sub-sample for multiwavelength follow-up.

---

## Key Results

1. The LRD population (N = 314) shows no statistically significant average photometric
   variability -- mean $|\Delta m| = 0.04 \pm 0.01$ mag, a factor 5--10 below DRW predictions.
2. Non-variability is consistent with super-Eddington accretion (photon trapping suppresses
   disk fluctuations) or galaxy-dominated emission.
3. Eight variable LRDs with $|\Delta m| = 0.24$--$0.82$ mag are identified as AGN-confirmed
   sub-sample; $M_{\rm BH} \sim 10^7$--$10^9 M_\odot$ from virial method.
4. Variable fraction: 8/314 = 2.5%, suggesting most LRDs accrete super-Eddington or have
   non-AGN-dominated optical continua.
5. This is the first systematic large-sample variability study of the LRD population.
6. Published in ApJ 985, 119 (2025).

---

## Impact and Legacy

Zhang et al. (2024/2025) is a landmark paper because variability provides one of the cleanest
observational discriminators between AGN-dominated and galaxy-dominated LRDs, independent of
spectral modeling assumptions. The non-detection in 97.5% of the sample sets strong constraints
on sub-Eddington AGN models and provides concrete support for the super-Eddington accretion
picture championed by Inayoshi et al. (2024) and Pacucci et al. (2026).

The eight variable sources identified here are high-value targets for future spectroscopic
campaigns with JWST/NIRSpec, radio follow-up with ALMA or the ngVLA, and X-ray observation
with Chandra (for the lowest-redshift cases).

---

## Connection to Phonon-Exflation Framework

Photometric variability of AGN is driven by instabilities in the accretion disk on the thermal
timescale $t_{\rm th} \sim H/c_s$. In the phonon-exflation framework, the effective metric
on the compactification manifold sets the phonon propagation speed and, through the spectral
action, modifies the effective coupling constants at each energy scale. A slowly rolling
compactification radius (tau) would alter the fine-structure constant on cosmological timescales
-- but the clock constraint (Session 22d E-3) shows that $d\alpha/\alpha = -3.08 \dot{\tau}$,
meaning any detectable variation in alpha would be accompanied by a 15,000x stronger variation
in other fundamental constants. The non-variability of LRDs as a population is thus relevant:
if LRDs probe a specific cosmic epoch ($z \sim 4$--$8$) where phonon-exflation predicts
significant tau evolution, the absence of systematic photometric drift in 97.5% of the sample
provides an observational constraint on the rolling rate $\dot{\tau}$ at those epochs.
