#!/usr/bin/env python3
"""
s74_r_family_stability.py -- R-FAMILY-STABILITY-74 (W2-M)
==========================================================

Gate: R-FAMILY-STABILITY-74
  Task: Compute a_8 at L_max in {3, 5, 7} and test R_2 = a_2*a_6/a_4^2 and
        R_3 = a_4*a_8/a_6^2 for L_max stability and uniformity with R_1.

  PASS if:
      (A) |R_i(L=5) - R_i(L=7)| / |R_i(L=7)| < 0.05 for i = 1, 2, 3 AND
      (B) |R_2 - R_1| < 0.2 AND |R_3 - R_1| < 0.2
  INFO if:
      A passes but B fails (stable but non-uniform)
  FAIL if:
      A fails (unstable under L_max)

Physics (substrate framing):
----------------------------
The R-family {R_1, R_2, R_3, ...} are dimensionless ratios of Seeley-DeWitt
spectral moments of the Dirac operator D_K at the Jensen fold. Each R_i
has volume dimension [Vol^2] / [Vol^2] = Vol^0, so Vol(SU(3)) cancels by
Baptista's B2 theorem. The question: does protection extend up the ladder?

  R_1 = a_0 * a_4 / a_2^2    (W1-M canonical: 1.128655 at L_max=3)
  R_2 = a_2 * a_6 / a_4^2    (new for W2-M)
  R_3 = a_4 * a_8 / a_6^2    (new for W2-M)

If the R-family is L_max-stable AND uniform (each R_i close to R_1), then
framework observables can be recast via R-family instead of individual
a_k, eliminating L_max fragility.

Convention: S73B project convention (half-spectrum)
    a_k = 0.5 * sum_{n: level<=L_max, lam_n>cutoff} d_n * |lam_n|^{-k}
matching W1-M (R_1 = 1.128655 at L_max=3) and canonical_constants.py
entries a0_fold, a2_fold, a4_fold.

Cross-reference W1-C (Wodzicki convention):
  R_1 = 1.434, R_2 = 1.238, R_3 = 1.141 at L_max=7
  |R_2 - R_1|_Wodzicki = 0.196 (marginal)
  |R_3 - R_1|_Wodzicki = 0.294 (FAIL)

The S73B convention is expected to give different absolute values but
the same qualitative stability pattern. We test both.

Agent: van-den-dungen-bridge-theorist (Session 74, Wave 2, Batch 3)
Parent action: S73B mack-vdd workshop carry-forward #5
"""

import numpy as np
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# CANONICAL CONSTANTS import
from canonical_constants import (
    tau_fold, PI,
    a0_fold, a2_fold, a4_fold,
    Vol_SU3_Haar, M_KK,
)

# ============================================================================
# CONFIGURATION
# ============================================================================

print("=" * 78)
print("R-FAMILY-STABILITY-74 (W2-M, S74 Wave 2 Batch 3)")
print("=" * 78)
print()
print(f"  tau_fold = {tau_fold}")
print(f"  Canonical R_1 (S42 fold): {a0_fold*a4_fold/a2_fold**2:.6f}")
print(f"  W1-M canonical: R_1 = 1.128655 at L_max=3")
print()

SPECTRUM_CACHE = 's74_spectrum_cache_L9_tau019.npz'  # (local)
EVAL_CUTOFF = 0.01  # (local) same as s73b_sdw_validation
L_MAX_VALUES = [3, 5, 7]  # (local) per W2-M task specification
L_MAX_VALUES_EXTENDED = [3, 5, 7, 9]  # (local) extended for context

W1M_R1_CANONICAL = 1.128655  # (local) W1-M canonical value at L_max=3

# Pre-registered gate thresholds
STABILITY_THRESHOLD = 0.05  # (local) (A) |R(L=5)-R(L=7)|/|R(L=7)|
UNIFORMITY_THRESHOLD = 0.2   # (local) (B) |R_i - R_1|


# ============================================================================
# STEP 1: LOAD SPECTRUM CACHE
# ============================================================================

