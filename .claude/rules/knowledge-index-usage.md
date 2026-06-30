---
paths:
  - "tools/**"
---

# Knowledge Index (`/weave` skill + `knowledge-weaver` agent)

The project maintains a structured knowledge graph at `tools/knowledge-index.json` tracking all theorems, closed mechanisms, gate verdicts, probability trajectory, data provenance, open channels, researchers, and equations (~12K) across all sessions.

## Quick Queries (use `/weave` skill directly)
- `/weave --show theorems|closed|gates|trajectory|open|researchers|equations` — formatted tables
- `/weave --trace "CPT"` — evidence chain for a named entity
- `/weave --provenance s24a_vspec.npz` — script->data->gate lineage
- `/weave --search "keyword"` or `/weave --db-search "keyword"` — cross-entity search
- `/weave --update` — rebuild index after adding new session files
- `/weave --viz-all` — generate all visualization PNGs

## Agent Spawn (use `knowledge-weaver` agent)
- **Solo**: spawn alone for full index rebuilds (runs `extract_entities.py`)
- **Teammate**: spawn on a team to answer live structured queries from physicists
- Model: Sonnet (cost-efficient). Never evaluates physics — only indexes and serves.
- See `skills-reference.md` (project root) for full usage guide.

## Rules
- `knowledge-index.json` is the single source of truth. SQLite (`knowledge.db`) is a query accelerator rebuilt via `/weave --db-sync`.
- Source authority: Sagan verdicts > synthesis files > gate verdict .txt > other minutes > computations/ filesystem.
- Deduplication: latest synthesis wins. Only the knowledge-weaver agent (or `/weave --update`) should write to the index.

## MCP as first-class identity-claim surface (plan §4.6)

**Agents MUST query the Knowledge MCP before stating any identity claim** —
a constant value, a gate verdict, a theorem 4-tuple, a closed mechanism status.
File-system reads (`computations/_shared/canonical_constants.py`, session markdown,
registry) are the **fallback** when the MCP is known-stale. Cross-check direction
is ALWAYS script ⇄ MCP — never trust one without the other.

### Required query patterns

| Question | MCP tool | Authority |
|:---------|:---------|:----------|
| "What is constant X's canonical value + provenance?" | `get_constant(X)` | Canonical; prefer over reading `canonical_constants.py` |
| "Has gate G been evaluated?" | `query_entity("gates", G)` | Canonical verdict ledger |
| "Is mechanism M closed?" | `query_entity("closed", M)` | Canonical; prevents re-derivation of settled results |
| "What sessions touched this topic?" | `search_knowledge(query)` | FTS5 across all entity types |
| "What is the evidence chain for concept C?" | `trace_entity(C)` | Cross-type traversal |
| "What constants match a pattern?" | `list_constants(regex)` | Canonical enumeration |
| "What theorems exist?" | `list_entities("theorems")` | Canonical enumeration |
| "Add / update a constant after rerun" | `update_constant(...)` | Write-back path (on PASS match) |
| "Emit a gate verdict line (race-safe)" | `emit_verdict(...)` | Single lock-serialized writer of `s{N}_gate_verdicts.txt`; script prints the payload via `print_verdict_payload`, agent calls the tool |

### Enforcement

- A review, audit, or synthesis that states an identity claim without a
  demonstrated MCP query is **incomplete** and must be re-run.
- Python-review agents (per `script-review-plan.md` §3) MUST
  show MCP query usage for every CLEAN / MINOR / MAJOR / BLOCKER grade that
  turns on an identity claim.
- GPU re-run anchors MUST fetch MCP baseline BEFORE
  modifying the script; compare reproduced value to MCP value; only call
  `update_constant` on match.

### When the MCP is wrong

If `get_constant(X)` returns a value that disagrees with an authoritative
source (registry, canonical_constants.py with `PROVENANCE` comment), that is
a data-ingestion bug in the weave extractor, not a framework fact. Flag via
`/weave --update` + a note in the relevant session file. Do NOT silently
trust the MCP over an audited source — but also do not silently trust the
file over the MCP. Reconcile.
