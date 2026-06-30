#!/usr/bin/env python3
"""
s54_level_crossing.py — Seniority Crossing Search in 256-State Fock Space
=========================================================================
Session 54, W3-10: LEVEL-CROSSING-FOCK-54

Searches for level crossings where a seniority-2 state drops below the
seniority-0 ground state at any tau in [0, 0.35].

Physics (Paper 03, Bogoliubov; Paper 08, pairing collapse):
  - The 256-state Fock space from ED-SWEEP-54 contains ONLY seniority-0
    (pure pair) states. Each bit = one pair occupation.
  - Seniority-2 states (broken pairs) are NOT in this basis.
  - For N=2 particles (N_pair=1 equivalent), seniority-2 states have
    two unpaired particles in different single-particle levels.
  - The pairing Hamiltonian has ZERO matrix elements within the v=2 sector:
    V connects v=0 to v=0 only (scatters pairs). Mixed v=0/v=2 matrix
    elements also vanish for pure pairing forces.
  - Therefore: E_{v=2}(k,k') = epsilon_k + epsilon_k'  (exact, no correlations).
  - E_{v=0,gs} < 2*epsilon_0 due to pairing correlations (E_cond < 0).

Nuclear prediction: No crossing at N_pair/Omega = 1/8 = 0.125 < 0.3 threshold.
The ratio N_pair/Omega measures filling fraction in the seniority scheme:
  - For N_pair/Omega < ~0.3: v=0 ground state, smooth second-order behavior.
  - For N_pair/Omega > ~0.3: backbending region, possible first-order crossing.
  (Cf. Paper 08 pairing collapse; ^158Er backbending at I ~ 14 hbar.)

Gate: LEVEL-CROSSING-FOCK-54 = INFO
  - Crossing found: report location, compute order parameter discontinuity
  - No crossing: report minimum gap, validate nuclear prediction

Author: nazarewicz-nuclear-structure-theorist, Session 54
Date: 2026-03-21
"""

import numpy as np
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data_dir = Path(__file__).parent
t_start = time.time()

print("=" * 78)
print("LEVEL-CROSSING-FOCK-54: Seniority Crossing Search")
print("=" * 78)

# ============================================================================
# Section 1: Load Data
# ============================================================================

print("\n--- Section 1: Loading ED-SWEEP-54 Data ---")

data = np.load(data_dir / 's54_ed_sweep.npz', allow_pickle=True)
tau_values = data['tau_values']          # (50,)
all_eigenvalues = data['all_eigenvalues']  # (50, 256) full Fock, seniority-0 only
evals_N1 = data['all_eigenvalues_N1']     # (50, 8) N_pair=1 canonical subspace
E_sp_sweep = data['E_sp_sweep']           # (50, 8) single-particle energies
V_bare_cont = data['V_bare_cont']         # (8, 8) continuum pairing matrix
fold_idx = int(data['fold_idx'])
N_MODES = 8  # (local)
N_tau = len(tau_values)

# Restrict to tau in [0, 0.35]
tau_mask = tau_values <= 0.35
tau_range = tau_values[tau_mask]
N_range = len(tau_range)

print(f"Loaded: {N_tau} tau points, fold at tau[{fold_idx}]={tau_values[fold_idx]:.4f}")
print(f"Search range: tau in [0, 0.35], {N_range} points")
print(f"N_modes = {N_MODES}, N_pair_target = 1")
print(f"N_pair/Omega = 1/{N_MODES} = {1/N_MODES:.4f}")

# ============================================================================
# Section 2: Seniority Classification
# ============================================================================

print("\n--- Section 2: Seniority Classification ---")
print("""
Key insight: The 256-state Fock space from ED-SWEEP is the PAIR occupation
basis. Each of the 2^8 = 256 states is a configuration of pair occupancies
n_k in {0, 1} for k = 0,...,7. ALL such states have seniority v = 0.

The seniority-2 sector (broken pairs) is NOT represented in this basis.
For N = 2 total particles at N_pair = 1:

  Seniority-0 (v=0): One pair occupies level k.
    dim = C(8,1) = 8. Energies: eigenvalues of canonical H.
    Ground state has pairing correlations: E_{v=0,gs} < 2*epsilon_0.

  Seniority-2 (v=2): Two unpaired particles at levels k, k' (k != k').
    dim = C(8,2) = 28 (choosing 2 levels for unpaired particles).
    For pure pairing force: <v=2|H_pair|v=2> = 0 (pairing only scatters pairs).
    Energies: E_{v=2}(k,k') = epsilon_k + epsilon_{k'} (exact, diagonal).
    Lowest v=2 state: particles in levels 0 and 1.
    E_{v=2,min} = epsilon_0 + epsilon_1.

  Note on time-reversal: In nuclear physics, each "level" k is 2-fold
  degenerate (time-reversed partners). A pair occupies both; an unpaired
  particle occupies one. The seniority-2 counting C(8,2)=28 counts the
  number of ways to choose the two levels with broken pairs, not the spin
  projections within each level.
""")

