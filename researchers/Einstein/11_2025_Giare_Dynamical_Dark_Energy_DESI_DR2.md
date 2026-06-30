# Dynamical Dark Energy in Light of the DESI DR2 Baryonic Acoustic Oscillations Measurements

**Author(s):** Gan Gu, Xiaoma Wang, Yuting Wang, Gong-Bo Zhao, Levon Pogosian, Kazuya Koyama, John A. Peacock, Zheng Cai, Jorge L. Cervantes-Cota, Mustapha Ishak, Arman Shafieloo, Ruiyang Zhao, et al.
**Year:** 2025
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2504.06118
**Relevance:** CRITICAL

---

## Abstract

Understanding whether cosmic acceleration arises from a cosmological constant or a dynamical component is a central goal of cosmology, and the Dark Energy Spectroscopic Instrument (DESI) enables stringent tests with high-precision distance measurements. We analyze baryon acoustic oscillation (BAO) measurements from DESI Data Release 1 (DR1) and Data Release 2 (DR2), combined with Type Ia supernovae and a cosmic microwave background (CMB) distance prior. With the larger statistical power and wider redshift coverage of DR2, the preference for dynamical dark energy does not diminish relative to DR1. Using both a shape-function reconstruction and non-parametric approaches with a Horndeski-motivated correlation prior, we find that the dark-energy equation of state w(z) varies with redshift. BAO data alone yield modest constraints, but in combination with independent supernova compilations and the CMB prior they strengthen the evidence for dynamics. Bayesian model comparison shows moderate support for departures from LCDM when multiple degrees of freedom in w(z) are allowed, corresponding to approximately 3 sigma tension with LCDM (and higher for some data sets). Despite methodological differences, our results are consistent with companion DESI papers, underscoring the complementarity of approaches. Possible systematics remain under study; forthcoming DESI, Euclid, and next-generation CMB data will provide decisive tests.

---

## Key Arguments and Derivations

### Section II: Shape-Function Analysis

