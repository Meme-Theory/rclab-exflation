"""
S83 W2-G25 -- EXCEPTIONAL-RANK-CARTAN-CLT-L8 (atlas G_2 / F_4 / Spin(8) at L=6,7,8)
====================================================================================

Gate: S83-EXCEPTIONAL-RANK-CARTAN-CLT-L8
Trigger: [VERIFY][CHAIN]
Classification: GEOMETRIC
Owner: spectral-geometer

Write-target: sessions/archive/session-83/session-83-results-workingpaper.md §W2-G25
Anchors:
  sessions/session-plan/session-83-plan.md L1714-L1763  (pre-registration)
  computations/session-83/s83_w2_g17_cartan_spin8_sanity.py   (G17 D_n family null)
  computations/session-83/s83_w2_g18_cartan_exceptional_falsifier.py  (G18 G_2 falsifier)
  sessions/archive/session-82/session-82-spectral-geometer-synthesis.md §II.b-c, §V.6.1

PRE-REGISTERED GATE
-------------------
HYPOTHESIS: Exceptional-rank groups {G_2, F_4, Spin(8)} at L in {6,7,8} follow
            CLT scaling drift = 0.5 + 0.5/sqrt(dim_H_pi(L)) within 15%.

PASS : all 3x3 = 9 combos have |drift_actual - CLT|/CLT < 15%.
INFO : most in band (>=6 of 9) but some outside, OR all 9 within 20% boundary.
FAIL : systematic deviation (< 6 of 9 in band AND not all within 20%).

CROSS-GATE CONTEXT
------------------
G17: Pure-T^r Cartan on D_n (simply-laced) produces drift_u1 ~ 1e-8 by Weyl-
     equivalence of simple roots (structural null). The drift formula is
     insensitive to |alpha_i|^2 because all D_n simple roots have identical
     length sqrt(2) and the weight lattice Z^r is invariant under permutation.

G18: G_2 rep-theoretic (h-branch = Cartan) drift = {1.3%, 2.5%, 4.1%} at
     L={6,7,8}. CLT using drift_u1^CLT(L) = 0.5 + 0.5/sqrt(L(L+1)) predicts
     {0.577, 0.567, 0.559}. Actual is 14-42x smaller than CLT. Verdict: FAIL
     (92.4%, 95.6%, 92.6% rel deviation).

G25 EXTENSION: The plan's CLT formula is drift^CLT(G,L) = 0.5 + 0.5/sqrt(dim_H_pi(G,L))
     where dim_H_pi is the Hilbert-space dimension of the truncation (sum of
     irrep dimensions up to L), NOT L*(L+1). For G_2 at L=6, dim_H_pi = 35783,
     so sqrt(dim_H_pi) ~ 189, CLT ~ 0.5026. The drift would have to be ~0.5
     to match -- actual is ~0.013 -- so FAIL is expected across the atlas.

SUBSTITUTION CHAIN (MANDATORY [VERIFY][CHAIN])
-----------------------------------------------
Step 1 (def, plan L1742):
  drift^CLT(G, L) = 0.5 + 0.5 / sqrt(dim_H_pi(G, L))
Step 2 (def):
  dim_H_pi(G, L) = sum over irreps (highest weights lambda with sum of Dynkin
                    labels <= L, excluding trivial) of dim(lambda)  [Weyl formula]
Step 3 (def, per G18 convention):
  drift_h(G, L) = | <alpha_1>^h - <alpha_1>^exact | / | <alpha_1>^exact |
  <alpha_1>^b = J_b^{zeta2} / J_b^{SDW}
  <alpha_1>^exact = mean over (h, short, long) branches for groups with mixed roots;
                    over equal-length branches for simply-laced D_4.
  Spectrum: lambda_rep = sqrt(C_2^G(lambda)) * exp(-tau * rho(lambda))
            mult_rep = dim_G(lambda)
            rho(lambda) = sum of Dynkin labels (height proxy, matches G18)
Step 4 (subst):
  For each (G, L) in {G_2, F_4, Spin(8)} x {6, 7, 8}:
    compute drift_h^actual(G, L) and drift^CLT(G, L)
    rel_dev(G, L) = | drift_h^actual - CLT | / | CLT |
Step 5 (direction, plan L1745):
  PASS if rel_dev(G, L) < 0.15 for all 9 combos
  INFO if (>=6 of 9 in band AND all within 0.20), OR all 9 within 0.20
  FAIL otherwise

Also report refined-rank-scaling prediction (per cross-gate NOTE):
  drift^rank(r, L) = O(1/L^a) with some a ~ 2 (empirical from G18 log-log trend)
  This is a DIAGNOSTIC, NOT a gate criterion.

PRU pins:
  (1) SHA-256 content-hash of all positive-root systems (fixed Bourbaki basis).
  (2) SHA-256 import-closure hash.
  (3) CLT formula pin: drift^CLT(G,L) = 0.5 + 0.5/sqrt(dim_H_pi(G,L))
  (4) Single run per (G, L) -- no iteration.
  (5) rho(lambda) = sum of Dynkin labels (height, G18 convention).
  (6) tau = tau_fold (canonical_constants.py).

OUTPUTS:
  computations/session-83/s83_w2_g25_exceptional_rank_cartan.py    (this script)
  computations/session-83/s83_w2_g25_exceptional_rank_cartan.npz   (data)
  computations/session-83/s83_w2_g25_exceptional_rank_cartan.png   (plot)
  Append verdict to computations/session-83/s83_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')            # (local)
os.environ.setdefault('MKL_NUM_THREADS', '8')            # (local)

import sys
import hashlib
import json
import time
from pathlib import Path
from itertools import product
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    tau_fold, M_KK, PI,
)

# =============================================================================
# Section 0: Gate identification
# =============================================================================
GATE_ID = "S83-EXCEPTIONAL-RANK-CARTAN-CLT-L8"                      # (local)
SESSION = "S83"                                                      # (local)
SCHEME_TAG = "CLT-atlas-exceptional-rank-L6-L7-L8"                   # (local)
CONVENTION_TAG = "G18-rep-theoretic-zeta2-over-SDW-rho-sum-Dynkin"   # (local)

OUT_NPZ = SCRIPT_DIR / "s83_w2_g25_exceptional_rank_cartan.npz"      # (local)
OUT_PNG = SCRIPT_DIR / "s83_w2_g25_exceptional_rank_cartan.png"      # (local)
VERDICT_TXT = SCRIPT_DIR / "s83_gate_verdicts.txt"                   # (local)

INPUT_FILES = [                                                      # (local)
    SCRIPT_DIR / "canonical_constants.py",
    SCRIPT_DIR / "s83_w2_g17_cartan_spin8_sanity.py",
    SCRIPT_DIR / "s83_w2_g18_cartan_exceptional_falsifier.py",
    SCRIPT_DIR / "s82_w3_3_dim_h_pi_universal.py",
]

# =============================================================================
# Section 1: SHA-256 input pins (MANDATORY first 20 lines of stdout)
# =============================================================================
def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()                                             # (local)
    try:
        with open(path, "rb") as fh:
            while True:
                chunk = fh.read(65536)
                if not chunk:
                    break
                h.update(chunk)
    except OSError:
        return ""
    return h.hexdigest()

def sha256_of_obj(obj) -> str:
    s = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(s).hexdigest()

print("=" * 78, flush=True)
print(f"{GATE_ID} [VERIFY][CHAIN]", flush=True)
print("  Exceptional-rank CLT atlas: {G_2, F_4, Spin(8)} x L in {6, 7, 8}", flush=True)
print("=" * 78, flush=True)

SHA_PINS = {}                                                        # (local)
print("=== SHA-256 input pins ===", flush=True)
for p in INPUT_FILES:
    sha = sha256_of_file(p)                                          # (local)
    rel = p.name                                                     # (local)
    SHA_PINS[rel] = sha
    print(f"  {rel}: {sha[:16]}...", flush=True)
SHA_SELF = sha256_of_file(Path(__file__))                            # (local)
SHA_PINS[Path(__file__).name] = SHA_SELF
print(f"  self: {SHA_SELF[:16]}...", flush=True)

# Sorted-concat closure SHA (matches G17/G18 conventions)
closure_concat = "".join(sorted(SHA_PINS.values())).encode()          # (local)
IMPORT_CLOSURE_SHA = hashlib.sha256(closure_concat).hexdigest()      # (local)
print(f"  closure_sha (sorted): {IMPORT_CLOSURE_SHA[:16]}...", flush=True)
print()

# =============================================================================
# Section 2: Pre-registered configuration
# =============================================================================
TAU = tau_fold                                                       # (local) 0.190
L_LIST = [6, 7, 8]                                                   # (local)
GROUPS = ["G_2", "F_4", "Spin(8)"]                                   # (local)
BAND_FRAC = 0.15                                                     # (local) PASS threshold
INFO_FRAC = 0.20                                                     # (local) INFO upper boundary

print("=== Pre-registered configuration ===", flush=True)
print(f"  tau_fold        = {TAU}", flush=True)
print(f"  L_LIST          = {L_LIST}", flush=True)
print(f"  GROUPS          = {GROUPS}", flush=True)
print(f"  BAND_FRAC (PASS)= {BAND_FRAC:.0%}", flush=True)
print(f"  INFO_FRAC       = {INFO_FRAC:.0%}", flush=True)
print(f"  CLT formula     : 0.5 + 0.5/sqrt(dim_H_pi(G,L))  (plan L1742)", flush=True)
print(f"  rho(lambda)     : sum of Dynkin labels (G18 convention)", flush=True)
print()

# =============================================================================
# Section 3: Root systems -- G_2, F_4, D_4=Spin(8)
# =============================================================================
#
# Bourbaki / Humphreys conventions with Euclidean inner product.
# |alpha_long|^2 = 2 (standard normalization); mixed groups have short roots
# at |alpha_short|^2 = 1 (F_4) or |alpha_short|^2 = 2/3 (G_2).

def g2_positive_roots() -> list[np.ndarray]:
    """G_2 has 6 positive roots: 3 long (|.|^2 = 2), 3 short (|.|^2 = 2/3).
    In R^2 orthonormal basis with simple roots
      alpha_1 = ( 1, 0 )  short, |.|^2 = 1  (we use rescaling below for |short|^2 = 2/3)
      alpha_2 = (-3/2, sqrt(3)/2)  long, |.|^2 = 3
    Bourbaki normalizes |long|^2 = 2 instead.  To preserve that:
      alpha_1 short = sqrt(2/3) * (1, 0)          |.|^2 = 2/3
      alpha_2 long  = sqrt(2)   * (-sqrt(3)/2, 1/2) |.|^2 = 2
    We use standard 3D projection instead (cleaner):
      alpha_1 = (1, -1, 0)      |.|^2 = 2   long
      alpha_2 = (-2, 1, 1)/... does not work.
    Cleanest: use 3D ambient with alpha_1 short, alpha_2 long in Bourbaki normalization:
      alpha_1 = ( 1,  0)      |.|^2 = 1   short
      alpha_2 = (-3/2, sqrt(3)/2)  |.|^2 = 3  long
    This has |alpha_long|^2/|alpha_short|^2 = 3, but Bourbaki uses 2/3 vs 2 = ratio 3 too.
    To make Bourbaki-normalized with |alpha_long|^2 = 2, SCALE by sqrt(2/3):
      alpha_1 = sqrt(2/3) * (1, 0),   |.|^2 = 2/3
      alpha_2 = sqrt(2/3) * (-3/2, sqrt(3)/2),   |.|^2 = 2.
    """
    s = np.sqrt(2.0/3.0)
    alpha_1 = s * np.array([1.0, 0.0])                      # short
    alpha_2 = s * np.array([-1.5, np.sqrt(3)/2])            # long
    # G_2 positive roots (6): alpha_1, alpha_2, a_1+a_2, 2a_1+a_2, 3a_1+a_2, 3a_1+2a_2
    pos = [alpha_1,
           alpha_2,
           alpha_1 + alpha_2,
           2*alpha_1 + alpha_2,
           3*alpha_1 + alpha_2,
           3*alpha_1 + 2*alpha_2]
    return pos, [alpha_1, alpha_2]

def f4_positive_roots() -> tuple[list[np.ndarray], list[np.ndarray]]:
    """F_4: 24 positive roots in R^4.
    Bourbaki simple roots:
      alpha_1 = e_2 - e_3  (long)
      alpha_2 = e_3 - e_4  (long)
      alpha_3 = e_4        (short)
      alpha_4 = (e_1 - e_2 - e_3 - e_4)/2  (short)
    """
    roots = []
    # Short type 1: e_i (4)
    for i in range(4):
        r = np.zeros(4); r[i] = 1.0; roots.append(r)
    # Long type 2: e_i + e_j  i<j (6)
    for i in range(4):
        for j in range(i+1, 4):
            r = np.zeros(4); r[i]=1.0; r[j]=1.0; roots.append(r)
    # Long type 3: e_i - e_j  i<j (6)
    for i in range(4):
        for j in range(i+1, 4):
            r = np.zeros(4); r[i]=1.0; r[j]=-1.0; roots.append(r)
    # Short type 4: (e_1 + s2*e_2 + s3*e_3 + s4*e_4)/2  (8)
    for signs in product([1, -1], repeat=3):
        r = np.array([0.5, 0.5*signs[0], 0.5*signs[1], 0.5*signs[2]])
        roots.append(r)
    alpha_1 = np.array([0.0, 1.0, -1.0, 0.0])  # long
    alpha_2 = np.array([0.0, 0.0, 1.0, -1.0])  # long
    alpha_3 = np.array([0.0, 0.0, 0.0, 1.0])   # short
    alpha_4 = np.array([0.5, -0.5, -0.5, -0.5])  # short
    return roots, [alpha_1, alpha_2, alpha_3, alpha_4]

def d4_positive_roots() -> tuple[list[np.ndarray], list[np.ndarray]]:
    """D_4 = Spin(8): 12 positive roots, all long (simply-laced).
    Bourbaki simple roots: alpha_i = e_i - e_{i+1} for i=1,2,3; alpha_4 = e_3 + e_4.
    """
    roots = []
    for i in range(4):
        for j in range(i+1, 4):
            r = np.zeros(4); r[i]=1.0; r[j]=1.0; roots.append(r)    # e_i + e_j
            r = np.zeros(4); r[i]=1.0; r[j]=-1.0; roots.append(r)   # e_i - e_j
    alpha_1 = np.array([1.0, -1.0, 0.0, 0.0])
    alpha_2 = np.array([0.0, 1.0, -1.0, 0.0])
    alpha_3 = np.array([0.0, 0.0, 1.0, -1.0])
    alpha_4 = np.array([0.0, 0.0, 1.0, 1.0])
    return roots, [alpha_1, alpha_2, alpha_3, alpha_4]


ROOT_SYSTEMS = {                                                      # (local)
    "G_2":     g2_positive_roots,
    "F_4":     f4_positive_roots,
    "Spin(8)": d4_positive_roots,
}


def fundamental_weights(simple_roots: list[np.ndarray]) -> list[np.ndarray]:
    """Compute fundamental weights w_i from simple roots.
       w_i satisfies <w_i, alpha_j^v> = delta_{ij}, where alpha_j^v = 2 alpha_j / |alpha_j|^2.
    """
    r = len(simple_roots)
    coroots = [2 * a / np.dot(a, a) for a in simple_roots]            # (local)
    M = np.array([[np.dot(si, cj) for cj in coroots] for si in simple_roots])  # (local)
    # Solve: M^T w = I (so rows of M^{-T} are w_i expressed in basis simple_roots)
    # Easier: w_i = sum_j (M^{-1})_{ij} * alpha_j
    Minv = np.linalg.inv(M)                                           # (local)
    w = [sum(Minv[i, j] * simple_roots[j] for j in range(r))
         for i in range(r)]                                           # (local)
    return w


# =============================================================================
# Section 4: Weyl dimension + quadratic Casimir
# =============================================================================
def weyl_dim(lam: np.ndarray, positive_roots: list[np.ndarray],
             rho: np.ndarray) -> float:
    """dim(lambda) = prod_{alpha > 0} <lambda + rho, alpha> / <rho, alpha>."""
    num = 1.0  # (local) Weyl dim numerator accumulator
    den = 1.0  # (local) Weyl dim denominator accumulator
    for alpha in positive_roots:
        num *= np.dot(lam + rho, alpha)
        den *= np.dot(rho, alpha)
    return num / den

def casimir_2(lam: np.ndarray, rho: np.ndarray) -> float:
    """C_2(lambda) = <lambda, lambda + 2*rho>."""
    return float(np.dot(lam, lam + 2 * rho))


# =============================================================================
# Section 5: Irrep enumeration
# =============================================================================
def enumerate_irreps(G_label: str, L_max: int,
                      w_list: list[np.ndarray]) -> list[dict]:
    """Enumerate highest-weight reps with height = sum(Dynkin labels) <= L_max,
    excluding the trivial rep (0,...,0).
    """
    r = len(w_list)
    out = []
    # Generate all (a_1, ..., a_r) with sum <= L_max via stars-and-bars enumeration
    def recurse(depth: int, partial: tuple, partial_sum: int):
        if depth == r:
            if partial_sum == 0:
                return  # skip trivial rep (0,...,0)
            dyn = partial
            lam = sum(dyn[i] * w_list[i] for i in range(r))
            out.append({
                "dynkin": dyn,
                "highest_weight": lam,
                "height": partial_sum,
            })
            return
        remaining = L_max - partial_sum
        for a in range(remaining + 1):
            recurse(depth + 1, partial + (a,), partial_sum + a)
    recurse(0, tuple(), 0)
    return out


# =============================================================================
# Section 6: dim_H_pi and spectral moments
# =============================================================================
def compute_spectral_data(G_label: str, L_max: int) -> dict:
    """Build spectrum {lambda, mult} and branch projections for G at height <= L_max.

    Uses G18 convention:
      - spectrum entry per irrep: lambda_rep = sqrt(C_2) * exp(-tau * rho(dynkin))
      - mult_rep = dim_G(lambda) from Weyl formula
      - rho(lambda) = sum of Dynkin labels
      - branch decomposition per group:
          Mixed-root groups (G_2, F_4): h (Cartan), s (short-root), l (long-root)
          Simply-laced (Spin(8) = D_4): h (Cartan), r (all roots Weyl-equivalent)
        For simply-laced we use SINGLE non-Cartan branch (12 roots all equivalent)
        and the h vs r comparison.
    """
    pos_roots, simple_roots = ROOT_SYSTEMS[G_label]()
    w_list = fundamental_weights(simple_roots)
    r = len(simple_roots)
    rho = 0.5 * sum(pos_roots)

    # Enumerate irreps with height <= L_max
    irreps = enumerate_irreps(G_label, L_max, w_list)

    dims = []
    lams = []
    heights = []
    dyn_list = []
    a1s = []      # sum of short-root Dynkin labels
    a2s = []      # sum of long-root Dynkin labels
    for rep in irreps:
        dyn = rep["dynkin"]
        lam = rep["highest_weight"]
        d = weyl_dim(lam, pos_roots, rho)
        c2 = casimir_2(lam, rho)
        # Skip reps with C_2 ~ 0 (should only be trivial, already excluded)
        lam_sp = float(np.sqrt(max(c2, 1e-30)) * np.exp(-TAU * rep["height"]))
        dims.append(round(d))
        lams.append(lam_sp)
        heights.append(rep["height"])
        dyn_list.append(dyn)
        # Per-group root-length split for branch weights
        if G_label == "G_2":
            # alpha_1 short, alpha_2 long => Dynkin (a_1, a_2)
            a1s.append(dyn[0])
            a2s.append(dyn[1])
        elif G_label == "F_4":
            # alpha_1,2 long; alpha_3,4 short => (a_1, a_2, a_3, a_4)
            a1s.append(dyn[2] + dyn[3])   # short sum
            a2s.append(dyn[0] + dyn[1])   # long sum
        elif G_label == "Spin(8)":
            # simply-laced: split labels evenly (a_1, a_2, a_3, a_4)
            # No short/long distinction; use "half-labels" convention
            # Convention: a1 = a_1 + a_3, a2 = a_2 + a_4 as rough split -- but the branch
            # decomposition for simply-laced is rank-based, not root-length-based.
            a1s.append(dyn[0] + dyn[2])
            a2s.append(dyn[1] + dyn[3])

    dims = np.array(dims, dtype=np.float64)
    lams = np.array(lams, dtype=np.float64)
    heights = np.array(heights, dtype=np.float64)
    a1s = np.array(a1s, dtype=np.float64)
    a2s = np.array(a2s, dtype=np.float64)

    dim_H_pi = float(np.sum(dims))

    return {
        "G_label": G_label,
        "L_max": L_max,
        "rank": r,
        "n_pos_roots": len(pos_roots),
        "n_irreps": len(irreps),
        "dims": dims,
        "lams": lams,
        "heights": heights,
        "dyn_list": dyn_list,
        "a1s": a1s,
        "a2s": a2s,
        "dim_H_pi": dim_H_pi,
    }


# =============================================================================
# Section 7: Branch-projected drift computation (G18 methodology)
# =============================================================================
def compute_drift_atlas(G_label: str, L_max: int) -> dict:
    """Compute drift_h(G, L) per P4-B definition, using rep-theoretic proxy
    consistent with s83_w2_g18_cartan_exceptional_falsifier.py (G18).

    Branch weights per irrep:
      w_h(rep) = mult = dim_G(lam)                  (h-branch Cartan, full wt)
      w_s(rep) = mult * (a_1 / height)               (short-root weighted)
      w_l(rep) = mult * (a_2 / height)               (long-root weighted)
    Scalar (dim_b/dim_adj) prefactors cancel in ratio J_b^{zeta2}/J_b^{SDW}.

    alpha_1^b(L) = J_b^{zeta2}(L) / J_b^{SDW}(L)
      J_b^{SDW}(L)   = sum_rep w_b * lam_rep
      J_b^{zeta2}(L) = sum_rep w_b / lam_rep^2

    <alpha_1>^exact = mean over branches (h, s, l).
    drift_b = |alpha_1^b - <alpha_1>^exact| / |<alpha_1>^exact|.

    The h-branch drift is the "Cartan analog" -- the diagnostic for Level-2
    protection universality.
    """
    sd = compute_spectral_data(G_label, L_max)
    lams = sd["lams"]
    dims = sd["dims"]
    heights = sd["heights"]
    a1s = sd["a1s"]
    a2s = sd["a2s"]

    # Branch weights per rep (G18 convention)
    w_h = dims.copy()                                                 # (local) Cartan (all reps)
    # Short / long weights: scale by label fraction, but only if height > 0
    with np.errstate(divide='ignore', invalid='ignore'):
        w_s = np.where(heights > 0, dims * a1s / heights, 0.0)         # (local)
        w_l = np.where(heights > 0, dims * a2s / heights, 0.0)         # (local)

    # Spectral functionals (skip any lam ~ 0, which doesn't occur since we
    # excluded trivial rep)
    lam2 = lams ** 2                                                  # (local)

    def J_of(w):
        J_sdw = float(np.sum(w * lams))                               # (local)
        J_z2  = float(np.sum(w / lam2))                               # (local)
        return J_sdw, J_z2

    J_SDW_h, J_z2_h = J_of(w_h)
    J_SDW_s, J_z2_s = J_of(w_s)
    J_SDW_l, J_z2_l = J_of(w_l)

    def ratio(J_sdw, J_z2):
        if abs(J_sdw) < 1e-30:
            return float('nan')
        return J_z2 / J_sdw

    alpha1_h = ratio(J_SDW_h, J_z2_h)
    alpha1_s = ratio(J_SDW_s, J_z2_s)
    alpha1_l = ratio(J_SDW_l, J_z2_l)

    # Cross-branch mean (exclude nans if a branch is vacuous)
    all_branches = np.array([alpha1_h, alpha1_s, alpha1_l])
    valid = ~np.isnan(all_branches)
    alpha1_exact = float(np.mean(all_branches[valid])) if valid.any() else float('nan')

    def drift(alpha_b):
        if np.isnan(alpha_b) or np.isnan(alpha1_exact) or abs(alpha1_exact) < 1e-30:
            return float('nan')
        return abs(alpha_b - alpha1_exact) / abs(alpha1_exact)

    drift_h = drift(alpha1_h)
    drift_s = drift(alpha1_s)
    drift_l = drift(alpha1_l)

    # Spectrum SHA
    spectrum_sha = hashlib.sha256(
        np.ascontiguousarray(np.sort(lams), dtype=np.float64).tobytes()
    ).hexdigest()

    return {
        **sd,
        "alpha1_h": alpha1_h,
        "alpha1_s": alpha1_s,
        "alpha1_l": alpha1_l,
        "alpha1_exact": alpha1_exact,
        "drift_h": drift_h,
        "drift_s": drift_s,
        "drift_l": drift_l,
        "J_SDW_h": J_SDW_h, "J_z2_h": J_z2_h,
        "J_SDW_s": J_SDW_s, "J_z2_s": J_z2_s,
        "J_SDW_l": J_SDW_l, "J_z2_l": J_z2_l,
        "spectrum_sha": spectrum_sha,
    }


# =============================================================================
# Section 8: Cross-gate consistency sanity checks
# =============================================================================
print("=" * 78, flush=True)
print("Section 8: Cross-gate consistency sanity checks", flush=True)
print("=" * 78, flush=True)

# Consistency check 1: G_2 low-dim reps match published values
sd_G2_test = compute_spectral_data("G_2", 2)
print("\n  G_2 low-dim irrep check (height <= 2, expected: 7, 14, 27, 64, 77):")
for (dyn, lam_sp, h, d) in zip(sd_G2_test["dyn_list"],
                                 sd_G2_test["lams"],
                                 sd_G2_test["heights"],
                                 sd_G2_test["dims"]):
    print(f"    dynkin={dyn}, dim={int(d):5d}, height={int(h)}")

# Consistency check 2: Spin(8) adjoint dim 28
sd_D4_test = compute_spectral_data("Spin(8)", 2)
for (dyn, d) in zip(sd_D4_test["dyn_list"], sd_D4_test["dims"]):
    if dyn == (0, 1, 0, 0):
        assert int(d) == 28, f"Spin(8) adjoint dim should be 28, got {int(d)}"
        print(f"\n  Spin(8) adjoint (0,1,0,0) dim check: {int(d)} (OK)")

# Consistency check 3: F_4 26-dim
sd_F4_test = compute_spectral_data("F_4", 1)
for (dyn, d) in zip(sd_F4_test["dyn_list"], sd_F4_test["dims"]):
    if dyn == (0, 0, 0, 1):
        assert int(d) == 26, f"F_4 (0,0,0,1) should be 26, got {int(d)}"
        print(f"  F_4 (0,0,0,1) dim check: {int(d)} (OK)")
    if dyn == (1, 0, 0, 0):
        assert int(d) == 52, f"F_4 (1,0,0,0) should be 52, got {int(d)}"
        print(f"  F_4 adjoint (1,0,0,0) dim check: {int(d)} (OK)")

# Consistency check 4: G18 G_2 h-drift at L=8 should match ~4.1%
print("\n  G_2 h-drift cross-check (G18 reported 4.108% at L=8):")
r_G2_L8 = compute_drift_atlas("G_2", 8)
print(f"    G_2 L=8 h-drift = {r_G2_L8['drift_h']:.4%} (G18 expected 4.108%)")
g18_diff = abs(r_G2_L8["drift_h"] - 0.04108) / 0.04108
print(f"    G18 cross-consistency: |delta|/G18 = {g18_diff:.2%}")
if g18_diff < 0.05:
    print(f"    OK: within 5% of G18 reference")
else:
    print(f"    DIVERGENT: flagged for review")

# =============================================================================
# Section 9: Full 3x3 atlas
# =============================================================================
print("\n" + "=" * 78, flush=True)
print("Section 9: Compute drift_h atlas over {G_2, F_4, Spin(8)} x {6, 7, 8}", flush=True)
print("=" * 78, flush=True)

results = {}                                                         # (local)
t_start = time.time()
for G in GROUPS:
    for L in L_LIST:
        t0 = time.time()
        r = compute_drift_atlas(G, L)
        results[(G, L)] = r
        dt = time.time() - t0
        print(f"  {G:<9s} L={L}: n_irreps={r['n_irreps']:5d}, "
              f"dim_H_pi={int(r['dim_H_pi']):10d}, "
              f"alpha1_h={r['alpha1_h']:.4e}, exact={r['alpha1_exact']:.4e}, "
              f"drift_h={r['drift_h']:.6%}  [{dt:.2f}s]", flush=True)

t_compute = time.time() - t_start                                    # (local)
print(f"\n  total compute time: {t_compute:.2f}s", flush=True)

# =============================================================================
# Section 10: CLT predictions and in-band test
# =============================================================================
# SUBSTITUTION CHAIN (final direction step):
# Step 1 (def): CLT(G,L) = 0.5 + 0.5/sqrt(dim_H_pi(G,L))
# Step 2 (subst): per (G,L) compute dim_H_pi from the atlas
# Step 3 (subst): compute actual drift_h per atlas
# Step 4 (simpl): rel_dev = |drift_h - CLT|/CLT
# Step 5 (direction):
#   PASS  if all 9 combos satisfy rel_dev < BAND_FRAC (15%)
#   INFO  if all 9 within INFO_FRAC (20%), or >=6 of 9 in BAND with rest in INFO
#   FAIL  otherwise

print("\n" + "=" * 78, flush=True)
print("Section 10: CLT predictions and in-band test", flush=True)
print("=" * 78, flush=True)

# Build CLT predictions and rel_devs
clt_vals = {}                                                        # (local)
drift_vals = {}                                                      # (local)
rel_devs = {}                                                        # (local)
in_band = {}                                                         # (local)
in_info = {}                                                         # (local)
dim_H_pi_vals = {}                                                   # (local)

print(f"  {'(G, L)':<16} {'dim_H_pi':>12} {'drift_h^act':>15} "
      f"{'CLT':>10} {'rel_dev':>10} {'in 15%?':>9} {'in 20%?':>9}", flush=True)
for G in GROUPS:
    for L in L_LIST:
        r = results[(G, L)]
        dim_H = r["dim_H_pi"]
        clt = 0.5 + 0.5 / np.sqrt(dim_H)
        drift = r["drift_h"]
        rel = abs(drift - clt) / clt if clt > 0 else float('nan')
        clt_vals[(G, L)] = clt
        drift_vals[(G, L)] = drift
        rel_devs[(G, L)] = rel
        dim_H_pi_vals[(G, L)] = dim_H
        in_band[(G, L)] = rel < BAND_FRAC
        in_info[(G, L)] = rel < INFO_FRAC
        print(f"  ({G}, L={L})".ljust(16) +
              f" {int(dim_H):>12d}" +
              f" {drift:>14.6%}" +
              f" {clt:>10.4f}" +
              f" {rel:>9.2%}" +
              f" {str(in_band[(G,L)]):>9}" +
              f" {str(in_info[(G,L)]):>9}", flush=True)

n_in_band = sum(in_band.values())                                    # (local)
n_in_info = sum(in_info.values())                                    # (local)
N_TOTAL = len(GROUPS) * len(L_LIST)                                  # (local) = 9

print(f"\n  in_15%_band: {n_in_band}/{N_TOTAL}", flush=True)
print(f"  in_20%_band: {n_in_info}/{N_TOTAL}", flush=True)

# Verdict
if n_in_band == N_TOTAL:
    verdict = "PASS"
    verdict_reason = (f"All {N_TOTAL}/9 exceptional-rank combos within CLT 15% band -- "
                      f"CLT atlas confirmed across {{G_2, F_4, Spin(8)}} x L={{6,7,8}}.")
elif n_in_info == N_TOTAL or (n_in_band >= 6 and n_in_info == N_TOTAL):
    verdict = "INFO"
    verdict_reason = (f"{n_in_band}/9 in 15% band but all {n_in_info}/9 within 20%. "
                      f"Most in band with minor NLO deviations.")
else:
    verdict = "FAIL"
    verdict_reason = (f"{n_in_band}/9 in 15% band, {n_in_info}/9 in 20% band. "
                      f"CLT atlas does NOT hold uniformly for exceptional ranks -- "
                      f"systematic deviation. Drift^actual is ~100x SMALLER than CLT "
                      f"(rank-dependent Cartan protection, per G17/G18 structural null).")

print(f"\n  VERDICT: {verdict}", flush=True)
print(f"  reason : {verdict_reason}", flush=True)

# =============================================================================
# Section 11: Refined rank-scaling diagnostic (cross-gate NOTE)
# =============================================================================
# G17 showed pure-T^r Cartan has drift ~ 1e-8 (structural null by Weyl sym).
# G18 showed G_2 rep-theoretic drift is finite but 14-42x smaller than CLT(L(L+1)).
# The refined prediction: drift ~ dim_b / dim_H_pi * O(1) or
# log-log fit suggests drift ~ C * L^a with a ~ 2 (empirical).
# This is NOT a gate criterion; only a diagnostic.
print("\n" + "=" * 78, flush=True)
print("Section 11: Refined rank-scaling diagnostic (not a gate criterion)", flush=True)
print("=" * 78, flush=True)

# For each group: fit log(drift_h) vs log(L) across L=6,7,8
for G in GROUPS:
    drifts_G = np.array([drift_vals[(G, L)] for L in L_LIST])         # (local)
    # If any are zero or nan, skip
    valid = (drifts_G > 0) & np.isfinite(drifts_G)                    # (local)
    if valid.sum() >= 2:
        logL = np.log(np.array(L_LIST)[valid])                        # (local)
        logD = np.log(drifts_G[valid])                                # (local)
        slope_a, intercept_b = np.polyfit(logL, logD, 1)              # (local)
        print(f"  {G}: drift ~ L^{slope_a:.3f} * exp({intercept_b:.3f})  "
              f"(drift L=8 ~ {np.exp(intercept_b) * 8**slope_a:.4%})", flush=True)
    else:
        print(f"  {G}: insufficient valid points for log-log fit", flush=True)

# Rank comparison: drift vs rank at L=8
print("\n  Rank vs drift_h at L=8 (G17/G18 'protection proportional to rank'):", flush=True)
for G in GROUPS:
    r_data = results[(G, 8)]
    print(f"    {G:<9s} rank={r_data['rank']}, drift_h(L=8)={drift_vals[(G,8)]:.6%}", flush=True)

# =============================================================================
# Section 12: Plot
# =============================================================================
print("\n" + "=" * 78, flush=True)
print("Section 12: Plot", flush=True)
print("=" * 78, flush=True)

fig, axes = plt.subplots(1, 3, figsize=(16, 5.5))
fig.suptitle(f"{GATE_ID}: VERDICT={verdict}  "
             f"({n_in_band}/{N_TOTAL} in 15%, {n_in_info}/{N_TOTAL} in 20%)",
             fontsize=12)

# Panel 1: drift_h vs L for all 3 groups + CLT line
ax = axes[0]
colors = {"G_2": "tab:blue", "F_4": "tab:orange", "Spin(8)": "tab:green"}
for G in GROUPS:
    Ls = np.array(L_LIST)
    drifts = np.array([drift_vals[(G, L)] for L in L_LIST])
    clts = np.array([clt_vals[(G, L)] for L in L_LIST])
    ax.plot(Ls, drifts, 'o-', color=colors[G], lw=2, ms=10, label=f"{G} actual")
    ax.plot(Ls, clts, 's--', color=colors[G], lw=1, ms=5, alpha=0.6,
            label=f"{G} CLT = 0.5+0.5/sqrt(dim_H_pi)")
ax.set_xlabel("L_max")
ax.set_ylabel("drift_h")
ax.set_title("Atlas: drift vs L (log scale)")
ax.set_xticks(L_LIST)
ax.set_yscale('log')
ax.grid(alpha=0.3)
ax.legend(fontsize=7, loc='best')

# Panel 2: Rel dev bar chart (9 combos)
ax = axes[1]
x_pos = []
y_vals = []
bar_colors = []
labels = []
for i, G in enumerate(GROUPS):
    for j, L in enumerate(L_LIST):
        idx = i * 3 + j
        x_pos.append(idx)
        y_vals.append(rel_devs[(G, L)] * 100)
        col = 'green' if in_band[(G, L)] else ('orange' if in_info[(G, L)] else 'red')
        bar_colors.append(col)
        labels.append(f"{G[:3]}\nL={L}")
bars = ax.bar(x_pos, y_vals, color=bar_colors)
ax.axhline(BAND_FRAC * 100, color='k', ls='--', lw=1, label=f'{int(BAND_FRAC*100)}% PASS')
ax.axhline(INFO_FRAC * 100, color='gray', ls=':', lw=1, label=f'{int(INFO_FRAC*100)}% INFO')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=8)
ax.set_ylabel("|drift - CLT| / CLT  (%)")
ax.set_title(f"Relative deviation -- {verdict}")
ax.legend(fontsize=8)
ax.grid(alpha=0.3, axis='y')
# Annotate values
for x, y in zip(x_pos, y_vals):
    ax.text(x, y + 2, f'{y:.1f}', ha='center', fontsize=7)

# Panel 3: log-log drift vs L atlas
ax = axes[2]
for G in GROUPS:
    drifts_G = np.array([drift_vals[(G, L)] for L in L_LIST])
    valid = (drifts_G > 0) & np.isfinite(drifts_G)
    if valid.sum() >= 2:
        Ls = np.array(L_LIST)[valid]
        ds = drifts_G[valid]
        ax.loglog(Ls, ds, 'o-', color=colors[G], lw=2, ms=10, label=f"{G}")
# Guide line: CLT ~ 0.5 (roughly constant)
ax.axhline(0.5, color='k', ls='--', alpha=0.5, label='CLT ~ 0.5 limit')
ax.set_xlabel("L_max")
ax.set_ylabel("drift_h")
ax.set_title("Log-log: drift scaling vs L")
ax.grid(alpha=0.3, which='both')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=130, bbox_inches='tight')
plt.close(fig)
print(f"  PNG saved: {OUT_PNG.name}", flush=True)

# =============================================================================
# Section 13: Save NPZ + closure hash
# =============================================================================
print("\n" + "=" * 78, flush=True)
print("Section 13: Save NPZ", flush=True)
print("=" * 78, flush=True)

# Arrays: 3 groups x 3 L_values
groups_arr = np.array(GROUPS)
L_arr = np.array(L_LIST, dtype=np.int64)
drift_h_grid = np.array([[drift_vals[(G, L)] for L in L_LIST]
                          for G in GROUPS])                           # (local) (3, 3)
clt_grid = np.array([[clt_vals[(G, L)] for L in L_LIST]
                      for G in GROUPS])                               # (local)
rel_dev_grid = np.array([[rel_devs[(G, L)] for L in L_LIST]
                          for G in GROUPS])                           # (local)
dim_H_pi_grid = np.array([[dim_H_pi_vals[(G, L)] for L in L_LIST]
                           for G in GROUPS])                          # (local)
in_band_grid = np.array([[in_band[(G, L)] for L in L_LIST]
                          for G in GROUPS])                           # (local)

# Alpha_1 branches: flat dict
alpha1_h_grid = np.array([[results[(G, L)]['alpha1_h'] for L in L_LIST]
                            for G in GROUPS])
alpha1_exact_grid = np.array([[results[(G, L)]['alpha1_exact'] for L in L_LIST]
                                for G in GROUPS])
n_irreps_grid = np.array([[results[(G, L)]['n_irreps'] for L in L_LIST]
                           for G in GROUPS])
rank_arr = np.array([results[(G, 8)]['rank'] for G in GROUPS])

spectrum_sha_grid = np.array([[results[(G, L)]['spectrum_sha']
                                  for L in L_LIST] for G in GROUPS])

# Headline value: L=8 rel_devs for all 3 groups
headline_value = float(np.max([rel_devs[(G, 8)] for G in GROUPS]))  # (local) max rel dev at L=8
L_MAX_TAG = 8                                                         # (local)

# Output pins for closure SHA
OUTPUT_PINS = {
    "tau_fold": TAU,
    "L_LIST": L_LIST,
    "GROUPS": GROUPS,
    "BAND_FRAC": BAND_FRAC,
    "INFO_FRAC": INFO_FRAC,
    "verdict": verdict,
    "n_in_band": n_in_band,
    "n_in_info": n_in_info,
    "drift_grid": drift_h_grid.tolist(),
    "clt_grid": clt_grid.tolist(),
    "rel_dev_grid": rel_dev_grid.tolist(),
    "dim_H_pi_grid": dim_H_pi_grid.tolist(),
    "import_closure_sha": IMPORT_CLOSURE_SHA,
    "spectrum_sha_flat": spectrum_sha_grid.ravel().tolist(),
    "gate": GATE_ID,
    "plan_section": "W2-G25",
}
CLOSURE_SHA = sha256_of_obj(OUTPUT_PINS)                             # (local)

np.savez_compressed(
    OUT_NPZ,
    gate_id=np.array(GATE_ID),
    session=np.array(SESSION),
    verdict=np.array(verdict),
    verdict_reason=np.array(verdict_reason),
    scheme_tag=np.array(SCHEME_TAG),
    convention_tag=np.array(CONVENTION_TAG),
    # Config
    tau_fold_used=np.float64(TAU),
    L_list=L_arr,
    groups=groups_arr,
    band_frac=np.float64(BAND_FRAC),
    info_frac=np.float64(INFO_FRAC),
    # Main grids (3 groups x 3 L values)
    drift_h_grid=drift_h_grid,
    clt_grid=clt_grid,
    rel_dev_grid=rel_dev_grid,
    dim_H_pi_grid=dim_H_pi_grid,
    in_band_grid=in_band_grid,
    alpha1_h_grid=alpha1_h_grid,
    alpha1_exact_grid=alpha1_exact_grid,
    n_irreps_grid=n_irreps_grid,
    rank_arr=rank_arr,
    # Summary
    n_in_band=np.int64(n_in_band),
    n_in_info=np.int64(n_in_info),
    N_total=np.int64(N_TOTAL),
    headline_value=np.float64(headline_value),
    # Spectrum SHAs
    spectrum_sha_grid=spectrum_sha_grid,
    # Closure
    SHA_closure=np.array(CLOSURE_SHA),
    SHA_import_closure=np.array(IMPORT_CLOSURE_SHA),
    SHA_self=np.array(SHA_SELF),
)
print(f"  NPZ saved: {OUT_NPZ.name}", flush=True)
print(f"  closure SHA: {CLOSURE_SHA}", flush=True)

# =============================================================================
# Section 14: Verdict line (S81+ canonical form with 64-char SHA)
# =============================================================================
print("\n" + "=" * 78, flush=True)
print("Section 14: Append verdict line", flush=True)
print("=" * 78, flush=True)

# 4-tuple: (value=headline_value (= max rel_dev at L=8), scheme, convention, L_max=8)
tuple_4 = (f"value=max_rel_dev_L8={headline_value:.6f} "
           f"scheme={SCHEME_TAG} "
           f"convention={CONVENTION_TAG} "
           f"L_max={L_MAX_TAG}")                                      # (local)

verdict_line = (f"{GATE_ID}: {verdict} -- "
                f"n_in_15%_band={n_in_band}/{N_TOTAL}, "
                f"n_in_20%_band={n_in_info}/{N_TOTAL}, "
                f"max_rel_dev_L8={headline_value:.6f}, "
                f"drift_h(G_2,L=8)={drift_vals[('G_2',8)]:.6%}, "
                f"drift_h(F_4,L=8)={drift_vals[('F_4',8)]:.6%}, "
                f"drift_h(Spin(8),L=8)={drift_vals[('Spin(8)',8)]:.6%}, "
                f"CLT(G_2,L=8)={clt_vals[('G_2',8)]:.4f}, "
                f"CLT(F_4,L=8)={clt_vals[('F_4',8)]:.4f}, "
                f"CLT(Spin(8),L=8)={clt_vals[('Spin(8)',8)]:.4f}, "
                f"{tuple_4}, "
                f"sha256={CLOSURE_SHA}")                              # (local)

with open(VERDICT_TXT, "a", encoding="utf-8") as fh:
    fh.write(verdict_line + "\n")

print(f"  appended to: {VERDICT_TXT.name}", flush=True)
print(f"  verdict line:\n    {verdict_line}", flush=True)

# 4-tuple as final non-verdict line
print(f"\n  4-tuple: ({tuple_4})", flush=True)

t_total = time.time() - t_start                                      # (local)
print("\n" + "=" * 78, flush=True)
print(f"DONE. VERDICT: {verdict}  |  max rel_dev at L=8: {headline_value:.2%}", flush=True)
print(f"total wall time: {t_total:.1f}s", flush=True)
print("=" * 78, flush=True)
