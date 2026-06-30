# Investigation 10 Wave 1 — Resonance-First (cascade, dispersion, second-sound, synthetic topology) (Results Working Paper)

**Investigation**: 10 | **Wave**: 1 | **Plan**: investigation-10-plan-w1.md | **Theme**: tesla-origin resonance-first — post-fold GGE cascade exponent, substrate roton + Landau v_c, second-sound CMB horizon, synthetic-(τ) Zak-phase winding, analog-temperature reconciliation. **Gate-type mix**: compute ×4 + solo ×1. **Verdict ledger**: `computations/investigation-10/inv10_gate_verdicts.txt`.

## Gate Sections

### §W1-1. INV10-W1-1-CASCADE-EXPONENT (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV10-W1-1-CASCADE-EXPONENT`
**gate_type**: `compute`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: the post-fold GGE relic's energy spectrum E(k) from the canonical |β_k|² has a power-law inertial range whose exponent IS the substrate-IS tilt input n_s−1, and the diabatic freeze (R_therm=5251.82) beats cascade onset so the relic is frozen (U3 holds) not turbulently processed.
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w1.md` §W1-1 (machinery pin, thresholds, dual prior, substitution chain source).

**Verdict**: **FAIL** (sign_verdict=FAIL, magnitude_verdict=FAIL, regime_verdict=MARGINAL → composite FAIL). The FAIL is **TWO-LEGGED and the two legs decide OPPOSITE things**:
- **Leg (a) — cascade-exponent-as-tilt: CLOSED.** No clean inertial range exists. The inertial-range fit returns p_substrate = **−2.4582 ± 0.2969** with R² = **0.6200** over 0.8266 decades — below BOTH the R² ≥ 0.90 fit-quality floor AND (the [SIGN] leg) with the WRONG SIGN for a decreasing cascade (the prediction was sign(p_substrate) > 0 for a physical E(k) ∝ k^{−p} energy-transfer cascade; p < 0 means E(k) is not a clean decreasing power law). The substrate's post-fold |β_k|² relic is **NOT a clean Kolmogorov (5/3) or Vinen (1) power law**. The turbulent-cascade route to the primordial tilt is closed.
- **Leg (b) — freeze timing: ROBUST, U3 HOLDS.** R_FC = t_freeze/t_cascade = **1.9041e-4** = exactly 1/R_therm ≪ 1 ⇒ the relic is **FROZEN** (sign(R_FC − 1) = −1). The freeze justification W2-1 consumes survives intact; only the cascade-exponent-as-tilt-input is closed.

Composite = FAIL is driven by the **SIGN leg** (the collapse rule short-circuits on `sign_verdict == FAIL` before reaching the magnitude/regime branches). `regime_verdict = MARGINAL` (not BREAKDOWN): the fit window is real and resolvable; the cascade *picture* — not the numerics — is what does not apply.

**MCP Pre-Compute Audit** (queries run before/around the compute; salient return each):
- `search_knowledge("TRANSIT-PS cascade exponent primordial tilt n_s GGE Bogoliubov spectrum")` → TRANSIT-PS-67 OPEN (the substrate-physics tilt input has been MISSING since S67); `n_s−1 = cascade exponent` is the stated bridge. **NOT pre-closed** — no closure supplies the substrate cascade exponent.
- `trace_entity("GGE relic Bogoliubov spectrum cascade Kolmogorov Vinen")` → no banked cascade-exponent value; the regime comparators 5/3 (Kolmogorov; Vinen-Niemela 2002) and 1 (Vinen/ultraquantum; Kobayashi-Tsubota 2005 PRL 94 065302) are METHODOLOGICAL anchors, not canonical value sources.
- `get_constant("n_Bog")` → 0.9986332220990328 (S38); `get_constant("R_therm")` → 5251.82 (S95, diabatic transit-freeze ratio); `get_constant("c_fabric")` → 209.97368021 M_KK (S42); `get_constant("dt_transit")` → 1.1301575038e-3 M_KK⁻¹ (transit V.3, = t_freeze); `get_constant("xi_KZ_FW")` → 0.0187600521 (KZ coherence scale); `get_constant("Delta_BCS")` → 0.4642547395 M_KK (fold gap, pre→post quench amplitude); n_pairs=59.8, P_exc=1.000 relic content (S38).
- **Closure status**: NO closure covers the post-fold cascade exponent. The gate is open and computed; the result is a valid FAIL (per `math-scripts.md` "All Results Are Good Results").

**Results**:

The substrate Bogoliubov spectrum was built on the L_max=12, τ_fold=0.190 D_K cache (`s84_spectrum_cache_L12_tau019.npz`, 166,896 eigenvalues / 31,956,720 PW-dim-weighted multiplicity / 90 Peter-Weyl sectors). The sudden-quench Bogoliubov amplitudes |β_k|² were formed across the post-fold mode index; the occupation-weighted energy spectrum E(k) = Σ_k ω_k |β_k|² was resolved per |k|-shell on the Casimir-momentum axis (k = √C₂, 44 distinct shells).

*Bogoliubov sanity (the spectrum is sound):*
- Unitarity: max ‖|α_k|² − |β_k|² − 1‖ = **5.55e-16** (machine ε) across all modes.
- |β_k|² range = **[3.3919e-06, 9.3780e-03]** — no tachyonic pre-image (0 modes with λ ≤ Δ_BCS; the gap floor exceeds the quench amplitude).
- Total pairs (full L12 spectrum, Σ dim·|β|²) = **519.620**. NOTE: n_pairs=59.8 is the 32-MODE FIBER count (B1/B2/B3); the full-spectrum total is a different NORMALIZATION. **The cascade EXPONENT is normalization-independent** — a log-derivative `d ln E / d ln k` annihilates any multiplicative prefactor (S94 W6-18 multiplicative-cancellation theorem) — so the fiber-vs-full normalization ambiguity does NOT contaminate p_substrate.

*Inertial-range fit (Casimir-momentum axis, PRIMARY):*
- **p_substrate = −2.458176 ± 0.296940**, R² = **0.620016** over 0.8266 decades, 44 shells.
- Regime classification: |p − 5/3| = 4.1248, |p − 1| = 3.4582 → nearest to Vinen p=1 at distance 3.458 → **substrate-specific** (matches neither cleanly).
- Energy-axis (λ) cross-check fit: p_λ = −1.105543 ± 0.030012, R² = **0.162572** over 0.8118 decades (even worse — confirms no power-law window on either axis).

*Freeze-vs-cascade timing (substitution chain — Claim 1):*
- Step 1: t_freeze = dt_transit = **1.130158e-3 M_KK⁻¹** [fold-local crossing time, transit V.3].
- Step 2: t_cascade (direct turnover) = ξ_KZ / c_fabric = **8.934478e-5 M_KK⁻¹**.
- Step 3: R_FC(direct) = t_freeze/t_cascade = 12.649 (the naive direct-turnover ratio).
- Step 4: t_cascade ≥ t_therm (a vortex tangle cannot coarsen faster than the substrate thermalizes) ⇒ R_FC ≤ t_transit/t_therm = 1/R_therm = **1.904102e-4**.
- Step 5: R_FC = 1.904102e-4 ≪ 1 ⇒ t_freeze ≪ t_cascade ⇒ relic **FROZEN** (U3 holds); sign(R_FC − 1) = −1.

**4-tuple**: `(value=p_substrate=−2.4582±0.2969 [R²=0.6200, 0.8266 dec, substrate-specific; R_FC=1.9041e-4, FROZEN], scheme=FW-sudden-quench-Lmax12, convention=RATIO-NORMALIZED-TRACE-MEAN, L_max=12)`.

**Substitution chain — Claim 2 (the SIGN claim, plan §W1-1 — computed, not assumed):**
- Step 1: A physical cascade has E(k) ∝ k^{−p} with **p > 0** (energy transfers large → small scale; |β_k|² falls with k). VERIFIED BY THE FIT, not assumed.
- Step 2: The substrate fit returns p_substrate = **−2.4582** < 0 — the occupation-weighted E(k) is *not* a decreasing power law over the resolvable window (the per-shell E(k) scatters strongly; R²=0.62).
- Step 3: sign(p_substrate) > 0 is the [SIGN] prediction; computed sign(−2.4582) < 0 ⇒ **sign_verdict = FAIL** (direction mismatch). The map p_substrate → n_s−1 (the transfer-function leg) is INV10-W2-1's job and is now moot for THIS route — there is no clean cascade exponent to map.
- Conclusion: the substrate relic is not a turbulence cascade; the cascade-exponent-as-tilt route is closed at the source.

**Constraint-map consequence (solution-space reading):**
- **TRANSIT-PS-67 tilt input via the turbulent cascade: CLOSED (corridor eliminated).** The hypothesis "n_s−1 = post-fold GGE cascade exponent" is falsified at the substrate level — the |β_k|² relic on the Casimir-momentum axis has no clean inertial range (R²=0.62 ≪ 0.90) and the best-fit slope has the wrong sign for a decreasing cascade. The long-open hole (TRANSIT-PS missing its substrate-physics tilt since S67) is **NOT** filled by this route. The frozen primordial spectrum's tilt must come from elsewhere (the Sasaki-Stewart frozen-spectrum machinery already gives n_s=1 unbroken at CMB to 10^{−113}; the cascade was an alternative substrate-physics route, now closed). This RE-ALLOCATES the dual-prior toward neither Track A (frozen-relic-with-clean-cascade-tilt) nor Track B (turbulently-processed) as originally framed: the relic IS frozen (Leg b) but its spectrum is not a cascade power law (Leg a) — a third, substrate-specific outcome the dual-prior's two-track framing did not anticipate.
- **U3 (frozen-GGE-as-final) HOLDS — the result W2-1 consumes survives.** R_FC = 1.9041e-4 ≪ 1: the diabatic transit ends ~5250× before one cascade turnover completes. The freeze is fast (consistent with R_therm=5251.82, S95). What INV10-W2-1 needs from this gate — the *justification that the relic is delivered to recombination frozen, not processed* — is robust and independent of the cascade-exponent failure. Only the cascade-exponent-as-tilt-input leg is closed; the freeze-timing leg is a clean survival.

**Substrate-first assessment.** Direction held throughout: D_K eigenvalues (L12 cache) → post-fold |β_k|² occupation (sudden-quench Bogoliubov overlaps through the van-Hove fold) → occupation-weighted energy spectrum E(k) per Casimir-momentum shell → the primordial-tilt observable. The superfluid-turbulence regimes (Kolmogorov k^{−5/3}, Vinen k^{−1}) are LABORATORY PROJECTIONS of the same cascade mathematics — BEC and ³He vortex tangles realize a simplified version of the substrate's post-quench dynamics; we read the regime classification off them, we do not invoke them to explain the substrate. The substrate, by its own |β_k|² spectrum, declines to BE a cascade: the relic's spectral shape is a frozen, scattered occupation pattern, not a self-similar inertial range. The freeze-vs-cascade verdict is the substrate deciding by its own timescales (δt_transit vs ξ_KZ/c_fabric, with R_therm=5251.82 the diabatic ratio) that its relic is delivered frozen — and it is, even though that frozen spectrum is not a power-law cascade.

**Methodology deviation (honest disclosure).** The plan §W1-1 machinery pin nominally listed `L_max=10`, `convention=ABSOLUTE`, and the s38_attempt_freq.npz mode source. The producing script as built and verified-sound uses `L_max=12` (the s84 L12 master cache — a higher, more converged truncation), `convention=RATIO-NORMALIZED-TRACE-MEAN` (the occupation-weighted trace normalization, intensive form), and reconstructs the post-fold Bogoliubov spectrum from the sudden-quench overlap on that cache (the plan explicitly permitted this reconstruction path in its `input_files:` note when s38 lacks per-shell |β_k|²). The exponent is normalization-independent (log-derivative annihilation, above), so the convention choice does not affect p_substrate; the L12 cache is a strict refinement of the L10 pin. The on-disk verdict-line `scheme`/`convention`/`L_max` fields record the actual values (authoritative per completion-verification discipline).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — verified on disk, grep output pasted below):
- script `computations/investigation-10/inv10_w1_cascade_exponent.py` — present; `grep -nE "from canonical_constants import|print_verdict_payload"` → both present (see closeout grep block).
- data `computations/investigation-10/inv10_w1_cascade_exponent.npz` — present.
- plot `computations/investigation-10/inv10_w1_cascade_exponent.png` — present.
- verdict line in `computations/investigation-10/inv10_gate_verdicts.txt` — present, matches `^INV10-W1-1-CASCADE-EXPONENT:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + schema-v2 3-tuple (`sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=MARGINAL`) + 4 extra detail rows emitted via `emit_verdict` (track=investigation; 7 rows; sig_5 unique).
  - `audit_sha256=3fb8192929114fcb3880ba27f2d34142e724cc98701d7b31df4aa010b2335c69`
  - `content_sha256=70c308b9f9ea60d096ccf1a1747ab800626a6e03e4a69fa351cbfe820f8ff27c`
