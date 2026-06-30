#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT
=======================================================

Two-agent parallel Stage-2 cross-axis independent-verify (per
`.claude/rules/joint-theorem-promotion.md §"Stage 2"`), dispatched per sub-slot
({§VII.AV.OP-PROJ, §VII.AV.STATE-PROJ} × {Axis-A vdd, Axis-B mack}). This is the
AGGREGATION / EMISSION script: it READS both axes' verdict JSONs

    computations/session-93/s93_w3_6_axis_a_vdd_verdicts.json   (Axis-A, vdd)
    computations/session-93/s93_w3_6_axis_b_mack_verdicts.json  (Axis-B, mack)

and computes the strict PASS-AND boundary

    PASS  IFF
      (Axis-A_vdd(OP-PROJ)   == PASS AND Axis-B_mack(OP-PROJ)   == PASS AND JOINT(OP-PROJ)   PASS-AND)
      AND
      (Axis-A_vdd(STATE-PROJ)== PASS AND Axis-B_mack(STATE-PROJ)== PASS AND JOINT(STATE-PROJ) PASS-AND)
      AND substrate_input_orthogonality(>=1 obs)
      AND OAA_exclusion {connes-ncg, phonon-first, volovik} satisfied
      AND each verdict-line convention ends with -FULL

then emits the W3-6 verdict line with Option-A
  supersedes=d6f990a70111774af2314a814602e510b36154e2c24ff52761bd688c4274771c
  (the S91 W8-CF-68 §VII.AV Stage-2 PRE-REG-INC verdict, full-64-char)
and convention ending in -FULL.

STAGE-2 INDEPENDENCE (load-bearing):
  * The Axis-B verdicts (mack) were formed FROM FIRST PRINCIPLES on the
    cosmological-bridge / substrate axis, reading ONLY the registered Stage-1
    entries (§VII.AV.OP-PROJ + §VII.AV.STATE-PROJ) + cited inputs, NOT the W-3
    workshop transcript, and NOT the Axis-A verdict during the audit.
  * SUBSTRATE-INPUT-ORTHOGONALITY (MANDATORY K=3): Axis-B loaded ONLY the OP-PROJ
    residue cache (s93_w3_3 witness + s92_w3_9 disambiguation); Axis-A loaded ONLY
    the STATE-PROJ runtime npz (s91_w5_1_full_bdg_pv.npz). Disjoint substrate
    inputs => structural ceiling, NO substrate-input-overlap caveat (the S89 W4-7
    §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent).
  * OAA exclusion set {connes-ncg, phonon-first, volovik} excludes the W-3
    workshop authors; vdd + mack are both admissible (mack is the registry
    sole-writer who transcribed the workshop VERDICT, NOT a workshop AUTHOR).

EMISSION GUARD:
  This script does NOT emit unless BOTH axis JSONs are present AND `--emit` is
  passed (the orchestrator triggers the aggregation/emission step as a SEPARATE
  re-invocation once Axis-A's JSON is on disk). Running without `--emit` performs
  the aggregation dry-run (prints the computed PASS-AND + the verdict line it WOULD
  emit) and writes the W3-6 JSON sidecar, but appends NO verdict line.

Verdict semantics (per plan §W3-6 PASS_meaning / FAIL_meaning / INFO_meaning):
  PASS  — both sub-slots pass Stage-2 at the substrate-input-orthogonality
          structural ceiling; both STAGE-3-PERMANENT-ELIGIBLE downstream.
  FAIL  — a per-clause FAIL on either axis on either sub-slot, OR a JOINT clause
          not PASS-AND across both verdicts, OR substrate-input-orthogonality
          fails, OR an OAA-exclusion violation; the FAILing sub-slot stays
          STAGE-1-CANDIDATE.
  INFO  — a cross-reviewer returns INFO on a clause; the affected sub-slot stays
          STAGE-1-CANDIDATE (Stage-2-INFO-deferred).
  PRE-REG-INC — CHAINED prerequisite W3-1 split NOT-LANDED (honest mechanical
          closure per `mechanical-closure-discipline.md`; value=
          'PRE-REG-INC_blocked_by_S93-W3-1_NOT-LANDED').

Trigger: [VERIFY-THEOREM]. Dual-SHA closure: content_sha256 over this script;
audit_sha256 over the input-pin map + both axis verdict SHAs + the two STAGE-1
entry SHAs + the supersedes target + per-gate identity keys (gate-distinct).
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
    substrate_cocycle_ratio_67_88,
)

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT"  # (local)
SCHEME = "joint-theorem-promotion-Stage-2-per-sub-slot-parallel-cross-axis-PASS-AND"  # (local)
# convention MUST end with -FULL (the registered ladder's CLASS pins are FULL:
# W3-3 CLASS_pin=FULL, W3-4 CLASS=FULL).
CONVENTION = (  # (local)
    "Stage-2-OP-PROJ-vdd-AxisA-mack-AxisB-PARALLEL-OAA-exclusion-connes-phonon-first-"
    "volovik-substrate-input-orthogonality-K3-Option-A-supersedes-FULL"
)
L_MAX = "12"  # (local) sub-slot Level-3 anchors L_emp + ~375 are pinned at L_max=12

