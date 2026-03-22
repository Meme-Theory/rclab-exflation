#!/usr/bin/env python3
"""
s30b_sdw_grid.py — Seeley-DeWitt shortcut on U(2)-invariant 2D grid
====================================================================

Session 30Ba Step 1: Compute scalar curvature, Seeley-DeWitt coefficients,
Weinberg angle, and gauge coupling ratio on a 21x21 grid in (tau, epsilon)
on the volume-preserving U(2)-invariant surface.

Parameterization (volume-preserving, orthogonal to Jensen tangent):
  log L1 = 2*tau - 11*eps/N
  log L2 = -2*tau - 7*eps/N
  log L3 = tau + 8*eps/N
  N = sqrt(234) = |T2_DIR|

  tau in [0.0, 0.60], 21 points
  eps in [-0.15, 0.15], 21 points

At each grid point:
  1. R (scalar curvature via full Riemann tensor from connection coefficients)
  2. a_2 ~ R * Vol (Seeley-DeWitt second coefficient)
  3. sin^2(theta_W) = L2 / (L1 + L2)
  4. g1/g2 = sqrt(L2/L1)
  5. Volume factor = L1 * L2^3 * L3^4

The scalar curvature is computed from the full Levi-Civita connection on SU(3)
(not from an analytic formula, which has convention ambiguities).

Author: phonon-exflation-sim agent, Session 30Ba
Date: 2026-02-28
"""

import numpy as np
from numpy.linalg import eigvalsh
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    u2_invariant_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ───────────────────────────────────────────────────────────
DATA_DIR = Path(SCRIPT_DIR)
OUT_NPZ = DATA_DIR / 's30b_sdw_grid.npz'
OUT_PNG = DATA_DIR / 's30b_sdw_grid.png'

# Grid dimensions
N_TAU = 21
N_EPS = 21
TAU_MIN, TAU_MAX = 0.0, 0.60
EPS_MIN, EPS_MAX = -0.15, 0.15

# T2 normalization
T2_DIR = np.array([-11.0, -7.0, 8.0])
N_T2 = np.sqrt(np.dot(T2_DIR, T2_DIR))  # sqrt(234) = 15.297


# =============================================================================
# MODULE 1: (tau, eps) -> (L1, L2, L3) parameterization
# =============================================================================

def tau_eps_to_lambdas(tau, eps):
    """
    Convert (tau, eps) on the volume-preserving U(2)-invariant surface
    to scale factors (L1, L2, L3).

    log L1 = 2*tau - 11*eps/N
    log L2 = -2*tau - 7*eps/N
    log L3 = tau + 8*eps/N

    Volume = L1 * L2^3 * L3^4 = exp(0) = 1 exactly.
    Orthogonal to Jensen tangent (2, -2, 1): checked algebraically.

    Parameters
    ----------
    tau : float
        Jensen-direction parameter.
    eps : float
        T2-direction parameter (cross-block ratio shift).

    Returns
    -------
    L1, L2, L3 : float
        Scale factors for u(1), su(2), C^2 blocks.
    """
    L1 = np.exp(2.0 * tau - 11.0 * eps / N_T2)
    L2 = np.exp(-2.0 * tau - 7.0 * eps / N_T2)
    L3 = np.exp(tau + 8.0 * eps / N_T2)
    return L1, L2, L3


# =============================================================================
# MODULE 2: Scalar curvature from full Riemann tensor
# =============================================================================

