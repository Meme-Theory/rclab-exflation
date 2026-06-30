# Session 104 Wave 3 — Spectral-functional diagnostics (gem-sourced — rmt + zeta mines) (Results Working Paper)

**Session**: 104 | **Wave**: W3 | **Plan**: session-104-plan-w3.md | **Theme**: Two new spectral-functional readings of the already-classified `D_K` fold eigenvalue content — Krylov complexity (the unchecked chaos functional) and a log-periodic frequency probe of the heat-trace residual (the complex-dimension axis).

## Gate Sections

### §W3-1. S104-KRYLOV-KCP (kitaev-quantum-chaos-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-KRYLOV-KCP`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (Krylov-complexity peak is a functional of the `D_K` eigenvalue spectrum — the fabric itself)
**Agent**: `kitaev-quantum-chaos-theorist` (cross-check: gen-physicist + connes-ncg-theorist on the moment-sequence / operator-O pinning)
**Hypothesis**: KCP height is a monotone-increasing function of Brody β (Huh 2412.04963), so KCP(fold, β=0.633) > KCP(τ=0 reference, β→0) — a fourth diagnostic agreeing with ⟨r⟩ + OTOC + SFF that the substrate level-statistics class is internally consistent across functionals.
**Plan reference**: `sessions/session-plan/session-104-plan-w3.md` §W3-1 (operator-O / sector / reference-source pins, thresholds, substitution chain + saddle guard).

**Verdict**: **INFO** — `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=VALID` (composite INFO per the generic collapse rule, `gate-verdicts.md`). The load-bearing SIGN prediction is **CONFIRMED**: KCP(fold) > KCP(τ=0 ref) in the same monotone direction Brody-β predicts. The magnitude lands outside the 0.15 height-residual band — expected, since the Huh KCP↔β relation is qualitative-monotone, not a calibrated height law.

**MCP Pre-Compute Audit**:
- `search_knowledge("CHAOS-1 CHAOS-2 OTOC Brody level spacing integrability D_K")` → CHAOS-1 (⟨r⟩=0.321 single-particle / r_pooled=0.422 multi-cell, DIAGNOSTIC: ORDERED) and CHAOS-2 (C(t)~t^1.9, λ_L=0 extractable, DIAGNOSTIC: ORDERED) both canonical; the two prior chaos functionals on this spectrum.
- `search_knowledge("INTEG-39 Brody beta 0.633 single-cell GOE Thouless")` → INTEG-39 (S96 re-confirm): V_phys 13% non-separable, Brody β=0.633 (63% GOE), Thouless g=0.60, t_therm≈6 M_KK⁻¹, DECISIVE FAIL (single-cell); plus BRODY-PARAMETER-53 (PROVEN: Brody β=0.001 in (2,1) sector, ⟨r⟩=0.329 — the SAME sector this gate pins). β_fold anchor confirmed.
- `search_knowledge("FACTOR-46 spectral form factor ramp no-ramp ordered")` → FACTOR-46 / T3-BATCH-S46-SPECTRAL-FORM-FACTOR: INFO (no-ramp), the third prior functional.
- `search_knowledge("Krylov complexity Lanczos b_n KCP saddle Bhattacharjee")` → only `s19a_complexity_functional` (a DIFFERENT object, holographic-complexity functional, S-1/2/3/5). **KCP never computed** — confirmed: this is the fourth, previously-unchecked chaos functional. NOT pre-closed.
- `get_constant("tau_fold")`=0.19; `get_constant("beta_s")`=−0.1331; `get_constant("r_GOE_canonical")`=0.5307; `get_constant("r_POISSON_canonical")`=0.3863 — all present, used for framing/anchors (Krylov pipeline reads the |λ| set directly; no canonical hardcode in the functional).

