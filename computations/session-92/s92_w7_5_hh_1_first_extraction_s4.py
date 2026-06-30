#!/usr/bin/env python3
"""
S92 W7-5 — S92-W7-CF-W8-CONSOLIDATED-6-CF-W9-10-A-HH-1-FIRST-EXTRACTION-S4
============================================================================

Gate: S92-W7-CF-W8-CONSOLIDATED-6-CF-W9-10-A-HH-1-FIRST-EXTRACTION-S4 ([SIGN])

Pre-registered threshold (plan §W7-5 strict_PASS_boundary; band [1.5, 4.0]):
  PASS  iff alpha_HH1_emp(s=4) in [1.5, 4.0]
        AND ABS(alpha_HH1_emp(s=4) - 4) <= 1.5 at 6 sig figs
        AND eta_FB_lower(L=14) >= 0.40 across sectors intersecting M_3(C)
        AND truncation_consistent across L_op in {6, 8, 10, 12, 14}
        AND substrate-physics direction alpha_HH1_emp(s=4) > 0 matches
            Wodzicki/Connes d=4 expectation
  INFO  iff alpha_HH1_emp(s=4) in (0, 1.5) U (4.0, +inf) AND direction matches
  FAIL  iff alpha_HH1_emp(s=4) <= 0 OR direction inversion OR FB floor violation
        OR truncation inconsistency

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-87/s87_spectrum_cache_L14_tau019.npz
    (L_max=14 master spectrum cache; 2.58 MB built 2026-04-28 per S87 W11-3
     precedent; sector_evals dict keyed by (p,q) -> {'dim', 'level', 'abs_evals'}
     per Peter-Weyl decomposition with K-spinor fiber dim 16)
  - computations/_shared/canonical_constants.py (feeds audit_sha256)
  - computations/_shared/_cm_1995_residue_formula.py (FULL CM-1995 §III.4
     simple-pole residue evaluator; substrate-natural FULL physical
     regularization per substrate-first-canonical-sourcing.md §(iv) K=4
     MANDATORY level-pin discipline)
  - computations/_shared/_schur_orthogonality_decomp.py (M_3(C) Wedderburn
     block index pin; A_F_REAL_DIM_TARGET = (1, 4, 18); M3C block index = 2)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<alpha_HH1_emp_s4>,
   scheme=full-cm-1995-iii-4-simple-pole-residue,
   convention=substrate-distance-2-pole-s4-FULL,
   L_max=14)

Classification: GEOMETRIC (substrate-IS Hochschild-cocycle norm L_max-scan
first-extraction at substrate-distance-2 pole s=4 on M_3(C) Peter-Weyl block).

METHODOLOGY
-----------
Substrate-IS substitution chain (plan §W7-5 Field 6 + 4-sub-option extraction):

Step 1 (Definitions):
  A_K = C (+) H (+) M_3(C)   [Wedderburn decomposition of K-fiber algebra]
  M_3(C) Peter-Weyl block correspondence: by SU(3) triality decomposition,
    sectors (p,q) with (p - q) mod 3 != 0 lie in the M_3(C) Cartan-zone
    (color-charged) sub-algebra image; (p,q) with (p-q) mod 3 == 0 lie in
    the BdG-restricted (C + H) sector image of iota_*.

  HH^1(M_3(C), M_3(C)*) = Hochschild first cohomology of M_3(C) on
    the spectral triple (A_K, H_K, D_K).
    Wodzicki/Connes d=4 substrate-physics prediction at substrate-distance
    N = s - d/2 = s - 2:
      alpha_HH1(s) = 2 (s - 2)
      alpha_HH1(s=4) = 4   [substrate-distance-2; this gate's central pole]

  Substrate-distance-2 pole s_0 = 4 (Mellin weight |D|^{-2s} = |lambda|^{-8}):
    HH^1 cocycle norm at L_max=L on M_3(C) block:
      norm_HH1_M3C(L; s=4) = sum_{(p,q): (p-q) mod 3 != 0, p+q <= L} sum_alpha
                                 |lambda_alpha(p,q;tau_fold)|^{-8}

Step 2 (Substitution L_max-scan):
  L_scan = {10, 12, 14}   [substrate-distance-2 pole requires deeper L-arm;
                            S91 §W9-10 substrate-distance-1 pole used {8,10,12}]
  L_op_scan = {6, 8, 10, 12, 14}   [Casimir-bound truncation_consistent flag]
  For each L in L_scan:
    Filter master cache sector_evals to (p,q) with p+q <= L; within each
    kept sector apply triality (p-q) mod 3 != 0; sum |lambda_alpha|^{-8}.

Step 3 (Friedrich-Bar tail bound at substrate-distance-2 pole):
  Per S87 W11-3 precedent, tail beyond L=14 is bounded by
    tail(L>14) <= sum_{p+q > 14} dim(p,q)*16 * (eta_FB * sqrt(C_2(p,q)+1))^{-8}
  with eta_FB_lower = 0.40 (8% below empirical floor 0.4365 at sector (1,1)).
  Decay super-polynomially in (p+q); at pole s=4 the convergence is markedly
  faster than at pole s=3 due to the higher exponent (-8 vs -6).

Step 4 (Log-log fit):
  norm_canonical_FB = norm_HH1_M3C(L=14) + tail_FB_bound(L > 14 to L=100)
  deltas[L] = |norm_HH1_M3C(L) - norm_canonical_FB|
  log_L = log([10, 12, 14]); log_d = log(deltas)
  slope, intercept = polyfit(log_L, log_d, 1)
  alpha_HH1_emp_s4 = -slope; C_HH1 = exp(intercept)

Step 5 (Direction):
  Wodzicki/Connes d=4 substrate-physics prediction: alpha_HH1(s=4) = 4 > 0.
  Empirical alpha_HH1_emp_s4 MUST also be strictly positive to match the
  substrate-physics direction. Container-thinking FORBIDDEN:
  "the L_max=14 master cache CONTAINS the cocycle norm" -> INVERT:
  "the cocycle norm IS substrate-IS at the Peter-Weyl eigenvalue-gap layer
  of D_K on M_3(C) c A_K; the L_max=14 master cache IS the methodology-floor
  F-image at the cache-projection evaluation convention".

Step 6 (Decision band):
  PASS iff alpha_HH1_emp_s4 in [1.5, 4.0] AND
       ABS(alpha_HH1_emp_s4 - 4) <= 1.5 AND
       sub-option (b) FB floor >= 0.40 AND
       sub-option (c) truncation_consistent across {6,8,10,12,14} AND
       sub-option (d) substrate-physics direction match (alpha > 0)
  INFO iff alpha_HH1_emp_s4 in (0, 1.5) U (4.0, +inf) AND direction matches
  FAIL otherwise (negative, direction inversion, FB violation, or trunc-inconsistent)

DISCIPLINE
----------
- from canonical_constants import *
- Every local/intermediate tagged # (local)
- LEVEL pin = FULL (substrate-natural FULL CM-1995 §III.4 simple-pole residue
  evaluator; NOT SCHEMATIC _spectral_action_regulators.py per substrate-first-
  canonical-sourcing.md §(iv) K=4 MANDATORY level-pin discipline)
- MACHINERY-SCOPE pin = CACHE-PROJECTION (consumes L_max=14 master cache +
  Friedrich-Bar tail bound)
- Binding axis pin = substrate-natural-binding (HH^1 cocycle norm IS the
  substrate's intrinsic Hochschild first-cohomology functional)
- a_n^{Mellin} regulator pin per regulator-pin-discipline.md MANDATORY
  tagging for Seeley-DeWitt coefficient citations
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Schema-v2 3-tuple companion row REQUIRED ([SIGN] trigger per plan §W7-5;
  substitution chain Step 5 pre-registers alpha_HH1_emp(s=4) > 0 direction)

Substrate framing (per phononic-framing.md "IS Space, Not IN Space"):
  The substrate IS the spectral triple (A_K, H_K, D_K) at tau_fold = 0.19.
  The M_3(C) factor of A_K = C (+) H (+) M_3(C) IS the substrate's intrinsic
  strong-isospin / color-triplet sub-algebra. HH^1 cocycle norm IS the
  substrate's intrinsic Hochschild first-cohomology functional at substrate-
  distance-2 pole s=4; the L_max-scan IS the substrate's own envelope-
  extraction discipline. Direction:
  D_K eigenvalues at L_max=14 truncation -> Peter-Weyl per-sector cardinality
  decomposition on M_3(C) c A_K -> CM-1995 §III.4 simple-pole residue at
  s_0 = 4 -> per-shell log-log regression empirical alpha exponent ->
  comparison with Wodzicki/Connes d=4 substrate-physics prediction
  alpha_HH1(s=4) = 4 -> PASS/INFO/FAIL verdict at publication-precision floor.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — CPU thread cap (per math-scripts.md and computation-environment.md)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import time
import json
import hashlib
from pathlib import Path
from fractions import Fraction

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

# Canonical constants (MANDATORY first import per math-scripts.md)
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Wedderburn decomposition reference (M_3(C) block index pin)
from _schur_orthogonality_decomp import (  # noqa: E402
    A_F_BLOCK_NAMES,
    A_F_REAL_DIM_TARGET,
)

# FULL CM-1995 §III.4 simple-pole residue evaluator (substrate-natural;
# NOT SCHEMATIC _spectral_action_regulators.py per K=4 MANDATORY level-pin)
from _cm_1995_residue_formula import (  # noqa: E402
    su3_casimir,
    su3_dimension,
    CLASS as CM_1995_CLASS,
    REGULATOR_PIN as CM_1995_REGULATOR_PIN,
)


# ---------------------------------------------------------------------------
# Section 2 — Gate identifier + pre-registered machinery pins
# ---------------------------------------------------------------------------

GATE_ID = "S92-W7-CF-W8-CONSOLIDATED-6-CF-W9-10-A-HH-1-FIRST-EXTRACTION-S4"  # (local)
SCHEME = "full-cm-1995-iii-4-simple-pole-residue"  # (local)
CONVENTION = "substrate-distance-2-pole-s4-FULL"  # (local)

# Peter-Weyl block index for M_3(C) factor of A_K per Wedderburn decomposition
# A_F_BLOCK_NAMES = ("C", "H", "M_3(C)") with indices 0/1/2.
M3C_PETER_WEYL_BLOCK_INDEX = 2  # (local) Wedderburn block index pin: 0=C, 1=H, 2=M_3(C)
assert A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX] == "M_3(C)", \
    f"Wedderburn block index pin {M3C_PETER_WEYL_BLOCK_INDEX} must name M_3(C); " \
    f"got {A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX]!r}"

# Substrate-distance-2 pole s_0 = 4 (Mellin weight |D|^{-2s} = |lambda|^{-8})
s_0 = 4  # (local) substrate-distance-2 pole; central pole for this gate's first-extraction
SUBSTRATE_DISTANCE_POLE_S = s_0  # (local) alias for cross-script consistency
MELLIN_EXPONENT = -2 * s_0  # (local) = -8

# L_max scan range: deeper L-arm than S91 §W9-10 (which used {8, 10, 12})
# because at pole s=4 the per-shell convergence is faster than at s=3,
# and the L_max=14 master cache is now available.
L_SCAN = [10, 12, 14]  # (local) primary L_max-scan for log-log regression
L_MAX_OPERATIONAL = 14  # (local) canonical anchor for verdict line
L_MAX_ASYMPTOTIC_CUTOFF = 100  # (local) Friedrich-Bar tail integration upper bound

# Casimir-bound truncation-consistent scan (sub-option (c))
L_OP_SCAN = [6, 8, 10, 12, 14]  # (local) for truncation_consistent flag per plan §W7-5

# PASS band per plan §W7-5 strict_PASS_boundary
ALPHA_PASS_BAND_LOW = 1.5  # (local)
ALPHA_PASS_BAND_HIGH = 4.0  # (local)
ALPHA_PUBLICATION_TARGET = 4.0  # (local) Wodzicki/Connes d=4 prediction alpha_HH1(s=4) = 2(4-2) = 4
ALPHA_PUBLICATION_TOL = 1.5  # (local) ABS(alpha_emp - 4) <= 1.5 at publication-precision floor

# Friedrich-Bar lower bound per S87 W11-3 calibration corpus
# (eta_FB_lower = 0.40; 8.4% safety margin below empirical floor 0.4365 at sector (1,1))
ETA_FB_LOWER = 0.40  # (local) per math-scripts.md "Friedrich-Bar saturation theorem"

# K-spinor fiber dimension at each Peter-Weyl sector
K_SPINOR_DIM = 16  # (local) C^16 per dirac_spectrum.py module docstring

# Operational pins for verdict-line companion (4-axis pin compliance per
# substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin discipline)
LEVEL_PIN = "FULL"  # (local) substrate-natural FULL CM-1995 §III.4 evaluator (NOT SCHEMATIC)
MACHINERY_SCOPE_PIN = "CACHE-PROJECTION"  # (local) L_max=14 master cache + Friedrich-Bar tail bound
BINDING_AXIS_PIN = "substrate-natural-binding"  # (local) HH^1 cocycle norm IS substrate-IS
A_N_REGULATOR_PIN = "a_2^{Mellin}"  # (local) Mellin regulator per regulator-pin-discipline.md MANDATORY


# ---------------------------------------------------------------------------
# Section 3 — File paths
# ---------------------------------------------------------------------------

# L_max=14 master cache filename per plan §W7-5 machinery_pin_map
CACHE_L14_PATH = COMPUTATIONS_DIR / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
SCHUR_DECOMP_PATH = SHARED_DIR / "_schur_orthogonality_decomp.py"
CM_1995_RESIDUE_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"

OUT_NPZ = SESSION_DIR / "s92_w7_5_hh_1_first_extraction_s4.npz"
OUT_PNG = SESSION_DIR / "s92_w7_5_hh_1_first_extraction_s4.png"
VERDICT_TXT = SESSION_DIR / "s92_gate_verdicts.txt"

INPUT_FILES = [
    CACHE_L14_PATH,
    CANONICAL_PATH,
    SCHUR_DECOMP_PATH,
    CM_1995_RESIDUE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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


def compute_dual_sha(script_path, canonical_path, pins):
    """Return (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
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
# Section 5 — M_3(C) Wedderburn-block filter (triality based)
# ---------------------------------------------------------------------------

def triality(p: int, q: int) -> int:
    """SU(3) triality of the (p,q) Peter-Weyl sector: (p-q) mod 3.

    Canonical Wedderburn-to-Peter-Weyl correspondence per S88 W3a-14:
      - triality == 0: BdG-restricted (C + H) sector image of iota_*
      - triality != 0: M_3(C) Cartan-zone (color-charged) sub-algebra image
    """
    return (p - q) % 3


def is_m3c_sector(p: int, q: int) -> bool:
    """True iff (p,q) belongs to the M_3(C) Wedderburn block by triality."""
    return triality(p, q) != 0


# ---------------------------------------------------------------------------
# Section 6 — Cache loading (L_max=14 master spectrum)
# ---------------------------------------------------------------------------

def load_master_cache_L14():
    """Load the L_max=14 master cache and return sector_evals dict.

    Each value is a dict with keys 'dim' (Weyl dim of (p,q)), 'level' (p+q),
    and 'abs_evals' (1D numpy array of |lambda| values for all 16*dim K-spinor
    fiber eigenvalue copies at this sector).
    """
    cache = np.load(str(CACHE_L14_PATH), allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    return sector_evals  # dict[(p,q)] -> {'dim': int, 'level': int, 'abs_evals': np.ndarray}


def filter_to_m3c_block_at_L_max(sector_evals: dict, L_max: int):
    """Return list of (p, q, dim, abs_evals) for sectors satisfying BOTH
    (a) p + q <= L_max (Friedrich-Bar truncation per S87 W11-3) AND
    (b) (p - q) mod 3 != 0 (M_3(C) Wedderburn block by triality).
    """
    filtered = []  # (local)
    for (p, q), data in sector_evals.items():
        if (p + q) > L_max:
            continue
        if not is_m3c_sector(p, q):
            continue
        filtered.append((p, q, data["dim"], data["abs_evals"]))
    return filtered


# ---------------------------------------------------------------------------
# Section 7 — HH^1 cocycle norm on M_3(C) block at substrate-distance-2 pole s_0 = 4
# ---------------------------------------------------------------------------

def compute_hh1_norm_m3c_s4(sector_evals: dict, L_max: int):
    """HH^1 cocycle norm on M_3(C) Peter-Weyl block at substrate-distance-2
    pole s_0 = 4 (Mellin exponent -2s = -8) under Friedrich-Bar L_max truncation.

    norm_HH1_M3C(L; s=4) = sum_{(p,q): (p-q) mod 3 != 0, p+q <= L} sum_alpha
                              |lambda_alpha(p,q;tau_fold)|^{-8}

    The per-sector dim factor is already encoded in the abs_evals array
    size (= dim(p,q) * K_SPINOR_DIM = dim * 16); each fiber eigenvalue
    copy enters the sum once. Eigenvalues at |lambda| < SAFE_FLOOR are
    filtered out (zero-mode protection); none expected in M_3(C) at
    tau_fold = 0.19.

    Returns (norm_HH1, diagnostics_dict).
    """
    filtered = filter_to_m3c_block_at_L_max(sector_evals, L_max)  # (local)

    total = 0.0  # (local) accumulator for |lambda|^{-8} sum
    n_sectors = 0  # (local)
    n_evals_total = 0  # (local)
    n_evals_below_safe_floor = 0  # (local)
    SAFE_FLOOR = 1e-12  # (local) zero-mode protection
    eta_FB_floor_observed = float("inf")  # (local) running min of eta_FB per sector

    # Per-level (p+q) breakdown for partial-sum diagnostics
    per_level_sum = {}  # (local) p+q -> partial sum at that level
    # Per-sector Friedrich-Bar ratio table
    per_sector_eta_FB = {}  # (local) (p, q) -> eta_FB(p,q) at this sector

    for p, q, dim, abs_evals in filtered:
        level = p + q  # (local)
        safe_evals = abs_evals[abs_evals > SAFE_FLOOR]  # (local)
        n_safe = safe_evals.size  # (local)
        n_unsafe = abs_evals.size - n_safe  # (local)
        n_evals_below_safe_floor += n_unsafe

        # Mellin weight at pole s_0 = 4: |lambda|^{-8}
        contrib = float(np.sum(safe_evals ** MELLIN_EXPONENT))  # (local)
        total += contrib
        per_level_sum.setdefault(level, 0.0)
        per_level_sum[level] += contrib

        # Per-sector Friedrich-Bar ratio: eta_FB(p,q) = |lambda|_min / sqrt(C_2 + 1)
        lam_min_pq = float(np.min(safe_evals)) if n_safe > 0 else 0.0  # (local)
        C2_pq = su3_casimir(p, q)  # (local) Fraction-exact via _cm_1995_residue_formula
        denom = float(np.sqrt(float(C2_pq) + 1.0))  # (local)
        eta_FB_pq = lam_min_pq / denom if denom > 0 else 0.0  # (local)
        per_sector_eta_FB[(p, q)] = eta_FB_pq
        if eta_FB_pq < eta_FB_floor_observed:
            eta_FB_floor_observed = eta_FB_pq

        n_sectors += 1
        n_evals_total += abs_evals.size

    diagnostics = {
        "L_max": L_max,
        "n_sectors_M3C_in_L_max": n_sectors,
        "n_evals_M3C_in_L_max": n_evals_total,
        "n_evals_below_safe_floor": n_evals_below_safe_floor,
        "per_level_sum": per_level_sum,
        "per_sector_eta_FB": per_sector_eta_FB,
        "eta_FB_floor_observed": eta_FB_floor_observed,
        "eta_FB_floor_satisfied_against_pin": (eta_FB_floor_observed >= ETA_FB_LOWER),
    }
    return total, diagnostics


# ---------------------------------------------------------------------------
# Section 8 — Friedrich-Bar tail bound at substrate-distance-2 pole (canonical L_max -> inf proxy)
# ---------------------------------------------------------------------------

def weyl_dim(p: int, q: int) -> int:
    """SU(3) Weyl dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2 (integer)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def friedrich_baer_tail_bound_s4(L_canonical_anchor: int, L_max_extrapolation: int) -> float:
    """Friedrich-Bar tail bound for the M_3(C) HH^1 sum at pole s_0 = 4
    beyond L_canonical_anchor.

    For each (p,q) with L_canonical_anchor < p+q <= L_max_extrapolation and
    (p-q) mod 3 != 0:
      |lambda|_min(p,q) >= eta_FB_lower * sqrt(C_2(p,q) + 1)
    so contribution to |lambda|^{-8} sum bounded by
      contribution(p,q) <= dim(p,q) * K_SPINOR_DIM * (eta_FB_lower)^{-8}
                         * (C_2(p,q) + 1)^{-4}

    Returns conservative upper bound on tail contribution. At pole s=4
    (exponent -8) this decays as (C_2)^{-4} which is much faster than
    the (C_2)^{-3} at pole s=3, so the FB tail bound is tighter.
    """
    tail_total = 0.0  # (local)
    eta_FB_inv_8 = ETA_FB_LOWER ** MELLIN_EXPONENT  # (local) = (eta_FB)^{-8}; MELLIN_EXPONENT = -8
    for N in range(L_canonical_anchor + 1, L_max_extrapolation + 1):
        for p in range(N + 1):
            q = N - p
            if not is_m3c_sector(p, q):
                continue
            dim_pq = weyl_dim(p, q)  # (local)
            C2 = float(su3_casimir(p, q))  # (local) Fraction-exact
            denom = (C2 + 1.0) ** 4  # (local) |lambda|^{8} >= (eta_FB)^8 * (C_2+1)^4
            tail_total += dim_pq * K_SPINOR_DIM * eta_FB_inv_8 / denom
    return tail_total


# ---------------------------------------------------------------------------
# Section 9 — Log-log fit for alpha_HH1_emp(s=4)
# ---------------------------------------------------------------------------

def log_log_fit_alpha(L_scan: list, norm_at_L: dict, norm_canonical: float):
    """Extract alpha_HH1_emp(s=4) from log-log fit:
       |norm(L) - norm_canonical| ~ C * L^{-alpha}

    Returns (alpha_emp, C_HH1, deltas, log_L, log_d, residuals).
    """
    deltas = np.array([abs(norm_at_L[L] - norm_canonical) for L in L_scan],
                      dtype=np.float64)  # (local)
    log_L = np.log(np.array(L_scan, dtype=np.float64))  # (local)
    log_d = np.log(deltas)  # (local)

    # Linear regression log_d = slope * log_L + intercept
    slope, intercept = np.polyfit(log_L, log_d, 1)  # (local)
    alpha_emp = -float(slope)  # (local)
    C_HH1 = float(np.exp(intercept))  # (local)

    log_d_pred = slope * log_L + intercept  # (local)
    residuals = log_d - log_d_pred  # (local)
    return alpha_emp, C_HH1, deltas, log_L, log_d, residuals


# ---------------------------------------------------------------------------
# Section 10 — Casimir-bound truncation_consistent flag (sub-option (c))
# ---------------------------------------------------------------------------

def casimir_bound_truncation_consistent(sector_evals: dict, L_op_scan: list):
    """Sub-option (c): truncate L_max=14 master cache at L_op in {6,8,10,12,14}
    and report norm_HH1_M3C(s=4; L_op) per L_op.

    truncation_consistent flag: per the substrate's Casimir-bound prediction
    at substrate-distance-2 pole s=4, the higher Mellin exponent (-8)
    enforces faster convergence than at pole s=3. The truncation_consistent
    flag is True iff the relative difference between consecutive L_op values
    monotonically decreases (consistent with super-polynomial Friedrich-Bar
    convergence) AND the highest-L_op value is the largest (consistent with
    a positive sum of |lambda|^{-8} terms that all add).

    Returns (truncation_consistent_flag: bool, norms_per_L_op: dict).
    """
    norms_per_L_op = {}  # (local)
    for L_op in L_op_scan:
        norm_L_op, _ = compute_hh1_norm_m3c_s4(sector_evals, L_op)  # (local)
        norms_per_L_op[L_op] = norm_L_op

    # Monotonicity check: the sum |lambda|^{-8} over M_3(C) sectors strictly
    # grows as L_op grows (each new sector adds positive contributions).
    L_sorted = sorted(L_op_scan)  # (local)
    monotone_increasing = True  # (local)
    for k in range(1, len(L_sorted)):
        if norms_per_L_op[L_sorted[k]] < norms_per_L_op[L_sorted[k - 1]]:
            monotone_increasing = False
            break

    # Consistency-decay check: |norm(L_op) - norm(L_op_max)| / norm(L_op_max)
    # decreases monotonically as L_op approaches L_op_max
    rel_diffs = []  # (local) (L_op, rel_diff) pairs
    norm_anchor = norms_per_L_op[L_sorted[-1]]  # (local)
    for L_op in L_sorted:
        rel = abs(norms_per_L_op[L_op] - norm_anchor) / norm_anchor if norm_anchor != 0 else 0.0  # (local)
        rel_diffs.append((L_op, rel))

    # The relative-diff sequence (from L_op_min to L_op_max) must be non-increasing
    rel_diff_values = [r for _, r in rel_diffs]  # (local)
    decay_monotone = all(rel_diff_values[i] >= rel_diff_values[i + 1]
                          for i in range(len(rel_diff_values) - 1))  # (local)

    truncation_consistent_flag = monotone_increasing and decay_monotone  # (local)

    return truncation_consistent_flag, norms_per_L_op, rel_diffs


# ---------------------------------------------------------------------------
# Section 11 — Gate evaluation per plan §W7-5 decision predicate
# ---------------------------------------------------------------------------

def evaluate_gate(alpha_emp: float, eta_FB_floor_observed: float,
                  truncation_consistent_flag: bool):
    """Apply plan §W7-5 strict_PASS_boundary 4-sub-option conjunction.

    Returns (composite, sign_verdict, magnitude_verdict, regime_verdict,
             per_sub_option_results).
    """
    # Sub-option (a): band membership of alpha_emp
    sub_a_in_band = ALPHA_PASS_BAND_LOW <= alpha_emp <= ALPHA_PASS_BAND_HIGH if np.isfinite(alpha_emp) else False  # (local)

    # Sub-option (b): Friedrich-Bar floor satisfied
    sub_b_FB_satisfied = (eta_FB_floor_observed >= ETA_FB_LOWER)  # (local)

    # Sub-option (c): truncation_consistent flag
    sub_c_truncation_consistent = bool(truncation_consistent_flag)  # (local)

    # Sub-option (d): substrate-physics direction match
    # alpha_HH1_emp(s=4) > 0 AND ABS(alpha_emp - 4) <= 1.5 at publication-precision floor
    sub_d_direction_match = (
        np.isfinite(alpha_emp)
        and alpha_emp > 0
        and abs(alpha_emp - ALPHA_PUBLICATION_TARGET) <= ALPHA_PUBLICATION_TOL
    )  # (local)

    per_sub_option_results = {
        "sub_a_in_band_1p5_to_4p0": sub_a_in_band,
        "sub_b_FB_floor_satisfied_at_eta_FB_lower_0p40": sub_b_FB_satisfied,
        "sub_c_truncation_consistent_across_L_op_6_8_10_12_14": sub_c_truncation_consistent,
        "sub_d_direction_match_alpha_gt_0_and_within_1p5_of_4": sub_d_direction_match,
    }

    # Magnitude verdict (band membership)
    if not np.isfinite(alpha_emp):
        magnitude_verdict = "FAIL"  # (local)
    elif alpha_emp < ALPHA_PASS_BAND_LOW:
        # Outside band but positive -> INFO; <=0 -> FAIL
        if alpha_emp <= 0:
            magnitude_verdict = "FAIL"  # (local) negative or zero
        else:
            magnitude_verdict = "INFO"  # (local) envelope too coarse
    elif alpha_emp > ALPHA_PASS_BAND_HIGH:
        magnitude_verdict = "INFO"  # (local) envelope unusually tight
    else:
        magnitude_verdict = "PASS"  # (local) in admissibility band [1.5, 4.0]

    # Sign verdict (substitution chain Step 5 pre-registers alpha_emp > 0)
    if np.isfinite(alpha_emp) and alpha_emp > 0:
        sign_verdict = "PASS"  # (local) substrate-physics direction confirmed (positive envelope exponent)
    else:
        sign_verdict = "FAIL"  # (local) direction inversion / container-thinking violation

    # Regime verdict (Friedrich-Bar saturation theorem applicability)
    # At L_max=14 with FB tail bound at L=100 the saturation theorem operates
    # across full L_scan window; we report MARGINAL if FB floor violated,
    # BREAKDOWN if truncation_consistent FAILED (operator domain compromised).
    if not sub_c_truncation_consistent:
        regime_verdict = "BREAKDOWN"  # (local) truncation inconsistency = operator-domain failure
    elif not sub_b_FB_satisfied:
        regime_verdict = "MARGINAL"  # (local) FB floor violated; saturation theorem soft
    else:
        regime_verdict = "VALID"  # (local) FB saturation operates throughout L_scan

    # Composite-collapse rule per gate-verdicts.md S87+ schema-v2
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

    # All-AND of plan §W7-5 strict_PASS_boundary 4-sub-option conjunction:
    # if ANY sub-option FAILs while composite is PASS, downgrade to INFO
    # (consistent with plan's strict-AND specification at PASS predicate)
    if composite == "PASS" and not all(per_sub_option_results.values()):
        composite = "INFO"

    return composite, sign_verdict, magnitude_verdict, regime_verdict, per_sub_option_results


# ---------------------------------------------------------------------------
# Section 12 — Plotting
# ---------------------------------------------------------------------------

def make_plot(L_scan, norm_at_L, norm_canonical, alpha_emp, C_HH1,
              per_level_sum, norms_per_L_op, out_path):
    """Two-panel figure:
      (a) log-log scatter of deltas[L] vs L_scan with fitted line + Wodzicki/Connes target.
      (b) Casimir-bound truncation_consistent bar chart over L_op_scan.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # (local)

    # Panel (a): log-log fit at substrate-distance-2 pole s_0 = 4
    ax = axes[0]
    L_arr = np.array(L_scan, dtype=np.float64)  # (local)
    deltas = np.array([abs(norm_at_L[L] - norm_canonical) for L in L_scan],
                      dtype=np.float64)  # (local)
    ax.loglog(L_arr, deltas, "o-",
              label=r"$|\mathrm{norm}_{HH^1}^{M_3(\mathbb{C})}(L; s{=}4) - \mathrm{norm}_{\mathrm{canonical}}|$",
              color="tab:blue", linewidth=2, markersize=10)

    L_fine = np.linspace(L_arr.min() * 0.9, L_arr.max() * 1.1, 100)  # (local)
    fit_line = C_HH1 * L_fine ** (-alpha_emp)  # (local)
    ax.loglog(L_fine, fit_line, "--", color="tab:red",
              label=fr"fit: $\alpha_{{HH^1,\,\mathrm{{emp}}}}(s{{=}}4) = {alpha_emp:.4f}$")

    # Wodzicki/Connes d=4 target reference line at alpha = 4
    alpha_target_line = C_HH1 * L_fine ** (-ALPHA_PUBLICATION_TARGET)  # (local)
    ax.loglog(L_fine, alpha_target_line, ":", color="tab:green",
              label=fr"Wodzicki/Connes d=4 target $\alpha(s{{=}}4) = {ALPHA_PUBLICATION_TARGET}$")

    ax.set_xlabel(r"$L_{\max}$")
    ax.set_ylabel(r"$|\mathrm{norm}_{HH^1}^{M_3(\mathbb{C})}(L; s{=}4) - \mathrm{norm}_{\mathrm{canonical}}|$")
    ax.set_title(
        rf"HH$^1$ first-extraction at substrate-distance-2 pole $s=4$; "
        rf"$M_3(\mathbb{{C}})$ block at $\tau_{{\mathrm{{fold}}}}=0.190$"
    )
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, which="both", linestyle=":", alpha=0.5)

    # Panel (b): Casimir-bound truncation_consistent bar chart at L_op_scan
    ax = axes[1]
    L_op_sorted = sorted(norms_per_L_op.keys())  # (local)
    norms_op = [norms_per_L_op[L] for L in L_op_sorted]  # (local)
    ax.bar([str(L) for L in L_op_sorted], norms_op, color="tab:purple", alpha=0.7, edgecolor="black")
    ax.set_xlabel(r"$L_{\mathrm{op}}$ (Casimir-bound truncation)")
    ax.set_ylabel(r"$\mathrm{norm}_{HH^1}^{M_3(\mathbb{C})}(L_{\mathrm{op}}; s{=}4)$")
    ax.set_title(
        r"sub-option (c) Casimir-bound truncation$\_$consistent flag scan"
    )
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 13 — Verdict line emission (S87+ canonical + dual-SHA + 3-tuple + level-pin)
# ---------------------------------------------------------------------------

def append_verdict_line(composite, value, audit_sha, content_sha,
                        sign_verdict, magnitude_verdict, regime_verdict):
    """Append canonical verdict line + dual-SHA companion + S87+ 3-tuple
    companion row + 4-axis level-pin companion per gate-verdicts.md S87+
    Schema-v2 + W9a-99 split.
    """
    L_max_tag = L_MAX_OPERATIONAL  # (local)
    safe_value = str(value).replace("'", "\\'")  # (local)
    line = (
        f"{GATE_ID}: {composite} -- value='{safe_value}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_max_tag} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    companion_dual = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    companion_3tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; substitution chain Step 5 "
        f"pre-registers alpha_HH1_emp(s=4) > 0 direction at substrate-distance-2 pole; "
        f"Wodzicki/Connes d=4 prediction alpha_HH1(s=4) = 4)\n"
    )  # (local)
    companion_level = (
        f"# LEVEL_CLASS_PIN={LEVEL_PIN} MACHINERY_SCOPE_PIN={MACHINERY_SCOPE_PIN} "
        f"BINDING_AXIS_PIN={BINDING_AXIS_PIN} A_N_REGULATOR_PIN={A_N_REGULATOR_PIN} "
        f"# {GATE_ID} 4-axis pin compliance (FULL CM-1995 §III.4 simple-pole residue "
        f"evaluator on substrate-natural M_3(C) Wedderburn block; CACHE-PROJECTION "
        f"L_max=14 master cache + Friedrich-Bar tail bound; substrate-natural-binding "
        f"HH^1 cocycle norm; a_2^{{Mellin}} regulator)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion_dual)
        fp.write(companion_3tuple)
        fp.write(companion_level)


# ---------------------------------------------------------------------------
# Section 14 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Verify L_max=14 master cache exists
    if not CACHE_L14_PATH.exists():
        print(f"ERROR: L_max=14 master cache not found at {CACHE_L14_PATH}")
        return 1
    print(f"  tau_fold (canonical) = {float(tau_fold)}")  # noqa: F405
    print(f"  L_max master         = 14 (loaded from cache)")
    print(f"  L_scan operational   = {L_SCAN}")
    print(f"  L_op_scan (sub-c)    = {L_OP_SCAN}")
    print(f"  L_max asymptotic     = {L_MAX_ASYMPTOTIC_CUTOFF}")
    print(f"  M_3(C) block index   = {M3C_PETER_WEYL_BLOCK_INDEX} "
          f"({A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX]})")
    print(f"  substrate pole s_0   = {s_0} (Mellin exponent {MELLIN_EXPONENT})")
    print(f"  Wodzicki target      = alpha_HH1(s=4) = 2*(4-2) = {ALPHA_PUBLICATION_TARGET}")
    print(f"  CM-1995 evaluator CLASS pin = {CM_1995_CLASS} (regulator: {CM_1995_REGULATOR_PIN})")
    print()

    # 3. Load master cache and compute HH^1 cocycle norm on M_3(C) at each L in L_scan
    sector_evals = load_master_cache_L14()
    print(f"  master cache sectors loaded: {len(sector_evals)}")
    print()

    norm_at_L = {}  # (local) L -> norm_HH1_M3C(L; s=4)
    diagnostics_at_L = {}  # (local) L -> diagnostics dict
    print("Per-L HH^1 cocycle norm on M_3(C) block at pole s_0 = 4:")
    for L in L_SCAN:
        norm_L, diag_L = compute_hh1_norm_m3c_s4(sector_evals, L)
        norm_at_L[L] = norm_L
        diagnostics_at_L[L] = diag_L
        print(f"  L = {L:2d}: norm_HH1 = {norm_L:.6e}; "
              f"n_sectors_M3C = {diag_L['n_sectors_M3C_in_L_max']}; "
              f"eta_FB_floor_observed = {diag_L['eta_FB_floor_observed']:.6f}; "
              f"eta_FB pin satisfied = {diag_L['eta_FB_floor_satisfied_against_pin']}")
    print()

    # 4. Friedrich-Bar tail bound at substrate-distance-2 pole s_0 = 4 (canonical L_max -> inf proxy)
    tail_FB_bound_to_100 = friedrich_baer_tail_bound_s4(L_MAX_OPERATIONAL, L_MAX_ASYMPTOTIC_CUTOFF)  # (local)
    norm_canonical_FB = norm_at_L[L_MAX_OPERATIONAL] + tail_FB_bound_to_100  # (local)
    print(f"  Friedrich-Bar tail bound (L > {L_MAX_OPERATIONAL}, ≤ {L_MAX_ASYMPTOTIC_CUTOFF}): "
          f"{tail_FB_bound_to_100:.6e}")
    print(f"  norm_canonical_FB = norm_HH1_M3C(L=14) + tail_FB = {norm_canonical_FB:.6e}")
    print()

    # 5. Log-log fit for alpha_HH1_emp(s=4)
    alpha_HH1_emp, C_HH1, deltas, log_L, log_d, residuals = log_log_fit_alpha(
        L_SCAN, norm_at_L, norm_canonical_FB
    )
    print(f"  Log-log regression on L_scan = {L_SCAN}:")
    for L, d in zip(L_SCAN, deltas):
        print(f"    L = {L:2d}: delta = {d:.6e}")
    print(f"  alpha_HH1_emp(s=4) = {alpha_HH1_emp:.6f}")
    print(f"  C_HH1              = {C_HH1:.6e}")
    print(f"  log_d_residuals    = {residuals}")
    print()

    # 6. Sub-option (c): Casimir-bound truncation_consistent flag
    truncation_consistent_flag, norms_per_L_op, rel_diffs = casimir_bound_truncation_consistent(
        sector_evals, L_OP_SCAN
    )
    print(f"  Sub-option (c) Casimir-bound truncation_consistent scan:")
    for L_op, rel in rel_diffs:
        print(f"    L_op = {L_op:2d}: norm = {norms_per_L_op[L_op]:.6e}; "
              f"rel_diff_vs_L_op_max = {rel:.6e}")
    print(f"  truncation_consistent_flag = {truncation_consistent_flag}")
    print()

    # 7. Friedrich-Bar floor (across full L_scan; use L=14 as canonical)
    eta_FB_floor_observed_L14 = diagnostics_at_L[L_MAX_OPERATIONAL]["eta_FB_floor_observed"]  # (local)
    print(f"  Friedrich-Bar floor (L=14): eta_FB_floor_observed = {eta_FB_floor_observed_L14:.6f}")
    print(f"  FB floor pin: eta_FB_lower = {ETA_FB_LOWER}")
    print()

    # 8. Per-sector eta_FB table (sectors intersecting M_3(C) at L=14)
    per_sector_eta_FB_L14 = diagnostics_at_L[L_MAX_OPERATIONAL]["per_sector_eta_FB"]  # (local)
    print(f"  Per-sector Friedrich-Bar table (L=14, M_3(C) intersection): "
          f"{len(per_sector_eta_FB_L14)} sectors")
    # Print first 6 sectors as sample
    sorted_sectors = sorted(per_sector_eta_FB_L14.keys(), key=lambda pq: (pq[0] + pq[1], pq[0]))  # (local)
    for pq in sorted_sectors[:6]:
        print(f"    (p,q)={pq}: eta_FB = {per_sector_eta_FB_L14[pq]:.6f}")
    print(f"    ... ({len(per_sector_eta_FB_L14) - 6} more sectors)")
    print()

    # 9. Apply gate decision predicate per plan §W7-5 strict_PASS_boundary
    composite, sign_verdict, magnitude_verdict, regime_verdict, per_sub_option = evaluate_gate(
        alpha_HH1_emp, eta_FB_floor_observed_L14, truncation_consistent_flag
    )
    print(f"  Gate decision:")
    for k, v in per_sub_option.items():
        print(f"    {k} = {v}")
    print(f"  composite = {composite}")
    print(f"  sign_verdict = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict = {regime_verdict}")
    print()

    # 10. Publication-precision cross-check vs Wodzicki/Connes d=4 prediction
    abs_diff_from_target = abs(alpha_HH1_emp - ALPHA_PUBLICATION_TARGET)  # (local)
    print(f"  Wodzicki/Connes d=4 cross-check:")
    print(f"    alpha_HH1_emp(s=4)         = {alpha_HH1_emp:.6f}")
    print(f"    Wodzicki target alpha(s=4) = {ALPHA_PUBLICATION_TARGET}")
    print(f"    ABS(alpha_emp - target)    = {abs_diff_from_target:.6f}")
    print(f"    Within tol {ALPHA_PUBLICATION_TOL}? = {abs_diff_from_target <= ALPHA_PUBLICATION_TOL}")
    print()

    # 11. Build value string + dual-SHA verdict line
    # Convert per-sector eta_FB to a serializable representation for npz
    per_sector_pq_list = sorted(per_sector_eta_FB_L14.keys(), key=lambda pq: (pq[0] + pq[1], pq[0]))  # (local)
    per_sector_eta_FB_array = np.array(
        [per_sector_eta_FB_L14[pq] for pq in per_sector_pq_list], dtype=np.float64
    )  # (local)
    per_sector_pq_array = np.array(per_sector_pq_list, dtype=np.int32)  # (local)

    value_summary = (
        f"alpha_HH1_emp_s4={alpha_HH1_emp:.6f};"
        f"alpha_target_wodzicki_d4={ALPHA_PUBLICATION_TARGET};"
        f"abs_diff_from_target={abs_diff_from_target:.6f};"
        f"abs_diff_within_tol_1p5={abs_diff_from_target <= ALPHA_PUBLICATION_TOL};"
        f"in_pass_band_1p5_to_4p0={per_sub_option['sub_a_in_band_1p5_to_4p0']};"
        f"C_HH1={C_HH1:.6e};"
        f"norm_HH1_at_L10={norm_at_L[10]:.6e};"
        f"norm_HH1_at_L12={norm_at_L[12]:.6e};"
        f"norm_HH1_at_L14={norm_at_L[14]:.6e};"
        f"norm_canonical_FB={norm_canonical_FB:.6e};"
        f"tail_FB_bound_L14_to_L100={tail_FB_bound_to_100:.6e};"
        f"eta_FB_lower_pin={ETA_FB_LOWER};"
        f"eta_FB_floor_observed_L14={eta_FB_floor_observed_L14:.6f};"
        f"sub_b_FB_satisfied={per_sub_option['sub_b_FB_floor_satisfied_at_eta_FB_lower_0p40']};"
        f"truncation_consistent_flag={truncation_consistent_flag};"
        f"sub_d_direction_match={per_sub_option['sub_d_direction_match_alpha_gt_0_and_within_1p5_of_4']};"
        f"M3C_PETER_WEYL_BLOCK_INDEX={M3C_PETER_WEYL_BLOCK_INDEX};"
        f"M3C_block_name=M_3(C);"
        f"substrate_distance=2;"
        f"pole_s_0=4;"
        f"Mellin_exponent={MELLIN_EXPONENT};"
        f"downstream_consumer=§W7-6_per-pole_alpha_table_central_anchor"
    )  # (local)

    # 12. Save .npz data
    # Serialize per_level_sum (L=14) for diagnostics consumer
    per_level_L14 = diagnostics_at_L[L_MAX_OPERATIONAL]["per_level_sum"]  # (local)
    levels_keys = np.array(sorted(per_level_L14.keys()), dtype=np.int32)  # (local)
    levels_sums = np.array([per_level_L14[L] for L in sorted(per_level_L14.keys())], dtype=np.float64)  # (local)

    np.savez_compressed(
        OUT_NPZ,
        # Primary first-extraction result
        alpha_HH1_emp_s4=alpha_HH1_emp,
        alpha_target_wodzicki_d4=ALPHA_PUBLICATION_TARGET,
        abs_diff_from_target=abs_diff_from_target,
        C_HH1=C_HH1,
        # L-scan data
        L_scan=np.array(L_SCAN, dtype=np.int32),
        L_op_scan=np.array(L_OP_SCAN, dtype=np.int32),
        norm_at_L=np.array([norm_at_L[L] for L in L_SCAN], dtype=np.float64),
        norms_per_L_op=np.array([norms_per_L_op[L] for L in sorted(L_OP_SCAN)], dtype=np.float64),
        norm_canonical_FB=norm_canonical_FB,
        tail_FB_bound_to_100=tail_FB_bound_to_100,
        # Log-log fit data
        log_L=log_L,
        log_d=log_d,
        deltas=deltas,
        residuals=residuals,
        # Sub-option flags
        sub_a_in_band=per_sub_option['sub_a_in_band_1p5_to_4p0'],
        sub_b_FB_satisfied=per_sub_option['sub_b_FB_floor_satisfied_at_eta_FB_lower_0p40'],
        sub_c_truncation_consistent=per_sub_option['sub_c_truncation_consistent_across_L_op_6_8_10_12_14'],
        sub_d_direction_match=per_sub_option['sub_d_direction_match_alpha_gt_0_and_within_1p5_of_4'],
        truncation_consistent_flag=truncation_consistent_flag,
        # Friedrich-Bar diagnostics
        eta_FB_floor_observed_L14=eta_FB_floor_observed_L14,
        eta_FB_lower_pin=ETA_FB_LOWER,
        per_sector_pq=per_sector_pq_array,
        per_sector_eta_FB=per_sector_eta_FB_array,
        # Per-level partial sums at L=14
        per_level_keys=levels_keys,
        per_level_sums=levels_sums,
        # Verdict components
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # Constants pinned for downstream
        s_0=s_0,
        MELLIN_EXPONENT=MELLIN_EXPONENT,
        M3C_PETER_WEYL_BLOCK_INDEX=M3C_PETER_WEYL_BLOCK_INDEX,
        ALPHA_PASS_BAND_LOW=ALPHA_PASS_BAND_LOW,
        ALPHA_PASS_BAND_HIGH=ALPHA_PASS_BAND_HIGH,
        ALPHA_PUBLICATION_TARGET=ALPHA_PUBLICATION_TARGET,
        ALPHA_PUBLICATION_TOL=ALPHA_PUBLICATION_TOL,
    )
    print(f"  .npz saved: {OUT_NPZ.name}")

    # 13. Make plot
    make_plot(L_SCAN, norm_at_L, norm_canonical_FB, alpha_HH1_emp, C_HH1,
              per_level_L14, norms_per_L_op, OUT_PNG)
    print(f"  .png saved: {OUT_PNG.name}")
    print()

    # 14. Emit verdict line
    append_verdict_line(composite, value_summary, audit_sha, content_sha,
                         sign_verdict, magnitude_verdict, regime_verdict)
    print(f"  Verdict line appended to: {VERDICT_TXT.name}")
    print(f"    composite = {composite}")
    print(f"    value     = {value_summary[:120]}...")

    elapsed = time.time() - t0  # (local)
    print()
    print(f"=== DONE in {elapsed:.1f}s ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
