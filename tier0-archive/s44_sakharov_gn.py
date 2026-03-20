#!/usr/bin/env python3
"""
SAKHAROV-GN-44: G_N from Sakharov induced gravity vs spectral action a_2.

Computes G_N from two independent formulae using the 992-mode KK spectrum:
  1. Sakharov (logarithmic):  1/(16 pi G_N^Sak) = (1/2) sum_k d_k ln(Lambda^2/lambda_k^2)
  2. Spectral action (poly):  1/(16 pi G_N^spec) = (4/pi^2) f_2 Lambda^2 a_2^K

The Sakharov formula follows Volovik Paper 07 (1994) and Paper 30 (2022):
gravity is INDUCED by fermionic quantum loops. The gravitating quantity
is the trace-log of the Dirac propagator, not the polynomial spectral action.

Gate: PASS if |log10(G_N^Sak / G_N^obs)| < 2 (within 2 OOM)
      FAIL if |log10(G_N^Sak / G_N^obs)| > 3
      BONUS if |log10(G_N^Sak / G_N^spec)| < 1

Input: tier0-computation/s36_sfull_tau_stabilization.npz (eigenvalues at tau=0.190)
       tier0-computation/s42_constants_snapshot.npz (M_KK, a_2, etc.)
       tier0-computation/s42_hauser_feshbach.npz (reference masses)

Output: tier0-computation/s44_sakharov_gn.npz, s44_sakharov_gn.png
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

DATA_DIR = Path(__file__).parent

# ==========================================================================
#  Physical constants
# ==========================================================================
from canonical_constants import G_N as G_N_OBS  # m^3 kg^-1 s^-2
from canonical_constants import M_Pl_reduced as M_PL_REDUCED  # GeV
from canonical_constants import M_Pl_unreduced as M_PL_UNREDUCED  # 1.2209e19 GeV
from canonical_constants import GeV_to_inv_m as GEV_TO_INVMETERS  # m^-1 per GeV
# G_N in natural units: G_N = 1/(8 pi M_Pl_red^2)
G_N_NAT = 1.0 / (8.0 * np.pi * M_PL_REDUCED**2)  # GeV^{-2}

print("=" * 78)
print("SAKHAROV-GN-44: Induced Gravity from 992 KK Modes")
print("=" * 78)

# ==========================================================================
#  Step 0: Load spectrum data
# ==========================================================================

d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d42c = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)
d42h = np.load(DATA_DIR / 's42_hauser_feshbach.npz', allow_pickle=True)

# Key values from S42
a0_fold = float(d42c['a0_fold'])        # 6440 (total Peter-Weyl count)
a2_fold = float(d42c['a2_fold'])        # 2776.165 (spectral zeta, PW-weighted)
a4_fold = float(d42c['a4_fold'])        # 1350.722
M_KK_GN = float(d42c['M_KK_from_GN'])  # 7.43e16 GeV
M_KK_K = float(d42c['M_KK_kerner'])    # 5.04e17 GeV
tau_fold = 0.19

print(f"\nLoaded S42 data:")
print(f"  a_0(fold) = {a0_fold:.1f}")
print(f"  a_2(fold) = {a2_fold:.4f}")
print(f"  a_4(fold) = {a4_fold:.4f}")
print(f"  M_KK (from G_N route) = {M_KK_GN:.4e} GeV")
print(f"  M_KK (Kerner route)   = {M_KK_K:.4e} GeV")

# ==========================================================================
#  Step 1: Build full spectrum with Peter-Weyl degeneracies
# ==========================================================================
# Use S36 eigenvalues at tau=0.190 with right-regular degeneracy

def dim_pq(p, q):
    """Dimension of SU(3) irrep (p, q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]

print(f"\n{'='*78}")
print("STEP 1: Build full KK spectrum with Peter-Weyl degeneracies")
print("=" * 78)

# Collect all (positive eigenvalue, total PW degeneracy) pairs
all_pos_evals = []
all_pw_degs = []
sector_info = {}

for (p, q) in SECTORS:
    key = f'evals_tau0.190_{p}_{q}'
    if key not in d36.files:
        print(f"  WARNING: sector ({p},{q}) not found at tau=0.190")
        continue

    evals = d36[key]
    pos = evals[evals > 0.01]  # cutoff consistent with S41
    deg = dim_pq(p, q)         # right-regular degeneracy per stored eigenvalue

    sector_info[(p, q)] = {
        'n_stored': len(evals),
        'n_pos': len(pos),
        'dim_rep': deg,
        'a0_contrib': deg * len(pos),
        'a2_contrib': deg * np.sum(pos**(-2)),
        'min_pos': np.min(pos) if len(pos) > 0 else np.inf,
        'max_pos': np.max(pos) if len(pos) > 0 else 0,
    }

    for lam in pos:
        all_pos_evals.append(lam)
        all_pw_degs.append(deg)

all_pos_evals = np.array(all_pos_evals)
all_pw_degs = np.array(all_pw_degs)

print(f"\nSector breakdown:")
print(f"{'(p,q)':>7s}  {'dim':>4s}  {'n_pos':>6s}  {'a0':>8s}  {'a2':>12s}  {'min':>8s}  {'max':>8s}")
for (p, q) in SECTORS:
    if (p, q) in sector_info:
        s = sector_info[(p, q)]
        print(f"  ({p},{q})  {s['dim_rep']:4d}  {s['n_pos']:6d}  {s['a0_contrib']:8.0f}  "
              f"{s['a2_contrib']:12.4f}  {s['min_pos']:8.4f}  {s['max_pos']:8.4f}")

total_a0 = np.sum(all_pw_degs)
total_a2 = np.sum(all_pw_degs * all_pos_evals**(-2))
total_a4 = np.sum(all_pw_degs * all_pos_evals**(-4))

