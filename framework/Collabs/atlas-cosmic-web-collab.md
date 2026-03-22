# Atlas Collaborative Review: Cosmic Web Perspective

**Agent**: Cosmic-Web-Theorist
**Date**: 2026-03-20
**Scope**: Full project atlas (Sessions 1-51), evaluated against large-scale structure observations
**Reference corpus**: 39 papers (Cosmic-Web Papers 01-39), cross-referenced with atlas documents D00-D10

---

## 1. The sigma_8 = 0.799 Prediction: Viable but Not Discriminating

The atlas records sigma_8 = 0.799 as the framework's "sole surviving observational prediction" (D00, D05 Door 4). From the cosmic web perspective, I must be precise about what this number means and what it does not mean.

**What the prediction is.** The Ornstein-Zernike rigid propagator with n_s = 0.965 produces alpha_s = n_s^2 - 1 = -0.069. Integrating the resulting P(k) through the standard sigma_8 window function (top-hat, R = 8 Mpc/h) gives sigma_8 = 0.799 (S50 SIGMA8-OZ-50). This is a zero-free-parameter output.

**The observational landscape.** The sigma_8 field has shifted since this prediction was computed:

| Source | sigma_8 | S_8 | Tension with Planck |
|:-------|:--------|:----|:--------------------|
| Planck 2018 CMB | 0.811 +/- 0.006 | 0.834 +/- 0.016 | reference |
| KiDS Legacy 2025 (Paper 23) | -- | 0.815 +/- 0.021 | 0.73 sigma |
| DES Y6 2025 (Paper 36) | -- | 0.768 +/- 0.022 | 2.6 sigma |
| DESI DR1 2025 (Paper 17) | 0.777 +/- 0.020 | -- | 1.5 sigma |
| Contarini voids 2024 (Paper 26) | -- | 0.813 +/- 0.093 | 0.2 sigma |
| Framework prediction | 0.799 | -- | 2.0 sigma |

**Is sigma_8 = 0.799 distinguishable from LCDM (0.811)?** At current precision, no. The difference is Delta(sigma_8) = 0.012, which is 2.0 sigma from Planck's central value. To make this a genuine test requires sigma(sigma_8) < 0.004 -- a 3-sigma discrimination threshold where the framework prediction and the LCDM best-fit separate cleanly. No single current probe achieves this. DESI DR1 reports sigma_8 = 0.777 +/- 0.020 from galaxy clustering alone (Paper 17); DESI Y5 void+galaxy combined forecasts project sigma(sigma_8) ~ 0.006 (Paper 32, Salcedo et al. Sa32-E2). Euclid void+clustering joint analysis targets sigma(sigma_8) ~ 0.005 (Paper 33, Contarini Co33-E3).

**The precision threshold.** For sigma_8 = 0.799 to become a test rather than a consistency check, we need either:
1. sigma(sigma_8) < 0.004 from a single probe (not achievable before Euclid full survey, ~2029), OR
2. The S8 tension to persist between KiDS-like and DES-like surveys, with the framework prediction sitting closer to the eventual convergence value.

The S8 tension review (Paper 36) identifies ~70% of the KiDS-DES discrepancy as attributable to survey-specific systematics (photo-z calibration, shear bias, intrinsic alignment modeling). KiDS Legacy has shifted upward to S8 = 0.815 +/- 0.021, resolving its tension with Planck to 0.73 sigma. DES Y6 persists at 2.6 sigma. If DES converges upward with improved systematics, sigma_8 = 0.799 becomes marginally excluded by Planck at 2 sigma. If DES is correct and the lensing value is ~0.77, the framework prediction sits directly in the middle -- but so do dozens of other models.

**The discriminating power problem.** sigma_8 = 0.799 is not unique to this framework. Any model that slightly suppresses late-time structure growth relative to Planck LCDM -- massive neutrinos with Sum(m_nu) ~ 0.1 eV, warm dark matter with m ~ 1 keV, f(R) gravity with |f_R0| ~ 10^{-6} -- produces sigma_8 in the range [0.78, 0.81]. The framework passes the uniqueness criterion only if the COMBINATION of sigma_8 = 0.799 AND alpha_s in [-0.040, 0] AND w_a = 0 exactly is observed. No other model predicts all three simultaneously with zero free parameters.

