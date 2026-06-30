# Session 99 Wave 4 — Robustness / Determinacy Closures (Results Working Paper)

**Session**: 99 | **Wave**: 4 | **Plan**: session-99-plan-w4.md | **Theme**: robustness / determinacy closures (full-PV a₀/a₂ at L_max≥13 + κ-alt-observable scan)

## Gate Sections

### §W4-1. S99-W4-A0A2-LMAX13 (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S99-W4-A0A2-LMAX13`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (L_max-axis RD residual on the §8.5 tier-2 a₀/a₂ survival partition)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Extending the FULL-physical Pauli-Villars a₀/a₂ continuation to L_max ≥ 13 shrinks the within-family L_max drift d_PV below ε_FI = 0.05, promoting the capstone §8.5 tier-2 survival INFO → PASS.
**Plan reference**: `sessions/session-plan/session-99-plan-w4.md` §W4-1 (machinery pin, ε_FI threshold, [SIGN] substitution chain source, L_max≥13 feasibility pre-check).

**Verdict**: **FAIL** (composite). 3-tuple: `sign_verdict=FAIL`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`. The drift-shrink hypothesis is **falsified**: extending L_max 10→12→14 the within-family drift `d_PV` does **not** shrink toward ε_FI — it **grows** (`d_PV(L12)=0.057026 → d_PV(L14)=0.095397`). Track B is selected: the RD residual is a **structural property of the L_max axis**, not a vanishing truncation artifact.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("a0 a2 tier-2 PV invariance L_max drift survival FI eps_FI 0.05703")` → returned the closed gate `S98-A0A2-TIER2-PV-INVARIANCE` (INFO, `d(survival)/d(PV-scheme)=0`, `d_PV_within_family_drift=0.05702620`, both anchors byte-identical SURVIVE) + the `Lmax_drift_ratio=5.703pct` equation entry. **NOT PRE-CLOSED**: the S98 gate closed the PV-vs-Mellin axis (survival LABEL regulator-INVARIANT) but left the L_max-axis residual OPEN at the L10→L12 pair sitting in the INFO band. This gate is the genuine L_max-axis extension (carry-forward CF-S99-W5-A0A2-LMAX-PV-CONTINUATION [genuine-math]).
- `trace_entity("S98-A0A2-TIER2-PV-INVARIANCE")` → 2 gate hits (the V.8 INFO line + S-3 lineage) + the producing-script provenance (`s98_a0a2_tier2_pv_invariance.py`); confirmed the within-family drift machinery (`ratio_PV_L10/L12`, `d_PV`, `eps_FI`, `info_band`) lives in the V.8 npz.
- `get_constant("a_0_FW_zeta")` → 6440.0 (S88, non-superseded); `get_constant("a_2_FW_zeta")` → 2776.165389 (S88, non-superseded). Confirmed canonical; imported (not hardcoded).

**Output Artifacts** (verified on disk by content presence per `feedback_max-effort-full-fidelity.md`, NOT line counts):
- **script** `computations/session-99/s99_w4_a0a2_lmax13.py` — exists (42 720 B). `grep -cE 'from canonical_constants import'` → **1**; `grep -cE 'print_verdict_payload'` → **2**. Both must_contain patterns PRESENT.
- **data** `computations/session-99/s99_w4_a0a2_lmax13.npz` — exists (15 043 B). Carries `ratio_PV_L10/L12/L14`, `d_PV_L12/L14`, `drift_shrinks`, `eps_FI`, `info_band`, the FULL-PV moments (`a0_PV_L14`, `a2_PV_L14`, `a0_zeta_L14`, `a2_zeta_L14`), `truncation_consistent=True`, `fb_fallback=False`, the L10 reproduction cross-checks (`xc_a0pv_L10/xc_a2pv_L10/xc_ratio_L10=True`), and the 3-tuple + composite verdict.
- **plot** `computations/session-99/s99_w4_a0a2_lmax13.png` — exists (106 098 B). Left: `ratio_PV(L)` trajectory (L10/L12/L14) with the L10 anchor; right: `d_PV(L12)` vs `d_PV(L14)` against the ε_FI=0.05 / info_band=0.10 bands.
- **verdict_line** `computations/session-99/s99_gate_verdicts.txt` — canonical line PRESENT, matches `^S99-W4-A0A2-LMAX13:.* audit_sha256=[a-f0-9]{64}`; `audit_sha256=87bd25703eda1f7730d2b27dd7499df06ba20dc1fc09e52be6f44263ac1164ff`, `content_sha256=eb72a9db45b9c56ffb7da9cdf7a16e9c44d2e043dad03598fc0e26fdcb944c63`. Dual-SHA companion row PRESENT; **[SIGN] schema-v2 3-tuple row** PRESENT (`sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`); 2 extra companion rows (regulator_pin + DI1 scope). Emitted via the race-safe `emit_verdict` knowledge-MCP tool (NO open-coded append; sig_5 unique).

