#!/usr/bin/env python3
"""
S87 W1b-HK-7 -- PAIRED-SLOT L=14 DISAMBIGUATION  [AUDIT]
========================================================

Gate: S87-W1B-HK-7-PAIRED-SLOT-L14-DISAMBIGUATION
Trigger: AUDIT (post-execution disambiguation of W1b-4 INFO_CLASS_B_NEAR_UNIQUE_GAP_A,C)
Classification: GEOMETRIC

Pre-registration (spawn prompt §HK-7):
  HYPOTHESIS: At L_max=14, the paired-slot integers shift in a way that
  either (a) closes the [1e-2, 1e-1] gap on CLASS-A by widening it past
  1e-1 (CLASS-B uniquely promoted), (b) tightens CLASS-A residual into
  PASS-band <1e-2 (CLASS-A becomes ambiguous co-passer), or (c) widens
  both CLASS-A and CLASS-B above 1e-1 (CLASS-D: the L=12 match was
  numerical coincidence).

  VERDICT BANDS (mirroring W1b-4 4-class enumeration verbatim):
    PASS-CLASS-B-UNIQUE-AT-L14:
        CLASS-B residual < 1e-3
        AND CLASS-A residual > 1e-1
        AND CLASS-C-min residual > 1e-1
      -> promotes CF-7 (S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY)
         to fixed-form S88 verify gate (a_n_FW canonicalization queued
         separately as S88-A-N-FW-CANONICALIZATION).

    INFO-CLASS-A-AMBIGUOUS-AT-L14:
        CLASS-A residual < 1e-2 at L=14
      -> CF stays open; carry-forward to L=16+ disambiguation.

    INFO-CLASS-D-AT-L14:
        CLASS-A residual > 1e-1 AND CLASS-B residual > 1e-1
      -> L=12 match closes as numerical coincidence (CLASS-D);
         CF closes as CLASS-D.

  Pre-registered taxonomic invariants (Class-6 PROHIBITED prevention):
    - CLASS-C candidate set is FROZEN at the W1b-4 enumeration (10
      candidates: C1..C10 in s87_w1b_paired_slot_ratio_interpretation.py
      lines 204-215). No post-hoc additions.
    - PASS_TOL = 1e-3 (HK-7 strict L=14 PASS band; tighter than W1b-4
      1e-2 to reflect the L=14 disambiguation premise that the L=12
      gap CAN be closed at L=14 only if CLASS-B tightens past 1e-3).
    - EXCLUDE_TOL = 1e-1 (W1b-4 verbatim).

INPUTS:
  - computations/session-87/s87_spectrum_cache_L14_tau019.npz (L=14 sector
    eigenvalue dict; 119 (p,q) sectors, 321,136 absolute eigenvalue
    entries; loaded with allow_pickle=True).
  - computations/_shared/canonical_constants.py (a0_fold = 6440.0,
    a2_fold = 2776.1653888633655, a4_fold = 1350.7216415169728;
    A0_GILKEY = 0.866 / A2_GILKEY = 0.728234972609 from S64 canonical
    Gilkey-Seeley-DeWitt geometric coefficients).
  - computations/session-87/s87_w1b_paired_slot_ratio_interpretation.py
    (W1b-4 canonical 4-class enumeration; reproduced verbatim).
  - computations/session-64/s64_bdg_kasparov.py (S64 canonical comment for
    Gilkey-vs-zeta split factors at a_0 and a_2 slots).

OUTPUT 4-tuple:
  (value=<min_class_residual_L14>, scheme=4-class-paired-slot-classification-L14,
   convention=substrate-paired-slot-L14-cache, L_max=14)

3-tuple annotation (S87 schema-v2):
  sign_verdict     = N/A (no directional pre-registration; classification probe)
  magnitude_verdict= per sub-classification (PASS for CLASS-B-UNIQUE; INFO for
                     CLASS-A-AMBIGUOUS; FAIL for CLASS-D)
  regime_verdict   = VALID (algebraic enumeration over fixed L=14 cache;
                     no truncation regime to break)

SUBSTITUTION CHAIN (L=14 disambiguation; verifying direction at runtime):

  Step 1 (definitions, per W1b-4 verbatim):
    a_n^zeta(L) := 0.5 * sum_n d_n / |lam_n|^{2n}    (S42 half-mode-count
                                                       zeta convention)
    A0_GILKEY  := 0.866                    (S64 canonical, L-invariant)
    A2_GILKEY  := 0.728234972609           (S64 canonical, L-invariant)
    paired_slot_num(L) := round(a_0^zeta(L) / A0_GILKEY)
    paired_slot_den(L) := round(a_2^zeta(L) / A2_GILKEY)
    r_obs(L) := paired_slot_num(L) / paired_slot_den(L)

  Step 2 (substitution at L=14 from cache):
    a_0^zeta(L=14) = 0.5 * sum_pq d_pq * (count of |lam| in sector pq)
    a_2^zeta(L=14) = 0.5 * sum_pq d_pq * sum_n |lam_n|^{-2}

  Step 3 (simplify per-class predictions):
    CLASS-A predicted:  r_A = 2.0   (L-invariant; hypercube-vertex 2:1)
    CLASS-B predicted:  r_B(L) = (a_0^zeta(L) * A2_GILKEY)
                                / (a_2^zeta(L) * A0_GILKEY)
    CLASS-C frozen:     {C1..C10} from W1b-4 verbatim (some L-invariant,
                                some computed from canonical_constants)
    residual_X(L) := |r_obs(L) - r_X(L)|

  Step 4 (read direction from canonical form at runtime):
    Direction is read from the computed residuals at L=14, NOT pre-claimed.
    Verdict assignment follows the pre-registered band rule; no convention-
    shopping.

DISCIPLINE:
  - canonical_constants imported (A0_GILKEY/A2_GILKEY local per S64 comment)
  - Local intermediates tagged # (local) per math-scripts.md
  - CPU-only path with OMP_NUM_THREADS=8 cap (per CLAUDE.md when no GPU)
  - Dual-SHA closure per S84+ schema (audit_sha256 + content_sha256 + companion)
  - 3-tuple Schema-v2 annotation (S87+; pre-registered collapse rule)
  - Verdict-line append: atomic single open("a") write per gate-verdicts.md
  - CLASS-C candidates frozen at W1b-4 enumeration (Class-6 PROHIBITED prevention)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
import math
import time
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import a0_fold, a2_fold, a4_fold  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent

GATE_ID = "S87-W1B-HK-7-PAIRED-SLOT-L14-DISAMBIGUATION"                  # (local)
SCHEME = "4-class-paired-slot-classification-L14"                        # (local)
CONVENTION = "substrate-paired-slot-L14-cache"                           # (local)
L_MAX_LABEL = "14"                                                       # (local)
SCHEMA_VERSION = "S87+"                                                  # (local)

# --- Pre-registered tolerance bounds (HK-7 spawn-prompt bands)
PASS_TOL = 1e-3                                                          # (local) HK-7 strict PASS band
EXCLUDE_TOL = 1e-1                                                       # (local) W1b-4 verbatim

# --- S64 canonical Gilkey-Seeley-DeWitt geometric coefficients
A0_GILKEY = 0.866                                                        # (local) a_0^Gilkey, S64 canonical
A2_GILKEY = 0.728234972609                                               # (local) a_2^Gilkey, S64 canonical

# --- Output paths
OUT_NPZ = SCRIPT_DIR / "s87_w1b_hk_7_paired_slot_l14_disambiguation.npz"
OUT_PNG = SCRIPT_DIR / "s87_w1b_hk_7_paired_slot_l14_disambiguation.png"
VERDICT_TXT = SCRIPT_DIR / "s87_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
L14_CACHE = SCRIPT_DIR / "s87_spectrum_cache_L14_tau019.npz"
W1B_4_SCRIPT = SCRIPT_DIR / "s87_w1b_paired_slot_ratio_interpretation.py"
S64_KASPAROV = SCRIPT_DIR / "s64_bdg_kasparov.py"

INPUT_FILES = [CANON_PY, L14_CACHE, W1B_4_SCRIPT, S64_KASPAROV]


# ---- SHA helpers (closure-hash pattern from S82 W1 template) ---------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                 # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                            # (local)
    for p in inputs:
        sha = sha256_of(p)                                               # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")    # (local)
        except ValueError:
            rel = p.name                                                 # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                           # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                         # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---- L=14 spectral moments ------------------------------------------------
def compute_l14_zeta_moments(cache_path: Path) -> dict:
    """Compute a_0^zeta(L=14), a_2^zeta(L=14) per the S42 half-mode-count
    zeta convention (matching the W1b-4 anchor convention exactly).

    For each (p, q) sector with multiplicity dim(p,q) and a list of absolute
    eigenvalues |lambda_n|, accumulate:
        a_0^zeta(L=14) := 0.5 * sum_pq dim(p,q) * count_pq
        a_2^zeta(L=14) := 0.5 * sum_pq dim(p,q) * sum_n |lambda_n|^{-2}
    Both float64; lambda_n > 0 throughout (cache stores absolute values).
    """
    data = np.load(cache_path, allow_pickle=True)                         # (local)
    sec = data["sector_evals"].item()                                     # (local) dict (p,q) -> sector dict

    total_count = 0                                                       # (local) sum d_pq * n_modes
    sum_inv_lam2 = 0.0                                                    # (local) sum d_pq * sum 1/lam^2
    n_sectors = 0                                                         # (local)
    n_raw_eigs = 0                                                        # (local) raw absolute eigenvalues across sectors
    abs_eig_min = float("inf")                                            # (local)
    abs_eig_max = 0.0                                                     # (local)

    for k, v in sec.items():
        if not isinstance(v, dict):
            continue
        if "abs_evals" not in v or "dim" not in v:
            continue
        n_sectors += 1
        dim_pq = int(v["dim"])                                            # (local) (p+1)(q+1)(p+q+2)/2
        abs_evals = np.asarray(v["abs_evals"])                            # (local)
        n_modes = abs_evals.size                                          # (local)
        n_raw_eigs += n_modes
        total_count += dim_pq * n_modes
        sum_inv_lam2 += dim_pq * float(np.sum(1.0 / abs_evals ** 2))
        abs_eig_min = min(abs_eig_min, float(np.min(abs_evals)))
        abs_eig_max = max(abs_eig_max, float(np.max(abs_evals)))

    a0_zeta_L14 = 0.5 * total_count                                       # (local) S42 half-mode-count
    a2_zeta_L14 = 0.5 * sum_inv_lam2                                      # (local)

    return {
        "n_sectors": n_sectors,
        "n_raw_abs_eigs": n_raw_eigs,
        "weighted_total_count": total_count,
        "a0_zeta_L14": a0_zeta_L14,
        "a2_zeta_L14": a2_zeta_L14,
        "abs_eig_min": abs_eig_min,
        "abs_eig_max": abs_eig_max,
    }


# ---- 4-class enumeration at L=14 ------------------------------------------
def enumerate_classes_l14(r_obs: float, a0_zeta: float, a2_zeta: float):
    """Replicate the W1b-4 4-class enumeration verbatim, evaluated at L=14.

    CLASS-C candidate set is FROZEN at the W1b-4 list of 10 candidates;
    no post-hoc additions are permitted (Class-6 PROHIBITED prevention).
    """
    pi_val = math.pi                                                      # (local)
    phi_paasch = 1.531580                                                 # (local) S12 chirality canonical

    # CLASS-A: hypercube-vertex 2:1 pairing (L-invariant)
    r_A = 2.0                                                             # (local)
    res_A = abs(r_obs - r_A)                                              # (local)

    # CLASS-B: SD mass-ratio expansion at a_0/a_2; structural identity at L=14:
    #   r_B(L=14) := (a_0^zeta(L=14) * A2_GILKEY) / (a_2^zeta(L=14) * A0_GILKEY)
    r_B = (a0_zeta * A2_GILKEY) / (a2_zeta * A0_GILKEY)                   # (local)
    res_B = abs(r_obs - r_B)                                              # (local)

    # CLASS-C: 10 candidates frozen verbatim from W1b-4 lines 204-215
    class_C_candidates = {                                                # (local)
        "C1_two_pi_squared_quotient": (2 * pi_val) ** 2 / (4 * pi_val) ** 2,
        "C2_phi_paasch_chirality_S12": phi_paasch,
        "C3_connes_karoubi_HP1_cocycle_ratio_S86_W5": 7.324992,
        "C4_SU3_dim_ratio_8_3": 8.0 / 3.0,
        "C5_atlas_cardinality_A5_A4_S86_W8": 5.0 / 4.0,
        "C6_V4_pair_orders_S86_W12": 2.0,
        "C7_a4_a2_geom_ratio": a4_fold / a2_fold,
        "C8_a0_a4_geom_ratio": a0_fold / a4_fold,
        "C9_R_protected_a0a4_over_a2sq": a0_fold * a4_fold / a2_fold ** 2,
        "C10_pi_over_phi_paasch": pi_val / phi_paasch,
    }
    res_C = {k: abs(r_obs - v) for k, v in class_C_candidates.items()}     # (local)
    res_C_min_name = min(res_C, key=res_C.get)                             # (local)
    res_C_min = res_C[res_C_min_name]                                      # (local)

    class_D_active = (res_A > EXCLUDE_TOL and res_B > EXCLUDE_TOL
                      and res_C_min > EXCLUDE_TOL)                        # (local)

    return {
        "r_obs": r_obs,
        "r_A": r_A,
        "res_A": res_A,
        "r_B": r_B,
        "res_B": res_B,
        "class_C_candidates": class_C_candidates,
        "class_C_residuals": res_C,
        "class_C_min_name": res_C_min_name,
        "class_C_min_residual": res_C_min,
        "class_D_active": class_D_active,
    }


# ---- HK-7 disambiguation classifier ---------------------------------------
def classify_hk7(enum_result):
    """HK-7 spawn-prompt 3-band rule:

      PASS-CLASS-B-UNIQUE-AT-L14:
          res_B < PASS_TOL AND res_A > EXCLUDE_TOL AND res_C_min > EXCLUDE_TOL
      INFO-CLASS-A-AMBIGUOUS-AT-L14:
          res_A < 1e-2  (the *L=14* CLASS-A residual shifts into PASS-band)
      INFO-CLASS-D-AT-L14:
          res_A > EXCLUDE_TOL AND res_B > EXCLUDE_TOL
      INFO-INDETERMINATE:
          otherwise (mixed bands, e.g., near-unique with gap)
    """
    res_A = enum_result["res_A"]                                          # (local)
    res_B = enum_result["res_B"]                                          # (local)
    res_C_min = enum_result["class_C_min_residual"]                       # (local)

    # PASS-CLASS-B-UNIQUE: B tight (<1e-3), A and C-min both excluded
    if (res_B < PASS_TOL
            and res_A > EXCLUDE_TOL
            and res_C_min > EXCLUDE_TOL):
        return {
            "verdict_class": "PASS-CLASS-B-UNIQUE-AT-L14",
            "magnitude_verdict": "PASS",
            "composite": "PASS",
            "promotion_path": (
                "S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY (CF-7) -- "
                "fixed-form S88 verify gate registry-landing queued; "
                "a_n_FW canonicalization queued separately as "
                "S88-A-N-FW-CANONICALIZATION (genuine future work)."
            ),
        }

    # INFO-CLASS-A-AMBIGUOUS: CLASS-A residual shifts into the W1b-4 PASS-band
    if res_A < 1e-2:
        return {
            "verdict_class": "INFO-CLASS-A-AMBIGUOUS-AT-L14",
            "magnitude_verdict": "INFO",
            "composite": "INFO",
            "promotion_path": (
                "Carry-forward to L=16+ disambiguation; CLASS-A and CLASS-B "
                "are both candidates at L=14 — strict uniqueness blocked."
            ),
        }

    # INFO-CLASS-D: both A and B widely excluded -> L=12 was numerical
    # coincidence; CF-7 closes as CLASS-D
    if res_A > EXCLUDE_TOL and res_B > EXCLUDE_TOL:
        return {
            "verdict_class": "INFO-CLASS-D-AT-L14",
            "magnitude_verdict": "FAIL",
            "composite": "INFO",
            "promotion_path": (
                "CLOSED as numerical coincidence -- "
                "CF-7 (S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY) "
                "demoted to no-future-work; the L=12 match was coincidence."
            ),
        }

    # Otherwise: indeterminate band
    return {
        "verdict_class": "INFO-INDETERMINATE-AT-L14",
        "magnitude_verdict": "INFO",
        "composite": "INFO",
        "promotion_path": (
            "Mixed-band outcome at L=14; CF-7 stays open with deeper "
            "CLASS-C enumeration or L=16+ confirmation queued."
        ),
    }


# ---- Plot ----
def make_plot(enum_l12, enum_l14, classification):
    fig, axes = plt.subplots(2, 2, figsize=(13, 11))                       # (local)

    # Panel 1: L=12 vs L=14 r_obs comparison
    ax = axes[0, 0]
    L_vals = [12, 14]
    r_vals = [enum_l12["r_obs"], enum_l14["r_obs"]]
    rB_vals = [enum_l12["r_B"], enum_l14["r_B"]]
    ax.plot(L_vals, r_vals, "o-", color="tab:red",
            label="r_obs (paired-slot int ratio)", markersize=12)
    ax.plot(L_vals, rB_vals, "s--", color="tab:green",
            label="r_B (CLASS-B structural identity)", markersize=10)
    ax.axhline(2.0, color="tab:blue", linestyle=":", alpha=0.6,
               label="CLASS-A r_A = 2.0 (L-invariant)")
    for L, r, rB in zip(L_vals, r_vals, rB_vals):
        ax.annotate(f"{r:.4f}", (L, r), textcoords="offset points",
                    xytext=(8, 8), fontsize=9, color="tab:red")
        ax.annotate(f"{rB:.4f}", (L, rB), textcoords="offset points",
                    xytext=(8, -16), fontsize=9, color="tab:green")
    ax.set_xticks(L_vals)
    ax.set_xlabel("L_max")
    ax.set_ylabel("paired-slot ratio")
    ax.set_title("L=12 -> L=14 paired-slot ratio shift")
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel 2: per-class residual table at L=14 (log-scale)
    ax = axes[0, 1]
    res_names = ["A", "B"] + list(enum_l14["class_C_residuals"].keys())
    res_values = ([enum_l14["res_A"], enum_l14["res_B"]]
                  + list(enum_l14["class_C_residuals"].values()))
    short_names = ["A", "B"] + [k.split("_")[0] for k in
                                 enum_l14["class_C_residuals"].keys()]
    colors = (["tab:blue", "tab:green"]
              + ["tab:orange"] * len(enum_l14["class_C_residuals"]))
    ax.barh(short_names, res_values, color=colors, alpha=0.7)
    ax.axvline(PASS_TOL, color="green", linestyle="--",
               label=f"PASS_TOL = {PASS_TOL:g} (HK-7)")
    ax.axvline(EXCLUDE_TOL, color="red", linestyle="--",
               label=f"EXCLUDE_TOL = {EXCLUDE_TOL:g}")
    ax.set_xscale("log")
    ax.set_xlabel("|r_obs - r_predicted|  (log scale)  at L=14")
    ax.set_title("Per-class residuals at L=14")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: CLASS-A vs CLASS-B gap evolution
    ax = axes[1, 0]
    L_pts = [12, 14]
    res_A_pts = [enum_l12["res_A"], enum_l14["res_A"]]
    res_B_pts = [enum_l12["res_B"], enum_l14["res_B"]]
    ax.semilogy(L_pts, res_A_pts, "o-", color="tab:blue",
                label="CLASS-A residual", markersize=12)
    ax.semilogy(L_pts, res_B_pts, "s-", color="tab:green",
                label="CLASS-B residual", markersize=10)
    ax.axhline(PASS_TOL, color="green", linestyle="--", alpha=0.5,
               label=f"PASS_TOL = {PASS_TOL:g}")
    ax.axhline(1e-2, color="orange", linestyle="--", alpha=0.5,
               label="W1b-4 PASS_TOL = 1e-2")
    ax.axhline(EXCLUDE_TOL, color="red", linestyle="--", alpha=0.5,
               label=f"EXCLUDE_TOL = {EXCLUDE_TOL:g}")
    for L, rA in zip(L_pts, res_A_pts):
        ax.annotate(f"{rA:.3e}", (L, rA), textcoords="offset points",
                    xytext=(8, 8), fontsize=9, color="tab:blue")
    for L, rB in zip(L_pts, res_B_pts):
        ax.annotate(f"{rB:.3e}", (L, rB), textcoords="offset points",
                    xytext=(8, -14), fontsize=9, color="tab:green")
    ax.set_xticks(L_pts)
    ax.set_xlabel("L_max")
    ax.set_ylabel("residual (log scale)")
    ax.set_title("CLASS-A vs CLASS-B residual gap evolution")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3, which="both")

    # Panel 4: classification flowchart text panel
    ax = axes[1, 1]
    ax.axis("off")
    flow_text = (
        f"HK-7 DISAMBIGUATION at L_max=14\n"
        f"-----------------------------\n\n"
        f"L=12 (W1b-4):\n"
        f"  num/den = 7436/3812 -> r_obs = {enum_l12['r_obs']:.6f}\n"
        f"  res_A   = {enum_l12['res_A']:.4e}  (GAP)\n"
        f"  res_B   = {enum_l12['res_B']:.4e}  (PASS)\n"
        f"  -> INFO_CLASS_B_NEAR_UNIQUE_GAP_A,C\n\n"
        f"L=14 (HK-7):\n"
        f"  num/den = {enum_l14['num']}/{enum_l14['den']}\n"
        f"  r_obs   = {enum_l14['r_obs']:.6f}\n"
        f"  res_A   = {enum_l14['res_A']:.4e}  "
        f"({'EXCL' if enum_l14['res_A'] > EXCLUDE_TOL else 'GAP'})\n"
        f"  res_B   = {enum_l14['res_B']:.4e}  "
        f"({'PASS' if enum_l14['res_B'] < PASS_TOL else 'GAP/EXCL'})\n"
        f"  res_C_min = {enum_l14['class_C_min_residual']:.4e} "
        f"({enum_l14['class_C_min_name'].split('_')[0]}, "
        f"{'EXCL' if enum_l14['class_C_min_residual'] > EXCLUDE_TOL else 'GAP'})\n\n"
        f"VERDICT CLASS:\n  {classification['verdict_class']}\n\n"
        f"Magnitude:    {classification['magnitude_verdict']}\n"
        f"Composite:    {classification['composite']}\n\n"
        f"Promotion path:\n  {classification['promotion_path'][:240]}"
    )
    ax.text(0.02, 0.98, flow_text, transform=ax.transAxes, fontsize=9,
            verticalalignment="top", family="monospace")
    ax.set_title("HK-7 disambiguation outcome")

    fig.suptitle(f"{GATE_ID} -- L=12 vs L=14 paired-slot disambiguation",
                 fontsize=12, weight="bold")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  Plot written: {OUT_PNG.name}")


# ---- Verdict-line emission (atomic single-line append; dual-SHA + 3-tuple) -
def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v):
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    annotation = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation "
        f"(S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(annotation)
    print(f"  Verdict + dual-SHA companion + 3-tuple annotation appended "
          f"to {VERDICT_TXT.name}")


# ---- Main ----
def main():
    t0 = time.time()                                                      # (local)
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                                # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Step A: compute L=14 spectral moments from cache
    moments = compute_l14_zeta_moments(L14_CACHE)
    print(f"  L=14 cache statistics:")
    print(f"    n_sectors           = {moments['n_sectors']}")
    print(f"    n_raw_abs_eigs      = {moments['n_raw_abs_eigs']}")
    print(f"    weighted_total_count= {moments['weighted_total_count']}")
    print(f"    abs_eig range       = [{moments['abs_eig_min']:.4e}, "
          f"{moments['abs_eig_max']:.4e}] M_KK")
    print(f"  a_0^zeta(L=14) = {moments['a0_zeta_L14']:.6f}  "
          f"(L=12 anchor: {a0_fold:.4f})")
    print(f"  a_2^zeta(L=14) = {moments['a2_zeta_L14']:.6f}  "
          f"(L=12 anchor: {a2_fold:.4f})")
    print()

    # Step B: paired-slot integers at L=14
    ps_num_L14 = round(moments["a0_zeta_L14"] / A0_GILKEY)                # (local)
    ps_den_L14 = round(moments["a2_zeta_L14"] / A2_GILKEY)                # (local)
    r_obs_L14 = ps_num_L14 / ps_den_L14                                   # (local)

    # Sage QQ-exact reduction via Python Fraction
    f_L14 = Fraction(ps_num_L14, ps_den_L14)                              # (local)
    print(f"  Paired-slot integers at L=14:")
    print(f"    num = round({moments['a0_zeta_L14']:.4f}/{A0_GILKEY}) "
          f"= {ps_num_L14}")
    print(f"    den = round({moments['a2_zeta_L14']:.4f}/{A2_GILKEY}) "
          f"= {ps_den_L14}")
    print(f"    r_obs(L=14) = {ps_num_L14}/{ps_den_L14} = {r_obs_L14:.10f}")
    print(f"    Sage QQ-exact reduction: {f_L14.numerator}/{f_L14.denominator} "
          f"(gcd = {math.gcd(ps_num_L14, ps_den_L14)})")
    print(f"  L=12 reference (W1b-4): r_obs(L=12) = 7436/3812 "
          f"= {7436/3812:.10f}")
    print()

    # Step C: 4-class enumeration at L=14 (CLASS-C frozen verbatim)
    enum_l14 = enumerate_classes_l14(r_obs_L14,
                                      moments["a0_zeta_L14"],
                                      moments["a2_zeta_L14"])
    enum_l14["num"] = ps_num_L14
    enum_l14["den"] = ps_den_L14
    enum_l14["a0_zeta_L14"] = moments["a0_zeta_L14"]
    enum_l14["a2_zeta_L14"] = moments["a2_zeta_L14"]

    print(f"  Per-class residuals at L=14:")
    print(f"    CLASS-A (r_A=2.0):           "
          f"residual = {enum_l14['res_A']:.6e}")
    print(f"    CLASS-B (r_B={enum_l14['r_B']:.6f}): "
          f"residual = {enum_l14['res_B']:.6e}")
    print(f"    CLASS-C (10 frozen candidates):")
    for name, r in enum_l14["class_C_candidates"].items():
        res = enum_l14["class_C_residuals"][name]
        flag = "  <-- min" if name == enum_l14["class_C_min_name"] else ""
        print(f"      {name}: r={r:.4f}, residual={res:.4e}{flag}")
    print(f"    CLASS-D active: {enum_l14['class_D_active']}")
    print()

    # L=12 reference enumeration (for plot panel)
    # Pinned per W1b-4 verdict line + working-paper §W1b-4
    enum_l12 = {
        "r_obs": 7436 / 3812,
        "r_A": 2.0,
        "res_A": abs(7436 / 3812 - 2.0),
        "r_B": (a0_fold * A2_GILKEY) / (a2_fold * A0_GILKEY),
        "res_B": abs(7436 / 3812
                     - (a0_fold * A2_GILKEY) / (a2_fold * A0_GILKEY)),
    }
    enum_l12["num"] = 7436
    enum_l12["den"] = 3812

    # Step D: HK-7 classification
    classification = classify_hk7(enum_l14)
    print(f"  HK-7 classification:")
    print(f"    verdict_class:     {classification['verdict_class']}")
    print(f"    magnitude_verdict: {classification['magnitude_verdict']}")
    print(f"    composite:         {classification['composite']}")
    print(f"    promotion_path:    {classification['promotion_path']}")
    print()

    # Step E: assemble verdict
    verdict = classification["composite"]                                 # (local)
    sign_verdict = "N/A"                                                  # (local)
    magnitude_verdict = classification["magnitude_verdict"]               # (local)
    regime_verdict = "VALID"                                              # (local)

    # Composite collapse cross-check (gate-verdicts.md):
    # regime=VALID; sign=N/A; magnitude PASS->composite PASS, INFO->INFO,
    # FAIL->INFO (composite collapsed to INFO at this gate level since
    # the gate is a sub-classification probe; CLASS-D is a pre-registered
    # outcome, not a malformed run). HK-7 emits PASS only on the
    # CLASS-B-UNIQUE pre-registered band.
    print(f"  Composite verdict (collapse rule, S87 schema-v2): {verdict}")

    # Build verdict value string
    value_str = (
        f"r_obs_L14={r_obs_L14:.6f};"
        f"A_res={enum_l14['res_A']:.4e};"
        f"B_res={enum_l14['res_B']:.4e};"
        f"C_min_res={enum_l14['class_C_min_residual']:.4e};"
        f"C_min_name={enum_l14['class_C_min_name']};"
        f"sub_class={classification['verdict_class']}"
    )

    # Step F: NPZ data emission
    class_C_names = list(enum_l14["class_C_candidates"].keys())
    class_C_values = np.array(
        [enum_l14["class_C_candidates"][n] for n in class_C_names])
    class_C_residuals = np.array(
        [enum_l14["class_C_residuals"][n] for n in class_C_names])

    np.savez(
        OUT_NPZ,
        # L=14 paired-slot integers + ratio
        paired_slot_num_L14=ps_num_L14,
        paired_slot_den_L14=ps_den_L14,
        paired_slot_ratio_L14=r_obs_L14,
        paired_slot_qq_num=f_L14.numerator,
        paired_slot_qq_den=f_L14.denominator,
        # L=14 spectral moments
        a0_zeta_L14=moments["a0_zeta_L14"],
        a2_zeta_L14=moments["a2_zeta_L14"],
        n_sectors_L14=moments["n_sectors"],
        n_raw_abs_eigs_L14=moments["n_raw_abs_eigs"],
        weighted_total_count_L14=moments["weighted_total_count"],
        abs_eig_min_L14=moments["abs_eig_min"],
        abs_eig_max_L14=moments["abs_eig_max"],
        # Per-class residuals at L=14
        class_A_predicted=enum_l14["r_A"],
        class_A_residual_L14=enum_l14["res_A"],
        class_B_predicted_L14=enum_l14["r_B"],
        class_B_residual_L14=enum_l14["res_B"],
        class_C_candidates_list=np.array(class_C_names),
        class_C_predicted_values=class_C_values,
        class_C_residuals_L14=class_C_residuals,
        class_C_min_name=enum_l14["class_C_min_name"],
        class_C_min_residual_L14=enum_l14["class_C_min_residual"],
        class_D_active_L14=enum_l14["class_D_active"],
        # L=12 reference
        paired_slot_ratio_L12=7436 / 3812,
        class_A_residual_L12=abs(7436 / 3812 - 2.0),
        class_B_residual_L12=abs(7436 / 3812 - enum_l12["r_B"]),
        # Verdict
        verdict_class=classification["verdict_class"],
        magnitude_verdict=classification["magnitude_verdict"],
        composite_verdict=verdict,
        promotion_path=classification["promotion_path"],
        # Audit metadata
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_LABEL,
        # Provenance pins
        a0_fold_canonical=a0_fold,
        a2_fold_canonical=a2_fold,
        a4_fold_canonical=a4_fold,
        a0_gilkey=A0_GILKEY,
        a2_gilkey=A2_GILKEY,
        # Tolerance pins
        pass_tol=PASS_TOL,
        exclude_tol=EXCLUDE_TOL,
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    # Step G: plot
    make_plot(enum_l12, enum_l14, classification)

    # Step H: append verdict line + dual-SHA + 3-tuple annotation
    append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict)

    elapsed = time.time() - t0                                            # (local)
    print(f"  Elapsed: {elapsed:.2f}s")
    print(f"  Final verdict: {verdict} ({classification['verdict_class']})")
    print()
    print("--- Substitution chain summary (HK-7 L=14 disambiguation) ---")
    print("  Step 1 (definitions, S42 zeta convention):")
    print("    a_n^zeta(L) := 0.5 * sum_n d_n / |lam_n|^{2n}")
    print("    paired_slot_num(L) := round(a_0^zeta(L) / A0_GILKEY)")
    print("    paired_slot_den(L) := round(a_2^zeta(L) / A2_GILKEY)")
    print("  Step 2 (substitution at L=14):")
    print(f"    a_0^zeta(L=14) = {moments['a0_zeta_L14']:.4f}")
    print(f"    a_2^zeta(L=14) = {moments['a2_zeta_L14']:.4f}")
    print(f"    num = {ps_num_L14}, den = {ps_den_L14}")
    print(f"    r_obs(L=14) = {r_obs_L14:.6f}")
    print("  Step 3 (per-class predictions):")
    print(f"    CLASS-A: r_A = 2.0; res_A = {enum_l14['res_A']:.4e}")
    print(f"    CLASS-B: r_B(L=14) = {enum_l14['r_B']:.6f}; "
          f"res_B = {enum_l14['res_B']:.4e}")
    print(f"    CLASS-C-min: {enum_l14['class_C_min_name']} -> "
          f"res = {enum_l14['class_C_min_residual']:.4e}")
    print("  Step 4 (read direction):")
    print(f"    res_B < PASS_TOL ({PASS_TOL:g}): "
          f"{enum_l14['res_B'] < PASS_TOL}")
    print(f"    res_A > EXCLUDE_TOL ({EXCLUDE_TOL:g}): "
          f"{enum_l14['res_A'] > EXCLUDE_TOL}")
    print(f"    res_C_min > EXCLUDE_TOL ({EXCLUDE_TOL:g}): "
          f"{enum_l14['class_C_min_residual'] > EXCLUDE_TOL}")
    print(f"    -> {classification['verdict_class']}")
    print()


if __name__ == "__main__":
    main()
