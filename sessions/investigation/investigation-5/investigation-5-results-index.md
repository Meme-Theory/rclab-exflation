# Investigation 5 — Results Index (per-wave working papers)

**Date**: 2026-06-14
**Plan**: `investigation-5-plan-index.md` (3 waves, 12 gates: 10 compute + 1 workshop + 1 review)
**Seed**: `investigation-1/{connes-ncg-theorist, landau-condensed-matter-theorist, spectral-geometer}.md`
**Verdict track**: `computations/investigation-5/inv5_gate_verdicts.txt` (compute gates; `emit_verdict(session=5, track="investigation", ...)`). Workshop + review gates close by artifact-existence (no verdict line).

| Wave | Theme | Working paper | Gates |
|:----:|:------|:--------------|:------|
| 1 | NCG spectral-action joints | `investigation-5-w1-workingpaper.md` | compute×5 (INV5-W1-1…W1-5) |
| 2 | Condensed-matter functionals | `investigation-5-w2-workingpaper.md` | compute×4 (INV5-W2-1…W2-4) |
| 3 | Cross-vantage joints | `investigation-5-w3-workingpaper.md` | compute×1 + workshop×1 + review×1 (INV5-W3-1/2/3) |

Each per-wave WP carries one section per gate (compute = verdict-line closure checklist; workshop/review = artifact-existence checklist, no verdict line) + the four footer sections (Wave Synthesis / Carry-Forward Computations / Constraint-Map Updates / Files Produced).

**Workshop / review deliverables** (close by artifact-existence):
- INV5-W3-2 → `workshops/two-effective-actions.md`
- INV5-W3-3 → `investigation-5-higgs-residual-synthesis.md`

**Dispatch**: `/rclab-coordinate sessions/investigation/investigation-5/investigation-5-plan-index.md` (full investigation), or a single wave via `…/investigation-5-plan-w{i}.md`.

**Close**: `/rclab-investigate --investigation 5` — mines the WP outputs into a synthesis + next-investigation seed, housekeeps the index row (status → outputs → drives), and lifts the HY1 A_s-canonical-number hygiene item to session-promotion.
