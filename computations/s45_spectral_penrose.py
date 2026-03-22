#!/usr/bin/env python3
"""
SPECTRAL-PENROSE-45: Spectral Penrose Diagram in the (tau, lambda_k) plane.

Constructs the "spectral Penrose diagram" proposed in the S44 Connes-SP
workshop: a conformal diagram of eigenvalue flow in modulus space, colored
by Bogoliubov occupation number n_k. This is NOT a spacetime Penrose diagram
(tau is a scalar field value, not a coordinate). It is a spectral-geometric
object that makes the causal/topological structure of the Dirac spectrum
visible in a single figure.

Key features displayed:
  1. Eigenvalue trajectories lambda_k(tau) for sectors (0,0) and (1,0)
  2. Van Hove singularity tracks (band edges where d lambda/d tau -> 0 or
     DOS diverges)
  3. BCS gap boundary -- physical Bogoliubov gap from s29b, showing the
     paired region as an "acoustic horizon" in modulus space
  4. Particle creation intensity n_k(tau) colored by proximity to the fold
  5. DNP crossing, NEC boundary, dump point markers
  6. Conformal boundary annotations (tau=0 round metric, tau->inf Kasner)

The analogy to a spacetime Penrose diagram:
  - tau plays the role of "conformal time" in the spectral geometry
  - lambda_k eigenvalues are the "radial null coordinates"
  - Van Hove singularities (DOS divergences) = conjugate points / caustics
  - BCS gap = acoustic horizon (T_a/T_Gibbs = 0.993)
  - Fold/dump = extremal horizon (T_H = 0, kappa = 0, BPS saturation)
  - T3-T5 near-crossing = Cauchy horizon instability precursor

Input data:
  - s41_spectral_refinement.npz (tau grid, spectral range, gap statistics)
  - s44_vanhove_track.npz (12 van Hove trajectories, VH singularities)
  - s42_hauser_feshbach.npz (BCS gap, compound nucleus T, sector branching)
  - s35_sector_10_spectrum.npz (eigenvalue tracks for sectors (0,0), (1,0))

Output:
  - s45_spectral_penrose.png
  - s45_spectral_penrose.npz

Author: schwarzschild-penrose-geometer
Session: 45
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
import matplotlib.colors as mcolors
from scipy.interpolate import interp1d


# ===========================================================================
# 0. Load all data
# ===========================================================================
print("Loading data files...")

d_s41 = np.load('s41_spectral_refinement.npz', allow_pickle=True)
d_vh  = np.load('s44_vanhove_track.npz', allow_pickle=True)
d_hf  = np.load('s42_hauser_feshbach.npz', allow_pickle=True)
d_s35 = np.load('s35_sector_10_spectrum.npz', allow_pickle=True)
d_s44 = np.load('s44_bcs_tensor_r.npz', allow_pickle=True)
d_s29 = np.load('s29b_bogoliubov_bcs.npz', allow_pickle=True)


# ===========================================================================
# 1. Extract eigenvalue tracks from s35 data
# ===========================================================================
print("Extracting eigenvalue tracks...")

tau_s35 = d_s35['tau_values']   # (9,)
tracks_00 = d_s35['tracks_00']  # (9, 8) -- sector (0,0) positive eigenvalues
tracks_10 = d_s35['tracks_10']  # (9, 24) -- sector (1,0) positive eigenvalues

# ===========================================================================
# 2. Extract van Hove trajectories (12 tracks)
# ===========================================================================
print("Extracting van Hove trajectories...")

tau_vh = d_vh['tau_values']  # [0, 0.05, 0.10, 0.15, 0.19]

vh_tracks = {}
for i in range(1, 13):
    prefix = f'T{i}'
    vh_tracks[i] = {
        'omega':    d_vh[f'{prefix}_omega'],
        'label':    str(d_vh[f'{prefix}_label']),
        'branch':   str(d_vh[f'{prefix}_branch']),
        'edge':     str(d_vh[f'{prefix}_edge']),
        'velocity': float(d_vh[f'{prefix}_velocity']),
    }

bw_total  = d_vh['bw_total_vs_tau']
omega_gap = d_vh['omega_gap_vs_tau']
omega_max = d_vh['omega_max_vs_tau']

# ===========================================================================
# 3. Extract spectral summary from s41
# ===========================================================================
tau_s41 = d_s41['tau_values']
lambda_min_s41 = d_s41['lambda_min']
spectral_range_s41 = d_s41['spectral_range']

# ===========================================================================
# 4. Physical Bogoliubov gap and occupation numbers
# ===========================================================================
print("Computing Bogoliubov occupation numbers...")

# Physical Bogoliubov gap from s29b (actual gap in eigenvalue units)
tau_bcs = d_s29['tau_values']  # [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
# Sector (0,3) = (0,3)+(3,0) pairing channel: the dominant channel
delta_bog_03 = d_s29['s0_3_delta_bog']  # physical gap
delta_bog_30 = d_s29['s3_0_delta_bog']
delta_bog_00 = d_s29['s0_0_delta_bog']

# Use (3,0) channel which has the largest gap (strong coupling)
delta_physical = delta_bog_30  # [0.014, 0.026, 0.034, 0.040, 0.064, 0.091, 0.106, 0.109, 0.112]

# BCS order parameter from s44 (the "Delta" in BCS theory)
Delta_0_order = float(d_s44['Delta_0'])    # 0.770
ratio_gap_EF = float(d_s44['ratio_gap_EF'])  # 0.941
xi_fold = d_s44['xi_fold']  # [0.819, 0.845, 0.978]

# Chemical potential = bottom of B2 band (lowest eigenvalue)
mu_interp = interp1d(tau_s41, lambda_min_s41, kind='cubic',
                     fill_value='extrapolate')

# Interpolate physical gap
delta_interp = interp1d(tau_bcs, delta_physical, kind='cubic',
                        fill_value='extrapolate')

# Bogoliubov occupation: n_k = v_k^2 = 0.5*(1 - xi_k/E_k)
# We use the ORDER PARAMETER Delta for the color field (this controls n_k)
# but display the PHYSICAL gap for the "horizon" boundary
def bogoliubov_nk_order(lam, mu, Delta):
    """
    Occupation using the BCS order parameter.
    lam: eigenvalue |lambda_k|
    mu: chemical potential
    Delta: BCS order parameter (large in strong coupling)
    """
    xi = np.abs(lam) - mu
    Ek = np.sqrt(xi**2 + Delta**2)
    vk2 = 0.5 * (1.0 - xi / Ek)
    return vk2


# Model Delta_order(tau): starts from 0, grows to Delta_0 = 0.770
# The BCS instability exists for any g > 0 (1D theorem, S35)
# Growth matches the delta_physical profile shape
# Normalize so delta_order(tau=0.2) = Delta_0
delta_order_raw = interp1d(tau_bcs, delta_physical, kind='cubic',
                           fill_value='extrapolate')
# Scale up: physical gap at tau=0.2 is 0.040, order parameter is 0.770
# ratio = 0.770/0.040 = 19.3
delta_scale = Delta_0_order / delta_physical[3]  # at tau=0.2

def delta_order(tau):
    """BCS order parameter as function of tau."""
    return delta_order_raw(tau) * delta_scale

# ===========================================================================
# 5. Build the Bogoliubov occupation color field
# ===========================================================================
print("Building dense spectral field...")

tau_fine = np.linspace(0.001, 0.50, 400)
lambda_fine = np.linspace(0.70, 2.15, 500)
TAU, LAM = np.meshgrid(tau_fine, lambda_fine, indexing='ij')

MU = mu_interp(TAU)
DELTA_ORD = delta_order(TAU)
NK = bogoliubov_nk_order(LAM, MU, DELTA_ORD)

# Mask regions outside the physical spectrum
lmin_interp = interp1d(tau_s41, lambda_min_s41, kind='cubic',
                       fill_value='extrapolate')
lmax_interp = interp1d(tau_s41, lambda_min_s41 + spectral_range_s41,
                       kind='cubic', fill_value='extrapolate')
LMIN = lmin_interp(TAU)
LMAX = lmax_interp(TAU)

# Smooth masking: fade alpha outside spectrum
# In-spectrum: full alpha. Outside: zero.
outside = (LAM < LMIN - 0.01) | (LAM > LMAX + 0.01)
NK_masked = np.ma.masked_where(outside, NK)


# ===========================================================================
# 6. Construct the figure: main + inset
# ===========================================================================
print("Constructing spectral Penrose diagram...")

fig = plt.figure(figsize=(16, 11))
ax = fig.add_axes([0.07, 0.08, 0.70, 0.84])  # main panel

# ---------- BACKGROUND: Bogoliubov occupation pcolormesh ----------
cmap = plt.cm.inferno.copy()
cmap.set_bad('white', alpha=0.0)

pcm = ax.pcolormesh(TAU, LAM, NK_masked, cmap=cmap, vmin=0.0, vmax=0.50,
                    shading='gouraud', alpha=0.55, rasterized=True, zorder=1)

cbar = fig.colorbar(pcm, ax=ax, label=r'$n_k = v_k^2$ (Bogoliubov occupation)',
                    shrink=0.82, pad=0.015, aspect=30)
cbar.set_ticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])
cbar.ax.tick_params(labelsize=9)

# ---------- EIGENVALUE TRACKS ----------
# Sector (0,0): 8 tracks (singlet/adjoint)
for j in range(tracks_00.shape[1]):
    track = tracks_00[:, j]
    ax.plot(tau_s35, track, '-', color='#2c3e50', linewidth=0.7, alpha=0.45,
            zorder=3)

# Sector (1,0): 24 tracks (fundamental)
for j in range(tracks_10.shape[1]):
    track = tracks_10[:, j]
    ax.plot(tau_s35, track, '-', color='#5d6d7e', linewidth=0.35, alpha=0.25,
            zorder=3)

# ---------- VAN HOVE TRAJECTORIES (band edges) ----------
vh_colors = {
    'B1':    '#e74c3c',   # red
    'B2':    '#27ae60',   # green
    'B3':    '#2980b9',   # blue
    'B1/B2': '#f39c12',   # orange (bifurcation)
}

for i in range(1, 13):
    vt = vh_tracks[i]
    branch = vt['branch']
    edge   = vt['edge']
    omega  = vt['omega']
    color  = vh_colors.get(branch, '#8e44ad')

    if 'bottom' in edge:
        style, lw = '-', 2.2
    else:
        style, lw = '--', 1.6

    ax.plot(tau_vh, omega, style, color=color, linewidth=lw, zorder=6,
            alpha=0.92)

    # Selective labels at rightmost point
    if i in [1, 2, 3, 5, 6, 9, 11, 12]:
        dx = 0.006
        ax.annotate(f'T{i}', (tau_vh[-1] + dx, omega[-1]),
                   fontsize=6, color=color, ha='left', va='center',
                   weight='bold', zorder=7)

# ---------- BCS GAP BOUNDARY (physical Bogoliubov gap = "acoustic horizon") ----------
tau_gap = np.linspace(0.02, 0.48, 200)
mu_gap = mu_interp(tau_gap)
dg = delta_interp(tau_gap)

# Physical gap edges (narrow: ~0.01-0.11 in eigenvalue units)
ax.plot(tau_gap, mu_gap + dg, '-', color='#e67e22', linewidth=2.8, zorder=8,
        label=r'Bogoliubov gap: $\mu \pm \Delta_{\rm phys}$')
ax.plot(tau_gap, mu_gap - dg, '-', color='#e67e22', linewidth=2.8, zorder=8)
ax.plot(tau_gap, mu_gap, ':', color='#e67e22', linewidth=1.0, zorder=7,
        alpha=0.6)
ax.fill_between(tau_gap, mu_gap - dg, mu_gap + dg,
                color='#f39c12', alpha=0.12, zorder=2)

# ---------- T3-T5 NEAR-CROSSING (delta = 0.0008 at dump) ----------
T3_dump = vh_tracks[3]['omega'][-1]
T5_dump = vh_tracks[5]['omega'][-1]
delta_cross = T5_dump - T3_dump

ax.annotate('', xy=(0.194, T3_dump), xytext=(0.194, T5_dump),
           arrowprops=dict(arrowstyle='<->', color='#8e44ad', lw=1.8),
           zorder=9)
ax.annotate(f'T3-T5: $\\delta={delta_cross:.4f}$\nCauchy horizon\nprecursor',
           xy=(0.200, 0.5*(T3_dump + T5_dump)),
           fontsize=6.5, color='#8e44ad', ha='left', va='center',
           weight='bold', zorder=9,
           bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                    edgecolor='#8e44ad', alpha=0.85))

# ---------- CRITICAL TAU MARKERS ----------
markers = [
    (0.0,   r'$\tau\!=\!0$' + '\nround $S^3$\nWCH min',  '#2ecc71', 2.12),
    (0.19,  'dump\npoint',    '#c0392b', 2.12),
    (0.285, 'DNP\ncross',     '#8e44ad', 2.05),
]
for tau_c, label, color, y_pos in markers:
    ax.axvline(tau_c, color=color, linestyle=':', linewidth=1.3, alpha=0.55,
               zorder=4)
    ax.annotate(label, xy=(tau_c, y_pos), fontsize=7, color=color,
               ha='center', va='bottom', weight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                        edgecolor=color, alpha=0.85), zorder=10)

# ---------- BAND LABELS ----------
band_info = [
    (0.42, 0.85,  'B1: su(2)\nadjoint',    '#e74c3c'),
    (0.42, 1.20,  'B2: $\\mathbb{C}^2$\nfundamental', '#27ae60'),
    (0.42, 1.75,  'B3: u(1)+higher',        '#2980b9'),
]
for bx, by, btxt, bc in band_info:
    ax.annotate(btxt, xy=(bx, by), fontsize=8.5, color=bc,
               ha='center', va='center', weight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                        edgecolor=bc, alpha=0.88), zorder=10)

# ---------- CONFORMAL BOUNDARY: tau=0 data ----------
ax.annotate('$|C|^2 = 5/14$\n$K = 0.500$\n8-fold degeneracy',
           xy=(0.005, 0.88), fontsize=7, color='#2ecc71',
           ha='left', va='top',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='#eafaf1',
                    edgecolor='#2ecc71', alpha=0.9), zorder=10)

# ---------- DUMP POINT PHYSICS ----------
ax.annotate('$K=0.535$, $|C|^2=0.386$\n'
           '$v_{\\rm min}=0$, BPS, $\\kappa=0$\n'
           '$T_a / T_{\\rm Gibbs} = 0.993$\n'
           'extremal horizon',
           xy=(0.19, 0.735), fontsize=6.5, color='#c0392b',
           ha='center', va='top',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='#fdedec',
                    edgecolor='#c0392b', alpha=0.9), zorder=10)

# ---------- PARTICLE CREATION REGION ----------
ax.axvspan(0.16, 0.22, color='#e74c3c', alpha=0.04, zorder=0)
ax.annotate('FOLD / Parker creation\n$N_{qp}=59.8$ pairs, $P_{exc}=1.000$\n'
           'Schwinger-instanton: $S_{inst}=0.069$',
           xy=(0.19, 2.12), fontsize=7.5, color='#922b21',
           ha='center', va='bottom', weight='bold',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='#fdedec',
                    edgecolor='#922b21', alpha=0.9), zorder=10)

# ---------- TAU FLOW ARROW ----------
ax.annotate('', xy=(0.48, 0.725), xytext=(0.02, 0.725),
           arrowprops=dict(arrowstyle='->', color='#34495e', lw=2.0))
ax.annotate(r'$\tau$ flow (Jensen deformation $\to$ Kasner)',
           xy=(0.25, 0.717), fontsize=8.5, color='#34495e',
           ha='center', va='top', style='italic')

# ---------- BANDWIDTH BARS ----------
for idx_bw, tau_bw in enumerate(tau_vh):
    lo = omega_gap[idx_bw]
    hi = omega_max[idx_bw]
    ax.plot([tau_bw, tau_bw], [lo, hi], '-', color='#bdc3c7',
            linewidth=6, alpha=0.12, zorder=0, solid_capstyle='round')

# ---------- AXIS SETUP ----------
ax.set_xlabel(r'$\tau$ (modulus parameter)', fontsize=13)
ax.set_ylabel(r'$\lambda_k$ (Dirac eigenvalue, units of $M_{KK}$)', fontsize=13)
ax.set_title('Spectral Penrose Diagram: Eigenvalue Flow in Modulus Space\n'
             r'$(\tau, \lambda_k)$ plane colored by Bogoliubov occupation $n_k$',
             fontsize=14, weight='bold', pad=12)
ax.set_xlim(-0.02, 0.52)
ax.set_ylim(0.70, 2.22)
ax.grid(True, alpha=0.12, linestyle='-', linewidth=0.5)
ax.tick_params(labelsize=10)

# ---------- LEGEND ----------
legend_elements = [
    Line2D([0], [0], color='#e74c3c', lw=2.2, label='VH bottom: B1 (su(2))'),
    Line2D([0], [0], color='#e74c3c', lw=1.6, ls='--', label='VH top: B1'),
    Line2D([0], [0], color='#27ae60', lw=2.2, label='VH bottom: B2 ($\\mathbb{C}^2$)'),
    Line2D([0], [0], color='#27ae60', lw=1.6, ls='--', label='VH top: B2'),
    Line2D([0], [0], color='#2980b9', lw=2.2, label='VH bottom: B3 (u(1)+)'),
    Line2D([0], [0], color='#2980b9', lw=1.6, ls='--', label='VH top: B3'),
    Line2D([0], [0], color='#f39c12', lw=2.2, label='T3: B1/B2 bifurcation'),
    Line2D([0], [0], color='#e67e22', lw=2.8,
           label=r'Bogoliubov gap $\mu \pm \Delta_{\rm phys}$'),
    Line2D([0], [0], color='#2c3e50', lw=0.7, alpha=0.45,
           label='(0,0) eigenvalue tracks'),
    Line2D([0], [0], color='#5d6d7e', lw=0.35, alpha=0.25,
           label='(1,0) eigenvalue tracks'),
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=7,
         framealpha=0.92, edgecolor='#bdc3c7', ncol=1)


# ===========================================================================
# 7. INSET: zoomed gap region near dump
# ===========================================================================
axins = ax.inset_axes([0.57, 0.03, 0.40, 0.28])

# Zoom: tau in [0.05, 0.35], lambda in [0.78, 1.02]
tau_zidx = np.where((tau_fine >= 0.03) & (tau_fine <= 0.38))[0]
lam_zidx = np.where((lambda_fine >= 0.78) & (lambda_fine <= 1.02))[0]

if len(tau_zidx) > 0 and len(lam_zidx) > 0:
    TAU_z = TAU[np.ix_(tau_zidx, lam_zidx)]
    LAM_z = LAM[np.ix_(tau_zidx, lam_zidx)]
    NK_z  = NK_masked[np.ix_(tau_zidx, lam_zidx)]

    axins.pcolormesh(TAU_z, LAM_z, NK_z, cmap=cmap, vmin=0, vmax=0.50,
                     shading='gouraud', alpha=0.6, rasterized=True)

# Eigenvalue tracks in zoom
for j in range(tracks_00.shape[1]):
    axins.plot(tau_s35, tracks_00[:, j], '-', color='#2c3e50', lw=1.0,
               alpha=0.6)

# VH tracks in zoom window
for i in range(1, 13):
    vt = vh_tracks[i]
    omega = vt['omega']
    if np.any((omega >= 0.78) & (omega <= 1.02)):
        branch = vt['branch']
        edge   = vt['edge']
        color  = vh_colors.get(branch, '#8e44ad')
        style  = '-' if 'bottom' in edge else '--'
        lw     = 2.5 if 'bottom' in edge else 2.0
        axins.plot(tau_vh, omega, style, color=color, linewidth=lw, alpha=0.9)
        if omega[-1] >= 0.78 and omega[-1] <= 1.02:
            axins.annotate(f'T{i}', (tau_vh[-1]+0.004, omega[-1]),
                          fontsize=6.5, color=color, weight='bold')

# Physical gap in zoom
tau_gz = tau_gap[(tau_gap >= 0.03) & (tau_gap <= 0.38)]
mu_gz  = mu_interp(tau_gz)
dg_z   = delta_interp(tau_gz)
axins.plot(tau_gz, mu_gz + dg_z, '-', color='#e67e22', lw=2.2)
axins.plot(tau_gz, mu_gz - dg_z, '-', color='#e67e22', lw=2.2)
axins.plot(tau_gz, mu_gz, ':', color='#e67e22', lw=0.8, alpha=0.6)
axins.fill_between(tau_gz, mu_gz - dg_z, mu_gz + dg_z,
                   color='#f39c12', alpha=0.15)

# Dump + DNP markers
axins.axvline(0.19, color='#c0392b', ls=':', lw=1.5, alpha=0.65)
axins.axvline(0.285, color='#8e44ad', ls=':', lw=1.2, alpha=0.4)
axins.annotate('dump', xy=(0.192, 1.015), fontsize=7, color='#c0392b',
              ha='left', weight='bold')

# T3-T5 crossing in zoom
axins.annotate('', xy=(0.194, T3_dump), xytext=(0.194, T5_dump),
              arrowprops=dict(arrowstyle='<->', color='#8e44ad', lw=1.5))
axins.annotate(f'$\\delta$={delta_cross:.4f}',
              xy=(0.200, 0.5*(T3_dump+T5_dump)),
              fontsize=6.5, color='#8e44ad', ha='left', va='center',
              weight='bold')

axins.set_xlim(0.03, 0.38)
axins.set_ylim(0.78, 1.02)
axins.set_xlabel(r'$\tau$', fontsize=8)
axins.set_ylabel(r'$\lambda_k$', fontsize=8)
axins.set_title('Gap + B1/B2/B3 junction near dump', fontsize=8, weight='bold')
axins.tick_params(labelsize=7)
axins.grid(True, alpha=0.18, linewidth=0.3)

# Indicate zoom region
ax.indicate_inset_zoom(axins, edgecolor='#7f8c8d', linewidth=1.0, alpha=0.4)


# ===========================================================================
# 8. ASCII Penrose diagram annotation (right margin)
# ===========================================================================
# Add a text-based structural key on the right side
structural_lines = [
    r"$\bf{STRUCTURAL\ KEY}$",
    "________________________",
    r"$\tau\!=\!0$: round $S^3$ ($i^-$)",
    r"   8-fold degeneracy",
    r"   $|C|^2 = 5/14$ (WCH)",
    "",
    r"$\tau\!=\!0.19$: Extremal horizon",
    r"   $\kappa\!=\!0$, BPS, $T_H\!=\!0$",
    r"   $v_{\rm min}\!=\!0$ (GSL)",
    r"   59.8 qp pairs created",
    "",
    r"$\tau\!=\!0.285$: DNP crossing",
    r"   NEC boundary begins",
    "",
    r"$\tau\!=\!0.78$: NEC violation",
    r"   su(2) Ricci eigenvalue = 0",
    "",
    r"$\tau\!\to\!\infty$: Kasner singularity",
    r"   (censored by BCS)",
    "________________________",
    r"Petrov D $\to$ II at dump",
    r"K monotonic ($K'>0$ all $\tau>0$)",
    r"Weyl grows: WCH arrow",
]
structural_text = "\n".join(structural_lines)
fig.text(0.82, 0.50, structural_text, fontsize=7.5, va='center',
         ha='left', linespacing=1.35,
         bbox=dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa',
                  edgecolor='#aab7b8', alpha=0.95))


# ===========================================================================
# 9. Save outputs
# ===========================================================================
print("Saving outputs...")

fig.savefig('s45_spectral_penrose.png', dpi=200, bbox_inches='tight',
            facecolor='white')
plt.close(fig)
print(f"  -> s45_spectral_penrose.png saved")

# Save computed fields
np.savez_compressed('s45_spectral_penrose.npz',
    # Grid
    tau_fine=tau_fine,
    lambda_fine=lambda_fine,
    # Bogoliubov occupation field
    NK_field=NK,
    # Band boundaries
    lambda_min_interp=lmin_interp(tau_fine),
    lambda_max_interp=lmax_interp(tau_fine),
    # Physical BCS gap profile
    tau_gap=tau_gap,
    mu_gap=mu_interp(tau_gap),
    delta_phys_gap=delta_interp(tau_gap),
    # Order parameter profile
    delta_order_gap=delta_order(tau_gap),
    # Key numbers from data
    Delta_0_order_parameter=Delta_0_order,
    ratio_gap_EF=ratio_gap_EF,
    xi_fold=xi_fold,
    T3_T5_crossing_delta=delta_cross,
    T3_at_dump=T3_dump,
    T5_at_dump=T5_dump,
    # Van Hove velocities at dump
    vh_velocities=np.array([vh_tracks[i]['velocity'] for i in range(1,13)]),
    vh_omega_at_dump=np.array([vh_tracks[i]['omega'][-1] for i in range(1,13)]),
    vh_branches=np.array([vh_tracks[i]['branch'] for i in range(1,13)]),
    vh_edges=np.array([vh_tracks[i]['edge'] for i in range(1,13)]),
    # Bandwidth evolution
    bw_total_vs_tau=bw_total,
    omega_gap_vs_tau=omega_gap,
    omega_max_vs_tau=omega_max,
    # Occupation statistics
    nk_max=float(np.nanmax(NK)),
    # Gate
    gate_name='SPECTRAL-PENROSE-45',
    gate_verdict='INFO',
    gate_detail='Spectral Penrose diagram constructed. (tau,lambda_k) plane with '
                '12 VH trajectories, 32 eigenvalue tracks, physical Bogoliubov gap, '
                'and n_k occupation color field. T3-T5 near-crossing delta=0.0008 '
                'at dump. This is a spectral-geometric object, NOT a spacetime diagram.',
)
print(f"  -> s45_spectral_penrose.npz saved")


# ===========================================================================
# 10. Diagnostic summary
# ===========================================================================
print("\n" + "="*72)
print("SPECTRAL PENROSE DIAGRAM: DIAGNOSTIC SUMMARY")
print("="*72)

print(f"\nEigenvalue tracks:")
print(f"  Sector (0,0): {tracks_00.shape[1]} positive eigenvalues, "
      f"tau range [{tau_s35[0]:.2f}, {tau_s35[-1]:.2f}]")
print(f"  Sector (1,0): {tracks_10.shape[1]} positive eigenvalues")
print(f"  Van Hove: 12 trajectories (6 bottom, 6 top)")

print(f"\nBCS gap (physical Bogoliubov gap from s29b, sector (3,0)):")
for i, t in enumerate(tau_bcs):
    print(f"  tau={t:.2f}: Delta_phys = {delta_physical[i]:.6f}")

print(f"\nBCS order parameter (s44): Delta_0 = {Delta_0_order:.4f}")
print(f"  ratio Delta_0/E_F = {ratio_gap_EF:.4f}")
print(f"  Strong coupling: gap ~ Fermi energy")

print(f"\nVan Hove near-crossing at dump (tau=0.19):")
print(f"  T3 (B1/B2 bifurcation top): {T3_dump:.6f}")
print(f"  T5 (B3 bottom):             {T5_dump:.6f}")
print(f"  Separation:                  {delta_cross:.6f}")
print(f"  Analogy: Cauchy horizon instability (blueshift factor ~ 1/delta)")

print(f"\nBand structure at dump:")
for i in range(1, 13):
    vt = vh_tracks[i]
    print(f"  T{i:2d}: omega={vt['omega'][-1]:.6f}, "
          f"v={vt['velocity']:+.4f}, {vt['branch']:5s} {vt['edge']}")

print(f"\nBandwidth evolution:")
print(f"  tau=0.00: W = {bw_total[0]:.4f}")
print(f"  tau=0.19: W = {bw_total[-1]:.4f}")
print(f"  Growth rate: {float(d_vh['bw_growth_rate']):.4f}")

print(f"\nStructural analogies to spacetime Penrose diagram:")
print(f"  tau=0        <-> past timelike infinity i^- (round metric, max symmetry)")
print(f"  tau=0.19     <-> extremal horizon (kappa=0, BPS, T_H=0)")
print(f"  tau=0.285    <-> DNP boundary (NEC begins to be violated)")
print(f"  tau=0.78     <-> NEC violation surface (su(2) Ricci eigenvalue = 0)")
print(f"  tau -> inf   <-> Kasner singularity (censored by BCS)")
print(f"  VH tracks    <-> null geodesic congruences (band edges)")
print(f"  T3-T5 cross  <-> Cauchy horizon (near-crossing = blueshift)")
print(f"  BCS gap      <-> acoustic horizon (T_a/T_Gibbs = 0.993)")
print(f"  n_k color    <-> particle creation (Bogoliubov = Hawking analog)")

print(f"\nGate: SPECTRAL-PENROSE-45 = INFO (visualization)")
print("="*72)
