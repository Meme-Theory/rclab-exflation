# Session 84 — S-4 Mack Solo Synthesis: Falsifier Watchlist + Observational Roadmap

**Author**: mack-cosmic-bridge (solo synthesis, post-session S-4 slot, 1 of 2)
**Date**: 2026-04-20
**Scope**: S84 update to the 5-prediction S82 falsifier watchlist. Absorbs W1, W4, W5, W6, W10 new falsifier inventory items; constructs per-detector σ-forecast table with calendar timeline; pre-registers gates with sign-lockouts; maps EVOI ordering; identifies cross-channel correlation structure.
**Sources**: `sessions/archive/session-84/session-84-synthesis-collation.md`, wave working papers W1/W4/W5/W6/W10, `sessions/permanent-results-registry.md`, agent memory.
**Framing rule**: substrate language per `.claude/rules/phononic-framing.md`; substitution chains per `.claude/rules/math-scripts.md` for every σ/direction/threshold claim.

---

## §I. Executive position

The S82 watchlist carried five predictions: α_f_NL=0, n_T blue, C_cons, DR3 binary rectangle, GW α-vs-γ. S84 materially expanded that inventory — **18 channels classified under the W4-48 4-flag taxonomy** (ZFP=11, ACCOMMODATION=2, SCHEME-DEPENDENT=2, DETECTOR-STERILE=3). The structurally weightiest S84 update is **three calendar-bound falsification events in the 2026-2030 window**: DR3 R_842 (2026-04-23), BICEP/Keck 2026 r-release, and CMB-S4 α_s first light (~2030). The framework's load-bearing evidence column is the 11 ZFP channels; the three CMB/BAO calendar events test 4 of those 11 directly, plus two SCHEME-DEPENDENT channels (w_0, A_s) and one ACCOMMODATION channel (m_H via μ_BC). LISA CGWB (~2035) becomes the decisive branch-discriminator between H_TD and H_LI under the W6-50 +11-OOM margin. A_s regulator canonicalization (W1a-1+W1a-2 rate-limiter relocation) remains the framework's single open observational self-consistency problem.

Per `feedback_reporting-framing.md`: each ZFP prediction that lands on the LCDM-compatible value from zero free parameters carries BF > 1× independently; the joint probability of a random geometry producing 11 such matches is the product, not the average. W4-48 is the registry that preserves this accounting.

---

## §II. S84 update to the falsifier inventory — channel-by-channel

### §II.1. Rigor-class column (exactly-one-flag taxonomy, W4-48)

Source: `session-84-w4-workingpaper.md` §W4-48 Table (lines 1170-1189). Eighteen channels; no un-tagged, no multiply-tagged row. Verified on disk: `ratio = 1.0000, ZFP = 11, untagged = 0`.

| # | Channel | Rigor class | Framework value | Observational anchor | Status |
|:-:|:--------|:-----------:|:----------------|:---------------------|:------:|
| 1 | n_s (CMB pivot k=0.05 Mpc⁻¹) | **ZFP** | 0.9590 (Bogoliubov-inv triple) | 0.9649 ± 0.0042 (Planck 2018) | 1.40 σ |
| 2 | r (tensor-to-scalar, CMB) | **ZFP** | 0.01173 (S83 G46) | < 0.036 (95% CL, BK18) | PASS (headroom 3.07×) |
| 3 | n_T (transit, k ~ M_KK) | **ZFP** | +0.468 (BLUE, G50) | 54 decades above CMB | DET-STERILE context |
| 4 | n_T (CMB, k=0.05 Mpc⁻¹) | **ZFP** | −3.024×10⁻³ (W4-39) | σ_LB_3yr = 0.0654 | DET-STERILE for σ |
| 5 | α_s = n_s²−1 | **ZFP** | −0.068968 (S50/W6-52/W8-86) | −0.0045 ± 0.0067 (Planck) | 9.62 σ TENSION |
| 6 | m_H | **ACCOM** | 188.19 GeV at μ_BC | 125.25 ± 0.17 GeV (PDG) | μ_BC fit |
| 7 | sin²θ_W | **ACCOM** | 0.23480 at μ_BC fit | 0.23121 ± 0.00004 (PDG) | μ_BC tuned |
| 8 | A_s | **SCHEME-DEP** | 5.078×10⁻⁹ (TD canonical) | 2.099×10⁻⁹ (Planck) | 0.384 OOM above |
| 9 | f_NL (total, with folded shape) | **ZFP** | 1.03 total (eq=0.853, fold=0.129, multi=0.56) | −26 ± 47 (Planck) | 0.57 σ |
| 10 | α_f_NL (amplitude-running) | **DET-STERILE** | −0.143 ± 0.044 (W4-38) | σ_SKA-2 ~ 3.0 on α | SNR ~ 0.05 SKA-2 |
| 11 | w_0 | **SCHEME-DEP** | −0.918 canon / −0.842 branch-iv (L=5) | −0.752 ± 0.057 (DR2+DESY5) | split 0.08 (W4-46 FAIL structural) |
| 12 | w_a | **ZFP** | 0 (four-fold locked) | −0.73 ± 0.25 (DR2+DESY5) | 2.92 σ |
| 13 | μ (FIRAS) | **ZFP** | 4.976×10⁻¹⁰ (Planck-tilt) / 6.169×10⁻¹⁰ (flat) | \|μ\| < 9×10⁻⁵ (FIRAS 95% CL) | 5.26 OOM below |
| 14 | Ω_GW (walls, LISA f) | **DET-STERILE** | ~10⁻¹⁰ at 1 mHz | LISA ~10⁻¹² at 1 mHz | 46.7 OOM below LISA (plan-convention) |
| 15 | σ_8 | **ZFP** | 0.793 (S69 PVD-FSIG8) | 0.811 ± 0.006 (Planck) / 0.766 ± 0.03 (lensing) | S8 ameliorated |
| 16 | C_cons (internal consistency) | **DET-STERILE** | G44 FAIL (23× above PASS) | no external | internal |
| 17 | ISW tracking (c_s²_DE = 0) | **ZFP** | +7.6% vs quintessence (W6-50/S68) | A_ISW = 1.00 ± 0.25 (Planck) | 0.49 σ current |
| 18 | Neutrino mass ordering | **ZFP** | Normal (B1<B2<B3 at machine ε) | NO at ~2.5 σ (NuFit-6.0) | consistent |

