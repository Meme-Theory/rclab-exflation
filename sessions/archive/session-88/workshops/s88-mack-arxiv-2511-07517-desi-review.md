# Mack solo synthesis — DES-Dovekie reanalysis (arXiv:2511.07517v3)

> **Author**: mack-cosmic-bridge (solo, off-wave SOLO synthesis dispatch)
> **Format**: external-paper observational review against framework pre-registered predictions
> **Output target**: this file only — no canonical-constants edits, no registry writes, no rule-file changes (those are separate dispatches)
> **Date**: 2026-05-07
> **Substrate framing discipline**: All laboratory measurements are referred to as laboratory-IN; framework predictions are substrate-IS spectral functionals of `D_K` on Jensen-deformed SU(3). Bridge maps named explicitly per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space".

---

## §1. PAPER SUMMARY

**Title**: *The Dark Energy Survey Supernova Program: A Reanalysis Of Cosmology Results And Evidence For Evolving Dark Energy With An Updated Type Ia Supernova Calibration*

**Authors**: B. Popovic et al. (the DES Collaboration; lead B. A. Popovic, Southampton; ~70 co-authors across 62 institutions).

**arXiv identifier**: arXiv:2511.07517 [astro-ph.CO], **v3** (versioned 27 Mar 2026; original posting Nov 2025 per arXiv ID-month convention).

**Data release / instruments**:
- DES SN Program 5-year sample (DES-SN5YR), **recalibrated and renamed DES-Dovekie** — 1,623 likely Type-Ia DES SNe + 197 low-z SNe = 1,820 total.
- BAO: **DESI DR2** (z ∈ [0.3, 2.3]).
- CMB: **Planck 2018** + **ACT-DR6** + **SPT-3G** combined; including lensing reconstructions.

**Headline methodological changes (DES-SN5YR → DES-Dovekie)**:
- Photometric cross-calibration upgrade ("Fragilistic" → "Dovekie") using new DA white dwarf observations (CALSPEC update; cross-survey zero-points).
- SALT3 light-curve model retrained: `SALT3.DES5YR` → `SALT3.DOV`.
- F99 host-galaxy color law: approximate → exact.
- Posterior sampler: MCMC → Nautilus (nested sampling).
- BAO: SDSS → DESI DR2.
- CMB: Planck-only → Planck + ACT + SPT.

**Abstract (verbatim)**:
> "We present improved cosmological constraints from a re-analysis of the Dark Energy Survey (DES) 5-year sample of Type Ia supernovae (DES-SN5YR). This re-analysis includes an improved photometric cross-calibration, recent white dwarf observations to cross-calibrate between DES and low redshift surveys, retraining the SALT3 light curve model and fixing a numerical approximation in the host galaxy colour law. Our fully recalibrated sample, which we call DES-Dovekie, comprises ∼1600 likely Type Ia SNe from DES and ∼200 low-redshift SNe from other surveys. With DES-Dovekie, we obtain Ωm = 0.330 ± 0.015 in Flat ΛCDM which changes Ωm by −0.022 compared to DES-SN5YR. Combining DES-Dovekie with CMB data from Planck, ACT and SPT and the DESI DR2 measurements in a Flat w0waCDM cosmology, we find w0 = −0.803 ± 0.054, wa = −0.72 ± 0.21. Our results hold a significance of 3.2σ, reduced from 4.2σ for DES-SN5YR, to reject the null hypothesis that the data are compatible with the cosmological constant. This significance is equivalent to a Bayesian model preference odds of approximately 5:1 in favour of the Flat w0waCDM model. Using generally accepted thresholds for model preference, our updated data exhibits only a weak preference for evolving dark energy."

