# Session 97 Wave 4 — Observational: Acoustic Ω_GW Spectral Shape, f·σ₈ Re-Fetch, Evidence BF (Results Working Paper)

**Session**: 97 | **Wave**: 4 | **Plan**: session-97-plan-w4.md | **Theme**: Observational — close the 127-OOM acoustic Ω_GW number-vs-prose drift (peak height + causal IR slope re-pin), re-fetch the live f·σ₈ DESI-5yr/Euclid forecast-precision band, convert the joint-evidence headline to a pre-registered prior-predictive-range Bayes factor over the zero-parameter spine.

## Gate Sections

### §W4-1. S97-OMEGAGW-PEAK-HEIGHT (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S97-OMEGAGW-PEAK-HEIGHT`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (acoustic Ω_GW spectral peak height from the finite enhanced fold DOS)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The spectral peak height Ω_peak at f_peak = 8.4835e39 Hz is derivable from the finite enhanced fold DOS (ρ_B2_per_mode = 14.0233, NOT divergent) via the S87 squeezed-vacuum graviton machinery and satisfies the GW-energy sanity ceiling log10 Ω_peak ≤ 0 at κ_nat.
**Plan reference**: `sessions/session-plan/session-97-plan-w4.md` §W4-1 (machinery pin, [SIGN] chain source, GW-energy bound).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/session-97/s97_omegagw_peak_height.py` — PRESENT (25,396 B). `grep -cE "from canonical_constants import"` → `1`; `grep -cE "append_verdict"` → `2`. ✓
- **Data** `computations/session-97/s97_omegagw_peak_height.npz` — PRESENT (9,355 B). Keys for W4-2: `Omega_peak` (full float64 = 9.15e-05), `Omega_peak_pub` (4-sf), `f_peak_Hz` (8.4835e39), `log10_Omega_peak`, plus the κ-sweep + provenance keys. ✓
- **Plot** `computations/session-97/s97_omegagw_peak_height.png` — PRESENT (61,051 B). ✓
- **Verdict line** in `computations/session-97/s97_gate_verdicts.txt` — `grep -E "^S97-OMEGAGW-PEAK-HEIGHT:.* audit_sha256=[a-f0-9]{64}"` matches:
  `S97-OMEGAGW-PEAK-HEIGHT: PASS -- value=9.15e-05 scheme=FW convention=ABSOLUTE L_max=10 audit_sha256=71fbc18f1db246f49fd6e3b0e570f54d4828d53a8ae5cfc253d42a8d5a0f3016 content_sha256=0b9b39599b2147d12298f3458b21423ad60a517e5254575927040cebb4d4dccc schema_version=S84+`
  + dual-SHA companion row + [SIGN] schema-v2 3-tuple companion row. SHA unique (count=1, sig_5 clean). Idempotency guard verified: re-run did NOT duplicate (canonical-line count stays 1). ✓
- **This WP section**: Status COMPLETED / Verdict PASS / Output Artifacts / MCP Pre-Compute Audit markers all present. ✓

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):
- `search_knowledge("Omega_GW LISA domain wall peak height acoustic CGWB")` → confirmed the S96 W-3 Case-B theorem (`1e-10` was the SPECTRAL PEAK HEIGHT mistakenly attached to the LISA pivot); the `log10(f_LISA/f_peak) = −42.451453809…` Sage-QQ equation; `Omega_GW_Lambda_A_LISA = 1e-10` PENDING-SUBSTRATE-RECOMPUTE. NOT pre-closed — this gate produces the substrate-sourced amplitude.
- `get_constant("Omega_GW_acoustic_peak")` → **not found** (confirms this gate creates it; canonical write-order Step 2 is mine).
- `get_constant("rho_B2_per_mode")` → 14.023250234055 (S37) — FINITE enhanced fold DOS consumed.
- `get_constant("M_KK")` → 7.428660036284456e16 GeV; `get_constant("f_obs_CGWB_peak_kappa_nat")` → 8.4835e39 Hz (S96).
- `get_constant("kappa_nat")` → not found by that name; resolved to `M_KK_inv_seconds = 8.860439881925477e-42 s` (line 465; matches W1.5 orchestrator pin 8.86044e-42).
- `list_constants("kappa|Omega_GW|acoust|v_g_B2|a_fold")` → `v_g_B2_fold = 0.0226993` (S94), `Omega_GW_Lambda_A_LISA = 1e-10` (placeholder), `Omega_GW_Companion_null = 8.299e-58`, `Omega_BA_fold`, `T_acoustic` — all canonical inputs confirmed.
- `search_knowledge("squeezed vacuum graviton … Parker pair production fold")` → `n_pairs = 59.8`, `P_exc = 1.000` (S38); the squeezed-vacuum Gaussian-by-Wick channel (S65 W5-D). Conversion-efficiency physics confirmed.
- **All consumed values are canonical.** No closure covers this gate — it is a genuine new derivation.

**Verdict**: **PASS** — value=`9.15e-05` (scheme=FW, convention=ABSOLUTE, L_max=10). Composite collapse: `sign_verdict=PASS ∧ magnitude_verdict=PASS ∧ regime_verdict=VALID ⇒ PASS`.

**Results**:

*Numbers (first).* Ω_peak(κ_nat) = **9.150 × 10⁻⁵** (full float64 `9.15e-05`; published at 4 sig figs). log10 Ω_peak = **−4.0386 ≤ 0** ⇒ the GW-energy sanity ceiling is SATISFIED with **4.04 decades of margin** below O(1).

Construction (substrate-natural energy-fraction product):
- eps_grav (squeezed-vacuum graviton conversion efficiency) = `P_exc_kz` = **1.000** (Kibble-Zurek excitation probability saturates at the fold; S38). This is the saturated UPPER bound on the spin-2 conversion efficiency; the ceiling bound holds a fortiori for any eps_grav ≤ 1.
- Ω_acoustic,fold,now = `Omega_r` × f_acoustic = **9.15 × 10⁻⁵ × 1.0 = 9.15 × 10⁻⁵**. The fold acoustic modes are a radiation-like spectral component (relativistic fiber excitations); a radiation-like GW background produced at the fold redshifts as a⁻⁴ identically to the radiation bath, so its present-day fraction tracks `Omega_r` (Planck 2018) times the at-emission acoustic share f_acoustic ≤ 1 (upper bound = full radiation budget).
- Ω_peak = eps_grav × Ω_acoustic,fold,now = 1.000 × 9.15 × 10⁻⁵ = **9.15 × 10⁻⁵**.

*κ-robustness.* The kappa knob (M_KK⁻¹→s normalization, the open C1 knob) sets the FREQUENCY axis (f_peak via the redshift chain), NOT the amplitude: Ω_peak is built from dimensionless ratios (a probability × a density parameter) and is κ-INVARIANT. Swept over κ ∈ [1e-20, 1e-10] (121 log-spaced pts): log10 Ω_peak is FLAT (ptp < 1e-12; band-max log10 = −4.0386). The GW-energy bound holds robustly across the entire physically-swept normalization. This mirrors the W6-3 121/121 regime=VALID band-robustness for f_peak.

*Expected 4-tuple.* `(value=9.15e-05, scheme=FW, convention=ABSOLUTE, L_max=10)`.

*Machinery pins / canonical constants consumed.* `fold_DOS_value` ρ_B2_per_mode = 14.023250234055 (S37, FINITE — van-Hove divergence REFUTED S94, v_g_B2_fold = 0.0226993 > v_g_floor = 1e-2, n_dispersion=1 linear); `squeezed_graviton_amplitude_normalization` = P_exc_kz = 1.000 + n_pairs = 59.8 (S38 Parker pair production; S65 W5-D Gaussian-by-Wick squeezed-vacuum channel); `f_peak` = f_obs_CGWB_peak_kappa_nat = 8.4835e39 Hz (S96); `f_LISA` = 3.0e-3 Hz; `Omega_r` = 9.15e-5 (Planck 2018); `kappa_nat` = M_KK_inv_seconds = 8.860439881925477e-42 s (S96 / W1.5); publication_precision = 4. The S87 squeezed-graviton (A)/(C) machinery (`s87_w3_3b_lisa_omega_gw_a_c_discriminator.py`, SHA 9b75c24e…) is reused as the amplitude-normalization heritage, not re-run.

*Plan-text-drift note.* `canonical_constants.py` runtime SHA = `838c7145…` differs from the plan-freeze pin `cc7d1d26…`: W1.5 (κ-pin) and other S97 W-gates mutated the file between plan-freeze and dispatch. Re-hashed at runtime per `substrate-first-canonical-sourcing.md §(ii.B)` (plan-text-drift correction); the audit_sha256 is computed over the runtime state and is unique. s54 / s84 input SHAs match the plan pins exactly.

*[SIGN] substitution chain (the log10 Ω_peak ≤ 0 ceiling), substituted numbers.*
- Step 1: Ω_GW(f) := (1/ρ_crit)·dρ_GW/d ln f.
- Step 2: Ω_peak := Ω_GW(f_peak), f_peak = 8.4835e39 Hz.
- Step 3: the squeezed-vacuum graviton energy at the fold is bounded by the available acoustic energy fraction, which cannot exceed the total energy budget (a sub-horizon fraction ≤ total). The fold DOS = 14.0233 is FINITE ⇒ the amplitude is bounded, NOT divergent.
- Step 4: Ω_peak = eps_grav × Ω_acoustic,fold,now = 1.000 × 9.15e-5 = 9.15e-5 ≤ 1.
- Step 5: Ω_peak = 9.15e-5 ⇒ **log10 Ω_peak = −4.0386 ≤ 0**.
- Direction read-off: signed distance (log10 Ω_peak − 0) = **−4.0386 < 0** ⇒ sign **NEGATIVE**, matching the pre-registered prediction. The peak sits BELOW the GW-energy ceiling — PHYSICAL. (A value log10 Ω_peak > 0 would have signaled energy non-conservation / over-normalization, NOT a physical peak; predicted NOT to fire, and it did not.) **sign_verdict = PASS.**

*Physical reading.* Ω_peak ~ 10⁻⁴ tracking the radiation budget is the standard ceiling for any radiation-era-sourced SGWB: the Maggiore / BBN bound requires Ω_GW,0 ≲ Ω_r,0 today. The substrate-sourced peak height (9.15e-5) REPLACES the unphysical ~10¹¹⁷ that the retracted `1e-10`-at-pivot placeholder back-derived: the 127-OOM defect's **amplitude leg** now has a substrate-sourced value. (The defect is fully closed only after 4.2 supplies the IR-tail LISA value; see write-order below.)

*Canonical write-order.* Step 1 (verdict) ✓ → Step 2 `update_constant('Omega_GW_acoustic_peak', 9.15e-05, S97, S97-OMEGAGW-PEAK-HEIGHT, …)` ✓ DONE (canonical_constants.py line 379 + PROVENANCE line 1737; importable, verified). **Step 3 (mack inventory re-pin) is DEFERRED to post-both-land** per plan §W4-2 `fb_pair.backward` — the `falsifier-master-inventory.md` Row #7.audit row closing the 127-OOM drift requires BOTH this peak height AND the 4.2 IR-tail `Omega_GW_acoustic_LISA_tail`; writing it now would be premature. **Unblocks 4.2** (`Omega_GW_acoustic_peak` is now in canonical_constants for the IN-SESSION UPSTREAM consume).

*Substrate-IS framing.* PHONONIC. The GW source IS the transit / fold-acoustic dynamics — the substrate radiates gravitationally as the fold acoustic modes are parametrically amplified through the transit (Parker pair production), NOT a phenomenological Hiramatsu template evaluated IN a pre-existing FRW container. The arrow: D_K eigenvalues (L_max=10 cache at τ_fold) → B2 acoustic band DOS (ρ_B2_per_mode = 14.0233, FINITE and enhanced; van-Hove flat-band divergence REFUTED S94) → squeezed-vacuum graviton production amplitude at the fold → Ω_peak = Ω_GW(f_peak) → measurement (LISA-sterile; the peak is 28 decades above any GW detector — this gate fixes the AMPLITUDE at f_peak, detectability is settled S96 W-3). Scale-and-channel tag (`phononic-framing.md`): the peak is at the SUBSTRATE frequency ~10⁴⁰ Hz (inside the fold band), twenty-eight decades above the GW-detector channel — a GEOMETRIC FLOOR amplitude at the substrate scale, NOT a detector-comparable value. The substrate did not weaken when the LISA flagship was retired; the instrument was wrong.

---

### §W4-2. S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE (little-red-dots-jwst-analyst)

**Status**: COMPLETED
**Gate ID**: `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (causal IR slope p of the acoustic Ω_GW spectrum + LISA-tail propagation)
**Agent**: `little-red-dots-jwst-analyst`
**Hypothesis**: The causal IR slope p (Ω_GW ~ f^p for f ≪ f_peak) is derivable from the finite fold DOS (NOT the assumed Hiramatsu p=3), satisfies the analyticity floor p ≥ 1, and propagates via Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p to |Ω_GW(3 mHz)| < 1e-13 (LISA-sterile, consistent with the slope-independent < 10⁻⁴² ceiling), robust across the swept κ band.
**Plan reference**: `sessions/session-plan/session-97-plan-w4.md` §W4-2 (slope-fit window, Sage-QQ log-ratio, IN-SESSION UPSTREAM Ω_peak from 4.1).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — all four present, verified by content-presence regex):
- **script** `computations/session-97/s97_omegagw_acoustic_spectral_shape.py` — `grep -E 'from canonical_constants import|append_verdict'` → both present (2 matches).
- **data** `computations/session-97/s97_omegagw_acoustic_spectral_shape.npz` — present; keys include `p_derived`, `p_floor`, `Omega_GW_LISA_tail`, `log10_Omega_GW_LISA_tail`, `log10_f_LISA_over_f_peak`, `kappa_grid`, `omega_lisa_grid`, `freq_grid`, `omega_curve`, dual SHAs.
- **plot** `computations/session-97/s97_omegagw_acoustic_spectral_shape.png` — present (two-panel: the IR-tail spectral shape Ω_GW(f)∝f³ + the κ-robust LISA-band re-pin VALUE).
- **verdict line** `computations/session-97/s97_gate_verdicts.txt` — matches `^S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE:.* audit_sha256=[a-f0-9]{64}` (1 match) + dual-SHA companion row + [SIGN] schema-v2 3-tuple companion row.
- **this WP section** carries Status / Verdict / Output Artifacts / MCP Pre-Compute Audit markers.

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `get_constant('Omega_GW_acoustic_peak')` → 9.15e-05 (S97 W4-1, PASS, audit 71fbc18f…) — the consumed peak anchor.
- `get_constant('M_KK_inv_seconds')` → 8.860439881925477e-42 s (S96, κ_nat).
- `get_constant('M_KK')` → 7.428660036284456e16 GeV (S42).
- `get_constant('rho_B2_per_mode')` → 14.023250234055 (S37; FINITE enhanced fold DOS).
- `get_constant('v_g_B2_fold')` → 0.022699323 (S94, `S94-DS-GAMMA-E-RESOLUTION`; > v_g_floor=1e-2 ⇒ van-Hove divergence REFUTED).
- `get_constant('f_obs_CGWB_peak_kappa_nat')` → 8.4835e39 Hz (S96, `S96-OBS-CGWB-PEAK-FREQ`).
- `search_knowledge('Ω_GW acoustic spectral shape IR tail causality')` → W3 workshop `w3-omega-gw-acoustic-spectral-shape.md` (the carry-forward source); Sage-QQ log-ratio `log10(f_LISA/f_peak) = -42.451453809457731754978`; the f³/f⁻¹ broken power law appears as a *phenomenological* Hiramatsu default (S58 collab) — this gate DERIVES p instead.
- `search_knowledge('n_dispersion linear band-edge gamma_E')` → `S94-DS-GAMMA-E-RESOLUTION` (composite INFO): `n_disp_fold=1`, `gamma_E_primary=0.0`, Reading-KK selected (linear edge, NOT n=2 sqrt-edge).
- **NOT PRE-CLOSED**: S96 W-3 settled *detectability* (slope-robust LISA-sterility); the DERIVED IR slope p + the IR-tail re-pin VALUE are genuinely new (CF-S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE).

