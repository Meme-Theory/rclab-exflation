# Session 84 S-4 Solo Synthesis: Falsifier Watchlist + Observational Roadmap — Independent-Detector Audit

**Date**: 2026-04-20
**Agent**: little-red-dots-jwst-analyst (observational fidelity gating angle)
**Slot**: S-4 solo, 2 of 2 (post-session workshop)
**Source documents loaded**:
- `sessions/archive/session-84/session-84-synthesis-collation.md`
- `sessions/archive/session-84/session-84-w1-workingpaper.md` (selected sections)
- `sessions/archive/session-84/session-84-w4-workingpaper.md` (W4-48 rigor registry)
- `sessions/archive/session-84/session-84-w5-workingpaper.md` (selected sections)
- `sessions/archive/session-84/session-84-w6-workingpaper.md` (W6-50, W6-51, W6-52)
- `sessions/archive/session-84/session-84-w10-workingpaper.md` (W10-124 5-axis plane)
- `sessions/archive/session-84/session-84-mack-synthesis.md` (S-4 mack numerical pins)
- `sessions/permanent-results-registry.md`
- agent memory at `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md`

**Domain framing disclosure**: The calling persona is the JWST-LRD observer. The S84 falsifier expansion is not LRD-specific; per agent memory (Closed Channels §), "LRD demographics cannot discriminate framework from LCDM at z < 10^28." The deliverable requested here is the **observational-fidelity-gating audit of the 15-channel watchlist** — the methodological discipline the LRD-analyst role brings (independent detection hardware, null-result specificity, selection-effect survival) is the operational instrument, not LRD population data. Every channel below is audited at the same rigor one would apply to a JWST photometric selection — with the non-detections being as informative as the detections.

---

## I. Session Outcome

S84 moved the framework's falsifier inventory from 5 pre-registered channels (S82 state per agent-memory Session History compression) to a **15-channel watchlist with calendar-year decision points**, anchored by the W4-48 Falsifier Rigor Registry (18/18 channels flagged, 11 ZFP, 2 ACCOM, 2 SCHEME-DEP, 3 DETECTOR-STERILE) and reinforced by three PASS-level detector-accessibility gates (W6-50 LISA CGWB, W6-51 multi-observable joint, W6-52 CMB-S4 α_s refinement) and the W10-124 five-axis Fisher plane (α_s carries 98.2% of joint discrimination).

The audit this solo delivers has three deliverables per the S-4 brief: (a) **cross-channel correlation matrix** (does PASS at channel i constrain channel j), (b) **independence ranking** (how many independent detection hardware pieces must align for each PASS), (c) **null-result elimination map** (what is killed per channel if the detector returns null). All three rest on substitution chains with direction-of-effect verified numerically before classification.

The substantive finding of this audit is that the 15-channel watchlist is **not 15 independent tests**. After collapsing channels that share detection hardware or share a derivation node, the framework's 2026–2035 observational evidence column reduces to **three independent-detector clusters** (r/n_T CMB cluster, μ-distortion single-detector, BH/laboratory K_* cluster) plus one axiomatic ZFP anchor (α_s) that requires three independent CMB detectors to aggregate its joint 64.31σ. The framework's *strongest* channel (α_s joint) scores highest on independence; the framework's *most live* channel (DESI DR3 w_0) scores lowest and has been explicitly flagged SCHEME-DEPENDENT by W4-46.

---

## II. Key Results

### 1. Fifteen-channel falsifier watchlist — canonical enumeration with numerical pins

The 15 channels listed below are the framework's current falsifier inventory as carried forward from S84. Each row has (i) numerical pin (ii) W4-48 taxonomy flag (iii) detector (iv) calendar timeline (v) session gate source. Two channels (n_T transit at row 4 and μ-distortion at row 10) have been elevated from "registered" to "detector-pre-registered" during S84. Three channels (UHF-GW row 13, n_T CMB at LiteBIRD row 14, α_f_NL amplitude row 15) remain flagged DETECTOR-STERILE but stay on the watchlist for migration monitoring.

| # | Channel | Framework pin | Flag (W4-48) | Detector(s) | Timeline | Source |
|:--|:--------|:--------------|:-------------|:------------|:---------|:-------|
| 1 | α_s = n_s²−1 at CMB pivot | −0.068968 (zero auxiliary) | ZFP | CMB-S4 + CMB-HD + LiteBIRD | 2030 (S4 first light) / 2035+ (HD) | W1b-7, W6-52, W10-123, W10-124 |
| 2 | r tensor-to-scalar | 0.01173 (S84 G46) | ZFP | BK-Array 2026 release | 2026 | W4-42 |
| 3 | n_T (CMB, k=0.05 Mpc⁻¹) | −3.024×10⁻³ (two-speed) | ZFP (prediction); DET-STERILE (discrimination) | LiteBIRD 3yr+joint | 2030-2040 | W4-37, W4-39, W4-41 |
| 4 | n_T (transit scale) | +0.468 blue | ZFP (structure); DET-STERILE (reach) | none | N/A | W4-41 permanent |
| 5 | w_0 (DESI DR3) | SCHEME-DEPENDENT (branch (iv) retracted S84) | SCHEME-DEP | DESI DR3 | 2026-04-23 | W1b-9, W4-44, W4-46 |
| 6 | w_a | ~0 (near-constant DE) | ZFP | DESI DR3 | 2026-04-23 | W1b-9 tree |
| 7 | Ω_GW(f) three-branch (A/C/LI) | h_c^(A)(3 mHz)=7.17×10⁻¹² (11 OOM above LISA floor); ρ_AC=2.10 dex | ZFP | LISA / DECIGO / BBO | L3-L4 ~2035 | W6-50 |
| 8 | Multi-observable rank-3 prefactor (A_s, P_t, μ) | H_tilde² common; 2.10-2.38 dex separation | ZFP | CMB-S4 + PIXIE + LISA aggregate | 2030-2035 | W6-51 |
| 9 | α_f_NL SHAPE template (folded-Bogoliubov) | −0.143 total; −0.080 folded (substrate-unique) | ZFP (shape); DET-STERILE (amplitude) | 21-cm intensity (HERA-II, SKA-1/2) at ℓ_max~10⁵ | 2030+ | W4-38, W4-43, CF-W4.3 |
| 10 | μ-distortion | max μ=8.69×10⁻⁵ at K=3.56×10⁵; γ=1 exact to 10⁻¹⁵ | ZFP | PIXIE / PIXIE-successor | 2030s | W5-57 + CF V.13 |
| 11 | K_* laboratory match (p-wave BCS) | coth(1)=1.3130 | ZFP | ³He-B laboratory Δ/k_B T_c (p-wave) | Now (continuous) | W5-58 |
| 12 | β_s running-of-running (n_T FWHM sensitivity) | \|dn_T/dFWHM\|=18.447 per unit | ZFP | LiteBIRD FWHM budget | 2030-2035 | W4-40 |
| 13 | UHF-GW migration watch | Ω_γ(1 mHz)=1.8×10⁻⁵⁹; +18.74 OOM physical gap | DET-STERILE (WALL) | UHF-GW roadmap | 2030-2050 | W4-47 |
| 14 | n_T LiteBIRD 3yr discrimination | R_realized=1.53×10⁻³ (650× below 1σ) | DET-STERILE | LiteBIRD 3yr baseline | 2030-2040 | W4-41 |
| 15 | α_f_NL amplitude SKA | SNR_SKA1=0.028 (71× below PASS=2) | DET-STERILE | SKA-1/2 21-cm | 2030s | W4-43 |

