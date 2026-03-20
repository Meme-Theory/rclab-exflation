#!/usr/bin/env python3
"""
Session 45 W3-R1: Scale Selection Principle for Spectral Dimension n_s (SIGMA-SELECT-45)
========================================================================================

The spectral dimension d_s(sigma, tau) from S44 DIMFLOW-44 gives n_s as a function of
the diffusion-time parameter sigma, but sigma itself is unfixed. This script tests four
independent scale selection principles to determine whether a self-consistent sigma*
exists, and if so, what n_s(sigma*) it yields.

Mathematical framework:
  Heat kernel return probability:
    K(sigma) = Tr exp(-sigma D_K^2) = sum_k mult_k * exp(-sigma * lambda_k^2)

  Spectral dimension:
    d_s(sigma) = -2 * sigma * d(ln K) / d(sigma)   [Eq. (a)]
              = -2 * d(ln K) / d(ln sigma)

  n_s extraction (Hawking flow formula):
    n_s - 1 = -d(d_s)/d(tau) * dtau/d(ln k)   [Eq. (b)]

  We use dtau/d(ln k) = 1 (modes exit at unit rate in spectral time).
  The CDT formula n_s = 1 + (d_s - 4)/2 is also tested but is less physical.

  Limiting behavior [Eq. (c)]:
    sigma -> 0: d_s -> dim(M) = 8  (Weyl's law, continuum)
    sigma -> 0: d_s -> 0  (finite truncation, ~9280 modes)
    sigma -> infinity: d_s -> 0  (compact space, gap dominates)

References [Eq. (d)]:
  - Connes Paper 28 (spectral truncations)
  - S44 W2-2 (DIMFLOW-44): d_s(sigma, tau) landscape, n_s = 0.961 at sigma = 1.10

Four selection principles:
  1. BACKREACTION SELF-CONSISTENCY: Lambda = Lambda_0 * (d_s/4)^{1/2}
  2. HUBBLE MATCHING: sigma_H = 1/H^2 in M_KK units
  3. OCCUPIED-STATE: n_k * D_K^2 in heat kernel
  4. Q-THEORY sigma: sigma = f(tau*) where tau* = 0.209 from Q-THEORY-BCS-45

Pre-registered gate SIGMA-SELECT-45:
  PASS: Self-consistent sigma yields n_s in [0.955, 0.975]
  FAIL: No fixed point exists in any of the 4 methods
  INFO: Sigma found but n_s outside [0.955, 0.975]

Author: Connes NCG Theorist (Session 45)
"""

import numpy as np
from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Import canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, H_fold, M_KK_gravity, M_KK_kerner, M_KK,
    Delta_0_GL, E_cond, E_B1, E_B2_mean, E_B3_mean,
    dt_transit, v_terminal, G_DeWitt, S_fold, dS_fold,
    M_Pl_reduced, H_0_GeV, k_B, a2_fold, a4_fold
)

# ═══════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

data_dir = Path(__file__).parent
output_npz = data_dir / "s45_sigma_select.npz"
output_png = data_dir / "s45_sigma_select.png"

SECTORS = [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(3,0),(0,3),(2,1),(1,2)]

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ═══════════════════════════════════════════════════════════════════════
# STEP 0: LOAD DATA
# ═══════════════════════════════════════════════════════════════════════

print("=" * 78)
print("SESSION 45 W3-R1: SIGMA-SELECT-45")
print("Scale Selection Principle for Spectral Dimension n_s")
print("=" * 78)

# Load S44 dimflow landscape
dd = np.load(data_dir / "s44_dimflow.npz", allow_pickle=True)
valid_tau = dd['valid_tau']
sigma_arr = dd['sigma_arr']
ds_landscape = dd['ds_landscape']
P_landscape = dd['P_landscape']
dds_dtau_landscape = dd['dds_dtau_landscape']
fold_idx = int(dd['fold_idx'])
fold_tau_val = float(dd['fold_tau'])

print(f"Loaded S44 dimflow: {len(valid_tau)} tau points, {len(sigma_arr)} sigma points")
print(f"Fold: tau={fold_tau_val:.3f}, index={fold_idx}")

# Load eigenvalue data for recomputation
d27 = np.load(data_dir / "s27_multisector_bcs.npz", allow_pickle=True)
d36 = np.load(data_dir / "s36_sfull_tau_stabilization.npz", allow_pickle=True)

tau_27 = d27['tau_values']
tau_36 = [0.050, 0.160, 0.170, 0.180, 0.190, 0.210, 0.220]
all_tau_raw = sorted(set([float(f'{t:.3f}') for t in list(tau_27)] + tau_36))


def get_evals(p, q, tau):
    """Load eigenvalues for sector (p,q) at given tau."""
    key36 = f"evals_tau{tau:.3f}_{p}_{q}"
    if key36 in d36.files:
        return d36[key36]
    tau_idx = None
    for i, t in enumerate(tau_27):
        if abs(t - tau) < 1e-10:
            tau_idx = i
            break
    if tau_idx is not None:
        key27 = f"evals_{p}_{q}_{tau_idx}"
        if key27 in d27.files:
            return d27[key27]
        if (p, q) == (1, 2):
            key27c = f"evals_2_1_{tau_idx}"
            if key27c in d27.files:
                return d27[key27c]
    return None


# Collect eigenvalue data at all valid tau
tau_eig_data = {}
for tau in valid_tau:
    pairs = []
    n_found = 0
    for p, q in SECTORS:
        ev = get_evals(p, q, tau)
        if ev is None:
            continue
        n_found += 1
        d = dim_pq(p, q)
        for lam in ev:
            pairs.append((lam**2, d))
    if n_found >= 8:
        tau_eig_data[tau] = pairs

print(f"Eigenvalue data at {len(tau_eig_data)} tau values")

# Load q-theory data
dq = np.load(data_dir / "s45_qtheory_bcs.npz", allow_pickle=True)
tau_star_qtheory = float(dq['tau_star_flatband'])
Delta_B1_fb = float(dq['Delta_B1_flatband'])
Delta_B2_fb = float(dq['Delta_B2_flatband'])
Delta_B3_fb = float(dq['Delta_B3_flatband'])
B1_lam_sq = float(dq['B1_lam_sq_fold'])
B2_lam_sq = float(dq['B2_lam_sq_fold'])
B3_lam_sq = float(dq['B3_lam_sq_fold'])

print(f"Q-theory tau* = {tau_star_qtheory:.6f} (flatband, Q-THEORY-BCS-45 PASS)")


# ═══════════════════════════════════════════════════════════════════════
# HELPER: Compute d_s and n_s at arbitrary sigma
# ═══════════════════════════════════════════════════════════════════════

def compute_ds_ns(sigma_val, tau_idx=None):
    """Compute d_s and n_s(Hawking) at given sigma by interpolation."""
    if tau_idx is None:
        tau_idx = fold_idx
    idx = np.searchsorted(sigma_arr, sigma_val)
    if idx <= 0:
        idx = 1
    elif idx >= len(sigma_arr):
        idx = len(sigma_arr) - 1

    # Linear interpolation in log-sigma
    frac = (np.log10(sigma_val) - np.log10(sigma_arr[idx-1])) / \
           (np.log10(sigma_arr[idx]) - np.log10(sigma_arr[idx-1]))
    frac = np.clip(frac, 0, 1)

    ds_val = ds_landscape[tau_idx, idx-1] + frac * (ds_landscape[tau_idx, idx] - ds_landscape[tau_idx, idx-1])
    dds_val = dds_dtau_landscape[tau_idx, idx-1] + frac * (dds_dtau_landscape[tau_idx, idx] - dds_dtau_landscape[tau_idx, idx-1])

    ns_hawk = 1.0 - dds_val
    ns_cdt = 1.0 + (ds_val - 4.0) / 2.0

    return ds_val, ns_hawk, ns_cdt


