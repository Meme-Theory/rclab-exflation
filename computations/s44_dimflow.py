#!/usr/bin/env python3
"""
Session 44 W2-2: Spectral Dimension Flow for n_s (DIMFLOW-44)
================================================================

Computes the spectral dimension d_s(sigma, tau) from the heat kernel return
probability on (SU(3), g_tau), and extracts the spectral tilt n_s from the
spectral dimension flow during the Jensen transit.

Mathematical framework:
  The heat kernel return probability (trace of heat kernel on diagonal):
    P(sigma) = Tr exp(-sigma D_K^2) = sum_{(p,q)} dim(p,q) * sum_i exp(-sigma lambda_{(p,q),i}^2)

  where the Peter-Weyl multiplicity dim(p,q) accounts for the right-regular
  representation copy, and the sum over i runs over the dim(p,q)*16 eigenvalues
  of the Dirac matrix D_{(p,q)} in sector (p,q).

  The spectral dimension:
    d_s(sigma) = -2 d(ln P) / d(ln sigma)

  At small sigma (UV): d_s -> dim(SU(3)) = 8 (Weyl's law)
  At large sigma (IR): d_s -> 0 (compact space, gap dominates)

  The "walking regime" is where d_s transitions between these limits.

n_s extraction:
  1. CDT/causal-set formula: n_s - 1 = (d_s(sigma_*) - 4) / 2
     where sigma_* is the scale at which d_s transitions.
  2. Hawking flow formula: n_s - 1 ~ -d(d_s)/d(tau) at fixed sigma_*.

Pre-registered gate:
  DIMFLOW-44: PASS if n_s in [0.94, 0.97]. FAIL if n_s outside [0.80, 1.10].

Author: Connes NCG Theorist (Session 44)
"""

import numpy as np
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ═══════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

data_dir = Path("tier0-computation")
output_npz = data_dir / "s44_dimflow.npz"
output_png = data_dir / "s44_dimflow.png"

SECTORS = [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(3,0),(0,3),(2,1),(1,2)]

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# ═══════════════════════════════════════════════════════════════════════
# DATA LOADING
# ═══════════════════════════════════════════════════════════════════════

print("=" * 72)
print("SESSION 44 W2-2: SPECTRAL DIMENSION FLOW FOR n_s (DIMFLOW-44)")
print("=" * 72)

d27 = np.load(data_dir / "s27_multisector_bcs.npz", allow_pickle=True)
d36 = np.load(data_dir / "s36_sfull_tau_stabilization.npz", allow_pickle=True)

tau_27 = d27['tau_values']
tau_36 = [0.050, 0.160, 0.170, 0.180, 0.190, 0.210, 0.220]
all_tau = sorted(set([float(f'{t:.3f}') for t in list(tau_27)] + tau_36))

print(f"\nMerged tau grid ({len(all_tau)} points): {all_tau}")


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


# ═══════════════════════════════════════════════════════════════════════
# STEP 1: COLLECT EIGENVALUE DATA AT ALL TAU
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 1: COLLECTING EIGENVALUE DATA")
print("=" * 72)

# Structure: for each tau, collect (lambda_k^2, degeneracy_k) pairs
# where degeneracy_k = dim(p,q) from Peter-Weyl
# Each eigenvalue lambda from sector (p,q) matrix appears dim(p,q) times
# in the full L^2(G,S) spectrum.

tau_data = {}  # tau -> list of (lambda^2, PW_multiplicity)

for tau in all_tau:
    pairs = []  # (lambda^2, multiplicity)
    n_sectors_found = 0
    for p, q in SECTORS:
        ev = get_evals(p, q, tau)
        if ev is None:
            continue
        n_sectors_found += 1
        d = dim_pq(p, q)
        # ev contains the imaginary parts of D eigenvalues (anti-Hermitian convention)
        # D_K^2 eigenvalues are lambda^2 where lambda are the values in ev
        for lam in ev:
            pairs.append((lam**2, d))

    if n_sectors_found >= 8:  # Need most sectors
        tau_data[tau] = pairs
        total_modes = sum(mult for _, mult in pairs)
        n_evals = len(pairs)
        print(f"  tau={tau:.3f}: {n_sectors_found}/10 sectors, "
              f"{n_evals} distinct eigenvalues, {total_modes} total modes (with PW)")
    else:
        print(f"  tau={tau:.3f}: only {n_sectors_found}/10 sectors -- SKIPPED")

valid_tau = sorted(tau_data.keys())
print(f"\nValid tau values: {valid_tau} ({len(valid_tau)} points)")


# ═══════════════════════════════════════════════════════════════════════
# STEP 2: COMPUTE HEAT KERNEL AND SPECTRAL DIMENSION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 2: HEAT KERNEL RETURN PROBABILITY AND SPECTRAL DIMENSION")
print("=" * 72)

# sigma range: from UV (small sigma) to IR (large sigma)
# The natural scale is set by the eigenvalue spectrum: lambda^2 ~ O(1)
# so sigma ~ 1 is the crossover region
N_sigma = 300
log_sigma = np.linspace(-4, 4, N_sigma)
sigma_arr = 10.0**log_sigma

