"""
S79 P2-B k-scan with FIXED eta_end (= W1-E eta_end=1.23) — consistency replica.

The variable eta_end_for_k(k) in s79_w1e_k_scan.py introduces a phase-dependent
extraction at different post-fold times, which yields 2-3 OOM oscillation in S_IC.
This script uses the W1-E fixed eta_end=1.23 for ALL k and reports
S_IC-envelope (phase-averaged) behavior.

Target: measure MONOTONIC |α|², |β|² envelopes as k varies, decoupled from
phase-dependent |α+β|² oscillation.
"""
from __future__ import annotations

import os
import sys
import time
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import M_KK, dt_transit, tau_fold  # noqa: E402

# -----------------------------------------------------------------------------
w1e_data = np.load('s78_pre_fold_vacuum.npz', allow_pickle=True)
eta_plot = w1e_data['eta_plot']  # (local)
zppoz_plot = w1e_data['zppoz_plot']  # (local)
k_pivot_fold = float(w1e_data['k_pivot_fold'])  # (local)
eta_ic_W1E = float(w1e_data['eta_ic'])  # (local)
eta_end_W1E = float(w1e_data['eta_end'])  # (local)
H_dS = float(w1e_data['H_dS'])  # (local)
S_IC_pivot_W1E = float(w1e_data['S_IC_spectral_stationarity'])  # (local)
alpha_SS_W1E = complex(w1e_data['alpha_SS'])  # (local)
beta_SS_W1E = complex(w1e_data['beta_SS'])  # (local)

zppoz_interp = interp1d(eta_plot, zppoz_plot, kind='cubic',
                        bounds_error=False, fill_value=(zppoz_plot[0], zppoz_plot[-1]))


def zppoz_full(eta):
    out = zppoz_interp(eta)
    if out.ndim == 0:
        out = float(out)
    return out


def solve_mode(k_com, eta_start, eta_end, v0, dv0,
               rtol=1e-11, atol=1e-13, n_eval=4000):
    y0 = [v0.real, v0.imag, dv0.real, dv0.imag]  # (local)

    def rhs(eta, y):
        vr, vi, dvr, dvi = y
        zpp = float(zppoz_full(np.array([eta]))[0])
        omega2 = k_com**2 - zpp  # (local)
        return [dvr, dvi, -omega2 * vr, -omega2 * vi]

    d_eta = eta_end - eta_start  # (local)
    max_step = d_eta / 5000.0  # (local)
    sol = solve_ivp(rhs, [eta_start, eta_end], y0, method='DOP853',
                    rtol=rtol, atol=atol, dense_output=True, max_step=max_step)
    if not sol.success:
        return {'status': 'FAILED'}
    eta_eval = np.linspace(eta_start, eta_end, n_eval)  # (local)
    y_eval = sol.sol(eta_eval)
    v = y_eval[0] + 1j * y_eval[1]  # (local)
    dv = y_eval[2] + 1j * y_eval[3]  # (local)
    return {'status': 'OK', 'v': v, 'dv': dv, 'eta_eval': eta_eval}


def ic_SS(k, eta_ic):
    zpp = float(zppoz_full(np.array([eta_ic]))[0])
    omega2 = k**2 - zpp  # (local)
    omega = np.sqrt(omega2)  # (local)
    v0 = 1.0 / np.sqrt(2.0 * omega)  # (local)
    dv0 = -1j * omega * v0  # (local)
    return complex(v0), complex(dv0)


def bog(k, v_end, dv_end, eta_end):
    zpp_end = float(zppoz_full(np.array([eta_end]))[0])
    omega2_end = k**2 - zpp_end  # (local)
    if omega2_end <= 0:
        return {'status': 'TACHYONIC_END'}
    omega_end = np.sqrt(omega2_end)  # (local)
    factor = np.sqrt(omega_end / 2.0)  # (local)
    alpha = factor * (v_end + 1j * dv_end / omega_end)  # (local)
    beta = factor * (v_end - 1j * dv_end / omega_end)  # (local)
    uni = abs(alpha)**2 - abs(beta)**2  # (local)
    S_IC = abs(alpha + beta)**2  # (local)
    return {'status': 'OK', 'alpha': complex(alpha), 'beta': complex(beta),
            'S_IC': S_IC, 'unitarity': uni, 'omega_end': omega_end}


# -----------------------------------------------------------------------------
# k grid and FIXED eta_end = eta_end_W1E
# -----------------------------------------------------------------------------
n_k = 21  # (local)
k_ratios = np.logspace(-1.0, 1.0, n_k)  # (local)
# Force k_pivot at exact unity
# Replace nearest to unity with unity
idx_close = np.argmin(np.abs(k_ratios - 1.0))
k_ratios[idx_close] = 1.0
k_grid = k_pivot_fold * k_ratios  # (local)

