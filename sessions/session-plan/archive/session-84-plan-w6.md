# Session 84 Plan — Wave 6: Field-Theory Dressing + CGWB + Sibling Observables (8 gates)

**Session**: 84
**Wave**: 6 of 10
**Theme**: Field-theory dressing (counterterm existence, R-protected balanced-ratio atlas, F_amp FI-chain proof, field-expansion convergence) + observational tail (CGWB absolute-P_t + sibling-observables common-prefactor + CMB-S4 alpha_s projection refinement) + meta-gate on Mellin-balance pre-declaration template
**Planner**: feynman-theorist (W6 slice)
**Date planned**: 2026-04-18

---

## W6 Summary

Wave 6 closes the field-theory-dressing tail of the S83 carry-forward. It discharges five sub-obligations on the Mukhanov-Sasaki / 3PI derivation of A_s (clause-(b) FI chain, Z_R counterterm, balanced-ratio atlas completeness, field-expansion NLO), formalizes the Mellin-balance pre-declaration template as a meta-gate to prevent recurrence of the S83 G15 / G28 / G34 cluster-test failures, and pins three observational projections: (i) CGWB absolute P_t(f) at LISA/DECIGO/BBO with (A)-vs-(C) branch discrimination; (ii) the full sibling-observable inventory inheriting the H_tilde^n prefactor with d(ln O)/d(ln H_tilde) per channel; (iii) a refreshed CMB-S4 alpha_s projection against Abazajian 2022+ to confirm the ~34σ discrimination figure for the S50 prediction alpha_s = n_s^2 - 1 = -0.0690.

The Wave intentionally combines field-theory and observational gates because both inherit the H_tilde^n common-prefactor structure from CC3 identity (+2 exponent on A_s, absolute P_t, and the P_t-derivative chain). The dressing proofs feed the observational projections; the observational channels feed the falsifier registry.

**Concurrent dispatch**: 8 gates. To respect the user's ≤~8 concurrent cap, all 8 execute as one batch.

---

## W6 Decision Point Prerequisites

Before W6 dispatch:

- **W5 Mellin-balance template proposed** (if W5 produced a draft). W6-71 is the formalization-as-meta-gate. If W5 did not produce a draft, W6-71 constructs it from first principles.
- **W2 Theorem T4 registered** (3PI → linear limit as r→0). W6-69 verifies against this theorem's Hankel-form closed expression.
- **UNIFIED-AS-79 baseline** (S82-W1, S83-G16) frozen at A_s = 5.08e-9 canonical. W6-67 through W6-70 use this as anchor.
- **S76 modulus decay rate** Gamma_phi ≈ 1.6e-37 s^-1 pinned in canonical_constants.py for W6-50 propagation.
- **G46 r_CMB = 0.0117 frozen** as tensor amplitude anchor for W6-50 absolute-P_t projection.

W6 is independent of W1-W5 gates at compute time. Gates 67-71 can run concurrently with 50-52.

---

## §W6-50. S84-CGWB-ABSOLUTE-PT-PREDICTION

### 1. Gate ID
`S84-CGWB-ABSOLUTE-PT-PREDICTION`

### 2. Trigger
`[CHAIN]` — composite-ledger claim propagating H_tilde^2 prefactor through dS cascade + reheating-equivalent phase + CGWB transfer function to observable Omega_GW(f) at three frequencies.

### 3. Classification
PHONONIC — tensor power descends from the post-fold dS cascade (phonon pair-production spectrum on the substrate background), with reheating-equivalent phase driven by modulus SM decay rate Gamma_phi.

### 4. Agent type
`mack-cosmic-bridge` (observational cosmology projection + detector-sensitivity translation).

### 5. Hypothesis
At LISA / DECIGO / BBO frequencies, the framework predicts absolute tensor power P_t(f) whose value differs between the (A) TD-canonical branch and the (C) mixed-scheme branch by >10x at f ~ 3 mHz, giving a decisive multi-decade GW channel discriminator between the two H_tilde epochs.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: You are NOT computing CGWB "in" a Friedmann spacetime container. The absolute tensor power P_t(f) is the acoustic pair-production signature of the post-fold substrate cascade — phonon pairs on the M^4 x SU(3) fabric whose relay patterns propagate through g_M. The reheating-equivalent phase is NOT reheating in the LCDM sense; it is the Gamma_phi-driven modulus decay into SM relay patterns. The frame rate c bounds the propagation of these GW modes ACROSS the substrate, not the substrate's own dynamics. Invert the direction: D_K eigenvalues → spectral moments → emergent GW spectrum.

Canonical imports:
```python
from canonical_constants import (
    H_TD, H_LI, eps_H, tau_fold, r_CMB, M_KK, planck_ns,
    M_Pl_eff, k_pivot, k_CMB, H0_Planck, c_light,
)
Gamma_phi_modulus = 1.6e-37  # (local) s^-1, S76 modulus SM decay rate; promote to canonical on gate PASS
```

Inputs:
- H_tilde^(TD) branch = H_TD = 5.9076e-3 (canonical, S82 PASS-F2)
- H_tilde^(LI) branch = H_LI = 2.464e-5 (INFO endpoint, 240x smaller)
- H_tilde^(mixed-C) branch = geometric mean sqrt(H_TD * H_LI) = 3.814e-4 (local, used as (C)-branch pivot for discrimination)
- r_CMB = 0.0117 (G46 PASS); r(k_transit) reported from G46 data
- eps_H = 0.02163

Numerical procedure:

1. Absolute tensor power formula (canonical):
   ```
   P_t(k) = (2/pi^2) * (H_tilde(k_transit) / M_Pl_eff)^2 * (k/k_*)^n_t
   ```
   where n_t = +0.4676 BLUE from S83-G50 (transit-scale Bogoliubov tilt). At frequencies spanning LISA through BBO, k >> k_CMB, so the blue tilt strongly amplifies high-f modes.

2. Transfer function from k_transit to f_today. Use post-fold dS cascade → reheating-equivalent phase → CGWB transfer:
   ```
   f(k) = (k / 2pi) * a_transit / a_0
   a_transit / a_0 = (H_tilde / H0_Planck)^(1/2) * (Gamma_phi_modulus / H0_Planck)^(-1/2) * (transfer_correction)
   ```
   transfer_correction grid = {0.5, 1.0, 2.0} as sensitivity bracket. Pin central value at 1.0, report as machinery constant.

3. Evaluate P_t at three frequencies: f1 = 1e-4 Hz (LISA low), f2 = 1e-3 Hz (LISA mid), f3 = 1e-1 Hz (BBO/DECIGO).

4. For each frequency and each branch (A=H_TD, C=geometric-mean, +reference LI=H_LI), compute:
   - P_t(f) absolute value
   - Omega_GW(f) = (2 pi^2 / 3 H0_Planck^2) * f^2 * P_t(f) * (conversion-factor k_f^-3 → f^-3)
   - h_c(f) = sqrt(P_t(f) * f / c_light) (characteristic strain amplitude)

5. Compute log10-ratio rho_AC(f) = log10(Omega_GW^(A) / Omega_GW^(C)) at each frequency. This is the discriminator metric.

6. Compare h_c(f) to LISA strain sensitivity h_LISA(f = 3e-3 Hz) = 1e-21/sqrt(Hz).

GPU note: all computations are scalar; no torch.linalg required.

Cross-checks:
- At f ≈ k_CMB / 2pi, P_t should reproduce the CMB tensor amplitude consistent with r_CMB = 0.0117 to <1% (tensor-spectrum continuity check).
- Omega_GW(f) ≥ 0 at all frequencies (unitarity).
- n_t > 0 blue tilt must produce monotonically-increasing Omega_GW(f) across f ∈ [1e-4, 1e-1] Hz.

