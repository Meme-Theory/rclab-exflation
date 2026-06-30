#!/usr/bin/env python3
"""
RUNNING-NS-66 (W3-A) -- Spectral Running at L_max = 4
=======================================================

Sagan falsification challenge #1: alpha_s = dn_s/d(ln k) = -0.039 at L_max=3
is 5.8 sigma from Planck's -0.0045 +/- 0.0067. Is this a truncation artifact
or a genuine prediction in conflict with observation?

Physics:
--------
The spectral action S(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j |lambda_j(tau)|
is computed with cutoff function f(x) = sqrt(x), which yields the |lambda|
weighting. The spectral running alpha_s = dn_s/d(ln k) depends on derivatives
of eps_H, which depend on derivatives of S(tau).

At L_max = 3 (max_pq_sum = 3), only 10 PW sectors contribute (1232 eigenvalues).
At L_max = 4 (max_pq_sum = 4), 15 PW sectors contribute (2912 eigenvalues).
The 5 new sectors at L_max = 4 are:
  (4,0): dim=15, D-matrix 240x240
  (0,4): dim=15, D-matrix 240x240
  (3,1): dim=24, D-matrix 384x384
  (1,3): dim=24, D-matrix 384x384
  (2,2): dim=27, D-matrix 432x432

If the running decreases at L_max = 4, it is a truncation artifact from the
coarse tau-derivative structure at L_max = 3.

Method:
-------
1. Load S36 eigenvalues at 7 tau values for L_max = 3.
2. Compute new eigenvalues for L_max = 4 sectors at each tau using
   dirac_spectrum infrastructure.
3. Compute S(tau) at both L_max values using f(x) = sqrt(x) cutoff.
4. Compute eps_H, eta_H, n_s, alpha_s via cubic spline differentiation.
5. Compare alpha_s at L_max = 3 vs 4.

Gate: RUNNING-NS-66
  PASS: |alpha_s(L=4)| < 0.015 (running consistent with Planck within 2 sigma)
  FAIL: |alpha_s(L=4)| > 0.030 (running persists at falsification level)
  INFO: 0.015 < |alpha_s(L=4)| < 0.030 (reduced but still in tension)

Agent: gen-physicist (Session 66, Wave 3)
"""

import numpy as np
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, Delta_0_OES, S_fold, dS_fold, d2S_fold,
    G_DeWitt, M_KK, PI, a0_fold, a2_fold, a4_fold
)

from dirac_spectrum import (
    su3_generators, compute_structure_constants,
    build_cliff8, compute_killing_form, jensen_metric,
    orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    get_irrep, dirac_operator_on_irrep, _irrep_cache
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("RUNNING-NS-66 (W3-A): Spectral Running at L_max = 4")
print("=" * 78)

Delta = Delta_0_OES   # 0.464 M_KK (BCS gap)
G = G_DeWitt          # 5.0 (DeWitt moduli kinetic coefficient)
# planck_ns = 0.9649  # S72: now imported from canonical_constants
planck_sigma = planck_ns_err  # S72: was 0.0042, now imported from canonical_constants
planck_alpha_s = -0.0045  # (local)
planck_alpha_s_sigma = 0.0067  # (local)

tau_f = tau_fold  # 0.19

print(f"\n  tau_fold              = {tau_f}")
print(f"  Delta (BCS gap)       = {Delta:.6f} M_KK")
print(f"  G_DeWitt              = {G:.1f}")
print(f"  Planck n_s            = {planck_ns} +/- {planck_sigma}")
print(f"  Planck alpha_s        = {planck_alpha_s} +/- {planck_alpha_s_sigma}")

# =============================================================================
# STEP 0: LOAD L_max = 3 EIGENVALUES FROM S36
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load L_max = 3 Eigenvalues from S36 Archive")
print("=" * 78)

d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)

tau_evals = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])
tau_combined = d_s36['tau_combined']
S_full_s36 = d_s36['S_full']

def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# L_max = 3 sectors
sectors_L3 = []
for p in range(4):
    for q in range(4):
        if p + q <= 3:
            sectors_L3.append((p, q))

# L_max = 4 NEW sectors (those with p+q == 4)
sectors_L4_new = []
for p in range(5):
    for q in range(5):
        if p + q == 4:
            sectors_L4_new.append((p, q))

print(f"\n  L_max = 3 sectors: {len(sectors_L3)} -> {sectors_L3}")
print(f"  L_max = 4 new sectors: {len(sectors_L4_new)} -> {sectors_L4_new}")
print(f"  Tau grid: {tau_evals}")

# Verify S36 data availability
n_available = 0
for tau in tau_evals:
    for (p, q) in sectors_L3:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key in d_s36:
            n_available += 1
print(f"  S36 eigenvalue arrays available: {n_available} / {len(tau_evals) * len(sectors_L3)}")

# Count eigenvalues per level
total_evals_L3 = 0
total_evals_L4_new = 0
for (p, q) in sectors_L3:
    d = su3_dim(p, q)
    total_evals_L3 += d * 16  # 16 spinor components per irrep dim
for (p, q) in sectors_L4_new:
    d = su3_dim(p, q)
    total_evals_L4_new += d * 16

