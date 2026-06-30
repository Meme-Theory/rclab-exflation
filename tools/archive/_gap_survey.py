"""Gap survey: for EVERY entity table, count how many rows are graph-orphans.

Output: per-table (db_rows, edge_referenced_rows, orphan_rows, coverage_pct).
Definition of edge-referenced: appears as source_id OR target_id in edges
table with matching entity-type qualifier.

This is the gap-finding the genesis prompt asked for. Print it raw and
let the user see the shape of the problem across the whole graph.
"""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

ENTITY_TABLES = [
    ("closed_mechanisms", "closed_mechanisms"),
    ("theorems", "theorems"),
    ("gates", "gates"),
    ("sessions", "sessions"),
    ("researchers", "researchers"),
    ("agents", "agents"),
    ("open_channels", "open_channels"),
    ("data_provenance", "data_provenance"),
    ("session_files", "session_files"),
    ("equations", "equations"),
    ("constants", "constants"),
    ("registries", "registries"),
]

print("=" * 90)
print(f"{'Table':<20s} {'DB rows':>10s} {'Has-edge':>10s} {'Orphans':>10s} {'Coverage':>10s}")
print("-" * 90)

results = []
for table, edge_type in ENTITY_TABLES:
    # Discover primary-key column (id, or domain for researchers, etc.)
    cur.execute(f"PRAGMA table_info({table})")
    cols = [r[1] for r in cur.fetchall()]
    if not cols:
        continue
    # Pick the primary lookup column. Some tables (data_provenance) don't
    # have a single 'id' — try multiple candidate columns and union all
    # their values into the matchable id set, since edges may reference
    # any of them.
    candidate_cols = []
    for c in ("id", "slug", "domain", "script", "name"):
        if c in cols:
            candidate_cols.append(c)
    if not candidate_cols:
        candidate_cols = [cols[0]]
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    db_rows = cur.fetchone()[0]
    if db_rows == 0:
        continue
    db_ids: set = set()
    # Build the matchable id set as the union across candidate columns
    # OF THE FIRST candidate column (the "primary"). For coverage, we
    # only count a row as has-edge if its primary-key value appears.
    # Use the FIRST candidate (most-specific) as the primary key.
    pk = candidate_cols[0]
    cur.execute(f"SELECT {pk} FROM {table}")
    db_ids = {r[0] for r in cur.fetchall()}
    # Collect IDs referenced in edges
    cur.execute(
        "SELECT DISTINCT source_id FROM edges WHERE source_type = ? "
        "UNION SELECT DISTINCT target_id FROM edges WHERE target_type = ?",
        (edge_type, edge_type)
    )
    edge_ids = {r[0] for r in cur.fetchall()}
    intersection = db_ids & edge_ids
    has_edge = len(intersection)
    orphans = db_rows - has_edge
    coverage = (has_edge / db_rows * 100) if db_rows else 0
    print(f"{table:<20s} {db_rows:>10d} {has_edge:>10d} {orphans:>10d} {coverage:>9.1f}%")
    results.append((table, db_rows, has_edge, orphans, coverage))

print("=" * 90)
print()

# Also count edges by source_type and target_type — see where the edges DO terminate
print("=== Edge endpoints by entity-type (where edges DO touch) ===")
cur.execute(
    "SELECT source_type, COUNT(*) FROM edges GROUP BY source_type "
    "ORDER BY COUNT(*) DESC"
)
print(f"  {'source_type':<20s} {'count':>8s}")
for src_type, cnt in cur.fetchall():
    print(f"  {src_type:<20s} {cnt:>8d}")

print()
cur.execute(
    "SELECT target_type, COUNT(*) FROM edges GROUP BY target_type "
    "ORDER BY COUNT(*) DESC"
)
print(f"  {'target_type':<20s} {'count':>8s}")
for tgt_type, cnt in cur.fetchall():
    print(f"  {tgt_type:<20s} {cnt:>8d}")