print("=" * 78)
print("STEP 1: LOAD W1-C SPECTRUM CACHE")
print("=" * 78)

if not os.path.exists(SPECTRUM_CACHE):
    print(f"ERROR: Cache not found at {SPECTRUM_CACHE}")
    sys.exit(1)

cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
sector_evals_raw = cache['sector_evals'].item()
cache.close()
print(f"  Loaded {len(sector_evals_raw)} sectors from cache")
print(f"  Spectrum source: W1-C L_max=9 full enumeration at tau_fold=0.19")
print()


# ============================================================================
# STEP 2: COMPUTE a_0..a_8 IN S73B CONVENTION AT L_max IN {3, 5, 7, 9}
# ============================================================================

print("=" * 78)
print("STEP 2: S73B CONVENTION MOMENTS a_0..a_8")
print("=" * 78)


def compute_moments_S73B(L_max, cutoff):
    """Compute a_0..a_8 in the S73B half-spectrum convention.

    a_k = 0.5 * sum_{n: level <= L_max, lam_n > cutoff} d_n * |lam_n|^{-k}
    for k in {0, 2, 4, 6, 8}. The factor 0.5 is the positive-half convention.
    d_n = dim(p,q) of the irrep the eigenvalue belongs to.
    """
    all_abs = []
    all_mults = []
    n_sectors = 0  # (local)
    for (p, q), data in sorted(sector_evals_raw.items()):
        if data['level'] <= L_max:
            n_sectors += 1
            for ev in data['abs_evals']:
                all_abs.append(float(ev))
                all_mults.append(int(data['dim']))
    all_abs = np.array(all_abs)
    all_mults = np.array(all_mults, dtype=np.float64)

    mask = all_abs > cutoff
    lam = all_abs[mask]
    mult = all_mults[mask]

    a0_S = 0.5 * float(np.sum(mult))              # (local) half-count
    a2_S = 0.5 * float(np.sum(mult / lam**2))     # (local) half zeta_D(1)
    a4_S = 0.5 * float(np.sum(mult / lam**4))     # (local) half zeta_D(2)
    a6_S = 0.5 * float(np.sum(mult / lam**6))     # (local) half zeta_D(3)
    a8_S = 0.5 * float(np.sum(mult / lam**8))     # (local) half zeta_D(4)

    n_weighted = int(np.sum(mult))
    lam_min = float(np.min(lam))
    lam_max = float(np.max(lam))

    return {
        'n_sectors': n_sectors,
        'n_weighted': n_weighted,
        'lam_min': lam_min,
        'lam_max': lam_max,
        'a0': a0_S, 'a2': a2_S, 'a4': a4_S, 'a6': a6_S, 'a8': a8_S,
    }


results_S73B = {}
print(f"\n  {'L_max':>5} {'n_wgt':>8} {'a_0':>14} {'a_2':>14} "
      f"{'a_4':>14} {'a_6':>14} {'a_8':>16}")
print("  " + "-" * 96)
for L in L_MAX_VALUES_EXTENDED:
    r = compute_moments_S73B(L, EVAL_CUTOFF)
    results_S73B[L] = r
    print(f"  {L:>5d} {r['n_weighted']:>8d} {r['a0']:>14.4f} "
          f"{r['a2']:>14.4f} {r['a4']:>14.4f} {r['a6']:>14.6f} {r['a8']:>16.8f}")


# ============================================================================
# STEP 3: COMPUTE R_1, R_2, R_3 IN S73B CONVENTION
# ============================================================================

print("\n" + "=" * 78)
print("STEP 3: R_1, R_2, R_3 (S73B CONVENTION)")
print("=" * 78)

print(f"\n  {'L_max':>5} {'R_1=a0*a4/a2^2':>20} {'R_2=a2*a6/a4^2':>20} "
      f"{'R_3=a4*a8/a6^2':>20}")