print(f"\n  Raw eigenvalues at L_max=3: {total_evals_L3}")
print(f"  Raw eigenvalues from new L4 sectors: {total_evals_L4_new}")
print(f"  Total at L_max=4: {total_evals_L3 + total_evals_L4_new}")

# =============================================================================
# STEP 1: COMPUTE L_max = 4 SECTOR EIGENVALUES AT EACH TAU
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Compute L_max = 4 Sector Eigenvalues")
print("=" * 78)

print("""
  For each tau value and each new sector (p,q) with p+q=4, we:
  1. Build the Jensen metric g_s at deformation parameter tau
  2. Compute orthonormal frame, connection, spin connection offset Omega
  3. Build irrep rho_{(p,q)} via Casimir projection
  4. Assemble D_{(p,q)} = sum_a rho(e_a) x gamma_a + I x Omega
  5. Diagonalize D_{(p,q)} to get eigenvalues
""")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()
B_ab = compute_killing_form(f_abc)

# Store new eigenvalues: evals_L4[tau_idx][(p,q)] = array of eigenvalues
evals_L4_new_data = {}

t_total_start = time.time()

for i, tau in enumerate(tau_evals):
    t0 = time.time()
    print(f"\n  tau = {tau:.3f}:")

    # Build geometry for this tau
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Clear irrep cache for each tau (geometry changes)
    _irrep_cache.clear()

    for (p, q) in sectors_L4_new:
        dim_pq = su3_dim(p, q)
        D_size = dim_pq * 16

        t1 = time.time()

        # Build irrep representation matrices
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        assert dim_check == dim_pq, f"Dimension mismatch: {dim_check} vs {dim_pq}"

        # Assemble Dirac operator on this sector
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Diagonalize
        evals_pi = np.linalg.eigvals(D_pi)

        # Verify anti-Hermiticity: eigenvalues should be purely imaginary
        real_parts = np.real(evals_pi)
        imag_parts = np.imag(evals_pi)
        max_real = np.max(np.abs(real_parts))

        # Store eigenvalues (as full complex numbers, matching S36 convention)
        evals_L4_new_data[(i, p, q)] = evals_pi

        t2 = time.time()
        print(f"    ({p},{q}): dim={dim_pq}, D={D_size}x{D_size}, "
              f"|Re| max={max_real:.2e}, |Im| range=[{np.min(np.abs(imag_parts)):.4f}, "
              f"{np.max(np.abs(imag_parts)):.4f}], time={t2-t1:.1f}s")

t_total = time.time() - t_total_start
print(f"\n  Total L_max=4 computation time: {t_total:.1f}s")

# =============================================================================
# STEP 2: COMPUTE S(tau) AT BOTH L_max VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Spectral Action S(tau) at L_max = 3 and L_max = 4")
print("=" * 78)

print("""
  Cutoff function: f(x) = sqrt(x)
  Spectral action: S(tau) = sum_{(p,q)} dim(p,q)^2 * sum_j |lambda_j(tau)|

  Tree-level: S^bare using |lambda|
  BCS-dressed: S^BCS using sqrt(lambda^2 + Delta^2)
""")

# Arrays for both L_max values and both bare/BCS
S_bare_L3 = np.zeros(len(tau_evals))
S_bcs_L3 = np.zeros(len(tau_evals))
S_bare_L4 = np.zeros(len(tau_evals))
S_bcs_L4 = np.zeros(len(tau_evals))

# Also track one-loop contributions
S_1loop_bare_L3 = np.zeros(len(tau_evals))
S_1loop_bcs_L3 = np.zeros(len(tau_evals))
S_1loop_bare_L4 = np.zeros(len(tau_evals))
S_1loop_bcs_L4 = np.zeros(len(tau_evals))

for i, tau in enumerate(tau_evals):
    # L_max = 3: use S36 stored eigenvalues
    for (p, q) in sectors_L3:
        key = f'evals_tau{tau:.3f}_{p}_{q}'
        if key not in d_s36:
            print(f"  WARNING: {key} not found in S36 archive")
            continue

        evals = d_s36[key]
        dim_pq = su3_dim(p, q)
        pw_tree = dim_pq ** 2
        pw_1loop = dim_pq

        omega = np.abs(evals)
        omega_sq = omega ** 2
        E_bdg = np.sqrt(omega_sq + Delta ** 2)

        # Tree-level
        S_bare_L3[i] += pw_tree * np.sum(omega)
        S_bcs_L3[i] += pw_tree * np.sum(E_bdg)

        # One-loop
        omega_sq_safe = np.maximum(omega_sq, 1e-30)
        S_1loop_bare_L3[i] += 0.5 * pw_1loop * np.sum(np.log(omega_sq_safe))
        S_1loop_bcs_L3[i] += 0.5 * pw_1loop * np.sum(np.log(omega_sq + Delta ** 2))

    # L_max = 4: start from L_max = 3 and ADD new sectors
    S_bare_L4[i] = S_bare_L3[i]
    S_bcs_L4[i] = S_bcs_L3[i]
    S_1loop_bare_L4[i] = S_1loop_bare_L3[i]
    S_1loop_bcs_L4[i] = S_1loop_bcs_L3[i]

    for (p, q) in sectors_L4_new:
        evals = evals_L4_new_data[(i, p, q)]
        dim_pq = su3_dim(p, q)
        pw_tree = dim_pq ** 2
        pw_1loop = dim_pq

        omega = np.abs(evals)
        omega_sq = omega ** 2
        E_bdg = np.sqrt(omega_sq + Delta ** 2)

        S_bare_L4[i] += pw_tree * np.sum(omega)
        S_bcs_L4[i] += pw_tree * np.sum(E_bdg)

        omega_sq_safe = np.maximum(omega_sq, 1e-30)
        S_1loop_bare_L4[i] += 0.5 * pw_1loop * np.sum(np.log(omega_sq_safe))
        S_1loop_bcs_L4[i] += 0.5 * pw_1loop * np.sum(np.log(omega_sq + Delta ** 2))

