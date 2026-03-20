"""
Session 28a Computation L-1: Thermal Spectral Action
=====================================================

Evaluates the finite-temperature spectral action (free energy) using the
existing Dirac eigenvalue data. The perturbative spectral action S[D, f, Lambda]
is a T=0 quantity. The thermal version introduces a Boltzmann weight that
suppresses high modes, potentially breaking the Seeley-DeWitt monotonicity
and generating a tau minimum.

Physics:
--------
The Dirac operator D_K has a spectrum {lambda_n(tau)} that evolves with the
Jensen deformation. At finite temperature T, the fermionic free energy is:

    F(tau; T) = -T * sum_n ln(1 + exp(-|lambda_n(tau)| / T))

This is the standard fermionic grand canonical potential at zero chemical
potential. The factor T out front and the Fermi-Dirac weight 1/(1+exp(E/T))
suppress high modes exponentially, breaking the UV-dominated monotonicity
of the T=0 spectral action.

At low T (T << lambda_min), F ~ -T * N_modes * exp(-lambda_min/T) -- dominated
by the spectral gap. Modes with |lambda| >> T are frozen out.

At high T (T >> lambda_max), F ~ -T * N_modes * ln(2) -- all modes contribute
equally, and the free energy is proportional to the total DOF (tau-independent
if volume-preserving deformation does not change total mode count at fixed cutoff).

The interesting regime is T ~ O(lambda_min) where the Fermi-Dirac weight
selectively enhances modes near the gap edge, potentially creating a
non-monotonic F(tau; T) profile.

We also compute the bosonic version for comparison:
    F_bos(tau; T) = +T * sum_n ln(1 - exp(-|lambda_n(tau)| / T))

(Note: bosonic partition function requires |lambda| > 0 for all modes.)

Input: tier0-computation/s19a_sweep_data.npz (full spectrum at 21 tau values)
       tier0-computation/s27_multisector_bcs.npz (eigenvalues per sector)
Output: tier0-computation/s28a_thermal_spectral_action.npz
        tier0-computation/s28a_thermal_spectral_action.png

Gate L-1:
    PASS: F(tau; T) has a minimum at tau > 0 for some T -- thermal stabilization exists
    CLOSED: F(tau; T) monotonically decreasing at all T -- thermal correction does not help
    INCONCLUSIVE: Minimum exists but is shallow (F'' < 0.01)

Author: phonon-exflation-sim agent
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
INPUT_S19A = DATA_DIR / "s19a_sweep_data.npz"
INPUT_S27 = DATA_DIR / "s27_multisector_bcs.npz"
OUTPUT_NPZ = DATA_DIR / "s28a_thermal_spectral_action.npz"
OUTPUT_PNG = DATA_DIR / "s28a_thermal_spectral_action.png"

# Temperature values (in units of lambda_min(0))
# lambda_min(0) ~ 0.833 (from s19a data inspection)
T_VALUES_RELATIVE = np.array([0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0])

# Gate thresholds
F_CURVATURE_THRESHOLD = 0.01  # minimum F'' for PASS vs INCONCLUSIVE

# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("L-1: Thermal Spectral Action F(tau; T)")
print("=" * 72)

# Primary data: s19a (21 tau values, full spectrum)
data_s19a = np.load(INPUT_S19A, allow_pickle=True)
tau_values = data_s19a['tau_values']  # 21 values
n_tau = len(tau_values)

# Build eigenvalue array with multiplicities
print(f"Loading eigenvalues at {n_tau} tau values...")
n_modes = data_s19a['eigenvalues_0'].shape[0]

eigenvalues_all = np.zeros((n_tau, n_modes))
multiplicities_all = np.zeros((n_tau, n_modes), dtype=np.int32)
sector_p_all = np.zeros((n_tau, n_modes), dtype=np.int32)
sector_q_all = np.zeros((n_tau, n_modes), dtype=np.int32)

for i in range(n_tau):
    eigenvalues_all[i] = data_s19a[f'eigenvalues_{i}']
    multiplicities_all[i] = data_s19a[f'multiplicities_{i}']
    sector_p_all[i] = data_s19a[f'sector_p_{i}']
    sector_q_all[i] = data_s19a[f'sector_q_{i}']

omega_all = np.abs(eigenvalues_all)  # mode frequencies

# Reference lambda_min at tau=0
lambda_min_0 = np.min(omega_all[0, omega_all[0] > 1e-6])
print(f"lambda_min(tau=0) = {lambda_min_0:.6f}")

# Absolute temperature values
T_values = T_VALUES_RELATIVE * lambda_min_0
print(f"Temperature scan: T/lambda_min(0) = {T_VALUES_RELATIVE}")
print(f"Absolute T values: {T_values}")
n_T = len(T_values)

# Also load s27 data for per-sector analysis
data_s27 = np.load(INPUT_S27, allow_pickle=True)
tau_s27 = data_s27['tau_values']  # 9 values
sectors_s27 = data_s27['sectors']  # (9, 4) = (p, q, dim, mult)
print(f"\nS27 data: {len(tau_s27)} tau values, {len(sectors_s27)} sectors")

# ==============================================================================
# Compute fermionic free energy
# ==============================================================================

print("\nComputing fermionic free energy F_ferm(tau; T)...")
print("  F(tau; T) = -T * sum_n mult_n * ln(1 + exp(-|lambda_n| / T))")

F_ferm = np.zeros((n_tau, n_T))

for j, T in enumerate(T_values):
    for i in range(n_tau):
        # F = -T * sum_n mult_n * ln(1 + exp(-omega_n / T))
        # Use log1p for numerical stability: ln(1 + x) = log1p(x)
        x = omega_all[i] / T
        # For large x, exp(-x) is tiny; for small x, ln(1+exp(-x)) ~ ln(2) - x/2
        # Use: ln(1 + exp(-x)) = ln(1 + exp(-x))
        # Stable computation: for x > 50, ln(1 + exp(-x)) ~ exp(-x)
        ln_terms = np.where(x > 50,
                            np.exp(-x),
                            np.log1p(np.exp(-x)))
        F_ferm[i, j] = -T * np.sum(multiplicities_all[i] * ln_terms)

print("  Done.")

# ==============================================================================
# Compute bosonic free energy (for comparison)
# ==============================================================================

print("\nComputing bosonic free energy F_bos(tau; T)...")
print("  F_bos(tau; T) = +T * sum_n mult_n * ln(1 - exp(-|lambda_n| / T))")

F_bos = np.zeros((n_tau, n_T))

for j, T in enumerate(T_values):
    for i in range(n_tau):
        x = omega_all[i] / T
        # ln(1 - exp(-x)) is negative for x > 0
        # For large x: ln(1 - exp(-x)) ~ -exp(-x)
        # For small x: diverges as ln(x) -- need x > 0 strictly
        # Stable: use log1p(-exp(-x)) = log1p(-exp(-x))
        exp_neg_x = np.exp(-np.minimum(x, 700))  # clip to prevent underflow warnings
        ln_terms = np.where(x > 50,
                            -exp_neg_x,
                            np.log1p(-exp_neg_x))
        # Check for any x = 0 (zero modes) -- these would diverge
        bad = x < 1e-10
        if np.any(bad):
            ln_terms[bad] = 0  # exclude zero modes from bosonic sum
        F_bos[i, j] = T * np.sum(multiplicities_all[i] * ln_terms)

print("  Done.")

# ==============================================================================
# Combined free energy: F_total = F_bos + F_ferm
# ==============================================================================

# In the full KK tower, there are both bosonic and fermionic DOF.
# From Session 18: 52,556 bosonic vs 439,488 fermionic DOF at mps=5.
# But the eigenvalue data here is from the DIRAC spectrum only (fermionic).
# The bosonic spectrum comes from the Laplacian on different bundles.
#
# For this computation, we evaluate F_ferm and F_bos SEPARATELY as functions
# of the SAME Dirac eigenvalues, to see if EITHER partition function
# produces a minimum. This is physically motivated:
# - F_ferm uses the Dirac spectrum with Fermi-Dirac statistics
# - F_bos uses the same eigenvalue MAGNITUDES as boson frequencies

F_total = F_ferm + F_bos

print("\n--- Free energy summary ---")
for j, T in enumerate(T_values):
    T_rel = T / lambda_min_0
    print(f"  T/lam_min = {T_rel:.1f}: F_ferm range [{F_ferm[:, j].min():.4f}, "
          f"{F_ferm[:, j].max():.4f}], "
          f"F_bos range [{F_bos[:, j].min():.4f}, {F_bos[:, j].max():.4f}]")

# ==============================================================================
# Check for non-monotonicity in F_ferm
# ==============================================================================

print("\n--- Monotonicity analysis: F_ferm ---")

# For each T, check if F has an interior minimum at tau > 0
ferm_minima = {}
for j, T in enumerate(T_values):
    T_rel = T / lambda_min_0
    F_j = F_ferm[:, j]

    # Compute finite-difference derivative
    dF = np.diff(F_j) / np.diff(tau_values)

    # Look for sign changes in dF (negative to positive = minimum)
    sign_changes = []
    for k in range(len(dF) - 1):
        if dF[k] < 0 and dF[k + 1] > 0:
            # Interpolate to find zero crossing
            tau_min = tau_values[k + 1] + dF[k] / (dF[k] - dF[k + 1]) * (tau_values[k + 2] - tau_values[k + 1])
            F_min = F_j[k + 1]  # approximate
            sign_changes.append((tau_min, F_min, k + 1))

    if sign_changes:
        for tau_min, F_min, idx in sign_changes:
            # Estimate curvature (second derivative)
            if 1 <= idx <= n_tau - 2:
                dtau = tau_values[1] - tau_values[0]
                F_pp = (F_j[idx + 1] - 2 * F_j[idx] + F_j[idx - 1]) / dtau**2
            else:
                F_pp = 0.0
            ferm_minima[T_rel] = (tau_min, F_min, F_pp)
            print(f"  T/lam_min = {T_rel:.1f}: MINIMUM at tau ~ {tau_min:.3f}, "
                  f"F = {F_min:.6f}, F'' = {F_pp:.6f}")
    else:
        # Check if monotonically increasing or decreasing
        if np.all(dF >= -1e-10):
            trend = "INCREASING"
        elif np.all(dF <= 1e-10):
            trend = "DECREASING"
        else:
            trend = "MIXED (no clear minimum)"
        print(f"  T/lam_min = {T_rel:.1f}: {trend}, "
              f"F(0)={F_j[0]:.4f}, F(2)={F_j[-1]:.4f}, "
              f"dF range=[{dF.min():.4e}, {dF.max():.4e}]")

# ==============================================================================
# Check for non-monotonicity in F_bos
# ==============================================================================

print("\n--- Monotonicity analysis: F_bos ---")

bos_minima = {}
for j, T in enumerate(T_values):
    T_rel = T / lambda_min_0
    F_j = F_bos[:, j]

    dF = np.diff(F_j) / np.diff(tau_values)

    sign_changes = []
    for k in range(len(dF) - 1):
        if dF[k] < 0 and dF[k + 1] > 0:
            tau_min = tau_values[k + 1] + dF[k] / (dF[k] - dF[k + 1]) * (tau_values[k + 2] - tau_values[k + 1])
            F_min = F_j[k + 1]
            sign_changes.append((tau_min, F_min, k + 1))

    if sign_changes:
        for tau_min, F_min, idx in sign_changes:
            if 1 <= idx <= n_tau - 2:
                dtau = tau_values[1] - tau_values[0]
                F_pp = (F_j[idx + 1] - 2 * F_j[idx] + F_j[idx - 1]) / dtau**2
            else:
                F_pp = 0.0
            bos_minima[T_rel] = (tau_min, F_min, F_pp)
            print(f"  T/lam_min = {T_rel:.1f}: MINIMUM at tau ~ {tau_min:.3f}, "
                  f"F = {F_min:.6f}, F'' = {F_pp:.6f}")
    else:
        if np.all(dF >= -1e-10):
            trend = "INCREASING"
        elif np.all(dF <= 1e-10):
            trend = "DECREASING"
        else:
            trend = "MIXED (no clear minimum)"
        print(f"  T/lam_min = {T_rel:.1f}: {trend}, "
              f"F(0)={F_j[0]:.4f}, F(2)={F_j[-1]:.4f}, "
              f"dF range=[{dF.min():.4e}, {dF.max():.4e}]")

# ==============================================================================
# Check for non-monotonicity in F_total = F_ferm + F_bos
# ==============================================================================

print("\n--- Monotonicity analysis: F_total = F_ferm + F_bos ---")

total_minima = {}
for j, T in enumerate(T_values):
    T_rel = T / lambda_min_0
    F_j = F_total[:, j]

    dF = np.diff(F_j) / np.diff(tau_values)

    sign_changes = []
    for k in range(len(dF) - 1):
        if dF[k] < 0 and dF[k + 1] > 0:
            tau_min = tau_values[k + 1] + dF[k] / (dF[k] - dF[k + 1]) * (tau_values[k + 2] - tau_values[k + 1])
            F_min = F_j[k + 1]
            sign_changes.append((tau_min, F_min, k + 1))

    if sign_changes:
        for tau_min, F_min, idx in sign_changes:
            if 1 <= idx <= n_tau - 2:
                dtau = tau_values[1] - tau_values[0]
                F_pp = (F_j[idx + 1] - 2 * F_j[idx] + F_j[idx - 1]) / dtau**2
            else:
                F_pp = 0.0
            total_minima[T_rel] = (tau_min, F_min, F_pp)
            print(f"  T/lam_min = {T_rel:.1f}: MINIMUM at tau ~ {tau_min:.3f}, "
                  f"F = {F_min:.6f}, F'' = {F_pp:.6f}")
    else:
        if np.all(dF >= -1e-10):
            trend = "INCREASING"
        elif np.all(dF <= 1e-10):
            trend = "DECREASING"
        else:
            trend = "MIXED (no clear minimum)"
        print(f"  T/lam_min = {T_rel:.1f}: {trend}, "
              f"F(0)={F_j[0]:.4f}, F(2)={F_j[-1]:.4f}, "
              f"dF range=[{dF.min():.4e}, {dF.max():.4e}]")

# ==============================================================================
# Per-sector analysis using s27 data (finer tau grid in [0, 0.5])
# ==============================================================================

print("\n--- Per-sector thermal free energy (s27 data, tau in [0, 0.5]) ---")

# For select sectors, compute F_ferm at T = lambda_min(0)
T_mid = lambda_min_0  # T = lambda_min(0)
sector_names = []
F_sector_ferm = {}

for s_idx in range(len(sectors_s27)):
    p, q = int(sectors_s27[s_idx, 0]), int(sectors_s27[s_idx, 1])
    dim_pq = int(sectors_s27[s_idx, 2])
    mult_pq = int(sectors_s27[s_idx, 3])
    sector_name = f"({p},{q})"
    sector_names.append(sector_name)

    F_sec = np.zeros(len(tau_s27))
    for ti in range(len(tau_s27)):
        key = f'evals_{p}_{q}_{ti}'
        if key in data_s27:
            evals_sec = np.abs(data_s27[key])
            x = evals_sec / T_mid
            ln_terms = np.where(x > 50, np.exp(-x), np.log1p(np.exp(-x)))
            # Multiply by Peter-Weyl multiplicity: dim(p,q)^2
            F_sec[ti] = -T_mid * mult_pq * np.sum(ln_terms)
        else:
            F_sec[ti] = np.nan

    F_sector_ferm[sector_name] = F_sec

    # Check for minimum
    valid = ~np.isnan(F_sec)
    if np.sum(valid) >= 3:
        F_valid = F_sec[valid]
        tau_valid = tau_s27[valid]
        dF = np.diff(F_valid)
        min_idx = np.argmin(F_valid)
        is_interior_min = (0 < min_idx < len(F_valid) - 1)
        print(f"  {sector_name}: F range [{F_valid.min():.4f}, {F_valid.max():.4f}], "
              f"min at tau={tau_valid[min_idx]:.2f} "
              f"{'(INTERIOR)' if is_interior_min else '(boundary)'}")

# ==============================================================================
# Entropy and specific heat
# ==============================================================================

print("\n--- Entropy S = -dF/dT and specific heat C = -T d^2F/dT^2 ---")

# Compute entropy by finite difference in T
S_ferm = np.zeros((n_tau, n_T))
for i in range(n_tau):
    for j in range(1, n_T - 1):
        dT = T_values[j + 1] - T_values[j - 1]
        S_ferm[i, j] = -(F_ferm[i, j + 1] - F_ferm[i, j - 1]) / dT
    # Boundaries
    S_ferm[i, 0] = -(F_ferm[i, 1] - F_ferm[i, 0]) / (T_values[1] - T_values[0])
    S_ferm[i, -1] = -(F_ferm[i, -1] - F_ferm[i, -2]) / (T_values[-1] - T_values[-2])

# Specific heat
C_ferm = np.zeros((n_tau, n_T))
for i in range(n_tau):
    for j in range(1, n_T - 1):
        dT = T_values[j + 1] - T_values[j - 1]
        C_ferm[i, j] = T_values[j] * (S_ferm[i, j + 1] - S_ferm[i, j - 1]) / dT
    C_ferm[i, 0] = 0  # approximate
    C_ferm[i, -1] = 0

# ==============================================================================
# Gate verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE L-1 VERDICT")
print("=" * 72)

any_ferm_minimum = len(ferm_minima) > 0
any_bos_minimum = len(bos_minima) > 0
any_total_minimum = len(total_minima) > 0

print(f"\nFermionic minima found: {len(ferm_minima)}")
for T_rel, (tau_min, F_min, F_pp) in sorted(ferm_minima.items()):
    print(f"  T/lam_min = {T_rel:.1f}: tau_min = {tau_min:.3f}, F'' = {F_pp:.6f}")

print(f"Bosonic minima found: {len(bos_minima)}")
for T_rel, (tau_min, F_min, F_pp) in sorted(bos_minima.items()):
    print(f"  T/lam_min = {T_rel:.1f}: tau_min = {tau_min:.3f}, F'' = {F_pp:.6f}")

print(f"Total (F+B) minima found: {len(total_minima)}")
for T_rel, (tau_min, F_min, F_pp) in sorted(total_minima.items()):
    print(f"  T/lam_min = {T_rel:.1f}: tau_min = {tau_min:.3f}, F'' = {F_pp:.6f}")

# Determine verdict
if any_ferm_minimum or any_bos_minimum or any_total_minimum:
    # Check curvature at the deepest minimum
    all_minima = {}
    all_minima.update({('ferm', k): v for k, v in ferm_minima.items()})
    all_minima.update({('bos', k): v for k, v in bos_minima.items()})
    all_minima.update({('total', k): v for k, v in total_minima.items()})

    max_Fpp = max(abs(v[2]) for v in all_minima.values())

    if max_Fpp > F_CURVATURE_THRESHOLD:
        verdict = "PASS"
        print(f"\nVERDICT: **PASS** -- thermal minimum found with |F''| = {max_Fpp:.4e} > {F_CURVATURE_THRESHOLD}")
    else:
        verdict = "INCONCLUSIVE"
        print(f"\nVERDICT: **INCONCLUSIVE** -- minimum found but shallow, |F''| = {max_Fpp:.4e}")
else:
    verdict = "CLOSED"
    print(f"\nVERDICT: **CLOSED** -- F(tau; T) monotonic at ALL temperatures scanned")
    print("  No thermal stabilization of the Jensen deformation")

print(f"\nPhysical note: T is measured in units of the KK scale.")
print(f"  T ~ lambda_min(0) = {lambda_min_0:.4f} corresponds to the spectral gap.")
print(f"  Physical T >> M_KK would be T >> 10^16 GeV (Planck epoch relevant).")

# ==============================================================================
# Save data
# ==============================================================================

save_dict = dict(
    tau_values=tau_values,
    T_values=T_values,
    T_relative=T_VALUES_RELATIVE,
    lambda_min_0=np.array([lambda_min_0]),
    F_ferm=F_ferm,
    F_bos=F_bos,
    F_total=F_total,
    S_ferm=S_ferm,
    C_ferm=C_ferm,
    verdict=np.array([verdict]),
)

# Add per-sector data
for name, F_sec in F_sector_ferm.items():
    save_dict[f'F_sector_{name}'] = F_sec
save_dict['tau_s27'] = tau_s27
save_dict['sector_names'] = np.array(sector_names)

np.savez_compressed(OUTPUT_NPZ, **save_dict)
print(f"\nSaved: {OUTPUT_NPZ}")

# ==============================================================================
# Plotting
# ==============================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("L-1: Thermal Spectral Action F(tau; T)", fontsize=14, fontweight='bold')

# --- Panel 1: F_ferm vs tau at multiple T ---
ax = axes[0, 0]
colors = plt.cm.coolwarm(np.linspace(0, 1, n_T))
for j in range(n_T):
    T_rel = T_VALUES_RELATIVE[j]
    F_norm = F_ferm[:, j] / np.abs(F_ferm[0, j]) if F_ferm[0, j] != 0 else F_ferm[:, j]
    ax.plot(tau_values, F_norm, '-', color=colors[j], lw=1.5,
            label=f'T/{lambda_min_0:.2f}={T_rel:.1f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$F_{\rm ferm}(\tau) / |F_{\rm ferm}(0)|$')
ax.set_title('Fermionic Free Energy (normalized)')
ax.legend(fontsize=6, ncol=2)
ax.grid(True, alpha=0.3)

# --- Panel 2: F_bos vs tau at multiple T ---
ax = axes[0, 1]
for j in range(n_T):
    T_rel = T_VALUES_RELATIVE[j]
    F_norm = F_bos[:, j] / np.abs(F_bos[0, j]) if F_bos[0, j] != 0 else F_bos[:, j]
    ax.plot(tau_values, F_norm, '-', color=colors[j], lw=1.5,
            label=f'T/lam={T_rel:.1f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$F_{\rm bos}(\tau) / |F_{\rm bos}(0)|$')
ax.set_title('Bosonic Free Energy (normalized)')
ax.legend(fontsize=6, ncol=2)
ax.grid(True, alpha=0.3)

# --- Panel 3: F_total vs tau ---
ax = axes[0, 2]
for j in range(n_T):
    T_rel = T_VALUES_RELATIVE[j]
    F_norm = F_total[:, j] / np.abs(F_total[0, j]) if F_total[0, j] != 0 else F_total[:, j]
    ax.plot(tau_values, F_norm, '-', color=colors[j], lw=1.5,
            label=f'T/lam={T_rel:.1f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$F_{\rm total}(\tau) / |F_{\rm total}(0)|$')
ax.set_title('Total Free Energy (F+B)')
ax.legend(fontsize=6, ncol=2)
ax.grid(True, alpha=0.3)

# --- Panel 4: dF/dtau for fermionic at key temperatures ---
ax = axes[1, 0]
dtau = tau_values[1] - tau_values[0]
for j in [0, 2, 4, 6, 8]:  # T/lam = 0.1, 0.5, 1.0, 2.0, 5.0
    T_rel = T_VALUES_RELATIVE[j]
    dF = np.gradient(F_ferm[:, j], tau_values)
    ax.plot(tau_values, dF, '-', color=colors[j], lw=1.5,
            label=f'T/lam={T_rel:.1f}')
ax.axhline(0, color='k', ls='--', lw=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$dF_{\rm ferm}/d\tau$')
ax.set_title(r'$dF_{\rm ferm}/d\tau$ (zero crossing = minimum)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# --- Panel 5: Per-sector F at T = lambda_min ---
ax = axes[1, 1]
for s_name, F_sec in F_sector_ferm.items():
    valid = ~np.isnan(F_sec)
    if np.sum(valid) >= 2:
        F_norm = F_sec[valid] / np.abs(F_sec[valid][0]) if F_sec[valid][0] != 0 else F_sec[valid]
        ax.plot(tau_s27[valid], F_norm, '-o', markersize=3, label=s_name)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$F_{\rm sector} / |F_{\rm sector}(0)|$')
ax.set_title(f'Per-sector $F_{{\\rm ferm}}$ at T = $\\lambda_{{\\rm min}}$')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# --- Panel 6: Entropy vs tau at key temperatures ---
ax = axes[1, 2]
for j in [0, 2, 4, 6, 8]:
    T_rel = T_VALUES_RELATIVE[j]
    ax.plot(tau_values, S_ferm[:, j], '-', color=colors[j], lw=1.5,
            label=f'T/lam={T_rel:.1f}')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S(\tau, T) = -dF/dT$')
ax.set_title('Entropy')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved: {OUTPUT_PNG}")

print("\nDone.")
