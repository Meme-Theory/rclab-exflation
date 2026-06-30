# Session 112 — Planning Context (carry-forward corpus + register consumption)

**Mode**: fanout (per-wave plan + per-wave WP). **Planner default**: gen-physicist (cross-reviewer fallback; per-wave owner = reviewer-origin specialist). **Prompter**: gen-physicist. **PRIOR** = S111.

**Source manifest** (Phase 1b — carry-forwards lifted verbatim from the source `## Carry-Forward Computations` / housekeeping §B blocks; derivative-output citations inline):
- `sessions/session-111/session-111-w1-workingpaper.md` §"Carry-Forward Computations" (lines 442–462)
- `sessions/session-111/session-111-w2-workingpaper.md` §"Carry-Forward Computations" (lines 360–381)
- `sessions/session-111/session-111-w3-workingpaper.md` §"Carry-Forward Computations" (lines 256–268)
- `sessions/session-111/session-111-w4-workingpaper.md` §"Carry-Forward Computations" (lines 205–216)
- `sessions/session-111/session-111-w5-workingpaper.md` §"Carry-Forward Computations" (lines 346–366)
- `sessions/session-111/session-111-housekeeping.md` §B (lines 45–91) — the 4 Stage-2 verifies (mirrors of the WP CFs)

**S111 outcome** (from `computations/session-111/s111_gate_verdicts.txt`): 26 gates, 16 PASS / 7 INFO / 3 FAIL. The keystone result: `S111-CF-MKK-RG-INVARIANCE` FAILed as BARE-IMPORT (M_KK not τ-RG-invariant, CODATA-routed) — which *converts* the M_KK-derivation standing gap into a tractable S112 compute gate (CF-S112-MKK-SUBSTRATE-ANCHOR).

**EVOI staleness**: S2 advisory (currency S111 lags S112 by 1) → re-stamp at plan-freeze per 1c-REGISTERS.

---

## Carry-forward corpus (8 items, deduped)