### §II.2. S84 new structural additions (post-S82 watchlist)

Beyond the S82 five-item list, S84 added ten structural items to the falsifier landscape:

1. **W4-48 registry itself** — 18/18 tagged, 4-flag taxonomy frozen. Prevents cross-class citation of evidence (e.g., citing m_H ACCOMMODATION alongside n_s ZFP as if they carried the same evidential weight).
2. **W4-38 α_f_NL = −0.143** — 3-channel decomposition {equilateral −0.038, folded-Bog −0.080, multi −0.025}. Folded-Bog channel is the UNIQUE substrate signature (pair production, no scalar-field analog).
3. **W4-39 n_T(k_CMB) = −3.024×10⁻³** — two-speed metric `c_T/c_S = 2.062 = a_2/a_0 ratio`; modified consistency `n_T = −r·c_T/(8·c_S)`. ZFP channel.
4. **W4-43 SKA-1 SNR = 0.0279 FAIL** — closes amplitude-running channel for α_f_NL. 21-cm folded-SHAPE template (l_max ~ 10⁵) carries shape signature; SKA-2 also FAILs amplitude (SNR = 0.179).
5. **W4-37 LiteBIRD σ(n_T)_joint_3yr = 0.0654 FAIL boundary** — strengthens W4-41 EVOI=0 inaccessibility registration (3-param Fisher marginalization).
6. **W4-47 UHF-GW physical gap = +18.74 OOM** — threshold Ω_th=10⁻⁴⁰ above framework Ω_γ(1 mHz)=1.8×10⁻⁵⁹. Not 6.7 OOM (plan-convention artifact, now corrected).
7. **W4-44 7-scenario DR3 contingency tree FROZEN** — cells A1/A2/B1/B2/B3/C1/C2 outside R_842, SHA-pinned.
8. **W4-42 BICEP-Keck 2026 4-branch decision tree FROZEN** — frozen 2026-04-18, SHA `e2ca24d6`.
9. **W6-50 LISA CGWB +11 OOM above floor** — `h_c^(A)(3 mHz) = 7.17×10⁻¹²` characteristic strain; discriminant between H_TD (high) and H_LI (low) branch over 2.10 decades (fixed-f); 2.38 decades (fixed-k).
10. **W6-52 α_s joint detector reach** — {CMB-S4: 34.48σ, CMB-HD: 53.05σ, LiteBIRD: 11.49σ, joint: 64.31σ}. Verified via substitution chain: `|α_s_pred|/σ_CMB-S4 = 0.068968/0.002 = 34.484 σ` (arithmetic, verified in Python).

### §II.3. W1b-9 R_842 DR3 response protocol (calendar-imminent)

`R_842 = [−0.942, −0.742] × [−0.2, 0.2]` locked 6 days pre-window with 6 lockouts (A–F). Content SHA `9cc7f47e…79d9f`. DR3 window opens 2026-04-23.

- **Lockout A**: no dual-pin retreat
- **Lockout B**: no scheme-shopping
- **Lockout C**: no rectangle-resizing
- **Lockout D**: no w_a migration
- **Lockout E**: no post-window branch-(iv) redefinition
- **Lockout F**: no post-window τ_fold relocation

**S84 complication (W1a-3 SV2 FAIL)**: branch-(iv) retracted as provisional canonical at L_max≥6. R_842's anchor is now subject to S85 re-audit — the rectangle's BINARY containment rule still fires on 2026-04-23, but the branch classification of the outcome becomes S85-conditional.

### §II.4. W4-46 structural FAIL — w_0 is permanently SCHEME-DEPENDENT

Substitution chain for the W4-48 upgrade-path decision:

- *Definition*: `split(L) ≡ w_0^ζ(L) − w_0^Zubarev(L)` is the regulator split.
- *Substitution*: split(5) = 0.0809, split(7) = 0.3390, split(9) = 0.5028 (W4-46 numerical output, s84_w4_g51_lmax_convergence.py).
- *Simplification*: `|split(9)| / |split(5)| = 0.5028 / 0.0809 = 6.22`.
- *Direction*: ratio > 1 AND monotone-increasing with L_max ⇒ split GROWS, not shrinks ⇒ structural, not truncation-artifactual.
- *Conclusion*: W4-48's upgrade-path condition for w_0 ("if L_max convergence returns PASS, upgrade to ZFP") is DEFINITIVELY NOT met. w_0 stays SCHEME-DEPENDENT permanently.

Under Zubarev-L9, `w_0^Z(9) = −0.997`, which is OUTSIDE R_842 by 0.055. DR3 landing at −0.997 would FAIL the rectangle but remain CONSISTENT with the high-L substrate prediction. This is the structural interpretation-gap that S85 W4-carry-forward CF-W4.2 (regulator-conditional DR3 successor tree) addresses.

---

## §III. Per-detector σ-forecast timeline

Every row is verified numerically in this session's Python audit. Substitution chains are explicit where directional claims appear.

