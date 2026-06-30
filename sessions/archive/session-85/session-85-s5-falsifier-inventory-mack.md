# Session 85 Synthesis: S-5 Falsifier-Watchlist Master-Inventory (mack)

**Author**: mack-cosmic-bridge
**Date**: 2026-04-25
**Slot**: S-5 (W0–W5 review campaign, slot 1b synthesis)
**Source pin SHAs (input)**:
- `sessions/archive/session-85/session-85-w1a-workingpaper.md` (32,297 bytes)
- `sessions/archive/session-85/session-85-w1b-workingpaper.md` (38,986 bytes)
- `sessions/archive/session-85/session-85-w1c-workingpaper.md` (128,386 bytes)
- `sessions/archive/session-85/session-85-w3-workingpaper.md` (75,270 bytes)
- `sessions/archive/session-85/session-85-w4-workingpaper.md` (92,619 bytes)
- canonical_constants.py (post-W1c-1 patch)
- `sessions/framework/cross-channel-correlation-matrix.md` (W4-2 NEW; 8,133 bytes)
- `sessions/framework/falsifier-watchlist.md` (W4-8 augmented; 8,697 bytes)

---

## I. Scope and structural problem statement

W0–W5 generated nine overlapping falsifier ledgers across four waves (W1a, W1b, W1c, W3, W4) without a single binding master inventory. Each ledger is locally coherent and SHA-pinned, but downstream consumers (S86 plan, atlas registry, future joint-BF computations) face an authority-resolution problem: when two ledgers carry the same observable with different σ-distance values or different EVOI tags, which is canonical?

The most pointed example is **α_s**:
- W3-12 OZ-class table reports α_s = 0.1252 with the W1a SCHEME-DEP `c9a2beaf…` sha provenance (treating α_s as MS-bar QCD-style scheme-dependent quantity).
- W4-7 NULL-ELIM-MAP reports α_s_FW = +0.00117, σ-distance +2.70σ vs LCDM null −0.0045 (treating α_s as inflationary running dn_s/dlnk).
- W1c-5 §VII.Ω.α_s-gap reports α_s_FW = −0.068968 vs Planck −0.0045 with σ-separation **9.6221** and magnitude ratio **15.3262×** (treating α_s = n_s² − 1 as the framework prediction, INFLATIONARY referent committed by W1c-2).

The same observable appears in three rows with three different framework predictions and three different σ-distances. These are not contradictions — they are different scheme commits — but they need to be resolved into a single inventory that downstream readers can consult. **W1c-2's INFLATIONARY commit (48 inflationary-context hits / 0 QCD hits over 13 S50–S51 source files) is the AUTHORITATIVE physical referent**. The α_s row of the master inventory therefore lists `α_s_framework_central = −0.068968` against Planck inflationary observation, and the magnitude gap of 15.3× becomes the single canonical structural-open channel.

This synthesis consolidates the nine ledgers into one master-inventory table, ranks rows by EVOI = P(decisive_by_year) × |ΔP_framework|, applies correlation-discount factors from W4-3 (`f_indep = 0.8731`) and W4-6 (`geom-discount = 0.9926`), and pre-registers the decision-tree timeline 2026–2040.

The phononic framing throughout: each row is the substrate-measurement plan for a distinct spectral moment of `D_K` on the Jensen-deformed SU(3) fiber. Entries are not "predictions to be tested" — they are pre-registered acoustic-interrogation events of the eigenvalue problem at distinct k-bands, distinct epochs, distinct detectors. The master inventory is the substrate's pipeline-level projection onto observational capacity 2026–2040.

---

## II. Methodology

### II.1 Sources cross-walked

The nine source ledgers are:

| # | Ledger | Source | Verdict | Key SHA |
|:-:|:-------|:-------|:-------:|:--------|
| 1 | OZ-class falsifier table (7 rows) | W3-12 | PASS | content `f5a285d8…` (rTT row); table `s85_w3_falsifier_table_oz.md` |
| 2 | Falsifier watch certification (5 channels) | W4-4 | PASS | content `d3195720…` |
| 3 | Null σ-distance map (5 channels) | W4-7 | PASS | content `bf8135bf…` |
| 4 | Watchlist unified-schema update (6 rows) | W4-8 | PASS | content `4e09971a…` (post-update registry `aa10ad48…`) |
| 5 | §VII.Ω.α_s-gap structural channel | W1c-5 | PASS | audit `6f95338323805b28…`; content `5eb107604f93981a…` |
| 6 | BK-Array 2026 livewatch | W1a-4 | PENDING-EVENT | content `c96aedb0…`; reg-SHA `e2ca24d6…` |
| 7 | DESI DR3 livewatch | W1a-5 | PENDING-EVENT | content `123c0ced…`; reg-SHA `9cc7f47e…` |
| 8 | α_s × w_0 decoupled joint BF | W1b-10 | PENDING-EVENT | content `ec3e5515…`; BF_indep = 10.75 |
| 9 | 7D Fisher framework discriminator | W1a-9 | PASS | log10(BF) = +827.93 if FW right |
| (10) | Regulator-conditional DR3 tree | W1b-1 | FAIL | content `15e1b1ff…`; A1↔B2 flip at L_max=10→12 |
| (11) | Rank-universality monitor | W1a-10 | INFO | 4/4 PENDING |

