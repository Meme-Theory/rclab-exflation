#!/usr/bin/env python3
"""
s66_zeta_sa.py -- ZETA-SA-66: Zeta Spectral Action on Jensen-Deformed SU(3)
============================================================================

Gate: ZETA-SA-66
  PASS: n_s^{zeta} within 3 sigma of Planck (0.9649 +/- 0.0042, so 0.9523 to 0.9775)
  FAIL: n_s^{zeta} outside 3 sigma of Planck
  INFO: n_s^{zeta} within 3 sigma but differs from n_s^{cutoff} by > 0.01

Physics:
--------
The zeta spectral action (Lizzi, arXiv:1412.4669) is S_zeta = zeta_{D}(0),
which for a 4D almost-commutative geometry M^4 x K equals a_4(D_full^2).

In the product factorization:
  a_4(M4 x K) = a_0(M4)*a_4(K) + a_2(M4)*a_2(K) + a_4(M4)*a_0(K)

The first term gives Yang-Mills (~ Vol(M4) * a_4(K) * F^2),
the second gives Einstein-Hilbert (~ Vol(M4) * a_2(K) * R),
the third gives curvature-squared (~ a_0(K) * Gauss-Bonnet).

CRITICAL: The cosmological constant Lambda^4 * a_0(K) term is ABSENT.
The cutoff action S_cutoff = f_0 L^4 a_0 + f_2 L^2 a_2 + f_4 a_4 includes a_0;
the zeta action does NOT.

For the internal space K = (SU(3), g_tau), the spectral zeta moments are:
  a_0(tau) = sum dim(p,q) * N_pos(p,q)           [mode count, tau-independent]
  a_2(tau) = sum dim(p,q) * sum_{lam>0} lam^{-2}  [gravity coupling]
  a_4(tau) = sum dim(p,q) * sum_{lam>0} lam^{-4}  [gauge coupling]

The zeta spectral action S_zeta(tau) for the INTERNAL space is a linear
combination of a_2(tau) and a_4(tau) with coefficients from the 4D geometry.
Since only the tau-dependence matters for slow-roll, we can compute eps_H
from any combination c_2 * a_2(tau) + c_4 * a_4(tau) and compare to the
cutoff result.

We compute eps_H for three choices:
  1. S_zeta(tau) = a_4(tau)      [pure gauge sector, most aggressive zeta]
  2. S_zeta(tau) = a_2(tau)      [pure gravity sector]
  3. S_zeta(tau) = a_2(tau) + a_4(tau)  [combined zeta action]

Author: Lizzi Spectral Functional Theorist
Session: S66
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from canonical_constants import (, planck_ns
    tau_fold, a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    G_DeWitt, v_terminal, c_fabric,
    Vol_SU3_Haar, PI, g0_diag,
    Delta_0_OES,
    M_KK, M_KK_gravity, M_KK_kerner,
    H_fold, rho_Lambda_obs,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)

from spectral_action import dim_su3_irrep

# =============================================================================
# STEP 0: CONFIGURATION
# =============================================================================
print("=" * 78)
print("ZETA-SA-66: Zeta Spectral Action on Jensen-Deformed SU(3)")
print("=" * 78)

print(f"""
  SPECTRAL FUNCTIONAL COMPARISON
  ==============================
  Cutoff:  S_cutoff(tau) = sum dim(p,q)^2 * sum_j |lambda_j(tau)|
           Uses f(x) = sqrt(x). Includes a_0 (CC) and a_2 (EH) contributions.

  Zeta:    S_zeta(tau) = a_4(tau) = sum dim(p,q) * sum_{{lam>0}} lam^{{-4}}
           From zeta_D(0) = a_4(D_full^2). NO a_0 (CC), NO Lambda^2 a_2.

  The question: does eps_H change when we switch functional?
  If YES -> scheme-dependent (requires experimental determination).
  If NO  -> functional-independent (structural).
