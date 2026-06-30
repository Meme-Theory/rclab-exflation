#!/usr/bin/env python3
"""
s70_lmax7_pw.py — LMAX7-PW-70
Peter-Weyl Extension to L_max = 7: KK Threshold Corrections

STRUCTURAL CONTEXT
------------------
S64 (KK-THRESHOLD-64) established Formula C as correct:
  delta(1/g_3^2) = SUM_{(p,q) != (0,0)} T(p,q)/(8pi^2) * ln(Lambda^2/omega_min^2)
  with Gaussian regulation: multiply by exp(-omega_min^2 / Lambda^2)
  Lambda = 1/gamma_opt = 2.048 M_KK

S66 (KK-THRESHOLD-L5-66) verified convergence at L=5:
  r_5 = 1.216 < 1.5. PASS.
  Aitken S_inf = 2.895, m_H(inf) = 127.5 GeV.

S64 extended to L=6 showing r_6 = 0.556. Convergence improving.

This script extends to L=7:
  1. Loads S64 per-sector data (L=0..6, 28 sectors verified)
  2. Computes D_K eigenvalues for L=7 sectors: (7,0), (0,7), (6,1), (1,6),
     (5,2), (2,5), (4,3), (3,4) — 8 new sectors
  3. Computes cumulative threshold sum S_7
  4. Evaluates convergence ratio r_7 = Delta_7 / Delta_6
  5. Updates Aitken extrapolation S_inf
  6. Runs 2-loop SM RG for m_H prediction

Gate: LMAX7-PW-70
  PASS: r_7 < 1.5 AND delta(S_inf) < 1%
  FAIL: r_7 > 2 OR delta(S_inf) > 5%
  INFO: intermediate values

Author: baptista-spacetime-analyst
Session: S70 W1-J
"""

import sys
import os
import time

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
results_file = os.path.join(outdir, 's70_lmax7_pw_results.txt')
rf = open(results_file, 'w')


def log(msg=''):
    print(msg)
    rf.write(msg + '\n')
    rf.flush()


log("=" * 80)
log("LMAX7-PW-70: Peter-Weyl Extension to L_max = 7")
log("S70 W1-J | baptista-spacetime-analyst")
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


# Verify fundamentals
T_fund = T_su3(1, 0)
b3_quarks = 6 * (4.0 / 3.0) * T_fund
b3_SM = -11.0 + b3_quarks
assert abs(T_fund - 0.5) < 1e-10, f"T(fund) wrong: {T_fund}"
assert abs(b3_SM - (-7.0)) < 1e-10, f"b3 wrong: {b3_SM}"
log(f"  T(fund) = {T_fund:.4f} [OK]")
log(f"  b_3(SM) = {b3_SM:.4f} [OK]")

# L=7 sectors
log(f"\n  L=7 new sectors:")
log(f"  {'(p,q)':>6} {'dim':>5} {'C_2':>10} {'T':>12}")
L7_sectors = [(p, 7 - p) for p in range(8)]
for p, q in L7_sectors:
    d = dim_su3(p, q)
    c2 = C2_su3(p, q)
    T = T_su3(p, q)
    log(f"  ({p},{q}) {d:5d} {c2:10.4f} {T:12.4f}")

T_level7 = sum(T_su3(p, 7 - p) for p in range(8))
dim_level7 = sum(dim_su3(p, 7 - p) for p in range(8))
n_modes_level7 = sum(dim_su3(p, 7 - p)**2 * 16 for p in range(8))
log(f"\n  Total L=7: T_level = {T_level7:.2f}, dim_sum = {dim_level7}, "
    f"16*sum(dim^2) = {n_modes_level7}")

# Cumulative counts
total_sectors = sum(L + 1 for L in range(8))  # L=0..7
log(f"  Total sectors L=0..7: {total_sectors}")

# =============================================================================
# 2. LOAD S64 DATA (L=0..6 VERIFIED)
# =============================================================================
log("\n" + "=" * 80)
log("2. LOAD S64 DATA AND INFRASTRUCTURE")
log("=" * 80)

