#!/usr/bin/env python3
"""
s61_yukawa_pw_tower.py — Full Peter-Weyl Fermion Mass Tower
============================================================

Baptista Paper 14: "the full calculation of the fermionic mass terms
produced by the model is longer and is not carried out here."

THIS IS THAT CALCULATION.

Each SU(3) irrep (p,q) gives a different effective mass for the KK
fermion. If the SM's three generations correspond to three different
irrep sectors, the mass hierarchy comes from the Casimir differences.

Method:
  1. Build D_K on Jensen-deformed SU(3) at tau_fold = 0.19
  2. For each irrep (p,q) up to max_pq_sum = 5:
     - Construct D_K on that sector via dirac_spectrum
     - Diagonalize, get all eigenvalues
     - Extract the LOWEST positive eigenvalue = lightest fermion mass in that sector
  3. Sort sectors by lightest mass
  4. Compute mass RATIOS between sectors
  5. Compare to PDG mass ratios: m_t/m_u ~ 7.5e4, m_b/m_d ~ 900, m_tau/m_e ~ 3477

Gate: YUKAWA-PW-TOWER-61
  PASS if any inter-sector mass ratio > 100
  FAIL if all ratios < 10
  INFO if 10-100

Session 61
"""

import numpy as np
from numpy.linalg import eigh, norm
import sys, os, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, M_KK, PI

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    validate_clifford, build_chirality,
    get_irrep, dirac_operator_on_irrep, _irrep_cache,
)

print("=" * 72)
print("S61 YUKAWA-PW-TOWER: Full Peter-Weyl Fermion Mass Spectrum")
print("=" * 72)
print(f"  tau_fold = {tau_fold}")
print(f"  M_KK = {M_KK:.4e} GeV")

# =====================================================================
# SECTION 1: Build infrastructure at tau_fold
# =====================================================================
print("\nSECTION 1: Lie algebra + Clifford + Connection at fold")
sys.stdout.flush()

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
g_fold = jensen_metric(B_ab, tau_fold)
E_fold = orthonormal_frame(g_fold)
ft_fold = frame_structure_constants(f_abc, E_fold)
Gamma_fold = connection_coefficients(ft_fold)
gammas = build_cliff8()
gamma9 = build_chirality(gammas)
Omega_fold = spinor_connection_offset(Gamma_fold, gammas)

cliff_err = validate_clifford(gammas)
print(f"  Clifford error: {cliff_err:.2e}")
assert cliff_err < 1e-14

# =====================================================================
# SECTION 2: Compute D_K eigenvalues for all irreps up to max_pq_sum
# =====================================================================
MAX_PQ_SUM = 5  # (local)
print(f"\nSECTION 2: D_K eigenvalues for all irreps, max_pq_sum = {MAX_PQ_SUM}")
sys.stdout.flush()

results = []
t0 = time.time()

for p in range(MAX_PQ_SUM + 1):
    for q in range(MAX_PQ_SUM + 1 - p):
        if p == 0 and q == 0:
            # Singlet: D_K = Omega (spinor connection only)
            D_pi = Omega_fold.copy()
            dim_pq = 1
        else:
            try:
                rho, dim_check = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E_fold, gammas, Omega_fold)
                dim_pq = dim_check
            except Exception as e:
                print(f"  ({p},{q}): SKIP — {e}")
                continue

        # Diagonalize
        H = 1j * D_pi  # Hermitian
        h_err = np.max(np.abs(H - H.conj().T))
        if h_err > 1e-10:
            H = 0.5 * (H + H.conj().T)

        evals = np.sort(np.linalg.eigvalsh(H))

        # Casimir
        C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
        dim_irrep = (p + 1) * (q + 1) * (p + q + 2) // 2

        # Extract positive eigenvalues (J-symmetry pairs +/- )
        pos_evals = evals[evals > 1e-12]
        if len(pos_evals) == 0:
            min_pos = 0.0
        else:
            min_pos = np.min(pos_evals)

        # All positive eigenvalues for the sector
        all_pos = np.sort(pos_evals)

        results.append({
            'p': p, 'q': q,
            'dim_irrep': dim_irrep,
            'dim_matrix': len(evals),
            'C2': C2,
            'min_pos_eval': min_pos,
            'max_eval': np.max(np.abs(evals)),
            'n_pos': len(pos_evals),
            'all_pos': all_pos[:10] if len(all_pos) > 10 else all_pos,  # first 10
            'bandwidth': np.max(np.abs(evals)) - np.min(np.abs(evals[np.abs(evals) > 1e-12])) if np.any(np.abs(evals) > 1e-12) else 0,
        })

        elapsed = time.time() - t0
        print(f"  ({p},{q}): dim_irrep={dim_irrep}, dim_H={len(evals)}, "
              f"C2={C2:.2f}, min_pos={min_pos:.6f}, max={np.max(np.abs(evals)):.4f}, "
              f"n_pos={len(pos_evals)} [{elapsed:.1f}s]")
        sys.stdout.flush()

