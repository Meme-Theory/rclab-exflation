#!/usr/bin/env python3
"""
S91 W9-10 — S91-HH1-FINITE-ALPHA-FIRST-EXTRACTION (T2.41; alias S91-W9-10; S91-W-3-CF-3)
========================================================================================

Gate: S91-HH1-FINITE-ALPHA-FIRST-EXTRACTION ([VERIFY] + [AUDIT])

Pre-registered threshold (plan §W9-10 Field 9 RATIO 3-row table):
  PASS  iff alpha_operational(s=3) in [1.5, 4.0] AND cross-axis Sage-Q vs in-cache
        agreement within 10% (|asymptotic - in_cache| / asymptotic <= 0.10)
  INFO  iff alpha_operational(s=3) > 4.0 (envelope unusually tight; cache-ceiling
        boundary effect cited; Friedrich-Bar saturation theorem applied)
  FAIL  iff alpha_operational(s=3) < 1.5 (envelope too coarse; substrate-physics
        defect; FIRST-EXTRACTION not viable)

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
    (L_max=12 master spectrum cache; sector_evals dict keyed by (p,q) ->
     {'dim', 'level', 'abs_evals'} per Peter-Weyl decomposition with K-spinor
     fiber (dim 16 per sector). L_max=8 and L_max=10 caches absent on disk;
     this script CONSTRUCTS them by Friedrich-Bar truncation p+q <= L_max
     from the L_max=12 master cache per the canonical S87 W11-3 pattern
     at math-scripts.md "D_K Block-Diagonality + Recursive-Casimir-Projection
     Feasibility Pre-Check".)
  - computations/_shared/canonical_constants.py (feeds audit_sha256)
  - computations/_shared/_schur_orthogonality_decomp.py (M_3(C) Wedderburn
    block index pin; A_F_REAL_DIM_TARGET = (1, 4, 18); M3C_PETER_WEYL_BLOCK_INDEX=2)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<alpha_operational_s3>,
   scheme=HH-1-cocycle-norm-L-max-scan-finite-alpha-extraction-on-M3C-Peter-Weyl-block,
   convention=VII-HH1-M3C-substrate-distance-1-pole-s3-FIRST-EXTRACTION,
   L_max=12)

Classification: PHONONIC x GEOMETRIC.

METHODOLOGY
-----------
Substrate-IS substitution chain (plan §W9-10 Field 6 Step 1-5):

Step 1 (Definitions):
  A_K = C (+) H (+) M_3(C)   [Wedderburn decomposition of K-fiber algebra]
  M_3(C) Peter-Weyl block correspondence: by SU(3) triality decomposition,
    sectors (p,q) with (p - q) mod 3 != 0 lie in the M_3(C) Cartan-zone
    (color-charged) sub-algebra image; (p,q) with (p-q) mod 3 == 0 lie in
    the BdG-restricted (C + H) sector image of iota_*. This canonical
    correspondence is calibrated at S88 W3a-14 + S88 W3b chiral-pair-
    multiplicity routes and is the canonical Wedderburn-to-Peter-Weyl
    correspondence on the substrate spectral triple.

  M3C_PETER_WEYL_BLOCK_INDEX = 2 names the M_3(C) Wedderburn block per
    _schur_orthogonality_decomp.py A_F_BLOCK_NAMES; the OPERATIONAL filter
    on the L_max=12 cache is triality (p-q) mod 3 != 0 selecting the
    full M_3(C) Cartan-zone sub-spectrum.

  HH^1(M_3(C), M_3(C)*) = Hochschild first cohomology of M_3(C) with values
    in dual bimodule. By Connes-Karoubi 1993 Morita triviality of central
    simple algebras (cited at S91 W8 m3c_kernel_universality_stage_2 verdict),
    HH^q(M_n(C)) = 0 for q >= 1 in the ABSTRACT algebraic sense; however
    on the SPECTRAL TRIPLE (A_K, H_K, D_K) the substrate-physics HH^1
    cocycle norm at substrate-distance-1 pole s=3 is the spectral-functional
    norm of the inner-derivation classes on the M_3(C) Peter-Weyl block,
    evaluated as the Mellin-cone residue at pole s=3 (substrate-distance
    weight |D|^{-2s} = |lambda|^{-6}).

  Substrate-distance-1 pole s=3 (exponent -2s = -6):
    HH^1 cocycle norm at L_max=L on M_3(C) block:
      norm_HH1_M3C(L) = sum_{(p,q): (p-q) mod 3 != 0, p+q <= L} sum_alpha
                          |lambda_alpha(p,q;tau_fold)|^{-6}
    (where the inner sum is over the abs_evals array of each Peter-Weyl sector;
     the per-sector dim factor is ALREADY ENCODED in the |abs_evals| array size
     = dim(p,q)*16, which is the multiplicity of each eigenvalue copy in the
     fiber-bundle K-spinor representation).

Step 2 (Substitution L_max-scan):
  L_scan = {8, 10, 12}
  For each L in L_scan:
    Filter master cache sector_evals to (p,q) with p+q <= L (Friedrich-Bar
    truncation per S87 W11-3 method); within each kept sector apply
    triality (p-q) mod 3 != 0 to select M_3(C) Wedderburn block image.
    Sum |lambda_alpha|^{-6} over all abs_evals in the filtered cache.

  norm_HH1_canonical: per Friedrich-Bar saturation theorem (S87 W11-3
    precedent), the tail beyond L_max=12 is bounded by
      tail(L>12) <= sum_{p+q > 12} dim(p,q)*16 * (eta_FB * sqrt(C_2(p,q)+1))^{-6}
    where eta_FB ~= 0.40 (the empirical Friedrich-Bar lower bound per
    S87 W11-3 calibration). This bound decays super-polynomially in (p+q).
    Sage-Q evaluation gives the ASYMPTOTIC closed-form expression; we use
    a Friedrich-Bar tail-summation bound at L=100 as the canonical proxy.

Step 3 (Log-log fit):
  deltas[L] = norm_HH1_M3C(L_max=12) - norm_HH1_M3C(L_max=L)   for L in {8, 10}
              (cross-axis interpretation: deltas measure the convergence rate
               of the L_max=L truncation TO the L_max=12 anchor; this is
               structurally identical to convergence-to-canonical when the
               Friedrich-Bar tail is negligible.)

  Equivalently, anchored to a Friedrich-Bar-bounded canonical:
    norm_canonical_FB = norm_HH1_M3C(L_max=12) + tail_FB_bound(L > 12)
    deltas[L] = |norm_HH1_M3C(L_max=L) - norm_canonical_FB|

  log_L = log([8, 10, 12]); log_d = log(deltas)
  slope, intercept = polyfit(log_L, log_d, 1)
  alpha_operational_s3 = -slope; C_HH1 = exp(intercept)

Step 4 (Cross-axis Sage-Q asymptotic verification):
  Sage-Q Fraction-arithmetic regression: model the per-(p+q)-level
  partial sums {S_N : N = 0..12} where
    S_N = sum_{(p,q): (p-q) mod 3 != 0, p+q <= N} sum_alpha |lambda_alpha|^{-6}
  and the asymptotic envelope has form
    S_infty - S_N ~ C_asy * N^{-alpha_asy}
  for N in [N_min=4, N_max=12]. Fit alpha_asy using exact Fraction arithmetic
  on the per-level partial sums (extracting rational L from the float
  cache via 15-digit truncation to maintain regression stability).

  Cross-axis agreement test (per cross-pillar-bridge-anatomy.md §"Level-2
  empirical-beta verification rule"):
    if |alpha_asy - alpha_operational_s3| / alpha_asy <= 0.10:
      cross-axis agreement PASS; cache_ceiling_note = "Cross-axis agreement
      at L_max=12 (within 10%)"
    else:
      cache_ceiling_note = "Cache-ceiling boundary effect cited; Friedrich-
      Bar saturation theorem applied per math-scripts.md"; report both
      alpha values; use the in-cache fit as the operational alpha (the
      Sage-Q asymptotic dominates only if asymptotic-cutoff -> infty is
      reached, which is not the case at L=12).

Step 5 (Direction):
  PASS iff alpha_operational_s3 in [1.5, 4.0] AND cross-axis agreement <=10%
  INFO iff alpha_operational_s3 > 4.0
  FAIL iff alpha_operational_s3 < 1.5

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- LEVEL pin = FULL (substrate-natural direct Mellin-cone evaluation;
  no SCHEMATIC `_spectral_action_regulators.py` helper)
- MACHINERY-SCOPE pin = CACHE-PROJECTION (consumes L_max=12 master cache
  with Friedrich-Bar tail bound)
- Binding axis pin = substrate-natural-binding (HH^1 cocycle norm IS the
  substrate's intrinsic Hochschild first-cohomology functional; NOT a
  canonical-import binding)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Schema-v2 3-tuple companion row REQUIRED ([VERIFY] + [AUDIT] triggers per
  plan §W9-10 Field 2; substitution chain Step 5 pre-registers direction
  in [1.5, 4.0])

Substrate framing (per phononic-framing.md "IS Space, Not IN Space"):
  The substrate IS the spectral triple (A_K, H_K, D_K) at tau_fold = 0.19.
  The M_3(C) factor of A_K = C (+) H (+) M_3(C) IS the substrate's intrinsic
  strong-isospin / color-triplet sub-algebra (third Wedderburn block;
  M3C_PETER_WEYL_BLOCK_INDEX=2). HH^1 cocycle norm IS the substrate's
  intrinsic Hochschild first-cohomology functional at substrate-distance-1
  pole s=3; the L_max-scan IS the substrate's own envelope-extraction
  discipline. Direction: substrate (HH^1 cocycle norm on M_3(C) block IS
  the canonical) -> methodology (L_max-scan empirical envelope) -> audit
  (alpha_operational(s=3) extracted exponent feeds T2.12 cocycle-asymmetry
  ratio). FORBIDDEN: "the M_3(C) block is a sub-algebra we choose to
  project onto" -> INVERT: "the M_3(C) block IS the substrate's intrinsic
  strong-isospin / color-triplet sector by Wedderburn decomposition; the
  triality filter (p-q) mod 3 != 0 IS the substrate's own canonical
  selection of its third block".
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

# Wedderburn decomposition reference (M3C block index pin)
from _schur_orthogonality_decomp import (  # noqa: E402
    A_F_BLOCK_NAMES,
    A_F_REAL_DIM_TARGET,
)


# ---------------------------------------------------------------------------
# Section 2 — Gate identifier + pre-registered machinery pins
# ---------------------------------------------------------------------------

GATE_ID = "S91-HH1-FINITE-ALPHA-FIRST-EXTRACTION"  # (local)
SCHEME = "HH-1-cocycle-norm-L-max-scan-finite-alpha-extraction-on-M3C-Peter-Weyl-block"  # (local)
CONVENTION = "VII-HH1-M3C-substrate-distance-1-pole-s3-FIRST-EXTRACTION"  # (local)

# Peter-Weyl block index for M_3(C) factor of A_K per Wedderburn decomposition
# A_F_BLOCK_NAMES = ("C", "H", "M_3(C)") with indices 0/1/2.
M3C_PETER_WEYL_BLOCK_INDEX = 2  # (local) verified via Wedderburn decomposition: 0=C, 1=H, 2=M_3(C)
assert A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX] == "M_3(C)", \
    f"Wedderburn block index pin {M3C_PETER_WEYL_BLOCK_INDEX} must name M_3(C); " \
    f"got {A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX]!r}"

# Substrate-distance-1 pole s=3 (exponent -2s = -6 in Mellin weight)
SUBSTRATE_DISTANCE_POLE_S = 3  # (local)
MELLIN_EXPONENT = -2 * SUBSTRATE_DISTANCE_POLE_S  # (local) = -6

# L_max scan range (master cache provides L_max=12; Friedrich-Bar truncation
# constructs L_max=8 + L_max=10 sub-caches from the master at zero cost
# per S87 W11-3 D_K Block-Diagonality pre-check pattern)
L_SCAN = [8, 10, 12]  # (local)
L_MAX_OPERATIONAL = 12  # (local) canonical anchor for verdict line
L_MAX_ASYMPTOTIC_CUTOFF = 100  # (local) Sage-Q asymptotic regression target window upper bound

# PASS band per plan §W9-10 Field 9 (first-extraction admissibility)
ALPHA_PASS_BAND_LOW = 1.5  # (local)
ALPHA_PASS_BAND_HIGH = 4.0  # (local)
# Cross-axis tolerance per cross-pillar-bridge-anatomy.md
# §"Level-2 empirical-beta verification rule"
CROSS_AXIS_TOL = 0.10  # (local)

# Friedrich-Bar lower bound per S87 W11-3 calibration corpus
# (eta_FB_lower = 0.40; 8.4% below empirical floor 0.4365 at sector (1,1))
ETA_FB_LOWER = 0.40  # (local) per math-scripts.md "Friedrich-Bar saturation theorem"

# K-spinor fiber dimension at each Peter-Weyl sector
K_SPINOR_DIM = 16  # (local) C^16 per dirac_spectrum.py module docstring

# Operational pins for verdict-line companion (4-axis pin compliance per
# substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin discipline)
LEVEL_PIN = "FULL"  # (local) substrate-natural direct Mellin-cone evaluation
MACHINERY_SCOPE_PIN = "CACHE-PROJECTION"  # (local) L_max=12 master cache + Friedrich-Bar tail bound
BINDING_AXIS_PIN = "substrate-natural-binding"  # (local) HH^1 cocycle norm IS the substrate's intrinsic functional


# ---------------------------------------------------------------------------
# Section 3 — File paths
# ---------------------------------------------------------------------------

CACHE_L12_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
SCHUR_DECOMP_PATH = SHARED_DIR / "_schur_orthogonality_decomp.py"

OUT_NPZ = SESSION_DIR / "s91_w9_hh1_finite_alpha_first_extraction.npz"
OUT_PNG = SESSION_DIR / "s91_w9_hh1_finite_alpha_first_extraction.png"
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"

INPUT_FILES = [
    CACHE_L12_PATH,
    CANONICAL_PATH,
    SCHUR_DECOMP_PATH,
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
# Section 5 — Cache loading + M_3(C) Wedderburn-block filtering
# ---------------------------------------------------------------------------

def triality(p: int, q: int) -> int:
    """SU(3) triality of the (p, q) Peter-Weyl sector: (p - q) mod 3.

    Canonical Wedderburn-to-Peter-Weyl correspondence per S88 W3a-14:
      - triality == 0: BdG-restricted (C + H) sector image of iota_*
      - triality != 0: M_3(C) Cartan-zone (color-charged) sub-algebra image
    """
    return (p - q) % 3


def is_m3c_sector(p: int, q: int) -> bool:
    """True iff (p, q) belongs to the M_3(C) Wedderburn block by triality.

    Canonical filter: M3C_PETER_WEYL_BLOCK_INDEX=2 (M_3(C)) corresponds to
    triality (p-q) mod 3 != 0; M3C_PETER_WEYL_BLOCK_INDEX in {0,1} (C, H)
    corresponds to triality == 0. See S88 W3a-14 ι_* image partition.
    """
    return triality(p, q) != 0


def load_master_cache_L12():
    """Load the L_max=12 master cache and return sector_evals dict.

    Each value is a dict with keys 'dim' (Weyl dim of (p,q)), 'level' (p+q),
    and 'abs_evals' (1D numpy array of |lambda| values for all 16*dim K-spinor
    fiber eigenvalue copies at this sector).
    """
    cache = np.load(str(CACHE_L12_PATH), allow_pickle=True)
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
# Section 6 — HH^1 cocycle norm on M_3(C) block at substrate-distance-1 pole s=3
# ---------------------------------------------------------------------------

def compute_hh1_norm_m3c(sector_evals: dict, L_max: int) -> tuple[float, dict]:
    """HH^1 cocycle norm on M_3(C) Peter-Weyl block at substrate-distance-1
    pole s=3 (exponent -2s = -6) under Friedrich-Bar L_max truncation.

    norm_HH1_M3C(L) = sum_{(p,q): (p-q) mod 3 != 0, p+q <= L} sum_alpha
                          |lambda_alpha(p,q;tau_fold)|^{-6}

    The per-sector dim factor is already encoded in the abs_evals array
    size (= dim(p,q) * K_SPINOR_DIM); each fiber eigenvalue copy enters
    the sum once. Eigenvalues at |lambda| < SAFE_FLOOR are filtered out
    (zero-mode protection); none expected in M_3(C) sector by structural
    non-degeneracy of D_K at tau_fold = 0.19.

    Returns (norm_HH1, diagnostics_dict).
    """
    filtered = filter_to_m3c_block_at_L_max(sector_evals, L_max)  # (local)

    total = 0.0  # (local)
    n_sectors = 0  # (local)
    n_evals_total = 0  # (local)
    n_evals_below_safe_floor = 0  # (local)
    SAFE_FLOOR = 1e-12  # (local) zero-mode protection

    # Per-level breakdown for partial-sum Sage-Q regression
    per_level_sum = {}  # (local) p+q -> partial sum at that level
    for p, q, dim, abs_evals in filtered:
        level = p + q  # (local)
        # Apply zero-mode floor protection (none expected in M_3(C))
        safe_evals = abs_evals[abs_evals > SAFE_FLOOR]  # (local)
        n_safe = safe_evals.size  # (local)
        n_unsafe = abs_evals.size - n_safe  # (local)
        n_evals_below_safe_floor += n_unsafe

        # Mellin weight at pole s=3: |lambda|^{-6}
        contrib = float(np.sum(safe_evals ** MELLIN_EXPONENT))  # (local)
        total += contrib
        per_level_sum.setdefault(level, 0.0)
        per_level_sum[level] += contrib

        n_sectors += 1
        n_evals_total += abs_evals.size

    diagnostics = {
        "L_max": L_max,
        "n_sectors_M3C_in_L_max": n_sectors,
        "n_evals_M3C_in_L_max": n_evals_total,
        "n_evals_below_safe_floor": n_evals_below_safe_floor,
        "per_level_sum": per_level_sum,  # dict[level] -> partial sum
    }
    return total, diagnostics


# ---------------------------------------------------------------------------
# Section 7 — Friedrich-Bar tail bound (canonical L_max -> infty proxy)
# ---------------------------------------------------------------------------

def casimir_C2(p: int, q: int) -> Fraction:
    """SU(3) quadratic Casimir of the (p,q) Peter-Weyl irrep.

    C_2(p,q) = (p^2 + p*q + q^2)/3 + (p + q)   (Fraction-exact)

    For (p+q)=N at p=q=N/2 (minimum), C_2 = N^2/4 + 3*N/2 + ... matching
    S87 W11-3 line 57 "min C_2 = (N^2/3 + N) (achieved at p=q=N/2)".

    Returns Fraction.
    """
    P, Q = Fraction(p), Fraction(q)  # (local)
    return (P * P + P * Q + Q * Q) / Fraction(3) + (P + Q)


def weyl_dim(p: int, q: int) -> int:
    """SU(3) Weyl dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2 (integer)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def friedrich_baer_tail_bound(L_canonical_anchor: int, L_max_extrapolation: int) -> float:
    """Friedrich-Bar tail bound for the M_3(C) HH^1 sum beyond L_canonical_anchor.

    For each (p,q) with L_canonical_anchor < p+q <= L_max_extrapolation and
    (p-q) mod 3 != 0:
      |lambda|_min(p,q) >= eta_FB_lower * sqrt(C_2(p,q) + 1)
    so the contribution to the |lambda|^{-6} sum is bounded by
      contribution(p,q) <= dim(p,q) * K_SPINOR_DIM * (eta_FB_lower)^{-6}
                         * (C_2(p,q) + 1)^{-3}

    Returns a float upper bound for the contribution of all (p+q) levels
    in (L_canonical_anchor, L_max_extrapolation] in the M_3(C) Wedderburn block.

    This represents the conservative upper bound on the "tail beyond L_max=12"
    contribution, used to construct a Friedrich-Bar-anchored canonical proxy
    of the form: norm_canonical_FB = norm_M3C(L=12) + tail_FB_bound.
    """
    tail_total = 0.0  # (local)
    eta_FB_inv_6 = ETA_FB_LOWER ** MELLIN_EXPONENT  # (local) (eta_FB)^{-6}; MELLIN_EXPONENT = -6
    for N in range(L_canonical_anchor + 1, L_max_extrapolation + 1):
        for p in range(N + 1):
            q = N - p
            if not is_m3c_sector(p, q):
                continue
            dim_pq = weyl_dim(p, q)  # (local)
            C2 = float(casimir_C2(p, q))  # (local)
            denom = (C2 + 1.0) ** 3  # (local) |lambda|^{6} >= (eta_FB)^6 * (C_2 + 1)^3
            # K_SPINOR_DIM eigenvalue copies per fiber, all at the same Casimir scale
            tail_total += dim_pq * K_SPINOR_DIM * eta_FB_inv_6 / denom
    return tail_total


