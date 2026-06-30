#!/usr/bin/env python3
"""
S88 W8-95 — S88-CF-25-STAGE-2-INDEPENDENT-VERIFY (Aggregator)
==============================================================

Coordinator-side PASS-AND aggregator for the §VII.X.W4-1 9-cell tensor
STAGE-1-CANDIDATE Stage-2 cross-axis independent-verify per
`.claude/rules/joint-theorem-promotion.md` 4-stage pathway.

Aggregates the two upstream cross-reviewer per-axis verdicts:

  - Axis-A (NCG-axiomatic / spectral-action): connes-ncg-theorist
      input  : computations/session-88/s88_w8_cf25_stage2_axis_a_connes.npz
      verdict: PASS (5 axis-A + 4 JOINT, all PASS)

  - Axis-B (substrate-physics / superfluid analogy): volovik-superfluid-universe-theorist
      input  : computations/session-88/s88_w8_cf25_stage2_axis_b_volovik.npz
      verdict: INFO (10 axis-B + 2 JOINT; 10 PASS / 0 FAIL / 2 INFO)

This aggregator's job is NOT to re-derive the per-axis content.  It RECONCILES
the per-clause tables across the two reviewers, applies PASS-AND on JOINT
clauses, and emits the composite Stage-2 verdict.

Per joint-theorem-promotion.md §"Stage 2":
  - PASS criterion : BOTH cross-reviewers PASS on their single-axis clauses
                     AND JOINT clauses PASS independently in BOTH verdicts
                     (logical AND, not OR)
  - FAIL criterion : ANY clause FAIL in either verdict
  - INFO criterion : ANY JOINT clause INFO in either verdict; theorem stays at
                     STAGE-1; INFO clause routes to remediation carry-forward.
                     The text "any JOINT clause" is the literal rule, but the
                     same rule's prefatory sentence is broader: "Either
                     cross-reviewer returns INFO on a clause → theorem stays
                     at Stage 1; the INFO clause is documented as a
                     Stage-2-INFO-deferred item."  We take the BROADER reading
                     (any clause INFO) per Stage-2 protocol §"Stage 2 INFO
                     criterion" (line 76 of joint-theorem-promotion.md).

Substrate framing: §VII.X.W4-1 IS the cross-pillar bridge anatomy connecting
Pillars II / III / IV at substrate-IS observable layer (HKR, Connes-Karoubi,
K-theory boundary).  The two reviewers verify the bridge IS-not-IN structure
from independent axes WITHOUT shared workshop context — Stage-2 PASS-AND
is structurally independent verification per epistemic-discipline.md §"What
Counts as Evidence".

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-88/s88_w8_cf25_stage2_axis_a_connes.npz  (axis-A)
  - computations/session-88/s88_w8_cf25_stage2_axis_b_volovik.npz (axis-B)
  - canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=composite_verdict, scheme=Stage-2-two-agent-parallel-cross-axis-verify-no-workshop-context,
   convention=PASS-AND-on-JOINT-clauses-axis-A-connes-axis-B-volovik, L_max=10)

Classification: NON-PHONONIC (methodology-aggregator; no D_K eigenvalue computation).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _P
_SHARED = _P(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-only aggregator
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S88"                                                       # (local)
GATE_ID = "S88-CF-25-STAGE-2-INDEPENDENT-VERIFY"                      # (local)
SCHEME = "Stage-2-two-agent-parallel-cross-axis-verify-no-workshop-context"  # (local)
CONVENTION = "PASS-AND-on-JOINT-clauses-axis-A-connes-axis-B-volovik"  # (local)
L_MAX = 10                                                            # (local)

# Per-axis upstream verdict NPZ paths (orchestrator-provided)
AXIS_A_NPZ = SESSION_DIR / "s88_w8_cf25_stage2_axis_a_connes.npz"     # (local)
AXIS_B_NPZ = SESSION_DIR / "s88_w8_cf25_stage2_axis_b_volovik.npz"    # (local)

OUT_NPZ = SESSION_DIR / "s88_w8_cf25_stage_2_aggregate.npz"
VERDICT_TXT = SESSION_DIR / "s88_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AXIS_A_NPZ,
    AXIS_B_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA closure helpers
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
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
# Section 5 — Reconciliation table
#
# Cross-reviewer clause-id mapping.  The two reviewers parsed §VII.X.W4-1
# at DIFFERENT GRANULARITIES:
#   - connes:  9 clauses total  (5 axis-A + 4 JOINT)
#   - volovik: 12 clauses total (10 axis-B + 2 JOINT)
# Interpretation (a) of the spawn-prompt: different parsing granularity.
#
# Connes consolidated the bridge-axiom verification into a single 7×3×3
# tensor-cell PASS (C2 + C5).  Volovik split the substrate-side anatomy
# into separate Anatomy-1, Anatomy-2, LQT-inheritance, Corollary-1/2/3 sub-
# clauses.  The two reviewers AGREE on the JOINT-c (bridge map axiom
# preservation) and JOINT-d (Mellin-cone envelope) clauses; they DISAGREE
# on whether the L^{-1} sub-unity direction (connes C7) and the W-5 anchor
# numerical match (connes C8) are JOINT or AXIS-B.
#
# JOINT-by-either union (per spawn-prompt rule item 3):
#   {C5≡JOINT-c, C6≡JOINT-d, C7≡T2, C8≡T3}
# Volovik PASSes on T2 and T3 even though tagged AXIS-B; this lifts to
# JOINT PASS-AND under the broader "JOINT under EITHER attribution" reading.
# ---------------------------------------------------------------------------

# Manual reconciliation map: (axis_a_clause_id, axis_b_clause_id, content_match)
RECONCILIATION = [
    # connes_id, volovik_id, joint_under_either, content_anchor
    ("C1-Level1-Structural-Identity",        "T1-bit-exact-anchor",          False, "HP^1 strict F_4 anchor 1.030902"),
    ("C2-NCG-Axioms-Preservation",           "NCG-axioms-substrate-5-of-7",  False, "7-axiom-by-3-bridge-by-3-channel verification (axis-A connes covers all 7; axis-B volovik covers 5 substrate-side; 2 deferred to axis-A)"),
    ("C3-Channel-1-Cocycle-Rank",            "Corollary-1-channel-decomp",   False, "Channel-1 cocycle rank Tr|D|^{-1}=25248.15 (axis-A); BdG cumulant rank-1 channel decomposition (axis-B)"),
    ("C4-Channel-3-Cocycle-Rank",            "Corollary-3-falsifier-design", False, "Channel-3 cocycle rank Tr|D|^{-5}=682.51 (axis-A); rank-3 falsifier design forward-extension (axis-B)"),
    ("C5-Joint-c-Bridge-Map-Axiom-Preservation", "JOINT-c-bridge-axiom-preserve", True,  "JOINT (c) Bridge map axiom preservation [HKR / Connes-Karoubi / K-theory boundary]"),
    ("C6-Joint-d-Mellin-Cone-Envelope-d4",   "JOINT-d-Mellin-envelope-2k-1", True,  "JOINT (d) Mellin-cone envelope alpha_k = 2k-1 at d=4"),
    ("C7-Sub-Unity-Direction-Level3-Level2", "T2-envelope-alpha-k",          True,  "Sub-unity direction Level-3/Level-2 = 1/L = 0.1 < 1.0 (algebraic identity)"),
    ("C8-W5-Anchor-Numerical-Match",         "T3-W5-anchor-ratio",           True,  "W-5 anchor numerical match: 19/200 = 0.095 (Sage-exact); ~5% inside generic 1/L"),
    ("C9-Substrate-IS-Framing-OE-Form",      "Anatomy-1-substrate-IS-BdG",   False, "Substrate-IS framing 5-anatomy element 1 (substrate-IS BdG inheritance via chi morphism)"),
    # Volovik-side-only clauses (no axis-A counterpart)
    (None,                                    "Anatomy-2-lab-IN-quantum-metric", False, "[volovik-only] Lab-IN OE-form discipline; q=II Mellin OE-form not strict positive-match per W7a-73 regex"),
    (None,                                    "LQT-inheritance-k1-k3",         False, "[volovik-only] LQT (Loday-Quillen-Tsygan) invocation; registry text uses lower-k transport b:HC^k -> HC^{k-1} not LQT proper"),
    (None,                                    "Corollary-2-9cell-extension",   False, "[volovik-only] 9-cell extension via 3 functorial bridge maps; 16 non-W-5 cells empirically deferred"),
]


# ---------------------------------------------------------------------------
# Section 6 — Compute (load + reconcile + PASS-AND)
# ---------------------------------------------------------------------------
def _to_str(x) -> str:
    if isinstance(x, np.ndarray):
        return str(x.item()) if x.ndim == 0 else str(x[0])
    if isinstance(x, (bytes, np.bytes_)):
        return x.decode("utf-8")
    return str(x)


def load_axis_a():
    z = np.load(AXIS_A_NPZ, allow_pickle=True)
    rows = []
    for i in range(len(z["clause_id"])):
        rows.append(
            {
                "clause_id": _to_str(z["clause_id"][i]),
                "axis":      _to_str(z["axis"][i]),
                "verdict":   _to_str(z["verdict"][i]),
                "value":     _to_str(z["value"][i]),
                "substitution_chain": _to_str(z["substitution_chain"][i]),
            }
        )
    composite = _to_str(z["composite_per_axis_verdict"])
    return rows, composite


def load_axis_b():
    z = np.load(AXIS_B_NPZ, allow_pickle=True)
    rows = []
    for i in range(len(z["clause_id"])):
        rows.append(
            {
                "clause_id": _to_str(z["clause_id"][i]),
                "axis":      _to_str(z["axis"][i]),
                "verdict":   _to_str(z["verdict"][i]),
                "value":     _to_str(z["value"][i]),
                "substitution_chain": _to_str(z["substitution_chain"][i]),
            }
        )
    composite = _to_str(z["composite_verdict"])
    return rows, composite


def find_row(rows, cid):
    if cid is None:
        return None
    for r in rows:
        if r["clause_id"] == cid:
            return r
    return None


def compute() -> dict:
    rows_a, composite_a = load_axis_a()
    rows_b, composite_b = load_axis_b()

    print(f"  axis_A composite (connes):  {composite_a}  | n_clauses={len(rows_a)}")
    print(f"  axis_B composite (volovik): {composite_b}  | n_clauses={len(rows_b)}")
    print()

    # Build per-clause aggregate table (one row per RECONCILIATION entry)
    aggregate = []  # (local)
    n_pass_total = 0   # (local)
    n_fail_total = 0   # (local)
    n_info_total = 0   # (local)
    passand_joint_clauses = []  # (local)
    info_clauses_axis_a = []    # (local)
    info_clauses_axis_b = []    # (local)
    fail_clauses_any = []       # (local)
    joint_under_either_pass_and_pass = 0  # (local)
    joint_under_either_pass_and_total = 0  # (local)

    for cid_a, cid_b, joint_under_either, anchor in RECONCILIATION:
        r_a = find_row(rows_a, cid_a)
        r_b = find_row(rows_b, cid_b)
        v_a = r_a["verdict"] if r_a else "N/A"  # (local)
        v_b = r_b["verdict"] if r_b else "N/A"  # (local)

        # PASS-AND only meaningful if joint_under_either AND both reviewers gave verdicts
        pass_and = None  # (local)
        if joint_under_either:
            joint_under_either_pass_and_total += 1
            both_pass = (v_a == "PASS") and (v_b == "PASS")
            pass_and = "PASS" if both_pass else (
                "FAIL" if (v_a == "FAIL" or v_b == "FAIL") else "INFO"
            )
            if pass_and == "PASS":
                joint_under_either_pass_and_pass += 1
                passand_joint_clauses.append(
                    {
                        "axis_a_clause": cid_a,
                        "axis_b_clause": cid_b,
                        "anchor":        anchor,
                        "pass_and":      pass_and,
                    }
                )

        # Track INFO / FAIL by axis
        if v_a == "INFO":
            n_info_total += 1
            info_clauses_axis_a.append({"clause_id": cid_a, "anchor": anchor})
        if v_b == "INFO":
            n_info_total += 1
            info_clauses_axis_b.append({"clause_id": cid_b, "anchor": anchor})
        if v_a == "FAIL":
            n_fail_total += 1
            fail_clauses_any.append({"axis": "A", "clause_id": cid_a, "anchor": anchor})
        if v_b == "FAIL":
            n_fail_total += 1
            fail_clauses_any.append({"axis": "B", "clause_id": cid_b, "anchor": anchor})
        if v_a == "PASS":
            n_pass_total += 1
        if v_b == "PASS":
            n_pass_total += 1

        aggregate.append(
            {
                "axis_a_clause": cid_a or "(no axis-A counterpart)",
                "axis_b_clause": cid_b or "(no axis-B counterpart)",
                "joint_under_either": joint_under_either,
                "anchor":   anchor,
                "axis_a_verdict": v_a,
                "axis_b_verdict": v_b,
                "pass_and":       pass_and if pass_and is not None else "(single-axis)",
            }
        )

    # Composite verdict per joint-theorem-promotion.md §"Stage 2"
    # FAIL criterion : any clause FAIL in either verdict
    # INFO criterion : any clause INFO in either verdict (broader reading per
    #                  rule's prefatory sentence)
    # PASS criterion : everything else (all PASS in respective single-axis +
    #                  all JOINT PASS-AND'd)
    if n_fail_total > 0:
        composite = "FAIL"
        promotion_decision = "BLOCK"
    elif n_info_total > 0:
        composite = "INFO"
        promotion_decision = "BLOCK"
    else:
        composite = "PASS"
        promotion_decision = "PROMOTE"

    # Stage-2 protocol compliance (5-point checklist)
    protocol_compliance = {
        "1_dispatched_in_parallel":          True,   # orchestrator confirmed (Phase 2 dispatch)
        "2_different_axes":                  True,   # axis-A spectral vs axis-B substrate
        "3_not_original_workshop_authors":   True,   # connes/volovik are NOT W4-1 workshop authoring
                                                     # (W4-1 was a multi-agent CF-25 workshop;
                                                     #  per-clause first-principles verification
                                                     #  WITHOUT R1/R2/R3 transcripts)
        "4_no_workshop_transcripts_in_prompt": True, # orchestrator confirmed (spawn-prompt
                                                     # contained only Stage-1 entry text + canonical)
        "5_passand_on_joint_applied":        True,   # this aggregator
    }

    axis_attribution_discrepancy = {
        "n_clauses_axis_a":         len(rows_a),
        "n_clauses_axis_b":         len(rows_b),
        "n_joint_axis_a":           sum(1 for r in rows_a if r["axis"] == "JOINT"),
        "n_joint_axis_b":           sum(1 for r in rows_b if r["axis"] == "JOINT"),
        "interpretation":           "(a) different_parsing_granularity",
        "explanation": (
            "Connes consolidated bridge-axiom verification into a single "
            "7x3x3 tensor-cell PASS (C2 covers 7-axiom verification across "
            "all 9 cells; C5 covers JOINT bridge-map axiom preservation as "
            "a single clause). Volovik split the substrate-side anatomy "
            "into separate Anatomy-1, Anatomy-2, LQT-inheritance, "
            "Corollary-1/2/3 sub-clauses (10 axis-B clauses). Both "
            "reviewers AGREE on JOINT-c (bridge map axiom preservation) "
            "and JOINT-d (Mellin-cone envelope). They DISAGREE on whether "
            "the L^{-1} sub-unity direction (connes C7) and the W-5 "
            "anchor numerical match (connes C8) are JOINT (connes view) "
            "or AXIS-B (volovik view). PASS-AND under the broader 'JOINT "
            "under either attribution' reading lifts both to JOINT-PASS."
        ),
        "passand_under_either_total":   joint_under_either_pass_and_total,
        "passand_under_either_passing": joint_under_either_pass_and_pass,
    }

    s89_carryforwards = [
        {
            "id":      "S89-CF-25-AXIS-B-INFO-CLAUSES-REMEDIATION",
            "what":    ("Resolve the two volovik INFO clauses: (i) "
                        "Anatomy-2 lab-IN OE-form q=II Mellin discipline "
                        "(extend OE-form regex to admit Mellin-transform "
                        "form M(s=k+2) explicitly per W7a-73 protocol); "
                        "(ii) LQT-inheritance-k1-k3 (clarify whether the "
                        "registry text means lower-k transport b:HC^k -> "
                        "HC^{k-1} or LQT proper; if the former, retitle "
                        "the registry sub-clause to 'Connes-periodicity "
                        "lower-k transport' and demote LQT label)."),
            "inputs":  ("§VII.X.W4-1 registry entry text; "
                        "cross-pillar-bridge-anatomy.md §Element-2-OE-form-discipline; "
                        "Loday-Quillen-Tsygan reference (Loday 1992 §10.2); "
                        "Connes 1985 cyclic homology periodicity"),
            "gate":    ("PASS iff (i) OE-form regex extended and Anatomy-2 "
                        "passes positive-match for q=II Mellin form AND "
                        "(ii) LQT-inheritance retitled or full LQT proof "
                        "for k=1<->k=3 transport landed; both volovik "
                        "INFO clauses promote to PASS in S89 re-verify"),
            "effort":  "~1.0 wave-equivalents (rule-file extension + registry-entry sub-clause edits + S89 axis-B re-verify dispatch)",
        },
        {
            "id":      "S89-CF-25-AXIS-ATTRIBUTION-PROTOCOL-CLARIFICATION",
            "what":    ("Extend joint-theorem-promotion.md §Stage 2 with "
                        "axis-attribution discipline: at Stage-1 registration, "
                        "the registry entry MUST tag each clause with explicit "
                        "axis attribution (AXIS-A | AXIS-B | JOINT) at a "
                        "PRE-AGREED granularity; cross-reviewers must consume "
                        "the same per-clause table.  Forward-looking from S89: "
                        "Stage-1 candidates emit a per-clause axis-attribution "
                        "table as part of the registry entry.  Add calibration "
                        "corpus instance: S88 W8-95 W4-1 9-cell tensor (instance #1; "
                        "9 vs 12 clause discrepancy, JOINT-clause disagreement "
                        "on C7/C8 vs T2/T3)."),
            "inputs":  ("joint-theorem-promotion.md §Stage 2; "
                        "S88 W8-95 aggregate verdict; "
                        "S87 W5-1 §VII.AF.1 Pillar III↔IV bridge precedent; "
                        "S87 W11-5 §VII.AJ FWD-C3 precedent"),
            "gate":    ("PASS iff joint-theorem-promotion.md §Stage 2 extended "
                        "with axis-attribution discipline AND axis-attribution "
                        "table landed in §VII.X.W4-1 registry entry text"),
            "effort":  "~0.5 wave-equivalents (rule-file extension + registry-edit; methodology W-class)",
        },
    ]

    return {
        "value":                  composite,
        "composite_verdict":      composite,
        "promotion_decision":     promotion_decision,
        "n_pass_total":           n_pass_total,
        "n_fail_total":           n_fail_total,
        "n_info_total":           n_info_total,
        "axis_a_composite":       composite_a,
        "axis_b_composite":       composite_b,
        "aggregate":              aggregate,
        "passand_joint_clauses":  passand_joint_clauses,
        "info_clauses_axis_a":    info_clauses_axis_a,
        "info_clauses_axis_b":    info_clauses_axis_b,
        "fail_clauses_any":       fail_clauses_any,
        "axis_attribution_discrepancy_summary": axis_attribution_discrepancy,
        "protocol_compliance":    protocol_compliance,
        "s89_remediation_carryforwards": s89_carryforwards,
    }


# ---------------------------------------------------------------------------
# Section 7 — Verdict + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    annotation: str,
) -> None:
    """Atomic append of the canonical verdict line + dual-SHA companion row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); {annotation}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy)")

    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    composite = result["composite_verdict"]
    promotion = result["promotion_decision"]
    n_pass = result["n_pass_total"]
    n_fail = result["n_fail_total"]
    n_info = result["n_info_total"]
    discrep = result["axis_attribution_discrepancy_summary"]

    # Print human-readable summary
    print(f"=== Aggregate per-clause table ({len(result['aggregate'])} reconciled rows) ===")
    for row in result["aggregate"]:
        joint_tag = "JOINT-by-either" if row["joint_under_either"] else "single-axis"
        print(f"  [{joint_tag}] axis_a={row['axis_a_verdict']:<4} axis_b={row['axis_b_verdict']:<4} "
              f"PASS-AND={row['pass_and']:<14} | "
              f"A:{row['axis_a_clause'][:35]} ↔ B:{row['axis_b_clause'][:35]}")
    print()
    print(f"=== Axis-attribution discrepancy (interpretation (a)) ===")
    print(f"  n_clauses_axis_a       = {discrep['n_clauses_axis_a']}")
    print(f"  n_clauses_axis_b       = {discrep['n_clauses_axis_b']}")
    print(f"  n_joint_axis_a         = {discrep['n_joint_axis_a']}")
    print(f"  n_joint_axis_b         = {discrep['n_joint_axis_b']}")
    print(f"  passand_under_either   = {discrep['passand_under_either_passing']}/"
          f"{discrep['passand_under_either_total']}")
    print()
    print(f"=== Volovik INFO clauses (axis-B only; not JOINT under either) ===")
    for x in result["info_clauses_axis_b"]:
        print(f"  - {x['clause_id']}: {x['anchor']}")
    print()
    print(f"=== Composite (joint-theorem-promotion.md §Stage 2 collapse) ===")
    print(f"  n_pass={n_pass}  n_fail={n_fail}  n_info={n_info}")
    print(f"  composite_verdict   = {composite}")
    print(f"  promotion_decision  = {promotion} (§VII.X.W4-1 STAGE-1-CANDIDATE → "
          f"{'STAGE-3-PERMANENT' if promotion == 'PROMOTE' else 'stays at STAGE-1'})")
    print()

    # Save NPZ
    np.savez(
        OUT_NPZ,
        composite_verdict=np.array(composite, dtype="<U10"),
        per_clause_aggregate=np.array(json.dumps(result["aggregate"], default=str), dtype=object),
        passand_joint_clauses=np.array(json.dumps(result["passand_joint_clauses"], default=str), dtype=object),
        info_clauses_axis_a=np.array(json.dumps(result["info_clauses_axis_a"], default=str), dtype=object),
        info_clauses_axis_b=np.array(json.dumps(result["info_clauses_axis_b"], default=str), dtype=object),
        fail_clauses_any=np.array(json.dumps(result["fail_clauses_any"], default=str), dtype=object),
        axis_attribution_discrepancy_summary=np.array(json.dumps(discrep, default=str), dtype=object),
        protocol_compliance=np.array(json.dumps(result["protocol_compliance"], default=str), dtype=object),
        registry_promotion_decision=np.array(promotion, dtype="<U16"),
        s89_remediation_carryforwards=np.array(json.dumps(result["s89_remediation_carryforwards"], default=str), dtype=object),
        n_pass_total=np.int64(n_pass),
        n_fail_total=np.int64(n_fail),
        n_info_total=np.int64(n_info),
        axis_a_composite=np.array(result["axis_a_composite"], dtype="<U10"),
        axis_b_composite=np.array(result["axis_b_composite"], dtype="<U10"),
    )
    print(f"  NPZ saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 4-tuple + verdict line
    value_str = (
        f"composite={composite};promotion={promotion};"
        f"n_pass={n_pass};n_fail={n_fail};n_info={n_info};"
        f"axis_a_composite={result['axis_a_composite']};"
        f"axis_b_composite={result['axis_b_composite']};"
        f"axis_a_clauses={discrep['n_clauses_axis_a']};"
        f"axis_b_clauses={discrep['n_clauses_axis_b']};"
        f"passand_joint={discrep['passand_under_either_passing']}/{discrep['passand_under_either_total']}"
    )
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    annotation = (
        "Stage-2 PASS-AND aggregate; axis-A connes PASS (5+4 JOINT all PASS); "
        "axis-B volovik INFO (10 PASS / 0 FAIL / 2 INFO axis-B-only Anatomy-2+LQT-inheritance); "
        "passand_joint=4/4 PASS under JOINT-by-either; composite INFO blocks STAGE-1->STAGE-3 promotion; "
        "§VII.X.W4-1 stays at STAGE-1-CANDIDATE; INFO clauses route to S89 remediation"
    )
    append_verdict(composite, value_str, audit_sha, content_sha, annotation)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