The paper introduces three dimensionless shape functions S_0(a), S_1(a), S_2(a) that diagnose dark energy evolution without assuming an equation of state parametrization. S_0 captures the DE energy density evolution, S_1 captures the DE pressure evolution, and S_2(a) = -S''(a)/(3S'(a)) = w(a) - w'(a)/(3w(a)) encodes both w and its derivative (the "statefinder parameter"). All three shape functions show systematic deviation from LCDM in both DR1 and DR2, with the DESI DR2 signal being stronger. S_2 exhibits a characteristic crossing behavior.

### Section III: CPL Parametrization Results

Using w(a) = w_0 + w_a(1-a), the parameter space is divided into four regions: Quintessence (w > -1 at all epochs), Full Phantom (w < -1 at all epochs), Quintom A (w > -1 in past, w < -1 today), and Quintom B (w < -1 in past, w > -1 today). The data favor the Quintom B quadrant (w_0 > -1, w_a < 0).

Key constraints (DR2 + CMB + SNe):
- DR2 + PantheonPlus: mild (~2 sigma) preference for dynamical DE
- DR2 + Union3: ~3 sigma preference
- DR2 + DESY5: strongest preference (~3.5 sigma)

### Section III-IV: Non-parametric Bayesian Reconstruction

Using a correlation prior derived from Horndeski gravity theory, w(z) is reconstructed non-parametrically in 29 piecewise-constant bins. The reconstructed w(z) shows a persistent pattern: w > -1 at z < 0.2 and w < -1 at z ~ 0.75, with pronounced oscillatory features. This pattern is stable across all SNe datasets and both DR1 and DR2.

The significance of w != -1, defined via SNR^2 = (w - w_mod)^T C_w^{-1} (w - w_mod), reaches:
- DR2 alone: 2.6 sigma
- DR2 + PantheonPlus: 3.7 sigma
- DR2 + Union3: 4.3 sigma
- DR2 + DESY5: 4.5 sigma

### Section IV: Bayesian Evidence

Principal Component Analysis identifies ~3 effective degrees of freedom in w(z) constrained by the data without overfitting. Bayesian evidence (ln E):
- DR2 + DESY5: Delta ln E = 5.2 +/- 0.7 ("Moderate" on Jeffreys' scale) at N_eff = 3
- DR2 + Union3: Delta ln E = 3.3 +/- 0.7 ("Moderate")
- DR2 + PantheonPlus: Delta ln E = 1.4 +/- 0.7 ("Weak")

The maximum SNR for w != -1 with positive evidence (Delta ln E >= 0):
- DR2 + DESY5: 4.3 sigma
- DR2 + Union3: 3.9 sigma
- DR2 + PantheonPlus: 3.1 sigma

## Key Results

1. DESI DR2 strengthens the dynamical DE signal relative to DR1; the preference does not diminish with more data.
2. The reconstructed w(z) shows w > -1 at z < 0.2 and w < -1 at z ~ 0.75, with oscillatory features stable across datasets.
3. Bayesian evidence reaches "Moderate" support (ln E ~ 5.2) for w(z)CDM over LCDM when combining DR2 + CMB + DESY5.
4. Three independent SNe datasets (PantheonPlus, Union3, DESY5) all show consistent deviations from LCDM.
5. ~3 effective degrees of freedom in w(z) are constrained by the data, favoring a richer dark energy structure than simple CPL.
6. The oscillatory pattern in w(z) cannot be produced by known systematics (photometric offsets, BAO template shifts) which vary smoothly with redshift.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| SNR definition | ${\rm SNR}^2 = (\mathbf{w} - \mathbf{w}_{\rm mod})^T C_w^{-1} (\mathbf{w} - \mathbf{w}_{\rm mod})$ | Eq. 1 |
| Distance parametrization | $D_M(z)/D_M^f(z)\mathcal{R} = \alpha_0(1 + \alpha_1 x + \alpha_2 x^2 + \alpha_3 x^3 + ...)$ | Eq. 2 |
| Shape function S_0 | $S_0(a) \equiv \frac{a^3 + X(a)a^3 - 1}{w(1)} \xrightarrow{\Lambda} 1$ | Eq. 5 |
| Shape function S_1 | $S_1(a) \equiv \frac{P_{DE}(a)}{P_{DE}(1)} \xrightarrow{\Lambda} 1$ | Eq. 5 |
| Shape function S_2 | $S_2(a) \equiv -\frac{S''(a)}{3S'(a)} = w(a) - \frac{w'(a)}{3w(a)} \xrightarrow{\Lambda} -1$ | Eq. 5 |
| Horndeski correlation prior | $C(a) = 0.05 + 0.8a^2,\quad R(a,a') = \exp\left[-(|\ln a - \ln a'|/0.3)^{1.2}\right]$ | Eq. 7 |
| Total chi-squared | $\chi^2 = \chi^2_{\rm data} + A\chi^2_{\rm prior}$ | Eq. 8 |
| CPL parametrization | $w(a) = w_0 + w_a(1-a)$ | Sec. III |

## Relevance to Phonon-Exflation

This paper is the second primary falsification gate for the framework, providing multi-probe evidence at 2.8-4.5 sigma for w != -1. The oscillatory w(z) pattern -- with w crossing -1 at intermediate redshifts -- poses a specific challenge. The framework predicts w = -1 + O(10^{-29}), which is indistinguishable from LCDM. The Quintom B behavior (w crossing -1 from phantom to quintessence) is particularly relevant because single-field models cannot produce such crossing without violating the null energy condition. The S59 user insight connecting tau(x) to local matter density (generating Wiltshire-type clock variance and apparent w_a from a static framework) provides a potential resolution: the observed w(z) variation may be an apparent effect of inhomogeneous clocking rather than genuine dark energy dynamics. The Bayes factor of 12:1 to 45:1 favoring dynamical DE (depending on dataset) sets a quantitative threshold the framework must address.
