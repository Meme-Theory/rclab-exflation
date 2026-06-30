#!/usr/bin/env python3
"""
FULL-COV-PANTHEON-70 — Pantheon+ with Full 1701x1701 Covariance Matrix
======================================================================

Sharpens the S69 PVD-SNE-69 result (diagonal errors only, Delta chi^2 = -4.47)
by using the full Brout+2022 STAT+SYS covariance matrix from the Pantheon+ data
release.

Method:
  1. Download Pantheon+SH0ES.dat (1701 SNe, m_b_corr, zHD)
  2. Download Pantheon+SH0ES_STAT+SYS.cov (1701x1701 covariance matrix)
  3. Compute distance modulus mu(z) for FW (w=-0.918) and LCDM (w=-1)
  4. Analytically marginalize over M_B offset
  5. Compute chi^2 = (m_b - mu - M_B)^T C^{-1} (m_b - mu - M_B)
  6. Compare Delta chi^2(full cov) vs Delta chi^2(diag) = -4.47

The full covariance includes:
  - Statistical errors (photometry, light-curve fit)
  - Systematic errors (calibration, selection, dust, peculiar velocity)
  - Off-diagonal correlations between SNe sharing calibration, host properties

Framework predicts flat wCDM with:
  w_0 = -0.918, w_a = 0, Omega_m = 0.315, H_0 = 67.4 km/s/Mpc

Gate: FULL-COV-PANTHEON-70
  INFO: Report Delta_chi^2(full cov) and compare to Delta_chi^2(diag) = -4.47

Output: s70_full_cov_pantheon.npz, s70_full_cov_pantheon.png
"""

import numpy as np
from scipy import integrate, linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import urllib.request
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    H_0_km_s_Mpc, Omega_m, Omega_Lambda, c_light_km_s
)

out_dir = Path(__file__).parent

# ==============================================================================
#  SECTION 1: Load Pantheon+ Data and Full Covariance
# ==============================================================================

DATA_URL = "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat"
COV_URL = "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov"


