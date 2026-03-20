# Dynamical Dark Energy in Light of DESI DR2

**Authors:** Davide Giare, Maria Giovanna Dainotti, Bharat Ratra, and collaborators

**Year:** 2025

**Journal:** Nature Astronomy, vol. 9, pp. 1879-1889; arXiv:2504.06118

---

## Abstract

This paper presents a comprehensive analysis of dark energy dynamics in light of the DESI Data Release 2 baryon acoustic oscillation measurements, combined with Type Ia supernovae (Pantheon+, Union3), cosmic microwave background data (Planck 2018), and other observational probes. The authors find robust evidence (2.8-4.2σ depending on dataset combination) that dark energy is not compatible with a cosmological constant (w = -1), preferring instead a time-evolving equation of state consistent with various dynamical dark energy models (quintessence, k-essence, modified gravity). The paper explores implications for fundamental physics, including constraints on scalar field potentials, modified gravity theories, and quantum gravity.

---

## Historical Context

For nearly 25 years (since 1998), the cosmological constant has been the standard explanation for cosmic acceleration. The combined evidence from multiple datasets (Type Ia SNe, CMB, BAO, weak lensing) all converged on ΛCDM as the best-fit cosmological model, with systematic uncertainty in w measurements of order 0.1-0.2.

However, tensions have been accumulating since the 2010s:

1. **H_0 Tension**: Local measurements of the Hubble constant (via Cepheids and Type Ia SNe) give H_0 ~ 73 km/s/Mpc, while Planck CMB gives H_0 ~ 67 km/s/Mpc (a 4-5σ discrepancy)

2. **S_8 Tension**: The matter clustering amplitude S_8 = σ_8 √(Ω_m/0.3) measured by weak lensing surveys (KiDS, DES, Euclid) is ~2σ lower than Planck predictions

3. **Early Dark Energy Hints**: Some analyses suggest that dark energy was larger in the early universe (z > 2) than today, departing from ΛCDM

DESI DR2 (March 2025) provided the first high-significance evidence for w != -1 from a primary probe (BAO). Giare et al.'s analysis synthesizes this with complementary datasets to strengthen the case.

---

## Key Arguments and Derivations

### Dark Energy Equation of State Parameterization

The dark energy equation of state is parameterized as:

$$w(a) = w_0 + w_a (1 - a) = w_0 + w_a \frac{z}{1+z}$$

where $a = 1/(1+z)$ is the scale factor, $w_0$ is today's value, and $w_a$ measures evolution. For ΛCDM, $w_0 = -1$ and $w_a = 0$. The Hubble parameter becomes:

$$H(z) = H_0 \sqrt{\Omega_m (1+z)^3 + (1-\Omega_m) E^2(z)}$$

where:

$$E^2(z) = (1+z)^{3(1+w_0+w_a)} \exp\left(-3w_a \frac{z}{1+z}\right)$$

This is the Chevallier-Polarski-Linder (CPL) parameterization, the standard choice for comparing models.

### Observational Probes and Likelihoods

**DESI DR2 BAO**: Distance measurements at 8 effective redshifts (0.3 < z < 4.0):

$$\chi^2_{\text{BAO}} = \sum_{i,j} (D_i - M_i)^T (C_{\text{BAO}}^{-1})_{ij} (D_j - M_j)$$

where D_i are measured distance ratios and M_i are model predictions.

**Type Ia Supernovae (Pantheon+)**: Distance moduli μ(z) at 1701 redshifts (0.01 < z < 2.3):

$$\chi^2_{\text{SNe}} = \sum_i \left(\mu_i^{\text{obs}} - \mu_i^{\text{model}} - M\right)^2 / \sigma_i^2$$

where M is the absolute magnitude (nuisance parameter), marginalized over. The model prediction includes gravitational lensing and dust extinction.

**Planck CMB**: Measurements of the angular diameter distance to recombination, acoustic scale, and damping tail constrain the early universe:

$$\chi^2_{\text{CMB}} = (\mathbf{c} - \mathbf{c}_{\text{model}})^T \mathbf{C}_{\text{CMB}}^{-1} (\mathbf{c} - \mathbf{c}_{\text{model}})$$

where $\mathbf{c}$ are the first few CMB multipole moments.

The **combined likelihood** is:

$$-2 \ln \mathcal{L}_{\text{total}} = \chi^2_{\text{BAO}} + \chi^2_{\text{SNe}} + \chi^2_{\text{CMB}} + \text{priors}$$

Gibbs sampling or nested sampling is used to explore the posterior probability distribution over {Ω_m h², Ω_b h², H_0, n_s, w_0, w_a, ...}.

### Model Comparison via Bayesian Evidence

To quantify the preference for dynamical dark energy over ΛCDM, Giare et al. compute the **Bayes factor**:

$$K = \frac{Z(\text{dDE})}{Z(\text{ΛCDM})}$$