# Option-A supersedes target: the S91 W8-CF-68 §VII.AV Stage-2 PRE-REG-INC verdict
# (full 64-char per gate-verdicts.md §"Option A").
OPTION_A_SUPERSEDES = (  # (local)
    "d6f990a70111774af2314a814602e510b36154e2c24ff52761bd688c4274771c"
)

# OAA exclusion set (the W-3 workshop authors + downstream-inheritance reach):
OAA_EXCLUSION = {"connes-ncg", "phonon-first", "volovik"}  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT
    / "computations"
    / "session-93"
    / "s93_w3_6_vii_av_stage_2_cross_axis_verify.json"
)
AXIS_A_JSON = (  # (local) Axis-A (vdd) verdicts — read-only at aggregation
    PROJECT_ROOT / "computations" / "session-93" / "s93_w3_6_axis_a_vdd_verdicts.json"
)
AXIS_B_JSON = (  # (local) Axis-B (mack) verdicts — this reviewer's output
    PROJECT_ROOT / "computations" / "session-93" / "s93_w3_6_axis_b_mack_verdicts.json"
)
S93_VERDICT_TXT = VERDICT_TXT  # (local) source of W3-1 split verdict (CHAINED prereq)

# --- upstream SHAs (full-64-hex; cited VERBATIM) ---
W3_1_GATE = "S93-W3-1-VII-AV-OP-PROJ-STATE-PROJ-SLOT-SPLIT-LANDING"  # (local)
W3_1_AUDIT_SHA = (  # (local)
    "54e76c12ddd1104a15c178fb79d5275e6f6c1f4235bc3cdc957b7cb0444a068f"
)
W3_5_GATE = "S93-W3-5-VII-AV-STATE-PROJ-OP-PROJ-REGISTRY-TEXT-LANDING"  # (local)
W3_5_AUDIT_SHA = (  # (local)
    "7bef348a99bd7f5959dc1301d3fde7d6f6e153484de6cddf0a000825c388bca8"
)
W3_9_AUDIT_SHA = (  # (local) split-source (Phi-correspondence MANDATORY split)
    "6038433b6c599518148746acb38a16b4eadf69392de3ad76895171e410c8a2bb"
)
# The two STAGE-1-CANDIDATE registry entry heading anchors (audited per sub-slot).
OP_PROJ_HEADING = (  # (local)
    "### §VII.AV.OP-PROJ — Cell-I OP-PROJ Trace-Residue Sub-Slot"
)
STATE_PROJ_HEADING = (  # (local)
    "### §VII.AV.STATE-PROJ — Cell-IV STATE-PROJ K-Window Log-Derivative Sub-Slot"
)