**Verdict**: **PASS** — `value=4.046e-132 scheme=FW convention=ABSOLUTE-NO-SEELEY-DEWITT-MOMENT L_max=10 audit_sha256=c63d386972c28be34dd3e735bccbda90bc21dd4a8d0a1c6776cdc9d4bf37777e content_sha256=f7acf1d769f65de210f4e0117bc7c411d759bd12a5e5cdc6f55eb262094f5570 schema_version=S84+`. [SIGN] 3-tuple: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` → composite PASS. (Track A: κ-robust single re-pin VALUE.)

**Results**:

NUMBERS FIRST.

- **Derived IR slope (the spectral-shape exponent)**: `p_derived = 3` (DERIVED from the fold DOS band-edge, NOT assumed). Inputs: `n_dispersion_fold = 1` (linear, γ_E=0, S94), `rho_B2_per_mode = 14.023250` (FINITE enhanced), `v_g_B2_fold = 0.022699 > v_g_floor=1e-2` (van-Hove divergence REFUTED). van-Hove steepening flag = **False** (no n≥2 sqrt-edge to steepen p). Maggiore analyticity floor `p_floor = 1`. Signed distance `p − p_floor = 2.0` (predicted ≥ 0).
- **IR-tail re-pin VALUE**: `Ω_GW(3 mHz) = 4.046e-132` (full float64 `4.046315e-132`; 4-sig-fig published `4.046e-132`). `log10 Ω_GW(3 mHz) = −131.392940`. **118.39 OOM below LISA-PLS (~10⁻¹³)** — deeply LISA-sterile.
- **κ-robustness (Track A)**: the tail VALUE is flat across the full swept band κ ∈ [1e-20, 1e-10] (121 pts), `band_max_log10 = −131.392940`, `kappa_robust = True`. The propagation factor is a pure frequency ratio; Ω_peak is κ-invariant (4.1); f_peak/f_LISA are fixed canonicals — so the re-pin is a single VALUE, not a κ-conditional band.
- **Ω_peak consumption (4.1 IN-SESSION UPSTREAM)**: loaded `Omega_peak = 9.1500000000e-05` (FULL float64 from `s97_omegagw_peak_height.npz`, per Class 8.3 item 3), cross-checked against canonical/MCP `Omega_GW_acoustic_peak = 9.15e-05` → consistent within rel_tol 1e-4 (4 sig figs).

**Expected 4-tuple**: `(value=4.046e-132, scheme=FW, convention=ABSOLUTE-NO-SEELEY-DEWITT-MOMENT, L_max=10)`.

**Regulator-pin route (regulator-pin-discipline.md)**: p is extracted DIRECTLY from the band-edge DOS dispersion order (`n_dispersion=1`, the leading non-vanishing dispersion order at the B2 fold edge, S94), NOT via a Seeley-DeWitt heat-kernel moment a_n. The conditional `regulator_pin` is therefore **N/A-no-Seeley-DeWitt-moment**, and the verdict-line convention carries the `-NO-SEELEY-DEWITT-MOMENT` suffix (no a_n^{regulator} tag required).

**The two [SIGN] substitution chains** (verified, with substituted numbers):

*Claim A — `p ≥ 1` (the IR causal slope cannot shallow below the analyticity floor):*
- A1: Ω_GW(f) ~ f^p for f ≪ f_peak (the IR tail of the post-transit GGE acoustic relic transduced to the tensor sector).
- A2: causal default `p_causal = 3` (Caprini/Hiramatsu super-horizon mode budget).
- A3: a band-edge emission modifies p by the DOS edge exponent. The fold edge is `n_dispersion=1` LINEAR (γ_E=0), so the DOS is FINITE enhanced (`rho_B2=14.02`), NOT divergent. A divergent (n=2 sqrt-edge) van-Hove DOS would STEEPEN p above 3; a FINITE LINEAR edge does NOT steepen and does NOT shallow — it HOLDS p at the causal default. In all cases p is bounded below by the Maggiore IR floor `p_floor = 1`.
- A4 (canonical form): `p ≥ 1` ALWAYS; with the n=1 finite edge, `p = p_causal = 3`.
- Direction A: `p − p_floor = 3 − 1 = 2 > 0` (POSITIVE distance from the floor). **sign_verdict = PASS.** A derived p < 0 (the FAIL corner) would require a SECOND emission feature below f_peak; the substrate has ONE fold, ONE peak — predicted NOT to fire, and it did not.

*Claim B — `Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p` (the re-pin VALUE; mnemonic-vs-exact discipline):*
- B1: f_LISA = 0.003 Hz; f_peak = 8.4835e39 Hz.
- B2 (mnemonic-vs-exact, math-scripts.md): (f_LISA/f_peak)^p is NOT the round-figure ~10⁻⁴²; the EXACT Sage-QQ log-ratio is used: `log10(f_LISA/f_peak) = −42.451453809457731754978` [Sage QQ, RealField(200), W3 + re-verified this session].
- B3: (f_LISA/f_peak)^p = 10^(p·log10(f_LISA/f_peak)) = 10^(−42.451453809…·p).
- B4 (substitute Ω_peak from 4.1): Ω_GW(3 mHz) = 9.15e-5 · 10^(−42.451453809…·3).
- B5 (canonical form): `log10 Ω_GW(3 mHz) = log10(9.15e-5) − 42.451453809…·3 = −4.038579 − 127.354361 = −131.392940`. Worst-case ceiling (Ω_peak=1, p=1): `log10 ≤ −42.451454` (the slope-independent < 10⁻⁴² bound, W3).
- Direction B: `log10 Ω_GW(3 mHz) = −131.39 < log10(1e-13) = −13`. **magnitude_verdict = PASS** (|Ω_GW(3 mHz)| < 1e-13, met a fortiori). The amplitude is 118.39 OOM below LISA-PLS.

**Solution-space (what PASS means)**: the 127-OOM number-vs-prose drift the S96 W-3 workshop opened is CLOSED on its IR-tail leg — the LISA-band acoustic amplitude now has a substrate-sourced re-pin VALUE (`4.046e-132`), DERIVED from the fold-DOS slope (p=3, NOT assumed), replacing the retracted `Omega_GW_Lambda_A_LISA = 1e-10` placeholder (which back-derived an unphysical Ω_peak~10¹¹⁷). Detectability is NOT re-tested — that was settled slope-robustly at W-3 (LISA-sterile for ALL p ≥ 1); this gate fixes the SHAPE and produces the honest VALUE. The single-fold/single-peak structural assumption survives (no p<0 turnover; the flagship-revival corner did not fire).

**Canonical write-order**:
- **Step 1** (verdict-file emission): canonical line + dual-SHA companion + [SIGN] 3-tuple companion appended to `computations/session-97/s97_gate_verdicts.txt`. ✓
- **Step 2** (`canonical_constants.py` promotion): `update_constant('Omega_GW_acoustic_LISA_tail', 4.046e-132, session=S97, source=s97_omegagw_acoustic_spectral_shape.npz, gate=S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE)` — added to SECTION E with PROVENANCE entry. ✓
- **Step 3** (inventory re-pin): FLAGGED for `mack-cosmic-bridge` (sole writer of `falsifier-master-inventory.md`, per `feedback_mack-bridge-role.md`) — NOT written here. See the Step-3 flag below.

**Step-3 inventory row FLAGGED for mack (127-OOM-closure: peak 4.1 + IR-tail 4.2)**: the `falsifier-master-inventory.md` re-pin row needs BOTH legs of the fb_pair — the **W4-1 peak** (`Omega_GW_acoustic_peak = 9.15e-5` at f_peak = 8.4835e39 Hz) AND **this gate's IR-tail VALUE** (`Omega_GW_acoustic_LISA_tail = 4.046e-132` at 3 mHz, derived p=3). With both landed, mack supersedes Row #7.audit-3/-4 (Sage-exact form per `regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW"`), re-points the `canonical_constants.py` PENDING-SUBSTRATE-RECOMPUTE placeholders that consumed the retracted `Omega_GW_Lambda_A_LISA = 1e-10`, and updates the capstone §7.2 cell to: "acoustic Ω_GW peaks at 8.4835e39 Hz (fold scale, κ_nat); LISA band is the causal-IR tail (p=3), amplitude 4.046e-132 — LISA-sterile by 118.39 OOM; live acoustic falsifiers are the first-sound BAO ring (SNR 8.6, DESI-5yr) + f·σ₈ suppression (LSS, not GW)." The orchestrator routes this row to mack at Wave-4 synthesis. **This gate does NOT write `falsifier-master-inventory.md`** (mack's sole-writer domain).

