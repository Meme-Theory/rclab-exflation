#!/usr/bin/env python3
"""
S52 -- TORSION-52: Analytic Torsion on Jensen-Deformed SU(3)
=============================================================

Gate: TORSION-52
  PASS: nontrivial structure (minimum, inflection, discontinuity at fold)
  INFO: monotone

Computes the spinor analytic torsion log T_{RS}(tau) = -(1/2) zeta'_{D^2}(0)
across the Jensen deformation family on SU(3).

For a FINITE positive spectrum {|lambda_k|} with Peter-Weyl degeneracies {d_k}:

    zeta_{D^2}(s) = sum_k d_k |lambda_k|^{-2s}             (1)
    zeta'_{D^2}(0) = -2 sum_k d_k ln|lambda_k|              (2)
    log T = -(1/2) zeta'(0) = sum_k d_k ln|lambda_k|        (3)

Three torsion variants:
  A. Singlet torsion: T_{singlet}(tau) = prod_{k in (0,0)} |lambda_k|
     (16 modes, d_k = 1; physically relevant per S44 EIH)
  B. Full-spectrum torsion: log10 T = sum_k d_k^2 ln|lambda_k| / ln10
     (992 modes with PW weights; known S45 artifact but tracks geometry)
  C. Sector-decomposed torsion: per-sector contributions to track which
     Peter-Weyl sectors dominate the tau-variation

Method:
  1. Recompute Dirac eigenvalues at 50 tau values from dirac_spectrum
  2. Evaluate (2)-(3) exactly at each tau
  3. Numerical differentiation d(log T)/d(tau) for inflection detection
  4. Compare structure near tau_fold = 0.19

Input: dirac_spectrum.py (Dirac operator infrastructure)
Output: s52_analytic_torsion.{npz,png}

Author: Spectral-Geometer (Session 52)
Date: 2026-03-20
"""

import sys
import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(SCRIPT_DIR, "..", "_shared")
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

from canonical_constants import tau_fold, a0_fold, a2_fold, a4_fold, PI

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    get_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)

# =============================================================================
# SECTION 0: Constants and tau grid
# =============================================================================

TAU_FOLD = float(tau_fold)  # 0.19

# Dense tau grid: uniform + extra points near fold
tau_uniform = np.linspace(0.005, 0.30, 30)
tau_near_fold = np.array([0.17, 0.175, 0.18, 0.185, 0.188, 0.189, 0.190,
                          0.191, 0.192, 0.193, 0.195, 0.20, 0.205, 0.21])
tau_grid = np.sort(np.unique(np.concatenate([tau_uniform, tau_near_fold])))
N_TAU = len(tau_grid)

print(f"TORSION-52: Analytic torsion on Jensen SU(3)")
print(f"  tau_fold = {TAU_FOLD}")
print(f"  tau grid: {N_TAU} points from {tau_grid[0]:.4f} to {tau_grid[-1]:.4f}")
print(f"  Near-fold points: {len(tau_near_fold)}")

# Peter-Weyl sectors: (p,q) up to p+q <= 3
SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2),
           (3,0), (0,3), (2,1), (1,2)]

def dim_sq(p, q):
    """dim(p,q)^2 = Peter-Weyl degeneracy."""
    d = (p + 1) * (q + 1) * (p + q + 2) // 2
    return d * d


# =============================================================================
# SECTION 1: Build algebra infrastructure (once)
# =============================================================================

print("\n--- Building SU(3) algebra ---")
t0 = time.time()
gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()
print(f"  Algebra built in {time.time()-t0:.2f}s")


# =============================================================================
# SECTION 2: Compute eigenvalues at each tau
# =============================================================================

