#!/usr/bin/env python3
"""
PENROSE-SEQUENCE-70: 4-Panel Conformal Diagram Evolution Through Transit
========================================================================

Constructs the 4-panel conformal diagram showing the acoustic spacetime
evolution through the transit:
  (1) Pre-transit (tau > 0.25): subsonic, both null cones open, no horizon
  (2) Fold approach (tau ~ 0.20): v/c_s -> 1, null cones pinch, sonic horizon
  (3) Transit (tau = 0.19): v/c_s >> 1 (supersonic), acoustic white hole
  (4) Post-transit (tau < 0.15): v/c_s < 1, null cones re-open, GGE relic

Physics:
--------
The acoustic metric for phononic excitations in the condensate is:

    ds^2_acoustic = Omega^2 [-(c_s^2 - v^2) dt^2 - 2 v dt dx + dx^2]

where c_s is the sound speed and v is the flow velocity (= dtau/dt mapped
to the 1+1D acoustic spacetime). The null geodesics satisfy:

    dx/dt = -v +/- c_s

Panel 1: v < c_s  =>  both characteristics have positive slope in (t, x)
                      => all signals propagate forward => no horizon
Panel 2: v -> c_s =>  one characteristic becomes vertical => sonic point
Panel 3: v > c_s  =>  both characteristics point "inward" (toward past)
                      => acoustic white hole: no signals escape from past
Panel 4: v < c_s  =>  characteristics re-open => GGE relic propagates freely

The conformal compactification uses (U, V) where:
    U = t - x/(v + c_s),  V = t + x/(-v + c_s)
compactified via arctan.

Gate: PENROSE-SEQUENCE-70 -- INFO
Output: s70_penrose_sequence.npz, s70_penrose_sequence.png
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
from matplotlib.patches import FancyArrowPatch
from matplotlib.collections import LineCollection

from canonical_constants import (
    tau_fold, M_KK, v_terminal, PI, dt_transit,
    c_fabric, c_Gold, H_fold,
)

# ============================================================================
#  SECTION 1: Load transit background data
# ============================================================================

print("=" * 72)
print("PENROSE-SEQUENCE-70: 4-Panel Conformal Diagram Evolution")
print("=" * 72)

script_dir = os.path.dirname(os.path.abspath(__file__))

data_cf = np.load(os.path.join(script_dir, 's69_conformal_factor.npz'),
                  allow_pickle=True)
data_ps = np.load(os.path.join(script_dir, 's67_transit_ps.npz'),
                  allow_pickle=True)

tau_fine = data_ps['tau_fine']      # (8000,), range [0.10, 0.30]
eta_fine = data_ps['eta_fine']      # conformal time
a_fine   = data_ps['a_fine']        # scale factor
eps_fine = data_ps['eps_H_fine']    # slow-roll parameter
z_fine   = data_ps['z_fine']        # Mukhanov pump field

Mach_number = float(data_cf['Mach'])  # 54.73 at fold
pen_width   = float(data_cf['pen_width_tach'])  # 8.41 k_tach wide
k_tach_fold = float(data_cf['k_tach_fold'])

print(f"\nLoaded S67/S69 transit data:")
print(f"  tau range: [{tau_fine[0]:.2f}, {tau_fine[-1]:.2f}]")
print(f"  Mach at fold: {Mach_number:.2f}")
print(f"  Penumbra width: {pen_width:.2f} k_tach")
print(f"  k_tach(fold): {k_tach_fold:.2f} M_KK")

# ============================================================================
#  SECTION 2: Construct velocity and sound speed profiles
# ============================================================================
#
# The flow velocity v(tau) and sound speed c_s(tau) determine the acoustic
# causal structure. We model the transit as follows:
#
# The modulus velocity v_tau(tau) reaches v_terminal = 26.54 M_KK at the fold.
# The BLV sound speed c_s = 0.485 M_KK (from S69 conformal factor script).
#
# For the acoustic metric, the relevant velocity is the Mach number:
#   Ma(tau) = v_tau(tau) / c_s
#
# The velocity profile through the transit is driven by the spectral action
# gradient dS/dtau. We reconstruct it from the scale factor and conformal time.
#
# The key physics: v_tau increases as tau decreases toward the fold (0.19),
# reaches maximum at fold, then the BCS condensation decelerates it.

print(f"\n{'='*72}")
print("SECTION 2: Velocity and sound speed profiles")
print(f"{'='*72}")

c_s = 0.485  # BLV sound speed (M_KK units, from S69)  # (local)

# Reconstruct velocity profile from d(tau)/d(eta) using conformal time
# Since eta = integral dt/(v_tau * a), and v_tau = dtau/dt:
#   dtau/deta = v_tau^2 * a
#
# More directly: we model v(tau) as peaking at the fold with a profile
# determined by the spectral action gradient.
#
# From S38: the velocity profile is approximately
#   v(tau) = v_terminal * exp(-((tau - tau_fold)/sigma_v)^2)
# with sigma_v chosen so that v drops to c_s at tau_BCS = 0.22.

sigma_v = (0.22 - tau_fold) / np.sqrt(np.log(v_terminal / c_s))
print(f"  v_terminal = {v_terminal:.4f} M_KK")
print(f"  c_s = {c_s:.4f} M_KK")
print(f"  sigma_v = {sigma_v:.6f}")
print(f"  Ma(fold) = v_terminal/c_s = {v_terminal/c_s:.2f}")

# Full velocity profile
v_profile = v_terminal * np.exp(-((tau_fine - tau_fold) / sigma_v)**2)

# Mach number profile
Ma_profile = v_profile / c_s

# Find sonic point (Ma = 1) on each side of fold
idx_fold = np.argmin(np.abs(tau_fine - tau_fold))
# Post-fold (tau > tau_fold): sonic horizon
idx_post_fold = np.arange(idx_fold, len(tau_fine))
idx_sonic_post = idx_post_fold[np.argmin(np.abs(Ma_profile[idx_post_fold] - 1.0))]
tau_sonic_post = tau_fine[idx_sonic_post]

# Pre-fold (tau < tau_fold): sonic horizon
idx_pre_fold = np.arange(0, idx_fold)
idx_sonic_pre = idx_pre_fold[np.argmin(np.abs(Ma_profile[idx_pre_fold] - 1.0))]
tau_sonic_pre = tau_fine[idx_sonic_pre]

print(f"\n  Sonic horizon (post-fold): tau = {tau_sonic_post:.4f}")
print(f"  Sonic horizon (pre-fold): tau = {tau_sonic_pre:.4f}")
print(f"  Ma(fold) = {Ma_profile[idx_fold]:.2f}")
print(f"  Ma(tau=0.25) = {Ma_profile[np.argmin(np.abs(tau_fine - 0.25))]:.4f}")
print(f"  Ma(tau=0.15) = {Ma_profile[np.argmin(np.abs(tau_fine - 0.15))]:.4f}")

# ============================================================================
#  SECTION 3: Compute null geodesics for each panel
# ============================================================================
#
# The 1+1D acoustic metric is:
#   ds^2 = -(c_s^2 - v^2) dt^2 - 2v dt dx + dx^2
#
# Null geodesics: ds^2 = 0 => dx/dt = -v +/- c_s
#   Right-moving: dx/dt = -v + c_s  (= c_s - v for our sign convention)
#   Left-moving:  dx/dt = -v - c_s  (= -(v + c_s))
#
# In the acoustic spacetime:
#   - v < c_s: right-mover has positive slope, left-mover negative => normal
#   - v = c_s: right-mover slope = 0 => sonic horizon
#   - v > c_s: right-mover slope negative => both go "backward" => white hole

print(f"\n{'='*72}")
print("SECTION 3: Null geodesics for 4 panels")
print(f"{'='*72}")

# Define 4 representative tau values for the panels
# Panel 2 must be at the actual sonic point (Ma ~ 1) to show the horizon
# forming. The Gaussian velocity profile drops very steeply, so tau=0.205
# is already Ma >> 1. Use the computed sonic horizon location instead.
panel_taus = {
    'pre-transit': 0.25,                   # Well subsonic
    'fold-approach': tau_sonic_post + 0.001,  # Just outside sonic point (Ma ~ 1)
    'transit': tau_fold,                    # Supersonic Ma >> 1
    'post-transit': 0.15,                  # Subsonic again
}

# For each panel, compute the null cone structure
null_data = {}
for label, tau_panel in panel_taus.items():
    idx = np.argmin(np.abs(tau_fine - tau_panel))
    v_local = v_profile[idx]
    Ma_local = v_local / c_s

    # Null ray slopes
    slope_right = c_s - v_local   # -v + c_s
    slope_left = -(v_local + c_s)  # -v - c_s

    null_data[label] = {
        'tau': tau_fine[idx],
        'v': v_local,
        'Ma': Ma_local,
        'slope_right': slope_right,
        'slope_left': slope_left,
    }

    print(f"\n  Panel: {label}")
    print(f"    tau = {tau_fine[idx]:.4f}")
    print(f"    v = {v_local:.4f} M_KK, c_s = {c_s:.4f} M_KK")
    print(f"    Ma = {Ma_local:.4f}")
    print(f"    Right-mover slope: dx/dt = {slope_right:.4f}")
    print(f"    Left-mover slope:  dx/dt = {slope_left:.4f}")
    if Ma_local < 1:
        print(f"    Status: SUBSONIC — both cones open")
    elif abs(Ma_local - 1.0) < 0.1:
        print(f"    Status: NEAR-SONIC — null cone pinching")
    else:
        print(f"    Status: SUPERSONIC — acoustic white hole")

# ============================================================================
#  SECTION 4: Construct conformal (Penrose) coordinates for each panel
# ============================================================================
#
# For each panel, we construct the Penrose diagram by:
# 1. Defining a (t, x) grid
# 2. Computing null coordinates U = t - x/(v + c_s), V = t + x/(-v + c_s)
#    (or more carefully, integrating along the characteristics)
# 3. Compactifying with arctan
#
# For a UNIFORM flow (constant v, c_s), the null coordinates are:
#   U = t - x/c_+  where c_+ = v + c_s (ingoing speed in lab frame)
#   V = t - x/c_-  where c_- = v - c_s (outgoing speed in lab frame)
#
# The Penrose compactification is:
#   U_hat = (2/pi) arctan(U)
#   V_hat = (2/pi) arctan(V)
#
# Note: for the white hole case (v > c_s), both c_+ and c_- are positive,
# meaning both characteristics have the same sign slope. This is the
# defining feature of the acoustic white hole.

print(f"\n{'='*72}")
print("SECTION 4: Conformal coordinates for Penrose diagrams")
print(f"{'='*72}")

# Grid for null geodesic integration
N_rays = 15       # Number of null rays per family
N_pts = 200       # Points per ray

# Time range (in M_KK^{-1} units)
t_range = 0.01    # ~10x transit duration  # (local)

penrose_panels = {}

for label, nd in null_data.items():
    v_local = nd['v']
    Ma = nd['Ma']

    # Characteristic speeds in lab frame
    c_plus = v_local + c_s    # Always positive (ingoing)
    c_minus = v_local - c_s   # Negative if subsonic, positive if supersonic

    # Null geodesic families:
    # Family 1 (right-moving in comoving frame): dx/dt = c_minus (= v - c_s)
    # Family 2 (left-moving in comoving frame):  dx/dt = -c_plus (= -(v + c_s))

    # For Penrose coordinates, define:
    #   xi_+ = x - c_minus * t  (constant along right-movers)
    #   xi_- = x + c_plus * t   (constant along left-movers)
    #
    # Then null coordinates:
    #   U = (x - c_minus * t)  => right-moving characteristic label
    #   V = (x + c_plus * t)   => left-moving characteristic label

    # Generate null rays starting from t = 0 at different x positions
    x_starts = np.linspace(-0.005, 0.005, N_rays)
    t_array = np.linspace(-t_range/2, t_range/2, N_pts)

    # Right-movers: x = x_0 + c_minus * t
    rays_right_x = np.zeros((N_rays, N_pts))
    rays_right_t = np.tile(t_array, (N_rays, 1))
    for i, x0 in enumerate(x_starts):
        rays_right_x[i, :] = x0 + c_minus * t_array

    # Left-movers: x = x_0 - c_plus * t
    rays_left_x = np.zeros((N_rays, N_pts))
    rays_left_t = np.tile(t_array, (N_rays, 1))
    for i, x0 in enumerate(x_starts):
        rays_left_x[i, :] = x0 - c_plus * t_array

    # Penrose compactification
    # Use null coordinates: U = x - c_minus * t, V = x + c_plus * t
    # Compact: U_hat = (2/pi) arctan(alpha * U), similarly for V
    # Choose alpha to spread the diagram nicely
    alpha = 200.0  # Scaling factor for compactification (local)

    def compact(u):
        return (2.0 / PI) * np.arctan(alpha * u)

    # For right-movers: U = const, V varies
    # U = x - c_minus * t = x_0 (constant for each ray)
    # V = x + c_plus * t = x_0 + (c_minus + c_plus) * t = x_0 + 2*c_s_eff * t
    #   where c_s_eff depends on the Mach number

    # For left-movers: V = const, U varies
    # V = x + c_plus * t = x_0 (constant for each ray)
    # U = x - c_minus * t = x_0 - (c_minus + c_plus) * t

    # Transform all rays to (U_hat, V_hat) Penrose coordinates
    penrose_right_U = np.zeros_like(rays_right_x)
    penrose_right_V = np.zeros_like(rays_right_x)
    penrose_left_U = np.zeros_like(rays_left_x)
    penrose_left_V = np.zeros_like(rays_left_x)

    for i in range(N_rays):
        for j in range(N_pts):
            x_r = rays_right_x[i, j]
            t_r = rays_right_t[i, j]
            U_r = x_r - c_minus * t_r
            V_r = x_r + c_plus * t_r
            penrose_right_U[i, j] = compact(U_r)
            penrose_right_V[i, j] = compact(V_r)

            x_l = rays_left_x[i, j]
            t_l = rays_left_t[i, j]
            U_l = x_l - c_minus * t_l
            V_l = x_l + c_plus * t_l
            penrose_left_U[i, j] = compact(U_l)
            penrose_left_V[i, j] = compact(V_l)

    # Standard Penrose plot uses T_hat = (V_hat + U_hat)/2, X_hat = (V_hat - U_hat)/2
    penrose_right_T = (penrose_right_V + penrose_right_U) / 2
    penrose_right_X = (penrose_right_V - penrose_right_U) / 2

    penrose_left_T = (penrose_left_V + penrose_left_U) / 2
    penrose_left_X = (penrose_left_V - penrose_left_U) / 2

    penrose_panels[label] = {
        'right_T': penrose_right_T,
        'right_X': penrose_right_X,
        'left_T': penrose_left_T,
        'left_X': penrose_left_X,
        'c_plus': c_plus,
        'c_minus': c_minus,
        'Ma': Ma,
        'v': v_local,
    }

    print(f"\n  Panel: {label}")
    print(f"    c_+ = {c_plus:.4f}, c_- = {c_minus:.4f}")
    print(f"    c_-/c_+ = {c_minus/c_plus:.4f}")
    if c_minus < 0:
        print(f"    SUBSONIC: right-movers escape (slope > 0)")
    elif abs(c_minus) < 0.01:
        print(f"    SONIC: right-movers frozen (slope ~ 0)")
    else:
        print(f"    SUPERSONIC: right-movers dragged inward (slope < 0 in comoving)")

# ============================================================================
#  SECTION 5: Compute the full Mach profile and horizon location
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 5: Mach profile and horizon structure")
print(f"{'='*72}")

# The acoustic horizon is at Ma = 1. On a Penrose diagram this appears as
# the surface where the right-moving null cone becomes degenerate.

idx_025 = np.argmin(np.abs(tau_fine - 0.25))
idx_020 = np.argmin(np.abs(tau_fine - 0.20))
idx_015 = np.argmin(np.abs(tau_fine - 0.15))

print(f"\n  Mach profile at key points:")
print(f"    Ma(0.25) = {Ma_profile[idx_025]:.6f}")
print(f"    Ma(0.22) = {Ma_profile[np.argmin(np.abs(tau_fine - 0.22))]:.6f}")
print(f"    Ma(sonic_post) = {Ma_profile[idx_sonic_post]:.6f} at tau = {tau_sonic_post:.4f}")
print(f"    Ma(fold) = {Ma_profile[idx_fold]:.2f} at tau = {tau_fold}")
print(f"    Ma(sonic_pre) = {Ma_profile[idx_sonic_pre]:.6f} at tau = {tau_sonic_pre:.4f}")
print(f"    Ma(0.15) = {Ma_profile[idx_015]:.6f}")

# Supersonic region width
supersonic_mask = Ma_profile > 1.0
if np.any(supersonic_mask):
    tau_sup = tau_fine[supersonic_mask]
    tau_sup_lo = tau_sup.min()
    tau_sup_hi = tau_sup.max()
    print(f"\n  Supersonic region: tau in [{tau_sup_lo:.4f}, {tau_sup_hi:.4f}]")
    print(f"  Width: Delta_tau = {tau_sup_hi - tau_sup_lo:.4f}")
    print(f"  Transit duration: dt = {dt_transit:.6f} M_KK^{{-1}}")
else:
    print(f"  WARNING: No supersonic region found!")

# ============================================================================
#  SECTION 6: Construct the 4-panel Penrose diagram figure
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 6: Constructing 4-panel Penrose diagram")
print(f"{'='*72}")

fig, axes = plt.subplots(2, 2, figsize=(14, 14))
fig.suptitle('Acoustic Penrose Diagram Evolution Through Transit\n'
             'Phonon-Exflation Framework: Acoustic White Hole Causal Structure',
             fontsize=13, fontweight='bold', y=0.98)

panel_order = ['pre-transit', 'fold-approach', 'transit', 'post-transit']
panel_titles = [
    r'Panel 1: Pre-Transit ($\tau=0.25$, Ma={:.4f})'.format(null_data['pre-transit']['Ma']),
    r'Panel 2: Sonic Horizon ($\tau={:.3f}$, Ma={:.2f})'.format(
        null_data['fold-approach']['tau'], null_data['fold-approach']['Ma']),
    r'Panel 3: Transit ($\tau=0.190$, Ma={:.1f})'.format(null_data['transit']['Ma']),
    r'Panel 4: Post-Transit ($\tau=0.15$, Ma={:.4f})'.format(null_data['post-transit']['Ma']),
]
panel_status = [
    'SUBSONIC\nBoth null cones open\nNo horizon',
    'SONIC POINT\nNull cones pinching\nHorizon forming (Ma~1)',
    'SUPERSONIC (Ma=54.7)\nAcoustic white hole\nNo signals escape past',
    'SUBSONIC\nNull cones re-open\nGGE relic propagates',
]

colors_right = '#2166AC'   # Blue for right-movers
colors_left = '#B2182B'    # Red for left-movers
color_horizon = '#4DAF4A'  # Green for horizon
color_boundary = '#333333'

for ipanel, (label, title, status) in enumerate(zip(panel_order, panel_titles, panel_status)):
    ax = axes[ipanel // 2][ipanel % 2]
    pd = penrose_panels[label]

    # Draw the conformal diamond boundary
    # The diamond is bounded by U_hat = +/-1 and V_hat = +/-1
    # In (T, X) coordinates: T + X <= 1, T - X <= 1, T + X >= -1, T - X >= -1
    diamond_x = [0, 1, 0, -1, 0]
    diamond_t = [-1, 0, 1, 0, -1]
    ax.plot(diamond_x, diamond_t, '-', color=color_boundary, linewidth=2.0, zorder=5)

    # Fill diamond with very light gray
    ax.fill(diamond_x, diamond_t, color='#F7F7F7', zorder=0)

    # Draw null geodesics
    # Right-movers (blue): constant U, varying V
    for i in range(N_rays):
        ax.plot(pd['right_X'][i], pd['right_T'][i], '-',
                color=colors_right, alpha=0.6, linewidth=0.8, zorder=2)

    # Left-movers (red): constant V, varying U
    for i in range(N_rays):
        ax.plot(pd['left_X'][i], pd['left_T'][i], '-',
                color=colors_left, alpha=0.6, linewidth=0.8, zorder=2)

    # Draw representative null cones at the center
    # Null cone at origin: rays going from (0, 0) to (+/- slopes)
    v_loc = pd['v']
    cone_len = 0.25  # (local)

    # In the compactified diagram, the null cone at a point has opening angle
    # determined by the ratio of characteristic speeds.
    # Right-mover: direction (1, c_minus/(c_minus + c_plus))  in (T, X)
    # Left-mover:  direction (1, -c_plus/(c_minus + c_plus))

    c_p = pd['c_plus']
    c_m = pd['c_minus']

    # Angular directions of null rays in the Penrose (T, X) plane
    # For uniform flow: the Penrose diagram maps null rays to straight lines
    # that make angle theta with vertical, where:
    #   Right: tan(theta_R) = (c_m) / (c_m + c_p)  ... but in (X, T) coords
    #   We need to be careful about the compactification.
    #
    # In the raw (U, V) coordinates:
    #   Right-mover: V changes, U = const => dU=0 => dT = dV/2, dX = dV/2
    #     => dX/dT = +1 (always 45 degrees in Penrose diagram!)
    #   Left-mover: U changes, V = const => dV=0 => dT = dU/2, dX = -dU/2
    #     => dX/dT = -1 (always -45 degrees in Penrose diagram!)
    #
    # This is correct for uniform-speed flows where U, V are proper null coords.
    # But the PHYSICAL content is in how the null coordinates RELATE to the
    # physical (t, x) coordinates. In particular, the BOUNDARIES of the
    # Penrose diamond change character depending on Ma:
    #   - Subsonic: all four boundaries are "infinity" (normal causal diamond)
    #   - Supersonic: the "past" boundary becomes a white hole horizon

    # Draw null cone at center (always 45 degrees in Penrose coords)
    # But color/style indicates the physical meaning
    cone_x_r = [0, cone_len]
    cone_t_r = [0, cone_len]
    cone_x_l = [0, -cone_len]
    cone_t_l = [0, cone_len]

    ax.plot(cone_x_r, cone_t_r, '-', color=colors_right, linewidth=2.5, zorder=4)
    ax.plot(cone_x_l, cone_t_l, '-', color=colors_left, linewidth=2.5, zorder=4)
    ax.plot([0], [0], 'o', color='black', markersize=4, zorder=5)

    # Now draw the PHYSICAL null cone to show how the acoustic light cone
    # changes with Mach number. This is the key visual.
    # In physical (t, x) space:
    #   Right: dx/dt = c_s - v (positive if subsonic, negative if supersonic)
    #   Left:  dx/dt = -(c_s + v) (always negative)
    #
    # We draw this as an inset or as arrows at the center
    # Normalize to show the cone opening angle

    if abs(c_m) > 1e-10:
        angle_right = np.arctan2(c_m, 1.0)  # angle from t-axis for right-mover
    else:
        angle_right = 0.0  # (local)
    angle_left = np.arctan2(-c_p, 1.0)    # angle from t-axis for left-mover

    # Draw physical null cone arrows from center
    arrow_len = 0.18  # (local)
    # Right-mover arrow (in physical t, x)
    dx_r = arrow_len * np.sin(angle_right)
    dt_r = arrow_len * np.cos(angle_right)
    # Left-mover arrow
    dx_l = arrow_len * np.sin(angle_left)
    dt_l = arrow_len * np.cos(angle_left)

    # Place at offset from center to avoid overlap with Penrose null lines
    cx, cy = 0.0, -0.35
    ax.annotate('', xy=(cx + dx_r, cy + dt_r), xytext=(cx, cy),
                arrowprops=dict(arrowstyle='->', color=colors_right,
                                lw=2.5, mutation_scale=15),  # (local)
                zorder=6)
    ax.annotate('', xy=(cx + dx_l, cy + dt_l), xytext=(cx, cy),
                arrowprops=dict(arrowstyle='->', color=colors_left,
                                lw=2.5, mutation_scale=15),  # (local)
                zorder=6)
    ax.plot([cx], [cy], 's', color='black', markersize=5, zorder=6)

    # Draw the physical null cone envelope
    # Filled wedge showing the acoustic causal future
    n_wedge = 50
    if c_m > 0:
        # Subsonic: cone opens between angle_left and angle_right
        wedge_angles = np.linspace(angle_left, angle_right, n_wedge)
    elif c_m < 0:
        # Supersonic: both characteristics on same side
        # Physical cone is "inverted" — causal future is BEHIND
        wedge_angles = np.linspace(angle_left, angle_right, n_wedge)
    else:
        # Sonic: degenerate
        wedge_angles = np.linspace(angle_left, 0, n_wedge)

    wedge_x = cx + arrow_len * np.sin(wedge_angles)
    wedge_t = cy + arrow_len * np.cos(wedge_angles)
    wedge_poly_x = np.concatenate([[cx], wedge_x, [cx]])
    wedge_poly_t = np.concatenate([[cy], wedge_t, [cy]])

    if c_m >= 0:
        ax.fill(wedge_poly_x, wedge_poly_t, alpha=0.15, color='#FFD700', zorder=3)
    else:
        # Supersonic: shade differently to indicate white hole
        ax.fill(wedge_poly_x, wedge_poly_t, alpha=0.2, color='#FF4500', zorder=3)

    # Horizon indicator for supersonic case
    if pd['Ma'] > 1.0:
        # Draw the sonic horizon as a thick line at the past boundary
        horizon_x = np.array([-0.6, 0.6])
        horizon_t = np.array([-0.4, -0.4])
        ax.plot(horizon_x, horizon_t, '--', color=color_horizon,
                linewidth=2.5, zorder=4, label='Sonic horizon')
        ax.text(0.0, -0.50, 'SONIC HORIZON', fontsize=8, ha='center',
                color=color_horizon, fontweight='bold', zorder=6)

        # The white hole: shade the region below the horizon
        wh_x = [-0.6, 0.6, 0, -0.6]
        wh_t = [-0.4, -0.4, -1, -0.4]
        ax.fill(wh_x, wh_t, alpha=0.1, color=color_horizon, zorder=1)
        ax.text(0.0, -0.72, 'WHITE HOLE', fontsize=7, ha='center',
                color=color_horizon, style='italic', zorder=6)

    # Near-sonic indicator (for panel 2 at sonic point)
    if 0.5 < pd['Ma'] < 3.0 and label == 'fold-approach':
        ax.text(0.0, -0.50, 'FORMING HORIZON', fontsize=7, ha='center',
                color='#FF8C00', fontweight='bold', zorder=6)

    # Labels for conformal boundaries
    ax.text(0.55, 0.55, r'$\mathscr{I}^+$', fontsize=10, ha='center',
            color=color_boundary, zorder=6, style='italic')
    ax.text(-0.55, 0.55, r'$\mathscr{I}^+$', fontsize=10, ha='center',
            color=color_boundary, zorder=6, style='italic')
    ax.text(0.55, -0.55, r'$\mathscr{I}^-$', fontsize=10, ha='center',
            color=color_boundary, zorder=6, style='italic')
    ax.text(-0.55, -0.55, r'$\mathscr{I}^-$', fontsize=10, ha='center',
            color=color_boundary, zorder=6, style='italic')
    ax.text(0.0, 0.92, r'$i^+$', fontsize=10, ha='center',
            color=color_boundary, fontweight='bold', zorder=6)
    ax.text(0.0, -0.97, r'$i^-$', fontsize=10, ha='center',
            color=color_boundary, fontweight='bold', zorder=6)
    ax.text(0.85, 0.0, r'$i^0$', fontsize=10, ha='center',
            color=color_boundary, fontweight='bold', zorder=6)
    ax.text(-0.85, 0.0, r'$i^0$', fontsize=10, ha='center',
            color=color_boundary, fontweight='bold', zorder=6)

    # Title and status
    ax.set_title(title, fontsize=10, fontweight='bold', pad=10)
    ax.text(0.98, 0.02, status, fontsize=7, ha='right', va='bottom',
            transform=ax.transAxes, bbox=dict(boxstyle='round,pad=0.3',
            facecolor='white', edgecolor='gray', alpha=0.9),
            fontfamily='monospace')

    # Physical null cone label
    ax.text(cx, cy - 0.14, 'Physical null cone', fontsize=7,
            ha='center', color='gray')

    # Axes formatting
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.15, 1.15)
    ax.set_xlabel(r'$\hat{X}$ (compactified spatial)', fontsize=9)
    ax.set_ylabel(r'$\hat{T}$ (compactified temporal)', fontsize=9)
    ax.set_aspect('equal')
    ax.grid(False)

    # Remove ticks for cleaner look
    ax.set_xticks([])
    ax.set_yticks([])

# Add legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=colors_right, linewidth=2, label='Right-movers (outgoing)'),
    Line2D([0], [0], color=colors_left, linewidth=2, label='Left-movers (ingoing)'),
    Line2D([0], [0], color=color_horizon, linewidth=2, linestyle='--', label='Sonic horizon'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=3,
           fontsize=9, frameon=True, fancybox=True, shadow=True,
           bbox_to_anchor=(0.5, 0.01))

plt.tight_layout(rect=[0, 0.04, 1, 0.96])

output_png = os.path.join(script_dir, 's70_penrose_sequence.png')
fig.savefig(output_png, dpi=200, bbox_inches='tight', facecolor='white')
print(f"\n  Saved figure: {output_png}")
plt.close()

# ============================================================================
#  SECTION 7: Summary data and Mach profile plot (inset)
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 7: Mach profile summary")
print(f"{'='*72}")

# Create supplementary Mach profile plot
fig2, ax2 = plt.subplots(1, 1, figsize=(10, 5))
ax2.semilogy(tau_fine, Ma_profile, 'k-', linewidth=2, label=r'Ma($\tau$)')
ax2.axhline(y=1.0, color=color_horizon, linestyle='--', linewidth=1.5, label='Ma = 1 (sonic)')
ax2.axvline(x=tau_fold, color='gray', linestyle=':', linewidth=1, alpha=0.5)
ax2.axvline(x=0.22, color='gray', linestyle=':', linewidth=1, alpha=0.5)

# Mark panel locations
for label, tau_panel in panel_taus.items():
    idx = np.argmin(np.abs(tau_fine - tau_panel))
    ax2.plot(tau_panel, Ma_profile[idx], 'o', markersize=10, zorder=5,
             label=f'{label} (Ma={Ma_profile[idx]:.2f})')

# Mark sonic points
ax2.plot(tau_sonic_pre, 1.0, 'v', color=color_horizon, markersize=12,
         zorder=5, label=f'Sonic pre-fold ({tau_sonic_pre:.3f})')
ax2.plot(tau_sonic_post, 1.0, '^', color=color_horizon, markersize=12,
         zorder=5, label=f'Sonic post-fold ({tau_sonic_post:.3f})')

# Fill supersonic region
ax2.fill_between(tau_fine, 1.0, Ma_profile,
                 where=Ma_profile > 1.0,
                 alpha=0.15, color='red', label='Supersonic region')  # (local)

ax2.set_xlabel(r'$\tau$ (Jensen deformation)', fontsize=12)
ax2.set_ylabel(r'Mach number Ma = $v/c_s$', fontsize=12)
ax2.set_title('Acoustic Mach Number Through Transit\n'
              'Sonic Horizon Structure of the Acoustic White Hole', fontsize=12)
ax2.legend(fontsize=8, loc='upper right', ncol=2)
ax2.set_xlim(0.10, 0.30)
ax2.set_ylim(0.001, 200)
ax2.grid(True, alpha=0.3)

# Annotations
ax2.annotate(r'$\tau_{\rm fold} = 0.190$', xy=(tau_fold, Ma_profile[idx_fold]),
             xytext=(tau_fold + 0.02, Ma_profile[idx_fold] * 1.5),
             fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'))
ax2.annotate('BCS freeze\n' r'$\tau = 0.22$', xy=(0.22, 1.0),
             xytext=(0.24, 3.0), fontsize=9,
             arrowprops=dict(arrowstyle='->', color='gray'))

output_mach_png = os.path.join(script_dir, 's70_penrose_sequence_mach.png')
fig2.savefig(output_mach_png, dpi=200, bbox_inches='tight', facecolor='white')
print(f"  Saved Mach profile: {output_mach_png}")
plt.close()

# ============================================================================
#  SECTION 8: Save all computed data
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 8: Saving results")
print(f"{'='*72}")

# Collect panel data for saving
panel_tau_arr = np.array([null_data[l]['tau'] for l in panel_order])
panel_v_arr = np.array([null_data[l]['v'] for l in panel_order])
panel_Ma_arr = np.array([null_data[l]['Ma'] for l in panel_order])
panel_slope_right = np.array([null_data[l]['slope_right'] for l in panel_order])
panel_slope_left = np.array([null_data[l]['slope_left'] for l in panel_order])

output_npz = os.path.join(script_dir, 's70_penrose_sequence.npz')
np.savez(output_npz,
    # Panel data
    panel_labels=np.array(panel_order),
    panel_tau=panel_tau_arr,
    panel_v=panel_v_arr,
    panel_Ma=panel_Ma_arr,
    panel_slope_right=panel_slope_right,
    panel_slope_left=panel_slope_left,
    # Mach profile
    tau_fine=tau_fine,
    Ma_profile=Ma_profile,
    v_profile=v_profile,
    c_s=np.array(c_s),
    # Sonic horizons
    tau_sonic_pre=np.array(tau_sonic_pre),
    tau_sonic_post=np.array(tau_sonic_post),
    # Supersonic region
    tau_supersonic_lo=np.array(tau_sup_lo if np.any(supersonic_mask) else np.nan),
    tau_supersonic_hi=np.array(tau_sup_hi if np.any(supersonic_mask) else np.nan),
    # Key numbers
    Mach_fold=np.array(Ma_profile[idx_fold]),
    sigma_v=np.array(sigma_v),
    pen_width_tach=np.array(pen_width),
    k_tach_fold=np.array(k_tach_fold),
    # Gate
    gate_verdict=np.array('INFO'),
    gate_detail=np.array(
        f'4-panel conformal diagram. Ma(fold)={Ma_profile[idx_fold]:.1f}, '
        f'sonic at tau=[{tau_sonic_pre:.3f},{tau_sonic_post:.3f}]'
    ),
)
print(f"  Saved data: {output_npz}")

# ============================================================================
#  SECTION 9: Gate verdict
# ============================================================================

print(f"\n{'='*72}")
print("GATE VERDICT: PENROSE-SEQUENCE-70")
print(f"{'='*72}")
print(f"  Gate type: INFO")
print(f"  4-panel conformal diagram with causal structure classified")
print(f"")
print(f"  Panel 1 (pre-transit, tau=0.25):")
print(f"    Ma = {null_data['pre-transit']['Ma']:.4f} << 1")
print(f"    Both null cones open. Standard acoustic causal diamond.")
print(f"    Right-mover slope: {null_data['pre-transit']['slope_right']:.4f} M_KK")
print(f"    Left-mover slope: {null_data['pre-transit']['slope_left']:.4f} M_KK")
print(f"")
print(f"  Panel 2 (fold approach, tau=0.205):")
print(f"    Ma = {null_data['fold-approach']['Ma']:.4f}")
print(f"    Null cones pinching. Sonic horizon forming.")
print(f"    Right-mover slope: {null_data['fold-approach']['slope_right']:.4f} M_KK")
print(f"    Left-mover slope: {null_data['fold-approach']['slope_left']:.4f} M_KK")
print(f"")
print(f"  Panel 3 (transit, tau=0.19):")
print(f"    Ma = {null_data['transit']['Ma']:.2f} >> 1")
print(f"    Acoustic white hole. Both characteristics dragged inward.")
print(f"    Right-mover slope: {null_data['transit']['slope_right']:.4f} M_KK")
print(f"    Left-mover slope: {null_data['transit']['slope_left']:.4f} M_KK")
print(f"")
print(f"  Panel 4 (post-transit, tau=0.15):")
print(f"    Ma = {null_data['post-transit']['Ma']:.4f} << 1")
print(f"    Null cones re-open. GGE relic propagates freely.")
print(f"    Right-mover slope: {null_data['post-transit']['slope_right']:.4f} M_KK")
print(f"    Left-mover slope: {null_data['post-transit']['slope_left']:.4f} M_KK")
print(f"")
print(f"  Sonic horizon locations:")
print(f"    Pre-fold: tau = {tau_sonic_pre:.4f}")
print(f"    Post-fold: tau = {tau_sonic_post:.4f}")
print(f"    Supersonic region: [{tau_sup_lo:.4f}, {tau_sup_hi:.4f}]")
print(f"    Width: Delta_tau = {tau_sup_hi - tau_sup_lo:.4f}")
print(f"")
print(f"  Acoustic causal structure evolution:")
print(f"    tau > {tau_sonic_post:.3f}: SUBSONIC (normal)")
print(f"    tau = {tau_sonic_post:.3f}: Sonic horizon forms")
print(f"    {tau_sonic_pre:.3f} < tau < {tau_sonic_post:.3f}: SUPERSONIC (white hole)")
print(f"    tau = {tau_sonic_pre:.3f}: Sonic horizon closes")
print(f"    tau < {tau_sonic_pre:.3f}: SUBSONIC (GGE relic epoch)")
print(f"")
print(f"  Key invariant: the acoustic white hole is a TRANSIENT structure.")
print(f"  It exists only during the supersonic transit. Before and after,")
print(f"  the acoustic spacetime has standard causal structure.")
print(f"  This is the fundamental asymmetry that breaks time-reversal")
print(f"  in the acoustic sector -- the GGE relic carries the imprint.")
print(f"\n{'='*72}")
print("PENROSE-SEQUENCE-70: COMPLETE")
print(f"{'='*72}")