def scalar_curvature(g_s, f_abc):
    """
    Compute scalar curvature R of a left-invariant metric on SU(3)
    from the full Levi-Civita connection and Riemann tensor.

    For left-invariant fields on a Lie group:
      R^d_{cab} = Gamma^d_{ce} Gamma^e_{ab} - Gamma^d_{ae} Gamma^e_{cb}
                  - f~_{ca}^e Gamma^d_{eb}
      Ric_{ab} = sum_c R^c_{acb}
      R = sum_a Ric_{aa}  (ON frame)

    Parameters
    ----------
    g_s : ndarray (8,8)
        Positive definite metric on su(3).
    f_abc : ndarray (8,8,8)
        Structure constants.

    Returns
    -------
    R_scalar : float
        Scalar curvature.
    Ric_sq : float
        |Ric|^2 = sum_{ab} Ric_{ab}^2 (diagnostic).
    """
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    n = 8
    # Riemann tensor: R^d_{cab}
    # R^d_{cab} = Gamma^d_{ce} Gamma^e_{ab} - Gamma^d_{ae} Gamma^e_{cb}
    #            - ft[c,a,f] * Gamma^d_{fb}
    # Using einsum for the two contraction terms:
    # Term 1: sum_e Gamma[d,c,e] * Gamma[e,a,b]
    # Term 2: -sum_e Gamma[d,a,e] * Gamma[e,c,b]
    # Term 3: -sum_f ft[c,a,f] * Gamma[d,f,b]

    # Ricci = R^c_{acb} = sum_c R[c,a,c,b]
    # = sum_{c,e} Gamma[c,c,e]*Gamma[e,a,b] - sum_{c,e} Gamma[c,a,e]*Gamma[e,c,b]
    #   - sum_{c,f} ft[c,a,f]*Gamma[c,f,b]

    # Direct Ricci computation (avoids building full Riemann):
    # Ric_{ab} = sum_c [sum_e Gamma[c,c,e]*Gamma[e,a,b]
    #                   - sum_e Gamma[c,a,e]*Gamma[e,c,b]
    #                   - sum_f ft[c,a,f]*Gamma[c,f,b]]

    # Term 1: sum_{c,e} Gamma[c,c,e] * Gamma[e,a,b]
    # Let trace_Gamma[e] = sum_c Gamma[c,c,e]
    trace_Gamma = np.einsum('cce->e', Gamma)  # (8,)
    term1 = np.einsum('e,eab->ab', trace_Gamma, Gamma)  # (8,8)

    # Term 2: -sum_{c,e} Gamma[c,a,e] * Gamma[e,c,b]
    term2 = -np.einsum('cae,ecb->ab', Gamma, Gamma)  # (8,8)

    # Term 3: -sum_{c,f} ft[c,a,f] * Gamma[c,f,b]
    term3 = -np.einsum('caf,cfb->ab', ft, Gamma)  # (8,8)

    Ric = term1 + term2 + term3

    R_scalar = float(np.trace(Ric))
    Ric_sq = float(np.sum(Ric * Ric))

    return R_scalar, Ric_sq


# =============================================================================
# MODULE 3: GRID COMPUTATION
# =============================================================================

def compute_sdw_grid(B_ab, f_abc):
    """
    Compute Seeley-DeWitt quantities on the 21x21 (tau, eps) grid.

    Returns arrays of R, a_2, sin^2(theta_W), g1/g2, volume, L1, L2, L3,
    and Ric^2 at each grid point.
    """
    tau_arr = np.linspace(TAU_MIN, TAU_MAX, N_TAU)
    eps_arr = np.linspace(EPS_MIN, EPS_MAX, N_EPS)

    # Output arrays
    R_grid = np.zeros((N_TAU, N_EPS))
    Ric_sq_grid = np.zeros((N_TAU, N_EPS))
    a2_grid = np.zeros((N_TAU, N_EPS))
    sin2_tw_grid = np.zeros((N_TAU, N_EPS))
    g1g2_grid = np.zeros((N_TAU, N_EPS))
    vol_grid = np.zeros((N_TAU, N_EPS))
    L1_grid = np.zeros((N_TAU, N_EPS))
    L2_grid = np.zeros((N_TAU, N_EPS))
    L3_grid = np.zeros((N_TAU, N_EPS))

    t_start = time.time()
    n_total = N_TAU * N_EPS
    n_done = 0

    for i, tau in enumerate(tau_arr):
        for j, eps in enumerate(eps_arr):
            L1, L2, L3 = tau_eps_to_lambdas(tau, eps)
            L1_grid[i, j] = L1
            L2_grid[i, j] = L2
            L3_grid[i, j] = L3

            # Weinberg angle and gauge coupling ratio (algebraic, no spectrum needed)
            sin2_tw_grid[i, j] = L2 / (L1 + L2)
            g1g2_grid[i, j] = np.sqrt(L2 / L1)

            # Volume factor
            vol_grid[i, j] = L1 * L2**3 * L3**4

            # Scalar curvature (from full connection)
            g = u2_invariant_metric(B_ab, L1, L2, L3)
            R, Ric_sq = scalar_curvature(g, f_abc)
            R_grid[i, j] = R
            Ric_sq_grid[i, j] = Ric_sq

            # Seeley-DeWitt a_2 coefficient: proportional to R * sqrt(det(g))
            # For relative comparison across the grid, use a_2 ~ R * vol^{1/2}
            # (the actual a_2 includes dim(S) and (4pi)^{-d/2} prefactors)
            vol_half = np.sqrt(vol_grid[i, j])
            a2_grid[i, j] = R * vol_half

            n_done += 1

        elapsed = time.time() - t_start
        rate = n_done / elapsed if elapsed > 0 else 0
        remaining = (n_total - n_done) / rate if rate > 0 else 0
        print(f"  tau={tau:.2f}: {n_done}/{n_total} pts "
              f"({elapsed:.1f}s elapsed, ~{remaining:.0f}s remaining)")

    return {
        'tau': tau_arr,
        'eps': eps_arr,
        'R': R_grid,
        'Ric_sq': Ric_sq_grid,
        'a2': a2_grid,
        'sin2_tw': sin2_tw_grid,
        'g1g2': g1g2_grid,
        'vol': vol_grid,
        'L1': L1_grid,
        'L2': L2_grid,
        'L3': L3_grid,
    }


