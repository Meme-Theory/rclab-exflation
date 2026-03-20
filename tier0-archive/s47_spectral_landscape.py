#!/usr/bin/env python3
"""
s47_spectral_landscape.py — Publication-quality spectral landscape of Jensen-deformed SU(3)
===========================================================================================

GATE: SPECTRAL-LANDSCAPE-47 (INFO — visualization task, no pass/fail)

Shows all 992 Dirac eigenvalues at the fold (tau=0.19), annotated with:
  - Sector structure (B1/B2/B3) via rank ordering within each PW rep
  - Pi-phase topology from S47 W1-1 (13 states, PW-weighted)
  - BCS pairing information (gap edges, v² fractions)
  - Van Hove singularities (12 critical points)

Multi-panel layout:
  Top: PW-weighted density of states (sector-shaded)
  Middle: Spectral strip (individual eigenvalues, sector-colored)
  Inset: Sector decomposition bars

Session 47 Wave 2-3 | Spectral-Geometer
"""

import sys
sys.path.insert(0, ".")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe
from canonical_constants import tau_fold

# ============================================================================
#  Load data
# ============================================================================

d_dos = np.load("s44_dos_tau.npz", allow_pickle=True)
d_pi = np.load("s47_pi_sector.npz", allow_pickle=True)
d_bcs = np.load("s46_number_projected_bcs.npz", allow_pickle=True)

all_omega = d_dos["tau0.19_all_omega"]      # (992,)
all_dim2 = d_dos["tau0.19_all_dim2"]        # (992,)
vh_omega = d_dos["tau0.19_vh_omega"]        # (12,)
vh_type = d_dos["tau0.19_vh_type"]          # (12,) strings

pi_evals = d_pi["pi_phase_eigenvalues"]     # (13,)
pi_sectors = d_pi["pi_phase_sectors"]       # (13,) B1/B2/B3
pi_reps = d_pi["pi_phase_reps"]            # (13,) (p,q)
pw_pi = {
    "B1": int(d_pi["pw_pi_B1"]),            # 15
    "B2": int(d_pi["pw_pi_B2"]),            # 81
    "B3": int(d_pi["pw_pi_B3"]),            # 35
}

Delta_bcs = d_bcs["Delta_bcs_fold"]         # (3,) [B1, B2, B3]
v2_bcs = d_bcs["v2_bcs"]                   # (3,) [B1, B2, B3]
lam2_fold = d_bcs["lam2_fold"]             # (3,) [B1, B2, B3] — eigenvalue²

# ============================================================================
#  Rep structure: identify (p,q) from dim²
# ============================================================================

# Table of reps at max_pq_sum=3
rep_table = [
    ((0, 0), 1),
    ((0, 1), 3),
    ((1, 0), 3),
    ((0, 2), 6),
    ((2, 0), 6),
    ((1, 1), 8),
    ((0, 3), 10),
    ((3, 0), 10),
    ((2, 1), 15),
]

dim2_to_reps = {}
for (p, q), dim in rep_table:
    d2 = dim**2
    if d2 not in dim2_to_reps:
        dim2_to_reps[d2] = []
    dim2_to_reps[d2].append(((p, q), dim))

# ============================================================================
#  Classify each eigenvalue into (p,q) rep and B1/B2/B3 sector
# ============================================================================

# Group eigenvalues by dim² value
from collections import defaultdict

groups = defaultdict(list)
for i, (omega, d2) in enumerate(zip(all_omega, all_dim2)):
    groups[int(d2)].append((omega, i))

# Within each dim² group, sort by eigenvalue and assign sectors
# Each rep contributes 16*dim eigenvalues: lowest 2*dim -> B1, next 8*dim -> B2, top 6*dim -> B3
sector_labels = np.empty(992, dtype="U2")
rep_labels = np.empty(992, dtype="U5")

