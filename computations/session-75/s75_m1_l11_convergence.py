#!/usr/bin/env python3
"""
S75-D6-M1-L11: M_1 sqrt-moment CC convergence at L_max = 10 and 11
====================================================================

Extends the S74 W2-Q Scheme B CC computation to L_max = 10 and 11.

Strategy:
  1. Load existing L=9 spectrum cache (52 sectors, p+q <= 9).
  2. Compute new sectors at L=10 and L=11 ONLY for safe irrep chains
     (p > q, q <= 3), which avoid the slow conjugation path in tier1.
  3. Use proven (p,q) <-> (q,p) spectral symmetry (verified to 1e-14
     on all 24 cache pairs) to fill mirror sectors.
  4. Compute M_1 and <|lambda|> with partial coverage at L=10 and L=11.
  5. Cross-check with Pade extrapolation from the L=3..9 data.
  6. Report drift for gate S75-D6-M1-L11.

Pre-registered gate: S75-D6-M1-L11
    PASS if drift(<|lambda|>) from L_max = 10 to 11 is < 15%
    FAIL if drift > 30%

Agent: connes-ncg-theorist | Session: 75 (Task #49)
"""

from __future__ import annotations

import os
import sys
import time
import gc
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from canonical_constants import (
    PI, M_KK, M_Pl_reduced, H_0_GeV, rho_Lambda_obs, tau_fold,
)

import dirac_spectrum as tds

# =============================================================================
# 0. HEADER
# =============================================================================

GATE_ID = "S75-D6-M1-L11"  # (local)
print("=" * 78)
print(f"  {GATE_ID}  --  M_1 sqrt-moment CC convergence to L_max = 11")
print("=" * 78)

PASS_THRESHOLD = 0.15  # (local)
FAIL_THRESHOLD = 0.30  # (local)
EVAL_CUTOFF = 0.01     # (local)

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)

# =============================================================================
# 1. LOAD EXISTING DATA
# =============================================================================

print("\n[1] Loading existing spectrum cache and S74 HP4 data")

# Load L=9 cache
cache = np.load('s74_spectrum_cache_L9_tau019.npz', allow_pickle=True)
sector_evals = {}
for pq, data in cache['sector_evals'].item().items():
    sector_evals[tuple(pq)] = {
        'dim': int(data['dim']),
        'level': int(data['level']),
        'abs_evals': np.asarray(data['abs_evals']),
        'n_pos': int(data['n_pos']),
        'n_zero': int(data['n_zero']),
        'omega_min': float(data['omega_min']),
        'omega_max': float(data['omega_max']),
    }
cache.close()
print(f"    Loaded {len(sector_evals)} cached sectors")

# Load S74 HP4 sweep data (L=3..9)
hp4 = np.load('s74_hp4_pairing.npz', allow_pickle=True)
L_list_s74 = np.array([3, 4, 5, 6, 7, 8, 9])  # (local)
chi_2_s74 = np.array(hp4['chi_2_arr'])           # (local)
M1_s74 = np.array(hp4['M1_arr'])                 # (local)
N_s74 = np.array(hp4['n_arr'])                   # (local)
lam_max_s74 = np.array(hp4['lam_max_arr'])       # (local)
lam_avg_s74 = M1_s74 / N_s74                     # (local)

print(f"    S74 HP4 sweep (L=3..9):")
for i, L in enumerate(L_list_s74):
    print(f"      L={L}: <|lam|>={lam_avg_s74[i]:.6f}  chi_2={chi_2_s74[i]:.6f}  "
          f"M_1={M1_s74[i]:.4e}  N={N_s74[i]:>12.0f}")

# =============================================================================
# 2. BUILD GEOMETRIC INFRASTRUCTURE
# =============================================================================

print("\n[2] Building geometric infrastructure at tau_fold = %.4f" % tau_fold)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma_conn = tds.connection_coefficients(ft)
gammas = tds.build_cliff8()
Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

cliff_err = tds.validate_clifford(gammas)
print(f"    Clifford error: {cliff_err:.2e}")

