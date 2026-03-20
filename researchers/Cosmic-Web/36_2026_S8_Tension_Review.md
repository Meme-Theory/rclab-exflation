# Status of the S8 Tension: A 2026 Review of Probe Discrepancies

**Author(s):** Pantos, A., Perivolaropoulos, L., et al.
**Year:** 2026
**Journal:** arXiv:2602.12238 (under review, A&A submitted)

---

## Abstract

We provide a comprehensive review of the S8 tension—the discrepancy in measurements of the matter density fluctuation amplitude between early-universe (CMB) and late-universe (weak lensing, cluster counts, galaxy clustering) observations. Combining Planck Legacy, ACT DR6, and SPT-3G CMB data, we establish a 2026 baseline S8 = 0.836 +0.012 -0.013 with sub-percent precision. We find **stark divergence** among Stage III weak lensing surveys: KiDS-Legacy shows consistency with CMB (0.73σ discrepancy), while DES Y6 exhibits strong tension (2.4-2.7σ). We investigate systematic sources: photometric redshift calibration, intrinsic alignment modeling, shear measurement pipelines, cluster mass calibration (eROSITA, SPT), galaxy-galaxy lensing, and galaxy-matter cross-correlations. We find that survey-specific systematic effects contribute substantially to the observed discrepancies, though we cannot exclude new physics (modified gravity, massive neutrinos, early dark energy) as alternatives. We forecast that Euclid's first cosmologically relevant results (2026), combined with full-depth Roman Space Telescope observations (2027), will definitively resolve whether S8 tension is instrumental (survey systematics) or fundamental (new physics).

---

## Historical Context

The S8 tension has been one of the most contentious issues in observational cosmology since its emergence circa 2016-2017. The parameter S8 is defined as:

$$S_8 = \sigma_8 \sqrt{\frac{\Omega_m}{0.3}}$$

where $\sigma_8$ is the amplitude of matter density fluctuations (rms density contrast in 8 Mpc/h spheres) and $\Omega_m$ is the matter density parameter. This combination is chosen because it appears naturally in weak gravitational lensing predictions and cluster mass function observations, making it the primary probe of late-time structure growth.

The Planck satellite (2013-2018) measured the CMB anisotropies to extraordinary precision and, combined with local measurements of the Hubble constant, inferred S8 ≈ 0.834. This value is set in the context of the standard ΛCDM model with six parameters. The prediction for S8 is robustly determined by: (i) initial density fluctuations (nearly scale-invariant, as required by inflationary models), (ii) the growth of structure via gravity (dominated by dark matter), and (iii) the balance of matter vs. dark energy densities.

Beginning circa 2017, weak gravitational lensing surveys—which measure S8 directly by observing the bending of light from distant galaxies—began to report values of S8 that were significantly **lower** than Planck. The KiDS (Kilo-Degree Survey) collaboration reported S8 ≈ 0.745, implying a $\sim 2\sigma$ tension with Planck. The Dark Energy Survey (DES) reported values intermediate between KiDS and Planck, but leaning toward lower values.

This discrepancy has persisted and deepened as surveys accumulate more data. The stakes are high: if the tension is real, it implies either (i) systematic errors in the measurements (the most conservative hypothesis), (ii) previously unknown systematics in the CMB analysis, or (iii) physics beyond the standard ΛCDM model (e.g., modified gravity theories, time-varying dark energy, massive neutrinos, early dark energy). Each of these possibilities has profound implications.

The 2026 review by Pantos and Perivolaropoulos is the first comprehensive assessment to utilize the final KiDS-Legacy results (released 2025) and DES Year 6 results (2024-2025). It finds a **critical split**: KiDS has upward-shifted to consistency with Planck, while DES remains discrepant. This split is the most precise measurement-level diagnostic available: if the two surveys agree, they are likely both correct; if they disagree, at least one has significant systematics.

---

## Key Arguments and Derivations

### Weak Lensing Power Spectrum

Weak gravitational lensing measures the bending of light from distant galaxies due to the intervening mass distribution. The observed ellipticity of galaxy images, averaged over many galaxies, reveals the power spectrum of density fluctuations along the line of sight.

The weak lensing power spectrum is related to the matter power spectrum $P(k, z)$ via a line-of-sight integral:

$$P_\kappa(\ell, z_s) = \int_0^{z_s} dz \, \frac{W^2(z, z_s)}{\chi^2(z)} \, P\left(\frac{\ell}{\chi(z)}, z\right)$$

where $\kappa$ is the convergence (fractional magnification), $\ell$ is the spherical multipole, $\chi(z)$ is the comoving distance, $W(z, z_s)$ is the lensing kernel (depends on source redshift $z_s$ and lens redshift $z$), and $P(k, z)$ is the 3D power spectrum.

The matter power spectrum depends sensitively on $\sigma_8$ and $\Omega_m$:

$$P(k, z) = P_\text{lin}(k, z) \, [1 + \text{nonlinear corrections}]$$

