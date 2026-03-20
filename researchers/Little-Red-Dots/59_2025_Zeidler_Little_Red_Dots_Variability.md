# Analysis of Multi-epoch JWST Images of ~300 Little Red Dots: Tentative Detection of Variability in a Minority of Sources

**Author(s):** Zeidler, P., et al.
**Year:** 2025
**Journal:** Astrophysical Journal 985, 119 (2025)
**DOI/arXiv:** 10.3847/1538-4357/abcd...

---

## Abstract

We present a systematic analysis of variability in ~300 Little Red Dots (LRDs) using multi-epoch JWST/NIRCam imaging across five deep extragalactic fields (Ultra Deep Field, GOODS-S, GOODS-N, ABELL 2744, COSMOS). By carefully accounting for systematic photometric zero-point variations between observation epochs, we derive a variability distribution for the LRD population. We find that the vast majority (>90%) of LRDs show no significant variability above noise levels (~5-10% in typical filters) on timescales of months to years in the rest-frame. However, we identify eight strongly variable candidates with brightness changes of 0.24-0.82 magnitudes. In two gravitationally-lensed LRDs, multi-image time delays of ~130 years (in the rest frame) enable measurement of color and flux variations independently in each image. We discuss interpretations ranging from super-Eddington accretion (which naturally suppresses variability through envelope damping) to composite systems where variable AGN components dominate the mid-infrared but are overshadowed by stable stellar components in the optical. Our results place constraints on the AGN fractional contribution and accretion geometry in LRDs.

---

## Historical Context

AGN variability has long been a diagnostic tool in understanding black hole accretion. Low-redshift AGN exhibit optical variability on timescales of days to years, with amplitude and timescale both correlated with black hole mass: more massive black holes vary more slowly and typically with smaller fractional amplitudes. The canonical model relates timescale to the viscous timescale in the accretion disk:

$$t_{\rm var} \propto \frac{r_{\rm ISCO}^2}{c s_c}$$

where r_ISCO is the innermost stable circular orbit and s_c is the sound speed in the disk.

For a 10^8 M_sun black hole, this predicts variability timescales of ~months to years. For a 10^6 M_sun black hole (as implied by electron-scattering mass estimates for LRDs), the timescale shortens to days to weeks.

However, super-Eddington accretion is theoretically expected to suppress variability. At lambda_Edd >> 1, the disk transitions from geometrically-thin to geometrically-thick, and radiation pressure support becomes dominant. The thick disk has high viscosity and long dynamical timescales, damping rapid fluctuations in the accretion rate. Additionally, the dense envelope reprocesses rapid flux changes, smoothing variability that would otherwise appear in the emitted spectrum.

Prior to this work, only handful of LRDs had been observed at multiple epochs with JWST, and no systematic population study of variability existed. The detection or non-detection of variability at the expected amplitude would be a key test of the super-Eddington accretion scenario and the age of the LRD population.

---

## Key Arguments and Derivations

### Systematic Photometry Across Epochs

A critical challenge in this work is accounting for systematic variations in JWST photometric zero points between observation epochs. JWST's absolute photometric accuracy is ~2-3%, and offsets between epochs can reach 5-10% if not carefully calibrated. For faint sources like LRDs, this systematic uncertainty can exceed the intrinsic variability signal.

The authors implement a self-referential calibration method: they identify ~500 non-variable reference stars in each field, measure their flux in each epoch, and use the median reference-star ratio to correct the zero-point offset. The uncertainty in the zero-point correction is estimated by the scatter in individual reference-star ratios:

$$\Delta m_{\rm sys} = \frac{1.086 \sigma(\ln f_{\rm ref})}{N_{\rm ref}^{1/2}}$$

where sigma(ln f_ref) is the scatter in reference-star flux ratios across epochs, and N_ref is the number of reference stars (~500).

For the typical GOODS-S field, this yields $\Delta m_{\rm sys}$ ~ 0.03 mag (3%). After correcting for the zero-point variation, the residual photometric uncertainty for individual sources is:

$$\Delta m_{\rm phot}^2 = \Delta m_{\rm zeropoint}^2 + \Delta m_{\rm sky}^2 + \Delta m_{\rm aperture}^2$$

Typical values for bright LRDs (F444W ~ 23 mag) are ~0.05 mag per epoch.

### Variability Metrics

The authors compute several variability metrics for each object:

1. **Fractional variability amplitude**:
$$f_{\rm var} = \sqrt{\frac{\sigma_{f}^2 - \sigma_{\rm err}^2}}{\langle f \rangle}$$
where sigma_f is the observed flux variance across epochs, sigma_err is the mean photometric uncertainty, and <f> is the mean flux.

2. **Excess variance ratio**:
$$\eta = \frac{\sigma_f^2 - \sigma_{\rm err}^2}{\sigma_{\rm err}^2}$$
A source is classified as significantly variable if eta > 1 (i.e., observed variance exceeds measurement error by factor >1).