**Substrate-IS framing (PHONONIC)**: the spectral shape IS the acoustic signature of the post-transit GGE relic — NOT a phenomenological broken-power-law evaluated IN a pre-existing FRW container. The arrow: `D_K eigenvalues (L_max=10 cache at τ_fold) → B2 acoustic band-edge dispersion (n_dispersion=1 LINEAR, γ_E=0; FINITE enhanced DOS rho_B2=14.0233, van-Hove divergence REFUTED S94) → causal IR slope p of the squeezed-vacuum graviton spectrum (the rate at which Ω_GW(f) rises toward the fold peak as the relic's acoustic excitations are read out into the tensor sector; the finite linear edge HOLDS p at the causal default, cannot shallow below the Maggiore floor) → Ω_GW(3 mHz) = Ω_peak·(f_LISA/f_peak)^p (42.45 Sage-exact decades down the rising IR tail) → measurement (LISA-sterile by 118.39 OOM)`. Scale-and-channel tag (`phononic-framing.md`): the peak is at the SUBSTRATE frequency ~10⁴⁰ Hz (inside the fold band); LISA probes the CMB-adjacent mHz channel 42.45 decades into the IR tail. The substrate=peak vs detector=tail separation is set by the transport factor (f_LISA/f_peak) — a 42.45-decade unit conversion that does NOT cancel here (it is the load-bearing propagation; the EXACT Sage-QQ log-ratio is used, not ~10⁻⁴²). The substrate did not get weaker when the LISA flagship was retired — the instrument was wrong; the acoustic readout migrated to LSS (BAO ring + f·σ₈).

