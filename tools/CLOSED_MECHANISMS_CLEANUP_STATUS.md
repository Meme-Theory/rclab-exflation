# closed_mechanisms Extractor Cleanup — Status & Handoff

**Date**: 2026-05-17 (S90 continuation update)
**Owner**: orchestrator (knowledge-base extraction layer)
**Trigger**: User flag on S47 chain-of-custody asymmetry → audit revealed 735 closed_mechanism rows where the framework has ~287 real closures (~30× over-emission)

---

## TL;DR — S90 final state

**Trajectory**: 735 → 306 (S89-end) → 266 (S90-end). **63.8% noise eliminated.**

Issue 1 (atlas-04 over-emission) + Issue 2 (§V rollups) from prior handoff: **CLOSED**.
Additional S90 corrections:
- **spectral-post-mortem carve-out was wrong** — the file is a narrative retrospective with 13 H2 sections + 5 diagnostic tables, NOT a structured closure registry. All 13 prior rows were extraction artifacts (numeric table values + section headings). Now correctly blacklisted.
- **Digit-leading name filter** added to legacy Strategy-1 parser — rejects `"0.0 (bit-exact)"`-style table-data-as-closure-row noise without affecting the 2 real atlas-02 digit-leading entries (`"1-loop Coleman-Weinberg"`, `"3-pole Leggett propagator"`) which come from the canonical-source path.

Critical-check counts (all match expected):
| Source | Count |
|:-------|:-----:|
| atlas-02 canonical inventory | 196 |
| atlas-04 assumptions (expect 0) | 0 |
| permanent-results §V (no rollups) | 11 |
| spectral-post-mortem (correctly blacklisted) | 0 |
| closed-gw-channels | 7 |
| Legacy-path remainder | 52 |
| **TOTAL** | **266** |

20-row deterministic sample of legacy-path remainder shows ~85% real signal (above 80% threshold per §6 step 4 directive).