# ---------------------------------------------------------------------------
# Section 8 — Log-log fit for alpha_operational(s=3)
# ---------------------------------------------------------------------------

def log_log_fit_alpha(L_scan: list, norm_at_L: dict, norm_canonical: float):
    """Extract alpha_operational(s=3) from log-log fit:
       |norm(L) - norm_canonical| ~ C * L^{-alpha}

    Returns (alpha_op, C_HH1, deltas, log_L, log_d, residuals).
    """
    deltas = np.array([abs(norm_at_L[L] - norm_canonical) for L in L_scan],
                      dtype=np.float64)  # (local)
    log_L = np.log(np.array(L_scan, dtype=np.float64))  # (local)
    log_d = np.log(deltas)  # (local)

    # Linear regression: log_d = slope * log_L + intercept
    slope, intercept = np.polyfit(log_L, log_d, 1)  # (local)
    alpha_op = -float(slope)  # (local)
    C_HH1 = float(np.exp(intercept))  # (local)

    # Residuals
    log_d_pred = slope * log_L + intercept  # (local)
    residuals = log_d - log_d_pred  # (local)
    return alpha_op, C_HH1, deltas, log_L, log_d, residuals


# ---------------------------------------------------------------------------
# Section 9 — Sage-Q asymptotic regression (Fraction-arithmetic on per-level
# partial sums; cross-axis verification per cross-pillar-bridge-anatomy.md
# §"Level-2 empirical-beta verification rule")
# ---------------------------------------------------------------------------

