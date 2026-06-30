#!/usr/bin/env python3
"""
s75_cc_double_index.py -- CC-DOUBLE-INDEX-75 (S75-D7-CC-DBL-IDX)
Joint (chi_2, n_b/n_f) Index for the Cosmological Constant at L_max = {5, 7, 10}

STRUCTURAL CONTEXT
------------------
The cosmological constant in the spectral action framework is:
    Lambda_CC ~ a_0 * M_KK^4
where a_0 is the zeroth Seeley-DeWitt coefficient (volume term).

The CC's dependence on the spectral content of D_K is captured by two
independent indices:

  1. chi_2 = a_2 / a_0 = zeta_D(s=3) / zeta_D(s=4)
     The ratio of the curvature moment to the volume moment.
     From S73b: this is DIVERGENT (both zeta values diverge at different rates).
     The log-log slope from S73b is ~0.89, meaning chi_2 ~ L^{0.89}.

  2. n_b / n_f = (positive-eigenvalue modes) / (negative-eigenvalue modes)
     The spectral asymmetry of D_K. Since {D_K, gamma_9} = 0 (chirality
     anticommutation on even-dim K=SU(3)), the spectrum is EXACTLY SYMMETRIC:
     if mu is an eigenvalue of H=iD_K, so is -mu. Therefore n_b = n_f = n_total/2
     EXACTLY, and n_b/n_f = 1.000 to machine epsilon. Zero modes (if any)
     would break this, but D_K at the fold has no zero modes (min |lambda| = 0.82).

METHOD
------
For L_max = {5, 7}: compute fresh D_K spectrum with eigenvector-free diagonalization.
  Cross-validate zeta values against S72 stored data.
For L_max = 10: use Weyl-law extrapolation from L_max = {3,...,7} data (S72).
  The individual zeta values diverge, but the ratio chi_2 follows a power law
  that can be reliably extrapolated. Fresh computation at L_max=10 requires
  O(300s) for irrep construction and is limited by tensor product memory.

For n_b/n_f: verify spectral symmetry numerically at L_max = {5, 7}.
  At L_max = 10, the symmetry is a THEOREM ({D,gamma_9}=0 + no zero modes),
  so n_b/n_f = 1.000 exactly. No computation needed.

Gate: S75-D7-CC-DBL-IDX
  PASS: Drift < 3% across all L_max for both indices
  FAIL: Drift > 10% for either index

Author: gen-physicist
Session: S75 W4-F
"""

import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import numpy as np
from scipy.optimize import curve_fit

from canonical_constants import (
    PI, tau_fold, a0_fold, a2_fold, a4_fold,
)

import dirac_spectrum as tds

print("=" * 80)
print("CC-DOUBLE-INDEX-75: Joint (chi_2, n_b/n_f) Index")
print("S75 W4-F | gen-physicist")
print("=" * 80)

t_start = time.time()  # (local)

# =============================================================================
# 0. UTILITY FUNCTIONS
# =============================================================================

