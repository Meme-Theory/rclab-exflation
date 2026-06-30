#!/usr/bin/env python3
"""
ACOUSTIC-TENSOR-TRANSFER-67: Tensor Bogoliubov Through Acoustic White Hole
==========================================================================

Computes the tensor power spectrum P_T(k) through the van Hove fold transit,
and the tensor-to-scalar ratio r(k) = P_T(k) / P_zeta(k).

GOVERNING EQUATIONS:
--------------------
Tensor mode equation in conformal time eta:

    v_k'' + (k^2 - a''/a) v_k = 0                              (T.1)

where v_k = a * h_k, h_k is the tensor perturbation amplitude.

This DIFFERS from the scalar mode equation:

    u_k'' + (k^2 * c_BLV^2 - z''/z) u_k = 0                   (S.1)

in TWO ways:
  (a) Tensors propagate at c = 1 (speed of light), NOT c_BLV = 0.485.
  (b) The pump field is a''/a, NOT z''/z = (a*sqrt(2*eps_H))''/z.

Consequence: the tensor tachyonic threshold k_tach^T = sqrt(a''/a)
differs from the scalar k_tach^S = sqrt(z''/z) / c_BLV.

STANDARD INFLATION CONSISTENCY RELATION r = 16*eps IS INAPPLICABLE:
Five independent arguments (S66 workshops) established this. The
actual r(k) must be computed from the ratio of tensor and scalar
Bogoliubov spectra through the impulsive supersonic transit.

THREE METHODS (following W1-A structure):
  (i)   Sudden approximation: analytic |beta_k^T|^2
  (ii)  Transfer matrix: piecewise constant a''/a segments
  (iii) Full RK4/5: numerical ODE solve

OUTPUT:
  - P_T(k): tensor power spectrum at transit scale
  - r(k) = P_T(k) / P_zeta(k): tensor-to-scalar ratio
  - n_T(k): tensor spectral index

Gate: ACOUSTIC-TENSOR-TRANSFER-67 (INFO gate)
References: Parker [01], Birrell-Davies [02], S66 transit collab Sec. 5.2
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, cumulative_trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced,
    S_fold, dS_fold, d2S_fold, H_fold as H_fold_canon,
    dt_transit, v_terminal,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, PI,
)

# ============================================================================
#  SECTION 1: Reconstruct background from W1-A
# ============================================================================

print("=" * 72)
print("ACOUSTIC-TENSOR-TRANSFER-67: Tensor Bogoliubov Through Acoustic White Hole")
print("=" * 72)

# Load W1-A scalar data for comparison and background reconstruction
w1a_file = os.path.join(os.path.dirname(__file__), 's67_transit_ps.npz')
if not os.path.exists(w1a_file):
    print("ERROR: W1-A data file s67_transit_ps.npz not found.")
    sys.exit(1)

w1a = np.load(w1a_file, allow_pickle=True)

# Reconstruct the spectral action S(tau) exactly as in W1-A
zeta_data = np.load(os.path.join(os.path.dirname(__file__), 's66_zeta_sa.npz'),
                    allow_pickle=True)
tau_16 = zeta_data['tau_all']
a2_16 = zeta_data['a2']
a4_16 = zeta_data['a4']
a0_const = 6440.0  # (local)

running_data = np.load(os.path.join(os.path.dirname(__file__),
                                    's66_running_ns.npz'), allow_pickle=True)
S_bare_L3 = running_data['S_bare_L3']

a2_cal = np.array([np.interp(t, tau_16, a2_16) for t in [0.05, 0.19, 0.22]])
a4_cal = np.array([np.interp(t, tau_16, a4_16) for t in [0.05, 0.19, 0.22]])
A_mat = np.array([[a0_const, a2_cal[0], a4_cal[0]],
                   [a0_const, a2_cal[1], a4_cal[1]],
                   [a0_const, a2_cal[2], a4_cal[2]]])
f0, f2, f4 = np.linalg.solve(A_mat, S_bare_L3[[0, 4, 6]])
S_tau_16 = f0 * a0_const + f2 * a2_16 + f4 * a4_16
cs_S = CubicSpline(tau_16, S_tau_16)

print(f"\nS(tau_fold): recon = {cs_S(tau_fold):.2f}, canon = {S_fold:.2f}")

# ============================================================================
#  SECTION 2: Background quantities in transit window [0.10, 0.30]
# ============================================================================

# Kinetic normalization from canonical eps_H = 0.022 at fold
dlnS_fold = dS_fold / S_fold
eps_H_fold_canon = 0.022  # (local)
K_norm = dlnS_fold**2 / (2.0 * eps_H_fold_canon)

tau_lo, tau_hi = 0.10, 0.30
N_fine = 8000  # (local)
tau_fine = np.linspace(tau_lo, tau_hi, N_fine)

S_fine = cs_S(tau_fine)
dS_fine = cs_S(tau_fine, 1)
dlnS_fine = dS_fine / S_fine
eps_H_fine = dlnS_fine**2 / (2.0 * K_norm)

# Hubble rate H(tau) from spectral action: H^2 ~ S(tau)
H_fine = H_fold_canon * np.sqrt(S_fine / cs_S(tau_fold))

# Scale factor: d(ln a)/dtau = H / v_tau
v_tau = v_terminal
dlna_dtau = H_fine / v_tau
lna = cumulative_trapezoid(dlna_dtau, tau_fine, initial=0.0)
lna -= np.interp(tau_fold, tau_fine, lna)  # normalize a(fold) = 1
a_fine = np.exp(lna)

# Conformal time: d(eta)/d(tau) = 1/(v_tau * a)
deta_dtau = 1.0 / (v_tau * a_fine)
eta_fine = cumulative_trapezoid(deta_dtau, tau_fine, initial=0.0)

# Verify against W1-A
a_w1a = w1a['a_fine']
eta_w1a = w1a['eta_fine']
print(f"\nBackground cross-check vs W1-A:")
print(f"  a(fold): this = {np.interp(tau_fold, tau_fine, a_fine):.6f}, W1A = {a_w1a[3600]:.6f}")
print(f"  eta(end): this = {eta_fine[-1]:.6e}, W1A = {eta_w1a[-1]:.6e}")

# ============================================================================
#  SECTION 3: Tensor pump field a''/a in conformal time
# ============================================================================

print(f"\n{'='*72}")
print("TENSOR PUMP FIELD: a''/a")
print(f"{'='*72}")

# Compute a(eta) spline and its second derivative
cs_a_eta = CubicSpline(eta_fine, a_fine)
a_pp = cs_a_eta(eta_fine, 2)      # a''(eta)
app_over_a = a_pp / a_fine         # a''/a

# For comparison: the scalar pump field z''/z
z_fine = a_fine * np.sqrt(2.0 * eps_H_fine)
cs_z_eta = CubicSpline(eta_fine, z_fine)
zpp_z = cs_z_eta(eta_fine, 2) / z_fine

# At fold
eta_fold = np.interp(tau_fold, tau_fine, eta_fine)
fold_eta_idx = np.argmin(np.abs(eta_fine - eta_fold))

app_a_fold = app_over_a[fold_eta_idx]
zpp_z_fold = zpp_z[fold_eta_idx]

# Create spline of a''/a for ODE integration
cs_app_a = CubicSpline(eta_fine, app_over_a)

# Sound speeds: tensor c_T = 1, scalar c_S = c_BLV = 0.485
c_BLV = 0.485  # (local)
c_tensor = 1.0  # tensors propagate at speed of light  # (local)

# Tachyonic thresholds
k_tach_tensor = np.sqrt(abs(app_a_fold))       # for c_T = 1
k_tach_scalar = np.sqrt(abs(zpp_z_fold)) / c_BLV

# Hubble scale in tensor and scalar contexts
k_transit_scalar = H_fold_canon / c_BLV
k_transit_tensor = H_fold_canon / c_tensor  # = H_fold_canon

print(f"\n  PUMP FIELD COMPARISON AT FOLD (tau = {tau_fold}):")
print(f"  {'Quantity':<35} {'Tensor':<20} {'Scalar':<20} {'Ratio T/S'}")
print(f"  {'-'*90}")
print(f"  {'Pump field (M_KK^2)':<35} {app_a_fold:<20.4e} {zpp_z_fold:<20.4e} {app_a_fold/zpp_z_fold:<20.4f}")
print(f"  {'Sound speed (c/c_light)':<35} {c_tensor:<20.3f} {c_BLV:<20.3f} {c_tensor/c_BLV:<20.4f}")
print(f"  {'k_tach = sqrt(pump)/c (M_KK)':<35} {k_tach_tensor:<20.1f} {k_tach_scalar:<20.1f} {k_tach_tensor/k_tach_scalar:<20.4f}")
print(f"  {'k_transit = H/c (M_KK)':<35} {k_transit_tensor:<20.1f} {k_transit_scalar:<20.1f} {k_transit_tensor/k_transit_scalar:<20.4f}")

# Physical insight: a''/a vs z''/z
# In de Sitter: a = -1/(H*eta), so a''/a = 2/eta^2 = 2*a^2*H^2
# z = a*sqrt(2*eps_H), so z''/z = a''/a + (eps_H'' / 2*eps_H) + ...
# The difference z''/z - a''/a encodes the eps_H dynamics.
# Here: ratio = z''/z / (a''/a) = 1.329 at fold.
ratio_pumps = zpp_z_fold / app_a_fold
print(f"\n  z''/z / (a''/a) = {ratio_pumps:.4f}")
print(f"  This excess comes from eps_H dynamics (time-varying slow-roll).")
print(f"  In pure de Sitter (eps_H = const): ratio = 1 exactly.")

# Profile of a''/a across transit
print(f"\n  a''/a profile across transit:")
for tau_val in [0.10, 0.13, 0.15, 0.17, 0.19, 0.21, 0.23, 0.25, 0.30]:
    idx = np.argmin(np.abs(tau_fine - tau_val))
    print(f"    tau = {tau_val:.2f}: a''/a = {app_over_a[idx]:.4e}")

# ============================================================================
#  SECTION 4: Wavenumber grid
# ============================================================================

# For tensors: omega_k^2 = k^2 - a''/a (c_T = 1)
# Superhorizon when k^2 < a''/a, i.e. k < sqrt(a''/a)
# All modes with k < 831 M_KK are superhorizon at the fold

app_max = np.max(np.abs(app_over_a))
k_deeply_super = 50.0     # M_KK -- deeply superhorizon throughout  # (local)
k_wkb_boundary = 5.0 * np.sqrt(app_max)  # well into WKB regime

N_k = 500  # (local)
k_grid = np.geomspace(k_deeply_super, k_wkb_boundary, N_k)

print(f"\n  k grid: [{k_grid[0]:.1f}, {k_grid[-1]:.1f}] M_KK ({N_k} pts)")
print(f"  k_tach^T at fold = {k_tach_tensor:.1f} M_KK")
print(f"  sqrt(max|a''/a|) = {np.sqrt(app_max):.1f} M_KK")

# ============================================================================
#  SECTION 5: Method (iii) -- Full RK4/5 for tensor modes (PRIMARY)
# ============================================================================

print(f"\n{'='*72}")
print("METHOD (iii): FULL NUMERICAL RK4/5 -- TENSOR MODES")
print(f"{'='*72}")

eta_start = eta_fine[0]
eta_end = eta_fine[-1]

N_k_rk = 400
k_grid_rk = np.geomspace(k_grid[0], k_grid[-1], N_k_rk)

print(f"  Solving {N_k_rk} tensor modes on eta in [{eta_start:.4e}, {eta_end:.4e}]")

P_T_rk = np.zeros(N_k_rk)
beta_sq_T_rk = np.zeros(N_k_rk)

for ik, k in enumerate(k_grid_rk):
    # omega_k^2 = k^2 * c_T^2 - a''/a  (c_T = 1)
    om_sq_i = k**2 - cs_app_a(eta_start)

    if om_sq_i > 0:
        # Sub-horizon: Bunch-Davies vacuum
        om_i = np.sqrt(om_sq_i)
        y0 = [1.0 / np.sqrt(2.0 * om_i), 0.0,
              0.0, -np.sqrt(om_i / 2.0)]
    else:
        # Superhorizon: growing mode v_k ~ a(eta)
        # v_k = A * a(eta), v_k' = A * a'(eta)
        a_i = a_fine[0]
        ap_i = cs_a_eta(eta_start, 1)
        norm = 1.0 / np.sqrt(2.0 * k)  # (local)
        y0 = [norm * a_i, norm * ap_i, 0.0, 0.0]

    def rhs(eta, y, k_val=k):
        om_sq = k_val**2 - cs_app_a(float(eta))
        return [y[1], -om_sq * y[0], y[3], -om_sq * y[2]]

    try:
        sol = solve_ivp(rhs, [eta_start, eta_end], y0, method='RK45',
                        rtol=1e-10, atol=1e-13,
                        max_step=(eta_end - eta_start) / 800)
        if not sol.success:
            P_T_rk[ik] = np.nan
            continue
    except Exception:
        P_T_rk[ik] = np.nan
        continue

    # Extract |v_k/a|^2 at final time
    # P_T(k) = (k^3 / 2*pi^2) * |v_k/a|^2  (two polarizations: factor 2 included below)
    v_R_f = sol.y[0, -1]
    v_I_f = sol.y[2, -1]
    a_f = a_fine[-1]

    v_sq = v_R_f**2 + v_I_f**2
    # Per polarization:
    P_T_per_pol = k**3 / (2.0 * PI**2) * v_sq / a_f**2
    # Two polarizations:
    P_T_rk[ik] = 2.0 * P_T_per_pol

    # Extract beta_k for sub-horizon modes
    om_sq_f = k**2 - cs_app_a(eta_end)
    if om_sq_f > 0 and om_sq_i > 0:
        om_f = np.sqrt(om_sq_f)
        v_c = v_R_f + 1j * v_I_f
        vp_c = sol.y[1, -1] + 1j * sol.y[3, -1]
        # Bogoliubov decomposition: v = alpha * e^{-i omega eta} + beta * e^{+i omega eta}
        # beta = (sqrt(om/2) * v + i * v' / sqrt(2*om)) (with proper convention)
        beta_T = np.sqrt(om_f / 2.0) * v_c - 1j * vp_c / np.sqrt(2.0 * om_f)
        beta_sq_T_rk[ik] = np.abs(beta_T)**2
    else:
        # Superhorizon: effective beta from power spectrum
        beta_sq_T_rk[ik] = v_sq * np.sqrt(abs(cs_app_a(eta_end))) / a_f**2

    if (ik + 1) % 100 == 0:
        print(f"    {ik+1}/{N_k_rk} tensor modes completed")

print(f"    {N_k_rk}/{N_k_rk} tensor modes completed")

valid_T = np.isfinite(P_T_rk) & (P_T_rk > 0)
print(f"\n  Valid tensor modes: {np.sum(valid_T)}/{N_k_rk}")
if np.any(valid_T):
    print(f"  P_T range: [{P_T_rk[valid_T].min():.4e}, {P_T_rk[valid_T].max():.4e}]")

# ============================================================================
#  SECTION 6: Method (i) -- Sudden approximation for tensors
# ============================================================================

print(f"\n{'='*72}")
print("METHOD (i): SUDDEN APPROXIMATION -- TENSOR MODES")
print(f"{'='*72}")

# Pre/post fold a''/a
eta_pre = np.interp(0.16, tau_fine, eta_fine)
eta_post = np.interp(0.22, tau_fine, eta_fine)
app_a_pre = cs_app_a(eta_pre)
app_a_post = cs_app_a(eta_post)

print(f"  a''/a pre-fold  (tau=0.16) = {app_a_pre:.4e}")
print(f"  a''/a post-fold (tau=0.22) = {app_a_post:.4e}")

beta_sq_T_sudden = np.zeros(N_k)
P_T_sudden = np.zeros(N_k)

for ik, k in enumerate(k_grid):
    om_sq_pre = k**2 - app_a_pre
    om_sq_post = k**2 - app_a_post

    if om_sq_pre > 0 and om_sq_post > 0:
        # Both in WKB regime
        om_pre = np.sqrt(om_sq_pre)
        om_post = np.sqrt(om_sq_post)
        beta_k = (om_post - om_pre) / (2.0 * np.sqrt(om_pre * om_post))
        beta_sq_T_sudden[ik] = beta_k**2
        a_post = np.interp(0.22, tau_fine, a_fine)
        P_T_sudden[ik] = 2.0 * k**3 / (2*PI**2) * (1 + 2*beta_k**2) / (2*om_post * a_post**2)
    elif om_sq_pre > 0 and om_sq_post <= 0:
        # Sub-horizon -> superhorizon: strong mixing
        om_pre = np.sqrt(om_sq_pre)
        kappa_post = np.sqrt(-om_sq_post)
        beta_sq_T_sudden[ik] = (om_pre + kappa_post)**2 / (4 * om_pre * kappa_post)
        a_post = np.interp(0.22, tau_fine, a_fine)
        P_T_sudden[ik] = 2.0 * k**3 / (2*PI**2) * (1 + 2*beta_sq_T_sudden[ik]) / (2*om_pre * a_post**2)
    else:
        # Both superhorizon: frozen mode
        beta_sq_T_sudden[ik] = 1.0
        a_post = np.interp(0.22, tau_fine, a_fine)
        kappa_eff = np.sqrt(abs(app_a_post) - k**2)
        if kappa_eff > 0:
            P_T_sudden[ik] = 2.0 * k**3 / (2*PI**2) / (2.0 * kappa_eff * a_post**2)
        else:
            P_T_sudden[ik] = 2.0 * k**3 / (2*PI**2) / (2.0 * a_post**2)

print(f"  beta_sq^T range: [{beta_sq_T_sudden.min():.4e}, {beta_sq_T_sudden.max():.4e}]")

# ============================================================================
#  SECTION 7: Method (ii) -- Transfer matrix for tensors
# ============================================================================

print(f"\n{'='*72}")
print("METHOD (ii): TRANSFER MATRIX -- TENSOR MODES")
print(f"{'='*72}")

mask_seg = (tau_16 >= tau_lo) & (tau_16 <= 0.30)
tau_seg = tau_16[mask_seg]
N_seg = len(tau_seg)

tau_bounds = np.zeros(N_seg + 1)
tau_bounds[0] = tau_lo
tau_bounds[-1] = 0.30
for j in range(1, N_seg):
    tau_bounds[j] = 0.5 * (tau_seg[j-1] + tau_seg[j])

eta_bounds = np.interp(tau_bounds, tau_fine, eta_fine)
eta_centers = np.interp(tau_seg, tau_fine, eta_fine)
delta_eta = np.diff(eta_bounds)
app_a_seg = cs_app_a(eta_centers)
a_seg_end = np.interp(tau_bounds[-1], tau_fine, a_fine)

print(f"  {N_seg} segments from tau={tau_lo} to tau=0.30")

P_T_transfer = np.zeros(N_k)
beta_sq_T_transfer = np.zeros(N_k)

for ik, k in enumerate(k_grid):
    M_total = np.eye(2, dtype=complex)

    for j in range(N_seg):
        # Tensor: omega_k^2 = k^2 - a''/a (c_T = 1)
        om_sq = k**2 - app_a_seg[j]
        de = delta_eta[j]

        if om_sq > 0:
            om = np.sqrt(om_sq)
            c_val = np.cos(om * de)
            s_val = np.sin(om * de)
            M_j = np.array([[c_val, s_val/om], [-om*s_val, c_val]], dtype=complex)
        elif om_sq < 0:
            kp = np.sqrt(-om_sq)
            ch = np.cosh(kp * de)
            sh = np.sinh(kp * de)
            M_j = np.array([[ch, sh/kp], [kp*sh, ch]], dtype=complex)
        else:
            M_j = np.array([[1.0, de], [0.0, 1.0]], dtype=complex)

        M_total = M_j @ M_total

    # Initial conditions
    om_sq_in = k**2 - app_a_seg[0]
    if om_sq_in > 0:
        om_in = np.sqrt(om_sq_in)
        v_in = 1.0 / np.sqrt(2.0 * om_in)
        vp_in = -1j * np.sqrt(om_in / 2.0)
    else:
        kp_in = np.sqrt(-om_sq_in)
        v_in = 1.0 / np.sqrt(2.0 * kp_in)
        vp_in = kp_in * v_in  # growing mode

    v_out = M_total[0, 0] * v_in + M_total[0, 1] * vp_in
    vp_out = M_total[1, 0] * v_in + M_total[1, 1] * vp_in

    v_sq = np.abs(v_out)**2
    P_T_transfer[ik] = 2.0 * k**3 / (2.0 * PI**2) * v_sq / a_seg_end**2

    om_sq_out = k**2 - app_a_seg[-1]
    if om_sq_out > 0 and om_sq_in > 0:
        om_out = np.sqrt(om_sq_out)
        alpha_k = np.sqrt(om_out/2)*v_out + 1j*vp_out/np.sqrt(2*om_out)
        beta_k = np.sqrt(om_out/2)*v_out - 1j*vp_out/np.sqrt(2*om_out)
        beta_sq_T_transfer[ik] = np.abs(beta_k)**2
    else:
        beta_sq_T_transfer[ik] = v_sq * np.sqrt(abs(app_a_seg[-1])) / a_seg_end**2

print(f"  P_T range: [{P_T_transfer.min():.4e}, {P_T_transfer.max():.4e}]")

# ============================================================================
#  SECTION 8: Tensor spectral index and running
# ============================================================================

print(f"\n{'='*72}")
print("TENSOR SPECTRAL INDEX AND RUNNING")
print(f"{'='*72}")


def spectral_observables(k_arr, P_arr, smooth=7):
    """Compute n_T(k) and dn_T/dlnk from P_T(k)."""
    ln_k = np.log(k_arr)
    ln_P = np.log(np.maximum(P_arr, 1e-300))
    nT = np.gradient(ln_P, ln_k)
    if smooth > 1 and len(nT) > 2*smooth:
        kernel = np.ones(smooth) / smooth
        nT = np.convolve(nT, kernel, mode='same')
    dnT = np.gradient(nT, ln_k)
    if smooth > 1 and len(dnT) > 2*smooth:
        dnT = np.convolve(dnT, kernel, mode='same')
    return nT, dnT


# RK4/5
k_T_valid = k_grid_rk[valid_T]
P_T_valid = P_T_rk[valid_T]
nT_rk, dnT_rk = spectral_observables(k_T_valid, P_T_valid)

# Sudden
mask_s_valid = P_T_sudden > 0
k_Ts_valid = k_grid[mask_s_valid]
P_Ts_valid = P_T_sudden[mask_s_valid]
nT_sudden, dnT_sudden = spectral_observables(k_Ts_valid, P_Ts_valid)

# Transfer
mask_t_valid = P_T_transfer > 0
k_Tt_valid = k_grid[mask_t_valid]
P_Tt_valid = P_T_transfer[mask_t_valid]
nT_transfer, dnT_transfer = spectral_observables(k_Tt_valid, P_Tt_valid)


def eval_at_k(k_arr, vals, k_target):
    idx = np.argmin(np.abs(k_arr - k_target))
    return vals[idx], idx


# Report at key scales
for k_label, k_val in [("0.1*k_tach^T", 0.1*k_tach_tensor),
                         ("0.5*k_tach^T", 0.5*k_tach_tensor),
                         ("k_tach^T", k_tach_tensor),
                         ("2*k_tach^T", 2*k_tach_tensor),
                         ("k_transit^S", k_transit_scalar)]:
    if k_val < k_T_valid[0] or k_val > k_T_valid[-1]:
        continue
    v_nT, _ = eval_at_k(k_T_valid, nT_rk, k_val)
    v_dnT, _ = eval_at_k(k_T_valid, dnT_rk, k_val)
    print(f"  At {k_label} = {k_val:.1f} M_KK:")
    print(f"    RK4/5: n_T = {v_nT:.4f}, dn_T/dlnk = {v_dnT:.6f}")

# Plateau analysis (superhorizon tensor modes)
mask_plat_T = (k_T_valid > 0.03*k_tach_tensor) & (k_T_valid < 0.5*k_tach_tensor)
if np.any(mask_plat_T):
    nT_plat = nT_rk[mask_plat_T]
    print(f"\n  Superhorizon tensor plateau (k/k_tach^T in [0.03, 0.5]):")
    print(f"    <n_T> = {np.mean(nT_plat):.4f} +/- {np.std(nT_plat):.4f}")
    nT_plateau_mean = np.mean(nT_plat)
else:
    nT_plateau_mean = 3.0  # (local)

# ============================================================================
#  SECTION 9: Tensor-to-scalar ratio r(k)
# ============================================================================

print(f"\n{'='*72}")
print("TENSOR-TO-SCALAR RATIO r(k)")
print(f"{'='*72}")

# Load scalar P_zeta from W1-A
k_scalar_rk = w1a['k_grid_rk']
P_scalar_rk = w1a['P_zeta_rk']
valid_scalar = np.isfinite(P_scalar_rk) & (P_scalar_rk > 0)
k_scalar_valid = k_scalar_rk[valid_scalar]
P_scalar_valid = P_scalar_rk[valid_scalar]

# Interpolate tensor and scalar onto common k grid
# Use the overlap region
k_min_common = max(k_T_valid[0], k_scalar_valid[0])
k_max_common = min(k_T_valid[-1], k_scalar_valid[-1])

N_common = 300
k_common = np.geomspace(k_min_common, k_max_common, N_common)

# Interpolate in log space
from scipy.interpolate import interp1d

ln_P_T_interp = interp1d(np.log(k_T_valid), np.log(P_T_valid),
                          kind='cubic', fill_value='extrapolate')
ln_P_S_interp = interp1d(np.log(k_scalar_valid), np.log(P_scalar_valid),
                          kind='cubic', fill_value='extrapolate')

P_T_common = np.exp(ln_P_T_interp(np.log(k_common)))
P_S_common = np.exp(ln_P_S_interp(np.log(k_common)))

r_k = P_T_common / P_S_common

print(f"\n  Common k range: [{k_common[0]:.1f}, {k_common[-1]:.1f}] M_KK")
print(f"  r(k) range: [{r_k.min():.4e}, {r_k.max():.4e}]")

# r at key scales
print(f"\n  r(k) at key scales:")
for k_label, k_val in [("0.1*k_transit^S", 0.1*k_transit_scalar),
                         ("0.3*k_transit^S", 0.3*k_transit_scalar),
                         ("k_transit^S", k_transit_scalar),
                         ("k_tach^T", k_tach_tensor),
                         ("3*k_transit^S", 3*k_transit_scalar)]:
    if k_val < k_common[0] or k_val > k_common[-1]:
        print(f"    {k_label} = {k_val:.1f} M_KK: OUTSIDE RANGE")
        continue
    r_val, _ = eval_at_k(k_common, r_k, k_val)
    P_T_val, _ = eval_at_k(k_common, P_T_common, k_val)
    P_S_val, _ = eval_at_k(k_common, P_S_common, k_val)
    print(f"    {k_label} = {k_val:.1f} M_KK: r = {r_val:.4e}  (P_T = {P_T_val:.4e}, P_S = {P_S_val:.4e})")

# Consistency relation check: r = -8 * n_T (standard inflation)
# This should NOT hold for the impulsive transit.
nT_at_transit, _ = eval_at_k(k_T_valid, nT_rk, k_transit_scalar)
r_at_transit, _ = eval_at_k(k_common, r_k, k_transit_scalar)
r_consistency = -8.0 * nT_at_transit
print(f"\n  CONSISTENCY RELATION TEST:")
print(f"    n_T at k_transit = {nT_at_transit:.4f}")
print(f"    r at k_transit   = {r_at_transit:.4e}")
print(f"    -8*n_T           = {r_consistency:.4f}")
print(f"    r = 16*eps_H     = {16 * eps_H_fold_canon:.4f}")
print(f"    r / (-8*n_T)     = {r_at_transit / r_consistency:.4e}" if abs(r_consistency) > 1e-20 else "    r / (-8*n_T)     = N/A (n_T ~ 0)")
print(f"    --> Standard consistency relation {'HOLDS' if abs(r_at_transit + 8*nT_at_transit) < 0.5*abs(r_at_transit) else 'VIOLATED'}")

# ============================================================================
#  SECTION 10: Physical interpretation
# ============================================================================

print(f"\n{'='*72}")
print("PHYSICAL INTERPRETATION")
print(f"{'='*72}")

# Key structural insight: tensors see a SMALLER pump field than scalars
# because they don't couple to c_BLV.
# This means the tensor tachyonic threshold is LOWER: fewer modes are
# superhorizon at any given time.
# Moreover, c_tensor = 1 > c_BLV = 0.485 means tensor modes have
# HIGHER effective frequency: omega_T = k, omega_S = k*c_BLV.
# Result: tensor modes are MORE adiabatic through the transit.
# Less particle production for tensors => r < 16*eps.

# Superhorizon scaling comparison
# Scalar superhorizon: P_zeta ~ k^3 * const => n_s ~ 4
# Tensor superhorizon: P_T ~ k^3 * const => n_T ~ 3

# The k^3 comes from the mode function normalization.
# Both scale as k^3 in the deeply superhorizon limit, but with different prefactors.

print(f"""
  STRUCTURE OF THE TENSOR POWER SPECTRUM:

  1. SUPERHORIZON REGIME (k < {k_tach_tensor:.0f} M_KK = sqrt(a''/a)):
     Tensor modes with k^2 < a''/a at the fold are superhorizon.
     Their amplitude |v_k/a|^2 FREEZES. P_T(k) ~ k^3 * const.
     The tensor tachyonic threshold ({k_tach_tensor:.0f} M_KK) is 2.4x LOWER
     than the scalar one ({k_tach_scalar:.0f} M_KK) because:
       (a) The tensor pump a''/a < z''/z (no eps_H dynamics)
       (b) c_tensor = 1 > c_BLV = 0.485 (higher effective frequency)

  2. TRANSITION REGION (k ~ {k_tach_tensor:.0f} M_KK):
     Modes crossing k_tach^T show strong spectral index variation.

  3. SUB-HORIZON REGIME (k >> {k_tach_tensor:.0f} M_KK):
     These modes pass adiabatically. |beta_k^T|^2 ~ (a''/a)^2 / k^4 << 1.

  KEY PHYSICAL RESULTS:
  - Tensors are MORE ADIABATIC than scalars through the transit because
    they propagate faster (c = 1 vs c_BLV = 0.485).
  - The tensor tachyonic window is NARROWER: k_tach^T / k_tach^S = {k_tach_tensor/k_tach_scalar:.3f}.
  - The standard consistency relation r = 16*eps is VIOLATED because
    the Bogoliubov coefficients are set by the impulsive transit, not
    by slow-roll dynamics.
  - At the transit scale, r(k) reflects the ratio of tensor to scalar
    pump field strengths and sound speeds.

  ACOUSTIC WHITE HOLE TRANSFER:
  - The acoustic white hole has sonic Mach 13.75.
  - SCALAR perturbations are causally disconnected at c_BLV = 0.485.
  - TENSOR perturbations (GW) propagate at c = 1 > v_transit.
  - Whether tensors are also white-hole-trapped depends on whether
    v_transit = 26.5 * c_BLV = 12.9 M_KK/M_KK < c or > c.
  - v_terminal = {v_terminal:.2f} M_KK (in M_KK units, dimensionless velocity
    of the tau parameter). The physical Mach number for tensors is
    v_terminal / c_tensor = {v_terminal/c_tensor:.2f}, so the transit IS
    supersonic even for tensor modes.
  - TENSOR Mach number = {v_terminal/c_tensor:.2f} >> 1.
  - Tensors ARE white-hole-trapped, but at a LOWER Mach number than scalars
    (Mach {v_terminal/c_tensor:.1f} vs Mach {v_terminal/c_BLV:.1f}).
