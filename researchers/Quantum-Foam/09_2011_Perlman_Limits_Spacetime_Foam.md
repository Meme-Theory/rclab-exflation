# Limits on Spacetime Foam from Quasar Imaging

**Author(s):** Eric S. Perlman, Y. Jack Ng, David Bao, et al.
**Year:** 2011
**Journal:** Physical Review D, Vol. 83, 084003

---

## Abstract

Perlman et al. provide the first stringent observational constraints on spacetime foam models using high-resolution imaging of distant quasars from the Hubble Ultra-Deep Field. The key idea is that quantum-foam-induced diffraction of photon wavefronts should blur the images of distant point sources. The amplitude of this blurring depends on the foam model: random-walk foam predicts linear diffusion, while holographic foam predicts cube-root scaling.

By measuring the angular size of point-spread functions (PSFs) in HST observations at high resolution, the authors find that neither the random-walk nor the standard holographic model fits the data well. Specifically, random-walk foam with $\alpha \approx 1$ is ruled out at high significance, while holographic foam remains marginally consistent with $\alpha \approx 0.5$. This paper established quasar imaging as the most stringent astrophysical test of spacetime foam, displacing earlier work on gamma-ray timing.

The result is remarkable: quasar images provide a cleaner test of Planck-scale physics than direct Planck-energy observations, because the effect accumulates over cosmological distances.

---

## Historical Context

In the 2000s, several independent observational programs aimed to test spacetime foam:

1. **Gamma-ray bursts** (Amelino-Camelia, 1999-2010): searching for energy-dependent arrival time delays
2. **Cosmic rays** (IceCube, MAGIC): searching for violations of the GZK cutoff
3. **Gravitational waves** (LIGO, Virgo): searching for foam-induced noise
4. **Quasar imaging** (Perlman et al., 2006-2011): searching for image blur

The quasar imaging approach has several advantages:

- **Passive observations**: No need for extraordinary detectors; uses existing HST data
- **Clean geometry**: Point sources at known distances; clear null hypothesis
- **Long baseline**: Distances of Gigaparsecs (billions of light-years) mean huge photon propagation distances
- **Multiple wavelengths**: HST observes in multiple UV, visible, and near-IR bands; can search for wavelength dependence

By 2011, Perlman's group had accumulated enough data to make strong statements.

---

## Key Arguments and Derivations

### Diffraction from Spacetime Fuzziness

A photon wavefront propagating through fuzzy spacetime acquires random phase fluctuations. At each infinitesimal distance $dr$, the phase shift is:

$$d\phi \sim \frac{\omega}{c} \sqrt{\ell_P / r} \, dr$$

where $\omega$ is the angular frequency and $r$ is the distance propagated.

Integrating over a propagation distance $d$:

$$\Delta \phi \sim \omega \sqrt{\ell_P d / c}$$

This phase error causes diffraction. The diffraction-limited angular resolution of an optical system with wavelength $\lambda$ and aperture diameter $D$ is:

$$\theta_{\text{diffraction}} \sim \lambda / D$$

However, if the wavefront itself is fuzzy, the effective angular blur is:

$$\theta_{\text{foam}} \sim \frac{\Delta \phi}{\text{wavenumber}} \sim \frac{\Delta \phi}{2\pi/\lambda}$$

$$\theta_{\text{foam}} \sim \frac{\lambda}{2\pi} \cdot \frac{\omega \sqrt{\ell_P d / c}}{1} \sim \sqrt{\ell_P d} \frac{\nu}{c}$$

where $\nu = \omega/(2\pi)$ is the frequency.

### Different Foam Models

Different quantum-gravity models predict different functional forms:

**Random-walk foam** (Ng-van Dam):
$$\theta_{\text{RW}}^2 \sim \ell_P d \, \nu$$

**Holographic foam** (cube-root scaling):
$$\theta_{\text{HO}}^3 \sim \ell_P d \, \nu$$

More generally:
$$\theta^{1/\alpha} \sim (\ell_P d \nu)^{1/3}$$

with $\alpha = 1$ for random-walk and $\alpha = 3$ for holographic.

### Observational Test: Point Spread Function

For a quasar at cosmological distance $d$, imaged with HST:

1. **Intrinsic size**: Quasar cores are unresolved point sources; effective angular size $\sim 0$ (or $<10$ microarcsec)

2. **Atmospheric blur**: Eliminated by HST (space-based observatory)

3. **Optical diffraction**: $\theta_{\text{diffraction}} = 1.22 \lambda/D \approx 0.05$ arcsec for HST

4. **Foam blur**: $\theta_{\text{foam}} \sim \sqrt{\ell_P d}$

For a source at $d = 1$ Mpc ($10^{24}$ cm):
$$\theta_{\text{foam, RW}} \sim 10^{-27} \text{ arcsec}$$

For $d = 1$ Gpc ($10^{27}$ cm):
$$\theta_{\text{foam, RW}} \sim 10^{-23} \text{ arcsec}$$

While tiny, HST's angular resolution is $\sim 0.05$ arcsec $= 50$ milliArcsec. So the foam blur is 25 orders of magnitude smaller! This seems hopeless.

**However**: the effect is cumulative, and modern analysis of PSFs can achieve sub-pixel precision. Moreover, at shorter wavelengths (UV), the effect is larger (because $\theta \propto \nu$).

### The HST Ultra-Deep Field Sample

Perlman et al. observed a large sample of high-redshift quasars in the Hubble Ultra-Deep Field (HUDF), achieving:

- **Sample size**: 100+ quasars at redshift $z = 2$--$10$
- **Wavelength coverage**: UV to near-IR (200 nm to 1600 nm)
- **Angular resolution**: 0.05 arcsec to 0.1 arcsec