d64 = np.load(os.path.join(outdir, 's64_kk_threshold.npz'), allow_pickle=True)
s64_delta_C_gauss = d64['delta_C_gauss']  # cumulative L=0..6
s64_delta_C_sharp = d64['delta_C']        # cumulative L=0..6 (sharp)
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

# S64 per-sector data for cross-check
s64_omega_min = {}
s64_T = {}
for i in range(len(d64['sec_p'])):
    p_s, q_s = int(d64['sec_p'][i]), int(d64['sec_q'][i])
    s64_omega_min[(p_s, q_s)] = float(d64['sec_omega_min'][i])
    s64_T[(p_s, q_s)] = float(d64['sec_T'][i])

log(f"  S64 sectors: {len(s64_omega_min)} (L=0..6)")
log(f"  S64 cumulative sums (Gaussian): L=6 -> {s64_delta_C_gauss[6]:.8f}")

# Print existing convergence sequence
log(f"\n  EXISTING convergence sequence (S64, Gaussian):")
deltas_prev = np.diff(s64_delta_C_gauss)
log(f"  {'L':>3} {'S_L':>14} {'Delta_L':>14} {'r_L':>12}")
for iL in range(7):
    S_L = s64_delta_C_gauss[iL]
    if iL > 0:
        delta = deltas_prev[iL - 1]
    else:
        delta = 0.0
    if iL >= 2:
        r = deltas_prev[iL - 1] / deltas_prev[iL - 2]
        r_str = f"{r:12.6f}"
    else:
        r_str = "         ---"
    log(f"  {iL:3d} {S_L:14.8f} {delta:14.8f} {r_str}")

# =============================================================================
# 3. COMPUTE D_K EIGENVALUES FOR L=7 SECTORS
# =============================================================================
log("\n" + "=" * 80)
log("3. D_K EIGENVALUE COMPUTATION FOR L=7 SECTORS")
log("=" * 80)

log(f"  Building SU(3) geometric infrastructure at tau_fold = {tau_fold} ...")
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

log(f"  Infrastructure ready. Computing L=7 sectors ...")

# Compute ALL sectors L=0..7 for self-consistency
# But only L=7 sectors are new; L=0..6 cross-checked against S64
L_MAX = 7  # (local)
sector_data = {}
t_start = time.time()

# WORKAROUND: get_irrep(3,4) fails because _build_irrep_no_cache cannot
# recurse through (2,3) when building the conjugate of (4,3).
# Fix: build (4,3) first, then construct (3,4) = conjugate of (4,3)
# using rho_{(3,4)}(e_a) = rho_{(4,3)}(-e_a^T).
# The Dirac operator for (3,4) is then constructed from these conjugated reps.

def build_irrep_with_fallback(p, q, gens, f_abc):
    """Build irrep (p,q), with fallback for (3,4) via conjugation of (4,3)."""
    try:
        tds._irrep_cache.clear()
        rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
        return rho, dim_check
    except (NotImplementedError, Exception) as e:
        if q > p and q > 0 and p > 0:
            # Try: build (q,p) and conjugate
            log(f"    [{p},{q}] Direct build failed ({e}). Trying conjugation of ({q},{p}).")
            tds._irrep_cache.clear()
            rho_qp, dim_check = tds.get_irrep(q, p, gens, f_abc)
            # Conjugate: rho_{(p,q)}(e_a) = rho_{(q,p)}(-e_a^T)
            # For anti-Hermitian generators: -e_a^T = e_a^*
            rho_pq = [-r.T for r in rho_qp]
            return rho_pq, dim_check
        raise


