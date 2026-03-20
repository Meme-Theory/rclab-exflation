# Knowledge Weaver Agent Memory

## Index Location and Schema
- Index: `tools/knowledge-index.json` (schema v1)
- Extraction script: `tools/extract_entities.py`
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Standard library only (re, json, pathlib, argparse, datetime)

## Source Authority Order
1. Sagan verdict files (`*sagan-verdict*.md`) — Bayesian accounting
2. Synthesis files (`*synthesis*.md`) — canonical PROVEN/CLOSED/OPEN registries
3. Gate verdict text files (`s*_gate_verdicts.txt`) — raw classifications
4. Other session minutes — metadata, agent rosters
5. Tier0 filesystem — provenance triples

## Extraction Patterns (Key Lessons)
- Gate tables: use section-restricted matching; unrestricted table regex captures hundreds of false positives
- Closed Mechanism tables: `| name | session | reason | CLOSED |` format — parse by splitting on `|`
- Probability trajectory: two formats: inline `**Post-session probability: X%**` and code-block timeline
- Researcher cross-citations: counted by regex matching `researchers/{domain}/` patterns in meeting minutes
- Deduplication: latest synthesis wins (files processed in priority-ascending order)

## File Format Variations
- Early sessions (9): `## Date: YYYY-MM-DD` headers
- Late sessions (22d+): `**Date**: YYYY-MM-DD` inline in YAML-like headers
- Session IDs extracted from filename when not in content

## Equation Extraction (9th Entity Type)
- Extraction: `extract_equations(filepath, text)` in `extract_entities.py`
- Dedup: `dedup_equations(equations)` — normalizes LaTeX/whitespace, truncates to 100 chars
- 5 types: display ($$...$$), inline ($...$), structural (LHS=RHS), code (Python computations), comment (# formulas)
- PERMANENT USER DIRECTIVE: "the code IS the math" — Python computation lines are first-class equations
- Code equations: inclusive — keep all numeric/math/array computation lines; skip only pure infrastructure (imports, prints, plt, I/O, control flow)
- Equation IDs: `eq_1`, `eq_2`, ... assigned after dedup in authority order

## Tooling Reference
- Visualization: `tools/visualize_knowledge.py` — 7 subcommands (--graph, --timeline, --provenance, --citations, --gates, --mermaid, --all); output to `tools/viz/`
- SQLite accelerator: `tools/knowledge_db.py` — --sync, --search, --query; output `tools/knowledge.db`
- FTS5 indexes all entity names and text; `--search "BCS"` hits closed_mechanisms, open_channels, theorems, sessions, equations
- JSON is canonical; SQLite is query accelerator only

## Behavioral Rules
- Batch processing: when a teammate sends batches sequentially (part 1, then part 2), process ONLY what you have been explicitly told. Do NOT read ahead and apply files before the teammate instructs you. This broke the acknowledgment protocol and caused stale-notification confusion.
- Always wait for explicit instructions per batch part, even if files are already on disk.
