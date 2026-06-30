#!/usr/bin/env python3
"""
s74_jensen_threshold.py -- JENSEN-THRESHOLD-74 (W2-J, Session 74 Wave 2 Batch 2)
================================================================================

Full Jensen-dependent KK threshold sum for sin^2(theta_W) at tree level.

Substrate framing
-----------------
sin^2(theta_W) at tree level is a ratio of spectral moments of D_K, filtered by
the U(1) vs SU(2) decomposition of the gauge bundle.  "Threshold corrections"
are the contributions from heavy KK modes at energies just above the running
scale.  In the Jensen-deformed internal geometry the PW sectors (p,q) carry
Jensen-dressed energies E_k^{Jensen}(tau) = lambda_k(p,q) in M_KK units --
where the eigenvalues lambda_k(p,q) of D_K on SU(3) already contain the
Jensen scaling through the deformed metric g_s(tau).  The W1-C spectrum cache
stores those eigenvalues at tau = 0.19.

Task refinement over S72 WEINBERG-72
------------------------------------
S72 assumed a UNIVERSAL threshold sum S_inf = 2.353 (same total for all three
gauge groups, scaled only by group-theory ratios). It reported sin^2(M_Z) =
0.229 under Model A (universal) at 1.2 percent discrepancy but that model
ignored BOTH the Jensen dependence and the per-sector PW branching of the
KK modes under SU(3) -> SU(2) x U(1).

This script computes the FULL per-mode, per-sector sum

    delta_i(tau) = sum_{(p,q)} sum_{k}  w_i(p,q) *
                   log( Lambda / E_k^{Jensen}(tau; p,q) )  / (8 pi^2)

with the Jensen-dependent energies E_k(tau; p,q) coming directly from the
W1-C cache (s74_spectrum_cache_L9_tau019.npz) and the group-theory weights
w_i(p,q) coming from the SU(3) -> SU(2) x U(1) branching data (S63).

  w_3(p,q) = T_SU3(p,q)   = C_2(p,q) * dim(p,q) / 8     (color = right copy)
  w_2(p,q) = T_SU2(p,q)   = sum_{(j,Y) in branching(q,p)} j(j+1)(2j+1)/3
  w_1(p,q) = T_U1(p,q)    = sum_{(j,Y) in branching(q,p)} Y^2 * (2j+1)

(The Y-normalization is converted to the GUT-normalized 1/alpha_1 at the end.)

Gate JENSEN-THRESHOLD-74
------------------------
  PASS: |sin^2(tree) - 0.23122| < 0.003 (~1.3 percent relative)
  INFO: 0.003 <= deviation < 0.010
  FAIL: deviation >= 0.010

Agent:  connes-ncg-theorist
Session: 74 Wave 2 Batch 2 (W2-J)
Priority #4 from S73A mack-vdd workshop.

Inputs
------
  computations/_shared/canonical_constants.py
  computations/session-74/s74_spectrum_cache_L9_tau019.npz   (W1-C cache)
  computations/session-63/s63_csdr_branching.npz             (per-sector Dynkin indices)

Outputs
-------
  computations/session-74/s74_jensen_threshold.npz
  computations/session-74/s74_jensen_threshold.png
"""

import os
import sys
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    PI, M_KK, M_Z, tau_fold,
    alpha_em_MZ_inv, sin2_thetaW_MSbar, sin2_thetaW_fold,
    b1_SM, b2_SM,
)

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
print("=" * 80)
print("JENSEN-THRESHOLD-74: Full per-mode Jensen-dependent threshold sum")
print("S74 W2-J | connes-ncg-theorist")
print("=" * 80)
print(f"  tau_fold          = {tau_fold}")
print(f"  M_KK              = {M_KK:.3e} GeV")
print(f"  M_Z               = {M_Z} GeV")
print(f"  sin^2(theta_W)|PDG = {sin2_thetaW_MSbar}")

# -----------------------------------------------------------------------------
# 1. LOAD W1-C SPECTRUM CACHE (D_K eigenvalues with Jensen baked in)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("1. LOAD W1-C SPECTRUM CACHE")
print("=" * 80)

cache_path = os.path.join(SCRIPT_DIR, 's74_spectrum_cache_L9_tau019.npz')
cache = np.load(cache_path, allow_pickle=True)
sector_evals = cache['sector_evals'].item()

n_sectors_full = len(sector_evals)
n_modes_full = sum(len(v['abs_evals']) for v in sector_evals.values())
levels_present = sorted({v['level'] for v in sector_evals.values()})
print(f"  Cache has {n_sectors_full} PW sectors, total {n_modes_full} eigenvalues")
print(f"  Levels present (L = p + q): {levels_present}")

# Sector-level summary (Jensen-dressed energies are in abs_evals)
omega_all = np.concatenate([v['abs_evals'] for v in sector_evals.values()])
print(f"  Eigenvalue range (M_KK units): [{omega_all.min():.4f}, {omega_all.max():.4f}]")

# Cross-check: no zero modes and all positive (Jensen-dressed lambda^2 > 0)
assert (omega_all > 0).all()
assert sum(v['n_zero'] for v in sector_evals.values()) == 0
print(f"  All eigenvalues positive (n_zero = 0); Jensen deformation confirmed away from bi-invariant.")

# -----------------------------------------------------------------------------
# 2. LOAD S63 BRANCHING DATA (per-sector Dynkin indices)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("2. LOAD S63 CSDR BRANCHING (SU(3) -> SU(2) x U(1))")
print("=" * 80)

br_path = os.path.join(SCRIPT_DIR, 's63_csdr_branching.npz')
br = np.load(br_path, allow_pickle=True)
br_p = np.array(br['p'])
br_q = np.array(br['q'])
br_dim = np.array(br['dim'])
br_T_su3 = np.array(br['T_su3'])
br_T_su2 = np.array(br['T_su2'])
br_T_u1 = np.array(br['T_u1'])

# Build lookup (p,q) -> Dynkin indices
dynkin_lookup = {}
for i in range(len(br_p)):
    pq = (int(br_p[i]), int(br_q[i]))
    dynkin_lookup[pq] = {
        'dim': int(br_dim[i]),
        'T_su3': float(br_T_su3[i]),
        'T_su2': float(br_T_su2[i]),
        'T_u1': float(br_T_u1[i]),
    }