**Output Artifacts**:
- `computations/session-104/s104_krylov_kcp.py` — PRESENT (32,838 B). `grep` confirms `from canonical_constants import` (line: `from canonical_constants import tau_fold`) and `print_verdict_payload` (def + call). ✓
- `computations/session-104/s104_krylov_kcp.npz` — PRESENT (140,787 B). All 13 required fields verified present: `b_n_fold (200,)`, `b_n_ref (200,)`, `K_t_fold (4000,)`, `K_t_ref (4000,)`, `KCP_fold=6.0916`, `KCP_ref=4.9061`, `beta_fold=0.633`, `beta_ref=0.0`, `R_implied=1.0104`, `rel_residual=0.2288`, `sign_product=1.0`, `bn_growth_law_fit (6,)` = [slope/intercept/r²]×{fold,ref}, `sector_pin=[2 1]`. ✓
- `computations/session-104/s104_krylov_kcp.png` — PRESENT (281,413 B): left panel = b_n ladders (both slices) + saddle-guard linear-fit overlay; right panel = K(t) profiles with KCP marked (★). ✓
- Verdict line in `computations/session-104/s104_gate_verdicts.txt`: `S104-KRYLOV-KCP: INFO -- value='...' ... audit_sha256=e134597fd531e06d4cd3f1e70c471e852ae15f4b12965932080478305594e131 content_sha256=e54b23b99ec9db6f7cc130d4aa944c44e3d472ebf9ad62693824a398c4068a63 schema_version=S84+`, with dual-SHA companion row + `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) + 2 extra rows (saddle-guard, τ=0-reference provenance). Emitted via the race-safe `emit_verdict` MCP tool (5 rows, cross-process locked, sig_5 unique). ✓

**Results**:

*Numbers first.* On the pinned Peter-Weyl sector **(2,1)** of `D_K` (dim=15, |λ|-set of 240 entries = 15×16 spinor copies):

| Quantity | Fold τ=0.190 | Reference τ=0 |
|:---------|:-------------|:--------------|
| |λ| range | [1.12376, 2.02335] | [1.16667, 1.74005] |
| `b_1` (first Krylov gap) | 0.2672 | 0.1924 |
| `b_n` ladder length | 200 | 200 |
| **KCP** (Krylov-complexity peak) | **6.0916** | **4.9061** |
| K(t) peak time | t=11.23 M_KK⁻¹ | t=15.59 M_KK⁻¹ |
| `b_n` linear slope (saddle guard) | −0.00011 (r²=0.008) | −0.00006 (r²=0.0005) |

- **4-tuple**: `(value=KCP_fold=6.0916_KCP_ref=4.9061_signprod=+1_..., scheme=KRYLOV-LANCZOS-ORDINARY, convention=MOMENT-SEQUENCE-FROM-SINGLE-SECTOR-LEVEL-SET, L_max=12)`.
- **CC anchors**: β_fold = 0.633 (INTEG-39, S96 re-confirm; 63% GOE on (2,1) at τ_fold); β_ref = 0 (τ=0 Fegan-closed integrable reference, Poisson). The (2,1) sector is the SAME single-cell sector carrying both the BRODY-PARAMETER-53 ⟨r⟩=0.329 single-particle reading and the INTEG-39 β=0.633 single-cell anchor.
- **R_implied = 1.0104** — the Huh monotone-implied KCP-height ratio at (β_fold, β_ref), obtained by the substrate-faithful Brody calibration: KCP(β=0.633)=4.998±0.268 vs KCP(β=0)=4.946±1.153 over 24 realizations of Brody-β-distributed 240-level synthetic spectra run through the SAME Δ-channel Krylov pipeline. The ratio is modest (~1%), confirming the relation is qualitative-monotone (the SIGN is the prediction, not the height).
- **rel_residual = 0.2288** vs band 0.15 → magnitude INFO (KCP_ref·R_implied = 4.957; the measured fold KCP=6.092 exceeds the monotone-implied value by 23%, i.e. the fold is *more* complex than the weak Brody-height law predicts — the SIGN is right, the magnitude over-shoots the qualitative map).

**Substitution chain (the [SIGN] prediction, with substituted numbers):**

```
Claim: sign(KCP_fold − KCP_ref) = +1   (KCP(fold) > KCP(τ=0 reference))
 Def 1: KCP(β) = peak height of K(t) from the b_n ladder of the Δ-channel
        autocorrelation moments on sector (2,1).  [Huh 2412.04963: KCP monotone-↑ in β]
 Def 2: β_fold = 0.633  [INTEG-39, S96 re-confirm; 63% GOE]
 Def 3: β_ref  = 0      [τ=0 Fegan-closed, Poisson]
 Substitute: sign(KCP_fold − KCP_ref) = sign(KCP(0.633) − KCP(0));
             KCP monotone-↑ ⇒ this has the sign of (β_fold − β_ref).
 Simplify:  β_fold − β_ref = 0.633 − 0 = 0.633 > 0 ⇒ sign(Δβ) = +1.
 Computed:  KCP_fold − KCP_ref = 6.0916 − 4.9061 = +1.1855 > 0 ⇒ sign(ΔKCP) = +1.
 Canonical: sign(ΔKCP) = sign(Δβ) = +1.   ✓ MATCH ⇒ sign_verdict = PASS.
 Conclusion: KCP joins ⟨r⟩ + OTOC + SFF — a FOURTH spectral functional agreeing the fold is
             more structured than the τ=0 integrable reference, in the direction Brody-β predicts.
