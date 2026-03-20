# Bayesian Model Comparison in Cosmology with Population Monte Carlo

**Author(s):** Martin Kilbinger, Ludovic Van Waerbeke, Marian Douspis, Henk Hoekstra, James Heymans, Konrad Kuijken, et al.
**Year:** 2010
**Journal:** MNRAS, Vol. 405, pp. 492-502; arXiv:0912.1614

---

## Abstract

We present the Population Monte Carlo (PMC) method for Bayesian model comparison in cosmology, with applications to testing cosmological model extensions beyond the flat-Lambda CDM baseline. Using recent CMB (WMAP 5), Type Ia supernovae (Union), and BAO (SDSS LRG) data, we evaluate competing hypotheses: (1) flat LambdaCDM vs. dynamical dark energy (w0/wa parametrization), (2) flat LambdaCDM vs. curved universe (spatially open or closed), (3) power-law inflation with fixed spectral tilt vs. running spectral index. For each model pair, we compute Bayes factors, measure model evidence, and assess the statistical significance of preference for one model over another. We find inconclusive evidence between flat LambdaCDM and simple dark-energy extensions, strong disfavor for curved universes, and weak preference for running spectral index. We demonstrate that PMC is a practical, parallelizable alternative to nested sampling for high-dimensional evidence estimation, with quantified uncertainties.

---

## Historical Context

The "inverse problem" in cosmology is acute: given observations (CMB power spectrum, galaxy surveys, supernovae distances), which model is correct? The Standard Model (LCDM: 68% dark energy at w=-1, 27% dark matter, 5% baryons) fits current data well, but competing models exist:

- **Dynamical dark energy**: w(z) = w0 + wa(1 - a), allowing dark energy density to vary with redshift.
- **Curvature**: Omega_k ≠ 0, relaxing the assumption of a flat universe.
- **Modified gravity**: f(R) gravity, DGP braneworld, or scalar-tensor theories as alternatives to Lambda.
- **Early-universe physics**: Running spectral index, primordial tensors, or non-Gaussianity in inflation.

The problem is that all these models can fit current data with different assumptions, and each adds parameters. How does one decide which model is "best"? The frequentist answer is "model comparison via chi-squared" or "information criteria" (AIC, BIC). The Bayesian answer is "Bayes factors" and "model evidence."

**Bayes factor** for comparing models M1 and M2:

$$ B_{12} = \frac{P(D | M_1)}{P(D | M_2)} = \frac{\int \mathcal{L}(D | \theta_1, M_1) P(\theta_1 | M_1) d\theta_1}{\int \mathcal{L}(D | \theta_2, M_2) P(\theta_2 | M_2) d\theta_2} $$