Output files:
- Script: `computations/s84_w6_cgwb_absolute_pt.py`
- Data: `computations/s84_w6_cgwb_absolute_pt.npz` (arrays: f_grid, P_t_A, P_t_C, P_t_LI, Omega_GW_A/C/LI, h_c_A/C/LI, rho_AC, rho_AC_sigma_transfer)
- Plot: `computations/s84_w6_cgwb_absolute_pt.png` (top: Omega_GW(f) three branches vs LISA/DECIGO/BBO sensitivity; bottom: rho_AC(f) discriminator)
- Verdict line in `s84_gate_verdicts.txt`:
  `S84-CGWB-ABSOLUTE-PT-PREDICTION: PASS|FAIL|INFO -- value=<max_rho_AC> scheme=<TD-canonical-vs-mixed-C> convention=<transfer_correction=1.0> L_max=<N/A> sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: N/A (scalar computation, no mode-sum)
- scan_range: f_grid = {1e-4, 1e-3, 1e-1} Hz; transfer_correction ∈ {0.5, 1.0, 2.0} sensitivity bracket, central 1.0 pinned
- tolerance: 1% on transfer-continuity check, absolute log10-ratio rho_AC for verdict
- scheme: TD-canonical (A) vs geometric-mean (C); LI reported as endpoint reference only
- convention: transfer_correction = 1.0 pinned; n_t = +0.4676 from G50; r_CMB = 0.0117 from G46
- random_seed: N/A (deterministic)
- GPU path: N/A
- Gamma_phi_modulus = 1.6e-37 s^-1 pinned from S76

### 8. Expected output 4-tuple
`(value=<max_rho_AC over f_grid>, scheme=<TD-vs-mixed-C>, convention=<transfer_correction=1.0>, L_max=<N/A>)`

Prediction: max_rho_AC ≥ 1.0 (≥10x discrimination) at f ~ 3 mHz given H_tilde^2 scaling and (H_TD / sqrt(H_TD*H_LI))^2 = H_TD/H_LI = 240.

### 9. Thresholds
- PASS: max_rho_AC ≥ 1.0 at any f in f_grid AND h_c^(A) > h_LISA at f=3 mHz (detectable AND discriminating)
- FAIL: max_rho_AC < 0.5 across all f_grid (branches indistinguishable at any LISA/DECIGO/BBO frequency)
- INFO: 0.5 ≤ max_rho_AC < 1.0 (discriminable but marginal); OR h_c^(A) < h_LISA at 3 mHz (discrimination exists but below detector floor)

### 10. Substitution chain (mandatory — [CHAIN] trigger)

Claim: "H_tilde^(TD) branch produces Omega_GW at LISA frequencies ≥10x larger than H_tilde^(mixed-C) branch."

Step 1: Define P_t(k) = (2/pi^2) * (H_tilde / M_Pl_eff)^2 * (k/k_*)^n_t [canonical tensor power, Mukhanov-Sasaki]

Step 2: Ratio at fixed k:
```
P_t^(A)(k) / P_t^(C)(k)
= [(H_TD / M_Pl_eff)^2 / (H_mixed / M_Pl_eff)^2] * [(k/k_*)^n_t / (k/k_*)^n_t]
= (H_TD / H_mixed)^2
```

Step 3: Substitute H_mixed = sqrt(H_TD * H_LI):
```
(H_TD / sqrt(H_TD * H_LI))^2 = H_TD / H_LI = 5.9076e-3 / 2.464e-5 = 239.75
```

Step 4: Omega_GW inherits the P_t prefactor directly (proportional):
```
Omega_GW^(A) / Omega_GW^(C) = P_t^(A) / P_t^(C) = 239.75
log10(239.75) = 2.38
```

Step 5: 2.38 >> 1.0 threshold. PASS on discriminator value, CONDITIONAL on h_c^(A) > h_LISA at 3 mHz.

Step 6: h_c^(A) at 3 mHz, with n_t = +0.468 blue tilt, and P_t^(A) anchor ~ r_CMB * P_s / 8 propagated to transit-scale amplitude H_TD^2:
[Compute at runtime; the sign-chain establishes the discriminator direction at 2.38 decades.]

Conclusion: The ratio 240 in H-squared PROPAGATES to ~2.4-decade discrimination in absolute Omega_GW(f) at any tensor-spectrum-consistent frequency. The separate question of whether h_c^(A) exceeds LISA's h ~ 1e-21/sqrt(Hz) is answered by the script's absolute-value computation; only then does the gate PASS vs INFO.

### 11. What PASS / FAIL means for solution space
- **PASS**: LISA/DECIGO/BBO becomes a decisive (A)-vs-(C) branch discriminator. The H_tilde epoch commitment is OBSERVATIONALLY DECIDABLE on a 5-10 year horizon. This promotes S84-W0-REGULATOR-RESOLUTION from framework-internal to detector-testable.
- **FAIL**: Despite H_TD/H_LI = 240 in H-squared, the transfer function suppresses the discrimination below LISA reach — the CGWB channel joins G44 (CMB-S4 sigma_c-cons) as DETECTOR-STERILE. W0-regulator resolution stays framework-internal.
- **INFO**: Discrimination exists but not at >10x; LISA can contribute to but not decisively close (A)/(C).

### 12. Effort estimate
0.5 session. Pure scalar transfer-chain computation, no mode sums or eigenvalue problems. Primary effort is pinning Gamma_phi_modulus provenance and validating the transfer_correction normalization.

### 13. Substrate-framing reminder
Already embedded in §6 method prompt (top). Enforce: no "GW propagating through spacetime"; use "phonon-pair relay patterns on substrate fabric g_M".

---

## §W6-51. S84-SIBLING-OBSERVABLES-COMMON-PREFACTOR

### 1. Gate ID
`S84-SIBLING-OBSERVABLES-COMMON-PREFACTOR`

### 2. Trigger
`[CHAIN]` — composite-ledger enumeration of H_tilde^n exponents across all observables; each exponent is a chain-rule product of CC3 identities.

### 3. Classification
PHONONIC — every observable in the catalog is a spectral moment / spectral bispectrum of the substrate; the common-prefactor structure IS the substrate's CC3 propagation identity acting on the full observable sheet.

### 4. Agent type
`gen-physicist` (observable-family cataloging + cross-observable discriminator design).

### 5. Hypothesis
All framework observables that route through the H_tilde(k_transit) amplitude inherit an H_tilde^n prefactor with EXACTLY-PREDICTED exponent n from CC3/CC-5 propagation; jointly they define a multi-dimensional (A)-vs-(C) branch discriminator richer than the A_s-only or P_t-only channels.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: Observables are spectral moments/functionals of the D_K operator and its Jensen-deformation family. The common-prefactor structure reflects how EACH observable sits in the Mellin-moment atlas. Do NOT explain this via "inflation scaling"; it is substrate CC3 propagation acting on the observable sheet.

Canonical imports:
```python
from canonical_constants import (
    H_TD, H_LI, eps_H, tau_fold, M_Pl_eff, r_CMB, planck_ns,
    alpha_s_MZ_obs, n_s_Planck, k_pivot, k_CMB,
)
```

Procedure:

1. Catalog all framework observables inheriting H_tilde^n. Start with candidates:

   (a) A_s (scalar amplitude) — exponent +2 via A_s ~ H_tilde^2 / (8 pi^2 eps_H M_Pl_eff^2) * F_amp
   (b) P_t absolute (gate W6-50) — exponent +2 via P_t ~ (2/pi^2) * (H_tilde/M_Pl_eff)^2
   (c) n_s (spectral index) — exponent 0 via n_s - 1 = -2eps_H - eta_H + O(sr^2); LOGARITHMIC in H_tilde
   (d) alpha_s = d(n_s)/d(ln k) — exponent 0 (second-order SR); chain-rule inheritance via eta_H running
   (e) n_t (tensor tilt) — exponent 0 (Bogoliubov tilt, Jensen-curvature-locked); structural, not prefactor
   (f) r = P_t/P_s — exponent 0 (cancellation): r = 16 eps_H (standard) or r(k_transit) via G46 transfer
   (g) f_NL (bispectrum amplitude, local shape) — exponent +0 in amplitude but +1 in k-scale ratio; GGE bispectrum
   (h) mu (mu-distortion, FIRAS) — inherits A_s via dissipation; exponent +2
   (i) tau_reio (optical depth) — exponent 0 (astrophysical, not substrate-prefactor)
   (j) S76 alpha_s(CMB) = -0.0143 (mechanism-level S76 prediction) — inherits via eta_H; exponent 0
   (k) dn_s/d(ln k) — exponent 0 (chain rule on log-logarithmic form)
   (l) spectral-index cross-correlations — inherit via chain-rule products

2. For each observable O_i in the catalog, compute d(ln O_i)/d(ln H_tilde) analytically:
   ```
   d(ln A_s)/d(ln H_tilde) = +2
   d(ln P_t)/d(ln H_tilde) = +2
   d(ln n_s)/d(ln H_tilde) = 0 (structural)
   d(ln r)/d(ln H_tilde) = 0 (ratio cancellation)
   d(ln f_NL)/d(ln H_tilde) = ? (GGE bispectrum amplitude analysis)
   d(ln mu)/d(ln H_tilde) = +2 (A_s-inherited, dissipation kernel)
   d(ln (d n_s / d ln k))/d(ln H_tilde) = 0 (second-derivative ratio, LOG form cancellation)
   ```

3. Tabulate results in a "common-prefactor atlas" — one row per observable, columns = (exponent n, H_TD value, H_mixed-C value, ratio A/C in decades, detector reach).

4. Identify multi-D discriminator:
   - Which observables are ≥1 decade different between (A) and (C)? These are exponent ≥0.43 entries.
   - Which are detector-accessible in next 5-10 years? Intersect with: Planck (already), CMB-S4 (~2030), LiteBIRD (~2032), LISA (~2035), SKA-2 (~2030+).

5. Compute the rank-k joint discriminator power: combined sigma on (A)-vs-(C) for k observables, assuming diagonal covariance in observable space.

6. Report: (i) the exponent atlas (table); (ii) the (A)/(C) ratio atlas; (iii) the joint rank-k sigma-reach for k ∈ {2, 3, 5, 10}.

GPU note: scalar tabulation, no torch required.

Cross-checks:
- CC3 identity: sum of exponents across the A_s reconstruction equation = +2 (consistency).
- G46 r_CMB = 0.0117: r ratio should be H_tilde-independent to <1% (prefactor cancellation verification).
- Each exponent checked against d/d(ln H_tilde) numerically by evaluating at H_TD and H_TD*(1+1e-6), finite-differencing.

Output files:
- Script: `computations/s84_w6_sibling_common_prefactor.py`
- Data: `computations/s84_w6_sibling_common_prefactor.npz` (arrays: observable_names, n_exponent_analytic, n_exponent_fd, ratio_AC_log10, detector_reach_years, joint_sigma_k)
- Table: `computations/s84_w6_sibling_common_prefactor.csv` (CSV for atlas table)
- Plot: `computations/s84_w6_sibling_common_prefactor.png` (bar chart of n_exponent per observable + cumulative joint sigma)
- Verdict line:
  `S84-SIBLING-OBSERVABLES-COMMON-PREFACTOR: PASS|FAIL|INFO -- value=<k_obs_above_1decade> scheme=<CC3-propagation> convention=<H_TD-vs-mixed-C> L_max=<N/A> sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: N/A
- scan_range: observable catalog frozen (12 entries above), exponent computation analytic with finite-diff cross-check at delta = 1e-6
- tolerance: |analytic - finite-diff| < 1e-4 per exponent (cross-check)
- scheme: CC3 propagation identity (S82 PASS via CC-RATIOS-ONLY-THEOREM-SG)
- convention: H_TD-vs-mixed-C as primary discriminator pair; LI as endpoint reference
- random_seed: N/A
- GPU path: N/A

### 8. Expected output 4-tuple
`(value=<number_of_observables_with_|n|≥1>, scheme=<CC3-propagation>, convention=<H_TD-vs-mixed-C>, L_max=<N/A>)`

Prediction: k_obs_above_1decade ≥ 3 (A_s, P_t, mu at minimum).

### 9. Thresholds
- PASS: ≥3 observables with |n| ≥ 1 AND at least 2 observables in the atlas reachable within 2035 detector horizon (A_s PASS via Planck already, P_t PASS via LISA if W6-50 PASSes, mu PASS via PIXIE-class ≥ 2035)
- FAIL: 0 observables with |n| ≥ 1 (structural cancellation across the board — catastrophic for H_tilde-branch discrimination)
- INFO: 1-2 observables with |n| ≥ 1 (narrow channel); OR ≥3 but none detector-accessible before 2045

