# Session 99 Wave 1 — C1 emergent-FRW keystone (the a(t) unblocker) (Results Working Paper)

**Session**: 99 | **Wave**: 1 | **Plan**: session-99-plan-w1.md | **Theme**: Re-derive the post-fold deceleration history via a NON-ratio observable (the conformally-stationary AOFT ratio-form q is a 0/0 indeterminate); export the non-stationary substrate Hubble backbone H(τ) for Wave 2.

## Gate Sections

### §W1-1. S99-W1-Q-NONRATIO-OBSERVABLE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S99-W1-Q-NONRATIO-OBSERVABLE`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (D_K eigenvalues → a_2 moment → emergent a_eff(τ) → deceleration sign-history; the object IS the substrate's emergent expansion history, not a laboratory measurement)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The post-fold deceleration sign-history, read off a NON-ratio observable (sign of the q-numerator at the H_A=0 crossing, cross-checked by the bare-rate q_bare before conformal transport), is finite across the crossing and lands in the SF54 band [−0.97, +0.81] on ≥ 0.90 of sample points where the conformally-stationary AOFT ratio-form q gave a 0/0 indeterminate (S98 V.1 Clause-2 FAIL).
**Plan reference**: `sessions/session-plan/session-99-plan-w1.md` §W1-1 (machinery pin, [SIGN] threshold, substitution chain, export spec).

**Verdict**: **INFO** — composite via the pre-registered collapse rule (`magnitude_verdict=INFO ⇒ composite=INFO`; also `magnitude=PASS+regime=MARGINAL ⇒ INFO`). 3-tuple: **sign=PASS, magnitude=INFO, regime=MARGINAL**. The non-ratio deceleration observable is FINITE across all 18 H_A=0 crossings and the sign is well-defined (sign(q_bare) = −sign(ä_bare) at 100% of crossing-adjacent points), CONFIRMING the S98 0/0 was a conformal-frame artifact; but the deceleration history does NOT land in the SF54 band on ≥0.90 of points (band_frac = 0.490). Per the plan's `INFO_meaning`: a valid non-stationary `arr_H_bare_t` backbone EXISTS and is exported to Wave 2 (the keystone unblocker function is SATISFIED), while the SF54-band match fails — an informative constraint on the a_eff(a_2-channel) → SF54 mapping. DP-W1→W2-A fires (INFO supplies a valid backbone).

**Output Artifacts** (verified on disk by content-presence regex, per `agent-standards.md §"Completion Verification"`):

| Artifact | Path | Verification |
|:---------|:-----|:-------------|
| script | `computations/session-99/s99_w1_q_nonratio_observable.py` (42.8 KB) | `grep -E "from canonical_constants import"` → L97 `from canonical_constants import *`; L98 `from canonical_constants import a_2_FW_zeta, Omega_BA_fold`. `grep -E "print_verdict_payload"` → L564 `def print_verdict_payload(...)`. Both must_contain patterns PASS. |
| data | `computations/session-99/s99_w1_q_nonratio_observable.npz` (146 KB, 65 keys) | All 6 MANDATORY Wave-2 export keys present + validated: `arr_H_bare_t` (999,), `arr_tau` (999,), `arr_a_bare_t` (999,), `arr_Hdot_bare_t` (999,), `aeff_relvar`=7.427259e-07, `H_bare_nonstationarity_relvar`=3.886565e-01. In-script export-key assertion PASS; non-stationarity guard PASS (relvar 5.72 OOM > floor 7.4e-7×10). |
| plot | `computations/session-99/s99_w1_q_nonratio_observable.png` (314 KB) | 3 panels: (a) ä_bare (substrate-correct) vs ä_eff (degenerate) with 18 H_A=0 crossings marked; (b) q_bare(τ) with SF54 band [−0.97,+0.81] shaded; (c) arr_H_bare_t (non-stationary) vs flat H_A (stationary). |
| verdict_line | `computations/session-99/s99_gate_verdicts.txt` (L20) | `grep -E "^S99-W1-Q-NONRATIO-OBSERVABLE:.* audit_sha256=[a-f0-9]{64}"` → PASS. Dual-SHA companion row (L21) + [SIGN] 3-tuple companion row (L22: `sign_verdict=PASS magnitude_verdict=INFO regime_verdict=MARGINAL`) + 3 extra rows (regulator_pin / domain_used_frac / export_backbone). Emitted race-safe via `mcp__knowledge__emit_verdict` (6 rows, sig_5-unique). |