# Effective actions = tree + one-loop
S_eff_bare_L3 = S_bare_L3 + S_1loop_bare_L3
S_eff_bcs_L3 = S_bcs_L3 + S_1loop_bcs_L3
S_eff_bare_L4 = S_bare_L4 + S_1loop_bare_L4
S_eff_bcs_L4 = S_bcs_L4 + S_1loop_bcs_L4

# Cross-check: S_bare_L3 should match S36 S_full at matching tau
print(f"\n  Cross-checks:")
for j, tau in enumerate(tau_evals):
    idx_s36 = np.argmin(np.abs(tau_combined - tau))
    if abs(tau_combined[idx_s36] - tau) < 0.001:
        dev = abs(S_bare_L3[j] - S_full_s36[idx_s36]) / S_full_s36[idx_s36]
        status = "OK" if dev < 1e-8 else f"WARNING dev={dev:.2e}"
        if j == 0 or tau == 0.19:
            print(f"    tau={tau:.3f}: S_bare_L3={S_bare_L3[j]:.2f}, "
                  f"S36={S_full_s36[idx_s36]:.2f}, dev={dev:.2e} [{status}]")

# L4/L3 ratio at each tau
print(f"\n  {'tau':>6s}  {'S_bare_L3':>14s}  {'S_bare_L4':>14s}  {'L4/L3':>8s}  "
      f"{'S_eff_bcs_L3':>14s}  {'S_eff_bcs_L4':>14s}  {'L4/L3':>8s}")
print(f"  {'----':>6s}  {'-'*14}  {'-'*14}  {'-'*8}  {'-'*14}  {'-'*14}  {'-'*8}")
for j in range(len(tau_evals)):
    r_bare = S_bare_L4[j] / S_bare_L3[j]
    r_eff = S_eff_bcs_L4[j] / S_eff_bcs_L3[j]
    print(f"  {tau_evals[j]:6.3f}  {S_bare_L3[j]:14.2f}  {S_bare_L4[j]:14.2f}  "
          f"{r_bare:8.5f}  {S_eff_bcs_L3[j]:14.2f}  {S_eff_bcs_L4[j]:14.2f}  "
          f"{r_eff:8.5f}")

# Fractional contribution from L4 sectors
delta_S_L4 = S_bare_L4 - S_bare_L3
frac_L4 = delta_S_L4 / S_bare_L4
idx_fold = np.argmin(np.abs(tau_evals - 0.19))
print(f"\n  L4 sector contribution as fraction of total:")
print(f"    at fold (tau={tau_evals[idx_fold]:.2f}): "
      f"delta_S = {delta_S_L4[idx_fold]:.2f}, "
      f"fraction = {frac_L4[idx_fold]:.4f} = {frac_L4[idx_fold]*100:.2f}%")

# =============================================================================
# STEP 3: SLOW-ROLL PARAMETERS AT BOTH L_max VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Slow-Roll Parameters (L_max = 3 vs 4)")
print("=" * 78)

print("""
  For each L_max, compute eps_H, eta_H, n_s at the fold using:
  - BCS+1-loop effective action S_eff^BCS(tau)
  - Cubic spline interpolation through near-fold tau points
  - eps_H = (1/2) * (S')^2 / (S * S'')     [Hubble slow-roll]
  - eps_V = (1/2) * (S'/S)^2 / G_DeWitt     [potential slow-roll]
  - eta_V = S'' / (S * G_DeWitt)
  - eta_H = eta_V / (1 - eps_V/3)
  - n_s = 1 - 2*eps_H - eta_H
""")

# Use near-fold tau points (skip tau=0.05 which is far from fold)
idx_near = np.arange(1, len(tau_evals))  # indices 1-6: tau=0.16..0.22
tau_near = tau_evals[idx_near]

results = {}

configs = {
    'bare_L3': ('Bare tree L_max=3', S_bare_L3[idx_near]),
    'bare_L4': ('Bare tree L_max=4', S_bare_L4[idx_near]),
    'bcs_L3': ('BCS+1loop L_max=3', S_eff_bcs_L3[idx_near]),
    'bcs_L4': ('BCS+1loop L_max=4', S_eff_bcs_L4[idx_near]),
}