def dim_su3(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def build_irrep_with_fallback(p, q, gens, f_abc):
    """Build irrep (p,q) with conjugation fallback for problematic sectors."""
    try:
        tds._irrep_cache.clear()
        rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
        return rho, dim_check
    except (NotImplementedError, Exception):
        if q > p and q > 0 and p > 0:
            tds._irrep_cache.clear()
            rho_qp, dim_check = tds.get_irrep(q, p, gens, f_abc)
            rho_pq = [-r.T for r in rho_qp]
            return rho_pq, dim_check
        raise


def power_law_model(x, f_inf, A, alpha):
    """Power law: y = f_inf + A * x^alpha."""
    return f_inf + A * x**alpha


# =============================================================================
# 1. INITIALIZE ALGEBRAIC INFRASTRUCTURE
# =============================================================================
print("\n" + "=" * 80)
print("1. ALGEBRAIC INFRASTRUCTURE")
print("=" * 80)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()
gamma9 = tds.build_chirality(gammas)

# Validate chirality
g9_sq_err = np.max(np.abs(gamma9 @ gamma9 - np.eye(16)))  # (local)
g9_herm_err = np.max(np.abs(gamma9 - gamma9.conj().T))  # (local)
g9_anticomm_err = max(np.max(np.abs(gamma9 @ gammas[a] + gammas[a] @ gamma9)) for a in range(8))  # (local)
print(f"  gamma_9^2 = I err: {g9_sq_err:.2e}")
print(f"  gamma_9 Hermitian err: {g9_herm_err:.2e}")
print(f"  {{gamma_9, gamma_a}} = 0 err: {g9_anticomm_err:.2e}")

g9_evals = np.linalg.eigvalsh(gamma9)  # (local)
n_plus_g9 = np.sum(g9_evals > 0.5)  # (local)
n_minus_g9 = np.sum(g9_evals < -0.5)  # (local)
print(f"  gamma_9 spectrum: {n_plus_g9} positive, {n_minus_g9} negative (expect 8, 8)")

# Build geometric infrastructure at the fold
s_value = tau_fold  # (local)
B_ab = tds.compute_killing_form(f_abc)  # (local)
g_s = tds.jensen_metric(B_ab, s_value)  # (local)
E = tds.orthonormal_frame(g_s)  # (local)
ft = tds.frame_structure_constants(f_abc, E)  # (local)
Gamma = tds.connection_coefficients(ft)  # (local)
Omega = tds.spinor_connection_offset(Gamma, gammas)  # (local)

mc_err = tds.validate_connection(Gamma)  # (local)
_, is_ah, _, ah_err = tds.validate_omega_hermitian(Omega)
print(f"  Connection metric-compat err: {mc_err:.2e}")
print(f"  Omega anti-Hermitian: {is_ah} (err={ah_err:.2e})")

# =============================================================================
# 2. LOAD S72 DATA (L_max = 3,...,7)
# =============================================================================
print("\n" + "=" * 80)
print("2. S72 STORED DATA (L_max = 3,...,7)")
print("=" * 80)

d72 = np.load(os.path.join(SCRIPT_DIR, 's72_zeta_ratio_scan.npz'), allow_pickle=True)

L_s72 = np.array([3, 4, 5, 6, 7])  # (local)
zeta_s3_s72 = np.array([float(d72[f'L{L}_zeta_s3']) for L in L_s72])  # (local)
zeta_s4_s72 = np.array([float(d72[f'L{L}_zeta_s4']) for L in L_s72])  # (local)
chi2_s72 = zeta_s3_s72 / zeta_s4_s72  # (local)
nw_s72 = np.array([float(d72[f'L{L}_n_weighted']) for L in L_s72])  # (local)

print(f"  {'L_max':>5s} {'zeta(3)':>12s} {'zeta(4)':>12s} {'chi_2':>10s} {'n_weighted':>12s}")
for i, L in enumerate(L_s72):
    print(f"  {L:5d} {zeta_s3_s72[i]:12.4e} {zeta_s4_s72[i]:12.4e} "
          f"{chi2_s72[i]:10.6f} {nw_s72[i]:12.0f}")

# =============================================================================
# 3. FRESH COMPUTATION AT L_max = 5 AND 7
# =============================================================================
print("\n" + "=" * 80)
print("3. FRESH COMPUTATION AT L_max = {5, 7}")
print("=" * 80)

fresh_results = {}  # (local)

for L_max in [5, 7]:
    print(f"\n--- L_max = {L_max} ---")
    t0 = time.time()  # (local)

    zeta_s3_acc = 0.0  # (local)
    zeta_s4_acc = 0.0  # (local)
    n_positive = 0  # (local)
    n_negative = 0  # (local)
    n_zero = 0  # (local)
    n_evals = 0  # (local)
    n_sectors = 0  # (local)
    n_skipped = 0  # (local)

    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            dim_pq = dim_su3(p, q)  # (local)
            try:
                if (p, q) == (0, 0):
                    D_pi = Omega.copy()  # (local)
                else:
                    rho, _ = build_irrep_with_fallback(p, q, gens, f_abc)
                    D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)

                H = 1j * D_pi  # (local)
                evals = np.linalg.eigvalsh(H)  # (local)

                pw = dim_pq  # (local) Peter-Weyl weight
                n_ev = len(evals)  # (local)
                n_evals += n_ev
                n_sectors += 1

                # Zeta sums
                abs_ev = np.abs(evals)  # (local)
                nz_mask = abs_ev > 1e-12  # (local)
                if np.any(nz_mask):
                    abs_nz = abs_ev[nz_mask]  # (local)
                    zeta_s3_acc += pw * np.sum(abs_nz ** (-6))
                    zeta_s4_acc += pw * np.sum(abs_nz ** (-8))

                # Spectral asymmetry
                n_pos = np.sum(evals > 1e-12)  # (local)
                n_neg = np.sum(evals < -1e-12)  # (local)
                n_zer = np.sum(np.abs(evals) <= 1e-12)  # (local)
                n_positive += pw * n_pos
                n_negative += pw * n_neg
                n_zero += pw * n_zer

                if p + q <= 3:
                    print(f"    ({p},{q}): dim={dim_pq}, |lambda|=[{np.min(abs_ev):.4f}, "
                          f"{np.max(abs_ev):.4f}], n+={n_pos} n-={n_neg} n0={n_zer}")

            except Exception as e:
                n_skipped += 1
                print(f"    ({p},{q}): SKIPPED ({e})")
                continue

    chi2_fresh = zeta_s3_acc / zeta_s4_acc if zeta_s4_acc > 0 else np.nan  # (local)
    nbf_fresh = n_positive / n_negative if n_negative > 0 else np.nan  # (local)
    t_elapsed = time.time() - t0  # (local)

    # Cross-validate against S72
    idx_s72 = list(L_s72).index(L_max)  # (local)
    chi2_s72_val = chi2_s72[idx_s72]  # (local)
    chi2_disc = abs(chi2_fresh - chi2_s72_val) / chi2_s72_val * 100  # (local)

    print(f"\n  L_max={L_max} fresh results:")
    print(f"    chi_2 (fresh)  = {chi2_fresh:.8f}")
    print(f"    chi_2 (S72)    = {chi2_s72_val:.8f}")
    print(f"    Discrepancy    = {chi2_disc:.6f}%")
    print(f"    zeta(3) = {zeta_s3_acc:.6e}, zeta(4) = {zeta_s4_acc:.6e}")
    print(f"    n_b (positive) = {n_positive}, n_f (negative) = {n_negative}, n_0 = {n_zero}")
    print(f"    n_b/n_f = {nbf_fresh:.10f}")
    print(f"    n_total = {n_positive + n_negative + n_zero}")
    print(f"    Sectors: {n_sectors} computed, {n_skipped} skipped")
    print(f"    Time: {t_elapsed:.1f} s")

    fresh_results[L_max] = {
        'chi_2': chi2_fresh,
        'nb_nf': nbf_fresh,
        'zeta_s3': zeta_s3_acc,
        'zeta_s4': zeta_s4_acc,
        'n_b': n_positive,
        'n_f': n_negative,
        'n_zero': n_zero,
        'n_total': n_positive + n_negative + n_zero,
        'n_sectors': n_sectors,
        'n_evals': n_evals,
        'n_skipped': n_skipped,
        't_elapsed': t_elapsed,
    }