### 10. Substitution chain

Not required for [CHAIN] catalog gates without sign/direction claim. Each row of the atlas is its own sub-derivation, with the analytic exponent being the claim and the finite-difference cross-check being the verification — both printed to stdout.

For the joint discriminator claim: "k_obs ≥ 3 gives at least a 2-decade advantage in the joint sigma over A_s-alone", the chain is:
```
Step 1: joint_sigma_k^-2 = sum_i (n_i^2 / sigma_H,i^2) where sigma_H,i is the per-observable error on ln H_tilde from O_i alone.
Step 2: For k=3 with all |n_i|=2 and comparable sigma_H,i: joint_sigma = sigma_single / sqrt(3). Sensitivity gain = sqrt(3) ≈ 0.24 decade factor.
Step 3: Across k=12 candidates with mixed |n_i|, effective gain is ≥1 decade IF at least 3 channels have |n|=2 AND are detector-accessible.
Conclusion: the claim reduces to counting H_tilde^2-prefactor-carrying observables; the atlas delivers this count.
```

### 11. What PASS / FAIL means for solution space
- **PASS**: Multi-dimensional (A)/(C) discriminator established. Framework branch-ambiguity becomes empirically tractable via N-channel consistency test.
- **FAIL**: H_tilde-branch is under-determined observationally — framework internal degeneracy persists.
- **INFO**: Partial discrimination via A_s/mu only; LISA depends on W6-50 verdict.

### 12. Effort estimate
0.5 session. Analytic exponent tabulation + finite-diff cross-check. Primary effort is forecast-literature cross-reference for detector reach column.

### 13. Substrate-framing reminder
Observables are spectral moments of D_K; the common-prefactor structure IS CC3 propagation on the observable sheet, not a "Friedmann factor". Substrate first.

---

## §W6-52. S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT

### 1. Gate ID
`S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT`

### 2. Trigger
`[VERIFY]` — refresh of quantitative discriminator figure against external forecast literature; PASS/FAIL within factor 3 of historical 34σ claim.

### 3. Classification
PHONONIC — alpha_s = n_s^2 - 1 is a spectral-moment relationship (S50 permanent) on the post-fold GGE acoustic-optical pair spectrum. Refining the detector-reach figure is an observational-framing question, but the underlying observable is phononic.

### 4. Agent type
`mack-cosmic-bridge` (CMB forecast literature synthesis + joint-detector reach projection).

### 5. Hypothesis
CMB-S4 projected sensitivity sigma(alpha_s) ≈ 0.002 stands against Abazajian 2022+ forecasts; framework zero-parameter prediction alpha_s = n_s^2 - 1 = -0.068968 delivers ≥30σ discrimination against LCDM alpha_s = 0 baseline at full S4 survey; CMB-HD and LiteBIRD are viable alternate/complementary channels.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: alpha_s = n_s^2 - 1 is a SPECTRAL MOMENT RELATIONSHIP (S50 permanent) — the "running of the spectral index" IS substrate substructure speaking through the GGE acoustic-optical pair spectrum, not a Friedmann evolution. When reading Abazajian et al., translate their "inflation running" to "Mellin-moment evolution on the post-fold substrate".

Canonical imports:
```python
from canonical_constants import (
    alpha_s_MZ_obs, n_s_Planck, planck_ns, eps_H,
)
alpha_s_framework = -0.068968  # (local) S50 permanent; from n_s^2 - 1 at n_s=0.9653
```

Procedure:

1. Literature gather (use mcp__paper-search__search_arxiv if available):
   - Abazajian et al. 2019 "CMB-S4 Science Book" — forecast sigma(alpha_s) baseline
   - Abazajian 2022 update if available
   - CMB-HD Sehgal et al. 2019 "CMB-HD: An Ultra-Deep, High-Resolution Millimeter-Wave Survey"
   - LiteBIRD Hazumi et al. 2020 concept paper — alpha_s forecasts
   - Simons Observatory Ade et al. 2019 — SO+S4 joint projections
   Cite each with arXiv ID and year. Extract the quoted sigma(alpha_s) and the survey baseline (fsky, years, frequency bands).

2. Cross-compare each forecast:
   - CMB-S4 baseline: sigma(alpha_s) = ? (target ~0.002)
   - CMB-S4 + delensing: sigma(alpha_s) = ?
   - CMB-HD: sigma(alpha_s) = ?
   - LiteBIRD: sigma(alpha_s) = ?
   - SO/S4 joint: sigma(alpha_s) = ?

3. Compute sigma-discrimination factor per detector:
   ```
   discrimination_sigma_i = |alpha_s_framework - 0| / sigma(alpha_s)_i = 0.068968 / sigma_i
   ```
   Expected: CMB-S4 gives 0.069 / 0.002 = 34.5σ.

4. Joint detector reach if CMB-S4 + LiteBIRD + CMB-HD combine. Assume uncorrelated forecasts (weak assumption, stated explicitly).

5. Compare to the S83 G44 CMB-S4 DETECTOR-STERILE verdict on sigma_c-cons. alpha_s and sigma_c-cons are distinct observables — alpha_s should NOT inherit G44's sterility.

6. Report:
   - Table: {detector, sigma(alpha_s), discrimination sigma, year-of-first-data}
   - Does the 34σ figure survive? (PASS if ≥30σ on CMB-S4 alone)
   - Alternate channels in case CMB-S4 is delayed: CMB-HD, LiteBIRD reach?

GPU note: N/A.

Cross-checks:
- alpha_s_framework = -0.068968 consistent with n_s^2 - 1 at n_s = 0.9653 (Planck central).
- Derived sigma(alpha_s) from each forecast consistent with per-paper figures to <10%.
- The S50 zero-parameter derivation: verify by independent check `0.9653^2 - 1 = -0.0684` (approximate match given n_s rounding).

