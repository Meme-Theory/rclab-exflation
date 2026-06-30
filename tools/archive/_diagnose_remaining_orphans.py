"""Diagnose where the remaining orphan rows come from."""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

print("=== Orphan equation source_files (top 15) ===")
cur.execute("""
    SELECT source_file, COUNT(*) FROM equations
    WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='equations'
        UNION SELECT target_id FROM edges WHERE target_type='equations'
    )
    GROUP BY source_file ORDER BY COUNT(*) DESC LIMIT 15
""")
for r in cur.fetchall():
    norm = (r[0] or "").replace("\\", "/")[:70]
    print(f"  {r[1]:5d}  {norm}")

print()
print("=== Orphan data_provenance scripts (top 15) ===")
cur.execute("""
    SELECT script, session, outputs FROM data_provenance
    WHERE script NOT IN (
        SELECT source_id FROM edges WHERE source_type='data_provenance'
        UNION SELECT target_id FROM edges WHERE target_type='data_provenance'
    ) LIMIT 15
""")
for r in cur.fetchall():
    norm = (r[0] or "").replace("\\", "/")[:60]
    print(f"  session={r[1]!r:6s}  script={norm}")

print()
print("=== Orphan session_files (top 15) ===")
cur.execute("""
    SELECT path, filename FROM session_files
    WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='session_files'
        UNION SELECT target_id FROM edges WHERE target_type='session_files'
    ) LIMIT 15
""")
for r in cur.fetchall():
    print(f"  {r[0][:70]}")

print()
print("=== 17 orphan constants ===")
cur.execute("""
    SELECT name FROM constants
    WHERE name NOT IN (
        SELECT source_id FROM edges WHERE source_type='constants'
        UNION SELECT target_id FROM edges WHERE target_type='constants'
    )
""")
for r in cur.fetchall():
    print(f"  {r[0]}")

print()
print("=== 1 orphan session ===")
cur.execute("""
    SELECT id FROM sessions WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='sessions'
        UNION SELECT target_id FROM edges WHERE target_type='sessions'
    )
""")
for r in cur.fetchall():
    print(f"  {r[0]}")
