#!/usr/bin/env python3
"""
s38_otoc_bcs.py — OTOC of BCS gap operator in 0D Fock space (CHAOS-2)

Computes the out-of-time-ordered correlator F(t) = -<[A(t), A(0)]^2>_beta
for the pairing gap operator A = (Delta + Delta^dag)/sqrt(2) in the
reduced BCS Hamiltonian on 8 pairing modes (B2 x4, B1, B3 x3).

Diagnostics:
  1. OTOC F(t) at multiple temperatures -> Lyapunov exponent lambda_L
  2. MSS bound check: lambda_L <= 2*pi*T
  3. Level spacing statistics of H_BCS many-body spectrum
  4. Spectral form factor K(t) = |Tr(e^{-iHt})|^2 / (Tr(1))^2
  5. Scrambling time t_scr vs transit time t_transit (CHAOS-3)

Gate CHAOS-2: lambda_L > 0 with exponential growth => PASS (chaos)
             No exponential regime => FAIL (not chaotic)
             lambda_L > 2*pi*T => KILL (MSS violation)

Gate CHAOS-3: t_scr < t_transit => PASS (scrambling during transit)
             t_scr >> t_transit => FAIL (no scrambling)

Author: Kitaev-Quantum-Chaos-Theorist
Date: 2026-03-08
"""

import numpy as np
from scipy import linalg as la
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import time

# ============================================================
# 1. EXTRACT PARAMETERS FROM DATA FILES
# ============================================================

print("=" * 70)
print("CHAOS-2: OTOC of BCS Gap Operator in 0D Fock Space")
print("=" * 70)

# Load pairing data
d37 = np.load('tier0-computation/s37_pair_susceptibility.npz', allow_pickle=True)
d37i = np.load('tier0-computation/s37_instanton_action.npz', allow_pickle=True)

E_8 = d37['E_8']           # Single-particle energies (8 modes)
V_8x8 = d37['V_8x8']       # Pairing matrix V_{kk'}
rho_8 = d37['rho']          # DOS weights per mode
branch_labels = d37['branch_labels']
mu = float(d37['mu'])       # Chemical potential = 0
n_modes = int(d37['n_modes'])

# Transit time data
d36 = np.load('tier0-computation/s36_tau_dynamics.npz', allow_pickle=True)
t_transit_full = float(d36['an_S_full_dt_transit'])  # in natural units
tau_BCS = float(d36['tau_BCS'])

print(f"\nParameters:")
print(f"  n_modes = {n_modes}")
print(f"  E_8 = {E_8}")
print(f"  mu = {mu}")
print(f"  branch_labels = {branch_labels}")
print(f"  rho (DOS weights) = {rho_8}")
print(f"  V_8x8 max = {np.max(np.abs(V_8x8)):.6f}")
print(f"  V_B2B2 off-diag max = {np.max(np.abs(V_8x8[:4,:4] - np.diag(np.diag(V_8x8[:4,:4])))):.6f}")
print(f"  t_transit (full gradient) = {t_transit_full:.6e}")
print(f"  tau_BCS = {tau_BCS}")

# ============================================================
# 2. BUILD THE BCS HAMILTONIAN IN PAIR FOCK SPACE
# ============================================================
# The reduced BCS Hamiltonian in the pair basis:
#   H = sum_k (2*xi_k - V_kk) * n_k - sum_{k!=k'} V_{kk'} * P_k^dag P_k'
# where xi_k = E_k - mu, n_k = pair occupation (0 or 1),
# P_k^dag creates a pair in mode k, P_k annihilates it.
#
# In the pair Fock space, each state |n_1, ..., n_8> has n_k in {0,1}.
# Dimension: 2^8 = 256.
#
# Note: The DOS-weighted version uses V_{kk'} * sqrt(rho_k * rho_k')
# to account for the density of states at each mode. This is the
# physical pairing interaction strength.

N = n_modes  # 8 modes
dim = 2**N   # 256 states

print(f"\nFock space dimension: {dim}")

# Single-particle energies relative to Fermi level
xi = E_8 - mu  # xi_k = E_k - mu (mu=0)

# Build the DOS-weighted pairing matrix
# Physical pairing: V_phys_{kk'} = V_{kk'} * sqrt(rho_k * rho_k')
V_phys = V_8x8 * np.sqrt(np.outer(rho_8, rho_8))

print(f"\n  V_phys max = {np.max(np.abs(V_phys)):.6f}")
print(f"  V_phys B2-B2 block max = {np.max(np.abs(V_phys[:4,:4])):.6f}")

# Basis: binary representation of integers 0..255
# Bit k set => pair in mode k occupied

def build_H_BCS(xi, V, N, dim):
    """Build BCS Hamiltonian in pair Fock space."""
    H = np.zeros((dim, dim), dtype=np.float64)

    for alpha in range(dim):
        # Diagonal: kinetic energy + Hartree shift
        E_diag = 0.0
        for k in range(N):
            if alpha & (1 << k):
                E_diag += 2 * xi[k] - V[k, k]
        H[alpha, alpha] = E_diag

        # Off-diagonal: pair scattering P_k^dag P_k'
        # |alpha> -> |beta> where pair moves from k' to k
        for k in range(N):
            for kp in range(N):
                if k == kp:
                    continue
                # Check: mode kp occupied, mode k empty in |alpha>
                if (alpha & (1 << kp)) and not (alpha & (1 << k)):
                    beta = (alpha ^ (1 << kp)) | (1 << k)  # remove kp, add k
                    H[beta, alpha] -= V[k, kp]

    return H

print("\nBuilding H_BCS (256 x 256)...")
t0 = time.time()
H_BCS = build_H_BCS(xi, V_phys, N, dim)
t1 = time.time()
print(f"  Build time: {t1-t0:.3f}s")

