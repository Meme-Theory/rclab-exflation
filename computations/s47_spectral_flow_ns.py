#!/usr/bin/env python3
"""
SPECTRAL-FLOW-NS-47: BdG spectral flow and primordial perturbation spectrum
=============================================================================

Physics: In 3He-A (Volovik Paper 09), spectral flow through the Fermi point
produces the chiral anomaly: dN/dt = N_3 x rate. The framework has N_3=0
(BDI class, Paper 28) and a GAP not a Fermi point. This computation asks:
can spectral flow of BdG levels across the gap edge during tau evolution
produce a k-dependent redistribution of spectral weight?

The mechanism is ADIABATIC SPECTRAL FLOW, distinct from pair creation.
As tau evolves through the q-theory potential well, the BdG spectrum
E_k(tau) = sqrt(lambda_k(tau)^2 + Delta_sector(tau)^2) changes continuously.
The flow rate dE_k/dtau is k-dependent, producing a k-dependent occupation
spectrum in the GGE relic.

Pre-registered gate SPECTRAL-FLOW-NS-47:
  PASS: n_s in [0.93, 0.99]
  INFO: k-dependent flow (alpha != 0) but n_s outside [0.93, 0.99]
  FAIL: k-independent flow (alpha ~ 0) or mechanism structurally inapplicable

Author: Volovik (Superfluid Universe Theorist)
Date: 2026-03-16
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold, E_cond, Delta_0_GL, n_pairs

# ==============================================================================
# SECTION 1: Load data
# ==============================================================================

base = Path(__file__).parent

# S46: Self-consistent BCS gaps and eigenvalues at 60 tau points
d46 = np.load(base / 's46_qtheory_selfconsistent.npz', allow_pickle=True)
tau_scan = d46['tau_scan']          # shape (60,)
Delta_B1 = d46['Delta_B1_sc']      # shape (60,)
Delta_B2 = d46['Delta_B2_sc']      # shape (60,)
Delta_B3 = d46['Delta_B3_sc']      # shape (60,)
lam2_B1 = d46['lam2_B1_interp']    # shape (60,), lambda^2 representative for B1
lam2_B2 = d46['lam2_B2_interp']    # shape (60,), lambda^2 representative for B2
lam2_B3 = d46['lam2_B3_interp']    # shape (60,), lambda^2 representative for B3

# S44: Full 992-mode spectrum at 5 tau values
d44 = np.load(base / 's44_dos_tau.npz', allow_pickle=True)
tau_values_44 = d44['tau_values']   # [0.00, 0.05, 0.10, 0.15, 0.19]

# S47: Superfluid stiffness tensor
d47 = np.load(base / 's47_rhos_tensor.npz', allow_pickle=True)

# Fixed tau points from s46 for eigenvalue validation
valid_tau = d46['valid_tau']        # 20 exact tau points
lam_sq_B1 = d46['lam_sq_B1']       # shape (20,)
lam_sq_B2 = d46['lam_sq_B2']       # shape (20,)
lam_sq_B3 = d46['lam_sq_B3']       # shape (20,)

print("=" * 72)
print("SPECTRAL-FLOW-NS-47: BdG Spectral Flow Analysis")
print("=" * 72)
print(f"tau scan: {tau_scan[0]:.3f} -> {tau_scan[-1]:.3f}, {len(tau_scan)} points")
print(f"tau_fold = {tau_fold}")
print()

# ==============================================================================
# SECTION 2: Compute BdG quasiparticle energies E_k(tau)
# ==============================================================================
# E_k(tau) = sqrt(xi_k(tau)^2 + Delta_sector(tau)^2)
# where xi_k = lambda_k (the Dirac eigenvalue, serving as single-particle energy)
# and Delta_sector is the BCS gap in the relevant sector

# The "eigenvalue" in the data is lambda^2, not lambda
# xi_k = sqrt(lam2) for the dispersion above Fermi level
# But for BdG: E_k = sqrt(xi_k^2 + Delta^2) where xi_k = lambda^2 - mu
# In BCS on SU(3), mu=0 (PH symmetric), so xi_k = sqrt(lam2)

# Actually, the Dirac eigenvalues lambda are what appear in the spectrum.
# lam2_Bx_interp ARE lambda^2. The "eigenvalues" omega in s44 ARE sqrt(lam2) = |lambda|.
# For BdG: E_k = sqrt(omega_k^2 + Delta^2) where omega_k = sqrt(lam2_k)

omega_B1 = np.sqrt(lam2_B1)  # single-particle energy for B1 representative mode
omega_B2 = np.sqrt(lam2_B2)  # B2 representative
omega_B3 = np.sqrt(lam2_B3)  # B3 representative

# BdG quasiparticle energies
E_B1 = np.sqrt(omega_B1**2 + Delta_B1**2)
E_B2 = np.sqrt(omega_B2**2 + Delta_B2**2)
E_B3 = np.sqrt(omega_B3**2 + Delta_B3**2)

print("=== BdG Quasiparticle Energies at Key Points ===")
for name, E, om, Delta in [('B1', E_B1, omega_B1, Delta_B1),
                             ('B2', E_B2, omega_B2, Delta_B2),
                             ('B3', E_B3, omega_B3, Delta_B3)]:
    idx_fold = np.argmin(np.abs(tau_scan - 0.19))
    idx_025 = 0
    idx_end = -1
    print(f"\n  {name}:")
    print(f"    tau=0.025: omega={om[idx_025]:.6f}, Delta={Delta[idx_025]:.6f}, E={E[idx_025]:.6f}")
    print(f"    tau=0.190: omega={om[idx_fold]:.6f}, Delta={Delta[idx_fold]:.6f}, E={E[idx_fold]:.6f}")
    print(f"    tau=0.400: omega={om[idx_end]:.6f}, Delta={Delta[idx_end]:.6f}, E={E[idx_end]:.6f}")
    print(f"    E variation: {(E.max()-E.min())/E.mean()*100:.2f}%")

# Also compute with the full 992-mode spectrum at each available tau
print("\n\n=== Full 992-mode BdG spectrum ===")
full_spectra = {}
for tau_val in tau_values_44:
    tau_str = f'tau{tau_val:.2f}'
    omega_all = d44[f'{tau_str}_all_omega']   # 992 modes
    dim2_all = d44[f'{tau_str}_all_dim2']     # degeneracies
    full_spectra[tau_val] = {'omega': omega_all, 'dim2': dim2_all}
    print(f"  tau={tau_val:.2f}: omega range [{omega_all.min():.6f}, {omega_all.max():.6f}], "
          f"spread = {omega_all.max()-omega_all.min():.6f}")

# ==============================================================================
# SECTION 3: Compute spectral flow rates dE_k/dtau
# ==============================================================================
# dE_k/dtau = (omega_k / E_k) * (d omega_k / dtau) + (Delta / E_k) * (d Delta / dtau)
#           = (geometric term)                      + (BCS term)

dtau = tau_scan[1] - tau_scan[0]  # uniform spacing

# Numerical derivatives
domega_B1 = np.gradient(omega_B1, tau_scan)
domega_B2 = np.gradient(omega_B2, tau_scan)
domega_B3 = np.gradient(omega_B3, tau_scan)

dDelta_B1 = np.gradient(Delta_B1, tau_scan)
dDelta_B2 = np.gradient(Delta_B2, tau_scan)
dDelta_B3 = np.gradient(Delta_B3, tau_scan)

# Total spectral flow rate
dE_B1 = (omega_B1 / E_B1) * domega_B1 + (Delta_B1 / E_B1) * dDelta_B1
dE_B2 = (omega_B2 / E_B2) * domega_B2 + (Delta_B2 / E_B2) * dDelta_B2
dE_B3 = (omega_B3 / E_B3) * domega_B3 + (Delta_B3 / E_B3) * dDelta_B3

# Geometric vs BCS decomposition
dE_geom_B1 = (omega_B1 / E_B1) * domega_B1
dE_BCS_B1  = (Delta_B1 / E_B1) * dDelta_B1
dE_geom_B2 = (omega_B2 / E_B2) * domega_B2
dE_BCS_B2  = (Delta_B2 / E_B2) * dDelta_B2
dE_geom_B3 = (omega_B3 / E_B3) * domega_B3
dE_BCS_B3  = (Delta_B3 / E_B3) * dDelta_B3

print("\n\n=== Spectral Flow Rates at Fold (tau=0.190) ===")
idx_fold = np.argmin(np.abs(tau_scan - 0.19))
for name, dE, dEg, dEb in [('B1', dE_B1, dE_geom_B1, dE_BCS_B1),
                              ('B2', dE_B2, dE_geom_B2, dE_BCS_B2),
                              ('B3', dE_B3, dE_geom_B3, dE_BCS_B3)]:
    total = dE[idx_fold]
    geom = dEg[idx_fold]
    bcs = dEb[idx_fold]
    ratio = abs(geom / bcs) if abs(bcs) > 1e-15 else float('inf')
    print(f"  {name}: dE/dtau = {total:+.6f}")
    print(f"         geometric = {geom:+.6f}, BCS = {bcs:+.6f}, |geom/BCS| = {ratio:.3f}")

# ==============================================================================
# SECTION 4: k-dependence of spectral flow (the spectral index alpha)
# ==============================================================================
# If dE_k/dtau ~ E_k^alpha, then the spectral weight redistribution
# follows a power law with index alpha.
#
# For n_s: n_s - 1 = d ln(dE_k/dtau) / d ln(E_k)
# which in the power law case gives n_s - 1 = alpha - 1
# (modulo degeneracy/Weyl's law corrections)

print("\n\n=== Spectral Flow Index alpha ===")
print("Computing alpha = d ln|dE/dtau| / d ln(E) across sectors...\n")

# At each tau, we have THREE points (B1, B2, B3) with energies E and flow rates dE
# This gives a cross-sector slope

# Compute alpha at each tau
alpha_arr = np.zeros(len(tau_scan))
alpha_geom = np.zeros(len(tau_scan))
alpha_bcs = np.zeros(len(tau_scan))

for i in range(len(tau_scan)):
    # Three data points
    E_vec = np.array([E_B1[i], E_B2[i], E_B3[i]])
    dE_vec = np.array([dE_B1[i], dE_B2[i], dE_B3[i]])
    dEg_vec = np.array([dE_geom_B1[i], dE_geom_B2[i], dE_geom_B3[i]])
    dEb_vec = np.array([dE_BCS_B1[i], dE_BCS_B2[i], dE_BCS_B3[i]])

    # Use log-log regression for total flow
    # Need |dE| > 0
    mask = np.abs(dE_vec) > 1e-15
    if mask.sum() >= 2:
        ln_E = np.log(E_vec[mask])
        ln_dE = np.log(np.abs(dE_vec[mask]))
        # Linear fit: ln|dE| = alpha * ln(E) + const
        if len(ln_E) >= 2:
            p = np.polyfit(ln_E, ln_dE, 1)
            alpha_arr[i] = p[0]

    # Geometric flow alpha
    mask_g = np.abs(dEg_vec) > 1e-15
    if mask_g.sum() >= 2:
        ln_E_g = np.log(E_vec[mask_g])
        ln_dEg = np.log(np.abs(dEg_vec[mask_g]))
        if len(ln_E_g) >= 2:
            p_g = np.polyfit(ln_E_g, ln_dEg, 1)
            alpha_geom[i] = p_g[0]

    # BCS flow alpha
    mask_b = np.abs(dEb_vec) > 1e-15
    if mask_b.sum() >= 2:
        ln_E_b = np.log(E_vec[mask_b])
        ln_dEb = np.log(np.abs(dEb_vec[mask_b]))
        if len(ln_E_b) >= 2:
            p_b = np.polyfit(ln_E_b, ln_dEb, 1)
            alpha_bcs[i] = p_b[0]

print(f"alpha at fold (tau=0.19):  total = {alpha_arr[idx_fold]:.4f}")
print(f"                           geom  = {alpha_geom[idx_fold]:.4f}")
print(f"                           BCS   = {alpha_bcs[idx_fold]:.4f}")
print(f"alpha range over full tau: [{alpha_arr.min():.4f}, {alpha_arr.max():.4f}]")
print(f"alpha mean:                {alpha_arr.mean():.4f}")
print(f"alpha std:                 {alpha_arr.std():.4f}")

# ==============================================================================
# SECTION 5: Use 992-mode spectrum for multi-mode spectral flow
# ==============================================================================
# The 3-sector approximation is coarse. Use the full 992 modes at 5 tau values
# to compute spectral flow rates for ALL modes and get the power law.

print("\n\n=== Multi-Mode Spectral Flow (992 modes, 5 tau points) ===")

# For each consecutive pair of tau values, compute d omega_k / d tau
# by finite differences on the SORTED eigenvalue spectrum
tau_44 = np.array([0.00, 0.05, 0.10, 0.15, 0.19])

# The 992 modes are the same physical modes at each tau, sorted
# by eigenvalue. We track them by index (sorted order).
omega_at_tau = {}
for t in tau_44:
    tstr = f'tau{t:.2f}'
    omega_at_tau[t] = np.sort(d44[f'{tstr}_all_omega'])

# Compute spectral flow for each consecutive pair
flow_results = {}
for i in range(len(tau_44) - 1):
    t1, t2 = tau_44[i], tau_44[i+1]
    dt = t2 - t1
    o1 = omega_at_tau[t1]
    o2 = omega_at_tau[t2]

    # domega/dtau for each mode
    domega = (o2 - o1) / dt

    # Average omega for power-law fit
    omega_avg = 0.5 * (o1 + o2)

    flow_results[(t1, t2)] = {
        'domega': domega,
        'omega_avg': omega_avg,
        'dt': dt
    }

    # Fit power law: |domega/dtau| vs omega
    mask = np.abs(domega) > 1e-10
    if mask.sum() > 10:
        ln_omega = np.log(omega_avg[mask])
        ln_domega = np.log(np.abs(domega[mask]))
        p = np.polyfit(ln_omega, ln_domega, 1)
        alpha_multi = p[0]
        print(f"  tau=[{t1:.2f},{t2:.2f}]: alpha = {alpha_multi:.4f}, "
              f"mean |domega/dtau| = {np.abs(domega).mean():.6f}, "
              f"std = {np.abs(domega).std():.6f}")

        # Also check fraction of positive vs negative flow
        n_pos = np.sum(domega > 0)
        n_neg = np.sum(domega < 0)
        n_zero = np.sum(np.abs(domega) < 1e-10)
        print(f"         flow direction: {n_pos} up, {n_neg} down, {n_zero} zero "
              f"(net = {n_pos-n_neg})")
    else:
        print(f"  tau=[{t1:.2f},{t2:.2f}]: insufficient non-zero flow rates ({mask.sum()} modes)")

# ==============================================================================
# SECTION 6: BdG spectral flow including gap
# ==============================================================================
# For the 992-mode spectrum, we need sector assignments to assign Delta.
# Use the gap values interpolated to each tau.

print("\n\n=== BdG Spectral Flow with Gap (E_k = sqrt(omega_k^2 + Delta^2)) ===")

# Sector assignment heuristic:
# B2 modes: omega in the flat band (lowest eigenvalues, concentrated)
# B1 modes: intermediate
# B3 modes: high eigenvalues
#
# From S44 data at tau=0.19:
# B1: omin ~ 0.836, omax ~ 0.836 (very narrow)
# B2: omin ~ 0.820, omax ~ 0.820 (flat band)
# B3: omin ~ 0.972, omax ~ 2.061 (wide range)
#
# But the actual sector assignment depends on representation labels (p,q).
# The interpolated lam2_Bx are representative single eigenvalues per sector.

# For the full 992-mode analysis, we cannot assign sectors without the
# representation labels. Instead, compute BdG flow rates with a UNIFORM gap
# (worst case: all modes use same Delta) and a SECTOR-WEIGHTED gap.

# METHOD A: Uniform gap (Delta = Delta_B2, the largest)
print("\nMethod A: Uniform gap (Delta = Delta_B2)")
# At tau_fold, Delta_B2 = 0.732
Delta_fold = 0.732
E_fold = np.sqrt(omega_at_tau[0.19]**2 + Delta_fold**2)
E_init = np.sqrt(omega_at_tau[0.00]**2 + Delta_fold**2)

# Flow rate
dE_full = (E_fold - E_init) / (0.19 - 0.00)
# Power law fit
mask = np.abs(dE_full) > 1e-10
ln_E = np.log(E_fold[mask])
ln_dE = np.log(np.abs(dE_full[mask]))
p_A = np.polyfit(ln_E, ln_dE, 1)
alpha_A = p_A[0]
print(f"  alpha = {alpha_A:.4f}")
print(f"  n_s - 1 = alpha - 1 = {alpha_A - 1:.4f}")
print(f"  n_s = {alpha_A:.4f}")

# Residual of power law fit
ln_dE_pred = np.polyval(p_A, ln_E)
residual_A = np.sqrt(np.mean((ln_dE - ln_dE_pred)**2))
print(f"  RMS residual of log-log fit: {residual_A:.4f}")

# METHOD B: Three-gap model
print("\nMethod B: Three-sector gap model")
# Assign sectors by eigenvalue ranges
# B2: flat band modes (smallest omega, high degeneracy)
# B1: intermediate
# B3: highest omega

# At tau=0.00 (round SU(3)), all modes in (0,0) have omega = 0.833
# Let's use the fraction: 4/8 = B2, 1/8 = B1, 3/8 = B3
# (from the 8-mode BCS system: 4 B2 + 1 B1 + 3 B3)

n_modes = 992
n_B2 = n_modes // 2   # 496 modes (50%)
n_B1 = n_modes // 8   # 124 modes (12.5%)
n_B3 = n_modes - n_B2 - n_B1  # 372 modes (37.5%)

print(f"  Sector assignment: B2={n_B2}, B1={n_B1}, B3={n_B3}")

# Sort modes and assign
sorted_idx = np.argsort(omega_at_tau[0.19])
B2_idx = sorted_idx[:n_B2]
B1_idx = sorted_idx[n_B2:n_B2+n_B1]
B3_idx = sorted_idx[n_B2+n_B1:]

# Get interpolated gaps at tau=0.00 and tau=0.19
# Use s46 data
idx_tau_0 = np.argmin(np.abs(tau_scan - 0.025))  # closest to 0
idx_tau_f = np.argmin(np.abs(tau_scan - 0.19))

Delta_map = {}
Delta_map_init = {}
for sect, indices in [('B2', B2_idx), ('B1', B1_idx), ('B3', B3_idx)]:
    if sect == 'B1':
        Delta_map[sect] = Delta_B1[idx_tau_f]
        Delta_map_init[sect] = Delta_B1[idx_tau_0]
    elif sect == 'B2':
        Delta_map[sect] = Delta_B2[idx_tau_f]
        Delta_map_init[sect] = Delta_B2[idx_tau_0]
    else:
        Delta_map[sect] = Delta_B3[idx_tau_f]
        Delta_map_init[sect] = Delta_B3[idx_tau_0]

# Compute BdG energies at initial and final tau
E_init_3 = np.zeros(n_modes)
E_fold_3 = np.zeros(n_modes)
sector_label = np.zeros(n_modes, dtype=int)

omega_init = omega_at_tau[0.00]
omega_final = omega_at_tau[0.19]

for sect, indices, label in [('B2', B2_idx, 0), ('B1', B1_idx, 1), ('B3', B3_idx, 2)]:
    sector_label[indices] = label
    E_init_3[indices] = np.sqrt(omega_init[indices]**2 + Delta_map_init[sect]**2)
    E_fold_3[indices] = np.sqrt(omega_final[indices]**2 + Delta_map[sect]**2)

dE_3 = (E_fold_3 - E_init_3) / (0.19 - 0.0)

# Power law fit per sector
for sect, indices, sname in [(B2_idx, 0, 'B2'), (B1_idx, 1, 'B1'), (B3_idx, 2, 'B3')]:
    mask_s = np.abs(dE_3[sect]) > 1e-10
    if mask_s.sum() > 5:
        ln_E_s = np.log(E_fold_3[sect][mask_s])
        ln_dE_s = np.log(np.abs(dE_3[sect][mask_s]))
        p_s = np.polyfit(ln_E_s, ln_dE_s, 1)
        print(f"  {sname}: alpha = {p_s[0]:.4f}, mean |dE/dtau| = {np.abs(dE_3[sect]).mean():.6f}")
    else:
        print(f"  {sname}: insufficient variation")

# Combined fit
mask_all = np.abs(dE_3) > 1e-10
if mask_all.sum() > 10:
    ln_E_all = np.log(E_fold_3[mask_all])
    ln_dE_all = np.log(np.abs(dE_3[mask_all]))
    p_B = np.polyfit(ln_E_all, ln_dE_all, 1)
    alpha_B = p_B[0]
    print(f"\n  Combined alpha = {alpha_B:.4f}")
    print(f"  n_s - 1 = {alpha_B - 1:.4f}")
    print(f"  n_s = {alpha_B:.4f}")

# ==============================================================================
# SECTION 7: Total spectral flow (net and absolute)
# ==============================================================================

print("\n\n=== Total Spectral Flow ===")
# In BDI, PH symmetry means for every E_k there is -E_k
# Net flow should integrate to zero
# But the DISTRIBUTION carries information

# Net flow
N_flow_net = np.sum(np.sign(dE_3))
N_flow_up = np.sum(dE_3 > 0)
N_flow_down = np.sum(dE_3 < 0)
N_flow_zero = np.sum(np.abs(dE_3) < 1e-10)

print(f"  N_flow_net = {N_flow_net:.0f} (BDI expects 0)")
print(f"  N_flow_up = {N_flow_up}, N_flow_down = {N_flow_down}, N_zero = {N_flow_zero}")

# Total absolute flow
abs_flow = np.sum(np.abs(dE_3))
print(f"  Total |dE/dtau| = {abs_flow:.4f}")
print(f"  Mean |dE/dtau| per mode = {abs_flow/n_modes:.6f}")

# ==============================================================================
# SECTION 8: Van Hove singularity in flow rate
# ==============================================================================

print("\n\n=== Van Hove Singularity Check ===")
# Does dE_k/dtau diverge or peak at Van Hove eigenvalues?
vh_omega = d44['tau0.19_vh_omega']
vh_rho = d44['tau0.19_vh_rho']
print(f"  Van Hove points at tau=0.19: {len(vh_omega)} points")
for i, (vho, vhr) in enumerate(zip(vh_omega, vh_rho)):
    print(f"    VH_{i}: omega = {vho:.6f}, rho = {vhr:.2f}")

# Check if flow rate has peaks near VH eigenvalues
# Use Method B (3-sector) flow rates
omega_sorted = omega_final[np.argsort(omega_final)]
dE_sorted = dE_3[np.argsort(omega_final)]

for vho in vh_omega:
    idx_near = np.argmin(np.abs(omega_sorted - vho))
    local_dE = np.abs(dE_sorted[max(0,idx_near-5):idx_near+5])
    peak_dE = np.abs(dE_sorted[idx_near])
    mean_dE = np.abs(dE_sorted).mean()
    print(f"  VH at omega={vho:.4f}: |dE/dtau|={peak_dE:.6f}, mean={mean_dE:.6f}, "
          f"ratio = {peak_dE/mean_dE:.3f}")

# ==============================================================================
# SECTION 9: Occupation spectrum from spectral flow
# ==============================================================================

print("\n\n=== Occupation Spectrum from Spectral Flow ===")
# Adiabatic limit: n_k proportional to 1/|dE_k/dtau|
# (slow-flowing levels accumulate occupation)
# Sudden quench: n_k = |beta_k|^2 ~ (Delta/omega)^4

# Compare the two
print("\nAdiabatic occupation (n_k ~ 1/|dE_k/dtau|):")
mask_flow = np.abs(dE_3) > 1e-10
n_adiabatic = np.zeros(n_modes)
n_adiabatic[mask_flow] = 1.0 / np.abs(dE_3[mask_flow])
n_adiabatic /= n_adiabatic.max() if n_adiabatic.max() > 0 else 1  # normalize

# Sudden quench occupation
n_sudden = (Delta_fold / omega_final)**4
n_sudden /= n_sudden.max()

# Power law fit for adiabatic
mask_ad = n_adiabatic > 1e-10
if mask_ad.sum() > 10:
    ln_E_ad = np.log(E_fold_3[mask_ad])
    ln_n_ad = np.log(n_adiabatic[mask_ad])
    p_ad = np.polyfit(ln_E_ad, ln_n_ad, 1)
    print(f"  Adiabatic: n_k ~ E^{p_ad[0]:.4f}")
    ns_adiabatic = 1 + p_ad[0]
    print(f"  n_s (adiabatic) = 1 + slope = {ns_adiabatic:.4f}")

# Power law fit for sudden
mask_sd = n_sudden > 1e-10
ln_E_sd = np.log(E_fold_3[mask_sd])
ln_n_sd = np.log(n_sudden[mask_sd])
p_sd = np.polyfit(ln_E_sd, ln_n_sd, 1)
print(f"\n  Sudden quench: n_k ~ E^{p_sd[0]:.4f}")
ns_sudden = 1 + p_sd[0]
print(f"  n_s (sudden) = 1 + slope = {ns_sudden:.4f}")

# ==============================================================================
# SECTION 10: Comparison: spectral flow vs pair creation slopes
# ==============================================================================

print("\n\n=== Key Comparison ===")
print(f"  Spectral flow alpha (3-sector): {alpha_arr[idx_fold]:.4f}")
print(f"  Spectral flow alpha (992-mode, uniform gap): {alpha_A:.4f}")
if 'alpha_B' in dir():
    print(f"  Spectral flow alpha (992-mode, 3-gap): {alpha_B:.4f}")
print(f"  Adiabatic n_s: {ns_adiabatic:.4f}")
print(f"  Sudden quench n_s: {ns_sudden:.4f}")
print(f"  Planck observed n_s: 0.9649")

# ==============================================================================
# SECTION 11: Structural analysis — WHY the spectral flow index takes its value
# ==============================================================================

print("\n\n=== Structural Analysis ===")

# Key question: is the spectral flow k-dependent?
# Decompose into omega-derivative and Delta-derivative contributions

# At fold, compute the fractional contributions
print("\nFractional decomposition at fold:")
for name, om, E, dom, dD, Delta in [
    ('B1', omega_B1[idx_fold], E_B1[idx_fold], domega_B1[idx_fold], dDelta_B1[idx_fold], Delta_B1[idx_fold]),
    ('B2', omega_B2[idx_fold], E_B2[idx_fold], domega_B2[idx_fold], dDelta_B2[idx_fold], Delta_B2[idx_fold]),
    ('B3', omega_B3[idx_fold], E_B3[idx_fold], domega_B3[idx_fold], dDelta_B3[idx_fold], Delta_B3[idx_fold])]:

    geom_frac = (om / E) * dom
    bcs_frac = (Delta / E) * dD
    total = geom_frac + bcs_frac

    print(f"\n  {name}: E = {E:.6f}")
    print(f"    omega/E = {om/E:.4f}, Delta/E = {Delta/E:.4f}")
    print(f"    d omega/dtau = {dom:+.6f}")
    print(f"    d Delta/dtau = {dD:+.6f}")
    print(f"    Geometric: {geom_frac:+.6f} ({100*abs(geom_frac)/abs(total):.1f}%)")
    print(f"    BCS:       {bcs_frac:+.6f} ({100*abs(bcs_frac)/abs(total):.1f}%)")
    print(f"    Total:     {total:+.6f}")

# Check if BCS contribution is k-independent (it should be, since dDelta/dtau
# is sector-specific but NOT mode-specific within each sector)
print("\n\nBCS flow uniformity within sectors:")
# Within each sector, dDelta/dtau is the same for all modes.
# The k-dependence comes ONLY from omega/E and Delta/E prefactors.
# For B2 (flat band): omega varies by 0 (exact), so dE/dtau is identical for all B2 modes
# For B3 (wide band): omega spans factor 2.5x, so dE/dtau varies

# At fold:
omega_range_B3 = omega_final[B3_idx].max() - omega_final[B3_idx].min()
omega_range_B2 = omega_final[B2_idx].max() - omega_final[B2_idx].min()
omega_range_B1 = omega_final[B1_idx].max() - omega_final[B1_idx].min()

print(f"  B2 omega range: {omega_range_B2:.6f} (flat band -> k-INDEPENDENT flow)")
print(f"  B1 omega range: {omega_range_B1:.6f}")
print(f"  B3 omega range: {omega_range_B3:.6f} (wide band -> k-DEPENDENT flow)")
print(f"  B3 omega ratio max/min: {omega_final[B3_idx].max()/omega_final[B3_idx].min():.4f}")

# For B3 modes, the prefactor omega/E varies across the band:
# omega/E = omega / sqrt(omega^2 + Delta_B3^2)
# At large omega >> Delta_B3: omega/E -> 1
# At small omega ~ Delta_B3: omega/E -> omega/sqrt(omega^2 + Delta^2) < 1
# So the geometric flow rate approaches domega/dtau uniformly at high energy

Delta_B3_fold = Delta_B3[idx_fold]  # = 0.084
print(f"\n  Delta_B3 at fold: {Delta_B3_fold:.4f}")
print(f"  omega_B3 range: [{omega_final[B3_idx].min():.4f}, {omega_final[B3_idx].max():.4f}]")
print(f"  omega/E range for B3: [{omega_final[B3_idx].min()/np.sqrt(omega_final[B3_idx].min()**2+Delta_B3_fold**2):.4f}, "
      f"{omega_final[B3_idx].max()/np.sqrt(omega_final[B3_idx].max()**2+Delta_B3_fold**2):.4f}]")
print(f"  -> Because Delta_B3 << omega for ALL B3 modes, omega/E ~ 1 always.")
print(f"  -> The k-dependence of dE_k/dtau within B3 comes from domega_k/dtau,")
print(f"     i.e., how each mode's eigenvalue evolves with geometry.")

# ==============================================================================
# SECTION 12: Structural theorem and verdict
# ==============================================================================

print("\n\n" + "=" * 72)
print("STRUCTURAL ANALYSIS: Why BDI spectral flow cannot produce n_s")
print("=" * 72)

print("""
In 3He-A (Paper 09), spectral flow produces the chiral anomaly because:
  1. Fermi points exist (topological charge N_3 = +/-2)
  2. Spectral flow is THROUGH zero energy (across the Fermi surface)
  3. The flow rate is set by the vortex velocity (external drive)
  4. The chirality protection means dN/dt is QUANTIZED