3. **Maximum flux change**:
$$\Delta m_{\rm max} = \max(m_i) - \min(m_i)$$
the magnitude difference between brightest and faintest observations.

For the LRD population, the distribution of f_var values follows a Gaussian with mean ~ 0.04 (4% variability) and sigma ~ 0.03 (3%). This is entirely consistent with photometric noise and indicates that the population as a whole is not variable at >5% level.

### Lensed System Analysis

Two multiply-imaged LRDs in the ABELL 2744 field provide unique constraints. Gravitational lensing creates multiple images of the same source at different positions on the sky. The time delay between images is determined by the lensing geometry and can range from days to years.

The authors measure the time delay for LRD images A and B using spectroscopic redshifts (z_spec = 7.045) and lens mass modeling. The time delay is:

$$\Delta t = \frac{\phi_B - \phi_A}{c}$$

where phi_A and phi_B are the gravitational potential delays along the two light paths. They find Delta t ~ 130 years in the rest frame (~16 years observed frame).

Over this 130-year baseline, they measure H-alpha and H-beta equivalent widths:

- Image A: $W_{\rm H\alpha} = 1200 \pm 30$ A at epoch 1
- Image B: $W_{\rm H\alpha} = 1050 \pm 40$ A at epoch 1

The observed difference of ~150 A (12% change) is interpreted as intrinsic variation in the broad-line region of the AGN, occurring over ~130 years in the object's rest frame. Additionally, the continuum colors differ by ~0.1 magnitude between images, suggesting flux variations on the 130-year timescale.

This measurement provides direct evidence that at least some LRDs do exhibit variability on year-to-decade (rest-frame) timescales, consistent with accretion-disk variability in low-mass AGN.

---

## Key Results

1. **Overall population stability**: >90% of ~300 LRDs show no significant variability above photometric noise (~5%) on month-year timescales (rest-frame).

2. **Eight variable candidates**: Eight LRDs show Delta m_max = 0.24-0.82 mag, with excess variance ratio eta > 3. These likely represent genuine AGN-dominated systems.

3. **Variable fraction**: AGN-dominated LRDs (with strong Halpha broad lines in spectroscopy) show higher variability rates (~30-40%) than narrow-line or non-AGN LRDs (~5-10%).

4. **Lensed LRD findings**: Two multiply-imaged LRDs at z=7.045 show H-alpha equivalent-width variations of ~18% over 130 years (rest-frame), and continuum color variations of 0.1 mag.

5. **Timescale vs mass relation**: Observed variability timescales (~months to years at z~5-7 source frame) are consistent with accretion-disk viscous timescales for M_bh ~ 10^5-10^6 M_sun black holes.

6. **Super-Eddington damping**: Lack of rapid variability in most LRDs is consistent with damping by geometrically-thick accretion disks expected at lambda_Edd > 1.

7. **AGN fraction constraint**: Variability detections suggest 10-20% of LRDs have strong AGN contributions; remainder may be composite (AGN + starburst) or purely starburst-dominated.

---

## Impact and Legacy

This paper is the first systematic population study of LRD variability and establishes variability as a diagnostic tool for understanding LRD nature. The finding that most LRDs are variability-poor contrasts with low-redshift AGN, supporting the super-Eddington accretion scenario. The detection of variability in a minority of sources indicates that LRD population is heterogeneous, with a range of accretion rates and geometries.

The lensed-system time-delay measurements are particularly significant. They provide direct measurements of AGN-induced variability on timescales that are impossible to measure for unlensed sources—time delays of 100+ years in the source frame can be captured in a single observation epoch of the lensed images. This technique opens a new avenue for studying high-redshift AGN at much finer temporal resolution than conventional reverberation mapping.

Follow-up studies have used these findings to constrain the AGN and starburst contributions to LRD SEDs, measure black hole masses from variability timescales, and test whether LRD environments are particularly conducive to damping variability.

---

## Connection to Phonon-Exflation Framework

**Relevance: Very Low (time-domain AGN properties disconnected from NCG/particle physics).**

Time-domain AGN variability is governed by accretion-disk physics and black hole thermodynamics—subjects largely orthogonal to the noncommutative geometry and spectral action principles underlying phonon-exflation. The variability timescales depend on M_bh, spin, and accretion rate; none of these are directly constrained by NCG.

However, a potential connection exists through AGN feedback mechanisms. If super-Eddington accretion in LRDs produces strong radiative winds or jets (implications of thick-disk physics), this feedback could affect host-galaxy evolution and star-formation efficiency. In a phonon-exflation cosmology where early-universe physics differs from LCDM, the feedback cycle might be altered, affecting the expected LRD abundance or properties at a given redshift. But this remains speculative without detailed modeling.

The robust detection of low variability in most LRDs is valuable as a consistency check: it suggests that LRD accretion is indeed in a super-Eddington or high-lambda_Edd regime, confirming that these are very young systems where rapid growth is occurring. This accretion-rate constraint is a boundary condition that must be satisfied by any complete early-universe cosmology, including phonon-exflation models.

---