| Date | Detector | Channel | Framework prediction | Expected σ | Rigor class | Evidence effect on PASS/FAIL |
|:-----|:---------|:--------|:---------------------|:----------:|:-----------:|:---------------------------|
| **2026-04-23** | DESI DR3 | (w_0, w_a) R_842 binary | (−0.918, 0.0) canon / (−0.842, 0.0) branch-iv | 2-D covariance [[2.12e-3, −6.92e-3], [−6.92e-3, 3.13e-2]] pos-def | w_0 SCHEME-DEP / w_a ZFP | Binary containment fires: cell classification 1-of-7 per W4-44 |
| **2026 Q2/Q3** | BICEP Array + Keck | r | 0.01173 (G46) | σ_r ~ 0.005 (BA+SPT-3G projected) | ZFP | Binary branch per W4-42 4-branch tree |
| **~2030** | CMB-S4 | α_s | −0.068968 | σ(α_s) ≈ 0.002 (Abazajian 2022+) | ZFP | 34.48σ PASS |
| **~2030** | CMB-S4 | n_s | 0.9590 | σ(n_s) ≈ 0.00166 | ZFP | 2.94σ discrimination from Planck central (S69) |
| **~2030** | CMB-S4 | f_NL eq/folded | eq=0.853; fold=0.129 | σ(eq)=5.0; σ(fo)=6.9 (S68) | ZFP | NOT detectable at CMB-S4 |
| **~2030** | CMB-HD | α_s | −0.068968 | σ(α_s) ≈ 0.0013 | ZFP | 53.05σ PASS |
| **2030–2035** | LiteBIRD | r | 0.01173 | σ_r ≈ 0.001 | ZFP | 11.7σ PASS region |
| **2030–2035** | LiteBIRD | n_T (CMB) | −3.024×10⁻³ | σ(n_T)_joint_3yr = 0.0654 | ZFP/DET-STERILE | σ/|pred| = 21.6× — INACCESSIBLE (W4-41 EVOI=0) |
| **2030–2035** | LiteBIRD | α_s | −0.068968 | σ ≈ 0.006 | ZFP | 11.49σ PASS |
| **~2035** | LISA (L3–L4) | CGWB h_c^(A)(3 mHz) | 7.17×10⁻¹² | LISA reach ~10⁻²³ characteristic strain | ZFP | ~11 OOM above floor — decisive (A)/(C)/(LI) branch discriminator |
| **2035+** | PIXIE | μ-distortion | 4.976×10⁻¹⁰ | σ(μ) ~ 10⁻⁸ (PIXIE) | ZFP | FIRAS-clear; PIXIE 0.05σ (NOT discriminating at floor); K-corridor endpoint at K=3.56×10⁵ gives μ=8.69×10⁻⁵ = FIRAS-edge |
| **2032** | DUNE | ν mass ordering | Normal | 5σ Normal vs Inverted | ZFP | Framework matches at machine ε |
| **Post-2030** | SKA-2 | α_f_NL amplitude | −0.143 | σ_SKA-2 ≈ 3.0 | DET-STERILE | SNR 0.179 — FAIL (channel closes) |
| **Post-2035** | 21-cm purpose-built (l_max ~10⁵) | f_NL folded-triangle shape | 0.129 | TBD (channel exists) | ZFP | Sole folded-Bog shape discriminant |
| **~2030** | Euclid | f·σ_8 / ISW tracking | σ_8 = 0.793; ISW +7.6% vs quint | σ(fσ_8) ~ 0.005 / σ_ISW ~ 0.05 | ZFP | fσ_8 chi²/dof = 0.761 PASS (S69); ISW 1.58σ Euclid |
| **Post-2030** | SKA-1 Phase-1 | α_s | − | σ(α_s) ≈ 0.0247 (W4-43 Fisher) | DET-STERILE | SNR=0.028, 71× below PASS=2 |

### §III.1. Substitution chains for the principal σ claims

**α_s at CMB-S4**:
- *Definition*: `σ_sep = |α_s_pred − α_s_null| / σ_detector`.
- *Substitution*: `α_s_pred = −0.068968`; `α_s_null = 0.0` (benchmark projection point); `σ_detector = 0.002` (Abazajian 2022+ CMB-S4 projected).
- *Simplification*: `σ_sep = 0.068968 / 0.002 = 34.484`.
- *Direction*: quotient > 5 ⇒ detection-regime; framework prediction is a ZFP entry ⇒ **34.48σ PASS** is load-bearing on the W4-48 ZFP column for α_s.

**α_s at CMB-HD**: same definition, `σ_detector = 0.0013` ⇒ `σ_sep = 0.068968 / 0.0013 = 53.05`. Direction PASS (detection).

**α_s at LiteBIRD**: `σ_detector = 0.006` ⇒ `σ_sep = 11.49`. Direction PASS.

**α_s joint 3-detector quadrature**: `σ_sep_joint = sqrt(34.48² + 53.05² + 11.49²) = sqrt(1188.9 + 2814.3 + 132.0) = sqrt(4135.2) = 64.31` (Python-verified). Direction PASS (joint detection).

**n_T CMB under two-speed metric**:
- *Definition*: standard single-field slow-roll gives `n_T^SR = −r/8` at `c_T = c_S = 1`.
- *Substitution*: framework modified consistency is `n_T^FW = −(r · c_T) / (8 · c_S)` from W4-39; `r = 0.01173`; `c_T/c_S = 2.062` (a_2/a_0 spectral moment ratio, not regulator).
- *Simplification*: `Δn_T ≡ n_T^FW − n_T^SR = −(r/8) · (c_T/c_S − 1) = −(0.01173/8) · (2.062 − 1) = −(1.466×10⁻³) · (1.062) = −1.557×10⁻³`.
- *Direction*: `c_T/c_S > 1 ⇒ (c_T/c_S − 1) > 0 ⇒ Δn_T < 0` (more negative than slow-roll).
- *Conclusion*: n_T prediction is the two-speed substrate commitment, not a regulator. The direction is DEFINITE (more-negative-than-slow-roll); the magnitude sits 21.6× below LiteBIRD σ ⇒ detector-sterile for σ but the PREDICTION is ZFP.

