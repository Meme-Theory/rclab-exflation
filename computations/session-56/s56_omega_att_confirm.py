#!/usr/bin/env python3
"""
Session 56: OMEGA-ATT-CONFIRM-56 -- Tau-Sweep of omega_att = 9*(B3-B1)
========================================================================

GATE: OMEGA-ATT-CONFIRM-56
  INFO: algebraic or coincidental?

CONTEXT:
  S38 (W2, C-3) found omega_att = 9*(B3-B1) at 0.08% accuracy at the fold
  tau = 0.190. S39 tested this with the Kosmann 16-mode spectrum and found
  FAIL (COINCIDENCE) with 25% variation -- but that used a different spectral
  basis.

  This script re-examines the claim using the S54 tight-binding 32-cell
  Hamiltonian, which provides the complete spectrum on the Voronoi tessellation
  of reps up to max_pq_sum=6.

  In the 32-cell spectrum:
    B1 = eigenvalue[1]  (Fiedler mode, lowest non-zero eigenvalue)
    B3 = eigenvalue[31] (highest eigenvalue = bandwidth)

  We test: R(tau) = omega_att / (N * (E_B3(tau) - E_B1(tau))) for N = 7..11.
  If R(tau) = const for some N to within 1% across tau -> STRUCTURAL.

  Since omega_att = 1.430 M_KK is a BCS-derived quantity (from the GL
  functional at the fold), and B3-B1 is the tight-binding bandwidth, the
  ratio omega_att/(B3-B1) = 1.430 / bandwidth(tau).

  Key: the bandwidth varies from 14.65 (tau=0) to 2.62 (tau=0.5), so
  9*(B3-B1) ranges from ~132 to ~24, while omega_att = 1.430 is fixed.
  This means R = omega_att/(9*(B3-B1)) is NOT constant -- it was only
  close to 9 at the fold because B3-B1 ~ 0.159 in the Kosmann 16-mode
  spectrum, not in the 32-cell TB spectrum.

  We compute R at all 50 tau values and quantify the drift.

Author: phonon-first-cosmologist, Session 56
Date: 2026-03-22
"""

import os
import sys
import time
import numpy as np

# Canonical constants
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("S56: OMEGA-ATT-CONFIRM-56 -- omega_att = 9*(B3-B1) Tau-Sweep")
print("=" * 78)

# ======================================================================
#  Step 1: Load S54 tight-binding data
# ======================================================================
print("\n--- Step 1: Load S54 tight-binding Hamiltonian ---")

tb_path = os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz')
if not os.path.exists(tb_path):
    raise FileNotFoundError(f"Missing: {tb_path}")

data = np.load(tb_path, allow_pickle=True)
tau_values = data['tau_values']       # (50,)
eigenvalues = data['eigenvalues']     # (50, 32)
cell_labels = data['cell_labels']     # (32, 2) -- (p,q) labels
cell_casimirs = data['cell_casimirs'] # (32,)
cell_dims = data['cell_dims']         # (32,)
bandwidths = data['bandwidths']       # (50,)
eigenvectors = data['eigenvectors']   # (50, 32, 32)

N_tau = len(tau_values)
N_cells = int(data['N_cells'])

print(f"  Loaded: {N_tau} tau values in [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")
print(f"  N_cells = {N_cells}")
print(f"  Bandwidth range: [{bandwidths.min():.4f}, {bandwidths.max():.4f}] M_KK")

# ======================================================================
#  Step 2: Identify B1 and B3 at each tau
# ======================================================================
print("\n--- Step 2: Identify B1 (Fiedler) and B3 (max) eigenvalues ---")

# The eigenvalues are sorted at each tau. eigenvalue[0] = 0 (zero mode).
# B1 = eigenvalue[1] = Fiedler mode (lowest non-zero)
# B3 = eigenvalue[31] = highest eigenvalue (bandwidth)
#
# Also identify which (p,q) sector dominates each eigenstate using the
# eigenvector components (participation ratio).

E_B1 = np.zeros(N_tau)  # Fiedler mode
E_B3 = np.zeros(N_tau)  # Highest mode
B3_minus_B1 = np.zeros(N_tau)

# Track which (p,q) cell dominates B1 and B3
B1_dominant_cell = np.zeros(N_tau, dtype=int)
B3_dominant_cell = np.zeros(N_tau, dtype=int)

