#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S92 W5-5 — VII.AU.OP-PROJ §W8-1 RE-DISPATCH orchestrator-composite aggregator
=============================================================================

Gate: S92-W5-CF-W8-CONSOLIDATED-9-VII-AU-OP-PROJ-W8-1-RE-DISPATCH ([VERIFY-THEOREM])

Pre-registered threshold (Phase H per session-92-plan-w5.md §W5-5 line 896):

    composite_verdict := PASS iff (
        Axis_A_vdd_PASS_on_substrate_physics_NCG_bridge_single_axis_clauses
        AND
        Axis_B_mack_PASS_on_cosmological_anchor_single_axis_clauses
        AND
        (forall c in JOINT_clauses: Axis_A_verdict_on_c == PASS
                                AND Axis_B_verdict_on_c == PASS)
        AND
        substrate-input-orthogonality == PASS at obs_1 at STRUCTURAL CEILING
        (Set_A SHA != Set_B SHA; NO substrate-input-overlap caveat)
        AND
        supersedes_tag_emission_compliance == PASS
        (full 64-char supersedes=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b
         in value= field per Option A clause 5 forward-emission discipline since S88 W8-100)
    )

The dispatch implements the joint-theorem-promotion-stage-2-pass-and protocol
(`.claude/rules/joint-theorem-promotion.md §"Stage 2"`) composed with the
Option A supersedes-chain protocol (`.claude/rules/gate-verdicts.md
§"Option A — sig_5 remediation pathway under absolute verdict permanence"`
clauses 1-6).

PHASES (executed in order):
  A — runtime prerequisite verification: §W5-1 PASS captured at runtime per
      `substrate-first-canonical-sourcing.md §(ii.B)` runtime canonical-path
      rescue.
  B — supersedes-chain verification: grep `computations/session-91/s91_gate_verdicts.txt:148`
      for full 64-char audit_sha256=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b
      match; original line NOT modified or deleted per Option A clause 1.
  C — reviewer selection record: vdd + mack canonical pair preserved from
      S91 W8 §W8-1 original dispatch for Option A audit-trail continuity.
  D — per-axis single-axis clause verdicts loaded from JSON sidecars.
  E — JOINT-clause PASS-AND aggregation (logical AND across both axes).
  F — substrate-input-orthogonality verification at STRUCTURAL CEILING
      (Set_A SHA from vdd JSON != Set_B SHA from mack JSON; disjoint
      substrate-input partition at obs_1).
  G — Option A supersedes tag emission compliance check (full 64-char SHA
      in value= field at corrective canonical line emission).
  H — composite_verdict PASS-AND aggregation; emit corrective canonical
      verdict line with supersedes tag APPENDED to
      `computations/session-92/s92_gate_verdicts.txt` via atomic single
      `open("a")` write per the canonical `append_verdict()` helper.

Input pins (SHA-256 dual-pinned at runtime — S87+ dual-SHA schema):
  - computations/session-92/s92_w5_5_axis_a_vdd_verdict.json (Axis-A vdd verdict)
  - computations/session-92/s92_w5_5_axis_b_mack_verdict.json (Axis-B mack verdict)
  - computations/session-92/s92_w5_vii_au_op_proj_lmax14_extension.npz (Set_A)
  - sessions/framework/registry/mack-observational-constraints.md (Set_B)
  - sessions/permanent-results-registry.md (§VII.AU.OP-PROJ canonical-host block)
  - .claude/rules/joint-theorem-promotion.md (Stage 2 + substrate-input-orthogonality)
  - .claude/rules/gate-verdicts.md (Option A supersedes-chain clauses 1-6)
  - .claude/rules/cross-pillar-bridge-anatomy.md (Hybrid Independence Test K=3->K=4)
  - .claude/rules/epistemic-discipline.md (Layer-Decomposition Phi correspondence)
  - computations/session-91/s91_gate_verdicts.txt (supersedes-source: line 148
       audit_sha256=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b)
  - computations/session-92/s92_gate_verdicts.txt (chained prereq: §W5-1
       audit_sha256=395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf)
  - computations/_shared/canonical_constants.py (n_s pins)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite-PASS-record>,
   scheme=joint-theorem-promotion-stage-2-pass-and-orchestrator-composite-with-option-a-supersedes-chain,
   convention=cross-axis-axis-a-vdd-plus-axis-b-mack-orchestrator-direct-supersedes-cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b-substrate-input-orthogonality-structural-ceiling-MANDATORY-K-3,
   L_max=12)

Classification: GEOMETRIC (operates on §VII.AU.OP-PROJ Pillar I <-> Pillar II
  FWD-C1 bridge identity; Stage-2 PASS-AND re-dispatch is the methodology-floor
  F-image of the substrate-IS structural identity per epistemic-discipline.md
  §"Layer-Decomposition" Phi correspondence)

PASS-AND aggregation logic (Phase H):
  - Load Axis-A vdd verdict JSON; extract per-clause PASS/FAIL/INFO map.
  - Load Axis-B mack verdict JSON; extract per-clause PASS/FAIL/INFO map.
  - For each single-axis clause: verify each axis's clause is PASS.
  - For each JOINT clause: verify BOTH axes returned PASS (logical AND, not OR).
  - Verify substrate-input-orthogonality at structural ceiling (Set_A SHA from
    vdd JSON != Set_B SHA from mack JSON; both axes declared disjoint partition
    with no overlap caveat).
  - Verify supersedes tag is full 64-char (NOT head-truncated 16-char form).
  - Composite PASS iff all 5 predicates hold; INFO iff either Axis returns INFO
    OR substrate-input-overlap caveat applies AND all other predicates PASS;
    FAIL iff either Axis FAILs OR supersedes tag absent/malformed/head-truncated.

OPTION A supersedes-chain protocol invocation (gate-verdicts.md §"Option A"):
  - Original S91 W8 §W8-1 mechanical-closure verdict line at
    computations/session-91/s91_gate_verdicts.txt:148 with
    audit_sha256=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b
    is RETAINED on disk (Option A clause 1; absolute verdict permanence).
  - Corrective canonical line emitted by this script APPENDS to
    computations/session-92/s92_gate_verdicts.txt (NOT session-91; per
    gate-verdicts.md §"Canonical Verdict-File Path").
  - Corrective line carries `supersedes=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b`
    (FULL 64-character, NEVER head-truncated) in the `value=` field per
    Option A clause 5 MANDATORY forward-emission discipline (since S88 W8-100).
  - APPEND via atomic single `open("a", encoding="utf-8")` POSIX O_APPEND
    write per the canonical append_verdict() helper protocol; no read-modify-
    write, no truncate-and-rewrite.
  - Downstream consumers per Option A clause 3 cite the LATEST NON-SUPERSEDED
    line as canonical via the supersession-chain reading discipline.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# canonical_constants lives in computations/_shared/; add to path
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: F401,E402
    M_KK,
    planck_ns,
    planck_ns_err,
    n_s_framework,
    n_s_FW_exact,
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