# =============================================================================
# MODULE 4: PLOTTING
# =============================================================================

def plot_sdw_grid(results, out_png):
    """Generate 6-panel diagnostic plot of the SDW grid."""
    tau = results['tau']
    eps = results['eps']
    TAU, EPS = np.meshgrid(tau, eps, indexing='ij')

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # Panel 1: Scalar curvature R(tau, eps)
    ax = axes[0, 0]
    c = ax.contourf(TAU, EPS, results['R'], levels=30, cmap='RdBu_r')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(tau, np.zeros_like(tau), 'k--', linewidth=1, label='Jensen')
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('Scalar curvature R')
    ax.legend(fontsize=7)

    # Panel 2: sin^2(theta_W)
    ax = axes[0, 1]
    c = ax.contourf(TAU, EPS, results['sin2_tw'], levels=30, cmap='viridis')
    plt.colorbar(c, ax=ax, shrink=0.8)
    # Mark SM target contour
    cs = ax.contour(TAU, EPS, results['sin2_tw'], levels=[0.20, 0.231, 0.25],
                    colors=['white', 'red', 'white'], linewidths=[1, 2, 1])
    ax.clabel(cs, inline=True, fontsize=7)
    ax.plot(tau, np.zeros_like(tau), 'k--', linewidth=1)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('sin^2(theta_W)')

    # Panel 3: g1/g2 ratio
    ax = axes[0, 2]
    c = ax.contourf(TAU, EPS, results['g1g2'], levels=30, cmap='plasma')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(tau, np.zeros_like(tau), 'k--', linewidth=1)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('g_1/g_2 = sqrt(L_2/L_1)')

    # Panel 4: a_2 = R * sqrt(Vol)
    ax = axes[1, 0]
    c = ax.contourf(TAU, EPS, results['a2'], levels=30, cmap='coolwarm')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(tau, np.zeros_like(tau), 'k--', linewidth=1)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('a_2 ~ R * Vol^{1/2}')

    # Panel 5: Volume (should be ~1 everywhere)
    ax = axes[1, 1]
    c = ax.contourf(TAU, EPS, results['vol'], levels=30, cmap='YlOrRd')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('Volume L1*L2^3*L3^4')

    # Panel 6: |Ric|^2
    ax = axes[1, 2]
    c = ax.contourf(TAU, EPS, results['Ric_sq'], levels=30, cmap='inferno')
    plt.colorbar(c, ax=ax, shrink=0.8)
    ax.plot(tau, np.zeros_like(tau), 'k--', linewidth=1)
    ax.set_xlabel('tau')
    ax.set_ylabel('epsilon')
    ax.set_title('|Ric|^2')

    plt.suptitle('Session 30Ba Step 1: Seeley-DeWitt Grid on U(2)-invariant surface',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    print(f"Saved {out_png}")


# =============================================================================
# MODULE 5: MAIN
# =============================================================================

def main():
    t_start = time.time()
    print("=" * 70)
    print("Session 30Ba Step 1: Seeley-DeWitt Grid")
    print(f"  Grid: {N_TAU}x{N_EPS} = {N_TAU*N_EPS} points")
    print(f"  tau in [{TAU_MIN}, {TAU_MAX}], eps in [{EPS_MIN}, {EPS_MAX}]")
    print(f"  N_T2 = sqrt(234) = {N_T2:.6f}")
    print("=" * 70)

    # Infrastructure
    print("\n[SETUP] Building algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)

    # Validate parameterization
    print("\n[CHECK] Parameterization validation...")
    L1, L2, L3 = tau_eps_to_lambdas(0.0, 0.0)
    print(f"  (0,0): L1={L1:.6f}, L2={L2:.6f}, L3={L3:.6f} (should be 1,1,1)")
    assert abs(L1 - 1.0) < 1e-14 and abs(L2 - 1.0) < 1e-14 and abs(L3 - 1.0) < 1e-14

    L1, L2, L3 = tau_eps_to_lambdas(0.35, 0.0)
    L1_j = np.exp(0.7)
    L2_j = np.exp(-0.7)
    L3_j = np.exp(0.35)
    print(f"  (0.35,0): L1={L1:.6f} (ref {L1_j:.6f}), "
          f"L2={L2:.6f} (ref {L2_j:.6f}), "
          f"L3={L3:.6f} (ref {L3_j:.6f})")
    assert abs(L1 - L1_j) < 1e-14 and abs(L2 - L2_j) < 1e-14 and abs(L3 - L3_j) < 1e-14

    # Volume preservation
    for tau in [0.0, 0.15, 0.35, 0.60]:
        for eps in [-0.15, 0.0, 0.15]:
            L1, L2, L3 = tau_eps_to_lambdas(tau, eps)
            vol = L1 * L2**3 * L3**4
            assert abs(vol - 1.0) < 1e-12, f"Volume not preserved at tau={tau}, eps={eps}: {vol}"
    print("  Volume preservation: PASS (all grid corners)")

    # Compute grid
    print(f"\n[COMPUTE] Running SDW grid ({N_TAU*N_EPS} points)...")
    results = compute_sdw_grid(B_ab, f_abc)
    t_compute = time.time() - t_start

    # Summary statistics
    print(f"\n{'=' * 70}")
    print("GRID RESULTS SUMMARY")
    print(f"{'=' * 70}")

    R = results['R']
    sin2 = results['sin2_tw']
    g1g2 = results['g1g2']
    vol = results['vol']

    print(f"\nScalar curvature R:")
    print(f"  Range: [{np.min(R):.6f}, {np.max(R):.6f}]")
    print(f"  R(0,0) = {R[0, N_EPS//2]:.6f} (round metric)")
    print(f"  R(0.35,0) = {R[int(0.35/TAU_MAX*(N_TAU-1)), N_EPS//2]:.6f} (Jensen BCS min)")

    print(f"\nsin^2(theta_W):")
    print(f"  Range: [{np.min(sin2):.6f}, {np.max(sin2):.6f}]")
    print(f"  SM target: 0.231")
    # Check if 0.231 is in range
    if np.min(sin2) <= 0.231 <= np.max(sin2):
        print(f"  SM value IS within grid range")
    else:
        print(f"  SM value NOT in grid range (closest: {sin2.flat[np.argmin(np.abs(sin2 - 0.231))]:.6f})")

    print(f"\ng_1/g_2:")
    print(f"  Range: [{np.min(g1g2):.6f}, {np.max(g1g2):.6f}]")

    print(f"\nVolume (should be 1.0 everywhere):")
    print(f"  Range: [{np.min(vol):.12f}, {np.max(vol):.12f}]")
    print(f"  Max deviation from 1: {np.max(np.abs(vol - 1.0)):.2e}")

    # R along Jensen curve (eps=0)
    print(f"\nR along Jensen curve (eps=0):")
    j_col = N_EPS // 2  # eps=0 column
    tau_arr = results['tau']
    for i in range(0, N_TAU, 4):
        print(f"  tau={tau_arr[i]:.2f}: R={R[i, j_col]:.6f}")

    # Identify SDW landscape features
    # The spectral action V_spec ~ a_0 + a_2*R/Lambda^6 + ...
    # R increasing -> V_spec increases (for positive a_2 coefficient)
    # The BCS minimum from s29 is at tau~0.35.
    # We're interested in where R + F_BCS has a minimum.

    print(f"\nRuntime: {t_compute:.1f}s")

    # Save results
    print(f"\n[SAVE] Writing outputs...")
    np.savez_compressed(
        OUT_NPZ,
        tau=results['tau'],
        eps=results['eps'],
        R=R,
        Ric_sq=results['Ric_sq'],
        a2=results['a2'],
        sin2_tw=sin2,
        g1g2=g1g2,
        vol=vol,
        L1=results['L1'],
        L2=results['L2'],
        L3=results['L3'],
        N_T2=N_T2,
        T2_dir=T2_DIR,
        n_tau=N_TAU,
        n_eps=N_EPS,
    )
    print(f"  Saved: {OUT_NPZ}")

    # Plot
    plot_sdw_grid(results, OUT_PNG)

    print(f"\n{'=' * 70}")
    print(f"Step 1 COMPLETE. {N_TAU*N_EPS} SDW grid points computed in {t_compute:.1f}s.")
    print(f"{'=' * 70}")

    return results


if __name__ == '__main__':
    results = main()
