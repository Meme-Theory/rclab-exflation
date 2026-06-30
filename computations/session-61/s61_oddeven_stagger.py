#!/usr/bin/env python3
"""
S61 W3-15: Nuclear Odd-Even Staggering in CC Staircase (ODDEVEN-61)
=====================================================================

Gate: ODDEVEN-61
  INFO (diagnostic — classifies BCS-BEC crossover regime).

Nuclear physics uses the 3-point mass difference formula to extract pairing
gaps from binding energy staircases. The same diagnostic applied to the
BCS staircase E_GS(N) for N-pair sectors classifies where the phonon-
exflation condensate sits in the BCS-BEC crossover:

  BCS limit:      Delta^{(3)} ~ Delta_0 (constant, equals pairing gap)
  BEC limit:      Delta^{(3)} grows with N (bosonic pair binding)
  Crossover:      non-monotonic Delta^{(3)}

Formulas:
  Delta^{(3)}(N) = (-1)^N * [E(N+1) - 2*E(N) + E(N-1)] / 2
  Delta^{(5)}(N) = (-1)^N * [-E(N+2) + 4*E(N+1) - 6*E(N) + 4*E(N-1) - E(N-2)] / 8

These are centered finite differences of the binding energy, with the
alternating sign chosen so that Delta^{(3)} > 0 in the paired phase
for even N (the nuclear convention).

Cross-pillar connection:
  Pillar IV (flat band BCS) -> Pillar V (Josephson arrays):
    The Peotta-Torma quantum metric determines superfluid weight.
    Delta^{(3)} probes pairing correlations directly. If Delta^{(3)}
    shows BEC-like growth, the N_pair=1 condensate is strongly bound
    (deep in the Mott lobe of the E_J/E_C phase diagram).
    If BCS-like, the condensate is weakly paired (metallic side).

  Pillar II (superfluid cosmology):
    Volovik q-theory maps Lambda to partial F / partial q.
    The odd-even staggering is the discrete second derivative of F(q=N),
    i.e. d^2F/dq^2 = pair susceptibility chi_pair.

Author: phonon-first-cosmologist, Session 61
Date: 2026-03-28
"""

import os
import sys
import time
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# === Import canonical constants ===
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import *

# =====================================================================
#  1. LOAD INPUT DATA
# =====================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))
t_start = time.time()

print("=" * 72)
print("S61 W3-15: Nuclear Odd-Even Staggering — ODDEVEN-61")
print("=" * 72)

# Try VOL-8 output first (full N=0..8)
vol8_path = os.path.join(data_dir, 's61_multi_pair_qtheory.npz')
s60_path  = os.path.join(data_dir, 's60_staircase_ext.npz')
rg_path   = os.path.join(data_dir, 's60_rg_integrals.npz')

recomputed = False

if os.path.exists(vol8_path):
    d = np.load(vol8_path, allow_pickle=True)
    E_GS = d['E_GS']  # N=0..8
    eps_fold = d['eps_fold']
    V_fold_data = d['V_fold']
    N_modes = int(d['N_modes'])
    print(f"Loaded E_GS(N=0..{len(E_GS)-1}) from s61_multi_pair_qtheory.npz")
    print(f"Source: VOL-8 output (8-mode ED at tau_fold={tau_fold})")
else:
    # Recompute from scratch using 8-mode BCS ED
    print("VOL-8 output not found. Recomputing from scratch...")
    from itertools import combinations
    from math import comb

    d_rg = np.load(rg_path, allow_pickle=True)
    eps_fold = d_rg['eps_fold']
    V_fold_data = d_rg['V_fold']
    N_modes = 8  # (local)

    E_GS = np.zeros(N_modes + 1)
    for N_pair in range(N_modes + 1):
        dim = comb(N_modes, N_pair)
        if dim == 0:
            continue
        configs = list(combinations(range(N_modes), N_pair))
        H = np.zeros((dim, dim))
        for i, ci in enumerate(configs):
            H[i, i] = sum(eps_fold[k] for k in ci)
            for j in range(i + 1, dim):
                cj = configs[j]
                diff = set(ci).symmetric_difference(set(cj))
                if len(diff) == 2:
                    a, b = sorted(diff)
                    H[i, j] = V_fold_data[a, b]
                    H[j, i] = V_fold_data[a, b]
        evals = np.linalg.eigvalsh(H)
        E_GS[N_pair] = evals[0]

    recomputed = True
    print(f"Recomputed E_GS(N=0..{N_modes}) from 8-mode ED")