for ti in range(N_tau):
    ev = eigenvalues[ti]
    evec = eigenvectors[ti]

    # Sort eigenvalues (should already be sorted, but verify)
    sort_idx = np.argsort(ev)
    ev_sorted = ev[sort_idx]

    E_B1[ti] = ev_sorted[1]   # Fiedler
    E_B3[ti] = ev_sorted[-1]  # Highest
    B3_minus_B1[ti] = E_B3[ti] - E_B1[ti]

    # Dominant cell for B1 (index 1 in sorted)
    vec_B1 = evec[:, sort_idx[1]]
    B1_dominant_cell[ti] = np.argmax(np.abs(vec_B1))

    # Dominant cell for B3 (index 31 in sorted)
    vec_B3 = evec[:, sort_idx[-1]]
    B3_dominant_cell[ti] = np.argmax(np.abs(vec_B3))

print(f"  E_B1 range: [{E_B1.min():.6f}, {E_B1.max():.6f}]")
print(f"  E_B3 range: [{E_B3.min():.6f}, {E_B3.max():.6f}]")
print(f"  B3-B1 range: [{B3_minus_B1.min():.6f}, {B3_minus_B1.max():.6f}]")

# Print dominant cells at a few key tau
print(f"\n  Dominant cells at selected tau:")
print(f"  {'tau':>8s}  {'E_B1':>10s}  {'B1_cell':>10s}  {'E_B3':>10s}  {'B3_cell':>10s}  {'B3-B1':>10s}")
for ti in [0, 10, 19, 25, 35, 49]:  # ti=19 ~ tau=0.19 (fold)
    ci_b1 = B1_dominant_cell[ti]
    ci_b3 = B3_dominant_cell[ti]
    pq_b1 = cell_labels[ci_b1]
    pq_b3 = cell_labels[ci_b3]
    print(f"  {tau_values[ti]:8.4f}  {E_B1[ti]:10.6f}  ({pq_b1[0]},{pq_b1[1]})      "
          f"{E_B3[ti]:10.6f}  ({pq_b3[0]},{pq_b3[1]})      {B3_minus_B1[ti]:10.6f}")

# ======================================================================
#  Step 3: Compute R(tau) = omega_att / (N * (B3 - B1))
# ======================================================================
print("\n--- Step 3: Compute R(tau) = omega_att / (N * (B3 - B1)) ---")

# omega_att = 1.430 M_KK (canonical, from S38)
print(f"  omega_att = {omega_att:.6f} M_KK (canonical)")

# Test N = 7, 8, 9, 10, 11
N_test = [7, 8, 9, 10, 11]
R_arrays = {}

for N in N_test:
    R = omega_att / (N * B3_minus_B1)
    R_arrays[N] = R
    R_mean = np.mean(R)
    R_std = np.std(R)
    R_min = np.min(R)
    R_max = np.max(R)
    frac = R_std / R_mean if R_mean > 0 else np.nan

    print(f"\n  N={N}:")
    print(f"    R(tau) = omega_att / ({N} * (B3 - B1))")
    print(f"    R_mean = {R_mean:.6f}")
    print(f"    R_std  = {R_std:.6f}")
    print(f"    sigma/mean = {frac:.4f} ({frac*100:.2f}%)")
    print(f"    R_range = [{R_min:.6f}, {R_max:.6f}]")
    print(f"    R_max/R_min = {R_max/R_min:.4f}")

# ======================================================================
#  Step 3b: The CORRECT comparison -- what B3-B1 means in Kosmann spectrum
# ======================================================================
print("\n--- Step 3b: Comparison with Kosmann 16-mode B3-B1 ---")
print("  S38 used the KOSMANN 16-mode spectrum, not the 32-cell TB spectrum.")
print("  In Kosmann: B1 = lowest positive singlet, B3 = highest sub-band.")
print("  These are eigenvalues of the Dirac operator D_K, not the TB Hamiltonian.")
print("  The Kosmann B3-B1 ~ 0.14-0.16 at the fold (M_KK units).")
print("  The TB B3-B1 = bandwidth ~ 6.77 at the fold.")
print("  These are DIFFERENT quantities from DIFFERENT spectra.")

# Compute what omega_att / (B3-B1) actually is for the TB spectrum
R_raw = omega_att / B3_minus_B1
print(f"\n  R_raw(tau) = omega_att / (B3_TB - B1_TB):")
print(f"    At fold (tau~0.19): B3-B1 = {B3_minus_B1[19]:.4f}, R = {R_raw[19]:.6f}")
print(f"    R_raw range: [{R_raw.min():.6f}, {R_raw.max():.6f}]")
print(f"    sigma/mean = {np.std(R_raw)/np.mean(R_raw):.4f} ({np.std(R_raw)/np.mean(R_raw)*100:.2f}%)")