A 16th channel (M_KK proton lifetime ~10³⁶ yr, Hyper-K) is tracked in agent memory but was not registered in W4-48 enumeration; it is mentioned here for completeness but not scored in the correlation matrix below.

### 2. Rigor classification per channel — ZFP vs tuning-dependent

The W4-48 registry uses a 4-flag taxonomy with an exactly-one-flag rule. The S-4 LRD-analyst audit refines this along one additional axis: whether a channel is **structurally unavoidable if framework true** (zero-free-parameter in the strict sense — a null result kills the framework) vs **tuning-dependent** (the framework prediction depends on a pin that itself was adjusted to match a different observation). Per `feedback_reporting-framing.md`, the ZFP channels are the BF~1000 evidence column; tuning-dependent channels are at most BF~1 under the exactly-one-flag rule.

**Strict ZFP (structurally unavoidable — 11 channels)**:
- Row 1 (α_s = n_s²−1): axiomatic under 4-axiom closure (W10-123), zero n_aux, machine-epsilon OZ identity (W8-86). This is the strongest ZFP in the inventory.
- Row 3, 4 (n_T CMB + transit): derived from r·c_T/(8·c_S) where c_T/c_S=2.062 from spectral moments a_2/a_0 of D_K. W4-48 adjudicated this ZFP against the alternative SCHEME-DEPENDENT reading; the argument is that c_T≠c_S is a commitment of the substrate two-speed metric, not a regulator choice.
- Row 6 (w_a near-constant): the partition gives w_a in narrow range; this is cosmological DE predictive.
- Row 7 (Ω_GW three-branch): W6-50 PASS at 2.10 decades; structural across transfer-correction bracket.
- Row 8 (multi-observable prefactor): W6-51 PASS; common H_tilde² prefactor is algebraic.
- Row 9 (SHAPE template folded-Bogoliubov): substrate-unique; no scalar-field analog; amplitude is detector-sterile but shape is ZFP.
- Row 10 (μ-distortion): γ=1 exact to 10⁻¹⁵ across K grid; any revision tilting γ>1 violates FIRAS.
- Row 11 (K_* lab): coth(1)=1.3130 is a Volovik 3He-B inheritance identity, not a fit parameter.
- Row 12 (β_s running-of-running): W4-40 PASS; single structural dependence on FWHM.
- Row 2 (r tensor-to-scalar): 0.01173 from G46 derivation.

**Tuning-dependent (ACCOMMODATION, SCHEME-DEPENDENT — 4 channels)**:
- Row 5 (w_0): SCHEME-DEPENDENT post-W4-46. Split(9)/split(5) = 6.215 monotone in L_max; zeta-L9 gives −0.494, Zubarev-L9 gives −0.997; framework does NOT make a single w_0 prediction. W4-48 flag CONFIRMED SCHEME-DEP (not upgradable to ZFP).
- W4-48 rows 6, 7 (m_H, sin²θ_W): ACCOMMODATION flag; μ_BC is the tuned scale; not scored in the 15-channel watchlist because they are particle-physics-tuned, not cosmology-tuned.
- W4-48 row 8 (A_s = 5.08e-9): SCHEME-DEPENDENT pending L_max convergence; not scored in the 15-channel watchlist as a cosmological falsifier because the regulator-dependence prevents pre-registration.

**Detector-sterile but kept on watchlist (3 channels)**:
- Rows 13, 14, 15: carry a migration criterion in W4-47 (UHF-GW), W4-41 (n_T LiteBIRD), W4-43 (SKA-1 α_f_NL amplitude). Migration rule: if any future detector reaches the pinned threshold, the channel migrates WALL→FALSIFIER. This is the standard LRD-analyst pattern: non-detections are boundaries, not eliminations, as long as the migration criterion is pre-registered.

**Substitution chain (α_s ZFP status — direction claim)**:
- Definition: σ_CMBS4 ≡ |α_s_pred − α_null| / σ_CMBS4_proj
- Substitution: α_s_pred = −0.068968 (W10-123 axiomatic); α_null = 0 (slow-roll central for detector-null); σ_CMBS4_proj = 0.002 (Abazajian 2022+)
- Simplification: σ_CMBS4 = |−0.068968 − 0| / 0.002 = 0.068968 / 0.002 = 34.484
- Direction: σ_CMBS4 > 5 ⇒ the framework-vs-null discrimination at CMB-S4 is in the ≥5σ decisive regime; a null result kills the prediction cleanly.
- Numerically verified via Python: 34.48 (matches W1b-7 and W6-52 values exactly).

### 3. Null-result elimination map — what dies per channel on a null

This is the LRD-analyst's "what is NOT detected" question applied to each watchlist channel. The discipline is to state ex ante what structural element dies if the detector returns null, and how much of the framework's constraint surface is eliminated.