for label, (desc, S_arr) in configs.items():
    cs = CubicSpline(tau_near, S_arr)
    S_val = float(cs(tau_f))
    dS_val = float(cs(tau_f, 1))
    d2S_val = float(cs(tau_f, 2))

    # Hubble slow-roll
    eps_H = 0.5 * dS_val ** 2 / (S_val * d2S_val) if d2S_val > 0 else np.inf
    ns_hubble = 1.0 - 2.0 * eps_H

    # Potential slow-roll with G_DeWitt normalization
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

    print(f"\n  {label}: {desc}")
    print(f"    S(fold)      = {S_val:14.2f}")
    print(f"    S'(fold)     = {dS_val:14.2f}")
    print(f"    S''(fold)    = {d2S_val:14.2f}")
    print(f"    eps_H        = {eps_H:.6f}")
    print(f"    eta_H        = {eta_H:.6f}")
    print(f"    n_s(Hubble)  = {ns_hubble:.6f}")
    print(f"    n_s(3-param) = {ns_three:.6f}")

# =============================================================================
# STEP 4: SPECTRAL RUNNING dn_s/d(ln k) AT BOTH L_max VALUES
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Spectral Running dn_s/d(ln k)")
print("=" * 78)

print("""
  Running alpha_s = dn_s/d(ln k) = -2 * d(eps_H)/dtau * dtau/d(ln k)
  where dtau/d(ln k) = eps_H / (d(ln S)/dtau)

  Computed numerically: d(eps_H)/dtau via central difference at dtau = 0.001
""")

dtau = 0.001  # (local)
running_results = {}

for label in ['bare_L3', 'bare_L4', 'bcs_L3', 'bcs_L4']:
    cs = results[label]['spline']
    eps_H = results[label]['eps_H']

    # Numerical derivative of eps_H at fold
    def eps_at_tau(t):
        S_t = float(cs(t))
        dS_t = float(cs(t, 1))
        d2S_t = float(cs(t, 2))
        if d2S_t > 0 and S_t > 0:
            return 0.5 * dS_t ** 2 / (S_t * d2S_t)
        return np.nan

    eps_plus = eps_at_tau(tau_f + dtau)
    eps_minus = eps_at_tau(tau_f - dtau)
    deps_dtau = (eps_plus - eps_minus) / (2 * dtau)

    # dtau/d(ln k) in slow-roll
    dln_S_dtau = float(cs(tau_f, 1)) / float(cs(tau_f))
    dtau_dlnk = eps_H / dln_S_dtau if dln_S_dtau > 0 else 0

    # Running
    dn_s_dlnk = -2.0 * deps_dtau * dtau_dlnk

    running_results[label] = {
        'deps_dtau': deps_dtau,
        'dln_S_dtau': dln_S_dtau,
        'dtau_dlnk': dtau_dlnk,
        'alpha_s': dn_s_dlnk,
    }

    print(f"\n  {label}: {results[label]['desc']}")
    print(f"    d(eps_H)/dtau     = {deps_dtau:.6f}")
    print(f"    d(ln S)/dtau      = {dln_S_dtau:.6f}")
    print(f"    dtau/d(ln k)      = {dtau_dlnk:.6f}")
    print(f"    alpha_s           = {dn_s_dlnk:.6e}")

# Also try a wider stencil for the derivative (robustness check)
print(f"\n  Stencil robustness check on bcs_L4:")
for dt in [0.0005, 0.001, 0.002, 0.005]:
    cs = results['bcs_L4']['spline']
    ep = eps_at_tau(tau_f + dt)
    em = eps_at_tau(tau_f - dt)
    dep = (ep - em) / (2 * dt)
    dls = float(cs(tau_f, 1)) / float(cs(tau_f))
    dtdlk = results['bcs_L4']['eps_H'] / dls if dls > 0 else 0
    alpha = -2.0 * dep * dtdlk  # (local)
    print(f"    dtau={dt:.4f}: d(eps_H)/dtau={dep:.6f}, alpha_s={alpha:.6e}")

# =============================================================================
# STEP 5: COMPARISON AND CONVERGENCE ANALYSIS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: L_max Convergence Analysis")
print("=" * 78)

alpha_s_L3 = running_results['bcs_L3']['alpha_s']
alpha_s_L4 = running_results['bcs_L4']['alpha_s']
alpha_s_bare_L3 = running_results['bare_L3']['alpha_s']
alpha_s_bare_L4 = running_results['bare_L4']['alpha_s']

ratio_bcs = abs(alpha_s_L4) / abs(alpha_s_L3) if abs(alpha_s_L3) > 1e-20 else np.inf
ratio_bare = abs(alpha_s_bare_L4) / abs(alpha_s_bare_L3) if abs(alpha_s_bare_L3) > 1e-20 else np.inf

print(f"\n  BCS+1-loop running:")
print(f"    alpha_s(L=3) = {alpha_s_L3:.6e}")
print(f"    alpha_s(L=4) = {alpha_s_L4:.6e}")
print(f"    |alpha_s(L=4)| / |alpha_s(L=3)| = {ratio_bcs:.4f}")
print(f"    Reduction: {(1 - ratio_bcs) * 100:.1f}%")

print(f"\n  Bare tree running:")
print(f"    alpha_s(L=3) = {alpha_s_bare_L3:.6e}")
print(f"    alpha_s(L=4) = {alpha_s_bare_L4:.6e}")
print(f"    |alpha_s(L=4)| / |alpha_s(L=3)| = {ratio_bare:.4f}")
print(f"    Reduction: {(1 - ratio_bare) * 100:.1f}%")