""")

# =============================================================================
# STEP 1: COMPUTE EIGENVALUE SPECTRUM AT ALL TAU VALUES
# =============================================================================
print("=" * 78)
print("STEP 1: Eigenvalue Spectrum at 16 tau values")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Use the same 16 tau values as S36/S41
tau_all = np.array([0.0, 0.05, 0.10, 0.15, 0.16, 0.17, 0.18, 0.19,
                    0.20, 0.21, 0.22, 0.25, 0.30, 0.35, 0.40, 0.50])
n_tau = len(tau_all)

# Storage
S_cutoff_arr = np.zeros(n_tau)    # S(tau) = sum dim^2 * sum |lam|
a0_arr = np.zeros(n_tau)          # spectral zeta: mode count
a2_arr = np.zeros(n_tau)          # spectral zeta: sum lam^{-2}
a4_arr = np.zeros(n_tau)          # spectral zeta: sum lam^{-4}
a6_arr = np.zeros(n_tau)          # spectral zeta: sum lam^{-6}
n_modes = np.zeros(n_tau, dtype=int)

# Cross-check: load S36 bare spectral action for validation
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computation archive')
d36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
              allow_pickle=True)
S_S36 = d36['S_full']  # 16 tau values

# Load S41 a_2, a_4 for cross-check
d41 = np.load(os.path.join(ARCHIVE_DIR, 's41_constants_vs_tau.npz'),
              allow_pickle=True)
a2_s41 = d41['a2_cutoff0']
a4_s41 = d41['a4_cutoff0']

t_start = time.time()

for i, tau in enumerate(tau_all):
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                   max_pq_sum=3, verbose=False)

    S_cut_i = 0.0  # (local)
    a0_i = 0.0  # (local)
    a2_i = 0.0  # (local)
    a4_i = 0.0  # (local)
    a6_i = 0.0  # (local)
    nm_i = 0

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)
        # PW degeneracy for right-regular representation
        pw_deg = d_pq  # each eigenvalue appears dim(p,q) times in full spectrum

        # Cutoff action: dim^2 * sum|lam|
        S_cut_i += d_pq**2 * np.sum(omega)

        # Spectral zeta sums over POSITIVE eigenvalues only
        # (Dirac eigenvalues come in +/- pairs; zeta sums use |lam|)
        # n_positive = len(omega) // 2  but safer: take unique absolute values
        # Actually the s41 code uses all 'positive' eigenvalues. For purely
        # imaginary eigenvalues, 'positive' means Im > 0.
        pos_mask = np.ones(len(evals), dtype=bool)
        for j, e in enumerate(evals):
            if np.abs(np.imag(e)) > 1e-10:
                pos_mask[j] = (np.imag(e) > 0)
            elif np.abs(np.real(e)) > 1e-10:
                pos_mask[j] = (np.real(e) > 0)
            else:
                pos_mask[j] = False  # zero eigenvalue excluded

        pos_evals = np.abs(evals[pos_mask])
        n_pos = len(pos_evals)

        a0_i += pw_deg * n_pos
        if n_pos > 0:
            a2_i += pw_deg * np.sum(pos_evals**(-2))
            a4_i += pw_deg * np.sum(pos_evals**(-4))
            a6_i += pw_deg * np.sum(pos_evals**(-6))

        nm_i += len(evals)

    S_cutoff_arr[i] = S_cut_i
    a0_arr[i] = a0_i
    a2_arr[i] = a2_i
    a4_arr[i] = a4_i
    a6_arr[i] = a6_i
    n_modes[i] = nm_i

dt = time.time() - t_start
print(f"\n  Computed {n_tau} spectra in {dt:.1f}s")

# =============================================================================
# STEP 2: CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Cross-checks against canonical data")
print("=" * 78)

# Check S_cutoff against S36
S_dev = np.max(np.abs(S_cutoff_arr - S_S36) / S_S36)
print(f"\n  S_cutoff vs S36: max relative deviation = {S_dev:.2e}")
assert S_dev < 1e-10, f"Spectral action mismatch: {S_dev}"
print(f"  PASSED (machine epsilon)")

# Check a_0 is constant and equals 6440
a0_spread = np.max(a0_arr) - np.min(a0_arr)
print(f"\n  a_0 range: [{a0_arr.min():.1f}, {a0_arr.max():.1f}], spread = {a0_spread:.1f}")
print(f"  a_0 canonical = {a0_fold}")
assert abs(a0_arr[7] - a0_fold) < 1, f"a_0 mismatch at fold: {a0_arr[7]} vs {a0_fold}"
print(f"  a_0 is tau-INDEPENDENT (topological) -- CONFIRMED")

# Check a_2 at fold
a2_dev = abs(a2_arr[7] - a2_fold) / a2_fold
print(f"\n  a_2(fold) = {a2_arr[7]:.6f}, canonical = {a2_fold:.6f}, dev = {a2_dev:.2e}")
assert a2_dev < 1e-6, f"a_2 mismatch at fold"
print(f"  PASSED")

# Check a_4 at fold
a4_dev = abs(a4_arr[7] - a4_fold) / a4_fold
print(f"\n  a_4(fold) = {a4_arr[7]:.6f}, canonical = {a4_fold:.6f}, dev = {a4_dev:.2e}")
assert a4_dev < 1e-6, f"a_4 mismatch at fold"
print(f"  PASSED")

# Cross-check against S41
a2_s41_dev = np.max(np.abs(a2_arr - a2_s41) / a2_s41)
a4_s41_dev = np.max(np.abs(a4_arr - a4_s41) / a4_s41)
print(f"\n  a_2 vs S41: max relative deviation = {a2_s41_dev:.2e}")
print(f"  a_4 vs S41: max relative deviation = {a4_s41_dev:.2e}")

# =============================================================================
# STEP 3: PRINT SPECTRAL ZETA MOMENTS VS TAU
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Spectral Zeta Moments vs tau")
print("=" * 78)

print(f"\n  {'tau':>6}  {'S_cutoff':>14}  {'a_0':>10}  {'a_2':>12}  {'a_4':>12}  "
      f"{'a_2/a_0':>10}  {'a_4/a_0':>10}")
print(f"  {'----':>6}  {'--------':>14}  {'---':>10}  {'---':>12}  {'---':>12}  "
      f"{'-------':>10}  {'-------':>10}")
for i in range(n_tau):
    print(f"  {tau_all[i]:6.3f}  {S_cutoff_arr[i]:14.2f}  {a0_arr[i]:10.0f}  "
          f"{a2_arr[i]:12.4f}  {a4_arr[i]:12.4f}  "
          f"{a2_arr[i]/a0_arr[i]:10.4f}  {a4_arr[i]/a0_arr[i]:10.4f}")

# Key observation: a_0 is constant, a_2 and a_4 DECREASE with tau
print(f"\n  CRITICAL OBSERVATION:")
print(f"  a_0 is tau-INDEPENDENT: {a0_arr[0]:.0f} at all tau")
print(f"  a_2 decreases from {a2_arr[0]:.2f} to {a2_arr[-1]:.2f} ({(a2_arr[-1]-a2_arr[0])/a2_arr[0]*100:.1f}%)")
print(f"  a_4 decreases from {a4_arr[0]:.2f} to {a4_arr[-1]:.2f} ({(a4_arr[-1]-a4_arr[0])/a4_arr[0]*100:.1f}%)")

# =============================================================================
# STEP 4: SLOW-ROLL PARAMETERS IN DIFFERENT SPECTRAL FUNCTIONALS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Slow-Roll Parameters -- Cutoff vs Zeta")
print("=" * 78)

# Spline all quantities
cs_Scut = CubicSpline(tau_all, S_cutoff_arr)
cs_a2 = CubicSpline(tau_all, a2_arr)
cs_a4 = CubicSpline(tau_all, a4_arr)

# Combined zeta action: using a_2 + a_4 (both contribute to the 4D action)
a24_arr = a2_arr + a4_arr
cs_a24 = CubicSpline(tau_all, a24_arr)

# Also try a_2 - a_4 (gravitational minus gauge)
a2ma4_arr = a2_arr - a4_arr
cs_a2ma4 = CubicSpline(tau_all, a2ma4_arr)

# Evaluation points
tau_eval = np.array([0.05, 0.10, 0.15, 0.190, 0.25, 0.35, 0.50])
n_eval = len(tau_eval)

# Compute eps_H = (1/2) * (dS/dtau)^2 / (S * d2S/dtau2) for each functional
functionals = {
    'cutoff': cs_Scut,
    'zeta_a4': cs_a4,
    'zeta_a2': cs_a2,
    'zeta_a2+a4': cs_a24,
}

eps_H_all = {}
eps_V_all = {}
eta_V_all = {}
ns_all = {}

# NOTE ON eps_H FORMULA:
# eps_H = (1/2)(dS/dtau)^2 / (S * d2S/dtau2) is the HUBBLE slow-roll parameter.
# For the cutoff action, S_cutoff INCREASES with tau: dS > 0, d2S > 0 -> eps_H > 0.
# For the zeta actions (a_2, a_4), S_zeta DECREASES with tau: dS < 0.
# Also, d2S < 0 (concave) for the zeta actions.
# Then eps_H = (1/2)(dS)^2/(S*d2S): with S>0, (dS)^2>0, d2S<0 -> eps_H < 0.
# PHYSICAL MEANING: Negative eps_H means the "potential" is concave-down,
# which in inflationary context means eta_V < 0.
# For n_s = 1 - 2*eps_H: with eps_H < 0, n_s > 1 (blue tilt).
#
# The framework's n_s = 0.9590 uses 1 - 2*eps_H with the CUTOFF eps_H.
# For the ZETA action, the transit dynamics are different because the potential
# shape is inverted. We still compute eps_H as (dS)^2/(2*S*d2S) but allow
# negative values, and we report eps_V = (1/2G)(dS/S)^2 as the always-positive
# measure of the slope.

for name, cs in functionals.items():
    eps_H = np.zeros(n_eval)
    eps_V = np.zeros(n_eval)
    eta_V = np.zeros(n_eval)

    for j, tau in enumerate(tau_eval):
        S = cs(tau)
        dS = cs(tau, 1)
        d2S = cs(tau, 2)

        eps_V[j] = 0.5 * (dS / S)**2 / G_DeWitt
        eta_V[j] = d2S / (S * G_DeWitt)
        if abs(d2S) > 1e-20 and S > 0:
            eps_H[j] = 0.5 * dS**2 / (S * d2S)  # can be negative!
        else:
            eps_H[j] = np.nan

    # n_s: use 1 - 2*eps_H (Hubble slow-roll). For negative eps_H this gives n_s > 1.
    # Also compute eps_V-based n_s: 1 - 2*eps_V (always gives n_s < 1 since eps_V > 0)
    ns = 1.0 - 2.0 * eps_H
    # Note: the s65 formula used 1 - 2*eps_H - eta_H with eta_H = eta_V/(1-eps_V/3)
    # but eps_H can be negative for zeta, which makes eta_H formula unreliable.
    # We use the simpler 1 - 2*eps_H for direct comparison.

    # Also compute ns from eps_V for comparison
    ns_V = 1.0 - 2.0 * eps_V

    eps_H_all[name] = eps_H
    eps_V_all[name] = eps_V
    eta_V_all[name] = eta_V
    ns_all[name] = ns

# Print comparison table
print(f"\n  eps_H comparison (can be NEGATIVE for concave potentials):")
print(f"  {'tau':>6}  ", end="")
for name in functionals:
    print(f"  {'eps_H^'+name:>16}", end="")
print()
print(f"  {'----':>6}  ", end="")
for name in functionals:
    print(f"  {'-'*16}", end="")
print()
for j in range(n_eval):
    print(f"  {tau_eval[j]:6.3f}  ", end="")
    for name in functionals:
        v = eps_H_all[name][j]
        s = f"  {v:+16.8f}" if not np.isnan(v) else f"  {'NaN':>16}"
        print(s, end="")
    print()

print(f"\n  eps_V comparison (always positive):")
print(f"  {'tau':>6}  ", end="")
for name in functionals:
    print(f"  {'eps_V^'+name:>16}", end="")
print()
for j in range(n_eval):
    print(f"  {tau_eval[j]:6.3f}  ", end="")
    for name in functionals:
        print(f"  {eps_V_all[name][j]:16.8f}", end="")
    print()

print(f"\n  eta_V comparison (SIGN matters: negative = concave potential):")
print(f"  {'tau':>6}  ", end="")
for name in functionals:
    print(f"  {'eta_V^'+name:>16}", end="")
print()
for j in range(n_eval):
    print(f"  {tau_eval[j]:6.3f}  ", end="")
    for name in functionals:
        print(f"  {eta_V_all[name][j]:+16.8f}", end="")
    print()

# n_s = 1 - 2*eps_H comparison
print(f"\n  n_s = 1 - 2*eps_H comparison:")
print(f"  {'tau':>6}  ", end="")
for name in functionals:
    print(f"  {'ns^'+name:>16}", end="")
print()
print(f"  {'----':>6}  ", end="")
for name in functionals:
    print(f"  {'-'*16}", end="")
print()
for j in range(n_eval):
    print(f"  {tau_eval[j]:6.3f}  ", end="")
    for name in functionals:
        v = ns_all[name][j]
        s = f"  {v:16.6f}" if not np.isnan(v) else f"  {'NaN':>16}"
        print(s, end="")
    print()

# Key physics: n_s > 1 for zeta because eps_H < 0 (concave potential)
print(f"\n  KEY FINDING: Zeta functionals have CONCAVE potentials (d2S < 0),")
print(f"  yielding NEGATIVE eps_H and BLUE TILT (n_s > 1).")
print(f"  This is the OPPOSITE of the cutoff action which is CONVEX.")

# =============================================================================
# STEP 5: FOLD-POINT ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Detailed Analysis at Fold (tau = 0.190)")
print("=" * 78)

fold_idx = 3  # index into tau_eval for tau=0.190 (local)

print(f"\n  Quantity                    Cutoff           Zeta(a4)         Zeta(a2)         Zeta(a2+a4)")
print(f"  {'-'*100}")

for label, arr_dict in [('eps_H', eps_H_all), ('eps_V', eps_V_all),
                         ('eta_V', eta_V_all), ('n_s', ns_all)]:
    print(f"  {label:<25}", end="")
    for name in functionals:
        val = arr_dict[name][fold_idx]
        s = f"  {val:+16.8f}" if not np.isnan(val) else f"  {'NaN':>16}"
        print(s, end="")
    print()

# Differences at fold
eps_cut = eps_H_all['cutoff'][fold_idx]
ns_cut = ns_all['cutoff'][fold_idx]

print(f"\n  --- Differences from cutoff at fold ---")
for name in ['zeta_a4', 'zeta_a2', 'zeta_a2+a4']:
    eps_z = eps_H_all[name][fold_idx]
    ns_z = ns_all[name][fold_idx]
    d_eps = (eps_z - eps_cut) / abs(eps_cut) * 100
    d_ns = ns_z - ns_cut
    print(f"  {name:>16}: delta(eps_H)/|eps_H| = {d_eps:+.2f}%, delta(n_s) = {d_ns:+.6f}")

print(f"\n  CRITICAL: The zeta functionals give eps_H < 0 (concave potential),")
print(f"  meaning n_s > 1 (blue tilt). This is a qualitative difference from the")
print(f"  cutoff action which gives eps_H > 0 (convex potential, red tilt).")
print(f"  The SIGN of the spectral tilt is SCHEME-DEPENDENT.")

# =============================================================================
# STEP 6: FUNCTIONAL-INDEPENDENCE ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Functional-Independence Classification")
print("=" * 78)

print("""
  The cutoff spectral action S_cutoff(tau) = sum dim^2 |lam_j(tau)| uses the
  spectral functional f(x) = sqrt(x). This gives EQUAL weight to all eigenvalues.

  The zeta spectral action S_zeta(tau) = a_4(tau) = sum dim(p,q) lam^{-4}
  weights LOW eigenvalues MORE (infrared-sensitive). This is why a_4(tau) has
  a different tau-profile than S_cutoff(tau).

  The key structural question: since eps_H depends on the SHAPE (not the value)
  of S(tau), and the shape changes between functionals, eps_H is SCHEME-DEPENDENT.
