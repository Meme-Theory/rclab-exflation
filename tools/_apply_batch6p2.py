"""Apply batch 6: skip report (41 type reclassifications) + part 2 (102 LaTeX entries)."""
import json
import os
import re

ROOT = "C:/sandbox/Ainulindale Exflation"

# --- Parse skip report ---
with open(os.path.join(ROOT, "tools/_batch6_skip.txt"), "r", encoding="utf-8") as f:
    skip_content = f.read()

skip_ids = []
blocks = re.split(r'\n\n+', skip_content.strip())
for block in blocks:
    lines = block.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line.startswith("EQ_ID:"):
            eq_id = line.split(":", 1)[1].strip()
            skip_ids.append(eq_id)
            break

print(f"Parsed {len(skip_ids)} skip IDs from _batch6_skip.txt")

# --- Parse part 2 ---
with open(os.path.join(ROOT, "tools/_batch6_msg_part2.txt"), "r", encoding="utf-8") as f:
    p2_content = f.read()

batch_p2 = {}
blocks = re.split(r'\n\n+', p2_content.strip())
for block in blocks:
    lines = block.strip().split('\n')
    eq_id = None
    latex = None
    for line in lines:
        line = line.strip()
        if line.startswith("EQ_ID:"):
            eq_id = line.split(":", 1)[1].strip()
        elif line.startswith("LATEX:"):
            latex = line.split(":", 1)[1].strip()
    if eq_id and latex:
        batch_p2[eq_id] = latex

print(f"Parsed {len(batch_p2)} equations from _batch6_msg_part2.txt")

# --- Load index ---
with open(os.path.join(ROOT, "tools/knowledge-index.json"), "r", encoding="utf-8") as f:
    idx = json.load(f)

eq_map = {eq["id"]: i for i, eq in enumerate(idx["equations"])}

# --- Apply skip reclassifications ---
reclassified = 0
skip_missing = []
for eid in skip_ids:
    if eid in eq_map:
        i = eq_map[eid]
        old_type = idx["equations"][i].get("type", "unknown")
        idx["equations"][i]["type"] = "comment"
        reclassified += 1
    else:
        skip_missing.append(eid)

print(f"\nSkip report: {reclassified} reclassified to 'comment', {len(skip_missing)} missing")
if skip_missing:
    print(f"  Missing: {skip_missing}")

# --- Apply part 2 LaTeX ---
applied = 0
p2_missing = []
set_ok = 0
for eid, latex in batch_p2.items():
    if eid in eq_map:
        i = eq_map[eid]
        idx["equations"][i]["latex"] = latex
        applied += 1
        if idx["equations"][i].get("audit_status") != "ok":
            idx["equations"][i]["audit_status"] = "ok"
            set_ok += 1
    else:
        p2_missing.append(eid)

print(f"Part 2: {applied} LaTeX applied, {len(p2_missing)} missing, {set_ok} newly set to ok")
if p2_missing:
    print(f"  Missing: {p2_missing}")

# --- Write back ---
with open(os.path.join(ROOT, "tools/knowledge-index.json"), "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)

# --- Summary stats ---
with_latex = sum(1 for eq in idx["equations"] if eq.get("latex"))
type_counts = {}
for eq in idx["equations"]:
    t = eq.get("type", "unknown")
    type_counts[t] = type_counts.get(t, 0) + 1
status_counts = {}
for eq in idx["equations"]:
    s = eq.get("audit_status", "NONE") or "NONE"
    status_counts[s] = status_counts.get(s, 0) + 1

print(f"\n=== FINAL INDEX STATE ===")
print(f"Total equations: {len(idx['equations'])}")
print(f"With LaTeX: {with_latex}")
print(f"Type breakdown:")
for k, v in sorted(type_counts.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
print(f"Audit status:")
for k, v in sorted(status_counts.items()):
    print(f"  {k}: {v}")