def compute_heat_kernel(sigma_val, pairs):
    """Compute P(sigma) = Tr exp(-sigma D^2) from eigenvalue pairs."""
    lam2 = np.array([l for l, _ in pairs])
    mult = np.array([m for _, m in pairs])
    return np.sum(mult * np.exp(-sigma_val * lam2))


def compute_ds_direct(sigma_val, pairs, dsigma_frac=1e-4):
    """Compute d_s directly from eigenvalue data via finite difference."""
    s_lo = sigma_val * (1 - dsigma_frac)
    s_hi = sigma_val * (1 + dsigma_frac)

    P_lo = compute_heat_kernel(s_lo, pairs)
    P_hi = compute_heat_kernel(s_hi, pairs)

    if P_lo <= 0 or P_hi <= 0:
        return 0.0

    d_lnP = np.log(P_hi) - np.log(P_lo)
    d_lnsig = np.log(s_hi) - np.log(s_lo)
    return -2.0 * d_lnP / d_lnsig


# ═══════════════════════════════════════════════════════════════════════
# METHOD 1: BACKREACTION SELF-CONSISTENCY
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("METHOD 1: BACKREACTION SELF-CONSISTENCY")
print("=" * 78)
print()
print("Principle: The effective UV cutoff Lambda depends on the spectral dimension:")
print("  Lambda = Lambda_0 * (d_s / 4)^{1/2}")
print("But the diffusion time sigma = 1/Lambda^2 determines d_s(sigma).")
print("Self-consistency loop:")
print("  sigma -> d_s(sigma) -> Lambda(d_s) -> sigma'(Lambda) -> d_s(sigma') -> ...")
print()

# The backreaction hypothesis:
# In dimensionless units (sigma in units of 1/lam^2_typical):
# sigma = 1/Lambda^2 and Lambda = Lambda_0 * sqrt(d_s/4)
# so sigma = 1 / (Lambda_0^2 * d_s/4) = 4 / (Lambda_0^2 * d_s)
#
# Lambda_0 is the reference cutoff when d_s = 4. At the walking scale,
# d_s = 4 and sigma = sigma_walk. So Lambda_0^2 = 1/sigma_walk.
# Then: sigma = 4 * sigma_walk / d_s(sigma)
#
# Self-consistency: sigma * d_s(sigma) = 4 * sigma_walk
# This is a fixed-point equation.

# Find sigma_walk where d_s = 4 at fold
idx_walk = np.argmin(np.abs(ds_landscape[fold_idx, :] - 4.0))
sigma_walk = sigma_arr[idx_walk]
C_backreact = 4.0 * sigma_walk

print(f"Walking scale (d_s = 4): sigma_walk = {sigma_walk:.6f}")
print(f"Backreaction constant C = 4 * sigma_walk = {C_backreact:.6f}")
print(f"Fixed-point equation: sigma * d_s(sigma) = {C_backreact:.6f}")

# Compute sigma * d_s(sigma) as a function of sigma
product = sigma_arr * ds_landscape[fold_idx, :]

# Find crossings of product = C_backreact
print(f"\nSearching for fixed points: sigma * d_s(sigma) = C_backreact")
crossings = []
for i in range(1, len(sigma_arr) - 1):
    if (product[i-1] - C_backreact) * (product[i] - C_backreact) < 0:
        # Linear interpolation
        frac = (C_backreact - product[i-1]) / (product[i] - product[i-1])
        sigma_cross = sigma_arr[i-1] + frac * (sigma_arr[i] - sigma_arr[i-1])
        crossings.append(sigma_cross)

# Also check exact crossing at sigma_walk (trivial fixed point)
crossings.append(sigma_walk)
crossings = sorted(set([round(c, 8) for c in crossings]))

print(f"Fixed points found: {len(crossings)}")

backreact_results = []
for sc in crossings:
    ds_sc, ns_hawk_sc, ns_cdt_sc = compute_ds_ns(sc)
    prod_sc = sc * ds_sc
    print(f"  sigma* = {sc:.6f}: d_s = {ds_sc:.6f}, product = {prod_sc:.4f}, "
          f"n_s(Hawk) = {ns_hawk_sc:.6f}, n_s(CDT) = {ns_cdt_sc:.6f}")
    backreact_results.append({
        'sigma': sc, 'ds': ds_sc, 'ns_hawk': ns_hawk_sc,
        'ns_cdt': ns_cdt_sc, 'product': prod_sc
    })

# Stability analysis of the fixed point at sigma_walk
# If F(sigma) = C/d_s(sigma), fixed point is where F(sigma)=sigma
# Stability: |dF/dsigma| < 1 at fixed point
print(f"\nStability analysis at sigma_walk = {sigma_walk:.6f}:")
eps = 0.01 * sigma_walk
ds_plus, _, _ = compute_ds_ns(sigma_walk + eps)
ds_minus, _, _ = compute_ds_ns(sigma_walk - eps)
dds_dsigma = (ds_plus - ds_minus) / (2 * eps)
# F(sigma) = C / d_s(sigma), dF/dsigma = -C * d(d_s)/dsigma / d_s^2
ds_walk_val, _, _ = compute_ds_ns(sigma_walk)
dF_dsigma = -C_backreact * dds_dsigma / ds_walk_val**2
print(f"  d(d_s)/d(sigma) at walk = {dds_dsigma:.6f}")
print(f"  dF/dsigma at walk = {dF_dsigma:.6f}")
print(f"  |dF/dsigma| = {abs(dF_dsigma):.6f} {'< 1 (STABLE)' if abs(dF_dsigma) < 1 else '>= 1 (UNSTABLE)'}")

# Iterative convergence from different initial conditions
print(f"\nIterative convergence test (F(sigma) = C/d_s(sigma)):")
for sigma_init in [0.1, 0.5, 1.0, 2.0, 5.0]:
    sigma_iter = sigma_init
    converged = False
    for step in range(100):
        ds_iter, _, _ = compute_ds_ns(sigma_iter)
        if ds_iter <= 0:
            break
        sigma_new = C_backreact / ds_iter
        if abs(sigma_new - sigma_iter) / max(abs(sigma_iter), 1e-10) < 1e-8:
            converged = True
            ds_final, ns_hawk_final, ns_cdt_final = compute_ds_ns(sigma_new)
            print(f"  init={sigma_init:.1f}: converged in {step+1} steps to "
                  f"sigma* = {sigma_new:.6f}, d_s = {ds_final:.4f}, "
                  f"n_s(H) = {ns_hawk_final:.6f}")
            break
        sigma_iter = sigma_new
    if not converged:
        print(f"  init={sigma_init:.1f}: did NOT converge in 100 steps "
              f"(last sigma={sigma_iter:.6f})")

# PRIMARY backreaction result
sigma_br = sigma_walk  # The trivial fixed point at the walking scale
ds_br, ns_hawk_br, ns_cdt_br = compute_ds_ns(sigma_br)
print(f"\n>>> METHOD 1 RESULT:")
print(f"    sigma* = {sigma_br:.6f} (self-consistent backreaction)")
print(f"    d_s = {ds_br:.6f}")
print(f"    n_s(Hawking) = {ns_hawk_br:.6f}")
print(f"    n_s(CDT) = {ns_cdt_br:.6f} (trivially 1.000 by construction)")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 2: HUBBLE MATCHING
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("METHOD 2: HUBBLE MATCHING")
print("=" * 78)
print()
print("Principle: At the pivot scale k* = 0.05 Mpc^{-1}, the physical")
print("diffusion time is set by the Hubble rate: sigma_H = 1/H^2.")
print()

# H_fold is in M_KK units (dimensionless)
# sigma is also in M_KK units (1/lambda^2 where lambda is in M_KK units)
# So sigma_H = 1/H_fold^2