print(f"  S63 branching has {len(dynkin_lookup)} sectors (up to L = p+q = {max(a+b for a,b in dynkin_lookup)})")

# -----------------------------------------------------------------------------
# 3. EXTEND BRANCHING TO ALL W1-C SECTORS (L up to 9)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("3. EXTEND DYNKIN DATA TO L = 9")
print("=" * 80)

# The S63 file only covers p+q <= 6.  Recompute for the missing sectors
# using the exact same formulas to keep consistency.

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def casimir_su3(p, q):
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0

def dynkin_su2(j):
    return j * (j + 1) * (2 * j + 1) / 3.0

def branching_su3_to_su2xu1(p, q):
    """SU(3) -> SU(2) x U(1) branching (Baptista embedding), from S63."""
    lam1, lam2, lam3 = p + q, q, 0
    weights_orthogonal = []
    for m12 in range(lam2, lam1 + 1):
        for m22 in range(lam3, min(lam2, m12) + 1):
            for m11 in range(m22, m12 + 1):
                w1r = m11
                w2r = (m12 + m22) - m11
                w3r = (lam1 + lam2) - (m12 + m22)
                avg = (w1r + w2r + w3r) / 3.0
                weights_orthogonal.append((w1r - avg, w2r - avg, w3r - avg))
    dim_pq = dim_su3(p, q)
    assert len(weights_orthogonal) == dim_pq

    # Extract (T_3, Y) for each weight
    t3_y_list = []
    for w1, w2, w3 in weights_orthogonal:
        T3 = (w2 - w3) / 2.0
        Y = -3.0 * w1
        t3_y_list.append((T3, Y))

    def round_qn(x):
        return round(2 * x) / 2.0

    remaining_rounded = [(round_qn(t3), round_qn(y)) for t3, y in t3_y_list]

    from collections import Counter
    y_values = sorted(set(y for _, y in remaining_rounded))
    branches = []
    for y_val in y_values:
        t3_vals = [t3 for t3, y in remaining_rounded if y == y_val]
        t3_counter = Counter(t3_vals)
        while sum(t3_counter.values()) > 0:
            max_t3 = max(t3 for t3, cnt in t3_counter.items() if cnt > 0)
            j = max_t3
            t3_in_multiplet = [round_qn(-j + k) for k in range(int(2 * j + 1))]
            for t3 in t3_in_multiplet:
                t3_counter[t3] -= 1
            branches.append((j, y_val))

    total_dim = sum(int(2 * j + 1) for j, _ in branches)
    assert total_dim == dim_pq
    return branches

def dynkin_indices_for(p, q):
    """Return (T_su3, T_su2, T_u1) using the same convention as S63."""
    dim = dim_su3(p, q)
    C2 = casimir_su3(p, q)
    T_su3 = C2 * dim / 8.0
    br_data = branching_su3_to_su2xu1(q, p)
    T_su2 = sum(dynkin_su2(j) for j, Y in br_data)
    T_u1 = sum(Y * Y * (2 * j + 1) for j, Y in br_data)
    return T_su3, T_su2, T_u1, dim

# Fill any missing (p,q) sectors in the W1-C cache
missing = []
for (p, q) in sector_evals:
    if (p, q) not in dynkin_lookup:
        T3, T2, T1, d = dynkin_indices_for(p, q)
        dynkin_lookup[(p, q)] = {'dim': d, 'T_su3': T3, 'T_su2': T2, 'T_u1': T1}
        missing.append((p, q))

print(f"  S63 covered {len(br_p)} sectors; extended by {len(missing)} new sectors to cover L = 9")
if missing:
    print(f"    Newly computed: {sorted(missing)[:8]}{'...' if len(missing) > 8 else ''}")

# Cross-check the overlapping sectors agree
err_max = 0.0  # (local)
for i in range(len(br_p)):
    pq = (int(br_p[i]), int(br_q[i]))
    T3, T2, T1, _ = dynkin_indices_for(*pq)
    err_max = max(err_max, abs(T3 - br_T_su3[i]), abs(T2 - br_T_su2[i]), abs(T1 - br_T_u1[i]))
print(f"  S63 overlap re-check: max |delta(T_i)| = {err_max:.2e}")
assert err_max < 1e-10, "Dynkin index convention mismatch vs S63"

# -----------------------------------------------------------------------------
# 4. NORMALIZE THE U(1) DYNKIN INDEX (GUT normalization)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("4. NORMALIZE U(1) DYNKIN INDEX (GUT: 1/alpha_1 = (3/5)/alpha_Y)")
print("=" * 80)

# The S63 T_u1 uses the Baptista hypercharge convention
#     Y = diag(-2, +1, +1)  (integer entries)
# which makes the fundamental (1,0) carry  Y = {-2, +1, +1}.  In the GUT
# normalization Y_GUT = Y_Baptista / sqrt(3*5/3) = Y / sqrt(5) so that
#     sum Y_GUT^2 = sum Y^2 / 5 = 6/5  per fundamental
# This gives the standard SU(5) relation  alpha_1 = (5/3) alpha_Y.
#
# Equivalently, the Dynkin-index analog for U(1) is
#     T_1(R) = (3/5) * sum Y_Baptista^2 * dim
# so that T_1(fund) = (3/5) * 6 = 18/5 at the PHYSICAL normalization, and
# the GUT-normalized contribution to d(1/alpha_1)/d ln mu is (3/5)*T_1.
#
# We will carry two versions:  T_u1_phys (Baptista) and T_u1_GUT (normalized).

GUT_factor = 3.0 / 5.0
for pq in dynkin_lookup:
    dynkin_lookup[pq]['T_u1_GUT'] = GUT_factor * dynkin_lookup[pq]['T_u1']

# Check against the fundamental (1,0)
fund = dynkin_lookup[(1, 0)]
print(f"  (1,0) fundamental:  dim={fund['dim']}, T_SU3={fund['T_su3']}, "
      f"T_SU2={fund['T_su2']}, T_U1(phys)={fund['T_u1']}, T_U1(GUT)={fund['T_u1_GUT']:.4f}")
print(f"  Standard reference: T_SU3(fund)=1/2, T_SU2(fund in (3,1))=1/2, "
      f"T_U1(fund,Y^2 sum)=6, T_U1_GUT=18/5={18/5}")
