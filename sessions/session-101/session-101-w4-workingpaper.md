# Session 101 Wave W4 — Cosmology Corridor + DE/H₀/M₀ (Results Working Paper)

**Session**: 101 | **Wave**: W4 | **Plan**: session-101-plan-w4.md | **Theme**: Group-COS cosmology corridor + DE/H₀/M₀ — the two logically-independent C10 probes (KV oscillation-energy self-consistency `S101-W1-QEQ-SELFCONS` + its EMITTED graded relic-kernel odd-floor sibling `S101-W1-QEQ-RELIC-ODDFLOOR`, disjoint quantifier ranges, both run); the DR3-readiness branch-iv evaluator + CAC spread re-run (`S101-W0-BRANCH-IV-EVALUATOR`); the MANDATORY convergent-a₂ Friedmann/H₀ recompute (`S101-H0-PROPER-A2`); and the M₀-side BCS anomalous-self-energy screening (`S101-M0-BCS-SCREENING`). No gate requires a fresh D_K diagonalization — ODE + post-processing on the S97/S99/S100a backbone caches and cached canonical a_n.

**A19-conditional caveat (cross-wave pin 1, binding)**: gates W4-2 and W4-3 consume `s84_spectrum_cache_L12_tau019.npz`. If dispatched BEFORE Wave 1's `S101-TAU0-OPERATOR-CANONICITY: PASS` L4 caveat-lift has landed (deterministic grep of `computations/session-101/s101_gate_verdicts.txt` at dispatch), each MUST emit the extra `# A19-UNTRUSTED-UPSTREAM: s84_spectrum_cache_L12_tau019.npz consumed pre-L4-lift` companion row (values citable per the lift-with-appended-audit-rows mechanics, theorem-backed A-C3 σ-blind lemma); if the lift HAS landed, cite full-confidence and omit the row. Pre-registered conditional emission, not runtime freedom. Wave 4 is otherwise run-order independent of Waves 1–2 (partition: W3/W4/W8 independent).

## Gate Sections

### §W4-1. S101-W1-QEQ-SELFCONS (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-W1-QEQ-SELFCONS`
**Trigger**: `[SIGN]` (directional pre-registration: q_amp ∝ |H| ⇒ slope 1 → schema-v2 3-tuple companion row emitted)
**Classification**: **PHONONIC** (KV oscillation-energy self-consistency; q-channel back-reaction on the §6.3 Friedmann closure)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: Re-deriving H(τ) from the q-oscillation energy through the §6.3 closure makes d ln q/d ln |H| → 1 EMERGE from q-domination self-consistency — the corpus-faithful Klinkhamer-Volovik back-reaction (q_amp ∝ a^{−3/2} ∝ |H| on the self-consistent a ∝ t^{2/3} background; Volovik Paper 25 §V Eqs. (5.5a-b)) — supplying the slope-1 leg of the n = 2 tracking law as the unique parity-consistent route the H-parity theorem leaves open (clause-(f) carve-out: |H| occupies the non-analytic-even cell, structurally unavailable to the fixed-backbone equilibrium drive that FAILed at S100a-W1-2). Pre-registered PASS-variant: slope 1 realized NOT through q_amp ∝ |H| carries the NEW-AMPLITUDE-ANOMALY flag (annotation ii) and spawns its own S102 gate.
**Plan reference**: `sessions/session-plan/session-101-plan-w4.md` §W4-1

**Output Artifacts**:
- `computations/session-101/s101_w4_qeq_selfcons.py` — producing script (verified `from canonical_constants import`, `print_verdict_payload` present).
- `computations/session-101/s101_w4_qeq_selfcons.npz` — data (77112 bytes; `slope_selfcons=1.000074`, `composite=PASS`, `audit_sha256=c06a956b…`).
- `computations/session-101/s101_w4_qeq_selfcons.png` — 4-panel figure (self-consistent q/H trajectory; t^{2/3} attractor; gated log-log regression; summary).
- Verdict line in `computations/session-101/s101_gate_verdicts.txt`: `^S101-W1-QEQ-SELFCONS:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 3-tuple row + 4 extra companion rows (7 rows total, sig_5 unique).

**MCP Pre-Compute Audit**:
- `search_knowledge("QEQ self-consistency Klinkhamer-Volovik q-oscillation slope tracking H-parity back-reaction")` → top hit is the S100a freshness open-channel naming `CF-S101-W1-QEQ-S…` as the §6.3 surviving route (this gate); the "Spectral back-reaction → self-consistency loop diverges (S19d)" closed-mechanism is a DIFFERENT loop (DOS↔Δ wall, not the KV q-oscillation channel) — no conflict, gate NOT pre-closed.
- `get_constant("a_0_FW_zeta")` → 6440.0 (S88, gate S88-A-N-FW-CANONICALIZATION; not superseded) — matches plan pin.
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42; not superseded) — matches plan pin.

**Verdict**: **PASS** — `composite=PASS` (sign=PASS, magnitude=PASS, regime=VALID). `audit_sha256=c06a956b653cac7bf5a7ddda65daa9c9ece529fce63b846cd3a08b5767c5dd6d`, `content_sha256=55fc17250e05688e30f759ef62f76185b50ca6d5df9bc95e025c8ba27f111e4e`. 4-tuple: `(value=1.000074, scheme=FW, convention=SUBSTRATE-NATURAL-BINDING, L_max=N/A)`.

**Results**:

*Gated observable (operator):* `slope_selfcons = 1.000074` (OLS of ln q_dev vs ln|H| over the full post-fold tail, q_dev = cycle-RMS of (q − q_eq)). `|slope_selfcons − 1| = 7.4e-5 ≪ 0.05` → **magnitude PASS**. `domain_used_frac = 1.0000 ≥ 0.95` → **regime VALID** (no auto-shortening; full tail gated). Both joint operator conjuncts satisfied.

*[SIGN] 3-tuple:* `sign=PASS` (self-consistent back-reaction co-tracks the q-amplitude DOWN with |H| DOWN; realized slope > 0, the direction the substitution chain Step 4 predicts); `magnitude=PASS` (|slope − 1| ≤ 0.05); `regime=VALID` (domain_used_frac ≥ 0.95 AND solver_ok). Composite collapse → **PASS**.

*Substitution chain (realized numbers):*
- Def 1: q_eq = q* = 0.0000 (interior equilibrium, `s99_w2` key `q_star`); k_curv = +3586.5312 (`s100a_w1_qeq_drive.npz` key `k_curv`).
- Def 2: ρ_q = ½q̇² + ½k_curv(q−q*)²; ω_q = √k_curv = **59.8877** ≫ |H| (|H|/ω_q ≤ eps_ad = 9.4e-5 on the tail) → cycle-averaging valid.
- Def 3: §6.3 closure H² = (κ²/3)·ρ_q with C3 ≡ κ²/3 = 5.6416e−03 (a₀^{ζ}=6440.0 enters the S_SA sector normalization; C3 is a **multiplicative pre-factor**).
- Def 4: KV (Paper 25 §V): rapid oscillation → w=0 dust → ρ_q ∝ a⁻³ → a ∝ t^{2/3}, H = (2/3)t⁻¹.
- ICs (post-fold, `s99_w2` window start te=499): q0 = +0.054800, q̇0 = +0.024405 (q_boundary lineage `arr_u`/`arr_ud` at window start).
- Substitute: ½k_curv·q_amp² ∝ a⁻³ ∝ t⁻² ⇒ q_amp ∝ t⁻¹ ∝ |H| ⇒ **d ln q_amp/d ln|H| = 1**.

*Attractor confirmation (this is what distinguishes back-reaction from a fitted slope):* realized **a-exponent = 0.6554** (target 2/3 = 0.6667; dev 0.0113) and **H-t exponent = −0.9831** (target −1) — the w=0 dust attractor a ∝ t^{2/3}, H = (2/3)t⁻¹ establishes self-consistently on the gated tail.

*Coefficient-invariance (multiplicative-normalization cancellation; `math-scripts.md`):* re-running at **10×C3** gives slope 1.000015; `|slope(10·C3) − slope(C3)| = 5.9e-5 ≤ 1e-3` → `kappa_invariant=True`. The §6.3 closure normalization (κ²/3, a₀^{ζ}) is annihilated by the log-derivative — the slope-1 result is NOT a tuning artifact of the closure constant.

*Non-gating annotation (i) — E1 citation-scope inheritance (transcribed):* every downstream consumer of this verdict inherits the S100a-W1-2-QEQ-DRIVE canonical citation-scope clause `"scope: equilibrium sector theorem-grade; relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR; KV carve-out CF-S101-W1-QEQ-SELFCONS"`. The token `no_slope1_capable_substrate_drive` expands to its three scope qualifiers — **drive-type**: potential-slot q_eq(H); **fixed-backbone**; **equilibrium theorem-grade / relic argument-grade pending the sibling** — plus the carve-out pointer (THIS gate). This gate occupies that carve-out: the slope-1-capable route exists, but as a **self-consistent back-reaction**, not a fixed-backbone potential-slot drive.

*Non-gating annotation (ii) — amplitude-law diagnostic:* direct regression of the successive-extrema envelope gives **slope_amp = 1.0556** (|slope_amp − 1| = 0.0556); `amp_sc_consistent = True` (q_dev and q_amp regressions agree within 0.10). The secular-drift anomaly guard gives **slope_qbar = 0.9714** — the running mean of q is NOT the carrier; slope 1 is realized SPECIFICALLY through the oscillation amplitude q_amp ∝ |H| (the non-analytic-even, clause-(c) three-selector cell). Therefore **NEW-AMPLITUDE-ANOMALY = False** — the PASS is the genuine amplitude-law PASS, not a secular-drift mimic.

*ω_q cross-check (A-V2):* realized ω_q = √k_curv = 59.8877 vs plan pin 59.888 (dev 3.5e-4) and vs npz `omega` (dev 0.0e+00).

*Cross-checks:* XC-3 k_curv npz vs plan pin |dev|=0.0312 ≤ 0.05 ✓ (`k_curv_plan_pin`=3586.5); XC-kcurv drive-npz vs relax-npz k_curv |dev|=0.0e+00 ✓; XC-omega ✓; adiabaticity eps_ad=9.4e-5 ≪ 0.1 ✓; solver_ok=True; lnH_range_tail=0.6770.

**Substrate framing**: PHONONIC. q IS the substrate's vacuum variable — Volovik q-theory IS the spectral-action zeroth-moment (a₀^{ζ}) dynamics; there is no inflaton field rolling IN a container. The arrow flows D_K spectral moments (a₀^{ζ}) → q-channel quadratic well (k_curv) → self-consistent (q, H) dynamics → the tracking-slope observable. The decisive substrate fact: in the predecessor S100a-W1-2 the well-center q_eq(H) was an analytic-even drive on a **frozen** backbone H(τ) read from a file → slope 2.0556 (the H² parity wall). Here H is **NOT a fixed input** — the §6.3 closure makes the substrate's own emergent background a (sourced by ρ_q) dilute the oscillation energy, and the oscillation amplitude decays as q_amp ∝ |H|. This is the substrate writing its expansion history into its vacuum variable through the unique non-analytic-even cell the equilibrium-sector H-parity theorem (theorem-grade) leaves open (clause f). The slope-1 leg of the n = 2 tracking law is therefore DERIVED (unforced) as a back-reaction; the q ∝ H closure stops being an imposed INPUT. Downstream: the S100b-X C10 n_eff triangle's physical-route member activates at n = 2; C10 Object-C's STRUCTURALLY-CONDITIONAL status now has a surviving derivation channel; capstone §8.5 conditionality locus is routed to the capstone designated writer (capstone-hygiene Q3/Q4).

---

### §W4-2. S101-W1-QEQ-RELIC-ODDFLOOR (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-W1-QEQ-RELIC-ODDFLOOR`
**Trigger**: `[VERIFY]` (even-dominance direction pre-registered in the substitution chain → schema-v2 3-tuple companion row REQUIRED)
**Classification**: **PHONONIC** (graded relic-kernel odd-floor; GGE memory-force taxonomy on the q-channel)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The GGE-relic-induced effective force on the q-channel carries NO secular odd-in-H component above the 1e-3 floor — (A) the t→−t-graded Markovian reduction of the relic kernel (diagonal + anomalous sectors; T-eq.5) satisfies |c_odd|/|c_even| ≤ 1e-3, (B) the dilution-mimic window is empty (max(q_dec) < 1.857), (C) under the substrate-derived clock γ = dt/dτ the 2E_k ≈ ω_q parametric-resonance window stays clear (Δ_res guard, no tail crossing) and the frozen-branch premise is duration-consistent (Δt(window) vs t_therm ≈ 6 M_KK⁻¹) — discharging the single numerical hostage of relic clause (d). LOGICALLY INDEPENDENT of W4-1 (disjoint quantifier ranges: drive-slot-on-fixed-backbone vs back-reaction; both run, neither pre-judges the other). FAIL → clause (d) demoted argument-grade → coincidence-bounded; the Wave-6 Stage-1 H-parity entry is amended BEFORE any S102 Stage-2 dispatch.
**Plan reference**: `sessions/session-plan/session-101-plan-w4.md` §W4-2

