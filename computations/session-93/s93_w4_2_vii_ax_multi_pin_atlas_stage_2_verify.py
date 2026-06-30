#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY
=========================================================

Two-agent parallel Stage-2 cross-axis independent-verify (per
`.claude/rules/joint-theorem-promotion.md §"Stage 2"`) for the
§VII.AX.MULTI-PIN-ATLAS STAGE-1-CANDIDATE (regulator-class-pluralism multi-pin
atlas at substrate-distance-2 pole s=4 χ' restriction).

This is the AGGREGATION / EMISSION script. It READS both axes' verdict JSONs

    computations/session-93/s93_w4_2_axis_a_connes_multi_pin_atlas_verify.json   (Axis-A, connes)
    computations/session-93/s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json  (Axis-B, volovik)

and computes the strict Stage-2 PASS-AND boundary

    PASS  IFF
      (axis_a_composite == PASS) AND (axis_b_composite == PASS)
      AND (for each JOINT clause c in {Element-1, JOINT-Element-3, JOINT-Element-5}:
              axis_a[c] == PASS AND axis_b[c] == PASS)            # logical AND, not OR
      AND substrate_input_orthogonality(obs_2) == PASS           # >=1 obs by exactly ONE reviewer (Axis-B)
      AND OAA_exclusion {mack-cosmic-bridge} satisfied           # Stage-1 sole-writer excluded
      AND machinery_not_self_authored == PASS (both axes)        # joint-theorem-promotion §Audit item 6
      AND each axis convention ends with -FULL                   # FULL CM-1995 §III.4 evaluation class pin

then emits the W4-2 verdict line + dual-SHA companion. The verdict collapses to
FAIL on any per-clause FAIL on either axis, any JOINT clause not PASS-AND across
both verdicts, a substrate-input-orthogonality failure, an OAA-exclusion
violation, a self-authored-machinery violation, or a convention-not-FULL; INFO
when a reviewer returns INFO on a clause (Stage-2-INFO-deferred).

STAGE-2 INDEPENDENCE (load-bearing):
  * The Axis-B verdicts (volovik) were formed FROM FIRST PRINCIPLES on the
    substrate / superfluid-universe axis, reading ONLY the registered Stage-1
    entry §VII.AX.MULTI-PIN-ATLAS + cited pins (S91 §W2-1 PASS-V) + obs_2, NOT
    the S92 W6-1/W6-2 workshop transcript, and NOT the Axis-A verdict during the
    audit.
  * SUBSTRATE-INPUT-ORTHOGONALITY (MANDATORY K=3 since S90 W2 CF-20): Axis-B
    loaded obs_2 (the n_PBH cardinality grid s91_w5_3_cf41_upper_22_6.npz);
    Axis-A connes does NOT (per plan dispatch axis_a.loads_obs_2=false). The
    MULTI-PIN-ATLAS observable is the s=4 Mellin residue Res_s=4[Tr(D_K^-2s)];
    obs_2 (n_PBH) is the substrate-distance-3 pole s=5 cardinality cascade — a
    structurally DISTINCT observable. Disjoint relevant substrate inputs =>
    structural ceiling, NO substrate-input-overlap caveat (S89 W4-7 §VII.AH
    FIRST-INSTANCE-WITHOUT-caveat precedent).
  * OAA exclusion set {mack-cosmic-bridge} excludes the Stage-1 sole-writer;
    connes (Axis-A) + volovik (Axis-B) are both admissible per the registered
    §VII.AX.MULTI-PIN-ATLAS Stage-2 verify queue admissible-axes block.

EMISSION GUARD:
  This script does NOT emit unless BOTH axis JSONs are present AND `--emit` is
  passed (the orchestrator triggers the aggregation/emission step as a SEPARATE
  re-invocation once Axis-A's JSON is on disk). Running without `--emit` performs
  the aggregation dry-run (prints the computed PASS-AND + the verdict line it
  WOULD emit) and writes the W4-2 JSON sidecar + NPZ, but appends NO verdict
  line.

OPTION-A SUPERSEDES:
  No prior canonical verdict line exists for this gate-ID (the Stage-2 verify was
  only QUEUED at the §VII.AX.MULTI-PIN-ATLAS landing, never previously emitted a
  PRE-REG-INC). On a clean first emission the corrective line carries NO
  supersedes tag. If a prior NON-superseded S93 W4-2 line is found at emit-time
  (a re-run), the corrective line supersedes it per `gate-verdicts.md §"Option A"`.

Trigger: [VERIFY-THEOREM]. Dual-SHA closure: content_sha256 over this script;
audit_sha256 over the input-pin map + both axis verdict SHAs + the registered
Stage-1 entry block SHA + the S91 §W2-1 PASS-V source-verdict SHA + the aggregate
PASS-AND payload + per-gate identity keys (gate-distinct).

Structural template: this script mirrors the proven S93 W3-6 aggregation pattern
at `computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.py`
(lines 69-820): same dual-SHA helpers, same Option-A latest-non-superseded scan,
same `--emit` guard + both-JSON presence gate, same schema-robust JSON reading.
Adapted to the SINGLE-SLOT MULTI-PIN-ATLAS case (no OP-PROJ/STATE-PROJ sub-slot
split) with the Axis-A/Axis-B JSON clause naming used here.
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
)

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY"  # (local)
SCHEME = (  # (local)
    "stage-2-cross-axis-verify-MULTI-PIN-ATLAS-substrate-distance-2-pole-s4-chi-prime-restriction"
)
# convention MUST end with -FULL (the registered atlas is FULL CM-1995 §III.4
# evaluation; each fiducial sub-row is a FULL physical regularization).
CONVENTION = (  # (local)
    "stage-2-cross-reviewer-protocol-without-prior-workshop-context-PARALLEL-PASS-AND-"
    "substrate-input-orthogonality-K3-connes-AxisA-volovik-AxisB-OAA-exclusion-mack-FULL"
)
L_MAX = "12"  # (local) the MULTI-PIN-ATLAS observable Res_s=4[Tr(D_K^-2s)] is at L_max=12 master cache

# OAA exclusion set for the §VII.AX cluster: the Stage-1 sole-writer.
OAA_EXCLUSION = {"mack-cosmic-bridge", "mack"}  # (local)

# The three JOINT clauses (PASS-AND'd across both axes) per plan §W4-2 dispatch.
JOINT_CLAUSE_TAGS = ("Element_1", "JOINT_Element_3", "JOINT_Element_5")  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = (  # (local) canonical per gate-verdicts.md §"Canonical Verdict-File Path"
    PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"
)
JSON_PATH = (  # (local)
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.json"
)
NPZ_PATH = (  # (local)
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.npz"
)
AXIS_A_JSON = (  # (local) Axis-A (connes) verdicts — read-only at aggregation
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_2_axis_a_connes_multi_pin_atlas_verify.json"
)
AXIS_B_JSON = (  # (local) Axis-B (volovik) verdicts — this reviewer's output
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json"
)

# --- upstream SHAs (full-64-hex; cited VERBATIM) ---
# S91 §W2-1 PASS-V source verdict (the registered Stage-1 empirical anchor).
W2_1_SOURCE_AUDIT_SHA = (  # (local)
    "58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14"
)
# The registered Stage-1 entry heading anchor (audited).
MULTI_PIN_ATLAS_HEADING = (  # (local)
    "### §VII.AX.MULTI-PIN-ATLAS"
)
# obs_2 grid (Axis-B-only load; pinned for the substrate-input-orthogonality audit).
OBS_2_NPZ = (  # (local)
    PROJECT_ROOT / "computations" / "session-91" / "s91_w5_3_cf41_upper_22_6.npz"
)

# Input-pin map (source documents the aggregation consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    REGISTRY_PATH,
    AXIS_A_JSON,
    AXIS_B_JSON,
    OBS_2_NPZ,
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md",
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md",
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
                     registered Stage-1 entry block SHA + the S91 §W2-1 PASS-V
                     source-verdict SHA + the aggregate PASS-AND payload + per-gate
                     identity keys (gate-distinct).
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
    stage_1_block_sha = registry_stage_1_block_sha()  # (local)
    h_audit.update(
        (
            f"{W2_1_SOURCE_AUDIT_SHA}|stage1_block={stage_1_block_sha}|"
            f"axisA={axis_a_sha}|axisB={axis_b_sha}|{aggregate_payload}"
        ).encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


def registry_stage_1_block_sha() -> str:
    """SHA-256 over the registered §VII.AX.MULTI-PIN-ATLAS Stage-1 entry block
    (from its heading anchor to the next `### §VII.` heading). Pins the audited
    Stage-1 entry into the audit_sha256 so the verdict is bound to the exact
    registry text the cross-reviewers audited.
    """
    if not REGISTRY_PATH.exists():
        return "0" * 64
    lines = REGISTRY_PATH.read_text(encoding="utf-8").splitlines()  # (local)
    block: list[str] = []  # (local)
    capturing = False  # (local)
    for ln in lines:
        if ln.startswith(MULTI_PIN_ATLAS_HEADING):
            capturing = True
            block.append(ln)
            continue
        if capturing:
            if ln.startswith("### §VII.") and not ln.startswith(MULTI_PIN_ATLAS_HEADING):
                break
            block.append(ln)
    return hashlib.sha256("\n".join(block).encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Option-A latest-non-superseded scan (supersedes-tag source)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID in the S93
    verdict file (Option-A successor source). None if no prior S93 line — this is
    a clean first emission for the W4-2 gate-ID (the Stage-2 verify was only
    QUEUED at the §VII.AX.MULTI-PIN-ATLAS landing, never previously emitted).
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
# Schema-robust JSON readers (the two axes authored schematically different JSONs)
# ---------------------------------------------------------------------------
def _flatten_clause_dicts(axis_json: dict):
    """Yield (key, clause_dict) for every per-clause dict in an axis JSON, across
    single-axis + joint clause groups under any axis's naming. A clause dict is
    any dict carrying a string `verdict` field.
    """
    for grp_name, grp in axis_json.items():
        if not isinstance(grp, dict):
            continue
        gl = grp_name.lower()  # (local)
        if "clause" in gl or gl.endswith("_view") or "joint" in gl or "single_axis" in gl:
            for ck, cv in grp.items():
                if isinstance(cv, dict) and isinstance(cv.get("verdict"), str):
                    yield ck, cv


def _verdict_of(d: dict) -> str:
    v = d.get("verdict")  # (local)
    return v.upper() if isinstance(v, str) else "ABSENT"


def _axis_composite(axis_json: dict) -> str:
    """The axis's declared composite verdict, under either key spelling
    (axis_A_composite / axis_a_composite / axis_B_composite / composite)."""
    for k in (
        "axis_A_composite", "axis_a_composite",
        "axis_B_composite", "axis_b_composite",
        "composite", "composite_verdict",
    ):
        v = axis_json.get(k)  # (local)
        if isinstance(v, str):
            m = re.search(r"\b(PASS|FAIL|INFO)\b", v.upper())  # (local)
            if m:
                return m.group(1)
    # fallback: roll up all per-clause verdicts
    verdicts = [_verdict_of(cv) for _ck, cv in _flatten_clause_dicts(axis_json)]  # (local)
    if not verdicts:
        return "ABSENT"
    if any(v == "FAIL" for v in verdicts):
        return "FAIL"
    if any(v == "INFO" for v in verdicts):
        return "INFO"
    return "PASS" if all(v == "PASS" for v in verdicts) else "FAIL"


# Semantic substrings for each JOINT clause tag (axes may key them differently).
_JOINT_SEMANTICS = {  # (local)
    "Element_1": (
        "element_1", "element1", "substrate_is_observable", "substrate-is",
    ),
    "JOINT_Element_3": (
        "element_3", "element3", "bridge_map", "bridge-map",
    ),
    "JOINT_Element_5": (
        "element_5", "element5", "empirical_anchor", "empirical-anchor",
    ),
}


def _joint_verdict_for_axis(axis_json: dict, tag: str) -> str:
    """Find the verdict for JOINT clause `tag` in an axis JSON, matching clause
    keys against the semantic-substring table. JOINT clauses live in any group
    whose name contains 'joint'."""
    needles = _JOINT_SEMANTICS[tag]  # (local)
    # prefer joint groups
    for grp_name, grp in axis_json.items():
        if not isinstance(grp, dict) or "joint" not in grp_name.lower():
            continue
        for ck, cv in grp.items():
            if isinstance(cv, dict) and isinstance(cv.get("verdict"), str):
                if any(n in ck.lower() for n in needles):
                    return cv["verdict"].upper()
    # else any clause group
    for ck, cv in _flatten_clause_dicts(axis_json):
        if any(n in ck.lower() for n in needles):
            return cv["verdict"].upper()
    return "ABSENT"


def _joint_pass_and(axis_a: dict, axis_b: dict) -> tuple[bool, bool, dict]:
    """PASS-AND every JOINT clause across BOTH axes (logical AND, not OR), paired
    by SEMANTIC identity. Returns (all_pass_and, any_info, detail).
    Each JOINT clause must independently PASS in BOTH verdicts.
    """
    detail: dict = {}  # (local)
    all_ok = True  # (local)
    any_info = False  # (local)
    for tag in JOINT_CLAUSE_TAGS:
        a_v = _joint_verdict_for_axis(axis_a, tag)  # (local)
        b_v = _joint_verdict_for_axis(axis_b, tag)  # (local)
        clause_ok = (a_v == "PASS" and b_v == "PASS")  # (local)
        if a_v == "INFO" or b_v == "INFO":
            any_info = True
        detail[tag] = {"axis_A": a_v, "axis_B": b_v, "pass_and": clause_ok}
        all_ok = all_ok and clause_ok
    return all_ok, any_info, detail


def _orthogonality_obs_2(axis_a: dict, axis_b: dict) -> tuple[bool, bool, dict]:
    """substrate-input-orthogonality at obs_2 (>=1 obs loaded by exactly ONE
    reviewer). Returns (floor_ok, ceiling_no_caveat, detail). Axis-B loads obs_2;
    Axis-A must NOT (per plan dispatch axis_a.loads_obs_2=false).
    """
    def _flat(o) -> list[str]:  # (local)
        acc: list[str] = []  # (local)
        if isinstance(o, str):
            acc.append(o)
        elif isinstance(o, dict):
            for v in o.values():
                acc.extend(_flat(v))
        elif isinstance(o, (list, tuple)):
            for v in o:
                acc.extend(_flat(v))
        return acc

    a_ip = axis_a.get("independence_protocol", {})  # (local)
    b_ip = axis_b.get("independence_protocol", {})  # (local)
    obs2_token = "s91_w5_3_cf41_upper_22_6"  # (local) canonical obs_2 path token

    # Axis-B loaded set: prefer the affirmative `loaded_input_obs_2` field;
    # fall back to scanning loaded-keyed values.
    def _loaded_obs2(ip: dict) -> bool:  # (local)
        for k, v in ip.items():
            kl = k.lower()  # (local)
            if ("did_not" in kl) or ("not_load" in kl) or ("reserved" in kl):
                continue
            if ("load" in kl or "input" in kl) and obs2_token in " ".join(_flat(v)):
                return True
        return False

    # Axis-A NOT-loaded: explicit `did_not_load_*` field OR absence of obs2 token
    # in any affirmatively-loaded key.
    def _not_loaded_obs2(ip: dict) -> bool:  # (local)
        loaded = _loaded_obs2(ip)  # (local)
        return not loaded

    b_loads = _loaded_obs2(b_ip)  # (local)
    a_loads = _loaded_obs2(a_ip)  # (local)
    a_not = _not_loaded_obs2(a_ip)  # (local)

    # Axis-B's own orthogonality block (self-declared) corroborates.
    b_self = axis_b.get("substrate_input_orthogonality_obs_2", {})  # (local)
    b_self_ok = (
        isinstance(b_self, dict)
        and _verdict_of(b_self) == "PASS"
        and bool(b_self.get("obs_2_loaded_by_axis_B_only"))
    )  # (local)

    floor_ok = (b_loads or b_self_ok) and a_not and (not a_loads)  # >=1 obs by exactly one reviewer (local)
    ceiling_no_caveat = floor_ok  # obs_2 is the only shared-relevant grid; Axis-B-exclusive => ceiling (local)
    detail = {
        "obs_2_token": obs2_token,
        "axis_B_loads_obs_2": b_loads or b_self_ok,
        "axis_A_loads_obs_2": a_loads,
        "axis_A_not_loaded_obs_2": a_not,
        "axis_B_self_declared_orthogonality_PASS": b_self_ok,
        "floor_ok_>=1_obs_exactly_one_reviewer": floor_ok,
        "structural_ceiling_NO_overlap_caveat": ceiling_no_caveat,
    }
    return floor_ok, ceiling_no_caveat, detail


def _machinery_not_self_authored(axis_a: dict, axis_b: dict) -> tuple[bool, dict]:
    """joint-theorem-promotion.md §"Audit at plan-freeze" item 6: the
    cross-reviewer's verdict-layer audit machinery is NOT structurally
    self-authored. Both axes apply the shared 5-anatomy/3-level + Hybrid
    Independence Test machinery (rule-file canonical, not authored by either
    reviewer)."""
    def _msa(axis_json: dict) -> str:  # (local)
        blk = axis_json.get("machinery_not_self_authored", {})  # (local)
        if isinstance(blk, dict):
            return _verdict_of(blk)
        return "ABSENT"
    a_v = _msa(axis_a)  # (local)
    b_v = _msa(axis_b)  # (local)
    # default-safe: shared rule-file machinery => PASS unless a reviewer flags self-authoring
    ok = (a_v in ("PASS", "ABSENT")) and (b_v in ("PASS", "ABSENT"))  # (local)
    return ok, {"axis_A": a_v, "axis_B": b_v, "pass": ok}


def _oaa_ok(axis_a: dict, axis_b: dict) -> tuple[bool, dict]:
    """OAA exclusion {mack-cosmic-bridge} (the §VII.AX cluster Stage-1
    sole-writer) satisfied: neither reviewer is in the exclusion set; neither
    read the workshop transcript (downstream-inheritance reach check)."""
    a_rev = str(axis_a.get("reviewer", "")).lower()  # (local)
    b_rev = str(axis_b.get("reviewer", "")).lower()  # (local)
    excl_ok = not any(x in a_rev for x in OAA_EXCLUSION) and \
        not any(x in b_rev for x in OAA_EXCLUSION)  # (local)

    def _transcript_not_read(ip: dict) -> bool:  # (local)
        for k, v in ip.items():
            if "workshop_transcript" in k.lower():
                if isinstance(v, bool):
                    return not v
        return True  # absent flag => assume not read (default-safe)

    a_ip = axis_a.get("independence_protocol", {})  # (local)
    b_ip = axis_b.get("independence_protocol", {})  # (local)
    ok = excl_ok and _transcript_not_read(a_ip) and _transcript_not_read(b_ip)  # (local)
    return ok, {
        "axis_A_reviewer": a_rev,
        "axis_B_reviewer": b_rev,
        "exclusion_set": sorted(OAA_EXCLUSION),
        "exclusion_ok": excl_ok,
        "transcript_not_read_both": _transcript_not_read(a_ip) and _transcript_not_read(b_ip),
        "pass": ok,
    }


def _convention_ok(axis_a: dict, axis_b: dict) -> tuple[bool, dict]:
    """Each axis's CLASS pin is FULL (FULL CM-1995 §III.4 evaluation); the
    aggregation convention ends with -FULL."""
    agg_ok = CONVENTION.endswith("-FULL")  # (local)
    # the axes may declare a FULL class tag; default-safe if absent (the registry
    # entry is FULL CM-1995 §III.4 by construction).
    return agg_ok, {"aggregation_convention_ends_FULL": agg_ok}


# ---------------------------------------------------------------------------
# Strict PASS-AND aggregation
# ---------------------------------------------------------------------------
def aggregate(axis_a: dict, axis_b: dict) -> dict:
    a_comp = _axis_composite(axis_a)  # (local)
    b_comp = _axis_composite(axis_b)  # (local)
    joint_ok, joint_info, joint_detail = _joint_pass_and(axis_a, axis_b)  # (local)
    ortho_floor, ortho_ceiling, ortho_detail = _orthogonality_obs_2(axis_a, axis_b)  # (local)
    msa_ok, msa_detail = _machinery_not_self_authored(axis_a, axis_b)  # (local)
    oaa_ok, oaa_detail = _oaa_ok(axis_a, axis_b)  # (local)
    conv_ok, conv_detail = _convention_ok(axis_a, axis_b)  # (local)

    # structural-gate failures (independent of the per-clause verdicts)
    structural_gate_fail = (
        (not ortho_floor) or (not msa_ok) or (not oaa_ok) or (not conv_ok)
    )  # (local)

    composite_pass = (
        a_comp == "PASS" and b_comp == "PASS" and joint_ok
        and ortho_floor and msa_ok and oaa_ok and conv_ok
    )  # (local)
    # hard FAIL drivers
    hard_fail = (
        a_comp == "FAIL" or b_comp == "FAIL" or (not joint_ok and not joint_info)
        or structural_gate_fail
    )  # (local)
    # INFO: a reviewer returned INFO on a clause/composite, no hard FAIL
    info = (
        (not composite_pass) and (not hard_fail)
        and (a_comp == "INFO" or b_comp == "INFO" or joint_info)
    )  # (local)

    if composite_pass:
        composite = "PASS"  # (local)
    elif hard_fail:
        composite = "FAIL"  # (local)
    elif info:
        composite = "INFO"  # (local)
    else:
        composite = "FAIL"  # (local)

    stage_3_eligibility = (
        "STAGE-3-PERMANENT-ELIGIBLE" if composite == "PASS"
        else "STAGE-1-CANDIDATE"
    )  # (local)

    return {
        "axis_A_connes_composite": a_comp,
        "axis_B_volovik_composite": b_comp,
        "joint_clause_pass_and": joint_ok,
        "joint_clause_detail": joint_detail,
        "substrate_input_orthogonality": {
            "floor_ok": ortho_floor,
            "structural_ceiling_NO_caveat": ortho_ceiling,
            "detail": ortho_detail,
        },
        "machinery_not_self_authored": {"pass": msa_ok, "detail": msa_detail},
        "oaa_exclusion": {"pass": oaa_ok, "detail": oaa_detail},
        "convention_ends_FULL": {"pass": conv_ok, "detail": conv_detail},
        "structural_gate_fail": structural_gate_fail,
        "composite_hard_fail": hard_fail,
        "composite_info": info,
        "composite_verdict": composite,
        "stage_3_eligibility": stage_3_eligibility,
        "mack_tag_flip_licensed": composite == "PASS",
    }


# ---------------------------------------------------------------------------
# Emission
# ---------------------------------------------------------------------------
def build_value_field(agg: dict) -> str:
    so = agg["substrate_input_orthogonality"]  # (local)
    return (
        f"Stage-2-cross-axis-verify_VII-AX-MULTI-PIN-ATLAS_"
        f"axisA_connes={agg['axis_A_connes_composite']}_"
        f"axisB_volovik={agg['axis_B_volovik_composite']}_"
        f"JOINT-clause_PASS-AND={agg['joint_clause_pass_and']}_"
        f"substrate_input_orthogonality_obs_2_floor={so['floor_ok']}_"
        f"structural_ceiling_NO_caveat={so['structural_ceiling_NO_caveat']}_"
        f"machinery_not_self_authored={agg['machinery_not_self_authored']['pass']}_"
        f"OAA_excl_mack_satisfied={agg['oaa_exclusion']['pass']}_"
        f"convention_ends_FULL={agg['convention_ends_FULL']['pass']}_"
        f"stage3={agg['stage_3_eligibility']}_"
        f"mack_tag_flip_licensed={agg['mack_tag_flip_licensed']}"
    )


def append_verdict(
    verdict: str, value: str, audit_sha: str, content_sha: str,
    supersedes: str | None = None,
) -> None:
    """Append a single canonical dual-SHA verdict line + companion row (atomic
    single open("a")). Option-A: corrective line carries supersedes=<full-64-char>
    ONLY when a prior non-superseded line exists (clean first emission => none)."""
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
        f"Stage-2 cross-axis PASS-AND (connes Axis-A + volovik Axis-B); "
        f"[VERIFY-THEOREM] no [SIGN] 3-tuple{supersedes_note}\n"
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
        "aggregation": agg,
        "axis_A_json": str(AXIS_A_JSON.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "axis_B_json": str(AXIS_B_JSON.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "stage_1_source_verdict_audit_sha256": W2_1_SOURCE_AUDIT_SHA,
        "verdict_line_emitted": emitted,
        "M_KK": float(M_KK),
        "tau_fold": float(tau_fold),
    }
    JSON_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def write_npz(verdict: str, audit_sha: str, content_sha: str, agg: dict) -> None:
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        composite_verdict=verdict,
        axis_A_connes_composite=agg.get("axis_A_connes_composite", "ABSENT"),
        axis_B_volovik_composite=agg.get("axis_B_volovik_composite", "ABSENT"),
        joint_clause_pass_and=bool(agg.get("joint_clause_pass_and", False)),
        substrate_input_orthogonality_floor=bool(
            agg.get("substrate_input_orthogonality", {}).get("floor_ok", False)
        ),
        structural_ceiling_no_caveat=bool(
            agg.get("substrate_input_orthogonality", {}).get("structural_ceiling_NO_caveat", False)
        ),
        oaa_exclusion_pass=bool(agg.get("oaa_exclusion", {}).get("pass", False)),
        convention_ends_full=bool(agg.get("convention_ends_FULL", {}).get("pass", False)),
        stage_3_eligibility=agg.get("stage_3_eligibility", "STAGE-1-CANDIDATE"),
        mack_tag_flip_licensed=bool(agg.get("mack_tag_flip_licensed", False)),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        M_KK=float(M_KK),
        tau_fold=float(tau_fold),
    )


# ---------------------------------------------------------------------------
# Main — aggregation; emission gated behind --emit AND both-JSON presence
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()  # (local)
    ap.add_argument(
        "--emit",
        action="store_true",
        help="emit the W4-2 verdict line (orchestrator triggers this as a SEPARATE step "
        "once BOTH axis JSONs are on disk). Without it, dry-run only (no verdict line).",
    )
    args = ap.parse_args()  # (local)

    print(f"=== {GATE_ID} (aggregation) ===")
    print("Input-pin SHAs (first lines of stdout):")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # --- both axis JSONs must exist before aggregation can complete ---
    if not AXIS_A_JSON.exists() or not AXIS_B_JSON.exists():
        missing = [p.name for p in (AXIS_A_JSON, AXIS_B_JSON) if not p.exists()]  # (local)
        print(f"AGGREGATION DEFERRED: axis verdict JSON(s) absent: {missing}")
        print(
            "This dispatch authored the Axis-B JSON + this aggregation script. The "
            "orchestrator re-invokes with --emit once Axis-A's JSON is on disk."
        )
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
        write_npz(verdict, audit_sha, content_sha, agg)
        print(f"DRY-RUN: would emit '{verdict}'. Verdict line NOT appended (--emit not set).")
        supersedes = find_latest_prior_audit_sha()  # (local)
        sup_field = f"_supersedes={supersedes}" if supersedes else ""  # (local)
        print("PASS-AND boundary preview (the line the --emit step WILL append):")
        print(
            f"  {GATE_ID}: {verdict} -- value='{value}{sup_field}' "
            f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+"
        )
        return 0

    # --- EMIT (orchestrator-triggered separate step) ---
    # Option-A: clean first emission => no supersedes tag (None). If a prior
    # non-superseded S93 W4-2 line exists (a re-run), supersede it.
    supersedes = find_latest_prior_audit_sha()  # (local)
    append_verdict(verdict, value, audit_sha, content_sha, supersedes=supersedes)
    write_json(verdict, value, audit_sha, content_sha, agg, emitted=True)
    write_npz(verdict, audit_sha, content_sha, agg)
    sup_msg = f"; supersedes={supersedes}" if supersedes else " (clean first emission, no supersedes)"  # (local)
    print(f"VERDICT: {verdict} (emitted{sup_msg})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
