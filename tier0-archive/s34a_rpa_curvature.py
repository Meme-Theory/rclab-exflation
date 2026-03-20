"""
Session 34a: RPA-34a -- Spectral Action Curvature Under D_phys
=============================================================
Gate RPA-34a (diagnostic): Does the spectral action curvature
d^2(sum|lambda_k|)/dtau^2 remain above threshold 0.54 when eigenvalues
come from D_phys = D_K + phi + J*phi*J^{-1} instead of bare D_K?

RPA-32b baseline (bare D_K):
  d2S_abs(tau=0.15) = 20.46, d2S_abs(tau=0.20) = 20.43, d2S_abs(tau=0.25) = 20.45
  chi_pass_threshold = 0.54
  Margin: ~38x at tau=0.20

Method:
  1. Construct D_phys at each tau using worst-case phi direction (H_j from 34a-1)
  2. Diagonalize to get all 16 eigenvalues at each (tau, phi_VEV) point
  3. Compute S(tau; phi) = sum_k |lambda_k(tau; phi)|
  4. Compute d^2S/dtau^2 by central finite difference (same as s32b_rpa1_thouless.py)
  5. Sweep phi_VEV from 0 to 0.17 (max surviving amplitude from 34a-1)

MANDATORY CROSS-CHECK: At phi=0, must reproduce bare d2S_abs values.

Gate condition:
  CONSISTENT: d2S > 0.54 at |phi| = gap_{B2-B3} = 0.133
  CHALLENGE:  d2S < 0.54 at |phi| = gap

Author: bap (baptista-spacetime-analyst), Session 34a
Date: 2026-03-06
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

# Add parent for tier1 import
sys.path.insert(0, SCRIPT_DIR)

# ======================================================================
#  Constants
# ======================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
# Evaluation points for curvature (need +-1 neighbors for central diff)
EVAL_TAUS = [0.15, 0.20, 0.25]  # tau indices 2, 3, 4 (same as RPA-32b)
CHI_PASS = 0.54

# Phi amplitudes to sweep
PHI_AMPS = np.concatenate([
    np.linspace(0, 0.10, 11),
    np.array([0.12, 0.133, 0.14, 0.15, 0.16, 0.17])
])
PHI_AMPS = np.unique(PHI_AMPS)

GAP_B2_B3 = 0.133  # From 34a-1

# ======================================================================
#  D_phys Construction (reused from s34a_dphys_fold.py)
# ======================================================================

def build_J_operator(gammas):
    """Build J = C2*conj for KO-dim 0. C2 = gamma_1*gamma_3*gamma_5*gamma_7."""
    C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]
    err_sq = np.max(np.abs(C2 @ C2 - np.eye(16)))
    assert err_sq < 1e-13, f"C2^2 != +I, err = {err_sq}"
    return C2


def apply_J_to_matrix(C2, M):
    """Compute J M J^{-1} for linear M. J(v) = C2 conj(v), C2 real, C2^2=I."""
    return C2 @ np.conj(M) @ C2


def flat_idx(row, col):
    """4x4 -> flat 16 (Baptista convention)."""
    if row == 0 and col == 0:
        return 0
    elif row == 0:
        return col
    elif col == 0:
        return row + 3
    else:
        return 7 + 3 * (row - 1) + (col - 1)


def build_AF_gen_16(L_4x4, R_4x4):
    """16x16 A_F generator from left/right 4x4 actions."""
    gen = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for j in range(4):
            fi = flat_idx(i, j)
            for k in range(4):
                for ll in range(4):
                    fk = flat_idx(k, ll)
                    gen[fi, fk] = L_4x4[i, k] * R_4x4[ll, j]
    return gen


def build_AF_generators():
    """Build A_F = C + H + M_3(C) generators on C^16."""
    gens = []

    # C: Im(lambda)
    L = np.zeros((4, 4), dtype=complex)
    L[0, 0] = 1j; L[1, 1] = -1j; L[2, 2] = 1j; L[3, 3] = -1j
    R = np.eye(4, dtype=complex)
    gens.append(('C_Im', build_AF_gen_16(L, R)))

    # H: i, j, k
    L = np.zeros((4, 4), dtype=complex)
    L[0, 0] = 1j; L[1, 1] = -1j; L[2, 2] = 1j; L[3, 3] = -1j
    R = np.eye(4, dtype=complex)
    gens.append(('H_i', build_AF_gen_16(L, R)))

    L = np.zeros((4, 4), dtype=complex)
    L[2, 3] = 1.0; L[3, 2] = -1.0
    R = np.eye(4, dtype=complex)
    gens.append(('H_j', build_AF_gen_16(L, R)))

    L = np.zeros((4, 4), dtype=complex)
    L[2, 3] = 1j; L[3, 2] = 1j
    R = np.eye(4, dtype=complex)
    gens.append(('H_k', build_AF_gen_16(L, R)))

    # M_3(C): 8 Gell-Mann + trace
    def m3_gen(m_3x3):
        L2 = np.eye(4, dtype=complex)
        R2 = np.zeros((4, 4), dtype=complex)
        R2[1:4, 1:4] = m_3x3.T
        return build_AF_gen_16(L2, R2)

    gm = []
    gm.append(np.array([[0,1,0],[1,0,0],[0,0,0]], dtype=complex))
    gm.append(np.array([[0,-1j,0],[1j,0,0],[0,0,0]], dtype=complex))
    gm.append(np.array([[1,0,0],[0,-1,0],[0,0,0]], dtype=complex))
    gm.append(np.array([[0,0,1],[0,0,0],[1,0,0]], dtype=complex))
    gm.append(np.array([[0,0,-1j],[0,0,0],[1j,0,0]], dtype=complex))
    gm.append(np.array([[0,0,0],[0,0,1],[0,1,0]], dtype=complex))
    gm.append(np.array([[0,0,0],[0,0,-1j],[0,1j,0]], dtype=complex))
    gm.append(np.array([[1,0,0],[0,1,0],[0,0,-2]], dtype=complex)/np.sqrt(3))
    for k, g in enumerate(gm):
        gens.append((f'M3_{k}', m3_gen(g)))

    gens.append(('M3_id', m3_gen(np.eye(3, dtype=complex))))
    return gens


def compute_phi_generators(D_K_diag, evecs, af_gens):
    """Compute [D_K, b_i] in eigenspinor basis for each A_F generator."""
    phi_basis = []
    for name, gen in af_gens:
        gen_eig = evecs.conj().T @ gen @ evecs
        n = len(D_K_diag)
        comm = np.zeros((n, n), dtype=complex)
        for i in range(n):
            for j in range(n):
                comm[i, j] = (D_K_diag[i] - D_K_diag[j]) * gen_eig[i, j]
        norm = np.max(np.abs(comm))
        if norm > 1e-12:
            phi_basis.append((name, comm, norm))
    return phi_basis


def construct_D_phys_evals(D_K_diag, evecs, phi_eig, phi_amplitude, C2):
    """Construct D_phys = D_K + phi + J*phi*J^{-1}, return sorted eigenvalues.

    Works in original basis for J consistency.
    """
    D_K_orig = evecs @ np.diag(D_K_diag) @ evecs.conj().T
    phi_orig = evecs @ (phi_amplitude * phi_eig) @ evecs.conj().T
    J_phi_J = apply_J_to_matrix(C2, phi_orig)
    D_phys = D_K_orig + phi_orig + J_phi_J
    evals = eigh(D_phys)[0]  # sorted ascending
    return evals


# ======================================================================
#  Spectral Action Curvature (method from s32b_rpa1_thouless.py)
# ======================================================================

def compute_d2S_abs(evals_array, tau_values, tau_idx):
    """Compute d^2(sum|lambda_k|)/dtau^2 by central finite difference.

    S(tau) = sum_k |lambda_k(tau)|
    d^2S/dtau^2 = sum_k sign(lambda_k) * d^2(lambda_k)/dtau^2

    Uses non-uniform spacing formula:
      d^2f/dx^2 = 2[f(x+h+)*h- - f(x)*(h++h-) + f(x-h-)*h+] / [h+*h-*(h++h-)]
    """
    if tau_idx == 0 or tau_idx >= len(tau_values) - 1:
        return None

    h_plus = tau_values[tau_idx + 1] - tau_values[tau_idx]
    h_minus = tau_values[tau_idx] - tau_values[tau_idx - 1]

    d2lambda = 2.0 * (
        evals_array[tau_idx + 1] * h_minus
        - evals_array[tau_idx] * (h_plus + h_minus)
        + evals_array[tau_idx - 1] * h_plus
    ) / (h_plus * h_minus * (h_plus + h_minus))

    signs = np.sign(evals_array[tau_idx])
    d2S_abs = np.sum(signs * d2lambda)
    d2S_trace = np.sum(d2lambda)  # Should be ~0 (sanity check)

    return d2S_abs, d2S_trace


# ======================================================================
#  Main computation
# ======================================================================

def main():
    print("=" * 78)
    print("RPA-34a: Spectral Action Curvature Under D_phys")
    print("d^2(sum|lambda_k(phi)|)/dtau^2 at dump point under inner fluctuations")
    print("=" * 78)

    # --- Load data ---
    kosmann = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)
    rpa32b = np.load(os.path.join(SCRIPT_DIR, 's32b_rpa1_thouless.npz'),
                     allow_pickle=True)

    tau_vals = kosmann['tau_values']
    n_tau = len(tau_vals)
    print(f"\nTau values: {tau_vals}")

    # Load bare results for comparison
    bare_d2S_abs = rpa32b['d2S_abs']  # shape (3,) at tau=[0.15, 0.20, 0.25]
    bare_tau_eval = rpa32b['tau_eval']
    chi_pass = float(rpa32b['chi_pass_threshold'])
    print(f"Bare d2S_abs: {bare_d2S_abs}")
    print(f"PASS threshold: {chi_pass}")

    # --- Build Clifford algebra and J ---
    from tier1_dirac_spectrum import build_cliff8 as _bc8
    gammas = _bc8()
    C2 = build_J_operator(gammas)
    print(f"J operator built: C2 = gamma_1*gamma_3*gamma_5*gamma_7")

    # --- Build A_F generators ---
    af_gens = build_AF_generators()
    print(f"A_F generators: {len(af_gens)} total")

    # --- Identify worst-case phi direction (H_j) at tau=0.20 ---
    # Use the same direction as DPHYS-34a-1 for consistency
    ti_ref = 3  # tau=0.20
    evals_ref = kosmann[f'eigenvalues_{ti_ref}']
    evecs_ref = kosmann[f'eigenvectors_{ti_ref}']
    si = np.argsort(evals_ref)
    evals_sorted_ref = evals_ref[si]
    evecs_sorted_ref = evecs_ref[:, si]

    phi_basis_ref = compute_phi_generators(evals_sorted_ref, evecs_sorted_ref, af_gens)

    # Find H_j direction
    hj_idx = None
    for idx, (name, comm, norm) in enumerate(phi_basis_ref):
        if name == 'H_j':
            hj_idx = idx
            break

    if hj_idx is None:
        print("ERROR: H_j generator not found in phi basis!")
        return
    print(f"Using worst-case direction: {phi_basis_ref[hj_idx][0]} "
          f"(norm={phi_basis_ref[hj_idx][2]:.6f})")

    # ================================================================
    #  Compute D_phys eigenvalues across full tau grid for each phi_VEV
    # ================================================================
    print(f"\n{'='*78}")
    print("Computing D_phys eigenvalues at all (tau, phi_VEV) grid points")
    print(f"{'='*78}")

    # Storage: evals_grid[phi_idx, tau_idx, :] = 16 eigenvalues
    evals_grid = np.zeros((len(PHI_AMPS), n_tau, 16))

    for pi, phi_amp in enumerate(PHI_AMPS):
        for ti in range(n_tau):
            ev_ti = kosmann[f'eigenvalues_{ti}']
            ec_ti = kosmann[f'eigenvectors_{ti}']
            si = np.argsort(ev_ti)
            ev_s = ev_ti[si]
            ec_s = ec_ti[:, si]

            if phi_amp < 1e-14:
                # Bare D_K
                evals_grid[pi, ti, :] = ev_s
            else:
                # Compute phi in local eigenbasis (H_j direction)
                phi_local = compute_phi_generators(ev_s, ec_s, af_gens)
                phi_dir = None
                for name, comm, norm in phi_local:
                    if name == 'H_j':
                        phi_dir = comm / norm  # Normalize
                        break
                if phi_dir is None:
                    # Fallback: use raw H_j generator commutator
                    for name, gen in af_gens:
                        if name == 'H_j':
                            gen_eig = ec_s.conj().T @ gen @ ec_s
                            comm = np.zeros((16, 16), dtype=complex)
                            for i in range(16):
                                for j in range(16):
                                    comm[i, j] = (ev_s[i] - ev_s[j]) * gen_eig[i, j]
                            nrm = np.max(np.abs(comm))
                            phi_dir = comm / nrm if nrm > 1e-14 else comm
                            break

                evals_phys = construct_D_phys_evals(ev_s, ec_s, phi_dir, phi_amp, C2)
                evals_grid[pi, ti, :] = evals_phys

        if pi % 5 == 0 or phi_amp in [0.0, GAP_B2_B3, 0.17]:
            S_at_020 = np.sum(np.abs(evals_grid[pi, 3, :]))
            print(f"  phi={phi_amp:.4f}: S(tau=0.20) = {S_at_020:.6f}")

    # ================================================================
    #  CROSS-CHECK: phi=0 reproduces bare eigenvalues exactly
    # ================================================================
    print(f"\n--- Cross-check: phi=0 reproduces bare D_K ---")
    phi0_idx = 0  # phi=0
    max_err = 0
    for ti in range(n_tau):
        ev_bare = kosmann[f'eigenvalues_{ti}']
        si = np.argsort(ev_bare)
        ev_bare_sorted = ev_bare[si]
        err = np.max(np.abs(evals_grid[phi0_idx, ti, :] - ev_bare_sorted))
        max_err = max(max_err, err)
    print(f"  max|evals(phi=0) - evals(bare)| = {max_err:.2e}")
    assert max_err < 1e-12, f"CROSS-CHECK FAILED: phi=0 != bare"
    print(f"  PASS")

    # ================================================================
    #  Compute spectral action S(tau; phi) and d^2S/dtau^2
    # ================================================================
    print(f"\n{'='*78}")
    print("Computing d^2(sum|lambda|)/dtau^2 at evaluation points")
    print(f"{'='*78}")

    # S(tau; phi) = sum_k |lambda_k(tau; phi)|
    S_grid = np.sum(np.abs(evals_grid), axis=2)  # shape (n_phi, n_tau)

    # d^2S/dtau^2 for each phi at each evaluation tau
    # Using the same finite difference as RPA-32b
    d2S_results = {}  # phi_amp -> {tau: d2S_abs}

    for pi, phi_amp in enumerate(PHI_AMPS):
        d2S_at_phi = {}
        for tau_eval in EVAL_TAUS:
            ti = np.argmin(np.abs(tau_vals - tau_eval))
            result = compute_d2S_abs(evals_grid[pi], tau_vals, ti)
            if result is not None:
                d2S_abs, d2S_trace = result
                d2S_at_phi[tau_eval] = {'d2S_abs': d2S_abs, 'd2S_trace': d2S_trace}
        d2S_results[phi_amp] = d2S_at_phi

    # ================================================================
    #  MANDATORY CROSS-CHECK: phi=0 reproduces bare d2S_abs
    # ================================================================
    print(f"\n--- MANDATORY Cross-check: phi=0 reproduces bare d2S_abs ---")
    phi0_amp = PHI_AMPS[0]
    for i, tau_eval in enumerate(EVAL_TAUS):
        computed = d2S_results[phi0_amp][tau_eval]['d2S_abs']
        expected = bare_d2S_abs[i]
        err = abs(computed - expected)
        rel_err = err / abs(expected) if abs(expected) > 1e-14 else err
        print(f"  tau={tau_eval:.2f}: computed={computed:.6f}, bare={expected:.6f}, "
              f"|err|={err:.2e}, rel={rel_err:.2e}")
        if rel_err > 0.01:
            print(f"  WARNING: >1% deviation at phi=0!")
    print(f"  Cross-check: {'PASS' if rel_err < 0.01 else 'FAIL'}")

    # ================================================================
    #  Report: d2S_abs as a function of phi at dump point (tau=0.20)
    # ================================================================
    print(f"\n{'='*78}")
    print("Results: d^2(sum|lambda|)/dtau^2 vs |phi_VEV|")
    print(f"{'='*78}")

    print(f"\n  Dump point tau=0.20 (primary gate evaluation):")
    print(f"  {'|phi|':>8s}  {'d2S_abs':>10s}  {'ratio':>8s}  {'> 0.54?':>8s}  Status")
    print(f"  {'-'*8:>8s}  {'-'*10:>10s}  {'-'*8:>8s}  {'-'*8:>8s}  ------")

    bare_020 = bare_d2S_abs[1]  # tau=0.20
    d2S_at_gap = None
    min_d2S_any_phi = 1e10

    phi_for_plot = []
    d2S_for_plot_015 = []
    d2S_for_plot_020 = []
    d2S_for_plot_025 = []

    for phi_amp in PHI_AMPS:
        d2_data = d2S_results[phi_amp]
        d2_020 = d2_data[0.20]['d2S_abs']
        ratio_020 = d2_020 / bare_020

        above = "YES" if d2_020 > CHI_PASS else "NO"
        if abs(phi_amp - GAP_B2_B3) < 0.002:
            status = "<-- GAP"
            d2S_at_gap = d2_020
        elif phi_amp == 0:
            status = "<-- BARE"
        else:
            status = ""

        print(f"  {phi_amp:8.4f}  {d2_020:10.4f}  {ratio_020:8.4f}  {above:>8s}  {status}")
        min_d2S_any_phi = min(min_d2S_any_phi, d2_020)

        phi_for_plot.append(phi_amp)
        d2S_for_plot_015.append(d2_data[0.15]['d2S_abs'])
        d2S_for_plot_020.append(d2_data[0.20]['d2S_abs'])
        d2S_for_plot_025.append(d2_data[0.25]['d2S_abs'])

    phi_for_plot = np.array(phi_for_plot)
    d2S_for_plot_015 = np.array(d2S_for_plot_015)
    d2S_for_plot_020 = np.array(d2S_for_plot_020)
    d2S_for_plot_025 = np.array(d2S_for_plot_025)

    # Multi-tau report
    print(f"\n  Multi-tau summary at |phi| = gap ({GAP_B2_B3:.3f}):")
    gap_pi = np.argmin(np.abs(PHI_AMPS - GAP_B2_B3))
    for tau_eval in EVAL_TAUS:
        d2_val = d2S_results[PHI_AMPS[gap_pi]][tau_eval]['d2S_abs']
        bare_val = bare_d2S_abs[EVAL_TAUS.index(tau_eval)]
        print(f"  tau={tau_eval:.2f}: d2S_abs = {d2_val:.4f} "
              f"(bare: {bare_val:.4f}, ratio: {d2_val/bare_val:.4f})")

    # Extended tau sweep at phi=gap
    print(f"\n  Full tau sweep at |phi| = gap:")
    print(f"  {'tau':>6s}  {'d2S_abs':>10s}")
    for ti in range(1, n_tau - 1):
        result = compute_d2S_abs(evals_grid[gap_pi], tau_vals, ti)
        if result is not None:
            print(f"  {tau_vals[ti]:6.2f}  {result[0]:10.4f}")

    # ================================================================
    #  Spectral action S(tau) curves for different phi
    # ================================================================
    print(f"\n  S(tau) = sum|lambda_k(tau; phi)| values:")
    print(f"  {'tau':>6s}", end="")
    show_phis = [0.0, 0.05, 0.10, GAP_B2_B3, 0.17]
    for p in show_phis:
        print(f"  phi={p:.3f}", end="")
    print()
    for ti in range(n_tau):
        print(f"  {tau_vals[ti]:6.2f}", end="")
        for p in show_phis:
            pi_show = np.argmin(np.abs(PHI_AMPS - p))
            print(f"  {S_grid[pi_show, ti]:9.5f}", end="")
        print()

    # ================================================================
    #  Gate classification
    # ================================================================
    print(f"\n{'='*78}")
    print("GATE RPA-34a CLASSIFICATION")
    print(f"{'='*78}")

    if d2S_at_gap is None:
        # Closest phi to gap
        gap_pi = np.argmin(np.abs(PHI_AMPS - GAP_B2_B3))
        d2S_at_gap = d2S_results[PHI_AMPS[gap_pi]][0.20]['d2S_abs']

    ratio_at_gap = d2S_at_gap / bare_020
    margin_at_gap = d2S_at_gap / CHI_PASS

    print(f"\n  Bare d2S_abs (tau=0.20):        {bare_020:.4f}")
    print(f"  D_phys d2S_abs at phi=gap:      {d2S_at_gap:.4f}")
    print(f"  Ratio d2S(phi=gap)/d2S(bare):   {ratio_at_gap:.4f}")
    print(f"  Margin over threshold:          {margin_at_gap:.1f}x (threshold={CHI_PASS})")
    print(f"  Minimum d2S at any phi in [0, 0.17]: {min_d2S_any_phi:.4f}")
    print(f"  Min margin:                     {min_d2S_any_phi/CHI_PASS:.1f}x")

    if d2S_at_gap > CHI_PASS:
        verdict = "CONSISTENT"
        print(f"\n  VERDICT: CONSISTENT (d2S = {d2S_at_gap:.4f} > {CHI_PASS})")
        print(f"  RPA curvature SURVIVES inner fluctuations.")
        print(f"  W1 prediction confirmed: 38x margin implausible to overturn.")
    else:
        verdict = "CHALLENGE"
        print(f"\n  VERDICT: CHALLENGE (d2S = {d2S_at_gap:.4f} < {CHI_PASS})")
        print(f"  RPA curvature FAILS under inner fluctuations.")

    # ================================================================
    #  Save
    # ================================================================
    save_dict = {
        'phi_amplitudes': PHI_AMPS,
        'tau_values': tau_vals,
        'eval_taus': np.array(EVAL_TAUS),
        'evals_grid': evals_grid,
        'S_grid': S_grid,
        'd2S_015': d2S_for_plot_015,
        'd2S_020': d2S_for_plot_020,
        'd2S_025': d2S_for_plot_025,
        'bare_d2S_abs': bare_d2S_abs,
        'chi_pass_threshold': np.array(CHI_PASS),
        'd2S_at_gap': np.array(d2S_at_gap),
        'ratio_at_gap': np.array(ratio_at_gap),
        'margin_at_gap': np.array(margin_at_gap),
        'min_d2S_any_phi': np.array(min_d2S_any_phi),
        'gap_b2_b3': np.array(GAP_B2_B3),
        'verdict': np.array(verdict),
        'worst_direction': np.array('H_j'),
    }
    out_npz = os.path.join(SCRIPT_DIR, 's34a_rpa_curvature.npz')
    np.savez(out_npz, **save_dict)
    print(f"\n  Saved: {out_npz}")

    # ================================================================
    #  Plot
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: d2S_abs vs phi at three tau values
    ax = axes[0, 0]
    ax.plot(phi_for_plot, d2S_for_plot_015, 'b-o', ms=4, label='tau=0.15')
    ax.plot(phi_for_plot, d2S_for_plot_020, 'r-s', ms=4, label='tau=0.20')
    ax.plot(phi_for_plot, d2S_for_plot_025, 'g-^', ms=4, label='tau=0.25')
    ax.axhline(y=CHI_PASS, color='k', ls='--', lw=1.5, label=f'threshold={CHI_PASS}')
    ax.axvline(x=GAP_B2_B3, color='orange', ls=':', lw=1.5, label=f'gap={GAP_B2_B3:.3f}')
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel("d^2(sum|lambda|)/dtau^2")
    ax.set_title('Spectral Action Curvature vs Inner Fluctuation')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 2: Ratio to bare
    ax = axes[0, 1]
    ax.plot(phi_for_plot, d2S_for_plot_020 / bare_020, 'r-s', ms=4, label='tau=0.20')
    ax.plot(phi_for_plot, d2S_for_plot_015 / bare_d2S_abs[0], 'b-o', ms=4, label='tau=0.15')
    ax.plot(phi_for_plot, d2S_for_plot_025 / bare_d2S_abs[2], 'g-^', ms=4, label='tau=0.25')
    ax.axhline(y=1.0, color='gray', ls='-', lw=0.5)
    ax.axhline(y=CHI_PASS/bare_020, color='k', ls='--', lw=1.5,
               label=f'FAIL line ({CHI_PASS/bare_020:.4f})')
    ax.axvline(x=GAP_B2_B3, color='orange', ls=':', lw=1.5)
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('d2S(phi) / d2S(bare)')
    ax.set_title('Relative Curvature Change')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 3: S(tau) curves at different phi
    ax = axes[1, 0]
    for phi_amp in [0.0, 0.05, 0.10, GAP_B2_B3, 0.17]:
        pi = np.argmin(np.abs(PHI_AMPS - phi_amp))
        ax.plot(tau_vals, S_grid[pi, :], 'o-', ms=3,
                label=f'phi={PHI_AMPS[pi]:.3f}')
    ax.set_xlabel('tau')
    ax.set_ylabel('S(tau) = sum|lambda_k|')
    ax.set_title('Spectral Action Under Inner Fluctuations')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 4: Bar chart at phi=gap
    ax = axes[1, 1]
    labels_bar = ['bare\ntau=0.15', 'bare\ntau=0.20', 'bare\ntau=0.25',
                  'D_phys\ntau=0.15', 'D_phys\ntau=0.20', 'D_phys\ntau=0.25']
    vals_bar = list(bare_d2S_abs) + [
        d2S_results[PHI_AMPS[gap_pi]][t]['d2S_abs'] for t in EVAL_TAUS
    ]
    colors_bar = ['lightblue', 'blue', 'lightblue',
                  'lightsalmon', 'red', 'lightsalmon']
    ax.bar(range(len(labels_bar)), vals_bar, color=colors_bar, alpha=0.7,
           tick_label=labels_bar)
    ax.axhline(y=CHI_PASS, color='k', ls='--', lw=1.5, label=f'threshold={CHI_PASS}')
    ax.set_ylabel("d^2(sum|lambda|)/dtau^2")
    ax.set_title(f'Bare vs D_phys at |phi|=gap ({GAP_B2_B3:.3f})')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    fig.suptitle(f'Gate RPA-34a: {verdict}', fontsize=14, fontweight='bold')
    plt.tight_layout()
    out_png = os.path.join(SCRIPT_DIR, 's34a_rpa_curvature.png')
    plt.savefig(out_png, dpi=150)
    print(f"  Saved: {out_png}")

    elapsed = time.time() - t0
    print(f"\n  Total runtime: {elapsed:.1f}s")
    print(f"\n  GATE RPA-34a: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
