"""Throwaway audit: classify spectral-post-mortem rows + find legacy rows
with malformed session fields.

Output feeds the S90 handoff decision on whether to tighten Strategy 1
further, or accept the current legacy-path signal-to-noise.
"""
import re
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

print("=" * 78)
print("ALL 13 spectral-post-mortem rows")
print("=" * 78)
cur.execute(
    "SELECT id, name, closed_by, session, gate_id "
    "FROM closed_mechanisms WHERE source_file LIKE '%spectral-post-mortem%' "
    "ORDER BY id"
)
for r in cur.fetchall():
    print(f"  id={r[0]:30s} sess={(r[3] or '-'):10s} gate={(r[4] or '-')[:14]:14s}")
    print(f"    name      : {(r[1] or '-')[:100]}")
    print(f"    closed_by : {(r[2] or '-')[:100]}")
    print()

print("=" * 78)
print("Legacy rows with suspicious session fields")
print("(session present but doesn't FULLY match strict S?N[a-z] or Session N pattern)")
print("=" * 78)
session_re = re.compile(r"^(S?\d+[a-z]?|Session\s+\d+)$", re.IGNORECASE)
cur.execute("SELECT id, name, session, source_file FROM closed_mechanisms")
suspicious = []
for r in cur.fetchall():
    s = (r[2] or "").strip()
    if s and not session_re.match(s):
        suspicious.append(r)
print(f"Found {len(suspicious)} suspicious-session rows out of 280 total")
print()
for r in suspicious:
    src = (r[3] or "").replace("\\", "/")
    src_short = src.replace("sessions/", "")[:55]
    print(f"  session={r[2]:38s}  name={(r[1] or '')[:55]}")
    print(f"    src: {src_short}")

# Also: rows whose name is suspicious (numeric, single-letter, etc.)
print()
print("=" * 78)
print("Suspicious name patterns (numeric-only / very-short / fragment markers)")
print("=" * 78)
cur.execute(
    "SELECT id, name, session, source_file, closed_by FROM closed_mechanisms"
)
weird_name = []
NUMERIC_RE = re.compile(r"^[\d.\-]+$")
for r in cur.fetchall():
    n = (r[1] or "").strip()
    if not n:
        continue
    if NUMERIC_RE.match(n):
        weird_name.append((r, "NUMERIC_ONLY"))
    elif len(n) <= 3:
        weird_name.append((r, "SHORT"))
    elif n.lower().startswith(("the ", "a:", "b:", "c:", "d:", "e:", "f:")):
        # "The framing error..." or "A: Perturbative potential..."
        # The "A:" pattern is legitimate from session-25 Investigation-Closing;
        # "The X..." is the spectral-post-mortem section-heading noise.
        if n.lower().startswith("the "):
            weird_name.append((r, "HEADING-LIKE"))
print(f"Found {len(weird_name)} suspicious-name rows")
for (r, tag) in weird_name:
    src = (r[3] or "").replace("\\", "/").replace("sessions/", "")
    print(f"  [{tag:15s}] name={r[1]!r:55s}")
    print(f"    src: {src[:60]} closed_by={(r[4] or '')[:50]!r}")