def compute_all_eigenvalues(tau_val):
    """
    Compute Dirac eigenvalues on all sectors at given tau.

    Returns:
        sector_evals: dict (p,q) -> sorted array of |lambda_k| (positive)
        sector_dims: dict (p,q) -> dim(p,q) (so d_k^2 = dim^2)
    """
    _irrep_cache.clear()  # Clear cache for each tau

    # Build geometric data
    g_s = jensen_metric(B_ab, tau_val)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    sector_evals = {}
    sector_dims = {}

    for (p, q) in SECTORS:
        rho, dim_rho = get_irrep(p, q, gens, f_abc)
        D = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # D is anti-Hermitian: eigenvalues are purely imaginary
        # Make Hermitian: H = i*D, eigenvalues are real
        H = 1j * D
        # Enforce exact Hermiticity
        H = 0.5 * (H + H.conj().T)
        evals = eigvalsh(H)

        # Take absolute values (Dirac |lambda|)
        abs_evals = np.abs(evals)
        # Filter numerical zeros (should not happen for D_K on SU(3))
        abs_evals = abs_evals[abs_evals > 1e-12]
        abs_evals = np.sort(abs_evals)

        sector_evals[(p, q)] = abs_evals
        sector_dims[(p, q)] = dim_rho

    return sector_evals, sector_dims


print("\n--- Computing Dirac spectra across tau grid ---")
all_sector_evals = []
all_sector_dims = []

t_start = time.time()
for i, tau_val in enumerate(tau_grid):
    t_tau = time.time()
    se, sd = compute_all_eigenvalues(tau_val)
    dt = time.time() - t_tau

    # Quick sanity check: count modes
    n_modes = sum(len(se[(p,q)]) for (p,q) in SECTORS)
    n_phys = sum(len(se[(p,q)]) * sd[(p,q)]**2 for (p,q) in SECTORS)

    if i == 0 or i == N_TAU - 1 or abs(tau_val - TAU_FOLD) < 0.002:
        print(f"  tau={tau_val:.4f}: {n_modes} distinct eigenvalues, "
              f"{n_phys} physical modes, dt={dt:.1f}s")

    all_sector_evals.append(se)
    all_sector_dims.append(sd)

total_time = time.time() - t_start
print(f"  Total computation: {total_time:.1f}s ({total_time/N_TAU:.1f}s per tau)")


# =============================================================================
# SECTION 3: Compute torsion invariants
# =============================================================================

print("\n--- Computing torsion invariants ---")

# Storage arrays
singlet_logT = np.zeros(N_TAU)         # log T_singlet = sum ln|lambda_k| over (0,0)
full_logT = np.zeros(N_TAU)            # log T_full = sum d_k^2 ln|lambda_k| over all
zeta_prime_singlet = np.zeros(N_TAU)   # zeta'_singlet(0)
zeta_prime_full = np.zeros(N_TAU)      # zeta'_full(0)
sector_logT = {s: np.zeros(N_TAU) for s in SECTORS}
singlet_logdet = np.zeros(N_TAU)       # log det D_singlet^2

# Additional spectral invariants
zeta_1_singlet = np.zeros(N_TAU)       # zeta(1) = sum 1/lambda_k^2 on singlet
zeta_2_singlet = np.zeros(N_TAU)       # zeta(2) = sum 1/lambda_k^4 on singlet
heat_trace_singlet = np.zeros(N_TAU)   # K(1) = sum exp(-lambda_k^2) on singlet

for i, tau_val in enumerate(tau_grid):
    se = all_sector_evals[i]
    sd = all_sector_dims[i]

    # Singlet torsion: (0,0) sector, d_k = 1
    om_s = se[(0, 0)]
    n_s = len(om_s)
    singlet_logT[i] = np.sum(np.log(om_s))
    zeta_prime_singlet[i] = -2.0 * np.sum(np.log(om_s))
    singlet_logdet[i] = 2.0 * np.sum(np.log(om_s))  # log det D^2 = 2 sum ln|lambda|
    zeta_1_singlet[i] = np.sum(om_s**(-2))
    zeta_2_singlet[i] = np.sum(om_s**(-4))
    heat_trace_singlet[i] = np.sum(np.exp(-om_s**2))

    # Full-spectrum torsion
    for (p, q) in SECTORS:
        om = se[(p, q)]
        d2 = sd[(p, q)]**2  # Peter-Weyl weight
        contribution = d2 * np.sum(np.log(om))
        sector_logT[(p, q)][i] = contribution
        full_logT[i] += contribution

    zeta_prime_full[i] = -2.0 * full_logT[i]