for d2_val, entries in groups.items():
    entries_sorted = sorted(entries, key=lambda x: x[0])
    reps_info = dim2_to_reps.get(d2_val, [])

    if not reps_info:
        print(f"WARNING: No rep found for dim²={d2_val}")
        continue

    # For dim²=9 (dim=3): reps (0,1) and (1,0) each contribute 48 eigenvalues
    # For dim²=36: (0,2) and (2,0) each contribute 96
    # For dim²=100: (0,3) and (3,0) each contribute 160
    # Total eigenvalues with this dim² = n_reps * 16 * dim
    n_reps = len(reps_info)
    dim = reps_info[0][1]
    expected_per_rep = 16 * dim
    expected_total = n_reps * expected_per_rep

    if len(entries_sorted) != expected_total:
        print(f"WARNING: dim²={d2_val}, expected {expected_total}, got {len(entries_sorted)}")

    # Assign sectors within each chunk of 16*dim eigenvalues
    # For multiple reps sharing same dim², split evenly then assign
    n_B1_per_rep = 2 * dim
    n_B2_per_rep = 8 * dim
    n_B3_per_rep = 6 * dim

    for rep_idx in range(n_reps):
        start = rep_idx * expected_per_rep
        end = start + expected_per_rep
        chunk = entries_sorted[start:end]
        pq_label = f"({reps_info[rep_idx][0][0]},{reps_info[rep_idx][0][1]})"

        for j, (omega, orig_idx) in enumerate(chunk):
            rep_labels[orig_idx] = pq_label
            if j < n_B1_per_rep:
                sector_labels[orig_idx] = "B1"
            elif j < n_B1_per_rep + n_B2_per_rep:
                sector_labels[orig_idx] = "B2"
            else:
                sector_labels[orig_idx] = "B3"

# Verify counts
n_B1 = np.sum(sector_labels == "B1")
n_B2 = np.sum(sector_labels == "B2")
n_B3 = np.sum(sector_labels == "B3")
print(f"Sector counts: B1={n_B1}, B2={n_B2}, B3={n_B3}, total={n_B1+n_B2+n_B3}")
assert n_B1 + n_B2 + n_B3 == 992, f"Total mismatch: {n_B1+n_B2+n_B3}"

# ============================================================================
#  Color palette (colorblind-friendly: Okabe-Ito inspired)
# ============================================================================

# B1 = blue, B2 = vermillion/orange, B3 = bluish green
C_B1 = "#0072B2"   # blue
C_B2 = "#D55E00"   # vermillion
C_B3 = "#009E73"   # bluish green
C_PI = "#CC79A7"   # reddish purple (for pi-phase stars)
C_VH = "#666666"   # gray for van Hove lines
C_BCS = "#E69F00"  # amber for BCS gap markers

sector_colors = {"B1": C_B1, "B2": C_B2, "B3": C_B3}

# ============================================================================
#  Compute PW-weighted density of states (sector-resolved)
# ============================================================================

omega_grid = np.linspace(all_omega.min() - 0.05, all_omega.max() + 0.05, 2000)
sigma_dos = 0.012  # Gaussian smoothing width

dos_B1 = np.zeros_like(omega_grid)
dos_B2 = np.zeros_like(omega_grid)
dos_B3 = np.zeros_like(omega_grid)

for i in range(992):
    w = all_omega[i]
    d2 = all_dim2[i]
    gauss = d2 * np.exp(-0.5 * ((omega_grid - w) / sigma_dos)**2) / (sigma_dos * np.sqrt(2 * np.pi))
    if sector_labels[i] == "B1":
        dos_B1 += gauss
    elif sector_labels[i] == "B2":
        dos_B2 += gauss
    else:
        dos_B3 += gauss

dos_total = dos_B1 + dos_B2 + dos_B3

# ============================================================================
#  BCS gap edges
# ============================================================================

# lam2_fold contains eigenvalue² per sector: [B1, B2, B3]
# BCS gap edge: E_qp = sqrt(epsilon² + Delta²) where epsilon = lambda - mu (mu=0)
# Gap edge in eigenvalue space: the mode at the Fermi surface +/- Delta
# For B1: E_F ~ sqrt(lam2_fold[0]) = 0.820, Delta = 0.372
# The BCS gap opens around the lowest eigenvalue in each sector
sector_fermi = np.sqrt(lam2_fold)   # [0.820, 0.845, 0.971]
sector_gap_lo = sector_fermi - Delta_bcs  # gap edges below
sector_gap_hi = sector_fermi + Delta_bcs  # gap edges above