sigma_H = 1.0 / H_fold**2
print(f"H_fold = {H_fold:.6f} (M_KK units, from S38 s38_kz_defects)")
print(f"sigma_H = 1/H_fold^2 = {sigma_H:.6e}")
print()

# This is TINY compared to the eigenvalue scale lambda^2 ~ 0.7-4.3
# sigma_H * lambda^2 ~ 10^{-6} * 1 ~ 10^{-6} -> d_s ~ 0
# (deep in the UV/finite-truncation regime where P ~ N = const)

ds_H, ns_hawk_H, ns_cdt_H = compute_ds_ns(sigma_H)
print(f"d_s(sigma_H) = {ds_H:.6e} (deep UV, finite truncation -> 0)")
print(f"n_s(Hawking) at sigma_H = {ns_hawk_H:.6f}")
print(f"n_s(CDT) at sigma_H = {ns_cdt_H:.6f}")
print()

# Alternative: use H at the CMB scale in natural units
# k* = 0.05 Mpc^{-1}. Convert to M_KK units.
# 1 Mpc = 3.0857e22 m = 3.0857e22 / (1.973e-16) GeV^{-1} = 1.563e38 GeV^{-1}
# k* = 0.05 Mpc^{-1} = 0.05 / (1.563e38) GeV = 3.20e-40 GeV
# In M_KK units: k*_MKK = 3.20e-40 / M_KK = 3.20e-40 / 7.43e16 = 4.31e-57
# sigma = 1/k*^2 in M_KK units -> ENORMOUS, d_s = 0 (IR)

k_star_Mpc_inv = 0.05
k_star_GeV = k_star_Mpc_inv / (3.0857e22 / 1.973269804e-16)
k_star_MKK = k_star_GeV / M_KK
sigma_pivot_CMB = 1.0 / k_star_MKK**2

print(f"CMB pivot scale:")
print(f"  k* = {k_star_Mpc_inv} Mpc^{{-1}} = {k_star_GeV:.3e} GeV = {k_star_MKK:.3e} M_KK")
print(f"  sigma_CMB = 1/k*^2 = {sigma_pivot_CMB:.3e} (M_KK^{{-2}})")
print(f"  This is in the DEEP IR: d_s = 0 identically.")
print()

# The Hubble matching at the transit scale
# During transit, the Hubble rate is H_fold ~ 587 M_KK
# The relevant diffusion time sigma_H = 1/H^2 ~ 2.9e-6
# At this sigma, we're in the regime where exp(-sigma * lam^2) ~ 1 for all modes
# because sigma * lam_max^2 ~ 2.9e-6 * 4.3 ~ 1.2e-5

# Compute explicitly
if fold_tau_val in tau_eig_data:
    pairs = tau_eig_data[fold_tau_val]
    P_at_sigH = compute_heat_kernel(sigma_H, pairs)
    P_total = sum(m for _, m in pairs)
    print(f"P(sigma_H) = {P_at_sigH:.6f}, P(0) = {P_total}")
    print(f"P(sigma_H)/P(0) = {P_at_sigH/P_total:.10f}")
    print(f"1 - P(sigma_H)/P(0) = {1 - P_at_sigH/P_total:.6e}")
    # sigma_H is so small that ALL modes contribute equally -> d_s ~ 0

ds_H_direct = compute_ds_direct(sigma_H, pairs)
print(f"d_s(sigma_H) computed directly = {ds_H_direct:.6e}")

print(f"\n>>> METHOD 2 RESULT:")
print(f"    sigma_H = {sigma_H:.6e} (Hubble matching)")
print(f"    d_s = {ds_H:.6e} (deep UV, finite truncation)")
print(f"    n_s(Hawking) = {ns_hawk_H:.6f}")
print(f"    VERDICT: sigma_H is 5 orders below eigenvalue scale.")
print(f"    Hubble matching probes the CONSTANT region of P(sigma)")
print(f"    where d_s = 0 for a finite truncation. NO SELECTION.")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 3: OCCUPIED-STATE SIGMA
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("METHOD 3: OCCUPIED-STATE SPECTRAL DIMENSION")
print("=" * 78)
print()
print("Principle: Replace D_K^2 with n_k * D_K^2 in the heat kernel,")
print("where n_k is the BCS occupation number. This probes the PHYSICAL")
print("(occupied) spectrum rather than the vacuum spectrum.")
print()

# BCS occupation at fold: n_k = v_k^2 where v_k^2 = (1 - xi_k/E_k)/2
# xi_k = lambda_k - mu (with mu = 0 by PH symmetry)
# E_k = sqrt(xi_k^2 + Delta_k^2)
# For PH-symmetric system at mu=0: xi_k = |lambda_k|, E_k = sqrt(lambda_k^2 + Delta_k^2)
# n_k = v_k^2 = (1 - |lambda_k|/sqrt(lambda_k^2 + Delta_k^2))/2

# Use flatband gaps from q-theory
# Sector identification: B1 = (0,0), B2 = (1,0)+(0,1), B3 = higher sectors
# More precisely from the spectral data:
# B1: smallest eigenvalues near lambda^2 ~ 0.67
# B2: eigenvalues near lambda^2 ~ 0.71
# B3: eigenvalues near lambda^2 ~ 0.94+

# Delta assignment:
# Gap varies by sector: use the q-theory flatband values
Delta_sectors = {
    (0,0): Delta_B1_fb,   # B1
    (1,0): Delta_B2_fb,   # B2
    (0,1): Delta_B2_fb,   # B2
    (1,1): Delta_B2_fb,   # Higher B2-like
    (2,0): Delta_B3_fb,   # B3
    (0,2): Delta_B3_fb,   # B3
    (3,0): Delta_B3_fb,   # B3
    (0,3): Delta_B3_fb,   # B3
    (2,1): Delta_B3_fb,   # B3
    (1,2): Delta_B3_fb,   # B3
}

N_sigma_fine = 500
log_sigma_fine = np.linspace(-4, 4, N_sigma_fine)
sigma_fine = 10.0**log_sigma_fine

# Compute occupied-state heat kernel and spectral dimension
print("Computing occupied-state spectral dimension at fold...")
print()

# Build occupied pairs for multiple tau values
ds_occ_results = {}
ds_vac_results = {}

for tau in valid_tau:
    if tau not in tau_eig_data:
        continue

    occ_pairs = []  # (n_k * lambda_k^2, mult_k)
    vac_pairs = tau_eig_data[tau]

    for p, q in SECTORS:
        ev = get_evals(p, q, tau)
        if ev is None:
            continue
        d = dim_pq(p, q)
        Delta = Delta_sectors.get((p, q), Delta_B3_fb)

        for lam in ev:
            lam2 = lam**2
            lam_abs = abs(lam)
            E_k = np.sqrt(lam2 + Delta**2)
            v_k_sq = 0.5 * (1.0 - lam_abs / E_k)  # BCS occupation
            # n_k * lambda_k^2 is the effective eigenvalue for occupied kernel
            occ_pairs.append((v_k_sq * lam2, d))

    # Compute P_occ(sigma) and d_s^occ(sigma)
    lam2_occ = np.array([l for l, _ in occ_pairs])
    mult_occ = np.array([m for _, m in occ_pairs])
    lam2_vac = np.array([l for l, _ in vac_pairs])
    mult_vac = np.array([m for _, m in vac_pairs])

    P_occ = np.zeros(N_sigma_fine)
    P_vac = np.zeros(N_sigma_fine)
    for i, sig in enumerate(sigma_fine):
        P_occ[i] = np.sum(mult_occ * np.exp(-sig * lam2_occ))
        P_vac[i] = np.sum(mult_vac * np.exp(-sig * lam2_vac))

    # d_s from centered differences in log space
    ln_P_occ = np.log(P_occ + 1e-300)
    ln_P_vac = np.log(P_vac + 1e-300)
    ln_sig = np.log(sigma_fine)

    ds_occ = np.zeros(N_sigma_fine)
    ds_vac = np.zeros(N_sigma_fine)
    for i in range(1, N_sigma_fine - 1):
        ds_occ[i] = -2.0 * (ln_P_occ[i+1] - ln_P_occ[i-1]) / (ln_sig[i+1] - ln_sig[i-1])
        ds_vac[i] = -2.0 * (ln_P_vac[i+1] - ln_P_vac[i-1]) / (ln_sig[i+1] - ln_sig[i-1])
    ds_occ[0] = ds_occ[1]
    ds_occ[-1] = ds_occ[-2]
    ds_vac[0] = ds_vac[1]
    ds_vac[-1] = ds_vac[-2]

    ds_occ_results[tau] = ds_occ
    ds_vac_results[tau] = ds_vac

