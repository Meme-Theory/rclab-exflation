# Cosmic Web Theorist -- Collaborative Feedback on Session 69

**Author**: Cosmic Web Theorist
**Date**: 2026-04-05
**Re**: Session 69 Results (Nice.)

---

## Section 1: Key Observations

Session 69 is the first session to build a comprehensive phonon-vs-data scorecard across the full set of large-scale structure observables. From my domain -- power spectra, two-point statistics, growth rate, void/cluster counting, BAO distances, gravitational lensing, ISW -- this session addresses almost every channel I have been tracking since S43. The results demand careful numerical evaluation, not default classification.

**1.1 Growth rate f*sigma_8: framework OUTPERFORMS LCDM.** PVD-FSIG8-69 (W2-D) returns chi^2/dof = 0.761 vs LCDM 0.893 across 9 independent RSD bins from 6dFGS through DESI DR1. The data compilation is sound: BOSS DR12 and DESI DR1 are not double-counted at overlapping redshifts (DESI supersedes at z = 0.51 and 0.71 where errors are smaller). The framework's ~4% suppression of f*sigma_8 relative to LCDM at z < 1 pulls model predictions into better alignment with data that systematically sits below LCDM. This is not a tuned parameter -- it is a structural consequence of w_0 = -0.918 via the growth ODE. My S67 memory records chi^2/N = 0.27 (LCDM: 0.35) from a smaller dataset; the S69 result with expanded DESI DR1 data is quantitatively consistent and statistically sharper.

**1.2 sigma_8 / S_8 tension ameliorated but not resolved.** Three independent probes now confirm the same direction. The framework predicts sigma_8 = 0.793 (S_8 = 0.813), sitting between Planck CMB (0.831) and the weak lensing mean (0.771). From PVD-KAPPA-69 (W5-P): the WL-only chi^2 drops from 22.4 (Planck LCDM) to 11.0 (framework), a 51% reduction. From PVD-CLUST-69 (W5-M): cluster mass function tension drops from 2.1-sigma to 1.2-sigma. From PVD-FSIG8-69 (W2-D): RSD data prefers the lower growth amplitude. The direction is unambiguous. But the magnitude is insufficient for full resolution: closing the gap to sigma_8 ~ 0.75 would require a growth suppression of ~7%, double what w_0 = -0.918 provides. This is a structural ceiling.

**1.3 BAO distances: PASS but highest tension.** PVD-DA-69 (W2-F) computes D_M/r_d chi^2/dof = 2.076 and D_H/r_d chi^2/dof = 1.513 against DESI DR2. Both are below the PASS threshold of 3. The framework predicts distances 1.0-1.6% shorter than LCDM, while DESI at z = 0.51-0.71 (LRG1, LRG2) measures distances slightly LONGER than LCDM. This creates a coherent negative pull (mean = -0.68 sigma in D_M), worst at LRG2 z = 0.706 (-2.26 sigma). The pull is not random scatter -- it is the unavoidable geometrical signature of w_0 > -1 with w_a = 0. LCDM itself gets chi^2/dof = 1.39 for D_M, so the framework penalty is 0.68 units above LCDM. The S67 result (chi^2/N = 1.80 combined) is reproduced to 3 significant figures, confirming numerical stability.

**1.4 Galaxy angular power spectrum: below discrimination threshold.** PVD-GALCL-69 (W5-L) finds a combined 0.76-sigma deviation from LCDM across 49 l-bins. The 1.9% suppression in C_l^{gg} (from sigma_8 and n_s differences) is far below cosmic variance at SDSS precision (~15% per bin at l ~ 100). BAO wiggle positions are unchanged between framework and LCDM because they depend on Omega_m and Omega_b, which are shared. This is consistent with the S43 closure of volume-averaged statistics: at current survey precision, the framework and LCDM are observationally degenerate in the projected galaxy power spectrum.