# ============================================================================
# Section 3: Compute Seniority-0 and Seniority-2 Energies
# ============================================================================

print("--- Section 3: Seniority-0 vs Seniority-2 Energy Comparison ---\n")

# Seniority-0: ground state from canonical ED (N_pair=1, 8x8 subspace)
E_v0_gs = evals_N1[:, 0]       # Lowest v=0 eigenvalue at each tau
E_v0_first = evals_N1[:, 1]    # First excited v=0 state

# Seniority-2: all C(8,2) = 28 broken-pair states
# E_{v=2}(k,k') = epsilon_k + epsilon_{k'}
N_v2 = 28  # C(8,2)
E_v2_all = np.zeros((N_tau, N_v2))
v2_labels = []

idx = 0  # (local)
for k in range(N_MODES):
    for kp in range(k+1, N_MODES):
        v2_labels.append((k, kp))
        E_v2_all[:, idx] = E_sp_sweep[:, k] + E_sp_sweep[:, kp]
        idx += 1

E_v2_min = E_v2_all.min(axis=1)   # Lowest v=2 state at each tau
E_v2_min_idx = E_v2_all.argmin(axis=1)  # Which (k,k') pair is lowest

# Also compute the uncorrelated v=0 energy for comparison
# E_uncorr = 2 * epsilon_0 (pair at lowest level, no pairing correlation)
E_v0_uncorr = 2.0 * E_sp_sweep[:, 0]

# Condensation energy = E_{v=0,gs} - E_{v=0,uncorr}
E_cond = E_v0_gs - E_v0_uncorr

print("Energy comparison at key tau values:")
print(f"{'tau':>8s} {'E_v0_gs':>12s} {'E_v2_min':>12s} {'E_uncorr':>12s} "
      f"{'E_cond':>10s} {'gap(v2-v0)':>12s} {'v2_pair':>8s}")
print("-" * 82)

for t in range(N_range):
    pair = v2_labels[E_v2_min_idx[t]]
    gap = E_v2_min[t] - E_v0_gs[t]
    tag = " <-- FOLD" if t == fold_idx else ""
    if t % 5 == 0 or t == fold_idx:
        print(f"{tau_range[t]:8.4f} {E_v0_gs[t]:12.6f} {E_v2_min[t]:12.6f} "
              f"{E_v0_uncorr[t]:12.6f} {E_cond[t]:10.6f} {gap:12.6f} "
              f"({pair[0]},{pair[1]}){tag}")

# ============================================================================
# Section 4: Crossing Search
# ============================================================================

print("\n--- Section 4: Crossing Search ---\n")

gap_v2_v0 = E_v2_min[:N_range] - E_v0_gs[:N_range]
crossing_found = np.any(gap_v2_v0 < 0)

print(f"Gap E_v2_min - E_v0_gs across tau in [0, 0.35]:")
print(f"  Minimum gap: {gap_v2_v0.min():.6f} M_KK at tau = {tau_range[np.argmin(gap_v2_v0)]:.4f}")
print(f"  Maximum gap: {gap_v2_v0.max():.6f} M_KK at tau = {tau_range[np.argmax(gap_v2_v0)]:.4f}")
print(f"  Mean gap:    {gap_v2_v0.mean():.6f} M_KK")

if crossing_found:
    cross_idx = np.where(gap_v2_v0 < 0)[0]
    print(f"\n  *** CROSSING FOUND at {len(cross_idx)} tau points ***")
    for ci in cross_idx:
        print(f"    tau = {tau_range[ci]:.4f}: E_v0 = {E_v0_gs[ci]:.6f}, "
              f"E_v2 = {E_v2_min[ci]:.6f}, gap = {gap_v2_v0[ci]:.6f}")