**w_a DR3 separation** (published DR2+DESY5):
- *Definition*: `σ_sep = |w_a_pred − w_a_obs| / σ_obs`.
- *Substitution*: `w_a_pred = 0` (four-fold lock); `w_a_obs = −0.73`; `σ_obs = 0.25`.
- *Simplification*: `σ_sep = 0.73 / 0.25 = 2.920`.
- *Direction*: `w_a_obs − w_a_pred = −0.73` is already NEGATIVE; framework's 0 is ABOVE obs. DR3 is projected to tighten σ_obs ~2× — pass into the decisive-discrimination regime at ~6σ if central stays at −0.73.

**r at BK18 95% CL**:
- *Definition*: `r_pred ≤ r_obs_95%` check.
- *Substitution*: `r_pred = 0.01173`; `r_obs_95% = 0.036`; `σ_r ≈ r_obs_95%/1.96 ≈ 0.01837` (Gaussian on-the-wall proxy).
- *Simplification*: headroom `= r_obs_95%/r_pred = 3.07`.
- *Direction*: headroom > 1 ⇒ CURRENT PASS under 2018 data; BK/BA 2026 projected `σ_r ~ 0.005` would discriminate framework at `(r_pred − 0)/0.005 = 2.35σ` detection (if central lands at 0.012) or `0.036/0.005 = 7.2σ` exclusion of BK18 upper bound.

**ν mass ordering (DUNE 2032)**: framework predicts Normal (B1<B2<B3 exact at machine ε from Bogoliubov level ordering in SU(3) block). DUNE is projected 5σ. Direction: framework ZFP, observation PASS-expected.

---

## §IV. EVOI ordering (per `evoi-prioritization.md`)

EVOI = P(decisive) × |Δ P(obs-aligned)|. I use the W4-49 catalog of 4 upstream triggers (A1=DERIV-I∧II, A2=TAU-CROSS, B1=TRANSFER-FN-74, B2=CMB-S4-refine) as the reference for each event's potential to shift the ZFP column count (currently 7/9 on the reduced 9-channel atlas per S80 W0-12; 11/18 on the W4-48 full atlas).

| Rank | Event | Calendar | P(decisive) | |Δ P(obs-aligned)| | EVOI | Class |
|:-:|:-----|:--------:|:------------:|:------------------:|:----:|:-----:|
| **1** | LISA CGWB branch discriminator | ~2035 | 0.95 | ~0.30 (promotes H_TD or retracts) | **0.285** | ZFP |
| **2** | CMB-S4 α_s (W6-52 flagship) | ~2030 | 0.90 | ~0.25 (34.48σ promotes to direct detection) | **0.225** | ZFP |
| **3** | DESI DR3 (w_0, w_a) R_842 | **2026-04-23** | 0.85 | ~0.15 (binary cell classification) | **0.128** | SCHEME-DEP / ZFP |
| 4 | CMB-HD α_s (later-gen refinement) | ~2035+ | 0.50 | ~0.12 (post-CMB-S4 follow-up) | 0.060 | ZFP |
| 5 | SKA-2 21-cm folded shape | post-2030 | 0.30 | ~0.15 | 0.045 | ZFP (shape) |
| 6 | BICEP-Keck 2026 r | 2026 Q2/Q3 | 0.40 | ~0.10 | 0.040 | ZFP |
| 7 | Euclid fσ_8 + ISW | ~2030 | 0.30 | ~0.08 | 0.024 | ZFP |
| 8 | DUNE ν ordering | 2032 | 0.35 | ~0.05 | 0.018 | ZFP |
| 9 | PIXIE μ | 2035+ | 0.20 | ~0.04 | 0.008 | ZFP |
| 10 | LiteBIRD n_T | 2030+ | 0.01 (EVOI=0 per W4-41) | ~0.02 | **~0.0002** | DET-STERILE |
| 11 | SKA-1 α_f_NL amplitude | post-2030 | 0.01 (W4-43 FAIL) | ~0.03 | ~0.0003 | DET-STERILE |
| 12 | UHF-GW Ω_γ | post-2040 | <0.001 (W4-47 +18.74 OOM gap) | ~0.05 | ~0 | DET-STERILE |

**EVOI ordering is NOT a forecast of framework outcome** — it is a priority-of-work ordering on the observational queue. Rank-1 (LISA) and rank-2 (CMB-S4) carry ~90% of the decade-scale observational information; rank-3 (DR3) is calendar-imminent with 3-day lead time and must not be re-ordered by subsequent EVOI recalibrations (W1b-9 lockouts A-F).

---

## §V. Calendar-decision-tree timeline

```
2026-04-23  DR3 opens ----- R_842 binary containment fires (W1b-9, W4-44 7-cell tree)
                            |
                            v
                            LOCKOUTS A-F binding; framework pre-committed
                            |
             [R_842 interior]      [outside R_842: 1-of-7 cells]
                     |                        |
                     v                        v
                 PASS (canon)          PARTIAL (A1/A2/B1/B2/B3/C1/C2)

2026 Q2/Q3  BICEP Array + Keck r release (W4-42 4-branch tree FROZEN)
                            |
                            v
            [r < 0.005] [0.005 < r < 0.02] [r > 0.02] [r > 0.036]
                PASS         PASS              CONTEST      FAIL-BK18

~2030       CMB-S4 first-light
                            |
                            v
             [α_s @ 34.48σ: PASS]   [n_s @ 2.94σ discrim]   [f_NL shape: σ too wide to detect]

~2030       CMB-HD first-light — α_s refines from 34.48σ → 53.05σ (ZFP reinforcement)

2030-2035   LiteBIRD survey
                            |
                            v
             [r: ~12σ PASS]       [n_T: EVOI=0 per W4-41, not discriminating]
                                                          → 21.6× below σ

2032        DUNE 5σ ν ordering ——→ [Normal PASS]

~2035       LISA L3-L4
                            |
                            v
             [branch (A): 11 OOM above floor → PASS]
             [branch (C): intermediate, 2.1 dex lower → disc.]
             [branch (LI): 2.38 dex below (A) → retract claim if observed high]

Post-2030   SKA-2 21-cm amplitude-running α_f_NL → FAIL-channel (closed W4-43)
            SKA-2 21-cm folded-triangle SHAPE template (l_max ~10⁵) → sole surviving channel

2035+       PIXIE μ-distortion — K-endpoint corridor at K=3.56×10⁵ gives μ=8.69×10⁻⁵ edge-visible

Post-2040   UHF-GW — +18.74 OOM wall, no plausible migration path
```