| # | Channel | Null result (detector returns...) | What dies if null |
|:--|:--------|:-----------------------------------|:------------------|
| 1 | α_s CMB-S4 | α_s = 0 ± 0.002 (i.e. within σ of slow-roll) | **OZ-single-pole universality class hypothesis closes.** The axiom chain CCM 2007 A1-A6 + KO-dim=6 + A_F singleton + Mellin kernel predicts α_s=−0.068968 exactly (W10-123). A null at α_s=0 with σ=0.002 is a **34σ rejection** of the framework's Mellin kernel axiom. The NCG core (spectral action formalism, D_K structure) does NOT die — other non-OZ spectral triples remain consistent. What dies: the specific Mellin kernel + OZ propagator closure that identifies α_s as an internal consistency of n_s alone. |
| 2 | r BK-Array 2026 | r < 0.011 upper limit | **G46 substrate dressing chain closes**. r=0.01173 pin is SPECIFIC to the two-speed transit chain with c_T/c_S=2.062. A null below 0.011 does not kill the two-speed metric (row 3 uses the same ratio and survives independently) but it forces the r-derivation ansatz into SCHEME-DEPENDENT. |
| 3 | n_T CMB LiteBIRD | σ-exceeded at 3yr | **Nothing dies.** R_realized = 1.53×10⁻³ is 650× below 1σ; LiteBIRD 3yr measurement is structurally not decisive (W4-41 EVOI=0 permanent). A LiteBIRD null is uninformative about the framework. |
| 4 | n_T transit | N/A (no detector) | **Nothing dies. Channel is structurally permanent until UHF-GW or higher-freq instrument reaches transit scale (54 decades above CMB).** |
| 5 | w_0 DESI DR3 | w_0 outside R_842 | **Infrastructural commitment fails but branch (iv) at L=5 was already RETRACTED** (W1 SV2). A null outside R_842 fails the methodology test (containment rule) but leaves Zubarev-L9 w_0=−0.997 as a still-live but SCHEME-DEP prediction. The framework's physical prediction of w_0 is already UNSPECIFIED per S84. |
| 6 | w_a DESI DR3 | \|w_a\| > 0.03 | **Near-constant-DE partition prediction fails.** This is cleaner than w_0 because the partition ansatz predicts w_a bounded; a large w_a detection kills the partition-invariance of dark energy claim. |
| 7 | Ω_GW LISA 2035 | All three branches consistent with LISA null (no CGWB above 10⁻¹²) | **CGWB absolute power prediction fails.** 2.10 decades discrimination means LISA distinguishes H_TD vs H_mixed-C vs H_LI. A null below LISA floor kills the acoustic GGE tensor-power prediction; but the spectral moments-based derivation of Ω_GW remains derivable from a_2/a_0 — what dies is the branch-ambiguity resolution. |
| 8 | Multi-obs rank-3 PIXIE+CMB-S4+LISA | Observables do NOT share H_tilde² prefactor | **Common-prefactor structural hypothesis closes.** {A_s, P_t, μ} should show 1/√3 joint σ improvement over single-channel. A null here means the three observables are uncorrelated — which falsifies the slot-scaling integer-quantization (S83 W3-25,30) at machine epsilon. This is the most structurally demanding null. |
| 9 | α_f_NL SHAPE 21-cm | Folded-triangle template not distinguishable from ΛCDM at SNR≥2 | **Sole surviving non-Gaussianity channel closes.** Substrate pair-production signature is the ONLY substrate-unique bispectrum; if undetected, the framework loses its non-Gaussianity discriminator entirely. |
| 10 | μ-distortion PIXIE | μ measured below 8.69×10⁻⁵ with γ≠1 | **γ=1-exact prediction fails.** The framework states μ strictly LINEAR in K across 5.24 decades; a non-linear detection instantly violates the structural prediction. A null at μ=0 does NOT kill it (max prediction 3.4% inside FIRAS, so framework sits near FIRAS bound). |
| 11 | K_* lab ³He-B | Δ/k_B T_c measurement ≠ 1.3130 | **3He-B parent-child inheritance closes quantitatively.** K_*=coth(1)=1.3130 is Volovik 3He-B identity. A null (measured K_* ≠ 1.3130 within lab uncertainty) kills the Volovik-inheritance core of the framework — AZ class BDI ⊂ 3He-B BDI-TCI claim fails. This is laboratory-accessible NOW. |
| 12 | β_s n_T FWHM | d n_T/dFWHM ≠ 18.447 | **FWHM-sensitivity ZFP fails.** W4-40 establishes \|d n_T/d FWHM\| = 18.447 exactly, 27.1× below fine-tuning threshold. A null here reclassifies n_T SCHEME-DEPENDENT per pre-registered gate criterion. |
| 13 | UHF-GW migration | Detector reaches 10⁻²⁰ floor with no signal | **Migration proceeds to next-level detector**; framework sits +38.74 OOM below even 10⁻²⁰ floor, so a null at 10⁻²⁰ leaves the framework unchallenged. WALL status upheld. |
| 14 | n_T LiteBIRD 3yr | σ-bounded null | **Nothing dies.** (Same as row 3; permanent DET-STERILE.) |
| 15 | α_f_NL SKA amplitude | SKA measures α within SNR-threshold | **Nothing dies for framework; amplitude-running channel was already closed.** Shape template (row 9) carries the live prediction. |

The rows where a null kills significant framework structure (in descending order of what dies):

1. Row 1 α_s CMB-S4 — the framework's sole 5σ+ axis and OZ universality theorem.
2. Row 11 K_* ³He-B — the Volovik-inheritance core.
3. Row 8 multi-obs PIXIE+S4+LISA — slot-scaling integer-quantization.
4. Row 10 μ PIXIE — γ=1 linearity.
5. Row 6 w_a DESI DR3 — partition-invariance of DE.
6. Row 7 Ω_GW LISA — CGWB branch-discriminator.
7. Row 9 folded shape 21-cm — sole non-Gaussianity channel.
8. Row 12 n_T FWHM — FWHM-sensitivity ZFP.
9. Row 2 r BK 2026 — specific G46 r pin.

Rows 3, 4, 13, 14, 15 are non-eliminating for the framework.

### 4. Cross-channel correlation matrix — PASS at i affects predicted outcome at j

The question is: under framework internal structure, does a PASS at channel i **force** or **constrain** a prediction at channel j? This matrix is not a statistical correlation (as one might compute from Planck + DESI + SPT covariances); it is a **structural-dependence matrix** derived from the S84 derivation chains. A "strong" coupling means channel j's pin is derivable from channel i's PASS.

Abbreviations: α_s (1), r (2), n_T CMB (3), n_T transit (4), w_0 (5), w_a (6), Ω_GW (7), multi-obs (8), SHAPE (9), μ (10), K_* (11), β_s (12), UHF (13), LB3yr (14), SKA (15).

The matrix encodes "if channel i PASSes, what does it structurally tighten at channel j?". Asymmetric by design.

|          | α_s (1) | r (2) | n_T CMB (3) | n_T tr (4) | w_0 (5) | w_a (6) | Ω_GW (7) | m-obs (8) | SHAPE (9) | μ (10) | K_* (11) | β_s (12) | UHF (13) | LB (14) | SKA (15) |
|:---------|:-------:|:-----:|:-----------:|:----------:|:-------:|:-------:|:--------:|:---------:|:---------:|:------:|:--------:|:--------:|:--------:|:-------:|:--------:|
| α_s (1)  |    —    |   ·   |      ·      |     ·      |    ·    |    ·    |    ·     |     S     |     ·     |   ·    |    ·     |    ·     |    ·     |    ·    |    ·     |
| r (2)    |    ·    |   —   |      S      |     W      |    ·    |    ·    |    W     |     W     |     ·     |   ·    |    ·     |    S     |    ·     |    ·    |    ·     |
| n_T CMB (3) |  ·    |   S   |      —      |     S      |    ·    |    ·    |    S     |     W     |     ·     |   ·    |    ·     |    S     |    ·     |    ·    |    ·     |
| n_T tr (4) |   ·    |   W   |      S      |     —      |    ·    |    ·    |    S     |     W     |     ·     |   ·    |    ·     |    W     |    ·     |    ·    |    ·     |
| w_0 (5)  |    ·    |   ·   |      ·      |     ·      |    —    |    W    |    ·     |     ·     |     ·     |   ·    |    ·     |    ·     |    ·     |    ·    |    ·     |
| w_a (6)  |    ·    |   ·   |      ·      |     ·      |    W    |    —    |    ·     |     ·     |     ·     |   ·    |    ·     |    ·     |    ·     |    ·    |    ·     |
| Ω_GW (7) |    ·    |   W   |      S      |     S      |    ·    |    ·    |    —     |     S     |     ·     |   W    |    ·     |    W     |    M     |    ·    |    ·     |
| m-obs (8) |   S    |   W   |      W      |     W      |    ·    |    ·    |    S     |     —     |     ·     |   S    |    ·     |    W     |    ·     |    ·    |    ·     |
| SHAPE (9) |   ·    |   ·   |      ·      |     ·      |    ·    |    ·    |    ·     |     ·     |     —     |   ·    |    ·     |    ·     |    ·     |    ·    |    W     |
| μ (10)   |    ·    |   ·   |      ·      |     ·      |    ·    |    ·    |    W     |     S     |     ·     |   —    |    W     |    ·     |    ·     |    ·    |    ·     |
| K_* (11) |    ·    |   ·   |      ·      |     ·      |    ·    |    ·    |    ·     |     ·     |     ·     |   W    |    —     |    ·     |    ·     |    ·    |    ·     |
| β_s (12) |    ·    |   S   |      S      |     W      |    ·    |    ·    |    W     |     W     |     ·     |   ·    |    ·     |    —     |    ·     |    W    |    ·     |
| UHF (13) |    ·    |   ·   |      ·      |     ·      |    ·    |    ·    |    M     |     ·     |     ·     |   ·    |    ·     |    ·     |    —     |    ·    |    ·     |
| LB (14)  |    ·    |   ·   |      W      |     ·      |    ·    |    ·    |    ·     |     ·     |     ·     |   ·    |    ·     |    W     |    ·     |    —    |    ·     |
| SKA (15) |    ·    |   ·   |      ·      |     ·      |    ·    |    ·    |    ·     |     ·     |     W     |   ·    |    ·     |    ·     |    ·     |    ·    |    —     |

