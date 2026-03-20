"""
FEYNMAN PREDICTIONS SESSION: Compute quantitative predictions
=============================================================

Computes specific numerical predictions from the proven results of Session 17,
evaluated at the experimentally-indicated s_W = 0.2994 and at the
Boltzmann V_eff candidate s_0 = 0.164.

Predictions computed:
1. Gauge coupling ratios at s_W (all three)
2. Sector-specific mass ratios at s_W
3. Species count at s_W
4. W/Z mass ratio from C^2 boson masses
5. Spectral asymmetry / generation structure

Author: Feynman-Theorist Agent (Session 18)
Date: 2026-02-15
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, validate_clifford,
    get_irrep, dirac_operator_on_irrep, collect_spectrum,
)
from tier1_spectral_action import (
    dim_su3_irrep, scalar_curvature_analytical,
    gauge_boson_masses_baptista,
)

t_start = time.time()

print("=" * 80)
print("FEYNMAN PREDICTIONS SESSION: Quantitative Computations")
print("=" * 80)

# Initialize infrastructure
gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()
cliff_err = validate_clifford(gammas)
assert cliff_err < 1e-14

MAX_PQ = 6
s_W = 0.2994   # from sin^2(theta_W)
s_H1 = 0.164   # from Boltzmann V_eff (unconverged)

# =========================================================================
# PREDICTION 1: Gauge coupling ratios
# =========================================================================
print("\n" + "=" * 80)
print("PREDICTION 1: GAUGE COUPLING RATIOS")
print("=" * 80)

# Measured SM values (PDG at M_Z)
sin2_tW_meas = 0.23121
alpha_em_MZ = 1.0 / 127.951
alpha_s_MZ = 0.1179
alpha_1_MZ = alpha_em_MZ / (1.0 - sin2_tW_meas)
alpha_2_MZ = alpha_em_MZ / sin2_tW_meas
g1_g2_meas = np.sqrt(alpha_1_MZ / alpha_2_MZ)
g1_g3_meas = np.sqrt(alpha_1_MZ / alpha_s_MZ)
g2_g3_meas = np.sqrt(alpha_2_MZ / alpha_s_MZ)

for s_val, label in [(s_W, "s_W=0.2994"), (s_H1, "s_H1=0.164")]:
    g12 = np.exp(-2 * s_val)
    g13 = np.exp(-s_val)
    g23 = np.exp(s_val)
    s2tw = g12**2 / (1.0 + g12**2)

    print(f"\n  At {label}:")
    print(f"    g_1/g_2 = e^{{-2s}} = {g12:.6f}  (measured: {g1_g2_meas:.6f}, delta = {(g12-g1_g2_meas)/g1_g2_meas:+.2%})")
    print(f"    g_1/g_3 = e^{{-s}}  = {g13:.6f}  (measured: {g1_g3_meas:.6f}, delta = {(g13-g1_g3_meas)/g1_g3_meas:+.2%})")
    print(f"    g_2/g_3 = e^{{s}}   = {g23:.6f}  (measured: {g2_g3_meas:.6f}, delta = {(g23-g2_g3_meas)/g2_g3_meas:+.2%})")
    print(f"    sin^2(theta_W) = {s2tw:.6f}  (measured: {sin2_tW_meas}, delta = {(s2tw-sin2_tW_meas)/sin2_tW_meas:+.2%})")

# =========================================================================
# PREDICTION 2: Sector-specific mass ratios at s_W
# =========================================================================
print("\n" + "=" * 80)
print("PREDICTION 2: SECTOR-SPECIFIC MASS RATIOS")
print("=" * 80)

for s_val, label in [(s_W, "s_W=0.2994"), (s_H1, "s_H1=0.164"), (0.15, "s=0.15")]:
    print(f"\n  Computing spectrum at {label}...")
    all_evals, eval_data = collect_spectrum(s_val, gens, f_abc, gammas,
                                             max_pq_sum=MAX_PQ, verbose=False)

    # Extract lowest positive eigenvalue per sector
    sector_min = {}
    sector_all = {}
    for p, q, evals in eval_data:
        pos_evals = sorted([abs(e) for e in evals if abs(e) > 1e-10])
        if pos_evals:
            sector_min[(p, q)] = pos_evals[0]
            sector_all[(p, q)] = pos_evals

    print(f"\n  Lowest eigenvalue per sector at {label}:")
    for (p, q) in sorted(sector_min.keys(), key=lambda x: sector_min[x]):
        dim = dim_su3_irrep(p, q)
        z3 = (p - q) % 3
        print(f"    ({p},{q}) [dim={dim:3d}, Z3={z3}]: lambda_min = {sector_min[(p,q)]:.8f}")

    # Compute phi_paasch-relevant ratios
    print(f"\n  Key mass ratios at {label}:")
    phi_paasch = 1.53158  # Paasch constant, from x = e^{-x^2}; NOT the golden ratio (1.618)

    # Ratio between specific sectors
    interesting_pairs = [
        ((3,0), (0,0)), ((3,0), (2,0)), ((1,0), (0,0)),
        ((2,1), (1,0)), ((0,1), (0,0)), ((1,1), (0,0)),
    ]
    for (p1,q1), (p2,q2) in interesting_pairs:
        if (p1,q1) in sector_min and (p2,q2) in sector_min:
            r = sector_min[(p1,q1)] / sector_min[(p2,q2)]
            d_phi = abs(r - phi_paasch) / phi_paasch * 100
            print(f"    m({p1},{q1})/m({p2},{q2}) = {r:.8f}  (phi_paasch = {phi_paasch:.8f}, delta = {d_phi:.4f}%)")

# =========================================================================
# PREDICTION 3: Species count at s_W
# =========================================================================
print("\n" + "=" * 80)
print("PREDICTION 3: SPECIES COUNT")
print("=" * 80)

for s_val, label in [(s_W, "s_W=0.2994"), (s_H1, "s_H1=0.164")]:
    all_evals, eval_data = collect_spectrum(s_val, gens, f_abc, gammas,
                                             max_pq_sum=MAX_PQ, verbose=False)

    for cutoff in [0.5, 1.0, 1.23, 2.0]:
        n_pos = 0
        n_mult = 0
        for ev, mult in all_evals:
            val = abs(ev)
            if val < 1e-14:
                continue
            if val <= cutoff and (ev.imag > 0 or (abs(ev.imag) < 1e-14 and ev.real > 0)):
                n_pos += 1
                n_mult += mult
        n_tot = 2 * n_mult
        print(f"  {label}, Lambda={cutoff:.2f}: N_species={n_tot} (SM fermionic DOF=90, ratio={n_tot/90:.2f})")

# =========================================================================
# PREDICTION 4: W/Z mass ratio from C^2 gauge boson masses
# =========================================================================
print("\n" + "=" * 80)
print("PREDICTION 4: GAUGE BOSON MASS STRUCTURE")
print("=" * 80)

for s_val, label in [(s_W, "s_W=0.2994"), (s_H1, "s_H1=0.164")]:
    m2_vals = gauge_boson_masses_baptista(0.0, s_val)  # sigma=0, Jensen param s

    print(f"\n  C^2 gauge boson masses^2 at {label}:")
    for i, m2 in enumerate(m2_vals):
        print(f"    m^2_{i} = {m2:.8f}  (m = {np.sqrt(abs(m2)):.8f})")

    # The C^2 bosons should give W/Z structure
    if len(m2_vals) >= 2:
        unique_m2 = sorted(set(np.round(m2_vals, 8)))
        if len(unique_m2) >= 2:
            ratio = np.sqrt(unique_m2[1] / unique_m2[0]) if unique_m2[0] > 0 else float('inf')
            print(f"    Mass ratio (if distinct): {ratio:.6f}")
            print(f"    SM M_W/M_Z = {80.379/91.188:.6f}")

# =========================================================================
# PREDICTION 5: Z_3 generation structure
# =========================================================================
print("\n" + "=" * 80)
print("PREDICTION 5: Z_3 GENERATION STRUCTURE")
print("=" * 80)

for s_val, label in [(s_W, "s_W=0.2994")]:
    all_evals, eval_data = collect_spectrum(s_val, gens, f_abc, gammas,
                                             max_pq_sum=MAX_PQ, verbose=False)

    # Group by Z_3
    z3_evals = {0: [], 1: [], 2: []}
    for p, q, evals in eval_data:
        z3 = (p - q) % 3
        dim = dim_su3_irrep(p, q)
        pos_evals = sorted([abs(e) for e in evals if abs(e) > 1e-10])
        for e in pos_evals:
            z3_evals[z3].append((e, dim, p, q))

    for z3_val in [0, 1, 2]:
        entries = sorted(z3_evals[z3_val], key=lambda x: x[0])
        n = len(entries)
        sectors = set((p, q) for _, _, p, q in entries)
        print(f"\n  Z_3 = {z3_val}: {n} distinct eigenvalues from {len(sectors)} sectors")
        # Show 5 lowest
        for e, dim, p, q in entries[:5]:
            print(f"    lambda = {e:.8f}  from ({p},{q}) [dim={dim}]")

    # Inter-generation mass ratios: Z3=1 vs Z3=2 (should be conjugate-degenerate)
    print("\n  Z_3=1 vs Z_3=2 degeneracy check (conjugate sectors):")
    z1_sorted = sorted(z3_evals[1], key=lambda x: x[0])
    z2_sorted = sorted(z3_evals[2], key=lambda x: x[0])
    n_check = min(10, len(z1_sorted), len(z2_sorted))
    max_diff = 0
    for i in range(n_check):
        diff = abs(z1_sorted[i][0] - z2_sorted[i][0])
        max_diff = max(max_diff, diff)
        print(f"    Level {i}: Z3=1 lambda={z1_sorted[i][0]:.8f} ({z1_sorted[i][2]},{z1_sorted[i][3]}), "
              f"Z3=2 lambda={z2_sorted[i][0]:.8f} ({z2_sorted[i][2]},{z2_sorted[i][3]}), "
              f"diff={diff:.2e}")
    print(f"  Max degeneracy breaking: {max_diff:.2e}")

# =========================================================================
# PREDICTION 6: Scalar curvature and cosmological constant
# =========================================================================
print("\n" + "=" * 80)
print("PREDICTION 6: SCALAR CURVATURE R(s) AND VACUUM ENERGY")
print("=" * 80)

for s_val, label in [(0.0, "s=0"), (s_H1, "s_H1=0.164"), (s_W, "s_W=0.2994"), (0.5, "s=0.5")]:
    R_s = scalar_curvature_analytical(s_val)
    # V_tree = -(R(s)/R(0)) * Vol, normalized
    R_0 = scalar_curvature_analytical(0.0)
    v_tree = -R_s  # proportional, Vol is constant
    print(f"  {label}: R(s) = {R_s:.8f}, R(s)/R(0) = {R_s/R_0:.8f}")

# =========================================================================
# SUMMARY
# =========================================================================
print("\n" + "=" * 80)
print("COMPUTATION COMPLETE")
print(f"Total time: {time.time() - t_start:.1f}s")
print("=" * 80)