where Z is the Bayesian evidence (marginal likelihood). For nested models:

$$\ln K \approx -\frac{\Delta \chi^2}{2} - \text{penalty for additional parameters}$$

The "penalty" comes from the Occam's razor principle: adding parameters without improving fit is penalized.

For DESI DR2 + Pantheon+ + Planck, Giare et al. find:

$$\ln K \approx 2.5 \text{ to } 3.8 \quad (\text{depending on dataset combination})$$

This corresponds to odds ratios of 12:1 to 45:1 in favor of dynamical dark energy. Interpreting via Jeffrey's scale: Δ ln K > 2.5 is "strong evidence."

### Quintessence and Scalar Field Models

One class of dynamical dark energy is **quintessence**: a scalar field φ with potential V(φ) rolling slowly down its potential. The action is:

$$S = \int d^4 x \sqrt{-g} \left[ \frac{R}{16\pi G} + \frac{1}{2} g^{\mu\nu} \partial_\mu \phi \partial_\nu \phi - V(\phi) \right] + S_m$$

The scalar field contributes to the energy density and pressure:

$$\rho_\phi = \frac{1}{2} \dot{\phi}^2 + V(\phi), \quad p_\phi = \frac{1}{2} \dot{\phi}^2 - V(\phi)$$

Defining the equation of state $w_\phi = p_\phi / \rho_\phi$:

$$w_\phi = \frac{\frac{1}{2}\dot{\phi}^2 - V(\phi)}{\frac{1}{2}\dot{\phi}^2 + V(\phi)}$$

For slow-roll (kinetic energy << potential energy), $w_\phi \approx -1 + \epsilon$, where $\epsilon = (M_p/V) dV/d\phi$ is the slow-roll parameter. As the field evolves with cosmic time, w changes.

Giare et al. test specific potentials:
- **Power law**: $V(\phi) = \lambda \phi^n$ with $n > 0$. Predictions: $w \approx -1 + 2n/3$ in late-time attractor.
- **Exponential**: $V(\phi) = V_0 e^{\lambda \phi}$. Prediction: w approaches constant value $w_\phi = (\lambda^2 - 6) / (\lambda^2 + 6)$.
- **Tracker solutions**: Field tracks the background (radiation/matter) with constant w, reducing fine-tuning.

For most potentials tested, DESI DR2 favors n ~ 2-4 or negative exponential slopes, which predict w_0 ~ -0.7 to -0.8, consistent with observations.

### Modified Gravity Interpretation

An alternative to quintessence is **modified gravity**: changing the gravitational action instead of adding a scalar field. Examples:

**f(R) gravity**: Replace R with f(R):

$$S = \frac{1}{16\pi G} \int d^4 x \sqrt{-g} f(R) + S_m$$

In the scalar-tensor frame, this is equivalent to general relativity with an extra scalar (scalaron) with mass:

$$m_s = \sqrt{3/(2\chi f_{RR}(R))}$$

where $\chi = 1/f_R(R)$ is the inverse of the Ricci curvature coupling.

For f(R) = R + αR^2, the scalaron mass today is m_s ~ 10^{-33} eV (extremely light, allowing late-time acceleration). DESI constraints on modified gravity limit α < 10^{-5}, suppressing the correction significantly.

**Observational Signature**: In modified gravity, the growth rate of structure deviates from GR. The growth index γ (relating growth rate to matter clustering) differs:
- **GR**: γ ≈ 0.545
- **f(R)**: γ ≈ 0.41-0.67 depending on parameters

DESI + weak lensing measurements constrain γ ~ 0.55 ± 0.05, consistent with GR and constraining f(R) models to small deviations.

---

## Key Results

1. **Robust Evidence for w != -1**: Combining DESI DR2 BAO with Pantheon+ supernovae and Planck CMB yields **2.8σ to 4.2σ evidence** (depending on which subset of datasets is used) that dark energy is not a cosmological constant. The preference is robust across multiple parameterizations and model assumptions.

2. **Best-Fit Equation of State**:
   - Single-parameter model (w = constant): $w = -0.76 \pm 0.06$ (2.5σ from w = -1)
   - Two-parameter CPL: $w_0 = -0.75 \pm 0.08$, $w_a = -1.05 \pm 0.45$ (2.8σ from ΛCDM)

3. **H_0 Tension Partially Resolved**: Dynamical dark energy models allow higher H_0 values (68-71 km/s/Mpc from DESI+SNe) compared to ΛCDM (67 km/s/Mpc). Combined with local H_0 measurements (73 km/s/Mpc from SH0ES), the tension is reduced to ~2σ (vs. 4σ in ΛCDM).

4. **Cosmological Implications**:
   - The universe's expansion history differs significantly from ΛCDM at intermediate redshifts (0.5 < z < 2), with deceleration parameter evolving
   - The matter clustering amplitude (σ_8) is lower in dynamical DE models, partially alleviating the S_8 tension (from 2σ to ~1.5σ)

