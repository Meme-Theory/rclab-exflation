# Session 85 Synthesis: S-7 Combined Landscape (mack)

**Date**: 2026-04-25
**Agent**: mack-cosmic-bridge
**Source Documents**:
- `sessions/archive/session-85/session-85-w0-workingpaper.md`
- `sessions/archive/session-85/session-85-w1a-workingpaper.md`
- `sessions/archive/session-85/session-85-w1b-workingpaper.md`
- `sessions/archive/session-85/session-85-w1c-workingpaper.md`
- `sessions/archive/session-85/session-85-w2-workingpaper.md`
- `sessions/archive/session-85/session-85-w3-workingpaper.md`
- `sessions/archive/session-85/session-85-w4-workingpaper.md`
- `sessions/archive/session-85/session-85-w5-workingpaper.md`
- `sessions/archive/session-85/workshops/s85-w1-cutoff-authority-adjudication.md`
- `sessions/archive/session-85/workshops/s85-w2-as-band-authority.md`
- `sessions/framework/cross-channel-correlation-matrix.md` (W4-2 canonical registry)
- `sessions/framework/falsifier-watchlist.md` (W4-8 augmented registry)
- `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md`

---

## I. Session Outcome

S85 W0-W5 closes the observational-pipeline pre-registration scaffolding for the substrate's 2026-2030 detector window. Two flagship pre-registrations are now SHA-pinned and event-locked: DESI DR3 w_0 (window opened 2026-04-23, R_842 rectangle) and CMB-S4 β_s (60.5σ single-channel, 2028 launch); a third (BK-Array 2026 r) and a fourth (LiteBIRD 2030 r) are sequenced behind. The W2 A_s band-authority workshop reframed r from a single-pre-registration falsifier into a BOTH-Pathways internal-consistency discriminator AND live-watch falsifier under a 4-level unit-class taxonomy with FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030. The principal observational gates carry across S86: a structural-floor on LiteBIRD n_T (W1a-8, separation 588.78 ≫ 100), a 7D Fisher log10(BF_FW/LCDM) = +827.93 conditional on framework correctness (W1a-9), and a layer-conditional DR3 7-cell tree (W1b-1 FAIL on cell-flip across L_max ∈ {10, 12}).

---

## II. Key Results

### II.1 P_obs_aligned — Updated Observational Priority Table (2026-04-25 snapshot)

**Result**: Per-channel observational priority for S86-S95 ranked by P(decisive_result_by_year) × |ΔP_framework|, with W4-3 f_indep=0.8731 and W4-6 geometric-mean correlation discount 0.9926 folded in. **NON-PHONONIC** (pipeline-level priority artifact; the underlying predictions are PHONONIC fiber-eigenvalue-moment outputs).

**Substitution chain for the priority metric** (mandatory per `.claude/rules/math-scripts.md`):

```
Step 1 (definition):
  Priority_i = P(decisive_by_year_i) · |ΔP_framework_i|
  decisive   = |σ-distance| ≥ 3 (per W4-7 falsifier-σ-distance convention)
  ΔP_framework = Bayesian update on framework status conditional on detection / null

Step 2 (substitute):
  P(decisive | DESI DR3 by 2027)        = 1.0 (window opened 2026-04-23)
  P(decisive | CMB-S4 β_s by 2028)      = 1.0 (60.5σ single-channel)
  P(decisive | BK-Array 2026 r)         = ~0.6 (4-branch tree, 1.42σ marginal at Path-H)
  P(decisive | LiteBIRD 2030 r)         = 1.0 conditional on Path-H/Path-C
  P(decisive | LiteBIRD 2030 n_T)       = 0 (STRUCTURAL-FLOOR per W1a-8; r=16ε INAPPLICABLE)
  P(decisive | PIXIE 2029+ μ)           = 1.0 (8693σ pull per W0-8)
  P(decisive | CMB-HD 2035 α_s)         = 0.7 (5.155σ in W4-7; subject to W1b-6 PRE-REG-INCOMPLETE)
  P(decisive | SKA-1 2030 f_NL_folded)  = 0.05 (0.011σ; W4-7; SKA-2+ retains potential)
  P(decisive | LISA 2035+ CGWB)         = 1.0 (SNR=1.68×10^13, W1a-7)

Step 3 (simplify): pull |ΔP_framework| from W1a-9 7D Fisher chi² decomposition:
  β_s contributes 3660/3813 of the chi² (W1a-9 line 337) ⇒ |ΔP_framework|_β_s = LARGE
  r contributes 138/3813 (W1a-9 line 332) ⇒ |ΔP_framework|_r = MEDIUM
  μ-distortion at PIXIE ⇒ |ΔP_framework|_μ = LARGE (4-OOM separation, W0-8)
  w_0 ⇒ |ΔP_framework|_w0 = LARGE-conditional-on-DR3 (R_842 binary lockout)

Step 4 (direction):
  Decisive AND large-ΔP_framework channels rank highest:
  PIXIE_μ ~ DESI_DR3_w0 ~ CMB-S4_β_s > LISA_CGWB > LiteBIRD_r > CMB-HD_α_s > BK-Array_r >> SKA-1_f_NL.
```

**P_obs_aligned ranking (sole-purpose synthesis output)**:

| # | Channel | Detector reach date | Substrate moment probed | P(decisive) | \|ΔP_FW\| | Priority class |
|:--|:--------|:--------------------|:------------------------|:------------|:----------|:---------------|
| 1 | μ-distortion K-endpoint | PIXIE 2029+ | a_2 spectral GGE thermodynamic K-endpoint at γ=1 lockout | 1.0 | LARGE (8693σ; 4-OOM separation) | FLAGSHIP |
| 2 | w_0 dark energy | DESI DR3 (window opened 2026-04-23, public release ~2027) | a_0 Volovik partition / impedance leakage Γ=0.99970 | 1.0 | LARGE (3.28σ; binary R_842 lockout) | FLAGSHIP |
| 3 | β_s running-of-running | CMB-S4 2028 | 2nd Mellin-cone curvature at τ_fold via a_4 Seeley-DeWitt | 1.0 | LARGE (60.5σ; LCDM-null structural exclusion) | FLAGSHIP |
| 4 | CGWB amplitude | LISA 2035+ | Tensor-sector spectral action at fold | 1.0 | LARGE (SNR=1.68×10^13 fix-k-dominant) | FLAGSHIP |
| 5 | r tensor-to-scalar | LiteBIRD 2030 (decisive); BK-Array 2026 (sequenced upstream) | Tensor sector Dirac spectrum (B-mode) | 1.0 / ~0.6 | MEDIUM-LARGE (Path-H 5.82σ-Path-C 9.17σ at LiteBIRD; 1.42σ marginal at BK-Array) | FLAGSHIP-SEQUENCED |
| 6 | α_s scalar running | CMB-HD 2035; CMB-S4 2028 | 2nd derivative d²S_transfer/dk² at k_pivot | 0.7 / 1.0 | MEDIUM (S4 +2.70σ; HD +5.155σ; common-mode discount 0.9709 per W4-6) | SECONDARY-JOINT |
| 7 | f_NL folded bispectrum | SKA-1 2030 (undetectable); next-gen 21-cm post-2035 | 3-pt spectral moment at GGE acoustic 3-pt | 0.05 / future | SMALL (0.011σ at SKA-1; folded NG = 0.0547) | LONG-TERM |
| 8 | n_T tensor tilt at CMB | LiteBIRD 2030 | Tensor moment redshifted via S66 14.3× transfer suppression | 0 (STRUCTURAL-FLOOR) | NONE (separation 588.78 from transit; r=16ε INAPPLICABLE) | STRUCTURAL-FLOOR |

**Correlation discounts applied**: f_indep = 0.8731 (W4-3, BAO-CMB shared r_d ladder, ρ=0.35), geometric-mean discount 0.9926 (W4-6, common-mode CMB-S4 × CMB-HD α_s pair (0,3), ρ=0.7). The α_s common-mode pair is the only non-trivial discount; all other pair entries are INDEPENDENT.

