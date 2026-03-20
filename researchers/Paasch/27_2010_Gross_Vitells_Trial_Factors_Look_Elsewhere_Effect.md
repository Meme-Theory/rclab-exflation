# Trial Factors for the Look-Elsewhere Effect in High Energy Physics

**Author(s):** Eilam Gross, Ofer Vitells
**Year:** 2010
**Journal:** European Physical Journal C, 70:525
**arXiv:** 1005.1891
**DOI:** 10.1140/epjc/s10052-010-1470-8

---

## Abstract

When searching for a new resonance across a mass range, the observed local significance of a peak at any single mass point must be corrected for the probability of finding such a peak *anywhere* in the range due to statistical fluctuation. This correction is quantified by the trial factor (also called the look-elsewhere effect). The authors propose a practical and fast procedure for estimating trial factors based on asymptotic results by Davies (1987). The key result is that the trial factor grows linearly with the significance at fixed mass points, allowing physicists to rapidly adjust statistical significance thresholds in resonance searches without expensive Monte Carlo simulations.

---

## Historical Context

The look-elsewhere effect (LEE) is a fundamental correction in particle physics experiments. When the LEE is ignored, the reported significance of new discoveries inflates dramatically. A classic example: if searching for a resonance across 100 different mass points, each at the 2σ level (p-value ~0.05), the probability of finding *at least one* such excess by chance alone is not 0.05 but approximately 1 - (0.95)^100 ≈ 99.4%.

Before Gross and Vitells (2010), LEE corrections were either:

1. **Bonferroni correction**: Most conservative; multiply p-value by number of tests. Often too harsh, especially for correlated tests.
2. **Monte Carlo**: Simulate background-only hypothesis millions of times, observe maximum test statistic across the range. Computationally expensive, difficult to reproduce.
3. **Ad hoc scaling**: Rough engineering estimates used by experimental teams, often inconsistent.

Gross and Vitells provided a theoretically justified, analytically simple procedure that became the standard for LEE corrections in high-energy physics. It is now universally applied in discovery announcements (e.g., Higgs boson searches, resonance hunts at the LHC).

---

## Key Arguments and Derivations

### The Statistical Problem

Let $X(m)$ be a test statistic (e.g., signal strength parameter μ, or log-likelihood ratio) evaluated at resonance mass m. Define the **local significance** at fixed mass m₀:

$$Z(m_0) = \Phi^{-1}(1 - p(m_0))$$

where Φ is the standard normal CDF and p(m₀) is the p-value at mass m₀.

For a Gaussian test statistic centered at null hypothesis ($X(m) \sim N(0, 1)$ under H₀):
$$Z(m_0) = X(m_0)$$

(e.g., Z = 5 means p = 2.87 × 10^{-7}, or 5σ).

The problem: if we *scan* across the range [m_min, m_max] and report the maximum local significance found, we must account for the global significance:

$$Z_{\text{global}} = \text{quantile of} \max_{m \in [m_\text{min}, m_\text{max}]} X(m)$$

### Davies' Result (1987)

Davies proved that for a one-dimensional scan of a smooth test statistic with weak autocorrelation:

$$\text{Pr}[\max_m X(m) > z] \approx N_{\text{eff}} \Phi(-z)$$

where:
- $N_{\text{eff}}$ = effective number of independent degrees of freedom (depends on scan resolution and correlation length)
- $\Phi(-z)$ = standard normal tail probability

For z ≥ 3, this gives:
$$\text{Pr}[\text{max}_m X(m) > z] \approx N_{\text{eff}} \cdot z \phi(z)$$

where $\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$.

### Gross-Vitells Simplified Form

Gross and Vitells reorganize Davies' result into a **trial factor** F:

$$F(z) = \frac{p_{\text{local}}}{p_{\text{global}}} = \frac{\text{Pr}[X(m_0) > z]}{\text{Pr}[\max_m X(m) > z]} \approx \frac{1}{N_{\text{eff}} \cdot z}$$

So:
$$Z_{\text{global}} = \Phi^{-1}(1 - p_{\text{local}} \cdot F)$$

**Example**: If a local significance is Z_local = 5 (p_local ≈ 2.87 × 10^{-7}), scanning 50 independent mass points:
- Trial factor: $F = \frac{1}{50 \times 5} = 0.004$
- Global p-value: $p_{\text{global}} = 2.87 \times 10^{-7} / 0.004 ≈ 7.2 \times 10^{-5}$
- Global significance: $Z_{\text{global}} ≈ 3.8σ$

The 5σ local excess drops to 3.8σ global—still significant, but far weaker. This is why the 2012 Higgs discovery claimed 5σ *local* but reported conservative global significance accounting for LEE.

### Effective Number of Degrees of Freedom

$N_{\text{eff}}$ depends on the correlation structure of the test statistic across the range:

$$N_{\text{eff}} = 1 + 2 \int_0^{\infty} \rho(\delta m) d(\delta m)$$

where $\rho(\delta m)$ is the autocorrelation function. For:
- Independent tests: $N_{\text{eff}}$ = number of tests
- Fully correlated tests: $N_{\text{eff}} = 1$ (no penalty)
- Typical physics searches: $N_{\text{eff}}$ ≈ 0.5 to 2 times the naive count, accounting for mass resolution and signal width