Output files:
- Script: `computations/s84_w6_alpha_s_cmb_s4_refinement.py`
- Data: `computations/s84_w6_alpha_s_cmb_s4_refinement.npz` (arrays: detector_names, sigma_alpha_s, discrimination_sigma, year_first_data, reference_arxiv)
- Table: `computations/s84_w6_alpha_s_cmb_s4_refinement.csv`
- Verdict line:
  `S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT: PASS|FAIL|INFO -- value=<best_discrimination_sigma> scheme=<Abazajian+2022+> convention=<alpha_s=n_s^2-1> L_max=<N/A> sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: N/A
- scan_range: detector list = {CMB-S4, CMB-S4+delensing, CMB-HD, LiteBIRD, SO/S4-joint}
- tolerance: 10% on per-detector sigma(alpha_s) reading from source papers
- scheme: canonical sigma = sqrt(Fisher^-1) as reported in source forecasts
- convention: alpha_s = n_s^2 - 1 from S50 permanent, with n_s = 0.9653 Planck-central; alternative convention alpha_s = d n_s / d ln k central check at k_pivot
- random_seed: N/A
- GPU path: N/A

### 8. Expected output 4-tuple
`(value=<max_discrimination_sigma>, scheme=<Abazajian+2022+>, convention=<alpha_s=n_s^2-1>, L_max=<N/A>)`

Prediction: max_discrimination_sigma ≥ 30 on CMB-S4 alone; joint-detector ≥ 40σ.

### 9. Thresholds
- PASS: CMB-S4 alone gives ≥30σ discrimination AND at least one alternate (CMB-HD or LiteBIRD) gives ≥10σ (robust channel)
- FAIL: All detectors give <10σ (alpha_s becomes DETECTOR-STERILE — S50 becomes observationally inaccessible until 2040+)
- INFO: CMB-S4 gives 10-30σ or alternate channels give <10σ (single-detector dependency; not robust)

### 10. Substitution chain

Claim: "CMB-S4 gives ≥30σ discrimination of alpha_s_framework = -0.069 against LCDM alpha_s = 0."

Step 1: Define discrimination = |alpha_s_framework - alpha_s_LCDM| / sigma(alpha_s).

Step 2: alpha_s_framework - alpha_s_LCDM = 0.068968 - 0 = 0.068968.

Step 3: sigma(alpha_s)_CMB-S4 ≈ 0.002 (Abazajian+ 2019 CMB-S4 Science Book forecast).

Step 4: discrimination = 0.068968 / 0.002 = 34.5σ.

Step 5: 34.5 > 30 threshold. PASS conditional on sigma = 0.002 surviving 2022+ updates.

Conclusion: The 34σ figure stands if and only if the sigma = 0.002 forecast is stable. The gate's PASS-condition reduces to literature verification.

### 11. What PASS / FAIL means for solution space
- **PASS**: alpha_s = n_s^2 - 1 (S50 permanent) becomes the framework's strongest single-observable discriminator vs LCDM on a ~2030 horizon. Robust to CMB-HD / LiteBIRD as alternates.
- **FAIL**: Abazajian 2022+ revises sigma(alpha_s) upward by >15x → S50 observational closure delays to 2040+. Would trigger re-prioritization of S76 alpha_s(CMB) = -0.0143 as the nearer-term channel.
- **INFO**: Mixed result: CMB-S4 alone marginal, but CMB-HD or LiteBIRD compensates. Still PASS for framework but detection hinges on specific detector.

### 12. Effort estimate
0.5 session. Primarily literature synthesis + sigma-bookkeeping. Dispatch includes arxiv search; agent uses mcp__paper-search tools.

### 13. Substrate-framing reminder
alpha_s is a spectral-moment property of the substrate, not an "inflation running parameter". Translate all external forecasts into the Mellin-evolution picture when reporting.

---

## §W6-67. S84-Z-R-COUNTERTERM-EXISTENCE

### 1. Gate ID
`S84-Z-R-COUNTERTERM-EXISTENCE`

### 2. Trigger
`[VERIFY-THEOREM]` — theorem-level claim about existence of multiplicative renormalization constant Z_R.

### 3. Classification
GEOMETRIC — Seeley-DeWitt heat-kernel expansion is a geometric property of the spectral triple; counterterm Z_R consistency is a field-theoretic dressing on that geometric structure.

### 4. Agent type
`feynman-theorist` (counterterm / renormalization theorem construction + heat-kernel matching).

### 5. Hypothesis
A multiplicative renormalization factor Z_R(lambda_cut) exists such that Z_R * f_conv^R = const is cluster-invariant across all 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR}; this converts f_conv from S83-G28-FAIL clause-(a)-unbalanced (cluster=1766) to a balanced ratio at the single Mellin label k=0, restoring renormalizability at the field-theory level.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: f_conv = pi^4 / (9216 * M_0^2) is the Seeley-DeWitt expansion coefficient at the k=0 tadpole slot. The question "does a Z_R counterterm exist?" is a FIELD-THEORY-DRESSING question on a substrate structure. The substrate is fixed; the dressing (regulator) varies. Do NOT explain this as "UV divergence in an EFT over spacetime" — the spectral action heat-kernel IS the field-theory on the substrate.

Canonical imports:
```python
from canonical_constants import (
    M_KK, tau_fold, Vol_SU3, eps_H,
    # f_conv constants expected from S83 atlas — promote if missing
)
import torch
f_conv_k0 = 3.141592653589793**4 / 9216  # (local) divided by M_0^2 per-regulator
```

Procedure:

1. For each of 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR}, compute f_conv^R(L_max=5) using existing S83-G28 machinery (the f_conv cluster-test script). This reproduces the 5-regulator values from which the span=1766 was derived.

2. Compute Seeley-DeWitt heat-kernel expansion a_0, a_2, a_4 coefficients for the same 5 regulators. The heat-kernel expansion is:
   ```
   Tr(exp(-t D_K^2)) = sum_k a_k(D_K) t^(k-2) / (4 pi)^2
   ```
   Each regulator's a_k is a well-defined spectral moment; they differ across regulators due to measure-dependent treatment of the UV tail.

3. For each regulator R, solve for Z_R such that:
   ```
   Z_R * f_conv^R = C (constant across R)
   ```
   Choose C = mean{f_conv^R * a_2^R / a_2^zeta} as the reference normalization (zeta is the canonical axiomatic layer per S83-G3).

4. Compute Z_R for each regulator:
   ```
   Z_R = C / f_conv^R
   Z_R * f_conv^R = C (by construction per-row; the TEST is whether the Z_R values are consistent with spectral-action RG flow)
   ```

5. Spectral-action RG consistency: The Z_R's must satisfy the RG-equation:
   ```
   d(ln Z_R) / d(ln lambda_cut) = -beta_spectral-action(lambda_cut) / f_conv^R
   ```
   For Z_R to be a true counterterm (not an ad-hoc rescaling), the 5 Z_R values at lambda_cut = Lambda_Z canonical must satisfy a linear relation with the 5 heat-kernel a_2^R values within factor-1.5.

6. Compute the span of (Z_R * f_conv^R) after normalization:
   ```
   cluster_Zf = max_R(Z_R * f_conv^R) / min_R(Z_R * f_conv^R)
   ```
   By construction this should be 1.0 if Z_R is a pure rescaling; the TEST is whether the SAME Z_R that rescales f_conv also rescales a_2 consistently.

7. Report:
   - Z_R table per regulator
   - cluster_Zf after rescaling (should be 1.0)
   - cluster_Z_a2: span of (Z_R * a_2^R) — this is the ACTUAL test. If <1.5, counterterm is multiplicatively consistent.
   - PASS/FAIL on cluster_Z_a2.

GPU note: heat-kernel a_k values use the existing D_K eigenvalue cache (L_max=5, 52,625 eigenvalues). torch.linalg.eigvalsh on the 155,984 x 155,984 D_K matrix at L_max=10 is NOT required for this gate (L_max=5 suffices, 5258x5258 matrix — use torch GPU).

Cross-checks:
- In the zeta regulator (axiomatic layer L1), Z_zeta should = 1.0 by definition (Z is multiplicative, zeta is the reference).
- The dim-reg regulator, if the gate is to be meaningful, should give Z_dim-reg finite (no 1/epsilon pole at this order — this IS the renormalizability check).
- Heat-kernel a_2^R independent computation via direct spectral-moment integration; cross-check to within 5%.

Output files:
- Script: `computations/s84_w6_z_r_counterterm.py`
- Data: `computations/s84_w6_z_r_counterterm.npz` (arrays: regulator_names, f_conv_R, a_2_R, Z_R, cluster_Zf, cluster_Z_a2)
- Plot: `computations/s84_w6_z_r_counterterm.png` (bar chart: f_conv^R pre/post-Z rescaling; overlay a_2^R pre/post)
- Verdict line:
  `S84-Z-R-COUNTERTERM-EXISTENCE: PASS|FAIL|INFO -- value=<cluster_Z_a2> scheme=<zeta-reference> convention=<heat-kernel-matching> L_max=5 sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: 5 (D_K eigenvalue cache; 5258 x 5258 matrix via torch.linalg on GPU)
- scan_range: 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR}; lambda_cut = Lambda_Z canonical from S83
- tolerance: 5% on heat-kernel a_2^R cross-check; 1e-10 numerical precision on Z_R solve
- scheme: zeta as Z=1 reference (axiomatic L1 layer)
- convention: heat-kernel matching at lambda_cut = Lambda_Z; spectral-action RG beta from S80 framework-archive (promote to canonical if stable)
- random_seed: N/A (deterministic eigenvalue solve)
- GPU path: `torch.linalg.eigvalsh` on D_K at L_max=5 (~50MB GPU memory; well within 17.1 GB VRAM budget)

### 8. Expected output 4-tuple
`(value=<cluster_Z_a2>, scheme=<zeta-reference>, convention=<heat-kernel-matching>, L_max=5)`

Prediction: cluster_Z_a2 ∈ [1.0, 1.5] — if the Seeley-DeWitt a_2 is regulator-independent at leading order (spectral action theorem), the rescaling Z_R that cancels f_conv span ALSO cancels a_2 span, confirming multiplicative consistency.

### 9. Thresholds
- PASS: cluster_Z_a2 < 1.5 (multiplicative counterterm exists, Z_R * f_conv^R and Z_R * a_2^R both balanced)
- FAIL: cluster_Z_a2 ≥ 2.5 (Z_R is regulator-specific, NOT a true counterterm; f_conv remains NOT-R-protected even after dressing)
- INFO: 1.5 ≤ cluster_Z_a2 < 2.5 (marginal; counterterm exists but renormalization is scheme-dependent in a nontrivial way — triggers escalation to 2-loop)

### 10. Substitution chain (mandatory — [VERIFY-THEOREM])

Claim: "Z_R * f_conv^R balanced ⇒ f_conv becomes R-protected at a single Mellin label k=0."

Step 1: f_conv^R(L_max=5) is the k=0 Mellin-moment coefficient of heat-kernel expansion per regulator.

Step 2: f_conv = pi^4 / (9216 * M_0^2^R) — the M_0^R (regulator-dependent mass-scale) is what varies across R.

Step 3: Z_R = M_0^zeta^2 / M_0^R^2 (by construction, to equate f_conv^R * Z_R = f_conv^zeta).

Step 4: a_2^R = spectral moment int trace(D_K^2 * exp(-t D_K^2))|_{t=0^+ regularized, R} = a_2^zeta * M_0^zeta^2 / M_0^R^2 + delta_a2^R.

Step 5: Z_R * a_2^R = M_0^zeta^2 / M_0^R^2 * (a_2^zeta * M_0^zeta^2 / M_0^R^2 + delta_a2^R) = a_2^zeta + Z_R * delta_a2^R.

Step 6: cluster_Z_a2 = max(Z_R * a_2^R) / min(Z_R * a_2^R) = a_2^zeta * (1 + max_R(Z_R * delta_a2^R / a_2^zeta)) / a_2^zeta * (1 + min_R(Z_R * delta_a2^R / a_2^zeta)).