**Results**:

**NUMBERS (computed first):**

| L_max | ratio_PV(L) = a₀^PV/a₂^PV | signed Δ vs L10 | d_PV(L) = \|Δ\|/\|ratio(L10)\| | band |
|:------|:--------------------------|:----------------|:-------------------------------|:-----|
| 10 (anchor) | 0.5105953846 | — | 0 | — |
| 12 (S98 baseline) | 0.4814780709 | −0.029117 | **0.057026** | INFO (0.05, 0.10] |
| 14 (this gate) | 0.4618862409 | −0.048709 | **0.095397** | INFO band, but ≥ baseline |

- FULL-physical PV moments at L_max_operational=14: `a₀^ζ(L14)=3.3878×10³`, `a₂^ζ(L14)=2.3810×10⁴`, `a₀^PV(L14)=1.3333×10³`, `a₂^PV(L14)=2.8865×10³` (PV-subtracted with the physical set c_j={2,−1}, m_j²/M_KK²={1,2}, Λ_UV=M_KK; poleconv-A-double: a₀ at pole_in_s=4/n=0 → λ⁻⁸, a₂ at pole_in_s=3/n=2 → λ⁻⁶, d=8).
- **Machinery faithfulness cross-check (L10 reproduction from the L14 cache, p+q≤10):** `a₀^PV(L10)=1300.2094666` (S98 V.8 canon 1300.2094666, match), `a₂^PV(L10)=2546.4575393` (canon 2546.4575393, match), `ratio_PV(L10)=0.5105953846` (canon 0.5105953846, match). The L14-re-pointed evaluator reproduces the canonical L10 anchors to all printed digits — the FULL-physical PV math is byte-faithful to the S97 W2-1 / S98 V.8 evaluator; only the spectrum truncation changed.

**[SIGN] substitution chain (drift-shrink-direction claim, with substituted numbers):**
- Step 1 — `d_PV(L) := |ratio_PV(L) − ratio_PV(L10)| / |ratio_PV(L10)|`, `ratio_PV(L10)=0.510595` [S98 V.8 anchor]; `eps_FI=0.05` [capstone §8.5 tier-2 tolerance].
- Step 2 — `d_PV(L14) = |0.461886 − 0.510595| / |0.510595| = |−0.048709| / 0.510595`.
- Step 3 — `d_PV(L14) = 0.048709 / 0.510595 = 0.095397`.
- Step 4 (direction read-off) — the signed step L10→L12→L14 = `0.510595 → 0.481478 → 0.461886` is **monotonically DECREASING** (Δ₁₂=−0.029117, Δ₁₄=−0.048709), i.e. the ratio keeps moving **away** from the L10 anchor. The DRIFT-SHRINK hypothesis predicted `d_PV(L14) < d_PV(L12)=0.057026` (convergence toward ε_FI). **Computed: `d_PV(L14)=0.095397 > 0.057026` — the drift GREW by a factor 1.673; no convergence.** Friedrich-Bär truncation-saturation (new p+q∈{13,14} sectors λ⁻²ˢ-suppressed) does NOT dominate the ratio: the high-(p,q) sectors shift a₀^ζ and a₂^ζ by enough (a₂^ζ nearly doubles L10→L14) that the PV-subtracted ratio continues to drift.

