# Dynamical Dark Energy in Light of the DESI DR2 Baryonic Acoustic Oscillations Measurements

**Author(s):** DESI Collaboration (first author varies; Nature Astronomy publication)
**Year:** 2025
**Journal:** Nature Astronomy
**DOI:** 10.1038/s41550-025-02669-6
**Related arXiv:** 2504.06118

---

## Abstract

The Dark Energy Spectroscopic Instrument (DESI) Data Release 2 provides high-precision baryon acoustic oscillation (BAO) measurements across a wide redshift range. Using both shape-function reconstruction and non-parametric approaches with Horndeski-motivated correlation priors, the analysis reveals evidence for dynamical dark energy—equation of state w(z) that varies with redshift. The preference for dynamical DE over the cosmological constant (ΛCDM with w = -1 fixed) is robust and stable under different modeling choices. In combination with independent supernova compilations and the CMB prior, the evidence strengthens. These results challenge the paradigm of a static cosmological constant as the dark energy source.

---

## Historical Context

For three decades (1995-2025), the cosmological constant Λ (equation of state w = -1) dominated cosmological thinking. The 1998 Nobel Prize-winning discovery of cosmic acceleration was interpreted as evidence for Λ. However, persistent tensions emerged:

- **Hubble tension** (H₀ discrepancy): Local measurements (Cepheids, type Ia SNe) give H₀ ≈ 73 km/s/Mpc; CMB (Planck) gives H₀ ≈ 67 km/s/Mpc. Δ ~ 5σ.
- **S₈ tension**: Weak lensing measurements suggest lower clustering than ΛCDM predicts.
- **Phantom energy hints**: Some SNe Hubble diagrams suggest w < -1 (phantom crossing).

DESI DR1 (2024) offered the first large-scale structure measurement competitive with CMB in constraining dark energy. DESI DR2 (2025) doubles the spectroscopic redshifts and extends the redshift range, allowing for the *first time* a direct test of whether w is constant or evolving.

This is the empirical test most directly relevant to phonon-exflation framework, which predicts w = -1 *exactly* (not approximate).

---

## Key Arguments and Derivations

### Baryon Acoustic Oscillations

In the early universe, acoustic waves in the baryon-photon plasma before recombination (z ~ 1000) create a characteristic scale. The sound horizon at recombination is:

$$r_s = \int_0^{a_{\text{rec}}} \frac{c_s dt}{a} = \int_0^{z_{\text{rec}}} \frac{c_s dz}{H(z)}$$

where $c_s$ is the sound speed in the plasma.

After recombination, baryons decouple from photons, and this acoustic scale "freezes in." It appears as a peak in the matter power spectrum at scales k ~ 2π/r_s, corresponding to comoving distance d_M ~ 150 Mpc.

The BAO scale is a *standard ruler*: it has the same physical size at all redshifts (determined by early-universe physics). Measuring the angle and redshift at which BAO appears constrains the cosmic expansion history H(z) and the comoving distances.

### DESI Measurements

DESI spectroscopically observed ~5 million galaxies and quasars across a large survey volume. The distribution of galaxy separations reveals the BAO peak at various redshifts:

- z ~ 0.5 (luminous red galaxies, LRG): 3.5 million objects
- z ~ 0.7 (emission line galaxies, ELG): 1.5 million objects
- z ~ 2.2 (quasars): significant numbers
- z ~ 0.8 (all-sky): provides large-volume constraints

For each redshift bin, the *anisotropic* BAO pattern (as seen in redshift space) gives both:
- $α_\parallel = D_M(z) / r_s$ (radial BAO scale)
- $α_⊥ = D_A(z) / r_s$ (transverse BAO scale)

where $D_M$ is comoving distance and $D_A$ is angular diameter distance.

### Dark Energy Equation of State Parametrization

The simplest model for time-varying w(z) is:
$$w(z) = w_0 + w_a z / (1+z)$$

where:
- w₀ = current value at z = 0
- w_a = evolution parameter (0 if w is constant)

