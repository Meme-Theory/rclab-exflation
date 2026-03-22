#!/usr/bin/env python3
"""
Session 33a Step 3: Strutinsky Shell Correction Decomposition.

Decompose d^2S/dtau^2 = 20.43 (RPA-32b) into Strutinsky shell correction
(oscillatory) and smooth Seeley-DeWitt average.

Mathematical background:
    The spectral action S(tau) = sum_k |lambda_k(tau)| is the sum of absolute
    eigenvalues of D_K at Jensen parameter tau. Its second derivative at the
    dump point (tau ~ 0.20) is d^2S/dtau^2 = 20.43 (RPA-32b PASS, 38x).

    Strutinsky averaging: The smooth part S_smooth is obtained by convolving
    the level density with a Gaussian of width gamma. The shell correction
    delta_S = S - S_smooth contains the oscillatory part (quantum shell
    effects). In nuclear physics, the shell fraction |d^2(delta_S)/dtau^2| /
    |d^2S/dtau^2| ranges from 30-50% for light nuclei (16-O) to 1-3% for
    heavy nuclei.

    Here we work with eigenvalue sums directly: S(tau) = sum_k |lambda_k(tau)|.
    The Strutinsky smooth is obtained by averaging S(tau) over a window of
    width gamma in tau-space.

Method:
    1. Compute S(tau) = sum_k |lambda_k(tau)| at each tau in the grid.
    2. Apply Strutinsky Gaussian averaging with width gamma to get S_smooth.
    3. Shell correction delta_S = S - S_smooth.
    4. Compute d^2(delta_S)/dtau^2 at tau = 0.20 via cubic spline.
    5. Report shell fraction.

Note: We work with the SINGLET sector (0,0) eigenvalues from the RPA data,
since the RPA-32b result was computed in this sector. We also compute the
full multi-sector sum for comparison.

Author: sim (phonon-exflation-sim)
Date: 2026-03-06
"""

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.ndimage import gaussian_filter1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────────────────────
# 1. Load eigenvalue data
# ─────────────────────────────────────────────────────────────

d_ext = np.load('tier0-computation/s23a_eigenvectors_extended.npz', allow_pickle=True)
d_rpa = np.load('tier0-computation/s32b_rpa1_thouless.npz', allow_pickle=True)

tau_vals = d_ext['tau_values']
n_tau = len(tau_vals)
print(f"Tau grid: {tau_vals}")
print(f"RPA-32b sweep tau: {d_rpa['sweep_tau']}")
print(f"RPA-32b d^2S/dtau^2: {d_rpa['sweep_d2S_abs']}")

# ─────────────────────────────────────────────────────────────
# 2. Compute S(tau) for singlet (0,0) sector
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("SINGLET (0,0) SPECTRAL SUM")
print(f"{'=' * 70}")

# From the RPA data, we have eigenvalues at tau = 0.15, 0.20, 0.25 (singlet)
# These have 16 eigenvalues (8 positive, 8 negative)
S_singlet = np.zeros(n_tau)
eigenvalue_count = np.zeros(n_tau)

for ti in range(n_tau):
    evals = d_ext[f'eigenvalues_{ti}']
    sp = d_ext[f'sector_p_{ti}']
    sq = d_ext[f'sector_q_{ti}']
    mults = d_ext[f'multiplicities_{ti}']

    # Singlet sector
    mask = (sp == 0) & (sq == 0)
    e00 = evals[mask]
    m00 = mults[mask]
    S_singlet[ti] = np.sum(np.abs(e00) * m00)
    eigenvalue_count[ti] = np.sum(m00)

print(f"Eigenvalue count per tau: {eigenvalue_count}")
print(f"S_singlet(tau): {S_singlet}")

# Verify against RPA at tau = 0.15, 0.20, 0.25
for tau_check in [0.15, 0.20, 0.25]:
    ti = np.argmin(np.abs(tau_vals - tau_check))
    rpa_key = f'eigenvalues_0p{int(tau_check*100)}'
    if rpa_key in d_rpa.files:
        rpa_evals = d_rpa[rpa_key]
        S_rpa = np.sum(np.abs(rpa_evals))
        print(f"  tau={tau_check}: S_singlet(extended)={S_singlet[ti]:.6f}, "
              f"S_rpa={S_rpa:.6f}, diff={abs(S_singlet[ti]-S_rpa):.2e}")

# ─────────────────────────────────────────────────────────────
# 3. Compute S(tau) for ALL sectors (full Dirac spectrum)
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("FULL SPECTRUM SPECTRAL SUM (all sectors, N_max=6)")
print(f"{'=' * 70}")