**1.5 ISW cross-correlation: 12.4% enhancement, undetectable with current data.** PVD-ISW-69 (W5-O) computes A_ISW(FW) = 1.124 against published SDSS+Planck measurements. The combined delta_chi^2 = +0.43 across 6 tracers is statistical noise. Euclid would reach 2.5-sigma for FW vs LCDM; the substrate-specific tracking discriminant (c_s^2 = 0 vs 1) reaches only 1.36-sigma with Euclid. The 21cm intensity mapping era (2040s) is the earliest window for definitive ISW discrimination.

---

## Section 2: Assessment of Key Findings

**2.1 Methodological quality of the data comparisons.**

The growth rate comparison (W2-D) uses the correct approach: exact integration of the growth ODE with RK45 at rtol = 1e-12, comparison against 9 independent published RSD bins, and no free parameters. The Alcock-Paczynski correction between LCDM and w = -0.918 is correctly noted as <0.3%, negligible. The eBOSS QSO point at z = 1.48 (2-sigma outlier for ALL models) does not contaminate the conclusion -- it is a known systematics-limited measurement. The residual trend analysis (slope = -0.56 +/- 0.64, p = 0.41) confirms no redshift-dependent systematic.

The Pantheon+ comparison (W2-E) uses diagonal errors only, which is a limitation. The full 1701 x 1701 covariance matrix would increase chi^2/dof for both models. However, the published Pantheon+ constraint w = -0.90 +/- 0.14 (Brout et al. 2022, with full covariance) encompasses w_0 = -0.918, so the direction is secure. The fitted M_B = -19.43 correctly absorbs the H_0 tension, isolating the shape of d_L(z). The residual trend of 11.1 mmag over 3.27 dex in z is well below the 50 mmag FAIL threshold.

The BAO comparison (W2-F) correctly separates D_M/r_d and D_H/r_d rather than using the composite D_V/r_d, which was the approach in S68 PVD-02 and gave a worse chi^2/dof = 4.06. The D_M/r_d chi^2/dof = 2.08 is the cleaner number. The sound horizon r_d = 147.024 Mpc (Eisenstein & Hu fit) matches the integral cross-check to 0.06% and Planck to 0.25-sigma. This is a solid methodological foundation.

**2.2 The S_8 amelioration is physically transparent but observationally bounded.**

The mechanism is clean: w_0 = -0.918 means dark energy was marginally stronger at earlier times, suppressing the linear growth factor by ~2.2% relative to LCDM by z = 0. This propagates to sigma_8 (0.793 vs 0.811), f*sigma_8 (~4% lower at z < 1), cluster counts (7-18% fewer at M > 10^{14.5} M_sun), and lensing convergence (1.5% suppressed). The consistency across all four probes (RSD, clusters, WL kappa, galaxy C_l) is a strong cross-check.

The limitation: the tracking factor (1+w)/(1-3w) = 0.022 at w_0 = -0.918 produces only percent-level modifications to the Poisson equation source term. The DE clustering (c_s^2 = 0 from the Volovik tracking vacuum) enhances this by a further ~1%, but the total effect on structure growth is capped at ~4-5%. Getting to sigma_8 ~ 0.75 (full S_8 resolution) would require either w_0 ~ -0.80 (excluded by DESI BAO at much higher tension) or additional physics beyond the effacement residual.

**2.3 The cluster mass function comparison has real selection function limitations.**

PVD-CLUST-69 (W5-M) correctly uses Tinker et al. (2008) at Delta = 200, which is the standard for SZ-selected clusters. The chi^2/dof > 3 for both framework and LCDM is driven by the z > 0.7 bin where the simplified mass threshold parameterization fails. Excluding that bin gives chi^2/dof = 2.7 (FW) vs 2.4 (LCDM), with delta_chi^2 = 2.1 not statistically significant. The exponential sensitivity of the mass function to sigma_8 at the massive tail makes this a useful direction-indicator but not a precision discriminant. Hydrostatic mass bias (b ~ 0.2) and Eddington bias further degrade the comparison. The honest interpretation: the framework eases the tension from 2.1 to 1.2 sigma, which is directionally correct but not decisive.