ds_results = {}  # tau -> (sigma_arr, ds_arr, P_arr)

for tau in valid_tau:
    pairs = tau_data[tau]
    lam2 = np.array([l2 for l2, _ in pairs])
    mult = np.array([m for _, m in pairs])

    # P(sigma) = sum_k mult_k * exp(-sigma * lambda_k^2)
    # Use log-sum-exp for numerical stability at large sigma
    P = np.zeros(N_sigma)
    for i, sig in enumerate(sigma_arr):
        exponents = -sig * lam2
        # Weighted sum: sum mult_k * exp(exponent_k)
        P[i] = np.sum(mult * np.exp(exponents))

    # d_s(sigma) = -2 d(ln P) / d(ln sigma)
    # = -2 * (sigma / P) * dP/dsigma
    # Compute numerically via centered differences on log-spaced grid
    ln_P = np.log(P + 1e-300)  # protect against zero
    ln_sigma = np.log(sigma_arr)

    # Centered finite difference for d(ln P)/d(ln sigma)
    ds = np.zeros(N_sigma)
    for i in range(1, N_sigma - 1):
        ds[i] = -2.0 * (ln_P[i+1] - ln_P[i-1]) / (ln_sigma[i+1] - ln_sigma[i-1])
    ds[0] = ds[1]
    ds[-1] = ds[-2]

    ds_results[tau] = (sigma_arr, ds, P)

    # Find walking scale: where ds is closest to 4
    idx_4 = np.argmin(np.abs(ds[1:-1] - 4.0)) + 1
    sigma_4 = sigma_arr[idx_4]
    ds_at_4 = ds[idx_4]

    # UV limit (smallest sigma)
    ds_UV = ds[5]  # avoid edge effects
    # IR limit (largest sigma)
    ds_IR = ds[-5]

    # Walking regime: where derivative |d(ds)/d(ln sigma)| is maximum
    dds_dlnsigma = np.gradient(ds, ln_sigma)
    idx_walk = np.argmax(np.abs(dds_dlnsigma[10:-10])) + 10
    sigma_walk = sigma_arr[idx_walk]
    ds_walk = ds[idx_walk]

    print(f"  tau={tau:.3f}: d_s(UV)={ds_UV:.3f}, d_s(IR)={ds_IR:.4f}, "
          f"d_s(sigma=4)={ds_at_4:.4f} at sigma={sigma_4:.3e}, "
          f"walking at sigma={sigma_walk:.3e} (d_s={ds_walk:.3f})")


# ═══════════════════════════════════════════════════════════════════════
# STEP 3: SPECTRAL DIMENSION AT FIXED SCALES vs TAU
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 3: SPECTRAL DIMENSION vs TAU AT FIXED SCALES")
print("=" * 72)

# Choose several representative sigma values for cross-section
# The "walking" scale where d_s transitions from 8 to 0 is the physically
# relevant one. We'll identify it from the tau=0.19 (fold) spectrum.

# First find the sigma where ds=4 at the fold (tau=0.19 or closest)
fold_tau = 0.200 if 0.200 in ds_results else min(valid_tau, key=lambda t: abs(t-0.19))
sig_fold, ds_fold, P_fold = ds_results[fold_tau]

# Walking scale: where ds crosses 4
idx_cross4 = np.argmin(np.abs(ds_fold[1:-1] - 4.0)) + 1
sigma_pivot = sig_fold[idx_cross4]
print(f"Pivot scale (d_s=4 at fold tau={fold_tau:.3f}): sigma_pivot = {sigma_pivot:.4e}")

# Also examine d_s at several fixed sigma values
sigma_probes = [0.01, 0.1, 0.3, 1.0, 3.0, 10.0, sigma_pivot]
sigma_labels = ['0.01', '0.1', '0.3', '1.0', '3.0', '10.0', f'{sigma_pivot:.3e}']

print(f"\nSpectral dimension at fixed sigma probes:")
print(f"{'tau':>6} | " + " | ".join(f"sig={l:>8}" for l in sigma_labels))
print("-" * (8 + 13 * len(sigma_probes)))

ds_vs_tau = {sp: [] for sp in sigma_probes}

for tau in valid_tau:
    sig_arr, ds_arr, _ = ds_results[tau]
    row = f"{tau:6.3f} | "
    for sp in sigma_probes:
        # Interpolate ds at this sigma
        idx = np.searchsorted(sig_arr, sp)
        if idx == 0:
            val = ds_arr[0]
        elif idx >= len(sig_arr):
            val = ds_arr[-1]
        else:
            # Linear interpolation in log-sigma
            frac = (np.log10(sp) - np.log10(sig_arr[idx-1])) / \
                   (np.log10(sig_arr[idx]) - np.log10(sig_arr[idx-1]))
            val = ds_arr[idx-1] + frac * (ds_arr[idx] - ds_arr[idx-1])
        ds_vs_tau[sp].append(val)
        row += f"{val:12.4f} | "
    print(row)


# ═══════════════════════════════════════════════════════════════════════
# STEP 4: n_s FROM SPECTRAL DIMENSION
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 4: SPECTRAL TILT n_s FROM SPECTRAL DIMENSION FLOW")
print("=" * 72)

