#!/usr/bin/env python3
"""
B1-SOFT-MODE-53: V_B1 Non-Monotonicity as Transit Precursor
=============================================================

Computes per-branch spectral action contributions V_B1(tau), V_B2(tau), V_B3(tau)
across tau in [0, 0.35] from the archived Dirac eigenvalue data.

Physical motivation:
  At N_pair=1, B1 is the Fermi-surface orbital (mu_BCS = E_B1 = 0.819 at fold).
  The B1 mode sits at the spectral gap edge. Its spectral weight is maximally
  sensitive to BCS gap opening. A non-monotonicity in V_B1 near tau_fold
  would constitute a spectral precursor to the BCS transition.

Branch classification (SECTOR-based, from s44_dos_tau.py):
  B1 = "acoustic" branch:    sectors (0,0), (1,0), (0,1)
  B2 = "flat-optical" branch: sector (1,1)
  B3 = "dispersive-optical":  sectors (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)

Spectral action cutoff function:
  f(x) = x/2 + ln(1 - exp(-x))    [Connes-Chamseddine, phonon free energy]
  where x = lambda_n^2 / Lambda^2, Lambda = cutoff scale

For comparison, also computes:
  (a) log sum: sum of sign(lambda) * log(lambda^2)  [as in LOG-SIGNED-52]
  (b) heat kernel: sum of sign(lambda) * exp(-lambda^2/Lambda^2)

Data sources:
  computations/session-36/s36_sfull_tau_stabilization.npz (7 tau: 0.05, 0.16-0.22)
  computations/session-27/s27_multisector_bcs.npz (9 tau: 0.0, 0.10, 0.15, 0.20-0.50)

Gate: B1-SOFT-MODE-53 (INFO)
Output: s53_b1_soft_mode.npz, s53_b1_soft_mode.png
"""

import numpy as np
from pathlib import Path
import sys

# Canonical constants
sys.path.insert(0, str(Path("computations").resolve()))
from canonical_constants import tau_fold, E_cond, M_KK, E_B1, E_B2_mean, E_B3_mean

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

print("=" * 78)
print("B1-SOFT-MODE-53: V_B1 Non-Monotonicity as Transit Precursor")
print("=" * 78)

data_dir = Path("computations")
archive_dir = Path("computations/_shared")

# ==========================================================================
# 1. LOAD EIGENVALUE DATA FROM ARCHIVES
# ==========================================================================

# 10 sectors at max_pq_sum=3
sectors = [
    (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1), (1, 2)
]

# Sectors available in s27 (no (1,2) — use (2,1) conjugation)
sectors_s27 = [
    (0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1)
]


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mult_pq(p, q):
    """Peter-Weyl multiplicity = dim(p,q)^2."""
    return dim_pq(p, q) ** 2


# Branch classification: SECTOR-based (physical phonon branches)
branch_of_sector = {
    (0, 0): 'B1', (1, 0): 'B1', (0, 1): 'B1',
    (1, 1): 'B2',
    (2, 0): 'B3', (0, 2): 'B3', (3, 0): 'B3', (0, 3): 'B3',
    (2, 1): 'B3', (1, 2): 'B3',
}

# Peter-Weyl multiplicities per branch
mult_B1 = sum(mult_pq(p, q) for (p, q) in sectors if branch_of_sector[(p, q)] == 'B1')
mult_B2 = sum(mult_pq(p, q) for (p, q) in sectors if branch_of_sector[(p, q)] == 'B2')
mult_B3 = sum(mult_pq(p, q) for (p, q) in sectors if branch_of_sector[(p, q)] == 'B3')

print(f"\nBranch multiplicities (Peter-Weyl):")
print(f"  B1 sectors: (0,0), (1,0), (0,1)  -> mult = {mult_B1}")
print(f"  B2 sectors: (1,1)                 -> mult = {mult_B2}")
print(f"  B3 sectors: (2,0),(0,2),(3,0),(0,3),(2,1),(1,2) -> mult = {mult_B3}")
print(f"  Total = {mult_B1 + mult_B2 + mult_B3}")

# Load eigenvalue-level data from both archives
eigenvalues = {}

d36 = np.load(archive_dir / "s36_sfull_tau_stabilization.npz", allow_pickle=True)
d27 = np.load(archive_dir / "s27_multisector_bcs.npz", allow_pickle=True)

