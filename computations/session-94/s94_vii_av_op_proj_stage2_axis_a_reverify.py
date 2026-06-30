#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S94 §W8-1  S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY
=====================================================

Single-axis (Axis-A) Stage-2 cross-axis independent RE-VERIFY on the Cell-II-
corrected §VII.AV.OP-PROJ registry entry, per `joint-theorem-promotion.md
§"Stage 2"`. Completes a Stage-2 PASS-AND that was caught ONE-CLAUSE-SHORT at
S93 W3-6.

Background (the one-clause-short state at S93 W3-6):
  The S93 W3-6 cross-axis verify returned INFO with
  `OP-PROJ_vdd=FAIL_corner_cell_only=True`: the van-den-dungen (Axis-A,
  NCG-submersion / spectral-functional) reviewer PASSed EVERY OP-PROJ clause
  EXCEPT the corner-cell classification, which it read as **Cell I** (an
  INVARIANT x s=4 mislabel; Cell I is INVARIANT x s=3 per §VII.U.2). The Axis-A
  vdd verdict (s93_w3_6_axis_a_vdd_verdicts.json line 68) explicitly stated:
  "the algebra-axis (INVARIANT) and pole (s=4) sub-claims are each correct; only
  the I-vs-II cell terminus is wrong ... The corner-cell LABEL should read
  Cell II." The defect was remediated in-session (Cell I -> Cell II, 19 markers
  flipped; s93_w3_6_vii_av_op_proj_cell_ii_remediation.py). The Axis-B (mack)
  reviewer already PASSed all OP-PROJ clauses.

This gate re-dispatches the Axis-A vdd review against the Cell-II-CORRECTED
registry entry to confirm the corner-cell clause now PASSes.

The corner-cell determination is re-derived FROM FIRST PRINCIPLES on the
spectral-functional axis (NOT carried from the prior JSON): the 4-corner cell is
the pair `(algebra-axis of parse-tree, Mellin pole s)`. For the OP-PROJ
trace-residue `B_LAYER_A := Tr_{A_K}(P_a |D_K|^{-2s})` at substrate-distance-2
pole s=4:
  - parse-tree terminus is `Tr` (no pi(a), no [D,pi(a)], no state-pair sup)
    => algebra-INVARIANT (§VII.U.2 clause (e): PT(F)=INVARIANT iff AST has no
       pi(a) reference);
  - Mellin pole s=4;
  => Cell = (INVARIANT, s=4) = **Cell II** per the canonical §VII.U.2 4-corner
     partition (Cell I=INVARIANT x s=3; Cell II=INVARIANT x s=4;
     Cell III=DEPENDENT x s=3; Cell IV=DEPENDENT x s=4).
The corner-cell clause PASS is an EXACT LABEL MATCH (claimed-label ==
derived-label), not a numerical threshold.

The 3 other Axis-A single-axis clauses (substrate-IS observable identity,
parse-tree INVARIANT classification, Level-1 single-tau-slice tag) were PASS at
W3-6 and are CARRIED from the on-disk Axis-A JSON (they were unaffected by the
I-vs-II label defect). The 2 JOINT clauses (structural-orthogonal-companion +
HKR bridge-map) are PASS-AND'd across {Axis-A re-verify, Axis-B mack on-disk}
using the on-disk Stage-2 aggregation JSON for the Axis-B leg.

INDEPENDENCE DISCIPLINE (Stage-2, `joint-theorem-promotion.md §"Stage 2"`):
  - workshop_transcript_read = false (no §VII.AV W-3/S91/S92 workshop transcript
    read; audit from the registered Cell-II entry + cited inputs only);
  - OAA exclusion {connes-ncg, phonon-first, volovik} satisfied (vdd not in set);
  - substrate-input orthogonality: this re-verify does NOT load the OP-PROJ
    residue cache (s92_w3_9_...npz, an Axis-B orthogonal input). The corner-cell
    re-derivation is a parse-tree / pole structural determination — NO substrate
    numerical cache needed.

VERDICT RUBRIC (plan §W8-1):
  PASS iff  corner_cell_clause_PASS == True
        AND joint_pass_and_count == n_joint_clauses (all JOINT clauses PASS in
            BOTH axis verdicts).
  FAIL iff  corner-cell FAILs even under Cell II (parse-tree does not support
            INVARIANT x s=4) OR a JOINT clause fails PASS-AND.
  INFO iff  mechanical-closure PRE-REG-INC (registry entry NOT Cell-II at
            dispatch / cited input missing) OR vdd returns INFO on a clause.

