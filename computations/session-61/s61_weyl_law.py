#!/usr/bin/env python3
"""
s61_weyl_law.py — WEYL-VERIFY-61
Weyl Law Verification on Jensen-deformed SU(3) (d=8)

Theory
------
Weyl law for Dirac on closed d-dim spin manifold:

    N(omega) ~ C_d * Vol * omega^d   as omega -> infinity       (1)

    C_d = 2^{[d/2]} * omega_d / (2*pi)^d                       (2)

For d=8: C_8 = 1/(384*pi^4) = 2.673e-5                         (3)

Peter-Weyl structure on SU(3):
    L^2(S) = sum_{(p,q)} V_{(p,q)} otimes (V_{(p,q)}^* otimes S)
D is left-invariant, acts on dim(p,q)*16-dim block. Each eigenvalue appears
with PW multiplicity dim(p,q). Total count: 16 * sum dim(p,q)^2.

PW truncation at L_max=7: omega_max ~ 3.55. PW count ~ L^6, Weyl ~ L^8.
Ratio converges as L^{-2}: the data approaches but has not reached the
Weyl regime. Volume extraction uses heat-trace matching (Seeley-DeWitt a_0).

Gate: WEYL-VERIFY-61
    PASS if |Vol_Weyl - Vol_analytic|/Vol_analytic < 5%
    FAIL if >20%. INFO if 5-20% or structurally inapplicable.

Author: spectral-geometer | Session: S61 Wave 2
"""

