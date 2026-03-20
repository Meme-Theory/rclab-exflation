"""Apply batch 5: Parse _batch5_msg.txt and apply LaTeX to knowledge-index.json."""
import json
import os
import re

ROOT = "C:/sandbox/Ainulindale Exflation"

# Parse the batch file
with open(os.path.join(ROOT, "tools/_batch5_msg.txt"), "r", encoding="utf-8") as f:
    content = f.read()

# Parse EQ_ID/LATEX pairs
batch = {}
blocks = re.split(r'\n\n+', content.strip())
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
        batch[eq_id] = latex

print(f"Parsed {len(batch)} equations from _batch5_msg.txt")

# Load index
with open(os.path.join(ROOT, "tools/knowledge-index.json"), "r", encoding="utf-8") as f:
    idx = json.load(f)

eq_map = {eq["id"]: i for i, eq in enumerate(idx["equations"])}

applied = 0
missing = []
for eid, latex in batch.items():
    if eid in eq_map:
        i = eq_map[eid]
        idx["equations"][i]["latex"] = latex
        applied += 1
    else:
        missing.append(eid)

with open(os.path.join(ROOT, "tools/knowledge-index.json"), "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)

with_latex = sum(1 for eq in idx["equations"] if eq.get("latex"))
print(f"Batch 5: {applied} applied, {len(missing)} missing")
if missing:
    print(f"  Missing: {missing}")
print(f"With LaTeX: {with_latex} / {len(idx['equations'])}")