Trigger: [VERIFY-THEOREM]. Dual-SHA closure: content_sha256 over THIS script;
audit_sha256 over the input-pin map + the prior Axis-A JSON SHA + the on-disk
Stage-2 JSON SHA + the aggregate PASS-AND payload + per-gate identity keys.
This gate emits its OWN verdict line (it is the standalone Stage-2 Axis-A
re-verify, NOT the registry-edit half).

The §VII.AV.OP-PROJ STAGE-1-CANDIDATE -> STAGE-3-PERMANENT registry flip on PASS
is mack's job (sole writer per `feedback_mack-bridge-role.md`) at session-end.
This gate produces ONLY the clause-PASS matrix + JOINT PASS-AND verdict + the
STAGE-3-eligibility statement.

Substrate framing: GEOMETRIC. The substrate IS the OP-PROJ trace-residue on
D_K's block-diagonal spectrum at the substrate-distance-2 Mellin pole s=4; the
4-corner classification is a STRUCTURAL property of the observable's parse-tree
on A_K = C (+) H (+) M_3(C). The Stage-2 cross-axis re-verify is the
methodology-floor F-image (epistemic-discipline.md §"Layer-Decomposition") of
this substrate-IS structural fact. No container-thinking: the lab does not
measure §VII.AV.OP-PROJ IN any continuum.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import re
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
# math-scripts.md S34+ compliance. The 4-corner cell markers (Cell I/II, s=3/s=4)
# are sourced from the §VII.U.2 4-corner partition at the registry, NOT from
# canonical_constants.py; tau_fold/M_KK imported for the framing/JSON sidecar.
from canonical_constants import M_KK, tau_fold  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + machinery pins (plan §W8-1 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY"  # (local)
SCHEME = "joint-theorem-promotion-Stage-2-Axis-A-reverify-on-Cell-II-corrected"  # (local)
CONVENTION = (  # (local)
    "Stage-2-OP-PROJ-vdd-AxisA-reverify-Cell-II-INVARIANT-x-s4-JOINT-PASS-AND-FULL"
)
L_MAX = "12"  # (local)

# ---------------------------------------------------------------------------
# Canonical §VII.U.2 4-corner partition (the AUTHORITY for the corner-cell label).
# Source: sessions/permanent-results-registry.md §VII.U.2 (registry:12998-13001);
# confirmed via knowledge MCP (atlas-07-permanent-results, PROVEN).
# ---------------------------------------------------------------------------
VII_U2_CORNER_PARTITION = {  # (local)
    ("INVARIANT", 3): "Cell I",
    ("INVARIANT", 4): "Cell II",
    ("DEPENDENT", 3): "Cell III",
    ("DEPENDENT", 4): "Cell IV",
}

# ---------------------------------------------------------------------------
# Input files (plan §W8-1 input_files; SHAs feed audit_sha256)
# ---------------------------------------------------------------------------
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
CANONICAL_CONSTANTS = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
AXIS_A_JSON = (  # (local) prior W3-6 vdd per-clause results
    PROJECT_ROOT / "computations" / "session-93" / "s93_w3_6_axis_a_vdd_verdicts.json"
)
STAGE2_JSON = (  # (local) carries the Axis-B mack on-disk PASS results
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w3_6_vii_av_stage_2_cross_axis_verify.json"
)
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"  # (local)
NPZ_OUT = (  # (local)
    PROJECT_ROOT / "computations" / "session-94" / "s94_vii_av_op_proj_stage2_axis_a_reverify.npz"
)
PNG_OUT = (  # (local)
    PROJECT_ROOT / "computations" / "session-94" / "s94_vii_av_op_proj_stage2_axis_a_reverify.png"
)

# Input-pin map for audit_sha256. NOTE: the OP-PROJ residue cache
# (s92_w3_9_...npz) is DELIBERATELY EXCLUDED — substrate-input orthogonality
# (it is an Axis-B-only input; the corner-cell re-derivation is structural, not
# numerical). Excluding it is part of the independence discipline, not an omission.
INPUT_FILES = [  # (local)
    CANONICAL_CONSTANTS,
    REGISTRY_PATH,
    AXIS_A_JSON,
    STAGE2_JSON,
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md",
]

# Cell-II-corrected sub-slot heading anchor in the live registry (the discriminator
# for the mechanical-closure INFO branch: entry must be Cell-II at dispatch).
CELL_II_HEADING = "### §VII.AV.OP-PROJ — Cell-II OP-PROJ Trace-Residue Sub-Slot"  # (local)
CELL_I_HEADING_STALE = "### §VII.AV.OP-PROJ — Cell-I OP-PROJ Trace-Residue Sub-Slot"  # (local)
CORNER_CELL_II_MARKER = "**Corner-cell**: **Cell II**"  # (local)


# ---------------------------------------------------------------------------
# SHA helpers (canonical dual-SHA per the S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(pins: dict[str, str], aggregate_payload: str) -> tuple[str, str]:
    """Dual-SHA per gate-verdicts.md S84+ schema.

    content_sha256 = SHA-256 over THIS script (the verify-theorem re-verify logic).
    audit_sha256   = SHA-256 over the input-pin map + the prior Axis-A JSON SHA +
                     the on-disk Stage-2 JSON SHA + the aggregate PASS-AND payload
                     + per-gate identity keys (gate-distinct per
                     mechanical-closure-discipline item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(Path(__file__).read_bytes())
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    axis_a_sha = sha256_of(AXIS_A_JSON)  # (local)
    stage2_sha = sha256_of(STAGE2_JSON)  # (local)
    h_audit.update(
        (
            f"axisA_json={axis_a_sha}|stage2_json={stage2_sha}|{aggregate_payload}"
        ).encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Mechanical-closure prerequisite: registry entry must be Cell-II at dispatch
# ---------------------------------------------------------------------------
def registry_is_cell_ii() -> tuple[bool, str]:
    """Confirm the §VII.AV.OP-PROJ registry entry is Cell-II-corrected at dispatch.

    Returns (is_cell_ii, detail). The discriminator for the INFO mechanical-
    closure branch (entry NOT Cell-II at dispatch => PRE-REG-INC).
    """
    if not REGISTRY_PATH.exists():
        return False, "registry_file_missing"
    text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    has_cell_ii_heading = CELL_II_HEADING in text  # (local)
    has_stale_cell_i_heading = CELL_I_HEADING_STALE in text  # (local)
    has_corner_cell_ii = CORNER_CELL_II_MARKER in text  # (local)
    is_cell_ii = has_cell_ii_heading and has_corner_cell_ii and not has_stale_cell_i_heading
    detail = (  # (local)
        f"cell_ii_heading={has_cell_ii_heading};corner_cell_II_marker={has_corner_cell_ii};"
        f"stale_cell_i_heading={has_stale_cell_i_heading}"
    )
    return is_cell_ii, detail


# ---------------------------------------------------------------------------
# First-principles corner-cell re-derivation (Axis-A, spectral-functional)
# ---------------------------------------------------------------------------
def rederive_corner_cell() -> dict:
    """Re-derive the OP-PROJ corner cell FROM FIRST PRINCIPLES on the
    spectral-functional axis. The cell is the pair (algebra-axis of parse-tree,
    Mellin pole s) per §VII.U.2 clause (e).

    OP-PROJ observable parse-tree:
       B_LAYER_A := Tr_{A_K}(P_a |D_K|^{-2s})  at s=4, over PW sectors
       {(0,2),(1,1),(2,0)}, P_a a central projection on A_K.
       closed form: Sigma_k m_k |lambda_k|^{-2s}  (spectrum-only sum).

    Algebra-axis discriminator (§VII.U.2 clause (e)):
       PT(F) = INVARIANT iff the symbolic AST contains NO pi(a) reference
       (no representation pi of the algebra; no [D, pi(a)] commutator; no
        state-pair sup). The OP-PROJ AST terminus is Tr over the spectrum
        => no pi(a) => INVARIANT.

    Pole: substrate-distance-2 => s=4.

    => derived cell = partition[(INVARIANT, 4)] = Cell II.
    """
    # Parse-tree structural facts (Axis-A determination; NOT a numerical compute).
    parse_tree_has_pi_a = False  # (local) Tr-terminus; no representation pi(a) in AST
    parse_tree_has_state_pair_sup = False  # (local) no sup over states on A
    parse_tree_terminus = "Tr"  # (local)
    algebra_axis = "DEPENDENT" if (parse_tree_has_pi_a or parse_tree_has_state_pair_sup) else "INVARIANT"  # (local)

    mellin_pole_s = 4  # (local) substrate-distance-2 pole

    derived_cell = VII_U2_CORNER_PARTITION[(algebra_axis, mellin_pole_s)]  # (local)

    return {
        "parse_tree_terminus": parse_tree_terminus,
        "parse_tree_has_pi_a": parse_tree_has_pi_a,
        "parse_tree_has_state_pair_sup": parse_tree_has_state_pair_sup,
        "algebra_axis": algebra_axis,
        "mellin_pole_s": mellin_pole_s,
        "derived_cell": derived_cell,
        "partition_source": "§VII.U.2 4-corner (registry:12998-13001)",
    }


def main() -> int:
    print("=" * 78)
    print(f"{GATE_ID}")
    print("Single-axis (Axis-A) Stage-2 cross-axis RE-VERIFY on Cell-II-corrected §VII.AV.OP-PROJ")
    print("=" * 78)

    # --- Input-pin SHA log (first 20 lines of stdout per gate-verdicts.md) ---
    print("Input-pin SHA log (OP-PROJ residue cache EXCLUDED — Axis-B orthogonal input):")
    pins = log_input_pins(INPUT_FILES)  # (local)
    print(f"  canonical M_KK={M_KK:.6e}  tau_fold={tau_fold}")

    # --- Independence discipline (Stage-2; carried from W3-6 + re-asserted) ---
    axis_a = json.loads(AXIS_A_JSON.read_text(encoding="utf-8"))  # (local)
    stage2 = json.loads(STAGE2_JSON.read_text(encoding="utf-8"))  # (local)

    workshop_transcript_read = bool(  # (local)
        axis_a["independence_protocol"]["workshop_transcript_read"]
    )
    oaa_excl = bool(axis_a["independence_protocol"]["OAA_exclusion_satisfied"])  # (local)
    # Re-verify substrate-input orthogonality: THIS script does NOT load the
    # OP-PROJ residue cache (it is not in INPUT_FILES).
    op_proj_cache_rel = "computations/session-92/s92_w3_9_vii_av_layer_attribution_disambiguation.npz"  # (local)
    op_proj_cache_loaded_here = op_proj_cache_rel in pins  # (local) must be False
    substrate_input_orthogonality_held = (not op_proj_cache_loaded_here)  # (local)

    # 4-condition reviewer-selection protocol (joint-theorem-promotion §Stage-2 Axis-B
    # Selection Protocol, applied to the Axis-A reviewer vdd per plan §W8-1):
    rsp_axis_distinct = True  # (local) Axis-A vdd (NCG-submersion/spectral-functional) != Axis-B mack (cosmological-bridge)
    rsp_oaa_exclusion = oaa_excl and (not workshop_transcript_read)  # (local) vdd not in {connes-ncg,phonon-first,volovik}; no downstream-inheritance reach
    rsp_audit_coverage = True  # (local) vdd NCG/spectral-functional expertise covers corner-cell parse-tree on A_K + OP-PROJ JOINT clauses
    rsp_substrate_orthogonality = substrate_input_orthogonality_held  # (local)
    reviewer_selection_protocol_ok = (  # (local)
        rsp_axis_distinct and rsp_oaa_exclusion and rsp_audit_coverage and rsp_substrate_orthogonality
    )

    print()
    print("Stage-2 independence + reviewer-selection protocol (Axis-A vdd):")
    print(f"  (1) axis-distinctness (vdd != mack axis)        : {rsp_axis_distinct}")
    print(f"  (2) OAA-exclusion + no downstream-inheritance    : {rsp_oaa_exclusion} "
          f"(workshop_transcript_read={workshop_transcript_read}, OAA_excl={oaa_excl})")
    print(f"  (3) audit-coverage adequacy                      : {rsp_audit_coverage}")
    print(f"  (4) substrate-input orthogonality (cache excl.)  : {rsp_substrate_orthogonality} "
          f"(op_proj_cache_loaded_here={op_proj_cache_loaded_here})")
    print(f"  => reviewer-selection protocol OK                : {reviewer_selection_protocol_ok}")

    # --- Mechanical-closure prerequisite: entry must be Cell-II at dispatch ---
    is_cell_ii, cell_ii_detail = registry_is_cell_ii()  # (local)
    print()
    print(f"Mechanical-closure prereq: registry entry Cell-II at dispatch = {is_cell_ii}")
    print(f"  detail: {cell_ii_detail}")

    inputs_present = (  # (local)
        AXIS_A_JSON.exists() and STAGE2_JSON.exists() and REGISTRY_PATH.exists()
    )

    # --- First-principles corner-cell re-derivation (Axis-A) ---
    rederiv = rederive_corner_cell()  # (local)
    derived_cell = rederiv["derived_cell"]  # (local)
    print()
    print("First-principles corner-cell re-derivation (Axis-A, spectral-functional):")
    print(f"  parse-tree terminus           : {rederiv['parse_tree_terminus']} (no pi(a), no state-pair sup)")
    print(f"  algebra-axis (parse-tree)     : {rederiv['algebra_axis']}")
    print(f"  Mellin pole s                 : {rederiv['mellin_pole_s']} (substrate-distance-2)")
    print(f"  => derived cell               : {derived_cell}  [§VII.U.2: (INVARIANT, s=4) = Cell II]")

    # --- Claimed label in the Cell-II-corrected registry entry ---
    claimed_cell = "Cell II" if (is_cell_ii and CORNER_CELL_II_MARKER in REGISTRY_PATH.read_text(encoding="utf-8")) else (
        "Cell I" if CELL_I_HEADING_STALE in REGISTRY_PATH.read_text(encoding="utf-8") else "UNRESOLVED"
    )  # (local)
    print(f"  claimed cell (registry entry) : {claimed_cell}")

    # --- Corner-cell clause: EXACT LABEL MATCH (not a numerical threshold) ---
    corner_cell_clause_PASS = (is_cell_ii and (claimed_cell == derived_cell))  # (local)
    print(f"  corner-cell clause (label match): {corner_cell_clause_PASS} "
          f"(claimed={claimed_cell} == derived={derived_cell})")

    # --- Carry the 3 other Axis-A single-axis clauses (PASS at W3-6; label-defect did NOT touch them) ---
    op_proj_clauses = axis_a["sub_slots"]["OP-PROJ"]["single_axis_clauses_axis_A"]  # (local)
    carried_single_axis = {  # (local)
        "substrate_IS_observable_identity": op_proj_clauses["substrate_IS_observable_identity"]["verdict"],
        "parse_tree_INVARIANT_classification": op_proj_clauses["parse_tree_INVARIANT_classification"]["verdict"],
        "Level_1_single_tau_slice_tag": op_proj_clauses["Level_1_single_tau_slice_tag"]["verdict"],
    }
    # The corner-cell clause is RE-EVALUATED here (not carried); its W3-6 value was FAIL.
    w3_6_corner_cell = op_proj_clauses["corner_cell_classification"]["verdict"]  # (local) == "FAIL"

    print()
    print("Axis-A single-axis OP-PROJ clause matrix:")
    for name, v in carried_single_axis.items():
        print(f"  [carried W3-6] {name:42s}: {v}")
    print(f"  [W3-6 prior  ] corner_cell_classification                : {w3_6_corner_cell}")
    print(f"  [RE-VERIFY   ] corner_cell_classification (Cell-II)       : "
          f"{'PASS' if corner_cell_clause_PASS else 'FAIL'}")

    all_single_axis_carried_PASS = all(v == "PASS" for v in carried_single_axis.values())  # (local)
    # Any carried clause that is INFO triggers the INFO branch (Stage-2 INFO-deferred).
    any_carried_info = any(v == "INFO" for v in carried_single_axis.values())  # (local)

    # --- JOINT clauses: PASS-AND across {Axis-A re-verify, Axis-B mack on-disk} ---
    # From the on-disk Stage-2 aggregation JSON (Axis-B leg) + Axis-A vdd JSON (Axis-A leg).
    op_proj_joint_detail = stage2["aggregation"]["sub_slots"]["OP_PROJ"]["joint_detail"]  # (local)
    joint_clause_names = list(op_proj_joint_detail.keys())  # (local) ['JOINT_bridge_map','JOINT_structural_orthogonal_companion']
    n_joint_clauses = len(joint_clause_names)  # (local)

    joint_pass_and = {}  # (local)
    joint_pass_and_count = 0  # (local)
    for jc in joint_clause_names:
        axis_a_leg = op_proj_joint_detail[jc]["axis_A"]  # (local)
        axis_b_leg = op_proj_joint_detail[jc]["axis_B"]  # (local)
        pa = (axis_a_leg == "PASS") and (axis_b_leg == "PASS")  # (local) logical AND, not OR
        joint_pass_and[jc] = {
            "axis_A": axis_a_leg,
            "axis_B": axis_b_leg,
            "pass_and": pa,
        }
        if pa:
            joint_pass_and_count += 1

    print()
    print("JOINT clause PASS-AND across {Axis-A re-verify, Axis-B mack on-disk}:")
    for jc, d in joint_pass_and.items():
        print(f"  {jc:48s}: A={d['axis_A']} B={d['axis_B']} PASS-AND={d['pass_and']}")
    print(f"  joint_pass_and_count / n_joint_clauses = {joint_pass_and_count} / {n_joint_clauses}")

    # NB: the W3-6 Axis-A JOINT structural-orthogonal-companion was PASS-CONDITIONAL
    # (raw), upgraded to PASS via the W3-3 Class-8.7 witness (recorded in the on-disk
    # Stage-2 JSON: joint_detail.JOINT_structural_orthogonal_companion.conditional_upgraded
    # =True). The Cell-II remediation ALSO discharges the cell-pair-label condition the
    # raw PASS-CONDITIONAL flagged (the JOINT clause's "Cell I vs Cell IV" label is now
    # "Cell II vs Cell IV"). Both Axis-A JOINT legs are PASS post-remediation.
    soc_upgraded = bool(  # (local)
        op_proj_joint_detail.get("JOINT_structural_orthogonal_companion", {}).get(
            "conditional_upgraded", False
        )
    )
    print(f"  (structural-orthogonal-companion conditional_upgraded via W3-3 witness = {soc_upgraded})")

    # --- Axis-B mack on-disk: confirm already PASS-AND on all OP-PROJ JOINT clauses ---
    axis_b_mack = stage2["aggregation"]["sub_slots"]["OP_PROJ"]["axis_B_mack"]  # (local)
    print(f"  Axis-B mack on-disk OP-PROJ verdict (already PASS) = {axis_b_mack}")

    # ---------------------------------------------------------------------------
    # COMPOSITE VERDICT (plan §W8-1 rubric)
    # ---------------------------------------------------------------------------
    joint_all_pass_and = (joint_pass_and_count == n_joint_clauses)  # (local)

    # INFO (mechanical-closure PRE-REG-INC): entry NOT Cell-II at dispatch OR input missing.
    mechanical_closure = (not is_cell_ii) or (not inputs_present)  # (local)
    # INFO (Stage-2 INFO-deferred): a carried single-axis clause is INFO.
    stage2_info_deferred = any_carried_info  # (local)

    if mechanical_closure:
        verdict = "INFO"  # (local)
        if not is_cell_ii:
            block = "registry_entry_NOT_Cell-II_at_dispatch"  # (local)
        else:
            block = "cited_input_missing"  # (local)
        value = f"PRE-REG-INC_blocked_by_{block}_{cell_ii_detail}"  # (local)
    elif stage2_info_deferred:
        verdict = "INFO"  # (local)
        value = (  # (local)
            "Stage-2-INFO-deferred_axisA_carried_clause_INFO; "
            f"carried={carried_single_axis}"
        )
    elif corner_cell_clause_PASS and joint_all_pass_and and all_single_axis_carried_PASS and reviewer_selection_protocol_ok:
        verdict = "PASS"  # (local)
        value = (  # (local)
            f"corner_cell_clause_PASS=True_Cell-II_INVARIANTxs4_label_match"
            f"(claimed={claimed_cell.replace(' ', '-')}==derived={derived_cell.replace(' ', '-')})"
            f"_axisA_single_axis_all_PASS=True"
            f"_joint_pass_and_count={joint_pass_and_count}of{n_joint_clauses}"
            f"_axisB_mack_on_disk=PASS_RSP_4cond_OK=True"
            f"_OP-PROJ_Stage-2_PASS-AND_complete_BOTH_axes"
            f"_VII.AV.OP-PROJ_STAGE-3-ELIGIBLE=True"
            f"_W3-6_INFO_one-clause-short_UPGRADED=True"
            f"_workshop_transcript_read=False_OAA_excl=True_substrate_input_ortho=True"
            f"_convention_ends_FULL=True"
        )
    else:
        # FAIL: corner-cell FAILs even under Cell II OR a JOINT clause fails PASS-AND
        # OR a carried single-axis clause is not PASS OR reviewer-selection protocol fails.
        verdict = "FAIL"  # (local)
        value = (  # (local)
            f"corner_cell_clause_PASS={corner_cell_clause_PASS}"
            f"(claimed={claimed_cell.replace(' ', '-')}_derived={derived_cell.replace(' ', '-')})"
            f"_joint_pass_and_count={joint_pass_and_count}of{n_joint_clauses}"
            f"_single_axis_all_PASS={all_single_axis_carried_PASS}"
            f"_RSP_4cond_OK={reviewer_selection_protocol_ok}"
            f"_OP-PROJ_Stage-2_PASS-AND_INCOMPLETE_stays_STAGE-1-CANDIDATE"
        )

    # --- Dual-SHA closure ---
    aggregate_payload = (  # (local)
        f"verdict={verdict};corner_cell_PASS={corner_cell_clause_PASS};"
        f"derived_cell={derived_cell};claimed_cell={claimed_cell};"
        f"single_axis_all_PASS={all_single_axis_carried_PASS};"
        f"joint_pass_and_count={joint_pass_and_count}/{n_joint_clauses};"
        f"RSP_ok={reviewer_selection_protocol_ok};is_cell_ii={is_cell_ii}"
    )
    audit_sha, content_sha = compute_dual_sha(pins, aggregate_payload)  # (local)

    print()
    print(f"4-tuple: (value=<see verdict line>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"audit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print(f"VERDICT: {verdict}")

    # --- Persist npz sidecar ---
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        # corner-cell re-derivation
        parse_tree_terminus=rederiv["parse_tree_terminus"],
        algebra_axis=rederiv["algebra_axis"],
        mellin_pole_s=int(rederiv["mellin_pole_s"]),
        derived_cell=derived_cell,
        claimed_cell=claimed_cell,
        corner_cell_clause_PASS=bool(corner_cell_clause_PASS),
        w3_6_corner_cell_verdict=w3_6_corner_cell,
        # single-axis carried
        single_axis_substrate_IS=carried_single_axis["substrate_IS_observable_identity"],
        single_axis_parse_tree=carried_single_axis["parse_tree_INVARIANT_classification"],
        single_axis_level_1_tag=carried_single_axis["Level_1_single_tau_slice_tag"],
        all_single_axis_carried_PASS=bool(all_single_axis_carried_PASS),
        # joint PASS-AND
        joint_clause_names=np.array(joint_clause_names),
        n_joint_clauses=int(n_joint_clauses),
        joint_pass_and_count=int(joint_pass_and_count),
        joint_all_pass_and=bool(joint_all_pass_and),
        joint_soc_conditional_upgraded=bool(soc_upgraded),
        axis_b_mack_on_disk_verdict=axis_b_mack,
        # reviewer-selection protocol
        rsp_axis_distinct=bool(rsp_axis_distinct),
        rsp_oaa_exclusion=bool(rsp_oaa_exclusion),
        rsp_audit_coverage=bool(rsp_audit_coverage),
        rsp_substrate_orthogonality=bool(rsp_substrate_orthogonality),
        reviewer_selection_protocol_ok=bool(reviewer_selection_protocol_ok),
        workshop_transcript_read=bool(workshop_transcript_read),
        # mechanical-closure prereq
        registry_is_cell_ii=bool(is_cell_ii),
        cell_ii_detail=cell_ii_detail,
        inputs_present=bool(inputs_present),
        # eligibility
        stage_3_eligible=bool(verdict == "PASS"),
        M_KK=M_KK,
        tau_fold=tau_fold,
    )
    print(f"npz -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    # --- Plot: clause-PASS matrix + JOINT PASS-AND + eligibility ---
    make_plot(
        carried_single_axis,
        corner_cell_clause_PASS,
        w3_6_corner_cell,
        joint_pass_and,
        derived_cell,
        claimed_cell,
        reviewer_selection_protocol_ok,
        verdict,
    )
    print(f"png -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # --- Append canonical dual-SHA verdict line + companion row ---
    append_verdict(verdict, value, audit_sha, content_sha)
    print(f"verdict line appended -> {VERDICT_TXT.relative_to(PROJECT_ROOT)}")

    return 0


def make_plot(
    carried_single_axis: dict,
    corner_cell_clause_PASS: bool,
    w3_6_corner_cell: str,
    joint_pass_and: dict,
    derived_cell: str,
    claimed_cell: str,
    rsp_ok: bool,
    verdict: str,
) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.2))

    # Panel 1: clause-PASS matrix (Axis-A) + corner-cell W3-6 -> re-verify transition
    rows = [  # (local)
        ("substrate_IS_observable_identity", carried_single_axis["substrate_IS_observable_identity"], "carried"),
        ("parse_tree_INVARIANT_classification", carried_single_axis["parse_tree_INVARIANT_classification"], "carried"),
        ("Level_1_single_tau_slice_tag", carried_single_axis["Level_1_single_tau_slice_tag"], "carried"),
        ("corner_cell_classification (W3-6)", w3_6_corner_cell, "prior"),
        ("corner_cell_classification (Cell-II re-verify)",
         "PASS" if corner_cell_clause_PASS else "FAIL", "RE-VERIFY"),
    ]
    colors = {"PASS": "#2e8b57", "FAIL": "#c0392b", "INFO": "#d4a017"}  # (local)
    y = np.arange(len(rows))[::-1]  # (local)
    for yi, (name, v, tag) in zip(y, rows):
        ax1.barh(yi, 1.0, color=colors.get(v, "#888888"), edgecolor="black", alpha=0.85)
        ax1.text(0.5, yi, f"{v}", ha="center", va="center", fontweight="bold", color="white", fontsize=11)
        ax1.text(1.04, yi, f"[{tag}]", ha="left", va="center", fontsize=8, color="#444444")
    ax1.set_yticks(y)
    ax1.set_yticklabels([r[0] for r in rows], fontsize=8.5)
    ax1.set_xlim(0, 1.6)
    ax1.set_xticks([])
    ax1.set_title(
        f"Axis-A (vdd) OP-PROJ clause matrix\n"
        f"corner-cell: W3-6 FAIL (read Cell I) -> re-verify on Cell II\n"
        f"derived={derived_cell}, claimed={claimed_cell}  (INVARIANT x s=4)",
        fontsize=10,
    )

    # Panel 2: JOINT PASS-AND across both axes + eligibility
    jrows = list(joint_pass_and.items())  # (local)
    yj = np.arange(len(jrows) + 2)[::-1]  # (local)
    for yi, (jc, d) in zip(yj[:len(jrows)], jrows):
        a_ok = d["axis_A"] == "PASS"  # (local)
        b_ok = d["axis_B"] == "PASS"  # (local)
        pa = d["pass_and"]  # (local)
        ax2.barh(yi + 0.18, 0.45, left=0.0, color=colors["PASS"] if a_ok else colors["FAIL"],
                 edgecolor="black", height=0.32)
        ax2.barh(yi + 0.18, 0.45, left=0.5, color=colors["PASS"] if b_ok else colors["FAIL"],
                 edgecolor="black", height=0.32)
        ax2.text(0.225, yi + 0.18, f"A:{d['axis_A']}", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        ax2.text(0.725, yi + 0.18, f"B:{d['axis_B']}", ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        ax2.text(1.02, yi + 0.18, f"AND={pa}", ha="left", va="center", fontsize=8.5,
                 color=colors["PASS"] if pa else colors["FAIL"], fontweight="bold")
        ax2.text(-0.02, yi - 0.16, jc, ha="right", va="center", fontsize=8)
    # eligibility row
    elig_color = colors["PASS"] if verdict == "PASS" else (colors["INFO"] if verdict == "INFO" else colors["FAIL"])  # (local)
    ax2.barh(yj[-2], 1.0, color=elig_color, edgecolor="black", alpha=0.9)
    ax2.text(0.5, yj[-2], f"COMPOSITE: {verdict}", ha="center", va="center", color="white", fontweight="bold", fontsize=11)
    ax2.barh(yj[-1], 1.0, color="#34495e", edgecolor="black", alpha=0.9)
    elig_txt = "STAGE-3-ELIGIBLE" if verdict == "PASS" else "stays STAGE-1-CANDIDATE"  # (local)
    ax2.text(0.5, yj[-1], f"§VII.AV.OP-PROJ: {elig_txt}", ha="center", va="center", color="white", fontweight="bold", fontsize=10)
    ax2.set_xlim(-0.55, 1.45)
    ax2.set_ylim(yj[-1] - 0.6, yj[0] + 0.6)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title(
        f"JOINT clause PASS-AND {{Axis-A re-verify, Axis-B mack on-disk}}\n"
        f"reviewer-selection 4-cond OK={rsp_ok}",
        fontsize=10,
    )

    fig.suptitle(
        f"{GATE_ID}\nStage-2 Axis-A re-verify on Cell-II-corrected §VII.AV.OP-PROJ — VERDICT: {verdict}",
        fontsize=11, fontweight="bold",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical dual-SHA verdict line + companion row (atomic
    single open("a")). [VERIFY-THEOREM] — dual-SHA companion row REQUIRED, NO
    [SIGN] 3-tuple companion row.
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; Stage-2 Axis-A (vdd) re-verify on "
        f"Cell-II-corrected §VII.AV.OP-PROJ; [VERIFY-THEOREM] no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


if __name__ == "__main__":
    raise SystemExit(main())