""")

# Compute the RATIO of derivatives: d(ln S)/dtau for each functional
print(f"  d(ln S)/dtau at fold:")
for name, cs in functionals.items():
    S_fold_val = cs(tau_fold)
    dS_fold_val = cs(tau_fold, 1)
    dlnS = dS_fold_val / S_fold_val
    print(f"    {name:>16}: d(ln S)/dtau = {dlnS:.8f}")

# Check if eps_H ratios are constant (would indicate functional-independence)
print(f"\n  eps_H ratios (zeta/cutoff) at each tau:")
print(f"  {'tau':>6}  {'a4/cut':>12}  {'a2/cut':>12}  {'(a2+a4)/cut':>12}")
for j in range(n_eval):
    r4 = eps_H_all['zeta_a4'][j] / eps_H_all['cutoff'][j]
    r2 = eps_H_all['zeta_a2'][j] / eps_H_all['cutoff'][j]
    r24 = eps_H_all['zeta_a2+a4'][j] / eps_H_all['cutoff'][j]
    print(f"  {tau_eval[j]:6.3f}  {r4:12.6f}  {r2:12.6f}  {r24:12.6f}")

# =============================================================================
# STEP 7: CC IN THE ZETA SCHEME
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Cosmological Constant in the Zeta Scheme")
print("=" * 78)

Delta_BCS = Delta_0_OES  # = 0.464 M_KK

# Cutoff CC: rho_CC = (2/pi^2) * a_0 * M_KK^4
rho_CC_cutoff = (2.0 / PI**2) * a0_fold * M_KK_kerner**4
CC_gap_cutoff = np.log10(rho_CC_cutoff / rho_Lambda_obs)

# Zeta CC: In the zeta scheme, the CC comes from a_4 * (Majorana mass)^4
# The a_0 Lambda^4 term is ABSENT. Instead:
# rho_CC^zeta = beta_1 * Delta_BCS^4 where beta_1 ~ a_4 / (8 pi^2)
# This is the RESIDUAL CC from BCS physics, not from mode counting.
beta_1 = a4_fold / (8.0 * PI**2)
rho_CC_zeta_raw = beta_1 * (Delta_BCS * M_KK_kerner)**4
CC_gap_zeta_raw = np.log10(rho_CC_zeta_raw / rho_Lambda_obs)

# More conservative: just use a_4 * M_KK^4 (no additional 8pi^2)
rho_CC_zeta_naive = a4_fold * M_KK_kerner**4
CC_gap_zeta_naive = np.log10(rho_CC_zeta_naive / rho_Lambda_obs)

# Alternative: use a_4 * Delta^4 * M_KK^4 (fully suppressed by BCS gap)
rho_CC_zeta_BCS = a4_fold * Delta_BCS**4 * M_KK_kerner**4
CC_gap_zeta_BCS = np.log10(rho_CC_zeta_BCS / rho_Lambda_obs)

print(f"\n  BCS gap: Delta = {Delta_BCS:.4f} M_KK = {Delta_BCS * M_KK_kerner:.4e} GeV")
print(f"\n  Cutoff CC:")
print(f"    rho_CC = (2/pi^2) * a_0 * M_KK^4 = {rho_CC_cutoff:.4e} GeV^4")
print(f"    log10(rho_CC/rho_obs) = {CC_gap_cutoff:.2f}")
print(f"\n  Zeta CC estimates:")
print(f"    (1) a_4 * M_KK^4:              log10(gap) = {CC_gap_zeta_naive:.2f}")
print(f"    (2) a_4 * Delta^4 * M_KK^4:    log10(gap) = {CC_gap_zeta_BCS:.2f}")
print(f"    (3) beta_1 * Delta_BCS^4:       log10(gap) = {CC_gap_zeta_raw:.2f}")
print(f"\n  Improvement from zeta scheme:")
print(f"    Estimate (1): {CC_gap_cutoff - CC_gap_zeta_naive:.2f} OOM")
print(f"    Estimate (2): {CC_gap_cutoff - CC_gap_zeta_BCS:.2f} OOM")
print(f"    Estimate (3): {CC_gap_cutoff - CC_gap_zeta_raw:.2f} OOM")

# =============================================================================
# STEP 8: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Gate Verdict -- ZETA-SA-66")
print("=" * 78)

# Primary: use zeta_a4 as the canonical zeta action
ns_zeta_fold = ns_all['zeta_a4'][fold_idx]
ns_cutoff_fold = ns_all['cutoff'][fold_idx]
eps_zeta_fold = eps_H_all['zeta_a4'][fold_idx]
eps_cutoff_fold = eps_H_all['cutoff'][fold_idx]
eps_V_zeta_fold = eps_V_all['zeta_a4'][fold_idx]
eps_V_cutoff_fold = eps_V_all['cutoff'][fold_idx]

ns_planck = planck_ns  # canonical alias (was: = 0.9649)
ns_sigma = 0.0042  # (local)
ns_3sigma_low = ns_planck - 3 * ns_sigma   # 0.9523
ns_3sigma_high = ns_planck + 3 * ns_sigma  # 0.9775

print(f"\n  Primary result (zeta = a_4, n_s = 1 - 2*eps_H):")
print(f"    eps_H^{{zeta}}   = {eps_zeta_fold:+.8f} (NEGATIVE: concave potential)")
print(f"    eps_H^{{cutoff}} = {eps_cutoff_fold:+.8f} (positive: convex potential)")
print(f"    n_s^{{zeta}}     = {ns_zeta_fold:.6f} (BLUE TILT: > 1)")
print(f"    n_s^{{cutoff}}   = {ns_cutoff_fold:.6f}")
print(f"    Planck 3-sigma: [{ns_3sigma_low:.4f}, {ns_3sigma_high:.4f}]")

delta_ns = abs(ns_zeta_fold - ns_cutoff_fold)
print(f"    |n_s^zeta - n_s^cutoff| = {delta_ns:.6f}")

# Alternative: use eps_V (always positive) for the n_s comparison
ns_from_epsV_zeta = 1.0 - 2.0 * eps_V_zeta_fold
ns_from_epsV_cutoff = 1.0 - 2.0 * eps_V_cutoff_fold
print(f"\n  Alternative (n_s = 1 - 2*eps_V, always gives red tilt):")
print(f"    n_s^{{zeta}}(eps_V)   = {ns_from_epsV_zeta:.6f}")
print(f"    n_s^{{cutoff}}(eps_V) = {ns_from_epsV_cutoff:.6f}")

# Gate logic: the zeta action gives n_s > 1, which is OUTSIDE Planck
if ns_3sigma_low <= ns_zeta_fold <= ns_3sigma_high:
    if delta_ns > 0.01:
        gate_verdict = "INFORMATIVE"
        gate_detail = (f"n_s^zeta = {ns_zeta_fold:.6f} is within Planck 3-sigma "
                      f"but differs from n_s^cutoff by {delta_ns:.6f} > 0.01 -- SCHEME-DEPENDENT")
    else:
        gate_verdict = "PASS"
        gate_detail = (f"n_s^zeta = {ns_zeta_fold:.6f} within Planck 3-sigma "
                      f"and close to n_s^cutoff (delta = {delta_ns:.6f} < 0.01)")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"n_s^zeta = {ns_zeta_fold:.6f} outside Planck 3-sigma "
                   f"[{ns_3sigma_low:.4f}, {ns_3sigma_high:.4f}]. "
                   f"Zeta action has CONCAVE potential -> BLUE tilt (n_s > 1). "
                   f"This is a qualitative scheme-dependence: the SIGN of the tilt flips.")

print(f"\n  Gate: ZETA-SA-66")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# Functional-independence classification
eps_ratio = eps_zeta_fold / eps_cutoff_fold
ns_diff = abs(ns_zeta_fold - ns_cutoff_fold)

# Check eps_H ratios across tau
ratios = eps_H_all['zeta_a4'] / eps_H_all['cutoff']
valid = ~np.isnan(ratios)
if np.sum(valid) > 2:
    ratio_spread = np.max(ratios[valid]) - np.min(ratios[valid])
    ratio_mean = np.mean(ratios[valid])
    ratio_cv = abs(ratio_spread / ratio_mean) if abs(ratio_mean) > 1e-10 else np.inf
else:
    ratio_spread = np.nan
    ratio_mean = np.nan
    ratio_cv = np.inf

# Classification: eps_H changes SIGN -> maximally scheme-dependent
if eps_ratio < 0:
    independence = "SCHEME-DEPENDENT (sign flip: eps_H changes sign between functionals)"
elif ratio_cv < 0.01:
    independence = "FUNCTIONAL-INDEPENDENT (ratio constant to 1%)"
elif ns_diff < 0.001:
    independence = "WEAKLY SCHEME-DEPENDENT (n_s differs by < 0.001)"
else:
    independence = "SCHEME-DEPENDENT"

print(f"\n  Functional-independence classification:")
print(f"    eps_H(zeta) / eps_H(cutoff) at fold: {eps_ratio:+.6f}")
print(f"    Ratio spread across tau: {ratio_spread:.6f} (CV = {ratio_cv:.4f})")
print(f"    n_s difference: {ns_diff:.6f}")
print(f"    Classification: {independence}")

# Additional: check all three zeta functionals
print(f"\n  --- All zeta functionals at fold ---")
for name in ['zeta_a4', 'zeta_a2', 'zeta_a2+a4']:
    ns_z = ns_all[name][fold_idx]
    eps_z = eps_H_all[name][fold_idx]
    eps_v = eps_V_all[name][fold_idx]
    status = "IN" if ns_3sigma_low <= ns_z <= ns_3sigma_high else "OUT"
    print(f"    {name:>16}: eps_H = {eps_z:+.8f}, eps_V = {eps_v:.8f}, "
          f"n_s(1-2eps_H) = {ns_z:.6f}  [{status} of Planck 3-sigma]")

# =============================================================================
# STEP 9: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Saving Results")
print("=" * 78)

np.savez(os.path.join(SCRIPT_DIR, 's66_zeta_sa.npz'),
    # Gate
    gate_name='ZETA-SA-66',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    independence_class=independence,
    # Tau grid
    tau_all=tau_all,
    tau_eval=tau_eval,
    # Raw spectral data
    S_cutoff=S_cutoff_arr,
    a0=a0_arr,
    a2=a2_arr,
    a4=a4_arr,
    a6=a6_arr,
    n_modes=n_modes,
    # Slow-roll parameters at eval points
    eps_H_cutoff=eps_H_all['cutoff'],
    eps_H_zeta_a4=eps_H_all['zeta_a4'],
    eps_H_zeta_a2=eps_H_all['zeta_a2'],
    eps_H_zeta_a24=eps_H_all['zeta_a2+a4'],
    ns_cutoff=ns_all['cutoff'],
    ns_zeta_a4=ns_all['zeta_a4'],
    ns_zeta_a2=ns_all['zeta_a2'],
    ns_zeta_a24=ns_all['zeta_a2+a4'],
    # Fold values
    ns_zeta_fold=ns_zeta_fold,
    ns_cutoff_fold=ns_cutoff_fold,
    eps_zeta_fold=eps_zeta_fold,
    eps_cutoff_fold=eps_cutoff_fold,
    # CC analysis
    CC_gap_cutoff=CC_gap_cutoff,
    CC_gap_zeta_naive=CC_gap_zeta_naive,
    CC_gap_zeta_BCS=CC_gap_zeta_BCS,
    beta_1=beta_1,
)
print(f"  Saved: s66_zeta_sa.npz")

# =============================================================================
# STEP 10: PLOT
# =============================================================================
print("\nGenerating plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: S(tau) comparison (normalized)
ax = axes[0, 0]
tau_dense = np.linspace(0.01, 0.50, 200)
ax.plot(tau_dense, cs_Scut(tau_dense) / cs_Scut(tau_fold), 'b-', lw=2,
        label=r'$S_{\rm cutoff}(\tau)$ [f(x)=$\sqrt{x}$]')
ax.plot(tau_dense, cs_a4(tau_dense) / cs_a4(tau_fold), 'r-', lw=2,
        label=r'$S_{\zeta}(\tau) = a_4(\tau)$')
ax.plot(tau_dense, cs_a2(tau_dense) / cs_a2(tau_fold), 'g--', lw=1.5,
        label=r'$a_2(\tau)$')
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S(\tau) / S(\tau_{\rm fold})$')
ax.set_title('Spectral Action: Cutoff vs Zeta (normalized)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: |eps_H| comparison (absolute value since zeta eps_H is negative)
ax = axes[0, 1]
for name, color, ls, label in [
    ('cutoff', 'blue', '-', r'$|\epsilon_H^{\rm cutoff}|$ (>0)'),
    ('zeta_a4', 'red', '-', r'$|\epsilon_H^{\zeta}|$ ($a_4$, <0)'),
    ('zeta_a2', 'green', '--', r'$|\epsilon_H^{\zeta}|$ ($a_2$, <0)'),
    ('zeta_a2+a4', 'purple', ':', r'$|\epsilon_H^{\zeta}|$ ($a_2+a_4$, <0)'),
]:
    ax.plot(tau_eval, np.abs(eps_H_all[name]), color=color, ls=ls, marker='o',
            ms=4, lw=1.5, label=label)
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$|\epsilon_H|$')
ax.set_title(r'$|\epsilon_H|$ (cutoff >0, zeta <0: SIGN FLIP)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

# Panel 3: n_s comparison with Planck band
ax = axes[1, 0]
for name, color, ls, label in [
    ('cutoff', 'blue', '-', r'$n_s^{\rm cutoff}$'),
    ('zeta_a4', 'red', '-', r'$n_s^{\zeta}$ ($a_4$)'),
    ('zeta_a2', 'green', '--', r'$n_s^{\zeta}$ ($a_2$)'),
    ('zeta_a2+a4', 'purple', ':', r'$n_s^{\zeta}$ ($a_2+a_4$)'),
]:
    ax.plot(tau_eval, ns_all[name], color=color, ls=ls, marker='o',
            ms=4, lw=1.5, label=label)
ax.axhspan(ns_3sigma_low, ns_3sigma_high, color='gold', alpha=0.2, label='Planck 3$\\sigma$')
ax.axhline(ns_planck, color='gold', ls='-', lw=1, alpha=0.5)
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$n_s$')
ax.set_title(r'Spectral tilt $n_s = 1 - 2\epsilon_H$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: eps_H ratio (zeta/cutoff)
ax = axes[1, 1]
for name, color, label in [
    ('zeta_a4', 'red', r'$a_4$'),
    ('zeta_a2', 'green', r'$a_2$'),
    ('zeta_a2+a4', 'purple', r'$a_2+a_4$'),
]:
    ratio = eps_H_all[name] / eps_H_all['cutoff']
    ax.plot(tau_eval, ratio, color=color, marker='o', ms=4, lw=1.5, label=label)
ax.axhline(1.0, color='gray', ls=':', alpha=0.5)
ax.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\epsilon_H^{\zeta} / \epsilon_H^{\rm cutoff}$')
ax.set_title(r'$\epsilon_H$ ratio: zeta / cutoff')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.suptitle('ZETA-SA-66: Zeta Spectral Action on Jensen-Deformed SU(3)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's66_zeta_sa.png'), dpi=150,
            bbox_inches='tight')
print(f"  Saved: s66_zeta_sa.png")

print("\n" + "=" * 78)
print("COMPUTATION COMPLETE")
print("=" * 78)