For each quasar, they measure the FWHM (full width at half maximum) of the PSF:

$$\text{FWHM}_{\text{obs}} = \sqrt{\text{FWHM}_{\text{PSF}}^2 + \theta_{\text{foam}}^2}$$

### Constraints from FWHM Data

Comparing observed PSFs to models:

**Random-walk foam** ($\alpha = 1$, linear diffusion):
$$\theta_{\text{RW}} = \alpha_{\text{RW}} \sqrt{\ell_P d}$$

where $\alpha_{\text{RW}}$ is a model-dependent coefficient. The data constrain:

$$\alpha_{\text{RW}} < 0.8 \quad (95\% \text{ CL})$$

This rules out standard random-walk models.

**Holographic foam** ($\alpha = 3$, cube-root scaling):
$$\theta_{\text{HO}} = \alpha_{\text{HO}} (\ell_P d)^{1/3}$$

The data allow:

$$\alpha_{\text{HO}} < 0.5 \quad (68\% \text{ CL}), \quad \alpha_{\text{HO}} < 1.2 \quad (95\% \text{ CL})$$

Holographic foam remains consistent with observations, but only marginally.

### Wavelength Dependence

Examining the PSF size as a function of wavelength $\lambda$:

$$\text{FWHM}(\lambda) = \text{FWHM}_0 \sqrt{1 + (\lambda/\lambda_{\text{critical}})^{-1}}$$

where $\lambda_{\text{critical}}$ encodes the foam contribution. The data search for this dependence.

Finding: **No significant wavelength dependence detected**. This constrains models where foam effects scale differently at different wavelengths (e.g., DSR-type models).

---

## Key Results

1. **Random-walk foam ruled out**: Linear diffusion models are excluded at high confidence.

2. **Holographic foam remains viable**: Cube-root scaling models are consistent with data.

3. **Stringent Planck-scale constraints**: Effective constraints on foam models approach $\Delta\theta \lesssim 10^{-24}$ arcsec, corresponding to distance scales $\sim 10^{-18}$ m.

4. **Distance-cumulative effect**: The long photon propagation distance (Gigaparsecs) makes quasar imaging more sensitive to Planck-scale effects than direct Planck-energy experiments.

5. **Model discrimination**: Different foam models make different predictions for PSF size, wavelength dependence, and redshift evolution. These can be tested systematically.

6. **Future sensitivity**: Next-generation optical telescopes (ELT, TMT) combined with space-based observations could improve constraints by orders of magnitude.

---

## Impact and Legacy

Perlman's 2011 paper established quasar imaging as the premier observational test of spacetime foam:

1. **Methodology**: Demonstrated that high-precision imaging of distant point sources is a powerful tool for Planck-scale physics.

2. **Observations guide theory**: Observations began constraining theoretical models rather than vice versa.

3. **Multi-wavelength strategy**: Showed importance of testing foam models across wavelength ranges.

4. **Future observations**: Motivated systematic surveys of distant quasars, GRBs, and other point sources in ongoing (2015-2025) and future observatories.

5. **Null result interpretation**: Even null results (ruling out certain foam models) are scientifically valuable, narrowing the parameter space for quantum gravity.

---

## Connection to Phonon-Exflation Framework

**High relevance (astrophysical observational tests)**:

Perlman's quasar imaging methodology directly applies to testing phonon-exflation predictions:

1. **Image blurring from internal geometry**: If phonon-exflation is correct, photon wavefronts should be blurred by interactions with phononic excitations in the internal SU(3) manifold.

2. **Spectral dependence**: The blurring should have specific frequency/wavelength dependence encoded in the phonon dispersion relation.

3. **Redshift dependence**: Blurring should evolve with redshift, reflecting how phonon modes change over cosmic time.

4. **Wavefront distortion**: Not just diffuse blur, but structured wavefront distortions from the discreteness of the internal manifold (analogous to random-walk foam structure).

5. **Model discrimination**: Measuring PSF size across redshifts and wavelengths can distinguish phonon-exflation from other quantum-gravity models (Carlip foam, DSR, etc.).

6. **Quantitative predictions**: Phonon-exflation must predict specific functional form for $\theta_{\text{foam}}(\lambda, z)$. Perlman's methodology provides direct test.

**Potential signatures**:

- If phonons produce $(L/\ell_P)^{2/3}$ diffusion (similar to holographic foam), PSF should show $d^{1/3}$ scaling
- If phonons are discrete (which they are), PSF might show oscillatory or non-monotonic redshift evolution
- Spectral dependence $\theta \propto \nu$ (or different power law) encodes phonon dispersion relation

---

## Key Equations

| Equation | Meaning |
|:---------|:---------|
| $d\phi \sim \omega\sqrt{\ell_P/r} dr$ | Phase fluctuation per unit path |
| $\Delta \phi \sim \omega\sqrt{\ell_P d/c}$ | Total phase error |
| $\theta_{\text{foam}} \sim \sqrt{\ell_P d}$ | Angular blur (random-walk) |
| $\theta_{\text{foam}} \sim (\ell_P d)^{1/3}$ | Angular blur (holographic) |
| $\text{FWHM}^2 = \text{FWHM}_0^2 + \theta_{\text{foam}}^2$ | Observed PSF size |
| $\theta_{\text{diffraction}} = 1.22\lambda/D$ | Diffraction-limited resolution |

---

## Primary Source

Perlman, E.S., Ng, Y.J., Bao, D., et al. (2011). "Limits on Spacetime Foam." *Physical Review D*, Vol. 83, 084003.
doi: 10.1103/PhysRevD.83.084003