---

## Section 3: Collaborative Suggestions

**3.1 Void size function at w_0 = -0.918.**

Voids are the most underexploited discriminant in this session. The void size function (VSF) is sensitive to the expansion history through the shell-crossing condition and to sigma_8 through the excursion set formalism (Sheth & van de Weygaert 2004). The framework's 2.2% lower sigma_8 and modified growth rate will shift the predicted VSF at the few-percent level. BOSS/DESI void catalogs from VIDE (Sutter et al. 2014) exist and have been used to constrain dark energy (Hamaus et al. 2020, arXiv:2007.07895; Contarini et al. 2024 for DESI). A chi^2 comparison of the framework VSF against the BOSS void catalog would be a zero-cost test. Pre-register: PASS if chi^2/dof < 2, FAIL if chi^2/dof > 5.

**3.2 Void-galaxy cross-correlation for Alcock-Paczynski test.**

The Alcock-Paczynski (AP) test using void stacking measures the ratio D_A(z) * H(z), which is insensitive to galaxy bias and provides a clean geometric probe. Hamaus et al. (2022) demonstrated this with BOSS voids. At w_0 = -0.918, the predicted AP ratio differs from LCDM by ~2% at z = 0.5. The existing BOSS void catalog can test this directly. This is complementary to the BAO D_M/r_d and D_H/r_d tests (W2-F) because voids probe the AP ratio through a different geometric configuration.

**3.3 Redshift-space void profiles for growth rate extraction.**

Cai, Padilla & Li (2015) showed that redshift-space void density profiles constrain f*sigma_8 independently of galaxy bias. The framework's ~4% suppression of f*sigma_8 at z < 0.7 (W2-D) could in principle be cross-checked using BOSS void profiles. This provides an independent path to the f*sigma_8 constraint that avoids the standard RSD analysis pipeline and its assumptions about the velocity divergence power spectrum.

**3.4 BAO peak position at n_s = 0.9595.**

The session confirmed that BAO wiggle positions are unchanged between framework and LCDM (W5-L: BAO phase correlation r = 0.558, amplitude shift 0.23%). This is expected because the BAO scale depends on the pre-recombination sound horizon, set by Omega_b and Omega_m. However, the BAO DAMPING (Silk damping) depends on n_s through the primordial power spectrum slope. At n_s = 0.9595 vs 0.9649, the BAO peak heights are marginally reduced at higher harmonics (k > 0.15 h/Mpc). DESI DR2 measures BAO peak shapes with enough precision to test this. A computation of the BAO peak amplitude ratio at the 2nd and 3rd harmonics would quantify whether the n_s shift produces a detectable BAO damping signature.

**3.5 Persistent homology / Betti numbers at framework cosmology.**

The S43 closure of persistent homology tests was for direct substrate signatures (preferred scales, topological defects). But persistent Betti numbers are also sensitive to sigma_8, n_s, and w_0 through the large-scale density field topology. Feldbrugge et al. (2019, our Paper Pr28) demonstrated that persistent Betti numbers B_0, B_1, B_2 from N-body simulations discriminate between cosmological parameters. A Fisher forecast for the discriminating power of persistent Betti numbers between framework (sigma_8 = 0.793, n_s = 0.9595, w_0 = -0.918) and LCDM (0.811, 0.9649, -1) would quantify whether topological statistics add constraining power beyond P(k) and xi(r). Given that these are integral statistics (not volume-averaged moments), they may capture information that the two-point function misses -- particularly in the void-dominated regime where the growth suppression is strongest.

**3.6 Cosmic web classification with modified growth.**