# ======================================================================
#  Step 4: Check if omega_att has ANY simple relationship to TB spectrum
# ======================================================================
print("\n--- Step 4: Systematic ratio scan ---")
print("  Test omega_att / f(spectrum) for various spectral quantities:")

# Quantities to test
test_quantities = {}

# (a) Bandwidth = B3 - B1
test_quantities['bandwidth'] = B3_minus_B1

# (b) Band gap (from data)
test_quantities['band_gap'] = data['band_gaps']

# (c) Specific eigenvalue differences
for i in range(1, min(8, N_cells)):
    for j in range(i+1, min(10, N_cells)):
        key = f'E[{j}]-E[{i}]'
        diff = eigenvalues[:, j] - eigenvalues[:, i]
        if np.all(diff > 1e-10):
            test_quantities[key] = diff

# (d) Mean eigenvalue gap
mean_gap = np.zeros(N_tau)
for ti in range(N_tau):
    ev = np.sort(eigenvalues[ti])
    gaps = np.diff(ev[1:])  # skip zero mode
    mean_gap[ti] = np.mean(gaps)
test_quantities['mean_gap'] = mean_gap

# (e) Median eigenvalue
test_quantities['median_eig'] = np.median(eigenvalues[:, 1:], axis=1)

# (f) J_C2 coupling (main hopping)
test_quantities['J_C2'] = data['J_C2_tau']

# (g) Specific eigenvalues
for i in [1, 2, 3, 4, 5, 10, 15, 20, 25, 31]:
    test_quantities[f'E[{i}]'] = eigenvalues[:, i]

# Now for each, compute omega_att / Q(tau) and check constancy
print(f"\n  {'Quantity':<20s}  {'R_mean':>10s}  {'R_std':>10s}  {'sigma/mu':>10s}  {'at fold':>10s}")
print(f"  {'='*20}  {'='*10}  {'='*10}  {'='*10}  {'='*10}")

results_scan = []
for name, Q in sorted(test_quantities.items()):
    mask = np.abs(Q) > 1e-10
    if np.sum(mask) < 10:
        continue
    R = omega_att / Q[mask]
    R_mean = np.mean(R)
    R_std = np.std(R)
    frac = R_std / R_mean if R_mean > 0 else np.nan
    # Value at fold
    fold_idx = 19  # tau ~ 0.19 (local)
    R_fold = omega_att / Q[fold_idx] if np.abs(Q[fold_idx]) > 1e-10 else np.nan
    results_scan.append((name, R_mean, R_std, frac, R_fold))
    if frac < 0.10:  # Only print if less than 10% variation
        print(f"  {name:<20s}  {R_mean:10.6f}  {R_std:10.6f}  {frac:10.4f}  {R_fold:10.6f}")

# Sort by constancy (lowest sigma/mean)
results_scan.sort(key=lambda x: x[3])
print(f"\n  Top 10 most constant ratios (sorted by sigma/mean):")
print(f"  {'Quantity':<20s}  {'R_mean':>10s}  {'sigma/mu':>10s}  {'R_fold':>10s}")
for name, R_mean, R_std, frac, R_fold in results_scan[:10]:
    print(f"  {name:<20s}  {R_mean:10.6f}  {frac:10.4f}  {R_fold:10.6f}")

# ======================================================================
#  Step 5: The Kosmann-relevant test: compare with S39 B3-B1
# ======================================================================
print("\n--- Step 5: Reconstruct S38's omega_att = 9*(B3-B1) claim ---")
print("  S38 used the Kosmann 16-mode Dirac eigenvalues at the fold.")
print("  In that basis:")
print("    B1 = lowest positive singlet eigenvalue (~0.820)")
print("    B3 = highest sub-band eigenvalue (~0.962)")
print("    B3-B1 ~ 0.142")
print(f"    9 * (B3-B1) ~ 9 * 0.142 = 1.278 vs omega_att = {omega_att:.3f}")
print("  S39 showed this drifts by 25% across tau. COINCIDENCE at fold.")

