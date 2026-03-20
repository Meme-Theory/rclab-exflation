# DESI DR2 Results II: Baryon Acoustic Oscillations and Cosmological Constraints from 14 Million Galaxies

**Author(s):** DESI Collaboration (Adame, Aguilar, Ahlen, et al.)
**Year:** 2025
**Journal:** arXiv:2503.14738

---

## Abstract

The DESI Dark Energy Spectroscopic Instrument releases the second major data reduction (DR2) using three years of observations spanning redshift 0.1 < z < 4.2. With 14 million galaxies, quasars, and Lyman-alpha forest absorbers, BAO measurements across independent redshift bins yield a **3.1σ preference for dynamical dark energy** with w₀ > −1 and w_a < 0 when combined with Planck CMB. Results show 2.3σ tension between BAO-preferred and CMB-preferred cosmological parameters, suggesting either new dark energy physics or systematic effects in large-scale structure.

---

## Historical Context

DESI DR2 (2025) marks the transition from "first-year hints" (DR1, 2.6σ) to "statistically significant dynamical DE signal" (3.1σ). The increase in statistical power (14M vs 6M objects) and longer baseline (3 years of pointing data) reduce systematic uncertainties and sharpen constraints on w(z).

The **3.1σ result is a critical test for phonon-exflation**: the framework predicts w = −1 + O(10⁻²⁹), with zero redshift evolution. A genuine 3.1σ deviation from ΛCDM either (A) falsifies internal-compactification cosmology, or (B) validates the S42 tessellation-lensing hypothesis, or (C) reflects unaccounted systematic bias in galaxy clustering amplitudes.

DR2 also tightens neutrino mass bounds to Σmᵥ < 0.064 eV (ΛCDM) and extends the limit to 0.16 eV in extended w(z) models—comparable to oscillation mass scales.

---

## Key Arguments and Derivations

### Multi-Tracer Expansion and BAO in Extended Cosmologies

DESI DR2 maintains three independent tracers across 9 redshift bins:

1. **LRG (0.4 < z < 1.0)**: 5 bins, 8.5M objects
2. **ELG (0.8 < z < 1.6)**: 3 bins, 3.2M objects
3. **QSO (0.8 < z < 2.4)**: 1 bin, 0.8M objects
4. **Ly-α forest (2.0 < z < 3.5)**: continuous absorption

Each tracer independently measures transverse comoving distance $d_A(z)$ and Hubble rate H(z) via the BAO scale:

$$\alpha_\parallel = \frac{H(z) r_s^\text{fid}}{H^\text{fid}(z) r_s} \quad, \quad \alpha_\perp = \frac{d_A(z)}{d_A^\text{fid}(z)}$$

where superscript "fid" denotes fiducial (Planck 2018 ΛCDM) values. The joint fit across redshifts reconstructs the expansion history without assuming dark energy's equation of state.

### Dynamical Dark Energy in Friedmann Framework

For general w(z), the Hubble parameter satisfies:

$$H^2(z) = H_0^2 \left[ \Omega_m(1+z)^3 + \Omega_k(1+z)^2 + \Omega_\Lambda \rho_\Lambda(z) \right]$$

where the dark energy density scales as:

