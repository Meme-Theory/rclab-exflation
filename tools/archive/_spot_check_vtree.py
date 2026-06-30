"""Spot-check: pick V_tree minimum (S17a, SP-4) and verify it has:
  (1) a stable canonical-namespace ID (closed_atlas02_eraI_1)
  (2) an incoming edge from sessions/S17a
  (3) an incoming edge from gates/SP-4
"""
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).resolve().parent / "knowledge.db")
cur = conn.cursor()

# 1. Find V_tree row
print("=== STEP 1: Find V_tree minimum row ===")
cur.execute(
    "SELECT id, name, session, gate_id, source_file "
    "FROM closed_mechanisms WHERE name LIKE '%V_tree%'"
)
rows = cur.fetchall()
print(f"Matching rows: {len(rows)}")
for r in rows:
    print(f"  id={r[0]!r}")
    print(f"    name={r[1]!r}, session={r[2]!r}, gate_id={r[3]!r}")
    print(f"    source_file={r[4]!r}")

if not rows:
    print("FAIL: V_tree minimum not found in closed_mechanisms")
    raise SystemExit(1)

v_tree_id = rows[0][0]
print(f"\n=== STEP 2: Has stable canonical-namespace ID? ===")
if v_tree_id.startswith("closed_atlas02_"):
    print(f"PASS: id={v_tree_id} uses canonical namespace")
else:
    print(f"FAIL: id={v_tree_id} is flat (should start with 'closed_atlas02_')")

print(f"\n=== STEP 3: Edges where target_id == {v_tree_id!r} ===")
cur.execute(
    "SELECT type, source_type, source_id, comment FROM edges "
    "WHERE target_id = ? AND target_type = 'closed_mechanisms'",
    (v_tree_id,)
)
inbound = cur.fetchall()
print(f"Inbound edges: {len(inbound)}")
for e in inbound:
    print(f"  [{e[0]}] {e[1]}/{e[2]}  -- {(e[3] or '')[:60]}")

print(f"\n=== STEP 4: Edges where source_id == {v_tree_id!r} (closures should have NONE) ===")
cur.execute(
    "SELECT type, target_type, target_id, comment FROM edges "
    "WHERE source_id = ? AND source_type = 'closed_mechanisms'",
    (v_tree_id,)
)
outbound = cur.fetchall()
print(f"Outbound edges: {len(outbound)}")
for e in outbound:
    print(f"  [{e[0]}] {e[1]}/{e[2]}  -- {(e[3] or '')[:60]}")

print()
print("=== VERDICT ===")
has_session_edge = any(e[1] == "sessions" for e in inbound)
has_gate_edge = any(e[1] == "gates" for e in inbound)
if has_session_edge and has_gate_edge:
    print("PASS: V_tree has both upstream session and gate edges")
elif has_session_edge:
    print("PARTIAL: V_tree has session edge but NO gate edge")
elif has_gate_edge:
    print("PARTIAL: V_tree has gate edge but NO session edge")
else:
    print("FAIL: V_tree still has no upstream edges")
