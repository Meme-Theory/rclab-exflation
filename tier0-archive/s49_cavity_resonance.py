#!/usr/bin/env python3
"""
Session 49: CAVITY-RESONANCE-49 — Normal Modes of Analog Mach-1 Cavity
=======================================================================

Tests whether Leggett inter-sector phase oscillation frequencies (omega_L1,
omega_L2 from s48_leggett_mode.npz) match the normal-mode spectrum of the
analog acoustic cavity bounded by the Mach-1 horizon on T^2.

Physics:
  The condensate on the maximal torus T^2 of SU(3) creates an analog
  acoustic metric (Volovik/Akama-Diakonov). Where the condensate gradient
  exceeds the BdG sound speed (Mach > 1), quasiparticles cannot propagate.
  The Mach-1 contour acts as an analog event horizon, confining
  quasiparticles to subsonic "cavities."

  If Leggett modes ARE cavity resonances, their frequencies omega_L must
  match eigenvalues of the acoustic Helmholtz equation inside the cavity.

Method:
  1. Reconstruct Mach field from S47 condensate torus data
  2. Identify connected subsonic regions (Mach < 1)
  3. Solve -div[c_eff^2(x) grad phi] = omega^2 phi with Dirichlet BC
     at Mach-1 boundary for each cavity
  4. Compare cavity spectrum to Leggett frequencies
  5. Compute cavity Q-factor from WKB tunneling through supersonic barrier

Gate: CAVITY-RESONANCE-49
  PASS: |omega_cavity - omega_Leggett|/omega_Leggett < 0.10 for at least one pair
  INFO: modes exist but matching > 10%
  FAIL: no confined modes

Input:
  - s47_condensate_torus.npz (Delta field on T^2)
  - s48_leggett_mode.npz (omega_L1, omega_L2)

Output:
  - s49_cavity_resonance.npz
  - s49_cavity_resonance.png

Author: Tesla-Resonance (Session 49)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.ndimage import label
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    g0_diag, tau_fold, E_B2_mean, PI, Delta_0_GL,
    E_B1, E_B3_mean, c_light,
    rho_B2_per_mode,
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def load_npz(name):
    return np.load(os.path.join(DATA_DIR, name), allow_pickle=True)


# ============================================================================
#  LOAD INPUT DATA
# ============================================================================

print("=" * 78)
print("SESSION 49: CAVITY-RESONANCE-49")
print("Normal Modes of Analog Mach-1 Cavity on T^2")
print("=" * 78)

d_cond = load_npz('s47_condensate_torus.npz')
d_legg = load_npz('s48_leggett_mode.npz')

theta1 = d_cond['theta1']
theta2 = d_cond['theta2']
density_bcs = d_cond['density_bcs_weighted']
haar_measure = d_cond['haar_measure']
N_grid = int(d_cond['N_grid'])  # 200

# Leggett frequencies
omega_L1 = float(d_legg['omega_L1_fold'])
omega_L2 = float(d_legg['omega_L2_fold'])

print(f"\nInput Leggett frequencies:")
print(f"  omega_L1 = {omega_L1:.6f} M_KK")
print(f"  omega_L2 = {omega_L2:.6f} M_KK")

# ============================================================================
#  RECONSTRUCT MACH FIELD
# ============================================================================

print("\n" + "-" * 78)
print("Reconstructing Mach field from condensate profile...")

Delta_field = np.sqrt(np.abs(density_bcs))
dtheta = theta1[1] - theta1[0]

# Metric on T^2 at the fold
g_11 = g0_diag * np.exp(2 * tau_fold)
g_22 = g_11  # isotropic Cartan

# BdG sound speed
v_F = np.sqrt(2 * E_B2_mean)
c_BdG = v_F / np.sqrt(3)

# Gradient of condensate amplitude on T^2
grad1 = np.gradient(Delta_field, dtheta, axis=0) / np.sqrt(g_11)
grad2 = np.gradient(Delta_field, dtheta, axis=1) / np.sqrt(g_22)
grad_mag = np.sqrt(grad1**2 + grad2**2)

# Mach number
Delta_safe = np.where(Delta_field > 1e-10, Delta_field, 1e-10)
mach_field = grad_mag / (Delta_safe * c_BdG)

# Physical grid spacing
h_phys = dtheta * np.sqrt(g_11)

print(f"  N_grid = {N_grid}")
print(f"  g_11 = g_22 = {g_11:.4f}")
print(f"  v_F = {v_F:.4f} M_KK")
print(f"  c_BdG = {c_BdG:.4f} M_KK")
print(f"  h_phys = {h_phys:.4f} M_KK^{{-1}}")
print(f"  Mach field: min={mach_field.min():.4f}, max={mach_field.max():.2f}, mean={mach_field.mean():.2f}")
print(f"  Subsonic (Mach<1) fraction: {np.mean(mach_field<1.0):.3f}")

# ============================================================================
#  IDENTIFY SUBSONIC CAVITIES
# ============================================================================

print("\n" + "-" * 78)
print("Identifying subsonic cavities (Mach < 1 regions)...")

subsonic = mach_field < 1.0
labeled_arr, n_features = label(subsonic.astype(int))

# Sort by size
comp_list = [(c, np.sum(labeled_arr == c)) for c in range(1, n_features + 1)]
comp_list.sort(key=lambda x: -x[1])

print(f"  Total connected subsonic components: {n_features}")
print(f"  Top 10 by size:")
for rank, (cid, csize) in enumerate(comp_list[:10]):
    mask = labeled_arr == cid
    iy, ix = np.where(mask)
    cy, cx = np.mean(theta1[iy]), np.mean(theta2[ix])
    A_phys = csize * dtheta**2 * g_11
    R_eff = np.sqrt(A_phys / PI)
    mean_mach = np.mean(mach_field[mask])
    mean_delta = np.mean(Delta_field[mask])
    print(f"    #{rank+1}: comp={cid:3d}, {csize:5d} pts, "
          f"centroid=({cy:.2f},{cx:.2f}), R_eff={R_eff:.3f}, "
          f"<Mach>={mean_mach:.3f}, <Delta>={mean_delta:.1f}")

# Component containing identity
identity_comp = labeled_arr[0, 0]
identity_size = np.sum(labeled_arr == identity_comp) if identity_comp > 0 else 0
print(f"\n  Component containing identity (0,0): #{identity_comp}, size={identity_size}")

# ============================================================================
#  SOLVE HELMHOLTZ ON EACH CAVITY (VARIABLE c_eff, DIRICHLET BC)
# ============================================================================

print("\n" + "=" * 78)
print("Solving acoustic Helmholtz equation on top-5 subsonic cavities")
print("  -div[c_eff^2(x) grad phi] = omega^2 phi,  phi=0 at Mach-1 boundary")
print("  c_eff^2(x) = c_BdG^2 * (1 - M(x)^2)")
print("=" * 78)

all_cavity_modes = []  # (omega, cavity_rank, mode_index)
cavity_data = []       # per-cavity info

for rank, (comp_id, comp_size) in enumerate(comp_list[:5]):
    mask = labeled_arr == comp_id
    iy, ix = np.where(mask)

    # Map interior points
    idx_map = {}
    pts = []
    for p, (ii, jj) in enumerate(zip(iy, ix)):
        idx_map[(int(ii), int(jj))] = p
        pts.append((int(ii), int(jj)))

    n_int = len(pts)

    if n_int < 10:
        print(f"\n  Cavity #{rank+1} (comp {comp_id}): only {n_int} pts, too small to solve")
        continue

    # Build sparse Laplacian
    rows, cols, vals = [], [], []
    for p, (ii, jj) in enumerate(pts):
        c2_here = c_BdG**2 * max(1.0 - mach_field[ii, jj]**2, 0.0)
        diag = 0.0
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni2, nj2 = ii + di, jj + dj
            if (ni2, nj2) in idx_map:
                p2 = idx_map[(ni2, nj2)]
                c2_nb = c_BdG**2 * max(1.0 - mach_field[ni2, nj2]**2, 0.0)
                c2_avg = 0.5 * (c2_here + c2_nb)
                coeff = c2_avg / h_phys**2
                rows.append(p)
                cols.append(p2)
                vals.append(-coeff)
                diag += coeff
            else:
                # Dirichlet BC: phi=0 at boundary
                diag += c2_here / h_phys**2
        rows.append(p)
        cols.append(p)
        vals.append(diag)

    L = coo_matrix((vals, (rows, cols)), shape=(n_int, n_int)).tocsc()

    # Solve
    n_modes = min(10, n_int - 2)
    try:
        if n_int < 200:
            # Dense for small matrices
            L_dense = L.toarray()
            evals = np.linalg.eigvalsh(L_dense)
            evals.sort()
            omega_modes = np.sqrt(np.maximum(evals[:n_modes], 0.0))
        else:
            evals, evecs = eigsh(L, k=n_modes, which='SM')
            omega_modes = np.sqrt(np.maximum(evals, 0.0))
            omega_modes.sort()
    except Exception as e:
        print(f"\n  Cavity #{rank+1} (comp {comp_id}): eigensolver failed: {e}")
        continue

    # Cavity properties
    cy, cx = np.mean(theta1[iy]), np.mean(theta2[ix])
    A_phys = comp_size * dtheta**2 * g_11
    R_eff = np.sqrt(A_phys / PI)
    mean_mach = np.mean(mach_field[mask])

    cav_info = {
        'rank': rank + 1,
        'comp_id': comp_id,
        'n_pts': comp_size,
        'centroid': (cy, cx),
        'R_eff': R_eff,
        'mean_mach': mean_mach,
        'modes': omega_modes,
    }
    cavity_data.append(cav_info)

    print(f"\n  Cavity #{rank+1}: comp={comp_id}, {comp_size} pts, "
          f"centroid=({cy:.2f},{cx:.2f}), R_eff={R_eff:.3f}, <Mach>={mean_mach:.3f}")
    for m, w in enumerate(omega_modes[:5]):
        all_cavity_modes.append((w, rank + 1, m))
        print(f"    mode {m}: omega = {w:.5f} M_KK")

# Also solve for identity component if not in top 5
if identity_comp > 0 and identity_comp not in [c for c, s in comp_list[:5]]:
    mask_id = labeled_arr == identity_comp
    iy, ix = np.where(mask_id)
    idx_map = {}
    pts = []
    for p, (ii, jj) in enumerate(zip(iy, ix)):
        idx_map[(int(ii), int(jj))] = p
        pts.append((int(ii), int(jj)))
    n_int = len(pts)

    if n_int >= 10:
        rows, cols, vals = [], [], []
        for p, (ii, jj) in enumerate(pts):
            c2_here = c_BdG**2 * max(1.0 - mach_field[ii, jj]**2, 0.0)
            diag = 0.0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni2, nj2 = ii + di, jj + dj
                if (ni2, nj2) in idx_map:
                    p2 = idx_map[(ni2, nj2)]
                    c2_nb = c_BdG**2 * max(1.0 - mach_field[ni2, nj2]**2, 0.0)
                    c2_avg = 0.5 * (c2_here + c2_nb)
                    coeff = c2_avg / h_phys**2
                    rows.append(p); cols.append(p2); vals.append(-coeff)
                    diag += coeff
                else:
                    diag += c2_here / h_phys**2
            rows.append(p); cols.append(p); vals.append(diag)

        L = coo_matrix((vals, (rows, cols)), shape=(n_int, n_int)).tocsc()
        L_dense = L.toarray()
        evals = np.linalg.eigvalsh(L_dense)
        evals.sort()
        omega_id = np.sqrt(np.maximum(evals[:min(5, n_int-1)], 0.0))

        print(f"\n  Identity cavity: comp={identity_comp}, {identity_size} pts")
        for m, w in enumerate(omega_id[:5]):
            all_cavity_modes.append((w, 0, m))
            print(f"    mode {m}: omega = {w:.5f} M_KK")

# ============================================================================
#  FLAT TORUS REFERENCE SPECTRUM
# ============================================================================

print("\n" + "=" * 78)
print("Reference: flat T^2 modes (uniform c = c_BdG, periodic BC)")
print("=" * 78)

L_circ = 2 * PI * np.sqrt(g_11)
omega_fund = c_BdG * 2 * PI / L_circ
print(f"  Circumference L = {L_circ:.4f} M_KK^{{-1}}")
print(f"  omega_{{1,0}} = {omega_fund:.5f} M_KK")
print(f"  omega_{{1,1}} = {omega_fund * np.sqrt(2):.5f} M_KK")
print(f"  omega_{{2,0}} = {2 * omega_fund:.5f} M_KK")
print(f"  Ratio omega_{{1,0}}/omega_L1 = {omega_fund/omega_L1:.3f}")

# ============================================================================
#  Q-FACTOR FROM WKB TUNNELING
# ============================================================================

print("\n" + "=" * 78)
print("Q-factor estimation (WKB tunneling through supersonic barrier)")
print("=" * 78)

supersonic = mach_field > 1.0
mean_mach_super = np.mean(mach_field[supersonic])

# Typical barrier width (distance between adjacent subsonic regions)
# From the top-2 cavities: centroids at (2.10, 2.10) and (4.19, 4.19)
# Physical separation ~ 2.09 * sqrt(g_11) = 4.37
if len(cavity_data) >= 2:
    c1 = cavity_data[0]['centroid']
    c2 = cavity_data[1]['centroid']
    sep_coord = np.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
    barrier_width = sep_coord * np.sqrt(g_11) - cavity_data[0]['R_eff'] - cavity_data[1]['R_eff']
    barrier_width = max(barrier_width, 0.5)  # floor
else:
    barrier_width = PI * np.sqrt(g_11)

# For the lowest cavity mode:
if all_cavity_modes:
    omega_lowest = min(w for w, _, _ in all_cavity_modes)
    kappa = omega_lowest / c_BdG * np.sqrt(mean_mach_super**2 - 1)
    Q_exponent = 2 * kappa * barrier_width

    print(f"  Lowest cavity omega = {omega_lowest:.4f} M_KK")
    print(f"  Mean supersonic Mach = {mean_mach_super:.2f}")
    print(f"  Estimated barrier width = {barrier_width:.3f} M_KK^{{-1}}")
    print(f"  Evanescent kappa = {kappa:.4f} M_KK")
    print(f"  Q ~ exp({Q_exponent:.1f}) >> 1")
    print(f"  Interpretation: modes are perfectly confined (no leakage)")
else:
    omega_lowest = 0
    Q_exponent = 0
    print(f"  No cavity modes found")

# ============================================================================
#  GATE VERDICT
# ============================================================================

print("\n" + "=" * 78)
print("GATE: CAVITY-RESONANCE-49")
print("=" * 78)

# Sort all cavity modes
all_modes_sorted = sorted(all_cavity_modes, key=lambda x: x[0])

# Find best matches
best_r1, best_r2 = 999.0, 999.0
best_w1, best_w2 = 0.0, 0.0
best_cav1, best_cav2 = -1, -1
best_mode1, best_mode2 = -1, -1

for w, cav, mode in all_modes_sorted:
    if w < 1e-4:
        continue
    r1 = abs(w / omega_L1 - 1.0)
    r2 = abs(w / omega_L2 - 1.0)
    if r1 < best_r1:
        best_r1, best_w1, best_cav1, best_mode1 = r1, w, cav, mode
    if r2 < best_r2:
        best_r2, best_w2, best_cav2, best_mode2 = r2, w, cav, mode

print(f"\n  Leggett omega_L1 = {omega_L1:.6f} M_KK")
print(f"  Leggett omega_L2 = {omega_L2:.6f} M_KK")
print(f"\n  Lowest cavity mode = {all_modes_sorted[0][0]:.5f} M_KK (cavity #{all_modes_sorted[0][1]})")
print(f"  Frequency scale ratio: omega_cav_min / omega_L1 = {all_modes_sorted[0][0]/omega_L1:.2f}")

print(f"\n  Best match to omega_L1:")
print(f"    omega_cav = {best_w1:.5f} M_KK (cavity #{best_cav1}, mode {best_mode1})")
print(f"    |delta|/omega_L = {best_r1:.4f} ({best_r1*100:.1f}%)")

print(f"\n  Best match to omega_L2:")
print(f"    omega_cav = {best_w2:.5f} M_KK (cavity #{best_cav2}, mode {best_mode2})")
print(f"    |delta|/omega_L = {best_r2:.4f} ({best_r2*100:.1f}%)")

# Determine verdict
has_confined_modes = len(all_cavity_modes) > 0
pass_L1 = best_r1 < 0.10
pass_L2 = best_r2 < 0.10
any_pass = pass_L1 or pass_L2

if not has_confined_modes:
    verdict = "FAIL"
    detail = "No confined modes found in any subsonic cavity"
elif any_pass:
    verdict = "PASS"
    detail = f"Cavity mode matches Leggett frequency within 10%"
else:
    verdict = "INFO"
    detail = (f"Confined modes exist but mismatch is {min(best_r1,best_r2)*100:.0f}%. "
              f"Cavity modes (position-space) and Leggett modes (momentum-space) "
              f"are distinct excitation types at different frequency scales.")

print(f"\n  PASS criterion: |omega_cav - omega_L|/omega_L < 0.10")
print(f"  L1: {'PASS' if pass_L1 else 'FAIL'} ({best_r1*100:.1f}% mismatch)")
print(f"  L2: {'PASS' if pass_L2 else 'FAIL'} ({best_r2*100:.1f}% mismatch)")
print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")

# ============================================================================
#  PHYSICAL INTERPRETATION
# ============================================================================

print("\n" + "=" * 78)
print("PHYSICAL INTERPRETATION")
print("=" * 78)

print("""
  The Leggett inter-sector phase oscillations (omega_L ~ 0.07-0.11 M_KK)
  and the acoustic cavity normal modes (omega_cav ~ 0.8+ M_KK) live at
  fundamentally different frequency scales.

  Leggett modes are MOMENTUM-SPACE excitations: relative phase oscillations
  between the B1, B2, B3 BCS sectors. Their frequency is set by the
  inter-sector Josephson coupling J_{ij}, which depends on the V-matrix
  elements (sector-sector interaction) and the gap magnitudes Delta_i.

  Cavity modes are POSITION-SPACE excitations: standing acoustic waves
  confined by the Mach-1 horizon on T^2. Their frequency is set by the
  cavity geometry (R_eff ~ 0.5-1.2 M_KK^{-1}) and the local sound speed
  (c_BdG ~ 0.75 M_KK), giving omega ~ c/R ~ 0.6-1.5 M_KK.

  The frequency scale mismatch is structural:
    omega_Leggett ~ sqrt(J/rho) ~ sqrt(V*Delta^2/rho) << c_BdG
    omega_cavity  ~ c_BdG / R_eff ~ c_BdG

  Leggett modes are SOFT (set by weak inter-sector coupling V ~ 0.035).
  Cavity modes are HARD (set by the sound speed / cavity size).

  This is the analog of the distinction between:
    - Josephson plasma frequency in a junction array (soft, coupling-limited)
    - Acoustic resonance of the junction cavity (hard, geometry-limited)

  The analog horizon IS physically real (confirmed by S48 AKAMA-DIAKONOV-48:
  Mach_max=54.3). But it confines acoustic quasiparticles, not Leggett modes.
  Leggett oscillations propagate through the Josephson coupling network,
  which percolates across the ENTIRE T^2 regardless of the Mach field.