The NEXUS+ (Cautun et al. 2013) or DisPerSE (Sousbie 2011) cosmic web classifiers partition the density field into filaments, walls, voids, and clusters. The framework's 4% lower growth amplitude changes the relative volume fractions: fewer voids reach shell-crossing, filament connectivity is marginally reduced, and the node/filament mass ratio shifts. A comparison of web type fractions between framework and LCDM N-body simulations would test whether the growth suppression produces a measurable shift in web morphology statistics. This would require running or analyzing existing N-body suites at the framework cosmology -- not zero-cost, but the QUIJOTE simulation suite (Villaescusa-Navarro et al. 2020) includes runs at varied sigma_8 that could be interpolated.

**3.7 Full covariance matrix for Pantheon+ and DESI RSD.**

Both W2-D and W2-E use diagonal errors. The Pantheon+ covariance matrix is publicly available (Brout et al. 2022 data release). The DESI DR1 RSD covariance between redshift bins is also available. Re-running both comparisons with the full covariance would tighten the Delta_chi^2 estimates and provide publication-quality numbers. This is a computational exercise, not a new test, but it converts "directionally correct" into "quantitatively robust."

---

## Section 4: Connections to Framework

**4.1 The w_0 = -0.918 effacement residual as the sole source of LSS modifications.**

Every LSS result in this session traces to a single parameter: w_0 = -0.918. The growth suppression (f*sigma_8, sigma_8, cluster counts, lensing) and the distance shortening (BAO, SNe) are both geometric consequences of the modified expansion history H^2(z) = H_0^2 [Omega_m(1+z)^3 + Omega_DE(1+z)^{3(1+w_0)}]. The framework adds a second channel (DE clustering from c_s^2 = 0), but this produces only percent-level effects on top of the expansion history modification. From the cosmic web perspective, the framework is LCDM-with-one-parameter-shifted in all volume-averaged statistics. The discriminating power lies entirely in the precision of the w_0 measurement and the c_s^2 signature.

**4.2 Volovik tracking and its observational consequences.**

The S67 structural result -- constant-chi tracking is algebraically LCDM -- means the framework's DE is not dynamical in the w_a sense. The observational consequence, confirmed by W2-F (chi^2 with DESI), is that the framework cannot accommodate the DESI DR2 preference for w_a < 0. If DESI DR3 strengthens the w_a evidence (|w_a| > 0.53 at >3-sigma), the framework faces a structural tension that cannot be resolved by adjusting w_0 alone. The Volovik tracking result is not a tunable degree of freedom -- it is an algebraic identity. This makes the w_a = 0 prediction the framework's sharpest falsifiable LSS test.

**4.3 The n_s shift and large-scale structure.**

The framework's n_s = 0.9595 vs Planck 0.9649 produces a -0.0054 tilt that is visible in the CMB C_l^TT at 1.15% (W3-D) but washed out in the projected galaxy power spectrum (W5-L). At face value, this is observationally degenerate in LSS. But the tilt cumulates over decades in k: at k = 0.001 h/Mpc (the largest BAO-accessible scales), the power is 3.5% higher than LCDM, while at k = 0.3 h/Mpc it is 1.5% lower. This scale-dependent tilt, combined with the sigma_8 shift, produces a composite P(k) shape that is in principle distinguishable from a pure sigma_8 shift at fixed n_s. Euclid's spectroscopic survey (k_max ~ 0.25 h/Mpc over V ~ 100 Gpc^3) may resolve this through broadband P(k) shape analysis rather than BAO-only extraction.

---

## Section 5: Open Questions

**5.1** The framework's expansion history (w_0 = -0.918, w_a = 0) predicts distances 1.0-1.6% shorter than LCDM while DESI measures distances at z = 0.5-0.7 that are slightly LONGER than LCDM. This creates a coherent pull in the wrong direction at intermediate redshifts. Can any LSS observable break this geometric degeneracy, or is BAO the final word?