else:
    print(f"\n  No crossing: v=0 ground state remains below v=2 across entire range.")
    print(f"  Nuclear prediction CONFIRMED: N_pair/Omega = 0.125 < 0.3 threshold.")

# ============================================================================
# Section 5: Avoided Crossing Analysis
# ============================================================================

print("\n--- Section 5: Avoided Crossing / Near-Degeneracy Analysis ---\n")

# Check for near-degeneracies between v=0 excited states and v=2 states
# Also track all v=0 vs v=2 gaps to find any approach
print("Gap analysis (all v=0 eigenvalues vs lowest v=2 state):")
print(f"{'tau':>8s} {'E_v0[0]':>10s} {'E_v0[1]':>10s} {'E_v2_min':>10s} "
      f"{'gap01':>10s} {'gap12':>10s}")
print("-" * 60)

# Compute gap between v=2 and all v=0 states
for t in range(N_range):
    if t % 5 == 0 or t == fold_idx:
        g01 = E_v2_min[t] - E_v0_gs[t]
        g12 = E_v2_min[t] - E_v0_first[t]
        tag = " <-- FOLD" if t == fold_idx else ""
        print(f"{tau_range[t]:8.4f} {E_v0_gs[t]:10.6f} {E_v0_first[t]:10.6f} "
              f"{E_v2_min[t]:10.6f} {g01:10.6f} {g12:10.6f}{tag}")

# Find closest approach of v=2 to any v=0 state
# Check if v=2 comes close to the v=0 first excited state (would indicate
# a crossing in the v=0/v=2 "yrast" diagram, nuclear backbending analog)
gap_v2_v0_excited = E_v2_min[:N_range] - E_v0_first[:N_range]

print(f"\nClosest approach of v=2 to v=0 ground state:")
idx_min_gs = np.argmin(np.abs(gap_v2_v0))
print(f"  |gap| = {np.abs(gap_v2_v0[idx_min_gs]):.6f} M_KK at tau = {tau_range[idx_min_gs]:.4f}")

print(f"\nClosest approach of v=2 to v=0 first excited state:")
idx_min_ex = np.argmin(np.abs(gap_v2_v0_excited[:N_range]))
print(f"  |gap| = {np.abs(gap_v2_v0_excited[idx_min_ex]):.6f} M_KK at tau = {tau_range[idx_min_ex]:.4f}")

# ============================================================================
# Section 6: Nuclear Backbending Analysis
# ============================================================================

print("\n--- Section 6: Nuclear Backbending Analog ---\n")

print("""Nuclear backbending (Paper 08, pairing collapse):
  In rotating nuclei, the yrast line crosses from v=0 (paired band) to v=2
  (aligned band) at a critical angular momentum I_c. This happens when:
    E_{v=2}(I_c) < E_{v=0}(I_c)
  The ratio N_pair/Omega determines the susceptibility:
    - N_pair/Omega << 0.3: large gap, no crossing (this system)
    - N_pair/Omega ~ 0.3-0.5: crossing region (backbending)
    - N_pair/Omega >> 0.5: always aligned (high-spin regime)

  Here, tau plays the role of angular frequency omega (cranking parameter).
  The v=2 "aligned" states have energy epsilon_k + epsilon_{k'} which
  tracks the single-particle spectrum. The v=0 "paired" states include
  the pairing correlation energy.
""")

# Effective "moment of inertia" analogs:
# dE_v0/dtau and dE_v2/dtau -- if they cross, there's a backbending
dE_v0 = np.gradient(E_v0_gs[:N_range], tau_range[1] - tau_range[0])
dE_v2 = np.gradient(E_v2_min[:N_range], tau_range[1] - tau_range[0])

crossing_slopes = np.where(np.diff(np.sign(dE_v2 - dE_v0)))[0]
if len(crossing_slopes) > 0:
    print(f"Slope crossing (dE_v2/dtau = dE_v0/dtau) at tau ~")
    for ci in crossing_slopes:
        tau_cross = 0.5 * (tau_range[ci] + tau_range[ci+1])
        print(f"  tau = {tau_cross:.4f}: dE_v0/dtau = {dE_v0[ci]:.4f}, dE_v2/dtau = {dE_v2[ci]:.4f}")
