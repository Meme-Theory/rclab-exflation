"""
SP-5: DNP STABILITY BOUND lambda_L/m^2(tau)
=============================================

Session 22a -- Schwarzschild-Penrose-Geometer

Computes the minimum Lichnerowicz eigenvalue lambda_L_min(tau) on TT
2-tensors in the (0,0) sector, then forms the ratio
    lambda_L_min(tau) / m^2_gauge(tau)
where m^2_gauge ~ e^{-4*tau} from the KK gauge coupling (Session 17a).

The Duff-Nilsson-Pope (DNP) stability bound states: for TT tensors on
a compact internal manifold, stability requires lambda_L >= certain
threshold related to m^2. If lambda_L_min * e^{4*tau} drops below 3,
the TT sector is unstable.

NOTE: The l20_TT_spectrum.npz file contains only aggregate quantities
(total Casimir energy, CW potential), not individual eigenvalues. We
must re-compute the (0,0) sector Lichnerowicz eigenvalues, which is
fast (35x35 matrix per tau).

DATA SOURCES:
    - l20_lichnerowicz.py: TT eigenvalue computation infrastructure
    - r20a_riemann_tensor.py: Riemann tensor at each tau

PRE-REGISTERED Constraint GateS:
    COMPELLING: lambda_L/m^2 drops below 3 in [0.15, 0.55]   (+3-5 pp)
    INTERESTING: lambda_L/m^2 non-monotonic                    (+1-2 pp)
    NEUTRAL: lambda_L/m^2 > 3 everywhere, monotonically increasing (0 pp)
    CLOSED: lambda_L/m^2 identical at all tau (symmetry artifact)  (-1 pp)

Author: Schwarzschild-Penrose-Geometer (Session 22a)
Date: 2026-02-20
"""

import numpy as np
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from l20_lichnerowicz import (
    build_sym2_traceless_basis,
    riemann_endomorphism_on_sym2,
    ricci_endomorphism_on_sym2,
    build_lichnerowicz_on_sector,
)
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
)
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
)

print("=" * 78)
print("  SP-5: DNP STABILITY BOUND lambda_L/m^2(tau)")
print("  Schwarzschild-Penrose-Geometer -- Session 22a")
print("=" * 78)

# ===========================================================================
# INFRASTRUCTURE
# ===========================================================================

gens = su3_generators()
f_abc = compute_structure_constants(gens)
basis = build_sym2_traceless_basis(8)
n = 8

# ===========================================================================
# PART 1: COMPUTE MINIMUM TT EIGENVALUE AT EACH TAU
# ===========================================================================

print("\n  PART 1: MINIMUM TT LICHNEROWICZ EIGENVALUE AT EACH TAU")
print()

tau_values = np.arange(0.0, 2.05, 0.1)
lambda_min_arr = []
lambda_max_arr = []
n_TT_arr = []

# Also check (1,0) and (0,1) sectors for completeness
lambda_min_10_arr = []
lambda_min_01_arr = []

print(f"  {'tau':>5}  {'lambda_min(0,0)':>15}  {'lambda_max(0,0)':>15}  {'n_TT':>5}  {'lambda_min(1,0)':>15}  {'lambda_min(0,1)':>15}")
print(f"  {'-----':>5}  {'---------------':>15}  {'---------------':>15}  {'-----':>5}  {'---------------':>15}  {'---------------':>15}")

for tau in tau_values:
    # Build geometric infrastructure
    R_abcd = compute_riemann_tensor_ON_fast(tau)
    Ric = ricci_from_riemann(R_abcd)
    R_endo = riemann_endomorphism_on_sym2(R_abcd, basis)
    Ric_endo = ricci_endomorphism_on_sym2(Ric, basis)

    # (0,0) sector -- this is where the global minimum lives
    evals_TT_00, n_TT_00, n_full_00 = build_lichnerowicz_on_sector(
        0, 0, tau, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, n
    )

    if len(evals_TT_00) > 0:
        lmin_00 = np.min(evals_TT_00)
        lmax_00 = np.max(evals_TT_00)
    else:
        lmin_00 = np.nan
        lmax_00 = np.nan

    lambda_min_arr.append(lmin_00)
    lambda_max_arr.append(lmax_00)
    n_TT_arr.append(n_TT_00)

    # (1,0) sector
    try:
        evals_TT_10, _, _ = build_lichnerowicz_on_sector(
            1, 0, tau, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, n
        )
        lmin_10 = np.min(evals_TT_10) if len(evals_TT_10) > 0 else np.nan
    except Exception:
        lmin_10 = np.nan

    # (0,1) sector
    try:
        evals_TT_01, _, _ = build_lichnerowicz_on_sector(
            0, 1, tau, R_abcd, basis, R_endo, Ric_endo, gens, f_abc, n
        )
        lmin_01 = np.min(evals_TT_01) if len(evals_TT_01) > 0 else np.nan
    except Exception:
        lmin_01 = np.nan

    lambda_min_10_arr.append(lmin_10)
    lambda_min_01_arr.append(lmin_01)

    print(f"  {tau:5.2f}  {lmin_00:15.8f}  {lmax_00:15.8f}  {n_TT_00:5d}  {lmin_10:15.8f}  {lmin_01:15.8f}")