# ============================================================================
#  Figure layout
# ============================================================================

fig = plt.figure(figsize=(14, 8.5), dpi=150)
gs = GridSpec(2, 1, height_ratios=[1, 1.6], hspace=0.05,
             left=0.08, right=0.82, top=0.94, bottom=0.08)

ax_dos = fig.add_subplot(gs[0])
ax_strip = fig.add_subplot(gs[1], sharex=ax_dos)

# Inset axes for sector decomposition
ax_inset = fig.add_axes([0.845, 0.38, 0.14, 0.50])

# ============================================================================
#  Panel 1: Density of states (stacked, sector-shaded)
# ============================================================================

ax_dos.fill_between(omega_grid, 0, dos_B1, color=C_B1, alpha=0.5, label="B1 (trivial)")
ax_dos.fill_between(omega_grid, dos_B1, dos_B1 + dos_B2, color=C_B2, alpha=0.5, label="B2 (fund.)")
ax_dos.fill_between(omega_grid, dos_B1 + dos_B2, dos_total, color=C_B3, alpha=0.5, label="B3 (adj.)")
ax_dos.plot(omega_grid, dos_total, color="k", lw=0.8, alpha=0.7)

# Van Hove singularities
for i, (vhw, vht) in enumerate(zip(vh_omega, vh_type)):
    if vhw >= omega_grid[0] and vhw <= omega_grid[-1]:
        ax_dos.axvline(vhw, color=C_VH, ls=":", lw=0.7, alpha=0.6)
        # Only label a few to avoid clutter
        if str(vht) in ("M_3",):
            y_pos = dos_total.max() * 0.92
            ax_dos.text(vhw, y_pos, str(vht), fontsize=7, color=C_VH,
                       ha="center", va="bottom", rotation=0)

# BCS gap edges (B2 only — dominant sector)
for label, lo, hi, color in [
    ("B2", sector_gap_lo[1], sector_gap_hi[1], C_B2),
]:
    ax_dos.axvspan(lo, hi, color=color, alpha=0.08, zorder=0)
    ax_dos.axvline(lo, color=color, ls="--", lw=1.0, alpha=0.4)
    ax_dos.axvline(hi, color=color, ls="--", lw=1.0, alpha=0.4)

ax_dos.set_ylabel(r"$\rho_{\rm PW}(\omega)$", fontsize=12)
ax_dos.set_xlim(omega_grid[0], omega_grid[-1])
ax_dos.set_ylim(0, dos_total.max() * 1.12)
ax_dos.tick_params(labelbottom=False, labelsize=10)
ax_dos.legend(fontsize=9, loc="upper right", framealpha=0.8)

# Title
ax_dos.set_title(
    r"Spectral Landscape: Dirac Operator on Jensen-deformed SU(3) at $\tau = 0.19$ (fold)",
    fontsize=13, fontweight="bold", pad=10
)

# ============================================================================
#  Panel 2: Spectral strip (individual eigenvalues)
# ============================================================================

# Compute marker sizes proportional to sqrt(dim²) for visibility
marker_sizes = np.sqrt(all_dim2)
# Normalize to a reasonable range [2, 18]
ms_min, ms_max = 2.0, 16.0
ms_range = marker_sizes.max() - marker_sizes.min()
if ms_range > 0:
    marker_sizes_norm = ms_min + (ms_max - ms_min) * (marker_sizes - marker_sizes.min()) / ms_range
else:
    marker_sizes_norm = np.full_like(marker_sizes, 8.0)

