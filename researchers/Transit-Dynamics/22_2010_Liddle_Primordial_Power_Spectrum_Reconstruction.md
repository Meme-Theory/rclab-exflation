# Measuring the Primordial Power Spectrum

**Author(s):** Andrew R. Liddle, Samuel M. Leach
**Year:** 2003-2010
**Journal:** Monthly Notices of the Royal Astronomical Society, Physical Review D

---

## Abstract

Liddle and Leach developed methods to reconstruct the primordial power spectrum from CMB observations without assuming any particular inflation model. Using principal component analysis, they decomposed the power spectrum into orthonormal modes, allowing model-independent measurements of deviations from pure power law (scale-invariance).

---

## Key Methods

### Principal Component Analysis (PCA)

Define:

P(k) = P_0 [1 + Σ_n a_n f_n(k)]

where f_n are orthonormal eigenmodes determined by the information matrix of CMB observations. The coefficients a_n are measured directly from data.

### Scale-Invariant Baseline

Decompose around Harrison-Zeldovich spectrum (n_s = 1):

P(k) = A [1 + (n_s − 1) ln(k/k_0) + higher terms]

Measure deviations systematically.

---

## Key Results

1. **Model-Independent Reconstruction**: Avoids assuming slow-roll or other assumptions; directly measures spectrum shape.

2. **Deviations from Scale-Invariance**: Any running, oscillations, or features in P(k) detected.

3. **Feature Searches**: Identifies localized deviations (resonances, cuts, discontinuities).

---

## Impact and Legacy

Enabled precision cosmology without inflation model assumptions. Used in Planck 2018 analysis.

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: MEDIUM**

Framework predicts a specific shape: P(k) ~ k^{n_s − 1} with n_s = 0.9561 (exact), no running. Using Liddle's PCA reconstruction:

- Measure a_1 (first PCA coefficient, essentially n_s): should be a_1 ≈ −0.0439 (deviation from scale-invariance)
- Measure a_2, a_3 (higher-order corrections): framework predicts a_2, a_3 << a_1

If Planck data show a_n for n ≥ 2 are all consistent with zero, framework is validated (rigid prediction vs many-parameter slow-roll models).
