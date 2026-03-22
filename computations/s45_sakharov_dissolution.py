#!/usr/bin/env python3
"""
SAKHAROV-UV-DISSOLUTION-45: Connecting Sakharov UV Cutoff to Dissolution Scale
===============================================================================

Two S44 results constrain the same physics from opposite directions:

  1. SAKHAROV-GN-44 (W1-1, corrected by audit): The standard Sakharov induced
     gravity formula at Lambda = 10 * M_KK gives G_N within factor ~27 of
     observed. The EFFECTIVE UV cutoff is Lambda_eff ~ 10 M_KK ~ 7.4e17 GeV.

  2. DISSOLUTION-SCALING-44 (W6-7): The spectral triple's block-diagonal
     structure dissolves under random perturbation at epsilon_c ~ a * N^{-alpha}
     with a = 0.188, alpha = 0.457, R^2 = 0.957.

QUESTION: Is there a quantitative relationship? Specifically:
  - At what truncation N does epsilon_c match the physical foam strength?
  - Does the corresponding energy scale E_diss = M_KK * (N/N_spinor)^{1/8}
    match Lambda_eff ~ 10 M_KK from the Sakharov formula?
  - Does the dissolution N correspond to the mode count needed for Sakharov
    to produce observed G_N?

The key relationship to test:
  N_PW(max_pq_sum) = sum_{p+q <= L} 16 * dim(p,q)
  epsilon_c(N) = 0.188 * N^{-0.457}
  Lambda_eff(L) = max eigenvalue * M_KK at truncation L

If the Sakharov UV cutoff = dissolution scale, then the scale at which
the spectral triple EMERGES is the same scale at which induced gravity
becomes the correct effective description.

Gate: SAKHAROV-UV-DISSOLUTION-45
  INFO if quantitative relationship found
  PASS if Lambda_eff and epsilon_c give consistent picture

Author: quantum-foam-theorist, Session 45
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path
import sys, os

DATA_DIR = Path(__file__).parent
sys.path.insert(0, str(DATA_DIR))

from canonical_constants import (
    tau_fold as TAU_FOLD,
    M_KK as M_KK_GN,
    M_Pl_reduced as M_PL_RED,
    G_N as G_N_OBS,
    l_Planck as L_PLANCK,
    Lambda_obs_MP4,
    rho_Lambda_obs as RHO_LAMBDA_OBS,
)

G_N_NAT = 1.0 / (8.0 * np.pi * M_PL_RED**2)   # GeV^{-2}
INV_16piG_OBS = M_PL_RED**2 / 2.0               # = 1/(16piG) in GeV^2

print("=" * 78)
print("SAKHAROV-UV-DISSOLUTION-45")
print("Connecting the Sakharov UV Cutoff to the Dissolution Emergence Scale")
print("=" * 78)

# ===========================================================================
# Step 0: Load S44 results
# ===========================================================================
print("\n--- Step 0: Load S44 data ---")

d_sak_audit = np.load(DATA_DIR / 's44_sakharov_gn_audit.npz', allow_pickle=True)
d_sak_full  = np.load(DATA_DIR / 's44_sakharov_gn.npz', allow_pickle=True)
d_diss      = np.load(DATA_DIR / 's44_dissolution_scaling.npz', allow_pickle=True)
d36         = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d42c        = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)

# Sakharov audit results (Formula B = standard Sakharov, corrected)
inv_16piG_sak_full = float(d_sak_audit['inv_16piG_sakharov_full'])   # GeV^2, at Lambda=M_Pl
inv_16piG_obs      = float(d_sak_audit['inv_16piG_obs'])             # GeV^2
ratio_B            = float(d_sak_audit['ratio_B'])                   # sak/obs
log10_dev_B        = float(d_sak_audit['log10_dev'])                 # |log10(ratio)|

# Dissolution scaling results
N_diss      = d_diss['N_values']         # [112, 432, 1232, 2912, 6048]
eps_diss    = d_diss['epsilon_crossover'] # measured epsilon_c at each N
alpha_power = d_diss['fit_N_-alpha_params']  # [a, alpha] for epsilon_c = a*N^{-alpha}
R2_power    = float(d_diss['fit_N_-alpha_R2'][0])
a_fit       = alpha_power[0]  # 0.188
alpha_fit   = alpha_power[1]  # 0.457

# Spectrum data
a0_fold = float(d42c['a0_fold'])
a2_fold = float(d42c['a2_fold'])
a4_fold = float(d42c['a4_fold'])
S_log   = float(d_sak_full['S_log'])

SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

print(f"  Sakharov (Formula B, Lambda=M_Pl): ratio to obs = {ratio_B:.4f} ({log10_dev_B:.2f} dex)")
print(f"  Dissolution: epsilon_c = {a_fit:.4f} * N^(-{alpha_fit:.4f}), R^2 = {R2_power:.4f}")
print(f"  a_0 = {a0_fold:.0f}, a_2 = {a2_fold:.2f}")
print(f"  M_KK = {M_KK_GN:.4e} GeV, M_Pl = {M_PL_RED:.4e} GeV")
print(f"  Lambda/M_KK = {M_PL_RED / M_KK_GN:.2f}")


# ===========================================================================
# Step 1: Mode count N(L) for SU(3) Peter-Weyl truncation
# ===========================================================================
print(f"\n{'='*78}")
print("Step 1: Mode count N(L) = sum_{p+q <= L} 16 * dim(p,q) for SU(3)")
print("=" * 78)

def N_PW(L_max):
    """Total Hilbert space dimension at truncation p+q <= L_max."""
    total = 0
    n_sec = 0
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            d = dim_pq(p, q)
            total += 16 * d
            n_sec += 1
    return total, n_sec

def a0_PW(L_max):
    """Peter-Weyl weighted mode count a_0 = sum 8*dim(p,q)^2 at truncation L_max."""
    total = 0
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            d = dim_pq(p, q)
            total += 8 * d**2  # right-regular rep: degeneracy = dim(p,q) per spinor mode
    return total

# Build table up to L=50
L_vals = list(range(1, 51))
N_hilbert = []
N_a0 = []
N_sectors = []

print(f"\n  {'L':>4s}  {'N_Hilbert':>10s}  {'a0_PW':>12s}  {'n_sectors':>10s}")
for L in L_vals:
    N_h, n_s = N_PW(L)
    a0_val = a0_PW(L)
    N_hilbert.append(N_h)
    N_a0.append(a0_val)
    N_sectors.append(n_s)
    if L <= 10 or L % 5 == 0:
        print(f"  {L:4d}  {N_h:10d}  {a0_val:12d}  {n_s:10d}")

N_hilbert = np.array(N_hilbert, dtype=float)
N_a0 = np.array(N_a0, dtype=float)
N_sectors = np.array(N_sectors, dtype=float)
L_vals = np.array(L_vals, dtype=float)

# Verify against dissolution data
print(f"\n  Cross-check against S44 dissolution data:")
for i, Nd in enumerate(N_diss):
    max_pq = int(d_diss['max_pq_sums'][i])
    N_check, _ = N_PW(max_pq)
    match = "MATCH" if N_check == int(Nd) else f"MISMATCH ({N_check})"
    print(f"    max_pq_sum={max_pq}: N_diss={int(Nd)}, N_PW={N_check} -> {match}")


# ===========================================================================
# Step 2: Dissolution threshold epsilon_c(N) extrapolation
# ===========================================================================
print(f"\n{'='*78}")
print("Step 2: Dissolution threshold epsilon_c(N) extrapolation")
print("=" * 78)

# Use the power-law fit: epsilon_c = a_fit * N^{-alpha_fit}
# where N = N_Hilbert (total Hilbert space dimension)
# a_fit = 0.188, alpha_fit = 0.457

eps_c_extrap = a_fit * N_hilbert**(-alpha_fit)

print(f"\n  Power-law fit: epsilon_c = {a_fit:.4f} * N^(-{alpha_fit:.4f})")
print(f"  R^2 = {R2_power:.4f}")
print(f"\n  {'L':>4s}  {'N':>10s}  {'eps_c':>12s}  {'1/eps_c':>12s}")
for i, L in enumerate(L_vals):
    if L <= 10 or int(L) % 5 == 0:
        print(f"  {int(L):4d}  {int(N_hilbert[i]):10d}  {eps_c_extrap[i]:12.2e}  {1/eps_c_extrap[i]:12.1f}")


# ===========================================================================
# Step 3: Sakharov 1/(16piG) as function of truncation level
# ===========================================================================
print(f"\n{'='*78}")
print("Step 3: Sakharov induced gravity vs truncation level")
print("=" * 78)

# Formula B (standard Sakharov, from audit):
#   1/(16piG) = (1/48pi^2) sum_k d_k [Lambda^2 - m_k^2 ln(1 + Lambda^2/m_k^2)]
#
# The LEADING term is ~ (a_0/48pi^2) * Lambda^2, dominant for Lambda >> m_k.
# For a given truncation L, a_0(L) determines the species count.
#
# The spectral action formula:
#   1/(16piG) = (6/pi^3) * a_2(L) * M_KK^2
#
# Since we only have the full spectrum at L=3 (10 sectors), we cannot compute
# exact a_2(L) for higher L. But the LEADING Sakharov term lets us estimate
# the scale at which the formula gives the correct G_N.
#
# Species contribution to Sakharov:
#   1/(16piG) ≈ a_0(L) / (48pi^2) * Lambda_eff^2
# Setting this equal to observed:
#   Lambda_eff^2 = 48pi^2 * INV_16piG_OBS / a_0(L)
#   Lambda_eff(L) = sqrt(48*pi^2 / a_0(L)) * M_Pl_red / sqrt(2)

# More precisely, from the audit at L=3 (a_0=6440), Lambda=M_Pl:
# inv_16piG_sak_full = 7.95e37 = (a_0/48pi^2)*M_Pl^2 * [1 - correction]
# The correction from m_k^2*ln(1+Lambda^2/m_k^2) is subleading.
# The leading coefficient is:
coeff_leading = a0_fold / (48 * np.pi**2)  # for L=3
inv_leading_L3 = coeff_leading * M_PL_RED**2
print(f"\n  At L=3 (a_0=6440), Lambda=M_Pl:")
print(f"    Leading term: (a_0/48pi^2)*Lambda^2 = {inv_leading_L3:.4e} GeV^2")
print(f"    Full Sakharov (audit):               = {inv_16piG_sak_full:.4e} GeV^2")
print(f"    Observed:                             = {inv_16piG_obs:.4e} GeV^2")
print(f"    Leading/observed = {inv_leading_L3/inv_16piG_obs:.4f}")
print(f"    Full/observed    = {inv_16piG_sak_full/inv_16piG_obs:.4f}")

# The leading term overshoots by ~27x (ratio_B).
# This is because Lambda=M_Pl and a_0=6440 together give too many species
# contributing too much. The SUBLEADING m_k^2*ln correction is negative
# and partially cancels.

# For GENERAL L, the leading Sakharov term at Lambda=M_Pl:
inv_sak_leading = (N_a0 / (48 * np.pi**2)) * M_PL_RED**2

# And the matching cutoff Lambda_match(L) where leading term = observed:
# Lambda_match^2 = 48*pi^2 * INV_16piG_OBS / a_0(L)
Lambda_match = np.sqrt(48 * np.pi**2 * INV_16piG_OBS / N_a0)

print(f"\n  Lambda_match(L) = sqrt(48*pi^2 * (M_Pl_red^2/2) / a_0(L))")
print(f"  = scale where leading Sakharov term matches observed G_N")
print(f"\n  {'L':>4s}  {'a_0':>12s}  {'Lambda_match':>14s}  {'Lambda/M_KK':>12s}  {'Lambda/M_Pl':>12s}")
for i, L in enumerate(L_vals):
    if L <= 10 or int(L) % 5 == 0:
        print(f"  {int(L):4d}  {int(N_a0[i]):12d}  {Lambda_match[i]:14.4e}  "
              f"{Lambda_match[i]/M_KK_GN:12.2f}  {Lambda_match[i]/M_PL_RED:12.6f}")

# Find L where Lambda_match ~ 10*M_KK (the S44 W1-1 result)
Lambda_target = 10 * M_KK_GN
idx_10mkk = np.argmin(np.abs(Lambda_match - Lambda_target))
L_10mkk = int(L_vals[idx_10mkk])
a0_10mkk = int(N_a0[idx_10mkk])
print(f"\n  Lambda_match ≈ 10*M_KK at L = {L_10mkk}, a_0 = {a0_10mkk}")
print(f"    Lambda_match({L_10mkk}) = {Lambda_match[idx_10mkk]:.4e} GeV")
print(f"    10*M_KK = {Lambda_target:.4e} GeV")


# ===========================================================================
# Step 4: The relationship -- N at Lambda_match vs N at dissolution
# ===========================================================================
print(f"\n{'='*78}")
print("Step 4: Central computation -- Sakharov scale vs dissolution scale")
print("=" * 78)

# At truncation L:
#   - N_Hilbert(L) determines the dissolution threshold epsilon_c(L)
#   - a_0(L) determines the Sakharov G_N via leading term
#   - Lambda_match(L) is the UV cutoff at which Sakharov = observed G_N
#
# The PHYSICAL question: at what L does epsilon_c become smaller than
# the PHYSICAL foam strength epsilon_phys?
#
# Physical foam strength estimates:
# (a) Carlip foam: metric fluctuation delta_g/g ~ (l_P/L)^{2/3}
#     At scale L_Carlip = 1.74 mm: delta_g/g ~ 4.4e-22 (QF-57)
#     At scale l_KK = 1/M_KK: delta_g/g ~ (l_P * M_KK)^{2/3}

l_KK = 1.0 / (M_KK_GN * 5.068e15)  # M_KK in m (GeV * GeV_to_inv_m = inv_m, so l = 1/that)
# Actually: l_KK [m] = hbar*c / (M_KK [GeV]) = 1.973e-16 / M_KK
l_KK_m = 1.973269804e-16 / M_KK_GN
L_PLANCK_M = 1.616255e-35

print(f"\n  Physical scales:")
print(f"    l_P = {L_PLANCK_M:.4e} m")
print(f"    l_KK = hbar*c/M_KK = {l_KK_m:.4e} m")
print(f"    l_KK / l_P = {l_KK_m / L_PLANCK_M:.2e}")

# Carlip/Ng holographic foam at KK scale:
delta_g_holographic_KK = (L_PLANCK_M / l_KK_m)**(2.0/3.0)
delta_g_randomwalk_KK = (L_PLANCK_M / l_KK_m)**(1.0/2.0)
delta_g_planck_KK = L_PLANCK_M / l_KK_m

print(f"\n  Metric fluctuations at KK scale (l = l_KK):")
print(f"    Holographic (Ng):   delta_g/g = (l_P/l_KK)^(2/3) = {delta_g_holographic_KK:.4e}")
print(f"    Random walk:        delta_g/g = (l_P/l_KK)^(1/2) = {delta_g_randomwalk_KK:.4e}")
print(f"    Planck:             delta_g/g = l_P/l_KK          = {delta_g_planck_KK:.4e}")

# (b) Left-invariant foam (S43 QF-12): sigma_lambda ~ 10^{-4} on SU(3)
epsilon_left_inv = 1e-4

# (c) Generic foam (non-left-invariant): epsilon ~ 0.01-0.02 (S43 DISSOLUTION)
epsilon_generic = 0.014

# (d) Physical Planck-scale foam on SU(3):
# The metric fluctuation on SU(3) induced by 4D Planck-scale foam
# is effaced by the M_KK/M_Pl hierarchy.
# Effacement (S42 EFFACEMENT-42): delta_g(SU3) ~ delta_g(4D) * (l_P/l_KK)
# At KK scale: delta_g(4D) ~ (l_P/l_KK)^{2/3}, so
# delta_g(SU3) ~ (l_P/l_KK)^{2/3} * (l_P/l_KK) = (l_P/l_KK)^{5/3}
epsilon_effaced_holographic = (L_PLANCK_M / l_KK_m)**(5.0/3.0)
# But the dissolution perturbation is in Frobenius norm, not pointwise metric.
# For an N-dimensional matrix, ||V||_F / ||H||_F ~ epsilon (our definition).
# The connection: epsilon ~ delta_g/g for random perturbation of the metric.
# (In the dissolution test, V is a random Hermitian matrix with
#  ||V||_F = epsilon * ||H_0||_F)

print(f"\n  Foam strength epsilon estimates:")
print(f"    Left-invariant SU(3):                  {epsilon_left_inv:.4e}")
print(f"    Generic dissolution (S43 at N=432):    {epsilon_generic:.4e}")
print(f"    Holographic at KK scale:               {delta_g_holographic_KK:.4e}")
print(f"    Effaced holographic on SU(3):          {epsilon_effaced_holographic:.4e}")

# Now find N_crit where epsilon_c(N) = epsilon_phys for each estimate
def N_crit_from_eps(epsilon_phys, a, alpha):
    """Solve a * N^{-alpha} = epsilon_phys for N."""
    return (a / epsilon_phys)**(1.0/alpha)

foam_scenarios = {
    'left-invariant':    epsilon_left_inv,
    'holographic@l_KK': delta_g_holographic_KK,
    'effaced-hol':      epsilon_effaced_holographic,
}

print(f"\n  N_crit where epsilon_c(N) = epsilon_phys:")
print(f"  {'Scenario':>25s}  {'epsilon_phys':>14s}  {'N_crit':>14s}  {'L ~ N^{1/5}':>12s}")
for name, eps in foam_scenarios.items():
    N_c = N_crit_from_eps(eps, a_fit, alpha_fit)
    L_approx = N_c**(1.0/5.0)  # rough: N_Hilbert ~ L^5 for SU(3)
    print(f"  {name:>25s}  {eps:14.4e}  {N_c:14.2e}  {L_approx:12.1f}")

# For the holographic foam at KK scale:
N_crit_hol = N_crit_from_eps(delta_g_holographic_KK, a_fit, alpha_fit)
# Find the corresponding a_0 (PW-weighted mode count)
# Rough: a_0 ~ 0.8 * L^5 (from the crosscheck script)
L_crit_hol = N_crit_hol**(1.0/5.0)

print(f"\n  Focus: Holographic foam at KK scale")
print(f"    epsilon_phys = {delta_g_holographic_KK:.4e}")
print(f"    N_crit = {N_crit_hol:.4e}")
print(f"    L_crit ~ {L_crit_hol:.1f} (crude N ~ L^5)")


# ===========================================================================
# Step 5: Match Sakharov scale to dissolution scale
# ===========================================================================
print(f"\n{'='*78}")
print("Step 5: Match Sakharov UV cutoff to dissolution emergence scale")
print("=" * 78)

# For each truncation L:
#   Sakharov gives Lambda_match(L) = UV cutoff where G_N matches observed
#   Dissolution gives epsilon_c(L) = foam tolerance of spectral triple
#
# The CONSISTENCY CONDITION is:
#   At L where epsilon_c(L) = epsilon_phys (spectral triple just emerges),
#   Lambda_match(L) should be the PHYSICAL UV cutoff (~ M_Pl or a few * M_KK)

# Compute both curves
print(f"\n  {'L':>4s}  {'N_H':>10s}  {'a_0':>12s}  {'eps_c':>12s}  "
      f"{'Lambda_m':>14s}  {'Lam/M_KK':>10s}  {'Lam/M_Pl':>10s}")
print(f"  {'-'*90}")

for i, L in enumerate(L_vals):
    if L <= 15 or int(L) % 5 == 0:
        print(f"  {int(L):4d}  {int(N_hilbert[i]):10d}  {int(N_a0[i]):12d}  "
              f"{eps_c_extrap[i]:12.2e}  {Lambda_match[i]:14.4e}  "
              f"{Lambda_match[i]/M_KK_GN:10.2f}  {Lambda_match[i]/M_PL_RED:10.6f}")

# The crossover: where does eps_c drop below physical foam?
# And what is Lambda_match there?

for name, eps_phys in foam_scenarios.items():
    N_c = N_crit_from_eps(eps_phys, a_fit, alpha_fit)
    # Find closest L in our table
    idx = np.argmin(np.abs(N_hilbert - N_c))
    L_c = int(L_vals[idx])
    a0_c = int(N_a0[idx])
    Lam_c = Lambda_match[idx]
    eps_at_L = eps_c_extrap[idx]

    print(f"\n  Scenario: {name}")
    print(f"    epsilon_phys = {eps_phys:.4e}")
    print(f"    N_crit = {N_c:.2e}, closest L = {L_c}")
    print(f"    At L={L_c}: eps_c = {eps_at_L:.4e} (target: {eps_phys:.4e})")
    print(f"    At L={L_c}: Lambda_match = {Lam_c:.4e} GeV = {Lam_c/M_KK_GN:.2f} * M_KK")
    print(f"    At L={L_c}: Lambda_match/M_Pl = {Lam_c/M_PL_RED:.6f}")


# ===========================================================================
# Step 6: Detailed analysis -- the 10*M_KK scale
# ===========================================================================
print(f"\n{'='*78}")
print("Step 6: Detailed analysis of the Lambda_eff ~ 10*M_KK scale")
print("=" * 78)

# From S44 audit: at Lambda = 10*M_KK (with a_0=6440, L=3):
# inv_16piG_sak ≈ (6440/48pi^2) * (10*M_KK)^2 = 13.6 * (10*7.43e16)^2
# = 13.6 * 5.52e35 = 7.5e36 vs obs 2.96e36 => ratio ~2.5
# More precisely from the audit: ratio_B = 26.8 (at Lambda=M_Pl)
# At Lambda = 10*M_KK: Lambda^2/M_Pl^2 = (10*7.43e16/2.435e18)^2 = 0.305^2 = 0.093
# So ratio at 10*M_KK ≈ ratio_B * 0.093 ≈ 2.5 (rough)

# Let's compute exactly at 10*M_KK using the audit's Formula B approach
# Load spectrum for direct computation
evals_list = []
degs_list = []
for (p, q) in SECTORS:
    key = f'evals_tau0.190_{p}_{q}'
    if key not in d36.files:
        continue
    ev = d36[key]
    pos = ev[ev > 0.01]
    d = dim_pq(p, q)
    for lam in pos:
        evals_list.append(lam)
        degs_list.append(d)
evals_arr = np.array(evals_list)
degs_arr = np.array(degs_list)

# Formula B at various cutoffs
for Lambda_label, Lambda_4D in [("M_Pl", M_PL_RED),
                                 ("10*M_KK", 10*M_KK_GN),
                                 ("100*M_KK", 100*M_KK_GN),
                                 ("3*M_KK", 3*M_KK_GN)]:
    m_k = evals_arr * M_KK_GN
    term_per_mode = Lambda_4D**2 - m_k**2 * np.log(1 + Lambda_4D**2 / m_k**2)
    inv_16piG_B = np.sum(degs_arr * term_per_mode) / (48 * np.pi**2)
    ratio = inv_16piG_B / INV_16piG_OBS
    log10_ratio = np.log10(abs(ratio))

    print(f"  Lambda = {Lambda_label:>10s} ({Lambda_4D:.4e} GeV):")
    print(f"    1/(16piG) = {inv_16piG_B:.4e} GeV^2, ratio = {ratio:.4f}, "
          f"log10|ratio| = {log10_ratio:+.3f}")

# Find Lambda where G_Sak = G_obs (exact crossover)
Lambda_scan = np.logspace(np.log10(M_KK_GN), np.log10(10*M_PL_RED), 500)
inv_sak_scan = np.zeros_like(Lambda_scan)
for i, Lam in enumerate(Lambda_scan):
    m_k = evals_arr * M_KK_GN
    term = Lam**2 - m_k**2 * np.log(1 + Lam**2 / m_k**2)
    inv_sak_scan[i] = np.sum(degs_arr * term) / (48 * np.pi**2)

# Find where ratio crosses 1
ratio_scan = inv_sak_scan / INV_16piG_OBS
idx_cross = np.argmin(np.abs(ratio_scan - 1.0))
Lambda_cross = Lambda_scan[idx_cross]

print(f"\n  Exact crossover (Formula B = observed G_N):")
print(f"    Lambda_cross = {Lambda_cross:.4e} GeV")
print(f"    Lambda_cross / M_KK = {Lambda_cross / M_KK_GN:.4f}")
print(f"    Lambda_cross / M_Pl = {Lambda_cross / M_PL_RED:.6f}")

# Refine with finer grid around crossover
Lambda_fine = np.linspace(Lambda_cross*0.8, Lambda_cross*1.2, 1000)
inv_fine = np.zeros_like(Lambda_fine)
for i, Lam in enumerate(Lambda_fine):
    m_k = evals_arr * M_KK_GN
    term = Lam**2 - m_k**2 * np.log(1 + Lam**2 / m_k**2)
    inv_fine[i] = np.sum(degs_arr * term) / (48 * np.pi**2)
ratio_fine = inv_fine / INV_16piG_OBS
idx_fine = np.argmin(np.abs(ratio_fine - 1.0))
Lambda_cross_fine = Lambda_fine[idx_fine]

print(f"    Refined: Lambda_cross = {Lambda_cross_fine:.6e} GeV")
print(f"    Lambda_cross / M_KK = {Lambda_cross_fine / M_KK_GN:.6f}")


# ===========================================================================
# Step 7: The central question -- can we identify a self-consistent scale?
# ===========================================================================
print(f"\n{'='*78}")
print("Step 7: Self-consistency analysis")
print("=" * 78)

# The question in the prompt: at N ~ (Lambda_eff/M_KK)^8 = 10^8,
# epsilon_c ~ 10^{-4}. Does this match the foam strength?
#
# (Lambda_eff/M_KK)^8 arises if we assume each Peter-Weyl sector
# contributes modes up to energy Lambda_eff, with N ~ (Lambda_eff/M_KK)^8
# from the density of states on SU(3) (dim 8, so N ~ (E/M_KK)^8).
#
# However, the actual PW mode count scales as N ~ L^5 (where L = max p+q),
# NOT as (Lambda/M_KK)^8. The maximum eigenvalue at truncation L grows
# roughly as L (the representation labels scale linearly with Casimir).
# So Lambda_max ~ L * M_KK, giving N ~ Lambda_max^5 / M_KK^5.
#
# Let's check the actual scaling.

# From S44 dissolution data, max_pq_sum vs N:
max_pq_arr = np.array([1, 2, 3, 4, 5], dtype=float)
N_actual = np.array([112, 432, 1232, 2912, 6048], dtype=float)

# Fit N = c * L^beta
from scipy.optimize import curve_fit

def power_model(L, c, beta):
    return c * L**beta

popt_NL, _ = curve_fit(power_model, max_pq_arr, N_actual, p0=[10, 5])
c_NL, beta_NL = popt_NL

print(f"\n  N_Hilbert(L) scaling:")
print(f"    Fit: N = {c_NL:.2f} * L^{beta_NL:.3f}")
print(f"    Expected for SU(3) (dim 8): N ~ L^5 (from Weyl's law on compact group)")
print(f"    Actual exponent: {beta_NL:.3f} (close to 5 as expected)")

# Now the 8-dimensional claim: if SU(3) is 8-dimensional,
# the Weyl asymptotic for the Dirac operator gives
# N(Lambda) ~ vol(S^*M) * Lambda^{dim} = const * Lambda^8 (for the cotangent bundle)
# But with Peter-Weyl, we're truncating by representation label L, not by eigenvalue.
# The eigenvalues scale as: lambda ~ sqrt(Casimir) ~ sqrt(L^2) ~ L
# So N ~ L^5 and Lambda ~ L gives N ~ Lambda^5, not Lambda^8.
#
# The discrepancy: 8 = dim(SU(3)) but N ~ L^5, not L^8.
# This is because Peter-Weyl truncation cuts by representation level,
# which captures FEWER modes than an energy cutoff would.
# The correct Weyl counting gives N ~ Lambda^8 for eigenvalue cutoff,
# while PW gives N ~ L^5 for rep-label cutoff.

# Check: at L=3, max eigenvalue
max_evals = []
for (p, q) in SECTORS:
    key = f'evals_tau0.190_{p}_{q}'
    if key not in d36.files:
        continue
    ev = d36[key]
    pos = ev[ev > 0.01]
    if len(pos) > 0:
        max_evals.append(np.max(pos))
lambda_max_L3 = max(max_evals) if max_evals else 0

print(f"\n  At L=3 (max_pq_sum=3):")
print(f"    Max eigenvalue (code units) = {lambda_max_L3:.4f}")
print(f"    Max eigenvalue (physical) = {lambda_max_L3 * M_KK_GN:.4e} GeV")
print(f"    Lambda_max / M_KK = {lambda_max_L3:.4f}")

# For the prompt's assertion: N ~ (Lambda_eff/M_KK)^8
# Let's compute what this would give
Lambda_eff_10MKK = 10 * M_KK_GN
N_prompt = (Lambda_eff_10MKK / M_KK_GN)**8  # = 10^8
epsilon_c_prompt = a_fit * N_prompt**(-alpha_fit)

print(f"\n  Prompt's scenario: N = (Lambda_eff/M_KK)^8 = (10)^8 = {N_prompt:.2e}")
print(f"    epsilon_c(10^8) = {a_fit:.4f} * (10^8)^(-{alpha_fit:.3f}) = {epsilon_c_prompt:.4e}")

# Compare to foam estimates
print(f"\n  Comparison to foam strengths:")
print(f"    epsilon_c(10^8) = {epsilon_c_prompt:.4e}")
print(f"    Left-invariant foam: {epsilon_left_inv:.4e}  -- ratio = {epsilon_c_prompt/epsilon_left_inv:.2f}")
print(f"    Holographic @ KK:    {delta_g_holographic_KK:.4e}  -- ratio = {epsilon_c_prompt/delta_g_holographic_KK:.2f}")

# The prompt's claim: epsilon_c ~ 10^{-4}
# Actual: epsilon_c(10^8) = 0.188 * (10^8)^{-0.457} = 0.188 * 10^{-3.66} = 0.188 * 2.19e-4 = 4.1e-5
# This is BELOW the left-invariant foam (10^{-4}) and ABOVE the holographic foam.

# Now check: does N ~ 10^8 correspond to L ~ (10^8)^{1/5} ~ 40?
L_from_10e8 = N_prompt**(1.0/beta_NL)
a0_from_L = a0_PW(int(min(L_from_10e8, 80)))

print(f"\n  At N=10^8:")
print(f"    Equivalent L (from N~L^{beta_NL:.1f}) = {L_from_10e8:.1f}")
print(f"    a_0 at L={int(min(L_from_10e8, 80))} = {a0_from_L}")

# Lambda_match at this L
Lambda_m_at_N8 = np.sqrt(48 * np.pi**2 * INV_16piG_OBS / a0_from_L)
print(f"    Lambda_match = {Lambda_m_at_N8:.4e} GeV")
print(f"    Lambda_match / M_KK = {Lambda_m_at_N8 / M_KK_GN:.4f}")
print(f"    Lambda_match / M_Pl = {Lambda_m_at_N8 / M_PL_RED:.6f}")


# ===========================================================================
# Step 8: Alternative scaling -- Weyl asymptotics N ~ Lambda^8
# ===========================================================================
print(f"\n{'='*78}")
print("Step 8: Weyl asymptotics N ~ Lambda^8 (eigenvalue cutoff)")
print("=" * 78)

# The correct Weyl asymptotic for the Dirac operator on a compact
# 8-dimensional manifold (cotangent bundle of SU(3)) gives:
#   N(Lambda) ~ c_W * Lambda^8
# where c_W = vol(S^*M) / (2pi)^8 * vol(SU(3)) / vol(S^7)
# For our discrete spectrum at L=3:
#   a_0 = 6440, lambda_max ~ 2.2 (code units)
#   c_W ~ 6440 / 2.2^8 ~ 6440 / 549 ~ 11.7
# This is the DISCRETE Weyl coefficient.

# Physical Weyl counting: if we had ALL modes up to Lambda/M_KK in code units
c_W_discrete = a0_fold / lambda_max_L3**8 if lambda_max_L3 > 0 else 0
print(f"\n  Discrete Weyl coefficient: c_W = a_0/lambda_max^8 = {c_W_discrete:.2f}")
print(f"    (Using a_0={a0_fold:.0f}, lambda_max={lambda_max_L3:.4f})")

# With Weyl asymptotics: N(Lambda) = c_W * (Lambda/M_KK)^8
# Then epsilon_c(Lambda) = a_fit * [c_W * (Lambda/M_KK)^8]^{-alpha_fit}

Lambda_over_MKK = np.logspace(0, 3, 200)  # 1 to 1000
N_weyl = c_W_discrete * Lambda_over_MKK**8
eps_c_weyl = a_fit * N_weyl**(-alpha_fit)

# Also compute Sakharov G_N ratio at each Lambda (leading term only)
# 1/(16piG) ~ (N/48pi^2) * Lambda^2
# Ratio to observed: (N/48pi^2 * Lambda^2) / INV_16piG_OBS
# With N = c_W * (Lambda/M_KK)^8 and physical Lambda = (Lambda/M_KK)*M_KK:
ratio_sak_weyl = (N_weyl / (48 * np.pi**2)) * (Lambda_over_MKK * M_KK_GN)**2 / INV_16piG_OBS

# Find crossover: where Sakharov = observed (ratio = 1)
idx_sak_cross = np.argmin(np.abs(ratio_sak_weyl - 1.0))
Lambda_sak_weyl_cross = Lambda_over_MKK[idx_sak_cross]

# And where epsilon_c = various foam thresholds
for name, eps in foam_scenarios.items():
    N_c = N_crit_from_eps(eps, a_fit, alpha_fit)
    Lambda_c_over_MKK = (N_c / c_W_discrete)**(1.0/8.0)
    ratio_sak_at_c = (N_c / (48 * np.pi**2)) * (Lambda_c_over_MKK * M_KK_GN)**2 / INV_16piG_OBS

    print(f"\n  {name}: epsilon_phys = {eps:.4e}")
    print(f"    N_crit = {N_c:.2e}")
    print(f"    Lambda_diss/M_KK = {Lambda_c_over_MKK:.2f}")
    print(f"    Sakharov ratio at this scale = {ratio_sak_at_c:.2e}")

# Key result: at the holographic foam scale
N_crit_hol_2 = N_crit_from_eps(delta_g_holographic_KK, a_fit, alpha_fit)
Lambda_diss_hol = (N_crit_hol_2 / c_W_discrete)**(1.0/8.0) * M_KK_GN

print(f"\n  Key results:")
print(f"    Sakharov crossover (G_Sak=G_obs):    Lambda/M_KK = {Lambda_sak_weyl_cross:.2f}")
print(f"    Dissolution crossover (hol. foam):    Lambda/M_KK = {(N_crit_hol_2/c_W_discrete)**(1.0/8.0):.2f}")
print(f"    Dissolution energy:                   {Lambda_diss_hol:.4e} GeV")
print(f"    Ratio (Sakharov / dissolution):       {Lambda_sak_weyl_cross / (N_crit_hol_2/c_W_discrete)**(1.0/8.0):.4f}")


# ===========================================================================
# Step 9: The emergence picture
# ===========================================================================
print(f"\n{'='*78}")
print("Step 9: Physical interpretation -- the emergence picture")
print("=" * 78)

# At scale Lambda >> Lambda_diss:
#   - epsilon_c << epsilon_phys: spectral triple dissolved, foam dominates
#   - No well-defined Dirac spectrum, no Peter-Weyl structure
#   - Sakharov formula meaningless (no well-defined modes to sum over)
#
# At scale Lambda ~ Lambda_diss:
#   - epsilon_c ~ epsilon_phys: spectral triple crystallizes
#   - Block-diagonal structure of D_K becomes robust
#   - Sakharov formula becomes applicable
#   - The EFFECTIVE UV cutoff IS Lambda_diss
#
# At scale Lambda << Lambda_diss:
#   - epsilon_c >> epsilon_phys: spectral triple fully formed
#   - Modes are sharp, Sakharov formula well-defined
#   - But only modes up to Lambda_diss contribute (higher modes dissolved)
#
# PREDICTION: G_N = sum over modes up to Lambda_diss (not M_Pl!)

# Compute G_N with Lambda = Lambda_diss_hol
if Lambda_diss_hol > M_KK_GN:
    m_k = evals_arr * M_KK_GN
    # Only count modes with m_k < Lambda_diss_hol
    mask = m_k < Lambda_diss_hol
    term_diss = Lambda_diss_hol**2 - m_k[mask]**2 * np.log(1 + Lambda_diss_hol**2 / m_k[mask]**2)
    inv_16piG_diss = np.sum(degs_arr[mask] * term_diss) / (48 * np.pi**2)
    ratio_diss = inv_16piG_diss / INV_16piG_OBS

    print(f"\n  Sakharov G_N with Lambda = Lambda_diss (hol):")
    print(f"    Lambda_diss = {Lambda_diss_hol:.4e} GeV = {Lambda_diss_hol/M_KK_GN:.2f} * M_KK")
    print(f"    Modes contributing (m_k < Lambda_diss): {np.sum(mask)} / {len(m_k)}")
    print(f"    1/(16piG) = {inv_16piG_diss:.4e} GeV^2")
    print(f"    Ratio to observed: {ratio_diss:.4f}")
    print(f"    log10|ratio|: {np.log10(abs(ratio_diss)):+.3f}")
else:
    inv_16piG_diss = 0
    ratio_diss = 0
    print(f"\n  Lambda_diss < M_KK -- no modes contribute. G_N undefined.")

# Also with Lambda_cross_fine (where G_Sak = G_obs exactly)
print(f"\n  For reference:")
print(f"    Lambda at which G_Sak = G_obs: {Lambda_cross_fine:.4e} GeV = {Lambda_cross_fine/M_KK_GN:.4f} * M_KK")

# Self-consistency check: does the dissolution scale at L=3 (our data)
# match the Lambda_cross?
eps_c_at_L3 = a_fit * 6048**(-alpha_fit)  # L=5 (largest measured)
eps_c_at_current = eps_c_extrap[2]  # L=3

print(f"\n  Self-consistency at current truncation (L=3):")
print(f"    epsilon_c(L=3, N=1232) = {eps_c_extrap[2]:.4e}")
print(f"    Generic foam strength:   {epsilon_generic:.4e}")
print(f"    Ratio eps_foam/eps_c:    {epsilon_generic/eps_c_extrap[2]:.1f}")
print(f"    Status: foam {'EXCEEDS' if epsilon_generic > eps_c_extrap[2] else 'BELOW'} dissolution threshold")
print(f"    => Spectral triple at L=3 IS dissolved by generic foam (as found in DISSOLUTION-43)")


# ===========================================================================
# Step 10: Scaling relations summary
# ===========================================================================
print(f"\n{'='*78}")
print("Step 10: Scaling relations and dimensional analysis")
print("=" * 78)

# Key scaling relations:
# (1) epsilon_c(N) = 0.188 * N^{-0.457}
# (2) N(L) ~ 10.3 * L^4.94 (Peter-Weyl)
# (3) Lambda_match(L) = sqrt(48*pi^2 * M_Pl^2 / (2*a_0(L)))
# (4) a_0(L) ~ 8 * sum dim(p,q)^2 up to L
#
# The SELF-CONSISTENT emergence picture:
# Lambda_emergence is set by epsilon_c(N(Lambda_emergence)) = epsilon_foam
# This is a FIXED POINT equation in Lambda (given the foam model).
#
# For holographic foam: epsilon_foam = (l_P * Lambda)^{2/3}
# (evaluated at scale 1/Lambda)
# Combined with epsilon_c = a * N^{-alpha} and N = c_W * (Lambda/M_KK)^8:
#
# (l_P * Lambda)^{2/3} = a * [c_W * (Lambda/M_KK)^8]^{-alpha}
# Let x = Lambda/M_KK:
# (l_P * M_KK * x)^{2/3} = a * (c_W * x^8)^{-alpha}
# (l_P * M_KK)^{2/3} * x^{2/3} = a * c_W^{-alpha} * x^{-8*alpha}
# x^{2/3 + 8*alpha} = a * c_W^{-alpha} / (l_P * M_KK)^{2/3}

exponent = 2.0/3.0 + 8 * alpha_fit
l_P_MKK = L_PLANCK_M * M_KK_GN * 5.068e15  # dimensionless l_P * M_KK in natural units
# More carefully: l_P * M_KK = (l_P [m]) * (M_KK [GeV]) * (GeV_to_inv_m)
# l_P [m] * GeV_to_inv_m [m^{-1}/GeV] = l_P * 5.068e15 = dimensionless (l_P/lambda_compton)
# Actually l_P * M_KK in natural units = M_KK / M_Pl = M_KK_GN / M_PL_RED (reduced)
l_P_MKK_nat = M_KK_GN / M_PL_RED  # = 0.0305

rhs = a_fit * c_W_discrete**(-alpha_fit) / l_P_MKK_nat**(2.0/3.0)
x_star = rhs**(1.0/exponent)
Lambda_star = x_star * M_KK_GN

print(f"\n  Self-consistent fixed-point equation:")
print(f"    (l_P * Lambda)^(2/3) = {a_fit:.4f} * [{c_W_discrete:.2f} * (Lambda/M_KK)^8]^(-{alpha_fit:.3f})")
print(f"    => (Lambda/M_KK)^({exponent:.3f}) = {rhs:.4e}")
print(f"    => Lambda/M_KK = {x_star:.4f}")
print(f"    => Lambda_emergence = {Lambda_star:.4e} GeV")
print(f"    => Lambda_emergence / M_Pl = {Lambda_star / M_PL_RED:.6f}")
print(f"\n  Key physical scales:")
print(f"    M_KK            = {M_KK_GN:.4e} GeV")
print(f"    Lambda_emergence = {Lambda_star:.4e} GeV = {x_star:.2f} * M_KK")
print(f"    M_Pl             = {M_PL_RED:.4e} GeV")
print(f"\n  Exponent: 2/3 + 8*alpha = {exponent:.3f}")
print(f"  l_P * M_KK (nat) = M_KK/M_Pl = {l_P_MKK_nat:.6f}")

# N at emergence:
N_emergence = c_W_discrete * x_star**8
eps_at_emergence = a_fit * N_emergence**(-alpha_fit)
foam_at_emergence = l_P_MKK_nat**(2.0/3.0) * x_star**(2.0/3.0)

print(f"\n  At Lambda_emergence:")
print(f"    N = c_W * x^8 = {N_emergence:.4e}")
print(f"    epsilon_c(N) = {eps_at_emergence:.4e}")
print(f"    epsilon_foam = (l_P*Lambda)^(2/3) = {foam_at_emergence:.4e}")
print(f"    Ratio epsilon_c/epsilon_foam = {eps_at_emergence/foam_at_emergence:.4f}")
print(f"    (Should be 1.0 by construction: {'PASS' if abs(eps_at_emergence/foam_at_emergence - 1.0) < 0.01 else 'CHECK'})")

# Sakharov G_N at Lambda_emergence
inv_16piG_emergence = (N_emergence / (48 * np.pi**2)) * Lambda_star**2
ratio_emergence = inv_16piG_emergence / INV_16piG_OBS

print(f"\n  Sakharov G_N at Lambda_emergence (leading term):")
print(f"    1/(16piG) = {inv_16piG_emergence:.4e} GeV^2")
print(f"    Ratio to observed: {ratio_emergence:.4e}")
print(f"    log10(ratio): {np.log10(abs(ratio_emergence)):+.2f}")

# For the PW truncation (not Weyl): what L gives this N?
L_emergence_PW = (N_emergence / c_NL)**(1.0/beta_NL)
print(f"    Equivalent PW truncation: L ~ {L_emergence_PW:.1f}")


# ===========================================================================
# Step 11: Gate verdict
# ===========================================================================
print(f"\n{'='*78}")
print("GATE VERDICT: SAKHAROV-UV-DISSOLUTION-45")
print("=" * 78)

# Summarize the quantitative findings
print(f"""
KEY FINDINGS:

1. DISSOLUTION SCALING (S44 W6-7):
   epsilon_c(N) = {a_fit:.4f} * N^(-{alpha_fit:.4f}), R^2 = {R2_power:.4f}

2. SAKHAROV UV CUTOFF (S44 W1-1, corrected):
   Lambda where G_Sak = G_obs: {Lambda_cross_fine:.4e} GeV = {Lambda_cross_fine/M_KK_GN:.4f} M_KK
   (At Lambda=M_Pl, G_Sak overshoots by {ratio_B:.1f}x)

3. SELF-CONSISTENT EMERGENCE SCALE (holographic foam):
   Lambda_emergence = {Lambda_star:.4e} GeV = {x_star:.2f} * M_KK
   N_emergence = {N_emergence:.2e}
   epsilon_c = epsilon_foam = {eps_at_emergence:.4e}

4. SAKHAROV G_N AT EMERGENCE SCALE:
   1/(16piG) = {inv_16piG_emergence:.4e} GeV^2
   Ratio to observed: {ratio_emergence:.2e} ({np.log10(abs(ratio_emergence)):+.1f} dex)

5. DIMENSIONAL ANALYSIS SCALING:
   Lambda_emergence/M_KK = (a/c_W^alpha * M_Pl^(2/3) / M_KK^(2/3))^(1/(2/3+8*alpha))
   Exponent = 2/3 + 8*alpha = {exponent:.3f}
   This is a PREDICTION from the foam model + dissolution scaling.