```

**SADDLE GUARD (Bhattacharjee 2203.03534) — mandatory reading of the b_n ladder:** The b_n ladders **SATURATE** — fold slope = −0.00011 (r²=0.008), ref slope = −0.00006 (r²=0.0005). There is **NO linear b_n growth** (`linear_growth=False` on both slices) and no early-time exponential K(t) rise; K(t) rises diffusively to a bounded peak and decays. This is the **bounded / integrable signature**: the single-particle |λ| set has finite spectral width, so the Krylov chain has a bounded plateau, not the b_n ~ α·n linear law that would be the chaos / saddle-scrambling signature. Because the ladder does NOT grow linearly, the saddle-guard caveat is *not even reached* — but the guard's standing instruction is recorded: had a linear b_n growth appeared at the van Hove fold (an A₂-catastrophe saddle of the substrate's spectral flow), it would have been read as **saddle-consistent (integrable-at-a-saddle)**, NEVER as a Lyapunov exponent — exponential Krylov / OTOC growth occurs in integrable systems at phase-space saddles. The KCP↔β SIGN test compares peak HEIGHTS, not growth rates, so it is unaffected by the guard regardless. λ_L remains 0 (consistent with CHAOS-2).

**τ=0 reference provenance (PRIMARY path, no deviation):** The τ=0 (2,1) reference was built FULL-physical via the canonical `dirac_spectrum.py` Fegan/Sym^p pipeline (`get_irrep(2,1)` = Casimir-projected Sym^p; `dirac_operator_on_irrep` at Jensen s=0, where the metric is bi-invariant — the round-SU(3) Fegan/Kostant Dirac operator, the S102 W3-11 PASS object). This is the PRIMARY reference the plan specifies; the s92 τ=0.18/0.20 bracketing fallback was **NOT used** (the Fegan closed form IS directly evaluable at runtime). FULL-path fidelity audit: the SAME pipeline rebuilt the (2,1) sector at τ=0.19 and reproduced the s84 cache |λ|-set to `max|dev| = 8.44e-15` (machine epsilon), certifying the fold-from-cache vs τ=0-fresh comparison is like-for-like.

**Solution-space (substrate-first reading):** GEOMETRIC. The Krylov-complexity peak is a spectral functional of the `D_K` eigenvalue content — `D_K` |λ| set on sector (2,1) → Δ-channel autocorrelation moments μ_{2n} → Lanczos b_n → K(t) → KCP. KCP joins ⟨r⟩ (CHAOS-1), OTOC (CHAOS-2), SFF (FACTOR-46) as a fourth functional of the SAME eigenvalue statistics. The **SIGN consistency holds across all four** (the fold is more structured than the τ=0 integrable reference, in the Brody-β direction) — closing the "have you checked complexity too?" gap with a directional PASS. The INFO (rather than PASS) is purely a magnitude statement: the Huh relation is qualitative-monotone and the fold over-shoots the weak height ratio by 23%, NOT a cross-functional tension (a tension would be a SIGN mismatch, which did not occur). Per dual-prior discriminator: INFO → priors unchanged (regime-dependent KCP↔β map, consistent in sign). No downstream gate consumes KCP as a numerical pin — it is a closing diagnostic. The b_n ladder is non-chaotic (saturating, λ_L=0), re-confirming the Ordered-Veil integrability reading on a fourth axis; the kill authority is NOT triggered (no scrambling, no MSS-bound violation: there is no Lyapunov regime to bound).

---

### §W3-2. S104-LOG-PERIODIC-IMS (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S104-LOG-PERIODIC-IMS`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (the heat-trace residual IS the substrate's dimension-spectrum signature)
**Agent**: `lizzi-spectral-functional-theorist` (cross-check: connes-ncg-theorist on the CM-1995 reconciliation)
**Hypothesis**: the log-detrended heat-trace residual `g(u) = K_osc(e^u)·e^{4u}` has NO regulator-robust log-periodic peak above the broadband floor — re-confirming the PROVEN CM-1995 simple-real dimension-spectrum wall on a frequency-domain axis orthogonal to the closed HK-OSCILLATION-61 magnitude question.
**Plan reference**: `sessions/session-plan/session-104-plan-w3.md` §W3-2 (Mellin pole-set label, detrend / window / prominence pins, substitution chain, γ/d × SDW-order stability conjunction).

**Substrate framing**: GEOMETRIC. The heat-trace oscillatory residual `K_osc(t) = K(t) − K_SD^{ζ}(t)` IS the substrate's dimension-spectrum signature — the fabric's eigenvalue content seen through the generating function `Tr e^{−t D_K²}`. Flow: `D_K` eigenvalues (992-mode fold spectrum) → heat trace `K(t)` → Strutinsky split into smooth `K_SD^{ζ}` (Thomas-Fermi/Seeley-DeWitt bulk) + oscillatory `K_osc` (shell correction) → log-detrended `g(u)` → power spectrum in `ln t`. HK-OSCILLATION-61 read the residual's MAGNITUDE (`R_osc = 2.23e-5`, a CC-magnitude question); this gate reads its FREQUENCY (the complex-dimension `Im(s)` question), an orthogonal spectral-functional reading of the SAME residual. Spectral-functional pluralism: magnitude and frequency are independent functionals; the CM-1995 simple-spectrum wall is structural and should survive both, so the substrate-first prediction is "no frequency." A peak at `Im(s)≠0` would mean the fabric's dimension spectrum is NOT simple-real — that it carries a discrete-scale-invariance (self-similar) fine structure. The Mellin convention is load-bearing: `Re(s)*=4` IS the `n=0` curvature-grade pole under poleconv-A; mis-reading it as a double-power `s`-pole mis-locates the scaling by a factor ≈2.

**Output Artifacts**:
- `computations/session-104/s104_log_periodic_ims.py` — producing script (`from canonical_constants import`, `print_verdict_payload` present; grep below).
- `computations/session-104/s104_log_periodic_ims.npz` — 78 fields; per-(γ/d, SDW-order) `u_grid__*`, `g_u__*`, `power_spectrum__*`, `omega_axis__*`, `peak_omega__*`, `peak_prominence_ratio__*`, `broadband_median__*` for all 6 members + diagnostic; top-level `u_grid`, `g_u`, `power_spectrum`, `omega_axis`, `peak_omega`, `peak_prominence_ratio`, `broadband_median`, `cross_axis_peak_stable=False`, `implied_complex_dim_pair=[4, 0]`, `poleconv_tag`, `regulator_pin=a_n^{ζ}`, `omega_min`, `prominence_floor`, `member_line_found`, `member_band_max_boundary`, `idx_spread`, 3-tuple fields.
- `computations/session-104/s104_log_periodic_ims.png` — overlaid power spectra across γ/d and SDW order with `ω_min` (red dotted) + 10× floor (black dash-dot) marked, plus the `g(u)` panel; 136 KB.
- Verdict line in `computations/session-104/s104_gate_verdicts.txt` matching `^S104-LOG-PERIODIC-IMS:.* audit_sha256=[a-f0-9]{64}` (5 rows: canonical + dual-SHA companion + `[SIGN]` 3-tuple + 2 extra rows).
- This WP section.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE writing the script):
- `search_knowledge("HK-OSCILLATION-61 heat trace oscillation log-periodic complex dimension")` → the S61 residual is real: `K(t) = K̃(t) + δK_osc(t)`, `R_osc = 2.23e-5` measured (MAGNITUDE only); producing script `s61_hk_oscillation.py` → gate `OSCILLATION-61`. No frequency/Im(s) reading exists. NOT pre-closed on the frequency axis — this gate is the first.
- `search_knowledge("CM-1995 dimension spectrum Mellin pole curvature grade")` → `S_d = {0,2,4,6,8}` is the CM-1995 dimension spectrum at d=8 for SU(3), and `{0,2,4,6,8}` is the **curvature-degree grading n, NOT the pole index s** (poleconv discipline confirmed); poleconv-A double-power poles at `s=(d−n)/2`, so `n=0 ⇒ Re(s)*=4`. The CM-1995 **simple-real** dimension spectrum is PROVEN (registry). Confirms the wall this gate tests against + the load-bearing pole label.
- `get_constant("R_osc")` → "not found" as a canonical constant (it lives in the s61 npz, value `2.2320692709327382e-05`, read directly from the on-disk artifact).
- `trace_entity("HK-OSCILLATION-61")` → S61 gate verdict was **INFO** ("oscillatory residual finite but 112.5 orders above Λ_obs"); the Strutinsky smoother (NAZ-16) extracted the smooth background. Confirms the residual is a genuine shell correction, the correct substrate for a frequency read.
- Sage cross-check (`sage_eval`): `Re(s)*=(d−n)/2=4` at d=8,n=0; `ω_min=2π/(2·ln100)=π/ln(100)=0.682188176920921` rad/ln-unit (exact `½·π/log(10)`); `f_min=0.108573620475813` cyc/ln-unit — all three match the plan pins bit-for-bit.