print(f"=== FIXED eta_end k-scan ({n_k} values) ===")
print(f"eta_end (fixed, W1-E) = {eta_end_W1E:.4f}")
print()

# For small k, eta_end = 1.23 may place mode SUPER-horizon (tachyonic end).
# Check and skip/adjust as needed.

results = []
for i, k in enumerate(k_grid):
    eta_ic = eta_ic_W1E  # (local)
    eta_end = eta_end_W1E  # (local) FIXED

    # Check if k is subhorizon at eta_end
    zpp_end = float(zppoz_full(np.array([eta_end]))[0])
    omega2_end = k**2 - zpp_end  # (local)
    if omega2_end <= 0:
        print(f"  [{i+1:2d}/{n_k}] k/k_pivot={k/k_pivot_fold:.3f}: ω²_end = {omega2_end:.2e} < 0 → superhorizon at fixed eta_end. Trying k/aH=3 fallback.")
        # Use k/aH=3 fallback
        eta_end = 1.0 / H_dS - H_dS / (3.0 * k)
        zpp_end2 = float(zppoz_full(np.array([eta_end]))[0])
        if k**2 - zpp_end2 <= 0:
            print(f"       still superhorizon. SKIP.")
            continue

    v0, dv0 = ic_SS(k, eta_ic)
    sol = solve_mode(k, eta_ic, eta_end, v0, dv0)
    if sol['status'] != 'OK':
        print(f"  [{i+1:2d}/{n_k}] SOLVER FAIL")
        continue
    b = bog(k, sol['v'][-1], sol['dv'][-1], eta_end)
    if b['status'] != 'OK':
        print(f"  [{i+1:2d}/{n_k}] TACHYONIC END")
        continue

    ratio = k / k_pivot_fold  # (local)
    print(f"  [{i+1:2d}/{n_k}] k/k_pivot={ratio:7.3f}  |α|²={abs(b['alpha'])**2:.3e}  "
          f"|β|²={abs(b['beta'])**2:.3e}  S_IC={b['S_IC']:.3e}  uni={b['unitarity']:+.4f}  eta_end={eta_end:.3f}")
    results.append({
        'k': k, 'k_ratio': ratio, 'eta_end_used': eta_end,
        'alpha_re': b['alpha'].real, 'alpha_im': b['alpha'].imag,
        'beta_re': b['beta'].real, 'beta_im': b['beta'].imag,
        'alpha_sq': abs(b['alpha'])**2, 'beta_sq': abs(b['beta'])**2,
        'S_IC': b['S_IC'], 'unitarity': b['unitarity'],
    })

# -----------------------------------------------------------------------------
# Summaries
# -----------------------------------------------------------------------------
k_arr = np.array([r['k'] for r in results])
S_IC_arr = np.array([r['S_IC'] for r in results])
beta_sq_arr = np.array([r['beta_sq'] for r in results])
alpha_sq_arr = np.array([r['alpha_sq'] for r in results])

# Consistency
idx_pivot = np.argmin(np.abs(k_arr - k_pivot_fold))
S_IC_pivot_scan = S_IC_arr[idx_pivot]  # (local)
print(f"\nCONSISTENCY CHECK:")
print(f"  W1-E S_IC(k_pivot)  = {S_IC_pivot_W1E:.6e}")
print(f"  Scan S_IC(k_pivot)  = {S_IC_pivot_scan:.6e}")
print(f"  Ratio               = {S_IC_pivot_scan/S_IC_pivot_W1E:.6f} (target: 1.000 ± 0.01)")

# Compute |α| and |β| envelopes via log-log fit over clean regimes
def slope_ll(k, s):
    k = np.array(k); s = np.array(s)
    mask = s > 0
    if mask.sum() < 2:
        return np.nan
    return np.polyfit(np.log(k[mask]), np.log(s[mask]), 1)[0]

mask_IR = k_arr < k_pivot_fold
mask_UV = k_arr > k_pivot_fold

slope_beta_UV = slope_ll(k_arr[mask_UV], beta_sq_arr[mask_UV])  # (local)
slope_alpha_UV = slope_ll(k_arr[mask_UV], alpha_sq_arr[mask_UV])  # (local)
slope_SIC_UV = slope_ll(k_arr[mask_UV], S_IC_arr[mask_UV])  # (local)
slope_beta_IR = slope_ll(k_arr[mask_IR], beta_sq_arr[mask_IR])  # (local)
slope_SIC_IR = slope_ll(k_arr[mask_IR], S_IC_arr[mask_IR])  # (local)

