# Dynamical Dark Energy in Light of the DESI DR2 Baryonic Acoustic Oscillations Measurements

**Author(s):** Gan Gu, Xiaoma Wang, Yuting Wang, Gong-Bo Zhao, Levon Pogosian, Kazuya Koyama, John A. Peacock, Zheng Cai, Jorge L. Cervantes-Cota, Mustapha Ishak, Arman Shafieloo, Ruiyang Zhao, et al. (DESI Collaboration)
**Year:** 2025
**Journal:** [not stated in PDF]
**arXiv:** 2504.06118
**Relevance:** HIGH

---

## Abstract

Understanding whether cosmic acceleration arises from a cosmological constant or a dynamical component is a central goal of cosmology, and the Dark Energy Spectroscopic Instrument (DESI) enables stringent tests with high-precision distance measurements. We analyze baryon acoustic oscillation (BAO) measurements from DESI Data Release 1 (DR1) and Data Release 2 (DR2), combined with Type Ia supernovae and a cosmic microwave background (CMB) distance prior. With the larger statistical power and wider redshift coverage of DR2, the preference for dynamical dark energy does not diminish relative to DR1. Using both a shape-function reconstruction and non-parametric approaches with a Horndeski-motivated correlation prior, we find that the dark-energy equation of state $w(z)$ varies with redshift. BAO data alone yield modest constraints, but in combination with independent supernova compilations and the CMB prior they strengthen the evidence for dynamics. Bayesian model comparison shows moderate support for departures from $\Lambda$CDM when multiple degrees of freedom in $w(z)$ are allowed, corresponding to $\approx 3\sigma$ tension with $\Lambda$CDM (and higher for some data sets). Despite methodological differences, our results are consistent with companion DESI papers, underscoring the complementarity of approaches. Possible systematics remain under study; forthcoming DESI, Euclid, and next-generation CMB data will provide decisive tests.

---

## Key Arguments and Derivations

### Section II: Shape-Function Analysis

The shape functions $S_0(a)$, $S_1(a)$, $S_2(a)$ encode the time evolution of the dark energy density, pressure, and equation of state respectively. All five distance probes (DESI DR1, DR2, PantheonPlus, Union3, DESY5) show a consistent, $\Lambda$CDM-deviating trend. DESI DR2 uncovers a stronger dynamical DE signal than DR1: $S_0$ and $S_1$ lie systematically above the $\Lambda$CDM expectation, and $S_2$ exhibits a sharper crossing behavior.

### Section III: Evolution of the Equation of State ($w_0$-$w_a$ parametrization)

Using $w(a) = w_0 + w_a(1-a)$:

**DESI DR1 alone (BAO + BBN + $\theta_*$):** Broadly consistent with $\Lambda$CDM, with mild 1.5--2$\sigma$ hints of departure.

**DESI DR2 alone:** Achieves notably tighter constraints than DR1 and favors $w_0 > -1$ with $w_a < 0$ (Quintom B scenario). $\Lambda$CDM remains viable at $\sim 1.5\sigma$.

**DR2 + supernovae:** Tension with $\Lambda$CDM pushed above 2$\sigma$, showing stronger preference for dynamical dark energy.

The parameter space is divided into four models:
- **Quintessence:** $w > -1$ at all epochs ($w_0 > -1$ and $w_0 + w_a > -1$)
- **Full Phantom:** $w < -1$ at all epochs ($w_0 < -1$ and $w_0 + w_a < -1$)
- **Quintom A:** $w > -1$ in the past but $w < -1$ today ($w_0 < -1$ and $w_0 + w_a > -1$)
- **Quintom B:** $w < -1$ in the past but $w > -1$ today ($w_0 > -1$ and $w_0 + w_a < -1$)

DESI data consistently favor the Quintom B region.

### Section III: Non-parametric Bayesian Reconstruction of $w(z)$

Using a correlation prior derived from Horndeski theory, $w(z)$ is treated as a free function. All dataset combinations exhibit a persistent pattern: $w > -1$ at $z \lesssim 0.2$ and $w < -1$ at $z \sim 0.75$.

**Signal-to-noise ratio for $w \ne -1$:**
- DR1 BAO only: SNR = 2.6
- DR1 + PantheonPlus: SNR = 3.9
- DR1 + Union3: SNR = 3.9
- DR1 + DESY5: SNR = 4.2
- DR2 BAO only: SNR = 2.6
- DR2 + PantheonPlus: SNR = 3.7
- DR2 + Union3: SNR = 4.3
- DR2 + DESY5: SNR = 4.5

The oscillatory/non-monotonic $w(z)$ evolution is consistent across all SN samples and both DR1 and DR2, ruling out dataset-specific artifacts.

### Section IV: Bayesian Evidence

**Principal Component Analysis:** BAO data alone constrain one dominant mode of $w(z)$. Adding SN data produces additional constrained modes; 3 effective degrees of freedom are identified.

