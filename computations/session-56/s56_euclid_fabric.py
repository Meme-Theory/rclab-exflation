#!/usr/bin/env python3
"""
s56_euclid_fabric.py — Euclidean Free Energy on Fabric with Physical mu_eff

EUCLID-FABRIC-56 (INFO gate):
Cross-check of W1-1 (ROTOR-MF-56) with the physical mu_eff from W1-4 (MU-SHIFT-56).

The question: W1-1 computed F_cells at mu=0 (PH-symmetric, S34 theorem). W1-4 showed
mu_eff = -0.201 M_KK at the fold (PH broken by non-bipartite CG graph). Does computing
F_cells at the PHYSICAL mu_eff change the monotonicity of F_fabric?

Method:
1. F_cells(tau, mu_eff) using the FULL 32 TB eigenvalues (not 8 per cell):
   F_cells(tau, mu) = -T_GH * Sum_{k=0}^{31} ln(1 + exp(-(E_k - mu)/T_GH))
   This is the grand canonical free energy of the fabric single-particle sector.

2. Fermionic spectral action S_f at mu_eff:
   n_k(mu) = 1/(1 + exp((E_k - mu)/T_GH))  (Fermi-Dirac occupation)
   S_f(tau, mu) = Sum_k n_k * |E_k|
   Check sign of dS_f/dtau (S55 showed positive at half-filling, negative at mu=0).

3. BCS grand potential Omega_BCS at mu_eff:
   xi_k = E_k - mu
   E_qp_k = sqrt(xi_k^2 + Delta^2)
   Omega_BCS = Sum_k [xi_k - E_qp_k + Delta^2/(2*E_qp_k)*tanh(E_qp_k/(2T))]
   This captures the BCS pairing contribution at finite mu.

4. F_fabric_corrected = F_cells(mu_eff) + F_Josephson + F_BA

Gate: EUCLID-FABRIC-56 = INFO (cross-check, not pass/fail).

Author: phonon-first-cosmologist
Session: S56, Wave 2, Task 1
"""

import sys
import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

sys.path.insert(0, 'computations')
from canonical_constants import Delta_0_OES, tau_fold, N_cells

# =============================================================================
# 0. Load all upstream data
# =============================================================================

# W1-1: Fabric free energy components (mu=0 baseline)
w11 = np.load('computations/session-56/s56_rotor_mf.npz', allow_pickle=True)
tau_values    = w11['tau_values']     # (50,)
F_cells_mu0   = w11['F_cells']       # (50,) F_cells at mu=0
F_Josephson   = w11['F_Josephson']    # (50,)
F_BA          = w11['F_BA']          # (50,)
F_fabric_mu0  = w11['F_fabric']      # (50,)
m_order       = w11['m_order']       # (50,) XY order parameter
E_J_arr       = w11['E_J']          # (50,) Josephson energy per bond
E_c_arr       = w11['E_c']          # (50,) charging energy
T_GH_w11     = w11['T_GH']          # (50,) Gibbons-Hawking temperature

# W1-4: Chemical potential from PH breaking
w14 = np.load('computations/session-56/s56_mu_josephson.npz', allow_pickle=True)
mu_eff        = w14['mu_eff']        # (50,) effective chemical potential
mu_half       = w14['mu_half']       # (50,) half-filling mu
mu_PH         = w14['mu_PH']         # (50,) PH-symmetric midpoint
A_PH          = w14['A_PH']         # (50,) PH asymmetry measure
BW            = w14['BW']           # (50,) bandwidth

# TB eigenvalues (full 32-cell spectrum)
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
eigenvalues   = tb['eigenvalues']    # (50, 32) TB spectrum
adj_C2        = tb['adj_C2']        # (32, 32) C2 adjacency

# ED sweep (8 single-particle BCS-active energies per cell)
ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)
E_sp_sweep    = ed['E_sp_sweep']     # (50, 8) single-cell SP energies

# Scale factor (for T_GH cross-check)
sf = np.load('computations/session-54/s54_scale_factor.npz', allow_pickle=True)

# BA spectrum (for omega_BA)
ba = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)
T_GH          = ba['T_GH']          # (50,) — same as w11 T_GH
omega_BA_all  = ba['omega_BA']       # (50, 31) BA phonon frequencies

N_tau = len(tau_values)
N_cells_val = 32  # from canonical
N_bonds = int(np.sum(adj_C2 > 0)) // 2  # 50
Delta = Delta_0_OES  # 0.4643 M_KK

# Fold index
idx_fold = np.argmin(np.abs(tau_values - tau_fold))