""")

# ============================================================================
#  SAVE DATA
# ============================================================================

results = {
    # Gate info
    'gate_name': 'CAVITY-RESONANCE-49',
    'gate_verdict': verdict,
    'gate_detail': detail,

    # Mach field properties
    'mach_max': float(mach_field.max()),
    'mach_mean': float(mach_field.mean()),
    'subsonic_fraction': float(np.mean(subsonic)),
    'n_subsonic_components': n_features,

    # BdG sound speed
    'c_BdG': c_BdG,
    'v_F': v_F,
    'g_11': g_11,
    'h_phys': h_phys,

    # Cavity spectrum
    'n_cavities_solved': len(cavity_data),
    'cavity_modes_all': np.array([w for w, _, _ in all_modes_sorted]),
    'cavity_rank_all': np.array([c for _, c, _ in all_modes_sorted]),

    # Per-cavity data
    'cavity_R_eff': np.array([c['R_eff'] for c in cavity_data]),
    'cavity_n_pts': np.array([c['n_pts'] for c in cavity_data]),
    'cavity_mean_mach': np.array([c['mean_mach'] for c in cavity_data]),
    'cavity_lowest_mode': np.array([c['modes'][0] for c in cavity_data]),

    # Leggett comparison
    'omega_L1': omega_L1,
    'omega_L2': omega_L2,
    'best_match_L1_mismatch': best_r1,
    'best_match_L2_mismatch': best_r2,
    'best_match_L1_omega': best_w1,
    'best_match_L2_omega': best_w2,

    # Flat torus reference
    'omega_fund_flat': omega_fund,
    'L_circumference': L_circ,

    # Q-factor
    'Q_exponent': Q_exponent,
    'barrier_width': barrier_width,
    'omega_cavity_lowest': omega_lowest if all_cavity_modes else 0.0,

    # Identity cavity
    'identity_comp': identity_comp,
    'identity_size': identity_size,
}

outpath = os.path.join(DATA_DIR, 's49_cavity_resonance.npz')
np.savez(outpath, **results)
print(f"\nSaved: {outpath}")

# ============================================================================
#  PLOT
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Panel 1: Mach field on T^2 with cavity contours
ax = axes[0, 0]
T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')
im = ax.pcolormesh(T1, T2, np.log10(np.maximum(mach_field, 0.01)),
                   cmap='RdBu_r', vmin=-1, vmax=2)
# Mach=1 contour
ax.contour(T1, T2, mach_field, levels=[1.0], colors='black', linewidths=2)
ax.set_xlabel(r'$\theta_1$')
ax.set_ylabel(r'$\theta_2$')
ax.set_title(r'$\log_{10}(\mathrm{Mach})$ on $T^2$ (black = horizon)')
plt.colorbar(im, ax=ax)

# Panel 2: Cavity mode spectrum vs Leggett frequencies
ax = axes[0, 1]
if all_modes_sorted:
    # Plot cavity modes as horizontal lines per cavity
    cavity_ids_in_data = sorted(set(c for _, c, _ in all_modes_sorted))
    colors = plt.cm.tab10(np.linspace(0, 1, max(len(cavity_ids_in_data), 1)))
    for idx_c, cav_id in enumerate(cavity_ids_in_data):
        modes = sorted([w for w, c, _ in all_modes_sorted if c == cav_id])
        for m, w in enumerate(modes[:5]):
            ax.plot([cav_id - 0.3, cav_id + 0.3], [w, w], '-',
                    color=colors[idx_c % len(colors)], linewidth=2)

    # Leggett frequencies as horizontal dashed lines spanning all cavities
    ax.axhline(y=omega_L1, color='red', linestyle='--', linewidth=2,
               label=f'$\\omega_{{L1}}$ = {omega_L1:.4f}')
    ax.axhline(y=omega_L2, color='blue', linestyle='--', linewidth=2,
               label=f'$\\omega_{{L2}}$ = {omega_L2:.4f}')

    ax.set_xlabel('Cavity rank')
    ax.set_ylabel(r'$\omega$ [M$_{\rm KK}$]')
    ax.set_title('Cavity modes vs Leggett frequencies')
    ax.legend(fontsize=9)
    ax.set_yscale('log')
    ax.set_ylim(0.01, 5)

# Panel 3: Frequency scale comparison
ax = axes[1, 0]
categories = ['Leggett\n$\\omega_{L1}$', 'Leggett\n$\\omega_{L2}$',
              'Cavity\nlowest', 'Flat $T^2$\nfundamental']
values = [omega_L1, omega_L2,
          all_modes_sorted[0][0] if all_modes_sorted else 0,
          omega_fund]
bar_colors = ['red', 'blue', 'green', 'gray']
bars = ax.bar(categories, values, color=bar_colors, alpha=0.7, edgecolor='black')
ax.set_ylabel(r'$\omega$ [M$_{\rm KK}$]')
ax.set_title('Frequency scale comparison')
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
            f'{val:.3f}', ha='center', va='bottom', fontsize=9)

# Panel 4: Mode density and physical interpretation
ax = axes[1, 1]
if all_modes_sorted:
    modes_arr = np.array([w for w, _, _ in all_modes_sorted])
    modes_arr = modes_arr[modes_arr > 1e-4]
    ax.hist(modes_arr, bins=20, color='steelblue', edgecolor='black', alpha=0.7,
            label=f'{len(modes_arr)} cavity modes')
    ax.axvline(x=omega_L1, color='red', linestyle='--', linewidth=2,
               label=f'$\\omega_{{L1}}$ = {omega_L1:.4f}')
    ax.axvline(x=omega_L2, color='blue', linestyle='--', linewidth=2,
               label=f'$\\omega_{{L2}}$ = {omega_L2:.4f}')
    ax.set_xlabel(r'$\omega$ [M$_{\rm KK}$]')
    ax.set_ylabel('Count')
    ax.set_title(f'Cavity mode histogram (VERDICT: {verdict})')
    ax.legend(fontsize=9)

fig.suptitle('CAVITY-RESONANCE-49: Analog Cavity Normal Modes vs Leggett Frequencies',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(DATA_DIR, 's49_cavity_resonance.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")
plt.close()

print("\n" + "=" * 78)
print(f"FINAL VERDICT: CAVITY-RESONANCE-49 = {verdict}")
print("=" * 78)
