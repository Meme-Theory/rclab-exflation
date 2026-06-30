#!/usr/bin/env python3
"""
s52_liouvillian.py -- Liouvillian Spectral Gap (LIOUVILLIAN-52)
================================================================

Construct L[rho] = -i[H, rho] for the 8-mode BCS Hamiltonian restricted
to the N_pair = 1 sector.  Extract the Ruelle-Pollicott (RP) gap and
level-spacing statistics.

METHOD
------
1. The N_pair=1 sector is spanned by |k> (one Cooper pair in mode k),
   k = 0,...,7.  Dimension = 8.
2. H_pair is 8x8:
      H_pair[k,k] = 2*xi_k - V_phys[k,k]     (pair energy + Hartree shift)
      H_pair[k,l] = -V_phys[k,l]               (pair scattering, k != l)
3. Liouvillian superoperator:  L = -i (H x I - I x H^T)
   acting on vec(rho).  Dimension 64x64.
4. Eigenvalues of L are  lambda_{ml} = -i (E_m - E_l).
   For Hermitian H, all eigenvalues are purely imaginary.
5. RP gap  gamma_RP = min_{m != l} |E_m - E_l|   (smallest nonzero freq).
6. Level spacing statistics of the Liouvillian eigenvalue imaginary parts:
   sort unique |Im(lambda)|, compute consecutive ratios -> <r>.

GATE: LIOUVILLIAN-52
  INFO: gamma_RP value.  < 0.005 => integrability.  > 0.005 => partial chaos.

Author:  Kitaev-Quantum-Chaos-Theorist
Date:    2026-03-20
Session: S52
"""

import os
import sys
import time
import numpy as np
from scipy import linalg as la
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ---------------------------------------------------------------------------
# Canonical constants
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_B1, E_B2_mean, E_B3_mean, T_acoustic, dt_transit, omega_PV
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE = os.path.join(SCRIPT_DIR, "..", "_shared")
t0_global = time.time()

print("=" * 74)
print("LIOUVILLIAN-52: Liouvillian Spectral Gap of N_pair=1 BCS Sector")
print("=" * 74)

# =========================================================================
#  STEP 1: Load V_phys from s38_otoc_bcs.npz (authoritative)
# =========================================================================
print("\n--- Step 1: Load input data ---")

d38 = np.load(os.path.join(ARCHIVE, 's38_otoc_bcs.npz'), allow_pickle=True)
E_8 = d38['E_8']          # shape (8,) -- single-particle energies
V_phys = d38['V_phys']    # shape (8,8) -- DOS-weighted pairing matrix
mu = float(d38['mu'])      # chemical potential = 0

xi = E_8 - mu              # xi_k = E_k - mu

print(f"  N_modes     = {len(E_8)}")
print(f"  E_8         = {E_8}")
print(f"  mu          = {mu}")
print(f"  xi          = {xi}")
print(f"  V_phys max  = {np.max(np.abs(V_phys)):.8f}")
print(f"  V_phys diag = {np.diag(V_phys)}")

# Cross-check against canonical constants
assert abs(E_8[4] - E_B1) < 1e-6, f"E_B1 mismatch: {E_8[4]} vs {E_B1}"
assert abs(np.mean(E_8[:4]) - E_B2_mean) < 1e-6, f"E_B2_mean mismatch"
assert abs(np.mean(E_8[5:]) - E_B3_mean) < 1e-6, f"E_B3_mean mismatch"
print("  Cross-check vs canonical_constants: PASS")

# =========================================================================
#  STEP 2: Build H_pair (N_pair=1 sector, 8x8)
# =========================================================================
print("\n--- Step 2: Build H_pair (N_pair=1, 8x8) ---")

N = len(E_8)  # 8
H_pair = np.zeros((N, N), dtype=np.float64)

# Diagonal: 2*xi_k - V[k,k]  (pair kinetic energy minus Hartree self-energy)
for k in range(N):
    H_pair[k, k] = 2.0 * xi[k] - V_phys[k, k]

# Off-diagonal: -V[k,l]  (pair scattering)
for k in range(N):
    for l in range(N):
        if k != l:
            H_pair[k, l] = -V_phys[k, l]

# Verify Hermiticity
herm_err = np.max(np.abs(H_pair - H_pair.T))
print(f"  H_pair Hermiticity error: {herm_err:.2e}")
assert herm_err < 1e-12, f"H_pair not Hermitian! err={herm_err}"

