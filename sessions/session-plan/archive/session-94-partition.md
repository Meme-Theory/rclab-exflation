# Session 94 — Partition Manifest (fanout)

**Generated**: 2026-05-25 (`/rclab-plan --session 94`, Phase 1c)
**Context (authoritative scope)**: `sessions/session-plan/session-94-context.md`
**Sources**: session-93 (10-wave compute) + session-x (9-wave aggregate-expansion) carry-forwards — dual-source per `--extra` directive.
**Mode**: fanout — per-wave plan + per-wave WP shell.

**Totals**: 8 waves, 25 gates, ≈16.9 wave-equivalents. Dispatch the 8 per-wave planners in ONE batch (≤8 concurrent per `feedback_dispatch-discipline.md`).

| Wave | Theme | Owner (planner + default executor) | Gates |
|:----:|:------|:-----------------------------------|:-----:|
| W1 | §VII.BA composite-bridge + α_s transport + A_s normalization | `connes-ncg-theorist` | 5 |
| W2 | §VII.AU winding / 3He-B BDI Level-3 / α=−3 Layer-1 | `connes-ncg-theorist` | 3 |
| W3 | Pati-Salam SU(4)_PS Level-3 + module-as-canonical K3 + §VII.AZ re-extraction | `connes-ncg-theorist` | 3 |
| W4 | Stage-2 joint-theorem cross-axis promotions | `gen-physicist` | 2 |
| W5 | PBH truncation/band-breach + BAO-peak observational | `mack-cosmic-bridge` | 3 |
| W6 | methodology / K-counter / audit-script / a_n-retrofit | `gen-physicist` | 5 |
| W7 | spectral-dimension v_g^B2 discriminator + LQG narrow-path cocycle | `phonon-first-cosmologist` | 2 |
| W8 | §VII.AV Stage-2 re-verify + §VII.AR PASS-A substrate-derivation | `volovik-superfluid-universe-theorist` | 2 |

---

## Wave 1 — §VII.BA composite-bridge + α_s transport + A_s normalization

- **Owner**: `connes-ncg-theorist` (NCG/spectral-action; §VII.BA + α_s Mellin-residue + a_2-moment normalization)
- **Reviewer-origin**: S93 W1 (connes) + S93 W7 (connes) + session-x W1 (A_s)
- **Items** (5):
  - `CF-S94-W1-A` → `S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY` — §VII.BA Stage-2 cross-axis verify (STAGE-1 → STAGE-3). [0.5]
  - `CF-S94-W1-B` → `S94-VII-BA-T4-ENVELOPE-EXTENSION` — T4\|s≠s' Res_W ratio envelope L∈[14,100], L3<L2 saturation test. [0.3]
  - `CF-S94-W1-6` → `S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY` — T5 α_s direct-Connes-Karoubi @ a_4 (s=2); new 5-anatomy bridge + Stage-2. [1.5]
  - `CF-S94-K-CSUB-R-ABSOLUTE-CONVERGENCE` → same — FULL K_csub_R UV-convergence via S61/S78 PV subtraction at Λ_UV=M_KK. [1.0]
  - `CF-SX-2` → `S94-A_S-MPL-CONVERGENCE` — A_s M_Pl_spectral-vs-physical 0.12-OOM normalization gate. [1.0]
- **Natural split candidates** (if stalled): W1a = {W1-A, W1-B, W1-6} (§VII.BA cluster); W1b = {K-CSUB-R, CF-SX-2} (UV-convergence + A_s normalization).

## Wave 2 — §VII.AU winding / 3He-B BDI Level-3 / α=−3 Layer-1

- **Owner**: `connes-ncg-theorist` (cross-consult van-den-dungen K-homology + volovik BdG)
- **Reviewer-origin**: S93 W2 (connes)
- **Items** (3):
  - `CF-S94-W2-A` → `S94-VII-AU-WINDING-RECONCILIATION` — BDI winding N_K=2 on (0,0,0): rep-side K-homology vs BdG winding. [0.6]
  - `CF-S94-W2-B` → `S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR` — integer 3He-B BDI branch-count Level-3 anchor. **Depends on W2-A.** [0.5]
  - `CF-S94-W5-3` → `S94-VII-AU-ALPHA-MINUS-3-LAYER-1` — α=−3 Layer-1 asymptotic via Friedrich-Bär L∈[35,100]. [0.4]
