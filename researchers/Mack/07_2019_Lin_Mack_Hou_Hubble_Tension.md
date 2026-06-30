# Investigating the Hubble Constant Tension: Two Numbers in the Standard Cosmological Model

**Author(s):** Weikang Lin, Katherine J. Mack, Liqiang Hou
**Year:** 2019
**Journal/ArXiv:** arXiv:1910.02978, The Astrophysical Journal Letters (2020)

---

## Abstract

The Hubble constant H_0, measuring the current rate of cosmic expansion, has become increasingly contentious in observational cosmology. Early-universe measurements from the cosmic microwave background (Planck satellite) predict H_0 ~67 km/s/Mpc, while local measurements using type Ia supernovae and Cepheid variables yield H_0 ~73 km/s/Mpc, a discrepancy of ~4-5 sigma. This tension motivates investigation into whether systematic errors in specific measurement methods, undiscovered new physics, or unaccounted-for degeneracies might explain the discrepancy. Lin, Mack, and Hou investigate the Hubble tension by analyzing constraints in the two-dimensional parameter space of H_0 and Omega_m (present-day matter density), rather than treating H_0 in isolation. They find that while various observational constraints (CMB, galaxy clusters, BAO, weak lensing, gravitational lensing, supernovae) consistently overlap in the H_0-Omega_m plane with some exceptions, local supernova measurements and strong gravitational lensing constraints show the most significant deviations. The analysis suggests that it is not straightforward for non-standard cosmological models to reconcile all constraints simultaneously without accounting for systematic uncertainties in specific measurement techniques.

---

## Historical Context

The cosmic expansion rate, quantified by the Hubble constant H_0, is a cornerstone of modern cosmology. Its accurate measurement is essential for determining the age of the universe, the scale of cosmic structure, and the expansion history needed to infer dark energy properties. For decades, H_0 measurements converged toward a value around 70 km/s/Mpc from multiple independent methods.

However, precision improvements in both early-universe measurements (from the Planck satellite's observations of the cosmic microwave background) and late-universe measurements (from nearby supernovae and Cepheid variables) have revealed a significant tension. The early-universe infers H_0 = 67.4 ± 0.5 km/s/Mpc (under the assumption of a flat ΛCDM model), while local measurements consistently yield values around 72-73 km/s/Mpc. This ~4-5 sigma discrepancy has profound implications: either (1) there are unrecognized systematic errors in one class of measurements; (2) the late-universe expansion history differs from ΛCDM predictions (modified gravity, dynamical dark energy); or (3) undiscovered new physics couples the early and late universe in unexpected ways.

Understanding the Hubble tension is critical for cosmology. Rather than treating H_0 as a single isolated measurement, Lin et al. recognize that in ΛCDM (and similar models), the expansion history is determined by two key parameters: H_0 and Omega_m (the present-day matter density). Different observational probes constrain different combinations of these parameters, and their covariances and degeneracies become visible in the two-dimensional H_0-Omega_m plane.

---

## Key Arguments and Derivations

### Cosmic Expansion and ΛCDM

The expansion history of the universe in ΛCDM is governed by the Friedmann equation:

$$H(z)^2 = H_0^2 \left[ \Omega_m (1+z)^3 + \Omega_\Lambda \right]$$

where $H(z)$ is the Hubble constant at redshift $z$, $H_0$ is today's Hubble constant, $\Omega_m$ is the matter density parameter (dark plus baryonic matter), and $\Omega_\Lambda = 1 - \Omega_m$ is the dark energy density parameter (assuming spatial flatness).

Distance measures in cosmology (luminosity distance, comoving distance) depend on the integral of the inverse of the Hubble parameter:

$$d_L(z) = (1+z) \int_0^z \frac{dz'}{H(z')} = (1+z) \int_0^z \frac{dz'}{H_0 \sqrt{\Omega_m(1+z')^3 + \Omega_\Lambda}}$$

Different observational probes measure different combinations of $H_0$ and $\Omega_m$ through their dependence on distances, growth of structure, and other cosmological observables.

### Observational Constraints in H_0-Omega_m Space

**CMB (Planck)**: Observations of the cosmic microwave background power spectrum constrain the sound horizon at recombination:

$$r_s = \int_0^{z_{rec}} \frac{c_s(z')}{H(z')} dz'$$

The first peak in the CMB power spectrum is inversely proportional to $r_s$. Measurements of the acoustic peak positions tightly constrain the ratio $H_0 \times r_s / c$, creating a strong degeneracy between $H_0$ and other parameters including $\Omega_m$ and the baryon density $\Omega_b$.

**Baryon Acoustic Oscillations (BAO)**: Measured from galaxy surveys at multiple redshifts, BAO provide standard ruler measurements of the comoving distance:

$$d_A(z) = \int_0^z \frac{c dz'}{H(z')}$$

BAO measurements constrain combinations of $\Omega_m$, $H_0$, and dark energy properties.

**Type Ia Supernovae**: Standardizable candles measuring luminosity distance:

$$m = M + 5 \log_{10}(d_L) + 25$$

where the absolute magnitude $M$ depends on supernova properties (light curve shape, color) and uncertain host-galaxy extinction. Different local supernova samples (SDSS-SN, Pantheon, others) employ different standardization procedures and extinction corrections, creating potential systematic discrepancies.

**Weak Gravitational Lensing**: The growth of matter density fluctuations depends on both $\Omega_m$ and the expansion history. Weak lensing of distant galaxies by large-scale structure constrains the matter power spectrum and thus $\Omega_m$ and its evolution.

**Strong Gravitational Lensing**: Time delays in multiple images of gravitationally lensed supernovae or quasars depend on the expansion history. Strong lens time delays provide direct measurements of the combination $H_0 \times d_A$, constraining $H_0$ if the lens geometry and mass distribution are known.

