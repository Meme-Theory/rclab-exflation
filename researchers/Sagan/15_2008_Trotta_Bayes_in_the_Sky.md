# Bayes in the Sky: Bayesian Inference and Model Selection in Cosmology

**Author(s):** Roberto Trotta
**Year:** 2008
**Journal:** Contemporary Physics, vol. 49, pp. 71-104

---

## Abstract

This invited review covers Bayesian probability theory and its applications to cosmological inference, with particular emphasis on Bayesian model comparison. The paper systematically presents Bayes' theorem, the conceptual foundations of Bayesian inference, prior specification, parameter estimation via Markov Chain Monte Carlo methods, and the central novelty: Bayesian model selection via Bayesian evidence, Occam factors, and the Jeffreys scale. Recent applications to cosmological parameter extraction and model building are reviewed. The paper serves as the canonical pedagogical reference for model comparison in cosmology.

---

## Historical Context

Prior to ~2005, cosmological model comparison was dominated by frequentist approaches: chi-squared fitting, parameter error bars, and informal model preference. As the precision era began—driven by WMAP, galaxy surveys, and Type Ia supernovae—the question became acute: how do we *formally* compare non-nested models (e.g., LCDM vs. modified gravity)?

Trotta's 2008 review crystallized Bayesian model selection as the standard methodology. The key advantage over frequentism: Bayesian evidence automatically penalizes model complexity (Occam's razor emerges from the mathematics, not as external principle). This resolved a major technical gap: how to compare theories with different numbers of free parameters.

For the phonon-exflation framework, this is critical. At 18% probability, the framework is a minority model. Formal model selection tools provide objective criteria for comparing it against LCDM. The Jeffreys scale offers a standardized language for discussing relative plausibility.

---

## Key Arguments and Derivations

### Bayes' Theorem and Prior Specification

The foundation is Bayes' theorem:

$$P(M | D) = \frac{P(D|M)P(M)}{P(D)}$$

where $M$ is a model (theory), $D$ is data, $P(M|D)$ is the posterior probability of the model, $P(D|M)$ is the likelihood (evidence), and $P(M)$ is the prior probability on the model.

The denominator, $P(D)$, is the marginal likelihood or *Bayesian evidence*:

$$\mathcal{Z}(M) = P(D|M) = \int P(D | \theta, M) P(\theta | M) d\theta$$

This integral weights the likelihood by the prior over the entire parameter space. Crucially, high-dimensional parameter spaces with broader priors contribute *less* to the evidence (they "waste" prior volume on regions inconsistent with data). This is the origin of Occam's razor in Bayesian mechanics.

Prior specification is not arbitrary. Trotta discusses several principled approaches:

1. **Jeffreys priors**: Invariant under reparameterization, derived from Fisher information
2. **Reference priors**: Maximize entropy subject to constraints (Berger-Bernardo)
3. **Empirical Bayes**: Use marginal likelihood to set hyperparameters (avoids double-counting information)
4. **Hierarchical priors**: Encode domain knowledge without overfitting

### Parameter Inference: MCMC Methods

Once the posterior is defined, $P(\theta | D, M)$, samples are drawn via Markov Chain Monte Carlo:

$$P(\theta | D, M) \propto P(D | \theta, M) P(\theta | M)$$

Standard methods include:

- **Metropolis-Hastings**: Accept/reject proposals based on Metropolis ratio
- **Gibbs sampling**: Sample each parameter conditional on others (for well-structured posteriors)
- **Hamiltonian Monte Carlo**: Use gradient information to propose more efficient jumps
- **Importance sampling**: Weight samples by likelihoods to estimate evidence

Evidence is estimated from MCMC samples via:
- **Harmonic mean estimator**: $\mathcal{Z}^{-1} = \langle \mathcal{L}^{-1} \rangle$ (biased for sharp posteriors)
- **Nested sampling**: Iteratively volume-contract the prior, accumulate evidence (gold standard, Skilling 2004)
- **MultiNest**: Implementation of nested sampling with multimodal support

### Model Comparison: Evidence Ratios and Occam Factors

The posterior odds ratio is:

$$\frac{P(M_1 | D)}{P(M_2 | D)} = \frac{\mathcal{Z}(M_1)}{\mathcal{Z}(M_2)} \times \frac{P(M_1)}{P(M_2)}$$

If prior odds are equal, the ratio of evidences is the *Bayes factor*:

$$B_{12} = \frac{\mathcal{Z}(M_1)}{\mathcal{Z}(M_2)}$$

Trotta derives the decomposition:

$$B_{12} = \underbrace{\frac{\max P(D|\theta_1, M_1)}{\max P(D|\theta_2, M_2)}}_{\text{likelihood ratio}} \times \underbrace{\frac{\Delta V_1}{\Delta V_2}}_{\text{Occam factor}}$$

The Occam factor arises because:
- Simpler model (fewer parameters, tighter priors) has smaller $\Delta V$, larger Bayes factor *for same likelihood*
- Complex model spreads prior over larger space; must achieve proportionally higher likelihood to compensate

This is *not* arbitrary penalization—it emerges mathematically from the probability integral.

### Jeffreys Scale

Trotta presents the Jeffreys scale for interpreting Bayes factors:

| $\log_{10} B_{12}$ | $B_{12}$ | Interpretation |
|:---|:---|:---|
| $0 - 0.5$ | $1 - 3$ | Weak evidence for M1 |
| $0.5 - 1$ | $3 - 10$ | Moderate evidence for M1 |
| $1 - 2$ | $10 - 100$ | Strong evidence for M1 |
| $> 2$ | $> 100$ | Very strong evidence for M1 |

Negative values favor M2. The scale is conventionally applied as:
- $B > 10$: Decisive
- $B \sim 3-10$: Moderate (requires caution)
- $B < 3$: Weak (no strong conclusion)