N_max = len(E_GS) - 1
print()

# =====================================================================
#  2. DISPLAY THE STAIRCASE
# =====================================================================

print("BCS Staircase E_GS(N):")
print("-" * 40)
for N in range(N_max + 1):
    print(f"  E_GS({N}) = {E_GS[N]:+.8f} M_KK")
print()

# Chemical potential mu(N) = E_GS(N) - E_GS(N-1)
mu = np.diff(E_GS)
print("Chemical potential mu(N) = E_GS(N) - E_GS(N-1):")
print("-" * 40)
for N in range(1, N_max + 1):
    print(f"  mu({N}) = {mu[N-1]:+.8f} M_KK")
print()

# Second difference (raw curvature) d2E(N) = E(N+1) - 2E(N) + E(N-1)
d2E = np.zeros(N_max - 1)
for N in range(1, N_max):
    d2E[N - 1] = E_GS[N + 1] - 2 * E_GS[N] + E_GS[N - 1]

print("Raw second difference d2E(N) = E(N+1) - 2E(N) + E(N-1):")
print("-" * 40)
for N in range(1, N_max):
    print(f"  d2E({N}) = {d2E[N-1]:+.8f} M_KK")
print()

# =====================================================================
#  3. THREE-POINT ODD-EVEN STAGGERING Delta^{(3)}
# =====================================================================
#
# Nuclear convention (Bender, Dobaczewski, Nazarewicz, Satula):
#   Delta^{(3)}(N) = (-1)^N / 2 * [E(N+1) - 2*E(N) + E(N-1)]
#
# This is half the second difference, with alternating sign.
# For a pure pairing Hamiltonian:
#   Delta^{(3)}(even N) ≈ +Delta  (pairing gap)
#   Delta^{(3)}(odd N)  ≈ 0       (mean field)
# In BCS:
#   Delta^{(3)} ≈ Delta for all N (constant)
# In BEC:
#   Delta^{(3)} grows with N (pair binding energy increases)

print("=" * 72)
print("3-POINT ODD-EVEN STAGGERING Delta^{(3)}(N)")
print("=" * 72)

N_vals_3pt = np.arange(1, N_max)  # N = 1, 2, ..., 7
Delta3 = np.zeros(len(N_vals_3pt))

for i, N in enumerate(N_vals_3pt):
    Delta3[i] = ((-1)**N) * (E_GS[N + 1] - 2 * E_GS[N] + E_GS[N - 1]) / 2.0

print(f"{'N':>3}  {'Delta3(N)':>12}  {'|Delta3|':>10}  {'sign':>5}  {'class':>8}")
print("-" * 50)
for i, N in enumerate(N_vals_3pt):
    sign_str = "+" if Delta3[i] > 0 else "-"
    # Classification by comparison to known gaps
    abs_d3 = abs(Delta3[i])
    if abs_d3 < 0.5 * Delta_B3:
        cls = "weak"
    elif abs_d3 < Delta_0_OES:
        cls = "B3-like"
    elif abs_d3 < Delta_0_GL:
        cls = "OES-like"
    else:
        cls = "GL-like"
    print(f"  {N}  {Delta3[i]:+12.8f}  {abs_d3:10.8f}  {sign_str:>5}  {cls:>8}")
print()