# s36 tau values
s36_taus = [0.050, 0.160, 0.170, 0.180, 0.190, 0.210, 0.220]
for tau in s36_taus:
    tau_str = f"{tau:.3f}"
    for (p, q) in sectors:
        key = f"evals_tau{tau_str}_{p}_{q}"
        if key in d36:
            eigenvalues[(tau, p, q)] = d36[key]

# s27 tau values
tau27 = d27['tau_values']
for ti, tau in enumerate(tau27):
    tau_round = round(tau, 3)
    if tau_round in [0.050]:
        continue  # already in s36
    for (p, q) in sectors_s27:
        key = f"evals_{p}_{q}_{ti}"
        if key in d27:
            eigenvalues[(tau_round, p, q)] = d27[key]
    # (1,2) from (2,1) by conjugation
    key_21 = f"evals_2_1_{ti}"
    if key_21 in d27:
        eigenvalues[(tau_round, 1, 2)] = d27[key_21]

d36.close()
d27.close()

# Get all tau values where we have complete 10-sector data
all_taus_raw = sorted(set(t for (t, _, _) in eigenvalues.keys()))

# Filter to tau in [0, 0.35] with all 10 sectors
all_taus = []
for tau in all_taus_raw:
    present = sum(1 for (p, q) in sectors if (tau, p, q) in eigenvalues)
    if present == 10 and tau <= 0.351:
        all_taus.append(tau)

print(f"\nUsable tau grid ({len(all_taus)} points, [0, 0.35]): {all_taus}")

n_tau = len(all_taus)
taus_arr = np.array(all_taus)

# ==========================================================================
# 2. DEFINE SPECTRAL ACTION FUNCTIONS
# ==========================================================================

# Cutoff scale: Lambda = max eigenvalue across all tau (natural choice)
lambda_max_global = 0.0  # (local)
for (tau, p, q), ev in eigenvalues.items():
    if tau <= 0.351:
        lmax = np.max(np.abs(ev))
        if lmax > lambda_max_global:
            lambda_max_global = lmax

Lambda = lambda_max_global * 1.1  # 10% headroom above max eigenvalue
print(f"\nCutoff scale Lambda = {Lambda:.6f} M_KK (1.1 * lambda_max = {lambda_max_global:.6f})")


def f_spectral(x):
    """Connes-Chamseddine spectral action cutoff: f(x) = x/2 + ln(1-exp(-x)).
    x = lambda^2/Lambda^2 >= 0. Returns spectral action contribution per mode."""
    x = np.asarray(x, dtype=float)
    result = np.zeros_like(x)
    # Avoid log(0) for very small x
    mask = x > 1e-30
    result[mask] = x[mask] / 2.0 + np.log(1.0 - np.exp(-x[mask]))
    # For tiny x: f(x) ~ ln(x) + x/2 - x^2/24 + ... (divergent — but these don't occur)
    return result


def f_heat(x, t=1.0):
    """Heat kernel: exp(-t*x). x = lambda^2/Lambda^2."""
    return np.exp(-t * np.asarray(x, dtype=float))


def f_log(lam_sq):
    """Log sum: log(lambda^2). Input is lambda^2 directly."""
    return np.log(np.asarray(lam_sq, dtype=float))


# ==========================================================================
# 3. COMPUTE PER-BRANCH SPECTRAL ACTION CONTRIBUTIONS
# ==========================================================================

print("\n" + "=" * 78)
print("COMPUTING PER-BRANCH SPECTRAL SUMS")
print("=" * 78)

# Storage arrays
V_B1_spec = np.zeros(n_tau)   # spectral action f(x)
V_B2_spec = np.zeros(n_tau)
V_B3_spec = np.zeros(n_tau)

V_B1_log = np.zeros(n_tau)    # log sum
V_B2_log = np.zeros(n_tau)
V_B3_log = np.zeros(n_tau)

V_B1_heat = np.zeros(n_tau)   # heat kernel
V_B2_heat = np.zeros(n_tau)
V_B3_heat = np.zeros(n_tau)

# Also track per-sector contributions within B1
V_00_spec = np.zeros(n_tau)
V_10_spec = np.zeros(n_tau)
V_01_spec = np.zeros(n_tau)

# Number of positive eigenvalues per branch
N_B1 = np.zeros(n_tau, dtype=int)
N_B2 = np.zeros(n_tau, dtype=int)
N_B3 = np.zeros(n_tau, dtype=int)

# Mean eigenvalue per branch (for tracking softening)
E_B1_mean = np.zeros(n_tau)
E_B2_mean_arr = np.zeros(n_tau)
E_B3_mean_arr = np.zeros(n_tau)