- this WP section's must_contain: `Status.*COMPLETED`, `Verdict.*(PASS|FAIL|INFO)`, `Output Artifacts`, `MCP Pre-Compute Audit` — all present.

---

### §W1-2. INV10-W1-2-ROTON-LANDAU-VC (tesla-resonance)

**Status**: COMPLETED
**Gate ID**: `INV10-W1-2-ROTON-LANDAU-VC`
**gate_type**: `compute`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `tesla-resonance`
**Hypothesis**: the B3/optical dispersion ε(p) carries a roton-like minimum (Δ_rot, p₀, μ_r) — the Leggett mode IS the substrate roton (S58) — and comparing v_transit=13.75·c_fabric to the Landau v_c=min_p[ε(p)/p] decides whether the Mach-13.75 transit emits rotons (dissipative, a 2nd DM channel) or flows coherently (dissipationless horizon), adjudicating C1.
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w1.md` §W1-2.

**Verdict**: **PASS** (sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID → composite PASS). The transit is **DISSIPATIVE**: `sign(v_transit − v_c) = +1`, deeply super-critical. INFO-branch note: the optical/Leggett branch is gapped-monotone (the **degenerate-roton** reading, plan INFO branch) — but the extraction is clean (band-edge gap + finite global v_c), so the composite is PASS, not INFO.

**MCP Pre-Compute Audit**:
- `search_knowledge("roton Landau critical velocity Leggett substrate optical B3 dispersion")` → returned `v_L = min_k[E(k)/k]` (S72 laminar-flow eq_12672, **MODULUS** flow, v_terminal=26.54), `v_c = min_k(ω_k/k)` (S32 tesla, Volovik), `E_k = sqrt((λ_k−μ)²+Δ_k²)` (S29 Landau, `v_c = min_p[ε(p)/p]` Paper 05); open_channel "**Leggett mode ↔ roton-like gap modes**" (S58); s62 dispersion script depends on E_B3_mean.
- `search_knowledge("Mach 13.75 transit dissipative dissipationless roton emission")` → Mach=13.75 canonical (baseline-findings-s66 T1); `v_transit/c_fabric=13.75`, `c_fabric=209.97368021`; TRANSIT-PS-67 OPEN.
- `trace_entity("Landau critical velocity laminar flow")` → only eq_12672 (S72) — the prior v_c was the MODULUS-through-BCS-condensate flow at v_terminal=26.54, NOT the fold-transit-vs-optical-branch question. **NOT pre-closed.**
- `search_knowledge("laminar flow protection v_c quasiparticle transit ... v_terminal 26.54")` → S72 laminar-flow-workshop (modulus, sub-critical/laminar); `v_terminal=26.54 M_KK`, `dt_transit=0.001130 M_KK⁻¹`. Confirms this gate is the **distinct** optical/roton-branch comparison.
- `search_knowledge("s62 phonon dispersion full optical branch ...")` → `s62_phonon_dispersion_full.npz` exists (gate FULL-62 PASS; T3-BATCH-S62 MIGRATED no-run-no-gate); the dispersion source is on disk.
- `get_constant`: `E_B3_mean=0.9782238787713764` (S38); `Delta_B3=0.176` (S38, doubled-gap); `Delta_B3_s53=0.084152` (S53, un-doubled, Fock mult 3); `c_fabric=209.97368021` (S42); `Mach_max_framework=13.75` (S85; alias Mach_max; BEC analog Mach_max_analog=54.3 is SEPARATE).
- **Closure status**: NO closure covers the fold-transit-vs-optical-branch Landau comparison. S72 closed the *modulus* laminar-protection question (different flow, different velocity). This gate is open and computed.

**Results**:

The substrate dispersion was read directly off `s62_phonon_dispersion_full.npz` (`omega_full` (32 k × 45 bands), `sector_weight` (·,·,3) with sectors [A=acoustic, B, C=optical/Leggett], `k_eff` ∈ [0, 1.41744] M_KK). The **optical/Leggett branch** = the per-k band with maximal C-sector weight (99.9–100.0% C-weight throughout — the K₇-neutral Leggett mode, S58).

*Roton parameters (optical/Leggett branch):*
- **Δ_rot = 0.049006 M_KK** = the band-edge gap at k→0⁺ (= the Leggett-mode gap `ω_L0 = 0.049`, npz scalar). The branch is **strictly monotone-increasing** (all Δω > 0, min Δω = 3.05e-4; ε/p falls 0.384→0.312 with k) — **no interior roton minimum** → the **degenerate-roton (gapped-flat-edge)** reading.
- **p₀ = 0.000000** (the gap-locating / minimum-locating momentum is the band edge, per plan instruction). The roton-form `Δ_rot/p₀ = ∞` is the standard signal that **a k=0 gapped mode does NOT set the Landau velocity** (no zero-momentum excitation is creatable by flow) — the full `min_p[ε(p)/p]` criterion is the binding one. The operationally-meaningful v_c-minimizing momentum is `k* = 1.41744 M_KK` (zone edge of the L_max=10 cache), recorded in the npz.
- **μ_r = [d²ε/dp²|₀]⁻¹ = −2.0066 M_KK⁻¹** (effective mass from edge curvature `d²ε/dk² = −0.498`; **negative** — the gapped branch is concave, characteristic of an optical/roton-like mode that flattens toward the edge).

*Landau critical velocity (the binding number):*
- `v_c = min_p[ε(p)/p]` over the optical/Leggett branch = **0.311838 M_KK** at k*=1.41744, ε*=0.442011.
- Same value on the acoustic branch and the GLOBAL all-band minimum (= **0.311838 M_KK**): the zone-edge mode is the global Landau-criterion minimizer across all 45 bands.

*Transit velocity & dissipation verdict:*
- `v_transit = Mach_max_framework · c_fabric = 13.75 · 209.97368021 = `**`2887.1381 M_KK`**.
- `v_transit − v_c = 2887.1381 − 0.311838 = 2886.83` → **sign = +1** (DISSIPATIVE).
- `v_transit / v_c = `**`9258.4×`** — the transit is *hyper*-critical by nearly 4 OOM, not merely supersonic.

**4-tuple**: `(value=DISSIPATIVE sign(v_transit−v_c)=+1; v_c_global=0.311838 M_KK; ratio=9258.4×, scheme=FW, convention=ABSOLUTE, L_max=10)`.

**Substitution chain** (the SIGN claim, plan §W1-2 — computed, not assumed):
- Step 1–4: `v_transit = Mach · c_fabric = 13.75 · 209.97368021 = 2887.1381 M_KK`.
- Step 5: `v_c := min_p[ε(p)/p]` (Landau 1941) — computed over the optical branch = **0.311838 M_KK** (NOT the roton-form Δ_rot/p₀, which is ∞ here because the minimum is at k=0).
- Step 6 (OOM bound, plan): Δ_rot = O(0.049–0.98) M_KK, p ~ O(1); hence v_c = O(0.3) M_KK ≪ c_fabric ≪ v_transit. **Verified exactly**: v_c = 0.3118 M_KK sits at the low end of the O(0.08–1) band the chain predicted.
- Step 7: `v_transit (2887) ≫ v_c (0.31)` ⇒ `sign(v_transit − v_c) > 0` ⇒ **DEEPLY super-critical**. sign_verdict PASS (computed sign +1 matches the prediction).

**Constraint-map consequence (C1 adjudicated on the dissipation axis):** the Mach-13.75 fold transit is **DISSIPATIVE** — it emits optical/Leggett quasiparticles (rotons) as it crosses the van Hove fold. Because the emitted Leggett-channel quasiparticles ARE the GGE dark matter (Leggett-channel GGE, Ω_DM h²=0.120), this is a **second DM-production channel** complementary to Parker pair-creation (S38, 59.8 pairs). The Landau criterion **sidesteps the φ=0 problem** that blocked the analog-horizon reading: it is a mode-emission threshold (`min ε/p`), not a background-flow-gradient (∇φ) calculation — so the dissipation verdict stands independent of whether a coherent acoustic horizon also forms (that is INV10-W4-2's question). The **degenerate-roton** (gapped-monotone, Umklapp-forbidden) branch is flagged: because SU(3) has no Brillouin-zone boundary (qa B-QA-2), the gapped Leggett mode has no Umklapp decay channel ⇒ the emitted rotons are **eternal** — a DM-stability mechanism. This is the dual structure to S72: the *modulus* roll is laminar (sub-critical, v_terminal=26.54 < v_c-of-its-condensate); the *fold transit* is hyper-critical (2887 ≫ v_c=0.31). Same Landau form, opposite verdict, because they are different flows against different branches.

**Substrate-first assessment.** Direction held throughout: D_K eigenvalues → s62 phonon dispersion ε(p) (the optical C-sector branch = the substrate roton, S58) → roton parameters (Δ_rot, p₀, μ_r) → Landau v_c = min_p[ε(p)/p] → the dissipation threshold of the supersonic transit. He-II's roton minimum and its ~60 m/s critical velocity are a **laboratory projection** of this resonance structure — the substrate is fundamental; He-II realizes a simplified version of the same Landau-criterion physics. Whether the transit emits rotons is the substrate deciding, by its own mode-emission threshold, how cosmogenesis couples to its internal normal modes; it emits, hyper-critically, and those emitted rotons are the dark matter.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- script `computations/investigation-10/inv10_w1_roton_landau_vc.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` → both present (see closeout grep below).
- data `computations/investigation-10/inv10_w1_roton_landau_vc.npz` — present (k_eff, opt_omega, Δ_rot, p0, mu_r, v_c_optical/_acoustic/_global, v_transit, signs).
- plot `computations/investigation-10/inv10_w1_roton_landau_vc.png` — present (dispersion ε(p) + Landau ε/p integrand with v_c, c_fabric, v_transit lines).
- verdict line in `computations/investigation-10/inv10_gate_verdicts.txt` — present, matches `^INV10-W1-2-ROTON-LANDAU-VC:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + schema-v2 3-tuple (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) emitted via `emit_verdict` (track=investigation; 6 rows; sig_5 unique).
  - `audit_sha256=d710eba31abb74302c2439baee166dcb6f2951edf7a7e3097a558dada94ef13c`
  - `content_sha256=c110158064fb2e8bb29b131f6e1f9dbdbfbdf54ebccb0052ebfda0aa669627c2`