**5.2** The S_8 amelioration caps at ~30% of the tension (in sigma units). Is there a regime (nonlinear scales, halo-void cross-correlations, higher-order statistics) where the framework's growth suppression has an amplified effect relative to LCDM?

**5.3** Void interiors are regions where the local matter density is well below the mean. In the framework's Volovik tracking picture (c_s^2 = 0), the DE perturbation delta_DE = (1+w)/(c_s^2 - w) * delta_m has a pole at c_s^2 = 0 for w near -1. Does the tracking vacuum prediction produce measurably different void profiles compared to smooth quintessence (c_s^2 = 1)? The EUCLID-LENS-69 result (1.29% tracking suppression in CMB lensing) suggests a percent-level effect, but void interiors probe a different density regime.

**5.4** The bulk flow anomaly (>4 sigma at 200 h^{-1} Mpc, V = 419 +/- 36 km/s from CosmicFlows-4) and the cosmic dipole anomaly (>5 sigma in radio galaxies) remain the strongest surviving LSS anomalies with no framework mechanism. Does w_0 = -0.918 modify the predicted bulk flow amplitude at 200 h^{-1} Mpc relative to LCDM? This is a straightforward computation: v_bulk ~ H_0 * f * integral of P(k) * W^2(kR) dk, where f = Omega_m^{0.55} is modified by w_0.

**5.5** The folded bispectrum f_NL = 0.129 is undetectable by any survey before 21cm intensity mapping (W5-K: sigma = 18.9 for Euclid). Is there an integrated statistic (Minkowski functionals, peak counts, one-point PDF) that has enhanced sensitivity to the folded shape relative to the full bispectrum? Chiang et al. (2015) showed that the density PDF captures bispectrum information more efficiently than the bispectrum estimator itself for non-Gaussian fields. This could shorten the detection timeline.

---

## Section 6: Computation Suggestions Summary

| # | Computation | Input Data | Output | Pre-Registered Gate (if any) | Priority |
|:--|:-----------|:-----------|:-------|:----------------------------|:---------|
| 1 | Void size function at FW cosmology | BOSS/DESI void catalog (VIDE), Tinker MF, sigma_8=0.793, w_0=-0.918 | chi^2/dof against observed VSF | PASS if chi^2/dof < 2 | HIGH |
| 2 | AP test from void stacking | BOSS void catalog, D_A(z)*H(z) at FW cosmology | Delta(AP)/AP vs LCDM at z=0.5 | -- | MED |
| 3 | Void density profiles for f*sigma_8 | BOSS void stacks, Cai+2015 method | Independent f*sigma_8 constraint | -- | MED |
| 4 | BAO peak damping at n_s = 0.9595 | Eisenstein-Hu transfer function, DESI DR2 BAO peak shapes | 2nd/3rd harmonic amplitude ratio FW vs LCDM | -- | LOW |
| 5 | Persistent Betti number Fisher forecast | Feldbrugge+2019 (Pr28) methodology, FW vs LCDM parameters | sigma(sigma_8, n_s, w_0) from B_0, B_1, B_2 | -- | MED |
| 6 | Full covariance Pantheon+ and DESI RSD | Brout+2022 public covariance, DESI DR1 RSD covariance | Publication-quality Delta_chi^2 | -- | HIGH |
| 7 | Bulk flow amplitude at w_0 = -0.918 | P(k) at FW cosmology, v_bulk integral at R=200 h^-1 Mpc | v_bulk(FW) vs v_bulk(LCDM) vs CosmicFlows-4 | INFO: report shift magnitude | MED |
| 8 | DE clustering in void interiors (c_s^2=0) | Volovik tracking, VIDE void profiles | delta_DE in void centers; profile shift FW vs quintessence | -- | LOW |
| 9 | Density PDF sensitivity to folded f_NL | Chiang+2015 method, f_NL^folded=0.129 | Detection significance via PDF vs bispectrum estimator | -- | LOW |

---

## Section 7: Wrap-Up

### What Changed