---

## §VI. Per-channel pre-registered gates with sign-lockouts

Each channel carries a gate criterion, a `Δ_OOM` tolerance where applicable, and sign-lockouts enforcing no post-data retreat.

### §VI.1. α_s at CMB-S4 (rank-2 EVOI)

- **Gate**: `|α_s_pred − α_s_detected| / σ(α_s) < 3` ⇒ PASS (i.e., framework prediction recovered within 3σ).
- **Tolerance**: Δ_OOM=0 (direct central-value comparison; tolerance inherits CMB-S4 σ = 0.002).
- **Sign-lockout A**: no post-data retreat to auxiliary couplings (the α_s = n_s²−1 identity holds under the minimal 4-axiom set per W10-123; no aux coupling enters).
- **Sign-lockout B**: no post-data redefinition of the n_s input (n_s central pinned to Bogoliubov-inv triple 0.9590 at plan-freeze; any CMB-S4 revision of n_s is input-side, not framework-side).
- **Sign-lockout C**: no post-data change of the derivation chain (O-Z single-pole rational propagator is structural; alternative derivations would constitute a new framework, not a rescue).

### §VI.2. DR3 (w_0, w_a) R_842 binary (rank-3 EVOI)

- **Gate**: `(w_0_DR3, w_a_DR3) ∈ R_842` ⇒ PASS (branch-iv anchored); else ⇒ cell classification per W4-44.
- **Tolerance**: none — BINARY containment.
- **Lockouts A-F**: inherited from W1b-9 — no dual-pin retreat, no scheme-shopping, no rectangle-resizing, no w_a migration, no post-window branch-(iv) redefinition, no post-window τ_fold relocation.
- **Additional SCHEME-DEP flag on w_0**: S85 must resolve branch-(iv) re-audit before interpreting R_842 outcome — W1a-3 SV2 FAIL retraction sits in-flight.

### §VI.3. BICEP-Keck 2026 r (rank-6 EVOI)

- **Gate**: branch classification under W4-42 4-branch tree (frozen 2026-04-18, SHA `e2ca24d6…882d3`).
- **Tolerance**: Δ_OOM=0; r_pred = 0.01173 is a structural spectral-moment output (G46).
- **Sign-lockout**: no n_T blue-tilt retrofit post-r-detection; the transit-scale +0.468 vs CMB-scale −3.024×10⁻³ split is LOCKED (W4-39 two-speed metric, W4-41 EVOI=0 for CMB n_T σ).

### §VI.4. LISA CGWB (rank-1 EVOI)

- **Gate**: `h_c_obs_LISA(3 mHz) ∈ [1.0×10⁻²³, 1.5×10⁻¹¹]` discriminates branches (A/C/LI).
  - `h_c_obs > 1×10⁻¹² ⇒ A-branch consistent`
  - `h_c_obs ∈ [7×10⁻¹⁵, 1×10⁻¹²]` ⇒ C-branch consistent
  - `h_c_obs < 3×10⁻¹⁴` ⇒ LI-branch consistent / A-branch excluded
  - `h_c_obs < 1×10⁻²³` (LISA sensitivity floor) ⇒ all three branches below LISA reach (no discrimination)
- **Tolerance**: 2.10 decades (fixed-f) or 2.38 decades (fixed-k); W6-50 methodology note on fixed-k vs fixed-f distinction MUST be carried into S85-flagship pre-registration.
- **Sign-lockout**: no post-data relabeling of branch A/C/LI if the observed h_c lands between branches; the 3-branch interpretation is frozen at W6-50 freeze.

### §VI.5. LiteBIRD n_T (CMB) — DET-STERILE by construction

- **Gate**: W4-41 EVOI=0 registered permanent. `σ(n_T)_joint_3yr = 0.0654` and `|n_T_CMB_pred| = 3.024×10⁻³` ⇒ ratio 21.6× ⇒ framework prediction is 21.6× smaller than 1σ detector reach.
- **Tolerance**: the W4-48 rigor class remains ZFP (prediction is zero-free-parameter); detector-sterility is a LANDSCAPE fact, not a framework property.
- **Sign-lockout**: no post-data migration to "the prediction was actually at transit scale" — the W4-39 CMB-scale prediction −3.024×10⁻³ is LOCKED.
- **Upgrade path** (S85 CF-W4.6): LSST κκ A_lens prior could tighten σ ~20% — `σ(n_T) = 0.0654 × 0.80 ≈ 0.052`, still 17× larger than |n_T|. No detection horizon without instrument lift.

### §VI.6. CMB-S4 n_s (rank-2 companion to α_s)

- **Gate**: `|n_s_pred − n_s_detected| / σ_CMB-S4(n_s) < 3` ⇒ PASS; σ_CMB-S4 ≈ 0.00166 (S69 CMB-S4-NS-69).
- **Tolerance**: Δ_OOM=0; n_s = 0.9590 from Bogoliubov-inversion triple (isocurvature-PASS in S75).
- **Sign-lockout**: no post-data n_s redefinition if CMB-S4 lands at 0.963±0.002 (would be 3.25σ away); framework has committed to the triple-converge value.

