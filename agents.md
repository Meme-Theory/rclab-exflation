# `/weave` — Knowledge Index

Query and maintain the project knowledge graph at `tools/knowledge-index.json`.

## Commands

### Tier 1: JSON Queries

| Command | Returns |
|:--------|:--------|
| `/weave --show theorems` | PROVEN theorems |
| `/weave --show closed` | CLOSED mechanisms |
| `/weave --show gates` | Gate verdicts (CLOSURE/PASS/FAIL) |
| `/weave --show trajectory` | Probability timeline (panel + Sagan) |
| `/weave --show open` | Surviving rescue routes |
| `/weave --show researchers` | Researcher domain cross-map |
| `/weave --show equations` | Equations by type (display/inline/code), with names |
| `/weave --show equations named` | Only named equations (744 curated) |
| `/weave --trace "CPT"` | Evidence chain for a named entity |
| `/weave --provenance s24a_vspec.npz` | Script → data → gate lineage |
| `/weave --search "keyword"` | Cross-field keyword search |
| `/weave --stats` | Entity counts |
| `/weave --validate` | Consistency checks |
| `/weave --update` | Rebuild index from source files |

### Tier 2: Visualizations

| Command | Output |
|:--------|:-------|
| `/weave --graph` | `tools/viz/knowledge_graph.png` |
| `/weave --timeline` | `tools/viz/probability_timeline.png` |
| `/weave --mermaid` | `tools/viz/knowledge_graph.mmd` |
| `/weave --viz-all` | All 5 PNGs + Mermaid |

### Tier 3: SQLite (FTS5)

| Command | Returns |
|:--------|:--------|
| `/weave --db-sync` | Rebuild SQLite from JSON → `tools/knowledge.db` |
| `/weave --db-search "BCS gap"` | Ranked search across all entities |
| `/weave --db-query gates V-1` | Direct lookup by table + ID |

Use Tier 1 by default. Tier 3 when you need ranked relevance across ~12K entities.

## Architecture

```
sessions/*.md    ─┐
tier0-computation/*.py  ─┼─▶ extract_entities.py ─▶ knowledge-index.json (canonical)
tier0-computation/*.npz ─┘         │                       │
                                   ├── visualize_knowledge.py ─▶ tools/viz/*.png
                                   └── knowledge_db.py ─▶ knowledge.db (query accelerator)
```

JSON is truth. SQLite is rebuilt from JSON via `--db-sync`.

9 entity types: theorems, closed_mechanisms, gates, probability_trajectory, sessions, data_provenance, open_channels, researchers, equations.

### Curated Fields

Certain fields are manually curated and preserved across index rebuilds:

| Field | Entity Types | Description |
|:------|:-------------|:------------|
| `name` | equations | Human-readable name (e.g., "Spectral Action"). 744/12,247 named. Re-apply via `tools/name_equations.py`. |
| `latex` | equations | LaTeX rendering of the equation |
| `audit_status` | equations | ok, typo, etc. |
| `errata` | all entity types | Correction notes |

## Rules

- Source authority: Sagan verdicts > synthesis > gate verdict .txt > other minutes > tier0 filesystem
- Dedup: latest synthesis wins
- Only `knowledge-weaver` agent or `/weave --update` writes to the index

# LaTeX Typesetting Skill

Quick access to LaTeX formatting expertise for the phonon-exflation paper preparation. Backed by 14 reference documents in `researchers/LaTeX/` and the `latex-typesetting-specialist` agent definition.

## Usage

```
/latex --preamble jhep          # Generate JHEP-ready preamble with project macros
/latex --preamble cmp           # Generate CMP/JGP-ready preamble
/latex --preamble prd           # Generate PRD (REVTeX) preamble
/latex --macros                 # Show/generate phonon_exflation.sty macro file
/latex --notation               # Project notation quick reference
/latex --journal jhep           # JHEP style summary and requirements
/latex --journal cmp            # CMP style summary
/latex --journal jgp            # JGP style summary
/latex --journal prd            # PRD (REVTeX) style summary
/latex --check paper.tex        # Review a .tex file for common issues
/latex --arxiv                  # ArXiv submission checklist
/latex --bib                    # Bibliography setup guide (BibTeX vs BibLaTeX per venue)
/latex --index                  # Show the full document index