#!/usr/bin/env python3
"""
SQLite Knowledge Database for the Phonon-Exflation Project.

Syncs tools/knowledge-index.json into a SQLite database with FTS5 full-text
search across all entity types.

Usage:
    python knowledge_db.py --sync                    # Full rebuild from JSON
    python knowledge_db.py --search "BCS gap"        # FTS5 ranked search
    python knowledge_db.py --search "Kosmann" --limit 5
    python knowledge_db.py --query gates V-1         # Direct entity lookup
"""

import json
import sqlite3
import sys
import argparse
import textwrap
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"
CANONICAL_CONSTANTS_DIR = PROJECT_ROOT / "computations" / "_shared"


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA_SQL = """
-- Core entity tables (8 tables matching the 8 JSON arrays)

CREATE TABLE IF NOT EXISTS theorems (
    id TEXT PRIMARY KEY,
    name TEXT,
    status TEXT,
    sessions TEXT,
    precision TEXT,
    statement TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS closed_mechanisms (
    id TEXT PRIMARY KEY,
    name TEXT,
    closed_by TEXT,
    session TEXT,
    gate_id TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS gates (
    id TEXT PRIMARY KEY,
    name TEXT,
    session TEXT,
    condition TEXT,
    result TEXT,
    verdict TEXT,
    bayes_factor REAL,
    data_files TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS probability_trajectory (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    session TEXT,
    date TEXT,
    panel TEXT,
    sagan TEXT,
    key_event TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    date TEXT,
    type TEXT,
    agents TEXT,
    prior TEXT,
    posterior TEXT,
    verdict TEXT,
    files TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS data_provenance (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    script TEXT,
    session TEXT,
    name TEXT,
    inputs TEXT,
    outputs TEXT,
    gates_informed TEXT
);

CREATE TABLE IF NOT EXISTS open_channels (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    detail_1 TEXT,
    detail_2 TEXT,
    session TEXT,
    source_file TEXT
);

-- Session markdown files (S90+) — distinct entity from data_provenance.
-- The data_provenance table models compute-script provenance (.py files with
-- inputs/outputs/gates_informed); the harvested attribution corpus has
-- 2,496 unique edge IDs in "<session>:<filename.md>" form that reference
-- session markdown FILES, not scripts. The gap survey showed 17,526 edge
-- endpoints typed 'data_provenance' but 0% align with the DB rows because
-- of this type-meaning conflation. This table catalogs every markdown
-- file under sessions/, keyed by the encoded form so existing edges find
-- anchors after the extract_entities retyping pass.
CREATE TABLE IF NOT EXISTS session_files (
    id TEXT PRIMARY KEY,
    session TEXT,
    filename TEXT,
    path TEXT,
    size_bytes INTEGER
);
CREATE INDEX IF NOT EXISTS idx_session_files_session ON session_files(session);

CREATE TABLE IF NOT EXISTS researchers (
    domain TEXT PRIMARY KEY,
    paper_count INTEGER,
    description TEXT,
    index_file TEXT,
    path TEXT,
    citation_count INTEGER,
    cited_in_sessions TEXT
);

-- Agent personas (S90+) — distinct entity from researchers. An agent is a
-- specific persona/methodology configuration (.claude/agents/*.md slugs
-- like 'dirac-antimatter-theorist'); a researcher is an underlying paper
-- corpus directory (researchers/Antimatter/). Many edges in the harvested
-- attribution corpus reference agent slugs but were mis-typed as
-- source_type='researchers'; the post-process step in extract_entities
-- rewrites those to source_type='agents'. researcher_domain is the
-- foreign-key-style alias to researchers.domain (nullable for generic
-- agents like 'coordinator', 'gen-physicist', 'web-researcher').
CREATE TABLE IF NOT EXISTS agents (
    slug TEXT PRIMARY KEY,
    name TEXT,
    persona TEXT,
    description TEXT,
    researcher_domain TEXT,
    model TEXT,
    color TEXT,
    template TEXT,
    source_file TEXT
);

CREATE TABLE IF NOT EXISTS equations (
    id TEXT PRIMARY KEY,
    type TEXT,
    raw TEXT,
    file TEXT,
    line INTEGER,
    context TEXT,
    source_file TEXT
);

-- Framework registries (S90+) — one meta-entry per framework/*.md file.
-- These are the "registry" file metaentries that extract_entities.py
-- emits but knowledge_db never materialized. Required for the
-- registry->session_file edge synthesis to anchor framework docs.
CREATE TABLE IF NOT EXISTS registries (
    id TEXT PRIMARY KEY,
    registry_id TEXT,
    title TEXT,
    source_file TEXT,
    target_buckets TEXT,
    origin TEXT,
    summary_row_count INTEGER
);
CREATE INDEX IF NOT EXISTS idx_registries_source ON registries(source_file);

-- Canonical constants (S90+) — materialized from
-- computations/_shared/canonical_constants.py. Primary key is the constant
-- name; this matches the IDs that edges reference (the chain-of-custody
-- visualizer was previously synthesizing 297 constants anchors from edge
-- endpoints alone because no SQL table existed for the edges to terminate
-- in). value is stringified for storage flexibility; PROVENANCE dict's
-- session/source/gate/superseded fields are exploded as columns.
CREATE TABLE IF NOT EXISTS constants (
    name TEXT PRIMARY KEY,
    value TEXT,
    session TEXT,
    source TEXT,
    gate TEXT,
    superseded TEXT,
    has_provenance INTEGER
);

-- Relation edges (tagged-link syntax; see extract_entities.py extract_edges)
CREATE TABLE IF NOT EXISTS edges (
    id TEXT PRIMARY KEY,
    type TEXT,
    source_type TEXT,
    source_id TEXT,
    target_type TEXT,
    target_id TEXT,
    comment TEXT,
    source_file TEXT,
    line INTEGER
);
CREATE INDEX IF NOT EXISTS idx_edges_src ON edges(source_type, source_id);
CREATE INDEX IF NOT EXISTS idx_edges_tgt ON edges(target_type, target_id);
CREATE INDEX IF NOT EXISTS idx_edges_type ON edges(type);

-- Canonical classes (S86+) — sister to canonical_constants.
-- Source of truth: computations/_shared/canonical_classes.py.
-- See extract_entities.extract_classes() for the ingestion path.
CREATE TABLE IF NOT EXISTS classes (
    id TEXT PRIMARY KEY,
    name TEXT,
    tier INTEGER,
    parent_id TEXT,
    description TEXT,
    seed_session TEXT
);
CREATE INDEX IF NOT EXISTS idx_classes_parent ON classes(parent_id);
CREATE INDEX IF NOT EXISTS idx_classes_tier ON classes(tier);

-- Class edges (membership + parent_of). Edge-shape-compatible with the
-- visualizer's REAL_EDGES schema: short column names (src_type/src/tgt_type/
-- tgt) match the JSON form. Distinct table from `edges` because the two
-- collections serve different purposes — `edges` is the tagged-link harvest
-- across documents; `class_edges` is the curated grouping registry.
CREATE TABLE IF NOT EXISTS class_edges (
    rowid INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    src_type TEXT,
    src TEXT,
    tgt_type TEXT,
    tgt TEXT,
    role TEXT,
    comment TEXT
);
CREATE INDEX IF NOT EXISTS idx_class_edges_src ON class_edges(src_type, src);
CREATE INDEX IF NOT EXISTS idx_class_edges_tgt ON class_edges(tgt_type, tgt);
CREATE INDEX IF NOT EXISTS idx_class_edges_type ON class_edges(type);

-- FTS5 spanning all entity names/content
CREATE VIRTUAL TABLE IF NOT EXISTS knowledge_fts USING fts5(
    entity_type,
    entity_id,
    name,
    content,
    source_file
);
"""