**Gate (3-tuple per [SIGN], gate-verdicts.md composite-collapse rule):**
- `sign_verdict = FAIL` — the predicted convergent-decrease direction (`d_PV` shrinking toward ε_FI) does **not** match the computed direction; `d_PV(L14)=0.095397 ≥ d_PV(L12)=0.057026`, the drift increased.
- `magnitude_verdict = FAIL` — `d_PV(L14)=0.095397 ≥ d_PV(L12)` fires the rubric's "does-NOT-shrink" FAIL clause (FAIL_meaning: `≥ d_PV(L12)=0.05703`). (It is numerically still inside (0.05, 0.10], but the FAIL clause `≥ d_PV(L12)` triggers first; an INFO would require both `(0.05, 0.10]` **and** shrinking vs L12, which is false.)
- `regime_verdict = VALID` — deterministic Mellin–Dirichlet quadrature (mp.dps=50) on a finite L_max-truncated spectrum; no small-parameter / ODE-breakdown regime; `truncation_consistent=True`, `fb_fallback=False`.
- Composite — `sign_verdict==FAIL ⇒ FAIL`.

**L_max≥13 feasibility (LOAD-BEARING, `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`):** RESOLVED via the Casimir-bound + cache cross-check route (option 1). The L_max=14 master spectrum cache `computations/session-87/s87_spectrum_cache_L14_tau019.npz` (sha256 `fa2bfb83…`, 119 sectors, levels 0..14 contiguous) is ON DISK; `L_max_operational=14 ≥ L_max_plan=13` is achieved by re-pointing the GPU heat kernel to the cached L14 sector eigenvalues — **NO new irrep construction**, so the p+q≥13 timeout risk is structurally moot. `truncation_consistent=True` (all p+q≤14 sectors present, contiguous 0..14 ⇒ supplies every sector the bottom-K Mellin moment consumes). The FB-saturation analytic fallback was NOT engaged (`fb_fallback=False`); the verdict scheme carries no `-FB-SATURATION-ANALYTIC` suffix.

**Methodology note (shared-module discipline):** the L12-pinned `SPECTRUM_CACHE` inside `computations/_shared/_analytic_zeta.py` (a SHA-pinned input, sha256 `6383c87…`) was NOT edited or imported. The script reuses the module's EXACT Mellin↔Dirichlet math (`load_spectrum` filter logic + `_heat_kernel_gpu_factory` + mp.dps=50 quadrature, transcribed in-script as `load_spectrum_L14`/`hk_factory_L14`/`mellin_moment_pv`) re-pointed to the L14 cache. The L10 reproduction cross-check (all anchors matched to printed precision) confirms byte-faithfulness to the S97 W2-1 evaluator. `convention=…-PV-FULL-PHYSICAL`, `CLASS=FULL` ⇒ NO `-SCHEMATIC` suffix, NO `# tier_pin=TIER-2` row (S97 W2-1 / S98 V.8 FULL-side precedent, `substrate-first-canonical-sourcing.md §(iv)`).

**4-tuple output tag:** `(value=…d_PV_L14=0.095397…, scheme=TIER2-SURVIVAL-DUAL-ANCHOR-FI-vs-FULL-PV, convention=RATIO-LABEL-DISTANCE-poleconv-A-double-PV-FULL-PHYSICAL, L_max=13)`. Dual-SHA: `audit_sha256=87bd2570…`, `content_sha256=eb72a9db…`; 3-tuple `sign=FAIL magnitude=FAIL regime=VALID`. Artifacts `s99_w4_a0a2_lmax13.py/.npz/.png`.

**Substrate-first assessment (GEOMETRIC; what region of solution space this constrains):**

The arrow flows `D_K eigenvalues {λ_k, m_k} on (A_K^{≤L}, H_K^{≤L}, D_K^{≤L}) at τ_fold=0.190 → a₀ (zeroth, cosmological-term weight-0) / a₂ (second, Einstein-Hilbert weight-2) Seeley-DeWitt spectral moments → the §8.5 tier-2 survival partition`. The substrate **IS** the truncated spectral triple; a₀/a₂ is a substrate-IS read-off, not a laboratory measurement. This FAIL is an informative boundary, not a weakness:

- **Two-Layer reading (`epistemic-discipline.md §"Resolution-Specificity Scoping"`):**
  - **Layer 1 (pole-universal survival LABEL) — UNTOUCHED.** The §8.5 tier-2 a₀/a₂ SURVIVE label is regulator-INVARIANT (S98 V.8: byte-identical SURVIVE under both the FI-anchor 0.217563 and the full-PV anchor 0.510595; m_FI=m_PV=+1; Δ_survival_margin=0). This gate did NOT recompute the label and does NOT retract it. **No substrate-IS structural fact is retracted by this FAIL.**
  - **Layer 2 (L_max-axis RD residual) — the structural finding.** The residual regulator-DEPENDENCE on the L_max axis is **NOT** a vanishing truncation artifact. The within-family PV ratio drifts monotonically and *increasingly* with L_max (0.5106 → 0.4815 → 0.4619; d_PV growing 0.057 → 0.095). The L_max axis carries a genuine structural RD residual on the ratio **magnitude** — the surviving-side partition's signed position relative to the L10 anchor is L_max-sensitive, even though the surviving-side membership (the LABEL) is not.

- **Functional-sensitivity classification:** the survival LABEL is FUNCTIONAL-INDEPENDENT (regulator-INVARIANT across the FI/PV anchor family — a structural fact, capstone §8.2/§8.5). The ratio MAGNITUDE within the FULL-PV family is L_max-SCHEME-DEPENDENT: it does not converge to a continuum value across {L10, L12, L14}. This is consistent with the Lizzi-signature lesson that what is functional-independent is structural and what is functional-dependent must be determined — here the determination on the L_max axis returns "does not converge in [10,14]".

- **Solution-space update:** the L_max-axis-robustness corridor for promoting the §8.5 tier-2 survival INFO → PASS via L_max extension is **CLOSED** at the FULL-physical PV / [10,14] window. The §8.5 tier-2 survival stays **INFO** (Q3-NO on the capstone-hygiene 5-question gate: no PROVEN/CONDITIONAL/BROKEN/INFO status change — the cell was INFO and remains INFO; the tightened/grown drift is a ledger-row update, not a prose status flip). Per the plan's W4-1-FAIL routing + `feedback_fix-in-session-never-defer.md`, a corridor-mapping FAIL is **not** a carry-forward unless a higher-L_max cache (L≥16) becomes a genuine compute item; absent that, the FAIL closes this corridor and is not re-queued. The dual_prior discriminator re-allocates 0.9 to **Track B** (structural RD on the L_max axis).

- **Capstone-hygiene gate routing:** W4-1 FAIL touches NO capstone status-bearing claim above its register status (Layer-1 survival LABEL untouched). Q1–Q5 all NO ⇒ the standing 5-question gate fires no routing action for this gate (per `session-99-plan-w4.md §"Wave 4 → Wave 5 Decision Point"`: only a W4-1 PASS would have fired Q3-YES).

---

### §W4-2. S99-W4-KAPPA-ALT-OBSERVABLE-SCAN (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S99-W4-KAPPA-ALT-OBSERVABLE-SCAN`
**Trigger**: `[SIGN]`
**Classification**: **NON-PHONONIC** (κ-determinacy gate-OBJECT over substrate-IS seconds-scale observables)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: At least one κ-dependent substrate observable (complement of the closed CGWB-peak-frequency axis) lands in a realized detector/measurement band, which would upgrade κ from CONSISTENCY-PINNED to INDEPENDENTLY-PINNED.
**Plan reference**: `sessions/session-plan/session-99-plan-w4.md` §W4-2 (κ-dependent observable enumeration, realized-band membership gate, flat-grid discipline, S98 V.7 closed-axis baseline).

**Verdict**: **FAIL** — κ stays **CONSISTENCY-PINNED**.

