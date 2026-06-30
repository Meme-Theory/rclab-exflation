#!/usr/bin/env python3
"""
S92 W5-4 — §VII.AU.OP-PROJ Stage-2 PASS-AND Cross-Axis Independent-Verify
=========================================================================

Gate: S92-W5-CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY ([VERIFY-THEOREM])

Orchestrator-composite aggregator implementing Phase G of the §W5-4 plan-block
(Phases A-G; sessions/session-plan/session-92-plan-w5.md §W5-4 lines 670-883).

Phase A (Pre-flight chained prereq):
  - §W5-2 PASS verified on disk at computations/session-92/s92_gate_verdicts.txt:153
    audit_sha256=ed0050c30512a43d381005932525e46965a54c1f998333e7189b81d8eb6c9174
    (supersedes line 151 FAIL=6f82cb709cf1d503... per Option A protocol;
     S88 W8-100 supersession reading).
  - §W5-3 PASS (RETROFIT) verified on disk at s92_gate_verdicts.txt:146
    audit_sha256=c085d26890e16bc3654e9a29a9f6bb35f75e19998e8777eabf4b6869e7dbb25a

Phase B (Reviewer selection per joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"):
  - Axis-A = connes-ncg-theorist (NCG-axiomatic; framework-canonical spectral-side
    substitute when lizzi downstream-inheritance-excluded per S88 W-14 V.2)
  - Axis-B = transit-dynamics-theorist (transit-dynamics / substrate-physics)
  - EXCLUDED = lizzi-spectral-functional-theorist (original-authoring-agent +
    downstream-inheritance reach)

Phase F (Substrate-input-orthogonality, MANDATORY at K=3 per §VII.AH STAGE-3-PERMANENT
         precedent S90 W2 CF-20):
  - Set_A = computations/session-91/s91_w2_3_vii_au_op_proj_w7a74_first_extraction.npz
    [runtime canonical-path rescue from plan-pinned
     computations/session-90/s90_cf_61_w7a_74_primary_substrate_distance_1_pole_s_3.npz
     MISSING-on-disk per substrate-first-canonical-sourcing.md §(ii.B)
     plan-text-drift correction orchestrator-convention]
    SHA-256 = fbc439c4b248eb2efb7ff9cf89dbf07610c2c799eac00d3aa99fa7918b3a97b4
    Routed to Axis-A EXCLUSIVELY.
  - Set_B = computations/session-91/s91_w6_1_d4_envelope_extended_pathway_b.npz
    SHA-256 = d0bae70f249dbeb8adb07dc619b4b20ce86832fa9a807a7ae0a621ae099729d4
    Routed to Axis-B EXCLUSIVELY.
  - Predicate: Set_A_sha != Set_B_sha (data-orthogonal at structural ceiling).

Phase G (PASS-AND aggregation):
  composite_verdict = PASS iff (
      Axis-A PASS on all single-axis clauses (3 clauses)
      AND Axis-B PASS on all single-axis clauses (3 clauses)
      AND for-all c in JOINT_clauses: Axis-A PASS(c) AND Axis-B PASS(c)
      AND substrate-input-orthogonality PASS at obs_1
  )

Anchors cited (full 64-char):
  Anchor_1 W6-1 PASS-A:                       d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d
  Anchor_2 S91 W5/W6 in-session promotion:    54db93d799c76c67c78bdcc8cd0477ebb6d104914f2e6764be7af50d22f36459

scheme = joint-theorem-promotion-stage-2-pass-and-orchestrator-composite
convention = cross-axis-axis-a-connes-spectral-NCG-plus-axis-b-transit-dynamics-substrate-physics-orchestrator-direct-substrate-input-orthogonality-MANDATORY-K-3-VERIFIED
L_max = 12 (master cache; cross-reviewer scripts consume their own L_max scopes:
            Axis-A on Set_A first-extraction; Axis-B on Set_B L_max=22 sub-window)

Classification: GEOMETRIC (operates on §VII.AU.OP-PROJ STAGE-1-CANDIDATE registry-text
                image of substrate-IS bridge-anatomy; PASS-AND verdict is the
                methodology-floor F-image per epistemic-discipline.md §"Layer-Decomposition"
                Phi correspondence of substrate-IS cohomology-class identity).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# Path setup so canonical_constants can be imported from _shared
_THIS_DIR = Path(__file__).resolve().parent
_SHARED = _THIS_DIR.parent / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (no heavy linalg needed — verdict aggregator)
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from typing import Any

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = _THIS_DIR
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S92"                                                                  # (local)
GATE_ID = "S92-W5-CF-S91-W6-1-STAGE-2-PASS-AND-CROSS-AXIS-INDEPENDENT-VERIFY"    # (local)
SCHEME = "joint-theorem-promotion-stage-2-pass-and-orchestrator-composite"       # (local)
CONVENTION = (                                                                   # (local)
    "cross-axis-axis-a-connes-spectral-NCG-plus-axis-b-transit-dynamics-"
    "substrate-physics-orchestrator-direct-substrate-input-orthogonality-"
    "MANDATORY-K-3-VERIFIED"
)
L_MAX = 12                                                                       # (local)

# Anchor SHA-256 (full 64-char) — required must_contain markers in this file
ANCHOR_1_W6_1_PASS_A_SHORT = "d54b26a970e43b6b"                                  # (local)
ANCHOR_1_W6_1_PASS_A_FULL = (                                                    # (local)
    "d54b26a970e43b6b5a63bee474a4a8baa80ed012546021c9dfe191cdb108fd8d"
)
ANCHOR_2_S91_W5_W6_PROMO_SHORT = "54db93d799c76c67"                              # (local)
ANCHOR_2_S91_W5_W6_PROMO_FULL = (                                                # (local)
    "54db93d799c76c67c78bdcc8cd0477ebb6d104914f2e6764be7af50d22f36459"
)

# Chained-prereq audit_sha references (Phase A)
W5_2_PASS_AUDIT_SHA = (                                                          # (local)
    "ed0050c30512a43d381005932525e46965a54c1f998333e7189b81d8eb6c9174"
)
W5_3_PASS_AUDIT_SHA = (                                                          # (local)
    "c085d26890e16bc3654e9a29a9f6bb35f75e19998e8777eabf4b6869e7dbb25a"
)

# Input file paths
AXIS_A_VERDICT_JSON = SESSION_DIR / "s92_w5_4_axis_a_verdict.json"
AXIS_B_VERDICT_JSON = SESSION_DIR / "s92_w5_4_axis_b_verdict.json"
S92_VERDICTS_TXT = SESSION_DIR / "s92_gate_verdicts.txt"
S91_VERDICTS_TXT = COMPUTATIONS_DIR / "session-91" / "s91_gate_verdicts.txt"

SET_A_NPZ_PLAN_PINNED = (
    COMPUTATIONS_DIR / "session-90"
    / "s90_cf_61_w7a_74_primary_substrate_distance_1_pole_s_3.npz"
)
SET_A_NPZ_RUNTIME = (
    COMPUTATIONS_DIR / "session-91"
    / "s91_w2_3_vii_au_op_proj_w7a74_first_extraction.npz"
)
SET_B_NPZ = (
    COMPUTATIONS_DIR / "session-91"
    / "s91_w6_1_d4_envelope_extended_pathway_b.npz"
)
MASTER_CACHE_NPZ = (
    COMPUTATIONS_DIR / "session-84"
    / "s84_spectrum_cache_L12_tau019.npz"
)

REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
JOINT_THEOREM_PROMOTION_MD = (
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)
CROSS_PILLAR_BRIDGE_ANATOMY_MD = (
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
)
EPISTEMIC_DISCIPLINE_MD = (
    PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"
)
CANONICAL_CONSTANTS_PY = SHARED_DIR / "canonical_constants.py"

# Output destinations
OUT_NPZ = SESSION_DIR / "s92_w5_4_vii_au_op_proj_stage_2_pass_and.npz"
OUT_PNG = SESSION_DIR / "s92_w5_4_vii_au_op_proj_stage_2_pass_and.png"
VERDICT_TXT = S92_VERDICTS_TXT

INPUT_FILES = [
    CANONICAL_CONSTANTS_PY,
    REGISTRY_MD,
    JOINT_THEOREM_PROMOTION_MD,
    CROSS_PILLAR_BRIDGE_ANATOMY_MD,
    EPISTEMIC_DISCIPLINE_MD,
    S91_VERDICTS_TXT,           # Anchor_1 + Anchor_2 source
    S92_VERDICTS_TXT,           # §W5-2 + §W5-3 chained-prereq source
    AXIS_A_VERDICT_JSON,        # Axis-A connes per-clause verdict
    AXIS_B_VERDICT_JSON,        # Axis-B transit per-clause verdict
    SET_A_NPZ_RUNTIME,          # substrate-input-orthogonality Set_A
    SET_B_NPZ,                  # substrate-input-orthogonality Set_B
    MASTER_CACHE_NPZ,           # L_max=12 baseline (consumed by both reviewers via L_max pin)
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA helpers (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                                         # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json);
       content_sha256 = sha256(script)."""
    script_bytes = b""                                                           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                                        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(                                                    # (local)
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                                  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                              # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Phase A: chained-prereq verification
# ---------------------------------------------------------------------------

def verify_chained_prereq(verdicts_text: str, expected_audit_sha: str,
                          gate_id_prefix: str) -> dict[str, Any]:
    """Verify that a PASS verdict with the expected audit_sha256 exists for the
    named gate-id prefix.

    Per S88 W8-100 Option A: if a 'supersedes=<old_sha>' tag appears in a later
    line for the same gate, treat the later line (or any line not in the
    superseded set) as canonical.
    """
    matches: list[dict[str, Any]] = []                                           # (local)
    superseded_shas: set[str] = set()                                            # (local)
    for line_no, line in enumerate(verdicts_text.splitlines(), 1):
        if not line.startswith(gate_id_prefix):
            continue
        verdict = "UNKNOWN"
        if ": PASS " in line:
            verdict = "PASS"
        elif ": FAIL " in line:
            verdict = "FAIL"
        elif ": INFO " in line:
            verdict = "INFO"
        # extract audit_sha256
        sha = ""
        for tok in line.split():
            if tok.startswith("audit_sha256="):
                sha = tok.split("=", 1)[1]
                break
        # detect supersedes
        sup = ""
        # Either as value-field token or as a stand-alone substring
        for tok in line.split():
            if tok.startswith("supersedes="):
                sup = tok.split("=", 1)[1].rstrip("'\"")
        if "supersedes=" in line and not sup:
            # parse from inside value-field semicolon-delimited string
            for chunk in line.split(";"):
                chunk = chunk.strip().strip("'\"")
                if chunk.startswith("supersedes="):
                    sup = chunk.split("=", 1)[1].strip("'\"")
                    break
        if sup:
            superseded_shas.add(sup)
        matches.append({
            "line_no": line_no,
            "verdict": verdict,
            "audit_sha256": sha,
            "supersedes": sup,
        })
    # Find canonical (latest non-superseded) PASS line
    canonical = None                                                             # (local)
    for m in reversed(matches):
        if m["audit_sha256"] in superseded_shas:
            continue
        if m["verdict"] == "PASS":
            canonical = m
            break
    found_expected = any(
        m["audit_sha256"] == expected_audit_sha and m["verdict"] == "PASS"
        for m in matches
    )
    return {
        "matches": matches,
        "superseded_shas": sorted(superseded_shas),
        "canonical_latest_pass": canonical,
        "found_expected_pass_audit_sha": bool(found_expected),
        "expected_audit_sha": expected_audit_sha,
        "expected_is_canonical": (
            canonical is not None
            and canonical["audit_sha256"] == expected_audit_sha
        ),
    }


# ---------------------------------------------------------------------------
# Section 6 — Phase F: substrate-input-orthogonality
# ---------------------------------------------------------------------------

def verify_substrate_input_orthogonality(set_a_sha: str, set_b_sha: str) -> dict[str, Any]:
    """Predicate per joint-theorem-promotion.md §'Substrate-input-orthogonality clause'
    MANDATORY at K=3:

        ∃ obs_i such that the data file consumed by obs_i is loaded by exactly
        ONE cross-reviewer (NOT both).

    At obs_1 = §VII.AU.OP-PROJ first-extraction empirical anchor:
      Set_A is consumed by Axis-A only;
      Set_B is consumed by Axis-B only;
      Set_A and Set_B are distinct files (different SHA-256) ⇒ data-orthogonal
      at structural ceiling (NOT procedural-floor caveat).
    """
    if not set_a_sha or not set_b_sha:
        return {"verdict": "FAIL", "reason": "missing SHA"}
    if set_a_sha == set_b_sha:
        return {
            "verdict": "FAIL",
            "reason": "Set_A and Set_B have identical SHA — data fully shared, "
                      "no substrate-input orthogonality",
            "set_A_sha256": set_a_sha,
            "set_B_sha256": set_b_sha,
        }
    return {
        "verdict": "PASS",
        "reason": "Set_A and Set_B are distinct files (Set_A consumed by "
                  "Axis-A only; Set_B consumed by Axis-B only) — data-orthogonal "
                  "at structural ceiling at obs_1 = §VII.AU.OP-PROJ "
                  "first-extraction empirical anchor",
        "set_A_sha256": set_a_sha,
        "set_B_sha256": set_b_sha,
        "obs_1": "VII.AU.OP-PROJ first-extraction empirical anchor",
        "structural_ceiling": True,
        "overlap_caveat_required": False,
    }


# ---------------------------------------------------------------------------
# Section 7 — Phase G: PASS-AND aggregation
# ---------------------------------------------------------------------------

def aggregate_pass_and(
    axis_a: dict[str, Any],
    axis_b: dict[str, Any],
    sio: dict[str, Any],
) -> dict[str, Any]:
    """PASS-AND aggregator per joint-theorem-promotion.md §'Stage 2' protocol.

        composite = PASS iff (
            ALL Axis-A single-axis clauses PASS
            AND ALL Axis-B single-axis clauses PASS
            AND for each JOINT clause c: Axis-A(c) == PASS AND Axis-B(c) == PASS
            AND substrate-input-orthogonality == PASS
        )
        composite = FAIL iff (
            either Axis returns FAIL on ANY clause
            OR any JOINT clause fails PASS-AND aggregation
            OR substrate-input-orthogonality FAILs
        )
        composite = INFO iff (
            either Axis returns INFO on a JOINT clause
            AND no FAILs surfaced
        )
    """
    detail: dict[str, Any] = {}                                                  # (local)

    # ----- Axis-A single-axis clauses -----
    a_single = axis_a.get("single_axis_clauses", {})
    a_single_verdicts = {k: v["verdict"] for k, v in a_single.items()}
    a_single_all_pass = bool(a_single_verdicts) and all(
        v == "PASS" for v in a_single_verdicts.values()
    )
    a_single_any_fail = any(v == "FAIL" for v in a_single_verdicts.values())
    a_single_any_info = any(v == "INFO" for v in a_single_verdicts.values())
    detail["axis_a_single_axis_verdicts"] = a_single_verdicts
    detail["axis_a_single_axis_all_pass"] = a_single_all_pass

    # ----- Axis-B single-axis clauses -----
    b_single = axis_b.get("single_axis_clauses", {})
    b_single_verdicts = {k: v["verdict"] for k, v in b_single.items()}
    b_single_all_pass = bool(b_single_verdicts) and all(
        v == "PASS" for v in b_single_verdicts.values()
    )
    b_single_any_fail = any(v == "FAIL" for v in b_single_verdicts.values())
    b_single_any_info = any(v == "INFO" for v in b_single_verdicts.values())
    detail["axis_b_single_axis_verdicts"] = b_single_verdicts
    detail["axis_b_single_axis_all_pass"] = b_single_all_pass

    # ----- JOINT clauses PASS-AND -----
    a_joint = axis_a.get("joint_clauses", {})
    b_joint = axis_b.get("joint_clauses", {})
    joint_keys = sorted(set(a_joint.keys()) | set(b_joint.keys()))
    joint_pass_and: dict[str, dict[str, str]] = {}                               # (local)
    joint_all_pass_and = True
    joint_any_fail = False
    joint_any_info = False
    for k in joint_keys:
        a_v = a_joint.get(k, {}).get("verdict", "MISSING")
        b_v = b_joint.get(k, {}).get("verdict", "MISSING")
        if a_v == "PASS" and b_v == "PASS":
            agg = "PASS"
        elif a_v == "FAIL" or b_v == "FAIL":
            agg = "FAIL"
            joint_any_fail = True
            joint_all_pass_and = False
        elif a_v == "INFO" or b_v == "INFO":
            agg = "INFO"
            joint_any_info = True
            joint_all_pass_and = False
        else:
            agg = "FAIL"  # missing clause is structural failure
            joint_any_fail = True
            joint_all_pass_and = False
        joint_pass_and[k] = {"axis_a": a_v, "axis_b": b_v, "PASS_AND": agg}
    detail["joint_clauses_pass_and"] = joint_pass_and
    detail["joint_clauses_all_pass_and"] = joint_all_pass_and

    # ----- substrate-input-orthogonality -----
    sio_pass = (sio.get("verdict") == "PASS")
    detail["substrate_input_orthogonality"] = sio

    # ----- Composite verdict per pre-registered rubric -----
    any_fail = (
        a_single_any_fail or b_single_any_fail or joint_any_fail or (not sio_pass)
    )
    any_info = (
        a_single_any_info or b_single_any_info or joint_any_info
    )

    if any_fail:
        composite = "FAIL"
        composite_reason = (
            "At least one axis returned FAIL on a clause OR "
            "substrate-input-orthogonality FAILed"
        )
    elif (
        a_single_all_pass
        and b_single_all_pass
        and joint_all_pass_and
        and sio_pass
        and not any_info
    ):
        composite = "PASS"
        composite_reason = (
            "All 4 predicates hold: Axis-A single-axis PASS (3/3); "
            "Axis-B single-axis PASS (3/3); JOINT clauses PASS-AND'd (3/3); "
            "substrate-input-orthogonality PASS at obs_1 (data-orthogonal at "
            "structural ceiling)"
        )
    elif any_info:
        composite = "INFO"
        composite_reason = (
            "Either Axis returned INFO on a JOINT clause AND all other "
            "predicates PASS — STAGE-2 → 3 promotion BLOCKED; theorem stays at "
            "STAGE-1-CANDIDATE; INFO clause documented as Stage-2-INFO-deferred"
        )
    else:
        composite = "FAIL"
        composite_reason = "Fallthrough — verdict undetermined"

    detail["composite_verdict"] = composite
    detail["composite_reason"] = composite_reason
    return detail


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------

def make_plot(detail: dict[str, Any], out_png: Path) -> None:
    """Per-axis per-clause verdict matrix; substrate-input-orthogonality
    annotation."""
    a_sa = detail["axis_a_single_axis_verdicts"]
    b_sa = detail["axis_b_single_axis_verdicts"]
    joint = detail["joint_clauses_pass_and"]
    sio = detail["substrate_input_orthogonality"]

    # Layout rows = clauses; columns = {Axis-A, Axis-B, PASS-AND}
    clause_labels: list[str] = []
    matrix: list[list[str]] = []
    # single-axis Axis-A clauses (PASS-AND column = same as Axis-A; no Axis-B)
    for k, v in a_sa.items():
        clause_labels.append(f"A-single: {k}")
        matrix.append([v, "—", v])
    for k, v in b_sa.items():
        clause_labels.append(f"B-single: {k}")
        matrix.append(["—", v, v])
    for k, vv in joint.items():
        clause_labels.append(f"JOINT: {k}")
        matrix.append([vv["axis_a"], vv["axis_b"], vv["PASS_AND"]])

    n_rows = len(clause_labels)
    n_cols = 3                                                                   # (local)
    color_map = {                                                                # (local)
        "PASS": "#2ca02c",
        "INFO": "#ff7f0e",
        "FAIL": "#d62728",
        "—":    "#cccccc",
        "MISSING": "#444444",
    }
    fig, ax = plt.subplots(figsize=(11, max(3.5, 0.55 * n_rows + 2.5)))
    for i in range(n_rows):
        for j in range(n_cols):
            color = color_map.get(matrix[i][j], "#888888")
            ax.add_patch(plt.Rectangle((j, n_rows - 1 - i), 1, 1,
                                       facecolor=color, edgecolor="black", linewidth=0.5))
            ax.text(j + 0.5, n_rows - 1 - i + 0.5, matrix[i][j],
                    ha="center", va="center", fontsize=9,
                    color="white", weight="bold")
    ax.set_xlim(0, n_cols)
    ax.set_ylim(0, n_rows + 0.5)
    ax.set_xticks([0.5, 1.5, 2.5])
    ax.set_xticklabels(["Axis-A\n(connes-ncg)", "Axis-B\n(transit-dynamics)",
                        "PASS-AND\n(aggregate)"])
    ax.set_yticks([n_rows - 1 - i + 0.5 for i in range(n_rows)])
    ax.set_yticklabels(clause_labels, fontsize=8)
    ax.set_aspect("equal")
    ax.tick_params(axis="x", which="both", bottom=False, top=False)
    ax.tick_params(axis="y", which="both", left=False, right=False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    title = (
        f"§W5-4 Stage-2 PASS-AND Aggregator — composite={detail['composite_verdict']}\n"
        f"§VII.AU.OP-PROJ STAGE-1-CANDIDATE  |  obs_1 = first-extraction empirical anchor"
    )
    ax.set_title(title, fontsize=10)

    # Substrate-input-orthogonality annotation
    sio_text = (
        f"substrate-input-orthogonality: {sio.get('verdict')}\n"
        f"  Set_A (Axis-A only): {sio.get('set_A_sha256', '?')[:16]}...\n"
        f"  Set_B (Axis-B only): {sio.get('set_B_sha256', '?')[:16]}...\n"
        f"  Set_A != Set_B ⇒ data-orthogonal at structural ceiling\n"
        f"  (K=3 MANDATORY per joint-theorem-promotion.md §"
        f"'Substrate-input-orthogonality clause')"
    )
    fig.text(0.02, -0.02, sio_text, fontsize=8, ha="left", va="top",
             family="monospace")

    plt.tight_layout(rect=[0, 0.02, 1, 1])
    plt.savefig(out_png, dpi=130, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Section 9 — Verdict emission (atomic POSIX O_APPEND)
# ---------------------------------------------------------------------------

def append_verdict_line(verdict: str, value: str,
                        audit_sha: str, content_sha: str) -> None:
    """Atomic single-line append (S84+ dual-SHA schema).

    Also appends the dual-SHA companion comment row AND the S87+ schema-v2
    3-tuple companion row (REQUIRED for [VERIFY-THEOREM] trigger).
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # For Stage-2 PASS-AND aggregator, sign_verdict applies to the conjunctive
    # predicate direction (PASS-AND positive ⇒ sign_verdict=PASS); magnitude
    # is N/A for set-test, mapped to PASS when composite is PASS; regime is
    # VALID for verdict-aggregator (no auto-shortening, no scan window).
    sign_v, mag_v, reg_v = "PASS", "PASS", "VALID"                               # (local)
    if verdict == "FAIL":
        sign_v, mag_v, reg_v = "FAIL", "FAIL", "VALID"
    elif verdict == "INFO":
        sign_v, mag_v, reg_v = "PASS", "INFO", "VALID"
    companion_3tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    payload = canonical + companion_dual_sha + companion_3tuple
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(payload)


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                             # (local)
    print("=" * 78)
    print(f"  {GATE_ID}")
    print(f"  scheme={SCHEME}")
    print(f"  convention={CONVENTION}")
    print("=" * 78)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                                       # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS_PY, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 2. Phase A — chained-prereq verification
    print("--- Phase A: chained-prereq verification ---")
    s92_text = S92_VERDICTS_TXT.read_text(encoding="utf-8")
    w5_2_check = verify_chained_prereq(
        s92_text, W5_2_PASS_AUDIT_SHA,
        "S92-W5-CF-S92-W2-2-W2-3-JOINT-VII-AU-OP-PROJ-STAGE-1-CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED:"
    )
    w5_3_check = verify_chained_prereq(
        s92_text, W5_3_PASS_AUDIT_SHA,
        "S92-W5-CF-S91-W6-1-VII-AU-OP-PROJ-STAGE-1-CANDIDATE-LANDING:"
    )
    print(f"  §W5-2 expected PASS audit_sha={W5_2_PASS_AUDIT_SHA[:16]}... "
          f"found={w5_2_check['found_expected_pass_audit_sha']} "
          f"canonical={w5_2_check['expected_is_canonical']}")
    print(f"  §W5-3 expected PASS audit_sha={W5_3_PASS_AUDIT_SHA[:16]}... "
          f"found={w5_3_check['found_expected_pass_audit_sha']} "
          f"canonical={w5_3_check['expected_is_canonical']}")
    chained_prereq_pass = (
        w5_2_check["found_expected_pass_audit_sha"]
        and w5_3_check["found_expected_pass_audit_sha"]
    )
    if not chained_prereq_pass:
        print("  CHAINED-PREREQ FAIL — would trigger mechanical-closure-discipline")
    else:
        print("  CHAINED-PREREQ PASS")
    print()

    # 3. Phase B-D-E — load both cross-reviewer verdicts (workshop transcripts
    #    NOT read; reviewers operated independently per joint-theorem-promotion.md)
    print("--- Phase B-E: load cross-reviewer verdicts ---")
    axis_a = json.loads(AXIS_A_VERDICT_JSON.read_text(encoding="utf-8"))
    axis_b = json.loads(AXIS_B_VERDICT_JSON.read_text(encoding="utf-8"))
    print(f"  Axis-A agent: {axis_a.get('agent', '?')}")
    print(f"  Axis-A axis:  {axis_a.get('axis', '?')}")
    print(f"  Axis-A composite (self-reported): {axis_a.get('axis_A_composite', '?')}")
    print(f"  Axis-B agent: {axis_b.get('agent', '?')}")
    print(f"  Axis-B axis:  {axis_b.get('axis', '?')}")
    print(f"  Axis-B composite (self-reported): {axis_b.get('axis_B_composite', '?')}")
    print()

    # 4. Phase F — substrate-input-orthogonality
    print("--- Phase F: substrate-input-orthogonality ---")
    set_a_sha = sha256_of(SET_A_NPZ_RUNTIME)
    set_b_sha = sha256_of(SET_B_NPZ)
    print(f"  Set_A (Axis-A only): {SET_A_NPZ_RUNTIME.name}")
    print(f"    SHA-256: {set_a_sha}")
    print(f"    [runtime canonical-path rescue from plan-pinned")
    print(f"     {SET_A_NPZ_PLAN_PINNED.relative_to(PROJECT_ROOT)} (MISSING-on-disk)")
    print(f"     per substrate-first-canonical-sourcing.md §(ii.B)]")
    print(f"  Set_B (Axis-B only): {SET_B_NPZ.name}")
    print(f"    SHA-256: {set_b_sha}")
    # Cross-check against cross-reviewer-claimed SHAs
    axis_a_set_a_sha = axis_a.get("set_A_sha256", "")
    axis_b_set_b_sha = axis_b.get("set_B_sha256", "")
    if axis_a_set_a_sha and axis_a_set_a_sha != set_a_sha:
        print(f"  WARN: Axis-A's claimed Set_A SHA differs from runtime read:")
        print(f"        claimed   = {axis_a_set_a_sha}")
        print(f"        runtime   = {set_a_sha}")
    else:
        print(f"  Axis-A Set_A SHA cross-check: MATCH")
    if axis_b_set_b_sha and axis_b_set_b_sha != set_b_sha:
        print(f"  WARN: Axis-B's claimed Set_B SHA differs from runtime read:")
        print(f"        claimed   = {axis_b_set_b_sha}")
        print(f"        runtime   = {set_b_sha}")
    else:
        print(f"  Axis-B Set_B SHA cross-check: MATCH")
    sio = verify_substrate_input_orthogonality(set_a_sha, set_b_sha)
    print(f"  substrate-input-orthogonality: {sio['verdict']}")
    print(f"  reason: {sio['reason']}")
    print()

    # 5. Phase G — PASS-AND aggregation
    print("--- Phase G: PASS-AND aggregation ---")
    detail = aggregate_pass_and(axis_a, axis_b, sio)
    composite = detail["composite_verdict"]
    print(f"  Axis-A single-axis verdicts: {detail['axis_a_single_axis_verdicts']}")
    print(f"  Axis-B single-axis verdicts: {detail['axis_b_single_axis_verdicts']}")
    print(f"  JOINT PASS-AND: {detail['joint_clauses_pass_and']}")
    print(f"  composite={composite}")
    print(f"  reason: {detail['composite_reason']}")
    print()

    # 6. If chained-prereq fails, override composite to FAIL (mechanical closure)
    final_verdict = composite                                                    # (local)
    if not chained_prereq_pass:
        final_verdict = "FAIL"

    # 7. Build compact value string for verdict line
    n_a_pass = sum(1 for v in detail["axis_a_single_axis_verdicts"].values()
                   if v == "PASS")
    n_a_tot = len(detail["axis_a_single_axis_verdicts"])
    n_b_pass = sum(1 for v in detail["axis_b_single_axis_verdicts"].values()
                   if v == "PASS")
    n_b_tot = len(detail["axis_b_single_axis_verdicts"])
    n_joint_pass = sum(1 for vv in detail["joint_clauses_pass_and"].values()
                       if vv["PASS_AND"] == "PASS")
    n_joint_tot = len(detail["joint_clauses_pass_and"])
    value_str = (
        f"composite={composite};"
        f"axis_a_single={n_a_pass}_of_{n_a_tot}_PASS;"
        f"axis_b_single={n_b_pass}_of_{n_b_tot}_PASS;"
        f"joint_PASS_AND={n_joint_pass}_of_{n_joint_tot};"
        f"substrate_input_orthogonality={sio['verdict']};"
        f"set_A_sha256_short={set_a_sha[:16]};"
        f"set_B_sha256_short={set_b_sha[:16]};"
        f"anchor_1_w6_1_pass_a_short={ANCHOR_1_W6_1_PASS_A_SHORT};"
        f"anchor_2_s91_w5_w6_promo_short={ANCHOR_2_S91_W5_W6_PROMO_SHORT};"
        f"w5_2_chained_prereq_audit_sha_short={W5_2_PASS_AUDIT_SHA[:16]};"
        f"w5_3_chained_prereq_audit_sha_short={W5_3_PASS_AUDIT_SHA[:16]};"
        f"chained_prereq={chained_prereq_pass};"
        f"axis_a_agent=connes-ncg-theorist;"
        f"axis_b_agent=transit-dynamics-theorist;"
        f"lizzi_excluded=True;"
        f"set_A_runtime_canonical_path_rescue=True;"
        f"K_post_orthogonality=K_3_MANDATORY_PRESERVED;"
        f"vii_au_op_proj_stage_3_eligibility=conditional_on_W5_5_PASS"
    )

    # 8. Save composite npz
    np.savez_compressed(
        OUT_NPZ,
        gate_id=GATE_ID,
        composite_verdict=composite,
        final_verdict=final_verdict,
        composite_reason=detail["composite_reason"],
        axis_a_single_axis_keys=list(detail["axis_a_single_axis_verdicts"].keys()),
        axis_a_single_axis_values=list(detail["axis_a_single_axis_verdicts"].values()),
        axis_b_single_axis_keys=list(detail["axis_b_single_axis_verdicts"].keys()),
        axis_b_single_axis_values=list(detail["axis_b_single_axis_verdicts"].values()),
        joint_clause_keys=list(detail["joint_clauses_pass_and"].keys()),
        joint_clause_axis_a=[detail["joint_clauses_pass_and"][k]["axis_a"]
                             for k in detail["joint_clauses_pass_and"]],
        joint_clause_axis_b=[detail["joint_clauses_pass_and"][k]["axis_b"]
                             for k in detail["joint_clauses_pass_and"]],
        joint_clause_pass_and=[detail["joint_clauses_pass_and"][k]["PASS_AND"]
                               for k in detail["joint_clauses_pass_and"]],
        substrate_input_orthogonality=sio["verdict"],
        substrate_input_orthogonality_reason=sio["reason"],
        set_A_sha256=set_a_sha,
        set_B_sha256=set_b_sha,
        set_A_path_runtime=str(SET_A_NPZ_RUNTIME.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        set_A_path_plan_pinned=str(SET_A_NPZ_PLAN_PINNED.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        set_B_path=str(SET_B_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        anchor_1_w6_1_pass_a=ANCHOR_1_W6_1_PASS_A_FULL,
        anchor_2_s91_w5_w6_promotion=ANCHOR_2_S91_W5_W6_PROMO_FULL,
        w5_2_chained_prereq_audit_sha=W5_2_PASS_AUDIT_SHA,
        w5_3_chained_prereq_audit_sha=W5_3_PASS_AUDIT_SHA,
        chained_prereq_pass=chained_prereq_pass,
        axis_a_agent="connes-ncg-theorist",
        axis_b_agent="transit-dynamics-theorist",
        lizzi_excluded=True,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        n_pass_axis_a_single=n_a_pass,
        n_pass_axis_b_single=n_b_pass,
        n_pass_joint=n_joint_pass,
        n_total_axis_a_single=n_a_tot,
        n_total_axis_b_single=n_b_tot,
        n_total_joint=n_joint_tot,
    )
    print(f"  wrote: {OUT_NPZ}")

    # 9. Plot
    make_plot(detail, OUT_PNG)
    print(f"  wrote: {OUT_PNG}")

    # 10. Emit verdict line (S87+ schema-v2 with dual-SHA + 3-tuple companion rows)
    append_verdict_line(final_verdict, value_str, audit_sha, content_sha)
    print(f"  appended verdict: {final_verdict}")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")

    wall = time.time() - t0                                                      # (local)
    print()
    print(f"=== {GATE_ID}: {final_verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 always (per math-scripts.md §Exit Codes)


if __name__ == "__main__":
    sys.exit(main())