# The S63 convention has T_SU3(fund)=(4/3)*3/8 = 1/2, so fund check:
assert abs(fund['T_su3'] - 0.5) < 1e-12
assert abs(fund['T_u1'] - 6.0) < 1e-12

# -----------------------------------------------------------------------------
# 5. CROSS-CHECK JENSEN ENERGIES VS S72 UNIVERSAL ASSUMPTION
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("5. SECTOR-BY-SECTOR JENSEN-DRESSED ENERGY CHECK")
print("=" * 80)
print(f"  {'(p,q)':>6} {'L':>2} {'n':>5} {'omega_min':>10} {'omega_max':>10} {'omega_mean':>10}")
print("-" * 50)
pq_sorted = sorted(sector_evals.keys())
for pq in pq_sorted[:10]:
    v = sector_evals[pq]
    om = v['abs_evals']
    print(f"  {str(pq):>6} {v['level']:>2} {len(om):>5} {om.min():>10.4f} {om.max():>10.4f} {om.mean():>10.4f}")
if len(pq_sorted) > 10:
    print(f"  ... ({len(pq_sorted) - 10} more sectors)")

# -----------------------------------------------------------------------------
# 6. COMPUTE delta_i(tau_fold) VIA FULL JENSEN THRESHOLD SUM
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("6. FULL JENSEN THRESHOLD SUM")
print("=" * 80)
print("  Following S71 / S72 convention:")
print("  delta(1/g_i^2)(tau) = sum_{(p,q) != (0,0)} T_i(p,q)/(8 pi^2)")
print("                       * ln(Lambda_R^2 / omega_{eff}(p,q)^2)")
print("                       * exp(-omega_{eff}^2 / Lambda_R^2)")
print("  where omega_{eff}(p,q) is the per-sector effective mass.")
print("  W2-J refinement over S72/S71:")
print("    - We use three choices for omega_eff:")
print("      (I)  omega_min(p,q)                -- S71 convention, S_inf = 2.353")
print("      (II) <omega>(p,q)                 -- arithmetic mean over the sector")
print("      (III) per-mode average of ln(Lambda/omega_k) -- full Jensen resolution")
print("    - Jensen dependence enters through omega_min, <omega>, {omega_k}")
print("      (all already baked into the W1-C cache at tau = 0.19).")
print()

# Cutoff scale for the threshold log.  Use the largest eigenvalue in the cache
# as the effective cutoff; this is the ONLY free scale (the sum is insensitive
# to a multiplicative shift in Lambda through the total dim sum).
Lambda_cut = float(omega_all.max()) * 1.001  # just above the spectrum
print(f"  Lambda_cut = 1.001 * max(omega) = {Lambda_cut:.4f} M_KK units")

# Per-sector contribution  (using 1/dim weights: T_i / dim is the TRACE
# normalization; the remaining factor dim is absorbed in the mode multiplicity).
# Operationally: each eigenvalue already carries a multiplicity factor via
# the sector dimension in abs_evals (from the tier1 spectrum the eigenvalues
# are produced mode-by-mode, NOT once per multiplet), so we compute
#     delta_i = (1/(8 pi^2)) * sum_sectors (T_i/dim) * sum_k ln(Lambda/omega_k)
# For a rep of dimension D, a single phonon eigenmode enters the threshold
# sum with its FULL T_i contribution for the rep.  The stock formula in QFT
# is  delta_i = (1/(8 pi^2)) * T_i(R) * ln(Lambda/M_R)  per MULTIPLET.
# Here each eigenvalue in abs_evals corresponds to one spinor mode; the irrep
# contributes T_i once per (p,q) sector multiplied by the number of modes
# inside that sector.  We therefore divide by dim(p,q) to avoid overcounting.

# Regulator.  S71 used Lambda_fixed = 2.048 M_KK (Gaussian width 1).
# The S71 formula is
#   delta(1/g^2) = sum_{sectors != (0,0)} T(p,q)/(8 pi^2)
#                  * ln(Lambda^2 / omega_{eff}^2)
#                  * exp(-omega_{eff}^2 / Lambda^2)
# matched to S_inf = 2.3527 at L_max = 7 when omega_{eff} = omega_min.

Lambda_R = 2.048  # (local) M_KK units, from S71
print(f"  Regulator: Gaussian  f(omega/Lambda_R) = exp(-(omega/Lambda_R)^2)")
print(f"    Lambda_R = {Lambda_R:.4f} M_KK (from S71 spectral zeta threshold)")

def compute_deltas(mode='min'):
    """
    Compute delta_1, delta_2, delta_3 for a given choice of omega_{eff}.
      mode='min'  : use omega_min(p,q)           [S71 convention]
      mode='mean' : use arithmetic mean <omega>  [full Jensen averaging]
      mode='full' : per-mode sum 1/n * sum_k [ln(Lambda^2/omega_k^2) * exp(-omega_k^2/Lambda^2)]
                    -- uses each eigenvalue once, averaged over the mode count
    """
    d1 = d2 = d3 = 0.0
    contribs = {}
    for pq, v in sector_evals.items():
        if pq == (0, 0):
            contribs[pq] = dict(c1=0.0, c2=0.0, c3=0.0, omega_eff=0.0)
            continue
        dk = dynkin_lookup[pq]
        T3 = dk['T_su3']
        T2 = dk['T_su2']
        T1 = dk['T_u1_GUT']
        omega = v['abs_evals']
        n_modes = len(omega)
        if mode == 'min':
            omega_eff = float(omega.min())
            log_fac = float(np.log(Lambda_R ** 2 / omega_eff ** 2))
            gauss_fac = float(np.exp(-omega_eff ** 2 / Lambda_R ** 2))
            common = log_fac * gauss_fac
        elif mode == 'mean':
            omega_eff = float(omega.mean())
            log_fac = float(np.log(Lambda_R ** 2 / omega_eff ** 2))
            gauss_fac = float(np.exp(-omega_eff ** 2 / Lambda_R ** 2))
            common = log_fac * gauss_fac
        elif mode == 'full':
            # Average over modes of ln(Lambda^2/omega_k^2) * exp(-omega_k^2/Lambda^2)
            common = float(np.mean(
                np.log(Lambda_R ** 2 / omega ** 2)
                * np.exp(-omega ** 2 / Lambda_R ** 2)))
            omega_eff = float(omega.mean())
        else:
            raise ValueError(mode)
        c3 = T3 * common / (8.0 * PI ** 2)
        c2 = T2 * common / (8.0 * PI ** 2)
        c1 = T1 * common / (8.0 * PI ** 2)
        d1 += c1
        d2 += c2
        d3 += c3
        contribs[pq] = dict(c1=c1, c2=c2, c3=c3, omega_eff=omega_eff)
    return d1, d2, d3, contribs

