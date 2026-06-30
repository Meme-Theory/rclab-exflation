#!/usr/bin/env python3
"""
S52 OFFJENSEN supplementary analysis:
1. Verify the Z_3 selection rule blocking B2 mixing
2. Scan sin2_13 as a function of C^2 split parameter
3. Find the split parameter that reproduces measured sin2_13 = 0.0222
4. Compute condition for R = 33 and matching sin2_13 simultaneously
"""

import numpy as np
import sys, os, time
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


sys.path.insert(0, str(_x2_shared_dir()))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from canonical_constants import tau_fold

# Import the full machinery from the main script
from s52_offjensen_pmns import (
    su3_generators, compute_structure_constants, build_cliff8,
    jensen_metric, general_metric, compute_spectrum,
    compute_singlet_overlap, extract_pmns_angles,
    get_irreps_for_spectrum, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset
)

def main():
    t_start = time.time()
    print("=" * 72)
    print("S52 OFFJENSEN SUPPLEMENTARY ANALYSIS")
    print("=" * 72)

    # Setup
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
    gammas = build_cliff8()
    irreps_data = get_irreps_for_spectrum(gens, f_abc, max_pq_sum=3)

    tau_ref = tau_fold
    g_jensen = jensen_metric(B_ab, tau_ref)
    _, evecs_ref = compute_spectrum(g_jensen, gens, f_abc, gammas, irreps_data, return_evecs=True)
    ref_evals = evecs_ref[(0,0)][0]
    ref_evecs = evecs_ref[(0,0)][1]

    # ==========================================
    # ANALYSIS 1: Z_3 charge verification
    # ==========================================
    print("\n" + "=" * 72)
    print("ANALYSIS 1: Z_3 CHARGE SELECTION RULE")
    print("=" * 72)

    # Build K_7 = rho(e_7) for the singlet (0,0)
    # In the singlet, rho(e_a) = 0 for all a. So K_7 = 0 in the singlet.
    # This means K_7 CANNOT distinguish B1, B2, B3 within the singlet!
    #
    # The Z_3 = (p-q) mod 3 charge is a representation-level quantum number.
    # Within a SINGLE irrep (like the singlet (0,0)), all eigenvalues share
    # the same Z_3 charge = 0.
    #
    # The reason B1-B3 mix but B2 doesn't is different:
    # Within the (0,0) singlet, the 8 positive eigenvalues come from
    # the 8 gamma_a generators hitting the single representation vector.
    # The B1/B2/B3 splitting comes from the spin connection curvature Omega.
    #
    # Let's examine the structure of Omega and the eigenvectors.

    E_ref = orthonormal_frame(g_jensen)
    ft_ref = frame_structure_constants(f_abc, E_ref)
    Gamma_ref = connection_coefficients(ft_ref)
    Omega_ref = spinor_connection_offset(Gamma_ref, gammas)

    # In the singlet (0,0), D = Omega (since rho = 0)
    # So the B1, B2, B3 eigenvalues are just eigenvalues of Omega!
    # Let's verify:
    iOmega = -1j * Omega_ref
    omega_evals = np.sort(np.linalg.eigvalsh(iOmega))
    pos_omega = omega_evals[omega_evals > 1e-6]
    print(f"\n  Omega eigenvalues (positive): {np.sort(pos_omega)}")
    print(f"  Reference singlet eigenvalues: {np.sort(ref_evals[ref_evals > 1e-6])}")
    print(f"  Match: {np.allclose(np.sort(pos_omega), np.sort(ref_evals[ref_evals > 1e-6]))}")

    # Now examine the eigenvector structure of Omega
    # Omega is a 16x16 matrix. Its eigenvectors are spinors.
    # The Clifford algebra Cliff(R^8) has a natural decomposition under
    # the U(2) subalgebra.
    #
    # The key question: why does B2 not mix with B1/B3?
    # B1 is 1-fold, B2 is 4-fold, B3 is 3-fold.
    # When we perturb the metric, we change Omega. The B1 and B3 eigenstates
    # can mix because they span a subspace that is invariant under some
    # residual symmetry. B2's 4-fold degeneracy comes from a different
    # representation of the residual symmetry group.

    # Build the K_7 operator in spinor space
    # K_7 = sum_a E_{7a} * (something) -- but wait, in the singlet K_7 = rho(e_7) = 0
    # The relevant operator is gamma_7 in the Clifford algebra
    # or more precisely, the commutator [gamma_7, Omega]

    gamma_7 = gammas[6]  # 0-indexed: gammas[6] = gamma_7
    gamma_8 = gammas[7]  # gammas[7] = gamma_8

    # Check: does gamma_7 commute with Omega at Jensen?
    comm_g7 = gamma_7 @ iOmega - iOmega @ gamma_7
    comm_g8 = gamma_8 @ iOmega - iOmega @ gamma_8
    print(f"\n  ||[gamma_7, iOmega]|| = {np.max(np.abs(comm_g7)):.2e}")
    print(f"  ||[gamma_8, iOmega]|| = {np.max(np.abs(comm_g8)):.2e}")

    # Check: what about gamma_7 * gamma_8 (the u(1) generator in spinor space)?
    K7_spinor = -0.5j * gamma_7 @ gamma_8  # Spinor version of K_7
    comm_K7 = K7_spinor @ iOmega - iOmega @ K7_spinor
    print(f"  ||[K_7^spinor, iOmega]|| = {np.max(np.abs(comm_K7)):.2e}")

    # Eigenvalues of K_7^spinor
    K7_evals = np.sort(np.linalg.eigvalsh(K7_spinor))
    print(f"  K_7^spinor eigenvalues: {K7_evals}")

    # What are the K_7^spinor eigenvalues of the B1, B2, B3 eigenstates?
    omega_evals_full, omega_evecs_full = np.linalg.eigh(iOmega)
    pos_idx = np.where(omega_evals_full > 1e-6)[0]
    pos_sorted = np.argsort(omega_evals_full[pos_idx])

    print(f"\n  K_7^spinor expectation in each B eigenvector:")
    for k, idx in enumerate(pos_idx[pos_sorted]):
        v = omega_evecs_full[:, idx]
        k7_exp = np.real(v.conj() @ K7_spinor @ v)
        ev = omega_evals_full[idx]
        sector = "B1" if k == 0 else ("B2" if k <= 4 else "B3")
        print(f"    Mode {k} ({sector}): eigenvalue={ev:.6f}, <K_7>={k7_exp:.6f}")

    # ==========================================
    # ANALYSIS 2: sin2_13 vs split parameter
    # ==========================================
    print("\n" + "=" * 72)
    print("ANALYSIS 2: sin^2(theta_13) vs C^2 SPLIT PARAMETER")
    print("=" * 72)

    s = tau_ref
    L1_J = np.exp(2*s)
    L2_J = np.exp(-2*s)
    L3_J = np.exp(s)

    # Scan split from 0 to 0.5
    splits = np.concatenate([
        np.linspace(0, 0.05, 11),
        np.linspace(0.06, 0.15, 10),
        np.linspace(0.20, 0.50, 7)
    ])

    sin2_13_vs_split = []
    R_vs_split = []
    print(f"\n  {'split':>8s} {'sin2_13':>10s} {'R':>10s}")
    print(f"  {'-'*30}")

    for split in splits:
        L3a = L3_J * (1 + split)
        L3b = L3_J * (1 - split)
        scales = np.array([L2_J]*3 + [L3a, L3a, L3b, L3b] + [L1_J])
        g_off = general_metric(B_ab, scales)

        _, evecs_off = compute_spectrum(g_off, gens, f_abc, gammas, irreps_data, return_evecs=True)
        off_evals = evecs_off[(0,0)][0]
        off_evecs = evecs_off[(0,0)][1]

        O, _, info = compute_singlet_overlap(ref_evecs, off_evecs, ref_evals, off_evals)
        if O is not None:
            sin2_12, sin2_13, sin2_23, _ = extract_pmns_angles(O)
            pos_off = sorted(off_evals[off_evals > 1e-6])
            if len(pos_off) >= 6:
                denom = pos_off[1]**2 - pos_off[0]**2
                R = (pos_off[5]**2 - pos_off[1]**2) / denom if denom > 1e-12 else float('inf')
            else:
                R = float('nan')
            sin2_13_vs_split.append(sin2_13)
            R_vs_split.append(R)
            print(f"  {split:>8.4f} {sin2_13:>10.6f} {R:>10.2f}")
        else:
            sin2_13_vs_split.append(np.nan)
            R_vs_split.append(np.nan)

    sin2_13_vs_split = np.array(sin2_13_vs_split)
    R_vs_split = np.array(R_vs_split)

    # Find split that gives sin2_13 = 0.0222
    target_sin2_13 = 0.02225  # (local)
    # Interpolate
    valid = ~np.isnan(sin2_13_vs_split) & (sin2_13_vs_split > 0)
    if np.any(valid) and np.max(sin2_13_vs_split[valid]) > target_sin2_13:
        from scipy.interpolate import interp1d
        f_interp = interp1d(sin2_13_vs_split[valid], splits[valid])
        split_target = float(f_interp(target_sin2_13))
        R_at_target = float(interp1d(splits[valid], R_vs_split[valid])(split_target))
        print(f"\n  Split for sin^2(theta_13) = {target_sin2_13}: {split_target:.4f}")
        print(f"  R at that split: {R_at_target:.2f}")
        print(f"  Required R: 33.8")
        print(f"  R deficit: {R_at_target/33.8:.4f}")
    else:
        split_target = None
        print(f"\n  Could not find split matching sin2_13 = {target_sin2_13}")

    # ==========================================
    # ANALYSIS 3: tau scan with fixed C^2 split
    # ==========================================
    print("\n" + "=" * 72)
    print("ANALYSIS 3: R AND sin^2(theta_13) vs TAU (fixed split)")
    print("=" * 72)

    # Use the split that gives sin2_13 ~ 0.022 (or 0.10 if not found)
    fixed_split = split_target if split_target is not None else 0.10

    taus = np.linspace(0.05, 0.30, 26)
    R_vs_tau = []
    sin2_13_vs_tau = []

    print(f"\n  Fixed C^2 split = {fixed_split:.4f}")
    print(f"  {'tau':>8s} {'sin2_13':>10s} {'R':>10s}")
    print(f"  {'-'*30}")

    for tau in taus:
        s_t = tau
        L1_t = np.exp(2*s_t)
        L2_t = np.exp(-2*s_t)
        L3_t = np.exp(s_t)
        L3a = L3_t * (1 + fixed_split)
        L3b = L3_t * (1 - fixed_split)
        scales = np.array([L2_t]*3 + [L3a, L3a, L3b, L3b] + [L1_t])
        g_off = general_metric(B_ab, scales)

        # Need Jensen reference at each tau for overlap
        g_ref_t = jensen_metric(B_ab, tau)
        _, evecs_ref_t = compute_spectrum(g_ref_t, gens, f_abc, gammas, irreps_data, return_evecs=True)
        _, evecs_off_t = compute_spectrum(g_off, gens, f_abc, gammas, irreps_data, return_evecs=True)

        ref_ev_t = evecs_ref_t[(0,0)][0]
        ref_vec_t = evecs_ref_t[(0,0)][1]
        off_ev_t = evecs_off_t[(0,0)][0]
        off_vec_t = evecs_off_t[(0,0)][1]

        O, _, info = compute_singlet_overlap(ref_vec_t, off_vec_t, ref_ev_t, off_ev_t)
        if O is not None:
            _, sin2_13, _, _ = extract_pmns_angles(O)
            pos_off = sorted(off_ev_t[off_ev_t > 1e-6])
            if len(pos_off) >= 6:
                denom = pos_off[1]**2 - pos_off[0]**2
                R = (pos_off[5]**2 - pos_off[1]**2) / denom if denom > 1e-12 else float('inf')
            else:
                R = float('nan')
        else:
            sin2_13 = np.nan
            R = np.nan

        R_vs_tau.append(R)
        sin2_13_vs_tau.append(sin2_13)
        R_str = f"{R:.2f}" if not np.isinf(R) and not np.isnan(R) else str(R)
        print(f"  {tau:>8.4f} {sin2_13:>10.6f} {R_str:>10s}")

    R_vs_tau = np.array(R_vs_tau)
    sin2_13_vs_tau = np.array(sin2_13_vs_tau)

    # ==========================================
    # ANALYSIS 4: WHY sin2_12 = 0 EXACTLY
    # ==========================================
    print("\n" + "=" * 72)
    print("ANALYSIS 4: WHY sin^2(theta_12) = 0 EXACTLY")
    print("=" * 72)

    # The overlap matrix pattern is:
    #   [a  0  b]     B1 mixes with B3 only
    #   [0  c  0]     B2 doesn't mix at all
    #   [d  0  e]     B3 mixes with B1 only
    #
    # This means the 3x3 PMNS is block-diagonal: 2x2 (B1,B3) + 1x1 (B2)
    #
    # sin2_12 = O[0,1] / (1 - O[0,2]) = 0 because O[0,1] = 0 always
    # sin2_23 = O[1,2] / (1 - O[0,2]) = 0 because O[1,2] = 0 always
    #
    # The physical reason: B2 has different quantum numbers from B1 and B3
    # that survive ALL tested perturbations.
    #
    # In the singlet (0,0), D = Omega = (1/4) sum Gamma^b_{ac} gamma_a gamma_b gamma_c
    # The 16x16 spinor space decomposes under the Clifford algebra.
    # The C^2 split preserves the su(2) subalgebra (generators 0,1,2), and the
    # B2 eigenspace transforms as a doublet under this su(2).
    # B1 and B3 are both su(2)-singlets (or triplet).
    #
    # Let's verify: compute the su(2) Casimir on each eigenstate

    # su(2) Casimir in spinor space: C_su2 = (1/4)(gamma_1 gamma_2)^2 + ... = ...
    # Actually, the relevant symmetry is the su(2) subalgebra of Cliff(R^8) generated by
    # gamma_1*gamma_2, gamma_1*gamma_3, gamma_2*gamma_3 (or similar).

    # Let's just compute what group acts on the B2 eigenspace
    # The B2 eigenstates have 4-fold degeneracy. Under what symmetry?

    # Check: does gamma_{1,2} = (i/2)*gamma_1*gamma_2 commute with Omega?
    Sigma_12 = 0.5j * gammas[0] @ gammas[1]  # sigma_12 in spinor space
    Sigma_34 = 0.5j * gammas[2] @ gammas[3]  # C^2 pair 1
    Sigma_56 = 0.5j * gammas[4] @ gammas[5]  # C^2 pair 2

    comm_S12 = Sigma_12 @ iOmega - iOmega @ Sigma_12
    comm_S34 = Sigma_34 @ iOmega - iOmega @ Sigma_34
    comm_S56 = Sigma_56 @ iOmega - iOmega @ Sigma_56

    print(f"\n  Commutator norms with iOmega (Jensen):")
    print(f"    ||[Sigma_12, iOmega]|| = {np.max(np.abs(comm_S12)):.2e} (su(2) generators)")
    print(f"    ||[Sigma_34, iOmega]|| = {np.max(np.abs(comm_S34)):.2e} (C^2 pair 1)")
    print(f"    ||[Sigma_56, iOmega]|| = {np.max(np.abs(comm_S56)):.2e} (C^2 pair 2)")

    # Check at a C^2-split metric
    L3a = L3_J * 1.1
    L3b = L3_J * 0.9
    scales_split = np.array([L2_J]*3 + [L3a, L3a, L3b, L3b] + [L1_J])
    g_split = general_metric(B_ab, scales_split)
    E_split = orthonormal_frame(g_split)
    ft_split = frame_structure_constants(f_abc, E_split)
    Gamma_split = connection_coefficients(ft_split)
    Omega_split = spinor_connection_offset(Gamma_split, gammas)
    iOmega_split = -1j * Omega_split

    comm_S12_split = Sigma_12 @ iOmega_split - iOmega_split @ Sigma_12
    comm_S34_split = Sigma_34 @ iOmega_split - iOmega_split @ Sigma_34
    comm_S56_split = Sigma_56 @ iOmega_split - iOmega_split @ Sigma_56

    print(f"\n  Commutator norms with iOmega (C^2 split 10%):")
    print(f"    ||[Sigma_12, iOmega]|| = {np.max(np.abs(comm_S12_split)):.2e} (su(2) generators)")
    print(f"    ||[Sigma_34, iOmega]|| = {np.max(np.abs(comm_S34_split)):.2e} (C^2 pair 1)")
    print(f"    ||[Sigma_56, iOmega]|| = {np.max(np.abs(comm_S56_split)):.2e} (C^2 pair 2)")

    # Check su(2) Casimir of each B-eigenstate
    C_su2_spinor = (gammas[0]@gammas[1]@gammas[0]@gammas[1] +
                    gammas[0]@gammas[2]@gammas[0]@gammas[2] +
                    gammas[1]@gammas[2]@gammas[1]@gammas[2]) * (-0.25)

    print(f"\n  su(2) Casimir eigenvalues of B-eigenstates (Jensen):")
    for k, idx in enumerate(pos_idx[pos_sorted]):
        v = omega_evecs_full[:, idx]
        c2_exp = np.real(v.conj() @ C_su2_spinor @ v)
        ev = omega_evals_full[idx]
        sector = "B1" if k == 0 else ("B2" if k <= 4 else "B3")
        print(f"    Mode {k} ({sector}): eigenvalue={ev:.6f}, <C_su2>={c2_exp:.6f}")

    # ==========================================
    # SAVE SUPPLEMENTARY DATA
    # ==========================================
    print("\n" + "=" * 72)
    print("SAVING SUPPLEMENTARY DATA")
    print("=" * 72)

    np.savez("computations/session-52/s52_offjensen_pmns_supp.npz",
        splits=splits,
        sin2_13_vs_split=sin2_13_vs_split,
        R_vs_split=R_vs_split,
        split_target_sin2_13=split_target if split_target is not None else np.nan,
        taus=taus,
        R_vs_tau=R_vs_tau,
        sin2_13_vs_tau=sin2_13_vs_tau,
        fixed_split=fixed_split,
    )
    print("  Saved supplementary data to s52_offjensen_pmns_supp.npz")

    # ==========================================
    # SUPPLEMENTARY PLOT
    # ==========================================
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('OFFJENSEN-PMNS-52 Supplementary Analysis', fontsize=13, fontweight='bold')

    # Panel 1: sin2_13 vs split
    ax = axes[0]
    valid_s = ~np.isnan(sin2_13_vs_split) & (sin2_13_vs_split > 0)
    if np.any(valid_s):
        ax.plot(splits[valid_s], sin2_13_vs_split[valid_s], 'o-', markersize=4)
        ax.axhline(0.02225, color='red', ls='--', label=r'NuFit $\sin^2\theta_{13}=0.0222$')
        if split_target is not None:
            ax.axvline(split_target, color='green', ls=':', label=f'split={split_target:.4f}')
        ax.set_xlabel('C^2 split parameter')
        ax.set_ylabel(r'$\sin^2\theta_{13}$')
        ax.set_title(r'$\sin^2\theta_{13}$ vs C$^2$ split')
        ax.legend(fontsize=8)
        ax.set_yscale('log')
        ax.set_ylim(bottom=1e-6)

    # Panel 2: R vs split
    ax = axes[1]
    valid_r = ~np.isnan(R_vs_split) & ~np.isinf(R_vs_split)
    if np.any(valid_r):
        ax.plot(splits[valid_r], R_vs_split[valid_r], 's-', markersize=4, color='steelblue')
        ax.axhline(33.8, color='red', ls='--', label='Target R=33.8')
        if split_target is not None:
            ax.axvline(split_target, color='green', ls=':', label=f'split={split_target:.4f}')
        ax.set_xlabel('C^2 split parameter')
        ax.set_ylabel('R')
        ax.set_title('Mass ratio R vs C$^2$ split')
        ax.legend(fontsize=8)

    # Panel 3: R vs tau at fixed split
    ax = axes[2]
    valid_rt = ~np.isnan(R_vs_tau) & ~np.isinf(R_vs_tau)
    if np.any(valid_rt):
        ax.plot(taus[valid_rt], R_vs_tau[valid_rt], 'o-', markersize=4, color='darkred')
        ax.axhline(33.8, color='red', ls='--', label='Target R=33.8')
        ax.axvline(0.19, color='gray', ls=':', alpha=0.5, label='fold')
        ax.set_xlabel(r'$\tau$')
        ax.set_ylabel('R')
        ax.set_title(f'R vs $\\tau$ (C$^2$ split={fixed_split:.4f})')
        ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig("computations/session-52/s52_offjensen_pmns_supp.png", dpi=150, bbox_inches='tight')
    print("  Saved supplementary plot")

    elapsed = time.time() - t_start
    print(f"\n  Total time: {elapsed:.1f} s")
    print("  ANALYSIS COMPLETE")


if __name__ == "__main__":
    main()