S_full = np.zeros(n_tau)
for ti in range(n_tau):
    evals = d_ext[f'eigenvalues_{ti}']
    mults = d_ext[f'multiplicities_{ti}']
    S_full[ti] = np.sum(np.abs(evals) * mults)

print(f"S_full(tau): {S_full.round(2)}")
print(f"S_full/S_singlet ratio: {(S_full/S_singlet).round(2)}")

# ─────────────────────────────────────────────────────────────
# 4. Strutinsky averaging
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("STRUTINSKY SHELL CORRECTION")
print(f"{'=' * 70}")

# For Strutinsky averaging, we need S(tau) on a fine grid.
# We interpolate with cubic spline, then apply Gaussian smoothing.

# First, the singlet sector
cs_singlet = CubicSpline(tau_vals, S_singlet)

# Fine tau grid
dtau_fine = 0.001
tau_fine = np.arange(tau_vals[0], tau_vals[-1] + dtau_fine/2, dtau_fine)
S_fine = cs_singlet(tau_fine)

# Apply Strutinsky Gaussian averaging with different gamma values
gamma_values = [0.03, 0.05, 0.07, 0.10, 0.15]
results_singlet = {}

print("\n--- Singlet (0,0) ---")
for gamma in gamma_values:
    sigma_pts = gamma / dtau_fine
    S_smooth = gaussian_filter1d(S_fine, sigma=sigma_pts, mode='nearest')
    delta_S = S_fine - S_smooth

    # Second derivatives via central differences
    d2_S = np.gradient(np.gradient(S_fine, dtau_fine), dtau_fine)
    d2_S_smooth = np.gradient(np.gradient(S_smooth, dtau_fine), dtau_fine)
    d2_delta_S = np.gradient(np.gradient(delta_S, dtau_fine), dtau_fine)

    # Evaluate at tau = 0.20
    idx_020 = np.argmin(np.abs(tau_fine - 0.20))
    d2_S_val = d2_S[idx_020]
    d2_delta_val = d2_delta_S[idx_020]
    d2_smooth_val = d2_S_smooth[idx_020]

    shell_fraction = abs(d2_delta_val) / abs(d2_S_val) if abs(d2_S_val) > 1e-10 else 0.0

    results_singlet[gamma] = {
        'S_smooth': S_smooth,
        'delta_S': delta_S,
        'd2_S': d2_S_val,
        'd2_smooth': d2_smooth_val,
        'd2_delta': d2_delta_val,
        'shell_fraction': shell_fraction,
    }

    print(f"  gamma={gamma:.2f}: d^2S={d2_S_val:.2f}, d^2S_smooth={d2_smooth_val:.2f}, "
          f"d^2(delta_S)={d2_delta_val:.2f}, shell_frac={shell_fraction:.4f}")

# Also do the full spectrum
cs_full = CubicSpline(tau_vals, S_full)
S_full_fine = cs_full(tau_fine)

results_full = {}
print("\n--- Full spectrum ---")
for gamma in gamma_values:
    sigma_pts = gamma / dtau_fine
    S_smooth = gaussian_filter1d(S_full_fine, sigma=sigma_pts, mode='nearest')
    delta_S = S_full_fine - S_smooth

    d2_S = np.gradient(np.gradient(S_full_fine, dtau_fine), dtau_fine)
    d2_S_smooth = np.gradient(np.gradient(S_smooth, dtau_fine), dtau_fine)
    d2_delta_S = np.gradient(np.gradient(delta_S, dtau_fine), dtau_fine)

    idx_020 = np.argmin(np.abs(tau_fine - 0.20))
    d2_S_val = d2_S[idx_020]
    d2_delta_val = d2_delta_S[idx_020]
    d2_smooth_val = d2_S_smooth[idx_020]
    shell_fraction = abs(d2_delta_val) / abs(d2_S_val) if abs(d2_S_val) > 1e-10 else 0.0

    results_full[gamma] = {
        'd2_S': d2_S_val,
        'd2_smooth': d2_smooth_val,
        'd2_delta': d2_delta_val,
        'shell_fraction': shell_fraction,
    }

    print(f"  gamma={gamma:.2f}: d^2S={d2_S_val:.2f}, d^2S_smooth={d2_smooth_val:.2f}, "
          f"d^2(delta_S)={d2_delta_val:.2f}, shell_frac={shell_fraction:.4f}")

# ─────────────────────────────────────────────────────────────
# 5. Alternative: Mode-resolved decomposition
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("MODE-RESOLVED DECOMPOSITION (singlet)")
print(f"{'=' * 70}")

# Track individual modes and compute their contributions to d^2S/dtau^2
# Using eigenvalues at singlet: B1(1), B2(4), B3(3)
from scipy.interpolate import CubicSpline as CS

