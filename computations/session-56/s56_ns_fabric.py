"""
s56_ns_fabric.py — NS-FABRIC-56: Spectral Index from Fabric Collective Modes

Gate: NS-FABRIC-56 (INFO -> PASS if n_s in [0.93, 0.99])

Physics:
    The single-cell n_s = -4.45 (S45 KZ-NS-KMAP-45) uses the Dirac spectrum
    with d=8 Weyl class. The fabric's Bogoliubov-Anderson (BA) collective modes
    have LINEAR dispersion (omega ~ c_BA * k) with effective spectral dimension d_s=2.

    For sound-mediated perturbations on a substrate with tau-dependent sound speed c_BA(tau)
    and Hubble-like expansion rate H(tau), the analog spectral index follows from
    the slow-roll formalism adapted to variable-speed-of-sound cosmology:

        epsilon_s = -(1/H) * d(ln c_BA)/dtau     (sound speed slow-roll)
        eta_s = (1/(epsilon_s * H)) * d(epsilon_s)/dtau
        n_s - 1 = -2*epsilon_s - eta_s

    This is the phononic generalization: the tilt comes from the time variation
    of the medium's sound speed, not from a potential.

    Additional routes:
    (A) Direct power spectrum from BA mode counting on d_s=2 lattice
    (B) Analog of Mukhanov-Sasaki with c_BA replacing c
    (C) WKB adiabatic index from omega_BA(k, tau) spectrum

Inputs:
    - computations/session-56/s56_ba_spectrum.npz (BA frequencies at 50 tau)
    - computations/session-56/s56_cba_sound.npz (c_BA at 50 tau)
    - computations/session-54/s54_scale_factor.npz (H at 10 tau, interpolate)

Output:
    - computations/session-56/s56_ns_fabric.npz
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import *

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

# ─────────────────────────────────────────────────────────────
# 1. Load data
# ─────────────────────────────────────────────────────────────

ba_data = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)
cba_data = np.load('computations/session-56/s56_cba_sound.npz', allow_pickle=True)
sf_data = np.load('computations/session-54/s54_scale_factor.npz', allow_pickle=True)

tau_ba = ba_data['tau_values']      # shape (50,), range [0, 0.5]
c_BA = cba_data['c_BA_tau']         # shape (50,), sound speed
omega_BA = ba_data['omega_BA']      # shape (50, 31), BA mode frequencies
N_modes = omega_BA.shape[1]

# Scale factor data: interpolate H from 10 points to 50
tau_sf = sf_data['tau']             # shape (10,)
H_sf = sf_data['H']                # shape (10,)
a_sf = sf_data['a']                # shape (10,)

# Interpolate H and a to the 50-point tau grid
H_interp_func = interp1d(tau_sf, H_sf, kind='cubic', fill_value='extrapolate')
a_interp_func = interp1d(tau_sf, a_sf, kind='cubic', fill_value='extrapolate')

H_50 = H_interp_func(tau_ba)
a_50 = a_interp_func(tau_ba)

# Identify fold index
i_fold = int(cba_data['i_fold'])
tau_fold_val = float(cba_data['tau_fold_actual'])

print(f"tau grid: {len(tau_ba)} points, range [{tau_ba[0]:.4f}, {tau_ba[-1]:.4f}]")
print(f"Fold at index {i_fold}, tau_fold = {tau_fold_val:.5f}")
print(f"H at fold: {H_50[i_fold]:.4f}")
print(f"c_BA at fold: {c_BA[i_fold]:.6f}")
print(f"a at fold: {a_50[i_fold]:.4f}")

# ─────────────────────────────────────────────────────────────
# 2. Route A: Sound-speed slow-roll spectral index
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE A: Sound-speed slow-roll (analog inflationary)")
print("="*70)

dtau = tau_ba[1] - tau_ba[0]

# Compute ln(c_BA) and its derivative
ln_c = np.log(np.abs(c_BA))

# Use central differences for d(ln c_BA)/dtau
d_ln_c = np.gradient(ln_c, dtau)

# epsilon_s = -(1/H) * d(ln c_BA)/dtau
epsilon_s = -(1.0 / H_50) * d_ln_c

# d(epsilon_s)/dtau
d_eps = np.gradient(epsilon_s, dtau)

# eta_s = (1/(epsilon_s * H)) * d(epsilon_s)/dtau
# Avoid division by zero
eta_s = np.full_like(epsilon_s, np.nan)
good = np.abs(epsilon_s * H_50) > 1e-15
eta_s[good] = d_eps[good] / (epsilon_s[good] * H_50[good])

# n_s - 1 = -2*epsilon_s - eta_s
ns_A = 1.0 - 2.0 * epsilon_s - eta_s

print(f"\nAt fold (tau = {tau_fold_val:.5f}):")
print(f"  d(ln c_BA)/dtau = {d_ln_c[i_fold]:.6f}")
print(f"  epsilon_s       = {epsilon_s[i_fold]:.6f}")
print(f"  d(epsilon_s)/dtau = {d_eps[i_fold]:.6f}")
print(f"  eta_s           = {eta_s[i_fold]:.6f}")
print(f"  n_s             = {ns_A[i_fold]:.6f}")

# Also evaluate in the pre-fold region where c_BA is smoothly decreasing
# (tau < 0.19, before the non-monotonic region)
print("\nPre-fold region (smooth decrease):")
pre_fold_mask = tau_ba < tau_fold_val - 0.01
i_pre = np.where(pre_fold_mask)[0]
if len(i_pre) > 0:
    for idx in [0, len(i_pre)//4, len(i_pre)//2, 3*len(i_pre)//4, len(i_pre)-1]:
        ii = i_pre[idx]
        print(f"  tau={tau_ba[ii]:.4f}: eps_s={epsilon_s[ii]:.6f}, "
              f"eta_s={eta_s[ii]:.6f}, n_s={ns_A[ii]:.6f}")

# ─────────────────────────────────────────────────────────────
# 3. Route B: Direct power spectrum slope from BA dispersion
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE B: Direct power spectrum from BA mode counting (d_s=2)")
print("="*70)

# For a d_s-dimensional system with dispersion omega = c_BA * k,
# the density of states goes as g(omega) ~ omega^{d_s - 1}
# For d_s = 2: g(omega) ~ omega (linear DOS)
#
# The primordial power spectrum P(k) for modes that freeze out
# when H(tau_k) = c_BA(tau_k) * k is:
#   P(k) ~ (H^2 / (c_BA * epsilon_s)) at freeze-out
# For nearly constant H and slowly varying c_BA:
#   P(k) ~ 1/(c_BA * epsilon_s)
#
# The spectral index n_s - 1 = d ln P / d ln k

# On the 32-cell graph, the BA modes have discrete k values
# from the graph Laplacian eigenvalues: k_n = sqrt(lambda_n)
lambda_graph = cba_data['lambda_graph']
k_graph = np.sqrt(lambda_graph[1:])  # skip zero mode
print(f"Graph k-values (31 modes): [{k_graph[0]:.4f}, ..., {k_graph[-1]:.4f}]")
print(f"k range ratio: {k_graph[-1]/k_graph[0]:.2f}")

# At the fold, compute the power spectrum P(k) = H^2 / (2 * c_BA * epsilon_s)
# for each mode at its freeze-out time
# Freeze-out condition: omega_BA(k, tau*) = H(tau*)
# i.e., c_BA(tau*) * k = H(tau*)
# -> tau*(k) found by interpolation

# For each k, find tau_freeze where c_BA(tau) * k = H(tau)
tau_freeze_k = np.full(len(k_graph), np.nan)
ns_freeze = np.full(len(k_graph), np.nan)

for j, k_j in enumerate(k_graph):
    # Horizon crossing: c_BA * k = H
    diff_j = c_BA * k_j - H_50
    # Find zero crossings
    sign_changes = np.where(np.diff(np.sign(diff_j)))[0]
    if len(sign_changes) > 0:
        # Take the first crossing (horizon exit)
        ic = sign_changes[0]
        # Linear interpolation for tau_freeze
        frac = -diff_j[ic] / (diff_j[ic+1] - diff_j[ic])
        tau_freeze_k[j] = tau_ba[ic] + frac * dtau

        # Interpolate epsilon_s at freeze-out
        eps_at_freeze = epsilon_s[ic] + frac * (epsilon_s[ic+1] - epsilon_s[ic])
        ns_freeze[j] = 1.0 - 2.0 * eps_at_freeze

valid_freeze = ~np.isnan(tau_freeze_k)
n_frozen = np.sum(valid_freeze)
print(f"\nModes with horizon crossing: {n_frozen} / {len(k_graph)}")

if n_frozen > 2:
    k_frozen = k_graph[valid_freeze]
    tau_frozen = tau_freeze_k[valid_freeze]
    ns_frozen = ns_freeze[valid_freeze]

    print(f"  k range: [{k_frozen[0]:.4f}, {k_frozen[-1]:.4f}]")
    print(f"  tau_freeze range: [{tau_frozen[0]:.4f}, {tau_frozen[-1]:.4f}]")

    # Compute P(k) at each freeze-out
    c_at_freeze = np.interp(tau_frozen, tau_ba, c_BA)
    H_at_freeze = np.interp(tau_frozen, tau_ba, H_50)
    eps_at_freeze = np.interp(tau_frozen, tau_ba, epsilon_s)

    # P(k) ~ H^2 / (c * |epsilon_s|)
    P_k = H_at_freeze**2 / (c_at_freeze * np.abs(eps_at_freeze) + 1e-30)

    # Fit log P vs log k for spectral index
    ln_k = np.log(k_frozen)
    ln_P = np.log(P_k)

    # Linear fit: ln P = (n_s - 1) * ln k + const
    valid_fit = np.isfinite(ln_P)
    if np.sum(valid_fit) > 2:
        coeffs = np.polyfit(ln_k[valid_fit], ln_P[valid_fit], 1)
        ns_B_slope = 1.0 + coeffs[0]

        # Also compute R^2
        p_fit = np.polyval(coeffs, ln_k[valid_fit])
        SS_res = np.sum((ln_P[valid_fit] - p_fit)**2)
        SS_tot = np.sum((ln_P[valid_fit] - np.mean(ln_P[valid_fit]))**2)
        R2_B = 1.0 - SS_res / SS_tot if SS_tot > 0 else 0.0

        print(f"\n  Power spectrum fit:")
        print(f"    n_s - 1 = {coeffs[0]:.6f}")
        print(f"    n_s     = {ns_B_slope:.6f}")
        print(f"    R^2     = {R2_B:.6f}")
    else:
        ns_B_slope = np.nan
        R2_B = np.nan
        print("  Insufficient valid P(k) points for fit")
else:
    ns_B_slope = np.nan
    R2_B = np.nan
    k_frozen = np.array([])
    tau_frozen = np.array([])
    P_k = np.array([])
    print("  Too few modes cross the horizon — trying alternate approach")

# ─────────────────────────────────────────────────────────────
# 3b. Route B alternate: all modes evaluated at fold
# ─────────────────────────────────────────────────────────────

print("\n" + "-"*50)
print("Route B (alternate): All modes evaluated at fold")

# If c_BA*k never reaches H for most modes, evaluate at fold
omega_fold = omega_BA[i_fold, :]  # 31 modes at fold

# Power spectrum for d_s=2: P(k) ~ omega / k^2 * (H/omega)^2
# For modes that haven't frozen out, evaluate amplitude at fold
# P(k) ~ H_fold^2 / (k * c_BA_fold)^2 * (some function of omega/H)
# Standard result for sound horizon: P(k) ~ (H / (c_s * k))^2 at evaluation

H_fold = H_50[i_fold]
c_fold = c_BA[i_fold]
eps_fold = epsilon_s[i_fold]

# For modes with omega < H (super-Hubble at fold)
super_H_mask = omega_fold < H_fold
n_super = np.sum(super_H_mask)
print(f"Super-Hubble modes at fold: {n_super} / {N_modes}")
print(f"  omega range: [{omega_fold[super_H_mask].min():.4f}, {omega_fold[super_H_mask].max():.4f}]"
      if n_super > 0 else "  (none)")
print(f"  H_fold = {H_fold:.4f}")

# Fit slope of omega_BA vs k_graph at fold
ln_k_all = np.log(k_graph)
ln_omega_all = np.log(omega_fold)

coeffs_disp = np.polyfit(ln_k_all, ln_omega_all, 1)
alpha_disp = coeffs_disp[0]  # dispersion exponent: omega ~ k^alpha
print(f"\nDispersion at fold: omega ~ k^{alpha_disp:.4f} (linear = 1.0)")

# For a d_s=2 system with omega~k^alpha and slowly varying c(tau):
# n_s - 1 = (d_s - 1) - 2/alpha + (d/d ln k)(ln epsilon) corrections
# For alpha=1, d_s=2: n_s - 1 = 1 - 2 + corrections = -1 + corrections
# This gives n_s ~ 0 without corrections — VERY DIFFERENT from single-cell d=8

# ─────────────────────────────────────────────────────────────
# 4. Route C: Mukhanov-Sasaki analog with c_BA(tau)
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE C: Mukhanov-Sasaki analog with variable sound speed")
print("="*70)

# In standard inflation with variable sound speed c_s:
#   n_s - 1 = -2*epsilon - eta - s
# where s = (1/H) * d(ln c_s)/dtau (sound speed running)
# and epsilon = -dH/(H^2 dtau), eta = d(epsilon)/(epsilon*H*dtau)
#
# For our framework: H comes from scale factor, c_s = c_BA(tau)

# Compute epsilon_H = -dH/(H^2 dtau)
d_H = np.gradient(H_50, dtau)
epsilon_H = -d_H / (H_50**2)

# Sound speed running: s = (1/H) * d(ln c_BA)/dtau
# NOTE: in the standard formula this enters with a MINUS sign in n_s,
# while epsilon_s above absorbs it. Let's keep them separate.
s_param = (1.0 / H_50) * d_ln_c  # = -epsilon_s

# eta_H from epsilon_H
d_eps_H = np.gradient(epsilon_H, dtau)
eta_H = np.full_like(epsilon_H, np.nan)
good_H = np.abs(epsilon_H * H_50) > 1e-15
eta_H[good_H] = d_eps_H[good_H] / (epsilon_H[good_H] * H_50[good_H])

# Full formula: n_s - 1 = -2*epsilon_H - eta_H - s_param
ns_C = 1.0 - 2.0 * epsilon_H - eta_H - s_param

print(f"\nAt fold (tau = {tau_fold_val:.5f}):")
print(f"  dH/dtau        = {d_H[i_fold]:.6f}")
print(f"  epsilon_H      = {epsilon_H[i_fold]:.6f}")
print(f"  eta_H          = {eta_H[i_fold]:.6f}")
print(f"  s (sound run)  = {s_param[i_fold]:.6f}")
print(f"  -2*eps_H       = {-2*epsilon_H[i_fold]:.6f}")
print(f"  -eta_H         = {-eta_H[i_fold]:.6f}")
print(f"  -s             = {-s_param[i_fold]:.6f}")
print(f"  n_s - 1        = {ns_C[i_fold]-1:.6f}")
print(f"  n_s            = {ns_C[i_fold]:.6f}")

# ─────────────────────────────────────────────────────────────
# 5. Route D: WKB adiabaticity ratio from omega_BA(k, tau)
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE D: WKB adiabaticity and mode-by-mode tilt")
print("="*70)

# For each BA mode k, the adiabaticity parameter is:
#   Q_k = |d omega_k / dtau| / omega_k^2
# When Q_k >> 1 (non-adiabatic), modes get excited = particle creation
# The excitation probability |beta_k|^2 ~ exp(-pi/Q_k) for smooth transit
# Power spectrum tilt from k-dependence of Q_k

d_omega = np.gradient(omega_BA, dtau, axis=0)  # d(omega)/dtau at each tau

Q_k = np.abs(d_omega) / (omega_BA**2 + 1e-30)  # shape (50, 31)

# At the fold:
Q_fold = Q_k[i_fold, :]
print(f"Q_k at fold: [{Q_fold.min():.4f}, {Q_fold.max():.4f}]")
print(f"  mean Q = {Q_fold.mean():.4f}")

# Excitation probability (Landau-Zener style):
beta2_k = np.exp(-np.pi / (Q_fold + 1e-30))
# For modes where Q >> 1 (non-adiabatic), beta2 -> 1
# For modes where Q << 1 (adiabatic), beta2 -> 0

# Power spectrum from mode excitation: P(k) ~ beta_k^2 * (H/omega_k)^2
# For d_s=2: additional k^{d_s-1} = k factor from phase space
P_D = beta2_k * (H_fold / omega_fold)**2

# Fit spectral index
ln_k_all = np.log(k_graph)
ln_P_D = np.log(P_D + 1e-30)

valid_D = np.isfinite(ln_P_D) & (P_D > 1e-20)
if np.sum(valid_D) > 2:
    coeffs_D = np.polyfit(ln_k_all[valid_D], ln_P_D[valid_D], 1)
    ns_D = 1.0 + coeffs_D[0]

    p_fit_D = np.polyval(coeffs_D, ln_k_all[valid_D])
    SS_res_D = np.sum((ln_P_D[valid_D] - p_fit_D)**2)
    SS_tot_D = np.sum((ln_P_D[valid_D] - np.mean(ln_P_D[valid_D]))**2)
    R2_D = 1.0 - SS_res_D / SS_tot_D if SS_tot_D > 0 else 0.0

    print(f"\nWKB power spectrum fit:")
    print(f"  n_s - 1 = {coeffs_D[0]:.6f}")
    print(f"  n_s     = {ns_D:.6f}")
    print(f"  R^2     = {R2_D:.6f}")
    print(f"  Valid modes: {np.sum(valid_D)}")
else:
    ns_D = np.nan
    R2_D = np.nan
    print("  Insufficient excited modes for fit")

# ─────────────────────────────────────────────────────────────
# 6. Route E: Effective spectral index from c_BA power law
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE E: Effective index from c_BA(tau) power-law structure")
print("="*70)

# In the pre-fold region, c_BA ~ tau^p for some effective p
# Then n_s - 1 = -2p/(1-p) in de Sitter-like backgrounds
# (This is the k-inflation result for P(X) theories)

# Fit c_BA to power law in pre-fold region
pre_fold = tau_ba[2:i_fold]  # skip tau=0
c_pre = c_BA[2:i_fold]

ln_tau_pre = np.log(pre_fold)
ln_c_pre = np.log(c_pre)

coeffs_E = np.polyfit(ln_tau_pre, ln_c_pre, 1)
p_eff = coeffs_E[0]  # c_BA ~ tau^p_eff

p_fit_E = np.polyval(coeffs_E, ln_tau_pre)
SS_res_E = np.sum((ln_c_pre - p_fit_E)**2)
SS_tot_E = np.sum((ln_c_pre - np.mean(ln_c_pre))**2)
R2_E = 1.0 - SS_res_E / SS_tot_E if SS_tot_E > 0 else 0.0

print(f"c_BA ~ tau^{p_eff:.4f}  (R^2 = {R2_E:.6f})")

# For power-law c_s in de Sitter:
# n_s - 1 = -2*p_eff / (1 + p_eff)  [DBI-type result]
ns_E_dbi = 1.0 - 2.0 * p_eff / (1.0 + p_eff)
print(f"DBI-type n_s = {ns_E_dbi:.6f}")

# Alternative: n_s - 1 = p_eff * (something from H variation)
# For H ~ const (quasi-de Sitter), epsilon_H ~ 0:
# n_s - 1 ≈ -s = -p_eff / tau_fold * (1/H)
# But this is the local slope, which we computed in Route A

# More carefully: if c_BA = c_0 * (tau/tau_0)^p, then
# d(ln c)/dtau = p/tau
# epsilon_s = -p / (H * tau)
# This should match Route A
eps_powerlaw = -p_eff / (H_50[i_fold] * tau_fold_val)
print(f"Power-law epsilon_s at fold: {eps_powerlaw:.6f}")
print(f"Route A epsilon_s at fold:   {epsilon_s[i_fold]:.6f}")

# ─────────────────────────────────────────────────────────────
# 7. Route F: d_s-corrected spectral index
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE F: Spectral dimension correction (d_s = 2)")
print("="*70)

# For a d_s-dimensional phonon system, the power spectrum of
# density fluctuations scales as:
#   P(k) ~ k^{d_s - 1} * (H / c_s)^2 / epsilon
#
# The spectral index of the curvature perturbation is:
#   n_s - 1 = (d_s - 1) - 2*d_H/d_ln_k - d_epsilon/d_ln_k - d_c_s/d_ln_k
#
# For standard 3D: n_s - 1 = 2 - 2*epsilon_H - eta_H - s → n_s ~ 0.965
# For d_s = 2: n_s - 1 = 1 - 2*epsilon_H - eta_H - s
# But this overcounts: the (d_s - 1) is phase space, already in the
# definition. The standard result n_s - 1 = -2*epsilon - eta - s
# is independent of d_s for SCALAR perturbations.
#
# However, for a 2D substrate, the freeze-out condition changes:
# k * c_BA = H/a (3D) vs k * c_BA = H (in tau-natural units, no 'a')
# The relationship between k and tau at freeze-out changes.

# In our framework, tau IS the time variable. Modes freeze when
# their physical frequency drops below H. For BA phonons:
# omega_k = c_BA(tau) * k_phys = c_BA(tau) * k / a(tau)
# Freeze-out: c_BA(tau*) * k / a(tau*) = H(tau*)
# -> k = a(tau*) * H(tau*) / c_BA(tau*)

# The spectral index picks up a tilt from the tau-dependence of a*H/c_BA
aH_over_c = a_50 * H_50 / c_BA

ln_aHc = np.log(np.abs(aH_over_c))
d_ln_aHc = np.gradient(ln_aHc, dtau)

# n_s - 1 = d(ln P) / d(ln k)
# P(k) ~ H^2 / (epsilon * c_BA) at freeze-out
# d(ln k) = d(ln(aH/c_BA)) * dtau

# At freeze-out: k = aH/c_BA, so d ln k = d ln(aH/c_BA)
# n_s - 1 = [d ln(H^2/(epsilon*c_BA))/dtau] / [d ln(aH/c_BA)/dtau]

num = np.gradient(np.log(H_50**2 / (np.abs(epsilon_s) * c_BA + 1e-30)), dtau)
denom = d_ln_aHc

ns_F = 1.0 + num / (denom + 1e-30)

# Evaluate at fold
print(f"At fold:")
print(f"  a*H/c_BA     = {aH_over_c[i_fold]:.4f}")
print(f"  d(ln aH/c)/dtau = {d_ln_aHc[i_fold]:.4f}")
print(f"  numerator    = {num[i_fold]:.6f}")
print(f"  n_s          = {ns_F[i_fold]:.6f}")

# ─────────────────────────────────────────────────────────────
# 8. Route G: Exact numerical Mukhanov-Sasaki (beyond slow-roll)
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("ROUTE G: Exact numerical mode evolution (beyond slow-roll)")
print("="*70)

# The slow-roll approximation FAILS: epsilon_s ~ 1.8, eta_s ~ 1.4 at fold.
# We must solve the mode equation EXACTLY.
#
# For perturbations in a medium with sound speed c_s(tau) and expansion H(tau):
#   v_k'' + (c_s^2 k^2 - z''/z) v_k = 0   [Mukhanov-Sasaki equation]
# where z = a * sqrt(2*epsilon_H) / c_s  [pump field]
#
# At late times (after freeze-out), |v_k|^2 -> P(k) * k^3 / (2*pi^2)
# n_s - 1 = d ln P / d ln k
#
# We solve this for a range of k values and extract the slope.

from scipy.integrate import solve_ivp

# Build smooth interpolators for the key quantities
from scipy.interpolate import CubicSpline

c_BA_cs = CubicSpline(tau_ba, c_BA)
H_cs = CubicSpline(tau_ba, H_50)
a_cs = CubicSpline(tau_ba, a_50)
eps_H_cs = CubicSpline(tau_ba, epsilon_H)

# The pump field z = a * sqrt(2*epsilon_H) / c_s
# We need z''/z. Compute numerically.
z_arr = a_50 * np.sqrt(2.0 * np.abs(epsilon_H)) / (c_BA + 1e-30)
z_cs = CubicSpline(tau_ba, z_arr)

# z''/z from spline second derivative
z_pp_over_z = np.zeros_like(tau_ba)
for i in range(len(tau_ba)):
    z_val = z_cs(tau_ba[i])
    z_pp = z_cs(tau_ba[i], 2)
    if abs(z_val) > 1e-30:
        z_pp_over_z[i] = z_pp / z_val

z_pp_z_cs = CubicSpline(tau_ba, z_pp_over_z)

# Choose k values spanning the BA mode range
# Use the graph Laplacian eigenvalues as physical k
k_test = k_graph[::3]  # every 3rd mode to keep it tractable
if len(k_test) < 5:
    k_test = k_graph

# For each k, solve the mode equation from early tau to the fold
# Initial conditions: Bunch-Davies vacuum (WKB at early times)
#   v_k = (1/sqrt(2*omega_k)) * exp(-i * int omega_k dtau)
# where omega_k = c_s * k

tau_start = tau_ba[1]  # avoid tau=0
tau_end = tau_fold_val

P_k_G = np.zeros(len(k_test))
omega_k_at_start = c_BA_cs(tau_start) * k_test

for j, k_j in enumerate(k_test):
    omega_0 = c_BA_cs(tau_start) * k_j

    # Mode equation: v'' + (c_s^2 * k^2 - z''/z) * v = 0
    # Write as system: y = [Re(v), Im(v), Re(v'), Im(v')]
    def mode_eq(tau, y):
        c_s = c_BA_cs(tau)
        zppz = z_pp_z_cs(tau)
        omega2 = c_s**2 * k_j**2 - zppz
        return [y[2], y[3], -omega2 * y[0], -omega2 * y[1]]

    # Bunch-Davies initial conditions
    # v = 1/sqrt(2*omega_0), v' = -i*omega_0 * v
    v0 = 1.0 / np.sqrt(2.0 * omega_0)
    y0 = [v0, 0.0, 0.0, -omega_0 * v0]  # Re(v), Im(v), Re(v'), Im(v')

    try:
        sol = solve_ivp(mode_eq, [tau_start, tau_end], y0,
                       method='RK45', rtol=1e-8, atol=1e-12,
                       max_step=dtau/2)
        if sol.success:
            v_re = sol.y[0, -1]
            v_im = sol.y[1, -1]
            v_abs2 = v_re**2 + v_im**2
            # P(k) = k^3 * |v_k|^2 / (2*pi^2 * z^2)
            z_end = z_cs(tau_end)
            P_k_G[j] = k_j**3 * v_abs2 / (2.0 * np.pi**2 * z_end**2) if abs(z_end) > 1e-30 else np.nan
        else:
            P_k_G[j] = np.nan
    except Exception:
        P_k_G[j] = np.nan

# Fit spectral index
valid_G = np.isfinite(P_k_G) & (P_k_G > 0)
n_valid_G = np.sum(valid_G)
print(f"Solved {n_valid_G} / {len(k_test)} modes successfully")

if n_valid_G > 2:
    ln_k_G = np.log(k_test[valid_G])
    ln_P_G = np.log(P_k_G[valid_G])

    coeffs_G = np.polyfit(ln_k_G, ln_P_G, 1)
    ns_G = 1.0 + coeffs_G[0]

    p_fit_G = np.polyval(coeffs_G, ln_k_G)
    SS_res_G = np.sum((ln_P_G - p_fit_G)**2)
    SS_tot_G = np.sum((ln_P_G - np.mean(ln_P_G))**2)
    R2_G = 1.0 - SS_res_G / SS_tot_G if SS_tot_G > 0 else 0.0

    print(f"\nExact mode equation fit:")
    print(f"  n_s - 1 = {coeffs_G[0]:.6f}")
    print(f"  n_s     = {ns_G:.6f}")
    print(f"  R^2     = {R2_G:.6f}")

    for j in range(min(5, n_valid_G)):
        idx = np.where(valid_G)[0][j]
        print(f"  k={k_test[idx]:.4f}: P(k)={P_k_G[idx]:.6e}")
else:
    ns_G = np.nan
    R2_G = np.nan
    print("  Insufficient modes solved")

# ─────────────────────────────────────────────────────────────
# 9. Summary and comparison
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("SUMMARY: Spectral Index Estimates at Fold")
print("="*70)

print("\nCRITICAL: Slow-roll approximation INVALID at fold:")
print(f"  epsilon_s = {epsilon_s[i_fold]:.3f} (need << 1)")
print(f"  eta_s     = {eta_s[i_fold]:.3f} (need << 1)")
print(f"  epsilon_H = {epsilon_H[i_fold]:.3f} (marginal)")
print("Routes A, C, E use slow-roll and are UNRELIABLE at fold.")
print("Routes D, F, G do NOT assume slow-roll.\n")

results = {
    'A: sound-speed slow-roll (INVALID)': ns_A[i_fold],
    'C: Mukhanov-Sasaki slow-roll (INVALID)': ns_C[i_fold],
    'D: WKB excitation': ns_D,
    'E: power-law DBI (INVALID)': ns_E_dbi,
    'F: exact freeze-out slope': ns_F[i_fold],
    'G: exact mode equation': ns_G,
}

if not np.isnan(ns_B_slope):
    results['B: horizon crossing'] = ns_B_slope

print(f"{'Route':<42} {'n_s':>10} {'n_s - 1':>10} {'|n_s - 0.965|':>14}")
print("-"*80)
for name, val in results.items():
    if np.isfinite(val):
        marker = " <-- BEST" if 'F' in name[:2] or 'G' in name[:2] else ""
        print(f"{name:<42} {val:>10.6f} {val-1:>10.6f} {abs(val-0.965):>14.6f}{marker}")
    else:
        print(f"{name:<42} {'NaN':>10} {'NaN':>10} {'NaN':>14}")

# Best estimate from non-slow-roll routes
ns_valid = []
ns_labels = []
for label, val in [('F', ns_F[i_fold]), ('G', ns_G), ('D', ns_D)]:
    if np.isfinite(val):
        ns_valid.append(val)
        ns_labels.append(label)

ns_best = np.mean(ns_valid) if ns_valid else np.nan
ns_spread = (max(ns_valid) - min(ns_valid)) / 2.0 if len(ns_valid) > 1 else np.nan

print(f"\nBest estimate (non-slow-roll routes {','.join(ns_labels)}):")
print(f"  n_s = {ns_best:.6f} +/- {ns_spread:.6f}")
print(f"Observed (Planck 2018):   n_s = 0.9649 +/- 0.0042")
print(f"S45 single-cell:          n_s = -4.45")

# Gate verdict
in_range = 0.93 <= ns_best <= 0.99
print(f"\nGate NS-FABRIC-56: {'PASS' if in_range else 'FAIL'} "
      f"(n_s = {ns_best:.4f}, range [0.93, 0.99])")

# ─────────────────────────────────────────────────────────────
# 9. Profile: n_s across full transit
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("PROFILE: n_s(tau) across transit")
print("="*70)

# Show Route F (exact) alongside slow-roll for comparison
print(f"\n{'tau':>8} {'n_s(F)':>10} {'n_s(C)':>10} {'eps_H':>10} {'eps_s':>10} {'c_BA':>10}")
print("-"*62)
step = max(1, len(tau_ba) // 20)
for i in range(0, len(tau_ba), step):
    print(f"{tau_ba[i]:>8.4f} {ns_F[i]:>10.4f} {ns_C[i]:>10.4f} "
          f"{epsilon_H[i]:>10.4f} {epsilon_s[i]:>10.4f} {c_BA[i]:>10.4f}")

# ─────────────────────────────────────────────────────────────
# 10. Physical diagnostics
# ─────────────────────────────────────────────────────────────

print("\n" + "="*70)
print("PHYSICAL DIAGNOSTICS")
print("="*70)

# Number of e-folds
# N_e = integral of H dtau from some initial tau to fold
N_e_to_fold = np.trapezoid(H_50[:i_fold+1], tau_ba[:i_fold+1])
print(f"e-folds from tau=0 to fold: N_e = {N_e_to_fold:.4f}")

# Sound horizon at fold
# r_s = integral c_BA / a dtau
r_s = np.trapezoid(c_BA[:i_fold+1] / a_50[:i_fold+1], tau_ba[:i_fold+1])
print(f"Sound horizon at fold: r_s = {r_s:.4f}")

# Ratio of sound horizon to Hubble radius
print(f"r_s * H_fold = {r_s * H_fold:.4f} (should be O(1) for freeze-out)")

# Slow-roll validity check
print(f"\nSlow-roll validity at fold:")
print(f"  |epsilon_H| = {abs(epsilon_H[i_fold]):.6f} {'<< 1 OK' if abs(epsilon_H[i_fold]) < 1 else '>= 1 VIOLATED'}")
print(f"  |epsilon_s| = {abs(epsilon_s[i_fold]):.6f} {'<< 1 OK' if abs(epsilon_s[i_fold]) < 1 else '>= 1 VIOLATED'}")
print(f"  |eta_H|     = {abs(eta_H[i_fold]):.6f} {'<< 1 OK' if abs(eta_H[i_fold]) < 1 else '>= 1 VIOLATED'}")
print(f"  |s|         = {abs(s_param[i_fold]):.6f} {'<< 1 OK' if abs(s_param[i_fold]) < 1 else '>= 1 VIOLATED'}")

# Comparison: single-cell vs fabric
print(f"\n{'Single-cell n_s (S45)':>30}: -4.45 (d=8 Weyl, Bogoliubov coeffs)")
print(f"{'Fabric n_s (this computation)':>30}: {ns_best:.4f} (d_s=2 BA phonons, c_BA tilt)")
print(f"{'Improvement factor':>30}: {abs(-4.45 - 0.965) / abs(ns_best - 0.965):.1f}x closer to observed")

# ─────────────────────────────────────────────────────────────
# 11. Save results
# ─────────────────────────────────────────────────────────────

np.savez('computations/session-56/s56_ns_fabric.npz',
    # Grid
    tau_values=tau_ba,
    i_fold=i_fold,
    tau_fold=tau_fold_val,

    # Route A: sound-speed slow-roll
    epsilon_s=epsilon_s,
    eta_s=eta_s,
    ns_A=ns_A,
    ns_A_fold=ns_A[i_fold],
    d_ln_c=d_ln_c,

    # Route B: horizon crossing
    k_graph=k_graph,
    ns_B=ns_B_slope,
    R2_B=R2_B,
    k_frozen=k_frozen if n_frozen > 2 else np.array([]),
    tau_frozen=tau_frozen if n_frozen > 2 else np.array([]),

    # Route C: Mukhanov-Sasaki analog
    epsilon_H=epsilon_H,
    eta_H=eta_H,
    s_param=s_param,
    ns_C=ns_C,
    ns_C_fold=ns_C[i_fold],

    # Route D: WKB
    Q_k_fold=Q_fold,
    beta2_fold=beta2_k,
    ns_D=ns_D,
    R2_D=R2_D,

    # Route E: power-law
    p_eff=p_eff,
    R2_E=R2_E,
    ns_E_dbi=ns_E_dbi,

    # Route F: freeze-out
    ns_F=ns_F,
    ns_F_fold=ns_F[i_fold],
    aH_over_c=aH_over_c,

    # Route G: exact mode equation
    ns_G=ns_G,
    R2_G=R2_G,
    k_test_G=k_test,
    P_k_G=P_k_G,

    # Best estimate (non-slow-roll routes)
    ns_best=ns_best,
    ns_spread=ns_spread,
    slow_roll_violated=True,
    epsilon_s_fold=epsilon_s[i_fold],
    eta_s_fold=eta_s[i_fold],

    # Diagnostics
    N_e_to_fold=N_e_to_fold,
    r_s_fold=r_s,
    H_50=H_50,
    a_50=a_50,
    c_BA_tau=c_BA,

    # Gate
    gate_name='NS-FABRIC-56',
    gate_verdict='PASS' if in_range else 'FAIL',
    gate_criterion='n_s in [0.93, 0.99]',
)

print(f"\nSaved to computations/session-56/s56_ns_fabric.npz")
print(f"\nGATE: NS-FABRIC-56 = {'PASS' if in_range else 'FAIL'}")