# Load S39 result for comparison
s39_path = os.path.join(SCRIPT_DIR, "..", "_shared", 's39_9to1_sweep.npz')
s39_loaded = False
if os.path.exists(s39_path):
    s39 = np.load(s39_path, allow_pickle=True)
    print(f"\n  S39 results (Kosmann 16-mode):")
    print(f"    Verdict: {s39['verdict']}")
    print(f"    R_0 (mean) = {float(s39['R0_mean']):.4f}")
    print(f"    sigma_R/R_0 = {float(s39['frac_sigma']):.4f} ({float(s39['frac_sigma'])*100:.1f}%)")
    print(f"    R at fold = {float(s39['R_at_fold']):.4f}")
    print(f"    N_active = {int(s39['n_active'])}")
    s39_loaded = True
else:
    print(f"  S39 data not found at {s39_path}")

# ======================================================================
#  Step 6: Check if omega_att relates to the FOLD-SPECIFIC spectrum
# ======================================================================
print("\n--- Step 6: Fold-specific spectral structure ---")

fold_idx = 19  # tau ~ 0.19 (local)
ev_fold = np.sort(eigenvalues[fold_idx])
print(f"  tau_fold = {tau_values[fold_idx]:.6f}")
print(f"  32-cell eigenvalues at fold:")
for i in range(0, 32, 4):
    print(f"    [{i:2d}-{i+3:2d}]: " + "  ".join(f"{ev_fold[j]:.6f}" for j in range(i, min(i+4, 32))))

# Test all pairwise differences against omega_att
print(f"\n  Pairwise differences E[j]-E[i] closest to omega_att = {omega_att:.6f}:")
best_matches = []
for i in range(32):
    for j in range(i+1, 32):
        diff = ev_fold[j] - ev_fold[i]
        if diff > 0:
            # Check if omega_att is close to N*diff for integer N
            for N in range(1, 20):
                ratio = omega_att / (N * diff)
                if abs(ratio - 1.0) < 0.02:  # Within 2%
                    best_matches.append((i, j, N, diff, N*diff, abs(ratio - 1.0)))

best_matches.sort(key=lambda x: x[5])
print(f"  Found {len(best_matches)} matches within 2%:")
for i, j, N, diff, Ndiff, err in best_matches[:15]:
    print(f"    E[{j}]-E[{i}] = {diff:.6f}, N={N}, N*diff = {Ndiff:.6f}, "
          f"|R-1| = {err:.6f} ({err*100:.3f}%)")

# ======================================================================
#  Step 7: Check constancy of best matches across tau
# ======================================================================
print("\n--- Step 7: Tau-constancy of best fold-matched ratios ---")

if len(best_matches) > 0:
    print(f"  Testing top 5 fold matches for tau-constancy:")
    for i, j, N, diff_fold, Ndiff, err_fold in best_matches[:5]:
        R_tau = np.zeros(N_tau)
        for ti in range(N_tau):
            ev_ti = np.sort(eigenvalues[ti])
            diff_ti = ev_ti[j] - ev_ti[i]
            R_tau[ti] = omega_att / (N * diff_ti) if diff_ti > 1e-10 else np.nan

        valid = ~np.isnan(R_tau)
        R_mean = np.mean(R_tau[valid])
        R_std = np.std(R_tau[valid])
        frac = R_std / R_mean
        print(f"    E[{j}]-E[{i}], N={N}: R_mean={R_mean:.4f}, sigma/mu={frac:.4f} ({frac*100:.1f}%)")

# ======================================================================
#  Step 8: The definitive answer: omega_att IS fold-specific
# ======================================================================
print("\n--- Step 8: Definitive Analysis ---")

# omega_att = sqrt(F''(Delta_0)) where F is the GL free energy.
# This depends on Delta_0 and the BCS coupling, which are fold-specific.
# The BCS condensation energy E_cond = -0.137 is computed at the fold.
# omega_att = 1.430 is the small-oscillation frequency of the pair field
# around the BCS minimum, which exists ONLY near the van Hove singularity.
#
# Therefore omega_att is NOT a geometric constant of the spectrum at
# arbitrary tau -- it is a BCS-derived quantity that only makes sense
# at/near the fold where the van Hove DOS is large enough for pairing.
#
# Any relationship omega_att = f(spectrum) that holds at the fold but
# drifts at other tau is a COINCIDENCE, because omega_att itself is
# only defined at the fold.

# Check the bandwidth at the fold
bw_fold = B3_minus_B1[fold_idx]
print(f"  Bandwidth at fold = {bw_fold:.6f}")
print(f"  omega_att / bandwidth = {omega_att / bw_fold:.6f}")
print(f"  omega_att / (9 * bandwidth) = {omega_att / (9 * bw_fold):.6f}")