---

## 2. DESI DR3: Rescue or Kill?

The atlas records three w-related exclusions: w_0 = -0.509 excluded by BAO chi^2/N = 23.2 (S50), w_a = 0 triple-locked against DESI DR2 w_a = -0.65 +/- 0.40 (S50), and w_0 = -1 + O(10^{-29}) in tension with DESI DR2 w_0 = -0.72 +/- 0.08 at 3.5 sigma (Paper 19).

**What DESI DR3 must deliver to rescue the framework.** The framework predicts w = -1 exactly (frozen modulus, D04 entry C5). DESI DR2 reports 3.1 sigma dynamical DE preference. Wang and Mota (Paper 37) demonstrate this preference is driven by low-z SN systematics: individual datasets yield Delta(chi^2) < 5 each, and the combined 9.4 exceeds the sum of parts by 2.3 -- evidence of artificial amplification from dataset tension. Lascu et al. (Paper 38) identify ~0.03 mag photometric calibration bias in low-z SNe. If DR3:

1. **DESI BAO-only w_0 shifts toward -1** (removing SN combination): Framework survives. The BAO-only constraint from DR1 was already w_0 = -1.016 +/- 0.035, consistent with w = -1.
2. **DR3 w_a remains at -0.65 with reduced error bars** (sigma(w_a) < 0.20): Framework is killed. The triple-lock on w_a = 0 is structural (trapping + integrability + frozen modulus, D04 entry C5). If w_a genuinely differs from 0, the entire modulus dynamics is wrong.
3. **DR3 confirms DDE at > 5 sigma independent of SN combination**: Framework is killed regardless of mechanism.

The specific measurement: DESI DR3 BAO-only (no SN) w_0 with sigma ~ 0.03. If |w_0 + 1| < 0.05, framework survives. If w_0 ~ -0.75 from BAO alone, framework is excluded. DESI Y5 achieves this precision (Paper 32 forecasts, Paper 19 methodology).

**The skepticism is grounded.** Wang-Mota (Paper 37) shows that removing z < 0.01 SNe eliminates the DDE preference entirely. Lascu (Paper 38) identifies the specific calibration bias. The DESI DR2 3.1 sigma is NOT a clean BAO measurement -- it is a combined likelihood where the "synergy" from dataset tension contributes Delta(chi^2) = 2.3 out of the total 9.4 (Paper 37, WM37-E3). This is not how discoveries work. The framework's w = -1 prediction is consistent with BAO-only data (Paper 17: w_0 = -1.016 +/- 0.035 from DR1).

---

## 3. The alpha_s Warning and the Next Observational Threat