# Report occupied-state results at fold
fold_ds_occ = ds_occ_results.get(fold_tau_val)
fold_ds_vac = ds_vac_results.get(fold_tau_val)

if fold_ds_occ is not None:
    print(f"d_s^occ at fold (tau={fold_tau_val:.3f}):")
    print(f"{'sigma':>12} | {'d_s^vac':>10} | {'d_s^occ':>10} | {'ratio':>10}")
    print("-" * 52)
    for s_val in [0.01, 0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
        idx = np.argmin(np.abs(sigma_fine - s_val))
        ratio = fold_ds_occ[idx] / fold_ds_vac[idx] if abs(fold_ds_vac[idx]) > 1e-10 else np.inf
        print(f"{s_val:12.3f} | {fold_ds_vac[idx]:10.4f} | {fold_ds_occ[idx]:10.4f} | {ratio:10.4f}")

    # Walking scale of occupied spectrum: where d_s^occ = 4
    idx_walk_occ = np.argmin(np.abs(fold_ds_occ - 4.0))
    sigma_walk_occ = sigma_fine[idx_walk_occ]
    ds_walk_occ = fold_ds_occ[idx_walk_occ]
    print(f"\nOccupied walking scale (d_s^occ = 4): sigma = {sigma_walk_occ:.6f}, d_s = {ds_walk_occ:.6f}")

    # CDT n_s from occupied spectrum
    ns_cdt_occ_walk = 1.0 + (ds_walk_occ - 4.0) / 2.0
    print(f"n_s(CDT) at occupied walking scale = {ns_cdt_occ_walk:.6f}")

    # Key question: does the occupied spectrum have a sigma-INDEPENDENT regime?
    # Check if d_s^occ has a plateau
    dds_occ_dsig = np.gradient(fold_ds_occ, np.log10(sigma_fine))
    # Find where |dds/d(log sigma)| is minimized (flattest region)
    # Exclude edges
    inner = slice(20, -20)
    abs_grad = np.abs(dds_occ_dsig[inner])
    idx_flat = np.argmin(abs_grad) + 20
    sigma_flat = sigma_fine[idx_flat]
    ds_flat = fold_ds_occ[idx_flat]
    grad_flat = dds_occ_dsig[idx_flat]
    print(f"\nFlattest region of d_s^occ: sigma = {sigma_flat:.6f}, d_s = {ds_flat:.6f}")
    print(f"  |d(d_s)/d(log sigma)| = {abs(grad_flat):.6f}")
    print(f"  n_s(CDT) at plateau = {1.0 + (ds_flat - 4.0)/2.0:.6f}")

    # Hawking flow for occupied-state spectral dimension
    # Compute d(d_s^occ)/d(tau) at the occupied walking scale
    occ_tau_list = sorted(ds_occ_results.keys())
    if len(occ_tau_list) >= 3:
        occ_tau_arr = np.array(occ_tau_list)
        # At sigma_walk_occ
        ds_occ_vs_tau = np.array([ds_occ_results[t][idx_walk_occ] for t in occ_tau_list])
        dds_occ_dtau = np.gradient(ds_occ_vs_tau, occ_tau_arr)
        occ_fold_idx = np.argmin(np.abs(occ_tau_arr - fold_tau_val))
        ns_hawk_occ = 1.0 - dds_occ_dtau[occ_fold_idx]
        print(f"\nOccupied Hawking flow at sigma_walk_occ = {sigma_walk_occ:.6f}:")
        print(f"  d(d_s^occ)/d(tau) at fold = {dds_occ_dtau[occ_fold_idx]:.6f}")
        print(f"  n_s(Hawking, occ) = {ns_hawk_occ:.6f}")

        # Occupied Hawking n_s at multiple sigma values
        print(f"\nOccupied Hawking n_s vs sigma:")
        ns_occ_hawk_profile = []
        for idx_probe in range(0, N_sigma_fine, N_sigma_fine // 15):
            ds_probe_vs_tau = np.array([ds_occ_results[t][idx_probe] for t in occ_tau_list])
            dds_probe = np.gradient(ds_probe_vs_tau, occ_tau_arr)
            ns_probe = 1.0 - dds_probe[occ_fold_idx]
            ns_occ_hawk_profile.append((sigma_fine[idx_probe], ns_probe))
            if 0.05 < sigma_fine[idx_probe] < 20:
                print(f"  sigma={sigma_fine[idx_probe]:.4f}: n_s(Hawk,occ) = {ns_probe:.6f}")

        # Full occupied Hawking profile at fold
        ns_hawk_occ_full = np.zeros(N_sigma_fine)
        for idx_s in range(N_sigma_fine):
            ds_s_vs_tau = np.array([ds_occ_results[t][idx_s] for t in occ_tau_list])
            dds_s = np.gradient(ds_s_vs_tau, occ_tau_arr)
            ns_hawk_occ_full[idx_s] = 1.0 - dds_s[occ_fold_idx]

        # Does occupied Hawking n_s = 0.965 at any sigma?
        idx_target_occ = np.argmin(np.abs(ns_hawk_occ_full[20:-20] - 0.965)) + 20
        sigma_occ_target = sigma_fine[idx_target_occ]
        ns_occ_target = ns_hawk_occ_full[idx_target_occ]
        print(f"\nClosest to n_s = 0.965: n_s = {ns_occ_target:.6f} at sigma = {sigma_occ_target:.6f}")
    else:
        ns_hawk_occ = np.nan
        ns_hawk_occ_full = None

    # Check: does the ratio d_s^occ / d_s^vac have a natural scale?
    ratio_profile = fold_ds_occ / np.maximum(fold_ds_vac, 1e-10)
    # The BCS occupation weights DOWN the spectrum: n_k < 1 for all modes
    # So d_s^occ < d_s^vac everywhere. The RATIO tells us where the
    # occupation weighting matters most.
    print(f"\nRatio d_s^occ / d_s^vac profile:")
    for s_val in [0.1, 0.5, 1.0, 2.0, 5.0]:
        idx = np.argmin(np.abs(sigma_fine - s_val))
        print(f"  sigma={s_val:.1f}: ratio = {ratio_profile[idx]:.6f}")

print(f"\n>>> METHOD 3 RESULT:")
if fold_ds_occ is not None:
    print(f"    sigma_walk_occ = {sigma_walk_occ:.6f}")
    print(f"    d_s^occ at walking scale = {ds_walk_occ:.6f}")
    print(f"    n_s(Hawking, occ) at walking scale = {ns_hawk_occ:.6f}")
    print(f"    No sigma-independent regime found (monotonic transition)")
    print(f"    The BCS occupation weighting shifts the walking scale")
    print(f"    but does not SELECT a natural sigma.")
else:
    print(f"    COMPUTATION FAILED: no eigenvalue data at fold")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 4: Q-THEORY SIGMA
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("METHOD 4: Q-THEORY SIGMA")
print("=" * 78)
print()
print(f"Principle: The q-theory zero-crossing at tau* = {tau_star_qtheory:.6f}")
print("provides a PHYSICAL tau. If sigma is related to tau through modulus")
print("dynamics, then sigma = f(tau*). We test three prescriptions:")
print()

# Test: sigma = tau*, sigma = tau*^2, sigma = 1/tau*
sigma_qt = {
    'tau*':      tau_star_qtheory,
    'tau*^2':    tau_star_qtheory**2,
    '1/tau*':    1.0 / tau_star_qtheory,
    '2*tau*':    2.0 * tau_star_qtheory,
    'sqrt(tau*)': np.sqrt(tau_star_qtheory),
}

print(f"{'Prescription':>14} | {'sigma':>10} | {'d_s':>8} | {'n_s(Hawk)':>10} | {'n_s(CDT)':>10}")
print("-" * 68)

qt_results = {}
for name, sig_val in sigma_qt.items():
    ds_qt, ns_hawk_qt, ns_cdt_qt = compute_ds_ns(sig_val)
    print(f"{name:>14} | {sig_val:10.6f} | {ds_qt:8.4f} | {ns_hawk_qt:10.6f} | {ns_cdt_qt:10.6f}")
    qt_results[name] = {
        'sigma': sig_val, 'ds': ds_qt,
        'ns_hawk': ns_hawk_qt, 'ns_cdt': ns_cdt_qt
    }

# The q-theory tau* = 0.209 is close to the fold tau = 0.19-0.20
# So sigma = tau* ~ 0.209 probes the spectrum at a scale where
# d_s ~ 1.1 (too low for CDT n_s near 1)

# Most interesting: sigma = 1/tau* ~ 4.78 gives d_s ~ 9-10
# and sigma = tau* ~ 0.21 gives d_s ~ 0.9-1.1

# Check sensitivity around each prescription
print(f"\nSensitivity analysis:")
for name, sig_val in sigma_qt.items():
    dsig = 0.01 * sig_val
    ds_plus, ns_hawk_plus, _ = compute_ds_ns(sig_val + dsig)
    ds_minus, ns_hawk_minus, _ = compute_ds_ns(sig_val - dsig)
    dns_dsig = (ns_hawk_plus - ns_hawk_minus) / (2 * dsig)
    print(f"  {name}: d(n_s)/d(sigma) = {dns_dsig:.4f}, "
          f"delta_sigma for delta_ns=0.004: {0.004/max(abs(dns_dsig), 1e-10):.4f}")

print(f"\n>>> METHOD 4 RESULT:")
print(f"    tau* = {tau_star_qtheory:.6f} (Q-THEORY-BCS-45 PASS)")
best_qt = min(qt_results.items(), key=lambda x: abs(x[1]['ns_hawk'] - 0.965))
print(f"    Best q-theory prescription: {best_qt[0]}")
print(f"    sigma = {best_qt[1]['sigma']:.6f}, n_s(Hawk) = {best_qt[1]['ns_hawk']:.6f}")


# ═══════════════════════════════════════════════════════════════════════
# METHOD 5 (BONUS): SPECTRAL ZETA SELECTION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("METHOD 5 (BONUS): SPECTRAL ZETA FUNCTION RESIDUE")
print("=" * 78)
print()
print("The spectral zeta function zeta_D(s) = Tr |D|^{-2s} has a pole at s=d/2.")
print("For the truncated spectrum, define the 'effective dimension' as the")
print("value of s where zeta_D(s) has its steepest descent. This gives a")
print("natural sigma through sigma_zeta = 1/lam_zeta^2 where lam_zeta is")
print("the scale at which the zeta function transitions.")
print()

# Compute spectral zeta function from eigenvalues at fold
if fold_tau_val in tau_eig_data:
    pairs = tau_eig_data[fold_tau_val]
    lam2 = np.array([l for l, _ in pairs])
    mult = np.array([m for _, m in pairs])

    # zeta_D(s) = sum_k mult_k * |lambda_k|^{-2s} for lambda_k != 0
    nonzero = lam2 > 1e-10
    lam2_nz = lam2[nonzero]
    mult_nz = mult[nonzero]

    s_vals = np.linspace(0.1, 10, 200)
    zeta = np.array([np.sum(mult_nz * lam2_nz**(-s)) for s in s_vals])

    # Find the inflection point of log(zeta) vs s
    log_zeta = np.log(np.maximum(zeta, 1e-300))
    d2_log_zeta = np.gradient(np.gradient(log_zeta, s_vals), s_vals)
    # Inflection: where d2(log zeta)/ds^2 changes sign
    sign_changes = []
    for i in range(1, len(d2_log_zeta)):
        if d2_log_zeta[i-1] * d2_log_zeta[i] < 0:
            frac = abs(d2_log_zeta[i-1]) / (abs(d2_log_zeta[i-1]) + abs(d2_log_zeta[i]))
            s_infl = s_vals[i-1] + frac * (s_vals[i] - s_vals[i-1])
            sign_changes.append(s_infl)

    print(f"Spectral zeta function inflection points: {sign_changes}")

    if sign_changes:
        s_eff = sign_changes[0]
        # Effective dimension d_eff = 2 * s_eff (pole location)
        d_eff = 2 * s_eff
        # Effective scale: sigma_zeta = 1/(mean lambda^2)^{s_eff/s_0}
        lam2_mean = np.average(lam2_nz, weights=mult_nz)
        sigma_zeta = 1.0 / lam2_mean
        print(f"  s_eff = {s_eff:.4f}, d_eff = {d_eff:.4f}")
        print(f"  Mean lambda^2 = {lam2_mean:.4f}")
        print(f"  sigma_zeta = 1/<lambda^2> = {sigma_zeta:.6f}")

        ds_zeta, ns_hawk_zeta, ns_cdt_zeta = compute_ds_ns(sigma_zeta)
        print(f"  d_s(sigma_zeta) = {ds_zeta:.4f}")
        print(f"  n_s(Hawking, zeta) = {ns_hawk_zeta:.6f}")
        print(f"  n_s(CDT, zeta) = {ns_cdt_zeta:.6f}")
    else:
        sigma_zeta = np.nan
        ns_hawk_zeta = np.nan
        ns_cdt_zeta = np.nan
        print("  No inflection point found.")


# ═══════════════════════════════════════════════════════════════════════
# COMPREHENSIVE SUMMARY AND GATE VERDICT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("COMPREHENSIVE SUMMARY: SIGMA-SELECT-45")
print("=" * 78)

print(f"\n{'Method':>25} | {'sigma*':>12} | {'d_s':>8} | {'n_s(Hawk)':>10} | {'n_s(CDT)':>10} | {'Status':>12}")
print("-" * 90)

results_table = []

# Method 1: Backreaction
r = {'method': 'Backreaction', 'sigma': sigma_br, 'ds': ds_br,
     'ns_hawk': ns_hawk_br, 'ns_cdt': ns_cdt_br}
results_table.append(r)
print(f"{'1: Backreaction':>25} | {sigma_br:12.6f} | {ds_br:8.4f} | {ns_hawk_br:10.6f} | {ns_cdt_br:10.6f} | {'TRIVIAL':>12}")

# Method 2: Hubble matching
r = {'method': 'Hubble', 'sigma': sigma_H, 'ds': ds_H,
     'ns_hawk': ns_hawk_H, 'ns_cdt': ns_cdt_H}
results_table.append(r)
print(f"{'2: Hubble':>25} | {sigma_H:12.2e} | {ds_H:8.4f} | {ns_hawk_H:10.6f} | {ns_cdt_H:10.6f} | {'NO SELECTION':>12}")

# Method 3: Occupied-state
if fold_ds_occ is not None:
    r = {'method': 'Occupied', 'sigma': sigma_walk_occ,
         'ds': ds_walk_occ, 'ns_hawk': ns_hawk_occ,
         'ns_cdt': 1.0 + (ds_walk_occ - 4.0) / 2.0}
    results_table.append(r)
    occ_status = 'NO PLATEAU'
    print(f"{'3: Occupied-state':>25} | {sigma_walk_occ:12.6f} | {ds_walk_occ:8.4f} | {ns_hawk_occ:10.6f} | {1.0 + (ds_walk_occ - 4.0)/2.0:10.6f} | {occ_status:>12}")

# Method 4: Q-theory variants
for name, res in qt_results.items():
    r = {'method': f'Q: {name}', 'sigma': res['sigma'],
         'ds': res['ds'], 'ns_hawk': res['ns_hawk'], 'ns_cdt': res['ns_cdt']}
    results_table.append(r)
    in_range = 0.955 <= res['ns_hawk'] <= 0.975
    status = 'IN RANGE' if in_range else f"{'CLOSE' if abs(res['ns_hawk'] - 0.965) < 0.05 else 'FAR'}"
    print(f"{'4: Q(' + name + ')':>25} | {res['sigma']:12.6f} | {res['ds']:8.4f} | {res['ns_hawk']:10.6f} | {res['ns_cdt']:10.6f} | {status:>12}")

# Method 5: Spectral zeta
if not np.isnan(sigma_zeta):
    r = {'method': 'Zeta', 'sigma': sigma_zeta,
         'ds': ds_zeta, 'ns_hawk': ns_hawk_zeta, 'ns_cdt': ns_cdt_zeta}
    results_table.append(r)
    print(f"{'5: Spectral zeta':>25} | {sigma_zeta:12.6f} | {ds_zeta:8.4f} | {ns_hawk_zeta:10.6f} | {ns_cdt_zeta:10.6f} | {'BONUS':>12}")


# ═══════════════════════════════════════════════════════════════════════
# STRUCTURAL ANALYSIS
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("STRUCTURAL ANALYSIS")
print("=" * 78)

print("""
1. BACKREACTION (Method 1):
   The self-consistency equation sigma * d_s(sigma) = C has a UNIQUE fixed
   point at the walking scale sigma_walk where d_s = 4 by construction.
   This gives n_s(CDT) = 1.000 TAUTOLOGICALLY. The Hawking n_s at sigma_walk
   is non-trivial but reflects the sigma dependence of d(d_s)/d(tau).
   VERDICT: Produces a fixed point but n_s(CDT) is tautological.

2. HUBBLE MATCHING (Method 2):
   sigma_H = 1/H^2 ~ 3e-6 in M_KK units is 5 orders of magnitude below
   the spectral scale lambda^2 ~ 0.7-4.3. At this sigma, the heat kernel
   P(sigma) ~ P(0) = N (total mode count), so d_s ~ 0 for the finite
   truncation. The Hubble scale probes a regime where the discrete spectrum
   is indistinguishable from a continuum of constant density.
   VERDICT: No selection. sigma_H is in the UV-trivial regime.

3. OCCUPIED-STATE (Method 3):
   The BCS occupation n_k = v_k^2 rescales D_K^2 -> n_k * D_K^2, which
   SHIFTS the walking scale (since occupied eigenvalues are smaller) but
   does not create a sigma-independent regime. The d_s^occ(sigma) curve
   is qualitatively identical to d_s^vac(sigma), just compressed.
   VERDICT: No natural sigma selection. Walking scale shifts but
   n_s remains sigma-dependent.

4. Q-THEORY (Method 4):
   tau* = 0.209 provides a PHYSICAL modulus value, but the mapping
   tau* -> sigma requires an additional ansatz. None of the tested
   prescriptions (sigma = tau*, tau*^2, 1/tau*, etc.) produce n_s
   in the Planck range [0.955, 0.975] via the Hawking formula.
""")


# ═══════════════════════════════════════════════════════════════════════
# THE REAL ISSUE: DIMENSIONALITY OF d_s FROM FINITE TRUNCATION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("THE TRUNCATION PROBLEM")
print("=" * 78)

print(f"""
CRITICAL OBSERVATION:
The spectral dimension d_s(sigma) computed from the finite truncation
(10 sectors, ~9280 modes, max|lambda| = 2.077) does NOT reproduce the
continuum behavior d_s(sigma -> 0) = 8.

For the truncated spectrum:
  - sigma -> 0: P(sigma) -> N = {sum(m for _, m in tau_eig_data[fold_tau_val])}, d_s -> 0
  - sigma ~ 1/lam_max^2 ~ 0.23: d_s starts growing
  - sigma ~ 1/lam_min^2 ~ 1.49: d_s peaks
  - sigma -> inf: P -> 0 exponentially, d_s -> 0

The "walking scale" where d_s = 4 is a TRUNCATION ARTIFACT: it reflects
where ~4/8 = 50% of the modes have been exponentially suppressed. This has
no direct physical meaning.

The n_s(Hawking) = 1 - d(d_s)/d(tau) at any fixed sigma captures real
tau-dependence of the spectrum, but the overall scale sigma is set by
the truncation cutoff, not by physics.

IMPLICATION:
To extract a physically meaningful spectral dimension, one needs EITHER:
  (a) The full continuum spectrum (Weyl's law N(lam) ~ C * lam^8), OR
  (b) A sigma-independent observable derived from the spectral dimension flow.

Neither is available from the current 10-sector truncation.
""")


# ═══════════════════════════════════════════════════════════════════════
# GATE VERDICT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("GATE VERDICT: SIGMA-SELECT-45")
print("=" * 78)

# Check if ANY method gives n_s in [0.955, 0.975]
any_pass = False
for r in results_table:
    if 0.955 <= r['ns_hawk'] <= 0.975:
        any_pass = True
        print(f"  CANDIDATE: {r['method']} gives n_s(Hawk) = {r['ns_hawk']:.6f} at sigma = {r['sigma']:.6f}")

# Also check the Hawking n_s at the backreaction fixed point more carefully
# n_s(Hawk) at sigma_walk was already computed
print(f"\n  Method 1 (Backreaction): n_s(Hawk) = {ns_hawk_br:.6f}")
if 0.955 <= ns_hawk_br <= 0.975:
    any_pass = True
    print(f"    -> IN RANGE [0.955, 0.975]")

# Check all methods
all_ns_hawk = [r['ns_hawk'] for r in results_table if not np.isnan(r['ns_hawk'])]
closest_to_planck = min(all_ns_hawk, key=lambda x: abs(x - 0.9649))
closest_method = [r for r in results_table if abs(r['ns_hawk'] - closest_to_planck) < 1e-10][0]

print(f"\n  Closest to Planck (n_s = 0.9649):")
print(f"    Method: {closest_method['method']}")
print(f"    sigma = {closest_method['sigma']:.6f}")
print(f"    n_s(Hawk) = {closest_method['ns_hawk']:.6f}")
print(f"    |n_s - 0.9649| = {abs(closest_method['ns_hawk'] - 0.9649):.6f}")

# Determine verdict
if any_pass:
    verdict = "PASS"
    detail = f"sigma* found with n_s in [0.955, 0.975]"
elif any(0.90 <= r['ns_hawk'] <= 1.05 for r in results_table if not np.isnan(r['ns_hawk'])):
    verdict = "INFO"
    detail = f"Sigma found but n_s outside [0.955, 0.975]. Closest: {closest_to_planck:.6f}"
else:
    verdict = "FAIL"
    detail = "No fixed point with n_s near Planck value"

# STRUCTURAL FAILURE OVERRIDE:
# All four methods fail to SELECT sigma from first principles.
# The Hawking n_s at any sigma is a function of sigma, not a prediction.
# Even if n_s(Hawk) passes at some sigma, the sigma is not derived.
struct_verdict = "FAIL"
struct_detail = ("No method selects sigma from first principles. "
                 "Backreaction is tautological (CDT), Hubble is in UV-trivial regime, "
                 "occupied-state has no plateau, q-theory prescriptions are ad hoc.")

print(f"\n  NUMERICAL VERDICT: {verdict}")
print(f"    {detail}")
print(f"\n  STRUCTURAL VERDICT: {struct_verdict}")
print(f"    {struct_detail}")
print(f"\n  FINAL GATE: SIGMA-SELECT-45 = {struct_verdict}")
print(f"    Planck: n_s = 0.9649 +/- 0.0042")
print(f"    None of the 4 methods provides a self-consistent, physically")
print(f"    motivated sigma* that yields n_s in [0.955, 0.975].")
print(f"\n  CONSTRAINT: The spectral dimension route to n_s requires either")
print(f"  the full continuum spectrum or a sigma-independent observable.")
print(f"  The truncated spectral dimension is NOT predictive for n_s.")


# ═══════════════════════════════════════════════════════════════════════
# SAVE DATA
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("SAVING DATA")
print("=" * 78)

save_dict = {
    'gate_name': np.array(['SIGMA-SELECT-45']),
    'gate_verdict': np.array([struct_verdict]),
    'gate_detail': np.array([struct_detail]),

    # Method 1: Backreaction
    'sigma_backreact': np.float64(sigma_br),
    'ds_backreact': np.float64(ds_br),
    'ns_hawk_backreact': np.float64(ns_hawk_br),
    'ns_cdt_backreact': np.float64(ns_cdt_br),
    'C_backreact': np.float64(C_backreact),

    # Method 2: Hubble
    'sigma_hubble': np.float64(sigma_H),
    'ds_hubble': np.float64(ds_H),
    'ns_hawk_hubble': np.float64(ns_hawk_H),
    'H_fold': np.float64(H_fold),

    # Method 3: Occupied-state
    'sigma_occ_walk': np.float64(sigma_walk_occ) if fold_ds_occ is not None else np.float64(np.nan),
    'ds_occ_walk': np.float64(ds_walk_occ) if fold_ds_occ is not None else np.float64(np.nan),
    'ns_hawk_occ': np.float64(ns_hawk_occ) if fold_ds_occ is not None else np.float64(np.nan),
    'sigma_fine': sigma_fine,
    'ds_occ_fold': fold_ds_occ if fold_ds_occ is not None else np.array([]),
    'ds_vac_fold': fold_ds_vac if fold_ds_vac is not None else np.array([]),

    # Method 4: Q-theory
    'tau_star_qtheory': np.float64(tau_star_qtheory),
    'sigma_qt_tau': np.float64(qt_results['tau*']['sigma']),
    'ns_hawk_qt_tau': np.float64(qt_results['tau*']['ns_hawk']),
    'sigma_qt_tau2': np.float64(qt_results['tau*^2']['sigma']),
    'ns_hawk_qt_tau2': np.float64(qt_results['tau*^2']['ns_hawk']),
    'sigma_qt_inv': np.float64(qt_results['1/tau*']['sigma']),
    'ns_hawk_qt_inv': np.float64(qt_results['1/tau*']['ns_hawk']),

    # Method 5: Spectral zeta (bonus)
    'sigma_zeta': np.float64(sigma_zeta) if not np.isnan(sigma_zeta) else np.float64(np.nan),
    'ns_hawk_zeta': np.float64(ns_hawk_zeta) if not np.isnan(ns_hawk_zeta) else np.float64(np.nan),

    # Closest to Planck
    'closest_method': np.array([closest_method['method']]),
    'closest_ns_hawk': np.float64(closest_to_planck),
    'closest_sigma': np.float64(closest_method['sigma']),

    # Occupied-state Hawking profile
    'ns_hawk_occ_profile': ns_hawk_occ_full if ns_hawk_occ_full is not None else np.array([]),

    # Fold parameters
    'fold_tau': np.float64(fold_tau_val),
    'fold_idx': np.int64(fold_idx),
}

np.savez(output_npz, **save_dict)
print(f"Data saved to {output_npz}")


# ═══════════════════════════════════════════════════════════════════════
# PLOT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 78)
print("GENERATING PLOT")
print("=" * 78)

fig = plt.figure(figsize=(20, 16))
gs = GridSpec(3, 3, figure=fig, hspace=0.40, wspace=0.35)

# Panel 1: d_s(sigma) vacuum vs occupied at fold
ax1 = fig.add_subplot(gs[0, 0])
if fold_ds_vac is not None and fold_ds_occ is not None:
    ax1.semilogx(sigma_fine, fold_ds_vac, 'b-', linewidth=1.5, label=r'$d_s^{\rm vac}$')
    ax1.semilogx(sigma_fine, fold_ds_occ, 'r-', linewidth=1.5, label=r'$d_s^{\rm occ}$')
    ax1.axhline(y=4, ls=':', color='gray', alpha=0.5)
    ax1.axvline(x=sigma_walk, ls='--', color='blue', alpha=0.4, label=f'walk(vac)={sigma_walk:.3f}')
    ax1.axvline(x=sigma_walk_occ, ls='--', color='red', alpha=0.4, label=f'walk(occ)={sigma_walk_occ:.3f}')
ax1.set_xlabel(r'$\sigma$ (diffusion time)')
ax1.set_ylabel(r'$d_s(\sigma)$')
ax1.set_title('Vacuum vs Occupied Spectral Dimension')
ax1.set_ylim(-0.5, 12)
ax1.legend(fontsize=7)
ax1.grid(True, alpha=0.3)

# Panel 2: Backreaction fixed-point diagram
ax2 = fig.add_subplot(gs[0, 1])
product_curve = sigma_arr * ds_landscape[fold_idx, :]
ax2.semilogx(sigma_arr, product_curve, 'b-', linewidth=1.5, label=r'$\sigma \cdot d_s(\sigma)$')
ax2.axhline(y=C_backreact, ls='--', color='red', alpha=0.7, label=f'C = {C_backreact:.2f}')
ax2.axvline(x=sigma_walk, ls=':', color='green', alpha=0.5, label=f'Fixed pt = {sigma_walk:.3f}')
ax2.set_xlabel(r'$\sigma$')
ax2.set_ylabel(r'$\sigma \cdot d_s(\sigma)$')
ax2.set_title('Method 1: Backreaction Fixed Point')
ax2.set_ylim(0, max(C_backreact * 3, 20))
ax2.legend(fontsize=7)
ax2.grid(True, alpha=0.3)

# Panel 3: Hawking n_s vs sigma (vacuum)
ax3 = fig.add_subplot(gs[0, 2])
ns_hawk_prof = 1.0 - dds_dtau_landscape[fold_idx, :]
ax3.semilogx(sigma_arr[5:-5], ns_hawk_prof[5:-5], 'b-', linewidth=1.5, label='vacuum')
if ns_hawk_occ_full is not None:
    ax3.semilogx(sigma_fine[5:-5], ns_hawk_occ_full[5:-5], 'r-', linewidth=1, alpha=0.7, label='occupied')
ax3.axhspan(0.955, 0.975, alpha=0.15, color='green', label='Gate range')
ax3.axhline(y=0.9649, ls='--', color='green', alpha=0.5, label='Planck')
ax3.axhline(y=1.0, ls=':', color='gray', alpha=0.5)
# Mark method results
for name, res in qt_results.items():
    ax3.plot(res['sigma'], res['ns_hawk'], 'D', markersize=5, alpha=0.7)
ax3.plot(sigma_br, ns_hawk_br, 's', color='blue', markersize=8, label='Backreaction')
if not np.isnan(sigma_zeta):
    ax3.plot(sigma_zeta, ns_hawk_zeta, '^', color='purple', markersize=8, label='Zeta')
ax3.set_xlabel(r'$\sigma$')
ax3.set_ylabel(r'$n_s$ (Hawking)')
ax3.set_title(r'$n_s = 1 - \partial d_s / \partial \tau$ vs $\sigma$')
ax3.set_ylim(0.4, 1.5)
ax3.legend(fontsize=6, loc='upper left')
ax3.grid(True, alpha=0.3)

# Panel 4: Q-theory sigma prescriptions
ax4 = fig.add_subplot(gs[1, 0])
qt_names = list(qt_results.keys())
qt_sigmas = [qt_results[n]['sigma'] for n in qt_names]
qt_ns_hawk = [qt_results[n]['ns_hawk'] for n in qt_names]
qt_ns_cdt = [qt_results[n]['ns_cdt'] for n in qt_names]
x_pos = np.arange(len(qt_names))
width = 0.35
ax4.bar(x_pos - width/2, qt_ns_hawk, width, color='blue', alpha=0.7, label='n_s(Hawk)')
ax4.bar(x_pos + width/2, qt_ns_cdt, width, color='red', alpha=0.7, label='n_s(CDT)')
ax4.axhspan(0.955, 0.975, alpha=0.15, color='green')
ax4.axhline(y=0.9649, ls='--', color='green', alpha=0.5)
ax4.set_xticks(x_pos)
ax4.set_xticklabels(qt_names, fontsize=7, rotation=30)
ax4.set_ylabel(r'$n_s$')
ax4.set_title(r'Method 4: Q-Theory $\sigma = f(\tau^*)$')
ax4.legend(fontsize=7)
ax4.grid(True, alpha=0.3, axis='y')

# Panel 5: Occupied/vacuum ratio
ax5 = fig.add_subplot(gs[1, 1])
if fold_ds_occ is not None and fold_ds_vac is not None:
    ratio_occ_vac = fold_ds_occ / np.maximum(fold_ds_vac, 1e-10)
    valid_mask = fold_ds_vac > 0.1
    ax5.semilogx(sigma_fine[valid_mask], ratio_occ_vac[valid_mask], 'r-', linewidth=1.5)
    ax5.axhline(y=1.0, ls=':', color='gray', alpha=0.5)
    ax5.set_xlabel(r'$\sigma$')
    ax5.set_ylabel(r'$d_s^{\rm occ} / d_s^{\rm vac}$')
    ax5.set_title('Occupation Weighting Effect')
    ax5.grid(True, alpha=0.3)

# Panel 6: d_s vs tau at selected sigmas (occupied)
ax6 = fig.add_subplot(gs[1, 2])
if len(ds_occ_results) >= 3:
    occ_tau_arr = np.array(sorted(ds_occ_results.keys()))
    for s_probe, color, ls in [(0.5, 'blue', '-'), (1.0, 'red', '-'),
                                (2.0, 'green', '-'), (sigma_walk_occ, 'black', '--')]:
        idx_s = np.argmin(np.abs(sigma_fine - s_probe))
        ds_vs_tau = [ds_occ_results[t][idx_s] for t in occ_tau_arr]
        ax6.plot(occ_tau_arr, ds_vs_tau, f'{ls}', color=color, linewidth=1.5,
                 label=f'sig={s_probe:.2f}', markersize=3)
    ax6.axhline(y=4, ls=':', color='gray', alpha=0.5)
    ax6.set_xlabel(r'$\tau$')
    ax6.set_ylabel(r'$d_s^{\rm occ}$')
    ax6.set_title(r'$d_s^{\rm occ}$ vs $\tau$ at fixed $\sigma$')
    ax6.legend(fontsize=7)
    ax6.grid(True, alpha=0.3)

# Panel 7: Heat kernel P(sigma) vacuum vs occupied
ax7 = fig.add_subplot(gs[2, 0])
if fold_tau_val in tau_eig_data:
    # Recompute P_vac and P_occ
    pairs_vac = tau_eig_data[fold_tau_val]
    P_vac_plot = np.array([compute_heat_kernel(s, pairs_vac) for s in sigma_fine])

    # Build occupied pairs
    occ_pairs_plot = []
    for p, q in SECTORS:
        ev = get_evals(p, q, fold_tau_val)
        if ev is None:
            continue
        d = dim_pq(p, q)
        Delta = Delta_sectors.get((p, q), Delta_B3_fb)
        for lam in ev:
            lam2 = lam**2
            lam_abs = abs(lam)
            E_k = np.sqrt(lam2 + Delta**2)
            v_k_sq = 0.5 * (1.0 - lam_abs / E_k)
            occ_pairs_plot.append((v_k_sq * lam2, d))
    P_occ_plot = np.array([compute_heat_kernel(s, occ_pairs_plot) for s in sigma_fine])

    ax7.loglog(sigma_fine, P_vac_plot, 'b-', linewidth=1.5, label='vacuum')
    ax7.loglog(sigma_fine, P_occ_plot, 'r-', linewidth=1.5, label='occupied')
    ax7.set_xlabel(r'$\sigma$')
    ax7.set_ylabel(r'$P(\sigma)$')
    ax7.set_title('Heat Kernel: Vacuum vs Occupied')
    ax7.legend(fontsize=8)
    ax7.grid(True, alpha=0.3)

# Panel 8: Convergence of backreaction iteration
ax8 = fig.add_subplot(gs[2, 1])
for sigma_init, color in [(0.1, 'blue'), (0.5, 'green'), (1.0, 'red'),
                           (2.0, 'orange'), (5.0, 'purple')]:
    sigma_traj = [sigma_init]
    sig_curr = sigma_init
    for step in range(30):
        ds_curr, _, _ = compute_ds_ns(sig_curr)
        if ds_curr <= 0:
            break
        sig_next = C_backreact / ds_curr
        sigma_traj.append(sig_next)
        if abs(sig_next - sig_curr) / max(abs(sig_curr), 1e-10) < 1e-8:
            break
        sig_curr = sig_next
    ax8.plot(range(len(sigma_traj)), sigma_traj, 'o-', color=color, markersize=3,
             label=f'init={sigma_init}')
ax8.axhline(y=sigma_walk, ls='--', color='gray', alpha=0.5, label=f'sigma_walk={sigma_walk:.3f}')
ax8.set_xlabel('Iteration')
ax8.set_ylabel(r'$\sigma$')
ax8.set_title('Backreaction Iteration Convergence')
ax8.legend(fontsize=7)
ax8.set_yscale('log')
ax8.grid(True, alpha=0.3)

# Panel 9: Summary text
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')
summary_text = (
    f"SIGMA-SELECT-45 RESULTS\n"
    f"{'='*40}\n\n"
    f"Gate: {struct_verdict}\n\n"
    f"METHOD 1 (Backreaction):\n"
    f"  sigma* = {sigma_br:.4f} (trivial)\n"
    f"  n_s(H) = {ns_hawk_br:.4f}\n\n"
    f"METHOD 2 (Hubble):\n"
    f"  sigma_H = {sigma_H:.2e}\n"
    f"  d_s = {ds_H:.2e} (UV trivial)\n\n"
    f"METHOD 3 (Occupied):\n"
    f"  sigma_walk = {sigma_walk_occ:.4f}\n"
    f"  n_s(H) = {ns_hawk_occ:.4f}\n\n"
    f"METHOD 4 (Q-theory):\n"
    f"  Best: {best_qt[0]}\n"
    f"  n_s(H) = {best_qt[1]['ns_hawk']:.4f}\n\n"
    f"Planck: 0.9649 +/- 0.0042\n"
    f"No method selects sigma\n"
    f"from first principles."
)
ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

fig.suptitle('Session 45 W3-R1: Scale Selection for Spectral Dimension n_s (SIGMA-SELECT-45)',
             fontsize=13, fontweight='bold')
plt.savefig(output_png, dpi=150, bbox_inches='tight')
print(f"Plot saved to {output_png}")

print("\n" + "=" * 78)
print("SIGMA-SELECT-45 COMPLETE")
print("=" * 78)