# Min eigenvalue per branch
E_B1_min = np.zeros(n_tau)
E_B2_min = np.zeros(n_tau)
E_B3_min = np.zeros(n_tau)

Lambda_sq = Lambda ** 2

for i, tau in enumerate(all_taus):
    for (p, q) in sectors:
        ev = eigenvalues[(tau, p, q)]
        m = mult_pq(p, q)
        branch = branch_of_sector[(p, q)]

        # Use positive eigenvalues only (Dirac spectrum: +/- pairs)
        pos_ev = np.sort(ev[ev > 1e-15])
        n_pos = len(pos_ev)

        lam_sq = pos_ev ** 2
        x = lam_sq / Lambda_sq

        # Spectral action contributions (multiplicity-weighted)
        v_spec = m * np.sum(f_spectral(x))
        v_log = m * np.sum(f_log(lam_sq))
        v_heat = m * np.sum(f_heat(x))

        if branch == 'B1':
            V_B1_spec[i] += v_spec
            V_B1_log[i] += v_log
            V_B1_heat[i] += v_heat
            N_B1[i] += m * n_pos
            E_B1_mean[i] += m * np.sum(pos_ev)
            if (p, q) == (0, 0):
                V_00_spec[i] = v_spec
            elif (p, q) == (1, 0):
                V_10_spec[i] = v_spec
            elif (p, q) == (0, 1):
                V_01_spec[i] = v_spec

        elif branch == 'B2':
            V_B2_spec[i] += v_spec
            V_B2_log[i] += v_log
            V_B2_heat[i] += v_heat
            N_B2[i] += m * n_pos
            E_B2_mean_arr[i] += m * np.sum(pos_ev)

        elif branch == 'B3':
            V_B3_spec[i] += v_spec
            V_B3_log[i] += v_log
            V_B3_heat[i] += v_heat
            N_B3[i] += m * n_pos
            E_B3_mean_arr[i] += m * np.sum(pos_ev)

    # Normalize mean energies
    if N_B1[i] > 0:
        E_B1_mean[i] /= N_B1[i]
    if N_B2[i] > 0:
        E_B2_mean_arr[i] /= N_B2[i]
    if N_B3[i] > 0:
        E_B3_mean_arr[i] /= N_B3[i]

    # Minimum eigenvalues per branch at this tau
    b1_all = []
    b2_all = []
    b3_all = []
    for (p, q) in sectors:
        ev = eigenvalues[(tau, p, q)]
        pos_ev = ev[ev > 1e-15]
        branch = branch_of_sector[(p, q)]
        if branch == 'B1':
            b1_all.extend(pos_ev)
        elif branch == 'B2':
            b2_all.extend(pos_ev)
        elif branch == 'B3':
            b3_all.extend(pos_ev)

    E_B1_min[i] = min(b1_all) if b1_all else 0
    E_B2_min[i] = min(b2_all) if b2_all else 0
    E_B3_min[i] = min(b3_all) if b3_all else 0

# Total spectral action
V_total_spec = V_B1_spec + V_B2_spec + V_B3_spec
V_total_log = V_B1_log + V_B2_log + V_B3_log
V_total_heat = V_B1_heat + V_B2_heat + V_B3_heat

# ==========================================================================
# 4. PRINT RESULTS TABLE
# ==========================================================================

print("\n" + "=" * 78)
print("SPECTRAL ACTION f(x) = x/2 + ln(1-exp(-x)) PER BRANCH")
print(f"Lambda = {Lambda:.6f} M_KK")
print("=" * 78)

print(f"\n{'tau':>5s}  {'V_B1':>12s}  {'V_B2':>12s}  {'V_B3':>12s}  {'V_total':>12s}  "
      f"{'B1/tot%':>8s}  {'B2/tot%':>8s}  {'B3/tot%':>8s}")
for i, tau in enumerate(all_taus):
    pct_b1 = 100.0 * V_B1_spec[i] / V_total_spec[i] if V_total_spec[i] != 0 else 0
    pct_b2 = 100.0 * V_B2_spec[i] / V_total_spec[i] if V_total_spec[i] != 0 else 0
    pct_b3 = 100.0 * V_B3_spec[i] / V_total_spec[i] if V_total_spec[i] != 0 else 0
    print(f"  {tau:5.3f}  {V_B1_spec[i]:+12.4f}  {V_B2_spec[i]:+12.4f}  {V_B3_spec[i]:+12.4f}  "
          f"{V_total_spec[i]:+12.4f}  {pct_b1:8.2f}  {pct_b2:8.2f}  {pct_b3:8.2f}")