6. THE THREE SCALES:
   M_KK = {M_KK_GN:.2e} GeV  (compactification)
   Lambda_cross = {Lambda_cross_fine:.2e} GeV  (Sakharov = observed, L=3)
   Lambda_emergence = {Lambda_star:.2e} GeV  (dissolution = foam, Weyl)
   M_Pl = {M_PL_RED:.2e} GeV  (Planck)
""")

# The Sakharov formula at L=3 (6440 modes) gives G_obs at Lambda ≈ {Lambda_cross_fine/M_KK_GN:.1f}*M_KK.
# The dissolution emergence scale is at Lambda ≈ {x_star:.1f}*M_KK.
# These are {Lambda_cross_fine/Lambda_star:.1f}x apart.

scale_ratio = Lambda_cross_fine / Lambda_star
print(f"  RATIO Lambda_cross / Lambda_emergence = {scale_ratio:.2f}")

# The question: is there a QUANTITATIVE RELATIONSHIP?
# The Sakharov crossover depends on a_0 (species count at L=3 truncation).
# The emergence scale depends on c_W (Weyl coefficient extrapolated).
# These are BOTH extrapolations from the same L=3 spectrum.
# A self-consistent picture requires extending the spectrum to higher L.

# Verdict
if abs(np.log10(scale_ratio)) < 1.0:
    verdict = "INFO"
    detail = (f"Lambda_cross and Lambda_emergence within {abs(np.log10(scale_ratio)):.2f} dex. "
              f"Quantitative relationship exists but requires higher-L computation to verify.")
elif abs(np.log10(scale_ratio)) < 2.0:
    verdict = "INFO"
    detail = (f"Scales differ by {abs(np.log10(scale_ratio)):.2f} dex. "
              f"Qualitative relationship (both ~ few * M_KK) but no quantitative match.")
else:
    verdict = "INFO"
    detail = (f"Scales differ by {abs(np.log10(scale_ratio)):.1f} dex. "
              f"No quantitative relationship at current truncation.")

print(f"\n  GATE VERDICT: {verdict}")
print(f"    {detail}")


# ===========================================================================
# Step 12: Save data
# ===========================================================================
print(f"\n--- Saving results ---")

np.savez(DATA_DIR / 's45_sakharov_dissolution.npz',
    # Input parameters
    tau_fold=TAU_FOLD,
    M_KK_GN=M_KK_GN,
    M_PL_RED=M_PL_RED,
    a_fit=a_fit,
    alpha_fit=alpha_fit,
    R2_power=R2_power,

    # Scaling
    L_vals=L_vals,
    N_hilbert=N_hilbert,
    N_a0=N_a0,
    eps_c_extrap=eps_c_extrap,
    Lambda_match=Lambda_match,

    # Mode count scaling
    c_NL=c_NL,
    beta_NL=beta_NL,
    c_W_discrete=c_W_discrete,

    # Foam strengths
    epsilon_left_inv=epsilon_left_inv,
    delta_g_holographic_KK=delta_g_holographic_KK,
    delta_g_randomwalk_KK=delta_g_randomwalk_KK,
    epsilon_effaced_holographic=epsilon_effaced_holographic,

    # Sakharov crossover (Formula B at L=3)
    Lambda_cross_fine=Lambda_cross_fine,
    Lambda_cross_over_MKK=Lambda_cross_fine / M_KK_GN,

    # Self-consistent emergence
    Lambda_emergence=Lambda_star,
    Lambda_emergence_over_MKK=x_star,
    N_emergence=N_emergence,
    eps_at_emergence=eps_at_emergence,
    foam_at_emergence=foam_at_emergence,
    exponent_selfconsistent=exponent,
    inv_16piG_emergence=inv_16piG_emergence,
    ratio_emergence=ratio_emergence,

    # Sakharov formula B at various cutoffs
    ratio_B_MPl=ratio_B,
    log10_dev_B=log10_dev_B,
    Lambda_cross_scan=Lambda_scan,
    ratio_sak_scan=ratio_scan,
    inv_sak_scan=inv_sak_scan,

    # Weyl extrapolation
    Lambda_over_MKK_weyl=Lambda_over_MKK,
    N_weyl=N_weyl,
    eps_c_weyl=eps_c_weyl,
    ratio_sak_weyl=ratio_sak_weyl,

    # Scale comparison
    scale_ratio=scale_ratio,

    # Gate
    gate_name=np.array(['SAKHAROV-UV-DISSOLUTION-45']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"  Saved: tier0-computation/s45_sakharov_dissolution.npz")


# ===========================================================================
# Step 13: Plot
# ===========================================================================
print(f"  Generating plot...")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, hspace=0.4, wspace=0.35)

# --- Panel 1: epsilon_c and foam strengths vs N ---
ax1 = fig.add_subplot(gs[0, 0])
# Dissolution data
ax1.plot(N_diss, eps_diss, 'ko', markersize=10, zorder=5, label='Measured $\\epsilon_c$')
# Extrapolation
ax1.plot(N_hilbert, eps_c_extrap, 'b--', lw=1.5, alpha=0.7,
         label=f'$\\epsilon_c = {a_fit:.3f} N^{{-{alpha_fit:.3f}}}$')
# Foam thresholds
ax1.axhline(epsilon_left_inv, color='red', ls=':', lw=1.5, label=f'Left-inv foam ($10^{{-4}}$)')
ax1.axhline(delta_g_holographic_KK, color='orange', ls='-.', lw=1.5,
            label=f'Holographic @ $l_{{KK}}$ ({delta_g_holographic_KK:.1e})')
ax1.set_xscale('log')
ax1.set_yscale('log')
ax1.set_xlabel('$N$ (Hilbert space dimension)', fontsize=11)
ax1.set_ylabel('$\\epsilon$', fontsize=13)
ax1.set_title('Dissolution vs Foam Strength', fontsize=12)
ax1.legend(fontsize=7, loc='upper right')
ax1.grid(True, alpha=0.3)

# Mark N_crit for holographic
N_crit_hol_final = N_crit_from_eps(delta_g_holographic_KK, a_fit, alpha_fit)
ax1.axvline(N_crit_hol_final, color='orange', ls=':', alpha=0.5)

# --- Panel 2: Lambda_match vs L ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(L_vals, Lambda_match / M_KK_GN, 'b-', lw=2, label='$\\Lambda_{match}/M_{KK}$')
ax2.axhline(Lambda_cross_fine / M_KK_GN, color='green', ls='--', lw=1.5,
            label=f'$\\Lambda_{{cross}}$ (Formula B) = {Lambda_cross_fine/M_KK_GN:.1f}')
ax2.axhline(x_star, color='red', ls=':', lw=1.5,
            label=f'$\\Lambda_{{emerg}}$ = {x_star:.1f} $M_{{KK}}$')
ax2.axhline(M_PL_RED / M_KK_GN, color='gray', ls='-.', alpha=0.5,
            label=f'$M_{{Pl}}/M_{{KK}}$ = {M_PL_RED/M_KK_GN:.0f}')
ax2.set_xlabel('$L$ (max $p+q$)', fontsize=11)
ax2.set_ylabel('$\\Lambda_{match} / M_{KK}$', fontsize=12)
ax2.set_title('Sakharov Matching Scale', fontsize=12)
ax2.set_yscale('log')
ax2.legend(fontsize=7)
ax2.grid(True, alpha=0.3)

# --- Panel 3: Dual-axis -- epsilon_c and Lambda_match vs L ---
ax3 = fig.add_subplot(gs[0, 2])
color_eps = 'blue'
color_lam = 'red'
ax3_twin = ax3.twinx()

ax3.plot(L_vals, eps_c_extrap, color=color_eps, lw=2, label='$\\epsilon_c(L)$')
ax3.set_ylabel('$\\epsilon_c$', color=color_eps, fontsize=12)
ax3.tick_params(axis='y', labelcolor=color_eps)
ax3.set_yscale('log')

ax3_twin.plot(L_vals, Lambda_match / M_KK_GN, color=color_lam, lw=2, ls='--',
              label='$\\Lambda_{match}/M_{KK}$')
ax3_twin.set_ylabel('$\\Lambda_{match}/M_{KK}$', color=color_lam, fontsize=12)
ax3_twin.tick_params(axis='y', labelcolor=color_lam)
ax3_twin.set_yscale('log')

ax3.set_xlabel('$L$ (max $p+q$)', fontsize=11)
ax3.set_title('Dissolution vs UV Cutoff', fontsize=12)
ax3.grid(True, alpha=0.3)

# --- Panel 4: Sakharov Formula B ratio vs Lambda ---
ax4 = fig.add_subplot(gs[1, 0])
valid = ratio_scan > 0
ax4.plot(Lambda_scan[valid] / M_KK_GN, ratio_scan[valid], 'b-', lw=2)
ax4.axhline(1.0, color='green', ls='--', lw=1.5, label='$G_{Sak} = G_{obs}$')
ax4.axvline(Lambda_cross_fine / M_KK_GN, color='green', ls=':', alpha=0.5)
ax4.axvline(x_star, color='red', ls=':', alpha=0.5, label=f'$\\Lambda_{{emerg}}$')
ax4.set_xlabel('$\\Lambda / M_{KK}$', fontsize=11)
ax4.set_ylabel('$G_N^{Sak} / G_N^{obs}$', fontsize=12)
ax4.set_title('Sakharov Ratio (Formula B)', fontsize=12)
ax4.set_xscale('log')
ax4.set_yscale('log')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

# --- Panel 5: Weyl extrapolation ---
ax5 = fig.add_subplot(gs[1, 1])
ax5.plot(Lambda_over_MKK, eps_c_weyl, 'b-', lw=2, label='$\\epsilon_c(\\Lambda)$ (Weyl)')
ax5.axhline(delta_g_holographic_KK, color='orange', ls='-.', lw=1.5,
            label=f'Holographic foam')
ax5.axhline(epsilon_left_inv, color='red', ls=':', lw=1.5, label='Left-inv foam')

# Also plot foam strength as function of Lambda
foam_curve = l_P_MKK_nat**(2.0/3.0) * Lambda_over_MKK**(2.0/3.0)
ax5.plot(Lambda_over_MKK, foam_curve, 'r--', lw=1.5, alpha=0.7,
         label='$(l_P \\Lambda)^{2/3}$ foam')

ax5.set_xlabel('$\\Lambda / M_{KK}$', fontsize=11)
ax5.set_ylabel('$\\epsilon$', fontsize=13)
ax5.set_title('Dissolution vs Foam (Weyl)', fontsize=12)
ax5.set_xscale('log')
ax5.set_yscale('log')
ax5.legend(fontsize=7)
ax5.grid(True, alpha=0.3)

# Mark crossover
# Find where eps_c_weyl = foam_curve
ratio_eps_foam = eps_c_weyl / foam_curve
idx_ef_cross = np.argmin(np.abs(np.log10(ratio_eps_foam)))
ax5.axvline(Lambda_over_MKK[idx_ef_cross], color='purple', ls=':', alpha=0.5)

# --- Panel 6: N(L) and a_0(L) ---
ax6 = fig.add_subplot(gs[1, 2])
ax6.plot(L_vals, N_hilbert, 'b-', lw=2, label='$N_{Hilbert}$')
ax6.plot(L_vals, N_a0, 'r--', lw=2, label='$a_0$ (PW-weighted)')
ax6.set_xlabel('$L$ (max $p+q$)', fontsize=11)
ax6.set_ylabel('Mode count', fontsize=12)
ax6.set_title('Mode Count vs Truncation', fontsize=12)
ax6.set_yscale('log')
ax6.legend(fontsize=9)
ax6.grid(True, alpha=0.3)

# --- Panel 7: The emergence diagram ---
ax7 = fig.add_subplot(gs[2, :])
# Energy scale axis
E_vals = np.logspace(np.log10(M_KK_GN), np.log10(10*M_PL_RED), 500)
E_over_MKK = E_vals / M_KK_GN

# Plot regions
ax7.axvspan(M_KK_GN, Lambda_star, alpha=0.1, color='blue', label='Spectral triple regime')
ax7.axvspan(Lambda_star, M_PL_RED, alpha=0.1, color='red', label='Dissolution regime')
ax7.axvspan(M_PL_RED, 10*M_PL_RED, alpha=0.1, color='gray', label='Planck regime')

# Mark key scales
for E, label, color in [(M_KK_GN, '$M_{KK}$', 'blue'),
                          (Lambda_cross_fine, '$\\Lambda_{cross}$', 'green'),
                          (Lambda_star, '$\\Lambda_{emerg}$', 'red'),
                          (M_PL_RED, '$M_{Pl}$', 'black')]:
    ax7.axvline(E, color=color, ls='--', lw=2, alpha=0.7)
    ax7.text(E, 0.95, label, color=color, fontsize=10, ha='center', va='top',
             transform=ax7.get_xaxis_transform(), fontweight='bold')

ax7.set_xlabel('Energy (GeV)', fontsize=12)
ax7.set_xscale('log')
ax7.set_xlim(M_KK_GN * 0.5, M_PL_RED * 3)
ax7.set_yticks([])
ax7.set_title('Emergence Diagram: Spectral Triple Crystallization', fontsize=13)
ax7.legend(fontsize=9, loc='lower right')

# Add text annotations
ax7.text(np.sqrt(M_KK_GN * Lambda_star), 0.5,
         'Block-diagonal D$_K$\nWell-defined modes\nSakharov sum converges',
         ha='center', va='center', fontsize=9, transform=ax7.get_xaxis_transform(),
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue', alpha=0.5))
ax7.text(np.sqrt(Lambda_star * M_PL_RED), 0.5,
         'Foam dissolves D$_K$\nNo well-defined spectrum\nPre-geometric phase',
         ha='center', va='center', fontsize=9, transform=ax7.get_xaxis_transform(),
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.5))

fig.suptitle('SAKHAROV-UV-DISSOLUTION-45\nConnecting UV Cutoff to Spectral Triple Emergence',
             fontsize=14, fontweight='bold')

plt.savefig(DATA_DIR / 's45_sakharov_dissolution.png', dpi=150, bbox_inches='tight')
print(f"  Saved: tier0-computation/s45_sakharov_dissolution.png")

t_total = 0  # no timing wrapper
print(f"\n{'='*78}")
print("COMPUTATION COMPLETE")
print("=" * 78)
