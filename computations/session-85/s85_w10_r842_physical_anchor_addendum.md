# R_842 Physical-Anchor Addendum (S85 W10-2, 2026-04-24)

**Target**: `sessions/permanent-results-registry.md` §VII.M.1 (addendum; insert after the existing §VII.M.1 subsection).

**Type**: regulator-conditional physical-anchoring addendum. Does NOT resize R_842. LOCKOUT-C preserved.

## LOCKOUT-C status

- R_842 canonical geometry reproduced from registry §VII.M.1 lines 1105–1111 verbatim:
  - `w_0 ∈ [-0.942, -0.742]` (half-width 0.1)
  - `w_a ∈ [-0.2, 0.2]` (half-width 0.2)
  - center `(-0.842, 0.0)`
  - branch (iv) `w_0_pred = -0.842454`, offset 0.000454 (0.454% of half-width) from center.

- LOCKOUT-C holds: rectangle geometry (center, half-widths, axis ranges) equal to canonical. NO resize attempted.
- S84-W1b-9 closure SHAs present in registry (DR3 wiring intact):
  - content_sha256 `9cc7f47e3dedc978de50947914ebca073663c172fb9d5e45268bca4e74b79d9f`
  - audit_sha256   `e325e13e9dfe3b297a230fb510ef980c8fd184e5c99394708e75af0c04838e1f`
- S85 livewatch script present: `computations/session-85/s85_w1a_dr3_livewatch.py`.

## V.1 regulator-conditional portion

**V.1 pin**: `<pending-W6-V.1>` per dispatch-not-halt discipline (see `feedback_dispatch-discipline.md`).

The W6 conformal-infinity-bifurcation output currently available on disk is `s85_w6_conformal_infinity_bifurcation.npz` (a 5-regulator atlas mapping regulator → I⁺ topology). Its schema carries:

- `regulators`: ['cutoff', 'heat_kernel', 'zeta', 'pauli_villars', 'dimensional']
- `topologies`: ['dS_S3', 'dS_S3', 'flat_RxS2', 'flat_RxS2', 'dS_S3']
- Distinct topology count: 2 (plan-expected ζ/Zubarev 2-branch schema: NOT directly matched)

The plan-expected V.1 schema carries ζ-regulator w_0 central and Zubarev-regulator w_0 central as separate fields, which are not present in the current W6 output. The V.1-conditional addendum is therefore filed as a post-Batch-2 completion step; the V.1-agnostic LOCKOUT-C verification + DR3 wiring check IS complete in this gate.

**Physical-anchoring statement (V.1-agnostic)**: R_842 continues to be the observational rectangle bound to branch (iv) canonical `w_0_pred = -0.842454` under all currently-pinned regulators. The regulator-conditional late-time Penrose-diagram class (dS_S3 vs flat_R×S^2 in the W6 5-regulator atlas) is related to but not identical to the plan-expected ζ/Zubarev 2-branch schema.

## Gate closure

- S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT: see `computations/session-85/s85_gate_verdicts.txt`.
- audit_sha256: `8de72cde7d635949f45716191288da6656f8a9fe05411532ab848fdb93fd04e8`
- content_sha256: `b9a6a3014218386add94df8fef1034df5e17feb467c4d4b9cecacadfb133cd09`
- value resolution: `locked-v1-pending`
