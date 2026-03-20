"""
Re-apply LaTeX generation batches 1 and 2 from the weaver inbox messages.
Parses the structured EQ_ID/LATEX format from the physicist's batch messages.
"""

import json
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "tools" / "knowledge-index.json"
WEAVER_INBOX = Path.home() / ".claude" / "teams" / "equation-audit" / "inboxes" / "weaver.json"

# Load index
with open(INDEX_PATH, encoding="utf-8") as f:
    idx = json.load(f)
eqs = idx["equations"]
eq_by_id = {eq["id"]: eq for eq in eqs}

# Load weaver inbox to extract batch messages
with open(WEAVER_INBOX, encoding="utf-8") as f:
    inbox = json.load(f)

# Find physicist batch messages
batch_msgs = []
for msg in inbox:
    if msg.get("from") == "physicist" and "BATCH" in msg.get("text", "")[:20]:
        batch_msgs.append(msg)

print(f"Found {len(batch_msgs)} batch messages")

# Parse EQ_ID/LATEX pairs from batch messages
EQ_RE = re.compile(r"EQ_ID:\s*(eq_\d+)")
LATEX_RE = re.compile(r"LATEX:\s*(.+)")
STATUS_RE = re.compile(r"STATUS:\s*(\w+)")

total_applied = 0
total_skipped = 0
total_updated = 0

for i, msg in enumerate(batch_msgs):
    text = msg["text"]
    lines = text.split("\n")

    current_id = None
    current_latex = None
    current_status = None
    batch_count = 0

    for line in lines:
        eq_match = EQ_RE.match(line.strip())
        if eq_match:
            # Apply previous equation if we have one
            if current_id and current_latex:
                if current_id in eq_by_id:
                    eq = eq_by_id[current_id]
                    old_latex = eq.get("latex")
                    eq["latex"] = current_latex
                    if current_status:
                        eq["audit_status"] = current_status
                    if old_latex:
                        total_updated += 1
                    else:
                        total_applied += 1
                    batch_count += 1
                else:
                    total_skipped += 1

            current_id = eq_match.group(1)
            current_latex = None
            current_status = None
            continue

        latex_match = LATEX_RE.match(line.strip())
        if latex_match:
            current_latex = latex_match.group(1).strip()
            continue

        status_match = STATUS_RE.match(line.strip())
        if status_match:
            current_status = status_match.group(1).strip()
            continue

    # Apply last equation in message
    if current_id and current_latex:
        if current_id in eq_by_id:
            eq = eq_by_id[current_id]
            old_latex = eq.get("latex")
            eq["latex"] = current_latex
            if current_status:
                eq["audit_status"] = current_status
            if old_latex:
                total_updated += 1
            else:
                total_applied += 1
            batch_count += 1
        else:
            total_skipped += 1

    print(f"  Batch {i+1}: {batch_count} equations applied")

print(f"\nTotal: {total_applied} new LaTeX, {total_updated} updated, {total_skipped} skipped")

# Write back
latex_count = sum(1 for eq in eqs if eq.get("latex"))
print(f"Total equations with LaTeX: {latex_count}")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)
print("Written.")