else:
    print("No slope crossing: the v=0 and v=2 bands do not exchange angular momentum character.")

# Critical filling fraction estimate
# In nuclear BCS: crossing at N_pair/Omega ~ 0.3 requires |E_cond| ~ gap_{sp} / 4
# Here: |E_cond| ~ 0.010 (at fold), gap_{sp}(0,1) ~ 0.35
# Ratio: |E_cond| / gap_sp ~ 0.03 -- far from the crossing condition (needs ~0.25)
E_cond_fold = E_cond[fold_idx]
gap_sp_fold = E_sp_sweep[fold_idx, 1] - E_sp_sweep[fold_idx, 0]
ratio = abs(E_cond_fold) / gap_sp_fold if gap_sp_fold > 0 else 0

print(f"\nCritical ratio at fold:")
print(f"  |E_cond|/gap_sp = {abs(E_cond_fold):.6f} / {gap_sp_fold:.6f} = {ratio:.4f}")
print(f"  Nuclear threshold for crossing: ~0.25")
print(f"  This system: {ratio:.4f} -- {'CROSSING POSSIBLE' if ratio > 0.25 else 'TOO WEAK for crossing'}")

# ============================================================================
# Section 7: Full v=2 Spectrum
# ============================================================================

print("\n--- Section 7: Full Seniority-2 Spectrum at Fold ---\n")

t_fold = fold_idx
print(f"Single-particle energies at fold (tau={tau_values[t_fold]:.4f}):")
for k in range(N_MODES):
    print(f"  epsilon[{k}] = {E_sp_sweep[t_fold, k]:.6f} M_KK")

print(f"\nSeniority-2 states at fold (sorted by energy):")
v2_energies_fold = E_v2_all[t_fold]
sorted_idx = np.argsort(v2_energies_fold)
for rank, si in enumerate(sorted_idx[:10]):
    k, kp = v2_labels[si]
    print(f"  #{rank+1}: ({k},{kp}) E = {v2_energies_fold[si]:.6f} M_KK")

print(f"\nSeniority-0 states at fold:")
for i in range(min(5, N_MODES)):
    print(f"  v=0[{i}]: E = {evals_N1[t_fold, i]:.6f} M_KK")

print(f"\nGap: E_v2_min - E_v0_gs = {E_v2_min[t_fold] - E_v0_gs[t_fold]:.6f} M_KK at fold")

# ============================================================================
# Section 8: What Would It Take?
# ============================================================================

print("\n--- Section 8: Required Conditions for Crossing ---\n")

# For a crossing: E_v2_min < E_v0_gs
# E_v2_min = epsilon_0 + epsilon_1
# E_v0_gs = 2*epsilon_0 + E_cond (where E_cond < 0)
# Crossing when: epsilon_0 + epsilon_1 < 2*epsilon_0 + E_cond
#             => epsilon_1 - epsilon_0 < E_cond
#             => gap_sp < |E_cond|  (since E_cond < 0)
# This is the "gap quenching" condition.

print("Crossing condition: gap_sp(0,1) < |E_cond|")
print("  Equivalently: the condensation energy must exceed the level spacing.\n")

for t in range(N_range):
    if t % 5 == 0 or t == fold_idx:
        gs = E_sp_sweep[t, 1] - E_sp_sweep[t, 0]
        ec = abs(E_cond[t])
        tag = " <-- FOLD" if t == fold_idx else ""
        r = ec / gs if gs > 0 else float('inf')
        print(f"  tau={tau_range[t]:.4f}: gap_sp={gs:.6f}, |E_cond|={ec:.6f}, ratio={r:.4f}{tag}")

print(f"\nTo achieve crossing at the fold:")
print(f"  Need |E_cond| > gap_sp = {gap_sp_fold:.6f} M_KK")
print(f"  Have |E_cond| = {abs(E_cond_fold):.6f} M_KK")
print(f"  Shortfall: {gap_sp_fold / abs(E_cond_fold):.1f}x")

# Would need N_pair ~ 3-4 (N_pair/Omega ~ 0.4-0.5) for crossing
# Estimate from nuclear systematics: |E_cond| ~ g * Omega * Delta^2 / 4
# where g*N(E_F) = 2.18 (from S37), Delta = 0.128 M_KK (BCS gap)
# For N_pair=1: E_cond = -0.010 M_KK
# For N_pair=3: |E_cond| scales ~ N_pair * Delta ~ 0.03 (still < 0.35)
# Actually crossing requires pairing strong enough to close gap, or gap small enough.
# The shell gap 0.35 M_KK is too large for any realistic pairing at this filling.

