#!/usr/bin/env python3
"""
S112 W2-1 CF-S112-CLOCKLOC3-STAGE2 — Stage-2 cross-axis PASS-AND collation for §VII.CG
=====================================================================================

Gate: CF-S112-CLOCKLOC3-STAGE2 ([VERIFY-THEOREM])

This is a COLLATION gate, NOT a physics computation. It reads the two NON-AUTHOR
cross-reviewer clause-verdict JSONs (Axis-A einstein-theorist; Axis-B
transit-dynamics-theorist), builds the per-reviewer per-clause verdict matrix in
memory, and computes the deterministic logical PASS-AND that decides whether
§VII.CG (the r=16ε layer-obstruction no-go) passes Stage-2 cross-axis independent
verify per `joint-theorem-promotion.md §"Stage 2"`.

The collation does NOT re-adjudicate the physics — the reviewer verdicts are the
inputs (`Investigating-Workshops.md §"Q3"`: parallel-compute wave, structurally
orthogonal axes, no R1/R2/R3 rounds).

Pre-registered PASS-AND (plan §W2-1 operator):
  composite = PASS  iff  (A.clauses.a == PASS) AND (B.clauses.b == PASS)
                    AND  (A.clauses.c == PASS  AND  B.clauses.c == PASS)   # JOINT (c)
  ANY clause FAIL → composite FAIL (theorem stays STAGE-1-CANDIDATE);
  no FAIL but ANY clause INFO → composite INFO (Stage-2-INFO-deferred).

  Axis-A (einstein-theorist) audits single-axis clause (a) [Level-2-clock typing]
    + JOINT clause (c).
  Axis-B (transit-dynamics-theorist) audits single-axis clause (b) [ε[φ] Level-1
    field requirement] + JOINT clause (c).
  JOINT clause (c) [layer-obstruction no-go: a Level-2 deformation parameter
    cannot enter a Level-1 single-field consistency relation ⇒ no substrate ε[φ]
    ⇒ r=16ε has no substrate image] is PASS-AND'd across BOTH verdicts.

Dual-prior (registry §VII.CG): Track-A 6th-INDEPENDENT 0.40 / Track-B
structural-ROOT 0.60. Discriminator (plan §W2-1 dual_prior): JOINT-(c) PASS-AND
⇒ 0.9 to Track-B structural-ROOT; either-reviewer INFO on the track-allocation
⇒ unchanged (INFO-deferred); JOINT-(c) FAIL ⇒ track-allocation moot.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - this script (feeds BOTH audit_sha256 and content_sha256)
  - registered §VII.CG body (registry lines 22219–22235; feeds audit_sha256)
  - reviewer_A clause-verdict JSON (Axis-A einstein; feeds audit_sha256)
  - reviewer_B clause-verdict JSON (Axis-B transit; feeds audit_sha256)
  - the ordered pinmap (feeds audit_sha256)
  - canonical_constants.py (template default; feeds audit_sha256)

audit_sha256 = closure_hash over the ordered inputs
  [script, registered §VII.CG body, reviewer_A_json, reviewer_B_json, pinmap]
content_sha256 = sha256(bytes(script))

Output 4-tuple:
  (value=<composite>, scheme=STAGE-2-CROSS-AXIS-PASS-AND,
   convention=JOINT-CLAUSE-LOGICAL-AND, L_max=N/A)

Classification: GEOMETRIC (intra-substrate layer-type no-go on the moduli
  structure of (A_K,H_K,D_K(τ)); no laboratory-IN observable).

DISCIPLINE
----------
- CPU-only (JSON read + boolean AND + hashlib; no linear algebra). OMP_NUM_THREADS
  capped at 8 BEFORE any numpy import per computation-environment.md.
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): this
  script PRINTS the payload (`print_verdict_payload`); the dispatching agent calls
  `mcp__knowledge__emit_verdict(**payload)`. The script does NOT write the verdict
  file directly.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (collation only; set before numpy import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# canonical_constants.py lives in computations/_shared; add to path then import.
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S112"                                                   # (local)
GATE_ID = "CF-S112-CLOCKLOC3-STAGE2"                              # (local)
SCHEME = "STAGE-2-CROSS-AXIS-PASS-AND"                            # (local)
CONVENTION = "JOINT-CLAUSE-LOGICAL-AND"                           # (local)
L_MAX = "N/A"                                                      # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
REVIEWER_A_JSON = SESSION_DIR / "s112_clocloc3_stage2_axisA_einstein.json"  # (local)
REVIEWER_B_JSON = SESSION_DIR / "s112_clocloc3_stage2_axisB_transit.json"  # (local)

OUT_NPZ = SESSION_DIR / "s112_cf_clocloc3_stage2.npz"             # (local)

# §VII.CG registered-entry body span (registry lines 22219–22235 inclusive; the
# next "### §VII." header is line 22236). The audit_sha256 input is this body
# span — deterministic + reproducible from the registry file alone.
VII_CG_BODY_START = 22219                                          # (local)
VII_CG_BODY_END_EXCL = 22236   # first line of the NEXT §VII entry (exclusive)  # (local)

# Dual-prior priors (registry §VII.CG; plan §W2-1 dual_prior pin)
PRIOR_TRACK_A_6TH_INDEPENDENT = 0.40                              # (local)
PRIOR_TRACK_B_STRUCTURAL_ROOT = 0.60                              # (local)
# Discriminator: JOINT-(c) PASS-AND ⇒ posterior mass to Track-B structural-ROOT.
POST_TRACK_B_ON_JOINT_C_PASS = 0.90                              # (local)

# The single-axis clause each reviewer is REQUIRED to carry on its own axis, plus
# the JOINT clause both must carry (the PASS-AND structural-independence guarantee).
REVIEWER_A_SINGLE_AXIS_CLAUSE = "a"   # Level-2-clock typing (einstein)         # (local)
REVIEWER_B_SINGLE_AXIS_CLAUSE = "b"   # ε[φ] Level-1 field req (transit)        # (local)
JOINT_CLAUSE = "c"                     # layer-obstruction no-go (PASS-AND'd)    # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of_bytes(b: bytes) -> str:
    """SHA-256 hexdigest of a byte string."""
    h = hashlib.sha256()  # (local)
    h.update(b)
    return h.hexdigest()


def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    try:
        return sha256_of_bytes(path.read_bytes())
    except OSError:
        return ""


def extract_registry_body(path: Path, start: int, end_excl: int) -> bytes:
    """Extract the §VII.CG body span (1-indexed [start, end_excl) lines) as bytes.

    Deterministic + reproducible: any auditor re-reading the registry at the same
    line span recovers the same bytes, hence the same SHA. Line endings preserved
    by splitting on b'\\n' and re-joining with b'\\n'.
    """
    raw = path.read_bytes()  # (local)
    lines = raw.split(b"\n")  # (local)
    # 1-indexed: lines[start-1 : end_excl-1] is the inclusive [start, end_excl) span.
    span = lines[start - 1: end_excl - 1]  # (local)
    return b"\n".join(span)


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict insertion order via
    sorted keys). The pin KEYS are numeric-prefixed (0_/1_/2_/3_) so the sorted
    order reproduces the plan's intended input ordering deterministically."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Collation (the PASS-AND logical conjunction)
# ---------------------------------------------------------------------------

def load_reviewer(path: Path, expected_axis: str, expected_reviewer: str) -> dict:
    """Load + structurally validate a reviewer clause-verdict JSON."""
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)  # (local)
    # Structural sanity (NOT physics re-adjudication): correct gate / axis / reviewer.
    assert data.get("gate_id") == GATE_ID, (
        f"{path.name}: gate_id mismatch {data.get('gate_id')!r} != {GATE_ID!r}")
    assert data.get("axis") == expected_axis, (
        f"{path.name}: axis mismatch {data.get('axis')!r} != {expected_axis!r}")
    assert data.get("reviewer") == expected_reviewer, (
        f"{path.name}: reviewer mismatch {data.get('reviewer')!r} != {expected_reviewer!r}")
    assert data.get("theorem") == "§VII.CG", (
        f"{path.name}: theorem mismatch {data.get('theorem')!r} != '§VII.CG'")
    return data


def clause_verdict(data: dict, clause: str) -> str:
    """Pull a single clause's verdict string from a reviewer JSON (uppercased)."""
    clauses = data.get("clauses", {})  # (local)
    assert clause in clauses, (
        f"reviewer {data.get('reviewer')!r} missing required clause '{clause}'")
    v = clauses[clause].get("verdict", "").strip().upper()  # (local)
    assert v in ("PASS", "FAIL", "INFO"), (
        f"clause '{clause}' verdict {v!r} not in PASS/FAIL/INFO")
    return v