# Method A: CDT formula n_s - 1 = (d_s - 4) / 2
# This gives n_s at each (sigma, tau) point.

print("\n--- Method A: CDT formula n_s = 1 + (d_s - 4)/2 ---")
print(f"{'sigma':>12} | {'d_s range':>16} | {'n_s at fold':>12} | {'n_s range':>16}")
print("-" * 70)

ns_cdt_results = {}
for sp, label in zip(sigma_probes, sigma_labels):
    ds_vals = np.array(ds_vs_tau[sp])
    ns_vals = 1.0 + (ds_vals - 4.0) / 2.0

    fold_idx = min(range(len(valid_tau)), key=lambda i: abs(valid_tau[i] - fold_tau))
    ns_fold = ns_vals[fold_idx]
    ds_fold_val = ds_vals[fold_idx]

    ns_cdt_results[sp] = (ds_vals, ns_vals)

    print(f"{label:>12} | [{ds_vals.min():.4f}, {ds_vals.max():.4f}] | "
          f"{ns_fold:12.6f} | [{ns_vals.min():.4f}, {ns_vals.max():.4f}]")


# Method B: Hawking flow formula n_s - 1 ~ -d(d_s)/d(tau)
# Compute d(d_s)/d(tau) at each sigma probe
print("\n--- Method B: Hawking flow n_s - 1 = -d(d_s)/d(tau) ---")
print(f"{'sigma':>12} | {'dd_s/dtau at fold':>18} | {'n_s at fold':>12}")
print("-" * 50)

ns_hawk_results = {}
for sp, label in zip(sigma_probes, sigma_labels):
    ds_vals = np.array(ds_vs_tau[sp])
    tau_arr = np.array(valid_tau)

    # Numerical derivative d(d_s)/d(tau)
    dds_dtau = np.gradient(ds_vals, tau_arr)

    fold_idx = min(range(len(valid_tau)), key=lambda i: abs(valid_tau[i] - fold_tau))
    dds_fold = dds_dtau[fold_idx]
    ns_fold = 1.0 - dds_fold

    ns_hawk_results[sp] = (dds_dtau, ns_fold)

    print(f"{label:>12} | {dds_fold:18.6f} | {ns_fold:12.6f}")


# ═══════════════════════════════════════════════════════════════════════
# STEP 5: COMPREHENSIVE ANALYSIS OF d_s LANDSCAPE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 5: COMPREHENSIVE d_s LANDSCAPE ANALYSIS")
print("=" * 72)

# Build full 2D landscape d_s(sigma, tau)
ds_landscape = np.zeros((len(valid_tau), N_sigma))
P_landscape = np.zeros((len(valid_tau), N_sigma))
for i, tau in enumerate(valid_tau):
    _, ds_arr, P_arr = ds_results[tau]
    ds_landscape[i, :] = ds_arr
    P_landscape[i, :] = P_arr

# For the CDT formula, find the sigma band where d_s is in [3.9, 4.1]
# at the fold, which would give n_s in [0.95, 1.05]
print("\nSearching for sigma band where d_s(sigma, fold) ~ 4:")
fold_row = ds_landscape[min(range(len(valid_tau)), key=lambda i: abs(valid_tau[i] - fold_tau)), :]
sigma_band_mask = (fold_row > 3.0) & (fold_row < 5.0)
if np.any(sigma_band_mask):
    sigma_band = sigma_arr[sigma_band_mask]
    ds_band = fold_row[sigma_band_mask]
    print(f"  sigma range for d_s in [3,5]: [{sigma_band[0]:.4e}, {sigma_band[-1]:.4e}]")
    print(f"  d_s range in this band: [{ds_band.min():.4f}, {ds_band.max():.4f}]")

    # CDT n_s in this band
    ns_band = 1.0 + (ds_band - 4.0) / 2.0
    print(f"  CDT n_s range in band: [{ns_band.min():.4f}, {ns_band.max():.4f}]")

    # Find sigma where d_s = 3.93 exactly (giving n_s = 0.965)
    target_ds = 3.93
    idx_target = np.argmin(np.abs(fold_row - target_ds))
    if abs(fold_row[idx_target] - target_ds) < 0.1:
        sigma_target = sigma_arr[idx_target]
        print(f"\n  For n_s = 0.965: need d_s = 3.93")
        print(f"  Found d_s = {fold_row[idx_target]:.4f} at sigma = {sigma_target:.4e}")
    else:
        print(f"\n  d_s = {target_ds} not found in spectrum (closest: {fold_row[idx_target]:.4f})")
else:
    print("  No sigma values give d_s near 4 at fold.")

# UV asymptotic check: d_s -> 8 = dim(SU(3))
print(f"\nUV limit check (sigma -> 0):")
for i, tau in enumerate(valid_tau):
    ds_uv = ds_landscape[i, 3:8].mean()
    print(f"  tau={tau:.3f}: d_s(UV) = {ds_uv:.4f} (expect 8.000)")