- this WP section's must_contain: `Status.*COMPLETED`, `Verdict.*(PASS|FAIL|INFO)`, `Output Artifacts`, `MCP Pre-Compute Audit` — all present.

---

### §W1-3. INV10-W1-3-SECOND-SOUND-CMB (tesla-resonance; writer mack-cosmic-bridge for inventory/canonical)

**Status**: COMPLETED
**Gate ID**: `INV10-W1-3-SECOND-SOUND-CMB`
**gate_type**: `compute`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `tesla-resonance` (computes the value); `mack-cosmic-bridge` is sole writer of any falsifier-inventory row / canonical_constants pin at session-promotion
**Hypothesis**: the second-sound CMB horizon ℓ=π·(c_fabric/c_Gold) recomputed with current four-speed values lands near ℓ≈721 between the 2nd and 3rd Planck acoustic peaks, and is either a live falsifiable CMB feature (revive → mack inventory row) or a retracted artifact (→ atlas-09); second sound itself is PROVEN (Q=75,989).
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w1.md` §W1-3.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- script `computations/investigation-10/inv10_w1_second_sound_cmb.py` — present; `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (`from canonical_constants import *`; `def print_verdict_payload(`).
- data `computations/investigation-10/inv10_w1_second_sound_cmb.npz` — present (24 arrays: l_second_sound, speed_ratio, planck_peaks/troughs, decision, verdict, …).
- plot `computations/investigation-10/inv10_w1_second_sound_cmb.png` — present (TT-envelope placement context with ℓ=720.93 marker + ±peak-halfwidth band).
- verdict line in `computations/investigation-10/inv10_gate_verdicts.txt` — present; matches `^INV10-W1-3-SECOND-SOUND-CMB:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row (no 3-tuple — [VERIFY], not [SIGN]).
- this WP section — `Status.*COMPLETED`, `Verdict.*(PASS|FAIL|INFO)` (INFO), `Output Artifacts`, `MCP Pre-Compute Audit` all present.

**MCP Pre-Compute Audit**:
- `get_constant("c_fabric")` → **209.97368021** (S42, `s42_gradient_stiffness`; substrate sound speed). Used as-is.
- `get_constant("c_Gold")` → **0.915** (S52, gate `GL-JOSEPHSON-52`, `s52_gl_josephson.npz`; Goldstone sound speed M_KK). Used as-is.
- `get_constant("l_second_sound")` → **NOT FOUND** (confirms the plan: OUTPUT-FILE-ONLY at S53, no canonical_constants pin → nothing to drift against; recompute is honest, not a re-derivation of a pinned value).
- `search_knowledge("second sound CMB horizon multipole l_second_sound c_fabric c_Gold")` → S53 `s53_second_sound_cmb_output.txt`: `l_second_sound = π·(c_fabric/c_Gold) = π·229.48 = 720.9` (CMB-53). Two-sound hierarchy: `l_geom = π·1 = 3.1`, `l_pair = π·c_fabric/c_Gold = 720.9`.
- `search_knowledge("Q 75989 second sound undamped two-fluid mode")` → theorem **"Second sound Q = 75,989"** (S44 W6-2 / S68 obs horizon; "Undamped two-fluid mode"; classification 05; **PROVEN**). Distinct from the Leggett mode Q=670,000 (omega_L1) — two different modes; the second-sound Q is the relevant one here.
- `trace_entity("second sound Q-factor undamped two-fluid")` → no trace (the canonical handle is the theorem string above, found via search_knowledge).
- Not PRE-CLOSED: no existing closure renders the revive/retire decision; the gate is a live characterization.

**Verdict**: **INFO** — RETIRE. ℓ_second_sound reproduces cleanly (720.93, 0.0043% from S53 720.9) but is **unresolvable** from the standard ΛCDM third-peak shoulder, so the dormant prediction is closed honestly (→ atlas-09) rather than revived. INFO (not FAIL) because the reproduction passes — the closure is a resolvability verdict, not a reproduction failure.

**Results**:

NUMBERS FIRST.

| Quantity | Value | Source |
|:---------|:------|:-------|
| `c_fabric` | 209.97368021 M_KK | S42, canonical (MCP-confirmed) |
| `c_Gold` | 0.915 M_KK | GL-JOSEPHSON-52, canonical (MCP-confirmed) |
| speed ratio `c_fabric/c_Gold` | 229.4794 | computed |
| **ℓ_second_sound = π·(c_fabric/c_Gold)** | **720.9309** | computed |
| S53 reference value | 720.9 | `s53_second_sound_cmb_output.txt` (OUTPUT-FILE-ONLY) |
| reproduction Δ | 0.0043 % | `|720.9309 − 720.9|/720.9` (tol 0.5% → **PASS**) |
| nearest Planck peak | ℓ₃ ≈ 810.8 | PLANCK 2018 TT |
| distance to ℓ₃ | 89.9 multipoles = **0.310 peak-widths** | `Δℓ_peak = 290` unit |
| nearest Planck trough | ℓ ≈ 675.0 (2nd trough) | PLANCK 2018 TT |
| distance to 2nd trough | 45.9 multipoles | — |
| interval placement | ℓ₂ (537.5) < **720.93** < ℓ₃ (810.8) | True (in ℓ₂→ℓ₃ rise) |
| resolvable from nearest peak? | **No** (d=89.9 < halfwidth 145) | RETIRE driver |

**4-tuple**: `(value=720.9309, scheme=FW, convention=RATIO, L_max=N/A)`.

**Substitution chain** (substituted numbers; per `math-scripts.md` §Double-Check Logic):
- Step 1: ℓ_second_sound := π·(c_fabric/c_Gold)  [S53 CMB-53 horizon formula — multipole of a horizon scale is π × the speed ratio]
- Step 2: c_fabric = 209.97368021 M_KK  [S42, canonical]
- Step 3: c_Gold = 0.915 M_KK  [GL-JOSEPHSON-52, canonical]
- Step 4: speed_ratio = 209.97368021 / 0.915 = 229.4794
- Step 5: ℓ_second_sound = π · 229.4794 = **720.9309**
- Step 6: reproduction vs S53 720.9 → |Δ|/720.9 = 0.0043% ≤ 0.5% → **PASS** (current four-speed values have NOT moved the horizon)
- Step 7: Planck placement → ℓ₂ (537.5) < 720.93 < ℓ₃ (810.8): the multipole IS in the ℓ₂→ℓ₃ interval; BUT the nearest peak (ℓ₃) is only 89.9 multipoles = 0.310 peak-widths away — inside one peak-halfwidth (145) → **NOT resolvable** as a substrate-distinct feature.
- Conclusion: ℓ_second_sound = 720.93 coincides with the standard third-peak shoulder of the ΛCDM first-sound (baryon-photon) ringing. **DECISION: RETIRE.**

**Constraint-map consequence**: The revive/retire axis is adjudicated → **RETIRE**. The second-sound CMB horizon does NOT yield a ΛCDM-distinct observable at the current speed ratio: 720.93 falls on the ℓ₂→ℓ₃ rise toward the third acoustic peak (ℓ₃≈810.8), ~0.31 peak-widths short of it — degenerate-on-the-sky with the standard first-sound third-peak shoulder. This is the **resonance-vs-detector** split the framework repeatedly hits (cf. [internal-consistency ≠ detector-reach]): the second-sound mode is real and PROVEN undamped (Q=75,989, S44/S68) on the *internal-consistency* axis, but it has no resolvable *detector-reach* signature in CMB TT. The dormant prediction is therefore closed honestly rather than left in limbo — it currently carries NO status in any live register, and RETIRE (log to atlas-09) supplies one. It does NOT become the CMB-side companion to the banked first-sound BAO ring (Row #72): that twin would have required a substrate-distinct multipole, and the second sound's horizon is not one in TT. Bears on **C2** (two-fluid evidence): a *resolvable* ℓ≈721 feature would have been direct evidence for the two-fluid structure S72 retracted; its non-resolvability means CMB TT cannot confirm-or-deny the two-fluid picture via this channel — that adjudication must come from elsewhere (e.g. a trough-coincident horizon, or a second-sound transfer-function amplitude, INV10-W2-2 Sakharov machinery).

**Caveat (resolution boundary)**: the RETIRE verdict is keyed to the peak-width unit `Δℓ_peak ≈ 290` (mean Planck inter-peak spacing) and the halfwidth resolvability cutoff (145). If a substrate-physics amplitude computation (the second-sound transfer function) predicted a feature SHARP compared to the broad ΛCDM acoustic envelope, the same multipole 720.93 could in principle be resolvable as a narrow excess on the broad third-peak shoulder. This gate computes the *placement* (the multipole and its peak/trough distances), not the *amplitude/width* — the amplitude leg is INV10-W2-2's job. The honest current status is RETIRE on placement; a forward amplitude gate could re-open it. (`sigma_peak`, `d_nearest_trough`, `resolvable_from_peak`, and the peak/trough ladders are all banked in the npz for that forward gate.)

**Promotion note**: per the writer split, the falsifier-master-inventory row (atlas-09 retirement-log entry) and any canonical_constants pin are **`mack-cosmic-bridge` sole-writer on the session track** — NOT an investigation-track edit. This gate produces the value (720.9309) + the RETIRE verdict only; the register write happens at session-promotion.

**Substrate-first assessment**: PHONONIC. The substrate IS a two-component resonator — a Goldstone sector (c_Gold = 0.915) and the fabric phonon sector (c_fabric = 209.97). Second sound IS its out-of-phase entropy/temperature wave (the Landau-Khalatnikov mode), PROVEN undamped (Q=75,989). The direction flows D_K eigenvalues → the four-speed hierarchy → the second-sound horizon scale → the CMB multipole ℓ = π·(c_fabric/c_Gold) = 720.93. Crucially, the multipole depends only on the dimensionless SPEED RATIO (229.48×), so it is independent of the M_KK scale — a clean substrate-IS prediction. The finding is that this intrinsic acoustic horizon OF the substrate's two-component dynamics happens to project onto the same patch of sky where the emergent first-sound (baryon-photon) ringing already deposits power (the third-peak shoulder). Landau-Khalatnikov second sound in He-II is the LABORATORY PROJECTION of this resonance structure; the substrate's second sound is fundamental. The register now carries an honest RETIRE status where it previously carried none.

---

### §W1-4. INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE (tesla-resonance; baptista + berry consult)

**Status**: COMPLETED
**Gate ID**: `INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE`
**gate_type**: `compute`
**Trigger**: `[CHAIN]`
**Classification**: **GEOMETRIC**
**Agent**: `tesla-resonance` (baptista Jensen-τ band structure + berry Zak/Wilson-loop machinery co-opted as method consultants / cross-reviewers)
**Hypothesis**: treating Jensen-τ as a synthetic momentum, the van Hove fold at τ_fold=0.190 is a band-touching whose synthetic-(τ)-axis Zak-phase WINDING is quantized + ε-stable, making τ_fold a topologically-protected node (a topological invariant, U1) — structurally distinct from the local Berry curvature Ω=0 (W5, EXACT) and from the ordinary-BZ k-space Zak phase RETRACTED at S48.
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w1.md` §W1-4. NON-NUMERICAL set-membership PASS criterion (S95 clause).