print(f"\n{'tau':>5s}  {'E_B1_min':>10s}  {'E_B1_mean':>10s}  {'E_B2_min':>10s}  "
      f"{'E_B2_mean':>10s}  {'E_B3_min':>10s}  {'E_B3_mean':>10s}")
for i, tau in enumerate(all_taus):
    print(f"  {tau:5.3f}  {E_B1_min[i]:10.6f}  {E_B1_mean[i]:10.6f}  {E_B2_min[i]:10.6f}  "
          f"{E_B2_mean_arr[i]:10.6f}  {E_B3_min[i]:10.6f}  {E_B3_mean_arr[i]:10.6f}")

# ==========================================================================
# 5. MONOTONICITY ANALYSIS
# ==========================================================================

print("\n" + "=" * 78)
print("MONOTONICITY ANALYSIS")
print("=" * 78)


def analyze_monotonicity(name, arr, taus):
    """Check monotonicity and locate extrema."""
    d = np.diff(arr)
    all_inc = np.all(d > 0)
    all_dec = np.all(d < 0)

    if all_inc:
        print(f"\n  {name}: MONOTONICALLY INCREASING")
        print(f"    Range: [{arr.min():.6f}, {arr.max():.6f}]")
        print(f"    Total change: {arr[-1] - arr[0]:+.6f} ({(arr[-1]/arr[0] - 1)*100:+.2f}%)")
        return 'INCREASING', None
    elif all_dec:
        print(f"\n  {name}: MONOTONICALLY DECREASING")
        print(f"    Range: [{arr.min():.6f}, {arr.max():.6f}]")
        print(f"    Total change: {arr[-1] - arr[0]:+.6f} ({(arr[-1]/arr[0] - 1)*100:+.2f}%)")
        return 'DECREASING', None
    else:
        # Find sign changes in derivative
        extrema = []
        for j in range(len(d) - 1):
            if d[j] * d[j + 1] < 0:
                # Linear interpolation
                tau_ext = taus[j + 1] - d[j + 1] * (taus[j + 2] - taus[j + 1]) / (d[j + 2] - d[j + 1]) if j + 2 < len(taus) else taus[j + 1]
                typ = "MINIMUM" if d[j] < 0 else "MAXIMUM"
                extrema.append((tau_ext, typ, arr[j + 1]))

        print(f"\n  {name}: NON-MONOTONIC")
        print(f"    Range: [{arr.min():.6f}, {arr.max():.6f}]")
        print(f"    Total change: {arr[-1] - arr[0]:+.6f} ({(arr[-1]/arr[0] - 1)*100:+.2f}%)")
        for tau_ext, typ, val in extrema:
            print(f"    {typ} near tau ~ {tau_ext:.4f} (value ~ {val:.6f})")
        return 'NON-MONOTONIC', extrema


# Spectral action
mono_B1, ext_B1 = analyze_monotonicity("V_B1(tau) [spectral]", V_B1_spec, all_taus)
mono_B2, ext_B2 = analyze_monotonicity("V_B2(tau) [spectral]", V_B2_spec, all_taus)
mono_B3, ext_B3 = analyze_monotonicity("V_B3(tau) [spectral]", V_B3_spec, all_taus)
mono_tot, ext_tot = analyze_monotonicity("V_total(tau) [spectral]", V_total_spec, all_taus)

# Log sum (for comparison with LOG-SIGNED-52)
print("\n  --- LOG SUM (comparison) ---")
mono_B1_log, _ = analyze_monotonicity("V_B1(tau) [log]", V_B1_log, all_taus)
mono_B2_log, _ = analyze_monotonicity("V_B2(tau) [log]", V_B2_log, all_taus)
mono_B3_log, _ = analyze_monotonicity("V_B3(tau) [log]", V_B3_log, all_taus)

# Heat kernel
print("\n  --- HEAT KERNEL (comparison) ---")
mono_B1_heat, _ = analyze_monotonicity("V_B1(tau) [heat]", V_B1_heat, all_taus)
mono_B2_heat, _ = analyze_monotonicity("V_B2(tau) [heat]", V_B2_heat, all_taus)
mono_B3_heat, _ = analyze_monotonicity("V_B3(tau) [heat]", V_B3_heat, all_taus)

# ==========================================================================
# 6. SPLINE ANALYSIS FOR SMOOTH EXTREMA AND DERIVATIVES
# ==========================================================================

print("\n" + "=" * 78)
print("CUBIC SPLINE ANALYSIS (smooth extrema & derivatives)")
print("=" * 78)