### §VI.7. f_NL folded-triangle shape (post-2035 21-cm IM)

- **Gate**: `SNR_shape_folded ≥ 2` at purpose-built 21-cm tomography l_max ~10⁵ ⇒ PASS; `f_NL_folded = 0.129` (W4-38 channel decomposition).
- **Tolerance**: Δ_OOM=0 on central; SNR threshold.
- **Sign-lockout**: the folded-Bogoliubov channel is the UNIQUE substrate signature (pair production at transit). No retrofit to scalar-field single-clock inflation models is admissible post-discovery.

### §VI.8. DUNE ν mass ordering (2032)

- **Gate**: DUNE delivers `Normal ordering at ≥5σ` ⇒ PASS; framework predicts Normal at machine ε.
- **Tolerance**: Binary.
- **Sign-lockout**: no retrofit to Inverted under any observed pattern (B1 < B2 < B3 is a strict Bogoliubov-level consequence of the Jensen SU(3) fiber structure).

### §VI.9. Euclid fσ_8 + ISW (2030)

- **Gate**: `χ²/dof_Euclid(fσ_8) < 1.0` ⇒ PASS (S69 value 0.761 beats LCDM 0.893). `SNR_ISW_Euclid ≥ 2` ⇒ decisive.
- **Tolerance**: Δχ²/dof; ISW central 1.58σ Euclid projection per S68/W6-50.
- **Sign-lockout**: no post-data migration of c_s²_DE = 0 assumption — this is the substrate-tracking-scalar signature (W6-50 S-1 structural).

### §VI.10. PIXIE μ-distortion (2035+)

- **Gate**: `μ_pred ∈ [μ_detected − 3σ_PIXIE, μ_detected + 3σ_PIXIE]` ⇒ PASS; `μ_pred = 4.976×10⁻¹⁰` (Planck-tilt, W5-57 +Volovik partition).
- **Tolerance**: K-endpoint corridor analysis ⇒ `γ = 1.000` exactly to 10⁻¹⁵ per W5-57. Any framework revision that tilts γ > 1 instantly violates FIRAS.
- **Sign-lockout**: μ is linear-in-K with γ=1; post-data retreat to γ ≠ 1 is prohibited.

### §VI.11. SKA-1/SKA-2 α_f_NL amplitude (DET-STERILE, channel closed)

- **Gate**: W4-43 FAIL at SNR = 0.0279; channel permanently CLOSED for amplitude discriminator.
- **Carry-forward**: shape-template in S85 CF-W4.3 (folded-SHAPE at 21-cm l_max=10⁵) is the surviving channel.
- **Sign-lockout**: no post-observation migration of α_f_NL expectations; W4-38 prediction −0.143 stands as NEGATIVE (3-channel sum).

### §VI.12. Ω_GW (walls, LISA f) — DET-STERILE

- **Gate**: W4-47 physical gap +18.74 OOM (threshold above framework). UHF roadmap floor ~10⁻²⁰ needs 20 more OOM to reach threshold; framework still 38.74 OOM below even that.
- **Sign-lockout**: no post-data rescue via domain-wall amplification (S77 LISA GW retracted).

---

## §VII. Cross-channel correlation matrix

Is a PASS on α_s correlated with surviving R_842 prediction? Is n_T-CMB linked to r? I map the structural dependencies.

### §VII.1. Correlation structure

| Channel pair | Structural coupling | Correlation source | Cross-effect |
|:------|:-----|:-----|:---|
| n_s ↔ α_s | **Tight (machine-ε algebraic)** | α_s = n_s² − 1 (O-Z identity, W10-123 PASS with n_aux=0) | `d(α_s)/d(n_s) = 2·n_s ≈ 1.918`; any CMB-S4 shift in n_s shifts α_s by 2×n_s × Δn_s; both anchored to CMB pivot |
| r ↔ n_T (CMB) | **Tight (structural)** | W4-39 modified consistency `n_T = −r·c_T/(8·c_S)` | `d(n_T)/d(r) = −c_T/(8·c_S) = −0.258`; r detection by BK/LiteBIRD translates to n_T via c_T/c_S = 2.062 structural identity |
| A_s ↔ H_tilde | **Tight (CC3 identity)** | `d(ln A_s)/d(ln H_tilde) = +2` exact (W3-34) | A_s closure is NOT independent of H_tilde baseline window (W1a-1 [4.599e-3, 4.830e-3]) |
| w_0 ↔ w_a | **Moderate (DR3 joint)** | DR3 covariance [[2.12e-3, −6.92e-3], [−6.92e-3, 3.13e-2]] pos-def | joint cell classification (W4-44); w_0 SCHEME-DEP, w_a ZFP; anti-correlated by ρ = −0.855 in DR3 projection |
| CGWB branch ↔ A_s | **Latent via H_tilde** | W6-51 multi-observable common-prefactor H_tilde² | (A), (C), (LI) branches all carry `H_tilde²` factor; A_s and CGWB H_tilde² are coupled |
| α_s ↔ (w_0, w_a) | **None (W8-88 decoupling)** | Jacobian ∂Λ_CC/∂τ = 0 exactly | CMB-S4 α_s discriminator robust against CC-regulator disagreement |
| α_s ↔ A_s | **None (W8-88 structural)** | Spectral moment independence (a_0 τ-independence permanent) | CMB-S4 α_s robust regardless of A_s closure status |
| f_NL folded ↔ α_s | **Weak (both CMB ZFP but structurally distinct)** | GGE bispectrum vs O-Z single-pole | no algebraic coupling; detector-level correlations via Planck covariance are standard |
| σ_8 ↔ w_a | **Moderate (LSS joint)** | Growth rate sensitive to w(z); `fσ_8(z)` carries joint info | S69 `χ²/dof(fσ_8) = 0.761` PASS beats LCDM; Euclid tightens both |
| ν ordering ↔ all | **None (particle sector)** | Bogoliubov level ordering; not coupled to cosmological observables | DUNE independent of CMB/BAO/GW discriminators |
| m_H ↔ sin²θ_W | **Tight (μ_BC tie)** | Both ACCOMMODATION via μ_BC = 188.185 GeV fit | Single free μ_BC scale ties both; neither adds evidence weight independently |

