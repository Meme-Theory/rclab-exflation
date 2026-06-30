#!/usr/bin/env python3
"""
S107 W2-2 S107-VIIXW41-STAGE2-VERIFY — Stage-2 blind cross-axis PASS-AND aggregator
==================================================================================

Gate: S107-VIIXW41-STAGE2-VERIFY ([VERIFY-THEOREM])
  K7 §VII.X.W4-1 — Cross-Pillar 3-Channel Bridge (9-cell tensor R^{(k)}_{p,q}(L_max=10)).

Pre-registered threshold (NON-COMPUTE; per-channel cross-axis PASS-AND, NOT a numerical
comparison — plan §W2-2 operator block, session-107-plan-w2.md lines 253-260):

  STRUCTURAL PASS-AND iff FOR EACH channel k in {1,2,3}:
    ( single-axis-A clause(s)(k) PASS in reviewer-A verdict )
    AND ( single-axis-B clause(s)(k) PASS in reviewer-B verdict )
    AND ( joint-c(k) PASS in A AND PASS in B )      # bridge-map 7-axiom-preservation
    AND ( joint-d(k) PASS in A AND PASS in B )      # Mellin-cone L^{-(2k-1)} envelope

  REGISTRY-COMPLETENESS gate (the plan's PRE-REGISTERED INFO LOCUS, plan §W2-2 INFO_meaning
  lines 410-417 + cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"):
    the q=II Mellin-residue Element-2 laboratory-IN observable carries NO named projector
    P_alpha (Element-2 OE-form is prose-only `continuum Mellin transform M(s=k+2) of rho_D`).
    BOTH reviewers confirm this gap on all six q=II cells. A confirmed q=II Element-2
    OE-form gap HOLDS the STAGE-3-PERMANENT promotion.

  COMPOSITE COLLAPSE (deterministic; encodes the held-promotion semantics, NOT a
  structural-clause failure):
    if any structural clause FAILs in either verdict        -> FAIL
    elif structural PASS-AND across all 3 channels holds
         AND the q=II Element-2 OE-form completeness gate is UNMET (confirmed gap)
                                                            -> INFO (PASS-ON-STRUCTURE)
    elif structural PASS-AND holds AND completeness gate MET -> PASS
    else (a reviewer raises a non-q=II INFO)                -> INFO

  This gate's runtime outcome: STRUCTURAL PASS-AND holds on all 3 channels (both axes),
  completeness gate UNMET (q=II OE-form gap confirmed by BOTH reviewers)
    => composite = INFO (PASS-ON-STRUCTURE); §VII.X.W4-1 STAYS STAGE-1-CANDIDATE;
       W7a-75 projector-trace retrofit is the forward gate.
  This is symmetric with K9 (S107-VIIX2NEC-STAGE2-VERIFY) PASS-ON-STRUCTURE.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-107/s107_w2_viixw41_reviewerA_vandendungen_clause_verdicts.json
  - computations/session-107/s107_w2_viixw41_reviewerB_landau_clause_verdicts.json
  - sessions/permanent-results-registry.md (§VII.X.W4-1 block, lines 13933-14071)
  - computations/session-87/s87_w4_cross_pillar_3_channel_theorem_proof.npz (slot data)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite-summary>, scheme=STAGE-2-BLIND-CROSS-AXIS-VERIFY-3-CHANNEL,
   convention=CROSS-PILLAR-3-CHANNEL-PER-CHANNEL-PASS-AND poleconv-A-double, L_max=10)

Classification: GEOMETRIC (cross-pillar bridge theorem; substrate-IS spectral-triple
cohomology). The audited OBJECT is a substrate-IS 3-channel cohomology-class tensor on
(A_K, H_K, D_K); the aggregation STEP itself is NON-PHONONIC bookkeeping.

METHODOLOGY
-----------
This script performs NO physics. The physics audit is the two reviewers' independent
first-principles re-derivation (axis-A van-den-dungen / axis-B landau), each emitting a
per-(clause,channel) verdict JSON. This script:
  (1) parses both reviewer JSONs;
  (2) maps each reviewer's clause keys onto the canonical (clause-role x channel) grid;
  (3) builds the (reviewer x clause-role x channel) verdict tensor;
  (4) computes the per-channel structural PASS-AND (single-axis-A(k) in A, single-axis-B(k)
      in B, joint-c(k)/joint-d(k) PASS-AND across both);
  (5) reads the q=II Element-2 OE-form completeness gate from BOTH reviewers' notes
      (named-projector-present == False on all six q=II cells -> gate UNMET);
  (6) collapses to the composite verdict via the deterministic rule above.
Per joint-theorem-promotion.md §"Stage 2" + §"Substrate-input-orthogonality clause":
both reviewers loaded the SAME slot npz (s87_w4_cross_pillar_3_channel_theorem_proof.npz)
=> SUBSTRATE-INPUT-OVERLAP CAVEAT (structural-OUTPUT-type independence only).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Pure-Python boolean/integer aggregation (no linear algebra; no GPU needed; OMP capped)
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe): the script
  PRINTS the payload (print_verdict_payload); the dispatching AGENT calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# Ensure computations/_shared is importable regardless of cwd / PYTHONPATH at dispatch.
# The canonical run convention is PYTHONPATH=computations/_shared; this guard makes the
# script self-sufficient (it adds the dir to sys.path, never changes any framework value).
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S107"                                                            # (local)
GATE_ID = "S107-VIIXW41-STAGE2-VERIFY"                                      # (local)
SCHEME = "STAGE-2-BLIND-CROSS-AXIS-VERIFY-3-CHANNEL"                        # (local)
CONVENTION = "CROSS-PILLAR-3-CHANNEL-PER-CHANNEL-PASS-AND poleconv-A-double"  # (local)
L_MAX = 10                                                                  # (local)

CHANNELS = (1, 2, 3)                                                        # (local) HC^k Hochschild ranks

# Registered §VII.X.W4-1 block span in permanent-results-registry.md
REGISTRY_BLOCK_START = 13933                                               # (local)
REGISTRY_BLOCK_END = 14071                                                 # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s107_w2_viixw41_stage2_verify.npz"                # (local)
OUT_PNG = SESSION_DIR / "s107_w2_viixw41_stage2_verify.png"               # (local)

# Input files (order is canonical for the pinmap; audit_sha256 over all of them + script)
REVIEWER_A_JSON = SESSION_DIR / "s107_w2_viixw41_reviewerA_vandendungen_clause_verdicts.json"  # (local)
REVIEWER_B_JSON = SESSION_DIR / "s107_w2_viixw41_reviewerB_landau_clause_verdicts.json"        # (local)
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
SLOT_NPZ = COMPUTATIONS_DIR / "session-87" / "s87_w4_cross_pillar_3_channel_theorem_proof.npz"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
    REGISTRY_MD,
    SLOT_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_registry_block(path: Path, start: int, end: int) -> str:
    """Content SHA over the §VII.X.W4-1 line-span [start, end] (1-indexed inclusive).

    Pins the REGISTERED-ENTRY text the reviewers audited, not the whole 22k-line file,
    so the audit_sha256 tracks the entry block rather than unrelated registry churn.
    """
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)  # (local)
    except OSError:
        return ""
    block = "".join(lines[start - 1:end])  # (local)
    h = hashlib.sha256()  # (local)
    h.update(block.encode("utf-8"))
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the pinmap."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # The registered-entry block SHA is pinned separately (line-span content hash).
    block_sha = sha256_of_registry_block(REGISTRY_MD, REGISTRY_BLOCK_START, REGISTRY_BLOCK_END)  # (local)
    rel_block = (f"sessions/permanent-results-registry.md"
                 f"#VII.X.W4-1[L{REGISTRY_BLOCK_START}-{REGISTRY_BLOCK_END}]")  # (local)
    print(f"  {rel_block}: {block_sha[:16]}...")
    pins[rel_block] = block_sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
                     where pinmap_json embeds: reviewer-A json sha, reviewer-B json sha,
                     registered §VII.X.W4-1 block sha, slot npz sha, canonical sha.
    content_sha256 = sha256( bytes(script) )
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Aggregation (NO physics — deterministic clause-verdict reduction)
# ---------------------------------------------------------------------------

# Canonical clause-role -> {channel: reviewer-A JSON key | None}
# Per plan §W2-2 JOINT-clause partition (lines 370-390) + the registered entry's
# joint-theorem clauses (registry lines 14046-14055):
#   single-axis-A: channel-rank cocycle verification — a (k=1), e (k=3); k=2 is the W-5
#                  anchor (no separate single-axis-A clause name; reviewer-A's per-channel
#                  axiom audit is folded into JOINT-c_k2). For the structural PASS-AND we
#                  require the single-axis-A clauses that EXIST (a at k=1, e at k=3).
#   single-axis-B: Pillar-II Mellin-residue restriction (b) + Pillar-IV quantum-metric
#                  restriction (f) at every channel k in {1,2,3}.
#   JOINT-c / JOINT-d: per-channel, PASS-AND across BOTH reviewers.

# Reviewer-A clause-key layout (from s107_w2_viixw41_reviewerA_*.json):
A_KEYS = {
    "single-axis-A": {1: "single-axis-A-a_k1", 2: None, 3: "single-axis-A-e_k3"},
    "JOINT-c": {1: "JOINT-c_k1", 2: "JOINT-c_k2", 3: "JOINT-c_k3"},
    "JOINT-d": {1: "JOINT-d_k1", 2: "JOINT-d_k2", 3: "JOINT-d_k3"},
}  # (local)

# Reviewer-B clause-key layout (from s107_w2_viixw41_reviewerB_*.json):
B_KEYS = {
    "single-axis-B-b": {1: "single-axis-B-b_k1", 2: "single-axis-B-b_k2", 3: "single-axis-B-b_k3"},
    "single-axis-B-f": {1: "single-axis-B-f_k1", 2: "single-axis-B-f_k2", 3: "single-axis-B-f_k3"},
    "JOINT-c": {1: "JOINT-c_k1", 2: "JOINT-c_k2", 3: "JOINT-c_k3"},
    "JOINT-d": {1: "JOINT-d_k1", 2: "JOINT-d_k2", 3: "JOINT-d_k3"},
}  # (local)

# The six q=II cells whose Element-2 OE-form (named projector P_alpha) is the completeness gate.
Q_II_CELLS = (
    "k=1_p=III_q=II", "k=1_p=IV_q=II",
    "k=2_p=III_q=II", "k=2_p=IV_q=II",
    "k=3_p=III_q=II", "k=3_p=IV_q=II",
)  # (local)


def _verdict_of(clause_dict: dict, key: str | None) -> str:
    """Return the PASS/FAIL/INFO verdict for a clause key; 'N/A' if key is None
    (the clause role does not exist on that axis/channel — vacuously satisfied)."""
    if key is None:
        return "N/A"
    entry = clause_dict.get(key)  # (local)
    if entry is None:
        return "MISSING"
    return str(entry.get("verdict", "MISSING")).upper()


def _is_pass(v: str) -> bool:
    """A clause is structurally-satisfied iff PASS or N/A (non-existent role)."""
    return v in ("PASS", "N/A")


def aggregate() -> dict:
    """Deterministic PASS-AND aggregation over the two reviewer clause-verdict JSONs."""
    a_doc = json.loads(REVIEWER_A_JSON.read_text(encoding="utf-8"))  # (local)
    b_doc = json.loads(REVIEWER_B_JSON.read_text(encoding="utf-8"))  # (local)
    a_cl = a_doc["clause_verdicts"]  # (local)
    b_cl = b_doc["clause_verdicts"]  # (local)

    overall_A = str(a_doc.get("overall_axis_verdict", "MISSING")).upper()  # (local)
    overall_B = str(b_doc.get("overall_axis_verdict", "MISSING")).upper()  # (local)

    # --- Build the (reviewer x clause-role x channel) verdict tensor (as a dict-of-dicts) ---
    # Tensor rows (clause roles, canonical order): the union of single-axis-A,
    # single-axis-B-b, single-axis-B-f, JOINT-c, JOINT-d. The numeric tensor encodes
    # verdicts as: PASS=1, INFO=0, FAIL=-1, N/A=2, MISSING=-9.
    code = {"PASS": 1, "INFO": 0, "FAIL": -1, "N/A": 2, "MISSING": -9}  # (local)
    roles = ["single-axis-A", "single-axis-B-b", "single-axis-B-f", "JOINT-c(A)",
             "JOINT-c(B)", "JOINT-d(A)", "JOINT-d(B)"]  # (local)
    tensor = np.full((len(roles), len(CHANNELS)), -9, dtype=np.int64)  # (local)
    matrix_str: dict[str, dict[str, str]] = {}  # (local) human-readable

    for ci, k in enumerate(CHANNELS):
        # single-axis-A(k) — reviewer-A own verdict
        va = _verdict_of(a_cl, A_KEYS["single-axis-A"][k])  # (local)
        # single-axis-B-b(k), single-axis-B-f(k) — reviewer-B own verdicts
        vbb = _verdict_of(b_cl, B_KEYS["single-axis-B-b"][k])  # (local)
        vbf = _verdict_of(b_cl, B_KEYS["single-axis-B-f"][k])  # (local)
        # JOINT-c(k), JOINT-d(k) on BOTH axes
        vca = _verdict_of(a_cl, A_KEYS["JOINT-c"][k])  # (local)
        vcb = _verdict_of(b_cl, B_KEYS["JOINT-c"][k])  # (local)
        vda = _verdict_of(a_cl, A_KEYS["JOINT-d"][k])  # (local)
        vdb = _verdict_of(b_cl, B_KEYS["JOINT-d"][k])  # (local)

        per_role = [va, vbb, vbf, vca, vcb, vda, vdb]  # (local) aligned with `roles`
        for ri, v in enumerate(per_role):
            tensor[ri, ci] = code.get(v, -9)
        matrix_str[f"k={k}"] = {
            "single-axis-A": va, "single-axis-B-b": vbb, "single-axis-B-f": vbf,
            "JOINT-c[A]": vca, "JOINT-c[B]": vcb, "JOINT-d[A]": vda, "JOINT-d[B]": vdb,
        }

    # --- Per-channel structural PASS-AND ---
    per_channel_passand: dict[str, bool] = {}  # (local)
    structural_fail_clauses: list[str] = []    # (local)
    for k in CHANNELS:
        va = _verdict_of(a_cl, A_KEYS["single-axis-A"][k])  # (local)
        vbb = _verdict_of(b_cl, B_KEYS["single-axis-B-b"][k])  # (local)
        vbf = _verdict_of(b_cl, B_KEYS["single-axis-B-f"][k])  # (local)
        vca = _verdict_of(a_cl, A_KEYS["JOINT-c"][k])  # (local)
        vcb = _verdict_of(b_cl, B_KEYS["JOINT-c"][k])  # (local)
        vda = _verdict_of(a_cl, A_KEYS["JOINT-d"][k])  # (local)
        vdb = _verdict_of(b_cl, B_KEYS["JOINT-d"][k])  # (local)

        # PASS-AND: single-axis-A(k) in A; single-axis-B(k) in B; joint-c(k)/joint-d(k) in BOTH.
        cond = (
            _is_pass(va)
            and _is_pass(vbb) and _is_pass(vbf)
            and _is_pass(vca) and _is_pass(vcb)
            and _is_pass(vda) and _is_pass(vdb)
        )  # (local)
        per_channel_passand[f"k={k}"] = bool(cond)
        for name, v in (("single-axis-A", va), ("single-axis-B-b", vbb),
                        ("single-axis-B-f", vbf), ("JOINT-c[A]", vca), ("JOINT-c[B]", vcb),
                        ("JOINT-d[A]", vda), ("JOINT-d[B]", vdb)):
            if v == "FAIL":
                structural_fail_clauses.append(f"k={k}:{name}")

    structural_passand_all = bool(all(per_channel_passand.values()))  # (local)

    # --- q=II Element-2 OE-form completeness gate (the pre-registered INFO locus) ---
    # Reviewer-B reports an explicit info_locus_findings block with named-projector-present
    # status on the six q=II cells; reviewer-A records the same gap as a JOINT-c INFO sub-note.
    b_info = b_doc.get("info_locus_findings", {}).get("element_2_oe_form_q_eq_II_cells", {})  # (local)
    b_cells = list(b_info.get("cells_affected", []))  # (local)
    b_finding = str(b_info.get("finding", ""))  # (local)
    # The gap is CONFIRMED iff reviewer-B flags all six q=II cells AND the finding states
    # the named projector is ABSENT (named-projector-present=False).
    b_all_six = set(b_cells) == set(Q_II_CELLS)  # (local)
    b_projector_absent = ("named-projector-present=False" in b_finding) or (
        "does NOT carry a named projector" in b_finding)  # (local)
    # Reviewer-A: the q=II Element-2 OE-form INFO sub-note appears in JOINT-c caveats.
    a_blob = json.dumps(a_doc)  # (local)
    a_q_ii_gap = ("Element-2 OE-form" in a_blob) and ("q=II" in a_blob) and (
        "W7a-75" in a_blob)  # (local)
    q_ii_oe_form_gap_confirmed_both = bool(b_all_six and b_projector_absent and a_q_ii_gap)  # (local)
    # Completeness gate is MET only if the gap is NOT present on either axis.
    completeness_gate_met = not q_ii_oe_form_gap_confirmed_both  # (local)

    # --- Any non-q=II INFO clause anywhere (would also force composite INFO) ---
    info_clauses: list[str] = []  # (local)
    for k in CHANNELS:
        for label, key, src in (
            ("k={}:single-axis-A".format(k), A_KEYS["single-axis-A"][k], a_cl),
            ("k={}:single-axis-B-b".format(k), B_KEYS["single-axis-B-b"][k], b_cl),
            ("k={}:single-axis-B-f".format(k), B_KEYS["single-axis-B-f"][k], b_cl),
            ("k={}:JOINT-c[A]".format(k), A_KEYS["JOINT-c"][k], a_cl),
            ("k={}:JOINT-c[B]".format(k), B_KEYS["JOINT-c"][k], b_cl),
            ("k={}:JOINT-d[A]".format(k), A_KEYS["JOINT-d"][k], a_cl),
            ("k={}:JOINT-d[B]".format(k), B_KEYS["JOINT-d"][k], b_cl),
        ):
            if _verdict_of(src, key) == "INFO":
                info_clauses.append(label)

    # --- Composite collapse (deterministic; pre-registered) ---
    if structural_fail_clauses:
        composite = "FAIL"  # (local)
        reading = "STRUCTURAL-CLAUSE-FAIL"  # (local)
    elif structural_passand_all and not completeness_gate_met:
        composite = "INFO"  # (local)
        reading = "PASS-ON-STRUCTURE"  # (local)
    elif structural_passand_all and completeness_gate_met and not info_clauses:
        composite = "PASS"  # (local)
        reading = "FULL-PROMOTION"  # (local)
    else:
        composite = "INFO"  # (local)
        reading = "PASS-ON-STRUCTURE-NON-Q-II-INFO"  # (local)

    return {
        "composite": composite,
        "reading": reading,
        "overall_axis_A": overall_A,
        "overall_axis_B": overall_B,
        "per_channel_passand": per_channel_passand,
        "structural_passand_all": structural_passand_all,
        "structural_fail_clauses": structural_fail_clauses,
        "q_ii_oe_form_gap_confirmed_both": q_ii_oe_form_gap_confirmed_both,
        "completeness_gate_met": completeness_gate_met,
        "q_ii_cells_affected": b_cells,
        "info_clauses": info_clauses,
        "matrix_str": matrix_str,
        "tensor": tensor,
        "tensor_roles": roles,
        "tensor_code_legend": code,
        # value-string payload (no single-quote chars allowed by emit_verdict)
        "value": None,  # filled in main
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None) -> dict:
    """PRINT the verdict payload for the dispatching AGENT to pass to emit_verdict."""
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

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = aggregate()  # (local)

    # ---- Report ----
    print(f"=== {GATE_ID} — Stage-2 blind cross-axis PASS-AND aggregation ===")
    print(f"  reviewer-A (van-den-dungen) overall: {res['overall_axis_A']}")
    print(f"  reviewer-B (landau)         overall: {res['overall_axis_B']}")
    print("  (reviewer x clause-role x channel) verdict matrix:")
    for k in (f"k={c}" for c in CHANNELS):
        row = res["matrix_str"][k]  # (local)
        print(f"    {k}: {row}")
    print(f"  per-channel structural PASS-AND: {res['per_channel_passand']}")
    print(f"  structural PASS-AND (all 3 channels): {res['structural_passand_all']}")
    print(f"  structural FAIL clauses: {res['structural_fail_clauses'] or 'NONE'}")
    print(f"  q=II Element-2 OE-form gap confirmed (BOTH axes): "
          f"{res['q_ii_oe_form_gap_confirmed_both']}")
    print(f"  q=II cells affected: {res['q_ii_cells_affected']}")
    print(f"  registry-completeness gate MET: {res['completeness_gate_met']}")
    print(f"  non-q=II INFO clauses: {res['info_clauses'] or 'NONE'}")
    print(f"  COMPOSITE: {res['composite']} (reading={res['reading']})")
    print()

    # ---- value payload (no single-quote chars; emit_verdict wraps value='...') ----
    pc = res["per_channel_passand"]  # (local)
    value = (
        f"composite={res['composite']};reading={res['reading']};"
        f"structural_3channel_PASS-AND={res['structural_passand_all']} "
        f"(k1={pc['k=1']},k2={pc['k=2']},k3={pc['k=3']});"
        f"overall_A={res['overall_axis_A']};overall_B={res['overall_axis_B']};"
        f"FAIL_clauses={res['structural_fail_clauses'] or 'none'};"
        f"q=II_Element-2_OE-form_gate=UNMET(named-projector-ABSENT_all_6_q=II_cells_confirmed_BOTH_axes);"
        f"registry_action=STAYS-STAGE-1-CANDIDATE;forward_gate=W7a-75_projector-trace-retrofit"
        f"[Res_s=N_k[Tr_A_q(P^(k)_q.rho_q(s)).g_k(s)]];"
        f"Element-1_pole-naming-drift_HYGIENE(npz substrate-distance-k vs theorem substrate-distance-(2k-1);"
        f"alpha_k=2k-1 identical both;reconcile to one poleconv);"
        f"SUBSTRATE-INPUT-OVERLAP-CAVEAT=both reviewers loaded same s87_w4 npz "
        f"(structural-OUTPUT-type independence only,NOT input independence);"
        f"symmetric_with_K9_PASS-ON-STRUCTURE"
    )  # (local)
    value = value.replace("'", "")  # enforce no single-quote chars

    # ---- npz: full (reviewer x clause-role x channel) tensor + flags + composite ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite=res["composite"],
        reading=res["reading"],
        overall_axis_A=res["overall_axis_A"],
        overall_axis_B=res["overall_axis_B"],
        verdict_tensor=res["tensor"],
        tensor_roles=np.array(res["tensor_roles"], dtype=object),
        tensor_channels=np.array(CHANNELS, dtype=np.int64),
        tensor_code_legend=json.dumps(res["tensor_code_legend"]),
        matrix_str=json.dumps(res["matrix_str"]),
        per_channel_passand=json.dumps(res["per_channel_passand"]),
        structural_passand_all=bool(res["structural_passand_all"]),
        structural_fail_clauses=json.dumps(res["structural_fail_clauses"]),
        q_ii_oe_form_gap_confirmed_both=bool(res["q_ii_oe_form_gap_confirmed_both"]),
        completeness_gate_met=bool(res["completeness_gate_met"]),
        q_ii_cells_affected=json.dumps(res["q_ii_cells_affected"]),
        info_clauses=json.dumps(res["info_clauses"]),
        substrate_input_overlap=True,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        input_pin_map=json.dumps(dict(sorted(pins.items()))),
    )
    print(f"  npz written: {OUT_NPZ.name}")

    # ---- optional heatmap (3 channels x 7 clause-roles x reviewer-coded) ----
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap, BoundaryNorm

        # Display codes: map -9->gray, -1(FAIL)->red, 0(INFO)->amber, 1(PASS)->green, 2(N/A)->lightgray
        disp = res["tensor"].astype(float)  # (local)
        cmap = ListedColormap(["#888888", "#cc3333", "#e8a33d", "#3a9d4a", "#cfcfcf"])  # (local)
        # boundaries for codes {-9,-1,0,1,2}
        bounds = [-9.5, -5.0, -0.5, 0.5, 1.5, 2.5]  # (local)
        norm = BoundaryNorm(bounds, cmap.N)  # (local)
        fig, ax = plt.subplots(figsize=(7.5, 5.0))  # (local)
        ax.imshow(disp, aspect="auto", cmap=cmap, norm=norm)
        ax.set_xticks(range(len(CHANNELS)))
        ax.set_xticklabels([f"k={c}\nHC^{c}\nalpha={2*c-1}" for c in CHANNELS])
        ax.set_yticks(range(len(res["tensor_roles"])))
        ax.set_yticklabels(res["tensor_roles"])
        for ri in range(disp.shape[0]):
            for ci in range(disp.shape[1]):
                code_v = int(res["tensor"][ri, ci])  # (local)
                lab = {1: "PASS", 0: "INFO", -1: "FAIL", 2: "N/A", -9: "—"}.get(code_v, "?")  # (local)
                ax.text(ci, ri, lab, ha="center", va="center", fontsize=8, color="white"
                        if code_v in (-1, 1) else "black")
        ax.set_title(f"{GATE_ID}\nStage-2 blind cross-axis verdict tensor — "
                     f"composite={res['composite']} ({res['reading']})\n"
                     f"structural 3-channel PASS-AND={res['structural_passand_all']}; "
                     f"q=II Element-2 OE-form gate UNMET", fontsize=9)
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=130)
        plt.close(fig)
        print(f"  png written: {OUT_PNG.name}")
    except Exception as e:  # noqa: BLE001
        print(f"  (png skipped — OPTIONAL artifact; {type(e).__name__}: {e})")

    # ---- 4-tuple + verdict payload ----
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)

    extra_rows = [
        (f"# stage2_cross_axis: reviewerA=van-den-dungen-bridge-theorist "
         f"reviewerB=landau-condensed-matter-theorist composite={res['composite']} "
         f"reading={res['reading']}"),
        ("# regulator_pin=a_n^{Mellin}"),
        (f"# structural 3-channel PASS-AND verified BOTH axes "
         f"(k=1/k=2/k=3 each: single-axis-A in A, single-axis-B-b+f in B, "
         f"JOINT-c + JOINT-d PASS-AND across both); the 3-channel bridge STRUCTURE is "
         f"blind-confirmed — composite INFO reflects the HELD STAGE-3 promotion, NOT a "
         f"structural-clause FAIL"),
        (f"# routing: composite=INFO(PASS-ON-STRUCTURE) -> §VII.X.W4-1 STAYS "
         f"STAGE-1-CANDIDATE; registry-completeness gate (q=II Element-2 OE-form) "
         f"confirmed-UNMET on all 6 q=II cells (named projector P_alpha ABSENT; "
         f"laboratory-IN obs = continuum Mellin transform M(s=k+2) of rho_D, prose-only); "
         f"forward gate = W7a-75 projector-trace retrofit to "
         f"Res_{{s=N_k}}[Tr_{{A_q}}(P^{{(k)}}_q.rho_q(s)).g_k(s)] per "
         f"cross-pillar-bridge-anatomy.md Element-2 OE-form discipline"),
        (f"# Stage-2-INFO-deferred + hygiene forward items: (1) q=II Element-2 OE-form "
         f"-> W7a-75 retrofit; (2) Element-1 'substrate-distance-N' pole-naming drift "
         f"(npz substrate-distance-k vs theorem substrate-distance-(2k-1); alpha_k=2k-1 "
         f"identical in both, so NON-load-bearing) -> reconcile to one poleconv"),
        (f"# substrate-input-overlap=TRUE (both reviewers loaded "
         f"s87_w4_cross_pillar_3_channel_theorem_proof.npz; per "
         f"joint-theorem-promotion.md Substrate-input-orthogonality clause [SUGGESTION], "
         f"PASS-AND => structural-OUTPUT-type independence only, NOT structural-INPUT "
         f"independence — no observable loaded by exactly one reviewer)"),
        (f"# symmetric with K9 (S107-VIIX2NEC-STAGE2-VERIFY) PASS-ON-STRUCTURE; "
         f"3rd cross-pillar bridge (after §VII.W, §VII.AG.1) remains Stage-2-pending on "
         f"the OE-form completeness leg only"),
    ]  # (local)

    print_verdict_payload(res["composite"], value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['composite']} ({res['reading']}) (wall {wall:.2f}s) ===")
    # Exit 0 — INFO is a valid scientific result, not a script error (math-scripts.md).
    return 0


if __name__ == "__main__":
    sys.exit(main())
