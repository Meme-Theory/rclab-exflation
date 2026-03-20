#!/usr/bin/env python3
"""
Session 35 Task SECT-B2-35: Multi-Sector B2 Spectrum at (1,0) Sector.

Computes the full Dirac spectrum of D_K in the (1,0) Peter-Weyl sector at
9 tau values in [0.00, 0.50]. Identifies the B2-like branch by eigenvalue
tracking. Determines if a fold (v=0) exists in [0.15, 0.25]. If yes,
computes the Kosmann matrix elements V((1,0)_B2, (0,0)_B2) for the
cross-sector pairing.

Mathematical setup:
    In the (1,0) sector, dim(rho) = 3, so D_pi is a 48x48 matrix:
        D_pi = sum_{a,b} E_{ab} (rho_{(1,0)}(X_b) x gamma_a) + I_3 x Omega

    The spectrum is +/- symmetric (D anticommutes with gamma_9), giving
    24 positive eigenvalues. At tau=0, these group into degeneracy clusters
    that split under the Jensen deformation.

    The "B2-like" branch is identified by:
    (a) Having 4-fold degeneracy in the singlet that splits analogously
    (b) Having a minimum (fold) near tau ~ 0.19

    For the (1,0) sector, we expect a Casimir-shifted analog with a fold
    at a nearby tau value (SECT-33a showed delta_tau < 0.004).

Cross-sector Kosmann:
    The Kosmann operator K_a acts on spinor indices only (I_dim x K_a in
    the product space). Cross-sector matrix elements are:
        V_cross = sum_a |<psi_{(1,0)}|K_a|psi_{(0,0)}>|^2
    But since D_K is EXACTLY block-diagonal in Peter-Weyl (proven Session 22b),
    the Kosmann Lie derivative L_{K_a} also respects this decomposition IF
    K_a commutes with the left regular representation. However, K_a acts on
    spinor indices only within each sector. Cross-sector pairing requires
    the BCS interaction to couple different Peter-Weyl sectors, which
    depends on the structure of the Kosmann operator in the FULL Hilbert
    space.

    Key point: K_a = -(1/8) sum_{r,s} A^a_{rs} gamma_r gamma_s is a PURE
    SPINOR operator. In the product space V_pi x S, K_a = I_{dim_pi} x K_a.
    The cross-sector matrix element <(1,0),n|K_a|(0,0),m> = 0 because the
    representation spaces V_{(1,0)} and V_{(0,0)} are orthogonal in the
    Peter-Weyl decomposition. The BCS interaction V = sum_a K_a^dag K_a
    cannot couple different sectors.

    Therefore: the question is whether the (1,0) sector has its OWN fold
    and its OWN BCS instability with its OWN V matrix elements, contributing
    additional independent channels to N_eff.

Gate: SECT-B2-35 (INFORMATIVE)
    If fold exists in (1,0) AND intra-sector V((1,0)_B2,(1,0)_B2) > 0.01
    -> sector contributes independently to N_eff.

Author: baptista-spacetime-analyst (Session 35)
Date: 2026-03-07
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    validate_connection,
    dirac_operator_on_irrep,
    get_irrep,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)

from s23a_kosmann_singlet import kosmann_operator_antisymmetric


# ─────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────

TAU_VALUES = np.array([0.00, 0.06, 0.12, 0.18, 0.24, 0.30, 0.36, 0.42, 0.50])
FOLD_SEARCH_RANGE = (0.10, 0.35)  # wider than [0.15, 0.25] for safety
TAU_FINE = np.linspace(0.01, 0.55, 10000)


def compute_sector_spectrum(tau, gens, f_abc, gammas, p, q):
    """
    Compute D_K eigensystem in sector (p,q) at given tau.

    Returns:
        evals: real eigenvalues of (1j * D_pi), sorted ascending
        evecs: unitary matrix, columns = eigenvectors
        Gamma: connection coefficients
        Omega: spinor curvature offset
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    if (p, q) == (0, 0):
        D_pi = Omega.copy()
    else:
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

    # Verify anti-Hermiticity
    ah_err = np.max(np.abs(D_pi + D_pi.conj().T))

    # Diagonalize via Hermitian problem
    H = 1j * D_pi
    evals, evecs = eigh(H)

    return evals, evecs, Gamma, Omega, ah_err, D_pi


