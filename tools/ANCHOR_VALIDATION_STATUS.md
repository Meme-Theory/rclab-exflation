# Anchor Validation Status — Pick-Up Tracker

**Session pause**: 2026-05-18 (post-Pass-5 session_files closure)
**Pass 5 closed**: 2026-05-18 — all 184 batches validated, 0 contaminated, 99.7% VALID.

## Disk state at pause

| Table | Done | Total | % | Status |
|:------|-----:|------:|--:|:-------|
| closed_mechanisms | 27 | 27 | 100% | DONE |
| open_channels | 83 | 83 | 100% | DONE |
| theorems | 194 | 194 | 100% | DONE (1 parse-error tail) |
| gates | 279 | 279 | 100% | DONE (1 short-count tail) |
| data_provenance | 243 | 243 | 100% | DONE (1 over-count + 3 false-NOISE tails) |
| equations | 50 | 50 | 100% | DONE (2 schema-drift tails) |
| researchers | 4 | 4 | 100% | DONE |
| agents | 4 | 4 | 100% | DONE |
| constants | 14 | 14 | 100% | DONE |
| registries | 15 | 15 | 100% | DONE |
| **session_files** | **184** | **184** | **100%** | **DONE this session (Pass 5)** |

**Aggregate written**: **10,922 verdicts** across 11 tables (closed_mech 266 + open_channels 826 + theorems 1,936 + gates 2,789 + data_provenance 2,428 + equations 500 + researchers 32 + agents 33 + constants 133 + registries 144 + **session_files 1,835**).

All passes complete. Post-validation pipeline is now unblocked.

## Verdict tallies (11 closed tables)

| Table | Total | VALID | NOISE | UNSURE | %VALID | %NOISE |
|:------|------:|------:|------:|-------:|------:|------:|
| closed_mechanisms | 266 | 240 | 26 | 0 | 90.2% | 9.8% |
| open_channels | 826 | 337 | 481 | 8 | 40.8% | 58.2% |
| theorems | 1936 | 912 | 1020 | 4 | 47.1% | 52.7% |
| gates | 2789 | 2490 | 293 | 6 | 89.3% | 10.5% |
| data_provenance | 2428 | 2238 | 186 | 4 | 92.2% | 7.7% |
| equations | 500\* | 356\* | 144 | 0 | 71.2% | 28.8% |
| researchers | 32 | 30 | 2 | 0 | 93.8% | 6.3% |
| agents | 33 | 33 | 0 | 0 | 100.0% | 0.0% |
| constants | 133 | 131 | 2 | 0 | 98.5% | 1.5% |
| registries | 144 | 140 | 4 | 0 | 97.2% | 2.8% |
| **session_files** | **1835** | **1829** | **4** | **2** | **99.7%** | **0.2%** |