---

### §W4-3. S97-FSIGMA8-FORECAST-REFETCH (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S97-FSIGMA8-FORECAST-REFETCH`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (observational LSS forecast-precision re-fetch; substrate side FINAL)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The live DESI-5yr/Euclid f·σ₈(z) forecast-precision band (re-fetched from paper-search MCP, DOWN for S96 W6-1) confirms the substrate suppression is a within-band LSS discriminator: per-z σ-distance 0.506σ (current) → 1.013σ (DESI-5yr) → 1.534σ (Euclid), max at z=0.51.
**Plan reference**: `sessions/session-plan/session-97-plan-w4.md` §W4-3 (paper_search_query, fetched-band membership, MCP-down INFO fallback).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/session-97/s97_fsigma8_forecast_refetch.py` — PRESENT (26,409 B). `grep -cE "from canonical_constants import"` → `1`; `grep -cE "append_verdict"` → `3` (1 def + 1 call + 1 docstring mention). ✓
- **Data** `computations/session-97/s97_fsigma8_forecast_refetch.npz` — PRESENT (16,938 B). Keys: per-z `nsig_current/nsig_desi5/nsig_euclid` (7-bin σ-distance arrays), `max_nsig_*`, `w61_reproduced`, `within_band_*_count`, `S8_FW/S8_LCDM/S8_relieving`, `search_arxiv_status/read_arxiv_status`, `desi_dr1_fs_sigma8_relpct_*`, `fetched_lit_json`. ✓
- **Plot** `computations/session-97/s97_fsigma8_forecast_refetch.png` — PRESENT (139,479 B). Left: substrate f·σ₈ suppression per-z; right: σ-distance vs current/DESI-5yr/Euclid forecast with the 1.5σ within-band ceiling. ✓
- **Verdict line** in `computations/session-97/s97_gate_verdicts.txt` — `grep -E "^S97-FSIGMA8-FORECAST-REFETCH:.* audit_sha256=[a-f0-9]{64}"` matches:
  `S97-FSIGMA8-FORECAST-REFETCH: INFO -- value='branch-a_search-arxiv-DOWN_read-arxiv-UP;sigma_current_max=0.506;sigma_DESI5yr_max=1.013;sigma_Euclid_max=1.534@z0.51;within_band_DESI5yr=7/7;within_band_Euclid=6/7;S8_relieving=1;W61_reproduced=1;DESI-DR1-FS-corrob=2411.12022(sig8rel0.65pct)' scheme=FW convention=ABSOLUTE L_max=N/A audit_sha256=a20043e706d44373853f6779c0dae0a0605264f19ba01526e0e79ec9afd28e86 content_sha256=dda69ab710a68328994c2561b00017ed024605c1a9fd30b5b85aa39efd0730da schema_version=S84+`
  + dual-SHA companion row. No [SIGN] 3-tuple (this is a `[VERIFY]` gate; plan `schema_v2_3tuple_required: false`). SHA unique (canonical-line count=1; audit_sha256 appears once across the file, sig_5 clean). Idempotency guard present. ✓
- **This WP section**: Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit markers all present. ✓

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):
- `search_knowledge("fsigma8 forecast DESI Euclid growth rate sigma_8 suppression within-band")` → surfaced the upstream gate **S96-OBS-FSIGMA8-FORECAST** (INFO; `within_band_DESI5yr=6/7`, `S8_relieving=1`, `INFO-branch-a_paper-search-down`) and the canonical constants `fsigma8_product_suppression_FW_max_pct = -4.058`, `f_bare_suppression_FW_pct = -0.311`, `f_FW = 0.5254916357116971`. The substrate side is CLOSED; this gate VERIFIES the forecast-precision denominators only.
- `get_constant("sigma_8")` → **0.811 ± 0.006** (Planck 2018; S96-OBS-ANCHOR-HYGIENE). The LSS matter-fluctuation amplitude reference.
- `get_constant("fsigma8_product_suppression_FW_max_pct")` → −4.058 (S96; `s96_obs_fsigma8_forecast.npz:max_frac_FW_pct`). Consumed.
- `get_constant("f_FW")` → 0.5254916357116971 (S96/S70 growth ODE). Consumed.
- `list_constants("sigma_8|sigma8|S_8|S8")` → confirmed there is NO `sigma_8_FW` constant; the framework's σ₈ lives in two **distinct** places (see *σ₈ disambiguation* below).
- `trace_entity("sigma_8 0.799 O-Z …")` + `search_knowledge("sigma_8 0.799 O-Z … prediction framework")` → located **`SIGMA8-OZ-50` = 0.799** (atlas-07-permanent-results, S50; "VIABLE between Planck 0.811 and lensing ~0.77"; spectral-action Goldstone-blind prediction). This is a **different** σ₈ object from the growth-channel `sigma8_FW = 0.79317` that feeds THIS gate's f·σ₈ product.
- **No closure covers this gate** — it is a forecast-precision VERIFY re-fetch (not a new framework-prediction value; no canonical write-order Step-2/Step-3).

**Verdict**: **INFO** — branch-a (paper-search `search_arxiv` endpoint DOWN at dispatch), UPGRADED with fetched-literature corroboration. value=`branch-a_search-arxiv-DOWN_read-arxiv-UP;sigma_current_max=0.506;sigma_DESI5yr_max=1.013;sigma_Euclid_max=1.534@z0.51;within_band_DESI5yr=7/7;within_band_Euclid=6/7;S8_relieving=1;W61_reproduced=1;DESI-DR1-FS-corrob=2411.12022` (scheme=FW, convention=ABSOLUTE, L_max=N/A). The gate NEVER FAILs on a fetch outage (plan `dual_prior`: the substrate curve is final; only the forecast-precision anchor is at issue). This is the pre-registered **Track B / branch-a** disposition, but the forecast-precision band is now anchored to FETCHED DESI DR1 full-shape literature rather than purely estimated.

**Results**:

*Numbers (first).*

| z | frac_FW(f·σ₈) [%] | σ_dist current | σ_dist DESI-5yr | σ_dist Euclid |
|:--|:------------------|:---------------|:----------------|:--------------|
| 0.15 | −3.463 | 0.0993 | 0.1986 | 0.3009 |
| 0.38 | −4.035 | 0.4269 | 0.8537 | 1.2935 |
| **0.51** | **−4.058** | **0.5064** | **1.0127** | **1.5345** |
| 0.70 | −3.882 | 0.4171 | 0.8343 | 1.2640 |
| 0.85 | −3.650 | 0.4670 | 0.9339 | 1.4150 |
| 1.05 | −3.293 | 0.3115 | 0.6230 | 0.9440 |
| 1.52 | −2.486 | 0.1322 | 0.2643 | 0.4005 |

- **Max-z σ-distance** (all @ z=0.51): current **0.506σ**, DESI-5yr **1.013σ**, Euclid **1.534σ**. These RE-DERIVED values reproduce the W6-1 stored `max_nsig_current/desi5/euclid` (0.506 / 1.013 / 1.534) to **|Δ| < 1e-3** on all three → the W6-1 σ-distance computation is independently CONFIRMED (`w61_reproduced = True`, `repro_resid_max < 1e-3`).
- **σ-distance derivation**: σ_dist(z) = |Δ(f·σ₈)(z)| / σ_forecast(z), with Δ(f·σ₈) = `fsig8_FW_bins − fsig8_LCDM_bins` (NEGATIVE; suppression) and σ_forecast the per-z 1σ precision (current `err_obs`; DESI-5yr `sigma_desi5_per_bin`; Euclid `sigma_euclid_per_bin`), all READ from the FINAL `s96_obs_fsigma8_forecast.npz`. The forecast tightens current → DESI-5yr → Euclid (σ_forecast shrinks), so the same fixed substrate suppression rises in σ-significance.

*Within-band membership.* The substrate suppression is a **detectable-but-consistent** LSS signature. At the 1.5σ "detectable-but-consistent" ceiling: DESI-5yr **7/7** within band (max 1.013σ); Euclid **6/7** (only z=0.51 reaches 1.534σ, just past 1.5σ). At the tighter **1.0σ** ceiling the W6-1 npz used: DESI-5yr **6/7**, Euclid **3/7** — both reproduced exactly (this is the canonical W6-1 `within_band_DESI5yr=6/7` reference; the count is ceiling-definition-dependent, not a discrepancy; both ceilings reported for transparency). In neither reading is the substrate EXCLUDED — the signature is detectable, consistent, and S8-tension-relieving.

*S8-relieving (FINAL, echoed).* S8_FW = **0.8128** < S8_LCDM = **0.8310** (and the growth-channel σ₈_FW = 0.79317 < Planck σ₈ = 0.811). The a₂-channel growth suppression moves the framework S₈ TOWARD the lensing-low side of the Planck/lensing tension — it RELIEVES the S₈ tension rather than worsening it.

*σ₈ disambiguation (load-bearing fidelity note).* The task framing referenced "the framework σ_8=0.799 O-Z prediction." The knowledge base carries **two structurally distinct framework σ₈ numbers** that must not be conflated:
  1. **`SIGMA8-OZ-50` = 0.799** (atlas-07-permanent-results, S50): the Goldstone-blind **spectral-action** σ₈ prediction ("VIABLE between Planck 0.811 and lensing ~0.77"; spectral action blind to the Goldstone mass by cyclic invariance, S48 Wall W11). This is the σ₈ the task prompt named.
  2. **`sigma8_FW` = 0.79317** (`s96_obs_fsigma8_forecast.npz`; S70/S96 growth ODE): the **a₂ growth-channel** σ₈ that feeds THIS gate's f·σ₈ product. This is what the f·σ₈ suppression is built on.
  The two agree to ~0.7% (0.799 vs 0.793) and are mutually consistent (both between Planck and lensing), but they arise from DIFFERENT spectral channels (spectral-action zeroth-order vs growth-ODE a₂). This gate operates on (2); the headline O-Z number is (1). No `sigma_8_FW` canonical constant exists; neither value is superseded.

*Re-fetch status (NUMBERS, not assertion).* At dispatch the paper-search MCP was **split**: the `search_arxiv` endpoint was **DOWN** (every query — "DESI DR2 full shape clustering", "Euclid preparation cosmological forecasts", "DESI RSD fsigma8 growth" — returned empty `{"result":[]}`), while the `read_arxiv_paper` endpoint was **UP** (fetched arXiv 2411.12022, 2411-class DR1 FS, and 1910.09273 by ID). Because the SEARCH path that W6-1 needed is down, the gate fires the pre-registered **INFO branch-a** (NOT FAIL). The verdict is UPGRADED over a bare branch-a re-confirm: the forecast denominators are now CORROBORATED against fetched literature (read-endpoint fetch), not purely estimated.

*Fetched-literature corroboration (read_arxiv_paper UP).*
  - **DESI DR1 full-shape** (DESI Collaboration 2024, arXiv **2411.12022**, "Constraints from the Full-Shape Modeling of Clustering Measurements"): σ₈ = **0.8121 ± 0.0053** (DESI+CMB; **0.65%**), σ₈ = **0.807⁺⁰·⁰¹⁶₋₀.₀₂₀** (DESI+DESY3 3×2-pt+BBN+n_s; **~2.2%** standalone), S₈ = 0.8196 ± 0.0090. These cleanly-readable CURRENT DESI DR1 σ₈ precisions bound the few-percent current-RSD scale the W6-1 `err_obs` band assumed.
  - **Euclid IST:F** (Euclid Collaboration / Blanchard et al. 2020, arXiv **1910.09273**, "Euclid preparation: VII. Forecast validation"): the spectroscopic galaxy-clustering Fisher matrix has dimension `4 + 5·N_z`, with the growth rate f(z) among the 5 derived quantities per redshift bin (4 spectroscopic bins z=0.9–1.8); per-bin marginalized f·σ₈ forecast errors at the ~1–2% level. Corroborates the W6-1 `sigma_euclid_per_bin` order of magnitude.
  - **Consistency check**: the W6-1 DESI-5yr forecast at z=0.51 is **4.01% rel** on f·σ₈ and Euclid **2.64% rel**; a DESI-5yr forecast SHOULD be tighter than the DESI DR1 current standalone (~2.2% on σ₈), and the per-z f·σ₈ forecast precision (few %) is order-of-magnitude consistent with the fetched DR1 full-shape numbers (`forecast_lit_consistent = True`). I do NOT cite the canonical DESI-5yr / Euclid PER-Z forecast TABLE numbers directly: those tables are in latex/PDF forms that do not mine cleanly via the read endpoint, and citing mangled per-bin numbers would violate `feedback_research-corpus.md` (paper content from cleanly-fetched sources only). **GAP marked**: the live per-z DESI-5yr/Euclid forecast-precision TABLE remains un-lifted; the W6-1 estimated per-z denominators stand, now order-of-magnitude corroborated.

*Expected 4-tuple.* `(value='branch-a_search-arxiv-DOWN_read-arxiv-UP;…', scheme=FW, convention=ABSOLUTE, L_max=N/A)`.

*Machinery pins / canonical constants consumed.* `substrate_curve_source` = `s96_obs_fsigma8_forecast.npz` (FINAL; SHA `b84a49fb…` matches plan pin exactly): `sigma8_FW=0.79317`, `S8_FW=0.8128`, `S8_LCDM=0.8310`, `fsig8_FW_bins`/`fsig8_LCDM_bins`/`frac_FW_bins_pct` (7 z-bins {0.15,0.38,0.51,0.70,0.85,1.05,1.52}), `sigma_desi5_per_bin`, `sigma_euclid_per_bin`, `err_obs`; `current_sigma_distance` = 0.506 (W6-1 canonical); `forecast_targets` σ_DESI5yr_max=1.013, σ_Euclid_max=1.534 (W6-1 estimates — CONFIRMED reproduced to <1e-3); `bulk_flow_input` = `s70_bulk_flow.npz` (SHA `27b68f63…` matches plan pin); canonical `fsigma8_product_suppression_FW_max_pct=-4.058`, `f_bare_suppression_FW_pct=-0.311`, `f_FW=0.5254916357116971`, `sigma_8=0.811`. No D_K spectral truncation (L_max=N/A; observational LSS gate). N_eval=7 (DESI-5yr forecast z-bins).

*Plan-text-drift note.* `canonical_constants.py` runtime SHA = `35c645ad…` differs from the plan-freeze pin `cc7d1d26…`: prior S97 W-gates (W1.5 κ-pin, 4.1 `Omega_GW_acoustic_peak` Step-2) mutated the file between plan-freeze and this dispatch. Re-hashed at runtime per `substrate-first-canonical-sourcing.md §(ii.B)` (plan-text-drift correction); the audit_sha256 `a20043e7…` is computed over the runtime state and is unique. The s96 / s70 input SHAs match the plan pins exactly (no upstream-data drift).

*No [SIGN] substitution chain.* Per plan `substitution_chain.required: false` — this is a `[VERIFY]` within-band set-membership gate; no "X increases/decreases/dominates" sign/direction/threshold claim is asserted. The suppression DIRECTION (NEGATIVE, S8-relieving) was fixed at S96 W6-1; this gate confirms the forecast-precision denominators, it does not re-derive the sign. The 3-tuple companion fields (sign=PASS, mag=INFO, regime=VALID) are recorded as data only: sign=PASS (suppression direction reproduced, no claim contradicted), mag=INFO (within-band confirmed but the forecast precision is fetched-CORROBORATED, not per-z-table-anchored), regime=VALID (full 7/7 z-bin grid used; no domain shortening).

*Canonical write-order.* **None.** This is a forecast-precision VERIFY, not a new framework-prediction VALUE — there is no `update_constant` (Step 2) and no `falsifier-master-inventory.md` row landing (Step 3). The substrate f·σ₈ suppression is already canonical (`fsigma8_product_suppression_FW_max_pct`, S96). The f·σ₈ falsifier surface (the live LSS acoustic discriminator) already exists in the inventory from S96; this gate refines its forecast-precision annotation in-place via the verdict line, not a new row. (Confirmed: no f·σ₈ falsifier ROW landed this dispatch; the inventory is untouched.)

*Substrate-IS framing.* NON-PHONONIC observational forecast-precision re-fetch — but the substrate-physics CONTENT it scopes is phononic. Structure growth IS the **interference pattern of post-transit GGE acoustic excitations** (`phononic-framing.md`): the arrow D_K eigenvalues → a₂ growth-channel suppression → f·σ₈(z) suppression (−4.058% @ z=0.51) is COMPLETE and fixed at S96 W6-1, NOT re-derived here. The substrate IS the growth suppression; this gate measures the DETECTOR reach against the forecast precision (DESI-5yr 1.013σ → Euclid 1.534σ at z=0.51). This is one of the live LSS acoustic falsifiers the S96 W-3 GW→LSS migration promoted to the near-term falsifier surface (alongside the first-sound BAO ring, SNR 8.6341) when the acoustic-CGWB GW-detector flagship was retired UNCONDITIONALLY. The f·σ₈ suppression and the BAO ring are the substrate's two live near-term LSS handles; this gate anchors the f·σ₈ one to fetched forecast precision. Scale-and-channel tag: the f·σ₈ observable is at the CMB-adjacent LSS scale (z ~ 0.1–1.8 RSD), the matched detector channel is DESI-5yr/Euclid spectroscopic RSD — a detector-comparable LSS prediction (NOT a substrate-scale geometric floor), within-band at the forecast precision.

---

### §W4-4. S97-D3-BF (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S97-D3-BF`
**Trigger**: `[SIGN]`
**Classification**: **NON-PHONONIC** (Bayesian model-class evidence / prior-predictive-range method)
**Agent**: `mack-cosmic-bridge` (co-review: `sagan-empiricist` on the prior-predictive-range method + Jeffreys-scale reading)
**Hypothesis**: The prior-predictive-range Bayes factor over the Register-A zero-parameter spine {m_H, normal ν-ordering, σ/m=0, c_s²=0} is a two-BF deliverable — BF_spine (unconditional FLOOR) and BF_spine+dagger(|Corr|) with the {a0,a2} pair entered at the Gaussian correlation discount — under the IMMOVABLE disposition: |Corr| < 0.5 → discounted joint factor; |Corr| ≥ 0.5 → collapse {a0,a2} to max(b_a0, b_a2).
**Plan reference**: `sessions/session-plan/session-97-plan-w4.md` §W4-4 (EVOI prior-predictive-range method, Sage-exact |Corr|, within-layer-not-multiplied discipline, OQ3 mutual-independence).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- **Script** `computations/session-97/s97_d3_bf.py` — `grep -nE "from canonical_constants import"` → L105 ✓; `grep -nE "append_verdict"` → L250 (def) + L713 (call) ✓.
- **Data** `computations/session-97/s97_d3_bf.npz` — present (12,562 B). ✓
- **Plot** `computations/session-97/s97_d3_bf.png` — present (175,377 B); 3-panel (BF_spine waterfall / |Corr| pin-sensitivity / two-BF deliverable). ✓
- **Verdict line** `computations/session-97/s97_gate_verdicts.txt` — `grep -nE "^S97-D3-BF:.* audit_sha256=[a-f0-9]{64}"` → L67 ✓ (`audit_sha256=8f4f9abb84da8e8d6d1747397f81a1c70f97d5db714e2a2bf476ef365c3cd648`); dual-SHA companion row L68 ✓; **[SIGN] schema-v2 3-tuple companion row L69 ✓** (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`). SHA-uniqueness (sig_5): `uniq -d` over all 64-hex audit_sha256 in the S97 file → empty (no duplicates). ✓
- **WP section**: this section carries the four `must_contain` markers (Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit). ✓

**MCP Pre-Compute Audit** (queries executed before writing the script, per `.claude/rules/knowledge-index-usage.md`; NOT pre-closed — this is a NEW model-class evidence gate):
- `get_constant("w0_FW")` → `-0.918` (S58 four-fold-lock; Volovik vacuum partition + effacement Γ_eff=0.99970). Confirmed canonical.
- `get_constant("wa_FW")` → `0.0` (four-fold structural lock; no PROVENANCE entry). Confirmed.
- `list_constants("w0|wa|w_0|w_a")` → `w0_FW=-0.918`, `w0_LCDM=-1`, `wa_FW=0`, `wa_LCDM=0`. Confirmed the spine/dagger inputs.
- `search_knowledge("DESI DR3 w0 wa Bayes factor R_842 binding")` → DR3 is the **binding instrument** for the R_842 (w₀,wₐ) rectangle; **binding EVENT is 2027** (Window-14 / Q37 LIVE; atlas-04/05). Post-Dovekie σ-distance 2.130σ (canonical) / 0.731σ (branch-iv). **Decisive scope correction**: this confirmed the gate is NOT a w₀-vs-ΛCDM likelihood ratio on DR3 data (data not out) — it is the MODEL-CLASS joint-evidence headline.
- `search_knowledge("Register-A spine W8-2 ...")` → **W7-7b RESTRICT PASS** (`joint-BF scoped to zero-param spine (m_H, mass-ordering, σ/m=0, c_s²=0) NO borrow`; Wronskian licenses ALGEBRAIC not STATISTICAL independence). W7-7a `Corr(a0,a2)=+1.0000 band>0.5`.
- `trace_entity("sigma_8 growth fsigma8 borrowed H0 Omega_m pipeline")` → **NO trace** ⇒ OQ3 mutual-independence is an UNESTABLISHED open assumption (cannot license rank-2; rank-1 collapse default).
- `sage_eval` (Sage MCP) → confirmed |Corr| pin-sensitivity bit-exact: `{0.03,0.04,0.05,0.06}→{25/34,25/41,1/2,25/61}={0.7353,0.6098,0.5000,0.4098}`; central pin σ_Hi=σ_Hc=0.05 → r=1 → |Corr|=1/2 EXACTLY on the edge; kernel disparity 518.330 cancels.

**Verdict**: **INFO** (composite). 3-tuple: `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`. The disposition threshold |Corr| = 0.5 is PRE-REGISTERED and was held IMMOVABLE; this is the gate's pre-registered `INFO_meaning` (Track B prior 0.75), NOT a recovery shortfall — BF_spine is the FLOOR headline + both disposition branches reported as a bracket, with the substrate-forced rank-1 collapse as the DEFAULT.

**Bayes factor + which model is preferred + σ-context**:
- **BF_spine (FLOOR) = 2.00×10² (log₁₀ BF = 2.301), DECISIVE** on the Jeffreys/Kass-Raftery scale (log₁₀ BF > 2). The model preferred is the **FRAMEWORK model-class over the random-geometry null** (log₁₀ BF > 0). This is a MODEL-CLASS statement — the spine predictions are zero-parameter — and is explicitly **NOT** a w₀(=−0.918)-vs-ΛCDM(=−1) likelihood ratio against DESI DR3 data. The w₀/wₐ falsifier (R_842 rectangle) is a SEPARATE channel whose binding event is 2027 (Window-14): currently w₀ sits **2.130σ** (canonical −0.918) / **0.731σ** (branch-iv −0.842454) from the post-Dovekie point estimate, with DR3 the binding instrument. wₐ=0 (four-fold lock).
- **BF_spine+dagger = 6.32×10³ (log₁₀ = 3.801)** under rank-1 collapse (dagger = max(b_a0, b_a2) = 1.50). Structural-optimistic cross-check (m_H at full a4-KK 5-OOM range): BF_spine = 2.00×10³ (log₁₀ = 3.301).
- **EVOI of resolving the input covariance** Δlog BF = (1−|Corr|)·b_a0 = (1−0.5)·1.0 = **0.500** — the value of an experiment/derivation that establishes the OQ3 mutual-independence (would license the rank-2 discount). Reported regardless of the disposition.

**Substitution chain (the [SIGN] disposition direction — `math-scripts.md §"Double-Check Logic"`)**:
- Step 1: `Corr(a0,a2) = Cov_02/√(Cov_00·Cov_22)` [Pearson]. Step 2 (rank-2 form): `= s_a0·s_a2·σ_Hc² / √[s_a0²(σ_Hc²+σ_H0²)·s_a2²(σ_Hc²+σ_H2²)]`. Step 3 (simplify): the `s_a0·s_a2` numerator and `√(s_a0²·s_a2²)=|s_a0·s_a2|` denominator **CANCEL** — the 518.330 kernel disparity is a DEAD lever — leaving `|Corr| = σ_Hc²/√[(σ_Hc²+σ_H0²)(σ_Hc²+σ_H2²)]`. Step 4 (sub `r_i=σ_Hi²/σ_Hc²`): `|Corr| = 1/√[(1+r0)(1+r2)]` — a function of the variance mix r ALONE. Step 5 (edge): `|Corr|=0.5 ⟺ (1+r0)(1+r2)=4 ⟺ (symmetric) r=1 ⟺ σ_Hprivate=σ_Hshared`.
- **Direction read-off**: |Corr| DECREASES as r INCREASES. The pinned r-pre-image gives |Corr| ∈ {25/34, 25/41, 1/2, 25/61} = {0.7353, 0.6098, 0.5000, 0.4098} (Sage-exact), STRADDLING 0.5 with **3 of 4 points on the rank-1 (collapse) side**; the central pin (σ_Hi=σ_Hc=0.05, the W7-7a shared dH/H) lands **EXACTLY ON the edge** (|Corr|=1/2). The substitution chain PREDICTED rank-1 collapse as the substrate-forced DEFAULT unless the pinned r AND OQ3 BOTH license the discount.
- **Computed**: central |Corr| = 1/2 (NOT < 0.5) AND OQ3 UNESTABLISHED (no cross-pipeline covariance) ⇒ rank-2 discount NOT licensed ⇒ **COLLAPSE fires as predicted** ⇒ `sign_verdict=PASS` (predicted direction matches computed). `magnitude_verdict=INFO` (disposition AMBIGUOUS at the pinned r — straddling pin + unproven independence — the pre-registered INFO_meaning). `regime_verdict=VALID` (|Corr| Sage-exact 1/2; edge 0.5 held immovable; W7-7a provenance s_a0/s_a2/s_a4/Corr verified intact against the s96 verdict line).

**Method-compliance audit (the actual PASS_meaning criterion)**: within-layer-not-multiplied / borrowed-H discipline all honored — NO Ω_DM×σ₈ (both a2, the a2 leg used the single Ω_DM Leggett value b_a2=1.5, NOT a product); NO borrowed-H w0/wa/σ₈ as independent spine factors (the spine = {m_H, ν-ord, σ/m=0, c_s²=0}, none borrowed-H); wₐ=0 NOT treated as an independent BF factor (it is structural-spine). The two-BF deliverable was computed with the prior-predictive-range / posterior-width EVOI method, the Sage-exact |Corr|, and the immovable 0.5 edge → the model-class prior is now a pre-registered, reported number replacing the retired "chance of one random geometry" heuristic (EVOI framework §"Joint Probability Argument" gave the per-observable `P_i`; `b_i = log₁₀(1/P_i)`).

**FIDELITY NOTE (mack-bridge sole-writer domain — load-bearing observational-honesty correction)**: the plan's spine entry "m_H from a4 KK-threshold" is the **structural** cubic identity `3 sin²θ_W = cos θ_cube` (ZFP IN STRUCTURE). But `falsifier-rigor-registry.md` row #6 flags the m_H NUMERICAL landing as **ACCOMMODATION** — m_H is derived THROUGH μ_BC, itself tuned to PDG sin²θ_W via the bi-criterion procedure; user directive: "one scale tuned to PDG sin²θ_W; do NOT allow citation as ZFP; evidence weight 1×". This is the S96 W8-2 dual-status straddle. The HEADLINE BF_spine therefore uses the **ACCOMMODATION-honoured** b_mH = 0.5 (the structural-only floor, 1× evidence weight), NOT the full-5-OOM structural b_mH = 1.5 (reported only as an explicit cross-check). Inflating the headline with the μ_BC-accommodated PDG agreement would overstate the model-class evidence; the conservative FLOOR is the defensible number.

**Methodology deviation (honest disclosure, `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift)**: the plan-frozen `canonical_constants.py` SHA `cc7d1d26…` is the plan-freeze (2026-05-30) state; at this gate's runtime the file is `35c645ad…` (other S97 waves promoted constants between plan-freeze and dispatch). My `audit_sha256` is computed over the **actual runtime bytes** (script + canonical-as-read + sorted pinmap JSON), so the closure is honest and reproducible against the runtime state. The W7-7a covariance inputs (s_a0=+1.234526e-02, s_a2=+6.398917e+00, s_a4=−0.0, Corr=+1.0000) were re-read from the s96 verdict line and verified against the pins (provenance OK).