### Information Criteria as Approximations

For large datasets, Bayesian model selection can be approximated via information criteria (avoiding explicit evidence computation):

**Akaike Information Criterion (AIC)**:
$$\text{AIC} = -2 \ln \mathcal{L}_{\max} + 2k$$

**Bayesian Information Criterion (BIC)**:
$$\text{BIC} = -2 \ln \mathcal{L}_{\max} + k \ln N$$

where $k$ is number of parameters, $N$ is sample size. AIC is frequentist (no priors), BIC approximates Bayes factor under uniform priors. Both penalize complexity; BIC does so more strongly.

### Application to Cosmological Model Building

Trotta reviews applications to:

1. **Parameterized dark energy models**: $w = w_0 + w_a(1-a)$ vs. LCDM. Bayes factors show LCDM strongly preferred unless data significantly improve under richer model.

2. **Modified gravity vs. GR**: Screened modifications (chameleon, symmetron, etc.) add parameters; Bayes factors favor simpler gravity unless deviations are large.

3. **Neutrino mass hierarchy**: Normal vs. inverted, fixed vs. free masses. Bayes factors quantify gain from precision oscillation data.

4. **Curvature**: Closed vs. open universe. Non-zero curvature requires significant likelihood improvement to overcome Occam factor.

5. **Inflation variants**: Single-field slow-roll vs. multiple fields, DBI, ekpyrotic. Nested models compared via evidence.

The key finding across all these: LCDM is remarkably resilient. For it to be disfavored, an alternative must fit data *substantially* better to overcome Occam penalty. This is the quantitative meaning of "LCDM is the minimal model"—it wins on Bayes factors, not just chi-squared.

---

## Key Results

1. **Bayesian evidence is the gold standard for model comparison**. It automatically incorporates Occam's razor via the prior volume integral.

2. **Occam factor** arises mathematically: $\Delta V_1 / \Delta V_2$ (not ad hoc). Simpler models are favored *if* they fit equally well.

3. **Jeffreys scale** provides standardized language. $B > 10$ is decisive; $3 < B < 10$ is worth reporting but requires caution.

4. **Nested sampling** is the preferred implementation (Skilling 2004). Requires ~10^3 to 10^5 likelihood evaluations per parameter dimension.

5. **Information criteria (AIC, BIC)** are fast approximations but lose information. Suitable for exploratory comparisons; evidence is preferred for final conclusions.

6. **LCDM dominates cosmological model selection** across independent datasets (WMAP, BAO, SNe, galaxy clusters) because it has few parameters and fits well. Alternatives must show >10× likelihood improvement to overcome Occam factor.

7. **Prior sensitivity matters**. Broader priors on extra parameters penalize the model more (larger $\Delta V$). Empirical Bayes helps, but "weak" priors must be justified theoretically.

---

## Impact and Legacy

Trotta 2008 became the standard reference for cosmological model selection. Within a few years, it was adopted by:

- **Planck Collaboration**: Used Bayesian model selection for inflation parameterizations, neutrino masses, curvature
- **Dark energy task forces**: Recommended Bayes factors for comparing modified gravity models
- **ACT, SPT, DESI teams**: Standard toolkit for model comparison against LCDM
- **Modified gravity reviews**: Reviewers cite Jeffreys scale when evaluating screened theories

The paper also catalyzed development of faster nested sampling algorithms (MultiNest, PolyChord, UltraNest) and hybrid methods (ABC, variational inference) for high-dimensional problems.

---

## Connection to Phonon-Exflation Framework

**CRITICAL RELEVANCE**: Trotta 2008 provides the formal machinery for evaluating phonon-exflation against LCDM.

Current status: Framework at 18% post-Session 38, LCDM at 82%. Translating this to Bayesian language:

- Prior odds $P(\text{phonon})/P(\text{LCDM}) \approx 1$ (symmetric at outset, each is a "possibility")
- Posterior odds post-S38: $\approx 18/82 \approx 0.22$
- Implied Bayes factor: $B \approx 0.22$ (favors LCDM, barely decisive on Jeffreys scale)

The framework currently loses because:

1. **No novel predictions of *unmeasured* observables**: Phonon-exflation reduces to LCDM in the IR (Standard Model + gravity + dark sector). All tested observables (CMB, BAO, SNe) are consistent but not preferred.

2. **Effective complexity**: Once you add BCS pairing, instanton gas, spectral action, KK radius estimation, you have ~8-12 structural parameters. LCDM has ~6-7. Occam factor penalizes.

3. **Prior volume**: The phonon framework lives in a narrower subspace (must satisfy NCG consistency, spectral action monotonicity, BCS instability threshold, K_7 exact symmetry, etc.). Broader LCDM parameter space "uses" priors more efficiently.

**Path forward**:

- **Paper 20 (DESI DR2)** will test the *one* novel prediction: $w = -1$ exactly (constant dark energy equation of state).
  - If $w = -1 \pm 0.05$ (3-sigma), phonon-exflation gains Occam factor advantage (fewer effective parameters for dark energy).
  - If $w \neq -1$ significantly (e.g., $w_0 = -0.72$, $w_a < 0$ as DESI 2025 hints), Bayes factor strongly favors LCDM. Framework probability drops to <5%.

- **Paper 16 (Gross-Vitells)** quantifies how many trials have been run in framework development (Sessions 1-38). Must account for look-elsewhere effect when assigning significance to post-hoc fits.

---

## File Metadata

**Source**: Contemporary Physics 49:71-104 (2008); arXiv:0803.4089
**Citations**: ~4000+ (highly influential)
**Relevance score**: 10/10 (foundational for framework evaluation)
**Lines**: 185
