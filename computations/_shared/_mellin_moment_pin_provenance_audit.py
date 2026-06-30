#!/usr/bin/env python
"""
_mellin_moment_pin_provenance_audit.py — S89 W6-2
==================================================

AST-parse audit of f0/f2/f4 Mellin moment pin derivation provenance for
the producing script `computations/session-87/s82_w3_9_as_adjacent_obs.py`.

Per §VII.AN registry-anchor framing in
`sessions/permanent-results-registry.md`, the f0/f2/f4 Mellin moment
pins are declared as derived via Route-A "single-pole Mellin closure".
This audit parses the producing script's AST and matches its function
calls / imports / docstring keywords against ROUTE_A_SIGNATURES vs
ROUTE_B_SIGNATURES, classifies the actual derivation path, and reports
whether the declared registry route matches the actual implementation
route.

Calibration: K=4 NEGATIVE-CALIBRATION corpus instance W5a-44
(`audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b`)
per `substrate-first-canonical-sourcing.md §(i)` K=4 NEGATIVE-CALIBRATION
corpus.

Substrate framing
-----------------
The AST IS the methodology-layer F-image of the substrate-derivation
chain (Mellin closure path). The audit verifies F-image consistency
between producing-script body and registry-text declaration; both are
emergent under F from the same substrate-derivation chain.

CLI
---
    python _mellin_moment_pin_provenance_audit.py [--script PATH] [--json]
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import ast
import json
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
# Route signature sets (per plan §W6-2 §6)
# ---------------------------------------------------------------------------
ROUTE_A_SIGNATURES: dict[str, set[str]] = {  # (local) Mellin single-pole closure
    "function_calls": {
        "mellin_single_pole_closure",
        "compute_residue_at_s_eq_3",
        "single_pole_residue",
        "mellin_residue_s3",
    },
    "imports_required": {
        "analytic_zeta",
        "mellin_barnes_residue",
        "single_pole_closure",
    },
    "docstring_keywords": {
        "single-pole",
        "Mellin closure",
        "residue at s=3",
        "single-pole Mellin",
    },
}

ROUTE_B_SIGNATURES: dict[str, set[str]] = {  # (local) adjacent observable / alternate chain
    "function_calls": {
        "adjacent_observable_path",
        "compute_via_alternate_chain",
        "as_adjacent_obs",
        "adjacent_observable",
    },
    "imports_required": {
        "_spectral_action_regulators",
        "compute_aN_zeta",
        "spectral_action_regulators",
    },
    "docstring_keywords": {
        "adjacent observable",
        "alternate path",
        "Route-B",
        "as_adjacent_obs",
    },
}


def parse_script(script_path: Path) -> dict[str, Any]:
    """Parse a Python script and extract function calls, imports, docstrings.

    Returns {'calls': [...], 'imports': [...], 'docstrings': [...]}.
    Raises FileNotFoundError if script_path does not exist.
    """
    text = script_path.read_text(encoding="utf-8")
    tree = ast.parse(text)
    calls: list[str] = []  # local
    imports: list[str] = []  # local
    docstrings: list[str] = []  # local

    # Module-level docstring
    mod_doc = ast.get_docstring(tree)
    if mod_doc:
        docstrings.append(mod_doc)

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            doc = ast.get_docstring(node)
            if doc:
                docstrings.append(doc)
    return {
        "calls": calls,
        "imports": imports,
        "docstrings": docstrings,
        "n_calls": len(calls),
        "n_imports": len(imports),
        "n_docstrings": len(docstrings),
    }


def classify_route(parsed: dict[str, Any]) -> dict[str, Any]:
    """Score the parsed AST against ROUTE_A and ROUTE_B signatures and
    return classification.

    Per plan §6: a_score > 2 * b_score AND a_score >= 3 → Route-A;
    symmetric for Route-B. Otherwise AMBIGUOUS.
    """
    calls_set = set(parsed["calls"])  # local
    imports_set = set(parsed["imports"])  # local
    docstring_blob = "\n".join(parsed["docstrings"]).lower()  # local

    a_score = 0  # local
    a_score += len(calls_set & ROUTE_A_SIGNATURES["function_calls"])
    a_score += len(imports_set & ROUTE_A_SIGNATURES["imports_required"])
    for kw in ROUTE_A_SIGNATURES["docstring_keywords"]:
        if kw.lower() in docstring_blob:
            a_score += 1

    b_score = 0  # local
    b_score += len(calls_set & ROUTE_B_SIGNATURES["function_calls"])
    b_score += len(imports_set & ROUTE_B_SIGNATURES["imports_required"])
    for kw in ROUTE_B_SIGNATURES["docstring_keywords"]:
        if kw.lower() in docstring_blob:
            b_score += 1

    # Plan §6 thresholds: dominance ratio + absolute floor
    if a_score > 2 * b_score and a_score >= 3:
        classification = "Route-A"
    elif b_score > 2 * a_score and b_score >= 3:
        classification = "Route-B"
    else:
        classification = "AMBIGUOUS"
    return {
        "a_score": a_score,
        "b_score": b_score,
        "classification": classification,
        "threshold_rule": "a_score > 2*b_score AND a_score >= 3 → Route-A; "
                          "b_score > 2*a_score AND b_score >= 3 → Route-B; "
                          "else AMBIGUOUS",
    }


def audit_provenance(script_path: Path,
                     declared_route: str = "Route-A",
                     declared_in: str = "sessions/permanent-results-registry.md §VII.AN"
                     ) -> dict[str, Any]:
    """Run the full audit: parse + classify + compare against declared route.

    If script_path does not exist, return FAIL-with-diagnostic (NOT a crash).
    """
    if not script_path.exists():
        return {
            "gate": "S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT",
            "script_path": str(script_path),
            "script_exists": False,
            "declared_route": declared_route,
            "declared_in": declared_in,
            "actual_route": "SCRIPT-NOT-FOUND",
            "conflation_detected": True,
            "verdict": "FAIL",
            "severity": "MANDATORY",
            "rationale": (
                f"Producing script cited at registry-anchor framing "
                f"({declared_in}) does not exist on disk at {script_path}. "
                f"This is a registry-anchor dangling-reference: the §VII.AN "
                f"text cites a script the producing-side has not authored "
                f"(or has renamed/moved). AST-parse audit cannot complete; "
                f"the dangling-reference IS the audit's structural finding."
            ),
            "remediation": (
                "Route to mack-cosmic-bridge sole-writer (per "
                "feedback_mack-bridge-role.md) for §VII.AN registry-text "
                "reconciliation: either (a) restore the missing producing "
                "script at the cited path, or (b) update the §VII.AN "
                "anchor text to cite the actual current producing script."
            ),
        }

    try:
        parsed = parse_script(script_path)
    except SyntaxError as e:
        return {
            "gate": "S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT",
            "script_path": str(script_path),
            "script_exists": True,
            "parse_error": f"SyntaxError: {e}",
            "verdict": "FAIL",
            "severity": "MANDATORY",
            "rationale": "Producing script does not parse; AST audit aborted.",
        }

    classification = classify_route(parsed)
    actual_route = classification["classification"]
    conflation_detected = (declared_route != actual_route)
    verdict = "FAIL" if conflation_detected else "PASS"
    severity = "MANDATORY" if conflation_detected else "NO-ACTION"

    return {
        "gate": "S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT",
        "script_path": str(script_path),
        "script_exists": True,
        "declared_route": declared_route,
        "declared_in": declared_in,
        "actual_route": actual_route,
        "a_score": classification["a_score"],
        "b_score": classification["b_score"],
        "threshold_rule": classification["threshold_rule"],
        "conflation_detected": conflation_detected,
        "verdict": verdict,
        "severity": severity,
        "parsed_summary": {
            "n_calls": parsed["n_calls"],
            "n_imports": parsed["n_imports"],
            "n_docstrings": parsed["n_docstrings"],
        },
        "remediation": (
            "Route to mack-cosmic-bridge sole-writer (per "
            "feedback_mack-bridge-role.md) for §VII.AN registry-text "
            "reconciliation; declare actual Route-B path; cite Class-(g) "
            "REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION audit-script "
            "extension per A.22 sub-item (ii)."
        ) if conflation_detected else "No remediation required.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--script",
        default="computations/session-87/s82_w3_9_as_adjacent_obs.py",
        help="AST-parse target (default: §VII.AN cited closure script)")
    parser.add_argument(
        "--declared-route", default="Route-A",
        help="Registry-declared route (default: Route-A per §VII.AN)")
    parser.add_argument("--json", action="store_true",
                        help="JSON output (default: pretty JSON)")
    args = parser.parse_args()

    report = audit_provenance(Path(args.script), args.declared_route)
    print(json.dumps(report, indent=2))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
