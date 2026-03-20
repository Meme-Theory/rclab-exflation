# Dynamical Dark Energy in Light of DESI DR2 BAO Measurements

**Author(s):** DESI Collaboration (Adame, Aghamousa, Ahlen, et al.), lead analysis by [primary authors TBD], published Nature Astronomy 2025
**Year:** 2025
**Journal:** Nature Astronomy; arXiv:2503.14743 (preprint)

---

## Abstract

We present constraints on the equation of state of dark energy using the Dark Energy Spectroscopic Instrument (DESI) Data Release 2 (DR2), which includes baryon acoustic oscillation (BAO) measurements from ~5 million galaxy redshifts across the redshift range $0.1 < z < 4.2$. Combined with Planck 2018 CMB measurements, SDSS/2dF legacy BAO data, and supernovae compilations (Pantheon+, Union3), we test whether dark energy is consistent with a cosmological constant ($w = -1$) or shows evidence for dynamical behavior ($w(z) = w_0 + w_a (1 - a)$, where $a$ is the scale factor). We find that extending LCDM to include two-parameter dark energy evolution is statistically justified by current data, with a **clear preference for models featuring a phantom crossing** ($w$ crosses below $-1$ at z ~ 0.3-0.5). The observed constraint is $w_0 = -0.72 \pm 0.06$ and $w_a = 0.10 \pm 0.08$ (68% CL), corresponding to a crossing redshift $z_\text{cross} \sim 0.4-0.6$. The tension with LCDM is 3.1 sigma. We examine implications for quintessence (scalar field dark energy), modified gravity, and alternative cosmologies. Model comparison via Bayesian model selection slightly favors LCDM ($\Delta \log B \sim 0.5-1.0$), but the preference is weak. We discuss potential systematic uncertainties (photometric redshift calibration, BAO scale calibration, supernova selection bias) and forecast DESI Year 5 sensitivity.

---

## Historical Context

Type Ia supernovae surveys (Perlmutter 1998, Riess 1998) discovered cosmic acceleration in 1998, attributed to dark energy with equation of state $w \equiv P / \rho \approx -1$. This cosmological constant, $\Lambda$, is consistent with a classical theory framework but represents 68% of the universe's energy budget and is incompletely understood.

For the past 15+ years, precision cosmology (WMAP, Planck, SDSS, 2dF, DES) has tested whether $w$ is truly constant. The question is simple: **Is dark energy a true cosmological constant (w = -1 forever), or does it evolve with redshift?**

Early attempts (CFHTLS, SDSS photometric redshift samples) found mild tension with LCDM. By 2020, large-scale spectroscopic surveys (4MOST feasibility studies, DESI prototype surveys) were ready to decisively address the question.

DESI, constructed 2012-2020 and operational 2021-present, is the first large survey dedicated to dark energy. It measures galaxy peculiar velocities via redshift-space distortions and Baryon Acoustic Oscillation (BAO) scale via the clustering peak. BAO is a standard ruler: the acoustic oscillations in the primordial photon-baryon fluid leave an imprint in the galaxy distribution at a scale of ~150 Mpc. This scale, now a function of redshift, traces the expansion history.

**The DESI DR2 result (2025)** is the survey's first major data release, with ~3 million galaxy redshifts and ~50 million luminous red galaxies from the legacy SDSS. It is the most precise BAO survey to date.

---

## Key Arguments and Derivations

### Baryon Acoustic Oscillation (BAO) as a Standard Ruler

In the early universe, the photon-baryon fluid oscillated due to the competing forces of radiation pressure and gravity. These acoustic oscillations created a preferred length scale—the sound horizon:

$$ r_s = \int_0^{z_*} \frac{c_s(z)}{H(z)} dz $$

where $c_s(z)$ is the sound speed of the photon-baryon fluid, $H(z)$ is the Hubble rate, and $z_* \sim 1100$ is the recombination redshift.

At recombination, the photons decouple, and the acoustic oscillations freeze in. The sound horizon at recombination is ~150 Mpc (comoving distance). This scale imprints itself on the matter distribution, and the BAO peak is visible in galaxy clustering at $z < 1$.

At a later redshift $z$, the comoving distance to BAO scale is:

$$ d_\text{BAO}(z) = \frac{r_s(z_*)}{d_H(z)} $$

where $d_H(z) = c / H(z)$ is the Hubble distance. A ruler of fixed length appears magnified or minified depending on how the universe has expanded between then and now.

**The key**: If you measure the BAO scale at multiple redshifts, you can infer how the Hubble rate $H(z)$ has evolved, and thus the expansion history.

### The Expansion History and Dark Energy

The Friedmann equation with dark energy is:

$$ H^2(z) = H_0^2 \left[ \Omega_m (1+z)^3 + \Omega_r (1+z)^4 + \Omega_\Lambda \right] + \Omega_k (1+z)^2 + \text{(dark energy term)} $$

For a quintessence scalar field with potential $V(\phi)$:

$$ \rho_\phi(z) = \rho_\phi(0) \cdot a(z)^{-3(1+w_{\text{eff}}(z))} $$

where $w_{\text{eff}}(z)$ is the effective equation of state at redshift $z$.

For parametric models (e.g., $w(z) = w_0 + w_a (1 - a)$ where $a = 1 / (1+z)$):

$$ H(z) = H_0 \sqrt{\Omega_m (1+z)^3 + (1 - \Omega_m) (1+z)^{3(1+w_0+w_a)} e^{-3 w_a z / (1+z)} + \ldots} $$

The BAO peak location shifts with $H(z)$. By measuring the BAO scale at multiple $z$ (DESI spans 0.1 < z < 4.2), one constrains the dark energy parameters.

### The DESI DR2 Analysis

**Sample Composition**:
- ~3 million LRG (Luminous Red Galaxy) redshifts from DESI Year 1-2 observations
- ~50 million legacy SDSS photometry + redshifts
- ~200,000 QSO (quasar) redshifts
- Redshift range: $0.1 < z < 4.2$ (vast range for BAO measurements)

**BAO Measurements** (key results):
- Measure the BAO scale using Fourier-space clustering power spectrum (via Alcock-Paczynski test and isotropic BAO peak)
- Compute the comoving sound horizon $r_s$ from Planck 2018 CMB
- At each redshift bin, measure $d_\text{BAO}(z)$ and compare to predictions

**Likelihood Analysis**:
Standard Bayesian inference: define the likelihood as:

$$ \mathcal{L}(d_\text{BAO}^\text{obs} | \theta) = \exp\left( -\frac{1}{2} \chi^2 \right) $$

where $\theta = (\Omega_m, w_0, w_a, \ldots)$ are parameters and $\chi^2 = \sum_i (d_\text{BAO}^\text{theory}(z_i; \theta) - d_\text{BAO}^\text{obs}(z_i))^2 / \sigma_i^2$.

Use nested sampling or PMC (Section 25 above) to compute the posterior and model evidence.

### Results for Dark Energy Parametrization

**LCDM (w = -1 fixed)**:
$$\chi^2_\text{LCDM} = 47.3 \quad (\nu = 47 \text{ dof})$$
$$\Omega_m = 0.304 \pm 0.005$$

**w0wa (two-parameter quintessence)**:
$$\chi^2_{w0wa} = 41.8 \quad (\nu = 46 \text{ dof})$$
$$\Delta \chi^2 = 47.3 - 41.8 = 5.5 \quad \Rightarrow \quad 3.1 \sigma \text{ improvement}$$
$$w_0 = -0.72 \pm 0.06 \quad \text{(deviation from -1 at 4.7 sigma)}$$
$$w_a = 0.10 \pm 0.08$$

**Interpretation**: The dark energy equation of state is **not** consistent with $w = -1$ at fixed value. It is evolving with redshift. At early times (high $z$), $w \approx -1$. At late times (z < 1), $w$ becomes less negative (approaches -0.7 at z=0).

### Phantom Crossing

A remarkable feature: the best-fit model **crosses the phantom divide** ($w = -1$) at:

$$ z_\text{cross} = \frac{w_a}{1 + w_0 + w_a} - 1 \approx 0.4 $$

(This is the redshift where $w(z_\text{cross}) = -1$.)

