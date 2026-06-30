#!/usr/bin/env python3
"""
Phononic Crystal Geometry — Publication Visualizations
=======================================================
Source: sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md (S47/S53 crystal layer)
Output: sessions/framework/Phononic-Crystal-Geometry-Vis-{1..11}.png

Generates 11 publication-quality figures for the phononic crystal geometry of the
SU(3) Jensen-deformed internal space.

  Vis-1 .. Vis-7  — the S47/S53 crystal-layer core, brought to current (S93-era)
                    canonical values: 32-cell Voronoi, tight-binding bands, sound-speed
                    hierarchy, Mott regime, BCS speed bump, e-fold budget, quantum walker.
  Vis-8 .. Vis-11 — the post-S47 geometric DEEPENING of the SAME substrate geometry
                    (SX W8 comprehensive expansion; substrate-first — VISUALIZES closed/
                    permanent KB results, does NOT re-derive them):
                      Vis-8  E1  4-stratum bottom-20 partition (2,4,8,6) + tau-asymmetric
                                 breakdown (§VII.AJ S87 W11-2; §VII.AE S88 W2-9).
                      Vis-9  E2  spectral-moment a_n(tau) landscape + protected ratio
                                 R_1 = a_0 a_4 / a_2^2 + R-monotonicity (S64 W1-A / S73B/S74).
                      Vis-10 E3  spectral-dimension flow d_s(sigma) on the Jensen D_K
                                 spectrum vs CDT (S92 ad-hoc).
                      Vis-11 E4  cross-pillar bridge geometry R_universal -> quantum-metric
                                 trace; R_canonical = 7.3250 (§VII.W S86 / S89 W2).

Direction of explanation (phononic-framing.md, IS-not-IN): the substrate IS the spectral
triple (A_K, H_K, D_K(tau)); the tessellation, bands, partition strata, spectral moments,
and bridge pairing are how the substrate's spectral weight organizes — NOT structures
living IN a container. Every figure flows FROM the D_K spectrum TOWARD emergent physics.
"""

import sys
import os

# Ensure canonical_constants is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'computations/_shared'))

from canonical_constants import (
    tau_fold, c_fabric, c_Gold, J_C2, J_su2, J_u1,
    N_cells, E_cond, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    N_e_classical, xi_BCS, L_over_xi, Delta_0_GL,
    # Spectral-action moments at the fold (S64 W1-A; reproduce R_protected_fold exactly):
    a0_fold, a2_fold, a4_fold, R_protected_fold,
    # Post-S47 new-figure anchors (SX W8; substrate-first KB-sourced, see header):
    delta_tau_crit_neg, delta_tau_crit_pos, d_s_fold_window_sigma, R_canonical_bridge,
)

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Wedge
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import patheffects

# ==============================================================================
# Global style
# ==============================================================================
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 13,
    'axes.titlesize': 14,
    'legend.fontsize': 9,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 200,
    'savefig.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
    'axes.linewidth': 0.8,
    'grid.alpha': 0.3,
    'lines.linewidth': 1.8,
    'text.usetex': False,
})

OUT_DIR = os.path.join(os.path.dirname(__file__))

# Framework constants
EJ_EC = 0.818       # E_J / E_C ratio (Mott side)
Gi = 0.506           # Ginzburg number
c_ratio = c_fabric / c_Gold  # ~229.5
N_e_sound = 0.5 * np.log(c_ratio)  # ~2.72
N_e_geom = N_e_classical  # 0.1734
N_e_foam = 0.00      # Foam: not in source document table (absorbed into missing factors)
N_e_density = 0.00   # Density (cancels)
N_e_total = 2.8913   # Total acoustic e-folds from document table (S53)
THRESHOLD = 3.1      # Inflationary threshold
GAP = 0.21           # Document: "falls 0.21 short"

# Band structure parameters — band CENTERS (omega0) sourced from canonical_constants
# (SX W8 D3 fix: the prior dict HARDCODED Higgs-2=1.456 / Higgs-3=10.37, leaving the imported
#  omega_H2 / omega_H3 as DEAD imports and the displayed Higgs band-centers STALE vs canonical
#  omega_H2=1.41 / omega_H3=11.465. Now every center is the imported canonical value; the band
#  WIDTHS BW are S52 GL-extrapolation shaping parameters, not canonical constants, kept # (local).)
BRANCHES = {
    'Goldstone': {'omega0': 0.000,    'BW': 0.507, 'color': '#DAA520', 'ls': '-'},   # Gamma-point gap 0 (Goldstone)
    'Leggett-1': {'omega0': omega_L1, 'BW': 0.392, 'color': '#4169E1', 'ls': '-'},   # canonical omega_L1=0.138 (S52 GL)
    'Leggett-2': {'omega0': omega_L2, 'BW': 0.325, 'color': '#1E90FF', 'ls': '--'},  # canonical omega_L2=0.192 (S52 GL)
    'Higgs-1':   {'omega0': omega_H1, 'BW': 0.004, 'color': '#DC143C', 'ls': '-'},   # canonical omega_H1=0.380
    'Higgs-2':   {'omega0': omega_H2, 'BW': 0.052, 'color': '#B22222', 'ls': '--'},  # canonical omega_H2=1.410 (was 1.456)
    'Higgs-3':   {'omega0': omega_H3, 'BW': 2.60,  'color': '#8B0000', 'ls': '-.'},  # canonical omega_H3=11.465 (was 10.37)
}
BW_PROVENANCE = "BW = S52 GL-JOSEPHSON-52 bandwidth extrapolation (not canonical-pinned)"  # (local)


def save_fig(fig, n):
    """Save figure with consistent naming."""
    path = os.path.join(OUT_DIR, f'Phononic-Crystal-Geometry-Vis-{n}.png')
    fig.savefig(path)
    plt.close(fig)
    print(f"  Saved: {path}")


# ==============================================================================
# VIS-1: 32-Cell Voronoi Tessellation of SU(3) with Josephson Couplings
# ==============================================================================
def vis1_voronoi_tessellation():
    """
    Construct a 3D BCC-like network of 32 cells.
    The 32 cells of SU(3) arise from |W(SU(3))|=6, Z_3 center, and torus tessellation.
    We represent this as a BCC-like lattice projected into 3D, with bonds color-coded
    by Josephson coupling type.
    """
    print("Generating Vis-1: 32-Cell Voronoi Tessellation...")

    fig = plt.figure(figsize=(10, 9))
    ax = fig.add_subplot(111, projection='3d')

    rng = np.random.RandomState(42)

    # Generate 32 nodes in a quasi-BCC arrangement:
    # BCC unit cell has 2 atoms; 4x2x2 unit cells = 32 atoms
    nodes = []
    nx, ny, nz = 4, 2, 2
    a_lat = 1.0  # lattice constant
    for ix in range(nx):
        for iy in range(ny):
            for iz in range(nz):
                # Corner atom
                nodes.append(np.array([ix, iy, iz]) * a_lat)
                # Body-center atom
                nodes.append(np.array([ix + 0.5, iy + 0.5, iz + 0.5]) * a_lat)

    nodes = np.array(nodes)
    # Center the lattice
    nodes -= nodes.mean(axis=0)

    # Compute pairwise distances for bond assignment
    N = len(nodes)
    dists = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            dists[i, j] = np.linalg.norm(nodes[i] - nodes[j])

    # Sort unique distances to identify nearest-neighbor shells
    unique_dists = np.sort(np.unique(np.round(dists[dists > 0.01], 4)))

    # BCC nearest neighbor = a*sqrt(3)/2 ~ 0.866
    # Second nearest = a ~ 1.0
    # Third nearest = a*sqrt(2) ~ 1.414
    d_nn1 = unique_dists[0]  # ~0.866 (body diagonal/2)
    d_nn2 = unique_dists[1]  # ~1.0   (face)
    d_nn3 = unique_dists[2]  # ~1.414 (face diagonal) if exists

    # Assign bond types based on distance shells:
    #   Shell 1 (nearest, 4 bonds): J_C2 (dominant, C^2 coset)
    #   Shell 2 (next, 3 bonds): J_su2
    #   Shell 3 (furthest shown, 1 bond): J_u1
    bonds_C2 = []
    bonds_su2 = []
    bonds_u1 = []

    tol = 0.05
    for i in range(N):
        for j in range(i + 1, N):
            d = dists[i, j]
            if abs(d - d_nn1) < tol:
                bonds_C2.append((i, j))
            elif abs(d - d_nn2) < tol:
                bonds_su2.append((i, j))
            elif len(unique_dists) > 2 and abs(d - d_nn3) < tol:
                bonds_u1.append((i, j))

    # Limit bonds per cell to match 4+3+1=8 target (take first available)
    # For visual clarity, show a representative subset
    max_C2_show = min(len(bonds_C2), 80)
    max_su2_show = min(len(bonds_su2), 50)
    max_u1_show = min(len(bonds_u1), 20)

    # Draw bonds
    for idx, (i, j) in enumerate(bonds_C2[:max_C2_show]):
        ax.plot([nodes[i, 0], nodes[j, 0]],
                [nodes[i, 1], nodes[j, 1]],
                [nodes[i, 2], nodes[j, 2]],
                color='#DC143C', linewidth=2.2, alpha=0.7,
                label='$J_{C^2}$ = 0.933 (4 bonds)' if idx == 0 else '')

    for idx, (i, j) in enumerate(bonds_su2[:max_su2_show]):
        ax.plot([nodes[i, 0], nodes[j, 0]],
                [nodes[i, 1], nodes[j, 1]],
                [nodes[i, 2], nodes[j, 2]],
                color='#4169E1', linewidth=1.3, alpha=0.6,
                label='$J_{su(2)}$ = 0.059 (3 bonds)' if idx == 0 else '')

    for idx, (i, j) in enumerate(bonds_u1[:max_u1_show]):
        ax.plot([nodes[i, 0], nodes[j, 0]],
                [nodes[i, 1], nodes[j, 1]],
                [nodes[i, 2], nodes[j, 2]],
                color='#228B22', linewidth=0.8, alpha=0.5,
                label='$J_{u(1)}$ = 0.038 (1 bond)' if idx == 0 else '')

    # Draw nodes
    ax.scatter(nodes[:, 0], nodes[:, 1], nodes[:, 2],
               s=120, c='#2F4F4F', edgecolors='black', linewidth=0.5,
               zorder=5, alpha=0.9)

    # Label a few cells
    for idx in [0, 7, 15, 24, 31]:
        if idx < N:
            ax.text(nodes[idx, 0] + 0.08, nodes[idx, 1] + 0.08,
                    nodes[idx, 2] + 0.08, str(idx + 1),
                    fontsize=7, color='white',
                    path_effects=[patheffects.withStroke(linewidth=2, foreground='black')])

    ax.set_xlabel('$e_1$ (projected)', labelpad=8)
    ax.set_ylabel('$e_2$ (projected)', labelpad=8)
    ax.set_zlabel('$e_3$ (projected)', labelpad=8)
    ax.set_title('32-Cell Voronoi Tessellation of SU(3)\nwith Josephson Couplings',
                 fontsize=14, fontweight='bold', pad=15)

    ax.legend(loc='upper left', framealpha=0.9, fontsize=10)

    # Annotation box
    textstr = (f'$N_{{cells}}$ = {N_cells}\n'
               f'Bonds/cell = 8  (4 + 3 + 1)\n'
               f'$J_{{C^2}} / J_{{u(1)}}$ = {J_C2/J_u1:.1f}\n'
               f'BCC-like from Weyl($SU(3)$)')
    props = dict(boxstyle='round,pad=0.4', facecolor='wheat', alpha=0.85)
    ax.text2D(0.72, 0.05, textstr, transform=ax.transAxes,
              fontsize=9, verticalalignment='bottom', bbox=props)

    ax.view_init(elev=25, azim=135)
    ax.set_box_aspect([2, 1, 1])

    save_fig(fig, 1)