print(f"\n  Total sectors: {len(results)}, time: {time.time()-t0:.1f}s")

# =====================================================================
# SECTION 3: Mass hierarchy analysis
# =====================================================================
print("\n" + "=" * 72)
print("SECTION 3: MASS HIERARCHY FROM PW TOWER")
print("=" * 72)

# Sort by lightest mass (min positive eigenvalue)
sorted_results = sorted(results, key=lambda r: r['min_pos_eval'] if r['min_pos_eval'] > 0 else 1e10)

print("\n  Sectors sorted by lightest fermion mass:")
print(f"  {'(p,q)':>8s} {'dim':>5s} {'C2':>8s} {'m_min (M_KK)':>14s} {'m_max':>10s} {'m_min/m_min[0]':>16s}")
print("  " + "-" * 65)

m_lightest = sorted_results[0]['min_pos_eval'] if sorted_results[0]['min_pos_eval'] > 0 else 1e-10

for r in sorted_results:
    if r['min_pos_eval'] > 0:
        ratio = r['min_pos_eval'] / m_lightest
        pq_label = f"({r['p']},{r['q']})"
        print(f"  {pq_label:<8s} {r['dim_irrep']:5d} {r['C2']:8.2f} "
              f"{r['min_pos_eval']:14.6f} {r['max_eval']:10.4f} {ratio:16.2f}")

# Mass ratios between adjacent sectors
print("\n  Inter-sector mass ratios (consecutive lightest masses):")
masses = [r['min_pos_eval'] for r in sorted_results if r['min_pos_eval'] > 0]
labels = [f"({r['p']},{r['q']})" for r in sorted_results if r['min_pos_eval'] > 0]

for i in range(1, min(len(masses), 15)):
    ratio = masses[i] / masses[0]
    print(f"    {labels[i]:>8s} / {labels[0]:>8s} = {ratio:.4f}")

# Maximum mass ratio across all sectors
max_ratio = masses[-1] / masses[0] if len(masses) > 1 else 1.0
print(f"\n  Maximum mass ratio (heaviest/lightest): {max_ratio:.2f}")
print(f"  Lightest: {labels[0]} at {masses[0]:.6f} M_KK")
print(f"  Heaviest: {labels[-1]} at {masses[-1]:.6f} M_KK")

# PDG comparison
print("\n  PDG mass ratios for comparison:")
print(f"    m_t/m_u     = {172500/2.16:.0f}")
print(f"    m_b/m_d     = {4180/4.67:.0f}")
print(f"    m_tau/m_e   = {1776.86/0.511:.0f}")
print(f"    m_mu/m_e    = {105.66/0.511:.0f}")
print(f"    m_c/m_u     = {1270/2.16:.0f}")
print(f"    m_s/m_d     = {93.4/4.67:.0f}")

# Check: does the Casimir C2 correlate with mass?
print("\n  Casimir vs mass correlation:")
c2_vals = [r['C2'] for r in sorted_results if r['min_pos_eval'] > 0]
m_vals = [r['min_pos_eval'] for r in sorted_results if r['min_pos_eval'] > 0]
if len(c2_vals) > 2:
    corr = np.corrcoef(c2_vals, m_vals)[0, 1]
    print(f"    Pearson r(C2, m_min) = {corr:.4f}")

    # Fit: m = a * sqrt(C2) + b (Parthasarathy-type)
    from numpy.polynomial import polynomial as P
    sqrt_c2 = np.sqrt(c2_vals)
    coeffs = np.polyfit(sqrt_c2, m_vals, 1)
    print(f"    Linear fit: m_min = {coeffs[0]:.4f} * sqrt(C2) + {coeffs[1]:.4f}")
    residuals = np.array(m_vals) - np.polyval(coeffs, sqrt_c2)
    print(f"    Fit residual RMS: {np.sqrt(np.mean(residuals**2)):.6f}")

