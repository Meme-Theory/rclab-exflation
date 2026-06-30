#!/usr/bin/env python3
"""
S80 W1-5: CHI-N-WARD-DUAL (rank-2 fallback spectral-measure functional)
========================================================================

GATE [VERIFY elevated]: S80-CHI-N-WARD-DUAL
HYPOTHESIS: The rank-2 dual functional chi_N(tau) * W(tau) is constant
  under tau-variation (Ward identity, substrate U(1)_EM gauge structure).

PRE-REGISTERED:
  - Compute chi_N(tau) and W(tau) at tau in {0.15, 0.19, 0.25} (coarse).
  - Fine grid tau in {0.10, 0.12, ..., 0.28} for van-Hove check.
  - Test: chi_N * W independence within 5% (PASS), [5%, 20%] (INFO),
          >20% (FAIL).

SECONDARY: If chi_N(tau) alone exhibits van-Hove-like concentration at
  tau_fold = 0.190 (fine-grid argmax within Delta_tau <= 0.02 of 0.190),
  it qualifies as a candidate for the §VII.I Fold Transit Event 4th
  functional (replacing the monotone-profile FOLD-INST-GRADIENT that
  CONVERGENT-FAILED in W1-3).

Agent: gen-physicist (S80, compute mode)
Classification: GEOMETRIC
  - chi_N is the alternating sum of Laplace moments of D_K spectrum
    (Euler-characteristic analog in spectral-measure space).
  - W(tau) is the Ward functional for U(1)_EM, built from Chamseddine-Connes
    Seeley-DeWitt gauge-sector moments.
  - Both are D_K spectral-triple invariants — properties of the fiber's
    eigenvalue spectrum, NOT cosmological observables.

Substrate framing: chi_N is a topological invariant of the fiber's
  eigenvalue spectrum under Jensen deformation. W encodes the Ward
  identity constraint on the gauge-sector of the spectral action.
  Their product is predicted constant if the U(1)_EM anomaly cancels
  against the Jensen-deformation of the moment tower.

--------------------------------------------------------------------
SUBSTITUTION CHAIN ([VERIFY] — mandatory per math-scripts.md)
--------------------------------------------------------------------

Step 1 — chi_N definition:
  Take the N=4 Chamseddine-Connes Laplace-moment tower
    mu_0(tau) = a_0(tau)            [volume / mode count]
    mu_1(tau) = a_2(tau)            [scalar curvature]
    mu_2(tau) = a_4(tau)            [Gauss-Bonnet / gauge kinetic]
  where a_k is the S73B half-spectrum convention:
    a_k(tau) = 0.5 * sum_{n: |lam_n| > cutoff} d_n * |lam_n|^{-k}

  Euler-characteristic analog (alternating sum):
    chi_N(tau) = sum_{k=0}^{2} (-1)^k * mu_k(tau)
               = a_0(tau) - a_2(tau) + a_4(tau)

Step 2 — W(tau) definition (Ward functional, U(1)_EM gauge sector):
  Per Chamseddine-Connes 1996 eq 2.11, the U(1)_EM gauge kinetic term
  emerges from the a_4 moment with coupling g_U1^2. The Ward functional
  balancing gauge-sector against scalar-curvature is:
    W(tau) = g_U1(tau)^2 * sqrt(a_4(tau) / a_2(tau))
  where g_U1(tau)^2 = g_U1_fold * exp(-2 * (tau - tau_fold))
  (canonical identity S22a, g1/g2 = e^{-2*tau}).

  Using the framework canonical value g_U1_fold = g_U1_fold_canonical.

Step 3 — Product (Ward-duality prediction):
  Pi(tau) = chi_N(tau) * W(tau)
         = [a_0(tau) - a_2(tau) + a_4(tau)]
            * g_U1(tau)^2 * sqrt(a_4(tau) / a_2(tau))

Step 4 — Ward-duality hypothesis:
  Pi(tau) = constant  <=>  dPi/dtau = 0  identically

Step 5 — Test:
  Compute max(Pi)/min(Pi) - 1 (percent variation) over tau grid.
  Direction of variation is OUTPUT, not input claim.

--------------------------------------------------------------------
IMPORTANT STRUCTURAL CAVEAT (from knowledge MCP trace)
--------------------------------------------------------------------
S22c identified: chi(SU(3)) = 0 for compact Lie group (structural).
The Gauss-Bonnet Euler characteristic of the SU(3) group manifold itself
vanishes. HOWEVER, chi_N as defined here is NOT the group-manifold Euler
characteristic — it is the alternating sum of SPECTRAL-MEASURE moments
of the Dirac operator D_K. These moments depend on tau via Jensen
deformation of the metric, so chi_N(tau) is a non-trivial function
even though chi(SU(3), round) = 0.

The S22c result (chi(SU(3))=0) is a statement about the 8-form integral
of the Lagrangian L_E in Gauss-Bonnet form. chi_N defined here is a
1-parameter family of spectral moments, NOT a topological invariant of
the manifold. It is a "spectral Euler characteristic" in the sense of
McKean-Singer applied to truncated Laplace-moment towers.
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

from canonical_constants import (
    tau_fold,
    a0_fold,
    a2_fold,
    a4_fold,
    g_U1_fold,
)

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    collect_spectrum,
    build_cliff8,
)


print("=" * 78)
print("S80 W1-5: CHI-N-WARD-DUAL (rank-2 spectral-measure functional)")
print("=" * 78)
print(f"  Canonical anchors:")
print(f"    tau_fold      = {tau_fold}")
print(f"    a0_fold       = {a0_fold}")
print(f"    a2_fold       = {a2_fold}")
print(f"    a4_fold       = {a4_fold}")
print(f"    g_U1_fold^2   = {g_U1_fold}")
print()


# ---------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------

# Coarse gate grid (pre-registered)
TAU_COARSE = np.array([0.15, 0.19, 0.25])  # (local)

# Fine grid for van-Hove concentration check (secondary deliverable)
TAU_FINE = np.arange(0.10, 0.281, 0.02)  # (local) 10 points: 0.10..0.28

# Union for computation (unique, sorted)
TAU_ALL = np.unique(np.concatenate([TAU_COARSE, TAU_FINE, [tau_fold]]))  # (local)

# Peter-Weyl truncation (canonical L_max=3, same as R_1 canonical)
MAX_PQ_SUM = 3  # (local) L_max=3 — S73B / S74 / S77 canonical
EVAL_CUTOFF = 0.01  # (local) near-zero eigenvalue exclusion — same as S77 canonical

# Gate thresholds
PASS_THRESH = 5.0   # (local) percent variation threshold (PASS)
INFO_THRESH = 20.0  # (local) percent variation threshold (INFO)
VAN_HOVE_DTAU = 0.02  # (local) tau_fold proximity for van-Hove qualification

print(f"  Configuration:")
print(f"    L_max (max_pq_sum)    = {MAX_PQ_SUM}")
print(f"    Eigenvalue cutoff     = {EVAL_CUTOFF}")
print(f"    Coarse tau grid       = {TAU_COARSE}")
print(f"    Fine tau grid         = {TAU_FINE}")
print(f"    Union grid size       = {len(TAU_ALL)}")
print(f"    PASS threshold        = {PASS_THRESH}% variation")
print(f"    INFO threshold        = {INFO_THRESH}% variation")
print()


# ---------------------------------------------------------------
# ALGEBRAIC INFRASTRUCTURE (once)
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 1: BUILD SU(3) INFRASTRUCTURE")
print("=" * 78)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
print(f"  8 su(3) anti-Hermitian generators, structure constants, Clifford-8 generators built.")
print()


# ---------------------------------------------------------------
# SPECTRAL MOMENT COMPUTATION FUNCTION
# ---------------------------------------------------------------

def compute_moments_at_tau(tau_val):
    """
    Compute a_0, a_2, a_4 in S73B half-spectrum convention at given tau.
    Returns dict with a0, a2, a4, n_evals, lam_min, lam_max.
    """
    all_evals, eval_data = collect_spectrum(
        tau_val, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=False
    )

    abs_vals = []  # (local)
    mults = []  # (local)
    for ev, mult in all_evals:
        aev = abs(ev)  # (local)
        if aev > EVAL_CUTOFF:
            abs_vals.append(aev)
            mults.append(mult)

    abs_vals = np.array(abs_vals)  # (local)
    mults = np.array(mults, dtype=np.float64)  # (local)

    # S73B half-spectrum convention: factor 0.5
    a0 = 0.5 * float(np.sum(mults))  # (local)
    a2 = 0.5 * float(np.sum(mults / abs_vals**2))  # (local)
    a4 = 0.5 * float(np.sum(mults / abs_vals**4))  # (local)

    return {
        'tau': tau_val,
        'a0': a0,
        'a2': a2,
        'a4': a4,
        'n_evals': len(abs_vals),
        'lam_min': float(np.min(abs_vals)),
        'lam_max': float(np.max(abs_vals)),
    }


# ---------------------------------------------------------------
# TAU SWEEP: compute (a_0, a_2, a_4) at each tau
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 2: SWEEP TAU -- compute spectral moments a_0, a_2, a_4")
print("=" * 78)

results = []  # (local)
t_start = time.time()  # (local)

for i, tau_val in enumerate(TAU_ALL):
    t0 = time.time()  # (local)
    r = compute_moments_at_tau(tau_val)  # (local)
    dt_step = time.time() - t0  # (local)
    results.append(r)
    print(f"  [{i+1:2d}/{len(TAU_ALL)}] tau={tau_val:.4f}: "
          f"a0={r['a0']:.1f}, a2={r['a2']:.3f}, a4={r['a4']:.4f}, "
          f"n_evals={r['n_evals']}, dt={dt_step:.1f}s")

t_total = time.time() - t_start  # (local)
print(f"\n  Total sweep time: {t_total:.1f}s")
print()


# ---------------------------------------------------------------
# CANONICAL ANCHOR VERIFICATION
# ---------------------------------------------------------------
# At tau=0.19, we must reproduce the canonical a0_fold, a2_fold, a4_fold
# within numerical tolerance (else L_max/cutoff conventions have drifted).

tau_arr_full = np.array([r['tau'] for r in results])  # (local)
a0_arr = np.array([r['a0'] for r in results])  # (local)
a2_arr = np.array([r['a2'] for r in results])  # (local)
a4_arr = np.array([r['a4'] for r in results])  # (local)

idx_fold = int(np.argmin(np.abs(tau_arr_full - tau_fold)))  # (local)
a0_check = a0_arr[idx_fold]  # (local)
a2_check = a2_arr[idx_fold]  # (local)
a4_check = a4_arr[idx_fold]  # (local)

print("=" * 78)
print("CANONICAL ANCHOR VERIFICATION (tau=0.19)")
print("=" * 78)
print(f"  a_0 computed = {a0_check:.3f} | canonical a0_fold = {a0_fold:.3f} | "
      f"drift = {100*(a0_check/a0_fold - 1):.3f}%")
print(f"  a_2 computed = {a2_check:.3f} | canonical a2_fold = {a2_fold:.3f} | "
      f"drift = {100*(a2_check/a2_fold - 1):.3f}%")
print(f"  a_4 computed = {a4_check:.3f} | canonical a4_fold = {a4_fold:.3f} | "
      f"drift = {100*(a4_check/a4_fold - 1):.3f}%")
print()


# ---------------------------------------------------------------
# STEP 3: FORM chi_N(tau) (Euler-characteristic analog)
# ---------------------------------------------------------------
# chi_N(tau) = mu_0 - mu_1 + mu_2 = a_0 - a_2 + a_4
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 3: FORM chi_N(tau) = a_0(tau) - a_2(tau) + a_4(tau)")
print("=" * 78)

chi_N_arr = a0_arr - a2_arr + a4_arr  # (local)
chi_N_fold = chi_N_arr[idx_fold]  # (local)

print(f"  chi_N at tau_fold = {chi_N_fold:.4f}")
print()
print(f"  {'tau':>6s} | {'a_0':>10s} | {'a_2':>10s} | {'a_4':>10s} | {'chi_N':>12s}")
print(f"  " + "-" * 62)
for i in range(len(tau_arr_full)):
    mark = "  <-- fold" if abs(tau_arr_full[i] - tau_fold) < 1e-4 else ""
    print(f"  {tau_arr_full[i]:>6.4f} | {a0_arr[i]:>10.3f} | {a2_arr[i]:>10.3f} | "
          f"{a4_arr[i]:>10.4f} | {chi_N_arr[i]:>12.4f}{mark}")
print()


# ---------------------------------------------------------------
# STEP 4: FORM W(tau) (Ward functional, U(1)_EM gauge sector)
# ---------------------------------------------------------------
# W(tau) = g_U1(tau)^2 * sqrt(a_4(tau)/a_2(tau))
# g_U1(tau)^2 = g_U1_fold * exp(-2*(tau - tau_fold))
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 4: FORM W(tau) = g_U1(tau)^2 * sqrt(a_4/a_2)")
print("=" * 78)

g_U1_sq_arr = g_U1_fold * np.exp(-2.0 * (tau_arr_full - tau_fold))  # (local)
sqrt_ratio = np.sqrt(a4_arr / a2_arr)  # (local)
W_arr = g_U1_sq_arr * sqrt_ratio  # (local)
W_fold = W_arr[idx_fold]  # (local)

print(f"  W at tau_fold = {W_fold:.6f}")
print()
print(f"  {'tau':>6s} | {'g_U1^2':>10s} | {'sqrt(a4/a2)':>14s} | {'W(tau)':>12s}")
print(f"  " + "-" * 52)
for i in range(len(tau_arr_full)):
    mark = "  <-- fold" if abs(tau_arr_full[i] - tau_fold) < 1e-4 else ""
    print(f"  {tau_arr_full[i]:>6.4f} | {g_U1_sq_arr[i]:>10.4f} | "
          f"{sqrt_ratio[i]:>14.6f} | {W_arr[i]:>12.6f}{mark}")
print()


# ---------------------------------------------------------------
# STEP 5: FORM PRODUCT Pi(tau) = chi_N(tau) * W(tau)
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 5: FORM PRODUCT Pi(tau) = chi_N(tau) * W(tau)")
print("=" * 78)

Pi_arr = chi_N_arr * W_arr  # (local)
Pi_fold = Pi_arr[idx_fold]  # (local)

print(f"  Pi at tau_fold = {Pi_fold:.4f}")
print()


# ---------------------------------------------------------------
# STEP 6: COARSE-GRID GATE TEST (PRE-REGISTERED)
# ---------------------------------------------------------------
# Compute max-min variation across coarse grid {0.15, 0.19, 0.25}
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 6: COARSE-GRID GATE TEST (tau in {0.15, 0.19, 0.25})")
print("=" * 78)

# Index the coarse grid within the full results
coarse_idx = []  # (local)
for t_c in TAU_COARSE:
    coarse_idx.append(int(np.argmin(np.abs(tau_arr_full - t_c))))
coarse_idx = np.array(coarse_idx)  # (local)

tau_coarse_actual = tau_arr_full[coarse_idx]  # (local)
chi_N_coarse = chi_N_arr[coarse_idx]  # (local)
W_coarse = W_arr[coarse_idx]  # (local)
Pi_coarse = Pi_arr[coarse_idx]  # (local)

print(f"\n  Coarse-grid values:")
print(f"  {'tau':>6s} | {'chi_N':>12s} | {'W':>12s} | {'Pi=chi_N*W':>14s}")
print(f"  " + "-" * 52)
for i in range(len(TAU_COARSE)):
    print(f"  {tau_coarse_actual[i]:>6.4f} | {chi_N_coarse[i]:>12.4f} | "
          f"{W_coarse[i]:>12.6f} | {Pi_coarse[i]:>14.4f}")

Pi_max_coarse = float(np.max(Pi_coarse))  # (local)
Pi_min_coarse = float(np.min(Pi_coarse))  # (local)
Pi_mean_coarse = float(np.mean(Pi_coarse))  # (local)
pct_var_coarse = 100.0 * (Pi_max_coarse - Pi_min_coarse) / Pi_mean_coarse  # (local)

print(f"\n  COARSE GATE STATISTICS:")
print(f"    max(Pi) = {Pi_max_coarse:.4f}")
print(f"    min(Pi) = {Pi_min_coarse:.4f}")
print(f"    mean    = {Pi_mean_coarse:.4f}")
print(f"    variation = (max-min)/mean = {pct_var_coarse:.3f}%")
print()

# GATE VERDICT
if pct_var_coarse < PASS_THRESH:
    verdict_coarse = "PASS"
    verdict_explanation = (
        f"chi_N * W constant within {PASS_THRESH}% "
        f"({pct_var_coarse:.3f}%) -- Ward duality confirmed"
    )  # (local)
elif pct_var_coarse < INFO_THRESH:
    verdict_coarse = "INFO"
    verdict_explanation = (
        f"chi_N * W varies {pct_var_coarse:.3f}% "
        f"in [{PASS_THRESH}%, {INFO_THRESH}%] -- partial Ward signature"
    )  # (local)
else:
    verdict_coarse = "FAIL"
    verdict_explanation = (
        f"chi_N * W varies {pct_var_coarse:.3f}% > {INFO_THRESH}% -- "
        f"no Ward duality; rank-2 functional rejected"
    )  # (local)

print(f"  COARSE GATE VERDICT: {verdict_coarse}")
print(f"    {verdict_explanation}")
print()


# ---------------------------------------------------------------
# STEP 7: FINE-GRID VAN-HOVE CHECK (SECONDARY)
# ---------------------------------------------------------------
# Question: does chi_N(tau) alone show concentration at tau_fold?
# Method: find argmax |chi_N(tau) - chi_N(tau_fold)|, or argmax of |chi_N|,
# or argmin (peak/valley), within the fine grid.  Check if the extremum
# lies within Delta_tau <= 0.02 of tau_fold = 0.190.
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 7: FINE-GRID VAN-HOVE CHECK (secondary deliverable)")
print("=" * 78)

# Index the fine grid
fine_idx = []  # (local)
for t_f in TAU_FINE:
    fine_idx.append(int(np.argmin(np.abs(tau_arr_full - t_f))))
fine_idx = np.array(fine_idx)  # (local)

tau_fine_actual = tau_arr_full[fine_idx]  # (local)
chi_N_fine = chi_N_arr[fine_idx]  # (local)

# Where does chi_N peak (max) and where does it trough (min)?
idx_max_fine = int(np.argmax(chi_N_fine))  # (local)
idx_min_fine = int(np.argmin(chi_N_fine))  # (local)

tau_argmax_chi = float(tau_fine_actual[idx_max_fine])  # (local)
tau_argmin_chi = float(tau_fine_actual[idx_min_fine])  # (local)

# Also: does chi_N have an extremum (local max OR local min) on the fine grid?
chi_N_diffs = np.diff(chi_N_fine)  # (local)
n_sign_changes = int(np.sum(np.diff(np.sign(chi_N_diffs)) != 0))  # (local)

# Distance from fold of the global extremum that is NOT at the boundary
# (endpoints are suspect by monotonicity artifacts)
interior_mask = (
    (tau_fine_actual > TAU_FINE.min() + 1e-6) &
    (tau_fine_actual < TAU_FINE.max() - 1e-6)
)  # (local)

if np.any(interior_mask):
    chi_N_interior = chi_N_fine.copy()  # (local)
    chi_N_interior_masked = np.where(interior_mask, chi_N_fine, np.nan)  # (local)

    # Find interior argmax, argmin
    try:
        idx_interior_max = int(np.nanargmax(chi_N_interior_masked))
        idx_interior_min = int(np.nanargmin(chi_N_interior_masked))
        tau_interior_argmax = float(tau_fine_actual[idx_interior_max])  # (local)
        tau_interior_argmin = float(tau_fine_actual[idx_interior_min])  # (local)
    except ValueError:
        tau_interior_argmax = np.nan
        tau_interior_argmin = np.nan
else:
    tau_interior_argmax = np.nan
    tau_interior_argmin = np.nan

# Local extrema detection (true local max/min interior to the fine grid)
local_extrema = []  # (local)
for i in range(1, len(chi_N_fine) - 1):
    if chi_N_fine[i] > chi_N_fine[i-1] and chi_N_fine[i] > chi_N_fine[i+1]:
        local_extrema.append(('MAX', float(tau_fine_actual[i]), float(chi_N_fine[i])))
    elif chi_N_fine[i] < chi_N_fine[i-1] and chi_N_fine[i] < chi_N_fine[i+1]:
        local_extrema.append(('MIN', float(tau_fine_actual[i]), float(chi_N_fine[i])))

print(f"\n  Fine grid {TAU_FINE}:")
print(f"  {'tau':>6s} | {'chi_N':>12s} | {'W':>12s} | {'Pi':>12s}")
print(f"  " + "-" * 52)
for i in range(len(tau_fine_actual)):
    mark = "  <-- fold" if abs(tau_fine_actual[i] - tau_fold) < 1e-4 else ""
    print(f"  {tau_fine_actual[i]:>6.4f} | {chi_N_fine[i]:>12.4f} | "
          f"{W_arr[fine_idx[i]]:>12.6f} | "
          f"{Pi_arr[fine_idx[i]]:>12.4f}{mark}")
print()

print(f"  Global argmax(chi_N) on fine grid: tau = {tau_argmax_chi:.4f}, "
      f"delta_to_fold = {abs(tau_argmax_chi - tau_fold):.4f}")
print(f"  Global argmin(chi_N) on fine grid: tau = {tau_argmin_chi:.4f}, "
      f"delta_to_fold = {abs(tau_argmin_chi - tau_fold):.4f}")
print(f"  Interior extrema: {len(local_extrema)}")
for kind, t_e, v_e in local_extrema:
    print(f"    {kind} at tau = {t_e:.4f}, chi_N = {v_e:.4f}, "
          f"delta_to_fold = {abs(t_e - tau_fold):.4f}")

# Sign-change count gives an indication of oscillatory vs monotone behavior
print(f"  Sign changes in d(chi_N)/dtau on fine grid: {n_sign_changes}")
print()

# Van-Hove qualification criterion: interior argmax of |chi_N - chi_N(fold)|
# within Delta_tau <= 0.02 of tau_fold, AND interior not on boundary.
chi_N_at_fold = float(chi_N_arr[idx_fold])  # (local)
chi_N_dev_fine = np.abs(chi_N_fine - chi_N_at_fold)  # (local)

# The van-Hove-like concentration CRITERION: interior local extremum near fold
van_hove_candidates = [
    (kind, t_e, v_e) for (kind, t_e, v_e) in local_extrema
    if abs(t_e - tau_fold) <= VAN_HOVE_DTAU
]  # (local)

if len(van_hove_candidates) > 0:
    van_hove_qualify = True
    van_hove_msg = (
        f"chi_N has interior extremum at tau in "
        f"[{tau_fold - VAN_HOVE_DTAU:.4f}, {tau_fold + VAN_HOVE_DTAU:.4f}]"
    )  # (local)
else:
    van_hove_qualify = False
    van_hove_msg = "chi_N has NO interior extremum near tau_fold (monotone or displaced)"  # (local)

print(f"  Van-Hove-like concentration qualification: {van_hove_qualify}")
print(f"    Criterion: interior local extremum within Delta_tau <= {VAN_HOVE_DTAU} of tau_fold")
print(f"    {van_hove_msg}")
if van_hove_qualify:
    print(f"    SECONDARY VERDICT: chi_N QUALIFIES as Sec VII.I 4th functional candidate.")
else:
    print(f"    SECONDARY VERDICT: chi_N DOES NOT qualify as Sec VII.I 4th functional candidate.")
print()


# ---------------------------------------------------------------
# STEP 8: SAVE NPZ
# ---------------------------------------------------------------

print("=" * 78)
print("STEP 8: SAVE OUTPUTS")
print("=" * 78)

out_npz = os.path.join(SCRIPT_DIR, "s80_chi_N_ward_dual.npz")
np.savez(
    out_npz,
    tau_all=tau_arr_full,
    a0=a0_arr,
    a2=a2_arr,
    a4=a4_arr,
    g_U1_sq=g_U1_sq_arr,
    sqrt_a4_over_a2=sqrt_ratio,
    chi_N=chi_N_arr,
    W=W_arr,
    Pi=Pi_arr,
    tau_coarse=tau_coarse_actual,
    chi_N_coarse=chi_N_coarse,
    W_coarse=W_coarse,
    Pi_coarse=Pi_coarse,
    tau_fine=tau_fine_actual,
    chi_N_fine=chi_N_fine,
    pct_var_coarse=pct_var_coarse,
    verdict_coarse=verdict_coarse,
    van_hove_qualify=van_hove_qualify,
    tau_argmax_chi=tau_argmax_chi,
    tau_argmin_chi=tau_argmin_chi,
    MAX_PQ_SUM=MAX_PQ_SUM,
    EVAL_CUTOFF=EVAL_CUTOFF,  # (local)
)
print(f"  Saved: {out_npz}")


# ---------------------------------------------------------------
# STEP 9: PLOTS
# ---------------------------------------------------------------

print()
print("=" * 78)
print("STEP 9: PLOTS")
print("=" * 78)

fig, axes = plt.subplots(3, 1, figsize=(9, 11), sharex=True)

# Panel 1: chi_N(tau)
ax1 = axes[0]
ax1.plot(tau_arr_full, chi_N_arr, 'o-', color='steelblue', lw=2, ms=5, label='chi_N(tau)')
ax1.axvline(tau_fold, color='red', ls='--', alpha=0.7, label=f'tau_fold = {tau_fold}')
ax1.scatter(tau_coarse_actual, chi_N_coarse, color='crimson', s=80, zorder=5,
            label='coarse grid (gate points)')
ax1.set_ylabel('chi_N(tau) = a_0 - a_2 + a_4')
ax1.set_title('S80 W1-5: CHI-N-WARD-DUAL functional (spectral Euler characteristic)')
ax1.legend(loc='best', fontsize=9)
ax1.grid(alpha=0.3)

# Panel 2: W(tau)
ax2 = axes[1]
ax2.plot(tau_arr_full, W_arr, 's-', color='darkorange', lw=2, ms=5, label='W(tau)')
ax2.axvline(tau_fold, color='red', ls='--', alpha=0.7, label=f'tau_fold = {tau_fold}')
ax2.scatter(tau_coarse_actual, W_coarse, color='crimson', s=80, zorder=5)
ax2.set_ylabel('W(tau) = g_U1^2 * sqrt(a_4/a_2)')
ax2.legend(loc='best', fontsize=9)
ax2.grid(alpha=0.3)

# Panel 3: Pi(tau) = chi_N * W
ax3 = axes[2]
ax3.plot(tau_arr_full, Pi_arr, '^-', color='seagreen', lw=2, ms=6, label='Pi(tau) = chi_N * W')
ax3.axvline(tau_fold, color='red', ls='--', alpha=0.7, label=f'tau_fold = {tau_fold}')
ax3.scatter(tau_coarse_actual, Pi_coarse, color='crimson', s=80, zorder=5,
            label='coarse grid')
# Annotate variation
ax3.text(0.02, 0.95,
         f'COARSE GRID variation = {pct_var_coarse:.2f}%\n'
         f'Gate verdict: {verdict_coarse}\n'
         f'(PASS<{PASS_THRESH}%, INFO<{INFO_THRESH}%, FAIL otherwise)',
         transform=ax3.transAxes, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='ivory', alpha=0.9), fontsize=10)
ax3.set_xlabel('tau (Jensen deformation parameter)')
ax3.set_ylabel('Pi(tau) = chi_N(tau) * W(tau)')
ax3.legend(loc='lower left', fontsize=9)
ax3.grid(alpha=0.3)

plt.tight_layout()
out_png = os.path.join(SCRIPT_DIR, "s80_chi_N_ward_dual.png")
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"  Saved: {out_png}")
plt.close()


# ---------------------------------------------------------------
# STEP 10: APPEND GATE VERDICT TO s80_gate_verdicts.txt
# ---------------------------------------------------------------

print()
print("=" * 78)
print("STEP 10: APPEND VERDICT")
print("=" * 78)

# Build the 4-tuple
scheme = "zeta"  # (local) S73B half-spectrum convention
convention = "S73B-Jensen-canonical"  # (local)

# Compute SHA-256 over the key numeric outputs for immutable provenance
import hashlib  # (local)
data_digest_input = (
    f"{pct_var_coarse:.8e}|{Pi_coarse[0]:.8e}|{Pi_coarse[1]:.8e}|"
    f"{Pi_coarse[2]:.8e}|{chi_N_fold:.8e}|{W_fold:.8e}"
).encode('utf-8')  # (local)
sha_digest = hashlib.sha256(data_digest_input).hexdigest()[:16]  # (local)

from datetime import datetime, timezone
timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # (local)

verdict_line = (
    f"[{timestamp}] S80-CHI-N-WARD-DUAL | {verdict_coarse} | "
    f"pct_var_coarse={pct_var_coarse:.4f}%% | "
    f"Pi_at_tau15={Pi_coarse[0]:.4f}, Pi_at_tau19={Pi_coarse[1]:.4f}, "
    f"Pi_at_tau25={Pi_coarse[2]:.4f} | "
    f"chi_N_at_fold={chi_N_fold:.4f}, W_at_fold={W_fold:.6f} | "
    f"van_hove_qualify={van_hove_qualify} | "
    f"tau_argmax_chi={tau_argmax_chi:.4f}, tau_argmin_chi={tau_argmin_chi:.4f} | "
    f"n_interior_extrema={len(local_extrema)} | "
    f"4-tuple=(Pi_at_fold={Pi_fold:.4f},scheme={scheme},"
    f"convention={convention},L_max={MAX_PQ_SUM}) | "
    f"classification=GEOMETRIC | "
    f"interpretation={verdict_explanation.replace(chr(124), '|')} | "
    f"sha256={sha_digest} | "
    f"agent=gen-physicist | script=s80_chi_N_ward_dual.py"
)  # (local)

# Normalize percent sign (remove literal %%) for shell-safe text
verdict_line = verdict_line.replace("%%", "%")  # (local)

verdicts_file = os.path.join(SCRIPT_DIR, "s80_gate_verdicts.txt")
with open(verdicts_file, "a", encoding="utf-8") as f:
    f.write("\n" + verdict_line + "\n")

print(f"  Appended to: {verdicts_file}")
print()
print(verdict_line)
print()
print("=" * 78)
print("S80 W1-5 CHI-N-WARD-DUAL COMPLETE")
print("=" * 78)
