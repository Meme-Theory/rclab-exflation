"""
Session 33b TRAP-1: 5-Band BdG for B1+B2 at Domain Wall (v3 -- FULL KERNEL)
============================================================================
THE EXISTENTIAL GATE for the mechanism chain.

CRITICAL CORRECTION (v3):
  Session 23a K-1e used ONLY C^2 generators (a=3,4,5,6) for the Kosmann
  pairing kernel: V_nm = sum_{a in C^2} |<n|K_a|m>|^2.
  This gives V(B2,B2) = 0 EXACTLY (by U(1) charge conservation on C^2).

  The FULL Kosmann pairing kernel uses ALL 8 generators:
    V_nm = sum_{a=0..7} |<n|K_a|m>|^2

  In the U(2) branch-adapted basis (from A_antisym matrices):
    - SU(2) generators (a=0,1,2): V(B2,B2) off-diag = 0.037
    - U(1) generator (a=7): V(B2,B2) off-diag = 0.250 (doublet structure)
    - Combined: V(B2,B2) off-diag max = 0.287

  The K-1e closure "V(gap,gap) = 0 EXACTLY" is a C^2-generator artifact.

Physics:
  - B2 modes trapped at walls via van Hove singularity (W-32b PASS 1.9-3.2x)
  - V(B2,B2) from SU(2)+U(1) generators = 0.287 (off-diagonal max)
  - V(B1,B2) from C^2 generators = 0.124-0.168 (shell-crossing channel)
  - Both channels contribute to BCS pairing at the wall
  - Multi-sector DOS boost from SECT-33a UNIVERSAL
  - Impedance correction 1/(1-R) = 1.56 (CT-4)
  - A_antisym basis ordering: B3(0,1,2), B2(3,4,5,6), B1(7)

Gate TRAP-33b (EXISTENTIAL):
  PASS:        Delta_wall > 0 AND M_max > 1.0
  STRONG PASS: M_max > 3.0
  FAIL:        M_max < 1.0 at all physical mu values

Author: bap (baptista-spacetime-analyst), Session 33b
Date: 2026-03-06
"""

import os
import time
import numpy as np
from scipy.linalg import eigh
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Branch indices in the A_antisym 8x8 basis (positive eigenvalue sector)
# Ordering: B3 = {0,1,2}, B2 = {3,4,5,6}, B1 = {7}
B3_IDX = np.array([0, 1, 2])
B2_IDX = np.array([3, 4, 5, 6])
B1_IDX = np.array([7])

# Physical constants
IMPEDANCE_FACTOR = 1.56  # CT-4: 1/(1-R), R = 0.36
E_KIN_ETA005 = 0.0095    # Modulus kinetic energy at eta = 0.05
DELTA_CRIT_THIN = 0.07   # Thin-wall Delta_crit (W3-R2-F)
ETA_REG = 0.001           # Regulator floor for |xi| as fraction of lambda_min


# ======================================================================
#  Data Loading
# ======================================================================

def load_all_data():
    """Load all required .npz files."""
    kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)
    wall_dos = np.load(os.path.join(SCRIPT_DIR, 's32b_wall_dos.npz'),
                       allow_pickle=True)
    sector = np.load(os.path.join(SCRIPT_DIR, 's33a_landau_sector.npz'),
                     allow_pickle=True)
    return kosmann, wall_dos, sector


# ======================================================================
#  Pairing Kernel (FULL 8-generator)
# ======================================================================

def build_full_V_8x8(kosmann, tau_idx):
    """Build V_nm = sum_{a=0..7} |<n|K_a|m>|^2 from A_antisym matrices.

    Returns the 8x8 matrix in the U(2) branch-adapted basis.
    This is the CORRECT full Kosmann pairing kernel.
    """
    V = np.zeros((8, 8))
    for a in range(8):
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        V += np.abs(A) ** 2
    return V


def build_V_decomposed(kosmann, tau_idx):
    """Build V decomposed by generator type: C^2, SU(2), U(1).

    Returns V_C2, V_SU2, V_U1, V_full (all 8x8).
    """
    V_C2 = np.zeros((8, 8))
    V_SU2 = np.zeros((8, 8))
    V_U1 = np.zeros((8, 8))
    for a in range(8):
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        Vg = np.abs(A) ** 2
        if a in [3, 4, 5, 6]:
            V_C2 += Vg
        elif a in [0, 1, 2]:
            V_SU2 += Vg
        else:
            V_U1 += Vg
    return V_C2, V_SU2, V_U1, V_C2 + V_SU2 + V_U1