Step 7: If delta_a2^R is SUBLEADING (i.e., the spectral-action theorem's a_2 is regulator-independent at leading order), then max-min ratio ≈ 1 and cluster_Z_a2 ≈ 1. PASS.

Step 8: If delta_a2^R is LEADING (a_2 has regulator-dependent sub-coefficient), cluster_Z_a2 can grow beyond 1.5. FAIL.

Conclusion: The gate IS a test of whether a_2 is truly the geometric invariant (Connes-Chamseddine theorem) or whether there is a regulator-specific correction at the L_max=5 truncation. Either way is informative.

### 11. What PASS / FAIL means for solution space
- **PASS**: f_conv becomes R-protected at k=0 AFTER the Z_R dressing. The S83-G28 cluster=1766 result does NOT reflect a structural regulator problem; it reflects an un-dressed f_conv. Counterterm dressing moves f_conv into the R-protected atlas (W6-68). Renormalizability at the spectral-action level preserved.
- **FAIL**: Z_R cancellation of f_conv does NOT extend to a_2. f_conv is intrinsically NOT-R-protected even after multiplicative dressing. Heat-kernel cluster-failure is a TRUE regulator obstruction, not a dressing artifact. Framework must accept that f_conv is a physical scheme-dependence (scheme-dependent falsifier class in G48).
- **INFO**: Marginal; triggers NNLO counterterm investigation in S85.

### 12. Effort estimate
1 session. Requires heat-kernel a_2^R computation for 5 regulators at L_max=5, plus Z_R solve and cluster-check. Eigenvalue cache from S83 reusable; new work is the a_2^R / regulator-matching code.

### 13. Substrate-framing reminder
f_conv is a SPECTRAL MOMENT of D_K, not a "UV coupling in some spacetime EFT". The heat-kernel expansion is the substrate's internal structure speaking. Z_R is the dressing factor that makes the spectral-moment representation basis-independent.

---

## §W6-68. S84-R-PROTECTED-ATLAS-COMPLETENESS

### 1. Gate ID
`S84-R-PROTECTED-ATLAS-COMPLETENESS`

### 2. Trigger
`[VERIFY]` — factor-1.5 cluster check across the enumerated atlas; PASS/FAIL within factor 3 of threshold.

### 3. Classification
GEOMETRIC — R-protected atlas is a geometric structure: the set of observables that are dimensionless ratios of spectral moments at matching Mellin label. This is a classification statement on the Mellin-moment lattice of D_K.

### 4. Agent type
`feynman-theorist` (observable classification + balanced-ratio enumeration + cluster-test dispatch).

### 5. Hypothesis
Every framework observable claimed to be an R-protected balanced dimensionless ratio (numerator and denominator at same Mellin label k) passes the factor-1.5 cluster-test across 5 regulators; no observable in the claimed-balanced class exceeds cluster=1.5; and at least 2 new entries at k=2 extend the atlas.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: The R-protected atlas IS the balanced-Mellin-label sub-lattice of the spectral-moment lattice. The test of "balanced ratio" is not about "dimensional analysis in some ambient EFT" — it is about the equality of Mellin k-labels on the substrate's spectral-moment generating function.

Canonical imports:
```python
from canonical_constants import (
    M_KK, tau_fold, Vol_SU3, eps_H, c_s,
)
import torch
```

Procedure:

1. Enumerate R-protected observables with CLAIMED Mellin-balance:
   - c_s (sound speed, G14 span=1.227) — claimed balance at k=0: (a_0^R / a_0^R)^0.5 slot
   - alpha_SDW^NLO (NLO spectral-action running, G26 span=1.053) — claimed balance at k=2: a_2^R / a_2^R
   - R-family: a_{k-1} * a_{k+1} / a_k^2 at k ∈ {1, 2, 3} — claimed balance at k: numerator k, denominator k
   - chi_2 (S83 new balanced ratio) — claimed balance at k=2, <3.6% span
   - F_amp^3PI at pivot (G35 span=0.0037 NNLO) — linear limit is R-protected; NNLO clause-(b) FI

   Plus new entries at k=2:
   - Jensen coupling g2/g3 ratio — CLAIMED balance at k=2: second spectral moment ratio
   - S83 new "two-slot at k=2" entry (from G61 MIXED sub-tag ledger if any row landed)

2. For each atlas entry O_i:
   a. Pre-declare: numerator Mellin label k_num, denominator Mellin label k_den. REQUIRE k_num == k_den (balance condition).
   b. Compute O_i across 5 regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR}.
   c. Compute cluster_i = max_R(O_i^R) / min_R(O_i^R).
   d. Classify:
      - cluster_i < 1.5 → "R-protected passes"
      - 1.5 ≤ cluster_i < 2.5 → "marginal"
      - cluster_i ≥ 2.5 → "R-protected violates" (membership claim false)

3. For any entry with cluster ≥ 1.5 DESPITE claimed balance, diagnose:
   - Is the Mellin-balance claim correct?
   - Are there subleading mixed terms breaking balance?
   - Report as "CLAIMED-BALANCED-ATLAS-VIOLATION" and flag for S85 audit.

4. For NEW atlas candidates at k=2: compute cluster and report PASS/FAIL per entry.

5. Composite PASS rule: EVERY entry with claimed Mellin-balance passes factor-1.5 AND at least 2 new k=2 entries extend the atlas successfully.

GPU note: each entry reuses the existing D_K eigenvalue cache at L_max=5 (10,000-50,000 eigenvalues). Cluster computations are scalar per regulator; no matrix operations on large matrices.

Cross-checks:
- G14 c_s span=1.227 must REPRODUCE from this script to <1% (reproducibility anchor).
- G26 alpha_SDW^NLO span=1.053 must REPRODUCE from this script to <1%.
- CC-5 identity: for balanced ratios, cluster(O) ≈ cluster(F_num) / cluster(F_den) ≈ 1 when labels match; verify numerically.

Output files:
- Script: `computations/s84_w6_r_protected_atlas_completeness.py`
- Data: `computations/s84_w6_r_protected_atlas_completeness.npz` (arrays: atlas_names, k_num, k_den, claimed_balanced, cluster_measured, cluster_verdict, new_k2_entries)
- Table: `computations/s84_w6_r_protected_atlas_completeness.csv`
- Plot: `computations/s84_w6_r_protected_atlas_completeness.png` (horizontal bar chart of cluster per entry with threshold lines at 1.5 and 2.5)
- Verdict line:
  `S84-R-PROTECTED-ATLAS-COMPLETENESS: PASS|FAIL|INFO -- value=<max_cluster_among_claimed-balanced> scheme=<Mellin-label-balanced> convention=<5-regulator> L_max=5 sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: 5 (eigenvalue cache)
- scan_range: atlas entries = {c_s, alpha_SDW^NLO, R-family-k1, R-family-k2, R-family-k3, chi_2, F_amp^3PI-linear-limit, g2/g3-k2, new-k2-candidates}; 5 regulators per entry
- tolerance: 1% reproducibility against G14/G26 priors; 1e-6 numerical precision on cluster ratio
- scheme: 5-regulator {zeta, Zubarev, SDW, dim-reg, lattice-BR}
- convention: Mellin-label pre-declared for every entry before scan; report in manifest
- random_seed: N/A
- GPU path: `torch.linalg` for eigenvalue dependencies in atlas computation; cache reuse from S83

### 8. Expected output 4-tuple
`(value=<max_cluster_among_claimed-balanced>, scheme=<Mellin-label-balanced>, convention=<5-regulator>, L_max=5)`

Prediction: max_cluster ∈ [1.05, 1.3] — consistent with G14 (1.23) and G26 (1.05) priors; new k=2 entries predicted to cluster at ~1.1.

### 9. Thresholds
- PASS: max_cluster_among_claimed-balanced < 1.5 AND at least 2 new k=2 entries PASS
- FAIL: any entry with claimed Mellin-balance has cluster ≥ 2.5 (membership violation)
- INFO: max_cluster ∈ [1.5, 2.5] OR fewer than 2 new k=2 entries PASS (incomplete extension)

### 10. Substitution chain

Claim: "Claimed-balanced entries cluster <1.5 across regulators."

Step 1: For entry O = f_num^R(k) / f_den^R(k) with CLAIMED k_num = k_den = k (balance condition):

Step 2: Each f_slot^R(k) varies across regulators by factor span(slot, R) = max_R(f_slot^R) / min_R(f_slot^R).

Step 3: By CC-5 propagation identity: cluster(O) = span(f_num)^1 * span(f_den)^(-1).

Step 4: If k_num = k_den = k, then span(f_num) = span(f_den) = span(k) (same slot, same moment). So cluster(O) = span(k) / span(k) = 1.0.

Step 5: Real-world measurement cluster ≈ 1 + O(epsilon^R) where epsilon^R is the regulator-specific finite-truncation correction at L_max=5.

Step 6: For L_max=5 and typical epsilon^R < 0.2, cluster ≈ 1.05 to 1.3. Empirical G14 and G26 consistent.

Step 7: Therefore cluster < 1.5 follows from balance condition UP TO truncation corrections.

Conclusion: PASS is structurally expected from CC-5; FAIL would indicate unpredicted L_max-truncation effect OR that the balance claim was spurious.

### 11. What PASS / FAIL means for solution space
- **PASS**: R-protected atlas is COMPLETE and CORRECT. All claims in the S83 classification survive. The meta-principle §VII.K-META (R-protected ≤1.5 / NOT-R ≥2.5) is validated on extended atlas. Framework renormalization sheet is consistent.
- **FAIL**: One or more claimed-balanced observables have cluster ≥2.5 — the R-protected atlas has a false member. Classification error; S85 must identify and correct.
- **INFO**: Marginal entries (1.5-2.5 cluster) suggest sub-leading mixed terms; atlas incomplete at NLO.

### 12. Effort estimate
1 session. Atlas enumeration + 5-regulator scan per entry. Heavy eigenvalue work reused from S83 cache.

### 13. Substrate-framing reminder
Balanced ratios are Mellin-moment equalities on the substrate spectral-lattice. "R-protection" is the substrate's guarantee that ratio observables are scheme-independent at leading order because BOTH slots sample the same moment of D_K.

---

## §W6-69. S84-F-AMP-3PI-FI-CHAIN

### 1. Gate ID
`S84-F-AMP-3PI-FI-CHAIN`

### 2. Trigger
`[VERIFY-THEOREM]` — theorem-level claim about the clause (b) applicability of F_amp^3PI under Berges-Serreau 3PI action.

### 3. Classification
PHONONIC — F_amp^3PI is the 3-particle-irreducible amplitude on the Mukhanov-Sasaki scalar-perturbation mode function, which is a substrate phonon-pair-creation observable. The FI-chain proof is a field-theoretic derivation on this phononic amplitude.

### 4. Agent type
`feynman-theorist` (Mukhanov-Sasaki substitution chain + 3PI clause-(b) theorem construction).

### 5. Hypothesis
Clause (b) of the CC-5 propagation identity applies to F_amp^3PI at pivot N_pivot=64.08: z_R rescaling cancels in the Mukhanov-Sasaki output ratio A_s ~ H^2 / (eps_H * M_Pl_eff^2 * z^2) when all regulator factors grouped consistently; and W2 Theorem T4 (3PI limit to linear as r → 0) holds against closed-form Hankel at eps_H=0.02163 with residual < 1%.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: F_amp^3PI is the Berges-Serreau 3-particle-irreducible amplitude on the Mukhanov-Sasaki phonon-pair mode. The clause-(b) FI status is a FIELD-THEORETIC CANCELLATION property. You are NOT proving "inflation amplitude is renormalizable"; you are proving the CC-5 propagation identity's clause (b) applies to a substrate phonon amplitude.

Canonical imports:
```python
from canonical_constants import (
    H_TD, eps_H, tau_fold, M_Pl_eff, k_pivot, N_pivot,  # N_pivot=64.0819
)
F_amp_3PI_pivot_L3 = 47.92  # (local) S82 W3-5 PASS at L_max=3
F_amp_lin_pivot = 1.026  # (local) S83 G7 CC7-DYNAMICAL PASS
```

Procedure:

1. Explicit Mukhanov-Sasaki substitution chain:

   Step 1. Define canonical Mukhanov-Sasaki equation for scalar perturbation v_k:
   ```
   v''_k + (k^2 - z''/z) v_k = 0
   ```
   where z = a * sqrt(2 * eps_H) * M_Pl_eff.

   Step 2. Scalar power spectrum:
   ```
   P_s(k) = |v_k|^2 / z^2
   ```

   Step 3. Under regulator R, the effective z_R is:
   ```
   z_R(k) = a(k) * sqrt(2 * eps_H) * M_Pl_eff^R(k)
   ```
   where M_Pl_eff^R is the regulator-dependent Planck mass.

   Step 4. A_s(pivot) ~ P_s(k_pivot) * F_amp^3PI(pivot), where F_amp^3PI is the 3PI resummation of the Mukhanov-Sasaki amplitude at pivot.

   Step 5. A_s ratio between regulators:
   ```
   A_s^R / A_s^zeta
   = [P_s^R(pivot) * F_amp^3PI^R(pivot)] / [P_s^zeta(pivot) * F_amp^3PI^zeta(pivot)]
   = [|v^R|^2/z_R^2 * F^R] / [|v^zeta|^2/z_zeta^2 * F^zeta]
   ```

   Step 6. Clause (b) assertion: F_amp^3PI^R / F_amp^3PI^zeta and z_R^2 / z_zeta^2 are EACH regulator-dependent, but their PRODUCT cancels consistently.

   Step 7. Specifically, F_amp^3PI^R contains factors of z_R^(−2) from the Mukhanov normalization embedded in the 3PI self-energy; these cancel the explicit z_R^2 when grouped.

   Step 8. Net ratio: A_s^R / A_s^zeta ~ [spectrum-part] / [spectrum-part] * O(1), with the spectrum-part being balanced in numerator and denominator at the SAME Mellin label k = k_pivot.

   Step 9. Conclusion: F_amp^3PI is a clause-(b) bounded-range mode-equation output → FI (Feynman-Invariant).

2. Verify numerically. Compute F_amp^3PI^R(pivot) for 5 regulators at L_max=3 AND its ratio to F_amp_lin_pivot = 1.026.

3. Verify W2 Theorem T4: In the limit r → 0 (tensor-to-scalar ratio small), F_amp^3PI(pivot) should approach F_amp_lin(pivot). Use closed-form Hankel function H_nu^(1)(k tau) at eps_H = 0.02163, with nu = 3/2 + eps_H:
   ```
   F_amp_Hankel(eps_H) = |H_nu^(1)(x)|^2 at x = k/aH(1+eps_H)
   ```
   Compare F_amp^3PI(pivot) - F_amp_Hankel(eps_H); report residual as |F_amp_3PI(pivot, L_max=3) - F_amp_Hankel(eps_H)| / F_amp_Hankel.

4. Confirm F_amp^3PI(pivot) = 47.92 from S82 W3-5. Hankel prediction at eps_H=0.02163, nu=1.52163: F_amp_Hankel ≈ O(1-10) depending on normalization. The NORMALIZATION is the key: the T4 theorem holds in the LIMIT, not at finite r.

5. Report:
   - Explicit substitution chain (prose) with every equation numbered
   - Numerical verification table: {regulator, F_amp^3PI^R(pivot, L=3), z_R^2 / z_zeta^2, product ratio}
   - T4-theorem residual: |F_amp_3PI - F_amp_Hankel| / F_amp_Hankel
   - Clause (b) verdict: PASS/FAIL

GPU note: Hankel function evaluation is scalar (use scipy.special.hankel1). Mukhanov solver (if re-running) uses existing S82 framework; no new eigenvalue work.

Cross-checks:
- G35 NNLO-1/N-CONVERGENCE = 0.0037 (PASS) implies F_amp^3PI is expansion-convergent at 1/N_gauge. Clause (b) + 1/N convergence jointly imply the full amplitude is renormalizable.
- CC3 identity: A_s exponent +2 in H_tilde. Verify the substitution chain's H_tilde^2 prefactor emerges correctly from z_R^2 cancellation pattern.
- At eps_H → 0 limit, F_amp_Hankel → 1 exactly (slow-roll flat limit). Verify numerically.

Output files:
- Script: `computations/s84_w6_f_amp_3pi_fi_chain.py`
- Data: `computations/s84_w6_f_amp_3pi_fi_chain.npz` (arrays: regulator_names, F_amp_3PI_R, z_R_sq_ratio, product_ratio, hankel_residual)
- Proof document (prose): embedded in script's docstring with 9-step substitution chain
- Plot: `computations/s84_w6_f_amp_3pi_fi_chain.png` (log-scale F_amp^3PI ratio per regulator with clause-(b) cancellation visualized)
- Verdict line:
  `S84-F-AMP-3PI-FI-CHAIN: PASS|FAIL|INFO -- value=<hankel_residual> scheme=<Berges-Serreau-3PI> convention=<clause-b-FI> L_max=3 sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: 3 (F_amp^3PI convergence already at NNLO per G35)