# ---------------------------------------------------------------------------
# Sync logic
# ---------------------------------------------------------------------------

def load_index() -> dict:
    """Load the knowledge index JSON."""
    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Index not found at {INDEX_PATH}. Run: /weave --update"
        )
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def list_to_text(lst) -> str:
    """Convert a list to a comma-separated string for storage."""
    if isinstance(lst, list):
        return ", ".join(str(x) for x in lst)
    return str(lst) if lst else ""


def safe_str(val) -> str:
    """Convert any value to a string safe for SQLite binding."""
    if val is None:
        return None
    if isinstance(val, (dict, list)):
        return json.dumps(val)
    return str(val)


def build_fts_content(entity: dict, skip_keys=("id", "source_file")) -> str:
    """Concatenate all text fields of an entity for FTS indexing."""
    parts = []
    for key, val in entity.items():
        if key in skip_keys or val is None:
            continue
        if isinstance(val, list):
            parts.append(", ".join(str(x) for x in val))
        elif isinstance(val, str) and val.strip():
            parts.append(val.strip())
    return " | ".join(parts)


def sync_db(idx: dict):
    """Rebuild the SQLite database from the JSON index."""
    # Remove existing DB for clean rebuild
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Create schema
    cur.executescript(SCHEMA_SQL)

    counts = {}

    # --- Theorems ---
    for t in idx.get("theorems", []):
        cur.execute(
            "INSERT OR REPLACE INTO theorems VALUES (?,?,?,?,?,?,?)",
            (t["id"], t.get("name"), t.get("status"), t.get("sessions"),
             t.get("precision"), t.get("statement"), t.get("source_file")),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("theorem", t["id"], t.get("name", ""),
             build_fts_content(t), t.get("source_file", "")),
        )
    counts["theorems"] = len(idx.get("theorems", []))

    # --- Closed Mechanism ---
    for dm in idx.get("closed_mechanisms", []):
        cur.execute(
            "INSERT OR REPLACE INTO closed_mechanisms VALUES (?,?,?,?,?,?)",
            (dm["id"], dm.get("name"), dm.get("closed_by"), dm.get("session"),
             dm.get("gate_id"), dm.get("source_file")),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("closed_mechanism", dm["id"], dm.get("name", ""),
             build_fts_content(dm), dm.get("source_file", "")),
        )
    counts["closed_mechanisms"] = len(idx.get("closed_mechanisms", []))

    # --- Gates ---
    for g in idx.get("gates", []):
        cur.execute(
            "INSERT OR REPLACE INTO gates VALUES (?,?,?,?,?,?,?,?,?)",
            (g["id"], g.get("name"), g.get("session"), g.get("condition"),
             g.get("result"), g.get("verdict"), g.get("bayes_factor"),
             list_to_text(g.get("data_files", [])), g.get("source_file")),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("gate", g["id"], g.get("name", ""),
             build_fts_content(g), g.get("source_file", "")),
        )
    counts["gates"] = len(idx.get("gates", []))

    # --- Probability Trajectory ---
    for pt in idx.get("probability_trajectory", []):
        cur.execute(
            "INSERT INTO probability_trajectory (session, date, panel, sagan, key_event, source_file) "
            "VALUES (?,?,?,?,?,?)",
            (pt.get("session"), pt.get("date"), pt.get("panel"), pt.get("sagan"),
             pt.get("key_event"), pt.get("source_file")),
        )
        # FTS entry only for entries with meaningful key_event
        if pt.get("key_event", "").strip():
            cur.execute(
                "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
                ("trajectory", pt.get("session", ""),
                 pt.get("key_event", ""), build_fts_content(pt),
                 pt.get("source_file", "")),
            )
    counts["probability_trajectory"] = len(idx.get("probability_trajectory", []))

    # --- Sessions ---
    for s in idx.get("sessions", []):
        cur.execute(
            "INSERT OR REPLACE INTO sessions VALUES (?,?,?,?,?,?,?,?,?)",
            (s["id"], s.get("date"), safe_str(s.get("type")), safe_str(s.get("agents")),
             safe_str(s.get("prior")), safe_str(s.get("posterior")), safe_str(s.get("verdict")),
             list_to_text(s.get("files", [])), s.get("source_file")),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("session", s["id"], f"Session {s['id']}",
             build_fts_content(s), s.get("source_file", "")),
        )
    counts["sessions"] = len(idx.get("sessions", []))

    # --- Data Provenance ---
    for p in idx.get("data_provenance", []):
        cur.execute(
            "INSERT INTO data_provenance (script, session, name, inputs, outputs, gates_informed) "
            "VALUES (?,?,?,?,?,?)",
            (p.get("script"), p.get("session"), p.get("name"),
             list_to_text(p.get("inputs", [])),
             list_to_text(p.get("outputs", [])),
             list_to_text(p.get("gates_informed", []))),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("provenance", p.get("script", p.get("name", "")),
             p.get("name", ""), build_fts_content(p), ""),
        )
    counts["data_provenance"] = len(idx.get("data_provenance", []))

    # --- Open Channels ---
    for oc in idx.get("open_channels", []):
        cur.execute(
            "INSERT INTO open_channels (name, detail_1, detail_2, session, source_file) "
            "VALUES (?,?,?,?,?)",
            (oc.get("name"), oc.get("detail_1"), oc.get("detail_2"),
             oc.get("session"), oc.get("source_file")),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("open_channel", "", oc.get("name", ""),
             build_fts_content(oc), oc.get("source_file", "")),
        )
    counts["open_channels"] = len(idx.get("open_channels", []))

    # --- Session Files (S90+) ---
    for sf in idx.get("session_files", []):
        cur.execute(
            "INSERT OR REPLACE INTO session_files VALUES (?,?,?,?,?)",
            (sf.get("id"), sf.get("session"), sf.get("filename"),
             sf.get("path"), sf.get("size_bytes", 0)),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("session_file", sf.get("id", ""), sf.get("filename", ""),
             f"{sf.get('session','')} | {sf.get('path','')}",
             sf.get("path", "")),
        )
    counts["session_files"] = len(idx.get("session_files", []))

    # --- Researchers ---
    for r in idx.get("researchers", []):
        cur.execute(
            "INSERT OR REPLACE INTO researchers VALUES (?,?,?,?,?,?,?)",
            (r.get("domain"), r.get("paper_count"), r.get("description"),
             r.get("index_file"), r.get("path"), r.get("citation_count"),
             list_to_text(r.get("cited_in_sessions", []))),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("researcher", r.get("domain", ""), r.get("domain", ""),
             build_fts_content(r), r.get("index_file", "")),
        )
    counts["researchers"] = len(idx.get("researchers", []))

    # --- Agents (S90+) ---
    # Read from idx['agents']; populated by extract_entities.extract_agents()
    # scanning .claude/agents/*.md. Agent slugs (dirac-antimatter-theorist
    # etc.) are the IDs that many attribution edges reference; this table
    # gives those edges a concrete anchor.
    for a in idx.get("agents", []):
        cur.execute(
            "INSERT OR REPLACE INTO agents VALUES (?,?,?,?,?,?,?,?,?)",
            (a.get("slug"), a.get("name"), a.get("persona"),
             a.get("description"), a.get("researcher_domain"),
             a.get("model"), a.get("color"), a.get("template"),
             a.get("source_file")),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("agent", a.get("slug", ""), a.get("name", ""),
             build_fts_content(a), a.get("source_file", "")),
        )
    counts["agents"] = len(idx.get("agents", []))

    # --- Framework Registries (S90+) ---
    for r in idx.get("registries", []):
        cur.execute(
            "INSERT OR REPLACE INTO registries VALUES (?,?,?,?,?,?,?)",
            (r.get("id"), r.get("registry_id"), r.get("title"),
             r.get("source_file"),
             ",".join(r.get("target_buckets") or []),
             r.get("origin", "framework-registry"),
             r.get("summary_row_count", 0)),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("registry", r.get("id", ""), r.get("title", ""),
             build_fts_content(r), r.get("source_file", "")),
        )
    counts["registries"] = len(idx.get("registries", []))

    # --- Equations ---
    for eq in idx.get("equations", []):
        cur.execute(
            "INSERT OR REPLACE INTO equations VALUES (?,?,?,?,?,?,?)",
            (eq.get("id", ""), eq.get("type", ""), eq.get("raw", ""),
             eq.get("file", ""), eq.get("line", 0),
             eq.get("context", ""), eq.get("source_file", "")),
        )
        # FTS entry: use raw equation as both name and content
        raw_short = (eq.get("raw", "") or "")[:200]
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("equation", eq.get("id", ""), raw_short,
             f"{eq.get('type', '')} | {eq.get('raw', '')} | {eq.get('context', '')}",
             eq.get("source_file", "")),
        )
    counts["equations"] = len(idx.get("equations", []))

    # --- Canonical Constants (S90+) ---
    # Materialized from computations/_shared/canonical_constants.py. The
    # edges table has 23,879 edge endpoints targeting `constants` — they
    # were previously dangling because no SQL table existed. This pass
    # creates one row per public identifier name in canonical_constants,
    # with PROVENANCE-dict columns when available. Names without a
    # PROVENANCE entry are inserted with has_provenance=0 so the visualizer
    # can still resolve the anchor (the goal is "anchors are accurate AND
    # cross-referenced" — a node without provenance is still a node).
    sys.path.insert(0, str(CANONICAL_CONSTANTS_DIR))
    try:
        import canonical_constants as CC  # noqa: WPS433
    except Exception as exc:  # noqa: BLE001
        print(f"  WARN: canonical_constants import failed: {exc}")
        CC = None
    constants_count = 0
    # Filter out infrastructure / non-substrate names that get caught by
    # the dir(CC) sweep but don't represent real canonical constants.
    _CONSTANTS_NOISE = {
        "sys", "AUDIT_EXEMPT_SCRIPTS", "AUDIT_PATTERNS",
        "AUDIT_PATTERNS_COMPILED", "CHANNEL_LABELS",
    }
    if CC is not None:
        prov_dict = getattr(CC, "PROVENANCE", {}) or {}
        public_names = [
            n for n in dir(CC)
            if not n.startswith("_") and n.isidentifier()
            and n != "PROVENANCE"
            and n not in _CONSTANTS_NOISE
        ]
        # Filter to only constants WITH a PROVENANCE entry — those are
        # the canonical, gate-derived values that have edges via the
        # canonical_constants_provenance_edges harvester. Constants
        # without PROVENANCE (derived/computed exports) lack edges and
        # would be permanent orphans in the visualizer.
        public_names = [n for n in public_names if n in prov_dict]
        for name in public_names:
            try:
                raw = getattr(CC, name)
            except Exception:  # noqa: BLE001
                continue
            # Skip module-typed exports (e.g. `import numpy as np` at top)
            if hasattr(raw, "__file__") or callable(raw):
                continue
            # Stringify value defensively
            try:
                value_str = repr(raw)
            except Exception:  # noqa: BLE001
                value_str = "<unstringifiable>"
            if len(value_str) > 1000:
                value_str = value_str[:997] + "..."
            prov = prov_dict.get(name) if isinstance(prov_dict, dict) else None
            if isinstance(prov, dict):
                sess = prov.get("session") or ""
                src = prov.get("source") or ""
                gate = prov.get("gate") or ""
                superseded = prov.get("superseded") or ""
                has_prov = 1
            else:
                sess = src = gate = superseded = ""
                has_prov = 0
            cur.execute(
                "INSERT OR REPLACE INTO constants VALUES (?,?,?,?,?,?,?)",
                (name, value_str, sess, src, gate, str(superseded), has_prov),
            )
            cur.execute(
                "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
                ("constant", name, name,
                 f"{name} = {value_str} | session={sess} | source={src} | gate={gate}",
                 "computations/_shared/canonical_constants.py"),
            )
            constants_count += 1
    counts["constants"] = constants_count

    # --- Edges (relation graph) ---
    for e in idx.get("edges", []):
        cur.execute(
            "INSERT OR REPLACE INTO edges VALUES (?,?,?,?,?,?,?,?,?)",
            (e.get("id", ""), e.get("type", ""),
             e.get("source_type", ""), e.get("source_id", ""),
             e.get("target_type", ""), e.get("target_id", ""),
             e.get("comment", ""), e.get("source_file", ""),
             e.get("line", 0)),
        )
        display = (
            f"{e.get('source_type', '')}:{e.get('source_id', '')} "
            f"--{e.get('type', '')}--> "
            f"{e.get('target_type', '')}:{e.get('target_id', '')}"
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("edge", e.get("id", ""), display,
             build_fts_content(e), e.get("source_file", "")),
        )
    counts["edges"] = len(idx.get("edges", []))

    # --- Canonical Classes (S86+) ---
    # Source: computations/_shared/canonical_classes.py via extract_classes().
    # Classes are FTS-indexed (rich descriptions); class_edges are NOT FTS-
    # indexed (per-edge content too thin — comments are 1 line each).
    for c in idx.get("classes", []):
        cur.execute(
            "INSERT OR REPLACE INTO classes VALUES (?,?,?,?,?,?)",
            (c.get("id", ""), c.get("name", ""), c.get("tier", 0),
             c.get("parent_id"), c.get("description", ""),
             c.get("seed_session", "")),
        )
        # FTS includes name + description so search_knowledge("CC family")
        # surfaces the class entry. Source_file is the canonical_classes.py
        # module since classes have no per-class source location.
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("class", c.get("id", ""), c.get("name", ""),
             build_fts_content(c, skip_keys=("id",)),
             "computations/_shared/canonical_classes.py"),
        )
    counts["classes"] = len(idx.get("classes", []))

    # --- Class Edges (membership + parent_of) ---
    for e in idx.get("class_edges", []):
        cur.execute(
            "INSERT INTO class_edges (type, src_type, src, tgt_type, tgt, role, comment) "
            "VALUES (?,?,?,?,?,?,?)",
            (e.get("type", ""), e.get("srcType", ""), e.get("src", ""),
             e.get("tgtType", ""), e.get("tgt", ""),
             e.get("role"), e.get("comment", "")),
        )
    counts["class_edges"] = len(idx.get("class_edges", []))

    conn.commit()

    # FTS row count
    cur.execute("SELECT COUNT(*) FROM knowledge_fts")
    fts_count = cur.fetchone()[0]

    conn.close()

    # Report
    total = sum(counts.values())
    db_size = DB_PATH.stat().st_size / 1024
    print(f"Synced {total} entities to {DB_PATH.name} ({db_size:.0f} KB)")
    print()
    for table, count in counts.items():
        print(f"  {table:25s} {count:4d} rows")
    print(f"  {'knowledge_fts':25s} {fts_count:4d} rows")
    print()
    print(f"Database: {DB_PATH}")


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