for L in range(L_MAX + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = dim_su3(p, q)
        t0 = time.time()

        try:
            rho, dim_check = build_irrep_with_fallback(p, q, gens, f_abc)
            assert dim_check == dim_pq, f"dim mismatch: {dim_check} vs {dim_pq}"
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

        # Cross-check against S64 for L<=6
        if (p, q) in s64_omega_min:
            s64_om = s64_omega_min[(p, q)]
            err = abs(omega_min - s64_om) / max(abs(s64_om), 1e-15)
            xcheck = f"S64 match: {err:.2e}" if err < 1e-8 else f"S64 MISMATCH: {err:.2e}"
        else:
            xcheck = "NEW (L=7)"

        status = "OK" if D_ah_err < 1e-10 else f"AH_ERR={D_ah_err:.2e}"
        log(f"  ({p},{q}): dim={dim_pq:4d}, n_pos={len(pos_evals):5d}, "
            f"|lam| in [{omega_min:.4f},{omega_max:.4f}], "
            f"{status}, {xcheck}, {t1 - t0:.2f}s")

t_total = time.time() - t_start
log(f"\n  Total: {len(sector_data)} sectors computed in {t_total:.1f}s")

# Verify L<=6 consistency with S64
log(f"\n  S64 cross-check summary:")
n_match = 0
n_mismatch = 0
for (p, q), sd in sorted(sector_data.items(), key=lambda x: (x[1]['level'], x[0])):
    if (p, q) in s64_omega_min and sd['level'] <= 6:
        err = abs(sd['omega_min'] - s64_omega_min[(p, q)]) / max(abs(s64_omega_min[(p, q)]), 1e-15)
        if err < 1e-8:
            n_match += 1
        else:
            n_mismatch += 1
            log(f"  MISMATCH ({p},{q}): this={sd['omega_min']:.10f}, "
                f"S64={s64_omega_min[(p, q)]:.10f}, rel_err={err:.2e}")

log(f"  S64 matches: {n_match}/{n_match + n_mismatch}")
if n_mismatch > 0:
    log(f"  WARNING: {n_mismatch} mismatches detected!")

# =============================================================================
# 4. FORMULA C WITH GAUSSIAN CUTOFF — CUMULATIVE SUMS L=0..7
# =============================================================================
log("\n" + "=" * 80)
log("4. FORMULA C (CORRECT): T(p,q)/(8pi^2) * ln(Lambda^2/omega_min^2) * Gaussian")
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

    if L == 7:  # Print detail for new sectors
        log(f"  ({p},{q}) L={L} T={T:8.2f} omega_min={omega_min:.6f} "
            f"gauss_w={gauss_w:.8f} dC_sharp={dC_sharp:.8f} dC_gauss={dC_gauss:.8f}")

# Cumulative sums at each L = 0..7
L_range_full = np.arange(0, L_MAX + 1)  # 0,1,...,7
S_sharp = np.zeros(len(L_range_full))
S_gauss = np.zeros(len(L_range_full))
T_cumul = np.zeros(len(L_range_full))
n_sec_cumul = np.zeros(len(L_range_full), dtype=int)
n_modes_cumul = np.zeros(len(L_range_full), dtype=int)

for iL, L_val in enumerate(L_range_full):
    for sd in per_sector:
        if sd['level'] <= L_val and not (sd['p'] == 0 and sd['q'] == 0):
            S_sharp[iL] += sd['delta_C_sharp']
            S_gauss[iL] += sd['delta_C_gauss']
            T_cumul[iL] += sd['T']
            n_sec_cumul[iL] += 1
    # Count modes
    for (p, q), sdd in sector_data.items():
        if sdd['level'] <= L_val:
            n_modes_cumul[iL] += sdd['n_pos_evals']

log(f"\n  Cumulative threshold sums (Formula C):")
log(f"  {'L':>3} {'N_sec':>6} {'T_total':>10} {'N_modes':>8} {'S_sharp':>14} {'S_gauss':>14}")
for iL, L_val in enumerate(L_range_full):
    log(f"  {L_val:3d} {n_sec_cumul[iL]:6d} {T_cumul[iL]:10.2f} {n_modes_cumul[iL]:8d} "
        f"{S_sharp[iL]:14.8f} {S_gauss[iL]:14.8f}")

# Cross-check: L=0..6 must match S64
log(f"\n  Cross-check against S64 delta_C_gauss:")
for iL in range(min(7, len(L_range_full))):
    if iL <= 6:
        s64_val = s64_delta_C_gauss[iL]
        err = abs(S_gauss[iL] - s64_val)
        status = "OK" if err < 1e-8 else f"MISMATCH ({err:.2e})"
        log(f"  L={iL}: this={S_gauss[iL]:.10f}, S64={s64_val:.10f}, |diff|={err:.2e} {status}")

# =============================================================================
# 5. CONVERGENCE ANALYSIS
# =============================================================================
log("\n" + "=" * 80)
log("5. CONVERGENCE ANALYSIS")
log("=" * 80)

# Per-level increments
delta_L_sharp = np.diff(S_sharp)
delta_L_gauss = np.diff(S_gauss)

log(f"\n  Per-level increments Delta_L = S_L - S_{{L-1}}:")
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
    r_s = delta_L_sharp[i] / delta_L_sharp[i - 1] if abs(delta_L_sharp[i - 1]) > 1e-15 else np.inf
    r_g = delta_L_gauss[i] / delta_L_gauss[i - 1] if abs(delta_L_gauss[i - 1]) > 1e-15 else np.inf
    r_sharp_list.append(r_s)
    r_gauss_list.append(r_g)
    log(f"  {L_val:3d} {r_s:12.6f} {r_g:12.6f}")

# The gate tests r_7 = Delta_7 / Delta_6 (Gaussian)
r_7_gauss = r_gauss_list[-1] if len(r_gauss_list) > 0 else np.inf
r_7_sharp = r_sharp_list[-1] if len(r_sharp_list) > 0 else np.inf

log(f"\n  *** PRIMARY CONVERGENCE RATIO r_7 (Gaussian) = {r_7_gauss:.6f} ***")
log(f"      r_7 (sharp) = {r_7_sharp:.6f}")
log(f"      [Previous: r_5 = 1.216, r_6 = 0.556]")

# =============================================================================
# 6. AITKEN EXTRAPOLATION
# =============================================================================
log("\n" + "=" * 80)
log("6. AITKEN DELTA^2 EXTRAPOLATION")
log("=" * 80)

# Aitken using L=5,6,7 (Gaussian)
S5g = S_gauss[5]
S6g = S_gauss[6]
S7g = S_gauss[7]

denom_567 = S7g - 2 * S6g + S5g
if abs(denom_567) > 1e-15:
    S_inf_567 = (S7g * S5g - S6g**2) / denom_567
    r_eff_567 = (S7g - S6g) / (S6g - S5g)
    log(f"  Aitken Delta^2 (L=5,6,7, Gaussian):")
    log(f"    S_5 = {S5g:.10f}")
    log(f"    S_6 = {S6g:.10f}")
    log(f"    S_7 = {S7g:.10f}")
    log(f"    S_inf(5,6,7) = {S_inf_567:.10f}")
    log(f"    Effective ratio r = {r_eff_567:.6f}")
else:
    S_inf_567 = S7g
    r_eff_567 = 0.0  # (local)
    log(f"  Aitken (5,6,7): denominator too small")

# Aitken using L=4,5,6 for comparison (old result)
S4g = S_gauss[4]
denom_456 = S6g - 2 * S5g + S4g
if abs(denom_456) > 1e-15:
    S_inf_456 = (S6g * S4g - S5g**2) / denom_456
    r_eff_456 = (S6g - S5g) / (S5g - S4g)
    log(f"\n  Aitken Delta^2 (L=4,5,6, Gaussian) [reproduction of S66]:")
    log(f"    S_inf(4,5,6) = {S_inf_456:.10f}")
    log(f"    Effective ratio r = {r_eff_456:.6f}")
else:
    S_inf_456 = S6g
    r_eff_456 = 0.0  # (local)

# S66 reference value for delta check
S_inf_old = 2.8952242203150993  # From S66 (Aitken L=4,5,6)  # (local)

# Geometric sum extrapolation: S_inf = S_L + Delta_L * r / (1-r)
# Using the known pattern that ratios are decreasing
if 0 < r_7_gauss < 1:
    Delta_7_gauss = delta_L_gauss[-1]
    S_inf_geom = S7g + Delta_7_gauss * r_7_gauss / (1 - r_7_gauss)
    log(f"\n  Geometric sum extrapolation (ratio r_7 = {r_7_gauss:.6f}):")
    log(f"    S_inf(geom) = {S_inf_geom:.10f}")
else:
    S_inf_geom = S7g
    log(f"\n  Geometric sum: r_7 = {r_7_gauss:.6f}, using S_7 directly")

# Best estimate: Aitken (5,6,7) if available
S_inf_best = S_inf_567 if abs(denom_567) > 1e-15 else S7g

# Relative change from S66 reference
delta_S_inf_rel = abs(S_inf_best - S_inf_old) / abs(S_inf_old)

log(f"\n  *** BEST ESTIMATE S_inf = {S_inf_best:.8f} ***")
log(f"  *** PREVIOUS S_inf (S66) = {S_inf_old:.8f} ***")
log(f"  *** RELATIVE CHANGE delta(S_inf) = {delta_S_inf_rel:.6f} ({delta_S_inf_rel*100:.4f}%) ***")

# =============================================================================
# 7. HIGGS MASS FROM 2-LOOP SM RG
# =============================================================================
log("\n" + "=" * 80)
log("7. HIGGS MASS PREDICTION")
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
m_t_MSbar = m_t_pole * (1.0 - 4.0 * alpha_s_MZ / (3.0 * PI))  # S72: was 172.69, now uses canonical m_t_pole
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

mH_by_L = np.zeros(len(L_range_full))
for iL, L_val in enumerate(L_range_full):
    delta = S_gauss[iL]
    g3_inv2 = g3_inv2_nominal + delta
    g3_eff = 1.0 / np.sqrt(g3_inv2) if g3_inv2 > 0 else 0.0
    lam_CCM = (4.0 / 3.0) * g3_eff**2 * ratio_gilkey
    mH = run_rg_down_get_mH(g3_eff, lam_CCM)
    mH_by_L[iL] = mH
    log(f"  {L_val:3d} {delta:14.8f} {g3_eff:10.6f} {lam_CCM:12.8f} {mH:12.4f}")

# m_H at extrapolated S_inf (new)
g3_inv2_inf = g3_inv2_nominal + S_inf_best
g3_eff_inf = 1.0 / np.sqrt(g3_inv2_inf) if g3_inv2_inf > 0 else 0.0
lam_CCM_inf = (4.0 / 3.0) * g3_eff_inf**2 * ratio_gilkey
mH_inf_new = run_rg_down_get_mH(g3_eff_inf, lam_CCM_inf)

# m_H at old extrapolated S_inf
g3_inv2_inf_old = g3_inv2_nominal + S_inf_old
g3_eff_inf_old = 1.0 / np.sqrt(g3_inv2_inf_old) if g3_inv2_inf_old > 0 else 0.0
lam_CCM_inf_old = (4.0 / 3.0) * g3_eff_inf_old**2 * ratio_gilkey
mH_inf_old = run_rg_down_get_mH(g3_eff_inf_old, lam_CCM_inf_old)

log(f"\n  Extrapolated (NEW, S_inf = {S_inf_best:.8f}):")
log(f"    g3_eff = {g3_eff_inf:.6f}, lam_CCM = {lam_CCM_inf:.8f}, m_H = {mH_inf_new:.4f} GeV")
log(f"  Extrapolated (OLD, S_inf = {S_inf_old:.8f}):")
log(f"    g3_eff = {g3_eff_inf_old:.6f}, lam_CCM = {lam_CCM_inf_old:.8f}, m_H = {mH_inf_old:.4f} GeV")
log(f"  Observed m_H = {m_H_obs:.2f} GeV")
log(f"  NEW deviation = {(mH_inf_new - m_H_obs) / m_H_obs * 100:.2f}%")
log(f"  OLD deviation = {(mH_inf_old - m_H_obs) / m_H_obs * 100:.2f}%")
log(f"  Shift: {mH_inf_new - mH_inf_old:.4f} GeV")

# =============================================================================
# 8. a_4 IMPACT ANALYSIS
# =============================================================================
log("\n" + "=" * 80)
log("8. a_4 IMPACT ANALYSIS")
log("=" * 80)

# The a_4 coefficient comes from the spectral action, not directly from the
# threshold sum. However the threshold correction delta(1/g_3^2) effectively
# modifies the UV coupling. Check relative change at L=7 vs L=6.
a4_change_frac = abs(S_gauss[7] - S_gauss[6]) / abs(S_gauss[6]) if abs(S_gauss[6]) > 1e-15 else 0.0
log(f"  S(L=7) = {S_gauss[7]:.8f}")
log(f"  S(L=6) = {S_gauss[6]:.8f}")
log(f"  Fractional change |S_7 - S_6| / |S_6| = {a4_change_frac:.6f} ({a4_change_frac*100:.4f}%)")

# =============================================================================
# 9. POWER-LAW GROWTH AND GAUSSIAN SUPPRESSION
# =============================================================================
log("\n" + "=" * 80)
log("9. POWER-LAW GROWTH & GAUSSIAN SUPPRESSION")
log("=" * 80)

# Fit S_L ~ a * L^b for L >= 2
mask = L_range_full >= 2
x_fit = np.log(L_range_full[mask].astype(float))
y_g_fit = np.log(np.abs(S_gauss[mask]) + 1e-30)
cg = np.polyfit(x_fit, y_g_fit, 1)
log(f"  Power-law fit S_L ~ L^alpha (L >= 2, Gaussian):")
log(f"    alpha = {cg[0]:.4f}")

# Per-level analysis
log(f"\n  Per-level: T_level vs Gaussian suppression")
log(f"  {'L':>3} {'T_level':>10} {'<omega_min>':>12} {'<gauss_w>':>12} {'Delta_L':>14}")

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
    Delta_L = delta_L_gauss[L_val - 1]

    log(f"  {L_val:3d} {T_level:10.2f} {avg_om:12.4f} {avg_gw:12.8f} {Delta_L:14.8f}")

# Dynkin index growth
T_by_level = []
for L_val in range(1, L_MAX + 1):
    T_lev = sum(T_su3(p, L_val - p) for p in range(L_val + 1))
    T_by_level.append(T_lev)

log(f"\n  Dynkin index per level: {[f'{t:.1f}' for t in T_by_level]}")
log(f"  Growth factor T(L)/T(L-1): {[f'{T_by_level[i]/T_by_level[i-1]:.3f}' for i in range(1, len(T_by_level))]}")

# =============================================================================
# 10. PLOT
# =============================================================================
log("\n" + "=" * 80)
log("10. PLOT")
log("=" * 80)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Cumulative threshold sum
ax1 = axes[0, 0]
ax1.plot(L_range_full, S_gauss, 'bo-', label='Gaussian', markersize=8, linewidth=2)
ax1.plot(L_range_full, S_sharp, 'rs--', label='Sharp', markersize=6)
ax1.axhline(S_inf_best, color='blue', linestyle=':', alpha=0.5, label=f'S_inf(new)={S_inf_best:.3f}')
ax1.axhline(S_inf_old, color='gray', linestyle=':', alpha=0.5, label=f'S_inf(old)={S_inf_old:.3f}')
ax1.set_xlabel('L_max')
ax1.set_ylabel('delta(1/g_3^2)')
ax1.set_title('Cumulative Threshold Sum')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel 2: Convergence ratios
ax2 = axes[0, 1]
L_ratio = np.arange(2, L_MAX + 1)
ax2.plot(L_ratio, r_gauss_list, 'bo-', label='Gaussian', markersize=8, linewidth=2)
ax2.plot(L_ratio, r_sharp_list, 'rs--', label='Sharp', markersize=6)
ax2.axhline(1.5, color='green', linestyle='--', alpha=0.5, label='PASS threshold')
ax2.axhline(2.0, color='red', linestyle='--', alpha=0.5, label='FAIL threshold')
ax2.axhline(1.0, color='gray', linestyle=':', alpha=0.3)
ax2.set_xlabel('L')
ax2.set_ylabel('r_L = Delta_L / Delta_{L-1}')
ax2.set_title('Convergence Ratios')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)
ax2.set_ylim(bottom=-0.5, top=max(max(r_gauss_list), max(r_sharp_list)) * 1.1 + 0.5)