---

## Key Results

1. **Analytic Trial Factor Formula**: $F(z) \approx 1 / (N_{\text{eff}} \times z)$ enables rapid, reproducible LEE corrections without Monte Carlo.

2. **Linear Growth with Significance**: Trial factor grows linearly in z (significance), unlike Bonferroni (which is independent of z). High-significance local peaks receive less penalty, reflecting their lower probability of being fluctuations.

3. **Fast Computation**: Replacing Monte Carlo simulations with an analytic formula reduced computational time from hours to microseconds per scan.

4. **Experimental Standard**: The method was adopted by ATLAS, CMS, and LHCb for all resonance searches, discovery claims, and limits.

5. **No Model Dependence**: The formula depends only on test statistic properties and the effective scan volume, not on physics model assumptions (background shape, signal model, etc.).

---

## Impact and Legacy

This paper became the methodological backbone of post-2010 particle physics discovery claims. Major applications:

- **Higgs Boson (2012)**: ATLAS and CMS reported local 5σ significance; Gross-Vitells global corrections placed it at ~5σ globally, below the 5σ threshold but above 4σ, validating the discovery.
- **Exotic Resonance Searches**: Any search for Z', W', new Higgs bosons, etc., cites this paper and applies the correction.
- **B Physics**: Belle II and LHCb measure rare decay rates using identical LEE corrections.

The paper is cited >1000 times and appears in nearly every particle physics result announced since 2010. It is taught in graduate particle physics courses as the standard statistical technique.

---

## Connection to Phonon-Exflation Framework

**Direct connection: CRITICAL for Paasch validation**

The framework's hypothesis of mass quantization (Paasch's m-numbers) must be tested against the null hypothesis of continuous mass variation. Any discrepancy between predicted masses and measured masses must account for the look-elsewhere effect:

### Problem Setup

Paasch predicts specific mass values: m_e = 0.510998..., m_μ = 105.658..., m_τ = 1776.858..., etc., derived from a discrete formula involving s (the spectral action parameter).

Experimental measurements have finite precision (PDG 2024: m_τ = 1776.86 ± 0.12 MeV).

**Naive significance**: If predicted m_τ = 1776.858 and measured m_τ = 1776.86 ± 0.12, the agreement is within 0.002σ, trivially consistent.

But the framework makes predictions for *all* particles simultaneously. The question is: **how likely is agreement across all N particles by chance?**

### Applying Gross-Vitells

Define test statistic:
$$X = \sum_i \left| \frac{m_i^{\text{predicted}} - m_i^{\text{measured}}}{\sigma_i} \right|$$

where the sum spans N = 14 particles (e, μ, τ, u, d, s, c, b, W, Z, Higgs, and 3 neutrino mass differences).

If masses were *random*, this sum would follow a chi-squared distribution with N degrees of freedom. The Gross-Vitells correction accounts for having scanned the parameter space (s, τ, other KK parameters) to find the s value that *minimizes* X.

**Without LEE correction**: Predicted mass values match measured values. Significance appears high.

**With LEE correction**: After scanning the parameter space over ranges determined by KK reduction and BCS instability, the trial factor penalizes the claimed agreement.

$$F_{\text{trial}} = \frac{p_{\text{local}}}{p_{\text{global}}} = \frac{1}{N_{\text{eff}} \times Z_{\text{local}}}$$

If N_eff ≈ 50 (parameter space volume) and Z_local = 3σ, then F ≈ 0.0067, reducing global significance dramatically.

### Recommendation

**Session 43+**: When claiming mass predictions from the framework agree with experiment, *compute* the global significance after Gross-Vitells correction. If global significance drops below 2σ, the framework's mass predictions are not yet experimentally validated.

---

## References

- Gross, E., Vitells, O. (2010). "Trial factors for the look elsewhere effect in high energy physics." European Physical Journal C 70, 525.
- Davies, R.B. (1987). "Hypothesis testing when a nuisance parameter is present only under the alternative." Biometrika 74(1), 33-43.
- ATLAS Collaboration. (2012). "Observation of a new particle in the search for the Standard Model Higgs boson with the ATLAS detector at the LHC." Physics Letters B 716, 1-29.
- CMS Collaboration. (2012). "Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC." Physics Letters B 716, 30-61.

---

## Appendix: Effective Degrees of Freedom Estimates

For typical particle physics mass scans:

| Scan Type | N_tests | Correlation | N_eff |
|:----------|:--------|:------------|:------|
| Higgs mass range (100-150 GeV, 0.1 GeV bins) | 500 | weak | ~5-10 |
| Resonance bump hunt across full spectrum (10-1000 GeV) | 1000+ | weak | ~20-50 |
| Parameter space scan (s in [0, 0.5], Δs = 0.01) | 50 | moderate | 5-15 |
| Precision mass measurement (m ± 0.01 MeV, 1000 points) | 1000 | strong | ~50-100 |

The phonon-exflation parameter space (s, τ, KK radius, BCS coupling) has ~4-8 free parameters with natural ranges and resolutions, implying N_eff ≈ 30-100 depending on which parameters are scanned for mass predictions.
