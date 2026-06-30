#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S94-VII-AX-STATE-PROJ-STAGE-2-CROSS-AXIS-VERIFY  (aggregation / emission)
========================================================================

MECHANICAL Stage-2 aggregation (gen-physicist, aggregation-emission author) of
the TWO completed cross-reviewer JSONs into the single composite §W4-1 verdict.
The reviewers' INDEPENDENCE is the physics; this script does the deterministic
boolean PASS-AND + verdict emission ONLY. It does NOT re-derive any clause.

Architecture mirrors the S93 W3-6 §VII.AV single-shot Stage-2 aggregation
(`computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.py`), but the
two S94 W4-1 reviewer JSONs use a FLAT schema (top-level `axisA_single_axis_all`
/ `axisB_single_axis_all`, `joint.{E1,E3,E4}`, `substrate_input_anchor`), so the
aggregation is a direct boolean roll-up — no nested sub-slot key reconciliation.

Reads (read-only; SHAs feed audit_sha256):
    computations/session-94/s94_w4_1_axis_a_vdd_vii_ax_state_proj_verdicts.json
    computations/session-94/s94_w4_1_axis_b_transit_vii_ax_state_proj_verdicts.json

Composite PASS-AND boundary (per plan §W4-1 operator + strict_PASS_boundary):

    composite == 'PASS'  IFF
        (axisA_single_axis_all == PASS)
        AND (axisB_single_axis_all == PASS)
        AND (E1, E3, E4 EACH PASS-AND across BOTH axes : logical AND, not OR)
        AND substrate_input_orthogonality (the two reviewers' substrate_input_anchor
            values are DISTINCT : >=1 obs loaded by exactly ONE reviewer)
        AND OAA_exclusion {mack-cosmic-bridge, connes-ncg, volovik} satisfied
        AND neither reviewer read a workshop transcript (downstream-inheritance reach)
        AND convention ends with -FULL.
    composite == 'FAIL'  iff a per-clause FAIL on EITHER axis on ANY clause, OR a
        JOINT clause not PASS-AND, OR a structural-gate FAIL (orthogonality / OAA /
        convention).
    composite == 'INFO'  iff no hard FAIL but >=1 reviewer returns INFO on a clause
        (Stage-2-INFO-deferred; the STATE-PROJ entry stays STAGE-1-CANDIDATE).

ELEMENT-5-HOLD (load-bearing substitution chain; per plan §W4-1 substitution_chain):
    A composite PASS promotes the §VII.AX.STATE-PROJ theorem-STRUCTURE to
    STAGE-3-PERMANENT-ELIGIBLE *only*. The inherited Tier-2-dimensionful m^-3
    Level-3 row stays HELD NOT-SATISFIED-PENDING (re-determination
    CF-S94-N-PBH-TRUNCATION-ANCHOR). composite_PASS EXCLUDES the Element-5 m^-3
    term by construction => composite_PASS is INDEPENDENT of the inherited HOLD.
    The Element-4 binding envelope rides the SATURATED bottom-K Bogoliubov channel
    (d(bottom-K)/dL -> 0), STRUCTURALLY DISTINCT from the OP-PROJ N_eigs total-count
    channel (dN_eigs/dL = (4/3)L^4 -> +inf, DIVERGENT) that carries the HOLD. A
    Stage-2 PASS does NOT (and MUST NOT) assert a registry-PASS the parent no longer
    claims.

EMISSION GUARD: no verdict line unless BOTH axis JSONs are present AND `--emit` is
passed. Running without `--emit` performs the aggregation dry-run (prints the
computed PASS-AND + the verdict line it WOULD emit) and writes the JSON sidecar +
.npz clause-by-reviewer matrix, but appends NO verdict line.

Trigger: [VERIFY-THEOREM]. Dual-SHA: content_sha256 over this script;
audit_sha256 over the input-pin map + both axis verdict SHAs + the STAGE-1 entry
SHA (§VII.AX.STATE-PROJ registry block) + OP-PROJ STAGE-3 baseline SHA + the
joint-theorem-promotion.md SHA + per-gate identity keys (gate-distinct per
mechanical-closure-discipline item 3).
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Delta_BCS,
    n_PBH_FW_central,
)

import numpy as np  # noqa: E402  (clause-by-reviewer PASS-AND matrix .npz)