def get_branch_eigenvalues(kosmann, tau_idx):
    """Get eigenvalues in the branch-adapted basis ordering.

    A_antisym basis: B3(0,1,2), B2(3,4,5,6), B1(7)
    Positive eigenvalues sorted ascending: B1(0.819), B2(0.845 x4), B3(0.978 x3)
    """
    evals_all = kosmann[f'eigenvalues_{tau_idx}']
    pos_evals = np.sort(evals_all[evals_all > 0])
    # Map to A_antisym ordering: B3, B2, B1
    E_branch = np.zeros(8)
    E_branch[0:3] = pos_evals[5:8]   # B3 = highest 3
    E_branch[3:7] = pos_evals[1:5]   # B2 = middle 4
    E_branch[7] = pos_evals[0]       # B1 = lowest 1
    return E_branch


# ======================================================================
#  Multi-Sector DOS Enhancement
# ======================================================================

def compute_multi_sector_factor(sector):
    """Compute multi-sector DOS enhancement factor from SECT-33a.

    SECT-33a UNIVERSAL: all sectors have B2-analog minima within
    delta_tau = 0.004 of the singlet. Non-singlet d2 up to 13x singlet.

    The wall-integrated DOS per sector scales as:
      N_eff ~ deg * sqrt(d2) * integral[1/sqrt(|tau - tau_min|)] ~ deg * sqrt(d2 * w_wall)

    where w_wall is the wall width. Higher d2 means a SHARPER fold,
    giving LESS integrated DOS per mode but MORE curvature. The integrated
    number of states in the van Hove peak is:
      N_vH ~ deg / sqrt(d2) (for fixed wall width)

    because the fold is narrower in tau-space.

    Conservative estimate: each non-singlet sector contributes
      factor = (deg_pq / deg_00) * sqrt(d2_00 / d2_pq) * suppression(xi)
    """
    d2_00 = float(sector['sector_0_0_cluster_d2'].flat[0])
    deg_00 = int(sector['sector_0_0_cluster_deg'].flat[0])
    lambda_00 = float(sector['sector_0_0_cluster_lambda'].flat[0])

    d2_01 = float(sector['sector_0_1_cluster_d2'].flat[0])
    deg_01 = int(sector['sector_0_1_cluster_deg'].flat[0])
    lambda_01 = float(sector['sector_0_1_cluster_lambda'].flat[0])

    d2_10 = float(sector['sector_1_0_cluster_d2'].flat[0])
    deg_10 = int(sector['sector_1_0_cluster_deg'].flat[0])
    lambda_10 = float(sector['sector_1_0_cluster_lambda'].flat[0])

    # van Hove integrated DOS ratio: each sector contributes
    # N_vH ~ deg / sqrt(d2) modes in the fold region
    # Relative to singlet: factor = (deg/deg_00) * sqrt(d2_00/d2)
    f_01 = (deg_01 / deg_00) * np.sqrt(d2_00 / d2_01)
    f_10 = (deg_10 / deg_00) * np.sqrt(d2_00 / d2_10)

    # Pairing suppression: non-singlet eigenvalues are at lambda ~ 1.08
    # vs singlet at 0.845. The pairing effectiveness for cross-sector
    # modes is suppressed by 1/(2|xi_cross|) vs 1/(2|xi_singlet|).
    # BUT: within each sector, the pairing is self-contained.
    # The multi-sector enhancement adds INDEPENDENT BCS channels in parallel.
    # Each sector pairs within itself. The total condensation energy sums.

    # Conservative: assume no cross-sector pairing (each sector independent).
    # The effective wall DOS for the gap equation is the singlet contribution
    # only, but the condensation energy and trapping force sum over all sectors.
    # For the Thouless criterion within the singlet, the multi-sector
    # contribution enters as additional spectral weight at the same tau.

    # Most conservative: the non-singlet modes at the wall contribute
    # additional spectral weight that enters the GAP EQUATION integral.
    # Their eigenvalue xi differs from singlet mu, so they contribute
    # with suppression ~ (shell_gap / |xi_cross|).

    shell_gap = 0.026  # B2-B1 in singlet
    xi_cross = abs(lambda_01 - lambda_00)  # eigenvalue separation
    suppression = min(shell_gap / xi_cross, 1.0) if xi_cross > 0 else 1.0

    total_factor = 1.0 + (f_01 + f_10) * suppression

    results = {
        'factor': total_factor,
        'f_01': f_01, 'f_10': f_10,
        'suppression': suppression,
        'deg_00': deg_00, 'deg_01': deg_01, 'deg_10': deg_10,
        'd2_00': d2_00, 'd2_01': d2_01, 'd2_10': d2_10,
        'lambda_00': lambda_00, 'lambda_01': lambda_01,
        'xi_cross': xi_cross,
    }
    return results


# ======================================================================
#  Thouless Criterion (Linearized BdG)
# ======================================================================

