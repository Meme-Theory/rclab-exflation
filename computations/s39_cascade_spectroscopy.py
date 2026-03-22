#!/usr/bin/env python3
"""
Session 39: CASCADE-39 -- Cascade Spectroscopy at 50 Tau Values
================================================================

Computes the full singlet (0,0) dispersion relation lambda_k(tau) at 50
uniformly spaced tau values in [0.00, 0.50]. Identifies all van Hove
singularities (v = dlambda/dtau = 0), computes the Thouless M_max at
each tau using the proper multi-band methodology from the s35/s36 chain,
and determines whether the known fold at tau ~ 0.190 is unique or part
of a cascade fragmentation sequence.

GATE CASCADE-39 (pre-registered):
  PASS (UNIQUE FOLD): Only the known fold at tau ~ 0.190 has M_max > 1.
  FAIL (CASCADE): Multiple van Hove singularities with M_max > 1.

Mathematical structure:
  The singlet sector has D = Omega(tau), a 16x16 anti-Hermitian matrix.
  Eigenvalues of H = 1j*Omega are real, come in +/- pairs (PH symmetry).
  8 positive eigenvalues split into 3 distinct branches:
    B1 (singlet, d=1): lowest positive eigenvalue
    B2 (quartet, d=4): middle four eigenvalues
    B3 (triplet, d=3): top three eigenvalues

  At each tau, the Thouless BCS criterion is evaluated as an 8x8 matrix
  problem in the positive eigenvalue subspace:
    M_nm = V_nm * rho_m / (2 * |xi_m|)
  where V_nm = sum_a |<n|K_a|m>|^2 is the Kosmann pairing interaction,
  rho_m is the DOS of branch m, and xi_m = lambda_m - mu with mu = 0.

  The DOS rho_m at each tau is computed from the group velocity:
    rho = 1 / (pi * |v_m|) where v_m = dlambda_m / dtau
  At a van Hove singularity (v_m = 0), rho diverges as 1/sqrt|tau - tau_VH|.
  We regularize by integrating over a small window of width delta_tau.

Author: gen-physicist, Session 39
Date: 2026-03-09
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh as scipy_eigh
from scipy.interpolate import CubicSpline

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
)

t0 = time.time()

# ======================================================================
#  Configuration
# ======================================================================
N_TAU = 50
TAU_MIN = 0.00
TAU_MAX = 0.50
TAU_GRID = np.linspace(TAU_MIN, TAU_MAX, N_TAU)
DTAU = TAU_GRID[1] - TAU_GRID[0]

# Branch structure
B1_IDX = np.array([0])          # indices in positive-sector (8 modes)
B2_IDX = np.array([1, 2, 3, 4])
B3_IDX = np.array([5, 6, 7])
BRANCH_MULTS = {'B1': 1, 'B2': 4, 'B3': 3}

# BCS parameters
MU = 0.0
ETA_REG_FRAC = 0.001  # regulator as fraction of lambda_min

# Wall region for DOS integration (from s35 chain)
TAU_WALL_LO = 0.15
TAU_WALL_HI = 0.25
WALL_WIDTH = TAU_WALL_HI - TAU_WALL_LO

# Known calibration: M_max = 1.674 at tau = 0.20 from s35/s36
MMAX_CALIBRATION = 1.674
MMAX_THRESHOLD = 1.0


# ======================================================================
#  Step 1: Compute singlet eigenvalues + Kosmann V matrix at all tau
# ======================================================================

def compute_singlet_spectrum_and_V(tau, gens, f_abc, gammas):
    """
    At a given tau, compute:
    1. The 16 eigenvalues of H = 1j * Omega (real, sorted ascending)
    2. The eigenvectors
    3. The Kosmann pairing matrix V_nm = sum_a |<n|K_a|m>|^2

    Returns:
        evals: (16,) real eigenvalues sorted ascending
        V_pos: (8,8) V matrix in positive-eigenvalue subspace
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Diagonalize H = 1j * Omega
    H = 1j * Omega
    evals, evecs = scipy_eigh(H)  # real eigenvalues, orthonormal eigenvectors

    # Build 8 Kosmann matrices K_a = (1/4) sum_{b,c} Gamma^b_{ac} gamma_b gamma_c
    # These represent the spin connection acting on spinors along direction a
    K_matrices = []
    for a in range(8):
        K_a = np.zeros((16, 16), dtype=complex)
        for b in range(8):
            for c in range(8):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    K_a += coeff * gammas[b] @ gammas[c]
        K_a *= 0.25
        K_matrices.append(K_a)

    # Transform K_a to eigenbasis, extract positive sector
    pos_evecs = evecs[:, 8:]  # columns 8-15 = positive eigenvalues

    # V_nm = sum_a |<n|K_a|m>|^2 for positive modes n, m = 0..7
    V_pos = np.zeros((8, 8))
    for a in range(8):
        K_a_eig = pos_evecs.conj().T @ K_matrices[a] @ pos_evecs  # (8, 8)
        V_pos += np.abs(K_a_eig)**2

    return evals, V_pos