# IR limit check: d_s -> 0 (compact)
print(f"\nIR limit check (sigma -> inf):")
for i, tau in enumerate(valid_tau):
    ds_ir = ds_landscape[i, -5:].mean()
    print(f"  tau={tau:.3f}: d_s(IR) = {ds_ir:.6f} (expect ~0)")


# ═══════════════════════════════════════════════════════════════════════
# STEP 6: SPECTRAL DIMENSION FLOW RATE
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 6: SPECTRAL DIMENSION FLOW d(d_s)/d(tau) AT ALL SCALES")
print("=" * 72)

tau_arr = np.array(valid_tau)
dds_dtau_landscape = np.zeros_like(ds_landscape)
for j in range(N_sigma):
    dds_dtau_landscape[:, j] = np.gradient(ds_landscape[:, j], tau_arr)

# At the fold
fold_idx = min(range(len(valid_tau)), key=lambda i: abs(valid_tau[i] - fold_tau))
dds_fold_profile = dds_dtau_landscape[fold_idx, :]

print(f"d(d_s)/d(tau) at fold tau={valid_tau[fold_idx]:.3f} as function of sigma:")
for idx in [10, 30, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275]:
    if idx < N_sigma:
        print(f"  sigma={sigma_arr[idx]:.3e}: d(d_s)/d(tau) = {dds_fold_profile[idx]:.6f}")

# Maximum |d(d_s)/d(tau)| at fold
idx_max_flow = np.argmax(np.abs(dds_fold_profile[5:-5])) + 5
sigma_max_flow = sigma_arr[idx_max_flow]
dds_max_flow = dds_fold_profile[idx_max_flow]
ns_hawk_max = 1.0 - dds_max_flow
print(f"\nMaximum |d(d_s)/d(tau)| at fold: {abs(dds_max_flow):.6f}")
print(f"  at sigma = {sigma_max_flow:.4e}")
print(f"  Hawking n_s = 1 - ({dds_max_flow:.6f}) = {ns_hawk_max:.6f}")


# ═══════════════════════════════════════════════════════════════════════
# STEP 7: WEYL'S LAW VERIFICATION AND ANALYTIC d_s
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 7: WEYL'S LAW AND ANALYTIC SPECTRAL DIMENSION")
print("=" * 72)

# For a compact d-dimensional Riemannian manifold, Weyl's law gives
# N(lambda) ~ C * lambda^d, so the heat kernel has
# P(sigma) ~ C * sigma^{-d/2} for small sigma
# and d_s(sigma->0) = d.
#
# For SU(3) (dim=8), d_s(UV) = 8.
#
# For large sigma on compact manifold: P(sigma) ~ exp(-sigma * lambda_0^2)
# where lambda_0 is the smallest nonzero eigenvalue.
# Then d_s ~ 2 * sigma * lambda_0^2.
#
# The transition happens at sigma ~ 1/lambda_0^2.

# Compute lambda_0 (smallest nonzero |eigenvalue|) at each tau
print("\nSmallest nonzero eigenvalue and natural crossover scale:")
for tau in valid_tau:
    pairs = tau_data[tau]
    lam2_all = np.array([l2 for l2, _ in pairs])
    # Filter out zero modes
    lam2_nonzero = lam2_all[lam2_all > 1e-10]
    lam2_min = lam2_nonzero.min() if len(lam2_nonzero) > 0 else 0
    sigma_cross = 1.0 / lam2_min if lam2_min > 0 else np.inf
    print(f"  tau={tau:.3f}: lambda_0^2 = {lam2_min:.6f}, "
          f"|lambda_0| = {np.sqrt(lam2_min):.6f}, "
          f"sigma_cross = {sigma_cross:.4f}")


# ═══════════════════════════════════════════════════════════════════════
# STEP 8: GATE VERDICT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 8: GATE VERDICT — DIMFLOW-44")
print("=" * 72)

# The CDT formula and Hawking flow give n_s at different sigma scales.
# Report the full landscape and the specific values at the walking scale.

# CDT n_s at sigma_pivot (where ds=4 at fold)
ds_cdt_pivot, ns_cdt_pivot = ns_cdt_results[sigma_pivot]
fold_idx_main = min(range(len(valid_tau)), key=lambda i: abs(valid_tau[i] - fold_tau))
ns_cdt_at_fold = ns_cdt_pivot[fold_idx_main]

# Hawking n_s at sigma_pivot
dds_hawk_pivot, ns_hawk_at_fold = ns_hawk_results[sigma_pivot]

# CDT n_s at sigma = 1.0 (natural scale)
ds_cdt_1, ns_cdt_1 = ns_cdt_results.get(1.0, (None, None))
ns_cdt_1_fold = ns_cdt_1[fold_idx_main] if ns_cdt_1 is not None else None

print(f"\n=== PRIMARY RESULTS ===")
print(f"CDT formula: n_s = 1 + (d_s - 4)/2")
print(f"  At sigma_pivot = {sigma_pivot:.4e}: n_s = {ns_cdt_at_fold:.6f}")
if ns_cdt_1_fold is not None:
    print(f"  At sigma = 1.0: n_s = {ns_cdt_1_fold:.6f}")
