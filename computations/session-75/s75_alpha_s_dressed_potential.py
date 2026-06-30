#!/usr/bin/env python3
"""
S75-C2-ALPHA-S-DRESSED — Joint (n_s, alpha_s) from BCS-Dressed CW Potential
=============================================================================

Computes the spectral index n_s AND its running alpha_s = dn_s/d ln k from
the BCS-dressed Coleman-Weinberg effective potential V_CW(tau).

Physics
-------
The running alpha_s requires the THIRD slow-roll parameter:

    xi_V^2 = M_Pl^4 * (V' * V''') / V^2

where primes are d/dphi (canonical field).  In terms of the dimensionless
spectral action S(tau) with dphi = sqrt(G) * M_KK * dtau:

    xi_V^2 = (M_Pl^2 / (G * M_KK^2))^2 * (dS/dtau) * (d^3S/dtau^3) / S^2

The running is then:
    alpha_s = 16 * eps_V * eta_V - 24 * eps_V^2 - 2 * xi_V^2

In the Hubble slow-roll convention (shape parameters only):
    eps_H = (1/2) * (S'/S)^2 * S / S''     [not standard — see below]

The HUBBLE-FLOW running is:
    alpha_s = d(n_s-1) / d ln k  at leading order in slow-roll.

For the spectral action, there is also the direct approach:
    n_s(k) = n_s(k_*) + alpha_s * ln(k/k_*) + (1/2)*beta_s * (ln(k/k_*))^2

where alpha_s is evaluated at the pivot scale k_* = 0.05 Mpc^{-1}.

S68 established alpha_s(primordial) = 0 EXACTLY from Bogoliubov saturation.
The CW route generates perturbations from potential curvature, not squeezing,
so alpha_s from CW need not be zero.

Gate: S75-C2-ALPHA-S-DRESSED
    PASS: n_s in [0.955, 0.975] AND alpha_s in [-0.015, +0.005]
    INFO: n_s passes but alpha_s outside Planck 2-sigma, or vice versa
    FAIL: n_s outside [0.950, 0.980] OR |alpha_s| > 0.03

Agent: Landau-Condensed-Matter-Theorist (Session 75)
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
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, Delta_0_OES, Delta_BCS, S_fold, dS_fold, d2S_fold,
    G_DeWitt, M_KK, M_KK_gravity, M_Pl_reduced,
    PI, A_s_CMB, planck_ns, planck_ns_err,
    planck_alpha_s, planck_alpha_s_err,
    a0_fold, a2_fold, a4_fold, H_fold, Z_fold,
    E_cond
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("S75-C2-ALPHA-S-DRESSED: Joint (n_s, alpha_s) from BCS-Dressed CW")
print("=" * 78)

Delta = Delta_BCS  # 0.4643 M_KK (canonical BCS gap)
G = G_DeWitt       # 5.0 (moduli kinetic coefficient)

# Renormalization scale
mu_dimless = 1.0  # (local) mu = M_KK

# Physical scales
M_Pl = M_Pl_reduced  # 2.435e18 GeV
M_KK_phys = M_KK     # 7.43e16 GeV
ratio_MPl_MKK = M_Pl / M_KK_phys  # (local)

print(f"\n  Configuration:")
print(f"    Delta_BCS          = {Delta:.6f} M_KK")
print(f"    G_DeWitt           = {G:.1f}")
print(f"    tau_fold           = {tau_fold}")
print(f"    M_KK (gravity)     = {M_KK_phys:.6e} GeV")
print(f"    M_Pl (reduced)     = {M_Pl:.6e} GeV")
print(f"    M_Pl / M_KK        = {ratio_MPl_MKK:.6f}")
print(f"    Planck n_s         = {planck_ns} +/- {planck_ns_err}")
print(f"    Planck alpha_s     = {planck_alpha_s} +/- {planck_alpha_s_err}")
print(f"    Planck alpha_s 1-sigma band: [{planck_alpha_s - planck_alpha_s_err:.4f}, "
      f"{planck_alpha_s + planck_alpha_s_err:.4f}]")

# =============================================================================
# STEP 0: LOAD INPUT DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load Input Data")
print("=" * 78)

ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

# S36: eigenvalues at multiple tau values (max_pq_sum = 3)
d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)
tau_combined = d_s36['tau_combined']

# S66 BCS-CW results (for cross-check)
d_s66 = np.load(os.path.join(SCRIPT_DIR, 's66_bcs_cw.npz'), allow_pickle=True)

print(f"  S36 tau grid: {tau_combined}")
print(f"  S66 n_s (BCS+CW, Hubble): {float(d_s66['ns_cw_hubble']):.8f}")

# =============================================================================
# STEP 1: BUILD BCS-DRESSED V_CW(tau) AT ALL TAU POINTS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute V_tree^BCS(tau) and V_CW^BCS(tau)")
print("=" * 78)


def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# Sectors with max_pq_sum = 3
sectors = []  # (local)
for p in range(4):
    for q in range(4):
        if p + q <= 3:
            sectors.append((p, q))

# tau values where eigenvalues are stored
tau_evals = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])

# Arrays for contributions (M_KK^4 units)
S_tree_bare = np.zeros(len(tau_evals))   # (local)
S_tree_bcs = np.zeros(len(tau_evals))    # (local)
V_CW_bcs = np.zeros(len(tau_evals))     # (local)

total_pw_modes = np.zeros(len(tau_evals), dtype=int)  # (local)
CW_prefactor = 1.0 / (64.0 * PI**2)  # (local)

t0 = time.time()  # (local)

for i, tau in enumerate(tau_evals):
    for (p, q) in sectors:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key not in d_s36:
            continue

        evals = d_s36[key]
        dim_pq = su3_dim(p, q)  # (local)
        pw_weight = dim_pq ** 2  # (local)

        omega = np.abs(evals)  # (local)
        omega_sq = omega ** 2  # (local)
        M_sq_bcs = omega_sq + Delta ** 2  # (local)
        M_bcs = np.sqrt(M_sq_bcs)  # (local)

        # Tree-level
        S_tree_bare[i] += pw_weight * np.sum(omega)
        S_tree_bcs[i] += pw_weight * np.sum(M_bcs)

        # Coleman-Weinberg BCS-dressed
        V_CW_bcs[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_bcs**2 * (np.log(M_sq_bcs / mu_dimless**2) - 1.5)
        )

        total_pw_modes[i] += pw_weight * len(evals)

t_compute = time.time() - t0  # (local)

# Total effective action (dimensionless M_KK^4 units)
S_total_bcs = S_tree_bcs + V_CW_bcs  # (local)

print(f"  Computed in {t_compute:.2f}s")
print(f"  Total PW-weighted modes = {total_pw_modes[0]}")
print(f"\n  {'tau':>6s}  {'S_tree^BCS':>14s}  {'V_CW^BCS':>14s}  {'S_total':>14s}")
print(f"  {'----':>6s}  {'-'*14}  {'-'*14}  {'-'*14}")
for j in range(len(tau_evals)):
    print(f"  {tau_evals[j]:6.3f}  {S_tree_bcs[j]:14.2f}  {V_CW_bcs[j]:14.2f}  "
          f"{S_total_bcs[j]:14.2f}")

# =============================================================================
# STEP 2: SPLINE AND DERIVATIVES UP TO THIRD ORDER
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Cubic Spline — S, S', S'', S''' at the Fold")
print("=" * 78)

# Use near-fold tau points (skip tau=0.05 which is far from fold)
idx_near = np.arange(1, len(tau_evals))  # (local) indices 1-6: tau=0.16..0.22
tau_near = tau_evals[idx_near]  # (local)
tau_f = tau_fold  # 0.19

# BCS tree + BCS CW (main config)
cs_D = CubicSpline(tau_near, S_total_bcs[idx_near])  # (local)
S_val = float(cs_D(tau_f))       # (local)
dS_val = float(cs_D(tau_f, 1))   # (local) dS/dtau
d2S_val = float(cs_D(tau_f, 2))  # (local) d^2S/dtau^2
d3S_val = float(cs_D(tau_f, 3))  # (local) d^3S/dtau^3

print(f"  S(tau_fold)     = {S_val:.4f}")
print(f"  S'(tau_fold)    = {dS_val:.4f}")
print(f"  S''(tau_fold)   = {d2S_val:.4f}")
print(f"  S'''(tau_fold)  = {d3S_val:.4f}")

# Cross-check with canonical values
print(f"\n  Cross-check against canonical:")
print(f"    S_fold   (canonical) = {S_fold:.4f}")
print(f"    dS_fold  (canonical) = {dS_fold:.4f}")
print(f"    d2S_fold (canonical) = {d2S_fold:.4f}")

dev_S = abs(S_val - S_fold) / S_fold  # (local)
dev_dS = abs(dS_val - dS_fold) / abs(dS_fold)  # (local)
dev_d2S = abs(d2S_val - d2S_fold) / abs(d2S_fold)  # (local)
print(f"    |S - S_fold| / S_fold       = {dev_S:.4e}")
print(f"    |S' - dS_fold| / |dS_fold|  = {dev_dS:.4e}")
print(f"    |S'' - d2S_fold| / |d2S_fold| = {dev_d2S:.4e}")

# Note on S''' reliability: CubicSpline's third derivative is piecewise constant.
# For 6 near-fold points, S''' at the fold is determined by the cubic spanning
# [0.18, 0.19] and [0.19, 0.21].  This is the leading source of uncertainty.

# Finite difference cross-check for S'''
h_fd = 0.01  # (local) step for finite differences
d3S_fd = float(cs_D(tau_f + h_fd, 2) - cs_D(tau_f - h_fd, 2)) / (2 * h_fd)  # (local)
print(f"\n  S''' finite-difference cross-check:")
print(f"    S''' (spline)    = {d3S_val:.4f}")
print(f"    S''' (FD, h=0.01) = {d3S_fd:.4f}")
print(f"    Deviation        = {abs(d3S_val - d3S_fd):.4f}")

# Also try with bare tree spline for comparison
cs_bare = CubicSpline(tau_near, S_tree_bare[idx_near])  # (local)
d3S_bare = float(cs_bare(tau_f, 3))  # (local)
print(f"    S''' (bare tree) = {d3S_bare:.4f}")

# =============================================================================
# STEP 3: SLOW-ROLL PARAMETERS — All three (eps_V, eta_V, xi_V^2)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Slow-Roll Parameters (Potential Convention)")
print("=" * 78)

print("""
  Canonical field: phi = sqrt(G) * M_KK * tau
  Physical potential: V = S(tau) * M_KK^4   [GeV^4]

  First slow-roll parameter:
    eps_V = (M_Pl^2 / 2) * (V'/V)^2
          = (M_Pl^2 / (2*G*M_KK^2)) * (S'/S)^2
          = R^2 / (2*G) * (S'/S)^2    where R = M_Pl/M_KK

  Second slow-roll parameter:
    eta_V = M_Pl^2 * V''/V
          = (M_Pl^2 / (G*M_KK^2)) * S''/S
          = R^2 / G * (S''/S)

  Third slow-roll parameter:
    xi_V^2 = M_Pl^4 * (V' * V''') / V^2
           = (M_Pl^4 / (G^2 * M_KK^4)) * (S' * S''') / S^2
           = R^4 / G^2 * (S' * S''') / S^2

  Running:
    alpha_s = 16 * eps_V * eta_V  -  24 * eps_V^2  -  2 * xi_V^2
""")

R = ratio_MPl_MKK  # (local) M_Pl / M_KK
R2 = R**2  # (local)
R4 = R**4  # (local)

# Potential slow-roll parameters
eps_V = (R2 / (2.0 * G)) * (dS_val / S_val)**2  # (local)
eta_V = (R2 / G) * (d2S_val / S_val)  # (local)
xi_V_sq = (R4 / G**2) * (dS_val * d3S_val) / S_val**2  # (local)

print(f"  R = M_Pl / M_KK = {R:.6f}")
print(f"  R^2 = {R2:.6f}")
print(f"  R^4 = {R4:.6f}")
print(f"  G   = {G:.1f}")
print(f"\n  Spectral action ratios:")
print(f"    S'/S       = {dS_val / S_val:.8f}")
print(f"    S''/S      = {d2S_val / S_val:.8f}")
print(f"    S'*S'''/S^2 = {dS_val * d3S_val / S_val**2:.8f}")
print(f"\n  Slow-roll parameters:")
print(f"    eps_V  = {eps_V:.8e}")
print(f"    eta_V  = {eta_V:.8e}")
print(f"    xi_V^2 = {xi_V_sq:.8e}")

# Spectral index (potential convention)
ns_pot = 1.0 - 6.0 * eps_V + 2.0 * eta_V  # (local)
print(f"\n  n_s (potential) = 1 - 6*eps_V + 2*eta_V = {ns_pot:.8f}")

# Running (potential convention)
alpha_s_pot = 16.0 * eps_V * eta_V - 24.0 * eps_V**2 - 2.0 * xi_V_sq  # (local)
print(f"\n  alpha_s (potential) = 16*eps_V*eta_V - 24*eps_V^2 - 2*xi_V^2")
print(f"    term1 = 16*eps_V*eta_V = {16.0 * eps_V * eta_V:.8e}")
print(f"    term2 = -24*eps_V^2    = {-24.0 * eps_V**2:.8e}")
print(f"    term3 = -2*xi_V^2      = {-2.0 * xi_V_sq:.8e}")
print(f"    alpha_s                = {alpha_s_pot:.8e}")

# Check: slow-roll validity
print(f"\n  Slow-roll validity:")
print(f"    eps_V = {eps_V:.4e} {'<< 1 (valid)' if eps_V < 0.1 else '>> 1 (VIOLATED!)'}")
print(f"    |eta_V| = {abs(eta_V):.4e} {'<< 1 (valid)' if abs(eta_V) < 0.1 else '>> 1 (VIOLATED!)'}")

# =============================================================================
# STEP 4: HUBBLE SLOW-ROLL — Shape Parameters
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Hubble Slow-Roll (Shape Parameters)")
print("=" * 78)

print("""
  The Hubble (shape) convention uses dimensionless spectral action ratios:

    eps_H = (1/2) * (S')^2 / (S * S'')

  For the running, we need the second Hubble flow parameter:
    eta_H = eps_H - (1/2) * d(ln eps_H) / dN

  In practice, for the spectral action, the running comes from the
  variation of the slow-roll parameters with respect to the field
  displacement (number of e-folds N).

  Since n_s = 1 - 2*eps_H in the Hubble convention, the running is:
    alpha_s = d(n_s) / d(ln k) = -2 * d(eps_H) / d(ln k)

  We compute d(eps_H)/dtau and convert via:
    d(ln k) = dN = H * dt = (V / (sqrt(G)*M_KK)) * dtau / (dV/dtau)
            => dtau/dN depends on the dynamics.

  For the CW potential route, we compute eps_H(tau) on the spline
  and take its derivative numerically.
""")

# Hubble slow-roll at fold
eps_H = 0.5 * dS_val**2 / (S_val * d2S_val)  # (local)
ns_hubble = 1.0 - 2.0 * eps_H  # (local)

print(f"  eps_H = {eps_H:.8f}")
print(f"  n_s (Hubble) = {ns_hubble:.8f}")

# Cross-check S66
dev_ns_s66 = abs(ns_hubble - float(d_s66['ns_cw_hubble']))  # (local)
print(f"\n  CHK2: n_s(Hubble) = {ns_hubble:.8f}")
print(f"        S66 value   = {float(d_s66['ns_cw_hubble']):.8f}")
print(f"        Deviation   = {dev_ns_s66:.2e} {'OK' if dev_ns_s66 < 1e-6 else 'CHECK'}")

# Compute eps_H(tau) on a fine grid for numerical running
tau_fine = np.linspace(0.16, 0.22, 500)  # (local)
S_fine = cs_D(tau_fine)       # (local)
dS_fine = cs_D(tau_fine, 1)   # (local)
d2S_fine = cs_D(tau_fine, 2)  # (local)

# eps_H(tau) array
eps_H_fine = 0.5 * dS_fine**2 / (S_fine * d2S_fine)  # (local)

# d(eps_H)/dtau at the fold via finite difference on spline
h_eps = 1e-4  # (local) step
eps_H_plus = 0.5 * float(cs_D(tau_f + h_eps, 1))**2 / (float(cs_D(tau_f + h_eps)) * float(cs_D(tau_f + h_eps, 2)))  # (local)
eps_H_minus = 0.5 * float(cs_D(tau_f - h_eps, 1))**2 / (float(cs_D(tau_f - h_eps)) * float(cs_D(tau_f - h_eps, 2)))  # (local)
deps_H_dtau = (eps_H_plus - eps_H_minus) / (2 * h_eps)  # (local)

print(f"\n  d(eps_H)/dtau at fold = {deps_H_dtau:.8e}")

# The running in the Hubble convention:
# alpha_s = -2 * d(eps_H)/dN
# Need dtau/dN: in slow-roll, dN = H*dt and H*dtau = (H / f_tau_dot) * dtau
# More directly: dN = -(V / V') dphi = -(S / dS_dtau) * (1/sqrt(G)*M_KK) * sqrt(G)*M_KK dtau
#              = -(S / S') dtau   [in the Hubble convention]
# so dtau/dN = -S'/S   =>  d(eps_H)/dN = -(S'/S) * deps_H_dtau

# Wait -- be careful with signs. In standard inflation:
#   dN = H dt, and dN/dphi = -V'/(V) * (1/M_Pl^2)  [for V' > 0 rolling down]
# But our convention is that tau increases THROUGH the fold.
# The number of e-folds decreases as we approach the end of inflation.
# d(ln k) = dN = -(1/(eps_H)) * d(eps_H)/d(eps_H) ...

# More carefully: for a generic slow-roll potential:
# alpha_s = dn_s / d(ln k) at the pivot
# In the potential convention this is the exact formula already computed above.
# In the Hubble convention, we can compute it as:
#
#   alpha_s = -2 * (d eps_H / d ln k)
#           = -2 * (d eps_H / dN) * (dN / d ln k)
#
# At leading order dN = d ln k (aH evaluated at horizon crossing), so:
#   alpha_s = -2 * d(eps_H) / dN
#
# And d(eps_H)/dN = d(eps_H)/dtau * dtau/dN
#
# From the Hamilton-Jacobi flow: dphi/dN = -M_Pl^2 * V'/V = -M_Pl^2 * (S'/S) / (sqrt(G)*M_KK)
# => dtau/dN = dphi/dN / (sqrt(G)*M_KK) = -(M_Pl^2 / (G*M_KK^2)) * (S'/S)
#            = -(R^2/G) * (S'/S)

dtau_dN = -(R2 / G) * (dS_val / S_val)  # (local)
deps_H_dN = deps_H_dtau * dtau_dN  # (local)
alpha_s_hubble = -2.0 * deps_H_dN  # (local)

print(f"  dtau/dN at fold = {dtau_dN:.8e}")
print(f"  d(eps_H)/dN     = {deps_H_dN:.8e}")
print(f"  alpha_s (Hubble) = -2 * d(eps_H)/dN = {alpha_s_hubble:.8e}")

# =============================================================================
# STEP 5: TRANSIT RUNNING — Physical dtau/dN from dynamics
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Transit Running (Physical dtau/dN)")
print("=" * 78)

from canonical_constants import dt_transit, v_terminal

print("""
  The Hubble-flow running computed above used the slow-roll formula
  for dtau/dN, which gives dtau/dN = -(R^2/G)*(S'/S).  This is
  enormously large because R = M_Pl/M_KK >> 1, yielding |alpha_s| ~ 20.

  But the transit is NOT slow-roll.  It is an impulsive supersonic event
  (Mach 13.75).  The physical mapping from tau to e-folds uses the
  ACTUAL transit dynamics:

    dtau/dN = (dtau/dt) / (da/adt * 1/a) = v_terminal / H_fold

  where v_terminal = 26.54 M_KK is the modulus velocity during transit
  and H_fold = 586.5 M_KK is the Hubble rate.

  This gives dtau/dN = v/H ~ 0.045, not ~48 from the slow-roll formula.
  The slow-roll formula ASSUMES the field slowly evolves down the potential;
  the transit blows through it at Mach 13.75.

  The physical running is therefore:
    alpha_s(transit) = -2 * d(eps_H)/dtau * (v_terminal / H_fold)
""")

# Shape parameters at fold
sigma_1 = dS_val / S_val     # (local) S'/S
sigma_2 = d2S_val / S_val    # (local) S''/S
sigma_3 = d3S_val / S_val    # (local) S'''/S

print(f"  Shape parameters at fold:")
print(f"    sigma_1 = S'/S   = {sigma_1:.8f}")
print(f"    sigma_2 = S''/S  = {sigma_2:.8f}")
print(f"    sigma_3 = S'''/S = {sigma_3:.8f}")
print(f"    eps_H = sigma_1^2/(2*sigma_2) = {sigma_1**2 / (2 * sigma_2):.8f}")

# Transit e-folds and dtau/dN
N_transit = H_fold * dt_transit  # (local) total transit e-folds
dtau_dN_transit = v_terminal / H_fold  # (local) physical conversion
delta_tau_transit = v_terminal * dt_transit  # (local)

print(f"\n  Transit dynamics:")
print(f"    v_terminal    = {v_terminal:.4f} M_KK")
print(f"    H_fold        = {H_fold:.4f} M_KK")
print(f"    dt_transit    = {dt_transit:.6e} M_KK^-1")
print(f"    N_transit     = H*dt = {N_transit:.6f} e-folds")
print(f"    delta_tau     = v*dt = {delta_tau_transit:.6e}")
print(f"    dtau/dN(transit) = v/H = {dtau_dN_transit:.6e}")
print(f"    dtau/dN(slow-roll) = {dtau_dN:.6e}")
print(f"    Ratio (SR/transit) = {abs(dtau_dN / dtau_dN_transit):.2f}x")

# Physical running using transit dynamics
alpha_s_transit = -2.0 * deps_H_dtau * dtau_dN_transit  # (local)

print(f"\n  d(eps_H)/dtau = {deps_H_dtau:.8e}")
print(f"  alpha_s(transit) = -2 * d(eps_H)/dtau * v/H")
print(f"                   = -2 * {deps_H_dtau:.6e} * {dtau_dN_transit:.6e}")
print(f"                   = {alpha_s_transit:.8e}")
print(f"\n  alpha_s(slow-roll) = {alpha_s_hubble:.8e}  [for comparison -- UNPHYSICAL]")
print(f"  Ratio = {abs(alpha_s_hubble / alpha_s_transit):.2f}x  (slow-roll amplifies by R^2/G * S'/S_fold)")

# Planck band check
delta_N_planck = np.log(0.2 / 0.002)  # (local)
print(f"\n  Planck k-band: [0.002, 0.2] Mpc^-1 = {delta_N_planck:.4f} e-folds")
print(f"  Transit covers {N_transit:.4f} e-folds")
print(f"  Transit / Planck band = {N_transit / delta_N_planck:.4f}")
if N_transit < delta_N_planck:
    print(f"  NOTE: Transit does NOT span the full Planck band.")
    print(f"  Modes at k < k_min(transit) or k > k_max(transit) are NOT generated by the CW mechanism.")

# =============================================================================
# STEP 6: CONSISTENCY CHECK — de Sitter limit (CHK1)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: CHK1 — de Sitter Consistency Relation")
print("=" * 78)

print("""
  In exact de Sitter (eps_V = eta_V = 0), alpha_s = 0 trivially.
  At first order in slow-roll, the consistency relation is:
    alpha_s = 16*eps_V*eta_V - 24*eps_V^2 - 2*xi_V^2

  If eps_V is very large (slow-roll violated), this formula is not reliable
  as a perturbative expansion.  The dominant term is then 2*xi_V^2, and
  the other terms are higher-order corrections.

  We check: if eps_V >> 1, the formula alpha_s(potential) is NOT trustworthy.
  The transit-based alpha_s is the physical quantity.
""")

print(f"  Potential convention terms:")
print(f"    16*eps_V*eta_V = {16.0 * eps_V * eta_V:.8e}")
print(f"    -24*eps_V^2    = {-24.0 * eps_V**2:.8e}")
print(f"    -2*xi_V^2      = {-2.0 * xi_V_sq:.8e}")
print(f"    Sum = alpha_s  = {alpha_s_pot:.8e}")

print(f"\n  THREE alpha_s values:")
print(f"    alpha_s(potential)  = {alpha_s_pot:.8e}  (INVALID: eps_V >> 1)")
print(f"    alpha_s(SR Hubble)  = {alpha_s_hubble:.8e}  (uses slow-roll dtau/dN)")
print(f"    alpha_s(transit)    = {alpha_s_transit:.8e}  (uses physical v/H)")

if eps_V > 0.1:
    print(f"\n  eps_V = {eps_V:.4e} >> 1: potential slow-roll VIOLATED.")
    print(f"  The slow-roll Hubble formula also fails because it uses the")
    print(f"  wrong dtau/dN mapping (slow-roll instead of transit dynamics).")
    print(f"  The TRANSIT alpha_s uses physical v_terminal/H_fold and is correct.")
    alpha_s_physical = alpha_s_transit  # (local)
    ns_physical = ns_hubble  # (local)
    convention_used = "Hubble n_s + Transit alpha_s"  # (local)
else:
    print(f"\n  Slow-roll valid. All conventions should give consistent results.")
    alpha_s_physical = alpha_s_transit  # (local)
    ns_physical = ns_pot  # (local)
    convention_used = "Potential"  # (local)

print(f"\n  PHYSICAL alpha_s = {alpha_s_physical:.8e}  ({convention_used})")
print(f"  PHYSICAL n_s     = {ns_physical:.8f}  ({convention_used})")

# =============================================================================
# STEP 7: P(k) OVER PLANCK BAND [0.002, 0.2] Mpc^{-1}
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: P(k) Over Full Planck Band")
print("=" * 78)

print("""
  The power spectrum as a function of k:
    P_R(k) = A_s * (k/k_*)^{n_s - 1 + (1/2)*alpha_s*ln(k/k_*)}

  where k_* = 0.05 Mpc^{-1} is the Planck pivot scale.

  For the CW potential, A_s comes from the spectral formula:
    A_s = H_fold^2 / (8*pi * a_2 * eps_H)

  We use n_s and alpha_s from the Hubble flow analysis.
""")

# Pivot scale
k_star = 0.05  # (local) Mpc^{-1}

# A_s from spectral formula (same as S75-A4-CW-JOINT)
A_s_spectral = H_fold**2 / (8.0 * PI * a2_fold * eps_H)  # (local)
log10_As_ratio = np.log10(A_s_spectral / A_s_CMB)  # (local)

print(f"  A_s (spectral) = {A_s_spectral:.6e}")
print(f"  A_s (Planck)   = {A_s_CMB:.6e}")
print(f"  log10(A_s/A_s_obs) = {log10_As_ratio:.4f}")

# k array over Planck band
k_arr = np.logspace(np.log10(0.002), np.log10(0.2), 200)  # (local) Mpc^{-1}
ln_k_ratio = np.log(k_arr / k_star)  # (local) ln(k/k_*)

# Power spectrum: P(k) = A_s * (k/k_*)^{(n_s-1) + (1/2)*alpha_s*ln(k/k_*)}
# The exponent of (k/k_*) is:
#   n_s - 1 + alpha_s * ln(k/k_*) / 2 + ...
# So: P(k) = A_s * exp[ (n_s - 1) * ln(k/k_*) + (1/2)*alpha_s*(ln(k/k_*))^2 ]

# Using spectral A_s
exponent_spectral = (ns_physical - 1.0) * ln_k_ratio + 0.5 * alpha_s_physical * ln_k_ratio**2  # (local)
P_k_spectral = A_s_spectral * np.exp(exponent_spectral)  # (local)

# Using observed A_s (for comparison with Planck)
exponent_planck = (planck_ns - 1.0) * ln_k_ratio + 0.5 * planck_alpha_s * ln_k_ratio**2  # (local)
P_k_planck = A_s_CMB * np.exp(exponent_planck)  # (local)

# Using framework n_s with observed A_s (to isolate tilt effect)
exponent_fw_tilt = (ns_physical - 1.0) * ln_k_ratio + 0.5 * alpha_s_physical * ln_k_ratio**2  # (local)
P_k_fw_tilt = A_s_CMB * np.exp(exponent_fw_tilt)  # (local)

print(f"\n  P(k) at selected scales (using A_s_spectral):")
k_report = [0.002, 0.01, 0.05, 0.1, 0.2]  # (local)
for k_val in k_report:
    ln_kr = np.log(k_val / k_star)  # (local)
    exp_val = (ns_physical - 1.0) * ln_kr + 0.5 * alpha_s_physical * ln_kr**2  # (local)
    P_val = A_s_spectral * np.exp(exp_val)  # (local)
    print(f"    k = {k_val:.3f} Mpc^-1:  P(k) = {P_val:.6e}")

# Range across Planck band
P_ratio_band = P_k_fw_tilt[-1] / P_k_fw_tilt[0]  # (local)
print(f"\n  P(k=0.2) / P(k=0.002) [FW tilt] = {P_ratio_band:.6f}")
print(f"  Expected from n_s alone: (0.2/0.002)^{ns_physical-1:.4f} = "
      f"{(0.2/0.002)**(ns_physical-1):.6f}")

# =============================================================================
# STEP 8: SCHEME DEPENDENCE — mu variation
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Scheme Dependence (mu variation) for alpha_s")
print("=" * 78)

mu_values = [0.5, 1.0, 2.0]  # (local)
ns_scheme_arr = []  # (local)
alpha_s_scheme_arr = []  # (local)
eps_H_scheme_arr = []  # (local)

for mu_val in mu_values:
    # Recompute V_CW at different mu
    V_CW_mu = np.zeros(len(tau_evals))  # (local)
    for i, tau in enumerate(tau_evals):
        for (p, q) in sectors:
            key = f'evals_tau{tau:.3f}_{p}_{q}'
            if key not in d_s36:
                continue
            evals = d_s36[key]
            dim_pq = su3_dim(p, q)  # (local)
            pw_weight = dim_pq ** 2  # (local)
            omega_sq = np.abs(evals) ** 2  # (local)
            M_sq = omega_sq + Delta ** 2  # (local)
            V_CW_mu[i] += CW_prefactor * pw_weight * np.sum(
                M_sq**2 * (np.log(M_sq / mu_val**2) - 1.5)
            )

    S_total_mu = S_tree_bcs + V_CW_mu  # (local)
    cs_mu = CubicSpline(tau_near, S_total_mu[idx_near])  # (local)

    S_mu = float(cs_mu(tau_f))  # (local)
    dS_mu = float(cs_mu(tau_f, 1))  # (local)
    d2S_mu = float(cs_mu(tau_f, 2))  # (local)
    d3S_mu = float(cs_mu(tau_f, 3))  # (local)

    eps_H_mu = 0.5 * dS_mu**2 / (S_mu * d2S_mu) if (d2S_mu > 0 and S_mu > 0) else np.inf  # (local)
    ns_mu = 1.0 - 2.0 * eps_H_mu  # (local)

    # alpha_s from transit flow (physical)
    eps_H_p = 0.5 * float(cs_mu(tau_f + h_eps, 1))**2 / (float(cs_mu(tau_f + h_eps)) * float(cs_mu(tau_f + h_eps, 2)))  # (local)
    eps_H_m = 0.5 * float(cs_mu(tau_f - h_eps, 1))**2 / (float(cs_mu(tau_f - h_eps)) * float(cs_mu(tau_f - h_eps, 2)))  # (local)
    deps_H_dtau_mu = (eps_H_p - eps_H_m) / (2 * h_eps)  # (local)
    alpha_s_mu = -2.0 * deps_H_dtau_mu * dtau_dN_transit  # (local) uses physical v/H

    ns_scheme_arr.append(ns_mu)
    alpha_s_scheme_arr.append(alpha_s_mu)
    eps_H_scheme_arr.append(eps_H_mu)

    print(f"  mu = {mu_val:.1f} M_KK:")
    print(f"    eps_H     = {eps_H_mu:.8f}")
    print(f"    n_s       = {ns_mu:.8f}")
    print(f"    alpha_s   = {alpha_s_mu:.8e}")

ns_spread = max(ns_scheme_arr) - min(ns_scheme_arr)  # (local)
alpha_s_spread = max(alpha_s_scheme_arr) - min(alpha_s_scheme_arr)  # (local)
print(f"\n  n_s spread     = {ns_spread:.6f} ({ns_spread / planck_ns_err:.4f} sigma)")
print(f"  alpha_s spread = {alpha_s_spread:.8e}")

# =============================================================================
# STEP 9: CHK3 — Planck constraint
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: CHK3 — Planck Constraint on alpha_s")
print("=" * 78)

alpha_s_1sig_lo = planck_alpha_s - planck_alpha_s_err  # (local)
alpha_s_1sig_hi = planck_alpha_s + planck_alpha_s_err  # (local)
alpha_s_2sig_lo = planck_alpha_s - 2 * planck_alpha_s_err  # (local)
alpha_s_2sig_hi = planck_alpha_s + 2 * planck_alpha_s_err  # (local)

print(f"  Planck alpha_s = {planck_alpha_s} +/- {planck_alpha_s_err}")
print(f"  1-sigma band: [{alpha_s_1sig_lo:.4f}, {alpha_s_1sig_hi:.4f}]")
print(f"  2-sigma band: [{alpha_s_2sig_lo:.4f}, {alpha_s_2sig_hi:.4f}]")
print(f"\n  Framework alpha_s = {alpha_s_physical:.8e}")

# Tension in sigma
alpha_s_tension = abs(alpha_s_physical - planck_alpha_s) / planck_alpha_s_err  # (local)
print(f"  Tension = |alpha_s(FW) - alpha_s(Planck)| / sigma = {alpha_s_tension:.4f} sigma")

in_1sig = alpha_s_1sig_lo <= alpha_s_physical <= alpha_s_1sig_hi  # (local)
in_2sig = alpha_s_2sig_lo <= alpha_s_physical <= alpha_s_2sig_hi  # (local)
print(f"  Within 1-sigma: {'YES' if in_1sig else 'NO'}")
print(f"  Within 2-sigma: {'YES' if in_2sig else 'NO'}")

# =============================================================================
# STEP 10: MAIN RESULTS AND GATE CLASSIFICATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Main Results — Gate S75-C2-ALPHA-S-DRESSED")
print("=" * 78)

ns_final = ns_physical  # (local)
alpha_s_final = alpha_s_physical  # (local)

print(f"\n  PRIMARY RESULTS ({convention_used} convention):")
print(f"    n_s            = {ns_final:.8f}")
print(f"    alpha_s        = {alpha_s_final:.8e}")
print(f"    eps_H          = {eps_H:.8f}")
print(f"    eps_V          = {eps_V:.8e}")
print(f"    eta_V          = {eta_V:.8e}")
print(f"    xi_V^2         = {xi_V_sq:.8e}")
print(f"    A_s (spectral) = {A_s_spectral:.6e}")
print(f"    n_s tension    = {abs(ns_final - planck_ns) / planck_ns_err:.4f} sigma")
print(f"    alpha_s tension = {alpha_s_tension:.4f} sigma")

# Gate classification
ns_in_pass = (0.955 <= ns_final <= 0.975)  # (local)
alpha_s_in_pass = (-0.015 <= alpha_s_final <= 0.005)  # (local)
ns_in_fail = (ns_final < 0.950 or ns_final > 0.980)  # (local)
alpha_s_in_fail = (abs(alpha_s_final) > 0.03)  # (local)

if ns_in_pass and alpha_s_in_pass:
    gate_verdict = "PASS"  # (local)
    gate_detail = (f"PASS: n_s = {ns_final:.6f} in [0.955, 0.975] AND "
                   f"alpha_s = {alpha_s_final:.6e} in [-0.015, +0.005]")
elif ns_in_fail or alpha_s_in_fail:
    gate_verdict = "FAIL"  # (local)
    gate_detail = (f"FAIL: n_s = {ns_final:.6f} "
                   f"{'OUTSIDE [0.950, 0.980]' if ns_in_fail else 'in range'}, "
                   f"alpha_s = {alpha_s_final:.6e} "
                   f"{'|alpha_s| > 0.03' if alpha_s_in_fail else 'in range'}")
else:
    gate_verdict = "INFO"  # (local)
    gate_detail = (f"INFO: n_s = {ns_final:.6f} "
                   f"{'in [0.955, 0.975]' if ns_in_pass else 'OUTSIDE pass range'}, "
                   f"alpha_s = {alpha_s_final:.6e} "
                   f"{'in [-0.015, +0.005]' if alpha_s_in_pass else 'OUTSIDE pass range'}")

print(f"\n  GATE S75-C2-ALPHA-S-DRESSED: {gate_verdict}")
print(f"  {gate_detail}")

# Comparison with S68 Bogoliubov result
print(f"\n  S68 comparison:")
print(f"    S68 alpha_s (Bogoliubov) = 0 (exact, by saturation)")
print(f"    S75 alpha_s (CW)         = {alpha_s_final:.8e}")
print(f"    These are DIFFERENT mechanisms:")
print(f"      S68: squeezing generates scale-invariant perturbations (alpha_s = 0)")
print(f"      S75: potential curvature generates scale-dependent tilt (alpha_s != 0)")

# =============================================================================
# PLOTTING
# =============================================================================
print("\n" + "=" * 78)
print("Generating plots...")
print("=" * 78)

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, hspace=0.40, wspace=0.30)

# Panel 1: S(tau) profiles
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_evals, S_tree_bare, 'k--', label=r'$S_{\rm tree}^{\rm bare}$', lw=1.5)
ax1.plot(tau_evals, S_tree_bcs, 'b-', label=r'$S_{\rm tree}^{\rm BCS}$', lw=1.5)
ax1.plot(tau_evals, S_total_bcs, 'r-', label=r'$S_{\rm tree}^{\rm BCS} + V_{\rm CW}$', lw=2)
ax1.axvline(tau_fold, color='gray', ls=':', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax1.set_xlabel(r'$\tau$')
ax1.set_ylabel(r'$S(\tau)$  [M$_{\rm KK}^4$ units]')
ax1.set_title('Effective Potential (BCS-Dressed CW)')
ax1.legend(fontsize=9)

# Panel 2: eps_H(tau)
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_fine, eps_H_fine, 'r-', lw=2)
ax2.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax2.axhline(eps_H, color='blue', ls='--', alpha=0.5, label=f'$\\epsilon_H(\\tau_f)$ = {eps_H:.6f}')
ax2.set_xlabel(r'$\tau$')
ax2.set_ylabel(r'$\epsilon_H(\tau)$')
ax2.set_title('Hubble Slow-Roll Parameter')
ax2.legend(fontsize=9)

# Panel 3: P(k) — framework tilt with observed amplitude
ax3 = fig.add_subplot(gs[1, 0])
ax3.loglog(k_arr, P_k_fw_tilt * 1e9, 'r-', lw=2, label=f'Framework: $n_s$={ns_final:.4f}, $\\alpha_s$={alpha_s_final:.2e}')
ax3.loglog(k_arr, P_k_planck * 1e9, 'k--', lw=1.5, label=f'Planck: $n_s$={planck_ns}, $\\alpha_s$={planck_alpha_s}')
ax3.axvline(k_star, color='gray', ls=':', alpha=0.5, label='$k_*$ = 0.05 Mpc$^{-1}$')
ax3.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax3.set_ylabel(r'$10^9 \times \mathcal{P}_{\mathcal{R}}(k)$')
ax3.set_title(r'Power Spectrum $\mathcal{P}(k)$ (using $A_{s,\rm obs}$)')
ax3.legend(fontsize=8)
ax3.set_xlim(0.002, 0.2)

# Panel 4: P(k) ratio (framework / Planck)
ax4 = fig.add_subplot(gs[1, 1])
P_ratio = P_k_fw_tilt / P_k_planck  # (local)
ax4.semilogx(k_arr, P_ratio, 'r-', lw=2)
ax4.axhline(1.0, color='gray', ls='--', alpha=0.5)
ax4.axvline(k_star, color='gray', ls=':', alpha=0.5)
ax4.set_xlabel(r'$k$ [Mpc$^{-1}$]')
ax4.set_ylabel(r'$\mathcal{P}_{\rm FW}(k) / \mathcal{P}_{\rm Planck}(k)$')
ax4.set_title('Framework / Planck Ratio')
# Add shaded 1-sigma band
# The tilt-only ratio at edges of Planck band
ax4.fill_between(k_arr, 0.95, 1.05, alpha=0.15, color='blue', label=r'$\pm 5\%$')
ax4.legend(fontsize=9)
ax4.set_xlim(0.002, 0.2)

# Panel 5: Slow-roll parameters
ax5 = fig.add_subplot(gs[2, 0])
labels_sr = ['$\\epsilon_H$', '$\\epsilon_V$', '$|\\eta_V|$', '$|\\xi_V^2|$']
values_sr = [eps_H, eps_V, abs(eta_V), abs(xi_V_sq)]
colors_sr = ['blue', 'red', 'green', 'orange']
bars = ax5.bar(labels_sr, np.log10(np.array(values_sr) + 1e-30), color=colors_sr, alpha=0.7)
ax5.axhline(0, color='gray', ls='--', alpha=0.5, label='$=1$')
ax5.axhline(-1, color='gray', ls=':', alpha=0.3, label='$=0.1$')
ax5.set_ylabel(r'$\log_{10}$(parameter)')
ax5.set_title('Slow-Roll Parameters')
ax5.legend(fontsize=8)

# Panel 6: Scheme dependence
ax6 = fig.add_subplot(gs[2, 1])
mu_plot = mu_values  # (local)
ax6.plot(mu_plot, [a * 1e6 for a in alpha_s_scheme_arr], 'ro-', lw=2, markersize=8,
         label=r'$\alpha_s \times 10^6$')
ax6.axhline(planck_alpha_s * 1e6, color='gray', ls='--', alpha=0.5,
            label=f'Planck $\\alpha_s$ = {planck_alpha_s}')
ax6.fill_between(mu_plot,
                 [(planck_alpha_s - planck_alpha_s_err) * 1e6] * len(mu_plot),
                 [(planck_alpha_s + planck_alpha_s_err) * 1e6] * len(mu_plot),
                 alpha=0.15, color='blue')  # (local)
ax6.set_xlabel(r'$\mu$ [M$_{\rm KK}$]')
ax6.set_ylabel(r'$\alpha_s \times 10^6$')
ax6.set_title(r'Scheme Dependence of $\alpha_s$')
ax6.legend(fontsize=9)

fig.suptitle(f'S75-C2: Joint ($n_s$, $\\alpha_s$) from BCS-Dressed CW Potential\n'
             f'Gate: {gate_verdict}  |  $n_s$ = {ns_final:.6f}  |  $\\alpha_s$ = {alpha_s_final:.4e}',
             fontsize=13, fontweight='bold')

plt.savefig('s75_alpha_s_dressed_potential.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: s75_alpha_s_dressed_potential.png")
plt.close()

# =============================================================================
# SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("Saving data...")
print("=" * 78)

np.savez('s75_alpha_s_dressed_potential.npz',
         # Gate
         gate_name='S75-C2-ALPHA-S-DRESSED',
         gate_verdict=gate_verdict,
         convention_used=convention_used,
         # Primary results
         ns_final=ns_final,
         alpha_s_final=alpha_s_final,
         eps_H=eps_H,
         eps_V=eps_V,
         eta_V=eta_V,
         xi_V_sq=xi_V_sq,
         A_s_spectral=A_s_spectral,
         log10_As_ratio=log10_As_ratio,
         # Spectral action derivatives
         S_val=S_val,
         dS_val=dS_val,
         d2S_val=d2S_val,
         d3S_val=d3S_val,
         sigma_1=sigma_1,
         sigma_2=sigma_2,
         sigma_3=sigma_3,
         # Tensions
         ns_tension_sigma=abs(ns_final - planck_ns) / planck_ns_err,
         alpha_s_tension_sigma=alpha_s_tension,
         # Scheme dependence
         mu_values=np.array(mu_values),
         ns_scheme=np.array(ns_scheme_arr),
         alpha_s_scheme=np.array(alpha_s_scheme_arr),
         ns_spread=ns_spread,
         alpha_s_spread=alpha_s_spread,
         # P(k) data
         k_arr=k_arr,
         P_k_fw_tilt=P_k_fw_tilt,
         P_k_planck=P_k_planck,
         P_k_spectral=P_k_spectral,
         # Input tau grid
         tau_evals=tau_evals,
         S_total_bcs=S_total_bcs,
         S_tree_bcs=S_tree_bcs,
         V_CW_bcs=V_CW_bcs,
         )

print(f"  Data saved: s75_alpha_s_dressed_potential.npz")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)
print(f"""
  Gate: S75-C2-ALPHA-S-DRESSED — {gate_verdict}
  {gate_detail}

  n_s            = {ns_final:.8f}  (Planck: {planck_ns} +/- {planck_ns_err})
  n_s tension    = {abs(ns_final - planck_ns) / planck_ns_err:.2f} sigma
  alpha_s        = {alpha_s_final:.8e}  (Planck: {planck_alpha_s} +/- {planck_alpha_s_err})
  alpha_s tension = {alpha_s_tension:.2f} sigma

  Slow-roll:
    eps_H  = {eps_H:.8f}    (shape, M_Pl-independent)
    eps_V  = {eps_V:.4e}  (potential, uses M_Pl/M_KK)
    eta_V  = {eta_V:.4e}
    xi_V^2 = {xi_V_sq:.4e}

  Convention: {convention_used}
  {'(Potential slow-roll VIOLATED: eps_V >> 1)' if eps_V > 0.1 else '(Slow-roll valid)'}

  S68 Bogoliubov: alpha_s = 0 (exact).  CW: alpha_s = {alpha_s_final:.4e} ({'same' if abs(alpha_s_final) < 1e-10 else 'DIFFERENT'}).

  Scheme spread: n_s = {ns_spread:.6f}, alpha_s = {alpha_s_spread:.4e}
  Files: s75_alpha_s_dressed_potential.{{py,npz,png}}
""")

print("=" * 78)
print("DONE")
print("=" * 78)