# Y-axis: jittered by rep identity for visual separation
# Assign y-position by (p,q) rep
rep_y_map = {
    "(0,0)": 0.0,
    "(0,1)": 1.0, "(1,0)": 2.0,
    "(0,2)": 3.0, "(2,0)": 4.0,
    "(1,1)": 5.0,
    "(0,3)": 6.0, "(3,0)": 7.0,
    "(2,1)": 8.0,
}
rep_y_labels = [
    "(0,0)\ndim=1", "(0,1)\ndim=3", "(1,0)\ndim=3",
    "(0,2)\ndim=6", "(2,0)\ndim=6", "(1,1)\ndim=8",
    "(0,3)\ndim=10", "(3,0)\ndim=10", "(2,1)\ndim=15",
]

y_positions = np.array([rep_y_map.get(rep_labels[i], 0.0) for i in range(992)])

# Add small random jitter within each rep band for visibility
rng = np.random.default_rng(42)
y_jitter = rng.uniform(-0.3, 0.3, size=992)
y_plot = y_positions + y_jitter

# Plot by sector for legend
for sec, color in [("B1", C_B1), ("B2", C_B2), ("B3", C_B3)]:
    mask = sector_labels == sec
    ax_strip.scatter(
        all_omega[mask], y_plot[mask],
        s=marker_sizes_norm[mask]**1.3,
        c=color, alpha=0.55,
        edgecolors="none", zorder=2,
        label=f"{sec} ({np.sum(mask)} modes)"
    )

# Horizontal gridlines between reps
for yy in np.arange(-0.5, 9.0, 1.0):
    ax_strip.axhline(yy, color="#dddddd", lw=0.5, zorder=0)

# Pi-phase annotations — PROMINENT
pi_sector_colors = [sector_colors.get(str(s), C_PI) for s in pi_sectors]

# Map pi-phase eigenvalues to their rep y-position
pi_y = []
for ev, rep_str in zip(pi_evals, pi_reps):
    pi_y.append(rep_y_map.get(str(rep_str), 4.5))

ax_strip.scatter(
    pi_evals, pi_y,
    s=220, marker="*", zorder=5,
    c=pi_sector_colors,
    edgecolors="k", linewidths=0.8,
    label=r"$\pi$-phase (13 states)"
)

# Label each pi-phase star with its rep label, offset to avoid overlap
# Use alternating up/down offsets for nearby stars
pi_sorted_idx = np.argsort(pi_evals)
prev_x = -999
offset_sign = 1
for idx in pi_sorted_idx:
    ev = pi_evals[idx]
    yp = pi_y[idx]
    sec = str(pi_sectors[idx])
    rep = str(pi_reps[idx])
    # Alternate offset direction when stars are close
    if abs(ev - prev_x) < 0.06:
        offset_sign *= -1
    else:
        offset_sign = 1
    prev_x = ev
    y_off = 14 * offset_sign
    ax_strip.annotate(
        rep,
        xy=(ev, yp), xytext=(0, y_off),
        textcoords="offset points",
        fontsize=6, fontweight="bold",
        color=sector_colors.get(sec, "k"), ha="center",
        va="bottom" if offset_sign > 0 else "top",
        path_effects=[pe.withStroke(linewidth=2.5, foreground="white")],
        zorder=6,
        arrowprops=dict(arrowstyle="-", color="#aaa", lw=0.5) if abs(y_off) > 12 else None,
    )

# BCS gap shading — show all three sectors
for sec_idx, (sec, color, ls) in enumerate([
    ("B1", C_B1, "--"), ("B2", C_B2, "-"), ("B3", C_B3, "--")
]):
    lo, hi = sector_gap_lo[sec_idx], sector_gap_hi[sec_idx]
    alpha_fill = 0.10 if sec == "B2" else 0.04
    lw_edge = 1.2 if sec == "B2" else 0.7
    ax_strip.axvspan(lo, hi, color=color, alpha=alpha_fill, zorder=0)
    ax_strip.axvline(lo, color=color, ls=ls, lw=lw_edge, alpha=0.5, zorder=1)
    ax_strip.axvline(hi, color=color, ls=ls, lw=lw_edge, alpha=0.5, zorder=1)

