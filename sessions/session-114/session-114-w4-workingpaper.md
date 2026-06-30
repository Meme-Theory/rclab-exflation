# Session 114 Wave 4 — A_s functional-selection decider + the surviving white-hole microstate route (Results Working Paper)

**Session**: 114 | **Wave**: 4 | **Plan**: session-114-plan-w4.md | **Theme**: the A_s **Object-2** functional-selection decider (does the substrate single out one spectral functional for the post-transit relic amplitude, or is functional-choice a physical d.o.f.?) + the surviving two-sided thermofield-double (TFD) white-hole exit-slice microstate route (Tier-3 NON-BLOCKING). Both close residual magnitude-openness questions; neither is a Planck-comparison gate.

## Gate Sections

### §W4-1. CF-S114-AS-FUNCTIONAL-SELECTION (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S114-AS-FUNCTIONAL-SELECTION`
**Trigger**: `[CHAIN]` (directional `d|β_k̂|²/d(a_0/a_2)` sub-test; the substitution chain on the sub-test direction is the load-bearing derivation)
**Classification**: **PHONONIC**
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The substrate selects NO unique spectral functional for the post-transit A_s amplitude — the decisive sub-test (does `aH|_fold = 0.975 M_KK` carry the SDW/Zubarev `a_0/a_2` 181× split?) returns NO (transit-trajectory-fixed, `d|β_k̂|²/d(a_0/a_2) = 0`), so the openness is confined to the UNIFIED route, but the cross-functional spread (impulse-quench / UNIFIED / Parker, 1.2590 OOM, none in-band) persists ⇒ SELECTION FAILS (PLURALISM-PERMANENT, informative: A_s magnitude is a physical d.o.f. like the CC ratio). PASS (a substrate-canonical selector collapses the spread) is the pre-registered open alternative, not pre-judged.
**Plan reference**: `sessions/session-plan/session-114-plan-w4.md` §W4-1 (machinery pin, dual-prior, substitution chain source).

**Verdict**: **FAIL** (composite) — **FUNCTIONAL-PLURALISM PERMANENT** (the informative outcome, NOT a defeat). Set-membership verdict = **PLURALISM**. Schema-v2 3-tuple: **sign_verdict = PASS** (the structural sub-test direction prediction `d|β_k̂|²/d(a_0/a_2) = 0` is confirmed exactly), **magnitude_verdict = FAIL** (the 1.2590-OOM cross-functional spread persists; no substrate-canonical selector collapses it), **regime_verdict = VALID** (clean analytic structural-zero + deterministic spread assembly). Composite collapse: `magnitude=FAIL ∧ regime=VALID ⇒ composite = FAIL` (gate-verdicts.md deterministic rule). Dual-prior posterior re-allocated **0.10 / 0.90** to Track B (PLURALISM-PERMANENT).

**Output Artifacts** (closure-verification checklist):
- (1) `computations/session-114/s114_cf_as_functional_selection.py` — PRESENT; `grep -E "from canonical_constants import"` → `from canonical_constants import *  # noqa...`; `grep -E "print_verdict_payload"` → matches (def + call). ✔
- (2) `computations/session-114/s114_cf_as_functional_selection.npz` — PRESENT, non-stub (37 keys incl. `struct_deriv_dbeta2_d_a0a2`, `cross_functional_spread_OOM`, all three OOM values, both kinematic reproductions, dual-SHA). ✔
- (3) `computations/session-114/s114_cf_as_functional_selection.png` — PRESENT, non-stub (2-panel: (A) structural-derivative sub-test, (B) cross-functional spread bars). ✔
- (4) Verdict line in `computations/session-114/s114_gate_verdicts.txt` matching `^CF-S114-AS-FUNCTIONAL-SELECTION:.* audit_sha256=[a-f0-9]{64}` — PRESENT WITH dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row + regulator_pin row + in-session-correction row (5 rows total via `emit_verdict`). ✔
- (5) This WP section §W4-1 with Status/Verdict/Output-Artifacts/MCP-Pre-Compute-Audit. ✔

**MCP Pre-Compute Audit**:
- `search_knowledge("A_s functional selection impulse-quench UNIFIED-AS-79 Parker spectral functional pluralism")` → returns FUNCTIONAL-SELECT-67 (the *n_s* functional-selection open channel, atlas-08 Q28) + the lizzi-spectral-functional registry; **NO closure covers the *A_s* functional-selection question** (FUNCTIONAL-SELECT-67 is n_s, distinct observable) ⇒ genuinely new content, NOT pre-closed.
- `get_constant("A_s_FW")` → `1.5367059962762235e-08` (S111-CF-AS3a, impulse-quench, `value vs Planck 2.1e-9 = +0.864 OOM`). Used as the impulse-quench POINT (cited, not re-derived).
- `get_constant("a_0_FW_zeta")` → `6440.0` (S88; n=0/s=4 cosmological-constant moment).
- `get_constant("a_2_FW_zeta")` → `2776.165389` (S88; n=2/s=3 Einstein-Hilbert moment).
- `get_constant("xi_KZ_FW")` → `0.018760052113614718` (S89); `get_constant("H_fold")` → `586.5267713108464` (S38).

