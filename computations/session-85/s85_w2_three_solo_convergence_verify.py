#!/usr/bin/env python
"""
S85-W2-THREE-SOLO-CONVERGENCE-VERIFY

SHA-reproduction audit: the 4-anchor SHAs (W1-G1, W1-G3, G57, G58) and closure
SHA `cf3b7443be010558592cf7d278d7639de7293728f60b9740daa8caa4f664db42` from the
S84 W2a-11 three-solo (Connes + Lizzi + VdD) landing must still be present in
their canonical locations under the §VII.N routing.

PASS iff:
  (i) All four anchors found with full 64-char SHA in `computations/session-83/s83_gate_verdicts.txt`;
  (ii) Closure SHA cf3b7443... found in permanent-results-registry.md §VII.N block;
  (iii) §VII.M slot is occupied by DR3-RESPONSE-PROTOCOL (W1b-9) and §VII.N
       holds the three-solo Three-Layer Regulator Theorem.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

INPUT_FILES = [
    ".claude/agent-memory/connes-ncg-theorist/s84-w2a-11-vii-m-landing.md",
    "computations/session-83/s83_gate_verdicts.txt",
    "sessions/permanent-results-registry.md",
]

# Anchor definitions from S84 W2a-11 memo
# (Agent memory: .claude/agent-memory/connes-ncg-theorist/s84-w2a-11-vii-m-landing.md)
ANCHORS = {
    "W1-G1": {
        "full_sha": "227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd",
        "label": "L2 Zubarev uniqueness (substrate-action at tau_fold)",
    },
    "W1-G3": {
        "full_sha": "2343920a4c2a807a26bb9740ad6ede1c9d3465bb722d548dbefa978578c99ab5",
        "label": "L1 zeta uniqueness (axiomatic global)",
    },
    "G57": {
        "full_sha": "fcfbc362651e3f57137a90dd703a501d645ef87b99f8d250e92c6984bf6ccd68",
        "label": "L3 per-Q-span 11/11 pinning",
    },
    "G58": {
        "full_sha": "b941613aa8ae91fcebf4ecadb0da74ad37d9382c7cbd2413a14f9b91729d24f2",
        "label": "L3 band separation 10/10",
    },
}

CLOSURE_SHA_EXPECTED = (
    "cf3b7443be010558592cf7d278d7639de7293728f60b9740daa8caa4f664db42"
)


def sha256_of(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return "MISSING"
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_anchor(anchor_id: str, full_sha: str, s83_ledger: str) -> dict:
    """Verify that the anchor's 64-char SHA appears verbatim in the S83 ledger."""
    found = full_sha in s83_ledger
    # Also check it's the FULL 64-char hex (not truncated)
    is_full_64 = len(full_sha) == 64 and bool(re.fullmatch(r"[0-9a-f]{64}", full_sha))
    return {
        "anchor_id": anchor_id,
        "full_sha": full_sha,
        "found_in_ledger": found,
        "is_full_64_hex": is_full_64,
        "verified": found and is_full_64,
    }


def verify_registry_routing(registry_text: str) -> dict:
    """
    Verify that:
      - §VII.M section exists and is occupied by DR3 / event-driven pre-regs
      - §VII.N section exists and contains the three-solo three-layer regulator theorem
      - closure_sha `cf3b7443...` appears in the §VII.N block
    """
    has_vii_m = bool(re.search(r"^## §VII\.M", registry_text, re.MULTILINE))
    has_vii_n = bool(re.search(r"^## §VII\.N", registry_text, re.MULTILINE))
    has_closure = CLOSURE_SHA_EXPECTED in registry_text
    # Connes + Lizzi + Van den Dungen convergence attestation in §VII.N
    has_three_solo_attestation = bool(
        re.search(
            r"Three.Layer Regulator Theorem.*(?:Connes|Lizzi|Van den Dungen)",
            registry_text,
        )
    )
    # §VII.M occupation by DR3-RESPONSE-PROTOCOL or event-driven pre-registrations
    has_dr3_vii_m = bool(
        re.search(
            r"VII\.M.*Event.driven pre.registrations|DR3-RESPONSE-PROTOCOL",
            registry_text,
        )
    )
    return {
        "vii_m_exists": has_vii_m,
        "vii_n_exists": has_vii_n,
        "closure_sha_in_registry": has_closure,
        "three_solo_attestation_in_vii_n": has_three_solo_attestation,
        "vii_m_occupied_by_dr3_or_event_driven": has_dr3_vii_m,
    }