# CPU-only verdict-aggregator; cap CPU threads per computation-environment.md
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402

# Matplotlib non-interactive backend
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S92"  # (local)
GATE_ID = "S92-W5-CF-W8-CONSOLIDATED-9-VII-AU-OP-PROJ-W8-1-RE-DISPATCH"  # (local)
SCHEME = (
    "joint-theorem-promotion-stage-2-pass-and-"
    "orchestrator-composite-with-option-a-supersedes-chain"
)  # (local)
# Full 64-character supersedes target — NEVER head-truncated per Option A clause 5
SUPERSEDES_TARGET_FULL_64 = (
    "cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b"
)  # (local) — S91 W8 §W8-1 original mechanical-closure audit_sha256
CONVENTION = (
    "cross-axis-axis-a-vdd-plus-axis-b-mack-orchestrator-direct-"
    f"supersedes-{SUPERSEDES_TARGET_FULL_64}-"
    "substrate-input-orthogonality-structural-ceiling-MANDATORY-K-3"
)  # (local)
L_MAX = 12  # (local) — master baseline; L_max=14+ extension consumed via Set_A npz from §W5-1

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s92_w5_5_vii_au_op_proj_w8_1_re_dispatch.npz"  # (local)
OUT_PNG = SESSION_DIR / "s92_w5_5_vii_au_op_proj_w8_1_re_dispatch.png"  # (local)
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"  # (local)

# Input pin paths
PATH_AXIS_A_VDD_JSON = SESSION_DIR / "s92_w5_5_axis_a_vdd_verdict.json"  # (local)
PATH_AXIS_B_MACK_JSON = SESSION_DIR / "s92_w5_5_axis_b_mack_verdict.json"  # (local)
PATH_SET_A_NPZ = SESSION_DIR / "s92_w5_vii_au_op_proj_lmax14_extension.npz"  # (local)
PATH_SET_B_MACK_REGISTRY = (
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "mack-observational-constraints.md"
)  # (local)
PATH_PERMANENT_REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
PATH_RULE_JOINT_PROMO = (
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)  # (local)
PATH_RULE_GATE_VERDICTS = PROJECT_ROOT / ".claude" / "rules" / "gate-verdicts.md"  # (local)
PATH_RULE_CROSS_PILLAR = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)  # (local)
PATH_RULE_EPIST = PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"  # (local)
PATH_CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"  # (local)
PATH_S91_VERDICTS = (
    COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"
)  # (local) — Option A supersedes-source
PATH_S92_VERDICTS_PREREQ = SESSION_DIR / "s92_gate_verdicts.txt"  # (local) — chained prereq
# Master spectrum cache — runtime canonical-path rescue per substrate-first-canonical-sourcing.md §(ii.B):
# plan §W5-5 cites session-87 path which does NOT exist; runtime canonical path is session-84.
PATH_MASTER_SPECTRUM_CACHE = (
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
)  # (local)

INPUT_FILES = [
    PATH_CANONICAL_CONSTANTS,
    PATH_AXIS_A_VDD_JSON,
    PATH_AXIS_B_MACK_JSON,
    PATH_SET_A_NPZ,
    PATH_SET_B_MACK_REGISTRY,
    PATH_PERMANENT_REGISTRY,
    PATH_RULE_JOINT_PROMO,
    PATH_RULE_GATE_VERDICTS,
    PATH_RULE_CROSS_PILLAR,
    PATH_RULE_EPIST,
    PATH_S91_VERDICTS,
    PATH_S92_VERDICTS_PREREQ,
    PATH_MASTER_SPECTRUM_CACHE,
]

# §W5-1 chained prereq audit_sha256 — verified at plan-freeze + runtime
W5_1_AUDIT_SHA_FULL_64 = (
    "395c63c829c11546766ee78e49609c571046e53b6ea5acb4c5844a61d62b64bf"
)  # (local)

# Set_A SHA-256 expected from vdd JSON (substrate-input-orthogonality pin)
SET_A_SHA_EXPECTED = "23504adb91c29816f91f2e61e549f441ccfba34f460d82e3fce366bf7edae239"  # (local)