print(f"\nTotal spectral sums (10 sectors, PW-weighted):")
print(f"  a_0 = {total_a0:.1f}   (S41: {a0_fold:.1f})  check: {'PASS' if abs(total_a0 - a0_fold) < 0.5 else 'FAIL'}")
print(f"  a_2 = {total_a2:.4f}  (S41: {a2_fold:.4f})  check: {'PASS' if abs(total_a2 - a2_fold) < 0.01 else 'FAIL'}")
print(f"  a_4 = {total_a4:.4f}  (S41: {a4_fold:.4f})  check: {'PASS' if abs(total_a4 - a4_fold) < 0.01 else 'FAIL'}")

N_modes = int(total_a0)  # = 6440 effective PW-weighted modes

# Also build unique mass list for compact storage
unique_masses_dict = {}
for lam, deg in zip(all_pos_evals, all_pw_degs):
    lam_r = round(lam, 7)
    if lam_r not in unique_masses_dict:
        unique_masses_dict[lam_r] = 0
    unique_masses_dict[lam_r] += deg

unique_lams = np.array(sorted(unique_masses_dict.keys()))
unique_degs = np.array([unique_masses_dict[l] for l in unique_lams])
print(f"\n  Unique mass values: {len(unique_lams)} (with PW degeneracies summing to {np.sum(unique_degs)})")

# ==========================================================================
#  Step 2: Sakharov induced gravity formula
# ==========================================================================
# Following Volovik Paper 07 (1994):
#   1/(16 pi G_N^{Sak}) = (1/2) sum_k d_k ln(Lambda^2 / lambda_k^2)
#
# where lambda_k = |eigenvalue_k| * M_KK (physical eigenvalue)
# and d_k = Peter-Weyl degeneracy
#
# Since lambda_k^{phys} = lambda_k^{code} * M_KK, we get:
#   ln(Lambda^2/lambda_k^{phys,2}) = ln(Lambda^2/(lambda_k^{code,2} * M_KK^2))
#                                   = ln(Lambda^2/M_KK^2) - 2*ln(lambda_k^{code})
#
# So: 1/(16 pi G_N^{Sak}) = (1/2) * [a_0 * ln(Lambda^2/M_KK^2)
#                                      - 2 * sum_k d_k * ln(lambda_k^{code})]
#
# The log-sum is purely from the CODE spectrum:
#   S_log = sum_k d_k * ln(lambda_k^{code})  (sum over positive eigenvalues)

print(f"\n{'='*78}")
print("STEP 2: Sakharov Induced Gravity Formula")
print("=" * 78)

S_log = np.sum(all_pw_degs * np.log(all_pos_evals))
print(f"\n  Log-spectral sum: S_log = sum d_k ln(lambda_k) = {S_log:.6f}")
print(f"  Mean log eigenvalue: S_log / a_0 = {S_log / total_a0:.6f}")
print(f"  Geometric mean eigenvalue: exp(S_log/a_0) = {np.exp(S_log / total_a0):.6f}")

# Compute 1/(16 pi G_N^Sak) at three cutoffs
cutoffs_labels = {
    'M_Pl': M_PL_REDUCED,
    '100*M_KK(GN)': 100.0 * M_KK_GN,
    '10*M_KK(GN)': 10.0 * M_KK_GN,
    'M_KK(GN)': M_KK_GN,
    'M_KK(Kerner)': M_KK_K,
    '10*M_KK(K)': 10.0 * M_KK_K,
}

print(f"\nSakharov G_N at various UV cutoffs Lambda:")
print(f"{'Cutoff':>18s}  {'Lambda (GeV)':>14s}  {'1/(16piG_Sak)':>20s}  {'G_Sak^{-1/2} (GeV)':>20s}  "
      f"{'log10(G_Sak/G_obs)':>20s}")

results_sak = {}

for label, Lambda in cutoffs_labels.items():
    # 1/(16 pi G_N^Sak) = (1/2) [a_0 * ln(Lambda^2/M_KK^2) - 2*S_log]
    # with M_KK = M_KK_GN (gravity route)
    # Physical eigenvalues: lambda_phys = lambda_code * M_KK
    # 1/(16piG) = (1/2) sum d_k ln(Lambda^2 / (lambda_code_k * M_KK)^2)
    #           = (1/2) * {a_0 * [ln(Lambda^2) - ln(M_KK^2)] - 2*S_log}
    #           = (1/2) * {a_0 * ln(Lambda^2/M_KK^2) - 2*S_log}

    ln_ratio = np.log(Lambda**2 / M_KK_GN**2)
    inv_16piG_sak = 0.5 * (total_a0 * ln_ratio - 2.0 * S_log)

    # G_N^Sak in natural units (GeV^{-2})
    if inv_16piG_sak > 0:
        G_sak_nat = 1.0 / (16.0 * np.pi * inv_16piG_sak)
        # Convert to SI: G_N [m^3 kg^-1 s^-2] = G_nat [GeV^-2] * (hbar*c)^3/c^2
        # G_nat = 1/(8 pi M_Pl_red^2) => G_SI = G_N_OBS when M_Pl_red = 2.435e18
        # So G_SI/G_nat = G_N_OBS / G_N_NAT
        conversion = G_N_OBS / G_N_NAT
        G_sak_SI = G_sak_nat * conversion
        log10_ratio = np.log10(G_sak_SI / G_N_OBS)

        # Effective Planck mass: M_Pl_eff = 1/sqrt(8*pi*G_sak_nat)
        M_Pl_eff = 1.0 / np.sqrt(8.0 * np.pi * G_sak_nat)
    else:
        G_sak_nat = float('inf')
        G_sak_SI = float('inf')
        log10_ratio = float('inf')
        M_Pl_eff = 0.0

    results_sak[label] = {
        'Lambda': Lambda,
        'ln_ratio': ln_ratio,
        'inv_16piG': inv_16piG_sak,
        'G_nat': G_sak_nat,
        'G_SI': G_sak_SI,
        'log10_ratio': log10_ratio,
        'M_Pl_eff': M_Pl_eff,
    }

    print(f"{label:>18s}  {Lambda:14.4e}  {inv_16piG_sak:20.6e}  {M_Pl_eff:20.6e}  {log10_ratio:+20.6f}")