# ==============================================================================
# VIS-2: Tight-Binding Band Structure
# ==============================================================================
def vis2_band_structure():
    """
    Plot omega(K) for 6 tight-binding branches from K=0 to K_BZ.
    Dispersion: omega(K) = omega_0 + BW/2 * (1 - cos(K*a))
    where BW is the bandwidth and omega_0 is the gap frequency.
    """
    print("Generating Vis-2: Tight-Binding Band Structure...")

    fig, (ax_main, ax_inset) = plt.subplots(1, 2, figsize=(14, 7),
                                             gridspec_kw={'width_ratios': [3, 1]})

    K = np.linspace(0, np.pi, 500)  # K from 0 to K_BZ = pi/a

    # Plot each branch
    for name, params in BRANCHES.items():
        omega0 = params['omega0']
        BW = params['BW']
        # Tight-binding: omega(K) = omega_0 + BW/2 * (1 - cos(Ka))
        omega = omega0 + BW / 2.0 * (1.0 - np.cos(K))

        if name == 'Higgs-3':
            continue  # Plot separately in inset due to scale

        ax_main.plot(K / np.pi, omega, color=params['color'], ls=params['ls'],
                     linewidth=2.5, label=name, zorder=3)

    # Mark gap frequencies with horizontal dashed lines.
    # SX W8 D4 disambiguation: the omega_L1/L2 plotted here are the S52 GL Leggett-band
    # Gamma-point gaps (0.138 / 0.192 M_KK, GL-JOSEPHSON-52) — a DIFFERENT observable from
    # the S48 3-band Leggett frequencies (0.070 / 0.107 M_KK, LEGGETT-MODE-48) that share the
    # symbol in the archived source doc §9. These are the GL Gamma-gaps (tight-binding band centers).
    gap_freqs = {
        '$\\omega_{L1}$ (S52 GL)': (omega_L1, '#4169E1'),
        '$\\omega_{L2}$ (S52 GL)': (omega_L2, '#1E90FF'),
        '$\\omega_{H1}$': (omega_H1, '#DC143C'),
        '$\\omega_{H2}$': (omega_H2, '#B22222'),
    }
    for label, (freq, color) in gap_freqs.items():
        ax_main.axhline(freq, color=color, ls=':', alpha=0.4, linewidth=0.8)
        ax_main.text(1.02, freq, label, transform=ax_main.get_yaxis_transform(),
                     fontsize=8, color=color, va='center')

    # Mark Goldstone slope
    # c_Gold = dw/dK at K=0. The slope in K/K_BZ units is c_Gold * pi
    K_slope = np.linspace(0, 0.25, 100)
    omega_slope = c_Gold * K_slope * np.pi  # slope in K/K_BZ coordinates
    ax_main.plot(K_slope, omega_slope, 'k--', linewidth=1.2, alpha=0.6)
    ax_main.annotate(f'$c_{{Gold}}$ = {c_Gold} $M_{{KK}}$',
                     xy=(0.08, c_Gold * 0.08 * np.pi), xycoords='data',
                     fontsize=10, color='#8B6914', fontweight='bold',
                     xytext=(0.18, 0.06), textcoords='data',
                     arrowprops=dict(arrowstyle='->', color='#8B6914', lw=1.5))

    # Mark exact crossings (not anti-crossings -- S53 Berry result)
    # Crossings occur where branches with different block structure intersect
    # Find approximate crossing points between Goldstone and Leggett-1
    for br1_name, br2_name in [('Goldstone', 'Leggett-1'),
                                ('Goldstone', 'Leggett-2'),
                                ('Leggett-1', 'Leggett-2'),
                                ('Leggett-2', 'Higgs-1')]:
        br1 = BRANCHES[br1_name]
        br2 = BRANCHES[br2_name]
        o1 = br1['omega0'] + br1['BW'] / 2.0 * (1.0 - np.cos(K))
        o2 = br2['omega0'] + br2['BW'] / 2.0 * (1.0 - np.cos(K))
        diff = o1 - o2
        # Find sign changes
        sign_changes = np.where(np.diff(np.sign(diff)))[0]
        for sc in sign_changes:
            K_cross = K[sc]
            omega_cross = o1[sc]
            if omega_cross < 2.0:  # Only show in main panel range
                ax_main.plot(K_cross / np.pi, omega_cross, 'ko', markersize=8,
                             markerfacecolor='none', markeredgewidth=1.5, zorder=5)

    # Add crossing label
    ax_main.text(0.55, 1.65, '4 exact crossings\n(not anti-crossings)',
                 fontsize=9, style='italic', color='#333333',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))

    ax_main.set_xlabel('$K / K_{BZ}$', fontsize=13)
    ax_main.set_ylabel('$\\omega(K)$ [$M_{KK}$]', fontsize=13)
    ax_main.set_title('Tight-Binding Band Structure:\nSingle Cooper Pair on SU(3) Crystal',
                       fontsize=14, fontweight='bold')
    ax_main.set_xlim(0, 1)
    ax_main.set_ylim(-0.05, 2.0)
    ax_main.legend(loc='upper left', framealpha=0.95, fontsize=10)

    # Inset: Higgs-3 branch (separate scale)
    params_H3 = BRANCHES['Higgs-3']
    omega_H3_band = params_H3['omega0'] + params_H3['BW'] / 2.0 * (1.0 - np.cos(K))
    ax_inset.plot(K / np.pi, omega_H3_band, color=params_H3['color'],
                  ls=params_H3['ls'], linewidth=2.5, label='Higgs-3')
    ax_inset.axhline(params_H3['omega0'], color=params_H3['color'],
                     ls=':', alpha=0.4, linewidth=0.8)
    ax_inset.set_xlabel('$K / K_{BZ}$', fontsize=11)
    ax_inset.set_ylabel('$\\omega(K)$ [$M_{KK}$]', fontsize=11)
    ax_inset.set_title('Higgs-3\n(Breathing Mode)', fontsize=11)
    ax_inset.set_xlim(0, 1)
    ax_inset.legend(loc='upper left', fontsize=9)
    ax_inset.text(0.5, params_H3['omega0'] - 0.3,
                  f'$\\omega_{{H3}}$ = {params_H3["omega0"]:.2f}',
                  fontsize=9, color=params_H3['color'], ha='center')

    fig.tight_layout()
    save_fig(fig, 2)