# =============================================================================
# SECTION 4: Analysis -- derivatives, extrema, inflections
# =============================================================================

print("\n--- Analyzing torsion structure ---")

# Numerical derivatives (central differences)
d_singlet = np.gradient(singlet_logT, tau_grid)
d2_singlet = np.gradient(d_singlet, tau_grid)
d_full = np.gradient(full_logT, tau_grid)
d2_full = np.gradient(d_full, tau_grid)

# Find extrema of singlet torsion
sign_changes_d1 = np.where(np.diff(np.sign(d_singlet)))[0]
extrema_tau = tau_grid[sign_changes_d1]
extrema_logT = singlet_logT[sign_changes_d1]

# Find inflection points (sign changes of d2)
sign_changes_d2 = np.where(np.diff(np.sign(d2_singlet)))[0]
inflection_tau = tau_grid[sign_changes_d2]

# Monotonicity check
is_monotone_singlet = len(sign_changes_d1) == 0
is_monotone_full = len(np.where(np.diff(np.sign(d_full)))[0]) == 0

print(f"\n  SINGLET TORSION (16 modes, d_k = 1):")
print(f"    log T_singlet at tau=0.005: {singlet_logT[0]:.8f}")
i_fold = np.argmin(np.abs(tau_grid - TAU_FOLD))
print(f"    log T_singlet at fold (tau={tau_grid[i_fold]:.4f}): {singlet_logT[i_fold]:.8f}")
print(f"    log T_singlet at tau=0.30:  {singlet_logT[-1]:.8f}")
print(f"    T_singlet at fold:  {np.exp(singlet_logT[i_fold]):.6f}")
print(f"    Range: [{singlet_logT.min():.6f}, {singlet_logT.max():.6f}]")
print(f"    Monotone: {is_monotone_singlet}")

if not is_monotone_singlet:
    print(f"    Extrema at tau = {extrema_tau}")
    for idx in sign_changes_d1:
        tau_ex = tau_grid[idx]
        val_ex = singlet_logT[idx]
        typ = "maximum" if d2_singlet[idx] < 0 else "minimum"
        print(f"      tau={tau_ex:.4f}: log T = {val_ex:.6f} ({typ})")

if len(inflection_tau) > 0:
    print(f"    Inflection points at tau = {inflection_tau}")

print(f"\n  FULL-SPECTRUM TORSION ({sum(len(all_sector_evals[0][(p,q)]) for (p,q) in SECTORS)} modes):")
print(f"    log10 T_full at fold: {full_logT[i_fold]/np.log(10):.2f}")
print(f"    Monotone: {is_monotone_full}")

# Sector decomposition at fold
print(f"\n  SECTOR CONTRIBUTIONS AT FOLD (tau={tau_grid[i_fold]:.4f}):")
print(f"    {'Sector':>8s} {'dim':>5s} {'d^2':>6s} {'n_ev':>5s} {'logT_sector':>14s} {'%total':>8s}")
total_at_fold = full_logT[i_fold]
for (p, q) in SECTORS:
    dim_rho = all_sector_dims[i_fold][(p, q)]
    d2 = dim_rho**2
    n_ev = len(all_sector_evals[i_fold][(p, q)])
    lt = sector_logT[(p, q)][i_fold]
    pct = 100.0 * lt / total_at_fold if total_at_fold != 0 else 0
    print(f"    ({p},{q}):  {dim_rho:>5d} {d2:>6d} {n_ev:>5d} {lt:>14.6f} {pct:>7.2f}%")

# Check: which sector(s) drive the tau-variation?
print(f"\n  SECTOR VARIATION (d(logT)/d(tau) at fold):")
for (p, q) in SECTORS:
    d_sector = np.gradient(sector_logT[(p, q)], tau_grid)
    val_at_fold = d_sector[i_fold]
    dim_rho = all_sector_dims[i_fold][(p, q)]
    print(f"    ({p},{q}): d(logT)/dtau = {val_at_fold:>+12.6f}  (dim={dim_rho})")