def thouless_5x5(V_8x8, E_branch, mu, rho_B2, rho_B1=1.0):
    """Linearized BdG in the 5-mode B1+B2 subspace.

    M_nm = V_nm / (2 * |xi_m|)   for mode m
    with V weighted by per-mode DOS: V_eff_nm = V_nm * sqrt(rho_n * rho_m)
    (geometric mean weighting for DOS-enhanced pairing).

    Actually the correct Thouless formulation is:
      M_nm = V_nm * rho_m / (2 * |xi_m|)
    where rho_m is the effective DOS per mode at the wall.

    Parameters:
        V_8x8: full 8x8 pairing matrix in branch basis
        E_branch: 8 eigenvalues in branch ordering
        mu: chemical potential
        rho_B2: effective DOS per B2 mode (wall-enhanced)
        rho_B1: effective DOS for B1 mode (default 1.0 = bulk)
    """
    # Extract B1+B2 subspace: indices [3,4,5,6,7] in 8x8
    idx = np.concatenate([B2_IDX, B1_IDX])  # [3,4,5,6,7]
    V_sub = V_8x8[np.ix_(idx, idx)]  # 5x5
    E_sub = E_branch[idx]  # 5 eigenvalues

    xi = E_sub - mu
    lambda_min = np.min(np.abs(E_sub))
    eta = max(ETA_REG * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    # Per-mode DOS weights
    rho = np.array([rho_B2] * 4 + [rho_B1])

    # Build M: M_nm = V_nm * rho_m / (2 * |xi_m|)
    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_sub[:, m] * rho[m] / (2.0 * abs_xi[m])

    # Symmetrize (should already be nearly symmetric)
    # Actually M is NOT symmetric in general: V is symmetric but rho/|xi| differ per mode.
    # The Thouless criterion uses the max eigenvalue of M (not necessarily symmetric).
    # For the linearized gap equation Delta = M @ Delta, we need eigenvalues of M.

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))

    return M_max, M_evals, M, V_sub, E_sub


def thouless_8x8(V_8x8, E_branch, mu, rho_B2, rho_B1=1.0, rho_B3=1.0):
    """Full 8x8 Thouless criterion including B3.

    Same as thouless_5x5 but uses all 8 modes.
    """
    xi = E_branch - mu
    lambda_min = np.min(np.abs(E_branch))
    eta = max(ETA_REG * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    rho = np.zeros(8)
    rho[B3_IDX] = rho_B3
    rho[B2_IDX] = rho_B2
    rho[B1_IDX] = rho_B1

    M = np.zeros((8, 8))
    for m in range(8):
        M[:, m] = V_8x8[:, m] * rho[m] / (2.0 * abs_xi[m])

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))
    return M_max, M_evals


# ======================================================================
#  Self-Consistent BdG
# ======================================================================

def selfconsistent_5x5(V_8x8, E_branch, mu, rho_B2, rho_B1=1.0,
                       max_iter=100000, tol=1e-13, Delta0_scale=0.01):
    """Self-consistent gap equation in B1+B2 subspace."""
    idx = np.concatenate([B2_IDX, B1_IDX])
    V_sub = V_8x8[np.ix_(idx, idx)]
    E_sub = E_branch[idx]
    xi = E_sub - mu
    rho = np.array([rho_B2] * 4 + [rho_B1])

    V_eff = V_sub * rho[np.newaxis, :]

    lambda_min = np.min(np.abs(E_sub))
    Delta = np.ones(5) * Delta0_scale * lambda_min

    for k in range(max_iter):
        denom = 2.0 * np.sqrt(xi**2 + Delta**2)
        Delta_new = V_eff @ (Delta / denom)

        if np.linalg.norm(Delta) > 1e-15:
            rel_change = np.linalg.norm(Delta_new - Delta) / np.linalg.norm(Delta)
        else:
            rel_change = np.linalg.norm(Delta_new - Delta)

        Delta = Delta_new
        if rel_change < tol:
            return Delta, True, k + 1
        if np.linalg.norm(Delta) < 1e-30:
            return Delta, True, k + 1

    return Delta, False, max_iter


# ======================================================================
#  Main Computation
# ======================================================================

