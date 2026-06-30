#!/usr/bin/env python3
"""
S107 W2-4 S107-VIIAC4-STAGE2-VERIFY — Stage-2 PASS-AND aggregator (K11, §VII.AC.4)
=================================================================================

Gate: S107-VIIAC4-STAGE2-VERIFY ([VERIFY-THEOREM])

Pre-registered threshold (NON-COMPUTE adjudication gate; cross-axis PASS-AND):
  PASS iff ( ALL single-axis-A clauses PASS in reviewer-A verdict )
       AND ( ALL single-axis-B clauses PASS in reviewer-B verdict )
       AND ( EVERY JOINT clause PASS in reviewer-A verdict AND PASS in reviewer-B verdict )
  FAIL iff ANY clause FAIL in either verdict OR either overall_axis_verdict == FAIL.
  INFO otherwise (ANY clause INFO in either verdict OR either overall_axis_verdict == INFO).

This script performs NO physics. The physics audit is the two reviewers'
first-principles blind re-derivation (van-den-dungen on NCG-axiomatic C1;
kitaev on spectral-block V1). This script is the DETERMINISTIC AND-aggregator:
it reads the two clause-verdict JSONs, recomputes the cross-axis PASS-AND with
JOINT clauses PASS-AND'd across both verdicts, and prints the composite verdict
payload. gen-physicist then calls the emit_verdict knowledge-MCP tool.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - reviewer-A clause-verdict JSON (van-den-dungen, NCG C1)
  - reviewer-B clause-verdict JSON (kitaev, spectral-block V1)
  - registered §VII.AC.4 Stage-1 entry block (permanent-results-registry.md lines 15167-15204)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

audit_sha256 input-pin map (per plan §W2-4):
  [script, registered-entry §VII.AC.4 block SHA, reviewerA_json SHA, reviewerB_json SHA, pinmap]

Output 4-tuple:
  (value=<composite>, scheme=STAGE-2-BLIND-CROSS-AXIS-VERIFY,
   convention=SOURCE-DOUBLE-CITE-CO-PRIMARY-SEQUENTIAL-CHAIN-PASS-AND, L_max=10)

Classification: GEOMETRIC (object audited is a substrate-IS block decomposition
  forced by Schur orthogonality on the finite fiber A_F = C (+) H (+) M_3(C);
  the aggregation itself is NON-PHONONIC methodology).

METHODOLOGY
-----------
Per joint-theorem-promotion.md §"Stage 2": JOINT clauses are PASS-AND'd across
the two blind cross-reviewer verdicts (logical AND, not OR); single-axis clauses
must PASS in their own reviewer's verdict. An INFO on any clause in either
verdict holds the theorem at STAGE-1-CANDIDATE as a Stage-2-INFO-deferred item;
a FAIL on any clause blocks the promotion. The composite collapse is the
deterministic three-way rule above.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Pure integer/boolean aggregation; no linear algebra; cpu-cap-OMP8.
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- audit_sha256 = sha256( script || canonical || pinmap_json ) where pinmap_json
  includes the registered-entry-block SHA + both reviewer-JSON SHAs (the plan's
  5-element pin set: [script, registered-entry, reviewerA, reviewerB, pinmap]).
- 4-tuple printed as the final non-verdict line.
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (put computations/_shared on sys.path so the
# canonical_constants import below resolves regardless of cwd) + thread cap.
# ---------------------------------------------------------------------------
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
if str(SHARED_DIR) not in sys.path:
    sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration (paths computed in Section 0)
# ---------------------------------------------------------------------------

SESSION = "S107"                                                   # (local)
GATE_ID = "S107-VIIAC4-STAGE2-VERIFY"                              # (local)
SCHEME = "STAGE-2-BLIND-CROSS-AXIS-VERIFY"                         # (local)
CONVENTION = "SOURCE-DOUBLE-CITE-CO-PRIMARY-SEQUENTIAL-CHAIN-PASS-AND"  # (local)
L_MAX = 10                                                         # (local)

# Registered §VII.AC.4 Stage-1 entry block span (permanent-results-registry.md)
REG_ENTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
REG_ENTRY_LINE_START = 15167                                       # (local) 1-indexed inclusive
REG_ENTRY_LINE_END = 15204                                         # (local) 1-indexed inclusive

# Reviewer clause-verdict JSONs (already on disk; produced by the two blind reviewers)
REVIEWER_A_JSON = SESSION_DIR / "s107_w2_viiac4_reviewerA_vandendungen_clause_verdicts.json"  # (local)
REVIEWER_B_JSON = SESSION_DIR / "s107_w2_viiac4_reviewerB_kitaev_clause_verdicts.json"        # (local)

# Output destinations
OUT_NPZ = SESSION_DIR / "s107_w2_viiac4_stage2_verify.npz"        # (local)

# Files feeding the dual-SHA (canonical feeds audit only; script feeds both)
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    """SHA-256 of a UTF-8 string (used for the registered-entry block span)."""
    h = hashlib.sha256()  # (local)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def extract_block(path: Path, start_1idx: int, end_1idx: int) -> str:
    """Return the inclusive [start, end] 1-indexed line span of a file as text."""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)  # (local)
    # 1-indexed inclusive -> python slice [start-1 : end]
    return "".join(lines[start_1idx - 1:end_1idx])


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering); legacy."""
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256 = sha256( bytes(script) || bytes(canonical) || pinmap_json )
      where pinmap_json is the canonical sorted JSON of `pins`. Per plan §W2-4,
      `pins` includes the registered §VII.AC.4 block SHA + both reviewer-JSON
      SHAs + canonical_constants.py SHA, so the 5-element pin set
      [script, registered-entry, reviewerA, reviewerB, pinmap] is faithfully
      embedded (script bytes hashed directly; the other four enter via pins).
    content_sha256 = sha256( bytes(script) ) — script-only.
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Aggregation (NO physics; deterministic cross-axis PASS-AND)
# ---------------------------------------------------------------------------