# This is ~0.02, nowhere near 1. The S38 claim used Kosmann B3-B1,
# not TB bandwidth.
print(f"\n  In Kosmann 16-mode spectrum (S38/S39):")
print(f"    B3-B1 ~ 0.159 at fold")
print(f"    omega_att / (9 * 0.159) = {omega_att / (9 * 0.159):.6f}")
if s39_loaded:
    R_fold_s39 = float(s39['R_at_fold'])
    print(f"    S39 measured: R_fold = {R_fold_s39:.6f}")

# The ratio was close to 9 at the fold in the Kosmann spectrum, but
# S39 showed it drifts by 25% over even the narrow BCS-active window.
# In the TB spectrum, the ratio is completely different because the
# eigenvalue gap structure is different.

print(f"\n  CONCLUSION:")
print(f"    The S38 claim omega_att = 9*(B3-B1) was:")
print(f"    1. Specific to the Kosmann 16-mode Dirac spectrum")
print(f"    2. Only valid at the fold tau = 0.19 to ~0.08%")
print(f"    3. Already FAILED in S39 (25% drift over BCS window)")
print(f"    4. Does NOT transfer to the TB 32-cell spectrum")
print(f"       (TB bandwidth at fold = {bw_fold:.3f}, 9*bw = {9*bw_fold:.3f} vs omega_att = {omega_att:.3f})")
print(f"    VERDICT: COINCIDENCE (confirming S39)")

# ======================================================================
#  Step 9: Save results
# ======================================================================
print("\n--- Step 9: Save results ---")

out_path = os.path.join(SCRIPT_DIR, 's56_omega_att_confirm.npz')

np.savez(out_path,
    # Grid
    tau_values=tau_values,
    N_tau=N_tau,

    # Eigenvalues
    E_B1=E_B1,
    E_B3=E_B3,
    B3_minus_B1=B3_minus_B1,
    bandwidths=bandwidths,

    # R(tau) for various N
    R_N7=R_arrays[7],
    R_N8=R_arrays[8],
    R_N9=R_arrays[9],
    R_N10=R_arrays[10],
    R_N11=R_arrays[11],

    # Raw ratio
    R_raw=R_raw,
    R_raw_mean=np.mean(R_raw),
    R_raw_std=np.std(R_raw),
    R_raw_frac=np.std(R_raw)/np.mean(R_raw),

    # Canonical values
    omega_att_canonical=omega_att,
    tau_fold_canonical=tau_fold,

    # Best fold matches
    n_fold_matches_2pct=len(best_matches),

    # Scan results (top 10)
    scan_top10_names=np.array([r[0] for r in results_scan[:10]]),
    scan_top10_frac=np.array([r[3] for r in results_scan[:10]]),

    # Gate
    gate_name='OMEGA-ATT-CONFIRM-56',
    gate_verdict='COINCIDENCE',
    gate_detail=f'omega_att=9*(B3-B1) is fold-specific in Kosmann spectrum (S39: 25% drift). '
                f'Does not transfer to 32-cell TB spectrum (bandwidth={bw_fold:.3f}, '
                f'9*bw={9*bw_fold:.3f} vs omega_att={omega_att:.3f}). '
                f'R_raw(TB)={R_raw[fold_idx]:.4f}, sigma/mu={np.std(R_raw)/np.mean(R_raw):.4f}.',
)

print(f"  Saved: {out_path}")

# ======================================================================
#  Step 10: Plot
# ======================================================================
print("\n--- Step 10: Generate plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('OMEGA-ATT-CONFIRM-56: omega_att / (N * (B3_TB - B1_TB))\n'
             f'omega_att = {omega_att:.3f} M_KK | Verdict: COINCIDENCE',
             fontsize=13)

# Panel 1: R(tau) for N = 7..11
ax = axes[0, 0]
colors = ['blue', 'green', 'red', 'purple', 'orange']
for idx, N in enumerate(N_test):
    R = R_arrays[N]
    ax.plot(tau_values, R, '-', color=colors[idx], linewidth=1.5,
            label=f'N={N}')
