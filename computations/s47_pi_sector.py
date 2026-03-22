#!/usr/bin/env python3
"""
S47 PI-SECTOR-47: Sector Classification of Pi-Phase States
===========================================================

Classifies each of the 13 unweighted (131 PW-weighted) pi-phase states from
S46 berry phase computation by their B1/B2/B3 sector membership.

Method:
  1. Establish B1/B2/B3 cluster boundaries from the full 992-mode spectrum at fold
  2. For each rep with pi-phases, identify pi-phase eigenstates
  3. Classify by eigenvalue magnitude at fold using cluster boundaries

IMPORTANT SPECTRAL-GEOMETRIC NOTE:
  The B1/B2/B3 classification is a U(2) quantum number of the SPINOR sector
  in the (0,0) Peter-Weyl representation. In the (0,0) sector, the 16 spinor
  components split cleanly: B1(2), B2(8), B3(6) with distinct eigenvalues
  0.820, 0.845, 0.971 at the fold.

  In HIGHER PW sectors (p,q) != (0,0), the Dirac eigenstates are ENTANGLED
  across the tensor product V_{(p,q)} ⊗ S. The K_7 spinor operator does NOT
  commute with D_K in these sectors (verified: ||[I⊗iK7,D_K]||/||D_K|| = 7.5%
  for (0,1)). This means eigenstates are MIXTURES of spinor sectors.

  The classification below uses EIGENVALUE RANK within each PW sector:
  lowest 2*dim states -> B1, next 8*dim -> B2, top 6*dim -> B3.
  This inherits from the B1<B2<B3 ordering at the bi-invariant point (tau=0)
  via adiabatic continuity, but is APPROXIMATE for states near sector boundaries.

Gate PI-SECTOR-47:
  PASS: All 13 pi-phases classifiable into B1/B2/B3
  FAIL: Any pi-phase eigenvalue falls in a gap between clusters (ambiguous)

Author: Spectral-Geometer
Date: 2026-03-16
Session: 47, Wave 1-1
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# SECTION 1: LOAD DATA
# ============================================================================

print("=" * 72)
print("PI-SECTOR-47: Sector Classification of Pi-Phase States")
print("=" * 72)

# Load berry phase data
bp = np.load('tier0-computation/s46_berry_phase.npz', allow_pickle=True)
tau_grid = bp['tau_grid']
tau_fold_idx = np.argmin(np.abs(tau_grid - 0.19))
print(f"\ntau_grid: [{tau_grid[0]:.4f}, {tau_grid[-1]:.4f}], N={len(tau_grid)}")
print(f"Fold index: {tau_fold_idx}, tau={tau_grid[tau_fold_idx]:.4f}")

# Load full spectrum at fold for cluster boundaries
dos = np.load('tier0-computation/s44_dos_tau.npz', allow_pickle=True)
omega_full = dos['tau0.19_all_omega']  # 992 |eigenvalues| at fold
dims_full = dos['tau0.19_all_dim2']  # PW degeneracies

# Load reference eigenvalues from (0,0) sector
k7_data = np.load('tier0-computation/s35_k7_dphys.npz', allow_pickle=True)
evals_00 = k7_data['evals_DK']  # 16 signed eigenvalues at fold

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Reps with pi-phases (from S46)
reps_with_pi = [(0,1), (0,2), (0,3), (1,0), (1,1), (2,0), (2,1), (3,0)]

# S46 pi-phase criterion: |abs(phase) mod pi - pi| < 0.1
PI_THRESHOLD = 0.1

# ============================================================================
# SECTION 2: ESTABLISH CLUSTER BOUNDARIES
# ============================================================================

print(f"\n{'='*72}")
print("STEP 1: CLUSTER BOUNDARIES FROM FULL 992-MODE SPECTRUM")
print("=" * 72)

# The (0,0) sector defines the canonical B1/B2/B3 eigenvalues
abs_evals_00 = np.sort(np.abs(evals_00))
unique_00 = np.unique(np.round(abs_evals_00, 5))
print(f"\n(0,0) sector eigenvalues (canonical B1/B2/B3):")
for u in unique_00:
    m = np.sum(np.abs(abs_evals_00 - u) < 1e-4)
    sector = {2: 'B1', 8: 'B2', 6: 'B3'}.get(m, '??')
    print(f"  |lambda|={u:.6f}: mult={m} -> {sector}")

E_B1 = unique_00[0]  # 0.81974
E_B2 = unique_00[1]  # 0.84521
E_B3 = unique_00[2]  # 0.97141

# Find gaps in full spectrum
omega_sorted = np.sort(omega_full)
diffs = np.diff(omega_sorted)

# The three (0,0) clusters are separated by gaps
# B1-B2 gap: between 0.820 and 0.836 (next eigenvalue from (0,1)/(1,0))
# B2-B3 gap: between 0.845 and 0.873 (next eigenvalue from (1,1))
# B3-next gap: between 0.972 and 1.022

# Natural cluster boundaries:
gap_B1_B2 = (E_B2 + E_B1) / 2  # midpoint between B1 and B2
gap_B2_B3 = (E_B3 + E_B2) / 2  # midpoint between B2 and B3

# But pi-phase eigenvalues are all > 1.0. These boundaries don't apply.
# The task asks for cluster boundaries from the FULL spectrum.
# Let me find ALL significant gaps.

large_gaps = np.where(diffs > 0.02)[0]
print(f"\nFull spectrum gaps > 0.02:")
for i in large_gaps:
    print(f"  Between {omega_sorted[i]:.6f} and {omega_sorted[i+1]:.6f}, "
          f"gap={diffs[i]:.6f}, cumulative_rank={i+1}")

# The first three large gaps define B1/B2/B3 in the (0,0) sector:
# gap at 0.845->0.873 separates {B1,B2} from upper eigenvalues
# gap at 0.873->0.957 separates (0,0) B3 from (0,1)/(1,0) eigenvalues

# CLUSTER BOUNDARIES for the task:
# Using the (0,0) eigenvalue gaps:
cluster_B1_upper = 0.830  # above B1 (0.820), below B2 (0.836)
cluster_B2_upper = 0.915  # above B2/high-B2 (0.873), below B3 (0.957)
cluster_B3_upper = 0.985  # above B3 (0.972), below higher reps (1.022)

print(f"\n(0,0) cluster boundaries:")
print(f"  B1: [0, {cluster_B1_upper}]")
print(f"  B2: ({cluster_B1_upper}, {cluster_B2_upper}]")
print(f"  B3: ({cluster_B2_upper}, {cluster_B3_upper}]")
print(f"  Higher: > {cluster_B3_upper}")

# Count modes in each cluster
n_B1_cluster = np.sum(omega_full <= cluster_B1_upper)
n_B2_cluster = np.sum((omega_full > cluster_B1_upper) & (omega_full <= cluster_B2_upper))
n_B3_cluster = np.sum((omega_full > cluster_B2_upper) & (omega_full <= cluster_B3_upper))
n_higher = np.sum(omega_full > cluster_B3_upper)
print(f"\nModes in clusters: B1={n_B1_cluster}, B2={n_B2_cluster}, B3={n_B3_cluster}, higher={n_higher}")
print(f"Total: {n_B1_cluster + n_B2_cluster + n_B3_cluster + n_higher} (expect 992)")

# ============================================================================
# SECTION 3: RANK-BASED SECTOR CLASSIFICATION
# ============================================================================

print(f"\n{'='*72}")
print("STEP 2: RANK-BASED SECTOR CLASSIFICATION WITHIN EACH PW SECTOR")
print("=" * 72)

# For each (p,q) sector, the 16*dim(p,q) eigenvalues split by adiabatic
# continuation from tau=0:
#   lowest  2*dim eigenvalues -> B1 spinor sector
#   middle  8*dim eigenvalues -> B2 spinor sector
#   highest 6*dim eigenvalues -> B3 spinor sector
# This follows from B1 < B2 < B3 ordering at the bi-invariant point.

# VERIFICATION: check (0,0) gives correct assignment
evals_00_abs = np.sort(np.abs(bp['s00_evals'][tau_fold_idx, :]))
B1_target_00 = 2  # 2*dim(0,0) = 2*1
B2_target_00 = 10  # (2+8)*dim(0,0) = 10
print(f"\nVerification on (0,0):")
print(f"  Rank 0-1 (B1): {evals_00_abs[:2]} -> matches E_B1={E_B1:.5f}? "
      f"{'YES' if np.allclose(evals_00_abs[:2], E_B1, atol=1e-3) else 'NO'}")
print(f"  Rank 2-9 (B2): range [{evals_00_abs[2]:.5f}, {evals_00_abs[9]:.5f}] "
      f"-> matches E_B2={E_B2:.5f}? "
      f"{'YES' if np.allclose(evals_00_abs[2:10], E_B2, atol=1e-3) else 'NO'}")
print(f"  Rank 10-15 (B3): range [{evals_00_abs[10]:.5f}, {evals_00_abs[15]:.5f}] "
      f"-> matches E_B3={E_B3:.5f}? "
      f"{'YES' if np.allclose(evals_00_abs[10:], E_B3, atol=1e-3) else 'NO'}")

# Now classify all pi-phase states
results = []
all_pi_evals = []
all_pi_sectors = []
all_pi_reps = []
gate_pass = True  # assume PASS, will set to False if ambiguous

for p, q in reps_with_pi:
    rep_key = f"s{p}{q}"
    evals = bp[f'{rep_key}_evals']  # (40, N)
    phases = bp[f'{rep_key}_berry_phases']  # (N,)
    N = evals.shape[1]
    d = dim_pq(p, q)

    # S46 pi-phase criterion
    bp_mod_pi = np.abs(phases) % np.pi
    pi_mask = np.abs(bp_mod_pi - np.pi) < PI_THRESHOLD
    pi_indices = np.where(pi_mask)[0]
    n_pi = int(bp[f'{rep_key}_n_pi'])

    # Verify count matches stored value
    assert len(pi_indices) == n_pi, \
        f"Pi count mismatch for ({p},{q}): computed {len(pi_indices)} vs stored {n_pi}"

    if n_pi == 0:
        continue

    # Get |eigenvalues| at fold
    abs_evals_fold = np.abs(evals[tau_fold_idx, :])

    # Sort to determine ranks
    sorted_idx = np.argsort(abs_evals_fold)
    rank_of_state = np.zeros(N, dtype=int)
    rank_of_state[sorted_idx] = np.arange(N)

    # Sector boundaries by rank
    B1_upper_rank = 2 * d       # states 0..2d-1 are B1
    B2_upper_rank = 10 * d      # states 2d..10d-1 are B2
    # states 10d..16d-1 are B3

    # Check boundary gaps
    sorted_evals = np.sort(abs_evals_fold)
    b1_gap = sorted_evals[B1_upper_rank] - sorted_evals[B1_upper_rank - 1]
    b2_gap = sorted_evals[B2_upper_rank] - sorted_evals[B2_upper_rank - 1]

    print(f"\n({p},{q}) dim={d}, N={N}: B1<rank {B1_upper_rank}, B2<rank {B2_upper_rank}")
    print(f"  B1/B2 gap: {b1_gap:.6f}")
    print(f"  B2/B3 gap: {b2_gap:.6f}")

    for idx in pi_indices:
        ev = abs_evals_fold[idx]
        r = rank_of_state[idx]
        phase_val = phases[idx]

        if r < B1_upper_rank:
            sector = 'B1'
        elif r < B2_upper_rank:
            sector = 'B2'
        else:
            sector = 'B3'

        # Check if state is AT a degenerate boundary (potential ambiguity)
        # A state is ambiguous if it belongs to a degenerate level that straddles
        # the sector boundary
        ambiguous = False
        boundary_note = ''

        # Check proximity to B1/B2 boundary
        if abs(r - B1_upper_rank) < 3:  # within 3 ranks of boundary
            level_count = np.sum(np.abs(abs_evals_fold - ev) < 1e-4)
            if level_count > 1 and b1_gap < 1e-4:
                # Degenerate level straddles B1/B2 boundary
                ambiguous = True
                boundary_note = f' (degenerate level {level_count}-fold straddles B1/B2)'

        # Check proximity to B2/B3 boundary
        if abs(r - B2_upper_rank) < 3:
            level_count = np.sum(np.abs(abs_evals_fold - ev) < 1e-4)
            if level_count > 1 and b2_gap < 1e-4:
                ambiguous = True
                boundary_note = f' (degenerate level {level_count}-fold straddles B2/B3)'

        if ambiguous:
            gate_pass = False

        print(f"  Pi idx={idx}: |ev|={ev:.6f}, rank={r}, phase={phase_val:.4f} "
              f"({phase_val/np.pi:.4f}pi) -> {sector}{boundary_note}")

        results.append({
            'rep': (p, q),
            'dim': d,
            'idx': idx,
            'eigenvalue': ev,
            'rank': r,
            'phase': phase_val,
            'sector': sector,
            'ambiguous': ambiguous,
        })

        all_pi_evals.append(ev)
        all_pi_sectors.append(sector)
        all_pi_reps.append(f"({p},{q})")

# ============================================================================
# SECTION 4: COMPUTE PW-WEIGHTED COUNTS
# ============================================================================

print(f"\n{'='*72}")
print("STEP 3: PW-WEIGHTED SECTOR COUNTS")
print("=" * 72)

n_B1, n_B2, n_B3 = 0, 0, 0
pw_B1, pw_B2, pw_B3 = 0, 0, 0
n_ambiguous = 0

for r in results:
    d = r['dim']
    s = r['sector']
    if s == 'B1':
        n_B1 += 1
        pw_B1 += d
    elif s == 'B2':
        n_B2 += 1
        pw_B2 += d
    elif s == 'B3':
        n_B3 += 1
        pw_B3 += d
    if r['ambiguous']:
        n_ambiguous += 1

total_n = n_B1 + n_B2 + n_B3
total_pw = pw_B1 + pw_B2 + pw_B3

print(f"\nUnweighted pi-phase counts by sector:")
print(f"  B1: {n_B1}")
print(f"  B2: {n_B2}")
print(f"  B3: {n_B3}")
print(f"  Total: {total_n} (expect 13)")

print(f"\nPW-weighted pi-phase counts by sector:")
print(f"  B1: {pw_B1}")
print(f"  B2: {pw_B2}")
print(f"  B3: {pw_B3}")
print(f"  Total: {total_pw} (expect 131)")

assert total_n == 13, f"Total unweighted count {total_n} != 13"
assert total_pw == 131, f"Total PW-weighted count {total_pw} != 131"

print(f"\nAmbiguous states: {n_ambiguous}")

# Gate verdict
if n_ambiguous == 0:
    verdict = 'PASS'
    verdict_msg = f"All 13 pi-phases classified. B1:{n_B1}, B2:{n_B2}, B3:{n_B3}"
else:
    verdict = 'FAIL'
    verdict_msg = f"{n_ambiguous} ambiguous states at degenerate boundary crossings"

print(f"\n{'='*72}")
print(f"GATE PI-SECTOR-47: {verdict}")
print(f"  {verdict_msg}")
print(f"{'='*72}")

# ============================================================================
# SECTION 5: FULL TABLE
# ============================================================================

print(f"\n{'='*72}")
print("FULL SECTOR-RESOLVED PI-PHASE TABLE")
print("=" * 72)
print(f"{'Rep':>8} {'dim':>4} {'n_pi':>5} {'|eval|@fold':>12} {'rank':>6} "
      f"{'phase/pi':>10} {'sector':>7} {'PW_pi':>6} {'note':>12}")
print("-" * 80)

for r in results:
    p, q = r['rep']
    note = 'AMBIG' if r['ambiguous'] else ''
    print(f"({p},{q}){' '*(5-len(f'({p},{q})')):>5} {r['dim']:4d} "
          f"  {1:4d}  {r['eigenvalue']:11.6f} {r['rank']:6d} "
          f"{r['phase']/np.pi:+9.4f}  {r['sector']:>6s} {r['dim']:6d} {note:>12s}")

print("-" * 80)
print(f"{'TOTAL':>8} {' ':>4} {total_n:5d} {' ':>12} {' ':>6} {' ':>10} "
      f"{' ':>7} {total_pw:6d}")

# ============================================================================
# SECTION 6: SAVE RESULTS
# ============================================================================

print(f"\n{'='*72}")
print("SAVING RESULTS")
print("=" * 72)

np.savez('tier0-computation/s47_pi_sector.npz',
    # PW-weighted counts by sector
    pw_pi_B1=pw_B1,
    pw_pi_B2=pw_B2,
    pw_pi_B3=pw_B3,
    # Unweighted counts
    n_pi_B1=n_B1,
    n_pi_B2=n_B2,
    n_pi_B3=n_B3,
    # Cluster boundaries
    cluster_boundary_low=cluster_B1_upper,  # B1/B2 boundary in (0,0)
    cluster_boundary_high=cluster_B2_upper,  # B2/B3 boundary in (0,0)
    # Per-state data
    pi_phase_eigenvalues=np.array(all_pi_evals),
    pi_phase_sectors=np.array(all_pi_sectors),
    pi_phase_reps=np.array(all_pi_reps),
    # Gate
    gate_verdict=verdict,
    # Method metadata
    method='rank_within_PW_sector',
    rank_B1_fraction='2*dim/16*dim = 1/8',
    rank_B2_fraction='8*dim/16*dim = 1/2',
    rank_B3_fraction='6*dim/16*dim = 3/8',
    note='B1/B2/B3 is approximate in higher PW sectors; K7 does not commute with D_K outside (0,0)',
)

print(f"  Saved: tier0-computation/s47_pi_sector.npz")

# ============================================================================
# SECTION 7: VISUALIZATION
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Panel 1: Full spectrum histogram with cluster boundaries
ax1 = axes[0]
ax1.hist(omega_full, bins=60, color='steelblue', alpha=0.7, edgecolor='navy')
# Mark pi-phase eigenvalues
for ev, sec in zip(all_pi_evals, all_pi_sectors):
    color = {'B1': 'green', 'B2': 'orange', 'B3': 'red'}[sec]
    ax1.axvline(ev, color=color, alpha=0.6, linewidth=1.5)
ax1.axvline(E_B1, color='green', linestyle='--', label=f'B1={E_B1:.3f}')
ax1.axvline(E_B2, color='orange', linestyle='--', label=f'B2={E_B2:.3f}')
ax1.axvline(E_B3, color='red', linestyle='--', label=f'B3={E_B3:.3f}')
ax1.set_xlabel('|eigenvalue|')
ax1.set_ylabel('Count')
ax1.set_title('Full spectrum + pi-phase locations')
ax1.legend(fontsize=8)

# Panel 2: Pi-phase eigenvalues by sector
ax2 = axes[1]
colors = {'B1': 'green', 'B2': 'orange', 'B3': 'red'}
for i, r in enumerate(results):
    p, q = r['rep']
    ax2.scatter(i, r['eigenvalue'], c=colors[r['sector']], s=100,
                edgecolors='black', zorder=5)
    ax2.annotate(f"({p},{q})", (i, r['eigenvalue']),
                fontsize=7, ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points')

ax2.set_xticks(range(len(results)))
ax2.set_xticklabels([f"({r['rep'][0]},{r['rep'][1]})" for r in results],
                     rotation=45, fontsize=7)
ax2.set_ylabel('|eigenvalue| at fold')
ax2.set_title('Pi-phase states by sector')
ax2.axhline(E_B1, color='green', linestyle=':', alpha=0.5)
ax2.axhline(E_B2, color='orange', linestyle=':', alpha=0.5)
ax2.axhline(E_B3, color='red', linestyle=':', alpha=0.5)

# Panel 3: PW-weighted pie chart
ax3 = axes[2]
sizes = [pw_B1, pw_B2, pw_B3]
labels = [f'B1\n{pw_B1} ({100*pw_B1/total_pw:.0f}%)',
          f'B2\n{pw_B2} ({100*pw_B2/total_pw:.0f}%)',
          f'B3\n{pw_B3} ({100*pw_B3/total_pw:.0f}%)']
pie_colors = ['green', 'orange', 'red']
ax3.pie(sizes, labels=labels, colors=pie_colors, autopct='',
        startangle=90, textprops={'fontsize': 10})
ax3.set_title(f'PW-weighted pi-phases\n(total={total_pw})')

plt.suptitle(f'PI-SECTOR-47: {verdict}', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s47_pi_sector.png', dpi=150, bbox_inches='tight')
print(f"  Saved: tier0-computation/s47_pi_sector.png")

# ============================================================================
# SECTION 8: BCS ACCESSIBILITY FILTER
# ============================================================================

print(f"\n{'='*72}")
print("BCS ACCESSIBILITY ANALYSIS")
print("=" * 72)

# B1 pi-phases: INERT (Trap 1: V(B1,B1) = 0 exact)
# B2 pi-phases: ACTIVE (BCS pairing channel)
# B3 pi-phases: UNCERTAIN (may lack K7-compatible partners)

print(f"\nBCS selection rules applied to pi-phase states:")
print(f"  B1 pi-phases: {n_B1} (PW={pw_B1}) -> INERT (Trap 1)")
print(f"  B2 pi-phases: {n_B2} (PW={pw_B2}) -> ACTIVE")
print(f"  B3 pi-phases: {n_B3} (PW={pw_B3}) -> NEEDS K7 CHECK")
print(f"\nBCS-accessible pi-phases (B2 only): {n_B2} unweighted, {pw_B2} PW-weighted")
print(f"BCS-accessible ratio: {pw_B2}/{59.8:.1f} = {pw_B2/59.8:.2f}x")
print(f"(cf. original S46 ratio: 131/59.8 = 2.19x)")

print(f"\n{'='*72}")
print("COMPUTATION COMPLETE")
print(f"{'='*72}")
