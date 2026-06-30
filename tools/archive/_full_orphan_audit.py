"""Detailed audit of every remaining orphan across every table.

Per /goal-set requirement: ALL anchors must be cross-referenced.
This script enumerates exactly what's left.
"""
import sqlite3
from pathlib import Path
conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

def show(table, pk, extra_cols=None, limit=30):
    extras = (", " + ", ".join(extra_cols)) if extra_cols else ""
    cur.execute(f"""
        SELECT {pk}{extras} FROM {table}
        WHERE {pk} NOT IN (
            SELECT source_id FROM edges WHERE source_type='{table}'
            UNION SELECT target_id FROM edges WHERE target_type='{table}'
        )
        LIMIT {limit}
    """)
    rows = cur.fetchall()
    print(f"=== {table}: {len(rows)} orphans (showing first {limit}) ===")
    for r in rows:
        cells = " | ".join((c or "").replace("\\", "/") if isinstance(c, str) else str(c) for c in r)
        print(f"  {cells[:140]}")
    print()

show("constants", "name", ["has_provenance", "session"])
show("researchers", "domain", ["paper_count", "citation_count"])
show("theorems", "id", ["name", "source_file"])
show("open_channels", "name", ["session", "source_file"])
show("sessions", "id")
show("gates", "id", ["source_file"])
show("session_files", "id", ["path"])

# Equations: 1899 left, sample by source-file
print("=== equations: orphan source_files (top 10) ===")
from collections import Counter
cur.execute("""
    SELECT source_file FROM equations
    WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='equations'
        UNION SELECT target_id FROM edges WHERE target_type='equations'
    )
""")
dirs = Counter()
for r in cur.fetchall():
    src = (r[0] or "").replace("\\", "/")
    parts = src.split("/")
    if len(parts) >= 2:
        dirs["/".join(parts[:3]) if len(parts) >= 3 else "/".join(parts)] += 1
for k, v in dirs.most_common(10):
    print(f"  {v:5d}  {k}")