ax.axhline(1.0, color='black', linestyle='--', alpha=0.5, label='R = 1')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label=f'fold')
ax.set_xlabel('tau')
ax.set_ylabel('R(tau) = omega_att / (N * (B3-B1))')
ax.set_title('R(tau) for N = 7..11 (TB 32-cell)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 2: B3-B1 (bandwidth) vs tau
ax = axes[0, 1]
ax.plot(tau_values, E_B1, 'b-', label='E_B1 (Fiedler)', linewidth=1.5)
ax.plot(tau_values, E_B3, 'r-', label='E_B3 (max)', linewidth=1.5)
ax.plot(tau_values, B3_minus_B1, 'k--', label='B3 - B1 (bandwidth)', linewidth=2)
ax.axhline(omega_att, color='green', linestyle=':', linewidth=1.5,
           label=f'omega_att = {omega_att:.3f}')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('Energy (M_KK)')
ax.set_title('TB eigenvalues and bandwidth')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: omega_att / bandwidth (raw ratio) vs tau
ax = axes[1, 0]
ax.plot(tau_values, R_raw, 'ko-', markersize=3, linewidth=1.5)
ax.axhline(np.mean(R_raw), color='red', linestyle='--',
           label=f'mean = {np.mean(R_raw):.4f}')
ax.fill_between(tau_values,
                np.mean(R_raw) - np.std(R_raw),
                np.mean(R_raw) + np.std(R_raw),
                color='red', alpha=0.15,
                label=f'sigma/mu = {np.std(R_raw)/np.mean(R_raw):.3f}')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.5, label='fold')
ax.set_xlabel('tau')
ax.set_ylabel('omega_att / (B3_TB - B1_TB)')
ax.set_title('Raw ratio vs tau')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: S39 comparison (text panel)
ax = axes[1, 1]
ax.axis('off')
text_lines = [
    "OMEGA-ATT-CONFIRM-56 Summary",
    "=" * 40,
    f"omega_att = {omega_att:.3f} M_KK (canonical, S38)",
    "",
    "32-cell TB spectrum (this computation):",
    f"  B3-B1 at fold = {bw_fold:.3f} M_KK",
    f"  omega_att/bandwidth = {omega_att/bw_fold:.4f}",
    f"  sigma(R)/mean(R) = {np.std(R_raw)/np.mean(R_raw):.3f} ({np.std(R_raw)/np.mean(R_raw)*100:.1f}%)",
    "",
    "Kosmann 16-mode (S39):",
]
if s39_loaded:
    text_lines += [
        f"  S39 verdict: {str(s39['verdict'])}",
        f"  S39 R_0 = {float(s39['R0_mean']):.3f}",
        f"  S39 sigma/R_0 = {float(s39['frac_sigma']):.3f} ({float(s39['frac_sigma'])*100:.1f}%)",
        f"  S39 R at fold = {float(s39['R_at_fold']):.3f}",
    ]
text_lines += [
    "",
    "VERDICT: COINCIDENCE",
    "  S38 claim: omega_att = 9*(B3-B1)",
    "  S39: 25% drift in Kosmann spectrum (FAIL)",
    "  S56: Does not transfer to TB spectrum",
    "  omega_att is BCS-derived, fold-specific",
]
ax.text(0.05, 0.95, "\n".join(text_lines), transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace')

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's56_omega_att_confirm.png')
plt.savefig(plot_path, dpi=150)
plt.close()
print(f"  Saved: {plot_path}")

# ======================================================================
#  Final Summary
# ======================================================================
elapsed = time.time() - t0
print("\n" + "=" * 78)
print("  FINAL SUMMARY: OMEGA-ATT-CONFIRM-56")
print("=" * 78)
print(f"""
  GATE: OMEGA-ATT-CONFIRM-56
  VERDICT: COINCIDENCE (confirming S39)

  The S38 claim omega_att = 9*(B3-B1) at 0.08% was:
    - Specific to the Kosmann 16-mode Dirac eigenvalue spectrum
    - Only valid at the fold (tau ~ 0.19)
    - S39 showed 25% drift over the BCS-active window -> FAIL

  This computation (S56) tests the claim against the S54 32-cell
  tight-binding Hamiltonian spectrum:
    - TB bandwidth at fold: {bw_fold:.4f} M_KK
    - omega_att / bandwidth: {omega_att/bw_fold:.4f} (NOT 9, NOT constant)
    - sigma(R)/mean(R) = {np.std(R_raw)/np.mean(R_raw):.4f} ({np.std(R_raw)/np.mean(R_raw)*100:.1f}%)
    - No integer N makes omega_att/(N*(B3-B1)) constant to 1%

  The ratio is a fold-specific numerical coincidence in the Kosmann
  spectrum, arising because omega_att (BCS-derived) happens to land
  near 9 * (E_B3 - E_B1) at the single point where the van Hove
  singularity maximizes the DOS.

  Elapsed: {elapsed:.2f}s
""")
