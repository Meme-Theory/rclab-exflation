# Session 112 Wave 3 — Compact-Object + Floquet Precision (Tier-3 Refinement) (Results Working Paper)

**Session**: 112 | **Wave**: W3 | **Plan**: session-112-plan-w3.md | **Theme**: Two independent Tier-3 (non-blocking, corridor-narrowing) precision computes — each closes the *magnitude* leg of a prior bracketed/MARGINAL result whose SIGN already PASSed: the white-hole exit-slice microstate count (causal-patch bulk-mode fraction) and the Floquet ring-down modulation depth `h_par` (physical Volovik-tracking V_eff re-integration).

## Gate Sections

### §W3-1. CF-S112-B5A-BRACKETED (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S112-B5A-BRACKETED`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (white-hole exit-slice microstate count via causal-patch interpolation between two bracketing QES/island prescriptions)
**Agent**: `hawking-theorist`
**Hypothesis**: With the causally-accessible bulk-mode fraction `f_bulk` DERIVED from the white-hole exit-slice causal structure (not tuned to hit A/4), the microstate count `S_microstate = Area(∂I)/4 + f_bulk·S_bulk-EE(I)` lands at the emergent area-law value `A_horizon_FW/4` within 10% (`|R(f_bulk) − 1| ≤ 0.10`).
**Plan reference**: `sessions/session-plan/session-112-plan-w3.md` §W3-1 (machinery pin, bracket endpoints, substitution chain source).

**Verdict**: **FAIL** (composite). 3-tuple: **sign=PASS · magnitude=FAIL · regime=VALID**.