where:

$$P_\text{lin}(k, z) = P_\text{lin}(k, z=0) \times D_+(z)^2$$

and $D_+(z)$ is the linear growth factor. Thus, S8 directly sets the amplitude of $P_\text{lin}(k, z)$, making weak lensing a precision probe of S8.

### Systematics: Photometric Redshift Errors

The most significant systematic error in weak lensing surveys is **photometric redshift (photo-z) bias**. Each galaxy's redshift is estimated from broad-band photometry (imaging in multiple filters), not from spectroscopy. The uncertainty is:

$$\Delta z_\text{photo} = \sigma_z (1 + z) \sim 0.02-0.05 \times (1 + z)$$

Errors in the redshift distribution $n(z)$ of the source galaxies directly bias the inferred lensing signal. If sources are closer than assumed, the lensing signal is weaker (less line-of-sight mass); if sources are farther, the signal is stronger. This bias propagates into S8 as:

$$\delta S_8 / S_8 \approx \beta \times (\delta n(z) / n(z))$$

where $\beta$ is a mode-dependent sensitivity factor (typically $0.5-1.5$ depending on scale).

**KiDS-Legacy improvement**: The KiDS collaboration developed improved photo-z calibration using machine learning (K-Fold photometric redshift estimator) and cross-validation with spectroscopic redshifts from 40,000+ galaxies. This reduced photo-z systematic bias from $\sim 0.015$ (KiDS-1000) to $\sim 0.003$ (KiDS-Legacy).

**DES Y6 issue**: DES uses similar photo-z methods but relies more heavily on a single spectroscopic reference sample (COSMOS, ~30,000 galaxies). DES Y6 photo-z systematics are estimated at $\sim 0.008-0.010$, larger than KiDS-Legacy.

### Systematics: Intrinsic Alignment (IA)

Galaxy shapes are not randomly oriented; they tend to align with the local tidal field (density gradients) due to tidal torques during formation. This **intrinsic alignment** can mimic or suppress the weak lensing signal, depending on redshift and scale.

The intrinsic alignment power spectrum is:

$$P_{\text{II}}(k, z) = A_{\text{IA}} \, C_1 \rho_\text{crit} \, \frac{\Omega_m g(z)}{D_+(z)} \left(\frac{k}{k_\text{pivot}}\right)^{\eta_{\text{IA}}} P_\text{lin}(k, z)$$

where $A_{\text{IA}}$ is the IA amplitude (free parameter), $C_1$ is a calibration constant, and $\eta_{\text{IA}}$ is the power-law slope. The IA model is empirically calibrated using simulations and observational data, but remains one of the largest sources of model uncertainty.

**KiDS-Legacy approach**: Uses the "Nonlinear Alignment Model" (NLA) with $A_{\text{IA}}$ and $\eta_{\text{IA}}$ marginalized as nuisance parameters. Joint fitting with other cosmological parameters constrains the IA contamination but increases final error bars by $\sim 10-20\%$.

**DES Y6 approach**: Uses a similar NLA model but additionally fits for redshift-dependent IA ($A_{\text{IA}}(z)$), introducing more nuisance parameters and increasing marginalization uncertainty.

### Systematics: Shear Measurement

The measured ellipticities of galaxies must be corrected for instrumental effects (point-spread function, PSF) and selection biases. The multiplicative shear calibration bias is parameterized as:

$$\gamma_\text{obs} = (1 + m) \gamma_\text{true} + \vec{c}$$

where $m$ is the multiplicative bias and $\vec{c}$ is the additive bias. These must be calibrated using simulations (image simulations with known input shapes and magnifications).

**KiDS-Legacy**: Uses 10 billion GREAT3-like simulated images with realistic PSF, noise, and galaxy morphologies. Multiplicative bias is calibrated to $m \lesssim 0.002$ per tomographic bin, with remaining uncertainty $\approx 0.003$ (calibration uncertainty + sample variance).

**DES Y6**: Uses similar simulation-based calibration but with different image simulation pipeline (GALSIM). Reports $m \approx 0.003-0.005$, with systematic uncertainty $\approx 0.005$.

The impact on S8 is:

$$\delta S_8 / S_8 \approx (1 + m) - 1 = m \sim 0.003-0.005$$

This corresponds to $\delta S_8 \sim 0.002-0.004$, comparable to or larger than the statistical error on S8 from each survey individually.

---

## Key Results

1. **Combined CMB baseline** (Planck + ACT DR6 + SPT-3G): S8 = 0.836 +0.012 -0.013 (0.15% precision). This is the reference "early-universe" value.

2. **KiDS-Legacy weak lensing**: S8 = 0.834 +0.020 -0.021 (2.5% precision). **Discrepancy with CMB**: 0.1σ (complete agreement).

3. **DES Y6 weak lensing**: S8 = 0.768 +0.018 -0.022 (2.4% precision). **Discrepancy with CMB**: 2.6σ (strong tension).

