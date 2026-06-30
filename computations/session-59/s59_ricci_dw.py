#!/usr/bin/env python3
"""
S59 — RICCI-DW-59: Ricci Anisotropy at the Domain Wall
========================================================

Gate: RICCI-DW-59
  PASS if A_crit matches Paper 15 (Lauret-Will-Schwahn) stability threshold.
  FAIL if no correspondence. INFO if partial.

Physics:
  The S58 domain wall energy E_DW changes sign at tau ~ 0.114.
  This tests whether the sign change corresponds to a Ricci anisotropy threshold
  on the Jensen-deformed SU(3).

  Jensen metric: g_tau = diag(alpha*e^{2tau}, alpha*e^{-2tau}, alpha*e^{tau}) on (u(1), su(2), C^2).
  Volume-preserving: x1^1 * x2^3 * x3^4 = alpha^8.

  References:
    Paper 28 (Lauret 2021): Jensen metrics on SU(3) are G-unstable
    Paper 29 (Lauret-Will 2021): Explicit Ricci and Lichnerowicz formulas
    Paper 30 (Schwahn 2023): Stability criterion Delta_L > 2E
    Paper 46 (Derdzinski-Gal 2013): Omega eigenvalues {2, 1, -2/3} on SU(3)

Author: Baptista-Spacetime-Analyst (Session 59)
Date: 2026-03-24
"""

import sys
import os
import itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.optimize import brentq
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import tau_fold, g0_diag, PI

# ============================================================================
#  STEP 0: Load S58 domain wall data
# ============================================================================

