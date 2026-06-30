---
type: methodology-registry
ingested-by: /weave --update
---

# Session Format Generations

**Registry ID**: `session-format-generations`
**Owner agent(s)**: `orchestrator` (sole writer)
**Last updated**: 2026-05-17, Phase-0 / Task #6
**Ingestion**: `/weave --update` picks up this file; downstream consumer is `tools/harvest_attribution_edges.py` (Phase 1).

---

## Scope

This file catalogs the seven distinct authorship-attribution conventions used across the 90 session directories spanning S01-S91 (S03 and S07 are missing from filesystem; S73 splits into S73a / S73b). Each generation has its own header conventions, file shapes, and per-gate attribution granularity. The attribution-edge harvester (Phase 1 of the chain-of-custody work) routes each session through a generation-appropriate extractor; this document is the spec it consumes.

Why this is project-level rather than agent-private: the harvester output (`authored_by`, `participates_in`, `cites_prior_session`, `co_authored_by`, `reviewed_by`, `excluded_from`, `authored_round`, `discussed_in`, `synthesized_by` edges) lands in `knowledge.db::edges` and is read by every downstream consumer (the Genealogy view, the cross-link rewriter, every cross-reference output). Per AMRI Test 1 (`agent-standards.md`), this is canonical data that other gates pin as Input-SHA, not agent-private methodology.

Cross-links:
- Regex set + 18 self-test fixtures: `tools/_format_generation_regex_set.py`
- Full-corpus dry-run output: `tools/_format_generation_dry_run.json` + `tools/_format_generation_dry_run.md`
- Underlying inventory scan: `tools/_format_generation_scan.py` + `tools/_format_generation_scan.json`
- Future harvester (Phase 1): `tools/harvest_attribution_edges.py` (to be implemented)
- Phase-0 source document: `sessions/framework/registry/session-format-generations.md` (this file)

---

## Generation summary table

| Gen | Session range | n | Granularity | Top extractor pattern | Edges (dry-run) | Edges/sess |
|:---:|:--------------|--:|:------------|:----------------------|---------------:|-----------:|
| **G1** | S01-S15 (S03/S07 missing) | 13 | session-level inference | body-text mention frequency | 44 | 3.4 |
| **G2** | S16-S18 | 3 | session-level | `## Authors` block / `## Agents:` comma-list / deliverable-table `\| Agent \|` column | 11 | 3.7 |
| **G3** | S19-S35 | 17 | per-file | `**Author**: <Name> (<canonical-id>)` header | 220 | 12.9 |
| **G4** | S36-S60 | 25 | per-file + WP-section | `**Author**:` header continues; `**Author**: Team-lead` orchestrator self-attribution | 370 | 14.8 |
| **G5** | S61-S77 | 18 | per-gate via heading-parenthetical | `### <GATE-ID>: <description> (<canonical-id>)` heading | 669 | 37.2 |
| **G6** | S78-S81 | 4 | per-gate via Owner-field | `**Owner**: <canonical-id>` per gate-section | 30 | 7.5 |
| **G7** | S82-S91 | 10 | per-gate + multi-author + cross-session | `**Agent**:` / multi-author tuples / `> **Provenance**:` blocks / workshop round-binding | 1,101 | 110.1 |
| **TOTAL** | S01-S91 | 90 | — | — | **2,445** | 27.2 |

---

## G1 — Solo Narrative Prose (S01-S15)

### Defining markers

- File shape: single `session.md` or `session-N-{topic}.md`; 9-28 KB
- No structured author headers (0 `**Author**:` / `**Owner**:` / `**Agent**:` hits in the scan across all 13 sessions)
- Agent identity carried only via body-text mention frequency

### Verbatim sample (S05)

The S05 file `sessions/archive/session-5-qm-debate.md` has exactly one structured agent reference — a section heading:

```
### Gen-physicist overall survival estimate: ~30%
```

The rest of the attribution must be inferred from frequency. The scan shows S05 has top-agent counts: `gen-physicist=23`, `baptista=20`, `quantum-acoustics=17`.

### Extractor

`extract_g1(session_id, all_text)` in `tools/_format_generation_regex_set.py`. Concatenates all session-file text, counts canonical-agent mentions via `G1_AGENT_RE`, emits `discussed_in: agent → session` edges for top-3 agents OR any with ≥10 mentions.