- **Natural split candidates**: keep whole (W2-B depends on W2-A; small wave).

## Wave 3 — Pati-Salam SU(4)_PS Level-3 + module-as-canonical K3 + §VII.AZ re-extraction

- **Owner**: `connes-ncg-theorist` (SU(4)_PS spectral triple; heavy-feasibility wave)
- **Reviewer-origin**: S93 W6 (connes) + S93 W2 (connes)
- **Items** (3):
  - `CF-W9-12-3` → `S94-VII-PS-FULL-SPECTRUM-LEVEL-3` — full SU(4)_PS D_K_PS spectrum + Level-3 `Res_{s=4}`; serves §VII.AQ + §VII.BE. **HEAVY ~4.0; INFEASIBLE dense (1094.7 GB) — MUST pre-check sparse-Lanczos / Friedrich-Bär feasibility per `math-scripts.md §"D_K Block-Diagonality Pre-Check"` before pinning L_max.** [4.0]
  - `CF-S94-W2-C` → `S94-MODULE-AS-CANONICAL-K3` — corpus §19 weighting-functional-family K-counter K=1 → K=3 (Pati-Salam M_4(ℂ)_PS rank-4 triple). [0.5]
  - `CF-S94-VII-AZ-BAND-ADMISSIBLE-RE-EXTRACTION` → same — re-extract α_HH¹_emp(s=4) into [1.5,4.0]; §VII.AZ Element-4 discharge. [0.5]
- **Natural split candidates**: W3a = {CF-W9-12-3} (heavy SU(4)_PS, may run solo / Friedrich-Bär route); W3b = {W2-C, AZ-RE-EXTRACTION} (lighter Pati-Salam-adjacent + HH¹ residue).

## Wave 4 — Stage-2 joint-theorem cross-axis promotions

- **Owner**: `gen-physicist` (cross-reviewer breadth; per-gate Stage-2 dispatches TWO axis-distinct reviewers)
- **Reviewer-origin**: S93 W4 (mack) + session-x W1 (LQG/CDT)
- **Items** (2):
  - `CF-S94-W4-STAGE-2-VII-AX-STATE-PROJ-CROSS-AXIS-VERIFY` → same — §VII.AX.STATE-PROJ Stage-2 (STAGE-1 → STAGE-3). [0.6]
  - `CF-SX-3` → `S94-LQG-CDT-STAGE-2` — Stage-2 of the 5 LQG/CDT cross-framework comparisons. [1.0]
- **Note**: both are `joint-theorem-promotion.md §Stage 2` gates — Axis-distinctness + original-author-exclusion + downstream-inheritance-reach selection protocol per gate.
- **Natural split candidates**: keep whole (2 gates).

## Wave 5 — PBH truncation/band-breach + BAO-peak observational

- **Owner**: `mack-cosmic-bridge` (observational / PBH / BAO)
- **Reviewer-origin**: S93 W4 (mack) + session-x W4 (BAO)
- **Items** (3):
  - `CF-S94-N-PBH-CANONICAL-TRUNCATION-RE-DETERMINATION` → `S94-N-PBH-TRUNCATION-ANCHOR` — substrate-physical/lab-IN truncation anchor (NOT an N_eigs plateau). [0.5]
  - `CF-W4-1` → `S94-N-PBH-BAND-BREACH-PROJECTION` — L_max at which n_PBH_central breaches JE5 ceiling 2.2e-22. [0.3]
  - `CF-SX-4` → `S94-BAO-PEAK-BRANCH` — per-gapped-branch Layer-1/Layer-2 BAO-peak number. [1.0]
- **Natural split candidates**: W5a = {N-PBH-TRUNCATION, band-breach} (n_PBH cluster); W5b = {BAO-peak}.

## Wave 6 — methodology / K-counter / audit-script / a_n-retrofit

