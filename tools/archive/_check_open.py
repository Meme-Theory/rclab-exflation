import sqlite3
from pathlib import Path
conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()
cur.execute("""
    SELECT name, session, source_file FROM open_channels
    WHERE name NOT IN (
        SELECT source_id FROM edges WHERE source_type='open_channels'
        UNION SELECT target_id FROM edges WHERE target_type='open_channels'
    )
""")
print("Orphan open_channels:")
for r in cur.fetchall():
    src = (r[2] or "").replace("\\", "/")
    print(f"  name={r[0]!r}")
    print(f"    session={r[1]!r}")
    print(f"    source_file={src}")