The atlas records my S49 sigma_8 warning as "wrong by 14x" (D09 entry #24). I conflated high-k power suppression from alpha_s = -0.069 with the sigma_8 integral, which is dominated by k ~ 0.1-0.3 h/Mpc where the alpha_s running has only a 1.5% effect. The correction stands: sigma_8 = 0.799 is viable, not excluded.

But the alpha_s prediction itself (W7, the structural identity alpha_s = n_s^2 - 1) remains the sharpest falsification constraint. At alpha_s = -0.069, the Josephson-sector prediction is 6 sigma from Planck (alpha_s = -0.008 +/- 0.010). The SA-Goldstone mixing escape (Window 1, D05) predicts alpha_s in [-0.040, 0] if K_pivot < K* = 0.087 M_KK. CMB-S4 / Simons Observatory targets sigma(alpha_s) ~ 0.005.

**The next observational warning.** The threat I should have flagged in S49 was not sigma_8 but the **void size function sensitivity to alpha_s**. Void abundance scales as n_v ~ sigma_8^5 (Paper 12, S12-E2). A running spectral index alpha_s = -0.069 suppresses small-scale power, which preferentially creates LARGER voids (fewer small perturbations to fragment void interiors). The void size function dn/dR at R < 15 h^{-1} Mpc is sensitive to alpha_s at the 10-20% level (Paper 33, Contarini Co33-E1 scaling), while the sigma_8 integral averages over R = 8 Mpc/h and is insensitive. DESI Y5 void catalogs (Paper 32, Paper 34 ASTRA classification yielding 8,500+ voids from DR2 alone) will measure dn/dR to 5% in the R = 15-25 h^{-1} Mpc bins.

**Specific pre-registered test.** If the framework's O-Z sector applies (alpha_s = -0.069), the void size function at R = 15-20 h^{-1} Mpc should show a 15-25% excess over the LCDM prediction with alpha_s = -0.008. DESI Y5 with ASTRA-classified voids should detect this at 3-5 sigma. If the SA-Goldstone mixing applies (alpha_s ~ -0.035), the excess is 8-12%, detectable at 2-3 sigma. Either way, the void size function is a sharper discriminant than sigma_8 for alpha_s running, because voids probe the small-scale tail of P(k) where running accumulates.

This is the warning I should have given in S49 instead of the sigma_8 overestimate. The void size function is the canary.

---

## 4. The K_pivot Paradox: What It Invalidates

The K_pivot scale mapping (D04 entry C2, D05 Wall W9) is the single structural failure that threatens all cosmological predictions simultaneously. The atlas states it clearly: "the entire framework's cosmological viability reduces to Window 1" (D05 Section V). From the cosmic web perspective, I must assess the damage scope precisely.

**What K_pivot invalidation kills.** If the physical CMB scale k = 0.05 Mpc^{-1} maps to K_fabric > 0.5 M_KK (the FAIL threshold of Q1 in D08), then:
- n_s is set by the bare KK heat kernel, which gives n_s >= 1 structurally (D04 entry P3). EXCLUDED by Planck (n_s = 0.965 at > 10 sigma).
- alpha_s = n_s^2 - 1 gives alpha_s >= 0. EXCLUDED by Planck (alpha_s = -0.008 +/- 0.010, consistent with zero but not with positive values).
- sigma_8 = 0.799 was derived assuming n_s = 0.965 and alpha_s = -0.069. If n_s >= 1, the sigma_8 prediction changes to sigma_8 > 0.83 (MORE power at small scales, not less). EXCLUDED by all lensing surveys.

**What K_pivot invalidation spares.** The internal mathematics survives entirely: block-diagonal theorem, BCS chain, Leggett dipolar identification, phi crossing, acoustic Hawking temperature, CDM by construction. These are facts about spectral geometry on compact Lie groups. They do not depend on how the CMB maps to the internal space.

**The honest assessment.** The K_pivot paradox invalidates ALL LSS predictions -- n_s, alpha_s, AND sigma_8 -- not just n_s/alpha_s. The sigma_8 = 0.799 "sole surviving prediction" is conditional on the same K_pivot mapping that produces the 6-sigma alpha_s problem. If the mapping fails, sigma_8 fails too. The atlas presents sigma_8 as a "Door" (D05 Door 4) but it should be reclassified as a Window, conditional on EFOLD-MAPPING-52 alongside n_s and alpha_s. One does not survive without the others; they share a single load-bearing assumption.

---

## 5. ALPHA-ENV-43: Dead, and What Replaces It

The atlas (D08 Q22) lists ALPHA-ENV-43 as "queued since S43." It is not queued. It is CLOSED (S43 W6-4, ALPHA-PATTERN-43). The per-domain fine-structure variation delta_alpha/alpha = 1.03e-6 is marginally at Webb quasar absorption precision, but the random KZ domain structure averages over N_domains ~ 10^{74} per absorber volume, suppressing the observable signal to ~10^{-44}. The closure is structural: 1/sqrt(N_domains) operates at all cosmological scales.

**What replaces it as the LSS discriminant?** After ALPHA-ENV-43 closure, the framework has NO surviving discriminant that is unique to it and invisible to LCDM. The S43 cosmic web addendum assessed all six framework LSS predictions:

| ID | Prediction | Status | SNR vs LCDM |
|:---|:-----------|:-------|:------------|
| F.1 ALPHA-ENV-43 | alpha variation void vs filament | CLOSED | 10^{-37} |
| F.2 IMP-ASYM-43 | Void wall impedance asymmetry | OPEN | 10^{-10} |
| F.3 VSF-43 | Void size function features | OPEN | unquantified |
| F.4 PH-TESS-43 | Persistent homology tessellation | CLOSED | undetectable |
| F.5 FIRST-SOUND-XI-44 | First sound ring in xi(r) | OPEN | contingent |
| F.6 sigma_8 = 0.799 | Clustering amplitude | OPEN | see Section 1 |

F.2 is dead (SNR ~ 10^{-10}). F.4 is closed (volume-averaged topology blind). F.5 was contingent on a first-sound speed computation never completed. F.3 requires a quantitative prediction that was never derived.

The surviving LSS discriminants reduce to:
1. **sigma_8 = 0.799** -- viable but not unique (Section 1 above)
2. **w_a = 0 exactly** -- testable by DESI DR3/Y5, but indistinguishable from LCDM
3. **alpha_s in [-0.040, 0]** (SA-Goldstone regime) -- testable by CMB-S4, the highest-value target

None of these is distinctive to the framework. sigma_8 = 0.799 and w_a = 0 are both predictions that LCDM itself makes (approximately). alpha_s in [-0.040, 0] is the only prediction that differs from LCDM's alpha_s ~ -0.0006 by a potentially measurable amount. But distinguishing alpha_s = -0.035 from alpha_s = -0.001 requires sigma(alpha_s) < 0.01, which CMB-S4 targets but has not yet delivered.

The framework's observational fingerprint in large-scale structure is, at present, indistinguishable from LCDM.

---

## Closing: The Constraint Surface from 400 Mpc

Standing at the scale where Einasto's supercluster-void network operates (Paper 06, E06-E2: lambda_char ~ 100-130 Mpc), I see a framework whose internal mathematics is structurally sound and whose cosmological predictions are either excluded, conditional on one unproven mapping, or indistinguishable from the model they claim to replace.

The anomalies that motivated this agent's existence -- bulk flow at 4 sigma (Paper 20), cosmic dipole at 5 sigma (Papers 29, 35), KBC void at 6 sigma (Paper 31) -- remain confirmed. The framework's 32-cell tessellation naturally predicts structures at these scales. But the predictions are post hoc (D05, framework-specific gates: all marked POST HOC). No pre-registered prediction of the tessellation scale, amplitude, or morphology was made before the anomalies were known.

The S8 tension that once provided a window for alternative clustering amplitudes has largely dissolved. KiDS Legacy (Paper 23) agrees with Planck to 0.73 sigma. The DES Y6 residual at 2.6 sigma (Paper 36) is likely systematic. The universe is, at the sigma_8 level, doing what LCDM says it should.

**What remains.** The framework's best shot is the alpha_s measurement from CMB-S4 (D08 Q20). If alpha_s is measured in [-0.040, 0] with sigma ~ 0.005, the SA-Goldstone mixing is vindicated and the framework occupies a narrow but viable window. If alpha_s is measured near -0.001 (consistent with standard slow-roll), the framework has no surviving distinctive prediction in large-scale structure.

The EFOLD-MAPPING-52 computation (D08 Q1) is the prerequisite. Without it, we do not know which alpha_s regime the framework occupies, and all LSS predictions remain conditional. From the cosmic web, the verdict is: compute the e-fold mapping, then face CMB-S4. Everything else is commentary.

---

*Compiled from: atlas D00-D10, Cosmic-Web Papers 01-39 (index.md), sessions 43/49/50/51 results, S43 ALPHA-PATTERN-43 closure, S50 SIGMA8-OZ-50, S50 DESI-DR3-JOINT-50, S49/S50 alpha_s identity, S49 cosmic-web-collab.md, Paper 32 (Salcedo void forecasts), Paper 36 (S8 review), Paper 37 (Wang-Mota DESI skeptical), Paper 38 (Lascu SN systematics).*