# ==========================================================================
#  Step 3: Spectral action a_2 formula for G_N
# ==========================================================================
# CCM formula: 1/kappa^2 = (96 f_2 Lambda^2 - f_0 c)/(24 pi^2)
# with kappa^2 = 16 pi G_N.
# Dropping Yukawa term: 1/(16 pi G_N) = 4 f_2 Lambda^2 / pi^2
# Here Lambda = M_KK in the spectral action, and f_2 absorbs a_2.
#
# The S42 approach: 1/G_N = (96/pi^2) * f_2 * a_2 * M_KK^2
# => 1/(16 pi G_N) = (96/pi^2) * a_2 * M_KK^2 / (16 pi) = (6/pi^3) * a_2 * M_KK^2
#
# Actually from S42 code: M_KK^2 = pi^3 * M_Pl_red^2 / (12 * a_2)
# => 1/(8 pi M_Pl_red^2) = G_N
# => 1/(16 pi G_N) = 2 * M_Pl_red^2
# => 2 * M_Pl_red^2 = (12 * a_2 / pi^3) * M_KK^2 * (what normalization?)
#
# Let me just use the S42 result directly:
# M_KK = 7.43e16 GeV was obtained from: M_KK^2 = pi^3 M_Pl_red^2 / (12 a_2)
# with f_2 = 1. This means:
# 1/(16 pi G_N^spec) = (6/pi^3) * a_2 * M_KK^2  [with the S42 M_KK]

print(f"\n{'='*78}")
print("STEP 3: Spectral Action a_2 Formula for G_N")
print("=" * 78)

# The spectral action G_N is defined by:
# 8 pi M_Pl_red^2 = (96/pi^2) * a_2 * M_KK^2  (with f_2=1)
# => M_Pl_red^2 = (12/pi^2) * a_2 * M_KK^2
# Equivalently: 1/(16 pi G_N) = 2 M_Pl_red^2 = (24/pi^2) * a_2 * M_KK^2
# But let me verify from S42:
# M_KK^2 = pi^3 M_Pl_red^2 / (12 a_2)
# => M_Pl_red^2 = 12 a_2 M_KK^2 / pi^3
# => 8 pi M_Pl_red^2 = 96 pi a_2 M_KK^2 / pi^3 = 96 a_2 M_KK^2 / pi^2
# So: 1/G_N = 8 pi M_Pl_red^2 = (96/pi^2) a_2 M_KK^2  -- confirmed!
# => 1/(16 pi G_N) = (6/pi^3) * a_2 * M_KK^2

inv_16piG_spec = (6.0 / np.pi**3) * a2_fold * M_KK_GN**2
G_spec_nat = 1.0 / (16.0 * np.pi * inv_16piG_spec)
conversion = G_N_OBS / G_N_NAT
G_spec_SI = G_spec_nat * conversion
log10_spec = np.log10(G_spec_SI / G_N_OBS)

print(f"\n  Spectral action G_N (polynomial weighting, f_2=1):")
print(f"    1/(16 pi G_N^spec) = (6/pi^3) * a_2 * M_KK^2")
print(f"                       = (6/{np.pi**3:.4f}) * {a2_fold:.4f} * ({M_KK_GN:.4e})^2")
print(f"                       = {inv_16piG_spec:.6e}  (GeV^2)")
print(f"    G_N^spec (SI) = {G_spec_SI:.6e}  m^3 kg^-1 s^-2")
print(f"    log10(G_N^spec / G_N^obs) = {log10_spec:+.6f}")
print(f"    M_Pl_eff^spec = {1.0/np.sqrt(8*np.pi*G_spec_nat):.4e} GeV")

# Cross-check: since M_KK was DEFINED by matching G_N, this should give exactly G_N_obs
print(f"\n  Cross-check: M_KK was obtained from G_N matching, so log10 ratio should be ~0")
print(f"    Result: {log10_spec:+.6f} -- {'CONSISTENT' if abs(log10_spec) < 0.01 else 'INCONSISTENT'}")

# ==========================================================================
#  Step 4: Ratio G_N^spec / G_N^Sak at each cutoff
# ==========================================================================

print(f"\n{'='*78}")
print("STEP 4: Ratio R = G_N^spec / G_N^Sak")
print("=" * 78)

print(f"\n{'Cutoff':>18s}  {'log10(G_Sak/G_obs)':>20s}  {'R = G_spec/G_Sak':>18s}  {'log10(R)':>12s}")
for label in cutoffs_labels:
    r = results_sak[label]
    if r['G_nat'] > 0 and not np.isinf(r['G_nat']):
        R = G_spec_nat / r['G_nat']
        log10_R = np.log10(R) if R > 0 else float('inf')
    else:
        R = 0
        log10_R = float('-inf')
    results_sak[label]['R'] = R
    results_sak[label]['log10_R'] = log10_R
    print(f"{label:>18s}  {r['log10_ratio']:+20.6f}  {R:18.6e}  {log10_R:+12.6f}")

# ==========================================================================
#  Step 5: Physical G_N comparison — Which is closer?
# ==========================================================================

print(f"\n{'='*78}")
print("STEP 5: Physical G_N Comparison")
print("=" * 78)

print(f"\n  G_N^obs       = {G_N_OBS:.4e} m^3 kg^-1 s^-2")
print(f"  G_N^spec      = {G_spec_SI:.4e} m^3 kg^-1 s^-2  (deviation: {log10_spec:+.4f} dex)")

# The key Sakharov result at Lambda = M_Pl (standard assumption)
for label in ['M_Pl', '10*M_KK(GN)', '100*M_KK(GN)']:
    r = results_sak[label]
    print(f"  G_N^Sak({label:>15s}) = {r['G_SI']:.4e} m^3 kg^-1 s^-2  (deviation: {r['log10_ratio']:+.4f} dex)")