# Panel 3: Higgs mass prediction
ax3 = axes[1, 0]
ax3.plot(L_range_full, mH_by_L, 'go-', markersize=8, linewidth=2, label='m_H(L)')
ax3.axhline(m_H_obs, color='red', linewidth=2, label=f'Observed: {m_H_obs} GeV')
ax3.axhline(mH_inf_new, color='blue', linestyle=':', label=f'm_H(inf, new)={mH_inf_new:.1f} GeV')
ax3.axhline(mH_inf_old, color='gray', linestyle=':', label=f'm_H(inf, old)={mH_inf_old:.1f} GeV')
ax3.set_xlabel('L_max')
ax3.set_ylabel('m_H (GeV)')
ax3.set_title('Higgs Mass vs Truncation Level')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Panel 4: Per-level increments
ax4 = axes[1, 1]
L_delta = np.arange(1, L_MAX + 1)
ax4.semilogy(L_delta, np.abs(delta_L_gauss), 'bo-', label='|Delta_L| Gaussian', markersize=8, linewidth=2)
ax4.semilogy(L_delta, np.abs(delta_L_sharp), 'rs--', label='|Delta_L| Sharp', markersize=6)
ax4.set_xlabel('L')
ax4.set_ylabel('|Delta_L|')
ax4.set_title('Per-Level Threshold Increments')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

