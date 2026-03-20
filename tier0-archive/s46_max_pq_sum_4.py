#!/usr/bin/env python3
"""
Session 46 W3-6: Dirac Spectrum at max_pq_sum = 4
===================================================

Extends the Dirac spectrum on Jensen-deformed SU(3) from max_pq_sum=3
(1232 eigenvalues, 10 sectors) to max_pq_sum=4 (2912 eigenvalues, 15 sectors).

New sectors at p+q=4: (4,0), (0,4), (3,1), (1,3), (2,2).
  dim(4,0) = 15  -> D_pi: 240x240
  dim(0,4) = 15  -> D_pi: 240x240
  dim(3,1) = 24  -> D_pi: 384x384
  dim(1,3) = 24  -> D_pi: 384x384
  dim(2,2) = 27  -> D_pi: 432x432

Reports:
  1. Number of new modes: 1680 (total 2912)
  2. Eigenvalue range of new sectors
  3. New van Hove singularities (DOS peaks)
  4. Weyl counting dimension d_Weyl convergence toward 8
  5. Spectral gap change
  6. Seeley-DeWitt coefficients a_0, a_2, a_4 and their change

Gate: None explicit (infrastructure diagnostic).

Input:
  - tier1_dirac_spectrum.py (spectrum computation infrastructure)
  - s42_hauser_feshbach.npz (existing spectrum at max_pq_sum=3)
  - canonical_constants.py

Output:
  - s46_max_pq_sum_4.npz
  - s46_max_pq_sum_4.png

Author: Gen-Physicist (Session 46)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh as scipy_eigh
from pathlib import Path

# Setup paths
DATA_DIR = Path(__file__).parent
sys.path.insert(0, str(DATA_DIR))

# Import infrastructure
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, validate_connection,
    validate_omega_hermitian, build_cliff8, get_irrep, validate_irrep,
    dirac_operator_on_irrep, _irrep_cache
)
from canonical_constants import (
    tau_fold, a0_fold as a0_fold_canon, a2_fold as a2_fold_canon,
    a4_fold as a4_fold_canon, M_KK_gravity, M_Pl_reduced, G_N, PI
)

# Matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 78)
print("S46 W3-6: DIRAC SPECTRUM AT max_pq_sum = 4")
print("=" * 78)

# ======================================================================
#  Step 0: Infrastructure setup
# ======================================================================

t_start = time.time()

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

tau = tau_fold  # = 0.19
print(f"\nJensen parameter tau = {tau}")

# Build geometric infrastructure at the fold
B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, tau)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
Omega = spinor_connection_offset(Gamma, gammas)

mc_err = validate_connection(Gamma)
is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)
omega_type = "anti-Hermitian" if is_ah else ("Hermitian" if is_h else "NEITHER")
print(f"  Connection metric-compat err = {mc_err:.2e}")
print(f"  Omega is {omega_type} (non-antiHerm = {ah_err:.2e})")

# ======================================================================
#  Step 1: Compute eigenvalues for ALL sectors p+q <= 4
# ======================================================================

print(f"\n{'='*78}")
print("STEP 1: Computing Dirac spectrum at max_pq_sum = 4")
print("=" * 78)


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# All sectors up to max_pq_sum = 4
all_sectors = []
for pq_sum in range(5):  # 0, 1, 2, 3, 4
    for p in range(pq_sum + 1):
        q = pq_sum - p
        all_sectors.append((p, q))

print(f"\nTotal sectors: {len(all_sectors)}")
print(f"New sectors (p+q=4): (4,0), (3,1), (2,2), (1,3), (0,4)")
print(f"{'(p,q)':>8s}  {'dim':>5s}  {'D size':>8s}  {'PW deg':>7s}  {'status':>10s}")
print("-" * 50)

sector_results = {}
all_pos_evals_weighted = []  # (eigenvalue, PW_multiplicity)
total_new_evals = 0

for p, q in all_sectors:
    d = dim_pq(p, q)
    matsize = d * 16
    pw_deg = d  # Peter-Weyl degeneracy = dim(p,q)
    is_new = (p + q == 4)

    t_sector = time.time()

    # Clear cache for clean construction
    _irrep_cache.clear()

    try:
        if (p, q) == (0, 0):
            # Trivial irrep: D = Omega
            D_pi = Omega.copy()
        else:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == d, f"dim mismatch: {dim_check} vs {d}"

            # Validate irrep
            hom_err, ah_err_rho = validate_irrep(rho, f_abc, f"({p},{q})")
            if hom_err > 1e-9 or ah_err_rho > 1e-9:
                print(f"  WARNING ({p},{q}): hom_err={hom_err:.2e}, ah_err={ah_err_rho:.2e}")

            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Verify anti-Hermiticity of D_pi
        ah_err_D = np.max(np.abs(D_pi + D_pi.conj().T))

        # Diagonalize via Hermitian problem: H = i*D_pi
        H = 1j * D_pi
        h_err_D = np.max(np.abs(H - H.conj().T))

        evals, evecs = scipy_eigh(H)

        # evals are real eigenvalues of i*D; Dirac eigenvalues are -i*evals (purely imaginary)
        # We work with the real evals (= imaginary parts of Dirac eigenvalues)

        dt = time.time() - t_sector
        status = "NEW" if is_new else "existing"
        print(f"  ({p},{q}):  {d:5d}  {matsize:8d}  {pw_deg:7d}  {status:>10s}  "
              f"|eval| range: [{np.min(np.abs(evals)):.4f}, {np.max(np.abs(evals)):.4f}]  "
              f"ah_err={ah_err_D:.1e}  ({dt:.2f}s)")

        # Store
        sector_results[(p, q)] = {
            'dim': d,
            'evals': evals,  # real eigenvalues of i*D
            'ah_err': ah_err_D,
            'is_new': is_new,
        }

        # Collect positive eigenvalues with PW multiplicity
        for ev in evals:
            all_pos_evals_weighted.append((ev, pw_deg))

        if is_new:
            total_new_evals += len(evals)

    except Exception as e:
        print(f"  ({p},{q}):  {d:5d}  {matsize:8d}  {pw_deg:7d}  FAILED: {e}")
        import traceback
        traceback.print_exc()

print(f"\nNew eigenvalues from p+q=4: {total_new_evals}")
print(f"Total eigenvalues: {sum(len(sr['evals']) for sr in sector_results.values())}")

# ======================================================================
#  Step 2: Seeley-DeWitt coefficients
# ======================================================================

print(f"\n{'='*78}")
print("STEP 2: Seeley-DeWitt coefficients a_0, a_2, a_4")
print("=" * 78)

# Compute a_n = sum_i d_i * |lambda_i|^{-2n} for positive eigenvalues
# with d_i = PW degeneracy = dim(p,q)
# Cutoff: exclude eigenvalues below 0.01

CUTOFF = 0.01

a0_old = 0.0  # max_pq_sum=3
a2_old = 0.0
a4_old = 0.0
a0_new = 0.0  # max_pq_sum=4
a2_new = 0.0
a4_new = 0.0

print(f"\n{'(p,q)':>8s}  {'dim':>5s}  {'n_pos':>6s}  {'a0_contrib':>12s}  "
      f"{'a2_contrib':>14s}  {'a4_contrib':>16s}  {'min_eval':>10s}")
print("-" * 90)

for p, q in all_sectors:
    if (p, q) not in sector_results:
        continue
    sr = sector_results[(p, q)]
    evals = sr['evals']
    d = sr['dim']
    pw_deg = d

    # Positive eigenvalues above cutoff
    pos_evals = evals[evals > CUTOFF]
    n_pos = len(pos_evals)

    if n_pos == 0:
        continue

    # Seeley-DeWitt sums
    s_a0 = pw_deg * n_pos
    s_a2 = pw_deg * np.sum(pos_evals**(-2))
    s_a4 = pw_deg * np.sum(pos_evals**(-4))

    if p + q <= 3:
        a0_old += s_a0
        a2_old += s_a2
        a4_old += s_a4

    a0_new += s_a0
    a2_new += s_a2
    a4_new += s_a4

    print(f"  ({p},{q}):  {d:5d}  {n_pos:6d}  {s_a0:12.1f}  {s_a2:14.6f}  "
          f"{s_a4:16.6f}  {np.min(pos_evals):10.6f}")

print(f"\n--- Comparison ---")
print(f"  max_pq_sum=3:  a0 = {a0_old:.1f},  a2 = {a2_old:.6f},  a4 = {a4_old:.6f}")
print(f"  max_pq_sum=4:  a0 = {a0_new:.1f},  a2 = {a2_new:.6f},  a4 = {a4_new:.6f}")
print(f"  canonical S42: a0 = {a0_fold_canon:.1f},  a2 = {a2_fold_canon:.6f},  "
      f"a4 = {a4_fold_canon:.6f}")
print(f"\n  Fractional increase:")
if a0_old > 0:
    print(f"    Da0/a0 = {(a0_new - a0_old)/a0_old:+.6f}  ({a0_new - a0_old:.0f} new modes)")
if a2_old > 0:
    print(f"    Da2/a2 = {(a2_new - a2_old)/a2_old:+.6f}")
if a4_old > 0:
    print(f"    Da4/a4 = {(a4_new - a4_old)/a4_old:+.6f}")

# Key ratios
r20_old = a2_old / a0_old if a0_old > 0 else np.inf
r42_old = a4_old / a2_old if a2_old > 0 else np.inf
r20_new = a2_new / a0_new if a0_new > 0 else np.inf
r42_new = a4_new / a2_new if a2_new > 0 else np.inf

print(f"\n  Ratios:")
print(f"    a2/a0: {r20_old:.8f} -> {r20_new:.8f}  (change: {(r20_new-r20_old)/r20_old:+.6f})")
print(f"    a4/a2: {r42_old:.8f} -> {r42_new:.8f}  (change: {(r42_new-r42_old)/r42_old:+.6f})")

# ======================================================================
#  Step 3: M_KK update
# ======================================================================

print(f"\n{'='*78}")
print("STEP 3: M_KK from updated a_2")
print("=" * 78)

# From s42_constants_snapshot.py (Route A):
# 1/G_N = (96/pi^2) * a_2 * M_KK^2
# Using G_N = 1/(8*pi*M_Pl_red^2):
#   8*pi*M_Pl^2 = (96/pi^2) * a_2 * M_KK^2
#   M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2)
from canonical_constants import M_KK_kerner

M_KK_old_recomp = np.sqrt(PI**3 * M_Pl_reduced**2 / (12.0 * a2_old))
M_KK_new = np.sqrt(PI**3 * M_Pl_reduced**2 / (12.0 * a2_new))
tension_old = np.log10(M_KK_kerner / M_KK_old_recomp)
tension_new = np.log10(M_KK_kerner / M_KK_new)

print(f"  M_KK(grav, old a2={a2_old:.2f}) = {M_KK_old_recomp:.4e} GeV")
print(f"  M_KK(grav, new a2={a2_new:.2f}) = {M_KK_new:.4e} GeV")
print(f"  M_KK(grav, canonical)            = {M_KK_gravity:.4e} GeV")
print(f"  M_KK(Kerner)                     = {M_KK_kerner:.4e} GeV")
print(f"\n  0.83-decade tension update:")
print(f"    Old (max_pq=3): {tension_old:.4f} decades")
print(f"    New (max_pq=4): {tension_new:.4f} decades")
print(f"    Change: {tension_new - tension_old:+.4f} decades")

# ======================================================================
#  Step 4: Spectral gap
# ======================================================================

print(f"\n{'='*78}")
print("STEP 4: Spectral gap analysis")
print("=" * 78)

# Collect all absolute eigenvalues
all_abs_evals_old = []
all_abs_evals_new = []
for p, q in all_sectors:
    if (p, q) not in sector_results:
        continue
    evals = sector_results[(p, q)]['evals']
    abs_evals = np.abs(evals)
    if p + q <= 3:
        all_abs_evals_old.extend(abs_evals[abs_evals > 1e-10])
    all_abs_evals_new.extend(abs_evals[abs_evals > 1e-10])

all_abs_evals_old = np.sort(np.array(all_abs_evals_old))
all_abs_evals_new = np.sort(np.array(all_abs_evals_new))

# Spectral gap = smallest nonzero |eigenvalue|
gap_old = all_abs_evals_old[0] if len(all_abs_evals_old) > 0 else np.inf
gap_new = all_abs_evals_new[0] if len(all_abs_evals_new) > 0 else np.inf

print(f"  Spectral gap (max_pq=3): {gap_old:.6f}")
print(f"  Spectral gap (max_pq=4): {gap_new:.6f}")
if gap_old > 0:
    print(f"  Change: {(gap_new - gap_old)/gap_old:+.6f} (relative)")

# Check if new sectors introduce eigenvalues below old gap
new_sector_min = []
for p, q in all_sectors:
    if p + q != 4 or (p, q) not in sector_results:
        continue
    evals = sector_results[(p, q)]['evals']
    abs_evals = np.abs(evals[np.abs(evals) > 1e-10])
    if len(abs_evals) > 0:
        new_sector_min.append(((p, q), np.min(abs_evals)))

print(f"\n  Minimum |eigenvalue| in new sectors:")
for (p, q), mval in new_sector_min:
    below_old_gap = "BELOW OLD GAP" if mval < gap_old else ""
    print(f"    ({p},{q}): {mval:.6f}  {below_old_gap}")

# ======================================================================
#  Step 5: Weyl counting dimension d_Weyl
# ======================================================================

print(f"\n{'='*78}")
print("STEP 5: Weyl counting dimension d_Weyl")
print("=" * 78)

# d_Weyl defined by: N(Lambda) ~ Lambda^{d_Weyl} for large Lambda
# where N(Lambda) = number of eigenvalues with |lambda| < Lambda,
# counted with PW multiplicity.

# Build cumulative weighted eigenvalue count
evals_with_mult = []
for p, q in all_sectors:
    if (p, q) not in sector_results:
        continue
    sr = sector_results[(p, q)]
    pw_deg = sr['dim']
    for ev in sr['evals']:
        if abs(ev) > 1e-10:
            evals_with_mult.append((abs(ev), pw_deg))

evals_with_mult.sort(key=lambda x: x[0])
lambdas = np.array([x[0] for x in evals_with_mult])
mults = np.array([x[1] for x in evals_with_mult])

# Cumulative count
N_cumul = np.cumsum(mults)

# Same for old spectrum (max_pq=3)
evals_old_wm = []
for p, q in all_sectors:
    if p + q > 3 or (p, q) not in sector_results:
        continue
    sr = sector_results[(p, q)]
    pw_deg = sr['dim']
    for ev in sr['evals']:
        if abs(ev) > 1e-10:
            evals_old_wm.append((abs(ev), pw_deg))
evals_old_wm.sort(key=lambda x: x[0])
lambdas_old = np.array([x[0] for x in evals_old_wm])
mults_old = np.array([x[1] for x in evals_old_wm])
N_cumul_old = np.cumsum(mults_old)

# Weyl counting via the S45 method: build N(Lambda) on a grid, then fit
# log N = d_Weyl * log Lambda + const
def spectral_counting_from_sorted(sorted_lam, sorted_N_cumul, L):
    """Count N(Lambda) = sum d_k for |lambda_k| < L."""
    idx = np.searchsorted(sorted_lam, L, side='right')
    if idx == 0:
        return 0
    return int(sorted_N_cumul[idx - 1])


def fit_d_weyl_grid(sorted_lam, sorted_N_cumul, L_lo, L_hi, n_grid=100):
    """Fit d_Weyl from N(L) on a uniform grid [L_lo, L_hi].

    This reproduces the S45 UNEXPANDED-SA-45 method exactly.
    """
    L_grid = np.linspace(L_lo, L_hi, n_grid)
    N_grid = np.array([spectral_counting_from_sorted(sorted_lam, sorted_N_cumul, L)
                       for L in L_grid])
    pos = N_grid > 0
    if np.sum(pos) < 10:
        return np.nan, np.nan
    log_L = np.log(L_grid[pos])
    log_N = np.log(N_grid[pos].astype(float))
    coeffs = np.polyfit(log_L, log_N, 1)
    return coeffs[0], np.exp(coeffs[1])  # d_weyl, c_weyl


# Fit over standard range [0.8, 2.2] (same as S45)
d_weyl_old, c_weyl_old = fit_d_weyl_grid(lambdas_old, N_cumul_old, 0.8, 2.2)
# For new spectrum: use both the old range and an extended range
d_weyl_new_restricted, c_new_r = fit_d_weyl_grid(lambdas, N_cumul, 0.8, 2.2)
d_weyl_new, c_weyl_new = fit_d_weyl_grid(lambdas, N_cumul, 0.8, 2.5)

print(f"  Weyl counting dimension (S45 method, N(L) grid fit):")
print(f"    max_pq_sum=3 [0.8,2.2]: d_Weyl = {d_weyl_old:.4f}  (S45 reported: 6.8053)")
print(f"    max_pq_sum=4 [0.8,2.2]: d_Weyl = {d_weyl_new_restricted:.4f}")
print(f"    max_pq_sum=4 [0.8,2.5]: d_Weyl = {d_weyl_new:.4f}")
print(f"    continuum:               d_Weyl = 8.0000")

deficit_old = 8.0 - d_weyl_old
deficit_new = 8.0 - d_weyl_new
print(f"\n  Deficit from 8:")
print(f"    max_pq=3: {deficit_old:.4f}")
print(f"    max_pq=4: {deficit_new:.4f}")
if deficit_new > 0:
    print(f"    Deficit reduced by factor {deficit_old/deficit_new:.2f}x")
    print(f"    Convergence: {deficit_old:.2f} -> {deficit_new:.2f} (target: 0)")

# ======================================================================
#  Step 6: Van Hove singularities (DOS peaks)
# ======================================================================

print(f"\n{'='*78}")
print("STEP 6: Van Hove singularities (density of states)")
print("=" * 78)

# Build DOS with PW multiplicity as a histogram
# Use bins of width 0.02 in eigenvalue
bin_width = 0.02
max_eval = np.max(lambdas)
bins = np.arange(0, max_eval + bin_width, bin_width)

# Old DOS
dos_old = np.zeros(len(bins) - 1)
for ev, m in zip(lambdas_old, mults_old):
    idx = int(ev / bin_width)
    if 0 <= idx < len(dos_old):
        dos_old[idx] += m

# New DOS
dos_new = np.zeros(len(bins) - 1)
for ev, m in zip(lambdas, mults):
    idx = int(ev / bin_width)
    if 0 <= idx < len(dos_new):
        dos_new[idx] += m

bin_centers = (bins[:-1] + bins[1:]) / 2

# Find peaks in DOS (local maxima)
def find_peaks(dos, centers, min_height=None):
    """Find local maxima in DOS."""
    peaks = []
    if min_height is None:
        min_height = np.max(dos) * 0.1
    for i in range(1, len(dos) - 1):
        if dos[i] > dos[i-1] and dos[i] > dos[i+1] and dos[i] >= min_height:
            peaks.append((centers[i], dos[i]))
    return peaks

peaks_old = find_peaks(dos_old, bin_centers)
peaks_new = find_peaks(dos_new, bin_centers)

print(f"\n  DOS peaks (max_pq=3): {len(peaks_old)}")
for e, h in peaks_old[:10]:
    print(f"    E = {e:.4f}, height = {h:.0f}")

print(f"\n  DOS peaks (max_pq=4): {len(peaks_new)}")
for e, h in peaks_new[:10]:
    print(f"    E = {e:.4f}, height = {h:.0f}")

# Identify NEW peaks (not present in old DOS)
new_peaks = []
for e_new, h_new in peaks_new:
    is_new = True
    for e_old, h_old in peaks_old:
        if abs(e_new - e_old) < 2 * bin_width:
            is_new = False
            break
    if is_new:
        new_peaks.append((e_new, h_new))

print(f"\n  NEW peaks from p+q=4 sectors: {len(new_peaks)}")
for e, h in new_peaks[:10]:
    print(f"    E = {e:.4f}, height = {h:.0f}")

# ======================================================================
#  Step 7: Eigenvalue range of new sectors
# ======================================================================

print(f"\n{'='*78}")
print("STEP 7: Eigenvalue range of new sectors")
print("=" * 78)

for p, q in all_sectors:
    if p + q != 4 or (p, q) not in sector_results:
        continue
    sr = sector_results[(p, q)]
    evals = sr['evals']
    abs_evals = np.abs(evals)
    pos_evals = evals[evals > 0]
    neg_evals = evals[evals < 0]

    print(f"\n  ({p},{q}): dim={sr['dim']}, {len(evals)} eigenvalues")
    print(f"    Range: [{np.min(evals):.6f}, {np.max(evals):.6f}]")
    print(f"    |evals| range: [{np.min(abs_evals):.6f}, {np.max(abs_evals):.6f}]")
    print(f"    Positive: {len(pos_evals)}, Negative: {len(neg_evals)}, Zero: {np.sum(np.abs(evals) < 1e-10)}")
    print(f"    Mean |eval|: {np.mean(abs_evals):.6f}, Std: {np.std(abs_evals):.6f}")

# ======================================================================
#  Step 8: Summary table
# ======================================================================

t_total = time.time() - t_start

print(f"\n{'='*78}")
print("SUMMARY")
print("=" * 78)

print(f"""
  Computation time: {t_total:.1f} s

  MODE COUNT:
    max_pq_sum=3: {int(sum(len(sector_results[(p,q)]['evals']) for p,q in all_sectors if p+q<=3 and (p,q) in sector_results))} eigenvalues
    max_pq_sum=4: {int(sum(len(sr['evals']) for sr in sector_results.values()))} eigenvalues
    New modes:    {total_new_evals}

  SEELEY-DEWITT COEFFICIENTS:
    a0: {a0_old:.1f} -> {a0_new:.1f}  ({(a0_new-a0_old)/a0_old*100:+.2f}%)
    a2: {a2_old:.6f} -> {a2_new:.6f}  ({(a2_new-a2_old)/a2_old*100:+.2f}%)
    a4: {a4_old:.6f} -> {a4_new:.6f}  ({(a4_new-a4_old)/a4_old*100:+.2f}%)

  KEY RATIOS:
    a2/a0: {r20_old:.8f} -> {r20_new:.8f}
    a4/a2: {r42_old:.8f} -> {r42_new:.8f}

  WEYL DIMENSION (S45 method, N(L) grid fit):
    d_Weyl [0.8,2.2]: {d_weyl_old:.4f} -> {d_weyl_new_restricted:.4f}
    d_Weyl [0.8,2.5]: -- -> {d_weyl_new:.4f}  (target: 8.0)

  SPECTRAL GAP:
    gap: {gap_old:.6f} -> {gap_new:.6f}

  M_KK (gravity route):
    {M_KK_old_recomp:.4e} -> {M_KK_new:.4e} GeV
    Tension: {tension_old:.4f} -> {tension_new:.4f} decades