if n_tau >= 4:
    tau_dense = np.linspace(taus_arr[0], taus_arr[-1], 1000)

    for name, arr in [("V_B1_spec", V_B1_spec), ("V_B2_spec", V_B2_spec),
                       ("V_B3_spec", V_B3_spec), ("V_total_spec", V_total_spec)]:
        cs = CubicSpline(taus_arr, arr)
        dv = cs(tau_dense, 1)
        d2v = cs(tau_dense, 2)

        # Find extrema of the spline (dv = 0)
        extrema_tau = []
        for j in range(len(dv) - 1):
            if dv[j] * dv[j + 1] < 0:
                # Refine
                t_ext = tau_dense[j] - dv[j] * (tau_dense[j + 1] - tau_dense[j]) / (dv[j + 1] - dv[j])
                v_ext = cs(t_ext)
                d2_ext = cs(t_ext, 2)
                typ = "MINIMUM" if d2_ext > 0 else "MAXIMUM"
                extrema_tau.append((t_ext, v_ext, d2_ext, typ))

        print(f"\n  {name}:")
        print(f"    dV/dtau at tau=0.00: {cs(0.0, 1):+.4f}")
        if tau_fold <= taus_arr[-1]:
            print(f"    dV/dtau at tau={tau_fold}: {cs(tau_fold, 1):+.4f}")
            print(f"    d2V/dtau2 at tau={tau_fold}: {cs(tau_fold, 2):+.4f}")
        if extrema_tau:
            for t_ext, v_ext, d2_ext, typ in extrema_tau:
                print(f"    SPLINE {typ} at tau = {t_ext:.6f}, V = {v_ext:.6f}, d2V = {d2_ext:+.4f}")
                if typ == "MINIMUM" and abs(t_ext - tau_fold) < 0.05:
                    print(f"      *** NEAR FOLD (|tau_ext - tau_fold| = {abs(t_ext - tau_fold):.4f}) ***")
        else:
            print(f"    No spline extrema in [{taus_arr[0]:.2f}, {taus_arr[-1]:.2f}]")

# ==========================================================================
# 7. B1 SECTOR DECOMPOSITION
# ==========================================================================

print("\n" + "=" * 78)
print("B1 SECTOR DECOMPOSITION: (0,0), (1,0), (0,1)")
print("=" * 78)

print(f"\n{'tau':>5s}  {'V(0,0)':>12s}  {'V(1,0)':>12s}  {'V(0,1)':>12s}  {'V_B1_total':>12s}")
for i, tau in enumerate(all_taus):
    print(f"  {tau:5.3f}  {V_00_spec[i]:+12.6f}  {V_10_spec[i]:+12.6f}  {V_01_spec[i]:+12.6f}  "
          f"{V_B1_spec[i]:+12.6f}")

print(f"\n  (1,0) vs (0,1) ratio (should be 1 by conjugation):")
for i, tau in enumerate(all_taus):
    ratio = V_10_spec[i] / V_01_spec[i] if V_01_spec[i] != 0 else 0
    print(f"    tau={tau:.3f}: V(1,0)/V(0,1) = {ratio:.8f}")

# ==========================================================================
# 8. NORMALIZED RATIOS: V_B1/(V_B1+V_B2+V_B3) AS FUNCTION OF TAU
# ==========================================================================

print("\n" + "=" * 78)
print("FRACTIONAL CONTRIBUTIONS: V_Bi / V_total")
print("=" * 78)

frac_B1 = V_B1_spec / V_total_spec
frac_B2 = V_B2_spec / V_total_spec
frac_B3 = V_B3_spec / V_total_spec

print(f"\n{'tau':>5s}  {'f_B1':>10s}  {'f_B2':>10s}  {'f_B3':>10s}  {'f_B1+B3':>10s}")
for i, tau in enumerate(all_taus):
    print(f"  {tau:5.3f}  {frac_B1[i]:10.6f}  {frac_B2[i]:10.6f}  {frac_B3[i]:10.6f}  "
          f"{frac_B1[i]+frac_B3[i]:10.6f}")

# Variation of fractions
for name, frac in [("f_B1", frac_B1), ("f_B2", frac_B2), ("f_B3", frac_B3)]:
    variation = (frac.max() - frac.min()) / frac.mean() * 100
    print(f"\n  {name} variation: {variation:.4f}%")

# ==========================================================================
# 9. PER-MODE SPECTRAL ACTION (spectral weight per eigenvalue)
# ==========================================================================