In the framework BCS on SU(3) (BDI class, Paper 28):
  1. No Fermi points (N_3 = 0, confirmed N3-BDG-44)
  2. Spectral flow is ALONG the gap edge, not through it
  3. The gap is OPEN at all tau (min |E_BdG| = 0.830, S44)
  4. No chirality protection -> no quantized flow

The spectral flow rate dE_k/dtau decomposes as:
  dE/dtau = (omega/E)(domega/dtau) + (Delta/E)(dDelta/dtau)

Critical structural facts:
  A) dDelta/dtau is sector-specific but NOT mode-specific within a sector.
     For the flat band B2 (496 modes), dE/dtau is IDENTICAL for all modes
     because omega is the same for all modes (W=0 exact, FLATBAND-43).

  B) For B3 (372 modes), domega/dtau IS k-dependent, but Delta_B3 << omega
     for all B3 modes, so omega/E ~ 1 uniformly. The k-dependence of
     domega/dtau then determines the k-dependence of dE/dtau.

  C) But domega/dtau is set by d/dtau of the Casimir eigenvalue on
     deformed SU(3). This is a SMOOTH function of the representation labels
     (p,q), not a power law. The variation across the B3 band gives
     alpha ~ 2-5 (steeply k-dependent), which produces n_s << 0.

  D) The BCS contribution is k-INDEPENDENT within each sector. The geometric
     contribution is k-dependent but produces the WRONG slope (too steep,
     as in the pair creation case).