# =============================================================================
# 3. BUILD SAFE IRREP CACHE (p > q strictly, q <= 3)
# =============================================================================
#
# The dirac_spectrum.py irrep builder has a performance cliff:
# get_irrep(p, p) triggers get_irrep(p-1, p) which uses the slow
# _build_irrep_no_cache conjugation path. Any sector (p, q) with q >= 4
# and p > q eventually chains through a (k, k) diagonal sector.
#
# SAFE sectors are those whose full parent chain NEVER hits a diagonal:
#   (p, 0): symmetric powers (no Casimir projection needed)
#   (p, 1): chain to (1,1) = adjoint (special case, no conjugation)
#   (p, 2): chain to (2,2) = (1,1)x(1,1) (special case, fast)
#   (p, 3): chain to (3,3) -> (2,3) -> _build_irrep_no_cache(3,2,conj)
#            -> (2,2,conj) special case. Total: 2 Casimir projections. Fast.
#
# Sectors with q >= 4 chain through (4,4) -> (3,4) -> slow conjugation.
# We skip these and report partial coverage.

print("\n[3] Building safe irrep cache (q <= 3, p > q)")

tds._irrep_cache.clear()

# Build all (p,0) up to L=11
for p_s in range(12):
    try:
        tds.get_irrep(p_s, 0, gens, f_abc)
    except Exception:
        pass

# Build (1,1) = adjoint
tds.get_irrep(1, 1, gens, f_abc)

# Build (p,1) for p=2..10
for p_s in range(2, 11):
    try:
        tds.get_irrep(p_s, 1, gens, f_abc)
    except Exception as e:
        print(f"    ({p_s},1): FAILED: {e}", flush=True)

# Build (p,2) for p=3..9 (needs (2,2) which is special case)
tds.get_irrep(2, 2, gens, f_abc)  # special case
for p_s in range(3, 10):
    try:
        tds.get_irrep(p_s, 2, gens, f_abc)
    except Exception as e:
        print(f"    ({p_s},2): FAILED: {e}", flush=True)

# Build (p,3) for p=4..8 (needs (3,3) -> built via conjugation of (3,2), fast)
for p_s in range(4, 9):
    try:
        t0 = time.time()
        tds.get_irrep(p_s, 3, gens, f_abc)
        dt = time.time() - t0
        if dt > 1.0:
            print(f"    ({p_s},3): dim={dim_su3(p_s,3)}, t={dt:.1f}s", flush=True)
    except Exception as e:
        print(f"    ({p_s},3): FAILED: {e}", flush=True)

print(f"    Cache size: {len(tds._irrep_cache)} irreps", flush=True)

# =============================================================================
# 4. COMPUTE NEW DIRAC SECTORS
# =============================================================================

print("\n[4] Computing new Dirac sectors at L=10 and L=11")

n_new = 0  # (local)
n_copied = 0  # (local)
n_skipped = 0  # (local)
skip_reasons = []  # (local)
t_start = time.time()  # (local)

# Compute new sectors from cached irreps
for L in range(12):
    for p in range(L + 1):
        q = L - p
        if (p, q) in sector_evals:
            continue  # already have it
        if p < q:
            continue  # handle via mirror in pass 2

        dim_pq = dim_su3(p, q)  # (local)
        D_size = dim_pq * 16  # (local)
        key = tds._cache_key(p, q)  # (local)

        if key not in tds._irrep_cache:
            skip_reasons.append((p, q, L, dim_pq, "no_irrep"))
            n_skipped += 1
            continue

        t0 = time.time()  # (local)
        try:
            rho = tds._irrep_cache[key]
            D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
            H = 1j * D_pi  # (local)
            H = 0.5 * (H + H.conj().T)  # (local)
            evals = np.linalg.eigvalsh(H)  # (local)
            t1 = time.time()  # (local)

            abs_evals = np.abs(evals)  # (local)
            nonzero = abs_evals > 1e-12  # (local)
            pos_abs = abs_evals[nonzero]  # (local)

            omega_min = float(np.min(pos_abs)) if len(pos_abs) > 0 else np.inf  # (local)
            omega_max = float(np.max(pos_abs)) if len(pos_abs) > 0 else 0.0  # (local)
            n_zero = int(np.sum(~nonzero))  # (local)

            sector_evals[(p, q)] = {
                'dim': dim_pq,
                'level': L,
                'abs_evals': pos_abs,
                'n_pos': len(pos_abs),
                'n_zero': n_zero,
                'omega_min': omega_min,
                'omega_max': omega_max,
            }
            n_new += 1
            print(f"    ({p},{q}) L={L}: dim={dim_pq:4d}, D={D_size:5d}x{D_size}, "
                  f"|lam|=[{omega_min:.4f},{omega_max:.4f}], t={t1-t0:.1f}s", flush=True)
            del D_pi, H, evals, abs_evals
            gc.collect()

        except Exception as e:
            skip_reasons.append((p, q, L, dim_pq, str(e)))
            n_skipped += 1
            gc.collect()

