"""Throwaway: sample 20 random legacy-path closed_mechanisms for signal-to-noise.

Handoff §6 step 4: verify the legacy-path remainder (~50 rows after canonical-
source extraction) is mostly real signal rather than residual noise.
"""
import random
import sqlite3
from pathlib import Path

random.seed(42)
db = Path(__file__).resolve().parent / "knowledge.db"
conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute(
    "SELECT id, name, closed_by, session, gate_id, source_file "
    "FROM closed_mechanisms"
)
all_rows = cur.fetchall()

CANONICAL = ("atlas-02", "permanent-results", "closed-gw-channels")
legacy = [r for r in all_rows if not any(p in (r[5] or "") for p in CANONICAL)]

print(f"Total closed_mechanisms:  {len(all_rows)}")
print(f"Canonical-source rows:    {len(all_rows) - len(legacy)}")
print(f"Legacy-path remainder:    {len(legacy)}")
print()

sample = random.sample(legacy, min(20, len(legacy)))
print(f"=== 20 random legacy-path samples (deterministic seed=42) ===")
for i, r in enumerate(sample, 1):
    src = (r[5] or "")
    src_short = src.replace("sessions\\", "").replace("sessions/", "")[:50]
    print(f"  [{i:2d}] sess={(r[3] or '-'):8s} gate={(r[4] or '-')[:14]:14s}")
    print(f"       src: {src_short}")
    print(f"       name: {(r[1] or '-')[:100]}")
    print(f"       closed_by: {(r[2] or '-')[:100]}")
    print()

# Also categorize the legacy remainder by source-file directory
print("=== Legacy remainder by directory ===")
from collections import Counter
dirs = Counter()
for r in legacy:
    src = (r[5] or "").replace("\\", "/")
    if "/archive/" in src.lower():
        dirs["archive"] += 1
    elif "/workshops/" in src.lower():
        dirs["workshops"] += 1
    elif "/session-" in src.lower():
        dirs["session-N (active)"] += 1
    else:
        dirs["other"] += 1
for k, v in dirs.most_common():
    print(f"  {v:4d}  {k}")