4. **Cluster counts (eROSITA + SPT)**: S8 = 0.795 ± 0.022 (2.8% precision). **Discrepancy with CMB**: 1.4σ (moderate tension). Systematic errors in cluster mass calibration are the likely source.

5. **Galaxy-galaxy lensing** (DES + BOSS): S8 = 0.810 ± 0.025 (3.1% precision). **Discrepancy with CMB**: 0.9σ (agreement).

6. **Redshift-space distortions** (BOSS/eBOSS): S8 = 0.815 ± 0.030 (3.7% precision). **Discrepancy with CMB**: 0.6σ (agreement).

7. **Multi-probe combination** (KiDS-Legacy + BOSS clustering + eROSITA clusters): S8 = 0.820 ± 0.012 (1.5% precision). **Discrepancy with CMB**: 1.2σ (weak tension, likely from cluster mass calibration).

8. **KiDS-Legacy vs. DES Y6 direct comparison**: S8 difference = 0.066 ± 0.027, corresponding to **2.4σ tension**. This is the key result: the two largest Stage III weak lensing surveys disagree significantly.

---

## Systematic Error Attribution

The review systematically investigates each possible source of the KiDS-DES discrepancy:

1. **Photo-z systematatics**: KiDS-Legacy shows sub-0.003 bias; DES Y6 shows 0.008-0.010 bias. Photo-z differences alone can account for $\approx 30-40\%$ of the KiDS-DES discrepancy.

2. **IA model**: Different IA assumptions can shift S8 by $\sim 0.01-0.02$. KiDS uses fixed $\eta_{\text{IA}} = -0.5$; DES uses variable $\eta_{\text{IA}}(z)$. Reconciling these choices reduces discrepancy by $\sim 10\%$.

3. **Shear calibration**: Multiplicative bias differences ($\Delta m \approx 0.002-0.003$) account for $\sim 0.005-0.010$ shift in S8, contributing $\sim 15-20\%$ to discrepancy.

4. **Sample definition**: KiDS uses i-band magnitude limited; DES uses wider r-band selection. Different galaxy populations (morphology, redshift distribution) contribute $\sim 5-10\%$ to discrepancy.

5. **Small-scale modeling**: KiDS uses smaller $k_\text{max} = 1.3 \, h\text{Mpc}^{-1}$; DES uses $k_\text{max} = 0.8 \, h\text{Mpc}^{-1}$ in some measurements. Nonlinear modeling uncertainties contribute $\sim 5-10\%$.

**Conclusion**: $\approx 70\%$ of the KiDS-DES discrepancy can be attributed to identifiable systematic differences. The remaining $\sim 30\%$ is either unidentified systematic error or represents genuine tension (possibly from new physics).

---

## Impact and Legacy

This review closes one chapter and opens another. It establishes that:

1. The S8 tension is **real at the 2-3σ level**, not a statistical fluctuation.

2. The tension is **survey-specific**, not universal—KiDS and lensing-independent probes (galaxy clustering, lensing-independent cluster counts) show agreement with CMB.

3. Systematic errors are **quantifiable and substantial**, but do not fully explain the KiDS-DES split.

4. **New physics remains possible**, but is not demanded by the data.

The review points to three decisive tests:

- **Euclid (2026)**: Independent weak lensing survey with different systematic error budget (space-based, different photo-z methods). If Euclid agrees with KiDS, DES systematics are likely culprit. If Euclid agrees with DES, new physics is more plausible.

- **Roman Space Telescope (2027)**: Ultra-high-resolution imaging will improve photo-z calibration and shear measurement precision by order of magnitude.

- **LSST/Rubin (2025-2032)**: Unprecedented survey depth and area will improve cosmic shear statistics by factor of $\sim 10$, reducing statistical errors to $\lesssim 1\%$ and making systematic errors dominant.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts **w = -1 exactly** and **standard growth of structure** ($\sigma_8, \Omega_m$ evolving as in ΛCDM). This makes the framework **sensitive** to the S8 tension: if true new physics is required to resolve S8 tension, phonon-exflation would fail.

However, the current evidence suggests:

1. **KiDS-Legacy agrees with CMB** → No tension if we weight KiDS heavily. Phonon-exflation prediction **survives**.

2. **DES Y6 shows tension** → If DES is correct, the framework needs modification (e.g., modified gravity affecting structure growth, or early dark energy affecting early-time clustering). Phonon-exflation prediction **challenged**.

3. **Euclid 2026 will be decisive**. If Euclid shows agreement with KiDS+CMB, the DES tension is a DES-specific systematic, and phonon-exflation is safe. If Euclid agrees with DES, the framework faces pressure to explain why $\sigma_8$ is lower than predicted.

The phonon-exflation cosmology does **not** naturally predict a lower $\sigma_8$ (the phononic excitation spectrum does not suppress structure growth). Thus, persistent S8 tension would be a **challenge** to the framework (though not a falsification, as systematics remain the most probable explanation).

