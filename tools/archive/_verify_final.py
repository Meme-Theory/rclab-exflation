"""Throwaway: verify final closed_mechanisms state after S90 cleanup."""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM closed_mechanisms")
total = cur.fetchone()[0]
print(f"TOTAL closed_mechanisms: {total}")
print()
print("=== Critical-check counts (final state) ===")
checks = [
    ("atlas-02 canonical inventory", "%atlas-02%"),
    ("atlas-04 assumptions (expect 0)", "%atlas-04%"),
    ("permanent-results §V (no rollups)", "%permanent-results%"),
    ("spectral-post-mortem (expect 0)", "%spectral-post-mortem%"),
    ("closed-gw-channels", "%closed-gw-channels%"),
]
for label, pattern in checks:
    cur.execute(
        f"SELECT COUNT(*) FROM closed_mechanisms WHERE source_file LIKE '{pattern}'"
    )
    print(f"  {cur.fetchone()[0]:4d}  {label}")
print()
print("=== Cleanup trajectory ===")
print(f"  S89-baseline:           735 rows (95%+ noise)")
print(f"  S89-end:                306 rows  (-58.4% from baseline)")
print(f"  S90-after-issue-1+2:    280 rows  (-8.5% from S89-end)")
print(f"  S90-final:              {total} rows  (-{(280-total)*100//280}% additional)")
print()
print("=== Top source_files (final) ===")
cur.execute(
    "SELECT source_file, COUNT(*) FROM closed_mechanisms "
    "GROUP BY source_file ORDER BY COUNT(*) DESC LIMIT 12"
)
for src, cnt in cur.fetchall():
    norm = src.replace("\\", "/")
    short = norm.replace("sessions/", "")[:62]
    print(f"  {cnt:5d}  {short}")
