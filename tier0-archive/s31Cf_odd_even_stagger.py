"""
N-31Cf: Odd-Even Staggering Diagnostic
=======================================
Computes the third finite difference of the SU(3) Dirac eigenvalue sequence:

  Delta^(3)(N, tau) = (-1)^N * [lambda_{N+1} - 2*lambda_N + lambda_{N-1}] / 2

This is the spectral analog of odd-even mass staggering in nuclear physics
(Nazarewicz Paper 03). Large Delta^(3) indicates strong pairing correlations
(alternating level density near the gap edge).

Gate N-31Cf-G: INFORMATIVE if Delta^(3) shows sharp peak/sign-change at gap edge
for tau in [0.15, 0.25].

Input: s23a_gap_equation.npz, s30b_full_spectrum.npz, s23a_kosmann_singlet.npz
Output: s31Cf_odd_even_stagger.{npz,png}
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time

t0 = time.time()

data_dir = os.path.dirname(__file__)

# --- Load data ---
gap_data = np.load(os.path.join(data_dir, 's23a_gap_equation.npz'), allow_pickle=True)
kosmann_data = np.load(os.path.join(data_dir, 's23a_kosmann_singlet.npz'), allow_pickle=True)

tau_values = gap_data['tau_values']
n_tau = len(tau_values)

# Extract eigenvalues and gap-edge info
eigenvalues_list = []
lambda_mins = []
gap_edge_indices = []

for i in range(n_tau):
    evals = gap_data[f'eigenvalues_{i}']
    eigenvalues_list.append(evals)
    lambda_mins.append(float(gap_data[f'lambda_min_{i}']))
    gap_edge_indices.append(kosmann_data[f'gap_edge_indices_{i}'])

# --- Compute Delta^(3) ---
# Sort eigenvalues by absolute value at each tau
delta3_all = []
sorted_evals_all = []
max_delta3 = np.zeros(n_tau)
max_delta3_pos = np.zeros(n_tau, dtype=int)
integrated_S = np.zeros(n_tau)
gap_edge_N = np.zeros(n_tau, dtype=int)  # position of gap edge in sorted order

for i_tau in range(n_tau):
    evals = eigenvalues_list[i_tau]
    lmin = lambda_mins[i_tau]

    # Sort by absolute value
    sorted_idx = np.argsort(np.abs(evals))
    sorted_evals = np.abs(evals[sorted_idx])
    sorted_evals_all.append(sorted_evals)

    n_modes = len(sorted_evals)

    # Find gap-edge position in sorted order
    # Gap edge is at lambda_min; find which sorted index corresponds to it
    gap_N = np.argmin(np.abs(sorted_evals - lmin))
    gap_edge_N[i_tau] = gap_N

    # Compute Delta^(3)(N) for N = 1, ..., n_modes-2
    delta3 = np.zeros(n_modes)
    for N in range(1, n_modes - 1):
        delta3[N] = ((-1)**N) * (sorted_evals[N+1] - 2*sorted_evals[N] + sorted_evals[N-1]) / 2.0
    delta3_all.append(delta3)

    # Max |Delta^(3)| and its position
    abs_delta3 = np.abs(delta3[1:-1])  # exclude boundary artifacts
    if len(abs_delta3) > 0:
        max_pos = np.argmax(abs_delta3) + 1
        max_delta3[i_tau] = abs_delta3[max_pos - 1]
        max_delta3_pos[i_tau] = max_pos

    # Integrated staggering S(tau) = sum |Delta^(3)|
    integrated_S[i_tau] = np.sum(np.abs(delta3[1:-1]))

# --- Print results ---
print("=== N-31Cf: Odd-Even Staggering Results ===")
print(f"\n{'tau':>6s}  {'lambda_min':>10s}  {'gap_edge_N':>10s}  {'max|D3|':>10s}  {'max_pos':>8s}  {'S(tau)':>10s}")
for i_tau in range(n_tau):
    print(f"{tau_values[i_tau]:6.2f}  {lambda_mins[i_tau]:10.4f}  {gap_edge_N[i_tau]:10d}  {max_delta3[i_tau]:10.6f}  {max_delta3_pos[i_tau]:8d}  {integrated_S[i_tau]:10.6f}")

# Check for sharp features at gap edge in tau [0.15, 0.25]
print("\n=== Delta^(3) at and near gap edge ===")
for i_tau in range(n_tau):
    tau = tau_values[i_tau]
    gN = gap_edge_N[i_tau]
    d3 = delta3_all[i_tau]
    print(f"\ntau={tau:.2f}, gap_edge_N={gN}:")
    for N in range(max(1, gN-3), min(len(d3)-1, gN+4)):
        marker = " <-- GAP EDGE" if N == gN else ""
        print(f"  N={N:2d}: Delta^(3) = {d3[N]:+.6f}  |lambda_N|={sorted_evals_all[i_tau][N]:.4f}{marker}")

# --- Gate N-31Cf-G Assessment ---
tau_window = (tau_values >= 0.15) & (tau_values <= 0.25)
tau_window_idx = np.where(tau_window)[0]

# Check for sharp features: Delta^(3) peak at or near gap edge
sharp_feature = False
max_ratio_at_gap = 0.0
for i_tau in tau_window_idx:
    gN = gap_edge_N[i_tau]
    d3 = delta3_all[i_tau]
    # Is the max |Delta^(3)| within 2 positions of gap edge?
    if abs(max_delta3_pos[i_tau] - gN) <= 2:
        sharp_feature = True
    # Ratio of |Delta^(3)| at gap edge vs mean
    mean_d3 = np.mean(np.abs(d3[1:-1]))
    if mean_d3 > 0:
        gap_ratio = np.abs(d3[gN]) / mean_d3
        max_ratio_at_gap = max(max_ratio_at_gap, gap_ratio)

# Also check sign change
sign_changes_at_gap = 0
for i_tau in tau_window_idx:
    gN = gap_edge_N[i_tau]
    d3 = delta3_all[i_tau]
    if gN > 1 and gN < len(d3) - 1:
        if d3[gN-1] * d3[gN] < 0 or d3[gN] * d3[gN+1] < 0:
            sign_changes_at_gap += 1

# S(tau) peak assessment
S_peak_idx = np.argmax(integrated_S)
S_peak_in_window = S_peak_idx in tau_window_idx

print(f"\n=== GATE N-31Cf-G ===")
print(f"Sharp Delta^(3) peak at gap edge (within 2 positions): {sharp_feature}")
print(f"Max |Delta^(3)(gap)| / mean |Delta^(3)|: {max_ratio_at_gap:.4f}")
print(f"Sign changes at gap edge in [0.15,0.25]: {sign_changes_at_gap}/{len(tau_window_idx)}")
print(f"Integrated S(tau) peak at tau={tau_values[S_peak_idx]:.2f} (in window: {S_peak_in_window})")
print(f"S(tau) values: {['%.6f' % s for s in integrated_S]}")

if sharp_feature or max_ratio_at_gap > 2.0 or sign_changes_at_gap > 0:
    gate_verdict = "INFORMATIVE"
    print(f"Gate verdict: N-31Cf-G = INFORMATIVE (sharp spectral structure at gap edge)")
else:
    gate_verdict = "FEATURELESS"
    print(f"Gate verdict: N-31Cf-G = FEATURELESS (no special structure at gap edge)")

# --- Save ---
save_dict = {
    'tau_values': tau_values,
    'lambda_mins': np.array(lambda_mins),
    'gap_edge_N': gap_edge_N,
    'max_delta3': max_delta3,
    'max_delta3_pos': max_delta3_pos,
    'integrated_S': integrated_S,
    'gate_verdict': np.array(gate_verdict),
    'max_ratio_at_gap': np.array(max_ratio_at_gap),
    'sign_changes_at_gap': np.array(sign_changes_at_gap),
}
for i_tau in range(n_tau):
    save_dict[f'delta3_{i_tau}'] = delta3_all[i_tau]
    save_dict[f'sorted_evals_{i_tau}'] = sorted_evals_all[i_tau]

np.savez(os.path.join(data_dir, 's31Cf_odd_even_stagger.npz'), **save_dict)
print(f"\nSaved s31Cf_odd_even_stagger.npz")

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Delta^(3) heatmap over (N, tau)
ax = axes[0, 0]
n_modes_max = max(len(d) for d in delta3_all)
d3_matrix = np.zeros((n_tau, n_modes_max))
for i_tau in range(n_tau):
    d3 = delta3_all[i_tau]
    d3_matrix[i_tau, :len(d3)] = d3

# Use only valid modes (1 to n_modes-2)
im = ax.imshow(d3_matrix[:, 1:-1].T, aspect='auto', cmap='RdBu_r',
               extent=[tau_values[0], tau_values[-1], 1, n_modes_max-2],
               origin='lower', vmin=-np.max(np.abs(d3_matrix[:, 1:-1])),
               vmax=np.max(np.abs(d3_matrix[:, 1:-1])))
# Overlay gap edge
ax.plot(tau_values, gap_edge_N, 'k-o', markersize=4, label='gap edge')
ax.set_xlabel('tau')
ax.set_ylabel('Mode index N')
ax.set_title('Delta^(3)(N, tau) heatmap')
ax.legend()
plt.colorbar(im, ax=ax, label='Delta^(3)')

# Panel 2: Delta^(3) at gap edge vs tau
ax = axes[0, 1]
d3_at_gap = np.array([delta3_all[i][gap_edge_N[i]] for i in range(n_tau)])
ax.plot(tau_values, d3_at_gap, 'b-o', markersize=6, label='Delta^(3) at gap edge')
ax.plot(tau_values, max_delta3, 'r--s', markersize=4, label='max |Delta^(3)|')
ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax.axvspan(0.15, 0.25, alpha=0.1, color='yellow', label='tau window')
ax.set_xlabel('tau')
ax.set_ylabel('Delta^(3)')
ax.set_title('Delta^(3) at gap edge vs tau')
ax.legend()

# Panel 3: Integrated staggering S(tau)
ax = axes[1, 0]
ax.plot(tau_values, integrated_S, 'g-o', markersize=6)
ax.axvspan(0.15, 0.25, alpha=0.1, color='yellow', label='tau window')
ax.set_xlabel('tau')
ax.set_ylabel('S(tau) = sum |Delta^(3)|')
ax.set_title('Integrated staggering signal')
ax.legend()

# Panel 4: Delta^(3)(N) profiles at selected tau
ax = axes[1, 1]
for i_tau in [0, 2, 3, 4, 8]:  # tau = 0, 0.15, 0.20, 0.25, 0.50
    d3 = delta3_all[i_tau]
    N_range = np.arange(len(d3))
    ax.plot(N_range[1:-1], d3[1:-1], '-', label=f'tau={tau_values[i_tau]:.2f}', alpha=0.7)
    gN = gap_edge_N[i_tau]
    ax.plot(gN, d3[gN], 'ko', markersize=6)
ax.axhline(0, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('Mode index N')
ax.set_ylabel('Delta^(3)(N)')
ax.set_title('Delta^(3) profiles (dots = gap edge)')
ax.legend()

fig.suptitle(f'N-31Cf: Odd-Even Staggering | Gate: {gate_verdict}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's31Cf_odd_even_stagger.png'), dpi=150, bbox_inches='tight')
print(f"Saved s31Cf_odd_even_stagger.png")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.2f}s")
