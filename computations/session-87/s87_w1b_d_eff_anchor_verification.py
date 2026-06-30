#!/usr/bin/env python3
"""
S87 W1b-2 — S87-D-EFF-ANCHOR-VERIFICATION
==========================================

Gate: S87-D-EFF-ANCHOR-VERIFICATION ([VERIFY] [AUDIT])

Pre-registered threshold:
  PASS iff max(|d_eff_k - 8|) < 0.10 AND ordering monotone
  INFO iff max(|d_eff_k - 8|) in [0.10, 0.50] OR ordering breaks at 1 stratum-pair
  FAIL iff max(|d_eff_k - 8|) > 0.50  OR ordering breaks at >= 2 stratum-pairs OR regime BREAKDOWN

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (155984+ eigenvalues at L_max=12)
  - computations/_shared/canonical_constants.py             (audit_sha256 only)
  - script bytes                                          (BOTH SHAs)

Output 4-tuple:
  (value=max(|d_eff_k - 8|), scheme=Weyl-counting-function-fit,
   convention=substrate-stratum-partition-V4, L_max=12)

Schema-v2 3-tuple:
  sign_verdict     : N/A (audit gate; no directional pre-registration)
  magnitude_verdict: per pass/info/fail bands
  regime_verdict   : VALID iff max chi^2/d.o.f. < 5; MARGINAL [5,50]; BREAKDOWN >50

Classification: GEOMETRIC (substrate effective-dimension audit on finite-L spectrum)

METHODOLOGY
-----------
The substrate's effective dimension d_eff is the leading-asymptotic exponent of the
Weyl counting function N(λ) := #{|λ_i| <= λ}. Per the plan PRDR convention
N(λ) ~ C · λ^(d_eff/2) (treating |λ| as the eigenvalue of |D_K|, with the squared-
operator-convention factor of 2 absorbed into the exponent):

    log N(λ) = log C + (d_eff/2) · log λ
    ⇒ d_eff = 2 · slope (linear fit on log-log)

The 4-stratum V_4-monodromy partition (per S86 W-12 §"Map V_4 cosets ↔ Bulletin-4A
categories", workshop file `sessions/archive/session-86/workshops/s86-bimodality-and-4fold-cardinality.md`)
distinguishes 4 V_4-cosets at the moment-integral layer. At the bare-eigenvalue
layer, the canonical realization (S86 W-12 lines 309-322, 359-377, 533-552) is a
4-stratum partition by **|λ|-degeneracy-cluster ordinal modulo 4**:
the bottom-20 cardinality (2, 4, 8, 6) at τ_fold=0.190 confirms 4 distinct |λ|-
clusters in the bottom-20, after which the cyclic V_4-coset assignment continues
through the full spectrum's 7077 unique-|λ| clusters.

Stratum_k contains all eigenvalues whose unique-|λ|-cluster index satisfies
(cluster_idx mod 4) == k. This produces 4 disjoint subsets summing to the full
166896 eigenvalues. The Weyl fit per stratum recovers d_eff_k via the same log-
log slope formula.

DISCIPLINE
----------
- `from canonical_constants import *`
- All intermediates tagged `# (local)`
- CPU-only path with OMP_NUM_THREADS=8 set BEFORE numpy import (no GPU needed)
- Atomic verdict-line append via single open("a") write
- Dual-SHA (audit_sha256 + content_sha256) emitted; full 64-char form
- Schema-v2 second companion row emitted with sign/magnitude/regime triple
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (BEFORE numpy import)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SCRIPT_DIR = _Path(__file__).resolve().parent  # (local)
if str(_SCRIPT_DIR) not in _sys.path:
    _sys.path.insert(0, str(_SCRIPT_DIR))

from canonical_constants import *  # noqa: F401,F403  pull M_KK, tau_fold, etc.

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
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                      # (local)
GATE_ID = "S87-D-EFF-ANCHOR-VERIFICATION"                            # (local)
SCHEME = "Weyl-counting-function-fit"                                # (local)
CONVENTION = "substrate-stratum-partition-V4"                        # (local)
L_MAX = 12                                                           # (local)

# Pre-registered pass/fail thresholds (define BEFORE running)
PASS_BAND = 0.10                                                     # (local) ABS tol on |d_eff-8|
INFO_BAND = 0.50                                                     # (local) INFO ceiling
ANCHOR_D_EFF = 8                                                     # (local) d_eff anchor target
N_STRATA = 4                                                         # (local) V_4 partition cardinality
CHI2_VALID_MAX = 5.0                                                 # (local) regime VALID upper
CHI2_MARGINAL_MAX = 50.0                                             # (local) regime MARGINAL upper
RANDOM_SEED = 42                                                     # (local) plan PRDR pin

# Output destinations
SPECTRUM_NPZ = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
OUT_NPZ = resolve_output(87, 's87_w1b_d_eff_anchor_verification.npz')
OUT_PNG = resolve_output(87, 's87_w1b_d_eff_anchor_verification.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    SPECTRUM_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins):
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def load_spectrum_cache():
    """Load the L_max=12 master spectrum cache; return concatenated |lambda| array."""
    data = np.load(SPECTRUM_NPZ, allow_pickle=True)  # (local)
    sector_evals = data["sector_evals"].item()  # (local) dict[(p,q) -> dict]
    chunks = []  # (local)
    for k, v in sector_evals.items():
        chunks.append(np.asarray(v["abs_evals"], dtype=np.float64))
    all_evals = np.concatenate(chunks)  # (local)
    return all_evals


def assign_v4_strata(abs_evals_sorted, n_strata=4, cluster_eps=1e-9):
    """Assign each eigenvalue to one of n_strata V_4-coset bins.

    Per S86 W-12 (workshop §lines 309-322, 533-552): the bare-spectrum 4-stratum
    partition is realized by clustering on |lambda| at machine-precision, then
    assigning cluster_index mod n_strata to each unique-|lambda| cluster. Bottom-
    20 cardinality (2, 4, 8, 6) reproduces under this assignment when the unique
    clusters are ordered by ascending |lambda|.

    Inputs:
      abs_evals_sorted : 1-D float64 array, sorted ascending
      n_strata         : 4 (V_4-coset count)
      cluster_eps      : tolerance for unique-|lambda|-cluster identification
    Returns:
      stratum_indices  : 1-D int array of same length as abs_evals_sorted
                         with values in {0, 1, 2, 3}
      cluster_starts   : 1-D int array of cluster boundary indices (for audit)
    """
    n = len(abs_evals_sorted)  # (local)
    cluster_starts = [0]  # (local)
    for i in range(1, n):
        if abs_evals_sorted[i] - abs_evals_sorted[i - 1] > cluster_eps:
            cluster_starts.append(i)
    cluster_starts.append(n)
    n_clusters = len(cluster_starts) - 1  # (local)

    stratum_indices = np.empty(n, dtype=np.int32)  # (local)
    for ci in range(n_clusters):
        start = cluster_starts[ci]  # (local)
        end = cluster_starts[ci + 1]  # (local)
        stratum_indices[start:end] = ci % n_strata
    return stratum_indices, np.asarray(cluster_starts, dtype=np.int32)


def weyl_counting_function(abs_evals_sorted, n_grid=400):
    """Compute N(lambda) = #{|lambda_i| <= lambda} on a log-spaced lambda grid.

    Inputs:
      abs_evals_sorted : sorted array of |lambda| values
      n_grid           : number of log-spaced lambda samples
    Returns:
      lambda_grid : 1-D float64 array
      N_count     : 1-D float64 array (cumulative count at each lambda)
    """
    if len(abs_evals_sorted) == 0:
        return np.array([]), np.array([])
    lam_min = abs_evals_sorted[0]  # (local)
    lam_max = abs_evals_sorted[-1]  # (local)
    if lam_min <= 0:
        lam_min = abs_evals_sorted[abs_evals_sorted > 0][0] if (abs_evals_sorted > 0).any() else 1e-12
    lambda_grid = np.logspace(np.log10(lam_min), np.log10(lam_max), n_grid)  # (local)
    N_count = np.searchsorted(abs_evals_sorted, lambda_grid, side="right").astype(np.float64)  # (local)
    return lambda_grid, N_count


def fit_weyl_law(lambda_grid, N_count, fit_lo_frac=0.30, fit_hi_frac=0.95):
    """Fit log N(lambda) = log C + (d_eff/2) * log lambda on a log-window.

    Plan PRDR window: [lambda_min, 0.95 * lambda_max] excludes the finite-L
    cutoff edge. We additionally exclude the bottom 30% to avoid the small-
    lambda discreteness regime where the spectrum has not yet reached
    asymptotic Weyl behavior.

    Returns:
      d_eff      : 2 * slope of log-log fit
      C_fit      : exp(intercept)
      chi2_per_dof : reduced chi^2 of the linear fit (ordinary least squares)
      n_fit      : number of points used in fit
      lambda_lo  : lower bound of fit window
      lambda_hi  : upper bound of fit window
    """
    if len(lambda_grid) < 4:
        return float("nan"), float("nan"), float("inf"), 0, float("nan"), float("nan")

    valid = N_count > 0  # (local) drop zero-count points (log undefined)
    lam = lambda_grid[valid]  # (local)
    N = N_count[valid]  # (local)
    if len(lam) < 4:
        return float("nan"), float("nan"), float("inf"), 0, float("nan"), float("nan")

    lam_lo = lam[0] + (lam[-1] - lam[0]) * fit_lo_frac  # (local)
    lam_hi = lam[0] + (lam[-1] - lam[0]) * fit_hi_frac  # (local)
    # Use log-uniform window-fraction for stability
    log_lam = np.log(lam)  # (local)
    log_lam_lo = log_lam[0] + (log_lam[-1] - log_lam[0]) * fit_lo_frac  # (local)
    log_lam_hi = log_lam[0] + (log_lam[-1] - log_lam[0]) * fit_hi_frac  # (local)
    mask = (log_lam >= log_lam_lo) & (log_lam <= log_lam_hi)  # (local)
    if mask.sum() < 4:
        return float("nan"), float("nan"), float("inf"), 0, float("nan"), float("nan")

    x = log_lam[mask]  # (local)
    y = np.log(N[mask])  # (local)
    n_fit = len(x)  # (local)

    # Ordinary least squares: y = a + b * x
    A = np.vstack([np.ones_like(x), x]).T  # (local)
    coef, residuals, rank, sv = np.linalg.lstsq(A, y, rcond=None)  # (local)
    a, b = coef[0], coef[1]  # (local) intercept, slope

    # d_eff = 2 * slope per plan convention
    d_eff = 2.0 * b  # (local)
    C_fit = float(np.exp(a))  # (local)

    # Reduced chi^2 (assuming uniform unit variance on log y)
    y_pred = a + b * x  # (local)
    rss = float(np.sum((y - y_pred) ** 2))  # (local)
    dof = max(n_fit - 2, 1)  # (local)
    chi2_per_dof = rss / dof  # (local)

    lam_lo_used = float(np.exp(x[0]))  # (local)
    lam_hi_used = float(np.exp(x[-1]))  # (local)

    return float(d_eff), C_fit, float(chi2_per_dof), int(n_fit), lam_lo_used, lam_hi_used


def compute():
    """Main computation."""
    # ---- 1. Load and sort the L_max=12 spectrum ----
    abs_evals = load_spectrum_cache()  # (local)
    n_total = len(abs_evals)  # (local)
    print(f"[1] Loaded {n_total} eigenvalues from cache.")
    print(f"    |lambda| range: [{abs_evals.min():.6e}, {abs_evals.max():.6e}]")

    sort_idx = np.argsort(abs_evals)  # (local)
    lambda_sorted = abs_evals[sort_idx].astype(np.float64)  # (local)

    # ---- 2. Build Weyl counting function over full spectrum ----
    lambda_grid, N_count = weyl_counting_function(lambda_sorted, n_grid=400)
    print(f"[2] Weyl counting function on {len(lambda_grid)} log-spaced points.")

    # ---- 3. Fit global d_eff (sanity check) ----
    d_eff_global, C_global, chi2_global, n_fit_global, lo_g, hi_g = fit_weyl_law(
        lambda_grid, N_count, fit_lo_frac=0.30, fit_hi_frac=0.95
    )
    print(f"[3] GLOBAL d_eff = {d_eff_global:.6f}  C = {C_global:.4e}  "
          f"chi2/dof = {chi2_global:.4f}  n_fit = {n_fit_global}  "
          f"window = [{lo_g:.4e}, {hi_g:.4e}]")

    # ---- 4. Assign V_4-coset stratum to each eigenvalue ----
    stratum_indices, cluster_starts = assign_v4_strata(
        lambda_sorted, n_strata=N_STRATA, cluster_eps=1e-9
    )
    print(f"[4] V_4 partition: {len(cluster_starts) - 1} unique-|lambda| clusters; "
          f"sizes per stratum:")
    for k in range(N_STRATA):
        n_k = int((stratum_indices == k).sum())  # (local)
        print(f"    stratum_{k}: n_eigenvalues = {n_k}")

    # ---- 5. Per-stratum Weyl-fit ----
    d_eff_per_stratum = np.zeros(N_STRATA, dtype=np.float64)  # (local)
    chi2_per_stratum = np.zeros(N_STRATA, dtype=np.float64)  # (local)
    C_per_stratum = np.zeros(N_STRATA, dtype=np.float64)  # (local)
    n_fit_per_stratum = np.zeros(N_STRATA, dtype=np.int32)  # (local)
    lo_per_stratum = np.zeros(N_STRATA, dtype=np.float64)  # (local)
    hi_per_stratum = np.zeros(N_STRATA, dtype=np.float64)  # (local)
    weyl_curves_per_stratum = []  # (local) for plotting

    for k in range(N_STRATA):
        mask = stratum_indices == k  # (local)
        lam_k = lambda_sorted[mask]  # (local)  already sorted (sub-sequence of sorted array)
        lam_grid_k, N_count_k = weyl_counting_function(lam_k, n_grid=400)
        d_eff_k, C_k, chi2_k, n_fit_k, lo_k, hi_k = fit_weyl_law(
            lam_grid_k, N_count_k, fit_lo_frac=0.30, fit_hi_frac=0.95
        )
        d_eff_per_stratum[k] = d_eff_k
        chi2_per_stratum[k] = chi2_k
        C_per_stratum[k] = C_k
        n_fit_per_stratum[k] = n_fit_k
        lo_per_stratum[k] = lo_k
        hi_per_stratum[k] = hi_k
        weyl_curves_per_stratum.append((lam_grid_k, N_count_k))
        print(f"[5.{k}] stratum_{k}: d_eff = {d_eff_k:.6f}  chi2/dof = {chi2_k:.4f}  "
              f"window = [{lo_k:.4e}, {hi_k:.4e}]  n_fit = {n_fit_k}")

    # ---- 6. Anchor-deviation per stratum + ordering check ----
    deviation_per_stratum = np.abs(d_eff_per_stratum - ANCHOR_D_EFF)  # (local)
    max_deviation = float(deviation_per_stratum.max())  # (local)
    print(f"[6] |d_eff_k - 8| per stratum: {deviation_per_stratum.tolist()}")
    print(f"    max deviation = {max_deviation:.6f}")

    # Ordering check: d_eff_0 <= d_eff_1 <= d_eff_2 <= d_eff_3
    ordering_pass_mask = np.zeros(N_STRATA - 1, dtype=bool)  # (local) one bool per adjacent pair
    for k in range(N_STRATA - 1):
        ordering_pass_mask[k] = bool(d_eff_per_stratum[k] <= d_eff_per_stratum[k + 1])
    n_ordering_breaks = int((~ordering_pass_mask).sum())  # (local)
    print(f"[6b] ordering pairs (k, k+1): {ordering_pass_mask.tolist()}  "
          f"breaks = {n_ordering_breaks}")

    # ---- 7. Composite verdict (3-tuple per Schema-v2) ----
    sign_verdict = "N/A"  # (local) audit gate has no directional pre-reg

    # magnitude_verdict from band table; ordering modifies INFO/FAIL
    if max_deviation < PASS_BAND and n_ordering_breaks == 0:
        magnitude_verdict = "PASS"  # (local)
    elif max_deviation > INFO_BAND or n_ordering_breaks >= 2:
        magnitude_verdict = "FAIL"  # (local)
    else:
        magnitude_verdict = "INFO"  # (local)

    chi2_max_seen = float(np.nanmax(chi2_per_stratum))  # (local)
    if chi2_max_seen < CHI2_VALID_MAX:
        regime_verdict = "VALID"  # (local)
    elif chi2_max_seen <= CHI2_MARGINAL_MAX:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)

    # Composite collapse rule (gate-verdicts.md §"Composite-collapse rule")
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"[7] sign={sign_verdict}  magnitude={magnitude_verdict}  "
          f"regime={regime_verdict}  ⇒ composite={composite}")

    return {
        "value": max_deviation,
        "lambda_L12_sorted": lambda_sorted,
        "weyl_count_lambda": (lambda_grid, N_count),
        "d_eff_global": float(d_eff_global),
        "d_eff_per_stratum": d_eff_per_stratum,
        "chi2_per_stratum": chi2_per_stratum,
        "C_per_stratum": C_per_stratum,
        "n_fit_per_stratum": n_fit_per_stratum,
        "lo_per_stratum": lo_per_stratum,
        "hi_per_stratum": hi_per_stratum,
        "stratum_membership_indices": stratum_indices,
        "cluster_starts": cluster_starts,
        "ordering_pass_mask": ordering_pass_mask,
        "n_ordering_breaks": n_ordering_breaks,
        "deviation_per_stratum": deviation_per_stratum,
        "weyl_curves_per_stratum": weyl_curves_per_stratum,
        "anchor_d_eff": ANCHOR_D_EFF,
        "n_total": n_total,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite_verdict": composite,
    }


def make_plot(result, png_path: Path):
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel A: global Weyl counting function on log-log
    ax = axes[0]
    lam, N = result["weyl_count_lambda"]
    valid = N > 0
    ax.loglog(lam[valid], N[valid], color="black", lw=1.6, label="N(λ) global")
    # Overlay a slope-4 reference (d_eff/2 = 4)
    lam_ref = np.array([lam[valid][0], lam[valid][-1]])
    N_ref_anchor = N[valid][len(lam[valid]) // 2]
    lam_ref_anchor = lam[valid][len(lam[valid]) // 2]
    N_ref = N_ref_anchor * (lam_ref / lam_ref_anchor) ** 4.0
    ax.loglog(lam_ref, N_ref, color="red", linestyle="--", lw=1.2,
              label="slope = d_eff/2 = 4 (anchor)")
    ax.set_xlabel(r"$|\lambda|$")
    ax.set_ylabel(r"$N(\lambda) = \#\{|\lambda_i|\leq\lambda\}$")
    ax.set_title(f"Panel A — Weyl counting function (L_max={L_MAX}; n={result['n_total']})")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3, which="both")

    # Panel B: per-stratum d_eff bar chart with +/- tolerance
    ax = axes[1]
    d_eff_arr = result["d_eff_per_stratum"]
    x_pos = np.arange(N_STRATA)
    bars = ax.bar(x_pos, d_eff_arr, color="steelblue", edgecolor="black",
                  alpha=0.8, label="d_eff per stratum")
    ax.axhline(ANCHOR_D_EFF, color="red", linestyle="--", lw=1.5,
               label=f"anchor d_eff = {ANCHOR_D_EFF}")
    ax.axhspan(ANCHOR_D_EFF - PASS_BAND, ANCHOR_D_EFF + PASS_BAND,
               color="green", alpha=0.15, label=f"PASS band ±{PASS_BAND}")
    ax.axhspan(ANCHOR_D_EFF - INFO_BAND, ANCHOR_D_EFF + INFO_BAND,
               color="orange", alpha=0.10, label=f"INFO band ±{INFO_BAND}")
    for i, b in enumerate(bars):
        h = b.get_height()
        ax.text(b.get_x() + b.get_width() / 2, h + 0.05, f"{h:.4f}",
                ha="center", va="bottom", fontsize=9)
    ax.set_xticks(x_pos)
    ax.set_xticklabels([f"stratum {k}" for k in range(N_STRATA)])
    ax.set_ylabel("d_eff,k = 2 × slope (Weyl-fit)")
    ax.set_title("Panel B — per-stratum d_eff vs anchor")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    # Panel C: ordering check
    ax = axes[2]
    ord_mask = result["ordering_pass_mask"]
    pair_labels = [f"{k}≤{k+1}" for k in range(N_STRATA - 1)]
    colors = ["green" if ok else "red" for ok in ord_mask]
    ax.bar(pair_labels, [1] * len(pair_labels), color=colors, edgecolor="black", alpha=0.8)
    for i, ok in enumerate(ord_mask):
        ax.text(i, 0.5, "PASS" if ok else "FAIL",
                ha="center", va="center", color="white",
                fontsize=12, fontweight="bold")
    ax.set_ylim(0, 1.2)
    ax.set_yticks([])
    ax.set_title("Panel C — monotone-ordering check (per adjacent pair)")
    sub = (f"d_eff = ({d_eff_arr[0]:.4f}, {d_eff_arr[1]:.4f}, "
           f"{d_eff_arr[2]:.4f}, {d_eff_arr[3]:.4f})  "
           f"breaks = {result['n_ordering_breaks']}/{N_STRATA - 1}")
    ax.set_xlabel(sub)

    plt.suptitle(f"{GATE_ID} — composite={result['composite_verdict']} "
                 f"(value={result['value']:.6f}, anchor=8, scheme={SCHEME})",
                 fontsize=11)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(png_path, dpi=120)
    plt.close()


# ---------------------------------------------------------------------------
# Section 6 — Verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict_with_companions(verdict, value, audit_sha, content_sha,
                                   sign_v, magnitude_v, regime_v):
    """Atomic append of canonical verdict line + dual-SHA short companion +
    Schema-v2 3-tuple companion. Single open("a") write per row."""
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    short_comp = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_comp = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(short_comp)
        fp.write(schema_v2_comp)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    result = compute()
    value = result["value"]

    # 3. Persist .npz with all required keys (per spawn-prompt OUTPUT spec)
    np.savez_compressed(
        OUT_NPZ,
        lambda_L12_sorted=result["lambda_L12_sorted"],
        weyl_count_lambda_grid=result["weyl_count_lambda"][0],
        weyl_count_lambda_N=result["weyl_count_lambda"][1],
        d_eff_global=result["d_eff_global"],
        d_eff_stratum_0=result["d_eff_per_stratum"][0],
        d_eff_stratum_1=result["d_eff_per_stratum"][1],
        d_eff_stratum_2=result["d_eff_per_stratum"][2],
        d_eff_stratum_3=result["d_eff_per_stratum"][3],
        d_eff_per_stratum=result["d_eff_per_stratum"],
        chi2_per_stratum=result["chi2_per_stratum"],
        C_per_stratum=result["C_per_stratum"],
        n_fit_per_stratum=result["n_fit_per_stratum"],
        lo_per_stratum=result["lo_per_stratum"],
        hi_per_stratum=result["hi_per_stratum"],
        stratum_membership_indices=result["stratum_membership_indices"],
        cluster_starts=result["cluster_starts"],
        ordering_pass_mask=result["ordering_pass_mask"],
        n_ordering_breaks=result["n_ordering_breaks"],
        deviation_per_stratum=result["deviation_per_stratum"],
        anchor_d_eff=ANCHOR_D_EFF,
        n_total=result["n_total"],
        L_max=L_MAX,
        scheme=SCHEME,
        convention=CONVENTION,
        sign_verdict=result["sign_verdict"],
        magnitude_verdict=result["magnitude_verdict"],
        regime_verdict=result["regime_verdict"],
        composite_verdict=result["composite_verdict"],
        max_deviation=value,
    )
    print(f"[8] saved npz: {OUT_NPZ.name}")

    # 4. Plot
    make_plot(result, OUT_PNG)
    print(f"[9] saved png: {OUT_PNG.name}")

    # 5. Emit 4-tuple + append verdict (with two companion rows)
    composite = result["composite_verdict"]  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict_with_companions(
        composite, value, audit_sha, content_sha,
        result["sign_verdict"], result["magnitude_verdict"], result["regime_verdict"],
    )

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    # Exit 0 regardless of PASS/FAIL/INFO per math-scripts.md "Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