# Add BCS gap label for B2 only (dominant)
mid_b2 = (sector_gap_lo[1] + sector_gap_hi[1]) / 2
ax_strip.annotate(
    r"$2\Delta_{\rm B2} = %.2f$" % (2*Delta_bcs[1]),
    xy=(mid_b2, -0.35), xytext=(mid_b2, -0.55),
    fontsize=8.5, ha="center", va="top", color=C_B2, fontweight="bold",
    zorder=7
)
# Double-headed arrow for BCS gap width
ax_strip.annotate("", xy=(sector_gap_lo[1], -0.40), xytext=(sector_gap_hi[1], -0.40),
                  arrowprops=dict(arrowstyle="<->", color=C_B2, lw=1.5), zorder=7)

# Van Hove lines
for vhw in vh_omega:
    if vhw >= omega_grid[0] and vhw <= omega_grid[-1]:
        ax_strip.axvline(vhw, color=C_VH, ls=":", lw=0.6, alpha=0.4, zorder=1)

ax_strip.set_xlabel(r"$|\lambda|$ (eigenvalue magnitude, $M_{\rm KK}$ units)", fontsize=12)
ax_strip.set_ylabel("PW representation", fontsize=12)
ax_strip.set_yticks(range(9))
ax_strip.set_yticklabels(rep_y_labels, fontsize=8)
ax_strip.set_ylim(-0.9, 8.9)
ax_strip.tick_params(labelsize=10)
ax_strip.legend(fontsize=8.5, loc="upper left", framealpha=0.85, ncol=2)

# ============================================================================
#  Inset: Sector decomposition stacked bars
# ============================================================================

# Three bars: (a) total PW modes, (b) pi-phase PW, (c) BCS v² weight
categories = ["PW modes\n(992)", r"$\pi$-phase"+"\n(131 PW)", "BCS $v^2$\n(pairing)"]

# (a) Total PW-weighted modes
total_pw_B1 = np.sum(all_dim2[sector_labels == "B1"])
total_pw_B2 = np.sum(all_dim2[sector_labels == "B2"])
total_pw_B3 = np.sum(all_dim2[sector_labels == "B3"])
total_pw = total_pw_B1 + total_pw_B2 + total_pw_B3

# (b) Pi-phase PW weights
pi_pw_total = pw_pi["B1"] + pw_pi["B2"] + pw_pi["B3"]

# (c) BCS v² fractions
# v2 per mode * multiplicity per sector
# B1: 2 modes (in singlet), B2: 8 modes (4 per pair-mode), B3: 6 modes
# But v2_bcs already gives per-mode occupation
# Total pairing weight: sum v2_k * (sector multiplicity)
# Sector multiplicities from 8-mode Fock space: B1=1 mode, B2=4 modes, B3=3 modes
v2_weighted = np.array([v2_bcs[0] * 1, v2_bcs[1] * 4, v2_bcs[2] * 3])
v2_total = v2_weighted.sum()

# Normalize all to fractions
fracs = np.array([
    [total_pw_B1/total_pw, total_pw_B2/total_pw, total_pw_B3/total_pw],
    [pw_pi["B1"]/pi_pw_total, pw_pi["B2"]/pi_pw_total, pw_pi["B3"]/pi_pw_total],
    [v2_weighted[0]/v2_total, v2_weighted[1]/v2_total, v2_weighted[2]/v2_total],
])

x_bar = np.arange(3)
bar_width = 0.65

bottoms = np.zeros(3)
for sec_idx, (sec, color) in enumerate([("B1", C_B1), ("B2", C_B2), ("B3", C_B3)]):
    vals = fracs[:, sec_idx]
    bars = ax_inset.barh(x_bar, vals, left=bottoms, height=bar_width,
                         color=color, alpha=0.7, edgecolor="white", linewidth=0.5,
                         label=sec)
    # Add percentage text
    for j, v in enumerate(vals):
        if v > 0.08:
            ax_inset.text(bottoms[j] + v/2, x_bar[j], f"{v*100:.0f}%",
                         ha="center", va="center", fontsize=8, fontweight="bold",
                         color="white")
    bottoms += vals

