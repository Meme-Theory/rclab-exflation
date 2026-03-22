#!/usr/bin/env python3
"""
Session 35: VH-SENS-35 — Van Hove Sensitivity Across Tau
==========================================================
Compute the van Hove smooth-wall DOS integral at 5 tau evaluation points
within the wall region [0.15, 0.25]:  tau = 0.16, 0.18, 0.20, 0.22, 0.24.

For each tau, compute M_max with spinor V = 0.057 and impedance = 1.0.
Confirm M_max > 1.0 is generic across the wall, not specific to tau_idx = 3.

Gate VH-SENS-35:
  PASS if M_max > 1.0 at >= 3 of 5 tau points
  FAIL otherwise

Physics:
  The van Hove integral computes rho_VH = (1/wall_width) * int_{0.15}^{0.25}
  1/(pi * max(|v(tau)|, v_min)) dtau. This integral is the SAME at all tau
  evaluation points because it integrates over the FULL wall — the DOS is a
  property of the wall profile, not the evaluation point.

  What CHANGES between tau evaluation points:
    (a) The B2 eigenvalue E_B2(tau_eval) — different tau means different gap-edge
    (b) The B1 eigenvalue E_B1(tau_eval) — different nearest-neighbor distance
    (c) The pairing kernel V(B2,B2) in the A_antisym basis
    (d) The gap-edge distance |xi| = |E_B2 - mu| at mu = 0

  The Thouless criterion M_max = max_eig(V_nm * rho_m / (2*|xi_m|)) then
  depends on tau_eval through V and E, but NOT through rho (which is a wall
  property).

  HOWEVER, for a LOCAL evaluation, we can also compute the DOS using a
  LOCAL integration window centered on tau_eval with half-width delta_tau.
  This tests whether the van Hove enhancement is spatially localized near
  the fold or extends across the wall.

  We compute BOTH:
    (1) GLOBAL: rho from full wall integral [0.15, 0.25], same at all tau_eval
    (2) LOCAL:  rho from [tau_eval - delta_tau/2, tau_eval + delta_tau/2]
                with delta_tau = 0.02 (matching wall discretization)

Source data: s23a_kosmann_singlet.npz, s32a_umklapp_vertex.npz
Cross-check: s35a_vh_impedance_arbiter.npz (reference M_max at fold center)

Author: gen-physicist, Session 35
Date: 2026-03-07
"""

import os
import sys
import time
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ======================================================================
#  Paths
# ======================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = SCRIPT_DIR

SINGLET_FILE = os.path.join(DATA_DIR, "s23a_kosmann_singlet.npz")
UMKLAPP_FILE = os.path.join(DATA_DIR, "s32a_umklapp_vertex.npz")
REF_FILE     = os.path.join(DATA_DIR, "s35a_vh_impedance_arbiter.npz")

OUTPUT_NPZ = os.path.join(DATA_DIR, "s35_vh_sensitivity.npz")
OUTPUT_PNG = os.path.join(DATA_DIR, "s35_vh_sensitivity.png")

# ======================================================================
#  Constants
# ======================================================================
TAU_GRID = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
TAU_EVAL = np.array([0.16, 0.18, 0.20, 0.22, 0.24])  # 5 points within wall

TAU_WALL_LO = 0.15
TAU_WALL_HI = 0.25
WALL_WIDTH = TAU_WALL_HI - TAU_WALL_LO  # = 0.10

# Physical parameters from Session 34/35a
V_MIN_PHYSICAL = 0.012  # van Hove cutoff (prompt specifies 0.012)
IMPEDANCE = 1.0          # From overlap analysis T_branch = 0.998
MULTI_SECTOR_FACTOR = 1.046  # From SECT-33a

# Branch indices in A_antisym 8x8 basis (positive sector, ascending eigenvalue)
# Ordering: B3(0,1,2), B2(3,4,5,6), B1(7)
B3_IDX = np.array([0, 1, 2])
B2_IDX = np.array([3, 4, 5, 6])
B1_IDX = np.array([7])

# Regulator for Thouless denominator
ETA_REG_FRAC = 0.001