**Dual-channel-conditional**: post-DR3 (W1a-5), post-BK (W1a-4), and post-DR3-L_max-sub-tree (W1b-1) verdicts cascade into the joint Fisher (W1a-9) and the joint α_s × w_0 evidence ledger (W1b-10 PENDING-EVENT BF_indep = 10.75 with D := |log10(BF_joint) − log10(BF_indep)| pending DR3 + joint MCMC).

---

### II.2 Flagship Certifications (W0-W5 SHA-pinned pre-registrations)

**Result**: Eleven flagship pre-registrations and registry landings, each with dual-SHA closure on canonical input pin maps. **META** (pre-registration ledger entries; underlying observables are PHONONIC).

| Tag | Gate | Value (4-tuple) | content_sha₁₆ | Detector window | Pre-reg semantics |
|:----|:-----|:----------------|:--------------|:----------------|:------------------|
| W0-1 BETA-S-CMB-S4 | S85-BETA-S-CMB-S4-PREREG | β_s = −0.1331; σ_S4 = 2.2×10⁻³; pull = 60.5 (4-tuple: 60.5, MS-bar, Planck-central, L_max=8) | `cf3648a5f657275f...` | CMB-S4 launch 2028 | LCDM-null discriminator at single-channel ≥ 60σ |
| W0-8 PIXIE μ-K-ENDPOINT | S85-PIXIE-MU-K-ENDPOINT-PREREG | μ_FW = 8.69×10⁻⁵ at K_endpoint=3.556×10⁵ at γ=1 lockout; pull = 8693 (4-tuple: 8693, Chluba-Sunyaev-2012, γ-lockout, L_max=8) | `fad10105e7683657...` | PIXIE 2029+ | 4-OOM separation from LCDM μ ≈ 2×10⁻⁸; γ-lockout exact (residual 6.66e-16) |
| W1a-4 BK-ARRAY-LIVEWATCH | S85-W1a-BK-ARRAY-2026-LIVEWATCH | r_FW = 0.011732; 4-branch tree (Branch 1 r<0.005 FAIL, Branch 2 [0.005,0.018] PASS, Branch 3 [0.018,0.030] INFO, Branch 4 r≥0.030 FAIL) | `c96aedb08fce68e2...` (echoes S84 W4-42 SHA `e2ca24d6...`) | BK-Array 2026 release | 4-branch decision tree; FROZEN S84 W4-42 |
| W1a-5 DR3-LIVEWATCH | S85-W1a-DR3-LIVEWATCH | (w_0_FW, w_a_FW) = (−0.918, 0); R_842 = [−1.05,−0.85] × [−0.2,0.2]; 7-cell tree A1/A2/B1/B2/B3/C1/C2 | `123c0ced62898f29...` (echoes S84 W1b-9 SHA `9cc7f47e...`) | Window opened 2026-04-23; release ~2027 | Binary R_842 containment + cell classifier; LOCKOUTS A-F per S84 W1b-9 |
| W1a-6 LISA-FIX-K-FIX-F | S85-W1a-LISA-CGWB-FLAGSHIP-FIX-K | ratio (fix-f/fix-k) = 1.1333 vs target 1.133; residual 3.33e-4 (PASS ≤ 1e-3) | `2d938c61d6744f51...` | LISA 2035+ | Dual-convention pre-registration consistent at residual < 1e-3 |
| W1a-7 LISA-DECISIVE | S85-W1a-LISA-FLAGSHIP-FIX-TIGHTENING | SNR = 1.68×10¹³ vs threshold 5; 11-OOM margin from S84 W6-50 | `7d5cdb9338d794da...` | LISA 2035+ | Decisive at 3σ-tightening of error budget σ_fix_kf=1e-3, σ_cS=5e-2, σ_transit=2e-2 |
| W1a-8 LITEBIRD-N_T-STRUCTURAL-FLOOR | S85-W1a-LITEBIRD-NT-REGISTRY-LANDING | separation_normalized = 588.78 ∈ [540, 654] (S84 W4-41 reproducibility); robust σ_LB ∈ {1×10⁻⁴, 8×10⁻⁴, 8×10⁻³} | `0c1ab0e9ab063c59...` | LiteBIRD 2030 | n_T NOT a falsifier — 54-decade k-space transfer geometric, EVOI = 0 through 2040 |
| W1a-9 7D-FISHER | S85-W1a-MULTID-FISHER-FRAMEWORK | log10(BF_FW/LCDM) = +827.93; χ²_total = 3812.74; β_s contributes 3660/3813, r contributes 138/3813; subset cross-check 14.86 vs S84 W4-49 target 13.9 (within 7%) | (script-canonical) | All 7 channels by 2030 | Conditional discrimination IF framework correct |
| W1b-2 ALPHA-S-FISHER-CORRELATED | S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED | σ_corr/σ_diag = 1.1298 < 1.25 PASS threshold; 5×5 block-diagonal correlation matrix (S4-HD ρ=0.30, S4-LB ρ=0.15) | (verdict-line) | All α_s detectors | W1a-9 ensemble robust under correlated inference (~13% widening) |
| W1b-5 BETA-S-JOINT-S4-HD | S85-W1b-BETA-S-JOINT-S4-HD | σ_joint(β_s) = 1.279×10⁻³; tightening ratio 0.581 (41.9%); pull joint = 104σ vs single-channel 60.5σ | `ef098034bb08b613...` | CMB-S4 2028 + CMB-HD 2035 | Doubly decisive at 104σ from joint S4×HD |
| W3-1 PIXIE-K-FIRAS-PREREG | S85-W3-CF-5-PIXIE-KMFIRAS-PREREG | μ_canonical = 8.69×10⁻⁵; 5-regulator spread = 0.000 exact at K_FIRAS (γ=1 lockout fixes regulator-swap Jacobian to unity) | `4e7a06dfb45c62f3...` | PIXIE 2029+ | Regulator-invariant by construction (Step 3: γ=1 ⇒ (1−γ)=0 ⇒ all regulator factors collapse to canonical) |
| W4-4 5-CHANNEL-CERT | S85-W4-4-FALSIFIER-WATCH-CERT | 5/5 channels certified (CMB-S4 α_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD α_s, 21-cm folded f_NL) | `d31957202c4582a3...` | 2026-2030 roster | Sealed certification rows (detector, year, σ-prediction, xcorr class, EVOI) |
| W4-6 5-CHANNEL-FISHER | S85-W4-6-MULTI-D-JFD | Geometric-mean discount = 0.9926; α_s common-mode discount = 0.9709 (CMB-S4 × CMB-HD ρ=0.7, F_full[0,0]=8.77×10⁵ vs indep 1.05×10⁶) | `ccb38ea605c1d776...` | All 4 substrate-parameters by 2035 | Identity residual 0 (machine ε); PSD-ordering verified |
| W4-7 NULL-ELIM-MAP | S85-W4-7-NULL-ELIM-MAP | 5/5 σ-distance entries; 2/5 detectable at \|Δ\| > 3σ (DESI DR3 w_0 +3.28σ; CMB-HD α_s +5.155σ); 1/5 STRUCTURAL-FLOOR (LiteBIRD n_T) | `bf8135bf3636f2c0...` | Pre-registered for null/detection cascade | Locks branch-closure triggers BEFORE 2026-2030 data |
| W4-8 WATCHLIST-UPDATE | S85-W4-8-WATCHLIST-UPDATE (REFRAMED) | 6/6 rows unified-schema compliant; registry augmented 4363→8697 bytes; pre-SHA `202d867b...` → post-SHA `aa10ad48...` | `4e09971ad312e3a8...` | Project-level registry | Reframe: writes to `sessions/framework/falsifier-watchlist.md`, ZERO agent-memory writes (per AMRI rule) |

**Sub-classification of EVOI level**:
- FLAGSHIP: W0-1, W0-8, W1a-5, W1a-7
- FLAGSHIP-JOINT: W1b-5 (S4×HD); W4-6 (5-channel Fisher inversion)
- FLAGSHIP-SEQUENCED: W1a-4 (BK 2026 → LiteBIRD 2030)
- STRUCTURAL-FLOOR: W1a-8 (LiteBIRD n_T)
- META-CERTIFICATION: W4-4, W4-7, W4-8

---

### II.3 W-2 A_s Band-Authority Workshop Fold-In (load-bearing for observational policy)