# Free irrep cache
tds._irrep_cache.clear()
gc.collect()

# Pass 2: Mirror (q > p) sectors via spectral symmetry
for L in range(12):
    for p in range(L + 1):
        q = L - p
        if (p, q) in sector_evals:
            continue
        if q > p and (q, p) in sector_evals:
            mirror = sector_evals[(q, p)]
            sector_evals[(p, q)] = {
                'dim': mirror['dim'],
                'level': L,
                'abs_evals': mirror['abs_evals'].copy(),
                'n_pos': mirror['n_pos'],
                'n_zero': mirror['n_zero'],
                'omega_min': mirror['omega_min'],
                'omega_max': mirror['omega_max'],
            }
            n_copied += 1

t_total = time.time() - t_start  # (local)
print(f"\n    Computed: {n_new}, Copied: {n_copied}, Skipped: {n_skipped}")
print(f"    Time: {t_total:.1f}s")

# Report coverage
for L in range(12):
    expected = L + 1  # (local)
    have = sum(1 for p in range(L+1) if (p, L-p) in sector_evals)  # (local)
    missing = [(p, L-p) for p in range(L+1) if (p, L-p) not in sector_evals]  # (local)
    if missing:
        print(f"    L={L:2d}: {have}/{expected} sectors. Missing: {missing}")

# =============================================================================
# 5. COMPUTE M_1, <|lambda|>, chi_2 AT EACH L_max
# =============================================================================

print("\n[5] Computing M_1, <|lambda|>, chi_2 at each L_max")

L_range = list(range(3, 12))  # (local) L=3..11

def compute_m1(L_cap):
    """Compute M_1, N, <|lam|>, chi_2, lam_max at L_cap."""
    M1 = 0.0  # (local)
    N = 0  # (local)
    lm = 0.0  # (local) lambda_max
    ns = 0  # (local) sector count
    for (p, q), v in sector_evals.items():
        if p + q > L_cap:
            continue
        d = v['dim']  # (local)
        omega = v['abs_evals']
        pos = omega[omega > EVAL_CUTOFF]
        if pos.size == 0:
            continue
        M1 += d**2 * float(np.sum(pos))
        N += d**2 * pos.size
        ns += 1
        lm = max(lm, float(np.max(pos)))
    la = M1 / N if N > 0 else 0.0  # (local) <|lambda|>
    c2 = M1 / (N * lm) if N > 0 and lm > 0 else 0.0  # (local) chi_2
    return {'M1': M1, 'N': N, 'lam_avg': la, 'chi_2': c2, 'lam_max': lm, 'n_sec': ns}

results = {}  # (local)
for L in L_range:
    r = compute_m1(L)
    results[L] = r
    print(f"    L={L:2d}: <|lam|>={r['lam_avg']:.6f}  chi_2={r['chi_2']:.6f}  "
          f"M_1={r['M1']:.4e}  N={r['N']:>14.0f}  lam_max={r['lam_max']:.4f}  "
          f"sec={r['n_sec']}")

# Cross-check L=9 against S74 data
la_9 = results[9]['lam_avg']  # (local)
la_9_s74 = float(lam_avg_s74[-1])  # (local)
cc_dev = abs(la_9 - la_9_s74) / la_9_s74  # (local)
print(f"\n    L=9 cross-check: <|lam|> = {la_9:.6f} vs S74 = {la_9_s74:.6f}, "
      f"rel dev = {cc_dev:.2e}")

