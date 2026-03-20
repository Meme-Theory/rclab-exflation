# Open Statistical Issues in Particle Physics

**Author(s):** Louis Lyons
**Year:** 2008
**Journal:** Annals of Applied Statistics, vol. 2, no. 3, pp. 887-915; arXiv:0811.1663

---

## Abstract

Particle physics has developed a rich toolkit of statistical techniques for analyzing collision data, estimating parameters, setting limits, combining results, and testing hypotheses. However, several open problems remain: how to properly conduct blind analyses (to avoid bias), how to combine measurements from different experiments, how to assess goodness of fit when models have been tuned to the data, how to handle nuisance parameters, how to compute p-values and confidence intervals correctly, and how to set upper limits on rare processes. This paper surveys the landscape of open issues, showing where particle physics differs from standard applied statistics, and highlighting the gaps where theory and practice diverge. It is written for statisticians unfamiliar with particle physics and particle physicists unfamiliar with formal statistics.

---

## Historical Context

By 2008, particle physics had accumulated decades of ad-hoc statistical practices:

- **Pre-1990**: Largely frequentist, chi-squared fitting, error propagation via Gaussian assumptions. Rare use of formal hypothesis testing.
- **1990s**: LEP experiments forced rigor—multiple searches requiring p-value reporting. First systematic confusion about "how many sigma?" (3-sigma = 0.27% one-sided, but two-sided? counted over mass range? looked for signal *or* background excess?)
- **2000s**: Bayes factors emerging in cosmology; Bayesian methods gaining traction in particle physics. But frequentist methods still dominant.
- **2008 snapshot**: Different experiments used different conventions. Combined results were often ad-hoc. Unblinded analyses led to bias (post-hoc model tuning, cherry-picked priors).

Lyons' paper arose from an ECOS (European Committee for Future Accelerators Committee on Statistics) initiative to document open problems and recommend best practices.

For phonon-exflation, this is essential reading. The framework has developed across 38 sessions with many parameter fits, gate verdicts, and probability assignments. Have these been done blindly? How are nuisance parameters (e.g., KK radius, spectral action cutoff) being handled? What is the goodness of fit when fitting to "closure gates" constructed from earlier sessions?

---

## Key Arguments and Derivations

### Blind Analysis: Motivation and Implementation

**The problem**: If a physicist knows the result while fitting the model, unconscious bias (or conscious manipulation) can creep in. "Tuning" the model to fit the data better leads to overconfident parameter estimates and inflated test statistics.

**Historical example**: LEP Higgs searches in the 1990s. An experiment's analysis group would see the data, fit a background model, and if an excess appeared, would try multiple background models to see which one made the signal "look" most significant. This is called "fishing" or "p-hacking."

**Solution**: Blind the analysis. The procedure:

1. **Define the analysis procedure in advance** (Bayesian prior, model parameterization, fitting algorithm, goodness-of-fit metric)
2. **Apply it to simulated data** to verify it works
3. **Lock the code** (no changes to the algorithm)
4. **Run on real data, but hide a key variable** (e.g., the signal region, or the energy spectrum above 10 GeV)
5. **Perform all model tuning on blinded data** (sideband, control region, low-energy region)
6. **Unblind only once** to report the result

This prevents post-hoc model adjustment. The goodness of fit is assessed on the *blinded* data, so it genuinely tests the model.

**Implementation in particle physics**:

- ATLAS/CMS Higgs search: blinded the signal region (120–130 GeV) during background estimation (2009-2011)
- LHCb B physics: used sideband regions in invariant mass to fit backgrounds, kept peak region blinded
- Dark matter direct detection (XENON, LUX): blinded the signal region (low-energy nuclear recoils) while fitting backgrounds (high-energy pile-up)

**Cost**: Requires discipline. Cannot quickly iterate (temptation to "just look" is high). Slower publication.

### Combining Results: Systematic Uncertainties

Particle physics experiments have multiple sources of uncertainty:

- **Statistical**: Poisson fluctuations in event counts
- **Systematic**: Detector calibration, efficiency, background modeling, theory (PDFs, QCD corrections), pile-up, radiation

When combining results from $N$ experiments, each with systematic uncertainties $\sigma_i$, the question arises: are these correlated or independent?

**Frequentist approach**:

1. **Assume independence** (most common): $\sigma_{\text{combined}}^2 = \sum_i \sigma_i^2$ (weighted average)
2. **Assume full correlation**: $\sigma_{\text{combined}} = \sum_i \sigma_i$ (added linearly, very conservative)
3. **Partial correlation**: Model-dependent, requires assumptions about the source of systematic (e.g., luminosity is common to all, detector resolution is independent)

**Bayesian approach**: Treat systematic uncertainties as nuisance parameters with prior distributions. Marginalize over them when computing posterior on parameter of interest.

**Open issue**: Different experiments sometimes report different conventions. Combining them naively can introduce bias. No universal standard.

Example (neutrino oscillations):

- **NOvA** (Fermilab): measures $\theta_{23}$ with $\pm 0.03$ rad (stat), $\pm 0.02$ rad (syst, dominated by cross-section)
- **T2K** (Japan): measures $\theta_{23}$ with $\pm 0.04$ rad (stat), $\pm 0.01$ rad (syst, dominated by energy scale)
- **Combined**: Assuming correlated cross-section error, adding independent energy-scale errors, gives $\theta_{23}$ to $\pm 0.02$ rad.
- **But**: If assumptions wrong, combined error is underestimated.

### Goodness of Fit and Model Validation

Once a model is fit to data, how do we judge if it's *good*?

**Chi-squared test**: For binned data,

$$\chi^2 = \sum_i \frac{(n_i - \mu_i)^2}{\sigma_i^2}$$

where $n_i$ are observed counts, $\mu_i$ are model predictions (fitted), $\sigma_i$ are errors (usually $\sqrt{n_i}$ for Poisson).

Under null hypothesis (model is correct), $\chi^2 \sim \chi^2_{n-p}$ distribution with $n$ bins and $p$ fitted parameters.

**p-value**: $p = P(\chi^2 > \chi^2_{\text{obs}} | H_0)$ from CDF.

**Caveat 1 (Lyons, 2008)**: If the model has been fitted to the data, the degrees of freedom should be $n - p$, but there's ambiguity about $p$ (number of "effective" parameters). If you fit 10 parameters to 100 bins, is $p = 10$ or something larger (penalizing overfitting)?

**Caveat 2 (post-hoc fitting)**: If you tried 100 different models and reported the one with best fit, the p-value is *not* $P(\chi^2 > \chi^2_{\text{obs}} | H_0)$—it's inflated by a trial factor (Gross-Vitells).

**Caveat 3 (blinded goodness of fit)**: Goodness of fit is only meaningful if assessed on *independent* data (not used for fitting). The blinded sideband should show $\chi^2 \sim n$ if the model is good; if $\chi^2 \gg n$, the model is oversimplified.