# Statistics
Delta3_even = Delta3[1::2]  # N=2,4,6
Delta3_odd  = Delta3[0::2]  # N=1,3,5,7
print(f"Even-N mean |Delta3|: {np.mean(np.abs(Delta3_even)):.6f} M_KK")
print(f"Odd-N mean |Delta3|:  {np.mean(np.abs(Delta3_odd)):.6f} M_KK")
print(f"Overall mean |Delta3|: {np.mean(np.abs(Delta3)):.6f} M_KK")
print(f"Overall std |Delta3|:  {np.std(np.abs(Delta3)):.6f} M_KK")
print()

# =====================================================================
#  4. FIVE-POINT FORMULA Delta^{(5)}
# =====================================================================
#
# Higher-order smoothing of the staircase:
#   Delta^{(5)}(N) = (-1)^N / 8 * [-E(N+2) + 4E(N+1) - 6E(N) + 4E(N-1) - E(N-2)]
#
# This is the 5-point central fourth-order-corrected version:
#   (1/8) * (-1)^N * [fourth central difference coefficients applied to E]
# It removes linear mean-field trends more cleanly.

print("=" * 72)
print("5-POINT ODD-EVEN STAGGERING Delta^{(5)}(N)")
print("=" * 72)

N_vals_5pt = np.arange(2, N_max - 1)  # N = 2, 3, ..., 6
Delta5 = np.zeros(len(N_vals_5pt))

for i, N in enumerate(N_vals_5pt):
    Delta5[i] = ((-1)**N) / 8.0 * (
        -E_GS[N + 2] + 4 * E_GS[N + 1] - 6 * E_GS[N]
        + 4 * E_GS[N - 1] - E_GS[N - 2]
    )

print(f"{'N':>3}  {'Delta5(N)':>12}  {'Delta3(N)':>12}  {'ratio 5/3':>10}")
print("-" * 50)
for i, N in enumerate(N_vals_5pt):
    d3_at_N = Delta3[N - 1]  # Delta3 array starts at N=1
    ratio = Delta5[i] / d3_at_N if abs(d3_at_N) > 1e-15 else float('nan')
    print(f"  {N}  {Delta5[i]:+12.8f}  {d3_at_N:+12.8f}  {ratio:10.4f}")
print()

# =====================================================================
#  5. BCS-BEC CROSSOVER CLASSIFICATION
# =====================================================================

print("=" * 72)
print("BCS-BEC CROSSOVER CLASSIFICATION")
print("=" * 72)
print()

# Test 1: Is Delta^{(3)} approximately constant? (BCS signature)
Delta3_abs = np.abs(Delta3)
cv = np.std(Delta3_abs) / np.mean(Delta3_abs) if np.mean(Delta3_abs) > 0 else float('inf')
print(f"Coefficient of variation of |Delta3|: CV = {cv:.4f}")
if cv < 0.2:
    bcs_const = "PASS (BCS-like: roughly constant)"
elif cv < 0.5:
    bcs_const = "MARGINAL (some variation)"
else:
    bcs_const = "FAIL (not constant — not pure BCS)"
print(f"  Constancy test (CV < 0.2): {bcs_const}")
print()

# Test 2: Is there a monotone trend? (BEC growth)
from scipy.stats import spearmanr
rho_spearman, p_spearman = spearmanr(N_vals_3pt, Delta3_abs)
print(f"Spearman correlation |Delta3| vs N: rho = {rho_spearman:.4f}, p = {p_spearman:.4f}")
if rho_spearman > 0.7 and p_spearman < 0.05:
    bec_growth = "BEC-like growth detected"
elif rho_spearman < -0.7 and p_spearman < 0.05:
    bec_growth = "Anti-BEC (shrinking pairs)"
else:
    bec_growth = "No monotone trend"
print(f"  Growth test: {bec_growth}")
print()

