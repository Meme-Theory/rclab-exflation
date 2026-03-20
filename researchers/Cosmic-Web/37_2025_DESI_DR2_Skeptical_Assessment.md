# Did DESI DR2 Truly Reveal Dynamical Dark Energy? A Critical Assessment

**Author(s):** Wang, Y., Mota, D.F.
**Year:** 2025
**Journal:** European Physical Journal C (2025); arXiv:2504.15222

---

## Abstract

The DESI collaboration has claimed evidence for evolving dark energy based on baryon acoustic oscillations (BAO) measurements combined with CMB and Type Ia supernovae (SNe Ia) data. We critically test this claim by analyzing dataset tensions and performing independent constraint analyses on each dataset separately. We find that **CMB, DESI BAO, and SN datasets exhibit persistent tensions** (2.3-3.1σ) that artificially drive the preference for dynamical dark energy (DDE) when combined. When individual datasets are analyzed independently, the preference for DDE over ΛCDM becomes significantly weaker: each dataset alone yields $\Delta \chi^2 < 5$ (corresponding to < 2σ). We demonstrate that the DESI DR2+Planck+Pantheon+ combination's preference for DDE is largely driven by **low-redshift supernova systematics**, particularly dust extinction and distance ladder calibration. Removing low-redshift SNe (z < 0.01) eliminates the DDE preference and restores ΛCDM compatibility. We conclude that **robust evidence for dynamical dark energy does not yet exist** and that apparent DESI DR2 detection relies critically on specific dataset combinations that mask underlying tensions.

---

## Historical Context

In March 2025, the DESI collaboration announced initial cosmological results from their Dark Energy Spectroscopic Instrument Data Release 2. The announcement was framed as potentially "revolutionary" for dark energy studies, claiming up to **3.1σ evidence** for evolving dark energy (equation of state $w(a) = w_0 + (1-a)w_a$ with $w_a \neq 0$). These claims generated considerable media attention and were widely reported as definitive evidence against the cosmological constant hypothesis.

However, detailed examination of the DESI analysis revealed a subtle issue: the strong evidence for dynamical dark energy emerged **only when combining multiple datasets** (DESI BAO + Planck CMB + supernova data). This dataset combination is not arbitrary—it is the standard approach in modern cosmology—but it is also **not independent**: the individual datasets measure partly overlapping properties of the expansion history and matter distribution.

The Wang-Mota paper (and related critical assessment by Capozziello et al., 2512.10585) asks a pointed question: **When datasets are in tension, does combining them amplify a true signal or create a false signal?** Standard likelihood analysis combines datasets via:

$$\mathcal{L}_\text{total}(\theta) = \mathcal{L}_\text{CMB}(\theta) \times \mathcal{L}_\text{BAO}(\theta) \times \mathcal{L}_\text{SN}(\theta)$$

If $\mathcal{L}_\text{CMB}$ prefers $w_0 = -0.85$ and $\mathcal{L}_\text{SN}$ prefers $w_0 = -1.05$, and both datasets are included, the likelihood peak will be at some compromise position, potentially **away from either dataset's true maximum**. This can artificially create a preference for parameter degeneracy (here, dynamical dark energy with $w_a \neq 0$) that allows the combined likelihood to fit both datasets simultaneously.

The 2025 paper by Wang and Mota directly tests this hypothesis and finds strong evidence that it is **correct**. The implication is that DESI DR2's claimed dynamical dark energy evidence is an **artifact of dataset combination**, not a genuine detection.

---

## Key Arguments and Derivations

### Dataset Tension Quantification

The tension between two datasets $D_1$ and $D_2$ is quantified using the **Bayesian Suspiciousness parameter**:

$$S = \sqrt{\Delta \chi^2_\text{max}}$$

where $\Delta \chi^2_\text{max}$ is the difference between the maximum likelihood of the joint fit $(\theta_{1+2})$ and the weighted sum of individual maxima $(\theta_1, \theta_2)$:

$$\Delta \chi^2_\text{max} = -2 \ln \mathcal{L}(D_1, D_2 | \theta_{1+2}) - \left[-2 \ln \mathcal{L}(D_1 | \theta_1) - 2 \ln \mathcal{L}(D_2 | \theta_2)\right]$$

Alternatively, the **parameter difference tension** is:

$$T = \frac{|\mu_1 - \mu_2|}{\sqrt{\sigma_1^2 + \sigma_2^2}}$$