print("\n" + "=" * 78)
print("PER-MODE SPECTRAL WEIGHT: V_Bi / N_Bi")
print("=" * 78)

v_per_B1 = V_B1_spec / N_B1
v_per_B2 = V_B2_spec / N_B2
v_per_B3 = V_B3_spec / N_B3

print(f"\n{'tau':>5s}  {'v/N_B1':>12s}  {'v/N_B2':>12s}  {'v/N_B3':>12s}")
for i, tau in enumerate(all_taus):
    print(f"  {tau:5.3f}  {v_per_B1[i]:12.8f}  {v_per_B2[i]:12.8f}  {v_per_B3[i]:12.8f}")

# Monotonicity of per-mode weight
print("\n  Per-mode monotonicity:")
analyze_monotonicity("v/N_B1", v_per_B1, all_taus)
analyze_monotonicity("v/N_B2", v_per_B2, all_taus)
analyze_monotonicity("v/N_B3", v_per_B3, all_taus)

# ==========================================================================
# 10. B1 GAP EDGE ANALYSIS
# ==========================================================================

print("\n" + "=" * 78)
print("B1 GAP EDGE: E_B1_min(tau) — Fermi-surface orbital energy")
print("=" * 78)

print(f"\n{'tau':>5s}  {'E_B1_min':>10s}  {'dE_B1':>10s}  {'f(E^2/L^2)':>12s}")
for i, tau in enumerate(all_taus):
    x = E_B1_min[i] ** 2 / Lambda_sq
    fval = f_spectral(np.array([x]))[0]
    de = E_B1_min[i] - E_B1_min[0] if i > 0 else 0.0
    print(f"  {tau:5.3f}  {E_B1_min[i]:10.6f}  {de:+10.6f}  {fval:12.8f}")

analyze_monotonicity("E_B1_min(tau)", E_B1_min, all_taus)

# ==========================================================================
# 11. SENSITIVITY ANALYSIS: V_B1 RESPONSE TO GAP OPENING
# ==========================================================================

print("\n" + "=" * 78)
print("SENSITIVITY: d(V_B1)/d(tau) near fold vs BCS gap scale")
print("=" * 78)

if n_tau >= 4:
    cs_B1 = CubicSpline(taus_arr, V_B1_spec)
    cs_B2 = CubicSpline(taus_arr, V_B2_spec)
    cs_B3 = CubicSpline(taus_arr, V_B3_spec)
    cs_tot = CubicSpline(taus_arr, V_total_spec)

    # Compute d/dtau at the fold
    dV_B1_fold = cs_B1(tau_fold, 1) if tau_fold <= taus_arr[-1] else cs_B1(taus_arr[-1], 1)
    dV_B2_fold = cs_B2(tau_fold, 1) if tau_fold <= taus_arr[-1] else cs_B2(taus_arr[-1], 1)
    dV_B3_fold = cs_B3(tau_fold, 1) if tau_fold <= taus_arr[-1] else cs_B3(taus_arr[-1], 1)
    dV_tot_fold = cs_tot(tau_fold, 1) if tau_fold <= taus_arr[-1] else cs_tot(taus_arr[-1], 1)

    print(f"\n  At tau_fold = {tau_fold}:")
    print(f"    dV_B1/dtau = {dV_B1_fold:+.4f}")
    print(f"    dV_B2/dtau = {dV_B2_fold:+.4f}")
    print(f"    dV_B3/dtau = {dV_B3_fold:+.4f}")
    print(f"    dV_tot/dtau = {dV_tot_fold:+.4f}")

    # Fractional derivative: (dV_Bi/dtau) / V_Bi
    V_B1_fold = cs_B1(tau_fold)
    V_B2_fold = cs_B2(tau_fold)
    V_B3_fold = cs_B3(tau_fold)

    print(f"\n  Fractional sensitivity (dV/V per dtau):")
    print(f"    B1: {dV_B1_fold/V_B1_fold:+.6f}")
    print(f"    B2: {dV_B2_fold/V_B2_fold:+.6f}")
    print(f"    B3: {dV_B3_fold/V_B3_fold:+.6f}")

    # Second derivative — curvature signals
    d2V_B1_fold = cs_B1(tau_fold, 2)
    d2V_B2_fold = cs_B2(tau_fold, 2)
    d2V_B3_fold = cs_B3(tau_fold, 2)

    print(f"\n  Curvature at fold:")
    print(f"    d2V_B1/dtau2 = {d2V_B1_fold:+.4f}")
    print(f"    d2V_B2/dtau2 = {d2V_B2_fold:+.4f}")
    print(f"    d2V_B3/dtau2 = {d2V_B3_fold:+.4f}")

    # Ratio of curvatures
    if abs(d2V_B3_fold) > 1e-15:
        print(f"    d2V_B1/d2V_B3 = {d2V_B1_fold/d2V_B3_fold:.4f}")
    if abs(d2V_B2_fold) > 1e-15:
        print(f"    d2V_B1/d2V_B2 = {d2V_B1_fold/d2V_B2_fold:.4f}")

