#!/usr/bin/env python
"""
_pru_class_8_3_retroactive_audit_w6a_51.py — S89 W6-5 (A.33)
=============================================================

Retroactive PRU Class 8.3 audit on W6a-51 plan §10 Step 8 pre-registered
estimate `≈4e-9`.

Per `epistemic-discipline.md §"Publication-Precision Pre-Registration
(Class 8.3, MANDATORY at K=4)"` (existing K=4 MANDATORY clause), every
gate's pre-registered numerical estimate must declare:
    (1) explicit precision pin (publication_sig_figs / sig_figs);
    (2) substrate-first canonical-sourcing chain (CM-1995 / Connes-Moscovici
        / Seeley-DeWitt / Jensen perturbation OR equivalent first-principles
        derivation).

The W6a-51 estimate `≈4e-9` (originating in S88 W-19 V.4 substrate-derivable
estimate baseline) is classified into one of:
    PASS   — substrate-derivable AND precision-pinned (Class 8.3 satisfied)
    INFO   — substrate-derivable but missing precision pin (Class 8.3 advisory)
    FAIL   — ad-hoc placeholder without substrate-physics chain (Class-(f)
             PIN-PLACEHOLDER MANDATORY remediation)

Substrate framing
-----------------
The audit IS the methodology-layer F-image of the substrate-physics
estimate-provenance predicate. The estimate `≈4e-9` either traces to a
substrate-derivation chain (which the audit verifies via citation
patterns) or is an ad-hoc placeholder (which the audit flags via
placeholder pattern detection).

CLI
---
    python _pru_class_8_3_retroactive_audit_w6a_51.py [--plan PATH] [--json]
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
# Pattern sets per plan §6
# ---------------------------------------------------------------------------
PRECISION_PIN_PATTERNS: tuple[str, ...] = (  # (local) Class 8.3 precision-pin markers
    r"\bprecision_pin\s*[:=]",
    r"\bpublication_sig_figs\s*[:=]",
    r"\bsig_figs\s*[:=]",
    r"\brel_tol\s*[:=]",
    r"\babs_tol\s*[:=]\s*\d",
)

SUBSTRATE_DERIVATION_PATTERNS: tuple[str, ...] = (  # (local) substrate-physics chain markers
    r"\bCM[\- ]1995\b",
    r"\bConnes[\- ]Moscovici\b",
    r"\bSeeley[\- ]DeWitt\b",
    r"\bJensen\s+perturbation\b",
    r"\bsubstrate[\- ]derivable\b",
    r"\bfirst[\- ]principles\b",
    r"\bChamseddine[\- ]Connes\s+1996\b",
    r"\bspectral[\- ]action\s+a_n\b",
)

PLACEHOLDER_PATTERNS: tuple[str, ...] = (  # (local) Class-(f) placeholder markers
    r"O\(10\^?-?\d+\)",
    r"≈\s*10\^?-?\d+",
    r"≈\s*\d+e-?\d+",
    r"~\s*10\^?-?\d+",
    r"\bplaceholder\b",
    r"\bTBD\b",
    r"\bpending\b",
    r"\banalytic\s+estimate\b",
    r"\brough\s+estimate\b",
)


def _any_pattern_matches(text: str, patterns: tuple[str, ...]) -> bool:
    """Return True if ANY pattern in `patterns` matches `text`."""
    for pat in patterns:
        if re.search(pat, text):
            return True
    return False


def retroactive_class_8_3_audit(plan_path: Path) -> dict[str, Any]:
    """
    Audit the W6a-51 plan §10 Step 8 estimate `≈4e-9` against:
      (1) Class 8.3 publication-precision pre-registration
      (2) substrate-first canonical-sourcing
      (3) Class-(f) PIN-PLACEHOLDER detection
    """
    if not plan_path.exists():
        return {
            "gate": "S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51",
            "plan_path": str(plan_path),
            "verdict": "INFO",
            "reason": (
                f"W6a-51 plan file not found at {plan_path}. The audit "
                "cannot locate the §10 Step 8 block; this is itself a "
                "structural finding (the plan-file the §VII anchor cites "
                "does not exist on disk). Routes to a meta-remediation: "
                "either (a) restore the W6a plan file, or (b) update "
                "downstream registry/inventory entries that cite the "
                "estimate `≈4e-9` to point to a different substrate-"
                "derivation source."
            ),
            "severity": "MANDATORY",
            "rule_source": (
                "epistemic-discipline.md §\"Publication-Precision "
                "Pre-Registration (Class 8.3, MANDATORY at K=4)\" + "
                "substrate-first-canonical-sourcing.md §(v) Class-(f)"
            ),
        }

    text = plan_path.read_text(encoding="utf-8")
    # Locate W6a-51 §10 Step 8 block. Multi-line dotall match.
    pattern_step8 = (
        r"§W6a-51.*?§10.*?Step\s*8.*?(?:≈\s*4e-?9|4\s*[xX×]\s*10\^?-?9)"
    )
    match = re.search(pattern_step8, text, re.DOTALL)
    if not match:
        return {
            "gate": "S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51",
            "plan_path": str(plan_path),
            "verdict": "INFO",
            "reason": (
                "W6a-51 §10 Step 8 block not located in plan file. The "
                "estimate `≈4e-9` is not present at the cited anchor."
            ),
            "severity": "ADVISORY",
        }

    block_text = match.group(0)

    # Class 8.3 precision pin
    has_precision_pin = _any_pattern_matches(block_text, PRECISION_PIN_PATTERNS)
    # Substrate-first canonical-sourcing
    has_substrate_derivation = _any_pattern_matches(
        block_text, SUBSTRATE_DERIVATION_PATTERNS)
    # Class-(f) placeholder
    is_placeholder = _any_pattern_matches(block_text, PLACEHOLDER_PATTERNS)

    # Verdict per plan §9
    if has_substrate_derivation and has_precision_pin:
        verdict = "PASS"
        severity = "NO-ACTION"
        rationale = (
            "Estimate is substrate-derivable AND has precision pin; "
            "PRU Class 8.3 satisfied."
        )
    elif has_substrate_derivation and not has_precision_pin:
        verdict = "INFO"
        severity = "ADVISORY"
        rationale = (
            "Substrate-derivable but missing precision pin; "
            "Class 8.3 advisory remediation."
        )
    elif is_placeholder and not has_substrate_derivation:
        verdict = "FAIL"
        severity = "MANDATORY"
        rationale = (
            "Ad-hoc placeholder without substrate derivation; "
            "Class-(f) PIN-PLACEHOLDER MANDATORY remediation."
        )
    else:
        verdict = "FAIL"
        severity = "MANDATORY"
        rationale = (
            "Estimate lacks both substrate derivation AND precision pin."
        )

    return {
        "gate": "S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51",
        "plan_path": str(plan_path),
        "block_text_head": block_text[:400],
        "has_precision_pin": has_precision_pin,
        "has_substrate_derivation": has_substrate_derivation,
        "is_placeholder": is_placeholder,
        "verdict": verdict,
        "severity": severity,
        "rationale": rationale,
        "rule_source": (
            "epistemic-discipline.md §\"Publication-Precision "
            "Pre-Registration (Class 8.3)\" + "
            "substrate-first-canonical-sourcing.md §(v) Class-(f)"
        ),
        "remediation": (
            "Add precision pin (publication_sig_figs = N) AND/OR "
            "substrate-derivation citation (e.g., 'CM-1995 §III.4 Jensen "
            "perturbation chain reproduces 4e-9 from first principles')."
        ) if verdict != "PASS" else "No remediation required.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--plan",
        default="sessions/session-plan/session-88-plan-w6a.md",
        help="W6a plan file (default: session-88-plan-w6a.md per plan §W6-5)")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = retroactive_class_8_3_audit(Path(args.plan))
    print(json.dumps(report, indent=2))
    return 0 if report["verdict"] in ("PASS", "INFO") else 1


if __name__ == "__main__":
    sys.exit(main())