# ==========================================================================
#  Step 6: CC implication — vacuum energy from trace-log vs polynomial
# ==========================================================================
# Polynomial vacuum energy: rho_vac^poly = f_0 Lambda^4 a_0
#   = (2/pi^2) * a_0 * M_KK^4  (with f_0=1, Lambda=M_KK)
# From S42: rho_Lambda_spectral = 8.43e73 GeV^4
#
# Trace-log vacuum energy: rho_vac^log = (1/2) sum_k d_k lambda_k^4 ln(Lambda^2/lambda_k^2)
# This is the REGULARIZED vacuum energy density.
# In the NCG context: the relevant quantity is
#   rho_vac^log = (1/2) * M_KK^4 * sum_k d_k * (lambda_k^code)^4 * ln(Lambda^2/(lambda_k^code*M_KK)^2)

print(f"\n{'='*78}")
print("STEP 6: CC Implication — Vacuum Energy Comparison")
print("=" * 78)

# Polynomial vacuum energy (spectral action a_0 term)
rho_poly_stored = float(d42c['rho_Lambda_spectral'])
rho_poly_recompute = (2.0 / np.pi**2) * a0_fold * M_KK_GN**4

print(f"\n  Polynomial vacuum energy:")
print(f"    rho_vac^poly = (2/pi^2) * a_0 * M_KK^4")
print(f"    a_0 = {a0_fold:.1f}")
print(f"    M_KK = {M_KK_GN:.4e} GeV")
print(f"    rho_vac^poly = {rho_poly_recompute:.6e} GeV^4")
print(f"    (S42 stored: {rho_poly_stored:.6e} GeV^4)")

# Observed CC: rho_Lambda_obs ~ 2.9e-47 GeV^4
rho_Lambda_obs = 2.888e-47  # GeV^4 (from Planck 2018: Omega_Lambda = 0.685, H0 = 67.4)

# Log vacuum energy at each cutoff
print(f"\n  Trace-log vacuum energy at various cutoffs:")
print(f"    rho_vac^log = (M_KK^4 / 2) * sum d_k lambda_k^4 * ln(Lambda^2/(lambda_k*M_KK)^2)")

# The sum is over POSITIVE eigenvalues:
# S_log4 = sum_k d_k lambda_k^{code,4} ln(Lambda^2/(lambda_k^code * M_KK)^2)
#         = sum_k d_k lambda_k^4 [ln(Lambda^2/M_KK^2) - 2*ln(lambda_k^code)]

S_lambda4 = np.sum(all_pw_degs * all_pos_evals**4)               # = a_0^{(-4)} = sum d_k lambda_k^4
S_lambda4_log = np.sum(all_pw_degs * all_pos_evals**4 * np.log(all_pos_evals))  # = sum d_k lambda_k^4 ln(lambda_k)

print(f"    sum d_k lambda_k^4 = {S_lambda4:.4f} (= spectral a_{-4} moment)")
print(f"    sum d_k lambda_k^4 ln(lambda_k) = {S_lambda4_log:.6f}")

print(f"\n{'Cutoff':>18s}  {'rho_log (GeV^4)':>20s}  {'rho_log/rho_poly':>18s}  {'log10(rho_log/rho_obs)':>22s}")

for label in cutoffs_labels:
    Lambda = cutoffs_labels[label]
    ln_ratio = np.log(Lambda**2 / M_KK_GN**2)
    # rho_log = (M_KK^4 / 2) * [S_lambda4 * ln(Lambda^2/M_KK^2) - 2 * S_lambda4_log]
    rho_log = 0.5 * M_KK_GN**4 * (S_lambda4 * ln_ratio - 2.0 * S_lambda4_log)

    if rho_log > 0 and rho_poly_recompute > 0:
        ratio_log_poly = rho_log / rho_poly_recompute
        log10_rho_obs = np.log10(rho_log / rho_Lambda_obs)
    else:
        ratio_log_poly = float('inf')
        log10_rho_obs = float('inf')

    results_sak[label]['rho_log'] = rho_log
    results_sak[label]['ratio_log_poly'] = ratio_log_poly
    results_sak[label]['log10_rho_obs'] = log10_rho_obs

    print(f"{label:>18s}  {rho_log:20.6e}  {ratio_log_poly:18.6e}  {log10_rho_obs:+22.4f}")

# CC reduction in orders of magnitude
print(f"\n  CC reduction from using trace-log instead of polynomial:")
log10_poly_obs = np.log10(rho_poly_recompute / rho_Lambda_obs)
print(f"    Polynomial: log10(rho_poly/rho_obs) = {log10_poly_obs:+.2f}")
for label in ['M_Pl', '10*M_KK(GN)']:
    r = results_sak[label]
    if r['log10_rho_obs'] < float('inf'):
        reduction = log10_poly_obs - r['log10_rho_obs']
        print(f"    Log ({label:>15s}): log10(rho_log/rho_obs) = {r['log10_rho_obs']:+.2f}  (reduction: {reduction:.1f} orders)")

# ==========================================================================
#  Step 7: Cutoff function constraint — Hausdorff moment problem
# ==========================================================================
# If both give the same G_N (R ~ 1), then f_2 and f_0 are constrained.
# The Sakharov formula corresponds to f(x) = -ln(x).
# The spectral action with cutoff f(x) has moments:
#   f_0 = integral_0^infty f(x) dx
#   f_2 = integral_0^infty x f(x) dx
# For f(x) = -ln(x) * Theta(1-x) (sharp cutoff at x=1):
#   f_0 = integral_0^1 (-ln x) dx = 1
#   f_2 = integral_0^1 (-x ln x) dx = 1/4
# For f(x) = exp(-x) (standard smooth cutoff):
#   f_0 = 1, f_2 = 1

print(f"\n{'='*78}")
print("STEP 7: Cutoff Function Constraint")
print("=" * 78)