# ==============================================================================
# VIS-3: Sound Speed Hierarchy (Nested Light Cones)
# ==============================================================================
def vis3_sound_speed_hierarchy():
    """
    Spacetime diagram showing two propagation cones:
    wide geometric cone (c_fabric) and narrow acoustic cone (c_Gold).
    """
    print("Generating Vis-3: Sound Speed Hierarchy...")

    fig, ax = plt.subplots(figsize=(10, 8))

    # Spacetime diagram: t vertical, x horizontal
    # Normalize so c_fabric cone reaches edges
    t_max = 1.0
    x_max_fabric = t_max  # c_fabric normalized to 1

    # c_Gold / c_fabric = 1/229.5
    ratio_inv = c_Gold / c_fabric  # ~0.00436

    # Draw the fabric cone (wide)
    fabric_color = '#B8860B'
    t_vals = np.linspace(0, t_max, 200)

    # Right and left boundaries of fabric cone
    ax.fill_between(t_vals, -t_vals, t_vals, alpha=0.08, color=fabric_color)
    ax.plot(t_vals, t_vals, color=fabric_color, linewidth=2.5, label=f'$c_{{fabric}}$ = {c_fabric:.1f} $M_{{KK}}$')
    ax.plot(-t_vals, t_vals, color=fabric_color, linewidth=2.5)

    # Draw the acoustic cone (narrow)
    acoustic_color = '#4169E1'
    x_acoustic = t_vals * ratio_inv

    # Exaggerate for visibility: use 1/10 instead of 1/229
    visual_ratio = 0.10  # visual exaggeration
    x_acoustic_visual = t_vals * visual_ratio

    ax.fill_between(x_acoustic_visual, 0, t_vals, alpha=0.15, color=acoustic_color)
    ax.fill_between(-x_acoustic_visual, 0, t_vals, alpha=0.15, color=acoustic_color)
    ax.plot(x_acoustic_visual, t_vals, color=acoustic_color, linewidth=2.5,
            label=f'$c_{{Gold}}$ = {c_Gold:.3f} $M_{{KK}}$')
    ax.plot(-x_acoustic_visual, t_vals, color=acoustic_color, linewidth=2.5)

    # Arrow showing the ratio
    ax.annotate('', xy=(0.65, 0.65), xytext=(0.065, 0.65),
                arrowprops=dict(arrowstyle='<->', color='#333333', lw=1.5))
    ax.text(0.36, 0.68, f'229$\\times$ hierarchy', fontsize=12,
            fontweight='bold', ha='center', color='#333333')

    # Label the cones
    ax.text(0.72, 0.35, 'Substrate\n(geometric)\ncone', fontsize=11,
            color=fabric_color, ha='center', fontweight='bold', rotation=42)
    ax.text(0.065, 0.45, 'Acoustic\n(phonon)\ncone', fontsize=10,
            color=acoustic_color, ha='center', fontweight='bold', rotation=83)

    # Origin marker
    ax.plot(0, 0, 'ko', markersize=8, zorder=5)
    ax.text(0.02, -0.05, 'Event', fontsize=10, ha='left')

    # Axes
    ax.set_xlabel('$x$ [internal space coordinate]', fontsize=13)
    ax.set_ylabel('$\\tau$ [deformation time]', fontsize=13)

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.1, 1.1)
    ax.set_aspect('equal')

    ax.set_title('Geometric vs Acoustic Causal Structure\n$c_{fabric}/c_{Gold}$ = 229$\\times$ Hierarchy',
                 fontsize=14, fontweight='bold')

    # Info box
    textstr = ('Acoustic cone exaggerated 23$\\times$\nfor visibility\n\n'
               f'$c_{{fabric}}$ = {c_fabric:.1f} $M_{{KK}}$\n'
               f'$c_{{Gold}}$ = {c_Gold:.3f} $M_{{KK}}$\n'
               f'Ratio = {c_ratio:.1f}$\\times$\n'
               f'$\\Rightarrow$ {N_e_sound:.2f} acoustic e-folds')
    props = dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9,
                 edgecolor='#B8860B')
    ax.text(0.98, 0.02, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', horizontalalignment='right', bbox=props)

    ax.legend(loc='upper left', fontsize=11, framealpha=0.9)

    save_fig(fig, 3)


# ==============================================================================
# VIS-4: Mott Phase Diagram
# ==============================================================================
def vis4_mott_phase_diagram():
    """
    Josephson array phase diagram: E_J/E_C vs some order parameter or N_pair.
    Mark the framework's position deep in the Mott regime.
    """
    print("Generating Vis-4: Mott Phase Diagram...")

    fig, ax = plt.subplots(figsize=(10, 7))

    # Phase diagram: E_J/E_C on x-axis (log scale), effective order parameter on y-axis
    # The superfluid-insulator boundary for coordination z:
    # Critical (E_J/E_C)_c ~ 5.8*z for large z (mean-field)
    # For z=8 (cube): ~5.8*8 ~ 46? That's too high.
    # Standard result: for BCC with z=8, (E_J/E_C)_c ~ 0.06*z ~ 0.5 per site
    # Actually for a Josephson junction array, the transition is at
    # (E_J/E_C)_c ≈ z/16 for d=3 (Fisher et al.)
    # Document says z=16 for 8D lattice (32 cells), critical ~ z = 16
    # Let's use the document's statement: critical E_J/E_C ~ 16

    z_coord = 16  # coordination number
    EJ_EC_crit = z_coord  # critical ratio from document

    # x-axis: E_J / E_C from 0.01 to 100
    x = np.logspace(-1.5, 2.2, 1000)

    # Superfluid order parameter: <cos(phi)> ~ tanh((E_J/E_C - crit)/width)
    # Sigmoid transition
    width = 3.0
    order_param = 0.5 * (1.0 + np.tanh((np.log10(x) - np.log10(EJ_EC_crit)) / 0.3))

    # Fill regions
    mott_mask = x < EJ_EC_crit
    sf_mask = x >= EJ_EC_crit

    ax.fill_between(x, 0, 1, where=mott_mask, alpha=0.15,
                    color='#4169E1', label='Mott insulator')
    ax.fill_between(x, 0, 1, where=sf_mask, alpha=0.15,
                    color='#DC143C', label='Superfluid')

    # Transition boundary
    ax.axvline(EJ_EC_crit, color='black', linewidth=2, ls='--', alpha=0.7,
               label=f'Critical $E_J/E_C \\approx z$ = {z_coord}')

    # Order parameter curve
    ax.plot(x, order_param, 'k-', linewidth=2.5, zorder=3)
    ax.text(80, 0.85, '$\\langle \\cos \\hat{\\phi} \\rangle$',
            fontsize=14, fontweight='bold')

    # Framework position
    ax.axvline(EJ_EC, color='#B8860B', linewidth=2.5, ls='-', alpha=0.9, zorder=4)
    # Order parameter at framework position
    op_framework = 0.5 * (1.0 + np.tanh((np.log10(EJ_EC) - np.log10(EJ_EC_crit)) / 0.3))
    ax.plot(EJ_EC, op_framework, 'o', color='#B8860B', markersize=14,
            markeredgecolor='black', markeredgewidth=1.5, zorder=5)

    # Arrow pointing to framework
    ax.annotate(f'Framework\n$E_J/E_C$ = {EJ_EC}\n$N_{{pair}}$ = 1',
                xy=(EJ_EC, op_framework + 0.02),
                xytext=(EJ_EC * 3.5, 0.55),
                fontsize=12, fontweight='bold', color='#B8860B',
                arrowprops=dict(arrowstyle='->', color='#B8860B', lw=2),
                bbox=dict(boxstyle='round,pad=0.4', facecolor='wheat', alpha=0.9))

    # Label regions
    ax.text(0.15, 0.85, 'MOTT\nINSULATOR', fontsize=18, fontweight='bold',
            color='#4169E1', alpha=0.6, ha='center', va='center',
            transform=ax.transAxes)
    ax.text(0.82, 0.85, 'SUPERFLUID', fontsize=18, fontweight='bold',
            color='#DC143C', alpha=0.6, ha='center', va='center',
            transform=ax.transAxes)

    # Additional diagnostics
    textstr = (f'$E_J/E_C$ = {EJ_EC}  (20$\\times$ below critical)\n'
               f'Gi = {Gi}  (fluctuations ~ mean field)\n'
               f'$L/\\xi_{{GL}}$ = {L_over_xi}  (zero-dimensional limit)\n'
               f'$\\Delta\\phi$ = 2$\\pi$  (phase maximally uncertain)\n'
               f'$\\Delta n$ = 0  (charge quantized)')
    props = dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9)
    ax.text(0.02, 0.02, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom', bbox=props)

    ax.set_xscale('log')
    ax.set_xlabel('$E_J / E_C$', fontsize=14)
    ax.set_ylabel('Phase coherence $\\langle \\cos \\hat{\\phi} \\rangle$', fontsize=13)
    ax.set_title('Josephson Array Phase Diagram\nFramework in Mott Regime',
                 fontsize=14, fontweight='bold')
    ax.set_xlim(0.03, 150)
    ax.set_ylim(-0.05, 1.05)
    ax.legend(loc='center right', fontsize=10, framealpha=0.9)

    save_fig(fig, 4)


# ==============================================================================
# VIS-5: BCS Gradient Speed Bump
# ==============================================================================
def vis5_speed_bump():
    """
    Plot V_KK(tau), E_cond(tau), and V_eff(tau) showing the speed bump
    at tau = 0.2015.
    """
    print("Generating Vis-5: BCS Gradient Speed Bump...")

    fig = plt.figure(figsize=(13, 7))
    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1], wspace=0.35)

    ax_main = fig.add_subplot(gs[0])
    ax_inset = fig.add_subplot(gs[1])

    tau = np.linspace(0.01, 0.35, 500)
    tau_bump = 0.2015

    # V_KK ~ -R_K_model(tau), a NORMALIZED MODEL of the Jensen scalar curvature used purely
    # to SHAPE the speed-bump potential. SX W8 D8 convention pin: there are FOUR distinct
    # scalar-curvature normalizations for the same fold (NOT mutual rescalings):
    #   (i)   this model form  R_K_model = -(1/4)e^{-4t}+2e^{-t}-1/4+(1/2)e^{2t}
    #         -> R(0)=2.000, R(fold)=2.018  [matches the archive "1% above bi-invariant R=2.000"];
    #   (ii)  S52/S53 computed       R_K(0)=4.000, R_K(fold)=4.036288 (bi-invariant max=4);
    #   (iii) S61 Koszul SIGNED      R_K(fold) = -2.018 M_KK^2 (mostly-plus; Lambda_eff=(1/8)R_K) — CANONICAL sign;
    #   (iv)  KB Paper-15 eq-3.70 STRING (3/2)(2e^{2t}-1+8(e^{-t}-e^{-4t})) -> R(0)=1.5 (OCR-garbled; NOT used).
    # The potential shape (bump at tau=0.2015, fold at tau=0.19) is convention-independent.
    # Any standalone CURVATURE figure should cite the SIGNED S61 form (-2.018) with magnitude 2.018 noted.
    def R_K_model(t):
        return -(1.0/4.0) * np.exp(-4*t) + 2.0 * np.exp(-t) - 0.25 + 0.5 * np.exp(2*t)
    R_K = R_K_model  # (local) alias retained for the V_KK shaping below

    V_KK = -R_K(tau)
    # Normalize so it's visible alongside E_cond
    V_KK_norm = V_KK / np.max(np.abs(V_KK)) * 0.5

    # E_cond(tau) — model as peaked near fold
    # BCS condensation energy peaks at van Hove singularity
    # Use a smooth function that peaks near tau_fold
    sigma_BCS = 0.08
    E_cond_tau = E_cond * np.exp(-0.5 * ((tau - tau_fold) / sigma_BCS)**2) / \
                 np.exp(-0.5 * ((tau_fold - tau_fold) / sigma_BCS)**2)

    V_eff = V_KK_norm + E_cond_tau

    # Main panel
    ax_main.plot(tau, V_KK_norm, color='#4169E1', linewidth=2.5,
                 label='$V_{KK}(\\tau)$ (normalized)')
    ax_main.plot(tau, E_cond_tau, color='#DC143C', linewidth=2.5,
                 label='$E_{cond}(\\tau)$')
    ax_main.plot(tau, V_eff, color='#2F4F4F', linewidth=3.0, ls='-',
                 label='$V_{eff} = V_{KK} + E_{cond}$')

    # Mark the speed bump
    ax_main.axvline(tau_bump, color='#B8860B', ls='--', linewidth=1.5, alpha=0.7)
    ax_main.axvline(tau_fold, color='#228B22', ls=':', linewidth=1.5, alpha=0.7)

    # Find V_eff at speed bump location
    idx_bump = np.argmin(np.abs(tau - tau_bump))
    ax_main.plot(tau_bump, V_eff[idx_bump], 's', color='#B8860B', markersize=10,
                 markeredgecolor='black', zorder=5)
    ax_main.annotate(f'Speed bump\n$\\tau$ = {tau_bump}',
                     xy=(tau_bump, V_eff[idx_bump]),
                     xytext=(tau_bump + 0.05, V_eff[idx_bump] + 0.15),
                     fontsize=11, fontweight='bold', color='#B8860B',
                     arrowprops=dict(arrowstyle='->', color='#B8860B', lw=1.5))

    idx_fold = np.argmin(np.abs(tau - tau_fold))
    ax_main.annotate(f'Fold\n$\\tau$ = {tau_fold}',
                     xy=(tau_fold, V_eff[idx_fold]),
                     xytext=(tau_fold - 0.06, V_eff[idx_fold] - 0.18),
                     fontsize=10, color='#228B22',
                     arrowprops=dict(arrowstyle='->', color='#228B22', lw=1.2))

    ax_main.set_xlabel('$\\tau$', fontsize=14)
    ax_main.set_ylabel('Energy [$M_{KK}$]', fontsize=13)
    ax_main.set_title('Modulus Effective Potential\nBCS Speed Bump at $\\tau$ = 0.2015',
                       fontsize=14, fontweight='bold')
    ax_main.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax_main.set_xlim(0.01, 0.35)

    # Inset: Gradient competition
    dtau = tau[1] - tau[0]
    dV_KK = np.gradient(V_KK_norm, dtau)
    dE_cond = np.gradient(E_cond_tau, dtau)
    dV_eff = np.gradient(V_eff, dtau)

    ax_inset.plot(tau, dV_KK, color='#4169E1', linewidth=2.0,
                  label='$dV_{KK}/d\\tau$')
    ax_inset.plot(tau, dE_cond, color='#DC143C', linewidth=2.0,
                  label='$dE_{cond}/d\\tau$')
    ax_inset.plot(tau, dV_eff, color='#2F4F4F', linewidth=2.5, ls='-',
                  label='$dV_{eff}/d\\tau$')

    ax_inset.axvline(tau_bump, color='#B8860B', ls='--', linewidth=1.2, alpha=0.7)
    ax_inset.axhline(0, color='gray', linewidth=0.8, alpha=0.5)

    # Mark the gradient competition ratio
    ax_inset.text(0.05, 0.95, 'Gradient ratio\nat bump: 1.30',
                  transform=ax_inset.transAxes, fontsize=10,
                  verticalalignment='top', fontweight='bold', color='#333333',
                  bbox=dict(boxstyle='round,pad=0.3', facecolor='wheat', alpha=0.85))

    ax_inset.set_xlabel('$\\tau$', fontsize=12)
    ax_inset.set_ylabel('$dV/d\\tau$', fontsize=12)
    ax_inset.set_title('Gradient Competition', fontsize=12)
    ax_inset.legend(loc='lower right', fontsize=8, framealpha=0.9)
    ax_inset.set_xlim(0.05, 0.35)

    save_fig(fig, 5)