# =====================================================================
# SECTION 4: GATE VERDICT
# =====================================================================
print("\n" + "=" * 72)
print("SECTION 4: GATE VERDICT")
print("=" * 72)

if max_ratio > 100:
    verdict = "PASS"
    detail = f"Inter-sector mass ratio {max_ratio:.1f} > 100. PW tower generates hierarchy."
elif max_ratio > 10:
    verdict = "INFO"
    detail = f"Inter-sector mass ratio {max_ratio:.1f} in [10, 100]. Moderate hierarchy."
else:
    verdict = "FAIL"
    detail = f"Inter-sector mass ratio {max_ratio:.1f} < 10. Insufficient hierarchy."

print(f"  max inter-sector mass ratio: {max_ratio:.2f}")
print(f"  GATE YUKAWA-PW-TOWER-61: {verdict}")
print(f"  {detail}")

# =====================================================================
# SECTION 5: SAVE
# =====================================================================
print("\n" + "=" * 72)
print("SECTION 5: SAVE")
print("=" * 72)

save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          's61_yukawa_pw_tower.npz')

save_dict = {
    'gate_name': np.array(['YUKAWA-PW-TOWER-61']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([detail]),
    'tau_fold': tau_fold,
    'MAX_PQ_SUM': MAX_PQ_SUM,
    'n_sectors': len(results),
    'max_mass_ratio': max_ratio,
}

for i, r in enumerate(sorted_results):
    save_dict[f'sector_{i}_pq'] = np.array([r['p'], r['q']])
    save_dict[f'sector_{i}_C2'] = r['C2']
    save_dict[f'sector_{i}_dim'] = r['dim_irrep']
    save_dict[f'sector_{i}_min_mass'] = r['min_pos_eval']
    save_dict[f'sector_{i}_max_mass'] = r['max_eval']

np.savez(save_path, **save_dict)
print(f"  Saved: {save_path}")

# =====================================================================
# SECTION 6: PLOT
# =====================================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle(f'YUKAWA-PW-TOWER-61: Full PW Fermion Mass Spectrum\n'
             f'Gate: {verdict} (max ratio = {max_ratio:.1f})', fontsize=12, fontweight='bold')

# Panel 1: Mass vs Casimir
ax = axes[0]
c2_plot = [r['C2'] for r in results if r['min_pos_eval'] > 0]
m_plot = [r['min_pos_eval'] for r in results if r['min_pos_eval'] > 0]
labels_plot = [f"({r['p']},{r['q']})" for r in results if r['min_pos_eval'] > 0]
ax.scatter(c2_plot, m_plot, c='tab:blue', s=50, zorder=5)
for i, lbl in enumerate(labels_plot):
    ax.annotate(lbl, (c2_plot[i], m_plot[i]), fontsize=6, ha='left', va='bottom')
ax.set_xlabel('Casimir $C_2$', fontsize=11)
ax.set_ylabel('$m_{\\min}$ ($M_{\\mathrm{KK}}$)', fontsize=11)
ax.set_title('Lightest Mass per Sector')
ax.grid(True, alpha=0.3)

# Panel 2: Mass spectrum (all positive eigenvalues stacked)
ax = axes[1]
for r in sorted(results, key=lambda x: x['C2']):
    if r['min_pos_eval'] > 0:
        y = r['all_pos']
        x = np.full_like(y, r['C2'])
        ax.scatter(x, y, s=8, alpha=0.6)
ax.set_xlabel('Casimir $C_2$', fontsize=11)
ax.set_ylabel('Eigenvalue ($M_{\\mathrm{KK}}$)', fontsize=11)
ax.set_title('Full Positive Spectrum per Sector')
ax.grid(True, alpha=0.3)

# Panel 3: Mass ratio tower
ax = axes[2]
ratios = [m / masses[0] for m in masses[:20]]
sector_labels = labels[:20]
y_pos = range(len(ratios))
ax.barh(y_pos, ratios, color='tab:orange', alpha=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels(sector_labels, fontsize=7)
ax.set_xlabel('$m / m_{\\mathrm{lightest}}$', fontsize=11)
ax.set_title('Mass Hierarchy Tower')
ax.set_xscale('log')
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          's61_yukawa_pw_tower.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_path}")

print("\n" + "=" * 72)
print("COMPLETE")
print("=" * 72)