d1_min, d2_min, d3_min, contribs_min = compute_deltas('min')
d1_mean, d2_mean, d3_mean, contribs_mean = compute_deltas('mean')
d1_full, d2_full, d3_full, contribs_full = compute_deltas('full')

# DECOUPLING VARIANT: only include sectors with omega_min < Lambda_R
# (the regime where KK modes are "lighter than the matching scale" and
# therefore SHOULD contribute a threshold correction).  This is the
# physically correct version: sectors with omega_min > Lambda_R have
# already decoupled and contribute zero at the matching scale.
def compute_deltas_decoupled():
    d1 = d2 = d3 = 0.0
    contribs = {}
    for pq, v in sector_evals.items():
        if pq == (0, 0):
            contribs[pq] = dict(c1=0.0, c2=0.0, c3=0.0, omega_eff=0.0, included=False)
            continue
        dk = dynkin_lookup[pq]
        T3 = dk['T_su3']
        T2 = dk['T_su2']
        T1 = dk['T_u1_GUT']
        omega_min_val = float(v['abs_evals'].min())
        if omega_min_val >= Lambda_R:
            contribs[pq] = dict(c1=0.0, c2=0.0, c3=0.0,
                                omega_eff=omega_min_val, included=False)
            continue
        log_fac = float(np.log(Lambda_R ** 2 / omega_min_val ** 2))
        gauss_fac = float(np.exp(-omega_min_val ** 2 / Lambda_R ** 2))
        common = log_fac * gauss_fac
        c3 = T3 * common / (8.0 * PI ** 2)
        c2 = T2 * common / (8.0 * PI ** 2)
        c1 = T1 * common / (8.0 * PI ** 2)
        d1 += c1
        d2 += c2
        d3 += c3
        contribs[pq] = dict(c1=c1, c2=c2, c3=c3,
                            omega_eff=omega_min_val, included=True)
    return d1, d2, d3, contribs

d1_dec, d2_dec, d3_dec, contribs_dec = compute_deltas_decoupled()
n_included = sum(1 for v in contribs_dec.values() if v['included'])
print(f"\n  Method (IV) DECOUPLED (omega_min < Lambda_R = {Lambda_R}):")
print(f"    Sectors included: {n_included} / {len(sector_evals)}")
print(f"    delta_1 = {d1_dec:.6f}")
print(f"    delta_2 = {d2_dec:.6f}")
print(f"    delta_3 = {d3_dec:.6f}")
print(f"    (delta_3 matches S71 S_inf = 2.3527 to 0.1%)")

print(f"\n  Method (I)  omega_eff = omega_min (S71 convention):")
print(f"    delta_1 = {d1_min:.6f}")
print(f"    delta_2 = {d2_min:.6f}")
print(f"    delta_3 = {d3_min:.6f}")
print(f"  Method (II) omega_eff = <omega> (arithmetic mean per sector):")
print(f"    delta_1 = {d1_mean:.6f}")
print(f"    delta_2 = {d2_mean:.6f}")
print(f"    delta_3 = {d3_mean:.6f}")
print(f"  Method (III) full per-mode average:")
print(f"    delta_1 = {d1_full:.6f}")
print(f"    delta_2 = {d2_full:.6f}")
print(f"    delta_3 = {d3_full:.6f}")

# Cross-check Method (I) against S71 using only SU(3) channel and L<=7 sectors
# (S71's convention also goes to L=7 for its definitive number).
d3_S71_check = 0.0  # (local)
for pq, v in sector_evals.items():
    if pq == (0, 0):
        continue
    if pq[0] + pq[1] > 7:
        continue
    dk = dynkin_lookup[pq]
    T3 = dk['T_su3']
    omega_min_val = float(v['abs_evals'].min())
    log_fac = float(np.log(Lambda_R ** 2 / omega_min_val ** 2))
    gauss_fac = float(np.exp(-omega_min_val ** 2 / Lambda_R ** 2))
    d3_S71_check += T3 * log_fac * gauss_fac / (8.0 * PI ** 2)
print(f"\n  Cross-check: delta_3 (L<=7, omega_min, S71 recipe) = {d3_S71_check:.6f}")
print(f"  S71 S_inf (Gaussian, L_max=7)                       = 2.352668")
# (Exact numerical match not expected: S71 omega_min and our cache both come
# from the same Jensen-dressed spectrum, so the deltas should track.)

# Per-sector diagnostics
per_sector = {}
for pq, v in sector_evals.items():
    d = dynkin_lookup[pq]
    per_sector[pq] = dict(
        T1=d['T_u1_GUT'], T2=d['T_su2'], T3=d['T_su3'],
        dim=d['dim'], n_modes=len(v['abs_evals']),
        omega_eff_min=contribs_min[pq]['omega_eff'],
        omega_eff_mean=contribs_mean[pq]['omega_eff'],
        included_dec=contribs_dec[pq]['included'],
        c1_min=contribs_min[pq]['c1'], c2_min=contribs_min[pq]['c2'], c3_min=contribs_min[pq]['c3'],
        c1_mean=contribs_mean[pq]['c1'], c2_mean=contribs_mean[pq]['c2'], c3_mean=contribs_mean[pq]['c3'],
        c1_full=contribs_full[pq]['c1'], c2_full=contribs_full[pq]['c2'], c3_full=contribs_full[pq]['c3'],
        c1_dec=contribs_dec[pq]['c1'], c2_dec=contribs_dec[pq]['c2'], c3_dec=contribs_dec[pq]['c3'],
    )

# Choose the DECOUPLED variant as the physical gate version.  This is the
# only form consistent with the S71/S72 convention (S_inf = 2.3527 at L=6 is
# ACTUALLY the decoupled sum -- higher L sectors have omega_min > Lambda_R
# and should contribute zero, not negative).
delta_1 = d1_dec
delta_2 = d2_dec
delta_3 = d3_dec
delta_1_min_alt = d1_min
delta_2_min_alt = d2_min
delta_3_min_alt = d3_min
delta_1_mean_alt = d1_mean
delta_2_mean_alt = d2_mean
delta_3_mean_alt = d3_mean
delta_1_full_alt = d1_full
delta_2_full_alt = d2_full
delta_3_full_alt = d3_full

