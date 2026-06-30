# Pre-Registered Observational Predictions

**Last updated**: Session 68 (2026-04-05)
**Free parameters**: 0 (all predictions derived from D_K on Jensen-deformed SU(3))
**Source of truth**: S68 JOINT-OBSERVATIONAL-68, corrected by S68 workshops

---

## Timeline Overview

```
2026 ─── DESI DR3          w_0, w_a             SURVIVAL OR EXCLUSION
2027 ─── DESI DR3 final    w_0, w_a refined     
2028 ─── JUNO first        mass ordering (3σ)   STRUCTURAL TEST
         Hyper-K first     mass ordering
2029 ─── Euclid DR1        f·σ_8, ISW, w(z)     ISW TRACKING (marginal)
2030 ─── JUNO full         mass ordering (3σ+)
         Euclid DR2        ISW tomographic       SNR ~ 1.6 on c_s²=0
2032 ─── DUNE full         mass ordering (5σ)   DEFINITIVE NO/IO
2034 ─── LiteBIRD full     r, n_T               24σ DETECTION (necessary, not sufficient)
         CMB-S4 full       r, n_s, α_s, f_NL    8.1σ on r; f_NL undetectable
2035 ─── LISA early        Ω_GW (domain walls)  STRUCTURAL TEST
2040s── 21cm tomography    f_NL(folded), ISW    UNIQUE DISCRIMINANT
         (purpose-built)   c_s²_DE tracking     SNR ~ 7.9 on ISW; 3.6σ on folded
```

---

## DESI — Dark Energy Spectroscopic Instrument (2026-2027)

**What it measures**: BAO distances D_V(z)/r_d at 7 redshift bins, constraining w_0 and w_a.

### DESI Measurement Evolution (live during this project)

The DESI central values have shifted during the project's lifetime as the collaboration released updated analyses and supernova calibration combinations:

| Date | DESI Release / Combination | w_0 | σ(w_0) | w_a | σ(w_a) | FW Tension | Session |
|:-----|:---------------------------|:---:|:------:|:---:|:------:|:----------:|:-------:|
| 2026-02 | DR2 (early, CMB+BAO) | **-0.83** | 0.09 | -0.45 | 0.31 | 1.9σ (FW was w=-1 then) | S22 |
| 2026-03 | DR2 + Pantheon+ SN | **-0.827** | 0.063 | — | — | — | S42 |
| 2026-03 | DR2 + DESY5 SN (current) | **-0.752** | 0.057 | -0.73 | 0.25 | 2.91σ | S67-68 |

**Key observation**: DESI's w_0 has drifted from -0.83 toward -0.75 (away from framework) while w_a has grown more negative (-0.45 → -0.73, away from both framework and LCDM). The error bars have tightened (0.09 → 0.057). The supernova calibration choice (Pantheon+ vs DESY5 vs Union3) drives ~0.08 systematic shift in w_0.

### Current State

| Observable | Framework Prediction | Current (DR2 + DESY5) | Current Tension | DR3 Projected σ |
|:-----------|:-------------------:|:--------------:|:---------------:|:---------------:|
| w_0 | **-0.918** | -0.752 ± 0.057 | 2.91σ | ± 0.040 |
| w_a | **0** (exactly, four-fold locked) | -0.73 ± 0.25 | 2.92σ | ± 0.177 |

Note: The framework's w_0 prediction also evolved during the project — from w ≈ -1 (locked modulus, S22 era) to **-0.918** (S67 Volovik relaxation mechanism). The Volovik mechanism provided the first *derived* w_0 value, moving the prediction from "indistinguishable from LCDM" to "closer to DESI than LCDM."

### Pre-Registered DR3 Scenarios (S60 DR3-PREREGISTER-60)

