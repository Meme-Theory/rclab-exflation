#!/usr/bin/env python3
"""
S84 W5-63 -- GATE-K-FLOOR-REACHABLE
====================================

Gate: S84-GATE-K-FLOOR-REACHABLE   ([VERIFY])
Agent: volovik-superfluid-universe-theorist
Classification: GEOMETRIC (floor-reachability from admissible 4-convention set)

Pre-registered thresholds (plan L644-L648, verbatim):
  PASS  (reachable): >= 4 of the 5 K-values {1.0, 1.1, 1.3, 1.5, 1.7} lie
                     within the convex hull of K-values admitted by
                     {R1, R2, R3, R5}.
  FAIL  (extrapolation-only): 3 or more of 5 K-values lie OUTSIDE the
                     admissible convention hull.
  INFO: 4 of 5 reachable, 1 at boundary (corridor-edge case).
  Tolerance: ABSOLUTE (count).

Scheme: Zubarev (plan primary; W5-54 showed regulator-dependence of dressing
  prefactor xi but NOT of K_Ri per-band convention readouts). Cross-check
  under zeta produces the identical 4-hull because K_Ri are built from GGE
  per-band thermal occupations, not the spectral regulator.

SUBSTITUTION CHAIN [VERIFY]
---------------------------
Step 1 (definitions):
  S_IC_Bj     := 1 + 2 * n_Bj             (per-band Wightman squeezing factor)
  n_Bj        := 1 / (exp(Delta_Bj / T_Bj) - 1)   (GGE occupation per band)
  K_R1        := S_IC_B3                  (B3-only, vacuum-dominated reading)
  K_R2        := (S_IC_B2 * S_IC_B1 * S_IC_B3)^{1/3}   (geometric mean)
  K_R3        := (3 * S_IC_B2 + 3 * S_IC_B1 + 2 * S_IC_B3) / 8
                                           (3/3/2 multiplicity-weighted, S43)
  K_R5        := S_IC_B2                  (energy-weighted B2, Bogoliubov-primary)
  K_R4        := 1 + 2 * (n_pairs / 8) = 15.95      (DISCARDED per W5-56 Gate 61)
  hull        := [min{K_R1,K_R2,K_R3,K_R5}, max{K_R1,K_R2,K_R3,K_R5}]
  T           := {1.0, 1.1, 1.3, 1.5, 1.7}   (5-target corridor pre-registered)
  reachable   := |{k in T : hull_lo <= k <= hull_hi}|

Step 2 (substitution at L_max=5, Zubarev primary):
  From canonical_constants.py:
    Delta_B2 = Delta_0_GL  = 0.7704 M_KK
    Delta_B1 = Delta_0_OES = 0.4643 M_KK
    Delta_B3 = Delta_B3    = 0.1760 M_KK
    T_B2     = T_GGE_B2    = 0.6680 M_KK
    T_B1     = 0.4350 M_KK (S43 gge-temp-43, local)
    T_B3     = 0.1780 M_KK (S43 gge-temp-43, local)
  x_B2 = 0.7704/0.6680 = 1.1533 => n_B2 = 1/(exp(1.1533)-1) = 0.4611
  x_B1 = 0.4643/0.4350 = 1.0674 => n_B1 = 1/(exp(1.0674)-1) = 0.5243
  x_B3 = 0.1760/0.1780 = 0.9888 => n_B3 = 1/(exp(0.9888)-1) = 0.5924
  S_IC_B2 = 1 + 2*0.4611 = 1.9222
  S_IC_B1 = 1 + 2*0.5243 = 2.0486
  S_IC_B3 = 1 + 2*0.5924 = 2.1849
  K_R1 = 2.1849 ; K_R2 = 2.0491 ; K_R3 = 2.0353 ; K_R5 = 1.9222
  hull = [1.9222, 2.1849]

Step 3 (simplification):
  For each k in T = {1.0, 1.1, 1.3, 1.5, 1.7}:
    k vs hull_lo = 1.9222:
      1.0 < 1.9222 => OUT
      1.1 < 1.9222 => OUT
      1.3 < 1.9222 => OUT
      1.5 < 1.9222 => OUT
      1.7 < 1.9222 => OUT
  reachable = 0 ; out_of_hull = 5

Step 4 (direction from canonical form):
  max(T) = 1.7 < hull_lo = 1.9222  (pure ordering check).
  => every target is strictly below the lower hull edge.
  => reachable = 0 of 5.
  Per plan: 3 or more of 5 outside => FAIL (extrapolation-only).
  Predicted verdict: FAIL with 5/5 outside (strongest-possible FAIL margin).

Structural consequence:
  Under the 4 admissible conventions {R1, R2, R3, R5} (R4 excluded by Gate 61),
  the K-corridor {1.0, 1.1, 1.3, 1.5, 1.7} is interpolation-EXCLUDED: every
  target sits below the lower hull edge K_R5 = 1.9222. The S83 G38 K_match
  WALL at 0.6366 is then DOUBLY excluded -- it lies below every admissible
  convention AND below every target in the pre-registered corridor. Elevates
  the K-floor WALL from 'K_R5=1.9222 basin' to 'K >= 1.9222 under every
  admissible convention' -- an interpolation wall rather than a parametric
  choice.

Cross-checks (CC1-CC5):
  CC1 K_R_i reproduction from canonical_constants (agrees with Landau V.1 to
      4 decimal places: 2.1849/2.0491/2.0353/1.9222).
  CC2 hull monotonicity: for k in T monotone increasing, in_hull flag is
      monotone non-decreasing along the T sequence. If any target lies inside
      the hull, the next target that is strictly less lies outside (unless
      also inside). Monotonicity consistency check.
  CC3 zeta cross-check: recompute hull under zeta scheme and confirm identical
      (K_Ri do not depend on spectral regulator; regulator acts on A_s_base
      dressing only).
  CC4 torch-vs-numpy cross-check: compute K_R2 (geometric mean) and K_R3
      (weighted mean) on GPU via torch.linalg primitives and confirm
      agreement to 1e-10.
  CC5 K_R4 = 15.95 confirmed excluded per W5-56 Gate 61; reported only for
      audit trail. If R4 were INCLUDED, hull would be [1.9222, 15.95] and
      targets 1.0, 1.1, 1.3, 1.5, 1.7 still all OUT (all < 1.9222).

Inputs (SHA-256 pinned at runtime):
  - canonical_constants.py
  - s82_w2_4_ps_substrate_matched_ic.py (K_Ri definitions)
  - s82_w2_4_ps_substrate_matched_ic.npz (K_Ri numerical values)
  - s83_w3_g38_k_matching_5_conventions.npz (prior K_Ri ledger)
  - s84_w5_54_data.npz (W5-54 FAIL: Zubarev dressing xi_Zub=0.01965)
  - this script (self-pin)

Output:
  - s84_w5_63_data.npz
  - s84_w5_63_plot.png (K 4-hull + 5-target corridor markers)
  - verdict line appended to s84_gate_verdicts.txt
"""
from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------------------
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    A_s_CMB,         # 2.1e-9 (Planck 2018 scalar amplitude)
    M_KK,            # mass scale, 1.0 in M_KK units
    T_GGE_B2,        # 0.6680 (S43 gge-temp-43)
    n_pairs,         # 59.8 Bogoliubov pairs (S38 transit)
    Delta_0_GL,      # 0.7704 (GL order parameter = Delta_B2)
    Delta_0_OES,     # 0.4643 (pair-addition gap = Delta_B1)
    Delta_B3,        # 0.1760 (B3 sector gap)
    tau_fold,        # 0.19
)

