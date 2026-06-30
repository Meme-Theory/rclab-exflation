# Session 90 — Plan Index (fanout)

**Session**: 90 | **Date**: 2026-05-12 | **Format**: compute (fanout) | **Total waves**: 8 | **Total gates**: 66 | **Aggregate effort**: ~38.5 wave-equivalents

## Source materials (Phase 1 + 2 + 2.7 outputs)

| File | Lines | Purpose |
|:-----|------:|:--------|
| [session-90-context.md](session-90-context.md) | 260 | Mechanical-context-gathering output: 66 deduplicated S90-targeted carry-forwards across 8 thematic clusters A-H + source manifest from gen-physicist §6 closeout + 5 per-reviewer syntheses + 6 workshop §### Carry-Forward sections |
| [session-90-partition.md](session-90-partition.md) | 293 | Wave-partition manifest: 8 waves with owner / output / items / natural-split candidates / cross-wave deps + Dispatch Summary table + Reviewer-Origin Notes |

## Per-Wave Plans + Phase 3e Validation Status

| Wave | Theme | Owner | Gates | Effort | Plan File | Validator |
|:----:|:------|:------|:-----:|:------:|:----------|:----------|
| W1 | Methodology rule-file extensions + audit-script enhancements | `gen-physicist` orchestrator-direct (METHODOLOGY-class) | 17 | ~4.8 we | [session-90-plan-w1.md](session-90-plan-w1.md) | EXIT 0 PASS |
| W2 | Mack registry/inventory landings | `mack-cosmic-bridge` sole writer | 15 | ~5.1 we | [session-90-plan-w2.md](session-90-plan-w2.md) | EXIT 0 PASS (post-edit) |
| W3 | Mack watchlist + α_s symbol-overload calibration corpus | `mack-cosmic-bridge` sole writer | 4 | ~1.5 we | [session-90-plan-w3.md](session-90-plan-w3.md) | EXIT 0 PASS |
| W4 | W1 cascade-tail + α(M) ALT-CORRIDOR + LRD + PBH | `phonon-first-cosmologist` (CF-37 BIG 3.5 we) | 5 | ~6.4 we | [session-90-plan-w4.md](session-90-plan-w4.md) | EXIT 0 PASS |
| W5 | W2 substrate-IS R_canonical + downstream BCS | `connes-ncg-theorist` (PRIMARY CF-42 §W2-1.A) | 3 | ~3.8 we | [session-90-plan-w5.md](session-90-plan-w5.md) | EXIT 0 PASS |
| W6 | W3 substrate-derivation + V_4 + Richardson + Var_a Stage-1 + clock-cohort | `lizzi-spectral-functional-theorist` | 8 | ~4.7 we | [session-90-plan-w6.md](session-90-plan-w6.md) | EXIT 0 PASS |
| W7 | W4 §VII.AQ + Stage-2 + SCHEME-DISCRIMINATOR + 3-axis rule refactor + CF-A40 rescope | `lizzi-spectral-functional-theorist` (CF-54 W-4 workshop primary) | 6 | ~5.3 we | [session-90-plan-w7.md](session-90-plan-w7.md) | EXIT 0 PASS |
| W8 | W5 Convergence + FWD-Cn retries + FWD-C1 single-shot + LMAX scan | `lizzi-spectral-functional-theorist` (HIT K-counter advancement path) | 8 | ~6.9 we | [session-90-plan-w8.md](session-90-plan-w8.md) | EXIT 0 PASS (post-edit) |

## Companion artifacts

| File | Purpose |
|:-----|:--------|
| [session-90-plan-w{i}-validation.json](.) | Phase 3e upstream-pin validator JSON output per wave (8 files) |
| [../session-90/session-90-results-index.md](../session-90/session-90-results-index.md) | Results-side index: per-wave working-paper shells + cross-wave dependencies |
| [../session-90/session-90-w{i}-workingpaper.md](../session-90/) | 8 per-wave working-paper shells (compact 7-line context + 3 pending blocks per gate; canonical example shape; MCP Pre-Compute Audit + Verdict + Results pending blocks) |

## Dispatch

Each per-wave plan is independently dispatchable:

```
/rclab-coordinate sessions/session-plan/session-90-plan-w1.md
/rclab-coordinate sessions/session-plan/session-90-plan-w2.md
/rclab-coordinate sessions/session-plan/session-90-plan-w3.md
/rclab-coordinate sessions/session-plan/session-90-plan-w4.md
/rclab-coordinate sessions/session-plan/session-90-plan-w5.md
/rclab-coordinate sessions/session-plan/session-90-plan-w6.md
/rclab-coordinate sessions/session-plan/session-90-plan-w7.md
/rclab-coordinate sessions/session-plan/session-90-plan-w8.md
```

Per `feedback_dispatch-discipline.md` ≤8 concurrent: all 8 waves fit single batch.

## Status

All 8 wave plans frozen + validator-clean + companion WP shells generated. Ready for `/rclab-coordinate` compute-mode dispatch.

Plan-author lessons captured in-session per `feedback_fix-in-session-never-defer.md`:
- W2 + W8 initial planners produced typo-defect filename references (verbose-but-wrong on-disk path; a30→a31 typo); 4 validator-flagged Class C "missing-npz" issues + 2 Class B "real value mismatch" + ~7 Class A "npz-metadata-storage-convention" warnings
- 7 surgical edits resolved all real defects (1 W2 typo + 4 W8 typos/rephrasings + 1 W8 CF-66 pin semantic split + 1 W8 intentional-comparison documentation)
- Class A npz-metadata-convention warnings remain informational (npz files only store data not metadata keys) — non-blocking; validator returns EXIT 0 with these as warnings rather than mismatches
- No re-spawn of any planner agent needed; all defects were editable in-session per `feedback_fix-in-session-never-defer.md`