Composite collapse (3-tuple): `sign_verdict=PASS`, `magnitude_verdict=FAIL`, `regime_verdict=VALID` ⇒ `magnitude=FAIL ∧ regime=VALID ⇒ composite=FAIL` (per `gate-verdicts.md` composite-collapse rule; cross-checked in-script via `assert composite_check == verdict`). Every enumerated κ-dependent complement observable is out-of-band at κ_nat; no marginal-edge hit ⇒ a clean (non-marginal) FAIL, not INFO.

**Output Artifacts**:

- **script** `computations/session-99/s99_w4_kappa_alt_observable_scan.py` (26,839 bytes) — `ls` confirms on disk. `must_contain` grep:
  ```
  60:from canonical_constants import (  # noqa: E402
  127:def print_verdict_payload(verdict, value, audit_sha, content_sha,
  484:    print_verdict_payload(
  ```
- **data** `computations/session-99/s99_w4_kappa_alt_observable_scan.npz` (11,761 bytes) — on disk; carries `kappa_grid` (121), `f_obs_nat`/`t_obs_nat`/`in_band_nat`/`nearest_gap_dec` per observable, `count_in_band_nat=0`, `n_grid_in_band=71`, `kappa_status`, band edges, dual-SHA, 3-tuple.
- **plot** `computations/session-99/s99_w4_kappa_alt_observable_scan.png` (88,808 bytes) — on disk; complement observables on the log-frequency axis vs the shaded {PTA, LISA, LIGO/ET, resonant-HF} bands + the excluded CGWB-peak reference line.
- **verdict_line** `computations/session-99/s99_gate_verdicts.txt` — emitted via the race-safe `mcp__knowledge__emit_verdict` MCP tool (5 rows: canonical + dual-SHA companion + [SIGN] schema-v2 3-tuple + 2 annotation rows). `must_contain` grep `^S99-W4-KAPPA-ALT-OBSERVABLE-SCAN:.* audit_sha256=[a-f0-9]{64}`:
  ```
  S99-W4-KAPPA-ALT-OBSERVABLE-SCAN: FAIL -- value='complement_in_band_count=0;member_of_any_band=False;nearest_obs=relic_coherence_time;nearest_gap=+25.157dec;grid_in_band_pts=71/121;CGWB_freq_axis_excluded=True(S98_V7_FAIL_10d31d0e,+28.929dec);kappa_status=CONSISTENCY-PINNED' scheme=FW convention=ABSOLUTE L_max=N/A audit_sha256=7f796ea7a38657662f17623240648c28e2899997212bcbcea0cb51d8ffea66f0 content_sha256=b8bf6360aab6ee42b48509da01a214ee609e4fb034e0d5dc5d762b02b51d929c schema_version=S84+
  # sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID # S99-W4-KAPPA-ALT-OBSERVABLE-SCAN 3-tuple annotation (schema-v2)
  ```
- **4-tuple**: `(value='complement_in_band_count=0;…;kappa_status=CONSISTENCY-PINNED', scheme=FW, convention=ABSOLUTE, L_max=N/A)`.
- **dual-SHA**: `audit_sha256=7f796ea7a38657662f17623240648c28e2899997212bcbcea0cb51d8ffea66f0`, `content_sha256=b8bf6360aab6ee42b48509da01a214ee609e4fb034e0d5dc5d762b02b51d929c`.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):

- `get_constant("M_KK_inv_seconds")` → `8.860439881925477e-42` (S96, source `s96_w1_mkk_seconds.npz`, gate `S96-W1-MKK-SECONDS`; Superseded=False). Matches the spawn-prompt pin; κ_nat confirmed canonical.
- `trace_entity("S98-KAPPA-INDEP-FROM-CGWB-FREQ")` → gate hit: `value='f_obs=8.4835e+39Hz(log10=39.9286);member_of_any_band=False;nearest_horizon=resonant_HF_ceiling_1e+11;nearest_gap=+28.929dec_ABOVE;…'`. Confirms the closed-axis baseline (audit 10d31d0e) and that ONLY the CGWB-FREQUENCY axis is closed.
- `search_knowledge("kappa determinacy seconds-scale observable independent pin transport knob")` → nearest neighbours `S97-COOLING-BUDGET-KAPPA-PIN` (PASS; `kappa-indep; in_band_1e-20_1e-10=False; decades_below_band=21`) and `S98-KAPPA-INDEP-FROM-CGWB-FREQ` (FAIL). **No** gate matching `KAPPA-ALT-OBSERVABLE` / a complement-set scan exists. **NOT PRE-CLOSED** — the complement observable set is unscanned; gate is genuinely open.

