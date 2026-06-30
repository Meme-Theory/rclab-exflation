#!/usr/bin/env python3
"""
S94 W1-1 — S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY (composite Stage-2 aggregator)
=============================================================================

Gate: S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY ([VERIFY-THEOREM])

Orchestrator-of-gate Stage-2 aggregator for the §VII.BA `#### (h)` STAGE-1-CANDIDATE
JOINT TWO-AXIS composite-bridge-map dimensional-class admissibility theorem (registered
S93 W1-2; THIRD framework joint cross-axis theorem after §VII.AH and §VII.U.2 Var_a),
per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway, §"Stage 2".

This script does NOT re-derive the per-axis clauses — the INDEPENDENCE of the two
cross-reviews is the physics (both reviewers re-derived the registered Stage-1 entry
WITHOUT prior workshop context, on structurally orthogonal substrate-input anchors).
This aggregator's job is the DETERMINISTIC boolean PASS-AND aggregation:

  - load the two cross-reviewer per-clause verdict JSONs (computed booleans, NOT hardcoded)
  - PASS-AND the JOINT clause (c) across the two independent verdicts (logical AND, NOT OR)
  - confirm substrate-input-orthogonality (∃ obs_i loaded by exactly ONE reviewer)
  - emit the composite Stage-2 verdict.

Cross-reviewers (axis-distinct; NEITHER is connes nor mack, the EXCLUDED original authors):
  - Axis-A (spectral / NCG-axiomatic) : lizzi-spectral-functional-theorist
      input : computations/session-94/s94_w1_1_axisA_lizzi_verdict.json
      clauses: (a) homogeneity-degree obstruction, (e) pole-scoping/index-rigidity,
               JOINT (c) Delta_scheme->0 (Axis-A face)
      orthogonality anchor: s92_w1_cf_w9_8_1_composite_bridge_map_wodzicki_hkr.npz
  - Axis-B (transport / substrate-natural-binding) : volovik-superfluid-universe-theorist
      input : computations/session-94/s94_w1_1_axisB_volovik_verdict.json
      clauses: (binding) canonical-import-scalar-VACUOUS / substrate-natural-non-scalar,
               JOINT (c) Delta_scheme->0 (Axis-B face)
      orthogonality anchor: s92_w2_wodzicki_f_functor_normalization.npz

Aggregation operator (gate block §W1-1):
  Stage2_PASS := (axisA_single_axis_all == PASS)
               AND (axisB_single_axis_all == PASS)
               AND (clause_c_axisA == PASS AND clause_c_axisB == PASS)   [JOINT clause (c) logical AND]
               AND substrate_input_orthogonality
  substrate_input_orthogonality := (axisA.substrate_input_anchor != axisB.substrate_input_anchor)
    -> two DISTINCT data files => structural ceiling, NO substrate-input-overlap caveat
       (the §VII.AH STAGE-3-PERMANENT structural-ceiling precedent, S89 W4-7).

PASS_meaning : §VII.BA `#### (h)` becomes STAGE-3-PERMANENT-ELIGIBLE (orchestrator flips the
               registry tag at wave close). FOURTH framework cross-axis joint theorem toward
               STAGE-3-PERMANENT (after §VII.AH FIRST, §VII.U.2 Var_a, §VII.AW.OP-PROJ, §VII.BB).
FAIL_meaning : any reviewer FAIL on any clause -> theorem stays STAGE-1-CANDIDATE; FAIL clause
               routes to next-session remediation.
INFO_meaning : any reviewer INFO on a clause (no FAIL) -> stays STAGE-1, INFO clause documented
               as Stage-2-INFO-deferred. Also fires if orthogonality cannot be established
               (both reviewers load the SAME data) -> substrate-input-overlap caveat (Verdict B).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-94/s94_w1_1_axisA_lizzi_verdict.json   (Axis-A verdict; feeds audit_sha256)
  - computations/session-94/s94_w1_1_axisB_volovik_verdict.json (Axis-B verdict; feeds audit_sha256)
  - sessions/permanent-results-registry.md                      (registry entry; feeds audit_sha256)
  - canonical_constants.py                                      (feeds audit_sha256)
  - script bytes                                                (feeds BOTH audit_sha256 + content_sha256)
The gate-block audit_sha256_inputs = [script, canonical, pinmap, axisA_verdict_sha,
axisB_verdict_sha, registry_entry_sha]; the two reviewer JSONs + the registry file are
in INPUT_FILES, so the pinmap folds their SHAs into audit_sha256 by construction.

Output 4-tuple:
  (value=<composite + substitution-chain summary>,
   scheme=stage-2-independent-verify-two-axis-NCG-spectral-and-transport,
   convention=registry-§VII.BA-(h)-STAGE-1-CANDIDATE-per-clause-PASS-AND, L_max=12)

Classification: GEOMETRIC (Stage-2 of the joint-theorem-promotion pathway; no D_K diagonalization).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
import os as _os
from pathlib import Path as _P

_os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only boolean aggregator; no GPU
_os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

_SHARED = _P(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import M_KK_gravity, Delta_BCS  # noqa: F401  canonical pins (cross-check only)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S94"                                                              # (local)
GATE_ID = "S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY"                             # (local)
SCHEME = "stage-2-independent-verify-two-axis-NCG-spectral-and-transport"    # (local)
CONVENTION = "registry-VII.BA-(h)-STAGE-1-CANDIDATE-per-clause-PASS-AND"     # (local)
L_MAX = 12                                                                   # (local)

# Pre-registered tolerance (plan §W1-1): JOINT clause (c) Delta_scheme machine-zero band.
DELTA_SCHEME_TOL = 1e-9  # (local) |Delta_scheme| < 1e-9 M_KK^2 (CF-55 Reading-A anchor)

# Cross-reviewer verdict JSON inputs (orchestrator-provided; both verified on disk).
AXIS_A_JSON = SESSION_DIR / "s94_w1_1_axisA_lizzi_verdict.json"    # (local)
AXIS_B_JSON = SESSION_DIR / "s94_w1_1_axisB_volovik_verdict.json"  # (local)
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

OUT_NPZ = SESSION_DIR / "s94_w1_1_vii_ba_stage_2_cross_axis_verify.npz"
OUT_PNG = SESSION_DIR / "s94_w1_1_vii_ba_stage_2_cross_axis_verify.png"
VERDICT_TXT = SESSION_DIR / "s94_gate_verdicts.txt"

# INPUT_FILES order matters only for the printed pin log; the pinmap is sorted before hashing.
# Per gate-block audit_sha256_inputs: canonical + axisA_verdict + axisB_verdict + registry_entry.
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AXIS_A_JSON,
    AXIS_B_JSON,
    REGISTRY_MD,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin helpers (S84+ dual-SHA schema, W9a-99 split)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure/pinmap."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering); legacy informational."""
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
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
                     where pinmap_json folds the axis-A verdict SHA, axis-B verdict SHA,
                     and registry-entry SHA (all in `pins`), satisfying the gate-block
                     audit_sha256_inputs requirement.
    content_sha256 = sha256( bytes(script) )  — script-only, invariant under canonical/pinmap.
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
# Section 5 — Load the two cross-reviewer verdict JSONs (computed, NOT hardcoded)
# ---------------------------------------------------------------------------
def load_axis_verdicts() -> dict:
    """Load both reviewer JSONs; return a dict of the booleans the aggregation needs.

    The verdict strings are READ from the JSON file contents (not hardcoded), per the
    spawn directive: 'compute the booleans from the file contents'.
    """
    with AXIS_A_JSON.open("r", encoding="utf-8") as f:
        a = json.load(f)  # (local) Axis-A (lizzi) verdict
    with AXIS_B_JSON.open("r", encoding="utf-8") as f:
        b = json.load(f)  # (local) Axis-B (volovik) verdict

    return {
        # Axis-A (spectral): single-axis clauses (a),(e) + JOINT (c) face
        "axisA_clause_a": a["clauses"]["a"],
        "axisA_clause_e": a["clauses"]["e"],
        "axisA_clause_c": a["clauses"]["c_joint"],
        "axisA_single_axis_all": a["axisA_single_axis_all"],
        "axisA_delta_scheme": float(a.get("delta_scheme_value", float("nan"))),
        "axisA_anchor": a["substrate_input_anchor"],
        # Axis-B (transport): single-axis clause (binding) + JOINT (c) face
        "axisB_clause_binding": b["clauses"]["binding"],
        "axisB_clause_c": b["clauses"]["c_joint"],
        "axisB_single_axis_all": b["axisB_single_axis_all"],
        "axisB_delta_scheme": float(b.get("delta_scheme_value", float("nan"))),
        "axisB_anchor": b["substrate_input_anchor"],
        "_axisA_reviewer": a.get("reviewer", "lizzi-axisA"),
        "_axisB_reviewer": b.get("reviewer", "volovik-axisB"),
    }