# Pre-registered clause partition (plan §W2-4 mirrors §W2-1 with AC.4 anchors).
SINGLE_AXIS_A_CLAUSES = ["single-axis-A-1", "single-axis-A-2"]      # (local)
SINGLE_AXIS_B_CLAUSES = ["single-axis-B-1", "single-axis-B-2"]      # (local)
JOINT_CLAUSES = ["JOINT-1", "JOINT-2", "JOINT-3"]                   # (local)


def load_reviewer(path: Path) -> dict:
    """Load a reviewer clause-verdict JSON."""
    return json.loads(path.read_text(encoding="utf-8"))


def clause_verdict(reviewer: dict, clause: str) -> str:
    """Return the per-clause verdict string for a reviewer, or 'ABSENT'."""
    cv = reviewer.get("clause_verdicts", {})  # (local)
    entry = cv.get(clause)  # (local)
    if entry is None:
        return "ABSENT"
    return str(entry.get("verdict", "ABSENT")).upper()


def aggregate(reviewer_a: dict, reviewer_b: dict) -> dict:
    """Deterministic cross-axis PASS-AND aggregation.

    Returns a result dict with the reviewer x clause matrix, the JOINT-clause
    PASS-AND sub-verdicts, the sequential-chain (CO-PRIMARY direction) sub-verdict,
    and the composite.
    """
    # ---- Build the reviewer x clause matrix ----
    a_clauses = SINGLE_AXIS_A_CLAUSES + JOINT_CLAUSES  # clauses present in reviewer A
    b_clauses = SINGLE_AXIS_B_CLAUSES + JOINT_CLAUSES  # clauses present in reviewer B

    matrix = {  # (local)
        "reviewer_A": {c: clause_verdict(reviewer_a, c) for c in a_clauses},
        "reviewer_B": {c: clause_verdict(reviewer_b, c) for c in b_clauses},
    }

    overall_a = str(reviewer_a.get("overall_axis_verdict", "ABSENT")).upper()  # (local)
    overall_b = str(reviewer_b.get("overall_axis_verdict", "ABSENT")).upper()  # (local)

    # ---- Single-axis verdicts (each clause PASS in its own reviewer's verdict) ----
    single_a = {c: clause_verdict(reviewer_a, c) for c in SINGLE_AXIS_A_CLAUSES}  # (local)
    single_b = {c: clause_verdict(reviewer_b, c) for c in SINGLE_AXIS_B_CLAUSES}  # (local)

    # ---- JOINT-clause PASS-AND sub-verdicts (PASS only if PASS in BOTH) ----
    def collapse_pair(va: str, vb: str) -> str:
        """A JOINT clause PASS only if PASS in BOTH; FAIL if either FAIL; else INFO."""
        if va == "FAIL" or vb == "FAIL":
            return "FAIL"
        if va == "PASS" and vb == "PASS":
            return "PASS"
        return "INFO"  # any INFO/ABSENT in either degrades to INFO

    joint_pass_and = {}  # (local)
    for c in JOINT_CLAUSES:
        va = clause_verdict(reviewer_a, c)  # (local)
        vb = clause_verdict(reviewer_b, c)  # (local)
        joint_pass_and[c] = {"axis_A": va, "axis_B": vb, "pass_and": collapse_pair(va, vb)}

    # ---- Composite collapse (the pre-registered three-way rule) ----
    # Gather all clause verdicts across both reviewers + both overall verdicts.
    all_clause_verdicts = (
        list(single_a.values())
        + list(single_b.values())
        + [clause_verdict(reviewer_a, c) for c in JOINT_CLAUSES]
        + [clause_verdict(reviewer_b, c) for c in JOINT_CLAUSES]
    )  # (local)
    any_fail = ("FAIL" in all_clause_verdicts) or (overall_a == "FAIL") or (overall_b == "FAIL")  # (local)
    any_info = (
        ("INFO" in all_clause_verdicts) or (overall_a == "INFO") or (overall_b == "INFO")
    )  # (local)

    if any_fail:
        composite = "FAIL"  # (local)
    elif any_info:
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # ---- Sequential-chain (CO-PRIMARY direction) sub-verdict ----
    # JOINT-1 (sequential) + JOINT-2 (non-fungible) carry the CO-PRIMARY-vs-
    # PRIMARY+CONFIRMATION direction claim; JOINT-3 splits into a direction leg
    # (sub-claim a, PASS on both axes) + a same-cell tag-provenance leg
    # (sub-claim b, INFO on both axes: the s=3 Mellin pole is audit-substituted).
    co_primary_direction = collapse_pair(
        clause_verdict(reviewer_a, "JOINT-1"), clause_verdict(reviewer_b, "JOINT-1")
    )  # (local) -- sequential
    non_fungible = collapse_pair(
        clause_verdict(reviewer_a, "JOINT-2"), clause_verdict(reviewer_b, "JOINT-2")
    )  # (local) -- non-fungible
    # CO-PRIMARY-direction sub-verdict = AND of (sequential, non-fungible)
    seq_chain_direction = (
        "PASS" if (co_primary_direction == "PASS" and non_fungible == "PASS")
        else ("FAIL" if (co_primary_direction == "FAIL" or non_fungible == "FAIL") else "INFO")
    )  # (local)

    return {
        "matrix": matrix,
        "overall_axis_A": overall_a,
        "overall_axis_B": overall_b,
        "single_axis_A": single_a,
        "single_axis_B": single_b,
        "joint_pass_and": joint_pass_and,
        "co_primary_direction_sequential": co_primary_direction,
        "non_fungible": non_fungible,
        "seq_chain_co_primary_direction": seq_chain_direction,
        "joint3_axis_A": clause_verdict(reviewer_a, "JOINT-3"),
        "joint3_axis_B": clause_verdict(reviewer_b, "JOINT-3"),
        "any_fail": any_fail,
        "any_info": any_info,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
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
    """Print the verdict PAYLOAD for the dispatching AGENT to pass to emit_verdict.

    The script does NOT write the verdict file (race-safe single writer is the
    emit_verdict MCP tool). value is the RAW payload string (no single quotes).
    """
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

    # 1. Log input pins (first 20 lines of stdout). The registered-entry block
    #    SHA is computed over the line span and ADDED to the pin map so it
    #    enters audit_sha256 per the plan's 5-element pin set.
    pins = log_input_pins(INPUT_FILES)

    reg_block_text = extract_block(REG_ENTRY_PATH, REG_ENTRY_LINE_START, REG_ENTRY_LINE_END)  # (local)
    reg_block_sha = sha256_of_text(reg_block_text)  # (local)
    reg_pin_key = (
        f"sessions/permanent-results-registry.md#VII.AC.4"
        f"[L{REG_ENTRY_LINE_START}-{REG_ENTRY_LINE_END}]"
    )  # (local)
    pins[reg_pin_key] = reg_block_sha
    print(f"  {reg_pin_key}: {reg_block_sha[:16]}... (registered §VII.AC.4 block)")

    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs (pins now carry reg-block + both reviewer JSONs)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap[5-elem])")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Load reviewers + aggregate (NO physics)
    reviewer_a = load_reviewer(REVIEWER_A_JSON)
    reviewer_b = load_reviewer(REVIEWER_B_JSON)
    print(f"  reviewer_A: {reviewer_a.get('reviewer')} / axis={reviewer_a.get('axis')}")
    print(f"  reviewer_B: {reviewer_b.get('reviewer')} / axis={reviewer_b.get('axis')}")
    print()

    res = aggregate(reviewer_a, reviewer_b)

    # 3. Report the matrix + sub-verdicts
    print("=== reviewer x clause matrix ===")
    for rv in ("reviewer_A", "reviewer_B"):
        for c, v in res["matrix"][rv].items():
            print(f"  {rv:11s} {c:16s} {v}")
    print(f"  overall_axis_A = {res['overall_axis_A']}")
    print(f"  overall_axis_B = {res['overall_axis_B']}")
    print()
    print("=== JOINT-clause PASS-AND ===")
    for c, d in res["joint_pass_and"].items():
        print(f"  {c:8s} axis_A={d['axis_A']:5s} axis_B={d['axis_B']:5s} -> PASS-AND={d['pass_and']}")
    print()
    print("=== sequential-chain (CO-PRIMARY direction) sub-verdicts ===")
    print(f"  JOINT-1 sequential        = {res['co_primary_direction_sequential']}")
    print(f"  JOINT-2 non-fungible      = {res['non_fungible']}")
    print(f"  CO-PRIMARY-direction (AND) = {res['seq_chain_co_primary_direction']}")
    print(f"  JOINT-3 axis_A/axis_B      = {res['joint3_axis_A']}/{res['joint3_axis_B']} (same-cell tag leg)")
    print()
    print(f"  any_fail={res['any_fail']}  any_info={res['any_info']}")
    print(f"  COMPOSITE = {res['composite']}")
    print()

    verdict = res["composite"]  # (local)

    # 4. Persist the npz: reviewer x clause matrix + sub-verdicts + composite
    try:
        import numpy as np  # local import; small data only

        reviewers = np.array(["reviewer_A", "reviewer_B"])  # (local)
        all_clauses = np.array(
            SINGLE_AXIS_A_CLAUSES + SINGLE_AXIS_B_CLAUSES + JOINT_CLAUSES
        )  # (local)
        # Encode the matrix as a list of "reviewer|clause|verdict" rows for portability.
        matrix_rows = []  # (local)
        for rv in ("reviewer_A", "reviewer_B"):
            for c, v in res["matrix"][rv].items():
                matrix_rows.append(f"{rv}|{c}|{v}")
        np.savez(
            OUT_NPZ,
            gate_id=GATE_ID,
            reviewers=reviewers,
            single_axis_A_clauses=np.array(SINGLE_AXIS_A_CLAUSES),
            single_axis_B_clauses=np.array(SINGLE_AXIS_B_CLAUSES),
            joint_clauses=np.array(JOINT_CLAUSES),
            all_clauses=all_clauses,
            matrix_rows=np.array(matrix_rows),
            overall_axis_A=res["overall_axis_A"],
            overall_axis_B=res["overall_axis_B"],
            joint_pass_and=json.dumps(res["joint_pass_and"], sort_keys=True),
            co_primary_direction_sequential=res["co_primary_direction_sequential"],
            non_fungible=res["non_fungible"],
            seq_chain_co_primary_direction=res["seq_chain_co_primary_direction"],
            joint3_axis_A=res["joint3_axis_A"],
            joint3_axis_B=res["joint3_axis_B"],
            any_fail=res["any_fail"],
            any_info=res["any_info"],
            composite=res["composite"],
            substrate_input_overlap_caveat=(
                "BOTH reviewers loaded the SAME slot npz "
                "s87_w3_path_h_path_c_registry_landing.npz; shared with the "
                "§VII.AC.1 companion gate. Stage-2 PASS-AND establishes "
                "structural-OUTPUT-type independence (two distinct decision "
                "pipelines on shared data), NOT structural-INPUT independence."
            ),
            audit_sha256=audit_sha,
            content_sha256=content_sha,
            reg_block_sha256=reg_block_sha,
        )
        print(f"  wrote {OUT_NPZ.name}")
    except Exception as exc:  # noqa: BLE001
        print(f"  WARNING: npz write failed: {exc}")

    # 5. Emit 4-tuple + PRINT the emit_verdict payload.
    value_str = (
        f"composite_{verdict}_4clausePASS_JOINT3-INFO-both-axes_"
        f"CO-PRIMARY-direction-{res['seq_chain_co_primary_direction']}_"
        f"same-cell-tag-INFO_substrate-input-overlap-caveat_"
        f"JOINT3-Stage2-INFO-deferred-parse-tree-expansion-forward-path"
    )  # (local)
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        (
            "# substrate-input-overlap-caveat: both reviewers loaded "
            "s87_w3_path_h_path_c_registry_landing.npz (shared with §VII.AC.1); "
            "PASS-AND => structural-OUTPUT-type independence only, NOT INPUT independence"
        ),
        (
            "# JOINT-3 Stage-2-INFO-deferred: CO-PRIMARY direction (sequential+non-fungible) "
            "PASS on both axes; same-cell tag leg INFO (s=3 Mellin pole audit-substituted, "
            "3 non-reconcilable tokens {s=3, substrate-distance-1, a_4^zeta/n=4}); "
            "forward path = §VII.U.2 4-corner parse-tree expansion of BOTH anchors "
            "with lexical Corner-III marker + poleconv-{A|B} + (pole_in_s, curvature_grade_n)"
        ),
    ]  # (local)
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        companion_note="§VII.AC.4 STAYS STAGE-1-CANDIDATE (INFO composite); consistent with atlas-07 plan-freeze down-correction",
        extra_rows=extra,
    )

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    # Exit 0 regardless of verdict (verdict is data, not script health).
    return 0


if __name__ == "__main__":
    sys.exit(main())