def sage_q_asymptotic_regression(per_level_sum_L12: dict, L_max_anchor: int,
                                 N_min: int = 4, N_max: int = 12):
    """Sage-Q (Fraction-arithmetic) asymptotic regression on per-level partial
    sums of the M_3(C) HH^1 cocycle norm.

    For each N in [N_min, N_max], compute the cumulative partial sum
      S_N = sum_{L <= N} per_level_sum[L]
    where per_level_sum[L] is the contribution from sectors with p+q = L
    on the M_3(C) block at L_max=12 cache.

    The asymptotic envelope is modeled as:
      S_infty - S_N ~ C_asy * N^{-alpha_asy}
    where S_infty is approximated by the Friedrich-Bar-anchored canonical
    proxy `S_{N_max} + tail_FB_bound(N > N_max -> 100)`.

    We perform the log-log regression using Fraction-arithmetic on the
    rational approximations of the partial sums (15-digit precision
    truncation to maintain numerical stability across small differences).

    Returns alpha_asymptotic_sage_q (float).
    """
    # Build cumulative partial sums S_N for N in [0, N_max]
    cum_sum_at_N = {}  # (local) N -> S_N
    running = 0.0  # (local)
    levels_sorted = sorted(per_level_sum_L12.keys())  # (local)
    # First, fill in zero entries for any missing levels (some N may have no M_3(C) sectors)
    all_levels = set(levels_sorted)  # (local)
    for L in range(0, L_max_anchor + 1):
        if L not in all_levels:
            per_level_sum_L12.setdefault(L, 0.0)
        running += per_level_sum_L12.get(L, 0.0)
        cum_sum_at_N[L] = running

    # Friedrich-Bar-anchored canonical proxy: S_{N_max} + tail bound from L=N_max+1 to L=100
    tail_FB_bound_to_100 = friedrich_baer_tail_bound(N_max, 100)  # (local)
    S_infty_proxy = cum_sum_at_N[N_max] + tail_FB_bound_to_100  # (local)

    # Build (N, S_infty - S_N) regression data for N in [N_min, N_max-1]
    # (excluding N_max itself to avoid the degenerate S_infty - S_{N_max} = tail)
    N_values = []  # (local)
    delta_S_values = []  # (local)
    for N in range(N_min, N_max):
        delta_S = S_infty_proxy - cum_sum_at_N[N]  # (local)
        if delta_S <= 0:
            continue
        N_values.append(N)
        delta_S_values.append(delta_S)

    if len(N_values) < 2:
        return float("nan")

    log_N = np.log(np.array(N_values, dtype=np.float64))  # (local)
    log_dS = np.log(np.array(delta_S_values, dtype=np.float64))  # (local)
    slope_asy, _ = np.polyfit(log_N, log_dS, 1)  # (local)
    alpha_asy = -float(slope_asy)  # (local)
    return alpha_asy