- **The framework is now empirically competitive with LCDM across all LSS probes tested.** f*sigma_8 (chi^2/dof = 0.761 vs 0.893), Pantheon+ SNe (chi^2/dof = 1.025 vs 1.149), galaxy C_l (0.76-sigma indistinguishable), cluster mass function (tension reduced 2.1 to 1.2 sigma), CMB lensing S_8 (WL chi^2 halved). Zero free parameters. The combined Delta_chi^2 = -5.66 across f*sigma_8 + SNe (46 data points) favoring w_0 = -0.918 over w = -1 is the strongest empirical evidence the framework has produced from my domain.

- **The S_8 tension amelioration is confirmed across three independent probes but capped at ~30% of the gap.** sigma_8(FW) = 0.793, S_8 = 0.813 sits between Planck (0.831) and weak lensing (0.771). The mechanism is structurally determined: w_0 = -0.918 suppresses growth by ~4%, which is the maximum available from the effacement residual without modifying w_a or Omega_m. Full resolution to sigma_8 ~ 0.75 requires additional physics beyond what the framework provides in its current form.

- **BAO distances against DESI DR2 are cleaner than previously reported.** The S68 PVD-02 using D_V/r_d gave chi^2/dof = 4.06 (INFO/tension). The S69 separation into D_M/r_d (2.08) and D_H/r_d (1.51) is methodologically superior and both pass the pre-registered threshold. The framework's BAO performance is acceptable, not excellent -- it is the weakest link in the observational scorecard but no longer in formal tension.

### What Holds

- **All S43 closures remain valid.** Volume-averaged statistics (P(k), xi(r), sigma_8, VSF, Minkowski functionals, genus, persistent Betti numbers) show no substrate-specific signatures. The framework produces standard LCDM-like large-scale structure with a sigma_8 shift from the modified expansion history. No preferred scales, no topological defects, no anomalous features in the power spectrum. The k_transition = 9.4e23 h/Mpc permanent closure stands: the substrate's internal physics operates at scales 20+ orders of magnitude above any survey's resolution.

- **The f*sigma_8 growth rate is the framework's strongest LSS observable.** The 4% suppression relative to LCDM at z < 0.7 is structurally locked to w_0 = -0.918 and goes in the direction the data prefers. This was the prediction from S67 (chi^2/N = 0.27); S69 confirms it with more data (chi^2/dof = 0.761). DESI 5-year and Euclid spectroscopic RSD measurements at z = 0.9-1.8 will test this prediction at the sub-percent level.

- **The w_a = 0 prediction remains the sharpest falsifiable LSS test.** The Volovik tracking structural result (S67) and the substrate compaction closure (S66) both enforce w_a = 0 algebraically. DESI DR3 is the next decisive measurement. The pre-registered decision rules from S65 remain valid.

### What Breaks or Strains

- **The BAO distance tension persists at moderate significance.** D_M/r_d chi^2/dof = 2.08 passes the threshold but the coherent negative pull (-0.68 sigma mean across 7 DESI bins) is not statistical noise -- it is the structural signature of w_0 > -1 predicting shorter distances than observed. The worst bin (LRG2 at z = 0.706, -2.26 sigma) is individually concerning. With w_a = 0 locked, the framework has no degree of freedom to accommodate this. If DESI DR3 sharpens the BAO measurement and the pull grows, this becomes the dominant observational threat.

- **The c_s^2 = 0 tracking vacuum discriminant is observationally marginal through the Euclid era.** The FW vs Quintessence discrimination reaches only 1.72-sigma with Euclid ISW + RSD + lensing combined (W3-B). The tracking factor (1+w)/(1-3w) = 0.022 at w_0 = -0.918 produces percent-level effects that are below Euclid's discriminating power for the c_s^2 parameter. The substrate-specific prediction (tracking vacuum = LCDM with DE perturbations) cannot be confirmed or falsified until 21cm intensity mapping in the 2040s. This is a 15+ year observational deferral for the framework's most distinctive LSS prediction.

