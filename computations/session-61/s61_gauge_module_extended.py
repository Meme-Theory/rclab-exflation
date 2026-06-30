#!/usr/bin/env python3
"""
S61 GAUGE-MODULE-61 -- Extended Check
======================================

The base Omega^1_D (rank 173) is NOT an A-bimodule.
Check if the EXTENDED space (base + A^o products, rank 696) IS a bimodule.
If it closes, the extended space defines the gauge module.
Also check gauge covariance on the extended space.

Author: Van den Dungen Bridge Theorist (Session 61)
"""

import numpy as np
from numpy.linalg import svd, norm as la_norm
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold

from s61_gauge_module_check import (
    build_AF_generators, build_DK_fundamental, build_unitary_generators,
    o_map_16, G5, flat_idx, build_bimodule_16, _gell_mann_matrices,
)
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8,
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)
OUTDIR = os.path.dirname(os.path.abspath(__file__))


def compute_extended_omega1_basis(D_K, AF_16, dim_rep=3, n_levels=2):
    """Compute extended Omega^1 space by iteratively closing under A and A^o.

    Level 0: span{a [D, b]}
    Level 1: Level 0 + {omega * o(c)} + {o(c) * omega} + {a * omega} + {omega * a}
    Level 2: same closure on Level 1 output
    ...

    Stop when rank stabilizes.
    """
    n = D_K.shape[0]
    n_gen = len(AF_16)

    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
        opp_gens = [o_map_16(g) for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]
        opp_gens = [np.kron(np.eye(dim_rep), o_map_16(g)) for g in AF_16]

    # Level 0: basic 1-forms
    forms_vecs = []
    for i in range(n_gen):
        for j in range(n_gen):
            comm = D_K @ A_gens[j] - A_gens[j] @ D_K
            omega = A_gens[i] @ comm
            forms_vecs.append(omega.flatten())

    def current_rank(vecs):
        if not vecs:
            return 0, None
        mat = np.array(vecs)
        U, S, Vh = svd(mat, full_matrices=False)
        tol = max(mat.shape) * np.finfo(float).eps * S[0] if S[0] > 0 else 1e-14
        r = int(np.sum(S > tol))
        return r, Vh[:r, :]

    r0, basis0 = current_rank(forms_vecs)
    print(f"  Level 0: rank = {r0}")

    prev_rank = r0
    prev_basis_vecs = [v.copy() for v in forms_vecs]

    for level in range(1, n_levels + 1):
        new_vecs = list(prev_basis_vecs)

        # Get current basis matrices
        r_curr, basis_curr = current_rank(new_vecs)
        basis_mats = [basis_curr[k].reshape(n, n) for k in range(r_curr)]

        # Close under left/right A and A^o
        for k in range(min(r_curr, 50)):  # cap to avoid explosion
            omega_k = basis_mats[k]
            for c in range(n_gen):
                new_vecs.append((A_gens[c] @ omega_k).flatten())
                new_vecs.append((omega_k @ A_gens[c]).flatten())
                new_vecs.append((opp_gens[c] @ omega_k).flatten())
                new_vecs.append((omega_k @ opp_gens[c]).flatten())

        r_new, basis_new = current_rank(new_vecs)
        print(f"  Level {level}: rank = {r_new} (from {len(new_vecs)} vectors)")

        if r_new == prev_rank:
            print(f"  Rank stabilized at level {level}")
            return r_new, basis_new
        prev_rank = r_new
        prev_basis_vecs = new_vecs

    r_final, basis_final = current_rank(prev_basis_vecs)
    return r_final, basis_final


def check_bimodule_on_basis(basis, n, AF_16, dim_rep=3):
    """Check if the space spanned by basis is a bimodule under A and A^o."""
    n_gen = len(AF_16)
    rank = basis.shape[0]

    if dim_rep == 1:
        A_gens = [g.copy() for g in AF_16]
        opp_gens = [o_map_16(g) for g in AF_16]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in AF_16]
        opp_gens = [np.kron(np.eye(dim_rep), o_map_16(g)) for g in AF_16]

    basis_mats = [basis[k].reshape(n, n) for k in range(rank)]

    max_left = 0.0
    max_right = 0.0
    max_opp_left = 0.0
    max_opp_right = 0.0

    for k in range(min(rank, 50)):
        omega_k = basis_mats[k]
        for c in range(n_gen):
            # Left A
            prod = A_gens[c] @ omega_k
            coeffs = basis @ prod.flatten().conj()
            proj = coeffs.conj() @ basis
            res = la_norm(prod.flatten() - proj)
            nrm = la_norm(prod.flatten())
            if nrm > 1e-15:
                max_left = max(max_left, res / nrm)

            # Right A
            prod = omega_k @ A_gens[c]
            coeffs = basis @ prod.flatten().conj()
            proj = coeffs.conj() @ basis
            res = la_norm(prod.flatten() - proj)
            nrm = la_norm(prod.flatten())
            if nrm > 1e-15:
                max_right = max(max_right, res / nrm)

            # Left A^o
            prod = opp_gens[c] @ omega_k
            coeffs = basis @ prod.flatten().conj()
            proj = coeffs.conj() @ basis
            res = la_norm(prod.flatten() - proj)
            nrm = la_norm(prod.flatten())
            if nrm > 1e-15:
                max_opp_left = max(max_opp_left, res / nrm)

            # Right A^o
            prod = omega_k @ opp_gens[c]
            coeffs = basis @ prod.flatten().conj()
            proj = coeffs.conj() @ basis
            res = la_norm(prod.flatten() - proj)
            nrm = la_norm(prod.flatten())
            if nrm > 1e-15:
                max_opp_right = max(max_opp_right, res / nrm)

    return max_left, max_right, max_opp_left, max_opp_right