# =============================================================================
# 6. DRIFT ANALYSIS
# =============================================================================

print("\n[6] Drift analysis")

la = {L: results[L]['lam_avg'] for L in L_range}  # (local)
c2 = {L: results[L]['chi_2'] for L in L_range}  # (local)

drift_9_10 = abs(la[10] - la[9]) / la[9] if la[9] > 0 else np.inf  # (local)
drift_10_11 = abs(la[11] - la[10]) / la[10] if la[10] > 0 else np.inf  # (local)
drift_9_11 = abs(la[11] - la[9]) / la[9] if la[9] > 0 else np.inf  # (local)

drift_c2_10_11 = abs(c2[11] - c2[10]) / c2[10] if c2[10] > 0 else np.inf  # (local)

print(f"    <|lambda|> drift:")
print(f"      L=9  -> L=10: {drift_9_10*100:.2f}%")
print(f"      L=10 -> L=11: {drift_10_11*100:.2f}% <-- GATE RELEVANT")
print(f"      L=9  -> L=11: {drift_9_11*100:.2f}%")
print(f"    chi_2 drift L=10 -> L=11: {drift_c2_10_11*100:.2f}%")

# Incremental drift sequence
print(f"\n    Incremental <|lam|> drift (L -> L+1):")
for i in range(len(L_range)-1):
    L1, L2 = L_range[i], L_range[i+1]
    dr = abs(la[L2] - la[L1]) / la[L1]  # (local)
    print(f"      L={L1}->{L2}: {dr*100:.2f}%")

# =============================================================================
# 7. PADE EXTRAPOLATION CROSS-CHECK
# =============================================================================

print("\n[7] Pade extrapolation from L=3..9 data (independent cross-check)")

# Fit <|lambda|>(L) = a + b*L + c/L^2 (rational asymptotic form)
def rational_model(L, a, b, c):
    return a + b * L + c / L**2  # (local)

# Fit <|lambda|>(L) = a + b/L^alpha (power-law approach to asymptote)
def power_model(L, a, b, alpha):
    return a + b / L**alpha  # (local)

Ls = L_list_s74.astype(float)  # (local)
ys = lam_avg_s74  # (local)

# Rational fit
try:
    popt_r, _ = curve_fit(rational_model, Ls, ys, p0=[3.0, 0.05, 1.0])
    la_10_rat = rational_model(10.0, *popt_r)  # (local)
    la_11_rat = rational_model(11.0, *popt_r)  # (local)
    drift_rat = abs(la_11_rat - la_10_rat) / la_10_rat  # (local)
    print(f"    Rational (a + b*L + c/L^2):")
    print(f"      a={popt_r[0]:.4f}, b={popt_r[1]:.4f}, c={popt_r[2]:.4f}")
    print(f"      Extrapolated <|lam|>(10) = {la_10_rat:.6f}")
    print(f"      Extrapolated <|lam|>(11) = {la_11_rat:.6f}")
    print(f"      Predicted drift L=10->11 = {drift_rat*100:.2f}%")
except Exception as e:
    la_10_rat = np.nan  # (local)
    la_11_rat = np.nan  # (local)
    drift_rat = np.nan  # (local)
    print(f"    Rational fit failed: {e}")

# Power-law fit
try:
    popt_p, _ = curve_fit(power_model, Ls, ys, p0=[3.5, -1.0, 1.0],
                          bounds=([0, -np.inf, 0.1], [10, np.inf, 5]))
    la_10_pow = power_model(10.0, *popt_p)  # (local)
    la_11_pow = power_model(11.0, *popt_p)  # (local)
    drift_pow = abs(la_11_pow - la_10_pow) / la_10_pow  # (local)
    print(f"    Power-law (a + b/L^alpha):")
    print(f"      a={popt_p[0]:.4f}, b={popt_p[1]:.4f}, alpha={popt_p[2]:.4f}")
    print(f"      Extrapolated <|lam|>(10) = {la_10_pow:.6f}")
    print(f"      Extrapolated <|lam|>(11) = {la_11_pow:.6f}")
    print(f"      Predicted drift L=10->11 = {drift_pow*100:.2f}%")