print("  " + "-" * 70)
R1_table = {}  # (local)
R2_table = {}  # (local)
R3_table = {}  # (local)
for L in L_MAX_VALUES_EXTENDED:
    r = results_S73B[L]
    R1 = r['a0'] * r['a4'] / r['a2']**2
    R2 = r['a2'] * r['a6'] / r['a4']**2
    R3 = r['a4'] * r['a8'] / r['a6']**2
    R1_table[L] = R1
    R2_table[L] = R2
    R3_table[L] = R3
    print(f"  {L:>5d} {R1:>20.8f} {R2:>20.8f} {R3:>20.8f}")

# Cross-check R_1 at L_max=3 vs W1-M canonical
R1_L3 = R1_table[3]  # (local)
dev_from_W1M = abs(R1_L3 - W1M_R1_CANONICAL) / W1M_R1_CANONICAL  # (local)
print(f"\n  CROSS-CHECK: R_1(L=3) vs W1-M canonical")
print(f"    Computed: {R1_L3:.8f}")
print(f"    W1-M:     {W1M_R1_CANONICAL:.8f}")
print(f"    Rel dev:  {dev_from_W1M:.2e} (must be <1e-5 for agreement)")


# ============================================================================
# STEP 4: GATE (A) -- L_max STABILITY TEST
# ============================================================================

print("\n" + "=" * 78)
print("STEP 4: GATE (A) -- L_max STABILITY |R(L=5)-R(L=7)|/|R(L=7)|")
print("=" * 78)

def rel_stab(R_at_5, R_at_7):
    return abs(R_at_5 - R_at_7) / abs(R_at_7)

stab_R1 = rel_stab(R1_table[5], R1_table[7])  # (local)
stab_R2 = rel_stab(R2_table[5], R2_table[7])  # (local)
stab_R3 = rel_stab(R3_table[5], R3_table[7])  # (local)

print(f"\n  Stability threshold (A): < {STABILITY_THRESHOLD:.3f}")
print(f"  |R_1(L=5) - R_1(L=7)| / |R_1(L=7)| = {stab_R1:.6f} "
      f"-- {'PASS' if stab_R1 < STABILITY_THRESHOLD else 'FAIL'}")
print(f"  |R_2(L=5) - R_2(L=7)| / |R_2(L=7)| = {stab_R2:.6f} "
      f"-- {'PASS' if stab_R2 < STABILITY_THRESHOLD else 'FAIL'}")
print(f"  |R_3(L=5) - R_3(L=7)| / |R_3(L=7)| = {stab_R3:.6f} "
      f"-- {'PASS' if stab_R3 < STABILITY_THRESHOLD else 'FAIL'}")

gate_A_pass = (stab_R1 < STABILITY_THRESHOLD and
               stab_R2 < STABILITY_THRESHOLD and
               stab_R3 < STABILITY_THRESHOLD)
print(f"\n  Gate (A) stability: {'PASS' if gate_A_pass else 'FAIL'}")


# ============================================================================
# STEP 5: GATE (B) -- UNIFORMITY TEST |R_i - R_1| < 0.2
# ============================================================================

print("\n" + "=" * 78)
print("STEP 5: GATE (B) -- UNIFORMITY |R_i - R_1| < 0.2 (at L_max=7)")
print("=" * 78)

# Use L_max=7 as the deepest stable value per W2-M task
L_ref = 7  # (local)
R1_ref = R1_table[L_ref]  # (local)
R2_ref = R2_table[L_ref]  # (local)
R3_ref = R3_table[L_ref]  # (local)

diff_R2_R1 = abs(R2_ref - R1_ref)  # (local)
diff_R3_R1 = abs(R3_ref - R1_ref)  # (local)

print(f"\n  Uniformity threshold (B): < {UNIFORMITY_THRESHOLD:.2f}")
print(f"  R_1(L=7) = {R1_ref:.8f}")
print(f"  R_2(L=7) = {R2_ref:.8f}")
print(f"  R_3(L=7) = {R3_ref:.8f}")
print(f"  |R_2 - R_1| = {diff_R2_R1:.6f} "
      f"-- {'PASS' if diff_R2_R1 < UNIFORMITY_THRESHOLD else 'FAIL'}")
