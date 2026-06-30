# Session 84 Plan — Wave 4: Observational & Detector Forecasts

**Date**: 2026-04-18
**Wave**: 4 of 10
**Theme**: Observational + Detector Forecasts. Fisher-matrix joints, transfer-function sign and magnitude, pre-registration against imminent releases (BK-Array 2026, DR3, LiteBIRD 3-yr, CMB-S4 2030-2032, SKA-1/2), and the structural bookkeeping that defines which channels are detector-sterile vs live.
**Format**: 13 parallel single-agent computations (all 13 independent; no intra-wave dependencies except #43 depends on #38 output).
**Source**: S83 mack-synthesis §V (V.3-V.4, V.6-V.10, V.12), S83 sagan-synthesis §V (observational roadmap), §4.D of `session-84-context.md`.
**Motivation**: The framework's observational roadmap has three live 2026-2035 windows (BK-Array 2026 r-band, DESI DR3 w_0/w_a, LiteBIRD 3-yr n_T) and two deferred 2030-2035 windows (CMB-S4 α_s/n_T, SKA SNR on α_f_NL). Wave 4 pre-registers every prediction against a concrete detector threshold, flags detector-sterile channels explicitly, and freezes the 7/9 → 8/9 → 9/9 P_obs_aligned ceiling-lifting chain before ceiling-moving events land.

**Results file**: `sessions/archive/session-84/session-84-results-workingpaper.md` §W4 (sections §VI.W4-A through §VI.W4-M)

---

## Wave 4 Summary

| # | Gate ID | Trigger | Classification | Framework pred | Decisive threshold | Effort |
|:--|:--------|:--------|:---------------|:---------------|:-------------------|:-------|
| 37 | S84-LB-CMBS4-JOINT-SIGMA-NT | [VERIFY] | GEOMETRIC | σ(n_T)_joint_3yr | PASS ≤0.04 | 3-4h |
| 38 | S84-ALPHA-F-NL-FRAMEWORK-PRED | [SIGN][CHAIN] | PHONONIC | α_f_NL first-principles | PASS \|α\|>0.8 | 8-10h |
| 39 | S84-N_T-CMB-TRANSFER | [SIGN] | GEOMETRIC | n_T(k_CMB)=-3e-3 RED | PASS \|n_T\|<0.01 | 3-4h |
| 40 | S84-N_T-FWHM-SENSITIVITY | [VERIFY] | GEOMETRIC | d n_T / d FWHM | Fine-tuning FAIL >500/unit | 2-3h |
| 41 | S84-BLUE-TRANSIT-TILT-INACCESSIBILITY | [AUDIT] | GEOMETRIC | Δ(n_T)_CMB~10⁻⁴ vs σ_LB~0.05-0.15 | PASS registry entry | 1-2h |
| 42 | S84-BICEP-KECK-2026-PRE-REGISTER | [VERIFY] | GEOMETRIC | r(k_CMB)=0.0117 | Pre-reg filed | 1-2h |
| 43 | S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR | [VERIFY][CHAIN] | PHONONIC | α_framework/5.118 | PASS SNR≥2 | 1h (after #38) |
| 44 | S84-DR3-CONTINGENCY-FINE-GRAINED | [AUDIT] | GEOMETRIC | 7-scenario decision tree | Conditional on W1 DR3 FAIL | 2-3h |
| 45 | S84-YUKAWA-OOM-ESTIMATOR | [VERIFY] | PARTICLE | actual 10⁻⁶ vs estimator 10⁻⁴ | PASS within 30% | 2-3h |
| 46 | S84-G51-LMAX-CONVERGENCE | [VERIFY] | GEOMETRIC | w_0(L=9)-w_0(L=5) | PASS <0.005 + band | 6-8h |
| 47 | S84-UHF-GW-THRESHOLD-WATCH | [AUDIT] | GEOMETRIC | Ω_GW(1 mHz) 46.7 OOM below LISA | Pre-reg threshold | 1-2h |
| 48 | S84-FALSIFIER-RIGOR-REGISTRY | [AUDIT] | NON-PHONONIC | 4-class rigor tags | PASS registry complete | 2-3h |
| 49 | S84-P-OBS-ALIGNED-CEILING | [VERIFY] | NON-PHONONIC | 7/9 → 8/9 → 9/9 chain | PASS dependency-graph filed | 1-2h |

**Wave 4 total effort**: ~35-50h distributed; dispatch in 2 batches of ≤8 concurrent agents (Batch-A: #37-#44; Batch-B: #45-#49 after #38 completes to unblock #43).

**Detector windows (canonical constants to import or pin explicitly)**:
- BK-Array 2026 (Mar-Jun 2026, σ_r ≈ 0.005)
- DESI DR3 (expected 2026-Q2/Q3 through 2028 full release; σ_w0 ≈ 0.046, σ_wa ≈ 0.177, ρ=-0.85)
- LiteBIRD 3-yr (launch 2032; σ_3yr = 2.16 μK-arcmin, f_sky = 0.70, 50% delensing); 6-7 yr extended to reach σ(n_T) ≈ 0.04
- CMB-S4 (2030-2032 deployment; 1.0 μK-arcmin, 30-arcmin beam, f_sky = 0.40, 90% delensing)
- SKA-1 Phase-1 (2027-2029 commissioning; σ(α_f_NL) = 5.118)
- SKA-2 full science (2032-2035; σ(α_f_NL) = 0.80, G45 PASS value)

---

## Wave 4 Decision Point Prerequisites

Wave 4 is independent of W1 DR3-RESPONSE outcome at dispatch time; gates #42, #44, #47 encode pre-registration logic that resolves asynchronously on external release events. Gate #43 depends on #38 output (α_f_NL prediction), so dispatch #38 first in Batch-A and #43 at head of Batch-B.

**Batch-A (8 concurrent, dispatch together)**: #37, #38, #39, #40, #41, #42, #44, #45
**Batch-B (5 concurrent, dispatch after Batch-A completes)**: #43, #46, #47, #48, #49

---

## §W4-37. S84-LB-CMBS4-JOINT-SIGMA-NT

**Gate ID**: S84-LB-CMBS4-JOINT-SIGMA-NT
**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (Fisher-matrix joint on B-mode observables; not substrate excitation)
**Hypothesis being tested**: A 3-parameter joint Fisher (r, n_T, A_lens) combining LiteBIRD B-modes with CMB-S4 delensing crosses the σ(n_T) ≤ 0.04 threshold at 3-yr LiteBIRD + full-survey CMB-S4, closing the G43 INFO verdict (σ_3yr=0.054 LiteBIRD-alone).
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are extending S83-G43 (S83 Wave 3, LiteBIRD σ(n_T) reach, INFO at 0.054 at 3 yr) to a 3-parameter joint Fisher analysis combining LiteBIRD + CMB-S4. Framing rules: treat LiteBIRD and CMB-S4 as INDEPENDENT EXPERIMENTS (Fisher sum F_joint = F_LB + F_S4), not a single fused likelihood. The framework fiducial is (r, n_T, A_lens) = (0.0242, -0.003024, 1.0) where n_T is the CMB-scale value from G46 transfer (NOT the transit-scale +0.468 from G50).

**Substrate-framing reminder**: The transfer G46 is the relay-pattern propagation through the emergent g_M (c-bounded) from transit scale k_transit ~ 587 M_KK to k_CMB; the BLUE tilt +0.468 is substrate-scale and inaccessible (see gate #41).

**Computation steps**:

1. Import canonical constants: `from canonical_constants import M_KK, tau_fold, planck_ns`. Pin LiteBIRD and CMB-S4 noise specs from `canonical_constants.py` (add if missing WITH provenance): `sigma_LB_3yr = 2.16` (μK-arcmin), `f_sky_LB = 0.70`, `delens_LB = 0.50`, `sigma_S4 = 1.0` (μK-arcmin), `theta_beam_S4 = 30.0` (arcmin), `f_sky_S4 = 0.40`, `delens_S4 = 0.90`.
2. Build the B-mode noise power spectrum N_ell^BB for each experiment. Use Knox formula with beam deconvolution: N_ell = (σ_arcmin · θ_beam)² · exp(ell(ell+1)θ_beam²/8 ln 2).
3. Compute CMB-scale tensor power C_ell^BB at fiducial (r, n_T) via (a) primordial P_t(k) = r·A_s·(k/k_pivot)^{n_T} with k_pivot=0.05 Mpc⁻¹, (b) tensor transfer function (use CAMB or analytic fit; state which).
4. Compute lensing B-mode C_ell^BB,lens, scaled by (1 − delens) per experiment.
5. Build 3×3 Fisher matrix F_ij = Σ_ell (2ell+1)/2 · f_sky · (∂C_ell/∂p_i)(∂C_ell/∂p_j)/(C_ell + N_ell)², where p = (r, n_T, A_lens). Use central-difference derivatives with δp = 0.01·p for r, δn_T=0.005, δA_lens=0.01.
6. Sum F_LB + F_S4 → F_joint. Invert; σ(n_T)_joint = sqrt((F_joint⁻¹)_{n_T, n_T}).
7. Also report σ(r)_joint, σ(A_lens)_joint, and the (r, n_T) correlation coefficient ρ_{r, n_T}.
8. Substitution chain [VERIFY]: state (i) definition of Fisher information, (ii) substitute fiducial values into ∂C_ell/∂p_i, (iii) simplify to F_ij, (iv) read σ(n_T) from (F⁻¹)_{22}. DO NOT shortcut the direction claim — sign of ∂C_ell/∂n_T is positive at ell > ell_pivot and negative at ell < ell_pivot; Fisher is positive-definite, so σ(n_T) is always positive, but the improvement over LiteBIRD-alone must be verified numerically.
9. Write result to §VI.W4-37 of `sessions/archive/session-84/session-84-results-workingpaper.md` with full Fisher matrix, marginalized 1σ bounds, and comparison table vs G43.

**Machinery pin (PRDR)**:
- ell range: 2 ≤ ell ≤ 300 (LiteBIRD reheating bump + recombination peak); 50 ≤ ell ≤ 3000 (CMB-S4 delensing)
- k_pivot = 0.05 Mpc⁻¹ (Planck 2018 convention)
- Derivative scheme: 5-point centered stencil
- GPU path: NOT required (3×3 Fisher, CPU is fine; set OMP_NUM_THREADS=4)
- Random seed: N/A (deterministic Fisher)
- Convention: scalar A_s = 2.1e-9 Planck pivot; r = P_t/P_s ratio; n_T defined with minus-sign convention P_t ∝ k^{n_T} (Planck 2018 Eq. 5.1)

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g43_litebird_sigma_nT_reach.npz` — <computed-at-runtime>
- `computations/s83_w3_g46_tensor_transfer.npz` — <computed-at-runtime>
- LiteBIRD noise spec (Hazumi+ 2020 arXiv:2007.12538): literature citation, no file

**Expected output 4-tuple**: (value=σ(n_T)_joint_3yr, scheme="Fisher 3-param marginalized", convention="Planck 2018 n_T sign", L_max=N/A)

**PASS**: σ(n_T)_joint_3yr ≤ 0.04 → LB+S4 combined reaches sub-0.04 sensitivity at 3-yr integration.
**INFO**: 0.04 < σ(n_T)_joint_3yr ≤ 0.06.
**FAIL**: σ(n_T)_joint_3yr > 0.06 → joint no-better-than-alone; full-survey extension to 6-7 yr needed.

**What PASS vs FAIL means**: PASS maps which detector combinations CAN discriminate framework n_T at CMB scales within the 2032-2035 window. FAIL reinforces gate #41 (BLUE-TRANSIT-TILT-INACCESSIBILITY) as structurally permanent. Either way, the boundary is the 3-yr integration; extended mission reach is the consolation.

**Output files**:
- `computations/s84_w4_lb_cmbs4_joint_sigma_nt.py`
- `computations/s84_w4_lb_cmbs4_joint_sigma_nt.npz`
- `computations/s84_w4_lb_cmbs4_joint_sigma_nt.png` (σ(n_T) vs delensing fraction heatmap)
- Verdict line → `computations/s84_gate_verdicts.txt`
- Working-paper section § VI.W4-37

---

## §W4-38. S84-ALPHA-F-NL-FRAMEWORK-PRED

**Gate ID**: S84-ALPHA-F-NL-FRAMEWORK-PRED
**Trigger**: [SIGN][CHAIN]
**Classification**: PHONONIC (GGE bispectrum = substrate relay-pattern 3-point function)
**Hypothesis being tested**: The framework's native α_f_NL (running of equilateral f_NL with ln k) from (a) GGE bispectrum machinery and (b) fold-time dispersion across the transit exceeds |α| > 0.8, making it detectable at SKA-2.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are deriving the FIRST-PRINCIPLES framework prediction for α_f_NL ≡ d f_NL / d ln k at the CMB pivot, combining two sources: (i) the GGE bispectrum's intrinsic k-dependence (S67 GGE-BISPECTRUM-67 gave f_NL_total=1.03) and (ii) the fold-time dispersion from the Bogoliubov amplitude's k-dependence across the van Hove transit (see S63 RUNNING-NS-63 and S65 NT-BLUE-65 for precedent machinery). The framework is NOT free to adjust α; α emerges from the substrate eigenvalue problem.

**Substrate-framing reminder**: f_NL is the acoustic 3-point function of the emergent density field after relay-pattern propagation through g_M. α_f_NL measures the scale-dependence of this 3-point function, which inherits the k-dependence of the fold-time dispersion ω(k) - c_s k across the transit.

**Computation steps**:

1. Import `from canonical_constants import M_KK, tau_fold, c_Gold, c_fabric, dt_transit, Delta_BCS`. Pin k_pivot = 0.05 Mpc⁻¹ and k_transit ≈ 587·M_KK (from G46 tensor-transfer analysis).
2. Load S67 GGE-BISPECTRUM-67 result: f_NL^equil(k_pivot) = 0.853, f_NL^folded = 0.129, f_NL^multi = 0.56, f_NL^total = 1.03 (G45 pre-reg baseline 1.12 was transcription; use 1.03).
3. Compute d ln f_NL^equil / d ln k analytically from the GGE bispectrum triangle-closure integrand. Use the same dispersion relation ω(k) = c_s k · (1 + (k/k_transit)²·dispersion_coeff) that drives n_s running in S63.
4. Compute d ln f_NL^folded / d ln k — this channel involves Bogoliubov amplitude |β_k|² which has explicit k-dependence from the transit pair-production calculation. Use the k-power exponent from S63's running-ns machinery.
5. Sum weighted by channel amplitudes: α_f_NL = Σ_ch (f_NL^ch / f_NL^total) · d ln f_NL^ch / d ln k.
6. [SIGN] Substitution chain for the sign: (i) GGE bispectrum in equilateral limit has triangle-momentum scaling k^{n_s - 4}; (ii) n_s - 4 = 0.957 - 4 = -3.043; (iii) d f_NL/d ln k ∝ (n_s - 4) · f_NL — this is NEGATIVE if f_NL > 0. (iv) Folded contribution has opposite sign from transit-dispersion. (v) Sum them; read off net sign. Confirm the sign from numerical evaluation, do not assume.
7. [CHAIN] Quote α_f_NL in standard units α = d f_NL / d ln k at k = 0.05 Mpc⁻¹. Provide 1σ uncertainty from (a) propagation of M_KK uncertainty (treat Δ M_KK / M_KK = 1% as a sensitivity baseline) and (b) truncation error at L_max=5 (estimate from L_max=7 stability of S63 running-ns machinery).
8. Write result to §VI.W4-38 with full derivation, sign attribution per channel, and cross-check against slow-roll expectation α_f_NL ≈ -(n_s-1)·f_NL ≈ -0.043·1.03 ≈ -0.044 — if framework α is much larger in magnitude, it is a genuine substrate signature.

**Machinery pin (PRDR)**:
- k range for derivative: [k_pivot / 2, 2·k_pivot] = [0.025, 0.1] Mpc⁻¹
- Derivative: 4-point centered stencil in ln k
- L_max for GGE bispectrum sum: 5 (S67 canonical); cross-check at L_max=7 for truncation uncertainty
- Convention: α_f_NL per Planck 2018 equilateral template (NOT local, NOT orthogonal)
- GPU path: torch.linalg for bispectrum integrals if matrix > 500×500

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s67_gge_bispectrum.npz` — <computed-at-runtime>
- `computations/s63_running_ns.npz` — <computed-at-runtime>
- `computations/s65_blue_tensor_tilt.npz` — <computed-at-runtime>

**Expected output 4-tuple**: (value=α_f_NL, scheme="GGE-bispectrum-weighted-derivative", convention="Planck 2018 equilateral", L_max=5)

**PASS**: |α_f_NL| > 0.80 with < 20% relative uncertainty → detectable at SKA-2 (σ=0.80).
**INFO**: 0.30 ≤ |α_f_NL| ≤ 0.80 → marginal; SKA-2 sees it at 1-2σ; CMB-HD or 21-cm tomography needed.
**FAIL**: |α_f_NL| < 0.30 → invisible at SKA-2 even with tightest Fisher; 21-cm l_max ~ 10⁵ becomes sole channel.

**What PASS vs FAIL means**: PASS unlocks #43 (SKA-1 Phase-1 SNR) at ≥2σ and makes α_f_NL a live observable for 2027-2035 window. FAIL closes α_f_NL discrimination via SKA and forwards the question to deep 21-cm tomography.

**Output files**:
- `computations/s84_w4_alpha_fnl_framework_pred.py`
- `computations/s84_w4_alpha_fnl_framework_pred.npz`
- `computations/s84_w4_alpha_fnl_framework_pred.png` (α_f_NL vs k with channel decomposition)
- Verdict → `s84_gate_verdicts.txt`
- §VI.W4-38

---

## §W4-39. S84-N_T-CMB-TRANSFER

**Gate ID**: S84-N_T-CMB-TRANSFER
**Trigger**: [SIGN]
**Classification**: GEOMETRIC (tensor transfer through emergent g_M)
**Hypothesis being tested**: n_T(k_CMB) under the G46 ε_H-flow transfer is -3×10⁻³ (RED, slow-roll consistency-like), confirming the transit-scale BLUE tilt does NOT propagate to CMB scales.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are computing n_T at k_CMB from the G46 tensor-transfer machinery (S83 W3-G46 PASS at r_CMB = 0.0117). The framework's substrate-scale n_T is +0.468 BLUE (G50, transit-locked by Jensen curvature). The G46 transfer propagates tensor modes across 54 decades of k from k_transit ≈ 587·M_KK down to k_CMB = 0.05 Mpc⁻¹ through the emergent g_M (relay-pattern propagation, c-bounded).

**Substrate-framing reminder**: The BLUE +0.468 lives at the transit scale where relay patterns are born; the CMB-scale n_T is what a c-bounded observer infers from the propagated tensor spectrum. These are NOT competing predictions — they are the same physics at different scales.

**Computation steps**:

1. Import `from canonical_constants import M_KK, tau_fold, eps_H`. Pin k_transit ≈ 587·M_KK (verify via S66 transfer map), k_CMB = 0.05 Mpc⁻¹.
2. Load the G46 transfer kernel T(k_CMB; k_transit) from `s83_w3_g46_tensor_transfer.npz` or equivalent S66 result.
3. Apply the ε_H-flow transfer: n_T(k_CMB) = n_T^slow-roll + corrections from c-bounded ε_H evolution. Use n_T^slow-roll = -2·ε_H per standard inflationary identity; eps_H ≈ 0.02163 (from canonical).
4. [SIGN] Substitution chain:
   - Step 1 (definition): n_T^slow-roll(k) = -2·ε_H(k) per single-field inflation (Liddle-Lyth 2000).
   - Step 2 (substitution): eps_H(k_CMB) = 0.02163 from canonical; ε_H evolves logarithmically across transfer range.
   - Step 3 (simplification): n_T(k_CMB) ≈ -2·(0.02163) = -0.04326 in pure slow-roll limit.
   - Step 4 (correction): the G46 framework value is -3×10⁻³ (quoted in context §4.D row 39), which is SUPPRESSED by factor ~14 vs naive -2·ε_H. Verify this suppression numerically via the transfer-kernel machinery in G46.
   - Step 5 (direction): n_T(k_CMB) is NEGATIVE (RED), consistent with sub-LiteBIRD threshold.
5. Quote the transit-to-CMB k-ratio exactly (54 decades per S66) and confirm the transfer-kernel scale-dependence ln(T) ∝ ln(k_CMB/k_transit).
6. Cross-check: is n_T(k_CMB) = -3×10⁻³ CONSISTENT with the framework's r(k_CMB) = 0.0117 under the modified consistency relation n_T = -r/8 per G46 PASS? Verify: -0.0117/8 = -0.00146 (this deviates from -3×10⁻³ by factor 2). Reconcile or flag.
7. Write to §VI.W4-39 with the explicit transfer-kernel derivation, the suppression factor, and the slow-roll consistency-relation cross-check.

**Machinery pin (PRDR)**:
- k range spanned by transfer: [k_CMB, k_transit] = 54 decades
- ε_H scheme: canonical single-field, constant at k_CMB (no k-dependence beyond leading log)
- Convention: Planck 2018 n_T sign convention P_t ∝ k^{n_T}
- Numerical tolerance: 10⁻⁵ relative on transfer kernel evaluation
- GPU path: not required

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g46_tensor_transfer.npz` — <computed-at-runtime>
- `computations/s65_blue_tensor_tilt.npz` — <computed-at-runtime>
- `computations/s66_tensor_transfer.npz` — <computed-at-runtime>

**Expected output 4-tuple**: (value=n_T(k_CMB), scheme="ε_H-flow-transfer-G46", convention="Planck 2018", L_max=5)

**PASS**: |n_T(k_CMB) + 3×10⁻³| < 10⁻³ (consistent with G46 benchmark) AND |n_T(k_CMB)| < 0.01 (RED, sub-LiteBIRD).
**INFO**: |n_T(k_CMB)| ∈ [0.01, 0.05] — marginal LiteBIRD reach.
**FAIL**: |n_T(k_CMB)| > 0.05 OR sign is positive (BLUE at CMB). Either outcome reclassifies the substrate-to-CMB propagation.

**What PASS vs FAIL means**: PASS confirms the G46 framework value -3×10⁻³ is reproducible from first-principles transfer machinery, and that the substrate BLUE tilt is confined to transit scales. FAIL would force a rework of gate #41 and #37 at the structural level.

**Output files**:
- `computations/s84_w4_nt_cmb_transfer.py`
- `computations/s84_w4_nt_cmb_transfer.npz`
- `computations/s84_w4_nt_cmb_transfer.png` (n_T(k) across 54 decades, log-log)
- Verdict → `s84_gate_verdicts.txt`
- §VI.W4-39

---

## §W4-40. S84-N_T-FWHM-SENSITIVITY

**Gate ID**: S84-N_T-FWHM-SENSITIVITY
**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (backreaction-window sensitivity of tensor tilt)
**Hypothesis being tested**: The sensitivity d n_T(k_CMB) / d FWHM across the backreaction window [0.5×10⁻³, 3×10⁻³] is not fine-tuned (|∂n_T/∂FWHM| < 500 per unit FWHM); if it exceeds 500, the n_T prediction is fine-tuning-dependent.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are scanning the n_T(k_CMB) prediction over the transit FWHM (backreaction window width, S83-G31 BACKREACT-TAUWINDOW PASS at 1.65×10⁻³). Goal: check whether n_T is structurally stable across the FWHM range [0.5×10⁻³, 3×10⁻³] or whether it is pathologically sensitive.

**Computation steps**:

1. Import `from canonical_constants import M_KK, tau_fold`. Pin FWHM_baseline = 1.65×10⁻³ (S83-G31).
2. Scan FWHM over [0.5×10⁻³, 3×10⁻³] with 10 log-spaced points.
3. At each FWHM, recompute (a) the Bogoliubov amplitude |β_k|² spectrum (S63/S65 machinery), (b) the G46 transfer kernel, (c) n_T(k_CMB).
4. Compute numerical derivative d n_T / d FWHM at FWHM_baseline using 5-point stencil.
5. [VERIFY] Substitution chain:
   - Step 1 (definition): n_T(k_CMB) is a functional of FWHM through the transit-width-dependent Bogoliubov amplitude.
   - Step 2 (substitution): |β_k|² ∝ f(k · FWHM / dt_transit) — the FWHM enters via the adiabaticity parameter.
   - Step 3 (simplification): d n_T / d ln FWHM ~ leading-log coefficient; in units of per-FWHM-unit, divide by FWHM_baseline.
   - Step 4: compare |d n_T / d FWHM| to the fine-tuning threshold 500/unit.
6. Flag fine-tuning if |d n_T / d FWHM| > 500 per unit. Otherwise PASS.
7. Write to §VI.W4-40 with scan plot, numerical derivative, and the fine-tuning verdict.

**Machinery pin (PRDR)**:
- FWHM scan: 10 log-spaced points in [0.5×10⁻³, 3×10⁻³]
- Stencil: 5-point centered on FWHM_baseline
- L_max: 5 (S63/S65 canonical)
- GPU path: not required
- Convention: Planck 2018

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g31_backreact_tauwindow.npz` — <computed-at-runtime>
- `computations/s65_blue_tensor_tilt.npz` — <computed-at-runtime>

**Expected output 4-tuple**: (value=|d n_T / d FWHM|, scheme="5-point-stencil", convention="per-FWHM-unit", L_max=5)

**PASS**: |d n_T / d FWHM| ≤ 500 per unit → structural, not fine-tuned.
**INFO**: 500 < |d n_T / d FWHM| ≤ 2000.
**FAIL**: |d n_T / d FWHM| > 2000 → pathological fine-tuning flag; n_T prediction is FWHM-contingent and must be declared SCHEME-DEPENDENT in gate #48.

**What PASS vs FAIL means**: PASS confirms n_T(k_CMB) is stable under the G31 backreaction-window width. FAIL forwards the n_T prediction into the #48 registry as SCHEME-DEPENDENT, removing it from the zero-free-parameter evidence column.

**Output files**:
- `computations/s84_w4_nt_fwhm_sensitivity.py`
- `computations/s84_w4_nt_fwhm_sensitivity.npz`
- `computations/s84_w4_nt_fwhm_sensitivity.png` (n_T vs FWHM with baseline marked)
- Verdict → `s84_gate_verdicts.txt`
- §VI.W4-40

---

## §W4-41. S84-BLUE-TRANSIT-TILT-INACCESSIBILITY

**Gate ID**: S84-BLUE-TRANSIT-TILT-INACCESSIBILITY
**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (permanent structural result — observational boundary)
**Hypothesis being tested**: LiteBIRD structurally cannot discriminate the framework from slow-roll on n_T at CMB scales; Δ(n_T)_CMB ~ 10⁻⁴ vs realistic σ(n_T)_LB ~ 0.05-0.15 over 2030-2040 window. Registry bookkeeping gate.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are closing the "LiteBIRD cannot discriminate framework from slow-roll on n_T at CMB scales" result as a PERMANENT STRUCTURAL RESULT in the framework registry. This is a bookkeeping gate; it produces no new numerical computation but formalizes the existing numerical result from S68 LITEB-R-FORECAST-68 + G43 + #37 + #39 into a registry entry with an explicit observational-boundary tag.

**Computation steps**:

1. Load: S68 LITEB-R-FORECAST-68 (Δ(n_T)_CMB ~ 10⁻⁴ framework vs slow-roll); S83-G43 (σ(n_T)_LB_3yr = 0.054); S83-G46 (r_CMB = 0.0117, transfer); S83-G50 (n_T_transit = +0.468); #37 output (σ(n_T)_joint_3yr); #39 output (n_T(k_CMB)).
2. Verify the ratio Δ(n_T)_CMB / σ(n_T)_LB_3yr ~ 10⁻⁴ / 0.054 ~ 2×10⁻³ (500× below detection).
3. Also verify #37 joint LB+S4 reach: if σ(n_T)_joint = 0.04 (PASS threshold of #37), the ratio is still 10⁻⁴ / 0.04 = 2.5×10⁻³ (400× below detection).
4. Assert in registry: "The framework n_T signature at CMB scales is 10⁻⁴; realistic LiteBIRD σ(n_T) within 2030-2040 is 0.04-0.15; discrimination ratio 10⁻³ to 10⁻² throughout the decade. EVOI for LiteBIRD-based n_T discrimination of the framework = 0 for the 2030-2040 window."
5. Document the 54-decade k-scale separation (transit k_transit ≈ 587·M_KK vs k_CMB = 0.05 Mpc⁻¹) as the structural reason.
6. Register in `sessions/framework/permanent-results-registry.md` with tag `OBSERVATIONAL-BOUNDARY-LITEB-NT`. Also update `sessions/evoi-framework.md`: set EVOI for "LiteBIRD n_T-tilt discrimination" to 0 (with justification citing this gate).
7. Write to §VI.W4-41 with full derivation from #37+#39+G43+G46+G50 inputs; include the EVOI=0 tag for transparency.

**Substrate-framing note**: This is NOT a failure — it is a geometric property. The BLUE +0.468 tilt IS the substrate prediction. The CMB is not at the substrate scale. Discriminators must live where the substrate physics lives (transit scale, nonlinear bispectrum, 21-cm tomography).

**Machinery pin (PRDR)**:
- No numerical computation; bookkeeping only. PRDR N/A.
- Pre-registration document format: permanent-results-registry entry + EVOI update.

**Input SHA-256 pins**:
- `computations/s68_liteb_r_forecast.npz` — <computed-at-runtime>
- `computations/s83_w3_g43_litebird_sigma_nT_reach.npz` — <computed-at-runtime>
- `computations/s83_w3_g46_tensor_transfer.npz` — <computed-at-runtime>
- `computations/s83_w3_g50_nT_bogoliubov.npz` — <computed-at-runtime>
- `computations/s84_w4_lb_cmbs4_joint_sigma_nt.npz` (from #37) — <computed-at-runtime>
- `computations/s84_w4_nt_cmb_transfer.npz` (from #39) — <computed-at-runtime>

**Expected output 4-tuple**: (value=EVOI=0, scheme="registry-entry", convention="bookkeeping", L_max=N/A)

**PASS**: Registry entry filed + EVOI=0 tag for 2030-2040 window + dependency graph naming #37, #39, G43, G46, G50 as co-inputs.
**INFO**: Registry entry filed without EVOI=0 tag (analyst reserves right to reopen).
**FAIL**: Not filed.

**What PASS vs FAIL means**: PASS freezes the discrimination ceiling at CMB scales as structural. The framework does not lose evidence here — it loses one channel, unlocking the next evoi-weighted channel (bispectrum, 21-cm).

**Output files**:
- `computations/s84_w4_blue_transit_tilt_inaccessibility.py` (audit script, loads inputs, writes registry entry)
- Verdict → `s84_gate_verdicts.txt`
- `sessions/framework/permanent-results-registry.md` append
- `sessions/evoi-framework.md` update
- §VI.W4-41

---

## §W4-42. S84-BICEP-KECK-2026-PRE-REGISTER

**Gate ID**: S84-BICEP-KECK-2026-PRE-REGISTER
**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (tensor-to-scalar ratio at CMB)
**Hypothesis being tested**: Pre-register r(k_CMB) = 0.0117 against the 2026 BICEP/Keck Array release (expected σ_r ≈ 0.005), with explicit decision tree for post-release verdict.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are pre-registering the framework prediction r(k_CMB) = 0.01173 (S83-G46 PASS, 3.07× below BK18 upper bound 0.036) against the imminent 2026 BICEP/Keck Array release. This is a procedural gate: the output is a frozen decision tree with explicit post-release trigger criteria.

**Computation steps**:

1. Import `from canonical_constants import M_KK, tau_fold`. Load G46 r prediction: r = 0.01173 (quoted in context §4.D row 42 as 0.0117; use the 5-digit value if available in canonical_constants, else 0.01173).
2. Pin the BK-Array 2026 σ_r forecast: σ_r ≈ 0.005 (Ade+ 2025 preprint literature). Add to `canonical_constants.py` as `sigma_r_BK_2026 = 0.005` with provenance comment citing literature fetch.
3. Build decision tree:
   - **Branch A (CONFIRMATION)**: r_BK2026 ∈ [0.009, 0.015] (central ±3 × σ_theory; σ_theory from G46 propagation, estimate 0.003 from M_KK and transfer uncertainties) AND central within 0.012 ± 0.003 → framework +3-sigma confirmation. Verdict: PASS with high confidence.
   - **Branch B (CONSISTENCY)**: r_BK2026 < 0.020 (upper bound, 1-sided) → framework consistent; no discrimination vs slow-roll with r > 0. Verdict: INFO.
   - **Branch C (DISFAVORED)**: r_BK2026 > 0.025 (upper bound) → framework disfavored at 2-3 sigma by G46 prediction. Verdict: FAIL.
   - **Branch D (RULED OUT)**: r_BK2026 upper < 0.008 (tighter than prediction) → framework FAIL at 2+ sigma.
4. [VERIFY] Confirm the thresholds:
   - Step 1 (definition): "consistent" = framework r within ±2σ of experimental bound; "disfavored" = framework r > 2σ above experimental central or above upper bound.
   - Step 2 (substitution): σ_r ≈ 0.005, r_framework = 0.01173.
   - Step 3 (simplification): 2σ below framework = 0.01173 - 0.010 = 0.00173 (Branch D threshold); 2σ above = 0.02173 (≈ Branch C threshold 0.020-0.025 range).
   - Step 4 (direction): the decision-tree thresholds are internally consistent with G46 prediction.
5. Freeze the decision tree by committing the exact threshold values to `s84_bicep_keck_2026_decision_tree.json` with SHA-256 pin. Explicit "frozen 2026-04-18" tag, NO post-release re-registration.
6. Write to §VI.W4-42 with full tree, thresholds, and the single-author-independence tag (Mack is the registering authority, analog of S73b DR3 pre-registration).

**Machinery pin (PRDR)**:
- σ_r_BK_2026 source: Ade+ 2025 preprint (literature citation, external value)
- σ_theory_G46 estimate: 0.003 from r propagation (nominal; refine if available from G46 .npz)
- JSON schema: {branch: A|B|C|D, threshold_lower, threshold_upper, verdict, explanation}
- Freeze protocol: SHA-256 of JSON written + logged; no post-release edits

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g46_tensor_transfer.npz` — <computed-at-runtime>
- Ade+ 2025 literature value: external citation, no file SHA

**Expected output 4-tuple**: (value="decision-tree-frozen", scheme="pre-registration-JSON", convention="BK-Array 2026", L_max=N/A)

**PASS**: JSON decision tree frozen, SHA logged, 4 branches with thresholds, published date 2026-04-18, single-authority tag. Registry entry in `sessions/framework/pre-registered-predictions.md`.
**INFO**: Tree written but one threshold missing justification or explicit numerical value.
**FAIL**: Tree not committed.

**What PASS vs FAIL means**: PASS puts a live, frozen, publicly-defensible prediction on the record that resolves in ~2-6 months (BK-Array 2026 release expected Q2-Q3 2026). This is the first falsifier trip-wire of 2026 for the framework.

**Output files**:
- `computations/s84_w4_bicep_keck_2026_pre_register.py` (decision-tree generator + JSON writer)
- `computations/s84_w4_bicep_keck_2026_decision_tree.json` (frozen)
- Verdict → `s84_gate_verdicts.txt`
- `sessions/framework/pre-registered-predictions.md` append
- §VI.W4-42

---

## §W4-43. S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR

**Gate ID**: S84-SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR
**Trigger**: [VERIFY][CHAIN]
**Classification**: PHONONIC (GGE bispectrum running observable)
**Hypothesis being tested**: The SKA-1 Phase-1 SNR = |α_framework| / σ(α)_SKA1 = |α_framework| / 5.118 reaches ≥ 2σ detectability in 2027-2029, pre-SKA-2.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**DEPENDENCY**: This gate DEPENDS on #38 output. Dispatch only AFTER #38 completes and its α_framework value is written to `s84_w4_alpha_fnl_framework_pred.npz`.

**Prompt**:

You are computing the SKA-1 Phase-1 SNR against the framework's native α_f_NL (from #38). The G45 PASS value σ(α)_SKA-2 = 0.80 underlies the 2032-2035 window; σ(α)_SKA-1 = 5.118 (G45 S83 output) underlies the 2027-2029 window. Goal: determine whether SKA-1 provides a mid-2020s-to-early-2030s α_f_NL discriminator or whether SKA-2 is sole.

**Computation steps**:

1. Import `from canonical_constants import *`. Load `s84_w4_alpha_fnl_framework_pred.npz` (from #38).
2. Extract α_framework from #38 output (expected value and 1σ band).
3. Compute SNR_SKA1 = |α_framework| / σ(α)_SKA1 = |α_framework| / 5.118.
4. Compute SNR_SKA2 = |α_framework| / 0.80 as a cross-check against #38's PASS threshold (should equal the #38 PASS criterion).
5. [CHAIN] Chain verification:
   - Step 1 (definition): SNR = signal / noise = |α_framework| / σ(α).
   - Step 2 (substitution): plug α_framework from #38, σ_SKA1=5.118.
   - Step 3 (simplification): SNR_SKA1 = |α_framework| / 5.118.
   - Step 4: compare to threshold 2σ.
6. Forecast the SKA-1 timeline: commissioning 2027-Q1, first-science 2027-Q3, Phase-1 full 2029. Quote the detection-date window and its uncertainty.
7. Write to §VI.W4-43 with the full SNR, the detection-timeline, and the fallback-to-SKA-2 schedule.

**Substrate-framing note**: This is a detector-reach bookkeeping gate. The physics is set by #38 (substrate prediction) and the α value does not move; only the detector window matters.

**Machinery pin (PRDR)**:
- α_framework from #38 (read as (value, sigma)); no independent recomputation
- σ(α)_SKA1 = 5.118 (G45 canonical, S83 pre-reg)
- σ(α)_SKA2 = 0.80 (G45 PASS)
- Threshold: SNR ≥ 2
- Date window: SKA-1 Phase-1 first-light 2027, full 2029

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g45_21cm_sigma_alpha_fnl.npz` — <computed-at-runtime>
- `computations/s84_w4_alpha_fnl_framework_pred.npz` (from #38) — <computed-at-runtime>

**Expected output 4-tuple**: (value=SNR_SKA1, scheme="Fisher-alpha-SKA1", convention="equilateral-alpha", L_max=N/A)

**PASS**: SNR_SKA1 ≥ 2 → SKA-1 is a pre-SKA-2 discriminator in 2027-2029.
**INFO**: 1 ≤ SNR_SKA1 < 2 → marginal at SKA-1; SKA-2 is the strong channel.
**FAIL**: SNR_SKA1 < 1 → SKA-1 cannot see α; SKA-2 2032-2035 is sole channel.

**What PASS vs FAIL means**: PASS unlocks a 2027-2029 detector window. FAIL pushes α_f_NL detection to 2032-2035 via SKA-2 and keeps 21-cm (l_max ≈ 10⁵) as the alternative.

**Output files**:
- `computations/s84_w4_ska1_phase1_alpha_framework_snr.py`
- `computations/s84_w4_ska1_phase1_alpha_framework_snr.npz`
- Verdict → `s84_gate_verdicts.txt`
- §VI.W4-43

---

## §W4-44. S84-DR3-CONTINGENCY-FINE-GRAINED

**Gate ID**: S84-DR3-CONTINGENCY-FINE-GRAINED
**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (dark-energy equation-of-state decision tree)
**Hypothesis being tested**: Conditional on W1 DR3-RESPONSE FAIL, the S73 W4-C 7-scenario decision tree classifies which DESI DR3 sub-scenario (B1, B2, B3, A1, A2, C1, C2) is realized; this is the fine-grained successor to the G42 binary live-watch.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are pre-registering the fine-grained 7-scenario decision tree for DESI DR3 sub-scenarios. Parent gate G42 (S83-DR3-LIVE-WATCH) is PENDING-EVENT on the binary "is (w_0^DR3, w_a^DR3) inside rectangle R_842 = [-0.942, -0.742] × [-0.2, 0.2]" question. This gate handles the CONDITIONAL outcome: IF G42 fires FAIL (i.e., DR3 falls outside R_842), classify the sub-scenario.

**Computation steps**:

1. Load `s73_w4_c_dr3_prep.npz` (frozen 2026-04-10). Verify the 7-scenario taxonomy (A1, A2, B1, B2, B3, C1, C2 from S73b W4-C).
2. For each of 7 sub-scenarios, pre-register:
   - The DR3 (w_0, w_a) central values and 2σ rectangles that define the sub-scenario.
   - The framework interpretation (e.g., B1 = CPL w_a-driven exclusion, B2 = w_0-driven, B3 = joint; A-branches = framework consistent with mild inclination; C-branches = extreme Quintom).
   - The post-sub-scenario EVOI rank (which carry-forward computation becomes #1 priority).
3. [AUDIT] Cross-reference with S83 w_0-workshop adjudication: the current canonical w_0 = -0.918 (branch iv); if DR3 falls in A-branch (consistent with -0.918 to -0.95), the branch iv is corroborated; if it falls in B/C, branch iv is disfavored and the dual-pin retirement at S83 is revisited.
4. Document the "NO scheme-shopping, NO retreat to dual-pin" commitment from S83 sagan-synthesis §V.9.
5. Write to §VI.W4-44 with the 7-scenario decision tree, sub-scenario thresholds, and the post-release action matrix.

**Substrate-framing note**: w_0 is the emergent-dark-energy equation of state in the effective FRW description. The framework's -0.918 comes from the Volovik partition + Josephson sector (S58, S83 w_0-workshop). DR3 either lands in the corridor or forces a genuine reassessment.

**Machinery pin (PRDR)**:
- 7-scenario taxonomy: inherited from S73b W4-C (frozen 2026-04-10); no new scenarios added
- Rectangle R_842 boundaries: [-0.942, -0.742] × [-0.2, 0.2] (S83 migration)
- Single-authority freeze: this gate freezes once; post-release application does not re-register
- JSON output schema: {scenario_id, w0_range, wa_range, framework_verdict, evoi_post_release}

**Input SHA-256 pins**:
- `computations/s73_w4_c_dr3_prep.npz` — <computed-at-runtime>
- `computations/s83_w3_g42_dr3_live_watch.npz` — <computed-at-runtime>
- `computations/s83_w0_regulator_workshop_r3.md` (branch iv retention) — <computed-at-runtime>
- `computations/canonical_constants.py` — <computed-at-runtime>

**Expected output 4-tuple**: (value="7-scenario-tree-frozen", scheme="pre-registration", convention="CPL (w_0, w_a)", L_max=N/A)

**PASS**: 7-scenario tree written to `s84_dr3_contingency_fine_grained.json`, SHA logged, all 7 branches with {w_0, w_a, verdict, EVOI-post-release} fields populated.
**INFO**: Tree partially written (5-6 branches).
**FAIL**: Not committed.

**What PASS vs FAIL means**: PASS activates on W1 DR3-RESPONSE FAIL and classifies the sub-scenario without re-registration opportunity. The decision tree is the sole post-release path if the binary G42 rectangle is breached.

**Output files**:
- `computations/s84_w4_dr3_contingency_fine_grained.py`
- `computations/s84_w4_dr3_contingency_fine_grained.json`
- Verdict → `s84_gate_verdicts.txt`
- `sessions/framework/pre-registered-predictions.md` append
- §VI.W4-44

---

## §W4-45. S84-YUKAWA-OOM-ESTIMATOR

**Gate ID**: S84-YUKAWA-OOM-ESTIMATOR
**Trigger**: [VERIFY]
**Classification**: PARTICLE (2-loop SM RGE Yukawa threshold analysis)
**Hypothesis being tested**: A refined OOM estimator reproduces the actual G47 Yukawa shift O(10⁻⁶) to within 30% across at least 3 test cases (not the S83 G47-pre-reg O(10⁻⁴) which was 2 OOM too generous).
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are building a refined OOM estimator for 2-loop + Yukawa-threshold gates. Context: S83-G47 (SIN2-THETA-W-2-LOOP-PLUS-MU-BC) pre-registered Yukawa shift O(10⁻⁴); actual shift was O(10⁻⁶). The gap traces to (a) log-arm length 0.73 (not 1 decade from M_Z to μ_BC = 188 GeV) and (b) partial cancellation in (C_1 - C_2) between up-type and down-type Yukawa contributions.

**Computation steps**:

1. Write analytic formula for 2-loop Yukawa-threshold shift:
   Δ(sin²θ_W) ≈ (α/4π)² · (C_1 Y_t² - C_2 Y_b² - C_3 Y_τ²) · ln²(μ_BC/M_Z)
   with C_1, C_2, C_3 from Mihaila-Salomon-Steinhauser 2012 or equivalent 2-loop threshold calculation.
2. Pin Y_t = 0.993, Y_b = 0.024, Y_τ = 0.010 at M_Z (PDG central values).
3. Log-arm: ln(188.185/91.1876) = ln(2.065) = 0.725 (exact from canonical_constants μ_BC_K3 and M_Z).
4. Evaluate the formula with cancellation terms retained.
5. Test the estimator on 3 cases:
   - Case A: μ_BC = 188.185 GeV (S83 G47 reference) → expected O(10⁻⁶).
   - Case B: μ_BC = 500 GeV → scan up to see log² growth.
   - Case C: μ_BC = 2 TeV → verify the estimator extrapolates correctly.
6. [VERIFY] Substitution chain:
   - Step 1 (definition): Δ(sin²θ_W) at 2-loop = prefactor × Yukawa² × log-arm².
   - Step 2 (substitution): (α/4π)² ≈ 3.3×10⁻⁷; Y_t² ≈ 0.986; ln²(2.065) ≈ 0.526; C_1 ~ O(1).
   - Step 3 (simplification): leading term ≈ 3.3×10⁻⁷ × 0.986 × 0.526 × 1 ≈ 1.7×10⁻⁷; after cancellation with Y_b, Y_τ terms and residual C-factor balance, O(10⁻⁶).
   - Step 4 (direction): estimator shows the O(10⁻⁴) S83 pre-reg was too-generous by factor (1.7×10⁻⁶ / 10⁻⁴) ≈ 0.017, consistent with 2 OOM overestimate.
7. Document the estimator formula and commit to `computations/_yukawa_oom_estimator.py` as reusable utility. Verify all 3 test cases reproduce actual shifts within 30%.
8. Write to §VI.W4-45 with the formula derivation, 3 test cases, and the updated OOM rule for S84+ Yukawa gates.

**Machinery pin (PRDR)**:
- Reference: Mihaila-Salomon-Steinhauser 2012 (2-loop threshold coefficients)
- PDG central values for Yukawa couplings at M_Z
- Test case cardinality: 3 (A, B, C above)
- Acceptance tolerance: ≤30% relative deviation
- L_max: N/A (closed-form 2-loop RGE)

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g47_sin2thetaw_2loop_mu_bc.npz` — <computed-at-runtime>
- 2-loop reference: literature external

**Expected output 4-tuple**: (value=max_rel_dev_3_cases, scheme="2-loop-Yukawa-estimator", convention="PDG Yukawa at M_Z", L_max=N/A)

**PASS**: max |Δ_estimator - Δ_actual| / |Δ_actual| ≤ 0.30 across all 3 cases → estimator calibrated.
**INFO**: max deviation in (0.30, 3.0).
**FAIL**: max deviation > 3.0 → estimator not usable; replace with full 2-loop numerical RGE integration for S84+ gates.

**What PASS vs FAIL means**: PASS gives a reusable utility `_yukawa_oom_estimator.py` that closes the class of pre-reg threshold overestimates at 2-loop. FAIL requires a full numerical 2-loop RGE for every Yukawa gate going forward.

**Output files**:
- `computations/s84_w4_yukawa_oom_estimator.py`
- `computations/s84_w4_yukawa_oom_estimator.npz`
- `computations/_yukawa_oom_estimator.py` (utility, if PASS)
- Verdict → `s84_gate_verdicts.txt`
- §VI.W4-45

---

## §W4-46. S84-G51-LMAX-CONVERGENCE

**Gate ID**: S84-G51-LMAX-CONVERGENCE
**Trigger**: [VERIFY]
**Classification**: GEOMETRIC (spectral truncation convergence test)
**Hypothesis being tested**: The w_0 mixed-scheme canonical value -0.918 converges at L_max ∈ {5, 7, 9} with Δw_0 < 0.005 between L=5 and L=9; this complements SV2 in W1 and provides an independent L_max convergence check on the S83-G51 FAIL (zeta vs Zubarev split at L=5).
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are re-running the G51 w_0 regulator computation at L_max ∈ {5, 7, 9} to distinguish truncation artifact from structural scheme-split. S83-G51 FAIL at L_max=5 showed zeta (-0.998) vs Zubarev (-0.918 in mixed-scheme, or different under strict) at split of 0.08. Question: does the split grow, stay, or shrink with L_max?

**Computation steps**:

1. Import `from canonical_constants import M_KK, tau_fold, F_Josephson, N_cells, Vol_SU3`. Load S83 G51 machinery from `s83_w3_g51_w0_regulator.npz`.
2. At L_max = 5, 7, 9:
   - Compute full D_K eigenvalue spectrum. (L_max=9 requires ~10⁶ eigenvalues → use GPU torch.linalg MANDATORY.)
   - Compute zeta-regulated Volovik partition S_ζ(L_max) and Zubarev-regulated S_Z(L_max).
   - Compute w_0^{zeta}(L_max) = (P_J + P_GGE)/(ρ_J + ρ_GGE)|_ζ and w_0^{Zubarev}(L_max).
3. Report pairs (L_max, w_0^{zeta}, w_0^{Zubarev}, split = w_0^{zeta} - w_0^{Zubarev}).
4. [VERIFY] Direction check:
   - Step 1 (definition): scheme-split = w_0^{zeta}(L) - w_0^{Zubarev}(L).
   - Step 2: at L=5 (S83), split = (-0.998) - (-0.918) = -0.080 (zeta gives MORE NEGATIVE w_0).
   - Step 3: at L=9, if |split(L=9)| < |split(L=5)|, the tension shrinks with L_max → truncation artifact; if grows, structural.
   - Step 4 (direction): shrinks = truncation, grows = structural. No substitution shortcut.
5. Also verify w_0^{Zubarev}(L=9) vs w_0^{Zubarev}(L=5): does the CANONICAL Zubarev value converge to -0.918 ± 0.02?
6. GPU path: use `torch.linalg.eigvalsh` on CUDA; target GPU memory < 17 GB (RX 9070 XT). For L_max=9 matrices ~10⁵ × 10⁵ (sparse block-diagonal), use block-wise eigensolve per SU(3) irrep.
7. Write to §VI.W4-46 with table (L_max, w_0^ζ, w_0^Z, split), convergence verdict, and interpretation per W1 w_0-adjudication context.

**Substrate-framing note**: The spectral truncation L_max is a computational cutoff, not a physical parameter. Convergence under L_max is a test of whether G51's FAIL is an artifact (finite spectrum) or a structural finding (two regulators probe genuinely different substrate functionals).

**Machinery pin (PRDR)**:
- L_max grid: {5, 7, 9}
- Eigenvalue precision: 10⁻¹² relative (torch.linalg.eigvalsh default on float64)
- GPU path: torch.linalg on CUDA; fallback torch CPU if GPU unavailable but NOT numpy
- Convention: mixed-scheme Zubarev (S83 branch iv canonical); zeta-regulator reference
- Scheme: both zeta and Zubarev computed; both reported

**Input SHA-256 pins**:
- `computations/canonical_constants.py` — <computed-at-runtime>
- `computations/s83_w3_g51_w0_regulator.npz` — <computed-at-runtime>
- `computations/s83_w0_regulator_workshop_r3.md` — <computed-at-runtime>

**Expected output 4-tuple**: (value=|w_0(L=9) - w_0(L=5)|_Zubarev, scheme="Zubarev canonical", convention="branch iv", L_max="scan {5,7,9}")

**PASS**: |w_0^{Zubarev}(L=9) - w_0^{Zubarev}(L=5)| < 0.005 AND converged to -0.918 ± 0.02.
**INFO**: Converges but outside ±0.02 band.
**FAIL**: Does not converge (split grows with L_max or oscillates).

**What PASS vs FAIL means**: PASS confirms -0.918 as truncation-stable and strengthens DR3 pre-registration (gates #42-analog, #44). FAIL reopens the w_0 regulator tension as structural, interacting with W1 SV1-SV5 outcomes.

**Output files**:
- `computations/s84_w4_g51_lmax_convergence.py`
- `computations/s84_w4_g51_lmax_convergence.npz`
- `computations/s84_w4_g51_lmax_convergence.png` (w_0 vs L_max by regulator)
- Verdict → `s84_gate_verdicts.txt`
- §VI.W4-46

---

## §W4-47. S84-UHF-GW-THRESHOLD-WATCH

**Gate ID**: S84-UHF-GW-THRESHOLD-WATCH
**Trigger**: [AUDIT]
**Classification**: GEOMETRIC (domain-wall / primordial GW watch)
**Hypothesis being tested**: Pre-register re-migration criterion: if ultra-high-frequency GW detector reaches Ω_GW < 10⁻⁴⁰ at 1 mHz, reclassify S83-G52 C5 WALL (current 46.7 OOM below LISA) from WALL to FALSIFIER.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are pre-registering a migration criterion for the S83-G52 C5 (domain-wall / primordial GW) WALL. Current status: Ω_GW(1 mHz) is 46.7 OOM below LISA sensitivity, making C5 a permanent WALL (undetectable by current and near-future GW observatories). Question: what would have to change in detector capability to lift this WALL?

**Computation steps**:

1. Load S83-G52 result: C5 classification WALL at Ω_GW = Ω_LISA × 10⁻⁴⁶·⁷ at 1 mHz. Pin the framework prediction for Ω_GW(f) across the LISA-DECIGO-BBO-UHF range [10⁻⁴, 10⁵] Hz.
2. Identify the UHF GW detector landscape (2030-2050):
   - UHF GW detectors: Levitated sensors (McCuller et al.), inverse Gertsenshtein effect (Holometer+), cavity-based (ADMX-inspired UHF search), resonant-mass (MiniGrail-successor).
   - Sensitivity floor: literature suggests reach Ω_GW ~ 10⁻⁸ to 10⁻¹² at 10³-10⁷ Hz by 2035-2045.
3. Pre-register the migration threshold: "If ANY UHF GW detector reaches σ(Ω_GW) < 10⁻⁴⁰ at 1 mHz (or equivalent after frequency-rescaling), reclassify C5 from WALL to FALSIFIER."
4. [AUDIT] Current gap: 10⁻⁴⁰ vs framework 10⁻⁴⁶·⁷ = 6.7 OOM margin required before threshold is meaningful. Clearly state this is a long-horizon re-migration (no expected 2026-2035 trigger).
5. Document the WALL-vs-FALSIFIER taxonomy: WALL = provable but undetectable; FALSIFIER = detectable-or-refuted; DETECTOR-STERILE = undetectable even in principle under current physics. C5 is currently WALL; if threshold is crossed, becomes FALSIFIER.
6. Register in `sessions/framework/permanent-results-registry.md` with `WALL-MIGRATION-WATCH-C5` tag.
7. Write to §VI.W4-47 with the migration criterion, the 6.7-OOM gap, and the expected detector-development horizon.

**Substrate-framing note**: C5 is the domain-wall GW channel predicted by the cosmological phase-transition at the fold; its 46.7-OOM suppression below LISA is a consequence of the fold's FIRST-ORDER transition being weakly-coupled in the relevant spectral sector. This is a structural WALL, not a failure — it reflects the substrate's geometric protection.

**Machinery pin (PRDR)**:
- Framework Ω_GW prediction: inherited from S83-G52 (no recomputation)
- UHF detector landscape: literature citation (no files)
- Migration threshold: 10⁻⁴⁰ at 1 mHz (pre-registered; NOT re-set post-detector-release)
- No new numerical computation; registry + watch criteria only

**Input SHA-256 pins**:
- `computations/s83_w3_g52_c5_relabel.npz` — <computed-at-runtime>
- `computations/canonical_constants.py` — <computed-at-runtime>

**Expected output 4-tuple**: (value="watch-criterion-registered", scheme="UHF-GW-migration", convention="Ω_GW at 1 mHz", L_max=N/A)

**PASS**: Watch criterion registered with explicit threshold 10⁻⁴⁰, taxonomy (WALL→FALSIFIER) defined, 6.7-OOM gap documented.
**INFO**: Registered without threshold.
**FAIL**: Not registered.

**What PASS vs FAIL means**: PASS keeps C5 on the registry as a LIVE-WATCH-MIGRATABLE WALL. FAIL lets C5 drift as detector-sterile with no formal migration path.

**Output files**:
- `computations/s84_w4_uhf_gw_threshold_watch.py` (registry writer)
- Verdict → `s84_gate_verdicts.txt`
- `sessions/framework/permanent-results-registry.md` append
- §VI.W4-47

---

## §W4-48. S84-FALSIFIER-RIGOR-REGISTRY

**Gate ID**: S84-FALSIFIER-RIGOR-REGISTRY
**Trigger**: [AUDIT]
**Classification**: NON-PHONONIC (methodology / registry audit)
**Hypothesis being tested**: Every framework falsifier channel is tagged with one of 4 rigor flags: ZERO-FREE-PARAMETER / ACCOMMODATION / SCHEME-DEPENDENT / DETECTOR-STERILE; no channel is un-tagged.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are building the FALSIFIER-RIGOR-REGISTRY that tags every framework falsifier channel with a rigor flag. This closes a methodological gap identified in S83 sagan-synthesis §V (three-axis distinction: framework-internal consistency ≠ prediction-pinning tightness ≠ detector-reach). The 4 rigor flags:

- **ZERO-FREE-PARAMETER**: Prediction derived from substrate eigenvalue problem with NO free parameter; LCDM-match under these terms is genuine evidence.
- **ACCOMMODATION**: Framework is consistent with the data but one or more parameters were tuned to match; evidence weight is 1× (not >1×).
- **SCHEME-DEPENDENT**: Prediction magnitude or sign depends on regulator/scheme choice that has not been canonicalized; in the data-agreement column but flagged for resolution.
- **DETECTOR-STERILE**: Prediction is structural but outside all current and near-future (2030-2040) detector reach; no discrimination possible in window.

**Computation steps**:

1. Enumerate ALL framework falsifiable / pre-registered observables:
   - n_s (S83-G48 PASS)
   - r (G46 PASS)
   - n_T (G50 transit + G46 CMB — different flags per scale)
   - α_s (S50 permanent, CMB-S4 34σ)
   - m_H (S83 bi-criterion μ_BC provisional)
   - sin²θ_W (G47 PASS)
   - A_s (G10 PASS via 3PI)
   - f_NL (S67 f_NL_total=1.03)
   - α_f_NL (#38 output)
   - w_0 (branch iv -0.918)
   - w_a (CPL-derivative of w_0)
   - μ (FIRAS-Chluba, S82 PASS)
   - Ω_GW (C5 domain-wall, detector-sterile)
   - σ_8 (S69 fsig8)
   - C_cons (G44 FAIL; detector-sterile)
   - (L+R ≥ 16 channels total)

2. For each channel, assign rigor flag WITH justification:
   - ZERO-FREE-PARAMETER: e.g., α_s = n_s² - 1 (S50 permanent identity); m_H framework 97 GeV (if derives from a_6/a_4); n_s from Bogoliubov-inversion triple.
   - ACCOMMODATION: e.g., μ_BC fit to PDG-sin²θ_W under cube-3 override (bi-criterion in progress).
   - SCHEME-DEPENDENT: e.g., w_0 under Zubarev vs zeta split (G51 FAIL); A_s under R3 vs R5 regulator.
   - DETECTOR-STERILE: e.g., n_T(k_CMB) 10⁻⁴ vs σ_LB 0.05 (gate #41); Ω_GW(1 mHz) 46.7 OOM below LISA (#47); C_cons 23× above PASS (G44).

3. [AUDIT] Audit the existing registry entries in `sessions/framework/pre-registered-predictions.md` and `permanent-results-registry.md`; verify every channel has one and only one flag.

4. Build the registry as a table: {channel_id, rigor_flag, justification_text, dependent_gates, registry_location}. Commit to `computations/s84_falsifier_rigor_registry.json` with SHA.

5. Write to §VI.W4-48 with the full 16-row table, the 4-flag legend, the audit completeness check, and the "ZERO-FREE-PARAMETER count" headline (framework's strongest evidence column).

**Substrate-framing note**: This is a meta-registry; the physics content is inherited. The value is methodological rigor — preventing a SCHEME-DEPENDENT prediction from being cited as evidence-for-framework alongside a ZERO-FREE-PARAMETER prediction.

**Machinery pin (PRDR)**:
- Channel enumeration: ≥ 16 (from §5 structural harvest + §4.A-D carry-forward)
- Flag taxonomy: exactly 4 (as defined above); no fallback category
- Justification requirement: 1-3 sentences per channel with specific gate citation
- Audit completeness: 0 un-flagged channels tolerated

**Input SHA-256 pins**:
- `sessions/framework/pre-registered-predictions.md` — <computed-at-runtime>
- `sessions/framework/permanent-results-registry.md` — <computed-at-runtime>
- `computations/s83_gate_verdicts.txt` — <computed-at-runtime>
- `computations/s82_gate_verdicts.txt` — <computed-at-runtime>

**Expected output 4-tuple**: (value="N_channels_flagged / N_channels_total", scheme="4-flag-taxonomy", convention="S84 rigor registry", L_max=N/A)

**PASS**: N_flagged / N_total = 1.0 (all channels flagged); ZFP count ≥ 3; no un-tagged channel.
**INFO**: 0.8 ≤ ratio < 1.0.
**FAIL**: ratio < 0.8.

**What PASS vs FAIL means**: PASS distinguishes which of the framework's observational claims have zero-free-parameter strength vs which are accommodation vs scheme-dependent vs sterile. This directly feeds the framework-status narrative and prevents evidence-inflation. FAIL means some channels remain ambiguous and cannot be cited as load-bearing.

**Output files**:
- `computations/s84_w4_falsifier_rigor_registry.py`
- `computations/s84_w4_falsifier_rigor_registry.json`
- Verdict → `s84_gate_verdicts.txt`
- `sessions/framework/falsifier-rigor-registry.md` (new file)
- §VI.W4-48

---

## §W4-49. S84-P-OBS-ALIGNED-CEILING

**Gate ID**: S84-P-OBS-ALIGNED-CEILING
**Trigger**: [VERIFY]
**Classification**: NON-PHONONIC (ceiling-lifting chain registration)
**Hypothesis being tested**: The 7/9 → 8/9 → 9/9 P_obs_aligned ceiling-lifting chain is pre-registered with explicit dependency graph showing which gate ACTIVATES each transition.
**Agent**: `mack-cosmic-bridge`
**Model**: opus

**Prompt**:

You are pre-registering the ceiling-lifting chain for P_obs_aligned (S83-G48 PASS at 7/9 = 0.7778). Current: 7/9 PASS, 2 FAILs at sin²θ_W (downgraded) and α_s. Gates to lift the ceiling are already identified in other waves / carry-forwards; this gate makes the lifting chain FORMAL.

**Computation steps**:

1. Load current P_obs_aligned state from `s83_w3_g48_p_obs_aligned.npz` or equivalent. Confirm 7/9 PASS breakdown: PASS = {n_s, r, m_H (bi-criterion), N_eff, w_0, f_NL, A_s (via 3PI)}; FAIL = {sin²θ_W, α_s}. (INFO row may be absent or resolved per G48 co-PASS logic.)

2. Identify the ceiling-lifting gates from §4 carry-forward:
   - **sin²θ_W PASS activation**: Requires μ_BC geometric derivation (§4.K: DERIV-I cube-3 override, DERIV-II C² block omission). Pre-reg ref: S84-DERIV-I, S84-DERIV-II, S84-TAU-CROSS-SCALE.
   - **α_s PASS activation**: Requires multifield-transfer-function resolution (N1 TRANSFER-FUNCTION-74, EVOI rank 1) OR CMB-S4 projection refinement (#52 S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT).

3. Build dependency graph as directed acyclic:
   ```
   7/9 → 8/9:
     Trigger A1: S84-DERIV-I PASS ∧ S84-DERIV-II PASS → sin²θ_W PASS → 8/9
     Trigger A2: S84-TAU-CROSS-SCALE PASS (alternative route) → sin²θ_W PASS → 8/9

   8/9 → 9/9:
     Trigger B1: N1 TRANSFER-FUNCTION-74 PASS → α_s PASS → 9/9
     Trigger B2: #52 S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT PASS (projection tightens by 5×) → α_s PASS → 9/9
   ```

4. [VERIFY] Dependency-graph validation:
   - Step 1 (definition): each transition requires at least one trigger gate PASS.
   - Step 2 (substitution): A1/A2 are disjunctive for sin²θ_W (either path activates); B1/B2 are disjunctive for α_s.
   - Step 3 (simplification): minimum path 7/9→9/9 = (A1 OR A2) AND (B1 OR B2) = at most 4 gate dependencies.
   - Step 4 (direction): ceiling-lifting is monotone (no unlift; gate-PASS is permanent per gate-verdicts rule).

5. Document the dependency graph as a JSON + ASCII diagram. Commit to `s84_p_obs_aligned_ceiling_chain.json` with SHA.

6. Register in `sessions/framework/pre-registered-predictions.md` with tag `P-OBS-ALIGNED-CEILING-CHAIN`.

7. Write to §VI.W4-49 with the DAG, the 4 trigger gates, the post-lift evidence column expansion (what each sin²θ_W or α_s PASS adds to the framework narrative), and explicit note that this is a SEQUENTIAL pre-registration (ceilings may lift individually before the chain completes).

**Substrate-framing note**: P_obs_aligned is not a hypothesis-test statistic — it is a bookkeeping metric tracking how many of 9 canonical observables the framework matches within 2σ under its canonical predictions. Its ceiling-lifting is a registry event, not a physics event. The physics events are the individual trigger gates.

**Machinery pin (PRDR)**:
- P_obs_aligned denominator: 9 (fixed)
- Current state: 7/9 PASS (S83-G48); 2 active FAIL (sin²θ_W, α_s)
- Trigger gates: DERIV-I, DERIV-II, TAU-CROSS-SCALE (sin²θ_W path); N1 TRANSFER-FUNCTION-74, #52 (α_s path)
- JSON schema: {current_state, triggers_to_8_9: [A1, A2], triggers_to_9_9: [B1, B2], DAG_edges, sha}
- Freeze: single-authority pre-registration (2026-04-18); no re-registration on partial PASS

**Input SHA-256 pins**:
- `computations/s83_w3_g48_p_obs_aligned.npz` — <computed-at-runtime>
- `computations/canonical_constants.py` — <computed-at-runtime>
- `sessions/session-plan/session-84-plan-w1.md` (for N1 ref) — <computed-at-runtime>
- `sessions/session-plan/session-84-plan-w2.md` (for S84-DERIV-I/II/TAU-CROSS-SCALE refs) — <computed-at-runtime>

**Expected output 4-tuple**: (value="chain-registered", scheme="DAG-4-trigger", convention="P_obs_aligned 9-observable denom", L_max=N/A)

**PASS**: DAG written with 4 triggers, JSON frozen, SHA logged, registry entry filed.
**INFO**: DAG partially specified.
**FAIL**: Not committed.

**What PASS vs FAIL means**: PASS makes the 7/9 → 9/9 chain a FORMAL sequence — each ceiling-lift event is anticipated and its activating gate is pre-named. FAIL means post-hoc interpretation of ceiling lifts (unacceptable for a registry-driven framework).

**Output files**:
- `computations/s84_w4_p_obs_aligned_ceiling.py`
- `computations/s84_w4_p_obs_aligned_ceiling_chain.json`
- `computations/s84_w4_p_obs_aligned_ceiling.png` (DAG diagram)
- Verdict → `s84_gate_verdicts.txt`
- `sessions/framework/pre-registered-predictions.md` append
- §VI.W4-49

---

## Wave 4 → Wave 5 Decision Point

**After Wave 4 completes** (batch-A and batch-B both returned, all 13 verdicts appended to `s84_gate_verdicts.txt`):

- **If #38 α_framework PASS AND #43 SKA-1 SNR ≥ 2**: 2027-2029 α_f_NL discriminator ACTIVE. Flag in Wave 5 master synthesis as the leading 2020s-2030s live falsifier.
- **If #38 α_framework FAIL OR |α| < 0.3**: SKA-2 (2032-2035) becomes sole α_f_NL channel; 21-cm tomography flagged as structural alternative. Forward to Wave 5 for the master synthesis's "sole-channel watch" section.
- **If #37 PASS (σ(n_T)_joint ≤ 0.04)**: LiteBIRD + CMB-S4 joint B-mode reach crosses structural threshold. Wave 5 registry note: gate #41 (inaccessibility) is conditional on LiteBIRD-alone forecast; joint forecast may unlock decade discrimination under certain reheating scenarios.
- **If #37 FAIL**: gate #41 fully armed as structural permanent-result. Wave 5 includes #41 in framework-status synthesis.
- **If #39 FAIL (n_T(k_CMB) not reproducing -3e-3)**: G46 transfer-kernel derivation has a gap. Forward to Wave 5 as immediate follow-up computation at HIGH EVOI.
- **If #40 FAIL (fine-tuning flag fires)**: n_T(k_CMB) is declared SCHEME-DEPENDENT in gate #48 registry. Re-audit #41 under new flag.
- **If #46 FAIL (L_max divergence)**: w_0 regulator tension is structural; Wave 5 must re-open the W1 adjudication outcomes (SV1-SV5) under the L_max-divergent interpretation.
- **If #45 FAIL (Yukawa estimator not calibrated)**: Replace with full 2-loop numerical RGE for all Yukawa gates; Wave 5 flags this as methodology-infra debt.
- **If #48 FAIL (registry incomplete)**: framework narrative has ambiguity on evidence-column strength; Wave 5 synthesis must be careful not to cite un-flagged channels as load-bearing.
- **If #49 FAIL (DAG not filed)**: ceiling-lifting events become post-hoc; Wave 5 must explicitly label any G48 update as unregistered.
- **All 13 PASS/INFO (no FAIL)**: Wave 5 can proceed to full observational-roadmap synthesis without Wave-4 re-dispatch.

**Explicit Wave 5 carry-forward from Wave 4** (regardless of verdict):
- #38 α_framework value → Wave 5 master synthesis §V (if #38 returned a value).
- #42 frozen BK decision tree → publication-track artifact, cite in Wave 5 framework-status narrative as active falsifier.
- #44 frozen DR3 sub-scenario tree → similar.
- #47 UHF GW threshold → watch-list item.
- #48 rigor registry → load-bearing for Wave 5 evidence accounting.

---

## Wave 4 Machinery-Enumeration Pin (§0.11)

This section pins every gate-relevant machinery parameter to eliminate PRU (Pre-Registration Underspecification).

### Free parameters enumerated per gate

**#37 (LB-CMBS4-JOINT)**:
- LiteBIRD noise σ_3yr (pinned: 2.16 μK-arcmin)
- CMB-S4 noise σ (pinned: 1.0 μK-arcmin)
- Delensing fraction LB (pinned: 50%); S4 (pinned: 90%)
- f_sky LB (pinned: 0.70); S4 (pinned: 0.40)
- ell range for Fisher integral (pinned: [2, 300] LB; [50, 3000] S4)
- Fisher stencil (pinned: 5-point centered)
- Fiducial (r, n_T) (pinned from G46, G50: (0.0117, -0.003024))
- A_lens fiducial (pinned: 1.0)
- Tensor transfer T(k) scheme (diagnostic: CAMB vs analytic; to be declared in script)

**#38 (ALPHA-F-NL)**:
- k_pivot (pinned: 0.05 Mpc⁻¹)
- k_transit (pinned: 587 M_KK from G46)
- Derivative stencil (pinned: 4-point in ln k over [k_pivot/2, 2 k_pivot])
- L_max (pinned: 5 primary; cross-check 7)
- GGE channel weights (pinned: f_NL^equil=0.853, folded=0.129, multi=0.56 from S67)
- Bispectrum template (pinned: Planck 2018 equilateral)
- M_KK uncertainty for error budget (diagnostic: 1% nominal; to be reported)

**#39 (N_T-CMB-TRANSFER)**:
- ε_H value (pinned: 0.02163 canonical)
- k range for transfer (pinned: [k_CMB, k_transit] = 54 decades)
- Transfer-kernel scheme (pinned: G46 ε_H-flow)
- Slow-roll consistency relation check (diagnostic: n_T = -r/8 comparison to n_T = -2ε_H)

**#40 (N_T-FWHM-SENSITIVITY)**:
- FWHM scan range (pinned: [0.5e-3, 3e-3] log-spaced 10 points)
- FWHM baseline (pinned: 1.65e-3 from S83-G31)
- Derivative stencil (pinned: 5-point centered)
- L_max (pinned: 5)
- Fine-tuning threshold (pinned: 500 per unit FWHM; INFO at 2000)

**#41 (BLUE-TRANSIT-TILT-INACCESSIBILITY)**:
- No numerical machinery; bookkeeping gate.
- Registry target (pinned: `sessions/framework/permanent-results-registry.md`)
- EVOI-entry target (pinned: `sessions/evoi-framework.md`)

**#42 (BK-ARRAY-PRE-REG)**:
- r framework prediction (pinned: 0.01173 from G46)
- σ_r_BK_2026 forecast (pinned: 0.005 from Ade+ 2025 literature)
- Decision-tree thresholds (pinned: Branch A [0.009, 0.015]; B < 0.020; C > 0.025; D upper < 0.008)
- Freeze date (pinned: 2026-04-18)

**#43 (SKA-1-ALPHA-SNR)**:
- σ(α)_SKA1 (pinned: 5.118 from G45)
- σ(α)_SKA2 (pinned: 0.80 from G45 PASS)
- α_framework source (from #38; DEPENDENCY)
- SNR threshold (pinned: 2)

**#44 (DR3-CONTINGENCY-FINE)**:
- 7-scenario taxonomy (pinned: S73b W4-C frozen 2026-04-10)
- Rectangle R_842 (pinned: [-0.942, -0.742] × [-0.2, 0.2])
- JSON schema (pinned per gate spec)

**#45 (YUKAWA-OOM)**:
- Yukawa couplings at M_Z (pinned PDG: Y_t=0.993, Y_b=0.024, Y_τ=0.010)
- 2-loop coefficients (pinned: Mihaila-Salomon-Steinhauser 2012)
- Test-case cardinality (pinned: 3)
- Acceptance tolerance (pinned: 30% relative)

**#46 (G51-LMAX-CONVERGENCE)**:
- L_max grid (pinned: {5, 7, 9})
- Eigenvalue precision (pinned: 1e-12)
- GPU path (pinned: torch.linalg on CUDA)
- Convergence threshold (pinned: 0.005)
- Band (pinned: -0.918 ± 0.02)

**#47 (UHF-GW-THRESHOLD)**:
- Migration threshold (pinned: 10⁻⁴⁰ at 1 mHz)
- Framework prediction (pinned: from S83-G52)
- No new numerical machinery

**#48 (FALSIFIER-REGISTRY)**:
- Channel enumeration (pinned: ≥ 16 from §5 + §4)
- Flag taxonomy (pinned: 4 classes as defined)
- Audit completeness (pinned: 100%)

**#49 (P-OBS-ALIGNED-CEILING)**:
- Denominator (pinned: 9)
- Current state (pinned: 7/9 from S83-G48)
- Trigger gates (pinned: DERIV-I, DERIV-II, TAU-CROSS-SCALE, N1, #52)

### PRDR dry-run verdict

All 13 gates have their machinery parameters enumerated above. Free-parameter count per gate: #37=9, #38=7, #39=4, #40=5, #41=0 (bookkeeping), #42=5, #43=4, #44=3, #45=5, #46=5, #47=2, #48=3, #49=5. No parameter declared diagnostic-only without substitution-chain impact.

---

## Wave 4 Input-SHA Ledger

| Gate | Input files (computed-at-runtime SHAs) |
|:-----|:--------------------------------------|
| #37 | canonical_constants.py, s83_w3_g43_litebird_sigma_nT_reach.npz, s83_w3_g46_tensor_transfer.npz |
| #38 | canonical_constants.py, s67_gge_bispectrum.npz, s63_running_ns.npz, s65_blue_tensor_tilt.npz |
| #39 | canonical_constants.py, s83_w3_g46_tensor_transfer.npz, s65_blue_tensor_tilt.npz, s66_tensor_transfer.npz |
| #40 | canonical_constants.py, s83_w3_g31_backreact_tauwindow.npz, s65_blue_tensor_tilt.npz |
| #41 | s68_liteb_r_forecast.npz, s83_w3_g43_litebird_sigma_nT_reach.npz, s83_w3_g46_tensor_transfer.npz, s83_w3_g50_nT_bogoliubov.npz, s84_w4_lb_cmbs4_joint_sigma_nt.npz (#37), s84_w4_nt_cmb_transfer.npz (#39) |
| #42 | canonical_constants.py, s83_w3_g46_tensor_transfer.npz |
| #43 | canonical_constants.py, s83_w3_g45_21cm_sigma_alpha_fnl.npz, s84_w4_alpha_fnl_framework_pred.npz (#38) |
| #44 | s73_w4_c_dr3_prep.npz, s83_w3_g42_dr3_live_watch.npz, s83_w0_regulator_workshop_r3.md, canonical_constants.py |
| #45 | canonical_constants.py, s83_w3_g47_sin2thetaw_2loop_mu_bc.npz |
| #46 | canonical_constants.py, s83_w3_g51_w0_regulator.npz, s83_w0_regulator_workshop_r3.md |
| #47 | s83_w3_g52_c5_relabel.npz, canonical_constants.py |
| #48 | sessions/framework/pre-registered-predictions.md, sessions/framework/permanent-results-registry.md, s83_gate_verdicts.txt, s82_gate_verdicts.txt |
| #49 | s83_w3_g48_p_obs_aligned.npz, canonical_constants.py, sessions/session-plan/session-84-plan-w1.md, sessions/session-plan/session-84-plan-w2.md |

All SHAs are computed-at-runtime; each script MUST log the 64-char SHA-256 of every input in the first 20 lines of stdout per `gate-verdicts.md` §S81+ canonical form. Closure SHA written as final canonical verdict-line component.

### Verdict-line canonical form (all 13 gates)

```
S84-<GATE>: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> audit_sha256=<64-char> content_sha256=<64-char>
```

Dual-SHA per S84+ introduction (schema_version=S84+, from §4.J #99 of context). Both SHAs are 64-char hexdigest.

---

**End of Wave 4 plan.**