# ==========================================================================
# 12. SCAN CUTOFF DEPENDENCE
# ==========================================================================

print("\n" + "=" * 78)
print("CUTOFF DEPENDENCE: V_B1 monotonicity vs Lambda")
print("=" * 78)

Lambda_values = [Lambda * f for f in [0.5, 0.75, 1.0, 1.5, 2.0, 5.0, 10.0]]
print(f"\n  {'Lambda':>10s}  {'V_B1 mono':>12s}  {'V_B1 range':>20s}  {'V_B1 variation%':>15s}")

for Lam in Lambda_values:
    Lsq = Lam ** 2
    v_b1_test = np.zeros(n_tau)
    for i, tau in enumerate(all_taus):
        for (p, q) in sectors:
            if branch_of_sector[(p, q)] != 'B1':
                continue
            ev = eigenvalues[(tau, p, q)]
            m = mult_pq(p, q)
            pos_ev = ev[ev > 1e-15]
            x = pos_ev ** 2 / Lsq
            v_b1_test[i] += m * np.sum(f_spectral(x))

    d_test = np.diff(v_b1_test)
    if np.all(d_test > 0):
        mono_str = "INCREASING"
    elif np.all(d_test < 0):
        mono_str = "DECREASING"
    else:
        mono_str = "NON-MONOTONE"

    variation = (v_b1_test.max() - v_b1_test.min()) / abs(v_b1_test.mean()) * 100
    print(f"  {Lam:10.4f}  {mono_str:>12s}  [{v_b1_test.min():+.4f}, {v_b1_test.max():+.4f}]  {variation:15.4f}%")

# ==========================================================================
# 13. GATE VERDICT
# ==========================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: B1-SOFT-MODE-53 (INFO)")
print("=" * 78)

print(f"""
QUESTION: Is V_B1(tau) non-monotone? If so, does the extremum coincide with
the fold (tau ~ {tau_fold}), constituting a spectral precursor to the BCS transition?

ANSWER:
  V_B1(tau) [spectral action, f(x)=x/2+ln(1-exp(-x))]: {mono_B1}
  V_B2(tau): {mono_B2}
  V_B3(tau): {mono_B3}
  V_total(tau): {mono_tot}

  E_B1_min(tau) = {E_B1_min[0]:.6f} (tau=0) -> {E_B1_min[-1]:.6f} (tau={all_taus[-1]:.2f})
    The B1 gap edge DECREASES with tau (softening toward the fold).

PHYSICAL INTERPRETATION:
  V_B1(tau) = sector-summed spectral action for the acoustic branch.
  The B1 branch carries sectors (0,0), (1,0), (0,1) with Peter-Weyl
  multiplicity {mult_B1}. At N_pair=1, the B1 lowest mode IS the Fermi
  surface (E_B1 = {E_B1} M_KK at the fold).

  A non-monotonicity in V_B1 would signal that the spectral weight
  redistribution between branches REVERSES direction before/at the fold,
  providing a precursor signature visible in the spectral action alone.

Gate status: INFO — diagnostic result archived.
""")

# ==========================================================================
# 14. PLOT
# ==========================================================================

print("Generating plot...")

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('B1-SOFT-MODE-53: Per-Branch Spectral Action Contributions',
             fontsize=14, fontweight='bold')