# Convergence: if S(L) ~ S_inf * (1 - A/L^n), then derivatives converge as L^{-n}
# Fractional changes
frac_S = (results['bcs_L4']['S'] - results['bcs_L3']['S']) / results['bcs_L3']['S']
frac_dS = (results['bcs_L4']['dS'] - results['bcs_L3']['dS']) / results['bcs_L3']['dS']
frac_d2S = (results['bcs_L4']['d2S'] - results['bcs_L3']['d2S']) / results['bcs_L3']['d2S']

print(f"\n  Fractional changes in S, S', S'' (BCS+1loop, L3->L4):")
print(f"    delta(S)/S     = {frac_S:+.6f}  ({frac_S*100:+.4f}%)")
print(f"    delta(S')/S'   = {frac_dS:+.6f}  ({frac_dS*100:+.4f}%)")
print(f"    delta(S'')/S'' = {frac_d2S:+.6f}  ({frac_d2S*100:+.4f}%)")

# n_s comparison
ns_L3 = results['bcs_L3']['ns_hubble']
ns_L4 = results['bcs_L4']['ns_hubble']
delta_ns = ns_L4 - ns_L3
eps_L3 = results['bcs_L3']['eps_H']
eps_L4 = results['bcs_L4']['eps_H']

print(f"\n  n_s comparison:")
print(f"    n_s(L=3, BCS+1loop)  = {ns_L3:.6f}")
print(f"    n_s(L=4, BCS+1loop)  = {ns_L4:.6f}")
print(f"    delta(n_s)           = {delta_ns:+.6f}")
print(f"    eps_H(L=3)           = {eps_L3:.6f}")
print(f"    eps_H(L=4)           = {eps_L4:.6f}")

# =============================================================================
# STEP 6: EXTRAPOLATION ESTIMATE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: Extrapolation to L_max -> infinity")
print("=" * 78)

print("""
  With only 2 data points (L=3, L=4), we can at best fit alpha_s(L) = a + b/L^n.
  Assume n=2 (standard truncation convergence for smooth operators):
    alpha_s(inf) = alpha_s(L=4) - [alpha_s(L=3) - alpha_s(L=4)] * 4^2 / (3^2 - 4^2)
  This is Richardson extrapolation with assumed L^{-2} convergence.
""")

# Richardson extrapolation assuming L^{-2} convergence
# alpha(L) = alpha_inf + c/L^2
# alpha(3) = alpha_inf + c/9
# alpha(4) = alpha_inf + c/16
# => c = (alpha(3) - alpha(4)) * 9 * 16 / (16 - 9) = (alpha(3) - alpha(4)) * 144/7
# => alpha_inf = alpha(4) - c/16 = alpha(4) - (alpha(3) - alpha(4)) * 9/7

if abs(alpha_s_L3 - alpha_s_L4) > 1e-20:
    alpha_s_inf_2 = alpha_s_L4 - (alpha_s_L3 - alpha_s_L4) * 9.0 / 7.0
    print(f"\n  Richardson (L^{{-2}}): alpha_s(inf) = {alpha_s_inf_2:.6e}")
else:
    alpha_s_inf_2 = alpha_s_L4
    print(f"\n  No change between L=3 and L=4; alpha_s(inf) = alpha_s(L=4)")

# Repeat for L^{-4} assumption (more aggressive)
# alpha(L) = alpha_inf + c/L^4
# c = (alpha(3) - alpha(4)) * 81*256 / (256-81) = (alpha(3)-alpha(4)) * 20736/175
# alpha_inf = alpha(4) - c/256
if abs(alpha_s_L3 - alpha_s_L4) > 1e-20:
    c_4 = (alpha_s_L3 - alpha_s_L4) * 81 * 256 / (256 - 81)
    alpha_s_inf_4 = alpha_s_L4 - c_4 / 256
    print(f"  Richardson (L^{{-4}}): alpha_s(inf) = {alpha_s_inf_4:.6e}")
else:
    alpha_s_inf_4 = alpha_s_L4

# Planck tension
tension_L3 = (alpha_s_L3 - planck_alpha_s) / planck_alpha_s_sigma
tension_L4 = (alpha_s_L4 - planck_alpha_s) / planck_alpha_s_sigma
tension_inf_2 = (alpha_s_inf_2 - planck_alpha_s) / planck_alpha_s_sigma

print(f"\n  Planck tension on alpha_s:")
print(f"    L_max=3:  {tension_L3:+.1f} sigma")
print(f"    L_max=4:  {tension_L4:+.1f} sigma")
print(f"    Extrap:   {tension_inf_2:+.1f} sigma (Richardson L^{{-2}})")

# =============================================================================
# STEP 7: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: GATE VERDICT -- RUNNING-NS-66")
print("=" * 78)

# The gate is on |alpha_s(L=4)|
alpha_s_decisive = alpha_s_L4

if abs(alpha_s_decisive) < 0.015:
    verdict = "PASS"
    detail_reason = (f"|alpha_s(L=4)| = {abs(alpha_s_decisive):.6f} < 0.015 "
                     f"(running consistent with Planck within 2 sigma)")
