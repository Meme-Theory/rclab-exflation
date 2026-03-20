# Detection of the Baryon Acoustic Peak in the Large-Scale Correlation Function of SDSS Luminous Red Galaxies

**Author(s):** Daniel J. Eisenstein, Idit Zehavi, David W. Hogg, et al.

**Year:** 2005

**Journal:** The Astrophysical Journal, Volume 633, Pages 560--574

---

## Abstract

Using a spectroscopic sample of 46,748 luminous red galaxies (LRGs) from the Sloan Digital Sky Survey (SDSS), Eisenstein and collaborators detect a prominent peak in the two-point correlation function at a separation of ~100 h^-1 Mpc. This peak is the imprint of baryon acoustic oscillations (BAO)—sound waves in the primordial plasma that propagated during the first ~300,000 years after the Big Bang. The BAO peak serves as a "standard ruler" for measuring cosmic distances, enabling precise measurements of the expansion history of the universe and constraining dark energy properties. This landmark paper transformed cosmology by making dark energy measurable through large-scale structure.

---

## Historical Context

Baryon acoustic oscillations were predicted theoretically in the 1980s-1990s but were too small to detect in earlier galaxy surveys. By 2005, the SDSS had accumulated enough high-quality redshifts of distant galaxies to make BAO detectable. Eisenstein's team designed the LRG sample to be luminous and thus traceable to large distances, maximizing cosmic volume sampled. The detection of the BAO peak was immediately recognized as revolutionary: for the first time, one could use the BAO scale (set in the early universe) as a cosmic ruler to measure distances at late times, providing a powerful probe of dark energy independent of supernovae or the CMB.

---

## Key Arguments and Derivations

### Baryon Acoustic Oscillations in the Primordial Plasma

In the early universe (z ~ 1000), before recombination, baryons and photons formed a tightly coupled plasma. Sound waves propagated through this plasma at the speed of sound:

$$c_s = \frac{c}{\sqrt{3(1 + 3 \rho_b / 4 \rho_\gamma)}}$$

where $\rho_b$ is the baryon density and $\rho_\gamma$ is the radiation density. At recombination (z ~ 1100), when electrons combined with protons and the universe became transparent, these sound waves "froze" into the density distribution of matter. Overdense regions (where sound waves compressed the plasma) became clusters; underdense regions became voids.

The **sound horizon** is the distance a sound wave travels from the Big Bang to recombination:

$$r_s = \int_0^{z_{\text{rec}}} \frac{c_s dz'}{H(z')}$$

For ΛCDM with current parameters, $r_s \approx 150$ Mpc/h (comoving).

This sound horizon scales as $r_s \propto \sqrt{\Omega_b h^2 / \Omega_m h^2}$ and is well-determined from CMB measurements, making it a **standard ruler**—a length scale set in the early universe that can be measured at later times.

### Two-Point Correlation Function and the BAO Peak

The two-point correlation function $\xi(r)$ measures the excess probability of finding galaxies at separation $r$:

$$\xi(r) = \left\langle \frac{dN(r, r+dr)}{4\pi r^2 \bar{n} dr} - 1 \right\rangle$$

where $\bar{n}$ is the mean galaxy number density and $dN$ is the number of galaxy pairs at separation $r$.

On large scales (~50-200 Mpc), the correlation function exhibits structure from linear perturbations in the initial density field. The key feature is a **peak** at the BAO scale $r_{\text{BAO}} \sim r_s$:

$$\xi(r) = \xi_{\text{smooth}}(r) + A_{\text{BAO}} \exp\left( - \frac{(r - r_s)^2}{2\sigma_v^2} \right)$$

The peak arises because matter preferentially accumulates at distances close to $r_s$ from overdense regions (due to acoustic oscillations in the early universe). The width of the peak (Gaussian width $\sigma_v \sim 150$ km/s in redshift space) is broadened by peculiar velocities and non-linear structure growth.

### Measurement Technique: LRG Sample Design

To detect the BAO peak with high signal-to-noise, Eisenstein's team designed the LRG sample to maximize:

1. **Volume sampled**: Use galaxies at large distances (z ~ 0.35 for SDSS LRGs)
2. **Number density**: LRGs are rare but luminous, providing good coverage
3. **Clustering amplitude**: LRGs cluster more strongly than the average galaxy (linear bias ~2), making the BAO peak more prominent

The SDSS LRG sample:
- **46,748 galaxies** in the redshift range $0.16 < z < 0.47$
- **Median redshift**: z ~ 0.35
- **Comoving volume sampled**: ~1 h$^{-3}$ Gpc$^3$ (giant!!)
- **Number density**: ~10$^{-4}$ h$^3$ Mpc$^{-3}$ (sparse but uniform)

### Analysis Method: Finding the Peak

The BAO peak is extracted from the measured correlation function by:

1. **Fit the large-scale shape** to a smooth power-law model (accounting for cosmic variance and non-linear effects)
2. **Extract the residual** $\xi_{\text{residual}} = \xi_{\text{measured}} - \xi_{\text{smooth}}$
3. **Measure the peak position** and width in the residual

