# Session 115 — Plan Index (fanout)

**Built by**: `/rclab-plan --session 115` (2026-06-24). **Mode**: `--fanout` (per-wave plan + per-wave WP).
**Context**: `sessions/session-plan/session-115-context.md` · **Partition**: `sessions/session-plan/session-115-partition.md`
**Working papers**: `sessions/session-115/session-115-w{1,2,3}-workingpaper.md` (index: `session-115-results-index.md`)
**Verdict file**: `computations/session-115/s115_gate_verdicts.txt`
**Run**: `/rclab-coordinate sessions/session-plan/session-115-plan-index.md`

**Session character**: SMALL focused session at the framework's completion plateau — 6 compute gates / 3 waves. EVOI-ordered: the two §VII.CK STAGE-3-PERMANENT promotions + the lepton-PMNS corridor test first; one confirmatory re-run + two OPTIONAL low-EVOI refinements last. All COMPUTE-class (no METHODOLOGY-class gate, no allowlist append owed).

| Wave | Plan file | Theme | Owner (planner) | Gates | Validators |
|:--|:--|:--|:--|:--:|:--|
| W1 | `session-115-plan-w1.md` | §VII.CK D1–D3 Stage-2 promotion + lepton-corridor residue | gen-physicist | 2 | upstream-pin ✓ · yaml ✓ |
| W2 | `session-115-plan-w2.md` | §VII.CK D4 discharge (depends on W1-1) | gen-physicist | 1 | upstream-pin ✓ · yaml ✓ |
| W3 | `session-115-plan-w3.md` | confirmatory + 2 OPTIONAL low-EVOI refinements | transit-dynamics-theorist | 3 | upstream-pin ✓ · yaml ✓ |

## Dependency graph

```
W1-1 (VIICK-STAGE2-VERIFY, lizzi×kitaev)  ──►  W2-1 (VIICK-D4-DISCHARGE, spectral-geometer×volovik)
        [same §VII.CK slot; D1–D3 → PERMANENT must land before D4 re-scope → UNCONDITIONAL]
W1-2 (LEPTON-PMNS)   — independent
W3-1 / W3-2 / W3-3   — independent (W3-2, W3-3 OPTIONAL)
```

**Dispatch order**: W1 (both gates parallel) → W2 (after W1-1's D1–D3 promotion lands; upstream-block → PRE-REG-INC per `mechanical-closure-discipline.md` if W1-1 ≠ PASS) → W3 (3 independent gates). W1-2, W3-* carry no inter-wave dependency.

## Reviewer-disjointness (the two §VII.CK promotions)

W1-1 `{lizzi-spectral-functional-theorist (Axis-A), kitaev-quantum-chaos-theorist (Axis-B)}` ⊥ W2-1 `{spectral-geometer (Axis-A), volovik-superfluid-universe-theorist (Axis-B)}` — 4 distinct reviewers, no overlap (§EVOI.BF cross-reviewer-independence basis). Exclusions per `joint-theorem-promotion.md` Stage-2: both gates exclude connes + paasch (YUKSHAPE Stage-0); W2-1 additionally excludes vdd + baptista (W-2 authors) + kk (§VII.BL downstream-inheritance).

## Gate roster

| Gate ID | Wave | Type | Executor | Disposition |
|:--|:--|:--|:--|:--|
| `S115-VIICK-STAGE2-VERIFY` | W1 | Stage-2 blind verify | lizzi × kitaev (closeout gen-physicist) | §VII.CK D1–D3 → STAGE-3-PERMANENT |
| `S115-LEPTON-PMNS-FORCED-TEXTURE` | W1 | compute `[SIGN]` | neutrino-detection-specialist + gen-physicist | external-corridor PMNS texture test |
| `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` | W2 | Stage-2 blind verify | spectral-geometer × volovik (closeout gen-physicist) | §VII.CK D4 → STAGE-3-PERMANENT-UNCONDITIONAL |
| `S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` | W3 | compute | transit-dynamics-theorist | confirmatory (cannot flip W-1) |
| `S115-AS-NEWAXIS-SELECTOR` | W3 | compute | transit-dynamics-theorist | **OPTIONAL** (planner-discretion, EVOI-last) |
| `S115-B5A-TFD-QES` | W3 | compute | hawking-theorist | **OPTIONAL, Tier-3 NON-BLOCKING** (EVOI-last) |
