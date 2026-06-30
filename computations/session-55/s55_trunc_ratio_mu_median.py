#!/usr/bin/env python3
"""
S55 TRUNC-RATIO-55 — Supplementary: mu=median check
=====================================================

SF-SIGN-55 used mu=median (half-filling), which produced dS_f/dtau > 0.
The main TRUNC-RATIO script used mu=0 (theoretically correct per S34).
This supplementary checks whether the non-monotonicity from mu=median
also disappears at higher truncation.

Author: Spectral-Geometer (S55)
Date: 2026-03-22
"""

import sys
import os
import numpy as np
from time import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, str(_x2_shared_dir()))
from canonical_constants import tau_fold, Delta_0_OES

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, get_irrep, dirac_operator_on_irrep,
    _irrep_cache
)

Delta = Delta_0_OES
tau_values = np.array([0.00, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30])
trunc_levels = [3, 4, 5]

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

def bcs_occupation(omega, delta, mu):
    xi = np.abs(omega) - mu
    E = np.sqrt(xi**2 + delta**2)
    return 0.5 * (1.0 - xi / E)

def compute_spectrum_at_tau(tau, gens, f_abc, gammas, max_pq_sum):
    global _irrep_cache
    _irrep_cache.clear()
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    sector_data = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            d = dim_pq(p, q)
            if (p, q) == (0, 0):
                D_trivial = Omega.copy()
                evals_raw = np.linalg.eigvals(D_trivial)
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
                evals_raw = np.linalg.eigvals(D_pi)
            abs_omega = np.abs(evals_raw.imag)
            sector_data.append((p, q, d, abs_omega))
    return sector_data

def main():
    t0 = time()
    print("S55 TRUNC-RATIO-55 supplementary: mu=median check")
    print("=" * 60)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    max_trunc = max(trunc_levels)

    for L in trunc_levels:
        print(f"\n=== Truncation p+q <= {L} ===")
        S_f_vals = []

        for tau in tau_values:
            _irrep_cache.clear()
            sector_data = compute_spectrum_at_tau(tau, gens, f_abc, gammas, max_trunc)

            # Collect all PW-weighted eigenvalues for this truncation
            all_omega = []
            all_pw = []
            for (p, q, d, abs_omega) in sector_data:
                if p + q > L:
                    continue
                for om in abs_omega:
                    all_omega.append(om)
                    all_pw.append(d)
            all_omega = np.array(all_omega)
            all_pw = np.array(all_pw)

            # mu = median of PW-weighted eigenvalues
            # Weight each eigenvalue by PW multiplicity for median computation
            sorted_idx = np.argsort(all_omega)
            cum_weight = np.cumsum(all_pw[sorted_idx])
            total_weight = cum_weight[-1]
            median_idx = np.searchsorted(cum_weight, total_weight / 2)
            mu = all_omega[sorted_idx[median_idx]]

            # S_f with PW weighting
            n_k = bcs_occupation(all_omega, Delta, mu)
            S_f = np.sum(all_pw * n_k * all_omega)
            S_f_vals.append(S_f)

            S_b = np.sum(all_pw * all_omega**2)

        S_f_vals = np.array(S_f_vals)

        print(f"  tau     S_f(mu=median)")
        for i, tau in enumerate(tau_values):
            print(f"  {tau:.3f}  {S_f_vals[i]:.4f}")

        # Check monotonicity
        dSf = np.diff(S_f_vals)
        signs = np.sign(dSf)
        print(f"  dS_f signs: {signs}")
        nonmono = np.any(dSf > 0) and np.any(dSf < 0)
        print(f"  Non-monotone: {nonmono}")

        if nonmono:
            idx_max = np.argmax(S_f_vals)
            idx_min = np.argmin(S_f_vals)
            print(f"  Max at tau={tau_values[idx_max]:.3f}, Min at tau={tau_values[idx_min]:.3f}")

    print(f"\nRuntime: {time()-t0:.1f}s")
    print("DONE")

if __name__ == '__main__':
    main()