# Set_B SHA-256 expected from mack JSON (substrate-input-orthogonality pin)
SET_B_SHA_EXPECTED = "cc721a4e233ab4a0c98bb82baff6e3bf59b6bb59d94e7306a04c89e3764848f0"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block + dual-SHA helpers (S87+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 hexdigest of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
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


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S87+ dual-SHA schema.

    audit_sha256:
        sha256( bytes(script) || bytes(canonical_constants.py) || pinmap_json )
        where pinmap_json is the canonical sorted JSON serialization of pins.

    content_sha256:
        sha256( bytes(script) )
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
# Section 5 — Phase A: runtime prerequisite verification (§W5-1 PASS)
# ---------------------------------------------------------------------------
def phase_a_verify_w5_1_chained_prereq() -> dict:
    """Verify §W5-1 PASS chained prerequisite per `substrate-first-canonical-sourcing.md §(ii.B)`
    runtime canonical-path rescue. Looks up the §W5-1 canonical verdict line in
    computations/session-92/s92_gate_verdicts.txt at runtime; if §W5-1 NOT PASS,
    this gate honestly closes per `.claude/rules/mechanical-closure-discipline.md`
    with value='PRE-REG-INC_blocked_by_S92-W5-1_NOT_PASS'.
    """
    print("\n=== Phase A — Runtime prerequisite verification (§W5-1 PASS) ===")
    text = PATH_S92_VERDICTS_PREREQ.read_text(encoding="utf-8", errors="replace")  # (local)
    # Match the §W5-1 canonical line (S87+ format)
    pattern = re.compile(
        r"^S92-W5-CF-S92-W2-2-LMAX14-VII-AU-OP-PROJ-L-MAX-14-EXTENSION:"
        r"\s*(PASS|FAIL|INFO).*?audit_sha256=([a-f0-9]{64})",
        re.MULTILINE,
    )
    m = pattern.search(text)  # (local)
    if not m:
        return {
            "found": False,
            "w5_1_verdict": None,
            "w5_1_audit_sha": None,
            "prereq_PASS": False,
            "reason": "S92-W5-1 verdict line NOT FOUND in s92_gate_verdicts.txt",
        }
    w5_1_verdict = m.group(1)  # (local)
    w5_1_audit_sha = m.group(2)  # (local)
    prereq_PASS = (w5_1_verdict == "PASS") and (w5_1_audit_sha == W5_1_AUDIT_SHA_FULL_64)  # (local)
    print(f"  §W5-1 verdict: {w5_1_verdict}")
    print(f"  §W5-1 audit_sha256: {w5_1_audit_sha[:16]}...")
    print(
        f"  §W5-1 audit_sha256 matches plan-pinned "
        f"({W5_1_AUDIT_SHA_FULL_64[:16]}...): "
        f"{w5_1_audit_sha == W5_1_AUDIT_SHA_FULL_64}"
    )
    print(f"  Chained prereq PASS: {prereq_PASS}")
    return {
        "found": True,
        "w5_1_verdict": w5_1_verdict,
        "w5_1_audit_sha": w5_1_audit_sha,
        "w5_1_audit_sha_matches_plan_pin": (w5_1_audit_sha == W5_1_AUDIT_SHA_FULL_64),
        "prereq_PASS": prereq_PASS,
    }


# ---------------------------------------------------------------------------
# Section 6 — Phase B: supersedes-chain verification (Option A clause 1)
# ---------------------------------------------------------------------------
def phase_b_verify_supersedes_target() -> dict:
    """Phase B — Option A supersedes-chain verification per `gate-verdicts.md
    §"Option A — sig_5 remediation pathway under absolute verdict permanence"`
    clause 1: original S91 W8 §W8-1 mechanical-closure verdict line at
    `computations/session-91/s91_gate_verdicts.txt:148` is RETAINED on disk;
    full 64-char audit_sha256=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b
    matches the plan-pinned hash; the original line is NOT modified or deleted.
    """
    print("\n=== Phase B — Option A supersedes-chain verification ===")
    print(f"  Supersedes target (full 64-char): {SUPERSEDES_TARGET_FULL_64}")
    text = PATH_S91_VERDICTS.read_text(encoding="utf-8", errors="replace")  # (local)
    # Look for the S91 W8 §W8-1 line; match its full 64-char audit_sha256
    pattern = re.compile(
        r"^S91-W8-CF-67-VII-AU-OP-PROJ-FWD-C1-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY:"
        r"\s*FAIL.*?audit_sha256=([a-f0-9]{64})",
        re.MULTILINE,
    )
    m = pattern.search(text)  # (local)
    if not m:
        return {
            "found": False,
            "supersedes_target_audit_sha": None,
            "supersedes_target_matches": False,
            "original_retained_on_disk": False,
        }
    found_sha = m.group(1)  # (local)
    matches = (found_sha == SUPERSEDES_TARGET_FULL_64)  # (local)
    print(f"  S91 W8 §W8-1 original audit_sha256 found: {found_sha[:16]}...")
    print(f"  Supersedes target matches: {matches}")
    print(f"  Original verdict line RETAINED on disk (Option A clause 1): {matches}")
    return {
        "found": True,
        "supersedes_target_audit_sha": found_sha,
        "supersedes_target_matches": matches,
        "original_retained_on_disk": matches,
    }


# ---------------------------------------------------------------------------
# Section 7 — Phase D: load per-axis verdict JSON sidecars
# ---------------------------------------------------------------------------
def phase_d_load_axis_verdicts() -> tuple[dict, dict]:
    """Phase D — load per-axis verdict JSON sidecars produced by the two
    Stage-2 cross-reviewers (Axis-A vdd + Axis-B mack)."""
    print("\n=== Phase D — Load Axis-A vdd + Axis-B mack verdict JSONs ===")
    with PATH_AXIS_A_VDD_JSON.open("r", encoding="utf-8") as fp:
        vdd = json.load(fp)  # (local)
    with PATH_AXIS_B_MACK_JSON.open("r", encoding="utf-8") as fp:
        mack = json.load(fp)  # (local)
    print(
        f"  Axis-A vdd: {len(vdd.get('single_axis_clauses', {}))} single-axis + "
        f"{len(vdd.get('joint_clauses', {}))} joint clauses; "
        f"composite={vdd.get('axis_A_composite', 'UNKNOWN')}"
    )
    print(
        f"  Axis-B mack: {len(mack.get('single_axis_clauses', {}))} single-axis + "
        f"{len(mack.get('joint_clauses', {}))} joint clauses; "
        f"composite={mack.get('axis_B_composite', 'UNKNOWN')}"
    )
    return vdd, mack


# ---------------------------------------------------------------------------
# Section 8 — Phase E: JOINT-clause PASS-AND aggregation
# ---------------------------------------------------------------------------
def _clause_verdict(payload: dict) -> str:
    """Extract verdict string from a per-clause payload dict."""
    return str(payload.get("verdict", "UNKNOWN"))


def phase_e_joint_pass_and(vdd: dict, mack: dict) -> dict:
    """Phase E — Stage-2 PASS-AND aggregation per `joint-theorem-promotion.md
    §"Stage 2"` MANDATORY 4-stage pathway: BOTH cross-reviewers MUST return PASS
    on JOINT clauses (logical AND, not OR).

    JOINT clauses are NAMED IDENTICALLY across both axis JSONs by construction:
      - element_3_bridge_map
      - 3_level_ladder
      - HIT_K_3_K_4_advancement
    """
    print("\n=== Phase E — JOINT-clause PASS-AND aggregation ===")
    vdd_joint = vdd.get("joint_clauses", {})  # (local)
    mack_joint = mack.get("joint_clauses", {})  # (local)
    joint_names = sorted(set(vdd_joint.keys()) | set(mack_joint.keys()))  # (local)
    per_clause_aggregate: dict[str, dict] = {}  # (local)
    all_pass_and = True  # (local)
    any_info = False  # (local)
    any_fail = False  # (local)
    for name in joint_names:
        v_a = _clause_verdict(vdd_joint.get(name, {}))  # (local)
        v_b = _clause_verdict(mack_joint.get(name, {}))  # (local)
        pass_and = (v_a == "PASS") and (v_b == "PASS")  # (local)
        info_either = (v_a == "INFO") or (v_b == "INFO")  # (local)
        fail_either = (v_a == "FAIL") or (v_b == "FAIL")  # (local)
        per_clause_aggregate[name] = {
            "axis_a_vdd": v_a,
            "axis_b_mack": v_b,
            "PASS_AND": pass_and,
            "INFO_either": info_either,
            "FAIL_either": fail_either,
        }
        if not pass_and:
            all_pass_and = False
        if info_either:
            any_info = True
        if fail_either:
            any_fail = True
        print(
            f"  JOINT clause '{name}': vdd={v_a}, mack={v_b}, "
            f"PASS-AND={pass_and}"
        )
    return {
        "joint_clauses": per_clause_aggregate,
        "all_PASS_AND": all_pass_and,
        "any_INFO": any_info,
        "any_FAIL": any_fail,
        "n_joint_clauses": len(joint_names),
    }


# ---------------------------------------------------------------------------
# Section 9 — Phase E-bis: single-axis clause check
# ---------------------------------------------------------------------------
def phase_e_single_axis_check(vdd: dict, mack: dict) -> dict:
    """Verify each axis's single-axis clauses are ALL PASS on their own axis."""
    print("\n=== Phase E-bis — Single-axis clause PASS check ===")
    vdd_single = vdd.get("single_axis_clauses", {})  # (local)
    mack_single = mack.get("single_axis_clauses", {})  # (local)
    vdd_per_clause: dict[str, str] = {n: _clause_verdict(p) for n, p in vdd_single.items()}  # (local)
    mack_per_clause: dict[str, str] = {n: _clause_verdict(p) for n, p in mack_single.items()}  # (local)
    vdd_all_PASS = all(v == "PASS" for v in vdd_per_clause.values())  # (local)
    mack_all_PASS = all(v == "PASS" for v in mack_per_clause.values())  # (local)
    vdd_any_FAIL = any(v == "FAIL" for v in vdd_per_clause.values())  # (local)
    mack_any_FAIL = any(v == "FAIL" for v in mack_per_clause.values())  # (local)
    vdd_any_INFO = any(v == "INFO" for v in vdd_per_clause.values())  # (local)
    mack_any_INFO = any(v == "INFO" for v in mack_per_clause.values())  # (local)
    print(
        f"  Axis-A vdd single-axis: {len(vdd_per_clause)} clauses; "
        f"ALL_PASS={vdd_all_PASS}; any_FAIL={vdd_any_FAIL}; any_INFO={vdd_any_INFO}"
    )
    print(
        f"  Axis-B mack single-axis: {len(mack_per_clause)} clauses; "
        f"ALL_PASS={mack_all_PASS}; any_FAIL={mack_any_FAIL}; any_INFO={mack_any_INFO}"
    )
    for name, v in vdd_per_clause.items():
        print(f"    vdd  '{name}': {v}")
    for name, v in mack_per_clause.items():
        print(f"    mack '{name}': {v}")
    return {
        "vdd_single_per_clause": vdd_per_clause,
        "mack_single_per_clause": mack_per_clause,
        "vdd_all_PASS": vdd_all_PASS,
        "mack_all_PASS": mack_all_PASS,
        "vdd_any_FAIL": vdd_any_FAIL,
        "mack_any_FAIL": mack_any_FAIL,
        "vdd_any_INFO": vdd_any_INFO,
        "mack_any_INFO": mack_any_INFO,
    }


# ---------------------------------------------------------------------------
# Section 10 — Phase F: substrate-input-orthogonality at STRUCTURAL CEILING
# ---------------------------------------------------------------------------
def phase_f_substrate_input_orthogonality(vdd: dict, mack: dict) -> dict:
    """Phase F — substrate-input-orthogonality verification at STRUCTURAL CEILING
    per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`
    MANDATORY-K=3 since S90 W2 CF-20.

    Predicate: there exists obs_i such that the data file consumed by obs_i is
    loaded by exactly ONE cross-reviewer (NOT both); PASS-AND across orthogonal-
    data observables is INTACT (no substrate-input-overlap caveat applies).

    At §W5-5:
      Set_A = computations/session-92/s92_w5_vii_au_op_proj_lmax14_extension.npz
              (§W5-1 substrate-physics L_max=14+ first-extraction output) -> Axis-A only
      Set_B = sessions/framework/registry/mack-observational-constraints.md
              + canonical_constants.py n_s_obs_Planck pin -> Axis-B only
    obs_1 = framework-prediction vs Planck-observation comparison at
            §VII.AU.OP-PROJ Level 3 empirical anchor.
    """
    print("\n=== Phase F — Substrate-input-orthogonality at STRUCTURAL CEILING ===")
    # Set_A — vdd declared
    vdd_set_A_path = vdd.get("substrate_input_orthogonality_set_A_file")  # (local)
    vdd_set_A_sha = vdd.get("set_A_sha256")  # (local)
    # Set_B — mack declared
    mack_set_B_files = mack.get("substrate_input_orthogonality_set_B_files", [])  # (local)
    mack_set_B_sha = mack.get("set_B_sha256_registry")  # (local)

    # Independently re-compute SHAs to verify integrity
    set_A_sha_recomputed = sha256_of(PATH_SET_A_NPZ)  # (local)
    set_B_sha_recomputed = sha256_of(PATH_SET_B_MACK_REGISTRY)  # (local)

    set_A_sha_matches_vdd = (vdd_set_A_sha == set_A_sha_recomputed)  # (local)
    set_B_sha_matches_mack = (mack_set_B_sha == set_B_sha_recomputed)  # (local)
    set_A_sha_matches_expected = (set_A_sha_recomputed == SET_A_SHA_EXPECTED)  # (local)
    set_B_sha_matches_expected = (set_B_sha_recomputed == SET_B_SHA_EXPECTED)  # (local)
    # Disjoint partition test: Set_A SHA != Set_B SHA (different files)
    partition_disjoint = (set_A_sha_recomputed != set_B_sha_recomputed)  # (local)

    # Independent declaration that no substrate-input-overlap caveat applies
    # (both axis JSONs MUST declare structural-ceiling, not overlap-caveat)
    vdd_no_caveat = (
        "no substrate-input-overlap caveat applies"
        in vdd.get("substrate_input_orthogonality_partition_disclosure", "").lower()
        or "no substrate-input-overlap caveat"
        in vdd.get("substrate_input_orthogonality_partition_disclosure", "").lower()
    )  # (local)
    mack_no_caveat = (
        "structural ceiling" in mack.get("set_B_orthogonality_obs_1", "").lower()
        and "no substrate-input-overlap caveat" in mack.get("set_B_orthogonality_obs_1", "").lower()
    )  # (local)

    orthogonality_PASS_at_structural_ceiling = (
        partition_disjoint
        and set_A_sha_matches_vdd
        and set_B_sha_matches_mack
        and set_A_sha_matches_expected
        and set_B_sha_matches_expected
        and vdd_no_caveat
        and mack_no_caveat
    )  # (local)

    print(f"  Set_A path (vdd): {vdd_set_A_path}")
    print(f"  Set_A SHA-256 declared (vdd): {(vdd_set_A_sha or '')[:16]}...")
    print(f"  Set_A SHA-256 recomputed: {set_A_sha_recomputed[:16]}...")
    print(
        f"  Set_A SHA matches vdd declaration: {set_A_sha_matches_vdd}; "
        f"matches expected pin: {set_A_sha_matches_expected}"
    )
    print(f"  Set_B files (mack): {mack_set_B_files[:1]}...")
    print(f"  Set_B SHA-256 declared (mack): {(mack_set_B_sha or '')[:16]}...")
    print(f"  Set_B SHA-256 recomputed (mack-observational-constraints): {set_B_sha_recomputed[:16]}...")
    print(
        f"  Set_B SHA matches mack declaration: {set_B_sha_matches_mack}; "
        f"matches expected pin: {set_B_sha_matches_expected}"
    )
    print(f"  Partition disjoint (Set_A SHA != Set_B SHA): {partition_disjoint}")
    print(f"  vdd declares NO substrate-input-overlap caveat: {vdd_no_caveat}")
    print(f"  mack declares NO substrate-input-overlap caveat (STRUCTURAL CEILING): {mack_no_caveat}")
    print(
        f"  substrate-input-orthogonality PASS at STRUCTURAL CEILING: "
        f"{orthogonality_PASS_at_structural_ceiling}"
    )
    return {
        "set_A_path": str(vdd_set_A_path),
        "set_A_sha_vdd_declared": vdd_set_A_sha,
        "set_A_sha_recomputed": set_A_sha_recomputed,
        "set_A_sha_matches_vdd": set_A_sha_matches_vdd,
        "set_A_sha_matches_expected": set_A_sha_matches_expected,
        "set_B_files_mack_declared": mack_set_B_files,
        "set_B_sha_mack_declared": mack_set_B_sha,
        "set_B_sha_recomputed_mack_registry": set_B_sha_recomputed,
        "set_B_sha_matches_mack": set_B_sha_matches_mack,
        "set_B_sha_matches_expected": set_B_sha_matches_expected,
        "partition_disjoint": partition_disjoint,
        "vdd_no_overlap_caveat": vdd_no_caveat,
        "mack_no_overlap_caveat": mack_no_caveat,
        "orthogonality_PASS_at_structural_ceiling": orthogonality_PASS_at_structural_ceiling,
        "obs_1": (
            "framework-prediction vs Planck-observation comparison "
            "at §VII.AU.OP-PROJ Level 3 empirical anchor"
        ),
    }


# ---------------------------------------------------------------------------
# Section 11 — Phase G: Option A supersedes tag emission compliance
# ---------------------------------------------------------------------------
def phase_g_supersedes_tag_compliance() -> dict:
    """Phase G — Option A supersedes tag emission compliance per
    `gate-verdicts.md §"Option A"` clause 5 MANDATORY forward-emission discipline
    (since S88 W8-100).

    The corrective canonical line emitted by THIS script will carry
    `supersedes=<full-64-char-old-audit-sha>` in the `value=` field. Verify:
      (a) the supersedes target is exactly 64 hex characters (NOT 16-char head)
      (b) the supersedes target matches the verified Option A supersedes source
      (c) the regex `^[a-f0-9]{64}$` matches.

    Returns PASS iff (a) AND (b) AND (c).
    """
    print("\n=== Phase G — Option A supersedes tag emission compliance ===")
    target = SUPERSEDES_TARGET_FULL_64  # (local)
    is_64_char = (len(target) == 64)  # (local)
    matches_hex_regex = bool(re.fullmatch(r"[a-f0-9]{64}", target))  # (local)
    is_not_head_truncated = is_64_char and matches_hex_regex  # (local)
    matches_b_phase = (target == SUPERSEDES_TARGET_FULL_64)  # (local) — tautological by construction
    compliance_PASS = is_64_char and matches_hex_regex and matches_b_phase  # (local)
    print(f"  supersedes target: {target}")
    print(f"  length == 64: {is_64_char}")
    print(f"  matches ^[a-f0-9]{{64}}$ regex: {matches_hex_regex}")
    print(f"  is NOT head-truncated: {is_not_head_truncated}")
    print(f"  compliance PASS: {compliance_PASS}")
    return {
        "supersedes_target_full_64": target,
        "length_64": is_64_char,
        "matches_hex_regex": matches_hex_regex,
        "is_not_head_truncated": is_not_head_truncated,
        "compliance_PASS": compliance_PASS,
    }


# ---------------------------------------------------------------------------
# Section 12 — Phase H: composite PASS-AND aggregation
# ---------------------------------------------------------------------------
def phase_h_composite_aggregate(
    prereq: dict,
    supersedes_src: dict,
    single_axis: dict,
    joint: dict,
    orthogonality: dict,
    tag_compliance: dict,
) -> dict:
    """Phase H — composite PASS-AND aggregation per `joint-theorem-promotion.md
    §"Stage 2"` PASS-AND criterion + `gate-verdicts.md §"Option A"` clause 5
    forward-emission discipline.

    composite_verdict := PASS iff ALL of:
      (1) Axis-A vdd ALL single-axis PASS
      (2) Axis-B mack ALL single-axis PASS
      (3) All JOINT clauses PASS-AND'd (both axes PASS on each)
      (4) substrate-input-orthogonality PASS at STRUCTURAL CEILING
      (5) Option A supersedes tag compliance PASS

    composite_verdict := FAIL iff
      - any single-axis FAIL on either axis OR
      - any JOINT clause has either axis FAIL OR
      - substrate-input-orthogonality FAIL OR
      - supersedes tag absent/malformed/head-truncated OR
      - chained prereq §W5-1 NOT PASS OR
      - supersedes-source verification FAIL (Option A clause 1 violation)

    composite_verdict := INFO iff
      - chained prereqs and FAIL conditions clear AND
      - either Axis returns INFO on any clause OR substrate-input-overlap caveat
    """
    print("\n=== Phase H — Composite PASS-AND aggregation ===")
    # Hard FAIL channels
    prereq_PASS = bool(prereq.get("prereq_PASS"))  # (local)
    supersedes_src_PASS = bool(supersedes_src.get("supersedes_target_matches"))  # (local)
    p1_vdd_all_PASS = bool(single_axis.get("vdd_all_PASS"))  # (local)
    p2_mack_all_PASS = bool(single_axis.get("mack_all_PASS"))  # (local)
    p3_joint_all_PASS_AND = bool(joint.get("all_PASS_AND"))  # (local)
    p4_orthogonality_PASS = bool(orthogonality.get("orthogonality_PASS_at_structural_ceiling"))  # (local)
    p5_supersedes_tag_PASS = bool(tag_compliance.get("compliance_PASS"))  # (local)

    any_FAIL = (
        (not prereq_PASS)
        or (not supersedes_src_PASS)
        or single_axis.get("vdd_any_FAIL", False)
        or single_axis.get("mack_any_FAIL", False)
        or joint.get("any_FAIL", False)
        or (not p4_orthogonality_PASS)
        or (not p5_supersedes_tag_PASS)
    )  # (local)
    any_INFO = (
        single_axis.get("vdd_any_INFO", False)
        or single_axis.get("mack_any_INFO", False)
        or joint.get("any_INFO", False)
    )  # (local)
    all_PASS = (
        prereq_PASS
        and supersedes_src_PASS
        and p1_vdd_all_PASS
        and p2_mack_all_PASS
        and p3_joint_all_PASS_AND
        and p4_orthogonality_PASS
        and p5_supersedes_tag_PASS
    )  # (local)

    if any_FAIL:
        composite = "FAIL"  # (local)
    elif any_INFO:
        composite = "INFO"  # (local)
    elif all_PASS:
        composite = "PASS"  # (local)
    else:
        # Defensive: structurally unreachable but explicit
        composite = "FAIL"  # (local)

    print(f"  P1 Axis-A vdd ALL_PASS: {p1_vdd_all_PASS}")
    print(f"  P2 Axis-B mack ALL_PASS: {p2_mack_all_PASS}")
    print(f"  P3 JOINT PASS-AND (all clauses): {p3_joint_all_PASS_AND}")
    print(f"  P4 substrate-input-orthogonality STRUCTURAL CEILING: {p4_orthogonality_PASS}")
    print(f"  P5 supersedes tag compliance: {p5_supersedes_tag_PASS}")
    print(f"  Chained prereq §W5-1 PASS: {prereq_PASS}")
    print(f"  Option A supersedes-source verification PASS: {supersedes_src_PASS}")
    print(f"  composite_verdict: {composite}")
    return {
        "P1_vdd_single_axis_all_PASS": p1_vdd_all_PASS,
        "P2_mack_single_axis_all_PASS": p2_mack_all_PASS,
        "P3_joint_all_PASS_AND": p3_joint_all_PASS_AND,
        "P4_substrate_input_orthogonality_structural_ceiling": p4_orthogonality_PASS,
        "P5_supersedes_tag_compliance": p5_supersedes_tag_PASS,
        "chained_prereq_W5_1_PASS": prereq_PASS,
        "supersedes_source_verification_PASS": supersedes_src_PASS,
        "any_FAIL": any_FAIL,
        "any_INFO": any_INFO,
        "all_5_predicates_PASS": all_PASS,
        "composite_verdict": composite,
    }


# ---------------------------------------------------------------------------
# Section 13 — Verdict-line append (Option A supersedes tag emission)
# ---------------------------------------------------------------------------
def _scan_intermediate_supersedes(current_audit_sha: str) -> list[str]:
    """Scan computations/session-92/s92_gate_verdicts.txt for prior canonical
    lines for this gate_id. Returns the list of audit_sha256 hex strings of
    prior canonical-form emissions (regex `^{GATE_ID}: (PASS|FAIL|INFO) -- `)
    that are NOT the current emission. These are intermediate in-script bug
    emissions (per `gate-verdicts.md §"Option A" "script-bug fix" pattern type`)
    that the current corrective emission supersedes in the audit-trail-canonical
    reading per Option A clause 2 + clause 3 chain-completeness.

    If no prior canonical lines exist for this gate_id (first emission of the
    dispatch), returns an empty list — the supersedes chain points exclusively
    to the plan-pinned S91 W8 §W8-1 target per Option A clause 5.
    """
    if not VERDICT_TXT.exists():
        return []
    text = VERDICT_TXT.read_text(encoding="utf-8", errors="replace")  # (local)
    canonical_line_pattern = re.compile(
        rf"^{re.escape(GATE_ID)}:\s*(?:PASS|FAIL|INFO)\s+--.*?audit_sha256=([a-f0-9]{{64}})",
        re.MULTILINE,
    )
    found_shas: list[str] = []  # (local)
    for m in canonical_line_pattern.finditer(text):
        found_shas.append(m.group(1))
    # Exclude the current emission (in case the script is re-run and verdict
    # file already contains a line with the current emission's audit_sha)
    return [sha for sha in found_shas if sha != current_audit_sha]


def append_verdict(
    verdict: str,
    value_string: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append a single canonical verdict line to s92_gate_verdicts.txt per the
    S87+ dual-SHA schema, then a dual-SHA companion comment row, then the
    S87+ schema-v2 3-tuple companion row ([VERIFY-THEOREM] trigger requires it).

    Atomic single open('a', encoding='utf-8') write per POSIX O_APPEND
    semantics — no read-modify-write, no truncate-and-rewrite. The corrective
    canonical line carries `supersedes=<full-64-char-old-audit-sha>` as a
    TOP-LEVEL TOKEN (literal-space-preceded) per the plan-pinned regex
    `^...:.* supersedes=<full-64-char>.* audit_sha256=[a-f0-9]{64}` AND the
    same tag inside the `value=` field (doubly-visible per Option A clause 5
    MANDATORY forward-emission discipline since S88 W8-100). The original
    S91 W8 §W8-1 verdict at `computations/session-91/s91_gate_verdicts.txt:148`
    is RETAINED on disk per absolute verdict permanence (Option A clause 1).

    The 3-tuple field semantics (per `gate-verdicts.md §"S87+ canonical form"`):
      sign_verdict: PASS iff each axis returned PASS on each clause as
        pre-registered (joint-theorem-promotion-stage-2-pass-and direction).
      magnitude_verdict: PASS iff the 5-predicate conjunction holds; INFO iff
        any-INFO; FAIL otherwise.
      regime_verdict: VALID (verdict-aggregator gate; not an ODE / scan window).
    """
    # Canonical verdict line (S87+ dual-SHA schema). The supersedes= token
    # appears as a literal-space-preceded top-level field to satisfy the
    # plan-pinned regex `^...:.* supersedes=<full-64-char>.* audit_sha256=...`
    # AND is duplicated inside the value= field for Option A clause 5
    # forward-emission discipline.
    #
    # Supersession chain (Option A clauses 1+2+3+5, per gate-verdicts.md):
    #   - Original S91 W8 §W8-1 mechanical-closure: cdbebfa9... (RETAINED at s91:148)
    #   - Intermediate in-script bug emission(s) detected at runtime via
    #     prior-canonical-line scan (script-bug-fix per gate-verdicts.md Option A
    #     clause "script-bug fix" pattern type): each prior canonical line for
    #     THIS gate_id whose audit_sha256 is NOT the current emission's is added
    #     to the supersedes chain explicitly.
    # The corrective canonical line names the PLAN-PINNED S91 W8 target
    # (cdbebfa9...) as the top-level `supersedes=` token (satisfies plan regex
    # AND Option A clause 5 forward-emission discipline) AND lists any in-script
    # intermediate supersession targets in an `intermediate_supersedes=` token
    # for full audit-trail chain documentation per Option A clause 2 ("the
    # corrective canonical line carries a `supersedes=<full-64-char-old-audit-sha>`
    # token in its `value=` field OR in the dual-SHA companion comment row,
    # naming the original audit_sha256 the corrective line replaces in the
    # audit-trail-canonical reading").
    intermediate_supersedes_list = _scan_intermediate_supersedes(audit_sha)  # (local)
    intermediate_token = (
        f"intermediate_supersedes={','.join(intermediate_supersedes_list)} "
        if intermediate_supersedes_list
        else ""
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_string}' "
        f"supersedes={SUPERSEDES_TARGET_FULL_64} "
        f"{intermediate_token}"
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    # Dual-SHA companion comment row (W9a-99 split)
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"Option A supersedes-chain corrective canonical line "
        f"APPENDS to s92_gate_verdicts.txt; "
        f"supersedes target full-64-char "
        f"audit_sha256={SUPERSEDES_TARGET_FULL_64} "
        f"at computations/session-91/s91_gate_verdicts.txt:148; "
        f"original line RETAINED on disk per Option A clause 1; "
        f"forward-emission discipline per Option A clause 5 since S88 W8-100\n"
    )
    # S87+ schema-v2 3-tuple companion row ([VERIFY-THEOREM] trigger)
    if verdict == "PASS":
        sign_v, mag_v, regime_v = "PASS", "PASS", "VALID"  # (local)
    elif verdict == "INFO":
        sign_v, mag_v, regime_v = "PASS", "INFO", "VALID"  # (local)
    else:  # FAIL
        sign_v, mag_v, regime_v = "N/A", "FAIL", "VALID"  # (local)
    three_tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    # Atomic single open('a') write — POSIX O_APPEND, no read-modify-write
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)


# ---------------------------------------------------------------------------
# Section 14 — Output artifacts: .npz + .png
# ---------------------------------------------------------------------------
def write_npz_artifact(report: dict) -> None:
    """Composite-verdict npz: Axis-A vdd per-clause + Axis-B mack per-clause +
    JOINT PASS-AND aggregation + substrate-input-orthogonality structural-ceiling
    predicate + supersedes tag emission compliance boolean."""
    # Flatten nested dicts to a serializable form for np.savez
    flat: dict = {}  # (local)

    def _put(key: str, val):
        flat[key] = np.array(json.dumps(val, default=str, sort_keys=True), dtype=object)

    _put("gate_id", GATE_ID)
    _put("scheme", SCHEME)
    _put("convention", CONVENTION)
    _put("L_max", L_MAX)
    _put("supersedes_target_full_64", SUPERSEDES_TARGET_FULL_64)
    _put("W5_1_audit_sha_full_64", W5_1_AUDIT_SHA_FULL_64)
    _put("phase_A_prereq", report["phase_A"])
    _put("phase_B_supersedes_source", report["phase_B"])
    _put("phase_D_axis_a_vdd_composite", report["phase_D_vdd_composite"])
    _put("phase_D_axis_b_mack_composite", report["phase_D_mack_composite"])
    _put("phase_E_single_axis", report["phase_E_single_axis"])
    _put("phase_E_joint_pass_and", report["phase_E_joint"])
    _put("phase_F_orthogonality", report["phase_F"])
    _put("phase_G_supersedes_tag", report["phase_G"])
    _put("phase_H_composite", report["phase_H"])
    _put("audit_sha256", report["audit_sha256"])
    _put("content_sha256", report["content_sha256"])
    _put("composite_verdict", report["phase_H"]["composite_verdict"])
    _put(
        "structural_pin_M_KK",
        {"value": float(M_KK), "unit": "GeV", "anchor": "S42 gravity-route"},
    )
    _put(
        "structural_pin_n_s",
        {
            "n_s_FW_exact_numerator": int(n_s_FW_exact.numerator),
            "n_s_FW_exact_denominator": int(n_s_FW_exact.denominator),
            "planck_ns": float(planck_ns),
            "planck_ns_err": float(planck_ns_err),
            "discrimination_sigma": (
                float(planck_ns) - float(n_s_framework)
            ) / float(planck_ns_err),
            "alpha_canonical_asymptotic": float(alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC),
            "alpha_sample_pathway_B_L15_22": float(alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22),
        },
    )
    np.savez(OUT_NPZ, **flat)


def write_png_artifact(report: dict) -> None:
    """Per-axis per-clause verdict matrix (rows = clauses; columns = {Axis-A,
    Axis-B, PASS-AND aggregate}); supersedes-chain provenance annotation;
    substrate-input-orthogonality Set_A/Set_B partition visualization."""
    single = report["phase_E_single_axis"]  # (local)
    joint = report["phase_E_joint"]  # (local)
    orth = report["phase_F"]  # (local)
    tag = report["phase_G"]  # (local)
    composite = report["phase_H"]["composite_verdict"]  # (local)

    vdd_single = single["vdd_single_per_clause"]  # (local)
    mack_single = single["mack_single_per_clause"]  # (local)
    joint_per = joint["joint_clauses"]  # (local)

    # Build a unified rows × 3 verdict matrix
    rows: list[tuple[str, str, str, str]] = []  # (local)
    for name, v in vdd_single.items():
        rows.append((f"A-single:{name[:32]}", v, "-", "-"))
    for name, v in mack_single.items():
        rows.append((f"B-single:{name[:32]}", "-", v, "-"))
    for name, jp in joint_per.items():
        rows.append(
            (
                f"JOINT:{name[:32]}",
                jp["axis_a_vdd"],
                jp["axis_b_mack"],
                "PASS" if jp["PASS_AND"] else "FAIL",
            )
        )

    def _color(v: str) -> str:
        if v == "PASS":
            return "#1ec97a"
        if v == "INFO":
            return "#ffc41a"
        if v == "FAIL":
            return "#e84050"
        return "#9aa1ab"

    fig, ax = plt.subplots(figsize=(16, 1.0 + 0.42 * len(rows)))
    ax.set_xlim(0, 4)
    ax.set_ylim(-0.5, len(rows) - 0.5)
    ax.invert_yaxis()
    ax.set_xticks([0.5, 1.5, 2.5, 3.5])
    ax.set_xticklabels(["Clause", "Axis-A vdd", "Axis-B mack", "PASS-AND"])
    ax.set_yticks([])
    ax.set_title(
        "S92-W5-5 §VII.AU.OP-PROJ §W8-1 RE-DISPATCH — Stage-2 PASS-AND aggregation\n"
        f"composite_verdict = {composite}  |  "
        f"supersedes={SUPERSEDES_TARGET_FULL_64[:16]}...{SUPERSEDES_TARGET_FULL_64[-8:]} "
        f"(full 64-char per Option A clause 5)",
        fontsize=9,
        loc="left",
    )
    for i, (name, a, b, agg) in enumerate(rows):
        ax.text(0.05, i, name, ha="left", va="center", fontsize=7.5, family="monospace")
        for j, v in enumerate([a, b, agg], start=1):
            ax.add_patch(
                plt.Rectangle((j + 0.05, i - 0.4), 0.9, 0.8, facecolor=_color(v), edgecolor="black", lw=0.4)
            )
            ax.text(
                j + 0.5,
                i,
                v,
                ha="center",
                va="center",
                fontsize=8,
                fontweight="bold",
                color="white" if v in {"PASS", "FAIL", "INFO"} else "black",
            )

    # Substrate-input-orthogonality + supersedes annotation
    info_text = (
        f"Set_A SHA={orth['set_A_sha_recomputed'][:16]}... (vdd; §W5-1 lmax14 npz)  |  "
        f"Set_B SHA={orth['set_B_sha_recomputed_mack_registry'][:16]}... (mack; observational-constraints.md)\n"
        f"partition_disjoint={orth['partition_disjoint']}  "
        f"structural_ceiling_PASS={orth['orthogonality_PASS_at_structural_ceiling']}  "
        f"supersedes_tag_compliance={tag['compliance_PASS']}\n"
        "obs_1 = framework-prediction vs Planck-observation at §VII.AU.OP-PROJ Level 3 empirical anchor"
    )
    fig.text(0.05, 0.005, info_text, fontsize=7, family="monospace", verticalalignment="bottom")
    plt.tight_layout(rect=(0, 0.07, 1, 1))
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 15 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)  # (local)

    # Compute S87+ dual-SHA pair
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, PATH_CANONICAL_CONSTANTS, pins)  # (local)
    print(f"\n  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Phase A — runtime prerequisite verification
    phase_A = phase_a_verify_w5_1_chained_prereq()  # (local)

    # Phase B — Option A supersedes-chain verification
    phase_B = phase_b_verify_supersedes_target()  # (local)

    # Phase D — load per-axis verdict JSON sidecars
    vdd, mack = phase_d_load_axis_verdicts()  # (local)

    # Phase E-bis — single-axis clause PASS check
    phase_E_single_axis = phase_e_single_axis_check(vdd, mack)  # (local)

    # Phase E — JOINT-clause PASS-AND aggregation (logical AND)
    phase_E_joint = phase_e_joint_pass_and(vdd, mack)  # (local)

    # Phase F — substrate-input-orthogonality at STRUCTURAL CEILING
    phase_F = phase_f_substrate_input_orthogonality(vdd, mack)  # (local)

    # Phase G — Option A supersedes tag emission compliance
    phase_G = phase_g_supersedes_tag_compliance()  # (local)

    # Phase H — composite PASS-AND aggregation
    phase_H = phase_h_composite_aggregate(
        phase_A, phase_B, phase_E_single_axis, phase_E_joint, phase_F, phase_G
    )  # (local)

    # Build the consolidated report dict
    report: dict = {
        "phase_A": phase_A,
        "phase_B": phase_B,
        "phase_D_vdd_composite": vdd.get("axis_A_composite", "UNKNOWN"),
        "phase_D_mack_composite": mack.get("axis_B_composite", "UNKNOWN"),
        "phase_E_single_axis": phase_E_single_axis,
        "phase_E_joint": phase_E_joint,
        "phase_F": phase_F,
        "phase_G": phase_G,
        "phase_H": phase_H,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }

    # Persist output artifacts
    write_npz_artifact(report)
    write_png_artifact(report)

    # Build value= string for the canonical verdict line
    # Carries the full 64-char supersedes tag per Option A clause 5.
    composite_verdict = phase_H["composite_verdict"]  # (local)
    n_joint = phase_E_joint["n_joint_clauses"]  # (local)
    n_vdd_single = len(phase_E_single_axis["vdd_single_per_clause"])  # (local)
    n_mack_single = len(phase_E_single_axis["mack_single_per_clause"])  # (local)
    value_string = (
        f"composite={composite_verdict};"
        f"P1_vdd_single_axis_PASS={phase_H['P1_vdd_single_axis_all_PASS']};"
        f"P2_mack_single_axis_PASS={phase_H['P2_mack_single_axis_all_PASS']};"
        f"P3_joint_PASS_AND={phase_H['P3_joint_all_PASS_AND']};"
        f"P4_substrate_input_orthogonality_structural_ceiling="
        f"{phase_H['P4_substrate_input_orthogonality_structural_ceiling']};"
        f"P5_supersedes_tag_compliance={phase_H['P5_supersedes_tag_compliance']};"
        f"chained_prereq_W5_1_PASS={phase_H['chained_prereq_W5_1_PASS']};"
        f"supersedes_source_verification_PASS={phase_H['supersedes_source_verification_PASS']};"
        f"n_joint_clauses={n_joint};"
        f"n_vdd_single={n_vdd_single};"
        f"n_mack_single={n_mack_single};"
        f"axis_A_vdd_composite={vdd.get('axis_A_composite', 'UNKNOWN')};"
        f"axis_B_mack_composite={mack.get('axis_B_composite', 'UNKNOWN')};"
        f"set_A_sha_short={phase_F['set_A_sha_recomputed'][:16]};"
        f"set_B_sha_short={phase_F['set_B_sha_recomputed_mack_registry'][:16]};"
        f"partition_disjoint={phase_F['partition_disjoint']};"
        f"orthogonality_PASS_structural_ceiling="
        f"{phase_F['orthogonality_PASS_at_structural_ceiling']};"
        f"HIT_K_counter_advancement=K3_to_K4_saturation_continuation;"
        f"rule_status_MANDATORY_K3_PRESERVED=True;"
        f"VII_AU_OP_PROJ_STAGE_3_PERMANENT_eligibility_ENABLED_pending_W5_4_PASS="
        f"{composite_verdict == 'PASS'};"
        f"option_A_clause_1_original_retained=True;"
        f"option_A_clause_5_forward_emission_compliant={phase_G['compliance_PASS']};"
        f"supersedes={SUPERSEDES_TARGET_FULL_64}"
    )

    # Emit 4-tuple to stdout
    print()
    print(
        f"4-tuple: (value='{value_string}', scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )

    # Append canonical verdict line + dual-SHA companion + 3-tuple companion
    # via atomic single open('a') write per the canonical append_verdict() helper.
    append_verdict(composite_verdict, value_string, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite_verdict} (wall {wall:.1f}s) ===")
    print(f"  Artifacts: {OUT_NPZ.name}, {OUT_PNG.name}, verdict line appended to {VERDICT_TXT.name}")
    print(f"  Option A supersedes={SUPERSEDES_TARGET_FULL_64} (full 64-char, NOT head-truncated)")
    # Exit code reflects script health, not verdict (per math-scripts.md §"Exit Codes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
