#!/usr/bin/env python3
"""
BCS-CW-SELFCONSISTENT-66 (W5-B) — Coleman-Weinberg on BCS-Dressed Tree
========================================================================

Computes the Coleman-Weinberg one-loop effective potential V_CW(tau) for
the BCS-dressed KK spectrum, and extracts the corrected spectral index n_s.

Physics
-------
The 4D effective potential for the modulus tau receives a one-loop Coleman-Weinberg
correction from each massive KK mode.  For a real scalar field of mass M, the
standard CW result (dimensional regularization, MSbar) is:

    V_CW = (1 / (64 * pi^2)) * sum_n d_n * M_n^4 * (ln(M_n^2 / mu^2) - 3/2)

where:
  M_n^2(tau) = lambda_n^2(tau) + Delta^2     (BCS-dressed KK mass squared)
  lambda_n(tau) = eigenvalues of D_K at Jensen parameter tau
  Delta = 0.464 M_KK  (BCS gap from OES, canonical_constants)
  d_n = dim(p,q)^2  (Peter-Weyl degeneracy for spectral action)
  mu = M_KK  (renormalization scale set at the KK threshold)

The tree-level spectral action is:
    S_tree(tau) = sum_n d_n * |lambda_n(tau)|

with the BCS dressing:
    S_tree^BCS(tau) = sum_n d_n * sqrt(lambda_n^2(tau) + Delta^2)

The total effective action including CW is:
    S_total(tau) = S_tree^BCS(tau) + V_CW(tau)

The slow-roll parameter:
    epsilon_H = (1/2) * (S_total' / S_total)^2 / (S_total'' / S_total)

where primes denote d/dtau.  Then n_s = 1 - 2*epsilon_H.

Key distinction from S65
-------------------------
S65 computed S_1loop = (1/2) * sum dim(p,q) * sum_j ln(lambda_j^2 + Delta^2).
That is a 0+1D functional determinant (log-det of D_K^2 + Delta^2).

THIS computation uses the 4D Coleman-Weinberg potential, which is the proper
one-loop correction when the KK modes propagate in 4D.  The CW potential
has the M^4 * ln(M^2) structure from integrating over 4D loop momenta.

The CW potential scales as M_n^4, so it is UV-sensitive: high-lying KK modes
contribute MORE than low-lying ones.  This is the opposite of the log-det,
where low-lying modes dominate.

Renormalization-scale dependence
---------------------------------
V_CW depends on mu.  The physical content is in the mu-independent combination
when renormalization conditions are imposed.  Here we fix mu = M_KK and
explore mu = {0.5, 1.0, 2.0} M_KK to assess scheme dependence.

Gate: BCS-CW-SELFCONSISTENT-66
  PASS: n_s^{CW} > 0.9607 (within 1 sigma of Planck)
  FAIL: n_s^{CW} < 0.9557 (CW moves n_s AWAY from Planck)
  INFO: 0.9557 < n_s^{CW} < 0.9607 (partial improvement)

Agent: Landau-Condensed-Matter-Theorist (Session 66, Wave 5)
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
    tau_fold, Delta_0_OES, S_fold, dS_fold, d2S_fold,
    G_DeWitt, M_KK, PI
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("BCS-CW-SELFCONSISTENT-66 (W5-B): Coleman-Weinberg on BCS-Dressed Tree")
print("=" * 78)

Delta = Delta_0_OES   # 0.464 M_KK
G = G_DeWitt          # 5.0 (moduli kinetic coefficient)
# planck_ns = 0.9649  # S72: now imported from canonical_constants
planck_sigma = planck_ns_err  # S72: was 0.0042, now imported from canonical_constants

# Renormalization scales (in M_KK units, so mu_dimless = mu / M_KK)
mu_central = 1.0      # mu = M_KK  # (local)
mu_low = 0.5  # (local)
mu_high = 2.0  # (local)

print(f"\n  Delta (BCS gap)      = {Delta:.6f} M_KK")
print(f"  G_DeWitt             = {G:.1f}")
print(f"  tau_fold             = {tau_fold}")
print(f"  Planck n_s           = {planck_ns} +/- {planck_sigma}")
print(f"  Renormalization mu   = {mu_central} M_KK (central)")

# =============================================================================
# STEP 0: LOAD INPUT DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load Input Data")
print("=" * 78)

ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

# S36: eigenvalues at 7 tau values
d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)
tau_combined = d_s36['tau_combined']  # 16 tau values
S_full_s36 = d_s36['S_full']         # full spectral action at 16 tau

# S65 BCS-dressed results (for cross-check)
d_bcs = np.load(os.path.join(SCRIPT_DIR, 's65_bcs_dressed_sa.npz'),
                allow_pickle=True)

# S63 one-loop results (for cross-check)
d_1loop_ns = np.load(os.path.join(SCRIPT_DIR, 's63_oneloop_ns.npz'),
                     allow_pickle=True)

# Reference values from prior computations
ns_tree_s63 = float(d_1loop_ns['ns_tree'])         # 0.9567
eps_tree_s63 = float(d_1loop_ns['epsilon_tree'])    # 0.02163
ns_s65_bcs_1loop = 0.95901811  # From S65 BCS+1-loop (Hubble convention)  # (local)

print(f"  S63 tree:     n_s = {ns_tree_s63:.6f}, eps_H = {eps_tree_s63:.6f}")
print(f"  S65 BCS+1L:   n_s = {ns_s65_bcs_1loop:.6f}")

# =============================================================================
# STEP 1: BUILD SPECTRUM AND COMPUTE ALL CONTRIBUTIONS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute S_tree^BCS(tau) and V_CW(tau) at All tau")
print("=" * 78)

print("""
  Tree-level BCS-dressed spectral action:
    S_tree^BCS(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j sqrt(lambda_j^2(tau) + Delta^2)

  Coleman-Weinberg one-loop (4D, MSbar):
    V_CW(tau) = (1/(64*pi^2)) * sum_{(p,q)} dim(p,q)^2 * sum_j M_j^4 * (ln(M_j^2/mu^2) - 3/2)
    where M_j^2 = lambda_j^2(tau) + Delta^2

  Note: We use dim(p,q)^2 as the degeneracy — this matches the Peter-Weyl weight
  used in the spectral action.  Each KK mode appears dim(p,q)^2 times in the
  partition function (dim(p,q) from the representation, times dim(p,q) from the
  conjugate representation in the heat kernel trace).

  The CW contribution uses the SAME degeneracy as S_tree because both arise
  from the same set of 4D fields: each KK mode of the internal Dirac operator
  gives a 4D field with that multiplicity.
""")


def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# Sectors with max_pq_sum = 3
sectors = []
for p in range(4):
    for q in range(4):
        if p + q <= 3:
            sectors.append((p, q))

# tau values where eigenvalues are stored
tau_evals = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])

# Arrays for all contributions
S_tree_bare = np.zeros(len(tau_evals))      # sum d_n |lambda_n|
S_tree_bcs = np.zeros(len(tau_evals))       # sum d_n sqrt(lambda_n^2 + Delta^2)
V_CW_bare = np.zeros(len(tau_evals))        # CW with bare masses
V_CW_bcs = np.zeros(len(tau_evals))         # CW with BCS-dressed masses (MAIN)
V_CW_bcs_mu_low = np.zeros(len(tau_evals))  # CW at mu = 0.5 M_KK
V_CW_bcs_mu_high = np.zeros(len(tau_evals)) # CW at mu = 2.0 M_KK

# Also compute log-det for comparison with S65
S_logdet_bcs = np.zeros(len(tau_evals))     # (1/2) sum dim(p,q) * ln(M^2)

# Mode counting
total_modes = np.zeros(len(tau_evals), dtype=int)
total_pw_modes = np.zeros(len(tau_evals), dtype=int)

CW_prefactor = 1.0 / (64.0 * PI**2)

t0 = time.time()

for i, tau in enumerate(tau_evals):
    for (p, q) in sectors:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key not in d_s36:
            print(f"  WARNING: {key} not found")
            continue

        evals = d_s36[key]
        dim_pq = su3_dim(p, q)
        pw_weight = dim_pq ** 2  # Peter-Weyl multiplicity for tree-level AND CW

        omega = np.abs(evals)
        omega_sq = omega ** 2
        M_sq_bcs = omega_sq + Delta ** 2
        M_bcs = np.sqrt(M_sq_bcs)

        # --- Tree-level ---
        S_tree_bare[i] += pw_weight * np.sum(omega)
        S_tree_bcs[i] += pw_weight * np.sum(M_bcs)

        # --- Coleman-Weinberg: V = (1/64pi^2) * d_n * M^4 * (ln(M^2/mu^2) - 3/2) ---
        # Bare (no BCS): M^2 = omega^2, guard against omega=0
        omega_sq_safe = np.maximum(omega_sq, 1e-30)
        V_CW_bare[i] += CW_prefactor * pw_weight * np.sum(
            omega_sq_safe**2 * (np.log(omega_sq_safe / mu_central**2) - 1.5)
        )

        # BCS-dressed: M^2 = omega^2 + Delta^2
        V_CW_bcs[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_bcs**2 * (np.log(M_sq_bcs / mu_central**2) - 1.5)
        )

        # BCS at mu_low and mu_high (scheme dependence)
        V_CW_bcs_mu_low[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_bcs**2 * (np.log(M_sq_bcs / mu_low**2) - 1.5)
        )
        V_CW_bcs_mu_high[i] += CW_prefactor * pw_weight * np.sum(
            M_sq_bcs**2 * (np.log(M_sq_bcs / mu_high**2) - 1.5)
        )

        # Log-det for comparison (S65 convention: (1/2) * dim * ln(M^2))
        S_logdet_bcs[i] += 0.5 * dim_pq * np.sum(np.log(M_sq_bcs))

        total_modes[i] += len(evals)
        total_pw_modes[i] += pw_weight * len(evals)

t_compute = time.time() - t0
print(f"  Computed in {t_compute:.2f}s")
print(f"  Total bare modes per tau   = {total_modes[0]}")
print(f"  Total PW-weighted modes    = {total_pw_modes[0]}")

# Cross-check: S_tree_bare should match S36 S_full
print(f"\n  Cross-check S_tree^bare vs S36:")
for j, tau in enumerate(tau_evals):
    idx_s36 = np.argmin(np.abs(tau_combined - tau))
    dev = abs(S_tree_bare[j] - S_full_s36[idx_s36]) / S_full_s36[idx_s36]
    if j == 4:  # fold
        print(f"    tau={tau:.3f}: S_tree={S_tree_bare[j]:.2f}, S36={S_full_s36[idx_s36]:.2f}, "
              f"dev={dev:.2e} {'OK' if dev < 1e-8 else 'MISMATCH'}")

# Cross-check: S_tree_bcs should match S65
print(f"\n  Cross-check S_tree^BCS vs S65:")
tau_s65 = d_bcs['tau_S36']
S_bcs_s65 = d_bcs['S_BCS']
for j, tau in enumerate(tau_evals):
    idx_s65 = np.argmin(np.abs(tau_s65 - tau))
    if abs(tau_s65[idx_s65] - tau) < 0.001:
        dev = abs(S_tree_bcs[j] - S_bcs_s65[idx_s65]) / S_bcs_s65[idx_s65]
        if j == 4:  # fold
            print(f"    tau={tau:.3f}: S_BCS={S_tree_bcs[j]:.2f}, S65={S_bcs_s65[idx_s65]:.2f}, "
                  f"dev={dev:.2e} {'OK' if dev < 1e-8 else 'MISMATCH'}")

# =============================================================================
# STEP 2: DISPLAY CW PROFILES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Coleman-Weinberg Profile V_CW(tau)")
print("=" * 78)

# Total effective action: S_total = S_tree^BCS + V_CW^BCS
S_total_bcs = S_tree_bcs + V_CW_bcs
S_total_bcs_mu_low = S_tree_bcs + V_CW_bcs_mu_low
S_total_bcs_mu_high = S_tree_bcs + V_CW_bcs_mu_high

# Also compute: bare tree + bare CW (for reference)
S_total_bare = S_tree_bare + V_CW_bare

# Ratios
ratio_CW_tree = V_CW_bcs / S_tree_bcs

print(f"\n  {'tau':>6s}  {'S_tree^BCS':>14s}  {'V_CW^BCS':>14s}  {'V_CW/S_tree':>12s}  "
      f"{'S_total':>14s}  {'V_CW(mu=0.5)':>14s}  {'V_CW(mu=2)':>14s}")
print(f"  {'----':>6s}  {'-'*14}  {'-'*14}  {'-'*12}  "
      f"{'-'*14}  {'-'*14}  {'-'*14}")
for j in range(len(tau_evals)):
    print(f"  {tau_evals[j]:6.3f}  {S_tree_bcs[j]:14.2f}  {V_CW_bcs[j]:14.2f}  "
          f"{ratio_CW_tree[j]:12.6f}  {S_total_bcs[j]:14.2f}  "
          f"{V_CW_bcs_mu_low[j]:14.2f}  {V_CW_bcs_mu_high[j]:14.2f}")

# BCS shift in CW
delta_VCW = V_CW_bcs - V_CW_bare
print(f"\n  BCS correction to CW at fold (tau=0.19):")
print(f"    V_CW^bare(fold) = {V_CW_bare[4]:.4f}")
print(f"    V_CW^BCS(fold)  = {V_CW_bcs[4]:.4f}")
print(f"    delta_V_CW      = {delta_VCW[4]:+.4f}")
print(f"    delta_V_CW / V_CW^bare = {delta_VCW[4]/V_CW_bare[4]:.6f}" if abs(V_CW_bare[4]) > 1e-30 else "")

# =============================================================================
# STEP 3: SLOW-ROLL PARAMETERS FROM S_total = S_tree^BCS + V_CW
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Slow-Roll Parameters from CW-Corrected Action")
print("=" * 78)

print("""
  epsilon_H = (1/2) * (S')^2 / (S * S'')
  n_s = 1 - 2 * epsilon_H    (Hubble slow-roll convention)  # (local)

  We compute for 5 configurations:
    A: bare tree (no BCS, no CW) — baseline
    B: BCS tree (no CW) — S65 W1-A
    C: bare tree + bare CW
    D: BCS tree + BCS CW (mu=M_KK) — THIS RESULT
    E: BCS tree + BCS CW (mu=0.5 M_KK) — scheme check
    F: BCS tree + BCS CW (mu=2.0 M_KK) — scheme check
""")

# Use near-fold tau points for spline (skip tau=0.05)
idx_near = np.arange(1, len(tau_evals))  # indices 1-6: tau=0.16..0.22
tau_near = tau_evals[idx_near]

configs = {
    'A': ('bare tree', S_tree_bare[idx_near]),
    'B': ('BCS tree', S_tree_bcs[idx_near]),
    'C': ('bare tree + bare CW', S_total_bare[idx_near]),
    'D': ('BCS tree + BCS CW [mu=M_KK]', S_total_bcs[idx_near]),
    'E': ('BCS tree + BCS CW [mu=0.5 M_KK]', S_total_bcs_mu_low[idx_near]),
    'F': ('BCS tree + BCS CW [mu=2.0 M_KK]', S_total_bcs_mu_high[idx_near]),
}

results = {}
tau_f = tau_fold  # 0.19

for label, (desc, S_arr) in configs.items():
    cs = CubicSpline(tau_near, S_arr)
    S_val = float(cs(tau_f))
    dS_val = float(cs(tau_f, 1))
    d2S_val = float(cs(tau_f, 2))

    # Hubble slow-roll: epsilon_H = (1/2) * (S')^2 / (S * S'')
    if d2S_val > 0 and S_val > 0:
        eps_H = 0.5 * dS_val ** 2 / (S_val * d2S_val)
    else:
        eps_H = np.inf
    ns_hubble = 1.0 - 2.0 * eps_H

    # Potential slow-roll (with G_DeWitt normalization)
    eps_V = 0.5 * (dS_val / S_val) ** 2 / G
    eta_V = d2S_val / (S_val * G)
    eta_H = eta_V / (1.0 - eps_V / 3.0)
    ns_three = 1.0 - 2.0 * eps_H - eta_H

    results[label] = {
        'desc': desc,
        'S': S_val, 'dS': dS_val, 'd2S': d2S_val,
        'eps_H': eps_H, 'eps_V': eps_V, 'eta_V': eta_V, 'eta_H': eta_H,
        'ns_hubble': ns_hubble, 'ns_three': ns_three,
        'spline': cs,
    }

    print(f"\n  Config {label}: {desc}")
    print(f"    S(fold)      = {S_val:14.4f}")
    print(f"    S'(fold)     = {dS_val:14.4f}")
    print(f"    S''(fold)    = {d2S_val:14.4f}")
    print(f"    eps_H        = {eps_H:.8f}")
    print(f"    n_s(Hubble)  = {ns_hubble:.8f}")
    print(f"    n_s(3-param) = {ns_three:.8f}")

# =============================================================================
# STEP 4: CROSS-CHECKS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Cross-Checks")
print("=" * 78)

# Config A should reproduce S63 tree-level
dev_eps_A = abs(results['A']['eps_H'] - eps_tree_s63) / eps_tree_s63
print(f"\n  Config A (bare tree) vs S63 tree:")
print(f"    eps_H: {results['A']['eps_H']:.8f} vs {eps_tree_s63:.8f} (dev={dev_eps_A:.4e})")
print(f"    n_s:   {results['A']['ns_hubble']:.8f} vs {ns_tree_s63:.8f}")

# Config B should reproduce S65 BCS tree
eps_bcs_tree_s65 = float(d_bcs['eps_H_bcs'][3])  # index 3 = tau=0.19
ns_bcs_tree_s65 = float(d_bcs['ns_bcs'][3])
dev_eps_B = abs(results['B']['eps_H'] - eps_bcs_tree_s65) / eps_bcs_tree_s65
print(f"\n  Config B (BCS tree) vs S65 BCS tree:")
print(f"    eps_H: {results['B']['eps_H']:.8f} vs {eps_bcs_tree_s65:.8f} (dev={dev_eps_B:.4e})")

# =============================================================================
# STEP 5: MAIN RESULT — CW-CORRECTED n_s
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Main Result — BCS-CW n_s")
print("=" * 78)

# Config D is the main result
eps_H_cw = results['D']['eps_H']
ns_cw = results['D']['ns_hubble']
ns_cw_three = results['D']['ns_three']

print(f"\n  PRIMARY RESULT (Hubble slow-roll):")
print(f"    eps_H^{{BCS,CW}}    = {eps_H_cw:.8f}")
print(f"    n_s^{{BCS,CW}}     = {ns_cw:.8f}")
print(f"    Planck n_s        = {planck_ns} +/- {planck_sigma}")
print(f"    Tension           = {abs(ns_cw - planck_ns)/planck_sigma:.4f} sigma")

print(f"\n  SECONDARY (three-parameter formula):")
print(f"    n_s^{{BCS,CW,3p}}  = {ns_cw_three:.8f}")

# Shift decomposition relative to bare tree
ns_A = results['A']['ns_hubble']
ns_B = results['B']['ns_hubble']
ns_D = results['D']['ns_hubble']

delta_ns_bcs = ns_B - ns_A           # BCS shift alone
delta_ns_cw_total = ns_D - ns_A      # Total shift (BCS + CW)
delta_ns_cw_only = ns_D - ns_B       # CW shift (on top of BCS)

print(f"\n  Shift decomposition (Hubble convention):")
print(f"    n_s(bare tree)           = {ns_A:.8f}")
print(f"    n_s(BCS tree)            = {ns_B:.8f}   delta = {delta_ns_bcs:+.8f}")
print(f"    n_s(BCS + CW)            = {ns_D:.8f}   delta = {delta_ns_cw_total:+.8f}")
print(f"    CW-only shift            =               delta = {delta_ns_cw_only:+.8f}")

# Compare with S65 log-det approach
print(f"\n  Comparison with S65 log-det approach:")
print(f"    S65 BCS+logdet n_s       = {ns_s65_bcs_1loop:.8f}")
print(f"    This BCS+CW n_s          = {ns_cw:.8f}")
print(f"    Difference               = {ns_cw - ns_s65_bcs_1loop:+.8f}")
print(f"    CW vs log-det structures are DIFFERENT: CW ~ M^4*ln(M^2), log-det ~ ln(M^2)")

# =============================================================================
# STEP 6: SCHEME DEPENDENCE (mu variation)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Renormalization Scale Dependence")
print("=" * 78)

ns_mu_low = results['E']['ns_hubble']
ns_mu_high = results['F']['ns_hubble']
ns_spread = max(ns_mu_low, ns_cw, ns_mu_high) - min(ns_mu_low, ns_cw, ns_mu_high)

print(f"\n  mu = 0.5  M_KK:  n_s = {ns_mu_low:.8f}  (eps_H = {results['E']['eps_H']:.8f})")
print(f"  mu = 1.0  M_KK:  n_s = {ns_cw:.8f}  (eps_H = {results['D']['eps_H']:.8f})")
print(f"  mu = 2.0  M_KK:  n_s = {ns_mu_high:.8f}  (eps_H = {results['F']['eps_H']:.8f})")
print(f"  Spread in n_s             = {ns_spread:.8f}")
print(f"  Spread / Planck sigma     = {ns_spread/planck_sigma:.4f}")

# =============================================================================
# STEP 7: ANALYTIC DECOMPOSITION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Analytic Decomposition — alpha/beta/gamma")
print("=" * 78)

# CW modification of S_tree^BCS: S_total = S_tree^BCS * (1 + V_CW/S_tree^BCS)
# epsilon_total / epsilon_tree = (1+beta)^2 / [(1+alpha)(1+gamma)]
# where alpha = delta(S)/S, beta = delta(S')/S', gamma = delta(S'')/S''

# Delta relative to bare tree (Config A)
S_A = results['A']['S']
dS_A = results['A']['dS']
d2S_A = results['A']['d2S']

S_D = results['D']['S']
dS_D = results['D']['dS']
d2S_D = results['D']['d2S']

alpha_total = (S_D - S_A) / S_A
beta_total = (dS_D - dS_A) / dS_A
gamma_total = (d2S_D - d2S_A) / d2S_A

mod_factor = (1 + beta_total)**2 / ((1 + alpha_total) * (1 + gamma_total))
first_order = 1.0 + 2 * beta_total - alpha_total - gamma_total

actual_ratio = results['D']['eps_H'] / results['A']['eps_H']

print(f"\n  Total modification (BCS+CW vs bare tree):")
print(f"    alpha = delta(S)/S     = {alpha_total:+.8f}")
print(f"    beta  = delta(S')/S'   = {beta_total:+.8f}")
print(f"    gamma = delta(S'')/S'' = {gamma_total:+.8f}")
print(f"    Mod factor (exact):      {mod_factor:.8f}")
print(f"    Mod factor (1st order):  {first_order:.8f}")
print(f"    eps_D/eps_A (actual):    {actual_ratio:.8f}")

# CW-only modification (relative to BCS tree, Config B)
S_B = results['B']['S']
dS_B = results['B']['dS']
d2S_B = results['B']['d2S']

alpha_cw = (S_D - S_B) / S_B
beta_cw = (dS_D - dS_B) / dS_B
gamma_cw = (d2S_D - d2S_B) / d2S_B

print(f"\n  CW-only modification (BCS+CW vs BCS tree):")
print(f"    alpha_CW = {alpha_cw:+.8f}")
print(f"    beta_CW  = {beta_cw:+.8f}")
print(f"    gamma_CW = {gamma_cw:+.8f}")

# Physical interpretation
print(f"\n  Physical interpretation:")
print(f"    The CW correction V_CW ~ M^4 * ln(M^2) is POSITIVE and LARGE.")
print(f"    It adds to S_total, increasing the denominator in epsilon_H = S'^2/(2*S*S'').")
print(f"    The key question is whether it increases S' and S'' proportionally,")
print(f"    or whether it changes their ratio (i.e., whether alpha, beta, gamma differ).")
print(f"    beta > gamma => eps_H increases => n_s decreases (red tilt)")
print(f"    beta < gamma => eps_H decreases => n_s increases (toward Planck)")

# =============================================================================
# STEP 8: UNCERTAINTY ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Uncertainty Analysis")
print("=" * 78)

# Source 1: Interpolation (spline) uncertainty — drop points
tau_test1 = tau_near[[0, 2, 3, 4, 5]]  # drop tau=0.17
tau_test2 = tau_near[[0, 1, 3, 4, 5]]  # drop tau=0.18
S_D_near = S_total_bcs[idx_near]

eps_variants = []
for name, tau_sub, S_sub in [
    ('full 6-pt', tau_near, S_D_near),
    ('drop 0.17', tau_test1, S_D_near[[0, 2, 3, 4, 5]]),
    ('drop 0.18', tau_test2, S_D_near[[0, 1, 3, 4, 5]]),
]:
    cs_test = CubicSpline(tau_sub, S_sub)
    S_t = float(cs_test(tau_f))
    dS_t = float(cs_test(tau_f, 1))
    d2S_t = float(cs_test(tau_f, 2))
    eps_t = 0.5 * dS_t**2 / (S_t * d2S_t) if d2S_t > 0 else np.inf
    ns_t = 1.0 - 2.0 * eps_t
    eps_variants.append(eps_t)
    print(f"  {name:>15s}: eps_H = {eps_t:.8f}, n_s = {ns_t:.8f}")

sigma_interp = (max(eps_variants) - min(eps_variants)) / 2.0
sigma_ns_interp = 2.0 * sigma_interp

# Source 2: BCS gap uncertainty (Delta = 0.464 +/- 0.01 M_KK)
Delta_lo = 0.454  # (local)
Delta_hi = 0.474  # (local)
eps_delta_variants = []

for Delta_test in [Delta_lo, Delta, Delta_hi]:
    S_eff_test = np.zeros(len(tau_near))
    for j_near, j_all in enumerate(idx_near):
        tau = tau_evals[j_all]
        S_tree_test = 0.0  # (local)
        V_CW_test = 0.0  # (local)
        for (p, q) in sectors:
            key = f'evals_tau{tau:.3f}_{p}_{q}'
            if key not in d_s36:
                continue
            evals = d_s36[key]
            dim_pq = su3_dim(p, q)
            pw = dim_pq ** 2
            omega = np.abs(evals)
            M_sq = omega**2 + Delta_test**2
            M_val = np.sqrt(M_sq)
            S_tree_test += pw * np.sum(M_val)
            V_CW_test += CW_prefactor * pw * np.sum(
                M_sq**2 * (np.log(M_sq / mu_central**2) - 1.5)
            )
        S_eff_test[j_near] = S_tree_test + V_CW_test

    cs_test = CubicSpline(tau_near, S_eff_test)
    S_t = float(cs_test(tau_f))
    dS_t = float(cs_test(tau_f, 1))
    d2S_t = float(cs_test(tau_f, 2))
    eps_t = 0.5 * dS_t**2 / (S_t * d2S_t) if d2S_t > 0 else np.inf
    eps_delta_variants.append(eps_t)

sigma_delta = (max(eps_delta_variants) - min(eps_delta_variants)) / 2.0
sigma_ns_delta = 2.0 * sigma_delta

print(f"\n  Delta sensitivity:")
print(f"    Delta={Delta_lo}: eps_H = {eps_delta_variants[0]:.8f}")
print(f"    Delta={Delta}:  eps_H = {eps_delta_variants[1]:.8f}")
print(f"    Delta={Delta_hi}: eps_H = {eps_delta_variants[2]:.8f}")
print(f"    sigma(eps_H) = {sigma_delta:.8f}")

# Source 3: Scheme dependence
sigma_scheme = ns_spread / 2.0  # half the mu-spread as sigma estimate
sigma_eps_scheme = sigma_scheme / 2.0

# Source 4: Truncation (max_pq_sum = 3)
# Higher PW levels contribute ~5% to derivatives (S65 estimate)
sigma_trunc = 0.05 * abs(results['D']['eps_H'] - results['A']['eps_H'])
sigma_ns_trunc = 2.0 * sigma_trunc

# Total
sigma_eps_total = np.sqrt(sigma_interp**2 + sigma_delta**2 +
                          sigma_eps_scheme**2 + sigma_trunc**2)
sigma_ns_total = 2.0 * sigma_eps_total

print(f"\n  Error budget:")
print(f"    Interpolation:  sigma(eps_H) = {sigma_interp:.8f}  =>  sigma(n_s) = {sigma_ns_interp:.8f}")
print(f"    BCS gap:        sigma(eps_H) = {sigma_delta:.8f}  =>  sigma(n_s) = {sigma_ns_delta:.8f}")
print(f"    Scheme (mu):    sigma(eps_H) = {sigma_eps_scheme:.8f}  =>  sigma(n_s) = {sigma_scheme:.8f}")
print(f"    Truncation:     sigma(eps_H) = {sigma_trunc:.8f}  =>  sigma(n_s) = {sigma_ns_trunc:.8f}")
print(f"    Total:          sigma(eps_H) = {sigma_eps_total:.8f}")
print(f"    Total:          sigma(n_s)   = {sigma_ns_total:.8f}")

# =============================================================================
# STEP 9: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: GATE VERDICT — BCS-CW-SELFCONSISTENT-66")
print("=" * 78)

# Pre-registered criterion:
#   PASS: n_s^{CW} > 0.9607 (within 1 sigma of Planck)
#   FAIL: n_s^{CW} < 0.9557 (CW moves n_s AWAY from Planck)
#   INFO: 0.9557 < n_s^{CW} < 0.9607 (partial improvement)

if ns_cw > 0.9607:
    verdict = "PASS"
    detail_reason = f"n_s = {ns_cw:.6f} > 0.9607 (within 1 sigma of Planck)"
elif ns_cw < 0.9557:
    verdict = "FAIL"
    detail_reason = f"n_s = {ns_cw:.6f} < 0.9557 (CW moves n_s AWAY from Planck)"
else:
    verdict = "INFO"
    detail_reason = f"n_s = {ns_cw:.6f} in [0.9557, 0.9607] (partial improvement)"

tension_sigma = abs(ns_cw - planck_ns) / planck_sigma

# Direction check
improved_over_bare = abs(ns_cw - planck_ns) < abs(ns_A - planck_ns)
improved_over_bcs = abs(ns_cw - planck_ns) < abs(ns_B - planck_ns)
improved_over_s65 = abs(ns_cw - planck_ns) < abs(ns_s65_bcs_1loop - planck_ns)

gate_detail = (
    f"n_s^{{BCS,CW}} = {ns_cw:.6f}. "
    f"Planck tension = {tension_sigma:.2f} sigma. "
    f"eps_H = {eps_H_cw:.6f}. "
    f"BCS shift: delta(n_s) = {delta_ns_bcs:+.6f}. "
    f"CW-only shift: delta(n_s) = {delta_ns_cw_only:+.6f}. "
    f"Total shift: delta(n_s) = {delta_ns_cw_total:+.6f}. "
    f"sigma(n_s) = {sigma_ns_total:.6f}. "
    f"Scheme spread = {ns_spread:.6f}. "
    f"Improved over bare: {improved_over_bare}. "
    f"Improved over S65 BCS+logdet: {improved_over_s65}."
)

print(f"\n  GATE: BCS-CW-SELFCONSISTENT-66")
print(f"  CRITERION:")
print(f"    PASS: n_s > 0.9607")
print(f"    FAIL: n_s < 0.9557")
print(f"    INFO: 0.9557 < n_s < 0.9607")
print(f"")
print(f"  n_s^{{BCS,CW}} = {ns_cw:.6f}")
print(f"  Planck tension  = {tension_sigma:.2f} sigma")
print(f"  Direction vs bare tree:  {'TOWARD' if improved_over_bare else 'AWAY FROM'} Planck")
print(f"  Direction vs BCS tree:   {'TOWARD' if improved_over_bcs else 'AWAY FROM'} Planck")
print(f"  Direction vs S65 logdet: {'TOWARD' if improved_over_s65 else 'AWAY FROM'} Planck")
print(f"")
print(f"  VERDICT: {verdict}")
print(f"  {detail_reason}")

# =============================================================================
# STEP 10: SUMMARY TABLE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 10: Summary Table")
print("=" * 78)

print(f"\n  {'Configuration':>42s}  {'eps_H':>12s}  {'n_s(H)':>12s}  {'Tension':>10s}")
print(f"  {'-'*42}  {'-'*12}  {'-'*12}  {'-'*10}")
for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    r = results[label]
    sig = abs(r['ns_hubble'] - planck_ns) / planck_sigma
    print(f"  {label}: {r['desc']:>38s}  {r['eps_H']:12.8f}  {r['ns_hubble']:12.8f}  {sig:8.2f}sig")
print(f"  {'S65: BCS+logdet':>42s}  {'---':>12s}  {ns_s65_bcs_1loop:12.8f}  "
      f"{abs(ns_s65_bcs_1loop-planck_ns)/planck_sigma:8.2f}sig")
print(f"  {'Planck 2018':>42s}  {'---':>12s}  {planck_ns:12.4f}  {'0.00sig':>10s}")

# =============================================================================
# STEP 11: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 11: Saving")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's66_bcs_cw.npz')
np.savez(
    outpath,
    # Gate
    gate_name='BCS-CW-SELFCONSISTENT-66',
    gate_verdict=verdict,
    gate_detail=gate_detail,

    # Main results
    ns_cw_hubble=ns_cw,
    ns_cw_three=ns_cw_three,
    eps_H_cw=eps_H_cw,
    planck_tension_sigma=tension_sigma,

    # All configurations at fold
    eps_H_A=results['A']['eps_H'],
    eps_H_B=results['B']['eps_H'],
    eps_H_C=results['C']['eps_H'],
    eps_H_D=results['D']['eps_H'],
    eps_H_E=results['E']['eps_H'],
    eps_H_F=results['F']['eps_H'],

    ns_A=results['A']['ns_hubble'],
    ns_B=results['B']['ns_hubble'],
    ns_C=results['C']['ns_hubble'],
    ns_D=results['D']['ns_hubble'],
    ns_E=results['E']['ns_hubble'],
    ns_F=results['F']['ns_hubble'],

    # Shift decomposition
    delta_ns_bcs=delta_ns_bcs,
    delta_ns_cw_only=delta_ns_cw_only,
    delta_ns_cw_total=delta_ns_cw_total,

    # Analytic decomposition (total: BCS+CW vs bare)
    alpha_total=alpha_total,
    beta_total=beta_total,
    gamma_total=gamma_total,
    mod_factor=mod_factor,

    # CW-only decomposition
    alpha_cw=alpha_cw,
    beta_cw=beta_cw,
    gamma_cw=gamma_cw,

    # Scheme dependence
    ns_mu_low=ns_mu_low,
    ns_mu_high=ns_mu_high,
    ns_spread=ns_spread,

    # Error budget
    sigma_interp=sigma_interp,
    sigma_delta=sigma_delta,
    sigma_eps_scheme=sigma_eps_scheme,
    sigma_trunc=sigma_trunc,
    sigma_eps_total=sigma_eps_total,
    sigma_ns_total=sigma_ns_total,

    # Profiles
    tau_evals=tau_evals,
    S_tree_bare=S_tree_bare,
    S_tree_bcs=S_tree_bcs,
    V_CW_bare=V_CW_bare,
    V_CW_bcs=V_CW_bcs,
    V_CW_bcs_mu_low=V_CW_bcs_mu_low,
    V_CW_bcs_mu_high=V_CW_bcs_mu_high,
    S_total_bcs=S_total_bcs,
    S_total_bare=S_total_bare,

    # Reference
    Delta=Delta,
    tau_fold=tau_f,
    G_DeWitt=G,
    mu_central=mu_central,
    mu_low=mu_low,
    mu_high=mu_high,
    planck_ns=planck_ns,
    planck_sigma=planck_sigma,
    improved_over_bare=improved_over_bare,
    improved_over_bcs=improved_over_bcs,
    improved_over_s65=improved_over_s65,
)

print(f"  Saved: {outpath}")

# =============================================================================
# STEP 12: PLOT
# =============================================================================
print("\n  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.40, wspace=0.35)
fig.suptitle(f'BCS-CW-SELFCONSISTENT-66: Coleman-Weinberg on BCS-Dressed Tree [{verdict}]',
             fontsize=14, fontweight='bold')

# --- Panel (a): Effective action profiles ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_near, S_tree_bare[idx_near] / 1e3, 'b-o', ms=4,
         label=r'$S_\mathrm{tree}^\mathrm{bare}$ (A)')
ax1.plot(tau_near, S_tree_bcs[idx_near] / 1e3, 'r-^', ms=4,
         label=r'$S_\mathrm{tree}^\mathrm{BCS}$ (B)')
ax1.plot(tau_near, S_total_bcs[idx_near] / 1e3, 'k-D', ms=5, lw=2,
         label=r'$S_\mathrm{tree}^\mathrm{BCS}+V_\mathrm{CW}$ (D)')
ax1.axvline(x=0.19, color='gray', ls='--', alpha=0.5, label='fold')
ax1.set_xlabel(r'$\tau$', fontsize=11)
ax1.set_ylabel(r'$S \times 10^{-3}$', fontsize=11)
ax1.set_title('(a) Effective Action Profiles', fontsize=12)
ax1.legend(fontsize=8)

# --- Panel (b): Coleman-Weinberg contribution ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_near, V_CW_bare[idx_near], 'b-o', ms=4, label=r'$V_\mathrm{CW}^\mathrm{bare}$')
ax2.plot(tau_near, V_CW_bcs[idx_near], 'r-^', ms=4, label=r'$V_\mathrm{CW}^\mathrm{BCS}$')
ax2.plot(tau_near, V_CW_bcs_mu_low[idx_near], 'g--s', ms=3, alpha=0.7,
         label=r'$V_\mathrm{CW}^\mathrm{BCS}(\mu=0.5)$')
ax2.plot(tau_near, V_CW_bcs_mu_high[idx_near], 'm--v', ms=3, alpha=0.7,
         label=r'$V_\mathrm{CW}^\mathrm{BCS}(\mu=2.0)$')
ax2.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax2.set_xlabel(r'$\tau$', fontsize=11)
ax2.set_ylabel(r'$V_\mathrm{CW}$ ($M_\mathrm{KK}$ units)', fontsize=11)
ax2.set_title('(b) Coleman-Weinberg Potential', fontsize=12)
ax2.legend(fontsize=7)

# --- Panel (c): V_CW / S_tree ratio ---
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(tau_near, V_CW_bcs[idx_near] / S_tree_bcs[idx_near], 'k-D', ms=5, lw=2)
ax3.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax3.set_xlabel(r'$\tau$', fontsize=11)
ax3.set_ylabel(r'$V_\mathrm{CW} / S_\mathrm{tree}$', fontsize=11)
ax3.set_title(r'(c) $V_\mathrm{CW}/S_\mathrm{tree}$ Ratio', fontsize=12)
ax3.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

# --- Panel (d): epsilon_H profiles ---
ax4 = fig.add_subplot(gs[1, 0])
tau_scan = np.linspace(0.16, 0.22, 100)
for label, color, ls, lw in [('A', 'blue', '-', 1), ('B', 'red', '-', 1),
                               ('D', 'black', '-', 2.5)]:
    cs = results[label]['spline']
    eps_scan = np.zeros(len(tau_scan))
    for j, tau in enumerate(tau_scan):
        S_t = float(cs(tau))
        dS_t = float(cs(tau, 1))
        d2S_t = float(cs(tau, 2))
        if d2S_t > 0 and S_t > 0:
            eps_scan[j] = 0.5 * dS_t**2 / (S_t * d2S_t)
        else:
            eps_scan[j] = np.nan
    ax4.plot(tau_scan, eps_scan, color=color, ls=ls, lw=lw,
             label=f'{label}: {results[label]["desc"][:25]}')
ax4.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax4.set_xlabel(r'$\tau$', fontsize=11)
ax4.set_ylabel(r'$\epsilon_H$', fontsize=11)
ax4.set_title(r'(d) Slow-Roll Parameter $\epsilon_H(\tau)$', fontsize=12)
ax4.legend(fontsize=7)

# --- Panel (e): n_s comparison bar chart ---
ax5 = fig.add_subplot(gs[1, 1])
bar_labels = ['A: bare\ntree', 'B: BCS\ntree', 'D: BCS\n+CW',
              'S65:\nBCS+logdet', 'Planck']
bar_vals = [ns_A, ns_B, ns_cw, ns_s65_bcs_1loop, planck_ns]
bar_colors = ['#4477AA', '#CC6677', '#228833', '#AA3377', '#CCBB44']
bars = ax5.bar(range(len(bar_vals)), bar_vals, color=bar_colors, edgecolor='black', linewidth=0.8)
ax5.axhline(y=planck_ns, color='gold', ls='-', lw=2, alpha=0.8, label=f'Planck {planck_ns}')
ax5.axhspan(planck_ns - planck_sigma, planck_ns + planck_sigma,
            alpha=0.15, color='gold', label=r'$\pm 1\sigma$')  # (local)
ax5.set_xticks(range(len(bar_labels)))
ax5.set_xticklabels(bar_labels, fontsize=8)
ax5.set_ylabel(r'$n_s$', fontsize=11)
ax5.set_title('(e) Spectral Index Comparison', fontsize=12)
ax5.legend(fontsize=8, loc='lower right')
ax5.set_ylim(min(bar_vals) - 0.005, max(bar_vals) + 0.005)

# --- Panel (f): Scheme dependence ---
ax6 = fig.add_subplot(gs[1, 2])
mu_vals = [0.5, 1.0, 2.0]
ns_mu_vals = [ns_mu_low, ns_cw, ns_mu_high]
ax6.plot(mu_vals, ns_mu_vals, 'ko-', ms=8, lw=2)
ax6.axhline(y=planck_ns, color='gold', ls='-', lw=2, alpha=0.8)
ax6.axhspan(planck_ns - planck_sigma, planck_ns + planck_sigma,
            alpha=0.15, color='gold')  # (local)
ax6.set_xlabel(r'$\mu / M_\mathrm{KK}$', fontsize=11)
ax6.set_ylabel(r'$n_s$', fontsize=11)
ax6.set_title(r'(f) Scheme Dependence ($\mu$ variation)', fontsize=12)

# --- Panel (g): alpha/beta/gamma ---
ax7 = fig.add_subplot(gs[2, 0])
abg_labels = [r'$\alpha$', r'$\beta$', r'$\gamma$']
abg_total = [alpha_total, beta_total, gamma_total]
abg_cw = [alpha_cw, beta_cw, gamma_cw]
x = np.arange(3)
w = 0.35  # (local)
ax7.bar(x - w/2, abg_total, w, label='Total (BCS+CW vs bare)', color='#228833', edgecolor='black')
ax7.bar(x + w/2, abg_cw, w, label='CW-only (vs BCS tree)', color='#4477AA', edgecolor='black')
ax7.set_xticks(x)
ax7.set_xticklabels(abg_labels, fontsize=12)
ax7.set_ylabel('Fractional shift', fontsize=11)
ax7.set_title(r'(g) $\alpha/\beta/\gamma$ Decomposition', fontsize=12)
ax7.legend(fontsize=8)
ax7.axhline(y=0, color='gray', lw=0.5)

# --- Panel (h): Error budget ---
ax8 = fig.add_subplot(gs[2, 1])
err_labels = ['Interp', 'BCS gap', 'Scheme', 'Trunc', 'Total']
err_vals = [sigma_ns_interp, sigma_ns_delta, sigma_scheme, sigma_ns_trunc, sigma_ns_total]
colors_err = ['#4477AA', '#CC6677', '#AA3377', '#44AA99', '#000000']
ax8.barh(range(len(err_labels)), err_vals, color=colors_err, edgecolor='black')
ax8.set_yticks(range(len(err_labels)))
ax8.set_yticklabels(err_labels, fontsize=10)
ax8.set_xlabel(r'$\sigma(n_s)$', fontsize=11)
ax8.set_title('(h) Error Budget', fontsize=12)

# --- Panel (i): Physical summary text ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')
summary_text = (
    f"GATE: BCS-CW-SELFCONSISTENT-66\n"
    f"VERDICT: {verdict}\n\n"
    f"$n_s^{{\\mathrm{{BCS,CW}}}} = {ns_cw:.6f}$\n"
    f"Planck tension: {tension_sigma:.2f}$\\sigma$\n\n"
    f"Shifts from bare tree:\n"
    f"  BCS:  $\\delta n_s = {delta_ns_bcs:+.6f}$\n"
    f"  CW:   $\\delta n_s = {delta_ns_cw_only:+.6f}$\n"
    f"  Total: $\\delta n_s = {delta_ns_cw_total:+.6f}$\n\n"
    f"$\\sigma(n_s) = {sigma_ns_total:.6f}$\n"
    f"Scheme spread: {ns_spread:.6f}\n\n"
    f"Improved vs bare: {improved_over_bare}\n"
    f"Improved vs S65: {improved_over_s65}"
)
ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=10, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.savefig(os.path.join(SCRIPT_DIR, 's66_bcs_cw.png'), dpi=150, bbox_inches='tight')
print(f"  Saved: {os.path.join(SCRIPT_DIR, 's66_bcs_cw.png')}")

print("\n" + "=" * 78)
print("DONE")
print("=" * 78)
