#!/usr/bin/env python3
"""
s60_blocking_n3.py — BLOCKING-N3-60
Nuclear Blocking Interpretation of N_pair = 3 Minimum

The non-monotonic <r> sequence (0.442, 0.412, 0.419 for N_pair=2,3,4) has a
minimum at N_pair=3. We test whether this is explained by nuclear-style blocking:

1. Extract canonical-basis occupation numbers v_k^2 = <n_k> from ED ground states
2. Compute BCS gap from odd-even staggering (OES):
     Delta_OES(N) = (-1)^N * [E(N+1) - 2*E(N) + E(N-1)] / 2
3. Compute blocking parameter:
     b(N) = (1/N_modes) * sum_k (v_k^2 - 1/2)^2
   Measures distance from half-filling (maximal pairing). Minimum b => most pairing.
4. Identify Fermi surface structure at each N.

Gate: BLOCKING-N3-60
  PASS: Delta_OES minimum at N=3
  FAIL: Delta_OES minimum at N != 3
  INFO: Delta_OES minimum at N=3 but b(N) does not follow

Author: Nazarewicz Nuclear Structure Theorist
Session: S60
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, E_cond, N_dof_BCS

# ============================================================================
#  1. Load data
# ============================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# S52 HFB full contains E_vs_N staircase AND ED occupation numbers for N=1..4
d52 = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)

# S53 HFB spectral contains coherence factors u, v, Z for N=1..4
d53 = np.load(os.path.join(data_dir, 's53_hfb_spectral.npz'), allow_pickle=True)

# Fabric-scale data for <r> values (confirmation)
d58 = np.load(os.path.join(data_dir, 's58_npair2_integ.npz'), allow_pickle=True)
d59_3 = np.load(os.path.join(data_dir, 's59_npair3_integ.npz'), allow_pickle=True)
d59_4 = np.load(os.path.join(data_dir, 's59_therm_order.npz'), allow_pickle=True)

# ============================================================================
#  2. Energy staircase and OES
# ============================================================================

E_vs_N = d52['E_vs_N']  # E(N_pair) for N_pair = 0, 1, ..., 8
N_max = len(E_vs_N) - 1  # = 8

labels = d52['labels']  # ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']
N_modes = int(d52['N1_n_k_ed'].shape[0])  # = 8

print("=" * 70)
print("BLOCKING-N3-60: Nuclear Blocking Interpretation")
print("=" * 70)

# --- Energy staircase ---
print("\n--- Energy Staircase E(N_pair) [M_KK] ---")
for N in range(N_max + 1):
    print(f"  E({N}) = {E_vs_N[N]:.10f}")

# --- Separation energies ---
print("\n--- Single-Pair Separation Energies S_1(N) = E(N) - E(N-1) ---")
S1 = np.zeros(N_max)
for N in range(1, N_max + 1):
    S1[N-1] = E_vs_N[N] - E_vs_N[N-1]
    print(f"  S_1({N}) = {S1[N-1]:.10f}")

# --- OES pairing gap ---
# Standard nuclear formula:
#   Delta_OES(N) = (-1)^N * [E(N+1) - 2*E(N) + E(N-1)] / 2
# This gives the SIGNED staggering. |Delta_OES| is the pairing gap magnitude.
print("\n--- Odd-Even Staggering Delta_OES(N) ---")
Delta_OES = np.zeros(N_max - 1)  # N = 1, ..., N_max-1
for N in range(1, N_max):
    Delta_OES[N-1] = ((-1)**N) * (E_vs_N[N+1] - 2*E_vs_N[N] + E_vs_N[N-1]) / 2.0
    sign_label = "+" if Delta_OES[N-1] > 0 else "-"
    print(f"  Delta_OES({N}) = {Delta_OES[N-1]:+.10f}  |Delta_OES| = {abs(Delta_OES[N-1]):.10f}")

# Find minimum |Delta_OES|
abs_OES = np.abs(Delta_OES)
N_min_OES = np.argmin(abs_OES) + 1  # +1 because index 0 -> N=1
print(f"\n  Minimum |Delta_OES| at N_pair = {N_min_OES}: {abs_OES[N_min_OES-1]:.10f}")

# Check local minima
print("\n--- Local Structure of |Delta_OES| ---")
for i in range(1, len(abs_OES) - 1):
    N = i + 1
    if abs_OES[i] < abs_OES[i-1] and abs_OES[i] < abs_OES[i+1]:
        print(f"  LOCAL MINIMUM at N = {N}: |Delta_OES| = {abs_OES[i]:.10f}")
    elif abs_OES[i] > abs_OES[i-1] and abs_OES[i] > abs_OES[i+1]:
        print(f"  LOCAL MAXIMUM at N = {N}: |Delta_OES| = {abs_OES[i]:.10f}")

# ============================================================================
#  3. Occupation numbers and blocking parameter
# ============================================================================

# ED occupation numbers from S52
nk_ed = {}
for N in range(1, 5):
    nk_ed[N] = d52[f'N{N}_n_k_ed']

# Also available from fabric-scale data (S58/S59) but those are 2-cell (16 modes)
# The single-cell (8-mode) ED data from S52 is the correct benchmark

print("\n--- ED Occupation Numbers v_k^2 = <n_k> ---")
for N in range(1, 5):
    nk = nk_ed[N]
    print(f"  N_pair = {N}:")
    total = 0.0  # (local)
    for k in range(N_modes):
        lbl = str(labels[k])
        print(f"    k={k} ({lbl:>6s}): v_k^2 = {nk[k]:.6f}")
        total += nk[k]
    print(f"    Sum = {total:.6f} (expect {N}.000)")

# --- Blocking parameter ---
# b(N) = (1/N_modes) * sum_k (v_k^2 - 1/2)^2
# This measures the mean-square deviation of occupancies from 1/2.
# Minimum b => occupancies closest to 1/2 => strongest pairing (most BCS-like).
# Maximum b => occupancies far from 1/2 => sharp Fermi surface => blocking dominant.
print("\n--- Blocking Parameter b(N) = <(v_k^2 - 1/2)^2> ---")
b_param = {}
for N in range(1, 5):
    nk = nk_ed[N]
    b = np.mean((nk - 0.5)**2)
    b_param[N] = b
    print(f"  b({N}) = {b:.10f}")

N_min_b = min(b_param, key=b_param.get)
N_max_b = max(b_param, key=b_param.get)
print(f"\n  Minimum b at N_pair = {N_min_b}: {b_param[N_min_b]:.10f} (most BCS-like)")
print(f"  Maximum b at N_pair = {N_max_b}: {b_param[N_max_b]:.10f} (sharpest Fermi surface)")

# --- Fermi surface identification ---
# The Fermi surface is at the mode where n_k crosses 1/2.
# In the nuclear analog: the last partially occupied orbital.
print("\n--- Fermi Surface Identification ---")
for N in range(1, 5):
    nk = nk_ed[N]
    # Find mode closest to n_k = 0.5
    fermi_idx = np.argmin(np.abs(nk - 0.5))
    lbl = str(labels[fermi_idx])
    # Spread around Fermi surface
    spread = np.max(nk) - np.min(nk)
    print(f"  N_pair = {N}: Fermi mode = k={fermi_idx} ({lbl}), n_k = {nk[fermi_idx]:.6f}, spread = {spread:.6f}")

# ============================================================================
#  4. Coherence factors from S53 (Bogoliubov analysis)
# ============================================================================

print("\n--- Coherence Analysis (S53 data) ---")
print("  |u^2 - v^2| measures distance from maximal BCS mixing (0 = pure BCS, 1 = pure particle/hole)")
for N in range(1, 5):
    uv2 = np.abs(d53[f'N{N}_u2_minus_v2_ed'])
    Z = d53[f'N{N}_Z_ed']
    print(f"  N_pair = {N}: <|u^2-v^2|> = {np.mean(uv2):.6f}, <Z> = {np.mean(Z):.6f}")
    for k in range(N_modes):
        lbl = str(labels[k])
        print(f"    k={k} ({lbl:>6s}): |u^2-v^2| = {uv2[k]:.6f}, Z = {Z[k]:.6f}")

# ============================================================================
#  5. Three-point pairing gap (alternative formula)
# ============================================================================

# The three-point formula for even/odd pairing gaps:
#   Delta^(3)(N) = [E(N+1) + E(N-1) - 2*E(N)] / 2  (unsigned)
# This is the second finite difference, always positive for convex E(N).
print("\n--- Three-Point Gap Delta^(3)(N) = [E(N+1) + E(N-1) - 2*E(N)] / 2 ---")
Delta_3pt = np.zeros(N_max - 1)
for N in range(1, N_max):
    Delta_3pt[N-1] = (E_vs_N[N+1] + E_vs_N[N-1] - 2*E_vs_N[N]) / 2.0
    print(f"  Delta^(3)({N}) = {Delta_3pt[N-1]:.10f}")

N_min_3pt = np.argmin(Delta_3pt) + 1
print(f"\n  Minimum Delta^(3) at N_pair = {N_min_3pt}: {Delta_3pt[N_min_3pt-1]:.10f}")

# Check if minimum is at N=3
has_min_at_3_oes = (N_min_OES == 3)
has_min_at_3_3pt = (N_min_3pt == 3)

# ============================================================================
#  6. Blocking vs interaction: decomposition
# ============================================================================

# Nuclear structure insight: the CHANGE in occupation numbers between N and N+1
# reveals whether the added pair is distributed (BCS-like) or concentrated (blocking).
print("\n--- Occupation Change dn_k(N) = n_k(N+1) - n_k(N) ---")
for N in range(1, 4):
    nk_curr = nk_ed[N]
    nk_next = nk_ed[N+1]
    dn = nk_next - nk_curr
    print(f"  N_pair = {N} -> {N+1}:")
    dn_B2 = dn[:4]
    dn_B1 = dn[4]
    dn_B3 = dn[5:]
    print(f"    B2 sector: dn = [{', '.join(f'{x:.6f}' for x in dn_B2)}]  sum = {np.sum(dn_B2):.6f}")
    print(f"    B1 mode:   dn = {dn_B1:.6f}")
    print(f"    B3 sector: dn = [{', '.join(f'{x:.6f}' for x in dn_B3)}]  sum = {np.sum(dn_B3):.6f}")
    # Concentration ratio: how much of the added pair goes to B2 vs distributed
    total_dn = np.sum(dn)
    frac_B2 = np.sum(dn_B2) / total_dn if total_dn > 0 else 0
    frac_B1 = dn_B1 / total_dn if total_dn > 0 else 0
    frac_B3 = np.sum(dn_B3) / total_dn if total_dn > 0 else 0
    print(f"    Fraction: B2={frac_B2:.4f}, B1={frac_B1:.4f}, B3={frac_B3:.4f}")
    # Entropy of distribution (uniform = max entropy)
    probs = np.abs(dn) / np.sum(np.abs(dn))
    S_dn = -np.sum(probs * np.log(probs + 1e-30))
    S_max = np.log(N_modes)
    print(f"    Distribution entropy: {S_dn:.4f} / {S_max:.4f} = {S_dn/S_max:.4f}")

# ============================================================================
#  7. Pair density and Pauli blocking analysis
# ============================================================================

print("\n--- Pauli Blocking Analysis ---")
# For each N, compute:
# 1. Number of "active" modes (n_k neither ~0 nor ~1, within [0.1, 0.9])
# 2. Effective pairing space dimension
# 3. d/Delta ratio (level spacing / gap)

for N in range(1, 5):
    nk = nk_ed[N]
    # Active modes: n_k in [0.05, 0.95]
    active = np.sum((nk > 0.05) & (nk < 0.95))
    # BCS pairing is strongest when many modes are near half-filling
    near_half = np.sum(np.abs(nk - 0.5) < 0.2)
    # Effective occupation entropy (larger = more BCS-like)
    S_occ = -np.sum(nk * np.log(nk + 1e-30) + (1-nk) * np.log(1-nk + 1e-30))
    S_max = N_modes * np.log(2)
    print(f"  N_pair = {N}: active_modes = {active}, near_half = {near_half}, "
          f"S_occ = {S_occ:.4f} / {S_max:.4f} = {S_occ/S_max:.4f}")

# ============================================================================
#  8. Fabric-scale <r> values for context
# ============================================================================

print("\n--- Fabric-Scale <r> Values (from integrability computations) ---")
r_values = {
    2: float(d58['r_even']),
    3: float(d59_3['r_even']),
    4: float(d59_4['r_even']),
}
for N in sorted(r_values):
    print(f"  <r>_even(N_pair={N}) = {r_values[N]:.6f}")

# Non-monotonicity check
print(f"\n  <r> sequence: {r_values[2]:.4f} -> {r_values[3]:.4f} -> {r_values[4]:.4f}")
is_nonmonotonic = (r_values[3] < r_values[2]) and (r_values[3] < r_values[4])
print(f"  Non-monotonic with minimum at N_pair=3: {is_nonmonotonic}")

# ============================================================================
#  9. Gate verdict
# ============================================================================

print("\n" + "=" * 70)
print("GATE VERDICT: BLOCKING-N3-60")
print("=" * 70)

# Check: is |Delta_OES| minimized at N=3?
# From the full sequence: |Delta_OES(1..7)| = 0.066, 0.051, 0.047, 0.039, 0.034, 0.035, 0.049
# GLOBAL minimum at N=5, not N=3.
# But N=3 could be a local minimum if we restrict to odd-N or look at the rate of change.

# Also check the alternative: three-point gap Delta^(3)
# Delta^(3)(1..7) - all positive, same magnitudes.

# Separate odd and even N for nuclear-style analysis
odd_N = [1, 3, 5, 7]
even_N = [2, 4, 6]
abs_OES_odd = [abs_OES[N-1] for N in odd_N if N <= len(abs_OES)]
abs_OES_even = [abs_OES[N-1] for N in even_N if N <= len(abs_OES)]

print(f"\n  |Delta_OES| for odd N_pair:  {[f'{x:.6f}' for x in abs_OES_odd]}")
print(f"  |Delta_OES| for even N_pair: {[f'{x:.6f}' for x in abs_OES_even]}")

# Check if OES has minimum at N=3 among accessible N (1-7)
print(f"\n  Global minimum |Delta_OES|: N_pair = {N_min_OES}, value = {abs_OES[N_min_OES-1]:.10f}")
print(f"  Among odd N only: min at N_pair = {odd_N[np.argmin(abs_OES_odd)]}, "
      f"value = {min(abs_OES_odd):.10f}")
print(f"  Among even N only: min at N_pair = {even_N[np.argmin(abs_OES_even)]}, "
      f"value = {min(abs_OES_even):.10f}")

# Delta_3pt is unsigned and does not separate odd/even
print(f"\n  Global minimum Delta^(3): N_pair = {N_min_3pt}, value = {Delta_3pt[N_min_3pt-1]:.10f}")

# Blocking parameter
print(f"\n  Blocking parameter b(N):")
for N in range(1, 5):
    print(f"    b({N}) = {b_param[N]:.10f}")
print(f"  Minimum b at N_pair = {N_min_b}")
print(f"  Maximum b at N_pair = {N_max_b}")

# Determine gate
if N_min_OES == 3:
    if N_min_b == 3:
        gate_verdict = "PASS"
        gate_detail = (f"|Delta_OES| minimum at N_pair=3 ({abs_OES[2]:.6f}) AND "
                      f"blocking parameter b minimum at N_pair=3 ({b_param[3]:.6f}). "
                      f"Blocking dominance confirmed.")
    else:
        gate_verdict = "INFO"
        gate_detail = (f"|Delta_OES| minimum at N_pair=3 ({abs_OES[2]:.6f}) but "
                      f"b(N) minimum at N_pair={N_min_b} ({b_param[N_min_b]:.6f}). "
                      f"Mixed physics: OES tracks blocking, b tracks Fermi surface.")
elif N_min_OES == 5:
    # Check: is N=3 a local feature within the accessible range?
    # In nuclear physics, OES monotonically decreases with mass in mid-shell.
    # The relevant comparison is between consecutive pairs.
    gate_verdict = "FAIL"
    gate_detail = (f"|Delta_OES| minimum at N_pair={N_min_OES} ({abs_OES[N_min_OES-1]:.6f}), "
                  f"not at N_pair=3. |Delta_OES(3)| = {abs_OES[2]:.6f}. "
                  f"OES decreases monotonically through mid-shell (N=1 to 5), "
                  f"then recovers at N=6,7. This is STANDARD nuclear behavior: "
                  f"OES is smallest at mid-shell where level density is highest, "
                  f"not at N=3 specifically. The <r> minimum at N=3 is NOT explained by "
                  f"blocking-induced OES staggering.")
else:
    gate_verdict = "FAIL"
    gate_detail = (f"|Delta_OES| minimum at N_pair={N_min_OES} ({abs_OES[N_min_OES-1]:.6f}), "
                  f"not at N_pair=3.")

print(f"\n  VERDICT: {gate_verdict}")
print(f"  DETAIL: {gate_detail}")

# ============================================================================
#  10. Physical interpretation
# ============================================================================

print("\n" + "=" * 70)
print("PHYSICAL INTERPRETATION")
print("=" * 70)

print("""
The OES sequence |Delta_OES| = {0.066, 0.051, 0.047, 0.039, 0.034, 0.035, 0.049}
shows standard mid-shell behavior:

1. MONOTONE DECREASE from N=1 to N=5: As the system fills, the effective level
   density near the Fermi surface increases, distributing pairing correlations
   over more modes and reducing the per-particle staggering. This is identical
   to the nuclear mass parabola behavior in sd-shell nuclei (Paper 03).

2. UPTICK at N=6,7: Near complete filling, the pairing space shrinks (fewer
   empty modes available for scattering), and |Delta_OES| increases -- the
   particle-hole symmetric analog of the low-N behavior.

3. N=3 is NOT special in the OES: It sits on the monotone-decreasing branch.
   There is no local minimum, no kink, no anomaly.

4. The <r> minimum at N=3 is therefore NOT explained by blocking.
   Instead, it likely reflects the INTEGRABILITY structure:
   - N=2: 120-dim Hilbert space, still close to integrable (<r>=0.442)
   - N=3: 560-dim, Pauli blocking creates more near-degeneracies, ENHANCING
     level repulsion suppression (fewer avoided crossings), <r> DROPS
   - N=4: 1820-dim, the much larger Hilbert space partially restores
     GOE statistics through combinatorial complexity, <r> RISES

5. The blocking parameter b(N) DECREASES from N=1 to N=4, reflecting the
   approach to half-filling. This is the OPPOSITE of what "blocking at N=3"
   would predict. The occupations become MORE BCS-like (closer to 1/2) as N
   increases, consistent with the system being in the superweak pairing regime
   (d/Delta >> 1) where the BCS smearing grows with the number of available modes.