**Results**:

*Set-membership verdict*: **PLURALISM** (the substrate selects NO unique spectral functional for the post-transit A_s amplitude).

*PART (A) — structural sub-test [SIGN], the load-bearing [CHAIN] derivation*:
- `d|β_k̂|²/d(a_0/a_2 horizon-exit) = 0.000000e+00` (exactly), well below the `1e-12` machine-zero floor ⇒ **sign_verdict = PASS** (matches the chain Step-4 prediction of 0). Max `|Δβ²|` over the full perturbation grid (spanning the ±181× SDW/Zubarev split) = `0.000000e+00`.
- `a_0/a_2 in |β_k̂|² input keys? = False` (the box-delta closed form reads only `Omega_z_on/off`, `V_box`, `Delta_eta`, `tau_window`, `eta_window`, `k_grid` — all fold-transit/UV quantities; no a_0/a_2 input).
- `aH|_fold = aH_target = 0.9753935188 M_KK` reproduces **EXACTLY (rel-dev 0.0)** from TWO independent fold-passage kinematic routes: `a_fold_raw·H_fold/Λ_rescale = 0.9753935188` AND `k_pivot/(k/aH)|_fold = 0.9753935188`. ⇒ `aH_is_transit_trajectory_fixed = True`. The fold-transit pump barrier carries NO a_0/a_2 freedom ⇒ **openness CONFINED to the UNIFIED-AS-79 route** (does not propagate to the impulse-quench floor).
- **IN-SESSION CORRECTION** (honestly disclosed per `v3-closure-recovery.md` PROHIBITED_ACTIONS Class-1 boundary): plan §W4-1 chain Step 1 wrote `aH|_fold = H_fold / Λ_rescale`, which **drops the fold scale-factor `a_fold_raw`** (that combination gives `0.00253 M_KK`, rel-dev 0.997 — wrong). The correct conformal-trajectory relation is the standard `aH = a(τ)·H(τ)`: `aH|_fold = a_fold_raw · H_fold / Λ_rescale` (rel-dev 0.0 EXACT), corroborated by the independent `k_pivot/(k/aH)|_fold` reproduction. Both are fold-passage kinematics; neither contains a_0/a_2. The correction STRENGTHENS the sub-test conclusion (EXACT kinematic reproduction vs the plan's loose "within rescale precision"), and is recorded in the verdict-line companion row.

*PART (B) — selection assembly (the three defensible functionals vs Planck `A_s = 2.1e-9`)*:

| Functional | A_s | OOM vs Planck | In Planck ±5% band? |
|:-----------|:----|:--------------|:--------------------|
| impulse-quench (floor POINT, `A_s_FW`) | `1.536706e-08` | **+0.86437** | No |
| UNIFIED-AS-79 (slow-roll) | `3.297762e-09` | +0.19600 | No |
| Parker-adiabatic | `5.987138e-08` | +1.45500 | No |

- **Cross-functional spread = 1.25900 OOM** (5 sig figs; = +1.455 − +0.196, with the impulse-quench POINT +0.864 sitting between). `n_functionals_in_planck_band = 0` (Planck in-band `|OOM|` threshold = `log10(1.05) = 0.02119`, matching the plan's 0.0212; reported **DIAGNOSTIC-only** — this is NOT a Planck-comparison gate).
- `substrate_canonical_selector_exists = False`: the three functionals are three DIFFERENT spectral functionals of the SAME D_K-derived occupation spectrum (sudden-scattering / slow-roll / adiabatic). The regime that SETS the floor POINT (impulse-quench diabatic transit) is settled, but the magnitude-as-a-comparison-NUMBER admits all three as physically defensible — the substrate carries no scheme-independent normalization at this scale (the exit-greybody filter is itself a fitted knob, inv12 W3-4). `cross_functional_spread_persists = True` ⇒ SELECTION hypothesis FAILS.

*Sub-test SIGN vs SELECTION verdict run in OPPOSITE directions (pre-registered)*: sub-test NO (transit-fixed, derivative = 0) shows the openness is CONFINED to UNIFIED — but the (b-i) cross-functional spread persists regardless ⇒ no selection ⇒ FAIL. (Had the sub-test returned YES the openness would be UNIVERSAL ⇒ still no selection ⇒ FAIL. SELECTION PASS requires the SEPARATE event of a substrate-canonical collapse of (b-i), which did not occur.)

**4-tuple**: `(value='selection=PLURALISM|spread_OOM=1.259|struct_deriv=0|n_in_band=0|oom_impulse=0.86437/unified=0.196/parker=1.455', scheme=IMPULSE-QUENCH-BOGOLIUBOV-vs-UNIFIED-AS-79+PARKER-ADIABATIC, convention=OOM-SPREAD-AND-STRUCTURAL-DERIVATIVE, L_max=N/A)`.

**Full substitution chain (Steps 1–5, with substituted numbers)**:
- *Claim (sub-test direction)*: `aH|_fold` does NOT carry the a_0/a_2 SDW/Zubarev split; `d|β_k̂|²/d(a_0/a_2) = 0` (transit-trajectory-fixed).
- *Step 1 (Definitions)*: `|β_k̂|² = f(z''/z|_fold, Ω_z_on=1.2872, Ω_z_off=−1.2885, V_box=1.9028, Δη=0.00113, ξ_KZ)` [box-delta sudden, `beta2_pivot_closed_form = 3.0454e-07`, unitarity resid 1.87e-14]; `aH|_fold = a_fold_raw·H_fold/Λ_rescale = 386.024·586.527/232125.155 = 0.9753935` [corrected — see in-session correction]; `(a_0/a_2)|_horizon-exit` = SDW/Zubarev moment ratio carrying the 181× Path-B split [`a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389`]; `H̃ = 5.9076e-3 M_KK` [UNIFIED carrier].
- *Step 2 (Substitution)*: neither `f`'s argument list NOR `aH|_fold`'s definition contains `(a_0/a_2)|_horizon-exit`.
- *Step 3 (Simplify)*: `d|β_k̂|²/d(a_0/a_2) = Σ_inputs (∂f/∂input)·(d input/d(a_0/a_2)) = Σ_inputs (∂f/∂input)·0 = 0` [no input of `f` depends on the horizon-exit ratio]; independently `d(aH|_fold)/d(a_0/a_2) = 0` [`a_fold_raw·H_fold/Λ_rescale` is a fold-passage kinematic, EXACT rel-dev 0.0].
- *Step 4 (Direction read-off)*: `d|β_k̂|²/d(a_0/a_2) = 0` (computed exactly) ⇒ impulse-quench floor is a_0/a_2-INVARIANT ⇒ `aH|_fold` TRANSIT-TRAJECTORY-FIXED ⇒ the 181× openness CONFINED to the UNIFIED route. `sign_verdict = PASS`.
- *Step 5 (Selection conclusion)*: sub-test NO does not by itself SELECT a functional; the cross-functional spread (1.2590 OOM, none in-band) PERSISTS because three physically-defensible functionals of the same spectrum give three amplitudes and no substrate-canonical argument collapses them ⇒ SELECTION FAILS (PLURALISM-PERMANENT). **Informative**: PINS "A_s magnitude is a physical d.o.f. like the CC ratio" (the lizzi-signature; §EVOI.BF → "open, structurally").

**regulator_pin companion row**: `a_0^{ζ}/a_2^{ζ}` SDW/Zubarev 181× Path-B split (S82 Obs 6.3; poleconv-A-double; `a_0` n=0/s=4 cosmological-constant moment, `a_2` n=2/s=3 Einstein-Hilbert moment). Lives on the horizon-exit H̃ carrier, NOT the impulse-quench floor (`d|β|²/d(a_0/a_2)=0`).

**dual-SHA**: `audit_sha256 = 395f6800c8d143e440f5ad3ca54e14c902cfad1ec1f62ae8d465f1d2dc43cd71` (over [script, canonical, pinmap]); `content_sha256 = c3b007e002ab539252320a45236cf1ee703e8f0bd6980e1fd96e59011e5e76d1` (over [script]). **Runtime canonical drift**: `canonical_constants.py` runtime SHA `a4b8b679442de533…` ≠ plan-pin `9ee1a113b200f2ad…` (a sibling S114 gate promoted a constant mid-session); captured in the dual-SHA per `substrate-first-canonical-sourcing.md §(ii.B)`. The quantities this gate consumes (`A_s_FW` S111, `a_0/a_2_FW_zeta` S88, `xi_KZ_FW` S89, `H_fold` S38) all landed at-or-before S111 and are not S114-promotion candidates ⇒ no value-drift on consumed quantities.

**Solution-space interpretation**: this FAIL PINS §EVOI.BF from "open, may converge" to "open, structurally". The A_s magnitude-as-a-Planck-comparison-NUMBER is a genuine physical degree of freedom — like the a_0/a_2 cosmological-constant ratio. The floor-amplitude POINT (`A_s_FW = 1.5367e-08`, set by the TD source) and the floor INEQUALITY (`A_s ≥ A_s^BD`, permanent on 3 axes, S111 WS-AS-1 LIZ2-1) are UNTOUCHED by this FAIL. The >3-OOM liability is re-localized to the cross-functional + exit-greybody-filter (inv12 W3-4 FAIL) openness. Forward routing (per plan Wave 4 → Wave 5 Decision Point, FAIL branch): the capstone A_s conditional down-tag LANDS as "magnitude open, structurally — a physical d.o.f. like the CC ratio" (designated-writer patch, capstone-hygiene Q3 → `session-114-housekeeping.md`); `mack-cosmic-bridge` updates falsifier-master-inventory Row #12 / §EVOI.BF to "open, structurally" (sole-writer domain). No carry-forward emitted (CF-S115-AS-FUNCTIONAL-REGIME is emitted ONLY on an INFO outcome; this is a FAIL).

---

### §W4-2. CF-S113-B5A-TFD (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S113-B5A-TFD`
**Trigger**: `[SIGN]` (monotone in the TFD-accessible bulk-EE fraction: `dR_TFD/df_bulk > 0`)
**Classification**: **GEOMETRIC**
**Agent**: `hawking-theorist`
**Hypothesis**: The two-sided thermofield-double (TFD) island construction — doubling the white-hole exit-slice causal patch across the TFD purification partner — makes a larger fraction of the GGE island bulk-EE causally accessible than the single-sided exit slice (R≈0.53, edge-dominated, S112), and the TFD microstate count `S_TFD = Area(∂I_TFD)/4 + f_bulk^TFD·S_bulk-EE(I)` lands at the emergent area-law `A_horizon_FW/4` within 10% (`|R_TFD − 1| ≤ 0.10`). The R=1 crossing (`f* = 0.5536`) is FORBIDDEN as canonical (anti-tautology, diagnostic-only). Tier-3 NON-BLOCKING.
**Plan reference**: `sessions/session-plan/session-114-plan-w4.md` §W4-2 (3-band tolerance, anti-tautology fence, substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- (1) **Script** `computations/session-114/s114_cf_b5a_tfd.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` → both patterns match (L106 `from canonical_constants import (`; L162 `def print_verdict_payload(`).
- (2) **Data** `computations/session-114/s114_cf_b5a_tfd.npz` — present, non-stub (49 keys: canonical TFD landing, bracket endpoints, single-sided continuity, two-sided derivation, PASS/INFO bands, diagnostics, §(ii.B) drift disclosure).
- (3) **Plot** `computations/session-114/s114_cf_b5a_tfd.png` — present, non-stub (2-panel: R_TFD(f) interpolant with bands + cumulative bulk-EE vs λ with single/TFD/exit markers).
- (4) **Verdict line** `computations/session-114/s114_gate_verdicts.txt` — `^CF-S113-B5A-TFD:.* audit_sha256=[a-f0-9]{64}` matches; dual-SHA companion row present; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row present (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`); + §(ii.B) drift-disclosure row + regulator_pin row (5 rows total).
- (5) **WP section** this §W4-2 — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present.

**MCP Pre-Compute Audit**:
- `search_knowledge("B5A white-hole microstate TFD thermofield double island A/4 bracket")` → returned the S110-CF-B5A-MICROSTATE (R_edge=0.5263, FAIL), S111-CF-B5A-ISLAND (R_island=1.382, FAIL) gates + the s111_b5a_island.npz provenance. NOT pre-closed — the two-sided TFD route is the surviving corridor the plan dispatches.
- `get_constant("A_horizon_FW")` → 71226.26338976152 (S92, source S92-W8-CF-S92-T1-7-CF39); A_quarter = A_horizon_FW/4 = 17806.56584744038 confirmed.
- `search_knowledge("S112 B5A bracketed causal patch single-sided Mach 13.75 ...")` → confirmed Mach_max_framework = 13.75 (canonical L2467, S85); the S112 single-sided verdict line gives f_bulk=0.00396, R=0.5297, lambda_causal=0.9412, sbulk_causal=60.34, f*=0.5536 FORBIDDEN — all reproduced bit-for-bit in this gate's continuity cross-check.
- `c_conical` provenance: `0.2500001250001146` read directly from the `s111_b5a_island.npz` `c_conical` key (source inv4_w1_euclidean_replica.npz); NOT a canonical_constants entry — a_2^{Pauli-Villars} conical 2nd Seeley-DeWitt moment.
- Sage-MCP `sage_eval` (QQ-coerced) cross-check: `slope = R_island − R_edge = +0.8556794983884398 > 0` (directional claim exact), `f* = 0.5535685855247882`, `R_TFD = 0.534671524`, `|R_TFD−1| = 0.465328`, PASS band f∈[0.4367,0.6704] ≫ 2/M = 0.1455 ceiling.

**Verdict**: **FAIL** (composite). 3-tuple: **sign=PASS** (`dR_TFD/df_bulk = +0.8557 > 0`, gap-closing — the predicted direction), **magnitude=FAIL** (`|R_TFD − 1| = 0.4653 > 0.25` INFO ceiling), **regime=VALID** (`lambda_causal^TFD = 1.0626` strictly inside the island support `[0.8197, 2.4893]`; `f_bulk^TFD ∈ [0,1]`). Composite collapse: `magnitude=FAIL ∧ regime=VALID ⇒ FAIL`. Tier-3 NON-BLOCKING — does NOT gate any downstream wave or the session-close. **The FAIL is informative, not a defeat**: it CLOSES the "A/4 microstate count via a causally-derived bulk-EE fraction" corridor on BOTH the single-sided (S112) and two-sided-TFD routes.

**Results**:

| Quantity | Value | Source |
|:---------|:------|:-------|
| **R_TFD** (canonical) | **0.534672** | `R_edge + f_bulk^TFD·slope` |
| **\|R_TFD − 1\|** | **0.465328** | vs PASS 0.10 / INFO 0.25 ⇒ **FAIL** |
| `f_bulk^TFD` (DERIVED, two-sided) | 0.009757 | `cum_bulk(λ_causal^TFD)/sbulk_primary = 148.66/15236.71` |
| `f_bulk` single-sided (S112 continuity) | 0.003960 | reproduced bit-for-bit (assert < 1e-5) |
| `R` single-sided (S112 continuity) | 0.529711 | reproduced bit-for-bit (assert < 1e-5) |
| `λ_causal^TFD = λ_min + 2W/M` | 1.062586 | two-cone union, 2W/M = 0.242845 |
| `λ_causal^single = λ_min + W/M` | 0.941164 | one cone, W/M = 0.121422 |
| `R_edge` (S110 lower bracket) | 0.5263227104145511 | npz `R_edge_S110` (bulk-EE OMITTED) |
| `R_island` (S111 upper bracket) | 1.3820022088029909 | npz `R_island` (FULL island bulk-EE) |
| **slope = `dR_TFD/df` = R_island − R_edge** | **+0.8556794983884398 > 0** | sign_verdict=PASS source |
| `A_quarter = A_horizon_FW/4` | 17806.56584744038 | npz; 1e-9 rel-match vs canonical ✓ |
| `sbulk_primary` (island bulk-EE @ exit; f denom) | 15236.7133 | npz `sbulk_primary` |
| `S_bulk_total` (FULL spectral-support bulk-EE) | 180723.41563481884 | npz; **not** the bracket basis (see note) |
| `S_microstate^TFD` | 9520.66 | `R_TFD · A_quarter` |
| **`f*` (R=1 FORBIDDEN crossing)** | **0.5535685855247882** | DIAGNOSTIC-ONLY — never the canonical f_bulk |
| `c_conical = a_2^{Pauli-Villars}` | 0.2500001250001146 | npz; conical 2nd moment, Area(∂I)/4 normalization |

**The two-sided-TFD construction (substrate-first).** The acoustic white hole is a one-directional causal disconnect on each side (Mach-13.75 supersonic flow, PROVEN S85). The single-sided causal patch (S112) admits the sub-Mach cone subtending an eigenvalue window of width `W_island/M` from the spectral floor, capturing `sbulk_causal = 60.34` of 15236.71 nats → `f_bulk = 0.00396`. The TFD purification partner — the substrate's own two-sided eternal-white-hole geometry — supplies a SECOND cone; the island region `I` extends across both sides, so the causally-accessible bulk-EE is the UNION of the two cones, doubling the window reach to `2W_island/M`. This is the canonical island-formula doubling that reproduces the Page curve in two-sided geometries (the island contribution to `S_rad` doubles relative to the single-sided count; cf. the Hawking-information-paradox island-formula literature). The doubled window `λ_causal^TFD = 1.0626` captures `sbulk_causal^TFD = 148.66` nats → `f_bulk^TFD = 0.009757`.

**Substitution chain (`[SIGN]` trigger, MANDATORY — the `dR_TFD/df_bulk > 0` directional claim):**
- **Step 1 — Definitions:** `R_edge = S_boundary/(A/4) = 9372/17806.566 = 0.526323`; `R_island = [Area(∂I)/4 + S_bulk-EE(I)]/(A/4) = 1.382002`; `A_quarter = A_horizon_FW/4 = 71226.263/4 = 17806.566`; `f_bulk^TFD = S_bulk-EE(I_acc^TFD)/S_bulk-EE(I) = 148.66/15236.71 = 0.009757` (DERIVED from the two-sided TFD geometry, NOT tuned).
- **Step 2 — Substitution (no simplification):** `R_TFD(f) = R_edge + f·(R_island − R_edge) = 0.526323 + f·0.855679` (the same bracket interpolant S112 used, now with the two-sided `f_bulk^TFD` in place of the single-sided 0.00396).
- **Step 3 — Simplify (one step per line):** `dR_TFD/df = R_island − R_edge = 1.3820022088 − 0.5263227104 = 0.8556794984`.
- **Step 4 — Direction read-off:** `dR_TFD/df = +0.8557 > 0` ⇒ R_TFD strictly increasing in `f_bulk^TFD`. Since `f_bulk^TFD = 0.009757 > f_single = 0.003960`, `R_TFD = 0.534672 > R_single = 0.529711` (gap-closing toward A/4). **sign_verdict = PASS** (computed sign matches predicted +). Consistent with all three prior B5A verdicts' sign=PASS.
- **Step 5 — ANTI-TAUTOLOGY fence:** `R_TFD(f*) = 1 ⇒ f* = (1 − R_edge)/(R_island − R_edge) = 0.553569` — the FORBIDDEN crossing (the `f_bulk^TFD` that would hit A/4 BY CONSTRUCTION). Computed DIAGNOSTIC-ONLY; the canonical `f_bulk^TFD = 0.009757` is the substrate-derived two-sided fraction, NEVER `f* = 0.5536`. (Per the S112 B5A-BRACKETED precedent, which recorded exactly this crossing as forbidden.)

**Why the magnitude FAILs — the constraint-map content.** The PASS band requires `f_bulk ∈ [0.4367, 0.6704]`, i.e. capturing 44–67% of the 15236.71 nats of island bulk-EE. But the causally-accessible fraction from any sub-Mach patch at Mach 13.75 is at most a few percent: the sound-cone half-angle `sin θ_c = c_s/v_flow = 1/M ≈ 0.073` is tiny, so even the two-sided doubling (`2/M = 0.1455`) — and the most generous diagnostic reading `(D2) f_bulk = 2/M direct ⇒ R = 0.6508, |R−1| = 0.349` — falls short of the 0.4367 band floor. The two-sided TFD doubling is the RIGHT sign-correct move (R: 0.5297 → 0.5347, and up to 0.6508 under the most generous reading), but the white-hole causal patch at Mach 13.75 is simply too narrow, even doubled, to admit enough of the high-λ-concentrated GGE island bulk-EE to reach A/4. **In solution space: the "white-hole exit-slice microstate count = A/4 via a causally-derived bulk-EE fraction" corridor CLOSES on both the single-sided (S112, R≈0.53) and two-sided-TFD (this gate, R≈0.53) routes.** The A/4 microstate accounting would require a different (non-causal-patch) mechanism — e.g. a full two-sided island QES extremization rather than the linear bracket interpolant (the forward object), or the recognition that the emergent-area-law microstate count is not reconstructable from the exit-slice causal patch alone.

**Bracket-basis reconciliation (a load-bearing methodology note).** The plan Step-1 line names `S_bulk-EE(I) = S_bulk_total = 180723.4`, but the *bracket endpoint* `R_island = 1.382` was computed (S111) with `sbulk_primary = 15236.71` — the island-restricted bulk-EE up to the exit slice (λ ≤ λ_exit = 2.4893), NOT the full spectral-support `S_bulk_total`. The interpolant `R_TFD = R_edge + f·(R_island − R_edge)` therefore parametrizes the fraction `f` of the **island-restricted** 15236.71 nats — exactly the denominator S112 used (`f_bulk = 60.34/15236.71`). Using `sbulk_primary` (not `S_bulk_total`) as the f-denominator is REQUIRED for continuity with the pinned R_island bracket endpoint; the S112 single-sided continuity assertion (`f_bulk = 0.003960`, `R = 0.529711`) passes bit-for-bit, confirming the basis is correct. `S_bulk_total = 180723.4` is reported in the npz as the full-support reference but is NOT the bracket basis.

**Cross-checks.**
- **S112 continuity** (asserted in-script, < 1e-5): single-sided `f_bulk = 0.003960` and `R = 0.529711` reproduced exactly from the same `cum_bulk_at` interpolant + `sbulk_primary` denominator.
- **A_quarter = A_horizon_FW/4** rel-match < 1e-9 vs the canonical `A_horizon_FW = 71226.263` (Class-8.3-compliant: A_horizon_FW is full-float64, 1e-9 rel tolerance respects publication precision).
- **GPU monotonicity** (RX 9070 XT, torch): the cached L12 cumulative bulk-EE profile (166896 modes w/ multiplicity) is monotone-nondecreasing — confirmed True on-device.
- **Interpolation-basis artifact** (disclosed): `cum_bulk_at(λ_exit) = 15195.52` vs cached `sbulk_primary = 15236.71` differs by 0.27% (the 300-pt QES grid has no node exactly at λ_exit). This is inherited from the S111 npz and does NOT affect the canonical `f_bulk^TFD` (interp in numerator, cached `sbulk_primary` in denominator, identical to S112). The verdict is robust: even the most generous diagnostic (D2, R = 0.6508) is a FAIL.
- **Sage QQ-exact:** `slope`, `f*`, `R_TFD`, `|R_TFD−1|`, PASS band, 2/M ceiling all confirmed (see MCP Pre-Compute Audit).

**4-tuple output tag:** `(value=R_TFD=0.534672, scheme=TFD-ISLAND-TWO-SIDED-MICROSTATE-COUNT, convention=RATIO-DERIVED-TFD-CAUSAL-PATCH-FRACTION, L_max=12)`.

**Regulator pin** (companion row): `c_conical = 0.2500001250001146 = a_2^{Pauli-Villars}` — the conical 2nd Seeley-DeWitt moment (n=2 Einstein-Hilbert; Pauli-Villars-regulated conical-deficit replica normalization, the `Area(∂I)/4` boundary-term coefficient). DISTINCT regulator from W4-1's `a_2^{ζ}` spectral-action moment, per `regulator-pin-discipline.md` (the two `a_2` citations carry distinct regulator superscripts by construction).

**§(ii.B) plan-text-drift disclosure:** `canonical_constants.py` runtime SHA `a4b8b679442de533e176fc9f3eee9e6c2ea0077a94e2380c7a4f6510003867aa` ≠ plan-pin `9ee1a113b200f2ad9205881f21826dc4e7975008e049b9950e38882aca722639` (a sibling S114 gate promoted a constant mid-session). Per `substrate-first-canonical-sourcing.md §(ii.B)` the `audit_sha256` pins the RUNTIME state; the consumed values (`A_horizon_FW` S92, `Mach_max_framework` S85) are NOT S114 promotion candidates, so there is no value-drift on the consumed quantities. The `s111_b5a_island.npz` SHA matches the plan-pin (static file).

**Substrate framing (GEOMETRIC).** The white-hole microstate count is a property of the substrate's emergent causal/spectral geometry at the fold, not a laboratory-IN measurement. `D_K eigenvalues → GGE-relic island bulk-EE profile S_bulk-EE(λ) → S = Area(∂I)/4 + f_bulk·S_bulk-EE(I)`, with the area-law term normalized by the a_2 second Seeley-DeWitt moment (`c_conical`) and the emergent horizon area `A_horizon_FW`. Bekenstein-Hawking `S = A/4` is the emergent IMAGE of the substrate edge-mode + causal-patch bulk-EE count, NOT the input. The TFD doubling is the substrate's own two-sided eternal-white-hole geometry, not a holographic prescription imported from AdS/CFT. The arrow `D_K → S_bulk-EE → microstate count` is unchanged; the gate tested whether the two-sided causal-patch fraction is geometrically sufficient — it is not, closing the causal-patch corridor to A/4.

**Dual-SHA:** `audit_sha256 = b3a78eaec199238bd89c8ff865d72c062942a6263e232265d166c8a3b2304d21` (over [script ∥ canonical ∥ pinmap]); `content_sha256 = daca20d774a6d513644cb178c31a71eee5be3d60f62f52bdcd050e42ca277f25` (over [script]). Artifacts: `s114_cf_b5a_tfd.py/.npz/.png`.

---

## Wave 4 Synthesis (team-lead)

Two informative FAILs, each closing a residual magnitude-openness corridor. **W4-1 FAIL (FUNCTIONAL-PLURALISM PERMANENT)** — the post-transit A_s amplitude admits NO substrate-canonical functional selector. The structural sub-test `d|β_k̂|²/d(a_0/a_2) = 0` EXACT (the impulse-quench floor is a_0/a_2-invariant, transit-trajectory-fixed; `aH|_fold = 0.9753935` reproduced exactly from two independent kinematic routes), so the openness is CONFINED to the UNIFIED route — but the cross-functional spread (impulse-quench / UNIFIED-AS-79 / Parker = 1.2590 OOM, none in the Planck ±5% band) PERSISTS with no scheme-independent normalization ⇒ the A_s magnitude-as-a-Planck-comparison-NUMBER is a physical d.o.f. like the CC ratio. The floor POINT (`A_s_FW = 1.5367e-08`) and the floor INEQUALITY (`A_s ≥ A_s^BD`, permanent 3-axis) are UNTOUCHED. **W4-2 FAIL (Tier-3 NON-BLOCKING)** — the two-sided TFD doubling is the sign-correct move (`dR_TFD/df_bulk = +0.8557 > 0`, gap-closing) but the Mach-13.75 white-hole causal patch is too narrow even doubled (`|R_TFD − 1| = 0.4653 > 0.25`): the sound-cone half-angle `1/M ≈ 0.073` caps the causally-accessible fraction far below the PASS band [0.4367, 0.6704]. The "A/4 microstate count via a causally-derived bulk-EE fraction" corridor CLOSES on BOTH the single-sided (S112) and two-sided-TFD routes.

### (a) Numerical revisions
- W4-1: structural derivative `d|β_k̂|²/d(a_0/a_2) = 0.000000e+00` EXACT; cross-functional spread `1.2590 OOM` (impulse-quench +0.864 / UNIFIED +0.196 / Parker +1.455 vs Planck); `n_in_band = 0`.
- W4-2: `R_TFD = 0.534672`, `|R_TFD − 1| = 0.4653`; `dR_TFD/df = +0.8557`; `f_bulk^TFD = 0.009757` (doubled from single-sided 0.003960); forbidden R=1 crossing `f* = 0.5536` (diagnostic-only).

### (b) Structural changes
- A_s magnitude: `open, may converge → open, STRUCTURALLY (a physical d.o.f. like the CC ratio)` — the §EVOI.BF A_s axis re-typed (mack, Row #12 / §EVOI.BF).
- White-hole-microstate-via-causal-patch corridor: `surviving (two-sided-TFD route open) → CLOSED on both single- and two-sided routes` — A/4 microstate accounting needs a non-causal-patch mechanism (full two-sided island QES extremization, not the linear bracket interpolant).

## Carry-Forward Computations

No PRE-REGISTERED carry-forwards: both Wave-4 gates closed FAIL. The plan's conditional CFs were pre-registered to emit ONLY on an INFO outcome — `CF-S115-AS-FUNCTIONAL-REGIME` (W4-1 INFO) and `CF-S113-B5A-TFD-QES` (W4-2 INFO) — neither fired (both FAIL = closed corridors, not deferred computes per `Investigating-Workshops.md`).

**OPTIONAL planner-discretion forward objects (Q-other, NOT pre-registered CFs, NOT obligations).** Each closed corridor NAMES a forward object; per `Investigating-Workshops.md` a FAIL closes a corridor and is NOT a deferred compute, so these are surfaced for `/rclab-plan` S115 to weigh on EVOI merit (the planner may legitimately DROP either), NOT as workshop content and NOT as pre-registered obligations. Recorded here (mirroring the `/rclab-investigate` W4 seed) so the S115 planner sees the named objects without mistaking them for fired CFs.

### CF-S115-AS-NEWAXIS-SELECTOR (OPTIONAL, Q-other, low-priority — the planner MAY drop)

1. **What**: test whether a functional-determination principle NOT already exhausted by the three {impulse-quench, UNIFIED-AS-79, Parker-adiabatic} functionals (e.g. a maximum-entropy / Jaynes selection on the post-transit occupation, or a Connes-distance-canonical normalization of the relic spectral functional) collapses the 1.2590-OOM cross-functional A_s spread to one value.
2. **Inputs**: `s100b_box_delta_bogoliubov.npz` (the impulse-quench β² spectrum); the three functional A_s literals (impulse +0.864 / UNIFIED +0.196 / Parker +1.455 OOM); a candidate substrate-canonical selector spec.
3. **Gate**: PASS = selector collapses the spread → A_s becomes a typed one-functional prediction (retires the §EVOI.BF A_s liability); FAIL = no new-axis selector → FUNCTIONAL-PLURALISM-PERMANENT confirmed on a wider axis-basis.
4. **Effort**: ~1 wave. **Low priority**: §EVOI.BF already prices A_s magnitude as a permanent physical d.o.f.; this WIDENS the no-selector evidence, it does NOT change the headline. A genuine new derivation (a new structural claim on a new axis) ⇒ a COMPUTE gate if picked up, NOT a workshop.

### CF-S115-B5A-TFD-QES (OPTIONAL, Q-other, lowest-priority — the planner MAY drop)

1. **What**: replace the closed-form linear bracket interpolant `R_TFD = R_edge + f·(R_island − R_edge)` with a full two-sided island quantum-extremal-surface (QES) extremization of `S = Area(∂I)/4 + S_bulk-EE(I)` over the island boundary `∂I`, to test whether the A/4 microstate count is reachable by a NON-causal-patch mechanism (the surviving forward object after the causal-patch corridor closes on both single-sided + two-sided routes).
2. **Inputs**: `s111_b5a_island.npz` (L12 GGE bulk-EE profile, `R_edge`, `R_island`, `A_quarter`, `c_conical`); the L12 D_K spectrum cache for the QES variation.
3. **Gate**: `|R_QES − 1| ≤ 0.10` PASS / `≤ 0.25` INFO / `> 0.25` FAIL (the standard B5A 3-band).
4. **Effort**: ~1–2 waves (QES extremization is heavier than the interpolant). **Tier-3 NON-BLOCKING — internal-consistency corridor-narrowing, NOT an observational falsifier (no live falsifier row); LOWEST priority** — the causal-patch corridor closing is itself a clean result and the white-hole microstate count gates nothing downstream, so the planner may legitimately drop it.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-23 | W4-1 `CF-S114-AS-FUNCTIONAL-SELECTION` | A_s functional-selection open | **FAIL** — FUNCTIONAL-PLURALISM PERMANENT | sub-test=0 exact but 1.259-OOM spread persists; A_s magnitude = physical d.o.f. |
| 2026-06-23 | W4-2 `CF-S113-B5A-TFD` | A/4-via-two-sided-TFD surviving corridor | **FAIL** — A/4-via-causal-patch CLOSED (both routes) | TFD doubling sign-correct but Mach-13.75 patch too narrow; \|R_TFD−1\|=0.465 |
| 2026-06-23 | §EVOI.BF A_s axis | open, may converge | open, structurally (physical d.o.f.) | W4-1 FUNCTIONAL-PLURALISM PERMANENT (mack Row #12 / §EVOI.BF) |

Process observations: W4-1 carried an honestly-disclosed in-session correction (plan Step-1 `aH|_fold = H_fold/Λ_rescale` dropped the fold scale-factor; corrected to `aH = a_fold_raw·H_fold/Λ_rescale`, rel-dev 0.0 exact, corroborated by `k_pivot/(k/aH)|_fold` — strengthens the sub-test, recorded in the verdict companion row; in-session structural correction per `v3-closure-recovery.md` Class-1 boundary, NOT convention-shopping). W4-2 regulator pin `c_conical = a_2^{Pauli-Villars}` (distinct from W4-1's `a_2^{ζ}` per `regulator-pin-discipline.md`). Capstone A_s §8.5 reconciliation effected in-session (see `session-114-housekeeping.md §A7`); Row #12 / §EVOI.BF routed to mack (§A8).

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:--|:--|:--|:--|:--|
| W4-1 | `s114_cf_as_functional_selection.py` | ✓ | ✓ | FAIL (`395f6800…`) |
| W4-2 | `s114_cf_b5a_tfd.py` | ✓ | ✓ | FAIL (`b3a78eae…`) |