# Verify Hermiticity
herm_err = np.max(np.abs(H_BCS - H_BCS.T))
print(f"  Hermiticity error: {herm_err:.2e}")
assert herm_err < 1e-12, f"H_BCS not Hermitian: error = {herm_err}"

# Diagonalize
print("  Diagonalizing H_BCS...")
evals, evecs = la.eigh(H_BCS)
print(f"  E_min = {evals[0]:.6f}, E_max = {evals[-1]:.6f}")
print(f"  Spectrum width = {evals[-1] - evals[0]:.6f}")
print(f"  Ground state energy = {evals[0]:.6f}")

# Check number of pairs in ground state
gs = evecs[:, 0]
n_pairs_gs = sum(
    np.sum(np.abs(gs[alpha])**2 * bin(alpha).count('1'))
    for alpha in range(dim)
    if np.abs(gs[alpha]) > 1e-15
) / np.sum(np.abs(gs)**2)
# Simpler computation:
n_pairs_expectation = 0.0
for alpha in range(dim):
    n_p = bin(alpha).count('1')
    n_pairs_expectation += np.abs(gs[alpha])**2 * n_p
print(f"  <N_pair> in ground state = {n_pairs_expectation:.3f}")

# ============================================================
# 3. LEVEL SPACING STATISTICS OF H_BCS (MANY-BODY)
# ============================================================

print("\n" + "=" * 70)
print("MANY-BODY LEVEL SPACING STATISTICS")
print("=" * 70)

# The BCS Hamiltonian conserves total pair number N_pair = sum_k n_k.
# We should compute level statistics WITHIN each N_pair sector.

# Sort eigenvalues by N_pair sector
n_pair_list = np.array([bin(alpha).count('1') for alpha in range(dim)])

# For each sector, find eigenvalues
sector_evals = {}
for n_p in range(N + 1):
    mask = (n_pair_list == n_p)
    sector_dim = np.sum(mask)
    if sector_dim == 0:
        continue
    # Project H_BCS to this sector
    indices = np.where(mask)[0]
    H_sector = H_BCS[np.ix_(indices, indices)]
    ev = la.eigvalsh(H_sector)
    sector_evals[n_p] = ev
    print(f"  N_pair = {n_p}: dim = {sector_dim}, "
          f"C({N},{n_p}) = {__import__('math').comb(N, n_p)}, "
          f"E_range = [{ev[0]:.4f}, {ev[-1]:.4f}]")

# Compute r-ratio for each sector
def compute_r_ratio(evals, min_levels=4):
    """Compute the ratio statistic r = min(s_n, s_{n+1})/max(s_n, s_{n+1})."""
    if len(evals) < min_levels:
        return np.nan, np.nan, 0
    spacings = np.diff(np.sort(evals))
    # Remove zero spacings (degeneracies)
    spacings = spacings[spacings > 1e-12 * np.mean(np.abs(spacings) + 1e-30)]
    if len(spacings) < 3:
        return np.nan, np.nan, 0
    ratios = np.minimum(spacings[:-1], spacings[1:]) / np.maximum(spacings[:-1], spacings[1:])
    return np.mean(ratios), np.std(ratios) / np.sqrt(len(ratios)), len(ratios)

print(f"\n  {'N_pair':>6} {'dim':>5} {'<r>':>8} {'err':>8} {'N_ratios':>8} {'Class':>12}")
print(f"  {'-'*6} {'-'*5} {'-'*8} {'-'*8} {'-'*8} {'-'*12}")

r_by_sector = {}
for n_p in sorted(sector_evals.keys()):
    ev = sector_evals[n_p]
    r_mean, r_err, n_ratios = compute_r_ratio(ev)
    r_by_sector[n_p] = (r_mean, r_err, n_ratios)
    if np.isnan(r_mean):
        cls = "N/A"
    elif r_mean > 0.50:
        cls = "GOE"
    elif r_mean > 0.42:
        cls = "INTERMEDIATE"
    elif r_mean > 0.36:
        cls = "POISSON"
    else:
        cls = "SUB-POISSON"
    print(f"  {n_p:>6} {len(ev):>5} {r_mean:>8.4f} {r_err:>8.4f} {n_ratios:>8} {cls:>12}")

# Also compute for FULL spectrum (pooled, no sector decomposition)
r_full, r_full_err, n_full = compute_r_ratio(evals)
print(f"\n  Full spectrum (pooled): <r> = {r_full:.4f} +/- {r_full_err:.4f} (N={n_full})")

# Pooled across sectors with enough levels
pooled_ratios = []
for n_p in sorted(sector_evals.keys()):
    ev = sector_evals[n_p]
    if len(ev) < 6:
        continue
    spacings = np.diff(np.sort(ev))
    spacings = spacings[spacings > 1e-12 * np.mean(np.abs(spacings) + 1e-30)]
    if len(spacings) >= 3:
        ratios = np.minimum(spacings[:-1], spacings[1:]) / np.maximum(spacings[:-1], spacings[1:])
        pooled_ratios.extend(ratios)

if pooled_ratios:
    pooled_ratios = np.array(pooled_ratios)
    print(f"  Pooled within-sector: <r> = {np.mean(pooled_ratios):.4f} +/- "
          f"{np.std(pooled_ratios)/np.sqrt(len(pooled_ratios)):.4f} (N={len(pooled_ratios)})")

# ============================================================
# 4. BUILD THE GAP OPERATOR
# ============================================================

print("\n" + "=" * 70)
print("BUILDING GAP OPERATOR")
print("=" * 70)

# Delta = sum_k c_{k,down} c_{k,up} = sum_k P_k (pair annihilation)
# In pair Fock space: Delta|...,1_k,...> = |...,0_k,...> (removes pair at k)
# Delta^dag|...,0_k,...> = |...,1_k,...> (creates pair at k)
#
# We weight by sqrt(rho_k) to match the DOS-weighted BCS convention.
# A = (Delta + Delta^dag) / sqrt(2) is Hermitian.

# Also define B = (Delta - Delta^dag) / (i*sqrt(2)) as the imaginary part.

