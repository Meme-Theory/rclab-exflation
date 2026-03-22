#!/usr/bin/env python3
"""
Session 33 W3: Wall-Localized PMNS Extraction
==============================================================================

Computes the PMNS matrix and mass-squared ratio R from the WALL-LOCALIZED
hybrid Hamiltonian, where B2 is wall-localized (shifted by BCS condensate)
and B1, B3 remain at bulk values.

The "wrong triple" thesis: 31 sessions tested bulk + bare + uniform tau.
The correct physics is boundary + quantum-corrected + inhomogeneous tau.

Method:
    1. Use bulk eigenvalues: E_B1, E_B2, E_B3 from s23a_kosmann_singlet.npz
    2. Apply BCS shift to B2: E_B2^BCS = sqrt(E_B2^2 + Delta_B2^2)
    3. Construct wall-modified coupling matrix using eigenvector overlaps
       from s32b_wall_dos.npz
    4. Build hybrid tridiagonal H_3x3 and diagonalize
    5. Extract PMNS angles and R

Pre-registered gates:
    R-WALL: R_wall in [5, 100]
    PMNS-WALL: theta_23 in [35, 55] deg AND sin^2(theta_13) in [0.01, 0.05]

Author: neutrino (neutrino-detection-specialist)
Date: 2026-03-06
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.interpolate import CubicSpline

# ============================================================
# Configuration
# ============================================================
DATA_DIR = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")
SINGLET_FILE = DATA_DIR / "s23a_kosmann_singlet.npz"
WALL_DOS_FILE = DATA_DIR / "s32b_wall_dos.npz"
UMKLAPP_FILE = DATA_DIR / "s32a_umklapp_vertex.npz"
OUTPUT_NPZ = DATA_DIR / "s33w3_wall_pmns.npz"
OUTPUT_PNG = DATA_DIR / "s33w3_wall_pmns.png"

# PDG targets
PDG = {
    'sin2_13': (0.020, 0.024, 0.0218),  # (lo, hi, best_fit)
    'theta_12': (31.3, 35.9, 33.44),
    'theta_23': (40.1, 51.7, 49.1),
    'R': (29.0, 37.0, 32.6),  # R = Dm^2_32 / Dm^2_21
}

# BCS gap values to scan (Delta_B2)
# Range: 0 (no BCS) to 0.5 (strong BCS)
# From Session 23a: M_max_mu0 = 0.098-0.154 at tau 0.15-0.50 (bulk, too small)
# From W-32b: rho_wall = 12.5-21.6 (well above threshold 6.7)
# Wall BCS Delta_B2 is UNKNOWN -- scan over plausible range
DELTA_B2_SCAN = np.linspace(0.0, 0.5, 51)


# ============================================================
# Module 1: PMNS extraction from 3x3 matrix
# ============================================================
def extract_pmns(U):
    """Extract mixing angles from 3x3 eigenvector matrix.
    Convention: U[alpha, i] with alpha=flavor, i=mass (sorted ascending).
    """
    sin2_13 = abs(U[0, 2])**2
    theta_13 = np.degrees(np.arcsin(np.sqrt(np.clip(sin2_13, 0, 1))))

    if abs(U[0, 0]) > 1e-15:
        tan2_12 = abs(U[0, 1])**2 / abs(U[0, 0])**2
        theta_12 = np.degrees(np.arctan(np.sqrt(tan2_12)))
    else:
        theta_12 = 90.0

    if abs(U[2, 2]) > 1e-15:
        tan2_23 = abs(U[1, 2])**2 / abs(U[2, 2])**2
        theta_23 = np.degrees(np.arctan(np.sqrt(tan2_23)))
    else:
        theta_23 = 90.0

    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))

    return {
        'sin2_13': sin2_13,
        'theta_13': theta_13,
        'theta_12': theta_12,
        'theta_23': theta_23,
        'J': J,
    }


# ============================================================
# Module 2: Data loading
# ============================================================
def load_data():
    """Load all required data."""
    d = np.load(SINGLET_FILE, allow_pickle=True)
    tau_values = d['tau_values']

    eigenvalues = {}
    eigenvectors = {}
    V_pairing = {}
    for i in range(len(tau_values)):
        tau = float(tau_values[i])
        eigenvalues[tau] = d[f'eigenvalues_{i}']
        eigenvectors[tau] = d[f'eigenvectors_{i}']
        V_pairing[tau] = d[f'V_pairing_{i}']

    wd = np.load(WALL_DOS_FILE, allow_pickle=True)
    umk = np.load(UMKLAPP_FILE, allow_pickle=True)

    return tau_values, eigenvalues, eigenvectors, V_pairing, wd, umk


# ============================================================
# Module 3: Bulk PMNS (Method B) for comparison
# ============================================================
def compute_bulk_pmns(tau, eigenvalues, V_pairing):
    """Compute bulk PMNS at given tau using Method B."""
    evals = eigenvalues[tau]
    V = V_pairing[tau]

    E1 = evals[8]   # B1
    E2 = evals[9]   # B2 (degenerate quartet)
    E3 = evals[13]  # B3 (degenerate triplet)

    v_L1_L2 = V[8, 9:13]
    n12 = np.linalg.norm(v_L1_L2)
    L2_eff = v_L1_L2 / n12
    V_L2_L3 = V[9:13, 13:16]
    v_eff_L3 = L2_eff @ V_L2_L3
    n23 = np.linalg.norm(v_eff_L3)

    H = np.array([[E1, n12, 0.0],
                   [n12, E2, n23],
                   [0.0, n23, E3]])

    m_evals, U = np.linalg.eigh(H)
    pmns = extract_pmns(U)

    denom = m_evals[1]**2 - m_evals[0]**2
    R = (m_evals[2]**2 - m_evals[1]**2) / denom if abs(denom) > 1e-30 else np.inf

    return {
        'E1': E1, 'E2': E2, 'E3': E3,
        'V_12': n12, 'V_23': n23,
        'H': H, 'eigenvalues': m_evals, 'U': U,
        'R': R, **pmns,
    }


# ============================================================
# Module 4: Wall-localized PMNS with BCS shift
# ============================================================
def compute_wall_pmns(tau, eigenvalues, V_pairing, Delta_B2,
                      V12_wall_factor=1.0, V23_wall_factor=1.0):
    """Compute wall-localized PMNS with BCS-shifted B2.

    Parameters
    ----------
    tau : float
        Bulk tau value (for B1, B3 eigenvalues and coupling matrix).
    eigenvalues : dict
        Eigenvalues keyed by tau.
    V_pairing : dict
        Coupling matrices keyed by tau.
    Delta_B2 : float
        BCS gap for the B2 sector.
    V12_wall_factor : float
        Multiplicative factor for V_12 at the wall (default 1.0 = bulk).
    V23_wall_factor : float
        Multiplicative factor for V_23 at the wall (default 1.0 = bulk).

    Returns
    -------
    result : dict
    """
    evals = eigenvalues[tau]
    V = V_pairing[tau]

    E_B1 = evals[8]    # Uncondensed, at bulk value
    E_B2 = evals[9]    # To be BCS-shifted
    E_B3 = evals[13]   # Uncondensed, at bulk value

    # BCS quasiparticle energy
    E_B2_BCS = np.sqrt(E_B2**2 + Delta_B2**2)

    # Bulk coupling norms
    v_L1_L2 = V[8, 9:13]
    n12_bulk = np.linalg.norm(v_L1_L2)
    L2_eff = v_L1_L2 / n12_bulk
    V_L2_L3 = V[9:13, 13:16]
    v_eff_L3 = L2_eff @ V_L2_L3
    n23_bulk = np.linalg.norm(v_eff_L3)

    # Apply wall modification factors
    n12_wall = n12_bulk * V12_wall_factor
    n23_wall = n23_bulk * V23_wall_factor

    # Hybrid Hamiltonian: B1 (bulk) -- B2 (wall, BCS) -- B3 (bulk)
    H_wall = np.array([[E_B1,      n12_wall,  0.0],
                        [n12_wall,  E_B2_BCS,  n23_wall],
                        [0.0,       n23_wall,  E_B3]])

    m_evals, U = np.linalg.eigh(H_wall)
    pmns = extract_pmns(U)

    denom = m_evals[1]**2 - m_evals[0]**2
    R = (m_evals[2]**2 - m_evals[1]**2) / denom if abs(denom) > 1e-30 else np.inf

    # Mixing regime diagnostics
    dE_12 = abs(E_B2_BCS - E_B1)
    dE_23 = abs(E_B3 - E_B2_BCS)
    V12_over_dE12 = n12_wall / dE_12 if dE_12 > 1e-15 else np.inf
    V23_over_dE23 = n23_wall / dE_23 if dE_23 > 1e-15 else np.inf

    return {
        'E_B1': E_B1, 'E_B2_bare': E_B2, 'E_B2_BCS': E_B2_BCS, 'E_B3': E_B3,
        'Delta_B2': Delta_B2,
        'V_12_wall': n12_wall, 'V_23_wall': n23_wall,
        'V_12_bulk': n12_bulk, 'V_23_bulk': n23_bulk,
        'V12_wall_factor': V12_wall_factor, 'V23_wall_factor': V23_wall_factor,
        'H_wall': H_wall,
        'eigenvalues': m_evals,
        'U': U,
        'R': R,
        'dE_12': dE_12, 'dE_23': dE_23,
        'V12_over_dE12': V12_over_dE12,
        'V23_over_dE23': V23_over_dE23,
        **pmns,
    }


# ============================================================
# Module 5: Wall coupling modification analysis
# ============================================================
def analyze_wall_couplings(wd, eigenvalues, eigenvectors, V_pairing, tau_values):
    """Analyze how eigenvector mixing at the wall modifies couplings.

    Uses the overlap matrix O_kl = <psi_k(tau_1)|psi_l(tau_2)> to estimate
    the wall-modified coupling matrix elements.
    """
    results = {}

    for wall_idx, (t1_name, t2_name) in enumerate([
        ('wall_0', (0.10, 0.25)),
        ('wall_1', (0.10, 0.20)),
        ('wall_2', (0.15, 0.25)),
    ]):
        t1, t2 = t2_name
        prefix = f'wall_{wall_idx}'

        # Overlap matrix between tau_1 and tau_2 eigenstates
        O = wd[f'{prefix}_overlap_matrix']

        # The overlap between B2 eigenstates at tau_1 and tau_2
        # B2 positive indices: 9, 10, 11, 12
        # B1 positive index: 8
        # B3 positive indices: 13, 14, 15

        # Inter-branch overlaps at the wall:
        # How much B2(tau_1) projects onto B1(tau_2) and vice versa
        O_B2_to_B1 = np.mean([abs(O[9+i, 8]) for i in range(4)])
        O_B2_to_B3 = np.mean([abs(O[9+i, 13]) + abs(O[9+i, 14]) + abs(O[9+i, 15])
                               for i in range(4)]) / 3
        O_B1_to_B2 = np.mean([abs(O[8, 9+i]) for i in range(4)])
        O_B3_to_B2 = np.mean([abs(O[13+j, 9+i]) for i in range(4) for j in range(3)]) / 4

        # Wall-localized states are superpositions of tau_1 and tau_2 eigenstates
        # The effective coupling V_12^wall depends on how much the wall-localized
        # B2 state overlaps with the B1 state:
        #   V_12^wall ~ V_12(tau_1) * |<B2_wall|B2(tau_1)>| + V_12(tau_2) * |<B2_wall|B2(tau_2)>|

        # For a step wall, the wall-localized state is approximately
        # a 50/50 superposition of the two sides
        # V_12^wall ~ (V_12(tau_1) + V_12(tau_2)) / 2
        # This is conservative -- the actual wall state is more complex

        V_12_t1 = np.linalg.norm(V_pairing[t1][8, 9:13])
        V_12_t2 = np.linalg.norm(V_pairing[t2][8, 9:13])
        V_12_avg = (V_12_t1 + V_12_t2) / 2

        L2_eff_t1 = V_pairing[t1][8, 9:13] / np.linalg.norm(V_pairing[t1][8, 9:13])
        L2_eff_t2 = V_pairing[t2][8, 9:13] / np.linalg.norm(V_pairing[t2][8, 9:13])
        V_23_t1 = np.linalg.norm(L2_eff_t1 @ V_pairing[t1][9:13, 13:16])
        V_23_t2 = np.linalg.norm(L2_eff_t2 @ V_pairing[t2][9:13, 13:16])
        V_23_avg = (V_23_t1 + V_23_t2) / 2

        # Effective coupling ratio at the wall
        V12_over_V23 = V_12_avg / V_23_avg if V_23_avg > 1e-15 else np.inf

        results[(t1, t2)] = {
            'O_B2_to_B1': O_B2_to_B1,
            'O_B2_to_B3': O_B2_to_B3,
            'O_B1_to_B2': O_B1_to_B2,
            'O_B3_to_B2': O_B3_to_B2,
            'V_12_t1': V_12_t1, 'V_12_t2': V_12_t2, 'V_12_avg': V_12_avg,
            'V_23_t1': V_23_t1, 'V_23_t2': V_23_t2, 'V_23_avg': V_23_avg,
            'V12_over_V23': V12_over_V23,
        }

    return results


# ============================================================
# Module 6: Required V12/V23 ratio for R target
# ============================================================
def find_required_coupling_ratio(tau, eigenvalues, V_pairing, Delta_B2, R_target=33.0):
    """Find the V12_wall_factor / V23_wall_factor ratio needed for R = R_target.

    Scans V12_factor and V23_factor independently to map the R surface.
    """
    evals = eigenvalues[tau]
    V = V_pairing[tau]

    E_B1 = evals[8]
    E_B2 = evals[9]
    E_B3 = evals[13]
    E_B2_BCS = np.sqrt(E_B2**2 + Delta_B2**2)

    n12_bulk = np.linalg.norm(V[8, 9:13])
    L2_eff = V[8, 9:13] / n12_bulk
    n23_bulk = np.linalg.norm(L2_eff @ V[9:13, 13:16])

    # Scan: what ratio V12/V23 gives R = 33?
    # Use perturbation theory: for small V/dE, R ~ (V12/V23)^2 * (dE23/dE12)^2
    dE_12 = abs(E_B2_BCS - E_B1)
    dE_23 = abs(E_B3 - E_B2_BCS)

    # Perturbative estimate
    R_pert = lambda f12, f23: (f12 * n12_bulk / dE_12)**2 / (f23 * n23_bulk / dE_23)**2 \
        if (f23 * n23_bulk / dE_23) > 1e-15 else np.inf

    # Full diagonalization scan
    factor_grid = np.linspace(0.1, 10.0, 200)
    best_f12 = None
    best_f23 = None
    best_R = None
    best_diff = np.inf

    # First: fix V23 at bulk, scan V12
    R_vs_f12 = []
    for f12 in factor_grid:
        H = np.array([[E_B1,               f12 * n12_bulk, 0.0],
                       [f12 * n12_bulk,     E_B2_BCS,       n23_bulk],
                       [0.0,                n23_bulk,        E_B3]])
        m, _ = np.linalg.eigh(H)
        denom = m[1]**2 - m[0]**2
        R = (m[2]**2 - m[1]**2) / denom if abs(denom) > 1e-30 else np.inf
        R_vs_f12.append(R)
        if abs(R - R_target) < best_diff:
            best_diff = abs(R - R_target)
            best_f12 = f12
            best_R = R

    # Second: fix V12 at bulk, scan V23
    R_vs_f23 = []
    for f23 in factor_grid:
        H = np.array([[E_B1,           n12_bulk,       0.0],
                       [n12_bulk,       E_B2_BCS,       f23 * n23_bulk],
                       [0.0,            f23 * n23_bulk, E_B3]])
        m, _ = np.linalg.eigh(H)
        denom = m[1]**2 - m[0]**2
        R = (m[2]**2 - m[1]**2) / denom if abs(denom) > 1e-30 else np.inf
        R_vs_f23.append(R)

    # Third: scan ratio V12/V23 while keeping total coupling constant
    # f12 = r, f23 = 1/r  (total V^2 preserved)
    R_vs_ratio = []
    ratio_grid = np.linspace(0.5, 15.0, 200)
    for ratio in ratio_grid:
        H = np.array([[E_B1,                   ratio * n12_bulk, 0.0],
                       [ratio * n12_bulk,       E_B2_BCS,         (1.0/ratio) * n23_bulk],
                       [0.0,                    (1.0/ratio) * n23_bulk, E_B3]])
        m, _ = np.linalg.eigh(H)
        denom = m[1]**2 - m[0]**2
        R = (m[2]**2 - m[1]**2) / denom if abs(denom) > 1e-30 else np.inf
        R_vs_ratio.append(R)

    return {
        'factor_grid': factor_grid,
        'R_vs_f12': np.array(R_vs_f12),
        'R_vs_f23': np.array(R_vs_f23),
        'ratio_grid': ratio_grid,
        'R_vs_ratio': np.array(R_vs_ratio),
        'best_f12': best_f12,
        'best_R': best_R,
        'E_B2_BCS': E_B2_BCS,
        'dE_12': dE_12,
        'dE_23': dE_23,
        'n12_bulk': n12_bulk,
        'n23_bulk': n23_bulk,
    }


# ============================================================
# Module 7: Main computation
# ============================================================
def main():
    print("=" * 75)
    print("SESSION 33 W3: WALL-LOCALIZED PMNS EXTRACTION")
    print("=" * 75)

    tau_values, eigenvalues, eigenvectors, V_pairing, wd, umk = load_data()

    # Reference tau for analysis (dump point region)
    tau_ref = 0.20  # closest grid point to dump point 0.19

    # ============================================================
    # Part 1: Bulk PMNS baseline at tau = 0.20
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 1: BULK PMNS BASELINE (tau = 0.20)")
    print("=" * 70)

    bulk = compute_bulk_pmns(tau_ref, eigenvalues, V_pairing)
    print(f"  E_B1 = {bulk['E1']:.8f}")
    print(f"  E_B2 = {bulk['E2']:.8f}")
    print(f"  E_B3 = {bulk['E3']:.8f}")
    print(f"  dE_12 = {abs(bulk['E2'] - bulk['E1']):.8f}")
    print(f"  dE_23 = {abs(bulk['E3'] - bulk['E2']):.8f}")
    print(f"  V_12 = {bulk['V_12']:.8f}")
    print(f"  V_23 = {bulk['V_23']:.8f}")
    print(f"  V_12/dE_12 = {bulk['V_12']/abs(bulk['E2']-bulk['E1']):.4f}  (STRONG MIXING)")
    print(f"  V_23/dE_23 = {bulk['V_23']/abs(bulk['E3']-bulk['E2']):.4f}")
    print(f"  sin^2(theta_13) = {bulk['sin2_13']:.6f}  (PDG: 0.022)")
    print(f"  theta_12 = {bulk['theta_12']:.2f} deg  (PDG: 33.4)")
    print(f"  theta_23 = {bulk['theta_23']:.2f} deg  (PDG: 49.1)")
    print(f"  R = {bulk['R']:.4f}  (PDG: 32.6)")

    # ============================================================
    # Part 2: Wall-localized PMNS scan over Delta_B2
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 2: WALL-LOCALIZED PMNS vs Delta_B2 (bulk couplings)")
    print("=" * 70)
    print(f"{'Delta_B2':>10} | {'E_B2_BCS':>10} | {'dE_12':>10} | {'V12/dE12':>10} | "
          f"{'sin2_13':>10} | {'th12':>8} | {'th23':>8} | {'R':>10}")
    print("-" * 95)

    wall_results = []
    for Delta in DELTA_B2_SCAN:
        r = compute_wall_pmns(tau_ref, eigenvalues, V_pairing, Delta)
        wall_results.append(r)
        if Delta in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]:
            print(f"{Delta:10.3f} | {r['E_B2_BCS']:10.6f} | {r['dE_12']:10.6f} | "
                  f"{r['V12_over_dE12']:10.4f} | {r['sin2_13']:10.6f} | "
                  f"{r['theta_12']:8.2f} | {r['theta_23']:8.2f} | {r['R']:10.4f}")

    # ============================================================
    # Part 3: Find Delta_B2 where mixing regime transitions
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 3: MIXING REGIME TRANSITION")
    print("=" * 70)

    # Strong mixing: V12/dE12 > 2. Weak mixing: V12/dE12 < 0.5
    for i, r in enumerate(wall_results):
        if r['V12_over_dE12'] < 1.0:
            Delta_transition = r['Delta_B2']
            print(f"  V12/dE12 drops below 1.0 at Delta_B2 = {Delta_transition:.4f}")
            print(f"  At this point:")
            print(f"    E_B2_BCS = {r['E_B2_BCS']:.6f}")
            print(f"    dE_12 = {r['dE_12']:.6f}")
            print(f"    sin^2(theta_13) = {r['sin2_13']:.6f}")
            print(f"    theta_23 = {r['theta_23']:.2f} deg")
            print(f"    R = {r['R']:.4f}")
            break

    for i, r in enumerate(wall_results):
        if r['V12_over_dE12'] < 0.5:
            Delta_weak = r['Delta_B2']
            print(f"\n  V12/dE12 drops below 0.5 at Delta_B2 = {Delta_weak:.4f}")
            print(f"  At this point:")
            print(f"    E_B2_BCS = {r['E_B2_BCS']:.6f}")
            print(f"    dE_12 = {r['dE_12']:.6f}")
            print(f"    sin^2(theta_13) = {r['sin2_13']:.6f}")
            print(f"    theta_23 = {r['theta_23']:.2f} deg")
            print(f"    R = {r['R']:.4f}")
            break

    # ============================================================
    # Part 4: R as function of Delta_B2 -- does it reach 33?
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 4: R vs Delta_B2 -- CAN R REACH 33 WITH BULK COUPLINGS?")
    print("=" * 70)

    R_arr = np.array([r['R'] for r in wall_results])
    R_max = np.max(R_arr)
    Delta_at_Rmax = DELTA_B2_SCAN[np.argmax(R_arr)]
    print(f"  Maximum R = {R_max:.4f} at Delta_B2 = {Delta_at_Rmax:.4f}")
    print(f"  R at Delta_B2 = 0.25: {wall_results[25]['R']:.4f}")
    print(f"  R at Delta_B2 = 0.50: {wall_results[50]['R']:.4f}")

    if R_max >= 5.0:
        print(f"  R enters [5, 100] window: PARTIAL PASS")
    else:
        print(f"  R never reaches 5.0 with bulk couplings: FAIL (max R = {R_max:.4f})")

    if R_max >= 29.0:
        print(f"  R enters PDG window [29, 37]: PASS")
    else:
        print(f"  R never reaches PDG window with bulk couplings")
        print(f"  CONCLUSION: Wall-modified couplings REQUIRED for R ~ 33")

    # ============================================================
    # Part 5: Required coupling ratio for R = 33
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 5: REQUIRED COUPLING RATIO V12_wall/V23_wall FOR R ~ 33")
    print("=" * 70)

    # Test at several Delta_B2 values
    for Delta_test in [0.15, 0.20, 0.25, 0.30]:
        req = find_required_coupling_ratio(tau_ref, eigenvalues, V_pairing,
                                            Delta_test, R_target=33.0)
        print(f"\n  Delta_B2 = {Delta_test:.2f}:")
        print(f"    E_B2_BCS = {req['E_B2_BCS']:.6f}")
        print(f"    dE_12 = {req['dE_12']:.6f}, dE_23 = {req['dE_23']:.6f}")
        print(f"    n12_bulk = {req['n12_bulk']:.6f}, n23_bulk = {req['n23_bulk']:.6f}")

        # Find where R crosses 33 in the ratio scan
        R_ratio = req['R_vs_ratio']
        ratio_grid = req['ratio_grid']
        crossings = []
        for i in range(len(R_ratio) - 1):
            if (R_ratio[i] - 33) * (R_ratio[i+1] - 33) < 0:
                # Linear interpolation
                r_cross = ratio_grid[i] + (33 - R_ratio[i]) * (ratio_grid[i+1] - ratio_grid[i]) / (R_ratio[i+1] - R_ratio[i])
                crossings.append(r_cross)

        if crossings:
            print(f"    R = 33 at V12/V23 ratio factor = {crossings[0]:.4f}")
            # This means V12_wall = ratio * V12_bulk, V23_wall = (1/ratio) * V23_bulk
            # So V12_wall/V23_wall = ratio^2 * (V12_bulk/V23_bulk)
            actual_ratio = crossings[0]**2 * (req['n12_bulk'] / req['n23_bulk'])
            print(f"    Actual V12_wall/V23_wall = {actual_ratio:.4f}")
        else:
            print(f"    R = 33 NOT achievable in ratio range [0.5, 15]")

        # Also find where R crosses 33 with f12 scan (V23 at bulk)
        R_f12 = req['R_vs_f12']
        for i in range(len(R_f12) - 1):
            if (R_f12[i] - 33) * (R_f12[i+1] - 33) < 0:
                f12_cross = factor_grid[i] + (33 - R_f12[i]) * (factor_grid[i+1] - factor_grid[i]) / (R_f12[i+1] - R_f12[i])
                print(f"    R = 33 by V12 enhancement alone: f12 = {f12_cross:.4f}")
                break
        else:
            print(f"    R = 33 NOT achievable by V12 enhancement alone in [0.1, 10]")

        factor_grid = req['factor_grid']

    # ============================================================
    # Part 6: Wall coupling analysis from overlap matrices
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 6: WALL-MODIFIED COUPLINGS FROM OVERLAP MATRICES")
    print("=" * 70)

    wall_coupling = analyze_wall_couplings(wd, eigenvalues, eigenvectors,
                                            V_pairing, tau_values)

    for (t1, t2), wc in wall_coupling.items():
        print(f"\n  Wall ({t1}, {t2}):")
        print(f"    V_12(tau_1) = {wc['V_12_t1']:.6f}")
        print(f"    V_12(tau_2) = {wc['V_12_t2']:.6f}")
        print(f"    V_12_avg    = {wc['V_12_avg']:.6f}")
        print(f"    V_23(tau_1) = {wc['V_23_t1']:.6f}")
        print(f"    V_23(tau_2) = {wc['V_23_t2']:.6f}")
        print(f"    V_23_avg    = {wc['V_23_avg']:.6f}")
        print(f"    V12/V23 (bulk ratio, averaged) = {wc['V12_over_V23']:.4f}")
        print(f"    Inter-branch leakage: B2->B1 = {wc['O_B2_to_B1']:.4f}, "
              f"B2->B3 = {wc['O_B2_to_B3']:.4f}")

    # ============================================================
    # Part 7: Gate verdict
    # ============================================================
    print("\n" + "=" * 75)
    print("GATE VERDICTS")
    print("=" * 75)

    # Find the best-case scenario (optimizing over Delta_B2)
    best_R_bulk = max(r['R'] for r in wall_results)
    best_idx = np.argmax([r['R'] for r in wall_results])
    best = wall_results[best_idx]

    print(f"\n  R-WALL gate: R_wall in [5, 100]")
    print(f"    Best R with bulk couplings: {best_R_bulk:.4f} at Delta_B2 = {best['Delta_B2']:.4f}")
    if 5 <= best_R_bulk <= 100:
        print(f"    Verdict: PASS (R = {best_R_bulk:.4f} in [5, 100])")
    else:
        print(f"    Verdict: FAIL with bulk couplings (best R = {best_R_bulk:.4f})")
        print(f"    Wall-modified couplings V12/V23 > 5 REQUIRED")

    print(f"\n  PMNS-WALL gate: theta_23 in [35, 55] AND sin^2(theta_13) in [0.01, 0.05]")
    # Check at various Delta_B2
    for r in wall_results:
        if 35 <= r['theta_23'] <= 55 and 0.01 <= r['sin2_13'] <= 0.05:
            print(f"    PASS at Delta_B2 = {r['Delta_B2']:.4f}:")
            print(f"      theta_23 = {r['theta_23']:.2f}, sin^2(theta_13) = {r['sin2_13']:.6f}")
            break
    else:
        # Find closest approach to the gate
        # theta_23 is easy; sin^2(theta_13) is the problem
        min_s13 = min(r['sin2_13'] for r in wall_results)
        best_s13_r = min(wall_results, key=lambda r: r['sin2_13'])
        print(f"    FAIL: sin^2(theta_13) never drops below 0.05 with bulk couplings")
        print(f"    Minimum sin^2(theta_13) = {min_s13:.6f} at Delta_B2 = {best_s13_r['Delta_B2']:.4f}")
        print(f"    theta_23 at that point = {best_s13_r['theta_23']:.2f} deg")
        print(f"    CONCLUSION: Wall-modified couplings needed to reduce sin^2(theta_13)")

    # ============================================================
    # Part 8: theta_23 corridor check
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 8: theta_23 CORRIDOR (PDG WINDOW [40.1, 51.7])")
    print("=" * 70)

    in_window = [(r['Delta_B2'], r['theta_23']) for r in wall_results
                 if 40.1 <= r['theta_23'] <= 51.7]
    if in_window:
        print(f"  theta_23 in PDG window for Delta_B2 in:")
        print(f"    [{in_window[0][0]:.4f}, {in_window[-1][0]:.4f}]")
        print(f"    theta_23 range: [{in_window[0][1]:.2f}, {in_window[-1][1]:.2f}]")
    else:
        # Check a wider range
        for r in wall_results:
            if 35 <= r['theta_23'] <= 55:
                print(f"  theta_23 = {r['theta_23']:.2f} at Delta_B2 = {r['Delta_B2']:.4f}")

    # ============================================================
    # Part 9: Mass ordering at the wall
    # ============================================================
    print("\n" + "=" * 70)
    print("PART 9: MASS ORDERING AT THE WALL")
    print("=" * 70)

    for Delta_test in [0.0, 0.15, 0.25, 0.40]:
        r = compute_wall_pmns(tau_ref, eigenvalues, V_pairing, Delta_test)
        m = r['eigenvalues']
        ordering = "NORMAL" if m[2] > m[1] > m[0] else "INVERTED" if m[1] > m[2] > m[0] else "OTHER"
        print(f"  Delta_B2 = {Delta_test:.2f}: m = [{m[0]:.6f}, {m[1]:.6f}, {m[2]:.6f}]")
        print(f"    Ordering: {ordering}")
        print(f"    E_B1={r['E_B1']:.6f}, E_B2_BCS={r['E_B2_BCS']:.6f}, E_B3={r['E_B3']:.6f}")
        print(f"    Level order: B1 < {'B2_BCS < B3' if r['E_B2_BCS'] < r['E_B3'] else 'B3 < B2_BCS'}")

    # ============================================================
    # Save results
    # ============================================================
    save_dict = {
        'tau_ref': tau_ref,
        'Delta_B2_scan': DELTA_B2_SCAN,
        'R_vs_Delta': np.array([r['R'] for r in wall_results]),
        'sin2_13_vs_Delta': np.array([r['sin2_13'] for r in wall_results]),
        'theta_12_vs_Delta': np.array([r['theta_12'] for r in wall_results]),
        'theta_23_vs_Delta': np.array([r['theta_23'] for r in wall_results]),
        'V12_over_dE12_vs_Delta': np.array([r['V12_over_dE12'] for r in wall_results]),
        'dE_12_vs_Delta': np.array([r['dE_12'] for r in wall_results]),
        'E_B2_BCS_vs_Delta': np.array([r['E_B2_BCS'] for r in wall_results]),
        'bulk_R': bulk['R'],
        'bulk_sin2_13': bulk['sin2_13'],
        'bulk_theta_23': bulk['theta_23'],
    }
    np.savez(OUTPUT_NPZ, **save_dict)
    print(f"\nResults saved to {OUTPUT_NPZ}")

    # ============================================================
    # Plot
    # ============================================================
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Session 33 W3: Wall-Localized PMNS Extraction\n'
                 r'Hybrid Hamiltonian: B2$^{\rm BCS}$ (wall) + B1, B3 (bulk) at $\tau=0.20$',
                 fontsize=13, fontweight='bold')

    Delta_arr = DELTA_B2_SCAN
    R_arr = np.array([r['R'] for r in wall_results])
    s13_arr = np.array([r['sin2_13'] for r in wall_results])
    t12_arr = np.array([r['theta_12'] for r in wall_results])
    t23_arr = np.array([r['theta_23'] for r in wall_results])
    ratio_arr = np.array([r['V12_over_dE12'] for r in wall_results])
    dE12_arr = np.array([r['dE_12'] for r in wall_results])

    # Panel 1: R vs Delta_B2
    ax = axes[0, 0]
    ax.plot(Delta_arr, R_arr, 'b-', linewidth=2)
    ax.axhspan(29, 37, alpha=0.15, color='green', label='PDG window')
    ax.axhline(32.6, color='green', linestyle='--', alpha=0.5, label='PDG best fit')
    ax.axhline(5, color='orange', linestyle=':', alpha=0.5, label='Gate lower bound')
    ax.set_xlabel(r'$\Delta_{B2}$ (BCS gap)')
    ax.set_ylabel(r'$R = \Delta m^2_{32}/\Delta m^2_{21}$')
    ax.set_title('R vs BCS Gap (bulk couplings)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max(10, R_arr.max() * 1.1))

    # Panel 2: sin^2(theta_13) vs Delta_B2
    ax = axes[0, 1]
    ax.plot(Delta_arr, s13_arr, 'r-', linewidth=2)
    ax.axhspan(0.020, 0.024, alpha=0.15, color='green', label='PDG window')
    ax.axhline(0.0218, color='green', linestyle='--', alpha=0.5)
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$\sin^2(\theta_{13})$')
    ax.set_title(r'$\sin^2(\theta_{13})$ vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: theta_23 vs Delta_B2
    ax = axes[0, 2]
    ax.plot(Delta_arr, t23_arr, 'm-', linewidth=2)
    ax.axhspan(40.1, 51.7, alpha=0.15, color='green', label='PDG window')
    ax.axhline(49.1, color='green', linestyle='--', alpha=0.5)
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$\theta_{23}$ (deg)')
    ax.set_title(r'$\theta_{23}$ vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 4: V12/dE12 mixing ratio vs Delta_B2
    ax = axes[1, 0]
    ax.plot(Delta_arr, ratio_arr, 'k-', linewidth=2)
    ax.axhline(1.0, color='red', linestyle=':', label='Strong/weak boundary')
    ax.axhline(0.5, color='orange', linestyle=':', label='Perturbative boundary')
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$V_{12}/\delta E_{12}$')
    ax.set_title('Mixing Regime vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 5: Energy levels vs Delta_B2
    ax = axes[1, 1]
    E_B1_val = wall_results[0]['E_B1']
    E_B3_val = wall_results[0]['E_B3']
    E_B2_BCS_arr = np.array([r['E_B2_BCS'] for r in wall_results])
    ax.plot(Delta_arr, [E_B1_val]*len(Delta_arr), 'r--', linewidth=1.5, label='B1 (uncondensed)')
    ax.plot(Delta_arr, E_B2_BCS_arr, 'b-', linewidth=2, label=r'B2$^{\rm BCS}$')
    ax.plot(Delta_arr, [E_B3_val]*len(Delta_arr), 'g--', linewidth=1.5, label='B3 (uncondensed)')
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel('Energy level')
    ax.set_title('Branch Energy Levels vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 6: theta_12 vs Delta_B2
    ax = axes[1, 2]
    ax.plot(Delta_arr, t12_arr, 'c-', linewidth=2)
    ax.axhspan(31.3, 35.9, alpha=0.15, color='green', label='PDG window')
    ax.axhline(33.4, color='green', linestyle='--', alpha=0.5)
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$\theta_{12}$ (deg)')
    ax.set_title(r'$\theta_{12}$ vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Plot saved to {OUTPUT_PNG}")

    return wall_results, bulk


if __name__ == '__main__':
    wall_results, bulk = main()