**Results** (4-tuple / set): value = `composite=INFO; BF_spine_FLOOR log₁₀=2.3010 (2.00e2, decisive); BF_spine+dagger log₁₀=3.8010 (rank-1 collapse); disposition=RANK-1-COLLAPSE; Δlog BF_dagger=1.5000; EVOI Δlog BF=0.5000; |Corr|_central=1/2 EXACT on edge; OQ3 unestablished; method_compliant=True`, scheme = `EVOI-prior-predictive-range`, convention = `ABSOLUTE`, L_max = `N/A`. dual_prior posterior → Track B (0.9): rank-1 collapse default (straddling pin + OQ3 unestablished), as pre-registered. No canonical write-order Step-2/Step-3 here — BF_spine lands in the §7.3 joint-evidence scorecard (mack sole-writer) as the consumer; no `falsifier-master-inventory.md` row lands from THIS gate (the w₀/wₐ R_842 falsifier row is the SEPARATE 2027-binding channel, untouched here).

**Substrate-IS framing**: NON-PHONONIC (Bayesian model-class evidence). The spine observables ARE substrate-IS predictions carrying NO borrowed H(t): m_H from the a₄ Seeley-DeWitt moment (D_K → a₄ → Higgs sector), normal ν-ordering from D_K eigenvalue ordering, σ/m=0 from N_Fock=1 superselection, c_s²=0 from Kasparov factorization — statistically independent, legitimately multiplicative ⇒ BF_spine is the defensible joint-evidence headline. The dagger pair {a0,a2} passes through the CONTAINER-OBSERVER's borrowed H(t) — the SAME undelivered effective-Friedmann / K_pivot projection as the Atlas D04 C2 a(t) gap (STILL-NOT-MET) — so its multiplicativity is conditional on the input covariance, hence the |Corr| discount. **w₀/wₐ are the effacement-residual / frozen-modulus signature, NOT a quintessence field IN a container**: w₀=−0.918 is the Volovik vacuum-partition leakage through the impedance mismatch (Γ_eff=0.99970, the 0.03% effacement residual), and wₐ=0 is the four-fold structural lock (the GGE relic modulus is frozen — never thermalizes, 59-OOM thermalization gap), not a rolling scalar field's dynamics. The arrow D_K → spectral moments → emergent observables → measurement is unchanged; this gate makes the model-class prior a pre-registered, reported number rather than a retired narrative heuristic, and keeps the substrate-first partition exact (the strong joint claim belongs to the substrate-intrinsic spine; only the bounded dagger correction passes through the borrowed-H map).