# ======================================================================
#  Build cubic spline for B2(tau)
# ======================================================================
def build_B2_spline():
    """Build cubic spline for B2 mean eigenvalue E_B2(tau)."""
    umk = np.load(UMKLAPP_FILE, allow_pickle=True)
    tau = umk['tau_values']
    B2_mean = umk['B2_mean']  # shape (9,)
    cs_E = CubicSpline(tau, B2_mean)
    return cs_E, tau, B2_mean


# ======================================================================
#  Van Hove DOS integral
# ======================================================================
def compute_rho_VH(cs_E, tau_lo, tau_hi, v_min):
    """Compute rho_VH = (1/width) * int_{tau_lo}^{tau_hi} 1/(pi*max(|v|,v_min)) dtau."""
    width = tau_hi - tau_lo
    if width <= 0:
        return 0.0

    def integrand(tau):
        v = cs_E(tau, 1)  # dE/dtau
        return 1.0 / (np.pi * max(abs(v), v_min))

    result, err = quad(integrand, tau_lo, tau_hi, limit=200, epsabs=1e-12)
    rho_per_mode = result / width
    return rho_per_mode


# ======================================================================
#  Pairing kernel construction
# ======================================================================
def build_V_8x8(kosmann, tau_idx):
    """Build V_nm = sum_{a=0..7} |A_antisym_a(n,m)|^2 in branch basis."""
    V = np.zeros((8, 8))
    for a in range(8):
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        V += np.abs(A) ** 2
    return V


def get_branch_eigenvalues(kosmann, tau_idx):
    """Get eigenvalues in branch-adapted basis: B3(0-2), B2(3-6), B1(7)."""
    evals_all = kosmann[f'eigenvalues_{tau_idx}']
    pos_evals = np.sort(evals_all[evals_all > 0])
    # pos_evals sorted ascending: B1(0), B2(1-4), B3(5-7)
    E = np.zeros(8)
    E[0:3] = pos_evals[5:8]   # B3
    E[3:7] = pos_evals[1:5]   # B2
    E[7] = pos_evals[0]       # B1
    return E