where $\mathcal{L}$ is the likelihood and $P(\theta | M)$ is the prior. The Bayes factor naturally penalizes models with more free parameters (Occam's razor).

**The challenge**: Computing the model evidence $P(D|M)$ requires marginalizing over all parameter space. For a 10-parameter cosmological model, this is a high-dimensional integral. Traditional MCMC (Markov Chain Monte Carlo) is designed for parameter estimation (posterior $P(\theta|D)$), not evidence calculation.

The 2010 Kilbinger et al. paper introduces **Population Monte Carlo (PMC)**, a method specifically designed for evidence calculation.

---

## Key Arguments and Derivations

### Monte Carlo Evidence Estimation

The model evidence is:

$$ P(D | M) = \int \mathcal{L}(D | \theta) P(\theta | M) d\theta = \int p(\theta) \mathcal{L}(D | \theta) \frac{1}{\int p(\theta') \mathcal{L}(D | \theta') d\theta'} d\theta $$

where $p(\theta) P(\theta)$ is the prior-weighted density.

Naive Monte Carlo: if you sample $N$ points $\theta_i$ from the prior, then:

$$ P(D|M) \approx \frac{1}{N} \sum_{i=1}^N \mathcal{L}(D | \theta_i) $$

But this is inefficient: most prior samples have negligible likelihood. For a 10-parameter model, 99.99% of samples fall in regions with near-zero likelihood.

### Importance Sampling and Adaptive Sampling

**Importance sampling**: Sample from an **importance distribution** $q(\theta)$ (instead of the prior), and reweight:

$$ P(D|M) = \int p(\theta) \mathcal{L}(D|\theta) d\theta = \int \frac{p(\theta)}{q(\theta)} \mathcal{L}(D|\theta) q(\theta) d\theta $$

If $q(\theta)$ is chosen to peak where $p(\theta) \mathcal{L}(D|\theta)$ is large, the integral is estimated with fewer samples.

**The problem**: Choosing the optimal $q(\theta)$ requires knowledge of the posterior, which is what you're trying to compute.

**Adaptive solution** (Sequential Monte Carlo / PMC): Build up $q(\theta)$ iteratively.

### The Population Monte Carlo Algorithm

**Iteration t**:

1. **Initialization** ($t=1$): Draw $N$ samples $\theta_i^{(1)}$ from the prior $p(\theta)$. Compute weights:
   $$ w_i^{(1)} = \frac{\mathcal{L}(D | \theta_i^{(1)})}{\sum_j \mathcal{L}(D | \theta_j^{(1)})} $$
   Compute the evidence estimate:
   $$ \log P(D|M) \approx \log \left( \frac{1}{N} \sum_i \mathcal{L}(D | \theta_i^{(1)}) \right) $$

2. **Iteration t+1**: Build an importance distribution from the weighted samples at iteration $t$. One approach: fit a Gaussian mixture to the weighted samples, or use kernel density estimation.

3. **Resample**: Draw $N$ samples from the importance distribution $q^{(t+1)}(\theta)$. For each sample, compute:
   $$ w_i^{(t+1)} = \frac{\mathcal{L}(D | \theta_i^{(t+1)}) p(\theta_i^{(t+1)})}{q^{(t+1)}(\theta_i^{(t+1)})} $$

4. **Evidence accumulation**: Multiply evidence estimates across iterations:
   $$ \log P(D|M) = \sum_{t=1}^T \log \left( \frac{1}{N} \sum_i w_i^{(t)} \right) $$

5. **Repeat** until convergence (weights stabilize, or effective sample size $N_\text{eff} = N (\sum_i w_i^2)^{-1}$ reaches threshold).

**Advantages over nested sampling**:
- PMC is **parallelizable**: Each iteration draws samples independently; samples can be distributed across multiple processors.
- Nested sampling is inherently sequential (must remove low-likelihood samples one by one).
- PMC converges faster for well-behaved posteriors (fewer likelihood evaluations).

**Accuracy**: Kilbinger et al. show that PMC achieves evidence estimates accurate to $\Delta \log P(D|M) \sim 0.08$ (about 1 in log-space), sufficient for model comparison.

### Bayes Factor Interpretation

Standard interpretation (Jeffreys' scale):
- $\log B_{12} > 2.5$ (B > 12): Strong evidence for M1
- $0.5 < \log B_{12} < 2.5$: Weak-to-moderate evidence for M1
- $-0.5 < \log B_{12} < 0.5$: Inconclusive
- $\log B_{12} < -0.5$: Evidence for M2

---

## Key Results

### 1. Flat LambdaCDM vs. Dynamical Dark Energy (w0/wa)

**Data**: WMAP 5 CMB + Union SNIa + SDSS BAO

**Models**:
- M1: Flat, w = -1 (LCDM), 6 parameters (Omega_m, Omega_b, h, tau, n_s, A_s)
- M2: Flat, w(z) = w0 + wa(1-a), 8 parameters (adds w0, wa)

**Result**: $\log B_{21} = 0.3$ (inconclusive). Current data cannot decide whether dark energy is truly constant or evolving.

**Interpretation**: LCDM is slightly preferred by Occam's razor (fewer parameters), but the preference is weak. A large survey (DESI) might tighten this constraint.

### 2. Flat vs. Curved Universe

**Models**:
- M1: Flat, Omega_k = 0
- M2: Curved, Omega_k ≠ 0

**Result**: $\log B_{12} > 3$ (strong evidence for flatness). Curved universe is disfavored at > 99% confidence.

**Interpretation**: This is consistent with CMB observations (inflation predicts flatness). The large-scale geometry of the universe is flat to within 1-2%.

### 3. Running Spectral Index in Inflation

**Models**:
- M1: Power-law inflation, n_s = constant
- M2: Running index, dn_s/d(log k) ≠ 0 (adds 1 parameter)

**Result**: $\log B_{12} = 0.8$ (weak evidence for constant n_s). Data weakly prefer constant tilt, but the evidence is not strong.

**Interpretation**: Current data (WMAP 5) are not sensitive enough to detect running. Future CMB missions (Planck, CMB-S4) will improve.

### 4. Methodology Validation

Kilbinger et al. test PMC against analytical solutions (for toy problems) and nested sampling results. PMC achieves:
- Unbiased evidence estimates (difference < 0.05 in log-space from nested sampling)
- Efficient sampling (100-1000 likelihood evaluations per dimension, competitive with nested sampling)
- Quantified uncertainties (error bars on log B)

---

## Impact and Legacy

The 2010 PMC paper established a practical standard for Bayesian model comparison in cosmology. Its impacts:

1. **Adoption**: PMC became a standard tool in cosmological model comparison. Later surveys (DES, DESI, Euclid, LSST) use PMC or its variants (Importance Nested Sampling, etc.) for systematic model comparison.

2. **Parallelization**: PMC's parallel-friendly nature made it attractive for surveys with large datasets and high-dimensional parameter spaces.

3. **Methodological Clarity**: The paper clarified what Bayes factors do (compare model complexity and goodness-of-fit) and what they don't (tell you whether a model is "true").

4. **Limitations Recognized**: By 2015-2020, practitioners recognized that Bayes factors are sensitive to prior choices. A conservative prior (wide range for parameters) suppresses the Bayes factor (Occam's razor penalizes additional parameters even if they're unconstrained). Different prior choices can reverse the model preference. This led to recommendations: always report Bayes factors with explicit prior definitions, and conduct sensitivity analysis across reasonable priors.

---

## Connection to Phonon-Exflation Framework

**Phonon-exflation makes testable cosmological predictions (w = -1, specific spectrum of primordial perturbations) that must be compared against LCDM and other models using Bayesian methods.**

Key connections:

1. **Model Comparison Framework**: Phonon-exflation is M1 (the alternative); LCDM is M2 (the baseline). To assess whether phonon-exflation is viable, one must compute the Bayes factor B_{PEX/LCDM} using current data (DESI 2025, Planck 2018, SDSS, 2dF BAO, etc.).

2. **The Sagan Standard**: Sagan asks, "Is the framework falsifiable?" The Kilbinger et al. method answers "yes": define phonon-exflation's likelihood (how it predicts the CMB spectrum, BAO peak location, weak lensing convergence power spectrum, etc.), then compute Bayes factor. If B_{PEX/LCDM} < 0.1 (strong evidence against), the framework is excluded. If B > 1 (moderate evidence for), the framework is promising.

3. **Current Status**: Phonon-exflation's likelihood has NOT been fully computed (Sessions 35-38 focused on particle physics and BCS stability, not cosmology). A quantitative comparison with LCDM requires:
   - Integrating the Friedmann equations with the phonon-exflation energy density (the spectral action + BCS condensation energy).
   - Computing the CMB power spectrum (via CAMB or CLASS integration).
   - Computing BAO predictions (via growth function and linear perturbation theory).
   - Computing weak lensing power spectra.
   - Then PMC comparison with DESI 2025, Planck, SDSS.

4. **The Empirical Requirement**: Until this computation is done, phonon-exflation is mathematically interesting but empirically unvalidated. The Kilbinger et al. paper is the methodological blueprint for empirical validation.

5. **Sagan's Verdict**: The framework is **falsifiable but untested**. Once the likelihood is defined, PMC comparison can either validate (B > 1) or rule out (B < 0.1) the framework. The absence of this computation is a critical gap.

---

## Appendix: PMC Pseudocode

```
PMC-Evidence(likelihood, prior, data, N_samples, T_max):
  // Iteration t = 1: initial sampling from prior
  samples[1] = draw N_samples from prior()
  for i in 1:N_samples:
    likelihoods[i] = likelihood(data | samples[1][i])

  log_Z_1 = log(mean(likelihoods))
  log_Z_total = log_Z_1

  // Iterations t = 2, ..., T_max: adaptive importance sampling
  for t in 2:T_max:
    // Fit importance distribution from weighted samples
    weights = likelihoods / sum(likelihoods)
    importance_dist = fit_gaussian_mixture(samples[t-1], weights)

    // Resample
    samples[t] = draw N_samples from importance_dist()
    for i in 1:N_samples:
      likelihoods[i] = likelihood(data | samples[t][i])
      prior_vals[i] = prior(samples[t][i])
      importance_vals[i] = importance_dist(samples[t][i])
      weights[i] = likelihoods[i] * prior_vals[i] / importance_vals[i]

    log_Z_t = log(mean(weights))
    log_Z_total += log_Z_t

    // Check convergence
    if std(log_Z_t) < threshold or N_eff / N_samples > 0.5:
      return log_Z_total

  return log_Z_total
```

