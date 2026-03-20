# Uncertainty Quantification for Nuclear Density Functional Theory and Information Content of New Measurements

**Author(s):** J.D. McDonnell, N. Schunck, D. Higdon, J. Sarich, S.M. Wild, W. Nazarewicz

**Year:** 2015

**Journal:** Physical Review Letters, Vol. 114, p. 122501

---

## Abstract

Statistical tools of uncertainty quantification (UQ) are applied to assess the information content of measured observables with respect to present-day theoretical models. Using Bayesian inference and a Gaussian process emulator, the framework examines how new mass measurements from the Canadian Penning Trap constrain the parameters of the Skyrme energy density functional. The analysis demonstrates that while individual new measurements are vital for understanding nuclear structure, they do not always impose strong constraints on the effective interaction parameters. The methodology establishes a rigorous path toward quantifying theoretical errors in nuclear density functional theory and improving predictive capability for nuclei far from stability.

---

## Historical Context

Nuclear density functional theory has become the workhorse of nuclear structure calculations, yet it faces a fundamental challenge: despite decades of refinement, dozens of parametrizations exist, each with comparable predictive power on known nuclei but divergent predictions far from stability. The absence of quantified theoretical uncertainties hampered progress toward understanding which observable was most diagnostic of the underlying interaction.

In the 2010s, the nuclear physics community increasingly recognized that standard goodness-of-fit measures ($\chi^2$ values) provided inadequate guidance. A parametrization could fit existing data well yet produce wildly different predictions for exotic isotope half-lives or nuclear masses far from stability. The solution was to borrow statistical methodology from other fields: Bayesian inference combined with Gaussian process emulators to efficiently propagate parameter uncertainties through expensive nuclear structure calculations.

---

## Key Arguments and Derivations

### Bayesian Framework for Nuclear Model Parameters

Let $\boldsymbol{\theta}$ denote the parameters of the energy density functional (e.g., the 12 Skyrme force coefficients plus pairing parameters). The prior distribution $p(\boldsymbol{\theta})$ encodes our initial beliefs about plausible parameter ranges. New experimental data $\mathcal{D} = \{d_1, d_2, \ldots, d_n\}$ (e.g., nuclear masses from Penning trap measurements) updates our beliefs via Bayes' theorem:

$$p(\boldsymbol{\theta} | \mathcal{D}) = \frac{p(\mathcal{D} | \boldsymbol{\theta}) p(\boldsymbol{\theta})}{p(\mathcal{D})}$$

The likelihood $p(\mathcal{D} | \boldsymbol{\theta})$ quantifies how well a given set of parameters reproduces the data. For mass measurements with experimental uncertainty $\sigma_i$, the likelihood for a single observable $M_i$ is:

$$p(M_i^{\text{exp}} | \boldsymbol{\theta}) = \frac{1}{\sqrt{2\pi(\sigma_i^2 + \sigma_{\text{th}}^2)}} \exp\left( -\frac{(M_i^{\text{calc}}(\boldsymbol{\theta}) - M_i^{\text{exp}})^2}{2(\sigma_i^2 + \sigma_{\text{th}}^2)} \right)$$

where $\sigma_{\text{th}}$ is the theoretical uncertainty (model error), which is typically unknown but must be estimated from the overall fit quality.

The posterior distribution $p(\boldsymbol{\theta} | \mathcal{D})$ represents our updated knowledge after incorporating experiment. Predictions for new systems are obtained by marginalizing over the posterior:

$$p(y | \mathcal{D}) = \int d\boldsymbol{\theta} \, p(y | \boldsymbol{\theta}) p(\boldsymbol{\theta} | \mathcal{D})$$

### Gaussian Process Emulator

Direct evaluation of the posterior by sampling $p(\mathcal{D} | \boldsymbol{\theta})$ requires computing nuclear masses for thousands of parameter sets—computationally prohibitive with HFB codes that require hours per isotope. The solution is a Gaussian process (GP) emulator: a fast surrogate that learns the mapping from parameters to observables.

The GP assumes that the function $M(\boldsymbol{\theta})$ is a Gaussian process with mean and covariance:

$$M(\boldsymbol{\theta}) \sim \mathcal{GP}(m(\boldsymbol{\theta}), C(\boldsymbol{\theta}, \boldsymbol{\theta}'))$$

Given a training set of $N$ expensive function evaluations $\{(\boldsymbol{\theta}_i, M_i)\}_{i=1}^N$, the GP provides predictions $\mu(\boldsymbol{\theta}^*)$ and uncertainties $\sigma(\boldsymbol{\theta}^*)$ for new parameter vectors $\boldsymbol{\theta}^*$ without additional function evaluations. The posterior mean is:

$$\mu(\boldsymbol{\theta}^*) = \mathbf{k}^T (\mathbf{K} + \epsilon^2 I)^{-1} \mathbf{m}$$

where $\mathbf{K}$ is the training covariance matrix, $\mathbf{k}$ is the covariance between the test point and training set, and $\epsilon$ is a noise variance accounting for numerical errors. The predicted uncertainty:

$$\sigma^2(\boldsymbol{\theta}^*) = k(\boldsymbol{\theta}^*, \boldsymbol{\theta}^*) - \mathbf{k}^T (\mathbf{K} + \epsilon^2 I)^{-1} \mathbf{k}$$

quantifies the emulator's confidence—it is largest far from training points.

### Likelihood Function with Measurement Error

The likelihood for mass data is:

$$p(\mathcal{D} | \boldsymbol{\theta}) = \prod_{i \in \text{measured}} \exp\left( -\frac{(M_i^{\text{th}}(\boldsymbol{\theta}) - M_i^{\text{exp}})^2}{2 \sigma_i^2} \right) \prod_{j \in \text{unmeasured}} \exp\left( -\frac{(M_j^{\text{th}}(\boldsymbol{\theta}))^2}{2 \sigma_j^2} \right)$$

The first product includes experimental measurements and their uncertainties $\sigma_i \approx 10$ keV for modern Penning traps. The second product reflects the constraint that unmeasured masses should not be too far from systematic trends (a weak prior based on global fits). The theoretical uncertainty $\sigma_{\text{th}}$ is estimated from residuals:

$$\sigma_{\text{th}} = \sqrt{\frac{1}{N_{\text{fit}}} \sum_{i \in \text{fit}} (M_i^{\text{calc}} - M_i^{\text{exp}})^2}$$

### Information Content and Bayes Factor

To assess whether a new measurement significantly constrains the model, the information content is quantified via the Kullback-Leibler divergence:

$$D_{\text{KL}} = \int d\boldsymbol{\theta} \, p(\boldsymbol{\theta} | \mathcal{D}_{\text{new}}) \log \left( \frac{p(\boldsymbol{\theta} | \mathcal{D}_{\text{new}})}{p(\boldsymbol{\theta} | \mathcal{D}_{\text{old}})} \right)$$

High KL divergence indicates that the posterior has shifted significantly—the measurement is highly informative. Conversely, low KL divergence means the posterior barely changed—the measurement provides little new information.

The Bayes factor compares two models $M_1$ (with a new measurement included) and $M_0$ (without it):

$$BF = \frac{p(\mathcal{D}_{\text{new}} | M_1)}{p(\mathcal{D}_{\text{new}} | M_0)} = \frac{\int d\boldsymbol{\theta} \, p(\mathcal{D}_{\text{new}} | \boldsymbol{\theta}) p(\boldsymbol{\theta} | M_1)}{\int d\boldsymbol{\theta} \, p(\mathcal{D}_{\text{new}} | \boldsymbol{\theta}) p(\boldsymbol{\theta} | M_0)}$$

If $BF > 3$, the new data provides moderate evidence for Model 1; if $BF > 10$, strong evidence.

---

## Key Results

1. **Canadian Penning Trap Data Not Constraining**: The newly measured masses from the CPT (precision $\pm 10$ keV) do not significantly shift the posterior distribution of Skyrme force parameters compared to earlier mass compilations. The Bayes factor is $\sim 1.2$ (weak evidence), indicating the new data agrees with existing systematic trends but does not pinpoint new physics.

2. **Sensitivity Analysis**: Different observables constrain different parameter combinations. Charge radii are most sensitive to the symmetry energy; binding energies to the bulk incompressibility; pairing gaps to the effective mass.

3. **Dripline Predictions Remain Uncertain**: Despite improved mass constraints from CPT, predictions for the two-neutron dripline location remain uncertain by $\pm 2$ nucleons in heavy regions (Z < 50), demonstrating that current experimental data do not sufficiently constrain models for extreme isotopes.

4. **Theoretical Error Estimates**: The root-mean-square deviation between theory and experiment is $\sigma_{\text{th}} \approx 0.5$ MeV for a typical Skyrme functional, indicating that nuclear density functional theory has intrinsic limitations—improvements require physics beyond the functional form.

5. **Model Comparison**: Different Skyrme parametrizations yield posterior distributions with overlapping support, implying that no single data set unambiguously selects one EDF over others. Only when multiple observables are considered jointly does the posterior sharpen.

6. **Fission Barriers**: Predictions of spontaneous fission barriers remain uncertain by $\pm 1$ MeV even after incorporating all available mass and charge radius data—this uncertainty propagates to predictions of superheavy half-lives.

---

## Key Equations

| Concept | Formula |
|:--------|:--------|
| Bayes' theorem | $p(\boldsymbol{\theta} \| \mathcal{D}) = \frac{p(\mathcal{D} \| \boldsymbol{\theta}) p(\boldsymbol{\theta})}{p(\mathcal{D})}$ |
| Likelihood (mass measurement) | $p(M^{\text{exp}} \| \boldsymbol{\theta}) = \exp\left( -\frac{(M^{\text{th}} - M^{\text{exp}})^2}{2(\sigma_{\text{exp}}^2 + \sigma_{\text{th}}^2)} \right)$ |
| GP posterior mean | $\mu(\boldsymbol{\theta}^*) = \mathbf{k}^T (\mathbf{K} + \epsilon^2 I)^{-1} \mathbf{M}$ |
| GP posterior variance | $\sigma^2(\boldsymbol{\theta}^*) = k(\boldsymbol{\theta}^* \| \boldsymbol{\theta}^*) - \mathbf{k}^T (\mathbf{K} + \epsilon^2 I)^{-1} \mathbf{k}$ |
| Kullback-Leibler divergence | $D_{\text{KL}}(p_1 \| p_0) = \int p_1(\boldsymbol{\theta}) \log(p_1(\boldsymbol{\theta})/p_0(\boldsymbol{\theta})) d\boldsymbol{\theta}$ |

---

## Connection to Phonon-Exflation Framework

The uncertainty quantification approach exemplifies how modern nuclear physics integrates experimental data with computational predictions while honestly assessing limitations. The phonon-exflation framework must similarly address the question: what observations would definitively distinguish the framework from conventional models?

Key implications:

1. **Observable Signatures**: Just as McDonnell et al. identify which observables (radii, gaps, dripline location) most tightly constrain Skyrme parameters, the framework must identify its own "smoking gun" observables—perhaps certain ratios of neutron/proton pairing gaps, or anomalies in beta decay rates far from stability.

2. **Theoretical Uncertainty Floor**: The McDonnell analysis reveals that even with perfect data, nuclear density functional theory has a ~0.5 MeV error floor. If the phonon-exflation framework reduces this (by correctly accounting for phonon-mediated interactions), it would constitute positive evidence.

3. **Bayesian Model Comparison**: The framework's predictions for exotic nuclei could be compared to conventional models using Bayes factors. If future experiments of dripline nuclei or superheavy elements favor the phonon-exflation predictions, that would provide quantitative support.

4. **Parameter Space Exploration**: In the framework, the "parameters" would be the geometric properties of the SU(3) manifold (curvature, torsion, spinor connection). A Bayesian analysis could determine which aspects of the internal geometry are most tightly constrained by observed nuclear spectra.

---

## References

- Kennedy, M.C., O'Hagan, A. (2001). Bayesian calibration of computer models. J. Roy. Stat. Soc. 63, 425-464.
- Rasmussen, C.E., Williams, C.K.I. (2006). Gaussian Processes for Machine Learning. MIT Press.
- Dobaczewski, J., Nazarewicz, W., Reinhard, P.G. (2014). Error estimates of theoretical nuclear mass predictions. J. Phys. G 41, 074001.