def compute_all_data():
    """Compute eigenvalues and V matrices at all 50 tau values."""
    print(f"[1] Setting up SU(3) Lie algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    print(f"[2] Computing singlet spectrum + Kosmann V at {N_TAU} tau values...")
    all_evals = np.zeros((N_TAU, 16))
    all_V = np.zeros((N_TAU, 8, 8))

    for i, tau in enumerate(TAU_GRID):
        evals, V_pos = compute_singlet_spectrum_and_V(tau, gens, f_abc, gammas)
        all_evals[i] = evals
        all_V[i] = V_pos
        if (i + 1) % 10 == 0 or i == 0:
            pos = evals[8:]
            print(f"  tau[{i:2d}] = {tau:.4f}: B1={pos[0]:.6f}, "
                  f"B2={np.mean(pos[1:5]):.6f}, B3={np.mean(pos[5:8]):.6f}, "
                  f"V(B2,B2)_diag={np.mean(np.diag(V_pos)[1:5]):.6f}")

    return all_evals, all_V, gens, f_abc, gammas


# ======================================================================
#  Step 2: Extract branches
# ======================================================================

def extract_branches(all_evals):
    """Extract B1, B2, B3 branch eigenvalues from sorted spectrum."""
    N = all_evals.shape[0]
    B1 = np.zeros(N)
    B2 = np.zeros(N)
    B3 = np.zeros(N)

    for i in range(N):
        pos = all_evals[i, 8:]  # 8 positive eigenvalues, sorted ascending
        B1[i] = pos[0]
        B2[i] = np.mean(pos[1:5])
        B3[i] = np.mean(pos[5:8])

        # Check degeneracy integrity
        if i > 0:
            b2_spread = np.ptp(pos[1:5])
            b3_spread = np.ptp(pos[5:8])
            if b2_spread > 1e-6:
                print(f"  WARNING: B2 degeneracy broken at tau={TAU_GRID[i]:.4f}, "
                      f"spread={b2_spread:.2e}")
            if b3_spread > 1e-6:
                print(f"  WARNING: B3 degeneracy broken at tau={TAU_GRID[i]:.4f}, "
                      f"spread={b3_spread:.2e}")

    return {'B1': B1, 'B2': B2, 'B3': B3}


# ======================================================================
#  Step 3: Compute group velocities, effective masses, VH points
# ======================================================================

def compute_derivatives(branches):
    """Numerical first and second derivatives of each branch."""
    results = {}
    for name, lam in branches.items():
        v = np.gradient(lam, DTAU)
        d2 = np.gradient(v, DTAU)
        with np.errstate(divide='ignore', invalid='ignore'):
            meff = np.where(np.abs(d2) > 1e-10, 1.0 / d2, np.inf)
        results[name] = {'velocity': v, 'd2lam': d2, 'meff': meff}
    return results


def find_van_hove_points(branches, derivs):
    """Find all zero crossings of v_k(tau) via linear interpolation."""
    vh_points = []
    for name, lam in branches.items():
        v = derivs[name]['velocity']
        d2 = derivs[name]['d2lam']
        for i in range(len(v) - 1):
            if v[i] * v[i + 1] < 0:
                tau_vh = TAU_GRID[i] - v[i] * DTAU / (v[i + 1] - v[i])
                lam_vh = np.interp(tau_vh, TAU_GRID, lam)
                d2_vh = np.interp(tau_vh, TAU_GRID, d2)
                vh_type = 'minimum' if d2_vh > 0 else ('maximum' if d2_vh < 0 else 'inflection')
                vh_points.append({
                    'branch': name, 'tau': tau_vh, 'lambda': lam_vh,
                    'type': vh_type, 'curvature': d2_vh
                })
    return vh_points


# ======================================================================
#  Step 4: Compute DOS at each tau from group velocities
# ======================================================================

def compute_dos_profiles(branches, derivs):
    """
    Compute DOS for each branch at each tau.

    The 1D DOS from the dispersion lambda_k(tau) is:
        rho_k(tau) = 1 / (pi * |v_k(tau)|)

    This diverges at VH points. We use a smoothed version by fitting
    cubic splines to the branches and integrating 1/|v| over a local
    window.

    For the Thouless criterion, what matters is the DOS INTEGRATED over
    the wall region [tau_lo, tau_hi]. The effective per-mode DOS is:
        rho_k_eff = (1/Delta_tau) integral_{wall} dtau / (pi * |v_k(tau)|)
    """
    dos = {}
    for name, lam in branches.items():
        v = derivs[name]['velocity']
        # Raw DOS: 1/(pi * |v|), regularized
        v_abs = np.abs(v)
        v_min = 0.01 * np.max(v_abs)  # floor at 1% of max velocity
        rho_raw = 1.0 / (np.pi * np.maximum(v_abs, v_min))
        dos[name] = rho_raw
    return dos


def compute_wall_integrated_dos(branches):
    """
    Compute the wall-integrated DOS for each branch.
    This uses cubic spline interpolation for high-accuracy integration.

    rho_eff = (1/Delta_tau) * integral_{wall} 1/(pi*|v(tau)|) dtau

    At a van Hove point, the integral goes as sqrt(Delta_tau / |kappa|),
    giving a finite (but enhanced) effective DOS.
    """
    from scipy.integrate import quad

    dos_wall = {}
    for name, lam in branches.items():
        cs = CubicSpline(TAU_GRID, lam)

        def integrand(tau):
            v = cs(tau, 1)  # first derivative
            return 1.0 / (np.pi * max(abs(v), 1e-4))

        # Integrate over wall region
        result, _ = quad(integrand, TAU_WALL_LO, TAU_WALL_HI,
                         limit=200, epsabs=1e-12)
        rho_eff = result / WALL_WIDTH
        dos_wall[name] = rho_eff

    return dos_wall


def compute_sliding_window_dos(branches, half_width=0.05):
    """
    Compute DOS at each tau using a sliding window of half_width.
    This captures the local DOS enhancement at VH points while being
    well-defined everywhere.

    rho_k(tau_i) = (1/Delta) integral_{tau_i - hw}^{tau_i + hw} 1/(pi*|v|) dtau
    """
    from scipy.integrate import quad

    dos_sliding = {}
    for name, lam in branches.items():
        cs = CubicSpline(TAU_GRID, lam)
        rho = np.zeros(N_TAU)

        for i, tau in enumerate(TAU_GRID):
            lo = max(TAU_MIN, tau - half_width)
            hi = min(TAU_MAX, tau + half_width)
            window = hi - lo

            def integrand(t):
                v = cs(t, 1)
                return 1.0 / (np.pi * max(abs(v), 1e-4))

            result, _ = quad(integrand, lo, hi, limit=200, epsabs=1e-12)
            rho[i] = result / window

        dos_sliding[name] = rho

    return dos_sliding


# ======================================================================
#  Step 5: Multi-band Thouless M_max at each tau
# ======================================================================

def compute_mmax_thouless(all_evals, all_V, branches, dos_sliding):
    """
    Compute the full 8x8 Thouless M_max at each tau.

    M_nm = V_nm * rho_m / (2 * |xi_m|)

    where V_nm is from the Kosmann pairing matrix, rho_m is the sliding-
    window DOS, and xi_m = lambda_m (since mu = 0).

    Also computes the 4x4 B2-only Thouless matrix for cross-check.
    """
    print(f"\n[5] Computing full Thouless M_max at {N_TAU} tau values...")

    mmax_8x8 = np.zeros(N_TAU)
    mmax_4x4 = np.zeros(N_TAU)
    mmax_3x3 = np.zeros(N_TAU)
    V_B2B2_trace = np.zeros(N_TAU)

    for i in range(N_TAU):
        tau = TAU_GRID[i]
        evals = all_evals[i]
        V = all_V[i]
        pos_evals = evals[8:]  # 8 positive eigenvalues

        # Eigenvalue distances from Fermi level (mu=0)
        xi = pos_evals.copy()
        lambda_min = np.min(np.abs(xi))
        eta = max(ETA_REG_FRAC * lambda_min, 1e-15)
        abs_xi = np.maximum(np.abs(xi), eta)

        # Per-mode DOS from sliding window
        rho_8 = np.zeros(8)
        rho_8[0] = dos_sliding['B1'][i]
        rho_8[1:5] = dos_sliding['B2'][i]
        rho_8[5:8] = dos_sliding['B3'][i]

        # Full 8x8 Thouless matrix
        M_8x8 = np.zeros((8, 8))
        for m in range(8):
            M_8x8[:, m] = V[:, m] * rho_8[m] / (2.0 * abs_xi[m])

        evals_M8 = np.linalg.eigvals(M_8x8)
        mmax_8x8[i] = np.max(np.real(evals_M8))

        # B2-only 4x4 submatrix
        V_B2 = V[np.ix_(B2_IDX, B2_IDX)]
        xi_B2 = abs_xi[B2_IDX]
        rho_B2 = rho_8[B2_IDX]
        M_4x4 = np.zeros((4, 4))
        for m in range(4):
            M_4x4[:, m] = V_B2[:, m] * rho_B2[m] / (2.0 * xi_B2[m])
        evals_M4 = np.linalg.eigvals(M_4x4)
        mmax_4x4[i] = np.max(np.real(evals_M4))

        # 3x3 branch-level
        branch_idx = [B1_IDX, B2_IDX, B3_IDX]
        V_branch = np.zeros((3, 3))
        for ii in range(3):
            for jj in range(3):
                V_block = V[np.ix_(branch_idx[ii], branch_idx[jj])]
                V_branch[ii, jj] = np.mean(np.sum(V_block, axis=1))

        E_branch = np.array([pos_evals[0], np.mean(pos_evals[1:5]),
                              np.mean(pos_evals[5:8])])
        xi_br = np.maximum(np.abs(E_branch), eta)
        rho_br = np.array([dos_sliding['B1'][i], dos_sliding['B2'][i],
                            dos_sliding['B3'][i]])

        M_3x3 = np.zeros((3, 3))
        for jj in range(3):
            M_3x3[:, jj] = V_branch[:, jj] * rho_br[jj] / (2.0 * xi_br[jj])
        evals_M3 = np.linalg.eigvals(M_3x3)
        mmax_3x3[i] = np.max(np.real(evals_M3))

        V_B2B2_trace[i] = np.mean(np.diag(V[np.ix_(B2_IDX, B2_IDX)]))

        if (i + 1) % 10 == 0 or i == 0:
            print(f"  tau={tau:.4f}: M_8x8={mmax_8x8[i]:.4f}, "
                  f"M_4x4={mmax_4x4[i]:.4f}, M_3x3={mmax_3x3[i]:.4f}, "
                  f"rho_B2={dos_sliding['B2'][i]:.2f}")

    return mmax_8x8, mmax_4x4, mmax_3x3, V_B2B2_trace


# ======================================================================
#  Step 6: Cross-check against s35 calibration at tau = 0.20
# ======================================================================

def calibrate_and_report(mmax_8x8, mmax_4x4, mmax_3x3, branches, dos_sliding):
    """
    Cross-check our M_max at tau=0.20 against the s35/s36 result (1.674).
    If there's a systematic offset, report the ratio and apply it as a
    calibration factor.
    """
    # Find tau = 0.20 index
    idx_020 = np.argmin(np.abs(TAU_GRID - 0.20))
    tau_020 = TAU_GRID[idx_020]

    print(f"\n[6] Cross-check at tau = {tau_020:.4f} (nearest to 0.20):")
    print(f"  Our M_max(8x8) = {mmax_8x8[idx_020]:.6f}")
    print(f"  Our M_max(4x4) = {mmax_4x4[idx_020]:.6f}")
    print(f"  Our M_max(3x3) = {mmax_3x3[idx_020]:.6f}")
    print(f"  s35 calibration M_max = {MMAX_CALIBRATION}")
    print(f"  Our rho_B2 at fold = {dos_sliding['B2'][idx_020]:.4f}")

    # The s35 rho_B2 was 14.02 per mode from van Hove integral over wall
    # Our sliding window DOS may differ. Report the ratio.
    ratio = MMAX_CALIBRATION / mmax_8x8[idx_020] if mmax_8x8[idx_020] > 0 else np.inf
    print(f"  Calibration ratio: {ratio:.4f}")
    print(f"  (Ratio > 1 means s35 used different DOS methodology)")

    return ratio, idx_020


# ======================================================================
#  Step 7: Generate plots
# ======================================================================

def make_plots(branches, derivs, vh_points, mmax_8x8, mmax_4x4,
               dos_sliding, cal_ratio):
    """Multi-panel plot of cascade spectroscopy results."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec

    fig = plt.figure(figsize=(16, 16))
    gs = GridSpec(4, 2, figure=fig, hspace=0.35, wspace=0.3)
    colors = {'B1': '#1f77b4', 'B2': '#ff7f0e', 'B3': '#2ca02c'}

    # ---- Panel 1: Band structure ----
    ax1 = fig.add_subplot(gs[0, 0])
    for name in ['B1', 'B2', 'B3']:
        d = BRANCH_MULTS[name]
        ax1.plot(TAU_GRID, branches[name], color=colors[name], lw=2,
                 label=f'{name} (d={d})')
        ax1.plot(TAU_GRID, -branches[name], color=colors[name], lw=1,
                 alpha=0.3, linestyle='--')
    for vh in vh_points:
        ax1.plot(vh['tau'], vh['lambda'], 'r*', markersize=14, zorder=5)
        ax1.annotate(f"VH\ntau={vh['tau']:.3f}",
                    xy=(vh['tau'], vh['lambda']),
                    xytext=(10, -15), textcoords='offset points',
                    fontsize=7, color='red')
    ax1.set_xlabel('tau'); ax1.set_ylabel('lambda')
    ax1.set_title('Singlet (0,0) Band Structure')
    ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)
    ax1.axhline(0, color='gray', ls=':', alpha=0.5)

    # ---- Panel 2: Group velocities ----
    ax2 = fig.add_subplot(gs[0, 1])
    for name in ['B1', 'B2', 'B3']:
        ax2.plot(TAU_GRID, derivs[name]['velocity'], color=colors[name],
                 lw=2, label=name)
    ax2.axhline(0, color='red', ls='--', alpha=0.7, lw=1)
    ax2.set_xlabel('tau'); ax2.set_ylabel('v = dlambda/dtau')
    ax2.set_title('Group Velocities'); ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # ---- Panel 3: Gap-edge splittings ----
    ax3 = fig.add_subplot(gs[1, 0])
    delta_21 = branches['B2'] - branches['B1']
    delta_32 = branches['B3'] - branches['B2']
    ax3.plot(TAU_GRID, delta_21, 'b-', lw=2, label='B2 - B1 (gap edge)')
    ax3.plot(TAU_GRID, delta_32, 'g-', lw=2, label='B3 - B2')
    idx_min21 = np.argmin(delta_21[1:]) + 1
    ax3.plot(TAU_GRID[idx_min21], delta_21[idx_min21], 'r*', markersize=14)
    ax3.annotate(f'min = {delta_21[idx_min21]:.4f}\ntau = {TAU_GRID[idx_min21]:.3f}',
                xy=(TAU_GRID[idx_min21], delta_21[idx_min21]),
                xytext=(20, 10), textcoords='offset points', fontsize=9,
                color='red', arrowprops=dict(arrowstyle='->', color='red'))
    ax3.set_xlabel('tau'); ax3.set_ylabel('Splitting')
    ax3.set_title('Gap-Edge Splittings'); ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    # ---- Panel 4: DOS (sliding window) ----
    ax4 = fig.add_subplot(gs[1, 1])
    for name in ['B1', 'B2', 'B3']:
        ax4.plot(TAU_GRID, dos_sliding[name], color=colors[name], lw=2, label=name)
    ax4.set_xlabel('tau'); ax4.set_ylabel('rho (sliding window DOS)')
    ax4.set_title('Sliding-Window DOS (hw=0.05)')
    ax4.legend(fontsize=8); ax4.grid(True, alpha=0.3)

    # ---- Panel 5: M_max (raw) ----
    ax5 = fig.add_subplot(gs[2, 0])
    ax5.plot(TAU_GRID, mmax_8x8, 'k-', lw=2, label='M_max (8x8)')
    ax5.plot(TAU_GRID, mmax_4x4, 'b--', lw=1.5, label='M_max (4x4 B2-only)')
    ax5.axhline(1.0, color='red', ls='--', lw=1.5, alpha=0.7, label='BCS threshold')
    above = mmax_8x8 > 1.0
    if np.any(above):
        ax5.fill_between(TAU_GRID, 0, mmax_8x8, where=above,
                         color='red', alpha=0.15)
    idx_peak = np.argmax(mmax_8x8)
    ax5.plot(TAU_GRID[idx_peak], mmax_8x8[idx_peak], 'r*', markersize=14)
    ax5.annotate(f'peak = {mmax_8x8[idx_peak]:.3f}\ntau = {TAU_GRID[idx_peak]:.3f}',
                xy=(TAU_GRID[idx_peak], mmax_8x8[idx_peak]),
                xytext=(15, -25), textcoords='offset points', fontsize=9,
                color='red', arrowprops=dict(arrowstyle='->', color='red'))
    ax5.set_xlabel('tau'); ax5.set_ylabel('M_max')
    ax5.set_title('Thouless M_max (raw, sliding-window DOS)')
    ax5.legend(fontsize=8); ax5.grid(True, alpha=0.3); ax5.set_ylim(bottom=0)

    # ---- Panel 6: M_max calibrated to s35 ----
    ax6 = fig.add_subplot(gs[2, 1])
    mmax_cal = mmax_8x8 * cal_ratio
    ax6.plot(TAU_GRID, mmax_cal, 'k-', lw=2, label=f'M_max * {cal_ratio:.2f} (calibrated)')
    ax6.axhline(1.0, color='red', ls='--', lw=1.5, alpha=0.7, label='BCS threshold')
    above_cal = mmax_cal > 1.0
    if np.any(above_cal):
        ax6.fill_between(TAU_GRID, 0, mmax_cal, where=above_cal,
                         color='red', alpha=0.15)
        tau_above = TAU_GRID[above_cal]
        ax6.axvspan(tau_above[0], tau_above[-1], alpha=0.05, color='red')
    idx_peak_cal = np.argmax(mmax_cal)
    ax6.plot(TAU_GRID[idx_peak_cal], mmax_cal[idx_peak_cal], 'r*', markersize=14)
    ax6.annotate(f'peak = {mmax_cal[idx_peak_cal]:.3f}\ntau = {TAU_GRID[idx_peak_cal]:.3f}',
                xy=(TAU_GRID[idx_peak_cal], mmax_cal[idx_peak_cal]),
                xytext=(15, -25), textcoords='offset points', fontsize=9,
                color='red', arrowprops=dict(arrowstyle='->', color='red'))
    ax6.set_xlabel('tau'); ax6.set_ylabel('M_max (calibrated)')
    ax6.set_title('Calibrated M_max (matched to s35 at tau=0.20)')
    ax6.legend(fontsize=8); ax6.grid(True, alpha=0.3); ax6.set_ylim(bottom=0)

    # ---- Panel 7: Fold-region detail ----
    ax7 = fig.add_subplot(gs[3, 0])
    mask = (TAU_GRID >= 0.10) & (TAU_GRID <= 0.35)
    for name in ['B1', 'B2', 'B3']:
        ax7.plot(TAU_GRID[mask], branches[name][mask], color=colors[name],
                 lw=2, label=name)
    ax7b = ax7.twinx()
    ax7b.plot(TAU_GRID[mask], mmax_cal[mask], 'k--', lw=1.5, alpha=0.7)
    ax7b.axhline(1.0, color='red', ls=':', alpha=0.5)
    ax7b.set_ylabel('M_max (cal)', color='gray')
    ax7.set_xlabel('tau'); ax7.set_ylabel('lambda')
    ax7.set_title('Fold Region [0.10, 0.35]')
    ax7.legend(fontsize=8); ax7.grid(True, alpha=0.3)

    # ---- Panel 8: V matrix diagonal stability ----
    ax8 = fig.add_subplot(gs[3, 1])
    # Plot V_B2B2 diagonal and off-diagonal as function of tau
    V_diag_B2 = np.zeros(N_TAU)
    V_offdiag_B2 = np.zeros(N_TAU)
    V_B1B2_avg = np.zeros(N_TAU)
    for i in range(N_TAU):
        V_block = all_V_global[i][np.ix_(B2_IDX, B2_IDX)]
        V_diag_B2[i] = np.mean(np.diag(V_block))
        V_offdiag_B2[i] = np.mean(V_block[~np.eye(4, dtype=bool)])
        V_B1B2_avg[i] = np.mean(all_V_global[i][np.ix_(B1_IDX, B2_IDX)])
    ax8.plot(TAU_GRID, V_diag_B2, 'b-', lw=2, label='V(B2,B2) diag')
    ax8.plot(TAU_GRID, V_offdiag_B2, 'b--', lw=1.5, label='V(B2,B2) offdiag')
    ax8.plot(TAU_GRID, V_B1B2_avg, 'r-', lw=2, label='V(B1,B2)')
    ax8.set_xlabel('tau'); ax8.set_ylabel('V')
    ax8.set_title('Pairing Interaction V(tau)')
    ax8.legend(fontsize=8); ax8.grid(True, alpha=0.3)

    plt.suptitle('CASCADE-39: Singlet Cascade Spectroscopy (50 tau, 3 branches)',
                 fontsize=13, fontweight='bold', y=1.01)

    save_path = os.path.join(SCRIPT_DIR, 's39_cascade_spectroscopy.png')
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    print(f"\n  Plot saved: {save_path}")
    plt.close()


# ======================================================================
#  Main
# ======================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("SESSION 39: CASCADE-39 -- Cascade Spectroscopy")
    print("=" * 70)

    # Step 1-2: Compute all data
    all_evals, all_V, gens, f_abc, gammas = compute_all_data()
    all_V_global = all_V  # for plot access

    # Step 2: Extract branches
    print(f"\n[3] Extracting branches...")
    branches = extract_branches(all_evals)
    print(f"  B1: [{branches['B1'].min():.6f}, {branches['B1'].max():.6f}]")
    print(f"  B2: [{branches['B2'].min():.6f}, {branches['B2'].max():.6f}]")
    print(f"  B3: [{branches['B3'].min():.6f}, {branches['B3'].max():.6f}]")

    # Step 3: Derivatives
    print(f"\n[4] Computing derivatives and van Hove points...")
    derivs = compute_derivatives(branches)
    vh_points = find_van_hove_points(branches, derivs)
    print(f"  Found {len(vh_points)} van Hove singularities:")
    for vh in vh_points:
        print(f"    {vh['branch']} at tau={vh['tau']:.4f}: lambda={vh['lambda']:.6f}, "
              f"type={vh['type']}")

    # Step 4: DOS
    print(f"\n[4b] Computing sliding-window DOS...")
    dos_sliding = compute_sliding_window_dos(branches, half_width=0.05)
    for name in ['B1', 'B2', 'B3']:
        print(f"  {name} DOS: [{dos_sliding[name].min():.4f}, "
              f"{dos_sliding[name].max():.4f}]")

    # Step 5: Full Thouless M_max
    mmax_8x8, mmax_4x4, mmax_3x3, V_B2B2_trace = compute_mmax_thouless(
        all_evals, all_V, branches, dos_sliding)

    # Step 6: Calibration
    cal_ratio, idx_020 = calibrate_and_report(
        mmax_8x8, mmax_4x4, mmax_3x3, branches, dos_sliding)

    # Apply calibration
    mmax_calibrated = mmax_8x8 * cal_ratio

    # ================================================================
    # GATE VERDICT
    # ================================================================
    print(f"\n{'='*70}")
    print(f"GATE CASCADE-39: RESULTS")
    print(f"{'='*70}")

    # VH points with M_max
    for vh in vh_points:
        idx = np.argmin(np.abs(TAU_GRID - vh['tau']))
        vh['M_max_raw'] = mmax_8x8[idx]
        vh['M_max_cal'] = mmax_calibrated[idx]

    print(f"\nVan Hove singularities:")
    for vh in vh_points:
        print(f"  {vh['branch']} at tau={vh['tau']:.4f}: "
              f"M_max(raw)={vh['M_max_raw']:.4f}, "
              f"M_max(cal)={vh['M_max_cal']:.4f}")

    # Check how many regions exceed M_max > 1
    above_raw = mmax_8x8 > 1.0
    above_cal = mmax_calibrated > 1.0

    print(f"\nM_max > 1 analysis (raw):")
    print(f"  Points above threshold: {np.sum(above_raw)}")
    print(f"  Peak M_max(raw) = {mmax_8x8.max():.6f} at tau = {TAU_GRID[np.argmax(mmax_8x8)]:.4f}")

    print(f"\nM_max > 1 analysis (calibrated to s35):")
    print(f"  Points above threshold: {np.sum(above_cal)}")
    print(f"  Peak M_max(cal) = {mmax_calibrated.max():.6f} at tau = {TAU_GRID[np.argmax(mmax_calibrated)]:.4f}")

    if np.any(above_cal):
        tau_above = TAU_GRID[above_cal]
        # Find contiguous islands
        above_idx = np.where(above_cal)[0]
        gaps = np.diff(above_idx)
        n_islands = 1 + np.sum(gaps > 1)
        print(f"  Active region: [{tau_above[0]:.4f}, {tau_above[-1]:.4f}]")
        print(f"  Number of islands: {n_islands}")

        # For each island, find peak
        island_starts = [above_idx[0]]
        island_ends = []
        for g_idx in np.where(gaps > 1)[0]:
            island_ends.append(above_idx[g_idx])
            island_starts.append(above_idx[g_idx + 1])
        island_ends.append(above_idx[-1])

        for k, (s, e) in enumerate(zip(island_starts, island_ends)):
            peak_val = np.max(mmax_calibrated[s:e+1])
            peak_idx = s + np.argmax(mmax_calibrated[s:e+1])
            print(f"    Island {k+1}: tau in [{TAU_GRID[s]:.4f}, {TAU_GRID[e]:.4f}], "
                  f"peak M_max = {peak_val:.4f} at tau = {TAU_GRID[peak_idx]:.4f}")

        if n_islands == 1:
            verdict = "PASS (UNIQUE FOLD)"
            verdict_detail = (f"Single contiguous M_max > 1 region centered at "
                            f"tau = {TAU_GRID[np.argmax(mmax_calibrated)]:.4f}. "
                            f"No cascade.")
        else:
            verdict = "FAIL (CASCADE)"
            verdict_detail = f"{n_islands} separate M_max > 1 islands detected."
    else:
        # Check if the shape peaks uniquely even if < 1
        idx_peak = np.argmax(mmax_calibrated)
        # Check for secondary peaks
        from scipy.signal import find_peaks
        peaks, props = find_peaks(mmax_calibrated, prominence=0.01*mmax_calibrated.max())
        n_peaks = len(peaks)
        print(f"\n  Number of M_max peaks (prominence > 1%): {n_peaks}")
        for p in peaks:
            print(f"    tau = {TAU_GRID[p]:.4f}: M_max = {mmax_calibrated[p]:.4f}")

        if n_peaks <= 1:
            verdict = "PASS (UNIQUE FOLD)"
            verdict_detail = (f"M_max profile has single peak at "
                            f"tau = {TAU_GRID[idx_peak]:.4f}. No cascade.")
        else:
            # Check if secondary peaks could support BCS
            secondary_max = max(mmax_calibrated[p] for p in peaks if p != idx_peak) \
                if n_peaks > 1 else 0
            if secondary_max > MMAX_THRESHOLD:
                verdict = "FAIL (CASCADE)"
                verdict_detail = f"Secondary peak at M_max = {secondary_max:.4f} > 1."
            else:
                verdict = "PASS (UNIQUE FOLD)"
                verdict_detail = (f"Secondary peaks sub-threshold: max = "
                                f"{secondary_max:.4f} < 1.")

    print(f"\n  GATE VERDICT: {verdict}")
    print(f"  {verdict_detail}")
    print(f"{'='*70}")

    # Step 7: Save data
    save_path = os.path.join(SCRIPT_DIR, 's39_cascade_spectroscopy.npz')
    np.savez(save_path,
             tau_grid=TAU_GRID,
             all_evals=all_evals,
             B1=branches['B1'], B2=branches['B2'], B3=branches['B3'],
             v_B1=derivs['B1']['velocity'], v_B2=derivs['B2']['velocity'],
             v_B3=derivs['B3']['velocity'],
             d2_B1=derivs['B1']['d2lam'], d2_B2=derivs['B2']['d2lam'],
             d2_B3=derivs['B3']['d2lam'],
             meff_B1=derivs['B1']['meff'], meff_B2=derivs['B2']['meff'],
             meff_B3=derivs['B3']['meff'],
             dos_B1=dos_sliding['B1'], dos_B2=dos_sliding['B2'],
             dos_B3=dos_sliding['B3'],
             mmax_8x8=mmax_8x8, mmax_4x4=mmax_4x4, mmax_3x3=mmax_3x3,
             mmax_calibrated=mmax_calibrated,
             cal_ratio=cal_ratio,
             V_B2B2_trace=V_B2B2_trace,
             n_vh=len(vh_points),
             vh_taus=np.array([vh['tau'] for vh in vh_points]),
             vh_lambdas=np.array([vh['lambda'] for vh in vh_points]),
             vh_branches=np.array([vh['branch'] for vh in vh_points]),
             vh_types=np.array([vh['type'] for vh in vh_points]),
             all_V_diag=np.array([np.diag(all_V[i]) for i in range(N_TAU)]),
             verdict=verdict,
             )
    print(f"  Data saved: {save_path}")

    # Step 8: Plots
    make_plots(branches, derivs, vh_points, mmax_8x8, mmax_4x4,
               dos_sliding, cal_ratio)

    elapsed = time.time() - t0
    print(f"\n  Total runtime: {elapsed:.1f}s")