The closed_mechanisms arc is now CONVERGED. Next priority: theorems extractor (Task #30 in handoff §6).

---

## What this document is for

The conversation that built this status was compacted twice. Anything a follow-up session needs to know about the **closed_mechanisms extractor cleanup** lives here. Read this in full before touching any extractor code — re-deriving the audit is hours of work that this doc preserves.

The cleanup is **functionally complete** for closed_mechanisms. The original two structural defects (Issue 1 + Issue 2) are closed; spectral-post-mortem turned out to be misdiagnosed and is now correctly handled; digit-leading-name noise is filtered. The work fits into a larger goal (chain-of-custody Genealogy visualizer for `../meme-engine-web`) the user described two compactions ago — preserved verbatim in this doc's §"Larger context".

---

## 1. The problem

Surface: user clicked `sessions:47` in the chain-of-custody sidecar (`tools/viz/console/chain_of_custody.json`) and observed S47 had 28 upstream entries / 0 downstream entries. Investigation:

- The BFS directionality bug was real but a separate fix (PREDECESSOR_POSITION map in `tools/viz/console/build_chain_of_custody.py`; landed earlier in this session).
- The deeper bug: the `closed_mechanisms` table in `tools/knowledge.db` had **735 rows**, of which:
  - Real framework closures (per `sessions/framework/Atlas/atlas-02-mechanism-lifecycle.md` header): **287+** enumerated across 12 Eras.
  - The remainder were extraction noise: markdown subsection headers being treated as session IDs (`session='OPEN'`, `session='Closure'`, `session='Pending'`, `session='Path'`, etc.), bullet-list fragments grabbed from sections that merely *mentioned* "closure", tech notes, registry bookkeeping rows, and numeric values like `session='R² = -72.3'` and `session='2.9952'`.

User's framing of the bigger picture (verbatim, two compactions ago):
> "I expect we are going to find gaps in what our current knowledge base tool makes cross-referenceable, and I don't want you to just shrug and hide any gaps like that, lets plan to fix them. The /goal of the visualizer is to provide an incredibly complex connection map, with the edges as the shared index."

Then this session, on the closed_mechanisms specifically:
> "closed mechanisms should NEVER have downstream, otherwise 'closed' means nothing"
> "Lets work the knowledgebase extraction scripts until they are extracting ACTUAL knowledge"

---

## 2. What this session accomplished

### 2.1 Audit (look at the data first)

`tools/_audit_closed_mechanisms.py` — throwaway diagnostic script that categorizes every closed_mechanism row by source-file pattern, gate_id shape, and session-field shape. Read this if you want to see the pre-cleanup noise modes in detail.

### 2.2 Three canonical-source extractors

Added to `tools/extract_entities.py`:

- **`_extract_closed_from_atlas_02`** — parses `sessions/framework/Atlas/atlas-02-mechanism-lifecycle.md`. Two schemas auto-detected:
  - Schema 1 (Era I–IX): `# | Mechanism | Proposed | Tested | Closed | Kill Shot | Wall`
  - Schema 2 (Era IX–XII): `# | Mechanism | Session | Verdict | Class | Wall / Slot | Author`
  - Handles `#` column variants: integer (`1`), sub-numbered (`56.1`), range (`72-75`).
  - **Output: 196 high-confidence rows**, each with session+gate_id+closed_by+wall+era.

- **`_extract_closed_from_permanent_results_v`** — parses §V of `sessions/permanent-results-registry.md`. Era-keyed subsections V-A through V-G (Eras I–VII; §V stops at S62). Handles:
  - 4-column variant (Era III–VII; no Wall column) and 5-column variant (Era I–II).
  - En-dash `–` and em-dash `—` in range numbers (Era II–VI use en-dash for ranges like `22–26`).
  - Wall-suffix stripping (`W4 (value=..., scheme=CLOSURE-DECLARATION, convention=constraint-eliminated, L_max=NA)` → `W4`).
  - Malformed-row recovery (e.g., §V row #81 at line 1750 has an extra empty pipe orphaning the closure reason; reconstructed via cell concat).
  - V-H/V-I/V-J intentionally skipped (S63/S64/S65 closures; atlas-02 Era VIII enumerates them more completely).
  - V-K/V-L/V-M intentionally skipped (Wall Attribution Summary / Sagan Correlation Correction / Closure Tally — meta-sections, not closure inventories).
  - **Output: 38 standalone rows + 6 range-rollup tags + 1 source-malformed tag.** (See §4 issue 2 — this gets superseded to 17 in the full extractor run via dedup.)

- **`_extract_closed_from_closed_gw_channels`** — parses `sessions/framework/registry/closed-gw-channels.md` `### channel_name` headings. Handles parens in channel names (e.g., `U(1)_7_global_Goldstone_not_GW`). Pulls Claim/Basis/Consequence into `claim`, `closed_by`, `consequence` fields.
  - **Output: 7 rows** (all 7 documented channels).

### 2.3 Legacy narrative-path tightening

`extract_closed_mechanisms` dispatcher (`tools/extract_entities.py`) now routes:
1. Plan files → `[]` (unchanged from prior).
2. Canonical sources (atlas-02 / §V / closed-gw-channels) → dedicated parsers.
3. Files matching `_NON_CLOSURE_SOURCE_MARKERS` → `[]` (NEW blacklist of ~50 source-path patterns covering atlas-04/05/06/07/08/09/10/11/12, registry/* non-closure docs, EVOI framework, framework root non-closure docs, rule/hook/template/skill/agent dirs, framework Collabs, framework ARCHIVE except `spectral-post-mortem`).
4. Everything else → tightened legacy parser:
   - **Strategy 1 (table rows) kept with strict filters**: row's session must match `S?\d+[a-z]?` or `Session N` pattern; session not in markdown-header-word set; session not a free-text float; session ≤ 30 chars; name 4–80 chars; name doesn't start with backtick / `**`; name doesn't end with period.
   - **Strategy 2 (bullet-list pass) REMOVED**. Was the dominant noise source — picked up any bullet from any section that merely mentioned "closure".
   - **Strategy 3 (narrative kill headers) kept unchanged** — already strict (regex requires `### II.2 K-1e: ... — DECISIVE CLOSURE` form).

### 2.4 Test harness

`tools/_test_closed_extractor.py` — exercises the three canonical-source parsers without paying the full `/weave --update` cost. Run-on-demand to iterate. Currently asserts:
- atlas-02: 196 rows, per-Era counts match canonical-header claims for Eras I-VII (exact), Eras VIII-XII match enumerated row counts (gap-reported separately).
- §V: 38 standalone rows with 6 range-rollup detection, 1 source-malformed recovery, spot-check on row #1 (V_tree minimum, session=17a, gate_id=SP-4, wall=W4 stripped).
- closed-gw-channels: 7 channels including the parens-in-name case.

### 2.5 End-to-end /weave --update completed

Ran phases 1-3 of the seven-phase `/weave --update` pipeline (harvest archive edges, harvest provenance edges, rebuild knowledge-index.json, sync to SQLite). Phases 4-7 (build_data, build_topic_pages, export_routing_manifest, audit-paths) NOT YET RUN — they're downstream consumers of the DB and don't affect closed_mechanisms correctness.

**Final SQLite state**: 306 closed_mechanism rows (down from 735 baseline). Distribution:
```
196  atlas-02 (canonical) ✓
 17  permanent-results-registry §V (see issue 2 below)
 14  session-40-results-workingpaper (legacy narrative)
 13  spectral-post-mortem (legacy narrative, framework/ARCHIVE/)
 12  atlas-04-assumptions (see issue 1 below)
  7  closed-gw-channels (canonical) ✓
  7  constraint-mega-matrix (legacy narrative)
  6  session-25-Investigation-Closing (legacy narrative — real signal)
  4  session-32b-synthesis (legacy narrative)
  4  session-24-sagan-verdict (legacy narrative — real signal)
  ...
```

Backup of pre-cleanup DB: `tools/knowledge.db.s89-pre-cleanup-backup` (53 MB; restore with `cp` if needed).

---

## 3. Current state — what's in the table now (S90-end)

| Quality bucket | Count | Source |
|:--|--:|:--|
| HIGH (canonical extractors) | 214 | atlas-02 (196) + §V (11; no rollups) + closed-gw-channels (7) |
| MEDIUM-HIGH (real legacy narrative) | ~44 | session-25 Investigation-Closing, sagan-verdicts, S22-S40 synthesis tables, session WP rows passing strict filters |
| LOW (legacy-path edge cases) | ~8 | session-32b summary rows + a few minimal closures with only session-pointer in closed_by |
| **TOTAL** | **266** | |

Sample-verified at 85% real signal (20-row deterministic sample, seed=42). Compare to baseline 735 (95%+ noise). The cleaned table is **~85-90% real closure rows**, vs the prior ~5%.

---

## 4. Known remaining issues (for the next session)

### Issue 1 — RESOLVED (S90, 2026-05-17)

`framework-registry` extractor was over-labeling atlas-04 assumption rows as closures. The actual fix landed in `_classify_registry_buckets` (extract_entities.py around line 3585): the function now consults `_is_non_closure_source` and strips "closed_mechanisms" from the target_buckets list when the file is blacklisted. Atlas-04 still emits theorems (correctly), but no longer emits closures. Result: 12 → 0 rows from atlas-04.

*Note*: handoff prior to S90 cited line 3589 for the merge step, but the actual merge step is at line 4199. The bucket-filter fix is the structurally correct fix because it stops the noise at the entity-classification layer rather than filtering at merge. Either approach would work mechanically; bucket-filter is preferred.

### Issue 2 — RESOLVED (S90, 2026-05-17)

Diagnosis was slightly off: it was NOT framework-registry shadowing §V. The framework-registry path correctly emits zero closed_mechanisms for permanent-results-registry.md (its `_FW_BUCKET_HINTS` entry maps to `["theorems"]` only). The 17 → 11 (vs the test-harness 38) discrepancy was 6 §V range-rollup rows that the parser emitted as synthetic aggregation rows (e.g., "Instanton variants (gas, liquid, crystal, dilute)") plus 21 dedup collapses against atlas-02.

Fix: dispatcher (extract_entities.py around line 1090) filters `range_rollup=True` rows from `_extract_closed_from_permanent_results_v` output before they enter the closed_mechanisms collection. The parser's API is preserved so the test harness still sees the full 38 rows (including rollup-tagged ones) for diagnostic purposes; only the path that flows into closed_mechanisms drops them.

### Issue 2.5 — RESOLVED (S90, 2026-05-17) — spectral-post-mortem reclassification

Prior handoff (§2.5 distribution) classified spectral-post-mortem.md as a "MEDIUM-HIGH real legacy narrative" closures registry contributing 13 valid rows. **This was wrong**, discovered by direct file inspection.

`sessions/framework/ARCHIVE/spectral-post-mortem.md` is a 424-line retrospective with 13 H2 narrative sections (`## 1. The Question (Why We Looked)`, `## 4. The Structural Monotonicity Theorem (Why It Is Dead)`, etc.) plus 5 diagnostic tables (tau-eigenvalue pairs, spectral action values, session history, file index). The 13 closed_mechanisms rows that previously came from it were ALL extraction artifacts:
- 3 rows: numeric table values from Table 1 (`tau, <lambda^2>`) mis-parsed as closure rows
- 10 rows: H2 section headings being grabbed verbatim (closed_by mirrored name exactly because both came from the same H2 text)

The closures spectral-post-mortem discusses narratively are already in atlas-02 Era II as proper structured rows. So the blanket `framework/ARCHIVE/` blacklist pattern is correct as-stated; my initial S90 carve-out was wrong and was reverted. Result: 13 → 0 rows from spectral-post-mortem.

### Issue 3 — Legacy narrative path remains, but signal-to-noise is acceptable

Status after S90: 52 legacy-path rows. A 20-row deterministic sample (seed=42) showed **17/20 = 85% real signal**, comfortably above the 80% threshold from the prior handoff's directive. Per the directive: **leave alone**.

The S90 session DID apply one additional surgical filter to the legacy Strategy-1 parser: reject names starting with a digit/sign-digit pattern (`re.match(r"^\s*[-+]?\d", name)`). This catches "0.0 (bit-exact)" and "1-18" style noise without affecting real atlas-02 closures ("1-loop Coleman-Weinberg", "3-pole Leggett propagator") because those are extracted via the canonical-source path that bypasses the legacy parser entirely. Verified by direct DB query before applying the filter.

If future audit shows legacy-path signal-to-noise has degraded (e.g., new session files emit similar value-as-name patterns), consider tightening Strategy 1 to require gate_id non-empty, OR to fullmatch the session pattern rather than match-at-start.

### Issue 4 — Theorems table has the same noise profile

`theorems` table has 2,812 rows; per pre-cleanup audit, ~50% are rule-file bullet fragments and CLAUDE.md snippets that the bullet-list pass over-grabbed. Same noise modes as closed_mechanisms had. **Same two-pass canonical+narrative fix needed**:
- Canonical source: `permanent-results-registry.md §VII` (per S88 W4a-17 the canonical theorem inventory)
- Strict narrative-path predicate for non-canonical sources

### Issue 5 — `canonical_constants` SQL table doesn't exist

`tools/knowledge.db` has no `canonical_constants` table. The 297 `constants:` anchors in the chain-of-custody sidecar are SYNTHESIZED from edge endpoints — they have no value, no provenance, no session. The actual source of truth (`computations/_shared/canonical_constants.py`) is never materialized into SQLite. Extract it during `/weave --update` Phase 2.

### Issue 6 — `equations` (22,632 rows), `data_provenance` (3,069), `open_channels` (828) are unaudited

Same audit methodology as closed_mechanisms (per-source-file categorization + per-field pattern shapes) should be applied. Likely similar over-emission, especially `equations` which is by volume the largest table.

### Issue 7 — Phase 3 sidecars need rebuild + Phase 3 plan size estimates need updating

After all the closed_mechanisms cleanup (and the theorems cleanup when that lands), regenerate the chain-of-custody sidecar (`tools/viz/console/build_chain_of_custody.py`) — the anchor counts will change. The Phase 3 plan at `C:/sandbox/meme-engine-web/docs/PLAN-phase-3-genealogy-chain-of-custody.md` cites a 13.86 MB sidecar; that figure will change post-cleanup.

---

## 5. File pointers

### New code (this session)

- `tools/extract_entities.py` — modified:
  - `_NON_CLOSURE_SOURCE_MARKERS` list + `_is_non_closure_source()` (new)
  - `_ATLAS02_ERA_HEADER_RE`, `_ATLAS02_NUMBER_RE`, `_ATLAS02_SESSION_GATE_RE` (new regex constants)
  - `_REGV_SUBSECTION_HEADER_RE`, `_strip_regv_wall_suffix()` (new)
  - `_GWCH_CHANNEL_HEADER_RE` (new)
  - `_parse_atlas_02_table()`, `_extract_closed_from_atlas_02()` (new)
  - `_extract_closed_from_permanent_results_v()` (new)
  - `_extract_closed_from_closed_gw_channels()` (new)
  - `extract_closed_mechanisms()` REWRITTEN: canonical-source routing + blacklist + tightened legacy parser (no bullet pass, strict Strategy 1 filters)

### Test + diagnostic scripts

- `tools/_test_closed_extractor.py` — (S89) standalone test harness for the three canonical parsers (run-on-demand, no /weave required); still passes after S90 fixes
- `tools/_audit_closed_mechanisms.py` — (S89) pre-cleanup audit (still useful for verifying delta against baseline)
- `tools/_sample_legacy_rows.py` — (S90) deterministic 20-row sample of legacy-path remainder for signal-to-noise gauging
- `tools/_audit_legacy_signal.py` — (S90) inspects suspicious session-field/name patterns across the legacy remainder
- `tools/_check_digit_names.py` — (S90) lists all digit-leading names in current DB; used to verify the digit-name filter is safe before applying
- `tools/_verify_final.py` — (S90) end-state assertion script (critical-check counts + trajectory)

### Other artifacts

- `tools/knowledge.db` — current state (306 closed_mechanisms)
- `tools/knowledge.db.s89-pre-cleanup-backup` — pre-cleanup DB (735 closed_mechanisms; restore with `cp` if rollback needed)
- `tools/knowledge-index.json` — rebuilt by Phase 2 (uses new extractor)

### NOT touched this session (preserved as-is)

- `tools/extract_entities.py:3837 extract_framework_registry()` — needs fix per issue 1 + 2
- `tools/extract_entities.py:332 extract_proven_theorems()` — needs same two-pass treatment per issue 4
- `tools/viz/console/build_chain_of_custody.py` — already fixed earlier this session (PREDECESSOR_POSITION map). Sidecar at `tools/viz/console/chain_of_custody.json` reflects pre-cleanup closed_mechanisms; rebuild after issues 1+2 are fixed.

---

## 6. Next-session continuation plan

S90 closed steps 1-4 of the prior handoff. Remaining priority list:

1. **Theorems extractor (issue 4)**: apply the same canonical+narrative two-pass pattern that worked for closed_mechanisms. Canonical source: `permanent-results-registry.md §VII`. Effort: ~2 hours. Expected: 2,812 theorem rows drop to ~1,500 (similar 50% noise rate to closed_mechanisms baseline). Pattern: copy the §V parser as a template, swap to §VII iteration, add the same digit-leading + sentence-shape + length filters to the legacy theorem-extractor.
2. **canonical_constants SQL table (issue 5)**: extract `computations/_shared/canonical_constants.py` into a real `canonical_constants` table in `knowledge.db` during `/weave --update` Phase 2. The 297 `constants:` anchors in the chain-of-custody sidecar are currently SYNTHESIZED from edge endpoints — they have no value, no provenance, no session. Effort: ~1 hour.
3. **Rebuild `tools/viz/console/chain_of_custody.json`** with the cleaned closed_mechanisms; verify the closed_98 / closed_107 / closed_214 / etc. anchors that were noise BEFORE are now gone (closed_98 was atlas-04 noise; should disappear).
4. **Audit equations / open_channels / data_provenance (issue 6)**: similar pre-cleanup audit + selective cleanup. Effort: ~3 hours combined.

Steps 1-4 done in S90:
- ✅ Fix Issue 1 (atlas-04 over-emission)
- ✅ Fix Issue 2 (§V rollups; diagnosis corrected — not framework-registry shadow as previously thought)
- ✅ Re-run /weave Phases 1-6 (data.js 7.0 MB; routing_manifest Validation: PASS)
- ✅ Sample 20 legacy-path rows (85% signal — above threshold)
- ✅ Plus: corrected spectral-post-mortem misclassification (13 → 0); added digit-leading-name filter (2 → 0)

Optional follow-on (longer arc):
- Apply the Genealogy / chain-of-custody visualizer plan at `C:/sandbox/meme-engine-web/docs/PLAN-phase-3-genealogy-chain-of-custody.md` once theorems + canonical_constants are also clean.

---

## 7. Larger context — why this matters

The user's original ask (paraphrased from the verbatim prompt they preserved across compactions):

> Build a chain-of-custody output that gives every edge in the knowledge graph traceable upstream/downstream provenance. The "Connections" landing page on the meme-engine-web site is the primary data visualizer. Genealogy tab needs full tree structure. Expect to find gaps — DON'T HIDE THEM, plan to fix them. The /goal of the visualizer is to provide an incredibly complex connection map, with the edges as the shared index.

This `closed_mechanisms` cleanup is one piece of that. The visualizer's edges terminate at entity nodes (theorems, gates, mechanisms, sessions, researchers, constants). If those entity nodes are 95% noise, the visualizer's "incredibly complex connection map" is a graph of well-shaped pointers to garbage. The user explicitly called this out as the failure pattern when /goal was satisfied at the edge count layer but the targets were unverified.

Progress made this session puts closed_mechanisms at ~75% real-signal (up from ~5%). The remaining tables (theorems is the next critical one) need the same treatment before the visualizer can credibly claim "all sessions are cross-referenced" against meaningful data.

---

**End of handoff. Resume from §6 step 1.**