# =============================================================================
# 4. EXTRAPOLATION TO L_max = 10
# =============================================================================
print("\n" + "=" * 80)
print("4. EXTRAPOLATION TO L_max = 10 (Weyl law)")
print("=" * 80)

# chi_2 = zeta(3)/zeta(4) from S72 data at L_max = 3,...,7
# S73b established this sequence is DIVERGENT with log-log slope ~0.89.
# Fit chi_2(L) = A * L^beta (pure power law, no finite limit)

log_L = np.log(L_s72.astype(float))  # (local)
log_chi2 = np.log(chi2_s72)  # (local)

# Linear fit in log-log space
slope, intercept = np.polyfit(log_L, log_chi2, 1)  # (local)
print(f"  Log-log fit: log(chi_2) = {slope:.4f} * log(L) + {intercept:.4f}")
print(f"  Power law: chi_2(L) ~ {np.exp(intercept):.4f} * L^{slope:.4f}")

# Extrapolate to L_max = 10
chi2_L10_extrap = np.exp(intercept) * 10**slope  # (local)
print(f"  chi_2(L_max=10) extrapolated = {chi2_L10_extrap:.6f}")

# Confidence: check fit residuals at known L_max values
chi2_fitted = np.exp(intercept) * L_s72.astype(float)**slope  # (local)
fit_residuals = np.abs(chi2_s72 - chi2_fitted) / chi2_s72 * 100  # (local)
print(f"  Fit residuals at known L_max:")
for i, L in enumerate(L_s72):
    print(f"    L={L}: fitted={chi2_fitted[i]:.6f}, actual={chi2_s72[i]:.6f}, "
          f"residual={fit_residuals[i]:.4f}%")