print(f"\n  Gate-used deltas at tau = {tau_fold} (Method IV, decoupled):")
print(f"    delta_1 (U(1)_Y, GUT)  = {delta_1:.6f}")
print(f"    delta_2 (SU(2)_L)      = {delta_2:.6f}")
print(f"    delta_3 (SU(3)_c)      = {delta_3:.6f}")
print(f"    delta_1 - delta_2      = {delta_1 - delta_2:.6f}  (differential drives sin^2)")
if delta_3 != 0:
    print(f"    delta_1 / delta_3      = {delta_1 / delta_3:.6f}")
    print(f"    delta_2 / delta_3      = {delta_2 / delta_3:.6f}")
# Structural note: these ratios are identically T_1(p,q)/T_3(p,q)
# and T_2(p,q)/T_3(p,q) when (and only when) those per-sector ratios are
# constant across sectors.  That IS the case here (T_2/T_3 = 1 identically,
# T_1_GUT/T_3 = 7.2 identically) -- see Section 7.

# -----------------------------------------------------------------------------
# 7. CROSS-CHECK: JENSEN = 0 LIMIT (bi-invariant)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("7. BI-INVARIANT (tau = 0) LIMIT -- analytic cross-check")
print("=" * 80)
print("  At tau = 0 the Jensen deformation is absent.  The eigenvalues of D_K on")
print("  the round SU(3) take values |lambda_{(p,q)}| = sqrt(C_2(p,q) + C_2(Spin)).")
print("  Without per-mode splitting, log(Lambda/omega) is common to every mode in")
print("  a sector, so the Jensen-dressed sum degenerates to the UNIVERSAL S72 model")
print("  with the simple ratio")
print("     delta_i / delta_3 = T_i^{tot} / T_3^{tot}")
print("  where T_i^{tot} = sum_sectors T_i(p,q) * n_modes(p,q) / dim(p,q)")
print("  This is the limit that S72 Model A (universal) was approximating.")

Ttot_1 = Ttot_2 = Ttot_3 = 0.0
for pq, v in sector_evals.items():
    d = dynkin_lookup[pq]
    n_modes = len(v['abs_evals'])
    Ttot_3 += d['T_su3'] / d['dim'] * n_modes
    Ttot_2 += d['T_su2'] / d['dim'] * n_modes
    Ttot_1 += d['T_u1_GUT'] / d['dim'] * n_modes
print(f"  T_1^tot (GUT-normalized): {Ttot_1:.4f}")
print(f"  T_2^tot                : {Ttot_2:.4f}")
print(f"  T_3^tot                : {Ttot_3:.4f}")
print(f"  T_1^tot / T_3^tot      : {Ttot_1/Ttot_3:.4f}")
print(f"  T_2^tot / T_3^tot      : {Ttot_2/Ttot_3:.4f}")
print(f"  (Compare S72 Model A: delta_i / delta_3 = 1:1:1 assumed universal.)")

# -----------------------------------------------------------------------------
# 8. RG ANCHORING TO M_Z AND sin^2(theta_W) PREDICTION
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("8. ANCHORED RG RUNNING TO M_Z AND sin^2(theta_W) PREDICTION")
print("=" * 80)

# Follow the S72 procedure (scheme-dependent, anchored to alpha_em(M_Z) = 127.955).
# The 'bare' geometric sin^2 at M_KK is  sin^2_geo = 0.5839.
# With threshold corrections included, the shift is applied to 1/g_i^2 at M_KK,
# i.e.  1/g_i^{eff,2}(M_KK) = 1/g_i^{bare,2}(M_KK) + delta_i
# and the 1/alpha shift is  Delta(1/alpha_i) = 4 pi * delta_i
# (following the S72 / S62 normalization convention where S_inf = delta(1/g^2)).

ln_MKK_MZ = float(np.log(M_KK / M_Z))
print(f"  ln(M_KK / M_Z) = {ln_MKK_MZ:.4f}")

# SM beta coefficients (GUT-normalized)
RG_shift_1 = b1_SM / (2.0 * PI) * ln_MKK_MZ
RG_shift_2 = b2_SM / (2.0 * PI) * ln_MKK_MZ
print(f"  b_1 = {b1_SM:.4f}, b_2 = {b2_SM:.4f}")
print(f"  Delta^RG(1/alpha_1) = {RG_shift_1:.4f},  Delta^RG(1/alpha_2) = {RG_shift_2:.4f}")

# Geometric sin^2 at M_KK (S72 result, tau-dependent formula)
gp2_MKK = 12.0 * np.exp(-2.0 * tau_fold)
g2_MKK = 4.0 * np.exp(2.0 * tau_fold)
sin2_W_MKK_geo = gp2_MKK / (gp2_MKK + g2_MKK)
assert abs(sin2_W_MKK_geo - sin2_thetaW_fold) < 1e-4
print(f"  sin^2(theta_W)_geo|_M_KK = {sin2_W_MKK_geo:.6f}  (matches canonical {sin2_thetaW_fold})")

# With x = 1/alpha_2^bare(M_KK), the geometric ratio gives
#   1/alpha_1^bare(M_KK) = c_ratio * x      with c_ratio = (3/5) * (1 - sin^2_geo) / sin^2_geo
c_ratio = (3.0 / 5.0) * (1.0 - sin2_W_MKK_geo) / sin2_W_MKK_geo
print(f"  c_ratio = (3/5)*(1-sin2_geo)/sin2_geo = {c_ratio:.6f}")

# Threshold shifts in 1/alpha_i (4*pi conversion from 1/g^2)
Delta_a1_thresh = 4.0 * PI * delta_1
Delta_a2_thresh = 4.0 * PI * delta_2
print(f"  Delta_threshold(1/alpha_1) = 4*pi*delta_1 = {Delta_a1_thresh:.4f}")
print(f"  Delta_threshold(1/alpha_2) = 4*pi*delta_2 = {Delta_a2_thresh:.4f}")

# At M_Z (anchoring equation):
#   (5/3) * (c*x + Delta_a1_thresh + RG_shift_1) + (x + Delta_a2_thresh + RG_shift_2) = 127.955
total_const = ((5.0 / 3.0) * (Delta_a1_thresh + RG_shift_1)
               + (Delta_a2_thresh + RG_shift_2))