print(f"\nHawking flow: n_s = 1 - d(d_s)/d(tau)")
print(f"  At sigma_pivot = {sigma_pivot:.4e}: n_s = {ns_hawk_at_fold:.6f}")
print(f"  At sigma of max flow: n_s = {ns_hawk_max:.6f}")

# Determine gate verdict
# The CDT formula at the pivot scale gives n_s = 1 + 0/2 = 1.000 by construction!
# This is because sigma_pivot is defined as where d_s = 4.
# The PHYSICALLY meaningful n_s is at a scale that has physical motivation.

# Better approach: the spectral dimension at the FOLD should be evaluated
# at the scale sigma where primordial perturbations are generated.
# In standard cosmology, this is the Hubble scale at CMB.
# In the framework, the natural scale is sigma ~ 1/M_KK^2 in dimensionful units.
# In our dimensionless eigenvalues, sigma is already in units of 1/lambda^2.
# The "CMB scale" corresponds to modes that exit the horizon during transit.

# The honest result: the CDT formula gives n_s = 1.000 at sigma_pivot by tautology.
# At other scales, d_s != 4, so n_s != 1. The question is WHICH scale.

# Let's report d_s at sigma=1 (natural dimensionless scale) and sigma=0.1, 0.3
print("\n=== HONEST ASSESSMENT ===")
print("The CDT formula n_s = 1 + (d_s - 4)/2 gives n_s = 1 at the")
print("walking scale by construction (that's where d_s = 4).")
print("At other scales:")
for sp, label in zip([0.01, 0.1, 0.3, 1.0, 3.0, 10.0],
                      ['0.01', '0.1', '0.3', '1.0', '3.0', '10.0']):
    if sp in ds_vs_tau:
        ds_vals = np.array(ds_vs_tau[sp])
        ns_vals = 1.0 + (ds_vals - 4.0) / 2.0
        ns_f = ns_vals[fold_idx_main]
        ds_f = ds_vals[fold_idx_main]
        print(f"  sigma={label}: d_s={ds_f:.4f}, n_s(CDT)={ns_f:.4f}")

# Report tau-dependence of d_s at sigma=1
print("\n=== tau-DEPENDENCE at sigma=1.0 ===")
if 1.0 in ds_vs_tau:
    ds_1_arr = np.array(ds_vs_tau[1.0])
    ns_1_arr = 1.0 + (ds_1_arr - 4.0) / 2.0
    dds_1_dtau = np.gradient(ds_1_arr, tau_arr)
    ns_hawk_1 = 1.0 - dds_1_dtau
    for i, tau in enumerate(valid_tau):
        print(f"  tau={tau:.3f}: d_s={ds_1_arr[i]:.4f}, n_s(CDT)={ns_1_arr[i]:.4f}, "
              f"dd_s/dtau={dds_1_dtau[i]:.4f}, n_s(Hawk)={ns_hawk_1[i]:.4f}")