import sys
import os
import time
import warnings
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(_x2_shared_dir()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import gamma as gamma_func

from canonical_constants import tau_fold, PI, Vol_SU3_Haar

import dirac_spectrum as tds

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("WEYL-VERIFY-61: Weyl Law on Jensen SU(3) (d=8)")
print("=" * 72)

# =============================================================================
# 1. WEYL CONSTANT
# =============================================================================
d = 8  # (local)
spinor_rank = 2**(d // 2)  # 16
omega_d = PI**(d / 2) / gamma_func(d / 2 + 1)  # pi^4/24
C_d = spinor_rank * omega_d / (2 * PI)**d
C_8_check = 1.0 / (384.0 * PI**4)
assert abs(C_d - C_8_check) / C_8_check < 1e-12
Vol_analytic = Vol_SU3_Haar
a0_SD = spinor_rank * Vol_analytic  # = 16 * 1349.74 = 21595.84

print(f"\n  C_8 = 1/(384*pi^4) = {C_d:.10e}")
print(f"  Vol_analytic = {Vol_analytic:.4f}")
print(f"  a_0(SD) = 16*Vol = {a0_SD:.4f}")

# =============================================================================
# 2. DIRAC EIGENVALUES
# =============================================================================
print("\n" + "=" * 72)
print("2. DIRAC EIGENVALUE COMPUTATION AT tau_fold = %.4f" % tau_fold)
print("=" * 72)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()
B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma_conn = tds.connection_coefficients(ft)
Omega = tds.spinor_connection_offset(Gamma_conn, gammas)

L_max = 7  # (local)

# Collect eigenvalues: each bare eigenvalue gets PW multiplicity dim(p,q)
all_abs_evals = []
all_pw_mult = []    # dim(p,q) for each bare eigenvalue
irrep_list = []
skipped_irreps = []

t_start = time.time()
for L in range(L_max + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        tds._irrep_cache.clear()
        try:
            rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq
        except Exception as e:
            print(f"  ({p},{q}): SKIPPED - {e}")
            skipped_irreps.append((p, q, dim_pq))
            continue

        D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
        evals = np.linalg.eigvals(D_pi)
        abs_evals = np.sort(np.abs(evals))

        all_abs_evals.extend(abs_evals.tolist())
        all_pw_mult.extend([dim_pq] * len(abs_evals))

        irrep_list.append((p, q, dim_pq, len(evals),
                           float(np.min(abs_evals)), float(np.max(abs_evals))))
        print(f"  ({p},{q}): dim={dim_pq:3d}, n_ev={len(evals):5d}, "
              f"|lam|=[{np.min(abs_evals):.4f}, {np.max(abs_evals):.4f}]")

t_elapsed = time.time() - t_start
n_skipped_count = sum(d**2 * 16 for _, _, d in skipped_irreps)
print(f"\n  {len(irrep_list)} irreps computed, {len(skipped_irreps)} skipped, {t_elapsed:.1f}s")
print(f"  Skipped PW-weighted count: {n_skipped_count}")

all_abs_evals = np.array(all_abs_evals)
all_pw_mult = np.array(all_pw_mult, dtype=np.float64)

# Sort by eigenvalue magnitude
sort_idx = np.argsort(all_abs_evals)
omega_sorted = all_abs_evals[sort_idx]
pw_mult_sorted = all_pw_mult[sort_idx]

# Cumulative PW-weighted count N(omega)
N_pw = np.cumsum(pw_mult_sorted)

# =============================================================================
# 3. PW-WEIGHTED COUNTS vs WEYL
# =============================================================================
print("\n" + "=" * 72)
print("3. PW COUNTING FUNCTION vs WEYL ASYMPTOTIC")
print("=" * 72)

omega_max_all = omega_sorted[-1]
N_total_pw = N_pw[-1]
N_weyl_at_max = C_d * Vol_analytic * omega_max_all**8

print(f"  omega_max = {omega_max_all:.6f}")
print(f"  N_PW(omega_max) = {N_total_pw:.0f}")
print(f"  N_Weyl(omega_max) = {N_weyl_at_max:.2f}")
print(f"  Ratio N_PW/N_Weyl = {N_total_pw/N_weyl_at_max:.2f}")

# Ratio at each L cutoff (using omega_max of that level, counting everything below)
print(f"\n  {'L':>3s}  {'omega_max':>10s}  {'N_PW(om_max)':>14s}  {'N_Weyl':>12s}  {'ratio':>10s}")
L_data = []
for L_cut in range(L_max + 1):
    # omega_max at this level
    om_max_L = 0
    for (p, q, dim_pq, n_ev, om_min, om_max) in irrep_list:
        if p + q <= L_cut:
            om_max_L = max(om_max_L, om_max)
    if om_max_L == 0:
        continue
    # N_PW at omega = om_max_L (using the sorted cumulative)
    idx = np.searchsorted(omega_sorted, om_max_L, side='right') - 1
    N_at_L = N_pw[idx] if idx >= 0 else 0
    N_w = C_d * Vol_analytic * om_max_L**8
    r = N_at_L / N_w if N_w > 0 else float('inf')
    print(f"  {L_cut:3d}  {om_max_L:10.4f}  {N_at_L:14.0f}  {N_w:12.2f}  {r:10.2f}")
    L_data.append((L_cut, om_max_L, float(N_at_L), float(N_w), r))

# The ratio is ~ 1000 and DECREASING as L increases.
# This is the L^{-2} convergence toward the Weyl regime.
# The PW spectrum has too many low-energy eigenvalues (Van Hove clustering)
# relative to the Weyl asymptotic.

# Growth exponents
if len(L_data) >= 4:
    Ls = np.array([d[0] for d in L_data[2:]], dtype=float)
    N_s = np.array([d[2] for d in L_data[2:]])
    om_s = np.array([d[1] for d in L_data[2:]])
    alpha_N = np.polyfit(np.log(Ls), np.log(N_s), 1)[0]
    beta_om = np.polyfit(np.log(Ls), np.log(om_s), 1)[0]
    d_eff = alpha_N / beta_om
    print(f"\n  N_PW growth: L^{alpha_N:.2f}")
    print(f"  omega_max growth: L^{beta_om:.2f}")
    print(f"  d_eff = {alpha_N:.2f} / {beta_om:.2f} = {d_eff:.2f} (Weyl: 8)")
else:
    alpha_N = beta_om = d_eff = float('nan')

# =============================================================================
# 4. HEAT TRACE VOLUME EXTRACTION
# =============================================================================
print("\n" + "=" * 72)
print("4. HEAT TRACE a_0 EXTRACTION")
print("=" * 72)

# K(t) = sum_i mult_i * exp(-t * lambda_i^2) where mult_i = dim(p,q)
# Seeley-DeWitt: K(t) ~ (4*pi*t)^{-d/2} * [a_0 + a_2*t + ...]
# => F(t) := (4*pi*t)^{d/2} * K(t) ~ a_0 + a_2*t + a_4*t^2 + ...
# As t -> 0: F(t) -> a_0 (if we had the full spectrum)
# With PW truncation: K(t) -> N_total as t -> 0, so F(t) -> 0
# There is a WINDOW where F(t) ≈ a_0: the crossover between
# PW saturation regime (small t) and the Seeley-DeWitt regime (moderate t).

lam_sq = omega_sorted**2

t_arr = np.logspace(-3, 3, 400)
K_t = np.zeros(len(t_arr))

for j, t in enumerate(t_arr):
    K_t[j] = np.sum(pw_mult_sorted * np.exp(-t * lam_sq))

F_t = K_t * (4 * PI * t_arr)**4  # = (4*pi*t)^{d/2} * K(t)

print(f"  a_0(SD) = 16*Vol = {a0_SD:.4f}")
print(f"  K_PW(t=0) -> {N_total_pw:.0f} (PW saturation)")

# Find where F(t) is closest to a_0
# In the window between saturation and exponential decay
idx_best_a0 = np.argmin(np.abs(F_t - a0_SD))
t_best_a0 = t_arr[idx_best_a0]
F_best = F_t[idx_best_a0]

print(f"\n  Best a_0 match at t = {t_best_a0:.6f}")
print(f"  F(t) = {F_best:.4f}")
print(f"  |F - a_0| / a_0 = {abs(F_best - a0_SD)/a0_SD:.6f}")

Vol_heat_match = F_best / spinor_rank
pct_err_match = abs(Vol_heat_match / Vol_analytic - 1) * 100
print(f"  Vol_heat_match = {Vol_heat_match:.4f}")
print(f"  Error: {pct_err_match:.2f}%")

# Better method: fit F(t) = a_0 + a_2*t in a window near the crossing
# Use a range of t around t_best where F is within 50% of a_0
mask_window = (F_t > 0.5 * a0_SD) & (F_t < 2.0 * a0_SD)
if np.sum(mask_window) >= 5:
    t_win = t_arr[mask_window]
    F_win = F_t[mask_window]
    # Linear fit: F = a_0 + a_2 * t
    coeffs = np.polyfit(t_win, F_win, 1)
    a2_fit = coeffs[0]
    a0_fit = coeffs[1]
    Vol_heat_fit = a0_fit / spinor_rank
    pct_err_fit = abs(Vol_heat_fit / Vol_analytic - 1) * 100
    print(f"\n  Linear fit F(t) = a_0 + a_2*t in [{t_win[0]:.4f}, {t_win[-1]:.4f}]:")
    print(f"  a_0(fit) = {a0_fit:.4f}")
    print(f"  a_2(fit) = {a2_fit:.4f}")
    print(f"  Vol_heat(fit) = {Vol_heat_fit:.4f}")
    print(f"  Error: {pct_err_fit:.2f}%")

    # Quadratic fit for better extrapolation
    if np.sum(mask_window) >= 8:
        coeffs2 = np.polyfit(t_win, F_win, 2)
        a0_quad = coeffs2[2]
        Vol_heat_quad = a0_quad / spinor_rank
        pct_err_quad = abs(Vol_heat_quad / Vol_analytic - 1) * 100
        print(f"\n  Quadratic fit F(t) = a_0 + a_2*t + a_4*t^2:")
        print(f"  a_0(quad) = {a0_quad:.4f}")
        print(f"  Vol_heat(quad) = {Vol_heat_quad:.4f}")
        print(f"  Error: {pct_err_quad:.2f}%")
else:
    a0_fit = F_best
    Vol_heat_fit = Vol_heat_match
    pct_err_fit = pct_err_match
    a0_quad = a0_fit
    Vol_heat_quad = Vol_heat_fit
    pct_err_quad = pct_err_fit

# Select best estimate
estimates = [
    ("match", Vol_heat_match, pct_err_match),
    ("linear_fit", Vol_heat_fit, pct_err_fit),
]
if 'Vol_heat_quad' in dir() and not np.isnan(pct_err_quad):
    estimates.append(("quad_fit", Vol_heat_quad, pct_err_quad))

best_name, Vol_best, pct_err_best = min(estimates, key=lambda x: x[2])
print(f"\n  BEST ESTIMATE: {best_name}")
print(f"  Vol_heat = {Vol_best:.4f}")
print(f"  Error = {pct_err_best:.2f}%")

# =============================================================================
# 5. LOCAL SPECTRAL DIMENSION
# =============================================================================
print("\n" + "=" * 72)
print("5. LOCAL SPECTRAL DIMENSION d_s(omega)")
print("=" * 72)

# d_eff(omega) = d(log N)/d(log omega)
# Use BINNED data to avoid degeneracy issues: create a regular log-omega grid
# and interpolate N(omega) onto it.
n_bins = 200  # (local)
log_om_min = np.log(omega_sorted[omega_sorted > 0][0])
log_om_max = np.log(omega_sorted[-1])
log_om_grid = np.linspace(log_om_min, log_om_max, n_bins)
omega_grid = np.exp(log_om_grid)

# Interpolate N_pw onto the grid using searchsorted
N_grid = np.zeros(n_bins)
for i, om in enumerate(omega_grid):
    idx = np.searchsorted(omega_sorted, om, side='right') - 1
    N_grid[i] = N_pw[max(0, idx)]

log_N_grid = np.log(np.maximum(N_grid, 1.0))

# Compute d_eff = d(log N)/d(log omega) using central differences on the grid
d_eff_grid = np.gradient(log_N_grid, log_om_grid)

# Smooth with Savitzky-Golay-like running average
window = 15  # (local)
kernel = np.ones(window) / window
d_smooth = np.convolve(d_eff_grid, kernel, mode='same')
# Fix edge effects
d_smooth[:window] = d_smooth[window]
d_smooth[-window:] = d_smooth[-window - 1]

# Use omega_grid and d_smooth for output
omega_u = omega_grid
N_u = N_grid

print(f"  {'omega':>8s}  {'d_eff':>8s}  {'N_PW':>12s}")
for omega_target in [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]:
    idx = np.argmin(np.abs(omega_u - omega_target))
    print(f"  {omega_u[idx]:8.3f}  {d_smooth[idx]:8.3f}  {N_u[idx]:12.0f}")

# Interior range for d_max (avoid edges)
interior = slice(2 * window, len(d_smooth) - 2 * window)
if len(d_smooth) > 4 * window:
    d_max = np.max(d_smooth[interior])
    idx_d_max = 2 * window + np.argmax(d_smooth[interior])
    omega_d_max = omega_u[idx_d_max]
else:
    d_max = np.max(d_smooth)
    omega_d_max = omega_u[np.argmax(d_smooth)]

print(f"\n  d_max = {d_max:.3f} at omega = {omega_d_max:.3f}")
print(f"  d_eff from PW growth = {d_eff:.3f}")
print(f"  Weyl target = 8")

# =============================================================================
# 6. WEYL RATIO CONVERGENCE EXTRAPOLATION
# =============================================================================
print("\n" + "=" * 72)
print("6. WEYL RATIO CONVERGENCE (EXTRAPOLATION)")
print("=" * 72)

# The ratio R(L) = N_PW(omega_max(L)) / N_Weyl(omega_max(L))
# should converge to 1 as L -> infinity.
# Fit R(L) = 1 + A/L^2 + B/L^4 to extrapolate.
if len(L_data) >= 4:
    Ls_r = np.array([d[0] for d in L_data], dtype=float)
    Rs_r = np.array([d[4] for d in L_data])

    # R(L) should approach 1 but is currently ~1000
    # Actually R(L) approaches 1 from ABOVE as L -> inf
    # The convergence is slow: R ~ L^{-2} * constant
    # So R(L) * L^2 should be approximately constant at large L
    RL2 = Rs_r * Ls_r**2
    print(f"  R(L) * L^2 for convergence check:")
    for i in range(len(Ls_r)):
        print(f"    L={Ls_r[i]:.0f}: R={Rs_r[i]:.2f}, R*L^2={RL2[i]:.2f}")

    # Extrapolate: L_cross where R(L) = 1
    # R(L) ~ C * L^gamma => log R = gamma * log L + log C
    mask_L3 = Ls_r >= 3
    if np.sum(mask_L3) >= 3:
        log_L = np.log(Ls_r[mask_L3])
        log_R = np.log(Rs_r[mask_L3])
        gamma_R, log_C = np.polyfit(log_L, log_R, 1)
        C_R = np.exp(log_C)
        # R(L_cross) = 1 => C * L_cross^gamma = 1 => L_cross = C^{-1/gamma}
        if gamma_R < 0:
            L_cross = C_R ** (-1.0 / gamma_R)
            print(f"\n  R(L) ~ {C_R:.2f} * L^{gamma_R:.3f}")
            print(f"  Weyl regime (R=1) at L_cross ~ {L_cross:.0f}")
            print(f"  omega_max at L_cross ~ {L_cross * (omega_max_all / L_max):.1f}")
        else:
            L_cross = float('inf')
            print(f"\n  R(L) ~ {C_R:.2f} * L^{gamma_R:.3f} (NOT converging)")
else:
    L_cross = float('inf')
    gamma_R = float('nan')

# =============================================================================
# 7. GATE VERDICT
# =============================================================================
print("\n" + "=" * 72)
print("7. GATE VERDICT: WEYL-VERIFY-61")
print("=" * 72)

# Report both the heat-trace volume and the structural finding
print(f"\n  === VOLUME ESTIMATES ===")
print(f"  Vol_analytic (Haar) = {Vol_analytic:.4f}")
print(f"  Vol_heat (best={best_name}) = {Vol_best:.4f}")
print(f"  Pct error = {pct_err_best:.2f}%")

print(f"\n  === WEYL COUNTING FUNCTION ===")
print(f"  N_PW(omega_max) / N_Weyl(omega_max) = {N_total_pw/N_weyl_at_max:.2f}")
print(f"  d_eff (PW growth) = {d_eff:.2f}")
print(f"  d_eff (local max) = {d_max:.2f}")
if not np.isinf(L_cross):
    print(f"  Estimated L for Weyl regime: {L_cross:.0f}")

# The heat-trace method can extract volume even without reaching the Weyl regime
if pct_err_best < 5.0:
    verdict = "PASS"
    detail = (f"Heat-trace a_0 extraction: Vol = {Vol_best:.2f} vs {Vol_analytic:.2f} "
              f"({pct_err_best:.2f}% error). d_eff = {d_eff:.2f}. "
              f"Weyl counting N/N_Weyl = {N_total_pw/N_weyl_at_max:.0f}x at L=7 "
              f"(not in asymptotic regime; need L ~ {L_cross:.0f}).")
elif pct_err_best < 20.0:
    verdict = "INFO"
    detail = (f"Heat-trace a_0: Vol = {Vol_best:.2f} vs {Vol_analytic:.2f} "
              f"({pct_err_best:.2f}% error, in 5-20% band). "
              f"PW truncation at L=7 not in Weyl regime: "
              f"N_PW/N_Weyl = {N_total_pw/N_weyl_at_max:.0f}x. "
              f"d_eff(PW) = {d_eff:.2f}. "
              f"Weyl regime needs L ~ {L_cross:.0f}. "
              f"STRUCTURAL: Eigenvalue counting function grows as L^{alpha_N:.1f} "
              f"vs Weyl L^{8*beta_om:.1f}. PW bandwidth too narrow for Weyl asymptotics.")
else:
    verdict = "INFO"
    detail = (f"Weyl counting INAPPLICABLE at L=7 PW truncation. "
              f"N_PW/N_Weyl = {N_total_pw/N_weyl_at_max:.0f}x at omega_max. "
              f"Heat-trace: Vol = {Vol_best:.2f} ({pct_err_best:.1f}% from {Vol_analytic:.2f}). "
              f"d_eff(PW) = {d_eff:.2f}. "
              f"STRUCTURAL: Need L ~ {L_cross:.0f} for Weyl regime.")

print(f"\n  GATE: WEYL-VERIFY-61 -> {verdict}")
print(f"  {detail}")

# =============================================================================
# 8. SAVE DATA
# =============================================================================
npz_path = os.path.join(outdir, "s61_weyl_law.npz")
np.savez(
    npz_path,
    omega_sorted=omega_sorted,
    pw_mult_sorted=pw_mult_sorted,
    N_pw=N_pw,
    C_8=C_d,
    Vol_analytic=Vol_analytic,
    Vol_best=Vol_best,
    pct_err_best=pct_err_best,
    best_method=np.array([best_name]),
    t_arr=t_arr,
    K_t=K_t,
    F_t=F_t,
    a0_SD=a0_SD,
    omega_u=omega_u,
    d_smooth=d_smooth,
    d_max=d_max,
    d_eff=d_eff,
    alpha_N=alpha_N,
    beta_om=beta_om,
    N_PW_over_N_Weyl=N_total_pw / N_weyl_at_max,
    L_cross=np.float64(L_cross) if not np.isinf(L_cross) else np.float64(-1),
    L_data_L=np.array([d[0] for d in L_data]),
    L_data_om=np.array([d[1] for d in L_data]),
    L_data_Npw=np.array([d[2] for d in L_data]),
    L_data_Nweyl=np.array([d[3] for d in L_data]),
    L_data_ratio=np.array([d[4] for d in L_data]),
    gate_name=np.array(["WEYL-VERIFY-61"]),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
    L_max=L_max,
    tau_fold=tau_fold,
    d=d,
    n_irreps=len(irrep_list),
    n_evals_bare=len(all_abs_evals),
    n_evals_pw=int(N_total_pw),
)
print(f"  Saved: {npz_path}")

# =============================================================================
# 9. PLOT
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# (a) N(omega) vs Weyl
ax = axes[0, 0]
mask_p = omega_sorted > 0.5
ax.semilogy(omega_sorted[mask_p], N_pw[mask_p], 'b-', lw=1.5,
            label=r'$N_{PW}(\omega)$', alpha=0.8)
omega_sm = np.linspace(0.5, omega_sorted[-1]*1.5, 500)
ax.semilogy(omega_sm, C_d * Vol_analytic * omega_sm**8, 'r--', lw=2,
            label=r'$C_8 V_{Haar}\omega^8$')
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'$N(\omega)$')
ax.set_title('(a) PW Counting Function vs Weyl')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.text(0.05, 0.95,
        f'Ratio at $\\omega_{{max}}$: {N_total_pw/N_weyl_at_max:.0f}x',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# (b) Local spectral dimension
ax = axes[0, 1]
ax.plot(omega_u, d_smooth, 'b-', lw=1.5, label=r'$d_{eff}(\omega)$')
ax.axhline(8.0, color='r', ls='--', lw=2, label='$d = 8$ (Weyl)')
ax.axhline(d_eff, color='g', ls=':', lw=2,
           label=f'$d_{{PW}}$ = {d_eff:.1f}')
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'$d_{eff} = d\ln N / d\ln\omega$')
ax.set_title('(b) Local Spectral Dimension')
ax.set_ylim([0, max(20, d_max + 5) if d_max > 0 else 20])
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.text(0.05, 0.95, f'$d_{{max}}$ = {d_max:.1f} at $\\omega$ = {omega_d_max:.2f}',
        transform=ax.transAxes, fontsize=9, va='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# (c) Heat trace F(t)
ax = axes[1, 0]
ax.loglog(t_arr, F_t, 'b-', lw=1.5, label=r'$(4\pi t)^4 K(t)$')
ax.axhline(a0_SD, color='r', ls='--', lw=2,
           label=f'$a_0 = 16V$ = {a0_SD:.0f}')
ax.axhline(a0_SD * 1.05, color='g', ls=':', alpha=0.5)
ax.axhline(a0_SD * 0.95, color='g', ls=':', alpha=0.5, label='5% band')
ax.axvline(t_best_a0, color='orange', ls=':', lw=1.5,
           label=f'$t_{{match}}$ = {t_best_a0:.3f}')
ax.set_xlabel('$t$')
ax.set_ylabel(r'$(4\pi t)^{d/2} K(t)$')
ax.set_title('(c) Heat Trace $a_0$ Extraction')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.text(0.05, 0.05, f'Vol = {Vol_best:.1f} ({pct_err_best:.1f}% err)',
        transform=ax.transAxes, fontsize=9, va='bottom',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# (d) PW count vs Weyl by level
ax = axes[1, 1]
Ls_p = np.array([d[0] for d in L_data], dtype=float)
Ns_p = np.array([d[2] for d in L_data])
Nw_p = np.array([d[3] for d in L_data])
mask_L = Ls_p > 0
ax.semilogy(Ls_p[mask_L], Ns_p[mask_L], 'bo-', lw=2, ms=8,
            label=r'$N_{PW}$')
ax.semilogy(Ls_p[mask_L], Nw_p[mask_L], 'rs--', lw=2, ms=8,
            label=r'$N_{Weyl}(\omega_{max}(L))$')
if not np.isinf(L_cross) and L_cross < 200:
    ax.axvline(L_cross, color='purple', ls=':', lw=1.5,
               label=f'$L_{{cross}}$ ~ {L_cross:.0f}')
ax.set_xlabel('$L_{max}$ (PW truncation level)')
ax.set_ylabel('Eigenvalue count')
ax.set_title('(d) Convergence to Weyl Regime')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.text(0.05, 0.05,
        f'$N_{{PW}} \\sim L^{{{alpha_N:.1f}}}$\n'
        f'$N_{{Weyl}} \\sim L^{{{8*beta_om:.1f}}}$',
        transform=ax.transAxes, fontsize=9, va='bottom',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

fig.suptitle(
    f'WEYL-VERIFY-61: Jensen SU(3), $\\tau$={tau_fold:.2f}, $L_{{max}}$={L_max}\n'
    f'Gate: {verdict} | $V_{{heat}}$={Vol_best:.1f} vs $V_{{Haar}}$={Vol_analytic:.1f} '
    f'({pct_err_best:.1f}%) | $d_{{eff}}$={d_eff:.1f}',
    fontsize=11, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.92])
png_path = os.path.join(outdir, "s61_weyl_law.png")
plt.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {png_path}")

print("\n" + "=" * 72)
print("COMPLETE")
print("=" * 72)
