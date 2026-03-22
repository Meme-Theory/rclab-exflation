#!/usr/bin/env python3
"""
Session 35 W3-A: Wall-Localized PMNS with CORRECTED Spinor V
==============================================================================

Reruns the wall-localized PMNS extraction from Session 33 W3 with:
  1. CORRECTED spinor V matrix elements (from s34a_dphys_kosmann.npz):
     - V(B1,B2) = 0.077 (was 0.160 in frame V)
     - V(B2,B3) = 0.022 (was 0.059 in frame V)
     - V(B2,B2) = 0.086 at phi=gap
  2. BCS gap computed self-consistently from:
     - rho_smooth = 14.02/mode (van Hove wall DOS)
     - V(B2,B2) = 0.086 at phi=gap
  3. Bulk eigenvalues from s23a_kosmann_singlet.npz (unchanged)

Pre-registered gate:
    PMNS-CORRECTED-35: PASS if
        theta_23 in [35, 55] deg AND
        sin^2(theta_13) in [0.01, 0.05] AND
        R in [10, 100]

NuFIT 5.3 comparison targets (NO):
    Delta m^2_21 = 7.53e-5 eV^2
    |Delta m^2_32| = 2.453e-3 eV^2
    R = 32.6  (PDG window: 29-37)
    sin^2(theta_12) = 0.307 -> theta_12 = 33.44 deg
    sin^2(theta_23) = 0.546 -> theta_23 = 49.2 deg (NO)
    sin^2(theta_13) = 0.0220

Author: neutrino-detection-specialist
Date: 2026-03-07
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# Configuration
# ============================================================
DATA_DIR = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")
SINGLET_FILE = DATA_DIR / "s23a_kosmann_singlet.npz"
DPHYS_FILE = DATA_DIR / "s34a_dphys_kosmann.npz"
OLD_PMNS_FILE = DATA_DIR / "s33w3_wall_pmns.npz"
OUTPUT_NPZ = DATA_DIR / "s35_pmns_corrected.npz"
OUTPUT_PNG = DATA_DIR / "s35_pmns_corrected.png"

# Session 34 corrected spinor V (at phi=gap=0.13, tau=0.20)
V_B1B2_SPINOR = 0.076994  # from s34a_dphys_kosmann.npz at phi=0.13
V_B2B3_SPINOR = 0.021959  # from s34a_dphys_kosmann.npz at phi=0.13
V_B2B2_SPINOR = 0.085940  # from s34a_dphys_kosmann.npz at phi=0.13

# Van Hove smooth-wall DOS
RHO_SMOOTH = 14.02  # modes per unit energy at smooth wall

# NuFIT 5.3 targets (Normal Ordering)
NUFIT = {
    'sin2_13':   (0.02034, 0.02430, 0.02200),  # (lo, hi, best_fit) 3sigma
    'sin2_12':   (0.269, 0.343, 0.307),
    'theta_12':  (31.3, 35.9, 33.44),
    'theta_23':  (40.1, 51.7, 49.2),
    'sin2_23':   (0.415, 0.616, 0.546),
    'R':         (29.0, 37.0, 32.6),
    'Dm2_21':    7.53e-5,  # eV^2
    'Dm2_32':    2.453e-3, # eV^2
}

# BCS gap scan range
DELTA_B2_SCAN = np.linspace(0.0, 0.5, 101)


# ============================================================
# Module 1: BCS gap computation
# ============================================================
def compute_bcs_gap(V_eff, rho, W_B2=0.0579):
    """Compute BCS gap self-consistently.

    Delta = W * exp(-1/g) where g = V * rho

    Parameters
    ----------
    V_eff : float
        Effective pairing interaction strength.
    rho : float
        Density of states per mode.
    W_B2 : float
        B2 bandwidth (Debye energy analog).

    Returns
    -------
    Delta : float
        BCS gap.
    g : float
        Dimensionless coupling g = V * rho.
    """
    g = V_eff * rho
    if g <= 0:
        return 0.0, 0.0
    Delta = W_B2 * np.exp(-1.0 / g)
    return Delta, g


# ============================================================
# Module 2: PMNS extraction from 3x3 matrix
# ============================================================
def extract_pmns(U):
    """Extract mixing angles from 3x3 PMNS matrix.

    Convention: U[alpha, i] with alpha=flavor, i=mass eigenstate (sorted ascending).
    Standard parameterization:
        |U_e3|^2 = sin^2(theta_13)
        |U_e2|^2 / |U_e1|^2 = tan^2(theta_12)  [cos^2(theta_13) cancels]
        |U_mu3|^2 / |U_tau3|^2 = tan^2(theta_23)
    """
    # sin^2(theta_13) = |U_e3|^2
    sin2_13 = abs(U[0, 2])**2
    theta_13 = np.degrees(np.arcsin(np.sqrt(np.clip(sin2_13, 0, 1))))

    # theta_12 from |U_e2/U_e1|
    if abs(U[0, 0]) > 1e-15:
        tan2_12 = abs(U[0, 1])**2 / abs(U[0, 0])**2
        theta_12 = np.degrees(np.arctan(np.sqrt(tan2_12)))
    else:
        theta_12 = 90.0

    # theta_23 from |U_mu3/U_tau3|
    if abs(U[2, 2]) > 1e-15:
        tan2_23 = abs(U[1, 2])**2 / abs(U[2, 2])**2
        theta_23 = np.degrees(np.arctan(np.sqrt(tan2_23)))
    else:
        theta_23 = 90.0

    # Jarlskog invariant (CP phase)
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))

    # sin^2(theta_12) and sin^2(theta_23) for comparison
    sin2_12 = np.sin(np.radians(theta_12))**2
    sin2_23 = np.sin(np.radians(theta_23))**2

    return {
        'sin2_13': sin2_13,
        'theta_13': theta_13,
        'theta_12': theta_12,
        'theta_23': theta_23,
        'sin2_12': sin2_12,
        'sin2_23': sin2_23,
        'J': J,
    }


# ============================================================
# Module 3: Load data
# ============================================================
def load_data():
    """Load bulk eigenvalues and Session 34 corrected V data."""
    # Bulk eigenvalues
    d = np.load(SINGLET_FILE, allow_pickle=True)
    tau_values = d['tau_values']

    eigenvalues = {}
    eigenvectors = {}
    V_pairing_frame = {}  # Frame V (A_antisym) -- for comparison only
    for i in range(len(tau_values)):
        tau = float(tau_values[i])
        eigenvalues[tau] = d[f'eigenvalues_{i}']
        eigenvectors[tau] = d[f'eigenvectors_{i}']
        V_pairing_frame[tau] = d[f'V_pairing_{i}']

    # Session 34 corrected data
    d34 = np.load(DPHYS_FILE, allow_pickle=True)

    # Old PMNS results for comparison
    old = np.load(OLD_PMNS_FILE, allow_pickle=True)

    return tau_values, eigenvalues, eigenvectors, V_pairing_frame, d34, old


# ============================================================
# Module 4: Wall-localized PMNS with corrected V
# ============================================================
def compute_corrected_wall_pmns(tau, eigenvalues, Delta_B2,
                                 V12=None, V23=None):
    """Compute wall-localized PMNS with corrected spinor V and BCS-shifted B2.

    Parameters
    ----------
    tau : float
        Reference tau for bulk eigenvalues.
    eigenvalues : dict
        Eigenvalues keyed by tau.
    Delta_B2 : float
        BCS gap for the B2 sector.
    V12 : float
        Spinor coupling V(B1,B2). Default: V_B1B2_SPINOR.
    V23 : float
        Spinor coupling V(B2,B3). Default: V_B2B3_SPINOR.

    Returns
    -------
    result : dict
    """
    if V12 is None:
        V12 = V_B1B2_SPINOR
    if V23 is None:
        V23 = V_B2B3_SPINOR

    evals = eigenvalues[tau]

    # Branch energies at tau=0.20:
    # B1 = evals[8] = 0.81914  (trivial rep, 1-fold)
    # B2 = evals[9] = 0.84527  (fundamental, 4-fold degenerate)
    # B3 = evals[13] = 0.97822 (adjoint, 3-fold degenerate)
    E_B1 = evals[8]
    E_B2 = evals[9]
    E_B3 = evals[13]

    # BCS quasiparticle energy for B2
    E_B2_BCS = np.sqrt(E_B2**2 + Delta_B2**2)

    # Tridiagonal Hamiltonian with NNI texture (V_11=0, V_13=0 exact)
    #
    # H = [ E_B1     V_12      0    ]
    #     [ V_12   E_B2_BCS  V_23   ]
    #     [  0       V_23    E_B3   ]
    #
    # This is EXACT: V(B1,B1)=0 (Trap 1), V(B1,B3)=0 (Trap 4/Schur)
    H = np.array([
        [E_B1,     V12,      0.0],
        [V12,      E_B2_BCS, V23],
        [0.0,      V23,      E_B3]
    ])

    m_evals, U = np.linalg.eigh(H)

    pmns = extract_pmns(U)

    # Mass-squared ratio
    dm2_21 = m_evals[1]**2 - m_evals[0]**2
    dm2_31 = m_evals[2]**2 - m_evals[0]**2
    dm2_32 = m_evals[2]**2 - m_evals[1]**2
    R = dm2_32 / dm2_21 if abs(dm2_21) > 1e-30 else np.inf

    # Mixing regime diagnostics
    dE_12 = abs(E_B2_BCS - E_B1)
    dE_23 = abs(E_B3 - E_B2_BCS)
    V12_over_dE12 = V12 / dE_12 if dE_12 > 1e-15 else np.inf
    V23_over_dE23 = V23 / dE_23 if dE_23 > 1e-15 else np.inf

    # Mass ordering check
    ordering = "NORMAL" if m_evals[2] > m_evals[1] > m_evals[0] else \
               "INVERTED" if m_evals[1] > m_evals[2] > m_evals[0] else "OTHER"

    return {
        'E_B1': E_B1, 'E_B2_bare': E_B2, 'E_B2_BCS': E_B2_BCS, 'E_B3': E_B3,
        'Delta_B2': Delta_B2,
        'V_12': V12, 'V_23': V23,
        'V_12_over_V_23': V12 / V23 if V23 > 0 else np.inf,
        'H': H,
        'eigenvalues': m_evals,
        'U': U,
        'dm2_21': dm2_21, 'dm2_31': dm2_31, 'dm2_32': dm2_32,
        'R': R,
        'dE_12': dE_12, 'dE_23': dE_23,
        'V12_over_dE12': V12_over_dE12,
        'V23_over_dE23': V23_over_dE23,
        'ordering': ordering,
        **pmns,
    }


# ============================================================
# Module 5: Perturbative estimates for weak-mixing regime
# ============================================================
def perturbative_estimates(E_B1, E_B2_BCS, E_B3, V12, V23):
    """Compute perturbative (weak-mixing) estimates for R and sin^2(theta_13).

    Valid when V/dE << 1 (perturbative regime).

    In first-order perturbation theory for a tridiagonal 3x3:
        R ~ (V12/dE12)^2 * (dE23/dE12) / [(V23/dE23)^2 * (dE12/dE23)]
          = (V12 * dE23 / (V23 * dE12))^2

    Actually, for a 3x3 NNI (nearest-neighbor interaction):
        dm^2_21 ~ 2*E_B2 * V12^2 / dE_12  (perturbative shift)
        dm^2_32 ~ 2*E_B3 * V23^2 / dE_23 + ...

    More carefully, second-order perturbation theory:
        E'_1 = E_B1 - V12^2 / dE_12
        E'_2 = E_B2_BCS + V12^2/dE_12 - V23^2/dE_23
        E'_3 = E_B3 + V23^2/dE_23

    sin^2(theta_13) ~ (V12*V23 / (dE_12*dE_23))^2  [second order]
    """
    dE_12 = abs(E_B2_BCS - E_B1)
    dE_23 = abs(E_B3 - E_B2_BCS)

    # Mixing parameters
    eps_12 = V12 / dE_12 if dE_12 > 1e-15 else np.inf
    eps_23 = V23 / dE_23 if dE_23 > 1e-15 else np.inf

    # Second-order perturbed energies
    E1p = E_B1 - V12**2 / dE_12
    E2p = E_B2_BCS + V12**2 / dE_12 - V23**2 / dE_23
    E3p = E_B3 + V23**2 / dE_23

    dm2_21_pert = E2p**2 - E1p**2
    dm2_32_pert = E3p**2 - E2p**2
    R_pert = dm2_32_pert / dm2_21_pert if abs(dm2_21_pert) > 1e-30 else np.inf

    # sin^2(theta_13) ~ |V12*V23/(dE_12*dE_23)|^2  (indirect mixing)
    sin2_13_pert = (V12 * V23 / (dE_12 * dE_23))**2

    # theta_12 ~ V12/dE_12 (first order)
    sin_th12_pert = V12 / np.sqrt(V12**2 + dE_12**2) if dE_12 > 1e-15 else 1.0
    theta_12_pert = np.degrees(np.arcsin(sin_th12_pert))

    # theta_23 ~ V23/dE_23 (first order)
    sin_th23_pert = V23 / np.sqrt(V23**2 + dE_23**2) if dE_23 > 1e-15 else 1.0
    theta_23_pert = np.degrees(np.arcsin(sin_th23_pert))

    return {
        'eps_12': eps_12, 'eps_23': eps_23,
        'R_pert': R_pert,
        'sin2_13_pert': sin2_13_pert,
        'theta_12_pert': theta_12_pert,
        'theta_23_pert': theta_23_pert,
        'E1p': E1p, 'E2p': E2p, 'E3p': E3p,
        'dm2_21_pert': dm2_21_pert, 'dm2_32_pert': dm2_32_pert,
    }


# ============================================================
# Module 6: Main computation
# ============================================================
def main():
    print("=" * 80)
    print("SESSION 35 W3-A: WALL-LOCALIZED PMNS WITH CORRECTED SPINOR V")
    print("=" * 80)

    tau_values, eigenvalues, eigenvectors, V_pairing_frame, d34, old = load_data()
    tau_ref = 0.20

    # ============================================================
    # Part 0: Self-consistent BCS gap
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 0: SELF-CONSISTENT BCS GAP")
    print("=" * 75)

    Delta_BCS, g_BCS = compute_bcs_gap(V_B2B2_SPINOR, RHO_SMOOTH)
    print(f"  V(B2,B2) at phi=gap = {V_B2B2_SPINOR:.6f}")
    print(f"  rho_smooth = {RHO_SMOOTH:.2f}/mode")
    print(f"  g = V * rho = {g_BCS:.4f}")
    print(f"  Delta_BCS = W_B2 * exp(-1/g) = {Delta_BCS:.6f}")
    print(f"  Delta_BCS / W_B2 = {Delta_BCS/0.0579:.4f}")

    # Also compute gap with bare V for comparison
    Delta_bare, g_bare = compute_bcs_gap(0.05715, RHO_SMOOTH)
    print(f"\n  [Comparison] g_bare = {g_bare:.4f}, Delta_bare = {Delta_bare:.6f}")

    # ============================================================
    # Part 1: Corrected V vs old frame V -- comparison
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 1: CORRECTED SPINOR V vs OLD FRAME V COMPARISON")
    print("=" * 75)

    evals = eigenvalues[tau_ref]
    V_frame = V_pairing_frame[tau_ref]

    # Frame V couplings (WRONG -- what s33w3 used)
    n12_frame = np.linalg.norm(V_frame[8, 9:13])
    L2_eff_frame = V_frame[8, 9:13] / n12_frame
    n23_frame = np.linalg.norm(L2_eff_frame @ V_frame[9:13, 13:16])

    print(f"  {'Quantity':30s} | {'Frame V (s33w3)':>16s} | {'Spinor V (s34a)':>16s} | {'Ratio':>8s}")
    print(f"  {'-'*78}")
    print(f"  {'V(B1,B2)':30s} | {n12_frame:16.6f} | {V_B1B2_SPINOR:16.6f} | {n12_frame/V_B1B2_SPINOR:8.3f}")
    print(f"  {'V(B2,B3)':30s} | {n23_frame:16.6f} | {V_B2B3_SPINOR:16.6f} | {n23_frame/V_B2B3_SPINOR:8.3f}")
    print(f"  {'V_12/V_23':30s} | {n12_frame/n23_frame:16.4f} | {V_B1B2_SPINOR/V_B2B3_SPINOR:16.4f} | {'':>8s}")
    print(f"  {'V_12*V_23':30s} | {n12_frame*n23_frame:16.6f} | {V_B1B2_SPINOR*V_B2B3_SPINOR:16.6f} | {n12_frame*n23_frame/(V_B1B2_SPINOR*V_B2B3_SPINOR):8.3f}")

    # ============================================================
    # Part 2: Perturbative estimates (zero-cost diagnostic)
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 2: PERTURBATIVE (WEAK-MIXING) ESTIMATES")
    print("=" * 75)

    E_B1, E_B2, E_B3 = evals[8], evals[9], evals[13]
    dE_12_bare = abs(E_B2 - E_B1)
    dE_23_bare = abs(E_B3 - E_B2)

    # With BCS gap = Delta_BCS
    E_B2_bcs = np.sqrt(E_B2**2 + Delta_BCS**2)
    dE_12_bcs = abs(E_B2_bcs - E_B1)
    dE_23_bcs = abs(E_B3 - E_B2_bcs)

    pert_bare = perturbative_estimates(E_B1, E_B2, E_B3, V_B1B2_SPINOR, V_B2B3_SPINOR)
    pert_bcs = perturbative_estimates(E_B1, E_B2_bcs, E_B3, V_B1B2_SPINOR, V_B2B3_SPINOR)

    print(f"\n  Without BCS gap (Delta_B2 = 0):")
    print(f"    eps_12 = V12/dE12 = {pert_bare['eps_12']:.4f}")
    print(f"    eps_23 = V23/dE23 = {pert_bare['eps_23']:.4f}")
    print(f"    Regime: {'STRONG' if pert_bare['eps_12'] > 0.5 else 'WEAK' if pert_bare['eps_12'] < 0.2 else 'INTERMEDIATE'} mixing (1-2)")
    print(f"    Regime: {'STRONG' if pert_bare['eps_23'] > 0.5 else 'WEAK' if pert_bare['eps_23'] < 0.2 else 'INTERMEDIATE'} mixing (2-3)")
    print(f"    R_pert = {pert_bare['R_pert']:.4f}")
    print(f"    sin^2(theta_13)_pert = {pert_bare['sin2_13_pert']:.6f}")
    print(f"    theta_12_pert = {pert_bare['theta_12_pert']:.2f} deg")
    print(f"    theta_23_pert = {pert_bare['theta_23_pert']:.2f} deg")

    print(f"\n  With self-consistent BCS gap (Delta_B2 = {Delta_BCS:.6f}):")
    print(f"    E_B2_BCS = {E_B2_bcs:.8f}")
    print(f"    dE_12 = {dE_12_bcs:.6f} (bare: {dE_12_bare:.6f})")
    print(f"    dE_23 = {dE_23_bcs:.6f} (bare: {dE_23_bare:.6f})")
    print(f"    eps_12 = {pert_bcs['eps_12']:.4f}")
    print(f"    eps_23 = {pert_bcs['eps_23']:.4f}")
    print(f"    R_pert = {pert_bcs['R_pert']:.4f}")
    print(f"    sin^2(theta_13)_pert = {pert_bcs['sin2_13_pert']:.6f}")
    print(f"    theta_12_pert = {pert_bcs['theta_12_pert']:.2f} deg")
    print(f"    theta_23_pert = {pert_bcs['theta_23_pert']:.2f} deg")

    # ============================================================
    # Part 3: Full diagonalization scan over Delta_B2
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 3: CORRECTED WALL PMNS vs Delta_B2 (full diagonalization)")
    print("=" * 75)
    print(f"\n  Using V_12 = {V_B1B2_SPINOR:.6f}, V_23 = {V_B2B3_SPINOR:.6f}")
    print(f"  Self-consistent BCS gap: Delta_BCS = {Delta_BCS:.6f}")
    print(f"\n  {'Delta_B2':>10} | {'E_B2_BCS':>10} | {'dE_12':>10} | {'V12/dE12':>10} | "
          f"{'sin2_13':>10} | {'th12':>8} | {'th23':>8} | {'R':>10} | {'Order':>6}")
    print("  " + "-" * 105)

    results = []
    for Delta in DELTA_B2_SCAN:
        r = compute_corrected_wall_pmns(tau_ref, eigenvalues, Delta)
        results.append(r)

    # Print selected values
    print_deltas = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50]
    for r in results:
        if any(abs(r['Delta_B2'] - d) < 0.001 for d in print_deltas):
            print(f"  {r['Delta_B2']:10.4f} | {r['E_B2_BCS']:10.6f} | {r['dE_12']:10.6f} | "
                  f"{r['V12_over_dE12']:10.4f} | {r['sin2_13']:10.6f} | "
                  f"{r['theta_12']:8.2f} | {r['theta_23']:8.2f} | {r['R']:10.4f} | "
                  f"{r['ordering']:>6s}")

    # Highlight the self-consistent BCS point
    r_bcs = compute_corrected_wall_pmns(tau_ref, eigenvalues, Delta_BCS)
    print(f"\n  >>> SELF-CONSISTENT BCS POINT (Delta={Delta_BCS:.6f}):")
    print(f"      sin^2(theta_13) = {r_bcs['sin2_13']:.6f}  (NuFIT: 0.0220)")
    print(f"      theta_12 = {r_bcs['theta_12']:.2f} deg  (NuFIT: 33.44)")
    print(f"      theta_23 = {r_bcs['theta_23']:.2f} deg  (NuFIT: 49.2)")
    print(f"      R = {r_bcs['R']:.4f}  (NuFIT: 32.6)")
    print(f"      Ordering: {r_bcs['ordering']}")
    print(f"      V12/dE12 = {r_bcs['V12_over_dE12']:.4f}")
    print(f"      V23/dE23 = {r_bcs['V23_over_dE23']:.4f}")

    # ============================================================
    # Part 4: Comparison with old (frame V) results
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 4: COMPARISON WITH OLD FRAME-V RESULTS (s33w3)")
    print("=" * 75)

    old_R_vs_Delta = old['R_vs_Delta']
    old_s13_vs_Delta = old['sin2_13_vs_Delta']
    old_t23_vs_Delta = old['theta_23_vs_Delta']

    print(f"\n  {'Quantity':35s} | {'Old (frame V)':>15s} | {'New (spinor V)':>15s} | {'Change':>10s}")
    print(f"  {'-'*82}")

    # At Delta=0
    r0 = results[0]
    print(f"  {'sin2_13 at Delta=0':35s} | {float(old_s13_vs_Delta[0]):15.6f} | {r0['sin2_13']:15.6f} | {r0['sin2_13']/float(old_s13_vs_Delta[0]):10.3f}x")
    print(f"  {'theta_23 at Delta=0':35s} | {float(old_t23_vs_Delta[0]):15.2f} | {r0['theta_23']:15.2f} | {'':>10s}")
    print(f"  {'R at Delta=0':35s} | {float(old_R_vs_Delta[0]):15.4f} | {r0['R']:15.4f} | {r0['R']/float(old_R_vs_Delta[0]):10.3f}x")

    # Max R
    R_arr = np.array([r['R'] for r in results])
    R_max = np.max(R_arr)
    Delta_at_Rmax = DELTA_B2_SCAN[np.argmax(R_arr)]
    old_R_max = float(np.max(old_R_vs_Delta))

    print(f"  {'Max R':35s} | {old_R_max:15.4f} | {R_max:15.4f} | {R_max/old_R_max:10.3f}x")
    print(f"  {'Delta at max R':35s} | {'0.500':>15s} | {Delta_at_Rmax:15.4f} | {'':>10s}")

    # Min sin2_13
    s13_arr = np.array([r['sin2_13'] for r in results])
    s13_min = np.min(s13_arr)
    Delta_at_s13min = DELTA_B2_SCAN[np.argmin(s13_arr)]
    old_s13_min = float(np.min(old_s13_vs_Delta))

    print(f"  {'Min sin^2(theta_13)':35s} | {old_s13_min:15.6f} | {s13_min:15.6f} | {s13_min/old_s13_min:10.3f}x")

    # ============================================================
    # Part 5: Mixing regime analysis
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 5: MIXING REGIME ANALYSIS")
    print("=" * 75)

    # With corrected V, check mixing regime at bare and BCS points
    r_bare = results[0]
    print(f"\n  At Delta=0 (bare):")
    print(f"    V12/dE12 = {V_B1B2_SPINOR}/{dE_12_bare:.6f} = {V_B1B2_SPINOR/dE_12_bare:.4f}")
    print(f"    V23/dE23 = {V_B2B3_SPINOR}/{dE_23_bare:.6f} = {V_B2B3_SPINOR/dE_23_bare:.4f}")
    print(f"    Mixing regime: {'STRONG (V/dE > 1)' if V_B1B2_SPINOR/dE_12_bare > 1 else 'INTERMEDIATE (0.2 < V/dE < 1)' if V_B1B2_SPINOR/dE_12_bare > 0.2 else 'WEAK (V/dE < 0.2)'} for 1-2")
    print(f"    Mixing regime: {'STRONG (V/dE > 1)' if V_B2B3_SPINOR/dE_23_bare > 1 else 'INTERMEDIATE (0.2 < V/dE < 1)' if V_B2B3_SPINOR/dE_23_bare > 0.2 else 'WEAK (V/dE < 0.2)'} for 2-3")

    # Find transition points
    for i, r in enumerate(results):
        if r['V12_over_dE12'] < 1.0 and i > 0:
            print(f"\n  V12/dE12 drops below 1.0 at Delta_B2 = {r['Delta_B2']:.4f}")
            break
    for i, r in enumerate(results):
        if r['V12_over_dE12'] < 0.5 and i > 0:
            print(f"  V12/dE12 drops below 0.5 at Delta_B2 = {r['Delta_B2']:.4f}")
            break
    for i, r in enumerate(results):
        if r['V12_over_dE12'] < 0.2 and i > 0:
            print(f"  V12/dE12 drops below 0.2 at Delta_B2 = {r['Delta_B2']:.4f} -> WEAK MIXING REGIME")
            break

    # ============================================================
    # Part 6: What V_12/V_23 ratio is NEEDED for R=33?
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 6: REQUIRED V_12/V_23 FOR R = 33")
    print("=" * 75)

    # At the self-consistent BCS gap
    Delta_test = Delta_BCS
    E_B2_test = np.sqrt(E_B2**2 + Delta_test**2)
    dE_12_test = abs(E_B2_test - E_B1)
    dE_23_test = abs(E_B3 - E_B2_test)

    # Scan V12_factor while keeping V23 fixed
    best_R = 0
    best_factor = 0
    factor_scan = np.linspace(0.1, 50.0, 5000)
    R_vs_factor = []
    for f in factor_scan:
        V12_test = V_B1B2_SPINOR * f
        H_test = np.array([
            [E_B1,      V12_test,    0.0],
            [V12_test,  E_B2_test,   V_B2B3_SPINOR],
            [0.0,       V_B2B3_SPINOR, E_B3]
        ])
        m_test, _ = np.linalg.eigh(H_test)
        dm21 = m_test[1]**2 - m_test[0]**2
        R_test = (m_test[2]**2 - m_test[1]**2) / dm21 if abs(dm21) > 1e-30 else np.inf
        R_vs_factor.append(R_test)
        if abs(R_test - 33.0) < abs(best_R - 33.0):
            best_R = R_test
            best_factor = f

    R_vs_factor = np.array(R_vs_factor)

    # Find crossings of R=33
    crossings_33 = []
    for i in range(len(R_vs_factor) - 1):
        if (R_vs_factor[i] - 33) * (R_vs_factor[i+1] - 33) < 0:
            f_cross = factor_scan[i] + (33 - R_vs_factor[i]) * (factor_scan[i+1] - factor_scan[i]) / (R_vs_factor[i+1] - R_vs_factor[i])
            crossings_33.append(f_cross)

    print(f"\n  At Delta_BCS = {Delta_BCS:.6f}:")
    print(f"    dE_12 = {dE_12_test:.6f}, dE_23 = {dE_23_test:.6f}")
    print(f"    dE_23/dE_12 = {dE_23_test/dE_12_test:.4f}")
    print(f"    Current V12/V23 = {V_B1B2_SPINOR/V_B2B3_SPINOR:.4f}")
    print(f"    Current R = {r_bcs['R']:.4f}")
    print(f"    Best R achievable by V12 enhancement: {best_R:.4f} at factor {best_factor:.2f}")

    if crossings_33:
        print(f"    R = 33 achievable at V12_factor = {crossings_33[0]:.4f}")
        print(f"    Required V12 = {V_B1B2_SPINOR * crossings_33[0]:.4f}")
        print(f"    Required V12/V23 = {V_B1B2_SPINOR * crossings_33[0] / V_B2B3_SPINOR:.4f}")
    else:
        print(f"    R = 33 NOT achievable in factor range [0.1, 50]")
        print(f"    Maximum R in scan: {R_vs_factor.max():.4f}")

    # ============================================================
    # Part 7: What V_23 reduction gives R=33?
    # ============================================================
    print("\n  Alternative: reducing V23 while keeping V12 fixed:")
    best_R_v23 = 0
    best_f23 = 0
    f23_scan = np.linspace(0.001, 2.0, 5000)
    R_vs_f23 = []
    for f in f23_scan:
        V23_test = V_B2B3_SPINOR * f
        H_test = np.array([
            [E_B1,           V_B1B2_SPINOR,  0.0],
            [V_B1B2_SPINOR,  E_B2_test,      V23_test],
            [0.0,            V23_test,        E_B3]
        ])
        m_test, _ = np.linalg.eigh(H_test)
        dm21 = m_test[1]**2 - m_test[0]**2
        R_test = (m_test[2]**2 - m_test[1]**2) / dm21 if abs(dm21) > 1e-30 else np.inf
        R_vs_f23.append(R_test)
        if abs(R_test - 33.0) < abs(best_R_v23 - 33.0):
            best_R_v23 = R_test
            best_f23 = f

    R_vs_f23 = np.array(R_vs_f23)

    crossings_33_v23 = []
    for i in range(len(R_vs_f23) - 1):
        if (R_vs_f23[i] - 33) * (R_vs_f23[i+1] - 33) < 0:
            f_cross = f23_scan[i] + (33 - R_vs_f23[i]) * (f23_scan[i+1] - f23_scan[i]) / (R_vs_f23[i+1] - R_vs_f23[i])
            crossings_33_v23.append(f_cross)

    if crossings_33_v23:
        print(f"    R = 33 at V23_factor = {crossings_33_v23[0]:.6f}")
        print(f"    Required V23 = {V_B2B3_SPINOR * crossings_33_v23[0]:.6f}")
    else:
        print(f"    R = 33 NOT achievable by V23 reduction alone")
        print(f"    Closest R = {best_R_v23:.4f} at V23_factor = {best_f23:.4f}")

    # ============================================================
    # Part 8: Scan across multiple tau values
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 8: CORRECTED PMNS AT MULTIPLE TAU VALUES")
    print("=" * 75)
    print(f"\n  Delta_BCS = {Delta_BCS:.6f}")
    print(f"  {'tau':>6} | {'E_B1':>10} | {'E_B2':>10} | {'E_B3':>10} | {'dE12':>10} | {'dE23':>10} | "
          f"{'sin2_13':>10} | {'th23':>8} | {'R':>10}")
    print("  " + "-" * 105)

    tau_results = {}
    for tau in [0.10, 0.15, 0.20, 0.25, 0.30]:
        if tau in eigenvalues:
            r_tau = compute_corrected_wall_pmns(tau, eigenvalues, Delta_BCS)
            tau_results[tau] = r_tau
            print(f"  {tau:6.2f} | {r_tau['E_B1']:10.6f} | {r_tau['E_B2_bare']:10.6f} | "
                  f"{r_tau['E_B3']:10.6f} | {r_tau['dE_12']:10.6f} | {r_tau['dE_23']:10.6f} | "
                  f"{r_tau['sin2_13']:10.6f} | {r_tau['theta_23']:8.2f} | {r_tau['R']:10.4f}")

    # ============================================================
    # Part 9: Gate verdicts
    # ============================================================
    print("\n" + "=" * 80)
    print("GATE VERDICTS: PMNS-CORRECTED-35")
    print("=" * 80)

    # Evaluate at self-consistent BCS point
    print(f"\n  Evaluation point: tau = {tau_ref}, Delta_B2 = {Delta_BCS:.6f} (self-consistent)")

    # Also check across all Delta_B2
    any_pass = False
    pass_ranges = {'theta_23': [], 'sin2_13': [], 'R': []}

    for r in results:
        t23_pass = 35 <= r['theta_23'] <= 55
        s13_pass = 0.01 <= r['sin2_13'] <= 0.05
        R_pass = 10 <= r['R'] <= 100

        if t23_pass:
            pass_ranges['theta_23'].append(r['Delta_B2'])
        if s13_pass:
            pass_ranges['sin2_13'].append(r['Delta_B2'])
        if R_pass:
            pass_ranges['R'].append(r['Delta_B2'])
        if t23_pass and s13_pass and R_pass:
            any_pass = True

    # Gate sub-criteria
    t23_at_bcs = r_bcs['theta_23']
    s13_at_bcs = r_bcs['sin2_13']
    R_at_bcs = r_bcs['R']

    print(f"\n  Sub-criterion 1: theta_23 in [35, 55] deg")
    print(f"    Value at BCS point: {t23_at_bcs:.2f} deg")
    if 35 <= t23_at_bcs <= 55:
        print(f"    Verdict: PASS")
    else:
        print(f"    Verdict: FAIL (outside window)")
    if pass_ranges['theta_23']:
        print(f"    Passes in Delta_B2 range: [{min(pass_ranges['theta_23']):.4f}, {max(pass_ranges['theta_23']):.4f}]")

    print(f"\n  Sub-criterion 2: sin^2(theta_13) in [0.01, 0.05]")
    print(f"    Value at BCS point: {s13_at_bcs:.6f}")
    if 0.01 <= s13_at_bcs <= 0.05:
        print(f"    Verdict: PASS")
    else:
        print(f"    Verdict: FAIL (min across scan: {np.min(s13_arr):.6f})")
    if pass_ranges['sin2_13']:
        print(f"    Passes in Delta_B2 range: [{min(pass_ranges['sin2_13']):.4f}, {max(pass_ranges['sin2_13']):.4f}]")

    print(f"\n  Sub-criterion 3: R in [10, 100]")
    print(f"    Value at BCS point: {R_at_bcs:.4f}")
    if 10 <= R_at_bcs <= 100:
        print(f"    Verdict: PASS")
    else:
        print(f"    Verdict: FAIL (max across scan: {R_max:.4f})")
    if pass_ranges['R']:
        print(f"    Passes in Delta_B2 range: [{min(pass_ranges['R']):.4f}, {max(pass_ranges['R']):.4f}]")

    # Overall gate
    bcs_all_pass = (35 <= t23_at_bcs <= 55) and (0.01 <= s13_at_bcs <= 0.05) and (10 <= R_at_bcs <= 100)
    print(f"\n  OVERALL GATE PMNS-CORRECTED-35:")
    if bcs_all_pass:
        print(f"    PASS at self-consistent BCS point")
    elif any_pass:
        print(f"    PASS at some Delta_B2 (not at self-consistent point)")
    else:
        print(f"    FAIL -- no Delta_B2 satisfies all three criteria simultaneously")
        # Detail which criteria fail
        if not pass_ranges['theta_23']:
            print(f"      theta_23 NEVER in [35, 55] (range: [{np.min([r['theta_23'] for r in results]):.2f}, {np.max([r['theta_23'] for r in results]):.2f}])")
        if not pass_ranges['sin2_13']:
            print(f"      sin^2(theta_13) NEVER in [0.01, 0.05] (range: [{np.min(s13_arr):.6f}, {np.max(s13_arr):.6f}])")
        if not pass_ranges['R']:
            print(f"      R NEVER in [10, 100] (range: [{np.min(R_arr):.4f}, {np.max(R_arr):.4f}])")

    # ============================================================
    # Part 10: Assessment -- what constrains R?
    # ============================================================
    print("\n" + "=" * 75)
    print("PART 10: WHAT CONSTRAINS R -- STRUCTURAL ANALYSIS")
    print("=" * 75)

    # The ratio V_12/V_23 is locked by Schur orthogonality
    # V_12/V_23 ~ 3.5 from Session 34
    # For R=33, we need:
    # In the weak mixing limit (V/dE << 1):
    #   R ~ (dE_23/dE_12) * [1 + 2*(V12^2/dE_12^2 - V23^2/dE_23^2)/(dE_23/dE_12 - 1)]
    # The dominant factor is dE_23/dE_12 (the bare energy gap ratio)

    print(f"\n  Bare energy gaps:")
    print(f"    dE_12 (B2-B1) = {dE_12_bare:.6f}")
    print(f"    dE_23 (B3-B2) = {dE_23_bare:.6f}")
    print(f"    dE_23/dE_12 = {dE_23_bare/dE_12_bare:.4f}")
    print(f"\n  This ratio sets the STRUCTURAL CEILING for R:")
    print(f"    In the weak mixing limit, R -> dE_23/dE_12 * (E_B3/E_B2) = {dE_23_bare/dE_12_bare * E_B3/E_B2:.4f}")
    print(f"    R CANNOT exceed ~{dE_23_bare/dE_12_bare * E_B3/E_B2:.1f} at any coupling strength")
    print(f"    with fixed bulk eigenvalues")

    # Check if BCS gap helps by increasing dE_12 (pushing B2 up toward B3)
    print(f"\n  BCS gap effect on hierarchy:")
    print(f"    Delta_BCS = {Delta_BCS:.6f}")
    print(f"    dE_12 with BCS: {dE_12_bcs:.6f} (ratio {dE_12_bcs/dE_12_bare:.3f}x)")
    print(f"    dE_23 with BCS: {dE_23_bcs:.6f} (ratio {dE_23_bcs/dE_23_bare:.3f}x)")
    print(f"    BCS REDUCES the gap hierarchy (dE_23/dE_12 decreases)")
    print(f"    BCS makes R WORSE, not better")

    # ============================================================
    # Save results
    # ============================================================
    save_dict = {
        'tau_ref': tau_ref,
        'Delta_B2_scan': DELTA_B2_SCAN,
        'Delta_BCS_selfconsistent': Delta_BCS,
        'g_BCS': g_BCS,
        'V_B1B2_spinor': V_B1B2_SPINOR,
        'V_B2B3_spinor': V_B2B3_SPINOR,
        'V_B2B2_spinor': V_B2B2_SPINOR,
        'rho_smooth': RHO_SMOOTH,
        'R_vs_Delta': np.array([r['R'] for r in results]),
        'sin2_13_vs_Delta': np.array([r['sin2_13'] for r in results]),
        'theta_12_vs_Delta': np.array([r['theta_12'] for r in results]),
        'theta_23_vs_Delta': np.array([r['theta_23'] for r in results]),
        'V12_over_dE12_vs_Delta': np.array([r['V12_over_dE12'] for r in results]),
        'dE_12_vs_Delta': np.array([r['dE_12'] for r in results]),
        'dm2_21_vs_Delta': np.array([r['dm2_21'] for r in results]),
        'dm2_32_vs_Delta': np.array([r['dm2_32'] for r in results]),
        'E_B2_BCS_vs_Delta': np.array([r['E_B2_BCS'] for r in results]),
        'E_B1': E_B1, 'E_B2': E_B2, 'E_B3': E_B3,
        'R_at_BCS': R_at_bcs,
        'sin2_13_at_BCS': s13_at_bcs,
        'theta_23_at_BCS': t23_at_bcs,
        'theta_12_at_BCS': r_bcs['theta_12'],
        # Old frame V results for comparison
        'old_V12_frame': n12_frame,
        'old_V23_frame': n23_frame,
        'old_R_max': old_R_max,
        'old_sin2_13_min': old_s13_min,
        # Factor scans
        'factor_scan': factor_scan,
        'R_vs_V12_factor': R_vs_factor,
        'f23_scan': f23_scan,
        'R_vs_V23_factor': R_vs_f23,
    }
    np.savez(OUTPUT_NPZ, **save_dict)
    print(f"\nResults saved to {OUTPUT_NPZ}")

    # ============================================================
    # Plot
    # ============================================================
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Session 35 W3-A: PMNS with Corrected Spinor V\n'
                 r'V$_{12}$ = %.4f, V$_{23}$ = %.4f, $\rho$ = %.1f, $\Delta_{\rm BCS}$ = %.4f'
                 % (V_B1B2_SPINOR, V_B2B3_SPINOR, RHO_SMOOTH, Delta_BCS),
                 fontsize=13, fontweight='bold')

    Delta_arr = DELTA_B2_SCAN
    R_arr_plot = np.array([r['R'] for r in results])
    s13_arr_plot = np.array([r['sin2_13'] for r in results])
    t12_arr_plot = np.array([r['theta_12'] for r in results])
    t23_arr_plot = np.array([r['theta_23'] for r in results])
    ratio_arr_plot = np.array([r['V12_over_dE12'] for r in results])

    # Panel 1: R vs Delta_B2
    ax = axes[0, 0]
    ax.plot(Delta_arr, R_arr_plot, 'b-', linewidth=2, label='Corrected (spinor V)')
    ax.plot(old['Delta_B2_scan'], old['R_vs_Delta'], 'b--', linewidth=1, alpha=0.5, label='Old (frame V)')
    ax.axhspan(29, 37, alpha=0.1, color='green', label='PDG [29, 37]')
    ax.axhspan(10, 100, alpha=0.05, color='orange', label='Gate [10, 100]')
    ax.axhline(32.6, color='green', linestyle=':', alpha=0.5)
    ax.axvline(Delta_BCS, color='red', linestyle=':', alpha=0.7, label=r'$\Delta_{\rm BCS}$')
    ax.set_xlabel(r'$\Delta_{B2}$ (BCS gap)')
    ax.set_ylabel(r'$R = \Delta m^2_{32}/\Delta m^2_{21}$')
    ax.set_title('R vs BCS Gap')
    ax.legend(fontsize=7, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, max(5, R_arr_plot.max() * 1.2))

    # Panel 2: sin^2(theta_13) vs Delta_B2
    ax = axes[0, 1]
    ax.plot(Delta_arr, s13_arr_plot, 'r-', linewidth=2, label='Corrected')
    ax.plot(old['Delta_B2_scan'], old['sin2_13_vs_Delta'], 'r--', linewidth=1, alpha=0.5, label='Old (frame V)')
    ax.axhspan(0.01, 0.05, alpha=0.1, color='orange', label='Gate [0.01, 0.05]')
    ax.axhspan(0.020, 0.024, alpha=0.15, color='green', label='PDG 3$\\sigma$')
    ax.axhline(0.0220, color='green', linestyle=':', alpha=0.5)
    ax.axvline(Delta_BCS, color='red', linestyle=':', alpha=0.7)
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$\sin^2(\theta_{13})$')
    ax.set_title(r'$\sin^2(\theta_{13})$ vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: theta_23 vs Delta_B2
    ax = axes[0, 2]
    ax.plot(Delta_arr, t23_arr_plot, 'm-', linewidth=2, label='Corrected')
    ax.plot(old['Delta_B2_scan'], old['theta_23_vs_Delta'], 'm--', linewidth=1, alpha=0.5, label='Old (frame V)')
    ax.axhspan(35, 55, alpha=0.05, color='orange', label='Gate [35, 55]')
    ax.axhspan(40.1, 51.7, alpha=0.15, color='green', label='PDG 3$\\sigma$')
    ax.axhline(49.2, color='green', linestyle=':', alpha=0.5)
    ax.axvline(Delta_BCS, color='red', linestyle=':', alpha=0.7)
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$\theta_{23}$ (deg)')
    ax.set_title(r'$\theta_{23}$ vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 4: V12/dE12 mixing ratio
    ax = axes[1, 0]
    ax.plot(Delta_arr, ratio_arr_plot, 'k-', linewidth=2, label='Corrected')
    old_ratio = old.get('V12_over_dE12_vs_Delta', None)
    if old_ratio is not None:
        ax.plot(old['Delta_B2_scan'], old_ratio, 'k--', linewidth=1, alpha=0.5, label='Old (frame V)')
    ax.axhline(1.0, color='red', linestyle=':', label='Strong/weak')
    ax.axhline(0.2, color='orange', linestyle=':', label='Perturbative')
    ax.axvline(Delta_BCS, color='red', linestyle=':', alpha=0.7)
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel(r'$V_{12}/\delta E_{12}$')
    ax.set_title('Mixing Regime vs BCS Gap')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 5: Energy levels
    ax = axes[1, 1]
    E_B2_BCS_arr = np.array([r['E_B2_BCS'] for r in results])
    ax.plot(Delta_arr, [E_B1]*len(Delta_arr), 'r--', linewidth=1.5, label='B1')
    ax.plot(Delta_arr, E_B2_BCS_arr, 'b-', linewidth=2, label=r'B2$^{\rm BCS}$')
    ax.plot(Delta_arr, [E_B3]*len(Delta_arr), 'g--', linewidth=1.5, label='B3')
    ax.axvline(Delta_BCS, color='red', linestyle=':', alpha=0.7, label=r'$\Delta_{\rm BCS}$')
    ax.set_xlabel(r'$\Delta_{B2}$')
    ax.set_ylabel('Energy level')
    ax.set_title('Branch Energy Levels')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 6: R vs V12 enhancement factor
    ax = axes[1, 2]
    ax.plot(factor_scan[:500], R_vs_factor[:500], 'b-', linewidth=2)
    ax.axhspan(10, 100, alpha=0.05, color='orange', label='Gate')
    ax.axhspan(29, 37, alpha=0.15, color='green', label='PDG')
    ax.axhline(33, color='green', linestyle=':', alpha=0.5)
    ax.axvline(1.0, color='red', linestyle=':', alpha=0.5, label='Current V12')
    ax.set_xlabel(r'V$_{12}$ enhancement factor')
    ax.set_ylabel(r'$R$')
    ax.set_title(r'R vs V$_{12}$ Enhancement (V$_{23}$ fixed)')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, min(100, R_vs_factor[:500].max() * 1.2))

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Plot saved to {OUTPUT_PNG}")

    return results, r_bcs


if __name__ == '__main__':
    results, r_bcs = main()