Eisenstein et al. used multiple fitting techniques and found consistent results:
- **Peak position**: $r_{\text{BAO}} = 101.6 \pm 3.3$ h$^{-1}$ Mpc
- **Expected from CMB**: $r_s = 153.8 \pm 2.0$ Mpc/h
- **Ratio**: $r_{\text{BAO}} / r_s = 0.66 \pm 0.03$

The ratio of 0.66 reflects the expansion of the universe between recombination and z ~ 0.35. This measures the cosmic distance ladder and constrains expansion history.

### Cosmological Constraints

From the BAO measurement, one can constrain dark energy by measuring the **comoving distance** as a function of redshift:

$$d_c(z) = c \int_0^z \frac{dz'}{H(z')}$$

If one measures the BAO scale at two different redshifts, one can measure $H(z)$ and constrain the equation of state of dark energy $w = P / \rho$.

In the 2005 paper, the constraints were modest (large error bars), but the technique's power was immediately clear: future surveys with many more galaxies would tighten constraints dramatically.

---

## Key Results

1. **First detection of BAO peak in galaxy surveys**: A statistically significant peak in the correlation function at 100 h$^{-1}$ Mpc, matching theoretical predictions for acoustic oscillations.

2. **Standard ruler calibration**: The BAO peak, with its scale set by the sound horizon from the CMB, provides an absolute distance measurement independent of the cosmic distance ladder (supernovae, Cepheids, etc.).

3. **Expansion history measurement**: The BAO scale at z ~ 0.35 combined with CMB measurements constrains the comoving distance and expansion rate, directly measuring dark energy effects.

4. **Method validation**: The technique is proven to work in real data, opening a new avenue for dark energy studies complementary to supernovae and CMB.

5. **Luminous red galaxy clustering**: LRGs exhibit strong clustering with no obvious systematics, making them excellent tracers of large-scale structure for cosmology.

6. **Non-linear smearing quantified**: The broadening of the BAO peak in the correlation function provides a direct measurement of small-scale non-linear clustering (non-linear growth, peculiar velocities), quantified as velocity dispersion ~150 km/s.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: MEDIUM**

The BAO peak provides crucial observational constraints for fundamental physics:

- **Sound speed in the early universe**: The BAO scale reflects the sound speed in the early universe plasma. In phonon-exflation, if particles are phonons, the early universe's sound speed would be determined by the phonon dispersion relation from the NCG structure. The observed BAO scale constrains this relation.

- **Primordial density fluctuation spectrum**: The height and shape of the BAO peak encode information about the primordial power spectrum of density fluctuations. In phonon-exflation, these fluctuations emerge from quantum geometry fluctuations of the M4 x SU(3) substrate.

- **Standard ruler as geometric probe**: The BAO scale is a standard ruler because it's set by geometry (the sound horizon in the early universe). Similarly, phonon-exflation predicts that observable large-scale structure serves as a probe of the underlying geometric substrate's properties.

- **Expansion history and effective equation of state**: The BAO measurements constrain how the universe expands with time, directly testing whether dark energy behaves like a cosmological constant (w = -1) or evolves dynamically. Phonon-exflation predicts a specific equation of state from the spectral action.

- **Scale-dependent clustering from phonon spectrum**: The clustering amplitude and BAO peak strength depend on the transfer function, which relates density perturbations at different scales. This shape encodes information about particle physics (whether particles couple to radiation, etc.), which in phonon-exflation emerges from the phonon spectrum.

---

## Key Equations

1. **Sound speed in early universe plasma**:
   $$c_s = \frac{c}{\sqrt{3(1 + 3\rho_b / 4\rho_\gamma)}}$$

2. **Sound horizon**:
   $$r_s = \int_0^{z_{\text{rec}}} \frac{c_s dz'}{H(z')}$$

3. **Two-point correlation function**:
   $$\xi(r) = \left\langle \frac{dN(r)}{4\pi r^2 \bar{n} dr} - 1 \right\rangle$$

4. **Correlation function with BAO peak**:
   $$\xi(r) = \xi_{\text{smooth}}(r) + A_{\text{BAO}} \exp\left( - \frac{(r - r_s)^2}{2\sigma_v^2} \right)$$

5. **Comoving distance**:
   $$d_c(z) = \frac{c}{H_0} \int_0^z \frac{dz'}{E(z')}$$

6. **Hubble parameter** (ΛCDM):
   $$H(z) = H_0 \sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$$

---

## Legacy and Significance

The BAO method has become one of the most important tools in observational cosmology:

- **SDSS-III (BOSS)**: Detected BAO with ~1% precision, constraining dark energy strongly
- **Baryon Oscillation Spectroscopic Survey (BOSS)**: Dedicated survey measuring BAO at multiple redshifts
- **Dark Energy Spectroscopic Instrument (DESI)**: Measuring BAO to unprecedented precision (2024-2025)
- **Future surveys**: Euclid, LSST will push BAO precision further

For the cosmic web, BAO provides a constraint on the "standard sound speed" in the early universe and thus on the overall physical consistency of structure formation models. Any exotic early-universe physics (like the phonon-geometric effects proposed in phonon-exflation) must produce BAO properties consistent with observations.

---

## References

[Search results integrated; full citations available in search output above.]