- scan_range: 5 regulators; eps_H ∈ {0.01, 0.02163, 0.05} sensitivity bracket on T4 theorem
- tolerance: residual on T4 < 1% for PASS; cancellation consistency 5%; algebraic substitution verified step-by-step
- scheme: Berges-Serreau 3PI action at 2PI-level truncation
- convention: clause (b) of CC-5 propagation identity; A_s reconstruction via H^2 / (eps_H M_Pl^2 z^2) * F_amp
- random_seed: N/A
- GPU path: N/A (scalar + special-function)

### 8. Expected output 4-tuple
`(value=<hankel_residual>, scheme=<Berges-Serreau-3PI>, convention=<clause-b-FI>, L_max=3)`

Prediction: residual < 0.01 (T4 holds at 1%); clause (b) PASS.

### 9. Thresholds
- PASS: hankel_residual < 0.01 AND clause-(b) cancellation product_ratio <1.5 across regulators (F_amp^3PI is FI)
- FAIL: hankel_residual ≥ 0.1 OR clause-(b) product_ratio ≥2.5 (clause (b) does NOT apply to F_amp^3PI — the CC-5 identity is restricted)
- INFO: 0.01 ≤ residual < 0.1 or 1.5 ≤ product_ratio < 2.5 (subleading corrections; T4 holds only at leading order)

### 10. Substitution chain (mandatory — [VERIFY-THEOREM])

Complete chain given in §6 step-by-step. Summary:

Step A: A_s = H^2/(8 pi^2 eps_H M_Pl^2) * F_amp^3PI with explicit z^2 in P_s = |v|^2/z^2.

Step B: Under regulator R, z_R^2 = z_zeta^2 * (M_Pl_eff^R / M_Pl_eff^zeta)^2.

Step C: F_amp^3PI^R = F_amp^3PI^zeta * g^R where g^R is the regulator-dependent 3PI correction.

Step D: A_s^R / A_s^zeta = (z_zeta^2 / z_R^2) * g^R = (M_Pl_eff^zeta / M_Pl_eff^R)^2 * g^R.

Step E: Clause (b) claim: g^R = (M_Pl_eff^R / M_Pl_eff^zeta)^2 exactly (exact cancellation), so A_s^R / A_s^zeta = 1.

Step F: Numerical verification at L_max=3. Compare g^R predicted to actual.

Step G: If residual <1%, clause (b) HOLDS — F_amp^3PI is FI (regulator-independent amplitude).

Conclusion: The cancellation structure (Step E) is the theorem content. Numerical verification (Step F) is the proof evidence.

### 11. What PASS / FAIL means for solution space
- **PASS**: F_amp^3PI is FI under clause (b). A_s amplitude is regulator-independent at leading order (plus subleading corrections under dressing dressings). The UNIFIED-AS-79 framework (G16 PASS) is theoretically well-founded. G35 NNLO + W6-69 clause-(b) jointly close the field-theoretic closure of A_s.
- **FAIL**: F_amp^3PI is NOT clause-(b) FI. A_s has residual regulator dependence beyond what z_R cancellation provides. Would reopen G16 and demand alternative clause (c, d, ...) identification OR scheme-specific A_s convention.
- **INFO**: T4 theorem holds only at LO; NNLO clause-(b) correction needed in S85.

### 12. Effort estimate
1.5 sessions. Substitution chain derivation is the primary work; numerical 5-regulator scan reuses S82 W3-5 machinery; Hankel cross-check is scipy scalar.

### 13. Substrate-framing reminder
F_amp^3PI is a phononic pair-amplitude on the substrate. The clause-(b) FI property is substrate-structural, not a coincidence of "inflation formalism". The Mukhanov-Sasaki equation IS the substrate's acoustic equation for scalar-mode relay patterns.

---

## §W6-70. S84-FIELD-EXPANSION-CONVERGENCE

### 1. Gate ID
`S84-FIELD-EXPANSION-CONVERGENCE`

### 2. Trigger
`[VERIFY]` — factor-3 rule on NLO coefficient vs eps_H = 0.02163.

### 3. Classification
PHONONIC — the field-theory 3PI expansion at CMB pivot (N_field=1) is a Mukhanov-Sasaki phonon amplitude expansion; convergence is a substrate-structural property of the phonon sector's self-interaction hierarchy.

### 4. Agent type
`feynman-theorist` (3PI NLO-in-N_field computation + convergence rate bounding).

### 5. Hypothesis
The NLO-in-N_field coefficient of the 3PI expansion at CMB pivot (N_field=1, single scalar degree of freedom) is bounded by slow-roll suppression of scalar self-interaction vertex on the post-fold cascade, with NLO coefficient < eps_H = 0.02163 — establishing field-sector expansion convergence at EFT-bound rate INDEPENDENT of the 1/N_gauge (S83 G37) atlas.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: The 3PI expansion has TWO formally independent expansion parameters: 1/N_gauge (color-group size) and 1/N_field (scalar-field-content count). G35 addressed 1/N_gauge. W6-70 addresses 1/N_field. This is a PHONONIC self-interaction expansion — post-fold cascade amplitudes for scalar-mode relay patterns on the substrate fabric.

Canonical imports:
```python
from canonical_constants import (
    H_TD, eps_H, tau_fold, N_pivot, k_pivot,
)
```

Procedure:

1. Definition of field-expansion NLO coefficient at CMB pivot:
   ```
   F_amp^3PI(pivot; N_field) = F_amp^3PI^(0) + (1/N_field) * F_amp^3PI^(NLO) + O(1/N_field^2)
   ```
   At N_field = 1 (single scalar d.o.f., framework-canonical), the expansion is TRUNCATED; the question is whether F_amp^3PI^(NLO) / F_amp^3PI^(0) is bounded by eps_H.

2. Compute F_amp^3PI^(NLO) coefficient from 3PI skeleton expansion at pivot. This involves the NLO scalar self-interaction vertex on post-fold cascade background:
   ```
   F_amp^3PI^(NLO)(pivot) = integrate over k-mode-shell_pivot [L_3-vertex * mode-propagator-squared] / (mode-propagator-tree)
   ```
   where L_3-vertex is the 3-point scalar self-coupling at pivot.

3. Slow-roll bound on L_3-vertex: on post-fold cascade (cubic van-Hove transit), slow-roll parameter eps_H = 0.02163 gives SCALAR self-coupling lambda_3 ~ eps_H * H^2 * M_Pl_eff. This is the EFT-bound suppression.

4. NLO coefficient:
   ```
   |F_amp^3PI^(NLO)(pivot)| / |F_amp^3PI^(0)(pivot)| ≤ lambda_3 / (H^2) = eps_H = 0.02163
   ```
   The bound is STRUCTURAL (slow-roll).

5. Numerical verification: compute F_amp^3PI^(NLO) at pivot using explicit 3PI skeleton integration on substrate background. Compare to eps_H.

6. Cross-check against G35: the 1/N_gauge convergence at 0.0037 is DISTINCT from 1/N_field convergence. Both should separately be < eps_H for field-sector convergence.

7. Report:
   - F_amp^3PI^(NLO) / F_amp^3PI^(0) at pivot
   - Comparison to eps_H = 0.02163
   - Cross-check against G35 rate 0.0037 (1/N_gauge)
   - Combined-expansion sanity check: (1/N_field) * NLO_field + (1/N_gauge) * NLO_gauge total < eps_H

GPU note: 3PI skeleton integration at L_max=3 pivot uses existing Mukhanov-solver machinery; no new large-matrix work. Scalar integration with scipy.integrate.

Cross-checks:
- G35 NNLO-1/N-CONVERGENCE = 0.0037 (1/N_gauge=1/3 of color) implies 1/N_field should be comparable or smaller on slow-roll-bound hypothesis.
- eps_H = 0.02163 canonical (S80 permanent); eps_H^2 = 4.68e-4 is NNLO bound.
- Field-expansion NLO should be eps_H * O(1) coefficient; large coefficients (>10) would indicate unboundedness.

Output files:
- Script: `computations/s84_w6_field_expansion_convergence.py`
- Data: `computations/s84_w6_field_expansion_convergence.npz` (arrays: NLO_coef_field, NLO_coef_gauge, eps_H_bound, combined_expansion_total)
- Plot: `computations/s84_w6_field_expansion_convergence.png` (bar chart: NLO_field vs NLO_gauge vs eps_H bound)
- Verdict line:
  `S84-FIELD-EXPANSION-CONVERGENCE: PASS|FAIL|INFO -- value=<NLO_coef_field> scheme=<3PI-skeleton> convention=<slow-roll-bound> L_max=3 sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: 3 (same as F_amp^3PI scope)
- scan_range: pivot = k_pivot; N_field=1 (framework-canonical scalar d.o.f.); NNLO-in-field correction bracket {0.5, 1.0, 2.0} × eps_H^2
- tolerance: 5% on NLO coefficient; bound eps_H = 0.02163 pinned
- scheme: 3PI skeleton expansion at 2PI-level self-energy; slow-roll bound
- convention: pivot = k_pivot; N_field=1 single-scalar; canonical slow-roll eps_H
- random_seed: N/A
- GPU path: N/A

### 8. Expected output 4-tuple
`(value=<NLO_coef_field>, scheme=<3PI-skeleton>, convention=<slow-roll-bound>, L_max=3)`

Prediction: NLO_coef_field ∈ [0.005, 0.02] — slow-roll-bound gives eps_H ceiling, but typical coefficient is O(1) * eps_H = 0.02163 with possible O(0.1-1) multiplier from 3PI integration.

### 9. Thresholds
- PASS: NLO_coef_field < eps_H = 0.02163 (field-sector expansion converges at EFT-bound rate)
- FAIL: NLO_coef_field ≥ 0.1 (5x above eps_H; expansion divergent; 3PI untrustworthy at pivot)
- INFO: eps_H ≤ NLO_coef_field < 0.1 (convergent but slower than EFT-bound; indicates subleading enhancement)

### 10. Substitution chain ([VERIFY] — factor-3 threshold)

Claim: "NLO_field < eps_H = 0.02163."

Step 1: F_amp^3PI(N_field) = F_amp^(0) + (1/N_field) * F_amp^(NLO_field) + ...

Step 2: Define dimensionless NLO coefficient c_field = F_amp^(NLO_field) / F_amp^(0) at pivot.

Step 3: c_field arises from 3PI skeleton-graph integration: c_field = int[mode-sum * vertex-factor * propagator] / (tree-amplitude).

Step 4: Scalar self-vertex lambda_3 ~ partial^2 V / partial phi^3 on post-fold cascade. In slow-roll limit: lambda_3 = (3 H^2 / M_Pl_eff) * eps_H + O(eps_H^2).

Step 5: vertex-factor in skeleton integral: lambda_3 / H^2 = eps_H / M_Pl_eff * (3) ~ eps_H × O(1) dimensionally.

Step 6: Therefore c_field ~ eps_H * (integrand_phase-space) where integrand is O(1) on slow-roll background.

Step 7: c_field ≤ eps_H is the slow-roll-bound expectation. PASS iff numerical c_field < 0.02163.

Conclusion: Slow-roll structurally bounds c_field by eps_H; numerical value verifies this slow-roll hypothesis on the post-fold cascade background.

### 11. What PASS / FAIL means for solution space
- **PASS**: 3PI amplitude expansion converges in BOTH 1/N_gauge (G35) AND 1/N_field (W6-70). F_amp^3PI is a genuine asymptotic expansion with eps_H-bounded higher orders. Framework A_s = 5.08e-9 (G16) has both gauge-sector and field-sector convergence verified — full field-theoretic closure at pivot.
- **FAIL**: 3PI expansion diverges in field sector. F_amp^3PI at pivot is untrustworthy; A_s prediction requires non-perturbative resummation. Would demote G16 to INFO status pending S85 re-derivation.
- **INFO**: Convergent but above EFT-bound rate; subleading enhancement present; S85 should identify the enhancement source (could be substrate-specific feature).

### 12. Effort estimate
1 session. 3PI skeleton integration with scalar self-vertex; reuse existing Mukhanov-solver machinery.

### 13. Substrate-framing reminder
The 3PI field expansion is over substrate scalar-mode phonon self-interactions on the post-fold cascade background. Slow-roll bound is a substrate-structural consequence of the fold's near-quadratic shape in action-space, not a generic "inflation" bound.

---

## §W6-71. S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE

### 1. Gate ID
`S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE`

### 2. Trigger
`[AUDIT]` — meta-gate re-examining the S83 cluster-test methodology and formalizing the pre-declaration requirement.

### 3. Classification
META — methodological template ensuring all S84+ cluster-test gates pre-declare Mellin-balance BEFORE running scans. Not a physics observable; not phononic/geometric/particle.

### 4. Agent type
`feynman-theorist` (methodology-template construction + template-application audit across S84 gate blocks).

### 5. Hypothesis
A standardized pre-registration snippet requiring the computing agent to IDENTIFY the Mellin labels of numerator and denominator BEFORE running the scan, attached to every S84+ cluster-test gate, prevents recurrence of S83 G15/G28/G34 ad-hoc membership claims AND achieves measured cluster span matching predicted span to <1% on every covered gate.

### 6. Method (full-fidelity dispatch prompt)

Substrate-framing note: Mellin labels are the substrate's grading of spectral moments. Pre-declaration is an EPISTEMIC discipline — ensuring that claims about "balanced ratios" are made against the Mellin-moment structure BEFORE empirical cluster-test, not post hoc.

Canonical imports:
```python
# No canonical constants needed — this is a template + audit gate.
```

Procedure:

1. Construct the standard pre-registration snippet (the TEMPLATE):

```
## Mellin-Balance Pre-Declaration (REQUIRED for S84+ cluster-test gates)

**Observable**: O = <explicit definition>

**Numerator (f_num)**: Mellin label k_num = <integer>
  **Reason**: <which spectral moment is being sampled, e.g., "a_k^R Seeley-DeWitt coefficient">

**Denominator (f_den)**: Mellin label k_den = <integer>
  **Reason**: <which spectral moment>

**Balance condition**: k_num == k_den = <pass/fail>

**Classification** (PRE-SCAN):
  - If k_num == k_den → CLAIMED-R-PROTECTED → predicted cluster < 1.5
  - If k_num != k_den → CLAIMED-NOT-R-PROTECTED → predicted cluster ≥ 2.5

**Predicted cluster**: cluster_predicted = <numeric>
  **Derivation**: via CC-5 identity, cluster(O) = span(f_num)^|p_num| * span(f_den)^|p_den|

**Post-scan measured cluster**: <filled after run>

**Agreement check**: |cluster_measured - cluster_predicted| / cluster_predicted < 0.01 → TEMPLATE PASS