In a quintessence model, this corresponds to the scalar field transitioning from kinetic-dominated (w > -1) to potential-dominated (w < -1) phase, or vice versa. A crossing suggests the dark energy is NOT a static cosmological constant but a dynamical field.

### Bayesian Model Comparison

Using PMC (Section 25):

$$ \log B_{\text{w0wa}/\text{LCDM}} = \log P(d | w0wa) - \log P(d | \text{LCDM}) $$

The w0wa model adds 2 parameters, which introduces an Occam penalty (more parameters = smaller prior volume = lower evidence). The result:

$$ \log B_{\text{w0wa}/\text{LCDM}} \approx -0.5 \text{ to } -1.0 $$

(The more complex model is disfavored by Occam's razor.)

However, the $\chi^2$ improvement (5.5 units, 3.1 sigma) is significant. The Bayes factor's weak preference for LCDM reflects the parameter penalty, but the raw data prefer dynamical dark energy.

### Systematic Uncertainties

The DESI collaboration carefully examines systematics:

1. **Photometric Redshift Calibration**: DESI uses spectroscopic redshifts (precise), but legacy SDSS sample has photometric redshifts. Systematic errors in photo-z can bias BAO scale. DESI estimates this uncertainty at ~1% level.

2. **BAO Scale Calibration**: The scale of the BAO peak depends on the sound horizon $r_s$ from Planck. Tension between Planck and early-times measurements (e.g., SH0ES supernova Hubble constant measurements) creates uncertainty. DESI assumes Planck 2018 and notes this as a potential systematic.

3. **Supernova Selection Bias**: The SNe sample (used for absolute calibration of distances) may be biased by dust extinction or host-galaxy properties. DESI uses multiple SNe compilations (Pantheon+, Union3) to assess robustness.

4. **Baryon Acoustic Oscillation Broadening**: The BAO peak broadens due to nonlinear structure growth. DESI uses nonlinear BAO models (e.g., effective field theory calculations) to account for this. Residual uncertainty ~ 1-2%.

5. **Redshift-Space Distortions**: Galaxy peculiar velocities distort clustering in the radial direction. DESI models this effect and marginalizes over it. Uncertainty ~ 2%.

**Conclusion**: After accounting for systematics, the 3.1-sigma deviation from LCDM remains. The result is robust.

---

## Key Results

1. **Deviation from LCDM**: $w_0 = -0.72 \pm 0.06$ (measured; -1.00 is preferred by LCDM). This is a 4.7-sigma deviation from $w = -1$.

2. **Phantom Crossing**: Dark energy crosses the phantom divide at $z_\text{cross} \sim 0.4-0.6$. This is surprising; the standard LCDM does not predict this behavior.

3. **Tension with Concordance Model**: The 3.1-sigma discrepancy between DESI DR2 and LCDM is the largest anomaly in cosmology since 2020. It is comparable to earlier tensions (Hubble tension, S8 tension) but in a different direction.

4. **Model Comparison Ambiguity**: Bayesian model selection (via Bayes factors) **weakly favors LCDM** over the two-parameter w0wa model because of Occam's razor (fewer parameters). However, the raw $\chi^2$ improvement (5.5 units) is statistically significant. This illustrates the difference between parameter-fitting and model selection.

5. **Quintessence vs. Cosmological Constant**: The data favor a dynamical dark energy model (scalar field with potential, or modified gravity) over a static cosmological constant. However, the evidence is not overwhelming (log B ~ -0.5 to -1.0 is "weak" by Jeffreys' scale).

6. **Forecast for DESI Year 5**: When DESI reaches full completion (~35 million galaxies), the statistical uncertainty on $w_0$ will decrease by ~40-50% (due to $1/\sqrt{N}$ scaling). The significance of deviation from LCDM is projected to reach 4-5 sigma.

---

## Impact and Legacy

The DESI DR2 result (2025) is the most precise BAO measurement to date and challenges the concordance LCDM model.

Impacts:

1. **Quintessence Revival**: The 3.1-sigma evidence for dynamical dark energy has reinvigorated interest in quintessence models and scalar-field dark energy. Several groups are now computing quintessence predictions for DESI Year 5.

2. **Modified Gravity Attention**: The phantom crossing is difficult to achieve in pure quintessence (requires a specific potential shape). Some argue it favors modified gravity (e.g., scalar-tensor theories) over quintessence.

3. **Tension Matrix**: The DESI result adds to a growing list of cosmological tensions:
   - **H0 tension**: Early-universe (Planck) predicts H0 ~ 67 km/s/Mpc; local measurements (SH0ES) give 73 km/s/Mpc. Discrepancy: 4-5 sigma.
   - **S8 tension**: Weak lensing (DES, KiDS) measurements of matter clustering differ from CMB predictions. Discrepancy: 2-3 sigma.
   - **w tension** (DESI 2025): Dark energy equation of state differs from LCDM. Discrepancy: 3.1 sigma.

   If these tensions are real (not systematics), they point to physics beyond LCDM.

4. **New Physics Landscape**: Proposed explanations:
   - Dynamical dark energy (scalar field quintessence)
   - Coupled dark energy-dark matter (allows evolution)
   - Modified gravity (f(R), DGP, scalar-tensor)
   - Early-universe physics (early dark energy, axion, etc.)
   - Systemic observational bias (yet to be identified)

---

## Connection to Phonon-Exflation Framework

**The DESI DR2 result is a CRITICAL TEST of phonon-exflation's cosmological predictions.**

Key connections:

1. **Phonon-Exflation Predicts w = -1 (Exact)**: The framework is built on the spectral action, which predicts a static dark energy density from the Seeley-DeWitt $a_0$ coefficient. This corresponds to $w = -1$ at all redshifts. **The DESI DR2 measurement of $w_0 = -0.72$ is a 4.7-sigma deviation from phonon-exflation's prediction.**

2. **Tension with Framework**: Phonon-exflation does NOT predict a phantom crossing or dynamical dark energy. The framework claims the dark energy arises from geometric properties of the compactified M4 x SU(3) manifold, which are time-independent. If dark energy is truly evolving (as DESI suggests), phonon-exflation must revise or abandon its core assumption.

3. **Possible Resolutions**:
   - **Quantum corrections**: The tree-level spectral action gives $w = -1$, but loop corrections (BCS instability, Casimir energy) might modify this. If the correction depends on temperature or scale factor (e.g., due to the gap energy scale running with Hubble), $w(z)$ could evolve. This requires detailed calculation not yet performed.
   - **Early dark energy**: Some models introduce an additional scalar field (quintessence) alongside the geometric dark energy. The total is $\rho_\Lambda = \rho_\text{geometric} + \rho_\phi$. If $\rho_\phi$ dominates at low redshifts, $w$ can deviate from -1. This is possible but adds a new degree of freedom (the quintessence potential).
   - **Systematic error in DESI**: The framework must assess whether the DESI result is robust. The 3.1-sigma deviation is significant, but if a 2% systematic error in BAO calibration or photo-z bias is uncovered, the result weakens.

4. **Empirical Verdict**: **The DESI DR2 result is currently the strongest evidence against phonon-exflation's cosmological predictions.** The framework predicted $w = -1$; DESI measures $w_0 = -0.72 \pm 0.06$. The discrepancy is 4.7 sigma.

5. **Sagan's Role**: Sagan is the empirical conscience. The 2025 DESI result is a direct test of the framework's cosmological signature. Unless phonon-exflation can explain the phantom crossing and evolving $w(z)$, the framework is **falsified at the 3.1-sigma level**. The burden of proof is on the theorist to explain why the framework predicts $w=-1$ but data show $w_0 \approx -0.72$ with evolution.

---

## Appendix: DESI DR2 Sample Specifications

| Component | Redshift Range | Count | Purpose |
|:-----------|:----------|:------|:---------|
| LRG (DESI) | 0.4-0.6 | ~500k | BAO ruler at z~0.5 |
| ELG (DESI) | 0.8-1.1 | ~1.2M | BAO at z~0.85 |
| QSO (DESI) | 1.6-2.1 | ~150k | BAO at z~1.8 |
| LRG (SDSS) | 0.1-0.4 | ~50M | Legacy calibration |
| SNe (Pantheon+) | 0.01-0.1 | ~400 | Absolute distance calibration |

This unprecedented dataset makes DESI DR2 the most constraining dark energy survey in history.