except Exception as e:
    la_10_pow = np.nan  # (local)
    la_11_pow = np.nan  # (local)
    drift_pow = np.nan  # (local)
    print(f"    Power-law fit failed: {e}")

# =============================================================================
# 8. CC VIA SCHEME B AT EACH L
# =============================================================================

print("\n[8] CC via Scheme B (gravity-normalised) at each L_max")

f_0_sqrt = 0.912  # (local) sqrt component of f*
H_sq_MPl_sq = (H_0_GeV ** 2) * (M_Pl_reduced ** 2)  # (local) GeV^4

cc_table = {}  # (local)
for L in L_range:
    r = results[L]
    rho_B = f_0_sqrt * r['lam_avg'] * H_sq_MPl_sq  # (local) GeV^4
    log10_r = float(np.log10(rho_B / rho_Lambda_obs)) if rho_B > 0 else np.inf  # (local)
    cc_table[L] = {'rho_B': rho_B, 'log10_ratio': log10_r}
    print(f"    L={L:2d}: rho_B={rho_B:.4e} GeV^4  log10(rho_B/rho_obs)={log10_r:+.4f}")

# =============================================================================
# 9. GATE VERDICT
# =============================================================================

print("\n[9] Gate verdict -- S75-D6-M1-L11")

if drift_10_11 < PASS_THRESHOLD:
    verdict = "PASS"  # (local)
elif drift_10_11 > FAIL_THRESHOLD:
    verdict = "FAIL"  # (local)
else:
    verdict = "INFO"  # (local)

print(f"    PASS threshold: drift < {PASS_THRESHOLD*100:.0f}%")
print(f"    FAIL threshold: drift > {FAIL_THRESHOLD*100:.0f}%")
print(f"    Measured drift (L=10 -> L=11): {drift_10_11*100:.2f}%")
print(f"    Verdict: {verdict}")

# =============================================================================
# 10. SAVE NPZ
# =============================================================================

out_npz = os.path.join(SCRIPT_DIR, 's75_m1_l11_convergence.npz')
np.savez(
    out_npz,
    gate_id=GATE_ID,
    gate_verdict=verdict,
    L_list=np.array(L_range),
    lam_avg_arr=np.array([results[L]['lam_avg'] for L in L_range]),
    chi_2_arr=np.array([results[L]['chi_2'] for L in L_range]),
    M1_arr=np.array([results[L]['M1'] for L in L_range]),
    N_arr=np.array([results[L]['N'] for L in L_range]),
    lam_max_arr=np.array([results[L]['lam_max'] for L in L_range]),
    lam_avg_L9=la[9],
    lam_avg_L10=la[10],
    lam_avg_L11=la[11],
    chi2_L9=c2[9],
    chi2_L10=c2[10],
    chi2_L11=c2[11],
    drift_9_10=drift_9_10,
    drift_10_11=drift_10_11,
    drift_9_11=drift_9_11,
    drift_chi2_10_11=drift_c2_10_11,
    log10_ratio_L9=cc_table[9]['log10_ratio'],
    log10_ratio_L10=cc_table[10]['log10_ratio'],
    log10_ratio_L11=cc_table[11]['log10_ratio'],
    # Extrapolation cross-check
    la_10_rational=la_10_rat,
    la_11_rational=la_11_rat,
    drift_rational=drift_rat,
    la_10_power=la_10_pow,
    la_11_power=la_11_pow,
    drift_power=drift_pow,
    # Gate
    pass_threshold=PASS_THRESHOLD,
    fail_threshold=FAIL_THRESHOLD,
    n_new_sectors=n_new,
    n_copied_sectors=n_copied,
    n_skipped_sectors=n_skipped,
    total_sectors=len(sector_evals),
    tau_fold=tau_fold,
    rho_Lambda_obs=rho_Lambda_obs,
    f_0_sqrt=f_0_sqrt,
)
print(f"\n[10] Saved: {out_npz}")

# =============================================================================
# 11. PLOT
# =============================================================================

print("\n[11] Building plot")

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

Ls_all = np.array(L_range)
la_arr = np.array([results[L]['lam_avg'] for L in L_range])
c2_arr = np.array([results[L]['chi_2'] for L in L_range])
log10_arr = np.array([cc_table[L]['log10_ratio'] for L in L_range])

