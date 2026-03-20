#!/usr/bin/env python3
"""
Session 21c P0-1: V_IR(tau) for p+q <= 2 — THE DECISIVE TEST

Computes the low-mode Casimir energy V_IR(tau) = E_bos(tau) - E_ferm(tau)
using eigenvalues with p+q <= 2, as a function of the Jensen deformation parameter tau.

The constant-ratio trap locks the full-spectrum F/B ratio at 0.55.
This computation tests whether the LOWEST modes escape that trap.

Data sources:
  - s19a_sweep_data.npz: Dirac (fermionic) eigenvalues at 21 tau values, with (p,q) sector labels
  - kk1_bosonic_spectrum.npz: Bosonic eigenvalues at 4 tau values (0.0, 0.15, 0.30, 0.50)

Constraint Gates:
  DECISIVE: minimum at tau in [0.15, 0.35] with depth > 20%
  COMPELLING: minimum at tau in [0.15, 0.35] with depth > 5%
  INTERESTING: any interior extremum
  CLOSED: monotonic for all N
  STRUCTURAL CLOSURE: monotonic AND low-mode F/B = 0.55

Output: s21c_V_IR.npz, s21c_V_IR.png
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# 1. LOAD DATA
# ============================================================

data_dir = os.path.dirname(os.path.abspath(__file__))

# Dirac (fermionic) sweep data
dirac = np.load(os.path.join(data_dir, 's19a_sweep_data.npz'), allow_pickle=True)
tau_dirac = dirac['tau_values']
n_tau_dirac = len(tau_dirac)
print(f"Dirac data: {n_tau_dirac} tau values from {tau_dirac[0]} to {tau_dirac[-1]}")

# Bosonic spectrum
bos = np.load(os.path.join(data_dir, 'kk1_bosonic_spectrum.npz'), allow_pickle=True)
bos_tau_keys = sorted(bos.keys())  # 's_0.0000', 's_0.1500', etc.
bos_tau_vals = np.array([float(k.split('_')[1]) for k in bos_tau_keys])
print(f"Bosonic data: {len(bos_tau_vals)} tau values: {bos_tau_vals}")

# ============================================================
# 2. IDENTIFY BOSONIC p+q <= 2 MODES
# ============================================================
# At tau=0, scalar eigenvalue = C_2(p,q)/3 where C_2 = (p^2+q^2+pq+3p+3q)/3
# We identify sectors by matching eigenvalues at tau=0 to known analytic values.
# For p+q <= 2 (excluding trivial (0,0)):
#   (1,0),(0,1): lambda = 4/9 = 0.4444, dim = 3 each
#   (1,1):       lambda = 1.0,          dim = 8
#   (2,0),(0,2): lambda = 10/9 = 1.1111, dim = 6 each

# Sector identification threshold
tol = 1e-4

# Analytic scalar eigenvalues for p+q <= 2 on round SU(3)
scalar_sectors_pq2 = {
    # C_2/3 value: (sector_name, total_multiplicity)
    0.0: ('(0,0)', 1),
    4/9: ('(1,0)+(0,1)', 6),
    1.0: ('(1,1)', 8),
    10/9: ('(2,0)+(0,2)', 12),
}

# Eigenvalue cutoff for p+q <= 2 bosonic modes at tau=0
# The highest scalar eigenvalue at p+q=2 is 10/9 ~ 1.111
# Vector eigenvalues may be different, but let's identify what we have
bos0 = bos['s_0.0000']
eigs0 = bos0['eigenvalue']
types0 = bos0['type']
mults0 = bos0['multiplicity']

print("\n--- Bosonic eigenvalue identification at tau=0 ---")
# For scalar (type=0), check against analytic
scalar_mask = types0 == 0
scalar_eigs = eigs0[scalar_mask]
scalar_mults = mults0[scalar_mask]

unique_scalar = np.unique(np.round(scalar_eigs, 6))
print(f"Unique scalar eigenvalues (type=0): {unique_scalar[:10]}")

# For vector (type=1)
vec_mask = types0 == 1
vec_eigs = eigs0[vec_mask]
vec_mults = mults0[vec_mask]
unique_vec = np.unique(np.round(vec_eigs, 6))
print(f"Unique vector eigenvalues (type=1): {unique_vec[:10]}")

# Strategy: since we cannot precisely identify (p,q) for bosonic modes at tau>0,
# use the LOWEST N eigenvalues from the sorted bosonic spectrum.
# This is physically motivated: the lowest bosonic eigenvalues at any tau
# correspond to low (p,q) sectors, since the Casimir C_2 increases with p+q.

# ============================================================
# 3. COMPUTE V_IR AT OVERLAPPING TAU VALUES
# ============================================================
# Overlapping tau values between Dirac and bosonic data
# Dirac: 0.0, 0.1, 0.2, ..., 2.0
# Bosonic: 0.0, 0.15, 0.30, 0.50
# Only tau=0.0, 0.30, 0.50 overlap (approximately: 0.15 is between Dirac's 0.1 and 0.2)

# For V_IR, we need BOTH bosonic and fermionic at the same tau.
# The bosonic data gives us tau = 0.0, 0.15, 0.30, 0.50
# Dirac data has tau = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, ...
# Match: 0.0 <-> 0.0, 0.15 <-> interpolate(0.1, 0.2), 0.30 <-> 0.3, 0.50 <-> 0.5

# For clean computation: use the 4 bosonic tau values
# For 0.15: interpolate Dirac between tau=0.1 and tau=0.2

def get_fermionic_eigs_at_tau(tau_target, dirac_data, tau_vals, pq_max=2):
    """Extract sorted fermionic eigenvalues with p+q <= pq_max at given tau."""
    # Find closest tau index
    idx = np.argmin(np.abs(tau_vals - tau_target))
    if np.abs(tau_vals[idx] - tau_target) < 1e-6:
        # Exact match
        eigs = dirac_data[f'eigenvalues_{idx}']
        p_arr = dirac_data[f'sector_p_{idx}']
        q_arr = dirac_data[f'sector_q_{idx}']
        mask = (p_arr + q_arr) <= pq_max
        return np.sort(np.abs(eigs[mask]))  # abs for Dirac eigenvalues
    else:
        # Linear interpolation between two nearest tau values
        if tau_target < tau_vals[idx]:
            i1, i2 = idx - 1, idx
        else:
            i1, i2 = idx, idx + 1
        t1, t2 = tau_vals[i1], tau_vals[i2]
        alpha = (tau_target - t1) / (t2 - t1)

        eigs1 = dirac_data[f'eigenvalues_{i1}']
        p1 = dirac_data[f'sector_p_{i1}']
        q1 = dirac_data[f'sector_q_{i1}']
        mask1 = (p1 + q1) <= pq_max

        eigs2 = dirac_data[f'eigenvalues_{i2}']
        p2 = dirac_data[f'sector_p_{i2}']
        q2 = dirac_data[f'sector_q_{i2}']
        mask2 = (p2 + q2) <= pq_max

        # Interpolate (same number of eigenvalues at each tau since same sectors)
        sorted1 = np.sort(np.abs(eigs1[mask1]))
        sorted2 = np.sort(np.abs(eigs2[mask2]))
        return (1 - alpha) * sorted1 + alpha * sorted2


def get_bosonic_eigs_at_tau(tau_target, bos_data, bos_keys, bos_taus):
    """Extract sorted bosonic eigenvalues at given tau."""
    idx = np.argmin(np.abs(bos_taus - tau_target))
    key = bos_keys[idx]
    arr = bos_data[key]
    eigs = arr['eigenvalue']
    # Sort and return (exclude zero mode)
    sorted_eigs = np.sort(eigs[eigs > 1e-10])
    return sorted_eigs


# N-mode cut values
N_values = [10, 20, 50, 100, 150, 200]

# Schwinger cutoff values
Lambda_values = [1, 2, 5, 10, 20]

# Tau values for computation (bosonic data availability)
tau_compute = bos_tau_vals.copy()
print(f"\nComputing V_IR at tau = {tau_compute}")

# ============================================================
# 3a. ALSO COMPUTE FERMIONIC-ONLY V_IR AT ALL 21 DIRAC TAU VALUES
# ============================================================
# Even though bosonic data is limited to 4 tau values,
# we can compute the fermionic contribution alone at all 21 tau values
# to understand its shape. This is informative for the Constraint Gate.

print("\n--- Computing fermionic energy E_ferm(tau) for p+q <= 2 at all 21 tau ---")
ferm_energy_full = {}
for N in N_values:
    ferm_energy_full[N] = np.zeros(n_tau_dirac)
    for i, tau in enumerate(tau_dirac):
        feigs = get_fermionic_eigs_at_tau(tau, dirac, tau_dirac, pq_max=2)
        n_use = min(N, len(feigs))
        ferm_energy_full[N][i] = 0.5 * np.sum(np.sqrt(feigs[:n_use]))

print("Fermionic energy at N=50:")
for i, tau in enumerate(tau_dirac):
    print(f"  tau={tau:.1f}: E_ferm={ferm_energy_full[50][i]:.4f}")

# ============================================================
# 4. COMPUTE V_IR(tau) AT 4 BOSONIC TAU VALUES
# ============================================================
print("\n--- Computing V_IR(tau) = E_bos - E_ferm ---")

results = {}
for N in N_values:
    V_IR = np.zeros(len(tau_compute))
    E_bos_arr = np.zeros(len(tau_compute))
    E_ferm_arr = np.zeros(len(tau_compute))
    FB_ratio_arr = np.zeros(len(tau_compute))

    for j, tau in enumerate(tau_compute):
        feigs = get_fermionic_eigs_at_tau(tau, dirac, tau_dirac, pq_max=2)
        beigs = get_bosonic_eigs_at_tau(tau, bos, bos_tau_keys, bos_tau_vals)

        n_ferm = min(N, len(feigs))
        n_bos = min(N, len(beigs))

        E_ferm = 0.5 * np.sum(np.sqrt(feigs[:n_ferm]))
        E_bos = 0.5 * np.sum(np.sqrt(beigs[:n_bos]))

        V_IR[j] = E_bos - E_ferm
        E_bos_arr[j] = E_bos
        E_ferm_arr[j] = E_ferm
        FB_ratio_arr[j] = E_ferm / E_bos if E_bos > 0 else np.nan

        print(f"  N={N:3d}, tau={tau:.2f}: E_bos={E_bos:.4f}, E_ferm={E_ferm:.4f}, "
              f"V_IR={V_IR[j]:.4f}, F/B={FB_ratio_arr[j]:.4f}")

    results[N] = {
        'V_IR': V_IR,
        'E_bos': E_bos_arr,
        'E_ferm': E_ferm_arr,
        'FB_ratio': FB_ratio_arr,
    }

# ============================================================
# 5. SCHWINGER-REGULATED COMPUTATION
# ============================================================
print("\n--- Computing Schwinger-regulated V_IR ---")

schwinger_results = {}
for Lambda in Lambda_values:
    V_IR_schwinger = np.zeros(len(tau_compute))

    for j, tau in enumerate(tau_compute):
        feigs = get_fermionic_eigs_at_tau(tau, dirac, tau_dirac, pq_max=2)
        beigs = get_bosonic_eigs_at_tau(tau, bos, bos_tau_keys, bos_tau_vals)

        # Schwinger: sum sqrt(lambda) * exp(-lambda/Lambda^2)
        E_ferm_S = 0.5 * np.sum(np.sqrt(feigs) * np.exp(-feigs / Lambda**2))
        E_bos_S = 0.5 * np.sum(np.sqrt(beigs) * np.exp(-beigs / Lambda**2))

        V_IR_schwinger[j] = E_bos_S - E_ferm_S

        print(f"  Lambda={Lambda:2d}, tau={tau:.2f}: V_IR_S={V_IR_schwinger[j]:.6f}")

    schwinger_results[Lambda] = V_IR_schwinger

# ============================================================
# 6. FERMIONIC-ONLY ANALYSIS AT ALL 21 TAU VALUES
# ============================================================
# Also compute Schwinger-regulated fermionic energy at all tau values
print("\n--- Schwinger-regulated fermionic energy at all 21 tau ---")
schwinger_ferm_full = {}
for Lambda in Lambda_values:
    schwinger_ferm_full[Lambda] = np.zeros(n_tau_dirac)
    for i, tau in enumerate(tau_dirac):
        feigs = get_fermionic_eigs_at_tau(tau, dirac, tau_dirac, pq_max=2)
        schwinger_ferm_full[Lambda][i] = 0.5 * np.sum(np.sqrt(feigs) * np.exp(-feigs / Lambda**2))

# ============================================================
# 7. Constraint Gate ANALYSIS
# ============================================================
print("\n" + "="*60)
print("Constraint Gate ANALYSIS")
print("="*60)

has_minimum = False
min_tau = None
min_depth = None
kill_verdict = None

for N in N_values:
    V = results[N]['V_IR']
    # Check monotonicity
    diffs = np.diff(V)
    is_monotonic = np.all(diffs >= 0) or np.all(diffs <= 0)

    if not is_monotonic:
        # Find minimum
        min_idx = np.argmin(V)
        if 0 < min_idx < len(V) - 1:  # Interior minimum
            has_minimum = True
            min_tau_val = tau_compute[min_idx]
            # Depth = max - min relative to endpoints
            depth = (max(V[0], V[-1]) - V[min_idx]) / abs(max(V[0], V[-1])) * 100
            print(f"N={N:3d}: INTERIOR MINIMUM at tau={min_tau_val:.2f}, depth={depth:.1f}%")

            if 0.15 <= min_tau_val <= 0.35:
                if depth > 20:
                    print(f"  --> DECISIVE: minimum in [0.15, 0.35] with depth > 20%")
                elif depth > 5:
                    print(f"  --> COMPELLING: minimum in [0.15, 0.35] with depth > 5%")
                else:
                    print(f"  --> INTERESTING: minimum in [0.15, 0.35] but shallow")
            else:
                print(f"  --> INTERESTING: minimum exists but outside [0.15, 0.35]")
        else:
            print(f"N={N:3d}: Non-monotonic but no interior minimum (boundary)")
    else:
        direction = "INCREASING" if diffs[0] > 0 else "DECREASING"
        FB = results[N]['FB_ratio']
        FB_var = (FB.max() - FB.min()) / FB.mean() * 100
        print(f"N={N:3d}: MONOTONIC {direction}. F/B range=[{FB.min():.4f}, {FB.max():.4f}], var={FB_var:.1f}%")

        if abs(FB.mean() - 0.55) < 0.05:
            print(f"  --> WARNING: F/B near 0.55 (trap extends to IR)")

# Schwinger analysis
print("\nSchwinger-regulated V_IR:")
for Lambda in Lambda_values:
    V = schwinger_results[Lambda]
    diffs = np.diff(V)
    is_monotonic = np.all(diffs >= 0) or np.all(diffs <= 0)
    if not is_monotonic:
        min_idx = np.argmin(V)
        if 0 < min_idx < len(V) - 1:
            depth = (max(V[0], V[-1]) - V[min_idx]) / abs(max(V[0], V[-1])) * 100
            print(f"Lambda={Lambda:2d}: INTERIOR MINIMUM at tau={tau_compute[min_idx]:.2f}, depth={depth:.1f}%")
        else:
            print(f"Lambda={Lambda:2d}: Non-monotonic, boundary extremum")
    else:
        direction = "INCREASING" if diffs[0] > 0 else "DECREASING"
        print(f"Lambda={Lambda:2d}: MONOTONIC {direction}. V_IR range=[{V.min():.6f}, {V.max():.6f}]")

# Overall verdict
print("\n" + "="*60)
any_nonmono = False
for N in N_values:
    V = results[N]['V_IR']
    diffs = np.diff(V)
    if not (np.all(diffs >= 0) or np.all(diffs <= 0)):
        any_nonmono = True

for Lambda in Lambda_values:
    V = schwinger_results[Lambda]
    diffs = np.diff(V)
    if not (np.all(diffs >= 0) or np.all(diffs <= 0)):
        any_nonmono = True

if any_nonmono:
    print("VERDICT: NON-MONOTONIC V_IR DETECTED")
else:
    # Check if F/B ~ 0.55 (structural closure)
    FB_at_N50 = results[50]['FB_ratio']
    if abs(FB_at_N50.mean() - 0.55) < 0.1:
        print("VERDICT: STRUCTURAL CLOSURE — monotonic AND F/B near 0.55")
    else:
        print("VERDICT: CLOSED — monotonic for all N and Lambda")
print("="*60)

# ============================================================
# 8. SAVE DATA
# ============================================================
save_dict = {
    'tau_compute': tau_compute,
    'tau_dirac_full': tau_dirac,
    'N_values': np.array(N_values),
    'Lambda_values': np.array(Lambda_values),
}

for N in N_values:
    for key, val in results[N].items():
        save_dict[f'N{N}_{key}'] = val

for Lambda in Lambda_values:
    save_dict[f'schwinger_Lambda{Lambda}'] = schwinger_results[Lambda]

for N in N_values:
    save_dict[f'ferm_energy_full_N{N}'] = ferm_energy_full[N]

for Lambda in Lambda_values:
    save_dict[f'schwinger_ferm_full_Lambda{Lambda}'] = schwinger_ferm_full[Lambda]

np.savez(os.path.join(data_dir, 's21c_V_IR.npz'), **save_dict)
print(f"\nData saved to {os.path.join(data_dir, 's21c_V_IR.npz')}")

# ============================================================
# 9. PLOT
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('Session 21c P0-1: V_IR(tau) for p+q <= 2 — THE DECISIVE TEST', fontsize=14, fontweight='bold')

# Panel 1: V_IR(tau) for different N
ax = axes[0, 0]
for N in N_values:
    ax.plot(tau_compute, results[N]['V_IR'], 'o-', label=f'N={N}', markersize=6)
ax.set_xlabel('tau')
ax.set_ylabel('V_IR = E_bos - E_ferm')
ax.set_title('V_IR(tau) — Hard Cutoff')
ax.legend(fontsize=8)
ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
ax.grid(True, alpha=0.3)

# Panel 2: F/B ratio for different N
ax = axes[0, 1]
for N in N_values:
    ax.plot(tau_compute, results[N]['FB_ratio'], 'o-', label=f'N={N}', markersize=6)
ax.axhline(y=0.55, color='r', linestyle='--', label='Trap value 0.55', alpha=0.7)
ax.axhline(y=1.0, color='k', linestyle=':', label='F/B = 1', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('F/B ratio')
ax.set_title('Low-Mode F/B Ratio')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Schwinger-regulated V_IR
ax = axes[0, 2]
for Lambda in Lambda_values:
    ax.plot(tau_compute, schwinger_results[Lambda], 'o-', label=f'Lambda={Lambda}', markersize=6)
ax.set_xlabel('tau')
ax.set_ylabel('V_IR (Schwinger)')
ax.set_title('Schwinger-Regulated V_IR')
ax.legend(fontsize=8)
ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
ax.grid(True, alpha=0.3)

# Panel 4: E_bos and E_ferm separately for N=50
ax = axes[1, 0]
N = 50
ax.plot(tau_compute, results[N]['E_bos'], 'bo-', label='E_bos', markersize=6)
ax.plot(tau_compute, results[N]['E_ferm'], 'rs-', label='E_ferm', markersize=6)
ax.set_xlabel('tau')
ax.set_ylabel('Energy')
ax.set_title(f'E_bos and E_ferm (N={N}, p+q<=2)')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 5: Fermionic energy at all 21 tau values (full resolution)
ax = axes[1, 1]
for N in [20, 50, 100, 200]:
    ax.plot(tau_dirac, ferm_energy_full[N], '-', label=f'N={N}')
ax.set_xlabel('tau')
ax.set_ylabel('E_ferm (p+q <= 2)')
ax.set_title('Fermionic Energy — Full Tau Resolution')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 6: Schwinger-regulated fermionic energy at all 21 tau values
ax = axes[1, 2]
for Lambda in Lambda_values:
    normalized = schwinger_ferm_full[Lambda] / schwinger_ferm_full[Lambda][0] if schwinger_ferm_full[Lambda][0] != 0 else schwinger_ferm_full[Lambda]
    ax.plot(tau_dirac, normalized, '-', label=f'Lambda={Lambda}')
ax.set_xlabel('tau')
ax.set_ylabel('E_ferm / E_ferm(tau=0)')
ax.set_title('Schwinger Ferm Energy — Normalized')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's21c_V_IR.png'), dpi=150, bbox_inches='tight')
print(f"Plot saved to {os.path.join(data_dir, 's21c_V_IR.png')}")
plt.close()

print("\n=== V_IR COMPUTATION COMPLETE ===")