# What f_2 would make spectral action give the same G_N as Sakharov at Lambda = M_Pl?
# Sakharov: 1/(16piG) = (1/2) sum d_k ln(Lambda^2/lambda_k^2)
# Spectral: 1/(16piG) = (6/pi^3) * f_2 * a_2 * M_KK^2  [M_KK could be different from Lambda]
#
# But in the spectral action, Lambda is the CUTOFF scale, and M_KK is read off separately.
# The comparison should use: spectral action with Lambda = M_KK gives G_N through:
#   1/(16piG) = (6/pi^3) * f_2 * a_2 * Lambda^2
# while Sakharov at the SAME Lambda gives:
#   1/(16piG) = (1/2) [a_0 * ln(Lambda^2/M_KK^2) - 2*S_log]
# These two formulae being equal at Lambda = M_KK means:
#   (6/pi^3) * f_2 * a_2 * M_KK^2 = (1/2) [a_0 * 0 - 2*S_log] = -S_log
#   => f_2 = -S_log * pi^3 / (6 * a_2 * M_KK^2)
# This is problematic because S_log > 0 (eigenvalues > 0.8), so f_2 < 0.
# That means at Lambda = M_KK, Sakharov gives NEGATIVE 1/(16piG) — gravity would be repulsive!

# The issue: at Lambda = M_KK, the log argument < 1 for most eigenvalues (Lambda/lambda < 1.2ish)
# The Sakharov formula REQUIRES Lambda >> lambda_k to make each term positive.

r_mkk = results_sak['M_KK(GN)']
print(f"\n  At Lambda = M_KK(GN) = {M_KK_GN:.4e} GeV:")
print(f"    1/(16piG_Sak) = {r_mkk['inv_16piG']:.6e} GeV^2")
print(f"    This is {'POSITIVE' if r_mkk['inv_16piG'] > 0 else 'NEGATIVE'} (gravity is {'attractive' if r_mkk['inv_16piG'] > 0 else 'WRONG SIGN'})")

# For the comparison to be meaningful, use Lambda >> M_KK
# At Lambda = M_Pl:
r_mpl = results_sak['M_Pl']
f2_implied = r_mpl['inv_16piG'] / ((6.0/np.pi**3) * a2_fold * M_PL_REDUCED**2)

print(f"\n  Matching Sakharov at Lambda=M_Pl with spectral action at Lambda=M_Pl:")
print(f"    Sakharov:  1/(16piG) = {r_mpl['inv_16piG']:.6e} GeV^2")
print(f"    Spectral:  1/(16piG) = (6/pi^3) * f_2 * a_2 * Lambda^2 = {(6.0/np.pi**3) * a2_fold * M_PL_REDUCED**2:.6e} * f_2")
print(f"    => f_2 (implied) = {f2_implied:.6f}")

# For f(x) = -ln(x)*Theta(1-x): f_2 = 1/4
# For f(x) = exp(-x): f_2 = 1
print(f"    Reference: f_2(-ln x * Theta(1-x)) = 0.25")
print(f"    Reference: f_2(exp(-x)) = 1.0")
print(f"    Implied f_2 = {f2_implied:.6f}")

# Similarly, implied f_0 from CC matching
# Sakharov CC: rho = (1/2) M_KK^4 * [S_lambda4 * ln(Lambda^2/M_KK^2) - 2*S_lambda4_log]
# Spectral CC: rho = (2/pi^2) * f_0 * a_0 * Lambda^4
# Matching at Lambda = M_Pl:
rho_log_mpl = r_mpl['rho_log']
f0_implied = rho_log_mpl / ((2.0/np.pi**2) * a0_fold * M_PL_REDUCED**4)

print(f"\n  Matching Sakharov rho_vac at Lambda=M_Pl:")
print(f"    f_0 (implied) = {f0_implied:.6e}")
print(f"    f_0/f_2 = {f0_implied/f2_implied:.6e}")

# Hausdorff moment problem: does a positive decreasing f(x) exist with these moments?
# For a probability measure on [0, infty): f_0 >= 0, f_2 >= 0, f_0*f_4 >= f_2^2 (Cauchy-Schwarz)
# We need f_0 > 0 and f_2 > 0, and the Stieltjes condition
f4_implied = 1.0  # unknown, but check consistency
print(f"\n  Hausdorff moment consistency:")
print(f"    f_0 = {f0_implied:.6e} (must be > 0): {'PASS' if f0_implied > 0 else 'FAIL'}")
print(f"    f_2 = {f2_implied:.6f} (must be > 0): {'PASS' if f2_implied > 0 else 'FAIL'}")
print(f"    f_0/f_2 >> 1? {f0_implied/f2_implied:.4e}")
print(f"    This implies f(x) peaked at small x (dominated by low momenta)")

# ==========================================================================
#  Step 8: Cross-check with BCS condensation energy
# ==========================================================================
# BCS free energy from trace-log: Delta F_BCS = -(1/2) N(E_F) Delta^2
# From S43 UV/IR workshop: this gives ~ -6.6 in spectral units
# Compare to Delta_S = 5522 (the spectral action change from tau=0 to fold)

print(f"\n{'='*78}")
print("STEP 8: Cross-Check with BCS Condensation Energy")
print("=" * 78)

# From S43 UV/IR: Delta_S = S(fold) - S(0) = 250361 - 244839 = 5522
S_fold = float(d36['S_fold'][0])
S0 = float(d36['S_full'][0])
Delta_S = S_fold - S0

# BCS trace-log: F_BCS = -(1/2) Tr ln(H_BdG^2/H_normal^2)
# In the 0D limit with gap Delta and DOS N(E_F):
# F_BCS ~ -(1/2) N(E_F) Delta^2 (weak coupling)
# From S38: E_cond = -0.115 (spectral units)
E_cond_BCS = -0.115

# The trace-log of the BdG determinant:
# F = -(1/2) sum_k ln(E_k^2/epsilon_k^2)
# where E_k = sqrt(epsilon_k^2 + Delta^2) are BdG quasi-particle energies
# For the framework: epsilon_k = lambda_k (Dirac eigenvalues), Delta ~ 0.464
Delta_BCS = float(d42h['Delta_pair'])
print(f"\n  BCS parameters:")
print(f"    Delta_pair = {Delta_BCS:.4f} (spectral units)")
print(f"    E_cond (S38) = {E_cond_BCS:.4f} (spectral units)")
print(f"    Delta_S (spectral action) = {Delta_S:.1f}")