print(f"  |R_3 - R_1| = {diff_R3_R1:.6f} "
      f"-- {'PASS' if diff_R3_R1 < UNIFORMITY_THRESHOLD else 'FAIL'}")

gate_B_pass = (diff_R2_R1 < UNIFORMITY_THRESHOLD and
               diff_R3_R1 < UNIFORMITY_THRESHOLD)
print(f"\n  Gate (B) uniformity: {'PASS' if gate_B_pass else 'FAIL'}")


# Also check uniformity at L_max=3 for comparison with W1-M
R1_L3 = R1_table[3]  # (local)
R2_L3 = R2_table[3]  # (local)
R3_L3 = R3_table[3]  # (local)
diff_R2_R1_L3 = abs(R2_L3 - R1_L3)  # (local)
diff_R3_R1_L3 = abs(R3_L3 - R1_L3)  # (local)
print(f"\n  Auxiliary (at L_max=3, the W1-M reference point):")
print(f"    R_1(L=3) = {R1_L3:.8f}")
print(f"    R_2(L=3) = {R2_L3:.8f}")
print(f"    R_3(L=3) = {R3_L3:.8f}")
print(f"    |R_2 - R_1| = {diff_R2_R1_L3:.6f}")
print(f"    |R_3 - R_1| = {diff_R3_R1_L3:.6f}")


# ============================================================================
# STEP 6: GATE VERDICT
# ============================================================================

print("\n" + "=" * 78)
print("STEP 6: PRE-REGISTERED GATE VERDICT")
print("=" * 78)

if gate_A_pass and gate_B_pass:
    verdict = "PASS"
    reason = (f"(A) L_max stability: all three R_i have |R(L=5)-R(L=7)|/|R(L=7)| "
              f"< {STABILITY_THRESHOLD} at L_max=7. (B) Uniformity: "
              f"|R_2 - R_1| = {diff_R2_R1:.3f} and |R_3 - R_1| = {diff_R3_R1:.3f} "
              f"both below {UNIFORMITY_THRESHOLD}. R-family protection extends to "
              f"R_2 and R_3 in the S73B convention.")
elif gate_A_pass and not gate_B_pass:
    verdict = "INFO"
    reason = (f"(A) PASS: all R_i L_max-stable at {STABILITY_THRESHOLD} level. "
              f"(B) FAIL: uniformity violated -- "
              f"|R_2-R_1|={diff_R2_R1:.3f}, |R_3-R_1|={diff_R3_R1:.3f}. "
              f"R-family is STABLE under L_max but NON-UNIFORM across the ladder. "
              f"R_1 is protected but each R_i has its own distinct value.")
else:
    verdict = "FAIL"
    reason = (f"(A) FAIL: at least one R_i has L_max instability > "
              f"{STABILITY_THRESHOLD}. R_1={stab_R1:.4f}, R_2={stab_R2:.4f}, "
              f"R_3={stab_R3:.4f}. R-family protection does not survive "
              f"L_max truncation.")

print(f"\n  Gate verdict: {verdict}")
print(f"  Reason: {reason}")


# ============================================================================
# STEP 7: COMPARISON WITH W1-C WODZICKI VALUES
# ============================================================================

print("\n" + "=" * 78)
print("STEP 7: CONVENTION COMPARISON -- W1-C WODZICKI VALUES")
print("=" * 78)


def compute_moments_Wodzicki(L_max, cutoff):
    """Compute a_0..a_8 in the W1-C Wodzicki convention.

    For d = 8:
      a_0 ~ zeta_D(4) = sum d_n / lam_n^8
      a_2 ~ zeta_D(3) = sum d_n / lam_n^6
      a_4 ~ zeta_D(2) = sum d_n / lam_n^4
      a_6 ~ zeta_D(1) = sum d_n / lam_n^2
      a_8 ~ zeta_D(0) = sum d_n
    """
    all_abs = []
    all_mults = []
    for (p, q), data in sorted(sector_evals_raw.items()):
        if data['level'] <= L_max:
            for ev in data['abs_evals']:
                all_abs.append(float(ev))
                all_mults.append(int(data['dim']))
    all_abs = np.array(all_abs)
    all_mults = np.array(all_mults, dtype=np.float64)
    mask = all_abs > cutoff
    lam = all_abs[mask]
    mult = all_mults[mask]

    P0 = float(np.sum(mult))
    P1 = float(np.sum(mult / lam**2))
    P2 = float(np.sum(mult / lam**4))
    P3 = float(np.sum(mult / lam**6))
    P4 = float(np.sum(mult / lam**8))

    return {'a0': P4, 'a2': P3, 'a4': P2, 'a6': P1, 'a8': P0}


