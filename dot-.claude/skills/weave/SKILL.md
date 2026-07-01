---
name: weave
description: Query and maintain the project knowledge index (including sessions/framework/ capstone registries)
argument-hint: --update | --show <type> | --show equations [type|named] | --trace "entity" | --provenance file | --search "keyword" | --stats | --validate | --audit-constants | --graph | --timeline | --mermaid | --viz-all | --db-sync | --db-search "query" | --show registries | --framework-diff | --export-manifest
---

# Knowledge Weave — Query the Project Index

Read, query, and maintain the structured knowledge index at `tools/knowledge-index.json`.

## Usage

```
/weave --update                    # Rebuild the index from source files
/weave --show theorems             # PROVEN theorems table
/weave --show closed                 # Closed mechanisms table
/weave --show gates                # Gate verdicts table
/weave --show trajectory           # Probability timeline
/weave --show open                 # OPEN channels table
/weave --show researchers          # Researcher cross-map
/weave --trace "CPT"               # Evidence chain for an entity
/weave --provenance s24a_vspec.npz # Script→data→gate lineage
/weave --show equations             # Equations by type (display/inline/code/etc)
/weave --search "keyword"          # Search across all entity fields
/weave --stats                     # Summary counts
/weave --validate                  # Consistency checks
/weave --graph                     # Knowledge topology PNG
/weave --timeline                  # Probability trajectory PNG
/weave --mermaid                   # Mermaid diagram to stdout
/weave --viz-all                   # All visualizations (5 PNGs + Mermaid)
/weave --db-sync                   # Rebuild SQLite database
/weave --db-search "BCS gap"       # FTS5 ranked search
/weave --db-query gates V-1        # Direct entity lookup
/weave --show registries           # Framework capstone registry inventory
/weave --framework-diff            # Cross-check session entries vs framework-canonical entries
/weave --export-manifest           # Build routing_manifest.json (consumer = meme-engine-web Astro rewriter)
/weave --audit-paths               # Audit dead path references under computations/ (post-_phase3 cleanup)
```

## Framework Registries (`sessions/framework/`)

Files under `sessions/framework/` are the **canonical destination** for knowledge. Entries from these files:

- Are stored in the new `registries` top-level bucket (one meta-entry per file) + promoted into `theorems` / `closed_mechanisms` / `gates` / `open_channels` as row-level entities.
- Carry `origin: "framework-registry"` and a `registry_id` pointer to the source file.
- Win dedup collisions over session-level entries via **priority 7** (above `synthesis` = 4 and `sagan-verdict` = 5). When a session file mentions "n_s = 0.9590" and the framework registry pins "n_s = 0.9590 (ZERO-FREE-PARAMETER, ref S65)", the framework entry wins and the session entry is dropped.
- If the framework value disagrees with a session value, `/weave --framework-diff` flags it — the framework is authoritative.

### Schema support
Four schemas are parsed:
- **Registry template** — YAML frontmatter `type: registry` + `**Registry ID**:` header + `## Summary table` (e.g. `framework-dm-properties.md`, `cross-channel-correlation-matrix.md`).
- **Falsifier-rigor / SHA-pinned** — `**Gate**:` + `**Closure SHA-256**:` header + `## Channel Table` (e.g. `falsifier-rigor-registry.md`).
- **Pre-registered observations** — per-detector H2 sections each with their own prediction tables (e.g. `pre-registered-observations.md`).
- **Atlas narrative** — numbered `## N. Title` H2 sections without tables (e.g. `Atlas/atlas-10-breakthrough-genealogy.md`).

## Parse Arguments

Extract the subcommand and argument from `$ARGUMENTS`. The first token after `/weave` is the subcommand flag. Anything after it is the argument.

## Subcommand Implementations

### `--update`

Rebuild the index from end to end. The chain is seven discrete phases — each must complete before the next, because each consumes the previous phase's output:

```
# Phase 1 — harvest fresh edges from filesystem sources
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/harvester.py archive
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/harvester.py provenance

# Phase 2 — rebuild knowledge-index.json from all sources (sessions, computations, harvested edges)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py

# Phase 3 — sync JSON into SQLite (knowledge.db)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/knowledge_db.py --sync

# Phase 4 — rebuild the console's bundled data.js from SQLite
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/viz/console/build_data.py

# Phase 5 — rebuild summary/topics/<class>.md pages from SQLite (S86+)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/build_topic_pages.py

# Phase 6 — emit routing_manifest.json for the meme-engine-web Astro rewriter
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/export_routing_manifest.py --check

# Phase 7 — audit dead path references under computations/ (post-_phase3 cleanup gate; WARN-only)
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/path_existence.py audit --json
```

**Supersedes-chain consumer adoption** (S91 W0 R6 landing per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"` item 3, 2026-05-16): Phase 2 (`tools/extract_entities.py`) reads `s{N}_gate_verdicts.txt` files. For gates with corrective successors carrying `supersedes=<full-64-char-old-audit-sha>` tags, downstream consumers MUST follow the supersession chain — the latest non-superseded line per gate-ID is the canonical entry; the original line is RETAINED on disk per absolute verdict permanence but EXCLUDED from canonical reading. The canonical adoption interface is `_consolidate_intake.resolve_supersession_chains(records, verdict_file_text)` which returns `{'canonical_records', 'superseded_records', 'canonical_latest_per_gate', 'pointers', 'superseded_shas'}`. Consumers (extract_entities.py knowledge-MCP indexer, plan-freeze auditors, viz/console build_data.py) SHOULD import this resolver when they need canonical-reading semantics. Calibration corpus: S88 W8-100 N=3 trios + S90 W2-2 + W2-7 correctives (5 + 8 = 13 known supersedes pointers across S88-S90 verdict files; verified at `computations/_shared/s91_w0_r6_supersession_test.py`).

**Why all seven phases**: each output downstream depends on the upstream. `extract_entities.py` reads the harvested `computations/_shared/*_edges.txt` files (so harvesters run first); `knowledge_db.py --sync` consumes `knowledge-index.json` (so JSON rebuild precedes); `build_data.py`, `build_topic_pages.py`, and `export_routing_manifest.py` all read `knowledge.db` (so DB sync precedes). `build_topic_pages.py` reads the `classes` and `class_edges` tables (S86+) plus imports `canonical_constants.py` for value resolution; it emits one markdown topic page per class to `summary/topics/`. `export_routing_manifest.py` joins the entity tables with the `PROVENANCE` dict from `canonical_constants.py` and serializes the regex inventory imported from `extract_entities.py` + `harvest_archive_edges.py`, producing `tools/routing_manifest.json` (~8 MB) — the cross-link resolution contract the meme-engine-web Astro build binds to. Phase 6 runs with `--check` so a quality regression in any upstream extractor (placeholder edges leaking, theorems with scrambled columns, gates without sessions) fails the rebuild loudly. Phase 7 (post-`_phase3` cleanup gate) runs `_path_existence_audit.py --json` to detect dead `Path()` / `os.path.join()` references under `computations/` — bare `computations/X.py` references that the abandoned `_phase3_path_string_migration.py` was supposed to fix. The audit is WARN-only inside `/weave --update` (always exits 0) so a new dead reference does NOT block the index rebuild; for CI gating, run `tools/path_existence.py audit --strict` standalone (exits 1 on any dead ref). Refs annotated `# soft prereq` / `# planned` / `# expected missing` are recognized as forward-pinned (legitimate references to outputs from gates that haven't run yet) and excluded from the dead-refs list. Skipping any phase leaves the next out of date.

**Optional second pass** (only if the session you just ingested registered new theorems / equations / closed mechanisms — these harvesters read the freshly-synced DB):

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/harvester.py theorem-closure
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/harvester.py equation
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/knowledge_db.py --sync
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/viz/console/build_data.py
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/build_topic_pages.py
```

Report the statistics output of each phase to the user (file scan counts, edge tally, DB row counts, data.js byte size).

### `--show theorems`

1. Read `tools/knowledge-index.json` using the Read tool.
2. Parse the JSON.
3. Format the `theorems` array as a markdown table:

| # | Theorem | Sessions | Precision | Source |
|:--|:--------|:---------|:----------|:-------|

Sort by session number (ascending). Show all entries.

### `--show closed`

1. Read `tools/knowledge-index.json`.
2. Format the `closed_mechanisms` array as a markdown table:

| # | Mechanism | Session | Closed By | Gate ID |
|:--|:----------|:--------|:----------|:--------|

Sort by session number.

### `--show gates`

1. Read `tools/knowledge-index.json`.
2. Format the `gates` array as a markdown table:

| Gate | Session | Condition | Result | Verdict | BF |
|:-----|:--------|:----------|:-------|:--------|:---|

Highlight CLOSED verdicts with bold. Show BF if available.

### `--show trajectory`

1. Read `tools/knowledge-index.json`.
2. Format the `probability_trajectory` array as a timeline:

```
Session  | Panel  | Sagan  | Key Event
---------|--------|--------|-----------
prior    | 2-5%   |        | Theoretical
7-8      | 10-15% |        | KO-dim=6
...
24a/24b  | 5%     | 3%     | V-1 CLOSED
```

Only show entries that have panel or sagan values (skip empty ones).

### `--show open`

1. Read `tools/knowledge-index.json`.
2. Format the `open_channels` array as a markdown table:

| Channel | Detail | Session |
|:--------|:-------|:--------|

### `--show researchers`

1. Read `tools/knowledge-index.json`.
2. Format the `researchers` array as a markdown table:

| Domain | Papers | Citations | Sessions Referenced | Description |
|:-------|:-------|:----------|:-------------------|:------------|

Sort by citation count (descending).

### `--show equations`

1. Read `tools/knowledge-index.json`.
2. Parse the `equations` array (12,000+ entries after dedup).
3. Group by `type` (display, inline, structural, code, comment).
4. For each type, show count, named count, and the first 10 examples:

```
Type: display (111 equations, 111 named)
  eq_42  | Spectral Action          | s24a_vspec.py:15        | $$V_{spec}(\tau) = a_2 R + a_4 R^2$$
  eq_43  | Seeley-DeWitt Coefficients | session-20a-synth.md:88 | $$\text{Tr}(f(D^2/\Lambda^2)) = \sum a_n$$
  ...

Type: code (8,333 equations, 81 named)
  eq_500 | BCS Gap Equation         | s23a_bcs_gap.py:42      | M_evals, M_evecs, M_max, M_matrix = linearized_bcs(...)
  ...
```

Show the `name` column when an equation has one; show `—` when `name` is null.
If the equation has an `errata` field, append ` [ERRATA]` after the raw text.

If the user specifies a type (e.g., `--show equations display`), filter to that type only and show up to 50 entries.
If the user specifies `--show equations named`, show ONLY equations that have a non-null `name`, across all types, up to 100 entries.

### `--show registries`

1. Read `tools/knowledge-index.json`.
2. Format the `registries` array as a markdown table:

| Registry ID | Title | Owner agents | Summary rows | Consumer gates | Last updated | Content SHA |
|:------------|:------|:-------------|:------------:|:--------------:|:-------------|:------------|

Sort alphabetically by `registry_id`. Show `—` where the field is null. This is the capstone inventory — every file under `sessions/framework/` appears as one row. Rows with `target_buckets = []` are discussion/prose files (no row-level extraction); rows with non-empty `target_buckets` have promoted entries visible via `/weave --show theorems` etc. (tagged `origin: framework-registry`).

### `--framework-diff`

Run the framework rectification diff (Phase 2 of the framework-ingestion fix):

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/framework_diff.py
```

For each entity that is present in both a framework registry (origin = `framework-registry`) AND a session-level source (other origin), compare the status / verdict / precision / detail fields. Mismatches are written to `tools/framework_diff_report.md` as WARRANT lines framed as "framework authoritative — investigate session file". Matches are reported as count summaries only (not per-entry).

### `--trace "entity"`

1. Read `tools/knowledge-index.json`.
2. Search the entity name (case-insensitive) across ALL entity types: theorems, closed_mechanisms, gates, open_channels.
3. For each match:
   - Show the full entity record.
   - Read the `source_file` using the Read tool to get surrounding context (±10 lines around the entity mention).
   - List related entities (same session, same gate_id, or name substring matches in other entities).
4. Format as an evidence chain showing how the entity connects to other findings.

### `--provenance <filename>`

1. Read `tools/knowledge-index.json`.
2. Search `data_provenance` for entries where:
   - `script` matches the filename, OR
   - any item in `outputs` matches the filename, OR
   - any item in `inputs` matches the filename.
3. For each match, show the full provenance chain:
   ```
   Script: s24a_vspec.py
   Session: s24a
   Inputs: [list of .npz files loaded]
   Outputs: [s24a_vspec.npz, s24a_vspec.png]
   Gates informed: [V-1, V-3]
   ```
4. If a gate is listed in `gates_informed`, also show the gate verdict from the gates array.

### `--search "keyword"`

1. Read `tools/knowledge-index.json`.
2. Search the keyword (case-insensitive) across ALL fields of ALL entity types.
3. For each match, show:
   - Entity type (theorem/closed/gate/session/open/provenance/researcher)
   - Entity name or id
   - The matching field and its value (truncated to 200 chars)
4. Group results by entity type.

### `--stats`

Run the extraction script in stats mode:

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --stats
```

Report the output.

### `--validate`

Run the extraction script in validation mode:

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --validate
```

Report violations (if any) or confirm consistency.

### `--audit-paths`

Run the dead-path-reference audit. Detects `Path()` / `os.path.join()` expressions under `computations/` that resolve to non-existent files — typically the residue of the abandoned `_phase3_path_string_migration.py` migration (bare `computations/X` references that should be `computations/_shared/X` or `computations/session-N/X`).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/path_existence.py audit --json
```

Output: stdout report + `tools/_path_existence_audit_report.json`. Reports total scanned files, alive vs dead vs expected-missing (annotated) counts, top offending files, category breakdown (SESSION-FILE-MISLOCATED / SHARED-HELPER-MISLOCATED / GENERIC-MISLOCATED / UNKNOWN), and per-finding suggested-fix coverage.

For CI gating, append `--strict` (non-zero exit on any dead ref):

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/path_existence.py audit --strict
```

To auto-apply the suggested fixes (~92% coverage on the typical post-migration corpus):

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/path_existence.py fix --dry-run    # preview
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/path_existence.py fix --execute    # apply
```

The fix-applicator handles two substitution shapes: INSERT (`computations/X` → `computations/_shared/X`) and REPLACE (`computations/_shared/sN_X` → `computations/session-N/sN_X`). The remaining ~8% (genuinely-missing files, planned outputs, soft prereqs) need manual annotation with `# soft prereq` / `# planned` / `# expected missing` comments to be recognized as forward-pinned (excluded from dead-refs).

This audit is also Phase 7 of `--update`. Run standalone for ad-hoc audit or CI gating.

### `--export-manifest`

Build the cross-link routing manifest the meme-engine-web Astro site consumes for build-time deep-link rewriting. Joins `tools/knowledge.db` entity tables with the `PROVENANCE` dict from `computations/_shared/canonical_constants.py`, then serializes the regex inventory imported from `tools/extract_entities.py` + `tools/harvester.py archive` into the same JSON file. The Astro rewriter binds to this manifest as a single contract (one source of truth for both the entity tables AND the regex set), so an upstream change to either propagates downstream automatically.

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/export_routing_manifest.py --check
```

Output: `tools/routing_manifest.json` (~8 MB). Report the row counts per table (constants, gates, theorems, mechanisms, open_channels, sessions, researchers, edges) and the source-input SHA-256 prefixes.

The `--check` flag runs validation: minimum-count assertions (constants ≥ 100, gates ≥ 50, theorems ≥ 30, sessions ≥ 50, edges ≥ 30) AND quality assertions (no placeholder-id edges, no theorems with statement < 20 chars, no more than 5% of gates with empty session field). Any failure exits non-zero; investigate before committing the regenerated manifest.

Optional `--out <path>` overrides the default output location. Otherwise the script writes to `tools/routing_manifest.json`.

This is also Phase 6 of `--update`. Run standalone (without re-running the full chain) when only the published-web cross-link table needs refreshing — e.g., after manually editing `canonical_constants.py:PROVENANCE` to add a new entry without changing entity counts.

---

## Visualization Subcommands

These generate PNG graphs and diagrams from the knowledge index.

### `--graph`

Generate the knowledge topology graph (theorems, gates, closed mechanisms, sessions as connected nodes).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --graph
```

Report the output path and file size to the user. Output: `tools/viz/knowledge_graph.png`.

### `--timeline`

Generate the probability trajectory chart (panel + Sagan assessments over sessions, with milestone annotations).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --timeline
```

Report the output path. Output: `tools/viz/probability_timeline.png`.

### `--provenance-graph`

Generate the data provenance flow graph (scripts → outputs → gates).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --provenance
```

Report the output path. Output: `tools/viz/data_provenance.png`.

### `--citations-graph`

Generate the researcher domain citation network.

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --citations
```

Report the output path. Output: `tools/viz/researcher_citations.png`.

### `--gates-graph`

Generate the gate verdict visual summary table.

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --gates
```

Report the output path. Output: `tools/viz/gate_verdicts.png`.

### `--mermaid`

Generate Mermaid flowchart code showing key theorems, gates, and closed mechanisms.

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --mermaid
```

Show the Mermaid code to the user (it prints to stdout). Also writes `tools/viz/knowledge_graph.mmd`.

### `--viz-all`

Generate all visualizations at once (5 PNGs + 1 Mermaid file).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/visualize_knowledge.py --all
```

Report the summary table of all output files and sizes.

---

## SQLite Database Subcommands

These use a SQLite database with FTS5 full-text search for fast ranked queries.

### `--db-sync`

Rebuild the SQLite database from the JSON index.

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/knowledge_db.py --sync
```

Report the row counts per table. Output: `tools/knowledge.db`.

### `--db-search "query"`

Run a FTS5 ranked search across all entity types. Extract the search query from `$ARGUMENTS` (everything after `--db-search`).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/knowledge_db.py --search "QUERY"
```

Show the grouped, ranked results to the user.

### `--db-query TABLE ID`

Look up a specific entity by table name and ID.

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/knowledge_db.py --query TABLE ID
```

Show the full entity record.

### `--audit-constants`

Run the canonical constants audit on S34+ computation scripts. Flags hardcoded values that should import from `computations/_shared/canonical_constants.py`. Scans `computations/_shared/` (active scripts).

```
"phonon-exflation-sim/.venv312/Scripts/python.exe" tools/extract_entities.py --audit-constants
```

Reports compliant scripts (using `from canonical_constants import ...`) and violations (stale hardcoded E_cond, Vol_SU3, M_KK). Scripts from session 33 and lower are exempt (historical). The audit also runs automatically during `--update` and `--validate`.

## Error Handling

- If `tools/knowledge-index.json` does not exist, tell the user to run `/weave --update` first.
- If a `--show` subcommand has no entries, say "No {type} entries found in the index."
- If `--trace` finds no matches, say "No matches found for '{query}'."
- If `--provenance` finds no matches, say "No provenance found for '{filename}'."

## Notes

- The index is the single source of truth. Always read it fresh — never cache.
- For `--trace`, reading the source file provides the human context that the JSON alone cannot capture. Always include the source excerpt.
- The index is generated by `tools/extract_entities.py`. If results look stale, suggest `/weave --update`.
- **Curated equation fields**: Equations may have `name` (human-readable, e.g., "Spectral Action"), `latex` (LaTeX rendering), `audit_status` (ok/typo), and `errata` (correction notes). These are manually curated and preserved across index rebuilds. Use `tools/name_equations.py` to re-apply names after a rebuild.
- **Curated entity fields**: Any entity type may have an `errata` field containing correction notes. These are preserved across rebuilds by `merge_curated_from_existing()` in `extract_entities.py`.