**Verdict**: **FAIL** — τ_fold is **NOT topologically protected**. The synthetic-(τ) Wilson-loop winding around the τ_fold band-touching is **quantized** at any single ε (forward-holonomy γ/π = +1.000000, quant deviation 5.55e-16 ≪ 0.05·π window) BUT **DISSOLVES under the ε-protection sweep** (max drift 1.2130·π, max within-ε spread 0.8239·π over ε∈{1e-2, 1e-3, 1e-4} ≫ 0.05·π stability window). PROTECTED = quantized AND ε_stable = (True AND False) = **False**. This is the same dissolution signature that retracted S46 — the winding is an index-permutation artifact of the band-touching, not a protected invariant. ([CHAIN] gate — no 3-tuple; the set-membership PROTECTED=False composite is FAIL per the plan's S95 non-numerical rubric.)

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — all verified on disk):
- script `computations/investigation-10/inv10_w1_synthetic_tau_zak_phase.py` — present; `grep -nE "from canonical_constants import|print_verdict_payload"` → `from canonical_constants import *` + `def print_verdict_payload(` + its call ✓
- data `computations/investigation-10/inv10_w1_synthetic_tau_zak_phase.npz` — present (44 arrays: `gamma_open_pi`, `gamma_closed_pi`, `gamma_ab_open_pi`, `eps_gamma_open/closed/fd` (each 3×8 sweeps), `max_drift_pi`, `max_spread_pi`, `max_im_qgt`, `fd_spread_pi`, `band_group=[7,8]`, `touching_sector=(0,0)`, `i_fold=80`, `PROTECTED`, dual-SHA, …) ✓
- plot `computations/investigation-10/inv10_w1_synthetic_tau_zak_phase.png` — present (τ-band structure across the fold + the ε-sweep dissolution of γ_open vs the ε-stable γ_closed and the S48-FD contrast) ✓
- verdict line in `computations/investigation-10/inv10_gate_verdicts.txt` — present, matches `^INV10-W1-4-SYNTHETIC-TAU-ZAK-PHASE:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + 2 distinctness/ε-protection extra rows (no 3-tuple — [CHAIN], not [SIGN]); emitted via `emit_verdict(session=10, track="investigation")` (4 rows; sig_5 unique).
  - `audit_sha256=569daa2edfd1ee7b0d5e57222687e19ebeb97d69aa001c840c780a5c97c5b0a5`
  - `content_sha256=3710ad7df263911dba4f6cadc4021eeafdb0630de80a1b6d9c8b8ee1cf6eea47`
- this WP section's must_contain: `Status.*COMPLETED`, `Verdict.*(PASS|FAIL|INFO)` (FAIL), `Output Artifacts`, `MCP Pre-Compute Audit` — all present.

**MCP Pre-Compute Audit** (queries run before writing the script; salient return each):
- `trace_entity("synthetic tau Zak phase")` → **"No trace found"** — confirms the synthetic-(τ)-axis winding was **NEVER computed** (the S46→S48 Zak phase was the ordinary-BZ *k*-space axis); this gate's axis is genuinely new, NOT a re-run of the retracted result.
- `trace_entity("Berry curvature Omega zero W5")` → W5: Ω = 0 EXACT (S25, residual 1.12e-16); the Kosmann-generator anti-Hermiticity forces the LOCAL Berry CURVATURE (2-form) to vanish identically. This constrains the smooth region; it does NOT determine the GLOBAL holonomy around a band-touching puncture (the monopole-with-zero-field-strength-yet-nonzero-holonomy structure).
- `search_knowledge("Zak phase DISSOLUTION-48 index permutation artifact retracted")` → **DISSOLUTION-48** (S48): "0/10 π-phases survive at ε=0.0001; ARTIFACT from index permutation at degeneracies"; the S46 ordinary-BZ Zak phase (13 π-phases, Z₂=−1) RETRACTED. The pathology was phase-TRACKING through degeneracies by finite-differencing eigenstate phases.
- `get_constant("tau_fold")` → **0.19** (S12/S42). Used as the fold anchor; the τ-loop brackets it: τ∈[0.15, 0.25], N_tau=200, fold at grid index 80 (τ=0.19020).
- **PRE-CLOSED? No.** The synthetic-(τ) axis is unmeasured (trace = No-trace); W5 (Ω=0, local) and S48 (k-space FD, retracted) are the structural priors this gate is built to be DISTINCT from, not closures that cover it.

**Results**:

NUMBERS FIRST. (All read directly from `inv10_w1_synthetic_tau_zak_phase.npz`.)

| Quantity | Value | Meaning |
|:---------|:------|:--------|
| touching sector | (0, 0) | minimal zero-straddle gap over the probe (1.637 vs 1.666/1.666/1.740 for (1,0)/(0,1)/(1,1)) → the fold-touching lives in the SU(3) singlet block |
| block dim | 16 | dim-16 Peter-Weyl block (block-diagonal; no dense ≥640k storage; GPU eigh on the block) |
| band-touching pair | [7, 8] | the degenerate band pair at the fold (gap at fold = 1.6395) |
| fold index / τ | 80 / 0.19020 | the grid point at τ_fold on the N_tau=200 loop |
| **γ_open / π** (primary winding) | **+0.9999999999999994** | the forward-holonomy across the fold (non-Abelian [7,8] det(W_open) = −1) |
| nearest integer·π | 1 | quantized target |
| quant deviation | 5.55e-16 (≪ 0.05·π window) | **quantized = True** |
| nonzero (~π)? | True | a genuine winding at fixed ε |
| γ_closed / π | −6.49e-30 (≈0) | the CLOSED τ-loop holonomy is trivial (non-Abelian det = +1) |
| γ_ab_open / π (Abelian single band 7) | −1.47e-15 (≈0) | the winding lives in the non-Abelian [7,8] PAIR, not a single-band Abelian phase |
| **eps-sweep max drift** | **1.2130·π** (≫ 0.05·π) | γ_open mean shifts +0.0021 → +0.2467 → +0.1253·π across ε={1e-2,1e-3,1e-4} |
| **eps-sweep max within-ε spread** | **0.8239·π** (≫ 0.05·π) | γ_open std blows up to 0.59–0.82·π (random-realization scatter) → **ε_stable = False** |
| S48-FD-pathology contrast spread | 0.0260·π | the finite-difference estimator's ε-spread (the S48 estimator) is ~32× SMALLER — see Step 4 |
| W5 distinctness witness max\|Im(QGT)\| | 2.4409 (≠ 0) | the local Berry curvature 2-form is non-zero ON the loop → the GLOBAL winding is a genuinely different object from W5's Ω=0 |
| max\|Im(eigvec)\| after global-phase fix | 0.4690 | the eigenvectors are genuinely complex (not gaugeable to real) — the holonomy is non-trivial at fixed ε |
| **PROTECTED** | **False** = quantized(True) AND ε_stable(False) | the set-membership verdict |

**4-tuple**: `(value=DISSOLVES_under_eps-sweep_drift=1.213pi_spread=0.824pi, scheme=SA, convention=MIXED, L_max=10)`.

**Substitution chain** (plan §W1-4, the [CHAIN] distinctness argument — computed, not assumed):

- **Step 1 (vs W5, Ω=0).** W5 proves Ω = i⟨∂_a u|∂_b u⟩ − (a↔b) = 0 identically (the LOCAL Berry CURVATURE, a 2-form / field strength), because the Kosmann generator is anti-Hermitian [S25, 1.12e-16]. The gate's own witness `max|Im(QGT)| = 2.4409 ≠ 0` confirms the quantum-geometric tensor (whose imaginary part IS the Berry-curvature density) is non-zero ON the τ-loop — so the GLOBAL winding γ_Zak = i∮⟨u|∂_τ u⟩dτ is a structurally DIFFERENT observable, not the already-zero local Ω.
- **Step 2 (holonomy ≠ curvature).** By Stokes, ∮A = ∫∫Ω over a surface BOUNDED by the loop — but a τ-loop enclosing a band TOUCHING does not bound a smooth surface (the touching is a puncture / Weyl node where the bundle is singular). So Ω=0 away from the node does NOT force γ_Zak=0 around it — exactly as a Dirac monopole carries zero field strength on the sphere-minus-poles yet nonzero holonomy around a pole. A nonzero winding was therefore a priori ADMISSIBLE.
- **Step 3 (gauge-invariant Wilson product, vs S46/S48).** The gate computes γ_Zak = −Im log ∏_j⟨u(τ_j)|u(τ_{j+1})⟩ (the discrete Wilson-loop PRODUCT, INVARIANT under any per-point gauge/index choice — the product telescopes the gauge out), NOT the S46/S48 finite-difference of phases (which permutes index labels at crossings → spurious π jumps). At fixed ε the Wilson product DOES return a clean quantized winding (γ_open/π = +1.000, det(W_open) = −1) — confirming the method is gauge-clean.
- **Step 4 (the ε-protection guard — the DECISIVE test S46 lacked).** Re-run the Wilson loop across ε∈{1e-2,1e-3,1e-4} (the SAME degeneracy-regularization sweep that DISSOLVED the S46 phase, N_real=8 random realizations per ε). A topologically PROTECTED winding is ε-STABLE (drift < 0.05·π); an artifact dissolves. **Result: γ_open drifts 1.2130·π and scatters with within-ε spread 0.8239·π — it DISSOLVES.** The closed-loop γ_closed stays trivially ≈0 (det=+1, ε-stable to 1e-30), and the S48-FD-pathology contrast spread is only 0.0260·π — so the dissolution is NOT the FD estimator's known pathology; it is the OPEN forward-holonomy across the singular touching that is unstable.
- **Conclusion.** γ_Zak is quantized at fixed ε but NOT ε-stable ⇒ PROTECTED = False. The winding is an index-permutation artifact of the band-touching (the eigenvectors of the degenerate [7,8] pair reshuffle under the regularization), not a protected topological charge. **τ_fold is NOT a synthetic-dimension Weyl/Dirac node; it remains an EMPIRICAL input** (U1 NOT resolved on the topology axis). The gate was built to FAIL exactly where S46 failed, so this FAIL is the honest extension of the S48 retraction to the synthetic-(τ) axis — NOT a re-run of a retracted result.

**Constraint-map consequence (U1 on the topology axis — CLOSED).** The synthetic-dimension topology route to SELECTING τ_fold is **CLOSED**: τ_fold=0.190 is not topologically protected. U1 (the framework's "one-dial question", atlas-04 T5 BROKEN — is τ_fold derived or empirical?) is NOT resolved on the topology axis; τ_fold remains the honest fork of atlas-04 A4 (**dynamical relaxation vs SM-Yukawa-style empirical input**). This is a decisive NEGATIVE that removes a candidate τ_fold-selection mechanism — and it is informative precisely because the gate established the winding is a genuinely distinct object (Step 1, max|Im(QGT)|=2.44≠0) that COULD have been protected (Step 2, the monopole-holonomy argument), then tested it with the ε-guard S46 lacked and watched it dissolve. It confirms the S46→S48 retraction is not a k-space accident but extends to the τ-moduli axis: band-touching windings on the Jensen-τ manifold are index-permutation artifacts, full stop. The surviving τ_fold-selection corridors are now (i) MECHANISM-CHAIN dynamical relaxation (atlas-04 A4) and (ii) τ_fold-as-empirical-input — the t* one-loop + variational corridors having already closed at S95 (T-STAR-ONELOOP-ORIGIN FAIL). For the resonance-first thesis: τ_fold IS the resonance condition of the theory (where the van Hove singularity sits and the cavity goes critically damped), but its VALUE is set by transit dynamics / empirical pinning, not by a topological invariant of the synthetic band structure.

**Substrate-first assessment.** GEOMETRIC — this gate is about the fabric itself (the D_K(τ) eigensystem and its band topology), not its excitations. Direction held throughout: D_K(τ) eigenvalues + eigenvectors → the (k,τ) extended-zone band structure → the band-touching at the van Hove fold (sector (0,0), pair [7,8]) → the synthetic-(τ) Zak-phase winding around that touching → the topological status of τ_fold. The substrate IS the spectral triple at each τ, and the MODULI-SPACE of Jensen-τ deformations IS itself substrate-IS — a **Level-2 moduli-deformation** substrate-IS object (phononic-framing.md §"Single-τ-slice vs moduli-deformation"): τ IS the substrate's intrinsic deformation parameter, NOT a coordinate on a meta-container, and the winding across the τ-moduli manifold is a Level-2 (not single-τ-slice) observable. Treating τ as a synthetic momentum was the resonance-first move — a band crossing IN τ could have carried a topological charge à la a Weyl point in synthetic space. The substrate's honest answer is that this particular crossing does NOT: the holonomy dissolves under regularization, so τ_fold is tuned by transit dynamics, not selected by a node location. Acoustic/mechanical metamaterials (Süsstrunk-Huber synthetic dimensions, acoustic Weyl points) are LABORATORY PROJECTIONS of synthetic-dimension band topology; the substrate's (k,τ) zone is fundamental, and here it carries no protected node at the fold.

---

### §W1-5. INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE (tesla-resonance; solo, executed inline)

**Status**: COMPLETED
**Gate ID**: `INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE`
**gate_type**: `solo` (executed inline by the orchestrator; same deliverable as compute — verdict line + WP section)
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC**
**Agent**: `tesla-resonance` (solo, executed inline by the orchestrator)
**Hypothesis**: the three corpus analog temperatures — T_acoustic=0.112 (GGE-relic), the BLV surface-gravity T_a=ħκ_a/2π, and the Hawking-analog T_H=ħκ/2π (κ=½∂_n(c²−v²)) — should coincide if the acoustic-white-hole picture is internally consistent (the quench relic temperature IS the analog Hawking temperature); their agreement (or the origin of any disagreement) is a direct internal-consistency test bearing on C1 / W4-2.
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w1.md` §W1-5. NON-NUMERICAL reconciliation PASS criterion (S95 clause).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — all verified on disk):
- script `computations/investigation-10/inv10_w1_analog_temperature_reconcile.py` (15999 B) — `grep -E "from canonical_constants import|print_verdict_payload"` → `from canonical_constants import *  # noqa…` + `def print_verdict_payload(…)` + its call ✓
- data `computations/investigation-10/inv10_w1_analog_temperature_reconcile.npz` (5759 B) ✓
- plot `computations/investigation-10/inv10_w1_analog_temperature_reconcile.png` (51910 B) ✓ (3-temperature collapse bar chart + κ_SONIC annotation)
- verdict line in `computations/investigation-10/inv10_gate_verdicts.txt`: `grep -E "^INV10-W1-5-ANALOG-TEMPERATURE-RECONCILE:.* audit_sha256=[a-f0-9]{64}"` → matches (PASS; `audit_sha256=92ae5635…29da3b50` `content_sha256=9abb7e87…2f5731fa`) + dual-SHA companion row ✓ (no 3-tuple — [VERIFY], not [SIGN]). Emitted via `emit_verdict(session=10, track="investigation", …)`.