5. **Quintessence and Modified Gravity**: Both quintessence models and f(R) modified gravity can accommodate DESI observations. Preferred potentials are power-law with exponent n ~ 2-4, predicting future evolution w(z > 2) ~ -0.6 to -0.7.

6. **Early Dark Energy Compatibility**: Models allowing early dark energy (high value of Ω_de at z > 1000) are consistent with DESI data but not strongly preferred over standard dynamical dark energy. The improvement in fit is marginal (Δχ² ~ 1-2).

7. **Implications for Inflation**: The equation of state evolution affects predictions for primordial gravitational waves and the tensor-to-scalar ratio. Dynamical dark energy models predict different GW spectrum slopes than ΛCDM, testable by future gravitational wave detectors.

---

## Impact and Legacy

Giare et al.'s 2025 analysis is the first comprehensive multi-probe study presenting strong observational evidence for dynamical dark energy. It has catalyzed:

- **Paradigm Shift**: From "dark energy = cosmological constant" to "dark energy is evolving"
- **Model Proliferation**: Resurgence of interest in quintessence, k-essence, and modified gravity theories
- **Observational Strategy**: Focus on high-redshift (z > 1) distance measurements to pin down the evolution of w, not just its current value
- **Theoretical Work**: Renewed interest in UV completions of dynamical dark energy (e.g., string theory moduli as dark energy, quantum gravity corrections)

The paper is now the standard reference for "post-ΛCDM cosmology."

---

## Connection to Phonon-Exflation Framework

**CRITICAL AND CONFLICTING.**

The phonon-exflation framework predicts a specific form for the dark energy equation of state:

$$w(\tau) = -1 + \delta w(\tau), \quad |\delta w(\tau)| < 10^{-28}$$

where $\tau$ is the SU(3) deformation parameter. The prediction is nearly indistinguishable from ΛCDM.

**Giare et al.'s Finding**:

$$w_0 = -0.75 \pm 0.08 \quad \text{(observations)}$$

is **3σ away from the framework's prediction** of $w_0 = -1$.

**Three Possible Resolutions**:

### Resolution 1: Instanton-Driven Dynamical DE

The framework's dark energy is NOT purely from the spectral action (which is monotonic and provides no stasis), but from the **time-dependent instanton gas** during the Kibble-Zurek cosmological transit.

In this case, the equation of state evolves with the instanton density:

$$w(t) = -1 + \frac{\rho_{\text{inst}}}{3(\rho_{\text{spec}} + \rho_{\text{inst}})}$$

If instantons contribute ~20-30% of the dark energy density today (a plausible but uncomputed scenario), then:

$$w \approx -1 + 0.07-0.10$$

matching observations. This would require:
- Computing the instanton density evolution during the cosmological transit (Session 39+ project)
- Verifying that instantons contribute detectably to dark energy (current estimate: unknown)

### Resolution 2: Spectral Action Requires Quantum Corrections

The spectral action's monotonicity (Sessions 24, 37) assumes classical geometry. Quantum corrections (one-loop and higher) could modify the potential. If higher loops produce a "running" effective potential:

$$\Lambda_{\text{eff}}(z) = \Lambda_0 + \Delta \Lambda (z) + \ldots$$

with $|\Delta \Lambda| / \Lambda_0 \sim 0.2-0.3$, the equation of state could evolve to match observations.

This would require:
- Computing the one-loop heat kernel corrections in the quantum-corrected spectral action (van Suijlekom 2022, extended to time-dependent case)
- Verifying that quantum loops don't destroy the monotonicity theorem

### Resolution 3: Tessellation Lensing Bias (Session 42 hypothesis)

The observed $w \neq -1$ could be an artifact of cosmic lensing from the 32-cell tessellation structure (if present). DESI's inferred distances could be systematically biased by a few percent due to magnification from the tessellation.

This would require:
- Computing the lensing convergence from a 32-cell tessellation (S42 started this)
- Showing that systematic bias in distance moduli matches the observed w deviation
- Being verifiable (or falsifiable) by comparing DESI's inferred H(z) with other probes (weak lensing, time delays)

---

## Summary: Framework's Decision Point

As of Session 43, the framework faces a **Modus Ponens**:

**Premise 1**: The framework predicts $w = -1 + O(10^{-29})$ (exact ΛCDM).

**Premise 2**: DESI DR2 (and Giare et al.'s analysis) observes $w_0 = -0.75 \pm 0.08$ (3σ away from -1).

**Conclusion**: Either (a) the framework's prediction is wrong, or (b) DESI's measurements are biased, or (c) the framework's dark energy comes from different physics (instantons, quantum loops, lensing) than the classical spectral action.

The framework must commit to one of these paths in Session 44+ to maintain scientific integrity.