# Determine primary n_s value for gate
# Use d_s at the "walking midpoint" -- where d_s is between 3 and 5,
# averaged over the walking region
print("\n=== WALKING MIDPOINT ANALYSIS ===")
# At the fold, find the sigma range where d_s is in [3,5] (the walking band)
fold_ds = ds_landscape[fold_idx_main, :]
walking_mask = (fold_ds > 2.0) & (fold_ds < 6.0)
if np.any(walking_mask):
    ds_walking = fold_ds[walking_mask]
    sigma_walking = sigma_arr[walking_mask]
    ds_midpoint = np.median(ds_walking)
    ns_midpoint = 1.0 + (ds_midpoint - 4.0) / 2.0
    print(f"Walking band at fold: sigma in [{sigma_walking[0]:.3e}, {sigma_walking[-1]:.3e}]")
    print(f"Median d_s in walking band: {ds_midpoint:.4f}")
    print(f"CDT n_s at median: {ns_midpoint:.4f}")

    # Also compute the tau-average of d_s at the midpoint sigma
    sigma_mid = sigma_walking[len(sigma_walking)//2]
    idx_mid = np.argmin(np.abs(sigma_arr - sigma_mid))
    ds_mid_vs_tau = ds_landscape[:, idx_mid]
    dds_mid_dtau = np.gradient(ds_mid_vs_tau, tau_arr)
    ns_hawk_mid = 1.0 - dds_mid_dtau[fold_idx_main]

    print(f"\nAt walking midpoint sigma={sigma_mid:.3e}:")
    print(f"  d_s at fold = {ds_mid_vs_tau[fold_idx_main]:.4f}")
    print(f"  dd_s/dtau at fold = {dds_mid_dtau[fold_idx_main]:.6f}")
    print(f"  Hawking n_s = {ns_hawk_mid:.6f}")
else:
    ds_midpoint = None
    ns_midpoint = None
    ns_hawk_mid = None

# Final gate verdict
print("\n" + "=" * 72)
print("GATE VERDICT: DIMFLOW-44")
print("=" * 72)

# For the CDT formula: the scale is not determined from within the framework,
# making n_s a function of the arbitrary parameter sigma.
# For the Hawking flow: it gives the rate of change, which IS scale-dependent.

# Report honestly: the spectral dimension framework produces a LANDSCAPE
# d_s(sigma, tau) but does not determine the physically relevant sigma.
# The n_s value depends on which scale is chosen.

# Check if ANY scale gives n_s in [0.94, 0.97]
ns_cdt_all_scales = 1.0 + (fold_ds - 4.0) / 2.0
passes_cdt = np.any((ns_cdt_all_scales >= 0.94) & (ns_cdt_all_scales <= 0.97))

# Check Hawking flow at all scales
ns_hawk_all = 1.0 - dds_fold_profile
passes_hawk = np.any((ns_hawk_all[5:-5] >= 0.94) & (ns_hawk_all[5:-5] <= 0.97))

# Find which sigma gives n_s = 0.965 (CDT)
target_ns = 0.965
target_ds_cdt = 4.0 + 2.0 * (target_ns - 1.0)  # = 3.93
idx_target_cdt = np.argmin(np.abs(fold_ds - target_ds_cdt))
sigma_for_target = sigma_arr[idx_target_cdt]
ds_at_target = fold_ds[idx_target_cdt]

print(f"\nCDT formula results:")
print(f"  n_s = 0.965 requires d_s = 3.930")
if abs(ds_at_target - target_ds_cdt) < 0.5:
    print(f"  Found d_s = {ds_at_target:.4f} at sigma = {sigma_for_target:.4e}")
    print(f"  => n_s(CDT) = {1.0 + (ds_at_target - 4.0)/2.0:.6f}")
    # Check if this sigma has physical meaning
    print(f"  This sigma value {'IS' if 0.01 < sigma_for_target < 100 else 'is NOT'} "
          f"in the natural dimensionless range")
else:
    print(f"  d_s = 3.93 NOT found in spectrum")

# Hawking flow: find sigma where n_s(Hawk) = 0.965
ns_hawk_profile = 1.0 - dds_fold_profile
idx_hawk_target = np.argmin(np.abs(ns_hawk_profile[5:-5] - 0.965)) + 5
sigma_hawk_target = sigma_arr[idx_hawk_target]
ns_hawk_target = ns_hawk_profile[idx_hawk_target]
print(f"\nHawking flow results:")
print(f"  Closest to n_s = 0.965: n_s = {ns_hawk_target:.6f} at sigma = {sigma_hawk_target:.4e}")

# PRIMARY VERDICT
# The CDT formula can produce n_s = 0.965 at a specific sigma, but that sigma
# is not determined from within the framework.
# The Hawking flow depends on how d_s changes with tau, which IS physical.

# Report at sigma = 1 (natural dimensionless scale)
if 1.0 in ds_vs_tau:
    ds_1_fold = np.array(ds_vs_tau[1.0])[fold_idx_main]
    ns_1_cdt = 1.0 + (ds_1_fold - 4.0) / 2.0
    dds_1_dtau_fold = np.gradient(np.array(ds_vs_tau[1.0]), tau_arr)[fold_idx_main]
    ns_1_hawk = 1.0 - dds_1_dtau_fold

    print(f"\n=== PRIMARY n_s VALUES (sigma=1, natural scale) ===")
    print(f"  d_s(sigma=1, fold) = {ds_1_fold:.6f}")
    print(f"  n_s(CDT, sigma=1) = {ns_1_cdt:.6f}")
    print(f"  n_s(Hawk, sigma=1) = {ns_1_hawk:.6f}")

    primary_ns_cdt = ns_1_cdt
    primary_ns_hawk = ns_1_hawk
else:
    primary_ns_cdt = ns_cdt_at_fold
    primary_ns_hawk = ns_hawk_at_fold

# Gate classification
if 0.94 <= primary_ns_cdt <= 0.97 or 0.94 <= primary_ns_hawk <= 0.97:
    gate_verdict = "PASS"
elif 0.80 <= primary_ns_cdt <= 1.10 or 0.80 <= primary_ns_hawk <= 1.10:
    gate_verdict = "FAIL"
else:
    gate_verdict = "FAIL"

# Also report the RANGE of n_s across all natural scales
ns_natural_range_cdt = ns_cdt_all_scales[(sigma_arr > 0.1) & (sigma_arr < 10.0)]
ns_natural_range_hawk = ns_hawk_all[(sigma_arr > 0.1) & (sigma_arr < 10.0)]

print(f"\n=== GATE: DIMFLOW-44 ===")
print(f"  n_s(CDT) at sigma=1: {primary_ns_cdt:.6f}")
print(f"  n_s(Hawk) at sigma=1: {primary_ns_hawk:.6f}")
print(f"  n_s(CDT) range [sigma in 0.1-10]: [{ns_natural_range_cdt.min():.4f}, {ns_natural_range_cdt.max():.4f}]")
print(f"  n_s(Hawk) range [sigma in 0.1-10]: [{ns_natural_range_hawk.min():.4f}, {ns_natural_range_hawk.max():.4f}]")
print(f"  Passes exist at some sigma? CDT={passes_cdt}, Hawk={passes_hawk}")
print(f"\n  VERDICT: {gate_verdict}")
print(f"  Planck: n_s = 0.9649 +/- 0.0042")

# Unification gate with Lifshitz
ns_lifshitz = -2.77  # from W1-3 LIFSHITZ-ETA-44 FAIL
print(f"\n  UNIFICATION GATE:")
print(f"    n_s(Lifshitz) = {ns_lifshitz:.2f} (FAIL, mechanism CLOSED)")
print(f"    n_s(DIMFLOW, CDT) = {primary_ns_cdt:.4f}")
print(f"    |difference| = {abs(primary_ns_cdt - ns_lifshitz):.4f}")
print(f"    Unification: MOOT (Lifshitz CLOSED)")


# ═══════════════════════════════════════════════════════════════════════
# STEP 9: SAVE DATA
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 9: SAVING DATA")
print("=" * 72)

save_dict = {
    'valid_tau': np.array(valid_tau),
    'sigma_arr': sigma_arr,
    'log_sigma': log_sigma,
    'ds_landscape': ds_landscape,
    'P_landscape': P_landscape,
    'dds_dtau_landscape': dds_dtau_landscape,
    'sigma_pivot': np.float64(sigma_pivot),
    'fold_tau': np.float64(fold_tau),
    'fold_idx': np.int64(fold_idx_main),
    'primary_ns_cdt': np.float64(primary_ns_cdt),
    'primary_ns_hawk': np.float64(primary_ns_hawk),
    'gate_verdict': np.array([gate_verdict]),
    'ns_lifshitz': np.float64(ns_lifshitz),
}

# Add ds_vs_tau at probe sigmas
for sp, label in zip(sigma_probes[:-1], sigma_labels[:-1]):
    save_dict[f'ds_sigma_{label}'] = np.array(ds_vs_tau[sp])

np.savez(output_npz, **save_dict)
print(f"Data saved to {output_npz}")


# ═══════════════════════════════════════════════════════════════════════
# STEP 10: PLOT
# ═══════════════════════════════════════════════════════════════════════

print("\n" + "=" * 72)
print("STEP 10: GENERATING PLOT")
print("=" * 72)

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.30)