def search_fts(query: str, limit: int = 20):
    """Run a FTS5 ranked search across all entities."""
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}. Run: python knowledge_db.py --sync")
        return

    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Sanitize the user query for FTS5 MATCH. A bare hyphenated or colon-bearing
    # token (e.g. a gate-ID "S92-HK-VII-AU-CLASS-FULL-LEVEL-3-LANDING") is otherwise
    # parsed as FTS5 query syntax and crashes the parser ("no such column: ...").
    # Wrapping each whitespace-separated token in double quotes makes FTS5 treat it
    # as a literal string (tokenized internally) while preserving implicit-AND
    # semantics across multiple search words.
    fts_query = " ".join('"' + tok.replace('"', '""') + '"' for tok in query.split())
    if not fts_query:
        print(f"No results for '{query}'")
        conn.close()
        return

    # BM25 ranking (lower = better match)
    cur.execute(
        """
        SELECT entity_type, entity_id, name, content, source_file,
               bm25(knowledge_fts) AS rank
        FROM knowledge_fts
        WHERE knowledge_fts MATCH ?
        ORDER BY rank
        LIMIT ?
        """,
        (fts_query, limit),
    )
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print(f"No results for '{query}'")
        return

    # Group by entity_type
    grouped = {}
    for row in rows:
        etype = row[0]
        if etype not in grouped:
            grouped[etype] = []
        grouped[etype].append(row)

    print(f"Search: '{query}' — {len(rows)} results\n")
    for etype, entries in grouped.items():
        print(f"  [{etype}] ({len(entries)} hits)")
        for _, eid, name, content, src, rank in entries:
            # Truncate content for display
            content_short = content[:200].replace("\n", " ")
            if len(content) > 200:
                content_short += "…"
            name_display = name or eid or "(unnamed)"
            print(f"    • {name_display}")
            print(f"      {content_short}")
            if src:
                print(f"      src: {Path(src).name}")
            print()