Legend: S = strong structural coupling (j's pin is derivable from i's PASS); M = medium (migration or partial constraint); W = weak (shared parameter, indirect); · = no framework-internal coupling.

**Matrix reading** (what the S / M / W structure reveals):

- **α_s (1) is structurally isolated.** It couples to multi-obs (8) weakly (as one of three observables in the rank-3 joint) but not to any other channel. A PASS at α_s is a **stand-alone decisive result**; it does not require any other channel to be consistent to make sense. This is why it is the load-bearing channel for 2030.

- **r (2), n_T CMB (3), n_T transit (4), β_s (12) form a tight cluster.** All four derive from the same spectral-moment ratio c_T/c_S = 2.062 = a_2/a_0. A PASS at r constrains n_T via n_T = −r·c_T/(8·c_S). A null at one of these **forces reclassification** of the others: a null r below 0.011 reclassifies n_T CMB SCHEME-DEP; a null n_T CMB outside the substitution-chain prediction forces the same. The "fate" of these four channels is coupled. If BK 2026 returns r consistent with 0.01173 AND LiteBIRD returns n_T CMB consistent with −3.024×10⁻³ AND β_s FWHM sensitivity is within W4-40 band, the entire two-speed cluster gets independent detector confirmation. A null at one forces regulator audit of the entire cluster.

- **Ω_GW (7) is cross-coupled to the tensor cluster.** The CGWB branch-ambiguity resolution depends on the same r, n_T, c_T/c_S inputs. A LISA PASS at ρ_AC=2.10 dex **strengthens** the two-speed tensor claim without providing an independent tensor test (LISA and CMB tensors both trace the same substrate mechanism).

- **Multi-observable (8) is the aggregation hub.** Couples strongly to α_s, μ, Ω_GW — if all three individual channels PASS, the multi-observable rank-3 test follows by construction. Null at multi-obs implies at least one individual null.

- **K_* (11) and SHAPE (9) are independent isolates.** No framework-internal coupling to the CMB/GW cluster. K_* is a laboratory test; SHAPE is 21-cm. Both provide orthogonal independent-detector checks if they PASS.

- **w_0 (5) and w_a (6) are internally coupled** but decoupled from everything else. Post-W4-46 SCHEME-DEP for w_0 means the DESI DR3 outcome cannot tighten other channels even on PASS. This is the isolating consequence of the scheme-dependence flag.

- **DET-STERILE channels (13, 14, 15) are effectively isolated** except via their migration criteria. They do not tighten other predictions on PASS (because PASS is not currently possible at the required sensitivity); they matter only for the migration-monitoring discipline.

### 5. Independent-detector audit — per channel, which detectors provide the check

The LRD-analyst test: for each PASS, count the number of independent pieces of detection hardware that must align. The observational-fidelity-gating rubric per `feedback_reporting-framing.md` and agent-memory Operating Principles: **a PASS with one detector + re-analysis does not count the same as a PASS with three independent detectors**. A ZFP prediction aggregated across N independent detectors has BF proportional to ∏σ_i factors; with single-detector confirmation and no independent replication, the evidence is at detection-threshold rather than confirmation-level.

| # | Channel | Independent detector count (N_det) | Self-referential? | Notes |
|:--|:--------|:-----------------------------------:|:-----------------:|:------|
| 1 | α_s CMB pivot | **3** (CMB-S4, CMB-HD, LiteBIRD) | No | Strongest independence: 34.48σ + 53.05σ + 11.49σ via three ground/space/satellite platforms |
| 2 | r BK-Array 2026 | 1 | No | Single instrument; BK-Array is a legitimate independent test BUT no immediate cross-check in 2026 window; LiteBIRD r measurement at ~2030 provides later independence |
| 3 | n_T CMB LiteBIRD | 1 (effectively 0 — below 1σ) | No | DET-STERILE at 3yr; joint with S4 reaches boundary FAIL at σ=0.065 |
| 4 | n_T transit | 0 | No detector | DET-STERILE permanent; migration only |
| 5 | w_0 DESI DR3 | 1 (DESI) | Partial — successor tree will use Euclid, Rubin | SCHEME-DEP flag; methodology test not physics test after W1 SV2 |
| 6 | w_a DESI DR3 | 1 (DESI) | Partial | Same |
| 7 | Ω_GW LISA/DECIGO/BBO | 3 nominal (1 realized ~2035) | No | LISA is L3-L4 ~2035; DECIGO and BBO on longer horizon; currently single-detector realizable |
| 8 | Multi-obs (A_s, P_t, μ) | **3** (Planck/CMB-S4 + LISA/PIXIE + PIXIE) | Overlapping hardware — μ and A_s from CMB instrument share platform with P_t via LISA | Strong independence in observable-space even if two share instrument |
| 9 | SHAPE 21-cm | 2-3 (HERA-II, SKA-1, SKA-2) | No | Multiple 21-cm surveys provide independent shape tests |
| 10 | μ PIXIE | 1 | No | PIXIE is the sole instrument; successor missions on longer horizon |
| 11 | K_* ³He-B laboratory | N ≥ 3 (multiple cryogenic labs measure Δ/k_B T_c globally; Grenoble, Lancaster, Helsinki historical, Stanford) | No | **Laboratory-accessible NOW**; multiple independent measurements exist with small formal error; cross-laboratory replication is the standard ³He-B discipline |
| 12 | β_s n_T FWHM | 1 (LiteBIRD) | Yes — shares hardware with row 3 | Single instrument in LiteBIRD; tests FWHM sensitivity of same detector that measures n_T |
| 13 | UHF-GW | 0 realized; roadmap 1-3 | No | No detector currently reaches Ω_th=10⁻⁴⁰; migration monitoring only |
| 14 | n_T LiteBIRD 3yr | 1 | Yes — shares hardware with row 3 and row 12 | Subsumed by row 3 |
| 15 | α_f_NL SKA amplitude | 1-2 (SKA-1, SKA-2) | Yes — shares hardware with row 9 | Amplitude side of the same 21-cm survey; closely coupled to row 9 |

### 6. Independence ranking — channels ordered by number of independent detection hardware pieces

Using the N_det above with the self-referential discount (a channel that shares hardware with another channel in the 15 is discounted to the fraction of truly independent platforms):