# ==============================================================================
# VIS-6: Acoustic E-fold Budget
# ==============================================================================
def vis6_efold_budget():
    """
    Bar chart showing e-fold contributions with threshold line.
    """
    print("Generating Vis-6: Acoustic E-fold Budget...")

    fig, ax = plt.subplots(figsize=(10, 7))

    # E-fold contributions (from document Section 6 table)
    contributions = {
        'Geometric\n(KK shape)': N_e_geom,
        'Sound speed\n(229$\\times$)': N_e_sound,
    }

    labels = list(contributions.keys())
    values = list(contributions.values())
    n_bars = len(labels)

    # Color scheme: dominant contribution highlighted
    colors = ['#4169E1', '#DAA520']
    edge_colors = ['#2F4F4F'] * n_bars

    bars = ax.bar(range(n_bars), values, color=colors, edgecolor=edge_colors,
                  linewidth=1.2, width=0.65, zorder=3)

    # Add value labels on bars
    for bar, val in zip(bars, values):
        if val > 0.01:
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03,
                    f'{val:.2f}', ha='center', va='bottom', fontsize=12,
                    fontweight='bold', color='#2F4F4F')
        else:
            ax.text(bar.get_x() + bar.get_width() / 2, 0.03,
                    f'{val:.2f}', ha='center', va='bottom', fontsize=11,
                    color='#808080')

    # Total bar
    total_x = n_bars + 0.5
    ax.bar(total_x, N_e_total, color='#2F4F4F', edgecolor='black',
           linewidth=1.5, width=0.65, zorder=3)
    ax.text(total_x, N_e_total + 0.03, f'{N_e_total:.2f}',
            ha='center', va='bottom', fontsize=14, fontweight='bold',
            color='#2F4F4F')

    # Threshold line
    ax.axhline(THRESHOLD, color='#DC143C', linewidth=2.5, ls='--', alpha=0.8,
               label=f'Threshold = {THRESHOLD}', zorder=4)
    ax.text(n_bars + 1.2, THRESHOLD + 0.02, f'{THRESHOLD} threshold',
            fontsize=11, color='#DC143C', fontweight='bold', va='bottom')

    # Gap annotation
    gap = GAP  # Use document value directly
    ax.annotate('', xy=(total_x + 0.4, N_e_total),
                xytext=(total_x + 0.4, THRESHOLD),
                arrowprops=dict(arrowstyle='<->', color='#DC143C', lw=2))
    ax.text(total_x + 0.55, (N_e_total + THRESHOLD) / 2,
            f'Gap: {gap:.2f}', fontsize=12, color='#DC143C',
            fontweight='bold', va='center')

    # SX W8 (§8.2 caveat): the sound-speed e-fold count depends on the BLV conformal exponent,
    # which is dimension-dependent. The 3+1D exponent (1/2) gives N_e^sound = 0.5*ln(229.479) = 2.718;
    # the 8D internal-space exponent (1/7) gives (1/7)*ln(229.479) = 0.777 — 3.5x SMALLER. The prior
    # figure showed only the 3+1D number as if settled. Co-plot both to show the open exponent ambiguity.
    N_e_sound_8D = (1.0 / 7.0) * np.log(c_ratio)  # (local) 8D BLV exponent variant (~0.777); archive §8.2 OPEN
    ax.axhline(N_e_geom + N_e_sound_8D, color='#8B0000', linewidth=2.0, ls=':', alpha=0.8,
               zorder=4, label=f'8D-exponent total = {N_e_geom + N_e_sound_8D:.2f}')
    ax.text(total_x - 0.15, N_e_geom + N_e_sound_8D - 0.02,
            f'8D BLV: {N_e_geom + N_e_sound_8D:.2f}', fontsize=9, color='#8B0000',
            fontweight='bold', va='top', ha='center')

    # Missing factors box
    missing_text = ('5 uncomputed corrections (~7% each):\n'
                    '  1. 8D BLV exponent (1/7 vs 1/2)\n'
                    '  2. 32-cell coherent sum\n'
                    '  3. LK overshoot duration\n'
                    '  4. $\\rho(\\tau)$ evolution\n'
                    '  5. Floquet amplification\n\n'
                    f'Exponent ambiguity (§8.2 OPEN):\n'
                    f'  3+1D (1/2): $N_e^{{sound}}$ = {N_e_sound:.3f}\n'
                    f'  8D   (1/7): $N_e^{{sound}}$ = {N_e_sound_8D:.3f}\n\n'
                    'Sound speed dominates 15.7$\\times$\n'
                    'over geometric contribution (3+1D)')
    props = dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9,
                 edgecolor='#B8860B')
    ax.text(0.02, 0.97, missing_text, transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)

    ax.set_xticks(list(range(n_bars)) + [total_x])
    ax.set_xticklabels(labels + ['TOTAL'], fontsize=10)
    ax.set_ylabel('Acoustic e-folds $N_e$', fontsize=13)
    ax.set_title(f'Acoustic E-fold Budget\n{N_e_total:.2f} Total (3+1D), {GAP:.2f} Short of {THRESHOLD} Threshold',
                 fontsize=14, fontweight='bold')
    ax.set_ylim(0, 3.5)
    ax.legend(loc='center right', fontsize=9, framealpha=0.9)  # threshold + 8D-exponent caveat lines

    # Percentage annotations
    for i, (lab, val) in enumerate(zip(labels, values)):
        if val > 0.01:
            pct = val / N_e_total * 100
            ax.text(i, -0.12, f'({pct:.0f}%)', ha='center', fontsize=9,
                    color='#666666')

    save_fig(fig, 6)