# ---------------------------------------------------------------------------
# Gate identity + canonical paths (per plan §W4-1 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S94-VII-AX-STATE-PROJ-STAGE-2-CROSS-AXIS-VERIFY"  # (local)
SCHEME = "joint-theorem-promotion-Stage-2-single-sub-slot-parallel-cross-axis-PASS-AND"  # (local)
# convention MUST end with -FULL (the registered STATE-PROJ ladder's CLASS pins are
# FULL; the inherited OP-PROJ T1.13 anchor is FULL-class).
CONVENTION = (  # (local)
    "Stage-2-VII-AX-STATE-PROJ-vdd-AxisA-transit-AxisB-PARALLEL-OAA-exclusion-"
    "mack-connes-volovik-substrate-input-orthogonality-K3-FULL"
)
L_MAX = "14"  # (local) STATE-PROJ Level-1 single-tau-slice + Element-5 inheritance pinned at L_max=14

# OAA exclusion set (the W4-4 companion-landing author + downstream-inheritance reach):
#   mack  = Stage-1 sole-writer of the §VII.AX.STATE-PROJ companion landing.
#   connes/volovik = Axis-A/Axis-B reviewers of the chained §VII.AX OP-PROJ +
#   MULTI-PIN-ATLAS cluster the STATE-PROJ companion CHAINS on.
OAA_EXCLUSION = {"mack", "connes", "volovik"}  # (local)

# --- the THREE JOINT clauses PASS-AND'd across both axes (plan §W4-1 line 122) ---
JOINT_CLAUSES = ("E1", "E3", "E4")  # (local)