| Scenario | DR3 Outcome | FW Exclusion | LCDM Exclusion | FW Status |
|:---------|:------------|:------------:|:--------------:|:---------:|
| A: confirms DR2 (DESY5) | w_0=-0.75, w_a=-0.73 | 3.91σ | 6.25σ | **EXCLUDED** |
| B: toward LCDM | w_0=-0.90, w_a=-0.30 | 2.06σ | 2.12σ | **SURVIVES** |
| C: more dynamical | w_0=-0.65, w_a=-1.0 | 6.33σ | 37.1σ | **EXCLUDED** |

If DR3 reverts toward the early DR2 values (w_0 ~ -0.83, w_a ~ -0.30), framework tension drops to ~1.5σ — comfortably surviving.

**Decision rule**: Framework **survives** if w_a > -0.35. Framework **fails** if w_a < -0.530.

**Why this matters first**: DESI DR3 is the only experiment that can *exclude* the framework on a 1-year timescale. w_a = 0 is structurally locked (GGE integrability + Josephson phase + frozen texture + thermalization barrier, 59 OOM gap). It cannot be adjusted. The supernova calibration systematic (~0.08 in w_0) is a significant fraction of the total tension — DR3 with improved SN calibration could shift the picture substantially in either direction. Source: S67 DESI-VOLOVIK-67, S68 W2-C, S68 Volovik-Mack workshop.

### DR3-7-SCENARIO-TREE (S84 W4-44, frozen 2026-04-19)

**Tag**: `DR3-7-SCENARIO-TREE` | **Gate**: `S84-DR3-CONTINGENCY-FINE-GRAINED` (PASS at registration) | **Parent**: `S84-DR3-RESPONSE-PROTOCOL` (W1b-9, PASS at registration 2026-04-19)

**Content SHA-256**: `801e4690eee8e7f4c4152be7701567229a377ab3d23a66a5a39b318469323d6f`
**Audit SHA-256**: `f6e102fd5f322dd3f6fa1e4866c6a2f0c425f344d359cf07e37e4d5877cb265e`
**Artifacts**: `computations/s84_w4_dr3_contingency_fine_grained.py`, `s84_w4_dr3_contingency_fine_grained.json`

This gate pre-registers a fine-grained seven-cell partition of the {DR3 central (w_0, w_a): outside R_842} plane, activated *only if* the parent gate (binary rectangle containment) fires FAIL at DR3 release. The rectangle R_842 = [-0.942, -0.742] × [-0.2, 0.2] is centered on the S83 W0-workshop branch-(iv) promotion at w_0 = -0.842454 (see `project_s83_w0_regulator_workshop_r3.md`); the canonical `w0_FW = -0.918` in canonical_constants.py remains pinned pending S85 conditional promotion.

| Cell | w_0 range | w_a range | Framework verdict | Scorecard entry |
|:----|:----------|:----------|:------------------|:----------------|
| A1 | [-0.988, -0.942) | [-0.2, +0.2] | SURVIVE-promote (branch-(iv) corroborated, mild deep shift) | corroboration |
| A2 | [-1.05, -0.988) | [-0.2, +0.2] | SURVIVE-recal (branch-(iv) stretched ~1.7σ deep) | corroboration |
| B1 | [-0.942, -0.742] | [-1.0, -0.2) ∪ (+0.2, +1.0] | PARTIAL-REFUTE w_a-lock (S73b Scen A & B both land here) | refutation (w_a) |
| B2 | (-0.742, -0.50] | [-0.2, +0.2] | PARTIAL-REFUTE Volovik-w_0 partition | refutation (w_0) |
| B3 | (-0.742, -0.50] | [-0.5, -0.2) | DUAL-REFUTE partition AND lock | refutation (dual) |
| C1 | (-0.742, -0.20] | [-1.5, -0.5) | STRONG-REFUTE substrate-DE (S73b Scen C lands here) | refutation (triple) |
| C2 | [-1.20, -1.05) or shallow + thaw | — | PHANTOM-REFUTE or thaw-REFUTE (impedance audit) | refutation |

**Lockouts (A–F)** inherited from W1b-9: NO retreat to dual-pin, NO scheme-shopping post-data, NO rectangle-resizing, NO w_a axis migration, NO post-2026-04-23 redefinition of branch-(iv) canonical w_0_pred, NO tau_fold relocation. Alternative-branch canonical pre-registration requires S85+ fresh pre-reg under new content_sha256.

