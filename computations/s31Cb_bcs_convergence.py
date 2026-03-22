"""
N-31Cb: BCS Convergence with Truncation Level (Berggren Analog)
================================================================
Tests whether the BCS gap equation result changes as we include more
modes from the SU(3) Dirac spectrum.

The 16 singlet modes at each tau split into 3 eigenvalue groups:
  - Group A: 2 modes at lambda_min (gap-edge)
  - Group B: 8 modes at intermediate eigenvalue
  - Group C: 6 modes at highest eigenvalue

Truncation levels:
  N_eff = 2:  Group A only (gap-edge 2-mode, matches K-1e "gap2")
  N_eff = 10: Groups A+B (10-mode, matches K-1e "gap10")
  N_eff = 16: All groups (full basis, matches K-1e "full16")

We use CONSTANT coupling (per N-31Ca-G FAIL verdict).

Additionally, we test the SCALING of M_max with N_eff by studying the
V_matrix sub-blocks and their eigenvalue spectra.

Gate N-31Cb-G: PASS if M_max at mu=0 shows monotonic INCREASE with N_eff
AND extrapolated M_inf > 0.5. FAIL if M_max decreases or converges to < 0.1.

Input: s23a_gap_equation.npz, s23a_kosmann_singlet.npz
Output: s31Cb_bcs_convergence.{npz,png}
"""

import numpy as np
from numpy.linalg import eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os, time

t0 = time.time()

data_dir = os.path.dirname(__file__)
gap_data = np.load(os.path.join(data_dir, 's23a_gap_equation.npz'), allow_pickle=True)

tau_values = gap_data['tau_values']
n_tau = len(tau_values)

# --- Already-computed M_max at 3 truncation levels (from K-1e) ---
print("=== K-1e BASELINE: M_max at 3 truncation levels ===")
print(f"{'tau':>6s}  {'N=2 (mu=0)':>12s}  {'N=10 (mu=0)':>12s}  {'N=16 (mu=0)':>12s}  {'N=2 (mu=lmin)':>14s}  {'N=10 (mu=lmin)':>14s}  {'N=16 (mu=lmin)':>14s}")

M_mu0 = np.zeros((n_tau, 3))  # 3 truncation levels
M_mugap = np.zeros((n_tau, 3))
N_eff_values = np.array([2, 10, 16])

for i in range(n_tau):
    M_mu0[i, 0] = float(gap_data[f'M_max_gap2_mu=0_{i}'])
    M_mu0[i, 1] = float(gap_data[f'M_max_gap10_mu=0_{i}'])
    M_mu0[i, 2] = float(gap_data[f'M_max_full16_mu=0_{i}'])
    M_mugap[i, 0] = float(gap_data[f'M_max_gap2_mu=+lmin_{i}'])
    M_mugap[i, 1] = float(gap_data[f'M_max_gap10_mu=+lmin_{i}'])
    M_mugap[i, 2] = float(gap_data[f'M_max_full16_mu=+lmin_{i}'])
    print(f"{tau_values[i]:6.2f}  {M_mu0[i,0]:12.6f}  {M_mu0[i,1]:12.6f}  {M_mu0[i,2]:12.6f}  "
          f"{M_mugap[i,0]:14.6f}  {M_mugap[i,1]:14.6f}  {M_mugap[i,2]:14.6f}")

# --- Eigenvalue spectrum of V sub-blocks ---
print("\n=== V_matrix eigenvalue spectra at sub-truncation levels ===")
V_eig_all = np.zeros((n_tau, 3))  # max|eig(V_sub)| at each truncation

