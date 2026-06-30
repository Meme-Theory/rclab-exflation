#!/usr/bin/env python3
"""
s63_debye_fold.py — DEBYE-FOLD-63 (W5-05)
==========================================

Compute effective Debye temperature theta_D = hbar*omega_max/k_B from KK spectrum.
Compare to T_GGE = 0.386 M_KK. Classify Debye vs classical regime.
Compute heat capacity C_V(T_GGE) from exact spectral sum (Einstein-mode sum)
and from the Debye model.

Gate: INFO (regime classification).

Input:  s62_cutoff_london.npz, s62_meissner_gge.npz, s61_weyl_law.npz, s44_dos_tau.npz
Output: s63_debye_fold.npz + s63_debye_fold.png
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    T_acoustic, E_cond, PI,
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    k_B, hbar_SI, k_B_SI,
    E_B1, E_B2_mean, E_B3_mean,
)

SCRIPT = os.path.basename(__file__)
OUT_NPZ = os.path.join(os.path.dirname(__file__), 's63_debye_fold.npz')
OUT_PNG = os.path.join(os.path.dirname(__file__), 's63_debye_fold.png')

# =============================================================================
#  1. Load KK spectrum data
# =============================================================================

data_weyl = np.load(os.path.join(os.path.dirname(__file__),
                    's61_weyl_law.npz'), allow_pickle=True)
omega_all = data_weyl['omega_sorted']      # |D_K| eigenvalues, shape (18624,)
pw_mult = data_weyl['pw_mult_sorted']      # PW multiplicities

data_dos = np.load(os.path.join(os.path.dirname(__file__),
                   's44_dos_tau.npz'), allow_pickle=True)
omega_fold = data_dos['tau0.19_all_omega']   # eigenvalues at tau=0.19
dim2_fold = data_dos['tau0.19_all_dim2']     # dim(p,q)^2 multiplicities

data_meissner = np.load(os.path.join(os.path.dirname(__file__),
                        's62_meissner_gge.npz'), allow_pickle=True)
T_GGE = float(data_meissner['T_GGE_eff'])   # 0.386 M_KK

data_cutoff = np.load(os.path.join(os.path.dirname(__file__),
                      's62_cutoff_london.npz'), allow_pickle=True)

print(f"[{SCRIPT}] Loaded spectrum: {len(omega_all)} bare eigenvalues (s61 Weyl)")
print(f"  omega range: [{omega_all.min():.6f}, {omega_all.max():.6f}] M_KK")
print(f"  Total PW states: {pw_mult.sum():.0f}")
print(f"  T_GGE = {T_GGE:.6f} M_KK")
print()

# =============================================================================
#  2. Define Debye temperature(s)
# =============================================================================
#
# The KK spectrum on Jensen-deformed SU(3) is BOUNDED — it lives in a finite
# Brillouin zone analog. Unlike a crystal with ~10^23 modes, we have a
# discrete finite set of eigenvalues.
#
# There are multiple natural definitions of omega_max:
#
# (a) omega_max_PW: highest eigenvalue in the PW truncation (3.549 M_KK)
#     This is an artifact of the truncation — the true manifold has infinitely
#     many eigenvalues. But the spectral action cutoff renders modes above
#     ~Lambda_cutoff irrelevant.
#
# (b) omega_max_fold: highest eigenvalue at tau=0.19 from s44 data (2.061 M_KK)
#     This is a different PW truncation (max_pq=6).
#
# (c) omega_cutoff: the spectral action cutoff ~1/gamma_opt.
#     Gaussian: 1/0.488 = 2.048 M_KK. Exponential: 1/0.345 = 2.897 M_KK.
#     This is the PHYSICAL cutoff — modes above this are exponentially suppressed.
#
# (d) omega_max_BCS: the highest BCS mode energy (~E_B3_mean = 0.978 M_KK)
#     Relevant for the 8-mode BCS sector, not the full KK tower.
#
# The Debye model applies to ACOUSTIC branches. In the phonon-exflation framework,
# the KK eigenvalues are the "acoustic" modes of the internal geometry.
# The Debye cutoff is set by matching the total number of modes:
#   N_modes = integral_0^{omega_D} g(omega) d(omega)
# For a bounded spectrum, omega_D = omega_max (the Debye model IS the spectrum).
#
# In natural units where hbar=k_B=1, theta_D = omega_max.
# In M_KK units: theta_D/M_KK = omega_max/M_KK (dimensionless).

# Definition (a): full PW truncation maximum
omega_max_pw = omega_all.max()

# Definition (b): fold-specific (max_pq=6 truncation)
omega_max_fold = omega_fold.max()

# Definition (c): spectral action cutoff (Gaussian, which passed)
gamma_gauss = float(data_cutoff['Gaussian_gamma_opt'])
omega_cutoff_gauss = 1.0 / gamma_gauss  # = 2.048 M_KK

# Definition (d): BCS sector maximum
omega_max_bcs = max(E_B1, E_B2_mean, E_B3_mean)  # 0.978 M_KK

# The PHYSICAL Debye temperature should use the spectral action cutoff.
# Modes above this scale are exponentially damped. The cutoff sets the
# effective "zone boundary."
omega_D = omega_cutoff_gauss  # = 2.048 M_KK (Gaussian)
theta_D = omega_D             # In units where hbar = k_B = 1 = M_KK

print("=" * 60)
print("Debye temperature definitions (all in M_KK units)")
print("=" * 60)
print(f"  (a) omega_max (full PW):      {omega_max_pw:.4f} M_KK")
print(f"  (b) omega_max (fold, pq<=6):  {omega_max_fold:.4f} M_KK")
print(f"  (c) omega_cutoff (Gaussian):  {omega_cutoff_gauss:.4f} M_KK  <-- PHYSICAL")
print(f"  (d) omega_max (BCS sector):   {omega_max_bcs:.4f} M_KK")
print(f"  theta_D (physical) = {theta_D:.4f} M_KK")
print(f"  T_GGE             = {T_GGE:.4f} M_KK")
print(f"  theta_D / T_GGE   = {theta_D / T_GGE:.4f}")
print()

# =============================================================================
#  3. Regime classification
# =============================================================================
#
# Debye classification:
#   T >> theta_D:  classical (Dulong-Petit), C_V -> 3N k_B
#   T << theta_D:  quantum (T^3 law), C_V ~ (12/5) pi^4 N k_B (T/theta_D)^3
#   T ~ theta_D:   intermediate
#
# Our case: theta_D/T_GGE ~ 5.3, so T_GGE < theta_D by a factor ~5.
# This puts us in the QUANTUM regime, but not deeply.
# The Debye function D_3(theta_D/T) will be needed.

ratio = theta_D / T_GGE

if ratio > 10:
    regime = "DEEP QUANTUM (T << theta_D)"
elif ratio > 2:
    regime = "QUANTUM (T < theta_D)"
elif ratio > 0.5:
    regime = "INTERMEDIATE (T ~ theta_D)"
else:
    regime = "CLASSICAL (T >> theta_D)"

print(f"Regime: {regime}")
print(f"  theta_D / T_GGE = {ratio:.4f}")
print()

# Also classify per definition
for name, om in [("PW full", omega_max_pw), ("fold pq6", omega_max_fold),
                  ("Gaussian cutoff", omega_cutoff_gauss), ("BCS sector", omega_max_bcs)]:
    r = om / T_GGE
    if r > 10:
        reg = "DEEP QUANTUM"
    elif r > 2:
        reg = "QUANTUM"
    elif r > 0.5:
        reg = "INTERMEDIATE"
    else:
        reg = "CLASSICAL"
    print(f"  {name:20s}: omega/T = {r:.3f}  [{reg}]")

print()

# =============================================================================
#  4. Heat capacity C_V(T) from exact spectral sum (Einstein sum)
# =============================================================================
#
# Each KK mode at frequency omega_n with degeneracy g_n contributes to C_V
# as an Einstein oscillator:
#   C_V / k_B = sum_n g_n * (omega_n / T)^2 * exp(omega_n/T) / (exp(omega_n/T) - 1)^2
#
# The Dulong-Petit limit is C_V / k_B = N_total (one degree of freedom per mode).
# For 3D oscillators, C_V = 3N k_B. Our modes are scalar, so C_V = N k_B.

def cv_einstein_exact(T, omega_arr, mult_arr):
    """Exact C_V from sum of Einstein oscillators.
    Returns C_V / k_B per mode (normalized to N_total)."""
    if T <= 0:
        return 0.0
    x = omega_arr / T
    # Prevent overflow for large x
    mask = x < 500
    contrib = np.zeros_like(x)
    contrib[mask] = mult_arr[mask] * x[mask]**2 * np.exp(x[mask]) / (np.exp(x[mask]) - 1)**2
    N_total = mult_arr.sum()
    return contrib.sum() / N_total


def cv_debye(T, theta_D, d=3):
    """Debye model C_V/k_B per mode for d-dimensional density of states.
    Standard d=3 Debye: C_V = 9 N k_B (T/theta_D)^3 int_0^{x_D} x^4 e^x/(e^x-1)^2 dx
    where x_D = theta_D / T.
    For d=6 (internal manifold dimension): replace 3->6 in the prefactor and power.
    For d=8 (SU(3) has dim=8): same.

    Using the general formula for d-dimensional Debye model:
    C_V / (N k_B) = d * (d+1) * (T/theta_D)^d * int_0^{x_D} x^{d+1} e^x / (e^x-1)^2 dx
    """
    if T <= 0:
        return 0.0
    x_D = theta_D / T
    # Numerical integration
    n_pts = 10000  # (local)
    x = np.linspace(1e-10, x_D, n_pts)
    dx = x[1] - x[0]
    integrand = x**(d+1) * np.exp(x) / (np.exp(x) - 1)**2
    # Handle overflow at large x
    overflow = x > 500
    integrand[overflow] = 0.0
    integral = np.trapezoid(integrand, x)
    prefactor = d * (d + 1) * (T / theta_D)**d
    return prefactor * integral


# Temperature scan
T_scan = np.linspace(0.01, 3.0, 500)  # in M_KK

# Using s61 full spectrum (omega_all, pw_mult) — all 18624 modes
cv_exact_full = np.array([cv_einstein_exact(T, omega_all, pw_mult) for T in T_scan])

# Using s44 fold spectrum (omega_fold, dim2_fold) — 992 modes at tau=0.19
cv_exact_fold = np.array([cv_einstein_exact(T, omega_fold, dim2_fold) for T in T_scan])

# Debye models
# d=3 standard (even though internal manifold is 8-dimensional)
cv_debye_3d = np.array([cv_debye(T, theta_D, d=3) for T in T_scan])
# d=8 for dim(SU(3))=8
cv_debye_8d = np.array([cv_debye(T, theta_D, d=8) for T in T_scan])

# C_V at T_GGE specifically
cv_at_T_GGE_full = cv_einstein_exact(T_GGE, omega_all, pw_mult)
cv_at_T_GGE_fold = cv_einstein_exact(T_GGE, omega_fold, dim2_fold)
cv_debye_3d_at_T = cv_debye(T_GGE, theta_D, d=3)
cv_debye_8d_at_T = cv_debye(T_GGE, theta_D, d=8)

print("=" * 60)
print("Heat capacity C_V(T_GGE) / (N k_B) per mode")
print("=" * 60)
print(f"  Einstein exact (full PW):  {cv_at_T_GGE_full:.6f}")
print(f"  Einstein exact (fold pq6): {cv_at_T_GGE_fold:.6f}")
print(f"  Debye d=3:                 {cv_debye_3d_at_T:.6f}")
print(f"  Debye d=8:                 {cv_debye_8d_at_T:.6f}")
print(f"  Dulong-Petit limit:        1.000000")
print(f"  Quantum fraction C_V/C_DP: {cv_at_T_GGE_full:.4f} (full), {cv_at_T_GGE_fold:.4f} (fold)")
print()

# =============================================================================
#  5. Spectral statistics: moments and effective dimensionality
# =============================================================================

# Weighted moments of the spectrum
N_pw = pw_mult.sum()
omega_mean_pw = (pw_mult * omega_all).sum() / N_pw
omega2_mean_pw = (pw_mult * omega_all**2).sum() / N_pw
omega_rms_pw = np.sqrt(omega2_mean_pw)
omega_var_pw = omega2_mean_pw - omega_mean_pw**2

# For fold spectrum
N_fold = dim2_fold.sum()
omega_mean_fold = (dim2_fold * omega_fold).sum() / N_fold
omega2_mean_fold = (dim2_fold * omega_fold**2).sum() / N_fold
omega_rms_fold = np.sqrt(omega2_mean_fold)

# Bandwidth
Delta_omega_pw = omega_all.max() - omega_all.min()
Delta_omega_fold = omega_fold.max() - omega_fold.min()

# Spectral weight at T_GGE: which modes are thermally active?
x_arr = omega_all / T_GGE
bose = np.zeros_like(x_arr)
mask = x_arr < 500
bose[mask] = 1.0 / (np.exp(x_arr[mask]) - 1)
n_thermal_pw = (pw_mult * bose).sum()
N_active_fraction = n_thermal_pw / N_pw

print("=" * 60)
print("Spectral statistics")
print("=" * 60)
print(f"  Full PW (s61): N_modes = {N_pw:.0f}")
print(f"    <omega>     = {omega_mean_pw:.4f} M_KK")
print(f"    <omega^2>^{1/2} = {omega_rms_pw:.4f} M_KK")
print(f"    Bandwidth   = {Delta_omega_pw:.4f} M_KK")
print(f"    omega_min   = {omega_all.min():.4f} M_KK")
print(f"    omega_max   = {omega_all.max():.4f} M_KK")
print(f"  Fold (s44): N_modes = {N_fold:.0f}")
print(f"    <omega>     = {omega_mean_fold:.4f} M_KK")
print(f"    <omega^2>^{1/2} = {omega_rms_fold:.4f} M_KK")
print(f"    Bandwidth   = {Delta_omega_fold:.4f} M_KK")
print(f"  Thermal occupation at T_GGE:")
print(f"    <n_thermal> / N_PW = {N_active_fraction:.6f}")
print(f"    Total thermal quanta = {n_thermal_pw:.1f}")
print()

# =============================================================================
#  6. Condensed matter analog: superfluid He-3 comparison
# =============================================================================
#
# In He-3B, theta_D ~ 14 K (bulk He), T_c ~ 1 mK.
# So theta_D/T_c ~ 14,000 — far deeper quantum.
#
# Here theta_D/T_GGE ~ 5.3 — the KK "crystal" is relatively HOT compared to
# its Debye temperature. The GGE is a substantial fraction of the bandwidth.
# This is more like a warm solid than a cold superfluid.
#
# Cross-domain: acoustic metamaterial with few modes per cell.
# A finite phononic crystal with 992 modes at 0.82-2.06 M_KK has
# theta_D ~ 2 M_KK and operates at T ~ 0.39 M_KK: warm crystal regime.

# Phonon-exflation framing:
# The KK modes are the "lattice vibrations" of the internal geometry.
# theta_D sets the scale at which ALL geometric modes are thermally activated.
# T_GGE < theta_D means the GGE DOES NOT fully populate the high-frequency
# geometric modes. The internal geometry is in a partially frozen quantum state.
# Only modes with omega < few * T_GGE are significantly populated.

# Crossover temperature: where <n(omega)> = 0.5 (half-occupied)
omega_half = T_GGE * np.log(3)  # Bose: n=0.5 when omega/T = ln(3)
print(f"  omega at <n>=0.5: {omega_half:.4f} M_KK")
print(f"  Fraction of bandwidth thermally active: "
      f"{(omega_half - omega_all.min())/Delta_omega_pw:.3f}")
print()

# =============================================================================
#  7. Collective mode spectrum comparison
# =============================================================================
#
# S52 identified specific collective modes:
# Goldstone: c_Gold = 0.915 (gapless, acoustic)
# Leggett: omega_L1=0.138, omega_L2=0.192 (gapped, optical-like)
# Higgs: omega_H1=0.380, omega_H2=1.410, omega_H3=11.465 (gapped, massive)
#
# These are the BCS/GL collective excitations of the ORDER PARAMETER,
# distinct from the KK geometric modes. The Debye temperature applies to
# the geometric (KK) sector. The collective modes live in the BCS sector.

collective_freqs = {
    'Goldstone (k=0)': 0.0,
    'Leggett-1': omega_L1,
    'Leggett-2': omega_L2,
    'Higgs-1': omega_H1,
    'Higgs-2': omega_H2,
    'Higgs-3': omega_H3,
}

print("=" * 60)
print("Collective mode thermal population at T_GGE")
print("=" * 60)
for name, om in collective_freqs.items():
    if om == 0:
        print(f"  {name:20s}: omega = {om:.3f} M_KK  [Bose-condensed]")
    else:
        x = om / T_GGE
        if x < 500:
            n_bose = 1.0 / (np.exp(x) - 1)
        else:
            n_bose = 0.0
        pop = "ACTIVE" if n_bose > 0.01 else "FROZEN" if n_bose < 1e-6 else "MARGINAL"
        print(f"  {name:20s}: omega = {om:.3f} M_KK, x = omega/T = {x:.2f}, "
              f"<n> = {n_bose:.4e}  [{pop}]")

print()

# =============================================================================
#  8. Debye function D_n(x) and exact comparison
# =============================================================================

def debye_function(n, x):
    """Debye function D_n(x) = (n/x^n) * int_0^x t^n / (e^t - 1) dt."""
    if x <= 0:
        return 1.0  # D_n(0) = 1
    t = np.linspace(1e-12, x, 10000)
    dt = t[1] - t[0]
    integrand = t**n / (np.exp(t) - 1)
    mask = t < 500
    integrand[~mask] = 0.0
    return n / x**n * np.trapezoid(integrand, t)

x_D = theta_D / T_GGE
D3 = debye_function(3, x_D)
D8 = debye_function(8, x_D)

# Internal energy per mode from Debye model:
# U / (N k_B T) = d * D_d(theta_D/T) for d-dim Debye
# C_V / (N k_B) = d * [d * D_d(x) - d * x * D_d'(x)] ... use numerical derivative

# Or more directly: Debye C_V / C_DP = 1 - correction
# High T: C_V -> N k_B (DP)
# Low T: C_V ~ (T/theta_D)^d

print("=" * 60)
print("Debye function values at theta_D/T_GGE")
print("=" * 60)
print(f"  x_D = theta_D / T_GGE = {x_D:.4f}")
print(f"  D_3(x_D) = {D3:.6f}")
print(f"  D_8(x_D) = {D8:.6f}")
print()

# =============================================================================
#  9. Physical scale conversion
# =============================================================================
#
# M_KK = 7.43e16 GeV (gravity route).
# In SI: T_Debye = theta_D * M_KK / k_B (in Kelvin? No: in natural units,
# theta_D is already a temperature in M_KK energy units.)
# T_Debye_GeV = theta_D * M_KK = 2.048 * 7.43e16 = 1.52e17 GeV
# T_Debye_K = T_Debye_GeV / k_B = 1.52e17 / 8.617e-14 = 1.76e30 K
# (k_B in GeV/K = 8.617e-5 eV/K = 8.617e-14 GeV/K)

k_B_GeV_per_K = k_B * 1e-9   # Convert eV/K to GeV/K = 8.617e-14

theta_D_GeV = theta_D * M_KK_gravity
T_GGE_GeV = T_GGE * M_KK_gravity
theta_D_K = theta_D_GeV / k_B_GeV_per_K
T_GGE_K = T_GGE_GeV / k_B_GeV_per_K

print("=" * 60)
print("Physical scales (gravity route M_KK)")
print("=" * 60)
print(f"  theta_D = {theta_D:.4f} M_KK = {theta_D_GeV:.3e} GeV = {theta_D_K:.3e} K")
print(f"  T_GGE   = {T_GGE:.4f} M_KK = {T_GGE_GeV:.3e} GeV = {T_GGE_K:.3e} K")
print(f"  T_GGE / theta_D = {T_GGE/theta_D:.4f}")
print()

# =============================================================================
#  10. Summary and gate verdict
# =============================================================================

gate_detail = (
    f"theta_D = {theta_D:.4f} M_KK (spectral action Gaussian cutoff). "
    f"T_GGE = {T_GGE:.4f} M_KK. "
    f"theta_D / T_GGE = {ratio:.2f}. "
    f"Regime: {regime}. "
    f"C_V(T_GGE)/C_DP = {cv_at_T_GGE_full:.4f} (exact), "
    f"{cv_at_T_GGE_fold:.4f} (fold). "
    f"Debye D_3({x_D:.2f}) = {D3:.4f}."
)

print("=" * 60)
print(f"GATE: DEBYE-FOLD-63 | INFO | {regime}")
print("=" * 60)
print(gate_detail)
print()

# =============================================================================
#  11. Save data
# =============================================================================

np.savez(OUT_NPZ,
    # Gate
    gate_name='DEBYE-FOLD-63',
    gate_verdict='INFO',
    gate_detail=gate_detail,
    # Debye temperatures (all definitions)
    theta_D_physical=theta_D,
    omega_max_pw=omega_max_pw,
    omega_max_fold=omega_max_fold,
    omega_cutoff_gauss=omega_cutoff_gauss,
    omega_max_bcs=omega_max_bcs,
    # Temperature comparison
    T_GGE=T_GGE,
    ratio_theta_T=ratio,
    regime=regime,
    # Heat capacity
    T_scan=T_scan,
    cv_exact_full=cv_exact_full,
    cv_exact_fold=cv_exact_fold,
    cv_debye_3d=cv_debye_3d,
    cv_debye_8d=cv_debye_8d,
    cv_at_T_GGE_full=cv_at_T_GGE_full,
    cv_at_T_GGE_fold=cv_at_T_GGE_fold,
    cv_debye_3d_at_T=cv_debye_3d_at_T,
    cv_debye_8d_at_T=cv_debye_8d_at_T,
    # Spectral statistics
    omega_mean_pw=omega_mean_pw,
    omega_rms_pw=omega_rms_pw,
    omega_mean_fold=omega_mean_fold,
    omega_rms_fold=omega_rms_fold,
    N_pw_total=N_pw,
    N_fold_total=N_fold,
    N_active_fraction=N_active_fraction,
    n_thermal_total=n_thermal_pw,
    # Debye functions
    x_D=x_D,
    D3_at_T_GGE=D3,
    D8_at_T_GGE=D8,
    # Physical scales
    theta_D_GeV=theta_D_GeV,
    T_GGE_GeV=T_GGE_GeV,
    theta_D_K=theta_D_K,
    T_GGE_K=T_GGE_K,
    # Thermal crossover
    omega_half_occupation=omega_half,
)

print(f"Saved: {OUT_NPZ}")

# =============================================================================
#  12. Plot
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'DEBYE-FOLD-63: Effective Debye Temperature at Fold ($\tau = 0.19$)',
             fontsize=13, fontweight='bold')

# Panel (a): C_V(T) comparison
ax = axes[0, 0]
ax.plot(T_scan, cv_exact_full, 'b-', linewidth=2, label='Einstein exact (full PW)')
ax.plot(T_scan, cv_exact_fold, 'c--', linewidth=1.5, label='Einstein exact (fold pq6)')
ax.plot(T_scan, cv_debye_3d, 'r:', linewidth=1.5, label=r'Debye $d=3$')
ax.plot(T_scan, cv_debye_8d, 'g-.', linewidth=1.5, label=r'Debye $d=8$')
ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5, label='Dulong-Petit')
ax.axvline(T_GGE, color='orange', linewidth=2, alpha=0.7, label=f'$T_{{GGE}} = {T_GGE:.3f}$')
ax.axvline(theta_D, color='red', linewidth=1.5, alpha=0.5, label=fr'$\theta_D = {theta_D:.3f}$')
ax.set_xlabel(r'$T$ [$M_{KK}$]')
ax.set_ylabel(r'$C_V / (N k_B)$')
ax.set_title('(a) Heat capacity vs temperature')
ax.legend(fontsize=8, loc='lower right')
ax.set_xlim(0, 3)
ax.set_ylim(0, 1.05)
ax.grid(alpha=0.3)

# Panel (b): DOS-weighted spectrum with thermal window
ax = axes[0, 1]
# Histogram of eigenvalues weighted by multiplicities
bins = np.linspace(0.7, 3.6, 100)
ax.hist(omega_all, bins=bins, weights=pw_mult, color='steelblue', alpha=0.6,
        label=f'KK modes (N={N_pw:.0f})')
ax.axvline(T_GGE, color='orange', linewidth=2, label=f'$T_{{GGE}}$')
ax.axvline(theta_D, color='red', linewidth=1.5, linestyle='--', label=fr'$\theta_D$')
ax.axvline(omega_half, color='green', linewidth=1.5, linestyle=':',
           label=fr'$\omega_{{1/2}} = {omega_half:.3f}$')
ax.axvspan(omega_all.min(), omega_half, color='yellow', alpha=0.15, label='Thermally active')
ax.set_xlabel(r'$\omega$ [$M_{KK}$]')
ax.set_ylabel('Weighted DOS')
ax.set_title('(b) KK spectrum with thermal window')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Panel (c): Bose occupation n(omega) at T_GGE
ax = axes[1, 0]
omega_plot = np.linspace(omega_all.min(), omega_all.max(), 500)
x_plot = omega_plot / T_GGE
n_bose_plot = np.where(x_plot < 500, 1.0 / (np.exp(x_plot) - 1), 0.0)
ax.semilogy(omega_plot, n_bose_plot, 'b-', linewidth=2)
ax.axhline(0.5, color='gray', linestyle='--', alpha=0.5, label=r'$\langle n \rangle = 0.5$')
ax.axvline(omega_half, color='green', linewidth=1, linestyle=':', alpha=0.7)
# Mark collective modes
for name, om in [('L1', omega_L1), ('L2', omega_L2), ('H1', omega_H1), ('H2', omega_H2)]:
    if om > 0.05:
        x_m = om / T_GGE
        n_m = 1.0 / (np.exp(x_m) - 1) if x_m < 500 else 0
        ax.plot(om, n_m, 'rv', markersize=8)
        ax.annotate(name, (om, n_m), fontsize=7, ha='center', va='bottom')
ax.set_xlabel(r'$\omega$ [$M_{KK}$]')
ax.set_ylabel(r'$\langle n(\omega) \rangle$')
ax.set_title(f'(c) Bose occupation at $T_{{GGE}} = {T_GGE:.3f}$')
ax.set_ylim(1e-4, 10)
ax.set_xlim(0, 3.6)
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

# Panel (d): Summary table
ax = axes[1, 1]
ax.axis('off')
table_data = [
    [r'$\theta_D$ (physical)', f'{theta_D:.4f} M_KK', f'{theta_D_GeV:.2e} GeV'],
    [r'$T_{GGE}$', f'{T_GGE:.4f} M_KK', f'{T_GGE_GeV:.2e} GeV'],
    [r'$\theta_D / T_{GGE}$', f'{ratio:.4f}', regime],
    [r'$C_V / C_{DP}$ (exact)', f'{cv_at_T_GGE_full:.4f}', f'{cv_at_T_GGE_fold:.4f} (fold)'],
    [r'$D_3(\theta_D/T)$', f'{D3:.6f}', ''],
    [r'$\omega_{min}$', f'{omega_all.min():.4f} M_KK', ''],
    [r'$\omega_{max}$ (PW)', f'{omega_max_pw:.4f} M_KK', ''],
    [r'$\langle\omega\rangle$', f'{omega_mean_pw:.4f} M_KK', ''],
    [r'$N_{modes}$ (PW)', f'{N_pw:.0f}', f'({N_fold:.0f} at fold)'],
    [r'Thermal fraction', f'{N_active_fraction:.6f}', f'{n_thermal_pw:.1f} quanta'],
]
table = ax.table(cellText=table_data,
                 colLabels=['Quantity', 'Value', 'Note'],
                 loc='center', cellLoc='left')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.4)
ax.set_title('(d) DEBYE-FOLD-63 Summary', fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")
print()
print("DONE.")