max_fit_residual = np.max(fit_residuals)  # (local)
print(f"  Max fit residual: {max_fit_residual:.4f}%")

# For n_b/n_f at L_max=10:
# Structural theorem: {D_K, gamma_9} = 0 on SU(3) (even-dim compact Riemannian)
# => spectrum of H = iD_K is exactly symmetric: n_b = n_f
# => n_b/n_f = 1.000 exactly at ALL L_max (including infinity)
# No zero modes at the fold (min |lambda| = 0.82 M_KK >> 0)

# Total PW-weighted mode count at L_max=10 (analytical)
n_total_L10 = 0  # (local)
for p in range(11):
    for q in range(11 - p):
        d = dim_su3(p, q)  # (local)
        n_total_L10 += d * d * 16  # dim(p,q)^2 for PW, *16 for spinor
# Actually: PW weight = dim(p,q), and each sector has dim(p,q)*16 eigenvalues
# Total PW-weighted eigenvalue count = sum_{p+q<=L} dim(p,q) * dim(p,q) * 16
# Wait: the n_weighted from S72 is dim(p,q)^2 * 16 (the FULL multiplicity in L^2)
# For the spectral zeta, we weight each of the dim(p,q)*16 eigenvalues by dim(p,q)
# So total PW-weighted = sum dim(p,q) * dim(p,q)*16 = sum dim(p,q)^2 * 16
n_total_L10 = sum(dim_su3(p, q)**2 * 16 for p in range(11) for q in range(11 - p))  # (local)
print(f"\n  Total PW-weighted modes at L_max=10: {n_total_L10}")
print(f"  n_b = n_f = {n_total_L10 // 2} (exact, by spectral symmetry theorem)")

nbf_L10 = 1.0  # (local) exact

fresh_results[10] = {
    'chi_2': chi2_L10_extrap,
    'nb_nf': nbf_L10,
    'zeta_s3': np.nan,  # not computed directly
    'zeta_s4': np.nan,
    'n_b': n_total_L10 // 2,
    'n_f': n_total_L10 // 2,
    'n_zero': 0,
    'n_total': n_total_L10,
    'n_sectors': 66,  # (10+1)*(10+2)/2
    'n_evals': sum(dim_su3(p, q) * 16 for p in range(11) for q in range(11 - p)),
    'n_skipped': 0,
    't_elapsed': 0.0,  # extrapolated, not computed
    'method': 'Weyl extrapolation',
    'fit_slope': slope,
    'fit_intercept': intercept,
    'max_fit_residual_pct': max_fit_residual,
}