# =============================================================================
# SECTION 5: Spectral zeta moments
# =============================================================================

print("\n--- Spectral zeta moments (singlet sector) ---")
print(f"  {'tau':>8s} {'zeta(1)':>12s} {'zeta(2)':>12s} {'K(t=1)':>12s} {'logdet':>12s}")
for idx in [0, i_fold, -1]:
    print(f"  {tau_grid[idx]:>8.4f} {zeta_1_singlet[idx]:>12.6f} "
          f"{zeta_2_singlet[idx]:>12.6f} {heat_trace_singlet[idx]:>12.8f} "
          f"{singlet_logdet[idx]:>12.6f}")


# =============================================================================
# SECTION 6: Relative torsion (fold / round)
# =============================================================================

print("\n--- Relative torsion: T(tau)/T(tau_min) ---")
ref_idx = 0  # tau ~ 0.005
rel_singlet = singlet_logT - singlet_logT[ref_idx]
rel_full = full_logT - full_logT[ref_idx]
print(f"  Singlet: log[T(fold)/T(ref)] = {rel_singlet[i_fold]:.8f}")
print(f"  Full:    log[T(fold)/T(ref)] = {rel_full[i_fold]:.4f}")
print(f"  Singlet relative variation: {(singlet_logT.max()-singlet_logT.min())/np.abs(singlet_logT.mean())*100:.3f}%")


# =============================================================================
# SECTION 7: Gate Verdict
# =============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: TORSION-52")
print("=" * 78)

has_extremum = not is_monotone_singlet
has_inflection = len(inflection_tau) > 0
has_discontinuity = False  # Not expected for smooth deformation

# Check for nontrivial structure near fold
near_fold_mask = np.abs(tau_grid - TAU_FOLD) < 0.03
if np.any(near_fold_mask):
    d2_near_fold = d2_singlet[near_fold_mask]
    has_curvature_change = np.any(np.diff(np.sign(d2_near_fold)) != 0)
else:
    has_curvature_change = False

if has_extremum:
    verdict = "PASS"
    reason = f"Extremum in singlet torsion at tau = {extrema_tau}"
elif has_inflection and np.any(np.abs(inflection_tau - TAU_FOLD) < 0.05):
    verdict = "PASS"
    reason = f"Inflection in singlet torsion near fold at tau = {inflection_tau}"
elif has_curvature_change:
    verdict = "PASS (THIN)"
    reason = f"Curvature change near fold in singlet torsion"
else:
    verdict = "INFO"
    reason = "Singlet torsion is monotone with no inflection near fold"

print(f"\n  Verdict: {verdict}")
print(f"  Reason:  {reason}")
print(f"  Singlet monotone: {is_monotone_singlet}")
print(f"  Full monotone:    {is_monotone_full}")
print(f"  Extrema:          {len(sign_changes_d1)}")
print(f"  Inflections:      {len(sign_changes_d2)}")
if has_inflection:
    print(f"  Nearest inflection to fold: tau = {inflection_tau[np.argmin(np.abs(inflection_tau - TAU_FOLD))]:.4f}")


# =============================================================================
# SECTION 8: Save data
# =============================================================================

out_data = {
    'tau_grid': tau_grid,
    'tau_fold': TAU_FOLD,
    'n_tau': N_TAU,
    'singlet_logT': singlet_logT,
    'full_logT': full_logT,
    'zeta_prime_singlet': zeta_prime_singlet,
    'zeta_prime_full': zeta_prime_full,
    'singlet_logdet': singlet_logdet,
    'zeta_1_singlet': zeta_1_singlet,
    'zeta_2_singlet': zeta_2_singlet,
    'heat_trace_singlet': heat_trace_singlet,
    'd_singlet_dtau': d_singlet,
    'd2_singlet_dtau2': d2_singlet,
    'd_full_dtau': d_full,
    'd2_full_dtau2': d2_full,
    'rel_singlet': rel_singlet,
    'rel_full': rel_full,
    'verdict': np.array(verdict),
    'reason': np.array(reason),
    'is_monotone_singlet': np.array(is_monotone_singlet),
    'is_monotone_full': np.array(is_monotone_full),
}