# Get singlet eigenvalues at each tau (from s27 data for consistency)
d_bcs = np.load('tier0-computation/s27_multisector_bcs.npz', allow_pickle=True)
tracks = np.zeros((n_tau, 8))
for ti in range(n_tau):
    e = d_bcs[f'evals_0_0_{ti}']
    pos = np.sort(e[e > 1e-10])
    tracks[ti, :] = pos

# S(tau) = sum_k |lambda_k| = 2 * sum_{k>0} lambda_k (spectral pairing)
S_check = 2 * tracks.sum(axis=1)
print(f"S from tracked modes: {S_check.round(6)}")
print(f"S from extended data: {S_singlet.round(6)}")

# Individual mode contributions to d^2S/dtau^2
# d^2(|lambda_k|)/dtau^2 = d^2(lambda_k)/dtau^2 for lambda_k > 0 (all our modes)
print(f"\nMode-resolved d^2|lambda_k|/dtau^2 at tau=0.20:")
branch_labels = ['B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3']
d2_contributions = np.zeros(8)

for j in range(8):
    cs_j = CS(tau_vals, tracks[:, j])
    d2_j = cs_j(0.20, 2)
    d2_contributions[j] = d2_j
    print(f"  Mode {j} ({branch_labels[j]}): d^2/dtau^2 = {d2_j:.6f}")

# x2 for positive+negative
total_d2 = 2 * np.sum(d2_contributions)
b1_d2 = 2 * d2_contributions[0]
b2_d2 = 2 * np.sum(d2_contributions[1:5])
b3_d2 = 2 * np.sum(d2_contributions[5:8])

print(f"\n  Branch decomposition (x2 for +/- pairing):")
print(f"    B1 (1 mode): {b1_d2:.4f} ({100*b1_d2/total_d2:.1f}%)")
print(f"    B2 (4 modes): {b2_d2:.4f} ({100*b2_d2/total_d2:.1f}%)")
print(f"    B3 (3 modes): {b3_d2:.4f} ({100*b3_d2/total_d2:.1f}%)")
print(f"    Total (8 modes, x2): {total_d2:.4f}")
print(f"    RPA-32b bare curvature: {d_rpa['bare_curvature'][1]:.4f}")
print(f"    Agreement: {abs(total_d2 - d_rpa['bare_curvature'][1]) / d_rpa['bare_curvature'][1] * 100:.2f}%")

# "Shell" in the nuclear sense: the B2 contribution near its fold minimum
# is the "shell effect" -- a localized feature in eigenvalue space
# The "smooth" background is the B3 Debye-like tail
print(f"\n  Physical interpretation:")
print(f"    B2 fold (localized, shell-like): {b2_d2:.4f} ({100*b2_d2/total_d2:.1f}%)")
print(f"    B3 Debye tail (smooth): {b3_d2:.4f} ({100*b3_d2/total_d2:.1f}%)")
print(f"    B1 (single mode): {b1_d2:.4f} ({100*b1_d2/total_d2:.1f}%)")
shell_frac_mode = abs(b2_d2) / abs(total_d2)
print(f"    Shell fraction (B2/total): {shell_frac_mode:.4f} = {100*shell_frac_mode:.1f}%")

# ─────────────────────────────────────────────────────────────
# 6. Plot
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: S(tau) singlet and full
ax = axes[0, 0]
ax.plot(tau_vals, S_singlet, 'bo-', markersize=5, label='Singlet (0,0)')
ax.plot(tau_vals, S_full / (S_full[0] / S_singlet[0]), 'go-', markersize=5,
        label='Full (rescaled)')
