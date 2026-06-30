#!/usr/bin/env python
"""
_v4_anchor_structure_audit.py — S89 W6-3 sub-item (iv)
=======================================================

V_4 program parallel-compute-wave + §VII.AE vs §VII.AD anchor-structure
audit.

Per S88 W-7 V.6/V.7 (V_4-on-triality cocycle functor calibration corpus
instance #2 of `phononic-framing.md §"Single-τ-slice vs moduli-deformation
substrate-IS levels"` K-counter), the §VII.AE entry (Level-2
moduli-deformation substrate-IS) and §VII.AD entry (Level-1 single-τ-slice
substrate-IS) MUST declare which substrate-IS level their observable lives
at, AND the cocycle functor `F : m(p,q) ↦ Δ_0(m)` must be cited for the
V_4-triality multi-orbit deformation that lifts Level-1 to Level-2.

Detection
---------
The audit reads `sessions/permanent-results-registry.md`, extracts the
§VII.AE and §VII.AD blocks, and verifies that:

    (a) §VII.AE block declares Level-2 OR moduli-deformation;
    (b) §VII.AD block declares Level-1 OR single-τ-slice;
    (c) the registry text cites the cocycle functor F : m(p,q) → Δ_0.

PASS iff all 3 declarations present; FAIL otherwise.

Substrate framing
-----------------
The audit IS the methodology-layer F-image of the substrate-physics
Single-τ-slice ↔ moduli-deformation Level-1 ↔ Level-2 distinction.
Container thinking inversion: the moduli-space of τ-deformations IS
substrate-IS at Level-2 (NOT a coordinate on a meta-container).

CLI
---
    python _v4_anchor_structure_audit.py [--registry PATH] [--json]
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


AE_LEVEL_2_PATTERN = (  # (local) Level-2 moduli-deformation marker
    r"(?:Level\s*[\-]?\s*2|moduli[\- ]deformation)"
)
AD_LEVEL_1_PATTERN = (  # (local) Level-1 single-τ-slice marker
    r"(?:Level\s*[\-]?\s*1|single[\- ]τ[\- ]slice|single[\- ]tau[\- ]slice)"
)
COCYCLE_FUNCTOR_PATTERN = (  # (local) F : m(p,q) → Δ_0 citation
    r"cocycle\s+functor\s+F\s*:\s*m\(p\s*,\s*q\)\s*[→↦\-]+\s*Δ?_?0?"
)


def _extract_block(registry_text: str, slot_label: str) -> str | None:
    """Extract the §VII.<slot> block up to the next §VII.<other> heading."""
    pat = (
        rf"§VII\.{re.escape(slot_label)}\b.*?"
        rf"(?=§VII\.[A-Z][A-Z0-9]*\b|\Z)"
    )
    match = re.search(pat, registry_text, re.DOTALL)
    return match.group(0) if match else None


def v4_anchor_structure_audit(registry_text: str) -> dict[str, Any]:
    """
    Per S88 W-7 V.6/V.7: §VII.AE Level-2 + §VII.AD Level-1 + cocycle
    functor F : m(p,q) → Δ_0 must all be declared in registry text.

    Returns audit dict with per-block findings + verdict.
    """
    ae_block = _extract_block(registry_text, "AE")
    ad_block = _extract_block(registry_text, "AD")

    if ae_block is None and ad_block is None:
        return {
            "verdict": "INFO",
            "reason": "Both §VII.AE and §VII.AD blocks absent; rule "
                      "K-counter advancement not blocked but anchor-structure "
                      "discipline cannot be verified.",
            "ae_block_present": False,
            "ad_block_present": False,
        }

    ae_has_level_2 = bool(ae_block and re.search(
        AE_LEVEL_2_PATTERN, ae_block, re.IGNORECASE))
    ad_has_level_1 = bool(ad_block and re.search(
        AD_LEVEL_1_PATTERN, ad_block, re.IGNORECASE))
    cocycle_functor_cited = bool(re.search(
        COCYCLE_FUNCTOR_PATTERN, registry_text, re.IGNORECASE))

    all_three_present = (
        ae_has_level_2 and ad_has_level_1 and cocycle_functor_cited
    )
    verdict = "PASS" if all_three_present else "FAIL"
    severity = "NO-ACTION" if all_three_present else "MANDATORY"

    return {
        "ae_block_present": ae_block is not None,
        "ad_block_present": ad_block is not None,
        "ae_level_2_declared": ae_has_level_2,
        "ad_level_1_declared": ad_has_level_1,
        "cocycle_functor_cited": cocycle_functor_cited,
        "all_three_present": all_three_present,
        "verdict": verdict,
        "severity": severity,
        "rule_source": "phononic-framing.md §\"Single-τ-slice vs moduli-deformation substrate-IS levels\"",
        "calibration_source": "S88 W-7 V.6/V.7 (V_4-on-triality cocycle functor; K-counter instance #2)",
        "remediation": (
            "Add Level-2 declaration to §VII.AE block AND/OR Level-1 "
            "declaration to §VII.AD block AND/OR cite the cocycle "
            "functor F : m(p,q) → Δ_0 in registry text. Route to "
            "mack-cosmic-bridge sole-writer for §VII.AE/§VII.AD "
            "registry-text reconciliation."
        ) if not all_three_present else "No remediation required.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        default="sessions/permanent-results-registry.md",
        help="Permanent-results-registry markdown path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    p = Path(args.registry)
    if not p.exists():
        print(json.dumps({
            "verdict": "INFO",
            "reason": f"Registry file not found at {args.registry}; "
                      "audit cannot proceed.",
        }, indent=2))
        return 0

    text = p.read_text(encoding="utf-8")
    report = v4_anchor_structure_audit(text)
    print(json.dumps(report, indent=2))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