elif abs(alpha_s_decisive) > 0.030:
    verdict = "FAIL"
    detail_reason = (f"|alpha_s(L=4)| = {abs(alpha_s_decisive):.6f} > 0.030 "
                     f"(running persists at falsification level)")
else:
    verdict = "INFO"
    detail_reason = (f"|alpha_s(L=4)| = {abs(alpha_s_decisive):.6f} in [0.015, 0.030] "
                     f"(reduced but still in tension)")

print(f"\n  GATE: RUNNING-NS-66")
print(f"  CRITERION:")
print(f"    PASS: |alpha_s(L=4)| < 0.015")
print(f"    FAIL: |alpha_s(L=4)| > 0.030")
print(f"    INFO: 0.015 < |alpha_s(L=4)| < 0.030")
print(f"")
print(f"  |alpha_s(L=4)| = {abs(alpha_s_decisive):.6f}")
print(f"  alpha_s(L=3)   = {alpha_s_L3:.6e}")
print(f"  alpha_s(L=4)   = {alpha_s_L4:.6e}")
print(f"  Reduction ratio = {ratio_bcs:.4f}")
print(f"")
print(f"  VERDICT: {verdict}")
print(f"  {detail_reason}")

# =============================================================================
# STEP 8: SUMMARY TABLE
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Summary Table")
print("=" * 78)

print(f"\n  {'Configuration':>30s}  {'eps_H':>10s}  {'n_s':>10s}  {'alpha_s':>12s}  "
      f"{'|alpha_s|/Planck':>16s}")
print(f"  {'-'*30}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*16}")
for label in ['bare_L3', 'bare_L4', 'bcs_L3', 'bcs_L4']:
    ns = results[label]['ns_hubble']
    alpha = running_results[label]['alpha_s']
    ratio_planck = abs(alpha - planck_alpha_s) / planck_alpha_s_sigma
    print(f"  {results[label]['desc']:>30s}  {results[label]['eps_H']:10.6f}  "
          f"{ns:10.6f}  {alpha:12.6e}  {ratio_planck:16.1f} sigma")
print(f"  {'Planck 2018':>30s}  {'---':>10s}  {planck_ns:10.4f}  "
      f"{planck_alpha_s:12.6e}  {'0.0 sigma':>16s}")

# =============================================================================
# STEP 9: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Save Data")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's66_running_ns.npz')

# Prepare eigenvalue data for new sectors
evals_save = {}
for (key, evals) in evals_L4_new_data.items():
    i, p, q = key
    evals_save[f'evals_L4_tau{tau_evals[i]:.3f}_{p}_{q}'] = evals

np.savez(
    outpath,
    # Gate
    gate_name='RUNNING-NS-66',
    gate_verdict=verdict,
    gate_detail=detail_reason,

    # Alpha_s results
    alpha_s_L3=alpha_s_L3,
    alpha_s_L4=alpha_s_L4,
    alpha_s_bare_L3=alpha_s_bare_L3,
    alpha_s_bare_L4=alpha_s_bare_L4,
    alpha_s_ratio=ratio_bcs,
    alpha_s_extrap_L2=alpha_s_inf_2,
    alpha_s_extrap_L4=alpha_s_inf_4,

    # n_s results
    ns_bcs_L3=ns_L3,
    ns_bcs_L4=ns_L4,
    ns_bare_L3=results['bare_L3']['ns_hubble'],
    ns_bare_L4=results['bare_L4']['ns_hubble'],

    # eps_H
    eps_H_bcs_L3=eps_L3,
    eps_H_bcs_L4=eps_L4,
    eps_H_bare_L3=results['bare_L3']['eps_H'],
    eps_H_bare_L4=results['bare_L4']['eps_H'],

    # Running components
    deps_dtau_L3=running_results['bcs_L3']['deps_dtau'],
    deps_dtau_L4=running_results['bcs_L4']['deps_dtau'],
    dtau_dlnk_L3=running_results['bcs_L3']['dtau_dlnk'],
    dtau_dlnk_L4=running_results['bcs_L4']['dtau_dlnk'],

    # Spectral action profiles
    tau_evals=tau_evals,
    S_bare_L3=S_bare_L3,
    S_bare_L4=S_bare_L4,
    S_bcs_L3=S_bcs_L3,
    S_bcs_L4=S_bcs_L4,
    S_1loop_bare_L3=S_1loop_bare_L3,
    S_1loop_bare_L4=S_1loop_bare_L4,
    S_1loop_bcs_L3=S_1loop_bcs_L3,
    S_1loop_bcs_L4=S_1loop_bcs_L4,
    S_eff_bcs_L3=S_eff_bcs_L3,
    S_eff_bcs_L4=S_eff_bcs_L4,

    # Fractional changes
    frac_delta_S=frac_S,
    frac_delta_dS=frac_dS,
    frac_delta_d2S=frac_d2S,

    # Planck reference
    planck_ns=planck_ns,
    planck_sigma=planck_sigma,
    planck_alpha_s=planck_alpha_s,
    planck_alpha_s_sigma=planck_alpha_s_sigma,

    # Configuration
    Delta=Delta,
    tau_fold=tau_f,
    G_DeWitt=G,

    # New eigenvalues
    **evals_save,
)

print(f"  Saved: {outpath}")