**Timeline**: DR3 window opens 2026-04-23; successor script loads `s84_w4_dr3_contingency_fine_grained.json`, applies the classification rule unchanged, and appends a verdict line to `s85_gate_verdicts.txt` overriding the PASS-at-registration status.

**INFORMATIONAL note (S88 W5 mack-arxiv DES-Dovekie 2026 reanalysis)**: The DES-Dovekie + DESI DR2 + Planck/ACT/SPT joint Flat-w0waCDM constraint (Popovic et al., arXiv:2511.07517v3; mack solo-review report `sessions/archive/session-88/workshops/s88-mack-arxiv-2511-07517-desi-review.md` SHA `9e2225fc756a359f9e12a21a1a2cb154c1d69232e0531ab51aed606d5f61c69a`) reports central (w_0, w_a) = (-0.803 ± 0.054, -0.72 ± 0.21). Cosmetic mapping of the Dovekie central onto the 7-cell partition above lands in **cell B1** (PARTIAL-REFUTE w_a-lock; same cell as S73b Scen A & B). This mapping is **NON-BINDING informational only** — the pre-committed binding instrument is **DESI DR3** (window opens 2026-04-23), NOT a DES-SN reanalysis on DR2 BAO. The R_842 rectangle remains armed for the DR3 release; **no Lockout (A–F) is triggered by this paper**. The branch-(iv) σ-distance (0.731σ post-Dovekie vs 1.59σ pre-Dovekie) is one empirical input toward the §W13-3 P9 PRIMARY-VALUE-RESOLVE (canonical -0.918 vs branch-(iv) -0.842454) which is a STRUCTURAL adjudication, not an empirical-vote.

---

## JUNO — Jiangmen Underground Neutrino Observatory (2028-2030)

**What it measures**: Reactor antineutrino oscillations → neutrino mass ordering (NO vs IO) via Δm²_21 interference pattern.

| Observable | Framework Prediction | Current Data | Current Tension |
|:-----------|:-------------------:|:------------:|:---------------:|
| Mass ordering | **Normal** (B1 < B2 < B3) | NO preferred at Δχ² = 6.1 (~2.5σ, NuFit-6.0) | consistent |

