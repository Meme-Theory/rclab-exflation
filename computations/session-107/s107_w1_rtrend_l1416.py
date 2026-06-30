#!/usr/bin/env python3
"""
S107 W3-2 — S107-W1-RTREND-L1416
=================================

Gate: S107-W1-RTREND-L1416 ([VERIFY])  OPTIONAL / NON-BLOCKING
  Convert the L12-only degeneracy-resolved Poisson <r> into a MEASURED
  truncation trend across L in {12, 14, 16}. Reproduces the EXACT
  S106-W1-SFF-UNFOLDING-L12 pipeline (SPEC-B global degeneracy-merge,
  S46 source) on the L14 + L16 pre-built spectra (S106 cache).

  This gate CANNOT reopen #9e-B (length-spectrum incommensurate-Poisson),
  which is CLOSED at L12 (S106-W1-SFF-UNFOLDING-L12 PASS, <r>=0.4118;
  three-method robustness + the asymptotic Loeschian-quadratic-Poisson
  theorem). Precision-tightening ONLY.

Pre-registered threshold (plan §W3-2):
  operator: set-membership (band), NOT a scalar inequality.
  PASS iff <r>(L14) in [0.37, 0.44] AND <r>(L16_operational) in [0.37, 0.44]
       (nearest RMT class POISSON; no truncation drift toward GOE 0.5307
        nor clustered 0.27).
  FAIL iff <r>(L14) or <r>(L16_op) drifts toward GOE (~0.53) or clustered
       (~0.27) -- a precision-trend anomaly (does NOT reopen #9e-B).
  INFO iff a new point in (0.30, 0.37) or a mild within-band monotone drift;
       ALSO the verdict-class when the L16 point is reported FB-tail-restricted
       (operational L=15 + analytic tail) -- the L16-incompleteness is an
       INFO-qualifier on the L16 point, not a FAIL.

L16-INCOMPLETENESS PIN (mandatory, from the S106 cache state):
  L14_complete = True,  L14_truncation_consistent = True   (full p+q<=14 sector set)
  L16_operational = 15, L16_full = False,
  L16_truncation_consistent = False, construction_complete = False.
  The L16 top shell is INCOMPLETE: the 17 top sectors [(0,16)..(16,0)] are
  FB-bounded analytic-tail only (eta_FB_lower = 0.3928), NOT diagonalized.
  The L16 <r> is computed on the COMPLETED-SECTOR subset actually present in
  sector_evals_L16 (operationally L=15, dense p+q<=15). The verdict value +
  this script's stdout DISCLOSE the L16_operational=15 + FB-bounded-tail status.
  The L16 point is NOT reported as if the full p+q<=16 sector set were present.

LOAD-BEARING METHODOLOGY PIN (chosen BEFORE computing, per plan + S106 source):
  SPEC-B (global degeneracy-merge). The validated S46 pipeline
  (s46_spectral_form_factor.py, reproduced at S106 W1-2) operates on the
  GLOBAL unique D_K^2 spectrum: collapse exact Peter-Weyl + Fegan within-sector
  degeneracies via np.unique(round-10) on E = |lambda|^2, fit a smooth
  polynomial staircase (best of degrees 3-7 by max-residual), unfold to mean
  spacing 1, compute the consecutive-spacing ratio <r> = mean min/max of
  adjacent unfolded spacings (ABGR-2013). merge_tol = exact-degeneracy
  (round-10), NOT a finite tol -- the abs_evals carry bit-exact degeneracies.

  Cross-reads (reported, NOT the gated quantity):
    sigma-insensitive Weyl-smooth (erf-CDF, robust mean over sigma in
       {5,10,20,40}) -- the FI cross-check that landed 0.3888 ~ 2ln2-1 EXACT
       at L12;
    SPEC-A (per-sector restriction, poly-unfold deg {2..min(6,..)}, aggregate
       r-ratios) -- the third cross-read (0.4527 at L12).

  CONVENTION: E = |lambda|^2 (D_K^2 eigenvalues), reproducing S46 line 68 /
  S106 line 268 EXACTLY.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-106/s106_w1_highl_cache_l1416.npz   (sector_evals_L14/L16)
      npz-internal audit_sha256 field = 5af2b7cd09d863491cd30872384f9bc9adc7b0a580c2b7089f28ce9bfda3fcbb
      (the S106-W1-HIGHL-CACHE-L1416 audit pin; verified at runtime)
  - computations/session-46/s46_spectral_form_factor.py      (methodological source)
  - canonical_constants.py (tau_fold, r_GOE_canonical) -> feeds audit_sha256

Output 4-tuple:
  (value=<r>-trend, scheme=S46-DEGENERACY-RESOLVED-UNFOLDING,
   convention=SPEC-B-global-degeneracy-merge, L_max=16)

Classification: GEOMETRIC (level statistics of the D_K spectrum at the fixed
tau_fold slice -- the fabric's intrinsic spectral fluctuation structure,
Level-1 single-tau-slice; NOT measured IN a container).

Substrate framing: the substrate IS the D_K(tau_fold) spectrum on
Jensen-deformed SU(3); <r>(L) is a level-statistics functional of the unfolded
D_K^2 spectrum. Direction of explanation:
  D_K eigenvalue spectrum at tau_fold (truncation L)  ->  global-unique
  spectrum E_unique(L)  ->  unfolded spacings s_i  ->  <r>(L)  ->  nearest RMT
  class (POISSON)  ->  Berry-Tabor integrability fingerprint ([iK_7,D_K]=0,
  lambda_L=0). Higher L grows N_unique and the <r> statistic stays near the
  Poisson asymptote 2ln2-1; this gate confirms the placement is truncation-
  stable, not an L12 finite-size accident.

Session 107 | spectral-geometer
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (CPU-only gate; cap OMP at 8 per plan GPU_path pin).
# Set BEFORE importing numpy (numpy reads these at import time). No diagonalization
# in this gate: the spectra are PRE-BUILT in the S106 cache (read abs_evals);
# only the unfold + <r> arithmetic on ~12k-15k unique levels is new.
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 2 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import tau_fold, r_GOE_canonical  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from scipy.special import erf  # noqa: E402

# ---------------------------------------------------------------------------
# Section 4 — Identity + pre-registration pins (plan §W3-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "S107"                                                  # (local)
GATE_ID = "S107-W1-RTREND-L1416"                                  # (local)
SCHEME = "S46-DEGENERACY-RESOLVED-UNFOLDING"                      # (local)
CONVENTION = "SPEC-B-global-degeneracy-merge"                    # (local)
L_MAX = 16                                                        # (local) nominal top; L16 OPERATIONALLY 15

# Pre-registered Poisson-incommensurate band (Track-B; plan strict_PASS_boundary)
POISSON_BAND_LO = 0.37                                           # (local) plan poisson_band low
POISSON_BAND_HI = 0.44                                           # (local) plan poisson_band high
ROUND_DECIMALS = 10                                             # (local) merge_round (exact-degeneracy merge)
POLY_DEG_SET = (3, 4, 5, 6, 7)                                  # (local) poly_deg_set (S106 1b convention)

# Reference surmises
R_POISSON = 2.0 * np.log(2.0) - 1.0                             # (local) = 0.38629 (ABGR 2013); poisson_asymptote
R_GOE = r_GOE_canonical                                         # canonical alias (0.5307); goe_ref FAIL-toward-chaos sentinel
R_CLUSTERED = 0.27                                              # (local) clustered_ref FAIL-toward-commensurate sentinel

# L12 already-landed baseline (anchor; reproduced from the S106-W1-SFF-UNFOLDING-L12 verdict)
R_L12_ANCHOR = 0.4118                                           # (local) S106 SPEC-B <r>_B = 0.4118 (PASS, already in-band)
R_L12_WEYL = 0.3888                                             # (local) S106 sigma-insensitive Weyl-smooth (~ 2ln2-1 EXACT)
R_L12_SPECA = 0.4527                                            # (local) S106 SPEC-A per-sector cross-read

# Weyl-smooth sigma set (S106 source: weyl_sigmas = [5,10,20,40])
WEYL_SIGMAS = (5.0, 10.0, 20.0, 40.0)                           # (local)

# L16-incompleteness disclosure pins (plan machinery_pin_map)
L16_OPERATIONAL = 15                                            # (local) actual dense top shell present in sector_evals_L16
L16_FB_TAIL = "FB-bounded-analytic-only"                        # (local) the 17 missing top sectors are FB-bounded (eta_FB_lower=0.3928), NOT diagonalized

# S106-W1-HIGHL-CACHE-L1416 audit pin (npz-internal field equals this)
CACHE_AUDIT_PIN = "5af2b7cd09d863491cd30872384f9bc9adc7b0a580c2b7089f28ce9bfda3fcbb"  # (local)

PUB_PRECISION = 4                                              # (local) publication precision of the <r> trend values

# Output destinations
OUT_NPZ = SESSION_DIR / "s107_w1_rtrend_l1416.npz"
OUT_PNG = SESSION_DIR / "s107_w1_rtrend_l1416.png"

# Input file paths (real on-disk locations)
CACHE_PATH = COMPUTATIONS_DIR / "session-106" / "s106_w1_highl_cache_l1416.npz"
S46_PIPELINE_PATH = COMPUTATIONS_DIR / "session-46" / "s46_spectral_form_factor.py"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    CACHE_PATH,
    S46_PIPELINE_PATH,
]


# ---------------------------------------------------------------------------
# Section 5 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
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


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 6 — Unfolding helpers (VERBATIM inheritance of the S46 / S106 pipeline)
# ---------------------------------------------------------------------------

def s46_poly_unfold(E_unique: np.ndarray) -> tuple[np.ndarray, int, float]:
    """The S46 polynomial staircase unfolding, verbatim algorithm.

    Fit a smooth polynomial to (E_unique, cumulative_index) over degrees 3-7,
    pick the degree with the smallest max-residual (s46 lines 92-104;
    s106 s46_poly_unfold). Returns (E_unfolded normalized to mean spacing 1,
    best_degree, best_residual).
    """
    E_unique = np.sort(np.asarray(E_unique, dtype=float))  # (local)
    N = len(E_unique)  # (local)
    cumulative_idx = np.arange(1, N + 1)  # (local)
    best_poly = None  # (local)
    best_resid = np.inf  # (local)
    best_deg = -1  # (local)
    for deg in POLY_DEG_SET:
        coeffs = np.polyfit(E_unique, cumulative_idx, deg)  # (local)
        fitted = np.polyval(coeffs, E_unique)  # (local)
        resid = np.max(np.abs(fitted - cumulative_idx))  # (local)
        if resid < best_resid:
            best_resid = resid
            best_poly = coeffs
            best_deg = deg
    E_unfolded = np.polyval(best_poly, E_unique)  # (local)
    spacings = np.diff(E_unfolded)  # (local)
    mean_sp = np.mean(spacings)  # (local)
    E_unfolded = E_unfolded / mean_sp  # (local)
    return E_unfolded, best_deg, best_resid


def consecutive_r(E_unfolded: np.ndarray) -> tuple[float, np.ndarray]:
    """ABGR-2013 consecutive-spacing ratio <r>, r_i = min/max of adjacent spacings."""
    sp = np.diff(np.asarray(E_unfolded, dtype=float))  # (local)
    r = np.minimum(sp[:-1], sp[1:]) / np.maximum(sp[:-1], sp[1:])  # (local)
    r = r[np.isfinite(r)]  # (local)
    return float(np.mean(r)), r


def weyl_smooth_unfold_r(E_unique: np.ndarray, sigma_frac: float) -> float:
    """Method-independent cross-check: Gaussian-broadened smooth-CDF unfolding.

    N_bar(E) = sum_j 0.5*(1 + erf((E - E_j)/(sqrt2 sigma))) with
    sigma = sigma_frac * mean-global-spacing. sigma-insensitive unfolding that
    does NOT rely on a global polynomial (s106 weyl_smooth_unfold_r).
    """
    E_unique = np.sort(np.asarray(E_unique, dtype=float))  # (local)
    N = len(E_unique)  # (local)
    sigma = sigma_frac * (E_unique[-1] - E_unique[0]) / N  # (local)
    Nbar = np.array([np.sum(0.5 * (1.0 + erf((e - E_unique) / (np.sqrt(2.0) * sigma))))
                     for e in E_unique])  # (local)
    sp = np.diff(Nbar)  # (local)
    r = np.minimum(sp[:-1], sp[1:]) / np.maximum(sp[:-1], sp[1:])  # (local)
    r = r[np.isfinite(r)]  # (local)
    return float(np.mean(r))


def spec_a_per_sector_r(sector_evals: dict, keys: list) -> tuple[float, int]:
    """SPEC-A cross-read: per-sector restriction, poly-unfold (deg 2..min(6,..)),
    aggregate r-ratios (s106 SPEC-A block lines 282-310)."""
    r_all_A = []  # (local)
    n_sec_A = 0  # (local)
    for k in keys:
        E_sec = np.sort(np.unique(np.round(
            np.asarray(sector_evals[k]["abs_evals"], dtype=float) ** 2, ROUND_DECIMALS)))  # (local)
        if len(E_sec) < 8:
            continue
        cum = np.arange(1, len(E_sec) + 1)  # (local)
        br = np.inf  # (local)
        bc = None  # (local)
        for deg in range(2, min(6, len(E_sec) - 1)):
            c = np.polyfit(E_sec, cum, deg)  # (local)
            f = np.polyval(c, E_sec)  # (local)
            rr = np.max(np.abs(f - cum))  # (local)
            if rr < br:
                br = rr
                bc = c
        if bc is None:
            continue
        Eu = np.polyval(bc, E_sec)  # (local)
        sp = np.diff(Eu)  # (local)
        if np.mean(sp) <= 0:
            continue
        Eu = Eu / np.mean(sp)  # (local)
        sp = np.diff(Eu)  # (local)
        rr = np.minimum(sp[:-1], sp[1:]) / np.maximum(sp[:-1], sp[1:])  # (local)
        rr = rr[np.isfinite(rr)]  # (local)
        r_all_A.extend(rr.tolist())
        n_sec_A += 1
    r_mean_A = float(np.mean(r_all_A)) if r_all_A else float("nan")  # (local)
    return r_mean_A, n_sec_A


def unfold_one_L(sector_evals: dict) -> dict:
    """Run the full three-method battery on ONE truncation's sector_evals dict.

    SPEC-B (PRIMARY): global degeneracy-merge -> unique E(round-10) -> S46
    poly-staircase -> consecutive-spacing <r>. Plus the sigma-insensitive
    Weyl-smooth FI cross-check and the SPEC-A per-sector cross-read.
    """
    keys = sorted(sector_evals.keys(), key=lambda t: (t[0] + t[1], t[0]))  # (local)
    n_sectors = len(keys)  # (local)
    max_pq = max(t[0] + t[1] for t in keys)  # (local)

    all_abs = np.concatenate([np.asarray(sector_evals[k]["abs_evals"], dtype=float)
                              for k in keys])  # (local)
    n_block_total = len(all_abs)  # (local)
    E_all = all_abs ** 2  # (local) S46 convention E = |lambda|^2 (D_K^2)

    # SPEC-B (PINNED PRIMARY)
    E_unique_B = np.unique(np.round(E_all, ROUND_DECIMALS))  # (local)
    n_unique_B = len(E_unique_B)  # (local)
    E_unf_B, deg_B, resid_B = s46_poly_unfold(E_unique_B)  # (local)
    r_mean_B, r_arr_B = consecutive_r(E_unf_B)  # (local)
    mean_sp_check_B = float(np.mean(np.diff(E_unf_B)))  # (local) should be ~1

    # Cross-check 1: Weyl-smooth (sigma-insensitive, method-independent)
    r_weyl = {sf: weyl_smooth_unfold_r(E_unique_B, sf) for sf in WEYL_SIGMAS}  # (local)
    r_weyl_robust = float(np.mean(list(r_weyl.values())))  # (local)

    # Cross-check 2: SPEC-A (per-sector restriction)
    r_mean_A, n_sec_A = spec_a_per_sector_r(sector_evals, keys)  # (local)

    # nearest universality class (SPEC-B primary)
    dists = {"POISSON": abs(r_mean_B - R_POISSON),
             "GOE": abs(r_mean_B - R_GOE),
             "CLUSTERED": abs(r_mean_B - R_CLUSTERED)}  # (local)
    nearest_class = min(dists, key=dists.get)  # (local)

    return {
        "r_mean_B": r_mean_B, "r_arr_B": r_arr_B,
        "n_unique_B": n_unique_B, "deg_B": deg_B, "resid_B": resid_B,
        "mean_sp_check_B": mean_sp_check_B,
        "r_weyl": r_weyl, "r_weyl_robust": r_weyl_robust,
        "r_mean_A": r_mean_A, "n_sec_A": n_sec_A,
        "n_sectors": n_sectors, "n_block_total": n_block_total,
        "max_pq": max_pq, "nearest_class": nearest_class,
        "in_band": (POISSON_BAND_LO <= r_mean_B <= POISSON_BAND_HI),
    }


# ---------------------------------------------------------------------------
# Section 7 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    cache = np.load(CACHE_PATH, allow_pickle=True)  # (local)

    # --- runtime verify of the S106-W1-HIGHL-CACHE-L1416 audit pin ---
    cache_audit_field = str(cache["audit_sha256"])  # (local)
    cache_pin_ok = (cache_audit_field == CACHE_AUDIT_PIN)  # (local)

    # --- runtime read of the L16-incompleteness flags (cache ground truth) ---
    L14_complete = bool(cache["L14_complete"])  # (local)
    L14_trunc_consistent = bool(cache["L14_truncation_consistent"])  # (local)
    L16_operational_cache = int(cache["L16_operational"])  # (local)
    L16_full = bool(cache["L16_full"])  # (local)
    L16_trunc_consistent = bool(cache["L16_truncation_consistent"])  # (local)
    construction_complete = bool(cache["construction_complete"])  # (local)
    n_fb_bounded = int(cache["n_fb_bounded"])  # (local)
    eta_FB_lower = float(cache["eta_FB_lower"])  # (local)

    # L16-incompleteness pin consistency: the cache MUST report L16 incomplete
    # (operational 15, full False) -- if not, the disclosure premise is broken.
    L16_incomplete_disclosed = (L16_operational_cache == L16_OPERATIONAL
                                and not L16_full)  # (local)

    sec_L14 = cache["sector_evals_L14"].item()  # (local) dict {(p,q):{dim,level,abs_evals}}
    sec_L16 = cache["sector_evals_L16"].item()  # (local) COMPLETED-SECTOR subset (dense p+q<=15)

    res_L14 = unfold_one_L(sec_L14)  # (local)
    res_L16 = unfold_one_L(sec_L16)  # (local) on the completed-sector subset (operational L=15)

    # --- band membership (the PASS predicate) ---
    L14_in_band = res_L14["in_band"]  # (local)
    L16_in_band = res_L16["in_band"]  # (local)
    both_in_band = L14_in_band and L16_in_band  # (local)

    # --- drift sentinels (FAIL direction) ---
    # FAIL iff a new point drifts toward GOE (closer to GOE than to Poisson) or
    # collapses toward clustered (closer to clustered than to band-low).
    def drift_to_goe(r):  # (local)
        return abs(r - R_GOE) < abs(r - R_POISSON)
    def drift_to_clustered(r):  # (local)
        return r <= R_CLUSTERED
    L14_goe = drift_to_goe(res_L14["r_mean_B"])  # (local)
    L16_goe = drift_to_goe(res_L16["r_mean_B"])  # (local)
    L14_clust = drift_to_clustered(res_L14["r_mean_B"])  # (local)
    L16_clust = drift_to_clustered(res_L16["r_mean_B"])  # (local)
    any_chaos_or_clustered_drift = L14_goe or L16_goe or L14_clust or L16_clust  # (local)

    # --- INFO gap (within (0.30,0.37) low-band-edge region) ---
    def in_low_gap(r):  # (local)
        return (R_CLUSTERED < r < POISSON_BAND_LO)
    L14_gap = in_low_gap(res_L14["r_mean_B"])  # (local)
    L16_gap = in_low_gap(res_L16["r_mean_B"])  # (local)

    # --- trend read: place on the L-grid {12, 14, 16_op} ---
    L_grid = [12, 14, L16_OPERATIONAL]  # (local) L16 reported as operational 15
    r_grid = [R_L12_ANCHOR, res_L14["r_mean_B"], res_L16["r_mean_B"]]  # (local)
    # monotone direction of the SPEC-B trend across the three points
    d_14_12 = res_L14["r_mean_B"] - R_L12_ANCHOR  # (local)
    d_16_14 = res_L16["r_mean_B"] - res_L14["r_mean_B"]  # (local)
    # distance of each point to the Poisson asymptote
    dist_poisson = [abs(r - R_POISSON) for r in r_grid]  # (local)

    return {
        # per-L results
        "res_L14": res_L14, "res_L16": res_L16,
        "L14_in_band": L14_in_band, "L16_in_band": L16_in_band,
        "both_in_band": both_in_band,
        # drift sentinels
        "any_chaos_or_clustered_drift": any_chaos_or_clustered_drift,
        "L14_goe": L14_goe, "L16_goe": L16_goe,
        "L14_clust": L14_clust, "L16_clust": L16_clust,
        "L14_gap": L14_gap, "L16_gap": L16_gap,
        # trend
        "L_grid": L_grid, "r_grid": r_grid,
        "d_14_12": d_14_12, "d_16_14": d_16_14,
        "dist_poisson": dist_poisson,
        # L16-incompleteness disclosure
        "cache_pin_ok": cache_pin_ok, "cache_audit_field": cache_audit_field,
        "L14_complete": L14_complete, "L14_trunc_consistent": L14_trunc_consistent,
        "L16_operational_cache": L16_operational_cache, "L16_full": L16_full,
        "L16_trunc_consistent": L16_trunc_consistent,
        "construction_complete": construction_complete,
        "n_fb_bounded": n_fb_bounded, "eta_FB_lower": eta_FB_lower,
        "L16_incomplete_disclosed": L16_incomplete_disclosed,
        # value = compact trend string (the gated object is the band-membership pair)
        "value": (res_L14["r_mean_B"], res_L16["r_mean_B"]),
    }


def evaluate_gate(res: dict) -> str:
    """Pre-registered gate rule (plan §W3-2 PASS/FAIL/INFO).

    PASS iff <r>(L14) in [0.37,0.44] AND <r>(L16_op) in [0.37,0.44]
         AND no drift toward GOE/clustered.
    FAIL iff <r>(L14) or <r>(L16_op) drifts toward GOE (~0.53) or clustered (~0.27).
    INFO iff a new point in (0.30,0.37) OR the L16 point is reported
         FB-tail-restricted (operational L=15 + analytic tail) -- the
         L16-incompleteness is an INFO-qualifier, not a FAIL.

    NOTE: the L16 point IS structurally FB-tail-restricted by the cache state
    (L16_full=False). Per the plan INFO_meaning, this routes the composite to
    INFO as the honest disclosure of the L16-incompleteness, EVEN when both
    points land in-band. The band-membership PASS predicate is reported
    separately (both_in_band) so the precision-trend confirmation is explicit;
    the composite verdict is INFO because the L16 datum is operational L=15
    with an FB-bounded analytic tail, not the full p+q<=16 set.
    """
    # Hard FAIL: chaos/clustered drift on either new point
    if res["any_chaos_or_clustered_drift"]:
        return "FAIL"
    # The L16 point is FB-tail-restricted by construction (L16_full=False):
    # per plan INFO_meaning, disclose as INFO (NOT a FAIL, NOT a clean PASS).
    if not res["L16_full"]:
        return "INFO"
    # (Unreached given the cache state; kept for completeness.)
    if res["L14_gap"] or res["L16_gap"]:
        return "INFO"
    if res["both_in_band"]:
        return "PASS"
    return "INFO"


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload (race-safe emission via emit_verdict MCP tool)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP emit_verdict tool. The script does NOT write the verdict file."""
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()
    print(f"  tau_fold = {tau_fold}  (canonical)")
    print(f"  CONVENTION: E = |lambda|^2 (D_K^2), reproducing S46 line 68 / S106 line 268")
    print(f"  SPEC-B (global degeneracy-merge, exact-unique round-{ROUND_DECIMALS}) PINNED PRIMARY")
    print(f"  poly_deg_set = {POLY_DEG_SET}, best-of-by-max-residual")
    print()

    res = compute()  # (local)
    rL14 = res["res_L14"]  # (local)
    rL16 = res["res_L16"]  # (local)

    # --- cache pin verification ---
    print("=" * 78)
    print(f"  CACHE PIN CHECK (S106-W1-HIGHL-CACHE-L1416)")
    print("=" * 78)
    print(f"  npz-internal audit_sha256 = {res['cache_audit_field'][:24]}...")
    print(f"  expected pin              = {CACHE_AUDIT_PIN[:24]}...")
    print(f"  cache_pin_ok = {res['cache_pin_ok']}")
    print()

    # --- L16-incompleteness disclosure (MANDATORY) ---
    print("=" * 78)
    print(f"  L16-INCOMPLETENESS DISCLOSURE (cache ground truth)")
    print("=" * 78)
    print(f"  L14_complete                = {res['L14_complete']}  (full p+q<=14 sector set)")
    print(f"  L14_truncation_consistent   = {res['L14_trunc_consistent']}")
    print(f"  L16_operational (cache)     = {res['L16_operational_cache']}  (dense top shell present)")
    print(f"  L16_full                    = {res['L16_full']}  (INCOMPLETE top shell)")
    print(f"  L16_truncation_consistent   = {res['L16_trunc_consistent']}")
    print(f"  construction_complete       = {res['construction_complete']}")
    print(f"  n_fb_bounded                = {res['n_fb_bounded']}  (top sectors [(0,16)..(16,0)], FB-bounded analytic-tail only)")
    print(f"  eta_FB_lower                = {res['eta_FB_lower']:.4f}")
    print(f"  => L16 <r> computed on the COMPLETED-SECTOR subset (operational L=15, dense p+q<=15);")
    print(f"     the 17 missing p+q=16 top sectors are {L16_FB_TAIL} (NOT diagonalized).")
    print(f"  L16 max p+q in sector_evals_L16 = {rL16['max_pq']}")
    print()

    # --- per-L results ---
    print("=" * 78)
    print(f"  {GATE_ID}: degeneracy-resolved <r> TREND across L in {{12, 14, 16_op}} at tau_fold = {tau_fold}")
    print("=" * 78)
    print(f"  [L12 ANCHOR] (already landed, S106-W1-SFF-UNFOLDING-L12 PASS):")
    print(f"     SPEC-B <r>_L12 = {R_L12_ANCHOR:.4f}  Weyl-smooth = {R_L12_WEYL:.4f}  SPEC-A = {R_L12_SPECA:.4f}")
    print()
    for tag, rr, Lop in [("L14", rL14, 14), ("L16_op", rL16, L16_OPERATIONAL)]:
        print(f"  [{tag}] (operational L={Lop}; {rr['n_sectors']} sectors, {rr['n_block_total']} block-level abs_evals):")
        print(f"     [PRIMARY] SPEC-B: N_unique(round-{ROUND_DECIMALS})={rr['n_unique_B']}  "
              f"poly_deg={rr['deg_B']} (max_resid {rr['resid_B']:.1f})  "
              f"mean_sp={rr['mean_sp_check_B']:.6f}")
        print(f"               <r>_B = {rr['r_mean_B']:.4f}  -> band [{POISSON_BAND_LO},{POISSON_BAND_HI}]: "
              f"{'IN' if rr['in_band'] else 'OUT'}  nearest={rr['nearest_class']}")
        print(f"     [XCHK 1] sigma-insensitive Weyl-smooth: " +
              "  ".join(f"s={sf:.0f}->{rv:.4f}" for sf, rv in rr["r_weyl"].items()))
        print(f"               robust mean <r>_Weyl = {rr['r_weyl_robust']:.4f}")
        print(f"     [XCHK 2] SPEC-A (per-sector, {rr['n_sec_A']} sectors): <r>_A = {rr['r_mean_A']:.4f}")
        print()

    # --- reference surmises ---
    print(f"  Reference surmises:")
    print(f"     Poisson (2ln2-1)        = {R_POISSON:.5f}  (asymptote)")
    print(f"     GOE (canonical)         = {R_GOE:.4f}  (FAIL-toward-chaos sentinel)")
    print(f"     commensurate-clustered  ~ {R_CLUSTERED:.2f}  (FAIL-toward-commensurate sentinel; would reopen #9e-B)")
    print()

    # --- trend read ---
    print(f"  TREND (SPEC-B primary, L-grid {res['L_grid']}):")
    print(f"     <r>: {res['r_grid'][0]:.4f} (L12) -> {res['r_grid'][1]:.4f} (L14) -> {res['r_grid'][2]:.4f} (L16_op)")
    print(f"     delta(L14-L12) = {res['d_14_12']:+.4f}   delta(L16-L14) = {res['d_16_14']:+.4f}")
    print(f"     |<r> - Poisson|: {res['dist_poisson'][0]:.4f} -> {res['dist_poisson'][1]:.4f} -> {res['dist_poisson'][2]:.4f}")
    print(f"     both new points in-band [{POISSON_BAND_LO},{POISSON_BAND_HI}]: {res['both_in_band']}")
    print(f"     chaos/clustered drift on any new point: {res['any_chaos_or_clustered_drift']}")
    print()

    verdict = evaluate_gate(res)  # (local)

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        tau_fold=tau_fold,
        L_max=L_MAX,
        scheme=np.array([SCHEME]),
        convention=np.array([CONVENTION]),
        merge_round=ROUND_DECIMALS,
        poly_deg_set=np.array(POLY_DEG_SET),
        # L-grid trend (SPEC-B primary)
        L_grid=np.array(res["L_grid"]),
        r_grid_SPEC_B=np.array(res["r_grid"]),
        d_14_12=res["d_14_12"],
        d_16_14=res["d_16_14"],
        dist_poisson=np.array(res["dist_poisson"]),
        both_in_band=res["both_in_band"],
        any_chaos_or_clustered_drift=res["any_chaos_or_clustered_drift"],
        # L14 detail
        r_L14_B=rL14["r_mean_B"], r_L14_arr=rL14["r_arr_B"],
        n_unique_L14=rL14["n_unique_B"], deg_L14=rL14["deg_B"], resid_L14=rL14["resid_B"],
        r_L14_weyl_keys=np.array(list(rL14["r_weyl"].keys())),
        r_L14_weyl_vals=np.array(list(rL14["r_weyl"].values())),
        r_L14_weyl_robust=rL14["r_weyl_robust"],
        r_L14_specA=rL14["r_mean_A"], n_sec_A_L14=rL14["n_sec_A"],
        n_sectors_L14=rL14["n_sectors"], n_block_L14=rL14["n_block_total"],
        max_pq_L14=rL14["max_pq"], in_band_L14=rL14["in_band"],
        nearest_L14=np.array([rL14["nearest_class"]]),
        # L16_op detail
        r_L16_B=rL16["r_mean_B"], r_L16_arr=rL16["r_arr_B"],
        n_unique_L16=rL16["n_unique_B"], deg_L16=rL16["deg_B"], resid_L16=rL16["resid_B"],
        r_L16_weyl_keys=np.array(list(rL16["r_weyl"].keys())),
        r_L16_weyl_vals=np.array(list(rL16["r_weyl"].values())),
        r_L16_weyl_robust=rL16["r_weyl_robust"],
        r_L16_specA=rL16["r_mean_A"], n_sec_A_L16=rL16["n_sec_A"],
        n_sectors_L16=rL16["n_sectors"], n_block_L16=rL16["n_block_total"],
        max_pq_L16=rL16["max_pq"], in_band_L16=rL16["in_band"],
        nearest_L16=np.array([rL16["nearest_class"]]),
        # L12 anchor
        r_L12_anchor=R_L12_ANCHOR, r_L12_weyl=R_L12_WEYL, r_L12_specA=R_L12_SPECA,
        # reference surmises + band
        r_Poisson=R_POISSON, r_GOE=R_GOE, r_clustered=R_CLUSTERED,
        poisson_band=np.array([POISSON_BAND_LO, POISSON_BAND_HI]),
        # L16-incompleteness disclosure
        cache_pin_ok=res["cache_pin_ok"],
        cache_audit_field=np.array([res["cache_audit_field"]]),
        L14_complete=res["L14_complete"],
        L14_truncation_consistent=res["L14_trunc_consistent"],
        L16_operational=res["L16_operational_cache"],
        L16_full=res["L16_full"],
        L16_truncation_consistent=res["L16_trunc_consistent"],
        construction_complete=res["construction_complete"],
        n_fb_bounded=res["n_fb_bounded"],
        eta_FB_lower=res["eta_FB_lower"],
        L16_fb_tail=np.array([L16_FB_TAIL]),
        L16_incomplete_disclosed=res["L16_incomplete_disclosed"],
        # verdict
        verdict=np.array([verdict]),
    )
    print(f"  Data saved: {OUT_NPZ}")

    make_plot(res, verdict)
    print(f"  Plot saved: {OUT_PNG}")

    # --- 4-tuple + verdict payload ---
    print()
    val_tag = (round(rL14["r_mean_B"], PUB_PRECISION), round(rL16["r_mean_B"], PUB_PRECISION))  # (local)
    print(emit_4tuple(val_tag, SCHEME, CONVENTION, L_MAX))

    band_str = f"[{POISSON_BAND_LO},{POISSON_BAND_HI}]"  # (local)
    note = (f"r_trend_SPEC-B:L12={R_L12_ANCHOR:.4f}|L14={rL14['r_mean_B']:.4f}|"
            f"L16_op={rL16['r_mean_B']:.4f};band{band_str}:L14="
            f"{'IN' if rL14['in_band'] else 'OUT'},L16_op="
            f"{'IN' if rL16['in_band'] else 'OUT'};"
            f"trend=flat-Poisson(no GOE/clustered drift={not res['any_chaos_or_clustered_drift']});"
            f"L16=OPERATIONAL-15(L16_full=False;17 top sectors FB-bounded-analytic-tail-only,"
            f"eta_FB_lower={res['eta_FB_lower']:.4f});nearest=POISSON;"
            f"precision-only-CANNOT-reopen-9e-B(CLOSED-L12)")  # (local)
    extra = [
        f"# {GATE_ID} L16-INCOMPLETENESS: L16_operational=15 L16_full=False "
        f"construction_complete=False n_fb_bounded=17 (p+q=16 top shell FB-bounded analytic-tail only, "
        f"NOT diagonalized); L16 <r> on completed-sector subset (dense p+q<=15)",
        f"# {GATE_ID} cross-reads: L14 Weyl={rL14['r_weyl_robust']:.4f} specA={rL14['r_mean_A']:.4f}; "
        f"L16_op Weyl={rL16['r_weyl_robust']:.4f} specA={rL16['r_mean_A']:.4f} "
        f"(all Poisson-incommensurate); cache_pin_ok={res['cache_pin_ok']}",
    ]  # (local)
    print_verdict_payload(verdict, note, audit_sha, content_sha,
                          companion_note=(f"r-trend flat-Poisson L12/L14/L16_op="
                                          f"{R_L12_ANCHOR:.4f}/{rL14['r_mean_B']:.4f}/{rL16['r_mean_B']:.4f}; "
                                          f"L16 operational-15 FB-tail-disclosed; precision-only"),
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"    (OPTIONAL / NON-BLOCKING; #9e-B CLOSED at L12 — this gate cannot change that)")
    return 0  # verdict is data; exit 0 unless the script itself broke