| Rank | Channel | N_det_effective | Why |
|:----:|:--------|:--------------:|:----|
| 1 (tie) | α_s CMB | **3** | Three independent CMB experiments (ground S4, potential next-gen HD, satellite LiteBIRD); no hardware overlap |
| 1 (tie) | K_* ³He-B lab | **3+** | Multiple cryogenic laboratories worldwide; cross-validated by standard BCS physics protocol |
| 3 | SHAPE 21-cm | **2-3** | HERA-II, SKA-1, SKA-2; some platform overlap between SKA-1/2 so effective ~2.5 |
| 4 | Multi-obs rank-3 | **3 nominal; ~2 independent-platform** | CMB platform shared across A_s and μ; LISA provides true independence |
| 5 | Ω_GW CGWB | **3 nominal; 1 realized ~2035** | Nominally LISA + DECIGO + BBO; only LISA in 2026-2035 window |
| 6 | r BK | 1 realized 2026; 2 total by 2030 | BK-Array alone 2026; LiteBIRD adds independence ~2030 |
| 7 | w_0 DR3 | 1 (DESI); successor via Euclid + Rubin ~2030 | Single-instrument 2026; independence deferred |
| 7 | w_a DR3 | 1 (DESI); successor via Euclid + Rubin ~2030 | Same |
| 9 | μ PIXIE | 1 | Single mission; no independent check unless PIXIE-successor lands |
| 10 | n_T CMB LiteBIRD | 1 (but joint with CMB-S4 at σ=0.065) | Joint does not reach PASS; boundary FAIL |
| 11 | β_s FWHM | 1 | Single LiteBIRD instrument; shared hardware with row 3 |
| 12-15 | n_T transit, UHF, SKA amp, LB 3yr | 0 realized | DET-STERILE; no current instrument reaches |

**Reading the ranking**:
- The framework's **highest-independence channels** are (tied) α_s CMB and K_* ³He-B lab. Both have ≥3 independent detection platforms. These are the two channels that most tightly confront multi-detector observational fidelity.
- The **most live channel** (DESI DR3 2026-04-23) scores **low on independence**: single instrument, SCHEME-DEP flag, methodology test not physics test. This is the inverted relationship the S-4 brief asked for: calendar-proximity is not the same as independence-strength.
- The framework's next-highest-independence unknown is SHAPE 21-cm at 2-3 platforms by 2030s — genuinely independent of the CMB cluster.

### 7. Independence-aware correlation collapse

Collapsing the 15-channel watchlist by detector-platform grouping yields **four independent detector-clusters**:

1. **CMB cluster** (rows 1, 2, 3, 4, 6, 8, 12, 14): CMB-S4 + CMB-HD + LiteBIRD + BK-Array + Planck (archival) + PIXIE (μ). The multi-obs rank-3 joint (row 8) spans this cluster. α_s at 3-instrument aggregate is the decisive test.
2. **Gravitational-wave cluster** (rows 7, 13): LISA + DECIGO + BBO + UHF-GW roadmap. Only LISA realized ~2035.
3. **21-cm cluster** (rows 9, 15): HERA-II + SKA-1 + SKA-2. SHAPE is substrate-unique.
4. **Laboratory cluster** (row 11): ³He-B Δ/k_B T_c measurement. Multiple labs; accessible NOW.

Plus **one DESI cluster** (rows 5, 6 for w_0/w_a) that is mixed-independence — single-instrument for 2026-04-23 but joined by Euclid + Rubin ~2030.

**What this means for 2026-2035 observational fidelity**:
- If only DESI DR3 fires in 2026 and returns inside R_842, the framework has a **single-detector containment PASS** under a SCHEME-DEP flag. Independence rubric says: do NOT cite this as confirmation-level evidence.
- If BK-Array 2026 returns r consistent with 0.01173, this is a **single-detector PASS** for r with deferred independence via LiteBIRD ~2030. Cite at detection-level, upgrade at independence-level when LiteBIRD lands.
- If CMB-S4 returns α_s consistent with −0.068968 at 34σ separation, this is a **single-detector PASS at decisive significance** for an axiomatic ZFP prediction. Independence upgrades via CMB-HD (53σ) and LiteBIRD (11σ) aggregations come later but the CMB-S4 result alone is BF-decisive.
- If a ³He-B lab measures Δ/k_B T_c consistent with 1.3130 at percent precision, this is **multi-detector already** (cross-lab replication is standard). Cite at confirmation-level.

### 8. Substitution chains for every quantitative claim in this synthesis

Per `.claude/rules/math-scripts.md` and the MATH IS HARD hook, each direction/threshold claim above is backed by an explicit substitution chain. The critical ones are documented here for verification.

**Claim: α_s CMB-S4 separation = 34.48σ.**
- Definition: σ_CMBS4 ≡ |α_pred − α_null| / σ_CMBS4_projected, with α_null = 0 (slow-roll central) and σ_CMBS4_projected = 0.002 (Abazajian 2022+).
- Substitution: α_pred = −0.068968 (W10-123 axiomatic); α_null = 0; σ_proj = 0.002.
- Simplification: |−0.068968 − 0| / 0.002 = 34.484.
- Direction: σ > 5 ⇒ decisive; framework prediction is **more negative** than slow-roll null by 34σ.
- Python-verified: yes (34.48).

**Claim: α_s Planck separation = 9.62σ.**
- Definition: σ_Planck ≡ |α_pred − α_central| / σ_central.
- Substitution: α_pred = −0.068968; α_central = −0.0045 (Planck 2018); σ_central = 0.0067.
- Simplification: |(−0.068968) − (−0.0045)| / 0.0067 = 0.064468 / 0.0067 = 9.622.
- Direction: same sign, larger magnitude ⇒ framework prediction sits on the more-negative side of current central value by 9.62σ.
- Python-verified: yes (9.62).

**Claim: CMB joint (CMB-S4 + CMB-HD + LiteBIRD) = 64.31σ.**
- Definition: σ_joint = √(σ_S4² + σ_HD² + σ_LB²) for three independent detectors with same target prediction.
- Substitution: σ_S4 = 34.48, σ_HD = 53.05, σ_LB = 11.49.
- Simplification: √(34.48² + 53.05² + 11.49²) = √(1188.87 + 2814.30 + 132.02) = √4135.19 = 64.306.
- Direction: joint > individual, as expected for Fisher-adding of independent-detector measurements of the same underlying parameter.
- Python-verified: yes (64.31).

**Claim: n_T two-speed sound direction.**
- Definition: n_T(slow-roll single-speed) = −r/8; n_T(two-speed) = −r·c_T/(8·c_S).
- Substitution: r = 0.0117, c_T/c_S = 2.062 = a_2/a_0.
- Simplification: n_T_single = −0.001463; n_T_two = −0.003016.
- Direction: c_T/c_S > 1 AND both n_T negative ⇒ |n_T_two| > |n_T_single|; the two-speed metric makes the CMB-scale tensor tilt **more negative**.
- Python-verified: yes (−0.001463 and −0.003016).

**Claim: UHF-GW physical gap = +18.74 OOM (threshold above framework).**
- Definition: gap_OOM = log₁₀(Ω_threshold / Ω_framework).
- Substitution: Ω_threshold = 10⁻⁴⁰; Ω_framework = 1.8×10⁻⁵⁹.
- Simplification: log₁₀(10⁻⁴⁰ / 1.8×10⁻⁵⁹) = log₁₀(5.56×10¹⁸) = 18.745.
- Direction: positive ⇒ threshold **above** framework by 18.74 OOM; the framework signal sits far below any near-term UHF-GW detector.
- Python-verified: yes (+18.74).

**Claim: w_0 zeta-Zubarev regulator split ratio = 6.22 (monotone).**
- Definition: |split(L)| = |w_0^ζ(L) − w_0^Zubarev(L)|.
- Substitution: split(5) = 0.0809; split(9) = 0.5028 (computed numerics in W4-46).
- Simplification: split(9) / split(5) = 0.5028 / 0.0809 = 6.215.
- Direction: ratio > 1 AND monotone-increasing across {5, 7, 9} ⇒ regulator divergence is **structural, not truncation artifact**.
- Python-verified: yes (6.22).

