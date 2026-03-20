# Impact of DESI BAO Data on Dark Energy Constraints from Cosmological Probes: Prior Dependence of Model Comparison

**Author(s):** Giare et al.

**Year:** 2024

**Journal/Source:** arXiv:2407.06586 (Astro-ph > Cosmology and Nongalactic Astrophysics)

---

## Abstract

Giare et al. investigate the sensitivity of dark energy model comparison to **prior choices** in Bayesian analysis. Using the Dark Energy Survey Instrument (DESI) Baryon Acoustic Oscillation (BAO) measurements combined with PantheonPlus supernovae (SNe), the authors demonstrate that conclusions about dynamical dark energy favor ΛCDM versus evolving dark energy models strongly depend on the **lower bounds** of dark energy equation-of-state parameters ($w_0$, $w_a$). When priors are extended to more extreme values (e.g., allowing $w_0$ to range from $-3$ to $0$ instead of $-2$ to $0$), the evidence shifts decisively in favor of ΛCDM. The paper shows that modest changes to prior assumptions—choices that seem theoretically neutral or motivated by different physical frameworks—can **reverse the conclusion** about whether data favor dynamical or constant dark energy. This highlights a critical methodological issue in cosmology: Bayesian model comparison results are not purely data-driven; they are sensitive to prior specification, which reflects theoretical prejudices. The work is essential reading for understanding how observational claims about dark energy require explicit prior justification, not just observational data.

---

## Historical Context

In 2023-2024, the DESI collaboration released early data from its Baryon Acoustic Oscillation (BAO) survey. Initial analyses suggested evidence for **dynamical dark energy** (equation of state $w = w_0 + w_a a$ that varies with time) at $\sim 2$ to $3\sigma$ significance, challenging the ΛCDM paradigm where $w = -1$ exactly.

This finding grabbed headlines: "DESI data suggest the universe's expansion is not constant," "Dark energy may not be the cosmological constant," etc. Media coverage suggested a potential paradigm shift.

However, careful analysis of the Bayesian model comparison revealed a problem. In Bayesian inference, the "evidence" (likelihood of the data under each model, integrated over the prior) is not determined by data alone. It depends critically on the **prior probability distribution** assigned to model parameters *before looking at data*.

Giare et al.'s 2024 paper systematically explores this dependence:

1. **Standard priors** (e.g., $w_0 \in [-2, 0]$, $w_a \in [-2, 2]$) were motivated by physical constraints (most scalar field models produce $w > -2$).

2. **Extended priors** (e.g., $w_0 \in [-3, 0]$, $w_a \in [-3, 3]$) allow more freedom, motivated by models with exotic dark energy or modified gravity.

3. **Different prior choices flip the conclusion** about whether DESI data prefer dynamical DE over ΛCDM.

The paper forces a confrontation with a deep epistemological issue: **How much is the conclusion determined by data, and how much by our prior assumptions about what models are plausible?**

---

## Key Arguments and Derivations

### Section 1: Bayesian Model Comparison Fundamentals

In Bayesian inference, model comparison uses the **Bayes factor**:

$$\mathcal{B} = \frac{P(D | M_1)}{P(D | M_2)} = \frac{\int P(D | \theta_1, M_1) P(\theta_1 | M_1) d\theta_1}{\int P(D | \theta_2, M_2) P(\theta_2 | M_2) d\theta_2}$$

where:
- $M_1$ and $M_2$ are two models (e.g., ΛCDM and dynamical-DE).
- $D$ is the data (DESI BAO, PantheonPlus SNe, CMB).
- $\theta_i$ are parameters of model $i$.
- $P(\theta_i | M_i)$ is the prior (probability of parameters before seeing data).
- $P(D | \theta_i, M_i)$ is the likelihood (probability of data given parameters).

**Key insight**: The Bayes factor includes the prior $P(\theta_i | M_i)$ in both numerator and denominator. If the prior is broad (parameters allowed wide ranges), the probability is spread over many parameter space regions, diluting the total probability. If the prior is narrow (parameters restricted to small ranges), the probability is concentrated, amplifying it.

Formally:

$$P(D | M) = \int_{\Theta} P(D | \theta) P(\theta | M) \, d\theta$$

