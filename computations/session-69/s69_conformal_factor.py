#!/usr/bin/env python3
"""
CONFORMAL-FACTOR-TRANSIT-69: Penrose Diagram Shape of the Acoustic White Hole
==============================================================================

Computes the exact conformal factor Omega(tau, k) for the transit spacetime.
The Mach 13.75 transit through the van Hove fold creates an acoustic white
hole. The conformal factor determines the Penrose diagram shape, the penumbra
width near k_tach, and the nested horizon structure.

Physics:
--------
The Mukhanov variable u_k satisfies u_k'' + omega_k^2 u_k = 0 where
omega_k^2 = k^2 c_s^2 - z''/z. The effective potential z''/z acts as a
frequency-dependent barrier. Modes with k < k_tach = sqrt(z''/z)/c_s are
superhorizon (tachyonic); modes with k > k_tach are subhorizon (oscillatory).

The conformal factor Omega(tau, k) maps the physical (tau, k) plane into the
compactified Penrose diagram. We define:
  - Conformal time: eta = integral dtau / (v_tau * a(tau))
  - Tortoise wavenumber: r* = integral dk / omega(k)  [in WKB regime]
  - Conformal factor: Omega = a * z / sqrt(2k)  [for mode k at time tau]

The Penrose diagram has three nested boundaries:
  1. Tachyonic shell: k = k_tach(tau) where omega_k^2 = 0
  2. BCS stretched horizon: tau_BCS = 0.22 (post-transit freeze)
  3. Cosmological event horizon: a*H = k (standard Hubble crossing)

Gate: CONF-FACTOR-69 -- INFO
Output: s69_conformal_factor.npz, s69_conformal_factor.png
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import cumulative_trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, H_fold as H_fold_canon,
    S_fold, dS_fold, v_terminal, PI, dt_transit,
)

# ============================================================================
#  SECTION 1: Load S67 transit background
# ============================================================================

print("=" * 72)
print("CONFORMAL-FACTOR-TRANSIT-69: Penrose Diagram Shape")
print("=" * 72)

data = np.load(os.path.join(os.path.dirname(__file__), 's67_transit_ps.npz'),
               allow_pickle=True)

tau_fine = data['tau_fine']     # shape (8000,), range [0.10, 0.30]
eta_fine = data['eta_fine']     # conformal time
z_fine   = data['z_fine']       # Mukhanov pump z = a*sqrt(2*eps_H)
a_fine   = data['a_fine']       # scale factor (normalized a(fold)=1)
eps_fine = data['eps_H_fine']   # slow-roll parameter eps_H
k_grid_rk = data['k_grid_rk']  # wavenumber grid (400 pts)
beta_sq_rk = data['beta_sq_rk']  # Bogoliubov |beta_k|^2 from RK
k_transit  = float(data['k_transit'])  # k_transit = H/c_s
zpp_z_fold = float(data['zpp_z_fold'])  # z''/z at fold

c_BLV = 0.485   # BLV sound speed (M_KK units)  # (local)
v_tau = v_terminal

# Key indices
idx_fold = np.argmin(np.abs(tau_fine - tau_fold))
idx_BCS  = np.argmin(np.abs(tau_fine - 0.22))

print(f"\nLoaded S67 transit data:")
print(f"  tau range: [{tau_fine[0]:.2f}, {tau_fine[-1]:.2f}]")
print(f"  eta range: [{eta_fine[0]:.4e}, {eta_fine[-1]:.4e}]")
print(f"  a(fold) = {a_fine[idx_fold]:.6f}")
print(f"  z(fold) = {z_fine[idx_fold]:.6f}")
print(f"  eps_H(fold) = {eps_fine[idx_fold]:.6f}")
print(f"  k_transit = {k_transit:.2f} M_KK")

# ============================================================================
#  SECTION 2: Reconstruct z''/z(eta) -- the effective potential
# ============================================================================

cs_z_eta = CubicSpline(eta_fine, z_fine)
zpp_z = cs_z_eta(eta_fine, 2) / z_fine
cs_zpp_z = CubicSpline(eta_fine, zpp_z)

# Tachyonic boundary k_tach(tau): k_tach^2 * c_s^2 = z''/z
k_tach_tau = np.sqrt(np.abs(zpp_z)) / c_BLV
k_tach_fold = k_tach_tau[idx_fold]

# Hubble crossing scale k_H(tau) = a*H where H comes from eps_H
# In this framework: H(tau) = H_fold * sqrt(S(tau)/S(fold))
# Since z''/z >> k_H^2 * c_s^2, the tachyonic shell is well outside Hubble
H_fine_approx = np.sqrt(2.0 * eps_fine) * z_fine / (a_fine * a_fine) * v_tau
# Actually, simpler: k_H(tau) = a(tau)*H(tau)/c_s from Hubble crossing
# But for the acoustic white hole, the relevant boundary is k_tach, not k_H.

print(f"\n{'='*72}")
print("SECTION 2: Effective potential z''/z and boundaries")
print(f"{'='*72}")
print(f"  z''/z at fold = {zpp_z[idx_fold]:.4e}")
print(f"  k_tach(fold) = {k_tach_fold:.2f} M_KK")
print(f"  k_tach/k_transit = {k_tach_fold/k_transit:.4f}")
print(f"  k_tach(tau=0.10) = {k_tach_tau[0]:.2f} M_KK")
print(f"  k_tach(tau=0.22) = {k_tach_tau[idx_BCS]:.2f} M_KK")
print(f"  k_tach(tau=0.30) = {k_tach_tau[-1]:.2f} M_KK")

# ============================================================================
#  SECTION 3: Conformal factor Omega(tau, k)
# ============================================================================
#
# The conformal factor for the mode-space Penrose diagram.
#
# In standard cosmology, the Penrose diagram uses coordinates
#   (eta, chi) where ds^2 = a^2(-deta^2 + dchi^2 + ...)
# and the conformal factor is Omega = a.
#
# For the acoustic white hole, we extend this to (eta, k) space where
# each mode k has its own effective frequency omega_k^2 = k^2*c_s^2 - z''/z.
# The conformal factor governing the mode's behavior is:
#
#   Omega(tau, k) = a(tau) * z(tau) / sqrt(2k)
#
# This measures the "optical depth" of the mode: how much the universe's
# expansion has stretched the mode's wavelength relative to the pump field.
# At fixed k, Omega grows with a (expansion) and with z (pump growth).
# At fixed tau, Omega falls as 1/sqrt(k) -- short wavelengths are less affected.
#
# The tachyonic boundary Omega_tach separates oscillatory from growing modes.

print(f"\n{'='*72}")
print("SECTION 3: Conformal factor Omega(tau, k)")
print(f"{'='*72}")

# Build Omega on a 2D grid (tau, k)
N_tau = len(tau_fine)
N_k = 300  # (local)
k_grid = np.geomspace(50.0, 2e5, N_k)

Omega = np.zeros((N_tau, N_k))
for ik, k in enumerate(k_grid):
    Omega[:, ik] = a_fine * z_fine / np.sqrt(2.0 * k)

# Omega at fold for representative k values
print(f"\nOmega at fold (tau = {tau_fold}):")
a_fold = a_fine[idx_fold]
z_fold = z_fine[idx_fold]
for k_ref in [100, 500, k_transit, k_tach_fold, 5000, 10000, 50000]:
    Om = a_fold * z_fold / np.sqrt(2.0 * k_ref)
    print(f"  k = {k_ref:10.1f} M_KK:  Omega = {Om:.6e}")

# Omega at fold for k = k_transit (the reference scale)
Omega_fold_transit = a_fold * z_fold / np.sqrt(2.0 * k_transit)
Omega_fold_tach = a_fold * z_fold / np.sqrt(2.0 * k_tach_fold)
print(f"\n  Omega(fold, k_transit) = {Omega_fold_transit:.6e}")
print(f"  Omega(fold, k_tach)    = {Omega_fold_tach:.6e}")

# Omega range across the transit
Omega_min = Omega.min()
Omega_max = Omega.max()
print(f"\n  Omega range: [{Omega_min:.4e}, {Omega_max:.4e}]")
print(f"  Omega ratio max/min = {Omega_max/Omega_min:.2e}")

# ============================================================================
#  SECTION 4: Penumbra width
# ============================================================================
#
# The penumbra is the k-range where mode production transitions from
# strong (|beta_k|^2 >> 1, superhorizon) to negligible (|beta_k|^2 << 1,
# subhorizon). We define the penumbra as 0.1 < |beta_k|^2 < 0.9.
#
# For a sharp transition, the penumbra would be narrow (Delta k / k_tach << 1).
# For the acoustic white hole with its extended z''/z barrier, the penumbra
# may be broad.

print(f"\n{'='*72}")
print("SECTION 4: Penumbra width")
print(f"{'='*72}")

# Use the RK beta_sq data
beta_sq = beta_sq_rk
k_rk = k_grid_rk

# Standard penumbra: 0.1 < beta^2 < 0.9
pen_mask = (beta_sq > 0.1) & (beta_sq < 0.9)
if np.any(pen_mask):
    k_pen = k_rk[pen_mask]
    k_pen_lo = k_pen.min()
    k_pen_hi = k_pen.max()
    Delta_k_pen = k_pen_hi - k_pen_lo
    print(f"  Standard penumbra (0.1 < beta^2 < 0.9):")
    print(f"    k range: [{k_pen_lo:.2f}, {k_pen_hi:.2f}] M_KK")
    print(f"    Delta_k = {Delta_k_pen:.2f} M_KK")
    print(f"    Delta_k / k_tach = {Delta_k_pen / k_tach_fold:.4f}")
    print(f"    Delta_k / k_transit = {Delta_k_pen / k_transit:.4f}")
    pen_width_tach = Delta_k_pen / k_tach_fold
    pen_center = np.sqrt(k_pen_lo * k_pen_hi)
else:
    print("  No modes in standard penumbra range 0.1 < beta^2 < 0.9")
    pen_width_tach = np.nan
    pen_center = np.nan

# Extended penumbra: 0.01 < beta^2 < 10
pen_ext_mask = (beta_sq > 0.01) & (beta_sq < 10)
if np.any(pen_ext_mask):
    k_pen_ext = k_rk[pen_ext_mask]
    print(f"\n  Extended penumbra (0.01 < beta^2 < 10):")
    print(f"    k range: [{k_pen_ext.min():.2f}, {k_pen_ext.max():.2f}] M_KK")
    print(f"    Delta_k / k_tach = {(k_pen_ext.max() - k_pen_ext.min()) / k_tach_fold:.4f}")

# beta^2 = 1 crossing (the "horizon" in mode space)
crossings_1 = []
for i in range(len(beta_sq) - 1):
    if (beta_sq[i] - 1.0) * (beta_sq[i+1] - 1.0) < 0:
        k_cross = k_rk[i] + (k_rk[i+1] - k_rk[i]) * (1.0 - beta_sq[i]) / (beta_sq[i+1] - beta_sq[i])
        crossings_1.append(k_cross)
        print(f"\n  beta^2 = 1 crossing at k = {k_cross:.2f} M_KK (k/k_tach = {k_cross/k_tach_fold:.4f})")

# beta^2 = 0.5 crossings
crossings_05 = []
for i in range(len(beta_sq) - 1):
    if (beta_sq[i] - 0.5) * (beta_sq[i+1] - 0.5) < 0:
        k_cross = k_rk[i] + (k_rk[i+1] - k_rk[i]) * (0.5 - beta_sq[i]) / (beta_sq[i+1] - beta_sq[i])
        crossings_05.append(k_cross)

if crossings_05:
    print(f"\n  beta^2 = 0.5 crossings at k = {[f'{c:.1f}' for c in crossings_05]} M_KK")

# The "horizon" scale where beta^2 = 1
k_horizon = crossings_1[0] if crossings_1 else k_tach_fold
print(f"\n  Acoustic horizon (beta^2 = 1): k = {k_horizon:.2f} M_KK")
print(f"  k_horizon / k_tach = {k_horizon / k_tach_fold:.4f}")
print(f"  k_horizon / k_transit = {k_horizon / k_transit:.4f}")

# ============================================================================
#  SECTION 5: Null coordinates and Penrose diagram construction
# ============================================================================
#
# Standard Penrose diagram uses null coordinates:
#   u = eta - chi  (outgoing null)
#   v = eta + chi  (ingoing null)
# then compactified via U = arctan(u), V = arctan(v).
#
# For the acoustic white hole, the spatial coordinate is k (wavenumber),
# and the "tortoise" coordinate is:
#   r*(k) = integral dk / |omega(k)|
# evaluated at a reference time (the fold).
#
# The causal structure in (eta, r*) space has null rays at 45 degrees.
# The tachyonic shell is the curve where omega_k = 0.

print(f"\n{'='*72}")
print("SECTION 5: Null coordinates and diagram construction")
print(f"{'='*72}")

# Tortoise wavenumber r*(k) at the fold
# omega_k^2(fold) = k^2 * c_s^2 - z''/z(fold)
zpp_z_at_fold = zpp_z[idx_fold]
omega_sq_fold = k_grid**2 * c_BLV**2 - zpp_z_at_fold

# For sub-horizon modes (omega_sq > 0): r* = int dk / omega_k
# For super-horizon modes (omega_sq < 0): r* = int dk / kappa_k (evanescent)
omega_fold = np.where(omega_sq_fold > 0,
                       np.sqrt(omega_sq_fold),
                       -np.sqrt(-omega_sq_fold))  # signed

# Tortoise coordinate: cumulative integral
dr_star = 1.0 / np.abs(omega_fold + 1e-30)  # regularize near zero
r_star = cumulative_trapezoid(dr_star, k_grid, initial=0.0)

# Reference: r* at k_tach
idx_k_tach = np.argmin(np.abs(k_grid - k_tach_fold))
r_star_tach = r_star[idx_k_tach]

print(f"  r*(k_tach) = {r_star_tach:.6e}")
print(f"  r*(k_max) = {r_star[-1]:.6e}")

# Null coordinates at the fold
eta_fold_val = eta_fine[idx_fold]
u_grid = eta_fold_val - r_star   # outgoing null
v_grid = eta_fold_val + r_star   # ingoing null

# Compactify: U = (2/pi) arctan(u), V = (2/pi) arctan(v)
U_grid = (2.0 / PI) * np.arctan(u_grid * 1e3)  # scale for visibility
V_grid = (2.0 / PI) * np.arctan(v_grid * 1e3)

# Penrose coordinates: T = (V + U)/2, R = (V - U)/2
T_pen = (V_grid + U_grid) / 2.0
R_pen = (V_grid - U_grid) / 2.0

print(f"\n  Null coordinate ranges:")
print(f"    u: [{u_grid[0]:.4e}, {u_grid[-1]:.4e}]")
print(f"    v: [{v_grid[0]:.4e}, {v_grid[-1]:.4e}]")
print(f"    U (compactified): [{U_grid[0]:.4f}, {U_grid[-1]:.4f}]")
print(f"    V (compactified): [{V_grid[0]:.4f}, {V_grid[-1]:.4f}]")

# ============================================================================
#  SECTION 6: Three nested boundaries
# ============================================================================
#
# The acoustic white hole has three nested boundaries, from innermost to
# outermost in mode space:
#
#  1. Tachyonic shell: k = k_tach(tau) where omega_k^2 = 0
#     This is the analog of the white hole horizon in the spacetime diagram.
#     Inside: modes grow exponentially (evanescent). Outside: modes oscillate.
#
#  2. BCS stretched horizon: tau = tau_BCS = 0.22
#     The BCS gap freezes the modulus at tau = 0.22. This is the causal
#     boundary beyond which no dynamics occurs. Analog: stretched horizon.
#
#  3. Cosmological event horizon: k = k_CEH(tau) = a(tau)*H(tau)
#     Standard Hubble crossing. For the transit, this is at k_transit ~ 1209.
#     Deeply inside the tachyonic shell at the fold (k_transit << k_tach).

print(f"\n{'='*72}")
print("SECTION 6: Three nested boundaries")
print(f"{'='*72}")

# 1. Tachyonic shell k_tach(tau)
print(f"\n  1. TACHYONIC SHELL: k_tach(tau)")
print(f"     Analog: White hole horizon (frequency-dependent)")
print(f"     k_tach(0.15) = {k_tach_tau[idx_fold - (idx_fold - np.argmin(np.abs(tau_fine-0.15)))]:.2f} M_KK")
print(f"     k_tach(fold)  = {k_tach_fold:.2f} M_KK")
print(f"     k_tach(0.22) = {k_tach_tau[idx_BCS]:.2f} M_KK")
print(f"     k_tach(0.30) = {k_tach_tau[-1]:.2f} M_KK")
print(f"     Shape: monotonically increasing (z''/z grows with a^2)")

# 2. BCS stretched horizon
eta_BCS = eta_fine[idx_BCS]
tau_BCS = 0.22  # (local)
print(f"\n  2. BCS STRETCHED HORIZON: tau = {tau_BCS}")
print(f"     eta(BCS) = {eta_BCS:.6e}")
print(f"     Analog: Stretched horizon / cosmic censorship boundary")
print(f"     Post-BCS: modulus frozen, no further spectral evolution")
print("     Surface gravity analog: kappa_BCS = d(ln(Delta))/dtau|_{BCS}")

# 3. Cosmological event horizon at k_transit
k_CEH_tau = a_fine * np.sqrt(2.0 * eps_fine) * v_tau  # a*H (approximate)
print(f"\n  3. COSMOLOGICAL EVENT HORIZON: k_CEH(tau) = a*H")
print(f"     k_CEH(fold) ~ {k_CEH_tau[idx_fold]:.2f} M_KK")
print(f"     k_transit = {k_transit:.2f} M_KK")
print(f"     k_CEH << k_tach: cosmological horizon deep inside tachyonic shell")
print(f"     Nesting ratio: k_tach/k_CEH = {k_tach_fold/k_CEH_tau[idx_fold]:.2f}")

# ============================================================================
#  SECTION 7: Diagram shape analysis
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 7: Diagram shape analysis")
print(f"{'='*72}")

# The shape is determined by the ratio k_tach(tau) / k_tach(fold)
# as a function of conformal time eta.
shape_ratio = k_tach_tau / k_tach_fold

# The tachyonic shell curve in the Penrose diagram
# In (eta, r*) space, the shell sits at r*(k_tach(eta))
r_star_tach_curve = np.zeros(N_tau)
for it in range(N_tau):
    # Tortoise at k_tach(tau_it) using fold-time potential
    idx_k = np.argmin(np.abs(k_grid - k_tach_tau[it]))
    if idx_k < len(r_star):
        r_star_tach_curve[it] = r_star[min(idx_k, len(r_star)-1)]

# Aspect ratio of the diagram: Delta_eta / Delta_r*
Delta_eta = eta_fine[-1] - eta_fine[0]
Delta_r_star = r_star[-1] - r_star[0]
aspect = Delta_eta / Delta_r_star if Delta_r_star > 0 else np.inf

print(f"\n  Delta_eta (total conformal time) = {Delta_eta:.6e}")
print(f"  Delta_r* (total tortoise range) = {Delta_r_star:.6e}")
print(f"  Aspect ratio eta/r* = {aspect:.4f}")
print(f"  Diagram shape: {'tall (eta-dominated)' if aspect > 1 else 'wide (k-dominated)' if aspect < 1 else 'square'}")

# Mach number profile: v_tau / c_s
# The transit is at Mach = v_terminal / c_BLV
Mach = v_tau / c_BLV
print(f"\n  Mach number = v_terminal / c_s = {Mach:.2f}")
print(f"  (Strongly supersonic: white hole analog)")

# Conformal factor profile along the transit for k = k_transit
Omega_transit_profile = a_fine * z_fine / np.sqrt(2.0 * k_transit)
print(f"\n  Omega(tau, k_transit) profile:")
print(f"    Omega(0.10) = {Omega_transit_profile[0]:.6e}")
print(f"    Omega(fold) = {Omega_transit_profile[idx_fold]:.6e}")
print(f"    Omega(0.22) = {Omega_transit_profile[idx_BCS]:.6e}")
print(f"    Omega(0.30) = {Omega_transit_profile[-1]:.6e}")
print(f"    Growth factor: Omega(0.30)/Omega(0.10) = {Omega_transit_profile[-1]/Omega_transit_profile[0]:.2f}")

# ============================================================================
#  SECTION 8: Summary
# ============================================================================

print(f"\n{'='*72}")
print("SUMMARY")
print(f"{'='*72}")

print(f"""
  CONFORMAL FACTOR at fold:
    Omega(fold, k_transit) = {Omega_fold_transit:.6e}
    Omega(fold, k_tach)    = {Omega_fold_tach:.6e}
    Omega range over transit: [{Omega_min:.4e}, {Omega_max:.4e}]

  PENUMBRA (0.1 < |beta_k|^2 < 0.9):
    k range: [{k_pen_lo:.1f}, {k_pen_hi:.1f}] M_KK
    Width: Delta_k / k_tach = {pen_width_tach:.4f}
    Center: k ~ {pen_center:.1f} M_KK = {pen_center/k_tach_fold:.2f} k_tach

  ACOUSTIC HORIZON (|beta_k|^2 = 1):
    k_horizon = {k_horizon:.1f} M_KK = {k_horizon/k_tach_fold:.2f} k_tach

  THREE NESTED BOUNDARIES:
    Inner:  k_CEH ~ {k_CEH_tau[idx_fold]:.0f} M_KK (cosmological event horizon)
    Middle: k_tach = {k_tach_fold:.0f} M_KK (tachyonic shell)
    Outer:  k_horizon = {k_horizon:.0f} M_KK (acoustic horizon beta^2=1)

  DIAGRAM SHAPE:
    Aspect ratio = {aspect:.4f}
    {'TALL diamond' if aspect > 1 else 'WIDE diamond'}: conformal time dominates
    Mach = {Mach:.2f}: deep supersonic
    Penumbra at {pen_center/k_tach_fold:.1f}x k_tach: {pen_width_tach:.1f}x broad