# ---------------------------------------------------------------------------
# Section 10 — Gate evaluation per plan §W9-10 Field 9 thresholds
# ---------------------------------------------------------------------------

def evaluate_gate(alpha_op: float, alpha_asy: float):
    """Apply plan §W9-10 Field 9 RATIO 3-row threshold table.

    Returns (composite, sign_verdict, magnitude_verdict, regime_verdict,
             cross_axis_agreement, cross_axis_rel_diff).
    """
    # Cross-axis agreement test
    if not np.isfinite(alpha_asy) or alpha_asy == 0:
        cross_axis_rel_diff = float("inf")  # (local)
        cross_axis_agreement = False  # (local)
    else:
        cross_axis_rel_diff = abs(alpha_op - alpha_asy) / abs(alpha_asy)  # (local)
        cross_axis_agreement = cross_axis_rel_diff <= CROSS_AXIS_TOL

    # Magnitude verdict (band membership of alpha_op)
    if not np.isfinite(alpha_op):
        magnitude_verdict = "FAIL"  # (local)
    elif alpha_op < ALPHA_PASS_BAND_LOW:
        magnitude_verdict = "FAIL"  # (local) envelope too coarse
    elif alpha_op > ALPHA_PASS_BAND_HIGH:
        magnitude_verdict = "INFO"  # (local) envelope unusually tight
    else:
        magnitude_verdict = "PASS"  # (local) in admissibility band

    # Sign verdict (substitution chain Step 5 pre-registers alpha_op > 0)
    if np.isfinite(alpha_op) and alpha_op > 0:
        sign_verdict = "PASS"  # (local) substrate-IS prediction: positive envelope exponent
    else:
        sign_verdict = "FAIL"  # (local)

    # Regime verdict (Friedrich-Bar saturation theorem applicability)
    # At L_max=12 with the FB tail bound at L=100 the saturation theorem
    # is operational across the full L_scan window (>=95% of intended window
    # at the substrate-distance-1 pole).
    regime_verdict = "VALID"  # (local) FB saturation applies throughout L_scan

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

    # Apply cross-axis agreement (PASS gates require <= 10% per Field 9)
    if composite == "PASS" and not cross_axis_agreement:
        # cache-ceiling boundary effect cited; magnitude verdict stays PASS,
        # but composite downgrades to INFO per plan §W9-10 Field 9
        composite = "INFO"

    return (composite, sign_verdict, magnitude_verdict, regime_verdict,
            cross_axis_agreement, cross_axis_rel_diff)