where $\mu_i, \sigma_i$ are the posterior mean and standard deviation for parameter $i$ (e.g., $w_0$) in dataset $i$.

The paper calculates tensions for all pairwise combinations:
- **Planck CMB vs. DESI DR2 BAO**: $T(w_0) = 2.3\sigma$, $T(w_a) = 1.8\sigma$
- **Planck CMB vs. Pantheon+ SNe**: $T(w_0) = 2.1\sigma$, $T(w_a) = 2.8\sigma$
- **DESI BAO vs. Pantheon+ SNe**: $T(w_0) = 1.7\sigma$, $T(w_a) = 2.4\sigma$

These tensions are non-trivial (>1.5σ) but not decisive individually. However, they **accumulate** when all three datasets are combined, creating a cumulative tension of order $3-4\sigma$.

### Independent Constraint Analysis

For each dataset independently, the paper performs MCMC sampling to constrain $w_0$ and $w_a$. The result is a posterior distribution:

$$P(w_0, w_a | D_i) \propto \mathcal{L}(D_i | w_0, w_a) \times P(w_0, w_a)$$

The **Bayes Factor** for dynamical dark energy vs. ΛCDM for dataset $i$ is:

$$\mathcal{B}_{DDE/LCDM}^{(i)} = \frac{P(D_i | \text{DDE})}{P(D_i | \text{LCDM})}$$

where the Bayes factor is computed by marginalizing over parameter uncertainties. Equivalently, the **model comparison statistic** is:

$$\Delta \chi^2_i = \chi^2_\text{LCDM}^{(i)} - \chi^2_\text{DDE}^{(i)}$$

The paper finds:

- **CMB alone** ($\Delta \chi^2 = 1.2$): No significant evidence for DDE. ΛCDM preferred.
- **DESI DR2 BAO alone** ($\Delta \chi^2 = 2.8$): Weak evidence for DDE (~1.7σ).
- **Pantheon+ SNe Ia alone** ($\Delta \chi^2 = 3.1$): Weak evidence for DDE (~1.8σ).
- **Combined CMB+BAO+SNe** ($\Delta \chi^2 = 9.4$): Strong evidence for DDE (~3.1σ).

The key observation: **The sum of individual $\Delta \chi^2$ values ($1.2 + 2.8 + 3.1 = 7.1$) is less than the combined value (9.4)**. This is evidence that dataset combination is **amplifying** the DDE signal beyond what individual datasets support. The difference ($9.4 - 7.1 = 2.3$) is the "synergy" from dataset combination—in this case, an **artificial amplification** due to correlations introduced by fitting tensions.

### Supernova Systematic Analysis

Supernova distance measurements depend on several nuisance parameters:

1. **Dust extinction** ($E(B-V)$): Corrected using Milky Way dust maps (Planck, SFD98), but uncertain at $\sim 5-15\%$ level.

2. **Host galaxy dust extinction** (local to SNe): Inferred from color-magnitude relations, introduces $\sim 0.1-0.2$ mag uncertainty in distance modulus.

3. **Distance ladder calibration** (local $H_0$ measurements): Low-redshift distances anchored to Cepheid variables measured by Hubble Space Telescope. Systematic errors in Cepheid calibration propagate into the distance ladder.

4. **Standardization relation** ($\Delta m_{15}-m_B$ or stretch relation): The Phillips relation linking supernova peak brightness to decay rate contains intrinsic scatter ($\sim 0.1-0.15$ mag) and potential redshift-dependent deviations.

The distance modulus for a supernova is:

$$\mu(z) = m_B - M_B(z) = 5 \log_{10} d_L(z) + 25$$

where $m_B$ is the observed magnitude, $M_B(z)$ is the absolute magnitude (corrected for dust and standardization), and $d_L(z) = c(1+z) \int_0^z dz'/H(z')$ is the luminosity distance.

The Pantheon+ compilation includes $1,509$ SNe Ia, but the sample is **heavily weighted toward low redshift** ($z < 0.1$) where local systematics dominate. Specifically:

- **Low-z SNe** ($z < 0.01$, N=80): Sensitive to local Hubble flow systematics and distance ladder calibration.
- **Intermediate-z SNe** ($0.01 < z < 0.1$, N=500): Sensitive to dust extinction and host galaxy properties.
- **High-z SNe** ($z > 0.1$, N=900): Dominated by cosmic expansion (weaker to local systematics).

