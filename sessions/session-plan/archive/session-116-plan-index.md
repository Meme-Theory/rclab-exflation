# Session 116 — Plan Index (fanout)

**Date**: 2026-06-27
**Mode**: SESSION (session-116 namespace), mixed gate types per wave (workshop + compute).
**Scope**: user-supplied 9-open-question table — one question per wave; in-wave workshops + computes.
**Context**: `sessions/session-plan/session-116-context.md` (per-wave scope + grounding catches).
**Partition**: `sessions/session-plan/session-116-partition.md` (gate-type manifest).
**Dispatch**: `/rclab-coordinate sessions/session-plan/session-116-plan-index.md` (juggles compute + workshop gate types).

| Wave | Q | Theme | Owner | Types | Gates | Plan file |
|:----:|:--|:------|:------|:------|:-----:|:----------|
| 1 | Q23 | Transit power spectrum / A_s normalization (critical) | transit-dynamics-theorist | workshop×1, compute×3 | 4 | session-116-plan-w1.md |
| 2 | Q18b | Yukawa hierarchy (§VII.CK Stage-2 + lepton PMNS) | connes-ncg-theorist | compute×2, workshop×1 | 3 | session-116-plan-w2.md |
| 3 | Q3 | Goldstone mass from disorder (170× problem) | landau-condensed-matter-theorist | workshop×1, compute×1 | 2 | session-116-plan-w3.md |
| 4 | Q8 | 4D modulus effective action | kaluza-klein-theorist | workshop×1, compute×1 | 2 | session-116-plan-w4.md |
| 5 | Q11 | A_F quaternion (H) extraction | connes-ncg-theorist | workshop×1, compute×1 | 2 | session-116-plan-w5.md |
| 6 | Q12 | τ=0 initial conditions (Wheeler-DeWitt) | quantum-foam-theorist | workshop×1, compute×1 | 2 | session-116-plan-w6.md |
| 7 | Q33 | §VII.AJ.STATE-PROJ derivation | volovik-superfluid-universe-theorist | compute×1, workshop×1 | 2 | session-116-plan-w7.md |
| 8 | Q30 | Forward bridges FWD-C1/FWD-C2 (residual-targeting) | connes-ncg-theorist | compute×2, workshop×1 | 3 | session-116-plan-w8.md |
| 9 | Q36 | D_K sectors p+q=15 (GT-builder) | baptista-spacetime-analyst | workshop×1, compute×1 | 2 | session-116-plan-w9.md |

**Totals**: 9 waves, 22 gates (13 compute, 9 workshop).

## Verdict tracks
- **compute** gates → `computations/session-116/s116_gate_verdicts.txt` (session track; dual-SHA closure).
- **workshop** gates → `sessions/session-116/workshops/s116-w{i}-{slug}.md` (artifact-existence closure; NO verdict line, per `wave-classification.md §M1`).

## Plan-freeze validation (closed)
- **Upstream-pin validator**: 9/9 PASS — 0 mismatches, 0 missing npz (every compute-gate upstream npz resolves on disk).
- **PRDR (R3 YAML) validator**: all 13 **compute** gates PASS. The 5 workshop-gate PRDR-FAILs (`PMNS-RESCUE`, `DISORDER-CLOSURE`, `ZNORM-PROVENANCE`, `ALGEBRA-AXIS`, `SATURATION-ADJUD`) are **expected N/A** — `_yaml_gate_validator.py` is not gate_type-aware and checks the 8 PRDR keys for every R3 yaml gate, but workshop gates close by artifact-existence and are NOT PRU-vulnerable (`wave-classification.md §M1`; skill Phase-3-delta "run on compute gates only"). All 9 workshop gates verified block-complete (exactly 2 agents, sources, output_path, adjudication_question). When re-running the PRDR validator, read workshop-gate FAILs as N/A.

## Plan-freeze grounding corrections (fix-in-session)
- **Q30 (Wave 8)**: the table's "never dispatched" was ~25 sessions stale. FWD-C1 LANDED S90 (§VII.AU.OP-PROJ PASS, Hybrid-Independence-Test B6=True); FWD-C2 → §VII.AV.STATE-PROJ STAGE-3-PERMANENT (S93). W8 re-scoped to the genuine residuals (FWD-C1 Level-2 NUMERICAL-DEFERRED CF-S94; FWD-C2 Corner-II Var_a PROXY-REFINEMENT) — re-deriving the landings would be the rediscovery failure mode. Full forward-trace: `session-116-plan-w8.md §"GROUNDING RECONCILIATION"`.
- **c_sub_baseline PROVENANCE backfill**: `c_sub_baseline=2.238` lacked a structured PROVENANCE-dict entry (flagged by W8 SOURCE-RECON); backfilled to `canonical_constants.py` PROVENANCE (session S78 W2-E), import-verified.
- **Grounding catches folded into the context file** (true prior state): Q3 (inv5 Imry-Ma FAIL, frac170≈4e-5), Q12 (inv11 WDW e-fold-clause FAIL), Q18b (§VII.CK PASS S114 → Stage-2 verify).