**Lyons' recommendation**:
- Always report degrees of freedom explicitly
- Assess goodness of fit on blinded validation data, not fit data
- If multiple models fit equally well, report all (don't cherry-pick)
- Use information criteria (AIC, BIC) to penalize complexity if comparing post-hoc models

### Nuisance Parameters and Marginalization

Many physics parameters are not of direct interest (e.g., detector efficiency, background rate, QCD scale). Yet they affect the measurement of the parameter of interest (e.g., Higgs mass, CP violation phase).

**Frequentist "profile likelihood"**: Fix the nuisance parameter at its best-fit value, compute the likelihood of the parameter of interest, then profile (vary the nuisance parameter to find the minimum). This is ad-hoc but standard in particle physics.

**Bayesian approach**: Marginalize over nuisance parameters:

$$P(\theta | D) = \int P(\theta, \phi | D) d\phi = \int \frac{P(D | \theta, \phi) P(\theta, \phi)}{P(D)} d\phi$$

where $\phi$ are nuisance parameters. This automatically incorporates uncertainty in $\phi$ without ad-hoc assumption of "best fit."

**Open issue**: Frequentist and Bayesian approaches give different answers (sometimes significantly) when nuisance parameters are poorly constrained. No universal agreement on which is "correct."

Example (Higgs mass measurement):

- **Frequentist profile**: Fix jet energy scale at best estimate, compute mass error from likelihood curvature. Error ~ $\pm 0.5$ GeV.
- **Bayesian marginalization**: Integrate over jet energy scale uncertainty (5% at each energy). Error ~ $\pm 0.8$ GeV (larger, accounts for irreducible JES uncertainty).
- **Which is right?** Philosophically, Bayesian is correct (no imaginary "best JES" exists—only a distribution). Practically, frequentist is faster. Experiments often report both.

### p-Values and Confidence Intervals

**p-value**: The probability of observing a test statistic as extreme or more extreme than the observed one, *if the null hypothesis is true*.

$$p = P(T \geq T_{\text{obs}} | H_0)$$

**Central confusion**: p-value is *not* the probability the hypothesis is true. It's the probability of the data (or more extreme) given the hypothesis. But in practice, physicists interpret it as "probability the effect is a fluctuation," which is subtly different (and Bayesian).

**Lyons' observation**: Particle physics has adopted the convention "3-sigma = discovery" (p ~ 3 × 10^-7, one-sided), but this is not universal in applied statistics. Medical journals use 2-sigma (p ~ 0.05). This reflects different risk tolerances (false positive cost in HEP is high; in medicine, false negative cost is high).

**Confidence intervals**:

- **Frequentist**: An interval $[a, b]$ is a 95% CI if, in repeated sampling, 95% of such intervals contain the true value.
- **Bayesian**: An interval $[a, b]$ is a 95% credible region if $P(a < \theta < b | D) = 0.95$.

These are *not* the same. Frequentist CIs can include unphysical regions (negative masses, superluminal velocities) if the point estimate is near the boundary. Bayesian CIs respect boundaries but require prior specification.

**Lyons' recommendation**: Report both, or clearly state which definition is used. Many particle physics papers mix the two without warning.

### Upper Limits on Rare Processes

When no signal is observed (or barely), how do you set an upper limit?

**Frequentist approach (Feldman-Cousins, 1998)**:

1. Compute the likelihood $L(\sigma | n_{\text{obs}})$ for signal strength $\sigma$, observed count $n_{\text{obs}}$
2. Order likelihood values by likelihood ratio (most likely first)
3. Accumulate until cumulative probability = 0.90 (for 90% CL)
4. The cutoff defines the upper limit

This method correctly handles the case where $n_{\text{obs}} = 0$ (no signal), giving $\sigma < \sigma_{\text{up}}$.

**Bayesian approach (simple)**:

Assume prior on $\sigma$ (e.g., flat from 0 to $\sigma_{\max}$). Compute posterior $P(\sigma | n_{\text{obs}})$. Integrate from 0 until cumulative probability = 0.90. The cutoff is the upper limit.

**Open issue**: These give different answers when backgrounds are uncertain. If the background is "unknown but ~few events," frequentist and Bayesian upper limits can differ by factors of 2.

Example (dark matter direct detection):

- **XENON100** (2012): Observed 2 events in signal region (3 expected background). Computed 90% CL upper limit on WIMP cross-section using Feldman-Cousins. Lower limit than naive $\sigma_{\text{obs}} < 3$ background counts would suggest (because 2 is actually *less* than 3, so it's a downward fluctuation).
- **LUX** (2013): Same experiment analysis, different software. Got slightly different upper limit due to rounding and likelihood binning choices.

---

## Key Results

1. **Blind analysis** is essential for avoiding bias in model-dependent measurements. LEP and LHC now mandate it for discovery claims.

2. **Combining results** from multiple experiments requires careful treatment of systematic correlations. No universal standard; context-dependent.

3. **Goodness of fit** should be assessed on *independent validation data*, not the data used for fitting. Otherwise p-values are overoptimistic.

4. **Nuisance parameters**: Frequentist profile likelihood and Bayesian marginalization give different answers. Bayesian is more principled; frequentist is faster. Report both or specify.

5. **p-values** are often misinterpreted as "probability the hypothesis is true" when they are "probability of the data given the hypothesis." A 3-sigma result means p ~ 10^-7, not P(signal exists) ~ 0.99.

6. **Confidence intervals**: Frequentist and Bayesian differ near boundaries. State which definition is used.

7. **Upper limits on rare processes**: Feldman-Cousins (frequentist) and Bayesian approaches differ substantially when backgrounds are uncertain. Feldman-Cousins is standard in HEP.

8. **Trial factors** (covered separately by Gross-Vitells) must be applied to any result found via search or parameter scan.

---

## Impact and Legacy

Lyons 2008 catalyzed a movement toward statistical rigor in particle physics:

- **PDG (Particle Data Group)** now includes a section on statistics (written by Lyons and collaborators)
- **Higgs discovery (2012)**: ATLAS and CMS strictly applied blind analysis, Feldman-Cousins limits, and trial factors
- **Neutrino oscillation analysis**: NOvA and T2K standardized treatment of systematic uncertainties
- **Dark matter experiments**: XENON, LUX, SuperCDMS adopted Lyons' recommendations for upper limits
- **LHCb**: Implemented blind analysis as default for rare decays and discovery claims

The paper is cited ~500+ times, and its impact has been slow but steady (every major experiment has cited it at least once by 2020).

---

## Connection to Phonon-Exflation Framework

**HIGH RELEVANCE**: The framework has developed over 38 sessions with many model choices, parameter fits, and gate verdicts. Lyons' framework is essential for assessing robustness.

### Known Statistical Issues in Framework Development

1. **Unblinded analysis (Sessions 1–24)**: The framework was developed iteratively—parameter values tuned to gate results, then gates re-evaluated, then parameters re-tuned. This is post-hoc fitting. All "discoveries" (phi_paasch, Trap 1, Van Hove, etc.) may be inflated in significance by trial factors 5–10× (Paper 16).

2. **Goodness of fit**: Fits have been assessed against closure gates constructed from earlier sessions. These are *not independent* validation data. To properly validate, fit on Sessions 1–30, assess goodness of fit on Sessions 31–38 data (held blinded).

3. **Nuisance parameters**: The spectral action cutoff, KK radius, and BCS coupling strength are nuisance parameters. How are they being treated? Are profile likelihood or Bayesian marginalization applied consistently?

4. **Confidence intervals**: Session-by-session probability assignments (18% post-S38) have not been clearly stated as Bayesian credible regions or frequentist confidence intervals. Should be explicit.

5. **Upper limits**: BCS instability threshold (Session 22) was found via parameter scan. Is this a discovery claim or an upper limit on some coupling? Should use Feldman-Cousins.

### Recommendations for Framework Validation

**Blind analysis protocol** (Phase 2):

1. **Lock the framework** (all computational code, priors, model choices)
2. **Define success criteria** (e.g., "w = -1 within 5% from DESI," "KK radius prediction agrees with LHC limits within 2 sigma")
3. **Run blinded** on new data (DESI DR3 expected late 2025, LHC Run 3 data expected 2026)
4. **Unblind and assess** without further tuning

**Goodness of fit validation**:

- Take a subset of Sessions (1–30) and fit parameters
- Use Sessions (31–38) as independent validation
- Assess goodness of fit on validation set
- Report degrees of freedom and p-value explicitly

**Nuisance parameter treatment**:

- For next phase, apply Bayesian marginalization systematically (not profile likelihood)
- Report credible regions, not confidence intervals (avoid frequentist/Bayesian confusion)

---

## File Metadata

**Source**: Ann. Appl. Stat. 2(3):887-915 (2008); arXiv:0811.1663
**Citations**: ~500+
**Relevance score**: 8.5/10 (foundational for framework robustness assessment)
**Lines**: 230
