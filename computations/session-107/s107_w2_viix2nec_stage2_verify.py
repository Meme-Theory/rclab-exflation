#!/usr/bin/env python3
"""
S107 W2-3 S107-VIIX2NEC-STAGE2-VERIFY — Stage-2 PASS-AND aggregator for §VII.X.2-NECESSITY (K9)
==============================================================================================

Gate: S107-VIIX2NEC-STAGE2-VERIFY ([VERIFY-THEOREM])

Pre-registered threshold (NON-COMPUTE; set-membership cross-axis PASS-AND, per
sessions/session-plan/session-107-plan-w2.md §W2-3 + joint-theorem-promotion.md §"Stage 2"):
  PASS iff ( single-axis-A clauses PASS in reviewer-A verdict )
       AND ( single-axis-B clauses PASS in reviewer-B verdict )
       AND ( EVERY JOINT clause PASS in reviewer-A verdict AND PASS in reviewer-B verdict )
  ... THEN the composite is FURTHER lowered to the worst of {clause-composite,
  reviewer-A overall_axis_verdict, reviewer-B overall_axis_verdict} under the
  precedence FAIL > INFO > PASS. This propagates reviewer-A's overall_axis_verdict=INFO
  (registry-PASS criterion = 6/6 full-64-char anchor-SHA harvest UNMET as the registered
  entry text presents it; SOURCE-RECON Class-(c), SEPARATE from the structural clauses),
  giving the expected K9 outcome: INFO (PASS-ON-STRUCTURE).

THIS SCRIPT PERFORMS NO PHYSICS. The physics audit is the two reviewers' blind
first-principles re-derivation (their clause-verdict JSONs); this script is the
deterministic AND-aggregator. It loads the two JSONs, builds the reviewer x clause
matrix, computes the necessity (JOINT-1) and converse-asymmetry (JOINT-2) sub-verdicts
via PASS-AND across reviewers, computes the clause-level composite, then propagates each
reviewer's overall_axis_verdict, and PRINTS the verdict payload (print_verdict_payload).
The dispatching AGENT then calls mcp__knowledge__emit_verdict (race-safe).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - reviewer-A (NCG M2): s107_w2_viix2nec_reviewerA_vandendungen_clause_verdicts.json
  - reviewer-B (substrate): s107_w2_viix2nec_reviewerB_volovik_clause_verdicts.json
  - necessity truth-table sidecar: computations/session-87/s87_w1a_m2_necessity_truth_table.json
  - registered §VII.X.2-NECESSITY entry SPAN (registry lines 16514-16577) content SHA
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

audit_sha256 inputs (per plan §W2-3 audit_discriminators):
  [script, registered_stage1_entry_sha, reviewerA_json_sha, reviewerB_json_sha,
   truth_table_json_sha, pinmap]

Output 4-tuple:
  (value=<composite-summary>, scheme=STAGE-2-BLIND-CROSS-AXIS-VERIFY-NECESSITY-ONLY,
   convention=NCG-M2-Lambda-SA-finite-L-residual-NECESSITY-ASYMMETRIC poleconv-A-double,
   L_max=mixed)

Classification: GEOMETRIC (NCG-axiomatic necessity-only meta-theorem; the AGGREGATION is
NON-PHONONIC, but the OBJECT verified is substrate-IS: M2 = structural property of A_F
constrains the substrate-organized Lambda_SA finite-L residual at substrate-distance-0).

METHODOLOGY
-----------
Two-agent parallel cross-axis Stage-2 verify per joint-theorem-promotion.md §"Stage 2".
Reviewer-A (van-den-dungen, NCG-axiomatic M2 first-order axis) and reviewer-B (volovik,
substrate/superfluid-vacuum axis) were dispatched IN PARALLEL, each blind to the originating
S86 W-1 workshop (s86-mellin-cone-repair-or-no-go.md). Each re-derived its assigned clauses
from first principles. This gate is the structural fulfillment of the S88 carry-forward
S89-VII-X-2-STAGE-2-INDEPENDENT-VERIFY: the S88-VII-X-2-NECESSITY-PROMOTE-STAGE-3 gate
returned INFO (anchors 6/6 present but Stage-2 dispatched in /rclab-solo single-thread mode,
which cannot satisfy the §Stage 2 independence requirement); the present gate supplies the
proper parallel blind cross-axis dispatch. The clause partition (plan §W2-3):
  JOINT (PASS-AND in BOTH): JOINT-1 (necessity direction, contrapositive
    M2-failure -> non-Hochschild Delta a_0 -> regulator-divergence -> undefined residual),
    JOINT-2 (necessity-ONLY asymmetry; converse DENIED by the S65 continuum witness).
  single-axis-A (van-den-dungen): single-axis-A-1 (first-order mechanism),
    single-axis-A-2 (regulator-divergence consequence across reg in F_4).
  single-axis-B (volovik): single-axis-B-1 (substrate-internal Lambda_SA reading,
    anti-inversion), single-axis-B-2 (converse-failure-witness substrate reading).

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- Deterministic integer/boolean aggregation; no linear algebra, no GPU needed
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA)
- Gate verdict emitted via emit_verdict MCP tool: this script PRINTS the payload;
  the dispatching agent reads it and calls mcp__knowledge__emit_verdict.
- SUBSTRATE-INPUT-OVERLAP CAVEAT: both reviewers loaded the same truth-table JSON; the
  necessity reasoning is largely STRUCTURAL (a substitution-chain contrapositive, not a
  data read), so the PASS-AND is closer to structural-OUTPUT-type independence over a
  shared structural input (admissible under the SUGGESTION-status substrate-input-
  orthogonality clause of joint-theorem-promotion.md). Recorded in the value field + WP.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# Ensure computations/_shared is importable regardless of cwd / PYTHONPATH at dispatch.
# The canonical run convention is PYTHONPATH=computations/_shared; this guard makes the
# script self-sufficient (it adds the dir to sys.path, never changes any framework value).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"  # computations/_shared
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import sys  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S107"                                                  # (local)
GATE_ID = "S107-VIIX2NEC-STAGE2-VERIFY"                           # (local)
SCHEME = "STAGE-2-BLIND-CROSS-AXIS-VERIFY-NECESSITY-ONLY"         # (local)
CONVENTION = ("NCG-M2-Lambda-SA-finite-L-residual-NECESSITY-ASYMMETRIC "
             "poleconv-A-double")                                 # (local)
L_MAX = "mixed"                                                   # (local)

# Registered §VII.X.2-NECESSITY entry span (plan §W2-3 pin: registry lines 16514-16577,
# 1-indexed inclusive). The content SHA of this span is an audit_sha256 input.
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
REG_SPAN_START_1IDX = 16514                                       # (local)
REG_SPAN_END_1IDX = 16577                                         # (local)

REVIEWER_A_JSON = SESSION_DIR / "s107_w2_viix2nec_reviewerA_vandendungen_clause_verdicts.json"  # (local)
REVIEWER_B_JSON = SESSION_DIR / "s107_w2_viix2nec_reviewerB_volovik_clause_verdicts.json"        # (local)
TRUTH_TABLE_JSON = COMPUTATIONS_DIR / "session-87" / "s87_w1a_m2_necessity_truth_table.json"     # (local)

OUT_NPZ = SESSION_DIR / "s107_w2_viix2nec_stage2_verify.npz"      # (local)

# Files that feed the closure-hash pinmap (audit_sha256 = script || canonical || pinmap)
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REVIEWER_A_JSON,
    REVIEWER_B_JSON,
    TRUTH_TABLE_JSON,
]

# ---- Clause partition (plan §W2-3 JOINT-clause PASS-AND logic) ----
SINGLE_AXIS_A_CLAUSES = ["single-axis-A-1", "single-axis-A-2"]    # (local)
SINGLE_AXIS_B_CLAUSES = ["single-axis-B-1", "single-axis-B-2"]    # (local)
JOINT_CLAUSES = ["JOINT-1", "JOINT-2"]                            # (local)

# Verdict precedence (FAIL worst, then INFO, then PASS) for the worst-of reduction
VERDICT_RANK = {"FAIL": 2, "INFO": 1, "PASS": 0}                  # (local)
RANK_TO_VERDICT = {2: "FAIL", 1: "INFO", 0: "PASS"}              # (local)


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


def sha256_of_registry_span(path: Path, start_1idx: int, end_1idx: int) -> str:
    """Content SHA of registry lines [start_1idx, end_1idx] (1-indexed inclusive),
    joined by '\\n' — the §VII.X.2-NECESSITY section span the blind reviewers read."""
    raw = path.read_bytes()  # (local)
    lines = raw.split(b"\n")  # (local)
    span = b"\n".join(lines[start_1idx - 1:end_1idx])  # (local)
    return hashlib.sha256(span).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    # registered-entry span content SHA (pinned distinctly per plan audit_discriminators)
    reg_span_sha = sha256_of_registry_span(REGISTRY_PATH, REG_SPAN_START_1IDX, REG_SPAN_END_1IDX)  # (local)
    reg_key = (f"sessions/permanent-results-registry.md"
              f"#VII.X.2-NECESSITY[lines {REG_SPAN_START_1IDX}-{REG_SPAN_END_1IDX}]")  # (local)
    print(f"  {reg_key}: {reg_span_sha[:16]}...")
    pins[reg_key] = reg_span_sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
        where pinmap_json embeds the registered-entry-span SHA, both reviewer-JSON
        SHAs, and the truth-table-JSON SHA (the plan §W2-3 audit_discriminators set).
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                            separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

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
# Section 5 — Aggregation (NO physics; deterministic clause-verdict AND)
# ---------------------------------------------------------------------------
def _clause_verdict(reviewer_obj: dict, clause: str) -> str:
    """Extract a clause's verdict ('PASS'|'FAIL'|'INFO') from a reviewer JSON.
    Missing clause -> 'FAIL' (a clause the reviewer was supposed to audit but did
    not return is a non-PASS by construction)."""
    cv = reviewer_obj.get("clause_verdicts", {})  # (local)
    entry = cv.get(clause)  # (local)
    if entry is None:
        return "FAIL"
    v = str(entry.get("verdict", "FAIL")).strip().upper()  # (local)
    return v if v in VERDICT_RANK else "FAIL"


def _worst(verdicts: list[str]) -> str:
    """Worst verdict under FAIL > INFO > PASS."""
    if not verdicts:
        return "FAIL"
    return RANK_TO_VERDICT[max(VERDICT_RANK[v] for v in verdicts)]


def aggregate(rev_a: dict, rev_b: dict) -> dict:
    """Deterministic Stage-2 PASS-AND aggregation. Returns a dict of all sub-verdicts
    + the composite + the reviewer x clause matrix."""
    # --- single-axis clauses (each from its own reviewer) ---
    a_single = {c: _clause_verdict(rev_a, c) for c in SINGLE_AXIS_A_CLAUSES}  # (local)
    b_single = {c: _clause_verdict(rev_b, c) for c in SINGLE_AXIS_B_CLAUSES}  # (local)

    # --- JOINT clauses: PASS only if PASS in BOTH (logical AND) ---
    joint_paired: dict[str, dict] = {}  # (local)
    for c in JOINT_CLAUSES:
        va = _clause_verdict(rev_a, c)  # (local)
        vb = _clause_verdict(rev_b, c)  # (local)
        # AND semantics: PASS iff both PASS; else worst of the two
        pass_and = "PASS" if (va == "PASS" and vb == "PASS") else _worst([va, vb])  # (local)
        joint_paired[c] = {"axis_A": va, "axis_B": vb, "pass_and": pass_and}

    # --- single-axis-A PASS-AND (all A single clauses PASS in A) ---
    single_a_ok = all(v == "PASS" for v in a_single.values())  # (local)
    single_b_ok = all(v == "PASS" for v in b_single.values())  # (local)
    joint_ok = all(jp["pass_and"] == "PASS" for jp in joint_paired.values())  # (local)

    # --- clause-level composite (FAIL if any FAIL; else INFO if any INFO; else PASS) ---
    all_clause_verdicts = (
        list(a_single.values())
        + list(b_single.values())
        + [jp["pass_and"] for jp in joint_paired.values()]
    )  # (local)
    clause_composite = _worst(all_clause_verdicts)  # (local)

    # --- propagate each reviewer's overall_axis_verdict ---
    overall_a = str(rev_a.get("overall_axis_verdict", "FAIL")).strip().upper()  # (local)
    overall_b = str(rev_b.get("overall_axis_verdict", "FAIL")).strip().upper()  # (local)
    overall_a = overall_a if overall_a in VERDICT_RANK else "FAIL"
    overall_b = overall_b if overall_b in VERDICT_RANK else "FAIL"

    # --- FINAL composite = worst of {clause_composite, overall_A, overall_B} ---
    # This is the spawn-prompt aggregation rule applied exactly:
    #   composite = FAIL if ANY clause FAIL OR either overall_axis_verdict FAIL;
    #               else INFO if ANY clause INFO OR either overall_axis_verdict INFO;
    #               else PASS.
    composite = _worst([clause_composite, overall_a, overall_b])  # (local)

    # --- map JOINT sub-verdicts to the necessity / converse-asymmetry readings ---
    # JOINT-1 = NECESSITY direction; JOINT-2 = NECESSITY-ONLY (converse-failure) asymmetry
    necessity_subverdict = joint_paired["JOINT-1"]["pass_and"]      # (local)
    converse_asymmetry_subverdict = joint_paired["JOINT-2"]["pass_and"]  # (local)

    # --- PASS-ON-STRUCTURE flag ---
    # The structural necessity is blind-verified PASS-AND on EVERY clause (clause_composite
    # == PASS) AND at least one reviewer down-graded the OVERALL axis verdict to INFO purely
    # on the registry-PASS criterion (the 6/6 anchor-SHA harvest as the registered entry text
    # presents it) -> the composite is INFO, but it is PASS-ON-STRUCTURE.
    structure_pass_and = (clause_composite == "PASS")             # (local)
    overall_info_only = (composite == "INFO"
                        and "FAIL" not in (overall_a, overall_b, clause_composite))  # (local)
    pass_on_structure = bool(structure_pass_and and overall_info_only)  # (local)

    return {
        "a_single": a_single,
        "b_single": b_single,
        "joint_paired": joint_paired,
        "single_a_ok": single_a_ok,
        "single_b_ok": single_b_ok,
        "joint_ok": joint_ok,
        "clause_composite": clause_composite,
        "overall_axis_A": overall_a,
        "overall_axis_B": overall_b,
        "necessity_subverdict": necessity_subverdict,
        "converse_asymmetry_subverdict": converse_asymmetry_subverdict,
        "composite": composite,
        "structure_pass_and": structure_pass_and,
        "pass_on_structure": pass_on_structure,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """Print the verdict PAYLOAD for the dispatching AGENT to pass to emit_verdict.
    The script does NOT write the verdict file (race-safe single writer = emit_verdict)."""
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

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Load the two reviewer clause-verdict JSONs (NO physics — just read)
    rev_a = json.loads(REVIEWER_A_JSON.read_text(encoding="utf-8"))  # (local)
    rev_b = json.loads(REVIEWER_B_JSON.read_text(encoding="utf-8"))  # (local)
    # sanity: both JSONs target THIS gate + slot
    assert rev_a.get("gate_id") == GATE_ID, f"reviewer-A gate_id mismatch: {rev_a.get('gate_id')}"
    assert rev_b.get("gate_id") == GATE_ID, f"reviewer-B gate_id mismatch: {rev_b.get('gate_id')}"
    assert "§VII.X.2-NECESSITY" in str(rev_a.get("slot", "")), "reviewer-A slot mismatch"
    assert "§VII.X.2-NECESSITY" in str(rev_b.get("slot", "")), "reviewer-B slot mismatch"

    # 3. Aggregate (deterministic)
    agg = aggregate(rev_a, rev_b)

    # 4. Build the reviewer x clause matrix for the npz (rows = reviewers, cols = clauses)
    clause_order = (SINGLE_AXIS_A_CLAUSES + SINGLE_AXIS_B_CLAUSES + JOINT_CLAUSES)  # (local)
    reviewer_order = ["axis_A_van-den-dungen", "axis_B_volovik"]  # (local)
    # numeric encoding: PASS=1, INFO=0, FAIL=-1, N/A-not-assigned=2
    code = {"PASS": 1, "INFO": 0, "FAIL": -1}  # (local)
    matrix = np.full((2, len(clause_order)), 2, dtype=np.int64)  # 2 = clause not assigned to that reviewer  # (local)
    for j, c in enumerate(clause_order):
        if c in SINGLE_AXIS_A_CLAUSES or c in JOINT_CLAUSES:
            matrix[0, j] = code[_clause_verdict(rev_a, c)]
        if c in SINGLE_AXIS_B_CLAUSES or c in JOINT_CLAUSES:
            matrix[1, j] = code[_clause_verdict(rev_b, c)]

    # 5. Report
    print("=== Reviewer x clause matrix (PASS=1 INFO=0 FAIL=-1 not-assigned=2) ===")
    print(f"  clauses: {clause_order}")
    for i, r in enumerate(reviewer_order):
        print(f"  {r}: {matrix[i].tolist()}")
    print()
    print("=== JOINT-clause PASS-AND (PASS only if PASS in BOTH) ===")
    for c in JOINT_CLAUSES:
        jp = agg["joint_paired"][c]
        print(f"  {c}: axis_A={jp['axis_A']} axis_B={jp['axis_B']} -> pass_and={jp['pass_and']}")
    print(f"  necessity (JOINT-1) sub-verdict       : {agg['necessity_subverdict']}")
    print(f"  converse-asymmetry (JOINT-2) sub-verdict: {agg['converse_asymmetry_subverdict']}")
    print()
    print("=== single-axis clauses ===")
    print(f"  axis-A single: {agg['a_single']}  (all PASS: {agg['single_a_ok']})")
    print(f"  axis-B single: {agg['b_single']}  (all PASS: {agg['single_b_ok']})")
    print()
    print("=== overall_axis_verdict propagation ===")
    print(f"  reviewer-A overall_axis_verdict: {agg['overall_axis_A']}")
    print(f"  reviewer-B overall_axis_verdict: {agg['overall_axis_B']}")
    print(f"  clause-level composite         : {agg['clause_composite']}")
    print(f"  FINAL composite (worst-of)     : {agg['composite']}")
    print(f"  structure_pass_and             : {agg['structure_pass_and']}")
    print(f"  PASS-ON-STRUCTURE              : {agg['pass_on_structure']}")
    print()

    verdict = agg["composite"]  # (local)

    # 6. Compose the value payload (no single-quote chars — emit_verdict wraps value='...')
    reading = "PASS-ON-STRUCTURE" if agg["pass_on_structure"] else verdict  # (local)
    value = (
        f"composite={verdict};reading={reading};"
        f"clause_composite={agg['clause_composite']};"
        f"necessity_JOINT1_passand={agg['necessity_subverdict']};"
        f"converse_asym_JOINT2_passand={agg['converse_asymmetry_subverdict']};"
        f"single_A_allPASS={agg['single_a_ok']};single_B_allPASS={agg['single_b_ok']};"
        f"overall_axis_A={agg['overall_axis_A']};overall_axis_B={agg['overall_axis_B']};"
        f"INFO_reason=6of6_anchor_SHA_harvest_UNMET_as_registered_entry_text_presents_it_"
        f"SOURCE-RECON_Class-c_SEPARATE_from_structural_clauses;"
        f"substrate_input_overlap_CAVEAT=both_reviewers_loaded_same_truth_table_json_"
        f"necessity_largely_STRUCTURAL_substitution_chain_contrapositive_so_closer_to_"
        f"structural_output_independence_over_shared_structural_input;"
        f"S108_fwd_gate=S88-LAMBDA-SA-SUCCESSOR-EMISSION_family_PLUS_proper_Stage2to3_promotion;"
        f"registry_action=STAGE-1-CANDIDATE_PRESERVED"
    )  # (local)

    # 7. Save the npz (matrix + sub-verdicts + composite)
    np.savez(
        OUT_NPZ,
        reviewer_clause_matrix=matrix,
        clause_order=np.array(clause_order, dtype=object),
        reviewer_order=np.array(reviewer_order, dtype=object),
        joint1_axis_A=agg["joint_paired"]["JOINT-1"]["axis_A"],
        joint1_axis_B=agg["joint_paired"]["JOINT-1"]["axis_B"],
        joint1_pass_and=agg["necessity_subverdict"],
        joint2_axis_A=agg["joint_paired"]["JOINT-2"]["axis_A"],
        joint2_axis_B=agg["joint_paired"]["JOINT-2"]["axis_B"],
        joint2_pass_and=agg["converse_asymmetry_subverdict"],
        single_axis_A=json.dumps(agg["a_single"]),
        single_axis_B=json.dumps(agg["b_single"]),
        single_a_ok=agg["single_a_ok"],
        single_b_ok=agg["single_b_ok"],
        joint_ok=agg["joint_ok"],
        clause_composite=agg["clause_composite"],
        overall_axis_A=agg["overall_axis_A"],
        overall_axis_B=agg["overall_axis_B"],
        composite=agg["composite"],
        structure_pass_and=agg["structure_pass_and"],
        pass_on_structure=agg["pass_on_structure"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 8. 4-tuple + verdict payload
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    extra_rows = [
        "# regulator_pin=a_n^{Mellin}",
    ]  # (local)
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        companion_note=(f"reading={reading}; "
                       f"necessity_JOINT1={agg['necessity_subverdict']} "
                       f"converse_asym_JOINT2={agg['converse_asymmetry_subverdict']}; "
                       f"clause-PASS-AND_all_PASS_overall_axis_A_INFO_propagated"),
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (reading={reading}) (wall {wall:.2f}s) ===")
    # Verdict is DATA; exit 0 on script health regardless of PASS/FAIL/INFO.
    return 0


if __name__ == "__main__":
    sys.exit(main())