print(f"\n  {'L_max':>5} {'R_1(W)':>14} {'R_2(W)':>14} {'R_3(W)':>14}")
print("  " + "-" * 60)
R1_W_tab = {}  # (local)
R2_W_tab = {}  # (local)
R3_W_tab = {}  # (local)
for L in L_MAX_VALUES_EXTENDED:
    rW = compute_moments_Wodzicki(L, EVAL_CUTOFF)
    R1W = rW['a0'] * rW['a4'] / rW['a2']**2
    R2W = rW['a2'] * rW['a6'] / rW['a4']**2
    R3W = rW['a4'] * rW['a8'] / rW['a6']**2
    R1_W_tab[L] = R1W
    R2_W_tab[L] = R2W
    R3_W_tab[L] = R3W
    print(f"  {L:>5d} {R1W:>14.6f} {R2W:>14.6f} {R3W:>14.6f}")

# W1-C reported Wodzicki at L_max=7
print(f"\n  W1-C reported Wodzicki values (L_max=7):")
print(f"    R_1 = 1.434 (target), computed = {R1_W_tab[7]:.6f}")
print(f"    R_2 = 1.238 (target), computed = {R2_W_tab[7]:.6f}")
print(f"    R_3 = 1.141 (target), computed = {R3_W_tab[7]:.6f}")
print(f"    |R_2-R_1|_W = {abs(R2_W_tab[7]-R1_W_tab[7]):.3f}")
print(f"    |R_3-R_1|_W = {abs(R3_W_tab[7]-R1_W_tab[7]):.3f}")
print()
print("  The two conventions give DIFFERENT numerical values for each R_i but")
print("  both satisfy the same gate definition structure. S73B convention is")
print("  canonical for this project (matches canonical_constants.py).")


# ============================================================================
# STEP 8: DIMENSIONAL CONSISTENCY CHECK
# ============================================================================

print("\n" + "=" * 78)
print("STEP 8: DIMENSIONAL CONSISTENCY")
print("=" * 78)

# In S73B convention (a_k = 0.5 sum d_n / lam^k):
#   [a_k] = [lam]^{-k} = [M]^{-k}  (mass-dimension interpretation)
# R_1 = a_0 * a_4 / a_2^2  -->  [M^0] * [M^{-4}] / [M^{-4}] = [M^0]
# R_2 = a_2 * a_6 / a_4^2  -->  [M^{-2}] * [M^{-6}] / [M^{-8}] = [M^0]
# R_3 = a_4 * a_8 / a_6^2  -->  [M^{-4}] * [M^{-8}] / [M^{-12}] = [M^0]
# All dimensionless. PASS.

print("  S73B convention mass dimensions:")
print("    [a_k] = [M]^{-k}  (half-zeta of 1/lam^k)")
print()
print("    [R_1] = [a_0][a_4]/[a_2]^2 = [M^0 * M^{-4}] / [M^{-4}] = [M^0]. PASS.")
print("    [R_2] = [a_2][a_6]/[a_4]^2 = [M^{-2} * M^{-6}] / [M^{-8}] = [M^0]. PASS.")
print("    [R_3] = [a_4][a_8]/[a_6]^2 = [M^{-4} * M^{-8}] / [M^{-12}] = [M^0]. PASS.")
print()
print("  All three R_i are dimensionless. Volume cancellation per Baptista B2:")