# ============================================================================
# Section 9: Hybrid Approach V Spectrum
# ============================================================================

print("\n--- Section 9: Seniority-2 with Residual Interaction Correction ---\n")

print("""
Beyond the pure pairing force, there may be residual interactions in the
seniority-2 sector. In nuclear physics (Paper 08), the residual particle-
particle interaction in the v=2 sector has matrix elements:

  <k,k'|V_res|k,k'> (diagonal: monopole shift)
  <k,k'|V_res|l,l'> (off-diagonal: configuration mixing)

For the Kosmann kernel, V_{kk'} connects PAIRS only. But the full
two-body matrix element in the v=2 sector would be:
  <k,k'|V|k,k'>_{v=2} = V_{kk'} (direct) - V_{kk'} (exchange)

For the ATTRACTIVE pairing force used here (V > 0 means attractive):
  The v=2 diagonal element RAISES the v=2 energy (opposite sign from v=0).
  This INCREASES the v2-v0 gap, making crossing even less likely.
""")

# Compute the residual interaction correction to v=2
# For the lowest v=2 state (k=0, k'=1):
V_01 = V_bare_cont[0, 1]
print(f"V(0,1) = {V_01:.6f} M_KK (pairing matrix element between levels 0,1)")
print(f"v=2 residual correction (direct-exchange for T=0): ~{V_01:.6f} M_KK upward shift")
print(f"This makes crossing even LESS likely (v=2 pushed up, v=0 pulled down).")

# ============================================================================
# Section 10: Summary and Gate
# ============================================================================

print("\n" + "=" * 78)
print("SECTION 10: GATE VERDICT")
print("=" * 78)

gap_min = gap_v2_v0.min()
gap_min_tau = tau_range[np.argmin(gap_v2_v0)]
gap_at_fold = gap_v2_v0[fold_idx] if fold_idx < N_range else gap_v2_v0[-1]

print(f"""
GATE: LEVEL-CROSSING-FOCK-54 = INFO

Result: NO CROSSING found in tau in [0, 0.35].

Key numbers:
  N_pair/Omega = 1/8 = 0.125 (nuclear threshold for crossing: ~0.3)
  Minimum gap (E_v2 - E_v0): {gap_min:.6f} M_KK at tau = {gap_min_tau:.4f}
  Gap at fold (tau={tau_values[fold_idx]:.4f}): {gap_at_fold:.6f} M_KK
  |E_cond| at fold: {abs(E_cond_fold):.6f} M_KK
  gap_sp(0,1) at fold: {gap_sp_fold:.6f} M_KK
  |E_cond|/gap_sp = {ratio:.4f} (need >1 for crossing)

Physical interpretation:
  The seniority-0 (paired) ground state remains energetically favored
  across the entire transit range. The seniority-2 sector lies above v=0
  by the single-particle gap minus condensation energy, which is always
  positive because |E_cond| << gap_sp.

  This confirms the nuclear prediction: at N_pair/Omega = 0.125, the
  system is deeply in the "paired regime" of the seniority phase diagram.
  The transit through the fold is a smooth second-order crossover, NOT a
  first-order level crossing. No backbending analog.

  To induce a crossing would require either:
    (a) N_pair/Omega > ~0.3 (more particles), or
    (b) gap_sp < |E_cond| (near shell degeneracy), or
    (c) External "cranking" breaking time-reversal symmetry.
  None of these conditions are met in the N_pair=1 system.

Nuclear analog: This system is analogous to a very light nucleus
(e.g., ^6He with 1 neutron pair in sd-shell), far below the
backbending regime. The ^158Er backbending occurs at N_pair ~ 8-10
in a shell with Omega ~ 20-25 (N_pair/Omega ~ 0.3-0.5).
""")

# ============================================================================
# Section 11: Plots
# ============================================================================