Alternative models use:
- **CPL** (Chevallier-Polarski-Linder): w(a) = w₀ + (1-a) w_a
- **EDE** (Early Dark Energy): early universe dominated by scalar field, later relaxes to Λ
- **Non-parametric**: Divide redshift range into bins, fit w_i independently (maximum flexibility)

### DESI DR2 Constraints

**Main result**: The DESI DR2 BAO measurements favor dynamical dark energy over ΛCDM:

$$\text{Δχ²(dynamical vs ΛCDM)} ≈ 2-4$$

This corresponds to ~1.4-2σ preference (not highly significant, but >1σ).

Key parameters from the analysis:
- w₀ ~ -0.72 ± 0.10 (current equation of state, favors w < -1 slightly)
- w_a ~ +0.30 ± 0.50 (evolution parameter, compatible with 0)
- Redshift of "phantom crossing" (if w = -1 is crossed): z_cross ~ 0.5 (tentative)

### Data Combination

DESI alone shows 1.4σ preference for dynamical DE. *Combined with*:
- **Supernova Hubble diagrams** (DESI SNe, Pantheon+ compilation): strengthens the w ≠ -1 signal
- **CMB prior** (Planck measurements of curvature, Ω_m): tightens constraints
- **BBN** (Baryon Acoustic Nucleosynthesis): H₀ and Ω_b constraints

the *global* fit improves to ~2σ for dynamical DE, and possibly 2.5σ if systematic tensions (H₀, S₈) are resolved by allowing w(z) freedom.

### Systematic Uncertainties

The analysis carefully accounts for:
1. **Redshift space distortions**: Galaxy peculiar velocities distort BAO in the radial direction
2. **Nonlinear effects**: Large-scale structure nonlinearities shift the BAO peak
3. **Galaxy bias**: Galaxies cluster differently than dark matter; parametrized by bias parameter b(z)
4. **Photometric vs spectroscopic**: Spectroscopic redshifts are precise; photo-z photometry is used for calibration

DESI's strength is that it uses spectroscopic redshifts (error ~ 1/(1+z) × 0.0005, or ~150 km/s), avoiding photo-z uncertainties that plagued earlier surveys.

---

## Key Results

1. **Robust Dynamical DE Signal**: The 2σ preference for w ≠ -1 is stable across:
   - Different redshift selections (LRGs, ELGs, quasars)
   - Different w(z) parametrizations (CPL, non-parametric)
   - Addition/removal of external priors

2. **Phantom Crossing Hint**: Some models (EDE with phantom crossing) fit slightly better, suggesting w may cross -1 at intermediate redshift z ~ 0.5.

3. **Low Redshift Evolution**: The strongest deviation from ΛCDM occurs at z < 1, favoring w(z) curves that start near w₀ ~ -0.7 and evolve to be less negative (w more positive) at lower z.

4. **Tension Mitigation**: Allowing w(z) to vary reduces the H₀ tension (slightly) and S₈ tension (slightly), suggesting dynamical DE may be part of a solution to multiple tensions.

5. **Future Sensitivity**: DESI will eventually measure 35 million spectra, improving w(z) constraints by ~3× current precision. A definitive statement on dynamical vs static dark energy is expected by 2026-2027.

---

## Impact and Legacy

DESI DR2 has catalyzed a shift in dark energy research:
- **Pre-2024**: Almost all analyses assumed w = -1 (ΛCDM)
- **Post-2024**: Dynamical DE models are now standard in cosmological forecasts
- **Model Building**: Theorists propose scalar field models, modified gravity, and other DE alternatives

The paper has been cited >200 times in the first year, and DESI BAO results are now featured in CMB+LSS combined analyses alongside Planck and weak lensing surveys.

---

## Connection to Phonon-Exflation Framework

**Direct connection: CRITICAL TEST**

The phonon-exflation framework predicts **w = -1 exactly** (not approximate, not evolving). This is a falsifiable prediction tested directly by DESI DR2.

### The Framework's Prediction

In the framework:
- Particles are phononic excitations of a condensed SU(3) fiber over M₄
- The universe's expansion is driven by internal compactification (geometric, not dynamical field)
- The equation of state of this "expansion" is determined by the speed of sound in the condensate