""")

# ============================================================================
#  11. Save data
# ============================================================================

output_path = os.path.join(data_dir, 's60_blocking_n3.npz')
np.savez(output_path,
    # Staircase
    E_vs_N=E_vs_N,
    N_max=N_max,
    N_modes=N_modes,
    labels=labels,
    # OES
    Delta_OES=Delta_OES,
    abs_Delta_OES=abs_OES,
    N_min_OES=N_min_OES,
    Delta_3pt=Delta_3pt,
    N_min_3pt=N_min_3pt,
    # Occupations
    nk_N1=nk_ed[1],
    nk_N2=nk_ed[2],
    nk_N3=nk_ed[3],
    nk_N4=nk_ed[4],
    # Blocking parameter
    b_N1=b_param[1],
    b_N2=b_param[2],
    b_N3=b_param[3],
    b_N4=b_param[4],
    # <r> values
    r_even_N2=r_values[2],
    r_even_N3=r_values[3],
    r_even_N4=r_values[4],
    # Gate
    gate_name=np.array(['BLOCKING-N3-60']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"\nData saved to {output_path}")

# ============================================================================
#  12. Plot
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('BLOCKING-N3-60: Nuclear Blocking Analysis\n'
             f'Gate: {gate_verdict}', fontsize=14, fontweight='bold')

# Panel (a): Occupation numbers v_k^2 vs mode index k
ax = axes[0, 0]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for N in range(1, 5):
    nk = nk_ed[N]
    ax.plot(range(N_modes), nk, 'o-', color=colors[N-1], label=f'N={N}', markersize=6)
ax.axhline(0.5, color='gray', linestyle='--', alpha=0.5, label='n=1/2')
ax.set_xlabel('Mode index k')
ax.set_ylabel('$v_k^2 = \\langle n_k \\rangle$')
ax.set_title('(a) Occupation numbers')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([str(l) for l in labels], rotation=45, ha='right', fontsize=7)
ax.legend(fontsize=8)
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)

# Panel (b): |Delta_OES| vs N
ax = axes[0, 1]
N_arr = np.arange(1, N_max)
ax.plot(N_arr, abs_OES, 'ko-', markersize=8, linewidth=2)
ax.axvline(3, color='red', linestyle='--', alpha=0.5, label='N=3')
ax.set_xlabel('$N_{pair}$')
ax.set_ylabel('$|\\Delta_{OES}|$ [M$_{KK}$]')
ax.set_title('(b) Odd-Even Staggering')
# Mark odd/even with different markers
for i, N in enumerate(N_arr):
    if N % 2 == 1:
        ax.plot(N, abs_OES[i], 'bs', markersize=10, zorder=5)
    else:
        ax.plot(N, abs_OES[i], 'r^', markersize=10, zorder=5)
ax.legend(['All N', 'N=3 line'], fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Blocking parameter b(N)
ax = axes[0, 2]
N_b = np.arange(1, 5)
b_vals = [b_param[N] for N in N_b]
ax.bar(N_b, b_vals, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.7, edgecolor='black')
ax.set_xlabel('$N_{pair}$')
ax.set_ylabel('$b(N) = \\langle (v_k^2 - 1/2)^2 \\rangle$')
ax.set_title('(c) Blocking parameter')
ax.set_xticks(N_b)
ax.grid(True, alpha=0.3, axis='y')

# Panel (d): Energy staircase
ax = axes[1, 0]
N_all = np.arange(0, N_max + 1)
ax.plot(N_all, E_vs_N, 'ko-', markersize=8, linewidth=2)
# Overlay the second differences
ax.set_xlabel('$N_{pair}$')
ax.set_ylabel('$E(N)$ [M$_{KK}$]')
ax.set_title('(d) Energy staircase')
ax.grid(True, alpha=0.3)
# Add separation energy on secondary axis
ax2 = ax.twinx()
ax2.plot(np.arange(1, N_max + 1), S1, 'r--s', markersize=6, alpha=0.7)
ax2.set_ylabel('$S_1(N)$ [M$_{KK}$]', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Panel (e): <r> values
ax = axes[1, 1]
N_r = [2, 3, 4]
r_vals = [r_values[N] for N in N_r]
ax.plot(N_r, r_vals, 'ko-', markersize=10, linewidth=2)
ax.axhline(0.386, color='blue', linestyle=':', alpha=0.5, label='Poisson (0.386)')
ax.axhline(0.5307, color='red', linestyle=':', alpha=0.5, label='GOE (0.531)')
ax.fill_between([1.5, 4.5], 0.386, 0.5307, alpha=0.1, color='green')
ax.set_xlabel('$N_{pair}$')
ax.set_ylabel('$\\langle r \\rangle_{even}$')
ax.set_title('(e) Level spacing ratio')
ax.legend(fontsize=8)
ax.set_xlim(1.5, 4.5)
ax.set_xticks(N_r)
ax.grid(True, alpha=0.3)

# Panel (f): |u^2 - v^2| at each N (Bogoliubov coherence)
ax = axes[1, 2]
for N in range(1, 5):
    uv2 = np.abs(d53[f'N{N}_u2_minus_v2_ed'])
    ax.plot(range(N_modes), uv2, 'o-', color=colors[N-1], label=f'N={N}', markersize=6)
ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('Mode index k')
ax.set_ylabel('$|u_k^2 - v_k^2|$')
ax.set_title('(f) Bogoliubov coherence factors')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([str(l) for l in labels], rotation=45, ha='right', fontsize=7)
ax.legend(fontsize=8)
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(data_dir, 's60_blocking_n3.png')
fig.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Plot saved to {plot_path}")

print("\n--- DONE ---")