**Result**: The W2 A_s band-authority workshop (Round 1-3, transit × mack) registered **BOTH-Pathways** for the r tensor-to-scalar amplitude, a **4-level unit-class taxonomy** for closure thresholds, and a **FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030**. **META** (band-authority policy; underlying r and A_s observables are PHONONIC). The reclassification reshapes the observational policy for r (sequencing BK-Array 2026 ahead of LiteBIRD 2030) and locks A_s reporting into a four-band severity taxonomy.

#### II.3.a BOTH-Pathways r-discriminator

The workshop's BOTH-Pathways pre-registration:
- **Path-H** (Hawking-side substrate dynamics route): r = 0.00745 (Hawking-side derivation of tensor amplitude at fold)
- **Path-C** (canonical S83 G46 TENSOR-TRANSFER): r = 0.0117 (canonical_constants.py `r_CMB_framework` = 0.0117315)
- **Ratio**: r_PathH/r_PathC = 0.6367 (workshop-canonical; my Python verification computes 0.6350 from r_PathC=0.0117315 and r_PathH=0.00745, off by 0.27% due to r_PathC truncation in the workshop quote — non-load-bearing)

**Substitution chain for the r elevation** (mandatory):

```
Step 1 (definition): under ONE pre-registered r value (canonical S83 G46),
  r is a single-pre-registration livewatch falsifier (4-branch tree per W1a-4).
  Under TWO pre-registered r values (Path-H and Path-C) tagged BOTH-PATHWAYS,
  r becomes ALSO an internal-consistency discriminator:
  the framework's two derivation routes either agree (within scheme floor) or split.

Step 2 (substitute):
  Path-H − Path-C = 0.00745 − 0.0117315 = −0.00428 (Path-H is below Path-C by 36.5%)
  Threshold for split-discriminator: r_PathH ≠ r_PathC at scheme floor 12.5% (W1a-1 STRUCTURAL FAIL on f_conv)
  |delta_r/r_PathC| = 36.5% > 12.5% scheme floor

Step 3 (simplify):
  The two pathways are split by 36.5%, well above the 12.5% scheme floor of f_conv-bearing predictions.
  Under LiteBIRD σ(r) = 1.28×10⁻³ (W1a-4 / W4-7 anchor):
    SNR_PathC = 0.0117315 / 1.28e-3 = 9.17σ (Python-verified)
    SNR_PathH = 0.00745   / 1.28e-3 = 5.82σ (Python-verified)
    Workshop-quoted: 4.25σ decisive; 9.31σ at Path-H sigma-anchor; 14.6σ at Path-C
    (Workshop value families differ on which σ_LB anchor is used; my values use σ_LB = 1.28e-3
    from W1b-5 sensitivity-scaling proxy. Both cohort PASS the 3σ decisive threshold.)

Step 4 (direction):
  r elevates from "live-watch falsifier" (single-prediction comparison)
  to "internal-consistency discriminator AND live-watch falsifier" (two-prediction split + comparison).
  Direction: BK-Array 2026 (1.42σ marginal at single-r) → LiteBIRD 2030 (decisive at split-r) is the SEQUENCED discriminator timeline.
```

#### II.3.b 4-level unit-class taxonomy

The workshop registered four observational-comparison unit classes for closure thresholds, anchored on the W1a-1 f_conv STRUCTURAL FAIL (12.5% scheme floor):

| Level | Unit class | Threshold | Question answered |
|:-----|:-----------|:----------|:------------------|
| 1 | LCDM-statistical | Planck σ ≈ 1.4% on A_s | Direct comparison to observed posterior |
| 2 | framework-floor | f_conv scheme floor 12.5% | Internal precision floor (W1a-1 binding) |
| 3 | framework-severity | 30% (geometric mid-band on log-scale between floor and closure) | Strict severity test (W3-7 inflationary anchor) |
| 4 | framework-closure | factor-2 (PASS-F2) | Closure pipeline integrity (S80 PASS-F2) |

**Substitution chain for level-ordering** (Python-verified):

```
Step 1 (definition): level ordering by log10 cutoff width
  level-1 cutoff = log10(1.014) = 0.00604 OOM
  level-2 cutoff = log10(1.125) = 0.05115 OOM
  level-3 cutoff = log10(1.30)  = 0.11394 OOM
  level-4 cutoff = log10(2)     = 0.30103 OOM

Step 2 (substitute): geometric mid-band check (level-3 vs sqrt(level-2 × level-4))
  sqrt(0.05115 × 0.30103) = sqrt(0.01540) = 0.12410 OOM
  level-3 = 0.11394 OOM; ratio 0.11394/0.12410 = 0.918

Step 3 (simplify): level-3 sits within 8% of the geometric mid-band of levels (2,4).

Step 4 (direction): level-3 (30%) is the principled mid-band on log-scale;
  it is NOT arbitrary. The 4-level ordering 1.4% < 12.5% < 30% < factor-2 covers
  the observational/framework-precision axis with each level answering a different question.
```

#### II.3.c FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030

Because BK-Array 2026, DESI DR3 2027, CMB-S4 2028, PIXIE 2029+, and LiteBIRD 2030 form a **4-year external-clock window**, the workshop ratified a FROZEN-PREDICTION-DISCIPLINE-COMMIT: no canonical-band change permitted between 2026 and 2030 except via a structurally-required pre-registration update (e.g., a canonical_constants.py provenance update like W1b-8 α_s ACT DR4 +1σ drift). Band-authority is **structurally ephemeral** during this window — once the data lands, any post-data band re-tightening is convention-shopping (S78 Class 1).

#### II.3.d W3-7 reclassification under the BOTH-Pathways A_s band

The W3-7 FAIL verdict (A_s_TD = 3.299×10⁻⁹, |dev| = 0.5712, +0.1962 OOM) sits **inside PASS-F2** [0, 0.301] AND **outside W3-7 strict 30%** [0, 0.114]. Both verdicts are correct under their respective bands; the reclassification removes the band-authority adjudication burden from the W3-7 single gate and reassigns it to the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 — i.e., the framework's load-bearing burden shifts from "decide the band" to "honor the FROZEN COMMIT 2026-2030 and let the four-year window rule on its own data."

**Convention-translation footnote** (Mack bridge role): in standard cosmology, A_s is reported with Planck statistical precision ≈ 1.4% (`ln(10^10 A_s) = 3.044 ± 0.014`). The framework's prediction-precision is bounded below by the W1a-1 STRUCTURAL FAIL at 12.5% scheme floor; therefore comparison to Planck must use the WIDER of the two precisions, which is the framework's. This is the substrate-emergence-vs-precision-CMB tension that the 4-level taxonomy explicitly addresses.

---

### II.4 Pending Livewatches (event-driven verdicts)

**Result**: Three pre-registered livewatch tracks active at S85 close. **META** (event-driven gates).

| Track | Gate | Window | Inputs | Cascade-on-trigger |
|:------|:-----|:-------|:-------|:-------------------|
| DESI DR3 w_0 | W1a-5 + W1b-1 (regulator-conditional sub-tree) | Window opened 2026-04-23 | (w_0_FW, w_a_FW) = (−0.918, 0); R_842 = [−1.05,−0.85] × [−0.2,0.2]; 7-cell tree; **W1b-1 FAIL forces 3-layer L_max sub-tree** at L_max ∈ {8, 10, 12} because Zubarev w_0 flips A1 ↔ B2 between L=10 (−0.918) and L=12 (−0.635 extrapolation) | LOCKOUTS A-F (S84 W1b-9); kaku R_842-PHYSICAL-ANCHOR-REAUDIT + W0-L-INVERTED-BRANCH-ENUMERATION on FAIL |
| BK-Array 2026 r | W1a-4 | Quarterly poll (next 2026-07-01) | r_FW = 0.0117315 (canonical S83 G46); 4-branch tree; **NEW from W2**: Path-H r=0.00745 alternative pin lifts BK-Array role from single-r livewatch to internal-consistency split-test | LISA re-analysis on upward excursion; c_T/c_S re-audit on downward excursion |
| CF-M6 α_s × w_0 joint | W1b-10 | Post-DR3 + joint MCMC | BF_indep(narrow×narrow) = 10.75 (BF_α_narrow=1.682 × BF_w_FW-right=6.38); D := \|log10(BF_joint) − log10(BF_indep)\| pending DR3 data | PASS at D < 0.30 dex; FAIL at D > 0.60 dex |