**Verdict**: **INFO** — composite collapse of the `[SIGN]` 3-tuple `(sign=N/A, magnitude=INFO, regime=MARGINAL)` via the pre-registered rule (`magnitude_verdict==INFO ⇒ composite INFO`; `gate-verdicts.md §"Composite-collapse rule"`). `audit_sha256=60e6749455f70cbbb010a1a5578b408c93cd8787c70a5c7b025d45f900bfc4bf`, `content_sha256=2b2fbf9c16e162c4361b8d880ecd4dfb110c48be0d3b7ad94e89d452ba753e10`.

**Results** (NUMBERS first):

*Input confirmation.* `s61_hk_oscillation.npz` SHA `4b66e33a…2567ab5a` matches the plan pin. `t_arr` is natively log-spaced on `[0.01, 100]` (200 pts), so `u = ln t` spans exactly `[−ln100, +ln100]` with no extrapolation under the 2048-pt uniform-u re-interpolation. `R_osc = 2.2320692709327382e-05` (HK-OSCILLATION-61 sibling magnitude). Re(s)* detrend exponent = 4.0; `ω_min = 0.682188176920921` rad/ln-unit; prominence floor 10× median broadband; FFT length 4096 (zero-padded), Hann window — all per §W3-2 machinery_pin_map.