def download_or_cache(url, cache_name):
    """Download file from URL or use local cache."""
    cache_path = out_dir / cache_name
    if cache_path.exists():
        print(f"  Loading cached {cache_name}")
        return cache_path.read_text()
    else:
        print(f"  Downloading {cache_name} from GitHub...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read().decode('utf-8')
        cache_path.write_text(raw)
        print(f"  Cached to {cache_path} ({len(raw)/1e6:.1f} MB)")
        return raw


def load_pantheon_data():
    """Load Pantheon+SH0ES data: z, m_b_corr, diagonal errors."""
    raw = download_or_cache(DATA_URL, "pantheon_plus_cache.dat")
    lines = raw.strip().split('\n')
    header = lines[0].split()
    cols = {name: i for i, name in enumerate(header)}
    idx_z = cols['zHD']
    idx_mb = cols['m_b_corr']
    idx_err = cols['m_b_corr_err_DIAG']

    z_all, mb_all, err_all = [], [], []
    for line in lines[1:]:
        parts = line.split()
        if len(parts) < max(idx_z, idx_mb, idx_err) + 1:
            continue
        z = float(parts[idx_z])
        mb = float(parts[idx_mb])
        err = float(parts[idx_err])
        if z > 0.001 and np.isfinite(mb) and np.isfinite(err) and err > 0 and err < 5.0:
            z_all.append(z)
            mb_all.append(mb)
            err_all.append(err)

    return np.array(z_all), np.array(mb_all), np.array(err_all)


def load_full_covariance():
    """Load the full 1701x1701 STAT+SYS covariance matrix.

    Format: first line = N (dimension), then N*N values in row-major order.
    The values can be multiple per line or one per line.
    """
    raw = download_or_cache(COV_URL, "pantheon_plus_cov_cache.txt")
    values = raw.split()
    N = int(values[0])
    print(f"  Covariance dimension: {N}x{N}")

    # The remaining values form the N*N matrix
    cov_flat = np.array([float(v) for v in values[1:]])
    expected = N * N
    print(f"  Read {len(cov_flat)} covariance values (expected {expected})")

    if len(cov_flat) < expected:
        raise RuntimeError(f"Covariance file too short: {len(cov_flat)} < {expected}")

    C = cov_flat[:expected].reshape(N, N)
    return N, C


print("=" * 65)
print("  FULL-COV-PANTHEON-70: Loading Data")
print("=" * 65)

t0 = time.time()

# Load SN data
z_raw, mb_raw, err_raw = load_pantheon_data()
N_sne = len(z_raw)
print(f"\n  Loaded {N_sne} SNe, z = [{z_raw.min():.5f}, {z_raw.max():.5f}]")

# Load full covariance
N_cov, C_full = load_full_covariance()

# Verify dimensions match
# The covariance file includes ALL 1701 SNe in the same order as the .dat file.
# Our filtering (z > 0.001, finite values, etc.) may exclude some.
# We need to match indices carefully.
print(f"\n  Data file SNe after cuts: {N_sne}")
print(f"  Covariance matrix dimension: {N_cov}")

# Re-load WITHOUT cuts to get the full ordered set, then apply cuts to covariance
raw_dat = download_or_cache(DATA_URL, "pantheon_plus_cache.dat")
lines = raw_dat.strip().split('\n')
header = lines[0].split()
cols = {name: i for i, name in enumerate(header)}
idx_z = cols['zHD']
idx_mb = cols['m_b_corr']
idx_err = cols['m_b_corr_err_DIAG']

z_full, mb_full, err_full = [], [], []
valid_mask = []  # True if this SN passes our cuts

for line in lines[1:]:
    parts = line.split()
    if len(parts) < max(idx_z, idx_mb, idx_err) + 1:
        continue
    z = float(parts[idx_z])
    mb = float(parts[idx_mb])
    err = float(parts[idx_err])
    z_full.append(z)
    mb_full.append(mb)
    err_full.append(err)
    passes = (z > 0.001 and np.isfinite(mb) and np.isfinite(err)
              and err > 0 and err < 5.0)
    valid_mask.append(passes)

z_full = np.array(z_full)
mb_full = np.array(mb_full)
err_full = np.array(err_full)
valid_mask = np.array(valid_mask)

print(f"  Total SNe in data file: {len(z_full)}")
print(f"  SNe passing cuts: {np.sum(valid_mask)}")

# Extract sub-covariance for valid SNe
# C_full should be N_cov x N_cov where N_cov matches len(z_full)
if N_cov != len(z_full):
    print(f"  WARNING: Covariance dim {N_cov} != data count {len(z_full)}")
    print(f"  Using min({N_cov}, {len(z_full)}) entries")
    n_use = min(N_cov, len(z_full))
    valid_mask = valid_mask[:n_use]
    z_full = z_full[:n_use]
    mb_full = mb_full[:n_use]
    err_full = err_full[:n_use]

# Get indices of valid SNe
valid_idx = np.where(valid_mask)[0]
N_valid = len(valid_idx)

# Extract sub-covariance matrix
C_sub = C_full[np.ix_(valid_idx, valid_idx)]

# Verify: diagonal should match err^2 approximately
diag_cov = np.diag(C_sub)
diag_err2 = err_full[valid_idx] ** 2
rel_diff = np.abs(diag_cov - diag_err2) / diag_err2
print(f"\n  Diagonal validation: max |C_ii - sigma_i^2| / sigma_i^2 = {np.max(rel_diff):.6f}")
print(f"  Mean relative difference = {np.mean(rel_diff):.6f}")

# Use valid data
z_data = z_full[valid_idx]
mb_data = mb_full[valid_idx]
err_data = err_full[valid_idx]

t_load = time.time() - t0
print(f"\n  Data loading time: {t_load:.1f}s")

# ==============================================================================
#  SECTION 2: Covariance Matrix Properties
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 2: Covariance Matrix Properties")
print("=" * 65)

# Condition number
cond_number = np.linalg.cond(C_sub)
print(f"\n  Matrix dimension: {N_valid} x {N_valid}")
print(f"  Condition number: {cond_number:.2e}")

# Off-diagonal magnitude
diag_sqrt = np.sqrt(np.diag(C_sub))
# Correlation matrix
corr_matrix = C_sub / np.outer(diag_sqrt, diag_sqrt)
np.fill_diagonal(corr_matrix, 0.0)  # zero out diagonal for off-diag stats

off_diag_abs = np.abs(corr_matrix)
print(f"\n  Off-diagonal correlation statistics:")
print(f"    Max |r_ij| = {np.max(off_diag_abs):.4f}")
print(f"    Mean |r_ij| = {np.mean(off_diag_abs):.6f}")
print(f"    Median |r_ij| = {np.median(off_diag_abs):.6f}")
print(f"    Fraction |r_ij| > 0.1: {np.mean(off_diag_abs > 0.1):.4f}")
print(f"    Fraction |r_ij| > 0.01: {np.mean(off_diag_abs > 0.01):.4f}")

# Ratio of off-diagonal to diagonal contribution
# ||C_off|| / ||C_diag|| in Frobenius norm
C_diag_only = np.diag(np.diag(C_sub))
C_off = C_sub - C_diag_only
frac_off = np.linalg.norm(C_off, 'fro') / np.linalg.norm(C_sub, 'fro')
print(f"\n  ||C_off||_F / ||C||_F = {frac_off:.4f}")
print(f"  Off-diagonal contribution: {frac_off*100:.1f}% of Frobenius norm")

# ==============================================================================
#  SECTION 3: Distance Modulus Computation
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 3: Computing Distance Moduli")
print("=" * 65)

# Framework parameters
# w0_FW = -0.918  # S72: now imported from canonical_constants
H0 = H_0_km_s_Mpc
Om = Omega_m
# w0_LCDM = -1.0  # S72: now imported from canonical_constants

print(f"\n  FW:   w_0 = {w0_FW}, Omega_m = {Om}, H_0 = {H0} km/s/Mpc")
print(f"  LCDM: w_0 = {w0_LCDM}, Omega_m = {Om}, H_0 = {H0} km/s/Mpc")


def H_wCDM(z, H0_val, Om_val, w0):
    """Hubble parameter for flat wCDM."""
    ODE = 1.0 - Om_val
    return H0_val * np.sqrt(Om_val * (1 + z)**3 + ODE * (1 + z)**(3 * (1 + w0)))


def distance_modulus_array(z_arr, H0_val, Om_val, w0):
    """
    Distance modulus mu(z) = 5 * log10(d_L / 10 pc) for flat wCDM.
    d_L(z) = (1+z) * (c/H0) * integral_0^z dz'/E(z')
    Returns mu in magnitudes. d_L in Mpc, so mu = 5*log10(d_L) + 25.
    """
    mu = np.zeros(len(z_arr))

    # Sort for efficiency in integration
    sort_idx = np.argsort(z_arr)
    z_sorted = z_arr[sort_idx]

    for j, zi in enumerate(z_sorted):
        def integrand(zp):
            return 1.0 / H_wCDM(zp, H0_val, Om_val, w0)
        result, _ = integrate.quad(integrand, 0, zi, limit=100)
        dl_Mpc = (1 + zi) * c_light_km_s * result
        mu[sort_idx[j]] = 5.0 * np.log10(dl_Mpc) + 25.0

    return mu


# Compute model predictions at each SN redshift
print(f"\n  Computing FW distance moduli for {N_valid} SNe...")
t1 = time.time()
mu_FW = distance_modulus_array(z_data, H0, Om, w0_FW)
t_fw = time.time() - t1
print(f"    Done in {t_fw:.1f}s")

print(f"  Computing LCDM distance moduli for {N_valid} SNe...")
t1 = time.time()
mu_LCDM = distance_modulus_array(z_data, H0, Om, w0_LCDM)
t_lcdm = time.time() - t1
print(f"    Done in {t_lcdm:.1f}s")

# ==============================================================================
#  SECTION 4: Chi^2 with Full Covariance
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 4: Chi^2 with Full Covariance Matrix")
print("=" * 65)


def chi2_with_covariance(mu_model, mb_obs, cov_matrix):
    """
    Compute chi^2 with full covariance, analytically marginalizing over M_B.

    chi^2 = min_{M_B} (m_b - mu - M_B)^T C^{-1} (m_b - mu - M_B)

    Analytical minimum:
      M_B = (1^T C^{-1} delta) / (1^T C^{-1} 1)
      where delta = m_b - mu

    Then:
      chi^2 = delta^T C^{-1} delta - (1^T C^{-1} delta)^2 / (1^T C^{-1} 1)

    This is the standard Pantheon+ analysis approach (Brout et al. 2022).
    """
    delta = mb_obs - mu_model
    ones = np.ones(len(mb_obs))

    # Solve C x = delta and C y = 1 via Cholesky
    # More numerically stable than explicit inversion
    try:
        L = linalg.cholesky(cov_matrix, lower=True)
        x = linalg.cho_solve((L, True), delta)  # C^{-1} delta
        y = linalg.cho_solve((L, True), ones)    # C^{-1} 1
    except linalg.LinAlgError:
        # Fall back to LU decomposition if Cholesky fails
        print("    WARNING: Cholesky failed, using LU decomposition")
        x = linalg.solve(cov_matrix, delta)
        y = linalg.solve(cov_matrix, ones)

    # Analytical M_B
    M_B = np.dot(ones, x) / np.dot(ones, y)

    # chi^2 with marginalised M_B
    chi2 = np.dot(delta, x) - (np.dot(ones, x))**2 / np.dot(ones, y)

    return M_B, chi2


def chi2_diagonal(mu_model, mb_obs, sigma):
    """Chi^2 with diagonal errors only (reproduces S69 approach)."""
    delta = mb_obs - mu_model
    w = 1.0 / sigma**2  # (local)

    M_B = np.sum(w * delta) / np.sum(w)
    chi2 = np.sum(((delta - M_B) / sigma)**2)
    return M_B, chi2


# --- Full covariance chi^2 ---
print("\n  Full covariance analysis:")
t1 = time.time()

MB_FW_full, chi2_FW_full = chi2_with_covariance(mu_FW, mb_data, C_sub)
MB_LCDM_full, chi2_LCDM_full = chi2_with_covariance(mu_LCDM, mb_data, C_sub)

dof_full = N_valid - 1  # 1 marginalised parameter (M_B)
chi2_dof_FW_full = chi2_FW_full / dof_full
chi2_dof_LCDM_full = chi2_LCDM_full / dof_full
delta_chi2_full = chi2_FW_full - chi2_LCDM_full

t_chi2 = time.time() - t1
print(f"    Computation time: {t_chi2:.2f}s")

print(f"\n    FW (w={w0_FW}):")
print(f"      M_B = {MB_FW_full:.6f} mag")
print(f"      chi^2 = {chi2_FW_full:.2f}")
print(f"      dof = {dof_full}")
print(f"      chi^2/dof = {chi2_dof_FW_full:.6f}")

print(f"\n    LCDM (w=-1):")
print(f"      M_B = {MB_LCDM_full:.6f} mag")
print(f"      chi^2 = {chi2_LCDM_full:.2f}")
print(f"      dof = {dof_full}")
print(f"      chi^2/dof = {chi2_dof_LCDM_full:.6f}")

print(f"\n    Delta chi^2 (FW - LCDM) = {delta_chi2_full:.4f}")
if delta_chi2_full < 0:
    print(f"    FW preferred by |Delta chi^2| = {abs(delta_chi2_full):.2f}")
else:
    print(f"    LCDM preferred by Delta chi^2 = {delta_chi2_full:.2f}")

# --- Diagonal chi^2 (reproduce S69 for consistency) ---
print("\n  Diagonal-only analysis (S69 cross-check):")

MB_FW_diag, chi2_FW_diag = chi2_diagonal(mu_FW, mb_data, err_data)
MB_LCDM_diag, chi2_LCDM_diag = chi2_diagonal(mu_LCDM, mb_data, err_data)

dof_diag = N_valid - 1
chi2_dof_FW_diag = chi2_FW_diag / dof_diag
chi2_dof_LCDM_diag = chi2_LCDM_diag / dof_diag
delta_chi2_diag = chi2_FW_diag - chi2_LCDM_diag

print(f"\n    FW:   chi^2/dof = {chi2_dof_FW_diag:.6f} ({chi2_FW_diag:.2f}/{dof_diag})")
print(f"    LCDM: chi^2/dof = {chi2_dof_LCDM_diag:.6f} ({chi2_LCDM_diag:.2f}/{dof_diag})")
print(f"    Delta chi^2 (diag) = {delta_chi2_diag:.4f}")
print(f"    S69 reference: Delta chi^2 = -4.47 (binned, 37 bins)")

# ==============================================================================
#  SECTION 5: Comparison: Full Covariance vs Diagonal
# ==============================================================================

print("\n" + "=" * 65)
print("  SECTION 5: Full Covariance vs Diagonal Comparison")
print("=" * 65)

print(f"\n  {'Quantity':<30} {'Diagonal':>12} {'Full Cov':>12} {'Change':>12}")
print(f"  {'-'*30} {'-'*12} {'-'*12} {'-'*12}")
print(f"  {'chi^2_FW':<30} {chi2_FW_diag:>12.2f} {chi2_FW_full:>12.2f} {chi2_FW_full-chi2_FW_diag:>+12.2f}")
print(f"  {'chi^2_LCDM':<30} {chi2_LCDM_diag:>12.2f} {chi2_LCDM_full:>12.2f} {chi2_LCDM_full-chi2_LCDM_diag:>+12.2f}")
print(f"  {'chi^2/dof FW':<30} {chi2_dof_FW_diag:>12.6f} {chi2_dof_FW_full:>12.6f} {chi2_dof_FW_full-chi2_dof_FW_diag:>+12.6f}")
print(f"  {'chi^2/dof LCDM':<30} {chi2_dof_LCDM_diag:>12.6f} {chi2_dof_LCDM_full:>12.6f} {chi2_dof_LCDM_full-chi2_dof_LCDM_diag:>+12.6f}")
print(f"  {'Delta chi^2 (FW-LCDM)':<30} {delta_chi2_diag:>12.4f} {delta_chi2_full:>12.4f} {delta_chi2_full-delta_chi2_diag:>+12.4f}")
print(f"  {'M_B (FW)':<30} {MB_FW_diag:>12.6f} {MB_FW_full:>12.6f} {MB_FW_full-MB_FW_diag:>+12.6f}")
print(f"  {'M_B (LCDM)':<30} {MB_LCDM_diag:>12.6f} {MB_LCDM_full:>12.6f} {MB_LCDM_full-MB_LCDM_diag:>+12.6f}")

# Assessment
print(f"\n  Assessment:")
shift = delta_chi2_full - delta_chi2_diag
if abs(shift) < 1.0:
    print(f"    Off-diagonal correlations shift Delta chi^2 by {shift:+.2f}")
    print(f"    This is a small correction — the S69 diagonal result is robust.")
elif shift > 0:
    print(f"    Off-diagonal correlations shift Delta chi^2 by {shift:+.2f}")
    print(f"    FW preference WEAKENED by {abs(shift):.1f} chi^2 units with full covariance.")
    if delta_chi2_full > 0:
        print(f"    SIGN FLIP: LCDM now preferred with full covariance!")
else:
    print(f"    Off-diagonal correlations shift Delta chi^2 by {shift:+.2f}")
    print(f"    FW preference STRENGTHENED by {abs(shift):.1f} chi^2 units with full covariance.")

# Effective sigma of model comparison
from scipy.stats import chi2 as chi2_dist
if delta_chi2_full < 0:
    # FW preferred: p-value for LCDM under chi^2 difference (1 dof)
    p_value = chi2_dist.sf(abs(delta_chi2_full), 1)
    sigma_equiv = -1  # placeholder
    from scipy.special import erfinv
    sigma_equiv = np.sqrt(2) * erfinv(1 - p_value)
    print(f"\n    Effective significance of FW preference: {sigma_equiv:.2f}-sigma")
    print(f"    (p-value = {p_value:.4e} from Delta chi^2 = {delta_chi2_full:.2f} with 1 dof)")
else:
    p_value = chi2_dist.sf(abs(delta_chi2_full), 1)
    from scipy.special import erfinv
    sigma_equiv = np.sqrt(2) * erfinv(1 - p_value)
    print(f"\n    Effective significance of LCDM preference: {sigma_equiv:.2f}-sigma")
    print(f"    (p-value = {p_value:.4e} from Delta chi^2 = {delta_chi2_full:.2f} with 1 dof)")

# ==============================================================================
#  SECTION 6: Binned Analysis with Propagated Covariance
# ==============================================================================
# Also bin the covariance for comparison with S69 binned result

print("\n" + "=" * 65)
print("  SECTION 6: Binned Covariance Analysis")
print("=" * 65)

N_BINS = 40
z_edges = np.logspace(np.log10(0.001), np.log10(2.5), N_BINS + 1)

# Assign each SN to a bin
bin_idx = np.digitize(z_data, z_edges) - 1  # 0-indexed
bin_idx = np.clip(bin_idx, 0, N_BINS - 1)

# Identify non-empty bins
occupied = [i for i in range(N_BINS) if np.sum(bin_idx == i) > 0]
N_occ = len(occupied)

# Build the binning matrix B: N_occ x N_valid
# B_ki = w_i / sum_j(w_j) for SNe j in bin k, where w = 1/sigma^2
# Then: z_bin = B @ z_data, mb_bin = B @ mb_data
# And: C_bin = B @ C_sub @ B^T

B = np.zeros((N_occ, N_valid))
z_bin = np.zeros(N_occ)
mb_bin = np.zeros(N_occ)
n_per_bin = np.zeros(N_occ, dtype=int)

for k_idx, k_bin in enumerate(occupied):
    mask = (bin_idx == k_bin)
    n = np.sum(mask)
    n_per_bin[k_idx] = n
    w = 1.0 / err_data[mask]**2  # (local)
    w_sum = np.sum(w)
    # Fill B matrix
    sn_indices = np.where(mask)[0]
    for j, sn_j in enumerate(sn_indices):
        B[k_idx, sn_j] = (1.0 / err_data[sn_j]**2) / w_sum
    z_bin[k_idx] = np.sum(w * z_data[mask]) / w_sum
    mb_bin[k_idx] = np.sum(w * mb_data[mask]) / w_sum

# Propagated binned covariance: C_bin = B C B^T
C_bin = B @ C_sub @ B.T
err_bin = np.sqrt(np.diag(C_bin))

# Model predictions at bin centres
mu_FW_bin = distance_modulus_array(z_bin, H0, Om, w0_FW)
mu_LCDM_bin = distance_modulus_array(z_bin, H0, Om, w0_LCDM)

# Chi^2 with binned full covariance
MB_FW_bin_full, chi2_FW_bin_full = chi2_with_covariance(mu_FW_bin, mb_bin, C_bin)
MB_LCDM_bin_full, chi2_LCDM_bin_full = chi2_with_covariance(mu_LCDM_bin, mb_bin, C_bin)
dof_bin = N_occ - 1
chi2_dof_FW_bin_full = chi2_FW_bin_full / dof_bin
chi2_dof_LCDM_bin_full = chi2_LCDM_bin_full / dof_bin
delta_chi2_bin_full = chi2_FW_bin_full - chi2_LCDM_bin_full

# Chi^2 with binned diagonal only
MB_FW_bin_diag, chi2_FW_bin_diag = chi2_diagonal(mu_FW_bin, mb_bin, err_bin)
MB_LCDM_bin_diag, chi2_LCDM_bin_diag = chi2_diagonal(mu_LCDM_bin, mb_bin, err_bin)
delta_chi2_bin_diag = chi2_FW_bin_diag - chi2_LCDM_bin_diag

print(f"\n  Binned analysis ({N_occ} bins from {N_valid} SNe):")
print(f"  {'Quantity':<30} {'Bin Diag':>12} {'Bin Full':>12} {'S69 ref':>12}")
print(f"  {'-'*30} {'-'*12} {'-'*12} {'-'*12}")
print(f"  {'chi^2/dof FW':<30} {chi2_FW_bin_diag/dof_bin:>12.4f} {chi2_dof_FW_bin_full:>12.4f} {'1.0249':>12}")
print(f"  {'chi^2/dof LCDM':<30} {chi2_LCDM_bin_diag/dof_bin:>12.4f} {chi2_dof_LCDM_bin_full:>12.4f} {'1.1491':>12}")
print(f"  {'Delta chi^2':<30} {delta_chi2_bin_diag:>12.4f} {delta_chi2_bin_full:>12.4f} {'-4.4723':>12}")

# Off-diagonal contribution in binned covariance
C_bin_diag_only = np.diag(np.diag(C_bin))
C_bin_off = C_bin - C_bin_diag_only
frac_off_bin = np.linalg.norm(C_bin_off, 'fro') / np.linalg.norm(C_bin, 'fro')
print(f"\n  Binned covariance off-diagonal fraction: {frac_off_bin*100:.1f}%")

# Correlation structure of binned covariance
diag_bin_sqrt = np.sqrt(np.diag(C_bin))
corr_bin = C_bin / np.outer(diag_bin_sqrt, diag_bin_sqrt)
print(f"  Binned correlation: max off-diag = {np.max(np.abs(corr_bin - np.eye(N_occ))):.4f}")

# ==============================================================================
#  SECTION 7: Gate Verdict
# ==============================================================================

print("\n" + "=" * 65)
print("  GATE VERDICT: FULL-COV-PANTHEON-70")
print("=" * 65)

print(f"\n  Gate type: INFO (sharpening of S69 result)")
print(f"\n  Primary result: Delta chi^2 with full 1701x1701 covariance")
print(f"    Delta chi^2 (full cov, unbinned) = {delta_chi2_full:.4f}")
print(f"    Delta chi^2 (diag only, unbinned) = {delta_chi2_diag:.4f}")
print(f"    S69 reference (diag, binned) = -4.4723")
print(f"\n  Shift from off-diagonal terms: {delta_chi2_full - delta_chi2_diag:+.4f}")
if delta_chi2_full < 0:
    print(f"\n  >>> GATE FULL-COV-PANTHEON-70: INFO — FW preference {'' if delta_chi2_full < delta_chi2_diag else 'weakened but '}survives full covariance <<<")
    print(f"  Delta chi^2 = {delta_chi2_full:.2f} (full cov) vs {delta_chi2_diag:.2f} (diagonal)")
else:
    print(f"\n  >>> GATE FULL-COV-PANTHEON-70: INFO — FW preference REVERSED by full covariance <<<")
    print(f"  Delta chi^2 = {delta_chi2_full:.2f} (full cov) vs {delta_chi2_diag:.2f} (diagonal)")

verdict = "INFO"

# ==============================================================================
#  SECTION 8: Plotting
# ==============================================================================

print("\n  Generating plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# --- Panel 1: Binned Hubble diagram ---
ax1 = axes[0, 0]
ax1.errorbar(z_bin, mb_bin, yerr=err_bin, fmt='o', color='k', markersize=3,
             capsize=1, label=f'Pantheon+ ({N_occ} bins)', zorder=5)
z_fine = np.logspace(np.log10(0.003), np.log10(2.8), 200)
mu_FW_fine = distance_modulus_array(z_fine, H0, Om, w0_FW)
mu_LCDM_fine = distance_modulus_array(z_fine, H0, Om, w0_LCDM)
ax1.plot(z_fine, mu_FW_fine + MB_FW_bin_full, 'b-', lw=1.5,
         label=f'FW (w={w0_FW})')
ax1.plot(z_fine, mu_LCDM_fine + MB_LCDM_bin_full, 'r--', lw=1.5,
         label=r'$\Lambda$CDM (w=$-$1)')
ax1.set_xscale('log')
ax1.set_ylabel(r'$m_B^{\rm corr}$ (mag)', fontsize=11)
ax1.set_title('Pantheon+ Hubble Diagram', fontsize=12)
ax1.legend(fontsize=9, loc='lower right')
ax1.set_xlim(0.003, 3.0)
ax1.grid(True, alpha=0.3)

# --- Panel 2: Binned residuals ---
ax2 = axes[0, 1]
res_FW_bin = mb_bin - mu_FW_bin - MB_FW_bin_full
res_LCDM_bin = mb_bin - mu_LCDM_bin - MB_LCDM_bin_full
ax2.errorbar(z_bin, res_FW_bin * 1000, yerr=err_bin * 1000, fmt='o', color='blue',
             markersize=3, capsize=1, label=f'FW residuals')
ax2.errorbar(z_bin * 1.03, res_LCDM_bin * 1000, yerr=err_bin * 1000, fmt='s',
             color='red', markersize=3, capsize=1, alpha=0.6,
             label=r'$\Lambda$CDM residuals')
ax2.axhline(0, color='k', ls='-', lw=0.5)
ax2.set_xscale('log')
ax2.set_ylabel(r'$\Delta m_B$ (mmag)', fontsize=11)
ax2.set_title('Hubble Residuals (binned, full cov)', fontsize=12)
ax2.legend(fontsize=9)
ax2.set_xlim(0.003, 3.0)
ax2.grid(True, alpha=0.3)

# --- Panel 3: Binned covariance correlation matrix ---
ax3 = axes[1, 0]
im = ax3.imshow(corr_bin, cmap='RdBu_r', vmin=-0.3, vmax=0.3,
                aspect='auto', origin='lower')
ax3.set_xlabel('Bin index', fontsize=11)
ax3.set_ylabel('Bin index', fontsize=11)
ax3.set_title('Binned Correlation Matrix', fontsize=12)
plt.colorbar(im, ax=ax3, label=r'$r_{ij}$')

# --- Panel 4: Delta chi^2 comparison ---
ax4 = axes[1, 1]
categories = ['S69\n(binned diag)', 'Unbinned\ndiag', 'Unbinned\nfull cov',
              'Binned\nfull cov']
values = [-4.4723, delta_chi2_diag, delta_chi2_full, delta_chi2_bin_full]
colors = ['#aaaaaa', '#66b3ff', '#ff6666', '#99ff99']

bars = ax4.bar(categories, values, color=colors, edgecolor='k', width=0.6)
ax4.axhline(0, color='k', ls='-', lw=1)
ax4.set_ylabel(r'$\Delta\chi^2$ (FW $-$ $\Lambda$CDM)', fontsize=11)
ax4.set_title(r'Model Comparison: $\Delta\chi^2$', fontsize=12)

# Add value labels on bars
for bar, val in zip(bars, values):
    y_pos = val - 0.3 if val < 0 else val + 0.1
    ax4.text(bar.get_x() + bar.get_width() / 2, y_pos,
             f'{val:.2f}', ha='center', va='top' if val < 0 else 'bottom',
             fontsize=10, fontweight='bold')

ax4.grid(True, alpha=0.3, axis='y')
# Shade the "FW preferred" region
ylim = ax4.get_ylim()
ax4.fill_between([-0.5, 3.5], [ylim[0]]*2, [0]*2, alpha=0.05, color='blue',
                 label='FW preferred')
ax4.set_xlim(-0.5, 3.5)

fig.suptitle('FULL-COV-PANTHEON-70: Pantheon+ with Full Covariance',
             fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig(out_dir / 's70_full_cov_pantheon.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: {out_dir / 's70_full_cov_pantheon.png'}")

# ==============================================================================
#  SECTION 9: Save Results
# ==============================================================================

np.savez(out_dir / 's70_full_cov_pantheon.npz',
    # Full covariance unbinned
    chi2_FW_full=chi2_FW_full,
    chi2_LCDM_full=chi2_LCDM_full,
    chi2_dof_FW_full=chi2_dof_FW_full,
    chi2_dof_LCDM_full=chi2_dof_LCDM_full,
    delta_chi2_full=delta_chi2_full,
    MB_FW_full=MB_FW_full,
    MB_LCDM_full=MB_LCDM_full,
    # Diagonal unbinned (cross-check)
    chi2_FW_diag=chi2_FW_diag,
    chi2_LCDM_diag=chi2_LCDM_diag,
    delta_chi2_diag=delta_chi2_diag,
    MB_FW_diag=MB_FW_diag,
    MB_LCDM_diag=MB_LCDM_diag,
    # Binned full cov
    chi2_FW_bin_full=chi2_FW_bin_full,
    chi2_LCDM_bin_full=chi2_LCDM_bin_full,
    delta_chi2_bin_full=delta_chi2_bin_full,
    chi2_dof_FW_bin_full=chi2_dof_FW_bin_full,
    chi2_dof_LCDM_bin_full=chi2_dof_LCDM_bin_full,
    # Binned diagonal
    chi2_FW_bin_diag=chi2_FW_bin_diag,
    chi2_LCDM_bin_diag=chi2_LCDM_bin_diag,
    delta_chi2_bin_diag=delta_chi2_bin_diag,
    # Covariance properties
    cov_condition_number=cond_number,
    off_diag_frac_unbinned=frac_off,
    off_diag_frac_binned=frac_off_bin,
    # Binned data
    z_bin=z_bin, mb_bin=mb_bin, err_bin=err_bin, n_per_bin=n_per_bin,
    mu_FW_bin=mu_FW_bin, mu_LCDM_bin=mu_LCDM_bin,
    # Parameters
    w0_FW=w0_FW, w0_LCDM=w0_LCDM, H0=H0, Omega_m_val=Om,
    N_valid=N_valid, N_bins=N_occ, N_cov=N_cov,
    # Gate
    verdict=verdict,
)
print(f"\n  Data saved: {out_dir / 's70_full_cov_pantheon.npz'}")

total_time = time.time() - t0
print(f"\n  Total computation time: {total_time:.1f}s")

print("\n" + "=" * 65)
print("  COMPUTATION COMPLETE")
print("=" * 65)
