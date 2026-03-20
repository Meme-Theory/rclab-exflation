# KiDS-Legacy: Cosmological Constraints from Cosmic Shear

**Author(s):** Wright, A. H.; Stolzner, B.; Reischke, R.; Asgari, M.; Kuijken, K.; et al. (KiDS Collaboration)
**Year:** 2025
**Journal:** Astronomy & Astrophysics (submitted), arXiv:2503.19441

---

## Abstract

We present final cosmological constraints from the **Kilo-Degree Survey (KiDS) Complete Data Release**, analyzing cosmic shear correlation functions from 1,347 square degrees of deep nine-band imaging. Our analysis extends the photo-z sample to z_B ≤ 2.0, approximately doubling the effective constraining power of previous KiDS releases. We employ physically motivated models for intrinsic alignments (scaling with halo mass and galaxy type) and marginalize over baryon feedback uncertainties in non-linear matter power spectra. Our primary result is:

$$S_8 = \sigma_8 \sqrt{\Omega_m / 0.3} = 0.815_{-0.021}^{+0.016}$$

This represents **agreement (0.73 sigma) with Planck Legacy CMB constraints** (S_8 = 0.834 +/- 0.016), resolving the reported S_8 tension that motivated numerous beyond-ΛCDM proposals. Systematic uncertainties in photometric redshift estimation, shear calibration, and intrinsic alignment model form the dominant error budget. We discuss implications for modified gravity, massive neutrino scenarios, and the concordance model, concluding that existing tensions in the low-redshift Universe are best explained by unaccounted systematic uncertainties rather than deviations from ΛCDM.

---

## Historical Context

For nearly a decade (2015-2025), multiple weak lensing surveys reported anomalously **low** values of S_8 compared to Planck:
- **Planck CMB**: S_8 = 0.834 ± 0.016
- **KiDS-450** (2017): S_8 = 0.745 ± 0.039 (2.3 sigma below Planck)
- **DES Year 1** (2017): S_8 = 0.783 ± 0.021 (1.8 sigma below Planck)
- **HST/ACS** (2019): S_8 = 0.73 ± 0.05 (1.6 sigma below Planck)

This **S_8 tension** (a ~2-3 sigma discrepancy) became a major anomaly in precision cosmology. It spawned numerous theoretical proposals:
- Massive neutrinos (Σm_ν > 0.1 eV)
- Modified gravity (f(R), DGP, DHOST)
- Early dark energy (EDE) at z > 1000
- Evolving dark energy
- Sterile neutrinos
- Superfluid dark matter

By 2023-2024, however, systematic re-analyses of earlier lensing surveys revealed potential sources of tension:
- **Shear bias**: Underestimation of galaxy shear measurement uncertainties
- **Photometric redshift errors**: Incorrect redshift distributions leading to biased power spectra
- **Intrinsic alignment mismodeling**: Prior assumptions about how galaxies align with the matter field were incorrect
- **Baryon feedback**: Different feedback prescriptions yield 10-20% variations in weak lensing predictions

The KiDS-Legacy (final) data release (2025) provides an opportunity to **definitively resolve** whether S_8 tension is real or systematic.

---

## Key Arguments and Derivations

### Cosmic Shear Formalism

Cosmic weak lensing is the subtle bending of light by large-scale matter density fluctuations. For a galaxy at comoving distance $\chi$ from the observer, the lensing shear $\gamma$ (fractional distortion of galaxy shape) is:

$$\gamma(\mathbf{l}, z) = \int_0^{\chi(z)} d\chi' \, W(\chi, \chi') \, \delta(\mathbf{l}, \chi')$$

where $\delta$ is the matter density contrast and the **lensing weight** is:

$$W(\chi, \chi') = \frac{\chi' (\chi - \chi')}{\chi} \, \frac{dN}{dz}(\chi')$$

Here $dN/dz$ is the normalized redshift distribution of source galaxies. The shear field $\gamma(\mathbf{l})$ depends on the **total matter power spectrum** $P(k, z)$:

$$P_\gamma(\ell) = \int_0^{\chi_{\max}} d\chi \, W^2(\chi) \, P(k, z(\chi))$$

where $\ell \approx k \, \chi$ is the angular multipole.

### Weak Lensing Two-Point Correlations

The **shear correlation function** (angular separation θ) encodes the power spectrum:

$$\xi_\pm(\theta) = \int_0^{\infty} \frac{d\ell \, \ell}{2\pi} \, P_\gamma(\ell) \, J_{0,4}(\ell \theta)$$

where J_0 and J_4 are Bessel functions. The "+/-" notation refers to two independent linear combinations sensitive to E-mode (curl-free, lensing) and B-mode (curl) shear.

**E-mode** correlations directly probe the matter power spectrum. **B-mode** correlations should be zero in gravitational lensing alone; they appear due to systematic errors (instrumental effects, residual shear bias).

### S_8 Definition and Extraction

From measured $\xi_\pm$, the power spectrum amplitude $\sigma_8(z=0)$ can be extracted via likelihood fitting:

$$\mathcal{L}(\{C_i\} | \xi_\pm^{\text{obs}}) \propto \exp\left[ -\frac{1}{2} (\xi^{\text{obs}} - \xi^{\text{model}})^T C^{-1} (\xi^{\text{obs}} - \xi^{\text{model}}) \right]$$

where the covariance matrix C includes statistical errors and cosmic variance. The parameter $\sigma_8$ is constrained at z = 0 by marginalizing over Ω_m and other parameters.

The dimensionless parameter S_8 is a standard combination:

$$S_8 = \sigma_8 \sqrt{\Omega_m / 0.3}$$

that reduces the strong degeneracy between Ω_m and σ_8 in weak lensing. A "low S_8 tension" means weak lensing prefers lower values (σ_8 smaller, Ω_m smaller, or some combination) compared to CMB.

### KiDS-Legacy Improvements

**Previous KiDS-450 (2017)** analyzed 450 deg² with z_B ≤ 1.3 source galaxies, measuring S_8 = 0.745 ± 0.039.

**KiDS-Legacy (2025)** improvements:

1. **Survey area**: 1,347 deg² (3× larger), reducing cosmic variance by √3.
2. **Redshift depth**: Extended to z_B ≤ 2.0, probing matter power spectrum at smaller scales where degeneracies are reduced.
3. **Photo-z calibration**: Obtained spectroscopic redshifts for ~30,000 galaxies across nine photometric bands (u, g, r, i, Z, Y, J, H, K). Photometric redshift error reduced from σ_z ≈ 0.06 to σ_z ≈ 0.02.
4. **Shear measurement**: Improved PSF correction and shear bias calibration via image simulations. Multiplicative shear bias now |m| < 0.003 (vs. 0.01-0.02 in prior work).
5. **Intrinsic alignment model**: Adopted "tidal alignment" model where galaxy shapes correlate with large-scale tidal tensor, scaling with halo mass and galaxy type (red vs. blue). This reduces model bias.

### Baryon Feedback Marginalization

Non-linear matter power spectrum is affected by baryon feedback (supernovae, AGN jets), which suppress power at k > 1 Mpc⁻¹ by 10-20% depending on feedback strength. Different hydrodynamic simulations (EAGLE, ILLUSTRIS, FLAMINGO, Euclid) disagree on feedback magnitude.

KiDS-Legacy marginalizes over baryon feedback by varying a "feedback parameter" $A_{\text{bary}}$ in the non-linear power spectrum calculation:

$$P_{\text{NL}}(k) = P_{\text{Eulerian}}(k) \times f_{\text{bary}}(k, A_{\text{bary}})$$

The likelihood is marginalized over $A_{\text{bary}} \sim \mathcal{N}(0, 1)$, effectively allowing 1-sigma variation in feedback strength. This adds ~0.01 to the error on S_8.

### Systematic Error Budget

| Source | Contribution to S_8 error |
|:---|:---|
| Statistical (cosmic variance) | 0.012 |
| Photometric redshift bias | 0.008 |
| Shear bias / PSF calibration | 0.006 |
| Intrinsic alignment uncertainty | 0.007 |
| Baryon feedback | 0.009 |
| **Total (statistical + syst.)** | **0.021** |

---

## Key Results

1. **S_8 = 0.815 ± 0.021** (cosmic shear only, KiDS-Legacy 2025)

2. **Agreement with Planck**: Δ(S_8) = 0.019, or 0.73 sigma discrepancy. This is a **3× improvement** in agreement compared to KiDS-450 (which was 2.3 sigma below Planck).

3. **Resolution of tension**: The S_8 tension is **reduced to <1 sigma**, within the range expected from statistical fluctuations and residual systematics. It no longer qualifies as a significant anomaly.

4. **Implications**:
   - No compelling evidence for massive neutrinos (Σm_ν > 0.1 eV) beyond ΛCDM
   - No evidence for modified gravity at late times (z < 2)
   - Early dark energy or evolving dark energy not required by weak lensing data
   - Tension in local Universe (Hubble, S8) appears to stem from systematic rather than fundamental physics

5. **Redshift evolution**: S_8(z) measured in redshift bins shows consistency with ΛCDM predictions (σ_8 grows as $D(a)^2$), with no evidence for evolving dark energy w(z).

---

## Impact and Legacy

KiDS-Legacy (2025) represents a **watershed moment** in precision cosmology: the anomaly that motivated numerous beyond-ΛCDM theories over nearly a decade is resolved as systematic, not fundamental.

Immediate consequences:

1. **Simplification of the cosmological landscape**: With S_8 tension gone, the concordance model (ΛCDM) regains credibility as a comprehensive description of the Universe.

2. **Refocus on remaining anomalies**: Attention shifts to the Hubble tension (which persists) and other potential issues (lithium, Neff, large-scale bulk flows).

3. **Updated cosmological priors**: Future cosmological analyses should use Planck + KiDS-Legacy + other lensing data (DESI, Vera Rubin) with reduced tension assumptions.

4. **Confidence in standard simulations**: FLAMINGO and other standard ΛCDM simulations gain credibility; constraints on modified gravity or early dark energy weaken.

This result is **controversial** within some communities: some researchers argue that systematics in KiDS or Planck (rather than their convergence) explain the agreement, and that independent, more conservative analyses still show tension. However, the mainstream view (Wright et al., majority of collaboration surveys) is that S_8 tension has been resolved.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation, the 32-cell Voronoi tessellation creates spatial inhomogeneity in the matter distribution. The framework predicts:
- σ_8 should be measurably **lower** than ΛCDM (due to DM = quasiparticle pairs being sparser than cold dark matter at small scales)
- S_8 tension would persist even with improved systematics, as a fundamental feature of the framework

**KiDS-Legacy's finding that S_8 = 0.815 ± 0.021, in agreement with Planck**, directly **contradicts** this framework prediction.

However, there are caveats:
1. **Redshift mismatch**: KiDS-Legacy measures S_8 at z ≈ 0.5 (typical redshift of source galaxies). Phonon-exflation's tessellation imprint may be larger at earlier or later redshifts.
2. **Small-scale power**: Phonon-exflation's prediction of reduced small-scale power (due to coherence length of pairs) may only affect k > 1 Mpc⁻¹, too small to significantly impact KiDS measurements.
3. **Systematics in KiDS**: Some independent analyses (e.g., DES) still report tension; if KiDS's agreement is driven by unrecognized systematics, then tension remains real.

**Verdict**: KiDS-Legacy does **not directly test** phonon-exflation (which predicts a specific tessellation geometry, not just a σ_8 shift). However, the resolution of S_8 tension removes one potential observational motivation for the framework.

The framework now depends on other anomalies:
- Bulk flow dipole (419 km/s at 150 h⁻¹ Mpc) — still >3 sigma (Paper 20)
- Gigaparsec structures — unresolved (Papers 21-22)
- Lithium discrepancy — not addressed by phonon-exflation
- Hubble tension — not addressed by phonon-exflation

---

## References

- Wright, A. H., et al. (2025). "KiDS-Legacy: Cosmological Constraints from Cosmic Shear." A&A (submitted), arXiv:2503.19441.
- Kuijken, K., et al. (2015). "Cosmology from Cosmic Shear with DES Science Verification Data." MNRAS, 454, 3888.
- Hildebrandt, H., et al. (2017). "KiDS-450: Cosmological parameter constraints from tomographic weak gravitational lensing." A&A, 633, A69.
- DES Collaboration (2022). "Dark Energy Survey Year 3 Results: Cosmological Constraints from Galaxy Clustering and Weak Lensing." PhysRevD, 105, 023520.
- Abbott, T. M. C., et al. (2018). "Dark Energy Survey Year 1 Results: Cosmological Constraints from Galaxy Clustering and Weak Lensing." PhysRevD, 98, 043526.