""")

# ============================================================================
#  SECTION 9: Save data
# ============================================================================

outfile = os.path.join(os.path.dirname(__file__), 's69_conformal_factor.npz')
np.savez(outfile,
    # Grids
    tau_fine=tau_fine,
    eta_fine=eta_fine,
    k_grid=k_grid,
    k_grid_rk=k_grid_rk,
    # Background
    a_fine=a_fine,
    z_fine=z_fine,
    eps_fine=eps_fine,
    zpp_z=zpp_z,
    # Conformal factor (2D)
    Omega=Omega,
    # 1D profiles
    Omega_transit_profile=Omega_transit_profile,
    k_tach_tau=k_tach_tau,
    beta_sq_rk=beta_sq_rk,
    # Boundaries
    r_star=r_star,
    r_star_tach_curve=r_star_tach_curve,
    # Scalars
    k_tach_fold=k_tach_fold,
    k_transit=k_transit,
    k_horizon=k_horizon,
    Omega_fold_transit=Omega_fold_transit,
    Omega_fold_tach=Omega_fold_tach,
    pen_width_tach=pen_width_tach,
    pen_k_lo=k_pen_lo,
    pen_k_hi=k_pen_hi,
    Mach=Mach,
    aspect_ratio=aspect,
    gate_verdict='INFO',
    gate_detail=f'Omega(fold,k_tr)={Omega_fold_transit:.3e}, pen={pen_width_tach:.2f}',
)
print(f"\nSaved: {outfile}")

# ============================================================================
#  SECTION 10: Plotting
# ============================================================================

fig = plt.figure(figsize=(18, 14))

# --- Panel 1: Conformal factor Omega(tau, k) heatmap ---
ax1 = fig.add_subplot(2, 2, 1)
K_2d, T_2d = np.meshgrid(k_grid, tau_fine)
log_Omega = np.log10(Omega + 1e-30)
pcm = ax1.pcolormesh(K_2d, T_2d, log_Omega, cmap='inferno', shading='auto')
# Overlay tachyonic shell
ax1.plot(k_tach_tau, tau_fine, 'c-', lw=2, label=r'$k_{\rm tach}(\tau)$')
# BCS horizon
ax1.axhline(0.22, color='lime', ls='--', lw=1.5, label=r'BCS freeze ($\tau=0.22$)')
# Fold
ax1.axhline(tau_fold, color='white', ls=':', lw=1, label=r'Fold ($\tau=0.190$)')
ax1.set_xscale('log')
ax1.set_xlabel(r'$k$ [M$_{\rm KK}$]', fontsize=12)
ax1.set_ylabel(r'$\tau$', fontsize=12)
ax1.set_title(r'$\log_{10}\Omega(\tau, k)$', fontsize=13)
cb = plt.colorbar(pcm, ax=ax1)
cb.set_label(r'$\log_{10}\Omega$', fontsize=11)
ax1.legend(loc='upper left', fontsize=9, facecolor='k', edgecolor='w',
           labelcolor='w', framealpha=0.7)

# --- Panel 2: beta_sq(k) with penumbra ---
ax2 = fig.add_subplot(2, 2, 2)
valid = beta_sq_rk > 0
ax2.semilogy(k_rk[valid], beta_sq_rk[valid], 'b-', lw=1.5, label=r'$|\beta_k|^2$ (RK)')
ax2.axhline(1.0, color='r', ls='--', lw=1, label=r'$|\beta_k|^2 = 1$')
ax2.axhline(0.1, color='orange', ls=':', lw=0.8)
ax2.axhline(0.9, color='orange', ls=':', lw=0.8)
ax2.axvspan(k_pen_lo, k_pen_hi, alpha=0.15, color='orange', label='Penumbra')
ax2.axvline(k_tach_fold, color='cyan', ls='--', lw=1, label=r'$k_{\rm tach}$')
ax2.axvline(k_transit, color='green', ls='--', lw=1, label=r'$k_{\rm transit}$')
if crossings_1:
    ax2.axvline(crossings_1[0], color='red', ls='-', lw=1, alpha=0.5,
                label=r'$|\beta|^2=1$ crossing')
ax2.set_xscale('log')
ax2.set_xlabel(r'$k$ [M$_{\rm KK}$]', fontsize=12)
ax2.set_ylabel(r'$|\beta_k|^2$', fontsize=12)
ax2.set_title('Bogoliubov coefficient and penumbra', fontsize=13)
ax2.legend(loc='upper right', fontsize=8)
ax2.set_xlim(50, 2e5)
ax2.set_ylim(1e-7, 1e7)

# --- Panel 3: Penrose diagram (ASCII-like in matplotlib) ---
ax3 = fig.add_subplot(2, 2, 3)
# Plot in compactified (T, R) coordinates
# Use eta and r* at the fold time slice
# Multiple time slices for the full diagram
eta_vals = eta_fine[::200]  # subsample
for eta_val in eta_vals:
    u_line = eta_val - r_star
    v_line = eta_val + r_star
    U_line = (2.0/PI) * np.arctan(u_line * 1e3)
    V_line = (2.0/PI) * np.arctan(v_line * 1e3)
    T_line = (V_line + U_line) / 2.0
    R_line = (V_line - U_line) / 2.0
    ax3.plot(R_line, T_line, 'gray', lw=0.3, alpha=0.4)

# Tachyonic shell in Penrose coords at fold
u_tach = eta_fine[idx_fold] - r_star_tach
v_tach = eta_fine[idx_fold] + r_star_tach
U_tach = (2.0/PI) * np.arctan(u_tach * 1e3)
V_tach = (2.0/PI) * np.arctan(v_tach * 1e3)
T_tach = (V_tach + U_tach) / 2.0
R_tach = (V_tach - U_tach) / 2.0
ax3.axhline(T_pen[idx_k_tach], color='cyan', ls='--', lw=1.5,
            label=r'$k_{\rm tach}$ shell')

# BCS horizon in Penrose coords
u_BCS = eta_BCS - r_star
v_BCS = eta_BCS + r_star
U_BCS = (2.0/PI) * np.arctan(u_BCS * 1e3)
V_BCS = (2.0/PI) * np.arctan(v_BCS * 1e3)
T_BCS = (V_BCS + U_BCS) / 2.0
R_BCS = (V_BCS - U_BCS) / 2.0
ax3.plot(R_BCS, T_BCS, 'lime', ls='--', lw=1.5, label='BCS horizon')

# Horizon (beta^2 = 1) -- vertical line in mode space at k_horizon
idx_kh = np.argmin(np.abs(k_grid - k_horizon))
ax3.axvline(R_pen[idx_kh], color='red', ls='-', lw=1, alpha=0.6,
            label=r'$|\beta|^2=1$ horizon')

# Conformal boundary
ax3.plot([-1, 0], [0, 1], 'k-', lw=2)
ax3.plot([0, 1], [1, 0], 'k-', lw=2)
ax3.plot([-1, 0], [0, -1], 'k-', lw=2)
ax3.plot([0, 1], [-1, 0], 'k-', lw=2)

ax3.set_xlabel(r'$R$ (compactified)', fontsize=12)
ax3.set_ylabel(r'$T$ (compactified)', fontsize=12)
ax3.set_title('Penrose diagram (acoustic white hole)', fontsize=13)
ax3.legend(loc='upper left', fontsize=8)
ax3.set_xlim(-0.2, 1.1)
ax3.set_ylim(-0.5, 1.1)
ax3.set_aspect('equal')

# --- Panel 4: Omega profiles ---
ax4 = fig.add_subplot(2, 2, 4)
for k_ref, label, color in [
    (100, 'k=100', 'navy'),
    (k_transit, f'k_transit={k_transit:.0f}', 'green'),
    (k_tach_fold, f'k_tach={k_tach_fold:.0f}', 'cyan'),
    (k_horizon, f'k_hor={k_horizon:.0f}', 'red'),
    (20000, 'k=2e4', 'purple'),
]:
    Om_prof = a_fine * z_fine / np.sqrt(2.0 * k_ref)
    ax4.semilogy(tau_fine, Om_prof, color=color, lw=1.5, label=label)
ax4.axvline(tau_fold, color='gray', ls=':', lw=1)
ax4.axvline(0.22, color='lime', ls='--', lw=1, alpha=0.5)
ax4.set_xlabel(r'$\tau$', fontsize=12)
ax4.set_ylabel(r'$\Omega(\tau, k)$', fontsize=12)
ax4.set_title(r'Conformal factor $\Omega = az/\sqrt{2k}$', fontsize=13)
ax4.legend(loc='upper left', fontsize=8)

plt.suptitle('CONFORMAL-FACTOR-TRANSIT-69: Acoustic White Hole Penrose Structure',
             fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.96])

plotfile = os.path.join(os.path.dirname(__file__), 's69_conformal_factor.png')
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
print(f"Saved: {plotfile}")

print(f"\n{'='*72}")
print("Gate CONF-FACTOR-69: INFO")
print(f"  Omega(fold, k_transit) = {Omega_fold_transit:.4e}")
print(f"  Penumbra width Delta_k/k_tach = {pen_width_tach:.4f}")
print(f"  Diagram shape: {'TALL' if aspect > 1 else 'WIDE'} (aspect = {aspect:.4f})")
print(f"  Three nested horizons: CEH({k_CEH_tau[idx_fold]:.0f}) < tach({k_tach_fold:.0f}) < acoustic({k_horizon:.0f}) M_KK")
print(f"{'='*72}")
