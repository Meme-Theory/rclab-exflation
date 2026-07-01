# Web-Researcher Agent Memory

## Active Context

**Role**: Comprehensive paper researcher & writer for scientific domains (physics, cosmology, mathematics). Generates 14+ markdown reference documents per researcher, with full abstracts, derivations, historical context, and framework-relevance sections.

**Workflow**:
1. Search (arXiv API + Google Scholar) → compile paper list
2. Download PDFs via MCP tools (paper-search)
3. Extract content → write NN_YEAR_Author_ShortTitle.md files
4. Create INDEX.md per researcher (thematic groupings)
5. Include "Connection to Phonon-Exflation Framework" section in every paper

## WebFetch Reliability Matrix

| Source | Status | Priority |
|:-------|:-------|:---------|
| arXiv abs pages | WORKS | PRIMARY — use arXiv API syntax (au:Lastname_Firstname) |
| Google Scholar | WORKS | Secondary for broad discovery |
| MathWorld | WORKS | Math content |
| PubMed | WORKS | Biomedical abstracts |
| Blogs (Baez, etc.) | WORKS | Conceptual foundations |
| HandWiki | WORKS | Wikipedia alternative |
| **AVOID**: Wikipedia (403) | Springer (303) | OUP (403) | ResearchGate (403) | Semantic Scholar (unreliable) | ADS (unreliable) |

## File Conventions

- **Format**: `NN_YEAR_Author_Short_title.md` (zero-padded, underscores for spaces)
- **Length**: 140–250 lines per paper
- **Sections**: Abstract, Historical Context, Key Arguments, Key Results, Impact & Legacy, Connection to Phonon-Exflation
- **ASCII-safe only** — no unicode em-dashes, arrows, checkmarks
- **Use LaTeX** for equations: $...$ notation
- **Mark gaps**: `[INCOMPLETE -- source not accessible]` when fetches fail

## Completed Researchers (19 projects, 2020+ papers)

- **Berry** (14 papers) — geometric phase, quantum chaos
- **Connes NCG** (28 papers) — spectral action, order-one violations, Pati-Salam
- **Baptista** (27 papers) — KK geometry, spectral action at finite density
- **Volovik** (22 papers) — emergent spacetime, 3He analogues
- **Landau** (8 papers) — BCS-BEC thermodynamics, flat bands
- **String Theory** (24 papers) — M-theory, dualities, swampland
- **Schwarzschild-Penrose** (9 papers) — conformal geometry, twistors
- **Tesla-Resonance** (7 papers) — analog gravity, Kibble-Zurek, DESI w=-1
- **Quantum-Foam** (8 papers) — Lorentz invariance tests, causal sets
- **Sagan** (5 papers) — falsifiability audit, epistemic discipline
- **Little-Red-Dots** (10 papers) — JWST early SMBH assembly
- Plus: Nazarewicz, Quantum Foam, Paasch, Kitaev, Richardson-Gaudin, Cosmic-Web, NCG-Chemical-Potential

## Key Findings

> See `literature-novelty-audit.md` (CRITICAL — publication strategy). Audited 5 mathematical physics results: Berry curvature (PARTIAL novelty), spectral flow (ROUTINE), Petrov Type D on SU(3) (MEDIUM novelty, publishable in GRG), Landau-Zener (WEAK), grading trace (ROUTINE). **Strategic**: Publish Result 3 (Petrov); use others as supporting lemmas.

> See `research-novelty-findings.md` (REFERENCE — Dirac block-diagonal, NCG monotonicity detail)

## Debugging Notes

- **WebFetch 403/redirect**: Skip Springer, OUP, ResearchGate. Use arXiv DOI links instead.
- **PDF extraction failure**: Fall back to WebFetch the arXiv abstract page + Google Books description.
- **Author names**: Use `au:Lastname_Firstname` syntax in arXiv API; spaces break the query.
- **Large files**: Split reads using `limit` parameter in Read tool to stay under 30KB byte ceiling.
- **Unicode trap**: ASCII-safe only. Replace em-dash (—) with `--`, arrows (→) with `->`, checkmarks ([✓]) with `[OK]`.

---

**Last update**: 2026-04-28. Memory collapse: 2,612 → ~120 lines. Deleted 13 stale project-completion records; consolidated into MEMORY.md table. Promoted publication-strategy audit to REFERENCE index.