print(f"\nENVELOPE SLOPES (log-log):")
print(f"  UV (k > k_pivot):")
print(f"    |β|² slope   = {slope_beta_UV:+.3f}")
print(f"    |α|² slope   = {slope_alpha_UV:+.3f}")
print(f"    S_IC slope   = {slope_SIC_UV:+.3f}")
print(f"  IR (k < k_pivot):")
print(f"    |β|² slope   = {slope_beta_IR:+.3f}")
print(f"    S_IC slope   = {slope_SIC_IR:+.3f}")
print(f"  W3-E extrapolated slope (CHK6 factor-3 baseline) = +1.509")

# Peak locations
idx_beta_max = np.argmax(beta_sq_arr)
idx_SIC_max = np.argmax(S_IC_arr)
print(f"\nPEAK DIAGNOSTICS:")
print(f"  |β|² peaks at k/k_pivot = {k_arr[idx_beta_max]/k_pivot_fold:.3f}, value = {beta_sq_arr[idx_beta_max]:.3e}")
print(f"  S_IC peaks at k/k_pivot = {k_arr[idx_SIC_max]/k_pivot_fold:.3f}, value = {S_IC_arr[idx_SIC_max]:.3e}")

# Saturation: does S_IC approach 1 at high k?
print(f"\nHIGH-k BEHAVIOR:")
print(f"  S_IC(k/k_pivot = {k_arr[-1]/k_pivot_fold:.2f}) = {S_IC_arr[-1]:.3e}")
print(f"  |β|²(k/k_pivot = {k_arr[-1]/k_pivot_fold:.2f}) = {beta_sq_arr[-1]:.3e}")
# Does |β|² go to 0 (i.e. S_IC → 1)?
frac_sat = (beta_sq_arr[-1] < 1.0)  # (local)
print(f"  |β|² < 1 at max k? {frac_sat}")

# FIRAS-kinematic projection: above |β|² = 1, S_IC still amplifies; cap is at |β|² ~ 1.
# For FIRAS k up to 10^4 Mpc^-1:
# k_pivot_Mpc = k_pivot / (scale conversion); FIRAS k > 8e7 * k_pivot in M_KK units (deep UV)
# So: is |β|² still finite at k = 10 k_pivot? If yes, extrapolate to 10^7.
print(f"\nEXTRAPOLATION TO FIRAS WINDOW:")
# Fit log |β|² vs log k on clean UV (k/k_pivot ≥ 3) regime
mask_deep_UV = k_arr / k_pivot_fold >= 3.0
if mask_deep_UV.sum() >= 2:
    log_beta = np.log(np.maximum(beta_sq_arr[mask_deep_UV], 1e-300))
    log_k = np.log(k_arr[mask_deep_UV])
    slope_deep = np.polyfit(log_k, log_beta, 1)[0]  # (local)
    intercept_deep = np.polyfit(log_k, log_beta, 1)[1]  # (local)
    k_FIRAS_ratio = 1e7  # ridiculous UV; test numerics, not to believe extrapolation
    beta_extrap = np.exp(slope_deep * np.log(k_FIRAS_ratio * k_pivot_fold) + intercept_deep)  # (local)
    print(f"  Deep UV (k/k_pivot >= 3) |β|² slope = {slope_deep:+.3f}")
    # If slope < -2, |β|² decays fast → physical cap at S_IC=1 at some k
    # Crossover: |β|² = 1 at what k/k_pivot?
    k_cross_ratio = np.exp((-intercept_deep) / slope_deep) / k_pivot_fold if slope_deep < 0 else np.inf  # (local)
    print(f"  |β|² = 1 at k/k_pivot ≈ {k_cross_ratio:.2e} (extrapolation; unreliable beyond factor ~10)")

# Save
np.savez(
    's79_w1e_k_scan_fixed_eta.npz',
    k=k_arr, k_ratio=k_arr/k_pivot_fold,
    alpha_re=np.array([r['alpha_re'] for r in results]),
    alpha_im=np.array([r['alpha_im'] for r in results]),
    beta_re=np.array([r['beta_re'] for r in results]),
    beta_im=np.array([r['beta_im'] for r in results]),
    alpha_sq=alpha_sq_arr, beta_sq=beta_sq_arr,
    S_IC=S_IC_arr,
    eta_end_fixed=eta_end_W1E,
    slope_beta_UV=slope_beta_UV, slope_alpha_UV=slope_alpha_UV,
    slope_SIC_UV=slope_SIC_UV, slope_beta_IR=slope_beta_IR, slope_SIC_IR=slope_SIC_IR,
    k_pivot_fold=k_pivot_fold, S_IC_pivot_W1E=S_IC_pivot_W1E,
)
print("\nSaved: s79_w1e_k_scan_fixed_eta.npz")
print("Done.")
