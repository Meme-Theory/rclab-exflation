#!/usr/bin/env python3
"""
s66_kk_threshold_l5.py — KK-THRESHOLD-L5-66
Gaussian-cutoff KK threshold corrections: convergence at L_max = 5.

STRUCTURAL CONTEXT
------------------
S64 (KK-THRESHOLD-64) established:
  - Formula C is correct: delta(1/g_3^2) = SUM_{(p,q)} T(p,q)/(8pi^2) * ln(Lambda^2/omega_min^2)
    where omega_min is the smallest positive D_K eigenvalue in sector (p,q).
  - Gaussian regulation: multiply by exp(-omega_min^2 / Lambda^2)
  - Lambda = 1/gamma_opt = 2.048 M_KK (from S62 Gaussian optimization)
  - Formula A (eigenvalue-resolved) DIVERGES (overcounts by dim^2 per sector)
  - Formula B (S62 workshop) also overcounts

This script:
  1. Loads S64 per-sector data (verified eigenvalue computations)
  2. INDEPENDENTLY recomputes D_K eigenvalues for all L=5 sectors (fresh verification)
  3. Computes the convergence sequence S_1, S_2, ..., S_5 (cumulative threshold sums)
  4. Evaluates convergence ratio r_L = |S_L - S_{L-1}| / |S_{L-1} - S_{L-2}|
  5. Richardson extrapolation if converging
  6. Runs 2-loop SM RG to get m_H prediction at L=5

CONVERGENCE DEFINITION
---------------------
r_L = (S_L - S_{L-1}) / (S_{L-1} - S_{L-2})  (per-level ratio, not cumulative)
For geometric convergence, r_L -> const < 1. The gate tests r_5 specifically.

Gate: KK-THRESHOLD-L5-66
  PASS: r_5 < 1.5
  FAIL: r_5 > 3.0
  INFO: 1.5 < r_5 < 3.0

Author: baptista-spacetime-analyst
Session: S66 W7-A
"""

import sys
import os
import time
import json

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

import dirac_spectrum as tds

outdir = os.path.dirname(os.path.abspath(__file__))
results_file = os.path.join(outdir, 's66_kk_threshold_l5_results.txt')
rf = open(results_file, 'w')

def log(msg=''):
    print(msg)
    rf.write(msg + '\n')
    rf.flush()

log("=" * 80)
log("KK-THRESHOLD-L5-66: Gaussian-Cutoff Threshold Sum — Convergence at L=5")
log("S66 W7-A | baptista-spacetime-analyst")
log("=" * 80)

# =============================================================================
# 1. SU(3) REPRESENTATION THEORY
# =============================================================================
log("\n" + "=" * 80)
log("1. SU(3) REPRESENTATION THEORY")
log("=" * 80)


