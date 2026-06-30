# Session-X — Plan Index (fanout, COMPREHENSIVE aggregate-expansion)

**Generated**: 2026-05-25 (`/rclab-plan "session-x"`, Phase 3c)
**Mode**: fanout — per-wave plan + per-wave WP shell
**Context (authoritative scope)**: `sessions/session-plan/session-x-context.md` — **PRIMARY MODE = COMPREHENSIVE AGGREGATE EXPANSION** (validation is the embedded QA sub-layer).
**Partition**: `sessions/session-plan/session-x-partition.md`

Each wave comprehensively EXPANDS one `sessions/framework/phononic*` document to a current (S93-era)
view of the whole project, executed by the document's natural author-specialist. Gate spine:
`G1 AGGREGATE-DOMAIN-SURVEY → G2 COMPREHENSIVE-EXPANSION → G3 RECONCILE+VERIFY`.

| Wave | Document / target | Owner (planner + executor) | Gates | Plan file |
|:----:|:------------------|:---------------------------|:-----:|:----------|
| W1 | `Phononic-framework-hypothesis.md` | `tesla-resonance` | 3 | `session-x-plan-w1.md` |
| W2 | `Phononic-Substrate-Geometry.md` | `tesla-resonance` | 3 | `session-x-plan-w2.md` |
| W3 | `Phononic-to-Cosmos.md` | `mack-cosmic-bridge` | 3 | `session-x-plan-w3.md` |
| W4 | `Phononic-C-Causality.md` | `transit-dynamics-theorist` | 3 | `session-x-plan-w4.md` |
| W5 | `Phononic-Penrose-Diagrams.md` | `schwarzschild-penrose-geometer` | 3 | `session-x-plan-w5.md` |
| W6 | `Phononic-Investigation.md` | `phonon-first-cosmologist` | 3 | `session-x-plan-w6.md` |
| W7 | `Classification-of-phonon-exflation.md` | `landau-condensed-matter-theorist` | 3 | `session-x-plan-w7.md` |
| W8 | `Phononic-crystal-geometry_viz.py` (+7 PNGs, +ARCHIVE doc) | `baptista-spacetime-analyst` | 3 | `session-x-plan-w8.md` |
| W9 | cross-document consistency + coverage closeout | `gen-physicist` | 2 | `session-x-plan-w9.md` |

**Totals**: 9 waves, 26 gates.

## Execution ordering

- **W1–W8 are independent** — each is a self-contained aggregate expansion of one document; dispatch in parallel (≤8 concurrent per `feedback_dispatch-discipline.md`).
- **W9 runs LAST** — it consumes the 8 EXPANDED documents (each `WX-W{i}-2` must have landed). It is a verification sweep, not a progressive derivation; droppable without affecting W1–W8.

## Plan-freeze validation status

| Validator | Result |
|:----------|:-------|
| `_yaml_gate_validator.py` (R3/PRDR) | 26/26 gates PASS (W1–W8: 3×8=24; W9: 2) — `FAIL=0` |
| Expansion-primary gate spine present | 9/9 waves (`AGGREGATE-DOMAIN-SURVEY` + `COMPREHENSIVE-EXPANSION` in every file) |
| AMRI (no `agent-memory` input-SHA pins) | clean — 0 refs in any plan |
| `_plan_upstream_pin_validator.py` (numerical-npz) | N/A by construction — these are document-expansion gates; inputs are the documents + `canonical_constants.py` + `tools/knowledge.db` (no upstream `.npz` pins). W9 depends on the W1–W8 document outputs (verified at runtime). |

## Per-wave dispatch

`/rclab-coordinate sessions/session-plan/session-x-plan-w{i}.md` (selective) or
`/rclab-coordinate sessions/session-plan/session-x-plan-index.md` (full session).

**Note**: `/rclab-coordinate` is the EXECUTION step — it is where the curated `sessions/framework/`
documents are actually expanded/edited (by each document's author-specialist) and the figures
regenerated. It is user-triggered.

## Next step

Working-paper shells (`sessions/session-x/session-x-w{i}-workingpaper.md`) per
`.claude/templates/workingpaper.md`, then `/rclab-coordinate`.