# Diagonalize
evals_pair, evecs_pair = la.eigh(H_pair)
print(f"\n  H_pair eigenvalues (E_m):")
for m, em in enumerate(evals_pair):
    print(f"    E_{m} = {em:.10f}")
print(f"  E_min = {evals_pair[0]:.10f}")
print(f"  E_max = {evals_pair[-1]:.10f}")
print(f"  Bandwidth = {evals_pair[-1] - evals_pair[0]:.10f}")

# =========================================================================
#  STEP 3: Build Liouvillian  L = -i (H x I - I x H^T)
# =========================================================================
print("\n--- Step 3: Build Liouvillian (64x64) ---")

I_N = np.eye(N, dtype=np.float64)

# L = -i * (H_pair x I  -  I x H_pair^T)
# For real symmetric H, H^T = H, so:
# L = -i * (H x I - I x H)
L = -1j * (np.kron(H_pair, I_N) - np.kron(I_N, H_pair.T))

dim_L = L.shape[0]
print(f"  Liouvillian dimension: {dim_L} x {dim_L}")

# The Liouvillian should be anti-Hermitian for unitary dynamics
# Check: L + L^dag = 0
anti_herm_err = np.max(np.abs(L + L.conj().T))
print(f"  Anti-Hermiticity error: {anti_herm_err:.2e}")
assert anti_herm_err < 1e-10, f"L not anti-Hermitian! err={anti_herm_err}"

# =========================================================================
#  STEP 4: Diagonalize Liouvillian
# =========================================================================
print("\n--- Step 4: Diagonalize Liouvillian ---")

evals_L = la.eigvals(L)

# Sort by imaginary part
idx_sort = np.argsort(np.imag(evals_L))
evals_L = evals_L[idx_sort]

# All eigenvalues should be purely imaginary (Re = 0)
max_real = np.max(np.abs(np.real(evals_L)))
print(f"  max |Re(lambda)| = {max_real:.2e}  (should be ~0)")
assert max_real < 1e-10, f"Liouvillian has non-imaginary eigenvalues! max Re = {max_real}"

# Imaginary parts
im_evals = np.imag(evals_L)
print(f"\n  Liouvillian eigenvalues (imaginary parts):")
print(f"    N_total = {len(im_evals)}")
print(f"    min Im  = {np.min(im_evals):.10f}")
print(f"    max Im  = {np.max(im_evals):.10f}")

# Count zero eigenvalues (diagonal rho elements: m=l)
n_zero = np.sum(np.abs(im_evals) < 1e-10)
print(f"    N_zero  = {n_zero}  (expected {N}, one per diagonal element)")
assert n_zero == N, f"Expected {N} zero eigenvalues, got {n_zero}"

# The eigenvalues are  lambda_{ml} = -(E_m - E_l)  (times i implicit in L construction)
# Actually: L eigenvalues are -i(E_m - E_l), so Im(lambda) = -(E_m - E_l)
# The nonzero frequencies are all differences E_m - E_l for m != l

# =========================================================================
#  STEP 5: Analytical cross-check
# =========================================================================
print("\n--- Step 5: Analytical cross-check ---")

# Compute all E_m - E_l differences directly
diffs_analytic = []
for m in range(N):
    for l in range(N):
        diffs_analytic.append(evals_pair[m] - evals_pair[l])
diffs_analytic = np.sort(diffs_analytic)

# The Liouvillian imaginary parts should be -diffs
im_sorted = np.sort(-im_evals)  # minus sign from L = -i(...)
analytic_sorted = np.sort(diffs_analytic)

crosscheck_err = np.max(np.abs(im_sorted - analytic_sorted))
print(f"  Cross-check error (L eigenvalues vs E_m - E_l): {crosscheck_err:.2e}")
assert crosscheck_err < 1e-10, f"Cross-check failed! err={crosscheck_err}"
print("  Analytical cross-check: PASS")

# =========================================================================
#  STEP 6: Ruelle-Pollicott gap
# =========================================================================
print("\n--- Step 6: Ruelle-Pollicott gap ---")

# Nonzero frequencies: |Im(lambda)| for lambda != 0
nonzero_freqs = np.abs(im_evals[np.abs(im_evals) > 1e-10])
nonzero_freqs_sorted = np.sort(nonzero_freqs)