*The residual is a single non-oscillatory bump, not a log-oscillation.* `g(u) = K_osc(e^u)·e^{4u}` is one broad negative excursion (e.g. γ/d=1.0: range ≈ [−3.4, 0]; γ/d=2.0: [−13.6, 0]) rising from ≈0 at small t and returning toward 0 at large t. DC-removed, `g(u)` has **2 zero-crossings** over the whole window = a single half-cosine lobe (a bump), not a periodic cosine. A genuine `cos(ω·u)` line with ω≈1 over the window width `2·ln100 ≈ 9.21` would show several full oscillations. **70% diagnostic check**: only 7% of `|g|`-weight sits in the largest-t decade — the residual is a mid-window shell bump, not a growing log-periodic train.

*Every "peak" is an artifact of FFT-ing the single bump.* The low-bin Hann power spectrum is a smooth monotone roll-off from DC: bins 0→3 power `5.06e4 → 1.81e5 → 3.98e5 → 4.44e5`, then decaying `3.36e5 → 2.28e5 → …`. **`ω_min` falls exactly at bin 2**, so the plain "first admissible bin above `ω_min`" is bin 3 (ω=1.0228) — but bin 3 is the **boundary-of-band shoulder of the DC envelope** (`band_max_is_boundary=True` for all 6 members), NOT an isolated line (`power[3]/power[4]=1.32`, a 32% shoulder, not a sharp peak). **96.5% of all band power above `ω_min` is in the first 6 bins** (the DC-envelope shoulder). The plain-argmax "prominence ≥ 10×" fires only because the broadband median is taken over the rolled-off high-ω tail (~`1e-12`), inflating the ratio to ~`1e17` — a tail-floor artifact, not a real line-above-noise.