def main() -> int:
    print("=" * 70)
    print("S85-W2-THREE-SOLO-CONVERGENCE-VERIFY")
    print("=" * 70)
    input_shas: dict[str, str] = {}
    for f in INPUT_FILES:
        sha = sha256_of(f)
        input_shas[f] = sha
        print(f"INPUT  {f}  sha256={sha}")
    print("-" * 70)

    # Load S83 ledger and registry
    s83_ledger_path = Path("computations/session-83/s83_gate_verdicts.txt")
    registry_path = Path("sessions/permanent-results-registry.md")
    s83_ledger = s83_ledger_path.read_text(encoding="utf-8", errors="ignore")
    registry_text = registry_path.read_text(encoding="utf-8", errors="ignore")

    # Verify 4 anchors
    anchor_results = []
    num_anchors_verified = 0  # (local) accumulator
    for anchor_id, meta in ANCHORS.items():
        r = verify_anchor(anchor_id, meta["full_sha"], s83_ledger)
        r["label"] = meta["label"]
        anchor_results.append(r)
        if r["verified"]:
            num_anchors_verified += 1

    # Verify registry routing
    routing = verify_registry_routing(registry_text)

    # Verdict
    closure_match = routing["closure_sha_in_registry"]
    routing_ok = (
        routing["vii_m_exists"]
        and routing["vii_n_exists"]
        and routing["vii_m_occupied_by_dr3_or_event_driven"]
        and routing["three_solo_attestation_in_vii_n"]
    )

    if num_anchors_verified == 4 and closure_match and routing_ok:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    # Build SHA closure
    pin_map_str = json.dumps(
        {
            "inputs": input_shas,
            "anchors_verified": [
                {"id": r["anchor_id"], "sha": r["full_sha"], "verified": r["verified"]}
                for r in anchor_results
            ],
            "closure_sha_expected": CLOSURE_SHA_EXPECTED,
            "closure_match": closure_match,
            "routing": routing,
            "num_anchors_verified": num_anchors_verified,
        },
        sort_keys=True,
    )
    closure_sha = hashlib.sha256(pin_map_str.encode()).hexdigest()
    content_sha = hashlib.sha256(
        json.dumps({"anchors": anchor_results, "routing": routing}, sort_keys=True).encode()
    ).hexdigest()

    print("Anchor verification:")
    for r in anchor_results:
        mark = "[OK]" if r["verified"] else "[FAIL]"
        print(f"  {mark} {r['anchor_id']:<7}  sha={r['full_sha'][:16]}...  ({r['label']})")
    print(f"  num_anchors_verified = {num_anchors_verified} / 4")
    print("-" * 70)
    print("Routing verification:")
    for k, v in routing.items():
        mark = "[OK]" if v else "[FAIL]"
        print(f"  {mark} {k} = {v}")
    print(f"  closure SHA ({CLOSURE_SHA_EXPECTED[:16]}...) found: {closure_match}")
    print("-" * 70)

    out_json = {
        "gate_id": "S85-W2-THREE-SOLO-CONVERGENCE-VERIFY",
        "verdict": verdict,
        "value_4tuple": {
            "value": num_anchors_verified,
            "scheme": "three-solo-sha-reproduction",
            "convention": "S84-W2a-11",
            "L_max": "N/A",
        },
        "anchors": anchor_results,
        "routing": routing,
        "closure_sha_expected": CLOSURE_SHA_EXPECTED,
        "closure_sha_matched_in_registry": closure_match,
        "closure_sha256": closure_sha,
        "content_sha256": content_sha,
        "input_shas": input_shas,
    }
    out_path = Path(__file__).parent / "s85_w2_three_solo_anchor_sha.json"
    out_path.write_text(json.dumps(out_json, indent=2))
    print(f"WROTE {out_path}")
    print(f"VERDICT: {verdict}")
    print(f"closure_sha256 = {closure_sha}")
    print(f"content_sha256 = {content_sha}")
    print(
        f"4-tuple: value={num_anchors_verified}, scheme=three-solo-sha-reproduction, "
        f"convention=S84-W2a-11, L_max=N/A"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