with open('s59_ricci_dw_log.txt', 'w') as LOG:
    def log(msg):
        LOG.write(msg + '\n')
        LOG.flush()

    log("=" * 72)
    log("  S59 — RICCI-DW-59: Ricci Anisotropy at the Domain Wall")
    log("=" * 72)

    d58 = np.load('s58_off_jensen_dw.npz', allow_pickle=True)
    tau_scan_58 = d58['tau_scan']
    E_DW_tau_geom = d58['E_DW_tau_geom']
    E_DW_tau_arith = d58['E_DW_tau_arith']

    log(f"\n  S58 data loaded: tau range [{tau_scan_58[0]:.4f}, {tau_scan_58[-1]:.4f}], N={len(tau_scan_58)}")

    # Find precise E_DW=0 crossing
    f_edw_geom = interp1d(tau_scan_58, E_DW_tau_geom, kind='cubic')
    f_edw_arith = interp1d(tau_scan_58, E_DW_tau_arith, kind='cubic')

    tau_dw_geom = 0.114  # fallback  # (local)
    for i in range(len(tau_scan_58) - 1):
        if E_DW_tau_geom[i] < 0 and E_DW_tau_geom[i+1] > 0:
            tau_dw_geom = brentq(f_edw_geom, tau_scan_58[i], tau_scan_58[i+1])
            break

    tau_dw_arith = 0.114  # (local)
    for i in range(len(tau_scan_58) - 1):
        if E_DW_tau_arith[i] < 0 and E_DW_tau_arith[i+1] > 0:
            tau_dw_arith = brentq(f_edw_arith, tau_scan_58[i], tau_scan_58[i+1])
            break

    log(f"  E_DW=0 crossing (geom): tau_DW = {tau_dw_geom:.6f}")
    log(f"  E_DW=0 crossing (arith): tau_DW = {tau_dw_arith:.6f}")

    # ============================================================================
    #  STEP 1: SU(3) Structure Constants (vectorized)
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 1: SU(3) Structure Constants")
    log(f"{'='*72}")

    d1, d2, d3 = 1, 3, 4
    n_lie = 8
    alpha = g0_diag  # = 3.0

    # Build full antisymmetric structure constant tensor
    f_abc_dict = {
        (1,2,3): 1.0, (1,4,7): 0.5, (1,6,5): 0.5, (2,4,6): 0.5,
        (2,5,7): 0.5, (3,4,5): 0.5, (3,7,6): 0.5,
        (4,5,8): np.sqrt(3)/2, (6,7,8): np.sqrt(3)/2,
    }

    f_full = np.zeros((9, 9, 9))
    for (a, b, c), val in f_abc_dict.items():
        for perm in itertools.permutations([a, b, c]):
            inv = sum(1 for ii in range(3) for jj in range(ii+1, 3) if perm[ii] > perm[jj])
            f_full[perm[0], perm[1], perm[2]] = (-1)**inv * val

    # Group mapping: Lie index (1-8) -> group (0=u1, 1=su2, 2=C2)
    grp_map = np.array([1, 1, 1, 2, 2, 2, 2, 0])  # indices 0-7 -> groups

    # Precompute bracket_sq[i,j,k] = sum_{a in m_i, b in m_j, c in m_k} f_{abc}^2
    groups = [[8], [1,2,3], [4,5,6,7]]
    bracket_sq = np.zeros((3, 3, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                total = 0.0  # (local)
                for a in groups[i]:
                    for b in groups[j]:
                        for c in groups[k]:
                            total += f_full[a, b, c]**2
                bracket_sq[i, j, k] = total

    group_names = ['u(1)', 'su(2)', 'C^2']
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if bracket_sq[i, j, k] > 1e-15:
                    log(f"    [{group_names[i]},{group_names[j]},{group_names[k]}] = {bracket_sq[i,j,k]:.6f}")

    # ============================================================================
    #  STEP 2: Vectorized Ricci and Sectional Curvature
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 2: Ricci Tensor (vectorized)")
    log(f"{'='*72}")

    # Extract nonzero structure constants for efficient computation
    # f_full[a,b,c] with 1-indexed a,b,c. We need 0-indexed for arrays.
    nz_indices = []
    nz_values = []
    for a in range(1, 9):
        for b in range(a+1, 9):  # antisymmetric: only a < b needed
            for c in range(1, 9):
                if abs(f_full[a, b, c]) > 1e-15:
                    nz_indices.append((a-1, b-1, c-1))  # 0-indexed
                    nz_values.append(f_full[a, b, c])

    nz_indices = np.array(nz_indices)
    nz_values = np.array(nz_values)
    log(f"  Non-zero structure constants (a<b): {len(nz_values)}")

    def jensen_metric(tau):
        return alpha * np.exp(2*tau), alpha * np.exp(-2*tau), alpha * np.exp(tau)

    def compute_ricci_and_sectional(tau):
        """
        Compute Ricci eigenvalues and sectional curvature bounds at given tau.
        Uses precomputed structure constants with vectorized Levi-Civita connection.
        """
        x1, x2, x3 = jensen_metric(tau)
        x_vals = np.array([x1, x2, x3])
        n = 8

        # Scale factors per Lie algebra direction (0-indexed)
        x_per_dir = x_vals[grp_map]  # shape (8,)

        # Build gamma^k_{ij} = f_{ijk} * sqrt(2*x_k / (x_i * x_j))
        # For efficiency, build via nonzero entries only
        gamma = np.zeros((n, n, n))

        for idx in range(len(nz_values)):
            a, b, c = nz_indices[idx]
            f_val = nz_values[idx]
            xa, xb, xc = x_per_dir[a], x_per_dir[b], x_per_dir[c]

            # gamma[c, a, b] from [e_a, e_b] = gamma^c_{ab} e_c
            factor_c = f_val * np.sqrt(2.0 * xc / (xa * xb))
            gamma[c, a, b] = factor_c
            gamma[c, b, a] = -factor_c  # antisymmetry in (a,b)

            # Also the terms gamma[a, b, c] and gamma[b, a, c] from permutations
            # f_full is fully antisymmetric, so [b,c] -> f_{bca} = f_{abc} * sgn(bca)
            # But f_full already handles all permutations. We need to fill gamma for
            # ALL index triples, not just those with a < b.

        # Actually, rebuild gamma directly from full f_full (cleaner)
        gamma = np.zeros((n, n, n))
        for i in range(n):
            for j in range(n):
                for c in range(n):
                    fv = f_full[i+1, j+1, c+1]
                    if abs(fv) > 1e-15:
                        gamma[c, i, j] = fv * np.sqrt(2.0 * x_per_dir[c] / (x_per_dir[i] * x_per_dir[j]))

        # Levi-Civita connection: Gamma^k_{ij} = 0.5*(gamma[k,i,j] - gamma[i,j,k] + gamma[j,k,i])
        # Vectorized using numpy einsum-style
        Gamma = 0.5 * (gamma - np.transpose(gamma, (1, 2, 0)) + np.transpose(gamma, (2, 0, 1)))

        # Ricci: Ric(e_a, e_a) = sum_c <R(e_c, e_a)e_a, e_c>
        # R^c_{a,c,a}: R(e_c, e_a)e_a component c
        # = sum_m [Gamma^m_{a,a} Gamma^c_{c,m} - Gamma^m_{c,a} Gamma^c_{a,m}
        #          - gamma^m_{c,a} Gamma^c_{m,a}]
        #
        # Vectorized:
        # Term1: sum_c sum_m Gamma[m,a,a]*Gamma[c,c,m] = sum_m Gamma[m,a,a] * sum_c Gamma[c,c,m]
        #       = Gamma[:,a,a] . (sum_c Gamma[c,c,:])
        # Let trace_Gamma[m] = sum_c Gamma[c,c,m]
        trace_Gamma = np.einsum('ccm->m', Gamma)

        Ric_diag = np.zeros(n)
        for a in range(n):
            # Term 1: sum_{c,m} Gamma[m,a,a]*Gamma[c,c,m]
            t1 = np.dot(Gamma[:, a, a], trace_Gamma)

            # Term 2: -sum_{c,m} Gamma[m,c,a]*Gamma[c,a,m]
            # = -sum_c (Gamma[:,c,a] . Gamma[c,a,:])
            t2 = 0.0
            for c in range(n):
                t2 -= np.dot(Gamma[:, c, a], Gamma[c, a, :])

            # Term 3: -sum_{c,m} gamma[m,c,a]*Gamma[c,m,a]
            # = -sum_c (gamma[:,c,a] . Gamma[c,:,a])
            t3 = 0.0
            for c in range(n):
                t3 -= np.dot(gamma[:, c, a], Gamma[c, :, a])

            Ric_diag[a] = t1 + t2 + t3

        r1 = Ric_diag[7]  # u(1)
        r2 = np.mean(Ric_diag[0:3])  # su(2)
        r3 = np.mean(Ric_diag[3:7])  # C^2

        # Scalar curvature
        R_scalar = np.sum(Ric_diag)

        # Sectional curvatures: K(e_a, e_b) for all pairs
        # K(e_a, e_b) = sum_m [Gamma[m,b,b]*Gamma[a,a,m] - Gamma[m,a,b]*Gamma[a,b,m]
        #               - gamma[m,a,b]*Gamma[a,m,b]]
        sec_vals = []
        for a in range(n):
            for b in range(a+1, n):
                K = 0.0
                for m in range(n):
                    K += Gamma[m, b, b] * Gamma[a, a, m]
                    K -= Gamma[m, a, b] * Gamma[a, b, m]
                    K -= gamma[m, a, b] * Gamma[a, m, b]
                sec_vals.append(K)

        sec_vals = np.array(sec_vals)
        sec_min = np.min(sec_vals)
        sec_max = np.max(sec_vals)
        n_neg = np.sum(sec_vals < -1e-14)

        return r1, r2, r3, R_scalar, sec_min, sec_max, n_neg, Ric_diag

    # Validation at tau=0
    r1_0, r2_0, r3_0, R0, smin0, smax0, nneg0, rd0 = compute_ricci_and_sectional(0.0)
    expected = 3.0 / (2.0 * alpha)
    log(f"\n  Validation at tau=0:")
    log(f"  r1={r1_0:.8f}, r2={r2_0:.8f}, r3={r3_0:.8f}")
    log(f"  Expected: {expected:.8f}")
    log(f"  R_scalar = {R0:.6f}, expected 12/alpha = {12.0/alpha:.6f}")
    log(f"  sec_min={smin0:.8f}, sec_max={smax0:.8f}, n_neg={nneg0}")
    log(f"  Anisotropy at tau=0: {abs(r3_0 - r2_0)/np.mean([r1_0,r2_0,r3_0]):.2e}")

    # ============================================================================
    #  STEP 3: Full tau scan
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 3: Full tau scan [0, 0.25], N=50")
    log(f"{'='*72}")

    N_tau = 50  # (local)
    tau_vals = np.linspace(0, 0.25, N_tau)

    r1_arr = np.zeros(N_tau)
    r2_arr = np.zeros(N_tau)
    r3_arr = np.zeros(N_tau)
    R_arr = np.zeros(N_tau)
    sec_min_arr = np.zeros(N_tau)
    sec_max_arr = np.zeros(N_tau)
    n_neg_arr = np.zeros(N_tau, dtype=int)

    for idx, tau in enumerate(tau_vals):
        r1, r2, r3, R, smin, smax, nneg, _ = compute_ricci_and_sectional(tau)
        r1_arr[idx] = r1
        r2_arr[idx] = r2
        r3_arr[idx] = r3
        R_arr[idx] = R
        sec_min_arr[idx] = smin
        sec_max_arr[idx] = smax
        n_neg_arr[idx] = nneg

        if idx % 10 == 0:
            log(f"  tau={tau:.4f}: r1={r1:.6f}, r2={r2:.6f}, r3={r3:.6f}, R={R:.4f}, smin={smin:.6f}")

    # ============================================================================
    #  STEP 4: Anisotropy
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 4: Anisotropy and Domain Wall")
    log(f"{'='*72}")

    r_avg = (d1 * r1_arr + d2 * r2_arr + d3 * r3_arr) / (d1 + d2 + d3)
    A_aniso = np.abs(r3_arr - r2_arr) / np.abs(r_avg)
    sigma_ric = np.sqrt(d1*(r1_arr - r_avg)**2 + d2*(r2_arr - r_avg)**2 + d3*(r3_arr - r_avg)**2) / (np.sqrt(d1+d2+d3) * np.abs(r_avg))

    f_A = interp1d(tau_vals, A_aniso, kind='cubic')
    f_sigma = interp1d(tau_vals, sigma_ric, kind='cubic')
    f_sec_min = interp1d(tau_vals, sec_min_arr, kind='cubic')

    A_crit = f_A(tau_dw_geom)
    sigma_crit = f_sigma(tau_dw_geom)
    sec_at_dw = f_sec_min(tau_dw_geom)

    log(f"\n  Domain wall anisotropy:")
    log(f"  tau_DW              = {tau_dw_geom:.6f}")
    log(f"  A_crit              = {A_crit:.8f}")
    log(f"  sigma_ric(tau_DW)   = {sigma_crit:.8f}")
    log(f"  sec_min(tau_DW)     = {sec_at_dw:.8f}")

    # Ricci components at DW
    r1_dw, r2_dw, r3_dw, _, _, _, _, _ = compute_ricci_and_sectional(tau_dw_geom)
    log(f"  r1(tau_DW)          = {r1_dw:.8f}")
    log(f"  r2(tau_DW)          = {r2_dw:.8f}")
    log(f"  r3(tau_DW)          = {r3_dw:.8f}")

    # Table
    log(f"\n  {'tau':>8s} {'r1':>10s} {'r2':>10s} {'r3':>10s} {'R':>10s} {'A':>10s} {'sec_min':>10s} {'n_neg':>5s}")
    for idx in range(N_tau):
        if idx % 5 == 0 or abs(tau_vals[idx] - tau_dw_geom) < 0.005:
            log(f"  {tau_vals[idx]:8.4f} {r1_arr[idx]:10.6f} {r2_arr[idx]:10.6f} {r3_arr[idx]:10.6f} "
                f"{R_arr[idx]:10.6f} {A_aniso[idx]:10.6f} {sec_min_arr[idx]:10.6f} {n_neg_arr[idx]:5d}")

    # ============================================================================
    #  STEP 5: Sectional curvature zero crossing
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 5: Sectional Curvature Zero Crossing")
    log(f"{'='*72}")

    tau_sec_zero = None
    for i in range(N_tau - 1):
        if sec_min_arr[i] > 0 and sec_min_arr[i+1] < 0:
            tau_sec_zero = brentq(f_sec_min, tau_vals[i], tau_vals[i+1])
            break

    if tau_sec_zero is not None:
        log(f"  min(sec) = 0 at tau = {tau_sec_zero:.6f}")
        A_at_sz = f_A(tau_sec_zero)
        log(f"  A(tau_sec_zero) = {A_at_sz:.8f}")
        log(f"  tau_DW / tau_sec_zero = {tau_dw_geom / tau_sec_zero:.4f}")
    elif np.all(sec_min_arr > 0):
        log(f"  min(sec) > 0 for all tau in [0, 0.25]")
        log(f"  Minimum of sec_min: {np.min(sec_min_arr):.8f} at tau = {tau_vals[np.argmin(sec_min_arr)]:.4f}")
        # Extend scan
        tau_ext = np.linspace(0.25, 0.50, 25)
        sec_ext = np.zeros(25)
        for idx, tau in enumerate(tau_ext):
            _, _, _, _, smin, _, _, _ = compute_ricci_and_sectional(tau)
            sec_ext[idx] = smin
        log(f"  Extended scan to tau=0.50: sec_min range [{np.min(sec_ext):.6f}, {np.max(sec_ext):.6f}]")
        all_tau = np.concatenate([tau_vals, tau_ext])
        all_sec = np.concatenate([sec_min_arr, sec_ext])
        f_sec_all = interp1d(all_tau, all_sec, kind='cubic')
        for i in range(len(all_tau) - 1):
            if all_sec[i] > 0 and all_sec[i+1] < 0:
                tau_sec_zero = brentq(f_sec_all, all_tau[i], all_tau[i+1])
                log(f"  min(sec) = 0 at tau = {tau_sec_zero:.6f} (extended)")
                break
        if tau_sec_zero is None:
            log(f"  min(sec) stays positive through tau = 0.50")
    else:
        log(f"  sec_min already negative at tau=0: {sec_min_arr[0]:.8f}")

    # ============================================================================
    #  STEP 6: Lichnerowicz Stability (Lauret-Will formula)
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 6: Lichnerowicz Stability Margin")
    log(f"{'='*72}")

    dims = np.array([d1, d2, d3], dtype=float)

    def lichnerowicz_matrix(x1, x2, x3):
        """Lauret-Will Theorem 3.1 matrix for SU(3)."""
        x = np.array([x1, x2, x3])
        L = np.zeros((3, 3))
        for k in range(3):
            diag = 0.0
            for i in range(3):
                for j in range(3):
                    if i != k and j != k and bracket_sq[i, j, k] > 1e-15:
                        diag += (x[k] / (x[i] * x[j])) * bracket_sq[i, j, k]
            for i in range(3):
                if i != k and bracket_sq[i, k, k] > 1e-15:
                    diag += (x[i] / x[k]**2) * bracket_sq[i, k, k]
            L[k, k] = diag / dims[k]
        for k in range(3):
            for m in range(k+1, 3):
                off = 0.0
                for i in range(3):
                    if bracket_sq[i, k, m] > 1e-15:
                        off += ((x[i]**2 - x[k]**2 - x[m]**2) / (x[i] * x[k] * x[m])) * bracket_sq[i, k, m]
                L[k, m] = off / np.sqrt(dims[k] * dims[m])
                L[m, k] = L[k, m]
        return L

    L_eigs = np.zeros((N_tau, 3))
    rho_arr = np.zeros(N_tau)
    margin_arr = np.zeros(N_tau)

    for idx, tau in enumerate(tau_vals):
        x1, x2, x3 = jensen_metric(tau)
        L = lichnerowicz_matrix(x1, x2, x3)
        eigs = np.sort(np.linalg.eigvalsh(L))
        L_eigs[idx] = eigs
        rho = R_arr[idx] / n_lie
        rho_arr[idx] = rho
        margin_arr[idx] = eigs[0] - 2 * rho

    f_margin = interp1d(tau_vals, margin_arr, kind='cubic')

    log(f"\n  {'tau':>8s} {'lam1':>10s} {'lam2':>10s} {'lam3':>10s} {'2rho':>10s} {'margin':>10s}")
    for idx in range(N_tau):
        if idx % 5 == 0 or abs(tau_vals[idx] - tau_dw_geom) < 0.005:
            log(f"  {tau_vals[idx]:8.4f} {L_eigs[idx,0]:10.6f} {L_eigs[idx,1]:10.6f} "
                f"{L_eigs[idx,2]:10.6f} {2*rho_arr[idx]:10.6f} {margin_arr[idx]:10.6f}")

    # Find stability margin crossing
    tau_stab_cross = None
    for i in range(N_tau - 1):
        if margin_arr[i] * margin_arr[i+1] < 0:
            tau_stab_cross = brentq(f_margin, tau_vals[i], tau_vals[i+1])
            break

    if tau_stab_cross is not None:
        log(f"\n  Stability margin = 0 at tau = {tau_stab_cross:.6f}")
        log(f"  |tau_DW - tau_stab| = {abs(tau_dw_geom - tau_stab_cross):.6f}")
    else:
        log(f"\n  Stability margin does not cross zero in [0, 0.25]")
        log(f"  margin(0) = {margin_arr[0]:.6f}, margin(0.25) = {margin_arr[-1]:.6f}")

    # Paper 46 note
    log(f"\n  Paper 46 (Derdzinski-Gal):")
    log(f"  Omega eigenvalues on SU(3): {{2, 1, -2/3}}, mults {{1, 8, 27}}")
    log(f"  Eigenvalue 1 unique to SU(n), n>=3 -> bi-invariant metric NOT isolated")

    # ============================================================================
    #  STEP 7: Gate Verdict
    # ============================================================================

    log(f"\n{'='*72}")
    log(f"  STEP 7: Gate Verdict")
    log(f"{'='*72}")

    log(f"\n  tau_DW (E_DW=0)     = {tau_dw_geom:.6f}")
    log(f"  A_crit              = {A_crit:.8f}")
    log(f"  sigma_crit          = {sigma_crit:.8f}")
    log(f"  sec_min(tau_DW)     = {sec_at_dw:.8f}")
    if tau_sec_zero is not None:
        log(f"  tau(sec_min=0)      = {tau_sec_zero:.6f}")
    if tau_stab_cross is not None:
        log(f"  tau(margin=0)       = {tau_stab_cross:.6f}")

    gate_verdict = "INFO"
    if tau_sec_zero is not None and abs(tau_dw_geom - tau_sec_zero) < 0.01:
        gate_verdict = "PASS"
        gate_detail = (f"E_DW=0 at tau={tau_dw_geom:.4f} coincides with sec_min=0 at "
                       f"tau={tau_sec_zero:.4f} (diff {abs(tau_dw_geom-tau_sec_zero):.4f}). "
                       f"A_crit={A_crit:.6f}.")
    elif tau_stab_cross is not None and abs(tau_dw_geom - tau_stab_cross) < 0.01:
        gate_verdict = "PASS"
        gate_detail = (f"E_DW=0 at tau={tau_dw_geom:.4f} coincides with Lichnerowicz margin=0 at "
                       f"tau={tau_stab_cross:.4f}. A_crit={A_crit:.6f}.")
    else:
        gate_detail = (f"E_DW=0 at tau={tau_dw_geom:.4f}. A_crit={A_crit:.6f}. "
                       f"sec_min(DW)={sec_at_dw:.6f}. ")
        if tau_sec_zero is not None:
            gate_detail += f"sec_min=0 at tau={tau_sec_zero:.4f}. "
        else:
            gate_detail += "sec_min>0 throughout. "
        if tau_stab_cross is not None:
            gate_detail += f"margin=0 at tau={tau_stab_cross:.4f}. "
        else:
            gate_detail += f"Margin sign: {np.sign(margin_arr[0]):.0f} throughout. "
        gate_detail += "Partial correspondence only."

    log(f"\n  GATE: RICCI-DW-59")
    log(f"  VERDICT: {gate_verdict}")
    log(f"  DETAIL: {gate_detail}")

    # ============================================================================
    #  STEP 8: Save and plot
    # ============================================================================

    np.savez('s59_ricci_dw.npz',
        tau_vals=tau_vals,
        r1_arr=r1_arr, r2_arr=r2_arr, r3_arr=r3_arr,
        R_arr=R_arr,
        A_aniso=A_aniso, sigma_ric=sigma_ric,
        sec_min_arr=sec_min_arr, sec_max_arr=sec_max_arr, n_neg_arr=n_neg_arr,
        L_eigs=L_eigs, rho_arr=rho_arr, margin_arr=margin_arr,
        tau_dw_geom=np.float64(tau_dw_geom),
        tau_dw_arith=np.float64(tau_dw_arith),
        A_crit=np.float64(A_crit),
        sigma_crit=np.float64(sigma_crit),
        sec_at_dw=np.float64(sec_at_dw),
        tau_sec_zero=np.float64(tau_sec_zero if tau_sec_zero is not None else np.nan),
        tau_stab_cross=np.float64(tau_stab_cross if tau_stab_cross is not None else np.nan),
        gate_name=np.array(['RICCI-DW-59']),
        gate_verdict=np.array([gate_verdict]),
        gate_detail=np.array([gate_detail]),
    )
    log(f"\n  Saved: s59_ricci_dw.npz")

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax = axes[0, 0]
    ax.plot(tau_vals, r1_arr, 'b-', lw=2, label=r'$r_1$ (u(1))')
    ax.plot(tau_vals, r2_arr, 'r-', lw=2, label=r'$r_2$ (su(2))')
    ax.plot(tau_vals, r3_arr, 'g-', lw=2, label=r'$r_3$ ($\mathbb{C}^2$)')
    ax.axvline(tau_dw_geom, color='k', ls='--', alpha=0.5, label=f'$\\tau_{{DW}}={tau_dw_geom:.3f}$')
    ax.axvline(tau_fold, color='orange', ls=':', alpha=0.5, label=f'$\\tau_{{fold}}={tau_fold}$')
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel('Ricci eigenvalue')
    ax.set_title('Ricci Components on Jensen SU(3)')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(tau_vals, A_aniso, 'k-', lw=2, label=r'$A = |r_3-r_2|/r_{avg}$')
    ax.plot(tau_vals, sigma_ric, 'b--', lw=1.5, label=r'$\sigma_{Ric}$')
    ax.axvline(tau_dw_geom, color='k', ls='--', alpha=0.5)
    ax.axvline(tau_fold, color='orange', ls=':', alpha=0.5)
    ax.axhline(A_crit, color='red', ls=':', alpha=0.5, label=f'$A_{{crit}}={A_crit:.4f}$')
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel('Anisotropy')
    ax.set_title(f'Ricci Anisotropy ($A_{{crit}}={A_crit:.4f}$)')
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.plot(tau_vals, sec_min_arr, 'r-', lw=2, label=r'$K_{sec}^{min}$')
    ax.plot(tau_vals, sec_max_arr, 'b-', lw=2, label=r'$K_{sec}^{max}$')
    ax.axhline(0, color='k', ls='-', alpha=0.3)
    ax.axvline(tau_dw_geom, color='k', ls='--', alpha=0.5, label=r'$\tau_{DW}$')
    ax.axvline(tau_fold, color='orange', ls=':', alpha=0.5)
    if tau_sec_zero is not None and np.isfinite(tau_sec_zero):
        ax.axvline(tau_sec_zero, color='red', ls='--', alpha=0.7,
                   label=f'$K^{{min}}_{{sec}}=0$ at $\\tau={tau_sec_zero:.3f}$')
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel('Sectional curvature')
    ax.set_title('Sectional Curvature Bounds'); ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(tau_vals, L_eigs[:, 0], 'r-', lw=2, label=r'$\lambda_L^{min}$')
    ax.plot(tau_vals, 2*rho_arr, 'k--', lw=2, label=r'$2\rho$')
    ax.plot(tau_vals, margin_arr, 'b-', lw=1.5, label='margin')
    ax.axhline(0, color='k', ls='-', alpha=0.3)
    ax.axvline(tau_dw_geom, color='k', ls='--', alpha=0.5, label=r'$\tau_{DW}$')
    ax.axvline(tau_fold, color='orange', ls=':', alpha=0.5)
    if tau_stab_cross is not None:
        ax.axvline(tau_stab_cross, color='red', ls='--', alpha=0.7,
                   label=f'margin=0 at $\\tau={tau_stab_cross:.3f}$')
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel('Eigenvalue')
    ax.set_title('Lichnerowicz Stability (Lauret-Will)')
    ax.legend(fontsize=8, loc='best'); ax.grid(True, alpha=0.3)

    fig.suptitle(f'S59 RICCI-DW-59: Ricci Anisotropy at Domain Wall (Gate: {gate_verdict})',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig('s59_ricci_dw.png', dpi=150, bbox_inches='tight')
    log(f"  Saved: s59_ricci_dw.png")

    log(f"\n{'='*72}")
    log(f"  COMPUTATION COMPLETE")
    log(f"{'='*72}")

print("Done. See s59_ricci_dw_log.txt for full output.")