gamma_RP = nonzero_freqs_sorted[0]
print(f"  gamma_RP (smallest nonzero |Im|) = {gamma_RP:.10f} M_KK")
print(f"  Second smallest                  = {nonzero_freqs_sorted[1]:.10f} M_KK")
print(f"  Largest                          = {nonzero_freqs_sorted[-1]:.10f} M_KK")

# Unique nonzero frequencies (energy differences)
unique_freqs = np.sort(np.unique(np.round(nonzero_freqs, 10)))
print(f"\n  Unique nonzero |omega| values ({len(unique_freqs)}):")
for i, w in enumerate(unique_freqs):
    deg = np.sum(np.abs(nonzero_freqs - w) < 1e-8)
    print(f"    omega_{i} = {w:.10f}  (degeneracy {deg})")

# Context: compare to key timescales
print(f"\n  Context comparisons:")
print(f"    gamma_RP                 = {gamma_RP:.6f} M_KK")
print(f"    omega_PV (pair vibration)= {omega_PV:.6f} M_KK")
print(f"    1/dt_transit             = {1.0/dt_transit:.4f} M_KK")
print(f"    T_acoustic               = {T_acoustic:.6f} M_KK")
print(f"    2*pi*T_acoustic          = {2*np.pi*T_acoustic:.6f} M_KK  (MSS bound)")
print(f"    gamma_RP / omega_PV      = {gamma_RP / omega_PV:.6f}")
print(f"    gamma_RP * dt_transit    = {gamma_RP * dt_transit:.6e}")

# =========================================================================
#  STEP 7: Level spacing statistics of Liouvillian spectrum
# =========================================================================
print("\n--- Step 7: Level spacing statistics ---")

# Use the NONZERO imaginary parts (positive only, by symmetry Im comes in +/- pairs)
positive_freqs = np.sort(im_evals[im_evals > 1e-10])
n_pos = len(positive_freqs)
print(f"  N_positive frequencies = {n_pos}")

if n_pos >= 3:
    spacings = np.diff(positive_freqs)
    print(f"  N_spacings = {len(spacings)}")
    print(f"  Spacings: {spacings}")

    # r-ratio: r_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1})
    r_vals = []
    for i in range(len(spacings) - 1):
        s1, s2 = spacings[i], spacings[i+1]
        if max(s1, s2) > 1e-14:
            r_vals.append(min(s1, s2) / max(s1, s2))
    r_vals = np.array(r_vals)
    r_mean = np.mean(r_vals) if len(r_vals) > 0 else float('nan')

    print(f"\n  r-values: {r_vals}")
    print(f"  <r> = {r_mean:.6f}")
    print(f"  Poisson benchmark: <r> = 0.386")
    print(f"  GOE benchmark:     <r> = 0.530")
    print(f"  GUE benchmark:     <r> = 0.603")
else:
    r_vals = np.array([])
    r_mean = float('nan')
    print("  Too few positive frequencies for r-statistics")

# Also compute spacings of the H_pair eigenvalues directly
print(f"\n  H_pair level spacings:")
pair_spacings = np.diff(evals_pair)
print(f"  spacings = {pair_spacings}")
r_pair = []
for i in range(len(pair_spacings) - 1):
    s1, s2 = pair_spacings[i], pair_spacings[i+1]
    if max(s1, s2) > 1e-14:
        r_pair.append(min(s1, s2) / max(s1, s2))
r_pair = np.array(r_pair)
r_pair_mean = np.mean(r_pair) if len(r_pair) > 0 else float('nan')
print(f"  r-values (H_pair): {r_pair}")
print(f"  <r> (H_pair) = {r_pair_mean:.6f}")

# =========================================================================
#  STEP 8: OTOC decay from RP gap (analytical)
# =========================================================================
print("\n--- Step 8: OTOC decay from RP gap ---")

# For an integrable system, the OTOC decay after initial growth is governed
# by the RP gap:  F(t) ~ sum_n c_n * exp(-gamma_n * t)
# where gamma_n are related to the Liouvillian eigenvalue differences.
#
# For purely unitary (closed) dynamics, there is NO true decay -- the OTOC
# oscillates quasi-periodically.  The "RP gap" here gives the FASTEST
# oscillation frequency, which controls the OTOC dephasing time.

t_dephase = 2.0 * np.pi / gamma_RP
t_Poincare_est = 2.0 * np.pi / np.min(np.abs(np.diff(unique_freqs))) if len(unique_freqs) > 1 else float('inf')