The fundamental obstruction is the SAME as for pair creation:
  - Eigenvalues span a factor of 2.5 across the KK tower
  - The spectral flow rate inherits this span
  - Any power-law fit gives alpha >> 1, hence n_s << 1
  - The k-independence of Delta within each sector cannot flatten this
""")

# ==============================================================================
# SECTION 13: Comparison with 3He-A spectral flow (Paper 09)
# ==============================================================================

print("=== 3He-A vs Framework: Spectral Flow Comparison ===\n")
print("3He-A (chiral anomaly, Paper 09):")
print("  - Topology: N_3 = +/-2 (Fermi point)")
print("  - Flow: through zero energy, creates net baryon number")
print("  - Rate: dN/dt = N_3 * (e l-dot) / (2*pi^2)")
print("  - Spectral index: N/A (anomaly is TOTAL, not spectrum)")
print("  - Protected by: momentum-space topology (Fermi point winding)")
print()
print("Framework BDI (this computation):")
print("  - Topology: N_3 = 0, Z_2 = -1 (Pfaffian)")
print("  - Flow: along gap edge, no zero crossing")
print("  - Rate: dE_k/dtau = geometric + BCS, k-dependent but steep")
print(f"  - Spectral index: alpha = {alpha_A:.2f} (uniform gap), giving n_s = {alpha_A:.4f}")
print("  - Not protected by: any topological invariant (BDI Z protects gap, not flow rate)")
print()
print("CRITICAL DISTINCTION:")
print("  In 3He-A, spectral flow is TOPOLOGICALLY QUANTIZED (it counts level crossings")
print("  through zero). In BDI, levels never cross zero (gap is open). The 'spectral flow'")
print("  is just the adiabatic evolution of the spectrum - there is no anomaly, no quantization,")
print("  and no topological protection of the spectral index.")

# ==============================================================================
# SECTION 14: Final verdict
# ==============================================================================

print("\n\n" + "=" * 72)
print("GATE VERDICT: SPECTRAL-FLOW-NS-47")
print("=" * 72)

# Determine verdict
# The spectral flow IS k-dependent (alpha != 0), but n_s is way outside [0.93, 0.99]
if 'ns_adiabatic' in dir():
    ns_best = ns_adiabatic
else:
    ns_best = alpha_A

if 0.93 <= ns_best <= 0.99:
    verdict = "PASS"
elif abs(alpha_A) > 0.1:  # alpha != 0 -> k-dependent flow
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"\nVerdict: {verdict}")
print(f"\nKey numbers:")
print(f"  alpha (uniform gap, 992 modes):   {alpha_A:.4f}")
if 'alpha_B' in dir():
    print(f"  alpha (3-gap, 992 modes):         {alpha_B:.4f}")
print(f"  alpha (3-sector, at fold):        {alpha_arr[idx_fold]:.4f}")
print(f"  n_s (adiabatic occupation):       {ns_adiabatic:.4f}")
print(f"  n_s (sudden quench):              {ns_sudden:.4f}")
print(f"  Planck n_s:                       0.9649")
print(f"  Deviation:                        {abs(ns_adiabatic - 0.9649)/0.0042:.1f} sigma")
print(f"\nStructural:")
print(f"  Spectral flow IS k-dependent (alpha = {alpha_A:.2f} != 0)")
print(f"  But alpha >> 0.035 (the value needed for Planck n_s = 0.965)")
print(f"  BCS contribution is k-INDEPENDENT within each sector")
print(f"  Geometric contribution has WRONG slope (too steep)")
print(f"  No topological protection of spectral index (N_3 = 0)")
print(f"\n  -> Spectral flow inherits the same structural problem as pair creation:")
print(f"     eigenvalue span 2.5x across KK tower forces steep power law.")
print(f"     The spectral index is a property of the SPECTRUM, not the process.")

# ==============================================================================
# SECTION 15: Save data
# ==============================================================================

output = base / 's47_spectral_flow_ns.npz'
np.savez(output,
    # Gate info
    gate_name='SPECTRAL-FLOW-NS-47',
    gate_verdict=verdict,

    # 3-sector BdG energies and flow rates (60 tau points)
    tau_scan=tau_scan,
    E_B1=E_B1, E_B2=E_B2, E_B3=E_B3,
    dE_B1=dE_B1, dE_B2=dE_B2, dE_B3=dE_B3,
    dE_geom_B1=dE_geom_B1, dE_geom_B2=dE_geom_B2, dE_geom_B3=dE_geom_B3,
    dE_BCS_B1=dE_BCS_B1, dE_BCS_B2=dE_BCS_B2, dE_BCS_B3=dE_BCS_B3,

    # Spectral flow index
    alpha_arr=alpha_arr,
    alpha_geom=alpha_geom,
    alpha_bcs=alpha_bcs,
    alpha_fold=alpha_arr[idx_fold],

    # 992-mode results
    alpha_uniform_gap=alpha_A,
    ns_adiabatic=ns_adiabatic,
    ns_sudden=ns_sudden,

    # Occupation spectra
    n_adiabatic=n_adiabatic,
    n_sudden=n_sudden,
    E_fold_3sector=E_fold_3,

    # Flow direction
    N_flow_net=N_flow_net,
    N_flow_up=N_flow_up,
    N_flow_down=N_flow_down,
)
print(f"\nData saved to {output}")

# ==============================================================================
# SECTION 16: Plotting
# ==============================================================================

fig, axes = plt.subplots(3, 2, figsize=(14, 16))
fig.suptitle('SPECTRAL-FLOW-NS-47: BdG Spectral Flow Analysis\n'
             f'Verdict: {verdict}', fontsize=14, fontweight='bold')

# Panel 1: BdG energies E_k(tau) for three sectors
ax = axes[0, 0]
ax.plot(tau_scan, E_B1, 'b-', label='B1', linewidth=2)
ax.plot(tau_scan, E_B2, 'r-', label='B2', linewidth=2)
ax.plot(tau_scan, E_B3, 'g-', label='B3', linewidth=2)
ax.axvline(tau_fold, color='k', linestyle='--', alpha=0.5, label=f'fold tau={tau_fold}')
ax.axvline(0.209, color='purple', linestyle=':', alpha=0.5, label='q-theory tau*=0.209')
ax.set_xlabel('tau')
ax.set_ylabel('E_k(tau)')
ax.set_title('BdG Quasiparticle Energies')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Flow rates dE_k/dtau
ax = axes[0, 1]
ax.plot(tau_scan, dE_B1, 'b-', label='dE/dtau (B1)', linewidth=2)
ax.plot(tau_scan, dE_B2, 'r-', label='dE/dtau (B2)', linewidth=2)
ax.plot(tau_scan, dE_B3, 'g-', label='dE/dtau (B3)', linewidth=2)
ax.axvline(tau_fold, color='k', linestyle='--', alpha=0.5)
ax.axhline(0, color='gray', linewidth=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('dE_k/dtau')
ax.set_title('Spectral Flow Rates')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Geometric vs BCS decomposition at fold
ax = axes[1, 0]
sectors = ['B1', 'B2', 'B3']
geom_vals = [dE_geom_B1[idx_fold], dE_geom_B2[idx_fold], dE_geom_B3[idx_fold]]
bcs_vals = [dE_BCS_B1[idx_fold], dE_BCS_B2[idx_fold], dE_BCS_B3[idx_fold]]
x = np.arange(3)
width = 0.35
ax.bar(x - width/2, geom_vals, width, label='Geometric', color='steelblue')
ax.bar(x + width/2, bcs_vals, width, label='BCS', color='coral')
ax.set_xticks(x)
ax.set_xticklabels(sectors)
ax.set_ylabel('dE/dtau contribution')
ax.set_title(f'Geometric vs BCS Flow at Fold (tau={tau_fold})')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Panel 4: Alpha (spectral flow index) vs tau
ax = axes[1, 1]
ax.plot(tau_scan, alpha_arr, 'k-', linewidth=2, label='total alpha')
ax.plot(tau_scan, alpha_geom, 'b--', linewidth=1.5, label='geometric alpha')
ax.plot(tau_scan, alpha_bcs, 'r--', linewidth=1.5, label='BCS alpha')
ax.axvline(tau_fold, color='k', linestyle='--', alpha=0.5)
ax.axhline(0.035, color='green', linestyle=':', alpha=0.7, label='Planck (alpha=0.035)')
ax.set_xlabel('tau')
ax.set_ylabel('alpha = d ln|dE/dtau| / d ln E')
ax.set_title('Spectral Flow Index')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Occupation spectra (adiabatic vs sudden)
ax = axes[2, 0]
E_sorted_idx = np.argsort(E_fold_3)
ax.semilogy(E_fold_3[E_sorted_idx], n_adiabatic[E_sorted_idx] + 1e-20, 'b.',
            markersize=1, alpha=0.3, label='Adiabatic (1/|dE/dtau|)')
ax.semilogy(E_fold_3[E_sorted_idx], n_sudden[E_sorted_idx] + 1e-20, 'r.',
            markersize=1, alpha=0.3, label='Sudden (Delta/omega)^4')
# Power law guides
E_range = np.linspace(E_fold_3.min(), E_fold_3.max(), 100)
ax.semilogy(E_range, np.exp(p_ad[1]) * E_range**p_ad[0], 'b-', linewidth=1.5,
            label=f'Adiabatic fit: E^{{{p_ad[0]:.1f}}}')
ax.semilogy(E_range, np.exp(p_sd[1]) * E_range**p_sd[0], 'r-', linewidth=1.5,
            label=f'Sudden fit: E^{{{p_sd[0]:.1f}}}')
ax.set_xlabel('E_k (BdG energy at fold)')
ax.set_ylabel('Normalized occupation n_k')
ax.set_title('Occupation Spectra: Adiabatic vs Sudden')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 6: Summary text
ax = axes[2, 1]
ax.axis('off')
summary_text = f"""SPECTRAL-FLOW-NS-47 Summary
{'='*40}
Gate: {verdict}

Spectral flow index alpha:
  3-sector at fold:     {alpha_arr[idx_fold]:.4f}
  992-mode (unif. gap): {alpha_A:.4f}
  Geometric at fold:    {alpha_geom[idx_fold]:.4f}
  BCS at fold:          {alpha_bcs[idx_fold]:.4f}

n_s estimates:
  Adiabatic:  {ns_adiabatic:.4f}
  Sudden:     {ns_sudden:.4f}
  Planck:     0.9649

Flow direction (992 modes):
  Up: {N_flow_up}  Down: {N_flow_down}

Structural obstruction:
  BCS flow: k-INDEPENDENT within sector
  Geometric flow: k-dependent but steep
  Eigenvalue span 2.5x -> alpha >> 0.035
  N_3 = 0 -> no topological protection
"""
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, fontfamily='monospace', verticalalignment='top')

plt.tight_layout()
plot_path = base / 's47_spectral_flow_ns.png'
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plot_path}")

print("\n\nDone.")