# Per-sector data
for (p, q) in SECTORS:
    out_data[f'sector_{p}_{q}_logT'] = sector_logT[(p, q)]
    # Store eigenvalues at fold
    out_data[f'evals_fold_{p}_{q}'] = all_sector_evals[i_fold][(p, q)]

out_path = os.path.join(SCRIPT_DIR, 's52_analytic_torsion.npz')
np.savez_compressed(out_path, **out_data)
print(f"\n  Saved: {out_path}")


# =============================================================================
# SECTION 9: Plots
# =============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('TORSION-52: Analytic Torsion on Jensen SU(3)', fontsize=14, fontweight='bold')

# --- Panel (0,0): Singlet log T vs tau ---
ax = axes[0, 0]
ax.plot(tau_grid, singlet_logT, 'b-', linewidth=2, label='log T_singlet')
ax.axvline(TAU_FOLD, color='red', linestyle='--', alpha=0.7, label=f'fold (tau={TAU_FOLD})')
if has_extremum:
    for idx in sign_changes_d1:
        ax.plot(tau_grid[idx], singlet_logT[idx], 'ro', markersize=10, zorder=5)
if has_inflection:
    for idx in sign_changes_d2:
        ax.plot(tau_grid[idx], singlet_logT[idx], 'g^', markersize=8, zorder=5)
ax.set_xlabel('tau')
ax.set_ylabel('log T_singlet')
ax.set_title('Singlet Torsion (16 modes)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (0,1): d(logT)/dtau ---
ax = axes[0, 1]
ax.plot(tau_grid, d_singlet, 'b-', linewidth=2, label="d(log T)/d(tau)")
ax.axhline(0, color='gray', linestyle='-', alpha=0.5)
ax.axvline(TAU_FOLD, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel("d(log T)/d(tau)")
ax.set_title('First Derivative (singlet)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (0,2): d^2(logT)/dtau^2 ---
ax = axes[0, 2]
ax.plot(tau_grid, d2_singlet, 'b-', linewidth=2, label="d^2(log T)/d(tau)^2")
ax.axhline(0, color='gray', linestyle='-', alpha=0.5)
ax.axvline(TAU_FOLD, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel("d^2(log T)/d(tau)^2")
ax.set_title('Second Derivative (singlet)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (1,0): Full-spectrum log10 T ---
ax = axes[1, 0]
ax.plot(tau_grid, full_logT / np.log(10), 'r-', linewidth=2)
ax.axvline(TAU_FOLD, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel('log10 T_full')
ax.set_title('Full-Spectrum Torsion (PW weighted)')
ax.grid(True, alpha=0.3)

# --- Panel (1,1): Sector decomposition at tau ---
ax = axes[1, 1]
colors = plt.cm.tab10(np.linspace(0, 1, len(SECTORS)))
for j, (p, q) in enumerate(SECTORS):
    ax.plot(tau_grid, sector_logT[(p, q)], '-', color=colors[j],
            linewidth=1.5, label=f'({p},{q})')
ax.axvline(TAU_FOLD, color='red', linestyle='--', alpha=0.7)
ax.set_xlabel('tau')
ax.set_ylabel('logT contribution')
ax.set_title('Per-Sector Torsion')
ax.legend(fontsize=7, ncol=2, loc='upper left')
ax.grid(True, alpha=0.3)

# --- Panel (1,2): T_singlet vs tau (exp scale) ---
ax = axes[1, 2]
T_singlet_vals = np.exp(singlet_logT)
ax.plot(tau_grid, T_singlet_vals, 'b-', linewidth=2)
ax.axvline(TAU_FOLD, color='red', linestyle='--', alpha=0.7, label=f'fold')
ax.set_xlabel('tau')
ax.set_ylabel('T_singlet')
ax.set_title('Singlet Torsion (linear scale)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's52_analytic_torsion.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved: {plot_path}")

print(f"\nDone. Total wall time: {time.time()-t_start:.1f}s")