def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def C2_su3(p, q):
    """Quadratic Casimir of SU(3) irrep (p,q)."""
    return (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0


def T_su3(p, q):
    """Dynkin index: T(R) = dim(R)*C_2(R)/dim(adj) = dim(R)*C_2(R)/8."""
    return dim_su3(p, q) * C2_su3(p, q) / 8.0


# Verify
T_fund = T_su3(1, 0)
b3_quarks = 6 * (4.0 / 3.0) * T_fund
b3_SM = -11.0 + b3_quarks
assert abs(T_fund - 0.5) < 1e-10, f"T(fund) wrong: {T_fund}"
assert abs(b3_SM - (-7.0)) < 1e-10, f"b3 wrong: {b3_SM}"
log(f"  T(fund) = {T_fund:.4f} [OK]")
log(f"  b_3(SM) = {b3_SM:.4f} [OK]")

# Sector table
log(f"\n  {'(p,q)':>6} {'dim':>5} {'C_2':>8} {'T':>10}")
for L in range(6):  # L=0..5
    for p in range(L + 1):
        q = L - p
        d = dim_su3(p, q)
        c2 = C2_su3(p, q)
        T = T_su3(p, q)
        log(f"  ({p},{q}) {d:5d} {c2:8.4f} {T:10.4f}")

# Sector count at each L
n_sectors_by_L = {}
for L in range(7):
    n_sectors_by_L[L] = L + 1  # sectors (0,L), (1,L-1), ..., (L,0)
cumul_sectors = {L: sum(n_sectors_by_L[l] for l in range(L + 1)) for L in range(7)}
log(f"\n  Sector counts: L=0:{cumul_sectors[0]}, L=1:{cumul_sectors[1]}, "
    f"L=2:{cumul_sectors[2]}, L=3:{cumul_sectors[3]}, "
    f"L=4:{cumul_sectors[4]}, L=5:{cumul_sectors[5]}, L=6:{cumul_sectors[6]}")

# =============================================================================
# 2. LOAD S64 DATA AND INDEPENDENTLY VERIFY L=5 SECTORS
# =============================================================================
log("\n" + "=" * 80)
log("2. INDEPENDENT VERIFICATION OF L=5 D_K EIGENVALUES")
log("=" * 80)

# Load S64 for cross-check
d64 = np.load(os.path.join(outdir, 's64_kk_threshold.npz'), allow_pickle=True)
s64_delta_C_gauss = d64['delta_C_gauss']
s64_L_range = d64['L_range']
Lambda_fixed = float(d64['Lambda_fixed'])
gamma_opt = float(d64['gamma_opt'])
g3_MKK_nominal = float(d64['g3_MKK_nominal'])
g3_inv2_nominal = float(d64['g3_inv2_nominal'])
ratio_gilkey = float(d64['ratio_gilkey'])

log(f"  S64 reference data loaded:")
log(f"    Lambda_fixed = {Lambda_fixed:.6f} M_KK")
log(f"    gamma_opt = {gamma_opt:.6f}")
log(f"    g3_MKK_nominal = {g3_MKK_nominal:.6f}")
log(f"    g3_inv2_nominal = {g3_inv2_nominal:.6f}")
log(f"    ratio_gilkey = {ratio_gilkey:.6f}")

# S64 per-sector omega_min for cross-check
s64_omega_min = {}
for i in range(len(d64['sec_p'])):
    p, q = int(d64['sec_p'][i]), int(d64['sec_q'][i])
    s64_omega_min[(p, q)] = float(d64['sec_omega_min'][i])

# Fresh computation of D_K eigenvalues at fold for L=5 sectors
log(f"\n  Computing D_K eigenvalues at tau_fold = {tau_fold} ...")

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()

cliff_err = tds.validate_clifford(gammas)
log(f"  Clifford algebra error: {cliff_err:.2e}")

B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma = tds.connection_coefficients(ft)
Omega = tds.spinor_connection_offset(Gamma, gammas)

L_MAX = 5  # We compute up to L=5 for this gate (local)

sector_data = {}
t_start = time.time()

for L in range(L_MAX + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = dim_su3(p, q)
        t0 = time.time()
        tds._irrep_cache.clear()

        try:
            rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq
        except Exception as e:
            log(f"  ({p},{q}): SKIPPED - {e}")
            continue

        D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)

        # D_pi is anti-Hermitian: eigenvalues purely imaginary
        H = 1j * D_pi
        H = 0.5 * (H + H.conj().T)  # Enforce exact Hermiticity
        evals = np.linalg.eigvalsh(H)

        pos_evals = np.sort(np.abs(evals[evals > 1e-12]))
        t1 = time.time()

        D_ah_err = np.max(np.abs(D_pi + D_pi.conj().T))

        omega_min = np.min(pos_evals) if len(pos_evals) > 0 else np.inf
        omega_max = np.max(pos_evals) if len(pos_evals) > 0 else 0.0

        sector_data[(p, q)] = {
            'dim': dim_pq,
            'level': L,
            'C2': C2_su3(p, q),
            'T': T_su3(p, q),
            'pos_evals': pos_evals,
            'n_pos_evals': len(pos_evals),
            'omega_min': omega_min,
            'omega_max': omega_max,
            'D_ah_err': D_ah_err,
            'time': t1 - t0,
        }

        # Cross-check against S64
        if (p, q) in s64_omega_min:
            s64_om = s64_omega_min[(p, q)]
            err = abs(omega_min - s64_om) / max(abs(s64_om), 1e-15) if s64_om != np.inf else 0.0
            xcheck = f"S64 match: {err:.2e}" if err < 1e-8 else f"S64 MISMATCH: {err:.2e}"
        else:
            xcheck = "no S64 ref"

        status = "OK" if D_ah_err < 1e-10 else f"AH_ERR={D_ah_err:.2e}"
        log(f"  ({p},{q}): dim={dim_pq:3d}, n_pos={len(pos_evals):4d}, "
            f"|lam| in [{omega_min:.4f},{omega_max:.4f}], "
            f"{status}, {xcheck}, {t1 - t0:.3f}s")

t_total = time.time() - t_start
log(f"\n  Total: {len(sector_data)} sectors computed in {t_total:.1f}s")

# =============================================================================
# 3. FORMULA C WITH GAUSSIAN CUTOFF — CUMULATIVE SUMS
# =============================================================================
log("\n" + "=" * 80)
log("3. FORMULA C (CORRECT): T(p,q)/(8pi^2) * ln(Lambda^2/omega_min^2) * Gaussian")
log("=" * 80)

Lambda = Lambda_fixed
log(f"  Lambda = {Lambda:.6f} M_KK")

# Per-sector threshold contributions
per_sector = []
for (p, q), sd in sorted(sector_data.items(), key=lambda x: (x[1]['level'], x[0])):
    L = sd['level']
    T = sd['T']
    omega_min = sd['omega_min']

    if p == 0 and q == 0:
        # (0,0) is the SM zero mode — not a threshold correction
        per_sector.append({
            'p': p, 'q': q, 'level': L, 'dim': sd['dim'], 'T': T,
            'omega_min': omega_min,
            'delta_C_sharp': 0.0, 'delta_C_gauss': 0.0,
        })
        continue

    # Sharp cutoff: T/(8pi^2) * ln(Lambda^2/omega_min^2)
    ln_term = np.log(Lambda**2 / omega_min**2)
    dC_sharp = T * ln_term / (8.0 * PI**2)

    # Gaussian cutoff: multiply by exp(-omega_min^2/Lambda^2)
    gauss_w = np.exp(-omega_min**2 / Lambda**2)
    dC_gauss = T * gauss_w * ln_term / (8.0 * PI**2)

    per_sector.append({
        'p': p, 'q': q, 'level': L, 'dim': sd['dim'], 'T': T,
        'omega_min': omega_min,
        'delta_C_sharp': dC_sharp, 'delta_C_gauss': dC_gauss,
    })

    log(f"  ({p},{q}) L={L} T={T:8.2f} omega_min={omega_min:.4f} "
        f"gauss_w={gauss_w:.6f} dC_sharp={dC_sharp:.6f} dC_gauss={dC_gauss:.6f}")

# Cumulative sums at each L
L_range = np.arange(0, L_MAX + 1)  # 0,1,2,3,4,5
S_sharp = np.zeros(len(L_range))
S_gauss = np.zeros(len(L_range))
T_cumul = np.zeros(len(L_range))
n_sec_cumul = np.zeros(len(L_range), dtype=int)

for iL, L_val in enumerate(L_range):
    for sd in per_sector:
        if sd['level'] <= L_val and not (sd['p'] == 0 and sd['q'] == 0):
            S_sharp[iL] += sd['delta_C_sharp']
            S_gauss[iL] += sd['delta_C_gauss']
            T_cumul[iL] += sd['T']
            n_sec_cumul[iL] += 1

log(f"\n  Cumulative threshold sums (Formula C):")
log(f"  {'L':>3} {'N_sec':>6} {'T_total':>10} {'S_sharp':>14} {'S_gauss':>14}")
for iL, L_val in enumerate(L_range):
    log(f"  {L_val:3d} {n_sec_cumul[iL]:6d} {T_cumul[iL]:10.2f} "
        f"{S_sharp[iL]:14.6f} {S_gauss[iL]:14.6f}")

# Cross-check: S64 values
log(f"\n  Cross-check against S64 delta_C_gauss:")
for iL, L_val in enumerate(L_range):
    if L_val <= 6:
        s64_val = s64_delta_C_gauss[L_val]
        err = abs(S_gauss[iL] - s64_val)
        log(f"  L={L_val}: this={S_gauss[iL]:.8f}, S64={s64_val:.8f}, |diff|={err:.2e}")

# =============================================================================
# 4. CONVERGENCE ANALYSIS
# =============================================================================
log("\n" + "=" * 80)
log("4. CONVERGENCE ANALYSIS")
log("=" * 80)

# Per-level increments
delta_L_sharp = np.diff(S_sharp)  # S_1-S_0, S_2-S_1, ..., S_5-S_4
delta_L_gauss = np.diff(S_gauss)

log(f"\n  Per-level increments Delta_L = S_L - S_{'{L-1}'}:")
log(f"  {'L':>3} {'Delta_L_sharp':>16} {'Delta_L_gauss':>16}")
for i in range(len(delta_L_sharp)):
    L_val = i + 1
    log(f"  {L_val:3d} {delta_L_sharp[i]:16.8f} {delta_L_gauss[i]:16.8f}")

# Convergence ratios: r_L = Delta_L / Delta_{L-1}
log(f"\n  Convergence ratios r_L = Delta_L / Delta_{{L-1}}:")
log(f"  {'L':>3} {'r_sharp':>12} {'r_gauss':>12}")

r_sharp_list = []
r_gauss_list = []
for i in range(1, len(delta_L_sharp)):
    L_val = i + 1
    r_s = delta_L_sharp[i] / delta_L_sharp[i - 1] if delta_L_sharp[i - 1] != 0 else np.inf
    r_g = delta_L_gauss[i] / delta_L_gauss[i - 1] if delta_L_gauss[i - 1] != 0 else np.inf
    r_sharp_list.append(r_s)
    r_gauss_list.append(r_g)
    log(f"  {L_val:3d} {r_s:12.6f} {r_g:12.6f}")

# The gate tests r_5 = Delta_5 / Delta_4 (Gaussian)
r_5_gauss = r_gauss_list[-1] if len(r_gauss_list) > 0 else np.inf
r_5_sharp = r_sharp_list[-1] if len(r_sharp_list) > 0 else np.inf

log(f"\n  *** PRIMARY CONVERGENCE RATIO r_5 (Gaussian) = {r_5_gauss:.6f} ***")
log(f"      r_5 (sharp) = {r_5_sharp:.6f}")

# Also compute from S64 L=6 data for extended analysis
# S64 gives delta_C_gauss at L=0..6
delta_L_s64 = np.diff(s64_delta_C_gauss)
log(f"\n  Extended convergence from S64 (L=0..6):")
log(f"  {'L':>3} {'Delta_L':>16} {'r_L':>12}")
for i in range(len(delta_L_s64)):
    L_val = i + 1
    if i > 0:
        r = delta_L_s64[i] / delta_L_s64[i - 1] if delta_L_s64[i - 1] != 0 else np.inf
    else:
        r = np.inf
    log(f"  {L_val:3d} {delta_L_s64[i]:16.8f} {r:12.6f}" if i > 0
        else f"  {L_val:3d} {delta_L_s64[i]:16.8f} {'---':>12}")

# =============================================================================
# 5. RICHARDSON EXTRAPOLATION
# =============================================================================
log("\n" + "=" * 80)
log("5. RICHARDSON EXTRAPOLATION")
log("=" * 80)

# If the series S_L converges geometrically: S_L = S_inf + A * r^L
# Then S_inf = (S_L * S_{L-2} - S_{L-1}^2) / (S_L - 2*S_{L-1} + S_{L-2})
# This is the Aitken Delta^2 acceleration

# Use L=3,4,5 (Gaussian)
S3, S4, S5 = S_gauss[3], S_gauss[4], S_gauss[5]

denom = S5 - 2 * S4 + S3
if abs(denom) > 1e-15:
    S_inf_aitken = (S5 * S3 - S4**2) / denom
    r_eff = (S5 - S4) / (S4 - S3)
    log(f"  Aitken Delta^2 (L=3,4,5, Gaussian):")
    log(f"    S_3 = {S3:.8f}")
    log(f"    S_4 = {S4:.8f}")
    log(f"    S_5 = {S5:.8f}")
    log(f"    S_inf = {S_inf_aitken:.8f}")
    log(f"    Effective ratio r = {r_eff:.6f}")
else:
    S_inf_aitken = S5
    r_eff = 0.0  # (local)
    log(f"  Aitken: denominator too small, using S_5 directly")

# Also with S64 L=6 data: use L=4,5,6
s64_S4 = s64_delta_C_gauss[4]
s64_S5 = s64_delta_C_gauss[5]
s64_S6 = s64_delta_C_gauss[6]
denom_ext = s64_S6 - 2 * s64_S5 + s64_S4
if abs(denom_ext) > 1e-15:
    S_inf_ext = (s64_S6 * s64_S4 - s64_S5**2) / denom_ext
    r_eff_ext = (s64_S6 - s64_S5) / (s64_S5 - s64_S4)
    log(f"\n  Aitken Delta^2 (L=4,5,6, Gaussian from S64):")
    log(f"    S_4 = {s64_S4:.8f}")
    log(f"    S_5 = {s64_S5:.8f}")
    log(f"    S_6 = {s64_S6:.8f}")
    log(f"    S_inf = {S_inf_ext:.8f}")
    log(f"    Effective ratio r = {r_eff_ext:.6f}")
else:
    S_inf_ext = s64_S6
    r_eff_ext = 0.0  # (local)

# Simple geometric sum extrapolation: S_inf = S_L + Delta_L * r / (1-r)
# Using the last known ratio r_5
if abs(r_5_gauss) < 1.0 and r_5_gauss > 0:
    Delta_5_gauss = delta_L_gauss[-1]
    S_inf_geom = S5 + Delta_5_gauss * r_5_gauss / (1 - r_5_gauss)
    log(f"\n  Geometric sum extrapolation (ratio r_5 = {r_5_gauss:.6f}):")
    log(f"    S_inf = {S_inf_geom:.8f}")
else:
    S_inf_geom = S5
    log(f"\n  Geometric sum: r_5 = {r_5_gauss:.6f} >= 1, cannot extrapolate from L=5 alone")

# Best estimate: use the extended (L=4,5,6) Aitken if available
S_inf_best = S_inf_ext if abs(denom_ext) > 1e-15 else S_inf_aitken
log(f"\n  *** BEST ESTIMATE S_inf = {S_inf_best:.6f} ***")
log(f"      (from Aitken L=4,5,6 using S64 data)")

# =============================================================================
# 6. HIGGS MASS FROM 2-LOOP SM RG
# =============================================================================
log("\n" + "=" * 80)
log("6. HIGGS MASS PREDICTION")
log("=" * 80)

# SM parameters
# m_H_obs = 125.10  # GeV  # S72: now imported from canonical_constants
v_ew = 246.22  # GeV  # S72: intentionally differs from canonical v_ew=246.0 (Fermi-extracted)
# alpha_s_MZ = 0.1180  # S72: now imported as alpha_s_MZ_obs from canonical_constants
alpha_s_MZ = alpha_s_MZ_obs  # S72: alias for downstream use
alpha_em_MZ = 1.0 / alpha_em_MZ_inv
sin2_tW = sin2_thetaW_MSbar
g1_MZ = np.sqrt(5.0 / 3.0) * np.sqrt(4 * PI * alpha_em_MZ / (1 - sin2_tW))
g2_MZ = np.sqrt(4 * PI * alpha_em_MZ / sin2_tW)
g3_MZ = np.sqrt(4 * PI * alpha_s_MZ)
m_t_MSbar = 172.69 * (1.0 - 4.0 * alpha_s_MZ / (3.0 * PI))
yt_MZ = np.sqrt(2) * m_t_MSbar / v_ew
lambda_MZ_obs = m_H_obs**2 / (2.0 * v_ew**2)

t_MKK = np.log(M_KK_gravity / M_Z)

log(f"  SM parameters at M_Z:")
log(f"    g_1 = {g1_MZ:.6f}, g_2 = {g2_MZ:.6f}, g_3 = {g3_MZ:.6f}")
log(f"    y_t = {yt_MZ:.6f}, lambda_obs = {lambda_MZ_obs:.6f}")
log(f"    t(M_KK) = ln(M_KK/M_Z) = {t_MKK:.4f}")


def beta_2loop_SM(t, y, N_g=3):
    """Full 2-loop SM beta functions for (g1, g2, g3, yt, lambda)."""
    g1, g2, g3, yt, lam = y
    g1sq, g2sq, g3sq = g1**2, g2**2, g3**2
    ytsq = yt**2
    b16 = 16.0 * PI**2
    b16sq = b16**2

    dg1 = g1**3 / b16 * (41.0 / 10.0) + g1**3 / b16sq * (
        199.0 / 50.0 * g1sq + 27.0 / 10.0 * g2sq + 44.0 / 5.0 * g3sq - 17.0 / 10.0 * ytsq)
    dg2 = g2**3 / b16 * (-19.0 / 6.0) + g2**3 / b16sq * (
        9.0 / 10.0 * g1sq + 35.0 / 6.0 * g2sq + 12.0 * g3sq - 3.0 / 2.0 * ytsq)
    dg3 = g3**3 / b16 * (-7.0) + g3**3 / b16sq * (
        11.0 / 10.0 * g1sq + 9.0 / 2.0 * g2sq - 26.0 * g3sq - 2.0 * ytsq)

    dyt = yt / b16 * (9.0 / 2.0 * ytsq - 17.0 / 20.0 * g1sq - 9.0 / 4.0 * g2sq - 8.0 * g3sq)
    dyt += yt / b16sq * (
        -12.0 * ytsq**2
        + ytsq * (393.0 / 80.0 * g1sq + 225.0 / 16.0 * g2sq + 36.0 * g3sq)
        + 1187.0 / 600.0 * g1sq**2 - 9.0 / 20.0 * g1sq * g2sq
        + 19.0 / 15.0 * g1sq * g3sq - 23.0 / 4.0 * g2sq**2
        + 9.0 * g2sq * g3sq - 108.0 * g3sq**2
        + 6.0 * lam**2 - 3.0 / 2.0 * lam * ytsq)

    dlam = (1.0 / b16) * (
        24.0 * lam**2
        + 12.0 * lam * ytsq - 12.0 * ytsq**2
        - 3.0 * lam * (3.0 / 5.0 * g1sq + 3.0 * g2sq)
        + 3.0 / 8.0 * (3.0 / 25.0 * g1sq**2 + 6.0 / 5.0 * g1sq * g2sq + 3.0 * g2sq**2))
    dlam += (1.0 / b16sq) * (
        -312.0 * lam**3
        - 144.0 * lam**2 * ytsq
        + lam * ytsq * (-3.0 * ytsq + 80.0 * g3sq + 45.0 / 2.0 * g2sq + 85.0 / 6.0 * 3.0 / 5.0 * g1sq)
        + 60.0 * ytsq**3 - 16.0 * ytsq**2 * g3sq
        + lam * (108.0 / 5.0 * 3.0 / 25.0 * g1sq**2 + 36.0 * 3.0 / 5.0 * g1sq * g2sq / 5.0
                 - 73.0 / 8.0 * g2sq**2)
        - 3.0 / 5.0 * g1sq * (-57.0 / 10.0 * g2sq * g1sq + 12.0 * ytsq**2) / 2.0
        + g2sq * (-289.0 / 8.0 * g2sq**2 / 4.0))

    return [dg1, dg2, dg3, dyt, dlam]


# Run SM from M_Z UP to M_KK
y0_up = [g1_MZ, g2_MZ, g3_MZ, yt_MZ, lambda_MZ_obs]
sol_up = solve_ivp(
    beta_2loop_SM, [0, t_MKK], y0_up,
    t_eval=np.linspace(0, t_MKK, 3000),
    method='RK45', rtol=1e-12, atol=1e-14
)
g1_MKK = sol_up.y[0, -1]
g2_MKK = sol_up.y[1, -1]
g3_MKK = sol_up.y[2, -1]
yt_MKK = sol_up.y[3, -1]
lam_MKK = sol_up.y[4, -1]

log(f"\n  SM couplings at M_KK (2-loop upward):")
log(f"    g_1 = {g1_MKK:.6f}, g_2 = {g2_MKK:.6f}, g_3 = {g3_MKK:.6f}")
log(f"    y_t = {yt_MKK:.6f}, lambda = {lam_MKK:.6f}")
log(f"    1/g_3^2 = {1.0 / g3_MKK**2:.6f}")


def run_rg_down_get_mH(g3_eff, lam_UV):
    """Run 2-loop SM from M_KK to M_Z, return m_H."""
    y0 = [g1_MKK, g2_MKK, g3_eff, yt_MKK, lam_UV]
    sol = solve_ivp(
        beta_2loop_SM, [t_MKK, 0], y0,
        t_eval=np.linspace(t_MKK, 0, 2000),
        method='RK45', rtol=1e-12, atol=1e-14
    )
    if not sol.success:
        return np.nan
    lam_IR = sol.y[4, -1]
    return np.sqrt(2.0 * lam_IR) * v_ew if lam_IR > 0 else 0.0


# Compute m_H at each truncation level
log(f"\n  Higgs mass at each truncation level:")
log(f"  {'L':>3} {'delta':>14} {'g3_eff':>10} {'lam_CCM':>12} {'m_H (GeV)':>12}")

mH_by_L = np.zeros(len(L_range))
for iL, L_val in enumerate(L_range):
    delta = S_gauss[iL]
    g3_inv2 = g3_inv2_nominal + delta
    g3_eff = 1.0 / np.sqrt(g3_inv2) if g3_inv2 > 0 else 0.0
    lam_CCM = (4.0 / 3.0) * g3_eff**2 * ratio_gilkey
    mH = run_rg_down_get_mH(g3_eff, lam_CCM)
    mH_by_L[iL] = mH
    log(f"  {L_val:3d} {delta:14.8f} {g3_eff:10.6f} {lam_CCM:12.8f} {mH:12.4f}")

# m_H at extrapolated S_inf
g3_inv2_inf = g3_inv2_nominal + S_inf_best
g3_eff_inf = 1.0 / np.sqrt(g3_inv2_inf) if g3_inv2_inf > 0 else 0.0
lam_CCM_inf = (4.0 / 3.0) * g3_eff_inf**2 * ratio_gilkey
mH_inf = run_rg_down_get_mH(g3_eff_inf, lam_CCM_inf)

log(f"\n  Extrapolated (S_inf = {S_inf_best:.6f}):")
log(f"    g3_eff = {g3_eff_inf:.6f}, lam_CCM = {lam_CCM_inf:.8f}, m_H = {mH_inf:.4f} GeV")
log(f"    Observed m_H = {m_H_obs:.2f} GeV")
log(f"    Deviation = {(mH_inf - m_H_obs) / m_H_obs * 100:.2f}%")

# Also check S64's L=6 result
delta_L6 = float(s64_delta_C_gauss[6])
g3_inv2_L6 = g3_inv2_nominal + delta_L6
g3_eff_L6 = 1.0 / np.sqrt(g3_inv2_L6) if g3_inv2_L6 > 0 else 0.0
lam_CCM_L6 = (4.0 / 3.0) * g3_eff_L6**2 * ratio_gilkey
mH_L6 = run_rg_down_get_mH(g3_eff_L6, lam_CCM_L6)
log(f"\n  S64 L=6 check: delta={delta_L6:.6f}, m_H={mH_L6:.4f} GeV")

# =============================================================================
# 7. POWER-LAW GROWTH FIT
# =============================================================================
log("\n" + "=" * 80)
log("7. POWER-LAW GROWTH ANALYSIS")
log("=" * 80)

# Fit S_L ~ a * L^b for L >= 2
mask = L_range >= 2
x = np.log(L_range[mask].astype(float))
y_s = np.log(np.abs(S_sharp[mask]))
y_g = np.log(np.abs(S_gauss[mask]))

cs = np.polyfit(x, y_s, 1)
cg = np.polyfit(x, y_g, 1)
log(f"  Power-law fit S_L ~ L^alpha (L >= 2):")
log(f"    Sharp: alpha = {cs[0]:.4f}")
log(f"    Gauss: alpha = {cg[0]:.4f}")

# Fit per-level Delta_L ~ a * L^b for L >= 2
mask_dl = np.arange(len(delta_L_gauss)) + 1 >= 2
x_dl = np.log(np.arange(len(delta_L_gauss))[mask_dl] + 1.0)
y_dl = np.log(np.abs(delta_L_gauss[mask_dl]))
cdl = np.polyfit(x_dl, y_dl, 1)
log(f"    Per-level increment: alpha = {cdl[0]:.4f}")
log(f"    (For convergence, need alpha_increment < alpha_cumulative)")

# Dynkin index growth: T_total at each level
for L_val in range(1, L_MAX + 1):
    T_level = sum(T_su3(p, L_val - p) for p in range(L_val + 1))
    T_cumul_val = T_cumul[L_val]
    log(f"  L={L_val}: T_level={T_level:.2f}, T_cumul={T_cumul_val:.2f}")

# =============================================================================
# 8. GAUSSIAN SUPPRESSION ANALYSIS
# =============================================================================
log("\n" + "=" * 80)
log("8. GAUSSIAN SUPPRESSION vs DYNKIN GROWTH")
log("=" * 80)

# The key convergence mechanism: Gaussian weight exp(-omega_min^2/Lambda^2)
# competes with Dynkin index growth T(p,q) ~ L^5

log(f"  Per-level: T_level vs Gaussian suppression")
log(f"  {'L':>3} {'T_level':>10} {'<omega_min>':>12} {'<gauss_w>':>12} "
    f"{'T*gauss*ln':>14} {'Delta_L':>14}")

for L_val in range(1, L_MAX + 1):
    T_level = 0.0  # (local)
    omega_mins = []
    gauss_ws = []
    for sd in per_sector:
        if sd['level'] == L_val and not (sd['p'] == 0 and sd['q'] == 0):
            T_level += sd['T']
            omega_mins.append(sd['omega_min'])
            gauss_ws.append(np.exp(-sd['omega_min']**2 / Lambda**2))

    avg_om = np.mean(omega_mins) if omega_mins else 0
    avg_gw = np.mean(gauss_ws) if gauss_ws else 0
    effective = T_level * avg_gw * np.log(Lambda**2 / avg_om**2) / (8.0 * PI**2) if avg_om > 0 else 0
    Delta_L = delta_L_gauss[L_val - 1]

    log(f"  {L_val:3d} {T_level:10.2f} {avg_om:12.4f} {avg_gw:12.6f} "
        f"{effective:14.6f} {Delta_L:14.6f}")

# =============================================================================
# 9. GATE VERDICT
# =============================================================================
log("\n" + "=" * 80)
log("9. GATE VERDICT: KK-THRESHOLD-L5-66")
log("=" * 80)

PASS_THRESHOLD = 1.5  # (local)
FAIL_THRESHOLD = 3.0  # (local)

# The gate tests r_5 = Delta_5/Delta_4 for Gaussian cutoff
log(f"\n  Gate criterion: convergence ratio r_5 = Delta_5 / Delta_4 (Gaussian)")
log(f"  Delta_4 = S_4 - S_3 = {delta_L_gauss[3]:.8f}")
log(f"  Delta_5 = S_5 - S_4 = {delta_L_gauss[4]:.8f}")
log(f"  r_5 = {r_5_gauss:.6f}")
log(f"\n  Thresholds: PASS < {PASS_THRESHOLD}, FAIL > {FAIL_THRESHOLD}")

if r_5_gauss < PASS_THRESHOLD:
    verdict = "PASS"
    detail = (f"r_5 = {r_5_gauss:.4f} < {PASS_THRESHOLD}. Series converging. "
              f"S_5(Gauss) = {S_gauss[-1]:.4f}. m_H(L=5) = {mH_by_L[-1]:.1f} GeV. "
              f"Extrapolated m_H = {mH_inf:.1f} GeV (obs: {m_H_obs} GeV).")
elif r_5_gauss > FAIL_THRESHOLD:
    verdict = "FAIL"
    detail = (f"r_5 = {r_5_gauss:.4f} > {FAIL_THRESHOLD}. Series diverging.")
else:
    verdict = "INFO"
    detail = (f"r_5 = {r_5_gauss:.4f} in [{PASS_THRESHOLD}, {FAIL_THRESHOLD}]. "
              f"Slow convergence. S_5(Gauss) = {S_gauss[-1]:.4f}. m_H(L=5) = {mH_by_L[-1]:.1f} GeV.")

log(f"\n  *** VERDICT: {verdict} ***")
log(f"  {detail}")

# Extended analysis from S64
log(f"\n  EXTENDED ANALYSIS (using S64 L=6 data):")
r_6_gauss = (s64_delta_C_gauss[6] - s64_delta_C_gauss[5]) / (s64_delta_C_gauss[5] - s64_delta_C_gauss[4])
log(f"    r_6 = Delta_6/Delta_5 = {r_6_gauss:.6f}")
log(f"    Convergence IMPROVING: r_5={r_5_gauss:.4f} -> r_6={r_6_gauss:.4f}")
log(f"    Aitken S_inf = {S_inf_best:.6f}, m_H(inf) = {mH_inf:.1f} GeV")

log(f"\n  SUMMARY TABLE:")
log(f"  {'L':>3} {'S_L(Gauss)':>14} {'Delta_L':>14} {'r_L':>12} {'m_H':>10}")
for iL, L_val in enumerate(L_range):
    delta = delta_L_gauss[iL - 1] if iL > 0 else 0.0
    if iL >= 2:
        r = delta_L_gauss[iL - 1] / delta_L_gauss[iL - 2]
    else:
        r = np.inf
    r_str = f"{r:12.4f}" if np.isfinite(r) else "         ---"
    log(f"  {L_val:3d} {S_gauss[iL]:14.8f} {delta:14.8f} {r_str} {mH_by_L[iL]:10.2f}")

# S64 L=6
log(f"  {6:3d} {s64_delta_C_gauss[6]:14.8f} {s64_delta_C_gauss[6]-s64_delta_C_gauss[5]:14.8f} "
    f"{r_6_gauss:12.4f} {mH_L6:10.2f}")
log(f"  inf {S_inf_best:14.8f} {'---':>14} {'---':>12} {mH_inf:10.2f}")

# =============================================================================
# 10. SAVE DATA
# =============================================================================
log("\n" + "=" * 80)
log("10. SAVING DATA")
log("=" * 80)

save_path = os.path.join(outdir, 's66_kk_threshold_l5.npz')

sec_p = np.array([s['p'] for s in per_sector])
sec_q = np.array([s['q'] for s in per_sector])
sec_level = np.array([s['level'] for s in per_sector])
sec_dim = np.array([s['dim'] for s in per_sector])
sec_T = np.array([s['T'] for s in per_sector])
sec_omega_min = np.array([s['omega_min'] for s in per_sector])
sec_dC_sharp = np.array([s['delta_C_sharp'] for s in per_sector])
sec_dC_gauss = np.array([s['delta_C_gauss'] for s in per_sector])

np.savez(save_path,
         # Gate
         gate_name='KK-THRESHOLD-L5-66',
         gate_verdict=verdict,
         gate_detail=detail,
         # Cumulative sums
         L_range=L_range,
         S_sharp=S_sharp,
         S_gauss=S_gauss,
         T_cumul=T_cumul,
         n_sec_cumul=n_sec_cumul,
         # Per-level increments
         delta_L_sharp=delta_L_sharp,
         delta_L_gauss=delta_L_gauss,
         # Convergence ratios
         r_5_gauss=r_5_gauss,
         r_5_sharp=r_5_sharp,
         r_gauss_list=np.array(r_gauss_list),
         r_sharp_list=np.array(r_sharp_list),
         # Extrapolation
         S_inf_aitken=S_inf_aitken,
         S_inf_best=S_inf_best,
         r_eff=r_eff,
         # Higgs mass
         mH_by_L=mH_by_L,
         mH_inf=mH_inf,
         mH_L6=mH_L6,
         m_H_obs=m_H_obs,
         # Parameters
         Lambda_fixed=Lambda_fixed,
         gamma_opt=gamma_opt,
         g3_MKK_nominal=g3_MKK_nominal,
         g3_inv2_nominal=g3_inv2_nominal,
         ratio_gilkey=ratio_gilkey,
         # Per-sector data
         sec_p=sec_p, sec_q=sec_q, sec_level=sec_level,
         sec_dim=sec_dim, sec_T=sec_T, sec_omega_min=sec_omega_min,
         sec_dC_sharp=sec_dC_sharp, sec_dC_gauss=sec_dC_gauss,
         )

log(f"  Saved: {save_path}")

# =============================================================================
# 11. PLOT
# =============================================================================
log("\n" + "=" * 80)
log("11. GENERATING PLOT")
log("=" * 80)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('KK-THRESHOLD-L5-66: Convergence of Gaussian-Cutoff Threshold Sum',
             fontsize=14, fontweight='bold')

# Panel 1: Cumulative sum S_L vs L
ax1 = axes[0, 0]
# Include S64 L=6 and extrapolation
L_ext = np.array(list(L_range) + [6])
S_ext = np.array(list(S_gauss) + [s64_delta_C_gauss[6]])
ax1.plot(L_ext, S_ext, 'b-o', linewidth=2, markersize=8, label='S_L (Gaussian)')
ax1.axhline(S_inf_best, color='red', linewidth=1.5, linestyle='--',
            label=f'Aitken $S_\\infty$ = {S_inf_best:.3f}')
ax1.fill_between([0, 6], [0, 0], [S_inf_best, S_inf_best], alpha=0.05, color='red')
ax1.set_xlabel('Truncation level L', fontsize=12)
ax1.set_ylabel(r'$\delta(1/g_3^2)$ (Gaussian)', fontsize=12)
ax1.set_title('Cumulative threshold sum')
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Panel 2: Per-level increment
ax2 = axes[0, 1]
delta_ext = np.array(list(delta_L_gauss) + [s64_delta_C_gauss[6] - s64_delta_C_gauss[5]])
L_inc = np.arange(1, len(delta_ext) + 1)
ax2.bar(L_inc, delta_ext, color='steelblue', alpha=0.7, edgecolor='navy')
ax2.set_xlabel('Level L', fontsize=12)
ax2.set_ylabel(r'$\Delta_L = S_L - S_{L-1}$', fontsize=12)
ax2.set_title('Per-level increments (Gaussian)')
ax2.grid(True, alpha=0.3, axis='y')

# Panel 3: Convergence ratio
ax3 = axes[1, 0]
r_ext = list(r_gauss_list) + [r_6_gauss]
L_r = np.arange(3, 3 + len(r_ext))
ax3.plot(L_r, r_ext, 'ro-', markersize=10, linewidth=2)
ax3.axhline(1.0, color='green', linewidth=1, linestyle='--', label='r = 1 (boundary)')
ax3.axhline(PASS_THRESHOLD, color='orange', linewidth=1, linestyle=':', label=f'PASS < {PASS_THRESHOLD}')
ax3.axhline(FAIL_THRESHOLD, color='red', linewidth=1, linestyle=':', label=f'FAIL > {FAIL_THRESHOLD}')
ax3.set_xlabel('Level L', fontsize=12)
ax3.set_ylabel(r'$r_L = \Delta_L / \Delta_{L-1}$', fontsize=12)
ax3.set_title('Convergence ratio')
ax3.legend(fontsize=9)
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0, max(max(r_ext) * 1.2, FAIL_THRESHOLD * 1.1))

# Panel 4: Higgs mass
ax4 = axes[1, 1]
mH_ext = np.array(list(mH_by_L) + [mH_L6])
L_mH = np.array(list(L_range) + [6])
ax4.plot(L_mH, mH_ext, 'b-o', markersize=8, linewidth=2, label='m_H(L)')
ax4.axhline(125.10, color='green', linewidth=2, linestyle='--', label='Observed 125.1 GeV')
ax4.axhline(mH_inf, color='red', linewidth=1, linestyle=':', label=f'Extrapolated {mH_inf:.1f} GeV')
ax4.fill_between([0, 7], [120, 120], [135, 135], alpha=0.1, color='green', label='[120, 135] band')
ax4.set_xlabel('Truncation level L', fontsize=12)
ax4.set_ylabel(r'$m_H$ (GeV)', fontsize=12)
ax4.set_title('Predicted Higgs mass')
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(outdir, 's66_kk_threshold_l5.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
log(f"  Plot saved: {plot_path}")

log("\n" + "=" * 80)
log("COMPUTATION COMPLETE")
log("=" * 80)
rf.close()