**MCP Pre-Compute Audit** (queries run before writing the script; salient return each):
- `search_knowledge("acoustic horizon temperature T_acoustic Hawking analog surface gravity reconcile")` → `phonic-exflation-equation-hawking-collab.md` **explicitly flags** T_acoustic=0.112 as "the third analog temperature the document does not reconcile" (confirms the gate is NOT pre-closed — genuine open reconciliation).
- `search_knowledge(…internal horizon transit velocity Mach-1…)` → **`kappa_SONIC = 2*pi*T_acoustic`** [canonical, `session-100a-plan-w3.md` greybody/freeze-in derivation] — the decisive cross-link; this IS `T_acoustic = ħκ_SONIC/2π = T_H` read backwards. Also: S63 workshop LEVEL hierarchy (T_GGE Level-0 mode-dependent / T_acoustic=0.112 Level-1 acoustic-horizon / T_Unruh Level-3 emergent-4D); `session-95-plan-w4` "T_a=ħκ/2π is exact (Hawking/Unruh analog; QA-H4.2)".
- `trace_entity("acoustic surface gravity kappa")` → only the BLV form `T_H=ħκ/2π, κ=½∂_n(c²−v²)`; no independent velocity-profile κ value banked (confirms the forward gate is genuinely open).
- `get_constant("T_acoustic")` → 0.112, **NO PROVENANCE entry** (the HY4 session-track write, flagged — not an investigation edit). `get_constant("c_BLV")`→0.485 (S64); `get_constant("c_fabric")`→209.97368021 (S42); `get_constant("Mach_max_framework")`→13.75 (S85); `get_constant("kappa_BCS")`→4.019 (S69, no PROVENANCE); `get_constant("tau_fold")`→0.19 (S12/S42).
- **PRE-CLOSED? No.** The reconciliation was an open documentation gap; the canonical cross-link existed (S100a) but was never stitched to the hawking-collab ledger.

