#!/usr/bin/env python3
"""
s65_instability_timescale.py — INSTABILITY-65: Anti-Jensen Instability Timescale
=================================================================================

Gate: INSTABILITY-65
  PASS: tau_inst < tau_transit for at least one mode (Jensen curve unstable)
  FAIL: tau_inst > 10 * tau_transit for ALL modes (Jensen curve metastable)
  INFO: tau_inst ~ tau_transit (comparable timescales, marginal)

Context:
  S64 HESSIAN-DESCENT-64 proved the R-curvature Hessian at the fold has
  signature (8+, 27-) in the 35D volume-preserving subspace: a saddle point
  with 27 descent directions for R (and therefore a_2).

  S61 MODULI-HESS-61 proved ALL 36 eigenvalues of the full spectral action
  Hessian are negative at the fold — the fold is a maximum of S_A in all 36D.

  The 27 negative R-Hessian directions are off-diagonal in the U(2)-invariant
  basis. Baptista's U(2)-invariance preservation theorem shows these are
  structurally inaccessible to classical gradient flow. But quantum/thermal
  fluctuations CAN excite them.

  This computation determines the TIMESCALE of the instability for all 27
  descent modes and compares to the transit time.

Physical derivation:
  The spectral action generates the effective potential for moduli:
    V_eff(g) = Lambda^4 * S_A(g)   [in M_KK^4 units with Lambda^2 ~ a_0]

  The moduli kinetic term in DeWitt superspace:
    T = (1/2) G_ab^{cd} * dgot_ab * dgot_cd
  with G_DeWitt = 5.0 (canonical constant from S42).

  The physical frequency-squared for mode i is:
    omega_i^2 = |lambda_i^{SA}| / G_DeWitt   [M_KK^2 units]

  where lambda_i^{SA} are eigenvalues of d^2 S_A / dg^2.

  The instability timescale:
    tau_inst,i = 1 / omega_i = sqrt(G_DeWitt / |lambda_i^{SA}|)  [M_KK^{-1}]

  Two analyses:
    A. Using the S64 R-Hessian eigenvalues (as specified in task)
       tau_inst,i = 1/sqrt(|lambda_i^R|)   [M_KK^{-1}]
    B. Using the S61 full SA-Hessian eigenvalues (physically correct)
       tau_inst,i = sqrt(G_DeWitt / |lambda_i^{SA}|)  [M_KK^{-1}]

  Transit timescale: tau_transit = 1/H_phys = 1/0.396 = 2.525 M_KK^{-1}

Author: gen-physicist (Session 65, Wave 3-E)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import os
import time

t_start = time.time()

script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from canonical_constants import (
    tau_fold, G_DeWitt, PI,
    a0_fold, a2_fold, a4_fold,
)

print("=" * 78)
print("  INSTABILITY-65: Anti-Jensen Instability Timescale")
print("=" * 78)

# =============================================================================
# 1. Load S64 R-Hessian Data
# =============================================================================
print("\n--- 1. Loading S64 R-Hessian data ---")

data_s64 = np.load(str(script_dir / 's64_hessian_descent.npz'), allow_pickle=True)
evals_R_35 = data_s64['evals_35']           # 35 eigenvalues of d^2R/dg^2 (vol-preserving)
n_pos_R = int(data_s64['n_pos_R'])
n_neg_R = int(data_s64['n_neg_R'])
R_fold = float(data_s64['R_fold_ref'])
basis_labels = data_s64['basis_labels']

print(f"  R-Hessian signature: ({n_pos_R}+, {n_neg_R}-) in 35D VP subspace")
print(f"  R(fold) = {R_fold:.6f}")
print(f"  tau_fold = {tau_fold}")

# Sort eigenvalues (most negative first for descent analysis)
sort_idx_R = np.argsort(evals_R_35)
evals_R_sorted = evals_R_35[sort_idx_R]

# Extract the 27 negative eigenvalues (descent directions)
neg_mask = evals_R_sorted < 0
evals_R_neg = evals_R_sorted[neg_mask]
n_neg_check = len(evals_R_neg)
assert n_neg_check == 27, f"Expected 27 negative R-eigenvalues, got {n_neg_check}"

print(f"\n  27 negative R-Hessian eigenvalues:")
for i, ev in enumerate(evals_R_neg):
    print(f"    [{i:2d}] lambda_R = {ev:+.6e}")

# =============================================================================
# 2. Load S61 Full SA-Hessian Data
# =============================================================================
print("\n--- 2. Loading S61 full SA-Hessian data ---")

data_s61 = np.load(str(script_dir / 's61_moduli_hessian.npz'), allow_pickle=True)
evals_SA_36 = data_s61['evals_36']          # 36 eigenvalues of d^2 S_A / dg^2
SA_fold = float(data_s61['SA_fold'])
n_pos_SA = int(data_s61['n_pos_36'])
n_neg_SA = int(data_s61['n_neg_36'])

print(f"  SA-Hessian: ALL {n_neg_SA} negative (fold = maximum)")
print(f"  S_A(fold) = {SA_fold:.4f}")

# Sort (most negative first)
evals_SA_sorted = np.sort(evals_SA_36)

print(f"\n  SA-Hessian eigenvalues (all 36):")
for i, ev in enumerate(evals_SA_sorted):
    print(f"    [{i:2d}] lambda_SA = {ev:+.6e}")

# =============================================================================
# 3. Transit Timescale
# =============================================================================
print("\n--- 3. Transit timescale ---")

H_phys = 0.396  # M_KK units (from session-65-plan)  # (local)
tau_transit = 1.0 / H_phys

print(f"  H_phys = {H_phys:.3f} M_KK")
print(f"  tau_transit = 1/H_phys = {tau_transit:.4f} M_KK^{{-1}}")

# =============================================================================
# 4A. Instability Timescales from R-Hessian (task specification)
# =============================================================================
print("\n--- 4A. Instability timescales from R-Hessian ---")
print("  NOTE: tau_inst = 1/sqrt(|lambda_R|) as specified in task")
print("  These eigenvalues are d^2R/dg^2 (dimensionless).")
print("  Interpreting as M_KK^2 units follows if R is measured in M_KK^2.\n")

tau_inst_R = 1.0 / np.sqrt(np.abs(evals_R_neg))

# Identify distinct eigenvalue multiplets
# Group by value within tolerance
tolerance = 1e-4  # (local)
multiplets_R = []
current_val = evals_R_neg[0]
current_count = 1
current_indices = [0]

for i in range(1, len(evals_R_neg)):
    if abs(evals_R_neg[i] - current_val) / abs(current_val) < tolerance:
        current_count += 1
        current_indices.append(i)
    else:
        multiplets_R.append((current_val, current_count, current_indices.copy()))
        current_val = evals_R_neg[i]
        current_count = 1
        current_indices = [i]
multiplets_R.append((current_val, current_count, current_indices.copy()))

print(f"  {'Multiplet':<12s} {'lambda_R':>14s} {'Degeneracy':>10s} "
      f"{'tau_inst':>12s} {'tau_inst/tau_tr':>16s} {'Status':>12s}")
print("  " + "-" * 80)

n_faster = 0
for val, deg, indices in multiplets_R:
    t_inst = 1.0 / np.sqrt(abs(val))
    ratio = t_inst / tau_transit
    if ratio < 1.0:
        status = "UNSTABLE"
        n_faster += deg
    elif ratio < 10.0:
        status = "MARGINAL"
    else:
        status = "STABLE"
    print(f"  {deg:>4d}-fold    {val:>+14.6e}  {deg:>10d}  "
          f"{t_inst:>12.4f}  {ratio:>16.4f}  {status:>12s}")

lambda_min_R = evals_R_neg[0]
tau_inst_min_R = 1.0 / np.sqrt(abs(lambda_min_R))
ratio_min_R = tau_inst_min_R / tau_transit

print(f"\n  lambda_min (R-Hessian) = {lambda_min_R:.6e}")
print(f"  tau_inst_min (R-Hessian) = {tau_inst_min_R:.4f} M_KK^{{-1}}")
print(f"  tau_transit = {tau_transit:.4f} M_KK^{{-1}}")
print(f"  Ratio tau_inst_min / tau_transit = {ratio_min_R:.4f}")
print(f"  Modes with tau_inst < tau_transit: {n_faster} / {n_neg_check}")

# =============================================================================
# 4B. Instability Timescales from SA-Hessian (physically correct)
# =============================================================================
print("\n--- 4B. Instability timescales from SA-Hessian (physical) ---")
print(f"  tau_inst = sqrt(G_DeWitt / |lambda_SA|)")
print(f"  G_DeWitt = {G_DeWitt}")
print(f"  This uses the physical kinetic coefficient in the DeWitt supermetric.\n")

# All 36 SA eigenvalues are negative; use all of them
tau_inst_SA = np.sqrt(G_DeWitt / np.abs(evals_SA_sorted))

# Group SA multiplets
multiplets_SA = []
current_val = evals_SA_sorted[0]
current_count = 1
current_indices = [0]

for i in range(1, len(evals_SA_sorted)):
    if abs(evals_SA_sorted[i] - current_val) / abs(current_val) < tolerance:
        current_count += 1
        current_indices.append(i)
    else:
        multiplets_SA.append((current_val, current_count, current_indices.copy()))
        current_val = evals_SA_sorted[i]
        current_count = 1
        current_indices = [i]
multiplets_SA.append((current_val, current_count, current_indices.copy()))

print(f"  {'Multiplet':<12s} {'lambda_SA':>14s} {'Degeneracy':>10s} "
      f"{'tau_inst':>12s} {'tau_inst/tau_tr':>16s} {'Status':>12s}")
print("  " + "-" * 80)

n_faster_SA = 0
n_marginal_SA = 0
for val, deg, indices in multiplets_SA:
    t_inst = np.sqrt(G_DeWitt / abs(val))
    ratio = t_inst / tau_transit
    if ratio < 1.0:
        status = "UNSTABLE"
        n_faster_SA += deg
    elif ratio < 10.0:
        status = "MARGINAL"
        n_marginal_SA += deg
    else:
        status = "STABLE"
    print(f"  {deg:>4d}-fold    {val:>+14.6e}  {deg:>10d}  "
          f"{t_inst:>12.4f}  {ratio:>16.4f}  {status:>12s}")

lambda_min_SA = evals_SA_sorted[0]
tau_inst_min_SA = np.sqrt(G_DeWitt / abs(lambda_min_SA))
ratio_min_SA = tau_inst_min_SA / tau_transit

print(f"\n  lambda_min (SA-Hessian) = {lambda_min_SA:.6e}")
print(f"  tau_inst_min (SA-Hessian) = {tau_inst_min_SA:.4f} M_KK^{{-1}}")
print(f"  tau_transit = {tau_transit:.4f} M_KK^{{-1}}")
print(f"  Ratio tau_inst_min / tau_transit = {ratio_min_SA:.4f}")
print(f"  Modes with tau_inst < tau_transit: {n_faster_SA} / 36")
print(f"  Modes with tau_inst < 10*tau_transit: {n_faster_SA + n_marginal_SA} / 36")

# =============================================================================
# 5. Full Ranking: All 27 R-Hessian Descent Modes
# =============================================================================
print("\n--- 5. Full ranking of 27 R-descent modes by instability timescale ---")
print(f"  {'Mode':>5s} {'lambda_R':>14s} {'omega (M_KK)':>14s} "
      f"{'tau_inst (M_KK^-1)':>20s} {'tau_inst/tau_tr':>16s}")
print("  " + "-" * 75)

for i in range(len(evals_R_neg)):
    lam = evals_R_neg[i]
    omega = np.sqrt(abs(lam))
    t_inst = 1.0 / omega
    ratio = t_inst / tau_transit
    marker = " <-- FASTER" if ratio < 1.0 else (" <-- MARGINAL" if ratio < 10.0 else "")
    print(f"  {i:>5d}  {lam:>+14.6e}  {omega:>14.6f}  "
          f"{t_inst:>20.4f}  {ratio:>16.4f}{marker}")

# =============================================================================
# 6. Full Ranking: All 36 SA-Hessian Modes
# =============================================================================
print("\n--- 6. Full ranking of 36 SA modes by instability timescale ---")
print(f"  {'Mode':>5s} {'lambda_SA':>14s} {'omega (M_KK)':>14s} "
      f"{'tau_inst (M_KK^-1)':>20s} {'tau_inst/tau_tr':>16s}")
print("  " + "-" * 75)

for i in range(len(evals_SA_sorted)):
    lam = evals_SA_sorted[i]
    omega = np.sqrt(abs(lam) / G_DeWitt)
    t_inst = 1.0 / omega
    ratio = t_inst / tau_transit
    marker = " <-- FASTER" if ratio < 1.0 else (" <-- MARGINAL" if ratio < 10.0 else "")
    print(f"  {i:>5d}  {lam:>+14.6e}  {omega:>14.6f}  "
          f"{t_inst:>20.4f}  {ratio:>16.4f}{marker}")

# =============================================================================
# 7. Gate Verdict
# =============================================================================
print("\n" + "=" * 78)
print("  GATE VERDICT: INSTABILITY-65")
print("=" * 78)

# Use R-Hessian as specified in the task for the gate
all_tau_inst_R = 1.0 / np.sqrt(np.abs(evals_R_neg))
any_faster = np.any(all_tau_inst_R < tau_transit)
all_10x_slower = np.all(all_tau_inst_R > 10.0 * tau_transit)

if any_faster:
    gate_verdict = "PASS"
    print(f"  PASS: tau_inst < tau_transit for {n_faster} modes")
    print(f"  Fastest mode: tau_inst = {tau_inst_min_R:.4f} vs tau_transit = {tau_transit:.4f}")
    print(f"  Ratio: {ratio_min_R:.4f} (< 1 => classically unstable)")
elif all_10x_slower:
    gate_verdict = "FAIL"
    print(f"  FAIL: tau_inst > 10 * tau_transit for ALL modes")
else:
    gate_verdict = "INFO"
    print(f"  INFO: tau_inst ~ tau_transit (comparable timescales)")
    n_in_band = np.sum((all_tau_inst_R >= tau_transit) & (all_tau_inst_R <= 10.0 * tau_transit))
    print(f"  {n_in_band} modes in marginal band (1-10x tau_transit)")

print(f"\n  Gate verdict: {gate_verdict}")

# SA-Hessian cross-check
print(f"\n  SA-Hessian cross-check:")
print(f"    tau_inst_min (SA) = {tau_inst_min_SA:.4f} M_KK^{{-1}}")
print(f"    ratio = {ratio_min_SA:.4f}")
sa_verdict = "ALL UNSTABLE" if np.all(tau_inst_SA < tau_transit) else (
    f"{n_faster_SA}/36 UNSTABLE" if n_faster_SA > 0 else "STABLE")
print(f"    SA verdict: {sa_verdict}")

# =============================================================================
# 8. Physical Interpretation
# =============================================================================
print("\n--- 8. Physical Interpretation ---")

# Quantum fluctuation amplitude at zero temperature
# delta_g ~ 1/sqrt(omega * G_DeWitt) for zero-point motion
# (simple harmonic oscillator: <x^2> = 1/(2*m*omega) in natural units)
print("  Quantum zero-point fluctuation amplitudes (delta_g):")
print(f"  {'Mode':>5s} {'omega (M_KK)':>14s} {'delta_g':>14s}")
print("  " + "-" * 40)

for i, (val, deg, indices) in enumerate(multiplets_SA):
    omega = np.sqrt(abs(val) / G_DeWitt)
    delta_g = 1.0 / np.sqrt(2.0 * G_DeWitt * omega)
    print(f"  {deg:>4d}x    {omega:>14.6f}  {delta_g:>14.6f}")

# Thermal activation at GGE temperature
T_GGE = 0.112  # M_KK units (canonical: T_acoustic)  # (local)
print(f"\n  Thermal fluctuation at T_GGE = {T_GGE} M_KK:")
print(f"  Boltzmann suppression for each multiplet:")
for val, deg, indices in multiplets_SA:
    omega = np.sqrt(abs(val) / G_DeWitt)
    # Energy of the mode ~ omega (in M_KK units)
    # Boltzmann factor ~ exp(-omega / T_GGE)
    boltz = np.exp(-omega / T_GGE)
    print(f"    {deg}x: omega = {omega:.4f}, exp(-omega/T) = {boltz:.4e}")

# =============================================================================
# 9. Summary Table
# =============================================================================
print("\n--- 9. Summary ---")
print(f"  Transit:  tau_transit = {tau_transit:.4f} M_KK^{{-1}}")
print(f"  R-Hessian fastest instability: tau_inst = {tau_inst_min_R:.4f} M_KK^{{-1}}")
print(f"    ratio = {ratio_min_R:.4f}")
print(f"    modes faster than transit: {n_faster}/{n_neg_check}")
print(f"  SA-Hessian fastest instability: tau_inst = {tau_inst_min_SA:.4f} M_KK^{{-1}}")
print(f"    ratio = {ratio_min_SA:.4f}")
print(f"    modes faster than transit: {n_faster_SA}/36")
print(f"  Gate: {gate_verdict}")

# =============================================================================
# 10. Plotting
# =============================================================================
print("\n--- 10. Generating plots ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('INSTABILITY-65: Anti-Jensen Instability Timescales', fontsize=14, fontweight='bold')

# Panel (a): R-Hessian eigenvalue spectrum
ax = axes[0, 0]
colors_R = ['red' if e < 0 else 'blue' for e in evals_R_sorted]
ax.bar(range(len(evals_R_sorted)), evals_R_sorted, color=colors_R, alpha=0.7, width=0.8)
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('Mode index (sorted)')
ax.set_ylabel(r'$\lambda_R$ (R-Hessian eigenvalue)')
ax.set_title(f'(a) R-Hessian: ({n_pos_R}+, {n_neg_R}-)')

# Panel (b): SA-Hessian eigenvalue spectrum
ax = axes[0, 1]
ax.bar(range(len(evals_SA_sorted)), evals_SA_sorted, color='red', alpha=0.7, width=0.8)
ax.set_xlabel('Mode index (sorted)')
ax.set_ylabel(r'$\lambda_{SA}$ (SA-Hessian eigenvalue)')
ax.set_title(f'(b) SA-Hessian: (0+, 36-)')

# Panel (c): Instability timescales vs transit time (R-Hessian)
ax = axes[1, 0]
tau_inst_all_R = np.sort(1.0 / np.sqrt(np.abs(evals_R_sorted)))
mode_idx = np.arange(len(tau_inst_all_R))
colors_inst = ['red' if t < tau_transit else ('orange' if t < 10*tau_transit else 'green')
               for t in tau_inst_all_R]
ax.bar(mode_idx, tau_inst_all_R, color=colors_inst, alpha=0.7, width=0.8)
ax.axhline(y=tau_transit, color='blue', linewidth=2, linestyle='--', label=r'$\tau_{transit}$')
ax.axhline(y=10*tau_transit, color='blue', linewidth=1, linestyle=':', label=r'$10\times\tau_{transit}$')
ax.set_xlabel('Mode index (sorted by timescale)')
ax.set_ylabel(r'$\tau_{inst}$ ($M_{KK}^{-1}$)')
ax.set_title('(c) R-Hessian Instability Timescales')
ax.legend(fontsize=8)
ax.set_yscale('log')

# Panel (d): Instability timescales vs transit time (SA-Hessian)
ax = axes[1, 1]
tau_inst_all_SA = np.sort(np.sqrt(G_DeWitt / np.abs(evals_SA_sorted)))
mode_idx_SA = np.arange(len(tau_inst_all_SA))
colors_inst_SA = ['red' if t < tau_transit else ('orange' if t < 10*tau_transit else 'green')
                  for t in tau_inst_all_SA]
ax.bar(mode_idx_SA, tau_inst_all_SA, color=colors_inst_SA, alpha=0.7, width=0.8)
ax.axhline(y=tau_transit, color='blue', linewidth=2, linestyle='--', label=r'$\tau_{transit}$')
ax.axhline(y=10*tau_transit, color='blue', linewidth=1, linestyle=':', label=r'$10\times\tau_{transit}$')
ax.set_xlabel('Mode index (sorted by timescale)')
ax.set_ylabel(r'$\tau_{inst}$ ($M_{KK}^{-1}$)')
ax.set_title('(d) SA-Hessian Instability Timescales')
ax.legend(fontsize=8)
ax.set_yscale('log')

plt.tight_layout()
plt.savefig(str(script_dir / 's65_instability_timescale.png'), dpi=150, bbox_inches='tight')
print("  Plot saved: s65_instability_timescale.png")

# =============================================================================
# 11. Save Data
# =============================================================================
print("\n--- 11. Saving data ---")

np.savez(str(script_dir / 's65_instability_timescale.npz'),
    # R-Hessian analysis
    evals_R_neg=evals_R_neg,
    tau_inst_R=tau_inst_R,
    lambda_min_R=lambda_min_R,
    tau_inst_min_R=tau_inst_min_R,
    n_faster_R=n_faster,
    n_neg_R=n_neg_check,
    # SA-Hessian analysis
    evals_SA_sorted=evals_SA_sorted,
    tau_inst_SA=tau_inst_SA,
    lambda_min_SA=lambda_min_SA,
    tau_inst_min_SA=tau_inst_min_SA,
    n_faster_SA=n_faster_SA,
    # Transit parameters
    H_phys=H_phys,
    tau_transit=tau_transit,
    # Gate
    gate_verdict=gate_verdict,
    ratio_min_R=ratio_min_R,
    ratio_min_SA=ratio_min_SA,
    # Multiplet structure
    R_multiplet_vals=np.array([m[0] for m in multiplets_R]),
    R_multiplet_degs=np.array([m[1] for m in multiplets_R]),
    SA_multiplet_vals=np.array([m[0] for m in multiplets_SA]),
    SA_multiplet_degs=np.array([m[1] for m in multiplets_SA]),
    # Metadata
    G_DeWitt=G_DeWitt,
    tau_fold=tau_fold,
    R_fold=R_fold,
    SA_fold=SA_fold,
)
print("  Data saved: s65_instability_timescale.npz")

t_end = time.time()
print(f"\n  Total computation time: {t_end - t_start:.2f} s")
print("=" * 78)