**Results**:

*Transport convention (substrate-first; VERIFIED against the S98 V.7 baseline).* κ = M_KK⁻¹ is the emergent transport knob mapping dimensionless substrate-IS quantities into laboratory seconds/Hz: a dimensionless FREQUENCY f̃ (M_KK units) → `f_obs = f̃ · (1/κ)` [Hz]; a dimensionless TIME t̃ → `t_obs = t̃ · κ` [s], frequency image `f_obs = (1/t̃)·(1/κ)`. With κ_nat = ℏ/M_KK = 8.860439881925477e-42 s, the M_KK frequency scale is `1/κ_nat = 1.128612e+41 Hz`. The script reproduces the closed-axis baseline byte-exactly: `f̃_peak = f_obs_baseline·κ_nat = 0.075168` ⇒ `f_obs = 8.4835e+39 Hz` (= S98 V.7 `f_peak_Hz`; assert passes at rel 1e-9). The S98 V.7 verdict line is present, FAIL, and audit `10d31d0e` matches.

*Flat-grid discipline (plan note honored).* `Omega_peak_grid` is FLAT at 9.15e-5 across all 121 κ (max−min spread = 0.000e+00) — the κ-INDEPENDENT amplitude is NOT a candidate. The scan enumerates frequency/time-scale-type observables ONLY.

*Complement observable enumeration (κ-VARYING; frequency/time-scale-type; complement of the CGWB-peak frequency), evaluated at κ_nat:*

| Observable | kind | f̃ (M_KK units) | t_obs [s] | f_obs [Hz] | in-band? | nearest band (gap, dec) |
|:-----------|:-----|:---------------:|:---------:|:----------:|:--------:|:-----------------------:|
| transit_timescale (`dt_transit`=1.130e-3) | time | 8.848e+02 | 1.001e-44 | 9.986e+43 | **No** | resonant_HF (+32.999) |
| acoustic_period (`T_acoustic`=0.112) | time | 8.929e+00 | 9.924e-43 | 1.008e+42 | **No** | resonant_HF (+31.003) |
| acoustic_frequency (`f_acoustic`=1.0) | freq | 1.000e+00 | 8.860e-42 | 1.129e+41 | **No** | resonant_HF (+30.053) |
| relic_coherence_time (`tau_GGE_K_unit`=78600) | time | 1.272e-05 | 6.964e-37 | 1.436e+36 | **No** | resonant_HF (+25.157) |
| dephasing_time (`t_deph`=`t_deph/t_transit·dt_transit`=8.876e-1) | time | 6.332e-03 | 1.399e-39 | 7.147e+38 | **No** | resonant_HF (+27.854) |

All five complement observables map **+25 to +33 decades ABOVE** the resonant-HF ceiling (1e11 Hz) at κ_nat. `count(O_i(κ_nat) in-band) = 0`. Nearest approach: `relic_coherence_time` at +25.157 dec above the ceiling (the longest dimensionless timescale, f̃≈1.27e-5, gets closest but is still 25 decades out). No observable lies within the marginal tolerance (|gap| ≤ 0.30 dec of any band edge) ⇒ FAIL, not INFO.

*Detector/measurement band union (the S98 V.7 horizon union).* `{PTA [1e-9,1e-7], LISA [1e-4,1e-1], LIGO/ET [1e1,1e4], resonant_HF [1e3,1e11]}` Hz; global floor 1e-9 Hz (PTA), global ceiling 1e11 Hz (resonant-HF, the S98 V.7 `nearest_horizon`). No realized NON-GW measurement band (laboratory clock/spectroscopy) reaches the M_KK-frequency scale 1/κ_nat ≈ 1.1e41 Hz, so no non-GW band admits a κ-set substrate seconds-scale observable; the GW horizon union is the operative band set.

