# Planck 2015 Results. XIII. Cosmological Parameters

**Author(s):** Planck Collaboration (130+ authors)
**Year:** 2018 (revision of 2015 results)
**Journal/ArXiv:** A&A (Astronomy & Astrophysics)

---

## Abstract

The Planck satellite mission has measured the cosmic microwave background (CMB) temperature and polarization anisotropies with unprecedented precision. This paper presents the final Planck 2015 results on cosmological parameters derived from temperature and polarization power spectra, combined with Planck lensing, CMB lensing from other experiments, and external datasets (baryon acoustic oscillations, Type Ia supernovae, H_0 measurements).

The Planck 2015 legacy dataset provides the most precise measurements of the Standard Lambda-CDM (LCDM) parameters: baryon density Omega_b, dark matter density Omega_c, Hubble constant H_0, optical depth tau, and spectral index of scalar perturbations n_s. The paper also constrains extensions to LCDM including scalar-tensor theories, non-standard neutrino physics, and early dark energy.

---

## Historical Context

The Planck satellite (2009-2013) provided the third generation of full-sky CMB measurements, after COBE (1989) and WMAP (2001-2012). Planck's 30-70 GHz frequency coverage and sensitivity allowed detection of acoustic peaks and damping tails in the temperature power spectrum with exquisite precision.

The CMB angular power spectrum encodes information about the early universe: the sound horizon at recombination, the matter and energy density, curvature, reionization history, and inflation parameters. Combined with large-scale structure (BAO), Type Ia SNe distance measurements, and local H_0 determinations, Planck data constrains the full LCDM parameter set.

---

## Key Results

### Primary Parameters (68% CL)

| Parameter | Value |
|-----------|-------|
| Omega_b h^2 | 0.02226 ± 0.00023 |
| Omega_c h^2 | 0.1186 ± 0.0031 |
| H_0 [km/s/Mpc] | 67.74 ± 0.46 |
| tau (reionization) | 0.078 ± 0.019 |
| n_s (spectral index) | 0.9655 ± 0.0062 |
| sigma_8 (matter fluctuations) | 0.829 ± 0.012 |

**Interpretation**:
- **Baryon density**: Omega_b ~ 5% of critical density
- **Dark matter density**: Omega_c ~ 27% of critical density
- **Dark energy (Omega_Lambda)**: ~68% (inferred from geometry; Omega_b + Omega_c + Omega_Lambda ~ 1 in a flat universe)
- **Age of universe**: 13.799 ± 0.021 Gyr
- **Reionization optical depth**: tau = 0.078 indicates reionization began around z ~ 8.8

### Inflationary Constraints

From temperature and polarization power spectra:
- **Spectral index**: n_s = 0.9655 ± 0.0062 (red, slightly blue preferred over scale-invariant Harrison-Zeldovich n_s = 1)
- **Running of spectral index**: dns/dln(k) = -0.0084 +/- 0.0031 (statistically insignificant)
- **Tensor-to-scalar ratio**: r < 0.11 (95% CL) — excludes simple phi^4 and alpha*phi^2 potentials

**Inflationary models ruled out**:
- phi^4 inflation (power-law potential)
- Natural inflation
- Chaotic inflation with alpha*phi^{2/3}

**Favored models**:
- Starobinsky R^2 inflation
- Axion monodromy
- Effective field theory inflation with small epsilon (slow-roll parameter)

### Neutrino Physics Constraints

Sum of neutrino masses:
$$\sum m_\nu < 0.17 \text{ eV (95% CL)}$$

This is the tightest cosmological constraint on neutrino mass, excluding certain mass hierarchies and SUSY scenarios.

**Effective number of neutrino species**:
$$N_{\text{eff}} = 3.15 \pm 0.23 \text{ (TT+lowP)}$$

Consistent with three standard neutrinos. Values > 3.3 would indicate extra relativistic degrees of freedom.

### Tension on H_0

A persistent discrepancy exists between:
- **Planck + low-z data**: H_0 = 67.74 ± 0.46 km/s/Mpc
- **Local measurements** (Cepheids + SNe): H_0 = 73.52 ± 1.62 km/s/Mpc