- **Owner**: `gen-physicist` (methodology / audit-infra breadth)
- **Reviewer-origin**: S93 W1 + W3 + housekeeping §D + session-x W4
- **Items** (5; mostly METHODOLOGY-class M1-M4 → allowlist appends at plan-freeze):
  - `CF-S94-W1-C` → `S94-CPB-AUDIT-PENDING-VS-DEFECTIVE` — run_audit() pending-candidate vs complete-but-defective classification + parent/sub anatomy inheritance. [0.5]
  - `CF-S94-MULT-NORM-CANCELLATION-K3` → `S94-MULT-NORM-CANCELLATION-K3` — K=2 → K=3 MANDATORY promotion (bottom-K Casimir-ceiling = 3rd distinct form). [0.3]
  - `CF-S94-S1-SINGLET-AREA` → `S94-S16-AREA-FUNCTIONAL-K-ADVANCE` — §16 single-observable-per-triple K-counter assessment (Φ_area vs Φ_floor). [0.2]
  - `CF-S94-NON-PROMOTION-META-TAXONOMY` → `S94-NON-PROMOTION-META-TAXONOMY` — Tier-2-dimensionful + §(iv-bis) surrogate-theorem meta-taxonomy assessment (INFO-class). [0.3]
  - `CF-SX-1` → `S94-A_N-RETROFIT-C-CAUSALITY` — retrofit 193 bare `a_n` in `Phononic-C-Causality.md` with `a_n^{regulator}` tags (artifact-existence METHODOLOGY). [0.5]
- **Natural split candidates**: W6a = {W1-C, MULT-NORM-K3, S1-SINGLET, NON-PROMOTION-META} (K-counter/audit rule); W6b = {a_n-retrofit} (regulator-tag retrofit, transit-dynamics executor).

## Wave 7 — spectral-dimension v_g^B2 discriminator + LQG narrow-path cocycle

- **Owner**: `phonon-first-cosmologist` (cross-domain: spectral-dimension flow + analogue-gravity / LQG)
- **Reviewer-origin**: S93 W7 (kk/landau) + S93 W8 (phonon-first)
- **Items** (2):
  - `CF-S94-DS-GAMMA-E-RESOLUTION` → `S94-DS-GAMMA-E-RESOLUTION` — v_g^{B2}(τ) scalar-trajectory discriminator across ≥7 τ-slices (Reading-KK vs Reading-van-Hove). Per-gate executors: `kaluza-klein-theorist` + `landau-condensed-matter-theorist`. [0.5]
  - `CF-S94-NARROW-PATH-WORKSHOP-6-COCYCLE-CONSTRUCTION` → `S94-NARROW-PATH-WORKSHOP-6-COCYCLE` — exit-horizon Hochschild cocycle + α_bridge OOM (Regime I vs II). [1.5]
- **Natural split candidates**: W7a = {DS-GAMMA-E} (kk/landau); W7b = {NARROW-PATH-COCYCLE} (phonon-first / LQG-bridge).

## Wave 8 — §VII.AV Stage-2 re-verify + §VII.AR PASS-A substrate-derivation

- **Owner**: `volovik-superfluid-universe-theorist` (BdG / superfluid-universe substrate; §VII.AV + §VII.AR)
- **Reviewer-origin**: S93 W3 (volovik) + S93 W5 (volovik/mack)
- **Items** (2):
  - `CF-S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY` → same — Axis-A (vdd) re-verify on Cell-II-corrected §VII.AV.OP-PROJ → Stage-2 PASS-AND → STAGE-3-eligible. [0.3]
  - `CF-S94-VII-AR-PASS-A-CONTINUOUS-PARAM-SUBSTRATE-DERIVATION` → `S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION` — substrate-BdG derivation of the PASS-A param vector; FULL-tier N=4 PV rank test. `[SIGN]`. LOW priority. [0.75]
- **Natural split candidates**: keep whole (2 gates; AV-reverify is near-trivial Axis-A re-dispatch).

---

## Partition notes

- **session-x gate-ID re-namespacing**: `SX-NEXT-*` → `S94-*` (provenance CF-ID retained in each gate block). Verify no collision against `computations/session-93/s93_gate_verdicts.txt` + `computations/session-x/sx_gate_verdicts.txt`.
- **Heavy/feasibility wave**: W3's `CF-W9-12-3` is the one infeasible-in-session item (1094.7 GB dense). The W3 planner MUST apply the D_K block-diagonality + Friedrich-Bär feasibility pre-check and pin EITHER a sparse-Lanczos block route OR the analytic-saturation route — not a naive dense L_max.
- **Stage-2 gates** (W1-A, W4-STAGE-2, CF-SX-3, W8 AV-reverify): each requires TWO axis-distinct cross-reviewers without prior workshop context per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`; the gate block names both axes.
- **METHODOLOGY-class allowlist**: W6 gates (and any other M1-M4 gates) flagged by planners → orchestrator appends gate-IDs to `methodology-wave-allowlist-ledger.md` at plan-freeze (orchestrator-only edit).