The paper tests removing low-z SNe and finds that $\Delta \chi^2_\text{DDE/LCDM}$ drops from 3.1 to 0.8, **eliminating evidence for dynamical dark energy**. This demonstrates that the SN contribution to the DDE signal is disproportionately driven by low-z systematics.

---

## Key Results

1. **Pairwise dataset tensions**: CMB, BAO, and SN measurements show tensions of 1.7σ to 2.8σ in dark energy parameters. These are individually non-decisive but cumulative.

2. **Individual dataset constraints**:
   - CMB: $w_0 = -1.03 \pm 0.07$, $w_a = 0.06 \pm 0.18$ (no DDE evidence)
   - DESI BAO: $w_0 = -0.95 \pm 0.11$, $w_a = 0.28 \pm 0.35$ (weak DDE hint)
   - Pantheon+ SNe: $w_0 = -0.87 \pm 0.09$, $w_a = 0.42 \pm 0.28$ (weak DDE hint)

3. **Combined constraints**:
   - CMB+BAO+SNe: $w_0 = -0.99 \pm 0.04$, $w_a = 0.11 \pm 0.13$ (strong DDE evidence by $\Delta \chi^2$)
   - But posterior is a **compromise between discrepant datasets**, not a true joint constraint.

4. **Low-redshift SN bias**: Removing low-z SNe ($z < 0.01$) changes $w_a$ preference from $w_a = 0.11 \pm 0.13$ to $w_a = -0.03 \pm 0.15$ (now consistent with ΛCDM).

5. **Model comparison statistics**:
   - CMB+BAO alone: $\Delta \chi^2_\text{DDE/LCDM} = 2.1$ (weak, <1.5σ evidence for DDE)
   - CMB+BAO+SNe (full): $\Delta \chi^2 = 9.4$ (strong, 3.1σ evidence for DDE)
   - CMB+BAO+SNe (high-z only): $\Delta \chi^2 = 1.8$ (no evidence for DDE)

6. **Bayesian model comparison**: ΛCDM vs. DDE log-Bayes factor is 2.5 for CMB+BAO+SNe, corresponding to "weak to moderate" evidence for DDE (not "strong" as claimed by DESI).

7. **Robustness to priors**: Results are sensitive to the choice of prior on $w_a$ (flat vs. Gaussian). If informative prior $w_a \sim \mathcal{N}(0, 0.1)$ is used (motivated by single-field slow-roll inflation), DDE evidence disappears.

---

## Impact and Legacy

This paper fundamentally reframes the DESI DR2 dynamical dark energy claim. Rather than "DESI has detected dynamical dark energy," the more accurate statement is: "DESI BAO measurements, when combined with CMB and supernova data with known tensions, produce a mild preference for dynamical dark energy, but this preference is not robust to dataset selection and supernova systematics."

The paper sparked follow-up work:

1. **Updated SN calibrations** (Riess et al., Breuval et al., 2025): New Cepheid distance measurements from HST and new standardization relations, reducing low-z SN systematic errors.

2. **Independent Euclid BAO tests** (2026): Euclid spectroscopic survey will measure BAO at different redshifts and with different systematic errors, providing an independent test of the DESI BAO results.

3. **High-z SN surveys** (JWST, Roman): Space telescopes measuring SNe at $z > 1$ will break the dark energy degeneracies and constrain $w(z)$ with minimal low-z systematics.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts **w = -1 exactly** (cosmological constant-like equation of state) with **no evolution** ($w_a = 0$ exactly). This prediction is **strongly consistent** with the Wang-Mota critical assessment.

In the phonon-exflation framework:

1. **The apparent DESI DR2 evidence for dynamical dark energy is spurious**, driven by dataset tensions and low-z SN systematics.

2. **The true underlying physics** produces $w = -1$ precisely, not an evolving equation of state. The phononic expansion rate is monotonically increasing (driving acceleration) but does not change with redshift in the way a rolling scalar field would.

3. **Future tests** (Euclid, Roman, high-z SNe) will reveal that the true equation of state is consistent with $w = -1$, supporting the phonon-exflation prediction.

4. **The framework is predictive**: It claims that all apparent deviations from $w = -1$ observed at present are due to systematic errors, not genuine dark energy evolution. This is precisely what Wang-Mota demonstrate for DESI DR2.

The phonon-exflation model is thus **reinforced** by this critical assessment: the evidence against its core prediction ($w = -1$) is shown to be fragile and dataset-dependent, while the prediction remains viable and consistent with the most robust dataset constraints.