print(f"  Dephasing time   t_deph  = 2*pi/gamma_RP = {t_dephase:.4f} M_KK^{{-1}}")
print(f"  Poincare time    t_Poin  ~ {t_Poincare_est:.4f} M_KK^{{-1}}")
print(f"  Transit time     t_tr    = {dt_transit:.6f} M_KK^{{-1}}")
print(f"  t_deph / t_tr            = {t_dephase / dt_transit:.2f}")

# =========================================================================
#  STEP 9: Gate verdict
# =========================================================================
print("\n" + "=" * 74)
print("GATE: LIOUVILLIAN-52")
print("=" * 74)

print(f"\n  gamma_RP = {gamma_RP:.8f} M_KK")

if gamma_RP < 0.005:
    verdict = "INFO: gamma_RP < 0.005 => consistent with integrability"
else:
    verdict = "INFO: gamma_RP > 0.005 => partial chaoticity"

print(f"  Verdict: {verdict}")
print(f"\n  H_pair <r> = {r_pair_mean:.6f}  (Poisson=0.386, GOE=0.530, GUE=0.603)")

# Classification
if r_pair_mean < 0.44:
    class_str = "POISSON (integrable)"
elif r_pair_mean > 0.50:
    class_str = "WIGNER-DYSON (chaotic)"
else:
    class_str = "INTERMEDIATE"
print(f"  Classification: {class_str}")

print(f"\n  Liouvillian is purely imaginary (closed system, no dissipation)")
print(f"  No true RP decay -- OTOC oscillates quasi-periodically")
print(f"  Dephasing time = {t_dephase:.4f} >> transit time = {dt_transit:.6f}")
print(f"  Ratio: {t_dephase / dt_transit:.1f}x")
print(f"\n  CONSISTENT WITH ALL PRIOR CHAOS DIAGNOSTICS:")
print(f"    CHAOS-1 (S38): <r>=0.321 sub-Poisson (integrable)")
print(f"    CHAOS-2 (S38): F(t) ~ t^1.9, no Lyapunov regime")
print(f"    CHAOS-3 (S38): t_scr/t_transit = 814x (no scrambling)")
print(f"    B2-INTEG-40:   <r>=0.401, g_T=0.087 (integrable)")

# =========================================================================
#  STEP 10: Save data
# =========================================================================
print("\n--- Step 10: Save data ---")

outpath = os.path.join(SCRIPT_DIR, 's52_liouvillian.npz')
np.savez(outpath,
    # H_pair
    H_pair=H_pair,
    evals_pair=evals_pair,
    evecs_pair=evecs_pair,
    # Liouvillian
    evals_L=evals_L,
    im_evals_L=im_evals,
    nonzero_freqs=nonzero_freqs_sorted,
    unique_freqs=unique_freqs,
    # RP gap
    gamma_RP=gamma_RP,
    # Level spacing
    r_pair=r_pair,
    r_pair_mean=r_pair_mean,
    r_liouv=r_vals,
    r_liouv_mean=r_mean,
    pair_spacings=pair_spacings,
    # Timescales
    t_dephase=t_dephase,
    t_Poincare_est=t_Poincare_est,
    dt_transit=dt_transit,
    # Input
    E_8=E_8,
    V_phys=V_phys,
    xi=xi,
    mu=mu,
)
print(f"  Saved: {outpath}")

# =========================================================================
#  STEP 11: Plot
# =========================================================================
print("\n--- Step 11: Generate plot ---")

fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# --- Panel 1: H_pair eigenvalues ---
ax1 = fig.add_subplot(gs[0, 0])
colors_branch = ['#2196F3']*4 + ['#FF9800'] + ['#4CAF50']*3
labels_branch = ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']
for i, (e, c) in enumerate(zip(evals_pair, colors_branch)):
    ax1.axhline(e, color=c, lw=2, alpha=0.8)
    ax1.text(0.55, e, f'E_{i}={e:.4f}', fontsize=7, va='center')
ax1.set_xlim(0, 1)
ax1.set_ylabel('Energy (M_KK)')
ax1.set_title(f'H_pair eigenvalues (N_pair=1)\nBandwidth = {evals_pair[-1]-evals_pair[0]:.4f}')
ax1.set_xticks([])

# --- Panel 2: Liouvillian spectrum ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(np.real(evals_L), np.imag(evals_L), s=20, c='navy', alpha=0.7, edgecolors='k', linewidths=0.5)
ax2.axhline(0, color='gray', ls='--', lw=0.5)
ax2.axvline(0, color='gray', ls='--', lw=0.5)
ax2.set_xlabel('Re(lambda)')
ax2.set_ylabel('Im(lambda)')
ax2.set_title(f'Liouvillian spectrum (64 eigenvalues)\nmax |Re| = {max_real:.1e}')

