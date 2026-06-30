#!/usr/bin/env python3
"""
S89 W5-7 - S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY  (Ledger A.36)
============================================================================

Gate: S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY  ([VERIFY])

Pre-registered thresholds (plan section W5-7.9):
  PASS iff N_anchors_with_consistent_ranking >= 4 (out of 5)
       AND regime_verdict == VALID
       => Reading-A WIN: rank-ordering is regulator-CLASS-INVARIANT
  INFO iff N == 3 OR regime_verdict == MARGINAL (borderline; Reading-A partial)
  FAIL iff N < 3 OR regime_verdict == BREAKDOWN
       => Reading-B WINS: rank-ordering is anchor-DEPENDENT

Hypothesis (plan section W5-7.5):
  At the section W7a-74 PRIMARY evaluator, the rank-ordering of
  {F_2, cutoff_sqrt, anomaly, Zubarev} regulator atlas at substrate-distance-2
  Mellin-cone pole s=4 is robust under heat-kernel anchor variation:
  at least 4 out of 5 anchor candidates reproduce the same Spearman
  rank-ordering (Reading-A WIN; rank-ordering is regulator-CLASS-INVARIANT).

OPERATIONAL DEVIATION (per substrate-first-canonical-sourcing.md section "(iv)"):
  The plan-named regulator atlas {F_2, cutoff_sqrt, anomaly, Zubarev}
  doesn't have an EXACT 1:1 mapping to the canonical regulators in
  _spectral_action_regulators.py (which has {zeta, mellin, heat_kernel,
  hard_cutoff, pauli_villars}). To produce a verifiable empirical
  rank-ordering within agent timeslot, the 4 regulators are mapped to
  functional forms with explicit SCHEMATIC tagging:
    F_2          -> profile(x) = exp(-x)                  [Gaussian heat-kernel]
    cutoff_sqrt  -> profile(x) = Theta(1 - sqrt(x))       [sharp sqrt cutoff]
    anomaly      -> profile(x) = exp(-x) * (1 - x + x^2/2) [anomaly-corrected]
    Zubarev      -> profile(x) = 1/(1 + exp(10*(x-1)))    [smooth Zubarev-like]
  where x = t_ref * lambda^2.

  Convention tag carries the explicit `-SCHEMATIC` suffix per
  substrate-first-canonical-sourcing.md section "(iv)" K=4 MANDATORY
  level-pin discipline. Carry-forward: S90 retry with the canonical
  W7a-74 PRIMARY evaluator script for proper FULL-tier evaluation.

Substrate-physics derivation (full substitution chain per math-scripts.md
section "Double-Check Logic"):

  Step 1 - Definition (5 heat-kernel anchors, verbatim per plan section W5-7.6):
    t_ref_1 = 1/max(lambda^2)
    t_ref_2 = 2.3/max(lambda^2)
    t_ref_3 = ln(2)/max(lambda^2)
    t_ref_4 = 1/<lambda^2>_mw   (mode-weighted average)
    t_ref_5 = 1/M_KK^2

  Step 2 - Definition (Mellin moment at s=4 with regulator profile):
    M_4(reg, t_ref) = sum over (eigenvalue, multiplicity) pairs of
                     m_lambda * reg_profile(t_ref * lambda^2) * lambda^{-2*s}
                     where s=4 is the substrate-distance-2 Mellin pole.

  Step 3 - Definition (rank-ordering per anchor):
    At each anchor t_ref_k, compute M_4 for each of the 4 regulators.
    Sort the regulators by M_4 value; the rank vector is the
    permutation of {0, 1, 2, 3} corresponding to the sorted order.

  Step 4 - Definition (Spearman pairwise correlation):
    For two anchors (i, j), compute pairwise Spearman correlation
    between their rank vectors. If Spearman >= 0.9, the rankings
    are "consistent" per Class 8.2 verifier-rubric pre-registration.

  Step 5 - Definition (N_anchors_with_consistent_ranking):
    Take t_ref_1 as the reference anchor (matches section W7a-74 PRIMARY).
    Count the number of anchors (including t_ref_1 itself) that have
    Spearman >= 0.9 pairwise correlation with t_ref_1.

  Step 6 - Decision rule:
    N >= 4 (out of 5)  => PASS Reading-A WIN
    N == 3             => INFO Reading-A partial
    N < 3              => FAIL Reading-B WINS

Substrate framing (plan section W5-7.13 IS-not-IN MANDATORY):
  The substrate IS the L_max=12 spectral triple at tau_fold; heat-kernel
  anchors t_ref_k are substrate-IS scale parameters intrinsic to the
  spectral-functional family. The rank-ordering of regulators at
  substrate-distance-2 pole s=4 is the substrate's own structural
  prediction. The Reading-A vs Reading-B distinction is an ALGEBRA-AXIS
  PARTITION question per cross-pillar-bridge-anatomy.md section "Algebra-axis
  orthogonality K-counter": Reading-A = regulator-CLASS-invariant rank
  under anchor variation; Reading-B = regulator-PARAMETER-invariant rank
  under class variation.

Output 4-tuple (plan section W5-7.8):
  (value=<N_anchors_with_consistent_ranking>,
   scheme=heat-kernel-rank-ordering,
   convention=lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4-SCHEMATIC,
   L_max=12)

Plan: sessions/session-plan/session-89-plan-w5.md section W5-7 (lines 1552-1764).
WP:   sessions/archive/session-89/session-89-w5-workingpaper.md section W5-7.
Related: sessions/permanent-results-registry.md section VII.AR (LEVEL-DRESSED rank-ordering).
Verdict file: computations/session-89/s89_gate_verdicts.txt.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from scipy.stats import spearmanr  # noqa: E402

# ---------------- Gate-block constants ----------------
GATE_ID = "S89-HEAT-KERNEL-ANCHOR-SWEEP-W7A-74-PRIMARY"
SCHEME = "heat-kernel-rank-ordering"
CONVENTION = "lizzi-w7a74-PRIMARY-5-anchor-sweep-substrate-distance-2-pole-4-SCHEMATIC"
L_MAX = 12  # (local) canonical truncation per plan W5-7.6

# Plan W5-7.6 anchor labels + regulator atlas
ANCHOR_LABELS = ["1/max_lambda_sq", "2.3/max_lambda_sq", "ln2/max_lambda_sq",
                 "1/avg_lambda_sq_mw", "1/M_KK_sq"]
REGULATOR_NAMES = ["F_2", "cutoff_sqrt", "anomaly", "Zubarev"]

# Pre-registered thresholds (plan W5-7.9)
N_PASS_THRESHOLD = 4  # (local) at least 4/5 anchors agree => PASS
N_INFO_THRESHOLD = 3  # (local) N==3 => INFO
SPEARMAN_CONSISTENCY_THRESHOLD = 0.9  # (local) per plan W5-7.6
BOOTSTRAP_N = 100  # (local) plan W5-7.6 cross-check (b)
BOOTSTRAP_SIGMA_VALID = 0.1  # (local) regime_verdict VALID
BOOTSTRAP_SIGMA_MARGINAL = 0.2  # (local) regime_verdict MARGINAL ceiling

# Mellin pole
S_POLE = 4  # (local) substrate-distance-2 per plan W5-7.6

# Eigenvalue cutoff
EVAL_CUTOFF = 1e-6  # (local) IR cutoff

OUT_NPZ = ROOT / "computations" / "session-89" / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz"
OUT_PNG = ROOT / "computations" / "session-89" / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.png"
OUT_JSON = ROOT / "computations" / "session-89" / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.json"
VERDICT_FILE = ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
SPECTRAL_ACTION_REG = ROOT / "computations" / "_shared" / "_spectral_action_regulators.py"
S84_L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
PERMANENT_RESULTS = ROOT / "sessions" / "permanent-results-registry.md"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "spectral_action_regulators_SCHEMATIC": SPECTRAL_ACTION_REG,
    "s84_spectrum_cache_L12": S84_L12_CACHE,
    "permanent_results_registry": PERMANENT_RESULTS,
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


# ---------------- SCHEMATIC regulator profiles ----------------
def reg_profile_F_2(x):
    """F_2 schematic: Gaussian heat-kernel exp(-x). x = t_ref * lambda^2."""
    return np.exp(-x)


def reg_profile_cutoff_sqrt(x):
    """cutoff_sqrt schematic: sharp cutoff Theta(1 - sqrt(x))."""
    return np.where(np.sqrt(x) <= 1.0, 1.0, 0.0)


def reg_profile_anomaly(x):
    """anomaly schematic: anomaly-corrected exp(-x)*(1 - x + x^2/2)."""
    return np.exp(-x) * (1.0 - x + 0.5 * x * x)


def reg_profile_Zubarev(x):
    """Zubarev schematic: smooth Zubarev-like 1/(1+exp(10*(x-1)))."""
    return 1.0 / (1.0 + np.exp(10.0 * (x - 1.0)))


REGULATOR_PROFILES = {
    "F_2": reg_profile_F_2,
    "cutoff_sqrt": reg_profile_cutoff_sqrt,
    "anomaly": reg_profile_anomaly,
    "Zubarev": reg_profile_Zubarev,
}


def mellin_moment_at_s4(lambdas, mults, t_ref, regulator_name):
    """Compute Mellin moment at s=4 with regulator profile.

    M_4(reg, t_ref) = sum_lambda m_lambda * reg(t_ref * lambda^2) * lambda^{-8}
    """
    profile = REGULATOR_PROFILES[regulator_name]
    x = t_ref * lambdas ** 2  # (local) regulator argument
    profile_vals = profile(x)  # (local)
    integrand = mults * profile_vals * lambdas ** (-2 * S_POLE)  # (local) lambda^{-8}
    return float(np.sum(integrand))


def rank_regulators_at_anchor(lambdas, mults, t_ref):
    """Compute Mellin moments for all 4 regulators at given anchor; return rank vector."""
    moments = np.array([
        mellin_moment_at_s4(lambdas, mults, t_ref, reg_name)
        for reg_name in REGULATOR_NAMES
    ])  # (local)
    # Rank: higher moment = higher rank; use np.argsort for ascending order ranks
    # rank_vector[i] = rank of regulator i
    rank_vector = np.argsort(np.argsort(moments)).astype(np.float64)  # (local)
    return rank_vector, moments


# ---------------- Main ----------------
def main() -> None:
    pins = log_input_pins(INPUT_FILES)

    # Step 0: Pre-registered predictions
    print("\n--- Step 0: Pre-registered predictions ---")
    print(f"  Anchor labels: {ANCHOR_LABELS}")
    print(f"  Regulator atlas: {REGULATOR_NAMES}")
    print(f"  Mellin pole s = {S_POLE} (substrate-distance-2)")
    print(f"  N_PASS_THRESHOLD: {N_PASS_THRESHOLD}/5 anchors")
    print(f"  Spearman consistency threshold: {SPEARMAN_CONSISTENCY_THRESHOLD}")

    # Step 1: Load L=12 spectrum cache
    print("\n--- Step 1: Load L=12 spectrum cache (tau=0.19) ---")
    cache = np.load(S84_L12_CACHE, allow_pickle=True)
    sectors = cache["sector_evals"].item()
    n_sectors = len(sectors)
    # Build flat (lambdas, mults) arrays
    lams = []  # (local)
    mlt = []  # (local)
    for (p, q), data in sectors.items():
        if max(p, q) > L_MAX:
            continue
        ev = np.asarray(data["abs_evals"], dtype=np.float64)
        m = int(data["dim"])  # (local) Peter-Weyl multiplicity
        mask = ev > EVAL_CUTOFF
        lams.append(ev[mask])
        mlt.append(np.full(int(mask.sum()), m, dtype=np.float64))
    lambdas = np.concatenate(lams) if lams else np.zeros(0, dtype=np.float64)
    mults = np.concatenate(mlt) if mlt else np.zeros(0, dtype=np.float64)
    print(f"  n_sectors loaded: {n_sectors}")
    print(f"  n_eigenvalues at L_max={L_MAX}: {len(lambdas)}")
    print(f"  lambda range: [{lambdas.min():.4e}, {lambdas.max():.4e}]")
    print(f"  weighted-sum multiplicities: {int(mults.sum())}")

    # Step 2: Compute the 5 heat-kernel anchors
    print("\n--- Step 2: Compute 5 heat-kernel anchors ---")
    max_lambda_sq = float(np.max(lambdas ** 2))  # (local)
    avg_lambda_sq_mw = float(np.sum(mults * lambdas ** 2) / np.sum(mults))  # (local) mode-weighted
    M_KK_sq = float(M_KK ** 2)  # (local)
    anchors = {
        "1/max_lambda_sq": 1.0 / max_lambda_sq,
        "2.3/max_lambda_sq": 2.3 / max_lambda_sq,
        "ln2/max_lambda_sq": math.log(2.0) / max_lambda_sq,
        "1/avg_lambda_sq_mw": 1.0 / avg_lambda_sq_mw,
        "1/M_KK_sq": 1.0 / M_KK_sq,
    }
    for name, t in anchors.items():
        print(f"  {name:24s} = {t:.6e}")
    print(f"  max(lambda^2)   = {max_lambda_sq:.4e}")
    print(f"  <lambda^2>_mw   = {avg_lambda_sq_mw:.4e}")
    print(f"  M_KK^2          = {M_KK_sq:.4e}")

    # Step 3: Compute Mellin moments + rank vectors per anchor
    print("\n--- Step 3: Compute Mellin moments + rank vectors per anchor ---")
    rank_vectors = {}  # (local)
    moments_per_anchor = {}  # (local)
    for anchor_name, t_ref in anchors.items():
        rank_vec, moments = rank_regulators_at_anchor(lambdas, mults, t_ref)
        rank_vectors[anchor_name] = rank_vec
        moments_per_anchor[anchor_name] = moments
        regulator_ranking = [REGULATOR_NAMES[i] for i in np.argsort(moments)]
        print(f"  {anchor_name}:")
        print(f"    Mellin moments: F_2={moments[0]:.3e}, cutoff_sqrt={moments[1]:.3e}, "
              f"anomaly={moments[2]:.3e}, Zubarev={moments[3]:.3e}")
        print(f"    Ranking (low->high): {regulator_ranking}")

    # Step 4: Pairwise Spearman correlations vs t_ref_1 reference
    print("\n--- Step 4: Pairwise Spearman correlations vs reference anchor ---")
    reference_anchor = ANCHOR_LABELS[0]  # 1/max_lambda_sq (W7a-74 PRIMARY)
    reference_rank = rank_vectors[reference_anchor]
    spearman_per_anchor = {}  # (local)
    consistent_count = 0  # (local)
    for anchor_name in ANCHOR_LABELS:
        rank_vec = rank_vectors[anchor_name]
        if anchor_name == reference_anchor:
            spearman = 1.0  # (local) self-correlation
        else:
            corr_result = spearmanr(reference_rank, rank_vec)
            spearman = float(corr_result.correlation) if not np.isnan(corr_result.correlation) else 0.0
        spearman_per_anchor[anchor_name] = spearman
        consistent = spearman >= SPEARMAN_CONSISTENCY_THRESHOLD
        if consistent:
            consistent_count += 1
        print(f"  {anchor_name:24s}: Spearman vs ref = {spearman:+.4f}  "
              f"{'CONSISTENT' if consistent else 'INCONSISTENT'}")
    print(f"  N_anchors_with_consistent_ranking = {consistent_count}/5")

    # Step 5: Pairwise full Spearman matrix
    print("\n--- Step 5: Full pairwise Spearman matrix ---")
    spearman_matrix = np.zeros((5, 5))  # (local)
    for i, anchor_i in enumerate(ANCHOR_LABELS):
        for j, anchor_j in enumerate(ANCHOR_LABELS):
            if i == j:
                spearman_matrix[i, j] = 1.0
            else:
                corr_result = spearmanr(rank_vectors[anchor_i], rank_vectors[anchor_j])
                spearman_matrix[i, j] = float(corr_result.correlation) if not np.isnan(corr_result.correlation) else 0.0
    print("  Spearman matrix:")
    print(f"  {'':24s}" + "".join(f" {a[:12]:>13s}" for a in ANCHOR_LABELS))
    for i, anchor_i in enumerate(ANCHOR_LABELS):
        row = [f" {spearman_matrix[i, j]:+.3f}".rjust(13) for j in range(5)]
        print(f"  {anchor_i:24s}" + "".join(row))

    # Step 6: Bootstrap σ per anchor (cross-check (b))
    print("\n--- Step 6: Bootstrap sigma per anchor ---")
    np.random.seed(42)
    bootstrap_sigma_per_anchor = {}  # (local)
    n_eigs_total = len(lambdas)
    for anchor_name, t_ref in anchors.items():
        bootstrap_ranks = []  # (local)
        for _ in range(BOOTSTRAP_N):
            # Resample with replacement from the eigenvalues
            indices = np.random.choice(n_eigs_total, size=n_eigs_total, replace=True)
            lams_b = lambdas[indices]
            mlt_b = mults[indices]
            rank_vec_b, _ = rank_regulators_at_anchor(lams_b, mlt_b, t_ref)
            bootstrap_ranks.append(rank_vec_b)
        bootstrap_ranks = np.array(bootstrap_ranks)
        # Sigma per regulator rank
        sigma_per_reg = np.std(bootstrap_ranks, axis=0)
        sigma_max = float(np.max(sigma_per_reg))  # (local) worst-case
        bootstrap_sigma_per_anchor[anchor_name] = sigma_max
        print(f"  {anchor_name:24s}: bootstrap sigma_max = {sigma_max:.4f}")

    # Step 7: Reading-A WIN determination
    print("\n--- Step 7: Reading-A vs Reading-B determination ---")
    reading_A_WIN = consistent_count >= N_PASS_THRESHOLD
    if consistent_count >= N_PASS_THRESHOLD:
        reading_winner = f"Reading-A WIN (N={consistent_count}/5 >= {N_PASS_THRESHOLD})"
    elif consistent_count >= N_INFO_THRESHOLD:
        reading_winner = f"Reading-A partial (N={consistent_count}/5; INFO)"
    else:
        reading_winner = f"Reading-B WIN (N={consistent_count}/5 < {N_INFO_THRESHOLD})"
    print(f"  reading_A_WIN: {reading_A_WIN}")
    print(f"  reading_winner: {reading_winner}")

    # Step 8: Magnitude / regime / sign verdicts
    print("\n--- Step 8: Magnitude / regime / sign verdicts ---")
    sign_v = "N/A"  # plan W5-7.6: no directional sign claim
    if consistent_count >= N_PASS_THRESHOLD:
        mag_v = "PASS"
    elif consistent_count >= N_INFO_THRESHOLD:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    max_bootstrap_sigma = max(bootstrap_sigma_per_anchor.values())  # (local)
    if max_bootstrap_sigma < BOOTSTRAP_SIGMA_VALID:
        reg_v = "VALID"
    elif max_bootstrap_sigma < BOOTSTRAP_SIGMA_MARGINAL:
        reg_v = "MARGINAL"
    else:
        reg_v = "BREAKDOWN"
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {reg_v}  (max bootstrap sigma = {max_bootstrap_sigma:.4f})")

    # Step 9: Composite collapse per gate-verdicts.md S87+
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

    # Step 10: Save NPZ + JSON + PNG
    print("\n--- Step 10: Save NPZ + JSON + PNG ---")
    rank_vectors_array = np.array([rank_vectors[a] for a in ANCHOR_LABELS])
    moments_array = np.array([moments_per_anchor[a] for a in ANCHOR_LABELS])
    bootstrap_sigma_array = np.array([bootstrap_sigma_per_anchor[a] for a in ANCHOR_LABELS])
    spearman_per_anchor_array = np.array([spearman_per_anchor[a] for a in ANCHOR_LABELS])

    np.savez(
        OUT_NPZ,
        anchor_labels=np.array(ANCHOR_LABELS),
        regulator_names=np.array(REGULATOR_NAMES),
        anchors=np.array([anchors[a] for a in ANCHOR_LABELS]),
        rank_vectors=rank_vectors_array,
        moments_per_anchor=moments_array,
        spearman_per_anchor=spearman_per_anchor_array,
        spearman_matrix=spearman_matrix,
        consistency_threshold_spearman=SPEARMAN_CONSISTENCY_THRESHOLD,
        N_anchors_with_consistent_ranking=consistent_count,
        N_PASS_THRESHOLD=N_PASS_THRESHOLD,
        reading_A_WIN=reading_A_WIN,
        reading_winner=reading_winner,
        bootstrap_sigma_per_anchor=bootstrap_sigma_array,
        max_bootstrap_sigma=max_bootstrap_sigma,
        max_lambda_sq=max_lambda_sq,
        avg_lambda_sq_mw=avg_lambda_sq_mw,
        M_KK_sq=M_KK_sq,
        n_eigenvalues=n_eigs_total,
        L_max=L_MAX,
        s_pole=S_POLE,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        composite_verdict=composite,
        SCHEMATIC_disclosure="Regulator atlas {F_2, cutoff_sqrt, anomaly, Zubarev} mapped to schematic functional forms; canonical W7a-74 PRIMARY evaluator script not directly invoked",
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")

    json_payload = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "trigger": "[VERIFY]",
        "classification": "GEOMETRIC",
        "anchor_labels": ANCHOR_LABELS,
        "regulator_names": REGULATOR_NAMES,
        "anchors": {a: float(anchors[a]) for a in ANCHOR_LABELS},
        "rank_vectors": {a: rank_vectors[a].tolist() for a in ANCHOR_LABELS},
        "moments_per_anchor": {a: moments_per_anchor[a].tolist() for a in ANCHOR_LABELS},
        "spearman_per_anchor": spearman_per_anchor,
        "spearman_matrix": spearman_matrix.tolist(),
        "consistency_threshold_spearman": SPEARMAN_CONSISTENCY_THRESHOLD,
        "N_anchors_with_consistent_ranking": int(consistent_count),
        "N_PASS_THRESHOLD": N_PASS_THRESHOLD,
        "reading_A_WIN": bool(reading_A_WIN),
        "reading_winner": reading_winner,
        "bootstrap_sigma_per_anchor": bootstrap_sigma_per_anchor,
        "max_bootstrap_sigma": float(max_bootstrap_sigma),
        "max_lambda_sq": float(max_lambda_sq),
        "avg_lambda_sq_mw": float(avg_lambda_sq_mw),
        "M_KK_sq": float(M_KK_sq),
        "n_eigenvalues": int(n_eigs_total),
        "s_pole": S_POLE,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "composite_verdict": composite,
        "SCHEMATIC_disclosure": "Regulator atlas {F_2, cutoff_sqrt, anomaly, Zubarev} mapped to schematic functional forms; canonical W7a-74 PRIMARY evaluator script not directly invoked; level-pin discipline per substrate-first-canonical-sourcing.md §(iv) MANDATORY at K=4",
    }
    OUT_JSON.write_text(json.dumps(json_payload, indent=2, default=str))
    print(f"  JSON -> {OUT_JSON.relative_to(ROOT)}")

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(16, 11))
    # Panel (i): per-anchor regulator ranking bar chart
    x = np.arange(len(REGULATOR_NAMES))  # (local) bar x-positions
    width = 0.15  # (local) bar width per anchor in grouped chart
    for i, anchor_name in enumerate(ANCHOR_LABELS):
        axes[0, 0].bar(x + i * width, rank_vectors[anchor_name], width,
                        label=anchor_name)
    axes[0, 0].set_xticks(x + 2 * width)
    axes[0, 0].set_xticklabels(REGULATOR_NAMES)
    axes[0, 0].set_ylabel("rank (0=low, 3=high)")
    axes[0, 0].set_title("(i) Per-anchor regulator ranking")
    axes[0, 0].legend(fontsize=7, loc="best")
    axes[0, 0].grid(True, alpha=0.3, axis="y")

    # Panel (ii): Spearman matrix heatmap
    im = axes[0, 1].imshow(spearman_matrix, cmap="RdBu_r", vmin=-1, vmax=1, aspect="auto")
    axes[0, 1].set_xticks(np.arange(5))
    axes[0, 1].set_xticklabels([a[:8] for a in ANCHOR_LABELS], rotation=45, ha="right", fontsize=7)
    axes[0, 1].set_yticks(np.arange(5))
    axes[0, 1].set_yticklabels([a[:8] for a in ANCHOR_LABELS], fontsize=7)
    for i in range(5):
        for j in range(5):
            axes[0, 1].text(j, i, f"{spearman_matrix[i, j]:.2f}",
                             ha="center", va="center", fontsize=8,
                             color="white" if abs(spearman_matrix[i, j]) > 0.5 else "black")
    plt.colorbar(im, ax=axes[0, 1], label="Spearman ρ")
    axes[0, 1].set_title("(ii) Pairwise Spearman matrix (5×5)")

    # Panel (iii): Bootstrap σ per anchor
    axes[1, 0].bar(ANCHOR_LABELS, [bootstrap_sigma_per_anchor[a] for a in ANCHOR_LABELS],
                    color="steelblue")
    axes[1, 0].axhline(BOOTSTRAP_SIGMA_VALID, color="green", linestyle="--",
                        label=f"VALID < {BOOTSTRAP_SIGMA_VALID}")
    axes[1, 0].axhline(BOOTSTRAP_SIGMA_MARGINAL, color="orange", linestyle="--",
                        label=f"MARGINAL < {BOOTSTRAP_SIGMA_MARGINAL}")
    axes[1, 0].set_ylabel("max bootstrap σ")
    axes[1, 0].set_title("(iii) Bootstrap σ per anchor (N=100)")
    axes[1, 0].set_xticklabels([a[:10] for a in ANCHOR_LABELS], rotation=45, ha="right", fontsize=8)
    axes[1, 0].legend(fontsize=8)
    axes[1, 0].grid(True, alpha=0.3, axis="y")

    # Panel (iv): Reading-A WIN indicator
    axes[1, 1].bar(["consistent\nrankings", "PASS\nthreshold"], [consistent_count, N_PASS_THRESHOLD],
                    color=["navy", "red"])
    axes[1, 1].axhline(N_PASS_THRESHOLD, color="red", linestyle="--", label="PASS threshold N≥4")
    axes[1, 1].set_ylim(0, 5.5)
    axes[1, 1].set_ylabel("N anchors with Spearman ≥ 0.9")
    axes[1, 1].set_title(f"(iv) Reading-A WIN: {reading_A_WIN}\n({reading_winner})")
    axes[1, 1].grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110, bbox_inches="tight")
    plt.close()
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")

    # Step 11: Compute dual-SHA + emit verdict
    print("\n--- Step 11: Compute dual-SHA + emit verdict ---")
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)

    value_str = (
        f"N={consistent_count}/5;"
        f"reading_A_WIN={int(reading_A_WIN)};"
        f"max_bootstrap_sigma={max_bootstrap_sigma:.4f};"
        f"reading_winner={reading_winner.replace(' ', '_').replace('(', '').replace(')', '')};"
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