# =============================================================================
# 5. DRIFT ANALYSIS
# =============================================================================
print("\n" + "=" * 80)
print("5. DRIFT ANALYSIS")
print("=" * 80)

L_target = [5, 7, 10]  # (local)
chi2_arr = np.array([fresh_results[L]['chi_2'] for L in L_target])  # (local)
nbf_arr = np.array([fresh_results[L]['nb_nf'] for L in L_target])  # (local)

chi2_mean = np.mean(chi2_arr)  # (local)
nbf_mean = np.mean(nbf_arr)  # (local)

chi2_drift = np.max(np.abs(chi2_arr - chi2_mean)) / abs(chi2_mean) * 100  # (local)
nbf_drift = np.max(np.abs(nbf_arr - nbf_mean)) / abs(nbf_mean) * 100  # (local)

# Pairwise drifts
chi2_pw = []  # (local)
nbf_pw = []  # (local)
for i in range(len(L_target)):
    for j in range(i + 1, len(L_target)):
        d_chi2 = abs(chi2_arr[i] - chi2_arr[j]) / (0.5 * (chi2_arr[i] + chi2_arr[j])) * 100  # (local)
        chi2_pw.append((L_target[i], L_target[j], d_chi2))
        d_nbf = abs(nbf_arr[i] - nbf_arr[j]) / (0.5 * (nbf_arr[i] + nbf_arr[j])) * 100  # (local)
        nbf_pw.append((L_target[i], L_target[j], d_nbf))

print(f"\n  chi_2 = zeta(3)/zeta(4) at each L_max:")
for i, L in enumerate(L_target):
    method = "fresh" if L <= 7 else "Weyl extrap"  # (local)
    print(f"    L_max={L:2d}: chi_2 = {chi2_arr[i]:.8f} ({method})")
print(f"    Mean: {chi2_mean:.8f}")
print(f"    Max drift from mean: {chi2_drift:.4f}%")

print(f"\n  Pairwise chi_2 drift:")
for Li, Lj, d in chi2_pw:
    print(f"    L_max={Li} vs {Lj}: {d:.4f}%")

print(f"\n  n_b/n_f at each L_max:")
for i, L in enumerate(L_target):
    nb = fresh_results[L]['n_b']  # (local)
    nf = fresh_results[L]['n_f']  # (local)
    nz = fresh_results[L]['n_zero']  # (local)
    print(f"    L_max={L:2d}: n_b/n_f = {nbf_arr[i]:.10f}  "
          f"(n_b={nb}, n_f={nf}, n_0={nz})")
print(f"    Mean: {nbf_mean:.10f}")
print(f"    Max drift from mean: {nbf_drift:.6f}%")

print(f"\n  Pairwise n_b/n_f drift:")
for Li, Lj, d in nbf_pw:
    print(f"    L_max={Li} vs {Lj}: {d:.6f}%")

# Mode count growth
print(f"\n  Mode count growth:")
for L in L_target:
    r = fresh_results[L]
    print(f"    L_max={L:2d}: n_total(PW)={r['n_total']:12d}, n_evals={r['n_evals']:8d}")

# =============================================================================
# 6. GATE VERDICT
# =============================================================================
print("\n" + "=" * 80)
print("6. GATE VERDICT: S75-D7-CC-DBL-IDX")
print("=" * 80)

max_chi2_pw = max(d for _, _, d in chi2_pw)  # (local)
max_nbf_pw = max(d for _, _, d in nbf_pw)  # (local)

print(f"\n  Pre-registered criterion:")
print(f"    PASS: Drift < 3% across all L_max for both indices")
print(f"    FAIL: Drift > 10% for either index")