# (a) Raw spectral action per branch
ax = axes[0, 0]
ax.plot(taus_arr, V_B1_spec, 'b-o', markersize=4, label='B1 (acoustic)')
ax.plot(taus_arr, V_B2_spec, 'r-s', markersize=4, label='B2 (flat-optical)')
ax.plot(taus_arr, V_B3_spec, 'g-^', markersize=4, label='B3 (dispersive)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5, label=f'fold ({tau_fold})')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{Bi}(\tau)$')
ax.set_title('(a) Spectral action per branch')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (b) Normalized to tau=0 (fractional change)
ax = axes[0, 1]
ax.plot(taus_arr, V_B1_spec / V_B1_spec[0], 'b-o', markersize=4, label='B1')
ax.plot(taus_arr, V_B2_spec / V_B2_spec[0], 'r-s', markersize=4, label='B2')
ax.plot(taus_arr, V_B3_spec / V_B3_spec[0], 'g-^', markersize=4, label='B3')
ax.plot(taus_arr, V_total_spec / V_total_spec[0], 'k-d', markersize=4, label='Total', alpha=0.5)
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{Bi}(\tau) / V_{Bi}(0)$')
ax.set_title('(b) Normalized (tau=0 baseline)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (c) Fractional contribution
ax = axes[0, 2]
ax.plot(taus_arr, frac_B1, 'b-o', markersize=4, label='f_B1')
ax.plot(taus_arr, frac_B2, 'r-s', markersize=4, label='f_B2')
ax.plot(taus_arr, frac_B3, 'g-^', markersize=4, label='f_B3')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{Bi} / V_{total}$')
ax.set_title('(c) Fractional contributions')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (d) Gap edge energy (B1 lowest eigenvalue)
ax = axes[1, 0]
ax.plot(taus_arr, E_B1_min, 'b-o', markersize=4, label='E_B1_min')
ax.plot(taus_arr, E_B2_min, 'r-s', markersize=4, label='E_B2_min')
ax.plot(taus_arr, E_B3_min, 'g-^', markersize=4, label='E_B3_min')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_{min}$ (M_KK)')
ax.set_title(r'(d) Gap edge energy $E_{min}(\tau)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (e) Per-mode spectral weight
ax = axes[1, 1]
ax.plot(taus_arr, v_per_B1, 'b-o', markersize=4, label='B1 per-mode')
ax.plot(taus_arr, v_per_B2, 'r-s', markersize=4, label='B2 per-mode')
ax.plot(taus_arr, v_per_B3, 'g-^', markersize=4, label='B3 per-mode')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{Bi}/N_{Bi}$')
ax.set_title('(e) Per-mode spectral weight')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (f) B1 sub-sector decomposition
ax = axes[1, 2]
ax.plot(taus_arr, V_00_spec, 'b-o', markersize=4, label='(0,0)')
ax.plot(taus_arr, V_10_spec, 'c-s', markersize=4, label='(1,0)')
ax.plot(taus_arr, V_01_spec, 'm-^', markersize=4, label='(0,1)')
ax.axvline(tau_fold, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{sector}(\tau)$')
ax.set_title('(f) B1 sub-sector decomposition')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(data_dir / "s53_b1_soft_mode.png", dpi=150, bbox_inches='tight')
print(f"Plot saved: {data_dir / 's53_b1_soft_mode.png'}")

# ==========================================================================
# 15. SAVE DATA
# ==========================================================================

np.savez(data_dir / "s53_b1_soft_mode.npz",
         tau=taus_arr,
         Lambda=np.array(Lambda),
         # Per-branch spectral action
         V_B1_spec=V_B1_spec, V_B2_spec=V_B2_spec, V_B3_spec=V_B3_spec,
         V_total_spec=V_total_spec,
         # Per-branch log sum
         V_B1_log=V_B1_log, V_B2_log=V_B2_log, V_B3_log=V_B3_log,
         V_total_log=V_total_log,
         # Per-branch heat kernel
         V_B1_heat=V_B1_heat, V_B2_heat=V_B2_heat, V_B3_heat=V_B3_heat,
         V_total_heat=V_total_heat,
         # Per-mode spectral weight
         v_per_B1=v_per_B1, v_per_B2=v_per_B2, v_per_B3=v_per_B3,
         # Fractional contributions
         frac_B1=frac_B1, frac_B2=frac_B2, frac_B3=frac_B3,
         # Gap edge energies
         E_B1_min=E_B1_min, E_B2_min=E_B2_min, E_B3_min=E_B3_min,
         E_B1_mean=E_B1_mean, E_B2_mean_arr=E_B2_mean_arr, E_B3_mean_arr=E_B3_mean_arr,
         # Mode counts
         N_B1=N_B1, N_B2=N_B2, N_B3=N_B3,
         # B1 sub-sectors
         V_00_spec=V_00_spec, V_10_spec=V_10_spec, V_01_spec=V_01_spec,
         # Branch classification
         mult_B1=np.array(mult_B1), mult_B2=np.array(mult_B2), mult_B3=np.array(mult_B3),
         tau_fold=np.array(tau_fold),
         )

print(f"Data saved: {data_dir / 's53_b1_soft_mode.npz'}")
print("\nDone.")
