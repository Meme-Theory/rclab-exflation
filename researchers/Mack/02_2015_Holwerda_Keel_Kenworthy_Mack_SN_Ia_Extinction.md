# The Dependence of the A_V Prior for SN Ia on Host Mass and Disk Inclination

**Author(s):** B.W. Holwerda, W.C. Keel, M.A. Kenworthy, K.J. Mack
**Year:** 2015
**Journal/ArXiv:** arXiv:1505.03949

---

## Abstract

Supernovae type Ia (SN Ia) are used as "standard candles" for cosmological distance scales. To fit their light curve shape-absolute luminosity relation, one must assume an intrinsic color and a likelihood of host galaxy extinction (or convolution of these)--a color distribution prior. The host galaxy extinction prior is typically assumed to be an exponential dropoff for current supernova programs: P(A_V) ∝ e^{-A_V/tau_0}. The authors explore the validity of this prior using the distribution of extinction values inferred when two galaxies accidentally overlap (an occulting galaxy pair). Supernova luminosity distances from the SDSS-III Supernova projects (SDSS-SN) are corrected by matching the host galaxies to one of three templates from occulting galaxy pairs based on host galaxy mass and the A_V-bias-prior-scale relation from Jha et al. (2007). They find that introducing an A_V prior that depends on host mass results in lowered luminosity distances for the SDSS-SN on average, but does not reduce scatter in individual measurements.

---

## Historical Context

Type Ia supernovae have become the foundation of modern observational cosmology, providing evidence for cosmic acceleration and the discovery of dark energy. However, their application as "standard candles" depends critically on accurate distance measurements. The method requires fitting the light curve shape-absolute luminosity relationship (Phillips relation), which in turn requires assumptions about intrinsic color and host galaxy extinction.

The standard approach in supernova cosmology has long assumed that extinction follows an exponential prior with a fixed scale height tau_0. This assumption simplifies analysis but may not reflect the actual distribution of extinction in host galaxies. Different host galaxy properties--particularly stellar mass and morphology--likely correlate with dust properties and extinction distributions, yet these correlations have been poorly characterized.

Holwerda et al. develop a novel method to empirically constrain the extinction prior using accidental galaxy-galaxy overlaps (occulting pairs). When two galaxies overlap along the line of sight, the reddened galaxy's colors provide a direct measure of extinction. By collecting many such natural experiments, they can infer the true extinction distribution as a function of galaxy properties and use this to recalibrate SN Ia distances.

---

## Key Arguments and Derivations

### Standard Candle Method and Extinction Corrections

Type Ia supernovae follow the Phillips relation, which relates the supernova's absolute magnitude M to the light curve decline rate s:

$$M = M_0 + \alpha s$$

where $M_0$ is a reference magnitude and $\alpha$ is an empirical slope (~0.7-0.8 mag per 0.1 decline-rate unit). In practice, supernova observations measure apparent magnitudes m, which are related to absolute magnitude and distance modulus by:

$$m = M + \mu + A_V$$

where $\mu = 5 \log_{10}(d) - 5$ is the distance modulus in megaparsecs, and $A_V$ is the extinction (visual extinction) through the host galaxy and Milky Way. Measuring $\mu$ therefore requires accurate knowledge of extinction.

### Extinction Prior Framework

The host galaxy extinction is parameterized by a probability distribution. The standard assumption has been:

$$P(A_V) \propto e^{-A_V/\tau_0}$$

where $\tau_0$ is a scale parameter typically set to a constant value (often around 0.3-0.4 magnitude). This exponential prior is convenient for Bayesian analysis but lacks empirical justification.

Holwerda et al. challenge this assumption by examining how extinction varies with galaxy properties. They introduce a mass-dependent prior:

$$P(A_V | M_*) \propto e^{-A_V/\tau_0(M_*)}$$

where the scale height $\tau_0$ is a function of stellar mass $M_*$.

### Occulting Galaxy Pair Method

The key innovation is using accidentally-overlapping galaxy pairs to empirically measure extinction distributions. When a background galaxy is partially obscured by a foreground galaxy, the color excess between the obscured and unobscured portions directly measures extinction through the foreground disk.

For a color index C (e.g., u-r color), the color excess is:

$$E(C) = C_{obscured} - C_{unobscured} = A_{C,dust} - A_{V,dust} \times R_C$$

where $R_C$ is the reddening coefficient. By collecting many such measurements across different foreground galaxies with known properties, the distribution of extinction as a function of galaxy mass and orientation can be determined empirically.

### SDSS-SN Analysis

The SDSS-III Supernova projects provide a large sample of SN Ia with well-measured host galaxy properties. The analysis proceeds by:

1. Classifying each SDSS-SN host galaxy by stellar mass (estimated from photometry or spectroscopy)
2. Selecting an occulting pair template that matches the host mass and disk inclination
3. Assigning the extinction distribution from that template to the SN Ia
4. Recalculating luminosity distances using the mass-dependent prior

The sample spans from low-mass hosts ($\log_{10}(M_*/M_\odot) \sim 9$) to high-mass hosts ($\log_{10}(M_*/M_\odot) \sim 11$), allowing study of how extinction prior depends on stellar mass.

---

## Key Results

1. **Extinction prior depends on host mass**: The scale parameter $\tau_0$ is not constant but varies systematically with host galaxy stellar mass. Lower-mass galaxies (roughly $\log_{10}(M_*/M_\odot) < 10$) show lower mean extinction ($\langle A_V \rangle \lesssim 0.1$ mag), while higher-mass galaxies exhibit higher typical extinction values.

2. **Inclination dependence**: Disk inclination (orientation relative to line of sight) also affects extinction distribution. Edge-on galaxies show higher extinction variance than face-on galaxies, as expected from dust geometry.

3. **Luminosity distance corrections**: Applying mass-dependent extinction priors results in systematically lowered luminosity distances for SDSS-SN when compared to the standard fixed-prior analysis. For low-mass hosts, distances decrease on average by several percent; for high-mass hosts, changes can exceed 5-10%.

4. **No scatter reduction**: Despite lowering luminosity distances on average, the mass-dependent prior does not reduce the scatter in individual distance measurements. This indicates that host mass and inclination capture some systematic trends but do not explain the full range of supernova-to-supernova variation.

5. **Template matching**: Three template extinction distributions (derived from occulting pairs) are sufficient to characterize most of the mass and inclination dependence. The results suggest a simple mass-scaling of the extinction prior scale is viable.

---

## Impact and Legacy

This work demonstrates that extinction priors in SN Ia cosmology are not universal but depend on host galaxy properties. The technique of using occulting galaxy pairs provides an empirical handle on dust properties difficult to access otherwise. The findings have implications for SN Ia distance measurements and systematic uncertainties in dark energy constraints derived from SN Ia samples.

The study contributes to understanding systematic uncertainties in Type Ia supernova cosmology. While the mass-dependent extinction correction improves the physical realism of the prior, the persistence of scatter in distance measurements points to additional sources of supernova-to-supernova variation (possibly intrinsic supernova physics, dust properties not captured by mass/inclination, or residual extinction variation) that remain to be addressed.

---

## Connection to Phonon-Exflation Framework

In the context of phonon-exflation cosmology, SN Ia distance measurements are critical for constraining the cosmic expansion history and equation-of-state parameter w(z) of the dark energy. The framework predicts w=-1 exactly, providing a specific testable prediction against observations.

Holwerda et al.'s work on extinction priors is directly relevant because systematic uncertainties in SN Ia luminosity distances propagate into dark energy constraints. The framework's geometric origin of dark energy (from the spectral action of M4 x SU(3) compactification) predicts a specific form of w(z) that must be tested against observed distances. Improved extinction corrections--accounting for mass and inclination dependence--reduce a major source of systematic uncertainty in distance measurements.

The study also highlights how observable properties of host galaxies (stellar mass, morphology) correlate with environmental properties (dust content, extinction). In phonon-exflation terms, this could reflect how the density of dark matter (coupled to baryonic structure through gravity) affects dust properties and extinction in galaxies of different masses. The framework predicts that dark matter distribution follows the geometry of the compactified space, which manifests in galaxy-scale properties. Therefore, mass-dependent extinction prior could encode information about the coupling between the emergent dark matter and baryonic structure, providing an indirect probe of the geometric underpinning of the framework.
