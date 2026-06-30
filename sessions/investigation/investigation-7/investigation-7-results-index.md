# Investigation 7 — Results Index (per-wave working papers)

**Date**: 2026-06-14
**Plan index**: `investigation-7-plan-index.md`
**Seed**: `investigation-1/{cosmic-web-theorist, little-red-dots-jwst-analyst, loop-quantum-gravity-theorist}.md`
**Verdict track**: `computations/investigation-7/inv7_gate_verdicts.txt` (compute/solo gates; `emit_verdict(session=7, track="investigation", ...)`). Workshop gates close by artifact-existence (no verdict line).

Each per-wave working paper is the runtime fill target for its wave's gates. `/rclab-coordinate` fills the `*(pending — include: …)*` blocks at execution and verifies closure (verdict line + WP section for compute/solo; the `workshops/{slug}.md` deliverable with `## Wrap-Up` / `Effected In-Session` / `Carry-Forward Computations` for workshops).

| Wave | Working paper | Gates | Closure |
|:----:|:--------------|:------|:--------|
| 1 | `investigation-7-w1-workingpaper.md` | INV7-W1-1 … INV7-W1-6 (compute×6) | verdict line + WP section |
| 2 | `investigation-7-w2-workingpaper.md` | INV7-W2-1, INV7-W2-2 (compute), INV7-W2-3 (solo, INFO-by-construction) | verdict line + WP section |
| 3 | `investigation-7-w3-workingpaper.md` | INV7-W3-1, INV7-W3-2, INV7-W3-3 (compute×3) | verdict line + WP section |
| 4 | `investigation-7-w4-workingpaper.md` | INV7-W4-1, INV7-W4-2 (workshop×2) | artifact-existence → `workshops/effective-friedmann-functional-form.md`, `workshops/n-pbh-physical-vs-tautology.md` |

**Total: 14 gates** (11 compute + 1 solo + 2 workshop) across 4 waves. Compute/solo verdicts land in `computations/investigation-7/inv7_gate_verdicts.txt`; workshop deliverables land under `sessions/investigation/investigation-7/workshops/`.

**Session-track hygiene (NOT in these WPs)**: HY1–HY8 (proven_1450/proven_493 down-tags, lrd-observational-constraints refresh, α_LIV leading-order, capstone "no-bounce" scoping, area-clock cross-link, mack falsifier-inventory edits) are session-track curated-register edits an investigation cannot make (track-local boundary). They route to `/rclab-investigate --investigation 7` close for session-promotion. See `investigation-7-seed.md §"Non-gate items"`.