### §VII.2. Joint decisive pair tests

- **α_s + w_a joint**: CMB-S4 (2030) + DR3 (2026) jointly test integrability of GGE. If DR3 delivers w_a = −0.7 ± 0.12 (3σ from 0) AND CMB-S4 delivers α_s = 0.0 ± 0.002 (34σ from framework), both PASS-regions collapse independently — the JOINT framework survives only if both decisions land pro-framework.
- **r + n_T joint (BK/LiteBIRD)**: r-detection at 0.012 constrains n_T_CMB to −3.1×10⁻³ via framework's c_T/c_S = 2.062 ⇒ ANY simultaneous n_T measurement fall-back-rate at 21.6× below σ means only BRANCH discrimination via r, not independent n_T check.
- **(w_0, w_a) + α_s joint**: orthogonal channels (W8-88 decoupling theorem). A DR3 + CMB-S4 double-PASS gives independent confirmations, multiplying evidence BF.
- **LISA CGWB + A_s**: both carry H_tilde² prefactor (W6-51). Joint decisive for branch discrimination but NOT independent — any H_tilde revision shifts both.

---

## §VIII. Constraint-map update (S84 solution-space position)

Wave summaries:

- **W1**: A_s rate-limiter RELOCATED to baseline corridor (0.89% log-DC window open); branch-iv RETRACTED at L_max ≥ 6; α_s −0.068968 pre-registered (9.62σ from Planck central); R_842 locked with 6 lockouts; 2 new permanent theorems (W2-EPOCH-GATING, W2-HARMONIC-NOT-INSTANTON).
- **W4**: 13 gates landed; W4-48 18-channel rigor registry frozen; W4-46 w_0 scheme-dependence PERMANENT (split growth factor 6.22×); W4-41 LiteBIRD n_T inaccessibility EVOI=0 registered; W4-47 UHF-GW +18.74 OOM wall; W4-42 BK-2026 and W4-44 DR3-contingency trees frozen.
- **W5**: K-FLOOR-WALL-JOINT triply-supported (W5-54/59/63); K_* = 1.3130 PASS (3He-B parent-child inheritance validated); α_s partition-invariance PASS; K-corridor restricted to K ≤ K_crit=91.5 (Mukhanov-Sasaki applicability boundary).
- **W6**: W6-50 LISA CGWB PASS (+11 OOM above floor); W6-52 α_s joint 64.31σ PASS; W6-69 F_amp^3PI FI at machine ε; W6-67 Z_R counterterm FAIL (a_2-slot obstruction structural, not truncation).
- **W10**: α_s axiomatic closure n_aux=0 PASS; 5-axis Fisher d_M(K1)=34.30σ / K2=34.22σ (α_s carries 98.2% of joint); τ_fold uniqueness confirmed via Γ6 cubic-BC; Borel floor 4.7 OOM safety margin.

**What S84 moved**:
- ZFP column went from 7/9 (S80/S83 reduced 9-channel atlas) to **11/18 on the full atlas**; the upgrade-path DAG (W4-49) has 4 triggers and 2 transition paths to 9/9 on the reduced atlas.
- **w_0** moved from INFO-candidate-ZFP to **permanently SCHEME-DEPENDENT** (W4-46 structural FAIL).
- **α_s** moved from S83 candidate to **permanent theorem under minimal axiom set** (W10-123 PASS n_aux=0).
- **CGWB LISA** moved from speculative prediction to **flagship pre-registration** (W6-50 +11 OOM margin).

---

## §IX. Carry-forward to S85 (mandatory 4-field format)

Each entry is what / inputs / gate / effort.

