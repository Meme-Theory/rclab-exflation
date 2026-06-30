"""
S79 P2-B: Direct S_IC(k) k-scan on extended grid.

Purpose: answer the T1 question in P2-B workshop. W1-E computed S_IC at k_pivot
only; W3-E extrapolated via log-log slope 1.509 across factor-3 baseline. This
script runs the W1-E mode solver directly at 15 k values spanning
k ∈ [k_pivot/10, 10 × k_pivot] to quantify:

  (a) Whether S_IC(k) saturates at 1 (subhorizon adiabatic cap) for k > k_pivot.
  (b) Whether S_IC(k) continues to rise (in-regime parametric kick).
  (c) How the scheme-invariant ratio S_IC(k_pivot) / S_IC(k_lo) behaves.

This is the ONLY computation that can discriminate Path (b)/(c) (physical cap)
from extrapolation artifacts under the pinned conventions.

Uses the EXACT pre-fold vacuum script's solve_mode, ic_spectral_stationarity,
and bogoliubov_extract — no recomputation of the pump profile.

Convention pins: S_IC = |α+β|²; spectral-stationarity IC; f*, L_max=10.

Runtime estimate: ~30 seconds per k (DOP853, rtol=1e-11, n_eval=4000)
  × 15 k values = ~8 minutes.
"""
from __future__ import annotations

import os
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# Canonical constants import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import M_KK, dt_transit, tau_fold  # noqa: E402

# -----------------------------------------------------------------------------
# Load W1-E infrastructure (pump profile, parameters) rather than re-deriving
# -----------------------------------------------------------------------------
w1e_data = np.load('s78_pre_fold_vacuum.npz', allow_pickle=True)
eta_plot = w1e_data['eta_plot']  # (local)
zppoz_plot = w1e_data['zppoz_plot']  # (local)

k_pivot_fold = float(w1e_data['k_pivot_fold'])  # (local)
eta_ic_W1E = float(w1e_data['eta_ic'])  # (local)
eta_end_W1E = float(w1e_data['eta_end'])  # (local)
eta_match = float(w1e_data['eta_match'])  # (local)
H_dS = float(w1e_data['H_dS'])  # (local)

# Reference W1-E result at k_pivot (for consistency CHK)
S_IC_pivot_W1E = float(w1e_data['S_IC_spectral_stationarity'])  # (local)

# -----------------------------------------------------------------------------
# Reconstruct the pump profile interpolant (zppoz_full)
# -----------------------------------------------------------------------------
zppoz_interp = interp1d(eta_plot, zppoz_plot, kind='cubic',
                        bounds_error=False, fill_value=(zppoz_plot[0], zppoz_plot[-1]))


def zppoz_full(eta):
    """Full pump profile z''/z: pre-fold flat (=0), transit impulse, post-fold dS.

    Reconstructed from the W1-E data arrays for exact consistency.
    """
    out = zppoz_interp(eta)
    if out.ndim == 0:
        out = float(out)
    return out


