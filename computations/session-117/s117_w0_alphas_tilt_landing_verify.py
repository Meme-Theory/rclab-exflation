#!/usr/bin/env python3
"""
S117 W0-2 CF-S117-HK-ALPHAS-TILT-LANDING — grep-verifier for the A_s-leg tilt sub-row
====================================================================================

Gate: CF-S117-HK-ALPHAS-TILT-LANDING ([AUDIT])

Pre-registered threshold (artifact-existence; no numerical comparison):
  PASS iff the `α_s(primordial) ~ 0` tilt sub-row is present on the A_s leg
  (Row #12) of sessions/framework/registry/falsifier-master-inventory.md
  carrying ALL required content markers:
    - header  Row #12.compute-S117-W0-ALPHAS-TILT-LANDING
    - anchor  S116-W1-AS-CFB1 + its audit_sha256 f44a7b42...b3ec
    - mechanism  "Mode-Independent Occupation"
    - content  "primordial"  (α_s(primordial))
    - 𝒩-fork INDEPENDENCE  ("𝒩-fork-INDEPENDENT" + "{+0.196, +0.864}")
    - single-observable-per-triple distinctness  (DISTINCT from Row #3)
  FAIL iff the sub-row or any required marker is absent.

Inputs (SHA-256 dual-pinned at runtime):
  - sessions/framework/registry/falsifier-master-inventory.md  (post-landing; greped)
  - this script's bytes
  - citation pin: anchor S116-W1-AS-CFB1 audit_sha256 (a pinmap entry, not a file)
  NOTE: this verifier imports NO canonical_constants.py — it is a pure
  artifact-existence grep of the falsifier inventory (no numerical compute),
  per session-117-plan-w0.md §W0-2 output_artifacts.script.must_contain note.

Dual-SHA schema (S84+):
  content_sha256 = sha256( landed sub-row block text )   # the deliverable diff
  audit_sha256   = sha256( script bytes || inventory bytes || pinmap_json )

Classification: PHONONIC
"""

from __future__ import annotations

import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
INVENTORY = (PROJECT_ROOT / "sessions" / "framework" / "registry"
             / "falsifier-master-inventory.md")

SESSION = "S117"                                                    # (local)
GATE_ID = "CF-S117-HK-ALPHAS-TILT-LANDING"                          # (local)
SCHEME = "FALSIFIER-INVENTORY-SUBROW-LANDING"                       # (local)
CONVENTION = "MODE-INDEPENDENT-OCCUPATION-TILT-FLAT"                # (local)
L_MAX = "N/A"                                                       # (local)

# The new sub-row's header anchor (the block we verify lives between this
# header and the next "### Row" header).
SUBROW_HEADER = "### Row #12.compute-S117-W0-ALPHAS-TILT-LANDING"   # (local)

# Anchor pin (citation; an input-pin-map entry, NOT a file read).
ANCHOR_GATE = "S116-W1-AS-CFB1"                                     # (local)
ANCHOR_SHA = ("f44a7b4279d4227db9a7b2c755238c9c2bd256b93c88f5"
              "bcf87ae78b8264b3ec")                                 # (local)

# Required content markers inside the sub-row block (pre-registered).
REQUIRED_MARKERS = [                                                # (local)
    ANCHOR_GATE,                       # anchor name
    ANCHOR_SHA,                        # anchor audit_sha256
    "Mode-Independent Occupation",     # mechanism
    "primordial",                      # α_s(primordial)
    "\U0001D4A9-fork-INDEPENDENT",     # 𝒩-fork-INDEPENDENT
    "{+0.196, +0.864}",                # the magnitude 𝒩-fork it is independent of
    "DISTINCT from Row #3",            # single-observable-per-triple distinctness
]


def sha256_of_bytes(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def sha256_of(path: Path) -> str:
    try:
        return sha256_of_bytes(path.read_bytes())
    except OSError:
        return ""


def extract_subrow_block(text: str, header: str) -> str:
    """Return the sub-row block from `header` up to (not incl.) the next
    '### Row' header, or '' if the header is absent."""
    idx = text.find(header)  # (local)
    if idx < 0:
        return ""
    rest = text[idx + len(header):]  # (local)
    nxt = rest.find("\n### Row")  # (local)
    if nxt < 0:
        return header + rest
    return header + rest[:nxt]


def print_verdict_payload(verdict: str, value, audit_sha: str,
                          content_sha: str) -> dict:
    """Print the delimited emit_verdict payload for the dispatching agent.
    The script does NOT write the verdict file (race-safe emit_verdict owns
    that single lock-serialized write)."""
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main() -> int:
    t0 = time.time()  # (local)

    # 1. Read the inventory + extract the landed sub-row block.
    inv_bytes = INVENTORY.read_bytes()  # (local)
    inv_text = inv_bytes.decode("utf-8")  # (local)
    block = extract_subrow_block(inv_text, SUBROW_HEADER)  # (local)

    # 2. Log input SHA-256 pins (first lines of stdout).
    script_path = Path(__file__).resolve()  # (local)
    script_bytes = script_path.read_bytes()  # (local)
    inv_rel = str(INVENTORY.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    script_rel = str(script_path.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    pins = {  # (local)
        script_rel: sha256_of_bytes(script_bytes),
        inv_rel: sha256_of_bytes(inv_bytes),
        f"anchor:{ANCHOR_GATE}": ANCHOR_SHA,
    }
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}...")

    # 3. Marker checks (artifact-existence; the gate rule).
    header_present = bool(block)  # (local)
    missing = [m for m in REQUIRED_MARKERS if m not in block]  # (local)
    all_markers = header_present and not missing  # (local)
    # Cross-check the anchor appears at least twice in the WHOLE inventory
    # (the citation must already be live, not introduced solely by this row).
    anchor_count = inv_text.count(ANCHOR_SHA)  # (local)
    anchor_live = anchor_count >= 2  # (local)

    print(f"  subrow_header_present: {header_present}")
    print(f"  required_markers_missing: {missing}")
    print(f"  anchor_sha_occurrences_in_inventory: {anchor_count} (live>=2: {anchor_live})")

    # 4. Dual SHAs.
    #    content_sha256 = sha256(landed sub-row block text)  [the deliverable]
    #    audit_sha256   = sha256(script || inventory || pinmap_json)
    content_sha = sha256_of_bytes(block.encode("utf-8"))  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(inv_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+inventory+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (landed sub-row block)")
    print()

    # 5. Verdict (artifact-existence).
    verdict = "PASS" if (all_markers and anchor_live) else "FAIL"  # (local)
    value = (f"alphas_primordial_tilt_subrow={'LANDED' if all_markers else 'MISSING'};"
             f"header={header_present};markers_missing={len(missing)};"
             f"anchor={ANCHOR_GATE};anchor_live={anchor_live};"
             f"mechanism=Mode-Independent-Occupation;"
             f"N-fork-INDEPENDENT={{+0.196,+0.864}};"
             f"single-obs-per-triple=distinct-from-Row#3-and-Row#93")  # (local)

    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # exit 0 = script healthy regardless of PASS/FAIL (gate-verdicts.md)


if __name__ == "__main__":
    sys.exit(main())