# Scale check
for gamma in [0.5, 1.0, -1.0]:
    scale = Vol_SU3_Haar ** gamma
    rs = results_S73B[7]
    a0s = rs['a0'] * scale
    a2s = rs['a2'] * scale
    a4s = rs['a4'] * scale
    a6s = rs['a6'] * scale
    a8s = rs['a8'] * scale
    R1s = a0s * a4s / a2s**2
    R2s = a2s * a6s / a4s**2
    R3s = a4s * a8s / a6s**2
    R1u = rs['a0'] * rs['a4'] / rs['a2']**2
    R2u = rs['a2'] * rs['a6'] / rs['a4']**2
    R3u = rs['a4'] * rs['a8'] / rs['a6']**2
    print(f"    Vol^{gamma:+.1f}: |dR_1|={abs(R1s-R1u):.2e}, "
          f"|dR_2|={abs(R2s-R2u):.2e}, |dR_3|={abs(R3s-R3u):.2e}")


# ============================================================================
# STEP 9: SAVE OUTPUT DATA
# ============================================================================

print("\n" + "=" * 78)
print("STEP 9: SAVE OUTPUT DATA")
print("=" * 78)

OUTPUT_FILE = 's74_r_family_stability.npz'  # (local)

np.savez(
    OUTPUT_FILE,
    # Gate metadata
    gate_name=np.array("R-FAMILY-STABILITY-74"),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(reason),
    # S73B convention -- primary
    L_max_values=np.array(L_MAX_VALUES_EXTENDED),
    R1_S73B=np.array([R1_table[L] for L in L_MAX_VALUES_EXTENDED]),
    R2_S73B=np.array([R2_table[L] for L in L_MAX_VALUES_EXTENDED]),
    R3_S73B=np.array([R3_table[L] for L in L_MAX_VALUES_EXTENDED]),
    a0_S73B=np.array([results_S73B[L]['a0'] for L in L_MAX_VALUES_EXTENDED]),
    a2_S73B=np.array([results_S73B[L]['a2'] for L in L_MAX_VALUES_EXTENDED]),
    a4_S73B=np.array([results_S73B[L]['a4'] for L in L_MAX_VALUES_EXTENDED]),
    a6_S73B=np.array([results_S73B[L]['a6'] for L in L_MAX_VALUES_EXTENDED]),
    a8_S73B=np.array([results_S73B[L]['a8'] for L in L_MAX_VALUES_EXTENDED]),
    n_weighted_S73B=np.array(
        [results_S73B[L]['n_weighted'] for L in L_MAX_VALUES_EXTENDED]),
    # Wodzicki cross-check
    R1_Wodzicki=np.array([R1_W_tab[L] for L in L_MAX_VALUES_EXTENDED]),
    R2_Wodzicki=np.array([R2_W_tab[L] for L in L_MAX_VALUES_EXTENDED]),
    R3_Wodzicki=np.array([R3_W_tab[L] for L in L_MAX_VALUES_EXTENDED]),
    # Gate (A) L_max stability
    stab_R1=stab_R1,
    stab_R2=stab_R2,
    stab_R3=stab_R3,
    stability_threshold=STABILITY_THRESHOLD,
    gate_A_pass=gate_A_pass,
    # Gate (B) uniformity
    diff_R2_R1_L7=diff_R2_R1,
    diff_R3_R1_L7=diff_R3_R1,
    diff_R2_R1_L3=diff_R2_R1_L3,
    diff_R3_R1_L3=diff_R3_R1_L3,
    uniformity_threshold=UNIFORMITY_THRESHOLD,
    gate_B_pass=gate_B_pass,
    # Cross-check: W1-M
    dev_from_W1M=dev_from_W1M,
    W1M_canonical_R1=W1M_R1_CANONICAL,
    EVAL_CUTOFF=EVAL_CUTOFF,  # (local)
)
print(f"  Saved: {OUTPUT_FILE}")


# ============================================================================
# STEP 10: PLOT
# ============================================================================