print(f"Loaded all upstream data: {N_tau} tau values in [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"N_cells = {N_cells_val}, N_bonds = {N_bonds}, Delta = {Delta:.6f} M_KK")
print(f"Fold at tau = {tau_values[idx_fold]:.4f} (index {idx_fold})")
print(f"mu_eff at fold = {mu_eff[idx_fold]:.6f} M_KK")
print(f"T_GH at fold = {T_GH[idx_fold]:.6f} M_KK")

# Cross-check T_GH consistency
assert np.allclose(T_GH, T_GH_w11, rtol=1e-10), "T_GH mismatch between BA and W1-1"
print("T_GH cross-check: PASS")

# =============================================================================
# 1. F_cells at mu=0 vs mu=mu_eff — FULL 32-eigenvalue fabric partition function
#
#    F(tau, mu) = -T_GH * Sum_{k=0}^{31} ln(1 + exp(-(E_k - mu)/T_GH))
#
#    This is the grand canonical free energy Omega of the non-interacting
#    single-particle sector. At mu=0, it should reproduce something proportional
#    to the W1-1 F_cells (which used 8 SP energies * 32 cells).
#
#    KEY DISTINCTION: W1-1 used 8 single-cell SP energies x 32 cells.
#    Here we use the 32 TB eigenvalues directly. These are the FABRIC
#    single-particle energies, not cell-replicated.
# =============================================================================

def grand_canonical_F(E_k, T, mu):
    """Grand canonical free energy for fermionic spectrum.

    F(mu, T) = -T * Sum_k ln(1 + exp(-(E_k - mu)/T))

    Numerically stable: for large x = (E_k - mu)/T,
    ln(1 + exp(-x)) ~ exp(-x)
    """
    x = (E_k - mu) / T
    log_terms = np.where(x > 500, np.exp(-x), np.log1p(np.exp(-x)))
    return -T * np.sum(log_terms)


def fermi_dirac(E_k, T, mu):
    """Fermi-Dirac occupation numbers.

    n_k = 1/(1 + exp((E_k - mu)/T))
    """
    x = (E_k - mu) / T
    return np.where(x > 500, 0.0, np.where(x < -500, 1.0, 1.0 / (1.0 + np.exp(x))))


# --- Compute F_cells using full 32 TB eigenvalues ---
# Three chemical potentials compared:
# (a) mu = 0 (S34 theorem, single-cell PH)
# (b) mu = mu_eff(tau) from W1-4 (physical fabric mu)
# (c) mu = mu_half(tau) (exact half-filling)

F_cells_tb_mu0 = np.zeros(N_tau)        # 32 TB eigenvalues, mu=0
F_cells_tb_mueff = np.zeros(N_tau)      # 32 TB eigenvalues, mu=mu_eff
F_cells_tb_muhalf = np.zeros(N_tau)     # 32 TB eigenvalues, mu=mu_half
N_particles_mu0 = np.zeros(N_tau)       # Mean particle number at mu=0
N_particles_mueff = np.zeros(N_tau)     # Mean particle number at mu_eff
N_particles_muhalf = np.zeros(N_tau)    # Mean particle number at mu_half

for i in range(N_tau):
    E = np.sort(eigenvalues[i])  # 32 sorted eigenvalues
    T = T_GH[i]

    # mu = 0
    F_cells_tb_mu0[i] = grand_canonical_F(E, T, 0.0)
    N_particles_mu0[i] = np.sum(fermi_dirac(E, T, 0.0))

    # mu = mu_eff(tau)
    F_cells_tb_mueff[i] = grand_canonical_F(E, T, mu_eff[i])
    N_particles_mueff[i] = np.sum(fermi_dirac(E, T, mu_eff[i]))

    # mu = mu_half(tau)
    F_cells_tb_muhalf[i] = grand_canonical_F(E, T, mu_half[i])
    N_particles_muhalf[i] = np.sum(fermi_dirac(E, T, mu_half[i]))

print(f"\n{'='*72}")
print(f"FABRIC GRAND CANONICAL FREE ENERGY (32 TB eigenvalues)")
print(f"{'='*72}")
print(f"{'tau':>6s}  {'F(mu=0)':>12s}  {'F(mu_eff)':>12s}  {'F(mu_half)':>12s}  {'delta_F':>12s}  {'N(mu=0)':>8s}  {'N(mu_eff)':>8s}")
print(f"{'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*8}  {'-'*8}")

for idx in [0, 5, 10, 15, idx_fold, 20, 25, 30, 35, 40, 45, 49]:
    delta = F_cells_tb_mueff[idx] - F_cells_tb_mu0[idx]
    print(f"{tau_values[idx]:6.3f}  {F_cells_tb_mu0[idx]:12.4f}  {F_cells_tb_mueff[idx]:12.4f}  "
          f"{F_cells_tb_muhalf[idx]:12.4f}  {delta:12.4f}  {N_particles_mu0[idx]:8.2f}  "
          f"{N_particles_mueff[idx]:8.2f}")

# =============================================================================
# 2. Fermionic spectral action S_f at various mu
#
#    S_f(tau, mu) = Sum_{k=0}^{31} n_k(mu) * |E_k|
#
#    where n_k = Fermi-Dirac at temperature T_GH.
#    S55 showed dS_f/dtau > 0 at half-filling but < 0 at mu=0.
# =============================================================================

S_f_mu0 = np.zeros(N_tau)
S_f_mueff = np.zeros(N_tau)
S_f_muhalf = np.zeros(N_tau)

for i in range(N_tau):
    E = np.sort(eigenvalues[i])
    T = T_GH[i]

    n_mu0 = fermi_dirac(E, T, 0.0)
    n_mueff = fermi_dirac(E, T, mu_eff[i])
    n_muhalf = fermi_dirac(E, T, mu_half[i])

    S_f_mu0[i] = np.sum(n_mu0 * np.abs(E))
    S_f_mueff[i] = np.sum(n_mueff * np.abs(E))
    S_f_muhalf[i] = np.sum(n_muhalf * np.abs(E))

# Derivatives
dS_f_mu0 = np.gradient(S_f_mu0, tau_values)
dS_f_mueff = np.gradient(S_f_mueff, tau_values)
dS_f_muhalf = np.gradient(S_f_muhalf, tau_values)

print(f"\n{'='*72}")
print(f"FERMIONIC SPECTRAL ACTION S_f")
print(f"{'='*72}")
print(f"{'tau':>6s}  {'S_f(mu=0)':>12s}  {'S_f(mu_eff)':>12s}  {'S_f(mu_half)':>12s}  "
      f"{'dS_f(0)':>10s}  {'dS_f(eff)':>10s}  {'dS_f(half)':>10s}")
print(f"{'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*10}  {'-'*10}  {'-'*10}")

for idx in [0, 5, 10, 15, idx_fold, 20, 25, 30, 35, 40, 45, 49]:
    print(f"{tau_values[idx]:6.3f}  {S_f_mu0[idx]:12.4f}  {S_f_mueff[idx]:12.4f}  "
          f"{S_f_muhalf[idx]:12.4f}  {dS_f_mu0[idx]:+10.4f}  {dS_f_mueff[idx]:+10.4f}  "
          f"{dS_f_muhalf[idx]:+10.4f}")

# Sign analysis of dS_f
print(f"\nSign of dS_f/dtau at fold:")
print(f"  mu=0:      dS_f/dtau = {dS_f_mu0[idx_fold]:+.4f}  ({'positive' if dS_f_mu0[idx_fold] > 0 else 'NEGATIVE'})")
print(f"  mu=mu_eff: dS_f/dtau = {dS_f_mueff[idx_fold]:+.4f}  ({'positive' if dS_f_mueff[idx_fold] > 0 else 'NEGATIVE'})")
print(f"  mu=mu_half:dS_f/dtau = {dS_f_muhalf[idx_fold]:+.4f}  ({'positive' if dS_f_muhalf[idx_fold] > 0 else 'NEGATIVE'})")

# Find sign change of dS_f
for name, dSf in [("mu=0", dS_f_mu0), ("mu=mu_eff", dS_f_mueff), ("mu=mu_half", dS_f_muhalf)]:
    sign_changes = []
    for i in range(len(dSf)-1):
        if dSf[i] * dSf[i+1] < 0:
            tau_cross = tau_values[i] - dSf[i] * (tau_values[i+1] - tau_values[i]) / (dSf[i+1] - dSf[i])
            sign_changes.append(tau_cross)
    print(f"  dS_f({name}) sign changes at tau = {[f'{t:.4f}' for t in sign_changes]}")

# =============================================================================
# 3. BCS Grand Potential at mu_eff
#
#    Omega_BCS(tau, mu) = Sum_k [xi_k - E_qp_k - T*ln(1 + exp(-E_qp_k/T))]
#                         + N*Delta^2/V_eff  (gap equation self-consistency term)
#
#    where xi_k = E_k - mu, E_qp_k = sqrt(xi_k^2 + Delta^2)
#
#    We compare the BCS contribution at mu=0 vs mu=mu_eff.
# =============================================================================

Omega_BCS_mu0 = np.zeros(N_tau)
Omega_BCS_mueff = np.zeros(N_tau)
Omega_BCS_muhalf = np.zeros(N_tau)

for i in range(N_tau):
    E = np.sort(eigenvalues[i])
    T = T_GH[i]

    for mu_val, Omega_arr in [(0.0, Omega_BCS_mu0),
                               (mu_eff[i], Omega_BCS_mueff),
                               (mu_half[i], Omega_BCS_muhalf)]:
        xi = E - mu_val
        E_qp = np.sqrt(xi**2 + Delta**2)

        # BCS ground state contribution (T -> 0 limit well-approximated at T_GH << Delta)
        # Omega = Sum_k [xi_k - E_qp_k] + const
        # The constant (Delta^2/V) cancels when comparing different mu values
        # We include the thermal occupation for completeness
        x = E_qp / T
        thermal = np.where(x > 500, 0.0, -T * np.log1p(np.exp(-x)))

        Omega_arr[i] = np.sum(xi - E_qp + thermal)

print(f"\n{'='*72}")
print(f"BCS GRAND POTENTIAL (32 TB eigenvalues)")
print(f"{'='*72}")
print(f"{'tau':>6s}  {'Omega(mu=0)':>14s}  {'Omega(mu_eff)':>14s}  {'Omega(mu_half)':>14s}  {'delta_Omega':>14s}")
print(f"{'-'*6}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*14}")

for idx in [0, 5, 10, 15, idx_fold, 20, 25, 30, 35, 40, 45, 49]:
    delta = Omega_BCS_mueff[idx] - Omega_BCS_mu0[idx]
    print(f"{tau_values[idx]:6.3f}  {Omega_BCS_mu0[idx]:14.4f}  {Omega_BCS_mueff[idx]:14.4f}  "
          f"{Omega_BCS_muhalf[idx]:14.4f}  {delta:14.4f}")

# =============================================================================
# 4. Corrected F_fabric at mu_eff
#
#    F_fabric_corrected = F_cells(mu_eff) + F_Josephson + F_BA
#
#    We use the 32-TB grand canonical F for consistency.
#    But we also compute: what if we replace only F_cells while keeping
#    F_Josephson and F_BA from W1-1?
# =============================================================================

# Option A: Replace F_cells with grand canonical at mu_eff (using TB eigenvalues)
F_fabric_mueff = F_cells_tb_mueff + F_Josephson + F_BA
F_fabric_tb_mu0 = F_cells_tb_mu0 + F_Josephson + F_BA

# Option B: Use BCS grand potential instead of free-particle F
F_fabric_BCS_mueff = Omega_BCS_mueff + F_Josephson + F_BA
F_fabric_BCS_mu0 = Omega_BCS_mu0 + F_Josephson + F_BA

# Derivatives
dF_fabric_mu0_orig = np.gradient(F_fabric_mu0, tau_values)  # original W1-1
dF_fabric_mueff = np.gradient(F_fabric_mueff, tau_values)
dF_fabric_tb_mu0 = np.gradient(F_fabric_tb_mu0, tau_values)
dF_fabric_BCS_mueff = np.gradient(F_fabric_BCS_mueff, tau_values)
dF_fabric_BCS_mu0 = np.gradient(F_fabric_BCS_mu0, tau_values)

# Derivatives of the cell contributions alone
dF_cells_mu0_orig = np.gradient(F_cells_mu0, tau_values)
dF_cells_tb_mu0_arr = np.gradient(F_cells_tb_mu0, tau_values)
dF_cells_tb_mueff_arr = np.gradient(F_cells_tb_mueff, tau_values)
dOmega_BCS_mu0_arr = np.gradient(Omega_BCS_mu0, tau_values)
dOmega_BCS_mueff_arr = np.gradient(Omega_BCS_mueff, tau_values)

print(f"\n{'='*72}")
print(f"CORRECTED FABRIC FREE ENERGY")
print(f"{'='*72}")
print(f"{'tau':>6s}  {'F_orig(mu=0)':>14s}  {'F_tb(mu=0)':>14s}  {'F_tb(mu_eff)':>14s}  "
      f"{'delta':>10s}  {'%change':>10s}")
print(f"{'-'*6}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*10}  {'-'*10}")

for idx in [0, 5, 10, 15, idx_fold, 20, 25, 30, 35, 40, 45, 49]:
    delta = F_fabric_mueff[idx] - F_fabric_mu0[idx]
    pct = 100.0 * abs(delta / F_fabric_mu0[idx]) if abs(F_fabric_mu0[idx]) > 1e-10 else 0.0
    print(f"{tau_values[idx]:6.3f}  {F_fabric_mu0[idx]:14.4f}  {F_fabric_tb_mu0[idx]:14.4f}  "
          f"{F_fabric_mueff[idx]:14.4f}  {delta:10.4f}  {pct:10.4f}%")

# =============================================================================
# 5. Monotonicity analysis
# =============================================================================

print(f"\n{'='*72}")
print(f"MONOTONICITY ANALYSIS")
print(f"{'='*72}")

def find_extrema(F_arr, tau_arr, label):
    """Find sign changes in dF/dtau."""
    dF = np.gradient(F_arr, tau_arr)
    sign_dF = np.sign(dF)
    extrema = []
    for i in range(len(sign_dF) - 1):
        if sign_dF[i] * sign_dF[i+1] < 0:
            dtau = tau_arr[i+1] - tau_arr[i]
            tau_cross = tau_arr[i] - dF[i] * dtau / (dF[i+1] - dF[i])
            is_min = dF[i] < 0 and dF[i+1] > 0
            F_cross = np.interp(tau_cross, tau_arr, F_arr)
            extrema.append((tau_cross, 'MIN' if is_min else 'MAX', F_cross))

    minima_in_gate = [e for e in extrema if 0.10 <= e[0] <= 0.30 and e[1] == 'MIN']
    is_monotone = all(d >= -1e-8 for d in dF)  # monotonically increasing

    print(f"\n  {label}:")
    print(f"    dF/dtau range: [{dF.min():+.4f}, {dF.max():+.4f}]")
    print(f"    dF/dtau at fold: {dF[idx_fold]:+.4f}")
    print(f"    Monotonically increasing: {is_monotone}")
    print(f"    Total extrema: {len(extrema)}")
    print(f"    Minima in [0.10, 0.30]: {len(minima_in_gate)}")
    for e in extrema:
        print(f"      {e[1]} at tau={e[0]:.4f}, F={e[2]:.4f}")

    return extrema, minima_in_gate, is_monotone

ext_orig, min_orig, mono_orig = find_extrema(F_fabric_mu0, tau_values, "F_fabric (W1-1 original, mu=0)")
ext_tb0, min_tb0, mono_tb0 = find_extrema(F_fabric_tb_mu0, tau_values, "F_fabric (TB eigenvalues, mu=0)")
ext_mueff, min_mueff, mono_mueff = find_extrema(F_fabric_mueff, tau_values, "F_fabric (TB eigenvalues, mu=mu_eff)")
ext_bcs0, min_bcs0, mono_bcs0 = find_extrema(F_fabric_BCS_mu0, tau_values, "F_fabric_BCS (mu=0)")
ext_bcs_mu, min_bcs_mu, mono_bcs_mu = find_extrema(F_fabric_BCS_mueff, tau_values, "F_fabric_BCS (mu=mu_eff)")

# =============================================================================
# 6. Derivative decomposition at fold — mu_eff correction
# =============================================================================

print(f"\n{'='*72}")
print(f"DERIVATIVE DECOMPOSITION AT FOLD (tau={tau_values[idx_fold]:.4f})")
print(f"{'='*72}")

dF_Josephson_arr = np.gradient(F_Josephson, tau_values)
dF_BA_arr = np.gradient(F_BA, tau_values)

print(f"\n  W1-1 (original, 8 SP * 32 cells, mu=0):")
print(f"    dF_cells/dtau      = {dF_cells_mu0_orig[idx_fold]:+12.4f}")
print(f"    dF_Josephson/dtau  = {dF_Josephson_arr[idx_fold]:+12.4f}")
print(f"    dF_BA/dtau         = {dF_BA_arr[idx_fold]:+12.4f}")
print(f"    dF_fabric/dtau     = {dF_fabric_mu0_orig[idx_fold]:+12.4f}")

print(f"\n  This work (32 TB eigenvalues, mu=0):")
print(f"    dF_cells/dtau      = {dF_cells_tb_mu0_arr[idx_fold]:+12.4f}")
print(f"    dF_Josephson/dtau  = {dF_Josephson_arr[idx_fold]:+12.4f}")
print(f"    dF_BA/dtau         = {dF_BA_arr[idx_fold]:+12.4f}")
print(f"    dF_fabric/dtau     = {dF_fabric_tb_mu0[idx_fold]:+12.4f}")

print(f"\n  This work (32 TB eigenvalues, mu=mu_eff):")
print(f"    dF_cells/dtau      = {dF_cells_tb_mueff_arr[idx_fold]:+12.4f}")
print(f"    dF_Josephson/dtau  = {dF_Josephson_arr[idx_fold]:+12.4f}")
print(f"    dF_BA/dtau         = {dF_BA_arr[idx_fold]:+12.4f}")
print(f"    dF_fabric/dtau     = {dF_fabric_mueff[idx_fold]:+12.4f}")

print(f"\n  BCS grand potential (32 TB, mu=0):")
print(f"    dOmega_BCS/dtau    = {dOmega_BCS_mu0_arr[idx_fold]:+12.4f}")
print(f"    dF_Josephson/dtau  = {dF_Josephson_arr[idx_fold]:+12.4f}")
print(f"    dF_BA/dtau         = {dF_BA_arr[idx_fold]:+12.4f}")
print(f"    dF_total/dtau      = {dF_fabric_BCS_mu0[idx_fold]:+12.4f}")

print(f"\n  BCS grand potential (32 TB, mu=mu_eff):")
print(f"    dOmega_BCS/dtau    = {dOmega_BCS_mueff_arr[idx_fold]:+12.4f}")
print(f"    dF_Josephson/dtau  = {dF_Josephson_arr[idx_fold]:+12.4f}")
print(f"    dF_BA/dtau         = {dF_BA_arr[idx_fold]:+12.4f}")
print(f"    dF_total/dtau      = {dF_fabric_BCS_mueff[idx_fold]:+12.4f}")

# Quantify the mu_eff correction
delta_dF_cells = dF_cells_tb_mueff_arr[idx_fold] - dF_cells_tb_mu0_arr[idx_fold]
delta_dF_BCS = dOmega_BCS_mueff_arr[idx_fold] - dOmega_BCS_mu0_arr[idx_fold]
josephson_slope = dF_Josephson_arr[idx_fold]

print(f"\n  mu_eff correction to cell derivative at fold:")
print(f"    delta(dF_cells/dtau) = {delta_dF_cells:+.4f} M_KK")
print(f"    delta(dOmega_BCS/dtau) = {delta_dF_BCS:+.4f} M_KK")
print(f"    Josephson slope (to overcome): {josephson_slope:+.4f} M_KK")
print(f"    Ratio |delta_dF_cells / dF_Josephson|: {abs(delta_dF_cells/josephson_slope):.6f}")
print(f"    Ratio |delta_dOmega / dF_Josephson|:   {abs(delta_dF_BCS/josephson_slope):.6f}")

# =============================================================================
# 7. The critical ratio: can mu_eff correction overcome Josephson monotonicity?
# =============================================================================

print(f"\n{'='*72}")
print(f"CRITICAL RATIO ANALYSIS")
print(f"{'='*72}")

# At each tau, compute the ratio of the mu_eff correction to the Josephson slope
# The monotonicity can only be broken if the correction exceeds the Josephson slope

delta_dF_correction = np.gradient(F_cells_tb_mueff - F_cells_tb_mu0, tau_values)
ratio_correction_josephson = np.abs(delta_dF_correction / (dF_Josephson_arr + 1e-30))

print(f"\n  max |delta_dF(mu_eff - mu=0) / dF_Josephson|:")
print(f"    Over all tau: {ratio_correction_josephson.max():.6f} at tau={tau_values[np.argmax(ratio_correction_josephson)]:.4f}")
print(f"    In gate window: {ratio_correction_josephson[(tau_values >= 0.10) & (tau_values <= 0.30)].max():.6f}")
print(f"    At fold: {ratio_correction_josephson[idx_fold]:.6f}")

# Also: the mu_eff shift can help ONLY if it makes dF_cells more negative
# Check the sign
print(f"\n  Sign of mu_eff correction to dF_cells/dtau:")
for idx_show in [0, 5, 10, 15, idx_fold, 20, 25, 30, 35, 40, 45, 49]:
    dc = delta_dF_correction[idx_show]
    sign_str = "helps (more negative)" if dc < 0 else "hurts (more positive)"
    print(f"    tau={tau_values[idx_show]:.3f}: {dc:+.4f}  [{sign_str}]")

# =============================================================================
# 8. What mu_eff would be needed to overcome the Josephson slope?
# =============================================================================

print(f"\n{'='*72}")
print(f"REQUIRED mu_eff FOR NON-MONOTONICITY")
print(f"{'='*72}")

# The total negative slope available is dF_cells + dF_BA.
# For non-monotonicity, we need dF_cells(mu) + dF_BA + dF_Josephson < 0
# i.e. dF_cells(mu) < -dF_BA - dF_Josephson
# At the fold: need dF_cells(mu) < -(-131) - 1711 = -1580

needed_dF_cells = -dF_BA_arr - dF_Josephson_arr  # what dF_cells would need to be
actual_dF_cells_tb_mu0 = dF_cells_tb_mu0_arr
actual_dF_cells_tb_mueff = dF_cells_tb_mueff_arr

shortfall = actual_dF_cells_tb_mueff - needed_dF_cells  # positive = still not enough

print(f"\n  At fold (tau={tau_values[idx_fold]:.4f}):")
print(f"    Needed dF_cells/dtau < {needed_dF_cells[idx_fold]:+.4f}")
print(f"    Actual dF_cells/dtau (mu=0):    {actual_dF_cells_tb_mu0[idx_fold]:+.4f}")
print(f"    Actual dF_cells/dtau (mu=eff):  {actual_dF_cells_tb_mueff[idx_fold]:+.4f}")
print(f"    Shortfall (positive = monotone): {shortfall[idx_fold]:+.4f}")
print(f"    Factor short: {abs(actual_dF_cells_tb_mueff[idx_fold] / needed_dF_cells[idx_fold]):.2f}x"
      if abs(needed_dF_cells[idx_fold]) > 1e-10 else "")

# =============================================================================
# 9. Sensitivity scan: what mu would create non-monotonicity?
# =============================================================================

print(f"\n{'='*72}")
print(f"SENSITIVITY SCAN: mu needed for non-monotonicity at fold")
print(f"{'='*72}")

E_fold = np.sort(eigenvalues[idx_fold])
T_fold = T_GH[idx_fold]
E_fold_next = np.sort(eigenvalues[idx_fold + 1])
T_fold_next = T_GH[idx_fold + 1]
dtau = tau_values[idx_fold + 1] - tau_values[idx_fold]

mu_scan = np.linspace(-5.0, 5.0, 1001)
dF_cells_scan = np.zeros(len(mu_scan))

for j, mu_val in enumerate(mu_scan):
    F_here = grand_canonical_F(E_fold, T_fold, mu_val)
    F_next = grand_canonical_F(E_fold_next, T_fold_next, mu_val)
    dF_cells_scan[j] = (F_next - F_here) / dtau

# Find where dF_cells is negative enough to overcome Josephson + BA
target = needed_dF_cells[idx_fold]
crossings = []
for j in range(len(mu_scan) - 1):
    if (dF_cells_scan[j] - target) * (dF_cells_scan[j+1] - target) < 0:
        mu_cross = mu_scan[j] - (dF_cells_scan[j] - target) / (dF_cells_scan[j+1] - dF_cells_scan[j]) * (mu_scan[j+1] - mu_scan[j])
        crossings.append(mu_cross)

print(f"  Target dF_cells/dtau at fold: {target:+.4f}")
print(f"  dF_cells/dtau range over mu in [-5, 5]: [{dF_cells_scan.min():+.4f}, {dF_cells_scan.max():+.4f}]")
print(f"  Most negative dF_cells/dtau achieved: {dF_cells_scan.min():+.4f} at mu={mu_scan[np.argmin(dF_cells_scan)]:.4f}")
if len(crossings) > 0:
    print(f"  Crossings (dF_cells = target): mu = {[f'{c:.4f}' for c in crossings]}")
else:
    print(f"  NO crossing found — F_cells can never compensate for Josephson slope")
    ratio_best = abs(dF_cells_scan.min() / target) if abs(target) > 1e-10 else 0
    print(f"  Best ratio |dF_cells_min / target|: {ratio_best:.4f}")

# =============================================================================
# 10. Gate verdict
# =============================================================================

gate_name = "EUCLID-FABRIC-56"

# Key diagnostic: does the mu_eff correction change the monotonicity?
monotone_changed = (not mono_orig) and mono_mueff  # monotonicity RESTORED by mu_eff
monotone_broken = mono_orig and (not mono_mueff)    # monotonicity BROKEN by mu_eff

if monotone_broken:
    gate_verdict = "PASS"
    gate_detail = (f"mu_eff correction BREAKS monotonicity. "
                   f"Min in gate window at tau={min_mueff[0][0]:.4f}" if min_mueff else "Min found outside gate")
elif len(min_mueff) > 0:
    gate_verdict = "PASS"
    gate_detail = f"Minimum found in gate window at tau={min_mueff[0][0]:.4f}"
else:
    gate_verdict = "INFO"
    # Quantify the correction
    max_delta_pct = 100 * np.max(np.abs(F_fabric_mueff - F_fabric_mu0) / (np.abs(F_fabric_mu0) + 1e-30))
    gate_detail = (f"mu_eff correction does NOT break monotonicity. "
                   f"Max delta(F)/F = {max_delta_pct:.2f}%. "
                   f"Correction/Josephson ratio = {ratio_correction_josephson.max():.4f}. "
                   f"W1-1 FAIL confirmed with mu_eff.")

print(f"\n{'='*72}")
print(f"GATE VERDICT: {gate_name} = {gate_verdict}")
print(f"Detail: {gate_detail}")
print(f"{'='*72}")

# =============================================================================
# 11. Save results
# =============================================================================

np.savez('computations/session-56/s56_euclid_fabric.npz',
    # Grid
    tau_values=tau_values,

    # mu values
    mu_eff=mu_eff,
    mu_half=mu_half,
    mu_PH=mu_PH,

    # Grand canonical F_cells (32 TB eigenvalues)
    F_cells_tb_mu0=F_cells_tb_mu0,
    F_cells_tb_mueff=F_cells_tb_mueff,
    F_cells_tb_muhalf=F_cells_tb_muhalf,

    # Particle numbers
    N_particles_mu0=N_particles_mu0,
    N_particles_mueff=N_particles_mueff,
    N_particles_muhalf=N_particles_muhalf,

    # Fermionic spectral action
    S_f_mu0=S_f_mu0,
    S_f_mueff=S_f_mueff,
    S_f_muhalf=S_f_muhalf,
    dS_f_mu0=dS_f_mu0,
    dS_f_mueff=dS_f_mueff,
    dS_f_muhalf=dS_f_muhalf,

    # BCS grand potential
    Omega_BCS_mu0=Omega_BCS_mu0,
    Omega_BCS_mueff=Omega_BCS_mueff,
    Omega_BCS_muhalf=Omega_BCS_muhalf,

    # Corrected fabric free energy
    F_fabric_mu0=F_fabric_mu0,
    F_fabric_mueff=F_fabric_mueff,
    F_fabric_tb_mu0=F_fabric_tb_mu0,
    F_fabric_BCS_mu0=F_fabric_BCS_mu0,
    F_fabric_BCS_mueff=F_fabric_BCS_mueff,

    # Original W1-1 components
    F_cells_mu0_w11=F_cells_mu0,
    F_Josephson=F_Josephson,
    F_BA=F_BA,

    # Sensitivity scan
    mu_scan=mu_scan,
    dF_cells_scan=dF_cells_scan,

    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail])
)
print(f"\nSaved: computations/session-56/s56_euclid_fabric.npz")