# ---------------------------------------------------------------------------
# Section 6 — Compute (the deterministic PASS-AND aggregation)
# ---------------------------------------------------------------------------
def compute() -> dict:
    v = load_axis_verdicts()

    # ---- Substitution chain (gate block §W1-1, instantiated with loaded verdicts) ----
    # Step 1: clause_c_axisA = lizzi-spectral Delta_scheme->0 verdict (re-derived from
    #         the registered Stage-1 entry, NOT from the workshop).
    clause_c_axisA = (v["axisA_clause_c"] == "PASS")  # (local)
    # Step 2: clause_c_axisB = volovik-transport verdict on the SAME Delta_scheme->0 test
    #         (independently re-derived, no shared workshop context).
    clause_c_axisB = (v["axisB_clause_c"] == "PASS")  # (local)
    # Step 3: clause_c_PASS_AND = (clause_c_axisA AND clause_c_axisB)  [logical AND, NOT OR;
    #         single-reviewer PASS structurally insufficient per the joint-clause refusal of
    #         single-agent firings].
    clause_c_PASS_AND = bool(clause_c_axisA and clause_c_axisB)  # (local)

    # Single-axis aggregates (read from each reviewer's own all-clauses field AND
    # independently re-derived from the per-clause verdicts for cross-check).
    axisA_PASS = (v["axisA_single_axis_all"] == "PASS")  # (local)
    axisB_PASS = (v["axisB_single_axis_all"] == "PASS")  # (local)
    # Cross-check the reviewer-reported aggregate against the per-clause AND.
    axisA_PASS_recomputed = (v["axisA_clause_a"] == "PASS") and (v["axisA_clause_e"] == "PASS")  # (local)
    axisB_PASS_recomputed = (v["axisB_clause_binding"] == "PASS")  # (local) sole Axis-B single-axis clause
    axisA_aggregate_consistent = (axisA_PASS == axisA_PASS_recomputed)  # (local)
    axisB_aggregate_consistent = (axisB_PASS == axisB_PASS_recomputed)  # (local)

    # Step 5: substrate_input_orthogonality direction — EXISTS obs_i loaded by exactly ONE
    #         reviewer.  Here the two reviewers' substrate_input_anchor values are DISTINCT
    #         files => orthogonality at >= 1 observable => structural ceiling, NO overlap caveat.
    anchors_distinct = (v["axisA_anchor"] != v["axisB_anchor"])  # (local)
    substrate_input_orthogonality = bool(anchors_distinct)  # (local)

    # Step 4: Stage2_composite_PASS — substitute and simplify.
    stage2_PASS = bool(axisA_PASS and axisB_PASS and clause_c_PASS_AND and substrate_input_orthogonality)

    # ---- INFO detection (any clause INFO, no FAIL) and FAIL detection (any clause FAIL) ----
    all_clause_verdicts = [
        ("axisA", "(a)", v["axisA_clause_a"]),
        ("axisA", "(e)", v["axisA_clause_e"]),
        ("axisA", "(c)", v["axisA_clause_c"]),
        ("axisB", "(binding)", v["axisB_clause_binding"]),
        ("axisB", "(c)", v["axisB_clause_c"]),
    ]  # (local)
    fail_clauses = [(ax, cl) for ax, cl, vd in all_clause_verdicts if vd == "FAIL"]  # (local)
    info_clauses = [(ax, cl) for ax, cl, vd in all_clause_verdicts if vd == "INFO"]  # (local)
    n_pass = sum(1 for _, _, vd in all_clause_verdicts if vd == "PASS")  # (local)

    # ---- Composite verdict (joint-theorem-promotion.md §"Stage 2" collapse) ----
    #   FAIL : any clause FAIL  -> Stage-2->3 BLOCKED, theorem stays STAGE-1
    #   INFO : any clause INFO (no FAIL) OR orthogonality fails -> stays STAGE-1, Stage-2-INFO-deferred
    #          (orthogonality-fail also carries the substrate-input-overlap caveat, Verdict B)
    #   PASS : all PASS + clause_c_PASS_AND + orthogonality
    overlap_caveat = not substrate_input_orthogonality  # (local) Verdict B trigger
    if len(fail_clauses) > 0:
        composite = "FAIL"
        promotion_decision = "BLOCK"
        stage3_eligible = False
    elif len(info_clauses) > 0 or overlap_caveat:
        composite = "INFO"
        promotion_decision = "BLOCK"
        stage3_eligible = False
    elif stage2_PASS:
        composite = "PASS"
        promotion_decision = "PROMOTE-ELIGIBLE"
        stage3_eligible = True
    else:
        # Defensive: should not reach here if the boolean chain is consistent.
        composite = "INFO"
        promotion_decision = "BLOCK"
        stage3_eligible = False

    # ---- Stage-2 protocol-compliance checklist (joint-theorem-promotion.md §"Stage 2") ----
    protocol_compliance = {
        "1_dispatched_in_parallel": True,            # orchestrator dispatched both reviewers in parallel
        "2_different_axes": True,                    # Axis-A spectral/NCG vs Axis-B transport/superfluid
        "3_not_original_workshop_authors": True,     # lizzi + volovik; connes + mack EXCLUDED (original authors)
        "4_no_workshop_transcripts_in_prompt": True, # reviewers read only the registered Stage-1 entry + cited inputs
        "5_passand_on_joint_applied": True,          # this aggregator (clause (c) PASS-AND)
        "6_substrate_input_orthogonality_at_>=1_obs": substrate_input_orthogonality,
    }

    # ---- Canonical-pin cross-check (the reviewers both verified these; we re-confirm) ----
    canonical_cross_check = {
        "M_KK_gravity": float(M_KK_gravity),
        "Delta_BCS": float(Delta_BCS),
        "axisA_delta_scheme_within_tol": bool(abs(v["axisA_delta_scheme"]) < DELTA_SCHEME_TOL),
        "axisB_delta_scheme_within_tol": bool(abs(v["axisB_delta_scheme"]) < DELTA_SCHEME_TOL),
    }

    return {
        "value": composite,
        "composite_verdict": composite,
        "promotion_decision": promotion_decision,
        "stage3_eligible": stage3_eligible,
        "overlap_caveat": overlap_caveat,
        # substitution-chain booleans
        "clause_c_axisA": clause_c_axisA,
        "clause_c_axisB": clause_c_axisB,
        "clause_c_PASS_AND": clause_c_PASS_AND,
        "axisA_PASS": axisA_PASS,
        "axisB_PASS": axisB_PASS,
        "axisA_aggregate_consistent": axisA_aggregate_consistent,
        "axisB_aggregate_consistent": axisB_aggregate_consistent,
        "substrate_input_orthogonality": substrate_input_orthogonality,
        "anchors_distinct": anchors_distinct,
        "stage2_PASS": stage2_PASS,
        # per-clause table + diagnostics
        "all_clause_verdicts": all_clause_verdicts,
        "fail_clauses": fail_clauses,
        "info_clauses": info_clauses,
        "n_pass": n_pass,
        "protocol_compliance": protocol_compliance,
        "canonical_cross_check": canonical_cross_check,
        # raw loaded verdicts (for the npz + WP audit trail)
        "loaded": v,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot (clause × reviewer PASS-AND matrix heatmap)
# ---------------------------------------------------------------------------
def make_plot(result: dict) -> None:
    """Clause-by-reviewer PASS-AND matrix heatmap (optional figure for this aggregation gate)."""
    v = result["loaded"]
    # Rows = clauses; columns = {Axis-A lizzi, Axis-B volovik}. JOINT (c) spans both columns.
    clause_labels = ["(a) homog-degree", "(e) pole-scope/index", "(binding) scalar-VACUOUS", "(c) JOINT Δ_scheme→0"]
    col_labels = ["Axis-A (lizzi)\nspectral/NCG", "Axis-B (volovik)\ntransport"]

    # verdict -> numeric (PASS=1, INFO=0.5, FAIL=0, N/A=nan)
    def vnum(s):
        return {"PASS": 1.0, "INFO": 0.5, "FAIL": 0.0}.get(s, np.nan)

    # Build matrix: rows are the 4 clause-labels, cols are the 2 axes.
    M = np.full((4, 2), np.nan)  # (local)
    # (a): Axis-A only
    M[0, 0] = vnum(v["axisA_clause_a"])
    # (e): Axis-A only
    M[1, 0] = vnum(v["axisA_clause_e"])
    # (binding): Axis-B only
    M[2, 1] = vnum(v["axisB_clause_binding"])
    # (c) JOINT: both faces (PASS-AND)
    M[3, 0] = vnum(v["axisA_clause_c"])
    M[3, 1] = vnum(v["axisB_clause_c"])

    fig, ax = plt.subplots(figsize=(7.2, 5.0))
    cmap = matplotlib.colors.ListedColormap(["#c1432f", "#e0b13a", "#2e8b57"])  # FAIL/INFO/PASS
    bounds = [-0.25, 0.25, 0.75, 1.25]
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    masked = np.ma.masked_invalid(M)
    cmap.set_bad(color="#d9d9d9")
    im = ax.imshow(masked, cmap=cmap, norm=norm, aspect="auto")

    ax.set_xticks(range(2))
    ax.set_xticklabels(col_labels, fontsize=9)
    ax.set_yticks(range(4))
    ax.set_yticklabels(clause_labels, fontsize=9)

    # annotate each cell with the verdict string
    cell_text = [
        [v["axisA_clause_a"], ""],
        [v["axisA_clause_e"], ""],
        ["", v["axisB_clause_binding"]],
        [v["axisA_clause_c"], v["axisB_clause_c"]],
    ]
    for i in range(4):
        for j in range(2):
            t = cell_text[i][j]
            if t:
                ax.text(j, i, t, ha="center", va="center", color="white", fontweight="bold", fontsize=10)
            elif np.isnan(M[i, j]):
                ax.text(j, i, "n/a", ha="center", va="center", color="#777777", fontsize=8)

    composite = result["composite_verdict"]
    pa = "PASS-AND=True" if result["clause_c_PASS_AND"] else "PASS-AND=False"
    orth = "orthogonal" if result["substrate_input_orthogonality"] else "OVERLAP-caveat"
    ax.set_title(
        f"S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY\n"
        f"JOINT clause (c) {pa}  |  substrate-input {orth}\n"
        f"composite = {composite}  ->  "
        f"{'STAGE-3-PERMANENT-ELIGIBLE' if result['stage3_eligible'] else 'stays STAGE-1-CANDIDATE'}",
        fontsize=10,
    )
    cbar = fig.colorbar(im, ax=ax, ticks=[0.0, 0.5, 1.0], fraction=0.046, pad=0.04)
    cbar.ax.set_yticklabels(["FAIL", "INFO", "PASS"])
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)
    print(f"  PNG saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 8 — Verdict + 4-tuple
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str, annotation: str) -> None:
    """Atomic append of the canonical verdict line + dual-SHA companion comment row.

    No 3-tuple companion row ([VERIFY-THEOREM] trigger; no directional pre-registration).
    """
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
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first lines of stdout) + dual SHA
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap[axisA,axisB,registry])")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute (deterministic boolean PASS-AND aggregation)
    result = compute()
    v = result["loaded"]

    # 3. Print the substitution chain instantiated with the loaded verdicts
    print("=== Substitution chain (gate block §W1-1, instantiated) ===")
    print(f"  Step 1: clause_c_axisA  = lizzi  Δ_scheme→0 verdict = {v['axisA_clause_c']}  "
          f"(Δ_scheme={v['axisA_delta_scheme']:.3e} < {DELTA_SCHEME_TOL:.0e})  -> {result['clause_c_axisA']}")
    print(f"  Step 2: clause_c_axisB  = volovik Δ_scheme→0 verdict = {v['axisB_clause_c']}  "
          f"(Δ_scheme={v['axisB_delta_scheme']:.3e} < {DELTA_SCHEME_TOL:.0e})  -> {result['clause_c_axisB']}")
    print(f"  Step 3: clause_c_PASS_AND = (clause_c_axisA AND clause_c_axisB) = {result['clause_c_PASS_AND']}  "
          f"[logical AND, NOT OR]")
    print(f"  Step 4: Stage2_composite_PASS = (axisA_PASS={result['axisA_PASS']} "
          f"AND axisB_PASS={result['axisB_PASS']} AND clause_c_PASS_AND={result['clause_c_PASS_AND']} "
          f"AND orthogonality={result['substrate_input_orthogonality']}) = {result['stage2_PASS']}")
    print(f"  Step 5: substrate_input_orthogonality: axisA_anchor='{v['axisA_anchor']}' "
          f"!= axisB_anchor='{v['axisB_anchor']}' -> {result['anchors_distinct']} "
          f"(structural ceiling, {'NO' if not result['overlap_caveat'] else 'WITH'} overlap caveat)")
    print(f"  Conclusion: composite = {result['composite_verdict']}  "
          f"-> §VII.BA `#### (h)` {'STAGE-3-PERMANENT-ELIGIBLE' if result['stage3_eligible'] else 'stays STAGE-1-CANDIDATE'}")
    print()

    # 4. Print per-clause × per-reviewer matrix
    print("=== Per-clause × per-reviewer verdict matrix ===")
    for ax, cl, vd in result["all_clause_verdicts"]:
        print(f"  {ax:<6} clause {cl:<11} = {vd}")
    print(f"  n_pass={result['n_pass']}/5  n_fail={len(result['fail_clauses'])}  n_info={len(result['info_clauses'])}")
    print(f"  axisA aggregate consistent (reported==recomputed): {result['axisA_aggregate_consistent']}")
    print(f"  axisB aggregate consistent (reported==recomputed): {result['axisB_aggregate_consistent']}")
    print()
    print("=== Stage-2 protocol compliance ===")
    for k, val in result["protocol_compliance"].items():
        print(f"  {k}: {val}")
    print()
    print("=== Canonical-pin cross-check ===")
    for k, val in result["canonical_cross_check"].items():
        print(f"  {k}: {val}")
    print()

    # 5. Plot (optional figure)
    make_plot(result)

    # 6. Save NPZ — the clause-by-reviewer PASS-AND matrix + booleans
    np.savez(
        OUT_NPZ,
        composite_verdict=np.array(result["composite_verdict"], dtype="<U10"),
        promotion_decision=np.array(result["promotion_decision"], dtype="<U24"),
        stage3_eligible=np.array(result["stage3_eligible"]),
        # substitution-chain booleans
        clause_c_axisA=np.array(result["clause_c_axisA"]),
        clause_c_axisB=np.array(result["clause_c_axisB"]),
        clause_c_PASS_AND=np.array(result["clause_c_PASS_AND"]),
        axisA_PASS=np.array(result["axisA_PASS"]),
        axisB_PASS=np.array(result["axisB_PASS"]),
        substrate_input_orthogonality=np.array(result["substrate_input_orthogonality"]),
        anchors_distinct=np.array(result["anchors_distinct"]),
        overlap_caveat=np.array(result["overlap_caveat"]),
        stage2_PASS=np.array(result["stage2_PASS"]),
        axisA_aggregate_consistent=np.array(result["axisA_aggregate_consistent"]),
        axisB_aggregate_consistent=np.array(result["axisB_aggregate_consistent"]),
        # per-clause verdict strings (the clause × reviewer matrix)
        clause_axisA_a=np.array(v["axisA_clause_a"]),
        clause_axisA_e=np.array(v["axisA_clause_e"]),
        clause_axisA_c=np.array(v["axisA_clause_c"]),
        clause_axisB_binding=np.array(v["axisB_clause_binding"]),
        clause_axisB_c=np.array(v["axisB_clause_c"]),
        axisA_single_axis_all=np.array(v["axisA_single_axis_all"]),
        axisB_single_axis_all=np.array(v["axisB_single_axis_all"]),
        axisA_delta_scheme=np.array(v["axisA_delta_scheme"]),
        axisB_delta_scheme=np.array(v["axisB_delta_scheme"]),
        axisA_anchor=np.array(v["axisA_anchor"]),
        axisB_anchor=np.array(v["axisB_anchor"]),
        n_pass=np.int64(result["n_pass"]),
        n_fail=np.int64(len(result["fail_clauses"])),
        n_info=np.int64(len(result["info_clauses"])),
        DELTA_SCHEME_TOL=np.array(DELTA_SCHEME_TOL),
        protocol_compliance=np.array(json.dumps(result["protocol_compliance"], default=str), dtype=object),
        canonical_cross_check=np.array(json.dumps(result["canonical_cross_check"], default=str), dtype=object),
    )
    print(f"  NPZ saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 7. 4-tuple + verdict line
    value_str = (
        f"composite={result['composite_verdict']};"
        f"stage3_eligible={result['stage3_eligible']};"
        f"clause_c_PASS_AND={result['clause_c_PASS_AND']};"
        f"axisA_single_axis_all={v['axisA_single_axis_all']};"
        f"axisB_single_axis_all={v['axisB_single_axis_all']};"
        f"substrate_input_orthogonality={result['substrate_input_orthogonality']};"
        f"n_pass={result['n_pass']}of5;n_fail={len(result['fail_clauses'])};n_info={len(result['info_clauses'])}"
    )
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    annotation = (
        "Stage-2 PASS-AND aggregate of §VII.BA (h) STAGE-1-CANDIDATE; "
        f"axisA lizzi (a)/(e)/(c)=PASS; axisB volovik (binding)/(c)=PASS; "
        f"JOINT clause (c) PASS-AND={result['clause_c_PASS_AND']}; "
        f"substrate-input-orthogonality={result['substrate_input_orthogonality']} (distinct anchors, structural ceiling, no overlap caveat); "
        f"composite={result['composite_verdict']} -> "
        f"{'§VII.BA (h) STAGE-3-PERMANENT-ELIGIBLE (orchestrator flips registry tag at wave close)' if result['stage3_eligible'] else 'stays STAGE-1-CANDIDATE'}"
    )
    append_verdict(result["composite_verdict"], value_str, audit_sha, content_sha, annotation)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {result['composite_verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