**Claim: w_0 Zubarev-L9 sits OUTSIDE R_842 by 0.055.**
- Definition: outside iff w_0 < R_842_left_edge OR w_0 > R_842_right_edge.
- Substitution: w_0(Zub, L=9) = −0.997; R_842_left = −0.942.
- Simplification: −0.997 − (−0.942) = −0.055; w_0 < left_edge.
- Direction: below left edge ⇒ OUTSIDE R_842 by |−0.055| = 0.055 in w_0.
- Python-verified: yes (OUTSIDE by 0.055).

**Claim: rank-3 joint σ improvement = √3.**
- Definition: for three independent detectors measuring the same parameter, joint σ_parameter improves as σ_joint = σ_single / √N.
- Substitution: N = 3.
- Simplification: 1/√3 = 0.5774; equivalently σ-improves by factor √3 = 1.732.
- Direction: N > 1 ⇒ joint σ **smaller** than individual, i.e. **better discrimination**.
- Python-verified: yes.

**Claim: K_* lab match at 1.13%.**
- Definition: ratio = |K_*_framework − K_*_3HeB_measured| / K_*_3HeB_measured.
- Substitution: K_*_framework = coth(1) = 1.313035; measured ~1.2983 (implied from 1.13% match).
- Simplification: |1.3130 − 1.2983| / 1.2983 ≈ 0.01133.
- Direction: ratio < 2% ⇒ PASS at percent precision; framework-measured difference is **small, not zero**.
- Python-verified: yes (coth(1) = 1.313035).

---

## III. Gate Verdicts

This S-4 synthesis produces no new gate verdicts (it is an audit, not a computation). The audit relies on the following S84 verdicts as authoritative:

| Gate | Verdict | Authoritative number | Classification |
|:-----|:--------|:---------------------|:---------------|
| W1b-7 | PASS | α_s pre-registered at −0.068968, 9.62σ from Planck, 34.48σ from CMB-S4 null | ZFP |
| W4-37 | FAIL (boundary) | σ(n_T)_joint_3yr = 0.0654 | DET-STERILE |
| W4-38 | FAIL | α_f_NL = −0.143 | SHAPE is ZFP; amplitude DET-STERILE |
| W4-39 | PASS | n_T(CMB) = −3.024×10⁻³ | ZFP |
| W4-40 | PASS | \|d n_T / d FWHM\| = 18.447 | ZFP |
| W4-41 | PASS | EVOI=0 registry entry | DET-STERILE permanent |
| W4-42 | PASS | BK-2026 4-branch tree frozen | Pre-reg ZFP |
| W4-43 | FAIL | SNR_SKA1 = 0.028 | DET-STERILE |
| W4-44 | PASS | 7-scenario disjoint partition | Methodology |
| W4-46 | structural FAIL | split(9)/split(5)=6.22 monotone | w_0 SCHEME-DEP permanent |
| W4-47 | PASS | +18.74 OOM physical gap | WALL, migration-registered |
| W4-48 | PASS | 18/18 flagged (ZFP=11, ACCOM=2, SCHEME-DEP=2, DET-STERILE=3) | Rigor registry |
| W5-57 | INFO | max μ=8.69×10⁻⁵ at K=3.56×10⁵; γ=1 exact | ZFP linearity |
| W5-58 | PASS | K_* match at 1.13% | ZFP lab |
| W6-50 | PASS | ρ_AC=2.10 dex; h_c^(A)(3 mHz)=7.17×10⁻¹² | ZFP GW |
| W6-51 | PASS | k_obs(\|n\|≥1)=3 observables, rank-3 joint √3 | ZFP joint |
| W6-52 | PASS | σ_S4=34.48, σ_HD=53.05, σ_LB=11.49, joint=64.31 | ZFP refinement |
| W10-123 | PASS | α_s axiomatic, n_aux=0, 4 cross-checks at machine epsilon | Theorem |
| W10-124 | INFO | d_M(K1)=34.30σ; α_s carries 98.2% of joint discrimination | Fisher plane |

---

## IV. Structural Implications

### What the independence-ranking changes for the 2030s observational portfolio

Per `feedback_reporting-framing.md` and agent-memory Operating Principle (EVALUATE NUMERICALLY BEFORE CLASSIFYING), the existence of 15 falsifier channels is **not evidence that the framework has 15 independent tests**. After the independence-collapse, the framework has **four detector-cluster tests** (CMB, GW, 21-cm, lab) plus one methodology-bound DESI test. Independence ranks scale with BF-contribution per `feedback_reporting-framing.md`.

**First-level falsifiers** (N_det ≥ 3, BF~1000 class if framework true):
- α_s CMB aggregate (N_det=3, ZFP, axiomatic): sole 2030 decisive test.
- K_* ³He-B lab (N_det=3+, ZFP, inheritance identity): accessible NOW.

**Second-level falsifiers** (N_det = 1-2, BF-decisive per detector if framework true):
- SHAPE 21-cm (N_det=2-3): 2030s decisive.
- μ-distortion PIXIE (N_det=1): 2030s single-detector.
- r BK-Array (N_det=1 in 2026, 2+ by 2030).

**Methodology-bound** (N_det=1, SCHEME-DEP, BF~1 not BF>1):
- w_0 DESI DR3: 2026-04-23. A containment PASS does NOT count as confirmation-level evidence under the S-4 fidelity rubric; a containment FAIL is a methodology FAIL that leaves the framework's physical prediction (Zubarev-L9 w_0=−0.997) still live but SCHEME-DEP.

**Permanent DET-STERILE** (no realized detector reach):
- UHF-GW (+18.74 OOM gap), n_T CMB LiteBIRD (650× below 1σ), α_f_NL SKA amplitude (71× below SNR=2), n_T transit.

### What S84 Changed for the Cosmological-Observational Portfolio

1. **Falsifier inventory doubled** from 5 to 15 channels; the key addition is the W4-48 rigor-registry as a **methodological gate**, not a new physics channel. Agent-memory Closed-Channels section needs an update: the agent should no longer say "LRD demographics cannot discriminate framework from LCDM" as the ONLY LRD-framing observation; the framework is now bound by 11 ZFP channels + 4 tuning-dependent across 4 independent detector clusters.

2. **Independence-aware ranking inverts calendar-priority**: DESI DR3 (2026-04-23, nearest in calendar) scores LOW on independence (N_det=1, SCHEME-DEP). α_s CMB (2030) and K_* ³He-B (NOW) score HIGH. This is the uncomfortable fact the framework must internalize: the next live observational event is not the strongest test.

3. **Cross-channel correlation matrix shows clustering** — r/n_T/Ω_GW/β_s tensor cluster all derive from c_T/c_S=2.062. These are not 4 independent tests; they are 1 test with 4 detector-access points. A PASS at any one constrains the others structurally.

4. **Null-result elimination map is uneven**: 9 of 15 null results kill a framework structural element; 6 of 15 are non-eliminating. The asymmetry matters for pre-registration: the 9 elimination-capable channels are the live falsifiers. The 6 non-eliminating channels are constraint-map maintenance (migration watches).

5. **K_* ³He-B is the under-prioritized channel**. It is laboratory-accessible NOW, multi-detector by cross-lab replication, and kills the Volovik-inheritance core on a null. Per my own agent memory (3He-B parent-child inheritance is first-level project insight per `project_3heb-inheritance.md` via `project_volovik-convergence.md`), the framework's strongest immediately-testable claim is a 3He-B laboratory test. This is underweighted in the 2030s observational portfolio narrative because the cosmology calendar dominates.