def composite_passand(clause_verdicts: list[str]) -> str:
    """Deterministic PASS-AND collapse over the required clause-verdict list.

    ANY FAIL → FAIL; else ANY INFO → INFO; else PASS. (Plan §W2-1 verdict rubric.)
    """
    if "FAIL" in clause_verdicts:
        return "FAIL"
    if "INFO" in clause_verdicts:
        return "INFO"
    return "PASS"


def compute() -> dict:
    """Read both reviewer JSONs, build the clause-verdict matrix, PASS-AND it."""
    rev_a = load_reviewer(REVIEWER_A_JSON, "A", "einstein-theorist")  # (local)
    rev_b = load_reviewer(REVIEWER_B_JSON, "B", "transit-dynamics-theorist")  # (local)

    # Per-reviewer per-clause verdict matrix.
    a_a = clause_verdict(rev_a, REVIEWER_A_SINGLE_AXIS_CLAUSE)   # einstein (a)   # (local)
    a_c = clause_verdict(rev_a, JOINT_CLAUSE)                    # einstein (c)   # (local)
    b_b = clause_verdict(rev_b, REVIEWER_B_SINGLE_AXIS_CLAUSE)   # transit  (b)   # (local)
    b_c = clause_verdict(rev_b, JOINT_CLAUSE)                    # transit  (c)   # (local)

    # The PASS-AND set: 3 single-axis-side clause readings + JOINT (c) in BOTH.
    #   composite = (A.a) ∧ (B.b) ∧ (A.c) ∧ (B.c)
    passand_set = [a_a, b_b, a_c, b_c]  # (local)
    composite = composite_passand(passand_set)  # (local)

    # JOINT-(c) PASS-AND status (both reviewers must independently PASS (c)).
    joint_c_passand = composite_passand([a_c, b_c])  # (local)

    # Dual-prior resolution (the JOINT-(c) reading).
    #   JOINT-(c) PASS-AND ⇒ 0.9 to Track-B structural-ROOT; INFO ⇒ unchanged;
    #   FAIL ⇒ track-allocation moot.
    if joint_c_passand == "PASS":
        post_b = POST_TRACK_B_ON_JOINT_C_PASS  # (local)
        post_a = 1.0 - post_b                   # (local)
        dual_prior_resolution = "structural-ROOT"  # (local)
    elif joint_c_passand == "INFO":
        post_b = PRIOR_TRACK_B_STRUCTURAL_ROOT  # (local)
        post_a = PRIOR_TRACK_A_6TH_INDEPENDENT  # (local)
        dual_prior_resolution = "UNRESOLVED-INFO-DEFERRED"  # (local)
    else:  # FAIL
        post_b = float("nan")  # (local)
        post_a = float("nan")  # (local)
        dual_prior_resolution = "MOOT-JOINT-C-FAIL"  # (local)

    # Record each reviewer's own dual-prior reading (for the WP).
    reading_a = rev_a.get("dual_prior_reading", "")  # (local)
    reading_b = rev_b.get("dual_prior_reading", "")  # (local)
    overall_a = rev_a.get("overall_axis_verdict", "").strip().upper()  # (local)
    overall_b = rev_b.get("overall_axis_verdict", "").strip().upper()  # (local)

    return {
        "value": composite,
        "matrix": {
            "einstein_A": {"a": a_a, "c": a_c, "overall": overall_a},
            "transit_B": {"b": b_b, "c": b_c, "overall": overall_b},
        },
        "passand_set": passand_set,
        "joint_c_passand": joint_c_passand,
        "reading_A": reading_a,
        "reading_B": reading_b,
        "post_track_A": post_a,
        "post_track_B": post_b,
        "dual_prior_resolution": dual_prior_resolution,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """PRINT the verdict payload for the dispatching agent to pass to
    mcp__knowledge__emit_verdict. The script does NOT write the verdict file —
    that lock-serialized write is owned by emit_verdict (gate-verdicts.md
    §"Race-Safe Emission")."""
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
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)
    script_path = Path(__file__).resolve()  # (local)

    # 1. Extract the §VII.CG body span + read the two reviewer JSONs as bytes.
    vii_cg_body = extract_registry_body(REGISTRY, VII_CG_BODY_START, VII_CG_BODY_END_EXCL)  # (local)
    sha_script = sha256_of(script_path)  # (local)
    sha_body = sha256_of_bytes(vii_cg_body)  # (local)
    sha_rev_a = sha256_of(REVIEWER_A_JSON)  # (local)
    sha_rev_b = sha256_of(REVIEWER_B_JSON)  # (local)

    # 2. Ordered pin map (numeric-prefixed keys ⇒ sorted-closure preserves the
    #    plan's intended input ordering [script, body, rev_A, rev_B]).
    pins = {
        "0_script": sha_script,
        "1_registered_entry_VII_CG_body": sha_body,
        "2_reviewer_A_clause_verdict_json": sha_rev_a,
        "3_reviewer_B_clause_verdict_json": sha_rev_b,
    }  # (local)

    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    print(f"  script:                       {sha_script[:16]}...")
    print(f"  §VII.CG body (L{VII_CG_BODY_START}-{VII_CG_BODY_END_EXCL - 1}): {sha_body[:16]}...")
    print(f"  reviewer_A (einstein) json:   {sha_rev_a[:16]}...")
    print(f"  reviewer_B (transit) json:    {sha_rev_b[:16]}...")

    # 3. audit_sha256 = closure over the ordered pinmap; content_sha256 = script bytes.
    audit_sha = closure_hash(pins)  # (local)
    content_sha = sha_script  # content_sha256 = sha256(bytes(script))   # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (closure over ordered [script, body, revA, revB])")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 4. Compute the PASS-AND collation.
    result = compute()  # (local)
    composite = result["value"]  # (local)

    print("=== per-reviewer per-clause verdict matrix ===")
    m = result["matrix"]  # (local)
    print(f"  Axis-A einstein-theorist:        (a)={m['einstein_A']['a']}  "
          f"(c)={m['einstein_A']['c']}  overall={m['einstein_A']['overall']}")
    print(f"  Axis-B transit-dynamics-theorist:(b)={m['transit_B']['b']}  "
          f"(c)={m['transit_B']['c']}  overall={m['transit_B']['overall']}")
    print(f"  PASS-AND set [A.a, B.b, A.c, B.c] = {result['passand_set']}")
    print(f"  JOINT-(c) PASS-AND               = {result['joint_c_passand']}")
    print(f"  composite (A.a ∧ B.b ∧ A.c ∧ B.c) = {composite}")
    print()
    print("=== dual-prior resolution ===")
    print(f"  reviewer-A reading: {result['reading_A']}")
    print(f"  reviewer-B reading: {result['reading_B']}")
    print(f"  prior (Track-A 6th-INDEPENDENT / Track-B structural-ROOT) = "
          f"{PRIOR_TRACK_A_6TH_INDEPENDENT} / {PRIOR_TRACK_B_STRUCTURAL_ROOT}")
    print(f"  posterior (Track-A / Track-B) = "
          f"{result['post_track_A']:.3f} / {result['post_track_B']:.3f}")
    print(f"  resolution = {result['dual_prior_resolution']}")
    print()

    # 5. Persist the npz (clause-verdict matrix + dual-prior posterior).
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_verdict=composite,
        einstein_A_clause_a=m["einstein_A"]["a"],
        einstein_A_clause_c=m["einstein_A"]["c"],
        einstein_A_overall=m["einstein_A"]["overall"],
        transit_B_clause_b=m["transit_B"]["b"],
        transit_B_clause_c=m["transit_B"]["c"],
        transit_B_overall=m["transit_B"]["overall"],
        passand_set=np.array(result["passand_set"]),
        joint_c_passand=result["joint_c_passand"],
        reviewer_A_dual_prior_reading=result["reading_A"],
        reviewer_B_dual_prior_reading=result["reading_B"],
        prior_track_A_6th_independent=PRIOR_TRACK_A_6TH_INDEPENDENT,
        prior_track_B_structural_root=PRIOR_TRACK_B_STRUCTURAL_ROOT,
        post_track_A=result["post_track_A"],
        post_track_B=result["post_track_B"],
        dual_prior_resolution=result["dual_prior_resolution"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        vii_cg_body_sha256=sha_body,
        reviewer_A_json_sha256=sha_rev_a,
        reviewer_B_json_sha256=sha_rev_b,
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 6. Emit 4-tuple + PRINT the emit_verdict payload.
    tag = emit_4tuple(composite, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    companion = (
        f"Stage-2 cross-axis PASS-AND §VII.CG: "
        f"A(einstein) a={m['einstein_A']['a']} c={m['einstein_A']['c']}; "
        f"B(transit) b={m['transit_B']['b']} c={m['transit_B']['c']}; "
        f"JOINT-(c) PASS-AND={result['joint_c_passand']}; "
        f"dual-prior={result['dual_prior_resolution']} "
        f"(Track-B structural-ROOT posterior={result['post_track_B']:.2f})"
    )  # (local)
    print_verdict_payload(composite, composite, audit_sha, content_sha,
                          companion_note=companion)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