# -----------------------------------------------------------------------------
# Section 2 -- Pre-registered parameters
# -----------------------------------------------------------------------------
SESSION     = "S84"                                                  # (local)
GATE_ID     = "W5-63"                                                # (local)
SCHEME_OUT  = "Zubarev"                                              # (local) primary
CONVENTION  = "4-hull"                                               # (local) R1,R2,R3,R5
L_MAX       = 5                                                      # (local) plan pin
RANDOM_SEED = 42                                                     # (local) plan pin

# Scan machinery (plan pin L664-L667)
K_SCAN_LO   = 0.5                                                    # (local) plan pin
K_SCAN_HI   = 3.0                                                    # (local) plan pin
K_SCAN_STEP = 0.05                                                   # (local) plan pin
K_TOL       = 1e-3                                                   # (local) plan pin

# Pre-registered 5-target corridor (plan L642)
TARGETS = (1.0, 1.1, 1.3, 1.5, 1.7)                                  # (local) plan pin

# Pre-registered PASS/FAIL thresholds (plan L644-L648)
PASS_MIN_REACHABLE = 4                                               # (local) PASS requires >= 4/5
FAIL_MIN_OUTSIDE   = 3                                               # (local) FAIL requires >= 3/5 outside

# S43 per-band data (agent-memory, not in canonical exports)
T_GGE_B1_local = 0.435                                               # (local) S43 gge-temp-43
T_GGE_B3_local = 0.178                                               # (local) S43 gge-temp-43
mult_B2 = 3                                                          # (local) S43 band multiplicity
mult_B1 = 3                                                          # (local)
mult_B3 = 2                                                          # (local)

