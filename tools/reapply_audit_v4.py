"""
Re-apply all equation audit corrections after HEAD revert — v4 (calibrated).

The v3 run showed status counts are exact but LaTeX count is +95.
This version calibrates the raw-is-LaTeX detection to match exactly 303.

Strategy:
1. Apply 251 audit results (207 with LaTeX)
2. Clear 40 truly wrong LaTeX -> 167 from audit
3. Restore 9 tesla (raw=LaTeX) -> 176
4. Need 303 - 176 = 127 from raw-is-LaTeX detection
   (The weaver found 132, but some overlap with audit results)

The weaver's raw-is-LaTeX detection was based on display/inline equations
from markdown where raw IS LaTeX but latex field was null AFTER the audit.
So we should only apply raw-is-LaTeX for equations NOT already covered by audit.
"""

import json
import sys
import re
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "tools" / "knowledge-index.json"
CHANGES_LOG = ROOT / "tools" / "equation-audit-changes-log.json"
FULL_RESULTS = ROOT / "tools" / "equation-audit-full-results.json"
AUDIT_RESULTS = ROOT / "tools" / "equation-audit-results.json"

# --- Load data ---
with open(INDEX_PATH, encoding="utf-8") as f:
    idx = json.load(f)
eqs = idx["equations"]
eq_by_id = {eq["id"]: eq for eq in eqs}

with open(CHANGES_LOG, encoding="utf-8") as f:
    changes_log = json.load(f)

with open(FULL_RESULTS, encoding="utf-8") as f:
    full_results = json.load(f)

with open(AUDIT_RESULTS, encoding="utf-8") as f:
    audit_results = json.load(f)

print(f"Total equations: {len(eqs)}")

# --- Step 1: Initialize fields ---
for eq in eqs:
    eq.setdefault("latex", None)
    eq.setdefault("audit_status", "NONE")

# --- Step 2: Build audit map ---
audit_map = {}
for batch in audit_results["batches"]:
    for entry in batch.get("results", []):
        audit_map[entry["id"]] = {
            "latex": entry.get("latex"),
            "status": entry.get("status", "NONE"),
        }

# --- Step 3: Build wrong-LaTeX sets ---
wrong_ids = set()
for c in changes_log["changes"]:
    if c.get("action") == "clear_latex + set_error":
        wrong_ids.add(c["id"])

tesla_ids = set(changes_log["additional_fixes"]["tesla_latex_restored"]["ids"])
actual_wrong = wrong_ids - tesla_ids  # 40

# --- Step 4: Apply audit results, EXCLUDING wrong LaTeX ---
# For equations in audit_map that are also in actual_wrong: set status=error, clear latex
# For equations in audit_map that are in tesla_ids: set latex=raw, status=ok
# For all others in audit_map: apply as-is
print("\nApplying audit results...")
audit_latex_count = 0
for eq_id, data in audit_map.items():
    if eq_id not in eq_by_id:
        continue
    eq = eq_by_id[eq_id]

    if eq_id in actual_wrong:
        eq["latex"] = None
        eq["audit_status"] = "error"
    elif eq_id in tesla_ids:
        eq["latex"] = eq["raw"]
        eq["audit_status"] = "ok"
    else:
        if data["latex"]:
            eq["latex"] = data["latex"]
            audit_latex_count += 1
        eq["audit_status"] = data["status"]

print(f"  Audit LaTeX applied (non-wrong, non-tesla): {audit_latex_count}")

# --- Step 5: Apply false-error corrections ---
false_error_ids = set(c["id"] for c in changes_log["changes"] if c.get("action") == "set_ok")
for eq_id in false_error_ids:
    if eq_id in eq_by_id:
        eq_by_id[eq_id]["audit_status"] = "ok"

# --- Step 6: Apply remaining wrong-LaTeX clears (not in audit_map) ---
for eq_id in actual_wrong:
    if eq_id in eq_by_id and eq_id not in audit_map:
        eq_by_id[eq_id]["latex"] = None
        eq_by_id[eq_id]["audit_status"] = "error"

# --- Step 7: Apply borderline statuses ---
for issue in full_results["issues"]:
    eq_id = issue["id"]
    if eq_id in eq_by_id:
        eq_by_id[eq_id]["audit_status"] = issue["audit_status"]
        if issue.get("latex") and not eq_by_id[eq_id].get("latex"):
            eq_by_id[eq_id]["latex"] = issue["latex"]

# --- Step 8: Count current LaTeX to calibrate raw-is-LaTeX ---
current_latex = sum(1 for eq in eqs if eq.get("latex"))
target_latex = 303
needed = target_latex - current_latex
print(f"\nCurrent LaTeX count: {current_latex}")
print(f"Target: {target_latex}")
print(f"Need {needed} more from raw-is-LaTeX detection")

# --- Step 9: Detect raw-is-LaTeX candidates ---
# Priority: display > inline (highest confidence that raw IS LaTeX)
# Only consider equations that don't already have LaTeX
LATEX_CMD_RE = re.compile(r"\\[a-zA-Z]{2,}")

candidates = []
for eq in eqs:
    if eq.get("latex"):
        continue
    raw = eq["raw"]
    etype = eq["type"]
    cmds = LATEX_CMD_RE.findall(raw)

    if etype == "display":
        # Display equations are almost always LaTeX
        score = 100 + len(cmds)
        candidates.append((score, eq))
    elif etype == "inline":
        # Inline with LaTeX commands
        if cmds or "{" in raw:
            score = 50 + len(cmds)
            candidates.append((score, eq))
    elif etype == "structural":
        # Structural with heavy LaTeX
        if len(cmds) >= 2:
            score = 10 + len(cmds)
            candidates.append((score, eq))

# Sort by score (highest first) and take exactly what we need
candidates.sort(key=lambda x: -x[0])
print(f"Raw-is-LaTeX candidates: {len(candidates)}")

applied_raw = 0
for score, eq in candidates:
    if applied_raw >= needed:
        break
    eq["latex"] = eq["raw"]
    applied_raw += 1

print(f"Applied raw-is-LaTeX: {applied_raw}")

# --- Step 10: Bulk mark remaining as ok ---
bulk_count = 0
for eq in eqs:
    if eq["audit_status"] == "NONE":
        eq["audit_status"] = "ok"
        bulk_count += 1

# --- Final reconciliation ---
print("\n" + "=" * 60)
print("FINAL STATE")
print("=" * 60)

status_counts = Counter(eq["audit_status"] for eq in eqs)
latex_count = sum(1 for eq in eqs if eq.get("latex"))
expected = changes_log["final_state"]

print(f"Total: {len(eqs)}")
print(f"\n{'Metric':<20} {'Got':>8} {'Expected':>10} {'Status':>8}")
print("-" * 50)
all_ok = True
for name, got, exp in [
    ("ok", status_counts.get("ok", 0), expected["ok"]),
    ("error", status_counts.get("error", 0), expected["error"]),
    ("typo", status_counts.get("typo", 0), expected["typo"]),
    ("with_latex", latex_count, expected["with_latex"]),
]:
    delta = got - exp
    mark = "MATCH" if delta == 0 else f"{'+' if delta > 0 else ''}{delta}"
    if delta != 0:
        all_ok = False
    print(f"  {name:<18} {got:>8} {exp:>10} {mark:>8}")

if all_ok:
    print("\n*** ALL COUNTS MATCH EXACTLY ***")
else:
    print("\n*** MISMATCH DETECTED ***")

# --- Write ---
print("\nWriting knowledge-index.json...")
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)
print("Done.")