\* Equations totals include `REAL → VALID` normalization for batches 027 + 041 (18 entries; see tail item #5). Pre-normalization disk state: V=338, NOISE=144, non-canonical=18.

**Reading**: session_files is the highest-VALID-rate table (**99.7% VALID across 184 batches**), narrowly beating Pass-8 small-tables (97.7% subtotal). All session_files entries are filesystem-extracted (sessions/**/*.md paths), confirming the calibration: filesystem-mirroring tables consistently outperform concept-derived tables (open_channels 40.8%, theorems 47.1%). The 4 NOISE entries are tiny stub files; the 2 UNSURE entries are borderline-content edge cases worth manual spot-check.

## Tail cleanup queued for tomorrow

1. **theorems_016.json parse error** — Haiku emitted malformed JSON at char 442. Re-dispatch single batch with theorems rubric.
2. **gates_239.json short by 1** — agent wrote 9 verdicts instead of 10. Re-dispatch with gates rubric to recover the 10th.
3. **data_provenance_243.json over-count** — input batch had 4 anchors, verdict file has 8 (Haiku fabricated 4 extra). Inspect + truncate to 4, or re-dispatch.
4. **data_provenance_{013, 036, 122}.json false-NOISE** — all-NOISE results from `find computations/` Bash command splitting on the space in project root path. Re-dispatch with explicit "do not use Bash find; trust input batch source_context only" instruction.
5. **equations_027.json + equations_041.json schema-drift (REAL → VALID)** — agents emitted `"verdict": "REAL"` instead of `"verdict": "VALID"` for 9 of 10 entries each. Root cause: vocabulary collision between rubric document `tools/_haiku_evaluator_prompt.md` (uses REAL/NOISE) and dispatch-prompt output schema (uses VALID/NOISE/UNSURE). **RECOVERABLE via aggregation-time string substitution `REAL → VALID`** — verdicts are valid per-anchor judgments, just labeled with the wrong enum. NOT re-dispatch.
6. **Pass 8 — no tails**. All 37 batches across researchers + agents + constants + registries returned canonical verdict values on first attempt. No re-dispatch needed.
7. **Pass 5 — no tails after in-session cleanup**. All 184 batches landed clean post-cleanup. In-session incidents (all resolved): (a) batch 023 short-count by 1 — recovered by orchestrator-direct-write Edit appending the missing `sf_64:session-64-quantum-acoustics-synthesis.md` anchor at Pass-5 close; (b) batches 150 + 161 fabrication (Haiku invented `session_files_NNN_000` synthetic IDs on large >30KB inputs) — deleted contaminated artifacts and re-dispatched with explicit anti-fabrication clauses citing the `sf_` prefix requirement; (c) batches 152, 154, 159, 160 missing due to "out of extra usage" on initial wave-20 dispatch — all recovered via re-dispatch after usage reset; (d) one re-dispatch of 154 (subagent reported "wrote 10 verdicts" with no disk artifact) re-launched a second time and landed clean. Large-file chunked-read instruction was added to every batch >30KB after the first large-file failure (batch 150/152 first surfaced the `~30KB Read tool limit` per CLAUDE.md).
8. **Aggregate-audit script** — Pass 5 complete; ready to run `tools/_haiku_anchor_audit.py --aggregate`. **MUST include `REAL → VALID` normalization** in the aggregation pass to recover the 18 equations entries.

## How to resume tomorrow

### Disk-truth check (always first)

```powershell
"phonon-exflation-sim/.venv312/Scripts/python.exe" -c "
from pathlib import Path
RES = Path('tools/anchor_validation_results')
done = sorted(int(p.stem.rsplit('_',1)[1]) for p in RES.glob('session_files_*.json'))
missing = sorted(set(range(1,185)) - set(done))
print(f'session_files done: {len(done)}/184')
print(f'next 8: {missing[:8]}')
"
```

### Pass 5 (session_files) dispatch template

Rubric (from `tools/_haiku_evaluator_prompt.md` line 16): VALID = real session/framework markdown paths like `sessions/permanent-results-registry.md`, `sessions/archive/session-87/session-87-w2-workingpaper.md`. NOISE = tiny empty stubs, non-session files mislabeled.

Per-batch Haiku prompt:

```
Validate session_files entries. VALID=real session/framework markdown paths like "sessions/permanent-results-registry.md", "sessions/archive/session-87/session-87-w2-workingpaper.md", substantive session/wave files with content. NOISE=tiny empty stubs, non-session files mislabeled, fragment paths.

EXACTLY 2 tool calls. Read `tools/anchor_validation_batches/session_files_NNN.json`. Write JSON array to `tools/anchor_validation_results/session_files_NNN.json`.

Output: [{"anchor_id":"<id>","verdict":"VALID|NOISE|UNSURE","reason":"<one short sentence>"}]

Every anchor, preserve order, prefer NOISE. DO NOT NARRATE. Reply only: "wrote N verdicts".
```

Dispatch protocol: wave-of-8 background Haikus (max ~8 concurrent per `feedback_dispatch-discipline.md`), discrete batches (no rolling top-up — wait for ALL 8 to land before launching next 8). 184 batches → 23 full waves of 8.

## Post-validation pipeline (after Pass 5 completes)

1. ~~`python tools/_haiku_anchor_audit.py --aggregate` → produces `tools/_anchor_validation_results.json` (single aggregated map of anchor_id → verdict + reason). **Aggregation MUST include `REAL → VALID` normalization** to recover the 18 equations entries (batches 027 + 041) + any analogous future drift.~~ **DONE 2026-05-18** — see §"Phase 2 (concat) closeout" below.
2. Integrate NOISE filter into `tools/extract_entities.py` — entries marked NOISE get dropped at extract-time; UNSURE stays in for manual review.
3. `/weave --update` to rebuild knowledge.db with filtered data.
4. 30-anchor stratified spot-check across the 11 tables to confirm filter behavior is correct before treating the cleanup as canonical.

## Phase 2 (concat) closeout — 2026-05-18

**Aggregate landing**:
- `tools/_anchor_validation_results.json` — anchor_id → {verdict, reason} keyed by table.
- `tools/_anchor_validation_results_summary.json` — per-table tally + parse errors + REAL→VALID drift counts.

**Code change**: `tools/_haiku_anchor_audit.py::aggregate_results()` patched at S88-style minimal-edit (lines 322-388) to (a) normalize REAL→VALID at the per-verdict point with running counter, (b) emit a sibling summary JSON, (c) collect parse errors into the summary rather than only printing them.

**Aggregate tallies** (10,919 unique anchor_id dict keys; 10,922 raw on-disk verdicts):

| Table | Aggregate | Tracker §"Verdict tallies" | Δ | Notes |
|:------|----------:|---------------------------:|--:|:-----|
| closed_mechanisms | 266 | 266 | +0 | — |
| open_channels | 826 | 826 | +0 | — |
| theorems | 1936 | 1936 | +0 | parse error on theorems_016.json — known tail item #1 |
| gates | **2786** | **2789** | **−3** | anchor_id collision; see "Collision diagnosis" below |
| data_provenance | 2428 | 2428 | +0 | — |
| session_files | 1835 | 1835 | +0 | — |
| equations | 500 | 500 | +0 | 18 REAL→VALID normalizations applied (tail item #5 closed by code, not re-dispatch) |
| researchers | 32 | 32 | +0 | — |
| agents | 33 | 33 | +0 | — |
| constants | 133 | 133 | +0 | — |
| registries | 144 | 144 | +0 | — |

**Aggregate verdict shape**: 8,733 VALID (79.98%) / 2,162 NOISE (19.80%) / 24 UNSURE (0.22%). All verdicts in canonical enum {VALID, NOISE, UNSURE}; no stragglers.

**Collision diagnosis (gates Δ = −3)**: `_haiku_anchor_audit.py:157` truncates gate IDs via `id_[:60]`. The 6 DB rows below share the 60-char prefix `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-{1,2,3}-` and disambiguate only past char 60, so the dict-key dedup collapsed each pair to one entry:

- `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-1-AXIS-ORTHOGONALITY-SIDE-CONNES` (90 chars)
- `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-1-SPECTRAL-SIDE-MACK` (78 chars)
- `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-2-AXIS-ORTHOGONALITY-SIDE-CONNES` (90)
- `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-2-SPECTRAL-SIDE-MACK` (78)
- `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-3-AXIS-ORTHOGONALITY-SIDE-CONNES` (90)
- `S88-CROSS-AXIS-MULTI-OBSERVABLE-STAGE-2-VERIFY-OBSERVABLE-3-SPECTRAL-SIDE-MACK` (78)

All 6 underlying Haiku verdicts are VALID with concordant reasons, so the collision is benign for the filter task. Class of failure is identical to `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` — key-space narrower than data identity. **Recommended fix (deferred to Phase 3 design)**: raise truncation to ≥120 chars OR drop truncation entirely (anchor_ids are dict keys, not filesystem paths; truncation has no operational purpose here).

**Tail-item status after concat**:

1. theorems_016.json parse error — **STILL OPEN**; 10 verdicts unrecovered. Re-dispatch single batch with theorems rubric recovers; harmless if deferred (10 anchors stay unfiltered, i.e., treated as VALID-by-default at extract time).
2. gates_239.json short by 1 — **RECONFIRMED**; 9 verdicts on disk, 1 anchor lacks judgment. Same harmless-if-deferred classification.
3. data_provenance_243.json over-count — **NOT YET INSPECTED**; aggregate consumed all 8 entries (Haiku-fabricated 4). Aggregate may contain 4 fabricated anchor_ids that don't match the DB; needs manual truncate-to-4.
4. data_provenance_{013, 036, 122}.json false-NOISE — **NOT YET INSPECTED**; if aggregate carries the false-NOISE verdicts, the filter would incorrectly drop the affected provenance entries. Re-dispatch recommended.
5. equations_027/041 schema-drift — **CLOSED via aggregator normalization**; 18 entries successfully recovered.
6. Pass 8 — **NO TAILS** (confirmed).
7. Pass 5 — **NO TAILS** (confirmed).

**Phase 2 PASS criterion**: aggregate JSON exists with all 10,919 unique anchor IDs, tracker tallies match within the documented Δ, all known tail items are either closed or have residual scope clearly described. **PASS at 2026-05-18.**

## Key constraints (do NOT forget)

- **NEVER use the Anthropic API directly**. All Haiku validation goes through Claude Code subscription via Agent tool: `subagent_type: "general-purpose"`, `model: "haiku"`, `run_in_background: true`. User has ~$4 on API balance unrelated to this project.
- **One Haiku per batch, EXACTLY 2 tool calls per Haiku** (Read + Write). Mega-bundling = catastrophic failure mode (pre-compaction validated: agents fabricated verdicts when given 10 batches at once).
- **Disk is source of truth**. Subagent chat-tail summaries are intent, not reality. Always grep the results directory. (Pass 6 caught the equations_027 + 041 schema-drift only because disk-truth was run after each wave; chat-tails said "wrote 10 verdicts" but 9 were mis-labeled.)
- **No /goal during this work** — see `feedback_session-process.md`. `/compact` destroys Stop-hook context against multi-session predicates. Resume via disk-state check, not via goal state.
- **Max ~8 concurrent subagents** per `feedback_dispatch-discipline.md`.
- **Discrete batches**: launch 8, WAIT for ALL 8 to land, THEN launch next 8. Never rolling top-up.

## Vocabulary collision (Pass 6 + Pass 8 calibration)

Pass 6 surfaced a vocabulary collision between the rubric document `tools/_haiku_evaluator_prompt.md` (frames positive class as "REAL" vs "NOISE") and the dispatch-prompt output schema (positive class is "VALID" vs "NOISE" vs "UNSURE"). 2 of 50 equations batches (4%) emitted `"verdict": "REAL"` for positive verdicts. **Pass 8 result**: 0 of 37 batches (0%) drifted to REAL — likely because the 4 Pass-8 table rubrics do not involve LaTeX-like or domain-specific positive-class language that would trigger a Haiku to reach for the rubric document's vocabulary. Aggregation-time `REAL → VALID` normalization remains the safe fix for any Pass-5 drift; not worth pre-dispatch prompt revision.

## Task list state at pause

This session marked TaskList #9 (small tables = Pass 8 in tracker's naming, "Pass 8" in TaskList's naming) completed. Pending: #7 (session_files = Pass 5), #10 (aggregate), #11 (filter integration), #12 (/weave + spot-check). TaskList numbering may diverge from tracker's per-session pass-numbering; trust the tracker's table above for resume state.

## Prompt to restart next session

```
Resume anchor validation. Pass 5 = session_files (0/184). Same protocol as data_provenance + equations + Pass-8 small-tables — wave-of-8 single-batch-per-Haiku, discrete batches, run_in_background=true, model=haiku. Disk-truth before each wave. See tools/ANCHOR_VALIDATION_STATUS.md for full state, including REAL→VALID normalization for aggregation.
```
