"""
S22C-HIGGS-SIGMA: canonical-compliant re-run of s22c_higgs_sigma.py
===================================================================

Re-run of computations/session-22/s22c_higgs_sigma.py (Session 22c, 2026-02-20).
Patch: add `from canonical_constants import *`, tag local intermediates,
cap CPU threads, and preserve the archive baseline by writing to
s22c_higgs_sigma.npz/.png (does NOT overwrite archive).

Hypothesis tested (Trap 3): The CCM Higgs-sigma portal coupling
    lambda_{H,sigma}(tau) = pi^2 * e(tau) / (2 * f_0 * a(tau) * c(tau))
is EXACTLY tau-independent because e/(a*c) = 1/dim(spinor_8D) = 1/16 is a
geometric identity pinned by the Peter-Weyl trace structure of D_K on
(SU(3), g_Jensen). Portal cannot select the tau modulus.

All framework constants imported from canonical_constants. All structural
constants (spinor dim = 16, Trap 2 weights 4/13 and 9/13, SD coefficients
from a_4 spinor formula) are tagged `# (local)` — they are algebraic
invariants, not framework scales.

Author: gen-physicist (re-run, Session 81)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import *  # noqa: F401,F403

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    get_irrep,
)


# ----------------------------------------------------------------------
# SHA-256 INPUT PINS (logged to stdout in first 20 lines)
# ----------------------------------------------------------------------
def _sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


INPUT_PINS = {
    's22c_higgs_sigma_archive': _sha256_file(
        os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared',
                     's22c_higgs_sigma.py')),
    'dirac_spectrum': _sha256_file(
        os.path.join(SCRIPT_DIR, 'dirac_spectrum.py')),
    'canonical_constants': _sha256_file(
        os.path.join(SCRIPT_DIR, 'canonical_constants.py')),
    's22c_higgs_sigma_self': _sha256_file(
        os.path.abspath(__file__)),
}


# ----------------------------------------------------------------------
# CURVATURE INFRASTRUCTURE (scalar curvature invariants on Jensen SU(3))
# ----------------------------------------------------------------------
def R_exact(tau):
    """Scalar curvature R_K(tau) on (SU(3), g_Jensen)."""
    return -0.25*np.exp(-4*tau) + 2*np.exp(-tau) - 0.25 + 0.5*np.exp(2*tau)  # (local) algebraic


def Ric2_exact(tau):
    """|Ric|^2(tau) on (SU(3), g_Jensen)."""
    return (
        (1.0/12.0) * np.exp(-8*tau)                # (local) algebraic
        + (-1.0/2.0) * np.exp(-5*tau)              # (local) algebraic
        + (1.0/8.0) * np.exp(-4*tau)               # (local) algebraic
        + (13.0/12.0) * np.exp(-2*tau)             # (local) algebraic
        + (-1.0/2.0) * np.exp(-tau)                # (local) algebraic
        + 1.0/8.0                                   # (local) algebraic
        + (1.0/12.0) * np.exp(4*tau)               # (local) algebraic
    )


def K_exact(tau):
    """|Riem|^2(tau) = Kretschner scalar on (SU(3), g_Jensen)."""
    return (
        (23.0/96.0) * np.exp(-8*tau)               # (local) algebraic
        + (-1.0) * np.exp(-5*tau)                  # (local) algebraic
        + (5.0/16.0) * np.exp(-4*tau)              # (local) algebraic
        + (11.0/6.0) * np.exp(-2*tau)              # (local) algebraic
        + (-3.0/2.0) * np.exp(-tau)                # (local) algebraic
        + 17.0/32.0                                 # (local) algebraic
        + (1.0/12.0) * np.exp(4*tau)               # (local) algebraic
    )


# ----------------------------------------------------------------------
# APPROACH A: GAUGE-SECTOR a_4 AND ITS TAU-DERIVATIVES
# ----------------------------------------------------------------------
def gauge_coupling_ratio(tau):
    """g_1^2 ~ e^{-2 tau}, g_2^2 ~ e^{+2 tau} (Session 17a B-1)."""
    return np.exp(-2*tau), np.exp(2*tau)


def a4_gauge_component(tau):
    c1 = 4.0 / 13.0                                 # (local) Trap 2 U(1) weight
    c2 = 9.0 / 13.0                                 # (local) Trap 2 SU(2) weight
    alpha1_sq, alpha2_sq = gauge_coupling_ratio(tau)
    return c1 * alpha1_sq + c2 * alpha2_sq


def da4_gauge_dtau(tau):
    c1 = 4.0 / 13.0                                 # (local)
    c2 = 9.0 / 13.0                                 # (local)
    return c1 * (-2) * np.exp(-2*tau) + c2 * 2 * np.exp(2*tau)


def d2a4_gauge_dtau2(tau):
    c1 = 4.0 / 13.0                                 # (local)
    c2 = 9.0 / 13.0                                 # (local)
    return c1 * 4 * np.exp(-2*tau) + c2 * 4 * np.exp(2*tau)


# ----------------------------------------------------------------------
# APPROACH B: FULL SEELEY-DEWITT a_4 (SPIN)
# ----------------------------------------------------------------------
def a4_reduced_spin(tau):
    R = R_exact(tau)                                # (local)
    Ric2 = Ric2_exact(tau)                          # (local)
    K = K_exact(tau)                                # (local)
    return (1.0/90.0) * (125.0 * R**2 - 8.0 * Ric2 + 2.0 * K)  # (local) SD spin a_4


def da4_spin_dtau(tau, h=1e-6):                     # (local) finite-diff step
    return (a4_reduced_spin(tau + h) - a4_reduced_spin(tau - h)) / (2*h)


def d2a4_spin_dtau2(tau, h=1e-5):                   # (local) finite-diff step
    return (a4_reduced_spin(tau + h) - 2*a4_reduced_spin(tau) + a4_reduced_spin(tau - h)) / h**2


# ----------------------------------------------------------------------
# APPROACH C: EIGENVALUE-BASED YUKAWA TRACES FROM D_K(tau)
# ----------------------------------------------------------------------
def extract_yukawa_structure(tau, max_pq_sum=3):
    """
    Decomposes D_K into Killing (u(2)) and non-Killing (C^2) parts.
    Returns CCM traces a, b, c, d, e per Paper 13 eq 3.1-3.3.
    """
    gens = su3_generators()                         # (local) SU(3) generators
    f_abc = compute_structure_constants(gens)       # (local)
    B_ab = compute_killing_form(f_abc)              # (local) Killing form
    g_s = jensen_metric(B_ab, tau)                  # (local) Jensen-deformed metric
    E = orthonormal_frame(g_s)                      # (local) ON frame
    ft = frame_structure_constants(f_abc, E)        # (local)
    Gamma = connection_coefficients(ft)             # (local) Levi-Civita connection
    gamma_list = build_cliff8()                     # (local) Cliff8 basis
    Omega = spinor_connection_offset(Gamma, gamma_list)  # (local) spinor conn offset

    results = {
        'full_evals': {},
        'yukawa_evals': {},
        'majorana_evals': {},
        'sector_dims': {},
    }

    a_trace = 0.0                                   # (local) Tr(Y^dag Y)
    b_trace = 0.0                                   # (local) Tr((Y^dag Y)^2)
    c_trace = 0.0                                   # (local) Tr(M_R^* M_R)
    d_trace = 0.0                                   # (local) Tr((M_R^* M_R)^2)
    e_trace = 0.0                                   # (local) Tr(Y^* Y M^* M)

    # Omega is sector-independent; 1j*Omega is Hermitian with real eigvals.
    Omega_evals = np.linalg.eigvalsh(1j * Omega)
    M_R_squared = Omega_evals**2                    # (local)
    c_trace = float(np.sum(M_R_squared))
    d_trace = float(np.sum(M_R_squared**2))
    results['majorana_evals'] = np.sort(np.abs(Omega_evals))
    results['Omega_evals'] = Omega_evals

    sectors = []                                    # (local) (p,q) list
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            sectors.append((p, q))

    for (p, q) in sectors:
        result_irrep = get_irrep(p, q, gens, f_abc)
        if result_irrep is None:
            continue
        rho_mats, dim_rho = result_irrep
        if rho_mats is None or len(rho_mats) == 0:
            continue
        n_spin = 16                                 # (local) Cliff8 spinor dimension
        D_size = dim_rho * n_spin                   # (local) total sector dim

        # Non-Killing (Yukawa) part: directions 3,4,5,6 = C^2 = SU(3)/U(2)
        D_yukawa = np.zeros((D_size, D_size), dtype=complex)  # (local)
        non_killing_idx = [3, 4, 5, 6]              # (local) C^2 direction indices
        for a in range(8):
            if a not in non_killing_idx:
                continue
            rho_a = np.zeros((dim_rho, dim_rho), dtype=complex)  # (local)
            for b in range(8):
                rho_a += E[a, b] * rho_mats[b]
            D_yukawa += np.kron(rho_a, gamma_list[a])

        # Full D_pi for reference
        D_full = np.zeros((D_size, D_size), dtype=complex)  # (local)
        for a in range(8):
            rho_a = np.zeros((dim_rho, dim_rho), dtype=complex)  # (local)
            for b in range(8):
                rho_a += E[a, b] * rho_mats[b]
            D_full += np.kron(rho_a, gamma_list[a])
        D_full += np.kron(np.eye(dim_rho), Omega)

        evals_full = np.linalg.eigvalsh(1j * D_full)
        evals_yukawa = np.linalg.eigvalsh(1j * D_yukawa)

        results['full_evals'][(p, q)] = np.sort(np.abs(evals_full))
        results['yukawa_evals'][(p, q)] = np.sort(np.abs(evals_yukawa))
        results['sector_dims'][(p, q)] = dim_rho

        Y2 = evals_yukawa**2                        # (local)
        mult = dim_rho                              # (local) Peter-Weyl multiplicity

        a_trace += mult * np.sum(Y2)
        b_trace += mult * np.sum(Y2**2)

        D_Y_sq = D_yukawa.conj().T @ D_yukawa       # (local) Y^dag Y operator
        Omega_full = np.kron(np.eye(dim_rho), Omega)  # (local) lifted Omega
        M_sq = Omega_full.conj().T @ Omega_full     # (local) M^dag M operator

        cross = float(np.real(np.trace(D_Y_sq @ M_sq)))  # (local)
        e_trace += mult * cross

    results['a'] = float(a_trace)
    results['b'] = float(b_trace)
    results['c'] = float(c_trace)
    results['d'] = float(d_trace)
    results['e'] = float(e_trace)

    return results


def lambda_Hsigma_ccm(a, c, e, f0=1.0):             # (local) CCM formula
    """lambda_{H,sigma} = pi^2 * e / (2 * f_0 * a * c)  (Paper 13 eq 3.1-3.3)."""
    if abs(a) < 1e-15 or abs(c) < 1e-15:            # (local) tolerance
        return 0.0
    return np.pi**2 * e / (2 * f0 * a * c)


# ----------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------
def main():
    # First 20 lines of stdout: SHA-256 input pins
    print("=" * 76)
    print("  S22C-HIGGS-SIGMA: canonical-compliant re-run")
    print("  Session 22c -> S81 audit")
    print("=" * 76)
    print("INPUT SHA-256 PINS:")
    for k, v in INPUT_PINS.items():
        print(f"  {k}: {v}")
    print("=" * 76)

    # Pre-registered machinery
    MAX_PQ_SUM = 3                                   # (local) (p,q) cutoff
    TAU_GRID_A = np.linspace(0, 2.0, 21)            # (local) gauge-sector scan
    TAU_EIG = np.array([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35,
                        0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.50, 2.00])  # (local) eigenvalue scan
    F0_CUTOFF = 1.0                                  # (local) cutoff zeroth moment

    # ============ APPROACH A: gauge-sector a_4 ============
    print("\n  APPROACH A: GAUGE-SECTOR a_4(tau)")
    a4g_vals, da4g_vals, d2a4g_vals = [], [], []    # (local)
    for tau in TAU_GRID_A:
        a4g = a4_gauge_component(tau)               # (local)
        da4g = da4_gauge_dtau(tau)                  # (local)
        d2a4g = d2a4_gauge_dtau2(tau)               # (local)
        a4g_vals.append(a4g)
        da4g_vals.append(da4g)
        d2a4g_vals.append(d2a4g)
    print(f"  d2a4_gauge/dtau2 min = {min(d2a4g_vals):.4f}, max = {max(d2a4g_vals):.4f}")
    print(f"  All positive? {all(v > 0 for v in d2a4g_vals)}")

    # ============ APPROACH B: full SD a_4 ============
    print("\n  APPROACH B: FULL SD a_4 SECOND DERIVATIVE")
    a4s_vals, da4s_vals, d2a4s_vals = [], [], []    # (local)
    for tau in TAU_GRID_A:
        a4s = a4_reduced_spin(tau)                  # (local)
        da4s = da4_spin_dtau(tau)                   # (local)
        d2a4s = d2a4_spin_dtau2(tau)                # (local)
        a4s_vals.append(a4s)
        da4s_vals.append(da4s)
        d2a4s_vals.append(d2a4s)
    print(f"  d2a4_spin/dtau2 min = {min(d2a4s_vals):.4f}, max = {max(d2a4s_vals):.4f}")

    # ============ APPROACH C: CCM portal from D_K eigvals ============
    print(f"\n  APPROACH C: CCM PORTAL FROM D_K(tau) EIGENVALUES (max_pq_sum={MAX_PQ_SUM})")
    a_vals, b_vals, c_vals, d_vals_trace, e_vals = [], [], [], [], []  # (local)
    lambda_hs_vals = []                             # (local)
    for tau in TAU_EIG:
        res = extract_yukawa_structure(tau, max_pq_sum=MAX_PQ_SUM)
        a_val = res['a']                            # (local)
        b_val = res['b']                            # (local)
        c_val = res['c']                            # (local)
        d_val = res['d']                            # (local)
        e_val = res['e']                            # (local)
        lam_hs = lambda_Hsigma_ccm(a_val, c_val, e_val, f0=F0_CUTOFF)  # (local)

        a_vals.append(a_val)
        b_vals.append(b_val)
        c_vals.append(c_val)
        d_vals_trace.append(d_val)
        e_vals.append(e_val)
        lambda_hs_vals.append(lam_hs)

    lam_arr = np.array(lambda_hs_vals)
    lam_spread = float(np.max(lam_arr) - np.min(lam_arr))  # (local)
    lam_mean = float(np.mean(lam_arr))              # (local)
    is_constant = lam_spread / max(abs(lam_mean), 1e-15) < 1e-10  # (local) tolerance
    all_positive = all(v > 0 for v in lambda_hs_vals)  # (local)
    any_negative_020_035 = any(lambda_hs_vals[i] < 0
                               for i in range(len(TAU_EIG))
                               if 0.20 <= TAU_EIG[i] <= 0.35)  # (local)

    # ============ Cross-check: e/(a*c) = 1/16 identity ============
    print("\n  CROSS-CHECK: e(tau)/(a(tau)*c(tau)) identity")
    eac_ratios = [e_vals[i]/(a_vals[i]*c_vals[i])
                  for i in range(len(TAU_EIG))]     # (local)
    target_ratio = 1.0/16.0                         # (local) spinor-dim identity
    max_dev = float(np.max(np.abs(np.array(eac_ratios) - target_ratio)))  # (local)
    print(f"    e/(a*c) target   = {target_ratio:.16f}")
    print(f"    e/(a*c) observed = {eac_ratios[0]:.16f} (tau=0)")
    print(f"    Max deviation   = {max_dev:.2e}")

    # ============ Verdict mapping ============
    idx_030 = int(np.argmin(np.abs(TAU_EIG - 0.30)))  # (local)
    lam_030 = lambda_hs_vals[idx_030]               # (local)

    if any_negative_020_035:
        verdict = "DECISIVE"                        # (local)
        bf = 30.0                                    # (local)
    elif is_constant and all_positive:
        verdict = "STRUCTURAL CLOSURE (Trap 3)"     # (local)
        bf = 0.3                                     # (local)
    elif all_positive:
        verdict = "CLOSED"                          # (local)
        bf = 0.3                                     # (local)
    else:
        verdict = "NEUTRAL"                         # (local)
        bf = 1.0                                     # (local)

    # ============ Save reproduction npz ============
    out_npz = os.path.join(SCRIPT_DIR, 's22c_higgs_sigma.npz')  # (local)
    np.savez(out_npz,
             tau_grid_A=TAU_GRID_A,
             a4_gauge=np.array(a4g_vals),
             da4_gauge=np.array(da4g_vals),
             d2a4_gauge=np.array(d2a4g_vals),
             a4_spin=np.array(a4s_vals),
             da4_spin=np.array(da4s_vals),
             d2a4_spin=np.array(d2a4s_vals),
             tau_eig=TAU_EIG,
             a_trace=np.array(a_vals),
             b_trace=np.array(b_vals),
             c_trace=np.array(c_vals),
             d_trace=np.array(d_vals_trace),
             e_trace=np.array(e_vals),
             lambda_Hsigma=np.array(lambda_hs_vals),
             verdict=verdict,
             bf=bf,
             max_dev_1_over_16=max_dev,
             )

    # ============ Reproduction vs MCP baseline ============
    baseline_npz = os.path.join(os.path.dirname(SCRIPT_DIR),
                                'computations/_shared', 's22c_higgs_sigma.npz')  # (local)
    if os.path.exists(baseline_npz):
        base = np.load(baseline_npz, allow_pickle=True)
        lam_rel_err = float(np.max(np.abs(
            np.array(lambda_hs_vals) - base['lambda_Hsigma']))
            / max(abs(base['lambda_Hsigma'][0]), 1e-30))  # (local)
        a_rel_err = float(np.max(np.abs(
            np.array(a_vals) - base['a_trace'])) / max(base['a_trace'][0], 1e-30))  # (local)
        c_rel_err = float(np.max(np.abs(
            np.array(c_vals) - base['c_trace'])) / max(base['c_trace'][0], 1e-30))  # (local)
        e_rel_err = float(np.max(np.abs(
            np.array(e_vals) - base['e_trace'])) / max(base['e_trace'][0], 1e-30))  # (local)
        print(f"\n  REPRODUCTION vs baseline:")
        print(f"    lambda_Hs rel-err = {lam_rel_err:.2e}")
        print(f"    a_trace rel-err   = {a_rel_err:.2e}")
        print(f"    c_trace rel-err   = {c_rel_err:.2e}")
        print(f"    e_trace rel-err   = {e_rel_err:.2e}")
    else:
        lam_rel_err = a_rel_err = c_rel_err = e_rel_err = float('nan')

    # ============ Closure SHA: SHA-256 of ordered input-pin map ============
    closure_string = "|".join(f"{k}={v}" for k, v in sorted(INPUT_PINS.items()))  # (local)
    closure_sha = hashlib.sha256(closure_string.encode()).hexdigest()  # (local)

    # ============ Final canonical 4-tuple output tag ============
    print("\n" + "=" * 76)
    print("  CANONICAL OUTPUT TAG (4-tuple):")
    print(f"    value=lambda_Hs={lam_030:.8f}_constant,e_over_ac={eac_ratios[0]:.16f}")
    print(f"    scheme=CCM-portal-spinor-trace")
    print(f"    convention=non-Killing-Cliff8-C2-sector")
    print(f"    L_max={MAX_PQ_SUM}")
    print(f"    sha256={closure_sha}")
    print("=" * 76)

    # S81 canonical verdict line
    is_pass = is_constant and all_positive           # (local)
    status = "PASS" if is_pass else "FAIL"           # (local)
    print(f"\nS22C-HIGGS-SIGMA: {status} -- "
          f"value=lambda_Hs={lam_030:.8f}_constant,e_over_ac={eac_ratios[0]:.16f} "
          f"scheme=CCM-portal-spinor-trace "
          f"convention=non-Killing-Cliff8-C2-sector "
          f"L_max={MAX_PQ_SUM} "
          f"sha256={closure_sha}")

    return {
        'verdict': verdict,
        'status': status,
        'lambda_030': lam_030,
        'e_over_ac': eac_ratios[0],
        'max_dev_1_over_16': max_dev,
        'closure_sha': closure_sha,
        'is_constant': is_constant,
        'all_positive': all_positive,
        'lam_rel_err': lam_rel_err,
        'a_rel_err': a_rel_err,
        'c_rel_err': c_rel_err,
        'e_rel_err': e_rel_err,
    }


if __name__ == "__main__":
    main()
