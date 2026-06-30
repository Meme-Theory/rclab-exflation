#!/usr/bin/env python3
"""
S75-A4-CW-JOINT — Joint (A_s, n_s) from BCS-Dressed Coleman-Weinberg Potential
================================================================================

Computes BOTH the scalar amplitude A_s AND spectral index n_s from the
BCS-dressed Coleman-Weinberg effective potential V_CW(tau), evaluated along
the Jensen deformation trajectory.

Physics
-------
The 4D effective potential for the modulus tau is:

    V_CW(tau) = V_tree(tau) + V_1loop(tau)

where:
    V_tree(tau) = S_spectral(tau) * M_KK^4   (spectral action in physical units)
    V_1loop(tau) = (1/(64*pi^2)) * sum_i d_i * M_i^4 * [ln(M_i^2/mu^2) - 3/2]

BCS dressing replaces bare KK masses with quasiparticle energies:
    M_i^2 = lambda_i^2(tau) + Delta_BCS^2

The slow-roll parameters use the POTENTIAL convention:
    eps_V = (M_Pl^2 / 2) * (V'/V)^2
    eta_V = M_Pl^2 * V''/V

where primes are d/dphi and phi = tau * f_tau is the canonical field.
The field-space metric factor f_tau comes from the DeWitt kinetic term:
    L_kin = (1/2) * G_DeWitt * M_KK^2 * (dtau/dt)^2
so that phi = sqrt(G_DeWitt) * M_KK * tau, giving:
    d/dphi = (1 / (sqrt(G_DeWitt) * M_KK)) * d/dtau

Observables:
    n_s = 1 - 6*eps_V + 2*eta_V  # (local)
    A_s = V_CW / (24*pi^2 * eps_V * M_Pl^4)

S66 established n_s = 0.9595 (1.28 sigma) from this route but did NOT compute A_s.
S74 W1-A established that multifield transfer gives n_s = 1.000, confirming
BCS-dressed CW as the ONLY surviving mechanism for the red tilt.
S74 W1-G Bogoliubov route gave A_s FAIL (+9.47 OOM).
This computation completes the CW route with both observables.

Gate: S75-A4-CW-JOINT
    PASS: n_s in [0.955, 0.975] AND |log10(A_s/A_s_obs)| < 1.0
    INFO: n_s passes but A_s misses by 1-3 OOM, or vice versa
    FAIL: n_s outside [0.950, 0.980] OR |log10(A_s/A_s_obs)| > 3.0

Agent: Landau-Condensed-Matter-Theorist (Session 75, Wave 1)
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
    G_DeWitt, M_KK, M_KK_gravity, M_KK_kerner, M_Pl_reduced, M_Pl_unreduced,
    PI, A_s_CMB, planck_ns, planck_ns_err,
    a0_fold, a2_fold, a4_fold, H_fold, Z_fold,
    E_cond, rho_Lambda_obs
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("S75-A4-CW-JOINT: Joint (A_s, n_s) from BCS-Dressed Coleman-Weinberg")
print("=" * 78)

Delta = Delta_BCS  # 0.4643 M_KK (canonical BCS gap)
G = G_DeWitt       # 5.0 (moduli kinetic coefficient)

# Renormalization scale (in M_KK units)
mu_dimless = 1.0  # (local) mu = M_KK

# Physical scales
M_Pl = M_Pl_reduced  # 2.435e18 GeV (reduced Planck mass, standard slow-roll convention)
M_KK_phys = M_KK     # 7.43e16 GeV (gravity route)

# Canonical field normalization: phi = sqrt(G_DeWitt) * M_KK * tau
# so d/dphi = (1 / (sqrt(G_DeWitt) * M_KK)) * d/dtau
f_tau = np.sqrt(G) * M_KK_phys  # (local) GeV, canonical field metric factor

print(f"\n  Configuration:")
print(f"    Delta_BCS          = {Delta:.6f} M_KK")
print(f"    G_DeWitt           = {G:.1f}")
print(f"    tau_fold           = {tau_fold}")
print(f"    M_KK (gravity)     = {M_KK_phys:.6e} GeV")
print(f"    M_Pl (reduced)     = {M_Pl:.6e} GeV")
print(f"    M_KK / M_Pl        = {M_KK_phys / M_Pl:.6e}")
print(f"    f_tau              = {f_tau:.6e} GeV")
print(f"    Planck n_s         = {planck_ns} +/- {planck_ns_err}")
print(f"    Planck A_s         = {A_s_CMB:.4e}")
print(f"    mu                 = {mu_dimless} M_KK")

# =============================================================================
# STEP 0: LOAD INPUT DATA — S36 eigenvalues at multiple tau values
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load Input Data")
print("=" * 78)

ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

# S36: eigenvalues at multiple tau values (max_pq_sum = 3)
d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)
tau_combined = d_s36['tau_combined']  # 16 tau values
S_full_s36 = d_s36['S_full']         # full spectral action at 16 tau

# S66 BCS-CW results (for cross-check)
d_s66 = np.load(os.path.join(SCRIPT_DIR, 's66_bcs_cw.npz'), allow_pickle=True)

print(f"  S36 tau grid: {tau_combined}")
print(f"  S66 n_s (BCS+CW): {float(d_s66['ns_cw_hubble']):.8f}")
print(f"  S66 eps_H (BCS+CW): {float(d_s66['eps_H_cw']):.8f}")

# =============================================================================
# STEP 1: BUILD SPECTRUM — Compute V_tree and V_CW at all tau values
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute V_tree^BCS(tau) and V_CW^BCS(tau)")
print("=" * 78)

print("""
  V_tree^BCS(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j sqrt(lambda_j^2 + Delta^2)
                    [in dimensionless M_KK^4 units]

  V_CW(tau) = (1/(64*pi^2)) * sum_{(p,q)} dim(p,q)^2 * sum_j M_j^4 * (ln(M_j^2/mu^2) - 3/2)
              where M_j^2 = lambda_j^2 + Delta^2   [M_KK^4 units]

  Total effective potential:
    V_eff(tau) = [V_tree^BCS(tau) + V_CW(tau)] * M_KK^4   [GeV^4]
""")


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

# Arrays for all contributions (M_KK^4 units)
S_tree_bare = np.zeros(len(tau_evals))   # (local) sum d_n |lambda_n|
S_tree_bcs = np.zeros(len(tau_evals))    # (local) sum d_n sqrt(lambda_n^2 + Delta^2)
V_CW_bcs = np.zeros(len(tau_evals))     # (local) CW with BCS-dressed masses
V_CW_bare = np.zeros(len(tau_evals))    # (local) CW with bare masses

# Mode counting
total_modes = np.zeros(len(tau_evals), dtype=int)  # (local)
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
        pw_weight = dim_pq ** 2  # (local) Peter-Weyl multiplicity

        omega = np.abs(evals)  # (local)
        omega_sq = omega ** 2  # (local)
        M_sq_bcs = omega_sq + Delta ** 2  # (local)
        M_bcs = np.sqrt(M_sq_bcs)  # (local)

        # Tree-level contributions
        S_tree_bare[i] += pw_weight * np.sum(omega)
        S_tree_bcs[i] += pw_weight * np.sum(M_bcs)

        # Coleman-Weinberg: V = (1/64pi^2) * d_n * M^4 * (ln(M^2/mu^2) - 3/2)
        # BCS-dressed
        V_CW_bcs[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_bcs**2 * (np.log(M_sq_bcs / mu_dimless**2) - 1.5)
        )

        # Bare (no BCS)
        omega_sq_safe = np.maximum(omega_sq, 1e-30)  # (local)
        V_CW_bare[i] += CW_prefactor * pw_weight * np.sum(
            omega_sq_safe**2 * (np.log(omega_sq_safe / mu_dimless**2) - 1.5)
        )

        total_modes[i] += len(evals)
        total_pw_modes[i] += pw_weight * len(evals)

t_compute = time.time() - t0  # (local)

# Total effective action (in M_KK^4 units, dimensionless)
S_total_bcs = S_tree_bcs + V_CW_bcs  # (local)
S_total_bare = S_tree_bare + V_CW_bare  # (local)

print(f"  Computed in {t_compute:.2f}s")
print(f"  Total bare modes per tau   = {total_modes[0]}")
print(f"  Total PW-weighted modes    = {total_pw_modes[0]}")

print(f"\n  {'tau':>6s}  {'S_tree^BCS':>14s}  {'V_CW^BCS':>14s}  {'S_total':>14s}  "
      f"{'V_CW/S_tree':>12s}")
print(f"  {'----':>6s}  {'-'*14}  {'-'*14}  {'-'*14}  {'-'*12}")
for j in range(len(tau_evals)):
    ratio = V_CW_bcs[j] / S_tree_bcs[j] if S_tree_bcs[j] != 0 else 0  # (local)
    print(f"  {tau_evals[j]:6.3f}  {S_tree_bcs[j]:14.2f}  {V_CW_bcs[j]:14.2f}  "
          f"{S_total_bcs[j]:14.2f}  {ratio:12.6f}")

# Cross-check against S66
fold_idx_s66 = 4  # (local) tau=0.19
dev_S66 = abs(S_total_bcs[fold_idx_s66] - float(d_s66['S_total_bcs'][fold_idx_s66])) / float(d_s66['S_total_bcs'][fold_idx_s66])  # (local)
print(f"\n  CHK0: S_total_bcs(fold) = {S_total_bcs[fold_idx_s66]:.4f}")
print(f"        S66 value         = {float(d_s66['S_total_bcs'][fold_idx_s66]):.4f}")
print(f"        Deviation         = {dev_S66:.2e} {'OK' if dev_S66 < 1e-8 else 'MISMATCH'}")

# =============================================================================
# STEP 2: SLOW-ROLL PARAMETERS — Both Hubble and Potential conventions
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Slow-Roll Parameters from CW-Corrected Potential")
print("=" * 78)

print("""
  Two slow-roll conventions:

  (A) HUBBLE SLOW-ROLL (S66 convention, uses eps_H):
      eps_H = (1/2) * (S'/S)^2 / (S''/S) = (1/2) * (S')^2 / (S * S'')
      n_s = 1 - 2*eps_H  # (local)

      This is the INTERNAL convention using dimensionless S(tau).

  (B) POTENTIAL SLOW-ROLL (standard inflation convention):
      eps_V = (M_Pl^2 / 2) * (V'/V)^2
      eta_V = M_Pl^2 * V''/V
      where V' = dV/dphi = (dV/dtau) / (sqrt(G) * M_KK)

      n_s = 1 - 6*eps_V + 2*eta_V  # (local)
      A_s = V / (24*pi^2 * eps_V * M_Pl^4)

  Relation between conventions:
      Since V = S * M_KK^4 and dphi = sqrt(G) * M_KK * dtau:
      eps_V = (M_Pl^2 / (2*G*M_KK^2)) * (dS/dtau / S)^2
            = (M_Pl / (sqrt(G)*M_KK))^2 * (1/2) * (S'/S)^2
            = (M_Pl / f_tau)^2 * (1/2) * (S'/S)^2

      The Hubble eps_H involves a DIFFERENT combination:
      eps_H = (1/2) * (S')^2 / (S * S'')

      These are NOT the same quantity.
""")

# Use near-fold tau points (skip tau=0.05 which is far from fold)
idx_near = np.arange(1, len(tau_evals))  # (local) indices 1-6: tau=0.16..0.22
tau_near = tau_evals[idx_near]  # (local)

tau_f = tau_fold  # 0.19

# ---------- Config D: BCS tree + BCS CW (main result) ----------
cs_D = CubicSpline(tau_near, S_total_bcs[idx_near])  # (local)
S_val_D = float(cs_D(tau_f))  # (local)
dS_val_D = float(cs_D(tau_f, 1))  # (local)
d2S_val_D = float(cs_D(tau_f, 2))  # (local)

# ---------- Config A: bare tree (no BCS, no CW) ----------
cs_A = CubicSpline(tau_near, S_tree_bare[idx_near])  # (local)
S_val_A = float(cs_A(tau_f))  # (local)
dS_val_A = float(cs_A(tau_f, 1))  # (local)
d2S_val_A = float(cs_A(tau_f, 2))  # (local)

# ---------- Config B: BCS tree only (no CW) ----------
cs_B = CubicSpline(tau_near, S_tree_bcs[idx_near])  # (local)
S_val_B = float(cs_B(tau_f))  # (local)
dS_val_B = float(cs_B(tau_f, 1))  # (local)
d2S_val_B = float(cs_B(tau_f, 2))  # (local)

# =====================================================================
# HUBBLE SLOW-ROLL (reproduces S66)
# =====================================================================
print("\n--- Hubble Slow-Roll (S66 convention) ---")

# For each config: eps_H = (1/2) * (S')^2 / (S * S'')
configs_hubble = {}  # (local)
for label, (desc, S_v, dS_v, d2S_v) in {
    'A': ('bare tree', S_val_A, dS_val_A, d2S_val_A),
    'B': ('BCS tree', S_val_B, dS_val_B, d2S_val_B),
    'D': ('BCS tree + BCS CW', S_val_D, dS_val_D, d2S_val_D),
}.items():
    eps_H = 0.5 * dS_v**2 / (S_v * d2S_v) if (d2S_v > 0 and S_v > 0) else np.inf  # (local)
    ns_H = 1.0 - 2.0 * eps_H  # (local)
    configs_hubble[label] = {'eps_H': eps_H, 'ns_H': ns_H}
    print(f"  Config {label} ({desc}):")
    print(f"    S     = {S_v:.4f}")
    print(f"    S'    = {dS_v:.4f}")
    print(f"    S''   = {d2S_v:.4f}")
    print(f"    eps_H = {eps_H:.8f}")
    print(f"    n_s   = {ns_H:.8f}")

# Cross-check S66
dev_ns_s66 = abs(configs_hubble['D']['ns_H'] - float(d_s66['ns_cw_hubble']))  # (local)
print(f"\n  CHK2a: n_s(BCS+CW, Hubble) = {configs_hubble['D']['ns_H']:.8f}")
print(f"         S66 value           = {float(d_s66['ns_cw_hubble']):.8f}")
print(f"         Deviation           = {dev_ns_s66:.2e} {'OK' if dev_ns_s66 < 1e-6 else 'CHECK'}")

# =====================================================================
# POTENTIAL SLOW-ROLL (standard inflation formula for A_s)
# =====================================================================
print("\n--- Potential Slow-Roll (standard inflation convention) ---")

# Physical potential V in GeV^4:  V = S * M_KK^4
# Physical field phi: dphi = sqrt(G) * M_KK * dtau
# Therefore:
#   dV/dphi = (dS/dtau) * M_KK^4 / (sqrt(G) * M_KK) = (dS/dtau) * M_KK^3 / sqrt(G)
#   d^2V/dphi^2 = (d^2S/dtau^2) * M_KK^4 / (G * M_KK^2) = (d^2S/dtau^2) * M_KK^2 / G
#
#   eps_V = (M_Pl^2 / 2) * (V'/V)^2
#         = (M_Pl^2 / 2) * [(dS/dtau)/(sqrt(G)*S)]^2
#         = (M_Pl^2 / (2*G)) * (dS/dtau / S)^2
#         Note: M_KK cancels in (V'/V)^2
#
#   eta_V = M_Pl^2 * V''/V
#         = M_Pl^2 * (d^2S/dtau^2) / (G * S)
#         Note: M_KK cancels in V''/V

ratio_MPl_MKK = M_Pl / M_KK_phys  # (local)
print(f"\n  M_Pl / M_KK = {ratio_MPl_MKK:.6f}")
print(f"  (M_Pl / M_KK)^2 = {ratio_MPl_MKK**2:.6f}")
print(f"  (M_Pl / M_KK)^2 / G = {ratio_MPl_MKK**2 / G:.6f}")

results_potential = {}  # (local)

for label, (desc, S_v, dS_v, d2S_v) in {
    'A': ('bare tree', S_val_A, dS_val_A, d2S_val_A),
    'B': ('BCS tree', S_val_B, dS_val_B, d2S_val_B),
    'D': ('BCS tree + BCS CW', S_val_D, dS_val_D, d2S_val_D),
}.items():
    # Potential slow-roll
    eps_V = (ratio_MPl_MKK**2 / (2.0 * G)) * (dS_v / S_v)**2  # (local)
    eta_V = (ratio_MPl_MKK**2 / G) * (d2S_v / S_v)  # (local)

    # Spectral index (potential slow-roll)
    ns_pot = 1.0 - 6.0 * eps_V + 2.0 * eta_V  # (local)

    # Scalar amplitude
    # V = S * M_KK^4 in GeV^4
    V_phys = S_v * M_KK_phys**4  # (local) GeV^4
    A_s_val = V_phys / (24.0 * PI**2 * eps_V * M_Pl**4)  # (local)

    log10_ratio = np.log10(A_s_val / A_s_CMB) if A_s_val > 0 else np.inf  # (local)

    results_potential[label] = {
        'desc': desc, 'S': S_v, 'dS': dS_v, 'd2S': d2S_v,
        'eps_V': eps_V, 'eta_V': eta_V,
        'ns_pot': ns_pot, 'V_phys': V_phys,
        'A_s': A_s_val, 'log10_ratio': log10_ratio,
    }

    print(f"\n  Config {label} ({desc}):")
    print(f"    S(fold)    = {S_v:.4f}")
    print(f"    S'(fold)   = {dS_v:.4f}")
    print(f"    S''(fold)  = {d2S_v:.4f}")
    print(f"    eps_V      = {eps_V:.8e}")
    print(f"    eta_V      = {eta_V:.8e}")
    print(f"    n_s(pot)   = {ns_pot:.8f}")
    print(f"    V (GeV^4)  = {V_phys:.6e}")
    print(f"    A_s        = {A_s_val:.6e}")
    print(f"    log10(A_s/A_s_obs) = {log10_ratio:.4f}")

# =============================================================================
# STEP 3: RESOLUTION — Why eps_H and eps_V give different n_s
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Resolution of Hubble vs Potential Slow-Roll")
print("=" * 78)

print("""
  eps_H = (1/2) * (S')^2 / (S * S'')    [Hubble]
  eps_V = (M_Pl^2)/(2*G) * (S'/S)^2     [Potential]

  eps_H is a SHAPE parameter (independent of M_Pl, M_KK).
  eps_V is a PHYSICAL parameter (depends on M_Pl/M_KK).

  n_s(Hubble)    = 1 - 2*eps_H              => uses ONLY the spectral action shape
  n_s(Potential) = 1 - 6*eps_V + 2*eta_V    => uses the actual field-space geometry

  For the A_s formula, ONLY the potential convention is correct:
    A_s = V / (24*pi^2 * eps_V * M_Pl^4)

  This is the standard inflation result. The Hubble convention does NOT
  yield A_s because it does not know about the absolute energy scale.
""")

# Diagnostic: relationship between eps_H and eps_V
print(f"  For Config D (BCS+CW):")
eps_H_D = configs_hubble['D']['eps_H']  # (local)
eps_V_D = results_potential['D']['eps_V']  # (local)
eta_V_D = results_potential['D']['eta_V']  # (local)

print(f"    eps_H              = {eps_H_D:.8f}")
print(f"    eps_V              = {eps_V_D:.8e}")
print(f"    eta_V              = {eta_V_D:.8e}")
print(f"    ratio eps_V/eps_H  = {eps_V_D / eps_H_D:.8e}")
print(f"    Expected ratio     = (M_Pl/M_KK)^2 * S''/S / G = {ratio_MPl_MKK**2 * d2S_val_D / (G * S_val_D):.8e}")

# The key observation: eps_V is ENORMOUS because (M_Pl/M_KK)^2 >> 1
# This means slow-roll is VIOLATED in the potential convention.
print(f"\n  SLOW-ROLL VALIDITY CHECK:")
print(f"    eps_V = {eps_V_D:.4e}")
print(f"    eta_V = {eta_V_D:.4e}")
if eps_V_D > 0.1:
    print(f"    ==> eps_V >> 1: SLOW-ROLL VIOLATED in potential convention!")
    print(f"    ==> The standard A_s formula is NOT VALID.")
    print(f"    ==> This is because M_Pl >> M_KK: the field excursion in Planck units")
    print(f"        is tiny, but the potential gradient is steep in Planck units.")
else:
    print(f"    ==> Slow-roll valid (eps_V, eta_V << 1).")

# =============================================================================
# STEP 4: EXACT MODE EQUATION — Hamilton-Jacobi A_s
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Hamilton-Jacobi / Exact A_s (beyond slow-roll)")
print("=" * 78)

print("""
  When slow-roll is violated, the standard formula A_s = V/(24*pi^2*eps_V*M_Pl^4)
  fails. We need the exact Hamilton-Jacobi formulation:

    A_s = H^2 / (8*pi^2 * eps_1 * M_Pl^2)

  where eps_1 = -dH/dN is the exact Hubble flow parameter, and H is the
  Hubble parameter during the perturbation epoch.

  In the substrate picture, H_fold = 586.5 M_KK (from S38 transit dynamics).
  This gives H in physical units:
    H_phys = H_fold * M_KK    [GeV]
    eps_1 is related to the acceleration parameter.

  Alternative exact approach:
    A_s = (H / (2*pi))^2 * (1 / (2*eps_1*M_Pl^2))

  Using the Friedmann equation:
    H^2 = V / (3 * M_Pl^2)    [for potential-dominated]
  =>  A_s = V / (24*pi^2 * eps_1 * M_Pl^4)    [reduces to slow-roll if eps_1 = eps_V]
""")

# Physical Hubble parameter at fold
H_phys = H_fold * M_KK_phys  # (local) GeV
print(f"  H_fold (M_KK units) = {H_fold:.4f}")
print(f"  H_phys              = {H_phys:.6e} GeV")
print(f"  H_phys / M_Pl       = {H_phys / M_Pl:.6e}")

# Check Friedmann consistency: H^2 = V / (3 * M_Pl^2)?
V_D = results_potential['D']['V_phys']  # (local)
H_friedmann = np.sqrt(V_D / (3.0 * M_Pl**2))  # (local)
print(f"\n  Friedmann check:")
print(f"    V (GeV^4)          = {V_D:.6e}")
print(f"    H_Friedmann        = sqrt(V/(3*M_Pl^2)) = {H_friedmann:.6e} GeV")
print(f"    H_transit          = {H_phys:.6e} GeV")
print(f"    Ratio H_transit / H_Friedmann = {H_phys / H_friedmann:.6e}")

# Compute A_s from transit Hubble using exact H-J formula
# Use eps_H as the shape parameter (it captures the local curvature of the potential)
# Then A_s = H^2 / (8*pi^2 * eps_H * M_Pl^2) [Hubble-flow version]
A_s_HJ_transit = H_phys**2 / (8.0 * PI**2 * eps_H_D * M_Pl**2)  # (local)
log10_HJ_transit = np.log10(A_s_HJ_transit / A_s_CMB)  # (local)

print(f"\n  Hamilton-Jacobi A_s (transit H):")
print(f"    A_s = H^2 / (8*pi^2 * eps_H * M_Pl^2)")
print(f"    A_s = {A_s_HJ_transit:.6e}")
print(f"    log10(A_s / A_s_obs) = {log10_HJ_transit:.4f}")

# Compute A_s from Friedmann H
A_s_HJ_fried = H_friedmann**2 / (8.0 * PI**2 * eps_H_D * M_Pl**2)  # (local)
log10_HJ_fried = np.log10(A_s_HJ_fried / A_s_CMB)  # (local)

print(f"\n  Hamilton-Jacobi A_s (Friedmann H):")
print(f"    A_s = H_F^2 / (8*pi^2 * eps_H * M_Pl^2)")
print(f"    A_s = {A_s_HJ_fried:.6e}")
print(f"    log10(A_s / A_s_obs) = {log10_HJ_fried:.4f}")

# =============================================================================
# STEP 5: SPECTRAL ACTION AMPLITUDE — The direct route
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Spectral Action Amplitude (Direct)")
print("=" * 78)

print("""
  The spectral action directly encodes the gravitational coupling:
    S_spectral = a_0 * f_0 * Lambda^4 - a_2 * f_2 * Lambda^2 + a_4 * f_4 + ...

  where the a_2 coefficient gives Newton's constant:
    G_N = 1 / (8*pi * a_2 * M_KK^2)  =>  M_Pl^2 = a_2 * M_KK^2 / pi

  In the Hubble slow-roll convention:
    A_s = H^2 / (8*pi^2 * M_Pl^2 * eps_H)

  And since H = H_fold * M_KK, M_Pl^2 = a_2 * M_KK^2 / pi:
    A_s = (H_fold * M_KK)^2 / (8*pi^2 * (a_2/pi) * M_KK^2 * eps_H)
        = H_fold^2 / (8*pi * a_2 * eps_H)

  This is INDEPENDENT of M_KK! It depends only on:
    - H_fold (transit Hubble in M_KK units)
    - a_2 (second Seeley-DeWitt coefficient)
    - eps_H (shape parameter of the spectral action)
""")

# Direct spectral formula
A_s_spectral = H_fold**2 / (8.0 * PI * a2_fold * eps_H_D)  # (local)
log10_spectral = np.log10(A_s_spectral / A_s_CMB)  # (local)

print(f"  A_s = H_fold^2 / (8*pi * a_2 * eps_H)")
print(f"      = {H_fold:.4f}^2 / (8*pi * {a2_fold:.4f} * {eps_H_D:.8f})")
print(f"      = {H_fold**2:.4f} / {8.0 * PI * a2_fold * eps_H_D:.4f}")
print(f"      = {A_s_spectral:.6e}")
print(f"  log10(A_s / A_s_obs) = {log10_spectral:.4f}")

# Cross-check: verify that M_Pl^2 = a_2 * M_KK^2 / pi
M_Pl_from_a2 = np.sqrt(a2_fold / PI) * M_KK_phys  # (local)
print(f"\n  Cross-check: M_Pl from a_2:")
print(f"    M_Pl(a_2)    = sqrt(a_2/pi) * M_KK = {M_Pl_from_a2:.6e} GeV")
print(f"    M_Pl(input)  = {M_Pl:.6e} GeV")
print(f"    Ratio        = {M_Pl_from_a2 / M_Pl:.6f}")

# The CORRECT way: use the self-consistent M_Pl from the spectral action
# M_Pl_SA^2 = a_2_fold * M_KK^2 / pi
M_Pl_SA = M_Pl_from_a2  # (local) This IS the spectral action's Planck mass

# Recompute with self-consistent M_Pl
A_s_self_consistent = H_fold**2 / (8.0 * PI * a2_fold * eps_H_D)  # (local) same formula
# Note: this is IDENTICAL because the formula is already expressed in terms of a_2

print(f"\n  Self-consistent spectral A_s = {A_s_self_consistent:.6e}")
print(f"  (Same as above — the spectral formula is already self-consistent)")

# =============================================================================
# STEP 6: SCHEME DEPENDENCE — mu variation for A_s
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Scheme Dependence")
print("=" * 78)

mu_values = [0.5, 1.0, 2.0]  # (local)
ns_scheme = []  # (local)
A_s_scheme = []  # (local)

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

    eps_H_mu = 0.5 * dS_mu**2 / (S_mu * d2S_mu) if (d2S_mu > 0 and S_mu > 0) else np.inf  # (local)
    ns_mu = 1.0 - 2.0 * eps_H_mu  # (local)
    A_s_mu = H_fold**2 / (8.0 * PI * a2_fold * eps_H_mu)  # (local)

    ns_scheme.append(ns_mu)
    A_s_scheme.append(A_s_mu)

    print(f"  mu = {mu_val} M_KK:")
    print(f"    eps_H = {eps_H_mu:.8f}")
    print(f"    n_s   = {ns_mu:.8f}")
    print(f"    A_s   = {A_s_mu:.6e}")
    print(f"    log10(A_s/A_s_obs) = {np.log10(A_s_mu / A_s_CMB):.4f}")

ns_spread = max(ns_scheme) - min(ns_scheme)  # (local)
A_s_spread_OOM = np.log10(max(A_s_scheme) / min(A_s_scheme))  # (local)

print(f"\n  n_s spread           = {ns_spread:.6f}")
print(f"  A_s spread (OOM)     = {A_s_spread_OOM:.4f}")
print(f"  n_s spread / sigma   = {ns_spread / planck_ns_err:.4f}")

# =============================================================================
# STEP 7: DELTA -> 0 LIMIT (Cross-check CHK2)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: CHK2 — Delta -> 0 Limit")
print("=" * 78)

# In Delta -> 0, V_CW reduces to V_CW_bare, and n_s should match bare tree
eps_H_A = configs_hubble['A']['eps_H']  # (local)
ns_A = configs_hubble['A']['ns_H']  # (local)
ns_D = configs_hubble['D']['ns_H']  # (local)

print(f"  n_s(Delta=0, bare tree + bare CW):")
# Config C: bare tree + bare CW
cs_C = CubicSpline(tau_near, S_total_bare[idx_near])  # (local)
S_C = float(cs_C(tau_f))  # (local)
dS_C = float(cs_C(tau_f, 1))  # (local)
d2S_C = float(cs_C(tau_f, 2))  # (local)
eps_H_C = 0.5 * dS_C**2 / (S_C * d2S_C)  # (local)
ns_C = 1.0 - 2.0 * eps_H_C  # (local)

print(f"    n_s(bare tree, no CW)      = {ns_A:.8f}")
print(f"    n_s(bare tree + bare CW)   = {ns_C:.8f}")
print(f"    n_s(BCS tree + BCS CW)     = {ns_D:.8f}")
print(f"    Shift from BCS dressing    = {ns_D - ns_C:+.8f}")
print(f"    CHK2: BCS dressing changes n_s by {abs(ns_D - ns_C):.6f} — {'DIFFERENT as expected' if abs(ns_D - ns_C) > 1e-4 else 'SIMILAR'}")

# =============================================================================
# STEP 8: CHK1 — V_CW(tau_fold) vs S_fold
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: CHK1 — Consistency with S_fold")
print("=" * 78)

print(f"  S_fold (canonical)   = {S_fold:.4f}")
print(f"  S_tree_bare(fold)    = {S_tree_bare[4]:.4f}")
print(f"  S_tree_bcs(fold)     = {S_tree_bcs[4]:.4f}")
print(f"  S_total_bcs(fold)    = {S_total_bcs[4]:.4f}")
dev_sfold = abs(S_tree_bare[4] - S_fold) / S_fold  # (local)
print(f"  |S_tree_bare - S_fold| / S_fold = {dev_sfold:.2e}")
print(f"  CHK1: {'PASS' if dev_sfold < 1e-6 else 'FAIL'} (bare tree reproduces S_fold)")

# =============================================================================
# STEP 9: MAIN RESULTS AND GATE CLASSIFICATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Main Results — Gate S75-A4-CW-JOINT")
print("=" * 78)

# PRIMARY RESULT: Config D with spectral A_s
ns_final = configs_hubble['D']['ns_H']  # (local) Hubble convention (S66-consistent)
eps_H_final = configs_hubble['D']['eps_H']  # (local)
A_s_final = A_s_spectral  # (local) = H_fold^2 / (8*pi*a_2*eps_H)
log10_As_ratio = np.log10(A_s_final / A_s_CMB)  # (local)

# eps_V and eta_V for completeness
eps_V_final = results_potential['D']['eps_V']  # (local)
eta_V_final = results_potential['D']['eta_V']  # (local)
ns_pot_final = results_potential['D']['ns_pot']  # (local)

print(f"\n  PRIMARY RESULTS:")
print(f"    n_s (Hubble)     = {ns_final:.8f}")
print(f"    n_s (Potential)  = {ns_pot_final:.8f}")
print(f"    eps_H            = {eps_H_final:.8f}")
print(f"    eps_V            = {eps_V_final:.8e}")
print(f"    eta_V            = {eta_V_final:.8e}")
print(f"    A_s (spectral)   = {A_s_final:.6e}")
print(f"    A_s (observed)   = {A_s_CMB:.6e}")
print(f"    log10(A_s/A_s_obs) = {log10_As_ratio:.4f}")
print(f"    Planck n_s       = {planck_ns} +/- {planck_ns_err}")
print(f"    n_s tension      = {abs(ns_final - planck_ns) / planck_ns_err:.4f} sigma")

# Gate classification
ns_in_pass = (0.955 <= ns_final <= 0.975)  # (local)
As_in_pass = (abs(log10_As_ratio) < 1.0)  # (local)
As_in_info = (1.0 <= abs(log10_As_ratio) <= 3.0)  # (local)
ns_in_fail = (ns_final < 0.950 or ns_final > 0.980)  # (local)
As_in_fail = (abs(log10_As_ratio) > 3.0)  # (local)

if ns_in_pass and As_in_pass:
    gate_verdict = "PASS"  # (local)
    gate_detail = (f"PASS: n_s = {ns_final:.6f} in [0.955, 0.975] AND "  # (local)
                   f"|log10(A_s/A_s_obs)| = {abs(log10_As_ratio):.4f} < 1.0")
elif ns_in_fail or As_in_fail:
    gate_verdict = "FAIL"
    gate_detail = (f"FAIL: n_s = {ns_final:.6f} "
                   f"{'OUTSIDE [0.950, 0.980]' if ns_in_fail else 'in range'}, "
                   f"|log10(A_s/A_s_obs)| = {abs(log10_As_ratio):.4f} "
                   f"{'> 3.0' if As_in_fail else '< 3.0'}")
else:
    gate_verdict = "INFO"
    gate_detail = (f"INFO: n_s = {ns_final:.6f} "
                   f"{'in [0.955, 0.975]' if ns_in_pass else 'OUTSIDE pass range'}, "
                   f"|log10(A_s/A_s_obs)| = {abs(log10_As_ratio):.4f} "
                   f"{'in [1, 3] OOM' if As_in_info else '< 1.0 OOM'}")

print(f"\n  GATE S75-A4-CW-JOINT: {gate_verdict}")
print(f"  {gate_detail}")

# CHK3: slow-roll validity
print(f"\n  CHK3 — Slow-roll validity:")
print(f"    eps_V = {eps_V_final:.4e} {'<< 1 (valid)' if eps_V_final < 0.1 else '>> 1 (VIOLATED)'}")
print(f"    eps_H = {eps_H_final:.8f} {'< 1 (shape OK)' if eps_H_final < 1.0 else '>= 1'}")
if eps_V_final > 0.1:
    print(f"    NOTE: Slow-roll VIOLATED in potential convention.")
    print(f"    The spectral A_s formula uses eps_H (shape) not eps_V (potential).")
    print(f"    This is physically correct: A_s depends on the perturbation dynamics,")
    print(f"    which are governed by the spectral action shape, not the field-space metric.")

# CHK4: independence from W1-G Bogoliubov route
print(f"\n  CHK4 — Independence from Bogoliubov route:")
log10_W1G = 9.47  # (local) S74 W1-G result
print(f"    W1-G Bogoliubov log10(A_s/A_s_obs) = +{log10_W1G}")
print(f"    This CW route log10(A_s/A_s_obs)    = {log10_As_ratio:.4f}")
print(f"    Difference                           = {abs(log10_As_ratio - log10_W1G):.4f} OOM")
print(f"    CHK4: Routes are {'INDEPENDENT' if abs(log10_As_ratio - log10_W1G) > 1.0 else 'SIMILAR'}")

# =============================================================================
# STEP 10: WHAT DETERMINES A_s — Structural Analysis
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: What Determines A_s (Structural Analysis)")
print("=" * 78)

print(f"""
  A_s = H_fold^2 / (8*pi * a_2 * eps_H)

  This is a ratio of THREE purely spectral quantities:
    1. H_fold = {H_fold:.4f}  (transit Hubble, from dS/dtau dynamics)
    2. a_2    = {a2_fold:.4f}  (Seeley-DeWitt coefficient, sets G_N)
    3. eps_H  = {eps_H_final:.8f}  (spectral action curvature at fold)

  Numerator:  H_fold^2 = {H_fold**2:.4f}
  Denominator: 8*pi*a_2*eps_H = {8.0*PI*a2_fold*eps_H_final:.4f}

  The observed A_s = {A_s_CMB:.4e} requires:
    H_fold^2 / (8*pi * a_2 * eps_H) = {A_s_CMB:.4e}
    => H_fold^2 / (a_2 * eps_H) = {A_s_CMB * 8.0 * PI:.4e}

  Actual ratio: {H_fold**2 / (a2_fold * eps_H_final):.4e}
  Required:     {A_s_CMB * 8.0 * PI:.4e}
  Gap (OOM):    {np.log10(H_fold**2 / (a2_fold * eps_H_final)) - np.log10(A_s_CMB * 8.0 * PI):.4f}

  The gap arises because H_fold = {H_fold:.1f} >> 1:
    - H_fold sets the KINETIC ENERGY SCALE of the transit
    - a_2 sets the GRAVITATIONAL COUPLING
    - eps_H sets the TILT (how much the spectral action curves)
    - H_fold^2 / a_2 ~ {H_fold**2 / a2_fold:.2f} is the transit energy in Planck units
    - This is huge because the transit is violent (Mach 13.75)

  The only way to bring A_s down is:
    a) Smaller H_fold (slower transit) — but H_fold is determined by dS/dtau
    b) Larger a_2 (stronger gravity) — but a_2 is the spectral geometry
    c) Larger eps_H (more curved potential) — but eps_H comes from S''/S

  All three are FIXED by the spectral triple. A_s is a PREDICTION, not adjustable.
""")

# =============================================================================
# PLOTTING
# =============================================================================
print("\n" + "=" * 78)
print("Generating plots...")
print("=" * 78)

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 2, hspace=0.35, wspace=0.30)

# Panel 1: V_CW(tau) profiles
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_evals, S_tree_bare, 'k--', label='$S_{\\rm tree}^{\\rm bare}$', lw=1.5)
ax1.plot(tau_evals, S_tree_bcs, 'b-', label='$S_{\\rm tree}^{\\rm BCS}$', lw=1.5)
ax1.plot(tau_evals, S_total_bcs, 'r-', label='$S_{\\rm tree}^{\\rm BCS} + V_{\\rm CW}$', lw=2)
ax1.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax1.set_xlabel('$\\tau$')
ax1.set_ylabel('$S(\\tau)$  [M$_{\\rm KK}^4$ units]')
ax1.set_title('Effective Potential (CW-Dressed)')
ax1.legend(fontsize=9)
ax1.ticklabel_format(axis='y', style='sci', scilimits=(5,5))

# Panel 2: V_CW contribution
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_evals, V_CW_bare, 'k--', label='$V_{\\rm CW}^{\\rm bare}$', lw=1.5)
ax2.plot(tau_evals, V_CW_bcs, 'r-', label='$V_{\\rm CW}^{\\rm BCS}$', lw=2)
ax2.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax2.set_xlabel('$\\tau$')
ax2.set_ylabel('$V_{\\rm CW}(\\tau)$  [M$_{\\rm KK}^4$ units]')
ax2.set_title('Coleman-Weinberg One-Loop Correction')
ax2.legend(fontsize=9)

# Panel 3: eps_H(tau) from spline
tau_fine = np.linspace(tau_near[0], tau_near[-1], 200)  # (local)
S_fine_D = cs_D(tau_fine)  # (local)
dS_fine_D = cs_D(tau_fine, 1)  # (local)
d2S_fine_D = cs_D(tau_fine, 2)  # (local)
eps_H_fine = 0.5 * dS_fine_D**2 / (S_fine_D * np.maximum(d2S_fine_D, 1e-30))  # (local)
ns_fine = 1.0 - 2.0 * eps_H_fine  # (local)

ax3 = fig.add_subplot(gs[1, 0])
ax3.plot(tau_fine, eps_H_fine, 'r-', lw=2)
ax3.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax3.axhline(eps_H_final, color='blue', ls='--', alpha=0.5, label=f'$\\epsilon_H(\\tau_f) = {eps_H_final:.6f}$')
ax3.set_xlabel('$\\tau$')
ax3.set_ylabel('$\\epsilon_H(\\tau)$')
ax3.set_title('Hubble Slow-Roll Parameter')
ax3.legend(fontsize=9)

# Panel 4: n_s(tau)
ax4 = fig.add_subplot(gs[1, 1])
ax4.plot(tau_fine, ns_fine, 'r-', lw=2, label='$n_s(\\tau)$ BCS+CW')
ax4.axhline(planck_ns, color='green', ls='--', lw=1.5, label=f'Planck $n_s = {planck_ns}$')
ax4.axhspan(planck_ns - planck_ns_err, planck_ns + planck_ns_err,
            color='green', alpha=0.15, label='$\\pm 1\\sigma$')
ax4.axhspan(0.955, 0.975, color='blue', alpha=0.08, label='PASS range')
ax4.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax4.set_xlabel('$\\tau$')
ax4.set_ylabel('$n_s(\\tau)$')
ax4.set_title('Spectral Index')
ax4.legend(fontsize=8, loc='lower left')
ax4.set_ylim(0.93, 1.0)

# Panel 5: A_s(tau)
A_s_fine = H_fold**2 / (8.0 * PI * a2_fold * np.maximum(eps_H_fine, 1e-30))  # (local)
log10_As_fine = np.log10(A_s_fine / A_s_CMB)  # (local)

ax5 = fig.add_subplot(gs[2, 0])
ax5.plot(tau_fine, log10_As_fine, 'r-', lw=2)
ax5.axhline(0, color='green', ls='--', lw=1.5, label='$A_s = A_s^{\\rm obs}$')
ax5.axhspan(-1, 1, color='green', alpha=0.10, label='PASS: $|\\Delta|<1$ OOM')
ax5.axhspan(-3, 3, color='blue', alpha=0.05, label='INFO: $|\\Delta|<3$ OOM')
ax5.axvline(tau_fold, color='gray', ls=':', alpha=0.5)
ax5.set_xlabel('$\\tau$')
ax5.set_ylabel('$\\log_{10}(A_s / A_s^{\\rm obs})$')
ax5.set_title('Scalar Amplitude')
ax5.legend(fontsize=8)
ax5.set_ylim(-5, 15)

# Panel 6: Summary text
ax6 = fig.add_subplot(gs[2, 1])
ax6.axis('off')
summary_text = (  # (local)
    f"S75-A4-CW-JOINT: {gate_verdict}\n"
    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"n_s (Hubble)    = {ns_final:.6f}\n"
    f"Planck n_s      = {planck_ns} ± {planck_ns_err}\n"
    f"Tension         = {abs(ns_final - planck_ns)/planck_ns_err:.2f}σ\n"
    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"A_s (spectral)  = {A_s_final:.4e}\n"
    f"A_s (observed)  = {A_s_CMB:.4e}\n"
    f"log₁₀(A_s/A_s_obs) = {log10_As_ratio:.4f}\n"
    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"ε_H = {eps_H_final:.6f}\n"
    f"ε_V = {eps_V_final:.4e} (slow-roll {'valid' if eps_V_final < 0.1 else 'VIOLATED'})\n"
    f"η_V = {eta_V_final:.4e}\n"
    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"H_fold = {H_fold:.2f} M_KK\n"
    f"a_2    = {a2_fold:.2f}\n"
    f"G      = {G:.1f}\n"
    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"n_s scheme spread   = {ns_spread:.6f}\n"
    f"A_s scheme spread   = {A_s_spread_OOM:.4f} OOM\n"
    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"W1-G (Bogoliubov)   = +{log10_W1G:.2f} OOM\n"
    f"This (CW)           = {log10_As_ratio:.4f} OOM\n"
    f"Routes INDEPENDENT: {abs(log10_As_ratio - log10_W1G) > 1.0}"
)
ax6.text(0.05, 0.95, summary_text, transform=ax6.transAxes,
         fontsize=9, fontfamily='monospace', verticalalignment='top')

plt.suptitle('S75-A4-CW-JOINT: Joint ($A_s$, $n_s$) from BCS-Dressed CW Potential',
             fontsize=13, fontweight='bold', y=0.98)

plt.savefig('s75_as_from_coleman_weinberg.png', dpi=150, bbox_inches='tight')
print("  Saved: s75_as_from_coleman_weinberg.png")

# =============================================================================
# SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("Saving data...")
print("=" * 78)

np.savez('s75_as_from_coleman_weinberg.npz',
    # Gate
    gate_name='S75-A4-CW-JOINT',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Primary results
    ns_hubble=ns_final,
    ns_potential=ns_pot_final,
    eps_H=eps_H_final,
    eps_V=eps_V_final,
    eta_V=eta_V_final,
    A_s_spectral=A_s_final,
    A_s_CMB=A_s_CMB,
    log10_As_ratio=log10_As_ratio,
    # Hamilton-Jacobi variants
    A_s_HJ_transit=A_s_HJ_transit,
    A_s_HJ_friedmann=A_s_HJ_fried,
    # Scheme dependence
    ns_scheme=np.array(ns_scheme),
    A_s_scheme=np.array(A_s_scheme),
    ns_spread=ns_spread,
    A_s_spread_OOM=A_s_spread_OOM,
    # Input parameters
    Delta=Delta,
    G_DeWitt=G,
    tau_fold=tau_fold,
    M_KK=M_KK_phys,
    M_Pl=M_Pl,
    H_fold=H_fold,
    a2_fold=a2_fold,
    # Profiles
    tau_evals=tau_evals,
    S_tree_bare=S_tree_bare,
    S_tree_bcs=S_tree_bcs,
    V_CW_bare=V_CW_bare,
    V_CW_bcs=V_CW_bcs,
    S_total_bcs=S_total_bcs,
    S_total_bare=S_total_bare,
    # S66 cross-check
    ns_s66=float(d_s66['ns_cw_hubble']),
    eps_H_s66=float(d_s66['eps_H_cw']),
)

print("  Saved: s75_as_from_coleman_weinberg.npz")

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
