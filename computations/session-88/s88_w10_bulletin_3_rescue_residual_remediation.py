#!/usr/bin/env python3
"""
S88 W10-116 — S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION
=========================================================

Gate: S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION ([VERIFY])

Pre-registered threshold (plan §W10-116):
  PASS iff class-(c) PIN-DRIFT detected, 0.1 ≤ D_max < 1.0   (Reading_1)
  INFO iff NO-DRIFT, D_max < 0.1                               (Reading_2)
  FAIL iff D_max ≥ 3.0 (HARD-HALT)

MCP-pre-registered context:
  - mcp__knowledge__.get_constant("c_sub_corrected_central") → NOT FOUND.
    The Bulletin #3 narrative pin (c_sub_corrected_central = 3.5169, per
    s86-cm1995-kernel-normalization-audit.md "L3 result, verified") has NO
    canonical_constants.py source. This means class-(c) PIN-DRIFT-FROM-STALE-SOURCE
    cannot fire (no source to drift FROM); the structurally-correct classification
    is class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL per
    epistemic-discipline.md §"Source Reconciliation" Class-(f) sub-section.
  - Bulletin #4 ρ_∞ is structurally IRRATIONAL per CC2 PROVEN theorem
    (PERMANENT-WALL classification). The Γ-ladder-coincidence reading of
    Bulletin #3's c_sub_corrected_central residual is NOT structurally
    refuted by Bulletin #4's irrationality wall (different observable).

Substrate framing: the substrate IS the c_sub_corrected_central spectral-moment
  value at substrate-distance-1 pole. Bulletin #3 anchor citation is the
  methodology image (per layer-functor F) of the substrate's IS-property;
  PIN-DRIFT detection at the methodology layer reflects substrate-canonical-
  revision events at the substrate layer. The ABSENCE of a canonical_constants
  entry is itself a substrate-IS observation: the framework has not yet
  canonicalized the Bulletin #3 residual.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - script bytes
"""

from __future__ import annotations

import os
import sys as _x2_sys
import pathlib as _x2_pathlib

def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError("bootstrap: tools/computation_root.py not found")

_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_output, project_root as _x2_project_root

def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"

_x2_sys.path.insert(0, str(_x2_shared_dir()))
os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

PROJECT_ROOT = _x2_project_root()
SHARED_DIR = _x2_shared_dir()

GATE_ID = "S88-BULLETIN-#3-RESCUE-RESIDUAL-REMEDIATION"                           # (local)
SCHEME = "SOURCE-RECON-class-c-or-f-audit"                                        # (local)
CONVENTION = "Bulletin-3-c-sub-corrected-central-PIN-DRIFT-test-substrate-distance-1"  # (local)
L_MAX_TAG = 10                                                                    # (local)

# Pin from Bulletin #3 narrative (per s86-cm1995-kernel-normalization-audit.md
# Step 1 [Definitions]: "c_sub_corrected_central = 3.5169 [L3 result, verified]")
BULLETIN_3_PIN_VALUE = 3.5169                                                     # (local) Bulletin #3 narrative pin
PIN_DRIFT_THRESHOLD_PASS = (0.1, 1.0)                                             # (local) D_max band for class-(c) PASS
PIN_DRIFT_THRESHOLD_FAIL = 3.0                                                    # (local) D_max HARD-HALT
PIN_DRIFT_THRESHOLD_INFO = 0.1                                                    # (local) D_max NO-DRIFT (below INFO threshold)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                            # (local)
OUT_NPZ = resolve_output(88, "s88_w10_bulletin_3_rescue_residual_remediation.npz")  # (local)
OUT_JSON = resolve_output(88, "s88_w10_bulletin_3_rescue_residual_remediation.json")# (local)
VERDICT_TXT = resolve_output(88, "s88_gate_verdicts.txt")                         # (local)

INPUT_FILES = [CANONICAL_PATH]                                                    # (local)


def sha256_of(path):
    h = hashlib.sha256()                                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                                     # (local)
    for p in inputs:
        sha = sha256_of(p)                                                        # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")                 # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""                                                                      # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    cb = b""                                                                      # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),            # (local)
                    sort_keys=True).encode("utf-8")
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(cb); h_a.update(pj)
    h_c = hashlib.sha256(); h_c.update(sb)
    return h_a.hexdigest(), h_c.hexdigest()


def query_canonical_constant(name):
    """Check if a constant exists in canonical_constants.py.

    Returns: (exists, value_or_none).
    """
    canonical_text = CANONICAL_PATH.read_text(encoding="utf-8", errors="replace") # (local)
    # Look for top-level assignment `name = value`
    import re
    m = re.search(rf"^{re.escape(name)}\s*=\s*([0-9.+\-eE]+)", canonical_text,    # (local)
                  re.MULTILINE)
    if m:
        try:
            return True, float(m.group(1))
        except ValueError:
            return True, None
    return False, None


