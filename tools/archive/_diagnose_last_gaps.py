"""Last gap diagnosis."""
import sqlite3
from collections import Counter
from pathlib import Path
conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

print("=== Orphan equations by source_file directory ===")
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
        dirs["/".join(parts[:2])] += 1
    else:
        dirs[src] += 1
for k, v in dirs.most_common(15):
    print(f"  {v:5d}  {k}")

print()
print("=== Orphan data_provenance — what's missing? ===")
cur.execute("""
    SELECT script, session, name FROM data_provenance
    WHERE script IS NULL OR script = '' OR script NOT IN (
        SELECT source_id FROM edges WHERE source_type='data_provenance' AND source_id != ''
        UNION
        SELECT target_id FROM edges WHERE target_type='data_provenance' AND target_id != ''
    )
    LIMIT 12
""")
for r in cur.fetchall():
    print(f"  script={r[0]!r}, session={r[1]!r}, name={r[2]!r}")

print()
print("=== 144 orphan session_files (top 12) ===")
cur.execute("""
    SELECT path FROM session_files
    WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='session_files'
        UNION SELECT target_id FROM edges WHERE target_type='session_files'
    ) LIMIT 12
""")
for r in cur.fetchall():
    print(f"  {r[0]}")

print()
print("=== 7 orphan gates ===")
cur.execute("""
    SELECT id, name FROM gates WHERE id NOT IN (
        SELECT source_id FROM edges WHERE source_type='gates'
        UNION SELECT target_id FROM edges WHERE target_type='gates'
    )
""")
for r in cur.fetchall():
    print(f"  id={r[0]!r}, name={(r[1] or '')[:60]!r}")