# Compute trace-log BCS energy directly from the spectrum
# F_BCS = -(1/2) sum_k d_k ln(1 + Delta^2/lambda_k^2)
F_BCS_log = -0.5 * np.sum(all_pw_degs * np.log(1.0 + Delta_BCS**2 / all_pos_evals**2))
print(f"\n  BCS trace-log energy:")
print(f"    F_BCS^log = -(1/2) sum d_k ln(1 + Delta^2/lambda_k^2)")
print(f"             = {F_BCS_log:.6f} (spectral units)")
print(f"    E_cond (S38) = {E_cond_BCS:.4f}")
print(f"    Ratio F_BCS^log / E_cond = {F_BCS_log / E_cond_BCS:.4f}")

# The BCS free energy vs spectral action change
print(f"\n  Comparison:")
print(f"    Delta_S (spectral action change) = {Delta_S:.1f}")
print(f"    F_BCS^log (trace-log) = {F_BCS_log:.4f}")
print(f"    Ratio Delta_S / |F_BCS^log| = {Delta_S / abs(F_BCS_log):.1f}")
print(f"    log10 ratio = {np.log10(Delta_S / abs(F_BCS_log)):.2f}")
print(f"    UV/IR workshop prediction: ~836 (~3 orders). Actual: {Delta_S / abs(F_BCS_log):.1f}")

# ==========================================================================
#  Step 9: Cutoff dependence analysis
# ==========================================================================

print(f"\n{'='*78}")
print("STEP 9: Cutoff Dependence — Sakharov is Logarithmic, Spectral is Quadratic")
print("=" * 78)

# The Sakharov formula: 1/(16piG) = (a_0/2) ln(Lambda/M_KK)^2 - S_log
# => G_N ~ 1/ln(Lambda/M_KK)^2  (WEAK cutoff dependence)
# The spectral action: 1/(16piG) ~ f_2 Lambda^2 a_2
# => G_N ~ 1/Lambda^2  (STRONG cutoff dependence)

# Scan Lambda from M_KK to 10^3 * M_KK
log_Lambda_scan = np.linspace(np.log10(M_KK_GN), np.log10(M_PL_REDUCED), 200)
Lambda_scan = 10.0**log_Lambda_scan

inv_G_sak_scan = np.zeros_like(Lambda_scan)
inv_G_spec_scan = np.zeros_like(Lambda_scan)

for i, Lambda in enumerate(Lambda_scan):
    ln_ratio = np.log(Lambda**2 / M_KK_GN**2)
    inv_G_sak_scan[i] = 0.5 * (total_a0 * ln_ratio - 2.0 * S_log)
    inv_G_spec_scan[i] = (6.0/np.pi**3) * a2_fold * Lambda**2

# Ratio scan
ratio_scan = inv_G_spec_scan / inv_G_sak_scan
log10_ratio_scan = np.log10(np.abs(ratio_scan))

# Find crossover: where Sakharov = spectral (R=1)
crossover_idx = np.argmin(np.abs(np.log10(ratio_scan)))
Lambda_cross = Lambda_scan[crossover_idx]
print(f"\n  Crossover Lambda (where G_spec = G_Sak): {Lambda_cross:.4e} GeV")
print(f"    Lambda_cross / M_KK = {Lambda_cross / M_KK_GN:.4f}")
print(f"    Lambda_cross / M_Pl = {Lambda_cross / M_PL_REDUCED:.6f}")

# ==========================================================================
#  Gate verdict
# ==========================================================================

print(f"\n{'='*78}")
print("GATE VERDICT: SAKHAROV-GN-44")
print("=" * 78)

# Use Lambda = M_Pl (the natural UV cutoff)
primary = results_sak['M_Pl']
log10_dev = primary['log10_ratio']

print(f"\n  PRIMARY RESULT: Lambda = M_Pl")
print(f"    G_N^Sak(M_Pl)     = {primary['G_SI']:.6e} m^3 kg^-1 s^-2")
print(f"    G_N^obs            = {G_N_OBS:.6e} m^3 kg^-1 s^-2")
print(f"    |log10(G_Sak/G_obs)| = {abs(log10_dev):.4f}")
print(f"    M_Pl_eff^Sak       = {primary['M_Pl_eff']:.4e} GeV  (obs: {M_PL_REDUCED:.4e})")

# Gate criteria
if abs(log10_dev) < 2:
    gate_verdict = 'PASS'
    gate_detail = f'G_N^Sak within factor 10^{abs(log10_dev):.1f} of observed (< 2 OOM)'
elif abs(log10_dev) < 3:
    gate_verdict = 'INFO'
    gate_detail = f'G_N^Sak within factor 10^{abs(log10_dev):.1f} of observed (2-3 OOM)'
else:
    gate_verdict = 'FAIL'
    gate_detail = f'G_N^Sak off by factor 10^{abs(log10_dev):.1f} (> 3 OOM)'

print(f"\n  GATE: SAKHAROV-GN-44 = {gate_verdict}")
print(f"    {gate_detail}")

# Bonus: poly vs log agreement
r_mpl = results_sak['M_Pl']
log10_R = r_mpl['log10_R']
print(f"\n  BONUS: |log10(G_spec/G_Sak)| = {abs(log10_R):.4f}")
if abs(log10_R) < 1:
    bonus = 'PASS (functionals agree within 1 OOM)'
else:
    bonus = f'FAIL (functionals disagree by {abs(log10_R):.1f} OOM)'
print(f"    BONUS verdict: {bonus}")

# ==========================================================================
#  Summary table
# ==========================================================================

print(f"\n{'='*78}")
print("SUMMARY TABLE")
print("=" * 78)