- **Bulk flow and cosmic dipole anomalies remain unexplained.** The bulk flow at >4 sigma and the cosmic dipole at >5 sigma are the strongest surviving LSS anomalies (per meta-analysis update, 2026-03-13). The framework provides no mechanism for either. The w_0 = -0.918 modification to the growth rate changes the predicted bulk flow by only a few km/s at 200 h^{-1} Mpc -- negligible compared to the 419 km/s observed. If these anomalies are real departures from statistical isotropy, they point to physics beyond both LCDM and the framework.

### Carry-Forward Computations

1. **Void size function at FW cosmology.** Compute the predicted VSF using Sheth & van de Weygaert (2004) excursion set formalism at sigma_8 = 0.793, w_0 = -0.918. Compare against BOSS DR12 void catalog from VIDE. Input: canonical_constants.py, Tinker MF parameters. Output: chi^2/dof. Gate: PASS if < 2.

2. **Full covariance Pantheon+ reanalysis.** Download Brout et al. (2022) public covariance matrix. Recompute W2-E with full off-diagonal systematics. Input: s69_pvd04_sne.py, Pantheon+ public data. Output: publication-quality Delta_chi^2(FW vs LCDM). No gate; sharpens existing result.

3. **Full covariance DESI RSD reanalysis.** Obtain DESI DR1 RSD covariance between redshift bins. Recompute W2-D with correlations. Input: s69_pvd05_fsigma8.py, DESI public data. Output: correlated chi^2/dof. No gate; sharpens existing result.

4. **Bulk flow amplitude at w_0 = -0.918.** Compute v_bulk(R) = H_0 * f(w_0) * integral[P(k) W^2(kR) dk] at R = 200 h^{-1} Mpc. Compare FW vs LCDM vs CosmicFlows-4 (419 +/- 36 km/s). Input: P(k) from Eisenstein-Hu at FW parameters. Output: v_bulk(FW), delta_v/v vs LCDM. Gate: INFO.

5. **Persistent Betti number Fisher forecast.** Use Feldbrugge et al. (2019) scaling of B_0, B_1, B_2 with sigma_8 and n_s. Compute expected discriminating power between FW (0.793, 0.9595) and LCDM (0.811, 0.9649). Input: Pr28 scaling relations. Output: sigma(sigma_8) from topological statistics. No gate.

6. **Void density profiles for tracking vacuum discriminant.** Compute the predicted void density profile at w_0 = -0.918 with c_s^2 = 0 vs c_s^2 = 1. Quantify the difference in void center density and wall amplitude. Input: linear void model, tracking factor. Output: delta(rho/rho_mean) at void center, FW vs quintessence. No gate; explores whether voids amplify the c_s^2 signal beyond the 1.3% CMB lensing effect.

7. **BAO peak damping ratio at n_s = 0.9595.** Compute the ratio of 2nd-to-1st BAO peak amplitudes in P(k) for FW vs LCDM. Input: Eisenstein-Hu transfer function with wiggles, k = 0.05-0.30 h/Mpc. Output: amplitude ratio difference FW vs LCDM. No gate; quantifies n_s sensitivity in BAO peak shape.

8. **Density PDF sensitivity to folded f_NL.** Use Chiang et al. (2015) formalism to compute the SNR for f_NL^folded = 0.129 from the one-point density PDF of a Euclid-like survey. Input: folded template from S67, Euclid survey parameters. Output: SNR(PDF) vs SNR(bispectrum estimator). No gate; explores whether the PDF shortens the detection timeline relative to the W5-K result (sigma = 18.9).

---

The single most important finding: the framework's growth rate prediction at w_0 = -0.918 fits f*sigma_8 data better than LCDM (chi^2/dof = 0.761 vs 0.893, 9 independent RSD bins), and this same suppression ameliorates the S_8 tension across three probes -- all with zero free parameters.