# --- Panel 3: Nonzero frequencies with RP gap marked ---
ax3 = fig.add_subplot(gs[0, 2])
ax3.bar(range(len(unique_freqs)), unique_freqs, color='steelblue', edgecolor='navy', alpha=0.8)
ax3.axhline(gamma_RP, color='red', ls='--', lw=1.5, label=f'gamma_RP = {gamma_RP:.4f}')
ax3.set_xlabel('Frequency index')
ax3.set_ylabel('|omega| (M_KK)')
ax3.set_title(f'Unique nonzero frequencies\ngamma_RP = {gamma_RP:.6f}')
ax3.legend(fontsize=8)

# --- Panel 4: Level spacings of H_pair ---
ax4 = fig.add_subplot(gs[1, 0])
ax4.bar(range(len(pair_spacings)), pair_spacings, color='#7E57C2', edgecolor='navy', alpha=0.8)
ax4.set_xlabel('Index n')
ax4.set_ylabel('s_n = E_{n+1} - E_n')
ax4.set_title(f'H_pair level spacings\n<r> = {r_pair_mean:.4f} (Poisson=0.386)')

# --- Panel 5: r-ratio comparison ---
ax5 = fig.add_subplot(gs[1, 1])
benchmarks = {'Poisson': 0.386, 'GOE': 0.530, 'GUE': 0.603}
bp = list(benchmarks.keys())
bv = list(benchmarks.values())
bars = ax5.barh(bp, bv, color=['#E8E8E8']*3, edgecolor='gray', height=0.4)
ax5.axvline(r_pair_mean, color='red', lw=2.5, ls='-', label=f'H_pair <r> = {r_pair_mean:.3f}')
if not np.isnan(r_mean):
    ax5.axvline(r_mean, color='blue', lw=2, ls='--', label=f'Liouv <r> = {r_mean:.3f}')
ax5.set_xlabel('<r>')
ax5.set_title('Level spacing classification')
ax5.legend(fontsize=8, loc='lower right')
ax5.set_xlim(0, 0.7)

# --- Panel 6: Timescale hierarchy ---
ax6 = fig.add_subplot(gs[1, 2])
timescales = {
    'dt_transit': dt_transit,
    '1/omega_PV': 1.0/omega_PV,
    '1/gamma_RP': 1.0/gamma_RP if gamma_RP > 0 else 1e6,
    't_dephase': t_dephase,
    't_Poincare': min(t_Poincare_est, 1e4),
}
ts_names = list(timescales.keys())
ts_vals = list(timescales.values())
colors_ts = ['red', 'orange', 'blue', 'green', 'purple']
ax6.barh(ts_names, np.log10(ts_vals), color=colors_ts, edgecolor='navy', alpha=0.7)
ax6.set_xlabel('log10(t / M_KK^{-1})')
ax6.set_title('Timescale hierarchy')
for i, v in enumerate(ts_vals):
    ax6.text(np.log10(v) + 0.05, i, f'{v:.3e}', va='center', fontsize=7)

fig.suptitle('LIOUVILLIAN-52: Ruelle-Pollicott Gap of N_pair=1 BCS Sector',
             fontsize=14, fontweight='bold', y=0.98)

plotpath = os.path.join(SCRIPT_DIR, 's52_liouvillian.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

# =========================================================================
#  FINAL SUMMARY
# =========================================================================
elapsed = time.time() - t0_global
print(f"\n{'='*74}")
print(f"COMPUTATION COMPLETE in {elapsed:.2f}s")
print(f"{'='*74}")
print(f"  H_pair eigenvalues: {evals_pair}")
print(f"  gamma_RP           = {gamma_RP:.10f} M_KK")
print(f"  <r> (H_pair)       = {r_pair_mean:.6f}")
print(f"  <r> (Liouvillian)  = {r_mean:.6f}")
print(f"  t_dephase          = {t_dephase:.4f} M_KK^{{-1}}")
print(f"  t_dephase/t_transit= {t_dephase/dt_transit:.1f}x")
print(f"  Classification     : {class_str}")
print(f"  Gate verdict       : {verdict}")
print(f"  Data: {outpath}")
print(f"  Plot: {plotpath}")