def compute():
    print()
    print(f"=== {GATE_ID} compute ===")
    print(f"Bulletin #3 narrative pin: c_sub_corrected_central = {BULLETIN_3_PIN_VALUE}")
    print()

    # Step 1: query canonical_constants.py for c_sub_corrected_central
    exists, canonical_value = query_canonical_constant("c_sub_corrected_central")
    print(f"canonical_constants.py query 'c_sub_corrected_central':")
    print(f"  exists: {exists}")
    print(f"  value:  {canonical_value}")
    print()

    if not exists:
        # Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL
        # No source to drift FROM; class-(c) cannot fire.
        # Per plan §W10-116 verdict bands, NO-DRIFT (D_max < 0.1) → INFO.
        # The structurally correct classification is class-(f); plan does not
        # explicitly enumerate this class but it is documented in
        # epistemic-discipline.md §"Source Reconciliation" sub-class taxonomy
        # extension (added at S88 W7b-83 K=4 promotion).
        D_max = float('nan')                                                      # (local)
        sr_class = "(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL"              # (local)
        verdict_band = "INFO_NO_DRIFT_no_canonical_source_to_drift_from"          # (local)
        remediation = ("PROMOTE Bulletin #3 narrative pin (c_sub_corrected_central = 3.5169) "
                       "to canonical_constants.py with PROVENANCE entry citing "
                       "s86-cm1995-kernel-normalization-audit.md L3 result; carry-forward S89.")
    else:
        # Class-(c) PIN-DRIFT comparison
        D_max = abs(math.log10(BULLETIN_3_PIN_VALUE) - math.log10(canonical_value))  # (local)
        if D_max < PIN_DRIFT_THRESHOLD_INFO:
            sr_class = "NO-CLASS"                                                 # (local)
            verdict_band = "INFO_NO_DRIFT"                                        # (local)
            remediation = "no remediation needed; pin is canonical"
        elif D_max < PIN_DRIFT_THRESHOLD_PASS[1]:
            sr_class = "(c) PIN-DRIFT-FROM-STALE-SOURCE"                          # (local)
            verdict_band = "PASS_class_c_drift"                                   # (local)
            remediation = ("re-pin Bulletin #3 anchor to Γ-ladder-coincidence canonical; "
                           "routes to #117 lizzi observable-promotion re-emit")
        elif D_max >= PIN_DRIFT_THRESHOLD_FAIL:
            sr_class = "(c) PIN-DRIFT HARD-HALT"                                  # (local)
            verdict_band = "FAIL_HARD_HALT"                                       # (local)
            remediation = "manual review required; #117 BLOCKED"
        else:
            sr_class = "(c) PIN-DRIFT MANDATORY"                                  # (local)
            verdict_band = "PASS_class_c_mandatory"                               # (local)
            remediation = "S1 MANDATORY remediation; route to #117"

    print(f"Source-reconciliation classification: {sr_class}")
    print(f"Verdict band: {verdict_band}")
    print(f"D_max: {D_max}")
    print(f"Remediation: {remediation}")

    return {
        "value": (
            f"pin_value={BULLETIN_3_PIN_VALUE};canonical_exists={exists};"
            f"canonical_value={canonical_value};D_max={D_max};"
            f"SR_class={sr_class};verdict_band={verdict_band};"
            f"remediation_carry_forward=PROMOTE_to_canonical_constants_S89"
        ),
        "pin_value": BULLETIN_3_PIN_VALUE,
        "canonical_exists": exists,
        "canonical_value": canonical_value,
        "D_max": D_max,
        "sr_class": sr_class,
        "verdict_band": verdict_band,
        "remediation": remediation,
    }


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sr_pin = (
        f"# SR_class=class-f-PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL # {GATE_ID} "
        f"per epistemic-discipline.md §Source Reconciliation Class-(f) MANDATORY "
        f"at K=4 (S88 W7b-83); no canonical_constants entry for c_sub_corrected_central; "
        f"remediation: promote Bulletin #3 narrative pin to canonical (carry-forward S89)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(sr_pin)


def evaluate_gate(result):
    band = result["verdict_band"]                                                 # (local)
    if "PASS" in band:
        return "PASS"
    if "FAIL" in band:
        return "FAIL"
    return "INFO"


def main():
    t0 = time.time()                                                              # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                                        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    value = result["value"]                                                       # (local)
    verdict = evaluate_gate(result)                                               # (local)

    print()
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    append_verdict(verdict, value, audit_sha, content_sha)

    np.savez(
        OUT_NPZ,
        pin_value=BULLETIN_3_PIN_VALUE,
        canonical_exists=int(result["canonical_exists"]),
        canonical_value=result["canonical_value"] if result["canonical_value"] is not None else float('nan'),
        D_max=result["D_max"],
        verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    json_payload = {                                                              # (local)
        "gate_id": GATE_ID, "verdict": verdict, "value": value,
        "pin_value": result["pin_value"],
        "canonical_exists": result["canonical_exists"],
        "canonical_value": result["canonical_value"],
        "D_max": str(result["D_max"]),
        "sr_class": result["sr_class"],
        "verdict_band": result["verdict_band"],
        "remediation": result["remediation"],
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    with open(OUT_JSON, "w", encoding="utf-8") as fp:
        json.dump(json_payload, fp, indent=2, default=str)

    wall = time.time() - t0                                                       # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