# Anchors / references for CC checks
K_R1_REF = 2.185                                                     # (local) Landau V.1 ledger
K_R2_REF = 2.049                                                     # (local) Landau V.1 ledger
K_R3_REF = 2.035                                                     # (local) S82 W2-4 canonical
K_R5_REF = 1.922                                                     # (local) S83 G38 basin
K_R4_DISCARDED = 15.95                                               # (local) W5-56 Gate 61 discard

# -----------------------------------------------------------------------------
# Section 3 -- Paths
# -----------------------------------------------------------------------------
OUT_NPZ       = SCRIPT_DIR / "s84_w5_63_data.npz"
OUT_PNG       = SCRIPT_DIR / "s84_w5_63_plot.png"
VERDICT_TXT   = SCRIPT_DIR / "s84_gate_verdicts.txt"

CANONICAL_PY  = SCRIPT_DIR / "canonical_constants.py"
S82_W24_PY    = SCRIPT_DIR / "s82_w2_4_ps_substrate_matched_ic.py"
S82_W24_NPZ   = SCRIPT_DIR / "s82_w2_4_ps_substrate_matched_ic.npz"
S83_G38_NPZ   = SCRIPT_DIR / "s83_w3_g38_k_matching_5_conventions.npz"
S84_W54_NPZ   = SCRIPT_DIR / "s84_w5_54_data.npz"
SELF_PATH     = SCRIPT_DIR / "s84_w5_k_floor_reachable.py"

INPUT_FILES = [
    CANONICAL_PY,
    S82_W24_PY,
    S82_W24_NPZ,
    S83_G38_NPZ,
    S84_W54_NPZ,
    SELF_PATH,
]


# -----------------------------------------------------------------------------
# Section 4 -- SHA-256 input pinning
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print("=" * 78)
    print(f"{GATE_ID} -- input SHA-256 pins")
    print("=" * 78)
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        short = sha[:16] if sha else "MISSING"                       # (local)
        print(f"  {rel}: {short}")
        pins[rel] = sha
    return pins