lambda_min_arr = np.array(lambda_min_arr)
lambda_max_arr = np.array(lambda_max_arr)
n_TT_arr = np.array(n_TT_arr)
lambda_min_10_arr = np.array(lambda_min_10_arr)
lambda_min_01_arr = np.array(lambda_min_01_arr)

# ===========================================================================
# PART 2: GLOBAL MINIMUM ACROSS LOW SECTORS
# ===========================================================================

print("\n  PART 2: GLOBAL MINIMUM ACROSS SECTORS (0,0), (1,0), (0,1)")
print()

# Global min at each tau
global_min = np.minimum(lambda_min_arr, np.minimum(lambda_min_10_arr, lambda_min_01_arr))

print(f"  {'tau':>5}  {'global_min':>12}  {'source':>8}")
print(f"  {'-----':>5}  {'----------':>12}  {'--------':>8}")
for i, tau in enumerate(tau_values):
    gmin = global_min[i]
    if gmin == lambda_min_arr[i]:
        src = "(0,0)"
    elif gmin == lambda_min_10_arr[i]:
        src = "(1,0)"
    else:
        src = "(0,1)"
    print(f"  {tau:5.2f}  {gmin:12.8f}  {src:>8}")

# ===========================================================================
# PART 3: DNP RATIO lambda_L_min / m^2_gauge
# ===========================================================================

print("\n  PART 3: DNP RATIO lambda_L_min(tau) * e^{4*tau}")
print()

# m^2_gauge(tau) ~ g_1^2(tau) ~ e^{-4*tau}
# Ratio = lambda_L_min(tau) / m^2_gauge(tau) ~ lambda_L_min(tau) * e^{4*tau}

m2_gauge = np.exp(-4 * tau_values)
ratio = global_min / m2_gauge  # = global_min * e^{4*tau}

print(f"  {'tau':>5}  {'lambda_L_min':>12}  {'m2_gauge':>12}  {'ratio':>12}  {'DNP bound':>10}")
print(f"  {'-----':>5}  {'----------':>12}  {'----------':>12}  {'----------':>12}  {'----------':>10}")
for i, tau in enumerate(tau_values):
    bound_status = "STABLE" if ratio[i] >= 3.0 else "UNSTABLE"
    print(f"  {tau:5.2f}  {global_min[i]:12.8f}  {m2_gauge[i]:12.8f}  {ratio[i]:12.4f}  {bound_status:>10}")

print()
print(f"  Minimum ratio: {np.min(ratio):.4f} at tau={tau_values[np.argmin(ratio)]:.2f}")
print(f"  Maximum ratio: {np.max(ratio):.4f} at tau={tau_values[np.argmax(ratio)]:.2f}")
print(f"  Ratio at tau=0.00: {ratio[0]:.4f}")
print(f"  Ratio at tau=0.30: {ratio[3]:.4f}")
print(f"  Ratio at tau=0.50: {ratio[5]:.4f}")

# Check DNP bound violation
dnp_violated = np.any(ratio < 3.0)
if dnp_violated:
    violated_idx = np.where(ratio < 3.0)[0]
    print(f"\n  *** DNP BOUND VIOLATED at tau = {tau_values[violated_idx]} ***")
else:
    print(f"\n  DNP bound satisfied everywhere (ratio >= 3.0): {not dnp_violated}")

# ===========================================================================
# PART 4: MONOTONICITY CHECK
# ===========================================================================

print("\n  PART 4: MONOTONICITY ANALYSIS")
print()

# Check if ratio is monotonic
diffs = np.diff(ratio)
monotone_increasing = np.all(diffs > 0)
monotone_decreasing = np.all(diffs < 0)
non_monotonic = not (monotone_increasing or monotone_decreasing)

print(f"  Ratio monotonically increasing: {monotone_increasing}")
print(f"  Ratio monotonically decreasing: {monotone_decreasing}")
print(f"  Non-monotonic: {non_monotonic}")

if non_monotonic:
    # Find local extrema
    for i in range(1, len(ratio) - 1):
        if ratio[i] > ratio[i-1] and ratio[i] > ratio[i+1]:
            print(f"  Local maximum at tau={tau_values[i]:.2f}: ratio={ratio[i]:.4f}")
        elif ratio[i] < ratio[i-1] and ratio[i] < ratio[i+1]:
            print(f"  Local minimum at tau={tau_values[i]:.2f}: ratio={ratio[i]:.4f}")

# Also check: lambda_L_min itself -- is it monotonic?
diffs_lmin = np.diff(global_min)
lmin_monotone_inc = np.all(diffs_lmin > 0)
lmin_monotone_dec = np.all(diffs_lmin < 0)
print(f"\n  lambda_L_min monotonically increasing: {lmin_monotone_inc}")
print(f"  lambda_L_min monotonically decreasing: {lmin_monotone_dec}")

# ===========================================================================
# PART 5: Constraint Gate ASSESSMENT
# ===========================================================================