# Panel 1: <|lambda|> convergence
ax1 = axes[0]
ax1.plot(Ls_all, la_arr, 'bo-', lw=1.5, ms=6, label='computed')
# Extrapolation
if not np.isnan(la_10_rat):
    ax1.plot([10, 11], [la_10_rat, la_11_rat], 'r^--', ms=8, label='rational extrap')
if not np.isnan(la_10_pow):
    ax1.plot([10, 11], [la_10_pow, la_11_pow], 'gs--', ms=8, label='power-law extrap')
ax1.axvline(9, color='gray', ls='--', alpha=0.5, label='L=9 (S74)')
ax1.set_xlabel(r'$L_{\max}$')
ax1.set_ylabel(r'$\langle|\lambda|\rangle$ (M$_{KK}$)')
ax1.set_title(r'$M_1/a_0$ convergence')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# Panel 2: chi_2 convergence
ax2 = axes[1]
ax2.plot(Ls_all, c2_arr, 'rs-', lw=1.5, ms=6)
ax2.axhline(1.0, color='k', ls=':', alpha=0.3)
ax2.axvline(9, color='gray', ls='--', alpha=0.5)
ax2.set_xlabel(r'$L_{\max}$')
ax2.set_ylabel(r'$\chi_2$')
ax2.set_title(r'Spectral fill factor $\chi_2$')
ax2.grid(True, alpha=0.3)

# Panel 3: CC gap
ax3 = axes[2]
ax3.plot(Ls_all, log10_arr, 'g^-', lw=1.5, ms=6)
ax3.axhline(0, color='k', ls='-', lw=0.8)
ax3.axhspan(-0.5, 0.5, color='green', alpha=0.1, label='within 0.5 OOM')
ax3.axvline(9, color='gray', ls='--', alpha=0.5)
ax3.set_xlabel(r'$L_{\max}$')
ax3.set_ylabel(r'$\log_{10}(\rho_B/\rho_{\rm obs})$')
ax3.set_title('CC gap (Scheme B)')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
out_png = os.path.join(SCRIPT_DIR, 's75_m1_l11_convergence.png')
plt.savefig(out_png, dpi=140, bbox_inches='tight')
plt.close(fig)
print(f"    Saved: {out_png}")

# =============================================================================
# 12. SUMMARY
# =============================================================================

print("\n" + "=" * 78)
print(f"  {GATE_ID}  -- SUMMARY")
print("=" * 78)
print(f"  New sectors: {n_new} computed + {n_copied} copied, {n_skipped} skipped")
print(f"  Total sectors: {len(sector_evals)}")
print()
print(f"  L=9:  <|lam|> = {la[9]:.6f}, chi_2 = {c2[9]:.6f}, "
      f"log10(rho_B/rho_obs) = {cc_table[9]['log10_ratio']:+.4f}")
print(f"  L=10: <|lam|> = {la[10]:.6f}, chi_2 = {c2[10]:.6f}, "
      f"log10(rho_B/rho_obs) = {cc_table[10]['log10_ratio']:+.4f}")
print(f"  L=11: <|lam|> = {la[11]:.6f}, chi_2 = {c2[11]:.6f}, "
      f"log10(rho_B/rho_obs) = {cc_table[11]['log10_ratio']:+.4f}")
print()
print(f"  Drift <|lam|> (L=10 -> L=11): {drift_10_11*100:.2f}%")
print(f"  Drift chi_2   (L=10 -> L=11): {drift_c2_10_11*100:.2f}%")
if not np.isnan(drift_rat):
    print(f"  Rational extrapolation drift: {drift_rat*100:.2f}%")
if not np.isnan(drift_pow):
    print(f"  Power-law extrapolation drift: {drift_pow*100:.2f}%")
print()
print(f"  Gate S75-D6-M1-L11:")
print(f"    Threshold: PASS < {PASS_THRESHOLD*100:.0f}%, FAIL > {FAIL_THRESHOLD*100:.0f}%")
print(f"    Measured:  {drift_10_11*100:.2f}%")
print(f"    Verdict:   {verdict}")
print("=" * 78)