This ~3 sigma tension suggests either:
1. Systematic uncertainties in one or both measurements
2. Early dark energy (modified cosmology at z > 1000)
3. New physics in late-time cosmology

### Lensing-Induced Power Suppression

Planck detects the effects of gravitational lensing of CMB photons by large-scale structure:
- Lensing modifies power spectrum at multipole l > 100
- Amplitude of lensing constrains matter power spectrum
- Consistency with large-scale structure surveys confirms structure growth predictions

### Constraints on Dark Energy

Assuming LCDM (flat universe with cosmological constant):
- **Omega_Lambda**: 0.6817 ± 0.0095
- **Equation of state (fixed w = -1)**: consistent with observations
- **No evidence for dynamical dark energy**: extending to w(z) does not improve fit

---

## Technical Highlights

### Likelihoods Used

1. **TT**: Temperature power spectrum (ell < 30 and ell > 30 separately)
2. **TE, EE**: Polarization cross-correlation and auto-correlation
3. **lowP**: Low-ell (ell < 30) low-noise polarization priors
4. **lensing**: Planck CMB lensing power spectrum
5. **Foreground modeling**: Dust, synchrotron, free-free emission across 30-857 GHz

### Systematic Uncertainties

Sources of systematic error addressed:
- Beam asymmetry and leakage
- Calibration accuracy (< 0.1% for temperature)
- Polarization efficiency mismatch
- Foreground contamination

Planck achieves cosmic variance-limited measurements at ell ~ 100-1000, with systematics subdominant.

---

## Key Results Summary

1. **Precise LCDM parameters**: Six-parameter LCDM determined to percent-level precision
2. **Flat universe confirmed**: Omega_K = 0.040 +/- 0.038 (consistent with zero curvature)
3. **Early-universe physics probed**: Primordial non-Gaussianity f_NL < 5.8 (local type)
4. **Dark energy is smooth**: No evidence for clustering beyond the cosmological constant
5. **Neutrino mass bounded**: sum(m_nu) < 0.17 eV rules out degenerate hierarchy
6. **Inflation predictions mostly confirmed**: Spectral index and tensor bounds match slow-roll predictions
7. **Tension persists**: H_0 discrepancy suggests possible new physics or systematics

---

## Connection to Phonon-Exflation Framework

Planck 2015 data provides observational benchmarks for testing phonon-exflation:

1. **Inflation from internal compactification**: Phonon-exflation proposes inflation driven by SU(3) fiber dynamics, not a scalar field. This predicts spectral index n_s and tensor-to-scalar ratio r that may differ from single-field slow-roll. Planck's precise n_s = 0.9655 measurement constrains this alternative scenario.

2. **Effective equation of state**: If SU(3) fiber expansion drives inflation, the effective equation of state w may deviate from -1 in subtle ways. Planck's dark energy constraints (w = -1 to high precision) must be compatible with phonon-exflation predictions.

3. **Neutrino mass hierarchy**: The framework determines neutrino masses from SU(3) spectral geometry, not from Yukawa couplings. Planck's sum(m_nu) < 0.17 eV constraint tests whether the spectrum can be accommodated.

4. **Primordial non-Gaussianity**: Standard inflation predicts f_NL ~ 0.01 (very small). If phonon-exflation produces different non-Gaussianity, Planck's tight limit f_NL < 5.8 constrains this.

5. **Dark matter and dark energy**: Phonon-exflation attributes both to emergent quasiparticles in the M4 x SU(3) substrate. Planck's measurements of Omega_DM and Omega_DE (inferred from geometry) are key observational tests.

6. **H_0 tension resolution**: The observed tension between Planck and local measurements might indicate early dark energy. In phonon-exflation, if the framework predicts dynamical dark energy or early epoch with modified equation of state, this could address the H_0 tension.

---

## Impact and Legacy

Planck 2015 results provide the gold standard for LCDM parameter constraints. The precision achieved has been transformative:
- Verified predictions of inflation
- Constrained BSM physics (neutrino masses, dark energy, curvature)
- Set benchmarks for future CMB experiments (CMB-S4, Simons Observatory)
- Highlighted tensions needing resolution (H_0, S_8)

The data will remain essential for testing any alternative cosmology, including phonon-exflation.