for i in range(n_tau):
    V = gap_data[f'V_matrix_{i}']
    V_sym = (V + V.T) / 2
    evals = np.sort(np.abs(gap_data[f'eigenvalues_{i}']))

    # Identify group boundaries
    tol = 1e-6
    groups = []
    current = [0]
    for j in range(1, len(evals)):
        if abs(evals[j] - evals[j-1]) < tol:
            current.append(j)
        else:
            groups.append(current)
            current = [j]
    groups.append(current)

    # N=2: first 2 modes (gap-edge)
    idx2 = list(range(min(2, len(evals))))
    if len(idx2) >= 2:
        V_sub2 = V_sym[np.ix_(idx2, idx2)]
        eig2 = eigvalsh(V_sub2)
        V_eig_all[i, 0] = np.max(np.abs(eig2))
    else:
        V_eig_all[i, 0] = 0.0

    # N=10: first 10 modes
    if len(groups) >= 2:
        idx10 = groups[0] + groups[1]
    else:
        idx10 = list(range(min(10, len(evals))))
    V_sub10 = V_sym[np.ix_(idx10, idx10)]
    eig10 = eigvalsh(V_sub10)
    V_eig_all[i, 1] = np.max(np.abs(eig10))

    # N=16: all groups
    eig16 = eigvalsh(V_sym)
    V_eig_all[i, 2] = np.max(np.abs(eig16))

    print(f"tau={tau_values[i]:.2f}: max|eig(V_sub)|: N=2: {V_eig_all[i,0]:.6f}, "
          f"N=10: {V_eig_all[i,1]:.6f}, N=16: {V_eig_all[i,2]:.6f}")

# --- Convergence analysis ---
print("\n=== CONVERGENCE ANALYSIS ===")

# Check monotonicity of M_max(mu=0) with N_eff
monotonic_mu0 = np.zeros(n_tau, dtype=bool)
monotonic_mugap = np.zeros(n_tau, dtype=bool)
for i in range(n_tau):
    # mu=0: check if M increases with N
    monotonic_mu0[i] = (M_mu0[i, 1] >= M_mu0[i, 0]) and (M_mu0[i, 2] >= M_mu0[i, 1])
    # mu=lmin: check if M increases with N
    monotonic_mugap[i] = (M_mugap[i, 1] >= M_mugap[i, 0]) and (M_mugap[i, 2] >= M_mugap[i, 1])

print(f"\nMonotonic increase of M_max(mu=0) with N_eff:")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: {monotonic_mu0[i]} "
          f"(M_2={M_mu0[i,0]:.6f} -> M_10={M_mu0[i,1]:.6f} -> M_16={M_mu0[i,2]:.6f})")

print(f"\nMonotonic increase of M_max(mu=lmin) with N_eff:")
for i in range(n_tau):
    print(f"  tau={tau_values[i]:.2f}: {monotonic_mugap[i]} "
          f"(M_2={M_mugap[i,0]:.6f} -> M_10={M_mugap[i,1]:.6f} -> M_16={M_mugap[i,2]:.6f})")

# --- Extrapolation ---
# Fit M_max(N) = M_inf + a/N^b at each tau for mu=0
print("\n=== EXTRAPOLATION (power law) ===")

def power_law(N, M_inf, a, b):
    return M_inf + a / N**b

M_inf_mu0 = np.zeros(n_tau)
M_inf_mugap = np.zeros(n_tau)
fit_success_mu0 = np.zeros(n_tau, dtype=bool)
fit_success_mugap = np.zeros(n_tau, dtype=bool)

for i in range(n_tau):
    # mu=0
    try:
        if M_mu0[i, 2] > M_mu0[i, 0]:  # increasing trend
            popt, _ = curve_fit(power_law, N_eff_values.astype(float), M_mu0[i, :],
                               p0=[M_mu0[i, 2], -0.01, 1.0], maxfev=5000)
            M_inf_mu0[i] = popt[0]
            fit_success_mu0[i] = True
        else:
            M_inf_mu0[i] = M_mu0[i, 2]  # use N=16 as estimate
    except:
        M_inf_mu0[i] = M_mu0[i, 2]

    # mu=lmin
    try:
        if M_mugap[i, 2] > M_mugap[i, 0]:
            popt, _ = curve_fit(power_law, N_eff_values.astype(float), M_mugap[i, :],
                               p0=[M_mugap[i, 2], -1.0, 1.0], maxfev=5000)
            M_inf_mugap[i] = popt[0]
            fit_success_mugap[i] = True
        else:
            M_inf_mugap[i] = M_mugap[i, 2]
    except:
        M_inf_mugap[i] = M_mugap[i, 2]

    print(f"tau={tau_values[i]:.2f}: M_inf(mu=0) = {M_inf_mu0[i]:.6f} (fit: {fit_success_mu0[i]}), "
          f"M_inf(mu=lmin) = {M_inf_mugap[i]:.6f} (fit: {fit_success_mugap[i]})")

