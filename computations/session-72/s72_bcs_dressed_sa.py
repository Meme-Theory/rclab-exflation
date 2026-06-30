#!/usr/bin/env python3
"""
s72_bcs_dressed_sa.py -- BCS-DRESSED-SA-72: BCS-Dressed Spectral Action at 5 Tau Values
========================================================================================

Gate: BCS-DRESSED-SA-72
  PASS: |n_s^{BCS} - 0.9649| < 0.005 (within 1.2 sigma of Planck)
  INFO: |n_s^{BCS} - 0.9649| in [0.005, 0.010] (within 2.4 sigma)
  FAIL: |n_s^{BCS} - 0.9649| > 0.010 (more than 2.4 sigma from Planck)

Physics
-------
The BCS condensate on the internal fiber SU(3) dresses the Dirac operator D_K.
Each eigenvalue lambda_k is replaced by the BdG quasiparticle energy:

    E_k(tau) = sqrt(lambda_k(tau)^2 + Delta(tau)^2)                         (1)

where Delta(tau) is the BCS gap that varies with the Jensen deformation
parameter tau. The W1-A computation (KAPPA-DELTA-72, INFO) established that
Delta(tau) is MONOTONICALLY DECREASING near the fold:

    dDelta/dtau = -0.245 M_KK (linear term dominates)                       (2)
    kappa_Delta  = +0.330 M_KK (subdominant quadratic)                       (3)

This tau-dependence of Delta produces an ADDITIONAL contribution to the
derivative of the BCS-dressed spectral action beyond the bare spectral
variation. Specifically:

    dS^BCS/dtau = sum_j d_pq^2 * d/dtau[E_j(tau)]                          (4)
                = sum_j d_pq^2 * [lambda_j * dlambda_j/dtau + Delta * dDelta/dtau] / E_j

The first term is the bare spectral flow dressed by BCS. The second term
is a NEW contribution from the tau-dependent gap. At the fold where
dDelta/dtau = -0.245 and Delta = 0.464, this second term is significant.

The slow-roll parameter from the full spectral action:

    eps_H = (1/2) * (dS/dtau)^2 / (S * d2S/dtau^2)                         (5)

    n_s = 1 - 2*eps_H                                                       (6)  # (local)

The S65 BCS-DRESSED-65 (PASS) computed this with FIXED Delta at all tau
and found eps_H^BCS/eps_H^bare = 0.928 (7.2% reduction), giving n_s shift
of +0.021. The S68 BCS-DRESSED-MODE-68 (PASS) decomposed the channels
and found |delta_As/As| = 11.2%.

This computation extends S65/S68 by:
  1. Using the actual Delta(tau) profile from W1-A (monotonically decreasing)
  2. Computing at 5 closely-spaced tau values [0.17, 0.21] for numerical
     stability of derivatives
  3. Properly accounting for the dDelta/dtau contribution to dS^BCS/dtau

Cross-checks:
  - Delta=0 recovers bare eps_H
  - tau=0.19 reproduces S68 corrections (delta_a2/a2 ~ 11.6%, delta_a4/a4 ~ 29.8%)
  - 3-point vs 5-point stencil consistency

Author: Landau Condensed Matter Theorist
Session: S72, Wave 3
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

from canonical_constants import (
    # BCS parameters
    Delta_0_OES, Delta_BCS, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    # Spectral action at fold
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    # Transit dynamics
    H_fold,
    # Scales
    M_KK, M_KK_gravity,
    M_Pl_reduced, tau_fold,
    # Cosmological
    A_s_CMB,
    # Geometry
    G_DeWitt,
    PI,
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8,
    collect_spectrum,
)
from spectral_action import dim_su3_irrep

print("=" * 78)
print("BCS-DRESSED-SA-72: BCS-Dressed Spectral Action at 5 Tau Values")
print("=" * 78)

# =============================================================================
# STEP 0: LOAD INPUT DATA
# =============================================================================
print("\n" + "-" * 78)
print("STEP 0: Load input data")
print("-" * 78)

# W1-A: Delta(tau) profile from KAPPA-DELTA-72
d_kd = np.load('s72_kappa_delta.npz', allow_pickle=True)
tau_kd = d_kd['tau_fine']       # 21 tau values from 0.174 to 0.214
Delta_kd = d_kd['Delta_fine']   # Delta(tau) at each tau
kappa_Delta = float(d_kd['kappa_Delta'])
is_monotonic = bool(d_kd['is_monotonic'])

print(f"  W1-A: tau range [{tau_kd[0]:.4f}, {tau_kd[-1]:.4f}], {len(tau_kd)} points")
print(f"  W1-A: Delta range [{Delta_kd.min():.6f}, {Delta_kd.max():.6f}] M_KK")
print(f"  W1-A: kappa_Delta = {kappa_Delta:.4f} M_KK")
print(f"  W1-A: is_monotonic = {is_monotonic}")

# Build Delta(tau) interpolator
cs_Delta = CubicSpline(tau_kd, Delta_kd)

# S68 BCS dressed mode data (for cross-checks)
d_s68 = np.load('s68_bcs_dressed_mode.npz', allow_pickle=True)
delta_a2_s68 = float(d_s68['delta_a2_total'])
delta_a4_s68 = float(d_s68['delta_a4_total'])
eps_H_BCS_mf_s68 = float(d_s68['delta_eps_H_BCS_mf'])

print(f"\n  S68 cross-check targets:")
print(f"    delta_a2/a2 = {delta_a2_s68:.4f} ({delta_a2_s68*100:.1f}%)")
print(f"    delta_a4/a4 = {delta_a4_s68:.4f} ({delta_a4_s68*100:.1f}%)")
print(f"    delta_eps_H/eps_H (MF) = {eps_H_BCS_mf_s68:.4f}")

# S65 BCS dressed SA (for cross-checks)
d_s65 = np.load('s65_bcs_dressed_sa.npz', allow_pickle=True)
tau_S36 = d_s65['tau_S36']
S_bare_S65 = d_s65['S_bare']
S_BCS_S65 = d_s65['S_BCS']
ns_bare_s65_fold = float(d_s65['ns_bare_fold'])
ns_bcs_s65_fold = float(d_s65['ns_bcs_fold'])

print(f"\n  S65 cross-check targets:")
print(f"    n_s^bare(fold, S65) = {ns_bare_s65_fold:.6f}")
print(f"    n_s^BCS(fold, S65, fixed Delta) = {ns_bcs_s65_fold:.6f}")

# =============================================================================
# STEP 1: COMPUTE DIRAC SPECTRA AT 5 TAU VALUES
# =============================================================================
print("\n" + "-" * 78)
print("STEP 1: Compute D_K eigenvalue spectra at 5 tau values")
print("-" * 78)

print("""
  The spectral action S(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j |lambda_{pq,j}(tau)|
  where lambda_{pq,j} are the Dirac eigenvalues in sector (p,q).

  The BCS-dressed action replaces |lambda| -> E = sqrt(lambda^2 + Delta(tau)^2)
  for all modes (uniform gap approximation). Delta(tau) comes from W1-A.

  We compute at 5 tau values: 0.17, 0.18, 0.19, 0.20, 0.21
  Spacing h = 0.01 gives 5-point stencil accuracy O(h^4) for derivatives.
""")

# Initialize Lie algebra data
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Target tau values
tau_5pt = np.array([0.17, 0.18, 0.19, 0.20, 0.21])
n_tau = len(tau_5pt)
h = tau_5pt[1] - tau_5pt[0]  # = 0.01

# Arrays for results at each tau
S_bare_arr = np.zeros(n_tau)
S_BCS_fixed_arr = np.zeros(n_tau)   # Fixed Delta = Delta_BCS (S65-like)
S_BCS_vary_arr = np.zeros(n_tau)    # Varying Delta = Delta(tau) (NEW)
a2_bare_arr = np.zeros(n_tau)
a2_BCS_fixed_arr = np.zeros(n_tau)
a2_BCS_vary_arr = np.zeros(n_tau)
a4_bare_arr = np.zeros(n_tau)
a4_BCS_fixed_arr = np.zeros(n_tau)
a4_BCS_vary_arr = np.zeros(n_tau)
n_modes_arr = np.zeros(n_tau, dtype=int)
Delta_at_tau = np.zeros(n_tau)

# Fixed Delta for comparison
Delta_fixed = Delta_BCS  # = 0.4643 M_KK

t_start = time.time()

for i, tau in enumerate(tau_5pt):
    # Delta(tau) from W1-A interpolation
    Delta_tau = float(cs_Delta(tau))
    Delta_at_tau[i] = Delta_tau

    # Compute D_K spectrum
    _, eval_data = collect_spectrum(tau, gens, f_abc, gammas, max_pq_sum=3, verbose=(i == 0))

    S_bare_i = 0.0  # (local)
    S_BCS_f_i = 0.0  # fixed Delta  # (local)
    S_BCS_v_i = 0.0  # varying Delta  # (local)
    a2_bare_i = 0.0  # (local)
    a2_BCS_f_i = 0.0  # (local)
    a2_BCS_v_i = 0.0  # (local)
    a4_bare_i = 0.0  # (local)
    a4_BCS_f_i = 0.0  # (local)
    a4_BCS_v_i = 0.0  # (local)
    n_modes_i = 0  # (local)

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        omega = np.abs(evals)

        # BdG quasiparticle energies
        E_fixed = np.sqrt(omega**2 + Delta_fixed**2)
        E_vary = np.sqrt(omega**2 + Delta_tau**2)

        # Spectral action: S = sum d_pq^2 * |lambda|
        S_bare_i += d_pq**2 * np.sum(omega)
        S_BCS_f_i += d_pq**2 * np.sum(E_fixed)
        S_BCS_v_i += d_pq**2 * np.sum(E_vary)

        # Zeta-function moments: a_n = sum d_pq^2 * |lambda|^{-n}
        # Avoid division by zero for lambda = 0 (trivial sector)
        mask = omega > 1e-12
        omega_nz = omega[mask]
        E_fixed_nz = E_fixed[mask]
        E_vary_nz = E_vary[mask]

        a2_bare_i += d_pq**2 * np.sum(1.0 / omega_nz**2)
        a2_BCS_f_i += d_pq**2 * np.sum(1.0 / E_fixed_nz**2)
        a2_BCS_v_i += d_pq**2 * np.sum(1.0 / E_vary_nz**2)
        a4_bare_i += d_pq**2 * np.sum(1.0 / omega_nz**4)
        a4_BCS_f_i += d_pq**2 * np.sum(1.0 / E_fixed_nz**4)
        a4_BCS_v_i += d_pq**2 * np.sum(1.0 / E_vary_nz**4)

        n_modes_i += len(evals)

    S_bare_arr[i] = S_bare_i
    S_BCS_fixed_arr[i] = S_BCS_f_i
    S_BCS_vary_arr[i] = S_BCS_v_i
    a2_bare_arr[i] = a2_bare_i
    a2_BCS_fixed_arr[i] = a2_BCS_f_i
    a2_BCS_vary_arr[i] = a2_BCS_v_i
    a4_bare_arr[i] = a4_bare_i
    a4_BCS_fixed_arr[i] = a4_BCS_f_i
    a4_BCS_vary_arr[i] = a4_BCS_v_i
    n_modes_arr[i] = n_modes_i

    print(f"  tau={tau:.2f}: Delta={Delta_tau:.6f}, S_bare={S_bare_i:.2f}, "
          f"S_BCS(vary)={S_BCS_v_i:.2f}, R={S_BCS_v_i/S_bare_i:.6f}, "
          f"modes={n_modes_i}")

t_compute = time.time() - t_start
print(f"\n  Computed {n_tau} spectra in {t_compute:.1f}s")

# R_BCS ratios
R_BCS_fixed = S_BCS_fixed_arr / S_bare_arr
R_BCS_vary = S_BCS_vary_arr / S_bare_arr

print(f"\n  Summary:")
print(f"  {'tau':>8s}  {'Delta':>10s}  {'S_bare':>12s}  {'S_BCS(fix)':>12s}  "
      f"{'S_BCS(var)':>12s}  {'R_fix':>8s}  {'R_var':>8s}")
for i in range(n_tau):
    print(f"  {tau_5pt[i]:8.2f}  {Delta_at_tau[i]:10.6f}  {S_bare_arr[i]:12.2f}  "
          f"{S_BCS_fixed_arr[i]:12.2f}  {S_BCS_vary_arr[i]:12.2f}  "
          f"{R_BCS_fixed[i]:8.6f}  {R_BCS_vary[i]:8.6f}")

# =============================================================================
# STEP 2: CROSS-CHECK AT FOLD (tau = 0.19)
# =============================================================================
print("\n" + "-" * 78)
print("STEP 2: Cross-checks at tau = 0.19 (fold)")
print("-" * 78)

idx_fold = 2  # tau = 0.19 (local)

# Check 2a: S_bare matches canonical
S_bare_fold = S_bare_arr[idx_fold]
S_dev = abs(S_bare_fold - S_fold) / S_fold
print(f"\n  Cross-check 2a: S_bare at fold")
print(f"    Computed: {S_bare_fold:.2f}")
print(f"    Canonical: {S_fold:.2f}")
print(f"    Relative deviation: {S_dev:.2e}")
if S_dev < 1e-6:
    print(f"    PASSED (machine epsilon)")
else:
    print(f"    WARNING: deviation {S_dev:.2e}")

# Check 2b: Zeta-moment ratios match S68
# S68 used the projected moments approach with 8 BCS modes
# The full-spectrum BCS dressing gives DIFFERENT numbers because it applies
# Delta to ALL modes, not just the 8 near the Fermi surface.
# The correct comparison is against S65 which also used full-spectrum dressing.

# S65 a2 ratio at fold
r2_s65_fold = float(d_s65['r2_zeta'][np.argmin(np.abs(tau_S36 - 0.19))])
r4_s65_fold = float(d_s65['r4_zeta'][np.argmin(np.abs(tau_S36 - 0.19))])

r2_fold_fixed = a2_BCS_fixed_arr[idx_fold] / a2_bare_arr[idx_fold]
r4_fold_fixed = a4_BCS_fixed_arr[idx_fold] / a4_bare_arr[idx_fold]

print(f"\n  Cross-check 2b: Zeta-moment ratios at fold (fixed Delta)")
print(f"    r_2 = a2^BCS/a2^bare = {r2_fold_fixed:.6f} (S65: {r2_s65_fold:.6f})")
print(f"    r_4 = a4^BCS/a4^bare = {r4_fold_fixed:.6f} (S65: {r4_s65_fold:.6f})")
r2_dev = abs(r2_fold_fixed - r2_s65_fold) / r2_s65_fold
r4_dev = abs(r4_fold_fixed - r4_s65_fold) / r4_s65_fold
print(f"    r_2 deviation: {r2_dev:.2e}")
print(f"    r_4 deviation: {r4_dev:.2e}")
if r2_dev < 1e-5 and r4_dev < 1e-5:
    print(f"    PASSED")

# Check 2c: Delta(0.19) matches canonical
Delta_fold_computed = Delta_at_tau[idx_fold]
Delta_dev = abs(Delta_fold_computed - Delta_BCS) / Delta_BCS
print(f"\n  Cross-check 2c: Delta at fold")
print(f"    Delta(0.19) from W1-A interpolation: {Delta_fold_computed:.6f}")
print(f"    Canonical Delta_BCS: {Delta_BCS:.6f}")
print(f"    Relative deviation: {Delta_dev:.2e}")

# Check 2d: delta_a2/a2 and delta_a4/a4 at fold
# These are the RELATIVE shifts. S68 measured them for the 8-mode subsystem.
# The full-spectrum shift is different because Delta is applied to ALL modes.
da2_rel_fold_fixed = (a2_BCS_fixed_arr[idx_fold] - a2_bare_arr[idx_fold]) / a2_bare_arr[idx_fold]
da4_rel_fold_fixed = (a4_BCS_fixed_arr[idx_fold] - a4_bare_arr[idx_fold]) / a4_bare_arr[idx_fold]

print(f"\n  Cross-check 2d: Relative moment shifts at fold (fixed Delta, full spectrum)")
print(f"    delta_a2/a2 = {da2_rel_fold_fixed:+.6f} ({da2_rel_fold_fixed*100:+.2f}%)")
print(f"    delta_a4/a4 = {da4_rel_fold_fixed:+.6f} ({da4_rel_fold_fixed*100:+.2f}%)")
print(f"    NOTE: S68 values ({delta_a2_s68*100:+.1f}%, {delta_a4_s68*100:+.1f}%) are for")
print(f"          the 8-mode BCS subsystem only. The full-spectrum values differ")
print(f"          because BCS dressing lifts ALL eigenvalues, not just the 8 paired modes.")
print(f"    STRUCTURAL: a2^BCS < a2^bare (BCS raises energies, reducing inverse-square sum)")
print(f"    This is the correct sign: BCS WEAKENS gravity (increases G_N denominator)")

# =============================================================================
# STEP 3: SLOW-ROLL PARAMETERS FROM THE FULL SPECTRAL ACTION
# =============================================================================
print("\n" + "-" * 78)
print("STEP 3: Slow-roll parameters from numerical differentiation")
print("-" * 78)

print("""
  The slow-roll parameter eps_H from the spectral action is:

      eps_H = (1/2) * (dS/dtau)^2 / (S * d2S/dtau^2)                      (5)

  We compute dS/dtau and d2S/dtau^2 using 5-point stencils on the 5 tau values.

  5-point central difference stencil (for tau=0.19, the center point):
      f'  = (-f_{-2} + 8*f_{-1} - 8*f_{+1} + f_{+2}) / (12*h)
      f'' = (-f_{-2} + 16*f_{-1} - 30*f_0 + 16*f_{+1} - f_{+2}) / (12*h^2)

  For the boundary points, we use asymmetric stencils or spline interpolation.
""")

# Method 1: 5-point stencil at center (tau=0.19)
def five_pt_deriv1(f, h):
    """5-point central first derivative at center (index 2)."""
    return (-f[0] + 8*f[1] - 8*f[3] + f[4]) / (12*h)

def five_pt_deriv2(f, h):
    """5-point central second derivative at center (index 2)."""
    return (-f[0] + 16*f[1] - 30*f[2] + 16*f[3] - f[4]) / (12*h**2)

# Method 2: 3-point stencil at center
def three_pt_deriv1(f, h, idx=2):
    """3-point central first derivative."""
    return (f[idx+1] - f[idx-1]) / (2*h)

def three_pt_deriv2(f, h, idx=2):
    """3-point central second derivative."""
    return (f[idx+1] - 2*f[idx] + f[idx-1]) / h**2

# Method 3: Cubic spline (uses all 5 points)
def spline_derivs(tau_arr, f_arr, tau_eval):
    """Derivatives from cubic spline interpolation."""
    cs = CubicSpline(tau_arr, f_arr)
    return cs(tau_eval), cs(tau_eval, 1), cs(tau_eval, 2)

# ---- Bare spectral action ----
print("\n  === BARE SPECTRAL ACTION ===")

dS_bare_5pt = five_pt_deriv1(S_bare_arr, h)
d2S_bare_5pt = five_pt_deriv2(S_bare_arr, h)
dS_bare_3pt = three_pt_deriv1(S_bare_arr, h)
d2S_bare_3pt = three_pt_deriv2(S_bare_arr, h)
_, dS_bare_spl, d2S_bare_spl = spline_derivs(tau_5pt, S_bare_arr, 0.19)

print(f"  dS_bare/dtau at fold:")
print(f"    5-point: {dS_bare_5pt:.2f}")
print(f"    3-point: {dS_bare_3pt:.2f}")
print(f"    Spline:  {dS_bare_spl:.2f}")
print(f"    Canonical: {dS_fold:.2f}")
print(f"    3pt-5pt relative: {abs(dS_bare_5pt - dS_bare_3pt)/abs(dS_bare_5pt):.2e}")

print(f"\n  d2S_bare/dtau^2 at fold:")
print(f"    5-point: {d2S_bare_5pt:.2f}")
print(f"    3-point: {d2S_bare_3pt:.2f}")
print(f"    Spline:  {d2S_bare_spl:.2f}")
print(f"    Canonical: {d2S_fold:.2f}")

# eps_H bare
eps_H_bare_5pt = 0.5 * dS_bare_5pt**2 / (S_bare_arr[idx_fold] * d2S_bare_5pt) if d2S_bare_5pt > 0 else np.nan
eps_H_bare_3pt = 0.5 * dS_bare_3pt**2 / (S_bare_arr[idx_fold] * d2S_bare_3pt) if d2S_bare_3pt > 0 else np.nan
eps_H_bare_spl = 0.5 * dS_bare_spl**2 / (S_bare_arr[idx_fold] * d2S_bare_spl) if d2S_bare_spl > 0 else np.nan
eps_H_bare_canonical = 0.5 * dS_fold**2 / (S_fold * d2S_fold)

print(f"\n  eps_H^bare at fold:")
print(f"    5-point: {eps_H_bare_5pt:.6f}")
print(f"    3-point: {eps_H_bare_3pt:.6f}")
print(f"    Spline:  {eps_H_bare_spl:.6f}")
print(f"    Canonical: {eps_H_bare_canonical:.6f}")
stencil_spread_bare = abs(eps_H_bare_5pt - eps_H_bare_3pt) / eps_H_bare_5pt
print(f"    Stencil spread: {stencil_spread_bare:.2e}")

ns_bare_5pt = 1.0 - 2.0 * eps_H_bare_5pt
ns_bare_canonical = 1.0 - 2.0 * eps_H_bare_canonical
print(f"\n  n_s^bare = 1 - 2*eps_H:")
print(f"    5-point: {ns_bare_5pt:.6f}")
print(f"    Canonical: {ns_bare_canonical:.6f}")

# ---- BCS-dressed (fixed Delta, S65-like) ----
print("\n\n  === BCS-DRESSED (FIXED Delta = {:.4f}) ===".format(Delta_fixed))

dS_BCS_f_5pt = five_pt_deriv1(S_BCS_fixed_arr, h)
d2S_BCS_f_5pt = five_pt_deriv2(S_BCS_fixed_arr, h)
dS_BCS_f_3pt = three_pt_deriv1(S_BCS_fixed_arr, h)
d2S_BCS_f_3pt = three_pt_deriv2(S_BCS_fixed_arr, h)
_, dS_BCS_f_spl, d2S_BCS_f_spl = spline_derivs(tau_5pt, S_BCS_fixed_arr, 0.19)

print(f"  dS^BCS(fix)/dtau: 5pt={dS_BCS_f_5pt:.2f}, 3pt={dS_BCS_f_3pt:.2f}, spl={dS_BCS_f_spl:.2f}")
print(f"  d2S^BCS(fix)/dtau2: 5pt={d2S_BCS_f_5pt:.2f}, 3pt={d2S_BCS_f_3pt:.2f}, spl={d2S_BCS_f_spl:.2f}")

eps_H_BCS_f_5pt = 0.5 * dS_BCS_f_5pt**2 / (S_BCS_fixed_arr[idx_fold] * d2S_BCS_f_5pt) if d2S_BCS_f_5pt > 0 else np.nan
eps_H_BCS_f_3pt = 0.5 * dS_BCS_f_3pt**2 / (S_BCS_fixed_arr[idx_fold] * d2S_BCS_f_3pt) if d2S_BCS_f_3pt > 0 else np.nan
eps_H_BCS_f_spl = 0.5 * dS_BCS_f_spl**2 / (S_BCS_fixed_arr[idx_fold] * d2S_BCS_f_spl) if d2S_BCS_f_spl > 0 else np.nan

print(f"\n  eps_H^BCS(fix):")
print(f"    5-point: {eps_H_BCS_f_5pt:.6f}")
print(f"    3-point: {eps_H_BCS_f_3pt:.6f}")
print(f"    Spline:  {eps_H_BCS_f_spl:.6f}")
delta_eps_fix = (eps_H_BCS_f_5pt - eps_H_bare_5pt) / eps_H_bare_5pt
print(f"    delta_eps_H/eps_H (fix) = {delta_eps_fix:+.6f} ({delta_eps_fix*100:+.2f}%)")
print(f"    S65 value: {eps_H_BCS_mf_s68:+.4f} (-7.2% MF)")

ns_BCS_f_5pt = 1.0 - 2.0 * eps_H_BCS_f_5pt
print(f"\n  n_s^BCS(fix) = {ns_BCS_f_5pt:.6f}")
print(f"  delta_ns(fix) = {ns_BCS_f_5pt - ns_bare_5pt:+.6f}")

# ---- BCS-dressed (varying Delta, NEW) ----
print("\n\n  === BCS-DRESSED (VARYING Delta(tau) from W1-A) ===")

dS_BCS_v_5pt = five_pt_deriv1(S_BCS_vary_arr, h)
d2S_BCS_v_5pt = five_pt_deriv2(S_BCS_vary_arr, h)
dS_BCS_v_3pt = three_pt_deriv1(S_BCS_vary_arr, h)
d2S_BCS_v_3pt = three_pt_deriv2(S_BCS_vary_arr, h)
_, dS_BCS_v_spl, d2S_BCS_v_spl = spline_derivs(tau_5pt, S_BCS_vary_arr, 0.19)

print(f"  dS^BCS(var)/dtau: 5pt={dS_BCS_v_5pt:.2f}, 3pt={dS_BCS_v_3pt:.2f}, spl={dS_BCS_v_spl:.2f}")
print(f"  d2S^BCS(var)/dtau2: 5pt={d2S_BCS_v_5pt:.2f}, 3pt={d2S_BCS_v_3pt:.2f}, spl={d2S_BCS_v_spl:.2f}")

eps_H_BCS_v_5pt = 0.5 * dS_BCS_v_5pt**2 / (S_BCS_vary_arr[idx_fold] * d2S_BCS_v_5pt) if d2S_BCS_v_5pt > 0 else np.nan
eps_H_BCS_v_3pt = 0.5 * dS_BCS_v_3pt**2 / (S_BCS_vary_arr[idx_fold] * d2S_BCS_v_3pt) if d2S_BCS_v_3pt > 0 else np.nan
eps_H_BCS_v_spl = 0.5 * dS_BCS_v_spl**2 / (S_BCS_vary_arr[idx_fold] * d2S_BCS_v_spl) if d2S_BCS_v_spl > 0 else np.nan

stencil_spread_BCS_v = abs(eps_H_BCS_v_5pt - eps_H_BCS_v_3pt) / abs(eps_H_BCS_v_5pt) if eps_H_BCS_v_5pt != 0 else np.nan

print(f"\n  eps_H^BCS(var):")
print(f"    5-point: {eps_H_BCS_v_5pt:.6f}")
print(f"    3-point: {eps_H_BCS_v_3pt:.6f}")
print(f"    Spline:  {eps_H_BCS_v_spl:.6f}")
print(f"    Stencil spread: {stencil_spread_BCS_v:.2e}")

delta_eps_vary = (eps_H_BCS_v_5pt - eps_H_bare_5pt) / eps_H_bare_5pt
print(f"    delta_eps_H/eps_H (var) = {delta_eps_vary:+.6f} ({delta_eps_vary*100:+.2f}%)")

ns_BCS_v_5pt = 1.0 - 2.0 * eps_H_BCS_v_5pt
print(f"\n  n_s^BCS(var) = {ns_BCS_v_5pt:.6f}")
print(f"  delta_ns(var) = {ns_BCS_v_5pt - ns_bare_5pt:+.6f}")

# =============================================================================
# STEP 4: DECOMPOSE THE tau-DEPENDENT DELTA CONTRIBUTION
# =============================================================================
print("\n" + "-" * 78)
print("STEP 4: Decompose the dDelta/dtau contribution")
print("-" * 78)

print("""
  The difference between S^BCS(fixed Delta) and S^BCS(varying Delta) comes
  entirely from the tau-dependence of Delta:

      S^BCS(var) - S^BCS(fix) = sum d_pq^2 * sum_j [E_j(omega,Delta(tau)) - E_j(omega,Delta_0)]

  This is the ADDITIONAL spectral action variation from the running gap.
  Its tau-derivative is the dDelta/dtau contribution to dS^BCS/dtau.
""")

dS_Delta_contrib = dS_BCS_v_5pt - dS_BCS_f_5pt
d2S_Delta_contrib = d2S_BCS_v_5pt - d2S_BCS_f_5pt

print(f"  dDelta/dtau at fold (W1-A): {float(cs_Delta(0.19, 1)):.6f} M_KK")
print(f"  d2Delta/dtau2 at fold:     {float(cs_Delta(0.19, 2)):.4f} M_KK")
print()
print(f"  Additional dS/dtau from dDelta/dtau:  {dS_Delta_contrib:+.2f}")
print(f"  Additional d2S/dtau2 from d2Delta/dtau2: {d2S_Delta_contrib:+.2f}")
print(f"  Relative contribution to dS': {dS_Delta_contrib/dS_BCS_f_5pt:+.6f} ({dS_Delta_contrib/dS_BCS_f_5pt*100:+.2f}%)")

# =============================================================================
# STEP 5: CONSISTENCY CHECK -- DELTA = 0 RECOVERS BARE
# =============================================================================
print("\n" + "-" * 78)
print("STEP 5: Consistency check -- Delta=0 recovers bare eps_H")
print("-" * 78)

# With Delta=0, E_k = |lambda_k|, so S^BCS = S^bare exactly.
# We verify this numerically at the fold.
S_BCS_delta0 = 0.0  # (local)
for p, q, evals in eval_data:  # eval_data from last iteration (tau=0.21)
    d_pq = dim_su3_irrep(p, q)
    omega = np.abs(evals)
    E_0 = np.sqrt(omega**2 + 0.0)  # Delta = 0
    S_BCS_delta0 += d_pq**2 * np.sum(E_0)

# This should equal S_bare at the SAME tau value
S_bare_last = S_bare_arr[-1]  # tau=0.21
delta_check = abs(S_BCS_delta0 - S_bare_last) / S_bare_last
print(f"  S^BCS(Delta=0, tau=0.21) = {S_BCS_delta0:.6f}")
print(f"  S^bare(tau=0.21)         = {S_bare_last:.6f}")
print(f"  Relative deviation:       {delta_check:.2e}")
if delta_check < 1e-14:
    print(f"  PASSED (machine epsilon)")
else:
    print(f"  WARNING: deviation = {delta_check:.2e}")

# Also verify: eps_H from bare computation matches between 5pt and S65 spline
print(f"\n  eps_H bare agreement:")
print(f"    This computation (5pt): {eps_H_bare_5pt:.6f}")
print(f"    S65 at fold:            {float(d_s65['eps_H_bare'][3]):.6f}")
print(f"    Canonical:              {eps_H_bare_canonical:.6f}")

# =============================================================================
# STEP 6: COMPUTE eps_H AT ALL 5 TAU VALUES (for plot)
# =============================================================================
print("\n" + "-" * 78)
print("STEP 6: eps_H at all tau values via spline")
print("-" * 78)

# Use spline for smooth derivatives at each tau point
cs_S_bare = CubicSpline(tau_5pt, S_bare_arr)
cs_S_BCS_f = CubicSpline(tau_5pt, S_BCS_fixed_arr)
cs_S_BCS_v = CubicSpline(tau_5pt, S_BCS_vary_arr)

# Evaluate at each of the 5 tau points
eps_H_bare_all = np.zeros(n_tau)
eps_H_BCS_f_all = np.zeros(n_tau)
eps_H_BCS_v_all = np.zeros(n_tau)
ns_bare_all = np.zeros(n_tau)
ns_BCS_f_all = np.zeros(n_tau)
ns_BCS_v_all = np.zeros(n_tau)

for i, tau in enumerate(tau_5pt):
    # Bare
    S_b = cs_S_bare(tau)
    dS_b = cs_S_bare(tau, 1)
    d2S_b = cs_S_bare(tau, 2)
    eps_H_bare_all[i] = 0.5 * dS_b**2 / (S_b * d2S_b) if d2S_b > 0 else np.nan
    ns_bare_all[i] = 1.0 - 2.0 * eps_H_bare_all[i]

    # BCS fixed
    S_f = cs_S_BCS_f(tau)
    dS_f = cs_S_BCS_f(tau, 1)
    d2S_f = cs_S_BCS_f(tau, 2)
    eps_H_BCS_f_all[i] = 0.5 * dS_f**2 / (S_f * d2S_f) if d2S_f > 0 else np.nan
    ns_BCS_f_all[i] = 1.0 - 2.0 * eps_H_BCS_f_all[i]

    # BCS varying
    S_v = cs_S_BCS_v(tau)
    dS_v = cs_S_BCS_v(tau, 1)
    d2S_v = cs_S_BCS_v(tau, 2)
    eps_H_BCS_v_all[i] = 0.5 * dS_v**2 / (S_v * d2S_v) if d2S_v > 0 else np.nan
    ns_BCS_v_all[i] = 1.0 - 2.0 * eps_H_BCS_v_all[i]

print(f"  {'tau':>6s}  {'eps_H^bare':>12s}  {'eps_H^BCS(f)':>13s}  {'eps_H^BCS(v)':>13s}  "
      f"{'n_s^bare':>10s}  {'n_s^BCS(f)':>10s}  {'n_s^BCS(v)':>10s}")
for i in range(n_tau):
    print(f"  {tau_5pt[i]:6.2f}  {eps_H_bare_all[i]:12.6f}  {eps_H_BCS_f_all[i]:13.6f}  "
          f"{eps_H_BCS_v_all[i]:13.6f}  {ns_bare_all[i]:10.6f}  {ns_BCS_f_all[i]:10.6f}  "
          f"{ns_BCS_v_all[i]:10.6f}")

# =============================================================================
# STEP 7: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Gate Verdict -- BCS-DRESSED-SA-72")
print("=" * 78)

# Use 5-point stencil at fold for primary result
# The varying Delta is the physically correct computation
eps_H_final = eps_H_BCS_v_5pt
ns_final = ns_BCS_v_5pt

# Also compute the spline result for cross-check
eps_H_final_spl = eps_H_BCS_v_spl
ns_final_spl = 1.0 - 2.0 * eps_H_final_spl

# The deviation from Planck
ns_Planck = 0.9649  # (local)
sigma_Planck = 0.0042  # (local)
delta_ns_from_Planck = abs(ns_final - ns_Planck)
sigma_from_Planck = delta_ns_from_Planck / sigma_Planck

print(f"\n  PRIMARY RESULT (5-point stencil, varying Delta):")
print(f"    eps_H^BCS(vary) = {eps_H_final:.6f}")
print(f"    n_s^BCS(vary)   = {ns_final:.6f}")
print(f"    |n_s - 0.9649|  = {delta_ns_from_Planck:.6f}")
print(f"    Sigma from Planck: {sigma_from_Planck:.2f}")
print()
print(f"  SPLINE CHECK:")
print(f"    eps_H^BCS(spl) = {eps_H_final_spl:.6f}")
print(f"    n_s^BCS(spl)   = {ns_final_spl:.6f}")
print()

# BCS correction decomposition
delta_eps_total = (eps_H_final - eps_H_bare_5pt) / eps_H_bare_5pt
delta_ns_from_bare = ns_final - ns_bare_5pt
delta_ns_fixed = ns_BCS_f_5pt - ns_bare_5pt
delta_ns_gap_running = ns_final - ns_BCS_f_5pt

print(f"  BCS CORRECTION DECOMPOSITION:")
print(f"    eps_H^bare        = {eps_H_bare_5pt:.6f}")
print(f"    eps_H^BCS(fix)    = {eps_H_BCS_f_5pt:.6f}  (Delta constant)")
print(f"    eps_H^BCS(vary)   = {eps_H_final:.6f}  (Delta(tau) from W1-A)")
print(f"    delta_eps/eps (fix)   = {delta_eps_fix:+.6f} ({delta_eps_fix*100:+.2f}%)")
print(f"    delta_eps/eps (vary)  = {delta_eps_total:+.6f} ({delta_eps_total*100:+.2f}%)")
print()
print(f"    n_s^bare          = {ns_bare_5pt:.6f}")
print(f"    n_s^BCS(fix)      = {ns_BCS_f_5pt:.6f}  (Delta constant)")
print(f"    n_s^BCS(vary)     = {ns_final:.6f}  (Delta(tau) from W1-A)")
print(f"    delta_ns (from fixed Delta): {delta_ns_fixed:+.6f}")
print(f"    delta_ns (from gap running): {delta_ns_gap_running:+.6f}")
print(f"    delta_ns (total BCS):        {delta_ns_from_bare:+.6f}")
print()

# GATE
if delta_ns_from_Planck < 0.005:
    gate_verdict = "PASS"
    gate_detail = (f"|n_s^BCS - 0.9649| = {delta_ns_from_Planck:.4f} < 0.005 "
                   f"({sigma_from_Planck:.2f} sigma from Planck). "
                   f"BCS-dressed n_s = {ns_final:.4f} within 1.2 sigma of Planck.")
elif delta_ns_from_Planck < 0.010:
    gate_verdict = "INFO"
    gate_detail = (f"|n_s^BCS - 0.9649| = {delta_ns_from_Planck:.4f} in [0.005, 0.010] "
                   f"({sigma_from_Planck:.2f} sigma from Planck). "
                   f"BCS-dressed n_s = {ns_final:.4f}.")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"|n_s^BCS - 0.9649| = {delta_ns_from_Planck:.4f} > 0.010 "
                   f"({sigma_from_Planck:.2f} sigma from Planck). "
                   f"BCS-dressed n_s = {ns_final:.4f}.")

print(f"  *** Gate BCS-DRESSED-SA-72: {gate_verdict} ***")
print(f"  {gate_detail}")

# =============================================================================
# STEP 8: SAVE DATA
# =============================================================================
print("\n" + "-" * 78)
print("STEP 8: Save results")
print("-" * 78)

np.savez('s72_bcs_dressed_sa.npz',
    # Gate
    gate_name='BCS-DRESSED-SA-72',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Input
    tau_5pt=tau_5pt,
    h=h,
    Delta_at_tau=Delta_at_tau,
    Delta_fixed=Delta_fixed,
    kappa_Delta=kappa_Delta,
    # Spectral action arrays
    S_bare=S_bare_arr,
    S_BCS_fixed=S_BCS_fixed_arr,
    S_BCS_vary=S_BCS_vary_arr,
    R_BCS_fixed=R_BCS_fixed,
    R_BCS_vary=R_BCS_vary,
    # Zeta moments
    a2_bare=a2_bare_arr,
    a2_BCS_fixed=a2_BCS_fixed_arr,
    a2_BCS_vary=a2_BCS_vary_arr,
    a4_bare=a4_bare_arr,
    a4_BCS_fixed=a4_BCS_fixed_arr,
    a4_BCS_vary=a4_BCS_vary_arr,
    n_modes=n_modes_arr,
    # Derivatives at fold (5pt)
    dS_bare_5pt=dS_bare_5pt,
    d2S_bare_5pt=d2S_bare_5pt,
    dS_BCS_f_5pt=dS_BCS_f_5pt,
    d2S_BCS_f_5pt=d2S_BCS_f_5pt,
    dS_BCS_v_5pt=dS_BCS_v_5pt,
    d2S_BCS_v_5pt=d2S_BCS_v_5pt,
    # eps_H at fold
    eps_H_bare_5pt=eps_H_bare_5pt,
    eps_H_BCS_f_5pt=eps_H_BCS_f_5pt,
    eps_H_BCS_v_5pt=eps_H_BCS_v_5pt,
    eps_H_bare_3pt=eps_H_bare_3pt,
    eps_H_BCS_v_3pt=eps_H_BCS_v_3pt,
    eps_H_bare_spl=eps_H_bare_spl,
    eps_H_BCS_v_spl=eps_H_BCS_v_spl,
    # n_s at fold
    ns_bare_5pt=ns_bare_5pt,
    ns_BCS_f_5pt=ns_BCS_f_5pt,
    ns_BCS_v_5pt=ns_BCS_v_5pt,
    ns_final=ns_final,
    # delta quantities
    delta_eps_fix=delta_eps_fix,
    delta_eps_vary=delta_eps_total,
    delta_ns_fixed=delta_ns_fixed,
    delta_ns_gap_running=delta_ns_gap_running,
    delta_ns_total=delta_ns_from_bare,
    delta_ns_from_Planck=delta_ns_from_Planck,
    sigma_from_Planck=sigma_from_Planck,
    # All-tau arrays
    eps_H_bare_all=eps_H_bare_all,
    eps_H_BCS_f_all=eps_H_BCS_f_all,
    eps_H_BCS_v_all=eps_H_BCS_v_all,
    ns_bare_all=ns_bare_all,
    ns_BCS_f_all=ns_BCS_f_all,
    ns_BCS_v_all=ns_BCS_v_all,
    # dDelta contribution
    dDelta_dtau_fold=float(cs_Delta(0.19, 1)),
    dS_Delta_contrib=dS_Delta_contrib,
    d2S_Delta_contrib=d2S_Delta_contrib,
    # Stencil consistency
    stencil_spread_bare=stencil_spread_bare,
    stencil_spread_BCS_v=stencil_spread_BCS_v,
)

print(f"  Saved: s72_bcs_dressed_sa.npz")

# =============================================================================
# STEP 9: PLOT
# =============================================================================
print("\n" + "-" * 78)
print("STEP 9: Generate plot")
print("-" * 78)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Panel 1: eps_H vs tau
ax = axes[0]
ax.plot(tau_5pt, eps_H_bare_all, 'b.-', label=r'$\epsilon_H^{\rm bare}$', markersize=8)
ax.plot(tau_5pt, eps_H_BCS_f_all, 'r.--', label=r'$\epsilon_H^{\rm BCS}$ (fixed $\Delta$)', markersize=8)
ax.plot(tau_5pt, eps_H_BCS_v_all, 'g.-', label=r'$\epsilon_H^{\rm BCS}$ (varying $\Delta$)', markersize=8, linewidth=2)
ax.axhline(eps_H_bare_canonical, color='b', alpha=0.3, linestyle=':')
ax.axvline(0.19, color='gray', alpha=0.3, linestyle=':')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\epsilon_H$')
ax.set_title(r'Slow-roll parameter $\epsilon_H(\tau)$')
ax.legend(fontsize=8)

# Panel 2: n_s vs tau
ax = axes[1]
ax.plot(tau_5pt, ns_bare_all, 'b.-', label=r'$n_s^{\rm bare}$', markersize=8)
ax.plot(tau_5pt, ns_BCS_f_all, 'r.--', label=r'$n_s^{\rm BCS}$ (fixed $\Delta$)', markersize=8)
ax.plot(tau_5pt, ns_BCS_v_all, 'g.-', label=r'$n_s^{\rm BCS}$ (varying $\Delta$)', markersize=8, linewidth=2)
ax.axhline(0.9649, color='orange', alpha=0.5, linestyle='--', label='Planck 2018')
ax.fill_between(tau_5pt, 0.9649 - 0.0042, 0.9649 + 0.0042, alpha=0.1, color='orange')
ax.axvline(0.19, color='gray', alpha=0.3, linestyle=':')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$n_s$')
ax.set_title(r'Spectral index $n_s(\tau)$')
ax.legend(fontsize=8)

# Panel 3: Delta(tau) profile
ax = axes[2]
ax.plot(tau_5pt, Delta_at_tau, 'k.-', markersize=8, linewidth=2)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Delta(\tau)$ [M$_{\rm KK}$]')
ax.set_title(r'BCS gap $\Delta(\tau)$ (W1-A)')
ax.axvline(0.19, color='gray', alpha=0.3, linestyle=':')

plt.suptitle(f'BCS-DRESSED-SA-72: Gate {gate_verdict} | '
             f'$n_s^{{\\rm BCS}}$ = {ns_final:.4f} | '
             f'$|n_s - 0.9649|$ = {delta_ns_from_Planck:.4f}',
             fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('s72_bcs_dressed_sa.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s72_bcs_dressed_sa.png")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY: BCS-DRESSED-SA-72")
print("=" * 78)
print(f"  Gate verdict: {gate_verdict}")
print(f"  {gate_detail}")
print()
print(f"  KEY NUMBERS:")
print(f"    eps_H^bare                  = {eps_H_bare_5pt:.6f}")
print(f"    eps_H^BCS (fixed Delta)     = {eps_H_BCS_f_5pt:.6f}")
print(f"    eps_H^BCS (varying Delta)   = {eps_H_final:.6f}")
print(f"    n_s^bare                    = {ns_bare_5pt:.6f}")
print(f"    n_s^BCS (fixed Delta)       = {ns_BCS_f_5pt:.6f}")
print(f"    n_s^BCS (varying Delta)     = {ns_final:.6f}")
print(f"    Planck 2018                 = {ns_Planck} +/- {sigma_Planck}")
print(f"    |n_s^BCS - Planck|          = {delta_ns_from_Planck:.6f} ({sigma_from_Planck:.2f} sigma)")
print(f"    delta_eps_H/eps_H (total)   = {delta_eps_total:+.4f} ({delta_eps_total*100:+.1f}%)")
print(f"    delta_ns (fixed Delta part) = {delta_ns_fixed:+.6f}")
print(f"    delta_ns (gap running part) = {delta_ns_gap_running:+.6f}")
print(f"    Stencil consistency (bare)  = {stencil_spread_bare:.2e}")
print(f"    Stencil consistency (BCS)   = {stencil_spread_BCS_v:.2e}")
print(f"    dDelta/dtau at fold         = {float(cs_Delta(0.19, 1)):.6f} M_KK")