print("\n  PART 5: Constraint Gate ASSESSMENT")
print()

all_equal = np.all(np.abs(ratio - ratio[0]) < 1e-4)

if all_equal:
    verdict = "CLOSED"
    detail = "lambda_L/m^2 identical at all tau (symmetry artifact)"
    prob_shift = "-1 pp"
elif dnp_violated:
    # Check if violation is in physical window
    phys_window = (tau_values >= 0.15) & (tau_values <= 0.55)
    if np.any(ratio[phys_window] < 3.0):
        verdict = "COMPELLING"
        detail = f"DNP bound violated in physical window at tau = {tau_values[phys_window & (ratio < 3.0)]}"
        prob_shift = "+3-5 pp"
    else:
        verdict = "INTERESTING"
        detail = "DNP bound violated but outside physical window"
        prob_shift = "+1-2 pp"
elif non_monotonic:
    verdict = "INTERESTING"
    detail = "lambda_L/m^2 non-monotonic (structure in ratio)"
    prob_shift = "+1-2 pp"
else:
    verdict = "NEUTRAL"
    detail = "lambda_L/m^2 > 3 everywhere, monotonic"
    prob_shift = "0 pp"

print(f"  *** VERDICT: {verdict} ***")
print(f"  Detail: {detail}")
print(f"  Probability shift: {prob_shift}")
print()

# ===========================================================================
# SAVE DATA
# ===========================================================================

np.savez(os.path.join(SCRIPT_DIR, 's22a_dnp_bound.npz'),
         tau=tau_values,
         lambda_min_00=lambda_min_arr,
         lambda_max_00=lambda_max_arr,
         lambda_min_10=lambda_min_10_arr,
         lambda_min_01=lambda_min_01_arr,
         global_min=global_min,
         m2_gauge=m2_gauge,
         ratio=ratio,
         n_TT_00=n_TT_arr,
         verdict=np.array([verdict]),
         prob_shift=np.array([prob_shift]),
)
print(f"  Data saved: tier0-computation/s22a_dnp_bound.npz")

# ===========================================================================
# PLOT
# ===========================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: lambda_L_min vs tau
ax1 = axes[0, 0]
ax1.plot(tau_values, lambda_min_arr, 'bo-', label='(0,0) min', markersize=4)
ax1.plot(tau_values, lambda_min_10_arr, 'rs-', label='(1,0) min', markersize=4)
ax1.plot(tau_values, lambda_min_01_arr, 'g^-', label='(0,1) min', markersize=4)
ax1.plot(tau_values, global_min, 'k-', linewidth=2, label='Global min')
ax1.set_xlabel('tau')
ax1.set_ylabel('lambda_L_min')
ax1.set_title('Minimum TT Lichnerowicz eigenvalue')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel 2: DNP ratio
ax2 = axes[0, 1]
ax2.plot(tau_values, ratio, 'ko-', markersize=5)
ax2.axhline(y=3.0, color='red', linestyle='--', label='DNP bound = 3')
ax2.set_xlabel('tau')
ax2.set_ylabel('lambda_L_min / m^2_gauge')
ax2.set_title('DNP stability ratio')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.set_yscale('log')

# Panel 3: m^2_gauge vs tau
ax3 = axes[1, 0]
ax3.plot(tau_values, m2_gauge, 'b-', label='m^2_gauge = e^{-4*tau}')
ax3.plot(tau_values, global_min, 'r-', label='lambda_L_min')
ax3.set_xlabel('tau')
ax3.set_ylabel('Value')
ax3.set_title('Eigenvalue vs gauge mass')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)
ax3.set_yscale('log')

# Panel 4: (0,0) TT eigenvalue range
ax4 = axes[1, 1]
ax4.fill_between(tau_values, lambda_min_arr, lambda_max_arr, alpha=0.3, color='blue')
ax4.plot(tau_values, lambda_min_arr, 'b-', label='min')
ax4.plot(tau_values, lambda_max_arr, 'b--', label='max')
ax4.set_xlabel('tau')
ax4.set_ylabel('TT eigenvalue')
ax4.set_title('(0,0) sector TT eigenvalue range')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

plt.suptitle('SP-5: DNP Stability Bound', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's22a_dnp_bound.png'), dpi=150, bbox_inches='tight')
print(f"  Plot saved: tier0-computation/s22a_dnp_bound.png")

# ===========================================================================
# SUMMARY
# ===========================================================================

print("\n" + "=" * 78)
print("  SP-5 SUMMARY: DNP STABILITY BOUND")
print("=" * 78)
print()
print(f"  lambda_L_min range: [{np.min(global_min):.8f}, {np.max(global_min):.8f}]")
print(f"  DNP ratio range: [{np.min(ratio):.4f}, {np.max(ratio):.4f}]")
print(f"  DNP bound (>= 3) violated: {dnp_violated}")
print(f"  Ratio monotonic: {monotone_increasing or monotone_decreasing}")
print()
print(f"  *** VERDICT: {verdict} ***")
print(f"  {detail}")
print(f"  Probability shift: {prob_shift}")
print()
print("=" * 78)