# --- Also compare M_max from V eigenvalues (Metric A from N-31Ca) ---
print("\n=== V_eff EIGENVALUE CONVERGENCE (Metric A) ===")
V_eig_monotonic = np.zeros(n_tau, dtype=bool)
for i in range(n_tau):
    V_eig_monotonic[i] = (V_eig_all[i, 1] >= V_eig_all[i, 0]) and (V_eig_all[i, 2] >= V_eig_all[i, 1])
    print(f"tau={tau_values[i]:.2f}: Monotonic={V_eig_monotonic[i]}, "
          f"V2={V_eig_all[i,0]:.6f} -> V10={V_eig_all[i,1]:.6f} -> V16={V_eig_all[i,2]:.6f}")

# --- Additional: convergence rate ---
# Compare (M_16 - M_10) / (M_10 - M_2) to see if convergence is accelerating/decelerating
print("\n=== CONVERGENCE RATE (ratio of increments) ===")
for i in range(n_tau):
    d1 = M_mu0[i, 1] - M_mu0[i, 0]
    d2 = M_mu0[i, 2] - M_mu0[i, 1]
    if abs(d1) > 1e-10:
        ratio = d2 / d1
    else:
        ratio = 0
    print(f"tau={tau_values[i]:.2f}: (M_16-M_10)/(M_10-M_2) = {ratio:.4f} at mu=0")

# --- Gate N-31Cb-G ---
print("\n=== GATE N-31Cb-G ===")

# Check: M_max at mu=0 monotonically increasing with N_eff at tau in [0.15, 0.25]
tau_window = (tau_values >= 0.15) & (tau_values <= 0.25)
tau_idx = np.where(tau_window)[0]

all_monotonic = all(monotonic_mu0[i] for i in tau_idx)
all_M_inf_above_05 = all(M_inf_mu0[i] > 0.5 for i in tau_idx)

# The M_max at mu=0 from K-1e:
# tau=0.15: M_2=0, M_10=0, M_16=0.098
# tau=0.20: M_2=0, M_10=0, M_16=0.104
# tau=0.25: M_2=0, M_10=0, M_16=0.111
# This is NOT monotonically increasing: M_2 = M_10 = 0, M_16 > 0
# Technically it IS monotonically non-decreasing. But M_inf is ~0.1, far below 0.5.

# Report the actual M_max values at each truncation
print(f"M_max at mu=0 in [0.15, 0.25] window:")
for i in tau_idx:
    print(f"  tau={tau_values[i]:.2f}: M_2={M_mu0[i,0]:.6f}, M_10={M_mu0[i,1]:.6f}, M_16={M_mu0[i,2]:.6f}")
    print(f"    Monotonic: {monotonic_mu0[i]}, M_inf={M_inf_mu0[i]:.6f}")

print(f"\nAll monotonic in window: {all_monotonic}")
print(f"All M_inf > 0.5 in window: {all_M_inf_above_05}")

# V eigenvalue convergence:
print(f"\nV_eff eigenvalue max at each truncation (better metric):")
for i in tau_idx:
    print(f"  tau={tau_values[i]:.2f}: V_2={V_eig_all[i,0]:.6f}, V_10={V_eig_all[i,1]:.6f}, V_16={V_eig_all[i,2]:.6f}")
    print(f"    Monotonic: {V_eig_monotonic[i]}")

# Gate verdict
# M_max at mu=0 does increase with N (monotonically non-decreasing)
# But M_inf < 0.5 at all tau (max is ~0.15)
# V eigenvalue convergence: V increases with N, but tops out at ~0.28
if all_monotonic and all_M_inf_above_05:
    gate_verdict = "PASS"
elif all_monotonic and not all_M_inf_above_05:
    gate_verdict = "FAIL (monotonic but M_inf << 0.5)"
else:
    gate_verdict = "FAIL (not monotonic or M_inf << 0.5)"