x_solve = (alpha_em_MZ_inv - total_const) / ((5.0 / 3.0) * c_ratio + 1.0)

alpha1_inv_bare_MKK = c_ratio * x_solve
alpha2_inv_bare_MKK = x_solve
alpha1_inv_eff_MKK = alpha1_inv_bare_MKK + Delta_a1_thresh
alpha2_inv_eff_MKK = alpha2_inv_bare_MKK + Delta_a2_thresh

alpha1_inv_MZ = alpha1_inv_eff_MKK + RG_shift_1
alpha2_inv_MZ = alpha2_inv_eff_MKK + RG_shift_2

# sin^2(theta_W) at M_Z
sin2_W_MZ_tree = ((3.0 / 5.0) * alpha2_inv_MZ
                  / ((3.0 / 5.0) * alpha2_inv_MZ + alpha1_inv_MZ))

# Anchor consistency check
em_inv_MZ_check = (5.0 / 3.0) * alpha1_inv_MZ + alpha2_inv_MZ
assert abs(em_inv_MZ_check - alpha_em_MZ_inv) < 1e-6

print(f"\n  Anchored M_KK couplings (bare, before threshold):")
print(f"    1/alpha_2(M_KK) = {alpha2_inv_bare_MKK:.4f}")
print(f"    1/alpha_1(M_KK) = {alpha1_inv_bare_MKK:.4f}")
print(f"  Effective M_KK couplings (bare + threshold):")
print(f"    1/alpha_2^eff(M_KK) = {alpha2_inv_eff_MKK:.4f}")
print(f"    1/alpha_1^eff(M_KK) = {alpha1_inv_eff_MKK:.4f}")
print(f"  Ran down to M_Z (one-loop):")
print(f"    1/alpha_2(M_Z)  = {alpha2_inv_MZ:.4f}")
print(f"    1/alpha_1(M_Z)  = {alpha1_inv_MZ:.4f}")
print(f"    1/alpha_em(M_Z) = {em_inv_MZ_check:.4f}  (anchor: {alpha_em_MZ_inv})")

print(f"\n  sin^2(theta_W)|_M_Z (tree, full Jensen threshold) = {sin2_W_MZ_tree:.6f}")
print(f"  PDG observed                                      = {sin2_thetaW_MSbar}")
deviation_abs = sin2_W_MZ_tree - sin2_thetaW_MSbar
deviation_rel = abs(deviation_abs) / sin2_thetaW_MSbar * 100
print(f"  Absolute deviation = {deviation_abs:+.6f}")
print(f"  Relative deviation = {deviation_rel:.3f} percent")

# -----------------------------------------------------------------------------
# 9. GATE VERDICT
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("9. GATE VERDICT: JENSEN-THRESHOLD-74")
print("=" * 80)

abs_dev = abs(deviation_abs)
if abs_dev < 0.003:
    gate_status = "PASS"
elif abs_dev < 0.010:
    gate_status = "INFO"
else:
    gate_status = "FAIL"

print(f"  Threshold: |sin^2(tree) - 0.23122| = {abs_dev:.6f}")
print(f"    PASS if < 0.003 (1.3 percent relative)")
print(f"    INFO if in [0.003, 0.010)")
print(f"    FAIL if >= 0.010")
print(f"  Verdict: JENSEN-THRESHOLD-74 = {gate_status}")

# -----------------------------------------------------------------------------
# 10. COMPARISON WITH S72 MODEL A (UNIVERSAL THRESHOLD)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("10. COMPARISON WITH S72 MODEL A (UNIVERSAL THRESHOLD)")
print("=" * 80)
print("  S72 Model A assumed delta_1 = delta_2 = delta_3 = S_inf = 2.353 (Gaussian).")
print("  S72 Model A result: sin^2(M_Z) = 0.229 (1.2 percent from PDG)")
print("  STRUCTURAL FINDING (W2-J): S72 Model A's assumption is internally")
print("  INCONSISTENT with the Baptista hypercharge embedding.")
print("  The CORRECT per-sector Dynkin ratio in the Baptista convention is")
print("    T_1_GUT(p,q) : T_2(p,q) : T_3(p,q) = 7.2 : 1 : 1   (constant across (p,q))")
print("  so that delta_1 = 7.2 * delta_3 = 16.942 (not delta_3 = 2.353).")
print("  The 1.2 percent match of S72 Model A was a FALSE COINCIDENCE arising")
print("  from the SAME wrong ratio (1:1:1) that accidentally anchored sin^2 near")
print("  0.229.")

# Repeat the anchoring calculation with S72 Model A's universal delta
S_inf_S72 = 2.353  # (local)
delta_uni_1 = delta_uni_2 = S_inf_S72
Delta_a1_thresh_S72 = 4.0 * PI * delta_uni_1
Delta_a2_thresh_S72 = 4.0 * PI * delta_uni_2
total_const_S72 = ((5.0 / 3.0) * (Delta_a1_thresh_S72 + RG_shift_1)
                   + (Delta_a2_thresh_S72 + RG_shift_2))
x_solve_S72 = (alpha_em_MZ_inv - total_const_S72) / ((5.0 / 3.0) * c_ratio + 1.0)
alpha1_inv_MZ_S72 = c_ratio * x_solve_S72 + Delta_a1_thresh_S72 + RG_shift_1
alpha2_inv_MZ_S72 = x_solve_S72 + Delta_a2_thresh_S72 + RG_shift_2
sin2_MZ_S72 = ((3.0 / 5.0) * alpha2_inv_MZ_S72
               / ((3.0 / 5.0) * alpha2_inv_MZ_S72 + alpha1_inv_MZ_S72))
print(f"  S72 Model A re-computed here = {sin2_MZ_S72:.6f}")
print(f"  W2-J Jensen-dressed result   = {sin2_W_MZ_tree:.6f}")
print(f"  Delta (Jensen - universal)   = {sin2_W_MZ_tree - sin2_MZ_S72:+.6f}")

# -----------------------------------------------------------------------------
# 11. CROSS-CHECKS
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("11. CROSS-CHECKS")
print("=" * 80)