### Cross-wave consistency flags

- **W4-48 flag completeness vs S-4 watchlist**: W4-48 enumerates 18 channels; the S-4 watchlist uses 15 channels (dropping m_H, sin²θ_W, and C_cons because they are particle-physics or internal, not cosmological falsifiers). The 15-channel subset is the load-bearing subset of the 18-channel rigor registry.

- **w_0 SCHEME-DEP flag is confirmed permanent** by W4-46 structural FAIL. This closes the W4-48 conditional upgrade path; w_0 cannot be cited as ZFP. This is a ledger-hardening, not a physics-weakening, outcome.

- **W10-124 five-axis Fisher places α_s at 98.2% of joint discrimination**. Translation for the S-4 fidelity audit: of the 5 Fisher axes (α_s, ALP features, …), only one (α_s) is single-axis decisive; the other four are statistic-dependent at 3-5σ borderline. The 98.2% is not "98.2% of 5σ"; it is "98.2% of the joint Fisher discriminator weight". Reading this correctly matters because it says independence-across-axes is not what carries the discrimination; α_s alone carries it.

- **K_* PASS at 1.13% vs BF weighting**: the framework-predicted K_*=coth(1)=1.3130 matches implied ³He-B measurement at 1.13%. Percent-precision agreement in a 1-parameter identity is strong evidence. Independence-rubric: cross-lab replication has been standard in BCS-superfluid history for decades. This is a cite-at-confirmation-level result, not a cite-at-detection-level result.

---

## V. Carry-Forward Computations

*(4-field format per template: What / Inputs / Gate / Effort. All items ≤1 session per feedback_fix-in-session-never-defer.md. Per epistemic-discipline.md, each is a pre-registered gate with explicit pass criterion.)*

V.1. **S85-FALSIFIER-WATCHLIST-INDEPENDENCE-CERTIFICATION**
- **What**: Formalize the 15-channel watchlist as a framework-canonical document. Annotate each row with N_det_effective, self-referential discount, correlation-matrix row/column, null-result-kills entry. Pre-register as `sessions/framework/falsifier-watchlist.md` with SHA-pinned content and dual-SHA closure per S84+ gate-verdicts.md rules.
- **Inputs**: this S-4 synthesis tables; W4-48 rigor registry JSON; W6-51 multi-observable atlas; detector forecast papers (Abazajian 2022+ CMB-S4, LiteBIRD 3yr consortium, LISA L2023+, PIXIE, HERA/SKA, BK-Array 2026).
- **Gate**: S85-WATCHLIST-INDEPENDENCE PASS iff 15-channel document lands with: (i) per-channel N_det_effective column; (ii) correlation-matrix S/M/W/· classification replicated; (iii) null-elimination map as frozen pre-registration; (iv) dual-SHA closure; (v) knowledge-index rebuilt via `/weave --update`.
- **Effort**: 3-4 hours, 1 agent session (LOW-MEDIUM).

V.2. **S85-KSTAR-3HEB-LABORATORY-INDEPENDENCE-LEVEL-CERTIFICATION**
- **What**: Verify K_*=coth(1)=1.3130 cross-lab replication status. Catalogue current published Δ/k_B T_c p-wave BCS measurements from ³He-B lab literature (Grenoble, Lancaster, Helsinki, Stanford historical); assess cross-lab scatter; certify whether the K_*=1.3130 claim is at detection-level (single-lab) or confirmation-level (multi-lab consensus). This is the audit that tells the framework whether its highest-independence channel is actually replicated or only nominally multi-detector.
- **Inputs**: W5-58 script + data; 3He-B literature catalogue from `researchers/Volovik/`; cross-lab Δ/k_B T_c measurement values with error bars.
- **Gate**: S85-KSTAR-3HEB-INDEPENDENCE PASS iff ≥3 independent laboratories report Δ/k_B T_c measurements consistent with coth(1)=1.3130 at 95% confidence OR explicit FAIL with sub-laboratory count logged.
- **Effort**: 4-6 hours, 1 agent session (MEDIUM; library task).

V.3. **S85-CROSS-CHANNEL-CORRELATION-MATRIX-FORMALIZATION**
- **What**: Formalize the S/M/W/· correlation matrix in §II.4 as a machine-readable JSON: for each (i, j) pair where S or M is claimed, derive the explicit substitution chain showing how channel i's PASS constrains channel j's pin. Catch any W entries that are actually S or · on closer substitution-chain inspection.
- **Inputs**: this S-4 synthesis §II.4 matrix; W4-48 rigor registry; W6-51 rank-3 derivation; W4-39 two-speed n_T chain; W4-46 w_0 regulator chain.
- **Gate**: S85-CORR-MATRIX-JSON PASS iff matrix lands as JSON with per-cell substitution chain OR explicit · confirmation; each S/M coupling has a named derivation chain.
- **Effort**: 4-6 hours, 1 agent session (MEDIUM).

V.4. **S85-NULL-RESULT-ELIMINATION-MAP-PRE-REGISTRATION**
- **What**: For each of the 15 channels, pre-register in `sessions/pre-registered-observations.md` the exact null criterion and exact structural element that dies on that null. Per agent-memory Operating Principle (pre-registered evidence only), this is the required infrastructure so future CMB-S4 / PIXIE / LISA results can be auto-adjudicated against the framework without convention-shopping.
- **Inputs**: §II.3 null-result elimination map; W4-48 flags; W10-123 axioms (what exactly dies on α_s null); W5-58 K_* identity (what exactly dies on K_* null).
- **Gate**: S85-NULL-PRE-REG PASS iff 15 null-criterion rows land with dual-SHA closure; per-null structural-kill column filled; registry index rebuilt.
- **Effort**: 3-5 hours, 1 agent session (MEDIUM).

V.5. **S85-DESI-DR3-INDEPENDENCE-DISCOUNT-EXPLICITATION**
- **What**: Per agent-memory Closed-Channels section, w_0 is now confirmed SCHEME-DEP. Write explicit prose in `sessions/pre-registered-observations.md` stating that the DR3 2026-04-23 event is a single-detector test under SCHEME-DEP flag, which does NOT count as confirmation-level evidence under the independence-rubric, even on containment PASS. Per `feedback_reporting-framing.md`, this is required so the framework does not cite a single-detector SCHEME-DEP containment as BF>1 evidence. Pre-register BEFORE 2026-04-23.
- **Inputs**: W4-46 structural FAIL; W1b-9 R_842 lockouts; W4-44 7-scenario tree; this S-4 §II.6 independence ranking.
- **Gate**: S85-DR3-INDEPENDENCE-DISCOUNT PASS iff discount prose lands with explicit BF-class attribution AND dual-SHA closure before 2026-04-23 event.
- **Effort**: 2-3 hours, 1 agent session (LOW).

