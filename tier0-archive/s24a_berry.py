"""
Session 24a Step 2: Intra-Sector Berry Curvature
==================================================

B_n(tau) = sum_{m != n} |V_nm(tau)|^2 / (E_n(tau) - E_m(tau))^2

where V_nm is the Kosmann derivative matrix element and E_n are eigenvalues
of the (0,0) singlet sector.

Focus: n = gap-edge Kramers pair (indices from gap_edge_indices).

Data source: s23a_kosmann_singlet.npz
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# =====================================================================
# LOAD DATA
# =====================================================================
base = "C:/sandbox/Ainulindale Exflation/tier0-computation"
d = np.load(f"{base}/s23a_kosmann_singlet.npz")

tau_values = d['tau_values']  # shape (9,)
n_tau = len(tau_values)

print("=" * 60)
print("STEP 2: Intra-Sector Berry Curvature")
print("=" * 60)
print(f"tau values: {tau_values}")

# =====================================================================
# COMPUTE BERRY CURVATURE
# =====================================================================
# For each tau, we need:
#   - eigenvalues (16,)
#   - K_a_matrix (Kosmann derivative, 16x16) for each of 8 generators
#   - gap_edge_indices (2,): indices of gap-edge Kramers pair

B_gap_edge = np.zeros((n_tau, 2))  # Berry curvature for the 2 gap-edge states
B_all = np.zeros((n_tau, 16))      # Berry curvature for all 16 states

for t_idx in range(n_tau):
    evals = d[f'eigenvalues_{t_idx}']  # shape (16,)
    gap_idx = d[f'gap_edge_indices_{t_idx}']  # shape (2,)

    # Sum Berry curvature over all 8 generators
    B_n = np.zeros(16)
    for a in range(8):
        K_a = d[f'K_a_matrix_{t_idx}_{a}']  # shape (16, 16), complex
        # |V_nm|^2 = |K_a_nm|^2
        V_sq = np.abs(K_a)**2  # shape (16, 16)

        for n in range(16):
            for m in range(16):
                if m == n:
                    continue
                dE = evals[n] - evals[m]
                if abs(dE) < 1e-14:
                    continue  # skip degenerate pairs
                B_n[n] += V_sq[n, m] / dE**2

    B_all[t_idx] = B_n
    B_gap_edge[t_idx, 0] = B_n[gap_idx[0]]
    B_gap_edge[t_idx, 1] = B_n[gap_idx[1]]

    print(f"  tau={tau_values[t_idx]:.2f}: gap_edge=[{gap_idx[0]},{gap_idx[1]}], "
          f"B_1={B_gap_edge[t_idx,0]:.6f}, B_2={B_gap_edge[t_idx,1]:.6f}, "
          f"max_B={B_n.max():.6f}, min_B={B_n.min():.6f}")

# =====================================================================
# PEAK ANALYSIS
# =====================================================================
print("\n--- Peak Analysis ---")
for k in range(2):
    peak_idx = np.argmax(B_gap_edge[:, k])
    print(f"  Gap-edge state {k+1}: peak B = {B_gap_edge[peak_idx, k]:.6f} at tau = {tau_values[peak_idx]:.2f}")

# Overall peak across all states
for t_idx in range(n_tau):
    peak_state = np.argmax(B_all[t_idx])
    print(f"  tau={tau_values[t_idx]:.2f}: max B over all states = {B_all[t_idx].max():.6f} at state {peak_state}")

# =====================================================================
# SAVE
# =====================================================================
np.savez(f"{base}/s24a_berry.npz",
         tau=tau_values,
         B_gap_edge=B_gap_edge,
         B_all=B_all)
print(f"\nSaved: {base}/s24a_berry.npz")

# =====================================================================
# PLOT
# =====================================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: gap-edge Berry curvature
ax = axes[0]
ax.plot(tau_values, B_gap_edge[:, 0], 'b-o', linewidth=2, markersize=8, label='Gap-edge state 1')
ax.plot(tau_values, B_gap_edge[:, 1], 'r-s', linewidth=2, markersize=8, label='Gap-edge state 2')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('B_n(tau)', fontsize=12)
ax.set_title('Berry Curvature — Gap-Edge Kramers Pair', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Right: heatmap of all 16 states
ax2 = axes[1]
im = ax2.imshow(B_all.T, aspect='auto', origin='lower',
                extent=[tau_values[0], tau_values[-1], -0.5, 15.5],
                cmap='hot')
ax2.set_xlabel('tau', fontsize=12)
ax2.set_ylabel('State index n', fontsize=12)
ax2.set_title('Berry Curvature B_n(tau) — All States', fontsize=13)
plt.colorbar(im, ax=ax2, label='B_n')

plt.tight_layout()
plt.savefig(f"{base}/s24a_berry.png", dpi=150)
print(f"Saved: {base}/s24a_berry.png")

print("\n" + "=" * 60)
print("STEP 2 COMPLETE")
print("=" * 60)
