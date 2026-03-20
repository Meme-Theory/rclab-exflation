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
import argparse
import textwrap
from pathlib import Path


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = PROJECT_ROOT / "tools" / "knowledge-index.json"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"


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

CREATE TABLE IF NOT EXISTS researchers (
    domain TEXT PRIMARY KEY,
    paper_count INTEGER,
    description TEXT,
    index_file TEXT,
    path TEXT,
    citation_count INTEGER,
    cited_in_sessions TEXT
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
            (t["id"], t["name"], t["status"], t["sessions"],
             t["precision"], t["statement"], t["source_file"]),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("theorem", t["id"], t["name"],
             build_fts_content(t), t.get("source_file", "")),
        )
    counts["theorems"] = len(idx.get("theorems", []))

    # --- Closed Mechanism ---
    for dm in idx.get("closed_mechanisms", []):
        cur.execute(
            "INSERT OR REPLACE INTO closed_mechanisms VALUES (?,?,?,?,?,?)",
            (dm["id"], dm["name"], dm["closed_by"], dm["session"],
             dm["gate_id"], dm["source_file"]),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("closed_mechanism", dm["id"], dm["name"],
             build_fts_content(dm), dm.get("source_file", "")),
        )
    counts["closed_mechanisms"] = len(idx.get("closed_mechanisms", []))

    # --- Gates ---
    for g in idx.get("gates", []):
        cur.execute(
            "INSERT OR REPLACE INTO gates VALUES (?,?,?,?,?,?,?,?,?)",
            (g["id"], g["name"], g["session"], g["condition"],
             g["result"], g["verdict"], g["bayes_factor"],
             list_to_text(g.get("data_files", [])), g["source_file"]),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("gate", g["id"], g["name"],
             build_fts_content(g), g.get("source_file", "")),
        )
    counts["gates"] = len(idx.get("gates", []))

    # --- Probability Trajectory ---
    for pt in idx.get("probability_trajectory", []):
        cur.execute(
            "INSERT INTO probability_trajectory (session, date, panel, sagan, key_event, source_file) "
            "VALUES (?,?,?,?,?,?)",
            (pt["session"], pt["date"], pt["panel"], pt["sagan"],
             pt["key_event"], pt["source_file"]),
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
            (s["id"], s["date"], safe_str(s["type"]), safe_str(s["agents"]),
             safe_str(s["prior"]), safe_str(s["posterior"]), safe_str(s["verdict"]),
             list_to_text(s.get("files", [])), s["source_file"]),
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
            (p["script"], p["session"], p["name"],
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
            (oc["name"], oc["detail_1"], oc["detail_2"],
             oc["session"], oc["source_file"]),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("open_channel", "", oc["name"],
             build_fts_content(oc), oc.get("source_file", "")),
        )
    counts["open_channels"] = len(idx.get("open_channels", []))

    # --- Researchers ---
    for r in idx.get("researchers", []):
        cur.execute(
            "INSERT OR REPLACE INTO researchers VALUES (?,?,?,?,?,?,?)",
            (r["domain"], r["paper_count"], r["description"],
             r["index_file"], r["path"], r["citation_count"],
             list_to_text(r.get("cited_in_sessions", []))),
        )
        cur.execute(
            "INSERT INTO knowledge_fts VALUES (?,?,?,?,?)",
            ("researcher", r["domain"], r["domain"],
             build_fts_content(r), r.get("index_file", "")),
        )
    counts["researchers"] = len(idx.get("researchers", []))

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
        (query, limit),
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
        "equations": "id",
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