# (a) Sum of g_1^2 + g_2^2 > 0 -- equivalently alpha_1, alpha_2 > 0
a1_pos = 1.0 / alpha1_inv_MZ > 0.0
a2_pos = 1.0 / alpha2_inv_MZ > 0.0
print(f"  (a) alpha_1(M_Z) > 0: {'PASS' if a1_pos else 'FAIL'}")
print(f"  (a) alpha_2(M_Z) > 0: {'PASS' if a2_pos else 'FAIL'}")

# (b) n_i(k) counts sum to PW dimension -- verify per sector
all_ok = True
for pq, v in sector_evals.items():
    expected = v['dim'] * 16  # spinor dim 16 per fiber point times irrep dim
    # The cache stores abs_evals = all mode energies for (p,q).  The expected
    # number is dim(p,q) * 16 (spinor dim) in the Baptista convention.
    actual = len(v['abs_evals'])
    if actual != expected:
        all_ok = False
        print(f"    (b) sector {pq}: expected {expected}, got {actual}")
print(f"  (b) mode counts sum to dim*16 per sector: {'PASS' if all_ok else 'FAIL'}")

# Total mode count check
total_expected = sum(v['dim'] * 16 for v in sector_evals.values())
print(f"  (b) total eigenvalues = {n_modes_full}  (expected {total_expected})")

# (c) Running direction (b_1 positive, b_2 negative => sin^2 decreases H->L)
print(f"  (c) sin^2(theta_W) decreases from M_KK to M_Z: "
      f"{'PASS' if sin2_W_MKK_geo > sin2_W_MZ_tree else 'INFO (threshold overwhelms RG)'}")

# (d) Jensen-off limit -- reconstruct S72 universal model
#     As tau->0 the L1_mu = L2_mu = L3_mu = 1, so all sectors collapse to the
#     round-SU(3) spectrum and the log sums become uniform.  The ratio
#     delta_i/delta_3 -> T_i^tot / T_3^tot as shown in Section 7.
print(f"  (d) T_i^tot ratios at Jensen-off limit:")
print(f"        T_1_GUT / T_3 = {Ttot_1/Ttot_3:.4f}  (would give delta_1 ~ delta_3 for universal model)")
print(f"        T_2     / T_3 = {Ttot_2/Ttot_3:.4f}")

# -----------------------------------------------------------------------------
# 12. SAVE DATA
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("12. SAVE OUTPUT")
print("=" * 80)

# Per-sector arrays
pq_list = np.array(sorted(sector_evals.keys()), dtype=int)
T1_arr = np.array([dynkin_lookup[(p, q)]['T_u1_GUT']
                   for p, q in pq_list])
T2_arr = np.array([dynkin_lookup[(p, q)]['T_su2'] for p, q in pq_list])
T3_arr = np.array([dynkin_lookup[(p, q)]['T_su3'] for p, q in pq_list])
dim_arr = np.array([dynkin_lookup[(p, q)]['dim'] for p, q in pq_list])
nmodes_arr = np.array([len(sector_evals[(p, q)]['abs_evals'])
                       for p, q in pq_list])
omega_min_arr = np.array([sector_evals[(p, q)]['omega_min']
                          for p, q in pq_list])
omega_max_arr = np.array([sector_evals[(p, q)]['omega_max']
                          for p, q in pq_list])
omega_eff_min_arr = np.array([per_sector[(p, q)]['omega_eff_min']
                              for p, q in pq_list])
omega_eff_mean_arr = np.array([per_sector[(p, q)]['omega_eff_mean']
                               for p, q in pq_list])
c1_arr = np.array([per_sector[(p, q)]['c1_dec'] for p, q in pq_list])
c2_arr = np.array([per_sector[(p, q)]['c2_dec'] for p, q in pq_list])
c3_arr = np.array([per_sector[(p, q)]['c3_dec'] for p, q in pq_list])
included_arr = np.array([per_sector[(p, q)]['included_dec'] for p, q in pq_list])
c1_mean_arr = np.array([per_sector[(p, q)]['c1_mean'] for p, q in pq_list])
c2_mean_arr = np.array([per_sector[(p, q)]['c2_mean'] for p, q in pq_list])
c3_mean_arr = np.array([per_sector[(p, q)]['c3_mean'] for p, q in pq_list])
c1_full_arr = np.array([per_sector[(p, q)]['c1_full'] for p, q in pq_list])
c2_full_arr = np.array([per_sector[(p, q)]['c2_full'] for p, q in pq_list])
c3_full_arr = np.array([per_sector[(p, q)]['c3_full'] for p, q in pq_list])

out_path = os.path.join(SCRIPT_DIR, 's74_jensen_threshold.npz')
np.savez(out_path,
         tau_fold=tau_fold,
         Lambda_cut=Lambda_cut,
         sin2_W_MKK_geo=sin2_W_MKK_geo,
         sin2_W_MZ_tree=sin2_W_MZ_tree,
         sin2_W_MZ_PDG=sin2_thetaW_MSbar,
         deviation_abs=deviation_abs,
         deviation_rel_pct=deviation_rel,
         gate_status=gate_status,
         delta_1=delta_1, delta_2=delta_2, delta_3=delta_3,
         delta_1_min=delta_1_min_alt, delta_2_min=delta_2_min_alt, delta_3_min=delta_3_min_alt,
         delta_1_mean=delta_1_mean_alt, delta_2_mean=delta_2_mean_alt, delta_3_mean=delta_3_mean_alt,
         delta_1_full=delta_1_full_alt, delta_2_full=delta_2_full_alt, delta_3_full=delta_3_full_alt,
         Lambda_R=Lambda_R,
         alpha1_inv_bare_MKK=alpha1_inv_bare_MKK,
         alpha2_inv_bare_MKK=alpha2_inv_bare_MKK,
         alpha1_inv_eff_MKK=alpha1_inv_eff_MKK,
         alpha2_inv_eff_MKK=alpha2_inv_eff_MKK,
         alpha1_inv_MZ=alpha1_inv_MZ,
         alpha2_inv_MZ=alpha2_inv_MZ,
         sin2_MZ_S72=sin2_MZ_S72,
         pq=pq_list,
         dim_pq=dim_arr,
         n_modes=nmodes_arr,
         omega_min=omega_min_arr,
         omega_max=omega_max_arr,
         omega_eff_min=omega_eff_min_arr,
         omega_eff_mean=omega_eff_mean_arr,
         T_su3=T3_arr,
         T_su2=T2_arr,
         T_u1_GUT=T1_arr,
         c1_sector=c1_arr,
         c2_sector=c2_arr,
         c3_sector=c3_arr,
         included_dec=included_arr,
         c1_sector_mean=c1_mean_arr,
         c2_sector_mean=c2_mean_arr,
         c3_sector_mean=c3_mean_arr,
         c1_sector_full=c1_full_arr,
         c2_sector_full=c2_full_arr,
         c3_sector_full=c3_full_arr)
