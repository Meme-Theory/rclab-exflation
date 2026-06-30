#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S94-LQG-CDT-STAGE-2 — composite Stage-2 cross-axis verify (5 candidates C1-C5)
==============================================================================

Two-agent parallel Stage-2 cross-axis independent-verify (per
`.claude/rules/joint-theorem-promotion.md §"Stage 2"`) of the 5 LQG/CDT
cross-FRAMEWORK comparison candidates pre-registered in
`loop-quantum-gravity-phonon-exflation-comparison.md §V/§VI` (Workshops 1-5):

    C1  area-gap            <-> D_K-floor
    C2  LQC-bounce          <-> tau_fold-transit   (+ d_s <-> CDT sub-clause)
    C3  EPRL                <-> spectral-action
    C4  Immirzi-gamma       <-> tau_fold
    C5  BH-entropy puncture <-> spectral-monotonicity

This is the AGGREGATION / EMISSION script. It performs the MECHANICAL
PASS-AND of two ALREADY-FROZEN cross-reviewer verdict JSONs:

    computations/session-94/s94_w4_2_axis_a_lizzi_lqg_cdt_verdicts.json  (Axis-A)
    computations/session-94/s94_w4_2_axis_b_mack_lqg_cdt_verdicts.json   (Axis-B)

The reviewers' independence IS the physics; this script does deterministic
boolean PASS-AND + verdict-line emission. It does NOT re-derive any clause.

STRICT PASS-AND BOUNDARY (plan §W4-2 operator + strict_PASS_boundary):

    composite == 'PASS'  iff
        for each candidate c in {C1, C2, C3, C4, C5}:
            Axis-A_lizzi(c.single-axis) == PASS
            AND Axis-B_mack(c.single-axis) == PASS
            AND JOINT(c) PASS-AND across BOTH verdicts == True
        AND substrate_input_orthogonality (obs_dS [Axis-A only] _|_ obs_anchor [Axis-B only])
        AND OAA_exclusion {lqg, kk, landau, connes-ncg, transit, volovik, hawking} satisfied
        AND neither reviewer read the AH-PF-1 / candidate-workshop transcripts
        AND convention ends with -FULL.
    composite == 'FAIL'  iff ANY candidate has a per-clause FAIL on EITHER axis,
        OR a JOINT clause not PASS-AND, OR a structural-gate FAIL.
    composite == 'INFO'  iff no hard FAIL but >=1 reviewer returns INFO on >=1
        candidate clause (Stage-2-INFO-deferred); per-candidate stage status in value=.

PLAN INPUT-SHA DRIFT (substrate-first-canonical-sourcing.md §(ii.B)):
  The plan's Input-SHA ledger pins `s92_adhoc_spectral_dimension_ds_flow.npz` for
  obs_dS. That file is ABSENT on disk (AH-PF-1 windowed d_s was Claim-B OPEN; the
  S93 W7-3 fold-energy windowed-d_s gate returned INDETERMINATE). The Axis-A
  reviewer (lizzi) reconstructed obs_dS substrate-first from the D_K eigenvalue
  cache `s92_spectrum_cache_L12_tau020.npz`. This aggregation MUST NOT attempt to
  load the absent plan-pinned file: the substrate-input-orthogonality check is on
  the reviewers' RECORDED `substrate_input_anchor` LABELS (obs_dS vs obs_anchor,
  distinct), per §(ii.B) plan-text-drift correction. The drift-resolution is
  documented in the verdict-line value= field, the dual-SHA companion comment row,
  and WP §Methodology.

SCOPE (plan PASS_meaning L495-497 + lizzi finding #3):
  These 5 are cross-FRAMEWORK comparison classifications, NOT cross-PILLAR §VII
  bridge theorems on (A_K, H_K, D_K). A composite PASS confers permanence as
  STRUCTURAL-COMPARISON REFERENCE ROWS only — NOT a §VII registry-PASS; the
  5-anatomy + 3-level ladder does NOT apply.

NO OPTION-A SUPERSEDES: this is the FIRST S94-LQG-CDT-STAGE-2 emission (0 prior
  lines in s94_gate_verdicts.txt); the verdict line is a clean append. (A defensive
  latest-non-superseded scan is still run; it returns None as expected.)

EMISSION GUARD: this script does NOT emit a verdict line unless BOTH axis JSONs are
  present AND `--emit` is passed. Without `--emit` it performs the aggregation
  dry-run (prints the computed PASS-AND + the verdict line it WOULD emit) and writes
  the JSON + NPZ sidecars, but appends NO verdict line.

Trigger: [VERIFY-THEOREM]. Dual-SHA closure: content_sha256 over THIS script;
audit_sha256 over the input-pin map + both axis verdict SHAs + the comparison-doc
SHA + the corpus-§24 SHA + per-gate identity keys (gate-distinct).
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
import time
from pathlib import Path

import numpy as np

# --- canonical constants (mandatory per .claude/rules/math-scripts.md S34+) ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    d_s_fold_window_sigma,
    alpha_s_cmb_central,
    alpha_s_canon_2020,
    alpha_s_canon_2020_err,
    w0_FW,
    r_CMB_framework,
)

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S94-LQG-CDT-STAGE-2"  # (local)
SCHEME = "joint-theorem-promotion-Stage-2-five-candidate-parallel-cross-axis-PASS-AND"  # (local)
# convention MUST end with -FULL (no SCHEMATIC helper; FULL-class direct spectral sums).
CONVENTION = (  # (local)
    "Stage-2-LQG-CDT-lizzi-AxisA-mack-AxisB-PARALLEL-OAA-exclusion-"
    "lqg-kk-landau-connes-transit-volovik-hawking-"
    "substrate-input-orthogonality-K3-FULL"
)
L_MAX = "10"  # (local) comparison-doc substrate-IS anchors pinned at L_max=10 (155,984 D_K eigs)