**Bayesian evidence ($\Delta\ln E$):**
- BAO alone: consistent with zero for all $N_{\text{eff}}$
- DR2 + DESY5: peak $\Delta\ln E = 5.2 \pm 0.7$ ("Moderate" on Jeffreys' scale) at $N_{\text{eff}} = 3$
- DR2 + Union3: $\Delta\ln E = 3.3 \pm 0.7$ ("Moderate") at $N_{\text{eff}} = 3$
- DR2 + PantheonPlus: $\Delta\ln E = 1.4 \pm 0.7$ ("Weak") -- PantheonPlus shows weakest support

**Maximum SNR (with positive evidence constraint):**
- BAO + DESY5: 4.1 (DR1), 4.3 (DR2)
- BAO + Union3: 3.8 (DR1), 3.9 (DR2)
- BAO + PantheonPlus: 3.2 (DR1), 3.1 (DR2)

### Section V: Summary

Combining DESI BAO, CMB, and the 5-year DES supernova sample detects dark energy evolution at SNR = 3.9, with Bayesian evidence of $5.2 \pm 0.7$ in favor of $w(z)$CDM over $\Lambda$CDM when $N_{\text{eff}} = 3$. The preference for dynamical DE does not diminish from DR1 to DR2.

## Key Results

1. DESI DR2 BAO, with larger statistical power and wider redshift coverage, does not diminish the preference for dynamical dark energy relative to DR1.
2. The $w(z)$ reconstruction shows a persistent pattern: $w > -1$ at $z \lesssim 0.2$ and $w < -1$ at $z \sim 0.75$, across all datasets.
3. All data combinations favor the "Quintom B" scenario: $w$ crossed $-1$ from below (phantom in the past, quintessence-like today).
4. The oscillatory pattern in $w(z)$ is robust across different SN datasets and BAO releases, inconsistent with known systematics.
5. Bayesian evidence reaches "Moderate" support ($\Delta\ln E = 5.2 \pm 0.7$) for dynamical DE with DR2 + DESY5 at 3 effective degrees of freedom.
6. PCA identifies 3 independent modes of $w(z)$ constrained by combined BAO+SN data.
7. The $w_0$-$w_a$ parametrization and non-parametric reconstruction give consistent results.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| CPL parametrization | $w(a) = w_0 + w_a(1-a)$ | Sec. III |
| SNR definition | $\text{SNR}^2 = (\mathbf{w} - \mathbf{w}_{\text{mod}})^T C_w^{-1} (\mathbf{w} - \mathbf{w}_{\text{mod}})$ | Eq. (1) |
| Volume-averaged distance | $D_V = [zD_M^2 D_H]^{1/3}$ | Sec. VI-B |
| Hubble distance | $D_H \equiv c/H(z)$ | Sec. VI-B |
| Shape function $S_0$ | Encodes $\rho_{\text{DE}}(z)/\rho_{\text{DE},0}$ | Sec. II |
| Shape function $S_1$ | Encodes $P_{\text{DE}}(z)$ evolution | Sec. II |
| Shape function $S_2$ (statefinder) | Encodes $w(z)$ and $dw/d\ln a$ | Sec. II |
| Bayesian evidence (peak) | $\Delta\ln E = 5.2 \pm 0.7$ (DR2 + DESY5, $N_{\text{eff}} = 3$) | Sec. IV |
| Max SNR (DR2 + DESY5) | SNR = 4.5 for $w \ne -1$ | Sec. III |

## Relevance to Phonon-Exflation

This paper represents the state-of-the-art observational test for dynamical dark energy as of 2025 and is a direct confrontation for the phonon-exflation framework. The key findings:

1. **Quintom B crossing confirmed at higher significance with DR2:** The framework predicts $w(z)$ evolution arising from the spectral properties of the internal manifold during the tau-transit. The observed crossing pattern ($w < -1$ in the past, $w > -1$ today) must be reproduced quantitatively.

2. **Oscillatory $w(z)$ pattern:** The non-monotonic behavior with $w > -1$ at low $z$ and $w < -1$ at $z \sim 0.75$ is a stronger constraint than the simple $w_0$-$w_a$ parametrization. Axion-like quintessence with periodic potentials and multi-field quintom models are cited as possible explanations -- the phonon-exflation instanton gas may provide an alternative mechanism.

3. **Three effective degrees of freedom:** The PCA result that $w(z)$ has 3 constrained modes implies that any theoretical prediction needs to match at least 3 independent features of the dark energy evolution.

4. **DR2 strengthens DR1:** The signal does not diminish with more data, reducing the probability that it is a statistical fluctuation. This raises the stakes for the framework's FRIEDMANN-BCS-38 channel.

5. **The framework's closed mechanism DESI-dynamical-DE (Session 22d) was premature** -- it was closed because rolling quintessence required a rolling modulus, but the DESI data now show the signal is getting stronger. The instanton/Kibble-Zurek paradigm (Session 37+) may provide the mechanism.