def get_positive_tracks(all_evals, n_tau):
    """Extract sorted positive eigenvalue tracks."""
    tracks = []
    for ti in range(n_tau):
        pos = np.sort(all_evals[ti][all_evals[ti] > 1e-10])
        tracks.append(pos)
    n_pos = min(len(t) for t in tracks)
    arr = np.zeros((n_tau, n_pos))
    for ti in range(n_tau):
        arr[ti, :] = tracks[ti][:n_pos]
    return arr


def find_track_minima(tau_vals, traj, tau_range=(0.10, 0.35)):
    """Find all interior minima of a trajectory in tau_range using cubic spline."""
    cs = CubicSpline(tau_vals, traj)
    tf = TAU_FINE[(TAU_FINE >= tau_range[0]) & (TAU_FINE <= tau_range[1])]
    if len(tf) < 3:
        return []
    deriv = cs(tf, 1)
    sign_changes = np.where(np.diff(np.sign(deriv)))[0]
    minima = []
    for sc in sign_changes:
        try:
            tm = brentq(lambda t: cs(t, 1), tf[sc], tf[sc + 1])
            d2 = cs(tm, 2)
            if d2 > 0:
                minima.append({
                    'tau_min': tm,
                    'lambda_min': float(cs(tm)),
                    'd2': float(d2),
                    'velocity_at_min': float(cs(tm, 1)),
                })
        except Exception:
            pass
    return minima


def compute_intra_sector_kosmann(evecs_sector, Gamma, gammas, dim_rho):
    """
    Compute intra-sector Kosmann matrix elements V(B2, B2) within the (p,q) sector.

    K_a acts as I_{dim_rho} x K_a^{spinor} in the product space.
    The matrix element <n|K_a|m> = evecs^dag @ (I x K_a) @ evecs.

    Returns:
        V_matrix: (N,N) matrix V_{nm} = sum_a |<n|K_a|m>|^2
        K_norms: (8,) Frobenius norms of K_a in eigenbasis
    """
    n_states = evecs_sector.shape[0]
    V = np.zeros((n_states, n_states), dtype=np.float64)
    K_norms = np.zeros(8)

    for a in range(8):
        K_a_spinor, _ = kosmann_operator_antisymmetric(Gamma, gammas, a)
        # Embed in product space: I_{dim_rho} x K_a_spinor
        K_a_full = np.kron(np.eye(dim_rho), K_a_spinor)
        # Project into eigenbasis
        K_eig = evecs_sector.conj().T @ K_a_full @ evecs_sector
        V += np.abs(K_eig) ** 2
        K_norms[a] = np.sqrt(np.sum(np.abs(K_eig) ** 2))

    return V, K_norms