*Grid-reachability diagnostic (NOT the gate verdict).* Sweeping the full 121-pt κ-grid κ∈[1e-20,1e-10], 71/121 κ-points land ≥1 complement observable in-band (relic_coherence_time 71, dephasing_time 39, acoustic_frequency 13, acoustic_period 1, transit_timescale 0). In-band membership IS reachable *somewhere* on the candidate window — but NOT at the substrate-natural κ_nat = 8.86e-42 s, which sits 22 decades below the band-membership window for these observables. The determinacy verdict keys on κ_nat (the substrate-natural value); the grid sweep confirms band-membership is not vacuous, but it does not supply an *independent* (non-consistency) anchor that selects κ_nat.

*[SIGN] substitution chain (in-band-vs-out-of-band direction), with substituted numbers.* Step 4 of the plan's substitution chain registers the OPEN possibilities IN-BAND (≥1 complement obs in a realized band ⇒ κ INDEPENDENTLY-PINNED) vs OUT-OF-BAND (every complement obs strictly outside all bands ⇒ κ stays CONSISTENCY-PINNED). Computed: for the nearest-approach observable, `f_obs(relic_coherence_time, κ_nat) = (1/tau_GGE_K_unit)·(1/κ_nat) = 1.272e-5 · 1.1286e+41 = 1.436e+36 Hz`; `log10(f_obs) − log10(band_ceiling) = 36.157 − 11 = +25.157 dec ABOVE` ⇒ `member_of_any_band = False`. Every other complement observable is farther out. `sign_verdict = PASS` (the computed in/out-of-band determination matches the enumeration's set-membership read-off for all five observables); `magnitude_verdict = FAIL` (count-in-band = 0, no marginal hit); `regime_verdict = VALID` (the transport map `f_obs = f̃/κ` is exact, no small-parameter expansion; band-membership exact over the full window). The directional pre-registration was genuinely open — the FAIL is the OUT-OF-BAND branch, computed, not assumed.

*Solution-space interpretation (substrate-first; not a defect).* GEOMETRIC/substrate read of the arrow: `D_K eigenvalues → dimensionless substrate-IS observable (transit/acoustic/relic timescale at τ_fold) → (× κ^p) → laboratory seconds-scale image → detector-band membership`. The gate-OBJECT (does an independent κ-pin exist?) is the only NON-PHONONIC element; it does NOT invert the substrate-first direction (κ is the emergent transport leg, not a substrate primitive). Combined with S98 V.7 (CGWB-frequency axis closed, +28.9 dec out), this gate closes the COMPLEMENT observable set: the κ-determinacy corridor is now mapped as closed across BOTH the frequency axis and the time-scale complement. Per the dual-prior, FAIL re-allocates 0.9 → Track B (no independent pin; κ stays CONSISTENCY-PINNED, determinacy open BY DESIGN). This is **STRUCTURALLY-OPEN-BY-DESIGN**, NOT a deficiency: κ's epistemic status is LOW leverage (Tier-3/4) — it does NOT gate any observational prediction. No substrate-IS structural fact is retracted; the seconds-scale predictions themselves stand (they are real κ-images, just far from realized GW bands at κ_nat). Per `feedback_fix-in-session-never-defer.md`, a corridor-mapping FAIL is NOT a carry-forward; the corridor is mapped and not re-queued. No falsifier-master-inventory landing is triggered (a PASS-only routing action; this is a FAIL).

---

## Wave 4 Synthesis (team-lead)

