# Probing Spacetime Foam with Extragalactic Sources of High-Energy Photons

**Author(s):** Richard Lieu, Lloyd W. Hillman, Helmut K. Christiansen, et al.
**Year:** 2006
**Journal:** Physical Review Letters, Vol. 96, 051301

---

## Abstract

Lieu, Hillman, and Christiansen propose using observations of high-energy (TeV to GeV) photons from distant sources to test spacetime foam. Their key insight is that TeV photons are particularly sensitive to foam-induced wavefront distortions because:

1. High-energy photons have short wavelengths, leading to large diffraction angles in a fuzzy spacetime
2. They travel over cosmological distances, accumulating phase errors
3. They can be detected with high precision using modern Cherenkov telescopes

The authors analyze how foam-induced phase incoherence affects the arrival angle and timing of high-energy photons. For distant sources like gamma-ray bursts, quasars, and active galactic nuclei, they show that spacetime foam effects produce measurable changes in angular size, spectral properties, and temporal structure of the emission.

This paper established high-energy astrophysics as a major testing ground for quantum-gravity phenomenology, complementing Amelino-Camelia's GRB timing studies and Perlman's quasar imaging work.

---

## Historical Context

By the mid-2000s, ground-based gamma-ray telescopes (MAGIC, VERITAS, H.E.S.S., CANGAROO) were achieving sensitivity to TeV-scale gamma rays from distant astrophysical sources. Simultaneously, quantum-gravity phenomenology was proposing that such observations could detect Planck-scale physics.

The motivation was twofold:

1. **Technical**: TeV telescopes were achieving higher precision and sensitivity
2. **Theoretical**: TeV photons, with wavelength $\lambda = hc/E \sim 10^{-22}$ cm, interact with spacetime structure at scales approaching $10^{-16}$ cm -- much larger than Planck length but still quantum-gravity-relevant

Lieu et al. recognized that foam effects on TeV photons were cumulative and potentially observable.

---

## Key Arguments and Derivations

### Photon Propagation Through Fuzzy Spacetime

A high-energy photon of energy $E$ propagating through spacetime with fluctuating metric acquires a wave-front distortion. At each distance element $dr$, the phase error is:

$$d\phi(E) \sim \frac{2\pi}{\lambda} \sqrt{\ell_P/r} \, dr = \frac{E}{\hbar c} \sqrt{\ell_P/r} \, dr$$

Integrating from source (distance $d$) to observer:

$$\Delta\phi(E) \sim \frac{E}{\hbar c} \sqrt{\ell_P d}$$

This phase error causes the photon wavefront to become distorted. The wavefront deviations scale as:

$$\Delta\theta(E) \sim \frac{\Delta\phi}{(2\pi/\lambda)} = \frac{\hbar c}{E} \times \frac{E}{\hbar c}\sqrt{\ell_P d} = \sqrt{\ell_P d}$$

Remarkably, the energy dependence cancels! The angular deviation is energy-independent at leading order.

However, at higher orders (two-photon-like processes, or if different foam models apply), energy dependence can reappear.

### Incoherence of Wavefront

An extended source (angular size $\theta_s$) becomes blurred when its wavefront passes through fuzzy spacetime. The coherence length of the radiation becomes:

$$\ell_{\text{coh}} \sim \frac{\lambda}{(\Delta\phi)/(2\pi)} \sim \frac{\lambda}{\sqrt{\ell_P d}}$$

For $\lambda = 10^{-12}$ cm (optical) and $d = 1$ Gpc:

$$\ell_{\text{coh}} \sim 10^{-12} / \sqrt{10^{-33} \times 10^{27}} \sim 10^{-12} / 10^{-3} = 10^{-9} \text{ cm}$$

This is macroscopic! An optical image from a distant source would have coherence over millimeter scales, then become incoherent beyond that. A TeV photon (smaller wavelength) would have even shorter coherence length.

### Spectral Signature

If foam causes phase incoherence, the spectrum of a distant source should be affected:

1. **Suppression of fine structure**: High-frequency (angular frequency sense) components of the source's radiation pattern are washed out.

2. **Reddening**: Phase diffusion effectively introduces an absorption-like process, suppressing high-energy photons more than low-energy ones. A spectrum $N(E) \propto E^{-\Gamma}$ becomes modified to:

$$N_{\text{obs}}(E) \propto E^{-\Gamma} \exp(-\alpha E^{\beta})$$

where $\alpha, \beta$ depend on the foam model.

3. **Apparent spectral break**: If the source has intrinsic spectral features (breaks, cutoffs), foam can shift or smear these features.

### Time-Domain Signature: Microlensing-like Effects

Foam-induced phase fluctuations also affect the temporal structure of radiation. For a time-variable source (like a gamma-ray burst), the emission at different frequencies experiences slightly different propagation times:

$$\Delta t(E) \sim \frac{d}{c} \left(\frac{E}{E_P}\right)^\beta$$

where $\beta$ depends on the foam model. Comparing time-of-arrival of low-energy and high-energy photons can measure $\beta$ and constrain foam models.

For $E_{\text{low}} = 1$ MeV and $E_{\text{high}} = 10$ GeV, and $d = 1$ Gpc:

$$\Delta t \sim 10^9 \text{ s} \times 10^{-60} \sim 10^{-50} \text{ s}$$

With $\beta = 1$. This seems unmeasurable, but for burst sources with short timescales or coherent pulsars, it might accumulate to detectable levels.

### Angular Blurring of Point Sources

A point source (angular size $\theta_s \to 0$) appears blurred to angular size:

$$\theta_{\text{blur}} \sim \sqrt{\ell_P d}$$

For $d = 1$ Gpc:

$$\theta_{\text{blur}} \sim \sqrt{10^{-33} \times 10^{27}} \sim 10^{-3} \text{ arcsec} = 3 \text{ marcsec}$$

This is above atmospheric turbulence limits and potentially detectable with large ground-based telescopes or space-based observations.

### Extragalactic Source Distances

The paper emphasizes using distant sources to maximize the foam effect:

| Source Type | Typical Distance | Redshift | Effect Size |
|:------------|:-----------------|:---------|:-----------|
| Nearby quasar | 100 Mpc | $z = 0.02$ | $\theta \sim 10^{-5}$ arcsec |
| Distant quasar | 1 Gpc | $z = 2$ | $\theta \sim 10^{-3}$ arcsec |
| GRB (far) | 10 Gpc | $z = 10$ | $\theta \sim 10^{-2}$ arcsec |
| AGN (Mrk 421) | 150 Mpc | $z = 0.031$ | $\theta \sim 10^{-6}$ arcsec |

Distant sources give larger effects, but are fainter. A trade-off exists between sensitivity and distance.

---

## Key Results

1. **TeV photons are sensitive probes**: High-energy photons accumulate phase errors over cosmological distances, making them sensitive to Planck-scale fluctuations.

2. **Multiple observational signatures**: Foam effects manifest in:
   - Angular blurring
   - Spectral distortion
   - Temporal dispersion
   - Wavefront incoherence

3. **Energy-independent angular blur** (at leading order): Surprisingly, the foam-induced angular deviation does not depend on photon energy (though higher-order terms do).

4. **Detectable effects**: For distant sources ($d \sim 1$--$10$ Gpc), foam-induced angular blur $\sim 10^{-3}$--$10^{-2}$ arcsec is above detection threshold of modern ground-based telescopes.

5. **Spectral signature**: Foam-induced phase incoherence produces reddening and spectral break shifts in distant AGN and quasar spectra.

6. **Multiplet observation strategy**: Observing the same source type at multiple redshifts allows measurement of the distance scaling ($d^{1/3}$ for holographic foam, $d^{1/2}$ for random-walk), distinguishing models.

---

## Impact and Legacy

Lieu et al.'s 2006 paper established TeV astrophysics as a frontier for quantum-gravity phenomenology:

1. **Ground-based gamma-ray astronomy connection**: Connected the booming field of ground-based TeV observations to fundamental physics.

2. **GRB timing motivation**: Motivated multi-wavelength observations of gamma-ray bursts searching for energy-dependent delays (later pursued by Fermi, Swift).

3. **Spectral analysis methods**: Developed techniques for extracting foam constraints from spectral data.

4. **Future surveys**: Encouraged systematic observations of distant TeV sources with MAGIC, VERITAS, H.E.S.S., and later Cherenkov Telescope Array.

5. **Complementary probes**: TeV observations complement:
   - Quasar PSF measurements (Perlman)
   - GRB timing (Amelino-Camelia)
   - Gravitational wave detection (Amelino-Camelia)

---

## Connection to Phonon-Exflation Framework

**High relevance (high-energy astrophysics phenomenology)**:

Lieu et al.'s TeV astrophysics approach is directly applicable to phonon-exflation tests:

1. **High-energy probe**: TeV photons interact with quantum-gravity structure at scales comparable to phonon wavelengths in phonon-exflation. The physics should be similar.

2. **Energy-dependent propagation**: If phonon-exflation predicts energy-dependent propagation of photons through the vacuum (via internal-manifold phonons), TeV observations can test this.

3. **Spectral signatures**: The predicted spectral distortion from phonons should match the methods developed by Lieu et al. for analyzing foam effects.

4. **Wavefront distortion**: If phonons cause wavefront incoherence, this should be detectable as blurring of distant point sources -- exactly the effect Lieu et al. analyze.

5. **Redshift evolution**: Phonon-exflation predicts how the effective Planck scale or foam structure evolves with redshift (cosmic age). TeV observations at multiple redshifts test this.

6. **Quantitative model discrimination**: Using Lieu et al.'s methodology, one can measure specific parameters of the phonon-exflation spectrum (dispersion relation exponents, coupling strength, etc.).

**Specific testable predictions**:

- Angular blur $\theta(d, E, z)$ encodes phonon spectrum
- Spectral distortion amplitude and functional form reveal phonon density
- Time-of-arrival delays distinguish phonon-exflation from other foam models

---

## Key Equations

| Equation | Meaning |
|:---------|:---------|
| $d\phi(E) \sim (E/\hbar c)\sqrt{\ell_P d}$ | Phase error for photon energy E |
| $\Delta\theta(E) \sim \sqrt{\ell_P d}$ | Angular blur (energy-independent) |
| $\ell_{\text{coh}} \sim \lambda/\sqrt{\ell_P d}$ | Wavefront coherence length |
| $N_{\text{obs}}(E) \propto N_0(E) \exp(-\alpha E^\beta)$ | Foam-affected spectrum |
| $\Delta t \sim (d/c)(E/E_P)^\beta$ | Time-of-arrival dispersion |
| $\theta_{\text{blur}} \sim \sqrt{\ell_P d}$ | Angular size of blurred source |

---

## Primary Source

Lieu, R., Hillman, L.W., Christiansen, H.K., et al. (2006). "Probing Spacetime Foam with Extragalactic Sources of High-Energy Photons." *Physical Review Letters*, Vol. 96, 051301.
doi: 10.1103/PhysRevLett.96.051301