**Substitution chain for the W1b-1 FAIL meaning** (the most consequential carry-forward):

```
Step 1 (definition): R_842 7-cell tree placement at L_max=L is determined by Zubarev w_0(L).
Step 2 (substitute):
  L=5  : w_0 = −0.918 → cell A1 (1σ box around (−0.842, 0))
  L=10 : w_0 = −0.918 → cell A1 (matches canonical w0_FW)
  L=12 : w_0 = −0.635 (W0-7 ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE extrapolation FAIL value) → cell B2 (quintessence)
Step 3 (simplify): unique cells = {A1, B2}; flip A1 → B2 between L=10 and L=12 violates plan §W1b-1 threshold "FAIL iff at least one cell flips IN→OUT when L_max changes by 2."
Step 4 (direction): a single 7-cell tree is INSUFFICIENT for 2026-04-23 firing.
  S86 must maintain 3 sub-trees keyed on L_max ∈ {8, 10, 12}, and DR3 adjudication becomes regulator-AND-L_max-conditional.
```

---

### II.5 Cross-Channel Correlation Matrix (W4-2 canonical registry)

**Result**: 5×5 canonical detector-pair correlation matrix at `sessions/framework/cross-channel-correlation-matrix.md` (8133 bytes, frontmatter `type: registry`, `ingested-by: /weave --update`). **NON-PHONONIC** (pipeline-level metadata; the diagonal substrate-moment assignments are PHONONIC).

#### II.5.a Diagonal substrate-moment table

Each diagonal entry names which spectral moment of D_K on the Jensen-deformed SU(3) fiber the channel probes:

| Channel | Substrate moment |
|:--------|:-----------------|
| CMB-S4 α_s | d²S_transfer/dk² at k_pivot (scalar 2-pt 2nd derivative) |
| DESI DR3 w_0 | a_0 Volovik partition (zeroth spectral moment; impedance leakage Γ=0.99970) |
| LiteBIRD n_T | tensor-sector Dirac spectrum (B-mode); r=16ε INAPPLICABLE per `phononic-framing.md` |
| CMB-HD α_s | d²S_transfer/dk² at k_pivot (SAME moment as CMB-S4 → COMMON_MODE pair (0,3)) |
| 21-cm folded bispec | 3-pt spectral moment (folded NG = 0.0547 from S82 W3-4 GGE-FNL) |

#### II.5.b Off-diagonal classifications (10 pairs of C(5,2))

| Pair | Channels | Tag | Source |
|:----:|:---------|:---:|:------:|
| (0,1) | CMB-S4 α_s / DESI DR3 w_0 | PARTIALLY_CORRELATED (ρ=0.35; W4-3) | FISHER |
| (0,2) | CMB-S4 α_s / LiteBIRD n_T | INDEPENDENT | FISHER |
| (0,3) | CMB-S4 α_s / CMB-HD α_s | COMMON_MODE (ρ=0.7; W4-6) | FISHER |
| (0,4) | CMB-S4 α_s / 21-cm folded | INDEPENDENT | FIRST-PRINCIPLES-REASONING |
| (1,2) | DESI DR3 w_0 / LiteBIRD n_T | INDEPENDENT | FIRST-PRINCIPLES-REASONING |
| (1,3) | DESI DR3 w_0 / CMB-HD α_s | PARTIALLY_CORRELATED | FISHER |
| (1,4) | DESI DR3 w_0 / 21-cm folded | INDEPENDENT | FIRST-PRINCIPLES-REASONING |
| (2,3) | LiteBIRD n_T / CMB-HD α_s | INDEPENDENT | FISHER |
| (2,4) | LiteBIRD n_T / 21-cm folded | INDEPENDENT | FIRST-PRINCIPLES-REASONING |
| (3,4) | CMB-HD α_s / 21-cm folded | INDEPENDENT | FIRST-PRINCIPLES-REASONING |

**Pair sharing systematic**: (0,1), (0,3), (1,3) — all share the CMB acoustic ladder (r_d) at some level. (0,3) is COMMON_MODE because both CMB-S4 and CMB-HD probe the *same* α_s second-derivative moment.

**Conditionally-independent pairs**: (0,2), (0,4), (1,2), (1,4), (2,3), (2,4), (3,4) — the 7 pairs with INDEPENDENT tag. These give multiplicative joint evidence under the W4-1 BF discount formula `BF_joint = ∏_i BF_i^{f_i}` with `f_i = 1 − mean_{j≠i} ρ_ij`.

---

### II.6 Combined Observational Constraint Map (S86+ falsifier dispatch tree)

**Result**: Five observational triggers pre-registered for 2026-2030, each binding a substrate-prediction to a binary or n-cell classifier. **META** (constraint-map artifact).

#### II.6.a DR3 fires 2026-04-23 → activates W1a-5 7-cell tree branch + W1b-1 L_max sub-tree

- IF DR3 lands in cell A1 (within 1σ of (−0.918, 0)) AND L_max=10 sub-tree selects R2 Zubarev: PASS, compaction-timescape ratified, LISA W6-50 becomes next-stage falsifier.
- IF DR3 lands in cell A2 (1-2σ): INFO, regulator-class ambiguity carry-forward.
- IF DR3 lands in B1/B2/B3 (phantom / quintessence / |w_a|>0.2): FAIL; kaku cascade `R_842-PHYSICAL-ANCHOR-REAUDIT` + `W0-L-INVERTED-BRANCH-ENUMERATION`.
- IF DR3 lands in C1/C2 (exotic): FAIL + full re-audit.
- **W1b-1 modifier**: at L_max=12 the framework Zubarev w_0 extrapolates to −0.635 (cell B2), so the 7-cell tree must be evaluated at THREE L_max ∈ {8, 10, 12} sub-trees and the DR3 adjudication becomes regulator-AND-L_max-conditional.

#### II.6.b CMB-S4 2028 → triggers W0-1 60.5σ flagship posterior update

Substitution chain (verified W1b-5 joint S4×HD):

```
Step 1 (definition): pull = |β_s_FW − β_s_LCDM_null|/σ_S4
Step 2 (substitute): pull_S4 = 0.1331/2.2e-3 = 60.5σ (Python-verified)
                     joint S4×HD: σ_joint = 1/√(1/σ_S4² + 1/σ_HD²) where σ_HD = 1.571×10⁻³ (proxy; W1b-6 PRE-REG-INCOMPLETE)
                     σ_joint = 1.279×10⁻³ ⇒ pull_joint = 0.1331/1.279e-3 = 104σ (Python-verified)
Step 3 (simplify): tightening ratio σ_joint/σ_S4 = 1.279/2.2 = 0.581 (41.9% tightening)
Step 4 (direction): β_s either lands at −0.1331 (PASS, framework ratified) OR at >100σ from joint (FAIL).
                    No middle ground; decisive in either direction by 2034 (S4 + HD).
```

#### II.6.c BK-Array 2026 → triggers W1a-4 4-branch tree (NOW: Path-H vs Path-C r-discriminator)

Pre-W2 reading: 4-branch livewatch on r_FW = 0.011732. Post-W2 reading: 4-branch livewatch PLUS internal-consistency split-test against Path-H r=0.00745. The marginal 1.42σ at BK-Array (Path-H σ-budget) sequences the decisive verdict to LiteBIRD 2030.

#### II.6.d PIXIE 2029+ → W0-8 8693σ falsifier closes or framework rebuilds

Substitution chain:

```
Step 1 (definition): pull = |μ_FW − μ_LCDM|/σ_PIXIE
Step 2 (substitute): μ_FW = 8.69×10⁻⁵ (W5-57 K-endpoint γ=1 lockout)
                     μ_LCDM = 2×10⁻⁸; σ_PIXIE = 10⁻⁸
                     pull = 8.69×10⁻⁵/10⁻⁸ = 8693
Step 3 (simplify): pull = 8693 ≫ 100 PASS threshold (Python-verified)
Step 4 (direction): factor ~145× above the β_s pull (W0-1) and ~4 OOM separation.
                    PIXIE non-detection at this level falsifies framework; detection ratifies the GGE-relic K-endpoint thermodynamic prediction.
```

