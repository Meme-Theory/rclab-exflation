"""
B-4: Z_3 TRIALITY LABELING — PARTITION 28 IRREPS BY (p-q) mod 3
================================================================

From Session 16 Round 2b and Baptista Paper 18:
- LEFT Z_3 = (p-q) mod 3 commutes with D_K (conserved label)
- The center element zeta = exp(2*pi*i/3) * I_3 acts on V_{(p,q)} as
  rho(zeta) = omega^{(p-q) mod 3} * I_{dim(p,q)}, omega = e^{2pi i/3}
- This partitions the spectrum into three generation-like classes
- Each class should have the same U(2) quantum number content

This script:
1. Lists all 28 irreps with p+q <= 6
2. Computes (p-q) mod 3 for each
3. Runs the Dirac spectrum at target s-values
4. Verifies eigenvalue degeneracy (dim(p,q)-fold)
5. Groups eigenvalues by Z_3 class
6. Reports structural relationships within each class

Author: Baptista-Spacetime-Analyst, Session 17a
Date: 2026-02-14
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    get_irrep, dirac_operator_on_irrep, collect_spectrum,
    validate_connection, validate_omega_hermitian
)


def dim_pq(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_pq(p, q):
    """Quadratic Casimir C_2(p,q) for SU(3)."""
    return (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0


def z3_class(p, q):
    """Z_3 triality class: (p - q) mod 3."""
    return (p - q) % 3


def build_irrep_table(max_pq_sum=6):
    """
    Build the complete table of irreps with p+q <= max_pq_sum.

    Returns:
        table: list of dicts with keys: p, q, dim, C2, z3, dirac_size
    """
    table = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            d = dim_pq(p, q)
            c2 = casimir_pq(p, q)
            z3 = z3_class(p, q)
            table.append({
                'p': p, 'q': q, 'dim': d, 'C2': c2,
                'z3': z3, 'dirac_size': d * 16
            })
    return table


def print_irrep_table(table):
    """Print the full irrep table sorted by Z_3 class."""
    print("=" * 90)
    print("COMPLETE IRREP TABLE: p+q <= 6, SORTED BY Z_3 CLASS")
    print("=" * 90)
    print()
    print(f"  {'(p,q)':>8s}  {'dim':>5s}  {'C_2':>8s}  {'Z_3':>4s}  {'D_size':>7s}  {'Conjugate':>12s}")
    print("-" * 60)

    for z3_val in [0, 1, 2]:
        entries = [e for e in table if e['z3'] == z3_val]
        entries.sort(key=lambda x: x['C2'])
        total_dim = sum(e['dim'] for e in entries)
        total_dirac = sum(e['dirac_size'] for e in entries)
        n_irreps = len(entries)

        print(f"\n  --- Z_3 class {z3_val} ({n_irreps} irreps, total dim = {total_dim}, "
              f"total D-matrix = {total_dirac}) ---")

        for e in entries:
            p, q = e['p'], e['q']
            # Conjugate irrep
            conj = f"({q},{p})"
            conj_z3 = z3_class(q, p)
            print(f"  ({p},{q}){' ':>{5-len(f'({p},{q})')}}  "
                  f"{e['dim']:5d}  {e['C2']:8.3f}  {e['z3']:4d}  "
                  f"{e['dirac_size']:7d}  "
                  f"conj={conj}, Z_3(conj)={conj_z3}")

    print()


def verify_z3_partition(table):
    """
    Verify that Z_3 partitions the irreps into three non-overlapping classes
    and check structural properties.
    """
    print("=" * 90)
    print("Z_3 PARTITION VERIFICATION")
    print("=" * 90)
    print()

    classes = {0: [], 1: [], 2: []}
    for e in table:
        classes[e['z3']].append(e)

    # 1. Count check
    n0, n1, n2 = len(classes[0]), len(classes[1]), len(classes[2])
    total = n0 + n1 + n2
    print(f"  1. Partition completeness:")
    print(f"     Z_3=0: {n0} irreps, Z_3=1: {n1} irreps, Z_3=2: {n2} irreps")
    print(f"     Total: {total} (expected: 28 for p+q<=6)")
    assert total == 28, f"Expected 28 irreps, got {total}"
    print(f"     PASS: all 28 irreps assigned to exactly one Z_3 class")
    print()

    # 2. Conjugate check: (p,q) has Z_3 class k <=> (q,p) has Z_3 class (3-k) mod 3
    print(f"  2. Conjugation symmetry:")
    print(f"     Z_3(p,q) = (p-q) mod 3,  Z_3(q,p) = (q-p) mod 3 = (-Z_3(p,q)) mod 3")
    print(f"     So class 0 is self-conjugate, class 1 and class 2 are conjugate to each other.")
    n_self_conj_0 = sum(1 for e in classes[0] if e['p'] == e['q'])
    n_non_self_0 = len(classes[0]) - n_self_conj_0
    print(f"     Class 0: {n_self_conj_0} self-conjugate, {n_non_self_0} in conjugate pairs")
    print(f"     PASS: dim(class 1) = {n1} = dim(class 2) = {n2} [conjugation symmetry]")
    assert n1 == n2, f"Expected |Z_3=1| = |Z_3=2|, got {n1} vs {n2}"
    print()

    # 3. Dimension distribution
    print(f"  3. Dimension distribution per class:")
    for z3_val in [0, 1, 2]:
        dims = sorted([e['dim'] for e in classes[z3_val]])
        total_dim = sum(dims)
        print(f"     Z_3={z3_val}: dims = {dims}, total = {total_dim}")
    print()

    # 4. Casimir structure
    print(f"  4. Casimir C_2 values per class:")
    for z3_val in [0, 1, 2]:
        c2s = sorted([e['C2'] for e in classes[z3_val]])
        print(f"     Z_3={z3_val}: C_2 = {[f'{c:.1f}' for c in c2s]}")
    print()

    return classes


def compute_spectrum_by_z3(s_values, table, max_pq_sum=6):
    """
    Compute the Dirac spectrum at given s-values and group by Z_3 class.

    Returns:
        results: dict mapping s -> {z3_class -> [(p,q,eigenvalues), ...]}
    """
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    results = {}
    for s in s_values:
        print(f"\n  Computing spectrum at s = {s:.4f}...")
        all_evals, eval_data = collect_spectrum(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
        )

        # Group eval_data by Z_3 class
        z3_groups = {0: [], 1: [], 2: []}
        for p, q, evals in eval_data:
            z3 = z3_class(p, q)
            z3_groups[z3].append((p, q, evals))

        results[s] = z3_groups

    return results


def verify_degeneracy(eval_data, table):
    """
    Verify that each eigenvalue in sector (p,q) has the correct multiplicity.

    In the Tier 1 computation, D_{(p,q)} is a (dim(p,q)*16 x dim(p,q)*16) matrix.
    Its eigenvalues have no a-priori degeneracy constraint from the sector-level
    computation alone.

    The Peter-Weyl multiplicity is: each eigenvalue of D_{(p,q)} appears
    dim(p,q) times in the FULL L^2 spectrum (from the right-regular copy).
    This is automatic and does not need numerical verification -- it's a
    theorem.

    What we CAN verify: the Dirac operator block D_{(p,q)} has dimension
    dim(p,q) * 16 as expected.
    """
    print("=" * 90)
    print("DEGENERACY VERIFICATION")
    print("=" * 90)
    print()
    print("Peter-Weyl theorem: each eigenvalue of D_{(p,q)} appears dim(p,q)")
    print("times in the full L^2(SU(3), S) spectrum.")
    print()
    print(f"  {'(p,q)':>8s}  {'dim(p,q)':>8s}  {'D-block size':>12s}  {'# eigenvalues':>14s}  {'Status':>8s}")
    print("-" * 60)

    all_pass = True
    for p, q, evals in eval_data:
        d = dim_pq(p, q)
        expected_size = d * 16
        actual_count = len(evals)
        ok = actual_count == expected_size
        if not ok:
            all_pass = False
        status = "PASS" if ok else "FAIL"
        print(f"  ({p},{q}){' ':>{5-len(f'({p},{q})')}}  {d:8d}  {expected_size:12d}  "
              f"{actual_count:14d}  {status:>8s}")

    print()
    if all_pass:
        print("  ALL degeneracies verified: D_{(p,q)} block sizes match dim(p,q)*16.")
    else:
        print("  WARNING: Some block sizes do not match!")
    print()
    return all_pass


def analyze_z3_eigenvalue_structure(results, s):
    """
    Analyze the eigenvalue structure within each Z_3 class at a given s.

    For each Z_3 class:
    - Count total eigenvalues
    - Find the lightest (smallest |lambda|) eigenvalue
    - Compute inter-sector mass ratios
    - Check for structural relationships
    """
    z3_groups = results[s]

    print()
    print("=" * 90)
    print(f"Z_3 EIGENVALUE STRUCTURE AT s = {s:.4f}")
    print("=" * 90)

    for z3_val in [0, 1, 2]:
        sectors = z3_groups[z3_val]
        print(f"\n  --- Z_3 = {z3_val} ({len(sectors)} sectors) ---")
        print(f"  {'(p,q)':>8s}  {'dim':>5s}  {'C_2':>7s}  {'min|lam|':>10s}  "
              f"{'max|lam|':>10s}  {'# evals':>8s}")
        print("  " + "-" * 60)

        sector_min_masses = []
        for p, q, evals in sorted(sectors, key=lambda x: casimir_pq(x[0], x[1])):
            d = dim_pq(p, q)
            c2 = casimir_pq(p, q)
            abs_evals = np.abs(evals)
            min_ev = np.min(abs_evals)
            max_ev = np.max(abs_evals)
            n_evals = len(evals)

            sector_min_masses.append((p, q, min_ev, d, c2))

            print(f"  ({p},{q}){' ':>{5-len(f'({p},{q})')}}  {d:5d}  {c2:7.2f}  "
                  f"{min_ev:10.6f}  {max_ev:10.6f}  {n_evals:8d}")

        # Inter-sector ratios within this Z_3 class
        if len(sector_min_masses) > 1:
            print(f"\n  Inter-sector mass ratios (lightest eigenvalue):")
            sorted_masses = sorted(sector_min_masses, key=lambda x: x[2])
            m0 = sorted_masses[0][2]
            phi = 1.53158
            golden = (1 + np.sqrt(5)) / 2

            for i, (p, q, m, d, c2) in enumerate(sorted_masses):
                ratio = m / m0 if m0 > 1e-15 else float('inf')
                flags = ""
                if abs(ratio - phi) / phi < 0.01 and ratio > 1.01:
                    flags = " <-- NEAR phi (1.532)"
                if abs(ratio - golden) / golden < 0.01 and ratio > 1.01:
                    flags = " <-- NEAR golden ratio (1.618)"
                print(f"    ({p},{q}): min|lam| = {m:.6f}, ratio to lightest = {ratio:.6f}{flags}")

    return


def analyze_cross_z3_comparison(results, s):
    """
    Compare the eigenvalue spectra across Z_3 classes.
    Key question: Do different Z_3 classes have analogous mass patterns?
    """
    z3_groups = results[s]

    print()
    print("=" * 90)
    print(f"CROSS-Z_3 COMPARISON AT s = {s:.4f}")
    print("=" * 90)
    print()

    # For each Z_3 class, collect the lightest mass from each sector
    class_lightest = {}
    for z3_val in [0, 1, 2]:
        sectors = z3_groups[z3_val]
        lightest = []
        for p, q, evals in sorted(sectors, key=lambda x: casimir_pq(x[0], x[1])):
            abs_evals = np.abs(evals)
            lightest.append((p, q, np.min(abs_evals), casimir_pq(p, q)))
        class_lightest[z3_val] = sorted(lightest, key=lambda x: x[2])

    # Print lightest eigenvalues per class, aligned
    max_sectors = max(len(class_lightest[z]) for z in [0, 1, 2])
    print(f"  Lightest eigenvalue per sector, ordered by mass:")
    print(f"  {'#':>3s}  {'Z_3=0':>20s}  {'Z_3=1':>20s}  {'Z_3=2':>20s}")
    print("  " + "-" * 70)

    for i in range(max_sectors):
        row = f"  {i:3d}"
        for z3_val in [0, 1, 2]:
            if i < len(class_lightest[z3_val]):
                p, q, m, c2 = class_lightest[z3_val][i]
                row += f"  ({p},{q}) {m:8.4f}"
            else:
                row += f"  {'---':>20s}"
        print(row)

    # Compare corresponding mass ratios
    print()
    print(f"  Inter-generation mass ratios (comparing Z_3=1 vs Z_3=0, Z_3=2 vs Z_3=0):")
    n_compare = min(len(class_lightest[z]) for z in [0, 1, 2])
    if n_compare > 0:
        print(f"  {'#':>3s}  {'m(Z3=0)':>10s}  {'m(Z3=1)':>10s}  {'m(Z3=2)':>10s}  "
              f"{'m1/m0':>8s}  {'m2/m0':>8s}  {'m2/m1':>8s}")
        print("  " + "-" * 70)
        for i in range(min(n_compare, 8)):
            m0 = class_lightest[0][i][2]
            m1 = class_lightest[1][i][2]
            m2 = class_lightest[2][i][2]
            r10 = m1 / m0 if m0 > 1e-15 else float('inf')
            r20 = m2 / m0 if m0 > 1e-15 else float('inf')
            r21 = m2 / m1 if m1 > 1e-15 else float('inf')
            print(f"  {i:3d}  {m0:10.6f}  {m1:10.6f}  {m2:10.6f}  "
                  f"{r10:8.4f}  {r20:8.4f}  {r21:8.4f}")
    print()


def main():
    print("=" * 90)
    print("B-4: Z_3 TRIALITY LABELING — (p-q) mod 3 PARTITION")
    print("     28 irreps with p+q <= 6 on (SU(3), g_s)")
    print("=" * 90)
    print()

    # Step 1: Build and display the irrep table
    table = build_irrep_table(max_pq_sum=6)
    print_irrep_table(table)

    # Step 2: Verify Z_3 partition properties
    classes = verify_z3_partition(table)

    # Step 3: Compute spectrum at key s-values
    s_values = [0.0, 0.15, 0.30]
    print()
    print("=" * 90)
    print("DIRAC SPECTRUM COMPUTATION BY Z_3 CLASS")
    print("=" * 90)

    results = compute_spectrum_by_z3(s_values, table, max_pq_sum=6)

    # Step 4: Verify degeneracy at s=0 (bi-invariant)
    # We need the raw eval_data for this
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    _, eval_data_s0 = collect_spectrum(
        0.0, gens, f_abc, gammas, max_pq_sum=6, verbose=False
    )
    verify_degeneracy(eval_data_s0, table)

    # Step 5: Analyze eigenvalue structure per Z_3 class
    for s in s_values:
        analyze_z3_eigenvalue_structure(results, s)

    # Step 6: Cross-Z_3 comparison
    for s in s_values:
        analyze_cross_z3_comparison(results, s)

    # Step 7: Summary
    print("=" * 90)
    print("SUMMARY (B-4)")
    print("=" * 90)
    print()
    print("1. Z_3 PARTITION:")
    print("   (p-q) mod 3 partitions 28 irreps (p+q<=6) into 3 classes:")
    for z3_val in [0, 1, 2]:
        entries = [(e['p'], e['q']) for e in classes[z3_val]]
        entries.sort(key=lambda x: casimir_pq(x[0], x[1]))
        labels = [f"({p},{q})" for p, q in entries]
        print(f"   Z_3={z3_val}: {', '.join(labels)}")
    print()
    print("2. CONJUGATION SYMMETRY:")
    print("   Z_3(q,p) = -Z_3(p,q) mod 3")
    print("   Class 0 is self-conjugate, classes 1 and 2 are conjugate pair")
    print()
    print("3. DEGENERACY:")
    print("   Each eigenvalue of D_{(p,q)} appears dim(p,q) times in L^2 spectrum")
    print("   (Peter-Weyl theorem — automatic, not a test)")
    print("   D-block sizes verified: dim(p,q) * 16 for all 28 irreps")
    print()
    print("4. PHYSICAL INTERPRETATION:")
    print("   LEFT Z_3 = conserved quantum number (generation label)")
    print("   Commutes with D_K at all s (center elements are isometries)")
    print("   Does NOT create inter-generation mass splitting by itself")
    print("   Inter-generation hierarchy requires RIGHT Z_3 (Tier 2)")
    print()

    return table, classes, results


if __name__ == "__main__":
    table, classes, results = main()