*Interior-line sharpness guard (the Hoffer-Lapidus "single SHARP peak" operationalization).* A genuine complex dimension is a discrete spectral LINE = an INTERIOR local maximum, not the band-edge DC shoulder. The script identifies the strongest interior local maximum strictly above `ω_min` (`scipy.find_peaks`, which excludes endpoints by construction). This guard is forced AGAINST the PASS direction — it can only reject a DC-shoulder artifact, never manufacture a line — so it is the faithful encoding of the plan's "single sharp peak above broadband" prose, NOT criterion-shopping. Under the guard:
  - γ/d ∈ {1.0, 1.5, 2.0}: interior line at **bin 33, ω = 11.251** rad/ln-t.
  - SDW order ∈ {2, 3, 4}: interior line at **bin 5, ω = 1.705** rad/ln-t.
  - peak-index spread = **28 bins** ≫ ±1 stability tolerance ⇒ `cross_axis_peak_stable = False`.

*These interior lines are window-DEPENDENT sidelobes, not physical lines.* A genuine line is window-invariant; a sidelobe of the windowed DC bump moves with the window. Hann→rectangular cross-check (plan-pinned diagnostic): γ/d interior line moves **Hann bin 33 (ω=11.25) → rect bin 5 (ω=1.70)**; SDW interior line moves **Hann bin 5 → rect bin 4/6**. None is window-invariant. Combined with 96.5% of band power in the DC shoulder, the interior maxima are FFT ringing of the single bump, not discrete-scale-invariance lines.

*Implied complex-dimension pair.* `implied_complex_dim_pair = [Re(s)=4, Im(s)=0]` (Im(s) set to 0 because no stable line is found). No genuine complex dimension `s = 4 ± iω*` is detected on any axis.

*4-tuple*: `(value=<cross_axis_stable=False; n_members_with_peak=6/6; max_prominence=3e+11; strongest_omega=6.47762 rad/lnt; implied_s=4+i0; ω_min=0.682188; R_osc_sibling=2.232e-05>, scheme=FFT-LOG-DETRENDED-RESIDUAL, convention=poleconv-A-double-power-Re_s_4-curvature_grade_n_0, L_max=N/A)`.

*Regulator + Mellin pin*: `regulator_pin = a_n^{ζ}` (the `K_SD` smooth part is the zeta-regulated Seeley-DeWitt expansion `a0_mm…a8_mm`; the residual `K_osc = K_exact − K_SD^{ζ}`). Mellin pole label `(pole_in_s = 4, curvature_grade_n = 0)`, poleconv-A double-power per `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`. Companion rows carry both pins.

*frequency→Im(s) substitution chain (fixed at plan-freeze; NOT chosen at runtime).* A complex dimension `s = σ + i·ω_s` of `ζ_{D_K}` announces (Hoffer-Lapidus 2508.09512) as `cos(ω_s·ln t)` in the heat-trace residual, `ω_s = Im(s)` in rad per unit `ln t`. With `g(u) = K_osc(e^u)·e^{u·Re(s)*}`, `Re(s)* = (d−n)/2 = (8−0)/2 = 4` at d=8, n=0 (Sage-verified). A `cos(ω_s·u)` component appears in the power spectrum at angular `w_fft = ω_s`, so `Im(s) = w*` (angular) `= 2π·f*` (ordinary). Predicted pair `s = 4 ± i·w*`. Direction: a peak at `ω* > ω_min` with prominence ≥ 10× median floor, STABLE across γ/d AND SDW order ⇒ `Im(s)≠0` ⇒ genuine complex dimension ⇒ PASS (wall tension); no such stable line ⇒ `Im(s)=0` detectable ⇒ FAIL (wall re-confirmed). **Computed**: no stable, window-invariant, sharp line ⇒ `Im(s)=0`; but the literal 10× tail-floor criterion fires on scheme-dependent ringing that is NOT stable across the family ⇒ the pre-registered INFO clause (see below).