def run_trap1():
    print("=" * 80)
    print("Session 33b: TRAP-1 -- 5-Band BdG at Domain Wall (v3 FULL KERNEL)")
    print("THE EXISTENTIAL GATE")
    print("=" * 80)
    print()

    t0 = time.time()
    kosmann, wall_dos, sector = load_all_data()
    print(f"Data loaded in {time.time()-t0:.1f}s")

    # ==================================================================
    # STEP 1: Pairing kernel structure (FULL vs C^2-only)
    # ==================================================================
    print()
    print("=" * 70)
    print("STEP 1: Pairing Kernel -- FULL 8-Generator vs C^2-Only")
    print("=" * 70)
    print()

    tau_idx = 3  # tau = 0.20 (near dump point)
    V_C2, V_SU2, V_U1, V_full = build_V_decomposed(kosmann, tau_idx)
    E_branch = get_branch_eigenvalues(kosmann, tau_idx)

    print(f"Eigenvalues (branch basis): B3={E_branch[0]:.6f}, "
          f"B2={E_branch[3]:.6f}, B1={E_branch[7]:.6f}")
    print(f"Shell gap (B2-B1): {E_branch[3] - E_branch[7]:.6f}")
    print()

    # B2-B2 block comparison
    V_B2B2_C2 = V_C2[np.ix_(B2_IDX, B2_IDX)]
    V_B2B2_SU2 = V_SU2[np.ix_(B2_IDX, B2_IDX)]
    V_B2B2_U1 = V_U1[np.ix_(B2_IDX, B2_IDX)]
    V_B2B2_full = V_full[np.ix_(B2_IDX, B2_IDX)]

    print("V(B2,B2) by generator type:")
    print(f"  C^2 (a=3..6):  max = {np.max(V_B2B2_C2):.2e}  << Session 23a used ONLY this")
    print(f"  SU(2) (a=0..2): max = {np.max(V_B2B2_SU2):.6f}")
    print(f"  U(1) (a=7):     max = {np.max(V_B2B2_U1):.6f}")
    print(f"  FULL:            max = {np.max(V_B2B2_full):.6f}")
    print()

    print("V(B2,B2) FULL matrix [4x4]:")
    np.set_printoptions(precision=6, suppress=True, linewidth=100)
    print(V_B2B2_full)
    print()

    # B2-B2 doublet structure from U(1)
    print("U(1) doublet structure: V_U1(B2,B2) =")
    print(V_B2B2_U1)
    print("  B2 modes pair as (3,4) and (5,6) doublets under U(1).")
    print()

    # B1-B2 coupling
    V_B1B2 = V_full[np.ix_(B1_IDX, B2_IDX)]
    print(f"V(B1,B2) [full]: {V_B1B2.flatten()}")
    print(f"V(B1,B2) mean = {np.mean(V_B1B2):.6f}")
    print()

    # Full 5x5 B1+B2 sub-matrix
    idx_5 = np.concatenate([B2_IDX, B1_IDX])
    V_5x5 = V_full[np.ix_(idx_5, idx_5)]
    print("5x5 V_sub (B2_0, B2_1, B2_2, B2_3, B1):")
    print(V_5x5)
    print()

    # Bulk reference (no wall enhancement)
    M_max_bulk_C2, _, _, _, _ = thouless_5x5(V_C2, E_branch, 0.0, 1.0, 1.0)
    M_max_bulk_full, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0, 1.0, 1.0)
    print(f"Bulk M_max (mu=0, no wall):")
    print(f"  C^2-only kernel: {M_max_bulk_C2:.6f}  (Session 23a K-1e)")
    print(f"  Full kernel:     {M_max_bulk_full:.6f}")
    print(f"  Enhancement:     {M_max_bulk_full/max(M_max_bulk_C2,1e-10):.2f}x")
    print()

    # ==================================================================
    # STEP 2: Multi-sector DOS enhancement
    # ==================================================================
    print("=" * 70)
    print("STEP 2: Multi-Sector DOS Enhancement (SECT-33a)")
    print("=" * 70)
    print()

    ms = compute_multi_sector_factor(sector)
    print(f"Singlet (0,0): {ms['deg_00']} modes, d2 = {ms['d2_00']:.4f}, lambda = {ms['lambda_00']:.6f}")
    print(f"Fund (1,0):    {ms['deg_10']} modes, d2 = {ms['d2_10']:.4f}, lambda = {ms['lambda_01']:.6f}")
    print(f"Antifund (0,1):{ms['deg_01']} modes, d2 = {ms['d2_01']:.4f}")
    print(f"xi_cross = {ms['xi_cross']:.6f}")
    print(f"Suppression = {ms['suppression']:.6f}")
    print(f"f_01 = {ms['f_01']:.4f}, f_10 = {ms['f_10']:.4f}")
    print(f"Total multi-sector factor: {ms['factor']:.4f}")
    print()

    # ==================================================================
    # STEP 3: Wall DOS configurations
    # ==================================================================
    print("=" * 70)
    print("STEP 3: Wall DOS Configurations")
    print("=" * 70)
    print()

    wall_configs = []
    for w_idx in range(3):
        tau_1 = float(wall_dos[f'wall_{w_idx}_tau_1'])
        tau_2 = float(wall_dos[f'wall_{w_idx}_tau_2'])
        rho_wall = float(wall_dos[f'wall_{w_idx}_rho_wall_all'])
        rho_per_mode = rho_wall / 4.0
        rho_ms = rho_per_mode * ms['factor']
        rho_full = rho_ms * IMPEDANCE_FACTOR

        wall_configs.append({
            'w_idx': w_idx, 'tau_1': tau_1, 'tau_2': tau_2,
            'rho_wall': rho_wall, 'rho_per_mode': rho_per_mode,
            'rho_ms': rho_ms, 'rho_full': rho_full,
        })

        print(f"Wall {w_idx} [{tau_1:.2f}, {tau_2:.2f}]:")
        print(f"  rho_wall = {rho_wall:.2f}, per mode = {rho_per_mode:.2f}")
        print(f"  + multi-sector (x{ms['factor']:.3f}) = {rho_ms:.2f}")
        print(f"  + impedance (x{IMPEDANCE_FACTOR:.2f}) = {rho_full:.2f}")

    print()

    # ==================================================================
    # STEP 4: Thouless criterion (THE GATE)
    # ==================================================================
    print("=" * 70)
    print("STEP 4: THOULESS CRITERION -- TRAP-33b GATE")
    print("=" * 70)
    print()

    print(f"{'Config':>16s} {'rho_B2':>8s} {'M_max':>10s} {'Verdict':>10s}")
    print("-" * 50)

    gate_results = {}

    for wc in wall_configs:
        w_idx = wc['w_idx']
        scenarios = [
            (f'W{w_idx} C2-only',  wc['rho_per_mode'], V_C2),
            (f'W{w_idx} bare',     wc['rho_per_mode'], V_full),
            (f'W{w_idx} sing+imp', wc['rho_per_mode'] * IMPEDANCE_FACTOR, V_full),
            (f'W{w_idx} multi',    wc['rho_ms'], V_full),
            (f'W{w_idx} FULL',     wc['rho_full'], V_full),
        ]

        for name, rho, V_use in scenarios:
            M_max, _, _, _, _ = thouless_5x5(V_use, E_branch, 0.0, rho, 1.0)
            verdict = "PASS" if M_max > 1.0 else "FAIL"
            print(f"{name:>16s} {rho:>8.2f} {M_max:>10.6f} {verdict:>10s}")

        # Store full result
        M_max_full, M_evals_full, M_mat, V_sub_best, E_sub_best = thouless_5x5(
            V_full, E_branch, 0.0, wc['rho_full'], 1.0)
        gate_results[w_idx] = {
            'M_max': M_max_full, 'M_evals': M_evals_full,
            'rho_full': wc['rho_full'],
            'verdict': "PASS" if M_max_full > 1.0 else "FAIL",
            'M_mat': M_mat, 'V_sub': V_sub_best, 'E_sub': E_sub_best,
        }
        print()

    # Also check full 8x8 (including B3)
    print("Full 8x8 check (including B3 modes):")
    for wc in wall_configs:
        w_idx = wc['w_idx']
        M_max_8, _ = thouless_8x8(V_full, E_branch, 0.0, wc['rho_full'], 1.0, 1.0)
        print(f"  Wall {w_idx}: M_max(8x8) = {M_max_8:.6f}")
    print()

    # ==================================================================
    # STEP 5: Tau dependence
    # ==================================================================
    print("=" * 70)
    print("STEP 5: Tau Dependence of M_max")
    print("=" * 70)
    print()

    best_wall = max(gate_results.keys(), key=lambda k: gate_results[k]['M_max'])
    rho_best = wall_configs[best_wall]['rho_full']

    print(f"Using Wall {best_wall} enhancement (rho_B2 = {rho_best:.2f})")
    print()

    print(f"{'tau':>6s} {'M_max(full)':>12s} {'M_max(C2)':>12s} {'M_max(bulk)':>12s}")
    print("-" * 48)

    M_max_tau = []
    for ti in range(1, len(TAU_VALUES)):
        V_f = build_full_V_8x8(kosmann, ti)
        V_c, _, _, _ = build_V_decomposed(kosmann, ti)
        E_b = get_branch_eigenvalues(kosmann, ti)

        M_full, _, _, _, _ = thouless_5x5(V_f, E_b, 0.0, rho_best, 1.0)
        M_c2, _, _, _, _ = thouless_5x5(V_c, E_b, 0.0, rho_best, 1.0)
        M_bulk, _, _, _, _ = thouless_5x5(V_f, E_b, 0.0, 1.0, 1.0)

        M_max_tau.append((TAU_VALUES[ti], M_full, M_c2, M_bulk))
        print(f"{TAU_VALUES[ti]:6.2f} {M_full:12.6f} {M_c2:12.6f} {M_bulk:12.6f}")

    print()

    # ==================================================================
    # STEP 6: Chemical potential sensitivity
    # ==================================================================
    print("=" * 70)
    print("STEP 6: Chemical Potential Scan")
    print("=" * 70)
    print()

    lambda_B1 = float(E_branch[B1_IDX[0]])
    lambda_B2 = float(np.mean(E_branch[B2_IDX]))

    mu_scan = np.linspace(0, lambda_B1, 201)
    M_vs_mu_full = []
    M_vs_mu_c2 = []

    for mu in mu_scan:
        M_f, _, _, _, _ = thouless_5x5(V_full, E_branch, mu, rho_best, 1.0)
        M_c, _, _, _, _ = thouless_5x5(V_C2, E_branch, mu, rho_best, 1.0)
        M_vs_mu_full.append(M_f)
        M_vs_mu_c2.append(M_c)

    M_vs_mu_full = np.array(M_vs_mu_full)
    M_vs_mu_c2 = np.array(M_vs_mu_c2)

    # Find critical mu where M_max crosses 1
    mu_crit_full = None
    for i in range(len(mu_scan) - 1):
        if M_vs_mu_full[i] < 1.0 <= M_vs_mu_full[i + 1]:
            frac = (1.0 - M_vs_mu_full[i]) / (M_vs_mu_full[i + 1] - M_vs_mu_full[i])
            mu_crit_full = mu_scan[i] + frac * (mu_scan[i + 1] - mu_scan[i])
            break

    print(f"{'mu':>10s} {'M_max(full)':>12s} {'M_max(C2)':>12s}")
    print("-" * 38)
    mu_show = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, lambda_B1]
    for ms_val in mu_show:
        idx = np.argmin(np.abs(mu_scan - ms_val))
        print(f"{mu_scan[idx]:10.4f} {M_vs_mu_full[idx]:12.6f} {M_vs_mu_c2[idx]:12.6f}")

    if mu_crit_full is not None:
        print(f"\nCritical mu (M=1, full kernel): {mu_crit_full:.6f}")
        print(f"  = {mu_crit_full/lambda_B1:.4f} * lambda_B1")
    else:
        # Check if M > 1 already at mu=0
        if M_vs_mu_full[0] > 1.0:
            print(f"\nM_max > 1 already at mu=0! No critical mu needed.")
        else:
            print(f"\nM_max never reaches 1 in scanned range.")

    print()

    # ==================================================================
    # STEP 7: Self-consistent gap equation
    # ==================================================================
    print("=" * 70)
    print("STEP 7: Self-Consistent BdG Gap Equation")
    print("=" * 70)
    print()

    # Try at mu=0 and at mu_crit
    mu_values_sc = [0.0]
    if mu_crit_full is not None:
        mu_values_sc.append(mu_crit_full)

    sc_results = {}
    for mu in mu_values_sc:
        print(f"--- mu = {mu:.6f} ---")
        for wc in wall_configs:
            w_idx = wc['w_idx']
            for D0 in [0.001, 0.01, 0.1, 0.5]:
                Delta, conv, nit = selfconsistent_5x5(
                    V_full, E_branch, mu, wc['rho_full'], 1.0,
                    max_iter=100000, tol=1e-14, Delta0_scale=D0)
                D_norm = np.linalg.norm(Delta)
                D_max = np.max(np.abs(Delta))
                trivial = D_norm < 1e-20

                if D0 == 0.01:
                    sc_results[(w_idx, mu)] = {
                        'Delta': Delta.copy(), 'trivial': trivial,
                        'D_norm': D_norm, 'D_max': D_max, 'conv': conv,
                    }

                if not trivial or D0 == 0.01:
                    print(f"  W{w_idx} D0={D0}: |D|={D_norm:.4e} D_max={D_max:.4e} "
                          f"{'TRIV' if trivial else 'NON-TRIV'} iter={nit}")
        print()

    # ==================================================================
    # STEP 8: Regulator sensitivity
    # ==================================================================
    print("=" * 70)
    print("STEP 8: Regulator Sensitivity (Wall 2, mu=0)")
    print("=" * 70)
    print()

    global ETA_REG
    eta_values = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05]
    print(f"{'eta_frac':>10s} {'M_max':>12s}")
    print("-" * 26)
    for eta in eta_values:
        ETA_REG = eta
        M_max, _, _, _, _ = thouless_5x5(V_full, E_branch, 0.0, rho_best, 1.0)
        print(f"{eta:10.4f} {M_max:12.6f}")
    ETA_REG = 0.001  # restore default
    print()

    # ==================================================================
    # GATE CLASSIFICATION
    # ==================================================================
    print("=" * 70)
    print("TRAP-33b GATE CLASSIFICATION")
    print("=" * 70)
    print()

    M_max_primary = gate_results[best_wall]['M_max']

    print(f"PRIMARY RESULT (mu=0, Wall {best_wall}, full enhancement):")
    print(f"  M_max = {M_max_primary:.6f}")
    print(f"  Kernel: FULL 8-generator Kosmann (NOT C^2-only)")
    print(f"  DOS: singlet wall {wall_configs[best_wall]['rho_per_mode']:.2f} "
          f"x multi-sector {ms['factor']:.3f} x impedance {IMPEDANCE_FACTOR:.2f} "
          f"= {rho_best:.2f} per B2 mode")
    print()

    if M_max_primary >= 3.0:
        verdict = "STRONG PASS"
    elif M_max_primary >= 1.0:
        verdict = "PASS"
    else:
        verdict = "FAIL"

    print(f"TRAP-33b: *** {verdict} ***")
    print(f"  M_max = {M_max_primary:.6f}")

    if verdict == "FAIL":
        shortfall = 1.0 / M_max_primary
        print(f"  Shortfall: {shortfall:.2f}x below threshold")
        if mu_crit_full is not None:
            print(f"  mu_crit (M=1): {mu_crit_full:.4f} = {mu_crit_full/lambda_B1:.1%} of lambda_B1")
        print()
        print("  K-1e RE-EVALUATION:")
        print(f"    Old (C^2-only): M_max = {M_max_bulk_C2:.6f} (bulk), closure correct for C^2")
        print(f"    New (full):     M_max = {M_max_bulk_full:.6f} (bulk)")
        print(f"    Wall enhanced:  M_max = {M_max_primary:.6f}")
        print()
        print("  REMAINING PATHS:")
        print("    1. Finite-density spectral action (mu != 0, P2b)")
        print("    2. Inner fluctuation D_phys (NEW-1)")
        print("    3. Swallowtail unconditional: any Delta > 0 at c_1 = 0")

    print()
    print("SUMMARY TABLE:")
    print("-" * 70)
    print(f"{'Wall':>5s} {'tau range':>14s} {'rho/mode':>10s} {'M_max':>10s} {'Verdict':>10s}")
    print("-" * 70)
    for w_idx in range(3):
        wc = wall_configs[w_idx]
        gr = gate_results[w_idx]
        print(f"{w_idx:>5d} [{wc['tau_1']:.2f}, {wc['tau_2']:.2f}] "
              f"{wc['rho_full']:>10.2f} {gr['M_max']:>10.6f} {gr['verdict']:>10s}")

    # ==================================================================
    # SAVE
    # ==================================================================
    save_data = {
        'tau_values': TAU_VALUES,
        'mu_physical': 0.0,
        'impedance_factor': IMPEDANCE_FACTOR,
        'multi_sector_factor': ms['factor'],
        'lambda_B1': lambda_B1,
        'lambda_B2': lambda_B2,
        'lambda_B3': float(E_branch[0]),
        'shell_gap': E_branch[3] - E_branch[7],
        'primary_verdict': np.array([verdict]),
        'primary_M_max': M_max_primary,
        'primary_wall': best_wall,
        'V_B2B2_full': V_B2B2_full,
        'V_B2B2_C2': V_B2B2_C2,
        'V_B2B2_SU2': V_B2B2_SU2,
        'V_B2B2_U1': V_B2B2_U1,
        'V_5x5_full': V_5x5,
        'M_max_bulk_C2': M_max_bulk_C2,
        'M_max_bulk_full': M_max_bulk_full,
        'mu_scan': mu_scan,
        'M_vs_mu_full': M_vs_mu_full,
        'M_vs_mu_c2': M_vs_mu_c2,
    }

    for w_idx in range(3):
        wc = wall_configs[w_idx]
        gr = gate_results[w_idx]
        save_data[f'wall_{w_idx}_tau_1'] = wc['tau_1']
        save_data[f'wall_{w_idx}_tau_2'] = wc['tau_2']
        save_data[f'wall_{w_idx}_M_max'] = gr['M_max']
        save_data[f'wall_{w_idx}_M_evals'] = np.array(gr['M_evals'])
        save_data[f'wall_{w_idx}_rho_per_mode'] = wc['rho_full']
        save_data[f'wall_{w_idx}_verdict'] = gr['verdict']

    if mu_crit_full is not None:
        save_data['mu_critical'] = mu_crit_full

    for key, val in sc_results.items():
        w, mu = key
        prefix = f'sc_w{w}_mu{mu:.4f}'
        save_data[f'{prefix}_Delta'] = val['Delta']
        save_data[f'{prefix}_trivial'] = val['trivial']

    output_npz = os.path.join(SCRIPT_DIR, "s33b_trap1_wall_bcs.npz")
    np.savez_compressed(output_npz, **save_data)
    print(f"\nSaved: {output_npz}")
    print(f"File size: {os.path.getsize(output_npz) / 1024:.1f} KB")

    # ==================================================================
    # PLOT
    # ==================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: V(B2,B2) comparison
    ax = axes[0, 0]
    labels = ['C2-only', 'SU(2)', 'U(1)', 'FULL']
    maxvals = [np.max(V_B2B2_C2), np.max(V_B2B2_SU2), np.max(V_B2B2_U1), np.max(V_B2B2_full)]
    colors = ['gray', 'blue', 'orange', 'green']
    ax.bar(labels, maxvals, color=colors, alpha=0.7, edgecolor='black')
    for i, v in enumerate(maxvals):
        ax.text(i, v + 0.005, f'{v:.3f}', ha='center', va='bottom', fontsize=10)
    ax.set_ylabel('Max V(B2,B2) off-diagonal')
    ax.set_title('Pairing Kernel by Generator Type')
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 2: M_max bar chart (all walls, full kernel)
    ax = axes[0, 1]
    wlabels = [f'W{w}\n[{wall_configs[w]["tau_1"]:.2f},{wall_configs[w]["tau_2"]:.2f}]'
               for w in range(3)]
    M_vals = [gate_results[w]['M_max'] for w in range(3)]
    colors_w = ['green' if m > 1.0 else 'red' for m in M_vals]
    bars = ax.bar(wlabels, M_vals, color=colors_w, alpha=0.7, edgecolor='black')
    ax.axhline(y=1.0, color='black', ls='--', lw=2, label='M=1 threshold')
    for bar, m in zip(bars, M_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{m:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.set_ylabel('M_max (Thouless)')
    ax.set_title(f'TRAP-33b: {verdict}')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 3: M_max vs mu
    ax = axes[1, 0]
    ax.plot(mu_scan, M_vs_mu_full, 'b-', lw=2, label='Full kernel')
    ax.plot(mu_scan, M_vs_mu_c2, 'r--', lw=1.5, label='C^2-only kernel')
    ax.axhline(y=1.0, color='black', ls='--', lw=2)
    ax.axvline(x=0, color='green', ls=':', alpha=0.6, label='mu=0 (physical)')
    if mu_crit_full is not None:
        ax.axvline(x=mu_crit_full, color='orange', ls=':', alpha=0.7,
                   label=f'mu_crit={mu_crit_full:.3f}')
    ax.set_xlabel('Chemical potential mu')
    ax.set_ylabel('M_max')
    ax.set_title(f'M_max vs mu (Wall {best_wall})')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: Scenario comparison (wall 2)
    ax = axes[1, 1]
    scen_labels = ['C2-only', 'Full\nbulk', 'Wall\nbare', 'Wall+\nimp', 'Wall+\nms+imp']
    scen_M = []
    for V_use, rho in [(V_C2, 1.0), (V_full, 1.0),
                        (V_full, wall_configs[2]['rho_per_mode']),
                        (V_full, wall_configs[2]['rho_per_mode'] * IMPEDANCE_FACTOR),
                        (V_full, wall_configs[2]['rho_full'])]:
        M, _, _, _, _ = thouless_5x5(V_use, E_branch, 0.0, rho, 1.0)
        scen_M.append(M)
    colors_s = ['green' if m > 1.0 else ('orange' if m > 0.5 else 'red') for m in scen_M]
    bars_s = ax.bar(scen_labels, scen_M, color=colors_s, alpha=0.7, edgecolor='black')
    ax.axhline(y=1.0, color='black', ls='--', lw=2)
    for bar, m in zip(bars_s, scen_M):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f'{m:.4f}', ha='center', va='bottom', fontsize=8, fontweight='bold')
    ax.set_ylabel('M_max at mu=0')
    ax.set_title('Sensitivity Analysis (Wall 2)')
    ax.grid(True, alpha=0.3, axis='y')

    fig.suptitle(f'TRAP-33b: {verdict} | M_max = {M_max_primary:.4f}',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plot_path = os.path.join(SCRIPT_DIR, "s33b_trap1_wall_bcs.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"Plot saved: {plot_path}")

    return gate_results, M_max_primary, verdict


if __name__ == "__main__":
    t_start = time.time()
    gate_results, M_max_primary, verdict = run_trap1()
    elapsed = time.time() - t_start

    print()
    print("=" * 80)
    print(f"TRAP-33b FINAL: {verdict} | M_max = {M_max_primary:.6f}")
    print(f"Runtime: {elapsed:.1f}s")
    print("=" * 80)