ax_inset.set_yticks(x_bar)
ax_inset.set_yticklabels(categories, fontsize=8)
ax_inset.set_xlim(0, 1)
ax_inset.set_xlabel("fraction", fontsize=9)
ax_inset.set_title("Sector\nDecomposition", fontsize=9.5, fontweight="bold")
ax_inset.tick_params(labelsize=8)
ax_inset.invert_yaxis()

# ============================================================================
#  Annotation box with key numbers
# ============================================================================

info_text = (
    f"$N_{{\\rm modes}} = 992$ (9 reps, $p+q \\leq 3$)\n"
    f"$\\lambda_{{\\min}} = {all_omega.min():.4f}$, "
    f"$\\lambda_{{\\max}} = {all_omega.max():.4f}$\n"
    f"$\\Delta_{{\\rm B2}} = {Delta_bcs[1]:.3f}$, "
    f"$v^2_{{\\rm B2}} = {v2_bcs[1]:.3f}$\n"
    f"$\\pi$-phases: {len(pi_evals)} states, "
    f"PW = {pi_pw_total}"
)
ax_dos.text(0.02, 0.95, info_text, transform=ax_dos.transAxes,
           fontsize=8.5, va="top", ha="left",
           bbox=dict(boxstyle="round,pad=0.4", facecolor="white", alpha=0.85, edgecolor="#aaa"),
           family="monospace")

# ============================================================================
#  Save
# ============================================================================

plt.savefig("s47_spectral_landscape.png", dpi=300, bbox_inches="tight")
plt.savefig("s47_spectral_landscape.pdf", bbox_inches="tight")
print("Saved: s47_spectral_landscape.png, s47_spectral_landscape.pdf")

# ============================================================================
#  Save processed data
# ============================================================================

np.savez("s47_spectral_landscape.npz",
    # Raw classified data
    all_omega=all_omega,
    all_dim2=all_dim2,
    sector_labels=sector_labels,
    rep_labels=rep_labels,
    # Sector counts
    n_B1=n_B1, n_B2=n_B2, n_B3=n_B3,
    # Pi-phase data
    pi_evals=pi_evals,
    pi_sectors=pi_sectors,
    pi_reps=pi_reps,
    pw_pi_B1=pw_pi["B1"], pw_pi_B2=pw_pi["B2"], pw_pi_B3=pw_pi["B3"],
    # BCS data
    Delta_bcs=Delta_bcs,
    v2_bcs=v2_bcs,
    sector_fermi=sector_fermi,
    sector_gap_lo=sector_gap_lo,
    sector_gap_hi=sector_gap_hi,
    # DOS curves
    omega_grid=omega_grid,
    dos_B1=dos_B1, dos_B2=dos_B2, dos_B3=dos_B3, dos_total=dos_total,
    # Sector decomposition fractions
    sector_fracs=fracs,
    # Van Hove data
    vh_omega=vh_omega, vh_type=vh_type,
    # Gate info
    gate_name="SPECTRAL-LANDSCAPE-47",
    gate_verdict="INFO",
    tau=tau_fold,
)
print("Saved: s47_spectral_landscape.npz")

# Verification
print(f"\n=== VERIFICATION ===")
print(f"Total eigenvalues plotted: {len(all_omega)}")
print(f"Pi-phase annotations: {len(pi_evals)}")
print(f"Sector counts: B1={n_B1}, B2={n_B2}, B3={n_B3}")
print(f"Sector PW fracs: B1={total_pw_B1/total_pw:.3f}, B2={total_pw_B2/total_pw:.3f}, B3={total_pw_B3/total_pw:.3f}")
print(f"Pi PW fracs: B1={pw_pi['B1']/pi_pw_total:.3f}, B2={pw_pi['B2']/pi_pw_total:.3f}, B3={pw_pi['B3']/pi_pw_total:.3f}")
print(f"BCS v2 fracs: B1={v2_weighted[0]/v2_total:.3f}, B2={v2_weighted[1]/v2_total:.3f}, B3={v2_weighted[2]/v2_total:.3f}")
print(f"Van Hove singularities: {len(vh_omega)}")
print(f"\nGATE: SPECTRAL-LANDSCAPE-47 — INFO (visualization)")
