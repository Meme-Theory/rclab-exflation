"""Throwaway: why does chain_of_custody.json show only 6 closed_mechanism
anchors when the DB has 266 rows? Hypothesis: ID mismatch between edges
and entity table after canonical-source renumbering."""
import sqlite3
from collections import Counter
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

# 1. What closed_mechanism IDs exist in the entity table?
cur.execute("SELECT id FROM closed_mechanisms")
db_ids = {r[0] for r in cur.fetchall()}
print(f"closed_mechanism IDs in DB: {len(db_ids)}")
prefixes = Counter()
for cid in db_ids:
    if cid.startswith("closed_atlas02_"):
        prefixes["closed_atlas02_*"] += 1
    elif cid.startswith("closed_regv_"):
        prefixes["closed_regv_*"] += 1
    elif cid.startswith("closed_gwch_"):
        prefixes["closed_gwch_*"] += 1
    else:
        prefixes["closed_N (legacy)"] += 1
for k, v in prefixes.most_common():
    print(f"  {v:4d}  {k}")
print()

# 2. What closed_* IDs are referenced as edge source or target?
cur.execute("SELECT source_id FROM edges WHERE source_type = 'closed_mechanisms'")
src_refs = Counter(r[0] for r in cur.fetchall())
cur.execute("SELECT target_id FROM edges WHERE target_type = 'closed_mechanisms'")
dst_refs = Counter(r[0] for r in cur.fetchall())
all_edge_ids = set(src_refs.keys()) | set(dst_refs.keys())
print(f"closed_* IDs referenced in edges: {len(all_edge_ids)} unique")
print(f"  edges with closed_* as src: {sum(src_refs.values())}")
print(f"  edges with closed_* as dst: {sum(dst_refs.values())}")
print()

# 3. How many overlap (edge-referenced AND in DB)?
in_db_and_edges = db_ids & all_edge_ids
only_in_db = db_ids - all_edge_ids
only_in_edges = all_edge_ids - db_ids
print(f"INTERSECTION (in DB AND referenced by edges): {len(in_db_and_edges)}")
print(f"  ONLY in DB (orphans — no edges):  {len(only_in_db)}")
print(f"  ONLY in edges (dangling refs):    {len(only_in_edges)}")
print()

# 4. Show samples of dangling edge refs (these are the bug)
if only_in_edges:
    print(f"=== Sample of {min(20, len(only_in_edges))} dangling edge refs ===")
    for cid in sorted(only_in_edges)[:20]:
        cnt = src_refs.get(cid, 0) + dst_refs.get(cid, 0)
        print(f"  {cid:30s}  (referenced in {cnt} edges)")

# 5. Show samples of orphaned DB entries
if only_in_db:
    print()
    print(f"=== Sample of {min(10, len(only_in_db))} orphan DB rows (no edges) ===")
    sample = list(only_in_db)[:10]
    placeholders = ",".join("?" * len(sample))
    cur.execute(
        f"SELECT id, name, session, gate_id FROM closed_mechanisms WHERE id IN ({placeholders})",
        sample
    )
    for r in cur.fetchall():
        print(f"  id={r[0]:28s} sess={(r[2] or '-'):8s} gate={(r[3] or '-')[:14]:14s} {(r[1] or '-')[:60]}")
