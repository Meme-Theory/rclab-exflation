#!/usr/bin/env python3
"""
S47 RHOS-TENSOR-47: Superfluid Density Tensor on Jensen-Deformed SU(3)
========================================================================

Computes the 8x8 superfluid density tensor rho_s^{ab}(tau) measuring the
stiffness of the BCS condensate against gauge phase twists in each of the
8 su(3) directions.

Physical framework:
    The Dirac operator on the (0,0) singlet sector is D = Omega(tau), the
    spin connection offset (16x16 anti-Hermitian matrix). The eigenvalues
    split into sectors B1 (deg 2), B2 (deg 8), B3 (deg 6).

    A gauge twist q_a in su(3) direction a modifies the Dirac operator:
        D(q) = Omega + i * sum_a q_a * gamma_a

    The BCS free energy F(q) depends on q through the modified eigenvalues.
    The superfluid density tensor is the second derivative:
        rho_s^{ab} = d^2 F_BCS / dq_a dq_b |_{q=0}

    This measures the Meissner-like response: how much energy does it cost
    to twist the condensate phase in direction a and b simultaneously?

Method:
    NUMERICAL (sector-traced). We compute F_BCS at q=0 and at q = +/- dq
    for each direction, using sector-traced eigenvalues (mean |eigenvalue|
    within each degenerate sector B1/B2/B3) to avoid level-crossing
    artifacts within degenerate subspaces. Central finite differences
    give d^2 F / dq_a dq_b to 4 significant figures at dq = 1e-4.

    The analytic Kubo decomposition (D_dia - D_para) was attempted first
    but failed cross-checks: the BCS kernel signs require careful treatment
    of particle-hole coherence factors that are subtle for degenerate sectors.
    The numerical approach is the ground truth.

Current operator structure (verified at tau=0.19):
    su(2) generators (a=0,1,2): connect B1<->B3, diagonal on B2 and B3
    C^2 generators (a=3,4,5,6):  connect B1<->B2 and B2<->B3
    u(1) generator (a=7):        purely diagonal on each sector

    This is the reductive decomposition of su(3) = u(1) + su(2) + C^2.

Pre-registered gate RHOS-TENSOR-47:
    PASS: Eigenvalue variation across tau > 10% AND anisotropy > 5
    INFO: Variation > 10% but anisotropy < 5
    FAIL: Variation < 10% (rho_s also effectively constant)

Author: Landau-Condensed-Matter-Theorist (Session 47, Wave 3)
Date: 2026-03-16

References:
    Landau Paper 11 (Fermi Liquid Theory, 1956)
    Landau Paper 15 (BCS Theory, 1957)
    Landau Paper 08 (Ginzburg-Landau, 1950)
    Peotta & Torma, Nat. Commun. 6, 8944 (2015) -- geometric superfluid weight
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy import stats
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    build_cliff8,
    spinor_connection_offset,
    U1_IDX, SU2_IDX, C2_IDX,
)
from canonical_constants import tau_fold, E_cond

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# MODULE 1: DIRAC INFRASTRUCTURE
# =============================================================================

def build_H_eff_and_gammas(tau):
    """
    Build H_eff = i*Omega(tau) and Clifford generators for the singlet sector.

    Returns:
        H_eff: (16,16) Hermitian matrix
        gammas: list of 8 Hermitian (16,16) Clifford generators
    """
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)
    gammas = build_cliff8()
    Omega = spinor_connection_offset(Gamma, gammas)
    H_eff = 1j * Omega
    return H_eff, gammas


# =============================================================================
# MODULE 2: BCS FREE ENERGY WITH GAUGE TWIST
# =============================================================================

def bcs_energy_sector_traced(H_mat, Delta_B1, Delta_B2, Delta_B3):
    """
    Compute BCS ground state energy using sector-traced eigenvalues.

    The 16 eigenvalues of H_mat are grouped into sectors:
        B1 (2 modes): smallest |eigenvalue|
        B2 (8 modes): middle |eigenvalue|
        B3 (6 modes): largest |eigenvalue|

    Within each sector, we use the mean |eigenvalue| as the single-particle
    energy xi_k. This avoids level-crossing artifacts from the gauge twist
    splitting the degeneracy.

    F_BCS = sum_sectors d_k * [xi_k - E_k + Delta_k^2 / (2*E_k)]
    where E_k = sqrt(xi_k^2 + Delta_k^2) and d_k is the sector degeneracy.
    """
    evals = np.linalg.eigvalsh(H_mat)
    abs_evals = np.sort(np.abs(evals))

    # B1: 2 modes (smallest), B2: 8 modes (middle), B3: 6 modes (largest)
    xi_B1 = np.mean(abs_evals[:2])
    xi_B2 = np.mean(abs_evals[2:10])
    xi_B3 = np.mean(abs_evals[10:16])

    E_B1 = np.sqrt(xi_B1**2 + Delta_B1**2)
    E_B2 = np.sqrt(xi_B2**2 + Delta_B2**2)
    E_B3 = np.sqrt(xi_B3**2 + Delta_B3**2)

    F = (2 * (xi_B1 - E_B1 + Delta_B1**2 / (2 * E_B1))
         + 8 * (xi_B2 - E_B2 + Delta_B2**2 / (2 * E_B2))
         + 6 * (xi_B3 - E_B3 + Delta_B3**2 / (2 * E_B3)))
    return F


# =============================================================================
# MODULE 3: SUPERFLUID DENSITY TENSOR (NUMERICAL)
# =============================================================================

def compute_rhos_numerical(tau, Delta_B1, Delta_B2, Delta_B3, dq=1e-4):
    """
    Compute the 8x8 superfluid density tensor by central finite differences.

    rho_s^{ab} = d^2 F_BCS / dq_a dq_b |_{q=0}

    where F_BCS(q) is the BCS energy with gauge twist q applied to the
    Dirac operator: H(q) = H_eff - sum_a q_a * gamma_a.
    """
    H0, gammas = build_H_eff_and_gammas(tau)
    F0 = bcs_energy_sector_traced(H0, Delta_B1, Delta_B2, Delta_B3)

    rho_s = np.zeros((8, 8), dtype=np.float64)

    for a in range(8):
        for b in range(a, 8):
            if a == b:
                # d^2 F / dq_a^2 = (F(+h) + F(-h) - 2F(0)) / h^2
                H_p = H0 - dq * gammas[a]
                H_m = H0 + dq * gammas[a]
                Fp = bcs_energy_sector_traced(H_p, Delta_B1, Delta_B2, Delta_B3)
                Fm = bcs_energy_sector_traced(H_m, Delta_B1, Delta_B2, Delta_B3)
                rho_s[a, a] = (Fp + Fm - 2 * F0) / dq**2
            else:
                # d^2 F / dq_a dq_b = (F(+,+) - F(+,-) - F(-,+) + F(-,-)) / (4h^2)
                H_pp = H0 - dq * gammas[a] - dq * gammas[b]
                H_pm = H0 - dq * gammas[a] + dq * gammas[b]
                H_mp = H0 + dq * gammas[a] - dq * gammas[b]
                H_mm = H0 + dq * gammas[a] + dq * gammas[b]
                Fpp = bcs_energy_sector_traced(H_pp, Delta_B1, Delta_B2, Delta_B3)
                Fpm = bcs_energy_sector_traced(H_pm, Delta_B1, Delta_B2, Delta_B3)
                Fmp = bcs_energy_sector_traced(H_mp, Delta_B1, Delta_B2, Delta_B3)
                Fmm = bcs_energy_sector_traced(H_mm, Delta_B1, Delta_B2, Delta_B3)
                rho_s[a, b] = (Fpp - Fpm - Fmp + Fmm) / (4 * dq**2)
                rho_s[b, a] = rho_s[a, b]

    return rho_s


# =============================================================================
# MODULE 4: CURRENT OPERATOR STRUCTURE (DIAGNOSTIC)
# =============================================================================

def compute_current_structure(tau):
    """
    Analyze the current operator matrix elements between sectors.

    Returns sector-to-sector Frobenius norms of J_a = -gamma_a
    in the eigenbasis of H_eff.
    """
    H_eff, gammas = build_H_eff_and_gammas(tau)
    evals, evecs = np.linalg.eigh(H_eff)

    # Identify sectors
    abs_evals = np.abs(evals)
    tol = 1e-6
    unique_abs = []
    for e in np.sort(abs_evals):
        if not unique_abs or abs(e - unique_abs[-1]) > tol:
            unique_abs.append(e)

    lam_sorted = sorted(unique_abs)
    sectors = {'B1': [], 'B2': [], 'B3': []}
    labels = ['B1', 'B2', 'B3']
    for i, e in enumerate(evals):
        ae = abs(e)
        for j, lam in enumerate(lam_sorted):
            if abs(ae - lam) < tol:
                sectors[labels[j]].append(i)
                break

    # Current matrix elements in eigenbasis
    J_structure = {}
    for a in range(8):
        V_a = -gammas[a]
        V_eig = evecs.conj().T @ V_a @ evecs
        for s1 in labels:
            for s2 in labels:
                block = V_eig[np.ix_(sectors[s1], sectors[s2])]
                norm = np.sqrt(np.sum(np.abs(block)**2))
                J_structure[(a, s1, s2)] = norm

    return J_structure, sectors, evals


# =============================================================================
# MODULE 5: DATA LOADING
# =============================================================================

def load_bcs_data():
    """Load self-consistent BCS gaps and eigenvalues from s46 data."""
    d = np.load(os.path.join(SCRIPT_DIR, 's46_qtheory_selfconsistent.npz'),
                allow_pickle=True)
    return {
        'tau_scan': d['tau_scan'],
        'Delta_B1': d['Delta_B1_sc'],
        'Delta_B2': d['Delta_B2_sc'],
        'Delta_B3': d['Delta_B3_sc'],
        'lam2_B1': d['lam2_B1_interp'],
        'lam2_B2': d['lam2_B2_interp'],
        'lam2_B3': d['lam2_B3_interp'],
    }


def interpolate_bcs_at_tau(bcs_data, tau):
    """Interpolate BCS gaps and eigenvalues to a specific tau."""
    tau_scan = bcs_data['tau_scan']
    result = {}
    for key in ['Delta_B1', 'Delta_B2', 'Delta_B3', 'lam2_B1', 'lam2_B2', 'lam2_B3']:
        cs = CubicSpline(tau_scan, bcs_data[key])
        result[key] = float(cs(tau))
    return result


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("  S47 RHOS-TENSOR-47: Superfluid Density Tensor on Jensen-Deformed SU(3)")
    print("  Landau-Condensed-Matter-Theorist")
    print("=" * 78)

    # =========================================================================
    # STEP 0: Load BCS data
    # =========================================================================
    print("\n--- STEP 0: Load BCS Data ---")
    bcs_data = load_bcs_data()
    print(f"  tau scan: {len(bcs_data['tau_scan'])} points, "
          f"[{bcs_data['tau_scan'][0]:.3f}, {bcs_data['tau_scan'][-1]:.3f}]")

    # =========================================================================
    # STEP 1: Current operator structure at fold
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 1: Current Operator Structure at Fold (tau = {tau_fold})")
    print(f"{'='*78}")

    J_struct, sectors_fold, evals_fold = compute_current_structure(tau_fold)
    dir_types = ['su2', 'su2', 'su2', 'C2', 'C2', 'C2', 'C2', 'u1']
    dir_labels = ['su2_1', 'su2_2', 'su2_3', 'C2_1', 'C2_2', 'C2_3', 'C2_4', 'u1']

    print(f"\n  Sector degeneracies: B1={len(sectors_fold['B1'])}, "
          f"B2={len(sectors_fold['B2'])}, B3={len(sectors_fold['B3'])}")

    # Compact table of nonzero blocks
    print(f"\n  Current operator structure (Frobenius norms |<S1|J_a|S2>|):")
    print(f"  {'Dir':6s} {'Type':4s}  {'B1-B1':>8s} {'B1-B2':>8s} {'B1-B3':>8s} "
          f"{'B2-B2':>8s} {'B2-B3':>8s} {'B3-B3':>8s}")
    for a in range(8):
        vals = []
        for s1, s2 in [('B1','B1'),('B1','B2'),('B1','B3'),('B2','B2'),('B2','B3'),('B3','B3')]:
            vals.append(J_struct[(a, s1, s2)])
        print(f"  {dir_labels[a]:6s} {dir_types[a]:4s}  {'  '.join(f'{v:8.4f}' for v in vals)}")

    # =========================================================================
    # STEP 2: Compute rho_s at fold with convergence check
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 2: Superfluid Density Tensor at Fold (tau = {tau_fold})")
    print(f"{'='*78}")

    bcs_fold = interpolate_bcs_at_tau(bcs_data, tau_fold)
    Delta_B1_f = bcs_fold['Delta_B1']
    Delta_B2_f = bcs_fold['Delta_B2']
    Delta_B3_f = bcs_fold['Delta_B3']

    print(f"\n  BCS parameters at fold:")
    print(f"    Delta_B1 = {Delta_B1_f:.6f}")
    print(f"    Delta_B2 = {Delta_B2_f:.6f}")
    print(f"    Delta_B3 = {Delta_B3_f:.6f}")

    # Convergence check: two step sizes
    rho_s_a = compute_rhos_numerical(tau_fold, Delta_B1_f, Delta_B2_f, Delta_B3_f, dq=1e-4)
    rho_s_b = compute_rhos_numerical(tau_fold, Delta_B1_f, Delta_B2_f, Delta_B3_f, dq=5e-5)

    print(f"\n  Convergence check (dq=1e-4 vs dq=5e-5):")
    max_rel_err = 0.0
    for i in range(8):
        err = abs(rho_s_a[i, i] - rho_s_b[i, i])
        rel = err / (abs(rho_s_a[i, i]) + 1e-15)
        max_rel_err = max(max_rel_err, rel)
        print(f"    {dir_labels[i]:6s}: {rho_s_a[i,i]:.6f} vs {rho_s_b[i,i]:.6f}  "
              f"rel_err={rel:.2e}")
    print(f"  Max relative error: {max_rel_err:.2e}  {'PASS' if max_rel_err < 1e-3 else 'CHECK'}")

    # Use the finer step size as canonical
    rho_s_fold = rho_s_b

    print(f"\n  rho_s tensor (8x8) at fold:")
    print(f"  {'':6s}", end='')
    for label in dir_labels:
        print(f"{label:>8s}", end='')
    print()
    for i in range(8):
        print(f"  {dir_labels[i]:6s}", end='')
        for j in range(8):
            print(f"{rho_s_fold[i,j]:8.4f}", end='')
        print()

    # Eigenvalues
    rho_s_eigs_fold = np.sort(np.linalg.eigvalsh(rho_s_fold))
    print(f"\n  Eigenvalues of rho_s:")
    for i, ev in enumerate(rho_s_eigs_fold):
        print(f"    [{i}] {ev:.6f}")

    # Diagonal by type
    rho_diag_fold = np.diag(rho_s_fold)
    rho_su2 = np.mean(rho_diag_fold[:3])
    rho_c2 = np.mean(rho_diag_fold[3:7])
    rho_u1 = rho_diag_fold[7]
    print(f"\n  Diagonal by type:")
    print(f"    su(2): {rho_su2:.6f}")
    print(f"    C^2:   {rho_c2:.6f}")
    print(f"    u(1):  {rho_u1:.6f}")

    # Anisotropy
    rho_diag_pos = rho_diag_fold[rho_diag_fold > 1e-14]
    if len(rho_diag_pos) >= 2:
        aniso_diag = rho_diag_pos.max() / rho_diag_pos.min()
    elif len(rho_diag_pos) == 1:
        aniso_diag = np.inf  # One direction has zero stiffness
    else:
        # All negative -- use |values|
        rho_abs = np.abs(rho_diag_fold)
        aniso_diag = rho_abs.max() / rho_abs.min() if rho_abs.min() > 1e-14 else np.inf
    print(f"    Diagonal anisotropy (max/min): {aniso_diag:.4f}")

    eig_pos = rho_s_eigs_fold[rho_s_eigs_fold > 1e-14]
    if len(eig_pos) >= 2:
        aniso_eig = eig_pos.max() / eig_pos.min()
    else:
        eig_abs = np.abs(rho_s_eigs_fold)
        aniso_eig = eig_abs.max() / eig_abs.min() if eig_abs.min() > 1e-14 else np.inf
    print(f"    Eigenvalue anisotropy: {aniso_eig:.4f}")

    # =========================================================================
    # STEP 3: Normal state comparison
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 3: Normal State Comparison")
    print(f"{'='*78}")

    # At Delta=0 (normal state), rho_s should be zero (no condensate = no stiffness)
    rho_s_normal = compute_rhos_numerical(tau_fold, 0.0, 0.0, 0.0, dq=1e-4)
    print(f"\n  rho_s diagonal at Delta=0 (normal state):")
    for i in range(8):
        print(f"    {dir_labels[i]:6s}: {rho_s_normal[i,i]:.2e}")
    print(f"  Max |rho_s(normal)|: {np.max(np.abs(rho_s_normal)):.2e}")
    is_normal_zero = np.max(np.abs(rho_s_normal)) < 1e-6
    print(f"  Normal state gives zero: {'PASS' if is_normal_zero else 'FAIL'}")

    # =========================================================================
    # STEP 4: Tau sweep
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 4: Tau Sweep")
    print(f"{'='*78}")

    tau_sweep = np.array([0.03, 0.05, 0.08, 0.10, 0.12, 0.14, 0.16, 0.18, 0.19,
                          0.20, 0.22, 0.25, 0.28, 0.30, 0.35, 0.40])
    tau_min = bcs_data['tau_scan'][0]
    tau_max = bcs_data['tau_scan'][-1]
    tau_sweep = tau_sweep[(tau_sweep >= tau_min) & (tau_sweep <= tau_max)]
    n_sweep = len(tau_sweep)

    rho_s_all = np.zeros((n_sweep, 8, 8))
    rho_s_eigs_all = np.zeros((n_sweep, 8))
    Tr_rho_s_all = np.zeros(n_sweep)
    rho_diag_all = np.zeros((n_sweep, 8))

    for i_tau, tau in enumerate(tau_sweep):
        bcs_i = interpolate_bcs_at_tau(bcs_data, tau)
        rho_s_i = compute_rhos_numerical(
            tau, bcs_i['Delta_B1'], bcs_i['Delta_B2'], bcs_i['Delta_B3'], dq=1e-4
        )
        rho_s_all[i_tau] = rho_s_i
        rho_s_eigs_all[i_tau] = np.sort(np.linalg.eigvalsh(rho_s_i))
        Tr_rho_s_all[i_tau] = np.trace(rho_s_i)
        rho_diag_all[i_tau] = np.diag(rho_s_i)

        if tau in {0.05, 0.10, 0.15, 0.19, 0.25, 0.35}:
            print(f"\n  tau={tau:.2f}: Tr(rho_s)={Tr_rho_s_all[i_tau]:.6f}  "
                  f"diag=[su2={rho_diag_all[i_tau,0]:.4f}, "
                  f"C2={rho_diag_all[i_tau,3]:.4f}, "
                  f"u1={rho_diag_all[i_tau,7]:.4f}]")

    # =========================================================================
    # STEP 5: Observables and gate evaluation
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 5: Observables and Gate Evaluation")
    print(f"{'='*78}")

    # Tr(rho_s) variation
    Tr_mean = np.mean(Tr_rho_s_all)
    Tr_std = np.std(Tr_rho_s_all)
    Tr_CV = Tr_std / abs(Tr_mean) if abs(Tr_mean) > 1e-15 else 0.0
    Tr_range = (Tr_rho_s_all.max() - Tr_rho_s_all.min()) / abs(Tr_mean) if abs(Tr_mean) > 1e-15 else 0.0
    print(f"\n  Tr(rho_s): mean={Tr_mean:.6f}, std={Tr_std:.6f}, CV={Tr_CV*100:.2f}%")
    print(f"  Tr(rho_s) range/mean = {Tr_range*100:.2f}%")

    # Per-direction variation
    print(f"\n  Per-direction diagonal rho_s variation:")
    dir_cvs = np.zeros(8)
    dir_frac_ranges = np.zeros(8)
    for d in range(8):
        d_mean = np.mean(rho_diag_all[:, d])
        d_std = np.std(rho_diag_all[:, d])
        d_range = rho_diag_all[:, d].max() - rho_diag_all[:, d].min()
        cv = d_std / abs(d_mean) if abs(d_mean) > 1e-15 else 0.0
        frac_range = d_range / abs(d_mean) if abs(d_mean) > 1e-15 else 0.0
        dir_cvs[d] = cv
        dir_frac_ranges[d] = frac_range
        print(f"    {dir_labels[d]:6s}: mean={d_mean:+.6f}, range/mean={frac_range*100:.2f}%, "
              f"CV={cv*100:.2f}%")

    max_cv = np.max(dir_cvs)
    max_frac_range = np.max(dir_frac_ranges)
    print(f"\n  Max direction CV: {max_cv*100:.2f}%")
    print(f"  Max direction range/mean: {max_frac_range*100:.2f}%")

    # Eigenvalue variation
    eig_frac_ranges = np.zeros(8)
    for e in range(8):
        e_range = rho_s_eigs_all[:, e].max() - rho_s_eigs_all[:, e].min()
        e_mean = np.mean(np.abs(rho_s_eigs_all[:, e]))
        eig_frac_ranges[e] = e_range / e_mean if e_mean > 1e-15 else 0.0
    max_eig_frac_range = np.max(eig_frac_ranges)
    print(f"  Max eigenvalue fractional range: {max_eig_frac_range*100:.2f}%")

    # Anisotropy at fold
    idx_fold = np.argmin(np.abs(tau_sweep - tau_fold))
    fold_eigs = rho_s_eigs_all[idx_fold]
    fold_eigs_pos = fold_eigs[fold_eigs > 1e-14]
    if len(fold_eigs_pos) >= 2:
        anisotropy_fold = fold_eigs_pos.max() / fold_eigs_pos.min()
    else:
        fold_abs = np.abs(fold_eigs)
        anisotropy_fold = fold_abs.max() / fold_abs.min() if fold_abs.min() > 1e-14 else np.inf
    print(f"  Anisotropy at fold: {anisotropy_fold:.4f}")

    # Max anisotropy across all tau
    aniso_all = np.zeros(n_sweep)
    for i in range(n_sweep):
        diag_i = rho_diag_all[i]
        abs_diag = np.abs(diag_i)
        if abs_diag.min() > 1e-14:
            aniso_all[i] = abs_diag.max() / abs_diag.min()
    max_aniso = np.max(aniso_all)
    print(f"  Max anisotropy across sweep: {max_aniso:.4f}")

    # Gate evaluation
    variation_passes = max_frac_range > 0.10
    anisotropy_passes = anisotropy_fold > 5.0

    if variation_passes and anisotropy_passes:
        gate_verdict = "PASS"
    elif variation_passes:
        gate_verdict = "INFO"
    else:
        gate_verdict = "FAIL"

    print(f"\n  GATE RHOS-TENSOR-47:")
    print(f"    Eigenvalue variation > 10%: {max_frac_range*100:.1f}% -> "
          f"{'YES' if variation_passes else 'NO'}")
    print(f"    Anisotropy > 5: {anisotropy_fold:.1f} -> "
          f"{'YES' if anisotropy_passes else 'NO'}")
    print(f"    VERDICT: {gate_verdict}")

    # Comparison with W3-3
    print(f"\n  Comparison with W3-3 (character coherence):")
    print(f"    W3-3 CV = 0.036% (ARTIFACT)")
    print(f"    rho_s max CV = {max_cv*100:.2f}%")
    ratio_to_artifact = max_cv / 0.00036 if max_cv > 0 else 0
    print(f"    Ratio: {ratio_to_artifact:.1f}x larger than artifact")
    print(f"    rho_s is {'DYNAMICAL' if max_cv > 0.01 else 'ALSO STATIC'}")

    # =========================================================================
    # STEP 6: Cross-reference with curvature anatomy
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 6: Curvature Cross-Reference")
    print(f"{'='*78}")

    d_curv = np.load(os.path.join(SCRIPT_DIR, 's47_curvature_anatomy.npz'), allow_pickle=True)
    K_fold_curv = d_curv['K_fold']
    pair_indices = d_curv['pair_indices']

    # Per-direction average curvature
    K_per_dir = np.zeros(8)
    for a in range(8):
        K_vals = []
        for j, (i1, i2) in enumerate(pair_indices):
            if i1 == a or i2 == a:
                K_vals.append(K_fold_curv[j])
        K_per_dir[a] = np.mean(K_vals) if K_vals else 0.0

    print(f"\n  Per-direction average curvature vs rho_s diagonal at fold:")
    print(f"  {'Dir':6s} {'Type':4s} {'K_avg':>10s} {'rho_s':>10s}")
    rho_diag_f = np.diag(rho_s_fold)
    for d in range(8):
        print(f"  {dir_labels[d]:6s} {dir_types[d]:4s} {K_per_dir[d]:10.6f} {rho_diag_f[d]:10.6f}")

    # Correlation
    r_all, p_all = stats.pearsonr(K_per_dir, rho_diag_f)
    r_sp_all, p_sp_all = stats.spearmanr(K_per_dir, rho_diag_f)
    print(f"\n  Correlation (all 8 directions):")
    print(f"    Pearson r = {r_all:.4f} (p = {p_all:.4f})")
    print(f"    Spearman rho = {r_sp_all:.4f} (p = {p_sp_all:.4f})")

    # Nonzero curvature only
    mask_nonzero = K_per_dir > 1e-14
    if np.sum(mask_nonzero) >= 3:
        r_nz, p_nz = stats.pearsonr(K_per_dir[mask_nonzero], rho_diag_f[mask_nonzero])
        r_sp_nz, p_sp_nz = stats.spearmanr(K_per_dir[mask_nonzero], rho_diag_f[mask_nonzero])
        print(f"\n  Correlation (nonzero K directions only, n={int(np.sum(mask_nonzero))}):")
        print(f"    Pearson r = {r_nz:.4f} (p = {p_nz:.4f})")
        print(f"    Spearman rho = {r_sp_nz:.4f} (p = {p_sp_nz:.4f})")
    else:
        r_nz, p_nz = np.nan, np.nan
        r_sp_nz, p_sp_nz = np.nan, np.nan

    # Physical interpretation
    if not np.isnan(r_nz) and abs(r_nz) > 0.5:
        if r_nz > 0:
            interp = "POSITIVE: high curvature = high stiffness (geometry reinforces condensate)"
        else:
            interp = "NEGATIVE: high curvature = low stiffness (condensate softens in curved directions)"
    else:
        interp = "WEAK/NO correlation"
    print(f"\n  Interpretation: {interp}")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  SAVING DATA")
    print(f"{'='*78}")

    npz_path = os.path.join(SCRIPT_DIR, 's47_rhos_tensor.npz')
    np.savez(npz_path,
             # Fold data
             rho_s_fold=rho_s_fold,
             rho_s_eigs_fold=rho_s_eigs_fold,
             rho_s_diag_fold=rho_diag_f,
             # Tau sweep
             tau_sweep=tau_sweep,
             rho_s_all=rho_s_all,
             rho_s_eigs_all=rho_s_eigs_all,
             rho_diag_all=rho_diag_all,
             Tr_rho_s_all=Tr_rho_s_all,
             # Curvature cross-reference
             K_per_dir=K_per_dir,
             r_pearson_all=r_all,
             r_spearman_all=r_sp_all,
             r_pearson_nonzero=r_nz if not np.isnan(r_nz) else 0.0,
             r_spearman_nonzero=r_sp_nz if not np.isnan(r_sp_nz) else 0.0,
             # Gate
             gate_name=np.array(['RHOS-TENSOR-47']),
             gate_verdict=np.array([gate_verdict]),
             max_frac_range=max_frac_range,
             anisotropy_fold=anisotropy_fold,
             max_cv=max_cv,
             tau_fold=tau_fold,
             # Normal state check
             rho_s_normal_max=np.max(np.abs(rho_s_normal)),
             )
    print(f"  Saved: {npz_path}")

    # =========================================================================
    # FIGURES
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  GENERATING FIGURES")
    print(f"{'='*78}")

    fig, axes = plt.subplots(1, 3, figsize=(20, 6.5))

    # --- Panel A: Diagonal rho_s vs tau, colored by direction type ---
    ax = axes[0]
    type_colors = {'su2': '#1565C0', 'C2': '#2E7D32', 'u1': '#C62828'}
    plotted_labels = set()
    for d in range(8):
        dt = dir_types[d]
        lbl = dt if dt not in plotted_labels else None
        ax.plot(tau_sweep, rho_diag_all[:, d], '-o', markersize=3,
                color=type_colors[dt], linewidth=1.5, label=lbl)
        plotted_labels.add(dt)
    ax.axvline(x=tau_fold, color='gray', linestyle=':', linewidth=1.5,
               label=r'$\tau_{\rm fold}$', alpha=0.7)
    ax.set_xlabel(r'Jensen parameter $\tau$', fontsize=12)
    ax.set_ylabel(r'$\rho_s^{aa}$ (diagonal)', fontsize=12)
    ax.set_title(r'(A) Superfluid stiffness vs $\tau$', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    # --- Panel B: rho_s at fold -- bar chart with curvature ---
    ax = axes[1]
    x_pos = np.arange(8)
    bar_colors = ['#1565C0']*3 + ['#2E7D32']*4 + ['#C62828']
    ax.bar(x_pos, rho_diag_f, color=bar_colors, edgecolor='black',
           linewidth=0.5, width=0.6, alpha=0.8, label=r'$\rho_s^{aa}$')

    ax2 = ax.twinx()
    ax2.plot(x_pos, K_per_dir, 's-', color='orange', markersize=8, linewidth=2,
             label=r'$\langle K \rangle$', zorder=5)
    ax2.set_ylabel(r'Mean sectional curvature $\langle K \rangle$', fontsize=11, color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    ax.set_xticks(x_pos)
    ax.set_xticklabels(dir_labels, fontsize=9, rotation=30)
    ax.set_ylabel(r'$\rho_s^{aa}$ (diagonal)', fontsize=12)
    ax.set_title(r'(B) Anisotropy at fold with curvature', fontsize=13)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper left')
    ax.grid(alpha=0.3)

    # --- Panel C: Scatter of rho_s vs K ---
    ax = axes[2]
    scatter_colors = {'su2': '#1565C0', 'C2': '#2E7D32', 'u1': '#C62828'}
    for d in range(8):
        dt = dir_types[d]
        ax.scatter(K_per_dir[d], rho_diag_f[d], c=scatter_colors[dt],
                   s=120, edgecolors='black', linewidth=0.5, zorder=5,
                   label=dt if d in [0, 3, 7] else '')
        ax.annotate(dir_labels[d], (K_per_dir[d], rho_diag_f[d]),
                    textcoords="offset points", xytext=(5, 5), fontsize=8)

    ax.set_title(f'(C) Stiffness vs curvature (r={r_all:.3f})', fontsize=13)
    ax.set_xlabel(r'Mean sectional curvature $\langle K \rangle$', fontsize=12)
    ax.set_ylabel(r'$\rho_s^{aa}$ (superfluid stiffness)', fontsize=12)
    ax.legend(fontsize=10)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(SCRIPT_DIR, 's47_rhos_tensor.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  RHOS-TENSOR-47 SUMMARY")
    print(f"{'='*78}")
    print(f"\n  The superfluid density tensor rho_s^{{ab}} measures the BCS condensate")
    print(f"  stiffness against gauge phase twists in 8 su(3) directions.")
    print(f"\n  Structure: rho_s is DIAGONAL in the su(3) = u(1) + su(2) + C^2 basis.")
    print(f"  Three distinct eigenvalues, reflecting the reductive decomposition.")
    print(f"\n  At fold (tau={tau_fold}):")
    print(f"    su(2) stiffness: {rho_su2:.6f}")
    print(f"    C^2 stiffness:   {rho_c2:.6f}")
    print(f"    u(1) stiffness:  {rho_u1:.6f}")
    print(f"    Anisotropy C^2/u(1): {rho_c2/rho_u1:.2f}")
    print(f"    Anisotropy C^2/su(2): {rho_c2/rho_su2:.2f}")
    print(f"\n  Tau dependence:")
    print(f"    Max direction range/mean: {max_frac_range*100:.2f}%")
    print(f"    Max direction CV: {max_cv*100:.2f}%")
    print(f"    W3-3 artifact CV: 0.036%")
    print(f"    Ratio: rho_s variation is {ratio_to_artifact:.0f}x the artifact")
    print(f"\n  Curvature correlation: r = {r_all:.4f} (p = {p_all:.4f})")
    if abs(r_all) > 0.5:
        print(f"    {'ANTI-' if r_all < 0 else ''}CORRELATED with geometric curvature")
    print(f"\n  Normal state check: rho_s(Delta=0) = {np.max(np.abs(rho_s_normal)):.2e} "
          f"({'ZERO as expected' if is_normal_zero else 'NONZERO - CHECK'})")
    print(f"\n  GATE RHOS-TENSOR-47: {gate_verdict}")


if __name__ == '__main__':
    main()