# ---------------------------------------------------------------------------
# Direct query
# ---------------------------------------------------------------------------

def query_entity(table: str, entity_id: str):
    """Look up a specific entity by table and ID."""
    if not DB_PATH.exists():
        print(f"Database not found. Run: python knowledge_db.py --sync")
        return

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Map short names to table names
    table_map = {
        "theorems": "theorems", "theorem": "theorems",
        "closed": "closed_mechanisms", "closed": "closed_mechanisms",
        "closed_mechanisms": "closed_mechanisms", "dead_mechanisms": "closed_mechanisms",
        "gates": "gates", "gate": "gates",
        "sessions": "sessions", "session": "sessions",
        "provenance": "data_provenance", "data_provenance": "data_provenance",
        "open": "open_channels", "open_channels": "open_channels",
        "researchers": "researchers", "researcher": "researchers",
        "trajectory": "probability_trajectory",
        "equations": "equations", "equation": "equations", "eq": "equations",
        "edges": "edges", "edge": "edges",
        "classes": "classes", "class": "classes",
    }

    tbl = table_map.get(table.lower())
    if not tbl:
        print(f"Unknown table: {table}")
        print(f"Available: {', '.join(sorted(set(table_map.values())))}")
        return

    # Determine the primary key column
    pk_cols = {
        "theorems": "id", "closed_mechanisms": "id", "gates": "id",
        "sessions": "id", "researchers": "domain",
        "probability_trajectory": "session",
        "data_provenance": "name", "open_channels": "name",
        "equations": "id", "edges": "id",
        "classes": "id",
    }
    pk = pk_cols.get(tbl, "id")

    cur.execute(f"SELECT * FROM {tbl} WHERE {pk} = ?", (entity_id,))
    rows = cur.fetchall()

    if not rows:
        # Try LIKE search as fallback
        cur.execute(f"SELECT * FROM {tbl} WHERE {pk} LIKE ?", (f"%{entity_id}%",))
        rows = cur.fetchall()

    conn.close()

    if not rows:
        print(f"No entity found in {tbl} matching '{entity_id}'")
        return

    print(f"Query: {tbl} / {entity_id} — {len(rows)} result(s)\n")
    for row in rows:
        for key in row.keys():
            val = row[key]
            if val is not None and str(val).strip():
                print(f"  {key:20s}: {val}")
        print()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="SQLite knowledge database for Phonon-Exflation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Examples:
              python knowledge_db.py --sync
              python knowledge_db.py --search "BCS gap"
              python knowledge_db.py --search "Kosmann" --limit 5
              python knowledge_db.py --query gates V-1
        """),
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--sync", action="store_true",
                        help="Full rebuild from knowledge-index.json")
    group.add_argument("--search", type=str, metavar="QUERY",
                        help="FTS5 ranked search")
    group.add_argument("--query", nargs=2, metavar=("TABLE", "ID"),
                        help="Direct entity lookup")

    parser.add_argument("--limit", type=int, default=20,
                         help="Max search results (default: 20)")

    args = parser.parse_args()

    if args.sync:
        idx = load_index()
        sync_db(idx)
    elif args.search:
        search_fts(args.search, limit=args.limit)
    elif args.query:
        query_entity(args.query[0], args.query[1])


if __name__ == "__main__":
    main()