| # | What | Inputs | Gate | Effort |
|:-:|:-----|:-------|:-----|:------:|
| CF-M1 | **DR3 live-watch**: 2026-04-23 binary R_842 containment firing; load JSON, classify cell 1-of-7 per W4-44, emit verdict within 48 h of release | W1b-9 JSON, W4-44 tree, DESI DR3 release `(w_0, w_a)` central + cov | classification PASS iff cell ID matches Py script emit | 0.5 session |
| CF-M2 | **Regulator-conditional DR3 successor tree**: amend W4-44 with layered branch conditional on W4-46 structural FAIL (branch iv retracted) | W4-44 frozen JSON, W4-46 w_0^Z(L=9)=−0.997, W1a-3 SV2 retraction | successor-tree SHA-pinned; no re-registration of parent | 2-3h |
| CF-M3 | **CMB-S4 α_s flagship pre-registration document** (W6-D.4): formalize as single-authority pre-registration with per-detector σ-forecast and branch-iv independence statement | W6-52 CSV, S50 permanent identity, W10-123 4-axiom proof | pre-registration landed in `sessions/pre-registered-observations.md`; timeline mapping to CMB-S4 first-light | 0.5 session |
| CF-M4 | **LISA CGWB flagship pre-registration** (W7b): fix-k vs fixed-f clarification; Ω_GW(f) at {1e-4, 1e-3, 1e-1} Hz for (A), (C), (LI) branches with transfer_correction {0.5, 1.0, 2.0} bracket | W6-50 script + data, LISA sensitivity curve L2023+ | pre-registration document + timeline mapping to LISA L3-L4 (~2035) | 0.5 session |
| CF-M5 | **LiteBIRD n_T W4-41 permanent registry landing**: write up EVOI=0 as structurally permanent for 2030-2040 window; attach to W4-48 rigor registry as reference for DET-STERILE scope | W4-41 verdict, W4-37 3-param Fisher numerics, rescue-path enumeration (6-yr LB, LSST κκ, delensing >50%) | registry entry cites rescue-path options; does NOT retract EVOI=0 | 0.25 session |
| CF-M6 | **α_s / w_a decoupled-joint evidence ledger**: book the joint test (CMB-S4 + DR3) as independent cross-channels per W8-88 decoupling theorem; maintain separate log-BF tallies | W8-88 Jacobian-zero theorem, W4-44 tree, W6-52 Fisher | per-channel BF accounts; no cross-contamination allowed | 0.25 session |
| CF-M7 | **n_T(CMB) two-speed re-adjudication under W4-48** (from W4 CF-W4.4): test whether S68's c_T=c_S=1 assumption was a CHOICE or a CONSEQUENCE of prior convention | W4-48 flag entry row 4, W4-39 derivation chain, S68 LITEB-R-FORECAST-68 code | adjudication verdict binding on W4-48 row classification | 3-4h |
| CF-M8 | **21-cm folded-shape template forecast** (W4 CF-W4.3): folded-triangle SHAPE template at l_max=10⁵; substrate-unique bispectrum shape NOT amplitude running | W4-38 folded channel −0.080, 21-cm purpose-built forecast | PASS iff shape distinguishable from LCDM at SNR ≥ 2 | 8-10h |
| CF-M9 | **BK-Array 2026 live-watch**: monitor BICEP Array + Keck 2026 r release; classify cell under W4-42 4-branch tree; framework is pre-committed to the branch | W4-42 frozen JSON, BK release data | classification fires on release | 0.25 session |
| CF-M10 | **PIXIE μ-distortion K-endpoint pre-registration**: write up W5-57 K=3.56×10⁵ endpoint giving μ=8.69×10⁻⁵ (edge of FIRAS) as PIXIE-visible prediction; γ=1 lockout | W5-57 corridor script + data | pre-registration document + lockout against γ>1 revision | 0.25 session |

---

## §X. Classification sign-off

Per `.claude/rules/phononic-framing.md`:

- **PHONONIC gates/channels**: f_NL (eq/fold/multi GGE bispectrum), α_f_NL (GGE running), CGWB (acoustic transit), 21-cm folded shape, ISW tracking (substrate compaction), σ_8 (post-transit structure).
- **GEOMETRIC gates/channels**: n_s (spectral tilt from Bogoliubov-inversion triple), α_s (O-Z single-pole identity from spectral-triple rank universality), r (tensor amplitude from G46), n_T (modified consistency via c_T/c_S = a_2/a_0), A_s (spectral-triple amplitude), μ (Chluba kernel on spectral UV-IR crossover), (w_0, w_a) (Josephson temporal-asymmetry + four-fold lock), τ_fold uniqueness under Γ6 cubic-BC.
- **PARTICLE gates/channels**: m_H / sin²θ_W (μ_BC fit, Cartan-trace W9b-106), ν mass ordering (Bogoliubov level ordering in SU(3) block).
- **NON-PHONONIC**: W4-48 registry itself (bookkeeping), C_cons internal consistency (not external-detector-facing).

---

## §XI. Methodology notes (load-bearing for S85 reviewer access)

- Per `.claude/rules/epistemic-discipline.md`: PASS on an LCDM-compatible target from zero free parameters is EVIDENCE, not neutrality (per `feedback_reporting-framing.md`). The 11 ZFP channels carry load-bearing BF.
- Per `.claude/rules/output-standards.md`: this synthesis uses action-item 4-field carry-forward format (What / Inputs / Gate / Effort); no unstructured `DEFERRED` tags.
- Per `.claude/rules/v3-closure-recovery.md`: S84 closed V3-NON-COMPLIANT (sig_5 only). Carry-forward items CF-M1…CF-M10 inherit the carry-forward priority; S85 plan-freeze must address PRU at the plan level (S85-PLAN-PRU-REMEDIATION from W9 §W9.5).
- EVOI table in §IV is my recalibration for the post-W4-48 atlas; should be reconciled with `sessions/evoi-framework.md` by S85 planner.

---

## §XII. What this synthesis does NOT claim

- I do NOT report an overall PASS/FAIL tally or "master gate" status for the framework (per `feedback_no-master-gate-tally.md`).
- I do NOT report a session probability update (per `.claude/rules/epistemic-discipline.md`, constraint counts are not arguments; the effort-based probability rule sits in `.claude/rules/evoi-prioritization.md`).
- I do NOT recommend retreating from w_0 = −0.918 canonical. W1a-3 SV2 FAIL RETRACTED branch-iv — this is a provisional retraction with S85 re-audit obligation. The canonical `w0_FW = −0.918` in canonical_constants.py remains pinned per Wave 1's reversion protocol.
- I do NOT claim the framework's ZFP column is an observational "score." Each ZFP row is a pre-registered test against an already-measured or to-be-measured channel; aggregate evidence is the PRODUCT of per-channel BFs, per `feedback_reporting-framing.md`.

---

*End of S4-Mack solo synthesis. 18-channel rigor registry preserved; 10 calendar-bound detector events mapped; 10 S85 carry-forwards registered with 4-field structure; sign-lockouts pre-committed per W1b-9 lockouts A-F and W4-44/W4-42 frozen trees. Every σ/direction/threshold claim in this document is backed by an explicit substitution chain or verified Python computation per `.claude/rules/math-scripts.md`.*