print(f"\n  {'Quantity':>35s}  {'Value':>20s}  {'Unit':>12s}")
print(f"  {'='*70}")
print(f"  {'N_modes (PW-weighted)':>35s}  {int(total_a0):>20d}  {'':>12s}")
print(f"  {'a_0':>35s}  {total_a0:>20.1f}  {'':>12s}")
print(f"  {'a_2':>35s}  {total_a2:>20.4f}  {'':>12s}")
print(f"  {'a_4':>35s}  {total_a4:>20.4f}  {'':>12s}")
print(f"  {'S_log = sum d_k ln(lambda_k)':>35s}  {S_log:>20.4f}  {'':>12s}")
print(f"  {'M_KK (GN route)':>35s}  {M_KK_GN:>20.4e}  {'GeV':>12s}")
print(f"  {'M_KK (Kerner route)':>35s}  {M_KK_K:>20.4e}  {'GeV':>12s}")
print(f"  {'G_N^obs':>35s}  {G_N_OBS:>20.4e}  {'m3 kg-1 s-2':>12s}")
print(f"  {'G_N^spec (a_2, f_2=1)':>35s}  {G_spec_SI:>20.4e}  {'m3 kg-1 s-2':>12s}")
for label in ['M_Pl', '10*M_KK(GN)', '100*M_KK(GN)']:
    r = results_sak[label]
    print(f"  {'G_N^Sak('+label+')':>35s}  {r['G_SI']:>20.4e}  {'m3 kg-1 s-2':>12s}")
print(f"  {'log10(G_Sak(M_Pl)/G_obs)':>35s}  {results_sak['M_Pl']['log10_ratio']:>+20.4f}  {'':>12s}")
print(f"  {'log10(G_spec/G_Sak(M_Pl))':>35s}  {results_sak['M_Pl']['log10_R']:>+20.4f}  {'':>12s}")
print(f"  {'rho_vac^poly (M_KK)':>35s}  {rho_poly_recompute:>20.4e}  {'GeV^4':>12s}")
print(f"  {'rho_vac^log (M_Pl)':>35s}  {results_sak['M_Pl']['rho_log']:>20.4e}  {'GeV^4':>12s}")
print(f"  {'CC reduction (poly->log)':>35s}  {log10_poly_obs - results_sak['M_Pl']['log10_rho_obs']:>+20.1f}  {'orders':>12s}")
print(f"  {'F_BCS^log':>35s}  {F_BCS_log:>20.4f}  {'spectral':>12s}")
print(f"  {'Delta_S / |F_BCS^log|':>35s}  {Delta_S/abs(F_BCS_log):>20.1f}  {'':>12s}")
print(f"  {'f_2 (implied, Lambda=M_Pl)':>35s}  {f2_implied:>20.6f}  {'':>12s}")
print(f"  {'Lambda_cross':>35s}  {Lambda_cross:>20.4e}  {'GeV':>12s}")
print(f"  {'GATE VERDICT':>35s}  {gate_verdict:>20s}  {'':>12s}")

# ==========================================================================
#  Save data
# ==========================================================================