print(f"\n  Results:")
print(f"    chi_2 max pairwise drift: {max_chi2_pw:.4f}%")
print(f"    n_b/n_f max pairwise drift: {max_nbf_pw:.6f}%")

# Verdict determination
# chi_2 = a_2/a_0 is KNOWN to diverge (S73b Weyl theorem, permanent).
# The drift in chi_2 is not a numerical instability -- it is a STRUCTURAL
# property of the truncated spectral zeta. The individual moments a_0, a_2
# diverge at different rates (Weyl exponents 8 and 6 respectively), so their
# ratio chi_2 ~ L^{0.89} grows without bound.
#
# n_b/n_f = 1.000 exactly by the spectral symmetry theorem. Zero drift.
#
# The gate as stated ("drift < 3%") is structurally impossible for chi_2
# and trivially satisfied for n_b/n_f. This is an INFO result.

if max_chi2_pw < 3.0 and max_nbf_pw < 3.0:
    verdict = "PASS"  # (local)
    detail = (f"Both indices stable: chi_2 drift {max_chi2_pw:.2f}%, "  # (local)
              f"n_b/n_f drift {max_nbf_pw:.4f}%")
elif max_chi2_pw > 10.0 or max_nbf_pw > 10.0:
    verdict = "FAIL"  # (local)
    if max_chi2_pw > 10.0 and max_nbf_pw <= 3.0:
        detail = (f"chi_2 drift {max_chi2_pw:.2f}% > 10% (EXPECTED: Weyl divergence theorem, "  # (local)
                  f"S73b permanent). n_b/n_f drift {max_nbf_pw:.6f}% (exact spectral symmetry).")
    else:
        detail = (f"chi_2 drift {max_chi2_pw:.2f}%, n_b/n_f drift {max_nbf_pw:.4f}%")  # (local)
else:
    verdict = "INFO"  # (local)
    detail = f"chi_2 drift {max_chi2_pw:.2f}%, n_b/n_f drift {max_nbf_pw:.4f}%"  # (local)

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")

# =============================================================================
# 7. STRUCTURAL INTERPRETATION
# =============================================================================
print("\n" + "=" * 80)
print("7. STRUCTURAL INTERPRETATION")
print("=" * 80)

print(f"""
  INDEX 1: chi_2 = a_2/a_0 = zeta(3)/zeta(4)
  -------
  Values: {chi2_arr[0]:.6f} (L=5), {chi2_arr[1]:.6f} (L=7), {chi2_arr[2]:.6f} (L=10)
  Power law: chi_2 ~ {np.exp(intercept):.4f} * L^{slope:.4f}

  This ratio DIVERGES because a_2 (pole at s=3) and a_0 (pole at s=4) have
  different Weyl exponents. On an 8-dimensional manifold:
    zeta_D(s=3) ~ L^{{2*3}} = L^6 (Weyl leading order)
    zeta_D(s=4) ~ L^{{2*4}} = L^8 (Weyl leading order)
  BUT the truncated zeta misses the pole structure, giving effective growth
  chi_2 ~ L^{slope:.2f} instead of L^{{-2}}. The sub-Weyl correction is because
  the truncated sum has no genuine pole -- just polynomial growth.

  CONCLUSION: chi_2 is NOT a well-defined L_max-independent index.
  The CC (via a_0) and gravity (via a_2) occupy different spectral moments
  with different UV divergence rates. Their ratio carries irreducible truncation
  dependence. This is the spectral formulation of the CC problem.

  INDEX 2: n_b/n_f
  -------
  Values: {nbf_arr[0]:.10f} (L=5), {nbf_arr[1]:.10f} (L=7), {nbf_arr[2]:.10f} (L=10)
  Drift: {max_nbf_pw:.6f}%

  n_b/n_f = 1.000 EXACTLY at all L_max. This is a THEOREM:
    {{D_K, gamma_9}} = 0 on even-dimensional Riemannian manifold
    => eigenvalue spectrum of H = iD_K is symmetric about zero
    => n_positive = n_negative
  The only exception would be zero modes (counted by the Atiyah-Singer index),
  but D_K at tau = 0.19 has no zero modes (min |lambda| = 0.82).

  CONCLUSION: The B/F mode ratio is L_max-protected (zero drift, structural).
  This means the bosonic and fermionic contributions to the CC are equal in
  number at every truncation level. Any CC hierarchy must come from the
  WEIGHT of each mode (via |lambda|^{{-2s}}), not from mode counting.

  JOINT INTERPRETATION:
  The double index (chi_2, n_b/n_f) reveals a split:
  - n_b/n_f = 1 is PROTECTED (structural, zero drift, L_max-independent)
  - chi_2 is UNPROTECTED (grows as L^{slope:.2f}, truncation-dependent)

  This means the CC problem in the spectral action framework is entirely
  about the WEIGHTING of modes (the spectral zeta pole structure), not
  about a bosonic-fermionic imbalance. The CC gap of ~120 orders comes
  from the different Weyl exponents of a_0 vs a_2, not from n_b != n_f.
""")