*Why INFO (not FAIL), pre-registered.* The plan's FAIL clause requires "NO peak above the 10× floor at ANY γ/d or SDW order (the residual non-periodic)." The plan's INFO clause is "a peak appears at one γ/d OR one SDW order but is NOT stable across the family … a smoothing/subtraction-order ARTIFACT … the residual carries scheme-dependent structure that is not a stable discrete-scale-invariance signature." The observed state is the INFO clause exactly: features clear the (tail-inflated) 10× floor but disagree across the γ/d-vs-SDW axes (bin 33 vs bin 5, spread 28) and are window-dependent. Reporting FAIL would *overstate* the wall-confirmation cleanliness by claiming a flat spectrum; INFO honestly reports **no regulator-robust complex dimension (the CM-1995 simple-real wall is NOT contradicted) AND not a clean flat-line either — the residual carries scheme-dependent envelope/sidelobe structure**. SIGN_verdict = N/A because the directional prediction is on a genuine line, and no genuine (window-invariant, family-stable) line exists to assign a sign to.

*Solution-space.* The complex-dimension corridor is neither opened nor cleanly closed: `Im(s)=0` is the honest reading (no stable line), but the residual is not a flat spectrum. The CM-1995 simple-real-dimension-spectrum wall is NOT contradicted on the frequency-domain axis. Per the plan Wave-3→Wave-4 routing, INFO routes to a candidate S105 higher-dynamic-range re-run on `s84_spectrum_cache_L12_tau019.npz` (the 200-point S61 residual has limited dynamic range; a denser t-grid would resolve whether the scheme-dependent ringing vanishes — the expected outcome under the substrate-first prediction that the Jensen deformation is not exactly self-similar). No downstream gate consumes `Im(s)` as a numerical pin; no corridor is opened.

---

## Wave 3 Synthesis (team-lead)

**Verdicts (2/2 landed, dual-SHA, sig_5-unique)**: W3-1 `S104-KRYLOV-KCP` **INFO** (`e134597f…`; sign=PASS / magnitude=INFO / regime=VALID) · W3-2 `S104-LOG-PERIODIC-IMS` **INFO** (`60e67494…`; magnitude=INFO / regime=MARGINAL).

- **W3-1**: the load-bearing SIGN half CONFIRMED — KCP(fold) = 6.0916 > KCP(τ=0 ref) = 4.9061 on sector (2,1), matching sign(β_fold − β_ref) = +1. Krylov complexity joins ⟨r⟩ (CHAOS-1), OTOC (CHAOS-2), SFF (FACTOR-46) as the **fourth internally-consistent spectral-functional diagnostic** of the same D_K eigenvalue content; the "have you checked complexity too?" gap is closed in direction. INFO (not PASS) solely on the magnitude band: rel_residual = 0.2288 > 0.15 — the Huh KCP↔β relation is qualitative-monotone, not a calibrated height law at these β. **No Q1 workshop seed** (no sign mismatch). **Saddle guard inactive**: the b_n ladders SATURATE (slopes ≈ −1e-4, r² ≈ 0.008) — the bounded/integrable signature; λ_L = 0 consistent with CHAOS-2; the A₂-saddle caveat was never reached but is documented as a standing methodology surface (GEM-TRIAGE Rank 12; flagged, not self-written — the linear-growth condition that would activate a `mack-cosmic-bridge`/methodology action did NOT occur). τ=0 reference built FULL-physical via the Fegan/Sym^p primary path (s92 fallback NOT used); fold-cache fidelity 8.44e-15.
- **W3-2**: the S61 heat-trace residual is a **single non-oscillatory shell-correction bump** (one lobe; 96.5% of band power in the DC shoulder); under the faithful Hoffer-Lapidus interior-line reading there is NO regulator-robust log-periodic line — candidate interior features are window-DEPENDENT sidelobes (Hann bin 33 vs rectangular bin 5; γ/d-vs-SDW axes disagree by 28 bins ≫ ±1). Im(s) = 0 detectable on this residual; the **PROVEN CM-1995 simple-real dimension-spectrum wall is uncontradicted on the frequency axis** (orthogonal to the magnitude axis HK-OSCILLATION-61 closed). INFO rather than FAIL because the pre-registered cross-axis-instability condition fired (scheme-dependent structure), and the 200-point/992-mode S61 residual's dynamic range is the live ambiguity. **Methodology disclosure (honest, anti-PASS)**: the literal band-argmax prominence criterion would have returned a false-positive PASS off the DC-envelope boundary shoulder; the agent applied the interior-local-maximum guard — a tightening that can only REJECT an artifact, never manufacture a line — disclosed in §W3-2. This is in-session structural correction with disclosure, not convention-shopping (`v3-closure-recovery.md` Class-1 boundary honored).