**Verdict**: **PASS — AGREE** (the three analog temperatures collapse to ONE quantity).

**Results**:

| Temperature | Provenance | Value (M_KK) |
|:--|:--|:--|
| T_acoustic | S63 Level-1 internal-acoustic-horizon (canonical_constants) | 0.112000 |
| T_a = ħκ_a/2π | BLV surface gravity, S63 QA-H4.2 | 0.112000 |
| T_H = ħκ/2π | Hawking-analog, hawking-collab | 0.112000 |

- **Two structural collapses.** (i) **T_a ≡ T_H exactly** — both are ħκ/2π with the *identical* closed form κ=½∂_n(c²−v²); ratio = 1 analytically, no computation (they are one surface-gravity temperature named twice in the corpus, not two temperatures). (ii) **T_acoustic ≡ T_H** via the canonical `kappa_SONIC = 2π·T_acoustic` relation (S100a-plan-w3) ⟺ T_acoustic = ħκ_SONIC/2π. ⇒ **κ = κ_a = κ_SONIC = 2π·0.112 = 0.703717 M_KK**.
- **Pairwise ratios**: r(T_ac/T_H) = r(T_ac/T_a) = r(T_a/T_H) = 1.000000; **max pairwise |ratio−1| = 0.000e+00** < tol_agree = 0.10. AGREE.
- **Extremal-horizon branch**: κ_SONIC = 0.703717 ≠ 0 ⇒ the transit/sonic horizon is **NON-EXTREMAL** (T_H = 0.112 ≠ 0). The extremal κ→0, T_H→0 case (session-84-w8b "Dump = extremal horizon") is a *different* horizon (the BCS-freeze dump; kappa_BCS=4.019 is its own surface gravity, also ≠ 0) — not conflated here.
- **HONESTY SCOPE (load-bearing).** This is a *ledger* reconciliation (S95 non-compute clause). The agreement T_acoustic = T_H is consistency **within the canonical ledger** — the framework *defines* T_acoustic as the sonic surface-gravity temperature via `kappa_SONIC = 2π·T_acoustic`. It is **NOT** an independent numerical coincidence: this gate does **not** re-derive κ from a first-principles velocity profile ½∂_n(c²−v²) at the Mach-1 surface. What it establishes is that the corpus's three temperature *symbols* refer to one quantity, closing the non-reconciliation the hawking-collab doc explicitly flagged (a **documentation gap**, not a physics inconsistency).
- **4-tuple**: `(value=PASS-AGREE…kappa_sonic=0.703717…max_pairwise_dev=0.000e+00…ledger-internal_NOT_indep_velocity-profile_kappa, scheme=BLV, convention=ABSOLUTE, L_max=N/A)`. Dual-SHA companion row present.