#### II.6.e LiteBIRD 2030 → 4.25σ decisive r-discriminator (Path-H 9.31σ; Path-C 14.6σ)

Workshop pre-registered SNR projections at LiteBIRD σ(r). My Python check at σ_LB=1.28×10⁻³ gives Path-H 5.82σ and Path-C 9.17σ; the workshop-quoted higher values use a tighter σ_LB anchor (Hazumi-2019 strawman σ_LB ~ 8×10⁻⁴ or the W1a-9 σ=1×10⁻³ anchor). Both anchors deliver decisive discrimination; LiteBIRD 2030 IS the resolution point of the BK-Array sequenced timeline.

---

## III. Gate Verdicts

Verdicts are AUTHORITATIVE per the source working papers; the table below lifts only the observational-track gates relevant to S-7 mack scope (W0 observational subset, W1a 1-10, W1b 1-10, W3-1 PIXIE, W4 1-8 livewatches and registry landings). PASS / FAIL / INFO / PRE-REG-INCOMPLETE / PENDING-EVENT distribution per `.claude/rules/math-scripts.md` "All Results Are Good Results" — no FAIL is treated as defeat.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W0-1 BETA-S-CMB-S4-PREREG | PASS | 60.5σ pull |
| W0-8 PIXIE-MU-K-ENDPOINT-PREREG | PASS | 8693σ pull |
| W1a-1 SCHEME-DEP | FAIL | 12.5% f_conv 2-loop floor (STRUCTURAL) |
| W1a-2 ALPHA-S-REGISTRY-UPGRADE | FAIL | 0.7876 partition residual; 197σ pull (topological-only single-scheme) |
| W1a-3 ALT-D-SPEC-PROBE | FAIL (truncation) | max residual 1.19 (route iii topological exact at 12) |
| W1a-4 BK-ARRAY-2026-LIVEWATCH | PENDING-EVENT | r_FW = 0.011732; 4-branch frozen S84 W4-42 |
| W1a-5 DR3-LIVEWATCH | PENDING-EVENT | (w_0_FW, w_a_FW) = (−0.918, 0); window opened 2026-04-23 |
| W1a-6 LISA-CGWB-FLAGSHIP-FIX-K | PASS | residual 3.33×10⁻⁴ < 1×10⁻³ |
| W1a-7 LISA-FLAGSHIP-FIX-TIGHTENING | PASS | SNR = 1.68×10¹³ |
| W1a-8 LITEBIRD-NT-REGISTRY-LANDING | PASS (STRUCTURAL-FLOOR) | separation_normalized = 588.78 |
| W1a-9 MULTID-FISHER-FRAMEWORK | PASS | log10(BF_FW/LCDM) = +827.93 |
| W1a-10 FALSIFIER-MONITOR-RANK-UNIVERSALITY | INFO | 4/4 PENDING; tesla W13 carry-forward |
| W1b-1 CF-M2-REGULATOR-CONDITIONAL-DR3-TREE | FAIL | A1 ↔ B2 cell-flip between L_max=10 and L_max=12 |
| W1b-2 ALPHA-S-JOINT-FISHER-CORRELATED | PASS | σ_corr/σ_diag = 1.130 |
| W1b-3 ALPHA-S-PRIOR-RANGE-LCDM | FAIL | min(BF) = 0.99 (Planck-Gauss prior); prior-sensitive |
| W1b-4 ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS | PASS | \|Δα\|=7.15×10⁻⁴ = 0.107σ_Planck (S62/S67 reconciled) |
| W1b-5 BETA-S-JOINT-S4-HD | PASS | σ_joint = 1.279×10⁻³; tightening ratio 0.581; pull 104σ |
| W1b-6 CMB-HD-ALPHA-S-MACINNIS-EXPLICIT | PRE-REG-INCOMPLETE | MacInnis 2022 has no σ(α_s) forecast |
| W1b-7 LITEBIRD-ALPHA-S-HAZUMI-VERIFIED | PRE-REG-INCOMPLETE | Hazumi 2022 has 0 hits for `alpha_s`/`running` across 156 pages |
| W1b-8 PLANCK-DESI-2025-ALPHA-S-RECALIBRATION | FAIL (real-data) | \|Δα\|/σ_2018 = 1.015 (ACT DR4+Planck Aiola 2020 supersedes) |
| W1b-9 GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM | FAIL | min(13322, 1.0) = 1.0 vs canonical 13322 (4 OOM); true statement is "two-valued at L1/L2 layer interface" |
| W1b-10 CF-M6-ALPHA-S-W-A-DECOUPLED-JOINT | PENDING-EVENT | BF_indep = 10.75 (narrow × narrow); BF_joint pending DR3 |
| W3-1 CF-5-PIXIE-KMFIRAS-PREREG | PASS | 5-regulator spread = 0.000 exact at γ=1 lockout |
| W4-1 CMB-S4-INDEP-AUG | INFO | 5/10 Fisher-cited, 5/10 WARRANT-DEFERRED (coverage_strict = 0.500) |
| W4-2 XCORR-MATRIX | PASS | 25/25 cells filled; 10 FISHER + 10 FP off-diag (pair-symmetric); 5 diag substrate-moments |
| W4-3 DESI-DR3-INDEP | INFO | f_indep = 0.873; PRE-REG-INCOMPLETE (Fisher PDF absent) |
| W4-4 FALSIFIER-WATCH-CERT | PASS | 5/5 channels certified |
| W4-5 KSTAR-3HEB-LAB-INDEP | INFO | 5/5 named; 2/5 ANALOG-CANDIDATE-UNVERIFIED |
| W4-6 MULTI-D-JFD | INFO | geometric-mean discount = 0.9926; identity residual 0; 0/5 Fisher PDFs ⇒ PRE-REG-INCOMPLETE |
| W4-7 NULL-ELIM-MAP | PASS | 5/5 σ-distance entries; 2/5 detectable |
| W4-8 WATCHLIST-UPDATE (REFRAMED) | PASS | 6/6 unified-schema rows; registry 4363 → 8697 bytes |

**Verdict distribution (observational subset only, N=29)**: PASS=16, FAIL=7 (W1a-1/2/3, W1b-1/3/8/9), INFO=4 (W1a-10, W4-1/3/5/6), PRE-REG-INCOMPLETE=2 (W1b-6/7), PENDING-EVENT=3 (W1a-4/5, W1b-10), with one gate W4-6 carrying both INFO and PRE-REG-INCOMPLETE tags. No master-gate tally is intended (per `feedback_no-master-gate-tally.md`); the distribution is reported only because the prompt requested it.

---

## IV. Structural Implications

### IV.1 Observational policy shifts after W-2 fold-in

1. **r elevated from single-pre-registration livewatch to BOTH-Pathways internal-consistency discriminator**. BK-Array 2026 (1.42σ marginal) is now the upstream split-test detector; LiteBIRD 2030 is the decisive resolution point. The two-path registration closes the convention-shopping risk that a single canonical r value would land at — under BOTH-Pathways discipline, an external observer sees the framework predicting TWO values for r, with their split (36.5%) above the W1a-1 12.5% scheme floor. This is structurally honest about the f_conv-bearing precision floor.

2. **Band-authority decision postponed to FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030**. The W3-7 "decide the band" question is reframed: the framework's load-bearing burden is no longer to ratify factor-2 vs 30%, but to honor the 4-year external-clock window without canonical-band changes. Any post-data band re-tightening between 2026 and 2030 is convention-shopping (S78 Class 1 execution failure).

3. **Observational scope transparently bounded by framework precision floor**. The 4-level taxonomy makes explicit that LCDM-statistical comparison (1.4%) is BELOW the framework's own scheme floor (12.5%). For f_conv-bearing observables (A_s, n_s, α_s, β_s), the comparison band must be the WIDER of the framework precision floor or the observational precision; framework precision is binding for A_s, observational precision is binding for β_s (where σ_S4=2.2×10⁻³ ≪ |β_s|=0.1331).

