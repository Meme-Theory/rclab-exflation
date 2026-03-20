#!/usr/bin/env python3
"""Apply equation audit results to knowledge-index.json.

Reads tools/equation-audit-results.json and applies:
  1. LaTeX formatting (207 equations)
  2. Audit status (ok/error/typo) for all audited equations
  3. Type reclassifications (46 misclassified equations)

Reusable: safe to re-run (idempotent).
"""
import json
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
INDEX_PATH = TOOLS_DIR / "knowledge-index.json"
AUDIT_PATH = TOOLS_DIR / "equation-audit-results.json"

# --- Misclassification corrections (46 total) ---
# Source: equation-audit-results.json batches 1, 2, 6
# Identified by gen-physicist auditor, cross-referenced by knowledge-weaver

RECLASSIFY_TO_CODE = {
    # Batch 1: Python code in fenced blocks captured as structural
    "eq_24", "eq_25", "eq_26",
    "eq_37", "eq_38", "eq_39", "eq_40",
    "eq_42", "eq_43", "eq_44", "eq_45", "eq_46", "eq_47",
    # Batch 2: Session 16 Round 2b fenced Python blocks (22 consecutive)
    "eq_62", "eq_63", "eq_64", "eq_65", "eq_66", "eq_67", "eq_68", "eq_69",
    "eq_70", "eq_71", "eq_72", "eq_73", "eq_74", "eq_75", "eq_76", "eq_77",
    "eq_78", "eq_79", "eq_80", "eq_81", "eq_82", "eq_83",
    "eq_95", "eq_97", "eq_98",
    # Batch 6: Remaining structural sampling
    "eq_104", "eq_105",
}  # 40 entries

RECLASSIFY_TO_COMMENT = {
    # Prose fragments / log messages / headers misclassified as structural
    "eq_27", "eq_48",   # Batch 1: procedural instruction, log message
    "eq_86", "eq_91",   # Batch 2: not-equation, header
    "eq_161", "eq_164", # Batch 6: topology prose, prose fragment
}  # 6 entries


def main():
    # Load knowledge index
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index = json.load(f)

    equations = index.get("equations", [])
    eq_by_id = {eq["id"]: eq for eq in equations}
    print(f"Loaded {len(equations)} equations from knowledge index")

    # Load audit results
    with open(AUDIT_PATH, "r", encoding="utf-8") as f:
        audit = json.load(f)

    # --- Pass 1: Apply LaTeX + audit_status from audit results ---
    latex_added = 0
    status_added = 0

    for batch in audit["batches"]:
        for result in batch["results"]:
            eq_id = result["id"]
            if eq_id not in eq_by_id:
                continue

            eq = eq_by_id[eq_id]

            # Add LaTeX if present and non-empty
            latex = (result.get("latex") or "").strip()
            if latex:
                eq["latex"] = latex
                latex_added += 1

            # Add audit status
            status = (result.get("status") or "").strip()
            if status:
                eq["audit_status"] = status
                status_added += 1

    # --- Pass 2: Apply type reclassifications ---
    reclassified_code = 0
    reclassified_comment = 0
    missing_ids = []

    for eq_id in RECLASSIFY_TO_CODE:
        if eq_id in eq_by_id:
            eq_by_id[eq_id]["type"] = "code"
            reclassified_code += 1
        else:
            missing_ids.append(eq_id)

    for eq_id in RECLASSIFY_TO_COMMENT:
        if eq_id in eq_by_id:
            eq_by_id[eq_id]["type"] = "comment"
            reclassified_comment += 1
        else:
            missing_ids.append(eq_id)

    # --- Write back ---
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
        f.write("\n")  # trailing newline

    # --- Summary ---
    print(f"\nAudit applied successfully:")
    print(f"  LaTeX added:              {latex_added}")
    print(f"  Audit status added:       {status_added}")
    print(f"  Reclassified -> code:     {reclassified_code}")
    print(f"  Reclassified -> comment:  {reclassified_comment}")
    print(f"  Total reclassified:       {reclassified_code + reclassified_comment}")

    if missing_ids:
        print(f"\n  WARNING: {len(missing_ids)} IDs not found in index: {missing_ids}")


if __name__ == "__main__":
    main()
