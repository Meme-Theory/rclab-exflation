---
paths:
  - "tools/mcp-servers/**"
  - "researchers/**"
  - "downloads/**"
---

# MCP Servers (Observational Data Access + Knowledge Base)

Four MCP servers provide live access to astronomical data, the project knowledge base, and canonical constants. Configured in `.mcp.json` (project root, gitignored). Servers start automatically when Claude Code loads.

## Available Servers

| Server | Entry Point | Data Sources | Framework Relevance |
|:-------|:-----------|:-------------|:-------------------|
| **knowledge** | `tools/mcp-servers/knowledge-mcp/server.py` | Knowledge index (SQLite FTS5), canonical constants | **ALL agents MUST query before computing** |
| **astro** | `tools/mcp-servers/astro-mcp/server.py` | DESI spectra + 31 astroquery services (SIMBAD, VizieR, SDSS, Gaia, MAST, IRSA, NED, etc.) | **DESI BAO = direct w(z) test** (highest priority) |

## Knowledge MCP Server

The knowledge server wraps the project's knowledge-index.json (SQLite FTS5 accelerated) and canonical_constants.py. **Every computation agent should query this server before starting work** to check whether a result is already known, a mechanism is closed, or a constant already exists.

### Tools

| Tool | Description | Example |
|:-----|:-----------|:--------|
| `search_knowledge` | FTS5 search across all entities | `search_knowledge("monotonic spectral action")` |
| `query_entity` | Direct lookup by table and ID | `query_entity("gates", "TAU-STAB-NN")` |
| `list_entities` | List all entities of a type | `list_entities("closed")` |
| `trace_entity` | Evidence chain for a concept | `trace_entity("tau stabilization")` |
| `get_constant` | Get constant value + provenance | `get_constant("tau_fold")` |
| `list_constants` | List/filter constants | `list_constants(pattern="BCS")` |
| `update_constant` | Add new constant with provenance | See below |
| `emit_verdict` | Append a gate verdict line — race-safe, syntax-forced (single lock-serialized writer) | See `gate-verdicts.md` §"Race-Safe Emission" |

### update_constant

Adds a NEW constant to canonical_constants.py with full provenance. Safety: refuses to overwrite existing constants.

```
update_constant(
  name="tau_equil_bcs",
  value="0.195",
  session="S{N}",
  source="s{N}_equil_tau_bcs.npz",
  gate="S{N}-A1-EQUIL-TAU",
  comment="BCS-dressed equilibrium tau",
  section_label="SECTION B"
)
```

## Paper-Search MCP

Tools for searching and downloading academic papers.

### search_arxiv — arXiv API (structured queries)

Passes queries directly to the arXiv API. **Sorts by relevance** (not date).

**CRITICAL**: The `ti:`, `au:`, `abs:` prefixes bind to ONE token only. Multi-word after a prefix silently drops to all-fields search. Every keyword needs its own prefix, joined by AND.

- Author search: `au:LastName_FirstName` (e.g., `au:Mack_Katherine`, `au:Volovik_G`)
- Title search: **one `ti:` per word**, joined with AND (e.g., `ti:dark AND ti:matter AND ti:annihilation`)
- Abstract search: `abs:keyword` (one per word, join with AND)
- All fields: `all:keyword`
- Category: `cat:astro-ph.CO`, `cat:hep-th`, etc.
- Combine fields: `au:Mack_Katherine AND ti:dark AND ti:matter`
- **WRONG**: `ti:dark matter annihilation` (only `dark` hits title; rest is orphaned)
- **RIGHT**: `au:Baptista AND ti:higher AND ti:dimensional AND ti:Standard AND ti:Model`

### search_google_scholar — Semantic Scholar API (natural language)

**Backend: Semantic Scholar** (replaces broken Google Scholar HTML scraper). Accepts natural language queries. Returns papers ranked by relevance with citation counts, arXiv IDs, DOIs.

- Free tier: 5,000 req / 5 min (IP-level rate limit)
- Set `SEMANTIC_SCHOLAR_API_KEY` env var for higher limits
- Has exponential-backoff retry on 429
- Returns arXiv IDs when available (use with `download_arxiv`)
- Example: `search_google_scholar("inflation cosmological constant vacuum energy", 10)`

### Other search tools
- `search_pubmed(query, max_results)` -- biomedical literature (REST API)
- `search_biorxiv(query, max_results)` -- biology preprints (REST API)

**Download/Read tools**:
- `download_arxiv(paper_id, save_path)` -- download PDF (e.g., `paper_id="1309.7783"`, `save_path="./downloads"`)
- `read_arxiv_paper(paper_id, save_path)` -- extract text from PDF (downloads first if needed)

**Workflow for researcher corpus building**:
1. `search_arxiv` with `au:` syntax to find paper IDs
2. `download_arxiv` each paper to `./downloads/`
3. `read_arxiv_paper` or Read tool on the PDFs to extract content
4. Spawn synthesis agents to write markdown reference docs from the downloaded content

## GWOSC Tools
- `list_catalogs` -- all GW event catalogs (GWTC-1 through GWTC-4)
- `list_events(catalog)` -- events with masses, distances, SNR
- `get_event(event_name)` -- full parameters for one event (e.g. GW150914)
- `search_events(min_mass, max_snr, ...)` -- filter by physical parameters
- `get_strain_urls(event_name, detector)` -- download URLs for strain data
- `get_run_info(dataset)` -- observing run metadata
- `get_timeline(dataset, gps_start, duration)` -- data quality segments

## Setup Notes
- **Astro MCP**: Cloned from `SandyYuan/astro_mcp`. 31 astroquery services auto-discovered on startup.
- All servers use system Python 3.13 (NOT the venv — MCP servers don't need GPU/torch).
- To check status: `/mcp` in Claude Code.
- Cloned repos (`nasa-mcp/`, `astro-mcp/`) are gitignored. Re-clone if missing:
  ```bash
  cd tools/mcp-servers
  git clone https://github.com/jezweb/nasa-mcp-server.git nasa-mcp
  git clone https://github.com/SandyYuan/astro_mcp.git astro-mcp
  pip install fastmcp httpx python-dotenv gwosc requests sparclclient astropy astroquery pandas
  ```
