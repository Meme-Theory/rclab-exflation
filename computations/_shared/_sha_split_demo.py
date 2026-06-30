#!/usr/bin/env python3
"""
_sha_split_demo.py — S84 W9a-99 dual-SHA differential-sensitivity demo
=====================================================================

Demonstrates that the S84+ dual-SHA schema separates script-content
sensitivity from (canonical, pinmap) sensitivity.

Claims checked (each gets a PASS/FAIL print):

  (A) Baseline: compute (audit_sha256, content_sha256) on a reference
      (script, canonical, pinmap) triple.

  (B) Mutate canonical, keep script + pinmap fixed:
        expected: content_sha256 UNCHANGED, audit_sha256 CHANGED
      (this is the S82 G59 ambiguity closure — the script-identity
       signal is no longer collapsed into the joint digest).

  (C) Mutate pinmap (an input SHA), keep script + canonical fixed:
        expected: content_sha256 UNCHANGED, audit_sha256 CHANGED

  (D) Mutate script, keep canonical + pinmap fixed:
        expected: BOTH content_sha256 AND audit_sha256 CHANGED
      (script bytes feed both hashes.)

Substitution chain (pre-registered in W9a-99 PRDR):

  Def 1: audit_SHA   = sha256( bytes(script) || bytes(canonical) || bytes(pinmap_json) )
  Def 2: content_SHA = sha256( bytes(script) )
  Def 3: H(gate | X) = log2 |preimage(X)|

  S82 G59: |preimage(single_SHA)| = 3   ->  H = log2(3) = 1.585 bits
  S84+:    |preimage((audit, content))| = 1  ->  H = log2(1) = 0 bits
  Direction: ΔH = +1.585 bits entropy reduction (matches sig_2 weight).

NON-PHONONIC. No substrate content — pure harness-level demonstration.
"""
from __future__ import annotations

# Canonical import per project rules (unused here; demo operates on
# synthetic bytes, but the audit rejects computation scripts missing this line).
from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import math
import sys


def _sha(b: bytes) -> str:
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def dual_sha(script: bytes, canonical: bytes, pins: dict[str, str]) -> tuple[str, str]:
    """Pure-bytes implementation of compute_dual_sha (demo/test-friendly)."""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script)
    h_audit.update(canonical)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = _sha(script)  # (local)
    return audit, content


def _row(label: str, audit: str, content: str) -> None:
    print(f"  {label:<28s}  audit={audit[:16]}...  content={content[:16]}...")


def main() -> int:
    print("=== _sha_split_demo.py — S84 W9a-99 dual-SHA differential sensitivity ===\n")

    # Reference triple (synthetic; bytes chosen to be unambiguous).
    script_0 = b"# computation script v1\nresult = 42\n"  # (local)
    canonical_0 = b"# canonical_constants\nM_KK = 1.0\n"  # (local)
    pins_0 = {  # (local)
        "computations/_shared/canonical_constants.py": "a" * 64,
        "computations/_shared/some_input.npz": "b" * 64,
    }

    a0, c0 = dual_sha(script_0, canonical_0, pins_0)
    print("(A) Baseline")
    _row("(script, canonical, pins)", a0, c0)
    print()

    # (B) Mutate canonical only.
    canonical_1 = canonical_0 + b"\nM_KK = 1.5\n"  # (local) append a line
    a1, c1 = dual_sha(script_0, canonical_1, pins_0)
    print("(B) Canonical mutated; script + pins unchanged")
    _row("(script, canonical', pins)", a1, c1)
    audit_changed_B = a1 != a0  # (local)
    content_same_B = c1 == c0  # (local)
    verdict_B = "PASS" if (audit_changed_B and content_same_B) else "FAIL"  # (local)
    print(f"    audit changed?   {audit_changed_B}   (expect True)")
    print(f"    content same?    {content_same_B}   (expect True)")
    print(f"    (B) {verdict_B}\n")

    # (C) Mutate pinmap only (flip one input SHA).
    pins_1 = dict(pins_0)  # (local)
    pins_1["computations/_shared/some_input.npz"] = "c" * 64
    a2, c2 = dual_sha(script_0, canonical_0, pins_1)
    print("(C) Pinmap mutated; script + canonical unchanged")
    _row("(script, canonical, pins')", a2, c2)
    audit_changed_C = a2 != a0  # (local)
    content_same_C = c2 == c0  # (local)
    verdict_C = "PASS" if (audit_changed_C and content_same_C) else "FAIL"  # (local)
    print(f"    audit changed?   {audit_changed_C}   (expect True)")
    print(f"    content same?    {content_same_C}   (expect True)")
    print(f"    (C) {verdict_C}\n")

    # (D) Mutate script only.
    script_1 = script_0 + b"\nresult = 43\n"  # (local)
    a3, c3 = dual_sha(script_1, canonical_0, pins_0)
    print("(D) Script mutated; canonical + pins unchanged")
    _row("(script', canonical, pins)", a3, c3)
    audit_changed_D = a3 != a0  # (local)
    content_changed_D = c3 != c0  # (local)
    verdict_D = "PASS" if (audit_changed_D and content_changed_D) else "FAIL"  # (local)
    print(f"    audit changed?   {audit_changed_D}   (expect True)")
    print(f"    content changed? {content_changed_D}   (expect True)")
    print(f"    (D) {verdict_D}\n")

    all_pass = all(v == "PASS" for v in (verdict_B, verdict_C, verdict_D))  # (local)

    # Substitution-chain numeric verification.
    preimage_single = 3  # (local) S82 G59 observed case
    preimage_dual = 1    # (local) joint match (collision-negligible)
    H_single = math.log2(preimage_single)  # (local)
    H_dual = math.log2(preimage_dual)      # (local)
    dH = H_single - H_dual                 # (local)
    print("Substitution-chain entropy reduction:")
    print(f"    H(gate | single_SHA) = log2({preimage_single}) = {H_single:.6f} bits")
    print(f"    H(gate | dual_SHA)   = log2({preimage_dual}) = {H_dual:.6f} bits")
    print(f"    ΔH                   = {dH:.6f} bits  (sig_2 weight = 1.585)")
    print()
    print(f"=== demo {'PASS' if all_pass else 'FAIL'} ===")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