# Test 3: Alternating sign pattern
signs = np.sign(Delta3)
sign_changes = np.sum(np.abs(np.diff(signs)) > 0)
print(f"Sign changes in Delta3: {sign_changes} out of {len(Delta3)-1} consecutive pairs")
alternating = all(signs[i] * signs[i + 1] < 0 for i in range(len(signs) - 1))
print(f"  Perfectly alternating: {'YES' if alternating else 'NO'}")
print()

# Test 4: Compare to known gaps
mean_abs_Delta3 = np.mean(Delta3_abs)
print("Comparison to known pairing gaps:")
print(f"  <|Delta3|> = {mean_abs_Delta3:.6f} M_KK")
print(f"  Delta_0_GL  = {Delta_0_GL:.6f} M_KK   (ratio: {mean_abs_Delta3/Delta_0_GL:.4f})")
print(f"  Delta_0_OES = {Delta_0_OES:.6f} M_KK   (ratio: {mean_abs_Delta3/Delta_0_OES:.4f})")
print(f"  Delta_B3    = {Delta_B3:.6f} M_KK   (ratio: {mean_abs_Delta3/Delta_B3:.4f})")
print()

# Test 5: Even-odd asymmetry (nuclear physics signature)
# In nuclei: Delta3(even) > Delta3(odd) because even systems are paired
if len(Delta3_even) > 0 and len(Delta3_odd) > 0:
    mean_even = np.mean(Delta3_even)
    mean_odd = np.mean(Delta3_odd)
    print(f"Even-N mean Delta3: {mean_even:+.6f} M_KK")
    print(f"Odd-N mean Delta3:  {mean_odd:+.6f} M_KK")
    print(f"Even-odd difference: {mean_even - mean_odd:+.6f} M_KK")
    if mean_even > mean_odd:
        eo_test = "Nuclear pairing pattern (even > odd)"
    else:
        eo_test = "Inverted (odd > even) — atypical"
    print(f"  Even-odd test: {eo_test}")
print()

# =====================================================================
#  6. PAIR SUSCEPTIBILITY (q-theory connection)
# =====================================================================
#
# chi_pair(N) = -d^2 E / dN^2 = -(E(N+1) - 2E(N) + E(N-1))
# This is the discrete pair susceptibility. Positive = pair-attractive.
# In Volovik q-theory, this maps to d^2 F / dq^2 at q = N.

print("=" * 72)
print("PAIR SUSCEPTIBILITY chi_pair(N) = -d2E/dN2")
print("=" * 72)

chi_pair = -d2E  # Negative of second difference

print(f"{'N':>3}  {'chi_pair(N)':>12}  {'sign':>5}  {'interpretation':>20}")
print("-" * 55)
for N in range(1, N_max):
    sign_str = "+" if chi_pair[N - 1] > 0 else "-"
    if chi_pair[N - 1] > 0:
        interp = "pair-attractive"
    else:
        interp = "pair-repulsive"
    print(f"  {N}  {chi_pair[N-1]:+12.8f}  {sign_str:>5}  {interp:>20}")
print()

# =====================================================================
#  7. OVERALL CLASSIFICATION
# =====================================================================

print("=" * 72)
print("OVERALL CLASSIFICATION")
print("=" * 72)

# Decision logic
if cv < 0.2 and abs(rho_spearman) < 0.5:
    regime = "BCS (weak-coupling)"
    regime_detail = ("Delta^{(3)} is roughly constant across N, matching "
                     "the BCS prediction that the pairing gap is N-independent.")
elif rho_spearman > 0.7 and p_spearman < 0.05:
    regime = "BEC (strong-coupling)"
    regime_detail = ("|Delta^{(3)}| grows monotonically with N, indicating "
                     "tightly bound bosonic pairs with N-dependent binding.")
elif alternating and cv > 0.3:
    regime = "BCS-BEC crossover (shell effects)"
    regime_detail = ("Delta^{(3)} alternates in sign with large amplitude "
                     "variations. This is the signature of discrete shell "
                     "structure dominating over mean-field pairing — the "
                     "crossover regime where neither pure BCS nor pure BEC "
                     "describes the system. In nuclear physics, this is the "
                     "regime of shell closures and deformation.")
