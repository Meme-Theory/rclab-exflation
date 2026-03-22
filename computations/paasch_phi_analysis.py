"""
PAASCH PHI STRUCTURE ANALYSIS
==============================

Analyzes whether the Dirac spectrum on (SU(3), g_s) with Jensen deformation
produces the RIGHT KIND of phi for Paasch's mass quantization framework.

Paasch requires:
  1. m_n = m_0 * phi^n for INTEGER n (not just one ratio = phi)
  2. Six mass sequences S1-S6 separated by 45 degrees in the log spiral
  3. Golden ratio in M-value ratios: M(i+1)/[2M(i)] -> 0.618034
  4. phi = 1.53158 from transcendental equation x = e^(-x^2)

This script extracts sector-minimum eigenvalues at s=0.15 and tests:
  - Are ALL inter-sector ratios powers of phi?
  - Do we see phi^1, phi^2, phi^3, phi^4, etc.?
  - Is the golden ratio present in the spectrum?
  - Do 6 sectors map to Paasch's 6 sequences?

Author: Paasch Mass Quantization Analyst (Session 13)
Date: 2026-02-12
"""

import numpy as np
import sys
import os

# Add tier0-computation to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, get_irrep,
    dirac_operator_on_irrep
)

# Constants
PHI_PAASCH = 1.53158     # Paasch quantization factor
GOLDEN = (1 + np.sqrt(5)) / 2  # 1.61803...