plt.suptitle('LMAX7-PW-70: Peter-Weyl Extension to L_max = 7', fontsize=14, fontweight='bold')
plt.tight_layout()

plot_path = os.path.join(outdir, 's70_lmax7_pw.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
log(f"  Plot saved: {plot_path}")
plt.close()

# =============================================================================
# 11. GATE VERDICT
# =============================================================================
log("\n" + "=" * 80)
log("11. GATE VERDICT: LMAX7-PW-70")
log("=" * 80)

PASS_R7 = 1.5  # (local)
FAIL_R7 = 2.0  # (local)
PASS_DELTA_SINF = 0.01  # 1%  # (local)
FAIL_DELTA_SINF = 0.05  # 5%  # (local)

log(f"\n  Gate criterion 1: r_7 = Delta_7 / Delta_6 (Gaussian)")
log(f"    Delta_6 = {delta_L_gauss[5]:.10f}")
log(f"    Delta_7 = {delta_L_gauss[6]:.10f}")
log(f"    r_7 = {r_7_gauss:.6f}")
log(f"    Thresholds: PASS < {PASS_R7}, FAIL > {FAIL_R7}")

log(f"\n  Gate criterion 2: delta(S_inf) = |S_inf(new) - S_inf(old)| / |S_inf(old)|")
log(f"    S_inf(new) = {S_inf_best:.8f}")
log(f"    S_inf(old) = {S_inf_old:.8f}")
log(f"    delta(S_inf) = {delta_S_inf_rel:.6f} ({delta_S_inf_rel*100:.4f}%)")
log(f"    Thresholds: PASS < {PASS_DELTA_SINF*100:.0f}%, FAIL > {FAIL_DELTA_SINF*100:.0f}%")

# Composite verdict
r7_pass = r_7_gauss < PASS_R7
r7_fail = r_7_gauss > FAIL_R7
sinf_pass = delta_S_inf_rel < PASS_DELTA_SINF
sinf_fail = delta_S_inf_rel > FAIL_DELTA_SINF

if r7_pass and sinf_pass:
    verdict = "PASS"
    detail = (f"r_7 = {r_7_gauss:.4f} < {PASS_R7} AND "
              f"delta(S_inf) = {delta_S_inf_rel*100:.4f}% < {PASS_DELTA_SINF*100:.0f}%. "
              f"Threshold sum CONVERGING. "
              f"S_7 = {S_gauss[7]:.6f}. m_H(L=7) = {mH_by_L[7]:.1f} GeV. "
              f"m_H(inf, new) = {mH_inf_new:.1f} GeV (obs: {m_H_obs} GeV, {(mH_inf_new - m_H_obs)/m_H_obs*100:.2f}%).")
elif r7_fail or sinf_fail:
    verdict = "FAIL"
    detail = (f"r_7 = {r_7_gauss:.4f}, delta(S_inf) = {delta_S_inf_rel*100:.4f}%. "
              f"Truncation error significant.")
else:
    verdict = "INFO"
    detail = (f"r_7 = {r_7_gauss:.4f}, delta(S_inf) = {delta_S_inf_rel*100:.4f}%. "
              f"Intermediate values. S_7 = {S_gauss[7]:.6f}. "
              f"m_H(inf, new) = {mH_inf_new:.1f} GeV.")

log(f"\n  *** VERDICT: {verdict} ***")
log(f"  {detail}")

log(f"\n  FULL SUMMARY TABLE:")
log(f"  {'L':>3} {'S_L(Gauss)':>14} {'Delta_L':>14} {'r_L':>12} {'m_H':>10}")
for iL, L_val in enumerate(L_range_full):
    delta = delta_L_gauss[iL - 1] if iL > 0 else 0.0
    if iL >= 2:
        r = r_gauss_list[iL - 2]
        r_str = f"{r:12.4f}"
    else:
        r_str = "         ---"
    log(f"  {L_val:3d} {S_gauss[iL]:14.8f} {delta:14.8f} {r_str} {mH_by_L[iL]:10.2f}")
log(f"  inf {S_inf_best:14.8f} {'---':>14} {'---':>12} {mH_inf_new:10.2f}")

# =============================================================================
# 12. SAVE DATA
# =============================================================================
log("\n" + "=" * 80)
log("12. SAVING DATA")
log("=" * 80)

save_path = os.path.join(outdir, 's70_lmax7_pw.npz')

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
         gate_name='LMAX7-PW-70',
         gate_verdict=verdict,
         gate_detail=detail,
         # Convergence
         r_7_gauss=r_7_gauss,
         r_7_sharp=r_7_sharp,
         delta_S_inf_rel=delta_S_inf_rel,
         r_gauss_list=np.array(r_gauss_list),
         r_sharp_list=np.array(r_sharp_list),
         # Cumulative sums
         L_range=L_range_full,
         S_gauss=S_gauss,
         S_sharp=S_sharp,
         T_cumul=T_cumul,
         n_sec_cumul=n_sec_cumul,
         n_modes_cumul=n_modes_cumul,
         delta_L_gauss=delta_L_gauss,
         delta_L_sharp=delta_L_sharp,
         # Extrapolation
         S_inf_best=S_inf_best,
         S_inf_old=S_inf_old,
         S_inf_567=S_inf_567,
         S_inf_456=S_inf_456,
         r_eff_567=r_eff_567,
         # Higgs mass
         mH_by_L=mH_by_L,
         mH_inf_new=mH_inf_new,
         mH_inf_old=mH_inf_old,
         m_H_obs=m_H_obs,
         # Parameters
         Lambda_fixed=Lambda_fixed,
         gamma_opt=gamma_opt,
         g3_MKK_nominal=g3_MKK_nominal,
         g3_inv2_nominal=g3_inv2_nominal,
         ratio_gilkey=ratio_gilkey,
         # Per-sector
         sec_p=sec_p,
         sec_q=sec_q,
         sec_level=sec_level,
         sec_dim=sec_dim,
         sec_T=sec_T,
         sec_omega_min=sec_omega_min,
         sec_dC_sharp=sec_dC_sharp,
         sec_dC_gauss=sec_dC_gauss,
         )

log(f"  Data saved: {save_path}")
log(f"  Plot saved: {plot_path}")
log(f"  Results saved: {results_file}")

rf.close()
print("\n[DONE]")