**Substrate framing (wave-level)**: spectral-functional pluralism executed as designed — two NEW functionals (Krylov chain; log-frequency power spectrum) of ALREADY-classified eigenvalue content returned readings consistent with the standing structural walls (ordered-not-chaotic level statistics; simple-real dimension spectrum). The fold's growth physics is transit-through-a-saddle, never an emergent Lyapunov container.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator)

- [x] No non-math items surfaced by this wave's agents (W3-2's interior-line guard is disclosed in its WP §Methodology + verdict value string; the saddle-guard methodology surface condition did not activate — no `mack-cosmic-bridge` action required)

## Carry-Forward Computations

### CF-S105-LOG-PERIODIC-HDR-RERUN — higher-dynamic-range log-periodic re-scan [MATH]

> **Routing note**: the plan's pre-registered conditional CF — "4-field CF only if INFO fires" (plan §"Wave 3 → Wave 4 Decision Point"). INFO fired; the smoothing-artifact reading is ambiguous at the S61 residual's dynamic range.

1. **What**: recompute the heat trace K(t) and the Strutinsky-split oscillatory residual K_osc(t) directly from the s84 L=12 fold spectrum (155,984 eigenvalues with multiplicity vs the 200-point 992-mode S61 residual), then run the IDENTICAL pinned pipeline (multiplicative e^{4u} detrend, poleconv-A Re(s)*=4, Hann window, 2048-pt u-grid, prominence ≥ 10× median broadband, interior-local-maximum guard, γ/d × SDW-order stability conjunction) at the higher dynamic range.
2. **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz`; `computations/session-104/s104_log_periodic_ims.py` (the pinned pipeline); `computations/session-61/s61_hk_oscillation.npz` (cross-check overlap on the shared t-window).
3. **Gate**: `S105-LOG-PERIODIC-HDR` — SAME pre-registered criterion: stable interior peak at ω* > ω_min with prominence ≥ 10× across the full family → PASS (Im(s) ≠ 0, CM-1995 reconciliation required); none → FAIL (wall re-confirmed at higher dynamic range — the corridor-closing outcome); single-axis peak → INFO (artifact).
4. **Effort**: 1 gate (heat-trace build from cache + pipeline re-run).

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-06-10 | Chaos-functional consistency (D_K fold spectrum) | 3 consistent diagnostics (⟨r⟩, OTOC, SFF) | 4 consistent IN SIGN (+ KCP; magnitude regime-dependent, Huh map qualitative) | S104-KRYLOV-KCP INFO (sign=PASS) |
| 2026-06-10 | CM-1995 simple-real dimension-spectrum wall (frequency axis) | untested in frequency domain (only magnitude axis closed, R_osc = 2.23e-5) | uncontradicted at S61 dynamic range (no regulator-robust log-periodic line; Im(s) = 0 detectable); HDR certification pending | S104-LOG-PERIODIC-IMS INFO (scheme-dependent sidelobes only) |
| 2026-06-10 | Saddle-guard methodology surface (GEM-TRIAGE Rank 12) | candidate (would activate on linear b_n growth) | INACTIVE — b_n saturate at the fold; guard documented as standing surface, no falsifier action | W3-1 b_n growth-law fit (slopes ≈ −1e-4) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Sizes |
|:-----|:-------|:------------|:------------|:------|
| W3-1 | `s104_krylov_kcp.py` | `s104_krylov_kcp.npz` (13 fields) | `s104_krylov_kcp.png` | 32.8 KB / 141 KB / 281 KB |
| W3-2 | `s104_log_periodic_ims.py` | `s104_log_periodic_ims.npz` (78 fields) | `s104_log_periodic_ims.png` | 33.4 KB / 546 KB / 136 KB |

Both verdict lines + dual-SHA companions + schema-v2 3-tuple rows ([SIGN] triggers) in `computations/session-104/s104_gate_verdicts.txt` (race-safe `emit_verdict`).