""")

# ======================================================================
#  Step 9: Save
# ======================================================================

print(f"Saving results...")

# Collect eigenvalue arrays per sector
evals_dict = {}
for p, q in all_sectors:
    if (p, q) in sector_results:
        evals_dict[f'evals_{p}_{q}'] = sector_results[(p, q)]['evals']

save_dict = {
    # Metadata
    'tau': tau,
    'max_pq_sum_old': 3,
    'max_pq_sum_new': 4,
    'n_evals_old': sum(len(sector_results[(p, q)]['evals'])
                       for p, q in all_sectors if p+q <= 3 and (p, q) in sector_results),
    'n_evals_new': sum(len(sr['evals']) for sr in sector_results.values()),
    'n_new_modes': total_new_evals,

    # Seeley-DeWitt at max_pq=3
    'a0_old': a0_old,
    'a2_old': a2_old,
    'a4_old': a4_old,

    # Seeley-DeWitt at max_pq=4
    'a0_new': a0_new,
    'a2_new': a2_new,
    'a4_new': a4_new,

    # Ratios
    'r20_old': r20_old,
    'r42_old': r42_old,
    'r20_new': r20_new,
    'r42_new': r42_new,

    # Weyl dimension
    'd_weyl_old': d_weyl_old,
    'd_weyl_new': d_weyl_new,
    'd_weyl_new_restricted': d_weyl_new_restricted,

    # Spectral gap
    'gap_old': gap_old,
    'gap_new': gap_new,

    # M_KK
    'M_KK_grav_old': M_KK_old_recomp,
    'M_KK_grav_new': M_KK_new,
    'tension_old': tension_old,
    'tension_new': tension_new,

    # DOS
    'dos_bins': bin_centers,
    'dos_old': dos_old,
    'dos_new': dos_new,

    # Weyl counting
    'weyl_lambdas': lambdas,
    'weyl_N_cumul': N_cumul,
    'weyl_lambdas_old': lambdas_old,
    'weyl_N_cumul_old': N_cumul_old,

    # Computation time
    'runtime_s': t_total,
}

# Add sector eigenvalues
save_dict.update(evals_dict)

np.savez(DATA_DIR / 's46_max_pq_sum_4.npz', **save_dict)
print(f"  Saved: {DATA_DIR / 's46_max_pq_sum_4.npz'}")

# ======================================================================
#  Step 10: Plotting
# ======================================================================

print(f"\nGenerating plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'S46 W3-6: Dirac Spectrum at max\_pq\_sum = 4 ($\tau = 0.19$)',
             fontsize=14, fontweight='bold')

# Panel 1: DOS comparison
ax = axes[0, 0]
ax.bar(bin_centers, dos_old, width=bin_width*0.9, alpha=0.5, color='steelblue',
       label=f'max pq sum = 3 ({int(a0_old)} modes)')
ax.bar(bin_centers, dos_new - dos_old, width=bin_width*0.9, bottom=dos_old,
       alpha=0.5, color='crimson', label=f'new at pq sum = 4 (+{total_new_evals})')
ax.set_xlabel(r'$|\lambda|$ (M$_{\rm KK}$)')
ax.set_ylabel('DOS (PW-weighted)')
ax.set_title('Density of States')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Weyl counting N(Lambda) vs Lambda
ax = axes[0, 1]
ax.loglog(lambdas_old, N_cumul_old, 'b-', linewidth=1.5, label='max pq sum = 3')
ax.loglog(lambdas, N_cumul, 'r-', linewidth=1.5, label='max pq sum = 4')
# Reference lines
if len(lambdas) > 10:
    lam_ref = np.logspace(np.log10(lambdas[len(lambdas)//2]),
                          np.log10(lambdas[-1]), 50)
    C = N_cumul[-1] / lambdas[-1]**8
    ax.loglog(lam_ref, C * lam_ref**8, 'k--', alpha=0.3, label=r'd = 8 (continuum)')
    C_fit = c_weyl_new if not np.isnan(d_weyl_new) else 1.0
    ax.loglog(lam_ref, C_fit * lam_ref**d_weyl_new, 'g--', alpha=0.3,
              label=f'd = {d_weyl_new:.2f} (fit)')
ax.set_xlabel(r'$\Lambda$ (M$_{\rm KK}$)')
ax.set_ylabel(r'$N(\Lambda)$ (PW-weighted)')
ax.set_title(r'Weyl counting: $N(\Lambda) \sim \Lambda^{d_{\rm Weyl}}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Sector-resolved eigenvalue distribution
ax = axes[1, 0]
colors_old = plt.cm.Blues(np.linspace(0.3, 0.8, 10))
colors_new = plt.cm.Reds(np.linspace(0.3, 0.8, 5))
ci_old = 0
ci_new = 0
for p, q in all_sectors:
    if (p, q) not in sector_results:
        continue
    sr = sector_results[(p, q)]
    evals = sr['evals']
    abs_evals = np.sort(np.abs(evals[np.abs(evals) > 1e-10]))
    y_pos = p + q + (p / (p + q + 1))  # stagger vertically
    if p + q <= 3:
        ax.scatter(abs_evals, [y_pos] * len(abs_evals), s=1,
                   color=colors_old[ci_old % 10], alpha=0.5)
        ci_old += 1
    else:
        ax.scatter(abs_evals, [y_pos] * len(abs_evals), s=3,
                   color=colors_new[ci_new % 5], alpha=0.7, marker='x')
        ci_new += 1
ax.set_xlabel(r'$|\lambda|$ (M$_{\rm KK}$)')
ax.set_ylabel('p + q (sector)')
ax.set_title('Sector-resolved eigenvalue distribution')
ax.set_yticks(range(5))
ax.set_yticklabels(['p+q=0', 'p+q=1', 'p+q=2', 'p+q=3', 'p+q=4'])
ax.grid(True, alpha=0.3)

# Panel 4: Convergence table as text
ax = axes[1, 1]
ax.axis('off')
table_text = (
    f"CONVERGENCE DIAGNOSTICS (tau = {tau})\n"
    f"{'='*50}\n"
    f"{'Quantity':<25s} {'pq<=3':>12s} {'pq<=4':>12s} {'Change':>12s}\n"
    f"{'-'*50}\n"
    f"{'a_0 (mode count)':<25s} {a0_old:>12.0f} {a0_new:>12.0f} {(a0_new-a0_old)/a0_old*100:>+11.1f}%\n"
    f"{'a_2 (curvature)':<25s} {a2_old:>12.2f} {a2_new:>12.2f} {(a2_new-a2_old)/a2_old*100:>+11.1f}%\n"
    f"{'a_4 (gauge)':<25s} {a4_old:>12.2f} {a4_new:>12.2f} {(a4_new-a4_old)/a4_old*100:>+11.1f}%\n"
    f"{'a_2/a_0':<25s} {r20_old:>12.6f} {r20_new:>12.6f} {(r20_new-r20_old)/r20_old*100:>+11.2f}%\n"
    f"{'a_4/a_2':<25s} {r42_old:>12.6f} {r42_new:>12.6f} {(r42_new-r42_old)/r42_old*100:>+11.2f}%\n"
    f"{'d_Weyl [0.8,2.5]':<25s} {d_weyl_old:>12.4f} {d_weyl_new:>12.4f} {'':>12s}\n"
    f"{'spectral gap':<25s} {gap_old:>12.6f} {gap_new:>12.6f} {'':>12s}\n"
    f"{'M_KK (GeV)':<25s} {M_KK_old_recomp:>12.2e} {M_KK_new:>12.2e} {'':>12s}\n"
    f"{'tension (decades)':<25s} {tension_old:>12.4f} {tension_new:>12.4f} {'':>12s}\n"
    f"{'-'*50}\n"
    f"Target d_Weyl = 8. Runtime = {t_total:.1f} s"
)
ax.text(0.05, 0.95, table_text, transform=ax.transAxes,
        fontsize=8, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plot_path = DATA_DIR / 's46_max_pq_sum_4.png'
plt.savefig(plot_path, dpi=150)
print(f"  Saved: {plot_path}")
plt.close()

print(f"\nDone. Total runtime: {t_total:.1f} s")