4. **DR3 firing today is regulator-AND-L_max-conditional** (W1b-1 FAIL). The S86 W0 plan must produce three L_max ∈ {8, 10, 12} sub-trees and a 21-cell adjudication matrix. The observational scope of DR3 expands from "binary R_842 containment" to "binary R_842 containment per L_max sub-tree", with the adjudication selecting the live regulator before reading the cell.

5. **LiteBIRD n_T is permanently STRUCTURAL-FLOOR** (W1a-8). EVOI for LiteBIRD on n_T is 0 through 2040 by construction — the 54-decade k-space transfer geometry of S66 forbids LiteBIRD from probing the transit-scale blue tilt n_T = +0.468; LiteBIRD probes only the CMB-scale n_T = −3.024×10⁻³ (S66 TENSOR-TRANSFER 14.3× suppression, modified consistency relation `n_T = −r·c_T/(8·c_S)` exact, S84 W4-39 PASS). The flagship tensor channel is LISA CGWB (W1a-7), not a CMB B-mode mission.

6. **Common-mode discount on α_s is the only non-trivial Fisher correction** (W4-6). The 5-channel Fisher matrix is otherwise diagonal at the parameter level; only the CMB-S4 × CMB-HD pair (probing the SAME d²S/dk² spectral moment) carries a ρ=0.7 common-mode discount, deflating α_s joint-information from 1.05×10⁶ (independent sum) to 8.77×10⁵ (correlated; 16.7% reduction). All other channels probe orthogonal substrate moments.

7. **Framework-internal precision floor is project-canonical for f_conv-bearing predictions** (W1a-1 STRUCTURAL FAIL). Every prediction consuming f_conv (A_s, n_s, α_s, β_s, m_H via running) must be reported as `(value, scheme=heat_kernel, convention=A, path=...)` tuples, NOT scalars. The 12.5% scheme variance is structural; future synthesis dispatches that compute joint BFs must use the f_conv-tuple precision as the binding floor.

### IV.2 Constraint-map updates (2026-04-23 to 2026-04-25)

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-04-23 | r = 0.0117 single livewatch | "single-prediction live-watch falsifier" | "BOTH-Pathways internal-consistency discriminator AND live-watch falsifier" | W2 workshop registration; Path-H/Path-C split 36.5% above scheme floor |
| 2026-04-23 | A_s band authority | "S80 PASS-F2 (factor-2) frozen since S80 W1-2; W3-7 30% band per-gate-only" | "4-level unit-class taxonomy + FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030" | W2 workshop convergence (transit × mack R1-3) |
| 2026-04-23 | DR3 7-cell tree | "single 7-cell tree, regulator-agnostic" | "3 L_max sub-trees keyed on {8,10,12}, regulator-AND-L_max-conditional" | W1b-1 FAIL on A1 ↔ B2 cell-flip |
| 2026-04-23 | LISA CGWB-PT | "consistent channel (S84 W6-50 PASS)" | "flagship discriminator at SNR=1.68×10¹³, decisiveness robust to 3σ tightening" | W1a-7 PASS |
| 2026-04-23 | LiteBIRD n_T | "INFO (540-654× below 1σ; S84 W4-41)" | "STRUCTURAL-FLOOR (54-decade geometric); EVOI=0 through 2040" | W1a-8 separation_normalized=588.78 |
| 2026-04-23 | 7D multi-channel Fisher | "single-channel S84 chi²s" | "assembled; subset reproduces S84 chi² within 7%; conditional log10(BF)=+828" | W1a-9 PASS |
| 2026-04-23 | `alpha_s_canon` constant | "−0.0045 ± 0.0067 (Planck 2018)" | "RECOMMENDED UPDATE: +0.0023 ± 0.0063 (ACT DR4+Planck, Aiola 2020 Table 5 col 3)" | W1b-8 FAIL with \|Δα\|/σ_2018 = 1.015 |
| 2026-04-23 | r_max layer-interface | "GENUINE-UNPINNED min-identity candidate" | "min-identity FALSIFIED; two-valuedness is the true statement" | W1b-9 FAIL of plan candidate |
| 2026-04-23 | Cross-channel correlation | "memory-driven re-derivation each session" | "canonical 5×5 registry at `sessions/framework/cross-channel-correlation-matrix.md` (8133 bytes)" | W4-2 PASS; AMRI input-pin test fires |
| 2026-04-23 | Falsifier watchlist | "agent-memory + path-misaligned" | "AMRI-migrated to `sessions/framework/falsifier-watchlist.md`; 8 columns; 6/6 unified-schema (4363 → 8697 bytes)" | W4-8 REFRAMED PASS; ZERO agent-memory writes |
| 2026-04-25 | A_s severity adjudication burden | "W3-7 single-gate decision" | "4-level taxonomy under FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030" | W2 workshop closure |

---

## V. Carry-Forward Computations

**MANDATORY** per `feedback_fix-in-session-never-defer.md`. Each entry has all four fields (What, Inputs, Gate, Effort).

### V.1. Promote r to falsifier-master-inventory under BOTH-Pathways

- **What**: Add a new entry in `sessions/framework/falsifier-watchlist.md` for `r_BOTH_PATHWAYS` carrying both `r_PathC = 0.0117315` (canonical S83 G46) and `r_PathH = 0.00745` (Hawking-side derivation), with the split = 36.5% > 12.5% scheme floor flag and the SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030. Schema: 9-column extension of W4-8's 8-column unified schema with an additional `pathways: {PathH, PathC}` field.
- **Inputs**: `r_CMB_framework` from canonical_constants.py (= 0.0117315, S83 G46 TENSOR-TRANSFER); Path-H derivation script (Hawking-workshop output, to be located or reproduced); workshop pre-registration content_sha for SHA-pin closure.
- **Gate**: `S86-W?-R-BOTH-PATHWAYS-WATCHLIST-LANDING`. PASS iff schema row lands with Path-H + Path-C values pinned and the 4-branch BK-Array livewatch tree references both. FAIL iff Path-H derivation cannot be reproduced from a forward substrate-dynamics computation (i.e., Path-H value is a backward inference only).
- **Effort**: 1.5 hours (registry edit + Path-H derivation reproduction + dual-SHA closure on workshop content).

### V.2. Register FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 in `baseline-findings-s66.md`

- **What**: Add a §FROZEN-COMMIT 2026-2030 section in `sessions/framework/baseline-findings-s66.md` (or its successor canonical band-authority file) documenting (a) the 4-level unit-class taxonomy, (b) the BOTH-Pathways r registration, (c) the 4-year external-clock window with canonical_constants.py-update-only exception clause, (d) the W3-7 reclassification under FROZEN-COMMIT.
- **Inputs**: W2 workshop document SHA pin; W1a-1 STRUCTURAL FAIL provenance; W1b-1 layer-conditional DR3 tree; current canonical_constants.py SHA at S85 close.
- **Gate**: `S86-W?-FROZEN-COMMIT-LANDING`. PASS iff section lands with all 4 sub-clauses, scheme floor 12.5% pinned as project-level minimum band on f_conv-bearing predictions, and the W3-7 reclassification documented as severity-flag-within-level-3-NOT-band-redefinition.
- **Effort**: 1 hour (file edit + cross-reference linking).

### V.3. Per-detector S86+ readiness checklist

- **What**: For each of the 9 detectors in the P_obs_aligned table (PIXIE, DESI DR3, CMB-S4, LISA, LiteBIRD, BK-Array, CMB-HD, SKA-1, lab-analogs ³He-B + K-STAR), produce a one-page readiness snapshot covering (i) data-release window, (ii) canonical framework prediction with scheme tuple, (iii) canonical detector σ with Fisher-PDF SHA pin or WARRANT-DEFERRED, (iv) cascade-on-trigger script names, (v) carry-forward computations triggered by detection vs null. Output as a single registry section in `sessions/framework/falsifier-watchlist.md` (extending the W4-8 update).
- **Inputs**: W1a-4 / W1a-5 / W1a-6 / W1a-7 / W1a-8 livewatch JSON files; W1b-1 layer-conditional sub-tree spec; W4-4 5-channel cert NPZ; W4-7 null-elim-map NPZ; canonical_constants.py.
- **Gate**: `S86-W?-DETECTOR-READINESS-9-CELL`. PASS iff 9/9 detectors carry all 5 fields, no silent rows, with detection-script paths verified to exist on disk (per `agent-standards.md` completion-verification rule). INFO if any field is WARRANT-DEFERRED with named missing source.
- **Effort**: 4 hours (data ingestion + cross-checking from session-85 wave NPZ files).