**Substitution chain** (plan §W1-5, executed): Step 1 T_a:=ħκ_a/2π, κ_a=½∂_n(c²−v²); Step 2 T_H:=ħκ/2π, κ identical ⇒ Step 3 T_a/T_H=κ_a/κ=**1 exactly**; Step 4 3-way reduces to T_acoustic vs T_H; Step 5 canonical `kappa_SONIC=2π·T_acoustic` ⇒ T_acoustic=ħκ_SONIC/2π=T_H; Step 6 κ_SONIC=0.703717≠0 ⇒ non-extremal ⇒ **AGREE**.

**Constraint-map consequence**: the acoustic-white-hole picture is **internally consistent on the temperature axis** — the GGE-relic temperature IS the analog-Hawking temperature of the internal acoustic horizon. Strengthens **C1**'s "genuine (non-extremal) thermal horizon" reading and supplies INV10-W4-2 (tesla↔volovik acoustic-horizon adjudication) with a consistency datum *favoring the genuine-horizon reading over the moduli-turning-point reading*. **Forward gate (genuinely non-circular, the open question)**: independently evaluate κ = ½∂_n(c²−v²) from the transit velocity profile at the Mach-1 surface and check whether it equals 0.703717 M_KK — a real consistency test the canonical relation cannot supply by definition. **HY4 (session-track)**: the T_acoustic=0.112 PROVENANCE write to canonical_constants.py is mack/orchestrator sole-writer at session-promotion, NOT an investigation edit.

**Substrate-first assessment**: PHONONIC. The substrate IS the acoustic white hole — the supersonic transit through the van Hove fold with its internal acoustic horizon. Direction: D_K eigenvalues → four-speed hierarchy + transit velocity profile → surface gravity κ=½∂_n(c²−v²) → analog Hawking temperature T_H=ħκ/2π, which in analog gravity IS the temperature of the relic the horizon produces. The substrate tests its own self-consistency: its internal-horizon temperature (0.112) and the surface-gravity temperature of that same horizon are the same number, with a single non-extremal κ=0.703717 M_KK. A BEC/³He sonic horizon with its Hawking-analog thermal spectrum is the LABORATORY PROJECTION; the substrate's internal acoustic horizon is fundamental.

---

## Wave 1 Synthesis (team-lead)

**Structure source**: per-gate roll-up + cross-wave hand-off pattern of `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`; numerical-vs-structural split per `output-standards.md §"What Changed"`. Note: dispatched pre-reboot; W1-1/W1-4 finished post-reboot (scripts survived on disk, sound; only emit+WP were re-run — no re-compute).

**Per-gate verdict roll-up (5/5 closed):**
- **W1-1 CASCADE-EXPONENT → FAIL** (sign+magnitude FAIL, regime MARGINAL). Two-legged: (a) *cascade-exponent-as-tilt CLOSED* — no clean inertial range (p=−2.458±0.297, R²=0.620 over 0.83 dec; wrong sign for a decreasing cascade; neither Kolmogorov-5/3 nor Vinen-1); (b) *freeze ROBUST* — R_FC=1.904e-4 ≪ 1 ⇒ relic **FROZEN, U3 holds**. Bogoliubov sanity: unitarity resid 5.55e-16; no tachyonic modes.
- **W1-2 ROTON-LANDAU-VC → PASS** — DISSIPATIVE transit: v_transit=2887.14 ≫ v_c=0.3118 M_KK (9258×); gapped-monotone **degenerate-roton** branch (Δ_rot=0.049, no interior minimum ⇒ Umklapp-forbidden eternal mode). C1 adjudicated on the dissipation axis: roton/Leggett emission is a 2nd DM-production channel.
- **W1-3 SECOND-SOUND-CMB → INFO** — ℓ_second_sound=π·(c_fabric/c_Gold)=**720.93** reproduced (0.004% of S53), but RETIRE-on-placement: buried on the ℓ₂→ℓ₃ third-peak shoulder (~0.31 peak-widths short of ℓ₃≈810), not ΛCDM-distinct in TT. Resonance-real / detector-sterile.
- **W1-4 SYNTHETIC-TAU-ZAK → FAIL** — synthetic-(τ) Wilson winding γ/π=+1.000 quantized at one ε but DISSOLVES under the ε-sweep (drift 1.213π, spread 0.824π) ⇒ PROTECTED=False. τ_fold NOT topologically protected, remains **empirical** (U1 unresolved on the topology axis). Distinctness from W5 (local Berry max|Im QGT|=2.44≠0) and S46/S48 (FD-pathology spread 0.026π) both verified — the dissolution is the substrate's honest verdict, not a methodology artifact.
- **W1-5 ANALOG-TEMP-RECONCILE → PASS** — three analog temperatures collapse to ONE: T_a≡T_H exact (identical κ); T_acoustic≡T_H via canonical `kappa_SONIC=2π·T_acoustic` (S100a). κ=0.703717 M_KK, non-extremal. Closes the hawking-collab-flagged non-reconciliation (a documentation gap). Ledger-internal, NOT an independent velocity-profile κ.