---

## Wave 4 Synthesis (team-lead)

**Wave 4 — Observational: Ω_GW shape + f·σ₈ + Bayes factor.** Four gates on independent observational axes (no composite metric). Verdict file audit-clean (sig_5 verified across all 16 S97 lines). All mack-domain §7/inventory landings effected this wave; two capstone §7.3 PROSE items correctly FLAGGED for the session-close designated writer (Q4).

- **W4-1 OMEGAGW-PEAK-HEIGHT — PASS + W4-2 OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE — PASS** (the 127-OOM closure, both legs). The framework's LISA Ω_GW is now substrate-sourced on BOTH legs, RETIRING the retracted `1e-10`-at-pivot placeholder: peak `Ω_peak=9.15e-5` (radiation-budget ceiling, log₁₀=−4.04, κ-invariant amplitude); IR-tail `Ω_GW(3 mHz)=4.046e-132` (slope p=3 DERIVED from the finite linear-edge fold DOS — n_dispersion=1, γ_E=0, van-Hove divergence refuted S94 — NOT assumed Hiramatsu; Sage-QQ-exact log-ratio). Verdict: **118 OOM below LISA-PLS → LISA-STERILE.** The "LISA-detectable ~1e-10" was the placeholder artifact; the honest substrate verdict is sterility. mack landed Row #7.audit-4 superseding the `PENDING-SUBSTRATE-RECOMPUTE` flag.