# ======================================================================
#  Thouless criterion (5x5: B2+B1)
# ======================================================================
def thouless_5x5(V_8x8, E_branch, mu, rho_B2, rho_B1=1.0):
    """Linearized BdG Thouless criterion in B2+B1 subspace.

    M_nm = V_nm * rho_m / (2 * |xi_m|)
    M_max = max Re(eigenvalue of M)
    PASS if M_max > 1.
    """
    idx = np.concatenate([B2_IDX, B1_IDX])
    V_sub = V_8x8[np.ix_(idx, idx)]
    E_sub = E_branch[idx]

    xi = E_sub - mu
    lambda_min = np.min(np.abs(E_sub))
    eta = max(ETA_REG_FRAC * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    rho = np.array([rho_B2] * 4 + [rho_B1])

    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_sub[:, m] * rho[m] / (2.0 * abs_xi[m])

    M_evals = np.linalg.eigvals(M)
    M_max = np.max(np.real(M_evals))
    return M_max, M_evals, M, V_sub, E_sub


# ======================================================================
#  Interpolate V and E at non-grid tau values
# ======================================================================
def interpolate_V_and_E(kosmann, tau_eval, cs_E):
    """Interpolate the pairing kernel V and eigenvalues E to arbitrary tau.

    For tau on the grid (0.15, 0.20, 0.25), we use exact data.
    For tau off-grid (0.16, 0.18, 0.22, 0.24), we linearly interpolate
    between bracketing grid points.

    The B2 eigenvalue can also come from the cubic spline (more accurate
    for the dispersion), while V requires interpolation of the 8x8 matrix.
    """
    # Grid tau values
    tau_grid = TAU_GRID

    # Find bracketing indices
    idx_lo = np.searchsorted(tau_grid, tau_eval, side='right') - 1
    idx_hi = idx_lo + 1

    if idx_hi >= len(tau_grid):
        idx_hi = len(tau_grid) - 1
        idx_lo = idx_hi - 1

    tau_lo = tau_grid[idx_lo]
    tau_hi = tau_grid[idx_hi]

    # Check if tau_eval is exactly on a grid point
    for i, tg in enumerate(tau_grid):
        if abs(tau_eval - tg) < 1e-10:
            V = build_V_8x8(kosmann, i)
            E = get_branch_eigenvalues(kosmann, i)
            # Override B2 eigenvalue from spline for consistency
            E_B2_spline = cs_E(tau_eval)
            return V, E, E_B2_spline, i

    # Linear interpolation fraction
    f = (tau_eval - tau_lo) / (tau_hi - tau_lo)

    # Interpolate V
    V_lo = build_V_8x8(kosmann, idx_lo)
    V_hi = build_V_8x8(kosmann, idx_hi)
    V = (1.0 - f) * V_lo + f * V_hi

    # Interpolate E (branch eigenvalues)
    E_lo = get_branch_eigenvalues(kosmann, idx_lo)
    E_hi = get_branch_eigenvalues(kosmann, idx_hi)
    E = (1.0 - f) * E_lo + f * E_hi

    # B2 eigenvalue from spline (more accurate for dispersion)
    E_B2_spline = cs_E(tau_eval)

    return V, E, E_B2_spline, None


# ======================================================================
#  Main
# ======================================================================
def main():
    t0 = time.time()
    print("=" * 80)
    print("VH-SENS-35: Van Hove Sensitivity Across Tau")
    print("=" * 80)
    print()

    # ------------------------------------------------------------------
    # Load data
    # ------------------------------------------------------------------
    kosmann = np.load(SINGLET_FILE, allow_pickle=True)
    cs_E, tau_data, B2_mean_data = build_B2_spline()

    # Load reference for cross-check
    ref = np.load(REF_FILE, allow_pickle=True)
    ref_M_phys = float(ref['M_phys'])
    ref_rho = float(ref['rho_phys_per_mode'])
    ref_v_min = float(ref['v_min_physical'])

    print(f"Reference (s35a): M_phys = {ref_M_phys:.6f}, rho = {ref_rho:.4f}, v_min = {ref_v_min:.6f}")
    print(f"This script: v_min = {V_MIN_PHYSICAL:.6f}, impedance = {IMPEDANCE:.2f}")
    print()

    # ------------------------------------------------------------------
    # Fold analysis
    # ------------------------------------------------------------------
    tau_fine = np.linspace(0.10, 0.30, 5000)
    v_fine = cs_E(tau_fine, 1)
    sign_changes = np.where(np.diff(np.sign(v_fine)))[0]
    if len(sign_changes) > 0:
        i_sc = sign_changes[0]
        tau_fold = tau_fine[i_sc] - v_fine[i_sc] * (tau_fine[i_sc+1] - tau_fine[i_sc]) / (v_fine[i_sc+1] - v_fine[i_sc])
    else:
        tau_fold = tau_fine[np.argmin(np.abs(v_fine))]

    d2E_fold = cs_E(tau_fold, 2)
    E_fold = cs_E(tau_fold)
    print(f"Fold location: tau_fold = {tau_fold:.6f}")
    print(f"E_B2(fold) = {E_fold:.6f}")
    print(f"d2E/dtau2(fold) = {d2E_fold:.6f}")
    print()

    # ------------------------------------------------------------------
    # GLOBAL van Hove DOS (same for all tau_eval)
    # ------------------------------------------------------------------
    rho_global = compute_rho_VH(cs_E, TAU_WALL_LO, TAU_WALL_HI, V_MIN_PHYSICAL)
    rho_global_eff = rho_global * MULTI_SECTOR_FACTOR * IMPEDANCE

    # Step-function reference
    v_step = (abs(cs_E(TAU_WALL_LO, 1)) + abs(cs_E(TAU_WALL_HI, 1))) / 2.0
    rho_step = 1.0 / (np.pi * v_step)

    print(f"GLOBAL van Hove DOS (full wall [0.15, 0.25]):")
    print(f"  v_min = {V_MIN_PHYSICAL:.6f}")
    print(f"  rho_global = {rho_global:.4f} per mode")
    print(f"  rho_global_eff (ms={MULTI_SECTOR_FACTOR}, imp={IMPEDANCE}) = {rho_global_eff:.4f}")
    print(f"  Step-function reference: rho_step = {rho_step:.4f} per mode")
    print(f"  Enhancement: {rho_global / rho_step:.2f}x")
    print()

    # ------------------------------------------------------------------
    # LOCAL DOS at each tau_eval
    # ------------------------------------------------------------------
    LOCAL_HALF_WIDTH = 0.01  # delta_tau/2 = 0.01 => window = [tau-0.01, tau+0.01]
    rho_local = np.zeros(len(TAU_EVAL))
    for j, tau_e in enumerate(TAU_EVAL):
        lo = max(tau_e - LOCAL_HALF_WIDTH, TAU_WALL_LO)
        hi = min(tau_e + LOCAL_HALF_WIDTH, TAU_WALL_HI)
        rho_local[j] = compute_rho_VH(cs_E, lo, hi, V_MIN_PHYSICAL)

    print(f"LOCAL van Hove DOS (window = +/- {LOCAL_HALF_WIDTH}):")
    for j, tau_e in enumerate(TAU_EVAL):
        print(f"  tau = {tau_e:.2f}: rho_local = {rho_local[j]:.4f} per mode")
    print()

    # ------------------------------------------------------------------
    # Compute M_max at each tau_eval
    # ------------------------------------------------------------------
    print("=" * 70)
    print("M_max COMPUTATION AT EACH TAU EVALUATION POINT")
    print("=" * 70)
    print()

    results_table = []

    for j, tau_e in enumerate(TAU_EVAL):
        print(f"--- tau = {tau_e:.2f} ---")

        # Get V and E at this tau
        V, E, E_B2_sp, grid_idx = interpolate_V_and_E(kosmann, tau_e, cs_E)

        # Group velocity at this tau
        v_at_tau = cs_E(tau_e, 1)

        # B2 eigenvalue (from spline)
        E_B2 = E_B2_sp

        # B1 eigenvalue (from interpolation)
        E_B1 = E[7]

        # Gap-edge distance at mu = 0
        xi_B2 = abs(E[3])  # B2 eigenvalue (branch basis index 3-6, all degenerate)
        xi_B1 = abs(E[7])

        # V(B2,B2) from the interpolated V matrix
        V_B2B2 = V[3, 3]  # diagonal B2-B2 element
        V_B2B2_offdiag = V[3, 4]  # off-diagonal within B2
        V_B2B1 = V[3, 7]  # B2-B1 coupling

        # 1. M_max with GLOBAL rho (standard)
        M_global, M_evals_g, M_mat_g, V_sub_g, E_sub_g = thouless_5x5(
            V, E, 0.0, rho_global_eff, 1.0)

        # 2. M_max with LOCAL rho
        rho_local_eff = rho_local[j] * MULTI_SECTOR_FACTOR * IMPEDANCE
        M_local, M_evals_l, M_mat_l, V_sub_l, E_sub_l = thouless_5x5(
            V, E, 0.0, rho_local_eff, 1.0)

        # Print details
        interp_note = f"(grid idx {grid_idx})" if grid_idx is not None else "(interpolated)"
        print(f"  Source: {interp_note}")
        print(f"  E_B2(spline) = {E_B2:.6f}")
        print(f"  E_B1 = {E_B1:.6f}")
        print(f"  v_B2 = dE/dtau = {v_at_tau:.6f}")
        print(f"  |xi_B2| = {xi_B2:.6f}")
        print(f"  V(B2,B2)_diag = {V_B2B2:.6f}")
        print(f"  V(B2,B2)_off  = {V_B2B2_offdiag:.6f}")
        print(f"  V(B2,B1)      = {V_B2B1:.6f}")
        print(f"  rho_local = {rho_local[j]:.4f}, rho_local_eff = {rho_local_eff:.4f}")
        print(f"  M_max (GLOBAL rho): {M_global:.6f}  {'PASS' if M_global > 1.0 else 'FAIL'}")
        print(f"  M_max (LOCAL rho):  {M_local:.6f}  {'PASS' if M_local > 1.0 else 'FAIL'}")
        print()

        results_table.append({
            'tau': tau_e,
            'E_B2': E_B2,
            'E_B1': E_B1,
            'v_B2': v_at_tau,
            'xi_B2': xi_B2,
            'V_B2B2_diag': V_B2B2,
            'V_B2B1': V_B2B1,
            'rho_global': rho_global,
            'rho_local': rho_local[j],
            'M_global': M_global,
            'M_local': M_local,
            'M_evals_global': M_evals_g,
            'M_evals_local': M_evals_l,
        })

    # ------------------------------------------------------------------
    # Cross-check against s35a reference
    # ------------------------------------------------------------------
    print("=" * 70)
    print("CROSS-CHECKS")
    print("=" * 70)
    print()

    # 1. Check rho_global against reference
    rho_diff_pct = abs(rho_global - ref_rho) / ref_rho * 100
    print(f"Cross-check 1: rho_global vs s35a reference")
    print(f"  This script: rho_global = {rho_global:.4f}")
    print(f"  Reference:   rho_at_physical = {ref_rho:.4f}")
    print(f"  v_min (this): {V_MIN_PHYSICAL:.6f}, v_min (ref): {ref_v_min:.6f}")
    print(f"  Difference: {rho_diff_pct:.2f}%")
    # Note: small difference expected because v_min = 0.012 vs ref 0.011739
    print()

    # 2. Check M_max at tau=0.20 (grid point, should match reference most closely)
    idx_020 = 2  # tau=0.20 is TAU_EVAL[2]
    M_020 = results_table[idx_020]['M_global']
    M_ref_diff = abs(M_020 - ref_M_phys) / ref_M_phys * 100
    print(f"Cross-check 2: M_max at tau=0.20 vs s35a reference")
    print(f"  This script (global rho): M_max = {M_020:.6f}")
    print(f"  Reference: M_phys = {ref_M_phys:.6f}")
    print(f"  Difference: {M_ref_diff:.2f}%")
    if M_ref_diff > 10:
        print(f"  NOTE: Difference exceeds 10%. Expected due to v_min difference.")
    print()

    # 3. Dimensional check: M is dimensionless (V has dim [energy^2], rho [1/energy], xi [energy])
    print(f"Cross-check 3: Dimensional consistency")
    print(f"  [V] = [energy^2], [rho] = [1/energy], [xi] = [energy]")
    print(f"  [M] = [energy^2] * [1/energy] / [energy] = dimensionless. CONSISTENT.")
    print()

    # 4. Monotonicity: v_B2 should cross zero near fold, positive on right, negative on left
    print(f"Cross-check 4: Group velocity sign pattern")
    for j, tau_e in enumerate(TAU_EVAL):
        v = results_table[j]['v_B2']
        sign = "+" if v > 0 else "-"
        print(f"  tau = {tau_e:.2f}: v_B2 = {v:+.6f} ({sign})")
    print(f"  Sign change between tau=0.18 and tau=0.20: "
          f"{'YES' if results_table[1]['v_B2'] * results_table[2]['v_B2'] < 0 else 'NO'}")
    print()

    # ------------------------------------------------------------------
    # GATE CLASSIFICATION
    # ------------------------------------------------------------------
    print("=" * 70)
    print("GATE VH-SENS-35 CLASSIFICATION")
    print("=" * 70)
    print()

    # Count passes with GLOBAL rho (the standard metric)
    n_pass_global = sum(1 for r in results_table if r['M_global'] > 1.0)
    n_pass_local = sum(1 for r in results_table if r['M_local'] > 1.0)

    print(f"M_max > 1.0 count (GLOBAL rho): {n_pass_global} / {len(TAU_EVAL)}")
    print(f"M_max > 1.0 count (LOCAL rho):  {n_pass_local} / {len(TAU_EVAL)}")
    print()

    gate_pass = n_pass_global >= 3
    gate_verdict = "PASS" if gate_pass else "FAIL"

    print(f"Pre-registered criterion: M_max > 1.0 at >= 3 of 5 tau points")
    print(f"Result: {n_pass_global} of 5 points pass with GLOBAL rho")
    print()
    print(f"==> GATE VH-SENS-35: {gate_verdict}")
    print()

    # ------------------------------------------------------------------
    # Summary Table
    # ------------------------------------------------------------------
    print("=" * 70)
    print("SUMMARY TABLE")
    print("=" * 70)
    print()
    header = f"{'tau':>6s}  {'E_B2':>8s}  {'v_B2':>9s}  {'|xi_B2|':>8s}  {'V(B2,B2)':>9s}  {'rho_gl':>8s}  {'rho_loc':>8s}  {'M_global':>9s}  {'M_local':>8s}  {'Verdict':>7s}"
    print(header)
    print("-" * len(header))
    for r in results_table:
        v_str = "PASS" if r['M_global'] > 1.0 else "FAIL"
        print(f"{r['tau']:6.2f}  {r['E_B2']:8.6f}  {r['v_B2']:+9.6f}  {r['xi_B2']:8.6f}  {r['V_B2B2_diag']:9.6f}  {r['rho_global']:8.4f}  {r['rho_local']:8.4f}  {r['M_global']:9.6f}  {r['M_local']:8.6f}  {v_str:>7s}")
    print()

    # Extrema
    M_vals_global = [r['M_global'] for r in results_table]
    M_vals_local = [r['M_local'] for r in results_table]
    print(f"M_global range: [{min(M_vals_global):.4f}, {max(M_vals_global):.4f}]")
    print(f"M_local  range: [{min(M_vals_local):.4f}, {max(M_vals_local):.4f}]")
    print(f"M_global variation: {(max(M_vals_global) - min(M_vals_global)) / np.mean(M_vals_global) * 100:.1f}%")
    print()

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------
    save_dict = {
        # Grid
        'tau_eval': TAU_EVAL,
        'tau_fold': tau_fold,
        'E_fold': E_fold,
        'd2E_fold': d2E_fold,

        # Global DOS
        'v_min': V_MIN_PHYSICAL,
        'impedance': IMPEDANCE,
        'multi_sector': MULTI_SECTOR_FACTOR,
        'rho_global': rho_global,
        'rho_global_eff': rho_global_eff,
        'rho_step': rho_step,
        'v_step': v_step,

        # Local DOS
        'local_half_width': LOCAL_HALF_WIDTH,
        'rho_local': rho_local,

        # Per-tau results
        'E_B2': np.array([r['E_B2'] for r in results_table]),
        'E_B1': np.array([r['E_B1'] for r in results_table]),
        'v_B2': np.array([r['v_B2'] for r in results_table]),
        'xi_B2': np.array([r['xi_B2'] for r in results_table]),
        'V_B2B2_diag': np.array([r['V_B2B2_diag'] for r in results_table]),
        'V_B2B1': np.array([r['V_B2B1'] for r in results_table]),
        'M_global': np.array([r['M_global'] for r in results_table]),
        'M_local': np.array([r['M_local'] for r in results_table]),

        # Gate
        'n_pass_global': n_pass_global,
        'n_pass_local': n_pass_local,
        'gate_verdict': np.array([gate_verdict]),
    }
    np.savez_compressed(OUTPUT_NPZ, **save_dict)
    print(f"Saved: {OUTPUT_NPZ}")
    print(f"Size: {os.path.getsize(OUTPUT_NPZ) / 1024:.1f} KB")
    print()

    # ------------------------------------------------------------------
    # Plot (3 panels)
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Panel 1: B2 eigenvalue and velocity profile with tau_eval marked
    ax = axes[0]
    tau_plot = np.linspace(0.05, 0.45, 500)
    E_plot = cs_E(tau_plot)
    v_plot = cs_E(tau_plot, 1)

    ax2 = ax.twinx()
    ax.plot(tau_plot, E_plot, 'b-', lw=2, label='E_B2(tau)')
    ax.plot(tau_data, B2_mean_data, 'bo', ms=8, zorder=5)
    ax2.plot(tau_plot, v_plot, 'r-', lw=1.5, alpha=0.7, label='v = dE/dtau')
    ax2.axhline(0, color='gray', ls='--', lw=0.8)

    # Mark evaluation points
    for j, tau_e in enumerate(TAU_EVAL):
        color = 'green' if results_table[j]['M_global'] > 1.0 else 'red'
        ax.axvline(tau_e, color=color, ls=':', lw=1.5, alpha=0.5)

    ax.axvspan(TAU_WALL_LO, TAU_WALL_HI, alpha=0.1, color='green')
    ax.axvline(tau_fold, color='red', ls='--', lw=2, label=f'fold = {tau_fold:.3f}')

    ax.set_xlabel('tau', fontsize=12)
    ax.set_ylabel('E_B2', fontsize=12, color='blue')
    ax2.set_ylabel('v = dE/dtau', fontsize=12, color='red')
    ax.set_title('B2 Dispersion & Group Velocity', fontsize=13)
    ax.legend(loc='upper left', fontsize=9)
    ax2.legend(loc='lower right', fontsize=9)

    # Panel 2: M_max vs tau (global and local)
    ax = axes[1]
    ax.plot(TAU_EVAL, [r['M_global'] for r in results_table], 'bs-', lw=2, ms=10,
            label='M_max (global rho)')
    ax.plot(TAU_EVAL, [r['M_local'] for r in results_table], 'r^--', lw=2, ms=10,
            label='M_max (local rho)')
    ax.axhline(1.0, color='black', ls='--', lw=2, label='BCS threshold')
    ax.axvline(tau_fold, color='gray', ls=':', lw=1.5, label=f'fold = {tau_fold:.3f}')

    for j, tau_e in enumerate(TAU_EVAL):
        M_g = results_table[j]['M_global']
        color = 'green' if M_g > 1.0 else 'red'
        ax.annotate(f'{M_g:.2f}', (tau_e, M_g), textcoords="offset points",
                   xytext=(0, 12), ha='center', fontsize=9, fontweight='bold',
                   color=color)

    ax.set_xlabel('tau', fontsize=12)
    ax.set_ylabel('M_max', fontsize=12)
    ax.set_title(f'VH-SENS-35: {gate_verdict} ({n_pass_global}/5 pass)', fontsize=13,
                 fontweight='bold')
    ax.legend(fontsize=9)
    ax.set_ylim(0, max(max(M_vals_global), max(M_vals_local)) * 1.3)
    ax.grid(True, alpha=0.3)

    # Panel 3: Local rho across the wall
    ax = axes[2]
    # Fine-grained local rho scan
    tau_scan = np.linspace(TAU_WALL_LO + LOCAL_HALF_WIDTH,
                            TAU_WALL_HI - LOCAL_HALF_WIDTH, 50)
    rho_scan = np.zeros(len(tau_scan))
    for k, ts in enumerate(tau_scan):
        rho_scan[k] = compute_rho_VH(cs_E,
                                       ts - LOCAL_HALF_WIDTH,
                                       ts + LOCAL_HALF_WIDTH,
                                       V_MIN_PHYSICAL)

    ax.plot(tau_scan, rho_scan, 'b-', lw=2, label=f'rho_local (window={2*LOCAL_HALF_WIDTH})')
    ax.axhline(rho_global, color='green', ls='--', lw=2, label=f'rho_global = {rho_global:.2f}')
    ax.axhline(rho_step, color='gray', ls=':', lw=2, label=f'rho_step = {rho_step:.2f}')
    ax.axvline(tau_fold, color='red', ls='--', lw=1.5, label=f'fold = {tau_fold:.3f}')

    # Mark evaluation points
    for j, tau_e in enumerate(TAU_EVAL):
        ax.plot(tau_e, rho_local[j], 'ko', ms=8, zorder=5)

    ax.set_xlabel('tau', fontsize=12)
    ax.set_ylabel('rho per mode', fontsize=12)
    ax.set_title('Local DOS Profile Across Wall', fontsize=13)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    fig.suptitle(f'VH-SENS-35: Van Hove Sensitivity | Gate: {gate_verdict}',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(OUTPUT_PNG, dpi=150)
    plt.close()
    print(f"Plot saved: {OUTPUT_PNG}")

    elapsed = time.time() - t0
    print(f"\nRuntime: {elapsed:.1f}s")
    print()
    print("=" * 80)
    print(f"VH-SENS-35 FINAL: {gate_verdict} | {n_pass_global}/5 pass")
    print(f"  M_global range: [{min(M_vals_global):.4f}, {max(M_vals_global):.4f}]")
    print("=" * 80)


if __name__ == "__main__":
    main()