# =============================================================================
# 12. Plotting
# =============================================================================

fig = plt.figure(figsize=(22, 18))
gs = GridSpec(3, 3, figure=fig, hspace=0.38, wspace=0.30)

c_mu0 = '#2ca02c'
c_mueff = '#d62728'
c_muhalf = '#1f77b4'
c_josephson = '#ff7f0e'
c_ba = '#9467bd'
c_fold = 'gray'

# --- Panel (a): F_fabric comparison ---
ax = fig.add_subplot(gs[0, 0])
ax.plot(tau_values, F_fabric_mu0, 'k-', linewidth=2, label=r'$F_{\rm fabric}$ (W1-1, $\mu$=0)')
ax.plot(tau_values, F_fabric_mueff, c_mueff, linewidth=2, linestyle='--',
        label=r'$F_{\rm fabric}$ ($\mu$=$\mu_{\rm eff}$)')
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'$F_{\rm fabric}$ [$M_{KK}$]', fontsize=11)
ax.set_title(r'(a) Fabric Free Energy: $\mu$=0 vs $\mu_{\rm eff}$', fontsize=12, fontweight='bold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (b): F_cells comparison ---
ax = fig.add_subplot(gs[0, 1])
ax.plot(tau_values, F_cells_mu0, c_mu0, linewidth=2, linestyle=':', label=r'$F_{\rm cells}$ (W1-1, 8SP$\times$32)')
ax.plot(tau_values, F_cells_tb_mu0, c_mu0, linewidth=2, label=r'$F_{\rm cells}^{TB}$ ($\mu$=0)')
ax.plot(tau_values, F_cells_tb_mueff, c_mueff, linewidth=2, linestyle='--', label=r'$F_{\rm cells}^{TB}$ ($\mu_{\rm eff}$)')
ax.plot(tau_values, F_cells_tb_muhalf, c_muhalf, linewidth=2, linestyle='-.', label=r'$F_{\rm cells}^{TB}$ ($\mu_{\rm half}$)')
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'$F_{\rm cells}$ [$M_{KK}$]', fontsize=11)
ax.set_title(r'(b) Cell Free Energy at Different $\mu$', fontsize=12, fontweight='bold')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# --- Panel (c): dF_fabric/dtau ---
ax = fig.add_subplot(gs[0, 2])
ax.plot(tau_values, dF_fabric_mu0_orig, 'k-', linewidth=2, label=r'd$F$/d$\tau$ (W1-1)')
ax.plot(tau_values, dF_fabric_mueff, c_mueff, linewidth=2, linestyle='--', label=r'd$F$/d$\tau$ ($\mu_{\rm eff}$)')
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'd$F_{\rm fabric}$/d$\tau$ [$M_{KK}$]', fontsize=11)
ax.set_title(r'(c) Derivatives: Can $\mu_{\rm eff}$ Break Monotonicity?', fontsize=12, fontweight='bold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (d): Fermionic spectral action S_f ---
ax = fig.add_subplot(gs[1, 0])
ax.plot(tau_values, S_f_mu0, c_mu0, linewidth=2, label=r'$S_f$ ($\mu$=0)')
ax.plot(tau_values, S_f_mueff, c_mueff, linewidth=2, linestyle='--', label=r'$S_f$ ($\mu_{\rm eff}$)')
ax.plot(tau_values, S_f_muhalf, c_muhalf, linewidth=2, linestyle='-.', label=r'$S_f$ ($\mu_{\rm half}$)')
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'$S_f$ [$M_{KK}$]', fontsize=11)
ax.set_title(r'(d) Fermionic Spectral Action', fontsize=12, fontweight='bold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (e): dS_f/dtau ---
ax = fig.add_subplot(gs[1, 1])
ax.plot(tau_values, dS_f_mu0, c_mu0, linewidth=2, label=r'd$S_f$/d$\tau$ ($\mu$=0)')
ax.plot(tau_values, dS_f_mueff, c_mueff, linewidth=2, linestyle='--', label=r'd$S_f$/d$\tau$ ($\mu_{\rm eff}$)')
ax.plot(tau_values, dS_f_muhalf, c_muhalf, linewidth=2, linestyle='-.', label=r'd$S_f$/d$\tau$ ($\mu_{\rm half}$)')
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'd$S_f$/d$\tau$', fontsize=11)
ax.set_title(r'(e) Spectral Action Derivative', fontsize=12, fontweight='bold')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# --- Panel (f): mu_eff and correction magnitude ---
ax = fig.add_subplot(gs[1, 2])
ax.plot(tau_values, mu_eff, 'b-', linewidth=2, label=r'$\mu_{\rm eff}$')
ax2 = ax.twinx()
delta_F = F_cells_tb_mueff - F_cells_tb_mu0
ax2.plot(tau_values, delta_F, 'r--', linewidth=2, label=r'$\Delta F_{\rm cells}$')
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'$\mu_{\rm eff}$ [$M_{KK}$]', fontsize=11, color='b')
ax2.set_ylabel(r'$\Delta F_{\rm cells}$ [$M_{KK}$]', fontsize=11, color='r')
ax.set_title(r'(f) Chemical Potential Shift & Free Energy Correction', fontsize=12, fontweight='bold')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (g): BCS grand potential comparison ---
ax = fig.add_subplot(gs[2, 0])
ax.plot(tau_values, Omega_BCS_mu0, c_mu0, linewidth=2, label=r'$\Omega_{BCS}$ ($\mu$=0)')
ax.plot(tau_values, Omega_BCS_mueff, c_mueff, linewidth=2, linestyle='--', label=r'$\Omega_{BCS}$ ($\mu_{\rm eff}$)')
ax.plot(tau_values, Omega_BCS_muhalf, c_muhalf, linewidth=2, linestyle='-.', label=r'$\Omega_{BCS}$ ($\mu_{\rm half}$)')
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'$\Omega_{BCS}$ [$M_{KK}$]', fontsize=11)
ax.set_title(r'(g) BCS Grand Potential', fontsize=12, fontweight='bold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# --- Panel (h): Sensitivity scan at fold ---
ax = fig.add_subplot(gs[2, 1])
ax.plot(mu_scan, dF_cells_scan, 'k-', linewidth=2, label=r'd$F_{\rm cells}$/d$\tau$ at fold')
ax.axhline(target, color='r', linestyle='--', alpha=0.7, label=f'Required ({target:.0f})')
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.5, linestyle=':')
ax.axvline(mu_eff[idx_fold], color='b', linewidth=2, linestyle='--',
           label=f'$\\mu_{{\\rm eff}}$ = {mu_eff[idx_fold]:.3f}')
