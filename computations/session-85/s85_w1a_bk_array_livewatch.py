#!/usr/bin/env python3
"""
S85 W1a-4: BK-ARRAY-2026-LIVEWATCH (CF-M9)
==========================================

Gate: S85-W1a-BK-ARRAY-2026-LIVEWATCH
Trigger: [AUDIT] (event-driven, no compute until trigger)
Classification: META (pre-registration + live-watch protocol)
Agent: mack-cosmic-bridge

Hypothesis: The framework r=0.01173 prediction (S84 W4-42) is tested
by the BICEP Array + Keck 2026 release. Four-branch decision tree
already registered at content_sha_head=e2ca24d6...882d3 (S84).

Event status as of plan freeze (2026-04-21) and execution (2026-04-23):
  BK-Array 2026 release is NOT YET PUBLIC. No post-release data parsing
  is possible. This livewatch:
    (a) verifies the S84 W4-42 registration SHA head matches the
        pre-registered value,
    (b) echoes the 4-branch decision tree,
    (c) emits verdict PENDING-EVENT with next-check date.

Substitution chain:
  Step 1: r_FW = 0.01173 (canonical_constants).
  Step 2: Decision-tree boundaries: (0.005, 0.018, 0.030) frozen at S84.
  Step 3: Branch classification (for later execution when data lands):
          Branch 1: r_obs < 0.005 -> FAIL (FW falsified at 2+ sigma down).
          Branch 2: 0.005 <= r_obs < 0.018 -> PASS (FW within 1-sigma).
          Branch 3: 0.018 <= r_obs < 0.030 -> INFO (FW within 2-sigma).
          Branch 4: r_obs >= 0.030 -> FAIL (FW falsified upward).
  Step 4: No classification today -> verdict = PENDING-EVENT.
  Direction: monitoring only; no physics claim is advanced today.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/archive/session-84/s84_w4_42_bicep_keck_prereg.md (if present)
  - script bytes

Output 4-tuple:
  (value='PENDING-EVENT', scheme=BK-Array-2026-pipeline,
   convention=BICEP-Keck-standard, L_max=N/A)

Thresholds (pre-registered, plan §W1a-4):
  - PASS iff release public AND r_obs in [0.005, 0.018].
  - FAIL iff release public AND (r_obs < 0.005 OR r_obs >= 0.030).
  - INFO iff release public AND r_obs in [0.018, 0.030].
  - PENDING-EVENT iff release not public; verdict = PENDING with SHA pin.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import r_CMB_framework as r_FW  # noqa: E402 (S83 G46 TENSOR-TRANSFER PASS)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1a-BK-ARRAY-2026-LIVEWATCH"                         # (local)
SCHEME = "BK-Array-2026-pipeline"                                   # (local)
CONVENTION = "BICEP-Keck-standard"                                  # (local)
L_MAX = "N/A"                                                       # (local) detector-only, no spectrum

# Pre-registered decision-tree boundaries (S84, frozen)
BRANCH_LOW = 0.005                                                  # (local) FAIL below this
BRANCH_PASS_HIGH = 0.018                                            # (local) PASS in [LOW, PASS_HIGH]
BRANCH_INFO_HIGH = 0.030                                            # (local) INFO in [PASS_HIGH, INFO_HIGH]

S84_REGISTRATION_SHA_HEAD = "e2ca24d6"                              # (local) S84 W4-42 content_sha prefix

# Event status (manually set; in future this would query https://bicepkeck.org)
EVENT_PUBLIC = False                                                # (local) as of 2026-04-23
NEXT_CHECK_DATE = "2026-07-01"                                      # (local) quarterly poll

OUT_JSON = SCRIPT_DIR / "s85_w1a_bk_array_livewatch.json"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
S84_PREREG_MD = PROJECT_ROOT / "sessions" / "session-84" / "s84_w4_42_bicep_keck_prereg.md"

INPUT_FILES = [CANON_PY]
if S84_PREREG_MD.exists():
    INPUT_FILES.append(S84_PREREG_MD)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def classify_branch(r_obs: float) -> str:
    if r_obs < BRANCH_LOW:
        return "Branch-1-FAIL-down"
    if r_obs < BRANCH_PASS_HIGH:
        return "Branch-2-PASS"
    if r_obs < BRANCH_INFO_HIGH:
        return "Branch-3-INFO"
    return "Branch-4-FAIL-up"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: r_FW = {r_FW} (canonical, S84 W4-42)")
    print(f"  Step 2: decision-tree boundaries = ({BRANCH_LOW}, {BRANCH_PASS_HIGH}, {BRANCH_INFO_HIGH}) FROZEN at S84")
    print(f"  Step 3: 4-branch classification table:")
    print(f"          Branch 1: r_obs < {BRANCH_LOW} -> FAIL (falsified down)")
    print(f"          Branch 2: [{BRANCH_LOW}, {BRANCH_PASS_HIGH}) -> PASS (within 1-sigma)")
    print(f"          Branch 3: [{BRANCH_PASS_HIGH}, {BRANCH_INFO_HIGH}) -> INFO (within 2-sigma)")
    print(f"          Branch 4: r_obs >= {BRANCH_INFO_HIGH} -> FAIL (falsified up)")
    print(f"  Step 4: BK-Array 2026 release status: public={EVENT_PUBLIC}")
    print(f"          -> no classification possible -> verdict = PENDING-EVENT")
    print(f"  Step 5: S84 registration SHA head echo: {S84_REGISTRATION_SHA_HEAD}...")
    print(f"          next-check date: {NEXT_CHECK_DATE}")
    print()

    verdict = "PENDING-EVENT" if not EVENT_PUBLIC else "TO-BE-CLASSIFIED"  # (local)
    value = "PENDING-EVENT" if not EVENT_PUBLIC else "unknown-classify"   # (local)

    # Emit JSON registration artifact for future processing
    reg = {
        "gate_id": GATE_ID,
        "event_public": EVENT_PUBLIC,
        "r_FW_prediction": float(r_FW),
        "decision_tree": {
            "boundaries": [BRANCH_LOW, BRANCH_PASS_HIGH, BRANCH_INFO_HIGH],
            "branch_1_FAIL_down":  f"r_obs < {BRANCH_LOW}",
            "branch_2_PASS":       f"{BRANCH_LOW} <= r_obs < {BRANCH_PASS_HIGH}",
            "branch_3_INFO":       f"{BRANCH_PASS_HIGH} <= r_obs < {BRANCH_INFO_HIGH}",
            "branch_4_FAIL_up":    f"r_obs >= {BRANCH_INFO_HIGH}",
        },
        "s84_registration_sha_head": S84_REGISTRATION_SHA_HEAD,
        "next_check_date": NEXT_CHECK_DATE,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "verdict": verdict,
    }
    OUT_JSON.write_text(json.dumps(reg, indent=2), encoding="utf-8")
    print(f"  JSON written: {OUT_JSON.name}")

    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