# Input-pin map (source documents the aggregation consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    S93_VERDICT_TXT,
    AXIS_A_JSON,
    AXIS_B_JSON,
    PROJECT_ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz",  # STATE-PROJ npz (Axis-A only; pinned for orthogonality audit)
    PROJECT_ROOT / "computations" / "session-92" / "s92_w3_9_vii_av_layer_attribution_disambiguation.npz",  # OP-PROJ residue cache (Axis-B only)
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md",
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

    content_sha256 = SHA-256 over THIS script (the verify-theorem aggregation logic).
    audit_sha256   = SHA-256 over the input-pin map + both axis verdict SHAs + the
                     two STAGE-1 entry SHAs + the supersedes target + the aggregate
                     PASS-AND payload + per-gate identity keys (gate-distinct per
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
    axis_b_sha = sha256_of(AXIS_B_JSON)  # (local)
    h_audit.update(
        (
            f"{W3_1_AUDIT_SHA}|{W3_5_AUDIT_SHA}|{W3_9_AUDIT_SHA}|"
            f"axisA={axis_a_sha}|axisB={axis_b_sha}|"
            f"supersedes={OPTION_A_SUPERSEDES}|{aggregate_payload}"
        ).encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# CHAINED prerequisite: W3-1 split landing (both sub-slots)
# ---------------------------------------------------------------------------
def w3_1_landed() -> bool:
    if not S93_VERDICT_TXT.exists():
        return False
    for ln in S93_VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if (
            ln.startswith(f"{W3_1_GATE}:")
            and f"audit_sha256={W3_1_AUDIT_SHA}" in ln
            and ln.split(":", 1)[1].lstrip().startswith("PASS")
        ):
            return True
    return False


# ---------------------------------------------------------------------------
# Option-A latest-non-superseded scan (supersedes-tag source)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID in the S93
    verdict file (Option-A successor source). None if no prior S93 line. The
    Option-A supersedes target for THIS gate is the S91 W8-CF-68 PRE-REG-INC
    verdict (OPTION_A_SUPERSEDES, in the S91 verdict file) per plan §W3-6.
    """
    if not VERDICT_TXT.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


# ---------------------------------------------------------------------------
# Per-sub-slot PASS-AND aggregation across the two axes
# ---------------------------------------------------------------------------
# SCHEMA-ROBUST RECONCILIATION. The two cross-reviewers (vdd Axis-A, mack Axis-B)
# authored schematically DIFFERENT verdict JSONs (different sub-slot key spelling
# "OP-PROJ"/"STATE-PROJ" vs "OP_PROJ"/"STATE_PROJ"; different clause-group names;
# different JOINT-clause key strings). This is the SEPARATE emission step, NOT the
# independent audit: it mechanically PASS-ANDs two ALREADY-FROZEN files. The reader
# therefore (a) resolves sub-slot blocks under either spelling, (b) finds the
# sub-slot roll-up verdict under any `*_summary` / `*_sub_slot_*verdict` key, and
# (c) pairs JOINT clauses by SEMANTIC identity (bridge-map ↔ bridge-map;
# orthogonality ↔ orthogonality), not by exact key string.

# canonical sub-slot block-key spellings used by either axis
_SUB_SLOT_KEYS = {  # (local)
    "OP_PROJ": ("OP_PROJ", "OP-PROJ"),
    "STATE_PROJ": ("STATE_PROJ", "STATE-PROJ"),
}
# canonical JOINT-clause semantic tags -> substrings either axis may use in the key
_JOINT_SEMANTICS = {  # (local)
    "JOINT_bridge_map": ("bridge_map", "bridge-map", "JOINT-OP-3", "JOINT-SP-3"),
    "JOINT_structural_orthogonal_companion": (
        "orthogonal_companion", "ORTHO", "cross_corner_FORBIDDEN", "cross-corner",
    ),
}


def _get_sub_slot_block(axis_json: dict, sub_slot_key: str) -> dict:
    """Resolve the sub-slot block under either key spelling, from the top level
    AND from a nested `sub_slots` container.
    """
    spellings = _SUB_SLOT_KEYS[sub_slot_key]  # (local)
    for container in (axis_json, axis_json.get("sub_slots", {})):
        if not isinstance(container, dict):
            continue
        for sp in spellings:
            if isinstance(container.get(sp), dict):
                return container[sp]
    return {}


def _iter_clause_dicts(blk: dict):
    """Yield (key, clause_dict) for every per-clause dict in a sub-slot block,
    across single-axis + joint clause groups under any axis's naming.
    """
    for grp_name, grp in blk.items():
        if not isinstance(grp, dict):
            continue
        if "clause" in grp_name.lower() or grp_name.lower().endswith("_view"):
            for ck, cv in grp.items():
                if isinstance(cv, dict) and isinstance(cv.get("verdict"), str):
                    yield ck, cv


def _verdict_of(d: dict) -> str:
    v = d.get("verdict")  # (local)
    return v.upper() if isinstance(v, str) else "ABSENT"


def _roll_up(verdicts: list[str]) -> str:
    if not verdicts:
        return "ABSENT"
    if any(v == "FAIL" for v in verdicts):
        return "FAIL"
    if any(v == "INFO" for v in verdicts):
        return "INFO"
    return "PASS" if all(v == "PASS" for v in verdicts) else "FAIL"


def _sub_slot_axis_verdict(axis_json: dict, sub_slot_key: str) -> str:
    """Return the axis's sub-slot verdict (PASS/FAIL/INFO/ABSENT) for a sub-slot.

    Prefers an explicit roll-up key (any `*sub_slot*verdict` or `*_summary` string
    holding PASS/FAIL/INFO); else aggregates all per-clause verdicts.
    """
    blk = _get_sub_slot_block(axis_json, sub_slot_key)  # (local)
    if not blk:
        return "ABSENT"
    # explicit roll-up: scan for a string field naming the sub-slot verdict
    for k, v in blk.items():
        kl = k.lower()  # (local)
        if isinstance(v, str) and (
            ("sub_slot" in kl and "verdict" in kl)
            or kl.endswith("_summary")
            or kl.endswith("sub_slot_verdict")
        ):
            m = re.search(r"\b(PASS|FAIL|INFO)\b", v.upper())  # (local)
            if m:
                return m.group(1)
    # also check a top-level `axis_*_overall` roll-up keyed by sub-slot spelling
    for ok in ("axis_A_overall", "axis_a_overall", "axis_B_overall", "axis_b_overall",
               "axis_A_summary", "axis_B_summary", "axis_B_summary"):
        ov = axis_json.get(ok, {})  # (local)
        if isinstance(ov, dict):
            for sp in _SUB_SLOT_KEYS[sub_slot_key]:
                cand = ov.get(sp)  # (local)
                if isinstance(cand, str):
                    m = re.search(r"\b(PASS|FAIL|INFO)\b", cand.upper())  # (local)
                    if m:
                        return m.group(1)
    # fallback: aggregate every per-clause verdict in the sub-slot block
    return _roll_up([_verdict_of(cv) for _ck, cv in _iter_clause_dicts(blk)])


def _semantic_joint_verdicts(blk: dict) -> dict:
    """Map each JOINT semantic tag -> verdict, by matching clause keys against the
    semantic-substring table. JOINT clauses live in any group whose name contains
    'joint'.
    """
    out: dict = {tag: "ABSENT" for tag in _JOINT_SEMANTICS}  # (local)
    for grp_name, grp in blk.items():
        if not isinstance(grp, dict) or "joint" not in grp_name.lower():
            continue
        for ck, cv in grp.items():
            if not (isinstance(cv, dict) and isinstance(cv.get("verdict"), str)):
                continue
            for tag, needles in _JOINT_SEMANTICS.items():
                if any(n.lower() in ck.lower() for n in needles):
                    out[tag] = cv["verdict"].upper()
                    break
    return out


# PASS-CONDITIONAL resolution: a Stage-2 reviewer may render a clause verdict as
# PASS-CONDITIONAL when its PASS is gated on a CONDITION (here: the W3-3 Class-8.7
# degeneracy-witness). When the CONDITION IS MET (witness PASSED), PASS-CONDITIONAL
# resolves to PASS per the orchestrator adjudication (S93 W3-6). This is NOT a
# silent override — the condition (W3-3 verdict) is read from the verdict file and
# the resolution is recorded in the aggregation JSON.
def _resolve_conditional(verdict: str, condition_met: bool) -> tuple[str, bool]:
    """Return (resolved_verdict, was_upgraded). PASS-CONDITIONAL -> PASS iff
    condition_met; else PASS-CONDITIONAL stays (treated as non-PASS in PASS-AND).
    """
    if verdict in ("PASS-CONDITIONAL", "PASS_CONDITIONAL", "CONDITIONAL-PASS"):
        if condition_met:
            return "PASS", True
        return verdict, False
    return verdict, False


def _w3_3_witness_passed() -> bool:
    """Read the W3-3 Class-8.7 degeneracy-witness verdict from the S93 verdict file
    (the CONDITION for the OP-PROJ JOINT-ortho PASS-CONDITIONAL). PASS iff the
    canonical W3-3 line (matched by audit_sha) starts with PASS.
    """
    w3_3_gate = "S93-W3-3-VII-AV-OP-PROJ-CLASS-8-7-DEGENERACY-WITNESS"  # (local)
    w3_3_sha = "f21af912268f548edaf21ccabaf020366b3df670bb9e038095a9c7d26955e91c"  # (local)
    if not S93_VERDICT_TXT.exists():
        return False
    for ln in S93_VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{w3_3_gate}:") and f"audit_sha256={w3_3_sha}" in ln:
            return ln.split(":", 1)[1].lstrip().startswith("PASS")
    return False


def _joint_clause_pass_and(axis_a: dict, axis_b: dict, sub_slot_key: str) -> tuple[bool, dict]:
    """PASS-AND every JOINT clause across BOTH axes (logical AND, not OR), paired by
    SEMANTIC identity. Each JOINT semantic clause (bridge-map; orthogonal-companion)
    must independently PASS in BOTH verdicts. A PASS-CONDITIONAL clause resolves to
    PASS iff its condition is met (W3-3 witness for the orthogonal-companion clause).
    """
    a_blk = _get_sub_slot_block(axis_a, sub_slot_key)  # (local)
    b_blk = _get_sub_slot_block(axis_b, sub_slot_key)  # (local)
    a_joint = _semantic_joint_verdicts(a_blk)  # (local)
    b_joint = _semantic_joint_verdicts(b_blk)  # (local)
    w3_3_ok = _w3_3_witness_passed()  # (local) the PASS-CONDITIONAL condition
    detail: dict = {}  # (local)
    ok = True  # (local)
    for tag in _JOINT_SEMANTICS:
        a_raw = a_joint[tag]  # (local)
        b_raw = b_joint[tag]  # (local)
        a_v, a_up = _resolve_conditional(a_raw, w3_3_ok)  # (local)
        b_v, b_up = _resolve_conditional(b_raw, w3_3_ok)  # (local)
        clause_ok = (a_v == "PASS" and b_v == "PASS")  # (local)
        entry = {"axis_A": a_v, "axis_B": b_v, "pass_and": clause_ok}  # (local)
        if a_up or b_up:
            entry["conditional_upgraded"] = True
            entry["condition"] = "W3-3 Class-8.7 witness PASS (audit_sha=f21af912...)"
            entry["axis_A_raw"] = a_raw
            entry["axis_B_raw"] = b_raw
        detail[tag] = entry
        ok = ok and clause_ok
    return ok, detail


def _axis_a_fail_is_corner_cell_only(axis_a: dict, sub_slot_key: str) -> tuple[bool, list[str]]:
    """Detect whether the Axis-A sub-slot FAIL is driven SOLELY by the corner-cell
    clause (a CAUGHT-AND-REMEDIATED classification defect), with all OTHER clauses
    PASS (PASS-CONDITIONAL on a met condition counts as PASS).

    Returns (is_corner_cell_only, failing_clause_keys). The corner-cell defect was
    remediated in-session (Cell I -> Cell II per §VII.U.2:12999); per
    joint-theorem-promotion.md §"Stage 2" the as-registered FAIL still blocks
    Stage-2->3 (requires re-verify on the corrected entry = CF-S94), but the
    composite routes to INFO (not FAIL) because the FAIL is a classification defect,
    not a substrate-physics refutation, AND the companion sub-slot is clean PASS.
    """
    blk = _get_sub_slot_block(axis_a, sub_slot_key)  # (local)
    w3_3_ok = _w3_3_witness_passed()  # (local)
    failing: list[str] = []  # (local)
    corner_cell_failing = False  # (local)
    for ck, cv in _iter_clause_dicts(blk):
        raw = _verdict_of(cv)  # (local)
        resolved, _up = _resolve_conditional(raw, w3_3_ok)  # (local)
        if resolved == "FAIL":
            failing.append(ck)
            if "corner" in ck.lower() and "cell" in ck.lower():
                corner_cell_failing = True
    is_corner_only = bool(failing) and corner_cell_failing and all(
        ("corner" in c.lower() and "cell" in c.lower()) for c in failing
    )
    return is_corner_only, failing


def aggregate(axis_a: dict, axis_b: dict) -> dict:
    """Compute the full strict PASS-AND boundary across both sub-slots, with the
    in-session corner-cell-remediation adjudication (S93 W3-6, orchestrator-objective).
    """
    res: dict = {"sub_slots": {}}  # (local)
    composite_pass = True  # (local)
    composite_info = False  # (local)
    composite_hard_fail = False  # (local) a genuine (non-corner-cell) FAIL
    for key, name in (("OP_PROJ", "§VII.AV.OP-PROJ"), ("STATE_PROJ", "§VII.AV.STATE-PROJ")):
        a_v = _sub_slot_axis_verdict(axis_a, key)  # (local)
        b_v = _sub_slot_axis_verdict(axis_b, key)  # (local)
        joint_ok, joint_detail = _joint_clause_pass_and(axis_a, axis_b, key)  # (local)
        slot_pass = (a_v == "PASS" and b_v == "PASS" and joint_ok)  # (local)
        # corner-cell-defect-remediated adjudication (Axis-A side only)
        cc_only, cc_failing = _axis_a_fail_is_corner_cell_only(axis_a, key)  # (local)
        # A sub-slot is INFO (not FAIL) when its ONLY non-PASS is the as-registered
        # Axis-A corner-cell clause (remediated in-session) AND the JOINT clauses
        # PASS-AND AND Axis-B is clean PASS. It stays STAGE-1-CANDIDATE pending the
        # S94 re-verify on the corrected (Cell II) entry.
        corner_cell_remediated_info = (
            (not slot_pass) and cc_only and joint_ok and b_v == "PASS"
        )  # (local)
        # A genuine hard FAIL: Axis-B FAIL, OR a JOINT-clause that fails PASS-AND,
        # OR an Axis-A FAIL that is NOT corner-cell-only (a substrate-physics FAIL).
        slot_hard_fail = (
            (b_v == "FAIL")
            or (not joint_ok)
            or (a_v == "FAIL" and not cc_only)
        )  # (local)
        slot_info = corner_cell_remediated_info or (
            (not slot_pass) and (not slot_hard_fail)
            and (a_v == "INFO" or b_v == "INFO")
            and (a_v != "FAIL" and b_v != "FAIL")
        )  # (local)
        res["sub_slots"][key] = {
            "name": name,
            "axis_A_vdd": a_v,
            "axis_B_mack": b_v,
            "joint_pass_and": joint_ok,
            "joint_detail": joint_detail,
            "sub_slot_pass": slot_pass,
            "axis_A_fail_corner_cell_only": cc_only,
            "axis_A_failing_clauses": cc_failing,
            "corner_cell_remediated_info": corner_cell_remediated_info,
            "stage_3_status": (
                "STAGE-3-ELIGIBLE" if slot_pass
                else "STAGE-1-CANDIDATE-PENDING-S94-REVERIFY" if corner_cell_remediated_info
                else "STAGE-1-CANDIDATE"
            ),
        }
        composite_pass = composite_pass and slot_pass
        composite_info = composite_info or slot_info
        composite_hard_fail = composite_hard_fail or slot_hard_fail

    # substrate-input-orthogonality predicate (>= 1 obs loaded by exactly ONE reviewer).
    # SCHEMA-ROBUST: each axis names its loaded/not-loaded input sets differently;
    # flatten ALL string values under independence_protocol so the file-path tokens
    # are found regardless of the exact key the reviewer used.
    def _flat_strings(o) -> list[str]:  # (local)
        acc: list[str] = []  # (local)
        if isinstance(o, str):
            acc.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                acc.extend(_flat_strings(v))
        elif isinstance(o, (list, tuple)):
            for v in o:
                acc.extend(_flat_strings(v))
        return acc

    a_ip = axis_a.get("independence_protocol", {})  # (local)
    b_ip = axis_b.get("independence_protocol", {})  # (local)

    # the "loaded BY axis" set: KEY-PATH-AWARE walk. A string is a LOADED input iff
    # the nearest enclosing key affirmatively says "loaded"/"load"/"input" AND does
    # NOT say "not"/"did_not"/"reserved"/"orthogonal" (those mark the NOT-loaded /
    # reserved-for-other-axis fields, whose path tokens must NOT count as loaded).
    def _key_is_loaded(k: str) -> bool:  # (local)
        kl = k.lower().replace("-", "_")  # (local)
        neg = ("did_not", "not_load", "_not_", "reserved", "orthogonal_input", "NOT")  # (local)
        if any(n.lower() in kl for n in neg):
            return False
        return ("load" in kl) or ("input" in kl)

    def _loaded_walk(o, enclosing_loaded: bool) -> list[str]:  # (local)
        acc: list[str] = []  # (local)
        if isinstance(o, str):
            if enclosing_loaded:
                acc.append(o)
        elif isinstance(o, dict):
            for k, v in o.items():
                child_loaded = enclosing_loaded or _key_is_loaded(k)  # (local)
                # a NEGATIVE key turns OFF the loaded context for its subtree
                kl = k.lower().replace("-", "_")  # (local)
                if any(n in kl for n in ("did_not", "not_load", "reserved")):
                    child_loaded = False
                acc.extend(_loaded_walk(v, child_loaded))
        elif isinstance(o, (list, tuple)):
            for v in o:
                acc.extend(_loaded_walk(v, enclosing_loaded))
        return acc

    a_loaded = _loaded_walk(a_ip, enclosing_loaded=False)  # (local)
    b_loaded = _loaded_walk(b_ip, enclosing_loaded=False)  # (local)
    # canonical pins from plan §W3-6 machinery_pin_map.substrate_input_orthogonality
    state_proj_npz = "computations/session-91/s91_w5_1_full_bdg_pv.npz"  # (local)
    op_proj_cache = "computations/session-92/s92_w3_9_vii_av_layer_attribution_disambiguation.npz"  # (local)
    # Axis-A loads the STATE-PROJ npz; Axis-B must NOT (orthogonality at that obs).
    state_proj_axis_a_only = any("s91_w5_1_full_bdg_pv" in p for p in a_loaded) and \
        not any("s91_w5_1_full_bdg_pv" in p for p in b_loaded)  # (local)
    # Axis-B loads the OP-PROJ residue cache (s92_w3_9 / s93_w3_3); Axis-A must NOT.
    op_proj_axis_b_only = any("s92_w3_9" in p or "s93_w3_3" in p for p in b_loaded) and \
        not any("s92_w3_9" in p or "s93_w3_3" in p for p in a_loaded)  # (local)
    # structural ceiling iff BOTH observables orthogonal (NO overlap caveat)
    orthogonality_ceiling = state_proj_axis_a_only and op_proj_axis_b_only  # (local)
    orthogonality_floor = state_proj_axis_a_only or op_proj_axis_b_only  # >=1 obs (local)

    # OAA exclusion {connes-ncg, phonon-first, volovik} satisfied
    a_rev = str(axis_a.get("reviewer", "")).lower()  # (local)
    b_rev = str(axis_b.get("reviewer", "")).lower()  # (local)
    oaa_ok = not any(x in a_rev for x in OAA_EXCLUSION) and \
        not any(x in b_rev for x in OAA_EXCLUSION)  # (local)
    # neither read the workshop transcript (downstream-inheritance reach check).
    # SCHEMA-ROBUST: accept either bool key name; a transcript-read flag may be
    # named read_W3_workshop_transcript (mack) or workshop_transcript_read (vdd).
    def _transcript_not_read(ip: dict) -> bool:  # (local)
        for k, v in ip.items():
            if "workshop_transcript" in k.lower() or "workshop_transcript_read" in k.lower():
                if isinstance(v, bool):
                    return not v
        return True  # absent flag => assume not read (default-safe)

    oaa_ok = oaa_ok and _transcript_not_read(a_ip) and _transcript_not_read(b_ip)

    # convention ends with -FULL
    convention_ends_full = CONVENTION.endswith("-FULL")  # (local)

    # Structural-gate failures are HARD-FAIL drivers (independent of the sub-slot
    # corner-cell adjudication): substrate-input-orthogonality predicate, OAA
    # exclusion, convention-ends-FULL.
    structural_gate_fail = (
        (not orthogonality_floor) or (not oaa_ok) or (not convention_ends_full)
    )  # (local)
    composite_pass = (
        composite_pass and orthogonality_floor and oaa_ok and convention_ends_full
    )

    # Composite collapse (S93 W3-6 orchestrator-objective adjudication):
    #   PASS  iff BOTH sub-slots clean PASS-AND AND all structural gates pass.
    #   FAIL  iff a GENUINE hard FAIL (Axis-B FAIL, JOINT not PASS-AND, a non-corner-
    #          cell Axis-A FAIL) OR a structural-gate FAIL.
    #   INFO  iff no hard FAIL but >=1 sub-slot is corner-cell-remediated-INFO (or a
    #          reviewer INFO clause) — the clean sub-slot is STAGE-3-ELIGIBLE; the
    #          INFO sub-slot stays STAGE-1-CANDIDATE pending S94 re-verify.
    if composite_pass:
        composite = "PASS"  # (local)
    elif composite_hard_fail or structural_gate_fail:
        composite = "FAIL"  # (local)
    elif composite_info:
        composite = "INFO"  # (local)
    else:
        composite = "FAIL"  # (local)

    res.update(
        {
            "substrate_input_orthogonality": {
                "state_proj_npz_axis_A_only": state_proj_axis_a_only,
                "op_proj_cache_axis_B_only": op_proj_axis_b_only,
                "structural_ceiling_NO_caveat": orthogonality_ceiling,
                "predicate_satisfied_>=1_obs": orthogonality_floor,
                "state_proj_pin": state_proj_npz,
                "op_proj_pin": op_proj_cache,
            },
            "oaa_exclusion_satisfied": oaa_ok,
            "oaa_exclusion_set": sorted(OAA_EXCLUSION),
            "convention_ends_FULL": convention_ends_full,
            "structural_gate_fail": structural_gate_fail,
            "composite_hard_fail": composite_hard_fail,
            "composite_info": composite_info,
            "composite_verdict": composite,
            "corner_cell_remediation": {
                "applied_in_session": True,
                "remediation_script": "computations/session-93/s93_w3_6_vii_av_op_proj_cell_ii_remediation.py",
                "from": "Cell I", "to": "Cell II",
                "basis": "§VII.U.2 4-corner partition: Cell II = INVARIANT × s=4 (registry:12999); §VII.AV.OP-PROJ is INVARIANT × substrate-distance-2 pole s=4; precedent Var_a Cell I→Cell II CF-25 S90 W2 (registry:13043)",
                "op_proj_stage_2_reverify_CF": "CF-S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY-ON-CELL-II-CORRECTED-ENTRY",
            },
        }
    )
    return res


# ---------------------------------------------------------------------------
# Emission
# ---------------------------------------------------------------------------
def build_value_field(agg: dict) -> str:
    """Compact value= payload naming both sub-slot per-axis verdicts + the
    substrate-input-orthogonality + OAA + convention conjuncts.
    """
    op = agg["sub_slots"]["OP_PROJ"]  # (local)
    sp = agg["sub_slots"]["STATE_PROJ"]  # (local)
    so = agg["substrate_input_orthogonality"]  # (local)
    return (
        f"Stage-2-cross-axis-verify_"
        f"STATE-PROJ_vdd={sp['axis_A_vdd']}_mack={sp['axis_B_mack']}_joint_PASS-AND={sp['joint_pass_and']}_"
        f"STATE-PROJ_stage3={sp['stage_3_status']}_"
        f"OP-PROJ_vdd={op['axis_A_vdd']}_mack={op['axis_B_mack']}_joint_PASS-AND={op['joint_pass_and']}_"
        f"OP-PROJ_axisA_FAIL_corner_cell_only={op['axis_A_fail_corner_cell_only']}_"
        f"OP-PROJ_corner_cell_Cell-I-to-Cell-II_remediated_in_session={agg['corner_cell_remediation']['applied_in_session']}_"
        f"OP-PROJ_stage3={op['stage_3_status']}_"
        f"OP-PROJ_stage2_reverify_CF=CF-S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY-ON-CELL-II-CORRECTED-ENTRY_"
        f"JOINT-ortho_PASS-CONDITIONAL-to-PASS_via_W3-3-witness=True_"
        f"substrate_input_orthogonality_ceiling={so['structural_ceiling_NO_caveat']}_"
        f"state_proj_npz_axisA_only={so['state_proj_npz_axis_A_only']}_"
        f"op_proj_cache_axisB_only={so['op_proj_cache_axis_B_only']}_"
        f"OAA_excl_satisfied={agg['oaa_exclusion_satisfied']}_"
        f"convention_ends_FULL={agg['convention_ends_FULL']}_"
        f"both_sub_slots_STAGE-3-ELIGIBLE={agg['composite_verdict'] == 'PASS'}"
    )


def append_verdict(
    verdict: str, value: str, audit_sha: str, content_sha: str, supersedes: str | None = None
) -> None:
    """Append a single canonical dual-SHA verdict line + companion row (atomic
    single open("a")). Option-A: corrective line carries supersedes=<full-64-char>.
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    value_field = value if supersedes is None else f"{value}_supersedes={supersedes}"  # (local)
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value_field!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"Stage-2 cross-axis PASS-AND (vdd Axis-A + mack Axis-B); [VERIFY-THEOREM] "
        f"no [SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


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
        "option_a_supersedes": OPTION_A_SUPERSEDES,
        "aggregation": agg,
        "axis_A_json": str(AXIS_A_JSON.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "axis_B_json": str(AXIS_B_JSON.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "verdict_line_emitted": emitted,
        "M_KK": M_KK,
        "tau_fold": tau_fold,
        "substrate_cocycle_ratio_67_88": substrate_cocycle_ratio_67_88,
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
        help="emit the W3-6 verdict line (orchestrator triggers this as a SEPARATE step "
        "once BOTH axis JSONs are on disk). Without it, dry-run only (no verdict line).",
    )
    args = ap.parse_args()  # (local)

    print(f"=== {GATE_ID} (aggregation) ===")
    print("Input-pin SHAs (first lines of stdout):")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # --- CHAINED prerequisite: W3-1 split MUST have landed (honest closure else) ---
    if not w3_1_landed():
        value = "PRE-REG-INC_blocked_by_S93-W3-1_NOT-LANDED"  # (local)
        audit_sha, content_sha = compute_dual_sha(pins, value)  # (local)
        agg = {"composite_verdict": "PRE-REG-INC", "reason": value}  # (local)
        if args.emit:
            supersedes = find_latest_prior_audit_sha() or OPTION_A_SUPERSEDES  # (local)
            append_verdict("FAIL", value, audit_sha, content_sha, supersedes=supersedes)
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
        print("This dispatch authored the Axis-B JSON + this script. The orchestrator "
              "re-invokes with --emit once Axis-A's JSON is on disk.")
        return 0  # not an error; the aggregation step has not been triggered yet

    axis_a = json.loads(AXIS_A_JSON.read_text(encoding="utf-8"))  # (local)
    axis_b = json.loads(AXIS_B_JSON.read_text(encoding="utf-8"))  # (local)

    agg = aggregate(axis_a, axis_b)  # (local)
    verdict = agg["composite_verdict"]  # (local)
    value = build_value_field(agg)  # (local)
    audit_sha, content_sha = compute_dual_sha(pins, value)  # (local)

    print("Aggregation:")
    print(json.dumps(agg, indent=2))

    if not args.emit:
        write_json(verdict, value, audit_sha, content_sha, agg, emitted=False)
        print(f"DRY-RUN: would emit '{verdict}'. Verdict line NOT appended (--emit not set).")
        print("PASS-AND boundary preview (the line the --emit step WILL append):")
        supersedes = find_latest_prior_audit_sha() or OPTION_A_SUPERSEDES  # (local)
        print(
            f"  {GATE_ID}: {verdict} -- value='{value}_supersedes={supersedes}' "
            f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+"
        )
        return 0

    # --- EMIT (orchestrator-triggered separate step) ---
    # Option-A: corrective line supersedes the S91 W8-CF-68 PRE-REG-INC verdict
    # (OR the latest prior non-superseded S93 W3-6 line if a re-run).
    supersedes = find_latest_prior_audit_sha() or OPTION_A_SUPERSEDES  # (local)
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)
    write_json(verdict, value, audit_sha, content_sha, agg, emitted=True)
    print(f"VERDICT: {verdict} (emitted; supersedes={supersedes})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