def build_pair_operator(N, dim, rho):
    """Build Delta = sum_k sqrt(rho_k) * P_k (DOS-weighted pair annihilation)."""
    Delta = np.zeros((dim, dim), dtype=np.float64)
    for alpha in range(dim):
        for k in range(N):
            if alpha & (1 << k):  # mode k occupied
                beta = alpha ^ (1 << k)  # remove pair at k
                Delta[beta, alpha] += np.sqrt(rho[k])
    return Delta

Delta_op = build_pair_operator(N, dim, rho_8)
Delta_dag = Delta_op.T  # Hermitian conjugate (real matrix, so just transpose)

# Verify Delta^dag Delta is positive semi-definite
DdD = Delta_dag @ Delta_op
print(f"  ||Delta|| = {la.norm(Delta_op):.6f}")
print(f"  Tr(Delta^dag Delta) = {np.trace(DdD):.6f}")

# Hermitian gap operator
A = (Delta_op + Delta_dag) / np.sqrt(2)
# Verify Hermiticity
assert np.max(np.abs(A - A.T)) < 1e-14, "A is not Hermitian"
print(f"  ||A|| = {la.norm(A):.6f}")

# Also build pair number operator
N_pair_op = np.zeros((dim, dim), dtype=np.float64)
for alpha in range(dim):
    N_pair_op[alpha, alpha] = bin(alpha).count('1')

# Check [H, N_pair] -- should be zero if H conserves pair number
comm_HN = H_BCS @ N_pair_op - N_pair_op @ H_BCS
print(f"  ||[H_BCS, N_pair]|| = {la.norm(comm_HN):.2e}")

# Check [H, A] -- should be nonzero (A changes pair number by 1)
comm_HA = H_BCS @ A - A @ H_BCS
print(f"  ||[H_BCS, A]|| = {la.norm(comm_HA):.6f}")

# ============================================================
# 5. COMPUTE OTOC F(t) = -<[A(t), A(0)]^2>_beta
# ============================================================

print("\n" + "=" * 70)
print("COMPUTING OTOC")
print("=" * 70)

# Method: exact diagonalization.
# H_BCS = U D U^T where D = diag(evals)
# A(t) = U^T exp(iDt) U A U^T exp(-iDt) U
# [A(t), A(0)] computed as matrix
# F(t) = -Tr(rho [A(t), A(0)]^2) / Z

# Transform A to energy eigenbasis
A_eig = evecs.T @ A @ evecs  # A in eigenbasis

# Temperature scan
beta_values = np.array([0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0])
# Time scan: use units of 1/omega_PV where omega_PV = 0.792
omega_PV = 0.792
t_max = 80.0  # in natural units
n_times = 2000
t_array = np.linspace(0, t_max, n_times)

print(f"  Temperature scan: beta = {beta_values}")
print(f"  Time scan: t = 0 to {t_max}, {n_times} points")
print(f"  omega_PV = {omega_PV}")

# Precompute energy differences
E_diff = evals[:, None] - evals[None, :]  # E_i - E_j

# The OTOC in the energy eigenbasis:
# C(t) = [A(t), A(0)]
# C_{ij}(t) = sum_{m} A_{im} A_{mj} (e^{i(E_i-E_m)t} - e^{i(E_m-E_j)t})
#           = sum_m [A_{im} e^{i(E_i-E_m)t}] A_{mj} - A_{im} [A_{mj} e^{i(E_m-E_j)t}]
#
# More efficiently:
# A(t)_{ij} = A_{ij} * e^{i(E_i - E_j)t}
# C(t) = A(t) A - A A(t) as matrices

# F(t) = -Tr(rho * C(t)^2) / Z where rho = e^{-beta*H}

# Store results
F_otoc = np.zeros((len(beta_values), n_times))
F_otoc_normalized = np.zeros((len(beta_values), n_times))

# Also compute the "regularized" OTOC:
# F_reg(t) = Tr(rho^{1/4} A(t) rho^{1/4} A(0) rho^{1/4} A(t) rho^{1/4} A(0))
# This is the version that appears in the MSS bound proof.
# But for small systems, the unregularized version suffices.

print("\nComputing OTOC for each temperature...")
t0_total = time.time()

for b_idx, beta in enumerate(beta_values):
    t0 = time.time()

    # Thermal density matrix in eigenbasis
    boltzmann = np.exp(-beta * (evals - evals[0]))  # shift to avoid overflow
    Z = np.sum(boltzmann)
    rho_diag = boltzmann / Z  # diagonal in eigenbasis

    # Effective temperature
    T_eff = 1.0 / beta
    E_thermal = np.sum(rho_diag * evals)

    # Normalization: F(0) should be Tr(rho [A, A]^2) / Z = 0 (at t=0, [A,A]=0)
    # The natural normalization is <A^2>_beta^2
    A2_thermal = np.sum(rho_diag[:, None] * np.abs(A_eig)**2)

    for t_idx, t in enumerate(t_array):
        # A(t) in eigenbasis: A(t)_{ij} = A_{ij} * exp(i*(E_i - E_j)*t)
        phase = np.exp(1j * E_diff * t)
        At_eig = A_eig * phase

        # Commutator C(t) = [A(t), A(0)] = A(t)A - AA(t)
        C = At_eig @ A_eig - A_eig @ At_eig

        # C^2
        C2 = C @ C

        # F(t) = -Tr(rho * C^2)
        # In eigenbasis: Tr(rho * C^2) = sum_i rho_i * C^2_{ii}
        F_val = -np.sum(rho_diag * np.real(np.diag(C2)))
        F_otoc[b_idx, t_idx] = F_val

        # Normalized version
        if A2_thermal > 1e-15:
            F_otoc_normalized[b_idx, t_idx] = F_val / A2_thermal**2

    t1 = time.time()
    print(f"  beta={beta:6.2f} (T={T_eff:.3f}): F(0)={F_otoc[b_idx,0]:.2e}, "
          f"F_max={np.max(F_otoc[b_idx,:]):.4f}, "
          f"F_max/A2^2={np.max(F_otoc_normalized[b_idx,:]):.4f}, "
          f"time={t1-t0:.2f}s")