else:
    regime = "Intermediate / unclassified"
    regime_detail = ("Delta^{(3)} pattern does not cleanly match BCS, BEC, "
                     "or standard crossover signatures.")

print(f"Regime: {regime}")
print(f"Detail: {regime_detail}")
print()

# Cross-pillar interpretation
print("Cross-pillar connections:")
print("  Pillar IV -> V: " + (
    "Shell-structured pairing -> condensate sits at boundary of "
    "Mott lobe (Josephson E_J/E_C ~ 1 regime)" if "crossover" in regime.lower() else
    "Classification maps to Josephson phase diagram"
))
print("  Pillar II: " + (
    "Discrete q-theory with strong shell effects -> "
    "Lambda_res oscillations are structural, not convergent" if "crossover" in regime.lower() or "shell" in regime.lower() else
    f"q-theory regime: {regime}"
))
print()

# =====================================================================
#  8. GATE VERDICT
# =====================================================================

gate_name = "ODDEVEN-61"
gate_verdict = "INFO"
gate_detail = (f"Regime={regime}. <|Delta3|>={mean_abs_Delta3:.4f} M_KK. "
               f"CV={cv:.3f}. rho_Spearman={rho_spearman:.3f}. "
               f"Alternating={alternating}. "
               f"Ratio to Delta_0_OES={mean_abs_Delta3/Delta_0_OES:.3f}.")

print("=" * 72)
print(f"GATE: {gate_name} = {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 72)
print()

# =====================================================================
#  9. SAVE RESULTS
# =====================================================================

out_path = os.path.join(data_dir, 's61_oddeven_stagger.npz')
np.savez(out_path,
    # Input
    N_modes=N_modes,
    tau_fold=tau_fold,
    E_GS=E_GS,
    eps_fold=eps_fold,
    recomputed=recomputed,
    # 3-point
    N_vals_3pt=N_vals_3pt,
    Delta3=Delta3,
    Delta3_abs=Delta3_abs,
    # 5-point
    N_vals_5pt=N_vals_5pt,
    Delta5=Delta5,
    # Chemical potential
    mu=mu,
    # Second difference
    d2E=d2E,
    # Pair susceptibility
    chi_pair=chi_pair,
    # Statistics
    cv_Delta3=cv,
    rho_spearman=rho_spearman,
    p_spearman=p_spearman,
    sign_changes=sign_changes,
    alternating=alternating,
    mean_abs_Delta3=mean_abs_Delta3,
    # Even-odd
    Delta3_even=Delta3_even,
    Delta3_odd=Delta3_odd,
    mean_even=np.mean(Delta3_even),
    mean_odd=np.mean(Delta3_odd),
    # Known gaps for reference
    Delta_0_GL=Delta_0_GL,
    Delta_0_OES=Delta_0_OES,
    Delta_B3=Delta_B3,
    # Classification
    regime=np.array([regime]),
    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"Saved: {out_path}")
print()

# =====================================================================
#  10. PLOT
# =====================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f"Nuclear Odd-Even Staggering — ODDEVEN-61\n"
             f"8-mode BCS ED, tau_fold={tau_fold}, Regime: {regime}",
             fontsize=13, fontweight='bold')

# --- Panel (a): E_GS staircase ---
ax = axes[0, 0]
N_all = np.arange(N_max + 1)
ax.plot(N_all, E_GS, 'ko-', markersize=7, linewidth=1.5, label='E_GS(N)')
# Linear fit for reference
coeffs_lin = np.polyfit(N_all, E_GS, 1)
ax.plot(N_all, np.polyval(coeffs_lin, N_all), 'r--', alpha=0.5,
        label=f'Linear fit: {coeffs_lin[0]:.3f}N + {coeffs_lin[1]:.3f}')