### V.4. Land BK-Array 2026 4-branch tree NOW (anticipating release)

- **What**: Pre-build the 4-branch decision script `computations/s86_bk_array_2026_classifier.py` triggered on BK-Array data publication, emitting verdict line under canonical 4-tuple `(value=branch, scheme=BICEP-Keck-2026, convention=BK-publication-r-form, L_max=N/A)` with dual-SHA closure over BK-published-data + canonical r_FW. Pre-build the ALSO Path-H comparison script using the BOTH-Pathways framing.
- **Inputs**: W1a-4 BK-Array livewatch JSON; canonical r_FW = 0.0117315; Path-H r = 0.00745; expected BK-Array 2026 release-format spec.
- **Gate**: `S86-W?-BK-ARRAY-CLASSIFIER-PRE-BUILD`. PASS iff scripts on disk, dry-run verified with synthetic test r ∈ {0.003, 0.012, 0.025, 0.040} producing branches {1, 2, 3, 4}. FAIL iff dry-run fails to map test inputs to expected branches.
- **Effort**: 4 hours (script build + dry-run + dual-SHA).

### V.5. Fetch and SHA-pin Fisher-forecast PDFs for W4-3, W4-6 PRE-REG-INCOMPLETE clearance

- **What**: Fetch the 5 Fisher-forecast PDFs cited in W4 (CMB-S4 Science Book v2, DESI 2025 BAO forecast, LiteBIRD forecast, CMB-HD Sehgal 2019 whitepaper, HERA Memo 54), store under `researchers/<DETECTOR>/`, SHA-pin each, and re-emit W4-3 + W4-6 verdicts under the now-pinnable Fisher-PDF map.
- **Inputs**: arXiv IDs (CMB-S4 Science Book v2 2022, DESI Collab 2024 III/VI, Hazumi 2022 LiteBIRD, Sehgal 2019 CMB-HD, HERA Memo 54 Ali+ 2018). Use mcp__paper-search__download_arxiv where applicable.
- **Gate**: `S86-W?-FISHER-PDF-PIN-CLOSURE`. PASS iff 5/5 PDFs on disk with SHA pinned and W4-3/W4-6 re-emitted. INFO if any PDF cannot be retrieved (carry-forward to S87+).
- **Effort**: 2 hours (fetch + SHA + re-emit).

### V.6. Build S86 W0 layer-conditional DR3 sub-trees (W1b-1 FAIL remediation)

- **What**: Generate 3 sub-trees keyed on L_max ∈ {8, 10, 12} for the W1a-5 7-cell DR3 tree. At L_max=8 the framework Zubarev w_0 is currently DATA-UNAVAILABLE per W1b-1; this carry-forward fills that gap by computing Zubarev w_0 from the L_max=8 D_K spectrum cache and placing the cell. Output: 21-cell matrix (3 L_max × 7 cells) replacing the single 7-cell tree.
- **Inputs**: D_K spectrum cache at L_max=8 (s84_spectrum_cache_L8_tau019.npz or successor); Zubarev kernel definition (Zubarev-1974 + CM-1995 ext.); 7-cell partition spec from W0-DR3-REGULATOR-SUCCESSOR-TREE JSON.
- **Gate**: `S86-W?-DR3-3-LAYER-SUB-TREE`. PASS iff all 21 cells have deterministic labels, NO TBD entries, AND the framework cell-membership at L_max ∈ {8,10,12} is monotone (no oscillation A → B → A across consecutive L). FAIL iff the cell-flip pattern is non-monotone (would indicate the L_max convergence is even more pathological than W1b-1 detected).
- **Effort**: 6 hours (Zubarev computation at L_max=8 + cell placement + 21-cell matrix emission).

### V.7. Resolve H̃ divergence chase to retire A_s band-authority ambiguity

- **What**: Promote the S80 H-TILDE-DIVERGENCE-CHASE from conditional to permanent. Pre-registered PASS criterion: H̃ at CMB pivot is the value derivable from forward BASELINE substrate dynamics independent of A_s. Three branches: TD (5.908×10⁻³, current canonical), LI (2.464×10⁻⁵, S80 cache LI verdict), BASELINE (4.714×10⁻³, S84 W1a-1 PASS-window centre).
- **Inputs**: S84 W1a-1 BASELINE-HTILDE-SENSITIVITY PASS-window NPZ; S80 W1-1 TD verdict NPZ; S80 W1-1 LI verdict NPZ; substrate-dynamics forward-derivation script (to be built as part of this gate).
- **Gate**: `S86-W?-H-TILDE-DIVERGENCE-PROMOTION`. PASS iff a structurally-derived H̃ at N_pivot=55 lands within ±5% of one of {TD, LI, BASELINE} from a forward substrate-dynamics integration NOT using the S80 TD verdict as input. Verdict chooses the canonical branch. INFO if no branch closes within ±5% (would push the resolution to S87+).
- **Effort**: 12 hours (substrate-dynamics derivation + verification + verdict).

### V.8. SKA-1 forecasts → lab-analog cross-validation for W4-5 INFO promotion

- **What**: Verify the 2 ANALOG-CANDIDATE-UNVERIFIED rows in W4-5 (LiteBIRD n_T ↔ ³He-B tensor-mode spectroscopy; 21-cm folded bispectrum ↔ K-STAR 3-pt correlations) by locating published lab-experiment specifications for tensor-mode spectroscopy and turbulence 3-pt analyses, mapping the lab parameters to substrate moments per the W4-5 §c row-by-row justification template.
- **Inputs**: ³He-B Zeeman + rotational coupling literature (Volovik 1992 Helium-3 textbook + recent torsion-oscillator papers); K-STAR turbulence 3-pt papers (Park et al.); Volovik agent memory `framework-3heb-comparison.md`; canonical_constants.py.
- **Gate**: `S86-W?-LAB-ANALOG-VERIFICATION-2OF5`. PASS iff both rows promoted from UNVERIFIED to FISHER or FIRST-PRINCIPLES-REASONING tag, lifting W4-5 to PASS at 5/5. INFO if 1 of 2 verified, 1 still UNVERIFIED (lifts W4-5 to PASS at 4/5 + 1 UNVERIFIED).
- **Effort**: 4 hours (literature search + parameter mapping + verdict re-emit).

### V.9. CMB-HD α_s explicit forecast tracking (W1b-6 PRE-REG-INCOMPLETE)

- **What**: Monitor publication of an explicit CMB-HD σ(α_s) forecast (candidate sources: Abazajian et al. CMB-HD companion papers; CMB-HD SciBook forecast code release; CMB-S4/CMB-HD joint forecast paper). On publication, fetch, SHA-pin, and re-fire W1b-6 with verified σ value and ratio test.
- **Inputs**: arXiv search query for CMB-HD α_s forecast post-2024; W1b-6 PRE-REG-INCOMPLETE script for re-fire.
- **Gate**: `S86+-W?-CMB-HD-ALPHA-S-FORECAST-PIN`. Re-fires W1b-6 to PASS or FAIL based on verified σ; INFO if no source landed.
- **Effort**: 0.5 hours per quarterly poll (when available).

### V.10. Update P_obs_aligned table after each detector window event

- **What**: After each detector window fires (DR3 2027, BK-Array 2026, CMB-S4 2028, PIXIE 2029, LiteBIRD 2030, LISA 2035), update the P_obs_aligned ranking table to remove fired channels and re-prioritize the remaining set. Output: revised priority table per session.
- **Inputs**: This synthesis's P_obs_aligned table; per-detector verdict cascade output; canonical_constants.py at session-of-update.
- **Gate**: `S87+ recurring-W?-P_OBS_ALIGNED-UPDATE`. PASS iff table re-emitted with at least one channel removed (post-event) AND the updated priority ordering reflects post-data |ΔP_FW| values (not pre-data illustrative values).
- **Effort**: 1 hour per session-of-update (recurring; structural data structure already in place from this synthesis).