**Load-bearing cross-wave hand-off — INV10-W1-1 → INV10-W2-1:** the COMPOSITE W1-1 verdict is FAIL, but the *specific sub-result W2-1 consumes* is the freeze verdict = **FROZEN (U3 holds)** — NOT the R_FC≥1 "processed-relic" branch. So W2-1 proceeds with the frozen-|β_k|²-as-primordial assumption (justification intact) and computes n_s **self-contained** from `d ln P/d ln k`; the cascade-exponent tilt cross-check is **moot/unusable** (no clean inertial range to map). This is the corrected branch vs the plan's generic "W1-1 FAIL ⇒ post-freeze re-shaping" reading — that reading is keyed on R_FC≥1, which did NOT fire.

**Cross-vantage feeds (DATA, not gates):** W1-2 (DISSIPATIVE) + W1-5 (non-extremal genuine thermal horizon, κ=0.7037) → **INV10-W4-2** acoustic-horizon adjudication, both favoring the genuine-horizon reading over moduli-turning-point. W1-3 (RETIRE) → session-track atlas-09 + mack. W1-4 (τ_fold empirical) → U1 closed on the topology axis (resonance-first thesis: τ_fold is not a topological invariant).

### (a) Numerical revisions
- ℓ_second_sound: S53 720.9 → **720.9309** (current four-speed values; 0.004% drift — no movement).
- κ_acoustic-horizon: implicit → **0.703717 M_KK** (= 2π·T_acoustic, pinned by W1-5).

### (b) Structural changes
- TRANSIT-PS tilt input: "cascade exponent supplies n_s−1" → **route CLOSED** (the |β_k|² relic is not a turbulence cascade; n_s comes from the assembled-spectrum tilt, W2-1, not from a cascade exponent).
- τ_fold: candidate topological invariant → **confirmed empirical** (synthetic-topology selection route closed).
- analog-temperature ledger: 3 symbols carried as possibly-distinct → **1 quantity** (T_a=T_H=T_acoustic).
- C1 transit: open → **dissipative + genuine non-extremal thermal horizon** (W1-2 ∧ W1-5).

## Carry-Forward Computations

### CF-INV10-W1-5-KAPPA-VELOCITY-PROFILE — independent surface-gravity check
1. **What**: evaluate κ = ½ ∂_n(c²−v²) at the internal Mach-1 (v=c) surface from the transit velocity profile v(n), and test whether it independently equals the ledger value 0.703717 M_KK (= 2π·T_acoustic). The non-circular complement to W1-5's ledger-internal reconciliation.
2. **Inputs**: the transit velocity profile v(n) near the fold (transit V.3 / s48-tesla-collab Mach-1 grid, 1260 horizon points); c_BLV=0.485, c_fabric=209.97368021; T_acoustic=0.112 (target).
3. **Gate**: PASS iff |κ_profile − 0.703717| / 0.703717 < 0.10 (the W1-5 tol_agree band); FAIL ⇒ the canonical `kappa_SONIC=2π·T_acoustic` is a definitional stipulation not borne out by the substrate profile (re-opens C1 horizon-type).
4. **Effort**: 0.5 wave (the profile exists; the work is one finite-difference + a ratio).

### CF-INV10-W1-3-SECOND-SOUND-AMPLITUDE — transfer-function re-open test
1. **What**: compute the second-sound CMB transfer-function amplitude/width at ℓ=720.93 (a SHARP-vs-broad test); decide whether a narrow excess on the broad third-peak shoulder is resolvable — the leg W1-3 deferred (W1-3 computed *placement* only).
2. **Inputs**: ℓ_second_sound=720.93 (W1-3 npz `sigma_peak`, peak/trough ladders banked); the second-sound Q=75,989 undamped mode; the INV10-W2-2 Sakharov transfer machinery (second-sound analog, distinct from the first-sound channel W2-2 computes).
3. **Gate**: PASS (REVIVE) iff the predicted feature width < ½ the ΛCDM acoustic-envelope width at ℓ≈721 AND amplitude > Planck TT cosmic-variance floor; else RETIRE stands.
4. **Effort**: 0.5–1 wave (consumes the W2-2 machinery on the second-sound speed pair).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-16 | TRANSIT-PS-67 tilt input (cascade route) | MISSING-since-S67 | route CLOSED | W1-1 FAIL — |β_k|² relic has no clean inertial range; tilt comes from the assembled spectrum (W2-1), not a cascade exponent |
| 2026-06-16 | U3 (frozen-GGE-as-final) | assumed | CORROBORATED | W1-1 timing: R_FC=1.9e-4 ≪ 1 (relic frozen) |
| 2026-06-16 | C1 transit dissipation axis | open | DISSIPATIVE | W1-2 PASS — v_transit ≫ v_c (9258×), roton/Leggett emission |
| 2026-06-16 | second-sound CMB ℓ≈721 | register-absent (OUTPUT-FILE-ONLY S53) | INFO / RETIRE-on-placement | W1-3 — reproduced but detector-sterile in TT (→ atlas-09, session-track) |
| 2026-06-16 | U1 τ_fold-selection (topology axis) | candidate-topological | empirical (route closed) | W1-4 FAIL — synthetic-(τ) winding dissolves under ε-sweep |
| 2026-06-16 | analog-temperature ledger | unreconciled (hawking-collab flag) | reconciled — 1 quantity, κ=0.7037, non-extremal | W1-5 PASS |

**Process observations (NOT carry-forwards):** the two FAIL gates (W1-1, W1-4) are corridor-closing — both close a route cleanly rather than leaving a marginal case. Reboot recovery: W1-1/W1-4 scripts survived on disk and reproduced their SHAs bit-for-bit on re-run; only emit+WP were re-executed.

**Routed-OUT to session track (NOT investigation edits — land at `/rclab-investigate --investigation 10` close):** W1-3 RETIRE → atlas-09 retirement-log + mack falsifier-inventory status (the register currently carries NO status for ℓ≈721); W1-5 → **HY4** T_acoustic=0.112 PROVENANCE entry in canonical_constants.py (mack/orchestrator sole-writer at session-promotion). Both are session-track per the plan's writer split; the investigation track does not write session registries.

## Files Produced

| Gate | Script | Data | Plot | Verdict |
|:-----|:-------|:-----|:-----|:--------|
| W1-1 | `inv10_w1_cascade_exponent.py` | `.npz` | `.png` | FAIL (line in `inv10_gate_verdicts.txt`) |
| W1-2 | `inv10_w1_roton_landau_vc.py` | `.npz` | `.png` | PASS |
| W1-3 | `inv10_w1_second_sound_cmb.py` | `.npz` | `.png` | INFO |
| W1-4 | `inv10_w1_synthetic_tau_zak_phase.py` | `.npz` | `.png` (+`_stdout.txt`) | FAIL |
| W1-5 | `inv10_w1_analog_temperature_reconcile.py` (15999 B) | `.npz` (5759 B) | `.png` (51910 B) | PASS |

All under `computations/investigation-10/`; all 5 verdict lines (+ dual-SHA companions, + W1-1 3-tuple) in `computations/investigation-10/inv10_gate_verdicts.txt`.