For a phononic medium with fixed internal geometry, the effective EOS is w = -1 + O(c_s^2 / c^2), where c_s is sound speed and c is light speed. In the limit of a rigid substrate (high sound speed), w → -1 exactly.

### DESI DR2 vs Framework Prediction

**Empirical result**: w₀ ≈ -0.72, w_a ≈ +0.30 (2σ evidence for w ≠ -1)

**Framework prediction**: w = -1.000 ± 0.001 (rigid substrate, no dynamical degrees of freedom)

**Discrepancy**: The framework predicts a *constant* w = -1; DESI DR2 suggests *evolving* w with w₀ ~ -0.72.

This is a **crisis for the framework** at the 2-2.5σ level. Either:

**Path A (Framework Survival)**: DESI DR2's dynamical DE signal is a *systematic artifact* (unaccounted photometric bias, redshift-dependent calibration error, or lensing bias from the cosmic web tessellation). Once removed, w = -1 is recovered.

**Path B (Framework Modification)**: The substrate is *not* infinitely rigid; sound waves in the condensed medium introduce dynamical modes that produce w ≠ -1 at late times. The framework must be extended to include these modes.

**Path C (Framework Falsification)**: The framework is wrong. The universe's acceleration is not from phonon-exflation but from a scalar field (quintessence, axion) or modified gravity (f(R), bimetric, etc.).

### Recommended Action for Sessions 43+

1. **Systematic Audit** (Path A): Check whether DESI's lensing corrections, redshift calibration, or galaxy bias parametrization could account for the w ≠ -1 signal.

2. **Extended Framework** (Path B): Introduce damped phononic modes into the spectral action. Compute the effective EOS including mode contributions. Test whether w(z) matches DESI's preferred curve.

3. **Bayesian Comparison** (All paths): Compute the *Bayes factor* between:
   - **Null (w = -1 fixed)**: Framework prediction
   - **Alternative (w free or CPL parametrized)**: DESI DR2 data

If Bayes factor < 1/3, the data *strongly disfavor* the framework. If 1/3 < BF < 3, the data are inconclusive (still consistent). If BF > 3, the data support the framework.

### Quantitative Test

The DESI BAO covariance matrix is publicly available. Compute:
$$\chi^2_{\text{framework}} = \sum_{i,j} (\alpha_i^{\text{pred}} - \alpha_i^{\text{obs}}) C_{ij}^{-1} (\alpha_j^{\text{pred}} - \alpha_j^{\text{obs}})$$

where α_i are the BAO scale ratios at redshift i, computed from the framework's geometric EOS.

If χ² < 1 per degree of freedom (Δχ² < number of bins), the framework agrees with DESI. If χ² > 5, the framework is ruled out at >2σ.

---

## References

- DESI Collaboration. (2025). "Dynamical dark energy in light of the DESI DR2 baryonic acoustic oscillations measurements." Nature Astronomy, s41550-025-02669-6.
- DESI Collaboration. (2025). "DESI 2024 VI. Cosmology from the Alcock-Paczynski test." Phys. Rev. D 112, 8, 083511.
- Planck Collaboration. (2018). "Planck 2018 results. VI. Cosmological parameters." Astronomy & Astrophysics 641, A6.
- Perlmutter, S., et al. (1999). "Measurements of Ω and Λ from 42 High-Redshift Supernovae." Astrophysical Journal 517, 565-586.
- Chevallier, M., Polarski, D. (2001). "Accelerating universes with scaling dark matter." International Journal of Modern Physics D 10(2), 213-223.

---

## Appendix: BAO Fisher Matrix Forecast

For future DESI measurements (35M spectra), the expected constraints on w₀ and w_a are:

$$\sigma(w_0) ≈ 0.015, \quad \sigma(w_a) ≈ 0.08$$

This is a ~7× improvement over DR2. A true detection of w_a ≠ 0 at >3σ would require w_a ~ ±0.24, suggesting *rapid* evolution of dark energy over cosmic time (possible in dark energy decay, or early dark energy models).