### Edge yield

- 44 edges total across 13 sessions
- Confidence tag: `session-level-inference` (signals to consumers that this is fuzzy)
- All emitted edge type: `discussed_in` (no `authored_by` for G1 — the data doesn't support it)

### Known limits

- Gates in G1 don't have canonical IDs (the framework was pre-formal-gate-shape). Per-gate attribution is impossible.
- Two sessions (S03, S07) are missing from filesystem — no inference possible.

---

## G2 — Transition Block (S16-S18)

### Defining markers

S16's master file uses `## Authors` heading + bulleted list. S17 and S18 use **different** sub-variants:
- `## Agents:` comma-separated list (S17 line 5)
- `## Synthesis Team:` comma-separated list with parenthetical role-descriptions (S17 line 6)
- Per-deliverable agent column in a markdown table (S17 line 21+)

### Verbatim samples

**S16** (`sessions/archive/session-16/session-16-final.md` lines 6-10):

```
## Authors
- **Gen-Physicist** (designated writer, master priority ranking, Bayesian analysis)
- **KK-Theorist** (geometric assessment, corrections, Session 17 seeds)
- **Sim-Specialist** (implementation roadmap, risk analysis, code specifications)
- **Sagan-Empiricist** (Venus Rule audit, pre-registration integrity, empirical assessment)
```

**S17** (`sessions/archive/session-17/session-17-final.md` lines 5-6):

```
## Agents: Baptista-Spacetime-Analyst, Hawking-Theorist, Schwarzschild-Penrose-Geometer, Dirac-Antimatter-Theorist
## Synthesis Team: KK-Theorist (structural), Hawking-Theorist (thermodynamic/writer), Sagan-Empiricist (evidential)
```

**S17 deliverable table** (lines 19-21+; first three rows shown):

```
| # | ID | Phase | Deliverable | Agent | Key Result |
|:--|:---|:------|:------------|:------|:-----------|
| 1 | B-1 | 17a | Gauge coupling derivation | Baptista | g_1/g_2 = e^{-2s}. |
| 3 | H-1 | 17a | Coleman-Weinberg V_eff | Hawking | 0/40 raw minima. |
| 5 | SP-1 | 17a | Explicit 8x8 metric | SP-Geometer | g_s = 3 diag(...) |
```

### Extractor

`extract_g2(text, session_id)` covers all three sub-variants:
1. `G2_AUTHORS_BLOCK_RE` for the bulleted `## Authors` block
2. `G2_AGENTS_LINE_RE` for `## Agents:` / `## Synthesis Team:` comma-lists
3. `G2_TABLE_HEADER_RE` + `G2_TABLE_ROW_RE` for deliverable-table agent column

Per-session deduplication (`seen` set) ensures an agent attributed via multiple sub-variants in the same session emits one edge.

### Edge yield

- 11 edges total across 3 sessions
- Edge type: `authored_by: session → researcher`, role=`primary`
- Confidence: `header-parsed`

### Known limits

- Per-gate attribution requires the deliverable-table parsing path; the table's "ID" column (e.g., `B-1`, `H-1`, `SP-1`) is the per-gate identifier but the current extractor only emits session-level edges. Phase 1 harvester should upgrade G2 deliverable-table parsing to emit per-gate `authored_by` edges keyed on the ID column.

---

## G3 — Per-File Author Header / Collab Era (S19-S35)

### Defining markers

- Filename pattern `session-N-<agent>-collab.md`, `-synthesis.md`, `-verdict.md`, `-wrapup.md`, `-constraint-audit.md`, `-deepdive.md`
- Header: `**Author**: <Name>` or `**Author**: <Name> (<canonical-id>)`
- Review-subtype header: `**Evaluator**: <agent>` for files where one agent reviews another's prior work
- Cross-link header: `**Subject**: <sibling-file-or-section>` identifying the reviewed work
- Stance header: `**Posture**: <descriptor>` (blind evaluation, sympathetic review, etc.)

### Verbatim samples

**S19** (`sessions/archive/session-19/session-19d-berry-collab.md` line 2):

```
**Author**: Berry-Geometric-Phase-Theorist
```

**S22** (`sessions/archive/session-22/session-22-baptista-collab.md` line 2 — parenthetical canonical ID):

```
**Author**: Baptista (baptista-spacetime-analyst)
```

**S19** review file (`sessions/archive/session-19/session-19d-feynman-quantum-acoustics-collab.md` lines 1-6 — multi-agent filename is reviewer×reviewee):

```
# Feynman Evaluation of Quantum-Acoustics Collaborative Review (Session 19d)

**Date**: 2026-02-15
**Evaluator**: Feynman-Theorist
**Subject**: `sessions/QuantumAcoustics-Collab-19d.md`
**Posture**: Blind evaluation. Honest physics, no cheerleading.
```

**S40** (parenthetical role-tags, not canonical ID):

```
**Author**: Baptista (Spacetime Analysis, KK Geometry, Metric Spaces)
```

### Extractor

`extract_g3(text, file_id, filename)`:
1. `G3_AUTHOR_RE` for `**Author**:` headers (with optional parenthetical)
2. `G3_EVALUATOR_RE` for `**Evaluator**:` → emit `reviewed_by` edge with role=`adversarial_review`
3. `G3_FILENAME_AGENT_RE` filename-fallback when no header present

Multi-agent filenames like `feynman-quantum-acoustics-collab.md` are NOT co-authored — the body's `**Evaluator**:` field disambiguates the authoring agent from the reviewed subject.

### Edge yield

- 220 edges total across 17 sessions
- 219 × `authored_by` + 1 × `reviewed_by`
- Top agents: baptista (20), connes (15), feynman (14), dirac (13), landau (13), einstein (12)

### Known limits

- Per-gate attribution inside a multi-gate `-collab.md` file requires "nearest preceding `**Author**:`" heuristic; current extractor emits per-file edges, not per-gate. Phase 1 could refine if gate-IDs are extractable from `## §...` headings within the file.
- The `**Posture**:` and `**Subject**:` fields carry useful provenance metadata; current extractor only consumes them for review-vs-author disambiguation. Future extension: emit `reviews: file → file` edges from `**Subject**:` fields.

---

## G4 — Workingpaper Anchor (S36-S60)

### Defining markers

- Master synthesis: `session-N-results-workingpaper.md` (single file per session)
- Per-agent collab files continue (filename pattern from G3)
- Named workshops emerge: `session-N-{a}-{b}-workshop.md` (multi-agent collaborations)
- New attribution variants:
  - `**Author**: Team-lead (direct synthesis)` orchestrator self-attribution (S50+)
  - Agent-with-title: `**Author**: Katie Mack (Cosmic Bridge Agent)` (S58+)

### Verbatim samples

**S50** (orchestrator self-attribution, `session-50-51-collective-analysis.md`):

```
**Author**: Team-lead (direct synthesis)
```

**S58** (agent-with-title):

```
**Author**: Katie Mack (Cosmic Bridge Agent)
```

### Extractor

Inherits G3's `extract_g3()` regex set. `canonicalize_agent()` handles:
- `Team-lead` / `team_lead` → `orchestrator` (meta-agent, not in `.claude/agents/`)
- `Katie Mack` / `Katie-Mack` / `Cosmic-Bridge` → `mack-cosmic-bridge`

### Edge yield

- 370 edges total across 25 sessions (largest G3-format yield)
- Top agents: volovik (38), nazarewicz (37), baptista (30), quantum-acoustics (30), tesla (27), landau (23)

### Known limits

- Same per-gate granularity gap as G3.
- Named workshops (`<a>-<b>-workshop.md`) currently treated as G3 files; could emit `participates_in: a → workshop` + `participates_in: b → workshop` from filename if workshop structure recognized.

---

## G5 — Wave-Decomposed (S61-S77)

### Defining markers

Two file-shape sub-variants:
- `session-N-wave{K}-workingpaper.md` (multiple WPs per session; S61 has 9 wave-WPs)
- `cc-path-{a..f}.md` (path-split investigations; S63)
- `session-N-audit-<agent>.md` (per-agent audits; S72)
- Multi-collab workshop: `session-N-<workshop>-<reviewer>-collab.md` (S72)

The critical NEW pattern is **per-gate attribution via parenthetical-in-heading**:

### Verbatim sample (S61 wave2, line 23)

```
### HAWK-1: Zeta-Function Regularization Cross-Check of a_2 (hawking-theorist)
```

Gate ID `HAWK-1` is in the heading; author `hawking-theorist` is in parens at the end. This pattern is dense across G5 wave-WPs (S61 alone yielded ~200 edges via this path).

### Extractor

`extract_g5_per_gate(text, file_id)` uses `G5_HEADING_AGENT_RE` to capture `(gate_id, agent_id)` per heading. Also runs G3's `extract_g3()` for files that retain the `**Author**:` header convention.

### Edge yield

- **669 edges total** across 18 sessions — second-largest yield by edge count (after G7)
- 37.2 edges/session average — highest density before G7
- Top agents: mack-cosmic-bridge (54), baptista (53), landau (51), einstein (45), gen-physicist (45), connes (43)

### Known limits

- Pattern requires gate-ID to be UPPERCASE in heading (`HAWK-1`, `KK-2`, etc.). Mixed-case gate IDs would miss.
- Some G5 audit-files use the `audit-<agent>.md` filename pattern; current extractor catches via G3's filename fallback. Forward improvement: emit `audited: agent → session` edge type to distinguish from regular authorship.

---

## G6 — Compaction + Owner-per-Gate (S78-S81)

### Defining markers

- File count drops to 1-4 per session; the WP carries everything
- **NEW header pattern**: `**Owner**: <canonical-id>` per gate-section
- Owner field uses lowercase canonical subagent IDs
- Special non-agent Owner: `**Owner**: synthesized across Wave N (not a single-agent gate)` for orchestrator-aggregated sections

### Verbatim samples (S78 `session-78-results-workingpaper.md`)

The 296KB file has 29 `**Owner**:` lines, each per gate-section. Lines 103-2813. Examples:

```
**Owner**: synthesized across Wave 1 (not a single-agent gate)    [line 103]
**Owner**: transit-dynamics-theorist                              [line 164]
**Owner**: einstein-theorist                                       [line 256]
**Owner**: lizzi-spectral-functional-theorist                     [line 838]
**Owner**: volovik-superfluid-universe-theorist                   [line 1682]
**Owner**: mack-cosmic-bridge                                     [line 1800]
```

### Extractor

`extract_g6(text, file_id)`:
1. Scan with `G6_OWNER_RE` for each Owner line
2. Bind each Owner to the nearest preceding gate-section heading via `G6_GATE_HEADING_RE` (matches `### §W{N}-{M}` or canonical-ID-shape headings)
3. Non-agent Owner values emit `synthesized_by: gate → (wave-synthesis)` instead of `authored_by`

### Edge yield

- 30 edges across 4 sessions (high density per session — S78 alone has ~29)
- 29 × `authored_by` (per-gate) + 1 × `synthesized_by`

### Known limits

- Gate-section heading regex is narrow; if S78 uses non-canonical section headings, some Owner lines may not bind to a gate ID.
- The `(wave-synthesis)` placeholder for non-agent Owner values is a deferred concept — Phase 1 should resolve to actual wave-anchor IDs.

---

## G7 — Registry-Anchored Wave-WPs + Multi-Author Roles + Provenance (S82-S91)

### Defining markers

Five new pattern variants stack:

1. **Per-gate `**Agent**:` header** — primary attribution (most common in G7; ~688 edges in dry-run)
2. **Multi-author tuples**: `**Agent**: <a> PRIMARY + <b> CO-AUTHOR (<role-notes>)`
3. **Semicolon-separated author list**: `**Author**: <a> PRIMARY; <b> CO-AUTHOR; <c> BLACKLISTED` (S88 pending-edits-ledger pattern)
4. **`> **Provenance**:` blockquote** — cross-session citation: `> **Provenance**: S<N> <wave> (<agent> sole writer ...)`
5. **Workshop format** (in `sessions/session-N/workshops/*.md`):
   - `**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)`
   - `**Agents**: <short-name> (<canonical-id>), <short-name> (<canonical-id>)`
   - `## Round N — <agent-short-name>: <round title>`

### Verbatim samples

**S86** (`session-86-w0a-workingpaper.md`):

```
**Agent**: orchestrator (lizzi-spectral-functional-theorist dispatched first; reconnaissance preserved, edits delegated up after permission-block)
```

**S86** (`session-86-w15-workingpaper.md`):

```
**Agent**: `kaku-speculative-theorist` (primary, executed)
```

**S88** (`session-88-w7c-workingpaper.md`):

```
**Agent**: `lizzi-spectral-functional-theorist` PRIMARY + `connes-ncg-theorist` CO-AUTHOR (NCG-axiomatic side per Chamseddine-Connes 1996 + Andrianov-...)
```

**S88** (`s88-pending-edits-ledger.md`):

```
**Author**: volovik PRIMARY; connes CO-AUTHOR; hawking BLACKLISTED
```

**S86 workshop** (`sessions/archive/session-86/workshops/s86-alpha-s-tension-and-sign-lock.md` lines 4-5, 35):

```
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: connes (connes-ncg-theorist), volovik (volovik-superfluid-universe-theorist)

## Round 1 — connes: Opening Analysis
```

**S90** (Provenance block):

```
> **Provenance**: S89 W7c (`mack-cosmic-bridge` sole writer per joint-theorem-promotion §Stage 2; this rule promotion lifts the K=3 calibration)
```

### Extractor

`extract_g7(text, file_id)` and `extract_workshop_g7(text, workshop_id)`:

| Pattern | Regex | Edge type emitted | Role |
|---|---|---|---|
| `**Agent**:` plain | `G7_AGENT_RE` | `authored_by` | `primary` |
| `**Agent**:` with role tuples | `G7_AGENT_RE` + `G7_ROLE_TUPLE_RE` | `authored_by` / `co_authored_by` / `reviewed_by` / `excluded_from` | tag-dependent |
| `**Author**:` semicolon-list | `G7_AUTHOR_MULTI_RE` + clause split + `G7_ROLE_TUPLE_RE` | same as above | tag-dependent |
| `> **Provenance**:` | `G7_PROVENANCE_RE` + `G7_PROVENANCE_SESSION_RE` + `G7_PROVENANCE_AGENT_RE` | `cites_prior_session` + `authored_by` | `sole_writer` |
| Workshop `**Agents**:` | `G7_WORKSHOP_AGENTS_LINE_RE` + `G7_WORKSHOP_AGENT_ENTRY_RE` | `participates_in` | `participant` |
| Workshop `## Round N — agent:` | `G7_WORKSHOP_ROUND_HEADING_RE` | `authored_round` | `round_author` |

### Role-tag vocabulary (G7)

| Tag | Canonical role | Edge type |
|---|---|---|
| `PRIMARY` | `primary` | `authored_by` |
| `CO-AUTHOR` | `co_author` | `co_authored_by` |
| `CO-SIGN` | `co_sign` | `co_authored_by` |
| `CO-SIGN-WITH-NOTES` | `co_sign_with_notes` | `co_authored_by` |
| `ADVERSARIAL REVIEW` | `adversarial_review` | `reviewed_by` |
| `BLACKLISTED` | `blacklisted` | `excluded_from` |
| `sole writer` / `sole-writer` | `sole_writer` | `authored_by` |

### Edge yield

- **1,101 edges total** across 10 sessions — largest yield (45% of grand total)
- 110.1 edges/session average — by far the densest generation
- Per-edge-type: `authored_by=688`, `authored_round=236`, `participates_in=100`, `co_authored_by=51`, `cites_prior_session` (counted as part of authored_by in dry-run; will split in Phase 1)
- Per-role: `primary=670`, `round_author=236`, `participant=100`, `co_author=38`, `sole_writer=18`, `co_sign=13`, `blacklisted=12`, `orchestrator=8`, `adversarial_review=2`
- Top agents: connes (251), lizzi (187), mack (154), volovik (124), gen-physicist (111), landau (47)

### Known limits

- BLACKLISTED entries (12 in dry-run) emit `excluded_from` edges — useful but represents agents NOT involved, which is a different graph-semantic from authorship. The Genealogy view should render these as crossed-out connections (negative authorship).
- Provenance blocks may cite MULTIPLE prior sessions; current extractor takes the first session match. Multi-cite parsing is forward work.
- The orchestrator meta-agent appears 8 times — represents user-triggered orchestrator-direct-writes. Treat as a synthetic agent in graph rendering.

---

## Edge-type emission summary

| Edge type | Emitted by | Source | Target | Cardinality (dry-run) |
|---|---|---|---|---:|
| `authored_by` | G2-G7 | gates/files/sessions | researchers | 2,121 |
| `discussed_in` | G1 | researchers | sessions | 44 |
| `co_authored_by` | G7 | gates | researchers | 51 |
| `reviewed_by` | G3, G7 | gates/files | researchers | 3 (will grow with Provenance-aware parse) |
| `excluded_from` | G7 | gates | researchers | 12 (BLACKLISTED tags) |
| `participates_in` | G7 (workshops) | researchers | workshops | 100 |
| `authored_round` | G7 (workshops) | researchers | workshops (with `#round-N` suffix) | 236 |
| `cites_prior_session` | G7 (Provenance) | gates | sessions | ≤18 (deferred split from authored_by-sole_writer) |
| `synthesized_by` | G6 | gates | sessions (wave-synthesis placeholder) | 1 |
| **TOTAL** | — | — | — | **2,568** |

The total here (2,568) exceeds the dry-run grand total (2,445) because some edges are emitted by multiple sub-extractors against the same source — e.g., G7 Provenance blocks emit both `cites_prior_session` AND `authored_by`. Phase 1 harvester should dedupe by (edge_type, source_id, target_id) tuple before inserting into `knowledge.db::edges`.

---

## Generation-detection algorithm

```python
def session_to_generation(session_id: str) -> str:
    # Strip sub-letter (S73a → 73)
    m = re.match(r"(\d+)", session_id)
    if not m:
        return "?"
    n = int(m.group(1))
    if n <= 15: return "G1"
    if n <= 18: return "G2"
    if n <= 35: return "G3"
    if n <= 60: return "G4"
    if n <= 77: return "G5"
    if n <= 81: return "G6"
    return "G7"
```

Boundaries are session-number-keyed. Sub-letter sessions (S17a/S17b/S73a/S73b) inherit their parent's generation. This is **mechanical routing** — the regex set's coverage decides actual yield per session.

---

## Boundary-evidence citations

| Transition | Evidence |
|:-----------|:---------|
| G1 → G2 (S15 → S16) | `sessions/archive/session-16/session-16-final.md:6` introduces `## Authors\n- **Gen-Physicist** (designated writer...)`; no G1 file has this. |
| G2 → G3 (S18 → S19) | `sessions/archive/session-19/session-19d-berry-collab.md:2` introduces `**Author**: Berry-Geometric-Phase-Theorist`; first per-file header. |
| G3 → G4 (S35 → S36) | S36 introduces `session-N-results-workingpaper.md` as single master synthesis; scan shows S36 has 22 `**Author**:` hits across 21 collab files + 1 WP. |
| G4 → G5 (S60 → S61) | `sessions/archive/session-61/session-61-wave1-workingpaper.md` is the first `wave{N}-workingpaper` filename; S61 has 9 such files. |
| G5 → G6 (S77 → S78) | `sessions/archive/session-78/session-78-results-workingpaper.md` introduces 29 `**Owner**: <canonical-id>` per-gate attribution at lines 103-2813. |
| G6 → G7 (S81 → S82) | S82 introduces `**Agent**:` per-gate (S82+) and the `workshops/` subdirectory standard with structured `**Agents**:` + `## Round N — agent:` round-binding (`s86-alpha-s-tension-and-sign-lock.md:4-5,35`). |

---

## Coverage gaps + forward improvements (Phase 1 carry-forward)

The dry-run baseline of 2,445 edges is the **author-attribution slice** only. The chain-of-custody work (Phase 3) needs four additional edge types that are NOT currently extracted:

1. **`carries_forward: gate → gate`** — parse session-plan markdown (`sessions/session-plan/session-N-plan-W.md`) for the canonical 4-field carry-forward specs. Each spec names a predecessor and a successor gate. Estimated yield: ~1,500-3,000 edges across S30+ sessions.

2. **`anchored_in: gate → session`** — re-type the existing 1,402 `reproduces gates → sessions` rows in `knowledge.db::edges`. The data is already present; only the type-tag needs adjustment.

3. **`cited_in: researcher → constant/theorem`** — walk `researchers/<domain>/*.md` for `RE_LOOSE_GATE_ID` + `_CONSTANT_NAME_STRICT` matches from `tools/harvest_archive_edges.py`. Estimated yield: ~500-1,000 edges.

4. **`succ_of: gate → gate`** — within-wave gate adjacency derived from gate-ID suffix structure (W1-2, W1-3, W1-4 form a sequence). Estimated yield: ~2,000 edges, mostly informational.

Phase 1 harvester (`tools/harvest_attribution_edges.py`) implements (1) attribution edges via this spec, (2) the four additional edge types above, and (3) idempotent insertion into `knowledge.db::edges` keyed on `(type, source_type, source_id, target_type, target_id)` UNIQUE constraint.

---

## Known per-session anomalies

| Session | Anomaly | Mitigation |
|:--------|:--------|:-----------|
| S03 | Directory missing from filesystem | Skip; no inference possible |
| S07 | Directory missing from filesystem | Skip |
| S17a, S17b | Sub-letter continuations of S17 | Inherit S17 attribution |
| S73a, S73b | First-class sub-sessions in G5 | Process independently |
| S78 | 296KB single WP with 29 Owner-per-gate lines | High-density G6; verified |
| S82 | Mixed G6/G7 — has both `**Owner**:` and `**Agent**:` patterns | Both extractors run on G7 sessions |
| S87 | Only 2 files (`results-workingpaper.md` + `workshop-schedule.md`) — schedule has no attribution | Schedule files contribute 0 attribution edges; expected |

---

## Self-test fixture inventory

The regex module ships with 18 self-test fixtures, each a verbatim extract from a real session file. Run:

```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/_format_generation_regex_set.py --self-test
```

| Fixture | Source file | Generation tested |
|---|---|---|
| `G2-S16-authors-block` | S16 final §6-10 | G2 sub-(a) |
| `G2-S17-agents-line` | S17 final line 5 | G2 sub-(b) |
| `G2-S17-synthesis-team` | S17 final line 6 | G2 sub-(b) |
| `G2-S17-deliverable-table` | S17 final line 21+ | G2 sub-(c) |
| `G3-S19-author-direct` | S19d berry-collab line 2 | G3 |
| `G3-S22-author-parenthetical` | S22 baptista-collab | G3 |
| `G3-S19-evaluator` | S19d feynman-qa-collab lines 1-6 | G3 review |
| `G3-S40-author-paren-roles` | S40 baptista-collab | G3 variant |
| `G4-S50-team-lead` | S50-51 collective-analysis | G4 orchestrator |
| `G4-S58-mack-cosmic-bridge` | S58 back-to-basics | G4 |
| `G5-S61-heading-paren-agent` | S61 wave2 line 23 | G5 per-gate |
| `G6-S78-owner-transit-dynamics` | S78 WP line 164 | G6 |
| `G6-S78-owner-non-agent` | S78 WP line 103 | G6 wave-synthesis |
| `G7-S86-agent-backticked` | S86 w15 | G7 plain |
| `G7-S88-multi-author-roles` | S88 pending-edits-ledger | G7 semicolon list |
| `G7-S88-agent-primary-coauthor` | S88 w7c | G7 multi-author tuple |
| `G7-S90-provenance` | S90 w2 | G7 Provenance block |
| `G7-S86-workshop-agents-and-round` | S86 alpha-s workshop lines 4-5, 35 | G7 workshop |

**Self-test status at landing**: 18 PASS / 0 FAIL.

---

## Consumer gates

Phase 1+ consumers of this registry:

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| `S91-HARVEST-ATTRIBUTION-EDGES` | S91+ | OUTPUT-WRITER | Implements harvester per this spec |
| `S91-CHAIN-OF-CUSTODY-BUILD` | S91+ | OUTPUT-WRITER | Consumes harvester output to build `chain_of_custody.json` sidecar |
| `S91-ROUTING-MANIFEST-V2-BUMP` | S91+ | OUTPUT-WRITER | Bumps manifest version after new edge types land in `knowledge.db` |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-05-17 | Phase-0 / Task #6 | Initial landing — 7 generations cataloged, 18 self-test fixtures, dry-run baseline 2,445 edges | orchestrator |

---

## Migration notes

This is a fresh landing (not an AMRI promotion). The methodology spec did not previously exist in agent memory or anywhere else — it is built from Phase-0 evidence (the inventory scan + targeted file reads + regex self-test + corpus dry-run).