### V.11. Tighten α_s canonical pin (W1b-8 FAIL → canonical_constants.py update)

- **What**: Execute the canonical_constants.py update from `alpha_s_canon = −0.0045 ± 0.0067` (Planck 2018 VI) to `alpha_s_canon_2020 = +0.0023 ± 0.0063` (ACT DR4 + Planck, Aiola 2020 Table 5 col 3) per `mcp__knowledge__update_constant` protocol with provenance "ACT DR4 + Planck, Aiola 2020 Table 5 col 3, post-2018 best". Re-run W1a-9 MULTID-FISHER and W1b-3 α_s prior-range BF with the new pin. Re-emit α_s certification rows in `falsifier-watchlist.md` with the updated central + σ.
- **Inputs**: W1b-8 NPZ; ACT DR4 paper SHA pin (downloads/2007.07288.pdf); canonical_constants.py current SHA at S85 close.
- **Gate**: `S86-W?-ALPHA-S-CANONICAL-UPDATE`. PASS iff (a) `mcp__knowledge__update_constant` returns success; (b) canonical_constants.py grows with provenance comment; (c) W1a-9 + W1b-3 re-emit verdicts under updated constant. INFO if downstream verdict changes ≤ 0.1σ (no propagation effect); FAIL if a downstream gate changes its verdict label (would indicate the α_s pin update is observationally consequential and triggers further carry-forward).
- **Effort**: 1.5 hours.

---

## VI. Summary Table

One row per observational channel, with P(decisive_by_year) × |ΔP_framework| as the priority metric. CLASSIFICATION column tags each as PHONONIC / GEOMETRIC / PARTICLE / NON-PHONONIC per `phononic-framing.md`.

| # | Channel | Detector / year | Framework prediction | LCDM null | σ_detector | σ-distance | P(decisive) × \|ΔP_FW\| | Status | Classification | Implication |
|:--|:--------|:----------------|:---------------------|:----------|:-----------|:-----------|:------------------------|:-------|:---------------|:------------|
| 1 | μ-distortion K-endpoint | PIXIE / 2029+ | μ_FW = 8.69×10⁻⁵ | μ_LCDM = 2×10⁻⁸ | 1×10⁻⁸ | +8693σ | LARGE × 1.0 | PASS pre-reg (W0-8) | PHONONIC (a_2 GGE thermodynamic K-endpoint, γ=1 lockout exact) | 4-OOM separation; PIXIE non-detection falsifies, detection ratifies |
| 2 | DESI DR3 w_0 | DESI DR3 / window opened 2026-04-23 | w_0_FW = −0.918 | w_0_LCDM = −1.000 | 2.5×10⁻² | +3.28σ | LARGE × 1.0 | PENDING-EVENT (W1a-5, W1b-1 layer-conditional) | PHONONIC (a_0 Volovik partition; impedance Γ=0.99970) | Binary R_842 lockout; LOCKOUTS A-F fire on FAIL; cell-flip A1↔B2 across L_max ∈ {10,12} requires 3 sub-trees |
| 3 | β_s running-of-running | CMB-S4 / 2028 | β_s_FW = −0.1331 | β_s_LCDM = 0 | 2.2×10⁻³ (S4); 1.279×10⁻³ (joint S4×HD) | +60.5σ (S4); +104σ (joint) | LARGE × 1.0 | PASS pre-reg (W0-1, W1b-5) | PHONONIC (2nd Mellin curvature at τ_fold via a_4) | Doubly decisive; framework's largest single-channel CMB pull |
| 4 | LISA CGWB amplitude | LISA / 2035+ | h_c^(A) = 11 OOM above LISA noise | h_c^LCDM = 0 (LCDM tensor below LISA) | LISA SRD-v3 | SNR = 1.68×10¹³ | LARGE × 1.0 | PASS pre-reg (W1a-6, W1a-7) | PHONONIC (tensor sector spectral action at fold; CGWB-PT) | 11-OOM margin; 3σ tightening leaves SNR = 10¹² |
| 5 | r tensor-to-scalar (BOTH-Pathways) | LiteBIRD / 2030 (decisive); BK-Array / 2026 (sequenced) | r_PathC = 0.01173; r_PathH = 0.00745; split = 36.5% > 12.5% scheme floor | r_LCDM single-field = 16ε (INAPPLICABLE) | 1×10⁻³ (LiteBIRD); higher at BK | LiteBIRD: PathC ≥ 9σ, PathH ≥ 5σ at σ=1.28×10⁻³ | LARGE × 1.0 (LiteBIRD); MEDIUM × 0.6 (BK-Array marginal 1.42σ) | PENDING-EVENT (W1a-4); BOTH-Pathways pre-reg (W2 workshop) | PHONONIC (tensor-sector Dirac spectrum, B-mode polarization) | Sequenced upstream-downstream test: BK-Array marginal → LiteBIRD decisive; W2 BOTH-Pathways elevates r to internal-consistency split-test |
| 6 | CMB-HD α_s | CMB-HD / 2035; CMB-S4 / 2028 | α_s_FW = +0.00117 | α_s_LCDM = 0 (or Planck 2018 −0.0045; W1b-8 update +0.0023) | 1.5×10⁻³ (HD); 2.1×10⁻³ (S4); joint corr σ = 1.068×10⁻³ | +5.155σ (HD per W4-7); +2.70σ (S4); common-mode discount 0.9709 (W4-6) | MEDIUM × 1.0 (HD) / × 0.7 (HD) / × 1.0 (S4) | SECONDARY-JOINT; W1b-6 PRE-REG-INCOMPLETE (MacInnis) | PHONONIC (d²S_transfer/dk² at k_pivot scalar 2-pt) | Common-mode pair (0,3); W1b-6 forecast tracking until publication |
| 7 | f_NL folded bispectrum | SKA-1 / 2030 (undetectable); next-gen 21-cm post-2035 | f_NL_folded_FW = +0.0547 | f_NL_LCDM = 0 (Planck 2.5±5.7) | 5.0 (SKA-1) | +0.011σ | SMALL × 0.05 | INFO observable (folded shape; W0-2 FAIL on SKA-2 detectability) | PHONONIC (3-pt spectral moment at GGE acoustic; pre/post-transit interference) | UNDETECTABLE at SKA-1 (factor 91 below detect); folded shape correct sub-substrate-causal-disconnection signature |
| 8 | LiteBIRD n_T (CMB scale) | LiteBIRD / 2030 | n_T_FW(CMB) = −3.024×10⁻³ (S66 14.3× transfer suppression of transit n_T = +0.468) | n_T_LCDM = −r/8 = −1.466×10⁻³ | 8×10⁻⁴ | −1.95σ | NONE × 0 (STRUCTURAL-FLOOR) | PASS-STRUCTURAL-FLOOR (W1a-8) | PHONONIC (tensor moment at CMB scale; geometric 54-decade transfer) | NOT a falsifier; r=16ε INAPPLICABLE; EVOI = 0 through 2040 |
| 9 | Lab analogs (³He-B + K-STAR) | Ongoing experiments | Substrate-correlated to cosmo channels via shared spectral moments | (none — direct lab measurement) | Lab σ varies | Substrate-CORRELATED + Pipeline-INDEPENDENT ⇒ joint-evidence multiplier | MEDIUM × CONTINUOUS | INFO (W4-5; 3/5 FISHER/FP, 2/5 ANALOG-CANDIDATE-UNVERIFIED) | PHONONIC (most fundamentally; 60-OOM bridge) | Bridge cosmological channels to laboratory measurements; 2 rows pending lab-experiment validation |

---

**End of synthesis.** Files referenced by absolute path are in:
- `C:\sandbox\Ainulindale Exflation\sessions\archive\session-85\` (working papers W0..W5)
- `C:\sandbox\Ainulindale Exflation\sessions\archive\session-85\workshops\` (cutoff-authority + A_s band-authority)
- `C:\sandbox\Ainulindale Exflation\sessions\framework\cross-channel-correlation-matrix.md` (W4-2)
- `C:\sandbox\Ainulindale Exflation\sessions\framework\falsifier-watchlist.md` (W4-8)
- `C:\sandbox\Ainulindale Exflation\.claude\agent-memory\mack-cosmic-bridge\MEMORY.md`
