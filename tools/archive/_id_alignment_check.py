"""Check ID alignment between researchers/data_provenance DB rows and the
IDs referenced by edges. The gap survey showed both tables at 0% coverage
despite high edge volume — so the IDs don't match. This script shows what
the actual DB IDs look like vs what the edges reference.
"""
import sqlite3
from collections import Counter
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

for table, edge_type in [("researchers", "researchers"), ("data_provenance", "data_provenance")]:
    print(f"=== {table} ===")
    # DB columns
    cur.execute(f"PRAGMA table_info({table})")
    cols = [r[1] for r in cur.fetchall()]
    print(f"  Columns: {cols}")
    # First 5 rows (all columns)
    cur.execute(f"SELECT * FROM {table} LIMIT 5")
    print("  Sample DB rows:")
    for r in cur.fetchall():
        print(f"    {r}")
    # First 5 edge references (as source_id) for this entity type
    cur.execute(
        "SELECT DISTINCT source_id FROM edges WHERE source_type = ? LIMIT 8",
        (edge_type,)
    )
    print(f"  Sample edge source_ids referencing {edge_type}:")
    for r in cur.fetchall():
        print(f"    {r[0]!r}")
    cur.execute(
        "SELECT DISTINCT target_id FROM edges WHERE target_type = ? LIMIT 8",
        (edge_type,)
    )
    print(f"  Sample edge target_ids referencing {edge_type}:")
    for r in cur.fetchall():
        print(f"    {r[0]!r}")
    print()