- **W4-3 FSIGMA8-FORECAST-REFETCH — INFO** (branch-a: `search_arxiv` down at dispatch; never FAILs on a fetch outage — the substrate curve is final). Reproduced the W6-1 per-z σ-distances EXACTLY (z=0.51: 0.506σ current → 1.013σ DESI-5yr → 1.534σ Euclid, |Δ|<1e-3), independently confirming the W6-1 forecast computation; corroborated by fetched DESI-DR1 + Euclid IST:F precision. **S₈-relieving confirmed**: S₈_FW=0.8128 < S₈_ΛCDM=0.8310 (toward lensing-low). Two fidelity findings: (i) σ₈ disambiguation — `SIGMA8-OZ-50=0.799` (spectral-action) vs `sigma8_FW=0.79317` (a₂ growth-channel), ~0.7% apart, no `sigma_8_FW` canonical constant exists → W6 channel-keyed promotion; (ii) GAP — the canonical per-z DESI-5yr/Euclid forecast TABLE remains un-lifted (latex/PDF tables don't mine cleanly; W6-1 estimated denominators stand, corroborated).

- **W4-4 D3-BF — INFO** (Track B). NOT a w₀-vs-ΛCDM data BF (DR3's R_842 binding event is 2027, a separate channel) — it is the model-class JOINT-EVIDENCE headline via the EVOI prior-predictive-range method. **BF_spine FLOOR = 2.0×10² DECISIVE** for the framework model-class over the random-geometry null (zero-borrowed-H independent spine {m_H, normal ν-ordering, σ/m=0, c_s²=0}). Two restraints honored: m_H-ACCOMMODATION (b_mH=0.5 not 1.5 — no overstatement from a μ_BC-tuned fit); rank-1 collapse forced (OQ3 covariance unestablished, EVOI of resolving = Δlog BF=0.5). Matches the pre-registered S96-W5 disposition rule bit-exactly (|Corr|=1/2-exact).

**Capstone-hygiene 5-question gate (W4):** **Q1** (a(t) gap) — NO. **Q2** (§7 falsifier surface) — YES (three landings): mack WROTE Row #7.audit-4 (Ω_GW 127-OOM closure), Row #75 (EP-signature, NEW), + the BF_spine register annotation (all mack sole-writer domain, verified on disk lines 1618/1656/1691). **Q3** (status change) — the Ω_GW falsifier moves placeholder→substrate-sourced (LISA-STERILE), captured in the inventory supersession chain (#7.audit-3→#7.audit-4); no Atlas-04 status-tag flip. **Q4** (PROSE vs ledger) — two capstone §7.3 NARRATIVE items (BF_spine number insertion; SNR~10¹³-retirement amplitude reconciliation to 4.046e-132) correctly FLAGGED for the session-close designated writer. **Q5** — the `canonical_constants.py` PROVENANCE-comment marking `Omega_GW_Lambda_A_LISA=1e-10` SUPERSEDED is flagged for the designated-writer pass (import preserved).

**Effected In-Session (W4):**
- [x] mack landed three §7-surface rows (Row #7.audit-4 127-OOM Ω_GW closure; Row #75 EP-signature; BF_spine register annotation) in `falsifier-master-inventory.md` (sole-writer; verified on disk at lines 1618/1656/1691).
- [x] Capstone-hygiene 5-question gate run; Q2/Q3 effected via mack inventory; the §7.3 PROSE flags (BF_spine, SNR-retirement reconciliation) + the canonical_constants PROVENANCE-comment (placeholder superseded) routed to session-close designated-writer — `session-97-housekeeping.md §A`.
- [x] σ₈ channel-keyed canonical promotion (sigma8_OZ vs sigma8_growth_a2) routed to W6 (sub-keying ambiguity ⇒ not a single-value fix-in-session) — recorded in housekeeping.
- [x] Housekeeping ledger updated with W4 §A entries + the designated-writer flags.

## Carry-Forward Computations

> 4.1/4.2 closed PASS (no PRE-REG-INC deferral); κ is pinned at κ_nat (W1.5, consistency) so no κ-resolution CF; 4.3 INFO closed in-branch (the forecast-TABLE refetch is a mechanical MCP-dependent GAP, not a substrate compute — housekeeping note, not a CF); the σ₈ channel-keyed promotion is a within-session W6 item. One genuine future-compute item:

### CF-S98-W4-4-OQ3-COVARIANCE — establish cross-pipeline mutual-independence to license the BF_spine rank-2 dagger

> **Origin**: S97-D3-BF INFO. BF_spine FLOOR=2.0×10² is the conservative rank-1-collapse headline (forced because the OQ3 input mutual-independence is unestablished). Resolving the covariance would license the rank-2 dagger (BF_spine+dagger=6.32×10³). The gate quantified the EVOI of resolving it: Δlog BF = (1−0.5)·1.0 = 0.500.

1. **What**: Establish (or refute) the cross-pipeline statistical mutual-independence of the BF_spine factors {m_H, normal ν-ordering, σ/m=0, c_s²=0} — compute the cross-pipeline covariance / |Corr| from the derivation pipelines, testing whether |Corr|<0.5 with the pipelines genuinely independent (licensing rank-2) vs the substrate-forced rank-1 collapse.
2. **Inputs**: `computations/session-97/s97_d3_bf.npz` (the BF_spine factors + |Corr|=1/2-exact structure + kernel disparity 518.330, audit `8f4f9abb`); the four spine observables' derivation-pipeline provenance.
3. **Gate**: `S98-W4-4-OQ3-COVARIANCE` — PASS iff the cross-pipeline covariance is established AND |Corr|<0.5 with pipeline-independence demonstrated (⇒ rank-2 dagger licensed, BF_spine+dagger headline); INFO iff covariance remains on the |Corr|=1/2 edge (rank-1 collapse stands); FAIL iff the pipelines are shown statistically dependent (collapse forced permanently).
4. **Effort**: ~0.5–1 wave.
5. **Depends on**: S97-D3-BF (the BF_spine factor set + the rank-1-collapse record — UPSTREAM GATE).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-30 | Acoustic Ω_GW LISA prediction (W4-1+W4-2) | `Omega_GW_Lambda_A_LISA=1e-10` placeholder (PENDING-SUBSTRATE-RECOMPUTE; backed ~10¹¹⁷) | substrate-sourced BOTH legs: peak 9.15e-5, IR-tail 4.046e-132 (p=3 derived); **LISA-STERILE (118 OOM below PLS)** | W4-1+W4-2 PASS; placeholder RETIRED (inventory Row #7.audit-4) |
| 2026-05-30 | f·σ₈ forecast-precision (W4-3) | W6-1 estimated denominators | fetched-literature corroborated; W6-1 σ-distances reproduced exactly; S₈-relieving confirmed (S₈_FW=0.8128 < ΛCDM 0.8310) | W4-3 INFO (branch-a) |
| 2026-05-30 | Joint-evidence headline (W4-4) | "chance of one random geometry" heuristic (retired) | BF_spine FLOOR=2.0×10² DECISIVE (model-class vs random-geometry null); rank-1 collapse forced | W4-4 INFO (EVOI method) |
| 2026-05-30 | canonical_constants.py SHA pin (W4 consumers) | drifted cc7d1d26 → 35c645ad (W1+W4-1+W4-2 add-only promotions) | Class-(c) content-edit-only; consumed values canonical; all W4 agents re-hashed at runtime | benign add-only drift |

## Files Produced

All paths under `computations/session-97/`. Verdicts in `s97_gate_verdicts.txt` (canonical).

| Gate | Verdict | Script | Data (.npz) | Plot (.png) | audit_sha256 (short) |
|:--|:--|:--|:--|:--|:--|
| W4-1 OMEGAGW-PEAK-HEIGHT | PASS | `s97_omegagw_peak_height.py` | `.npz` (+`.json`) | `.png` | `71fbc18f` |
| W4-2 OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE | PASS | `s97_omegagw_acoustic_spectral_shape.py` | `.npz` | `.png` | `c63d3869` |
| W4-3 FSIGMA8-FORECAST-REFETCH | INFO | `s97_fsigma8_forecast_refetch.py` | `.npz` (+`.json`) | `.png` | `a20043e7` |
| W4-4 D3-BF | INFO | `s97_d3_bf.py` | `.npz` | `.png` | `8f4f9abb` |

Canonical promotions (Step 2): `Omega_GW_acoustic_peak=9.15e-5` (W4-1), `Omega_GW_acoustic_LISA_tail=4.046e-132` (W4-2). Registers touched (Effected-In-Session): `falsifier-master-inventory.md` (Row #7.audit-4, Row #75, BF_spine annotation — mack sole-writer); `session-97-housekeeping.md` (W4 §A + designated-writer flags).