**PRU check**: Did the Mellin-balance pre-declaration appear BEFORE any scan? <yes/no>
```

2. Audit S84 gate blocks where cluster-tests are run. The S84 cluster-test gate set includes:
   - W6-67 (S84-Z-R-COUNTERTERM-EXISTENCE): cluster_Z_a2 test
   - W6-68 (S84-R-PROTECTED-ATLAS-COMPLETENESS): per-entry cluster
   - S84-CONV-B-PROPAGATION-ATLAS (item #22 in §4.C — separately dispatched): G15/G16/G28/G34 under Convention B
   - S84-K-A4-CANONICAL-RANGE (item #32): a_4 slot cluster
   - S84-BALANCED-RATIO-UNIVERSALITY (item #23): atlas extension
   - All §4.C §VII.K-PROP cluster-tests (items #21-#36)

3. For each cluster-test gate in S84+, verify:
   a. Does the gate block contain the Mellin-Balance Pre-Declaration snippet? YES/NO
   b. Is the predicted cluster computed BEFORE the scan? YES/NO
   c. Does |cluster_measured - cluster_predicted| / cluster_predicted < 0.01?

4. Produce audit report:
   - List of S84 cluster-test gates
   - For each: snippet-present YES/NO; predicted cluster value; measured cluster value (if gate has run); agreement ratio; template-compliance verdict.

5. Meta-gate PASS iff:
   - Every S84 cluster-test gate includes the snippet (100% coverage)
   - For gates that have run: predicted span matches measured span to <1% relative
   - No cluster-test gate reports a verdict without pre-declaration

6. Meta-gate FAIL iff: any S84 cluster-test gate reports a cluster verdict without the Mellin-balance pre-declaration snippet.

7. Output artifacts:
   - Template text (above) formalized and saved as `.claude/templates/mellin-balance-pre-declaration.md` for S85+ reuse
   - Audit report table
   - Verdict

GPU note: N/A.

Cross-checks:
- Apply template retroactively to S83 G15/G28/G34: their failures correspond to claim/fail mismatch on Mellin-balance. If pre-declaration had been in place, G28 cluster=1766 would have been classified CLAIMED-NOT-R-PROTECTED (or claim-retracted) ex ante.
- Apply to S83 PASSes: G14 c_s and G26 alpha_SDW^NLO were implicitly balanced; verify their cluster values align with CC-5 prediction under explicit pre-declaration.

Output files:
- Template: `.claude/templates/mellin-balance-pre-declaration.md`
- Script: `computations/s84_w6_mellin_balance_template_audit.py` (audits S84 gate blocks for snippet presence)
- Data: `computations/s84_w6_mellin_balance_template_audit.npz` (arrays: gate_ids, snippet_present, predicted_cluster, measured_cluster, agreement_ratio, compliance_verdict)
- Audit report: `computations/s84_w6_mellin_balance_template_audit.csv`
- Verdict line:
  `S84-OBSERVABLE-MELLIN-BALANCE-TEMPLATE: PASS|FAIL|INFO -- value=<compliance_fraction> scheme=<meta-gate> convention=<Mellin-pre-declaration-template> L_max=<N/A> sha256=<64-char>`

### 7. Machinery pin (PRDR)
- L_max: N/A
- scan_range: S84 cluster-test gate set (enumerated above; to be updated as gates are added)
- tolerance: 0% snippet-absence tolerance (either present or not); 1% relative on predicted-vs-measured cluster
- scheme: META-gate (template + audit)
- convention: pre-declaration text saved to `.claude/templates/mellin-balance-pre-declaration.md`
- random_seed: N/A
- GPU path: N/A

### 8. Expected output 4-tuple
`(value=<compliance_fraction>, scheme=<meta-gate>, convention=<Mellin-pre-declaration-template>, L_max=<N/A>)`

Prediction: compliance_fraction = 1.0 if all S84+ gate blocks include the snippet; < 1.0 if any is missing.

### 9. Thresholds
- PASS: compliance_fraction = 1.0 (100% snippet coverage) AND every run gate has |measured - predicted|/predicted < 0.01
- FAIL: any cluster-test gate reports a verdict without Mellin-balance pre-declaration (compliance < 1.0) OR any run gate has |measured - predicted|/predicted > 0.05
- INFO: compliance = 1.0 but one or more gates have 0.01 ≤ |measured - predicted|/predicted < 0.05 (template works but NLO corrections exist)

### 10. Substitution chain

Not required — this is a META-gate with no physics sign/direction claim. The template snippet itself embodies the methodological requirement.

### 11. What PASS / FAIL means for solution space
- **PASS**: S84+ cluster-test methodology is pre-registration-compliant. Recurrence of G15/G28/G34-type ad-hoc classification errors prevented BY CONSTRUCTION. The W1-W5 cluster gates and W6-67/W6-68 all ran under template discipline.
- **FAIL**: One or more S84 cluster-test gates ran without pre-declaration. Potential PRU (Class 8) vulnerability for those gates — triggers re-dispatch under template.
- **INFO**: Template works at leading order; NLO discrepancies between predicted and measured indicate subleading truncation effects — useful diagnostic for L_max extrapolation.

### 12. Effort estimate
0.5 session. Template construction (text) + audit script (enumerate gate blocks in session-84-plan-w*.md for snippet presence).

### 13. Substrate-framing reminder
Mellin labels are substrate-spectral-moment integer gradings. Pre-declaration is epistemic discipline on the substrate-observable mapping — ensuring that "balanced ratio" claims reflect the substrate's Mellin structure, not post-hoc fitting.

---

## W6 → W7 Decision Point

W6 delivers 8 gates. Based on outcomes, W7 priorities are:

1. **If W6-67 PASS (Z_R counterterm exists)** AND W6-68 PASS (R-protected atlas complete): field-theory renormalization sheet is consistent; W7 focuses on L_max → 7 extrapolation of counterterm structure AND R-atlas extension to k=4.
2. **If W6-67 FAIL OR W6-68 FAIL**: R-protected classification has a structural problem; W7 requires 2-loop investigation OR alternative renormalization scheme.
3. **If W6-69 FAIL (F_amp^3PI NOT clause-(b))**: A_s = 5.08e-9 reopens; W7 demands alternative amplitude reconstruction.
4. **If W6-70 FAIL (field-expansion divergent)**: 3PI amplitude at pivot untrustworthy; W7 requires non-perturbative resummation.
5. **If W6-50 PASS (LISA/DECIGO/BBO discriminator)**: promote to flagship prediction; pre-register against LISA timeline. If FAIL: CGWB joins detector-sterile list.
6. **If W6-51 ≥3-observable discriminator**: multi-D branch-discrimination framework established.
7. **If W6-52 34σ survives**: CMB-S4 alpha_s becomes flagship ~2030 discriminator.
8. **W6-71 template PASS**: mandatory for all S85+ cluster-test gates; becomes permanent plan-block requirement.

---

## W6 Machinery-Enumeration Pin (§0.11)

Per PRDR discipline, W6 gates declare the following FREE parameters explicitly:

| Gate | Free parameters enumerated | Pinned value / diagnostic-declared |
|:-----|:---------------------------|:-----------------------------------|
| W6-50 | transfer_correction (0.5/1.0/2.0 bracket), f_grid sample points | central 1.0 pinned, f_grid = {1e-4, 1e-3, 1e-1} Hz pinned; bracket reported as machinery constant |
| W6-51 | observable catalog cardinality, finite-diff delta | 12 entries pinned; delta = 1e-6 pinned |
| W6-52 | detector list, sigma literature sources | 5 detectors pinned; arxiv references mandatory-cited |
| W6-67 | L_max, lambda_cut, heat-kernel expansion order | L_max=5, lambda_cut=Lambda_Z canonical, order a_0/a_2/a_4 pinned |
| W6-68 | atlas entries, 5 regulators | atlas = 9 claimed + 2 new k=2 pinned; regulators = {zeta, Zubarev, SDW, dim-reg, lattice-BR} pinned |
| W6-69 | L_max, eps_H bracket | L_max=3, eps_H = 0.02163 pinned; bracket {0.01, 0.02163, 0.05} diagnostic |
| W6-70 | L_max, NNLO-in-field bracket | L_max=3 pinned; bracket {0.5, 1.0, 2.0} × eps_H^2 diagnostic |
| W6-71 | S84 cluster-test gate set (evolves with plan) | enumerated; evolves as plan completes — audit snapshot at execution time |

All machinery pins above are enforced by the script's input-pin map; any deviation triggers re-dispatch.

---

## W6 Input-SHA Ledger

Per S81+ discipline, every W6 script records the SHA-256 of every input in its first 20 stdout lines. W6 pin SHAs are computed at runtime; the following source files are READ and SHA'd:

| Script | Inputs (pre-runtime hash) | Inputs (runtime hash) |
|:-------|:--------------------------|:----------------------|
| s84_w6_cgwb_absolute_pt.py | canonical_constants.py, S83-G46 r_CMB anchor, S83-G50 n_T anchor | Gamma_phi_modulus S76 pin, transfer_correction bracket |
| s84_w6_sibling_common_prefactor.py | canonical_constants.py, CC3 identity spec | observable catalog, exponent table |
| s84_w6_alpha_s_cmb_s4_refinement.py | canonical_constants.py, S50 alpha_s=n_s²-1 derivation | detector forecast papers (arxiv references) |
| s84_w6_z_r_counterterm.py | canonical_constants.py, D_K eigenvalue cache (S83 L_max=5), Connes spectral-action RG beta | 5-regulator heat-kernel a_k values |
| s84_w6_r_protected_atlas_completeness.py | canonical_constants.py, D_K eigenvalue cache, S83 G14/G26 anchor values | 5-regulator atlas measurement |
| s84_w6_f_amp_3pi_fi_chain.py | canonical_constants.py, Mukhanov-Sasaki solver, Hankel function (scipy) | 5-regulator F_amp^3PI values, eps_H bracket |
| s84_w6_field_expansion_convergence.py | canonical_constants.py, 3PI skeleton integration machinery | NLO_field coefficient |
| s84_w6_mellin_balance_template_audit.py | .claude/templates/mellin-balance-pre-declaration.md (W6-71 writes this), session-84-plan-w1-w6.md gate blocks | per-gate snippet-presence scan |

All eight scripts produce:
- First-20-stdout-lines SHA-256 pin map of inputs
- Final-non-verdict-line 4-tuple `(value=<v>, scheme=<s>, convention=<c>, L_max=<L>)`
- Closure SHA-256 (full 64 hex) in final verdict line appended to `s84_gate_verdicts.txt`
- Data `.npz` and plot `.png` where applicable
- Dual-SHA schema_version=S84+ (`audit_sha256=<>` + `content_sha256=<>`) per S84-W1-CF-SHA-SPLIT carryforward

---

**End of Wave 6 Plan.**