# =============================================================================
# STEP 10: PLOT
# =============================================================================
print("\n  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.42, wspace=0.35)
fig.suptitle(f'RUNNING-NS-66: Spectral Running at L_max = 4 [{verdict}]',
             fontsize=14, fontweight='bold')

# --- Panel (a): S_eff profiles at L_max = 3 vs 4 ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(tau_evals, S_eff_bcs_L3 / 1e3, 'b-o', ms=4, label=r'$S_\mathrm{eff}^{BCS}$ L=3')
ax1.plot(tau_evals, S_eff_bcs_L4 / 1e3, 'r-s', ms=4, label=r'$S_\mathrm{eff}^{BCS}$ L=4')
ax1.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax1.set_xlabel(r'$\tau$', fontsize=11)
ax1.set_ylabel(r'$S_\mathrm{eff} \times 10^{-3}$', fontsize=11)
ax1.set_title('(a) Effective Action Profiles', fontsize=12)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# --- Panel (b): Fractional contribution from L4 sectors ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(tau_evals, frac_L4 * 100, 'k-o', ms=5, lw=2)
ax2.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax2.set_xlabel(r'$\tau$', fontsize=11)
ax2.set_ylabel(r'$\Delta S_{L=4} / S_\mathrm{total}$ (%)', fontsize=11)
ax2.set_title('(b) L=4 Sector Fractional Contribution', fontsize=12)
ax2.grid(True, alpha=0.3)

# --- Panel (c): Derivative S'(tau) at both L_max ---
ax3 = fig.add_subplot(gs[0, 2])
dS_L3_arr = np.array([float(results['bcs_L3']['spline'](t, 1)) for t in tau_near])
dS_L4_arr = np.array([float(results['bcs_L4']['spline'](t, 1)) for t in tau_near])
ax3.plot(tau_near, dS_L3_arr, 'b-o', ms=4, label="L=3")
ax3.plot(tau_near, dS_L4_arr, 'r-s', ms=4, label="L=4")
ax3.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax3.set_xlabel(r'$\tau$', fontsize=11)
ax3.set_ylabel(r"$S'(\tau)$", fontsize=11)
ax3.set_title(r"(c) $dS/d\tau$ at L=3 vs L=4", fontsize=12)
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)

# --- Panel (d): eps_H(tau) at both L_max ---
ax4 = fig.add_subplot(gs[1, 0])
tau_scan = np.linspace(0.16, 0.22, 100)
for label, color, marker in [('bcs_L3', 'blue', '-'), ('bcs_L4', 'red', '--')]:
    cs = results[label]['spline']
    eps_scan = []
    for t in tau_scan:
        S_t = float(cs(t))
        dS_t = float(cs(t, 1))
        d2S_t = float(cs(t, 2))
        if d2S_t > 0 and S_t > 0:
            eps_scan.append(0.5 * dS_t ** 2 / (S_t * d2S_t))
        else:
            eps_scan.append(np.nan)
    ax4.plot(tau_scan, eps_scan, color=color, ls=marker, lw=2,
             label=f"L={label[-1]}")
ax4.axvline(x=0.19, color='gray', ls='--', alpha=0.5)
ax4.set_xlabel(r'$\tau$', fontsize=11)
ax4.set_ylabel(r'$\epsilon_H$', fontsize=11)
ax4.set_title(r'(d) $\epsilon_H(\tau)$ at L=3 vs L=4', fontsize=12)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

# --- Panel (e): alpha_s bar chart ---
ax5 = fig.add_subplot(gs[1, 1])
labels_bar = ['Bare\nL=3', 'Bare\nL=4', 'BCS\nL=3', 'BCS\nL=4',
              'Extrap\n(L^-2)']
vals_bar = [alpha_s_bare_L3, alpha_s_bare_L4, alpha_s_L3, alpha_s_L4, alpha_s_inf_2]
colors_bar = ['#1f77b4', '#1f77b4', '#d62728', '#d62728', '#2ca02c']
bars = ax5.bar(labels_bar, vals_bar, color=colors_bar, edgecolor='black')
for bar, a in zip(bars, [0.5, 0.9, 0.5, 0.9, 0.7]):
    bar.set_alpha(a)
# Planck band
ax5.axhspan(planck_alpha_s - 2 * planck_alpha_s_sigma,
            planck_alpha_s + 2 * planck_alpha_s_sigma,
            alpha=0.15, color='gold', label=r'Planck $2\sigma$')  # (local)
ax5.axhline(y=planck_alpha_s, color='orange', ls='-', lw=2, alpha=0.5)
for bar, val in zip(bars, vals_bar):
    y_pos = bar.get_height() - 0.003 if val < 0 else bar.get_height() + 0.001
    ax5.text(bar.get_x() + bar.get_width() / 2., y_pos,
             f'{val:.4f}', ha='center', va='top' if val < 0 else 'bottom', fontsize=7)
ax5.set_ylabel(r'$\alpha_s = dn_s/d\ln k$', fontsize=11)
ax5.set_title(r'(e) Spectral Running $\alpha_s$', fontsize=12)
ax5.legend(fontsize=8, loc='lower right')
ax5.grid(True, alpha=0.3, axis='y')