**Galaxy Cluster Abundances**: The number density of massive galaxy clusters as a function of redshift is sensitive to $\Omega_m$ and its growth rate, providing independent constraints.

### Parameter Degeneracies

Different probes have different sensitivities and degeneracies:

- **CMB is tight in $H_0 \times r_s$** but degenerate with other parameters (e.g., optical depth to reionization, neutrino masses)
- **SN Ia is sensitive to $d_L(z)$** and thus to $H_0$ and $\Omega_m$, but suffers from extinction and potential evolution systematics
- **BAO provides standard ruler** and breaks some degeneracies but has limited redshift coverage
- **Lensing probes growth** and breaks $\Omega_m - \Omega_\Lambda$ degeneracies but introduces other systematics

In the H_0-Omega_m plane, most constraints form elongated ellipses or bands reflecting their intrinsic parameter correlations. Where these constraints should overlap (if all data are consistent) becomes visually apparent.

---

## Key Results

1. **Consistent overlap region**: When constraints from CMB, BAO, weak lensing, and other probes are plotted in the H_0-Omega_m plane, they consistently overlap in a region around H_0 ~ 67-68 km/s/Mpc and Omega_m ~ 0.31-0.32. This overlap validates the internal consistency of these measurements under ΛCDM.

2. **Local supernova divergence**: Type Ia supernovae from local samples (z < 0.1) consistently measure higher H_0 values (~73 km/s/Mpc) compared to the overlap region. The discrepancy is evident as a systematic offset, not a statistical scatter. Different local SN Ia samples (SDSS-SN, Pantheon, CfA) show correlated offsets, suggesting a common systematic issue rather than individual measurement errors.

3. **Strong gravitational lensing deviation**: Time-delay cosmography from strongly lensed systems (STRIDES, H0LiCOW collaborations) also measures H_0 values higher than the early-universe consensus, though with larger uncertainties. The tension is at ~2-3 sigma in recent samples.

4. **Omega_m consistency**: While H_0 shows tension, Omega_m measurements from different probes are generally consistent, clustering around Omega_m ~ 0.3 regardless of whether probes prefer high or low H_0. This suggests the tension is not a simple rescaling of all parameters but specific to H_0.

5. **Implications for new physics**: Simple extensions to ΛCDM (e.g., adding a dynamical dark energy component w ≠ -1) cannot easily reconcile all constraints simultaneously. The tension persists even when allowing more flexible dark energy models, suggesting either: (1) systematics in specific measurements; (2) more radical new physics; or (3) an assembly of multiple small issues combining to create the apparent discrepancy.

6. **Possible systematic sources**:
   - **SN Ia extinction**: Mass-dependent extinction corrections (as explored in complementary studies by Holwerda et al. on same issue) might systematically bias supernova distances
   - **Local universe flows**: Bulk flows and peculiar velocities in the local universe could bias local expansion rate measurements if not properly corrected
   - **Gravitational lensing systematics**: Mass models for strongly lensed systems depend on assumptions about density profiles that could introduce bias
   - **Calibration systematics**: Cepheid variable distance ladder calibration uncertainties propagate to supernova distances

---

## Impact and Legacy

This paper has become central to discussions of the Hubble tension. By shifting focus from a one-dimensional H_0 measurement to a two-dimensional analysis including Omega_m, Lin et al. revealed that the tension is specifically with H_0, not a wholesale inconsistency in the matter content of the universe. This diagnostic insight has guided subsequent investigations and has motivated:

1. Detailed studies of systematic uncertainties in each measurement method
2. Development of new, independent H_0 measurement techniques
3. Theoretical proposals for new physics (early dark energy, modified gravity) that might reconcile the tension
4. Critical evaluation of distance ladder calibration and extension

The recognition that the H_0 tension is a real, persistent feature of current data (not statistical fluctuation) has made it one of the highest-priority problems in observational cosmology.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation framework, the expansion history differs fundamentally from ΛCDM. The framework predicts that dark energy emerges from the spectral action of the internal geometry (M4 x SU(3) compactification), with a specific equation of state w=-1 (exactly) rather than a dynamical dark energy parameter.

The Friedmann equation would be modified in the framework by the geometric contributions:

$$H(z)^2 = H_0^2 \left[ \Omega_m(z) + \Omega_\Lambda^{geom}(z) \right]$$

where $\Omega_\Lambda^{geom}$ depends on the geometric state of the fold (how much the compactified space has unfolded).

Key implications for the Hubble tension:

1. **Early dark energy**: If the geometric dark energy was not always w=-1 but became w=-1 only at late times (after z~10), early-universe observations (CMB) would infer a different dark energy content than late-universe observations. This could naturally explain why CMB measures lower H_0 than late-universe probes.

2. **Modified growth rate**: The geometric dark matter (different density profile from CDM) and dark energy would affect the growth of structure differently, changing how weak lensing and other late-universe probes constrain Omega_m.

3. **Distance measurements**: If the luminosity distance evolution differs from ΛCDM due to the modified expansion history, local supernova distances would scale differently with redshift, potentially explaining the systematic offset.

4. **Parameter space**: The framework predicts specific relationships between H_0, Omega_m, and the geometric state, which could be tested against the observed constraints in the H_0-Omega_m plane.

Lin et al.'s two-dimensional analysis provides a powerful diagnostic that could distinguish phonon-exflation from ΛCDM: if the framework is correct, the overlap region and measured values of H_0 and Omega_m would differ from current ΛCDM expectations, and the geometric model would simultaneously resolve multiple tensions in precision cosmology (H_0, S_8, etc.) through a unified mechanism.