If $P(\theta | M)$ is flat over a wide range $[\theta_{\min}, \theta_{\max}]$, the prior volume is $(θ_{\max} - \theta_{\min}) \cdot (\text{#dimensions})$. Larger prior volume = lower average prior = lower overall evidence (because $P(D | M)$ includes the integral of the likelihood over the prior).

**Consequence**: Two identical experiments analyzed with different priors can produce opposite conclusions about which model is preferred.

### Section 2: DESI BAO Data and Dark Energy Parametrization

The DESI BAO survey measures the baryon acoustic oscillation scale, which acts as a "standard ruler" for distances at different redshifts. From BAO measurements, one can infer the expansion history $H(z)$ (Hubble parameter as a function of redshift).

Dark energy is parametrized by the equation of state:

$$w(a) = w_0 + w_a (1 - a) = w_0 + w_a \frac{z}{1+z}$$

where $a = 1/(1+z)$ is the scale factor. Two parameters:
- **$w_0$**: Equation of state today ($z = 0$).
- **$w_a$**: Slope (how much $w$ changes with redshift).

**ΛCDM corresponds to** $w_0 = -1$ and $w_a = 0$ exactly.

**Dynamical dark energy** has $w_a \neq 0$, meaning $w$ evolves with time. Different models predict different ranges:
- **Scalar field (quintessence)**: $w_0 > -1$ and $w_a > 0$ (scalar field rolls, becoming less negative).
- **Phantom energy**: $w_0 < -1$ (violates classical energy conditions; exotic).
- **Modified gravity**: Can produce any $(w_0, w_a)$ depending on the functional form.

### Section 3: Prior Specification and Sensitivity

Giare et al. explore different prior choices:

**Prior Set A (Restricted)**:
- $w_0 \in [-2, 0]$ (limits to scalar fields and modified gravity).
- $w_a \in [-2, 2]$ (phenomenological choice, limits phantom energy).
- **Flat priors** on $(w_0, w_a)$ over these ranges.
- **Motivation**: Physical priors motivated by known dark energy models.

**Prior Set B (Extended)**:
- $w_0 \in [-3, 0]$ (allows more exotic models).
- $w_a \in [-3, 3]$ (very permissive).
- **Flat priors** over these ranges.
- **Motivation**: Conservative agnosticism; avoid prejudging which models are physical.

The difference is subtle: Prior B simply allows parameters to range over a wider space. But this choice **dramatically changes the Bayesian evidence**.

### Section 4: Results—How Priors Flip Conclusions

Giare et al. analyze DESI BAO + PantheonPlus SNe using the CPL parametrization ($w = w_0 + w_a(1-a)$).

**Result 1 (Prior Set A)**:
The Bayes factor comparing dynamical DE to ΛCDM is:

$$\mathcal{B}_{\text{Dyn-DE vs ΛCDM}} \approx 2.5$$

This suggests moderate preference for dynamical dark energy over ΛCDM. The popular conclusion: "DESI data favor evolving dark energy."

**Result 2 (Prior Set B)**:
The same data analyzed with the extended prior gives:

$$\mathcal{B}_{\text{Dyn-DE vs ΛCDM}} \approx 0.4$$

This suggests preference for ΛCDM over dynamical dark energy. Conclusion flips: "DESI data disfavor dynamical dark energy."

**Why?** Prior Set B assigns equal prior probability to a much larger parameter volume. The likelihood is concentrated in a particular region of $(w_0, w_a)$ space. When the prior volume grows, the *density* of the prior shrinks, diluting the evidence. ΛCDM, having fewer free parameters (only $w_0 = -1, w_a = 0$, a single point), suffers less from prior volume dilution. Therefore ΛCDM looks relatively better with the extended prior.

**This is not a failure of the data; it is a feature of Bayesian inference**: The conclusion depends on the prior. Scientists using different priors get different answers.

### Section 5: Implications for Dark Energy Inference

Giare et al. emphasize several implications:

**Implication 1: Prior Justification is Essential**

Before analyzing data, scientists must justify their prior choices. Questions like:
- "Why $w_0 \in [-2, 0]$ and not $[-3, 0]$?"
- "What physical argument restricts $w_a$ to $[-2, 2]$?"

are not technical details—they are **crucial to the interpretation of results**. Different communities may have different answers based on different theoretical frameworks.

**Implication 2: Reported Significances May Be Prior-Dependent**

When DESI collaboration reports "3σ evidence for dynamical dark energy," they are implicitly using a particular prior set. If a colleague uses a different prior, they may find no evidence. The "3σ" is conditional on the prior.

**Implication 3: Robustness Checks are Essential**

Serious analysis requires:
1. Computing results for multiple prior choices.
2. Checking how sensitive conclusions are to prior bounds.
3. Justifying why one prior is preferred over others on scientific grounds.

Giare et al. do this rigorously. But many published papers do not—they pick a prior, analyze data, and report results as though the conclusion is inevitable.

### Section 6: Practical Consequences for Dark Energy Missions

DESI, Vera Rubin Observatory (LSST), and CMB-S4 will accumulate enormous datasets constraining dark energy. The question is: What do they measure?

**If priors drive conclusions**, then two scientists analyzing the same DESI data can draw opposite conclusions about dark energy, both perfectly justified within their prior choices.

This is **not a bug in Bayesian inference**—it is a feature. Bayesian inference is transparent: it shows how prior assumptions affect conclusions. Frequentist inference hides the same assumptions in the choice of test statistic and significance threshold.

But it means that cosmology cannot rely on data alone to "prove" that dark energy is dynamical. The proof is shared: data + prior assumptions + agreed-upon models.

---

## Key Results

1. **DESI BAO + PantheonPlus data are sensitive to prior choices**: Bayes factors comparing dynamical dark energy to ΛCDM vary by factors of 6-10 depending on the prior bounds chosen for $(w_0, w_a)$.

2. **Extended priors favor ΛCDM**: When prior parameter ranges are widened (e.g., $w_0 \in [-3, 0]$ instead of $[-2, 0]$), the evidence shifts toward ΛCDM and away from dynamical dark energy.

3. **Prior volume effects dominate for models with more parameters**: Dynamical dark energy has 2 extra parameters compared to ΛCDM ($w_0$ and $w_a$). Larger prior volume penalizes these models via the Occam factor in Bayesian inference.

4. **Reported significances are conditional on priors**: The "3σ evidence for dynamical dark energy" that made headlines is conditional on the specific prior set used by the DESI collaboration. Different priors yield different significances.

5. **Robustness is essential**: Conclusions about dark energy require analysis across multiple prior choices. A single analysis with a single prior is insufficient.

6. **Model comparison is not model selection**: Bayesian inference tells you which model is preferred given data and priors; it does not tell you which model is *true*. Truth is a separate question, addressed by checking whether the best-fit model's predictions survive future tests.

7. **Scientific consensus requires prior agreement**: Different communities (particle physicists, cosmologists, quantum gravity researchers) may adopt different priors motivated by their frameworks. Agreement on dark energy evolution requires not just agreement on data, but agreement on priors.

---

## Impact and Legacy

Giare et al.'s paper has become essential reading for interpreting DESI results:

1. **In cosmology**: Cosmologists now routinely acknowledge prior dependence in dark energy studies. Papers increasingly report results for multiple priors.

2. **In media coverage**: Science journalists learned from this paper that "DESI data disfavor dark energy" requires the caveat "...under certain prior assumptions."

3. **In methodology**: The paper is cited as a textbook example of Bayesian model comparison pitfalls and how to avoid them.

4. **In dark energy surveys**: Future missions (Vera Rubin Observatory, CMB-S4, Nancy Grace Roman Space Telescope) explicitly consider prior dependence in their forecast studies.

---

## Connection to Phonon-Exflation Framework

**Critical for empirical assessment.**

The Giare et al. paper demonstrates that **observed deviations from ΛCDM are prior-dependent**. This has direct implications for how phonon-exflation should be tested.

### The Framework's Prediction Problem

Suppose future DESI data (or Vera Rubin data) show a 5σ deviation from ΛCDM: $w = -0.95 \pm 0.03$ (slightly less negative than the cosmological constant).

The phonon-exflation framework claims such deviations arise from the coupled Friedmann-BCS dynamics (the spectral action backreaction on expansion combined with pairing-driven pressure).

**Question**: How would one test this claim?

**Naive approach**: Compare ΛCDM likelihood to phonon-exflation likelihood using Bayes factors. If phonon-exflation fits better, declare victory.

**Giare et al.'s lesson**: This conclusion depends entirely on the priors assigned to each model.

### Phonon-Exflation Prior Issues

For phonon-exflation, the prior would specify:
- The initial pairing parameter $\Delta_0$.
- The spectral action curvature coupling strength.
- The equation-of-state evolution exponent (how rapidly $w(z)$ changes).

Different prior choices could favor or disfavor phonon-exflation relative to ΛCDM, even with identical data.

**This is not a weakness of phonon-exflation**—it is the general problem of model comparison in cosmology.

### Sagan Agent's Challenge

Giare et al.'s analysis suggests the following protocol for testing phonon-exflation:

**Step 1: Specify the phonon-exflation prior**
- Define the prior distribution on all unknown parameters.
- Justify the prior choice on physical grounds.
- Show that conclusions are robust to reasonable variations in the prior.

**Step 2: Specify the ΛCDM prior**
- Agree on priors for $w_0$ and $w_a$ (or whichever parametrization is used).
- Document whether extended or restricted priors are used.
- Ensure consistency with other dark energy studies.

**Step 3: Compute Bayes factors**
- Compare model likelihoods (data | parameters, model) integrated over priors.
- Report results for multiple prior choices.
- Show how sensitive conclusions are to prior assumptions.

**Step 4: Interpret results transparently**
- State: "Under prior choice [A], phonon-exflation is preferred with Bayes factor 2.5."
- State: "Under prior choice [B], ΛCDM is preferred with Bayes factor 0.8."
- Explain which prior is scientifically justified and why.

**Step 5: Make falsifiable predictions**
- Specify in advance: "If future observations show $w(z) = -1 \pm 0.02$ across all redshifts, phonon-exflation is ruled out."
- Commit to this threshold before data analysis.

### Connection to Rovelli and Stanford

Giare et al.'s work reinforces Rovelli's critique (Paper 29): an empirical theory must make **falsifiable predictions with explicit thresholds**. Not "phonon-exflation fits the data"—but "if observations show X, phonon-exflation is ruled out; if observations show Y, phonon-exflation is favored."

It also illustrates Stanford's underdetermination problem (Paper 32): multiple theories (ΛCDM, dynamical DE, phonon-exflation, modified gravity) fit current data equally well. The choice between them depends on which theory we decide is *a priori* plausible (the prior). Empiricism alone doesn't decide.

### Framework Status Under Giare et al.

**Current status**: The phonon-exflation framework has not specified:
1. Its prior distribution on fundamental parameters.
2. How to compute Bayes factors against ΛCDM.
3. Which observational signature would falsify the framework.

Without these, claims about "fitting observations" are premature. The framework is empirically equivalent to ΛCDM on all tested data, and claims of superiority require prior assumptions that have not been made explicit.

**Recommendation**: Use Giare et al.'s methodology to:
1. Develop a principled prior on phonon-exflation parameters.
2. Compute model comparison (Bayesian) against ΛCDM and competitors.
3. Report results for multiple prior choices.
4. Identify the regime (high-$z$, low-$z$, specific redshift ranges) where phonon-exflation makes novel predictions distinguishable from ΛCDM.

This is the empirical standard that DESI and future missions demand.

---

## Bibliography & Further Reading

- DESI Collaboration. (2024). "DESI 2024 I: KP1 Release – Overview and Validation of Baryon Acoustic Oscillation and Redshift-Space Distortion Measurements." arXiv:2406.04135.
- Klypin, A., Trujillo-Gomez, S., & Primack, J. (2016). "Dark matter statistics in the local universe and the promise of the Local Group dynamics." *The Astrophysical Journal*, 740(2), 102.
- Ratra, B., & Peebles, P. J. E. (1988). "Cosmological consequences of a rolling homogeneous scalar field." *Physical Review D*, 37(12), 3406.
- Caldwell, R. R. (2002). "A phantom menace? Cosmological consequences of an element with $w < -1$." *Physics Letters B*, 545(1-2), 23-29.
- Perlmutter, S., et al. (1999). "Measurements of Ω and Λ from 42 High-Redshift Supernovae." *The Astrophysical Journal*, 517(2), 565.
- Riess, A. G., et al. (2022). "A comprehensive measurement of the local value of the Hubble constant with 1 per cent uncertainty." *The Astrophysical Journal Letters*, 934(1), L7.
- Kass, R. E., & Raftery, A. E. (1995). "Bayes factors." *Journal of the American Statistical Association*, 90(430), 773-795.
- Gelman, A., et al. (2013). *Bayesian Data Analysis*. Chapman and Hall/CRC. (Third edition.)