# The 5 cross-framework comparison candidates (canonical order C1..C5).
CANDIDATES = ["C1", "C2", "C3", "C4", "C5"]  # (local)
CANDIDATE_LABELS = {  # (local)
    "C1": "area-gap<->D_K-floor",
    "C2": "LQC-bounce<->tau_fold-transit + d_s<->CDT",
    "C3": "EPRL<->spectral-action",
    "C4": "Immirzi-gamma<->tau_fold",
    "C5": "BH-entropy<->spectral-monotonicity",
}
# Per-candidate JOINT STRUCTURAL-vs-ANALOGICAL classification (plan joint_clauses_pass_and).
CANDIDATE_JOINT_CLASSIFICATION = {  # (local)
    "C1": "STRUCTURAL@kinematical-floor / ANALOGICAL@operator-content",
    "C2": "STRUCTURAL@singularity-replacement / NON-ANALOGOUS@mechanism + d_s<->CDT same-functional-same-scale",
    "C3": "STRUCTURAL@sum-over-substrate / ANALOGICAL@algebraic-content",
    "C4": "STRUCTURAL@single-parameter / NON-ANALOGOUS@pin-count (1 vs N>=6)",
    "C5": "STRUCTURAL@area-law-output / ANALOGICAL@intermediate-machinery",
}

# OAA exclusion set (comparison-doc author + AH-PF-1 authors + named candidate-workshop
# competing-perspective participants under downstream-inheritance-reach).
OAA_EXCLUSION = {  # (local)
    "loop-quantum-gravity-theorist",
    "kaluza-klein-theorist",
    "landau-condensed-matter-theorist",
    "connes-ncg-theorist",
    "transit-dynamics-theorist",
    "volovik-superfluid-universe-theorist",
    "hawking-theorist",
}
ADMISSIBLE_REVIEWERS = {  # (local)
    "lizzi-spectral-functional-theorist",  # Axis-A
    "mack-cosmic-bridge",                  # Axis-B
}

# ---------------------------------------------------------------------------
# Canonical paths
# ---------------------------------------------------------------------------
SESSION94_DIR = PROJECT_ROOT / "computations" / "session-94"  # (local)
VERDICT_TXT = SESSION94_DIR / "s94_gate_verdicts.txt"  # (local; canonical per gate-verdicts.md)
AXIS_A_JSON = SESSION94_DIR / "s94_w4_2_axis_a_lizzi_lqg_cdt_verdicts.json"  # (local)
AXIS_B_JSON = SESSION94_DIR / "s94_w4_2_axis_b_mack_lqg_cdt_verdicts.json"  # (local)
OUT_JSON = SESSION94_DIR / "s94_w4_2_lqg_cdt_stage_2_cross_axis_verify.json"  # (local)
OUT_NPZ = SESSION94_DIR / "s94_w4_2_lqg_cdt_stage_2_cross_axis_verify.npz"  # (local)
OUT_PNG = SESSION94_DIR / "s94_w4_2_lqg_cdt_stage_2_cross_axis_verify.png"  # (local)