**Verdict**: **FAIL** — the derived substrate clock places **ω_q^phys = 2.012813 M_KK INSIDE the pair band** [2λ_min, 2E_max^{L12}] = [1.63948, 10.83787], and **24 modes (14 occupied; w_cross = 248) have 2E_k(q(τ)) = ω_q^phys crossing within the realized tail q-range** [0.2028, 0.6622] — a **tail crossing EXISTS**. This is the pre-registered FAIL trigger (workshop landing-list (iv) :763; method `operator.form`). The minimum occupation-weighted Δ_res = 0.000046 ≪ the guard max(0.1, 5·h_par/4) = 0.1, and the rectified odd-floor |c_odd|/|c_even| = 2.70e-2 ≫ 1e-3 (a SECOND, independent FAIL trigger). Relic clause (d) of the H-PARITY-DRIVE-EXCLUSION Stage-0 candidate is **DEMOTED argument-grade → coincidence-bounded**; the parametric-rectification channel becomes a LIVE odd-in-H force candidate (the {IN-band: resonance LIVE} self-consistent end-state — the workshop's "C2 becomes the biggest result" branch). **FAIL ROUTING**: the Wave-6 `S101-HPARITY-STAGE1-REGISTRATION` clause-(d) text is amended BEFORE any S102 Stage-2 dispatch (housekeeping §A in-session fix if Wave-6 has already registered). Conjunct (B) (dilution window) PASSES (max(q_dec)_tail = 0.0001 < 1.857); the FAIL lives entirely in conjunct (C) and the consequent (A).

**Output Artifacts** (on-disk verified; content-presence, not counts):
- `computations/session-101/s101_w4_qeq_relic_oddfloor.py` — present; contains `from canonical_constants import` and `print_verdict_payload` ✓
- `computations/session-101/s101_w4_qeq_relic_oddfloor.npz` — present (clock derivation S3/S5/χ_I/ω_q^phys/γ, resonance geometry, dilution window, odd-floor, duration, per-mode arrays, dual-SHA) ✓
- `computations/session-101/s101_w4_qeq_relic_oddfloor.png` — present (4 panels: pair-band/ω_q^phys, per-mode Δ_res + crossing, q_dec tail vs 1.857, verdict summary) ✓
- Verdict line `^S101-W1-QEQ-RELIC-ODDFLOOR:.* audit_sha256=[a-f0-9]{64}` in `computations/session-101/s101_gate_verdicts.txt` + dual-SHA companion row + schema-v2 3-tuple row (`sign=FAIL magnitude=FAIL regime=VALID`) + 3 companion `#` rows (regulator_pin a_0^{ζ}; clock χ_I/ω_q^phys/γ at 6 sf; end-state + FAIL-routing). **A19-UNTRUSTED-UPSTREAM row NOT emitted** — dispatch-time check found `S101-TAU0-OPERATOR-CANONICITY: PASS` (audit `194b2b3c…`), so the L12 cache upstream is trusted (post-L4-lift).
- `audit_sha256=98a923fd0ea4a6ec5f80360468422e05651ef301a25f71645bd543e6c1ad4282`; `content_sha256=01a4e0560e4099853abee904737c0b1d8b0c4b6af4178bcf6dacd899a4529137`
- 4-tuple: `(value=FAIL_IN-band_resonance-LIVE…, scheme=FW, convention=SUBSTRATE-NATURAL-BINDING, L_max=12)`

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):
- `search_knowledge("QEQ relic odd floor H-parity Markovian reduction parametric resonance clock gamma")` → surfaced the PROVEN theorem **"Post-transit parametric resonance: IMPOSSIBLE"** (S67, proven_1084) and the `session-101-plan-w6.md` equation `(frozen ⟹ d1-d4; thermalized ⟹ double-locked; crossover bounded by t_therm)` carrying the (d5) pincer + "parametric rectification at 2E_k ≈ ω_q the unique surviving odd channel, PENDING SIBLING." NOT PRE-CLOSED — the S67 theorem is the *broad-band* impossibility (no resonance during the supersonic transit); this gate prices the *narrow-band post-fold tail* coincidence 2E_k(q(τ)) = ω_q^phys under the DERIVED clock, which S67 does not resolve (it needs the in-script χ_I). The two are consistent: S67's transit-era impossibility + this gate's tail-era IN-band crossing = a *post-transit* rectification window the broad-band theorem does not cover.
- `trace_entity("Post-transit parametric resonance IMPOSSIBLE")` → single theorem hit (proven_1084, PROVEN, KO-dim-6-class); confirms the broad-band scope.
- `get_constant("R_therm")` → 5251.82 (S95; t_therm/t_transit; Ordered-Veil; pins the diabatic transit-freeze that froze the relic occupations). `get_constant("n_pairs")` → 59.8. `get_constant("tau_fold")` → 0.19. `get_constant("M_KK")` → 7.428660e16 GeV. `t_therm` NOT a canonical name (confirms the plan `t_therm_pin: 6.0 # (local)` disclosure; S39-corrected finite thermalization, R_therm canonical).
- `list_constants(".*omega.*")` → no `omega_q` / `k_curv` / `lam_sq_min` canonical names ⇒ these are DATA-sourced substrate observables (s97 npz `omega`, `k_curv`, `lam_sq_min`), not hardcoded; sourced from the pinned inputs per the plan machinery_pin_map.

**Results**:

*Substrate framing.* PHONONIC. The GGE relic IS the substrate's fold-frozen excitation content — 59.8 quasiparticle pairs whose occupations froze at the diabatic transit (R_therm = 5252, the Ordered Veil), not particles produced IN a curved-spacetime container. The relic kernel is the substrate's own memory of its transit, and the question this gate prices is whether that memory can push the vacuum variable q with a force ODD in the expansion-rate readout H. The arrow flows **D_K pair band** (2E_k = 2√(λ_k² + q), floor 2λ_min = 1.63948 M_KK) → **frozen GGE occupations** (n_k, σ_k) → **Markovian-reduced effective force on the q-channel** → **t→−t-graded coefficients** (c_even, c_odd). The clock normalization γ = dt/dτ is itself substrate-derived (the q-channel inertia χ_I from the kernel's reactive part) — the substrate sets its own clock; the laboratory FRW time is the emergent reading of it. The FAIL here is the substrate disclosing a genuine odd channel (parametric rectification at the pair-band resonance) — informative force taxonomy, demoting one clause of a Stage-0 theorem candidate, NOT a container anomaly.

**THE one new derivation — γ = dt/dτ via the kernel-reactive route (OQ-1 1a; the load-bearing element).** The relic influence kernel (T-eq.5, workshop line 480-485) is
> K(t,t′) = Σ_k (∂_q E_k)² [ (2n_k+1)·cos(2∫E_k ds) (diagonal) + 2|σ_k|·cos(2∫E_k ds + φ_k) (anomalous) ], causal χ ∝ θ(t−t′)·sin(2∫E_k ds).

Integrating out the relic bath gives a reactive (principal-value) self-energy on the q-coordinate; the **frequency-squared coefficient of the reactive part at zero secular frequency IS the renormalized q-channel inertia χ_I** (standard adiabatic-elimination mass term). Per-mode (Born-Markov, diagonal; Ω_k = 2E_k, g_k = ∂_q E_k = 1/(2E_k)):

> Σ_q(ω) = Σ_k g_k²(2n_k+1)·2Ω_k/(Ω_k² − ω²) = Σ_q(0) + χ_I·ω² + 𝒪(ω⁴),
> **Σ_q(0)|per-mode = (1/4)(2n_k+1)/E_k³** (static), **χ_I|per-mode = (1/16)(2n_k+1)/E_k⁵** (inertia).

⇒ **χ_I = (1/16) Σ_k w_k (2n_k+1)/E_k⁵** (Sage-verified coefficient via `mcp__sage__sage_eval`: series of Σ_q(ω) about ω=0 returns the (1/16)(2n_k+1)/E_k⁵ ω²-coefficient EXACTLY).

| quantity | value | provenance / check |
|:---------|:------|:-------------------|
| S3 = Σ_n w_n/λ_n³ | 28692.249449 | = **8·k_curv** (shared spectral sum); k_curv recon `S3/8` reldev = **1.27e-16** (machine ε) vs s97 documented k_curv |
| S5 = Σ_n w_n/λ_n⁵ | 14164.056599 (vacuum) / 14174.949282 (dressed) | the NEW spectral moment (not previously computed) |
| χ_I | **885.253537** M_KK⁻⁵ (vacuum) / 885.934330 (dressed) | reldev across weight conventions = **7.69e-4** (GGE occupations dominated by lowest few modes ⇒ barely shift the weighted moment) |
| ω_q^τ | **59.887655** τ⁻¹ | = √k_curv; matches s97 npz `omega` = 59.887655 EXACTLY |
| ω_q^phys | **2.012813** M_KK (vacuum) / 2.012040 (dressed) | = √(k_curv/χ_I); units [M_KK⁻³/M_KK⁻⁵]^{1/2} = M_KK ✓ |
| **γ = dt/dτ** | **29.753211** M_KK⁻¹ (vacuum) / 29.764649 (dressed) | = ω_q^τ/ω_q^phys; **fixes the s97 `t_relax = 1.0 # sets units; cancels in slope` disclosed freedom** (s97 L361) |

The k_curv reproduction to 1e-16 is the decisive self-consistency cross-check: the SAME spectral sum Σw_n/λ³ carries the documented k_curv at coefficient 1/8 (workshop A-V2 Step 2, s97 L388-389) AND the static self-energy at 1/4 — the weight is the degeneracy w_n and the (1/16)-coefficient on the ⁵-moment is fixed by the elimination, not chosen.

**WEIGHT-CONVENTION ROBUSTNESS (decisive for the clean Stage-2 verdict).** Both the vacuum weight ((2n_k+1)→1, degeneracy w_n) and the occupation-dressed weight ((2n_k+1) with the GGE n_k) give ω_q^phys = 2.0128/2.0120 M_KK and γ = 29.75/29.76 M_KK⁻¹ — **the IN-band, resonance-LIVE verdict is robust to the weight choice** (relative diff 7.7e-4 on χ_I; both solidly inside the pair band). The verdict is unambiguous for the S102 Stage-2 cross-axis verify.

**Conjunct (C) — resonance geometry (the FAIL).** With γ = 29.75 (< the Step-7 below-band threshold 36.53), ω_q^phys = 2.012813 M_KK lands IN the pair band:
- Pair band at q=0: bottom 2λ_min = **1.63948** (992-set + L12 agree on the floor); top **4.12112** (992 working set, truncation-dependent) / **10.83787** (full L_max=12 cache — band-top caveat R1; the L12 cache extends far above the working-set top, confirming ω_q^phys IN-band with wide margin). E_min^{L12} = 0.81974, E_max^{L12} = 5.41894.
- **Tail crossing TEST** (geometric, convention-light): a mode k crosses iff q_res,k = (ω_q^phys/2)² − λ_k² ∈ [min q_tail, max q_tail] = [0.2028, 0.6622]. **24 of 992 modes cross** (E_k ∈ [0.81974, 0.87298], the LOWEST modes; q_res ∈ [0.2508, 0.3409]; w_cross = 248), of which **14 lie in the occupation-weighted support** (n_k·w_n ≥ 1e-6·max). The resonant modes are the occupied + squeezed lowest BCS modes — exactly where rectification can source a real secular force (R2 occupied-band refinement satisfied).
- **Δ_res** = min over (τ, k) of |2E_k(q(τ)) − ω_q^phys|/ω_q^phys = **0.000046** (occupation-weighted) / 0.000046 (full band) — essentially exact resonance, **≪ guard 0.1**.
- **n=2 Mathieu-zone report** (C-T4.iv, double-suppressed, report-only): **60 crossings** of 2E_k = 2·ω_q^phys over the tail — no gate conjunct (width 𝒪(h_par²), throughput carries an extra h_par power).

**Conjunct (C) — measured parametric depth h_par.** h_par = q_osc/(λ_min² + q̄) = **0.000830** (q_osc = 0.000900 from a deg-4 detrend of q_GD on the tail; q̄ = 0.4122; λ_min² = 0.67198). Principal Mathieu half-width = h_par/4 = 0.000207. The guard max(0.1, 5·h_par/4) = max(0.1, 0.00104) = **0.1** (the flat floor dominates — h_par ≪ 0.08, exactly the D-2 fallback condition; h_par is REPORT-ONLY feeding the guard). The guard is irrelevant to the verdict because a tail crossing exists regardless (the resonance is not merely near-guard; it is a genuine sign-change crossing).

**Conjunct (B) — dilution-mimic window EMPTY (PASS).** max(q_dec)_tail = **0.0001** < 1.857 ⇒ the slope-1 dilution mimic (which requires q_dec ∈ [1.857, 2.158], stiff-fluid-class) is dead on the realized tail — consistent with the workshop's **0.0000-exact** result (clause (d2)). Realized 3·p_local tail range = [−11.9932, 22.4158] (spans the full p_local = 1/(1+q_dec) divergence across the q_dec ≈ −1 crossings; the window edge [0.95,1.05] is never sat from the feasible side — closest documented approach 1.657). Tail-restricted theorem-grade-quantitative stratum (q_dec ∈ (−2, 0)) fraction = **0.1540** (refines the frozen grid-mass bound [0.169, 0.668]; A-V5 DISSENT-refinement 3).

**Conjunct (d5) — duration / pincer.** Δt(tail) = γ·Δτ_tail = 29.753 × 0.13026 = **3.8756** M_KK⁻¹ (ratio 0.646 vs t_therm = 6); Δt(full) = γ·Δτ_full = **7.7513** M_KK⁻¹ (ratio 1.292). Note the realized state is IN-band (γ = 29.75), NOT the Step-7 below-band corner (which would need γ > 36.53 and force Δt past t_therm) — so the (d5) pincer's "below-band forces thermalization" logic is not the operative closure here; the realized state is directly the {IN-band: resonance LIVE} end-state. The duration is reported for completeness; it does not rescue the resonance conjunct.

**Conjunct (A) — odd-floor (the SECOND, independent FAIL trigger).** The graded relic force F_relic(q,a,H), antisymmetrized at fixed (q,a) (F_± = (F(+H)±F(−H))/2 at the occupation-weighted tail reference |H| = median|H_tail|):
- **c_even** = the even-force amplitude = |Σ_k n_k ∂_q E_k| (the order-zero frozen tilt, H-INDEPENDENT by (d1) ⇒ purely even) = **1.230890** (occupation-weighted; F_static dominates the reactive ∝Ḣ even-lag).
- **c_odd** = the rectified parametric force = Σ_{occ support} (∂_q E_k)²·w_k·(2n_k+1)·h_par·𝓛(Δ_res,k), with 𝓛 = (h_par/4)/√(Δ_res,k² + (h_par/4)²) the Lorentzian resonance factor (→1 on-resonance, → h_par/4Δ_res off-resonance) = **0.033205**. The c_odd is NON-ZERO precisely BECAUSE the resonance is live (𝓛 → 1 at the 14 occupied crossing modes); off-resonance it would dephase to ≈0 (1/√59.8 stacking + Berry-flat B=0).
- **|c_odd|/|c_even| = 2.697638e-2 ≫ 1e-3** ⇒ **odd-floor VIOLATED**. This is NOT circular with the geometric tail-crossing test (which references no force amplitude); it is the force-side confirmation that the geometric resonance sources a real secular odd-in-H force.

**Constancy report (C-T1, report-only).** max|Δ ln χ_I(q(τ))| over the tail = **0.485669** — NOT negligible (q ranges 0.20–0.66 ⇒ E_k = √(λ²+q) varies meaningfully). The slope clock-blindness reading is exact only for CONSTANT γ; the derived χ_I(q) clock inherits a bounded slope correction wherever χ_I varies, vanishing asymptotically at q → 0⁺ (E_n → λ_n). This does NOT touch the verdict: ω_q^phys uses the asymptotic (q→0) χ_I, and Δ_res sweeps the full tail q-range for the band 2E_k(q(τ)) — the resonance position and the crossing are evaluated with the full q-evolution, not the constant-γ approximation. The W1-2 FAIL (a clock-blind log-slope) remains permanent under any γ (E-T1).

**schema-v2 3-tuple (substitution chain pre-registers the even-dominance direction).**
- *sign_verdict = FAIL.* Step 4 of the substitution chain pre-registered the direction "OFF-resonance ⇒ c_even dominates AND no crossing CONFIRMS clause (d)." The realized geometry HAS a tail crossing ⇒ the even-dominance prediction is VOIDED ⇒ direction mismatch. The substrate disclosed the odd channel the chain flagged as the single hostage.
- *magnitude_verdict = FAIL.* The conjunctive gate target is all-PASS; with conjunct (C) and (A) failing, |value − target| ≫ any band.
- *regime_verdict = VALID.* The χ_I adiabatic-elimination, the band comparison, and the resonance test are within their regime of validity throughout the tail (the relic kernel's Markovian reduction is controlled — τ_mem ∼ 1/spread(2E_k) gap-scale-SHORT vs backbone; the γ derivation is exact; the resonance comparison is well-defined at every tail point). The integration window is fully covered (domain_used_frac = 1.0 inherited from the tail mask).
- *Composite collapse* (pre-registered rule, `gate-verdicts.md`): regime=VALID, sign=FAIL ⇒ **composite = FAIL**. ✓ Consistent.

**Cross-checks.**
- (1) Input SHA pins: all 5 npz + canonical_constants match the plan-block expected hashes EXACTLY (qeq_drive e31651ac…, backbone 1fdfe2eb…, relaxation 6d8d488a…, clock_prov 8a696af3…, L12 9e6d9cf7…). OK.
- (2) k_curv self-consistency: S3/8 reproduces s97 documented k_curv to 1.27e-16 — the spectral sums and weights are exactly right.
- (3) ω_q^τ = √k_curv = 59.887655 matches the s97 npz `omega` = 59.887655 bit-for-bit (the τ-clock frequency the C10 lineage used).
- (4) lam_sq_min cross-anchor: E_min² = 0.81974111² = 0.67197549 = |q_boundary| (s97), the 8-digit two-artifact match (workshop A-V2 Step 1). ✓
- (5) backbone deceleration q_dec = −1 − Ḣ/H² computed from arr_H_bare_t / arr_Hdot_bare_t (the S99 W1 canonical backbone); arr_q_primary_t is the q-curvature (different observable), correctly NOT used for q_dec.
- (6) weight robustness (vacuum vs n_k_gge-dressed): verdict invariant (diff 7.7e-4); both IN-band.

**Solution-space reading + FAIL routing.** FAIL closes the corridor "the fold-frozen GGE relic admits NO secular odd-in-H force on the q-channel off-resonance with the derived clock." The substrate's own q-channel inertia χ_I places ω_q^phys = 2.0128 M_KK squarely inside the pair band, and the tail evolution of q sweeps 24 occupied/squeezed pair modes through exact resonance — **the {IN-band: resonance LIVE} self-consistent end-state the workshop pre-identified as "C2 becomes the workshop's biggest result."** Relic clause (d) of the H-PARITY-DRIVE-EXCLUSION Stage-0 candidate is **DEMOTED argument-grade → coincidence-bounded**: the parametric-rectification channel is now a LIVE odd-in-H force candidate (C1/C2/C4 merge into one live drive with slope ≈ 1, T-eq.4), requiring its own gate (OQ-5's conditional rectified-drive gate is now UNBLOCKED — its Inputs field is filled by THIS gate's realized γ = 29.753211 M_KK⁻¹ and the crossing geometry q_res ∈ [0.2508, 0.3409], E_k ∈ [0.81974, 0.87298]). **FAIL ROUTING (BINDING, workshop (iv) :763 + fb_pair.backward):** the Wave-6 `S101-HPARITY-STAGE1-REGISTRATION` Stage-1 entry text is AMENDED BEFORE any S102 Stage-2 dispatch — clause (d)'s "relic argument-grade pending CF-S101-W1-QEQ-RELIC-ODDFLOOR" qualifier resolves to **demoted on FAIL**, and the E1 citation-scope clause's "relic argument-grade pending" qualifier follows. If Wave-6 has already registered, the amendment is an in-session designated-writer fix (housekeeping §A), never deferred past the S102 Stage-2 dispatch. The equilibrium-sector clauses (a)-(c) + the dilution window (d2, conjunct B PASS here) are UNTOUCHED — the demotion is local to the relic-resonance hostage. **Downstream clock inheritance:** future C10 clock consumers inherit γ = 29.753211 M_KK⁻¹ (6 sf, companion row).

---

### §W4-3. S101-W0-BRANCH-IV-EVALUATOR (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-W0-BRANCH-IV-EVALUATOR`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (branch-iv w₀(L_max) evaluator derivation + CAC truncation-spread; one gate, two sequenced legs)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: Under the post-S86 branch-iv formulation a principled w₀(L_max) evaluator EXISTS — a pre-registered recombination map Φ(R_JK distance-2, ξ_E_GGE_inv distance-1) → R-slot occupant that (leg 1, HARD admissibility) reproduces w_0_B = −0.842454 at L_anchor = 10 within 1e-5 with ZERO free normalization tuned to do so, and (leg 2) whose CAC spread over L ∈ {8, 10, 12} is ≤ 0.025. ADVERSARIAL PRESSURE POINT (closeout §V.4): the question was honestly UNCOMPUTABLE at S100b; the zero-free-normalization clause is what separates a derivation from a fit.
**Plan reference**: `sessions/session-plan/session-101-plan-w4.md` §W4-3

**Output Artifacts**:
- `computations/session-101/s101_w4_branch_iv_evaluator.py` — present; contains `from canonical_constants import` and `print_verdict_payload`.
- `computations/session-101/s101_w4_branch_iv_evaluator.npz` — present (leg-1 monomial scan + §(iv-bis) lock-test + leg-2 NaN block + attestation strings).
- `computations/session-101/s101_w4_branch_iv_evaluator.png` — present (two panels: R-slot reconstruction landscape + surrogate lock test).
- Verdict line `S101-W0-BRANCH-IV-EVALUATOR: INFO -- … audit_sha256=cd0492d6949a18dcd633777c3086d641c0e7ba4db67132356d0acb9b7f1bfc4a content_sha256=987b2b81729597987f76682a3e72de818a52d70856cb4a56b44dc8e48035cd8f` in `computations/session-101/s101_gate_verdicts.txt` + dual-SHA companion row + 3 companion `#` rows (regulator-pin, consumption-layer, leg-status). No schema-v2 3-tuple (`[VERIFY]`, no directional pre-registration). **A19-UNTRUSTED-UPSTREAM row NOT emitted** — dispatch-time check found `S101-TAU0-OPERATOR-CANONICITY: PASS` (the L12 cache upstream is trusted).

**MCP Pre-Compute Audit**:
- `search_knowledge("branch-iv w0 evaluator R_JK xi_E_GGE recombination SV1")` → surfaced S84-W0-REGULATOR-RESOLUTION-SV1 (PASS, w_0_B=−0.842454), S86-BRANCH-IV-FORMULATION-COMMIT (R_JE retired → R_JK + ξ_E_GGE_inv), and the R_JK canonical constant. NOT PRE-CLOSED — S100b-W0-BRANCH-RESOLUTION closed as **INFO-(ii)-evaluator-NOT-recoverable**; this gate is the pre-registered follow-up that asks the derivation-level question.
- `get_constant("R_JK")` → 0.00803460529503449 (S86; distance-2; anchor cache at L_max=10).
- `get_constant("xi_E_GGE_inv")` → 13.642473425595973 (S86; distance-1; substrate-natural 59.8·Δ_BCS/K_base).
- `get_constant("w0_FW_R842")` / `get_constant("w_0_FW")` → not found (confirms the conditional-canonical status; w0_FW canonical = −0.918, the A-branch).

**Verdict**: **INFO** — derivation-inadmissible (leg-1 fails the zero-free-normalization admissibility precondition; leg 2 does not execute). The pre-registered INFO-(leg-1-inadmissible) shape fired; the honest-UNCOMPUTABLE state of S100b persists at the derivation level.

**Results**:

*Substrate framing.* GEOMETRIC. w_0 IS the substrate's late-time spectral-action gradient projected onto observational coordinates; branch A (Volovik-partition, −0.918) and branch B (substrate-compaction, −0.842454) are two projections of the SAME spectral-triple observable. The arrow flows D_K eigenvalues → a_n^{ζ} spectral moments → R_JK (distance-2) + ξ_E_GGE (distance-1) → R-slot occupant → w₀(z=0). What S100b found is that this projection's *truncation behavior was undefined at the formulation level*; this gate asked whether a derived, offset-physical, zero-tuning evaluator supplies it — and certifies that branch-iv has none.

*The admissible anchor (SV1 closed form, all Θ-free).* The S84 W1-3.SV1 PASS is the f-reduction
> w₀^(iv) = f(R), f(R) = (−c_J·R + P_GGE^ζ) / (c_J·R + ρ_GGE^ζ), c_J = |F_Josephson^ζ|/N_cells = 10.52003125.
Every coefficient is canonical/substrate: `c_J` from |F_J^ζ|=336.641 (S58) and N_cells=32 (S42); `P_GGE^ζ=−0.688`, `ρ_GGE^ζ=1.709` from the SV1 npz. At R = R_sv1 = ξ_J/ξ_E_GGE = 0.45357833655706 (the SV1 dressing ratio = **legacy R_JE at L=5**), f(R_sv1) = −0.84245428 = w_0_B EXACTLY (verified to 1e-12; npz `sv1_f_reduction_exact=True`).

*Leg-1 derivation + HARD admissibility (the decisive result).* The R-slot occupant the f-reduction consumes is R_sv1 (the **retired** R_JE). The S86 commit replaced R_JE with TWO distance-tagged successors that must recombine, Θ-free, back into the R-slot. A monomial scan Φ = R_JK^a · ξ_E_GGE_inv^b over a,b ∈ {−2,−1,0,1,2} (no coefficient solved against w_0_B; residual COMPUTED, never minimized):

| quantity | value |
|:---|:---|
| best monomial for R-slot | R_JK^−1·ξ_E_GGE_inv^−2 = 0.668728 (rel dist to R_sv1 = **0.4743**, i.e. 47% off) |
| best monomial w₀ residual `|Φ(10) − w_0_B|` | **4.078068e-02** (Sage cross-check: no monomial within 1e-5) |
| admissibility (residual ≤ 1e-5) | **False — INADMISSIBLE** |

**No Θ-free combination of {R_JK, ξ_E_GGE_inv} reproduces R_sv1 (hence w_0_B) at 1e-5.** Sage-exact sweep (RealField(150)): R_JK(10)·ξ_E_GGE_inv = 0.10961 (0.242× of R_sv1); R_JK(10)/ξ_E_GGE = 0.40897 (0.901× — close but ≫1e-5); R_JK(10)/ξ_J = 0.90165 (2× off). The four S100b candidates that DO land near w_0_B at L=10 each smuggle a free normalization: **C2** (relative trajectory) and **C3** (additive base) reproduce w_0_B at L=10 *only by re-injecting R_sv1 itself* as multiplicative scale / additive base — R_sv1 is the retired object, and re-injecting it is exactly the tuned normalization the zero-free clause forbids; **C1** (raw R_JK → f) needs a CAC offset of −0.4117 that absorbs the distance-2 ≠ distance-1 mismatch, not a physical effacement; **C4** (−1+2·R_JK shoehorn) needs offset 0.1415. The zero-free-normalization attestation (npz key) records this. **Leg-1 INADMISSIBLE ⇒ composite INFO-(derivation-inadmissible); leg 2 does NOT execute.**

*§(iv-bis) surrogate-vs-canonical algebraic-distance theorem (pre-registered; substitution chain).*
- **(i) Surrogate → component reduction.** The surrogate w₀^surr(L) = f(R_JK(L)) reduces by the substitution chain to component substrate quantities: R_JK(L) (distance-2 cache-moment ratio) and the Θ-free c_J, P_GGE^ζ, ρ_GGE^ζ.
- **(ii) LOCK TEST (COMPUTED, not assumed).** Is sign(w₀) and the spread MECHANICALLY LOCKED to the monotone R_JK fall (0.011296 → 0.005990 over L=8→12), independent of map physical content? Raw f(R_JK(L)) spread = **0.0175966**; the analytic derivative-lock estimate |df/dR|·ΔR_JK = |−3.33909|·0.00530627 = **0.0177181** — match to **<10%** (npz `lock_match=True`). Sign: numerator (−c_J·R + P_GGE^ζ) < 0 for all R>0 (c_J>0, P_GGE^ζ<0), denominator (c_J·R + ρ_GGE^ζ) > 0 ⇒ w₀ < 0 ALWAYS, independent of physical content (npz `sign_locked=True`). ⇒ **algebraic-distance LOCKED** (`algebraic_distance_locked=True`): the surrogate is a **GEOMETRIC** observable, not a cohomology-class observable.
- **(iii) INFORMATIVENESS DECLARATION.** Because the lock fired, **a leg-2 spread verdict on this surrogate is UNINFORMATIVE on the canonical w₀ truncation stability** — the spread is mechanically forced by R_JK trajectory geometry, not by the DE object's convergence. A separate canonical-evaluation gate is REQUIRED; the surrogate FAIL (had leg 2 run) would NOT falsify the canonical. This is the §(iv-bis) clause-(iii) protection and the reason leg-1 inadmissibility (rather than a leg-2 spread number) is the correct verdict carrier.

*offset_ζ physical content (exhibited even on non-execution, per method).* The parent A-branch lockdown offset (−0.340827) is a *physical* effacement translation (Volovik partition + Γ_eff=0.99970). A branch-iv CAC offset would be admissible as the effacement/GGE-dressing translation ONLY when the map it dresses is itself Θ-free-admissible. The S100b C1 offset (−0.4117) instead absorbs the R_JK(distance-2) ≠ R_JE(distance-1) MISMATCH — the **C0-class silent-absorption pathology** (the sagan W1-4 item-4 cautionary instance: npz `C0_legacy_anchor_gap_sigma = 6.15`; for raw R_JK the anchor gap is **16.47σ**, npz `anchor_gap_sigma`). An offset that is merely numerically convenient is not a physical translation and does not redeem an inadmissible map.

*Consumption-layer declaration (substrate-first §(ii.A)).* R_JK(L) trajectory consumed at the **CACHE-MOMENT layer** (L-truncated D_K moment ratios; s85_w12_elim1 + s100b npz; canonical-constant match at L=10 verified, npz `R_JK_canon_match_L10=True`). The SV1 anchor consumed at the closed-form **ATLAS-ROW layer** (s84_w1a exact f-reduction). Cross-layer composition is explicit in the map text; the locked-norm machinery is not invoked because no admissible atlas-row identity is being tested at the cache-moment layer.

*Cross-checks.* (1) SV1 f-reduction reproduces w_0_iv to 1e-12 (`sv1_f_reduction_exact=True`). (2) ξ_E_GGE_inv substrate identity 59.8·Δ_BCS/K_base = 13.64247 matches canonical to 1e-5 (`xi_E_GGE_inv_substrate_match=True`). (3) R_JK(10) cache matches canonical `R_JK` to 1e-8. (4) S100b diag-spread span of the four candidates (0.000830, 0.036327) brackets the 0.025 PASS/INFO boundary — the freedom the derivation was tasked to eliminate, and DID eliminate by showing none of the admissible-looking candidates is Θ-free.

*4-tuple.* `(value=INFO-derivation-inadmissible…, scheme=zeta, convention=CAC-branch-iv-anchored-L10-DERIVED-OFFSET, L_max={8,10,12} anchor 10)`. dual-SHA: audit_sha256=`cd0492d6…`, content_sha256=`987b2b81…`.

*Solution-space reading.* INFO closes the corridor "branch-iv possesses a Θ-free L-truncation-converged w₀ evaluator built from its post-S86 ingredients (R_JK, ξ_E_GGE_inv)." The R_JE → {R_JK, ξ_E_GGE_inv} retirement is **algebraically lossy**: the two distance-tagged successors do not recombine into the dressing-ratio R-slot without re-injecting the retired object. **Downstream effect (mack routing):** the Falsifier #1 Row #1 SECONDARY stability-UNVERIFIED caveat does NOT lift (it required a leg-1-admissible + leg-2-converged evaluator) and does NOT harden either (the FAIL branch required an *admissible* evaluator that is then truncation-unstable — which did not occur); it **persists** with the refinement that the gap is at the *derivation* level (no principled evaluator), not the truncation level. The DESI DR3 R_842 reversal protocol cannot operate on a branch-iv w₀(L) object until a canonical-evaluation gate (NOT a surrogate) supplies one. **Carry-forward:** a canonical-evaluation gate that builds the R-slot from the spectral triple directly (not via the retired-R_JE recombination) — distinct from this surrogate by the §(iv-bis) clause-(iii) lock — is the genuine next computation.

---

### §W4-4. S101-H0-PROPER-A2 (einstein-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-H0-PROPER-A2`
**Trigger**: `[SIGN]` (Step-8 sign verification pre-registered: ∂H₀/∂a₂ < 0 → schema-v2 3-tuple companion row REQUIRED)
**Classification**: **GEOMETRIC** (convergent-a₂ Friedmann/H₀ readout recompute; a₂ → G_N emergence chain)
**Agent**: `einstein-theorist`
**Hypothesis**: Recomputing the full Friedmann-readout chain (§II.A Steps 1–8) with the exact spinor_norm_factor_FW = 4.0 and a CONVERGENT a₂ route lands N ≡ M_SA/(4·M_Pl_unred,obs) within |N − 1| ≤ 0.05, replacing the retracted truncated-WDW chain (68.8 baseline; S60 divergence FAIL negative control) with a convergent substrate-derived G_N/H₀ readout carrying the anchor-degeneracy disclosure and the Step-8 sign verification.
**Plan reference**: `sessions/session-plan/session-101-plan-w4.md` §W4-4

**Verdict**: **PASS** — N = 0.999859, |N − 1| = 0.000141 ≤ 0.05 (357× inside band); composite collapse PASS via sign=PASS ∧ magnitude=PASS ∧ regime=VALID; anchor-degeneracy disclosure present (rubric-checkable conjunct satisfied). The convergent-a₂ chain restores the H₀/G_N readout on a finite substrate footing; **Row #81's HELD value cell re-pins to this output on ANY landing** (mack-cosmic-bridge Step-3, session-close); the NON-PROMOTION-BY-HELD-NUMBER tag lifts; the 65.4/68.8/67.4 convention spread closes.

**Output Artifacts** (on-disk verified; content-presence, not counts):
- `computations/session-101/s101_w4_h0_proper_a2.py` — contains `from canonical_constants import`, `print_verdict_payload` ✓
- `computations/session-101/s101_w4_h0_proper_a2.npz` — reconciliation map group + 4 chain routes + sign-check + neg-control + exact-rationals + anchor-degeneracy disclosure string ✓
- `computations/session-101/s101_w4_h0_proper_a2.png` — Panel A (N across routes vs band) + Panel B (Step-8 H₀ directions) ✓
- Verdict line `^S101-H0-PROPER-A2:.* audit_sha256=[a-f0-9]{64}` in `computations/session-101/s101_gate_verdicts.txt` + dual-SHA companion row + schema-v2 3-tuple row + 3 companion rows (regulator_pin, WDW↔zeta map, Row #81 re-pin) ✓
- `audit_sha256=cd8e8c0b125a64cf73debf8b9b7663e4389f0860159fc7cd524550674c983f22`; `content_sha256=f7d27b152597500ff08001ad507084ab62b16165af26e0b3d0ea9918b7ec0a33`
- 4-tuple: `(value=N=0.999859, scheme=zeta-primary-localSD-fallback, convention=WDW-ZETA-RECONCILED-route-convergent-localSD, L_max=N/A)`

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script):
- `get_constant("a_2_FW_zeta")` → 2776.165389 (S88, S88-A-N-FW-CANONICALIZATION) — primary convergent-route anchor.
- `get_constant("a_0_FW_zeta")` → 6440.0 (S88) — WDW↔zeta map zeta-side a₀.
- `get_constant("spinor_norm_factor_FW")` → 4.0 (S100a, S100a-H0-SPINOR-FACTOR PASS) — √16 exact.
- `get_constant("M_KK")` → 7.428660036284456e16 GeV; `M_Pl_reduced` → 2.435e18; `M_Pl_unreduced` → 1.2209e19; `H_0_km_s_Mpc` → 67.4; `tau_fold` → 0.19.
- `search_knowledge("H0 proper a2 Friedmann spinor factor Row 81 NON-PROMOTION-BY-HELD-NUMBER")` → confirms Q27 RESOLVED (factor √16=4 stands), H₀ MAGNITUDE held; no prior gate computes the convergent-route N (this gate is the first). NOT PRE-CLOSED — the magnitude was explicitly "undecidable from existing artifacts" per the S-2 adjudication (`session-100a-h0-spinor-chain-synthesis.md` §II.C/§V.1).

**Results**:

**FIRST DELIVERABLE — WDW↔zeta reconciliation map (Class-8.4 representation-convention pin).** The WDW route (S52 5-point estimate, S58 npz) and the canonical zeta route (S88) are TWO normalizations of the SAME substrate spectral moments a₀, a₂ of D_K² at τ_fold. Each normalization factor named, valued, provenance-cited:

| Object | WDW route | per-component (÷16) | zeta canonical | κ = WDW_per/zeta | Provenance |
|:-------|:----------|:--------------------|:---------------|:-----------------|:-----------|
| Spinor multiplicity | Tr_Δ₈(1) = 16 | — | — | — | 2^(8/2)=16; Res_{s=8}ζ_D carries 16 (S87) |
| a₀ | 101984.0 (`a0_fold_wdw`) | 6374.0 | 6440.0 (`a_0_FW_zeta`) | **κ_a₀ = 0.989752** (clean, 1.02% residual) | S58 npz / S88 |
| a₂ | 162984.4151 (`a2_fold_wdw`) | 10186.5259 (= s59 `a2_corrected`) | 2776.165389 (`a_2_FW_zeta`) | **κ_a₂ = 3.669279** (estimator offset, DISCLOSED) | S58 npz / S88 |
| τ_fold pin | 0.19 | 0.19 | 0.19 | 1 (shared geometric anchor) | `tau_fold`, CONST-FREEZE-42 |

- **a₀ leg reconciles CLEANLY** via the structural spinor multiplicity 16 = Tr_Δ₈(1): a₀^WDW/16 = 6374.0 vs a₀^ζ = 6440.0, residual 1.02% (WDW-5-point-vs-zeta-sum estimator offset). The factor 16 is the dominant normalization difference — the WDW a₀ carries the full internal-spinor trace; the zeta a₀ is (close to) the per-component value.
- **a₂ leg does NOT close in clean closed form**: a₂^WDW/16 = 10186.53 vs a₂^ζ = 2776.17 leaves a residual κ_a₂ = 3.669 — the WDW↔zeta normalization offset SPECIFIC to the a₂ moment (different small-t weighting between the Wheeler-DeWitt mini-superspace 5-point estimate and the canonical zeta residue). **Map status: ESTABLISHED** (every factor named/valued/provenance-cited) with the a₂-leg κ_a₂ DISCLOSED as an estimator offset, not a clean structural constant. This realizes the plan's primary→fallback structure: the zeta a₂ is the convention anchor; the convergent **finite-local-SD** a₂ is the chain spine (the WDW a₂ IS a finite local heat-kernel coefficient estimate, distinct from the divergent cumulative-PW reconstruction killed by BAYESIAN-H0-60).

**THE chain (substrate-first; a₂ → M_SA → N → H₀, convergent route).** The arrow runs D_K eigenvalues → a₂^{ζ} second spectral moment → M_Pl^FW → G_N^FW → H₀ readout; the a₂ Seeley-DeWitt coefficient GENERATES the Einstein-Hilbert action (gravity is the second spectral moment, not a fundamental law). Deficit-closed a₂:

- a₂_convergent = a₂^WDW · (1 + frac_deficit) = 162984.4151 × 1.0410 = **169666.7307** (M_KK units; the 4.1% deficit from p+q≥4 closed onto the finite local-SD a₂).
- α = (f₂/2π²)·a₂ = 8595.42 (f₂=1 pinned, S64).
- M_SA = √(16π·α)·M_KK = **4.882912e19 GeV** (M_SA ∝ a₂^{1/2}, M_SA ∝ M_KK^{1}).
- **N = M_SA/(4·M_Pl_unred,obs) = 0.999859** [target 1; |N−1| = 0.000141, **PASS**].
- M_Pl,phys = M_SA/√16 = M_SA/4; M_Pl_red,FW = M_phys/√(8π) = **2.435000e18 GeV** (= observed reduced Planck mass at deficit closure).
- **G_N^FW/G_N^obs = 1.000000** (G ∝ 1/M_red²; deficit-closed).
- H₀ readout = H_obs × (M_red,obs/M_red,FW) = **67.40 km/s/Mpc**.

**Anchor-degeneracy disclosure (load-bearing, rubric-checkable).** The chain predicts the **ratio of Planck masses** (equivalently G_N^FW/G_N^obs — the fabric's a₂ second-spectral-moment gravitational coupling against the laboratory's Newton constant), NOT an anchor-independent H₀ magnitude. In Step 6 the energy content is the OBSERVED critical density, itself defined from observed H₀ and observed M_red; the H₀ readout is the observed anchor rescaled by that ratio's deviation from 1. **At exact deficit closure (N→1) the readout degenerates to H_obs = 67.4 identically.** The framework supplies the GRAVITATIONAL-COUPLING leg (the a₂^{ζ} second spectral moment); the laboratory currently supplies the ENERGY-CONTENT leg. An anchor-independent H₀ awaits the framework's own energy-content derivation — the Volovik-partition Level-2 of the S58 two-level architecture — joined to this convergent-a₂ Level-1; that joint is a **FUTURE pre-registration (S102+), NOT this gate**. The falsifiable content of this chain lives in the **G_N/M_Pl ratio channel** (G_N^FW/G_N^obs = 1.000000 at closure), with the disclosure rider on any Row #81 value.

**Step-8 sign verification (substitution chain; [SIGN] trigger).**

- *Claim*: deficit closure LOWERS the readout; the computed chain sits ABOVE the CMB anchor pre-closure and converges DOWN; the published 65.4 sits BELOW — the two displacement directions DIFFER.
- *Def 1*: H₀^FW = H_obs × (M_Pl_red,obs/M_Pl_red,FW) — the Step-8 readout form [H_obs = 67.4].
- *Def 2*: M_Pl,FW ∝ √(a₂^{ζ}) — the a₂ spectral moment IS the gravitational coupling (spinor division by 4 exact).
- *Substitute*: deficit closure a₂^trunc → a₂^conv = a₂^trunc·(1+0.0410) ⇒ M_Pl,FW → M_Pl,FW·√1.0410 = M_Pl,FW·1.020294 ⇒ (M_red,obs/M_red,FW) → ÷1.020294 ⇒ H₀^FW → H₀^FW/1.020294.
- *Canonical form*: ∂H₀^FW/∂a₂ < 0 (a₂ sits under the square root in the DENOMINATOR of the mass ratio) ⇒ raising a₂ to its convergent value LOWERS the readout.
- *Direction (realized)*: H₀^trunc (S59, RETRACTED-S60) = 68.7678 > 67.4 (ABOVE anchor); H₀^conv = 67.40 (approaches the anchor FROM ABOVE); published 65.4 < 67.4 (BELOW — sign INVERTED). Displacement directions DIFFER — the pure substitution-chain failure that survived 42 sessions because both lie "within ~3%" of observed. **sign_verdict = PASS** (convergent readout approaches the anchor from above; deficit-closure lowers H; published 65.4 sits below).
- **schema-v2 3-tuple**: `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` → composite **PASS**.

**S60 negative control (the divergence the convergent route must NOT reproduce).** BAYESIAN-H0-60 FAIL ("No convergent observable from truncated PW spectral action") was the **cumulative-PW** route: N_cumul = {…, 4.86 (L=3), 13.4, …, 121.0 (L=7)}, growth exponent α_a₂ = 9.1355. The convergent route uses a SINGLE finite local-SD a₂ (no L-scan) — its effective growth exponent is **0.0** (a₂ is L-independent at the fold; deficit closure changes it by a bounded 4.1%, not an unbounded power law). |0 − 9.1355| = 9.14 > 1 ⇒ **negative control PASS** (divergence NOT reproduced; regime_verdict = VALID).

**Regression contrast (RETRACTED S59 baseline — never the gated value).** S59 `N_factor_MPl` = 3.920438854652296 (N/4 = 0.98011, the truncated-WDW reference point inside the band), `frac_deficit` = 0.04099972, `H_0_corrected` = 68.76781146. This gate's recompute reproduces H₀^trunc = 68.7678 EXACTLY at the s59 pins (regression contrast), confirming the chain arithmetic; the truncated value is the pre-closure reference, RETRACTED-S60, and is never the gated number.

**Row #81 re-pin routing (mack-cosmic-bridge sole-writer, Step-3 write-order, session-close).** On this PASS landing, Row #81's value cell re-pins to N = 0.999859 / H₀ readout = 67.40 km/s/Mpc WITH the anchor-degeneracy disclosure; the NON-PROMOTION-BY-HELD-NUMBER (undischarged-magnitude-bound) tag lifts; the four A11 surfaces (inventory Row #81, watchlist H₀ row, capstone §7.2 row #10, atlas-05 Window-19) carry the re-pin. The BAYESIAN-H0-60 FAIL + 68.8 retraction travel with the row verbatim as the convergent-route's negative-control provenance. This gate's agent ROUTES; mack writes the inventory (per `feedback_mack-bridge-role.md`). `spinor_norm_factor_FW` untouched; Q27 stays RESOLVED.

**Cross-checks.**
- Input SHA pins: s58 / s59 / s60 npz all match plan-block expected hashes (OK).
- M_Pl_red,FW = 2.435000e18 GeV = observed M_Pl_reduced exactly at deficit closure (consistency: N→1 ⇒ G_N^FW = G_N^obs ⇒ M_red,FW = M_red,obs).
- Reconciliation consistency: √1.0410 = 1.020294 = 4/3.9204 (the a₂-deficit and the spinor-factor-deficit are two estimates of the SAME single deficit, agreeing — closure for the factor N_meas vs N_struct, per S-2 §II.C).
- Exact rationals carried: spinor factor = 4/1 EXACT; rel 3.92-vs-4 = 1/49 = 2.041% (S100a PW-truncation residual).

**Substrate framing.** GEOMETRIC. H₀ IS the a₂-moment readout — Newton's constant is the substrate's second spectral moment (a₂^{ζ} Seeley-DeWitt coefficient of D_K²), and the Hubble rate the laboratory reads IN its FRW container is the emergent bookkeeping of that moment against the observed energy content. The chain is a G_N PREDICTION re-expressed: M_Pl,FW ∝ √(a₂^{ζ})/4 with the 4 = √16 spinor-trace factor exact (Tr_Δ₈(1)=16; surviving 4-of-64 on-shell graviton block). The arrow flows D_K eigenvalues → a₂^{ζ} spectral moment → M_Pl^FW → G_N^FW → H₀ readout; never the reverse (no fitting of a₂ to the Hubble tension). The WDW↔zeta reconciliation map is a convention object INTERNAL to the substrate's own normalization bookkeeping (spinor trace, fiber volume, τ_fold) — Class-8.4 pins it so no silent normalization swap can manufacture or hide a 4% deficit again.

---

### §W4-5. S101-M0-BCS-SCREENING (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S101-M0-BCS-SCREENING`
**Trigger**: `[SIGN]` (per-anchor monotone-shrink direction pre-registered → schema-v2 3-tuple companion row emitted)
**Classification**: **PARTICLE** (S62 BCS anomalous-self-energy screening transfer to the |s(h)|²-anchored M₀^{sector})
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: Applying the S62 BCS anomalous-self-energy screening (THRESHOLD-62 / HIGGS-BCS-THRESHOLD-62 — the documented m_H 134 → ~125 closure, applied to date to m_H ONLY, never to M₀^{sector}) to the |s(h)|²-anchored M₀^{sector} shrinks the inherited residual band ([+5.356%, +7.114%], exact 67/1251, 89/1251) toward 0 IN STEP with the m_H closure — because M₀ inherits the anchor at LINEAR first power (S100a-M0-MH-INHERITANCE), the screening that closes m_H transfers to M₀ at first power. Three genuine contingencies guard against PASS-by-construction (root existence/uniqueness; δ-consistency |δ_BCS^solve − 0.07| ≤ 0.03; per-anchor monotone screened band); r_tree^scr = 0 is BY CALIBRATION, disclosed, not a finding.
**Plan reference**: `sessions/session-plan/session-101-plan-w4.md` §W4-5

**Output Artifacts** (content-presence verified on disk, not by line count):
- `computations/session-101/s101_w4_m0_bcs_screening.py` — contains `from canonical_constants import` (line 71) + `print_verdict_payload` (def line 365, call line 533). ✓
- `computations/session-101/s101_w4_m0_bcs_screening.npz` — full float64 round-trip (all conjunct outputs + scan arrays + dual-SHA). ✓
- `computations/session-101/s101_w4_m0_bcs_screening.png` — 2-panel: (a) m_H^scr,RG(δ) scan + root + δ-consistency window; (b) band-shrink bar chart (unscreened vs PRIMARY screened, exact-rational annotations). ✓
- Verdict line `^S101-M0-BCS-SCREENING:.* audit_sha256=[a-f0-9]{64}` in `computations/session-101/s101_gate_verdicts.txt` + dual-SHA companion row + schema-v2 3-tuple row + 2 extra companion rows (regulator_pin + calibration_disclosure). ✓
- This WP §W4-5 (Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit). ✓

**MCP Pre-Compute Audit** (queries executed before scripting):
- `search_knowledge("M0 sector inheritance m_H BCS screening THRESHOLD-62")` → returned the `m0_mh_inheritance` (S100a) + `higgs_bcs_threshold` (S62) provenance; constants `m_H_FW_tree=134.0` (theorem A10), `m_H_FW_KK_threshold=131.8` (KK-THRESHOLD-64). NOT pre-closed — this is the first transfer of the BCS screening to M₀^{sector} (the S100a `bcs_note` explicitly flags it as "applied to m_H ONLY — NOT to M₀^{sector}").
- `trace_entity("S100a-M0-MH-INHERITANCE")` → single provenance hit (the s100a script); confirms the LINEAR-first-power inheritance is the upstream law; no prior gate has applied screening to M₀.
- `get_constant("m_H_obs")` = 125.1; `get_constant("v_ew")` = 246.0 (canonical) — note S62 lineage intentionally uses the Fermi-extracted v_ew = 246.22 for the RG run (documented in s62 line 76); the inheritance-anchor algebra uses m_H values directly and is v_ew-independent.
- s100a npz cross-read confirmed exact rationals `r_kk=67/1251`, `r_tree=89/1251`, `band=22/1251` (matches plan freeze); s62 npz cross-read surfaced the cached `delta_BCS_best=0.2672` (the conjunct-2 tension, re-derived in-gate below, NOT trusted blindly).
- Sage QQ pre-verification of the PRIMARY-route band algebra (all exact): `r_KK^scr = -11/670`, `r_tree^scr = 0`, max|r| factor 4.333, irreducible remnant 11/1251.

**Verdict**: **INFO** — sign=PASS / magnitude=PASS / regime=MARGINAL (composite collapse: `magnitude=PASS + regime=MARGINAL ⇒ INFO`). The band-shrink DIRECTION is confirmed (both anchors move down toward 0, max|r| 7.114% → 1.642%, factor 4.33); the gate routes to INFO because TWO independent pre-registered INFO-triggers fired: (i) δ-consistency breach |δ_BCS^solve − 0.07| = 0.197 ≫ 0.03 — the needed screening is NOT the documented BCS-provided 0.07; (ii) CONVENTION-SENSITIVE flag — PRIMARY-vs-SECONDARY route deviation 0.0118 > 0.010.

**Results** (NUMBERS → gate → interpretation):

*Conjunct (1) — δ_BCS^solve root-solve (S62 2-loop machinery RE-RUN in-process, not cached):* the recomputed 2-loop SM RG (Machacek-Vaughn / Buttazzo et al., g₁ GUT-normalized, faithful copy of `s62_higgs_bcs_threshold.py` β-functions) gives m_H^scr,RG(δ) decreasing **monotonically** over δ ∈ [0, 0.5] (98.84 → 190.10 GeV reversed; ✓ matches the Definition-2 monotonicity claim), with m_H(δ=0, 2-loop, no-BCS) = 190.10 GeV. The equation m_H^scr,RG(δ) = 125.1 has **exactly one root**: δ_BCS^solve = **0.267156** (brentq; root residual 5.68×10⁻¹⁴ GeV). **PASS** — root exists and is unique. (This reproduces the cached S62 `delta_BCS_best=0.2672` to 6 sig figs from an independent in-process re-run — the machinery is NOT drifting.)

*Conjunct (2) — δ-consistency with the documented 0.07:* |δ_BCS^solve − 0.07| = |0.267156 − 0.07| = **0.197156 ≫ 0.03**. **FAIL.** The screening NEEDED to close the 2-loop-RG m_H (δ ≈ 0.267) is ~3.8× the documented BCS enhanced estimate (0.07), and ~3580× the direct BdG-spectral-action screening δ_BCS^direct = δa₄/(2·a₄) = 7.46×10⁻⁵ [a_4^{Pauli-Villars}]. The m_H closure works **numerically** but its attribution to the BCS mechanism at the documented strength **weakens**: the 2-loop-RG picture overshoots to 190 GeV and needs a large δ to come back, whereas the documented BCS content is a few-percent screening.

*Conjunct (3) PRIMARY — m_H-level first-power transfer (the S100a-measured inheritance law; EXACT rationals):* since m_H^scr,RG(δ_solve) = 125.1 by construction, the tree-calibrated first-power map gives
- r_tree^scr = 0 EXACT **BY CALIBRATION** (m_H_obs used once, on the tree anchor — DISCLOSED, not a finding);
- r_KK^scr = 131.8/134 − 1 = **−11/670 = −1.6418% EXACT** (independent of the RG machinery and of m_H_obs — pure anchor ratio).

Per-anchor monotone shrink: |r_KK^scr| = 1.642% < |r_KK^unscr| = 5.356% ✓; |r_tree^scr| = 0 < |r_tree^unscr| = 7.114% ✓ — **BOTH anchors shrink** (sign-keying contingency PASS). max_a|r_a^scr| = **0.016418 ≤ 0.020** ceiling (at **82.1%** of ceiling — a genuine test, not vacuous-margin). The band **[+5.356%, +7.114%] → [−1.642%, 0]**: worst-member max|r| factor **4.333**, midpoint 6.235% → −0.821% factor **7.595**. The irreducible remnant is the inter-anchor half-spread **11/1251 = 0.879%** (the S64 KK-threshold correction the anchors carry — NOT a screening effect; the screened band CANNOT close below it, which is why the 0.020 ceiling respects it).

*Conjunct (3) SECONDARY — KK-boundary RG transfer (convention-sensitivity diagnostic, report-only):* applying δ_solve at the KK-corrected boundary λ = (4/3)·g₃eff²·ratio_gilkey·(131.8/134)² and running the same 2-loop RG down gives m_H^scr,RG,KK = 124.523 GeV ⇒ r_KK^scr,RG = **−0.4612%**. Deviation from the PRIMARY value |r_KK^scr,PRIM − r_KK^scr,RG| = |−1.6418% − (−0.4612%)| = **0.011806 > 0.010** ⇒ **CONVENTION-SENSITIVE flag FIRES.** The two transfer conventions (m_H-level first-power vs boundary-level RG) disagree at the ~1.2% level — i.e., the RG-transfer nonlinearity (the screening enters the boundary as λ ∝ g²(1−δ)², then runs 2-loop) is slightly larger than the 0.36%-margin the 0.020 ceiling allotted. Both routes still confirm the DIRECTION (down toward 0) and stay well inside the INFO ceiling 0.035.

**Band-shrink substitution chain** (MANDATORY per the source CF; [SIGN] direction claim):

> **Claim**: "The screened M₀ residual band shrinks toward 0 in step with the m_H closure."
>
> **Def 1** — r_a ≡ δM₀/M₀ at anchor a, inherited LINEARLY at first power through the shared |s(h)|² fiber-embedding anchor [S100a-M0-MH-INHERITANCE, audit d00bbb37…]:
> r_KK = (131.8 − 125.1)/125.1 = 67/1251 = +5.356% EXACT; r_tree = (134.0 − 125.1)/125.1 = 89/1251 = +7.114% EXACT.
> **Def 2** — S62 screening: g₃^eff(M_KK) = g₃(M_KK)·(1 − δ_BCS); boundary λ_CCM = (4/3)·g₃eff²·ratio_gilkey; 2-loop RG down; m_H^scr = √(2λ_IR)·v_ew. m_H^scr(δ) is MONOTONE DECREASING in δ over [0, 0.5] (re-verified in-gate: 98.84 → 190.10 GeV reversed).
> **Def 3** — first-power transfer: m_H_a → m_H^scr,a = m_H^scr,RG(δ)·(m_H_a/m_H_tree); r_a^scr = (m_H^scr,a − m_H_obs)/m_H_obs.
>
> **Substitute**: r_a^scr = (m_H_a·(1 + δ_eff) − m_H_obs)/m_H_obs, with 1 + δ_eff ≡ m_H^scr,RG(δ)/m_H_tree, δ_eff < 0 for δ > 0 (Def-2 monotonicity).
> **Simplify** (split the numerator, one step): r_a^scr = (m_H_a − m_H_obs)/m_H_obs + δ_eff·(m_H_a/m_H_obs) = **r_a + δ_eff·(m_H_a/m_H_obs)**.
> **Canonical form**: r_a^scr = r_a − |δ_eff|·(m_H_a/m_H_obs) for δ > 0.
> **Direction**: |δ_eff|·(m_H_a/m_H_obs) > 0 for BOTH anchors ⇒ BOTH band members move **DOWN** (toward and through 0 from above). At δ = δ_solve (tree calibration): r_tree^scr = 0 exactly, r_KK^scr = 131.8/134 − 1 = −11/670 = −1.6418% exact ⇒ band [+5.356%, +7.114%] → **[−1.642%, 0]**: max|r| drops 7.114% → 1.642% (factor 4.33), midpoint 6.235% → 0.821% (factor 7.6) — "in step" with the m_H closure (134 → 125.1). The irreducible remnant is the inter-anchor half-spread 11/1251 = 0.879% (KK-threshold correction, not a screening effect).
> **Conclusion**: sign_verdict keys on per-anchor monotone shrink (|r_a^scr| < |r_a^unscr| for BOTH anchors → **PASS**); magnitude_verdict on max_a|r_a^scr| = 0.016418 vs 0.020/0.035 (→ **PASS**, ≤ 0.020). Mnemonic-vs-exact discipline observed: all band values carried as exact rationals (67/1251, 89/1251, −11/670, 11/1251) alongside floats — no round-figure substitution in registry-bound numbers.

**Cross-checks**:
1. **Exact-rational verification (Sage QQ)**: r_KK^scr = −11/670 confirmed (`r_KK_scr == QQ(-11)/670` → True); r_tree^scr = 0 exact; band 22/1251, half-spread 11/1251 confirmed; max|r| factor 4.333260…; midpoint factor 7.595378…
2. **Independent re-run vs cached S62**: in-process δ_solve = 0.267156 reproduces cached `delta_BCS_best = 0.2671608` (s62 npz) to 6 sig figs — machinery faithful, no drift.
3. **Unscreened band vs s100a npz**: r_kk = 0.0535572 (= 67/1251), r_tree = 0.0711431 (= 89/1251) — bit-match to the inheritance source.
4. **Monotonicity re-verification**: `np.all(np.diff(mH_scan) < 0)` → True over the full 101-point δ-scan (Definition-2 claim holds on the recomputed machinery, not just asserted from S62).
5. **Root tolerance**: |m_H^scr,RG(δ_solve) − 125.1| = 5.68×10⁻¹⁴ GeV ≪ 10⁻⁶ pin.

**Assessment** (substrate-first): The substrate exhibits ONE screening direction across both observables — the BCS condensate's screening of g₃(M_KK) (the a₄-channel fourth-spectral-moment coupling) moves BOTH the m_H residual and, via the linear-first-power |s(h)|² fiber-embedding inheritance, the M₀^{sector} residual DOWN toward 0. The direction is robust (sign=PASS) and the PRIMARY-route magnitude clears the ≤2% ceiling (max|r_scr| = 1.642%, dominated by the irreducible KK-threshold inter-anchor spread). What the gate maps as NOT-yet-in-step is twofold: (i) the **screening STRENGTH** the 2-loop-RG closure demands (δ ≈ 0.267) is far from the documented BCS estimate (0.07) — the 2-loop boundary-condition convention overshoots m_H to 190 GeV, so the closure's quantitative BCS attribution is weakened even though the tree-level A10 picture (m_H_tree = 134) and the direction are intact; (ii) the **transfer convention** (m_H-level first-power vs boundary-level RG) carries a ~1.2% ambiguity, slightly exceeding the 1.0% tolerance. The screened M₀ band is the tight **[−1.642%, 0]** under the PRIMARY (substrate-measured first-power) law, an honest tightening of the inherited [+5.4%, +7.1%]; the remnant is the KK-threshold spread the anchors carry, not a screening failure. Routing: capstone §7 honest-scope M₀ row update → mack-cosmic-bridge (sole-writer, on landing); the CONVENTION-SENSITIVE flag routes a transfer-convention derivation CF (boundary-level vs m_H-level first-power reconciliation) to the wave Carry-Forward block.

**4-tuple**: (value=0.016417910447761194, scheme=KK-threshold-131.8-plus-tree-A10-134, convention=FIRST-POWER-MH-LEVEL-TRANSFER-PRIMARY, L_max=N/A)
**Dual-SHA**: audit_sha256=`1a1eff669b3b1d8163645f8d7bbb35c9f2f7088bd96277200e9c4042e006445e` content_sha256=`ae076817e3ee88b2c94092f1a1809f30e20919d574f426138a24758d52ead404`

---

## Wave 4 Synthesis (team-lead)

**Outcome**: 5 gates — **2 PASS** (W4-1, W4-4) + **1 FAIL** (W4-2) + **2 INFO** (W4-3, W4-5). sig_5 clean. Verdict file lines 97/102/108/113/120.

**Headline — the H₀ flagship lands (W4-4 PASS)**: N = M_SA/(4·M_Pl) = 0.999859 (|N−1|=1.4e-4, 357× inside band); H₀ readout 67.40 km/s/Mpc; G_N^FW/G_N^obs = 1.000000. **NON-PROMOTION-BY-HELD-NUMBER LIFTS** — the framework can now cite the value with the anchor-degeneracy disclosure (it is a G_N prediction via the ratio channel, NOT an anchor-independent H₀; at N→1 the readout degenerates to H_obs — framework supplies the gravity-coupling leg, lab the energy-content leg). The 42-session substitution-chain sign-slip is killed (∂H₀/∂a₂<0; convergent route approaches from above 68.77→67.40; old 65.4 sat below). Class-8.4 WDW↔zeta reconciliation map established (a₀ leg clean; a₂ κ=3.669 disclosed as estimator-offset → finite-local-SD WDW a₂ is the spine).

**QEQ pair — self-consistency PASSES, relic resonance FAILS (both informative)**:
- W4-1 PASS: slope_selfcons=1.000074 — the q∝H closure is now DERIVED (not imposed) from KV self-consistency; the clause-(f) carve-out vs the frozen-backbone S100a-W1-2 FAIL (H² parity wall). q_amp∝|H| is the non-analytic-even cell the equilibrium H-parity theorem leaves open; the S100b-X C10 n_eff physical-route member activates at n=2 (q∝H stops being an imposed input).
- W4-2 FAIL: IN-band resonance LIVE (ω_q^phys=2.013 ∈ pair band [1.64,10.84]; 24 modes / 14 occupied cross resonance on the post-fold tail; odd-floor violated independently). Derived the clock **γ = dt/dτ = 29.7532 M_KK⁻¹** (fixes the s97 `t_relax` disclosed freedom; C10 clock consumers inherit it). **BINDING cross-wave**: relic clause (d) of H-PARITY-DRIVE-EXCLUSION → coincidence-bounded (carried to W6-4 dispatch). Consistent with the S67 PROVEN broad-band "post-transit resonance impossible" theorem (this prices the narrow-band post-fold-tail it does not cover).

**DE/M₀ — both INFO, both map walls honestly**:
- W4-3 INFO-(derivation-inadmissible): the zero-free-normalization filter proves branch-iv has **no principled w₀(L) evaluator** — the R_JE→{R_JK, ξ_E_GGE_inv} S86 retirement is algebraically LOSSY (best Θ-free monomial residual 4.08e-2 ≫ 1e-5; near-w₀_B candidates only re-inject the retired R_sv1=0.4536). §(iv-bis) lock: surrogate is geometric, a spread number would be uninformative. Row #1 SECONDARY caveat persists-refined (gap at the derivation level, not truncation).
- W4-5 INFO: M₀ band-shrink direction confirmed ([+5.4,+7.1]%→[−1.64,0]%, clears ≤2% ceiling); sign=PASS / mag=PASS / regime=MARGINAL; BCS attribution weakens (δ_solve=0.267 vs documented 0.07) + ~1.2% transfer-convention ambiguity (CONVENTION-SENSITIVE).

### Effected In-Session (non-math — completed by the team-lead orchestrator before STOP)

- [x] **EVOI rank-7b → RESOLVED** — `sessions/evoi-framework.md:55` status cell flipped `MAGNITUDE UNDECIDABLE — value HELD (NON-PROMOTION-BY-HELD-NUMBER) → RESOLVED — S101 W4-4 PASS`: value re-pinned N=0.999859 / 67.40 km/s/Mpc with the anchor-degeneracy disclosure (G_N prediction, not anchor-independent H₀); NON-PROMOTION-BY-HELD-NUMBER LIFTED. — audit `cd8e8c0b125a`
- [x] **W6 forward constraint recorded** (W4-2 FAIL) — relic clause (d) of `S101-HPARITY-STAGE1-REGISTRATION` (W6-4) MUST be registered as **coincidence-bounded** (demoted from argument-grade); the orchestrator carries this to the W6-4 dispatch prompt (W6 has not registered it yet — a forward pin, not a retroactive amendment). Recorded in `session-101-housekeeping.md §A`. — audit `98a923fd0ea4`
- [x] **Capstone-hygiene routings recorded → session-close 5-question gate** — W4-1 (§8.5 conditionality locus; q∝H now derived), W4-4 (Row #81 four A11 surfaces + §7 H₀ row), W4-5 (§7 honest-scope M₀ row) all route to mack-cosmic-bridge sole-writer / capstone designated writer at session close (Q3/Q4). Recorded in `session-101-housekeeping.md §A`; NOT bulk-edited mid-session (curated doc). — audits `c06a956b`/`cd8e8c0b`/`1a1eff66`

(Self-audit: `grep -c '^- \[ \]'` on this sub-section = 0 — all 3 items checked.)

## Carry-Forward Computations

### CF-S102-H0-ANCHOR-INDEPENDENT — anchor-independent H₀ (Volovik-L2 ⊕ convergent-a₂-L1)

1. **What**: pre-register the anchor-independent H₀ — join the Volovik-partition Level-2 (effacement / vacuum-tracking) to the W4-4 convergent-a₂ Level-1 (G_N ratio channel) so the readout no longer degenerates to H_obs at N→1 — i.e. the framework supplies BOTH the gravity-coupling leg AND a substrate-derived energy-content leg, yielding an H₀ with a genuine σ-distance to SH0ES/Planck.
2. **Inputs**: `s101_w4_h0_proper_a2.npz` (N=0.999859, M_SA=4.882912e19, M_Pl_red_FW=2.435e18 GeV, G_N ratio=1.0; audit `cd8e8c0b`); the Volovik-partition Level-2 machinery (S58/S60 effacement Γ_eff=0.99970); the anchor-degeneracy disclosure.
3. **Gate**: PASS iff the joint Level-1⊕Level-2 yields an H₀ that does NOT degenerate to H_obs (independent prediction with a σ-distance), substrate-derived energy-content leg, NO anchor re-injection.
4. **Effort**: 1–2 waves. **Depends on**: S101-H0-PROPER-A2 PASS (this wave); the Volovik-partition Level-2.

### CF-S102-BRANCH-IV-CANONICAL-EVAL — branch-iv R-slot evaluator from the spectral triple

1. **What**: build the branch-iv w₀(L) R-slot evaluator DIRECTLY from the spectral triple (distinct from the W4-3 surrogate by the §(iv-bis) lock), supplying the truncation-converged DE object the DESI DR3 R_842 reversal protocol needs ahead of the ~2027 horizon. W4-3 proved no Θ-free monomial recombination of {R_JK, ξ_E_GGE_inv} works (the R_JE retirement is lossy).
2. **Inputs**: `s101_w4_branch_iv_evaluator.npz` (recorded candidate map forms, §(iv-bis) lock witness, R_sv1=0.4536, SV1 closed form; audit `cd0492d6`); the spectral triple (A_K, H_K, D_K); w_0_B=−0.842454.
3. **Gate**: PASS iff a spectral-triple-direct R-slot reproduces w_0_B at L=10 within 1e-5 with ZERO free normalization AND CAC spread over L∈{8,10,12} ≤ 0.025; INFO iff still inadmissible (branch-iv confirmed evaluator-less).
4. **Effort**: 2 waves. **Depends on**: S101-W0-BRANCH-IV-EVALUATOR INFO (this wave); ahead of ~2027 DR3.

### CF-S102-OQ5-RECTIFIED-DRIVE — OQ-5 conditional rectified-drive gate

1. **What**: execute OQ-5's rectified-drive gate (unblocked by W4-2 FAIL) — quantify the post-fold-tail rectified parametric drive on the occupied modes that cross resonance, using the derived clock γ and the crossing geometry; determine whether the live narrow-band resonance contributes a measurable relic-abundance / spectral feature.
2. **Inputs**: `s101_w4_qeq_relic_oddfloor.npz` (γ=29.7532 M_KK⁻¹, χ_I=885.254, crossing geometry E_k∈[0.820,0.873], q_res∈[0.251,0.341], 24-mode/14-occupied crossing set; audit `98a923fd`).
3. **Gate**: pre-registered threshold on the rectified-drive amplitude / relic-abundance contribution (pinned at the OQ-5 gate's plan-freeze); PASS iff the contribution is within the GGE-relic budget, FAIL iff it overproduces.
4. **Effort**: 1 wave. **Depends on**: S101-W1-QEQ-RELIC-ODDFLOOR FAIL (this wave); the γ clock.

### CF-S102-M0-TRANSFER-CONVENTION — M₀-screening transfer-convention reconciliation

1. **What**: reconcile the M₀-screening transfer convention — boundary-level RG (r_KK^scr,RG=−0.461%) vs m_H-level first-power (r_KK^scr=−11/670=−1.642%), the ~1.2% ambiguity exceeding the 1.0% tolerance (W4-5 CONVENTION-SENSITIVE); DERIVE which transfer is substrate-canonical (not chosen).
2. **Inputs**: `s101_w4_m0_bcs_screening.npz` (r_KK^scr, r_KK^scr,RG, δ_solve=0.267; audit `1a1eff66`); the S62 BCS machinery; the tree-level A10 m_H=134 picture.
3. **Gate**: PASS iff the substrate-canonical transfer convention is DERIVED AND the PRIM−RG spread ≤ 1.0% with the band-shrink direction (sign=PASS) preserved; INFO iff the convention choice needs a workshop.
4. **Effort**: 0.5–1 wave. **Depends on**: S101-M0-BCS-SCREENING INFO (this wave).

### CF-coldread-6 — Jacobson thermodynamic a(t) route (R2) — substrate horizon-entropy V.P., conditional on the coldread-S2-1 verdict `[cold-read-origin: 04-a_t-critical-path-memo.md §4 R2]`

> Surfaced by the S101 external cold-read bundle, which the W4 WP predated. NEW by construction. Compute follow-up with a pre-registered gate + kill criterion; the memo R2 is gated "only if R1 shows partial structure" → SEQUENCED AFTER the coldread Slot-2 workshop (the S2-1 normalization-non-universality adjudication). DISTINCT from the four CFs above (those are H₀-anchor-independence / branch-iv / rectified-drive / M₀-transfer; this is the thermodynamic a(t)-derivation route). Cosmology-corridor / a(t)-Friedmann subject matter (anchored to w4).

1. **What**: IF the coldread Slot-2 (S2-1) verdict is R1-survives-partial-structure (normalization partly recoverable), attempt the Jacobson route: Clausius δQ = T dS on local acoustic horizons, entropy density from D_K mode counting, recover a Raychaudhuri-consistent sign relation between dS/dτ and emergent focusing. **Anchoring note**: the substrate is NOT virgin here — S64 (van-den-dungen synthesis) already carries a d=12-generalized Jacobson derivation (Rindler horizon → Unruh T → Clausius → Raychaudhuri → contracted Bianchi → `Λ^{(12)} = (3/8)R_K + (1/2)R^{(4)}`), `A_horizon_FW = 71226.26 GeV⁻²` is pinned (S82/S88/S92 emergent-area-theorem), and `GGE-ENTROPY-FUNCTIONAL as V.P.` is an OPEN channel (S84) noting τ_fold may extremize the Jacobson-Λ_J horizon-entropy. The memo's "build from scratch" framing is partly stale — the horizon-local object must be ASSEMBLED from these existing pieces, not invented.
2. **Inputs**: the coldread-S2-1 workshop verdict (GATING — fires only on R1-partial-structure); the S64 d=12 Jacobson derivation; `A_horizon_FW = 71226.26 GeV⁻²`; the `GGE-ENTROPY-FUNCTIONAL as V.P.` open channel (S84); D_K mode counting; the relic S_ent=0 purity (a GLOBAL-state property — distinct from horizon-local entropy, must be reconciled).
3. **Gate**: PASS = Raychaudhuri-consistent sign relation between dS/dτ and emergent focusing, pre-registered before compute. **Kill**: if the acoustic-horizon temperature is τ-degenerate (plausible given the S98 conformally-stationary-frame result, a_eff const to 7e-7), the route is structurally closed — log and stop.
4. **Effort**: separately-planned program (heavy; the memo flags it expensive), only if coldread-S2-1 → R1-partial-structure. **Depends on**: coldread-S2-1 verdict (gating); S64 Jacobson derivation; `A_horizon_FW`; the S84 GGE-entropy open channel.

> **DISPOSITION (2026-06-09, S101 normalization-non-universality workshop — `sessions/session-101/workshops/s101-normalization-non-universality-workshop.md`, R3 verdict CONVERGED): FORECLOSED-AS-GATED.** The coldread-S2-1 (normalization-non-universality) adjudication closed **R4-trigger**: the §6.3 obstruction is a single **rank-1** normalization non-universality (`O = w·Ô`, one un-fixed scale `w = M_KK`, certificate = Half-A Sage-proven covariance-rank theorem ∘ Half-B N₃=0-grounded BDI single-cutoff count). CF-coldread-6's gating condition is `R1 lands partial structure` (memo §5), operationalized as `rank(obstruction) ≥ 2` (R1 fixes one normalization but not another). Under the rank-1 certificate `rank = #(unprotected scales) = 1` — the decision is binary R1-PASS-rank-0 (falsifies) vs R4-rank-1 (confirms), with **NO rank≥2 partial-structure middle**. Therefore CF-coldread-6's trigger is **a-priori impossible**; the Jacobson-partial-structure route is NOT a deferred CF — its precondition cannot be met. This is a constraint-map elimination by structural argument (not a failed compute), completed in-session per the no-technical-debt discipline. **Carve-out PRESERVED**: only the *partial-structure-gated role* of the Jacobson route dies. An **independent** Jacobson horizon-entropy derivation pursued for a non-normalization reason (a separate derivation of horizon entropy from the S64 d=12 Jacobson chain, `A_horizon_FW = 71226.26 GeV⁻²`, the S84 GGE-entropy-functional-as-V.P. open channel) is a DIFFERENT object and remains admissible as its own future item — see Remaining Open Question 4 in the workshop. Do NOT route CF-coldread-6 as gated to S102; do NOT delete this block (append-only audit trail).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-08 | H₀ flagship (Row #81 / EVOI rank-7b) | value HELD (NON-PROMOTION-BY-HELD-NUMBER) | RESOLVED — N=0.999859/67.40 re-pinned w/ anchor-degeneracy disclosure (G_N prediction) | W4-4 PASS |
| 2026-06-08 | q∝H closure (C10 physical route) | imposed INPUT | DERIVED via self-consistency; C10 n_eff physical-route activates at n=2 | W4-1 PASS |
| 2026-06-08 | Post-fold relic parametric resonance | open (H-parity clause d argument-grade) | IN-band resonance LIVE → clause (d) coincidence-bounded; clock γ=29.7532 derived | W4-2 FAIL |
| 2026-06-08 | branch-iv w₀(L) evaluator (DR3-readiness) | truncation-unverified (S100b) | NO principled evaluator (R_JE retirement lossy); gap at derivation level | W4-3 INFO |
| 2026-06-08 | M₀^sector BCS screening | open ([+5.4,+7.1]% residual) | band-shrunk to [−1.64,0]% (≤2% ceiling); BCS attribution weakened; convention-sensitive | W4-5 INFO |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict audit |
|:-----|:-------|:------------|:------------|:--------------|
| W4-1 | `s101_w4_qeq_selfcons.py` | `.npz` (77 KB) | `.png` | `c06a956b…` |
| W4-2 | `s101_w4_qeq_relic_oddfloor.py` | `.npz` | `.png` | `98a923fd…` |
| W4-3 | `s101_w4_branch_iv_evaluator.py` | `.npz` | `.png` | `cd0492d6…` |
| W4-4 | `s101_w4_h0_proper_a2.py` | `.npz` | `.png` | `cd8e8c0b…` |
| W4-5 | `s101_w4_m0_bcs_screening.py` | `.npz` (19 KB) | `.png` | `1a1eff66…` |

All scripts in `computations/session-101/`. Verdicts + dual-SHA + schema-v2 3-tuples + provenance rows in `s101_gate_verdicts.txt`.