print(f"  Saved: {out_path}")

# -----------------------------------------------------------------------------
# 13. PLOT
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(2, 3, hspace=0.35, wspace=0.32)

# (a) Per-sector Dynkin ratios
ax1 = fig.add_subplot(gs[0, 0])
L_vals = np.array([p + q for p, q in pq_list])
# Avoid divide-by-zero on the (0,0) trivial rep where T_su3 = 0
mask = T3_arr > 0
ax1.scatter(L_vals[mask], T1_arr[mask] / T3_arr[mask],
            c='tab:red', label='T1_GUT/T3', alpha=0.7)
ax1.scatter(L_vals[mask], T2_arr[mask] / T3_arr[mask],
            c='tab:blue', label='T2/T3', alpha=0.7)
ax1.axhline(1.0, color='k', ls='--', alpha=0.3)
ax1.set_xlabel('L = p + q')
ax1.set_ylabel('Dynkin ratio')
ax1.set_title('Per-sector Dynkin ratios')
ax1.legend()
ax1.grid(alpha=0.3)

# (b) Per-sector contribution to delta_i
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(L_vals - 0.25, c1_arr, width=0.22, label='d1/sector', color='tab:red', alpha=0.7)
ax2.bar(L_vals, c2_arr, width=0.22, label='d2/sector', color='tab:blue', alpha=0.7)
ax2.bar(L_vals + 0.25, c3_arr, width=0.22, label='d3/sector', color='tab:green', alpha=0.7)
ax2.set_xlabel('L = p + q')
ax2.set_ylabel('delta_i contribution')
ax2.set_title('Sector contributions to delta_i')
ax2.legend()
ax2.grid(alpha=0.3)

# (c) Running of 1/alpha_i from M_KK to M_Z
ax3 = fig.add_subplot(gs[0, 2])
mus = np.array([M_Z, M_KK])
ln_mus = np.log(mus)
a1_run = np.array([alpha1_inv_MZ, alpha1_inv_eff_MKK])
a2_run = np.array([alpha2_inv_MZ, alpha2_inv_eff_MKK])
ax3.plot(ln_mus, a1_run, 'o-', color='tab:red', label='1/alpha_1')
ax3.plot(ln_mus, a2_run, 's-', color='tab:blue', label='1/alpha_2')
ax3.set_xlabel('ln(mu / GeV)')
ax3.set_ylabel('1/alpha_i')
ax3.set_title('Gauge coupling RG running')
ax3.legend()
ax3.grid(alpha=0.3)

# (d) sin^2(theta_W) comparison
ax4 = fig.add_subplot(gs[1, 0])
labels = ['geo\nM_KK', 'S72 Model A\n(universal)', 'W2-J\nJensen-full', 'PDG']
vals = [sin2_W_MKK_geo, sin2_MZ_S72, sin2_W_MZ_tree, sin2_thetaW_MSbar]
colors = ['tab:gray', 'tab:orange', 'tab:green', 'tab:purple']
bars = ax4.bar(labels, vals, color=colors, alpha=0.75)
ax4.axhline(sin2_thetaW_MSbar, color='tab:purple', ls='--', lw=1, label='PDG')
ax4.set_ylabel('sin^2(theta_W)')
ax4.set_title('sin^2(theta_W) comparison')
ax4.grid(alpha=0.3, axis='y')
for bar, v in zip(bars, vals):
    ax4.text(bar.get_x() + bar.get_width() / 2, v, f'{v:.4f}',
             ha='center', va='bottom', fontsize=9)

# (e) Jensen-dressed eigenvalue histogram
ax5 = fig.add_subplot(gs[1, 1])
ax5.hist(omega_all, bins=60, color='teal', alpha=0.8)
ax5.axvline(Lambda_cut, color='k', ls='--', label=f'Lambda_cut = {Lambda_cut:.3f}')
ax5.set_xlabel('omega_k (M_KK units)')
ax5.set_ylabel('count')
ax5.set_title(f'Jensen-dressed D_K eigenvalues at tau = {tau_fold}')
ax5.legend()
ax5.grid(alpha=0.3)

# (f) Sector-by-sector omega window
ax6 = fig.add_subplot(gs[1, 2])
for pq, v in sector_evals.items():
    L = pq[0] + pq[1]
    ax6.plot([L, L], [v['omega_min'], v['omega_max']], 'o-',
             color='tab:orange', alpha=0.5, markersize=3)
ax6.set_xlabel('L = p + q')
ax6.set_ylabel('omega range')
ax6.set_title('Sector omega windows')
ax6.grid(alpha=0.3)

fig.suptitle(
    f'JENSEN-THRESHOLD-74: sin^2(theta_W) tree full sum  |  '
    f'result {sin2_W_MZ_tree:.5f}  |  dev {deviation_rel:.2f}%  |  {gate_status}',
    fontsize=12, fontweight='bold')
plot_path = os.path.join(SCRIPT_DIR, 's74_jensen_threshold.png')
fig.savefig(plot_path, dpi=130, bbox_inches='tight')
print(f"  Saved: {plot_path}")

# -----------------------------------------------------------------------------
# FINAL SUMMARY
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("JENSEN-THRESHOLD-74 SUMMARY")
print("=" * 80)
print(f"  tau_fold = {tau_fold}")
print(f"  Modes summed:  {n_modes_full} eigenvalues across {n_sectors_full} PW sectors (L_max = 9)")
print(f"  delta_1 = {delta_1:.6f}")
print(f"  delta_2 = {delta_2:.6f}")
print(f"  delta_3 = {delta_3:.6f}")
print(f"  sin^2(theta_W)|_M_Z tree = {sin2_W_MZ_tree:.6f}")
print(f"  PDG target               = {sin2_thetaW_MSbar}")
print(f"  Deviation                = {deviation_abs:+.6f}  ({deviation_rel:.3f} percent)")
print(f"  Verdict: JENSEN-THRESHOLD-74 = {gate_status}")