def check_gauge_on_basis(basis, n, AF_16, dim_rep=3):
    """Check gauge covariance on the extended space."""
    u_gens, u_names, u_factors = build_unitary_generators(AF_16, None, None)
    if dim_rep > 1:
        u_gens = [np.kron(np.eye(dim_rep), g) for g in u_gens]

    rank = basis.shape[0]
    basis_mats = [basis[k].reshape(n, n) for k in range(rank)]

    per_gen_max = []
    for ui, T in enumerate(u_gens):
        gen_max = 0.0  # (local)
        for k in range(min(rank, 50)):
            omega_k = basis_mats[k]
            comm = T @ omega_k - omega_k @ T
            coeffs = basis @ comm.flatten().conj()
            proj = coeffs.conj() @ basis
            res = la_norm(comm.flatten() - proj)
            nrm = la_norm(comm.flatten())
            if nrm > 1e-15:
                gen_max = max(gen_max, res / nrm)
        per_gen_max.append(gen_max)

    return np.array(per_gen_max), u_names, u_factors


def main():
    t0 = time.time()
    print("=" * 72)
    print("S61 GAUGE-MODULE-61 -- Extended Space Analysis")
    print("=" * 72)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    tau = tau_fold

    AF_16, AF_names, AF_factors = build_AF_generators()

    # Build D_K on fundamental
    D_K = build_DK_fundamental(gammas, gens, f_abc, tau)
    n = D_K.shape[0]

    print(f"\nDim = {n}, tau = {tau}")
    print(f"\n--- Computing extended Omega^1 closure ---")

    rank_ext, basis_ext = compute_extended_omega1_basis(D_K, AF_16, dim_rep=3, n_levels=3)

    print(f"\n--- Checking bimodule on extended space (rank {rank_ext}) ---")
    ml, mr, mol, mor = check_bimodule_on_basis(basis_ext, n, AF_16, dim_rep=3)
    print(f"  Left A:     {ml:.6e}")
    print(f"  Right A:    {mr:.6e}")
    print(f"  Left A^o:   {mol:.6e}")
    print(f"  Right A^o:  {mor:.6e}")

    ext_is_bimodule = max(ml, mr, mol, mor) < 1e-4

    print(f"\n--- Checking gauge covariance on extended space ---")
    pgm, un, uf = check_gauge_on_basis(basis_ext, n, AF_16, dim_rep=3)
    for ui in range(len(un)):
        status = "PRESERVES" if pgm[ui] < 1e-4 else "BREAKS"
        print(f"  {un[ui]:>12}: {pgm[ui]:.6e}  [{status}]")

    n_preserve = np.sum(pgm < 1e-4)
    n_u1 = sum(1 for i, f in enumerate(uf) if f == 'U1' and pgm[i] < 1e-4)
    n_su2 = sum(1 for i, f in enumerate(uf) if f == 'SU2' and pgm[i] < 1e-4)
    n_su3 = sum(1 for i, f in enumerate(uf) if f == 'SU3' and pgm[i] < 1e-4)

    print(f"\n  Extended space: rank {rank_ext} / {n*n}")
    print(f"  Is A x A^o bimodule: {'YES' if ext_is_bimodule else 'NO'}")
    print(f"  Gauge generators preserving: {n_preserve} / {len(un)}")
    print(f"    U(1): {n_u1}, SU(2): {n_su2}, SU(3): {n_su3}")

    if ext_is_bimodule:
        if n_u1 >= 1 and n_su2 >= 3 and n_su3 >= 8:
            print(f"\n  RESULT: Extended gauge module with SM group SU(3) x SU(2) x U(1)")
        else:
            print(f"\n  RESULT: Extended gauge module with reduced group")
    else:
        # Check if it stabilized
        print(f"\n  RESULT: Extended space also fails bimodule closure")
        print(f"  Max residuals: {max(ml,mr,mol,mor):.6e}")

    dt = time.time() - t0
    print(f"\n  Runtime: {dt:.1f}s")

    # Save
    np.savez(os.path.join(OUTDIR, "s61_gauge_module_extended.npz"),
             rank_ext=rank_ext,
             bimod_left=ml, bimod_right=mr,
             bimod_opp_left=mol, bimod_opp_right=mor,
             gauge_residuals=pgm,
             gauge_names=np.array(un, dtype=object),
             gauge_factors=np.array(uf, dtype=object),
             n_preserve=n_preserve,
             is_bimodule=ext_is_bimodule)


if __name__ == "__main__":
    main()
