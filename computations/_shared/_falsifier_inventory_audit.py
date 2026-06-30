#!/usr/bin/env python
"""
_falsifier_inventory_audit.py — S89 W6-3 sub-item (iii)
========================================================

Falsifier-inventory audit. Scans
`sessions/framework/registry/falsifier-master-inventory.md` for
structural integrity of falsifier rows.

S89 W6-3 sub-item (iii) extension
----------------------------------
Adds **sign-PASS-tautology detection** per S88 W-5 V.4 (W1c-69
calibration corpus instance). A falsifier-inventory row is
sign-PASS-tautology iff its substrate prediction's SIGN is
mechanically forced by row-format conventions (e.g., absolute-value
ratio rows have sign = positive by construction; the row's sign-PASS
verdict conveys NO substrate-physics content).

Detection: rows whose prediction is wrapped in absolute-value bars
`|...|` and whose sign-PASS verdict adds no information beyond the
absolute-value convention.

Substrate framing
-----------------
The audit IS the methodology-layer F-image of the substrate-physics
falsifier-row content predicate. The sign-PASS-tautology pathology is
a methodology-floor failure: the row's SIGN-PASS is structurally vacuous
because the row's format (absolute-value wrapping) forces sign-positive
by construction.

CLI
---
    python _falsifier_inventory_audit.py [--inventory PATH] [--json]
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    print("ERROR: canonical_constants.py import failed", file=sys.stderr)
    raise


# ---------------------------------------------------------------------------
# §W6-3 sub-item (iii) Sign-PASS-tautology detection patterns
# ---------------------------------------------------------------------------
ROW_PATTERN = (  # (local) Markdown-table falsifier rows
    r"\|\s*F\d+\s*\|.*?\n"
)
ABS_VALUE_WRAP_PATTERN = (  # (local) |...| wrapping with > or < bound
    r"\|.*\|\s*[><=]"
)
SIGNED_RATIO_PATTERN = (  # (local) explicit + or - prefix on number
    r"(?<![A-Za-z|])(?:\+|\-)\s*\d"
)


def sign_pass_tautology_audit(inventory_text: str) -> dict[str, Any]:
    """
    Per W-5 V.4 (W1c-69 sign-PASS-tautology corpus instance):

    A falsifier-inventory row is sign-PASS-tautology iff its substrate
    prediction's SIGN is mechanically forced by row-format conventions.

    Detection: rows whose prediction is wrapped in absolute-value bars
    AND whose sign-PASS verdict adds no information.
    """
    rows = re.findall(ROW_PATTERN, inventory_text)
    findings: list[dict[str, Any]] = []  # local
    for row in rows:
        is_abs_value = bool(re.search(ABS_VALUE_WRAP_PATTERN, row))
        is_signed_ratio = bool(re.search(SIGNED_RATIO_PATTERN, row))
        if is_abs_value and not is_signed_ratio:
            findings.append({
                "row": row.strip()[:200],
                "sign_pass_tautology": True,
                "severity": "MANDATORY",
                "remediation": (
                    "Reformulate row to use signed substrate prediction, OR "
                    "explicitly disclose sign-PASS-tautology in row text "
                    "(per W-5 V.4 calibration corpus W1c-69)."
                ),
            })
    return {
        "rule_source": "S88 W-5 V.4 (W1c-69 calibration corpus instance)",
        "n_rows_scanned": len(rows),
        "n_tautology_rows": len(findings),
        "findings": findings,
        "verdict": "PASS" if not findings else "FAIL",
        "severity": "NO-ACTION" if not findings else "MANDATORY",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inventory",
        default="sessions/framework/registry/falsifier-master-inventory.md",
        help="Falsifier inventory markdown path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    p = Path(args.inventory)
    if not p.exists():
        report = {
            "gate": "falsifier-inventory-audit",
            "inventory_path": args.inventory,
            "verdict": "INFO",
            "reason": "Inventory file not found; audit cannot proceed.",
        }
        print(json.dumps(report, indent=2))
        return 0

    text = p.read_text(encoding="utf-8")
    coh = sign_pass_tautology_audit(text)
    report = {
        "gate": "falsifier-inventory-audit",
        "inventory_path": args.inventory,
        "sign_pass_tautology_audit": coh,
    }
    print(json.dumps(report, indent=2))
    return 0 if coh["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