np.savez(DATA_DIR / 's44_sakharov_gn.npz',
    # Spectrum
    a0_fold=total_a0,
    a2_fold=total_a2,
    a4_fold=total_a4,
    S_log=S_log,
    S_lambda4=S_lambda4,
    S_lambda4_log=S_lambda4_log,
    N_modes=int(total_a0),
    n_unique_masses=len(unique_lams),
    unique_masses_pw=unique_lams,
    unique_degs_pw=unique_degs,

    # G_N values
    G_spec_SI=G_spec_SI,
    G_spec_nat=G_spec_nat,
    inv_16piG_spec=inv_16piG_spec,

    # Sakharov at M_Pl
    G_sak_MPl_SI=results_sak['M_Pl']['G_SI'],
    G_sak_MPl_nat=results_sak['M_Pl']['G_nat'],
    inv_16piG_sak_MPl=results_sak['M_Pl']['inv_16piG'],
    log10_Gsak_Gobs_MPl=results_sak['M_Pl']['log10_ratio'],

    # Sakharov at 10*M_KK
    G_sak_10MKK_SI=results_sak['10*M_KK(GN)']['G_SI'],
    log10_Gsak_Gobs_10MKK=results_sak['10*M_KK(GN)']['log10_ratio'],

    # Sakharov at 100*M_KK
    G_sak_100MKK_SI=results_sak['100*M_KK(GN)']['G_SI'],
    log10_Gsak_Gobs_100MKK=results_sak['100*M_KK(GN)']['log10_ratio'],

    # Ratio
    log10_R_MPl=results_sak['M_Pl']['log10_R'],
    R_MPl=results_sak['M_Pl']['R'],

    # Vacuum energy
    rho_poly=rho_poly_recompute,
    rho_log_MPl=results_sak['M_Pl']['rho_log'],
    CC_reduction_orders=log10_poly_obs - results_sak['M_Pl']['log10_rho_obs'],
    log10_rho_poly_obs=log10_poly_obs,
    log10_rho_log_obs_MPl=results_sak['M_Pl']['log10_rho_obs'],

    # BCS cross-check
    F_BCS_log=F_BCS_log,
    Delta_S=Delta_S,
    ratio_DeltaS_FBCS=Delta_S / abs(F_BCS_log),
    Delta_BCS=Delta_BCS,

    # Cutoff function
    f2_implied=f2_implied,
    f0_implied=f0_implied,
    Lambda_cross=Lambda_cross,

    # Scan data
    Lambda_scan=Lambda_scan,
    inv_G_sak_scan=inv_G_sak_scan,
    inv_G_spec_scan=inv_G_spec_scan,

    # Gate
    gate_name=np.array(['SAKHAROV-GN-44']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
    bonus_verdict=np.array([bonus]),

    # Physical constants used
    M_KK_GN=M_KK_GN,
    M_KK_K=M_KK_K,
    M_PL_REDUCED=M_PL_REDUCED,
    G_N_OBS=G_N_OBS,
    rho_Lambda_obs=rho_Lambda_obs,
)

print(f"\n  Data saved to: tier0-computation/s44_sakharov_gn.npz")

# ==========================================================================
#  Plot
# ==========================================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('SAKHAROV-GN-44: Induced Gravity from 992 KK Modes', fontsize=14, fontweight='bold')

# Panel 1: Spectrum histogram (PW-weighted)
ax = axes[0, 0]
ax.hist(all_pos_evals, bins=50, weights=all_pw_degs, color='steelblue', alpha=0.7, edgecolor='k')
ax.set_xlabel(r'$|\lambda_k|$ (code units)')
ax.set_ylabel(r'$d_k$ (PW-weighted count)')
ax.set_title(f'KK Spectrum (N={int(total_a0)} PW modes)')
ax.axvline(np.exp(S_log/total_a0), color='red', ls='--', label=f'geom. mean = {np.exp(S_log/total_a0):.3f}')
ax.legend(fontsize=8)

# Panel 2: G_N vs cutoff Lambda
ax = axes[0, 1]
valid = inv_G_sak_scan > 0
log_lam = np.log10(Lambda_scan[valid])
log_inv_G_sak = np.log10(inv_G_sak_scan[valid])
log_inv_G_spec = np.log10(inv_G_spec_scan[valid])
ax.plot(log_lam, log_inv_G_sak, 'b-', lw=2, label='Sakharov (log)')
ax.plot(log_lam, log_inv_G_spec, 'r--', lw=2, label='Spectral (poly)')
ax.axhline(np.log10(2*M_PL_REDUCED**2), color='green', ls=':', lw=1.5, label=r'Observed ($2M_{Pl}^2$)')
ax.set_xlabel(r'$\log_{10}(\Lambda/\mathrm{GeV})$')
ax.set_ylabel(r'$\log_{10}(1/(16\pi G_N))$ [GeV$^2$]')
ax.set_title(r'$G_N$ vs UV Cutoff $\Lambda$')
ax.legend(fontsize=8)

# Panel 3: Ratio G_spec/G_Sak vs cutoff
ax = axes[0, 2]
valid_r = (ratio_scan > 0) & np.isfinite(ratio_scan)
ax.plot(np.log10(Lambda_scan[valid_r]), np.log10(ratio_scan[valid_r]), 'k-', lw=2)
ax.axhline(0, color='gray', ls=':', lw=1)
ax.axhline(1, color='red', ls='--', alpha=0.5, label='1 OOM')
ax.axhline(-1, color='red', ls='--', alpha=0.5)
ax.set_xlabel(r'$\log_{10}(\Lambda/\mathrm{GeV})$')
ax.set_ylabel(r'$\log_{10}(G_N^{spec}/G_N^{Sak})$')
ax.set_title('Ratio: Spectral / Sakharov')
ax.axvline(np.log10(Lambda_cross), color='orange', ls='--', label=f'Crossover: {Lambda_cross:.1e}')
ax.legend(fontsize=8)

# Panel 4: Vacuum energy comparison
ax = axes[1, 0]
labels_bar = ['Poly\n(spectral)', 'Log\n(Sakharov,MPl)', 'Observed']
vals_bar = [np.log10(rho_poly_recompute), results_sak['M_Pl']['log10_rho_obs'] + np.log10(rho_Lambda_obs),
            np.log10(rho_Lambda_obs)]
# Actually: plot log10(rho) directly
vals_bar = [np.log10(rho_poly_recompute), np.log10(results_sak['M_Pl']['rho_log']), np.log10(rho_Lambda_obs)]
colors_bar = ['red', 'blue', 'green']
ax.bar(labels_bar, vals_bar, color=colors_bar, alpha=0.7, edgecolor='k')
ax.set_ylabel(r'$\log_{10}(\rho_\Lambda / \mathrm{GeV}^4)$')
ax.set_title('Vacuum Energy Density')
for i, v in enumerate(vals_bar):
    ax.text(i, v + 1, f'{v:.1f}', ha='center', fontsize=9, fontweight='bold')

# Panel 5: Per-mode contribution to Sakharov G_N
ax = axes[1, 1]
contrib_per_mode = all_pw_degs * np.log(M_PL_REDUCED**2 / (all_pos_evals * M_KK_GN)**2)
ax.scatter(all_pos_evals, contrib_per_mode, s=2, alpha=0.3, c='steelblue')
ax.set_xlabel(r'$|\lambda_k|$ (code units)')
ax.set_ylabel(r'$d_k \ln(\Lambda^2/\lambda_k^{phys,2})$')
ax.set_title(f'Per-mode contribution to Sakharov $G_N$ ($\Lambda=M_{{Pl}}$)')
ax.axhline(0, color='gray', ls=':')

# Panel 6: Summary text
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"SAKHAROV-GN-44: {gate_verdict}\n"
    f"{'='*40}\n\n"
    f"N_modes (PW-weighted) = {int(total_a0)}\n"
    f"a_2 (spectral zeta) = {total_a2:.2f}\n"
    f"S_log = {S_log:.2f}\n\n"
    f"G_N^obs = {G_N_OBS:.3e} SI\n"
    f"G_N^spec = {G_spec_SI:.3e} SI\n"
    f"G_N^Sak(M_Pl) = {results_sak['M_Pl']['G_SI']:.3e} SI\n\n"
    f"log10(G_Sak/G_obs) = {results_sak['M_Pl']['log10_ratio']:+.3f}\n"
    f"log10(G_spec/G_Sak) = {results_sak['M_Pl']['log10_R']:+.3f}\n\n"
    f"CC reduction (poly->log): {log10_poly_obs - results_sak['M_Pl']['log10_rho_obs']:.1f} orders\n"
    f"BCS ratio Delta_S/|F_BCS| = {Delta_S/abs(F_BCS_log):.0f}\n\n"
    f"BONUS: {bonus}\n"
    f"f_2(implied) = {f2_implied:.4f}\n"
    f"Lambda_cross = {Lambda_cross:.2e} GeV"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(DATA_DIR / 's44_sakharov_gn.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved to: tier0-computation/s44_sakharov_gn.png")

print(f"\n{'='*78}")
print("COMPUTATION COMPLETE")
print("=" * 78)