# Panel 1: d_s(sigma) at multiple tau values
ax1 = fig.add_subplot(gs[0, 0])
cmap = plt.cm.viridis
for i, tau in enumerate(valid_tau):
    color = cmap(i / max(len(valid_tau)-1, 1))
    ax1.semilogx(sigma_arr, ds_landscape[i, :], color=color, alpha=0.7,
                  label=f'tau={tau:.2f}' if i % 3 == 0 else None)
ax1.axhline(y=8, ls='--', color='gray', alpha=0.5, label='dim=8')
ax1.axhline(y=4, ls=':', color='red', alpha=0.5, label='d_s=4')
ax1.axhline(y=0, ls='--', color='gray', alpha=0.3)
ax1.set_xlabel(r'$\sigma$ (diffusion time)')
ax1.set_ylabel(r'$d_s(\sigma)$')
ax1.set_title(r'Spectral Dimension $d_s(\sigma, \tau)$')
ax1.set_ylim(-0.5, 9)
ax1.legend(fontsize=7, loc='upper right')
ax1.grid(True, alpha=0.3)

# Panel 2: d_s at fixed sigma vs tau
ax2 = fig.add_subplot(gs[0, 1])
colors2 = ['blue', 'green', 'orange', 'red', 'purple', 'brown']
for idx, (sp, label) in enumerate(zip([0.01, 0.1, 0.3, 1.0, 3.0, 10.0],
                                       ['0.01', '0.1', '0.3', '1.0', '3.0', '10.0'])):
    if sp in ds_vs_tau:
        ax2.plot(valid_tau, ds_vs_tau[sp], 'o-', color=colors2[idx],
                 label=f'sigma={label}', markersize=3)
ax2.axhline(y=4, ls=':', color='red', alpha=0.5)
ax2.axhline(y=3.93, ls='--', color='red', alpha=0.3, label='d_s=3.93 (n_s=0.965)')
ax2.set_xlabel(r'$\tau$')
ax2.set_ylabel(r'$d_s$')
ax2.set_title(r'$d_s$ vs $\tau$ at fixed $\sigma$')
ax2.legend(fontsize=7)
ax2.grid(True, alpha=0.3)

# Panel 3: CDT n_s at fixed sigma vs tau
ax3 = fig.add_subplot(gs[0, 2])
for idx, (sp, label) in enumerate(zip([0.1, 0.3, 1.0, 3.0],
                                       ['0.1', '0.3', '1.0', '3.0'])):
    if sp in ds_vs_tau:
        ds_v = np.array(ds_vs_tau[sp])
        ns_v = 1.0 + (ds_v - 4.0) / 2.0
        ax3.plot(valid_tau, ns_v, 'o-', color=colors2[idx+1],
                 label=f'sigma={label}', markersize=3)
ax3.axhspan(0.9607, 0.9691, alpha=0.2, color='green', label='Planck 1sigma')
ax3.axhline(y=0.9649, ls='--', color='green', alpha=0.5)
ax3.axhline(y=1.0, ls=':', color='gray', alpha=0.5)
ax3.set_xlabel(r'$\tau$')
ax3.set_ylabel(r'$n_s$ (CDT)')
ax3.set_title(r'$n_s = 1 + (d_s - 4)/2$ (CDT formula)')
ax3.legend(fontsize=7)
ax3.grid(True, alpha=0.3)

