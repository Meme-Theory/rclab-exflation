---
name: S84 W5-56 R4 cross-class control result
description: R4 dim-error persists across BDI (3He-B, N_3=0) and AIII (A-phase Weyl, N_3=2); formula-level mistake, not class-specific; 3He-B inheritance uncontaminated
type: project
---

# W5-56 — S84-R4-CROSS-CLASS-CONTROL

**Verdict**: FAIL (cross-class dim-error)
**SHA**: ae4a7aac6d793660dc70436f276cbcfea2df41a90d7918b3ff548ad3b15b8466

## Fact
R4 := 1 + 2*(n_pairs / N_modes). BDI (3He-B, N_3=0): R4 = 1+2*(59.8/8) = 15.95 (S82 baseline reproduced).
AIII (A-phase Weyl analog, |N_3|=2) grid over f_Weyl in {1,2,4} x N_modes^AIII in {4,8}: min=15.95 (degenerate corner f=1, N=8), physics-natural ref=60.80 (f=2, N=4), max=120.60. All choices >= 10 → FAIL.

## Why
Plan line 470 (W5-61 branching) and plan §"If W5-56 FAIL" escalation rule 4. Tests whether the R4 FAIL at K=15.95 (S82 OOM ladder; S83 II.C "BCS-dimensional-inconsistency") is BDI-class-specific (PASS branch) or cross-class universal (FAIL branch).

## How to apply
- R4-discard audit (W5-61) should tag as "DIMENSIONAL-ERROR-CROSS-CLASS", NOT "BDI-CLASS-SPECIFIC".
- 3He-B inheritance (Gate 66) is NOT weakened. The error is formula-level (Fock integer / single-particle mode dim), not topology-level.
- W6 escalation: formula-level dimensional-grade audit across ALL BCS conventions, NOT universality-class-boundary gate (the plan's pre-W5-56 phrasing).
- Physical cluster {R1, R2, R3, R5} (K-corridor center K_R3=2.035) remains intact.
- Convention inventory: "5 → 4 physical + 1 cross-class dim-error".

## Cross-refs
- S82 W2-4 baseline (R4=15.95) reproduced
- S83 II.C diagnosis (BCS-dim-inconsistency) confirmed class-independent
- Volovik paper 10 Sec. 2 (3He-A/B AZ-class survey) — surrogate for 2003 monograph Ch. 7-8 (the plan-pinned path `researchers/Volovik/volovik-2003-universe-in-a-helium-droplet.md` is not transcribed; papers 03/08/10/01 are pinned as SHA-256 cross-references)
- Volovik paper 08 (axial anomaly, ABJ current ∝ N_3) justifies f_Weyl ≥ 2 lower bound
- Volovik paper 03 Sec. 2(b) justifies minimal-Weyl-cone mode count (N_modes^AIII = 4)

## Script
- `computations/s84_w5_r4_cross_class_control.py`
- `computations/s84_w5_56_data.npz` (grid, min/ref/max, thresholds)
- `computations/s84_w5_56_plot.png` (BDI baseline + AIII 6-point grid, PASS/INFO/FAIL bands)