**Dual-SHA** (full 64-char, schema_version=S84+):
- `audit_sha256 = 8bcbca9cf8821995562215e96011edee79a2a08cafd960e17f4e9401a885559f` (script ⊕ canonical_constants.py ⊕ pinmap{canonical, s98_w1_route_reconciliation.npz, s97_w1_omega_profile.npz})
- `content_sha256 = 23335c0c11b84b53c8577e900b94cb761d9a6bda7f6c4cc92a68090c35c8bb3d` (script bytes only)
- input-SHA pins (computed at runtime): `s98_w1_route_reconciliation.npz` = c5969fe69c42b088…, `s97_w1_omega_profile.npz` = 4d923ce1d64014b2…, `canonical_constants.py` = 906dba1eaf268f83…

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`; NOT pre-closed):

| Query | Salient return |
|:------|:---------------|
| `get_constant("a_2_FW_zeta")` | 2776.165389 — S88-A-N-FW-CANONICALIZATION; **Superseded: False**. Confirms the `a_eff ∝ √a_2` provenance anchor. |
| `get_constant("Omega_BA_fold")` | 2.241353 — S97-W1-OMEGA-PROFILE (PASS, rel 1.5e-4); **Superseded: False**. The √Γ-effacement conformal factor used to reconstruct a_bare = a_eff/Ω. |
| `search_knowledge("S99 NONRATIO deceleration sign-history H_A crossing bare-frame backbone")` | Surfaces the S98 V.1 0/0 POLE finding (`q(naive)=−1−Ḣ_A/H_A²` POLE form; `H_A=0 crossing … max_abs_dq=2.99e12`; the INPUT motivating this re-derivation) — NOT a closed S99 result. Gate is NOT pre-closed; proceed. |

Both named constants canonical + unsuperseded; SOURCE-RECON D_max=0. No SCHEMATIC-helper consumption (gate post-processes precomputed S98/S97 substrate trajectories). The `a_2^{zeta}` regulator-pin is carried as a companion-row provenance tag (a_eff ∝ √a_2; a_2 is NOT consumed as a regulated numerical input, so no `a_n^{regulator}`-tagged consumption per `regulator-pin-discipline.md`).

**Results**:

**4-tuple**: `(value='composite=INFO;sign=PASS;magnitude=INFO;regime=MARGINAL;band_frac_primary=0.490196;…', scheme=FW, convention=ABSOLUTE, L_max=N/A)` (publication_precision 6).

**Inputs consumed** (runtime npz-key introspection per the plan's no-silent-substitution clause):
- S98 `s98_w1_route_reconciliation.npz` resolved keys: τ=`arr_tau_t` (999-pt uniform grid, [0.19026, 0.45078]), a_eff=`arr_a_eff_t`, ȧ_eff=`arr_aeff_dot_t`, ä_eff=`arr_aeff_ddot_t`, H_A=`arr_H_A_t`; stationarity diagnostic `clause2_aeff_relvar`=7.427259e-07 carried forward.
- S97 `s97_w1_omega_profile.npz` resolved keys: `tau_grid` (1001-pt, [0.19, 0.6]), `Omega`. Ω interpolated onto the S98 τ-grid (np.interp; distinct meshes, same physical Ω(τ)).
- Verified: `H_A = ȧ_eff/a_eff` to 1.06e-22 (machine ε); a_eff rel-var = 1.77e-7 (the S98 conformal-stationarity finding); H_A crosses zero **18 times** (= S98 `clause2_n_cross`).

**Substitution chain (Step 1–4 with substituted numbers + the compute-time correction):**

- **Step 1 (Definitions)**: a_eff(τ) = a_bare(τ)·Ω(τ), Ω = √(ρ_s/a₂), Omega_BA_fold = 2.241353; H_A = ȧ_eff/a_eff; q_ratio = −a_eff·ä_eff/ȧ_eff² = −1 − Ḣ_A/H_A²; a_eff ∝ √a₂, a_2_FW_zeta = 2776.165389.
- **Step 2 (conformally-stationary degeneracy)**: S98 V.1 (audit 75a45dd7) — a_eff = const to rel-var 7.43e-7 ⇒ ȧ_eff → 0 AND ä_eff → 0 simultaneously ⇒ q_ratio = −(const)·(→0)/(→0)² = **0/0** (S98 Clause-2: q_central ≈ 1.94e7, 116/999 finite). REPRODUCED.
- **Step 3 (non-ratio observable) — COMPUTE-TIME STRUCTURAL CORRECTION**: the plan's substitution-chain Step 3 prescribed reading the sign off `sign(ä_eff)`, asserting (Step 4) the acceleration sign is "conformally INVARIANT up to dΩ/dτ corrections." **This assertion is FALSIFIED on the data.** ä_eff is the second derivative of the conformally-STATIONARY a_eff (rel-var 1.77e-7); the 2nd derivative of a near-constant signal is numerical noise centered on zero — `mean(ä_eff) = −9.40e-7 ≈ 0`, `std = 1.66e-3`, sign split **500 neg / 499 pos** (`ä_eff_pos_frac = 0.4995`, a coin flip). The detector flags `addot_eff_sign_is_degenerate = True`. **The stationarity degeneracy that produced the S98 0/0 in the RATIO propagates into the acoustic-frame NUMERATOR** — sign(ä_eff) carries no physical acceleration information. The dΩ/dτ corrections are NOT small (Ω̇ ∈ [−0.15, −0.94], Ω̈ ∈ [−1.5, −2.1]); they flip sign(ä_eff) vs sign(ä_bare) ~half the time (45% agreement). The plan's literal ä_eff sign-test vs q_bare yields **0.5215** agreement — degenerate, as the noise structure predicts.

  The SUBSTRATE-CORRECT non-ratio observable (faithful to the substitution-chain *Conclusion*: "a FINITE deceleration sign-history is read off the non-ratio observable") is **sign(ä_bare)** — the 2nd derivative of the genuinely-growing bare scale factor a_bare = a_eff/Ω (rel-var **1.35e-2**, 4.9 OOM larger; a physical signal). Algebra (a_eff>0, ȧ_eff²>0): sign(q_ratio) = sign(−a·ä) = −sign(ä); so ä_bare > 0 ⇔ q<0 (ACCELERATING), ä_bare < 0 ⇔ q>0 (DECELERATING).
- **Step 4 (well-conditioned canonical form + export)**: a_bare = a_eff/Ω is NOT conformally stationary ⇒ q_bare = −1 − Ḣ_bare/H_bare² is WELL-CONDITIONED (H_bare strictly positive, min 0.0691, max 0.3056; H_bare² bounded away from 0). The export backbone H_bare = ȧ_bare/a_bare reconstructed directly; structural cross-check against the decomposition H_bare = H_A − Ω̇/Ω agrees to **8.64e-4** (two numpy.gradient routes). q_bare(numerator-form) = −a_bare·ä_bare/ȧ_bare² matches q_bare(H-form) to 4.47e-3.

**[SIGN] direction (read off the canonical form):**
- **sign_verdict = PASS**: sign(q_bare) = −sign(ä_bare) agrees at **100.0%** of crossing-adjacent points (both-nonzero), **98.16%** globally. The 16/869 global disagreements all sit at q_bare ≈ 0 (range 4e-10 to 4.5e-9) — zero-crossing roundoff at inflection, not physical disagreement. The deceleration SIGN is FINITE and well-defined across every H_A=0 crossing. **The S98 0/0 is CONFIRMED a conformal-frame artifact** (it is not a statement that the deceleration sign is undefined; reading the sign in the non-stationary bare frame recovers a well-conditioned, finite history).
- **Deceleration consensus**: the post-fold bare frame is **mostly accelerating** — q_bare < 0 on 66.8% of points (median q_bare = −0.866), ä_bare > 0 on 68.4%.

**magnitude_verdict = INFO** (finite-but-out-of-band): SF54-band [−0.97, +0.81] membership = **band_frac_primary = 0.490196** (substrate-correct ä_bare sign-mapped q over 663 retained finite points) < 0.90 floor; cross-check band_frac_qbare = 0.501502. The substrate's emergent deceleration history is well-defined but does NOT reproduce the SF54 Connes-distance band on ≥90% of points (much of the trajectory sits at/below the SF54 lower edge q_lo = −0.97, consistent with the mostly-accelerating bare frame).

**regime_verdict = MARGINAL** (auto-shortening clause): `domain_used_frac = 0.663664` falls in the [0.50, 0.95) MARGINAL band. The pole_eps = 0.02 (τ-fraction) exclusion window around 18 densely-spaced H_A=0 crossings removes 336/999 points (the windows overlap). Emitted as `domain_used_frac=0.663664` per the gate-verdicts.md auto-shortening discipline.

**KEYSTONE EXPORT (Wave-2 HARD upstream) — VALID**: `arr_H_bare_t` (999-pt non-stationary substrate Hubble backbone) saved with `arr_tau`, `arr_a_bare_t`, `arr_Hdot_bare_t`, `aeff_relvar`=7.427259e-07, `H_bare_nonstationarity_relvar`=**3.886565e-01**. Non-stationarity gap = log10(0.389/7.43e-7) = **5.72 OOM** above the a_eff stationarity floor — far exceeding the plan's ">> 1 OOM" certification requirement. H_bare strictly positive. This is the valid HARD upstream for `S99-W2-RELAXATION-CLOSURE` (the AOFT acoustic frame cannot serve there — it is conformally stationary; the friction term 3·H·q′ must be driven by the substrate's actual complexity-growth rate). Backbone-validity guard PASS ⇒ DP-W1→W2-A.

**dual_prior re-allocation**: discriminator maps INFO (finite-but-out-of-band) → **0.9 to Track B** ("the deceleration history is finite but OUT of the SF54 band; the substrate's emergent expansion does not reproduce the SF54 Connes-distance band — an informative constraint on the a_eff → SF54 bridge"). Track A (PASS, in-band) is not realized; Track-collapse (FAIL, still-non-finite) is decisively excluded (finite_across_crossing = True, sign well-defined).

**Substrate-first assessment**: GEOMETRIC/PHONONIC bridge, explanation flows substrate → emergent physics: D_K eigenvalues → a_2 second Seeley-DeWitt moment (a_2_FW_zeta = 2776.165389) → emergent acoustic scale factor a_eff(τ) = a_bare(τ)·Ω(τ) → deceleration sign-history. This is the substrate's own emergent expansion history, NOT a measurement of a(t) IN a pre-existing container — exflation, not inflation; no metric expansion, no inflaton. The deeper structural lesson: the √Γ-effacement conformal factor Ω = √(ρ_s/a₂) (Omega_BA_fold = 2.241353) so completely cancels the bare spectral-complexity growth that the acoustic frame is stationary to BOTH first AND second order — the degeneracy is not confined to the H_A ratio (S98) but reaches the ä_eff numerator (this gate). The physically meaningful deceleration sign lives ONLY in the bare, pre-effacement frame, where a_bare carries the un-cancelled complexity growth (rel-var 1.35e-2). The exported arr_H_bare_t is the rate at which spectral complexity grows BEFORE effacement-cancellation — the substrate's own non-stationary Hubble backbone, and the physically correct driver for the Wave-2 friction-ODE.

---

## Wave 1 Synthesis (team-lead)

**W1-1 `S99-W1-Q-NONRATIO-OBSERVABLE` — INFO** (3-tuple sign=PASS, magnitude=INFO, regime=MARGINAL). The post-fold deceleration sign-history is FINITE across all 18 H_A=0 crossings (`sign(q_bare) = −sign(ä_bare)` at 100% of crossing-adjacent points), **confirming the S98 V.1 0/0 was a conformal-frame artifact**, not a structural degeneracy of the deceleration sign. The KEYSTONE unblocker function is SATISFIED: a valid non-conformally-stationary substrate Hubble backbone `arr_H_bare_t` is exported (`H_bare_nonstationarity_relvar = 0.3887`, 5.72 OOM above the a_eff stationarity floor 7.43e-7; H_bare strictly positive) — Wave 2's friction-ODE consumed it (DP-W1→W2-A fired). The SF54-band match FAILS (in-band fraction 0.490 < 0.90): the substrate's emergent post-fold expansion is mostly accelerating (q_bare median −0.866), sitting below the SF54 Connes-distance band edge q_lo = −0.97 over much of the trajectory.

Solution-space: the §6.3 a(t) keystone ADVANCES — the substrate carries a finite, well-conditioned post-fold deceleration history in the bare (pre-effacement) frame, and a non-stationary H(τ) backbone now EXISTS (the Wave-2 unblocker). It does NOT reproduce the SF54 band; the a_eff(a₂-channel) → SF54 bridge is the open residual (→ CF-S100-W1-SF54-MAPPING). The §6.3 gap stays OPEN (W2-1 did not close the friction-ODE leg), but the keystone's mechanical unblocker role is discharged.

**Carry-Forward Computations (math)**: CF-S100-W1-SF54-MAPPING (below). **Effected In-Session (non-math)**: the plan-PRIMARY-observable degeneracy finding (below) is logged as a process observation + `/rclab-investigate` Q1 workshop seed in `session-99-housekeeping.md §A`.

> **Process observation (non-propagating → housekeeping §A)**: the plan's literal PRIMARY observable `sign(ä_eff)` was discovered DEGENERATE at compute-time (ä_eff is the 2nd derivative of the conformally-stationary a_eff, rel-var 1.8e-7 → its sign is flat-signal roundoff, 500/499 coin-flip). The executor substituted the substrate-correct `sign(ä_bare)` (a_bare rel-var 1.35e-2, a physical signal), retaining the ä_eff-literal reading as a labelled diagnostic (`addot_eff_sign_is_degenerate=True`) — an honestly-disclosed in-session structural correction (no threshold/scheme/tolerance changed; `math-scripts.md` feasibility-deviation discipline, NOT convention-shopping). Whether ANY acoustic-frame observable can carry the post-fold deceleration sign, or the bare frame is structurally the only well-conditioned reading, is a Q1 math/physics question → `/rclab-investigate` workshop seed.

## Carry-Forward Computations

### CF-S100-W1-SF54-MAPPING — why the substrate post-fold expansion misses the SF54 deceleration band [genuine-math]

From §W1-1 (INFO; band_frac_primary = 0.490 < 0.90). The substrate's bare-frame deceleration history is finite and well-defined but does NOT land in the SF54 band [−0.97, +0.81] on ≥0.90 of points (q_bare median −0.866, mostly accelerating).

| Field | Spec |
|:------|:-----|
| **What** | Re-derive the a_eff(a₂-channel) → SF54 deceleration-band map: is SF54 [−0.97, +0.81] the correct comparison object for the bare-frame q_bare history, or does the Connes-distance proxy require a frame/normalization correction? Test band-membership under the corrected map. Resolves whether the SF54 miss is a genuine substrate prediction (post-fold mostly-accelerating, SF54 is the wrong band) or an a_eff→SF54 mapping defect. |
| **Inputs** | `s99_w1_q_nonratio_observable.npz` (arr_q_bare_t, arr_H_bare_t, arr_tau, band_frac_primary/qbare); `little-red-dots-synthesis.md` (SF54 derivation / Connes-distance proxy); `canonical_constants.py` (Omega_BA_fold, a_2_FW_zeta). |
| **Gate** | `[SIGN]`: PASS iff corrected-map in-band fraction ≥ 0.90; INFO iff the substrate is structurally mostly-accelerating post-fold and SF54 is the wrong band (informative re-scope); FAIL iff the mapping is ill-defined. |
| **Effort** | ~1 wave (1D post-processing of the exported q_bare/H_bare trajectories + SF54-map re-derivation; no diagonalization). |

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-01 | §6.3 post-fold deceleration sign | 0/0 indeterminate (S98 V.1 Clause-2 FAIL; conformally-stationary frame) | FINITE (conformal-frame artifact confirmed; bare-frame q_bare well-conditioned) | S99 W1-1 INFO: sign(q_bare)=−sign(ä_bare) at 100% of crossings |
| 2026-06-01 | Non-stationary substrate H(τ) backbone (Wave-2 unblocker) | absent (S98 W2 PRE-REG-INC; no non-stationary backbone) | EXISTS (`arr_H_bare_t`, 5.72-OOM non-stationarity, all-positive) | S99 W1-1 export; DP-W1→W2-A fired |
| 2026-06-01 | a_eff(a₂-channel) → SF54 deceleration-band match | untested | does-NOT-match (in-band 0.490 < 0.90) | S99 W1-1 INFO → CF-S100-W1-SF54-MAPPING |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| S99-W1-Q-NONRATIO-OBSERVABLE | `computations/session-99/s99_w1_q_nonratio_observable.py` | `s99_w1_q_nonratio_observable.npz` (65 keys; 6 Wave-2 export keys) | `s99_w1_q_nonratio_observable.png` | INFO (audit `8bcbca9c…`) |