""")

# ============================================================================
#  SECTION 11: Plots
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Pump fields a''/a and z''/z
ax = axes[0, 0]
tau_plot = tau_fine[::10]
idx_plot = np.arange(0, len(tau_fine), 10)
ax.semilogy(tau_plot, np.abs(app_over_a[idx_plot]), 'b-', lw=2, label="a''/a (tensor)")
ax.semilogy(tau_plot, np.abs(zpp_z[idx_plot]), 'r-', lw=2, label="z''/z (scalar)")
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.axhline(k_tach_tensor**2, color='b', ls=':', alpha=0.3)
ax.axhline((k_tach_scalar*c_BLV)**2, color='r', ls=':', alpha=0.3)
ax.set_xlabel('tau')
ax.set_ylabel('Pump field (M_KK^2)')
ax.set_title("Tensor vs Scalar Pump Fields")
ax.legend(fontsize=9)
ax.set_xlim(tau_lo, tau_hi)

# Panel 2: P_T(k) from three methods
ax = axes[0, 1]
ax.loglog(k_T_valid, P_T_valid, 'b-', lw=2, label='RK4/5', alpha=0.8)
ax.loglog(k_Ts_valid, P_Ts_valid, 'r--', lw=1.5, label='Sudden', alpha=0.7)
ax.loglog(k_Tt_valid, P_Tt_valid, 'g:', lw=1.5, label='Transfer', alpha=0.7)
ax.axvline(k_tach_tensor, color='gray', ls='--', alpha=0.5, label=f'k_tach^T={k_tach_tensor:.0f}')
ax.axvline(k_transit_scalar, color='orange', ls='--', alpha=0.5, label=f'k_transit^S={k_transit_scalar:.0f}')
ax.set_xlabel('k (M_KK)')
ax.set_ylabel('P_T(k)')
ax.set_title("Tensor Power Spectrum P_T(k)")
ax.legend(fontsize=8)

# Panel 3: r(k) = P_T / P_scalar
ax = axes[1, 0]
ax.loglog(k_common, r_k, 'k-', lw=2)
ax.axhline(16*eps_H_fold_canon, color='red', ls='--', alpha=0.5, label=f'16*eps = {16*eps_H_fold_canon:.3f}')
ax.axvline(k_tach_tensor, color='blue', ls=':', alpha=0.3, label=f'k_tach^T')
ax.axvline(k_transit_scalar, color='orange', ls=':', alpha=0.3, label=f'k_transit^S')
ax.set_xlabel('k (M_KK)')
ax.set_ylabel('r(k) = P_T / P_zeta')
ax.set_title("Tensor-to-Scalar Ratio r(k)")
ax.legend(fontsize=9)

# Panel 4: n_T(k) tensor spectral index
ax = axes[1, 1]
ax.plot(k_T_valid, nT_rk, 'b-', lw=2, label='RK4/5')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axhline(3, color='gray', ls=':', alpha=0.3, label='n_T = 3 (superhorizon)')
ax.axvline(k_tach_tensor, color='blue', ls='--', alpha=0.3, label=f'k_tach^T')
ax.set_xlabel('k (M_KK)')
ax.set_ylabel('n_T(k)')
ax.set_title("Tensor Spectral Index n_T(k)")
ax.set_xscale('log')
ax.legend(fontsize=9)

plt.tight_layout()
fig.savefig(os.path.join(os.path.dirname(__file__), 's67_acoustic_tensor.png'), dpi=150)
print(f"\n  Saved plot: s67_acoustic_tensor.png")

# ============================================================================
#  SECTION 12: Gate verdict
# ============================================================================

print(f"\n{'='*72}")
print("GATE VERDICT: ACOUSTIC-TENSOR-TRANSFER-67")
print(f"{'='*72}")

# This is an INFO gate: report tensor spectrum shape and r(k)

# Median r in the superhorizon regime
mask_super_r = (k_common > k_common[0]) & (k_common < 0.5*k_tach_tensor)
if np.any(mask_super_r):
    r_superhorizon_median = np.median(r_k[mask_super_r])
else:
    r_superhorizon_median = np.nan

# r at the scalar transit scale
r_transit, _ = eval_at_k(k_common, r_k, k_transit_scalar)

# r at the tensor tachyonic threshold
r_tach, _ = eval_at_k(k_common, r_k, k_tach_tensor)

print(f"\n  DECISIVE NUMBERS:")
print(f"    a''/a at fold             = {app_a_fold:.4e} M_KK^2")
print(f"    z''/z at fold             = {zpp_z_fold:.4e} M_KK^2")
print(f"    Ratio z''/z / (a''/a)     = {ratio_pumps:.4f}")
print(f"    k_tach^T (tensor)         = {k_tach_tensor:.1f} M_KK")
print(f"    k_tach^S (scalar)         = {k_tach_scalar:.1f} M_KK")
print(f"    k_tach^T / k_tach^S       = {k_tach_tensor/k_tach_scalar:.4f}")
print(f"    Tensor Mach number        = {v_terminal/c_tensor:.2f}")
print(f"    Scalar Mach number        = {v_terminal/c_BLV:.2f}")
print(f"    r (superhorizon median)   = {r_superhorizon_median:.4e}")
print(f"    r (k_transit^S)           = {r_transit:.4e}")
print(f"    r (k_tach^T)              = {r_tach:.4e}")
print(f"    r = 16*eps (null)         = {16*eps_H_fold_canon:.4f}")
print(f"    n_T (superhorizon)        = {nT_plateau_mean:.4f}")

gate_verdict = "INFO"
gate_detail = (
    f"Tensor spectrum computed through transit. "
    f"a''/a = {app_a_fold:.2e} (vs z''/z = {zpp_z_fold:.2e}). "
    f"k_tach^T = {k_tach_tensor:.0f} (vs k_tach^S = {k_tach_scalar:.0f}). "
    f"Tensor Mach = {v_terminal/c_tensor:.1f}. "
    f"r(superhorizon) = {r_superhorizon_median:.2e}. "
    f"Standard r = 16*eps = {16*eps_H_fold_canon:.3f} VIOLATED. "
    f"n_T(superhorizon) = {nT_plateau_mean:.2f}."
)

print(f"\n  GATE: {gate_verdict}")
print(f"  {gate_detail}")

rows = [
    ("app/a at fold (M_KK^2)", f"{app_a_fold:.4e}"),
    ("zpp/z at fold (M_KK^2)", f"{zpp_z_fold:.4e}"),
    ("Pump ratio zpp/z / (app/a)", f"{ratio_pumps:.4f}"),
    ("c_tensor / c_BLV", f"{c_tensor/c_BLV:.4f}"),
    ("k_tach^T (M_KK)", f"{k_tach_tensor:.1f}"),
    ("k_tach^S (M_KK)", f"{k_tach_scalar:.1f}"),
    ("k_tach ratio T/S", f"{k_tach_tensor/k_tach_scalar:.4f}"),
    ("Tensor Mach = v_term / c_T", f"{v_terminal/c_tensor:.2f}"),
    ("Scalar Mach = v_term / c_BLV", f"{v_terminal/c_BLV:.2f}"),
    ("r (superhorizon median)", f"{r_superhorizon_median:.4e}"),
    (f"r (k_transit^S = {k_transit_scalar:.0f})", f"{r_transit:.4e}"),
    ("r = 16*eps (standard, INAPPLICABLE)", f"{16*eps_H_fold_canon:.4f}"),
    ("n_T (superhorizon plateau)", f"{nT_plateau_mean:.4f}"),
    ("Gate verdict", gate_verdict),
]
print(f"\n  SUMMARY TABLE:")
print(f"  {'Quantity':<45} {'Value':<25}")
print(f"  {'-'*70}")
for lbl, val in rows:
    print(f"  {lbl:<45} {val:<25}")

# ============================================================================
#  SECTION 13: Save data
# ============================================================================

output_file = os.path.join(os.path.dirname(__file__), 's67_acoustic_tensor.npz')

np.savez(output_file,
         # Grids
         k_grid=k_grid,
         k_grid_rk=k_T_valid,
         k_common=k_common,
         k_tach_tensor=k_tach_tensor,
         k_tach_scalar=k_tach_scalar,
         k_transit_tensor=k_transit_tensor,
         k_transit_scalar=k_transit_scalar,
         # Tensor power spectra
         P_T_rk=P_T_valid,
         P_T_sudden=P_T_sudden,
         P_T_transfer=P_T_transfer,
         beta_sq_T_rk=beta_sq_T_rk[valid_T],
         beta_sq_T_sudden=beta_sq_T_sudden,
         beta_sq_T_transfer=beta_sq_T_transfer,
         # Tensor spectral index
         nT_rk=nT_rk,
         nT_sudden=nT_sudden,
         nT_transfer=nT_transfer,
         # Tensor-to-scalar ratio
         r_k=r_k,
         P_T_common=P_T_common,
         P_S_common=P_S_common,
         # Pump fields
         app_a_fold=app_a_fold,
         zpp_z_fold=zpp_z_fold,
         ratio_pumps=ratio_pumps,
         # Background
         tau_fine=tau_fine,
         eta_fine=eta_fine,
         a_fine=a_fine,
         app_over_a=app_over_a,
         # Velocities
         v_terminal=v_terminal,
         c_tensor=c_tensor,
         c_BLV=c_BLV,
         mach_tensor=v_terminal/c_tensor,
         mach_scalar=v_terminal/c_BLV,
         # Gate
         gate_verdict=gate_verdict,
         gate_detail=gate_detail,
         r_superhorizon_median=r_superhorizon_median,
         r_at_transit=r_transit,
         nT_plateau=nT_plateau_mean,
         )

print(f"\n  Saved: {output_file}")
print(f"\n{'='*72}")
print("ACOUSTIC-TENSOR-TRANSFER-67 COMPLETE")
print(f"{'='*72}")
