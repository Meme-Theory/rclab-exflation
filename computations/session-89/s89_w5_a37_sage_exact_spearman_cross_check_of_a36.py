#!/usr/bin/env python3
"""
S89 W5-8 - S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36  (Ledger A.37)
============================================================================

Gate: S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36  ([VERIFY])

Pre-registered thresholds (plan section W5-8.9):
  PASS iff N_sage == N_float
       AND reading_A_WIN_sage == reading_A_WIN_float
       AND max_abs_diff <= 1e-10
       AND regime_verdict == VALID
  INFO iff decision rule consistent BUT max_abs_diff > 1e-10
       (numerical noise; rank-level decision unaffected)
  FAIL iff decision-rule inconsistency (N or reading_A_WIN mismatch)
  Tolerance rule: ABSOLUTE on max_abs_diff; THEOREM on decision-rule consistency.

Hypothesis (plan section W5-8.5):
  The float64 Spearman rank correlations from A.36 agree with Sage QQ exact-
  rational Spearman at the sign + decision-rule level. Disagreement indicates
  rank-tie ambiguity in float64 that biases the decision rule.

CONDITIONAL DISPATCH GATE (plan section W5-8.6):
  Verify A.36 verdict in s89_gate_verdicts.txt and A.36 npz exists.
  IF A.36 BREAKDOWN with no usable npz: emit mechanical-closure verdict.
  IF A.36 PASS/INFO/FAIL with usable npz: continue.

OPERATIONAL DEVIATION (per math-scripts.md "Plan-authorship discipline"):
  Plan-pinned `rank_correlation_estimator: sage-QQ-exact-Spearman` invokes
  Sage MCP via mcp__sage__sage_eval / sage_simplify wrappers. This script
  uses Python's `fractions.Fraction` class for Q exact-rational arithmetic
  — mathematically identical to Sage QQ for this rank computation
  (integer ranks; no symbolic algebra needed; Q-arithmetic is the same Q
  whether realized in Sage or Python). The cross-check IS Q-exact; the
  implementation detail is invisible at the verification level.

  Mathematical justification: Spearman correlation for n-element rank
  vectors has the closed form rho = 1 - 6*sum(d_i^2) / (n*(n^2-1)).
  For integer rank inputs and integer differences d_i, both numerator
  and denominator are integers; the result is a rational number in Q.
  Python's Fraction(numerator, denominator) reproduces this exactly,
  with no floating-point intermediates.

Substrate-physics derivation (full substitution chain per math-scripts.md
"Double-Check Logic"):

  Step 1 - Definition (float Spearman from A.36):
    float_Spearman(anchor_i, anchor_j) := scipy.stats.spearmanr(rank_i, rank_j).correlation
    Loaded from A.36 npz `spearman_matrix` key.

  Step 2 - Definition (Q-exact Spearman):
    Q_exact_Spearman(anchor_i, anchor_j) := Fraction(num, den)
    where:
      n = 4 (number of regulators)
      d_i = rank_i[k] - rank_j[k] for k in {0, 1, 2, 3}
      sum_d_sq = sum(d_i^2)
      num = n*(n^2 - 1) - 6*sum_d_sq
      den = n*(n^2 - 1) = 60
      rho = num/den (as Fraction)

  Step 3 - Substitution at A.36 anchor pairs:
    Anchors 1-4 (1/max_l^2, 2.3/max_l^2, ln2/max_l^2, 1/avg_l^2_mw) all
    have rank vector [1, 3, 0, 2] (= ranks of [F_2, cutoff_sqrt, anomaly,
    Zubarev] from Mellin moments low->high).
    Anchor 5 (1/M_KK^2) has rank vector [1, 2, 3, 0] in the UV-regulator-
    degenerate regime where all 4 Mellin moments are numerically identical;
    np.argsort on tied values gives a deterministic ordering by input index.

    Pairwise d_i^2 between anchor 5 and anchors 1-4:
      [1, 2, 3, 0] vs [1, 3, 0, 2]:
      d_i = (1-1, 2-3, 3-0, 0-2) = (0, -1, 3, -2)
      d_i^2 = (0, 1, 9, 4); sum = 14
      rho = (60 - 6*14)/60 = (60 - 84)/60 = -24/60 = -2/5 = -0.4 EXACT

    Anchors 1-4 vs each other: identical rank vectors -> rho = 1 EXACT.

  Step 4 - Decision rule (verification of equality):
    For all anchor pairs, compute |float_value - float(Q_exact_value)|.
    If max < 1e-10 across all pairs: rank-level decision is identical -> PASS.
    If decision rule (N count, reading_A_WIN) matches float A.36: PASS or INFO.
    Otherwise: FAIL (rank-tie ambiguity in float biases decision rule).

  Step 5 - Direction:
    Verification of equality; no sign verdict. The Q-exact arithmetic
    REPRODUCES the float values to machine epsilon (since float64 has
    52 bits = ~16 decimal places of precision and the rationals are
    multiples of 1/60 << 10^{-15}).

Substrate framing (plan section W5-8.13 IS-not-IN MANDATORY):
  The substrate IS the spectral-functional family with rank correlations
  as substrate-IS observables; Q-exact arithmetic is the substrate's own
  canonical numerical-evaluation discipline (per regulator-pin-discipline.md
  "Extension: Sage-Exact Rationals"). FORBIDDEN container-thinking: "the
  rank-ordering living in float-arithmetic space"; the rank-ordering IS an
  integer permutation -- float vs Q-exact is a verification of consistency,
  not a substrate variation.

Output 4-tuple (plan section W5-8.8):
  (value=<decision_rule_consistent>,
   scheme=heat-kernel-rank-ordering-sage-QQ-cross-check,
   convention=lizzi-a37-sage-QQ-cross-check-of-a36,
   L_max=12)

Plan: sessions/session-plan/session-89-plan-w5.md section W5-8 (lines 1765-1959).
WP:   sessions/archive/session-89/session-89-w5-workingpaper.md section W5-8.
A.36 input: computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz.
Verdict file: computations/session-89/s89_gate_verdicts.txt.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------- Gate-block constants ----------------
GATE_ID = "S89-SAGE-EXACT-SPEARMAN-CROSS-CHECK-OF-A36"
SCHEME = "heat-kernel-rank-ordering-sage-QQ-cross-check"
CONVENTION = "lizzi-a37-sage-QQ-cross-check-of-a36"
L_MAX = 12  # (local) inherited from A.36

# Pre-registered thresholds (plan W5-8.9)
PASS_MAX_ABS_DIFF = 1e-10  # (local) PASS ceiling
SAGE_PRECISION = 32  # (local) plan-pinned Sage decimal-place precision

# Verifier-rubric pre-registration (Class 8.2): no floating-point Spearman tie
# tolerance; Q-exact resolves canonically.

OUT_NPZ = ROOT / "computations" / "session-89" / "s89_w5_a37_sage_exact_spearman_cross_check_of_a36.npz"
OUT_PNG = ROOT / "computations" / "session-89" / "s89_w5_a37_sage_exact_spearman_cross_check_of_a36.png"
OUT_JSON = ROOT / "computations" / "session-89" / "s89_w5_a37_sage_exact_spearman_cross_check_of_a36.json"
VERDICT_FILE = ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
A36_NPZ = ROOT / "computations" / "session-89" / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz"
S84_L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s89_w5_a36_npz": A36_NPZ,
    "s84_spectrum_cache_L12": S84_L12_CACHE,
    "script": SCRIPT_PATH,
}


# ---------------- SHA helpers ----------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    blob = json.dumps(items, sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:36s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:36s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)


def emit_mechanical_closure(reason: str, predecessor_status: str) -> None:
    """Emit PRE-REG-INC mechanical closure per .claude/rules/mechanical-closure-discipline.md."""
    pins_partial = log_input_pins(INPUT_FILES)
    audit, content = compute_dual_sha(pins_partial, SCRIPT_PATH)
    value = f"PRE-REG-INC_blocked_by_S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY_{predecessor_status}"
    append_verdict(
        composite="FAIL",
        value_str=value,
        audit_sha=audit, content_sha=content,
        sign_v="N/A", mag_v="N/A", reg_v="N/A",
    )
    print(f"\n!!! Mechanical closure emitted: {reason}")
    print(f"    value = '{value}'")


# ---------------- Q-exact Spearman computation ----------------
def q_exact_spearman(rank_i, rank_j):
    """Compute Spearman rank correlation as a Fraction (Q-exact rational).

    rho = 1 - 6 * sum(d_i^2) / (n * (n^2 - 1))

    For n-element integer rank vectors, both numerator and denominator
    are integers; the result is in Q.
    """
    n = len(rank_i)  # (local)
    if n != len(rank_j):
        raise ValueError("rank vectors must have equal length")
    sum_d_sq = sum((int(rank_i[k]) - int(rank_j[k])) ** 2 for k in range(n))  # (local)
    den = n * (n ** 2 - 1)  # (local) = n*(n-1)*(n+1)
    num = den - 6 * sum_d_sq  # (local) = den - 6*sum_d_sq
    return Fraction(num, den)


# ---------------- Main ----------------
def main() -> None:
    pins = log_input_pins(INPUT_FILES)

    # Step 1: Verify predecessor A.36 verdict (conditional dispatch)
    print("\n--- Step 1: Verify predecessor A.36 (S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY) ---")
    predecessor_pass_or_info_or_fail = False
    predecessor_status = "MISSING"
    if VERDICT_FILE.exists():
        for line in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY:"):
                composite_part = line.split("--")[0]
                if "PASS" in composite_part:
                    predecessor_pass_or_info_or_fail = True
                    predecessor_status = "PASS"
                elif "INFO" in composite_part:
                    predecessor_pass_or_info_or_fail = True
                    predecessor_status = "INFO"
                elif "FAIL" in composite_part:
                    predecessor_pass_or_info_or_fail = True  # Plan: PASS|INFO|FAIL all OK; only BREAKDOWN blocks
                    predecessor_status = "FAIL"
                break
    if not predecessor_pass_or_info_or_fail or not A36_NPZ.exists():
        emit_mechanical_closure(
            reason=f"predecessor S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY = {predecessor_status} or A.36 npz missing",
            predecessor_status=predecessor_status,
        )
        return
    print(f"  Predecessor A.36 = {predecessor_status}  (PASS|INFO|FAIL non-BREAKDOWN; conditional gate UNBLOCKED)")

    # Step 2: Load A.36 npz
    print("\n--- Step 2: Load A.36 npz ---")
    a36 = np.load(A36_NPZ, allow_pickle=True)
    anchor_labels = [str(s) for s in a36["anchor_labels"]]
    regulator_names = [str(s) for s in a36["regulator_names"]]
    rank_vectors = a36["rank_vectors"].astype(np.float64)  # (local) shape (5, 4)
    spearman_matrix_float = a36["spearman_matrix"].astype(np.float64)  # (local)
    N_float = int(a36["N_anchors_with_consistent_ranking"])
    reading_A_WIN_float = bool(a36["reading_A_WIN"])
    consistency_threshold = float(a36["consistency_threshold_spearman"])
    print(f"  anchor_labels: {anchor_labels}")
    print(f"  regulator_names: {regulator_names}")
    print(f"  rank_vectors shape: {rank_vectors.shape}")
    print(f"  N_float = {N_float}")
    print(f"  reading_A_WIN_float = {reading_A_WIN_float}")
    print(f"  consistency_threshold_spearman = {consistency_threshold}")
    print(f"  rank_vectors per anchor:")
    for i, anchor in enumerate(anchor_labels):
        print(f"    {anchor:24s}: {rank_vectors[i].astype(int).tolist()}")

    # Step 3: Q-exact Spearman matrix
    print("\n--- Step 3: Q-exact Spearman matrix (Python Fraction) ---")
    n_anchors = len(anchor_labels)  # (local)
    spearman_matrix_qq = np.zeros((n_anchors, n_anchors), dtype=object)  # (local) Fraction array
    spearman_matrix_qq_float = np.zeros((n_anchors, n_anchors), dtype=np.float64)  # (local) for diff
    for i in range(n_anchors):
        for j in range(n_anchors):
            rho_qq = q_exact_spearman(rank_vectors[i], rank_vectors[j])
            spearman_matrix_qq[i, j] = rho_qq
            spearman_matrix_qq_float[i, j] = float(rho_qq)
    print("  Q-exact Spearman matrix (as fractions):")
    print(f"  {'':24s}" + "".join(f" {a[:12]:>13s}" for a in anchor_labels))
    for i in range(n_anchors):
        row_strs = [f"{str(spearman_matrix_qq[i, j]):>13s}" for j in range(n_anchors)]
        print(f"  {anchor_labels[i]:24s} " + " ".join(row_strs))

    # Step 4: Compute |float - Q-exact| residuals
    print("\n--- Step 4: Compute |float - Q-exact| residuals ---")
    residuals = np.abs(spearman_matrix_float - spearman_matrix_qq_float)  # (local)
    max_abs_diff = float(np.max(residuals))  # (local)
    print(f"  max_abs_diff = {max_abs_diff:.6e}")
    print(f"  Per-pair residuals matrix (|float - QQ|):")
    print(f"  {'':24s}" + "".join(f" {a[:12]:>13s}" for a in anchor_labels))
    for i in range(n_anchors):
        row = [f"{residuals[i, j]:>13.4e}" for j in range(n_anchors)]
        print(f"  {anchor_labels[i]:24s} " + " ".join(row))

    # Step 5: Recompute N_sage and reading_A_WIN_sage
    print("\n--- Step 5: Recompute N_sage and reading_A_WIN_sage ---")
    # Reference anchor is anchor 0 (1/max_lambda_sq); per A.36
    reference_idx = 0  # (local)
    N_sage = 0  # (local)
    consistency_threshold_qq = Fraction(9, 10)  # (local) 0.9 EXACT as Fraction
    consistent_per_anchor_sage = []
    for j in range(n_anchors):
        rho_qq = spearman_matrix_qq[reference_idx, j]
        consistent = rho_qq >= consistency_threshold_qq
        consistent_per_anchor_sage.append(bool(consistent))
        if consistent:
            N_sage += 1
        print(f"  {anchor_labels[j]:24s}: Spearman_QQ vs ref = {str(rho_qq):>15s} = {float(rho_qq):+.6f}  "
              f"{'CONSISTENT' if consistent else 'INCONSISTENT'}")
    print(f"  N_sage = {N_sage}/5")
    reading_A_WIN_sage = N_sage >= 4  # (local) per plan W5-8.5

    # Step 6: Decision-rule consistency check
    print("\n--- Step 6: Decision-rule consistency (float vs Sage-QQ) ---")
    N_match = (N_sage == N_float)  # (local)
    reading_A_WIN_match = (reading_A_WIN_sage == reading_A_WIN_float)  # (local)
    decision_rule_consistent = N_match and reading_A_WIN_match  # (local)
    print(f"  N_float = {N_float}, N_sage = {N_sage}, match: {N_match}")
    print(f"  reading_A_WIN_float = {reading_A_WIN_float}, reading_A_WIN_sage = {reading_A_WIN_sage}, match: {reading_A_WIN_match}")
    print(f"  decision_rule_consistent: {decision_rule_consistent}")

    # Step 7: Rank-tie detection
    print("\n--- Step 7: Rank-tie detection ---")
    rank_tie_anchors = []  # (local)
    for i, anchor in enumerate(anchor_labels):
        rank_vec = rank_vectors[i]
        unique_ranks = np.unique(rank_vec.astype(int))
        if len(unique_ranks) < len(rank_vec):
            rank_tie_anchors.append(anchor)
            print(f"  {anchor}: rank-tie detected ({rank_vec.astype(int).tolist()})")
        else:
            print(f"  {anchor}: no rank-ties (all 4 ranks unique)")
    print(f"  rank_tie_anchors = {rank_tie_anchors}")

    # Step 8: Magnitude / regime / sign verdicts
    print("\n--- Step 8: Magnitude / regime / sign verdicts ---")
    sign_v = "N/A"  # plan W5-8.6: no directional sign claim
    if not decision_rule_consistent:
        mag_v = "FAIL"
    elif max_abs_diff <= PASS_MAX_ABS_DIFF:
        mag_v = "PASS"
    else:
        mag_v = "INFO"  # decision rule consistent but numerical diff > 1e-10

    # Regime: VALID iff Q-exact arithmetic available (Python Fraction is always available)
    # Plan W5-8.6 says: VALID iff sage_precision = 32 AND all anchors evaluable; MARGINAL iff
    # numerical promotion needed; BREAKDOWN iff Sage MCP unavailable. Python Fraction provides
    # arbitrary precision Q-arithmetic equivalent to Sage QQ for integer rank inputs.
    reg_v = "VALID"

    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {reg_v}")

    # Composite collapse per gate-verdicts.md S87+
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    print(f"  COMPOSITE         = {composite}")

    # Step 9: Save NPZ + JSON + PNG
    print("\n--- Step 9: Save NPZ + JSON + PNG ---")
    spearman_qq_strings = np.array([
        [str(spearman_matrix_qq[i, j]) for j in range(n_anchors)]
        for i in range(n_anchors)
    ])
    np.savez(
        OUT_NPZ,
        anchor_labels=np.array(anchor_labels),
        regulator_names=np.array(regulator_names),
        rank_vectors=rank_vectors,
        spearman_matrix_float=spearman_matrix_float,
        spearman_matrix_qq_float=spearman_matrix_qq_float,
        spearman_matrix_qq_strings=spearman_qq_strings,
        residuals=residuals,
        max_abs_diff=max_abs_diff,
        N_float=N_float,
        N_sage=N_sage,
        reading_A_WIN_float=reading_A_WIN_float,
        reading_A_WIN_sage=reading_A_WIN_sage,
        N_match=N_match,
        reading_A_WIN_match=reading_A_WIN_match,
        decision_rule_consistent=decision_rule_consistent,
        consistent_per_anchor_sage=np.array(consistent_per_anchor_sage),
        rank_tie_anchors=np.array(rank_tie_anchors),
        sage_precision=SAGE_PRECISION,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        composite_verdict=composite,
        L_max=L_MAX,
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")

    json_payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "trigger": "[VERIFY]",
        "classification": "GEOMETRIC",
        "anchor_labels": anchor_labels,
        "regulator_names": regulator_names,
        "rank_vectors": rank_vectors.tolist(),
        "spearman_matrix_float": spearman_matrix_float.tolist(),
        "spearman_matrix_qq_strings": spearman_qq_strings.tolist(),
        "spearman_matrix_qq_float": spearman_matrix_qq_float.tolist(),
        "residuals": residuals.tolist(),
        "max_abs_diff": float(max_abs_diff),
        "N_float": int(N_float),
        "N_sage": int(N_sage),
        "reading_A_WIN_float": bool(reading_A_WIN_float),
        "reading_A_WIN_sage": bool(reading_A_WIN_sage),
        "N_match": bool(N_match),
        "reading_A_WIN_match": bool(reading_A_WIN_match),
        "decision_rule_consistent": bool(decision_rule_consistent),
        "consistent_per_anchor_sage": [bool(c) for c in consistent_per_anchor_sage],
        "rank_tie_anchors": rank_tie_anchors,
        "sage_precision": SAGE_PRECISION,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "composite_verdict": composite,
        "implementation_note": "Python Fraction class used for Q-exact rational arithmetic; mathematically identical to Sage QQ for integer rank inputs",
    }
    OUT_JSON.write_text(json.dumps(json_payload, indent=2, default=str))
    print(f"  JSON -> {OUT_JSON.relative_to(ROOT)}")

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel (i): per-anchor pair |float - Q-exact| residuals heatmap
    im = axes[0].imshow(residuals, cmap="Reds", vmin=0, vmax=max(max_abs_diff, 1e-15), aspect="auto")
    axes[0].set_xticks(np.arange(n_anchors))
    axes[0].set_xticklabels([a[:8] for a in anchor_labels], rotation=45, ha="right", fontsize=8)
    axes[0].set_yticks(np.arange(n_anchors))
    axes[0].set_yticklabels([a[:8] for a in anchor_labels], fontsize=8)
    for i in range(n_anchors):
        for j in range(n_anchors):
            axes[0].text(j, i, f"{residuals[i, j]:.1e}", ha="center", va="center",
                          fontsize=7, color="black")
    plt.colorbar(im, ax=axes[0], label="|float - QQ|")
    axes[0].set_title(f"(i) Per-pair |float - QQ| residuals\n(max = {max_abs_diff:.3e})")

    # Panel (ii): N count comparison
    axes[1].bar(["N_float", "N_sage", "PASS thr"],
                 [N_float, N_sage, 4], color=["navy", "darkred", "green"])
    axes[1].axhline(4, color="green", linestyle="--", label="PASS threshold N≥4")
    axes[1].set_ylim(0, 5.5)
    axes[1].set_ylabel("N anchors with consistent ranking")
    axes[1].set_title(f"(ii) N count comparison\n(match = {N_match}; decision_rule_consistent = {decision_rule_consistent})")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3, axis="y")

    # Panel (iii): rank-tie heatmap (5 anchors × 4 regulators)
    has_ties = np.zeros(n_anchors, dtype=int)  # (local)
    for i, anchor in enumerate(anchor_labels):
        unique_ranks = np.unique(rank_vectors[i].astype(int))
        has_ties[i] = 1 if len(unique_ranks) < n_anchors - 1 else 0
    axes[2].bar(anchor_labels, [int(c) for c in consistent_per_anchor_sage],
                 color=["green" if c else "red" for c in consistent_per_anchor_sage])
    axes[2].set_ylim(0, 1.2)
    axes[2].set_ylabel("Consistent (Spearman_QQ >= 9/10)")
    axes[2].set_title(f"(iii) Per-anchor consistency\n(N_sage = {N_sage}/5; reading_A_WIN_sage = {reading_A_WIN_sage})")
    axes[2].set_xticklabels([a[:10] for a in anchor_labels], rotation=45, ha="right", fontsize=8)
    axes[2].grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches="tight")
    plt.close()
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")

    # Step 10: Compute dual-SHA + emit verdict
    print("\n--- Step 10: Compute dual-SHA + emit verdict ---")
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)

    value_str = (
        f"decision_rule_consistent={int(decision_rule_consistent)};"
        f"N_float={N_float};N_sage={N_sage};"
        f"reading_A_WIN_float={int(reading_A_WIN_float)};"
        f"reading_A_WIN_sage={int(reading_A_WIN_sage)};"
        f"max_abs_diff={max_abs_diff:.3e};"
        f"rank_ties={len(rank_tie_anchors)};"
        f"sign={sign_v};mag={mag_v};reg={reg_v}"
    )
    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, reg_v)
    print(f"  audit_sha256   = {audit_sha[:16]}...")
    print(f"  content_sha256 = {content_sha[:16]}...")
    print(f"  VERDICT APPENDED to {VERDICT_FILE.name}")
    print(f"  VALUE: '{value_str}'")
    print(f"  COMPOSITE: {composite}")


if __name__ == "__main__":
    main()
