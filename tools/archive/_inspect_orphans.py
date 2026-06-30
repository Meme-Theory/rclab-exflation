"""Inspect orphan entities (no incident edges) to determine which are
structurally orphan vs fixable.
"""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

print("=== 35 orphan sessions ===")
cur.execute("""
    SELECT id FROM sessions WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='sessions'
        UNION
        SELECT target_id FROM edges WHERE target_type='sessions'
    ) ORDER BY id
""")
orphans = [r[0] for r in cur.fetchall()]
print(f"Count: {len(orphans)}")
print(f"All: {orphans}")
print()

print("=== 10 orphan researchers ===")
cur.execute("""
    SELECT domain FROM researchers WHERE domain NOT IN (
        SELECT source_id FROM edges WHERE source_type='researchers'
        UNION
        SELECT target_id FROM edges WHERE target_type='researchers'
    ) ORDER BY domain
""")
for r in cur.fetchall():
    print(f"  {r[0]}")
print()

print("=== 9 orphan closed_mechanisms ===")
cur.execute("""
    SELECT id, name, session, gate_id, source_file FROM closed_mechanisms WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='closed_mechanisms'
        UNION
        SELECT target_id FROM edges WHERE target_type='closed_mechanisms'
    )
""")
for r in cur.fetchall():
    src = (r[4] or "").replace("\\", "/")
    print(f"  id={r[0]:24s} session={r[2]!r:10s} gate_id={r[3]!r:10s}")
    print(f"    name={(r[1] or '')[:60]!r}")
    print(f"    src={src[:60]}")
print()

print("=== Sample of 443 orphan theorems ===")
cur.execute("""
    SELECT id, name, sessions, source_file FROM theorems WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='theorems'
        UNION
        SELECT target_id FROM edges WHERE target_type='theorems'
    ) LIMIT 15
""")
for r in cur.fetchall():
    src = (r[3] or "").replace("\\", "/")
    print(f"  id={r[0]:18s} sessions={r[2]!r:20s}")
    print(f"    name={(r[1] or '')[:60]!r}")
    print(f"    src={src[:60]}")