t1_total = time.time()
print(f"\nTotal OTOC computation time: {t1_total - t0_total:.1f}s")

# ============================================================
# 6. EXTRACT LYAPUNOV EXPONENT
# ============================================================

print("\n" + "=" * 70)
print("LYAPUNOV EXPONENT EXTRACTION")
print("=" * 70)

# For each temperature, attempt to find an exponential growth regime.
# F(t) ~ F_0 * exp(lambda_L * t) in the early-time regime.
# We look for a window where log(F(t)) is approximately linear.

lambda_L_results = {}
scrambling_times = {}

for b_idx, beta in enumerate(beta_values):
    T = 1.0 / beta
    mss_bound = 2 * np.pi * T  # MSS bound: lambda_L <= 2*pi*T

    F = F_otoc[b_idx, :]

    # Find the time window where F is growing
    # Skip t=0 (F=0 exactly)
    F_positive = F.copy()
    F_positive[F_positive <= 0] = np.nan

    # Look for growth regime: F > 1e-10 and F < 0.5 * F_max (before saturation)
    F_max = np.nanmax(F_positive)
    if np.isnan(F_max) or F_max < 1e-15:
        lambda_L_results[beta] = (0.0, 0.0, mss_bound, "NO_GROWTH")
        print(f"  beta={beta:.2f}: No positive OTOC growth detected")
        continue

    # Growth window: F > 1e-4 * F_max and F < 0.3 * F_max
    growth_mask = (~np.isnan(F_positive)) & (F_positive > 1e-4 * F_max) & (F_positive < 0.3 * F_max)
    growth_indices = np.where(growth_mask)[0]

    if len(growth_indices) < 10:
        # Try a wider window
        growth_mask = (~np.isnan(F_positive)) & (F_positive > 1e-6 * F_max) & (F_positive < 0.5 * F_max)
        growth_indices = np.where(growth_mask)[0]

    if len(growth_indices) < 5:
        # Check if there's ANY growth
        # Look at early-time behavior: fit first 20% of positive data
        pos_idx = np.where((~np.isnan(F_positive)) & (F_positive > 1e-15))[0]
        if len(pos_idx) < 5:
            lambda_L_results[beta] = (0.0, 0.0, mss_bound, "NO_EXP_REGIME")
            print(f"  beta={beta:.2f}: Insufficient data for exponential fit")
            continue
        # Use first 20% of positive data
        n_use = max(5, len(pos_idx) // 5)
        growth_indices = pos_idx[:n_use]

    # Fit log(F) = log(F_0) + lambda_L * t
    t_fit = t_array[growth_indices]
    logF_fit = np.log(F_positive[growth_indices])

    # Check for NaN/Inf
    valid = np.isfinite(logF_fit)
    if np.sum(valid) < 3:
        lambda_L_results[beta] = (0.0, 0.0, mss_bound, "FIT_FAILED")
        print(f"  beta={beta:.2f}: Fit failed (insufficient valid points)")
        continue

    t_fit = t_fit[valid]
    logF_fit = logF_fit[valid]

    # Linear fit
    coeffs = np.polyfit(t_fit, logF_fit, 1)
    lambda_L = coeffs[0]

    # Compute R^2 to assess quality of exponential fit
    logF_pred = np.polyval(coeffs, t_fit)
    SS_res = np.sum((logF_fit - logF_pred)**2)
    SS_tot = np.sum((logF_fit - np.mean(logF_fit))**2)
    R2 = 1 - SS_res / (SS_tot + 1e-30)

    # Scrambling time: when F(t) reaches F_max/e or a significant fraction
    # Convention: t_scr = time when F(t) first reaches 0.5 * F_saturation
    F_sat = np.mean(F[len(F)//2:])  # late-time average
    if F_sat > 0:
        scr_idx = np.where(F >= 0.5 * F_sat)[0]
        if len(scr_idx) > 0:
            t_scr = t_array[scr_idx[0]]
        else:
            t_scr = np.inf
    else:
        t_scr = np.inf

    scrambling_times[beta] = t_scr

    # Classification
    if lambda_L > 0 and R2 > 0.9:
        if lambda_L > mss_bound:
            status = "KILL"
        else:
            status = f"EXP_GROWTH (R2={R2:.3f})"
    elif lambda_L > 0 and R2 > 0.7:
        status = f"WEAK_EXP (R2={R2:.3f})"
    elif lambda_L > 0:
        status = f"POOR_FIT (R2={R2:.3f})"
    else:
        status = "DECAY"

    lambda_L_results[beta] = (lambda_L, R2, mss_bound, status)

    ratio = lambda_L / mss_bound if mss_bound > 0 else np.inf
    print(f"  beta={beta:6.2f} (T={T:.3f}): lambda_L = {lambda_L:+.4f}, "
          f"R2 = {R2:.4f}, MSS = {mss_bound:.4f}, "
          f"lambda_L/MSS = {ratio:.4f}, t_scr = {t_scr:.2f}, "
          f"status = {status}")

# ============================================================
# 7. ALTERNATIVE GROWTH ANALYSIS
# ============================================================
# The OTOC may not show simple exponential growth in a small system.
# Check for:
# (a) Power-law growth: F(t) ~ t^alpha
# (b) Oscillatory behavior (pair vibration frequency)
# (c) Immediate saturation (no scrambling)

print("\n" + "=" * 70)
print("ALTERNATIVE GROWTH ANALYSIS")
print("=" * 70)

for b_idx, beta in enumerate(beta_values[:4]):  # Focus on first 4 temperatures
    T = 1.0 / beta
    F = F_otoc[b_idx, :]

    # Early-time behavior: F(t) ~ t^2 * ||[H, A]||^2 / 2 (Baker-Campbell-Hausdorff)
    # This is the universal early-time quadratic growth

    # Compute ||[H, A]||
    comm_HA_norm = la.norm(comm_HA, 'fro')

    # Find peak time
    t_peak_idx = np.argmax(F)
    t_peak = t_array[t_peak_idx]
    F_peak = F[t_peak_idx]

    # Late-time average (saturation value)
    F_late = np.mean(F[3*n_times//4:])

    # Check for oscillations: FFT of F(t) after subtracting mean
    F_centered = F[n_times//4:] - np.mean(F[n_times//4:])
    if np.std(F_centered) > 1e-15:
        fft_F = np.abs(np.fft.rfft(F_centered))
        freqs = np.fft.rfftfreq(len(F_centered), d=t_array[1]-t_array[0])
        # Find dominant frequency (skip DC)
        if len(fft_F) > 2:
            peak_freq_idx = np.argmax(fft_F[1:]) + 1
            dominant_freq = freqs[peak_freq_idx]
            dominant_period = 1.0 / dominant_freq if dominant_freq > 0 else np.inf
        else:
            dominant_freq = 0
            dominant_period = np.inf
    else:
        dominant_freq = 0
        dominant_period = np.inf

    # Power-law fit in early time
    early_mask = (t_array > 0.1) & (F > 1e-10 * F_peak) & (t_array < t_peak * 0.5)
    if np.sum(early_mask) > 5:
        t_early = t_array[early_mask]
        F_early = F[early_mask]
        # log(F) = alpha * log(t) + const
        log_t = np.log(t_early)
        log_F = np.log(np.maximum(F_early, 1e-30))
        valid_pl = np.isfinite(log_F)
        if np.sum(valid_pl) > 3:
            coeffs_pl = np.polyfit(log_t[valid_pl], log_F[valid_pl], 1)
            alpha_pl = coeffs_pl[0]
        else:
            alpha_pl = np.nan
    else:
        alpha_pl = np.nan

    print(f"  beta={beta:.1f} (T={T:.3f}):")
    print(f"    F_peak = {F_peak:.6f} at t = {t_peak:.2f}")
    print(f"    F_late (saturation) = {F_late:.6f}")
    print(f"    Dominant oscillation freq = {dominant_freq:.4f} (period = {dominant_period:.2f})")
    if dominant_freq > 0:
        print(f"    Ratio to omega_PV: {dominant_freq/omega_PV:.3f}")
    if not np.isnan(alpha_pl):
        print(f"    Power-law exponent alpha = {alpha_pl:.2f}")
    print(f"    ||[H, A]|| = {comm_HA_norm:.6f}")

# ============================================================
# 8. SPECTRAL FORM FACTOR
# ============================================================

print("\n" + "=" * 70)
print("SPECTRAL FORM FACTOR")
print("=" * 70)

# K(t) = |Z(beta + it)|^2 / |Z(beta)|^2
# Z(beta + it) = Tr(exp(-(beta+it)*H)) = sum_n exp(-(beta+it)*E_n)
# K(t) = |sum_n exp(-beta*E_n - i*E_n*t)|^2 / |sum_n exp(-beta*E_n)|^2

t_sff = np.linspace(0, 200, 5000)  # longer time for SFF
beta_sff = 1.0  # fixed temperature for SFF

boltz_sff = np.exp(-beta_sff * (evals - evals[0]))
Z_sff = np.sum(boltz_sff)

K_sff = np.zeros(len(t_sff))
for t_idx, t in enumerate(t_sff):
    Zt = np.sum(boltz_sff * np.exp(-1j * evals * t))
    K_sff[t_idx] = np.abs(Zt)**2 / Z_sff**2

# Identify the dip time and ramp
K_min = np.min(K_sff[100:])  # skip initial decay
K_min_idx = np.argmin(K_sff[100:]) + 100
t_dip = t_sff[K_min_idx]
K_plateau = np.mean(K_sff[-500:])

print(f"  beta = {beta_sff}")
print(f"  K(0) = {K_sff[0]:.6f}")
print(f"  K_min = {K_min:.6e} at t = {t_dip:.2f}")
print(f"  K_plateau = {K_plateau:.6e}")
print(f"  Dip-to-plateau ratio = {K_plateau / K_min:.2f}")
# For GOE/GUE, the ramp-plateau structure is characteristic
# For Poisson, K(t) should decay to plateau without a dip-ramp structure

# Also compute SFF within the largest N_pair sector
largest_sector_np = max(sector_evals.keys(), key=lambda k: len(sector_evals[k]))
ev_sector = sector_evals[largest_sector_np]
boltz_sector = np.exp(-beta_sff * (ev_sector - ev_sector[0]))
Z_sector = np.sum(boltz_sector)

K_sector = np.zeros(len(t_sff))
for t_idx, t in enumerate(t_sff):
    Zt = np.sum(boltz_sector * np.exp(-1j * ev_sector * t))
    K_sector[t_idx] = np.abs(Zt)**2 / Z_sector**2

K_sector_min = np.min(K_sector[100:])
K_sector_plateau = np.mean(K_sector[-500:])
print(f"\n  Largest sector (N_pair={largest_sector_np}, dim={len(ev_sector)}):")
print(f"    K_min = {K_sector_min:.6e}")
print(f"    K_plateau = {K_sector_plateau:.6e}")
print(f"    Dip-to-plateau = {K_sector_plateau / K_sector_min:.2f}")

# ============================================================
# 9. CHAOS-2 GATE VERDICT
# ============================================================

print("\n" + "=" * 70)
print("GATE VERDICTS")
print("=" * 70)

# Analyze results for gate classification
has_exponential = False
max_lambda_L = 0.0
best_R2 = 0.0
mss_violated = False

for beta, (lam, R2, mss, status) in sorted(lambda_L_results.items()):
    if "EXP_GROWTH" in status and lam > 0:
        has_exponential = True
        if lam > max_lambda_L:
            max_lambda_L = lam
            best_R2 = R2
    if "KILL" in status:
        mss_violated = True

print(f"\nCHAOS-2: OTOC of Gap Operator in BCS Fock Space")
print(f"  Max lambda_L = {max_lambda_L:.6f}")
print(f"  Best R^2 = {best_R2:.4f}")
print(f"  Has exponential regime? {has_exponential}")
print(f"  MSS bound violated? {mss_violated}")

if mss_violated:
    chaos2_verdict = "KILL"
    print(f"\n  *** CHAOS-2 VERDICT: KILL ***")
    print(f"  Lyapunov exponent exceeds MSS bound. Framework inconsistency.")
elif has_exponential:
    chaos2_verdict = "PASS"
    print(f"\n  *** CHAOS-2 VERDICT: PASS ***")
    print(f"  Genuine exponential OTOC growth detected.")
    print(f"  The many-body BCS dynamics are quantum chaotic.")
else:
    chaos2_verdict = "FAIL"
    print(f"\n  *** CHAOS-2 VERDICT: FAIL ***")
    print(f"  No exponential OTOC growth regime found.")
    print(f"  The many-body BCS dynamics are NOT quantum chaotic.")

# Additional assessment based on what we DO see
print(f"\n  Many-body level statistics:")
for n_p in sorted(r_by_sector.keys()):
    r_mean, r_err, n_rat = r_by_sector[n_p]
    if not np.isnan(r_mean) and n_rat >= 5:
        print(f"    N_pair={n_p}: <r> = {r_mean:.4f} +/- {r_err:.4f} (N={n_rat})")

# ============================================================
# 10. CHAOS-3: SCRAMBLING TIME VS TRANSIT TIME
# ============================================================

print(f"\nCHAOS-3: Scrambling Time vs Transit Time")

# Transit time through BCS window
t_transit = t_transit_full  # in natural units
print(f"  t_transit (full gradient) = {t_transit:.6e}")

# Scrambling time from OTOC
# Use the fastest scrambling temperature (lowest beta with defined t_scr)
t_scr_best = np.inf
beta_best_scr = None
for beta in sorted(scrambling_times.keys()):
    t_s = scrambling_times[beta]
    if t_s < t_scr_best:
        t_scr_best = t_s
        beta_best_scr = beta

if t_scr_best < np.inf:
    ratio_scr_transit = t_scr_best / t_transit
    print(f"  t_scr (fastest) = {t_scr_best:.4f} at beta = {beta_best_scr}")
    print(f"  t_scr / t_transit = {ratio_scr_transit:.1f}")

    if ratio_scr_transit < 1.0:
        chaos3_verdict = "PASS"
        print(f"  *** CHAOS-3 VERDICT: PASS ***")
        print(f"  Scrambling occurs faster than transit. Scrambling during transit viable.")
    else:
        chaos3_verdict = "FAIL"
        print(f"  *** CHAOS-3 VERDICT: FAIL ***")
        print(f"  Scrambling time {ratio_scr_transit:.0f}x longer than transit time.")
else:
    # Even without exponential growth, the OTOC rises to saturation
    # The "saturation time" is a proxy for scrambling
    t_sat_best = np.inf
    for b_idx, beta in enumerate(beta_values):
        F = F_otoc[b_idx, :]
        F_max_val = np.max(F)
        if F_max_val > 1e-15:
            # Time to reach 90% of max
            sat_idx = np.where(F >= 0.9 * F_max_val)[0]
            if len(sat_idx) > 0:
                t_sat = t_array[sat_idx[0]]
                if t_sat < t_sat_best:
                    t_sat_best = t_sat

    if t_sat_best < np.inf:
        ratio_sat_transit = t_sat_best / t_transit
        print(f"  t_sat (90% of max) = {t_sat_best:.4f}")
        print(f"  t_sat / t_transit = {ratio_sat_transit:.1f}")
        chaos3_verdict = "FAIL"
        print(f"  *** CHAOS-3 VERDICT: FAIL ***")
        print(f"  Saturation time {ratio_sat_transit:.0f}x longer than transit time.")
    else:
        chaos3_verdict = "FAIL"
        print(f"  *** CHAOS-3 VERDICT: FAIL ***")
        print(f"  No scrambling or saturation detected.")

# ============================================================
# 11. SECOND OPERATOR CHOICE: B = i(Delta^dag - Delta)/sqrt(2)
# ============================================================
# The OTOC can depend on operator choice. Let's also try:
# (a) Individual mode pair operator: A_k = (P_k + P_k^dag)/sqrt(2)
# (b) Pair number operator (diagonal, conserved)

print("\n" + "=" * 70)
print("CROSS-CHECK: SINGLE-MODE OTOC")
print("=" * 70)

# Build single-mode pair operator for B2[0]
Delta_0 = np.zeros((dim, dim))
for alpha in range(dim):
    if alpha & 1:  # mode 0 occupied
        beta_state = alpha ^ 1
        Delta_0[beta_state, alpha] = np.sqrt(rho_8[0])

A_0 = (Delta_0 + Delta_0.T) / np.sqrt(2)
A_0_eig = evecs.T @ A_0 @ evecs

# Compute OTOC for single mode at beta=1.0
beta_check = 1.0
boltz_check = np.exp(-beta_check * (evals - evals[0]))
Z_check = np.sum(boltz_check)
rho_check = boltz_check / Z_check

F_single = np.zeros(n_times)
for t_idx, t in enumerate(t_array):
    phase = np.exp(1j * E_diff * t)
    At_eig = A_0_eig * phase
    C = At_eig @ A_0_eig - A_0_eig @ At_eig
    C2 = C @ C
    F_single[t_idx] = -np.sum(rho_check * np.real(np.diag(C2)))

print(f"  Single-mode B2[0] at beta=1.0:")
print(f"    F_max = {np.max(F_single):.6f}")
print(f"    F_late = {np.mean(F_single[-500:]):.6f}")

# ============================================================
# 12. SAVE DATA
# ============================================================

print("\n" + "=" * 70)
print("SAVING DATA")
print("=" * 70)

# Prepare lambda_L arrays for saving
beta_arr = np.array(sorted(lambda_L_results.keys()))
lambda_arr = np.array([lambda_L_results[b][0] for b in beta_arr])
R2_arr = np.array([lambda_L_results[b][1] for b in beta_arr])
mss_arr = np.array([lambda_L_results[b][2] for b in beta_arr])

save_dict = {
    # Parameters
    'E_8': E_8,
    'V_phys': V_phys,
    'rho_8': rho_8,
    'mu': np.array(mu),
    'n_modes': np.array(N),
    'dim': np.array(dim),

    # BCS spectrum
    'evals_BCS': evals,
    'n_pairs_gs': np.array(n_pairs_expectation),

    # OTOC
    't_array': t_array,
    'beta_values': beta_values,
    'F_otoc': F_otoc,
    'F_otoc_normalized': F_otoc_normalized,

    # Lyapunov
    'beta_lambda': beta_arr,
    'lambda_L': lambda_arr,
    'R2_fit': R2_arr,
    'mss_bound': mss_arr,

    # Level statistics
    'r_full_spectrum': np.array(r_full),

    # Spectral form factor
    't_sff': t_sff,
    'K_sff': K_sff,
    'K_sector': K_sector,
    'beta_sff': np.array(beta_sff),

    # Single-mode cross-check
    'F_single_mode': F_single,

    # Gate verdicts
    'chaos2_verdict': np.array([chaos2_verdict]),
    'chaos3_verdict': np.array([chaos3_verdict]),

    # Transit time
    't_transit': np.array(t_transit),
}

# Add sector-resolved level statistics
for n_p, (r_mean, r_err, n_rat) in r_by_sector.items():
    save_dict[f'r_sector_{n_p}'] = np.array([r_mean, r_err, float(n_rat)])

np.savez('tier0-computation/s38_otoc_bcs.npz', **save_dict)
print("  Saved: tier0-computation/s38_otoc_bcs.npz")

# ============================================================
# 13. PLOT
# ============================================================

print("\nGenerating plots...")

fig = plt.figure(figsize=(20, 16))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: F(t) vs t at multiple temperatures
ax1 = fig.add_subplot(gs[0, 0])
for b_idx, beta in enumerate(beta_values):
    if b_idx < 6:
        T = 1.0/beta
        ax1.plot(t_array, F_otoc[b_idx, :], label=f'T={T:.2f}', alpha=0.8)
ax1.set_xlabel('t (natural units)')
ax1.set_ylabel('F(t) = -<[A(t),A(0)]^2>')
ax1.set_title('OTOC: Gap Operator')
ax1.legend(fontsize=7, loc='upper right')
ax1.set_xlim(0, t_max)

# Panel 2: log F(t) vs t (looking for exponential)
ax2 = fig.add_subplot(gs[0, 1])
for b_idx, beta in enumerate(beta_values):
    if b_idx < 6:
        T = 1.0/beta
        F_pos = F_otoc[b_idx, :].copy()
        F_pos[F_pos <= 0] = np.nan
        with np.errstate(invalid='ignore'):
            ax2.plot(t_array, np.log10(F_pos), label=f'T={T:.2f}', alpha=0.8)
ax2.set_xlabel('t (natural units)')
ax2.set_ylabel('log10 F(t)')
ax2.set_title('Log OTOC (exponential = straight line)')
ax2.legend(fontsize=7, loc='lower right')
ax2.set_xlim(0, t_max)

# Panel 3: lambda_L vs T with MSS bound
ax3 = fig.add_subplot(gs[0, 2])
T_arr = 1.0 / beta_arr
ax3.plot(T_arr, lambda_arr, 'bo-', label=r'$\lambda_L$ (fitted)', markersize=6)
T_fine = np.linspace(0, np.max(T_arr)*1.2, 100)
ax3.plot(T_fine, 2*np.pi*T_fine, 'r--', label=r'MSS: $2\pi T$', alpha=0.7)
ax3.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax3.set_xlabel('T')
ax3.set_ylabel(r'$\lambda_L$')
ax3.set_title(r'Lyapunov exponent vs MSS bound')
ax3.legend(fontsize=8)
ax3.set_xlim(0, np.max(T_arr)*1.2)

# Panel 4: Spectral form factor (full)
ax4 = fig.add_subplot(gs[1, 0])
ax4.semilogy(t_sff, K_sff, 'b-', alpha=0.5, linewidth=0.5)
# Running average
window = 50
K_smooth = np.convolve(K_sff, np.ones(window)/window, mode='valid')
t_smooth = t_sff[window//2:window//2+len(K_smooth)]
ax4.semilogy(t_smooth, K_smooth, 'r-', linewidth=1.5, label='Smoothed')
ax4.set_xlabel('t')
ax4.set_ylabel('K(t)')
ax4.set_title(f'Spectral Form Factor (full, beta={beta_sff})')
ax4.legend(fontsize=8)

# Panel 5: Spectral form factor (largest sector)
ax5 = fig.add_subplot(gs[1, 1])
ax5.semilogy(t_sff, K_sector, 'b-', alpha=0.5, linewidth=0.5)
K_sector_smooth = np.convolve(K_sector, np.ones(window)/window, mode='valid')
t_sector_smooth = t_sff[window//2:window//2+len(K_sector_smooth)]
ax5.semilogy(t_sector_smooth, K_sector_smooth, 'r-', linewidth=1.5, label='Smoothed')
ax5.set_xlabel('t')
ax5.set_ylabel('K(t)')
ax5.set_title(f'SFF: N_pair={largest_sector_np} sector (dim={len(ev_sector)})')
ax5.legend(fontsize=8)

# Panel 6: Level spacing histogram for largest sector
ax6 = fig.add_subplot(gs[1, 2])
ev_largest = sector_evals[largest_sector_np]
spacings_largest = np.diff(np.sort(ev_largest))
spacings_largest = spacings_largest[spacings_largest > 1e-12 * np.mean(np.abs(spacings_largest) + 1e-30)]
if len(spacings_largest) > 0:
    s_norm = spacings_largest / np.mean(spacings_largest)
    ax6.hist(s_norm, bins=20, density=True, alpha=0.7, color='steelblue', label=f'N_pair={largest_sector_np}')
    s_plot = np.linspace(0, 4, 200)
    ax6.plot(s_plot, np.exp(-s_plot), 'g--', linewidth=2, label='Poisson')
    ax6.plot(s_plot, np.pi*s_plot/2 * np.exp(-np.pi*s_plot**2/4), 'r--', linewidth=2, label='GOE')
    ax6.set_xlabel('s / <s>')
    ax6.set_ylabel('P(s)')
    ax6.set_title(f'Many-body level spacing (N_pair={largest_sector_np})')
    ax6.legend(fontsize=8)
    ax6.set_xlim(0, 4)

# Panel 7: OTOC normalized by A2^2
ax7 = fig.add_subplot(gs[2, 0])
for b_idx, beta in enumerate(beta_values):
    if b_idx < 6:
        T = 1.0/beta
        ax7.plot(t_array, F_otoc_normalized[b_idx, :], label=f'T={T:.2f}', alpha=0.8)
ax7.set_xlabel('t (natural units)')
ax7.set_ylabel(r'$F(t) / \langle A^2 \rangle^2$')
ax7.set_title('Normalized OTOC')
ax7.legend(fontsize=7, loc='upper right')

# Panel 8: Many-body r-ratio by sector
ax8 = fig.add_subplot(gs[2, 1])
sectors_plot = []
r_plot = []
r_err_plot = []
for n_p in sorted(r_by_sector.keys()):
    r_m, r_e, n_r = r_by_sector[n_p]
    if not np.isnan(r_m) and n_r >= 3:
        sectors_plot.append(n_p)
        r_plot.append(r_m)
        r_err_plot.append(r_e)

ax8.errorbar(sectors_plot, r_plot, yerr=r_err_plot, fmt='bo-', markersize=8, capsize=4)
ax8.axhline(y=0.386, color='g', linestyle='--', label='Poisson (0.386)')
ax8.axhline(y=0.5307, color='r', linestyle='--', label='GOE (0.531)')
ax8.set_xlabel('N_pair sector')
ax8.set_ylabel('<r>')
ax8.set_title('Many-body level spacing: r-ratio')
ax8.legend(fontsize=8)
ax8.set_ylim(0, 0.7)

# Panel 9: BCS energy spectrum by sector
ax9 = fig.add_subplot(gs[2, 2])
colors_sector = plt.cm.viridis(np.linspace(0, 1, len(sector_evals)))
for idx, n_p in enumerate(sorted(sector_evals.keys())):
    ev = sector_evals[n_p]
    ax9.plot(np.full_like(ev, n_p), ev, '.', color=colors_sector[idx],
             markersize=3, alpha=0.6)
ax9.set_xlabel('N_pair')
ax9.set_ylabel('Energy')
ax9.set_title('BCS Many-body Spectrum by Sector')

# Add overall title
fig.suptitle(f'CHAOS-2: OTOC Analysis of BCS Gap Operator (8 modes, dim={dim})\n'
             f'Verdict: {chaos2_verdict} | Many-body <r>_pooled = {np.mean(pooled_ratios):.3f}',
             fontsize=14, fontweight='bold')

plt.savefig('tier0-computation/s38_otoc_bcs.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s38_otoc_bcs.png")

# ============================================================
# 14. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("FINAL SUMMARY")
print("=" * 70)

print(f"\n  H_BCS: {dim}x{dim} ({N} modes, pair Fock space)")
print(f"  Ground state energy: {evals[0]:.6f}")
print(f"  <N_pair> in GS: {n_pairs_expectation:.3f}")
print(f"  Spectrum width: {evals[-1] - evals[0]:.4f}")

print(f"\n  OTOC Analysis:")
print(f"    Gate CHAOS-2: {chaos2_verdict}")
for beta in sorted(lambda_L_results.keys()):
    lam, R2, mss, status = lambda_L_results[beta]
    print(f"    beta={beta:.1f}: lambda_L={lam:+.4f}, R2={R2:.4f}, status={status}")

print(f"\n  Many-body Level Statistics:")
print(f"    Full spectrum <r> = {r_full:.4f}")
if pooled_ratios is not None and len(pooled_ratios) > 0:
    print(f"    Within-sector pooled <r> = {np.mean(pooled_ratios):.4f} +/- {np.std(pooled_ratios)/np.sqrt(len(pooled_ratios)):.4f}")

print(f"\n  Spectral Form Factor (beta={beta_sff}):")
print(f"    K_min = {K_min:.6e}")
print(f"    K_plateau = {K_plateau:.6e}")
print(f"    Dip-to-plateau = {K_plateau/K_min:.2f}")

print(f"\n  Gate CHAOS-3: {chaos3_verdict}")
print(f"    t_transit = {t_transit:.6e}")

print(f"\n  Classification: The BCS many-body dynamics in the 0D limit are ")
if chaos2_verdict == "PASS":
    print(f"  QUANTUM CHAOTIC with lambda_L = {max_lambda_L:.4f}")
elif chaos2_verdict == "FAIL":
    print(f"  NOT QUANTUM CHAOTIC. The OTOC saturates without exponential growth.")
    print(f"  The 8-mode BCS system is too small / too integrable for scrambling.")
else:
    print(f"  INCONSISTENT (MSS bound violated).")

print("\nDone.")