# Determine convergence type
max_M16 = np.max(M_mu0[tau_idx, 2])
print(f"\nMax M_max(N=16, mu=0) in window: {max_M16:.6f}")
print(f"Max V_eig(N=16) in window: {np.max(V_eig_all[tau_idx, 2]):.6f}")
print(f"Both are << 1.0. Adding modes helps, but cannot reach threshold.")
print(f"\nGate verdict: N-31Cb-G = {gate_verdict}")

# --- Save ---
save_dict = {
    'tau_values': tau_values,
    'N_eff_values': N_eff_values,
    'M_mu0': M_mu0,
    'M_mugap': M_mugap,
    'V_eig_all': V_eig_all,
    'M_inf_mu0': M_inf_mu0,
    'M_inf_mugap': M_inf_mugap,
    'monotonic_mu0': monotonic_mu0,
    'monotonic_mugap': monotonic_mugap,
    'V_eig_monotonic': V_eig_monotonic,
    'gate_verdict': np.array(gate_verdict),
}
np.savez(os.path.join(data_dir, 's31Cb_bcs_convergence.npz'), **save_dict)
print(f"\nSaved s31Cb_bcs_convergence.npz")

# --- Plot ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: M_max(mu=0) vs N_eff for selected tau
ax = axes[0, 0]
for i in [0, 2, 3, 4, 8]:
    ax.plot(N_eff_values, M_mu0[i, :], '-o', markersize=6,
            label=f'tau={tau_values[i]:.2f}')
ax.axhline(1.0, color='red', linestyle=':', alpha=0.5, label='BCS threshold')
ax.set_xlabel('N_eff (number of modes)')
ax.set_ylabel('M_max (mu=0)')
ax.set_title('BCS M_max at mu=0 vs truncation level')
ax.set_xticks(N_eff_values)
ax.legend()

# Panel 2: M_max(mu=lmin) vs N_eff
ax = axes[0, 1]
for i in [0, 2, 3, 4, 8]:
    ax.plot(N_eff_values, M_mugap[i, :], '-o', markersize=6,
            label=f'tau={tau_values[i]:.2f}')
ax.axhline(1.0, color='red', linestyle=':', alpha=0.5, label='BCS threshold')
ax.set_xlabel('N_eff (number of modes)')
ax.set_ylabel('M_max (mu=lambda_min)')
ax.set_title('BCS M_max at mu=lambda_min vs truncation')
ax.set_xticks(N_eff_values)
ax.legend()

# Panel 3: V eigenvalue convergence
ax = axes[1, 0]
for i in [0, 2, 3, 4, 8]:
    ax.plot(N_eff_values, V_eig_all[i, :], '-s', markersize=6,
            label=f'tau={tau_values[i]:.2f}')
ax.axhline(1.0, color='red', linestyle=':', alpha=0.5, label='BCS threshold')
ax.set_xlabel('N_eff (number of modes)')
ax.set_ylabel('max |eig(V_sub)|')
ax.set_title('Pairing matrix eigenvalue vs truncation')
ax.set_xticks(N_eff_values)
ax.legend()

# Panel 4: M_inf extrapolation and tau dependence
ax = axes[1, 1]
ax.plot(tau_values, M_inf_mu0, 'b-o', label='M_inf (mu=0)')
ax.plot(tau_values, M_mu0[:, 2], 'b--s', alpha=0.5, label='M_16 (mu=0)')
ax.plot(tau_values, M_inf_mugap, 'r-o', label='M_inf (mu=lmin)')
ax.plot(tau_values, M_mugap[:, 2], 'r--s', alpha=0.5, label='M_16 (mu=lmin)')
ax.axhline(0.5, color='green', linestyle=':', alpha=0.5, label='M_inf=0.5 threshold')
ax.axhline(1.0, color='red', linestyle=':', alpha=0.5, label='BCS threshold')
ax.axvspan(0.15, 0.25, alpha=0.1, color='yellow')
ax.set_xlabel('tau')
ax.set_ylabel('M_max')
ax.set_title('Extrapolated M_inf vs tau')
ax.legend(fontsize=7)

fig.suptitle(f'N-31Cb: BCS Convergence | Gate: {gate_verdict}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's31Cb_bcs_convergence.png'), dpi=150, bbox_inches='tight')
print(f"Saved s31Cb_bcs_convergence.png")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.2f}s")