print("\n" + "=" * 78)
print("STEP 10: PRODUCE PLOT")
print("=" * 78)

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Panel 1: R-family at each L_max in S73B convention
ax = axes[0]
R1_arr = [R1_table[L] for L in L_MAX_VALUES_EXTENDED]
R2_arr = [R2_table[L] for L in L_MAX_VALUES_EXTENDED]
R3_arr = [R3_table[L] for L in L_MAX_VALUES_EXTENDED]
ax.plot(L_MAX_VALUES_EXTENDED, R1_arr, 'o-', label='R_1 = a_0*a_4/a_2^2',
        color='navy', markersize=10, lw=2)
ax.plot(L_MAX_VALUES_EXTENDED, R2_arr, 's-', label='R_2 = a_2*a_6/a_4^2',
        color='darkred', markersize=10, lw=2)
ax.plot(L_MAX_VALUES_EXTENDED, R3_arr, '^-', label='R_3 = a_4*a_8/a_6^2',
        color='darkgreen', markersize=10, lw=2)
ax.axhline(W1M_R1_CANONICAL, color='navy', ls='--', alpha=0.5,
           label=f'W1-M canonical R_1={W1M_R1_CANONICAL:.6f}')
ax.set_xlabel('L_max')
ax.set_ylabel('R_i (S73B convention)')
ax.set_title('R-family stability (S73B convention)')
ax.legend(fontsize=8, loc='best')
ax.grid(True, alpha=0.3)
ax.set_xticks(L_MAX_VALUES_EXTENDED)

# Panel 2: Convention comparison (S73B vs Wodzicki) at L_max=7
ax = axes[1]
labels_c = ['R_1', 'R_2', 'R_3']
S73B_L7 = [R1_table[7], R2_table[7], R3_table[7]]  # (local)
W_L7 = [R1_W_tab[7], R2_W_tab[7], R3_W_tab[7]]  # (local)
x = np.arange(len(labels_c))
width = 0.35  # (local)
ax.bar(x - width/2, S73B_L7, width, label='S73B (canonical)', color='navy', alpha=0.8)
ax.bar(x + width/2, W_L7, width, label='Wodzicki (W1-C)', color='darkred', alpha=0.8)
ax.axhline(1.0, color='grey', ls=':', lw=1, alpha=0.7)
ax.set_xticks(x)
ax.set_xticklabels(labels_c)
ax.set_ylabel('Ratio value at L_max=7')
ax.set_title('S73B vs Wodzicki conventions (L_max=7)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# Value labels
for i, (v1, v2) in enumerate(zip(S73B_L7, W_L7)):
    ax.text(i - width/2, v1 + 0.01, f'{v1:.3f}', ha='center', fontsize=7)
    ax.text(i + width/2, v2 + 0.01, f'{v2:.3f}', ha='center', fontsize=7)

# Gate annotation on panel 1
gate_text = (
    f"Gate R-FAMILY-STABILITY-74\n"
    f"Verdict: {verdict}\n"
    f"(A) L_max stability <5%:\n"
    f"  R_1: {stab_R1*100:.3f}%  R_2: {stab_R2*100:.3f}%  R_3: {stab_R3*100:.3f}%\n"
    f"(B) Uniformity <0.2 (at L=7):\n"
    f"  |R_2-R_1| = {diff_R2_R1:.4f}\n"
    f"  |R_3-R_1| = {diff_R3_R1:.4f}"
)
axes[0].text(
    0.98, 0.02, gate_text, transform=axes[0].transAxes, va='bottom', ha='right',
    family='monospace', fontsize=7,
    bbox=dict(facecolor='lightyellow', edgecolor='black', alpha=0.9, pad=0.5)
)

plt.suptitle(f'R-FAMILY-STABILITY-74 (W2-M): verdict = {verdict}',
             fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('s74_r_family_stability.png', dpi=120, bbox_inches='tight')
print(f"  Saved: s74_r_family_stability.png")

print("\n" + "=" * 78)
print(f"R-FAMILY-STABILITY-74 (W2-M): {verdict}")
print("=" * 78)