**W4-1 `S99-W4-A0A2-LMAX13` — FAIL** (3-tuple sign=FAIL, magnitude=FAIL, regime=VALID; Track B). Extending the FULL-physical Pauli-Villars a₀/a₂ continuation to L_max=14 (on-disk L14 cache, no new diagonalization), the within-family drift d_PV does NOT shrink toward ε_FI=0.05 — it GROWS: d_PV(L12) = 0.05703 → d_PV(L14) = 0.09540 (ratio_PV L10/L12/L14 = 0.5106 / 0.4815 / 0.4619). The RD residual is a STRUCTURAL property of the L_max axis (Two-Layer reading per `epistemic-discipline.md §"Resolution-Specificity Scoping"`: Layer-1 survival LABEL untouched/regulator-INVARIANT per S98 V.8 byte-identical; Layer-2 L_max-axis RD residual is the structural finding). The capstone §8.5 tier-2 survival stays INFO; the L_max-extension INFO→PASS promotion corridor is CLOSED at the FULL-PV/[10,14] window. **No substrate-IS fact retracted.**

**W4-2 `S99-W4-KAPPA-ALT-OBSERVABLE-SCAN` — FAIL** (3-tuple sign=PASS, magnitude=FAIL, regime=VALID). All 5 enumerated κ-dependent complement observables (frequency/time-scale-type) map +25 to +33 decades ABOVE the resonant-HF ceiling at κ_nat; count(in-band) = 0. κ stays CONSISTENCY-PINNED. With the CGWB-frequency axis already closed (S98 V.7, +28.9 dec), the κ-determinacy corridor is now mapped closed across BOTH the frequency axis AND the time-scale complement set — STRUCTURALLY-OPEN-BY-DESIGN (LOW leverage; κ does not gate any observational prediction).

Solution-space: both robustness/determinacy corridors are MAPPED, not failed — the a₀/a₂ survival LABEL is regulator-invariant with the L_max-axis RD residual now characterized as a structural feature; the κ-determinacy question is closed-by-design across both observable axes.

**Carry-Forward Computations (math)**: none — both FAILs MAP corridors (per `feedback_fix-in-session-never-defer.md`, a corridor-mapping FAIL is not future work). W4-1 re-queues ONLY if an L≥16 cache becomes a genuine compute item (NOT pre-registered this session). **Effected In-Session (non-math)**: the §8.5 tier-2 survival cell stays INFO (W4-1 FAIL — ledger-row drift update, NO prose status change ⇒ capstone-hygiene Q3-NO for W4-1); recorded in `session-99-housekeeping.md §A`.

## Carry-Forward Computations

No carry-forwards: both Wave-4 outcomes are corridor-mapping FAILs closed in-session (W4-1 RD-structural on the L_max axis; W4-2 κ STRUCTURALLY-OPEN-BY-DESIGN). Neither admits a 4-field genuine-future-compute spec — re-queue W4-1 only if an L≥16 spectrum cache becomes a genuine compute item.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-01 | §8.5 tier-2 a₀/a₂ survival (L_max-axis RD residual) | INFO (d_PV(L12)=0.05703 in (0.05,0.10]) | INFO (stays; L_max-extension INFO→PASS corridor CLOSED) | S99 W4-1 FAIL: d_PV GROWS 0.057→0.095 at L14; RD structural on L_max axis; survival LABEL regulator-INVARIANT, untouched |
| 2026-06-01 | κ epistemic status (M_KK⁻¹→seconds determinacy) | CONSISTENCY-PINNED (CGWB-freq axis closed, S98 V.7) | CONSISTENCY-PINNED (corridor mapped closed across freq + complement axes) | S99 W4-2 FAIL: 5 complement observables +25 to +33 dec out-of-band at κ_nat; STRUCTURALLY-OPEN-BY-DESIGN |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| S99-W4-A0A2-LMAX13 | `computations/session-99/s99_w4_a0a2_lmax13.py` | `s99_w4_a0a2_lmax13.npz` | `s99_w4_a0a2_lmax13.png` | FAIL (audit `87bd2570…`) |
| S99-W4-KAPPA-ALT-OBSERVABLE-SCAN | `computations/session-99/s99_w4_kappa_alt_observable_scan.py` | `s99_w4_kappa_alt_observable_scan.npz` | `s99_w4_kappa_alt_observable_scan.png` | FAIL (audit `7f796ea7…`) |