# -----------------------------------------------------------------------------
# Mode solver (COPY of W1-E solve_mode — no divergence from W1-E semantics)
# -----------------------------------------------------------------------------
def solve_mode(k_com, eta_start, eta_end, v0, dv0,
               rtol=1e-11, atol=1e-13, n_eval=4000):
    """v'' + (k² - z''/z) v = 0 on [eta_start, eta_end] with IC (v0, dv0)."""
    y0 = [v0.real, v0.imag, dv0.real, dv0.imag]  # (local)

    def rhs(eta, y):
        vr, vi, dvr, dvi = y
        zpp = float(zppoz_full(np.array([eta]))[0])
        omega2 = k_com**2 - zpp  # (local)
        return [dvr, dvi, -omega2 * vr, -omega2 * vi]

    d_eta = eta_end - eta_start  # (local)
    max_step = d_eta / 5000.0  # (local)

    sol = solve_ivp(rhs, [eta_start, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)
    if not sol.success:
        return {'status': 'FAILED'}

    eta_eval = np.linspace(eta_start, eta_end, n_eval)  # (local)
    y_eval = sol.sol(eta_eval)
    v = y_eval[0] + 1j * y_eval[1]  # (local)
    dv = y_eval[2] + 1j * y_eval[3]  # (local)

    W = v[0] * np.conj(dv[0]) - np.conj(v[0]) * dv[0]  # (local) initial Wronskian
    Wf = v[-1] * np.conj(dv[-1]) - np.conj(v[-1]) * dv[-1]  # (local) final
    return {'status': 'OK', 'v': v, 'dv': dv, 'eta_eval': eta_eval,
            'W0': complex(W), 'Wf': complex(Wf)}


# -----------------------------------------------------------------------------
# IC: spectral stationarity (W1-E canonical)
# -----------------------------------------------------------------------------
def ic_spectral_stationarity(k, eta_ic):
    """Spectral stationarity IC (W1-E canonical). Pre-fold z''/z = 0, so
    omega² = k² always positive in pre-fold. Standard adiabatic vacuum.
    """
    zpp = float(zppoz_full(np.array([eta_ic]))[0])
    omega2 = k**2 - zpp  # (local)
    if omega2 <= 0:
        kappa = np.sqrt(-omega2)  # (local)
        v0 = 1.0 / np.sqrt(2.0 * kappa)  # (local)
        dv0 = -kappa * v0 + 0.0j  # (local)
        return complex(v0), complex(dv0)
    omega = np.sqrt(omega2)  # (local)
    v0 = 1.0 / np.sqrt(2.0 * omega)  # (local)
    dv0 = -1j * omega * v0  # (local) Wronskian W = -i
    return complex(v0), complex(dv0)


# -----------------------------------------------------------------------------
# Bogoliubov extraction at eta_end (W1-E bogoliubov_extract logic)
# -----------------------------------------------------------------------------
def bogoliubov_extract(k, v_end, dv_end, eta_end):
    """Project (v, dv) at eta_end onto post-fold WKB basis."""
    zpp_end = float(zppoz_full(np.array([eta_end]))[0])
    omega2_end = k**2 - zpp_end  # (local)
    if omega2_end <= 0:
        return {'status': 'TACHYONIC_END', 'omega2': omega2_end}
    omega_end = np.sqrt(omega2_end)  # (local)
    factor = np.sqrt(omega_end / 2.0)  # (local)
    alpha = factor * (v_end + 1j * dv_end / omega_end)  # (local)
    beta = factor * (v_end - 1j * dv_end / omega_end)  # (local)
    uni = abs(alpha)**2 - abs(beta)**2  # (local) should be 1
    S_IC = abs(alpha + beta)**2  # (local) |α+β|² convention pinned
    return {'status': 'OK', 'alpha': complex(alpha), 'beta': complex(beta),
            'S_IC': S_IC, 'unitarity': uni, 'omega_end': omega_end}


# -----------------------------------------------------------------------------
# Build k-grid
# -----------------------------------------------------------------------------
# Strategy: span k/k_pivot ∈ [0.1, 10], logarithmic.
# Include k_pivot exactly as consistency check (must reproduce 1.636e5).
n_k_scan = 15  # (local) # k points
k_ratios = np.logspace(-1.0, 1.0, n_k_scan)  # (local) k/k_pivot
k_ratios = np.sort(np.concatenate([k_ratios, [1.0]]))  # (local) force k_pivot exact
k_grid = k_pivot_fold * k_ratios  # (local) physical k in M_KK

print(f"=== S79 W1-E k-scan ({len(k_grid)} k values) ===")
print(f"k_pivot_fold = {k_pivot_fold:.4f} M_KK")
print(f"k range: [{k_grid.min():.3e}, {k_grid.max():.3e}] M_KK")
print(f"eta_ic  = {eta_ic_W1E:.4e}")
print(f"eta_end = {eta_end_W1E:.4e}")
print()

# For each k we may need a k-dependent eta_end:
#   the post-fold horizon-crossing eta scales as eta_cross ~ 1/(a*H).
#   In conformal dS: eta = -1/(aH), a = 1/(1 - H*eta); N = ln(a) = ln(1/(1-H*eta)).
#   N_k_cross (k/aH=1) = ln(k/H) efolds.
# For k_pivot: N=3.12 (W1-E). Gate pre-registered eta_end is "k/aH=3" (safely subhorizon).
# For k > k_pivot: eta_end at k/aH=3 is LATER, at eta_end ~ (1 - H/k) * 1/H ≈ 1/H - 3/k.
# For k < k_pivot: mode crosses horizon at earlier eta; keeping eta_end_W1E may leave mode
# SUPER-HORIZON (tachyonic-end) and Bogoliubov extraction fails.
# Solution: set eta_end(k) so k/(a*H) = 3 always.
#
# dS ansatz: a = a_fold * exp(H*(eta-eta_fold)*a_fold) under conformal H. Since we use
# post-fold eta (not N), a(eta) ≈ 1/(1 - H*eta) for post-fold dS.
# aH at eta = H / (1 - H*eta). Setting k/(aH)=3: 1 - H*eta_end = H/(3k/H) = H²/(3k).
# => eta_end(k) = (1 - H²/(3k)) / H = 1/H - H/(3k).

def eta_end_for_k(k):
    """eta_end such that k/(aH) = 3 in post-fold dS."""
    return 1.0 / H_dS - H_dS / (3.0 * k)


# -----------------------------------------------------------------------------
# Main k-scan
# -----------------------------------------------------------------------------
results = []
t_start = time.time()

for i, k in enumerate(k_grid):
    t0 = time.time()
    # eta_ic: 10 * dt_transit pre-fold (W1-E convention); scale with k maybe?
    # For k >> k_pivot, the WKB period is shorter; eta_ic_W1E ~ 10*dt_transit remains
    # deeply subhorizon (k * |eta_ic| = 14.3 * 0.01 = 0.14 per transit-scale period,
    # scaled at k/k_pivot = 10 gives 1.4 periods — adequate).
    eta_ic = eta_ic_W1E  # (local) consistent with W1-E
    eta_end = eta_end_for_k(k)  # (local) k-dependent

    # Ensure eta_end > 0 (post-fold) and mode is subhorizon at eta_end
    zpp_end = float(zppoz_full(np.array([eta_end]))[0])
    omega2_end_check = k**2 - zpp_end  # (local)
    if omega2_end_check <= 0:
        # fallback: back off eta_end to safely subhorizon
        # Find largest eta_end with k^2 - z''/z > 0.5 k^2:
        mask = (eta_plot > 0.0) & (zppoz_plot < 0.5 * k**2)
        if mask.any():
            eta_end = eta_plot[mask][-1]  # (local) latest safe eta_end
        else:
            print(f"  k={k:.3e}: NO SAFE eta_end → SKIP")
            continue

    v0, dv0 = ic_spectral_stationarity(k, eta_ic)
    sol = solve_mode(k, eta_ic, eta_end, v0, dv0)
    if sol['status'] != 'OK':
        print(f"  k={k:.3e}: SOLVER FAILED")
        continue

    bog = bogoliubov_extract(k, sol['v'][-1], sol['dv'][-1], eta_end)
    if bog['status'] != 'OK':
        print(f"  k={k:.3e}: TACHYONIC END (ω²={bog.get('omega2')}); skip")
        continue

    S_IC = bog['S_IC']
    beta_sq = abs(bog['beta'])**2  # (local)
    alpha_sq = abs(bog['alpha'])**2  # (local)
    uni = bog['unitarity']
    ratio = k / k_pivot_fold  # (local)

    t1 = time.time()
    print(f"  [{i+1:2d}/{len(k_grid)}] k/k_pivot = {ratio:7.3f}  k² = {k**2:9.2f}  "
          f"|β|² = {beta_sq:.3e}  S_IC = {S_IC:.3e}  uni = {uni:+.4f}  "
          f"eta_end = {eta_end:.3f}  t = {t1-t0:.1f}s")

    results.append({
        'k': k, 'k_ratio': ratio, 'k_sq': k**2,
        'eta_end': eta_end,
        'alpha_re': bog['alpha'].real, 'alpha_im': bog['alpha'].imag,
        'beta_re': bog['beta'].real, 'beta_im': bog['beta'].imag,
        'alpha_sq': alpha_sq, 'beta_sq': beta_sq,
        'S_IC': S_IC, 'unitarity': uni, 'omega_end': bog['omega_end'],
    })

t_total = time.time() - t_start
print(f"\n=== k-scan complete in {t_total:.1f}s ({t_total/60:.1f} min) ===")

# -----------------------------------------------------------------------------
# Post-process: log-log fit of S_IC(k) segments; detect saturation
# -----------------------------------------------------------------------------
k_arr = np.array([r['k'] for r in results])
S_IC_arr = np.array([r['S_IC'] for r in results])
beta_sq_arr = np.array([r['beta_sq'] for r in results])
alpha_sq_arr = np.array([r['alpha_sq'] for r in results])
uni_arr = np.array([r['unitarity'] for r in results])

# Consistency CHK: S_IC at k_pivot matches W1-E
idx_pivot = np.argmin(np.abs(k_arr - k_pivot_fold))
S_IC_at_pivot_scan = S_IC_arr[idx_pivot]  # (local)
consistency_ratio = S_IC_at_pivot_scan / S_IC_pivot_W1E  # (local)
print(f"\nCONSISTENCY CHECK:")
print(f"  W1-E  S_IC(k_pivot) = {S_IC_pivot_W1E:.6e}")
print(f"  Scan S_IC(k_pivot)  = {S_IC_at_pivot_scan:.6e}")
print(f"  Ratio (scan/W1E)    = {consistency_ratio:.6f} (target: 1.000 ± 0.01)")

# Log-log slope IR side (k < k_pivot) and UV side (k > k_pivot)
mask_IR = k_arr < k_pivot_fold
mask_UV = k_arr > k_pivot_fold

def slope_loglog(k, s):
    if len(k) < 2:
        return np.nan
    return np.polyfit(np.log(k), np.log(s), 1)[0]

slope_full = slope_loglog(k_arr, S_IC_arr)  # (local)
slope_IR = slope_loglog(k_arr[mask_IR], S_IC_arr[mask_IR]) if mask_IR.sum() >= 2 else np.nan  # (local)
slope_UV = slope_loglog(k_arr[mask_UV], S_IC_arr[mask_UV]) if mask_UV.sum() >= 2 else np.nan  # (local)

print(f"\nSLOPE DIAGNOSTICS (log-log S_IC vs k):")
print(f"  Full range slope (k ∈ [{k_arr.min():.2e}, {k_arr.max():.2e}]) = {slope_full:.3f}")
print(f"  IR slope (k < k_pivot)                                        = {slope_IR:.3f}")
print(f"  UV slope (k > k_pivot)                                        = {slope_UV:.3f}")
print(f"  W3-E extrapolation slope (CHK6 factor-3 baseline)             = 1.509")

# Saturation check: is S_IC(k_max) >= cap 1? What's the maximum?
print(f"\nSATURATION DIAGNOSTICS:")
print(f"  S_IC(k_max={k_arr[-1]:.2e}) = {S_IC_arr[-1]:.3e}")
print(f"  S_IC(k_pivot)              = {S_IC_arr[idx_pivot]:.3e}")
print(f"  S_IC(k_min={k_arr[0]:.2e}) = {S_IC_arr[0]:.3e}")
print(f"  max(S_IC) / min(S_IC)      = {S_IC_arr.max()/S_IC_arr.min():.3e}")

# Unitarity diagnostic
print(f"\nUNITARITY DIAGNOSTICS:")
print(f"  max |unitarity - 1| = {np.max(np.abs(uni_arr - 1.0)):.3e} (target: < 1e-3)")

# -----------------------------------------------------------------------------
# Save all data
# -----------------------------------------------------------------------------
np.savez(
    's79_w1e_k_scan.npz',
    k=k_arr, k_ratio=k_arr/k_pivot_fold,
    k_sq=np.array([r['k_sq'] for r in results]),
    eta_end=np.array([r['eta_end'] for r in results]),
    alpha_re=np.array([r['alpha_re'] for r in results]),
    alpha_im=np.array([r['alpha_im'] for r in results]),
    beta_re=np.array([r['beta_re'] for r in results]),
    beta_im=np.array([r['beta_im'] for r in results]),
    alpha_sq=alpha_sq_arr, beta_sq=beta_sq_arr,
    S_IC=S_IC_arr, unitarity=uni_arr,
    omega_end=np.array([r['omega_end'] for r in results]),
    slope_full=slope_full, slope_IR=slope_IR, slope_UV=slope_UV,
    slope_W3E_ref=1.509,
    k_pivot_fold=k_pivot_fold,
    consistency_ratio=consistency_ratio,
    S_IC_pivot_W1E=S_IC_pivot_W1E,
    scheme_tag='f*', convention_tag='|alpha+beta|^2', L_max_tag=10,
    IC_principle='spectral_stationarity',
)
print("\nSaved: s79_w1e_k_scan.npz")
print("Done.")