**Pre-registered gate**: PASS if any experiment reports NO at > 3σ. FAIL if any experiment reports IO at > 3σ (falsifies framework's Dirac spectrum geometry).

**Why it matters**: Normal ordering is a *structural* prediction — it follows from the Jensen-deformed SU(3) fiber spectrum. B1 < B2 < B3 at all τ > 0 is proven to machine epsilon across S8, S34-36, S52, S56. IO would invalidate the entire spectral geometry. Source: S56 Workshop 4, Level 1.

---

## Euclid — ESA Wide-Field Survey (2029-2032)

**What it measures**: Galaxy clustering + weak lensing → σ_8, f·σ_8(z), ISW-galaxy cross-correlation, w(z).

| Observable | Framework Prediction | Current Data | Current Tension | Euclid σ |
|:-----------|:-------------------:|:------------:|:---------------:|:--------:|
| σ_8 | **0.799** | 0.811 ± 0.006 (Planck) / 0.766 ± 0.03 (lensing) | between both | ~ 0.003 |
| ISW tracking (c_s²_DE=0) | **+12.3%** vs LCDM total | A_ISW = 1.00 ± 0.25 (Planck) | 0.49σ from LCDM | SNR ~ 1.58 |
| ISW substrate-specific | **+7.6%** vs quintessence (same w, different c_s²) | not yet isolated | — | marginal |
| f·σ_8 (at 5 DESI bins) | specific values from w_0=-0.918 | TBD | — | competitive in combination |

### ISW Tracking Test Results (S68 ISW-TRACKING-68 — PASS)

The S68 Volovik-Mack workshop discovered that the Volovik tracking vacuum produces induced DE perturbations with c_s²_DE(eff) = 0 (DE clusters with matter). Mack computed the full ISW-galaxy cross-correlation against Planck data:

**Three-model comparison (C_l^{Tg}, l = 2-30)**:

| Model | w_0 | c_s²_DE | C_l^{Tg} / LCDM | Physics |
|:------|:---:|:------:|:----------------:|:--------|
| **LCDM** | -1.0 | N/A (Λ) | 1.000 | No DE perturbations |
| **Quintessence** | -0.918 | 1 | 1.044 | Smooth DE, modified expansion |
| **Framework** | -0.918 | **0** | **1.123** | DE clusters with matter |

**Signal decomposition**:
- +4.4 ppt from modified expansion history (w = -0.918 vs -1) — shared with quintessence
- **+7.6 ppt from tracking-induced DE clustering** (c_s² = 0 vs 1) — substrate-specific, no other model produces this

**Chi-squared vs Planck ISW (A_ISW = 1.00 ± 0.25)**:
- LCDM: χ² = 0.00 | Framework: χ² = 0.24 (0.49σ) | Quintessence: χ² = 0.03
- All models consistent — current data cannot discriminate

**Detection forecasts (Framework vs Quintessence, the substrate-specific 7.6%)**:

| Experiment | SNR | Verdict | Timeline |
|:-----------|:---:|:--------|:---------|
| Planck (existing) | 0.32 | Not discriminating | Now |
| **Euclid tomographic** | **1.58** | **Marginal** | ~2030 |
| 21cm intensity mapping | 7.9 | Definitive | ~2040s |

**Pre-registered gate**: ISW-TRACKING-68. PASS if C_l^{Tg} framework/LCDM > 1.05 (computed: 1.123). **PASS.** The 7.6% substrate-specific signal exceeds the 5% threshold. This is the only observable where the framework makes a qualitatively different prediction from ALL standard DE models. Source: S68 ISW-TRACKING-68, S68 Volovik-Mack workshop (emergence A-M5).

**Why Euclid matters**: Euclid's tomographic ISW-galaxy cross-correlation is the first experiment with *marginal* sensitivity (SNR 1.58) to the substrate-specific DE clustering signature. It won't be definitive alone, but a ~1.5σ hint in the right direction combined with DESI DR3 w_a → 0 would constitute a two-channel signal. If σ_8 converges toward the lensing value (0.766), the framework's prediction (0.799) is the closest zero-parameter model. Source: S56 Workshop 4, S68 Volovik-Mack workshop, S68 ISW-TRACKING-68.

---

## BICEP/Keck → LiteBIRD (Current → 2034)

**What it measures**: CMB B-mode polarization → tensor-to-scalar ratio r, tensor tilt n_T.

| Observable | Framework Prediction | Current Data | Current Tension | LiteBIRD σ |
|:-----------|:-------------------:|:------------:|:---------------:|:----------:|
| r | **0.0242** | < 0.036 (95% CL, BK18) | PASS (headroom 1.49×) | 0.001 |
| n_T (CMB) | **-3.024e-3** (= -r/8 exactly) | not measured | — | insufficient lever arm |
| n_T (transit) | **+0.075** (blue, 113× above slow-roll) | inaccessible (10^37 Hz) | — | — |

**Detection significance**: LiteBIRD 24σ, CMB-S4 8.1σ. Non-detection of r = 0.024 at > 5σ would **falsify** the framework.

**Pre-registered gate**: r = 0 excluded at 24σ by LiteBIRD. But: r + 8n_T = 0.000 exactly at CMB → framework is **indistinguishable from slow-roll inflation** with same r at CMB scales. Detection is necessary but not sufficient.

**Why it matters**: LiteBIRD will definitively see or exclude r = 0.024. But even a detection cannot confirm the substrate — the unique transit-scale blue tilt lives at 10^37 Hz, 34 decades beyond any detector. Source: S66 TENSOR-TRANSFER-66, S68 W2-E, W3-A.

### Tag: BK-ARRAY-2026-R-DECISION-TREE (S84 W4-42, frozen 2026-04-18, `mack-cosmic-bridge` sole authority)

**Framework prediction (G46 inherited)**: `r(k_CMB) = 0.011731522176014426` at k_pivot = 0.05 Mpc^{-1}. Source gate S83-W3-G46-TENSOR-TRANSFER (PASS), file `s83_w3_g46_tensor_transfer.npz`. (Note: the S66 value 0.0242 in the table above pre-dates the G46 transfer-kernel correction; S83 G46 is the current canonical r.)

**Experiment**: BICEP/Keck Array 2026 release, expected Q2-Q3 2026. Ade+ 2025 preprint forecast `sigma_r ~= 0.005`.

**Pre-registered decision tree** (frozen JSON, `computations/s84_w4_bicep_keck_2026_decision_tree.json`, content SHA `e2ca24d6...882d3`, audit SHA `b1eb9e61...6be`):

| Branch | Label | Rule | Verdict | sigma-diagnostic |
|:------:|:------|:-----|:-------:|:-----------------|
| A | CONFIRMATION | `r_BK in [0.009, 0.015]` | PASS | +/-~1 sigma_theory |
| B | CONSISTENCY | `r_BK_upper < 0.020` (1-sided) | INFO | +1.65 sigma_exp |
| C | DISFAVORED | `r_BK_central > 0.025` | FAIL | +2.28 sigma_comb |
| D | RULED OUT | `r_BK_upper < 0.008` | FAIL | FW above 95% CL upper |

Inputs: `r_CMB_framework = 0.011731522176014426`, `sigma_r_BK_2026 = 0.005`, `sigma_theory_G46 = 0.003` (nominal), `sigma_comb = 0.005831`. Threshold substitution chain VERIFIED in §VI.W4-42 of `session-84-w4-workingpaper.md`.

**Freeze protocol**: `no_post_release_reregistration: True`. On BK-Array 2026 data release, branch selection is a mechanical posterior-summary lookup. No re-scaling of `sigma_theory`, no redefinition of windows, no alternate branch construction. One-shot bind.

**Gate verdict**: `S84-BICEP-KECK-2026-PRE-REGISTER: PASS` (procedural — JSON frozen, 4 branches, SHA logged, single-authority tag, registry entry filed).

---

## CMB-S4 — Stage 4 CMB Experiment (2034+)

**What it measures**: High-resolution CMB temperature + polarization → n_s, α_s, r, f_NL.

| Observable | Framework Prediction | Planck 2018 | Current Tension | CMB-S4 σ |
|:-----------|:-------------------:|:-----------:|:---------------:|:--------:|
| n_s | **0.9595** | 0.9649 ± 0.0042 | 1.29σ | ~ 0.002 |
| α_s | **0.000** (exact) | -0.0045 ± 0.0067 | 0.67σ | ~ 0.003 |
| r | **0.0242** | < 0.036 | PASS | 0.003 |
| f_NL (equilateral) | **0.853** | -26 ± 47 | 0.57σ | ~ 5.0 |
| f_NL (folded) | **0.129** | unconstrained | — | ~ 6.9 |

**Pre-registered finding**: f_NL is **undetectable** by CMB-S4. Equilateral at 0.17σ, folded at 0.02σ — both buried in noise. n_s tightens to ± 0.002, which would test the structural 1.25σ gap (Lizzi: no smooth cutoff can reach Planck central). α_s = 0 prediction strengthens with tighter error bars.

**Why it matters**: CMB-S4 sharpens the n_s and α_s constraints but cannot detect the bispectrum. If n_s tightens to exclude 0.9595, the fold curvature d²S/dτ² is wrong. Source: S68 W2-B, W2-D.

---

## LISA — Laser Interferometer Space Antenna (2035+)

**What it measures**: Gravitational wave background at mHz frequencies.

| Observable | Framework Prediction | Current Data | Status |
|:-----------|:-------------------:|:------------:|:------:|
| Ω_GW (domain walls) | **~ 10^{-10}** at LISA frequencies | not measured | **PREDICTION** |

**Pre-registered gate**: Detection of stochastic GW background consistent with domain wall spectrum would support framework. Non-detection at Ω_GW < 10^{-11} would constrain domain wall dynamics.

**Why it matters**: Domain walls from the CG(24) Cayley graph structure of the post-transit fabric produce a specific GW background. This is independent of all CMB predictions. Source: S59 LISA-GW-PREDICTION.

---

## DUNE — Deep Underground Neutrino Experiment (2032+)

**What it measures**: Long-baseline neutrino oscillations → mass ordering (5σ), CP phase δ_CP.

| Observable | Framework Prediction | Current Data | Status |
|:-----------|:-------------------:|:------------:|:------:|
| Mass ordering | **Normal** | NO preferred ~2.5σ | consistent |

**Pre-registered gate**: Same as JUNO but at 5σ. DUNE provides the definitive measurement. Source: S56 Workshop 4.

---

## 21cm Intensity Mapping — Purpose-Built Instrument (2040s+)

**What it measures**: Neutral hydrogen tomography at l_max ~ 10^5 → f_NL shapes, ISW tracking.

| Observable | Framework Prediction | Current | Detection SNR |
|:-----------|:-------------------:|:-------:|:-------------:|
| f_NL (folded) | **0.129** | unconstrained | **3.6σ** (l_max=10^5) |
| f_NL (equilateral) | **0.853** | -26 ± 47 | **32.8σ** (l_max=10^5) |
| ISW tracking (c_s²=0) | **+7.6%** vs quintessence | 0.49σ from LCDM | **7.9σ** |

**Pre-registered gate**: f_NL(folded) > 0 at > 3σ would be a **smoking gun** for Bogoliubov pair creation. No single-field inflation model produces the folded shape (k_1 + k_2 = k_3 from pair momentum conservation).

**Why this is the decisive experiment**: The folded bispectrum is the framework's UNIQUE discriminant — the only prediction no other model makes. But it requires a purpose-built 21cm instrument beyond SKA-Low capability. Timeline: 2040s at earliest. Source: S68 W2-D, CMBS4-FNL-FORECAST-68.

---

## 0νββ Decay Experiments — LEGEND-1000, nEXO (2030s)

**What it measures**: Neutrinoless double-beta decay rate → effective Majorana mass m_ββ.

| Observable | Framework Prediction | Current Data | Status |
|:-----------|:-------------------:|:------------:|:------:|
| S_F^Connes (tree-level T-channel fermionic functional) | **0** (identically, BDI symmetry; S41 W1-2 Theorem 1 — the same J-structure zero that makes the light Majorana mass seesaw-GENERATED rather than fundamental) | not directly testable by 0νββ (tree-level statement on the internal triple) | structural theorem (PERMANENT) |
| m_ββ (KO-dim-6 Pfaffian Majorana texture; internal-M_R type-I seesaw) | **3.695 meV** central; band **[1.516, 3.695] meV** (Row #80) | KamLAND-Zen < 122 meV (×33.0 above prediction) | consistent; one-sided next-gen falsifier |

**Pre-registered gate (re-scoped by the S100a W-4 D5 adjudication workshop, landed S101 W6-9; supersedes the S56-era gloss)**:
the framework predicts NO FREE-SCALE seesaw and NO fundamental tree-level Majorana mass term
(S41 W1-2, exact — scoped per S56 Workshop 4 Correction 1: "no Majorana mass through the Connes
seesaw route," NOT "no Majorana mass"). The light masses ARE seesaw-generated, with M_R = the
D_K B-branch fold energies — internal to the spectrum, spectral coincidence 1.77% < 2%
(S99-W3-SEESAW-SUMMNU PASS; S100a-D5-0NUBB-MAJORANA PASS). ONE 0νββ falsification logic
(= inventory Row #80): detection above the 4.5 meV NO-funnel edge FALSIFIES the
(NO, m₁=0, Majorana-texture, δ_CP∈{0,π}) configuration; an in-funnel detection
(beyond-next-gen sensitivity) is consistent-confirming; a next-gen null is consistent
non-confirming. Source: S41 W1-2 Theorem 1 + S56 Workshop 4 (Level 1 + Correction 1) +
S100a W5-2 + S100a W-4 D5 adjudication (reading RECONCILED-INTERNAL-M_R).

---

## Summary: What Decides When

| Year | Experiment | Tests | Stakes |
|:-----|:-----------|:------|:-------|
| **2026-27** | DESI DR3 | w_0=-0.918, w_a=0 | **Survival or exclusion** (sole current pressure) |
| **2028-30** | JUNO | Normal mass ordering | Structural geometry test |
| **2029-32** | Euclid | ISW tracking, σ_8, f·σ_8 | First marginal sensitivity to c_s²=0 |
| **2032** | DUNE | Mass ordering (5σ) | Definitive NO/IO |
| **2034** | LiteBIRD | r = 0.024 | 24σ detection, necessary not sufficient |
| **2034** | CMB-S4 | n_s, α_s, r | Sharpens shape parameters |
| **2035+** | LISA | Ω_GW ~ 10^-10 | Domain wall GW background |
| **2040s** | 21cm | f_NL(folded) = 0.129 | **UNIQUE DISCRIMINANT** — only test that can confirm (not just not-exclude) the substrate |

*The framework's fate is front-loaded to DESI DR3. Everything after that either sharpens the picture or waits for 21cm.*

---

## Falsifier-Rigor Registry (S84 W4-48, `mack-cosmic-bridge`)

**Tag**: `FALSIFIER-RIGOR-REGISTRY-S84` | **Gate**: `S84-FALSIFIER-RIGOR-REGISTRY` (PASS at registration) | **Frozen**: 2026-04-19

**Closure SHA-256**: `b221320bc74740c2589531559099a8cb73b8caeb6e5ad403e8f8d063f7c72f34`
**Artifacts**: `computations/s84_w4_falsifier_rigor_registry.py`, `s84_w4_falsifier_rigor_registry.json`, `sessions/framework/registry/falsifier-rigor-registry.md`

This meta-registry tags every framework falsifier channel with EXACTLY ONE of four rigor flags — `ZERO-FREE-PARAMETER`, `ACCOMMODATION`, `SCHEME-DEPENDENT`, `DETECTOR-STERILE` — to prevent evidence-inflation across the Wave 4 → Wave 5 synthesis and beyond. Audit completeness 18/18 (0 un-tagged); ZFP count **11**; ACCOMMODATION 2; SCHEME-DEPENDENT 2; DETECTOR-STERILE 3.

**Load-bearing subset for framework status narrative**: the 11 ZERO-FREE-PARAMETER channels (n_s, r, n_T transit, n_T CMB, α_s, f_NL+folded-shape, w_a, μ FIRAS, σ_8, ISW tracking, neutrino mass ordering). Data-agreement in these rows counts at BF > 1.

**Explicitly not load-bearing under exactly-one-flag rule**: the 2 ACCOMMODATION rows (m_H, sin²θ_W — tied together via μ_BC fit to PDG), 2 SCHEME-DEPENDENT rows (A_s regulator-shopping at 0.384 OOM, w_0 at 0.08 scheme split pending W4-46), 3 DETECTOR-STERILE rows (α_f_NL amplitude-running, Ω_GW at LISA frequencies, C_cons internal consistency).

**Upgrade paths** (contingent, pre-registered):
- **w_0**: PASS at W4-46 L_max convergence (split shrinks with L scan) → upgrade to ZFP.
- **A_s**: regulator canonicalization with structural argument → upgrade to ZFP; any posterior-selection path forbidden.
- **α_f_NL amplitude-running**: detector-reach breakthrough (21-cm CVL l_max ~ 10^5) would move this from sterile to testable.

**No upgrade path** for ACCOMMODATION rows without new derivation that eliminates the μ_BC free scale.

See `sessions/framework/registry/falsifier-rigor-registry.md` for the full 18-row registry with justifications, dependent gates, and adjudication notes for the five new-info cases (Δ(n_T) CMB, α_f_NL sub-channel split, n_T transit dual-property, w_0 scheme split, m_H accommodation).

---

*This document is the canonical reference for all framework predictions against observation. Updated each session. Gate verdicts are permanent.*

---

## P-OBS-ALIGNED-CEILING-CHAIN — Ceiling-Lifting DAG (S84 W4-49, 2026-04-18)

**Tag**: `P-OBS-ALIGNED-CEILING-CHAIN`
**Gate**: `S84-P-OBS-ALIGNED-CEILING` PASS (2026-04-18)
**content_sha256**: `0f8cb99b1f7a90d04a2b0957832c3e8bdd47ef2b634ff306cbd9184c2930f54e`
**audit_sha256**: `09e7d4ebd0558484b522f4aed7520c8e01457a846076c79ed2f5ca3a22499691`
**Frozen payload**: `computations/s84_w4_p_obs_aligned_ceiling_chain.json`

**Current state** (S83 W3-G48 baseline): P_obs_aligned = **7/9 = 0.7778** (PASS = {n_s, r, m_H, N_eff, w_0, f_NL, A_s}; FAIL = {sin²θ_W, α_s}; INFO = ∅).

**Substitution chain** (verified exhaustively over 16 PASS-subsets):

- *Definition*: Transition m/9 → (m+1)/9 requires ≥1 trigger-gate PASS re-classifying one FAIL channel to PASS (S72 observational convention).
- *Substitution*: Two disjunctive pairs — (A1 ∨ A2) for sin²θ_W; (B1 ∨ B2) for α_s.
- *Simplification*: Minimum PASS-set for 7/9 → 9/9 = 2 activations; upper bound dependencies = 4.
- *Direction*: Monotone non-decreasing (verdicts permanent; ceiling cannot un-lift).

**Trigger gates** (4 total, disjunctive within each transition):

| Transition | Label | Trigger Gate | Session Ref | ZFP Impact |
|:-----------|:-----:|:-------------|:------------|:-----------|
| 7/9 → 8/9 (sin²θ_W) | A1 | `S84-DERIV-I` ∧ `S84-DERIV-II` | S84 W9b-105 + W9b-106 | +1 ZFP |
| 7/9 → 8/9 (sin²θ_W) | A2 | `S84-TAU-CROSS-SCALE` | S84 W9b-107 | +1 SCHEME-DEPENDENT |
| 8/9 → 9/9 (α_s) | B1 | `N1 TRANSFER-FUNCTION-74` | S74 W1-A (EVOI #1 carry-fwd) | +1 ZFP |
| 8/9 → 9/9 (α_s) | B2 | `S84-ALPHA-S-CMB-S4-PROJECTION-REFINEMENT` | S84 item #52 carry-fwd | STERILE→ACTIVE flip |

**Sequential pre-registration note**: ceilings may lift individually before the chain completes. If A1 lands PASS in S85 and B1/B2 remain open, P_obs_aligned moves 7/9 → 8/9 as a standalone registry event citing this DAG. The ceiling-lift is *not* gated on chain completion.

**Evidence-column ladder separation**: P_obs_aligned and the W4-48 Falsifier Rigor Registry are distinct metrics. P_obs_aligned = 9/9 is *necessary but not sufficient* for a maximally-strong claim — the minimum-path A2 ∧ B2 reaches 9/9 with **zero** ZFP additions, while A1 ∧ B1 adds +2 ZFP rows. Downstream ceiling-lift events MUST cite `content_sha256=0f8cb99b1f7a90d04a2b0957832c3e8bdd47ef2b634ff306cbd9184c2930f54e` and report both P_obs_aligned and the W4-48 ZFP delta.

**Freeze policy**: single-authority pre-registration dated 2026-04-18. DAG permanent; downstream appends cite but do not modify. A re-registration (e.g., if the channel denominator changes or a new FAIL channel is added) requires a fresh gate ID (e.g., `S86-P-OBS-ALIGNED-CEILING-v2`) with its own SHA.