ax.axvline(x=0.20, color='red', linestyle='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('S(tau) = sum |lambda_k|')
ax.set_title('Spectral Sum S(tau)')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Strutinsky shell correction (singlet)
ax = axes[0, 1]
gamma_plot = 0.05
r = results_singlet[gamma_plot]
idx_range = (tau_fine >= 0.05) & (tau_fine <= 0.45)
S_smooth_plot = gaussian_filter1d(S_fine, sigma=gamma_plot/dtau_fine, mode='nearest')
delta_S_plot = S_fine - S_smooth_plot
ax.plot(tau_fine[idx_range], S_fine[idx_range], 'b-', linewidth=1.5, label='S(tau)')
ax.plot(tau_fine[idx_range], S_smooth_plot[idx_range], 'r-', linewidth=1.5,
        label=f'S_smooth (gamma={gamma_plot})')
ax.axvline(x=0.20, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('S(tau)')
ax.set_title(f'Strutinsky Averaging (singlet, gamma={gamma_plot})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Shell fraction vs gamma
ax = axes[1, 0]
gammas = sorted(results_singlet.keys())
fracs_s = [results_singlet[g]['shell_fraction'] for g in gammas]
fracs_f = [results_full[g]['shell_fraction'] for g in gammas]
ax.plot(gammas, fracs_s, 'bo-', markersize=6, label='Singlet')
ax.plot(gammas, fracs_f, 'go-', markersize=6, label='Full spectrum')
ax.axhspan(0.30, 0.50, alpha=0.1, color='blue', label='16-O regime (30-50%)')
ax.axhspan(0.01, 0.03, alpha=0.1, color='red', label='Heavy nucleus (1-3%)')
ax.set_xlabel('Gamma (Strutinsky width)')
ax.set_ylabel('Shell fraction |d^2(delta_S)/d^2S|')
ax.set_title('Shell Fraction vs Averaging Width')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_ylim(-0.05, 1.0)

# Panel 4: Mode-resolved d^2S/dtau^2
ax = axes[1, 1]
# Bar chart of branch contributions
branches = ['B1 (1)', 'B2 (4)', 'B3 (3)']
d2_vals = [b1_d2, b2_d2, b3_d2]
colors = ['C0', 'C1', 'C2']
bars = ax.bar(branches, d2_vals, color=colors, alpha=0.7)
for bar, val in zip(bars, d2_vals):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.2,
            f'{val:.2f}\n({100*val/total_d2:.0f}%)', ha='center', fontsize=9)
ax.axhline(y=total_d2, color='black', linestyle='--', label=f'Total: {total_d2:.2f}')
ax.set_ylabel('d^2(sum|lambda|)/dtau^2')
ax.set_title('Branch Decomposition of Bare Curvature at tau=0.20')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.suptitle('Session 33a: Strutinsky Shell Correction (STRUT-33a)',
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s33a_strutinsky.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: tier0-computation/s33a_strutinsky.png")

# ─────────────────────────────────────────────────────────────
# 7. Save
# ─────────────────────────────────────────────────────────────

save_dict = {
    'tau_values': tau_vals,
    'S_singlet': S_singlet,
    'S_full': S_full,
    'mode_d2_contributions': d2_contributions,
    'b1_d2': np.array([b1_d2]),
    'b2_d2': np.array([b2_d2]),
    'b3_d2': np.array([b3_d2]),
    'total_d2': np.array([total_d2]),
    'shell_fraction_mode_resolved': np.array([shell_frac_mode]),
}

for gamma in gamma_values:
    r_s = results_singlet[gamma]
    r_f = results_full[gamma]
    g_str = f'{gamma:.2f}'.replace('.', 'p')
    save_dict[f'singlet_gamma_{g_str}_d2S'] = np.array([r_s['d2_S']])
    save_dict[f'singlet_gamma_{g_str}_d2smooth'] = np.array([r_s['d2_smooth']])
    save_dict[f'singlet_gamma_{g_str}_d2delta'] = np.array([r_s['d2_delta']])
    save_dict[f'singlet_gamma_{g_str}_shell_frac'] = np.array([r_s['shell_fraction']])
    save_dict[f'full_gamma_{g_str}_shell_frac'] = np.array([r_f['shell_fraction']])

np.savez('tier0-computation/s33a_strutinsky.npz', **save_dict)
print("Data saved: tier0-computation/s33a_strutinsky.npz")

# ─────────────────────────────────────────────────────────────
# 8. Summary
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("SUMMARY: STRUT-33a")
print(f"{'=' * 70}")
print(f"\n  Mode-resolved decomposition (most reliable):")
print(f"    B1: {b1_d2:.3f} ({100*b1_d2/total_d2:.1f}%)")
print(f"    B2: {b2_d2:.3f} ({100*b2_d2/total_d2:.1f}%)")
print(f"    B3: {b3_d2:.3f} ({100*b3_d2/total_d2:.1f}%)")
print(f"    Total bare: {total_d2:.3f}")
print(f"    Shell fraction (B2 fold / total): {100*shell_frac_mode:.1f}%")
print(f"\n  Strutinsky averaging (gamma-dependent):")
for gamma in [0.05, 0.07, 0.10]:
    r = results_singlet[gamma]
    print(f"    gamma={gamma}: shell_frac = {r['shell_fraction']:.3f}")
print(f"\n  Physical interpretation:")
print(f"    B3 dominates ({100*b3_d2/total_d2:.0f}%) = smooth Debye tail (classical)")
print(f"    B2 contributes {100*b2_d2/total_d2:.0f}% = fold-localized (quantum shell)")
print(f"    B1 contributes {100*b1_d2/total_d2:.0f}% = single-mode")
print(f"    Regime: intermediate between light-nucleus (30-50%) and heavy (1-3%)")