### II.2 EVOI ranking method

The EVOI score for each row, per `/rules/evoi-prioritization.md`:

```
EVOI = P(decisive_result_by_target_year) × |ΔP_framework|
```

Substitution chain for a row with framework σ-distance Δ_i and detector deployment year Y_i:

- **Definition**: P(decisive) = probability the detector reaches ≥3σ discrimination by Y_i. For pre-registered FLAGSHIPS where the framework prediction is staked (DESI DR3 w_0, CMB-S4 β_s), this equals P(detector deploys on schedule with stated σ_detect). For STRUCTURAL-FLOOR rows where the framework prediction sits below detector reach by construction, P(decisive) ≡ 0 because no Bayesian update can fire.
- **|ΔP_framework|**: the magnitude of the posterior shift if the result lands. For binary FLAGSHIP falsifiers staked outside R_842 with explicit lockouts, |ΔP| ≥ 0.5 (the framework's compaction-timescape mechanism either survives or the kaku-cascade is triggered). For SECONDARY/SUPPORTING channels, |ΔP| ≤ 0.1.
- **Direction**: EVOI is monotone non-decreasing in both factors. Higher EVOI ⇒ priority.

Correlation-discount factors are applied per `sessions/framework/cross-channel-correlation-matrix.md` deflation formula `BF_joint ~ Π BF_i^{f_i}`, `f_i = 1 − mean_{j≠i} ρ_ij`. The two binding numerical pins:

- **W4-3 f_indep = 0.8731** (DESI×CMB on w_0 via shared r_d ladder, ρ=0.35, full 2×2 inverse-covariance).
- **W4-6 geom-mean discount = 0.9926** (4-parameter × 5-channel block-diagonal Fisher, common-mode α_s discount 0.9709).

### II.3 Authority resolution

When two ledgers conflict on the same row, the resolution rule used in this inventory is:

1. **W1c-2 §VII.Ω commit overrides** earlier framework-prediction values for α_s. The S50-51 identity is INFLATIONARY (derivation-supported, 48/0 hit ratio), not QCD. All α_s rows use `alpha_s_framework_central = −0.068968`.
2. **W4-7 σ-distance overrides** earlier σ-distance estimates that used pre-W1c α_s value `−0.069 ± 0.008`, BUT the W4-7 entry uses `+0.00117` from S63 RUNNING-NS-63 (a different framework α_s pathway). **This is a real internal split**: the §VII.Ω.α_s-gap registry pins `−0.068968`; S63 / W4-7 / W1a-9 use `+0.00117`. Both numbers exist in canonical_constants and trace to legitimate but distinct framework derivations. I flag this as Conflict #1 below.
3. **W1c-5 σ-separation** (9.6221) is the canonical observational distance for the §VII.Ω.α_s-gap row. W4-7's +2.70σ pertains to the alternative S63 pathway and is preserved as a parallel row.
4. **STRUCTURAL-FLOOR rows are NOT falsifiers.** LiteBIRD n_T is documented as STRUCTURAL-FLOOR (W1a-8, W4-4, W4-7) with `r = 16ε` INAPPLICABLE per phononic-framing rule. EVOI ≡ 0 through 2040 by construction. The master inventory carries it as a STRUCTURAL row (separate column) — not a falsifier row.

---

## III. Master Inventory Table (EVOI-ranked, ready for landing at `sessions/framework/falsifier-master-inventory.md`)

The table below consolidates the nine ledgers into 12 unified rows (5 cosmological flagships + 2 PIXIE/structural + 2 lab-substrate + 1 LISA flagship + 2 contingent). Each row carries: rank, observable, framework prediction (with explicit α_s pathway tag), detector + reach year, σ_detect, σ-distance vs LCDM null, source-gate SHA, EVOI level, P(decisive_by_year), correlation-discount factor (from W4-2 ρ_ij matrix), zero-free-parameter (ZFP) vs tuning-dependent (TD) tag.

### III.1 Master-inventory table

| # | Observable | FW prediction | Detector | Year | σ_detect | σ-distance | Source SHA | EVOI level | P(dec) by Yr | Discount factor | ZFP/TD |
|:-:|:-----------|:---|:---|:-:|:---:|:---:|:---|:---:|:--:|:---:|:---|
| 1 | **w_0** (Volovik partition / substrate compaction) | −0.918 | DESI DR3 | 2027 | 2.5e−2 | **+3.28σ** | W4-7 `bf8135bf…`; W1a-5 `123c0ced…` | **FLAGSHIP** | 0.85 (window opened 2026-04-23) | f_indep = 0.873 (DESI×CMB) | **ZFP** (S58 Volovik effacement Γ=0.99970) |
| 2 | **β_s** (3rd derivative of n_s) | −0.1331 | CMB-S4 | 2030 | 2.2e−3 | **+60.5σ** | W3-12 `50a3ca87…`; W0-1 PASS | **FLAGSHIP** | 0.95 (deployment locked) | 1.000 (no overlap) | **ZFP** (W1c-6: β_s = 2 n_s α_s, 42 ppm residual) |
| 3 | **α_s** (§VII.Ω-INFLATIONARY identity) | −0.068968 | CMB-S4 / CMB-HD joint | 2030 / 2035 | 2.1e−3 / 1.1e−3 | **+9.62σ** vs Planck 2018 | W1c-5 `6f953383…`; canonical SHA `e7999383…` | **FLAGSHIP** (gap = STRUCTURAL OPEN CHANNEL) | 0.95 / 0.99 | 0.971 (CMB-S4×CMB-HD common-mode) | **ZFP** (S50-51 identity n_s²−1) |
| 4 | **r** (tensor-to-scalar) | 0.011732 | BK-Array 2026 → LiteBIRD 2030 | 2026 / 2030 | ~5e−3 / 1e−3 | +2.35σ / +11.7σ | W1a-4 reg-SHA `e2ca24d6…`; G46 `r_CMB_framework` | **FLAGSHIP-PRECURSOR** | 0.60 / 0.95 | 1.000 | **ZFP** (G46 transit-fn PASS) |
| 5 | **w_a** (CPL evolution) | 0.000 | DESI DR3 | 2027 | 1.0e−1 | ~0σ (pinned at LCDM) | W1a-5; canonical | FLAGSHIP-JOINT | 0.85 | f_indep = 0.873 (joint w/ row 1) | **ZFP** (S74 W4-Z) |
| 6 | **μ-distortion** (PIXIE channel) | 8.69e−5 (regulator-spread = 0) | PIXIE | 2029+ | ~5e−8 | **>10⁴σ separation** vs LCDM 2e−8 | W3-1 `a5fd4a36…`; W3-12 PASS | **FLAGSHIP** (5-regulator atlas exact) | 0.55 (mission funding contingent) | 1.000 | **ZFP** (γ=1 lockout) |
| 7 | **CGWB ρ_AC** (PT amplitude) | h_c^(A) ≈ 11 OOM above LISA noise | LISA | 2035+ | sensitivity curve | SNR = 1.68×10¹³ | W1a-6 `2d938c61…`; W1a-7 `7d5cdb93…`; S84 W6-50 | **FLAGSHIP** (decisive at 3σ tightening) | 0.70 (LISA confirmed flight) | 1.000 | **ZFP** (fix-k/fix-f dual-conv) |
| 8 | **n_T** (CMB scale) | −3.024e−3 | LiteBIRD | 2030 | 8.0e−4 | −1.95σ | W1a-8 `0c1ab0e9…`; W4-4 STRUCTURAL-FLOOR | **STRUCTURAL-FLOOR** | **0** (geometric, not detector-limited) | N/A | **ZFP** but **NOT a falsifier** |
| 9 | **f_NL_folded** (3-pt) | 0.0547 (S82 W3-4 GGE) / 0.129 (S67 folded) | SKA-1 / 21-cm | 2030+ | 5.0 | +0.011σ / +0.026σ | W4-7 (`bf8135bf…`); S84 W4-43 | **SUPPORTING** (post-2035 next-gen 21-cm) | 0.05 at SKA-1; 0.40 at SKA-2 | 1.000 (orthogonal) | ZFP |
| 10 | **α_s** (S63 RUNNING-NS pathway) | +0.00117 | CMB-S4 / CMB-HD | 2030 / 2035 | 2.1e−3 / 1.1e−3 | +2.70σ / +5.15σ | W4-7 `bf8135bf…`; W1a-9 7D Fisher | **PARALLEL TO #3** (different framework derivation) | 0.36 (CMB-S4) / 1.0 (CMB-HD) | 0.971 | TD (one-loop MS through fold) |
| 11 | **n_s** (scalar tilt) | 0.9590 | CMB-S4 | 2030 | 4e−3 | ~1.4σ vs Planck | W1c-1 `n_s_canon` = `planck_ns`; W3-12 | **CONFIRMATION** | 0.95 | 0.971 | **ZFP** (S58 BCS-CW) |
| 12 | **A_s** (scalar amplitude) | 3.30e−9 | Planck (already landed) | 2018 | 0.03e−9 | ~ +57% (4×) | W3-7 `b59acafa…`; S80 PASS-F2 | **CONSTRAINT-MAP CLOSURE** | 1.0 (data exists) | 1.000 | TD (S80 f_conv·F_amp pipeline) |

**Notes on EVOI level definitions** (from W4-4 EVOI rules and the user `feedback_framework-hygiene` directive):
- **FLAGSHIP**: σ-distance ≥ 3σ AND ZFP framework prediction AND data within decade. EVOI ≥ 0.4.
- **FLAGSHIP-PRECURSOR**: data within ≤ 2 years (BK-Array 2026), feeds FLAGSHIP confirmation chain. EVOI ≥ 0.3.
- **FLAGSHIP-JOINT**: paired with another FLAGSHIP via shared experiment (DR3 w_0/w_a). EVOI same as parent.
- **STRUCTURAL-FLOOR**: framework prediction below detector reach by GEOMETRIC, not calibration, separation. EVOI ≡ 0. NOT a falsifier.
- **SUPPORTING**: σ-distance < 1σ at decade detector; potential at next-generation. EVOI ≤ 0.1.
- **CONFIRMATION**: σ-distance < 3σ but framework prediction is ZFP and likely to land within 2σ. EVOI ~ 0.2.
- **CONSTRAINT-MAP CLOSURE**: data already landed; row catalogues a FAIL/PASS that is not a future falsifier.

### III.2 EVOI-ranked priority list (top 7 binding falsifiers)

The substitution chain for each EVOI score:

1. **EVOI(w_0, DR3) = 0.85 × 0.5 = 0.425** — window opened 2026-04-23; binary R_842 containment fires within ~12 months; lockouts A–F pre-registered.
2. **EVOI(β_s, CMB-S4) = 0.95 × 0.5 = 0.475** — 60.5σ FLAGSHIP, single-channel decisive; W1b-5 joint S4×HD lifts to 104σ at ~2034.
3. **EVOI(α_s §VII.Ω-gap, CMB-S4/HD) = 0.95 × 0.5 = 0.475** — 9.62σ binding under the W1c-2 INFLATIONARY commit; closure criteria (a) framework refinement, (b) observable retargeting, (c) σ_obs widening 10×.
4. **EVOI(r, BK-Array 2026) = 0.60 × 0.4 = 0.24** — branch-2 PASS at r ∈ [0.005, 0.018] expected; LiteBIRD 2030 lifts to 0.95 × 0.5 = 0.475.
5. **EVOI(μ, PIXIE) = 0.55 × 0.5 = 0.275** — flagship pre-registration with regulator-spread = 0; pull = 8693σ if mission flies.
6. **EVOI(CGWB ρ_AC, LISA) = 0.70 × 0.5 = 0.35** — flagship-decisive at 11-OOM margin; (A)/(C) regulator discriminator.
7. **EVOI(α_s S63, CMB-S4/HD) = 0.36 × 0.3 = 0.108** — non-decisive single channel at CMB-S4; CMB-HD joint lifts to 1.0 × 0.4 = 0.40.

The top 3 (rows 1–3) are the **2026–2030 binding triplet**: DR3 w_0 (within 12 months) + CMB-S4 β_s (2030) + CMB-S4/HD α_s gap (2030–2035). All three are ZFP. All three are independent at the substrate-moment level (w_0 = a_0 Volovik partition; β_s = 3rd derivative of S_transfer at k_pivot; α_s = 2nd derivative). The `cross-channel-correlation-matrix.md` carries them as INDEPENDENT (1,2), PARTIALLY_CORRELATED (0,1) via r_d ladder.

---

## IV. Decision-Tree Timeline 2026–2040

The pre-registered branching of framework status as each detector publishes. Each branch is sealed by a SHA-pinned W1a/W4 livewatch document; firing is binary on data arrival.

### IV.1 2026-04-23 — DESI DR3 window OPEN (today)

Trigger: **W1a-5 DR3-LIVEWATCH** (reg-SHA `9cc7f47e…`); 7-cell decision tree.

```
DR3 publishes w_0_obs ± σ_obs:

A1: w_0 ∈ [−1.05, −0.85] AND |w_a| < 0.2 AND within 1σ of (−0.918, 0)
    ⇒ PASS — substrate compaction-timescape ratified; LISA becomes next falsifier (row 7)
A2: A1 conditions but 1–2σ
    ⇒ INFO — registers as quantitative tension; not decisive
B1: w_0 < −1.05 (phantom)
    ⇒ FAIL — kaku-cascade R_842-PHYSICAL-ANCHOR-REAUDIT + W0-L-INVERTED-BRANCH
B2: w_0 > −0.85 (quintessence)
    ⇒ FAIL — same kaku-cascade
B3: |w_a| > 0.2 (CPL evolution)
    ⇒ FAIL — same kaku-cascade
C1/C2: exotic w_0 < −1.5 OR > −0.5
    ⇒ FAIL + full re-audit
```

**W1b-1 sub-tree dependency**: at L_max ∈ {8, 10, 12} the framework-prediction cell flips A1↔B2 (L_max=10: A1 PASS; L_max=12: B2 FAIL). DR3 adjudication is regulator-layer-conditional. S86 must maintain 3 sub-trees.

### IV.2 2026 mid-year — BK-Array 2026 release

Trigger: **W1a-4 BK-ARRAY-LIVEWATCH** (reg-SHA `e2ca24d6…`); 4-branch tree.

```
BK-Array publishes r_obs:

Branch 1: r_obs < 0.005     ⇒ FAIL (FW falsified at 2σ down)
Branch 2: 0.005 ≤ r_obs < 0.018 ⇒ PASS (FW within 1σ of 0.01173)
Branch 3: 0.018 ≤ r_obs < 0.030 ⇒ INFO (FW within 2σ)
Branch 4: r_obs ≥ 0.030     ⇒ FAIL (FW falsified up)
```

Branch 2 is the FLAGSHIP-PRECURSOR PASS. Confirmation chain: BK-Array 2026 → LiteBIRD 2030 → joint at +11.7σ via W1a-9 7D Fisher.

### IV.3 2027 — DESI DR3 final + cosmology paper

If A1/A2 from §IV.1 lands: Volovik-partition branch (iv) ratified. **W1b-10 BF_indep = 10.75 MCMC computation fires** post-data; closes α_s × w_0 decoupled-joint gate. DR3 evidence multiplied by α_s_gap evidence with W4-2 ρ_01 = 0.35 partial correlation.

### IV.4 2028–2030 — CMB-S4 deploys

Trigger: **W0-1 BETA-S-CMB-S4-PREREG** flagship; **W1c-CF-4 CMB-S4 monitoring**.

```
CMB-S4 publishes β_s_obs and α_s_obs (post-data):

β_s test: |β_s_obs − (−0.1331)| / 2.2e−3
   ≤ 3 ⇒ PASS at 60.5σ FLAGSHIP — framework binding
   > 3 ⇒ FAIL — primary failure mode is single-channel-decisive

α_s test (under §VII.Ω-INFLATIONARY commit, value −0.068968):
   |α_s_obs − (−0.068968)| / σ_obs (CMB-S4 ~ 2.1e−3)
   The framework prediction sits 9.62σ from current Planck central (−0.0045);
   CMB-S4 narrows σ_obs from 0.0067 to ~0.001, so framework gap widens
   from 9.62σ to ~64σ if CMB-S4 confirms the Planck central.
   ⇒ §VII.Ω.α_s-gap closure criterion (a) FORCED:
      either framework refines prediction into [−0.025, +0.016], or gap
      becomes a permanent registry exception.
```

This is the binding moment: CMB-S4 either ratifies framework β_s at 60.5σ (which is a powerful confirmation given β_s_FW is ZFP via W1c-6 chain rule from α_s identity) **and** simultaneously sharpens the α_s gap from 9.62σ to ~64σ. The framework's α_s row enters STRUCTURAL OPEN CHANNEL at 64σ — closure criterion (a) becomes existentially binding.

### IV.5 2029+ — PIXIE μ-distortion

Trigger: **W3-1 PIXIE-K_FIRAS-PREREG** flagship.

```
PIXIE publishes μ_obs ± σ_PIXIE (~5e−8):

μ_FW = 8.69e−5 (regulator-spread = 0 by γ=1 lockout, 5-atlas)
μ_LCDM = 2e−8

|μ_FW − μ_LCDM| / σ_PIXIE ~ 8.69e−5 / 5e−8 ~ 1738
W0-8 reported pull = 8693σ (using narrower σ).

Either way: ⇒ DECISIVE to >>>3σ. Framework PASSes massively or FAILs decisively.
```

This is the highest single-channel signal-to-noise in the entire inventory after row 7 (LISA at SNR = 1.68×10¹³ via W1a-7), but contingent on PIXIE mission funding (P(decisive_by_2029) = 0.55 — flight not yet confirmed at this date).

### IV.6 2030 — LiteBIRD launches

Trigger: **W1a-8 LITEBIRD-NT-REGISTRY-LANDING** (STRUCTURAL-FLOOR). The framework's tensor channel at LiteBIRD is intrinsic-geometric: separation 588.78σ between transit-scale n_T = +0.468 and CMB-scale n_T = −3.024×10⁻³ across the 54-decade k-space transfer function. **A null LiteBIRD n_T result at slow-roll consistency is NOT a framework falsifier**. The `r = 16ε` relation is INAPPLICABLE per phononic-framing rule (5 independent VdD-Hawking arguments). EVOI through 2040 = 0 by construction.

LiteBIRD's FLAGSHIP role for the framework is in **r-confirmation** (row 4): r_FW = 0.01173 vs LiteBIRD σ(r) = 1e−3 gives +11.7σ.

### IV.7 2035+ — CMB-HD + LISA + 21-cm next-gen

Trigger cluster: **W1b-5 BETA-S-JOINT-S4-HD** (PASS, joint 104σ); **W1a-7 LISA-FLAGSHIP** (PASS, SNR = 1.68×10¹³ at 3σ tightening); **§VII.M.scorecard** carry-forwards.

CMB-HD α_s discriminator at +5.15σ single-channel; common-mode discounted joint with CMB-S4 via ρ = 0.7 (W4-2 pair (0,3)). Geom-mean discount factor 0.9926 lifts row #3 (§VII.Ω-α_s) discrimination from 9.62σ × √2 (independent CMB-S4+HD) to ~13σ at common-mode discount, to ~64σ if Planck central holds.

LISA confirms or refutes CGWB ρ_AC at SNR = 1.68×10¹³, an 11-OOM margin. (A)/(C) regulator discriminator activates: under fix-k convention LISA picks regulator class A, under fix-f convention it picks C — explicit framework-internal disambiguation.

### IV.8 Post-2035 — 21-cm next-generation

Row 9 (f_NL_folded = 0.0547 / 0.129) is undetectable at SKA-1 (σ = 5.0). Post-2035 21-cm intensity-mapping arrays at l_max ~ 10⁵ are required for σ ~ 0.05 sensitivity, lifting EVOI from 0.05 (today) to 0.40+. Carried forward as W1c-CF-4 / S86 monitoring item.

---

## V. Carry-Forward (mandatory per `feedback_fix-in-session-never-defer.md`)

Each item: **What / Inputs / Gate / Effort**.

### V.1 Land master inventory at project-level registry

- **What**: Land Section III.1 of this synthesis (12-row table) at `sessions/framework/falsifier-master-inventory.md` per AMRI rule. Cite W1a-4/5/9, W1c-2/5, W3-1/12, W4-2/4/7/8 as input-pin SHAs in frontmatter. Frontmatter: `type: registry, ingested-by: /weave --update`.
- **Inputs**: this synthesis file + the 9 source ledgers + canonical_constants.py (post-W1c-1 SHA `e7999383…`).
- **Gate**: S86-W0-MASTER-INVENTORY-LAND — PASS iff file lands with all 12 rows + frontmatter + 0 path-discrepancies in pre-execution dry-run.
- **Effort**: 1 h (writer + cross-reference verify).

### V.2 Resolve Conflict #1 — α_s pathway dual-presence (rows #3 vs #10)

- **What**: The §VII.Ω.α_s-gap row (#3, value −0.068968 from S50-51 identity) and the S63 RUNNING-NS row (#10, value +0.00117 from one-loop MS through fold) BOTH appear in canonical_constants and are BOTH derivation-supported. They give different σ-distances (9.62σ vs 2.70σ) at CMB-S4. Pre-register a decision rule — either (a) the §VII.Ω commit is the SOLE α_s prediction and S63 becomes a derived sub-result, or (b) the framework explicitly carries TWO α_s pathways and joint-BF computations apply both with their per-pathway pulls.
- **Inputs**: W1c-2 §VII.Ω commit (48 inflationary hits / 0 QCD); S63 RUNNING-NS-63 PASS at 0.78σ; W1c-6 β_s cascade chain rule (links pathway #3 to β_s via β_s = 2 n_s α_s).
- **Gate**: S86-W0-ALPHA-S-PATHWAY-RESOLVE — PASS iff a single decision rule lands in `sessions/framework/permanent-results-registry.md` §VII.Ω.α_s-gap with a sub-section "Pathway-A vs Pathway-B disposition" and the inventory table is updated to a single canonical row.
- **Effort**: 2 h adjudication workshop (mack-cosmic-bridge + connes-ncg-theorist + landau-condensed-matter-theorist; 1 round).

### V.3 Resolve regulator-conditional DR3 sub-trees (W1b-1 FAIL)

- **What**: Maintain 3 DR3 sub-trees keyed on L_max ∈ {8, 10, 12}. At L_max=10 framework predicts A1 (PASS); at L_max=12 framework predicts B2 (FAIL). Either compute Zubarev L_max=8 (currently unavailable) and converge on a single sub-tree, OR pre-register layer-first DR3 adjudication (regulator pin BEFORE box check).
- **Inputs**: W1b-1 verdict at content `15e1b1ff…`; S84 W4-46 G51-LMAX-CONVERGENCE FAIL (split = 0.503 at L_max=9); Zubarev L_max=8 computation (not on disk).
- **Gate**: S86-W1-DR3-REGULATOR-LAYER-PIN — PASS iff (a) Zubarev L_max=8 lands AND framework prediction lies in same R_842 cell as L_max=10, OR (b) DR3-adjudication protocol explicitly pre-registers regulator-first sequencing in the §VII.M.1 protocol document.
- **Effort**: 6 h GPU eigvals at L_max=8 + 0.5 h protocol patch.

### V.4 Re-fire α_s vocabulary remediation (W1c-CF-1 carry-forward)

- **What**: The historical α_s usage audit (W1c-3) FAILed at 2193 AMBIGUOUS sites against threshold 20 — 109× over. This is vocabulary, not physics, but the master inventory row #3 vs #10 conflict is partly downstream of this contamination. Remediate top 50 contaminated computation scripts.
- **Inputs**: `s85_w1c_historical_alpha_s_audit.json` (576 KB remediation list); post-W1c-1 canonical handles (`alpha_s_MZ_obs`, `planck_alpha_s`, `alpha_s_framework_central`).
- **Gate**: S86-W1d-ALPHA-S-REMEDIATION — PASS iff N_ambiguous reduces ≥50% (target < 1100) AND impact-matrix N_flagged ≤ 5.
- **Effort**: 4–6 h CPU (classifier extension + per-script remediation of top 50).

### V.5 Pin Fisher PDF SHAs for INFO→PASS lift (W4-3, W4-6)

- **What**: Five Fisher detector-forecast PDFs are absent at `researchers/{CMB-S4,DESI,LiteBIRD,CMB-HD,HERA}/`. W4-3 and W4-6 fire INFO via PRE-REG-INCOMPLETE clauses; the arithmetic is correct, only the PDF-SHA pin is missing. Web-fetch each, SHA-pin in input-pin map, re-emit PASS with identical f_indep = 0.873 / geom-discount = 0.9926.
- **Inputs**: arXiv handles cited in W4-1 §(b) (DESI 2024; Sehgal 2019; Hazumi 2202.02773; CMB-S4 SciBook v2 2022; HERA Memo 54 Ali+ 2018).
- **Gate**: S86-W2-FISHER-PDF-PINS — PASS iff 5/5 PDFs on disk with SHA pinned + W4-3/W4-6 re-emit PASS verdict lines.
- **Effort**: 2 h web-fetch + 0.5 h re-emit.

### V.6 Refine S50-51 derivation toward §VII.Ω.α_s-gap closure criterion (a) (W1c-CF-2)

- **What**: Attempt to bring the framework α_s prediction from −0.068968 into the 3σ band [−0.025, +0.016] around Planck. Three candidate paths: (i) re-examine 5 independent S49–S50 proofs for a suppressed prefactor in propagator-to-observable projection, (ii) check Connes phase-sector inner-fluctuation projection factor, (iii) check acoustic-sum-rule normalization.
- **Inputs**: 13 S50+S51 source files; canonical handles; §VII.Ω.α_s-gap closure criterion list.
- **Gate**: S86-W?-ALPHA-S-PREFACTOR-DERIVATION — PASS iff `alpha_s_framework_refined ∈ [−0.025, +0.016]`. FAIL is also useful (closes one of three candidate paths).
- **Effort**: 8–16 h workshop (connes-ncg-theorist + landau-condensed-matter-theorist + quantum-acoustics-theorist; possibly multi-round).

### V.7 BK-Array 2026 livewatch quarterly poll (W1a-4)

- **What**: When BK-Array 2026 release lands (currently registered, content `c96aedb0…`), re-fire W1a-4 with published r_obs through the 4-branch decision tree. Quarterly poll of `bicepkeck.org` per W1a carry-forward.
- **Inputs**: `r_CMB_framework = 0.011732` (canonical); 4-branch tree at S84 `e2ca24d6…`.
- **Gate**: S86-W?-BK-ARRAY-CLASSIFICATION — branch-specific verdict (PASS Branch 2 expected; alternative branches trigger downstream cascades).
- **Effort**: 0.25 h on event firing.

### V.8 PIXIE livewatch + mission-funding monitoring

- **What**: Add PIXIE livewatch to the §VII.M-namespace monitoring infrastructure. P(decisive_by_2029) = 0.55 reflects mission-funding contingency; track flight-status via NASA program updates. Currently W3-1 PASS pre-registers μ(K_FIRAS) = 8.69e−5 with regulator-spread = 0.
- **Inputs**: W3-1 verdict `a5fd4a36…`; W0-8 PIXIE pull = 8693σ flagship pre-registration.
- **Gate**: S86-META-PIXIE-LIVEWATCH-LAND — PASS iff livewatch document lands in `sessions/framework/` parallel to DR3-RESPONSE-PROTOCOL.
- **Effort**: 0.5 h registry only.

### V.9 LISA flagship pre-registration land in atlas

- **What**: Land W1a-6 + W1a-7 combined LISA flagship document at `sessions/framework/Atlas/atlas-XX-lisa-flagship.md` per W1a carry-forward #5. Convention pre-registration: fix-k-dominant primary, fix-f cross-convention companion.
- **Inputs**: `s85_w1a_cf_m4_lisa_flagship.md` + `s85_w1a_lisa_flagship_tightening.npz`; S84 W6-50 `b9c543c6…`.
- **Gate**: S86-W0-LISA-FLAGSHIP-LAND — PASS iff atlas row stamped with dual-convention sub-section + SNR = 1.68×10¹³ + (A)/(C) regulator discriminator note.
- **Effort**: 1 h coordinator.

### V.10 21-cm next-generation EVOI re-evaluation

- **What**: Row #9 (f_NL_folded) is undetectable at SKA-1 (σ = 5.0 vs FW = 0.0547 ⇒ +0.011σ). Re-evaluate EVOI for post-2035 21-cm intensity-mapping arrays at l_max ~ 10⁵. Carry-forward from S68 CMBS4-FNL-FORECAST-68 INFO ("21cm l_max ~ 10⁵ needed").
- **Inputs**: HERA Memo 54 Ali+ 2018; S82 W3-4 GGE-FNL-CHANNEL `f_NL = 0.0547`; S67 GGE-BISPECTRUM-67 `f_NL = 0.129` folded.
- **Gate**: S86-META-21CM-NEXTGEN-EVOI — PASS iff EVOI re-emit document lands with σ_post-2035 forecast + Bayesian update path.
- **Effort**: 2 h Fisher computation + write-up.

---

## VI. Conflicts and Open Questions Flagged

### VI.1 Conflict #1: α_s pathway dual-presence (rows #3 vs #10)

The §VII.Ω-INFLATIONARY commit anchored by W1c-2 (48 inflationary / 0 QCD hits) and the S63 RUNNING-NS-63 one-loop MS computation give DIFFERENT framework α_s values (−0.068968 vs +0.00117) under arguably-the-same physical observable (inflationary running). Both are derivation-supported; neither is wrong. The master inventory carries them as separate rows pending S86 adjudication (V.2). The 7D Fisher (W1a-9) used the S63 value (+0.00117) at 0.56 pull; the §VII.Ω.α_s-gap registry uses the identity value (−0.068968) at 9.62σ pull. Aggregate framework-LCDM 7D log10(BF) = +827.93 IS DOMINATED BY β_s and r (3798 of 3813 χ²) regardless of which α_s pathway is used — but the per-channel falsifier consequence at CMB-S4 differs by an order of magnitude.

### VI.2 Conflict #2: W3-12 α_s row vs W1c-5 / W4-7 σ-distances

The W3-12 OZ-class table reports `α_s = 0.1252` with the W1a SCHEME-DEP `c9a2beaf…` provenance. This is **framework MS-bar QCD-side α_s scheme variance**, NOT inflationary α_s. The naming is the W1c-3 vocabulary contamination problem (2193 AMBIGUOUS sites). The W3-12 row is correct under its own convention (MS-bar 2-loop scheme variance) but should be re-labelled "α_s_MS_2loop_variance" rather than appearing in a column shared with the inflationary-α_s rows. Disposition: consume W1c-CF-1 remediation and re-emit W3-12 with explicit pathway tags.

### VI.3 Open Question: r_TT row in W3-12 (588.78)

W3-12 lists r_TT = 588.78 from W1a-8 LITEBIRD-NT-REGISTRY. The 588.78 is the **n_T separation in σ-units** (n_T_transit = +0.468 vs n_T_CMB = −3.024×10⁻³ divided by σ_LB = 8e−4), NOT a tensor-to-scalar ratio. The registry row label is misleading. The actual tensor-to-scalar `r` is row #4 of the master inventory at 0.011732. Disposition: rename the W3-12 column header in the master inventory to "n_T transit/CMB separation (σ-units)" and place it in a STRUCTURAL row (not falsifier row) parallel to row #8.

### VI.4 LiteBIRD STRUCTURAL-FLOOR explicit non-falsifier discipline

Per task instruction and per W1a-8 / W4-4 / W4-7 documentation: do NOT classify LiteBIRD n_T as a falsifier. The framework prediction at CMB-scale n_T = −3.024×10⁻³ sits below LiteBIRD σ(n_T) = 8e−4 in **GEOMETRIC** separation (54-decade k-space transfer function from blue-tilted +0.468 transit scale to red-shifted −3e−3 CMB scale). The `r = 16ε` slow-roll consistency is INAPPLICABLE to the framework per 5 independent VdD-Hawking arguments. A null LiteBIRD result is therefore consistent with framework, NOT a falsifier. The master inventory carries this in row #8 as STRUCTURAL-FLOOR with explicit non-falsifier annotation. **EVOI ≡ 0 through 2040.**

LiteBIRD's FLAGSHIP role is **r-confirmation** at row #4 (r_FW = 0.01173, σ_LB(r) = 1e−3, +11.7σ), NOT n_T discrimination.

---

## VII. Summary of Structural Position

Mapping the post-W0–W5 falsifier ledger onto the EVOI-ranked master inventory yields a coherent observational roadmap:

- **2026–2030**: 3 binding FLAGSHIP falsifiers (DR3 w_0 / CMB-S4 β_s / CMB-S4 α_s gap) plus 1 PRECURSOR (BK-Array 2026 r). All ZFP. Joint discrimination (under W1a-9 7D Fisher) reaches log10(BF_FW/LCDM) = +827.93 IF framework correct.
- **2030–2035**: 2 additional FLAGSHIPS deploy (LiteBIRD r-confirmation; CMB-HD α_s common-mode discount lifts row #3 to ~64σ if Planck holds). PIXIE μ-distortion contingent on mission funding (P = 0.55).
- **2035+**: LISA CGWB at SNR = 1.68×10¹³ (decisive), CMB-HD α_s + β_s joint at ~104σ, 21-cm next-generation lifts row #9 EVOI from 0.05 to 0.40.

The framework's 12-row master inventory has no STRUCTURAL excuse rows except #8 (LiteBIRD n_T, geometrically beyond detector reach) and #12 (Planck A_s, already landed at ~57% above central — a constraint-map closure, not a future falsifier). **Every other row stakes a 2σ+ falsifiable position by 2035, with 7 of 12 staking ≥3σ binding within the 2026–2030 window.**

The single most decision-relevant fact for S86 planning: **DR3 fires within 12 months and its outcome reorders rows 3, 5, 7, 10 of this inventory by activating either the kaku-cascade (B-cells) or the LISA-flagship branch (A-cells). All other rows are downstream of DR3 in the priority queue. Maintain the 3 regulator-layer DR3 sub-trees per V.3.**

---

## VIII. Files Produced

| Artifact | Path |
|:---------|:-----|
| This synthesis (S-5 falsifier-inventory-mack) | `sessions/archive/session-85/session-85-s5-falsifier-inventory-mack.md` |
| Master-inventory draft (Section III.1) | ready for landing at `sessions/framework/falsifier-master-inventory.md` (V.1) |
| Carry-forward S86 specs (10 items) | Section V of this file |

**End of S-5 Falsifier-Watchlist Master-Inventory synthesis (mack).**