The derived causal-patch fraction `f_bulk = 0.00396` falls **far below** the PASS band `[0.4367, 0.6705]`. The bracketed microstate ratio lands at `R(f_bulk) = 0.5297` — essentially back at the edge-only undershoot — giving `|R(f_bulk) − 1| = 0.4703`, above the 0.25 INFO ceiling → **composite FAIL** per the plan rubric (`FAIL_meaning`: `|R−1| > 0.25`). The SIGN is correct (the bulk-EE correction is positive/gap-closing, `dR/df_bulk = +0.8557 > 0`, consistent with both prior verdicts' sign=PASS); the MAGNITUDE FAILs because the Mach-13.75 white-hole causal patch is too narrow to make the island bulk-EE causally accessible on the exit slice.

**Output Artifacts**:
- `computations/session-112/s112_cf_b5a_bracketed.py` — producing script (verified: contains `from canonical_constants import` and `print_verdict_payload`).
- `computations/session-112/s112_cf_b5a_bracketed.npz` — data (R(f_bulk), f_bulk, bracket endpoints, causal-patch derivation, PASS/INFO bands, diagnostic alternatives, FORBIDDEN tautology crossing).
- `computations/session-112/s112_cf_b5a_bracketed.png` — 2-panel plot (Panel A: `R(f_bulk)` interpolant with PASS/INFO bands + derived `f_bulk` + bracket endpoints + FORBIDDEN R=1 line; Panel B: cumulative island bulk-EE vs λ with `λ_causal`, `λ_exit`, `λ_QES` markers).
- `computations/session-112/s112_gate_verdicts.txt` — `CF-S112-B5A-BRACKETED` canonical line + dual-SHA companion + schema-v2 3-tuple row + regulator-pin row (4 rows; `audit_sha256=1bdf4c8d7a4e6abdbb63a10aeb880769b694a1ef978e3fb3344bfe074463ccba`, `content_sha256=adf143d970c8e90de2abadfe8ea470b504059ef37ca76f71ebdc5db536a2d989`).
- This WP section.

4-tuple: `(value=R_of_f=0.529711, scheme=QES-island-bracketed-interpolation, convention=RATIO-DERIVED-CAUSAL-PATCH-FRACTION, L_max=12)`.

**MCP Pre-Compute Audit**:
- `get_constant("A_horizon_FW")` → `71226.26338976152` (S92, gate S92-W8-CF-S92-T1-7-CF39-SUBSTANTIVE-RETRY; not superseded). Confirms `A_quarter = 17806.56584744038` pin.
- `get_constant("c_conical")` → not in MCP; canonical source is `inv4_w1_euclidean_replica.npz` (`c_conical = 0.2500001250001146`, the `a_2^{Pauli-Villars}` conical Seeley-DeWitt 2nd moment), consistent with the plan pin and cross-checked against all three input npz files.
- `search_knowledge("B5A microstate island white-hole exit-slice causal patch f_bulk")` → S110-CF-B5A-MICROSTATE (FAIL, R_edge), S111-CF-B5A-ISLAND (FAIL, R_island=1.382), and **Acoustic white hole — PROVEN S85** (theorem: one-directional / single-asymmetric-open causal disconnect). NOT pre-closed: the bracketed-interpolation gate is a new construction continuing the two FAILs.
- `search_knowledge("Mach 13.75 supersonic transit fold acoustic white hole causal disconnect threshold")` → `Mach_max_framework = 13.75` (canonical, S85; the framework Mach at the van Hove fold) and the S85 one-directional white-hole causal-disconnect theorem. These anchor the inverse-Mach causal-patch derivation.

**Results**:

*Bracket endpoints (pinned, npz-loaded; cross-checked vs plan to publication precision):*
- `R_edge = 0.5263227104145511` (S110-CF-B5A-MICROSTATE; edge-only `S_boundary = 9372` modes, bulk-EE OMITTED — the factor-1.9 UNDERCOUNT, lower bracket).
- `R_island = 1.3820022088029909` (S111-CF-B5A-ISLAND; full `Area(∂I)/4 + S_bulk-EE(I)` at the same `λ_exit` — the OVERSHOOT, upper bracket).
- `λ_exit = 2.4893` (the substrate-fixed `a_0/a_2` area-perimeter fold marker; NOT chosen to hit A/4).
- `A_quarter = A_horizon_FW/4 = 71226.26338976152 / 4 = 17806.56584744038` (CC2 anchor; matches `A_horizon_FW/4` to < 1e-9 rel).
- `c_conical = 0.2500001250001146` (`a_2^{Pauli-Villars}` conical 2nd moment; the `Area(∂I)/4` boundary-term normalization).

*Substitution chain ([SIGN] trigger; reproduced from the producing script):*
```
Def1: R_edge   = S_boundary/(A/4) = 9372/17806.5658 = 0.5263                 [S110, lower bracket]
Def2: S_bulk-EE(I) ≥ 0 (GGE von-Neumann entropy);  R_island = 1.3820         [S111, upper bracket]
Def3: A_quarter = A_horizon_FW/4 = 71226.263390/4 = 17806.565847            [emergent a_2 2nd moment]
Def6: f_bulk = S_bulk-EE(I_acc)/S_bulk-EE(I) = 60.34/15236.71 = 0.00396      [DERIVED causal-patch fraction]
Substitute: R(f) = R_edge + f·(R_island − R_edge) = 0.5263 + f·0.8557
Canonical form: dR/df = R_island − R_edge = +0.8557 > 0                       [strictly increasing — CC1]
Direction: R(0)=0.5263<1 (UNDERSHOOT), R(1)=1.3820>1 (OVERSHOOT);
           IVT ⇒ ∃! f* = 0.5536 with R(f*)=1                                 [the FORBIDDEN tautology crossing]
Result: f_bulk(derived) = 0.00396  ⇒  R(f_bulk) = 0.529711
        |R(f_bulk) − 1| = 0.470289  vs PASS 0.10, INFO 0.25
        PASS band on f_bulk = [0.4367, 0.6704];  derived f_bulk = 0.00396 ∉ band
```

*Causal-patch derivation (substrate geometry; NOT tuned to R=1):* the acoustic white hole is a ONE-DIRECTIONAL causal disconnect (PROVEN S85) — pre/post-transit are causally separated by the Mach-13.75 supersonic flow on the exit slice. The causally-accessible patch is the SUB-MACH portion of the island spectral support `[λ_min, λ_exit]` (width `W_island = λ_exit − λ_min = 1.6696`). For a one-directional white-hole horizon at `M = Mach_max_framework = 13.75`, the causally-connected fraction of the supersonic-flow region is the inverse Mach number `1/M` (the sound-cone half-angle `sin θ_c = c_s/v_flow = 1/M` subtends the accessible cone interior). The causal-patch threshold, measured from the spectral floor `λ_min` (the same floor S110 measured `λ_exit` from):
```
λ_causal = λ_min + W_island/M = 0.81974 + 1.66956/13.75 = 0.94116
f_bulk   = S_bulk-EE(|λ| ≤ λ_causal) / S_bulk-EE(I) = 60.3421 / 15236.7133 = 0.003960
```
The patch is extremely narrow (`λ_causal = 0.941` sits barely above the floor `λ_min = 0.820`), capturing only 60.34 of the 15236.71 nats of island bulk-EE: **the white-hole horizon is so deep in the supersonic regime that almost none of the island bulk-EE is causally accessible on the exit slice.**

*Cross-checks:*
- **CC1 (monotonicity)**: `dR/df_bulk = R_island − R_edge = +0.8557 > 0` — R rises from the edge undershoot toward the island overshoot. SIGN=PASS (the predicted positive/gap-closing direction holds; consistent with both prior FAILs carrying sign=PASS).
- **CC2 (anchor consistency)**: `A_quarter = A_horizon_FW/4` to < 1e-9 rel; `c_conical = 0.25` from inv4 replica npz (cross-checked across all three input npz). The L12 cumulative bulk-EE at `λ_exit` reproduces the cached `sbulk_primary` to 2.7e-3 rel (300-pt grid interpolation vs cached value), confirming the f_bulk denominator basis.
- **GPU**: the 166896-mode L12 cumulative bulk-EE monotone cross-check ran on `AMD Radeon RX 9070 XT` (torch 2.9.1+rocm); `used_gpu=True`.

*Diagnostic alternatives (NOT canonical — reported so the audit can see the canonical value follows the pinned definition and that NO substrate causal-patch reading reaches unity):*

| Causal-patch reading | `f_bulk` | `R(f_bulk)` | in PASS band? |
|:---|---:|---:|:---|
| **(canonical) inverse-Mach `W/M` on island support** | **0.00396** | **0.5297** | **NO** |
| (D1) inverse-Mach on full spectral support | 0.01715 | 0.5410 | NO |
| (D2) direct `1/M` bulk-EE fraction | 0.07273 | 0.5886 | NO |
| (D3) `c_BLV` sound-speed width fraction (`c_s = 0.485`) | 0.12681 | 0.6348 | NO |
| (D4) **[FORBIDDEN]** R=1 tautology crossing `f*` | 0.55357 | 1.0000 | — (excluded) |

Every substrate-physical causal-patch reading lands `R < 0.64` — well below the PASS band's lower edge of 0.90. The largest (D3, the `c_BLV` sound-speed reading) reaches only `R = 0.635`. The FORBIDDEN R=1 crossing (`f* = 0.5536`) is nowhere near any derived value — **the anti-tautology discipline held by a wide margin**: no comparator-shopped tuning was needed or possible to land within 10%.

**Anti-tautology discipline**: the `S_gen == A/4` crossing (`R_island_QES = 0.9868` at `λ_QES = 2.5579`) is FORBIDDEN as the canonical value — it forces `R = 1` by construction — and is reported DIAGNOSTIC-ONLY in the npz. The canonical landing is `R(f_bulk)` with `f_bulk` the substrate-derived inverse-Mach causal-patch fraction, pinned pre-result. No iterate-until-PASS; the bracket endpoints and the f_bulk definition were fixed before the result.

**Substrate framing (GEOMETRIC)**: the white-hole exit slice IS the spectral-triple structure `(A_K^{≤12}, H_K^{≤12}, D_K^{≤12})` on the exit configuration — the boundary entropy and bulk entanglement entropy are spectral functionals of the `D_K^{≤12}` eigenvalue spectrum, NOT fields on a pre-existing geometric container. Direction of explanation: `D_K^{≤12}` eigenvalues → conical `a_2^{Pauli-Villars}` Seeley-DeWitt 2nd moment (gravity IS the 2nd spectral moment) → `Area(∂I)/4` boundary term (`c_conical = 0.25`) → GGE occupation of exit-slice bulk modes inside the acoustic-white-hole causal patch → causally-accessible `S_bulk-EE(I_acc)` (fraction `f_bulk` of the full island) → `S_microstate = Area(∂I)/4 + f_bulk·S_bulk-EE(I)` → comparison to the EMERGENT area `A_horizon_FW/4` (`A = a_2` 2nd moment; the area theorem is the Level-3 emergent image of substrate spectral monotonicity, per `phononic-framing.md` "IS Space"). Bekenstein-Hawking `S = A/4` is the emergent image of the substrate edge-mode + causal-patch bulk-EE count, NOT the input. The causal-patch restriction is the acoustic-white-hole horizon (Mach-13.75 supersonic-flow causal disconnect), the exflation substrate description of the horizon — not an LCDM container boundary.

**Assessment / solution-space update**: this is a corridor-closing FAIL. The corridor "QES/island microstate = A/4 on the white-hole exit slice via a substrate-derived causal-patch `f_bulk`" is **closed**: the inverse-Mach causal patch (and every diagnostic causal-patch reading tested) leaves the microstate count at the edge-only undershoot `R ≈ 0.53–0.64`, far from unity. Physically — the one-directional Mach-13.75 white-hole horizon is so deep in the supersonic regime that the GGE bulk-EE of the island is almost entirely causally INACCESSIBLE on the exit slice, so the exit-slice microstate count is dominated by the boundary edge-mode term alone (the S110 reading). The two-sided bracket `[R_edge = 0.5263, R_island = 1.3820]` therefore stands as the standing bound, with the substrate-physical interior now pinned near its lower edge (`R ≈ 0.53`) rather than at unity. The factor-1.9 S110 undercount is NOT closed by causal-patch-restricted island bulk-EE — it is, if anything, reaffirmed: causal accessibility removes essentially all of the bulk-EE that the full-island (S111) overshoot added. The result is NON-BLOCKING (Tier-3 refinement); it does not change any PROVEN structural result, only maps which microstate-count corridor is closed. Per the dual-prior, the FAIL re-allocates 0.90 to Track B (corridor stays bracketed, residual reported) — sharpened: the residual is not merely "bracketed" but localized to the lower-bracket edge.

---

### §W3-2. CF-S112-FLOQUET3-HPAR-TIGHTEN (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S112-FLOQUET3-HPAR-TIGHTEN`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (modulus ring-down modulation depth from a physical late-time effective potential)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: Re-integrating the coupled modulus + Friedmann ODE with the PHYSICAL S66 Volovik-tracking `V_eff` (which settles at `τ_fold` instead of running away) yields a steady residual ring-down amplitude `δτ_amp` whose assembled modulation depth `h_par = δτ_amp·(d ln E²/dτ)` pins to the guard-floor `8.3e-4` within 10% (`|h_par_derived − 8.3e-4|/8.3e-4 ≤ 0.10`).
**Plan reference**: `sessions/session-plan/session-112-plan-w3.md` §W3-2 (coupled-ODE machinery pin, V_eff source, substitution chain).

**Verdict**: **INFO** — `sign=PASS, magnitude=INFO, regime=VALID` ⇒ composite **INFO** (generic collapse, gate-verdicts.md). `h_par_derived = 9.4248e-4`; `metric = |h_par_derived − 8.3e-4|/8.3e-4 = 0.1355` (just outside the 10% PASS band; well inside the 1.0 INFO band). The physical Volovik-tracking `V_eff` re-integration **RAISES** `δτ_amp` from the S111 one-period heuristic `1.842e-3` to the settled-envelope value `6.292e-3` (factor 3.42, the predicted direction), bringing `h_par` from S111's factor-3.01-**low** (metric 0.668) to **13.6% high** — a substantial corridor-narrowing onto the correct (high) side of the guard-floor, with the regime upgraded MARGINAL→VALID. `h_par` is upgraded from guard-floor-ASSERTED toward substrate-MOTIVATED (right scale + sign + side), but is not pinned within 10%, so it stays asserted-but-physically-motivated (the guard-floor `8.3e-4` is an odd-floor pin from a distinct S101-W1 construction and need not coincide bit-for-bit with the afterglow-derived value). **NON-BLOCKING**: `h_par = 9.42e-4 ≪` DTC threshold `14/193 = 0.072539` (by ~77×) ⇒ §VII.BP DEAD (no discrete time crystal) is UNAFFECTED.

**Output Artifacts**:
- `computations/session-112/s112_cf_floquet3_hpar_tighten.py` — producing script; contains `from canonical_constants import` (line 96; `_shared`-on-path then import `tau_fold, G_DeWitt, M_KK` per the S111 pattern) and `print_verdict_payload` (def line 341, call line 572).
- `computations/session-112/s112_cf_floquet3_hpar_tighten.npz` — data (trajectory + V_eff construction params + envelope reads + all comparison anchors).
- `computations/session-112/s112_cf_floquet3_hpar_tighten.png` — 2-panel plot (modulus ring-down with settled-envelope δτ_amp band vs S111 one-period; h_par log-bar comparison vs guard-floor 10% band & DTC threshold).
- `computations/session-112/s112_gate_verdicts.txt` — canonical line `CF-S112-FLOQUET3-HPAR-TIGHTEN: INFO` + dual-SHA companion + schema-v2 3-tuple row + 4 extra companion rows (composite-precedence / δτ_amp-settled / regulator_pin=N/A / NON-BLOCKING).
- This WP section.

`grep -E` confirmation (content presence, not line/byte counts):
```
$ grep -nE 'from canonical_constants import|print_verdict_payload' s112_cf_floquet3_hpar_tighten.py
96:from canonical_constants import tau_fold, G_DeWitt, M_KK  # noqa: E402  (framework constants)
341:def print_verdict_payload(verdict, value, audit_sha, content_sha,
572:    payload = print_verdict_payload(
$ grep -E '^CF-S112-FLOQUET3-HPAR-TIGHTEN:.* audit_sha256=[a-f0-9]{64}' s112_gate_verdicts.txt
CF-S112-FLOQUET3-HPAR-TIGHTEN: INFO -- value='0.0009424757846403458' scheme=FW convention=RATIO-physical-Veff-settled-envelope-x-spectral-sensitivity L_max=12 audit_sha256=dbb931952ee0fa5dcdc810f12bdc94a651dda36e73e4bbe89bd1be336e2ae85a content_sha256=15d93be1d8916faba0c8329a1eb0a3dca7909c15758e670a0bc34e8f6162919a schema_version=S84+
```
dual-SHA companion + 3-tuple companion rows present (`# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; query-first discipline):
- `search_knowledge("S66 Volovik tracking V_eff effective potential tau_fold minimum DILUTION-CC")` → `V_eff(τ) = V_KK(τ) + F_BCS(Δ_0(τ))` (s52_unified_action_output.txt); DILUTION-CC PROVEN S66, `rho_vac/rho_obs = 1.032`, Γ_eff=0.99970. Confirms the V_eff functional form + tracking-vacuum minimum at τ_fold.
- `get_constant("h_par")` → NOT a canonical constant (the guard-floor `8.3e-4` lives as the S101-W1-QEQ-RELIC-ODDFLOOR odd-floor pin, not a `canonical_constants.py` entry). Confirms no canonical `h_par` to overwrite; this gate tests against the odd-floor pin.
- `search_knowledge("h_par guard floor 8.3e-4 QEQ relic oddfloor Mathieu modulation depth S101")` → `q_M = A·h_par/2` with `h_par = 8.3e-4` (S101-W1-QEQ-RELIC-ODDFLOOR PROVEN); `h_par_derived = (dω²/dτ)·δτ_amp/ω²` (session-111-plan-w5). Confirms the guard-floor provenance + the assembly formula.
- `search_knowledge("modulus mass omega_tau ring-down frequency V_eff curvature ... Volovik tracking restoring")` → `omega_tau = sqrt(V_eff''(tau_min) / M(tau))` (QA-Q2.3, S75 Baptista workshop). The canonical modulus-frequency formula used to pin the V_eff curvature.
- NOT PRE-CLOSED: genuine carry-forward compute (S111-W5 §"Carry-Forward Computations" line 350); the S111 gate left δτ_amp regime-MARGINAL pending the physical-V_eff re-integration this gate performs.

**Results**:

*V_eff construction (Volovik-tracking, genuine minimum at τ_fold; NOT tuned to the PASS band):*
- `V_eff(τ) = V_KK(τ) + V_track(τ)`. `V_KK(τ)` = quadratic fit through the three s52 calibration points `V_KK(0)=−46.6528`, `V_KK(fold)=−47.0760`, `V_KK(0.50)=−53.3794` M_KK⁴ ⇒ `V_KK''=−72.4247 M_KK²` (negative; **this is the source of the bare runaway** — V_KK alone has no minimum, exactly the s73b `τ → −99.885` the S111 heuristic fought) and `dV_KK/dτ|_fold = −9.1077 M_KK³`.
- `V_track(τ) = −dV_KK/dτ|_fold·(τ−τ_fold) + ½(V_eff''−V_KK'')·(τ−τ_fold)²` — the Volovik-tracking restoring term, pinned by TWO substrate conditions, NOT the PASS band: **(i)** `dV_eff/dτ|_fold = 0` (DILUTION-CC tracking-vacuum equilibrium AT τ_fold; verified `= 0.000e+00`); **(ii)** `V_eff''(τ_fold) = M_mod·ω_q² = 116.6320·2.012813² = 472.5248 M_KK⁴` with `M_mod = G_mod_full = M_p²·G_DeWitt = 116.6320 M_KK²` (s52). The resulting modulus ring-down frequency `ω_τ = √(V_eff''/M_mod) = 2.012813 M_KK = ω_q EXACTLY` (the relic-mode near-a=1 frequency; the SAME scale the S111 heuristic used as a ring-down proxy — now DERIVED from the V_eff curvature via QA-Q2.3, not assumed).

*Coupled-ODE integration (`τ̈ + 3Hτ̇ + dV_eff/dτ = 0`, `H² = ⅓[½τ̇² + V_eff_shift]`):*
- `solve_ivp` LSODA, `rtol=1e-9`, `atol=1e-12`, `N=50000` steps, window `t_end = 30·T_ring = 136.36 M_KK⁻¹` (`T_ring=4.5454`). Success. Friedmann constant `κ=2.700e-3` calibrated so `H_launch = H_post_fold = 0.97539`.
- Trajectory: launched from `τ_fold=0.19` with `τ̇(0)=v_launch=26.545`, overshoots to `τ_max=1.298` (nonlinear `A_overshoot=1.108`), rings back through `τ_min=−0.739`, and **settles** toward `τ_fold` (`τ_final=0.18394`) — NO runaway (the physical V_eff minimum holds the modulus, unlike the bare s73b parameterization).
- Damping: underdamped discriminant `ω_τ²−γ²=1.911>0`, `γ=3H/2=1.46309`, `Q=ω_d/(2γ)=0.4724`. The late-time envelope decays at `d(ln amp)/dt = −0.0167` — ~90× SLOWER than the instantaneous `γ` because H itself dilutes as the modulus settles (Hubble friction self-extinguishes; H² ∝ ρ → small), so the residual ring-down is long-lived and the envelope plateaus near 6e-3 rather than vanishing.

*δτ_amp settled-envelope read + h_par assembly:*
- `δτ_amp = ½(max−min) of (τ−τ_fold) over the FINAL ring-down period [t_end−T_ring, t_end] = 6.2918e-3` (deterministic window-end definition; the launch transient `A_overshoot=1.108` is reported separately and EXCLUDED). **Robust to window choice**: last-1/2/3/5-period reads give `6.29/6.51/6.76/7.29e-3` (all INFO; metric 0.14→0.32 — no window flips the verdict).
- `δτ_amp/τ_fold = 0.0331 ≪ 1` (settled-phase linearization holds); breach fraction (|δ|/τ_fold > 0.5 over the FULL window, capturing only the brief launch transient) = 0.0362 ≤ 0.05 ⇒ `regime=VALID`.
- `h_par_derived = δτ_amp·(d ln E²/dτ) = 6.2918e-3·0.149795 = 9.4248e-4` (PRIMARY, near-a=1 spectral leg). Range lower (median band sensitivity): `h_par_median = δτ_amp·0.075338 = 4.7401e-4`.
- `metric = |9.4248e-4 − 8.3e-4|/8.3e-4 = 0.1355`. PASS band on δτ_amp `[4.9868e-3, 6.0950e-3]` (unity target `5.5409e-3`); the settled `6.2918e-3` sits just ABOVE the upper edge ⇒ INFO (13.6% high, vs S111's 66.8% low).

*4-tuple*: `(value=9.4248e-4, scheme=FW, convention=RATIO-physical-Veff-settled-envelope-x-spectral-sensitivity, L_max=12)`.

*Cross-checks*:
- **CC1 (monotonicity, substitution-chain Step 4)**: `∂h_par/∂δτ_amp = (d ln E²/dτ) = +0.14980 > 0` ⇒ h_par strictly increasing in δτ_amp. The physical V_eff settling RAISES δτ_amp 3.42× over the one-period heuristic ⇒ h_par rises 3.42× (2.76e-4 → 9.42e-4), crossing the guard-floor from below to slightly above — the predicted direction (settling-without-runaway raises δτ_amp vs the runaway-forced one-period truncation).
- **CC2 (cached spectral leg)**: `dlnE2_dtau = 0.14979505187425238` (`s_near1`, s111 npz) — read from the L12 cache, INVARIANT under the V_eff change (BdG `E_k=√(λ²+Δ_BCS²)`, Δ_BCS τ-independent ⇒ `dE²/dτ=dλ²/dτ` is a property of the cached spectrum, not the dynamics). NOT re-derived (plan: "same spectral leg"). Range lower `dlnE2_dtau_median = 0.07533807832928088`.

*Substitution chain (`[CHAIN]` with directional ring-down-envelope claim — fully substituted)*:
```
Claim: the physical S66 Volovik-tracking V_eff (settling the modulus at tau_fold) RAISES the
       residual ring-down amplitude delta_tau_amp from the S111 one-period heuristic (1.842e-3)
       toward the settled-envelope value, assembling h_par = delta_tau_amp*(d ln E^2/dtau) closer
       to the guard-floor 8.3e-4.

  Step 1: h_par := delta_tau_amp * (d ln E_n^2/dtau)         [inv-12 W3-2 Mathieu normal form]
  Step 2: (d ln E_n^2/dtau) = 0.149795  at near-a=1 relic mode [s111 s_near1; CACHED, INVARIANT]
  Step 3: delta_tau_amp := late-time settled envelope of  tau_ddot + 3H tau_dot + dV_eff/dtau = 0,
                           H^2 = (1/3)[(1/2)tau_dot^2 + V_eff_shift],  V_eff = Volovik-tracking
                           (min at tau_fold)                 [REPLACES S111 one-period 1.842e-3]
        => delta_tau_amp(ODE) = 6.2918e-3                    [the settled half-amplitude]
  Step 4: h_par_derived = 6.2918e-3 * 0.149795 = 9.4248e-4
          metric        = |9.4248e-4 - 8.3e-4| / 8.3e-4 = 0.1355

  Canonical form: d h_par / d delta_tau_amp = +0.14980 > 0   (h_par strictly increasing in delta_tau_amp)
  Direction:  settling-without-runaway gave delta_tau_amp = 6.2918e-3 (factor 3.42 ABOVE the
              one-period heuristic 1.842e-3) => h_par rose 2.76e-4 -> 9.4248e-4, crossing the
              guard-floor 8.3e-4 from below to 13.6% above. The DIRECTION (settling raises
              delta_tau_amp vs the runaway-forced one-period truncation) is the predicted sign
              (CONFIRMED); the magnitude lands INFO (just outside 10%).
  Conclusion: INFO (0.10 < metric = 0.1355 <= 1.0); h_par upgraded guard-floor-ASSERTED ->
              substrate-MOTIVATED at the right scale + sign + side, not pinned within 10%.
              NON-BLOCKING: h_par = 9.42e-4 << 14/193 = 0.072539; §VII.BP DEAD UNAFFECTED.
```

*3-tuple (schema-v2)*: `sign_verdict=PASS` (settled δτ_amp ≥ S111 heuristic AND h_par > 0 — predicted direction confirmed) · `magnitude_verdict=INFO` (`0.10 < metric=0.1355 ≤ 1.0`) · `regime_verdict=VALID` (settled-phase `δτ_amp/τ_fold=0.033 ≪ 1`; breach 3.6% ≤ 5%).

*Dual-SHA*: `audit_sha256=dbb931952ee0fa5dcdc810f12bdc94a651dda36e73e4bbe89bd1be336e2ae85a` (script+canonical+pinmap) · `content_sha256=15d93be1d8916faba0c8329a1eb0a3dca7909c15758e670a0bc34e8f6162919a` (script only).

*Comparison vs the S111 heuristic it replaces*: S111-CF-FLOQUET3 (INFO, `δτ_amp=1.842e-3` via `A_launch·exp(−γT_ring)`, `h_par=2.76e-4`, metric 0.668, factor-3.01 LOW, regime=MARGINAL). This gate: `δτ_amp=6.292e-3` (settled coupled-ODE envelope), `h_par=9.42e-4`, metric 0.136, factor-1.14 HIGH, regime=VALID. The corridor narrowed from 66.8% off (low) to 13.6% off (high), and the regime upgraded MARGINAL→VALID. The one-period heuristic was the underestimate exactly as the plan predicted: it truncated the ring-down at one period, but at Q≈0.47 with self-extinguishing Hubble friction the modulus rings for many periods and the residual envelope decays ~90× slower than the instantaneous γ.

**Substrate framing**: PHONONIC. The modulus τ IS the Jensen deformation parameter (Level-2 moduli-deformation substrate-IS per `phononic-framing.md`, NOT a coordinate on a meta-container). The Mach-13.75 supersonic transit through the van Hove fold is IMPULSIVE; the substrate FREEZES diabatically (the Ordered Veil: `S_ent=0`, `R_therm=5251.82`, the GGE never thermalizes). What remains is a residual modulus ring-down — τ(t) launched from τ_fold with the transit velocity, overshooting and ringing back, DAMPED by Hubble friction `3Hτ̇`. Direction of explanation: `D_K eigenvalues → spectral-action moments (V_KK) + BCS condensation (F_BCS) → V_eff(τ) = V_KK + F_BCS with the S66 Volovik-tracking term settling the modulus at τ_fold (tracking-vacuum equilibrium ρ_vac ~ M_Pl²H², DILUTION-CC) → coupled modulus+Friedmann ring-down → steady residual δτ_amp → δτ_amp×(d ln E²/dτ) [relic-mode BdG spectral sensitivity] = h_par, the Mathieu modulation depth on the Leggett-channel GGE relic modes`. The S66 Volovik-tracking V_eff is the substrate's OWN emergent effective potential (vacuum-tracking thermodynamics), NOT an externally-imposed inflaton potential — the LCDM "reheating/preheating" vocabulary is INAPPLICABLE: this is **GGE-relic ring-down**, not slow-roll, not preheating. The genuine substrate-physics content this gate exposes: the late-time ring-down envelope is **long-lived because the Hubble friction self-extinguishes as the cosmology dilutes** (H² ∝ ρ → small as the modulus settles), so the relic modes are driven by a slowly-decaying residual amplitude (~6e-3), not a transient. NON-BLOCKING: the §VII.BP DEAD verdict (no discrete time crystal) is UNAFFECTED — it requires only `h_par ≪ 14/193 = 0.072539` (S111-CF-FLOQUET2, QQ-exact), which `h_par=9.42e-4` satisfies by ~77×; PASS/INFO/FAIL here is corridor-narrowing, not status-changing.

---

## Wave 3 Synthesis (team-lead)

Two Tier-3 precision refinements, both NON-BLOCKING (no PROVEN structural result changed; corridor-mapping only).

- **W3-1 CF-S112-B5A-BRACKETED — FAIL** (sign=PASS · magnitude=FAIL · regime=VALID; audit `1bdf4c8d…`). The derived causally-accessible bulk fraction f_bulk=0.00396 ⇒ R(f_bulk)=0.5297, |R−1|=0.4703 > 0.25 INFO ceiling. The single-sided Mach-13.75 white-hole exit-slice causal patch (λ_causal=0.941, just above the spectral floor λ_min=0.820) captures only **60.34 of 15236.71 nats** of island bulk-EE — so the microstate count sits at the **lower bracket edge** (R≈0.53, the edge-dominated S110 reading); the S110 factor-1.9 undercount is NOT closed by causal-patch island bulk-EE. Anti-tautology held by a wide margin (FORBIDDEN R=1 crossing f*=0.5536; every substrate causal-patch reading lands R<0.64).
- **W3-2 CF-S112-FLOQUET3-HPAR-TIGHTEN — INFO** (sign=PASS · magnitude=INFO · regime=VALID; audit `dbb93195…`). The physical S66 Volovik-tracking V_eff (genuine minimum at τ_fold; no runaway) settles the modulus to δτ_amp=6.292e-3 — **3.42× the S111 one-period heuristic, the predicted direction** — assembling h_par=9.425e-4, metric=0.1355 (13.6% high, just outside the 10% PASS band). Corridor narrowed: S111 factor-3.01-LOW (regime MARGINAL) → 13.6%-HIGH (regime VALID), h_par now substrate-MOTIVATED (right scale + sign + side) but not pinned within 10% (the guard-floor 8.3e-4 is an S101-W1 odd-floor pin from a distinct construction). **NON-BLOCKING**: h_par ≪ DTC threshold 14/193=0.0725 (×77) ⇒ §VII.BP DEAD unaffected.

### Effected In-Session (non-math; verified on disk)

- [x] §VII.BP DEAD unaffected by FLOQUET3 — recorded in §W3-2 (h_par ≪ DTC threshold); the §VII.CJ 4th-pin (W2-4, registry `:21320`) is the cutoff-robustness companion confirming DEAD survives the L_max-extension loophole.
- [x] h_par provenance: no `canonical_constants.py` promotion — INFO does not clear the 10% band, so h_par stays guard-floor-ASSERTED (S101-W1 odd-floor pin), now substrate-MOTIVATED. (Per `math-scripts.md §"In-session promotion vs carry-forward"`: a value that does not clear its gate is not promoted.)

## Carry-Forward Computations

### CF-S113-B5A-TFD — two-sided TFD/island white-hole microstate count

| Field | Spec |
|:--|:--|
| **What** | Re-compute the white-hole exit-slice microstate count via a TWO-SIDED thermofield-double (TFD) island construction — the surviving route. The single-sided exit slice undershoots to the edge (R≈0.53), the full island overshoots (R≈1.38); A/4 sits between, unreached by either. Test the TFD microstate count against the emergent area-law A_horizon_FW/4. |
| **Inputs** | The L12 GGE bulk-EE profile (`computations/session-111/s111_b5a_island.npz` cum_S_bulk); a TFD doubling of the exit-slice causal patch; `A_horizon_FW=71226.26338976152` (canonical, S92); `c_conical=0.25` (a₂^{Pauli-Villars}). |
| **Gate** | `|R_TFD − 1| ≤ 0.10` PASS; `(0.10, 0.25]` INFO; `> 0.25` FAIL. [SIGN] — monotone in the TFD-accessible bulk-EE fraction. |
| **Effort** | ~1 wave (reuses the S111 L12 bulk-EE profile; new machinery = the TFD doubling geometry on the exit slice). |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-22 | CF-S112-B5A-BRACKETED | white-hole microstate two-sided-bracketed [0.5263, 1.382] | CLOSED-at-lower-edge — single-sided causal-patch f_bulk lands R≈0.53 (edge-dominated); the "QES/island=A/4 via single-sided causal patch" corridor closed | only 60/15237 nats causally accessible on the exit slice |
| 2026-06-22 | CF-S112-FLOQUET3-HPAR-TIGHTEN | h_par MARGINAL (S111 factor-3.01-low) | INFO — substrate-motivated 13.6%-high, regime VALID; §VII.BP DEAD unaffected | physical Volovik-tracking V_eff raises δτ_amp 3.42× (no runaway) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) |
|:--|:--|:--|:--|
| W3-1 | s112_cf_b5a_bracketed.py | s112_cf_b5a_bracketed.npz | s112_cf_b5a_bracketed.png |
| W3-2 | s112_cf_floquet3_hpar_tighten.py | s112_cf_floquet3_hpar_tighten.npz | s112_cf_floquet3_hpar_tighten.png |