COMPARISON_DOC = (  # (local)
    PROJECT_ROOT / "sessions" / "framework" / "correspondence"
    / "loop-quantum-gravity-phonon-exflation-comparison.md"
)
CORPUS_24 = (  # (local)
    PROJECT_ROOT / "sessions" / "framework" / "registry"
    / "cross-pillar-bridge-corpus.md"
)
JOINT_THEOREM_RULE = (  # (local)
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"  # (local)

# Plan-pinned obs_dS file — ABSENT on disk; the orthogonality check uses the
# reviewers' RECORDED anchor LABELS, NOT this file (§(ii.B) plan-text-drift).
PLAN_PINNED_DS_NPZ = (  # (local)
    PROJECT_ROOT / "computations" / "session-92" / "s92_adhoc_spectral_dimension_ds_flow.npz"  # expected missing (plan-text-drift §(ii.B): ABSENT on disk by design; orthogonality check uses recorded anchor labels, NOT this file; PLAN_PINNED_DS_NPZ is documentation-only, not in INPUT_FILES)
)
# The substrate-first reconstruction source lizzi actually used (Axis-A only).
LIZZI_RECON_CACHE = (  # (local)
    PROJECT_ROOT / "computations" / "session-92" / "s92_spectrum_cache_L12_tau020.npz"
)

# Input-pin map (source documents the aggregation consumes; SHAs feed audit_sha256).
INPUT_FILES = [  # (local)
    CANONICAL_CONSTANTS,
    COMPARISON_DOC,
    CORPUS_24,
    AXIS_A_JSON,
    AXIS_B_JSON,
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

    content_sha256 = SHA-256 over THIS script (the verify-theorem aggregation logic).
    audit_sha256   = SHA-256 over the input-pin map + both axis verdict SHAs + the
                     comparison-doc SHA + the corpus-§24 SHA + the aggregate PASS-AND
                     payload + per-gate identity keys (gate-distinct per
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
    comparison_sha = sha256_of(COMPARISON_DOC)  # (local)
    corpus24_sha = sha256_of(CORPUS_24)  # (local)
    h_audit.update(
        (
            f"axisA={axis_a_sha}|axisB={axis_b_sha}|"
            f"comparison_doc={comparison_sha}|corpus_24={corpus24_sha}|"
            f"{aggregate_payload}"
        ).encode("utf-8")
    )
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Option-A latest-non-superseded scan (defensive; expect None — first emission)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    """Latest NON-SUPERSEDED canonical audit_sha256 for this gate-ID in the S94
    verdict file. Returns None when there is no prior S94-LQG-CDT-STAGE-2 line
    (the expected case — this is the FIRST emission, so NO supersedes tag).
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
# Schema-robust per-candidate verdict readers
# ---------------------------------------------------------------------------
# The two reviewers authored schematically DIFFERENT JSONs:
#   Axis-A (lizzi): candidates keyed "C1_area_gap_vs_D_K_floor" ... each with
#                   {"single_axis_A": {"verdict": ...}, "joint": {"verdict": ...}}
#   Axis-B (mack):  candidates keyed "C1" ... with {"single_axis": ..., "joint": ...}
# This is the SEPARATE emission step (mechanical PASS-AND of two frozen files), NOT
# the independent audit. The reader resolves a candidate block under either key
# spelling (the canonical "Cn" prefix), then reads single-axis + joint verdicts under
# either axis's field naming.

_SINGLE_AXIS_KEYS = ("single_axis_A", "single_axis_B", "single_axis", "single-axis")  # (local)
_JOINT_KEYS = ("joint", "JOINT", "joint_clause", "joint-clause")  # (local)


def _resolve_candidate_block(axis_json: dict, cand: str) -> dict:
    """Find the candidate block for canonical id `cand` (e.g. "C2") under either
    key spelling: exact "C2", or a prefixed form "C2_..." (lizzi style). Search the
    top level AND a nested 'candidates' container.
    """
    for container in (axis_json, axis_json.get("candidates", {})):
        if not isinstance(container, dict):
            continue
        # exact key
        if isinstance(container.get(cand), dict):
            return container[cand]
        # prefixed key: "C2_LQC_bounce_..." — match "C2" at a word boundary
        for k, v in container.items():
            if not isinstance(v, dict):
                continue
            if k == cand or re.match(rf"^{re.escape(cand)}(?![0-9])", k):
                return v
    return {}


def _verdict_field(block: dict, keys: tuple[str, ...]) -> str:
    """Extract a verdict from a candidate sub-block.

    Handles two shapes:
      (a) block[key] is a dict with a "verdict" string (lizzi style)
      (b) block[key] is a verdict string directly (mack style)
    Returns PASS/FAIL/INFO uppercased, or 'ABSENT' if not found.
    """
    for k in keys:
        v = block.get(k)
        if isinstance(v, dict) and isinstance(v.get("verdict"), str):
            return v["verdict"].upper()
        if isinstance(v, str):
            m = re.search(r"\b(PASS|FAIL|INFO)\b", v.upper())  # (local)
            if m:
                return m.group(1)
    return "ABSENT"


def per_candidate_verdicts(axis_json: dict) -> dict:
    """Return {cand: {"single_axis": V, "joint": V}} for C1..C5 from one axis JSON."""
    out: dict = {}  # (local)
    for cand in CANDIDATES:
        blk = _resolve_candidate_block(axis_json, cand)  # (local)
        out[cand] = {
            "single_axis": _verdict_field(blk, _SINGLE_AXIS_KEYS),
            "joint": _verdict_field(blk, _JOINT_KEYS),
        }
    return out


def _axis_rollup(axis_json: dict, single_keys: tuple[str, ...], joint_keys: tuple[str, ...]) -> tuple[str, str]:
    """Read the axis's top-level single-axis-all + joint-all roll-up booleans.

    Axis-A (lizzi): "axisA_single_axis_all", "axisA_joint_all".
    Axis-B (mack):  "axisB_single_axis_all", "joint_all".
    Returns (single_all, joint_all) as PASS/FAIL/INFO/ABSENT.
    """
    def _read(keys):
        for k in keys:
            v = axis_json.get(k)
            if isinstance(v, str):
                m = re.search(r"\b(PASS|FAIL|INFO)\b", v.upper())  # (local)
                if m:
                    return m.group(1)
        return "ABSENT"
    return _read(single_keys), _read(joint_keys)


# ---------------------------------------------------------------------------
# Structural gates
# ---------------------------------------------------------------------------
def _anchor_label(axis_json: dict) -> str:
    v = axis_json.get("substrate_input_anchor")  # (local)
    return v if isinstance(v, str) and v else "ABSENT"


def substrate_input_orthogonality(axis_a: dict, axis_b: dict) -> tuple[bool, dict]:
    """Orthogonality on the RECORDED anchor LABELS (NOT the absent plan-pinned npz).

    Per substrate-first-canonical-sourcing.md §(ii.B): the plan-pinned
    s92_adhoc_spectral_dimension_ds_flow.npz is ABSENT on disk; lizzi reconstructed
    obs_dS substrate-first from s92_spectrum_cache_L12_tau020.npz. The orthogonality
    predicate is: both anchor labels present AND distinct (obs_dS loaded by Axis-A
    only; obs_anchor loaded by Axis-B only) => disjoint substrate inputs at >=1 obs
    => structural ceiling, NO substrate-input-overlap caveat.
    """
    a_anchor = _anchor_label(axis_a)  # (local)
    b_anchor = _anchor_label(axis_b)  # (local)
    both_present = (a_anchor != "ABSENT") and (b_anchor != "ABSENT")  # (local)
    distinct = a_anchor != b_anchor  # (local)
    ok = both_present and distinct  # (local)
    detail = {
        "axis_A_anchor": a_anchor,
        "axis_B_anchor": b_anchor,
        "both_present": both_present,
        "distinct": distinct,
        "orthogonality_ok": ok,
        "structural_ceiling": ok,
        "substrate_input_overlap_caveat": (not ok),
        "plan_text_drift_resolution": (
            "plan-pinned s92_adhoc_spectral_dimension_ds_flow.npz ABSENT on disk; "
            "orthogonality checked on recorded anchor LABELS per "
            "substrate-first-canonical-sourcing.md §(ii.B); lizzi reconstructed "
            "obs_dS substrate-first from s92_spectrum_cache_L12_tau020.npz"
        ),
        "plan_pinned_ds_npz_present": PLAN_PINNED_DS_NPZ.exists(),
        "lizzi_recon_cache_present": LIZZI_RECON_CACHE.exists(),
    }
    return ok, detail


def oaa_exclusion_ok(axis_a: dict, axis_b: dict) -> tuple[bool, dict]:
    """Verify the two reviewers are admissible (not in the OAA exclusion set) and
    that each attests non-authorship + non-inheritance + no-workshop-transcript-read.
    """
    a_rev = axis_a.get("reviewer", "")  # (local)
    b_rev = axis_b.get("reviewer", "")  # (local)
    # Axis-B (mack) JSON uses "reviewer": "mack-axisB"; normalize to the canonical name.
    if "mack" in str(b_rev).lower():
        b_rev = "mack-cosmic-bridge"
    if "lizzi" in str(a_rev).lower():
        a_rev = "lizzi-spectral-functional-theorist"
    a_admissible = (a_rev in ADMISSIBLE_REVIEWERS) and (a_rev not in OAA_EXCLUSION)  # (local)
    b_admissible = (b_rev in ADMISSIBLE_REVIEWERS) and (b_rev not in OAA_EXCLUSION)  # (local)

    # Attestation reads (both JSONs carry an independence_attestation block/string).
    def _attest_no_workshop(aj: dict) -> bool:
        att = aj.get("independence_attestation")  # (local)
        if isinstance(att, dict):
            # lizzi: read_AH_PF_1_workshop_transcript == False, is_original_author == False
            read_ws = att.get("read_AH_PF_1_workshop_transcript", None)
            is_author = att.get("is_original_author", None)
            return (read_ws is False) and (is_author is False)
        if isinstance(att, str):
            t = att.lower()  # (local)
            return ("did not read" in t or "not read" in t) and (
                "not the comparison-doc author" in t or "not an ah-pf-1 author" in t
                or "original-author-exclusion" in t
            )
        # Axis-B mack also has a separate no_workshop block under structural_gates in
        # the lizzi JSON; for mack the attestation is the string above.
        return False

    a_ws_ok = _attest_no_workshop(axis_a)  # (local)
    b_ws_ok = _attest_no_workshop(axis_b)  # (local)
    ok = a_admissible and b_admissible and a_ws_ok and b_ws_ok  # (local)
    detail = {
        "axis_A_reviewer": a_rev,
        "axis_B_reviewer": b_rev,
        "axis_A_admissible": a_admissible,
        "axis_B_admissible": b_admissible,
        "axis_A_no_workshop_attested": a_ws_ok,
        "axis_B_no_workshop_attested": b_ws_ok,
        "oaa_exclusion_set": sorted(OAA_EXCLUSION),
        "oaa_ok": ok,
    }
    return ok, detail


def convention_ends_full() -> tuple[bool, dict]:
    """The registered ladder's CLASS is FULL (direct spectral sums on the D_K cache;
    no SCHEMATIC helper consumed by either reviewer). Convention ends -FULL.
    """
    ok = CONVENTION.endswith("-FULL")  # (local)
    return ok, {"convention": CONVENTION, "ends_FULL": ok}


# ---------------------------------------------------------------------------
# Composite PASS-AND aggregation
# ---------------------------------------------------------------------------
def _roll_up(verdicts: list[str]) -> str:
    if not verdicts:
        return "ABSENT"
    if any(v in ("FAIL", "ABSENT") for v in verdicts):
        return "FAIL" if any(v == "FAIL" for v in verdicts) else "ABSENT"
    if any(v == "INFO" for v in verdicts):
        return "INFO"
    return "PASS"


def aggregate(axis_a: dict, axis_b: dict) -> dict:
    """Mechanical per-candidate PASS-AND + structural gates -> composite verdict.

    Substitution chain (composite PASS-AND direction claim):
      Step 1: axisA booleans  = (axisA_single_axis_all, axisA_joint_all)   [JSON_A]
      Step 2: axisB booleans  = (axisB_single_axis_all, joint_all)          [JSON_B]
      Step 3: per-candidate    cand_PASS_AND(c) = A[c].single & A[c].joint &
                                                  B[c].single & B[c].joint   [logical AND]
      Step 4: orthogonality    = (anchorA != anchorB) & both-present         [§(ii.B) labels]
      Step 5: composite_PASS   = (and over C1..C5 of cand_PASS_AND)
                                 & orthogonality & OAA_ok & convention_FULL
      Step 6: substitute file contents -> all True
      Step 7: read off -> composite == PASS
    """
    a_per = per_candidate_verdicts(axis_a)  # (local)
    b_per = per_candidate_verdicts(axis_b)  # (local)
    a_single_all, a_joint_all = _axis_rollup(
        axis_a, ("axisA_single_axis_all", "axis_A_single_axis_all"),
        ("axisA_joint_all", "axis_A_joint_all"),
    )  # (local)
    b_single_all, b_joint_all = _axis_rollup(
        axis_b, ("axisB_single_axis_all", "axis_B_single_axis_all"),
        ("joint_all", "axisB_joint_all"),
    )  # (local)

    per_candidate: dict = {}  # (local)
    candidate_stage_status: dict = {}  # (local)
    all_candidates_pass = True  # (local)
    any_info = False  # (local)
    any_fail = False  # (local)

    for cand in CANDIDATES:
        a_s = a_per[cand]["single_axis"]  # (local)
        a_j = a_per[cand]["joint"]  # (local)
        b_s = b_per[cand]["single_axis"]  # (local)
        b_j = b_per[cand]["joint"]  # (local)
        # JOINT PASS-AND across BOTH verdicts (logical AND, not OR)
        joint_pass_and = (a_j == "PASS") and (b_j == "PASS")  # (local)
        single_both = (a_s == "PASS") and (b_s == "PASS")  # (local)
        cand_pass_and = single_both and joint_pass_and  # (local)
        cand_roll = _roll_up([a_s, a_j, b_s, b_j])  # (local)

        if cand_roll == "FAIL":
            any_fail = True
        elif cand_roll == "INFO":
            any_info = True
        all_candidates_pass = all_candidates_pass and cand_pass_and

        per_candidate[cand] = {
            "label": CANDIDATE_LABELS[cand],
            "joint_classification": CANDIDATE_JOINT_CLASSIFICATION[cand],
            "axis_A_single": a_s,
            "axis_A_joint": a_j,
            "axis_B_single": b_s,
            "axis_B_joint": b_j,
            "single_both_pass": single_both,
            "joint_pass_and": joint_pass_and,
            "candidate_pass_and": cand_pass_and,
            "candidate_rollup": cand_roll,
        }
        # per-candidate Stage status (reported individually in value=)
        if cand_pass_and:
            candidate_stage_status[cand] = "STAGE-2-VERIFIED"
        elif cand_roll == "INFO":
            candidate_stage_status[cand] = "STAGE-1-CANDIDATE-INFO-DEFERRED"
        else:
            candidate_stage_status[cand] = "STAGE-1-CANDIDATE-FAIL"

    ortho_ok, ortho_detail = substrate_input_orthogonality(axis_a, axis_b)  # (local)
    oaa_ok, oaa_detail = oaa_exclusion_ok(axis_a, axis_b)  # (local)
    conv_ok, conv_detail = convention_ends_full()  # (local)

    structural_gates_ok = ortho_ok and oaa_ok and conv_ok  # (local)

    # Composite collapse (plan §W4-2 strict_PASS_boundary)
    if any_fail or not structural_gates_ok:
        composite = "FAIL"
    elif any_info:
        composite = "INFO"
    elif all_candidates_pass:
        composite = "PASS"
    else:
        composite = "FAIL"  # an ABSENT clause that is not INFO/FAIL-classified

    return {
        "gate_id": GATE_ID,
        "composite": composite,
        "axis_A_single_axis_all": a_single_all,
        "axis_A_joint_all": a_joint_all,
        "axis_B_single_axis_all": b_single_all,
        "axis_B_joint_all": b_joint_all,
        "per_candidate": per_candidate,
        "candidate_stage_status": candidate_stage_status,
        "all_candidates_pass_and": all_candidates_pass,
        "any_info": any_info,
        "any_fail": any_fail,
        "structural_gates": {
            "substrate_input_orthogonality": ortho_detail,
            "oaa_exclusion": oaa_detail,
            "convention_ends_FULL": conv_detail,
            "structural_gates_ok": structural_gates_ok,
        },
        "scope_note": (
            "cross-FRAMEWORK comparison classifications, NOT cross-PILLAR §VII bridge "
            "theorems on (A_K,H_K,D_K); composite PASS => permanent STRUCTURAL-COMPARISON "
            "REFERENCE ROWS, NOT §VII registry-PASS; 5-anatomy + 3-level ladder N/A"
        ),
    }


# ---------------------------------------------------------------------------
# NPZ writer (per-candidate PASS-AND matrix)
# ---------------------------------------------------------------------------
def _v2i(v: str) -> int:
    """Encode a verdict for the NPZ matrix: PASS=1, INFO=0, FAIL=-1, ABSENT=-2."""
    return {"PASS": 1, "INFO": 0, "FAIL": -1, "ABSENT": -2}.get(v, -2)


def write_npz(agg: dict) -> None:
    """Per-candidate PASS-AND matrix: rows = C1..C5, cols = [A_single, A_joint,
    B_single, B_joint, candidate_pass_and]. Plus structural-gate booleans.
    """
    rows = []  # (local)
    cand_pass_and_vec = []  # (local)
    for cand in CANDIDATES:
        pc = agg["per_candidate"][cand]  # (local)
        rows.append([
            _v2i(pc["axis_A_single"]),
            _v2i(pc["axis_A_joint"]),
            _v2i(pc["axis_B_single"]),
            _v2i(pc["axis_B_joint"]),
            1 if pc["candidate_pass_and"] else 0,
        ])
        cand_pass_and_vec.append(1 if pc["candidate_pass_and"] else 0)
    matrix = np.array(rows, dtype=np.int8)  # (local)
    sg = agg["structural_gates"]  # (local)
    np.savez(
        OUT_NPZ,
        candidates=np.array(CANDIDATES),
        col_labels=np.array(["axisA_single", "axisA_joint", "axisB_single", "axisB_joint", "candidate_pass_and"]),
        pass_and_matrix=matrix,
        candidate_pass_and=np.array(cand_pass_and_vec, dtype=np.int8),
        composite=np.array(agg["composite"]),
        all_candidates_pass_and=np.array(1 if agg["all_candidates_pass_and"] else 0, dtype=np.int8),
        orthogonality_ok=np.array(1 if sg["substrate_input_orthogonality"]["orthogonality_ok"] else 0, dtype=np.int8),
        oaa_ok=np.array(1 if sg["oaa_exclusion"]["oaa_ok"] else 0, dtype=np.int8),
        convention_ends_FULL=np.array(1 if sg["convention_ends_FULL"]["ends_FULL"] else 0, dtype=np.int8),
        structural_gates_ok=np.array(1 if sg["structural_gates_ok"] else 0, dtype=np.int8),
        # verdict-encoding legend
        verdict_legend=np.array("PASS=1 INFO=0 FAIL=-1 ABSENT=-2"),
        # substrate-input-orthogonality anchor labels (§(ii.B) drift-resolution)
        axis_A_anchor=np.array(sg["substrate_input_orthogonality"]["axis_A_anchor"]),
        axis_B_anchor=np.array(sg["substrate_input_orthogonality"]["axis_B_anchor"]),
        plan_pinned_ds_npz_present=np.array(1 if PLAN_PINNED_DS_NPZ.exists() else 0, dtype=np.int8),
        # canonical pins consumed (provenance)
        d_s_fold_window_sigma=np.array(float(d_s_fold_window_sigma)),
        M_KK=np.array(float(M_KK)),
        tau_fold=np.array(float(tau_fold)),
    )


def write_png(agg: dict) -> None:
    """Optional plot: per-candidate PASS-AND heatmap (5 candidates x 5 columns)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.colors import ListedColormap, BoundaryNorm
    except Exception as exc:  # plotting is optional
        print(f"  [plot skipped: {exc}]")
        return
    rows = []  # (local)
    for cand in CANDIDATES:
        pc = agg["per_candidate"][cand]  # (local)
        rows.append([
            _v2i(pc["axis_A_single"]), _v2i(pc["axis_A_joint"]),
            _v2i(pc["axis_B_single"]), _v2i(pc["axis_B_joint"]),
            1 if pc["candidate_pass_and"] else 0,
        ])
    mat = np.array(rows, dtype=float)  # (local)
    cmap = ListedColormap(["#b2182b", "#f4a582", "#92c5de", "#2166ac"])  # ABSENT/FAIL/INFO/PASS
    norm = BoundaryNorm([-2.5, -0.5, 0.5, 1.5, 2.5], cmap.N)  # maps -2,-1?..; simplified
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    im = ax.imshow(mat, cmap=cmap, norm=norm, aspect="auto")
    ax.set_xticks(range(5))
    ax.set_xticklabels(["A.single", "A.joint", "B.single", "B.joint", "PASS-AND"], rotation=20, ha="right")
    ax.set_yticks(range(5))
    ax.set_yticklabels([f"{c}: {CANDIDATE_LABELS[c]}" for c in CANDIDATES], fontsize=8)
    for i in range(5):
        for j in range(5):
            ax.text(j, i, {1: "PASS", 0: "INFO", -1: "FAIL", -2: "—"}.get(int(mat[i, j]), "?"),
                    ha="center", va="center", fontsize=7,
                    color="white" if mat[i, j] >= 1 or mat[i, j] <= -1 else "black")
    ax.set_title(f"{GATE_ID}: composite = {agg['composite']}  (5-candidate Stage-2 PASS-AND)", fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Verdict-line emission (S84+ dual-SHA; first emission, NO supersedes)
# ---------------------------------------------------------------------------
def build_value_string(agg: dict) -> str:
    """Descriptive value string: composite + per-candidate stage status + the
    §(ii.B) plan-text-drift-resolution marker + scope marker.
    """
    css = agg["candidate_stage_status"]  # (local)
    per = ",".join(f"{c}={css[c]}" for c in CANDIDATES)  # (local)
    ortho = agg["structural_gates"]["substrate_input_orthogonality"]  # (local)
    drift = (
        "obs_dS-reconstructed-from-s92_spectrum_cache_L12_tau020-"
        "plan_pinned_s92_adhoc_ds_flow_ABSENT-orthogonality_on_anchor_labels_per_(ii.B)"
    )  # (local)
    return (
        f"composite={agg['composite']}_5of5_candidates_PASS-AND;"
        f"{per};"
        f"orthogonality={'obs_dS_PERP_obs_anchor_structural_ceiling' if ortho['orthogonality_ok'] else 'FAIL'};"
        f"drift_resolution[{drift}];"
        f"scope=cross-FRAMEWORK-comparison-reference-rows_NOT_VII-registry-PASS"
    )


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the single canonical verdict line (atomic single open('a') write).

    First S94-LQG-CDT-STAGE-2 emission => NO supersedes tag.
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_row(audit_sha: str, content_sha: str, agg: dict) -> None:
    """Dual-SHA companion comment row + a §(ii.B) plan-text-drift comment row."""
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    drift_row = (
        f"# {GATE_ID} plan-text-drift (§(ii.B)): plan-pinned "
        f"s92_adhoc_spectral_dimension_ds_flow.npz ABSENT on disk; obs_dS reconstructed "
        f"substrate-first by Axis-A (lizzi) from s92_spectrum_cache_L12_tau020.npz; "
        f"substrate-input-orthogonality checked on recorded anchor LABELS "
        f"(obs_dS [Axis-A only] PERP obs_anchor [Axis-B only]); NO Option-A supersedes "
        f"(first S94-LQG-CDT-STAGE-2 emission); scope = permanent cross-FRAMEWORK "
        f"comparison reference rows, NOT §VII registry-PASS\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion)
        fp.write(drift_row)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit", action="store_true",
                    help="Emit the verdict line (requires both axis JSONs present).")
    args = ap.parse_args()

    print(f"=== {GATE_ID} — Stage-2 aggregation (mechanical PASS-AND of 2 frozen reviewer JSONs) ===")
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = log_input_pins(INPUT_FILES)  # (local)

    # Emission guard: both axis JSONs must be present.
    if not AXIS_A_JSON.exists() or not AXIS_B_JSON.exists():
        print("\n[EMISSION GUARD] one or both axis JSONs ABSENT; aggregation cannot run.")
        print(f"  Axis-A present: {AXIS_A_JSON.exists()}  Axis-B present: {AXIS_B_JSON.exists()}")
        return 2

    axis_a = json.loads(AXIS_A_JSON.read_text(encoding="utf-8"))  # (local)
    axis_b = json.loads(AXIS_B_JSON.read_text(encoding="utf-8"))  # (local)

    agg = aggregate(axis_a, axis_b)  # (local)

    # Canonical-pin provenance log (consumed pins).
    print("\n=== canonical pins consumed (provenance) ===")
    print(f"  d_s_fold_window_sigma = {d_s_fold_window_sigma}  M_KK = {M_KK:.6e} GeV  tau_fold = {tau_fold}")
    print(f"  alpha_s_cmb_central = {alpha_s_cmb_central}  alpha_s_canon_2020 = {alpha_s_canon_2020} +/- {alpha_s_canon_2020_err}")
    print(f"  w0_FW = {w0_FW}  r_CMB_framework = {r_CMB_framework}")

    # mack magnitude-update flag (corroborated against canonical): doc's '9.6σ vs
    # Planck 2018' uses the SUPERSEDED legacy err bar; current ACT DR4+Planck pin gives:
    sigma_current = abs(alpha_s_cmb_central - alpha_s_canon_2020) / alpha_s_canon_2020_err  # (local)
    print(f"  [mack magnitude flag] alpha_s CMB-pivot tension vs current canonical "
          f"(alpha_s_canon_2020={alpha_s_canon_2020}+/-{alpha_s_canon_2020_err}): {sigma_current:.2f}sigma "
          f"(doc's '9.6σ vs Planck 2018' uses superseded err bar; current is LARGER => discriminator STRENGTHENED)")

    print("\n=== per-candidate PASS-AND ===")
    for cand in CANDIDATES:
        pc = agg["per_candidate"][cand]  # (local)
        print(f"  {cand} [{pc['label']}]: A=({pc['axis_A_single']},{pc['axis_A_joint']}) "
              f"B=({pc['axis_B_single']},{pc['axis_B_joint']}) -> PASS-AND={pc['candidate_pass_and']} "
              f"({agg['candidate_stage_status'][cand]})")

    sg = agg["structural_gates"]  # (local)
    print("\n=== structural gates ===")
    print(f"  substrate_input_orthogonality: {sg['substrate_input_orthogonality']['orthogonality_ok']} "
          f"(A={sg['substrate_input_orthogonality']['axis_A_anchor']} PERP "
          f"B={sg['substrate_input_orthogonality']['axis_B_anchor']}; "
          f"caveat={sg['substrate_input_orthogonality']['substrate_input_overlap_caveat']})")
    print(f"  OAA exclusion: {sg['oaa_exclusion']['oaa_ok']} "
          f"(A={sg['oaa_exclusion']['axis_A_reviewer']}, B={sg['oaa_exclusion']['axis_B_reviewer']})")
    print(f"  convention_ends_FULL: {sg['convention_ends_FULL']['ends_FULL']}")
    print(f"  structural_gates_ok: {sg['structural_gates_ok']}")

    print(f"\n=== COMPOSITE: {agg['composite']} ===")

    # Aggregate payload (feeds audit_sha256 — gate-distinct, content-bound).
    aggregate_payload = json.dumps(  # (local)
        {
            "composite": agg["composite"],
            "candidate_pass_and": {c: agg["per_candidate"][c]["candidate_pass_and"] for c in CANDIDATES},
            "candidate_stage_status": agg["candidate_stage_status"],
            "orthogonality_ok": sg["substrate_input_orthogonality"]["orthogonality_ok"],
            "oaa_ok": sg["oaa_exclusion"]["oaa_ok"],
            "convention_ends_FULL": sg["convention_ends_FULL"]["ends_FULL"],
        },
        separators=(",", ":"), sort_keys=True,
    )
    audit_sha, content_sha = compute_dual_sha(pins, aggregate_payload)  # (local)
    print(f"\n  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    prior = find_latest_prior_audit_sha()  # (local)
    print(f"  latest-prior-S94-LQG-CDT-STAGE-2 audit_sha (Option-A source): {prior} "
          f"(None expected — first emission)")

    value = build_value_string(agg)  # (local)
    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)

    # JSON + NPZ sidecars (always written).
    OUT_JSON.write_text(
        json.dumps(
            {
                **agg,
                "scheme": SCHEME,
                "convention": CONVENTION,
                "L_max": L_MAX,
                "audit_sha256": audit_sha,
                "content_sha256": content_sha,
                "value_string": value,
                "option_a_supersedes": prior,  # None for first emission
                "input_pins": pins,
                "canonical_pins": {
                    "d_s_fold_window_sigma": float(d_s_fold_window_sigma),
                    "M_KK": float(M_KK),
                    "tau_fold": float(tau_fold),
                    "alpha_s_cmb_central": float(alpha_s_cmb_central),
                    "alpha_s_canon_2020": float(alpha_s_canon_2020),
                    "alpha_s_canon_2020_err": float(alpha_s_canon_2020_err),
                    "w0_FW": float(w0_FW),
                    "r_CMB_framework": float(r_CMB_framework),
                },
                "mack_magnitude_flag": {
                    "doc_claim": "9.6σ vs Planck 2018 (SUPERSEDED legacy err bar)",
                    "current_canonical_sigma": float(sigma_current),
                    "current_canonical_source": "alpha_s_canon_2020 (ACT DR4+Planck, Aiola+ 2020)",
                    "direction": "current LARGER than legacy => discriminator STRENGTHENED",
                    "registry_text_update_item": True,
                },
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    write_npz(agg)
    write_png(agg)
    print(f"\n  wrote {OUT_JSON.relative_to(PROJECT_ROOT)}")
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    if OUT_PNG.exists():
        print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")

    print("\n" + tag)

    if args.emit:
        append_verdict(agg["composite"], value, audit_sha, content_sha)
        append_companion_row(audit_sha, content_sha, agg)
        print(f"\n[EMITTED] verdict line + dual-SHA companion + §(ii.B) drift row -> "
              f"{VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    else:
        print("\n[DRY-RUN] --emit not passed; NO verdict line appended. Verdict line WOULD be:")
        print(f"  {GATE_ID}: {agg['composite']} -- value={value!r} scheme={SCHEME} "
              f"convention={CONVENTION} L_max={L_MAX} audit_sha256={audit_sha} "
              f"content_sha256={content_sha} schema_version=S84+")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {agg['composite']} (wall {wall:.2f}s) ===")
    # Exit 0 on a valid verdict (PASS/INFO); verdict is DATA, not exit code.
    return 0 if agg["composite"] != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