# Panel 4: 2D heatmap of d_s(sigma, tau)
ax4 = fig.add_subplot(gs[1, 0])
tau_mesh, sig_mesh = np.meshgrid(valid_tau, np.log10(sigma_arr), indexing='ij')
im = ax4.pcolormesh(tau_mesh, sig_mesh, ds_landscape, cmap='RdYlBu_r',
                     vmin=0, vmax=8, shading='auto')
plt.colorbar(im, ax=ax4, label=r'$d_s$')
ax4.contour(tau_mesh, sig_mesh, ds_landscape, levels=[4], colors='red', linewidths=2)
ax4.set_xlabel(r'$\tau$')
ax4.set_ylabel(r'$\log_{10}(\sigma)$')
ax4.set_title(r'$d_s(\sigma, \tau)$ landscape')

# Panel 5: Hawking flow d(d_s)/d(tau) at fold
ax5 = fig.add_subplot(gs[1, 1])
ax5.semilogx(sigma_arr[5:-5], dds_fold_profile[5:-5], 'b-', linewidth=1.5)
ax5.axhline(y=0, ls=':', color='gray')
ax5.set_xlabel(r'$\sigma$')
ax5.set_ylabel(r'$\partial d_s / \partial \tau$')
ax5.set_title(f'Hawking flow rate at fold (tau={valid_tau[fold_idx_main]:.3f})')
ax5.grid(True, alpha=0.3)

# Panel 6: Hawking n_s at fold vs sigma
ax6 = fig.add_subplot(gs[1, 2])
ns_hawk_prof = 1.0 - dds_fold_profile
ax6.semilogx(sigma_arr[5:-5], ns_hawk_prof[5:-5], 'r-', linewidth=1.5)
ax6.axhspan(0.9607, 0.9691, alpha=0.2, color='green', label='Planck 1sigma')
ax6.axhline(y=0.9649, ls='--', color='green', alpha=0.5)
ax6.axhline(y=1.0, ls=':', color='gray', alpha=0.5)
ax6.set_xlabel(r'$\sigma$')
ax6.set_ylabel(r'$n_s$ (Hawking)')
ax6.set_title(r'$n_s = 1 - \partial d_s / \partial \tau$')
ax6.set_ylim(0.5, 1.5)
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.3)

# Panel 7: Heat kernel P(sigma) at multiple tau
ax7 = fig.add_subplot(gs[2, 0])
for i, tau in enumerate(valid_tau):
    color = cmap(i / max(len(valid_tau)-1, 1))
    ax7.loglog(sigma_arr, P_landscape[i, :], color=color, alpha=0.7,
               label=f'tau={tau:.2f}' if i % 3 == 0 else None)
ax7.set_xlabel(r'$\sigma$')
ax7.set_ylabel(r'$P(\sigma) = \mathrm{Tr}\, e^{-\sigma D_K^2}$')
ax7.set_title('Heat Kernel Return Probability')
ax7.legend(fontsize=7)
ax7.grid(True, alpha=0.3)

# Panel 8: 2D heatmap of d(d_s)/d(tau)
ax8 = fig.add_subplot(gs[2, 1])
vmax_flow = np.percentile(np.abs(dds_dtau_landscape), 95)
im8 = ax8.pcolormesh(tau_mesh, sig_mesh, dds_dtau_landscape, cmap='RdBu',
                      vmin=-vmax_flow, vmax=vmax_flow, shading='auto')
plt.colorbar(im8, ax=ax8, label=r'$\partial d_s / \partial \tau$')
ax8.set_xlabel(r'$\tau$')
ax8.set_ylabel(r'$\log_{10}(\sigma)$')
ax8.set_title(r'$\partial d_s / \partial \tau$ landscape')

# Panel 9: Summary text
ax9 = fig.add_subplot(gs[2, 2])
ax9.axis('off')
summary_text = (
    f"DIMFLOW-44 RESULTS\n"
    f"{'='*35}\n\n"
    f"Valid tau points: {len(valid_tau)}\n"
    f"Sectors: {len(SECTORS)} (p+q <= 3)\n"
    f"Fold tau: {fold_tau:.3f}\n\n"
    f"d_s(UV) = {ds_landscape[fold_idx_main, 5]:.2f} (expect 8)\n"
    f"d_s(IR) = {ds_landscape[fold_idx_main, -5]:.4f}\n\n"
    f"CDT: n_s(sig=1) = {primary_ns_cdt:.4f}\n"
    f"Hawk: n_s(sig=1) = {primary_ns_hawk:.4f}\n\n"
    f"Planck: 0.9649 +/- 0.0042\n\n"
    f"VERDICT: {gate_verdict}"
)
ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=10, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.suptitle('Session 44 W2-2: Spectral Dimension Flow (DIMFLOW-44)',
             fontsize=14, fontweight='bold')
plt.savefig(output_png, dpi=150, bbox_inches='tight')
print(f"Plot saved to {output_png}")

print("\n" + "=" * 72)
print("DIMFLOW-44 COMPLETE")
print("=" * 72)
