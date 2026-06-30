# Investigation 12 — Results Index (per-wave working papers)

**Date**: 2026-06-14
**Seed (`--from`)**: three investigation-1 agent surveys — `lizzi-spectral-functional-theorist.md` + `van-den-dungen-bridge-theorist.md` + `transit-dynamics-theorist.md` (digest: `investigation-12-seed.md`).
**Plan**: `investigation-12-plan-index.md` — 4 waves, 18 gates (12 compute + 3 solo + 2 workshop + 1 review).
**Verdict ledger** (compute/solo only): `computations/investigation-12/inv12_gate_verdicts.txt` via `emit_verdict(session=12, track="investigation")`. The W4 workshop/review gates close by artifact-existence (NO verdict line) — their deliverables land under `sessions/investigation/investigation-12/workshops/` (workshops) and `investigation-12-as-synthesis.md` (review).

## Per-wave working papers

| Wave | Theme | Types | Gates | Working paper |
|:----:|:------|:------|:-----:|:--------------|
| 1 | Spectral-functional: selection, A_s reference-state, n_s coherence | compute×4 + solo×1 | 5 | `investigation-12-w1-workingpaper.md` |
| 2 | NCG bridge: factorization bounds, pole-audit, Krein, FWD-C1 | compute×3 + solo×2 | 5 | `investigation-12-w2-workingpaper.md` |
| 3 | Transit dynamics: lock the relic, Floquet, back-reaction, greybody, H̃ | compute×5 | 5 | `investigation-12-w3-workingpaper.md` |
| 4 | Cross-agent adjudication & A_s synthesis | workshop×2 + review×1 | 3 | `investigation-12-w4-workingpaper.md` |

Each per-wave WP carries one pending section per gate (a `*(pending — include: …)*` contract for the runtime agent) plus the footer block (`## Wave {i} Synthesis (team-lead)`, `## Carry-Forward Computations`, `## Constraint-Map Updates`, `## Files Produced`). Runtime fill is by `/rclab-coordinate`; compute/solo sections close on a dual-SHA verdict line, W4 sections on artifact-existence of the workshop/synthesis md.

## Next step

`/rclab-coordinate sessions/investigation/investigation-12/investigation-12-plan-index.md` (run INV12-W3-1 first — the foundational relic-spectrum lock feeds W3-2/3/4 + the cross-wave consumers W1-2 and W2-5; see the plan-index "FOUNDATIONAL dispatch-order directive").