| # | Gate ID | Wave | Executor (agent_type) | Source |
|:--|:--------|:-----|:----------------------|:-------|
| 1 | **CF-S112-MKK-SUBSTRATE-ANCHOR** | W1 | volovik-superfluid-universe-theorist | w2 WP 364 |
| 2 | **CF-S112-H0-BAND-CLOSURE** | W1 | mack-cosmic-bridge | w2 WP 373 (depends on #1) |
| 3 | **CF-S112-CLOCKLOC3-STAGE2** | W2 | 2 cross-reviewers (excl. schwarzschild-penrose, hawking) | w1 WP 446 / hk §B 47 |
| 4 | **CF-S112-NOHOLOFLUX-STAGE2** | W2 | 2 cross-reviewers (excl. einstein, loop-quantum-gravity) | w1 WP 455 / hk §B 58 |
| 5 | **CF-S112-M1-INTERTWINER-STAGE2** | W2 | 2 cross-reviewers (excl. connes-ncg, van-den-dungen) | w3 WP 260 / hk §B 69 |
| 6 | **CF-S112-VIICJ-STAGE2** | W2 | 2 cross-reviewers (excl. transit-dynamics) | w5 WP 359 / hk §B 80 |
| 7 | **CF-S112-B5A-BRACKETED** | W3 | hawking-theorist | w4 WP 209 |
| 8 | **CF-S112-FLOQUET3-HPAR-TIGHTEN** | W3 | transit-dynamics-theorist | w5 WP 350 |

---

## Full 4-field specs

### CF-S112-MKK-SUBSTRATE-ANCHOR — derive the dimensionful M_KK anchor from a substrate-natural scale (non-bare-import) `[KEYSTONE]`
*(source: w2 WP 364–371)*
- **What**: Find/derive a substrate-natural dimensionful scale that fixes M_KK WITHOUT importing CODATA and WITHOUT routing through M_Pl, then re-run the τ-RG-invariance two-leg test under that non-bare reading. This is the §6.3 a(t)/effective-Friedmann residual's remaining (magnitude) half.
- **Inputs**: `computations/session-111/s111_mkk_rg_invariance.npz` (BARE-IMPORT FAIL fingerprint: Δ_rel=8.193, leg1_RGinv=False, leg2_noimport=False, R_fold=1.6017e-01); the S110-CF-CV2A transmutation chain (`s110_cf_cv2a_mkk_transmut_promote.npz`); `canonical_constants.py` M_KK + the a₀/a₂ spectral moments.
- **Gate**: `leg1_RGinv=True` (M_KK τ-invariant under the new reading) AND `leg2_noimport=True` (no CODATA/M_Pl import) AND `Δ_rel < 5e-2`. PASS → §6.3 M_KK-magnitude leg CLOSES (and the H0 residual's held 93.875% becomes addressable); FAIL → magnitude leg is a permanent external-import boundary (narrate honestly in capstone).
- **Effort**: ~1–2 waves (M_KK origin is a hard substrate-physics problem; the keystone's open half).

### CF-S112-H0-BAND-CLOSURE — H0 full closure pending the M_KK-magnitude fix
*(source: w2 WP 373–381)*
- **What**: Re-test the H0-residual band closure once a substrate-natural M_KK anchor exists: the dimensionful `M_KK¹` scale leg INADMISSIBLE under the bare reading (parity-locked, `d_A=0` even) may become admissible if M_KK is substrate-derived, releasing the held 93.875%.
- **Inputs**: `computations/session-111/s111_cf3_h0_residual.npz` (partial_relief=49/800, residual_held=0.93875, a0_a2_orthogonal=True); output of CF-S112-MKK-SUBSTRATE-ANCHOR (UPSTREAM — proximate dependency).
- **Gate**: Band closes dimensionfully (`band_closed=True`) iff the M_KK anchor PASSes CF-S112-MKK-SUBSTRATE-ANCHOR; else residual stays held, H0 relief capped at the 6.125% dimensionless channel.
- **Effort**: ~0.5 wave (conditional re-run once the M_KK anchor lands).
- **Depends on**: CF-S112-MKK-SUBSTRATE-ANCHOR (UPSTREAM).

### CF-S112-CLOCKLOC3-STAGE2 — Stage-2 cross-axis verify of §VII.CG (r=16ε layer-obstruction)
*(source: w1 WP 446–453 / hk §B 47–56)*
- **What**: Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND of §VII.CG r=16ε layer-obstruction theorem (clauses (a) Level-2-clock typing, (b) ε[φ] Level-1-field requirement, (c) layer-obstruction no-go); also adjudicate the distinctness dual-prior (6th-INDEPENDENT 0.40 / structural-ROOT 0.60) vs the 5 VdD-Hawking arguments.
- **Inputs**: Registered §VII.CG entry (`sessions/permanent-results-registry.md:169`) — Level-1/Level-2 typing + ε=−Ḣ/H² single-field-slaving clauses. NO workshop transcript (Stage-2 without-prior-context per `joint-theorem-promotion.md`).
- **Gate**: Both reviewers PASS each single-axis clause AND JOINT clauses PASS-AND across both verdicts (logical AND). Axis-A causal-structure + Axis-B semiclassical-gravity; verifiers MUST NOT be schwarzschild-penrose-geometer or hawking-theorist (Stage-0 authors). PASS → STAGE-3-PERMANENT; any clause FAIL → stays STAGE-1-CANDIDATE.
- **Effort**: ~1 wave (2 parallel cross-reviewers + collation gate).

### CF-S112-NOHOLOFLUX-STAGE2 — Stage-2 cross-axis verify of §VII.CH (no-holonomy-flux root)
*(source: w1 WP 455–462 / hk §B 58–67)*
- **What**: Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND of the §VII.CH spectral-triple-no-holonomy-flux JOINT theorem (the three operator/parameter/causal projections + the single-root statement).
- **Inputs**: Registered §VII.CH entry (registry line 22231 body + line 170 master-index row); cites §VII.M.W10-3. NO workshop transcript.
- **Gate**: PASS-AND across both axes: Axis-A NCG-axiomatic (connes-ncg OR van-den-dungen) + Axis-B cosmological-bridge (mack OR volovik); verifiers MUST exclude Stage-0 authors einstein + loop-quantum-gravity (original-author exclusion + downstream-inheritance reach per Axis-B Selection Protocol). PASS → STAGE-3-PERMANENT.
- **Effort**: ~1 wave (2 parallel cross-reviewers + collation gate).

### CF-S112-M1-INTERTWINER-STAGE2 — Stage-2 cross-axis verify of §VII.CI (categorical two-conjunct obstruction)
*(source: w3 WP 260–268 / hk §B 69–78)*
- **What**: Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND of §VII.CI (conjunct (i) C*-algebra-type codomain-rank + Skolem-Noether foreclosure ∧ conjunct (ii) K-homology all-bridge-maps foreclosure). On PASS → STAGE-3-PERMANENT, which licenses the categorical upgrade of atlas-04 N7, §VII.W-3.SUBSTRATE, and atlas-08 Q10/Q9 from "obstructed-on-two-decidable-axes" to "categorically-obstructed-for-all-bridge-maps."
- **Inputs**: Registered §VII.CI entry (registry body 22267 + master-index row 171); conjunct artifacts `s111_m1_intertwiner_conjunct_i.npz` + `s111_m1_conjunct_ii_khomology.npz`; anchor gate S93-W2-1 ([φ_cd]=(0,0,0)). NO workshop transcript.
- **Gate**: Both reviewers PASS each single-axis conjunct AND complementary-conjunct JOINT PASS-AND across both verdicts. Verifiers MUST NOT be connes-ncg-theorist or van-den-dungen-bridge-theorist (Stage-0 authors); axis-distinct (Axis-A NCG/K-homology ≠ connes; Axis-B C*-algebra/representation ≠ vdd). PASS → STAGE-3-PERMANENT + the atlas/§VII.W-3 categorical upgrade; any conjunct FAIL → stays STAGE-1-CANDIDATE.
- **Effort**: ~1 wave (2 parallel cross-reviewers + collation).
- **Depends on**: §VII.CI STAGE-1-CANDIDATE landing (S111 W3-4 — COMPLETE).

### CF-S112-VIICJ-STAGE2 — Stage-2 cross-axis verify of §VII.CJ (McLachlan cutoff-robustness exponent)
*(source: w5 WP 359–366 / hk §B 80–89)*
- **What**: Stage-2 two-agent NON-AUTHOR cross-axis PASS-AND of §VII.CJ (the n-th Mathieu tongue half-width has leading power EXACTLY n on q ⇒ §VII.BP DEAD L_max-robust). The EXPONENT n is the registered claim (prefactors diagnostic-only). On PASS → STAGE-3-PERMANENT.
- **Inputs**: Registered §VII.CJ entry (registry body 22301 + master-index row 172); `inv12_w3_2_floquet_ordered_veil_resonance.npz` (A_relic, q_relic, nearest_n); the s84 L12 master cache; the McLachlan/DLMF-28.6 characteristic-value series. NO workshop transcript.
- **Gate**: Both reviewers PASS the single-axis + JOINT clauses (logical AND). Verifiers MUST NOT be transit-dynamics-theorist (Stage-0 math owner). PASS → STAGE-3-PERMANENT; FAIL → stays STAGE-1-CANDIDATE.
- **Effort**: ~1 wave (2 parallel cross-reviewers + collation).

### CF-S112-B5A-BRACKETED — bracketed white-hole microstate count
*(source: w4 WP 209–216)*
- **What**: The white-hole horizon microstate count is now TWO-SIDED bracketed: S110-CF-B5A-MICROSTATE (edge-only) undershoots A/4 (ratio ~0.47–0.53); S111-CF-B5A-ISLAND (island + GGE bulk-EE) overshoots (R_island=1.382). Find the prescription/parameter (e.g. the correct island region ∂I or the GGE bulk-EE truncation) that lands the ratio at unity. Both prior verdicts have sign=PASS (correct direction), so the corridor is bracketed, not closed.
- **Inputs**: `computations/session-111/s111_b5a_island.npz` (R_island=1.382, S_island=24608.7, R_span=1.082–1.382, c_conical=0.25); S110-CF-B5A-MICROSTATE verdict (edge-only ratio); `canonical_constants.py`: `A_horizon_FW = 71226.26` (A/4 = 17806.57); `inv4_w1_euclidean_replica.npz` (c_conical, a_2^{Pauli-Villars} regulator-pin).
- **Gate**: `|S_microstate/(A_horizon_FW/4) − 1| ≤ 0.10`. PASS → microstate count lands at the area-law value (S110 factor-2 undercount fully closed); FAIL/INFO → corridor remains two-sided-bracketed with residual quantified.
- **Effort**: ~1 wave (parameter interpolation/refinement between the two bracketing prescriptions; no new machinery).

### CF-S112-FLOQUET3-HPAR-TIGHTEN — pin h_par to 10% via a physical late-time V_eff
*(source: w5 WP 350–357)*
- **What**: Re-derive δτ_amp (hence h_par) by re-integrating the coupled modulus + Friedmann ODE with a PHYSICAL late-time effective potential (S66 Volovik-tracking V_eff) that settles at τ_fold instead of running away — closing the regime=MARGINAL gap. NON-BLOCKING (§VII.BP DEAD unaffected — every h_par reading ≪ DTC threshold).
- **Inputs**: `computations/session-111/s111_cf_floquet3_dtau_amp_afterglow.npz` (δτ_amp=1.84e-3, d ln E²/dτ=0.150, Q=0.47, h_par_derived=2.76e-4); the S73B trajectory; the S66 Volovik-tracking V_eff; the S101-W1 guard-floor pin 8.3e-4.
- **Gate**: `|h_par_derived − 8.3e-4| / 8.3e-4 ≤ 0.10`. PASS → h_par upgraded asserted→substrate-derived at 10%; FAIL/INFO → corridor stays narrowed, residual quantified.
- **Effort**: ~1 wave (one coupled-ODE re-integration with the physical V_eff).

---

## Register-sourced candidates (1c-REGISTERS.CONSUME)

Dedup vs the 8 carry-forwards above, then EVOI-tier order. The dominant register finding: the high-leverage EVOI standing gaps are mostly **no-tractable-compute-gate** items → they route to the **S112 EVOI-frontier WORKSHOP SCHEDULE** (the `--extra` deliverable, `sessions/session-112/session-112-workshop-schedule.md`), NOT compute waves. Per `Investigating-Workshops.md §"Cross-references"`, the workshop schedule and the compute carry-forward queue are SEPARATE streams.

- **M_KK-DERIVATION** — was the top standing gap; **now PROMOTED to a Wave-1 compute gate** (CF-S112-MKK-SUBSTRATE-ANCHOR) because S111's MKK-RG FAIL gave it a pre-registrable test. Its *interpretation* (τ-RG-invariant derivation vs bare freeze) is covered by the compute gate, NOT a duplicate workshop.
- **Routed to the workshop schedule (no tractable compute gate)**: atlas-04 C2 K_pivot · residual-3% CC + BBN-epoch arm Q29 · τ_fold-RELAXATION (Tier-2 #4) · 170× DM-mass anchor (HK-170X-DM) · A_s magnitude / CF21 TD-LI H̃-divergence · the §EVOI.BF CMB-orthogonal observational steer (NICER EoS / DESI-Euclid f·σ8) · the homogeneity-obstruction SHAPE branch (#9b).
- **GRAVITON-2TO2** (EVOI Tier-3 #13, OPEN, tractable) — register-sourced COMPUTE candidate (compute a 2→2 graviton amplitude from the spectral action, check unitarity). NOT a carry-forward; LOW-MED leverage; flagged as an OPTIONAL Wave-3 add-on. Default: deferred (compute plan focuses on the 8 tractable carry-forwards); promote only on user request.
- **K8 §VII.AF.1.STATE-PROJ** — PENDING-VERIFICATION structural-cohort holdout; no dispatch-ready Stage-2 gate (deliberately not-lifted). Standing.

---

## Workshop track (--extra): EVOI-frontier dive, modeled on S110

The user's `--extra` directive: "include a workshop-schedule to dive into EVOI items again (similar to session 110)." S110 dove into the M_KK-derivation keystone via a structural-support investigation + 8 workshops; the M_KK gate is now in the compute plan, so the S112 workshop schedule attacks the *remaining* high-leverage standing gaps (the "leverage ≠ tractability" frontier). Deliverable authored at plan-freeze: `sessions/session-112/session-112-workshop-schedule.md` (orchestrator-authored, register-grounded; the genuine adversarial tensions selected per `Investigating-Workshops.md` Q1 four-condition definition).
