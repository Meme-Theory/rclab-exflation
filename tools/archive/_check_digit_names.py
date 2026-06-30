"""Throwaway: check what closure names currently start with a digit, to gauge
the impact of adding a digit-leading-name filter to the legacy parser."""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()
cur.execute(
    "SELECT id, name, source_file FROM closed_mechanisms "
    "WHERE name GLOB '[0-9]*' OR name GLOB '-[0-9]*' OR name GLOB '+[0-9]*'"
)
rows = cur.fetchall()
print(f"Rows where name STARTS with digit/sign-digit: {len(rows)}")
print()
for r in rows:
    src_norm = (r[2] or "").replace("\\", "/").replace("sessions/", "")
    print(f"  name={r[1]!r:55s}")
    print(f"     src={src_norm[:60]}")