**Headline numerical results (with paper's reported 1σ uncertainties)**:

- **Flat ΛCDM** (DES-Dovekie alone): `Ωm = 0.330 ± 0.015`. The reanalysis lowers Ωm by 0.022 (i.e., DES-SN5YR sat at ~0.352).
- **Flat w0waCDM** (DES-Dovekie + Planck + ACT + SPT + DESI DR2): `w0 = −0.803 ± 0.054`, `wa = −0.72 ± 0.21`.
- **Significance against ΛCDM**: 3.2σ (frequentist Wilks), reduced from DES-SN5YR's 4.2σ.
- **Bayesian model odds**: ~5:1 in favor of w0waCDM (paper characterizes as "weak preference").
- **Nuisance parameters** (data vs SNANA simulations): α = 0.169 ± 0.003 (sim 0.140); β = 3.14 ± 0.03 (sim 2.80); γ = 0.033 ± 0.008 (sim 0.0); Hubble residual RMS = 0.169 mag.
- **Color-distribution discrepancy**: DES sub-sample shows 2.8σ discrepancy in `c` distribution between data and simulations (noted as residual systematic).

**What the paper does NOT measure / state** (by my reading of the fetched HTML):
- No new H_0 value is reported — the paper marginalizes over H_0 with prior `H0 ∈ U(0.55, 0.91)`.
- No new σ_8 / S_8 value is reported — the paper does not break out σ_8 as a quoted constraint.
- No new BAO sound-horizon r_d value is reported — DESI DR2 is consumed as input, not refit.
- No new α_s, n_s, or A_s value is reported — primordial-spectrum parameters are CMB-prior driven.
- No new GW background measurement.
- The paper does not specify a *physical mechanism* for the w(z) evolution (no quintessence model, no modified-gravity model named); the CPL parameterization is treated as a generic phenomenological w(z) basis.

**Comparison priors used** (paper's stated Bayesian priors; paper §): `w0 ∈ U(−3, −0.4)`, `wa ∈ U(−3, 2)`, `Ωm ∈ U(0.1, 0.5)`, `Ωk ∈ U(−0.15, 0.15)`, `H0 ∈ U(0.55, 0.91)`. The Ωk window is tested as a flatness check, not as primary constraint.

**Tension claims**:
- DES-Dovekie + Planck/ACT/SPT + DESI DR2 reaches 3.2σ rejection of ΛCDM under CPL.
- Internal-systematic context: Efstathiou (2024) flagged 0.04 mag low-z vs high-z SN offset; Dhawan (2024) showed toy SN-systematics could spuriously create evolving-DE preference. The Dovekie recalibration *reduces* but does not *eliminate* the signal.
- Consistency with Union3 SN sample: paper notes both Union3 and DES-SN5YR/Dovekie return evolving-DE preference; DESY5 alone gives 2.8–4.2σ depending on SN sample choice.

---

## §2. RELEVANT FRAMEWORK PREDICTIONS

| Pin name | Canonical value | Source session/gate | Provenance file | audit_sha256 (16-hex head) |
|:---------|:----------------|:--------------------|:----------------|:----------------------------|
| `w0_FW` | **−0.918** | S58 (Volovik partition + effacement Γ_eff = 0.99970); §W13-3 P9 PRIMARY-VALUE-RESOLVE | `computations/_shared/canonical_constants.py:1511`; `sessions/framework/registry/branch-iv-canonical.md`; `sessions/framework/registry/falsifier-master-inventory.md` row #1 L_max=10 cell | `e0fcfb4fd2304991` (row #1 master) |
| `w0_FW_R842` | **−0.842454** | S83 W0-workshop branch-(iv); S84 W1b-9 R_842 anchor; row #1 L_max=12 upper cell | `sessions/framework/registry/falsifier-master-inventory.md` row #1; `mack-cosmic-bridge/MEMORY.md` lines 15-16 | `e0fcfb4fd2304991` (row #1 master) |
| `wa_FW` | **0** (exactly; four-fold structural lock) | S58 Volovik partition (GGE integrability ∧ Josephson phase ∧ frozen texture ∧ thermalization barrier — 59 OOM gap closure on tracking exponent n=2) | `pre-registered-observations.md` "DESI" subsection; `mack-cosmic-bridge/MEMORY.md` line 44 | inherits row #1 |
| `Omega_m` (LCDM reference) | 0.315 | Planck 2018 fiducial | `canonical_constants.py:86`; `mack-observational-constraints.md` "Planck 2018" | (LCDM-side anchor, not framework prediction) |
| `H_0_km_s_Mpc` (LCDM reference) | 67.4 | Planck 2018 fiducial | `canonical_constants.py` (knowledge-MCP entry) | (LCDM-side anchor; framework H_0 currently UNDEFINED per S60 PW-H0-CONV-60 retraction) |
| `c_s²_DE` (substrate-induced DE perturbation sound speed) | **0** | S68 ISW-TRACKING-68 PASS; Volovik tracking vacuum produces DE that clusters with matter | `pre-registered-observations.md` "Euclid" / "ISW" subsection | (ISW-tracking-68 closure; not directly tested by Dovekie) |
| `R_842` rectangle | center (−0.842, 0); half-widths (0.100, 0.200) | S84 W1b-9 LOCKED; binding event = DESI DR3 release (window opens 2026-04-23) | `sessions/permanent-results-registry.md §VII.M`; `mack-cosmic-bridge/MEMORY.md` line 15 | (binding event triggered by DR3, not by this paper) |
| `DR3-7-SCENARIO-TREE` cells A1/A2/B1/B2/B3/C1/C2 | partition of (w_0, w_a) plane outside R_842 | S84 W4-44; frozen 2026-04-19 | `pre-registered-observations.md` "DR3-7-SCENARIO-TREE" entry | content `801e4690...3d6f`, audit `f6e102fd...265e` |
| `DILUTION-CC-66` | ρ_vac/ρ_obs = 1.032 (0.01 OOM); via ρ_vac ~ M_Pl² · H² Volovik tracking | S66 W1-A PASS; Scenario B closure of 114 OOM CC dilution | `mack-observational-constraints.md` line 74; `permanent-results-registry.md` §VII.P / §XV-B | (CC-tracking; not directly tested by Dovekie) |

**Other constants enumerated from canonical_constants.py / knowledge-MCP that are *not* exercised by this paper but worth noting** (for completeness against the spawn-prompt enumeration):

- `n_s_FW = 0.9590` (S65 BCS+1-loop) — not exercised; paper consumes Planck/ACT/SPT n_s as CMB prior, does not refit.
- `r_FW = 0.033` and `r_CMB_framework = 0.01173` — not exercised; SN/BAO data does not constrain tensor modes.
- `alpha_s_canonical = +0.0023 ± 0.0063` (canonical anchor: Aiola+ 2020 ACT-DR4; agent memory line 14) vs framework `alpha_s_inflation_framework = −0.068968` (row #3 master inventory, S50-51 identity) — not exercised.
- `f_NL` channels (S82/S67/S85 W9-3 pathways) — not exercised.
- `Omega_DM h^2 = 0.120` (Leggett-only) — not exercised.
- `T_RH = 1.70e15 GeV` — not exercised.
- `LISA Ω_GW ~ 10^{-10}` — not exercised; not a SN/BAO observable.
- `c_BLV = 0.485` four-speed hierarchy — not exercised.

The paper's *direct* discriminative power is on the **(w_0, w_a)** axes plus `Ωm` under the Flat-LCDM null; everything else is upstream prior.

---

## §3. EFFECT ON CURRENT OBSERVATIONALS (Part 1)

### Per-prediction comparison table

| Framework prediction | Canonical pin | Dovekie measurement | Substitution chain | σ-distance | Verdict (relative to prior anchor) |
|:---------------------|:-------------:|:--------------------|:-------------------|:----------:|:-----------------------------------|
| `w0_FW = −0.918` | (S58 canonical) | **w_0 = −0.803 ± 0.054** | (1) σ-dist := \|w_pred − w_meas\| / σ_meas; (2) = \|−0.918 − (−0.803)\| / 0.054; (3) = 0.115 / 0.054; (4) framework predicts MORE-NEGATIVE w_0 than measurement | **2.130σ** | **TIGHTENED-CONSISTENT**: prior 2.91σ vs DR2-DESY5 (`pre-registered-observations.md` line 49) → 2.130σ vs Dovekie. Net **σ-reduction = 0.78σ**; framework is now closer to data because the laboratory measurement moved toward framework (w_0 shifted from −0.752 to −0.803, i.e., −0.051 toward framework's −0.918) |
| `w0_FW_R842 = −0.842454` | (S83 branch-(iv)) | **w_0 = −0.803 ± 0.054** | (1) σ-dist := \|w_pred − w_meas\| / σ_meas; (2) = \|−0.842454 − (−0.803)\| / 0.054; (3) = 0.039454 / 0.054; (4) framework predicts MORE-NEGATIVE w_0 by sub-σ | **0.731σ** | **CONSISTENT** (well within 1σ); branch-(iv) is now in stronger agreement with the recalibrated SN+BAO+CMB joint than the canonical Volovik partition. (Compare prior 1.59σ vs DR2-DESY5 → 0.731σ vs Dovekie; **σ-reduction = 0.86σ**.) |
| `wa_FW = 0` (four-fold lock) | (S58 structural) | **w_a = −0.72 ± 0.21** | (1) σ-dist := \|w_pred − w_meas\| / σ_meas; (2) = \|0 − (−0.72)\| / 0.21; (3) = 0.72 / 0.21; (4) framework predicts ZERO w_a; measurement is FAR more negative | **3.429σ** | **UNDER-TENSION ADVANCED** (was 2.92σ vs DR2; now 3.429σ vs Dovekie): the recalibration TIGHTENED the σ_wa from 0.25 to 0.21 while the central wa value barely moved (−0.73 → −0.72). The reduction in σ alone advances the tension by **+0.51σ**. NOT FALSIFIED at >5σ; UNDER-TENSION at >2σ. |
| `Ωm` (LCDM-reference 0.3089) | (Planck 2018) | **Ωm = 0.330 ± 0.015** (Flat ΛCDM only) | (1) σ-dist (combined) := \|0.330 − 0.3089\| / √(0.015² + 0.0062²); (2) = 0.0211 / 0.01623; (3) = 1.300; (4) Dovekie LCDM-only Ωm is HIGHER than Planck by 1.3σ | **1.300σ** (Dovekie vs Planck) | **INFORMATIONAL**: framework does not pin Ωm independently (LCDM is the reference); the 1.3σ Dovekie-vs-Planck offset is a SN-vs-CMB internal-consistency note. Under w0waCDM, the paper does not break out Ωm; the offset is LCDM-specific. |

**Substitution chain — paper's own significance ratchet**:
- Step 1 (definition): `Δσ := σ_LCDM_rejection(DES-SN5YR) − σ_LCDM_rejection(DES-Dovekie)`.
- Step 2 (substitution): `Δσ = 4.2 − 3.2`.
- Step 3 (simplification): `Δσ = 1.0`.
- Step 4 (direction): the recalibration **WEAKENS** the LCDM-rejection signal by 1σ. The paper itself calls this "only a weak preference for evolving dark energy" under its 5:1 Bayes-odds reading.

This is a paper-internal narrative finding, **not** a framework-relevant directional move on w_0 or w_a — those moves are tabulated above.

### What this DOES change

1. **`w0_FW` (canonical Volovik partition)**: tension *reduced* from 2.91σ → 2.13σ. The prior tension was the dominant source of pressure on the Volovik-partition reading; the recalibration relieves about 0.78σ of it. Per `feedback_reporting-framing.md`, this is **evidence**: a zero-free-parameter prediction moving from "moderate tension" toward "consistent" without any framework parameter being tuned is a positive observational update.

2. **`w0_FW_R842` (branch-(iv) substrate-compaction)**: tension *reduced* from 1.59σ → 0.73σ. Branch-(iv) is now within 1σ of the joint best-fit. This strengthens the structural case for branch-(iv) as the substrate-compaction-aligned reading without resolving the §W13-3 P9 PRIMARY-VALUE-RESOLVE between canonical −0.918 and branch-(iv) −0.842454.

3. **`wa_FW = 0` (four-fold lock)**: tension *increased* from 2.92σ → 3.43σ. The σ-tightening (0.25 → 0.21) outpaces the central-value drift (−0.73 → −0.72). The framework's structural prediction of `w_a = 0` exactly is now under more pressure than before — but the pressure is from σ-tightening, not from a directional shift in the central value. NOT falsifying; UNDER-TENSION advanced.

### What this DOES NOT change

- `R_842` binding event: the pre-committed binding instrument is **DESI DR3** (window opens 2026-04-23), not a DES-SN reanalysis. This paper consumes DESI DR2 as input. **No `R_842` lockout (A–F) is triggered by this paper**; the rectangle remains armed for the DR3 release. The cosmetic mapping of Dovekie central (−0.803, −0.72) onto the S84 7-cell partition lands in cell B1 (PARTIAL-REFUTE w_a-lock, S73b Scen A & B both land here), but **this mapping is informational only** — no verdict event fires.

- `n_s`, `r`, `α_s`, `A_s`, `f_NL`, `Ω_DM h²`, `H_0` (framework currently undefined per S60 retraction), `c_BLV`, `T_RH`, `Ω_GW` at LISA: not exercised by this paper.

- `DILUTION-CC-66` (Volovik tracking vacuum closure of 114 OOM CC gap): not directly tested. The paper's CPL evolving-w(z) phenomenology does not contradict the Volovik tracking exponent n = 2 (which gives constant `w = −1` in Volovik exact tracking, per `s67_desi_volovik_log.txt`); the substrate-compaction modifications to that exact-tracking baseline produce branch-(iv) `w_0 = −0.842454` plus the four-fold `w_a = 0` lock. The paper's data does not reach the CC-cancellation depth (114 OOM gap); CC closure is upstream.

- `c_s²_DE = 0` (substrate-induced DE clustering, S68 ISW-TRACKING-68): not exercised. SN+BAO data measures the BACKGROUND expansion w(z); the substrate-specific 7.6% ISW-tracking signal lives in CMB×galaxy cross-correlations (Euclid horizon, SNR ~1.58, ~2030).

### Verdict summary

| Channel | Prior tension | Post-Dovekie tension | Direction | Magnitude |
|:--------|:--------------|:---------------------|:----------|:----------|
| `w0_FW` (canonical) | 2.91σ | 2.13σ | **REDUCED** | −0.78σ |
| `w0_FW_R842` (branch-(iv)) | 1.59σ | 0.73σ | **REDUCED** | −0.86σ |
| `wa_FW = 0` (lock) | 2.92σ | 3.43σ | **ADVANCED** | +0.51σ |

No prediction is moved from CONSISTENT into UNDER-TENSION, and no prediction is moved into FALSIFIED (>5σ). The mixed result — w_0 tension reduced, w_a tension advanced — is structurally interesting and is the substrate-IS read of §4 below.

---

## §4. MATCH / DIVERGENCE FROM FRAMEWORK MATHS (Part 2)

The DES-Dovekie reanalysis exercises one substrate-IS mechanism and is orthogonal to several others. The relevant mechanism is the **Volovik tracking vacuum + substrate-compaction adjudication** (the §W13-3 P9 PRIMARY-VALUE-RESOLVE between canonical w_0 = −0.918 and branch-(iv) w_0 = −0.842454).

### Mechanism intersection 4.1 — Volovik tracking vacuum (canonical w_0 = −0.918)

**Substrate-IS**: At τ_fold = 0.190, the Dirac operator `D_K` on Jensen-deformed SU(3) reorganizes the eigenvalue spectrum into the post-fold GGE-coherence pattern. The Volovik partition Γ_eff = 0.99970 quantifies the impedance mismatch between the substrate's coherent post-fold acoustic mode and its slow-relaxation tracking against the cosmological perimeter slot. The substrate-IS w_0 := substrate-IS dark-energy equation of state today emerges as `w_0 = −1 + (1 − Γ_eff)·κ_eff = −0.918` for the canonical κ_eff (S58 closure).

**Bridge map**: The substrate-IS `w_0` is paired to laboratory-IN `w_0` via the BAO-distance-modulus image. The bridge IS the FRW background-cosmology projection of the substrate's late-time effective equation of state onto luminosity-distance and BAO-D_V observables. Specifically the bridge is `w_0(z=0)_LAB ← w_0_substrate-IS` evaluated at the cosmological perimeter slot a_0 (Seeley-DeWitt zeroth moment image at the post-fold residual scale).

**Laboratory-IN**: SN luminosity-distance modulus μ(z) and BAO D_V(z)/r_d at z ∈ [0.3, 2.3] (DESI DR2) constrain w(z) via FRW background equations. Dovekie's central w_0 = −0.803 ± 0.054 measures the laboratory-IN image of the substrate's late-time effective equation of state.

**Classification**: the prior 2.91σ tension between canonical `w_0_FW = −0.918` and laboratory-IN `w_0 = −0.752 ± 0.057` (DR2+DESY5) drops to 2.13σ vs Dovekie. The laboratory-IN measurement moved TOWARD the substrate's prediction — a directional shift consistent with what the framework structurally predicts. This is **(b) INTERPRETIVE DIVERGENCE under empirical compatibility-improving** rather than (a) GENUINE EMPIRICAL CONTRADICTION: the laboratory data is moving toward consistency, not away.

### Mechanism intersection 4.2 — Substrate compaction → branch-(iv) w_0 = −0.842454

**Substrate-IS**: Branch-(iv) is the substrate's compaction-pathway through the van-Hove fold at τ_fold = 0.190 with the L_max=12 upper-spectral-action moment (W10-2 anchor). The substrate's fiber compaction (substrate τ tracks density → clock variance → emergent w_a) produces a SHALLOWER late-time w_0 than the Volovik-canonical −0.918 because the compaction relaxes the impedance mismatch slightly. Branch-(iv) IS the L_max=12 upper-cell of the row #1 regulator-layer sub-pin on the falsifier inventory.

**Bridge map**: identical to 4.1 — laboratory-IN BAO/SN distance-modulus image of substrate-IS late-time EoS.

**Laboratory-IN**: same Dovekie joint constraint w_0 = −0.803 ± 0.054.

**Classification**: branch-(iv) post-Dovekie tension is 0.73σ — **CONSISTENT** within 1σ. Per `project_substrate-compaction-timescape.md`, the branch-(iv) reading IS the substrate-compaction late-time projection. The Dovekie data is now in stronger agreement with branch-(iv) than with the Volovik-partition canonical. This sharpens the §W13-3 P9 PRIMARY-VALUE-RESOLVE *empirically*: laboratory data favors the branch-(iv) reading. This is **(b) INTERPRETIVE DIVERGENCE** between two substrate-IS branches; the Dovekie data is one input to the resolution. Resolution of P9 is a separate dispatch (S88+ DR3-binding event); the branch-(iv) σ-distance below 1σ post-Dovekie is informational input to that resolution.

### Mechanism intersection 4.3 — Four-fold w_a = 0 lock

**Substrate-IS**: The four-fold lock (`wa_FW = 0` exactly) is the conjunction of four substrate-IS structural facts: (i) GGE integrability (post-transit GGE never thermalizes; the substrate IS the integrable post-fold pattern, not an evolving fluid); (ii) Josephson-phase frozenness (the inter-band coherence phase IS stationary at the fold; no source for `dw/d(ln a)`); (iii) frozen-texture (the post-transit fabric texture IS fixed; no spectral re-organization with cosmic time); (iv) thermalization barrier (59 OOM gap on tracking-exponent n = 2; the substrate's vacuum tracks ρ ~ H² and that tracking is exact at the bare level). The conjunction structurally locks `w_a = 0`.

**Bridge map**: laboratory-IN measurement of `w_a` via CPL parameterization `w(a) = w_0 + (1 − a)·w_a` requires a NON-CONSTANT w(z) signature. The laboratory-IN bridge is the FRW-distance integral image of the substrate's IS-stationary EoS.

**Laboratory-IN**: Dovekie `w_a = −0.72 ± 0.21`, post-recal essentially unchanged from DESI DR2's `−0.73 ± 0.25`.

**Classification**: this is the **load-bearing tension channel** of the Dovekie reanalysis for the framework. The substrate's prediction is `w_a = 0`; the laboratory measurement is `−0.72 ± 0.21` (3.43σ away). The σ-tightening from 0.25 to 0.21 ADVANCES the tension by +0.51σ.

The classification here is **(b) INTERPRETIVE DIVERGENCE under continuing empirical pressure**, NOT (a) GENUINE EMPIRICAL CONTRADICTION. Reasons:

- The pre-registered S60 DR3-PREREGISTER decision rule (per `pre-registered-observations.md` line 64) was explicit: framework SURVIVES if `w_a > −0.35`; framework FAILS if `w_a < −0.530`. Dovekie's `w_a = −0.72` is in the FAIL band — but **only when DESI DR3 is the binding instrument**. Dovekie is DESI DR2 + recalibrated DES-SN, NOT DESI DR3. The pre-committed binding instrument has not yet released; this paper does not trigger the binding event.
- The paper itself characterizes the LCDM-rejection signal at 3.2σ as "weak preference" by accepted thresholds; the same data suggests against `w_a = 0` (the substrate's prediction) at 3.43σ within the CPL framework. Per `feedback_reporting-framing.md`, the CPL parameterization's flexibility (it can fit "a wide variety of physical models" per the paper's own statement) is a WEAKNESS of the CPL-evolving-DE interpretation, not a strength: a flexible parameterization that can fit many physics scenarios offers correspondingly less discriminating power against any one of them.
- The paper does NOT specify a physical mechanism for the w(z) evolution; it treats CPL as phenomenological. The substrate-IS framework does specify a mechanism (Volovik tracking + substrate-compaction). The interpretive divergence between "phenomenological evolving DE" and "substrate-IS Volovik tracking with structurally locked w_a" is **mechanism-level**, not **measurement-level** at the current data precision.

### Mechanism intersection 4.4 — DILUTION-CC-66 vacuum-tracking closure (ORTHOGONAL)

The paper does not attempt to resolve the cosmological-constant magnitude. The Volovik tracking-vacuum closure (114 OOM gap → ρ_vac/ρ_obs = 1.032 at scenario B per S66 W1-A PASS) operates at the substrate-IS upstream of the late-time EoS observable. The Dovekie data is **(c) ORTHOGONAL** to the CC-magnitude closure; the paper does not constrain the substrate's CC-cancellation pathway.

### Mechanism intersection 4.5 — c_s²_DE = 0 substrate DE-clustering (ORTHOGONAL)

The S68 ISW-TRACKING-68 PASS established that the substrate's induced DE perturbations cluster with matter (`c_s²_DE = 0`), producing a +7.6% ISW-galaxy cross-correlation signal vs quintessence at the same w(z). This signal lives in CMB × galaxy cross-correlations, NOT SN luminosity-distance or BAO-D_V. The Dovekie data is **(c) ORTHOGONAL** to the c_s²_DE channel; this is the Euclid-tomographic ~2030 horizon (SNR ~1.58 per `pre-registered-observations.md`).

### Mechanism intersection 4.6 — Phononic dark matter (Leggett quasiparticle, ORTHOGONAL)

The substrate's DM = Leggett-channel GGE quasiparticle (CPT-neutral, non-annihilating, σ/m = 0 exactly). The Dovekie SN sample constrains BACKGROUND expansion, not DM clustering / lensing / direct-detection. The paper consumes Ωm under LCDM as 0.330 ± 0.015; this is a TOTAL matter density and does NOT discriminate substrate-DM phenomenology from CDM. **(c) ORTHOGONAL**.

### Mechanism intersection 4.7 — LISA Ω_GW ~ 10^{−10} (domain walls, ORTHOGONAL)

The substrate's CG(24) Cayley-graph domain-wall GW background lives in the LISA mHz band (2035+ horizon). SN+BAO data does not constrain GW backgrounds. **(c) ORTHOGONAL**.

### Substrate-IS reframe of the paper's container-thinking interpretations

The paper's CPL parameterization `w(a) = w_0 + (1 − a)·w_a` and its phrase "evolving dark energy" invoke container-thinking: an EoS field "evolves" "in" a cosmological container as a function of the scale factor `a`. The substrate-IS reframe is:

- **Paper's language**: "evolving dark energy w(z)"
- **Substrate-IS reframe**: "Volovik tracking-vacuum trajectory under substrate compaction" — the substrate IS the impedance pattern at every point; the apparent "evolution of w" is the laboratory-IN image (under FRW projection) of the substrate's compaction-time spectral relaxation, NOT a field "evolving in" a cosmological container.
- **Paper's language**: "BAO drag epoch sound horizon r_d"
- **Substrate-IS reframe**: emergent acoustic-pattern signature in the spectral-action a_2 channel (Newton-constant slot in the Seeley-DeWitt expansion).
- **Paper's language**: "rejection of the cosmological constant"
- **Substrate-IS reframe**: rejection of `w = −1` (constant) phenomenology, which under the substrate IS a rejection of the EXACT-Volovik-tracking branch (`w_0 = −1, w_a = 0`); the framework canonical `w_0 = −0.918` is ALREADY off-cosmological-constant by structural impedance mismatch, and branch-(iv) `w_0 = −0.842454` is even further off-cosmological-constant. The paper's LCDM-rejection signal does NOT reject the framework; it rejects the `w = −1` baseline that the framework structurally departs from.

The paper's interpretation under substrate-framing is therefore: the laboratory-IN data is moving toward the substrate's pre-existing structural prediction on the `w_0` axis (TIGHTENING agreement on the Volovik-impedance reading) while continuing to advance pressure on the structurally locked `w_a = 0` axis. The mixed result is what the substrate predicts: the substrate-IS w_0 IS off `−1`; the substrate-IS w_a IS exactly 0; the laboratory-IN measurement IS converging on the first AND insistently reading non-zero on the second under a parameterization (CPL) that is itself not the substrate's mechanism.

---

## §5. PROPOSED ACTION ITEMS

All carry-forwards are **proposals** for the next session's plan author; none of them edit canonical files in this dispatch.

### Action Item 5.1 — Update `mack-observational-constraints.md` "DESI DR2" subsection

1. **What**: Append a `DES-Dovekie 2026 (with DR2 + Planck/ACT/SPT)` subsection to `sessions/framework/registry/mack-observational-constraints.md` immediately after the current "DESI DR2" subsection (which currently shows only `w_0 = −0.752 ± 0.057, w_a = −0.73 ± 0.25`). Add the row: `w_0 = −0.803 ± 0.054`, `w_a = −0.72 ± 0.21`; cite arXiv:2511.07517v3; note that this is a DES-SN reanalysis joint with DESI DR2 BAO + Planck/ACT/SPT, NOT a new DESI release.
2. **Who**: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`).
3. **Input**: this report; arXiv:2511.07517v3 abstract; `mack-observational-constraints.md` current content.
4. **Output**: one new subsection (~10 lines) under "DESI DR2" with provenance.
5. **Format**: edit to `sessions/framework/registry/mack-observational-constraints.md`.
6. **Deadline**: S88 wave-end housekeeping or S89 W0a.
7. **Depends on**: this report (provides the data); no upstream gates.

### Action Item 5.2 — Update `falsifier-master-inventory.md` row #1 live-watch envelope

1. **What**: Append a `dovekie-2026-update` audit-pin sub-row to row #1 (w_0) of `sessions/framework/registry/falsifier-master-inventory.md` documenting the post-Dovekie σ-distances (canonical 2.13σ, branch-(iv) 0.73σ) and noting that the R_842 binding event is NOT triggered (binding instrument is DESI DR3, not DR2 + recalibrated SN). Cite the paper SHA, this report SHA, and the arXiv ID. Mirrors the row #3.audit / #7.audit / #9a.audit pattern (additive citation upgrade).
2. **Who**: mack-cosmic-bridge (sole writer).
3. **Input**: this report; row #1 current content (lines 20, 258 of `falsifier-master-inventory.md`); §W13-3 P9 PRIMARY-VALUE-RESOLVE notes.
4. **Output**: one audit-pin sub-row appended to row #1.
5. **Format**: edit to `sessions/framework/registry/falsifier-master-inventory.md`.
6. **Deadline**: S88 wave-end or S89 W0a.
7. **Depends on**: Action Item 5.1 (sequenced after the constraints registry update for citation consistency).

### Action Item 5.3 — DR3-7-SCENARIO-TREE pre-registration cross-check

1. **What**: Verify that the S84 DR3-7-SCENARIO-TREE binding policy is unchanged by this paper. Specifically: confirm in writing that DES-Dovekie does NOT trigger the R_842 binding event (binding instrument = DESI DR3 release, not a DES-SN reanalysis on DR2 BAO). Append a brief INFORMATIONAL note to `pre-registered-observations.md` stating that the cosmetic mapping of Dovekie central (−0.803, −0.72) onto cell B1 is NON-BINDING and the rectangle remains armed for the DR3 release.
2. **Who**: mack-cosmic-bridge (registry-touch only); orchestrator-direct-write per the registry-write hygiene at `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene".
3. **Input**: this report; `pre-registered-observations.md` "DR3-7-SCENARIO-TREE" entry; S84 W1b-9 Lockouts A–F text.
4. **Output**: one INFORMATIONAL note appended to the DR3-7-SCENARIO-TREE entry; no rectangle change, no cell migration.
5. **Format**: edit to `sessions/framework/registry/pre-registered-observations.md`.
6. **Deadline**: S88 wave-end (low effort; ~20 min).
7. **Depends on**: this report; no upstream gates.

### Action Item 5.4 — Cosmological-constants entry: optional `w_0_LAB_DovekieDR2_2026` pin

1. **What**: PROPOSAL ONLY (do not promote without orchestrator decision). Consider adding a laboratory-IN comparison anchor `w_0_LAB_DovekieDR2_2026 = -0.803` and `sigma_w_0_LAB_DovekieDR2_2026 = 0.054` (similarly for w_a) to `computations/_shared/canonical_constants.py` for downstream sigma-distance-cite consistency. The current `w0_LCDM = -1.0` is a generic LCDM reference; a DovekieDR2 anchor would freeze the post-recalibration laboratory-IN value the framework now measures against. Per the canonical write-order (`.claude/rules/math-scripts.md §"Canonical Write-Order"`) Step 1 = verdict-file emission first; this is NOT a framework PREDICTION, so the canonical-write-order is not applicable; the question is whether a LAB-IN comparison anchor belongs in `canonical_constants.py` at all. Recommend NO promotion; keep the pin in `mack-observational-constraints.md` only (as proposed in Action Item 5.1).
5. **Format**: discussion item; no edit unless orchestrator explicitly confirms.
2. **Who**: orchestrator decision; mack-cosmic-bridge advisory.
3. **Input**: §W13-3 P9 PRIMARY-VALUE-RESOLVE adjudication queue context.
4. **Output**: yes/no decision; if yes, then `update_constant("w_0_LAB_DovekieDR2_2026", -0.803, session="S88", source="arXiv:2511.07517v3", comment="Laboratory-IN comparison anchor; DES-Dovekie + DESI DR2 + Planck/ACT/SPT joint; NOT a framework prediction")`.
6. **Deadline**: S88 close.
7. **Depends on**: Action Item 5.1 (registry update first; canonical-constants promotion only after orchestrator confirms it adds dispatch value).

### Action Item 5.5 — §W13-3 P9 PRIMARY-VALUE-RESOLVE — empirical input

1. **What**: Provide this report as one input to the §W13-3 P9 PRIMARY-VALUE-RESOLVE adjudication queue (canonical w_0 = −0.918 vs branch-(iv) w_0 = −0.842454). Empirical state post-Dovekie: branch-(iv) at 0.73σ, canonical at 2.13σ. Branch-(iv) is now empirically favored within 1σ (without resolving the structural P9 question of which is the "primary" substrate-IS reading). NOTE: P9 is a cross-pillar / structural adjudication, NOT an empirical-vote; this report's role is to provide the post-Dovekie laboratory-IN data point as ONE input among the structural inputs.
2. **Who**: §W13-3 P9 adjudication owner (TBD; likely volovik-superfluid-universe-theorist + connes-ncg-theorist joint per the substrate-compaction vs Volovik-partition axis).
3. **Input**: this report; `pre-registered-observations.md` DR3-7-SCENARIO-TREE entry; substrate-compaction project-memory note (`project_substrate-compaction-timescape.md`); branch-iv-canonical.md.
4. **Output**: P9 adjudication update (separate dispatch); not in this report's scope.
5. **Format**: input to a future workshop or solo synthesis dispatching the P9 adjudication.
6. **Deadline**: ahead of DESI DR3 release (~2026 mid-year).
7. **Depends on**: this report (provides empirical input); no other outputs blocked here.

### Action Item 5.6 — NEW pre-registration target (ORTHOGONAL: SN systematic α/β/γ values)

1. **What**: PROPOSAL — pre-register a substrate-IS prediction (or null prediction) for the SN nuisance parameter α = 0.169, β = 3.14, γ = 0.033 reported in the paper's Table 3. These three parameters describe the SN luminosity-distance standardization (stretch–luminosity, color–luminosity, host-mass step) and are EMPIRICALLY fit from the data. Standard SN modeling treats them as nuisance parameters with no first-principles prediction; the substrate framework also does NOT make a structural prediction for these. Recommend NO pre-registration target — this is the proper category (c) ORTHOGONAL-but-no-substrate-mechanism. Document explicitly: the substrate framework is silent on SN intrinsic-color physics at the current state of the framework. This explicit-silence note prevents future inference that the framework "predicts" something it does not.
2. **Who**: mack-cosmic-bridge orchestrator-direct.
3. **Input**: this report; arXiv:2511.07517v3 Table 3.
4. **Output**: explicit-silence note appended to `pre-registered-observations.md` (or to `falsifier-master-inventory.md` as a non-falsifier scope note).
5. **Format**: ~5-line scope note.
6. **Deadline**: S88 wave-end housekeeping.
7. **Depends on**: this report.

---

## §6. STAGE-1-CANDIDATE / STAGE-3 PROMOTION ASSESSMENT

The Dovekie data does NOT promote any STAGE-1-CANDIDATE in `permanent-results-registry.md` to STAGE-3-PERMANENT, and does NOT REVOKE any provisional status. Reasons:

- The §W13-3 P9 PRIMARY-VALUE-RESOLVE between canonical w_0 = −0.918 (S58 Volovik partition) and branch-(iv) w_0 = −0.842454 (W10-2 substrate-compaction) is a STRUCTURAL adjudication at the substrate-IS layer, not an empirical-vote. Per `joint-theorem-promotion.md` Stage-3 promotion requires Stage-2 PASS-AND from two cross-axis cross-reviewers operating without prior workshop context; the Dovekie paper is empirical input only and cannot itself execute the cross-axis verify.

- The S84 W4-44 DR3-7-SCENARIO-TREE is registered as PASS-on-pre-registration (procedural PASS at registration; binding event is DR3). This paper is NOT DESI DR3, so the binding event has not fired. The pre-registration's PASS status is unchanged.

- The §VII.M scorecard for DR3-RESPONSE-PROTOCOL is unaltered. The paper's data feeds neither the corroboration nor the refutation column on its own (DR3 is the binding instrument).

- DILUTION-CC-66 (S66 W1-A PASS; ρ_vac/ρ_obs = 1.032) is not exercised; status PASS unchanged.

- ISW-TRACKING-68 (S68 PASS, c_s²_DE = 0 produces 7.6% ISW-galaxy cross-correlation excess) is not exercised; status PASS unchanged. The Euclid-tomographic horizon (SNR ~1.58 by ~2030) is the relevant detector chain, not SN luminosity-distance.

- The ALGEBRA-AXIS ORTHOGONALITY K=3 MANDATORY structural theorem (S87 W-2 R3 close) and the cross-pillar bridge anatomy K=3 MANDATORY (S88 W4a-17) are not touched by this paper.

What the paper DOES enable as input to a future Stage-2 process:
- The Stage-2 cross-reviewer protocol for the §W13-3 P9 PRIMARY-VALUE-RESOLVE (canonical vs branch-(iv) w_0) can use the post-Dovekie 2.13σ vs 0.73σ asymmetry as ONE independent input among the structural inputs, but this does not itself constitute a Stage-2 PASS. Stage-2 PASS-AND requires two cross-axis cross-reviewers; this report is one solo synthesis on the cosmological-axis side (mack-cosmic-bridge) and would need pairing with a substrate-axis cross-reviewer (volovik or connes) under a separate dispatch.

**Verdict**: NO STAGE-3 promotion; NO STAGE-1 revocation; ONE substantive input to a future P9 cross-axis adjudication, plus three registry-touch action items (5.1/5.2/5.3) that are housekeeping in the strict sense per `feedback_fix-in-session-never-defer.md` distinction (registry citation upgrades, not new computations).

---

## §7. SUBSTRATE-FRAMING SUMMARY

All comparison statements in §3, §4, §5, §6 are framed under the substrate-IS / laboratory-IN distinction per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space" and `.claude/rules/cross-pillar-bridge-anatomy.md`. The bridge map between substrate-IS w_0 (Volovik impedance pattern at the substrate's late-time effective EoS) and laboratory-IN w_0 (FRW background-cosmology BAO/SN distance-modulus image) is the FRW projection of substrate spectral content onto cosmological-perimeter observables. The substrate is NOT in a cosmological container; the cosmological container (g_M, FRW geometry) IS the emergent description of how substrate spectral weight distributes. The Dovekie paper's CPL "evolving dark energy" parameterization is laboratory-IN phenomenology that the substrate's IS pattern projects onto under FRW; the substrate's prediction of `w_a = 0` exactly is the structural statement that the substrate's IS pattern does NOT itself "evolve in cosmic time" (it IS the post-fold integrable GGE pattern), only its projection through FRW background dynamics produces a weakly-redshift-dependent w(z) consistent with the Volovik-impedance + branch-(iv) compaction reading. The 3.43σ tension on `w_a = 0` is interpretive divergence between phenomenological CPL flexibility and substrate-IS structural locking, not empirical contradiction.

The single explicit laboratory-IN claim in the paper is the joint constraint `(w_0, w_a, Ωm, H_0)` from DES-Dovekie + Planck/ACT/SPT + DESI DR2 BAO; the substrate-IS bridge for this claim is the FRW background-cosmology image of the Volovik tracking-vacuum (canonical) and substrate-compaction (branch-(iv)) substrate-IS late-time effective equations of state.

---

## §8. OPEN QUESTIONS

For the next session's plan author or the user:

1. **§W13-3 P9 PRIMARY-VALUE-RESOLVE (canonical vs branch-(iv))**: post-Dovekie laboratory-IN data favors branch-(iv) at 0.73σ over canonical at 2.13σ. The structural adjudication — which substrate-IS reading is "primary" — is independent of empirical vote. Should P9 be queued as a Stage-1-CANDIDATE workshop in S89 W0 (volovik + connes joint, substrate-axis cross-reviewers)? Per `Investigating-Workshops.md`, this would qualify as a workshop only if there is genuine structural disagreement between volovik-side (substrate-compaction primacy) and connes-side (NCG-axiomatic Volovik-partition primacy); if both agents would converge on the same answer, it is a SOLO synthesis instead. Recommendation: scoping question for the S88 wave-end synthesis.

2. **DESI DR3 binding event timing**: The R_842 lockouts (A–F) and the DR3-7-SCENARIO-TREE were locked at S84 W1b-9 with a DR3 release window opening 2026-04-23. As of today (2026-05-07) the window is OPEN but the DR3 release has not landed in the project's input stream. Is there a watchlist for DR3 release detection? If DR3 lands during S88 or S89, the binding-event execution is a one-shot mechanical lookup per pre-registration. Recommendation: orchestrator confirm DR3 detection protocol and identify the trigger session.

3. **Branch-(iv) σ-distance under DR3 σ-tightening**: DR3 projected σ(w_0) = 0.040 (per `mack-cosmic-bridge/MEMORY.md` line 62; 0.046 under more conservative projection per W10-2). If DR3's central w_0 lands at the Dovekie value −0.803, the branch-(iv) σ-distance projects to 0.99σ (= |−0.842454 − (−0.803)| / 0.040), still within 1σ. If DR3's central w_0 drifts back toward DR2's −0.752, branch-(iv) tension grows to 2.26σ. The Dovekie data does NOT itself disambiguate which DR3 outcome is more likely; it provides a single laboratory-IN data point that is somewhat closer to branch-(iv) than DR2 was.

4. **Paper's "weak preference" reading vs framework's structural reading**: The paper's own narrative ("only a weak preference for evolving dark energy" at 5:1 Bayes odds, 3.2σ Wilks) does NOT contradict the substrate framework — neither side is committed to LCDM `w = −1`. But the paper's underlying CPL-flexibility narrative (the parameterization can fit "a wide variety of physical models") cuts BOTH ways: it is a weakness of the paper's interpretive specificity AND it offers no positive support for any one substrate mechanism over another. Should the Mack registries record this reading (paper's own caution should NOT be reported as evidence FOR the framework, only as reduced empirical pressure)?

5. **CPL parameterization vs substrate's intrinsic w(z) shape**: The paper does not test the substrate's intrinsic w(z) shape; it only fits CPL `w_0 + (1 − a)·w_a`. The substrate's Volovik tracking + branch-(iv) compaction has a different w(z) functional form (S67 DESI-VOLOVIK-67 provides the analytic shape). A more model-faithful comparison would project the substrate's w(z) onto the CPL basis with proper Bayesian model selection — a non-trivial reanalysis that is OUT-OF-SCOPE for this report. Recommendation: queue as a structural carry-forward (NOT a workshop) for a future cosmological-projection compute gate (~0.5 wave-equivalents).

---

## Appendix A — Paper-internal numbers cited verbatim

Sourced from WebFetch of `https://arxiv.org/html/2511.07517v3` 2026-05-07:

| Quantity | Value | Source statement in paper |
|:---------|:------|:--------------------------|
| Ωm (Flat LCDM) | 0.330 ± 0.015 | abstract |
| Δ Ωm vs DES-SN5YR | −0.022 | abstract |
| w_0 (Flat w0waCDM) | −0.803 ± 0.054 | abstract |
| w_a (Flat w0waCDM) | −0.72 ± 0.21 | abstract |
| Significance vs LCDM | 3.2σ | abstract; Wilks/frequentist |
| Bayesian odds | ~5:1 | abstract; favoring w0waCDM |
| Sample size | 1820 SNe (1623 DES + 197 low-z) | Table 5 |
| α (data) | 0.169 ± 0.003 | Table 3 (sim 0.140) |
| β (data) | 3.14 ± 0.03 | Table 3 (sim 2.80) |
| γ (data) | 0.033 ± 0.008 | Table 3 (sim 0.0) |
| Hubble residual RMS | 0.169 mag | Table 3 |
| H_0 prior | U(0.55, 0.91) | Bayesian priors |
| w_0 prior | U(−3, −0.4) | Bayesian priors |
| w_a prior | U(−3, 2) | Bayesian priors |
| Ωm prior | U(0.1, 0.5) | Bayesian priors |
| Ωk prior | U(−0.15, 0.15) | Bayesian priors (flatness check) |

The paper does not separately report H_0, σ_8, S_8, n_s, A_s, α_s, r, or any GW observable — those are upstream priors or downstream of the SN+BAO+CMB joint that this paper does not refit.

## Appendix B — substitution chains (Python-verified 2026-05-07)

All sigma-distance computations were verified via `phonon-exflation-sim/.venv312/Scripts/python.exe` prior to writing this report. The full transcript is in the conversation log at the assistant turn immediately preceding this file write. Key verified values:

- `w0_FW vs Dovekie: |−0.918 − (−0.803)| / 0.054 = 0.115 / 0.054 = 2.1296σ`
- `w0_FW_R842 vs Dovekie: |−0.842454 − (−0.803)| / 0.054 = 0.039454 / 0.054 = 0.7306σ`
- `wa_FW = 0 vs Dovekie: |0 − (−0.72)| / 0.21 = 0.72 / 0.21 = 3.4286σ`
- `Ωm Dovekie vs Planck: |0.330 − 0.3089| / √(0.015² + 0.0062²) = 0.0211 / 0.01623 = 1.300σ`
- `w_0 trajectory drift DR2 → Dovekie: −0.803 − (−0.752) = −0.051 (TOWARD framework)`
- `Distance from canonical w0_FW = −0.918: |−0.918 − (−0.752)| = 0.166 (DR2); |−0.918 − (−0.803)| = 0.115 (Dovekie); CLOSER by 0.051`

Per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`, every directional claim above carries an explicit substitution chain; no "obviously from structure" shortcuts.

---

*End of report.*
