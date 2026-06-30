#!/usr/bin/env python3
"""
s63_kk_threshold.py — KK-THRESHOLD-63
KK threshold corrections to gauge coupling g_3 at M_KK from PW tower.

Physics
-------
The CCM spectral action on M4 x SU(3) sets gauge couplings at the UV cutoff
Lambda via:
    1/g^2 = f_0 * (a_4 / pi^2)

where a_4 receives contributions from ALL Peter-Weyl sectors (p,q) up to
the spectral cutoff. When matching to the 4D effective theory at M_KK,
the KK modes (p,q) != (0,0) are integrated out, producing a finite
threshold correction:

    delta(1/g_3^2) = (1/(8*pi^2)) * SUM_{(p,q)!=(0,0)} T(p,q) * ln(Lambda^2 / M_{(p,q)}^2)

where:
    T(p,q) = dim(p,q) * C_2(p,q) / (2 * dim(adj))  [convention T(fund)=1/2]
           = dim(p,q) * C_2(p,q) / 8                  [for SU(3)]
    M_{(p,q)} = omega_min(p,q) * M_KK                  [lowest D_K eigenvalue in sector]
    Lambda = spectral action cutoff (set by gamma_opt)

S62 found delta(1/g_3^2) = 1.41 at L=3 truncation, sitting at the upper
boundary of the PASS band [0.73, 1.48]. The critical question is convergence
as L increases to 6.

The concern: T(p,q) grows as ~L^7 per sector with ~L^2 sectors per level,
giving total T ~ L^9. The logarithm only grows as ln(L). So the sum may
diverge, making the L=3 result an artifact of premature truncation.

Gate: KK-THRESHOLD-63
    PASS if delta(1/g_3^2) in [0.73, 1.48] for BOTH L=6 sharp AND Gaussian.
    FAIL if diverges (ratio L=6/L=5 > 2).
    INFO if converges but outside PASS band.

Method
------
1. Load PW sector data from s60_pw_h0_conv.npz (eigenvalues at fold)
2. For each (p,q) with p+q <= 6, compute T(p,q), M_{(p,q)}
3. Compute threshold at each truncation L = 1,...,6
4. Also compute Gaussian-regulated version: weight each term by
   exp(-M_{(p,q)}^2/Lambda^2)
5. Test both f_0 matching: alpha_GUT = 1/25 and 1/10.8
6. Propagate to m_H prediction using S62 RGE machinery

Author: baptista-spacetime-analyst
Session: S63 W1-02
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

from canonical_constants import (
    PI, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Z, M_W,
    alpha_em_MZ_inv, sin2_thetaW_MSbar,
    a0_fold, a2_fold, a4_fold,
    tau_fold, Vol_SU3_Haar,
)

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 76)
print("KK-THRESHOLD-63: KK Threshold Corrections to g_3 from PW Tower (L=6)")
print("=" * 76)

# =============================================================================
# 1. SU(3) REPRESENTATION THEORY
# =============================================================================
print("\n" + "=" * 76)
print("1. SU(3) REPRESENTATION THEORY")
print("=" * 76)

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q): (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def C2_su3(p, q):
    """Quadratic Casimir of SU(3) irrep (p,q).
    C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q) / 3.
    Normalization: C_2(1,0) = 4/3, C_2(1,1) = 3 (adjoint)."""
    return (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0

def T_su3(p, q):
    """Dynkin index T(p,q) of SU(3) irrep.
    Convention: T(fund) = T(1,0) = 1/2.
    Formula: T(R) = dim(R) * C_2(R) / (2 * dim(G)) = dim(R) * C_2(R) / 16
    But the STANDARD formula for SU(N) is:
        T(R) * delta^{ab} = Tr(T^a_R T^b_R)
        T(R) = dim(R) * C_2(R) / dim(adj)
    For SU(3): dim(adj) = 8, so T(R) = dim(R) * C_2(R) / 8.
    Check: T(1,0) = 3 * (4/3) / 8 = 1/2. Correct.
    Check: T(1,1) = 8 * 3 / 8 = 3. Correct (adjoint Dynkin index = N = 3)."""
    d = dim_su3(p, q)
    c2 = C2_su3(p, q)
    return d * c2 / 8.0

# Verify key values
print(f"  Verification:")
print(f"    dim(1,0) = {dim_su3(1,0)}, C_2(1,0) = {C2_su3(1,0):.4f}, T(1,0) = {T_su3(1,0):.4f}")
print(f"    dim(1,1) = {dim_su3(1,1)}, C_2(1,1) = {C2_su3(1,1):.4f}, T(1,1) = {T_su3(1,1):.4f}")
print(f"    dim(2,0) = {dim_su3(2,0)}, C_2(2,0) = {C2_su3(2,0):.4f}, T(2,0) = {T_su3(2,0):.4f}")
print(f"    dim(2,1) = {dim_su3(2,1)}, C_2(2,1) = {C2_su3(2,1):.4f}, T(2,1) = {T_su3(2,1):.4f}")

# =============================================================================
# 2. LOAD PW EIGENVALUE DATA
# =============================================================================
print("\n" + "=" * 76)
print("2. PW EIGENVALUE DATA FROM S60")
print("=" * 76)

d60 = np.load(os.path.join(outdir, 's60_pw_h0_conv.npz'), allow_pickle=True)

irrep_pq = d60['irrep_pq']       # (N_irreps, 2)
irrep_dim = d60['irrep_dim']     # dimension of each irrep
irrep_level = d60['irrep_level'] # L = p + q
irrep_omega_min = d60['irrep_omega_min']  # lowest |D_K| eigenvalue in sector
irrep_omega_max = d60['irrep_omega_max']  # highest |D_K| eigenvalue in sector

n_irreps = len(irrep_dim)
print(f"  Total irreps loaded: {n_irreps} (up to L={irrep_level.max()})")

# Build sector table for L = 0..6
# Each sector (p,q) has:
#   - dim(p,q): dimension of the representation
#   - C_2(p,q): quadratic Casimir
#   - T(p,q): Dynkin index
#   - M_{(p,q)}: mass of lowest KK mode = omega_min * M_KK
#   - omega_min, omega_max: D_K eigenvalue range (in M_KK units)

print(f"\n  PW sector table:")
print(f"  {'(p,q)':>6} {'dim':>5} {'L':>3} {'C_2':>8} {'T':>10} "
      f"{'omega_min':>10} {'omega_max':>10} {'M_KK/M':>10}")

sectors = []
for i in range(n_irreps):
    p, q = irrep_pq[i]
    L = irrep_level[i]
    if L > 6:
        continue
    d = int(irrep_dim[i])
    c2 = C2_su3(p, q)
    T = T_su3(p, q)
    om_min = irrep_omega_min[i]
    om_max = irrep_omega_max[i]

    sectors.append({
        'p': p, 'q': q, 'dim': d, 'level': L,
        'C2': c2, 'T': T,
        'omega_min': om_min, 'omega_max': om_max,
    })

    # M_{(p,q)} / M_KK = omega_min for the lightest mode
    ratio = 1.0 / om_min if om_min > 0 else np.inf
    print(f"  ({p},{q}){'':<2} {d:5d} {L:3d} {c2:8.4f} {T:10.4f} "
          f"{om_min:10.4f} {om_max:10.4f} {ratio:10.4f}")

# =============================================================================
# 3. THRESHOLD CORRECTION: SHARP CUTOFF
# =============================================================================
print("\n" + "=" * 76)
print("3. THRESHOLD CORRECTION: SHARP CUTOFF")
print("=" * 76)

# The threshold correction to 1/g_3^2 at the matching scale M_match from
# integrating out KK modes:
#
#   delta(1/g_3^2) = (1/(8*pi^2)) * SUM_{(p,q)!=(0,0)} T(p,q)
#                    * ln(Lambda^2 / M_{(p,q)}^2)
#
# where Lambda is the UV cutoff (spectral action scale) and
# M_{(p,q)} = omega_min(p,q) * M_KK is the lowest KK mass in sector (p,q).
#
# The omega values are D_K eigenvalues in M_KK units. The spectral action
# cutoff Lambda (in M_KK units) is set by gamma_opt from s62_cutoff_london.

# Load cutoff data
d62c = np.load(os.path.join(outdir, 's62_cutoff_london.npz'), allow_pickle=True)
gamma_opt = float(d62c['Gaussian_gamma_opt'])
f0_alpha25 = float(d62c['f0_for_alpha25'])
# The spectral action is S = Tr(f(D^2/Lambda^2)), so Lambda is in D_K eigenvalue
# units. From the Gaussian optimization, gamma = Lambda_phys / Lambda_eigen.
# But more precisely: the D_K eigenvalues omega are already in M_KK units,
# and the cutoff Lambda_eigen is in those same units.
# From s61: the max eigenvalue at L=6 is Lambda_max[6] = 2.784 (M_KK units)
d61 = np.load(os.path.join(outdir, 's61_trace_formula_geometric.npz'), allow_pickle=True)
Lambda_max_by_L = d61['Lambda_max']  # Lambda_max at each L

print(f"  Gaussian gamma_opt = {gamma_opt:.4f}")
print(f"  f_0 (alpha_GUT = 1/25) = {f0_alpha25:.4f}")
print(f"  Lambda_max by L: {Lambda_max_by_L}")

# For the threshold correction, Lambda is the FULL spectral cutoff.
# In the spectral action framework, all modes with omega < Lambda contribute.
# The "matching" to the 4D theory happens at M_KK (= 1 in these units).
#
# So the log factor is:
#   ln(Lambda^2 / M_{(p,q)}^2) = ln(Lambda^2 / omega_min^2)
#
# where Lambda is the spectral cutoff in M_KK units. We'll use two choices:
#   (a) Lambda = Lambda_max(L) -- the maximum eigenvalue at truncation level L
#   (b) Lambda = 1/gamma_opt -- from the Gaussian optimization
#
# For the Gaussian-regulated sum, the cutoff IS the regulation, so Lambda
# doesn't appear explicitly; instead we have:
#   delta_Gauss = (1/(8pi^2)) * SUM T(p,q) * exp(-omega_min^2/Lambda^2)
#                 * ln(Lambda^2/omega_min^2)

# Physical reasoning for Lambda:
# The spectral action cutoff Lambda sets where new physics enters.
# In our framework, Lambda^2 is the scale^2 in f(D^2/Lambda^2).
# The D_K eigenvalue omega is in M_KK units (omega * M_KK = mass in GeV).
# The spectral cutoff should be Lambda ~ a few M_KK (the scale of the
# highest modes we trust).
#
# From s61 trace formula: the eigenvalue spectrum extends to Lambda_max(L).
# But the physical cutoff is set by the Seeley-DeWitt expansion, not by
# the truncation. The Gaussian optimization found gamma_opt = 0.488,
# which means Lambda_eff ~ 1/gamma_opt ~ 2.05 in M_KK units.
#
# We'll compute BOTH: (a) Lambda = Lambda_max(L) [L-dependent], (b) Lambda = 1/gamma_opt [fixed].

Lambda_fixed = 1.0 / gamma_opt  # ~ 2.05 M_KK
print(f"  Lambda_fixed = 1/gamma_opt = {Lambda_fixed:.4f} M_KK")

# Also: internal matching. alpha_GUT = 1/25 gives f_0 = 9.82.
# The spectral action: 1/g^2 = f_0 * (a_4/pi^2).
# At the matching scale, the threshold correction shifts this.
#
# The target: delta(1/g_3^2) must be in [0.73, 1.48] to bring
# m_H from 190 GeV down to ~125 GeV.

# Compute threshold at each truncation level L = 1, ..., 6
L_range = np.arange(1, 7)  # L = 1 to 6

delta_g3_inv_sharp_Lmax = np.zeros(len(L_range))    # Lambda = Lambda_max(L)
delta_g3_inv_sharp_fixed = np.zeros(len(L_range))    # Lambda = Lambda_fixed
delta_g3_inv_gauss_fixed = np.zeros(len(L_range))    # Gaussian with Lambda_fixed
delta_g3_inv_gauss_Lmax = np.zeros(len(L_range))     # Gaussian with Lambda_max(L)
total_T_by_L = np.zeros(len(L_range))
n_sectors_by_L = np.zeros(len(L_range), dtype=int)

# Store per-sector contributions for analysis
sector_contributions = []

print(f"\n  Per-sector contributions (sharp, Lambda = Lambda_fixed):")
print(f"  {'(p,q)':>6} {'T(p,q)':>10} {'omega_min':>10} "
      f"{'ln(L^2/M^2)':>12} {'contribution':>14} {'cumul_delta':>14}")

cumul = 0.0
for sec in sectors:
    p, q = sec['p'], sec['q']
    L = sec['level']
    T = sec['T']
    om = sec['omega_min']

    if p == 0 and q == 0:
        # Skip zero mode
        sec['contrib_sharp_fixed'] = 0.0
        sec['contrib_gauss_fixed'] = 0.0
        sector_contributions.append(sec)
        continue

    # Sharp cutoff with Lambda_fixed
    log_ratio_fixed = np.log(Lambda_fixed**2 / om**2)
    contrib_sharp_fixed = T * log_ratio_fixed / (8.0 * PI**2)
    sec['contrib_sharp_fixed'] = contrib_sharp_fixed
    cumul += contrib_sharp_fixed

    # Gaussian-regulated with Lambda_fixed
    gauss_weight = np.exp(-om**2 / Lambda_fixed**2)
    contrib_gauss_fixed = T * gauss_weight * log_ratio_fixed / (8.0 * PI**2)
    sec['contrib_gauss_fixed'] = contrib_gauss_fixed

    sector_contributions.append(sec)

    print(f"  ({p},{q}){'':<2} {T:10.4f} {om:10.4f} "
          f"{log_ratio_fixed:12.4f} {contrib_sharp_fixed:14.6f} {cumul:14.6f}")

# Now compute cumulative sums at each L
for iL, L_val in enumerate(L_range):
    T_sum = 0.0  # (local)
    delta_sharp_Lmax = 0.0  # (local)
    delta_sharp_fixed = 0.0  # (local)
    delta_gauss_fixed = 0.0  # (local)
    delta_gauss_Lmax = 0.0  # (local)
    n_sec = 0  # (local)

    Lambda_L = Lambda_max_by_L[L_val] if L_val < len(Lambda_max_by_L) else Lambda_max_by_L[-1]

    for sec in sector_contributions:
        p, q = sec['p'], sec['q']
        if sec['level'] > L_val or (p == 0 and q == 0):
            continue

        T = sec['T']
        om = sec['omega_min']
        T_sum += T
        n_sec += 1

        # Sharp with Lambda_max(L)
        log_Lmax = np.log(Lambda_L**2 / om**2)
        delta_sharp_Lmax += T * log_Lmax / (8.0 * PI**2)

        # Sharp with Lambda_fixed
        log_fixed = np.log(Lambda_fixed**2 / om**2)
        delta_sharp_fixed += T * log_fixed / (8.0 * PI**2)

        # Gaussian with Lambda_fixed
        gw = np.exp(-om**2 / Lambda_fixed**2)
        delta_gauss_fixed += T * gw * log_fixed / (8.0 * PI**2)

        # Gaussian with Lambda_max(L)
        gw_L = np.exp(-om**2 / Lambda_L**2)
        delta_gauss_Lmax += T * gw_L * log_Lmax / (8.0 * PI**2)

    delta_g3_inv_sharp_Lmax[iL] = delta_sharp_Lmax
    delta_g3_inv_sharp_fixed[iL] = delta_sharp_fixed
    delta_g3_inv_gauss_fixed[iL] = delta_gauss_fixed
    delta_g3_inv_gauss_Lmax[iL] = delta_gauss_Lmax
    total_T_by_L[iL] = T_sum
    n_sectors_by_L[iL] = n_sec

print(f"\n\n  Threshold correction by truncation level L:")
print(f"  {'L':>3} {'N_sec':>6} {'T_total':>10} "
      f"{'d(1/g3^2)_Lmax':>16} {'d(1/g3^2)_fix':>16} "
      f"{'d(1/g3^2)_G_fix':>16} {'d(1/g3^2)_G_Lm':>16}")

for iL, L_val in enumerate(L_range):
    print(f"  {L_val:3d} {n_sectors_by_L[iL]:6d} {total_T_by_L[iL]:10.2f} "
          f"{delta_g3_inv_sharp_Lmax[iL]:16.6f} {delta_g3_inv_sharp_fixed[iL]:16.6f} "
          f"{delta_g3_inv_gauss_fixed[iL]:16.6f} {delta_g3_inv_gauss_Lmax[iL]:16.6f}")

# =============================================================================
# 4. CONVERGENCE ANALYSIS
# =============================================================================
print("\n" + "=" * 76)
print("4. CONVERGENCE ANALYSIS")
print("=" * 76)

# Compute ratios between consecutive levels
print(f"\n  Successive ratios delta(L)/delta(L-1):")
print(f"  {'L':>3} {'sharp_Lmax':>12} {'sharp_fix':>12} {'gauss_fix':>12} {'gauss_Lmax':>12}")

conv_ratio_sharp_Lmax = np.zeros(len(L_range) - 1)
conv_ratio_sharp_fixed = np.zeros(len(L_range) - 1)
conv_ratio_gauss_fixed = np.zeros(len(L_range) - 1)
conv_ratio_gauss_Lmax = np.zeros(len(L_range) - 1)

for iL in range(1, len(L_range)):
    r_sL = delta_g3_inv_sharp_Lmax[iL] / delta_g3_inv_sharp_Lmax[iL-1] if delta_g3_inv_sharp_Lmax[iL-1] != 0 else np.inf
    r_sf = delta_g3_inv_sharp_fixed[iL] / delta_g3_inv_sharp_fixed[iL-1] if delta_g3_inv_sharp_fixed[iL-1] != 0 else np.inf
    r_gf = delta_g3_inv_gauss_fixed[iL] / delta_g3_inv_gauss_fixed[iL-1] if delta_g3_inv_gauss_fixed[iL-1] != 0 else np.inf
    r_gL = delta_g3_inv_gauss_Lmax[iL] / delta_g3_inv_gauss_Lmax[iL-1] if delta_g3_inv_gauss_Lmax[iL-1] != 0 else np.inf
    conv_ratio_sharp_Lmax[iL-1] = r_sL
    conv_ratio_sharp_fixed[iL-1] = r_sf
    conv_ratio_gauss_fixed[iL-1] = r_gf
    conv_ratio_gauss_Lmax[iL-1] = r_gL
    print(f"  {L_range[iL]:3d} {r_sL:12.4f} {r_sf:12.4f} {r_gf:12.4f} {r_gL:12.4f}")

# Growth analysis: fit power law delta(L) ~ L^alpha
# Use log-log fit
for name, arr in [('sharp_Lmax', delta_g3_inv_sharp_Lmax),
                  ('sharp_fixed', delta_g3_inv_sharp_fixed),
                  ('gauss_fixed', delta_g3_inv_gauss_fixed),
                  ('gauss_Lmax', delta_g3_inv_gauss_Lmax)]:
    # Log-log fit over L = 2..6 (skip L=1 which may not be representative)
    mask = L_range >= 2
    x = np.log(L_range[mask].astype(float))
    y = np.log(np.abs(arr[mask]))
    if len(x) > 1 and np.all(np.isfinite(y)):
        coeffs = np.polyfit(x, y, 1)
        print(f"  Growth fit {name}: delta ~ L^{coeffs[0]:.2f}")
    else:
        print(f"  Growth fit {name}: cannot fit (non-finite values)")

# =============================================================================
# 5. DYNKIN INDEX SCALING ANALYSIS
# =============================================================================
print("\n" + "=" * 76)
print("5. DYNKIN INDEX SCALING")
print("=" * 76)

# The total Dynkin index at each level scales as:
# sum_{p+q=L} T(p,q) = sum_{p+q=L} dim(p,q) * C_2(p,q) / 8
# At level L: dim(p,q) ~ L^2, C_2(p,q) ~ L^2, and there are L+1 sectors.
# So T_total(L) ~ L^5 per level, and cumulative ~ L^6.
# But the threshold log only grows as ln(L). So the sharp sum grows as ~L^6.

# Let's compute the per-LEVEL contribution (not cumulative)
print(f"\n  Per-level Dynkin index and threshold contribution:")
print(f"  {'L':>3} {'T(level)':>12} {'T(cumul)':>12} "
      f"{'delta(level)':>14} {'delta(cumul)':>14}")

for iL, L_val in enumerate(L_range):
    T_level = 0.0  # (local)
    delta_level = 0.0  # (local)
    for sec in sector_contributions:
        if sec['level'] == L_val and not (sec['p'] == 0 and sec['q'] == 0):
            T_level += sec['T']
            delta_level += sec['contrib_sharp_fixed']

    T_cumul = total_T_by_L[iL]
    delta_cumul = delta_g3_inv_sharp_fixed[iL]
    print(f"  {L_val:3d} {T_level:12.2f} {T_cumul:12.2f} "
          f"{delta_level:14.6f} {delta_cumul:14.6f}")

# =============================================================================
# 6. PHYSICAL INTERPRETATION: IMPACT ON HIGGS MASS
# =============================================================================
print("\n" + "=" * 76)
print("6. IMPACT ON HIGGS MASS")
print("=" * 76)

# Load S62 Higgs mass data
d62h = np.load(os.path.join(outdir, 's62_higgs_bcs_threshold.npz'), allow_pickle=True)
g3_MKK_nominal = float(d62h['g3_MKK_nominal'])     # g_3(M_KK) from SM running up = 0.5161
ratio_gilkey = float(d62h['ratio_gilkey'])           # a_4/a_2 = 0.414
lambda_CCM = float(d62h['lambda_CCM_MKK'])           # (4/3) * g3^2 * ratio = 0.147
m_H_2loop_noBCS = float(d62h['m_H_2loop_noBCS'])    # 190.1 GeV
v_ew = 246.22  # GeV  # S72: intentionally differs from canonical v_ew=246.0 (Fermi-extracted)

# The threshold correction shifts g_3^{-2} at M_KK:
#   1/g_3^2(M_KK)_eff = 1/g_3^2(M_KK)_nominal + delta(1/g_3^2)
# This increases 1/g_3^2 (weakens the coupling), which reduces lambda_CCM
# and thereby reduces m_H.

g3_inv2_nominal = 1.0 / g3_MKK_nominal**2
print(f"  g_3(M_KK) nominal = {g3_MKK_nominal:.6f}")
print(f"  1/g_3^2 nominal = {g3_inv2_nominal:.6f}")

# For each L and each method, compute effective g_3 and m_H
# We need the full 2-loop RGE from S62 to get m_H. Import it.

# Physical constants
# m_H_obs = 125.10  # S72: now imported from canonical_constants
# m_t_pole = 172.69  # S72: now imported from canonical_constants
# alpha_s_MZ = 0.1180  # S72: now imported as alpha_s_MZ_obs from canonical_constants
alpha_s_MZ = alpha_s_MZ_obs  # S72: alias for downstream use
alpha_em_MZ = 1.0 / alpha_em_MZ_inv
sin2_tW = sin2_thetaW_MSbar
g1_MZ = np.sqrt(5.0/3.0) * np.sqrt(4 * PI * alpha_em_MZ / (1 - sin2_tW))
g2_MZ = np.sqrt(4 * PI * alpha_em_MZ / sin2_tW)
g3_MZ = np.sqrt(4 * PI * alpha_s_MZ)
m_t_MSbar = m_t_pole * (1.0 - 4.0 * alpha_s_MZ / (3.0 * PI))
yt_MZ = np.sqrt(2) * m_t_MSbar / v_ew
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)

t_MKK = np.log(M_KK_gravity / M_Z)

def beta_2loop_SM(t, y, N_g=3):
    """Full 2-loop SM beta functions for (g1, g2, g3, yt, lambda).
    Copied from s62_higgs_bcs_threshold.py for self-consistency."""
    g1, g2, g3, yt, lam = y
    g1sq = g1**2
    g2sq = g2**2
    g3sq = g3**2
    ytsq = yt**2
    lamsq = lam**2
    b16pi2 = 16.0 * PI**2
    b16pi2_sq = b16pi2**2

    b1_1 = 41.0 / 10.0
    b2_1 = -19.0 / 6.0
    b3_1 = -7.0  # (local)
    beta_g1_1 = b1_1 * g1**3 / b16pi2
    beta_g2_1 = b2_1 * g2**3 / b16pi2
    beta_g3_1 = b3_1 * g3**3 / b16pi2

    beta_g1_2 = g1**3 / b16pi2_sq * (
        199.0/50.0 * g1sq + 27.0/10.0 * g2sq + 44.0/5.0 * g3sq - 17.0/10.0 * ytsq)
    beta_g2_2 = g2**3 / b16pi2_sq * (
        9.0/10.0 * g1sq + 35.0/6.0 * g2sq + 12.0 * g3sq - 3.0/2.0 * ytsq)
    beta_g3_2 = g3**3 / b16pi2_sq * (
        11.0/10.0 * g1sq + 9.0/2.0 * g2sq - 26.0 * g3sq - 2.0 * ytsq)

    dg1 = beta_g1_1 + beta_g1_2
    dg2 = beta_g2_1 + beta_g2_2
    dg3 = beta_g3_1 + beta_g3_2

    beta_yt_1 = yt / b16pi2 * (
        9.0/2.0 * ytsq - 17.0/20.0 * g1sq - 9.0/4.0 * g2sq - 8.0 * g3sq)
    beta_yt_2 = yt / b16pi2_sq * (
        - 12.0 * ytsq**2
        + ytsq * (393.0/80.0 * g1sq + 225.0/16.0 * g2sq + 36.0 * g3sq)
        + 1187.0/600.0 * g1sq**2 - 9.0/20.0 * g1sq * g2sq
        + 19.0/15.0 * g1sq * g3sq - 23.0/4.0 * g2sq**2
        + 9.0 * g2sq * g3sq - 108.0 * g3sq**2
        + 6.0 * lam**2 - 3.0/2.0 * lam * ytsq)
    dyt = beta_yt_1 + beta_yt_2

    beta_lam_1 = (1.0 / b16pi2) * (
        24.0 * lamsq
        + 12.0 * lam * ytsq - 12.0 * ytsq**2
        - 3.0 * lam * (3.0/5.0 * g1sq + 3.0 * g2sq)
        + 3.0/8.0 * (3.0/25.0 * g1sq**2 + 6.0/5.0 * g1sq * g2sq + 3.0 * g2sq**2))
    beta_lam_2 = (1.0 / b16pi2_sq) * (
        - 312.0 * lam**3
        + lamsq * (-144.0 * ytsq)
        + lam * ytsq * (
            -3.0 * ytsq + 80.0 * g3sq
            + 45.0/2.0 * g2sq + 85.0/6.0 * (3.0/5.0) * g1sq)
        + 60.0 * ytsq**3 - 16.0 * ytsq**2 * g3sq
        + lam * (108.0/5.0 * (3.0/25.0) * g1sq**2
                  + 36.0 * (3.0/5.0 * g1sq * g2sq) / 5.0
                  - 73.0/8.0 * g2sq**2)
        - 3.0/5.0 * g1sq * (-57.0/10.0 * g2sq * g1sq + 12.0 * ytsq**2) / 2.0
        + g2sq * (-289.0/8.0 * g2sq**2 / 4.0))
    dlam = beta_lam_1 + beta_lam_2
    return [dg1, dg2, dg3, dyt, dlam]

# Run SM couplings UP from M_Z to M_KK (same as S62)
y0_up = [g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs]
sol_up = solve_ivp(
    beta_2loop_SM, [0, t_MKK], y0_up,
    t_eval=np.linspace(0, t_MKK, 3000),
    method='RK45', rtol=1e-12, atol=1e-14
)
g1_at_MKK = sol_up.y[0, -1]
g2_at_MKK = sol_up.y[1, -1]
g3_at_MKK = sol_up.y[2, -1]
yt_at_MKK = sol_up.y[3, -1]

print(f"  SM couplings at M_KK (from 2-loop upward run):")
print(f"    g_1 = {g1_at_MKK:.6f}, g_2 = {g2_at_MKK:.6f}, g_3 = {g3_at_MKK:.6f}")
print(f"    y_t = {yt_at_MKK:.6f}")

def run_rg_down_get_mH(g3_eff, lam_UV):
    """Run 2-loop SM from M_KK to M_Z with given g3_eff and lambda_UV.
    Returns m_H at M_Z."""
    y0 = [g1_at_MKK, g2_at_MKK, g3_eff, yt_at_MKK, lam_UV]
    sol = solve_ivp(
        beta_2loop_SM, [t_MKK, 0], y0,
        t_eval=np.linspace(t_MKK, 0, 2000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    if not sol.success:
        return np.nan
    lam_IR = sol.y[4, -1]
    if lam_IR > 0:
        return np.sqrt(2.0 * lam_IR) * v_ew
    else:
        return 0.0

# Compute m_H for each threshold correction at each L
# Two f_0 matching procedures:
# (a) f_0 = 9.82 (alpha_GUT = 1/25, external)
# (b) f_0 = 4.26 (alpha_GUT = 1/10.8, internal)
# The threshold correction modifies g_3^{-2} at M_KK.
# The CCM spectral action sets:
#   1/g_3^2 = f_0 * a_4 / pi^2
# The threshold shifts this:
#   1/g_3^2(eff) = 1/g_3^2(bare) + delta(1/g_3^2)
# equivalently:
#   g_3^2(eff) = 1 / (1/g_3^2(bare) + delta)

# For matching (a): f_0 = 9.82, alpha_GUT = pi / (2 * f_0) = pi / 19.64 = 0.160
# This gives g^2 = 4*pi*alpha_GUT = 4*pi*0.04 = 0.503. But the SM running
# gives g_3(M_KK) = 0.516, so there's a small mismatch.
#
# The MATCHING PROCEDURE: at M_KK, the spectral action coupling g_3^{bare}
# equals the SM running coupling, modulo the threshold correction.
# The threshold correction is a shift: 1/g_3^2(SM, M_KK) = 1/g_3^2(bare) + delta.
# So g_3^2(bare) = 1/(1/g_3^2(SM) - delta) if we're computing delta FROM the SA,
# OR g_3^2(eff, 4D) = 1/(1/g_3^2(SA, bare) + delta) if we're modifying the SA.
#
# We want: what is the effective g_3 at M_KK AFTER threshold correction?
# The SA gives g_3^2(bare) at the cutoff. Matching to 4D at M_KK:
#   1/g_3^2(4D, M_KK) = 1/g_3^2(SA, bare) + delta(1/g_3^2)
#
# Since delta > 0 (KK modes strengthen the coupling at the cutoff, and
# integrating them out reduces the 4D coupling), the effective 4D coupling
# is WEAKER (larger 1/g^2).
#
# Actually, let me be more careful about the SIGN.
# The one-loop KK threshold correction to the 4D coupling comes from
# integrating out heavy modes. For a gauge boson loop:
#   delta(1/g_a^2) = b_KK * ln(M_KK^2/mu^2) [standard heavy-particle decoupling]
# But for the KK tower, each mode at mass M_n gives:
#   delta(1/g_3^2) = -(1/(8pi^2)) * SUM T_n * ln(M_n^2/Lambda^2)
#                   = (1/(8pi^2)) * SUM T_n * ln(Lambda^2/M_n^2)
# This is POSITIVE when M_n < Lambda (modes below the cutoff).
# Positive delta(1/g_3^2) means the 4D coupling is WEAKER = higher 1/g^2.
# A weaker g_3 at M_KK -> smaller lambda_CCM -> smaller m_H. This is the
# CORRECT direction to bring m_H from 190 down toward 125.

# But we also need to check: the spectral action ALREADY includes these modes.
# The SA coefficient a_4 = sum over ALL modes. So the "bare" SA coupling
# already has the KK contributions. The threshold correction in the standard
# sense is the DIFFERENCE between the SA (which includes all modes) and
# the 4D theory (which only has the zero mode).
#
# More precisely:
# SA: 1/g^2(SA) includes all PW sectors
# 4D: 1/g^2(4D, M_KK) = 1/g^2(SA) - (KK contributions to a_4) / g^2(SA)
# So the 4D coupling is STRONGER (less 1/g^2) because you're removing the
# KK modes that were contributing positively to a_4.
#
# Wait. This is getting confused. Let me think from first principles.
#
# The spectral action gives:
#   S_YM = (f_0 / pi^2) * a_4[F] * int F^2
# where a_4[F] includes ALL PW modes. This sets:
#   1/g^2(SA) = f_0 * a_4 / pi^2
#
# Now a_4 = sum_{(p,q)} T(p,q) * f(lambda_{(p,q)}^2/Lambda^2)
# where f is the cutoff function.
#
# Below M_KK, only the (0,0) sector contributes. The 4D effective coupling:
#   1/g^2(4D, M_KK) = f_0 * a_4^{(0,0)} / pi^2 + [threshold from running M_KK -> mu]
#
# But a_4^{(0,0)} is much smaller than the full a_4. The difference
# a_4 - a_4^{(0,0)} = sum_{(p,q)!=(0,0)} T(p,q) * f(lambda^2/Lambda^2)
# IS the KK contribution that gets "integrated out" at M_KK.
#
# When we match, the 4D coupling at M_KK is:
#   1/g^2(4D, M_KK) = 1/g^2(SA) - delta(1/g^2)_threshold
# where delta accounts for the modes that are no longer present below M_KK.
#
# In the Choi-Kim-Shin framework, the finite threshold is:
#   delta(1/g^2) = (1/(8pi^2)) * SUM T_n * ln(Lambda^2/M_n^2)
# This is the amount by which the FULL theory's 1/g^2 EXCEEDS the zero-mode's.
# So at M_KK:
#   1/g^2(4D) = 1/g^2(SA_full) - delta(1/g^2)
# Making the 4D coupling STRONGER (smaller 1/g^2).
#
# BUT: in S62, the nominal g_3(M_KK) = 0.516 comes from RUNNING SM couplings
# UP from M_Z. This already assumes the correct 4D coupling. The SA predicts
# a particular 1/g^2(SA) at the cutoff. The threshold correction is needed
# to MATCH these:
#   1/g^2(SM, M_KK) = 1/g^2(SA, full) - delta(threshold)
#
# If 1/g^2(SA) > 1/g^2(SM) + delta, the SA predicts a weaker coupling
# and hence a lighter Higgs. If 1/g^2(SA) < 1/g^2(SM) + delta, the SA
# predicts a stronger coupling and heavier Higgs.
#
# The S62 result m_H = 190 GeV comes from using g_3(M_KK) = 0.516 (from SM running)
# as the CCM coupling, giving lambda_CCM = (4/3) * 0.516^2 * 0.414 = 0.147.
# This is too large -> m_H too heavy.
#
# To reduce m_H, we need a SMALLER g_3 at M_KK. The threshold correction
# tells us that the SA includes KK modes, so the BARE SA coupling is spread
# across all modes. The effective 4D coupling should be SMALLER than the SA value.
#
# The CORRECT matching: the spectral action coupling is set at the CUTOFF,
# not at M_KK. Running DOWN from Lambda to M_KK, the KK modes contribute
# to the running. The 4D coupling at M_KK is:
#
#   1/g_3^2(M_KK) = 1/g_3^2(Lambda) + (1/(8pi^2)) * SUM T(p,q) * ln(Lambda^2/M_{pq}^2)
#
# where the sum is over modes with M_KK < M_{pq} < Lambda.
# This INCREASES 1/g^2 (weakens the coupling) at M_KK relative to Lambda.
#
# So the effective g_3 at M_KK (for 4D matching) is SMALLER than at Lambda.
# This is what we want: smaller g_3 -> smaller lambda -> lighter Higgs.
#
# delta_BCS in S62 is the fractional reduction: g_3^eff = g_3 * (1 - delta_BCS).
# The equivalent delta_BCS from KK threshold:
#   g_3^{-2}(M_KK) = g_3^{-2}(Lambda) + delta
#   g_3(M_KK) = g_3(Lambda) / sqrt(1 + g_3^2(Lambda) * delta)
#   ~ g_3(Lambda) * (1 - g_3^2(Lambda) * delta / 2)
# So delta_BCS_eff = g_3^2(Lambda) * delta / 2

# For the computation: I'll use the nominal g_3(M_KK) = 0.516 as the
# starting point (from SM running), and add the KK threshold correction
# to SHIFT 1/g_3^2 UPWARD (weakening the coupling).
# Then compute lambda_CCM with the corrected g_3, and run down.

print(f"\n  Higgs mass prediction by truncation level:")
print(f"  {'L':>3} {'delta(1/g3^2)':>14} {'g3_eff':>8} {'lambda_CCM':>12} {'m_H (GeV)':>10}")

m_H_by_L_sharp = np.zeros(len(L_range))
m_H_by_L_gauss = np.zeros(len(L_range))
g3_eff_by_L_sharp = np.zeros(len(L_range))
g3_eff_by_L_gauss = np.zeros(len(L_range))
lam_CCM_by_L_sharp = np.zeros(len(L_range))
lam_CCM_by_L_gauss = np.zeros(len(L_range))

# Use sharp with fixed Lambda for the main result
for iL, L_val in enumerate(L_range):
    delta = delta_g3_inv_sharp_fixed[iL]
    g3_inv2_eff = g3_inv2_nominal + delta
    g3_eff = 1.0 / np.sqrt(g3_inv2_eff) if g3_inv2_eff > 0 else 0.0
    lam_ccm = (4.0/3.0) * g3_eff**2 * ratio_gilkey
    mH = run_rg_down_get_mH(g3_eff, lam_ccm)

    m_H_by_L_sharp[iL] = mH
    g3_eff_by_L_sharp[iL] = g3_eff
    lam_CCM_by_L_sharp[iL] = lam_ccm

    print(f"  {L_val:3d} {delta:14.6f} {g3_eff:8.4f} {lam_ccm:12.6f} {mH:10.2f}")

print(f"\n  Gaussian-regulated:")
print(f"  {'L':>3} {'delta(1/g3^2)':>14} {'g3_eff':>8} {'lambda_CCM':>12} {'m_H (GeV)':>10}")

for iL, L_val in enumerate(L_range):
    delta = delta_g3_inv_gauss_fixed[iL]
    g3_inv2_eff = g3_inv2_nominal + delta
    g3_eff = 1.0 / np.sqrt(g3_inv2_eff) if g3_inv2_eff > 0 else 0.0
    lam_ccm = (4.0/3.0) * g3_eff**2 * ratio_gilkey
    mH = run_rg_down_get_mH(g3_eff, lam_ccm)

    m_H_by_L_gauss[iL] = mH
    g3_eff_by_L_gauss[iL] = g3_eff
    lam_CCM_by_L_gauss[iL] = lam_ccm

    print(f"  {L_val:3d} {delta:14.6f} {g3_eff:8.4f} {lam_ccm:12.6f} {mH:10.2f}")

# =============================================================================
# 7. SECOND f_0 MATCHING: alpha_GUT = 1/10.8 (internal)
# =============================================================================
print("\n" + "=" * 76)
print("7. ALTERNATIVE MATCHING: alpha_GUT = 1/10.8")
print("=" * 76)

# From the internal metric: alpha_GUT = pi/(2*f_0) with f_0 from the a_2/a_0
# matching of gravity. The Kerner route gives a different M_KK and hence g_3.
# With f_0 = 4.26: alpha_GUT = pi / (2*4.26) = 0.369, 1/alpha = 2.71.
# This gives g^2 = 4*pi*alpha = 4.63, g = 2.15. Way too strong.
#
# Actually: f_0 = 4.26 is NOT the right value. Let me recompute.
# The internal matching uses the Kerner M_KK = 5.04e17 GeV.
# Running SM g_3 to this higher scale:

t_MKK_kerner = np.log(M_KK_kerner / M_Z)
sol_up_K = solve_ivp(
    beta_2loop_SM, [0, t_MKK_kerner], y0_up,
    t_eval=np.linspace(0, t_MKK_kerner, 3000),
    method='RK45', rtol=1e-12, atol=1e-14
)
g3_at_MKK_K = sol_up_K.y[2, -1]
g1_at_MKK_K = sol_up_K.y[0, -1]
g2_at_MKK_K = sol_up_K.y[1, -1]
yt_at_MKK_K = sol_up_K.y[3, -1]

g3_inv2_kerner = 1.0 / g3_at_MKK_K**2

print(f"  Kerner M_KK = {M_KK_kerner:.4e} GeV")
print(f"  t_MKK_kerner = {t_MKK_kerner:.4f}")
print(f"  g_3(M_KK_kerner) = {g3_at_MKK_K:.6f}")
print(f"  1/g_3^2(M_KK_kerner) = {g3_inv2_kerner:.6f}")

# The Kerner route threshold correction uses the same PW eigenvalues
# but at a different Lambda. Since M_KK_kerner/M_KK_gravity ~ 6.79,
# the eigenvalues in M_KK_kerner units are omega/6.79 (smaller).
# Actually no — the D_K eigenvalues are in the same geometric units.
# The physical mass M_{(p,q)} = omega * M_KK, and M_KK is different
# for the two routes. The threshold correction is:
#   delta(1/g_3^2) = (1/(8pi^2)) * SUM T(p,q) * ln(Lambda^2/M^2)
# where M = omega * M_KK and Lambda ~ few * M_KK.
# Since omega and Lambda/M_KK are the same in both routes, the
# threshold correction IN THE DIMENSIONLESS RATIO is the same.
# What differs is the starting g_3(M_KK).

# So for Kerner matching:
print(f"\n  Kerner-route Higgs mass:")
print(f"  {'L':>3} {'delta':>14} {'g3_eff':>8} {'lambda':>12} {'m_H':>10}")

m_H_kerner_sharp = np.zeros(len(L_range))
m_H_kerner_gauss = np.zeros(len(L_range))

for iL, L_val in enumerate(L_range):
    delta = delta_g3_inv_sharp_fixed[iL]
    g3_inv2_eff = g3_inv2_kerner + delta
    g3_eff = 1.0 / np.sqrt(g3_inv2_eff) if g3_inv2_eff > 0 else 0.0
    lam_ccm = (4.0/3.0) * g3_eff**2 * ratio_gilkey

    # Need to run from Kerner M_KK down to M_Z
    y0_K = [g1_at_MKK_K, g2_at_MKK_K, g3_eff, yt_at_MKK_K, lam_ccm]
    sol_K = solve_ivp(
        beta_2loop_SM, [t_MKK_kerner, 0], y0_K,
        t_eval=np.linspace(t_MKK_kerner, 0, 2000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    lam_IR = sol_K.y[4, -1]
    mH = np.sqrt(2.0 * abs(lam_IR)) * v_ew if lam_IR > 0 else 0.0
    m_H_kerner_sharp[iL] = mH

    print(f"  {L_val:3d} {delta:14.6f} {g3_eff:8.4f} {lam_ccm:12.6f} {mH:10.2f}")

print(f"\n  Kerner Gaussian-regulated:")
print(f"  {'L':>3} {'delta':>14} {'g3_eff':>8} {'lambda':>12} {'m_H':>10}")

for iL, L_val in enumerate(L_range):
    delta = delta_g3_inv_gauss_fixed[iL]
    g3_inv2_eff = g3_inv2_kerner + delta
    g3_eff = 1.0 / np.sqrt(g3_inv2_eff) if g3_inv2_eff > 0 else 0.0
    lam_ccm = (4.0/3.0) * g3_eff**2 * ratio_gilkey

    y0_K = [g1_at_MKK_K, g2_at_MKK_K, g3_eff, yt_at_MKK_K, lam_ccm]
    sol_K = solve_ivp(
        beta_2loop_SM, [t_MKK_kerner, 0], y0_K,
        t_eval=np.linspace(t_MKK_kerner, 0, 2000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    lam_IR = sol_K.y[4, -1]
    mH = np.sqrt(2.0 * abs(lam_IR)) * v_ew if lam_IR > 0 else 0.0
    m_H_kerner_gauss[iL] = mH

    print(f"  {L_val:3d} {delta:14.6f} {g3_eff:8.4f} {lam_ccm:12.6f} {mH:10.2f}")

# =============================================================================
# 8. GATE VERDICT
# =============================================================================
print("\n" + "=" * 76)
print("8. GATE VERDICT: KK-THRESHOLD-63")
print("=" * 76)

PASS_LO = 0.73  # (local)
PASS_HI = 1.48  # (local)

# Main result: L=6 sharp with fixed Lambda
delta_L6_sharp = delta_g3_inv_sharp_fixed[-1]
delta_L6_gauss = delta_g3_inv_gauss_fixed[-1]

# Convergence: ratio L=6/L=5
ratio_L6_L5_sharp = delta_g3_inv_sharp_fixed[-1] / delta_g3_inv_sharp_fixed[-2] if delta_g3_inv_sharp_fixed[-2] != 0 else np.inf
ratio_L6_L5_gauss = delta_g3_inv_gauss_fixed[-1] / delta_g3_inv_gauss_fixed[-2] if delta_g3_inv_gauss_fixed[-2] != 0 else np.inf

print(f"  delta(1/g_3^2) at L=6:")
print(f"    Sharp (Lambda_fixed):    {delta_L6_sharp:.6f}")
print(f"    Gaussian (Lambda_fixed): {delta_L6_gauss:.6f}")
print(f"    PASS band: [{PASS_LO}, {PASS_HI}]")
print(f"\n  Convergence ratio L=6/L=5:")
print(f"    Sharp:    {ratio_L6_L5_sharp:.4f}")
print(f"    Gaussian: {ratio_L6_L5_gauss:.4f}")
print(f"    DIVERGES if > 2.0")

# Determine verdict
sharp_in_band = PASS_LO <= delta_L6_sharp <= PASS_HI
gauss_in_band = PASS_LO <= delta_L6_gauss <= PASS_HI
diverges = ratio_L6_L5_sharp > 2.0 or ratio_L6_L5_gauss > 2.0

if diverges:
    verdict = "FAIL"
    detail = (f"Divergent: sharp ratio={ratio_L6_L5_sharp:.4f}, "
              f"gauss ratio={ratio_L6_L5_gauss:.4f}. "
              f"delta_sharp(L=6)={delta_L6_sharp:.4f}, "
              f"delta_gauss(L=6)={delta_L6_gauss:.4f}. "
              f"PW tower Dynkin sum grows as L^{conv_ratio_sharp_fixed[-1]:.1f}, "
              f"overwhelming logarithmic suppression.")
elif sharp_in_band and gauss_in_band:
    verdict = "PASS"
    detail = (f"Converged: delta_sharp(L=6)={delta_L6_sharp:.4f} in [{PASS_LO},{PASS_HI}], "
              f"delta_gauss(L=6)={delta_L6_gauss:.4f} in [{PASS_LO},{PASS_HI}]. "
              f"m_H(sharp)={m_H_by_L_sharp[-1]:.1f} GeV, "
              f"m_H(gauss)={m_H_by_L_gauss[-1]:.1f} GeV.")
else:
    verdict = "INFO"
    detail = (f"Converged but outside PASS band. "
              f"delta_sharp(L=6)={delta_L6_sharp:.4f}, "
              f"delta_gauss(L=6)={delta_L6_gauss:.4f}. "
              f"PASS band=[{PASS_LO},{PASS_HI}]. "
              f"m_H(sharp)={m_H_by_L_sharp[-1]:.1f} GeV, "
              f"m_H(gauss)={m_H_by_L_gauss[-1]:.1f} GeV.")

print(f"\n  *** VERDICT: {verdict} ***")
print(f"  {detail}")

# Summary of m_H predictions
print(f"\n  m_H summary at L=6:")
print(f"    Gravity route, sharp:    {m_H_by_L_sharp[-1]:.2f} GeV")
print(f"    Gravity route, Gaussian: {m_H_by_L_gauss[-1]:.2f} GeV")
print(f"    Kerner route, sharp:     {m_H_kerner_sharp[-1]:.2f} GeV")
print(f"    Kerner route, Gaussian:  {m_H_kerner_gauss[-1]:.2f} GeV")
print(f"    Observed:                {m_H_obs} GeV")
print(f"    S62 no threshold:        {m_H_2loop_noBCS:.2f} GeV")

# =============================================================================
# 9. SAVE DATA
# =============================================================================
print("\n" + "=" * 76)
print("9. SAVING DATA")
print("=" * 76)

save_path = os.path.join(outdir, 's63_kk_threshold.npz')

# Build sector data arrays for saving
n_sec = len(sector_contributions)
sec_p = np.array([s['p'] for s in sector_contributions])
sec_q = np.array([s['q'] for s in sector_contributions])
sec_dim = np.array([s['dim'] for s in sector_contributions])
sec_level = np.array([s['level'] for s in sector_contributions])
sec_C2 = np.array([s['C2'] for s in sector_contributions])
sec_T = np.array([s['T'] for s in sector_contributions])
sec_omega_min = np.array([s['omega_min'] for s in sector_contributions])
sec_omega_max = np.array([s['omega_max'] for s in sector_contributions])
sec_contrib_sharp = np.array([s['contrib_sharp_fixed'] for s in sector_contributions])
sec_contrib_gauss = np.array([s['contrib_gauss_fixed'] for s in sector_contributions])

np.savez(save_path,
    # Gate
    gate_name='KK-THRESHOLD-63',
    gate_verdict=verdict,
    gate_detail=detail,
    # Threshold corrections by L
    L_range=L_range,
    delta_g3_inv_sharp_Lmax=delta_g3_inv_sharp_Lmax,
    delta_g3_inv_sharp_fixed=delta_g3_inv_sharp_fixed,
    delta_g3_inv_gauss_fixed=delta_g3_inv_gauss_fixed,
    delta_g3_inv_gauss_Lmax=delta_g3_inv_gauss_Lmax,
    total_T_by_L=total_T_by_L,
    n_sectors_by_L=n_sectors_by_L,
    # Convergence
    conv_ratio_sharp_fixed=conv_ratio_sharp_fixed,
    conv_ratio_gauss_fixed=conv_ratio_gauss_fixed,
    ratio_L6_L5_sharp=ratio_L6_L5_sharp,
    ratio_L6_L5_gauss=ratio_L6_L5_gauss,
    # Higgs mass by L
    m_H_by_L_sharp=m_H_by_L_sharp,
    m_H_by_L_gauss=m_H_by_L_gauss,
    g3_eff_by_L_sharp=g3_eff_by_L_sharp,
    g3_eff_by_L_gauss=g3_eff_by_L_gauss,
    lam_CCM_by_L_sharp=lam_CCM_by_L_sharp,
    lam_CCM_by_L_gauss=lam_CCM_by_L_gauss,
    m_H_kerner_sharp=m_H_kerner_sharp,
    m_H_kerner_gauss=m_H_kerner_gauss,
    # Sector data
    sec_p=sec_p, sec_q=sec_q, sec_dim=sec_dim, sec_level=sec_level,
    sec_C2=sec_C2, sec_T=sec_T,
    sec_omega_min=sec_omega_min, sec_omega_max=sec_omega_max,
    sec_contrib_sharp=sec_contrib_sharp, sec_contrib_gauss=sec_contrib_gauss,
    # Parameters
    Lambda_fixed=Lambda_fixed,
    gamma_opt=gamma_opt,
    g3_MKK_nominal=g3_MKK_nominal,
    g3_inv2_nominal=g3_inv2_nominal,
    ratio_gilkey=ratio_gilkey,
    m_H_2loop_noBCS=m_H_2loop_noBCS,
    PASS_LO=PASS_LO, PASS_HI=PASS_HI,
)

print(f"  Saved: {save_path}")

# =============================================================================
# 10. PLOT
# =============================================================================
print("\n" + "=" * 76)
print("10. GENERATING PLOT")
print("=" * 76)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('KK-THRESHOLD-63: PW Tower Threshold Corrections to L=6',
             fontsize=14, fontweight='bold')

# Panel 1: Threshold correction vs L
ax1 = axes[0, 0]
ax1.plot(L_range, delta_g3_inv_sharp_fixed, 'b-o', label='Sharp (Lambda fixed)', linewidth=2)
ax1.plot(L_range, delta_g3_inv_gauss_fixed, 'r-s', label='Gaussian (Lambda fixed)', linewidth=2)
ax1.plot(L_range, delta_g3_inv_sharp_Lmax, 'b--^', label='Sharp (Lambda=Lmax)', alpha=0.6)
ax1.plot(L_range, delta_g3_inv_gauss_Lmax, 'r--v', label='Gaussian (Lambda=Lmax)', alpha=0.6)
ax1.axhspan(PASS_LO, PASS_HI, alpha=0.15, color='green', label=f'PASS band [{PASS_LO},{PASS_HI}]')
ax1.set_xlabel('Truncation level L')
ax1.set_ylabel(r'$\delta(1/g_3^2)$')
ax1.set_title(r'Threshold correction $\delta(1/g_3^2)$ vs L')
ax1.legend(fontsize=8, loc='upper left')
ax1.grid(True, alpha=0.3)

# Panel 2: Higgs mass vs L
ax2 = axes[0, 1]
ax2.plot(L_range, m_H_by_L_sharp, 'b-o', label='Gravity, sharp', linewidth=2)
ax2.plot(L_range, m_H_by_L_gauss, 'r-s', label='Gravity, Gaussian', linewidth=2)
ax2.plot(L_range, m_H_kerner_sharp, 'b--^', label='Kerner, sharp', alpha=0.6)
ax2.plot(L_range, m_H_kerner_gauss, 'r--v', label='Kerner, Gaussian', alpha=0.6)
ax2.axhline(125.10, color='green', linewidth=2, linestyle='--', label='Observed (125.1 GeV)')
ax2.axhline(m_H_2loop_noBCS, color='gray', linewidth=1, linestyle=':', label=f'No threshold ({m_H_2loop_noBCS:.0f} GeV)')
ax2.set_xlabel('Truncation level L')
ax2.set_ylabel(r'$m_H$ (GeV)')
ax2.set_title('Predicted Higgs mass vs truncation level')
ax2.legend(fontsize=8, loc='upper right')
ax2.grid(True, alpha=0.3)

# Panel 3: Convergence ratios
ax3 = axes[1, 0]
ax3.plot(L_range[1:], conv_ratio_sharp_fixed, 'b-o', label='Sharp (Lambda fixed)', linewidth=2)
ax3.plot(L_range[1:], conv_ratio_gauss_fixed, 'r-s', label='Gaussian (Lambda fixed)', linewidth=2)
ax3.axhline(2.0, color='red', linewidth=2, linestyle='--', label='Divergence threshold (2.0)')
ax3.axhline(1.0, color='green', linewidth=1, linestyle='--', label='Perfect convergence', alpha=0.5)
ax3.set_xlabel('Truncation level L')
ax3.set_ylabel(r'$\delta(L) / \delta(L-1)$')
ax3.set_title('Convergence ratio (successive levels)')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0, max(3, 1.1 * max(np.max(conv_ratio_sharp_fixed), np.max(conv_ratio_gauss_fixed))))

# Panel 4: Total Dynkin index and sector structure
ax4 = axes[1, 1]
ax4.semilogy(L_range, total_T_by_L, 'k-o', label='Total T(L)', linewidth=2)
# Also show per-level T
T_per_level = np.zeros(len(L_range))
for iL, L_val in enumerate(L_range):
    T_lev = sum(s['T'] for s in sector_contributions if s['level'] == L_val and not (s['p'] == 0 and s['q'] == 0))
    T_per_level[iL] = T_lev
ax4.semilogy(L_range, T_per_level, 'g--s', label='T (per level)', linewidth=1.5)
ax4.set_xlabel('Truncation level L')
ax4.set_ylabel('Dynkin index T')
ax4.set_title('Cumulative and per-level Dynkin index')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(outdir, 's63_kk_threshold.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

print("\n" + "=" * 76)
print("COMPUTATION COMPLETE")
print("=" * 76)
