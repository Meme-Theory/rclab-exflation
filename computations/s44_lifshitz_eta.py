#!/usr/bin/env python3
"""
LIFSHITZ-ETA-44: Anomalous dimension eta at the Type I Lifshitz transition
on SU(3), and its implication for the spectral tilt n_s.

Physics:
--------
The Dirac operator D_K on SU(3) with Jensen deformation parameter tau
undergoes a Type I Lifshitz transition at tau = 0. At the round metric
(tau = 0), the spectrum has maximal SU(3) degeneracy: 992 eigenvalues
collapse to N_eff = 32 distinct values. As tau departs from zero,
degeneracy breaks to N_eff = 240, and the spectral topology changes.

The anomalous dimension eta characterizes the power-law correction to
the two-point correlator at the critical point:
    G(k) ~ 1/|k|^{2 - eta}

For the spectral tilt n_s, the relevant quantity is the two-point function
of perturbation modes delta_tau projected from the internal SU(3) lattice
onto 4D spacetime. The power spectrum is:
    P(k) = <|delta_tau(k)|^2> / M_pl^2
where the mode amplitude is determined by the INVERSE propagator
(stiffness) of the spectral action.

Key insight: the n_s - 1 = -eta_eff relation involves eta_eff computed
from the STIFFNESS of the spectral action projected onto mode k, not
from the spectral response. The stiffness is:
    K(k) = d^2 S / d(delta_tau(k))^2
and the power spectrum goes as P(k) ~ 1/K(k).

Author: Landau Condensed Matter Theorist (Session 44, Wave 1)
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# SECTION 1: Load all input data
# ============================================================

base = Path(r'C:\sandbox\Ainulindale Exflation\tier0-computation')

d41 = np.load(base / 's41_spectral_refinement.npz', allow_pickle=True)
d36 = np.load(base / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d43_dos = np.load(base / 's43_phonon_dos.npz', allow_pickle=True)
d43_lif = np.load(base / 's43_lifshitz_class.npz', allow_pickle=True)
d36_mmax = np.load(base / 's36_mmax_authoritative.npz', allow_pickle=True)

# Extract key arrays
tau_s41 = d41['tau_values']
N_eff_s41 = d41['N_eff']
tau_combined = d36['tau_combined']
S_full = d36['S_full']

omega_fold = d43_dos['all_omega']
sector_p = d43_dos['all_sector_p']
sector_q = d43_dos['all_sector_q']
omega_gap = float(d43_dos['omega_gap'])
vh_omega = d43_dos['vh_omega']
vh_types = d43_dos['vh_types']
vh_rho = d43_dos['vh_rho']
group_names = d43_dos['group_names']
group_n_phys = d43_dos['group_n_phys']
group_n_ev = d43_dos['group_n_ev']

tau_dense = d43_lif['tau_dense']
B1_traj = d43_lif['B1_traj']
B2_traj = d43_lif['B2_traj']
B3_traj = d43_lif['B3_traj']

M_max = float(d36_mmax['M_8x8'])

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

print("=" * 70)
print("LIFSHITZ-ETA-44: Anomalous Dimension at Type I Lifshitz Transition")
print("=" * 70)

# ============================================================
# SECTION 2: Eigenvalue structure at round metric and fold
# ============================================================

# Round metric eigenvalue (tau -> 0 limit)
# At tau = 0, B1 = B2 = B3 by SU(3) symmetry
# Use tau = 0.001 data as proxy
B1_0 = B1_traj[0]  # tau = 0.001
B2_0 = B2_traj[0]
B3_0 = B3_traj[0]
lambda_round = (B1_0 + B2_0 + B3_0) / 3.0

print(f"\n--- Eigenvalue structure ---")
print(f"  Round metric (tau->0): lambda_0 = {lambda_round:.8f}")
print(f"  Split at tau=0.001: B3-B1 = {B3_0 - B1_0:.8f}")
print(f"  Fold (tau=0.20): B1={B1_traj[16]:.8f}, B2={B2_traj[16]:.8f}, B3={B3_traj[16]:.8f}")
print(f"  Gap edge: omega_gap = {omega_gap:.8f}")

# ============================================================
# SECTION 3: Branch derivatives (velocity of eigenvalue splitting)
# ============================================================

# Compute d(B_i)/d(tau) at multiple tau values
print(f"\n--- Branch derivatives ---")

def centered_deriv(arr, tau_arr, idx):
    if idx == 0:
        return (arr[1] - arr[0]) / (tau_arr[1] - tau_arr[0])
    elif idx == len(arr) - 1:
        return (arr[-1] - arr[-2]) / (tau_arr[-1] - tau_arr[-2])
    else:
        return (arr[idx+1] - arr[idx-1]) / (tau_arr[idx+1] - tau_arr[idx-1])

# At tau = 0 (from small tau)
dB1_0 = centered_deriv(B1_traj, tau_dense, 0)
dB2_0 = centered_deriv(B2_traj, tau_dense, 0)
dB3_0 = centered_deriv(B3_traj, tau_dense, 0)

# At tau = 0.20 (fold)
idx_fold = np.argmin(np.abs(tau_dense - 0.20))
dB1_fold = centered_deriv(B1_traj, tau_dense, idx_fold)
dB2_fold = centered_deriv(B2_traj, tau_dense, idx_fold)
dB3_fold = centered_deriv(B3_traj, tau_dense, idx_fold)

print(f"  tau = 0: dB1/dt={dB1_0:.6f}, dB2/dt={dB2_0:.6f}, dB3/dt={dB3_0:.6f}")
print(f"  tau = 0.20: dB1/dt={dB1_fold:.6f}, dB2/dt={dB2_fold:.6f}, dB3/dt={dB3_fold:.6f}")

# ============================================================
# SECTION 4: Sector data with physical degeneracies
# ============================================================

print(f"\n--- Sector data ---")

# Physical weight per eigenvalue in each group
phys_weight = {}
for i, name in enumerate(group_names):
    phys_weight[name] = group_n_phys[i] / group_n_ev[i]

# Build sector table
sectors_unique = [
    {'p': 0, 'q': 0, 'name': '(0,0)',         'branch': 'B1', 'n_phys': 1,    'n_ev': 16},
    {'p': 1, 'q': 0, 'name': '(1,0)',         'branch': 'B1', 'n_phys': 9,    'n_ev': 48},
    {'p': 0, 'q': 1, 'name': '(0,1)',         'branch': 'B1', 'n_phys': 9,    'n_ev': 48},
    {'p': 1, 'q': 1, 'name': '(1,1)',         'branch': 'B2', 'n_phys': 64,   'n_ev': 128},
    {'p': 2, 'q': 0, 'name': '(2,0)',         'branch': 'B3', 'n_phys': 36,   'n_ev': 96},
    {'p': 0, 'q': 2, 'name': '(0,2)',         'branch': 'B3', 'n_phys': 36,   'n_ev': 96},
    {'p': 3, 'q': 0, 'name': '(3,0)',         'branch': 'B3', 'n_phys': 100,  'n_ev': 160},
    {'p': 0, 'q': 3, 'name': '(0,3)',         'branch': 'B3', 'n_phys': 100,  'n_ev': 160},
    {'p': 2, 'q': 1, 'name': '(2,1)',         'branch': 'B3', 'n_phys': 225,  'n_ev': 240},
]
# Note: (1,2) and (2,1) are conjugate pairs in the truncation; handle via combined groups

for s in sectors_unique:
    s['C2'] = (s['p']**2 + s['q']**2 + s['p']*s['q'] + 3*s['p'] + 3*s['q']) / 3.0
    s['dim'] = dim_su3(s['p'], s['q'])

# Sort by Casimir
sectors_unique.sort(key=lambda x: x['C2'])

print(f"  {'Sector':<10} {'C_2':<8} {'Branch':<8} {'dim':<6} {'n_phys':<8}")
for s in sectors_unique:
    print(f"  ({s['p']},{s['q']}){' ':<5} {s['C2']:<8.3f} {s['branch']:<8} {s['dim']:<6} {s['n_phys']:<8}")

# ============================================================
# SECTION 5: CORRECT computation of eta from propagator inversion
# ============================================================

print("\n" + "=" * 70)
print("SECTION 5: Anomalous dimension from spectral action propagator")
print("=" * 70)

# The physical picture:
#
# The perturbation field delta_tau(x^mu, y^a) lives on M^4 x SU(3).
# It can be decomposed in harmonics on SU(3):
#   delta_tau(x, y) = sum_{(p,q)} delta_tau_{(p,q)}(x) * Y_{(p,q)}(y)
#
# Each mode (p,q) has a 4D effective mass determined by the spectral action:
#   m^2_{(p,q)} = (1/n_{(p,q)}) * d^2 S / d(delta_tau_{(p,q)})^2
# where n_{(p,q)} is the physical degeneracy.
#
# The 4D power spectrum of mode (p,q) is:
#   P_{(p,q)}(k_4D) ~ 1 / m^2_{(p,q)}  [for k_4D << m]
# or
#   P_{(p,q)}(k_4D) ~ 1 / k_4D^2  [for k_4D >> m]
#
# The TOTAL 4D power spectrum sums over all (p,q):
#   P(k_4D) = sum_{(p,q)} w_{(p,q)} / (k_4D^2 + m^2_{(p,q)})
#
# The spectral tilt n_s - 1 = d ln P / d ln k at the pivot scale.
#
# KEY: The spectral action second variation d^2S/d(delta_tau)^2 involves
# SECOND derivatives of eigenvalues with respect to the deformation.
# This is the STIFFNESS, not the first-order response.

# For the spectral action S = sum_i n_i * f(lambda_i^2):
# The variation with respect to a mode-specific perturbation delta_tau_{(p,q)} is:
#   d^2 S / d(delta_tau_{(p,q)})^2 = n_i * [2*f'*((d lambda_i/d tau)^2 + lambda_i * d^2 lambda_i/d tau^2)
#                                             + 4*f''*(lambda_i * d lambda_i/d tau)^2]
#
# For the SIMPLEST case (f = identity, S = sum lambda_i^2):
#   d^2 S / d(delta_tau)^2 = 2 * sum_i n_i * [(d lambda_i/d tau)^2 + lambda_i * d^2 lambda_i/d tau^2]

# The stiffness per sector:
# K(p,q) ~ n_phys(p,q) * (d lambda_{branch}/d tau)^2

# But the key point for n_s is: what is the K-DEPENDENCE of the stiffness?
# The modes that contribute to k_4D ~ k_pivot are those with:
#   C_2(p,q)^{1/2} * M_KK ~ k_pivot * M_pl

# Since we need P(k) ~ 1/K(k), the tilt is:
#   n_s - 1 = -d ln K / d ln k

# For each sector, K is proportional to n_phys * (d lambda/d tau)^2.
# The "wavenumber" is k_eff = sqrt(C_2) * M_KK.

# Let me build K(k_eff) and compute its logarithmic derivative.

# Second derivatives of branches near fold
d2B1 = np.zeros(len(tau_dense))
d2B2 = np.zeros(len(tau_dense))
d2B3 = np.zeros(len(tau_dense))

for i in range(1, len(tau_dense) - 1):
    dt_l = tau_dense[i] - tau_dense[i-1]
    dt_r = tau_dense[i+1] - tau_dense[i]
    d2B1[i] = 2*((B1_traj[i+1] - B1_traj[i])/dt_r - (B1_traj[i] - B1_traj[i-1])/dt_l) / (dt_l + dt_r)
    d2B2[i] = 2*((B2_traj[i+1] - B2_traj[i])/dt_r - (B2_traj[i] - B2_traj[i-1])/dt_l) / (dt_l + dt_r)
    d2B3[i] = 2*((B3_traj[i+1] - B3_traj[i])/dt_r - (B3_traj[i] - B3_traj[i-1])/dt_l) / (dt_l + dt_r)

print(f"\n  Second derivatives at fold (tau=0.20):")
print(f"    d2B1/dtau2 = {d2B1[idx_fold]:.6f}")
print(f"    d2B2/dtau2 = {d2B2[idx_fold]:.6f}")
print(f"    d2B3/dtau2 = {d2B3[idx_fold]:.6f}")

# Stiffness per sector at fold
# K_sector = n_phys * [2*(dB/dt)^2 + 2*B * d2B/dt2]  (for f = lambda^2)
# For the spectral tilt, only the k-dependent part matters.

# Map sectors to their branch derivatives
branch_derivs = {
    'B1': {'dB': dB1_fold, 'd2B': d2B1[idx_fold], 'B': B1_traj[idx_fold]},
    'B2': {'dB': dB2_fold, 'd2B': d2B2[idx_fold], 'B': B2_traj[idx_fold]},
    'B3': {'dB': dB3_fold, 'd2B': d2B3[idx_fold], 'B': B3_traj[idx_fold]},
}

# Compute stiffness K for each sector
print(f"\n  Stiffness K(C_2) at fold:")
print(f"  {'Sector':<10} {'C_2':<8} {'Branch':<8} {'K_kinetic':<14} {'K_curvature':<14} {'K_total':<14}")

K_sectors = []
C2_sectors = []
for s in sectors_unique:
    bd = branch_derivs[s['branch']]
    # Kinetic stiffness: (d lambda/d tau)^2
    K_kin = s['n_phys'] * bd['dB']**2
    # Curvature stiffness: lambda * d^2 lambda / d tau^2
    K_curv = s['n_phys'] * bd['B'] * bd['d2B']
    K_tot = 2 * K_kin + 2 * K_curv  # factor 2 from d/d(lambda^2)

    K_sectors.append(K_tot)
    C2_sectors.append(s['C2'])
    print(f"  ({s['p']},{s['q']}){' ':<5} {s['C2']:<8.3f} {s['branch']:<8} {K_kin:<14.6f} {K_curv:<14.6f} {K_tot:<14.6f}")

K_sectors = np.array(K_sectors)
C2_sectors = np.array(C2_sectors)
k_eff_sectors = np.sqrt(C2_sectors)

# ============================================================
# SECTION 6: Power spectrum P(k) = 1/K(k) and spectral tilt
# ============================================================

print("\n" + "=" * 70)
print("SECTION 6: Power spectrum and spectral tilt from 1/K(k)")
print("=" * 70)

# The 4D power spectrum for each mode is P ~ 1/K.
# Combine conjugate sectors [(p,q) and (q,p)] which have same C_2.

# Group by C_2
from collections import defaultdict
K_by_C2 = defaultdict(float)
for i, s in enumerate(sectors_unique):
    K_by_C2[s['C2']] += K_sectors[i]

C2_unique = np.array(sorted(K_by_C2.keys()))
K_unique = np.array([K_by_C2[c] for c in C2_unique])
k_eff_unique = np.sqrt(C2_unique)

# P(k) = 1/K(k) for each k
# Handle C_2 = 0 separately (zero mode)
P_sectors = np.zeros_like(K_unique)
for i in range(len(K_unique)):
    if np.abs(K_unique[i]) > 1e-10:
        P_sectors[i] = 1.0 / np.abs(K_unique[i])
    else:
        P_sectors[i] = 0  # zero mode is special

print(f"\n  {'C_2':<8} {'k_eff':<8} {'K(k)':<14} {'P(k)=1/K':<14}")
for i in range(len(C2_unique)):
    print(f"  {C2_unique[i]:<8.3f} {k_eff_unique[i]:<8.4f} {K_unique[i]:<14.6f} {P_sectors[i]:<14.6e}")

# The spectral tilt n_s - 1 = d ln P / d ln k
# Compute from sector-by-sector ratios

print(f"\n  Local spectral tilt between adjacent sectors:")
mask_valid = (k_eff_unique > 0) & (P_sectors > 0)
k_valid = k_eff_unique[mask_valid]
P_valid = P_sectors[mask_valid]

local_ns = []
k_mid = []
for i in range(1, len(k_valid)):
    dlogP = np.log(P_valid[i]) - np.log(P_valid[i-1])
    dlogk = np.log(k_valid[i]) - np.log(k_valid[i-1])
    if np.abs(dlogk) > 1e-10:
        ns_local = 1 + dlogP / dlogk
        local_ns.append(ns_local)
        k_m = np.sqrt(k_valid[i] * k_valid[i-1])
        k_mid.append(k_m)
        print(f"    k = {k_valid[i-1]:.4f} -> {k_valid[i]:.4f}: n_s = {ns_local:.6f}")

local_ns = np.array(local_ns)
k_mid = np.array(k_mid)

# Smooth power spectrum and tilt
# Use log-log interpolation
log_k_valid = np.log(k_valid)
log_P_valid = np.log(P_valid)

# Polynomial fit of log P vs log k
if len(k_valid) >= 3:
    poly_coeffs = np.polyfit(log_k_valid, log_P_valid, min(len(k_valid)-1, 3))
    poly = np.poly1d(poly_coeffs)
    # Derivative = spectral index - 1
    dpoly = np.polyder(poly)

    # Evaluate at different k
    print(f"\n  Spectral tilt from polynomial fit (degree {len(poly_coeffs)-1}):")
    for k_t in [0.5, 1.0, 1.15, 1.3, 1.5, 1.8, 2.0, 2.45]:
        if k_t > k_valid[0] * 0.9 and k_t < k_valid[-1] * 1.1:
            ns_poly = 1 + dpoly(np.log(k_t))
            print(f"    k = {k_t:.2f} (C_2 = {k_t**2:.2f}): n_s = {ns_poly:.6f}")

# ============================================================
# SECTION 7: The PHYSICAL eta from the stiffness scaling
# ============================================================

print("\n" + "=" * 70)
print("SECTION 7: Physical eta from stiffness scaling")
print("=" * 70)

# The stiffness K(k) ~ n_phys(k) * (dB/dtau)^2 has two competing factors:
# 1. n_phys grows with C_2 (more states at higher k)
# 2. (dB/dtau)^2 depends on the branch
#
# For B3 (dominant branch): dB3/dtau ~ 0.688 (nearly constant)
# So K(k) for B3 sectors ~ n_phys(k) * const
# And n_phys grows as dim(p,q)^2
#
# For the representation lattice of SU(3), dim(p,q)^2 ~ C_2^2 at large C_2
# (since dim ~ C_2^{1/2} * (p+q+2)^{1/2} at large p+q).
# More precisely, for the weight (n_phys) in our truncation:
# (0,0): 1, (1,0): 9, (1,1): 64, (2,0): 36, (3,0): 100, (2,1): 225
#
# The stiffness K ~ n_phys(C_2) * const grows with C_2.
# The power spectrum P ~ 1/K DECREASES with C_2.
# This means n_s < 1 (RED tilt), which is the correct direction.

# But the detailed scaling matters. Let me fit K(k) directly.
mask_B3 = np.array([s['branch'] == 'B3' for s in sectors_unique])
C2_B3 = C2_sectors[mask_B3]
K_B3 = K_sectors[mask_B3]
k_B3 = np.sqrt(C2_B3)

# For B3 sectors only (which dominate)
if len(k_B3) >= 2:
    mask_pos_B3 = (k_B3 > 0) & (K_B3 > 0)
    if np.sum(mask_pos_B3) >= 2:
        slope_K_B3 = np.polyfit(np.log(k_B3[mask_pos_B3]), np.log(K_B3[mask_pos_B3]), 1)
        print(f"  K_B3(k) ~ k^{slope_K_B3[0]:.4f}")
        print(f"  P_B3(k) ~ k^{-slope_K_B3[0]:.4f}")
        ns_B3 = 1 - slope_K_B3[0]
        eta_B3 = -ns_B3 + 1  # eta_eff = 1 - n_s
        print(f"  n_s (B3 only) = {ns_B3:.6f}")
        print(f"  eta_eff (B3 only) = {eta_B3:.6f}")

# For ALL sectors combined (grouped by C_2)
if len(k_valid) >= 2:
    slope_K_all = np.polyfit(np.log(k_valid), -np.log(P_valid), 1)  # K = 1/P
    print(f"\n  K_all(k) ~ k^{slope_K_all[0]:.4f}")
    print(f"  P_all(k) ~ k^{-slope_K_all[0]:.4f}")
    ns_all = 1 - slope_K_all[0]
    eta_all = slope_K_all[0]
    print(f"  n_s (all sectors) = {ns_all:.6f}")
    print(f"  eta_eff (all sectors) = {eta_all:.6f}")

# ============================================================
# SECTION 8: Refined eta from d_eff decomposition
# ============================================================

print("\n" + "=" * 70)
print("SECTION 8: Refined eta from effective dimensionality")
print("=" * 70)

# The standard Lifshitz anomalous dimension for a Type I transition
# in d_eff dimensions with dynamic exponent z = 2 is:
#   eta = 0 at mean-field level
#   eta = epsilon * f(n) at one-loop (epsilon = d_uc - d)
# where n is the number of order parameter components and
# d_uc = 2 + z/2 = 3 for z = 2.
#
# But in our system, the anomalous dimension is NOT from the standard
# Lifshitz universality class. It comes from the GEOMETRIC structure
# of the SU(3) representation lattice.
#
# The key quantity is: how does the physical DOS grow with energy?
# N_phys(E) = sum_{lambda_i < E} n_phys(i)
#
# For the SU(3) lattice: n_phys ~ dim(p,q)^2 and C_2 ~ p^2 + q^2 + pq
# At large C_2: dim(p,q) ~ C_2^{3/2} / const (exact leading term)
#   => n_phys ~ C_2^3
# And E ~ C_2^{1/2} (for quadratic Casimir dispersion)
#   => C_2 ~ E^2
#   => n_phys(E) ~ E^6
# This gives the spectral Weyl exponent for SU(3):
#   N(E) ~ integral_0^E n_phys(E') dE' ~ E^7
# Or more carefully, the DOS per unit energy:
#   rho(E) ~ E^6
#
# The anomalous dimension is the deviation from the "free" scaling.
# For a free scalar on SU(3) (dim = 8):
#   Weyl's law: N(lambda < Lambda) ~ Lambda^8 (volume factor)
#   => rho(lambda) ~ lambda^7
# The physical DOS counting representations gives rho ~ E^6 instead of E^7.
# The difference is because we are on the representation LATTICE, not the
# continuous manifold.
#
# For the spectral tilt:
# P(k) ~ 1/K(k) where K ~ n_phys(k) * (dB/dtau)^2
# If n_phys ~ k^{2*alpha} and (dB/dtau)^2 ~ const (B3 branch):
#   K ~ k^{2*alpha}
#   P ~ k^{-2*alpha}
#   n_s - 1 = -2*alpha
#
# The exponent alpha depends on how n_phys grows with C_2.

# Compute alpha from the sector data
C2_valid_sec = []
n_phys_sec = []
for s in sectors_unique:
    if s['C2'] > 0:
        C2_valid_sec.append(s['C2'])
        n_phys_sec.append(s['n_phys'])

C2_vs = np.array(C2_valid_sec)
n_phys_vs = np.array(n_phys_sec)

# Group conjugate pairs
C2_grouped = defaultdict(float)
for i in range(len(C2_vs)):
    C2_grouped[C2_vs[i]] += n_phys_vs[i]

C2_gp = np.array(sorted(C2_grouped.keys()))
n_gp = np.array([C2_grouped[c] for c in C2_gp])
k_gp = np.sqrt(C2_gp)

print(f"  Physical degeneracy vs C_2:")
for i in range(len(C2_gp)):
    print(f"    C_2 = {C2_gp[i]:.3f}, k = {k_gp[i]:.4f}, n_phys = {n_gp[i]:.0f}")

if len(k_gp) >= 2:
    slope_n = np.polyfit(np.log(k_gp), np.log(n_gp), 1)
    print(f"\n  n_phys(k) ~ k^{slope_n[0]:.4f}")
    print(f"  => K(k) ~ k^{slope_n[0]:.4f} (if dB/dtau ~ const)")
    print(f"  => P(k) ~ k^{-slope_n[0]:.4f}")
    print(f"  => n_s - 1 = {-slope_n[0]:.6f}")
    ns_from_lattice = 1 - slope_n[0]
    eta_from_lattice = slope_n[0]
    print(f"  => n_s = {ns_from_lattice:.6f}")
    print(f"  => eta_eff = {eta_from_lattice:.6f}")
else:
    ns_from_lattice = 1.0
    eta_from_lattice = 0.0

# ============================================================
# SECTION 9: Cross-check with actual stiffness data
# ============================================================

print("\n" + "=" * 70)
print("SECTION 9: Cross-check with sector-level stiffness")
print("=" * 70)

# Instead of using n_phys alone, use the ACTUAL stiffness K = n_phys * |dB/dt|^2
# This properly accounts for the fact that B1 and B2 have different derivatives
# from B3.

# For the P(k) = 1/K(k) computation at the FOLD:
print(f"  Stiffness per grouped sector at fold:")
K_grouped = defaultdict(float)
for i, s in enumerate(sectors_unique):
    K_grouped[s['C2']] += np.abs(K_sectors[i])

K_gp_arr = np.array([K_grouped[c] for c in C2_gp])
P_gp_arr = 1.0 / np.maximum(K_gp_arr, 1e-30)

for i in range(len(C2_gp)):
    print(f"    C_2 = {C2_gp[i]:.3f}: K = {K_gp_arr[i]:.6e}, P = {P_gp_arr[i]:.6e}")

# Fit P(k) directly
if len(k_gp) >= 2:
    slope_P = np.polyfit(np.log(k_gp), np.log(P_gp_arr), 1)
    print(f"\n  P(k) ~ k^{slope_P[0]:.4f}  (from actual stiffness)")
    ns_stiffness = 1 + slope_P[0]
    eta_stiffness = -slope_P[0]
    print(f"  n_s = {ns_stiffness:.6f}")
    print(f"  eta_eff = {eta_stiffness:.6f}")
else:
    ns_stiffness = ns_from_lattice
    eta_stiffness = eta_from_lattice

# ============================================================
# SECTION 10: Repeat at tau = 0 (round metric)
# ============================================================

print("\n" + "=" * 70)
print("SECTION 10: Computation at tau = 0 (round metric)")
print("=" * 70)

# At the round metric, all branches have derivative:
# dB1/dtau(0) = -0.427, dB2/dtau(0) = -0.213, dB3/dtau(0) = +0.437

branch_derivs_0 = {
    'B1': {'dB': dB1_0, 'B': lambda_round},
    'B2': {'dB': dB2_0, 'B': lambda_round},
    'B3': {'dB': dB3_0, 'B': lambda_round},
}

K_sectors_0 = []
for s in sectors_unique:
    bd = branch_derivs_0[s['branch']]
    K_kin = s['n_phys'] * bd['dB']**2
    K_sectors_0.append(2 * K_kin)  # just kinetic at round (curvature needs second deriv)

K_sectors_0 = np.array(K_sectors_0)

# Group by C_2
K_grouped_0 = defaultdict(float)
for i, s in enumerate(sectors_unique):
    K_grouped_0[s['C2']] += np.abs(K_sectors_0[i])

K_gp_0 = np.array([K_grouped_0[c] for c in C2_gp])
P_gp_0 = 1.0 / np.maximum(K_gp_0, 1e-30)

print(f"  Stiffness at round metric:")
for i in range(len(C2_gp)):
    print(f"    C_2 = {C2_gp[i]:.3f}: K = {K_gp_0[i]:.6e}, P = {P_gp_0[i]:.6e}")

if len(k_gp) >= 2:
    slope_P_0 = np.polyfit(np.log(k_gp), np.log(P_gp_0), 1)
    print(f"\n  P_0(k) ~ k^{slope_P_0[0]:.4f}")
    ns_round = 1 + slope_P_0[0]
    eta_round = -slope_P_0[0]
    print(f"  n_s (round) = {ns_round:.6f}")
    print(f"  eta_eff (round) = {eta_round:.6f}")
else:
    ns_round = 1.0
    eta_round = 0.0

# ============================================================
# SECTION 11: The transfer function correction
# ============================================================

print("\n" + "=" * 70)
print("SECTION 11: Transfer function correction")
print("=" * 70)

# The above computations give the INTERNAL spectral tilt: the scaling of
# the perturbation amplitude on the SU(3) representation lattice.
# The OBSERVED n_s in the CMB requires a transfer function that maps
# internal modes to 4D perturbations.
#
# The transfer function depends on:
# 1. How each internal mode (p,q) couples to the 4D metric (through
#    the KK reduction of the spectral action)
# 2. The time-dependence of the expansion during the transit
# 3. The KK mass hierarchy (modes with m_KK >> H are suppressed)
#
# For the simplest case (all modes have comparable m_KK, which they do
# in our truncation since the bandwidth is only 1.26):
#   The transfer function is approximately k-independent.
#   The 4D n_s is the same as the internal n_s.
#
# For the more realistic case where modes have m_KK = M_KK * sqrt(C_2):
#   Modes with C_2 = 0 couple most strongly (lightest KK mode).
#   Modes with C_2 > 0 are exponentially suppressed by m_KK/H.
#   The 4D power spectrum is dominated by the lowest C_2 modes.
#
# In this limit, the spectral tilt is determined by the FIRST FEW sectors,
# not the full lattice.

# Let me compute n_s including a KK mass suppression factor
# exp(-m_KK^2 / (2*H^2)) for each mode
# Using M_KK from the spectral range at fold: range ~ 1.26 natural units

print(f"\n  Computing n_s with KK mass suppression:")
for MKK_over_H in [0.5, 1.0, 2.0, 5.0, 10.0, 20.0]:
    # Suppression factor for each sector
    K_suppressed = np.zeros(len(C2_gp))
    for i in range(len(C2_gp)):
        supp = np.exp(-C2_gp[i] * MKK_over_H**2 / 2.0)
        K_suppressed[i] = K_gp_arr[i] * supp

    # Total P = 1/K for each sector
    P_suppressed = 1.0 / np.maximum(K_suppressed, 1e-30)

    # Weighted average spectral index
    mask_s = P_suppressed < 1e20
    if np.sum(mask_s) >= 2:
        k_s = k_gp[mask_s]
        P_s = P_suppressed[mask_s]
        slope_s = np.polyfit(np.log(k_s), np.log(P_s), 1)
        ns_s = 1 + slope_s[0]
    else:
        ns_s = 1.0
    print(f"    M_KK/H = {MKK_over_H:>5.1f}: n_s = {ns_s:.6f}")

# ============================================================
# SECTION 12: Fundamental structural result
# ============================================================

print("\n" + "=" * 70)
print("SECTION 12: STRUCTURAL RESULT — Geometric origin of the tilt")
print("=" * 70)

# The anomalous dimension in this system has a GEOMETRIC origin:
# it comes from the growth of physical degeneracies on the SU(3)
# representation lattice.
#
# The stiffness K(k) ~ n_phys(k) * |dB/dtau|^2.
# For the B3 branch (which dominates): |dB3/dtau| ~ 0.69 ~ const.
# So K(k) ~ n_phys(k) ~ k^{2*alpha} where alpha is the degeneracy
# growth exponent.
#
# The power spectrum P(k) ~ 1/K(k) ~ k^{-2*alpha}.
# The spectral tilt: n_s - 1 = -2*alpha.
#
# For the SU(3) lattice: dim(p,q)^2 grows as C_2^3 at large C_2.
# With k = sqrt(C_2): n_phys ~ k^6.
# So the naive prediction is n_s - 1 = -6, way too red.
#
# However, the actual exponent from the DATA (which has only a few
# sectors) is different from the asymptotic scaling. The low-C_2
# sectors dominate the CMB because of KK mass suppression.
#
# The PHYSICALLY CORRECT answer depends on:
# (a) How many representation sectors contribute at the CMB pivot
# (b) The actual n_phys values at those sectors
# (c) The branch derivatives at those sectors

# Let me compute the "first few sectors" tilt, which is relevant
# for the CMB.

# The B1 sectors: C_2 = 0, 4/3
# The B2 sector: C_2 = 3
# The B3 sectors: C_2 = 10/3, 6, 16/3

# First transition B1 -> B2:
# P(B1) / P(B2) = K(B2) / K(B1)
# K(B1) at C_2 = 4/3: 2 * 18 * dB1^2 = 2 * 18 * 0.0517^2 = 0.0961
# K(B2) at C_2 = 3: 2 * 64 * dB2^2 = 2 * 64 * 0.0116^2 = 0.0172

# Wait, the actual stiffness values computed above include the contributions.
# Let me be more precise.

print(f"\n  Sector-by-sector tilt (most important for CMB):")

# Use the k=0 sector as reference.
# The singlet (0,0) has C_2 = 0 and is the zero mode.
# The first nontrivial sectors are (1,0) and (0,1) with C_2 = 4/3.
# Then (1,1) with C_2 = 3.
# The tilt between these adjacent sectors is what determines n_s.

# (1,0)+(0,1) combined: K = 2 * 9 * dB1^2 * 2 = 36 * 0.0517^2 * 2 = 0.192
# Wait, n_phys for (1,0) is dim^2 = 3^2 = 9. Combined (1,0)+(0,1): 2*9 = 18.
# K = 2 * 18 * dB1^2

K_10_combined = K_grouped[4/3]
K_11 = K_grouped[3.0]
K_20_combined = K_grouped[10/3]
K_21_combined = K_grouped[16/3]
K_30_combined = K_grouped[6.0]

print(f"    K(C_2 = 4/3) [(1,0)+(0,1)]: {K_10_combined:.6e}")
print(f"    K(C_2 = 3)   [(1,1)]:       {K_11:.6e}")
print(f"    K(C_2 = 10/3)[(2,0)+(0,2)]: {K_20_combined:.6e}")
print(f"    K(C_2 = 16/3)[(2,1)]:       {K_21_combined:.6e}")
print(f"    K(C_2 = 6)   [(3,0)+(0,3)]: {K_30_combined:.6e}")

# The critical transition for the tilt:
# Between (1,0)+(0,1) [B1 branch] and (1,1) [B2 branch]
# k1 = sqrt(4/3) = 1.155
# k2 = sqrt(3) = 1.732
# P1 = 1/K1, P2 = 1/K2

P_10 = 1.0 / K_10_combined
P_11 = 1.0 / K_11
P_20 = 1.0 / K_20_combined

dlogP_12 = np.log(P_11) - np.log(P_10)
dlogk_12 = np.log(np.sqrt(3)) - np.log(np.sqrt(4/3))

ns_12 = 1 + dlogP_12 / dlogk_12
print(f"\n  Critical tilt (B1 -> B2 transition):")
print(f"    k: {np.sqrt(4/3):.4f} -> {np.sqrt(3):.4f}")
print(f"    n_s = {ns_12:.6f}")
print(f"    eta_eff = {1 - ns_12:.6f}")

# Between (1,1) and (2,0)+(0,2)
dlogP_23 = np.log(P_20) - np.log(P_11)
dlogk_23 = np.log(np.sqrt(10/3)) - np.log(np.sqrt(3))

ns_23 = 1 + dlogP_23 / dlogk_23
print(f"\n  B2 -> B3 transition:")
print(f"    k: {np.sqrt(3):.4f} -> {np.sqrt(10/3):.4f}")
print(f"    n_s = {ns_23:.6f}")
print(f"    eta_eff = {1 - ns_23:.6f}")

# ============================================================
# SECTION 13: The B1-B2 transition determines n_s
# ============================================================

print("\n" + "=" * 70)
print("SECTION 13: Physical interpretation — B1-B2 transition")
print("=" * 70)

# The B1 -> B2 transition is the CRITICAL feature for n_s.
# This is because:
# 1. The B1 branch has a SMALL derivative (|dB1/dtau| = 0.052 at fold)
# 2. The B2 branch has an even SMALLER derivative (|dB2/dtau| = 0.012)
# 3. But B2 has much LARGER physical degeneracy (64 vs 18)
#
# The competition between derivative magnitude and degeneracy creates
# a NON-MONOTONIC stiffness K(k), which produces a scale-dependent n_s.
#
# At the lowest k (B1 sectors): K is small because of large dB/dtau (in absolute terms)
# At intermediate k (B2): K can be SMALLER because dB2/dtau ~ 0
# At high k (B3): K is large because dB3/dtau ~ 0.69 AND n_phys is large
#
# The B2 branch has dB2/dtau ~ 0.012 (near its minimum at tau ~ 0.19).
# This is an ACCIDENT of the fold location: at the fold, B2 is near its
# own extremum, so its derivative nearly vanishes.
# This creates an anomalously LARGE P (small K) at the B2 sector,
# which appears as a "bump" in the power spectrum.

# The net result: the power spectrum has a feature at C_2 ~ 3 (B2 sector)
# where P is enhanced relative to the smooth power-law extrapolation.
# This is NOT a conventional anomalous dimension but a FEATURE of the
# specific SU(3) representation structure.

# For the spectral tilt, what matters is the BROAD TREND.
# From B1 to B3, the power spectrum drops because stiffness increases.
# The overall slope gives eta_eff.

# IMPORTANT: The eta_eff computed above depends on the PIVOT SCALE.
# If the pivot is at the B1-B2 transition (k ~ 1.4, C_2 ~ 2):
#   n_s is determined by the B1-B2 tilt.
# If the pivot is at B3 (k ~ 2.4, C_2 ~ 6):
#   n_s is determined by the B2-B3 tilt.

# Best estimate: use the GLOBAL fit over all sectors.
print(f"\n  Summary of eta_eff determinations:")
print(f"    Global fit (all sectors): eta_eff = {eta_stiffness:.6f}, n_s = {ns_stiffness:.6f}")
print(f"    B3-only fit: eta_eff = {eta_B3:.6f}, n_s = {ns_B3:.6f}")
print(f"    Lattice-only (no dB): eta_eff = {eta_from_lattice:.6f}, n_s = {ns_from_lattice:.6f}")
print(f"    B1->B2 transition: eta_eff = {1-ns_12:.6f}, n_s = {ns_12:.6f}")
print(f"    Round metric: eta_eff = {eta_round:.6f}, n_s = {ns_round:.6f}")

# ============================================================
# SECTION 14: Sensitivity analysis
# ============================================================

print("\n" + "=" * 70)
print("SECTION 14: Sensitivity analysis — which tau gives n_s ~ 0.965?")
print("=" * 70)

# The global eta depends on dB/dtau at the evaluation point.
# At tau = 0.20 (fold): dB1 ~ -0.05, dB2 ~ +0.01, dB3 ~ +0.69
# The B3 branch dominates and eta_eff ~ several.
#
# But at tau = 0, dB1 ~ -0.43, dB2 ~ -0.21, dB3 ~ +0.44
# The derivatives are more BALANCED, so the stiffness is more uniform
# across sectors, and eta_eff should be smaller.
#
# What tau gives eta_eff ~ 0.035 (Planck)?

# Compute eta_eff at each tau in the dense grid
eta_vs_tau = []
ns_vs_tau = []

for ti in range(1, len(tau_dense) - 1):
    dB1_t = centered_deriv(B1_traj, tau_dense, ti)
    dB2_t = centered_deriv(B2_traj, tau_dense, ti)
    dB3_t = centered_deriv(B3_traj, tau_dense, ti)

    # Stiffness per sector (kinetic only)
    K_t = []
    for s in sectors_unique:
        if s['branch'] == 'B1':
            dlam = dB1_t
        elif s['branch'] == 'B2':
            dlam = dB2_t
        else:
            dlam = dB3_t
        K_t.append(2 * s['n_phys'] * dlam**2)

    K_t = np.array(K_t)

    # Group by C_2
    K_grp_t = defaultdict(float)
    for j, s in enumerate(sectors_unique):
        K_grp_t[s['C2']] += np.abs(K_t[j])

    K_arr_t = np.array([K_grp_t[c] for c in C2_gp])
    P_arr_t = 1.0 / np.maximum(K_arr_t, 1e-30)

    # Fit slope
    mask_valid_t = (k_gp > 0) & np.isfinite(P_arr_t) & (P_arr_t < 1e20) & (P_arr_t > 0)
    if np.sum(mask_valid_t) >= 2:
        sl = np.polyfit(np.log(k_gp[mask_valid_t]), np.log(P_arr_t[mask_valid_t]), 1)
        ns_t = 1 + sl[0]
        eta_t = -sl[0]
    else:
        ns_t = 1.0
        eta_t = 0.0

    eta_vs_tau.append(eta_t)
    ns_vs_tau.append(ns_t)

tau_plot = tau_dense[1:-1]
eta_vs_tau = np.array(eta_vs_tau)
ns_vs_tau = np.array(ns_vs_tau)

print(f"  tau-dependence of eta_eff and n_s:")
print(f"  {'tau':<8} {'eta_eff':<12} {'n_s':<12}")
for i in range(len(tau_plot)):
    planck_note = " <-- near Planck" if abs(ns_vs_tau[i] - 0.9649) < 0.05 else ""
    print(f"  {tau_plot[i]:<8.3f} {eta_vs_tau[i]:<12.6f} {ns_vs_tau[i]:<12.6f}{planck_note}")

# Check if there's a tau where n_s ~ 0.9649
target_ns = 0.9649
closest_idx = np.argmin(np.abs(ns_vs_tau - target_ns))
print(f"\n  Closest to Planck: tau = {tau_plot[closest_idx]:.3f}, "
      f"n_s = {ns_vs_tau[closest_idx]:.6f}, eta = {eta_vs_tau[closest_idx]:.6f}")

# ============================================================
# SECTION 15: Final results and gate assessment
# ============================================================

print("\n" + "=" * 70)
print("SECTION 15: FINAL RESULTS AND GATE ASSESSMENT")
print("=" * 70)

# PRIMARY RESULT:
# The anomalous dimension at the fold (tau = 0.20) is eta_eff ~ 3.2,
# giving n_s ~ -2.2, which is wildly blue/negative and FAILS the gate.
#
# HOWEVER: the eta_eff is NOT from a conventional Lifshitz universality
# class. It is a GEOMETRIC quantity determined by the growth of physical
# degeneracies on the SU(3) representation lattice.
#
# The fundamental reason for the large eta_eff:
# At the fold, the B3 branch has d(B3)/d(tau) = 0.69, which is ~13x
# larger than the B1 derivative and ~60x larger than the B2 derivative.
# The B3 sectors have the largest physical degeneracies.
# So the stiffness is dominated by B3 and grows rapidly with C_2.
#
# STRUCTURAL INSIGHT:
# n_s - 1 = -d ln K / d ln k where K ~ n_phys(k) * |dB/dt|^2.
# For B3-dominated K: n_s - 1 ~ -(d ln n_phys / d ln k) ~ -4 to -6.
# This is too steep by a factor ~100.
#
# The only way to get n_s ~ 0.965 from this mechanism is if:
# (a) Only the LOWEST C_2 modes contribute (KK mass suppression), or
# (b) The transfer function from internal to 4D has compensating tilt, or
# (c) The perturbation mechanism is NOT the spectral action stiffness.
#
# PHYSICAL ASSESSMENT:
# The Lifshitz eta mechanism, as computed from the SU(3) representation
# lattice, produces a spectral tilt that is far too steep. The growth
# of dim(p,q)^2 with Casimir is too rapid. This means the representation
# lattice structure ALONE cannot explain n_s = 0.965.

# Use the fold value as the primary result
eta_eff_fold = eta_stiffness
ns_fold = ns_stiffness
eta_eff_round_final = eta_round
ns_round_final = ns_round

# Gate assessment
if 0.025 <= abs(eta_eff_fold) <= 0.045:
    gate_verdict = "PASS"
    gate_reason = f"eta_eff = {eta_eff_fold:.4f} in [0.025, 0.045]"
elif abs(eta_eff_fold) < 1e-4:
    gate_verdict = "FAIL"
    gate_reason = f"eta_eff ~ 0 (trivially vanishing)"
elif abs(eta_eff_fold) > 0.1:
    gate_verdict = "FAIL"
    gate_reason = (f"eta_eff = {eta_eff_fold:.4f} >> 0.1 (too steep). "
                   f"n_phys(C_2) grows too rapidly with C_2 on SU(3). "
                   f"Spectral tilt from representation lattice stiffness: n_s = {ns_fold:.4f}. "
                   f"Planck: n_s = 0.9649. "
                   f"Mechanism closed: SU(3) representation lattice alone cannot produce n_s ~ 0.965.")
else:
    gate_verdict = "INFO"
    gate_reason = f"eta_eff = {eta_eff_fold:.4f}, regime unclear"

print(f"\n  *** PRIMARY RESULTS ***")
print(f"  eta_eff (fold, tau=0.20) = {eta_eff_fold:.6f}")
print(f"  n_s (fold, tau=0.20) = {ns_fold:.6f}")
print(f"  eta_eff (round, tau=0) = {eta_eff_round_final:.6f}")
print(f"  n_s (round, tau=0) = {ns_round_final:.6f}")
print(f"")
print(f"  GATE: LIFSHITZ-ETA-44")
print(f"  Verdict: {gate_verdict}")
print(f"  Reason: {gate_reason}")
print(f"")
print(f"  Planck: n_s = 0.9649 +/- 0.0042")
delta_ns = ns_fold - 0.9649
print(f"  Delta n_s = {delta_ns:.4f} ({delta_ns/0.0042:.1f} sigma)")
print(f"")
print(f"  Closest tau to Planck: tau = {tau_plot[closest_idx]:.3f}, "
      f"n_s = {ns_vs_tau[closest_idx]:.6f}")

# ============================================================
# SECTION 16: Save all results
# ============================================================

print("\n" + "=" * 70)
print("SECTION 16: Saving results")
print("=" * 70)

np.savez(base / 's44_lifshitz_eta.npz',
         # Gate
         gate_verdict=np.array([gate_verdict]),
         gate_reason=np.array([gate_reason]),

         # Primary results
         eta_eff_fold=np.array([eta_eff_fold]),
         eta_eff_round=np.array([eta_eff_round_final]),
         ns_fold=np.array([ns_fold]),
         ns_round=np.array([ns_round_final]),

         # Derivatives at fold
         dB1_dtau_fold=np.array([dB1_fold]),
         dB2_dtau_fold=np.array([dB2_fold]),
         dB3_dtau_fold=np.array([dB3_fold]),

         # Derivatives at round
         dB1_dtau_0=np.array([dB1_0]),
         dB2_dtau_0=np.array([dB2_0]),
         dB3_dtau_0=np.array([dB3_0]),

         # Stiffness data
         C2_sectors=C2_gp,
         K_fold=K_gp_arr,
         P_fold=P_gp_arr,
         K_round=K_gp_0,
         P_round=P_gp_0,

         # Lattice scaling
         slope_n_phys=np.array([slope_n[0]]) if 'slope_n' in dir() else np.array([0.0]),
         slope_P_fold=np.array([slope_P[0]]) if 'slope_P' in dir() else np.array([0.0]),
         slope_P_round=np.array([slope_P_0[0]]) if 'slope_P_0' in dir() else np.array([0.0]),

         # tau scan
         tau_scan=tau_plot,
         eta_vs_tau=eta_vs_tau,
         ns_vs_tau=ns_vs_tau,

         # Van Hove
         n_vh=np.array([len(vh_omega)]),
         vh_omega=vh_omega,
         vh_types=vh_types,

         # Spectral action second derivatives
         d2S_fold=d36['d2S_fold'],
         dS_fold=d36['dS_fold'],

         # Planck comparison
         ns_planck=np.array([0.9649]),
         sigma_planck=np.array([0.0042]),
         delta_ns=np.array([delta_ns]),
)

print(f"  Saved: tier0-computation/s44_lifshitz_eta.npz")

# ============================================================
# SECTION 17: Generate plots
# ============================================================

print("\nGenerating plots...")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('LIFSHITZ-ETA-44: Anomalous Dimension at Type I Lifshitz Transition on SU(3)',
             fontsize=13, fontweight='bold')

# Panel 1: Branch trajectories
ax = axes[0, 0]
ax.plot(tau_dense, B1_traj, 'b-o', markersize=3, label='B1 (gap edge)')
ax.plot(tau_dense, B2_traj, 'r-s', markersize=3, label='B2')
ax.plot(tau_dense, B3_traj, 'g-^', markersize=3, label='B3')
ax.axvline(0.20, color='k', linestyle='--', alpha=0.5, label=r'$\tau_{fold}$')
ax.axhline(omega_gap, color='b', linestyle=':', alpha=0.3)
ax.set_xlabel(r'$\tau$ (Jensen parameter)')
ax.set_ylabel(r'$\lambda$ (eigenvalue)')
ax.set_title('Branch Trajectories')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Stiffness K(k) at fold and round
ax = axes[0, 1]
ax.semilogy(k_gp, K_gp_arr, 'bo-', markersize=8, label=r'$K(\tau_{fold})$')
ax.semilogy(k_gp, K_gp_0, 'rs--', markersize=8, label=r'$K(\tau=0)$')
# Power law fits
k_fit_range = np.linspace(k_gp[0], k_gp[-1], 50)
if 'slope_P' in dir():
    ax.semilogy(k_fit_range, np.exp(-slope_P[1]) * k_fit_range**(-slope_P[0]),
               'b:', alpha=0.5, label=f'$k^{{{-slope_P[0]:.1f}}}$')
ax.set_xlabel(r'$k_{eff} = \sqrt{C_2}$')
ax.set_ylabel(r'$K(k)$ (stiffness)')
ax.set_title('Stiffness $K(k) = n_{phys} |d\\lambda/d\\tau|^2$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Power spectrum P(k) = 1/K(k)
ax = axes[0, 2]
ax.loglog(k_gp, P_gp_arr, 'bo-', markersize=8, label=r'$P(\tau_{fold})$')
ax.loglog(k_gp, P_gp_0, 'rs--', markersize=8, label=r'$P(\tau=0)$')
# Reference lines
k_ref = np.linspace(k_gp[0], k_gp[-1], 50)
# P ~ k^{-0.035} reference (Planck-like)
P_planck_ref = k_ref**(-0.035)
P_planck_ref *= P_gp_arr[0] / P_planck_ref[0]
ax.loglog(k_ref, P_planck_ref, 'g:', alpha=0.5, label=r'$k^{-0.035}$ (Planck-like)')
ax.set_xlabel(r'$k_{eff} = \sqrt{C_2}$')
ax.set_ylabel(r'$P(k) = 1/K(k)$')
ax.set_title('Power Spectrum from Stiffness')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: eta_eff vs tau
ax = axes[1, 0]
ax.plot(tau_plot, eta_vs_tau, 'k-o', markersize=4)
ax.axhline(0.035, color='g', linestyle='--', alpha=0.7, label=r'Planck $\eta_{eff} = 0.035$')
ax.axhspan(0.025, 0.045, alpha=0.15, color='g', label='PASS window')
ax.axhline(0.1, color='r', linestyle=':', alpha=0.5, label='FAIL threshold')
ax.axvline(0.20, color='k', linestyle='--', alpha=0.3, label=r'$\tau_{fold}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\eta_{eff}$')
ax.set_title(r'$\eta_{eff}(\tau)$ scan')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_ylim(-1, max(eta_vs_tau) * 1.1)

# Panel 5: n_s vs tau
ax = axes[1, 1]
ax.plot(tau_plot, ns_vs_tau, 'k-o', markersize=4)
ax.axhline(0.9649, color='g', linestyle='--', alpha=0.7, label=r'Planck $n_s = 0.9649$')
ax.axhspan(0.9649 - 0.0042, 0.9649 + 0.0042, alpha=0.15, color='g')
ax.axhline(1.0, color='b', linestyle=':', alpha=0.3, label='$n_s = 1$ (HZ)')
ax.axvline(0.20, color='k', linestyle='--', alpha=0.3, label=r'$\tau_{fold}$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$n_s$')
ax.set_title(r'$n_s(\tau)$ scan')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_ylim(min(ns_vs_tau) - 0.5, max(ns_vs_tau) + 0.5)

# Panel 6: Summary
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"LIFSHITZ-ETA-44 RESULTS\n"
    f"{'=' * 40}\n\n"
    f"Gate verdict: {gate_verdict}\n\n"
    f"Anomalous dimension:\n"
    f"  eta_eff(fold) = {eta_eff_fold:.4f}\n"
    f"  eta_eff(round) = {eta_eff_round_final:.4f}\n\n"
    f"Spectral tilt:\n"
    f"  n_s(fold) = {ns_fold:.4f}\n"
    f"  n_s(round) = {ns_round_final:.4f}\n"
    f"  Planck: 0.9649 +/- 0.0042\n\n"
    f"Branch derivatives (fold):\n"
    f"  dB1/dt = {dB1_fold:.4f}\n"
    f"  dB2/dt = {dB2_fold:.4f}\n"
    f"  dB3/dt = {dB3_fold:.4f}\n\n"
    f"Physical degeneracy scaling:\n"
    f"  n_phys(k) ~ k^{slope_n[0]:.1f}\n"
    f"  K(k) ~ k^{-slope_P[0]:.1f}\n\n"
    f"STRUCTURAL RESULT:\n"
    f"dim(p,q)^2 grows too fast.\n"
    f"Lattice stiffness alone cannot\n"
    f"produce n_s = 0.965."
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(str(base / 's44_lifshitz_eta.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: tier0-computation/s44_lifshitz_eta.png")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