ax.set_xlabel('N (pair number)', fontsize=11)
ax.set_ylabel('E_GS (M_KK units)', fontsize=11)
ax.set_title('(a) BCS Staircase', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xticks(N_all)

# --- Panel (b): Delta^{(3)} ---
ax = axes[0, 1]
colors_3pt = ['C0' if N % 2 == 0 else 'C1' for N in N_vals_3pt]
ax.bar(N_vals_3pt, Delta3, color=colors_3pt, alpha=0.7, edgecolor='black', linewidth=0.5)
# Reference lines
ax.axhline(Delta_0_GL, color='red', linestyle='--', alpha=0.6, label=f'Delta_GL = {Delta_0_GL:.3f}')
ax.axhline(-Delta_0_GL, color='red', linestyle='--', alpha=0.6)
ax.axhline(Delta_0_OES, color='green', linestyle='--', alpha=0.6, label=f'Delta_OES = {Delta_0_OES:.3f}')
ax.axhline(-Delta_0_OES, color='green', linestyle='--', alpha=0.6)
ax.axhline(Delta_B3, color='purple', linestyle='--', alpha=0.6, label=f'Delta_B3 = {Delta_B3:.3f}')
ax.axhline(-Delta_B3, color='purple', linestyle='--', alpha=0.6)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlabel('N (pair number)', fontsize=11)
ax.set_ylabel('Delta^{(3)}(N) (M_KK)', fontsize=11)
ax.set_title('(b) 3-Point Odd-Even Staggering', fontsize=11)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)
ax.set_xticks(N_vals_3pt)

# --- Panel (c): Delta^{(5)} vs Delta^{(3)} ---
ax = axes[1, 0]
ax.plot(N_vals_3pt, Delta3, 'o-', color='C0', markersize=7, linewidth=1.5,
        label='Delta^{(3)}')
ax.plot(N_vals_5pt, Delta5, 's-', color='C3', markersize=7, linewidth=1.5,
        label='Delta^{(5)}')
ax.axhline(0, color='black', linewidth=0.5)
ax.axhline(Delta_0_OES, color='green', linestyle=':', alpha=0.5, label=f'Delta_OES')
ax.axhline(-Delta_0_OES, color='green', linestyle=':', alpha=0.5)
ax.set_xlabel('N (pair number)', fontsize=11)
ax.set_ylabel('Delta (M_KK)', fontsize=11)
ax.set_title('(c) 3-Point vs 5-Point Comparison', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_xticks(range(1, N_max))

# --- Panel (d): |Delta^{(3)}| with regime shading ---
ax = axes[1, 1]
ax.plot(N_vals_3pt, Delta3_abs, 'ko-', markersize=7, linewidth=1.5)
# Shade regime bands
ax.axhspan(0, Delta_B3, alpha=0.1, color='blue', label='weak (< Delta_B3)')
ax.axhspan(Delta_B3, Delta_0_OES, alpha=0.1, color='green', label='B3-like')
ax.axhspan(Delta_0_OES, Delta_0_GL, alpha=0.1, color='orange', label='OES-like')
ax.axhspan(Delta_0_GL, max(Delta3_abs) * 1.3, alpha=0.1, color='red', label='GL-like')
# Mean line
ax.axhline(mean_abs_Delta3, color='black', linestyle=':', linewidth=1,
           label=f'mean = {mean_abs_Delta3:.3f}')
ax.set_xlabel('N (pair number)', fontsize=11)
ax.set_ylabel('|Delta^{(3)}(N)| (M_KK)', fontsize=11)
ax.set_title(f'(d) |Delta3| — CV = {cv:.3f}', fontsize=11)
ax.legend(fontsize=8, loc='upper left')
ax.grid(True, alpha=0.3)
ax.set_xticks(N_vals_3pt)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's61_oddeven_stagger.png')
fig.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved: {plot_path}")
plt.close()

# =====================================================================
#  TIMING
# =====================================================================
elapsed = time.time() - t_start
print(f"\nTotal time: {elapsed:.2f}s")
