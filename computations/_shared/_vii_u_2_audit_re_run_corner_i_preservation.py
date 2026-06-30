#!/usr/bin/env python
"""
_vii_u_2_audit_re_run_corner_i_preservation.py — S89 W6-6 (A.34)
=================================================================

Re-runs `_corner_classification_audit.py` post-V.1+V.3 W-21 edits
and verifies that §VII.U.2 Corner-I classification is preserved
against the pre-V.1+V.3 baseline `algebra-INVARIANT-spectrum-only-functional`.

Wrapper structure (matches plan §W6-6 §6 method)
-------------------------------------------------
1. Import `_corner_classification_audit` directly (the existing audit
   does not expose a `--verdict-format=json` CLI flag; the audit's
   self-test mode writes JSON to `computations/_tmp/`. We invoke it
   programmatically via the public callable to capture per-slot
   results in-memory).

2. ALSO scan `sessions/permanent-results-registry.md` for §VII.U.2
   block directly (since the existing audit's target list does NOT
   include §VII.U.2 — it audits §VII.U.1, §VII.U.6, §VII.AC.1/4,
   §VII.W, §VII.AF.1, §VII.AJ instead). The §VII.U.2 corner-
   classification preservation is a TEXT-LEVEL verification.

3. Combined verdict: PASS iff §VII.U.2 block contains Corner-I
   markers (`algebra-INVARIANT` and/or `Corner I`) AND the existing
   audit's pre-V.1+V.3-comparable slots (§VII.U.1, §VII.U.6) still
   classify as Corner-I.

Substrate framing
-----------------
The audit IS the methodology-layer F-image of the substrate-physics
algebra-axis orthogonality 4-corner partition (`cross-pillar-bridge-
anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3).
Corner-I = algebra-INVARIANT spectrum-only-functional class.
Preservation under V.1+V.3 W-21 registry-text edits is the structural
predicate this audit verifies.

CLI
---
    python _vii_u_2_audit_re_run_corner_i_preservation.py [--registry PATH] [--json]
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:
    print("ERROR: canonical_constants.py import failed", file=sys.stderr)
    raise


PRE_V1_V3_BASELINE_CORNER_I = "algebra-INVARIANT-spectrum-only-functional"  # (local) per plan §7


def _extract_vii_u_2_block(registry_text: str) -> str | None:
    """Extract the §VII.U.2 block from registry text (up to next §VII.X heading)."""
    pat = (
        r"§VII\.U\.2\b.*?"
        r"(?=§VII\.[A-Z][A-Z0-9.]*\b|\Z)"
    )
    match = re.search(pat, registry_text, re.DOTALL)
    return match.group(0) if match else None


def vii_u_2_corner_i_text_audit(registry_path: Path) -> dict[str, Any]:
    """
    Direct text-level audit: scan §VII.U.2 block for Corner-I /
    algebra-INVARIANT markers.
    """
    if not registry_path.exists():
        return {"verdict": "INFO", "reason": f"Registry not found at {registry_path}"}
    text = registry_path.read_text(encoding="utf-8")
    block = _extract_vii_u_2_block(text)
    if block is None:
        return {
            "verdict": "INFO",
            "reason": "§VII.U.2 block not located in registry",
            "registry_path": str(registry_path),
        }
    has_corner_I = bool(re.search(r"\bCorner[\s\-]?I\b|\bcell\s*I\b|\bcorner_I\b",
                                  block, re.IGNORECASE))
    has_algebra_invariant = bool(re.search(
        r"\balgebra[\- ]INVARIANT\b", block, re.IGNORECASE))
    has_spectrum_only_functional = bool(re.search(
        r"\bspectrum[\- ]only[\- ]functional\b", block, re.IGNORECASE))
    has_baseline_phrase = bool(re.search(
        re.escape(PRE_V1_V3_BASELINE_CORNER_I), block))
    preserved = (
        has_algebra_invariant
        and (has_corner_I or has_spectrum_only_functional or has_baseline_phrase)
    )
    return {
        "registry_path": str(registry_path),
        "block_found": True,
        "block_head": block[:300],
        "has_corner_I": has_corner_I,
        "has_algebra_invariant": has_algebra_invariant,
        "has_spectrum_only_functional": has_spectrum_only_functional,
        "has_baseline_phrase": has_baseline_phrase,
        "preserved_at_text_level": preserved,
        "verdict": "PASS" if preserved else "FAIL",
    }


def existing_audit_subprocess() -> dict[str, Any]:
    """
    Invoke the existing `_corner_classification_audit.py` via subprocess
    self-test mode and parse the latest JSON output. The existing audit
    audits 7 slots NOT including §VII.U.2; we use it to cross-check that
    §VII.U.1 and §VII.U.6 still classify as Corner-I (they share the
    §VII.U.* family with §VII.U.2; if their corner classification
    flipped, that would suggest the W-21 V.1+V.3 edits affected the
    family more broadly).
    """
    venv_python = Path(
        "phonon-exflation-sim/.venv312/Scripts/python.exe"
    ).resolve()
    audit_script = Path(
        "computations/_shared/_corner_classification_audit.py"
    ).resolve()
    if not audit_script.exists():
        return {"verdict": "INFO", "reason": "audit script not found"}
    try:
        result = subprocess.run(
            [str(venv_python), str(audit_script)],
            capture_output=True, text=True, check=False, timeout=120)
    except Exception as e:
        return {"verdict": "INFO", "reason": f"subprocess invocation failed: {e}"}

    # Parse the latest JSON output written by the audit
    tmp_dir = Path("computations/_tmp")
    json_files = sorted(
        tmp_dir.glob("corner_classification_audit_*.json"), reverse=True)
    if not json_files:
        return {
            "verdict": "INFO",
            "reason": "no audit JSON output found",
            "stdout_tail": result.stdout[-500:] if result.returncode != 0 else "",
        }
    latest = json_files[0]
    try:
        audit_data = json.loads(latest.read_text(encoding="utf-8"))
    except Exception as e:
        return {"verdict": "INFO", "reason": f"could not parse audit JSON: {e}"}

    # Extract per-slot results for §VII.U.* family
    psr = audit_data.get("per_slot_results", [])
    vii_u_slots = [
        r for r in psr if isinstance(r, dict)
        and r.get("slot", "").startswith("§VII.U.")
    ]
    all_corner_i = all(
        r.get("corner") == "I" and r.get("algebra_axis") == "INVARIANT"
        for r in vii_u_slots
    ) if vii_u_slots else False
    return {
        "audit_json_path": str(latest),
        "registry_sha256": audit_data.get("registry_sha256"),
        "n_slots_checked": audit_data.get("n_slots_checked"),
        "vii_u_family_slots": vii_u_slots,
        "all_vii_u_slots_corner_I": all_corner_i,
        "verdict": "PASS" if all_corner_i else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--registry",
        default="sessions/permanent-results-registry.md",
        help="Permanent-results-registry path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    registry_path = Path(args.registry)
    text_audit = vii_u_2_corner_i_text_audit(registry_path)
    sub_audit = existing_audit_subprocess()

    # Combined verdict: PASS iff text-level Corner-I preservation AND
    # existing-audit §VII.U.* family all classify as Corner-I
    text_pass = text_audit.get("verdict") == "PASS"
    sub_pass = sub_audit.get("verdict") == "PASS"
    combined = text_pass and sub_pass
    verdict = "PASS" if combined else (
        "FAIL" if (text_pass is False or sub_pass is False) else "INFO")

    report = {
        "gate": "S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION",
        "pre_v1_v3_baseline_corner_i": PRE_V1_V3_BASELINE_CORNER_I,
        "text_level_audit": text_audit,
        "existing_audit_subprocess": sub_audit,
        "combined_verdict": verdict,
        "rationale": (
            "PASS: §VII.U.2 block contains Corner-I/algebra-INVARIANT "
            "markers AND existing _corner_classification_audit.py "
            "§VII.U.* family slots all classify as Corner-I."
            if verdict == "PASS"
            else (
                "FAIL: §VII.U.2 Corner-I preservation NOT verified "
                "(either §VII.U.2 text lacks Corner-I markers OR existing "
                "audit's §VII.U.* family classification has drifted). "
                "Route to mack-cosmic-bridge sole-writer for §VII.U.2 "
                "registry-text reconciliation; revert V.1 or V.3 edits "
                "and re-derive corner classification."
                if verdict == "FAIL"
                else "INFO: prerequisites missing; cannot verify."
            )
        ),
    }
    print(json.dumps(report, indent=2))
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