def compute_sector_eigenvalues(s, gens, f_abc, gammas, max_pq_sum=3):
    """
    Compute eigenvalues per sector and return sector-minimum |eigenvalue|.

    Returns:
        sector_data: dict mapping (p,q) -> {
            'all_evals': all eigenvalue absolute values,
            'min_eval': minimum positive |eigenvalue|,
            'max_eval': maximum |eigenvalue|,
        }
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    sector_data = {}

    # Trivial irrep
    D_trivial = Omega.copy()
    evals_trivial = np.abs(np.linalg.eigvals(D_trivial))
    evals_trivial = evals_trivial[evals_trivial > 1e-10]
    evals_trivial = np.sort(np.unique(np.round(evals_trivial, 10)))
    sector_data[(0,0)] = {
        'all_evals': evals_trivial,
        'min_eval': evals_trivial[0] if len(evals_trivial) > 0 else None,
        'max_eval': evals_trivial[-1] if len(evals_trivial) > 0 else None,
    }

    # Non-trivial irreps
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            if p == 0 and q == 0:
                continue
            try:
                rho, dim_rho = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals = np.abs(np.linalg.eigvals(D_pi))
                evals = evals[evals > 1e-10]
                evals = np.sort(np.unique(np.round(evals, 10)))
                sector_data[(p,q)] = {
                    'all_evals': evals,
                    'min_eval': evals[0] if len(evals) > 0 else None,
                    'max_eval': evals[-1] if len(evals) > 0 else None,
                }
            except Exception as e:
                print(f"  Warning: ({p},{q}) failed: {e}")

    return sector_data


def phi_power_test(ratio, max_power=8):
    """
    Test if a ratio is close to phi^n for any integer n from -max_power to +max_power.
    Returns (best_n, phi^n, relative_error).
    """
    best_n = None
    best_err = float('inf')
    for n in range(-max_power, max_power+1):
        if n == 0:
            continue
        target = PHI_PAASCH ** n
        err = abs(ratio - target) / target
        if err < best_err:
            best_err = err
            best_n = n
    return best_n, PHI_PAASCH ** best_n, best_err


def main():
    print("=" * 80)
    print("PAASCH PHI STRUCTURE ANALYSIS")
    print("=" * 80)

    # Build infrastructure
    print("\n[1] Building su(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # ================================================================
    # PART A: Sector-specific eigenvalues at s=0.15
    # ================================================================
    s_test = 0.15
    print(f"\n[2] Computing sector eigenvalues at s={s_test}...")
    sector_data = compute_sector_eigenvalues(s_test, gens, f_abc, gammas)

    # Print sector minima
    print(f"\n  SECTOR MINIMUM EIGENVALUES at s={s_test}:")
    print(f"  {'Sector':>10} {'dim':>5} {'min|lambda|':>12} {'max|lambda|':>12} {'#distinct':>10}")
    print(f"  {'-'*55}")

    sector_labels = []
    sector_mins = []
    for (p,q), data in sorted(sector_data.items()):
        dim_pq = (p+1)*(q+1)*(p+q+2)//2
        n_distinct = len(data['all_evals'])
        m = data['min_eval']
        M = data['max_eval']
        print(f"  ({p},{q}){'':<5} {dim_pq:5d} {m:12.6f} {M:12.6f} {n_distinct:10d}")
        sector_labels.append((p,q))
        sector_mins.append(m)

    sector_mins = np.array(sector_mins)

    # ================================================================
    # PART B: All inter-sector minimum eigenvalue ratios
    # ================================================================
    print(f"\n[3] INTER-SECTOR MINIMUM EIGENVALUE RATIOS:")
    print(f"  Testing if ratio = phi^n for integer n")
    print(f"  phi = {PHI_PAASCH}, phi^2 = {PHI_PAASCH**2:.5f}, phi^3 = {PHI_PAASCH**3:.5f}")
    print(f"  phi^4 = {PHI_PAASCH**4:.5f}, phi^5 = {PHI_PAASCH**5:.5f}")
    print()

    n_sectors = len(sector_labels)
    # Sort sectors by min eigenvalue
    sorted_idx = np.argsort(sector_mins)

    print(f"  Sectors ordered by min eigenvalue:")
    for rank, idx in enumerate(sorted_idx):
        p, q = sector_labels[idx]
        print(f"    Rank {rank}: ({p},{q}) -> min|lambda| = {sector_mins[idx]:.6f}")

    print(f"\n  ALL PAIRWISE RATIOS (larger/smaller):")
    print(f"  {'Sector A':>10} {'Sector B':>10} {'Ratio':>10} {'Best n':>7} {'phi^n':>10} {'Rel Err':>10} {'Match?':>8}")
    print(f"  {'-'*70}")

    phi_power_hits = []
    all_ratios = []

    for i in range(n_sectors):
        for j in range(i+1, n_sectors):
            if sector_mins[i] > 1e-10 and sector_mins[j] > 1e-10:
                ratio = max(sector_mins[i], sector_mins[j]) / min(sector_mins[i], sector_mins[j])
                best_n, phi_n, rel_err = phi_power_test(ratio)
                match = "YES" if rel_err < 0.01 else ("close" if rel_err < 0.03 else "no")
                pi, qi = sector_labels[i]
                pj, qj = sector_labels[j]

                # Ensure ratio > 1
                if sector_mins[j] >= sector_mins[i]:
                    sa, sb = f"({pj},{qj})", f"({pi},{qi})"
                else:
                    sa, sb = f"({pi},{qi})", f"({pj},{qj})"

                print(f"  {sa:>10}/{sb:<10} {ratio:10.6f} {best_n:7d} {phi_n:10.6f} {rel_err:10.6f} {match:>8}")
                all_ratios.append((pi, qi, pj, qj, ratio, best_n, rel_err))
                if rel_err < 0.01:
                    phi_power_hits.append((pi, qi, pj, qj, ratio, best_n, rel_err))

    print(f"\n  PHI-POWER MATCHES (< 1% error): {len(phi_power_hits)} / {len(all_ratios)}")
    for pi, qi, pj, qj, ratio, n, err in phi_power_hits:
        print(f"    ({pi},{qi})/({pj},{qj}) = {ratio:.6f} ~ phi^{n} = {PHI_PAASCH**n:.6f} (err {err*100:.4f}%)")

    # ================================================================
    # PART C: Conjugate pair analysis
    # ================================================================
    print(f"\n[4] CONJUGATE PAIR ANALYSIS:")
    print(f"  (p,q) and (q,p) should give identical eigenvalues")
    conj_pairs = [(1,0,0,1), (2,0,0,2), (3,0,0,3), (2,1,1,2)]
    for p1, q1, p2, q2 in conj_pairs:
        if (p1,q1) in sector_data and (p2,q2) in sector_data:
            m1 = sector_data[(p1,q1)]['min_eval']
            m2 = sector_data[(p2,q2)]['min_eval']
            diff = abs(m1 - m2) / m1 if m1 > 0 else 0
            print(f"  ({p1},{q1}) min={m1:.6f}, ({p2},{q2}) min={m2:.6f}, rel_diff={diff:.2e}")

    # ================================================================
    # PART D: Logarithmic spacing test (Paasch's key prediction)
    # ================================================================
    print(f"\n[5] LOGARITHMIC SPACING TEST (Paasch's key prediction):")
    print(f"  If masses follow m_n = m_0 * phi^n, then log(m_n)/log(phi) = log(m_0)/log(phi) + n")
    print(f"  i.e., log_phi(m_n) should be near-integer-spaced")
    print()

    log_phi = np.log(PHI_PAASCH)

    # Use unique sector minima (merge conjugate pairs)
    unique_sectors = {}
    for (p,q), data in sector_data.items():
        key = (min(p,q), max(p,q)) if p != q else (p,q)
        if key not in unique_sectors:
            unique_sectors[key] = data['min_eval']

    print(f"  Unique sector types (merging conjugates):")
    for key in sorted(unique_sectors.keys()):
        m = unique_sectors[key]
        log_m = np.log(m) / log_phi
        print(f"    {str(key):>10}: min|lambda| = {m:.6f}, log_phi(lambda) = {log_m:.4f}")

    # Assign mass numbers relative to (0,0)
    m0 = unique_sectors.get((0,0), None)
    if m0:
        print(f"\n  MASS NUMBERS relative to (0,0) [m_0 = {m0:.6f}]:")
        print(f"  If ratio = phi^N, then N is the mass number difference")
        for key in sorted(unique_sectors.keys()):
            m = unique_sectors[key]
            ratio = m / m0
            best_n, phi_n, rel_err = phi_power_test(ratio)
            print(f"    {str(key):>10}: m/m_0 = {ratio:.6f}, best N = {best_n}, "
                  f"phi^N = {phi_n:.6f}, err = {rel_err*100:.4f}%")

    # ================================================================
    # PART E: Higher powers of phi test
    # ================================================================
    print(f"\n[6] HIGHER POWERS OF PHI TEST:")
    print(f"  Checking if phi^2 = {PHI_PAASCH**2:.5f}, phi^3 = {PHI_PAASCH**3:.5f}, "
          f"phi^4 = {PHI_PAASCH**4:.5f} appear in sector minimum ratios")

    # Collect ALL sector minimum eigenvalues (not just unique)
    all_mins = []
    for (p,q), data in sorted(sector_data.items()):
        all_mins.append(((p,q), data['min_eval']))

    for target_power in [1, 2, 3, 4, 5]:
        target = PHI_PAASCH ** target_power
        print(f"\n  phi^{target_power} = {target:.6f}:")
        found = False
        for i, ((p1,q1), m1) in enumerate(all_mins):
            for j, ((p2,q2), m2) in enumerate(all_mins):
                if m2 > m1 and m1 > 1e-10:
                    ratio = m2 / m1
                    err = abs(ratio - target) / target
                    if err < 0.01:
                        print(f"    ({p2},{q2})/({p1},{q1}) = {ratio:.6f} (err {err*100:.4f}%)")
                        found = True
        if not found:
            print(f"    No pairs within 1%")

    # ================================================================
    # PART F: Golden ratio in the spectrum
    # ================================================================
    print(f"\n[7] GOLDEN RATIO TEST:")
    print(f"  golden = {GOLDEN:.6f}")

    for i, ((p1,q1), m1) in enumerate(all_mins):
        for j, ((p2,q2), m2) in enumerate(all_mins):
            if m2 > m1 and m1 > 1e-10:
                ratio = m2 / m1
                err = abs(ratio - GOLDEN) / GOLDEN
                if err < 0.01:
                    print(f"    ({p2},{q2})/({p1},{q1}) = {ratio:.6f} (err {err*100:.4f}%)")

    # ================================================================
    # PART G: s-sweep of sector-specific ratios
    # ================================================================
    print(f"\n[8] s-SWEEP OF SECTOR-SPECIFIC RATIOS:")
    print(f"  Tracking m_{{(3,0)}}/m_{{(0,0)}} and other key ratios vs s")

    s_values = np.linspace(0.0, 0.5, 51)

    print(f"\n  {'s':>6} {'m(0,0)':>10} {'m(1,0)':>10} {'m(1,1)':>10} {'m(2,0)':>10} "
          f"{'m(3,0)':>10} {'m(2,1)':>10} {'(3,0)/(0,0)':>12} {'(1,0)/(0,0)':>12}")
    print(f"  {'-'*105}")

    best_phi_match = {'s': None, 'err': float('inf'), 'ratio': None}
    ratio_curves = {k: [] for k in ['30_00', '10_00', '11_00', '20_00', '21_00']}

    for s in s_values:
        sd = compute_sector_eigenvalues(s, gens, f_abc, gammas)

        m00 = sd.get((0,0), {}).get('min_eval', None)
        m10 = sd.get((1,0), {}).get('min_eval', None)
        m11 = sd.get((1,1), {}).get('min_eval', None)
        m20 = sd.get((2,0), {}).get('min_eval', None)
        m30 = sd.get((3,0), {}).get('min_eval', None)
        m21 = sd.get((2,1), {}).get('min_eval', None)

        r30 = m30/m00 if (m00 and m30 and m00 > 1e-10) else None
        r10 = m10/m00 if (m00 and m10 and m00 > 1e-10) else None

        r30_str = f"{r30:.6f}" if r30 else "N/A"
        r10_str = f"{r10:.6f}" if r10 else "N/A"

        print(f"  {s:6.3f} {m00:10.6f} {m10:10.6f} {m11:10.6f} {m20:10.6f} "
              f"{m30:10.6f} {m21:10.6f} {r30_str:>12} {r10_str:>12}")

        if r30:
            err = abs(r30 - PHI_PAASCH) / PHI_PAASCH
            if err < best_phi_match['err']:
                best_phi_match = {'s': s, 'err': err, 'ratio': r30}

        # Store ratios
        if m00 and m00 > 1e-10:
            for label, mx in [('30_00', m30), ('10_00', m10), ('11_00', m11),
                              ('20_00', m20), ('21_00', m21)]:
                if mx:
                    ratio_curves[label].append((s, mx/m00))

    print(f"\n  BEST m(3,0)/m(0,0) match to phi:")
    print(f"    s = {best_phi_match['s']:.4f}")
    print(f"    ratio = {best_phi_match['ratio']:.8f}")
    print(f"    phi = {PHI_PAASCH:.8f}")
    print(f"    error = {best_phi_match['err']*100:.6f}%")

    # ================================================================
    # PART H: At the best-fit s, check ALL ratios for phi^n
    # ================================================================
    s_best = best_phi_match['s']
    print(f"\n[9] FULL RATIO TABLE AT s={s_best:.4f}:")
    sd_best = compute_sector_eigenvalues(s_best, gens, f_abc, gammas)

    m00 = sd_best[(0,0)]['min_eval']
    print(f"  Reference: m(0,0) = {m00:.8f}")
    print(f"  {'Sector':>10} {'m/m(0,0)':>12} {'Best n':>8} {'phi^n':>12} {'Rel Err':>10} {'log_phi':>10}")
    print(f"  {'-'*68}")

    unique_best = {}
    for (p,q), data in sd_best.items():
        key = (min(p,q), max(p,q)) if p != q else (p,q)
        if key not in unique_best:
            unique_best[key] = data['min_eval']

    for key in sorted(unique_best.keys()):
        m = unique_best[key]
        if key == (0,0):
            print(f"  {str(key):>10} {1.0:12.6f} {'0':>8} {'1.000000':>12} {'0.0000':>10} {'0.0000':>10}")
            continue
        ratio = m / m00
        best_n, phi_n, rel_err = phi_power_test(ratio)
        log_phi_val = np.log(ratio) / np.log(PHI_PAASCH)
        print(f"  {str(key):>10} {ratio:12.6f} {best_n:8d} {phi_n:12.6f} {rel_err*100:9.4f}% {log_phi_val:10.4f}")

    # ================================================================
    # PART I: Six sectors vs six sequences
    # ================================================================
    print(f"\n[10] SIX SECTORS vs SIX SEQUENCES:")
    print(f"  Paasch's 6 sequences S1-S6 at angles: 0, 45, 132, 182, 225, 317 degrees")
    print(f"  SU(3) has 6 sector types: (0,0), (1,0)/(0,1), (1,1), (2,0)/(0,2), (3,0)/(0,3), (2,1)/(1,2)")
    print(f"  Count match: {'YES' if len(unique_best) == 6 else 'NO'} ({len(unique_best)} unique sectors)")

    # Compute angles from log spiral
    if m00 > 0:
        k = np.log(PHI_PAASCH) / (2 * np.pi)
        print(f"\n  Spiral constant k = ln(phi)/(2*pi) = {k:.6f}")
        print(f"  For each sector, angle = ln(m/m_0) / k (mod 360):")

        for key in sorted(unique_best.keys()):
            m = unique_best[key]
            if m / m00 > 1e-10 and key != (0,0):
                angle = np.log(m / m00) / k
                angle_mod = angle % 360
                print(f"    {str(key):>10}: angle = {angle:.1f} deg (mod 360: {angle_mod:.1f} deg)")

    # ================================================================
    # PART J: Exponential structure connection
    # ================================================================
    print(f"\n[11] EXPONENTIAL STRUCTURE CONNECTION:")
    print(f"  Jensen deformation: e^{{2s}} (u(1)), e^{{-2s}} (su(2)), e^{{s}} (C^2)")
    print(f"  Paasch phi from: x = e^{{-x^2}}, phi = 1/x")
    print(f"  At s=0.15: e^{{2s}} = {np.exp(0.3):.6f}, e^{{-2s}} = {np.exp(-0.3):.6f}, e^{{s}} = {np.exp(0.15):.6f}")
    print(f"  At s=1.14: e^{{2s}} = {np.exp(2.28):.6f}, e^{{-2s}} = {np.exp(-2.28):.6f}, e^{{s}} = {np.exp(1.14):.6f}")

    # Check if phi appears in Jensen exponential ratios
    print(f"\n  Ratios of Jensen scale factors:")
    for s_val in [0.15, 1.14]:
        e2s = np.exp(2*s_val)
        em2s = np.exp(-2*s_val)
        es = np.exp(s_val)
        print(f"  s={s_val}: e^2s/e^s = {e2s/es:.6f}, e^s/e^-2s = {es/em2s:.6f}, e^2s/e^-2s = {e2s/em2s:.6f}")
        for name, val in [('e^2s/e^s', e2s/es), ('e^s/e^-2s', es/em2s), ('e^2s/e^-2s', e2s/em2s)]:
            best_n, phi_n, err = phi_power_test(val)
            if err < 0.05:
                print(f"    {name} = {val:.6f} ~ phi^{best_n} = {phi_n:.6f} (err {err*100:.2f}%)")

    # Check Paasch's transcendental equation
    x_paasch = 1.0 / PHI_PAASCH  # x = 1/phi
    print(f"\n  Paasch transcendental equation: x = e^(-x^2)")
    print(f"  x = 1/phi = {x_paasch:.6f}")
    print(f"  e^(-x^2) = {np.exp(-x_paasch**2):.6f}")
    print(f"  Match: {abs(x_paasch - np.exp(-x_paasch**2)):.2e}")

    # Is there a Jensen s where phi emerges from the deformation structure?
    # phi = e^s for some s?
    s_phi = np.log(PHI_PAASCH)
    print(f"\n  phi = e^s at s = ln(phi) = {s_phi:.6f}")
    print(f"  At this s: su(2) scale = e^{{-2*{s_phi:.4f}}} = {np.exp(-2*s_phi):.6f} = 1/phi^2 = {1/PHI_PAASCH**2:.6f}")
    print(f"  C^2 scale = e^{{{s_phi:.4f}}} = phi = {PHI_PAASCH:.6f}")
    print(f"  u(1) scale = e^{{2*{s_phi:.4f}}} = phi^2 = {PHI_PAASCH**2:.6f}")

    print(f"\n{'='*80}")
    print("ANALYSIS COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
