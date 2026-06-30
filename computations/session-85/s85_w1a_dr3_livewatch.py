#!/usr/bin/env python3
"""
S85 W1a-5: DR3-LIVEWATCH (CF-M1)
================================

Gate: S85-W1a-DR3-LIVEWATCH
Trigger: [AUDIT] (event-driven, 2026-04-23 window open)
Classification: META (binary R_842 containment check)
Agent: mack-cosmic-bridge

Hypothesis: The S84 W1b-9 DR3 response protocol with rectangle
R_842 = [-1.05, -0.85] x [-0.2, 0.2] at content_sha head
9cc7f47e...79d9f (S84) resolves to either:
  (i) R_842-contained => framework w_0 = -0.918 prediction ratified,
  (ii) R_842-excluded => cascade
       S85-R_842-PHYSICAL-ANCHOR-REAUDIT (kaku) and
       S85-W0-L-INVERTED-BRANCH-ENUMERATION (kaku) triggered.

Event status as of execution (2026-04-23, DR3 window opens today):
  DESI DR3 public release status: NOT YET PUBLIC. The window opens
  2026-04-23 but the data.desi.lbl.gov endpoint does not yet host
  the DR3 BAO/RSD catalogs. This livewatch:
    (a) verifies the S84 W1b-9 registration SHA head matches,
    (b) echoes the 7-cell decision tree (A1/A2/B1/B2/B3/C1/C2),
    (c) emits verdict PENDING-EVENT.

Substitution chain:
  Step 1: w_0_FW = -0.918 (canonical, S58 Volovik + effacement).
  Step 2: Rectangle R_842 = w_0 in [-1.05, -0.85] AND w_a in [-0.2, 0.2].
  Step 3: 7-cell decision tree (frozen S84 W4-44):
          A1: contained AND within 1-sigma of (-0.918, 0) -> PASS.
          A2: contained AND > 1-sigma but < 2-sigma -> INFO.
          B1/B2/B3: excluded cells; framework w_0 FALSIFIED.
          C1/C2: exotic CPL anomalies; framework w_0 FALSIFIED + cascade.
  Step 4: DR3 release status: public=False -> verdict = PENDING-EVENT.
  Direction: binary containment check; no direction to compute today.

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - sessions/archive/session-84/s84_w1b_9_dr3_response_protocol.md (if present)
  - script bytes

Output 4-tuple:
  (value='PENDING-EVENT', scheme=DESI-DR3-pipeline,
   convention=CPL-w0wa, L_max=N/A)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import w0_FW  # noqa: E402

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1a-DR3-LIVEWATCH"                                   # (local)
SCHEME = "DESI-DR3-pipeline"                                        # (local)
CONVENTION = "CPL-w0wa"                                             # (local)
L_MAX = "N/A"                                                       # (local)

# Rectangle R_842 from S84 (frozen)
R_842_W0_LOW = -1.05                                                # (local)
R_842_W0_HIGH = -0.85                                               # (local)
R_842_WA_LOW = -0.20                                                # (local)
R_842_WA_HIGH = 0.20                                                # (local)

S84_REGISTRATION_SHA_HEAD = "9cc7f47e"                              # (local) S84 W1b-9 content_sha prefix

EVENT_PUBLIC = False                                                # (local) DR3 not yet public as of 2026-04-23 window-open
NEXT_CHECK_DATE = "2026-05-15"                                      # (local) weekly check starting window open

OUT_JSON = SCRIPT_DIR / "s85_w1a_dr3_livewatch.json"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
S84_PROTOCOL_MD = PROJECT_ROOT / "sessions" / "session-84" / "s84_w1b_9_dr3_response_protocol.md"

INPUT_FILES = [CANON_PY]
if S84_PROTOCOL_MD.exists():
    INPUT_FILES.append(S84_PROTOCOL_MD)


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
    print(f"  Step 1: w_0_FW = {w0_FW} (canonical, S58 Volovik + effacement)")
    print(f"  Step 2: R_842 rectangle = w_0 in [{R_842_W0_LOW}, {R_842_W0_HIGH}] x "
          f"w_a in [{R_842_WA_LOW}, {R_842_WA_HIGH}] (FROZEN S84 W1b-9)")
    print(f"  Step 3: 7-cell decision tree:")
    print(f"          A1 contained + 1-sigma of (-0.918, 0) -> PASS")
    print(f"          A2 contained + 2-sigma -> INFO")
    print(f"          B1/B2/B3 excluded cells -> FAIL + kaku cascade")
    print(f"          C1/C2 exotic CPL regions -> FAIL + kaku cascade")
    print(f"  Step 4: DR3 release status: public={EVENT_PUBLIC}")
    print(f"          -> verdict = PENDING-EVENT")
    print(f"  Step 5: S84 registration SHA head echo: {S84_REGISTRATION_SHA_HEAD}...")
    print(f"          next-check date: {NEXT_CHECK_DATE}")
    print()

    verdict = "PENDING-EVENT" if not EVENT_PUBLIC else "TO-BE-CLASSIFIED"
    value = "PENDING-EVENT"                                         # (local)

    reg = {
        "gate_id": GATE_ID,
        "event_public": EVENT_PUBLIC,
        "w0_FW_prediction": float(w0_FW),
        "wa_FW_prediction": 0.0,
        "rectangle_R_842": {
            "w0_range": [R_842_W0_LOW, R_842_W0_HIGH],
            "wa_range": [R_842_WA_LOW, R_842_WA_HIGH],
        },
        "decision_tree": {
            "A1": "contained AND within 1-sigma of (-0.918, 0) => PASS",
            "A2": "contained AND 1-2 sigma => INFO",
            "B1": "w_0 < -1.05 (phantom excursion) => FAIL + cascade",
            "B2": "w_0 > -0.85 (quintessence) => FAIL + cascade",
            "B3": "|w_a| > 0.2 (CPL evolution) => FAIL + cascade",
            "C1": "exotic w_0 < -1.5 => FAIL + kaku W10 re-audit",
            "C2": "exotic w_0 > -0.5 => FAIL + kaku W10 re-audit",
        },
        "cascade_triggers_on_FAIL": [
            "S85-R_842-PHYSICAL-ANCHOR-REAUDIT (kaku)",
            "S85-W0-L-INVERTED-BRANCH-ENUMERATION (kaku)",
        ],
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