# --- Panel (f): n_s comparison ---
ax6 = fig.add_subplot(gs[1, 2])
labels_ns = ['Bare L=3', 'Bare L=4', 'BCS+1L L=3', 'BCS+1L L=4']
vals_ns = [results['bare_L3']['ns_hubble'], results['bare_L4']['ns_hubble'],
           ns_L3, ns_L4]
colors_ns = ['#1f77b4', '#1f77b4', '#d62728', '#d62728']
hbars = ax6.barh(labels_ns, vals_ns, color=colors_ns, edgecolor='black')
for bar, a in zip(hbars, [0.5, 0.9, 0.5, 0.9]):
    bar.set_alpha(a)
ax6.axvspan(planck_ns - planck_sigma, planck_ns + planck_sigma,
            alpha=0.15, color='gold', label=r'Planck $1\sigma$')  # (local)
ax6.axvline(x=planck_ns, color='red', ls='-', lw=2, alpha=0.5)
for j, val in enumerate(vals_ns):
    ax6.text(val + 0.0002, j, f'{val:.4f}', va='center', fontsize=8)
ax6.set_xlabel(r'$n_s$', fontsize=11)
ax6.set_title(r'(f) Spectral Index $n_s$', fontsize=12)
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.3, axis='x')

# --- Panel (g): L_max convergence ---
ax7 = fig.add_subplot(gs[2, 0])
L_vals = [3, 4]
alpha_vals = [abs(alpha_s_L3), abs(alpha_s_L4)]
ax7.semilogy(L_vals, alpha_vals, 'ro-', ms=8, lw=2, label=r'$|\alpha_s|$ (BCS+1loop)')
# Show threshold lines
ax7.axhline(y=0.015, color='green', ls='--', alpha=0.5, label='PASS threshold')
ax7.axhline(y=0.030, color='red', ls='--', alpha=0.5, label='FAIL threshold')
ax7.axhline(y=abs(planck_alpha_s), color='orange', ls=':', alpha=0.5, label='Planck central')
# Show extrapolation
if abs(alpha_s_inf_2) > 1e-20:
    ax7.plot([5], [abs(alpha_s_inf_2)], 'g^', ms=10, label=r'Extrap ($L^{-2}$)')
ax7.set_xlabel(r'$L_\mathrm{max}$ (max $p+q$)', fontsize=11)
ax7.set_ylabel(r'$|\alpha_s|$', fontsize=11)
ax7.set_title(r'(g) $|\alpha_s|$ Convergence', fontsize=12)
ax7.legend(fontsize=8)
ax7.set_xlim(2.5, 5.5)
ax7.grid(True, alpha=0.3)

# --- Panel (h): deps_dtau decomposition ---
ax8 = fig.add_subplot(gs[2, 1])
labels_dep = [r'$d\epsilon_H/d\tau$' + '\nL=3',
              r'$d\epsilon_H/d\tau$' + '\nL=4',
              r'$d\tau/d\ln k$' + '\nL=3',
              r'$d\tau/d\ln k$' + '\nL=4']
vals_dep = [running_results['bcs_L3']['deps_dtau'],
            running_results['bcs_L4']['deps_dtau'],
            running_results['bcs_L3']['dtau_dlnk'],
            running_results['bcs_L4']['dtau_dlnk']]
colors_dep = ['blue', 'red', 'blue', 'red']
bars8 = ax8.bar(labels_dep, vals_dep, color=colors_dep, edgecolor='black')
for bar, a in zip(bars8, [0.6, 0.9, 0.6, 0.9]):
    bar.set_alpha(a)
for bar, val in zip(bars8, vals_dep):
    ax8.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 0.003,
             f'{val:.4f}', ha='center', va='bottom', fontsize=7)
ax8.set_ylabel('Value', fontsize=11)
ax8.set_title('(h) Running Components', fontsize=12)
ax8.grid(True, alpha=0.3, axis='y')

# --- Panel (i): Summary text ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')
summary_text = (
    f"RUNNING-NS-66  [{verdict}]\n"
    f"{'='*40}\n\n"
    f"alpha_s(L=3) = {alpha_s_L3:.4e}\n"
    f"alpha_s(L=4) = {alpha_s_L4:.4e}\n"
    f"|L4|/|L3|    = {ratio_bcs:.4f}\n\n"
    f"n_s(L=3)     = {ns_L3:.6f}\n"
    f"n_s(L=4)     = {ns_L4:.6f}\n\n"
    f"Planck alpha_s = {planck_alpha_s}\n"
    f"  +/- {planck_alpha_s_sigma}\n\n"
    f"L4 sector fraction = {frac_L4[idx_fold]*100:.2f}%\n\n"
    f"Extrap (L^-2) = {alpha_s_inf_2:.4e}\n"
)
ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=10, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plotpath = os.path.join(SCRIPT_DIR, 's66_running_ns.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Saved plot: {plotpath}")

# =============================================================================
# DONE
# =============================================================================
print("\n" + "=" * 78)
print("RUNNING-NS-66 COMPLETE")
print("=" * 78)
print(f"\n  VERDICT: {verdict}")
print(f"  alpha_s(L=4) = {alpha_s_L4:.6e}")
print(f"  |alpha_s(L=4)| / |alpha_s(L=3)| = {ratio_bcs:.4f}")
print(f"  n_s(L=4) = {ns_L4:.6f}")