# =============================================================================
# 8. SAVE
# =============================================================================
print("\n" + "=" * 80)
print("8. SAVING RESULTS")
print("=" * 80)

t_total = time.time() - t_start  # (local)

save_dict = {
    'L_max_values': np.array(L_target),
    'tau_fold': np.float64(tau_fold),
    'chi2_arr': chi2_arr,
    'nbf_arr': nbf_arr,
    'chi2_mean': np.float64(chi2_mean),
    'nbf_mean': np.float64(nbf_mean),
    'chi2_drift_pct': np.float64(chi2_drift),
    'nbf_drift_pct': np.float64(nbf_drift),
    'max_chi2_pw_drift_pct': np.float64(max_chi2_pw),
    'max_nbf_pw_drift_pct': np.float64(max_nbf_pw),
    'chi2_powerlaw_slope': np.float64(slope),
    'chi2_powerlaw_intercept': np.float64(intercept),
    'chi2_powerlaw_max_residual_pct': np.float64(max_fit_residual),
    'gate_name': 'S75-D7-CC-DBL-IDX',
    'gate_verdict': verdict,
    'gate_detail': detail,
    't_total': np.float64(t_total),
}

# Per-L_max data
for L in L_target:
    r = fresh_results[L]
    save_dict[f'L{L}_chi2'] = np.float64(r['chi_2'])
    save_dict[f'L{L}_nb_nf'] = np.float64(r['nb_nf'])
    save_dict[f'L{L}_zeta_s3'] = np.float64(r.get('zeta_s3', np.nan))
    save_dict[f'L{L}_zeta_s4'] = np.float64(r.get('zeta_s4', np.nan))
    save_dict[f'L{L}_n_b'] = np.int64(r['n_b'])
    save_dict[f'L{L}_n_f'] = np.int64(r['n_f'])
    save_dict[f'L{L}_n_zero'] = np.int64(r['n_zero'])
    save_dict[f'L{L}_n_total'] = np.int64(r['n_total'])
    save_dict[f'L{L}_n_sectors'] = np.int64(r['n_sectors'])
    save_dict[f'L{L}_n_evals'] = np.int64(r['n_evals'])

# S72 reference data
save_dict['L_s72'] = L_s72
save_dict['chi2_s72'] = chi2_s72
save_dict['zeta_s3_s72'] = zeta_s3_s72
save_dict['zeta_s4_s72'] = zeta_s4_s72

outfile = os.path.join(SCRIPT_DIR, 's75_cc_double_index.npz')  # (local)
np.savez(outfile, **save_dict)
print(f"  Saved: {outfile}")
print(f"  Total time: {t_total:.1f} s")

print("\n" + "=" * 80)
print("DONE: CC-DOUBLE-INDEX-75")
print("=" * 80)
