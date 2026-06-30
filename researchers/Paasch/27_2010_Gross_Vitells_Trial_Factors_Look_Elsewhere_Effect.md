# Trial factors for the look elsewhere effect in high energy physics

**Author(s):** Eilam Gross, Ofer Vitells
**Year:** 2010
**Journal:** European Physical Journal C
**arXiv:** 1005.1891
**Relevance:** MEDIUM

---

## Abstract

When searching for a new resonance somewhere in a possible mass range, the significance of observing a local excess of events must take into account the probability of observing such an excess anywhere in the range. This is the so called "look elsewhere effect". The effect can be quantified in terms of a trial factor, which is the ratio between the probability of observing the excess at some fixed mass point, to the probability of observing it anywhere in the range. We propose a simple and fast procedure for estimating the trial factor, based on earlier results by Davies. We show that asymptotically, the trial factor grows linearly with the (fixed mass) significance.

---

## Key Arguments and Derivations

### 1. The Look Elsewhere Effect (Section 1)

The paper addresses the statistical problem that arises when searching for a signal (e.g., a mass bump) over a range of possible locations. The test statistic q(m) at a fixed mass m follows a chi-squared distribution with s degrees of freedom (Wilks' theorem). The global test statistic is q(m_hat) = max_m[q(m)], and the problem is assessing the tail probability of this maximum.

A brute-force Monte Carlo approach requires O(10^7) simulations for 5-sigma significance, making it computationally expensive.

### 2. Davies' Bound (Section 2)

The key theoretical result is Davies' bound on the tail probability of the maximum of a chi-squared process:

P(q(theta_hat) > c) <= P(chi^2_s > c) + <N(c)>

where N(c) is the number of upcrossings of level c by the process q(theta), with expectation given by equation (2). The bound becomes an equality for large c.

The authors propose estimating <N(c_0)> at a low reference level c_0 from a small set of background-only Monte Carlo simulations, then extrapolating to higher levels using Davies' formula.

### 3. Trial Factors (Section 2.1)

The trial factor is defined as the ratio of the global p-value to the local p-value:

trial# = P(q(theta_hat) > c) / P(q(theta) > c)

For the common case s = 1:

trial#_{s=1} ≈ 1 + sqrt(pi/2) * N * Z_fix

where N is the effective number of independent search regions and Z_fix is the local significance. The trial factor grows linearly with both N and Z_fix.

### 4. Toy Model Validation (Section 3)

The method is validated using a toy model with a Gaussian signal on a Rayleigh background in a mass range [0, 120], with mass-dependent resolution. Using c_0 = 0.5 and 100 Monte Carlo simulations, <N(c_0)> = 4.34 ± 0.11, giving N = 5.58 ± 0.14. The bound agrees with the observed p-values from ~1 million simulations for large c. Cases with s = 2, 3 degrees of freedom are also validated.

## Key Results

1. The trial factor grows asymptotically linearly with the local significance Z_fix and with the effective number of independent search regions N.
2. The method requires only ~100 Monte Carlo simulations at a low reference level, rather than O(10^7) for direct estimation.
3. The effective number of independent regions N has a natural interpretation: the search range is composed of N independent regions, each with one extra degree of freedom from the mass fit.
4. For s = 1 (most common case): trial# ≈ 1 + sqrt(pi/2) * N * Z_fix.
5. The optimal reference level is c_0 = s - 1 (or as low as numerically feasible for s = 1).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Davies bound | $P(q(\hat\theta) > c) \leq P(\chi^2_s > c) + \langle N(c) \rangle$ | Eq. (1) |
| Upcrossings | $\langle N(c) \rangle = \frac{c^{(s-1)/2} e^{-c/2}}{\sqrt{\pi} 2^{s/2} \Gamma(s/2 + 1/2)} \int_L^U C(\theta) d\theta$ | Eq. (2) |
| Practical bound | $P(q(\hat\theta) > c) \leq P(\chi^2_s > c) + \langle N(c_0) \rangle \left(\frac{c}{c_0}\right)^{(s-1)/2} e^{-(c-c_0)/2}$ | Eq. (3) |
| Asymptotic form | $P(q(\hat\theta) > c) \approx P(\chi^2_s > c) + N \cdot P(\chi^2_{s+1} > c)$ | Eq. (5) |
| Trial factor (s=1) | $\text{trial\#}_{s=1} \approx 1 + \sqrt{\pi/2}\, N\, Z_{\text{fix}}$ | Eq. (12) |

## Relevance to Phonon-Exflation

The look-elsewhere effect is directly relevant to assessing the statistical significance of the phi_paasch mass ratio (1.531580). Any claimed coincidence between a computed spectral ratio and an observed mass ratio must account for the number of tau values, sector pairs, and eigenvalue pairs scanned. The trial factor formalism provides the rigorous framework for converting a local p-value (at a specific tau) to a global p-value across the full search space, preventing false significance claims.