# Canonical paths.
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w4_1_vii_ax_state_proj_stage_2_cross_axis_verify.json"
)
NPZ_PATH = (  # (local) clause-by-reviewer PASS-AND matrix
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w4_1_vii_ax_state_proj_stage_2_cross_axis_verify.npz"
)
AXIS_A_JSON = (  # (local) Axis-A (van-den-dungen) verdicts — read-only at aggregation
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w4_1_axis_a_vdd_vii_ax_state_proj_verdicts.json"
)
AXIS_B_JSON = (  # (local) Axis-B (transit-dynamics) verdicts — read-only at aggregation
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w4_1_axis_b_transit_vii_ax_state_proj_verdicts.json"
)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
S93_VERDICT_TXT = (  # (local) source of W4-4 companion-landing PASS (CHAINED prereq) + OP-PROJ STAGE-3 chain
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
JOINT_THEOREM_RULE = (  # (local)
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)

# substrate-input-orthogonality canonical pins (plan §W4-1 substrate_input_orthogonality_obs).
# obs_STATE loaded by Axis-A ONLY; obs_OP loaded by Axis-B ONLY.
OBS_STATE_NPZ = (  # (local)
    PROJECT_ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz"
)
# Plan names obs_OP as s93_w4_3_vii_ax_op_proj_n_eigs_growth.npz; the on-disk canonical
# carrying the identical N_eigs cardinality-cascade is the factorization npz (plan-text
# drift resolved per substrate-first-canonical-sourcing.md §(ii.B); Axis-B documented
# this in its own JSON: substrate_input_anchor_ondisk).
OBS_OP_NPZ_PLAN = "s93_w4_3_vii_ax_op_proj_n_eigs_growth.npz"  # (local)
OBS_OP_NPZ_ONDISK = (  # (local)
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_3_n_pbh_canonical_truncation_factorization.npz"
)

# CHAINED prerequisite (defensive guard per plan "Wave 4 Decision Point Prerequisites"):
# §VII.AX.STATE-PROJ STAGE-1-CANDIDATE landed at S93 W4-4 (PASS). If absent at runtime,
# honest mechanical closure per mechanical-closure-discipline.md.
W4_4_GATE = "S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING"  # (local)

# Input-pin map (source docs the aggregation consumes; SHAs feed audit_sha256). obs_OP
# pinned to the on-disk canonical (drift-resolved); obs_STATE Axis-A only.
INPUT_FILES = [  # (local)
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S93_VERDICT_TXT,
    AXIS_A_JSON,
    AXIS_B_JSON,
    OBS_STATE_NPZ,
    OBS_OP_NPZ_ONDISK,
    JOINT_THEOREM_RULE,
]


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

    content_sha256 = SHA-256 over THIS script (the aggregation logic).
    audit_sha256   = SHA-256 over the input-pin map + both axis verdict SHAs + the
                     STAGE-1 entry SHA (§VII.AX.STATE-PROJ registry) + the OP-PROJ
                     STAGE-3 baseline (W4-4 PASS) SHA + the joint-theorem-promotion.md
                     SHA + the aggregate PASS-AND payload + per-gate identity keys
                     (gate-distinct per mechanical-closure-discipline item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(Path(__file__).read_bytes())
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    axis_a_sha = sha256_of(AXIS_A_JSON)  # (local)
    axis_b_sha = sha256_of(AXIS_B_JSON)  # (local)
    registry_sha = sha256_of(REGISTRY_PATH)  # (local) §VII.AX.STATE-PROJ Stage-1 entry + OP-PROJ STAGE-3 baseline
    rule_sha = sha256_of(JOINT_THEOREM_RULE)  # (local)
    w4_4_sha = _w4_4_companion_landing_sha()  # (local) the OP-PROJ STAGE-3 chain prereq

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(
        (
            f"axisA={axis_a_sha}|axisB={axis_b_sha}|"
            f"stage_1_entry_sha={registry_sha}|"
            f"op_proj_stage_3_baseline_w4_4_sha={w4_4_sha}|"
            f"joint_theorem_rule_sha={rule_sha}|{aggregate_payload}"
        ).encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


def _w4_4_companion_landing_sha() -> str:
    """Extract the audit_sha256 of the S93 W4-4 §VII.AX.STATE-PROJ companion-landing
    PASS line from the S93 verdict file (the CHAINED Stage-1-CANDIDATE prereq + the
    OP-PROJ STAGE-3 chain). Returns the 64-char SHA or '0'*64 if absent.
    """
    if not S93_VERDICT_TXT.exists():
        return "0" * 64
    for ln in S93_VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{W4_4_GATE}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                return m.group(1)
    return "0" * 64


def _w4_4_landed() -> bool:
    """CHAINED prerequisite check (defensive guard): the §VII.AX.STATE-PROJ
    STAGE-1-CANDIDATE landed at S93 W4-4 with verdict PASS.
    """
    if not S93_VERDICT_TXT.exists():
        return False
    for ln in S93_VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{W4_4_GATE}:") and ln.split(":", 1)[1].lstrip().startswith("PASS"):
            return True
    return False


# ---------------------------------------------------------------------------
# FLAT-schema clause readers (the W4-1 reviewer JSONs are flat, not nested)
# ---------------------------------------------------------------------------
def _norm(v) -> str:
    """Normalize a verdict token to PASS/FAIL/INFO/ABSENT (uppercase)."""
    if not isinstance(v, str):
        return "ABSENT"
    m = re.search(r"\b(PASS|FAIL|INFO)\b", v.upper())  # (local)
    return m.group(1) if m else "ABSENT"


def _single_axis_all(axis_json: dict, key: str) -> str:
    """Read the reviewer's single-axis roll-up boolean (`axisA_single_axis_all` /
    `axisB_single_axis_all`). If the explicit roll-up key is absent, aggregate the
    per-clause verdicts under the `single_axis` block.
    """
    v = axis_json.get(key)  # (local)
    if isinstance(v, str):
        return _norm(v)
    # fallback: roll up the single_axis clause block
    sa = axis_json.get("single_axis", {})  # (local)
    if isinstance(sa, dict) and sa:
        verds = [_norm(x) for x in sa.values()]  # (local)
        if any(x == "FAIL" for x in verds):
            return "FAIL"
        if any(x == "INFO" for x in verds):
            return "INFO"
        return "PASS" if all(x == "PASS" for x in verds) else "ABSENT"
    return "ABSENT"


def _joint_verdict(axis_json: dict, clause: str) -> str:
    """Read a JOINT clause verdict (E1/E3/E4) from the flat `joint` block."""
    jt = axis_json.get("joint", {})  # (local)
    if isinstance(jt, dict):
        return _norm(jt.get(clause))
    return "ABSENT"


def _substrate_input_anchor(axis_json: dict) -> str:
    """Read the reviewer's substrate_input_anchor string (the obs it loaded)."""
    v = axis_json.get("substrate_input_anchor")  # (local)
    return v if isinstance(v, str) else ""


def _reviewer(axis_json: dict) -> str:
    return str(axis_json.get("reviewer", "")).lower()  # (local)


def _read_workshop_transcript(axis_json: dict) -> bool:
    """True iff the reviewer's independence attestation says it read a workshop
    transcript. Default-safe: absent flag => not read => False.
    """
    att = axis_json.get("independence_attestation", {})  # (local)
    if isinstance(att, dict):
        for k, v in att.items():
            kl = k.lower()  # (local)
            if "workshop_transcript" in kl or "read_workshop" in kl:
                if isinstance(v, bool):
                    return v
    return False


# ---------------------------------------------------------------------------
# Aggregation — the strict PASS-AND boundary (plan §W4-1 operator)
# ---------------------------------------------------------------------------
def aggregate(axis_a: dict, axis_b: dict) -> dict:
    # --- single-axis roll-ups ---
    a_single = _single_axis_all(axis_a, "axisA_single_axis_all")  # (local)
    b_single = _single_axis_all(axis_b, "axisB_single_axis_all")  # (local)

    # --- JOINT clause PASS-AND across both axes (logical AND, not OR) ---
    joint_detail: dict = {}  # (local)
    joint_pass_and_all = True  # (local)
    any_joint_fail = False  # (local)
    any_joint_info = False  # (local)
    for c in JOINT_CLAUSES:
        a_v = _joint_verdict(axis_a, c)  # (local)
        b_v = _joint_verdict(axis_b, c)  # (local)
        clause_pass_and = (a_v == "PASS" and b_v == "PASS")  # (local)
        joint_detail[c] = {"axis_A": a_v, "axis_B": b_v, "pass_and": clause_pass_and}
        joint_pass_and_all = joint_pass_and_all and clause_pass_and
        if a_v == "FAIL" or b_v == "FAIL":
            any_joint_fail = True
        if a_v == "INFO" or b_v == "INFO":
            any_joint_info = True

    # --- substrate-input-orthogonality: the two anchors DISTINCT (>=1 obs single-reviewer) ---
    a_anchor = _substrate_input_anchor(axis_a)  # (local)
    b_anchor = _substrate_input_anchor(axis_b)  # (local)
    anchors_distinct = bool(a_anchor) and bool(b_anchor) and (a_anchor != b_anchor)  # (local)
    # cross-check the anchors against the canonical pins (obs_STATE Axis-A; obs_OP Axis-B)
    a_is_state = "s91_w5_1_full_bdg_pv" in a_anchor  # (local)
    b_is_op = ("s93_w4_3" in b_anchor) or ("n_pbh_canonical_truncation_factorization" in b_anchor)  # (local)
    # structural ceiling iff anchors distinct AND match the expected obs assignment
    orthogonality_structural_ceiling = anchors_distinct and a_is_state and b_is_op  # (local)
    # floor predicate: >=1 obs loaded by exactly one reviewer (distinctness suffices)
    orthogonality_floor = anchors_distinct  # (local)

    # --- OAA-exclusion {mack, connes, volovik} satisfied by BOTH reviewers ---
    a_rev = _reviewer(axis_a)  # (local)
    b_rev = _reviewer(axis_b)  # (local)
    oaa_ok = (
        not any(x in a_rev for x in OAA_EXCLUSION)
        and not any(x in b_rev for x in OAA_EXCLUSION)
    )  # (local)

    # --- neither reviewer read a workshop transcript (downstream-inheritance reach) ---
    a_read_ws = _read_workshop_transcript(axis_a)  # (local)
    b_read_ws = _read_workshop_transcript(axis_b)  # (local)
    no_workshop_transcript = (not a_read_ws) and (not b_read_ws)  # (local)

    # --- convention ends with -FULL ---
    convention_ends_full = CONVENTION.endswith("-FULL")  # (local)

    # --- composite collapse (plan §W4-1 strict_PASS_boundary) ---
    single_axes_pass = (a_single == "PASS" and b_single == "PASS")  # (local)
    structural_gates_pass = (
        orthogonality_floor and oaa_ok and no_workshop_transcript and convention_ends_full
    )  # (local)
    composite_pass = single_axes_pass and joint_pass_and_all and structural_gates_pass  # (local)

    # hard-FAIL drivers: any per-clause FAIL (single-axis OR joint), a joint not PASS-AND,
    # OR a structural-gate FAIL.
    hard_fail = (
        (a_single == "FAIL")
        or (b_single == "FAIL")
        or any_joint_fail
        or (not joint_pass_and_all)
        or (not structural_gates_pass)
    )  # (local)
    # INFO: no hard FAIL but >=1 reviewer INFO on a clause (single-axis or joint)
    info = (
        (not composite_pass)
        and (not hard_fail)
        and (a_single == "INFO" or b_single == "INFO" or any_joint_info)
    )  # (local)

    if composite_pass:
        composite = "PASS"  # (local)
    elif hard_fail:
        composite = "FAIL"  # (local)
    elif info:
        composite = "INFO"  # (local)
    else:
        composite = "FAIL"  # (local)

    stage_3 = (
        "STAGE-3-PERMANENT-ELIGIBLE" if composite == "PASS"
        else "STAGE-1-CANDIDATE"
    )  # (local)

    return {
        "axisA_single_axis_all": a_single,
        "axisB_single_axis_all": b_single,
        "single_axes_pass": single_axes_pass,
        "joint_clauses": list(JOINT_CLAUSES),
        "joint_detail": joint_detail,
        "joint_pass_and_all": joint_pass_and_all,
        "substrate_input_orthogonality": {
            "axis_A_anchor": a_anchor,
            "axis_B_anchor": b_anchor,
            "anchors_distinct": anchors_distinct,
            "axis_A_is_obs_STATE": a_is_state,
            "axis_B_is_obs_OP": b_is_op,
            "structural_ceiling_NO_caveat": orthogonality_structural_ceiling,
            "predicate_satisfied_>=1_obs": orthogonality_floor,
            "obs_OP_plan_name": OBS_OP_NPZ_PLAN,
            "obs_OP_ondisk_resolved": "s93_w4_3_n_pbh_canonical_truncation_factorization.npz",
            "plan_text_drift_resolved_per": "substrate-first-canonical-sourcing.md §(ii.B)",
        },
        "oaa_exclusion_satisfied": oaa_ok,
        "oaa_exclusion_set": sorted(OAA_EXCLUSION),
        "no_workshop_transcript_read": no_workshop_transcript,
        "convention_ends_FULL": convention_ends_full,
        "structural_gates_pass": structural_gates_pass,
        "composite_hard_fail": hard_fail,
        "composite_info": info,
        "composite_verdict": composite,
        "stage_3_status": stage_3,
        # Element-5-HOLD: the inherited dimensionful m^-3 Level-3 row is HELD; a Stage-2
        # PASS does NOT assert the m^-3 registry-PASS (substitution chain in module docstring).
        "element5_m3_level3_row": {
            "status": "HELD NOT-SATISFIED-PENDING (Tier-2-dimensionful; inherited from §VII.AX.OP-PROJ T1.13)",
            "n_PBH_FW_central_m3": n_PBH_FW_central,
            "asserted_by_composite_PASS": False,
            "re_determination_CF": "CF-S94-N-PBH-TRUNCATION-ANCHOR",
            "channel_distinction": (
                "Element-4 binding envelope rides the SATURATED bottom-K Bogoliubov "
                "channel (d(bottom-K)/dL -> 0); STRUCTURALLY DISTINCT from the OP-PROJ "
                "N_eigs total-count channel (dN_eigs/dL = (4/3)L^4 -> +inf, DIVERGENT) "
                "that carries the HOLD."
            ),
        },
    }


def build_value_field(agg: dict) -> str:
    """Compact value= payload (verdict is DATA). Names both axis single-axis verdicts,
    each JOINT-clause PASS-AND, substrate-input-orthogonality, OAA, convention, the
    Stage-3 eligibility, and the Element-5 m^-3 HOLD (NOT asserted by composite PASS).
    """
    jd = agg["joint_detail"]  # (local)
    so = agg["substrate_input_orthogonality"]  # (local)
    return (
        f"composite={agg['composite_verdict']};"
        f"stage3_eligible={agg['composite_verdict'] == 'PASS'};"
        f"axisA_single_axis_all={agg['axisA_single_axis_all']};"
        f"axisB_single_axis_all={agg['axisB_single_axis_all']};"
        f"E1_PASS-AND={jd['E1']['pass_and']};"
        f"E3_PASS-AND={jd['E3']['pass_and']};"
        f"E4_PASS-AND={jd['E4']['pass_and']};"
        f"joint_pass_and_all={agg['joint_pass_and_all']};"
        f"substrate_input_orthogonality={so['predicate_satisfied_>=1_obs']};"
        f"structural_ceiling_NO_caveat={so['structural_ceiling_NO_caveat']};"
        f"axisA_anchor_obs_STATE={so['axis_A_is_obs_STATE']};"
        f"axisB_anchor_obs_OP={so['axis_B_is_obs_OP']};"
        f"OAA_excl_satisfied={agg['oaa_exclusion_satisfied']};"
        f"no_workshop_transcript={agg['no_workshop_transcript_read']};"
        f"convention_ends_FULL={agg['convention_ends_FULL']};"
        f"stage_3_status={agg['stage_3_status']};"
        f"element5_m3_Level3_HELD_NOT-SATISFIED-PENDING=True;"
        f"element5_m3_asserted_by_composite_PASS=False;"
        f"m3_re_determination_CF=CF-S94-N-PBH-TRUNCATION-ANCHOR"
    )


# ---------------------------------------------------------------------------
# Emission
# ---------------------------------------------------------------------------
def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append a single canonical dual-SHA verdict line + companion row (atomic single
    open("a") write; no read-modify-write, no truncate). [VERIFY-THEOREM]: no [SIGN]
    3-tuple. No supersedes tag (no prior S94 §VII.AX.STATE-PROJ Stage-2 line on disk).
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
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"Stage-2 cross-axis PASS-AND (vdd Axis-A + transit-dynamics Axis-B); "
        f"[VERIFY-THEOREM] no [SIGN] 3-tuple; "
        f"composite PASS -> §VII.AX.STATE-PROJ theorem-STRUCTURE STAGE-3-PERMANENT-ELIGIBLE "
        f"(orchestrator flips registry tag at wave close); inherited dimensionful m^-3 "
        f"Level-3 row HELD NOT-SATISFIED-PENDING (CF-S94-N-PBH-TRUNCATION-ANCHOR)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def write_npz(agg: dict) -> None:
    """Clause-by-reviewer PASS-AND matrix (rows = clauses, cols = [Axis-A, Axis-B, PASS-AND]).
    Verdict encoding: PASS=1, INFO=0, FAIL=-1, ABSENT=-2.
    """
    enc = {"PASS": 1, "INFO": 0, "FAIL": -1, "ABSENT": -2}  # (local)
    rows = []  # (local) clause labels
    mat = []  # (local) [axisA, axisB, pass_and(1/0)]
    # single-axis roll-up rows
    rows.append("axisA_single_axis_all")
    mat.append([enc[agg["axisA_single_axis_all"]], -2, int(agg["axisA_single_axis_all"] == "PASS")])
    rows.append("axisB_single_axis_all")
    mat.append([-2, enc[agg["axisB_single_axis_all"]], int(agg["axisB_single_axis_all"] == "PASS")])
    # JOINT clause rows
    for c in agg["joint_clauses"]:
        d = agg["joint_detail"][c]  # (local)
        rows.append(f"JOINT_{c}")
        mat.append([enc[d["axis_A"]], enc[d["axis_B"]], int(d["pass_and"])])
    matrix = np.array(mat, dtype=np.int64)  # (local)
    so = agg["substrate_input_orthogonality"]  # (local)
    np.savez(
        NPZ_PATH,
        clause_labels=np.array(rows),
        clause_by_reviewer_matrix=matrix,
        matrix_columns=np.array(["axis_A_vdd", "axis_B_transit", "pass_and"]),
        verdict_encoding=np.array(["PASS=1", "INFO=0", "FAIL=-1", "ABSENT=-2"]),
        composite_verdict=np.array([agg["composite_verdict"]]),
        single_axes_pass=np.array([agg["single_axes_pass"]]),
        joint_pass_and_all=np.array([agg["joint_pass_and_all"]]),
        substrate_input_orthogonality_floor=np.array([so["predicate_satisfied_>=1_obs"]]),
        substrate_input_orthogonality_ceiling=np.array([so["structural_ceiling_NO_caveat"]]),
        oaa_exclusion_satisfied=np.array([agg["oaa_exclusion_satisfied"]]),
        no_workshop_transcript_read=np.array([agg["no_workshop_transcript_read"]]),
        convention_ends_FULL=np.array([agg["convention_ends_FULL"]]),
        stage_3_status=np.array([agg["stage_3_status"]]),
        element5_m3_asserted_by_composite_PASS=np.array([False]),
        n_PBH_FW_central_m3=np.array([n_PBH_FW_central]),
        axis_A_anchor=np.array([so["axis_A_anchor"]]),
        axis_B_anchor=np.array([so["axis_B_anchor"]]),
        M_KK=np.array([M_KK]),
        tau_fold=np.array([tau_fold]),
        Delta_BCS=np.array([Delta_BCS]),
        L_max=np.array([int(L_MAX)]),
    )


def write_json(verdict: str, value: str, audit_sha: str, content_sha: str,
               agg: dict, emitted: bool) -> None:
    payload = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "aggregation": agg,
        "axis_A_json": str(AXIS_A_JSON.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "axis_B_json": str(AXIS_B_JSON.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "axis_A_json_sha256": sha256_of(AXIS_A_JSON),
        "axis_B_json_sha256": sha256_of(AXIS_B_JSON),
        "verdict_line_emitted": emitted,
        "canonical_constants": {
            "M_KK": M_KK,
            "tau_fold": tau_fold,
            "Delta_BCS": Delta_BCS,
            "n_PBH_FW_central": n_PBH_FW_central,
        },
    }
    JSON_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main — aggregation; emission gated behind --emit AND both-JSON presence
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()  # (local)
    ap.add_argument(
        "--emit",
        action="store_true",
        help="emit the W4-1 verdict line (separate step once BOTH axis JSONs are on "
        "disk). Without it, dry-run only (no verdict line; JSON+NPZ still written).",
    )
    args = ap.parse_args()  # (local)

    print(f"=== {GATE_ID} (aggregation / emission) ===")
    print("Input-pin SHAs (first lines of stdout):")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # --- CHAINED prerequisite (defensive guard): W4-4 companion landing PASS ---
    if not _w4_4_landed():
        value = f"PRE-REG-INC_blocked_by_{W4_4_GATE}_NOT-LANDED"  # (local)
        audit_sha, content_sha = compute_dual_sha(pins, value)  # (local)
        agg = {"composite_verdict": "PRE-REG-INC", "reason": value}  # (local)
        if args.emit:
            append_verdict("FAIL", value, audit_sha, content_sha)
            write_json("FAIL", value, audit_sha, content_sha, agg, emitted=True)
            print(f"VERDICT: FAIL (honest mechanical closure: {value})")
        else:
            write_json("FAIL", value, audit_sha, content_sha, agg, emitted=False)
            print(f"DRY-RUN: would emit FAIL (mechanical closure: {value}); --emit not set")
        return 0  # verdict is DATA; exit 0

    # --- both axis JSONs must exist before aggregation can complete ---
    if not AXIS_A_JSON.exists() or not AXIS_B_JSON.exists():
        missing = [p.name for p in (AXIS_A_JSON, AXIS_B_JSON) if not p.exists()]  # (local)
        print(f"AGGREGATION DEFERRED: axis verdict JSON(s) absent: {missing}")
        return 0  # not an error; the aggregation step has not been triggered yet

    axis_a = json.loads(AXIS_A_JSON.read_text(encoding="utf-8"))  # (local)
    axis_b = json.loads(AXIS_B_JSON.read_text(encoding="utf-8"))  # (local)

    agg = aggregate(axis_a, axis_b)  # (local)
    verdict = agg["composite_verdict"]  # (local)
    value = build_value_field(agg)  # (local)
    audit_sha, content_sha = compute_dual_sha(pins, value)  # (local)

    print("\nAggregation:")
    print(json.dumps(agg, indent=2))

    # always write the .npz clause-by-reviewer matrix (it is data, not a verdict)
    write_npz(agg)

    if not args.emit:
        write_json(verdict, value, audit_sha, content_sha, agg, emitted=False)
        print(f"\nDRY-RUN: would emit '{verdict}'. Verdict line NOT appended (--emit not set).")
        print("Verdict line the --emit step WILL append:")
        print(
            f"  {GATE_ID}: {verdict} -- value={value!r} "
            f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+"
        )
        return 0

    # --- EMIT (separate step) ---
    append_verdict(verdict, value, audit_sha, content_sha)
    write_json(verdict, value, audit_sha, content_sha, agg, emitted=True)
    print(f"\nVERDICT: {verdict} (emitted)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