$$\rho_\Lambda(z) = \rho_{\Lambda,0} \exp\left( 3 \int_0^z \frac{1+w(z')}{1+z'} dz' \right)$$

Using the CPL (Chevallier-Polarski-Linder) parameterization:

$$w(z) = w_0 + w_a \frac{z}{1+z}$$

the expansion history becomes:

$$E(z) = H(z)/H_0 = \left[ \Omega_m(1+z)^3 + (1-\Omega_m-\Omega_k) \exp\left(3(1+w_0+w_a) \ln(1+z) - \frac{3w_a z}{1+z}\right) + \Omega_k(1+z)^2 \right]^{1/2}$$

DR2 fits this using a Gaussian likelihood in the (w₀, w_a) plane, marginalizing over Ωₘ, ΩₖH₀.

### Weak Lensing Magnification Bias and Systematics

Galaxy surveys are susceptible to magnification bias: brighter (more distant) sources are amplified by foreground mass concentrations. The effect scales as:

$$b_\text{mag} = 5(s - 2)$$

where s is the logarithmic slope of the galaxy luminosity function. For DESI tracers, $b_\text{mag} \sim 0.1$ to 0.2, introducing a scale-dependent bias in the clustering amplitude.

The S42 tessellation hypothesis suggests that the 32-cell (dodecahedral) voronoi decomposition of SU(3) at K_7 scale (ξ ~ 10 fm) creates coherent weak-lensing patterns at BAO scales (150 Mpc). If the internal SU(3) geometry has residual spatial correlation extending to large scales through the phonon dispersion, apparent w ≠ −1 could mimic dynamical DE.

### Constraint Surfaces and Tension Quantification

DESI DR2 (BAO alone) constrains:

$$w_0 = −0.78 \pm 0.12 \quad, \quad w_a = −0.58 \pm 0.35 \quad (1\sigma)$$

Combined with Planck CMB (temperature + polarization):

$$w_0 = −0.62 \pm 0.08 \quad , \quad w_a = −0.85 \pm 0.25$$

The **2.3σ tension** arises from the CMB preferring w₀ ~ −1 (via inverse-distance-ladder constraints on Ωₘ) while BAO prefers w₀ > −1. This tension is quantified via the discrepancy parameter:

$$\Delta\chi^2 = \chi^2_\text{BAO} + \chi^2_\text{CMB} - \chi^2_\text{BAO+CMB}$$

For the w₀w_a model, Δχ² ≈ 5.3 (2.3σ in 1D projection).

### Supernova Combination (DES, Pantheon+)

Including Type Ia supernovae (Dark Energy Survey and Pantheon+ compilations) pushes the dynamical DE preference to:

$$w_0 = −0.55 \pm 0.15 \quad , \quad w_a = −1.20 \pm 0.60$$

with 3.9σ tension vs. w = −1. The discrepancy introduces concern about systematic correlation between different probes.

---

## Key Results

1. **14M galaxy BAO**: Transverse and radial distances measured to <2% precision across 9 redshift bins
2. **3.1σ dynamical DE signal**: DESI DR2 + Planck CMB joint fit shows 3.1σ preference for w₀ ≠ −1
3. **Redshift evolution**: w_a < 0 marginally favored, suggesting dark energy becomes stiffer at higher z (opposite to quintessence)
4. **Neutrino mass**: Σmᵥ < 0.064 eV (ΛCDM), < 0.16 eV (w₀w_a), excludes degenerate ν at >2σ
5. **CMB-BAO tension**: 2.3σ discrepancy in parameter space suggests either new physics or unaccounted systematic
6. **Supernova anomaly**: including SNIa data drives w₀ even lower (−0.55) and amplifies w_a drift (−1.20)

---

## Impact and Legacy

DR2 transitions DESI from "hint" to "anomaly." The 3.1σ signal has catalyzed urgent scrutiny of (A) galaxy sample systematics (photometric redshift errors, clustering bias), (B) weak-lensing magnification in sparse samples, (C) BAO template uncertainties, and (D) supernova calibration systematics.

In the phonon-exflation context, DR2 is the **definitive test of w = −1**. If DR2 results persist after independent systematic audits, the framework requires either tessellation-lensing explanation (S42) or fundamental revision of the internal geometry. If future higher-z BAO (from Rubin LSST, Vera Rubin) shows w returning toward −1 at z > 2, this would support a lensing-bias origin (bias amplifies at z ~ 1 clustering peak) rather than true dark energy evolution.

---

## Connection to Phonon-Exflation Framework

**Direct Test**: The framework predicts **w(z) = −1 + O(10⁻²⁹) at all z**, with zero evolution (w_a = 0). All cosmic acceleration derives from the K_7 pairing gap monotonically decreasing with τ (fold parameter), not from dark energy field rolling.

**DESI DR2 Challenge**: The 3.1σ preference for w₀ > −1 and w_a < 0 is the **strongest observational challenge yet**. Three resolution paths:

1. **S42 Tessellation-Lensing Hypothesis** (preferred): The 32-cell dodecahedral structure of SU(3) at K_7 pairing scale creates coherent weak-lensing magnification bias at BAO wavelengths. The apparent w ≠ −1 is an observational artifact, not true dark energy evolution. Prediction: higher-z BAO (z > 2) should show w returning to −1 as clustering bias weakens.

2. **Internal Geometry Modification**: The monotonic spectral action assumes no residual K_7 spatial structure. If K_7 retains harmonic oscillation modes (phonons in the internal direction), the effective dark energy density could vary slowly with epoch, mimicking dynamical w(z). This would require extending the spectral action to include internal phonon contributions—currently unformulated.

3. **Framework Falsification**: w ≠ −1 falsifies phonon-exflation if independent systematics audits (photometric redshift, BAO template, weak-lensing calibration) find no explanation. S42 is the last circuit-breaker hypothesis.

**Critical next step**: DESI DR3 (2026) with 16M objects and improved photo-z will sharply constrain the lensing-bias component. If DR3 confirms 3.1σ, the framework enters crisis stage requiring either S42 or fundamental redesign.