def main():
    print("=" * 70)
    print("SECT-B2-35: Multi-Sector B2 Spectrum at (1,0) Sector")
    print("=" * 70)
    print(f"Tau values: {TAU_VALUES}")
    print(f"Fold search range: {FOLD_SEARCH_RANGE}")
    print()

    # Initialize infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 1: Compute (1,0) sector spectrum at all tau values
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 1: (1,0) SECTOR SPECTRUM")
    print("=" * 70)

    evals_10 = []
    evecs_10 = []
    Gammas = []
    Omegas = []

    for idx, tau in enumerate(TAU_VALUES):
        t0 = time.time()
        evals, evecs, Gamma, Omega, ah_err, D_pi = compute_sector_spectrum(
            tau, gens, f_abc, gammas, 1, 0
        )
        evals_10.append(evals)
        evecs_10.append(evecs)
        Gammas.append(Gamma)
        Omegas.append(Omega)

        pos = evals[evals > 1e-10]
        dt = time.time() - t0
        print(f"  tau={tau:.2f}: {len(evals)} evals, {len(pos)} positive, "
              f"ah_err={ah_err:.2e}, time={dt:.2f}s")
        print(f"    |lambda| range: [{np.min(np.abs(evals)):.6f}, {np.max(np.abs(evals)):.6f}]")

    # ═══════════════════════════════════════════════════════════════
    # STEP 2: Compute (0,0) singlet for reference
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 2: (0,0) SINGLET REFERENCE")
    print("=" * 70)

    evals_00 = []
    evecs_00 = []

    for idx, tau in enumerate(TAU_VALUES):
        evals, evecs, _, _, ah_err, _ = compute_sector_spectrum(
            tau, gens, f_abc, gammas, 0, 0
        )
        evals_00.append(evals)
        evecs_00.append(evecs)
        pos = np.sort(evals[evals > 1e-10])
        print(f"  tau={tau:.2f}: pos eigenvalues: {pos[:8]}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 3: Track positive eigenvalue branches
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 3: EIGENVALUE BRANCH TRACKING")
    print("=" * 70)

    tracks_10 = get_positive_tracks(evals_10, len(TAU_VALUES))
    tracks_00 = get_positive_tracks(evals_00, len(TAU_VALUES))
    n_tracks_10 = tracks_10.shape[1]
    n_tracks_00 = tracks_00.shape[1]

    print(f"(1,0): {n_tracks_10} positive tracks")
    print(f"(0,0): {n_tracks_00} positive tracks")

    # Degeneracy structure at tau=0
    e0_10 = tracks_10[0, :]
    groups_10 = []
    i = 0
    while i < len(e0_10):
        val = e0_10[i]
        cnt = 1
        while i + cnt < len(e0_10) and abs(e0_10[i + cnt] - val) < 1e-4:
            cnt += 1
        groups_10.append((i, cnt, val))
        i += cnt
    print(f"\n(1,0) degeneracy groups at tau=0:")
    for start, cnt, val in groups_10:
        print(f"  tracks [{start}:{start+cnt}], deg={cnt}, lambda={val:.6f}")

    e0_00 = tracks_00[0, :]
    groups_00 = []
    i = 0
    while i < len(e0_00):
        val = e0_00[i]
        cnt = 1
        while i + cnt < len(e0_00) and abs(e0_00[i + cnt] - val) < 1e-4:
            cnt += 1
        groups_00.append((i, cnt, val))
        i += cnt
    print(f"\n(0,0) degeneracy groups at tau=0:")
    for start, cnt, val in groups_00:
        print(f"  tracks [{start}:{start+cnt}], deg={cnt}, lambda={val:.6f}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 4: Find folds (v=0) in each track
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 4: FOLD SEARCH IN (1,0) SECTOR")
    print("=" * 70)

    all_minima_10 = []
    for j in range(n_tracks_10):
        mins = find_track_minima(TAU_VALUES, tracks_10[:, j], FOLD_SEARCH_RANGE)
        for m in mins:
            m['track'] = j
            # Identify which degeneracy group
            for start, cnt, val0 in groups_10:
                if start <= j < start + cnt:
                    m['group_start'] = start
                    m['group_deg'] = cnt
                    m['group_val0'] = val0
                    break
            all_minima_10.append(m)

    all_minima_10.sort(key=lambda m: m['tau_min'])

    if all_minima_10:
        print(f"Found {len(all_minima_10)} minima in (1,0) sector:")
        for m in all_minima_10:
            print(f"  track {m['track']:2d} (group deg={m['group_deg']}): "
                  f"tau_min={m['tau_min']:.5f}, lambda_min={m['lambda_min']:.7f}, "
                  f"d2={m['d2']:.4f}")
    else:
        print("NO minima found in (1,0) sector within search range!")

    # Reference: (0,0) B2 fold
    # B2 in singlet: tracks 1-4 (4-fold degenerate)
    b2_centroid_00 = tracks_00[:, 1:5].mean(axis=1) if n_tracks_00 >= 5 else tracks_00[:, 0]
    b2_min_00 = find_track_minima(TAU_VALUES, b2_centroid_00, FOLD_SEARCH_RANGE)
    if b2_min_00:
        tau_ref = b2_min_00[0]['tau_min']
        print(f"\n(0,0) B2 reference fold: tau_min={tau_ref:.5f}, "
              f"lambda_min={b2_min_00[0]['lambda_min']:.7f}")
    else:
        print("\nWARNING: no B2 fold found in (0,0) singlet!")
        tau_ref = 0.190

    # Identify which (1,0) minima are B2-analogs (close to tau_ref)
    b2_analog_10 = [m for m in all_minima_10 if abs(m['tau_min'] - tau_ref) < 0.05]
    if b2_analog_10:
        print(f"\n(1,0) B2-analogs (|delta_tau| < 0.05 from reference):")
        for m in b2_analog_10:
            dt = m['tau_min'] - tau_ref
            print(f"  track {m['track']}: tau_min={m['tau_min']:.5f} "
                  f"(delta_tau={dt:+.5f}), lambda={m['lambda_min']:.7f}, "
                  f"d2={m['d2']:.4f}, group_deg={m['group_deg']}")
    else:
        print("\nNO B2-analog folds found in (1,0) sector!")

    # Check if fold is within [0.15, 0.25]
    fold_in_target = [m for m in b2_analog_10 if 0.15 <= m['tau_min'] <= 0.25]
    fold_found = len(fold_in_target) > 0

    print(f"\nFold in [0.15, 0.25]: {'YES' if fold_found else 'NO'}")
    if fold_found:
        for m in fold_in_target:
            print(f"  track {m['track']}: tau_min={m['tau_min']:.5f}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 5: Compute intra-sector Kosmann V matrix at fold tau
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 5: INTRA-SECTOR KOSMANN V MATRIX AT FOLD")
    print("=" * 70)

    # Choose tau closest to fold for detailed analysis
    if fold_found:
        fold_tau = fold_in_target[0]['tau_min']
    elif b2_analog_10:
        fold_tau = b2_analog_10[0]['tau_min']
    else:
        fold_tau = 0.190  # fallback

    # Find the tau grid point nearest to the fold
    fold_idx = np.argmin(np.abs(TAU_VALUES - fold_tau))
    tau_at_fold = TAU_VALUES[fold_idx]
    print(f"Computing Kosmann at tau={tau_at_fold:.2f} (nearest grid point to fold at {fold_tau:.5f})")

    # Compute V matrix for (1,0) sector
    V_10, K_norms_10 = compute_intra_sector_kosmann(
        evecs_10[fold_idx], Gammas[fold_idx], gammas, dim_rho=3
    )

    # Identify B2-like modes (closest to fold eigenvalue)
    pos_evals = evals_10[fold_idx]
    pos_indices = np.where(pos_evals > 1e-10)[0]
    sorted_pos = pos_indices[np.argsort(pos_evals[pos_indices])]

    # The fold tracks correspond to the lowest positive eigenvalue group
    # At the fold, these are the modes with smallest |lambda|
    fold_track_indices = [m['track'] for m in (fold_in_target if fold_found else b2_analog_10[:4])]

    print(f"\nKosmann norms in (1,0) eigenbasis at tau={tau_at_fold:.2f}:")
    print(f"  C^2 directions (a=3,4,5,6): {K_norms_10[C2_IDX]}")
    print(f"  u(2) directions (a=0,1,2,7): {K_norms_10[U2_IDX]}")
    print(f"  Total C^2: {np.sqrt(np.sum(K_norms_10[C2_IDX]**2)):.6e}")

    # Extract V matrix in the B2-like subspace
    # The fold modes are in the lowest positive eigenvalue group
    # Use first few positive eigenvalue indices
    n_fold_modes = 6  # look at the lowest 6 positive modes
    b2_like_indices = sorted_pos[:n_fold_modes]
    V_b2_block = V_10[np.ix_(b2_like_indices, b2_like_indices)]

    print(f"\nV matrix (|K_a|^2 summed over all a=0..7) for lowest {n_fold_modes} positive modes:")
    print(f"  Indices: {b2_like_indices}")
    print(f"  Eigenvalues: {pos_evals[b2_like_indices]}")
    for i in range(n_fold_modes):
        row_str = "  ".join(f"{V_b2_block[i,j]:.4e}" for j in range(n_fold_modes))
        print(f"  [{i}]: {row_str}")

    # Max off-diagonal V in B2-like block
    offdiag_mask = ~np.eye(n_fold_modes, dtype=bool)
    V_offdiag_max = V_b2_block[offdiag_mask].max() if n_fold_modes > 1 else 0.0
    V_diag_max = np.max(np.diag(V_b2_block))

    print(f"\n  Max off-diagonal V(B2-like): {V_offdiag_max:.6e}")
    print(f"  Max diagonal V(B2-like): {V_diag_max:.6e}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 6: Compare with (0,0) singlet Kosmann
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 6: COMPARISON WITH (0,0) SINGLET KOSMANN")
    print("=" * 70)

    # Compute V matrix for (0,0) at same tau
    V_00, K_norms_00 = compute_intra_sector_kosmann(
        evecs_00[fold_idx], Gammas[fold_idx], gammas, dim_rho=1
    )

    # Singlet B2 modes: sorted positive modes 1-4
    pos_00 = evals_00[fold_idx]
    pos_idx_00 = np.where(pos_00 > 1e-10)[0]
    sorted_pos_00 = pos_idx_00[np.argsort(pos_00[pos_idx_00])]

    # B2 modes in singlet: indices 1-4 of sorted positive
    b2_singlet = sorted_pos_00[1:5] if len(sorted_pos_00) >= 5 else sorted_pos_00[:4]
    V_b2_00 = V_00[np.ix_(b2_singlet, b2_singlet)]

    V_offdiag_00 = V_b2_00[~np.eye(len(b2_singlet), dtype=bool)].max() if len(b2_singlet) > 1 else 0.0
    V_diag_00 = np.max(np.diag(V_b2_00)) if len(b2_singlet) > 0 else 0.0

    print(f"(0,0) singlet at tau={tau_at_fold:.2f}:")
    print(f"  Total C^2 K-norm: {np.sqrt(np.sum(K_norms_00[C2_IDX]**2)):.6e}")
    print(f"  B2 V off-diag max: {V_offdiag_00:.6e}")
    print(f"  B2 V diag max: {V_diag_00:.6e}")

    print(f"\n(1,0) sector at tau={tau_at_fold:.2f}:")
    print(f"  Total C^2 K-norm: {np.sqrt(np.sum(K_norms_10[C2_IDX]**2)):.6e}")
    print(f"  B2-like V off-diag max: {V_offdiag_max:.6e}")
    print(f"  B2-like V diag max: {V_diag_max:.6e}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 7: Group velocity analysis for all tracks
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 7: GROUP VELOCITY ANALYSIS")
    print("=" * 70)

    # For each track in (1,0), compute d(lambda)/d(tau) at the fold region
    print(f"\nTrack velocities at tau={tau_ref:.3f} (singlet B2 fold reference):")
    for j in range(min(n_tracks_10, 12)):
        cs = CubicSpline(TAU_VALUES, tracks_10[:, j])
        v = cs(tau_ref, 1)
        d2 = cs(tau_ref, 2)
        lam = cs(tau_ref)
        print(f"  track {j:2d}: lambda={lam:.6f}, v=d(lambda)/d(tau)={v:+.4f}, d2={d2:.4f}")

    # ═══════════════════════════════════════════════════════════════
    # STEP 8: Compute V at multiple tau for robustness
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("STEP 8: V MATRIX ACROSS TAU")
    print("=" * 70)

    V_offdiag_10_vs_tau = []
    V_offdiag_00_vs_tau = []

    for idx, tau in enumerate(TAU_VALUES):
        # (1,0) sector
        V_10_t, _ = compute_intra_sector_kosmann(
            evecs_10[idx], Gammas[idx], gammas, dim_rho=3
        )
        pos_evals_t = evals_10[idx]
        pi = np.where(pos_evals_t > 1e-10)[0]
        sp = pi[np.argsort(pos_evals_t[pi])]
        if len(sp) >= 6:
            block = V_10_t[np.ix_(sp[:6], sp[:6])]
            od = block[~np.eye(6, dtype=bool)].max()
        else:
            od = 0.0
        V_offdiag_10_vs_tau.append(od)

        # (0,0) singlet
        V_00_t, _ = compute_intra_sector_kosmann(
            evecs_00[idx], Gammas[idx], gammas, dim_rho=1
        )
        pe = evals_00[idx]
        pi2 = np.where(pe > 1e-10)[0]
        sp2 = pi2[np.argsort(pe[pi2])]
        if len(sp2) >= 5:
            b2_idx = sp2[1:5]
            block2 = V_00_t[np.ix_(b2_idx, b2_idx)]
            od2 = block2[~np.eye(len(b2_idx), dtype=bool)].max()
        else:
            od2 = 0.0
        V_offdiag_00_vs_tau.append(od2)

        print(f"  tau={tau:.2f}: V_offdiag_max(1,0)={od:.4e}, V_offdiag_max(0,0)={od2:.4e}")

    V_offdiag_10_vs_tau = np.array(V_offdiag_10_vs_tau)
    V_offdiag_00_vs_tau = np.array(V_offdiag_00_vs_tau)

    # ═══════════════════════════════════════════════════════════════
    # GATE EVALUATION
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("GATE EVALUATION: SECT-B2-35")
    print("=" * 70)

    # Criterion: fold in [0.15, 0.25] AND V_cross > 0.01
    # "V_cross" here is the intra-sector V for (1,0)
    if fold_found and V_offdiag_max > 0.01:
        gate_verdict = "PASS (contributes to N_eff)"
    elif fold_found and V_offdiag_max <= 0.01:
        gate_verdict = "FOLD EXISTS but V too small"
    else:
        gate_verdict = "NO FOLD in target range"

    print(f"\n  Fold in [0.15, 0.25]: {'YES' if fold_found else 'NO'}")
    if fold_found:
        print(f"  Fold tau: {fold_in_target[0]['tau_min']:.5f}")
        print(f"  Fold degeneracy: {fold_in_target[0].get('group_deg', '?')}")
    print(f"  V_offdiag_max at fold: {V_offdiag_max:.6e}")
    print(f"  Threshold: 0.01")
    print(f"\n  >>> SECT-B2-35 verdict: {gate_verdict} <<<")

    # Count contribution
    if fold_found:
        fold_deg = sum(1 for m in fold_in_target if abs(m['tau_min'] - fold_in_target[0]['tau_min']) < 0.005)
        pw_multiplicity = 3  # dim of (1,0) irrep
        # (0,1) is conjugate, same spectrum, contributes equally
        total_new_modes = fold_deg * 2  # (1,0) + (0,1) each contribute fold_deg modes
        print(f"\n  Fold modes in (1,0): {fold_deg}")
        print(f"  Conjugate (0,1): +{fold_deg} more (by conjugation symmetry)")
        print(f"  Total new fold modes from fundamental/anti-fundamental: {total_new_modes}")
        print(f"  Peter-Weyl multiplicity: {pw_multiplicity}^2 = {pw_multiplicity**2}")
        print(f"  N_eff contribution: {total_new_modes} modes x dim^2={pw_multiplicity**2} "
              f"= {total_new_modes * pw_multiplicity**2}")
    else:
        total_new_modes = 0

    # ═══════════════════════════════════════════════════════════════
    # SAVE DATA
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("SAVING DATA")
    print("=" * 70)

    save_data = {
        'tau_values': TAU_VALUES,
        'tau_ref_00': np.array([tau_ref]),
        'fold_found': np.array([fold_found]),
        'gate_verdict': np.array([gate_verdict]),
    }

    # Save eigenvalues at each tau
    for idx in range(len(TAU_VALUES)):
        save_data[f'evals_10_{idx}'] = evals_10[idx]
        save_data[f'evals_00_{idx}'] = evals_00[idx]

    # Save tracks
    save_data['tracks_10'] = tracks_10
    save_data['tracks_00'] = tracks_00

    # Save V data
    save_data['V_offdiag_10_vs_tau'] = V_offdiag_10_vs_tau
    save_data['V_offdiag_00_vs_tau'] = V_offdiag_00_vs_tau

    # Save fold info
    if fold_found:
        save_data['fold_tau'] = np.array([fold_in_target[0]['tau_min']])
        save_data['fold_lambda'] = np.array([fold_in_target[0]['lambda_min']])
        save_data['fold_d2'] = np.array([fold_in_target[0]['d2']])
        save_data['fold_deg'] = np.array([fold_deg])
        save_data['total_new_modes'] = np.array([total_new_modes])
    elif b2_analog_10:
        save_data['nearest_fold_tau'] = np.array([b2_analog_10[0]['tau_min']])
        save_data['nearest_fold_lambda'] = np.array([b2_analog_10[0]['lambda_min']])

    save_data['V_offdiag_max_at_fold'] = np.array([V_offdiag_max])

    output_path = os.path.join(SCRIPT_DIR, "s35_sector_10_spectrum.npz")
    np.savez_compressed(output_path, **save_data)
    print(f"Data saved: {output_path}")

    # ═══════════════════════════════════════════════════════════════
    # PLOT
    # ═══════════════════════════════════════════════════════════════
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # Panel 1: (0,0) singlet eigenvalue flow
    ax = axes[0, 0]
    for j in range(min(n_tracks_00, 8)):
        if j == 0:
            ax.plot(TAU_VALUES, tracks_00[:, j], 'o-', color='C0', ms=4, label='B1')
        elif j <= 4:
            lbl = 'B2 (4-fold)' if j == 1 else None
            ax.plot(TAU_VALUES, tracks_00[:, j], 'o-', color='C1', ms=4, label=lbl)
        else:
            lbl = 'B3 (3-fold)' if j == 5 else None
            ax.plot(TAU_VALUES, tracks_00[:, j], 'o-', color='C2', ms=4, label=lbl)
    ax.axvline(tau_ref, color='red', ls='--', alpha=0.7, label=f'B2 fold: {tau_ref:.3f}')
    ax.set_xlabel('tau')
    ax.set_ylabel('lambda')
    ax.set_title('(0,0) Singlet')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 2: (1,0) sector eigenvalue flow (ALL tracks)
    ax = axes[0, 1]
    cmap = plt.cm.tab20
    n_show = min(n_tracks_10, 16)
    for j in range(n_show):
        ax.plot(TAU_VALUES, tracks_10[:, j], 'o-', color=cmap(j / max(n_show, 1)),
                ms=3, label=f'trk {j}' if j < 8 else None)
    # Highlight fold tracks
    for m in (fold_in_target if fold_found else b2_analog_10[:4]):
        ax.plot(TAU_VALUES, tracks_10[:, m['track']], 'o-', color='red', ms=5, lw=2)
    ax.axvline(tau_ref, color='red', ls='--', alpha=0.7)
    ax.set_xlabel('tau')
    ax.set_ylabel('lambda')
    ax.set_title('(1,0) Sector (red = fold tracks)')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 3: Zoom on fold region
    ax = axes[0, 2]
    for j in range(min(n_tracks_10, 8)):
        cs = CubicSpline(TAU_VALUES, tracks_10[:, j])
        tf_zoom = np.linspace(0.10, 0.35, 500)
        ax.plot(tf_zoom, cs(tf_zoom), '-', color=cmap(j / 8), lw=1.5,
                label=f'trk {j}')
        ax.plot(TAU_VALUES, tracks_10[:, j], 'o', color=cmap(j / 8), ms=4)
    ax.axvline(tau_ref, color='red', ls='--', alpha=0.7, label='(0,0) B2 fold')
    # Mark found minima
    for m in all_minima_10:
        ax.plot(m['tau_min'], m['lambda_min'], '*', color='red', ms=12, zorder=10)
    ax.set_xlabel('tau')
    ax.set_ylabel('lambda')
    ax.set_title('(1,0) Fold Region Zoom')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.10, 0.35)

    # Panel 4: Group velocity d(lambda)/d(tau)
    ax = axes[1, 0]
    for j in range(min(n_tracks_10, 6)):
        cs = CubicSpline(TAU_VALUES, tracks_10[:, j])
        tf = np.linspace(0.05, 0.50, 500)
        ax.plot(tf, cs(tf, 1), '-', color=cmap(j / 6), lw=1.5, label=f'trk {j}')
    # Singlet B2 for reference
    cs_b2 = CubicSpline(TAU_VALUES, b2_centroid_00)
    ax.plot(tf, cs_b2(tf, 1), '--', color='blue', lw=2, label='(0,0) B2')
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(tau_ref, color='red', ls='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('d(lambda)/d(tau)')
    ax.set_title('Group Velocity')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-1.5, 1.5)

    # Panel 5: V_offdiag comparison across tau
    ax = axes[1, 1]
    ax.plot(TAU_VALUES, V_offdiag_10_vs_tau, 'o-', color='C1', lw=2, label='(1,0) V_offdiag')
    ax.plot(TAU_VALUES, V_offdiag_00_vs_tau, 's-', color='C0', lw=2, label='(0,0) V_offdiag')
    ax.axhline(0.01, color='red', ls=':', alpha=0.7, label='threshold 0.01')
    ax.axvline(tau_ref, color='red', ls='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('max V_offdiag')
    ax.set_title('Intra-Sector Kosmann V')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')

    # Panel 6: Degeneracy splitting
    ax = axes[1, 2]
    # Show how (1,0) tracks split from the tau=0 degenerate values
    for start, cnt, val0 in groups_10:
        for j in range(start, start + cnt):
            delta = tracks_10[:, j] - val0
            ax.plot(TAU_VALUES, delta, 'o-', color=cmap(start / n_tracks_10), ms=3,
                    label=f'group {val0:.4f}' if j == start else None)
    ax.set_xlabel('tau')
    ax.set_ylabel('lambda - lambda(tau=0)')
    ax.set_title('(1,0) Splitting from Round Metric')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='black', lw=0.5)

    verdict_str = gate_verdict
    fig.suptitle(f'SECT-B2-35: (1,0) Sector Spectrum | VERDICT: {verdict_str}',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plot_path = os.path.join(SCRIPT_DIR, "s35_sector_10_spectrum.png")
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"Plot saved: {plot_path}")

    # ═══════════════════════════════════════════════════════════════
    # FINAL SUMMARY
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("FINAL SUMMARY: SECT-B2-35")
    print("=" * 70)

    print(f"\n1. (1,0) sector has {n_tracks_10} positive eigenvalue tracks")
    print(f"   Degeneracy groups at tau=0: {[(cnt, f'{val:.6f}') for _,cnt,val in groups_10]}")
    print(f"2. (0,0) B2 fold reference: tau={tau_ref:.5f}")
    print(f"3. (1,0) folds found: {len(all_minima_10)}")
    for m in all_minima_10:
        print(f"   track {m['track']}: tau={m['tau_min']:.5f}, lambda={m['lambda_min']:.7f}")
    print(f"4. Fold in [0.15, 0.25]: {'YES' if fold_found else 'NO'}")
    if fold_found:
        print(f"   delta_tau from (0,0) reference: {abs(fold_in_target[0]['tau_min'] - tau_ref):.5f}")
    print(f"5. V_offdiag_max at fold: {V_offdiag_max:.6e}")
    print(f"6. Cross-sector V: IDENTICALLY ZERO (Peter-Weyl block-diagonal)")
    print(f"7. GATE: {gate_verdict}")

    return gate_verdict


if __name__ == "__main__":
    verdict = main()