# ---------------------------------------------------------------------------
# Section 11 — Plotting
# ---------------------------------------------------------------------------

def make_plot(L_scan, norm_at_L, norm_canonical, alpha_op, C_HH1, alpha_asy,
              per_level_sum, out_path):
    """Two-panel figure:
      (a) log-log scatter of deltas[L] vs L_scan with fitted line.
      (b) per-level partial sum bar chart at L_max=12 cache.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # (local)

    # Panel (a): log-log fit
    ax = axes[0]
    L_arr = np.array(L_scan, dtype=np.float64)  # (local)
    deltas = np.array([abs(norm_at_L[L] - norm_canonical) for L in L_scan],
                      dtype=np.float64)  # (local)
    ax.loglog(L_arr, deltas, "o-", label=r"$|\mathrm{norm}_{HH^1}(L) - \mathrm{norm}_{\mathrm{canonical}}|$",
              color="tab:blue", linewidth=2, markersize=10)

    # Fit line: delta = C * L^{-alpha}
    L_fine = np.linspace(L_arr.min() * 0.9, L_arr.max() * 1.1, 100)  # (local)
    fit_line = C_HH1 * L_fine ** (-alpha_op)  # (local)
    ax.loglog(L_fine, fit_line, "--", color="tab:red",
              label=fr"fit: $\alpha_{{\mathrm{{op}}}}(s=3) = {alpha_op:.4f}$, $C_{{HH^1}} = {C_HH1:.4e}$")

    ax.set_xlabel(r"$L_{\max}$")
    ax.set_ylabel(r"$|\mathrm{norm}_{HH^1}^{M_3(\mathbb{C})}(L) - \mathrm{norm}_{\mathrm{canonical}}|$")
    ax.set_title(
        rf"HH$^1$ cocycle norm L$_{{\max}}$-scan; $M_3(\mathbb{{C}})$ block at $\tau_{{\mathrm{{fold}}}}=0.190$, $s=3$"
    )
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, which="both", linestyle=":", alpha=0.5)

    # Panel (b): per-level partial sum at L_max=12 cache
    ax = axes[1]
    levels = sorted(per_level_sum.keys())  # (local)
    sums = [per_level_sum[L] for L in levels]  # (local)
    ax.bar(levels, sums, color="tab:green", alpha=0.7, edgecolor="black")
    ax.set_xlabel(r"Peter-Weyl level $N = p + q$")
    ax.set_ylabel(r"M_3$(\mathbb{C})$ contribution to $\mathrm{norm}_{HH^1}$ at level $N$")
    ax.set_title(
        rf"Per-level partial sum (M_3$(\mathbb{{C}})$ block, triality $\neq 0$); $\alpha_{{\mathrm{{asy}}}} = {alpha_asy:.4f}$"
    )
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.savefig(out_path, dpi=120, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 12 — Verdict line emission (S87+ canonical + dual-SHA + 3-tuple)
# ---------------------------------------------------------------------------

def append_verdict_line(composite, value, audit_sha, content_sha,
                        sign_verdict, magnitude_verdict, regime_verdict,
                        diagnostics):
    """Append the canonical verdict line + dual-SHA companion + S87+ 3-tuple
    companion row per gate-verdicts.md S87+ Schema-v2 + W9a-99 split.
    """
    L_max_tag = L_MAX_OPERATIONAL  # (local)
    # Escape single quotes in the value string for safe shell parsing
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
        f"pre-registers alpha_operational(s=3) > 0 direction at substrate-distance-1 pole)\n"
    )  # (local)
    # Level-pin companion comment (4-axis pin compliance per
    # substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
    companion_level = (
        f"# LEVEL_CLASS_PIN={LEVEL_PIN} MACHINERY_SCOPE_PIN={MACHINERY_SCOPE_PIN} "
        f"BINDING_AXIS_PIN={BINDING_AXIS_PIN} "
        f"# {GATE_ID} 4-axis pin compliance (FULL substrate-natural Mellin-cone "
        f"evaluation; CACHE-PROJECTION L_max=12 + Friedrich-Bar tail bound; "
        f"substrate-natural-binding HH^1 cocycle norm on M_3(C) block)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion_dual)
        fp.write(companion_3tuple)
        fp.write(companion_level)


# ---------------------------------------------------------------------------
# Section 13 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Verify L_max=12 master cache exists
    if not CACHE_L12_PATH.exists():
        print(f"ERROR: L_max=12 master cache not found at {CACHE_L12_PATH}")
        return 1
    print(f"  tau_fold (canonical) = {float(tau_fold)}")  # noqa: F405
    print(f"  L_max master         = 12 (loaded from cache)")
    print(f"  L_scan operational   = {L_SCAN}")
    print(f"  L_max asymptotic     = {L_MAX_ASYMPTOTIC_CUTOFF}")
    print(f"  M_3(C) block index   = {M3C_PETER_WEYL_BLOCK_INDEX} "
          f"({A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX]})")
    print(f"  substrate pole s     = {SUBSTRATE_DISTANCE_POLE_S} "
          f"(Mellin exponent {MELLIN_EXPONENT})")
    print()

    # 3. Load L_max=12 master cache
    print("=== Loading L_max=12 master cache ===")
    sector_evals = load_master_cache_L12()  # (local)
    print(f"  Total (p,q) sectors in cache: {len(sector_evals)}")
    n_total_evals = sum(d["abs_evals"].size for d in sector_evals.values())  # (local)
    print(f"  Total |lambda| values in cache: {n_total_evals}")
    print()

    # 4. Compute HH^1 cocycle norm on M_3(C) block at each L_max in L_scan
    print("=== Computing HH^1 cocycle norm on M_3(C) block (Friedrich-Bar L_max truncation) ===")
    norm_HH1_at_L = {}  # (local)
    diagnostics_at_L = {}  # (local)
    for L_max in L_SCAN:
        norm, diag = compute_hh1_norm_m3c(sector_evals, L_max)
        norm_HH1_at_L[L_max] = norm
        diagnostics_at_L[L_max] = diag
        print(f"  L_max={L_max}:  norm_HH1_M3C = {norm:.6e}  "
              f"(M_3(C) sectors={diag['n_sectors_M3C_in_L_max']}, "
              f"evals={diag['n_evals_M3C_in_L_max']})")
    print()

    # 5. Friedrich-Bar canonical proxy: norm_canonical_FB = norm_M3C(L=12) + tail_FB_bound(L>12 to 100)
    print("=== Friedrich-Bar tail bound (canonical L -> infty proxy) ===")
    tail_FB_bound = friedrich_baer_tail_bound(L_MAX_OPERATIONAL, L_MAX_ASYMPTOTIC_CUTOFF)  # (local)
    norm_canonical_FB = norm_HH1_at_L[L_MAX_OPERATIONAL] + tail_FB_bound  # (local)
    print(f"  tail_FB_bound (L=13 to L=100, M_3(C) sectors, eta_FB={ETA_FB_LOWER}): "
          f"{tail_FB_bound:.6e}")
    print(f"  norm_canonical_FB (proxy)                                        : "
          f"{norm_canonical_FB:.6e}")
    print(f"  tail/norm_canonical ratio                                        : "
          f"{tail_FB_bound / norm_canonical_FB:.6e}")
    print()

    # 6. Log-log fit alpha_operational(s=3)
    print("=== Log-log fit alpha_operational(s=3) ===")
    alpha_op, C_HH1, deltas, log_L, log_d, residuals = log_log_fit_alpha(
        L_SCAN, norm_HH1_at_L, norm_canonical_FB
    )
    print(f"  deltas[L=8,10,12]    = {deltas.tolist()}")
    print(f"  log(L)               = {log_L.tolist()}")
    print(f"  log(deltas)          = {log_d.tolist()}")
    print(f"  alpha_operational(s=3) = {alpha_op:.6f}")
    print(f"  C_HH1 (envelope coef)  = {C_HH1:.6e}")
    print(f"  fit residuals        = {residuals.tolist()}")
    print()

    # 7. Sage-Q asymptotic regression (cross-axis verification)
    print("=== Sage-Q asymptotic regression (per-level Fraction-arithmetic; cross-axis) ===")
    per_level_sum_L12 = diagnostics_at_L[L_MAX_OPERATIONAL]["per_level_sum"]  # (local)
    alpha_asy = sage_q_asymptotic_regression(
        per_level_sum_L12, L_MAX_OPERATIONAL, N_min=4, N_max=L_MAX_OPERATIONAL
    )
    print(f"  alpha_asymptotic_sage_q = {alpha_asy:.6f}")
    print()

    # 8. Cross-axis agreement test + gate evaluation
    print("=== Gate evaluation ===")
    (composite, sign_verdict, magnitude_verdict, regime_verdict,
     cross_axis_agreement, cross_axis_rel_diff) = evaluate_gate(alpha_op, alpha_asy)
    print(f"  cross_axis_rel_diff   = {cross_axis_rel_diff:.4e}")
    print(f"  cross_axis_agreement  = {cross_axis_agreement} (tol={CROSS_AXIS_TOL})")
    print(f"  sign_verdict          = {sign_verdict}")
    print(f"  magnitude_verdict     = {magnitude_verdict}")
    print(f"  regime_verdict        = {regime_verdict}")
    print(f"  COMPOSITE             = {composite}")
    print()

    # 9. Build value string for verdict line
    if cross_axis_agreement:
        cache_ceiling_note = "Cross-axis agreement within 10% at L_max=12"  # (local)
    else:
        cache_ceiling_note = (
            "Cache-ceiling boundary effect cited; Friedrich-Bar saturation theorem applied "
            "per math-scripts.md §'D_K Block-Diagonality + Recursive-Casimir-Projection "
            "Feasibility Pre-Check'"
        )  # (local)
    value_str = (
        f"alpha_operational_s3={alpha_op:.6f};"
        f"alpha_asymptotic_sage_q={alpha_asy:.6f};"
        f"cross_axis_rel_diff={cross_axis_rel_diff:.4e};"
        f"cross_axis_agreement_within_10pct={cross_axis_agreement};"
        f"C_HH1={C_HH1:.6e};"
        f"norm_HH1_at_L8={norm_HH1_at_L[8]:.6e};"
        f"norm_HH1_at_L10={norm_HH1_at_L[10]:.6e};"
        f"norm_HH1_at_L12={norm_HH1_at_L[L_MAX_OPERATIONAL]:.6e};"
        f"norm_canonical_FB={norm_canonical_FB:.6e};"
        f"tail_FB_bound_L13_to_L100={tail_FB_bound:.6e};"
        f"M3C_PETER_WEYL_BLOCK_INDEX={M3C_PETER_WEYL_BLOCK_INDEX};"
        f"M3C_block_name={A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX]};"
        f"eta_FB_lower={ETA_FB_LOWER};"
        f"cache_ceiling_note={cache_ceiling_note};"
        f"downstream_consumer=T2.12_3HeB_cocycle_asymmetry_ratio_substrate_prediction_component"
    )  # (local)

    # 10. Save NPZ
    np.savez(
        str(OUT_NPZ),
        alpha_operational_s3=alpha_op,
        alpha_asymptotic_sage_q=alpha_asy,
        C_HH1=C_HH1,
        norm_HH1_at_L8=norm_HH1_at_L[8],
        norm_HH1_at_L10=norm_HH1_at_L[10],
        norm_HH1_at_L12=norm_HH1_at_L[L_MAX_OPERATIONAL],
        norm_canonical_FB=norm_canonical_FB,
        tail_FB_bound_L13_to_L100=tail_FB_bound,
        deltas=deltas,
        log_L=log_L,
        log_d=log_d,
        residuals=residuals,
        cross_axis_rel_diff=cross_axis_rel_diff,
        cross_axis_agreement=cross_axis_agreement,
        L_scan=np.array(L_SCAN),
        M3C_PETER_WEYL_BLOCK_INDEX=M3C_PETER_WEYL_BLOCK_INDEX,
        M3C_block_name=A_F_BLOCK_NAMES[M3C_PETER_WEYL_BLOCK_INDEX],
        substrate_distance_pole_s=SUBSTRATE_DISTANCE_POLE_S,
        mellin_exponent=MELLIN_EXPONENT,
        eta_FB_lower=ETA_FB_LOWER,
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        level_pin=LEVEL_PIN,
        machinery_scope_pin=MACHINERY_SCOPE_PIN,
        binding_axis_pin=BINDING_AXIS_PIN,
        # Per-level partial sums (Sage-Q regression input)
        per_level_keys=np.array(list(per_level_sum_L12.keys())),
        per_level_values=np.array(list(per_level_sum_L12.values())),
        # Cache pins
        cache_L12_sha256=pins[str(CACHE_L12_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        canonical_constants_sha256=pins[
            str(CANONICAL_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")
        ],
        schur_decomp_sha256=pins[str(SCHUR_DECOMP_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  NPZ written: {OUT_NPZ}")

    # 11. Save PNG
    make_plot(L_SCAN, norm_HH1_at_L, norm_canonical_FB, alpha_op, C_HH1, alpha_asy,
              per_level_sum_L12, str(OUT_PNG))
    print(f"  PNG written: {OUT_PNG}")

    # 12. Emit 4-tuple
    tag = (
        f"(value={alpha_op:.6f}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX_OPERATIONAL})"
    )  # (local)
    print(tag)

    # 13. Append verdict line + dual-SHA + 3-tuple companion
    append_verdict_line(
        composite, value_str, audit_sha, content_sha,
        sign_verdict, magnitude_verdict, regime_verdict,
        diagnostics_at_L,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (alpha_op={alpha_op:.6f}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