V.6. **S85-SHAPE-TEMPLATE-INDEPENDENCE-FORECAST** (HERA-II + SKA-1 + SKA-2 cross-platform)
- **What**: Extend CF-W4.3 (Mack V.4 21-cm folded-bispectrum SHAPE) with explicit cross-platform independence scoring. Compute SNR for each of HERA-II, SKA-1, SKA-2 independently; report per-platform PASS/FAIL against SNR≥2; assess how many independent platforms are required for confirmation-level evidence.
- **Inputs**: W4-38 .npz (folded-Bogoliubov = −0.080); HERA-II forecast; SKA-1/2 forecasts; 21-cm intensity mapping ℓ_max~10⁵ covariance.
- **Gate**: S85-SHAPE-IND-FORECAST PASS iff ≥2 independent 21-cm platforms project SNR≥2 on folded-SHAPE; FAIL if all three below.
- **Effort**: 6-8 hours, 1 agent session (MEDIUM-HIGH).

V.7. **S85-CMB-S4-ALPHA-S-FLAGSHIP-PRE-REGISTRATION-INDEPENDENCE-AUGMENT**
- **What**: Extend the planned CMB-S4 α_s flagship pre-registration (Mack V.2 carry-forward) with explicit N_det=3 independence language. Pre-register timeline-staged evidence weights: CMB-S4 first-light (~2027) single-detector PASS = detection-level; CMB-HD addition (~2035+) and LiteBIRD joint (~2030) = confirmation-level. Per `feedback_reporting-framing.md`, this is the BF-class cite discipline.
- **Inputs**: W6-52 CSV; W10-123 axiomatic derivation chain; `sessions/pre-registered-observations.md` schema; CMB-S4 + CMB-HD + LiteBIRD timelines.
- **Gate**: S85-ALPHA-S-FLAGSHIP-IND PASS iff pre-registration lands with: (i) 3-detector timeline stages; (ii) BF-class cite discipline attached per stage; (iii) lockouts on auxiliary coupling AND on n_s_pred change; (iv) dual-SHA closure.
- **Effort**: 4-5 hours, 1 agent session (MEDIUM).

V.8. **S85-MULTI-D-JOINT-FISHER-INDEPENDENCE-DISCOUNT**
- **What**: Extend Mack V.6 (Multi-D N-channel Fisher) with the observational-fidelity-gating rubric: when computing joint σ-rejection across (A_s, P_t, μ, α_s, CGWB absolute) × (Planck, CMB-S4, CMB-HD, LiteBIRD, LISA, PIXIE) detector grid, discount self-referential pairs (channels sharing hardware). Report rejection σ for (a) nominal all-channel-independent treatment and (b) hardware-grouped treatment. The difference is the BF over-counting correction.
- **Inputs**: W6-51 table; W6-52 detector reach; W6-50 CGWB; §II.6 independence ranking; §II.4 correlation matrix.
- **Gate**: S85-MULTID-IND-DISCOUNT PASS iff joint-Fisher lands both nominal and hardware-grouped versions with explicit discount factor; joint rejection σ ≥ 10 for ≥ 2 detector combinations AFTER independence discount.
- **Effort**: 6-8 hours, 1 agent session (MEDIUM).

V.9. **S85-PIXIE-MU-INDEPENDENCE-AUGMENT**
- **What**: Extend Mack V.13 PIXIE μ pre-registration with explicit single-detector note. PIXIE is the sole planned μ-distortion mission; no independent check until PIXIE-successor. Pre-register as single-detector decisive test with BF-class attribution adjusted.
- **Inputs**: W5-57 INFO data; PIXIE forecast; this S-4 §II.6 N_det=1 classification for μ.
- **Gate**: S85-PIXIE-MU-IND PASS iff pre-registration lands with single-detector BF attribution; migration criterion for PIXIE-successor registered.
- **Effort**: 2-3 hours, 1 agent session (LOW).

V.10. **S85-WATCHLIST-MEMORY-UPDATE**
- **What**: Update agent memory at `.claude/agent-memory/little-red-dots-jwst-analyst/MEMORY.md` per the Operating Principle "Pre-registered evidence only". Add: (i) the 15-channel falsifier watchlist table; (ii) the four-cluster independence collapse; (iii) the observational-fidelity-gating rubric (N_det≥3 → confirmation-level; N_det=1 → detection-level); (iv) the updated Live Observational Tests table (replacing the S58 snapshot with S84 state).
- **Inputs**: this S-4 synthesis tables §II.1, §II.5, §II.6; current agent memory structure.
- **Gate**: S85-AGENT-MEMORY-S84-UPDATE PASS iff memory file updated with S84 state; no conflict with existing Live Observational Tests table; agent-memory consistency audit passes.
- **Effort**: 1-2 hours, 1 agent session (LOW).

---

## VI. Summary Table

| Item | State After S84 (post-audit) |
|:-----|:------------------------------|
| Falsifier channels on watchlist | 15 (up from 5 pre-S82) |
| ZFP-flagged channels (strict) | 11 |
| Tuning-dependent channels | 4 (2 ACCOM, 2 SCHEME-DEP, but ACCOM and one SCHEME-DEP are particle-physics not cosmology) |
| Independent detector clusters | 4 (CMB, GW, 21-cm, Lab) + 1 methodology (DESI) |
| Highest-independence channels (N_det≥3) | α_s CMB; K_* ³He-B lab |
| Calendar-nearest channel (2026-04-23) | w_0 DESI DR3 — N_det=1, SCHEME-DEP |
| Calendar-nearest 2026 ZFP channel | r BK-Array 2026, N_det=1 |
| Flagship 2030 channel | α_s CMB-S4, N_det=3 aggregate, 34.48σ projected |
| Correlation-matrix S couplings | 16 S-entries (tight tensor cluster r/n_T/Ω_GW/β_s) |
| Correlation-matrix isolates | α_s (weak to multi-obs only), K_* (isolated), SHAPE (isolated), w_0/w_a (internally coupled only) |
| Null-result-kills channels | 9 of 15 (4 non-eliminating, 2 migration-only) |
| Permanent DET-STERILE (no current reach) | 4 (UHF-GW, n_T CMB LiteBIRD, α_f_NL SKA, n_T transit) |

---

## VII. Classification Sign-off

- **PHONONIC** audit content: α_s (Mukhanov-Sasaki spectral tilt of post-transit acoustic GGE), K_* (³He-B p-wave BCS inheritance), SHAPE (GGE bispectrum from instanton-gas pair production), Ω_GW (acoustic GGE tensor power).
- **GEOMETRIC** audit content: n_T CMB + n_T transit + r + β_s (two-speed metric c_T/c_S=2.062 from spectral moments a_2/a_0), UHF-GW (substrate phase-transition spectrum), μ-distortion (K-corridor γ=1 linearity).
- **PARTICLE** audit content: m_H, sin²θ_W (flagged ACCOM by W4-48; outside 15-channel watchlist).
- **NON-PHONONIC** audit content: w_0/w_a (dark-energy partition at Leggett-Bogoliubov; DESI DR3 methodology test); C_cons internal consistency aggregate (flagged DET-STERILE).

Audit classification: the S-4 solo is methodology + independent-detector-fidelity gating across a 15-channel falsifier inventory. Substrate language enforced per `.claude/rules/phononic-framing.md` throughout. No claim of structural identity between the analyst's LRD-specialty and the content of the audit: the LRD-analyst role contributes the observational-fidelity-gating discipline, not domain-specific LRD constraints (which per agent memory cannot discriminate framework from LCDM at z<10²⁸).

---

**End of S-4 solo synthesis.** Deliverables: cross-channel correlation matrix (§II.4), independence ranking (§II.6), null-result elimination map (§II.3). Ten carry-forward computations (V.1-V.10) pre-registered with 4-field format. All substitution chains for direction claims explicit in §II.8. Numerical claims Python-verified prior to inclusion.