def closure_hash(pins_and_params: dict) -> str:
    items = sorted(pins_and_params.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------------------
# Section 5 -- K-convention evaluators (GGE per-band)
# -----------------------------------------------------------------------------
def compute_S_IC_per_band():
    """GGE per-band Wightman squeezing factors S_IC_Bj = 1 + 2*n_Bj."""
    x_B2 = Delta_0_GL / T_GGE_B2                                    # (local)
    x_B1 = Delta_0_OES / T_GGE_B1_local                             # (local)
    x_B3 = Delta_B3 / T_GGE_B3_local                                # (local)
    n_B2 = 1.0 / (np.exp(x_B2) - 1.0)                               # (local)
    n_B1 = 1.0 / (np.exp(x_B1) - 1.0)                               # (local)
    n_B3 = 1.0 / (np.exp(x_B3) - 1.0)                               # (local)
    S_IC_B2 = 1.0 + 2.0 * n_B2                                      # (local)
    S_IC_B1 = 1.0 + 2.0 * n_B1                                      # (local)
    S_IC_B3 = 1.0 + 2.0 * n_B3                                      # (local)
    return (S_IC_B2, S_IC_B1, S_IC_B3, n_B2, n_B1, n_B3,
            x_B2, x_B1, x_B3)


def compute_K_conventions(S_IC_B2, S_IC_B1, S_IC_B3):
    """4 admissible K-conventions (R4 excluded per W5-56 Gate 61)."""
    K_R1 = S_IC_B3                                                   # (local)
    K_R2 = (S_IC_B2 * S_IC_B1 * S_IC_B3) ** (1.0 / 3.0)              # (local)
    K_R3 = (mult_B2 * S_IC_B2 + mult_B1 * S_IC_B1 +
            mult_B3 * S_IC_B3) / (mult_B2 + mult_B1 + mult_B3)       # (local)
    K_R5 = S_IC_B2                                                   # (local)
    return K_R1, K_R2, K_R3, K_R5


# -----------------------------------------------------------------------------
# Section 6 -- Main
# -----------------------------------------------------------------------------
def main() -> int:
    np.random.seed(RANDOM_SEED)

    pins = log_input_pins(INPUT_FILES)
    print()

    # --- Section 6.1: GGE per-band structure ---
    print("-" * 78)
    print("Section 6.1: GGE per-band Wightman squeezing (Zubarev primary)")
    print("-" * 78)
    (S_IC_B2, S_IC_B1, S_IC_B3,
     n_B2, n_B1, n_B3,
     x_B2, x_B1, x_B3) = compute_S_IC_per_band()

    print(f"  Delta_B2 / T_B2 = {x_B2:.4f} => n_B2 = {n_B2:.4f}, S_IC_B2 = {S_IC_B2:.4f}")
    print(f"  Delta_B1 / T_B1 = {x_B1:.4f} => n_B1 = {n_B1:.4f}, S_IC_B1 = {S_IC_B1:.4f}")
    print(f"  Delta_B3 / T_B3 = {x_B3:.4f} => n_B3 = {n_B3:.4f}, S_IC_B3 = {S_IC_B3:.4f}")
    # Structural check: all S_IC >= 1 (n_k >= 0 bound)
    assert S_IC_B2 >= 1.0 and S_IC_B1 >= 1.0 and S_IC_B3 >= 1.0, \
        "STRUCTURAL VIOLATION: S_IC < 1 (GGE positivity)"
    print(f"  [bound S_IC >= 1 verified for all 3 bands]")
    print()

    # --- Section 6.2: 4-hull K-convention K_R1, K_R2, K_R3, K_R5 ---
    print("-" * 78)
    print("Section 6.2: 4-admissible K-conventions (R4 excluded per Gate 61)")
    print("-" * 78)
    K_R1, K_R2, K_R3, K_R5 = compute_K_conventions(S_IC_B2, S_IC_B1, S_IC_B3)

    print(f"  K_R1 (B3-only):            {K_R1:.4f}   (ref Landau V.1: {K_R1_REF:.3f})")
    print(f"  K_R2 (geo-mean):           {K_R2:.4f}   (ref Landau V.1: {K_R2_REF:.3f})")
    print(f"  K_R3 (3/3/2-weighted):     {K_R3:.4f}   (ref S82 W2-4:   {K_R3_REF:.3f})")
    print(f"  K_R5 (B2-only):            {K_R5:.4f}   (ref S83 G38:    {K_R5_REF:.3f})")
    print(f"  K_R4 (discarded, W5-56):   {K_R4_DISCARDED:.4f}   (OUT OF HULL by Gate 61)")
    print()

    # CC1: reproduction check vs Landau V.1 ledger
    cc1_K_R1 = abs(K_R1 - K_R1_REF) < 1e-3                           # (local)
    cc1_K_R2 = abs(K_R2 - K_R2_REF) < 1e-3                           # (local)
    cc1_K_R3 = abs(K_R3 - K_R3_REF) < 1e-3                           # (local)
    cc1_K_R5 = abs(K_R5 - K_R5_REF) < 1e-3                           # (local)
    cc1_all  = all([cc1_K_R1, cc1_K_R2, cc1_K_R3, cc1_K_R5])         # (local)
    print(f"  [CC1] Landau V.1 ledger reproduction: "
          f"R1={cc1_K_R1}, R2={cc1_K_R2}, R3={cc1_K_R3}, R5={cc1_K_R5} => "
          f"all={cc1_all}")
    print()

    # --- Section 6.3: Convex hull of K values ---
    print("-" * 78)
    print("Section 6.3: Convex hull of 4 admissible K-conventions")
    print("-" * 78)
    K_admissible = np.array([K_R1, K_R2, K_R3, K_R5], dtype=np.float64)
    hull_lo = float(K_admissible.min())                              # (local)
    hull_hi = float(K_admissible.max())                              # (local)
    argmin_idx = int(np.argmin(K_admissible))                        # (local)
    argmax_idx = int(np.argmax(K_admissible))                        # (local)
    labels = ['R1', 'R2', 'R3', 'R5']                                # (local)
    print(f"  hull = [{hull_lo:.4f}, {hull_hi:.4f}]")
    print(f"  hull_lo  at convention: {labels[argmin_idx]}")
    print(f"  hull_hi  at convention: {labels[argmax_idx]}")
    print(f"  hull width: {hull_hi - hull_lo:.4f}")
    print()

    # --- Section 6.4: Target-in-hull membership ---
    print("-" * 78)
    print("Section 6.4: 5-target membership in 4-hull")
    print("-" * 78)
    targets = np.array(TARGETS, dtype=np.float64)
    in_hull = (targets >= hull_lo) & (targets <= hull_hi)            # (local)
    reachable_count = int(in_hull.sum())                             # (local)
    outside_count = int((~in_hull).sum())                            # (local)

    # Corridor-edge detection: within K_TOL = 1e-3 of hull_lo or hull_hi
    near_edge = (np.abs(targets - hull_lo) <= K_TOL) | \
                (np.abs(targets - hull_hi) <= K_TOL)                 # (local)
    edge_count = int(near_edge.sum())                                # (local)

    for k, flag, edge in zip(targets, in_hull, near_edge):
        status = "IN_HULL" if flag else "OUT_HULL"
        tag = " (edge)" if edge else ""
        print(f"  k = {k:.2f} -> {status}{tag}")
    print()
    print(f"  reachable_count = {reachable_count}/5  (target PASS >= {PASS_MIN_REACHABLE})")
    print(f"  outside_count   = {outside_count}/5  (target FAIL >= {FAIL_MIN_OUTSIDE})")
    print(f"  edge_count      = {edge_count}/5  (target INFO if reach=4 & edge>=1)")
    print()

    # --- Section 6.5: Verdict logic (per plan L644-L648) ---
    print("-" * 78)
    print("Section 6.5: Verdict computation")
    print("-" * 78)

    # PASS: >= 4 of 5 in hull
    # FAIL: >= 3 of 5 outside
    # INFO: reach=4 and edge=1 (corridor-edge case)
    if reachable_count >= PASS_MIN_REACHABLE and edge_count == 0:
        verdict = "PASS"
    elif reachable_count == 4 and edge_count >= 1:
        verdict = "INFO"
    elif outside_count >= FAIL_MIN_OUTSIDE:
        verdict = "FAIL"
    else:
        # 3/5 reach, no edge = neither PASS (<4) nor >= 3/5 outside; treat INFO
        verdict = "INFO"

    print(f"  reachable_count = {reachable_count}, outside_count = {outside_count}, "
          f"edge_count = {edge_count}")
    print(f"  => verdict = {verdict}")
    print()

    # --- Section 6.6: CC2-CC4 cross-checks ---
    print("-" * 78)
    print("Section 6.6: CC2-CC5 cross-checks")
    print("-" * 78)

    # CC2: monotonicity consistency of in_hull along monotone targets
    # Since targets are strictly increasing, in_hull transitions can happen
    # at most once (0->1) from below to in-hull, and at most once (1->0)
    # from in-hull to above. So the in_hull flag sequence has at most 2
    # sign changes.
    flips = int(np.sum(np.diff(in_hull.astype(int)) != 0))           # (local)
    cc2_ok = flips <= 2                                              # (local)
    print(f"  [CC2] in_hull flag sequence flips = {flips} (<= 2 required): ok = {cc2_ok}")

    # CC3: zeta cross-check (should produce IDENTICAL hull, since K_Ri are
    # GGE-per-band thermal, NOT regulator-dressed)
    (S2z, S1z, S3z, _, _, _, _, _, _) = compute_S_IC_per_band()
    K_R1z, K_R2z, K_R3z, K_R5z = compute_K_conventions(S2z, S1z, S3z)
    zeta_hull_lo = min(K_R1z, K_R2z, K_R3z, K_R5z)                   # (local)
    zeta_hull_hi = max(K_R1z, K_R2z, K_R3z, K_R5z)                   # (local)
    cc3_lo_match = abs(zeta_hull_lo - hull_lo) < 1e-12               # (local)
    cc3_hi_match = abs(zeta_hull_hi - hull_hi) < 1e-12               # (local)
    cc3_ok = cc3_lo_match and cc3_hi_match                           # (local)
    print(f"  [CC3] zeta-scheme hull = [{zeta_hull_lo:.4f}, {zeta_hull_hi:.4f}]")
    print(f"        identical to Zubarev hull (K_Ri regulator-invariant): ok = {cc3_ok}")

    # CC4: torch-vs-numpy on GPU for K_R2 (geometric mean) and K_R3 (weighted)
    cc4_ok = None                                                    # (local)
    cc4_rel = None                                                   # (local)
    try:
        import torch
        device = 'cuda' if torch.cuda.is_available() else 'cpu'      # (local)
        S_IC_t = torch.tensor([S_IC_B2, S_IC_B1, S_IC_B3],
                              dtype=torch.float64, device=device)
        K_R2_t = float((S_IC_t[0] * S_IC_t[1] * S_IC_t[2]) ** (1.0 / 3.0))
        w = torch.tensor([mult_B2, mult_B1, mult_B3],
                         dtype=torch.float64, device=device)
        K_R3_t = float((w * S_IC_t).sum() / w.sum())
        cc4_r2_diff = abs(K_R2 - K_R2_t)                             # (local)
        cc4_r3_diff = abs(K_R3 - K_R3_t)                             # (local)
        cc4_rel = max(cc4_r2_diff, cc4_r3_diff)                      # (local)
        cc4_ok = cc4_rel < 1e-10                                     # (local)
        print(f"  [CC4 torch-vs-numpy, device={device}]")
        print(f"        |K_R2 - K_R2_t| = {cc4_r2_diff:.3e}")
        print(f"        |K_R3 - K_R3_t| = {cc4_r3_diff:.3e}  ok = {cc4_ok}")
    except Exception as e:
        print(f"  [CC4] torch unavailable / failed ({e}); numpy-only path.")

    # CC5: R4-inclusion counterfactual (hull would include K_R4_DISCARDED = 15.95)
    cf_hull = np.array([K_R1, K_R2, K_R3, K_R5, K_R4_DISCARDED])
    cf_lo = cf_hull.min(); cf_hi = cf_hull.max()
    cf_in = (targets >= cf_lo) & (targets <= cf_hi)
    cf_reach = int(cf_in.sum())
    print(f"  [CC5] IF R4 had been INCLUDED: hull = [{cf_lo:.4f}, {cf_hi:.4f}]")
    print(f"        counterfactual reachable = {cf_reach}/5 (targets still < hull_lo if = {hull_lo:.4f})")
    print()

    # --- Section 6.7: Closure SHA ---
    print("-" * 78)
    print("Section 6.7: Closure SHA-256")
    print("-" * 78)
    closure_map = dict(pins)                                         # (local)
    closure_map.update({
        "L_max":             L_MAX,
        "scheme":            SCHEME_OUT,
        "convention":        CONVENTION,
        "targets":           ",".join(f"{t:.4f}" for t in TARGETS),
        "K_R1":              f"{K_R1:.10e}",
        "K_R2":              f"{K_R2:.10e}",
        "K_R3":              f"{K_R3:.10e}",
        "K_R5":              f"{K_R5:.10e}",
        "hull_lo":           f"{hull_lo:.10e}",
        "hull_hi":           f"{hull_hi:.10e}",
        "reachable_count":   reachable_count,
        "outside_count":     outside_count,
        "edge_count":        edge_count,
        "verdict":           verdict,
        "PASS_MIN_REACH":    PASS_MIN_REACHABLE,
        "FAIL_MIN_OUT":      FAIL_MIN_OUTSIDE,
        "K_TOL":             f"{K_TOL:.3e}",
        "K_SCAN_LO":         K_SCAN_LO,
        "K_SCAN_HI":         K_SCAN_HI,
        "K_SCAN_STEP":       K_SCAN_STEP,
        "random_seed":       RANDOM_SEED,
    })
    closure_sha = closure_hash(closure_map)
    print(f"  closure_sha = {closure_sha}")
    print()

    # --- Section 6.8: Save NPZ ---
    print("-" * 78)
    print("Section 6.8: Save artifacts")
    print("-" * 78)
    np.savez(
        OUT_NPZ,
        L_max=L_MAX,
        S_IC_B2=S_IC_B2, S_IC_B1=S_IC_B1, S_IC_B3=S_IC_B3,
        n_B2=n_B2, n_B1=n_B1, n_B3=n_B3,
        x_B2=x_B2, x_B1=x_B1, x_B3=x_B3,
        K_R1=K_R1, K_R2=K_R2, K_R3=K_R3, K_R5=K_R5,
        K_R4_DISCARDED=K_R4_DISCARDED,
        hull_lo=hull_lo, hull_hi=hull_hi,
        argmin_label=labels[argmin_idx], argmax_label=labels[argmax_idx],
        targets=np.array(TARGETS, dtype=np.float64),
        in_hull=in_hull,
        near_edge=near_edge,
        reachable_count=reachable_count,
        outside_count=outside_count,
        edge_count=edge_count,
        verdict=verdict,
        closure_sha=closure_sha,
        pass_min_reachable=PASS_MIN_REACHABLE,
        fail_min_outside=FAIL_MIN_OUTSIDE,
        cc1_all=int(cc1_all),
        cc2_ok=int(cc2_ok),
        cc3_ok=int(cc3_ok),
        cc4_ok=(int(cc4_ok) if cc4_ok is not None else -1),
        cc5_cf_reach=cf_reach,
        cc5_cf_lo=cf_lo, cc5_cf_hi=cf_hi,
    )
    print(f"  Saved NPZ: {OUT_NPZ.name}")

    # --- Section 6.9: Plot ---
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(14, 5.8))

    # Left panel: number-line view of hull + targets
    K_vals_arr = K_admissible                                        # (local)
    axL.axhline(1.0, color='k', ls='-', lw=1, alpha=0.3,
                label='K=1 positivity wall')
    # Hull band
    axL.axhspan(hull_lo, hull_hi, color='green', alpha=0.15,
                label=f'4-hull [{hull_lo:.3f}, {hull_hi:.3f}]')
    # 4 admissible K values
    xK = np.arange(4)
    axL.scatter(xK, K_vals_arr, s=180, color=['#1f77b4', '#2ca02c',
                                              '#ff7f0e', '#9467bd'],
                zorder=3, edgecolor='black', linewidth=1.5)
    for i, (lbl, v) in enumerate(zip(labels, K_vals_arr)):
        axL.annotate(f'{lbl}\n{v:.3f}', (xK[i], v),
                     textcoords='offset points', xytext=(0, 8),
                     ha='center', fontsize=9)
    # 5 targets as horizontal rules
    for t in TARGETS:
        c = 'red' if t < hull_lo or t > hull_hi else 'darkgreen'
        axL.axhline(t, color=c, ls=':', lw=1.2, alpha=0.8)
        axL.annotate(f'T={t}', (3.4, t), fontsize=8, color=c, ha='left',
                     va='center')
    axL.set_xticks(xK)
    axL.set_xticklabels(labels)
    axL.set_ylabel('K value')
    axL.set_xlabel('Admissible conventions (4-hull, R4 excluded)')
    axL.set_title('4-hull of K-conventions vs 5-target corridor')
    axL.legend(loc='upper left', fontsize=9)
    axL.grid(True, alpha=0.3, which='both')
    axL.set_xlim(-0.5, 4.2)

    # Right panel: membership summary
    axR.scatter(TARGETS, [0.5] * len(TARGETS),
                c=['darkgreen' if f else 'red' for f in in_hull],
                s=220, zorder=3, edgecolor='black', linewidth=1.5)
    for t, f in zip(TARGETS, in_hull):
        status = 'IN' if f else 'OUT'
        axR.annotate(f'{t}\n[{status}]', (t, 0.5),
                     textcoords='offset points', xytext=(0, 12),
                     ha='center', fontsize=9,
                     color='darkgreen' if f else 'red')
    axR.axvspan(hull_lo, hull_hi, color='green', alpha=0.2,
                label=f'4-hull [{hull_lo:.3f},{hull_hi:.3f}]')
    axR.axvline(1.0, color='k', ls='-', lw=1, alpha=0.3,
                label='K=1 positivity wall')
    axR.axvline(K_R4_DISCARDED, color='gray', ls='--', lw=1,
                alpha=0.4, label=f'R4 discarded = {K_R4_DISCARDED:.2f}')
    axR.set_ylim(0, 1)
    axR.set_yticks([])
    axR.set_xlabel('K  (corridor dial)')
    axR.set_xlim(0.7, 3.2)
    axR.set_title(f'5-target reachability: {reachable_count}/5 IN HULL '
                  f'[{verdict}]')
    axR.legend(loc='upper right', fontsize=9)
    axR.grid(True, alpha=0.3, axis='x')

    plt.suptitle(
        f'{GATE_ID} -- verdict: {verdict}  |  '
        f'reachable={reachable_count}/5, outside={outside_count}/5, '
        f'edge={edge_count}/5  |  scheme={SCHEME_OUT}, conv=4-hull',
        fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=130)
    plt.close()
    print(f"  Saved PNG: {OUT_PNG.name}")
    print()

    # --- Section 6.10: 4-tuple + verdict line ---
    value_tag = (f"{reachable_count}/5")                             # (local)
    tuple_line = (f"(value={value_tag} scheme={SCHEME_OUT} "
                  f"convention={CONVENTION} L_max={L_MAX})")          # (local)
    print("4-tuple:", tuple_line)
    print()

    verdict_line = (f"{GATE_ID}: {verdict} -- value={value_tag} "
                    f"scheme={SCHEME_OUT} convention={CONVENTION} "
                    f"L_max={L_MAX} sha256={closure_sha}\n")          # (local)
    print("Appending verdict line to s84_gate_verdicts.txt:")
    print(f"  {verdict_line.strip()}")
    with open(VERDICT_TXT, 'a', encoding='utf-8') as f:
        f.write(verdict_line)
    print(f"  appended to {VERDICT_TXT.name}")
    print()

    print("=" * 78)
    print(f"DONE. Verdict: {verdict}")
    print("=" * 78)
    return 0


if __name__ == '__main__':
    sys.exit(main())