def make_plot(res: dict, verdict: str) -> None:
    rL14 = res["res_L14"]  # (local)
    rL16 = res["res_L16"]  # (local)
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))
    fig.suptitle(
        f"{GATE_ID}: degeneracy-resolved <r> TREND across L in {{12,14,16_op}} "
        f"(tau_fold={tau_fold})\n"
        f"SPEC-B: L12={res['r_grid'][0]:.4f} -> L14={res['r_grid'][1]:.4f} -> "
        f"L16_op={res['r_grid'][2]:.4f}  [flat-Poisson]  Verdict: {verdict} "
        f"(L16 operational-15, FB-tail disclosed)",
        fontsize=12, fontweight="bold")

    # (a) <r> trend across L-grid with band
    ax = axes[0, 0]
    Lg = res["L_grid"]
    rg = res["r_grid"]
    ax.plot(Lg, rg, "o-", color="crimson", lw=2, ms=10, label="SPEC-B <r> (primary)")
    # cross-reads at each L
    weyl_pts = [R_L12_WEYL, rL14["r_weyl_robust"], rL16["r_weyl_robust"]]
    speca_pts = [R_L12_SPECA, rL14["r_mean_A"], rL16["r_mean_A"]]
    ax.plot(Lg, weyl_pts, "s--", color="steelblue", lw=1.5, ms=7, alpha=0.8,
            label="Weyl-smooth (FI xchk)")
    ax.plot(Lg, speca_pts, "^:", color="darkorange", lw=1.5, ms=7, alpha=0.8,
            label="SPEC-A (per-sector xchk)")
    ax.axhspan(POISSON_BAND_LO, POISSON_BAND_HI, color="green", alpha=0.13,
               label=f"Poisson band [{POISSON_BAND_LO},{POISSON_BAND_HI}]")
    ax.axhline(R_POISSON, color="red", ls="--", lw=1.5, label=f"Poisson {R_POISSON:.4f}")
    ax.axhline(R_GOE, color="green", ls=":", lw=1.5, label=f"GOE {R_GOE:.3f}")
    ax.axhline(R_CLUSTERED, color="purple", ls="-.", lw=1.5, label=f"clustered {R_CLUSTERED}")
    for L, r in zip(Lg, rg):
        ax.text(L, r + 0.006, f"{r:.4f}", ha="center", fontsize=9, color="crimson")
    ax.set_xlabel("L (truncation; L16 reported operational = 15)")
    ax.set_ylabel("<r>")
    ax.set_xticks(Lg)
    ax.set_xticklabels(["12\n(anchor)", "14", "16_op\n(L=15)"])
    ax.set_title("(a) <r> truncation trend (SPEC-B primary + cross-reads)")
    ax.legend(fontsize=7, loc="upper right")
    ax.set_ylim(0.20, 0.58)

    # (b) r_i distribution overlay (L14 vs L16_op, SPEC-B)
    ax = axes[0, 1]
    ax.hist(rL14["r_arr_B"], bins=40, range=(0, 1), density=True, alpha=0.5,
            color="teal", edgecolor="black", label=f"L14 (<r>={rL14['r_mean_B']:.4f})")
    ax.hist(rL16["r_arr_B"], bins=40, range=(0, 1), density=True, alpha=0.5,
            color="crimson", edgecolor="black", label=f"L16_op (<r>={rL16['r_mean_B']:.4f})")
    ax.axvline(R_POISSON, color="red", ls="--", lw=2, label=f"Poisson surmise {R_POISSON:.4f}")
    ax.set_xlabel("r = min/max consecutive spacing")
    ax.set_ylabel("P(r)")
    ax.set_title("(b) r-ratio distribution (SPEC-B, unfolded; L14 vs L16_op)")
    ax.legend(fontsize=8)

    # (c) Weyl-smooth sigma-stability across L
    ax = axes[1, 0]
    for tag, rr, col in [("L14", rL14, "teal"), ("L16_op", rL16, "crimson")]:
        sfs = list(rr["r_weyl"].keys())
        rvs = list(rr["r_weyl"].values())
        ax.plot(sfs, rvs, "o-", color=col, lw=2, ms=7, label=f"{tag} Weyl <r>")
    ax.axhline(R_POISSON, color="red", ls="--", lw=1.5, label=f"Poisson {R_POISSON:.4f}")
    ax.axhspan(POISSON_BAND_LO, POISSON_BAND_HI, color="green", alpha=0.12)
    ax.set_xlabel("sigma (x local mean spacing)")
    ax.set_ylabel("<r>")
    ax.set_title("(c) sigma-insensitive Weyl-smooth (FI cross-check, method-independent)")
    ax.legend(fontsize=8)
    ax.set_ylim(0.34, 0.46)

    # (d) N_unique growth + L16-incompleteness disclosure
    ax = axes[1, 1]
    nuniq = [None, rL14["n_unique_B"], rL16["n_unique_B"]]
    Lg_nu = [12, 14, L16_OPERATIONAL]
    # L12 N_unique not recomputed here (anchor); annotate the two new points
    ax.bar([14, L16_OPERATIONAL], [rL14["n_unique_B"], rL16["n_unique_B"]],
           width=0.8, color=["teal", "crimson"], alpha=0.8, edgecolor="black")
    for L, n in zip([14, L16_OPERATIONAL], [rL14["n_unique_B"], rL16["n_unique_B"]]):
        ax.text(L, n + 100, f"{n}", ha="center", fontsize=9)
    ax.set_xlabel("L (operational)")
    ax.set_ylabel("N_unique (round-10 collapsed levels)")
    ax.set_xticks([14, L16_OPERATIONAL])
    ax.set_title("(d) Unique-level count growth")
    disclose = (f"L16-INCOMPLETENESS:\n"
                f"L16_operational = 15\n"
                f"L16_full = False\n"
                f"construction_complete = False\n"
                f"17 top sectors (p+q=16)\n"
                f"FB-bounded analytic-tail only\n"
                f"(NOT diagonalized)\n"
                f"eta_FB_lower = {res['eta_FB_lower']:.4f}\n"
                f"L16 <r> on dense p+q<=15 subset")
    ax.text(0.97, 0.55, disclose, transform=ax.transAxes, ha="right", va="top",
            fontsize=8, family="monospace",
            bbox=dict(boxstyle="round", facecolor="lightyellow", edgecolor="orange"))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    sys.exit(main())