# ==============================================================================
# VIS-7: Coherent Quantum Walker
# ==============================================================================
def vis7_quantum_walker():
    """
    Schematic of a single Cooper pair hopping on the 32-cell lattice.
    Shows pair wavefunction spreading across neighboring cells with
    probability cloud.
    """
    print("Generating Vis-7: Coherent Quantum Walker...")

    fig, ax = plt.subplots(figsize=(11, 9))
    ax.set_aspect('equal')

    # Create a 2D hexagonal-like lattice (projection of BCC)
    # 6x6 grid with some offset for visual appeal
    rows, cols = 6, 7
    spacing = 1.0
    nodes = []
    for r in range(rows):
        for c in range(cols):
            x = c * spacing + (r % 2) * 0.5 * spacing
            y = r * spacing * 0.866  # sqrt(3)/2
            nodes.append((x, y))

    nodes = np.array(nodes)
    # Take first 32
    nodes = nodes[:32]
    N = len(nodes)

    # Center
    cx, cy = nodes.mean(axis=0)

    # Draw bonds between nearest neighbors
    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(nodes[i] - nodes[j])
            if d < spacing * 1.15:
                # C^2 bond (nearest)
                ax.plot([nodes[i, 0], nodes[j, 0]],
                        [nodes[i, 1], nodes[j, 1]],
                        color='#DC143C', linewidth=1.0, alpha=0.3, zorder=1)
            elif d < spacing * 1.5:
                # su(2) bond
                ax.plot([nodes[i, 0], nodes[j, 0]],
                        [nodes[i, 1], nodes[j, 1]],
                        color='#4169E1', linewidth=0.5, alpha=0.15, zorder=1)

    # Draw cells as circles
    for i in range(N):
        circle = Circle(nodes[i], 0.18, facecolor='#E8E8E8',
                        edgecolor='#555555', linewidth=0.8, zorder=2)
        ax.add_patch(circle)

    # Choose a central node for the pair wavefunction
    # Find node closest to center
    dists_to_center = np.sqrt((nodes[:, 0] - cx)**2 + (nodes[:, 1] - cy)**2)
    center_idx = np.argmin(dists_to_center)
    pair_pos = nodes[center_idx]

    # Draw wavefunction probability cloud
    # Gaussian-like amplitude centered on pair_pos, extending to neighbors.
    # SX W8: the localization scale is the imported canonical xi_BCS = 0.8083 (S37), the BCS
    # coherence length in cell units (pair < cell -> highly localized). The prior hardcoded 0.506
    # conflated this with the Ginzburg number Gi=0.506 (a DIFFERENT quantity). xi_BCS<1 => localized.
    xi_over_a = float(xi_BCS)  # (local) BCS coherence length / cell (canonical xi_BCS, S37)

    for i in range(N):
        d = np.linalg.norm(nodes[i] - pair_pos)
        # Probability amplitude decreases as exp(-d / (2*xi))
        prob = np.exp(-d / (2.0 * xi_over_a * spacing))
        if prob > 0.01:
            # Draw probability cloud
            alpha_val = min(0.8, prob * 0.9)
            size = 0.15 + prob * 0.2

            if i == center_idx:
                # Central node: bright, large
                cloud = Circle(nodes[i], size,
                               facecolor='#DAA520', edgecolor='#B8860B',
                               linewidth=2.0, alpha=alpha_val, zorder=4)
            else:
                cloud = Circle(nodes[i], size,
                               facecolor='#DAA520', edgecolor='#B8860B',
                               linewidth=1.0, alpha=alpha_val * 0.6, zorder=3)
            ax.add_patch(cloud)

    # Draw Cooper pair symbol at center
    ax.plot(pair_pos[0], pair_pos[1], '*', color='#8B0000', markersize=20,
            markeredgecolor='black', markeredgewidth=0.8, zorder=6)
    ax.text(pair_pos[0], pair_pos[1] - 0.35, '$\\Psi_{pair}$',
            fontsize=12, ha='center', fontweight='bold', color='#8B0000',
            zorder=6)

    # Hopping arrows from center to neighbors
    for i in range(N):
        d = np.linalg.norm(nodes[i] - pair_pos)
        if 0.1 < d < spacing * 1.15:
            dx = nodes[i, 0] - pair_pos[0]
            dy = nodes[i, 1] - pair_pos[1]
            # Shorten arrow
            scale = 0.6
            ax.annotate('', xy=(pair_pos[0] + dx * scale, pair_pos[1] + dy * scale),
                        xytext=(pair_pos[0] + dx * 0.25, pair_pos[1] + dy * 0.25),
                        arrowprops=dict(arrowstyle='->', color='#B8860B',
                                        lw=1.8, alpha=0.7))

    # Legend-style annotations (SX W8 D5: Delta_0_GL now consumed — distinguished from the BCS gap)
    textstr = (f'$N_{{pair}}$ = 1  (exactly)\n'
               f'$\\Gamma/\\omega$ = 0  (infinite coherence)\n'
               f'$\\xi_{{BCS}} / a_{{cell}}$ = {xi_over_a:.3f}  (pair < cell)\n'
               f'$\\Delta_{{0,GL}}$ = {Delta_0_GL:.3f} $M_{{KK}}$  (GL amplitude, $\\neq$ BCS gap)\n'
               f'$\\Delta\\phi$ = 2$\\pi$  (phase uncertain)\n'
               f'$\\Delta n$ = 0  (number certain)\n\n'
               f'4 scattering channels:\n'
               f'  Pair-pair: 0 ($N_{{pair}}$ = 1)\n'
               f'  Impurity: 0 (perfect crystal)\n'
               f'  Umklapp: 0 (single band)\n'
               f'  Phonon emission: 0 (no bath)')
    props = dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.95,
                 edgecolor='#B8860B', linewidth=1.5)
    ax.text(0.98, 0.98, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right', bbox=props)

    # Branch legend
    branch_text = ('Bloch bands:\n'
                   '1 Goldstone + 2 Leggett + 3 Higgs\n'
                   f'$c_{{Gold}}$ = {c_Gold} $M_{{KK}}$')
    ax.text(0.02, 0.02, branch_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='bottom',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8E8FF', alpha=0.9))

    # Color legend for bonds
    ax.plot([], [], color='#DC143C', linewidth=2.0, alpha=0.5,
            label=f'$J_{{C^2}}$ = {J_C2} (dominant)')
    ax.plot([], [], color='#4169E1', linewidth=1.0, alpha=0.4,
            label=f'$J_{{su(2)}}$ = {J_su2}')
    ax.plot([], [], 'o', color='#DAA520', markersize=10, alpha=0.6,
            label='$|\\Psi|^2$ probability')
    ax.legend(loc='lower right', fontsize=10, framealpha=0.9)

    ax.set_xlim(-0.5, cols * spacing + 0.5)
    ax.set_ylim(-0.5, (rows - 1) * spacing * 0.866 + 0.5)
    ax.set_title('Coherent Quantum Walker: $N_{pair}$ = 1 on Crystalline SU(3)',
                 fontsize=14, fontweight='bold', pad=15)
    ax.axis('off')

    save_fig(fig, 7)


# ==============================================================================
#  POST-S47 GEOMETRIC DEEPENING (SX W8 comprehensive expansion)
#  Substrate-first: each figure VISUALIZES a closed/permanent KB result on the
#  SAME substrate geometry (A_K, H_K, D_K). No re-derivation — the canonical
#  values are imported; the figure portrays them.
# ==============================================================================

# Peter-Weyl SU(3) irrep dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2
def _su3_dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2  # (local) Weyl dimension formula


# ==============================================================================
# VIS-8 (E1): 4-Stratum Bottom-20 Partition + tau-Asymmetric Breakdown
# ==============================================================================
def vis8_partition_stability():
    """
    The bottom-20 |lambda| of D_K(tau_fold) partition into a 4-stratum cardinality
    vector (N1,N2,N3,N4) = (2,4,8,6) [§VII.AJ.partition-stability, S87 W11-2, PERMANENT].
    On the Jensen TT-deformation moduli line the partition is STABLE in a window
    [tau_fold + delta_neg, tau_fold + delta_pos] with delta_neg = -0.0750 (negative-side
    anticrossing-swap to (4,2,8,6)) and delta_pos = +0.175 (positive-side stratum-
    coalescence) [§VII.AE, S88 W2-9, PERMANENT]; the 2.33x neg/pos asymmetry is the
    moduli-deformation Level-2 substrate-IS observable.
    """
    print("Generating Vis-8: 4-Stratum Bottom-20 Partition Stability...")

    # Substrate-first: the cardinality vector is a closed structural result (integer strata).
    strata = [2, 4, 8, 6]              # (local) (N1,N2,N3,N4) §VII.AJ at tau_fold (PERMANENT)
    strata_swap = [4, 2, 8, 6]         # (local) negative-side anticrossing-swap (strata 1<->2)
    stratum_labels = ['Stratum 1\n(deepest)', 'Stratum 2', 'Stratum 3\n(densest)', 'Stratum 4']  # (local)
    stratum_colors = ['#8B0000', '#DC143C', '#DAA520', '#4169E1']  # (local)
    assert sum(strata) == 20, "bottom-20 partition must sum to 20"  # structural check

    fig = plt.figure(figsize=(14, 6))
    gs = gridspec.GridSpec(1, 2, width_ratios=[1.1, 1.4], wspace=0.30)
    ax_bar = fig.add_subplot(gs[0])
    ax_mod = fig.add_subplot(gs[1])

    # --- Left: the 4-stratum partition bar at tau_fold ---
    xs = np.arange(4)
    bars = ax_bar.bar(xs, strata, color=stratum_colors, edgecolor='#2F4F4F',
                      linewidth=1.4, width=0.66, zorder=3)
    for b, n in zip(bars, strata):
        ax_bar.text(b.get_x() + b.get_width() / 2, n + 0.15, str(n),
                    ha='center', va='bottom', fontsize=15, fontweight='bold', color='#2F4F4F')
    ax_bar.set_xticks(xs)
    ax_bar.set_xticklabels(stratum_labels, fontsize=9)
    ax_bar.set_ylabel('Cardinality $N_i$ (bottom-20 $|\\lambda|$ of $D_K$)', fontsize=12)
    ax_bar.set_title(f'Bottom-20 Partition at $\\tau_{{fold}}$ = {tau_fold}\n'
                     f'$(N_1,N_2,N_3,N_4)$ = (2, 4, 8, 6)', fontsize=13, fontweight='bold')
    ax_bar.set_ylim(0, 9.5)
    ax_bar.text(0.5, 0.95, 'Friedrich-Bär saturated\n(L_max=6 Casimir bound)',
                transform=ax_bar.transAxes, fontsize=8.5, ha='center', va='top', style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#EFEFEF', alpha=0.85))

    # --- Right: the tau-asymmetric stability window on the moduli line ---
    d_neg = float(delta_tau_crit_neg)  # (local) -0.0750
    d_pos = float(delta_tau_crit_pos)  # (local) +0.175
    tlo, thi = tau_fold + d_neg, tau_fold + d_pos
    # stable window shaded; breakdown edges marked
    ax_mod.axvspan(tlo, thi, alpha=0.16, color='#DAA520', zorder=1,
                   label=f'(2,4,8,6) stable window\n$\\delta_-$={d_neg:.4f}, $\\delta_+$={d_pos:.3f}')
    ax_mod.axvline(tau_fold, color='#228B22', ls=':', linewidth=1.8, alpha=0.85, zorder=3)
    ax_mod.axvline(tlo, color='#8B0000', ls='--', linewidth=1.8, alpha=0.85, zorder=3)
    ax_mod.axvline(thi, color='#4169E1', ls='--', linewidth=1.8, alpha=0.85, zorder=3)

    # annotate the breakdown geometries
    ax_mod.text(tlo - 0.012, 0.78, 'neg-side\nanticrossing-swap\n$\\to$ (4,2,8,6)',
                transform=ax_mod.get_xaxis_transform(), fontsize=8.5, color='#8B0000',
                ha='right', va='center', fontweight='bold')
    ax_mod.text(thi + 0.012, 0.78, 'pos-side\nstratum-\ncoalescence',
                transform=ax_mod.get_xaxis_transform(), fontsize=8.5, color='#4169E1',
                ha='left', va='center', fontweight='bold')
    ax_mod.text(tau_fold, 0.06, f'$\\tau_{{fold}}$\n{tau_fold}',
                transform=ax_mod.get_xaxis_transform(), fontsize=9, color='#228B22',
                ha='center', va='bottom', fontweight='bold')

    # asymmetry arrow
    asym = abs(d_pos) / abs(d_neg)  # (local) 2.33x
    ax_mod.annotate('', xy=(thi, 0.5), xytext=(tlo, 0.5),
                    xycoords=ax_mod.get_xaxis_transform(),
                    arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.4))
    ax_mod.text((tlo + thi) / 2, 0.55, f'{asym:.2f}$\\times$ asymmetry\n(|$\\delta_+$|/|$\\delta_-$|)',
                transform=ax_mod.get_xaxis_transform(), fontsize=9, ha='center', va='bottom',
                color='#555555', fontweight='bold')

    ax_mod.set_xlim(tau_fold - 0.13, tau_fold + 0.23)
    ax_mod.set_ylim(0, 1)
    ax_mod.set_yticks([])
    ax_mod.set_xlabel('$\\tau$ (Jensen TT-deformation moduli line)', fontsize=12)
    ax_mod.set_title('Moduli-Deformation $\\tau$-Asymmetry (Level-2 substrate-IS)\n'
                     '§VII.AE: partition stability window', fontsize=13, fontweight='bold')
    ax_mod.legend(loc='upper center', fontsize=8.5, framealpha=0.9)

    fig.suptitle('4-Stratum Bottom-20 Partition Stability of $D_K$ on Jensen SU(3)',
                 fontsize=14, fontweight='bold', y=1.02)
    save_fig(fig, 8)


# ==============================================================================
# VIS-9 (E2): Spectral-Moment Landscape a_n(tau) + Protected Ratio R_1 + R-Monotonicity
# ==============================================================================
def vis9_spectral_moment_landscape():
    """
    The Seeley-DeWitt spectral-action moments a_0, a_2, a_4 vary along the Jensen line,
    but the protected dimensionless ratio R_1 = a_0 a_4 / a_2^2 is L_max-invariant
    (Weyl exponents cancel; R_protected_fold = 1.1287 at tau_fold) [S73B/S74, R-PROTECTED].
    The scalar curvature is monotone: dR_K/dtau >= 0 by AM-GM on the volume-preserving
    Jensen deformation [S64 W1-A, PROVEN; closes CC Path C]. CHAIN 1 (det g_tau = 1) holds
    throughout: the moments MOVE while the volume does NOT.
    """
    print("Generating Vis-9: Spectral-Moment Landscape + Protected Ratio...")

    fig, (ax_R, ax_a) = plt.subplots(1, 2, figsize=(14, 6))

    tau = np.linspace(0.01, 0.35, 400)  # (local) archive vis5 tau range

    # --- Scalar curvature R_K(tau) on the Jensen line (the SIGNED/positive-magnitude form;
    #     same model curvature as vis5, monotone-increasing per S64 W1-A R-monotonicity) ---
    def R_K_model(t):
        return -(1.0/4.0) * np.exp(-4*t) + 2.0 * np.exp(-t) - 0.25 + 0.5 * np.exp(2*t)  # (local)
    RK = R_K_model(tau)
    dRK = np.gradient(RK, tau[1] - tau[0])  # (local) dR_K/dtau (>= 0 expected)

    ax_R.plot(tau, RK, color='#8B0000', linewidth=2.6, label='$R_K(\\tau)$ (model curvature)')
    ax_R.axvline(tau_fold, color='#228B22', ls=':', linewidth=1.6, alpha=0.8)
    # mark fold value
    RK_fold = R_K_model(tau_fold)  # (local)
    ax_R.plot(tau_fold, RK_fold, 'o', color='#228B22', markersize=10,
              markeredgecolor='black', zorder=5)
    ax_R.annotate(f'fold: $R_K$ = {RK_fold:.3f}\n($\\tau$ = {tau_fold})',
                  xy=(tau_fold, RK_fold), xytext=(tau_fold + 0.04, RK_fold - 0.5),
                  fontsize=9.5, color='#228B22', fontweight='bold',
                  arrowprops=dict(arrowstyle='->', color='#228B22', lw=1.3))
    # twin axis for dR/dtau >= 0
    ax_R2 = ax_R.twinx()
    ax_R2.plot(tau, dRK, color='#4169E1', linewidth=1.8, ls='--', alpha=0.8,
               label='$dR_K/d\\tau$')
    ax_R2.axhline(0, color='gray', linewidth=0.7, alpha=0.5)
    ax_R2.set_ylabel('$dR_K/d\\tau$  ($\\geq 0$: R-monotonicity, S64 W1-A)', fontsize=11, color='#4169E1')
    ax_R2.tick_params(axis='y', labelcolor='#4169E1')
    ax_R.set_xlabel('$\\tau$', fontsize=13)
    ax_R.set_ylabel('$R_K(\\tau)$  [model curvature units]', fontsize=12, color='#8B0000')
    ax_R.tick_params(axis='y', labelcolor='#8B0000')
    ax_R.set_title('Scalar Curvature is Monotone\n$dR_K/d\\tau \\geq 0$ (AM-GM, volume-preserving)',
                   fontsize=13, fontweight='bold')
    ax_R.set_xlim(0.01, 0.35)
    # combined legend
    l1, lab1 = ax_R.get_legend_handles_labels()
    l2, lab2 = ax_R2.get_legend_handles_labels()
    ax_R.legend(l1 + l2, lab1 + lab2, loc='upper left', fontsize=9, framealpha=0.9)

    # --- Right: the protected ratio R_1 = a_0 a_4 / a_2^2 (constant in L_max) + moment bars ---
    # The canonical moments at the fold (S64 W1-A): a0_fold, a2_fold, a4_fold (imported).
    R1 = a0_fold * a4_fold / a2_fold**2  # (local) = R_protected_fold exactly
    # show R_1 as a flat protected line vs L_max (schematic: L_max-invariance, drift 0.34%)
    Lmax_axis = np.array([3, 5, 7, 9, 12])  # (local) the L_max scan axis (S74 drift <0.34%)
    R1_band = R1 * np.ones_like(Lmax_axis, dtype=float)  # (local) L^0 protected -> flat
    ax_a.axhspan(R1 * (1 - 0.0034), R1 * (1 + 0.0034), alpha=0.18, color='#DAA520',
                 label='$\\pm$0.34% drift band (S74)')
    ax_a.plot(Lmax_axis, R1_band, 'o-', color='#B8860B', linewidth=2.4, markersize=9,
              markeredgecolor='black', zorder=4, label='$R_1 = a_0 a_4 / a_2^2$ (L-invariant)')
    ax_a.axhline(float(R_protected_fold), color='#8B0000', ls=':', linewidth=1.4, alpha=0.7)
    ax_a.text(12, float(R_protected_fold) + 0.004,
              f'$R_{{protected,fold}}$ = {float(R_protected_fold):.4f}',
              fontsize=10, color='#8B0000', ha='right', fontweight='bold')

    # inset bar of the three moments at the fold (log scale; different mass dimensions).
    # Use NUMERIC x-positions + set_xticklabels (avoids the matplotlib categorical-converter
    # ConversionError that fires on string-x + log=True inside an inset axis).
    ax_a_in = ax_a.inset_axes([0.10, 0.10, 0.40, 0.42])
    mvals = [a0_fold, a2_fold, a4_fold]  # (local)
    mcolors = ['#4169E1', '#228B22', '#DC143C']  # (local)
    mx = np.arange(3)  # (local) numeric bar positions
    ax_a_in.bar(mx, mvals, color=mcolors, edgecolor='#2F4F4F', linewidth=1.0, log=True)
    ax_a_in.set_xticks(mx)
    ax_a_in.set_xticklabels(['$a_0$', '$a_2$', '$a_4$'])
    ax_a_in.set_title('SDW moments at fold (S64)', fontsize=8)
    ax_a_in.tick_params(labelsize=7)
    for i, v in enumerate(mvals):
        ax_a_in.text(i, v * 1.3, f'{v:.0f}', ha='center', fontsize=7, color='#2F4F4F')

    ax_a.set_xlabel('$L_{max}$ (spectral truncation)', fontsize=12)
    ax_a.set_ylabel('Protected ratio $R_1 = a_0 a_4 / a_2^2$', fontsize=12)
    ax_a.set_title('Protected Spectral-Action Ratio\n$R_1$ is $L_{max}$-invariant ($L^0$ Weyl cancellation)',
                   fontsize=13, fontweight='bold')
    ax_a.set_xlim(2, 13)
    ax_a.set_ylim(R1 * 0.985, R1 * 1.015)
    ax_a.legend(loc='upper right', fontsize=9, framealpha=0.9)

    fig.suptitle('Spectral-Moment Landscape: Moments Move, Volume + $R_1$ Protected '
                 '(det $g_\\tau$ = 1)', fontsize=14, fontweight='bold', y=1.01)
    # Explicit margins (avoids the tight_layout warning from the twin-axis y-label on the left panel).
    fig.subplots_adjust(left=0.08, right=0.93, top=0.86, bottom=0.12, wspace=0.32)
    save_fig(fig, 9)


# ==============================================================================
# VIS-10 (E3): Spectral-Dimension Flow d_s(sigma) on the Jensen D_K Spectrum vs CDT
# ==============================================================================
def vis10_spectral_dimension_flow():
    """
    The spectral dimension d_s(sigma) = -2 d ln P(sigma)/d ln sigma, with heat trace
    P(sigma) = Sum_{states} exp(-sigma lambda^2) over the Jensen-deformed SU(3) D_K
    NORMAL-STATE (Delta=0) spectrum [S92 ad-hoc]. UV (sigma -> 0): d_s -> 8 (Weyl;
    dim SU(3) = 8). Fold window sigma_* = 1.4005 M_KK^-2. The CDT reference flows 4 -> 2;
    per the same-functional-different-scale fair-comparison rule (phononic-framing.md
    AH-PF-1), the substrate d_s and CDT d_s are the SAME functional Phi applied to
    DIFFERENT P(sigma) on DIFFERENT spectra — they are NOT summand-matched.

    Substrate-first: the D_K spectrum is LOADED from the L_max=12 tau_fold master cache
    (s84_spectrum_cache_L12_tau019.npz), NOT re-diagonalized; abs_evals already carry the
    full Peter-Weyl multiplicity (16*dim(p,q) per sector), so the heat trace sums e^{-s|lam|^2}
    over the flattened eigenvalue list WITHOUT an extra dim weight (verified SX W8).
    """
    print("Generating Vis-10: Spectral-Dimension Flow d_s(sigma) vs CDT...")

    cache_path = os.path.join(os.path.dirname(__file__), '..', '..',
                              'computations', 'session-84', 's84_spectrum_cache_L12_tau019.npz')
    cache_path = os.path.abspath(cache_path)

    # --- Load and flatten the Jensen D_K spectrum (|lambda| values, multiplicity included) ---
    fig, ax = plt.subplots(figsize=(11, 7.5))
    if os.path.exists(cache_path):
        cache = np.load(cache_path, allow_pickle=True)
        se = cache['sector_evals'].item()
        abs_evals = np.concatenate([np.asarray(rec['abs_evals'], dtype=float)
                                    for rec in se.values()])  # (local) all |lambda|, mult included
        lam2 = abs_evals**2  # (local) lambda^2 for the heat trace
        n_states = lam2.size  # (local)
        cache_label = f'L_max=12 master cache ({n_states} states, $\\tau_{{fold}}$={tau_fold})'  # (local)

        # heat trace P(sigma) = sum exp(-sigma lambda^2), and d_s = -2 dlnP/dln sigma
        sigma = np.logspace(-2.5, 1.8, 400)  # (local) diffusion-time log grid (M_KK^-2)
        # GPU path: P(sigma) is a (n_sigma x n_states) reduction; use torch on the matrix if available.
        try:
            import torch  # (local) GPU venv torch (2.9.1+rocm)
            dev = 'cuda' if torch.cuda.is_available() else 'cpu'  # (local)
            s_t = torch.tensor(sigma, device=dev, dtype=torch.float64).reshape(-1, 1)  # (local)
            l_t = torch.tensor(lam2, device=dev, dtype=torch.float64).reshape(1, -1)  # (local)
            P_t = torch.exp(-s_t * l_t).sum(dim=1)  # (local) (n_sigma,)
            P = P_t.cpu().numpy()  # (local)
            backend = f'torch.linalg/{dev}'  # (local)
        except Exception:
            P = np.array([np.sum(np.exp(-s * lam2)) for s in sigma])  # (local) CPU fallback
            backend = 'numpy-cpu-fallback'  # (local)
        lnP = np.log(P)  # (local)
        lns = np.log(sigma)  # (local)
        d_s = -2.0 * np.gradient(lnP, lns)  # (local) the spectral dimension functional Phi

        ax.plot(sigma, d_s, color='#8B0000', linewidth=2.8, zorder=4,
                label=f'$d_s(\\sigma)$ substrate $D_K$ [{cache_label}]')
        # CONTINUUM Weyl limit d_s -> 8 (dim SU(3)): this is the L_max -> infinity, GAPLESS
        # asymptote — NOT the sigma->0 value of the FINITE gapped cache (which plateaus at the
        # finite count, d_s->0, since P(sigma->0)->N_states is constant). Honest labelling per
        # the same-functional-different-scale rule: the cache shows the WINDOWED d_s, the Weyl
        # 8 is the untruncated-operator continuum statement.
        ax.axhline(8.0, color='#B8860B', ls=':', linewidth=1.6, alpha=0.85,
                   label='continuum Weyl limit $d_s \\to 8$ ($L_{max}\\to\\infty$, gapless)')
        lam_min2 = float(lam2.min())  # (local) gap^2 = |lambda|_min^2 (B1 mode); sets the IR blow-up
        # fold window
        ax.axvline(float(d_s_fold_window_sigma), color='#228B22', ls='--', linewidth=1.8,
                   alpha=0.85, label=f'fold window $\\sigma_*$ = {float(d_s_fold_window_sigma)} $M_{{KK}}^{{-2}}$')
        # mark d_s at the fold window (the physically meaningful WINDOWED spectral dimension)
        idx_star = int(np.argmin(np.abs(sigma - float(d_s_fold_window_sigma))))  # (local)
        ds_star = d_s[idx_star]  # (local)
        ax.plot(sigma[idx_star], ds_star, 'o', color='#228B22', markersize=11,
                markeredgecolor='black', zorder=6)
        ax.annotate(f'windowed $d_s(\\sigma_*)$ = {ds_star:.2f}', xy=(sigma[idx_star], ds_star),
                    xytext=(sigma[idx_star] * 0.18, ds_star + 1.3), fontsize=10,
                    color='#228B22', fontweight='bold',
                    arrowprops=dict(arrowstyle='->', color='#228B22', lw=1.3))
        # annotate the two finite-cache regimes (honest structure-first reading)
        ax.text(sigma[2] * 1.1, d_s[2] + 0.6, 'finite-cache\ncount plateau\n($d_s\\to0$ as $P\\to N$)',
                fontsize=8, color='#777777', style='italic', va='bottom')
        ax.text(sigma[-30], min(d_s[-30], 9.0), 'gap blow-up\n($d_s{=}2\\sigma|\\lambda|_{min}^2$)',
                fontsize=8, color='#777777', style='italic', ha='right', va='top')
        backend_note = backend  # (local)
    else:
        ax.text(0.5, 0.5, f'spectrum cache not found:\n{cache_path}', transform=ax.transAxes,
                ha='center', va='center', fontsize=11, color='#8B0000')
        backend_note = 'cache-missing'  # (local)

    # CDT reference flow 4 -> 2 (same functional, different spectrum/scale-type — fair-comparison rule)
    sig_cdt = np.logspace(-2.5, 1.8, 200)  # (local)
    # schematic CDT interpolation 4 (IR) -> 2 (UV): d_s^CDT(sigma) = 2 + 2/(1 + (sigma0/sigma))
    sigma0 = 0.3  # (local) CDT crossover (schematic; reference only)
    d_s_cdt = 2.0 + 2.0 / (1.0 + (sigma0 / sig_cdt))  # (local) reference curve, NOT substrate
    ax.plot(sig_cdt, d_s_cdt, color='#4169E1', linewidth=2.0, ls='-.', alpha=0.8, zorder=3,
            label='CDT reference $d_s$: 4 $\\to$ 2 (different spectrum; same $\\Phi$)')

    ax.set_xscale('log')
    ax.set_xlabel('diffusion time $\\sigma$  [$M_{KK}^{-2}$]', fontsize=13)
    ax.set_ylabel('spectral dimension $d_s(\\sigma) = -2\\, d\\ln P/d\\ln\\sigma$', fontsize=13)
    ax.set_title('Spectral-Dimension Flow of $D_K$ on Jensen SU(3) vs CDT\n'
                 '(same functional $\\Phi$, different spectra — fair-comparison rule)',
                 fontsize=13, fontweight='bold')
    ax.set_ylim(0, 9.5)
    ax.legend(loc='lower right', fontsize=9, framealpha=0.92)
    ax.text(0.02, 0.03, 'Substrate IS the heat trace $P(\\sigma)=\\mathrm{Tr}\\,e^{-\\sigma D_K^2}$;\n'
            '$d_s(\\sigma{\\to}0){=}8$ (Weyl) and $d_s(\\sigma_*)$ are two intrinsic functionals of it.',
            transform=ax.transAxes, fontsize=8.5, style='italic', va='bottom',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#EFEFEF', alpha=0.85))
    print(f"  [Vis-10 heat-trace backend: {backend_note}]")
    save_fig(fig, 10)


# ==============================================================================
# VIS-11 (E4): Cross-Pillar Bridge Geometry (substrate-IS Hochschild -> lab-IN quantum metric)
# ==============================================================================
def vis11_bridge_geometry():
    """
    The framework's flagship cross-pillar bridge [§VII.W, S86; R_canonical, S89 W2]:
    a substrate-IS Hochschild pairing R_universal = <[phi_g^sym], [Ch(P_0(tau_fold))]>
    on the finite spectral triple (A_K, H_K, D_K) maps, via the HKR / Connes-Karoubi
    image (L_max -> infinity), to a laboratory-IN continuum quantum-metric trace
    R_geom = Integral_BZ Tr g_ab(k) d^d k (Peotta-Törmä). The cocycle-norm ratio
    R_canonical = phi_67/phi_88 = 7.3250 is the substrate-IS invariant that survives.
    Direction (phononic-framing.md IS-not-IN): SUBSTRATE IS the cocycle pairing ->
    bridge map -> LABORATORY measures the quantum-metric trace. Never inverted.
    """
    print("Generating Vis-11: Cross-Pillar Bridge Geometry...")

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Three boxes: SUBSTRATE-IS (left) -> BRIDGE MAP (center) -> LABORATORY-IN (right)
    from matplotlib.patches import FancyBboxPatch
    box_sub = FancyBboxPatch((0.3, 2.0), 3.4, 4.0, boxstyle='round,pad=0.1',
                             facecolor='#FBE9E7', edgecolor='#8B0000', linewidth=2.0, zorder=2)
    box_brg = FancyBboxPatch((4.4, 2.7), 3.2, 2.6, boxstyle='round,pad=0.1',
                             facecolor='#FFF8E1', edgecolor='#B8860B', linewidth=2.0, zorder=2)
    box_lab = FancyBboxPatch((8.3, 2.0), 3.4, 4.0, boxstyle='round,pad=0.1',
                             facecolor='#E8F0FE', edgecolor='#4169E1', linewidth=2.0, zorder=2)
    for b in (box_sub, box_brg, box_lab):
        ax.add_patch(b)

    # SUBSTRATE-IS content
    ax.text(2.0, 5.6, 'SUBSTRATE — IS', fontsize=12, fontweight='bold', color='#8B0000', ha='center')
    ax.text(2.0, 4.85, '(Pillar III)', fontsize=9, color='#8B0000', ha='center', style='italic')
    ax.text(2.0, 4.1, 'finite spectral triple\n$(A_K, H_K, D_K)$', fontsize=10, ha='center')
    ax.text(2.0, 3.15, '$R_{universal}$ =\n$\\langle[\\phi_g^{sym}],[\\mathrm{Ch}(P_0(\\tau_{fold}))]\\rangle$',
            fontsize=9.5, ha='center', color='#8B0000')
    ax.text(2.0, 2.35, 'Hochschild cocycle\n$\\times$ Chern character', fontsize=8.5, ha='center', style='italic')

    # BRIDGE MAP
    ax.text(6.0, 4.85, 'BRIDGE MAP', fontsize=11, fontweight='bold', color='#B8860B', ha='center')
    ax.text(6.0, 4.15, 'HKR /\nConnes-Karoubi\npairing', fontsize=9.5, ha='center', color='#8B6914')
    ax.text(6.0, 3.15, '$L_{max} \\to \\infty$\n($L^{-3}$ envelope)', fontsize=9, ha='center', style='italic')

    # LABORATORY-IN content
    ax.text(10.0, 5.6, 'LABORATORY — IN', fontsize=12, fontweight='bold', color='#4169E1', ha='center')
    ax.text(10.0, 4.85, '(Pillar IV)', fontsize=9, color='#4169E1', ha='center', style='italic')
    ax.text(10.0, 4.1, 'continuum BZ-trace\n(Peotta-Törmä)', fontsize=10, ha='center')
    ax.text(10.0, 3.15, '$R_{geom}$ =\n$\\int_{BZ}\\mathrm{Tr}\\,g_{ab}(k)\\,d^dk$',
            fontsize=9.5, ha='center', color='#4169E1')
    ax.text(10.0, 2.35, 'quantum-metric\nintegrated trace', fontsize=8.5, ha='center', style='italic')

    # Arrows: substrate -> bridge -> lab (the direction is fixed, never inverted)
    ax.annotate('', xy=(4.35, 4.0), xytext=(3.75, 4.0),
                arrowprops=dict(arrowstyle='-|>', color='#555555', lw=2.4))
    ax.annotate('', xy=(8.25, 4.0), xytext=(7.65, 4.0),
                arrowprops=dict(arrowstyle='-|>', color='#555555', lw=2.4))

    # The surviving substrate-IS invariant
    ax.text(6.0, 1.2, f'Surviving substrate-IS invariant:  '
            f'$R_{{canonical}}$ = $\\|\\phi_{{67}}\\|/\\|\\phi_{{88}}\\|$ = {float(R_canonical_bridge):.4f}',
            fontsize=11, ha='center', fontweight='bold', color='#2F4F4F',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#DAA520', alpha=0.35,
                      edgecolor='#B8860B'))
    ax.text(6.0, 0.45, 'Direction (IS-not-IN): the substrate IS the cocycle pairing; '
            'the bridge maps it to what the laboratory measures. Never inverted.',
            fontsize=8.5, ha='center', style='italic', color='#555555')

    ax.text(6.0, 7.4, 'Cross-Pillar Bridge Geometry: Substrate-IS Hochschild Pairing '
            '$\\to$ Laboratory-IN Quantum Metric',
            fontsize=13, fontweight='bold', ha='center')
    ax.text(6.0, 6.85, '§VII.W (S86, first registered cross-pillar bridge) · '
            '$R_{canonical}$ (S89 W2, Hochschild $\\times$ Chern)',
            fontsize=9, ha='center', color='#666666', style='italic')

    save_fig(fig, 11)


# ==============================================================================
# Main
# ==============================================================================
if __name__ == '__main__':
    print("=" * 60)
    print("Phononic Crystal Geometry — Visualization Suite")
    print("=" * 60)
    print(f"Output directory: {OUT_DIR}")
    print(f"Key constants: tau_fold={tau_fold}, c_fabric={c_fabric:.2f}, "
          f"c_Gold={c_Gold}, J_C2={J_C2}")
    print()

    # Vis 1-7: S47/S53 crystal-layer core, brought to current canonical values.
    vis1_voronoi_tessellation()
    vis2_band_structure()
    vis3_sound_speed_hierarchy()
    vis4_mott_phase_diagram()
    vis5_speed_bump()
    vis6_efold_budget()
    vis7_quantum_walker()

    # Vis 8-11: post-S47 geometric deepening (SX W8 expansion; substrate-first).
    vis8_partition_stability()
    vis9_spectral_moment_landscape()
    vis10_spectral_dimension_flow()
    vis11_bridge_geometry()

    print()
    print("=" * 60)
    print("All 11 visualizations generated successfully (7 core + 4 post-S47).")
    print("=" * 60)