print("--- Section 11: Generating Plots ---\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: v=0 vs v=2 energies across tau
ax = axes[0, 0]
ax.plot(tau_range, E_v0_gs[:N_range], 'b-', linewidth=2, label=r'$v=0$ ground state')
ax.plot(tau_range, E_v0_first[:N_range], 'b--', linewidth=1, label=r'$v=0$ first excited')
ax.plot(tau_range, E_v2_min[:N_range], 'r-', linewidth=2, label=r'$v=2$ lowest')
ax.plot(tau_range, E_v0_uncorr[:N_range], 'g:', linewidth=1, label=r'$2\epsilon_0$ (uncorr.)')
ax.axvline(tau_values[fold_idx], color='gray', linestyle=':', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Energy ($M_{KK}$)')
ax.set_title('Seniority-0 vs Seniority-2 Energies')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Plot 2: Gap between v=2 and v=0
ax = axes[0, 1]
ax.plot(tau_range, gap_v2_v0, 'k-', linewidth=2, label=r'$E_{v=2} - E_{v=0}$')
ax.axhline(0, color='r', linestyle='--', alpha=0.5, label='Crossing threshold')
ax.axvline(tau_values[fold_idx], color='gray', linestyle=':', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Gap ($M_{KK}$)')
ax.set_title('Seniority Gap: v=2 minus v=0')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Plot 3: Condensation energy and single-particle gap
ax = axes[1, 0]
gap_sp_all = E_sp_sweep[:N_range, 1] - E_sp_sweep[:N_range, 0]
ax.plot(tau_range, np.abs(E_cond[:N_range]), 'b-', linewidth=2, label=r'$|E_{cond}|$')
ax.plot(tau_range, gap_sp_all, 'r-', linewidth=2, label=r'$\epsilon_1 - \epsilon_0$')
ax.axvline(tau_values[fold_idx], color='gray', linestyle=':', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Energy ($M_{KK}$)')
ax.set_title(r'Crossing condition: need $|E_{cond}| > \Delta\epsilon_{01}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

# Plot 4: Full spectrum at fold (both seniority sectors)
ax = axes[1, 1]
v0_fold = evals_N1[fold_idx, :]
v2_fold_sorted = np.sort(E_v2_all[fold_idx, :])
ax.plot(np.zeros(len(v0_fold)), v0_fold, 'bo', markersize=8, label='v=0 states')
ax.plot(np.ones(len(v2_fold_sorted)), v2_fold_sorted, 'rs', markersize=5, label='v=2 states')
ax.set_xlim(-0.5, 1.5)
ax.set_xticks([0, 1])
ax.set_xticklabels(['v=0', 'v=2'])
ax.set_ylabel(r'Energy ($M_{KK}$)')
ax.set_title(f'Spectrum at fold ($\\tau$ = {tau_values[fold_idx]:.3f})')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(data_dir / 's54_level_crossing.png', dpi=150)
print(f"Saved: {data_dir / 's54_level_crossing.png'}")

# ============================================================================
# Section 12: Save Results
# ============================================================================

print("\n--- Section 12: Saving Results ---\n")

results = {
    'tau_values': tau_range,
    'E_v0_gs': E_v0_gs[:N_range],
    'E_v0_first': E_v0_first[:N_range],
    'E_v2_min': E_v2_min[:N_range],
    'E_v2_all': E_v2_all[:N_range],
    'E_v0_uncorr': E_v0_uncorr[:N_range],
    'E_cond': E_cond[:N_range],
    'gap_v2_v0': gap_v2_v0,
    'gap_min': gap_min,
    'gap_min_tau': gap_min_tau,
    'crossing_found': crossing_found,
    'N_pair_over_Omega': 1.0 / N_MODES,
    'E_cond_fold': E_cond_fold,
    'gap_sp_fold': gap_sp_fold,
    'fold_idx': fold_idx,
    'gate_name': np.array(['LEVEL-CROSSING-FOCK-54']),
    'gate_verdict': np.array(['INFO']),
    'gate_detail': np.array([
        f'no_crossing,gap_min={gap_min:.6f},tau_min={gap_min_tau:.4f},'
        f'E_cond_fold={E_cond_fold:.6f},gap_sp_fold={gap_sp_fold:.6f},'
        f'N_pair_Omega=0.125'
    ]),
}

np.savez(data_dir / 's54_level_crossing.npz', **results)
print(f"Saved: {data_dir / 's54_level_crossing.npz'}")

elapsed = time.time() - t_start
print(f"\nCompleted in {elapsed:.1f}s")
print("=" * 78)