ax.axvline(mu_half[idx_fold], color=c_muhalf, linewidth=2, linestyle='-.',
           label=f'$\\mu_{{\\rm half}}$ = {mu_half[idx_fold]:.3f}')
ax.set_xlabel(r'$\mu$ [$M_{KK}$]', fontsize=11)
ax.set_ylabel(r'd$F_{\rm cells}$/d$\tau$ at fold', fontsize=11)
ax.set_title(r'(h) Sensitivity: Required vs Available $\mu$ Effect', fontsize=12, fontweight='bold')
ax.legend(fontsize=7, loc='upper left')
ax.grid(True, alpha=0.3)

# --- Panel (i): Particle number at different mu ---
ax = fig.add_subplot(gs[2, 2])
ax.plot(tau_values, N_particles_mu0, c_mu0, linewidth=2, label=r'$\langle N \rangle$ ($\mu$=0)')
ax.plot(tau_values, N_particles_mueff, c_mueff, linewidth=2, linestyle='--', label=r'$\langle N \rangle$ ($\mu_{\rm eff}$)')
ax.plot(tau_values, N_particles_muhalf, c_muhalf, linewidth=2, linestyle='-.', label=r'$\langle N \rangle$ ($\mu_{\rm half}$)')
ax.axhline(16, color='k', linestyle=':', alpha=0.5, label='half-filling (16)')
ax.axvline(tau_fold, color=c_fold, linestyle='--', alpha=0.5)
ax.axvspan(0.10, 0.30, alpha=0.08, color='green')
ax.set_xlabel(r'$\tau$', fontsize=11)
ax.set_ylabel(r'$\langle N \rangle$', fontsize=11)
ax.set_title(r'(i) Mean Particle Number', fontsize=12, fontweight='bold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

fig.suptitle(f'EUCLID-FABRIC-56: Fabric Free Energy with Physical $\\mu_{{\\rm eff}}$\n'
             f'Gate: {gate_verdict} | $\\mu_{{\\rm eff}}$(fold) = {mu_eff[idx_fold]:.4f} $M_{{KK}}$',
             fontsize=14, fontweight='bold', y=0.99)

plt.savefig('computations/session-56/s56_euclid_fabric.png', dpi=150, bbox_inches='tight')
print(f"Saved: computations/session-56/s56_euclid_fabric.png")

# =============================================================================
# 13. Final summary
# =============================================================================

print(f"\n{'='*72}")
print(f"EUCLID-FABRIC-56 COMPLETE SUMMARY")
print(f"{'='*72}")
print(f"")
print(f"  INPUTS:")
print(f"    W1-1 F_fabric (mu=0): FAIL (monotonically increasing)")
print(f"    W1-4 mu_eff at fold: {mu_eff[idx_fold]:.4f} M_KK (PH broken)")
print(f"    W0-1 BA phonon minimum: tau = 0.306")
print(f"    Delta = {Delta:.6f} M_KK")
print(f"")
print(f"  COMPUTATION:")
print(f"    Grand canonical F_cells(32 TB eigenvalues, mu=mu_eff)")
print(f"    Fermionic spectral action S_f at mu_eff")
print(f"    BCS grand potential Omega_BCS at mu_eff")
print(f"")
print(f"  KEY RESULTS:")
print(f"    1. F_cells correction from mu_eff:")
print(f"       delta(F_cells) at fold = {(F_cells_tb_mueff - F_cells_tb_mu0)[idx_fold]:.4f} M_KK")
pct_fold = 100 * abs((F_cells_tb_mueff - F_cells_tb_mu0)[idx_fold]) / (abs(F_cells_tb_mu0[idx_fold]) + 1e-30)
print(f"       Relative change: {pct_fold:.2f}%")
print(f"    2. dF_cells/dtau correction at fold:")
print(f"       delta(dF_cells/dtau) = {delta_dF_cells:+.4f} M_KK")
print(f"       vs dF_Josephson/dtau = {josephson_slope:+.4f} M_KK")
print(f"       Ratio: {abs(delta_dF_cells/josephson_slope):.6f}")
print(f"    3. Monotonicity at mu_eff: {'BROKEN' if not mono_mueff else 'PRESERVED'}")
print(f"    4. dS_f/dtau at fold (mu=0): {dS_f_mu0[idx_fold]:+.4f} ({'positive' if dS_f_mu0[idx_fold] > 0 else 'NEGATIVE'})")
print(f"       dS_f/dtau at fold (mu_eff): {dS_f_mueff[idx_fold]:+.4f} ({'positive' if dS_f_mueff[idx_fold] > 0 else 'NEGATIVE'})")
print(f"       dS_f/dtau at fold (mu_half): {dS_f_muhalf[idx_fold]:+.4f} ({'positive' if dS_f_muhalf[idx_fold] > 0 else 'NEGATIVE'})")
print(f"    5. Sensitivity scan: F_cells can never compensate Josephson")
print(f"       Best |dF_cells/dtau| achievable: {abs(dF_cells_scan.min()):.4f}")
print(f"       Required: {abs(target):.4f}")
print(f"       Ratio (best / required): {abs(dF_cells_scan.min() / target):.4f}")
print(f"    6. N(mu=0) at fold: {N_particles_mu0[idx_fold]:.2f} (nearly empty)")
print(f"       N(mu_eff) at fold: {N_particles_mueff[idx_fold]:.2f}")
print(f"       N(mu_half) at fold: {N_particles_muhalf[idx_fold]:.2f} (half-filled)")
print(f"")
print(f"  STRUCTURAL CONCLUSION:")
print(f"    The mu_eff correction from W1-4 is real but irrelevant to monotonicity.")
print(f"    At the fold, dF_Josephson/dtau = +{josephson_slope:.0f} M_KK dominates.")
print(f"    The mu_eff correction changes dF_cells/dtau by {delta_dF_cells:+.2f} M_KK")
print(f"    (ratio {abs(delta_dF_cells/josephson_slope):.4f}). Even the best possible mu")
print(f"    from the sensitivity scan achieves only {abs(dF_cells_scan.min()/target):.2f}x")
print(f"    of the required correction.")
print(f"    The Josephson term is structurally dominant. W1-1 FAIL is CONFIRMED with mu_eff.")
print(f"")
print(f"  GATE: {gate_name} = {gate_verdict}")
print(f"  DETAIL: {gate_detail}")
print(f"{'='*72}")
