"""
Session 23a: Einstein-Theorist Formula-by-Formula Validation
============================================================
Independently verifies every numerical claim in the synthesis document.
"""
import sys
import os
import numpy as np
from scipy.linalg import eigh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    print("=" * 80)
    print("EINSTEIN-THEORIST: Independent Validation of Session 23a Synthesis")
    print("=" * 80)

    # ================================================================
    # LOAD ALL DATA
    # ================================================================
    gap_data = np.load(os.path.join(SCRIPT_DIR, "s23a_gap_equation.npz"), allow_pickle=True)
    kosmann_data = np.load(os.path.join(SCRIPT_DIR, "s23a_kosmann_singlet.npz"), allow_pickle=True)

    tau_values = gap_data['tau_values']
    print(f"\nTau values: {tau_values}")
    print(f"Gap data keys: {sorted(gap_data.files)[:20]}...")
    print(f"Kosmann data keys: {sorted(kosmann_data.files)[:20]}...")

    # ================================================================
    # VALIDATION 1: M_max = 0.077-0.149 range (BdG, parameter-free)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 1: M_max range (mu=0, full16 basis)")
    print("Synthesis claims: 0.077-0.149 (BdG)")
    print("=" * 80)

    # The synthesis table II.2 says BdG M_max range is 0.077-0.149
    # The results file says mu=0 M_max range is 0.077-0.155
    # Let me reconstruct both from scratch

    C2_IDX = [3, 4, 5, 6]

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']

        # Rebuild V matrix from K_a matrices
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        # Compare with stored V matrix
        V_stored = gap_data[f'V_matrix_{idx}']
        V_diff = np.max(np.abs(V - V_stored))

        # Classify modes
        abs_e = np.abs(evals)
        sorted_idx = np.argsort(abs_e)
        lambda_min = abs_e[sorted_idx[0]]

        # Method A: mu=0 linearized (from synthesis)
        xi_mu0 = evals - 0.0
        abs_xi_mu0 = np.maximum(np.abs(xi_mu0), 0.01 * lambda_min)
        M_mu0 = np.zeros((16, 16))
        for m in range(16):
            M_mu0[:, m] = V[:, m] / (2.0 * abs_xi_mu0[m])
        evals_M_mu0 = np.linalg.eigvalsh(M_mu0)
        M_max_mu0 = np.max(evals_M_mu0)

        # Method B: BdG (parameter-free) -- uses E_n + E_m in denominator
        # For positive-energy modes only
        pos_mask = evals > 0
        pos_evals = evals[pos_mask]
        V_pos = V[np.ix_(np.where(pos_mask)[0], np.where(pos_mask)[0])]
        N_pos = len(pos_evals)
        M_bdg = np.zeros((N_pos, N_pos))
        for n in range(N_pos):
            for m in range(N_pos):
                M_bdg[n, m] = V_pos[n, m] / (pos_evals[n] + pos_evals[m])
        evals_bdg = np.linalg.eigvalsh(M_bdg)
        M_max_bdg = np.max(evals_bdg)

        # Also check stored M_max values
        try:
            M_max_stored_mu0 = float(gap_data[f'M_max_full16_mu=0_{idx}'])
        except:
            M_max_stored_mu0 = -999

        print(f"  tau={tau:.2f}: M_max(mu=0)={M_max_mu0:.6f} [stored={M_max_stored_mu0:.6f}], "
              f"M_max(BdG+)={M_max_bdg:.6f}, V_diff={V_diff:.2e}, lambda_min={lambda_min:.6f}")

    # ================================================================
    # VALIDATION 2: V(gap,gap) = 0 EXACTLY
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 2: V(gap,gap) = 0 selection rule")
    print("Synthesis claims: EXACTLY zero at all tau > 0 (~10^{-29})")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']

        # Rebuild V
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)

        # Find gap-edge modes (two smallest |lambda|)
        abs_e = np.abs(evals)
        sorted_idx = np.argsort(abs_e)

        # Group by levels
        levels = []
        tol = 1e-4
        current_val = abs_e[sorted_idx[0]]
        current_group = [sorted_idx[0]]
        for i in range(1, len(sorted_idx)):
            if abs(abs_e[sorted_idx[i]] - current_val) < tol:
                current_group.append(sorted_idx[i])
            else:
                levels.append((current_val, np.array(current_group)))
                current_val = abs_e[sorted_idx[i]]
                current_group = [sorted_idx[i]]
        levels.append((current_val, np.array(current_group)))

        gap_idx = levels[0][1]
        V_gap = V[np.ix_(gap_idx, gap_idx)]
        max_gap_self = np.max(np.abs(V_gap))

        # Check individual K_a contributions to gap-gap coupling
        K_gap_components = []
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            K_gap = K[np.ix_(gap_idx, gap_idx)]
            K_gap_components.append(np.max(np.abs(K_gap)))

        if len(levels) > 1:
            near_idx = levels[1][1]
            V_gap_near = V[np.ix_(gap_idx, near_idx)]
            max_gap_near = np.max(np.abs(V_gap_near))
        else:
            max_gap_near = 0.0

        print(f"  tau={tau:.2f}: V(gap,gap)_max = {max_gap_self:.4e}, "
              f"V(gap,near)_max = {max_gap_near:.6f}, "
              f"|K_a(gap,gap)|_max = {K_gap_components}, "
              f"gap_deg = {len(gap_idx)}, levels = {len(levels)}")

        # Investigate WHY V(gap,gap)=0: check each K_a separately
        if tau > 0:
            for a in C2_IDX:
                K = kosmann_data[f'K_a_matrix_{idx}_{a}']
                K_gap = K[np.ix_(gap_idx, gap_idx)]
                # V contribution: |K_{nm}|^2
                V_a_gap = np.abs(K_gap)**2
                # Check: is K_{nm} itself zero between gap modes?
                print(f"    K_{a}(gap): |K[0,0]|={abs(K_gap[0,0]):.4e}, "
                      f"|K[0,1]|={abs(K_gap[0,1]):.4e}, "
                      f"|K[1,0]|={abs(K_gap[1,0]):.4e}, "
                      f"|K[1,1]|={abs(K_gap[1,1]):.4e}")
            break  # Only need one tau to see structure

    # ================================================================
    # VALIDATION 3: ||K_a|| norms (antisymmetric formula)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 3: Kosmann operator norms")
    print("Synthesis claims: ||K_a|| = 0.77-0.88 per C^2 direction, total 0.77-1.76")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        K_norms = kosmann_data[f'K_norms_{idx}']
        c2_norms = K_norms[C2_IDX]
        total_c2 = np.sqrt(np.sum(c2_norms**2))

        # Also get S_norms for comparison
        S_norms = kosmann_data[f'S_norms_{idx}']
        c2_S_norms = S_norms[C2_IDX]
        total_S = np.sqrt(np.sum(c2_S_norms**2))

        print(f"  tau={tau:.2f}: ||K|| per C2 = [{c2_norms[0]:.4f}, {c2_norms[1]:.4f}, "
              f"{c2_norms[2]:.4f}, {c2_norms[3]:.4f}], total = {total_c2:.4f}, "
              f"||S|| total = {total_S:.4f}")

    # ================================================================
    # VALIDATION 4: Spectral gap 2*lambda_min at tau=0.30
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 4: Spectral gap 2*lambda_min")
    print("Synthesis claims: 2*lambda_min ~ 1.644 at tau=0.30")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        abs_e = np.abs(evals)
        lambda_min = np.min(abs_e)
        spectral_gap = 2 * lambda_min
        print(f"  tau={tau:.2f}: lambda_min = {lambda_min:.6f}, 2*lambda_min = {spectral_gap:.6f}")

    # ================================================================
    # VALIDATION 5: V(gap,nearest) ~ 0.093 at tau=0.30
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 5: V(gap,nearest) coupling at tau=0.30")
    print("Synthesis claims: V ~ 0.093")
    print("=" * 80)

    idx_030 = 5  # tau=0.30
    evals = kosmann_data[f'eigenvalues_{idx_030}']
    V = np.zeros((16, 16))
    for a in C2_IDX:
        K = kosmann_data[f'K_a_matrix_{idx_030}_{a}']
        V += np.abs(K) ** 2
    V = np.real(V)
    V = 0.5 * (V + V.T)

    abs_e = np.abs(evals)
    sorted_idx = np.argsort(abs_e)

    # Level classification
    levels = []
    tol = 1e-4
    current_val = abs_e[sorted_idx[0]]
    current_group = [sorted_idx[0]]
    for i in range(1, len(sorted_idx)):
        if abs(abs_e[sorted_idx[i]] - current_val) < tol:
            current_group.append(sorted_idx[i])
        else:
            levels.append((current_val, np.array(current_group)))
            current_val = abs_e[sorted_idx[i]]
            current_group = [sorted_idx[i]]
    levels.append((current_val, np.array(current_group)))

    if len(levels) > 1:
        gap_idx = levels[0][1]
        near_idx = levels[1][1]
        V_gn = V[np.ix_(gap_idx, near_idx)]
        print(f"  V(gap,nearest) matrix at tau=0.30:")
        print(f"  Shape: {V_gn.shape}")
        print(f"  Max: {np.max(V_gn):.6f}")
        print(f"  Min: {np.min(V_gn):.6f}")
        print(f"  Mean: {np.mean(V_gn):.6f}")
        print(f"  Std: {np.std(V_gn):.6f}")
        print(f"  Full matrix:\n{V_gn}")

        # Check if "uniform across degenerate modes" as claimed
        print(f"\n  Level 1: val={levels[0][0]:.6f}, deg={len(gap_idx)}")
        print(f"  Level 2: val={levels[1][0]:.6f}, deg={len(near_idx)}")
        if len(levels) > 2:
            print(f"  Level 3: val={levels[2][0]:.6f}, deg={len(levels[2][1])}")

    # ================================================================
    # VALIDATION 6: Full V_nm matrix structure (selection rules)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 6: V_nm selection rules")
    print("Synthesis claims: V couples only between distinct levels, zero within")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        if tau == 0:
            continue  # All degenerate at tau=0

        evals = kosmann_data[f'eigenvalues_{idx}']
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        abs_e = np.abs(evals)
        sorted_idx_local = np.argsort(abs_e)

        levels_local = []
        tol = 1e-4
        current_val = abs_e[sorted_idx_local[0]]
        current_group = [sorted_idx_local[0]]
        for i in range(1, len(sorted_idx_local)):
            if abs(abs_e[sorted_idx_local[i]] - current_val) < tol:
                current_group.append(sorted_idx_local[i])
            else:
                levels_local.append((current_val, np.array(current_group)))
                current_val = abs_e[sorted_idx_local[i]]
                current_group = [sorted_idx_local[i]]
        levels_local.append((current_val, np.array(current_group)))

        if tau == 0.30:  # Detailed at tau=0.30
            print(f"\n  tau={tau:.2f}: {len(levels_local)} levels")
            for i, (val, grp) in enumerate(levels_local):
                for j, (val2, grp2) in enumerate(levels_local):
                    V_block = V[np.ix_(grp, grp2)]
                    max_val = np.max(np.abs(V_block))
                    print(f"    V(L{i+1}, L{j+1}): max|V| = {max_val:.6e}  "
                          f"(deg {len(grp)} x {len(grp2)}, "
                          f"|lam| = {val:.4f} x {val2:.4f})")

    # ================================================================
    # VALIDATION 7: Self-doping energy balance
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 7: Self-doping energy balance")
    print("Synthesis claims: Cost/Gain ratio at tau=0.30 is 0.06, at tau=0.50 is 0.16")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        lambda_min = np.min(np.abs(evals))
        cost = 2 * lambda_min  # Energy to promote across gap

        # Gain: |F_cond| at mu=lambda_min
        # Need to recompute from self-consistent gap
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        # Self-consistent iteration at mu=lambda_min
        mu = lambda_min
        xi = evals - mu
        Delta = np.ones(16) * 0.01 * lambda_min

        for k in range(50000):
            denom = 2.0 * np.sqrt(xi**2 + Delta**2)
            Delta_new = V @ (Delta / denom)
            if np.linalg.norm(Delta) > 1e-15:
                rel_change = np.linalg.norm(Delta_new - Delta) / np.linalg.norm(Delta)
            else:
                rel_change = np.linalg.norm(Delta_new - Delta)
            Delta = Delta_new
            if rel_change < 1e-12:
                break
            if np.linalg.norm(Delta) < 1e-30:
                break

        # Free energy
        F_kin = -np.sum(np.sqrt(xi**2 + Delta**2) - np.abs(xi))
        try:
            V_inv = np.linalg.inv(V)
            F_pot = 0.5 * Delta @ V_inv @ Delta
        except:
            V_pinv = np.linalg.pinv(V, rcond=1e-10)
            F_pot = 0.5 * Delta @ V_pinv @ Delta
        F_cond = F_kin + F_pot

        gain = abs(F_cond)
        ratio = gain / cost if cost > 0 else 0

        if tau in [0.30, 0.50]:
            print(f"  tau={tau:.2f}: cost=2*lam_min={cost:.4f}, gain=|F_cond|={gain:.4f}, "
                  f"ratio={ratio:.4f}")

    # ================================================================
    # VALIDATION 8: Ratio V/(2*lambda_min) ~ 0.057 at tau=0.30
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 8: V/(2*lambda_min) ratio")
    print("Synthesis Section VI.1 claims: V/(2*lambda_min) ~ 0.057")
    print("=" * 80)

    idx_030 = 5
    evals = kosmann_data[f'eigenvalues_{idx_030}']
    lambda_min = np.min(np.abs(evals))

    V = np.zeros((16, 16))
    for a in C2_IDX:
        K = kosmann_data[f'K_a_matrix_{idx_030}_{a}']
        V += np.abs(K) ** 2
    V = np.real(V)
    V = 0.5 * (V + V.T)

    abs_e = np.abs(evals)
    sorted_idx = np.argsort(abs_e)
    levels = []
    tol = 1e-4
    current_val = abs_e[sorted_idx[0]]
    current_group = [sorted_idx[0]]
    for i in range(1, len(sorted_idx)):
        if abs(abs_e[sorted_idx[i]] - current_val) < tol:
            current_group.append(sorted_idx[i])
        else:
            levels.append((current_val, np.array(current_group)))
            current_val = abs_e[sorted_idx[i]]
            current_group = [sorted_idx[i]]
    levels.append((current_val, np.array(current_group)))

    gap_idx = levels[0][1]
    near_idx = levels[1][1]
    V_gn_max = np.max(V[np.ix_(gap_idx, near_idx)])

    ratio_claim = V_gn_max / (2 * lambda_min)
    print(f"  V(gap,nearest) = {V_gn_max:.6f}")
    print(f"  2*lambda_min = {2*lambda_min:.6f}")
    print(f"  V/(2*lambda_min) = {ratio_claim:.6f}")
    print(f"  Synthesis claims 0.057. Factor of 18 too small.")
    print(f"  Computed factor = {1.0/ratio_claim:.1f}x")

    # ================================================================
    # VALIDATION 9: mu=+lambda_min M_max ~ 11 at tau=0.30
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 9: M_max at mu=+lambda_min (conditional PASS)")
    print("Synthesis claims: M_max ~ 11 at tau=0.30")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        lambda_min_local = np.min(np.abs(evals))

        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        mu = lambda_min_local
        xi = evals - mu
        abs_xi = np.maximum(np.abs(xi), 0.01 * lambda_min_local)
        M = np.zeros((16, 16))
        for m in range(16):
            M[:, m] = V[:, m] / (2.0 * abs_xi[m])
        evals_M = np.linalg.eigvalsh(M)
        M_max = np.max(evals_M)

        print(f"  tau={tau:.2f}: M_max(mu=+lmin) = {M_max:.4f}, lambda_min = {lambda_min_local:.6f}")

    # ================================================================
    # VALIDATION 10: Level degeneracies (2, 8, 6)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 10: Level degeneracies")
    print("Synthesis claims: 2, 8, 6 (gap-edge, nearest, highest)")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        abs_e = np.abs(evals)
        sorted_idx_local = np.argsort(abs_e)

        levels_local = []
        tol = 1e-4
        current_val = abs_e[sorted_idx_local[0]]
        current_group = [sorted_idx_local[0]]
        for i in range(1, len(sorted_idx_local)):
            if abs(abs_e[sorted_idx_local[i]] - current_val) < tol:
                current_group.append(sorted_idx_local[i])
            else:
                levels_local.append((current_val, np.array(current_group)))
                current_val = abs_e[sorted_idx_local[i]]
                current_group = [sorted_idx_local[i]]
        levels_local.append((current_val, np.array(current_group)))

        deg_str = ", ".join([f"L{i+1}:{len(g)}@{v:.4f}" for i, (v, g) in enumerate(levels_local)])
        print(f"  tau={tau:.2f}: {deg_str}")

    # ================================================================
    # VALIDATION 11: Factor below critical (synthesis Table II.2)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 11: Factor below critical (1/M_max)")
    print("Synthesis Table II.2 claims BdG factor 6.7-12.9x below critical")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        lambda_min_local = np.min(np.abs(evals))

        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        # mu=0 linearized
        xi_mu0 = evals
        abs_xi_mu0 = np.maximum(np.abs(xi_mu0), 0.01 * lambda_min_local)
        M_mu0 = np.zeros((16, 16))
        for m in range(16):
            M_mu0[:, m] = V[:, m] / (2.0 * abs_xi_mu0[m])
        M_max_mu0 = np.max(np.linalg.eigvalsh(M_mu0))
        factor_mu0 = 1.0 / M_max_mu0 if M_max_mu0 > 0 else float('inf')

        print(f"  tau={tau:.2f}: M_max(mu=0)={M_max_mu0:.6f}, factor={factor_mu0:.1f}x below")

    # ================================================================
    # VALIDATION 12: Antisymmetric tensor check (Kosmann formula)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 12: Antisymmetric tensor A_{rs}^a properties")
    print("Check: A_{rs} = -A_{sr} (antisymmetric)?")
    print("=" * 80)

    for idx, tau in enumerate([0.0, 0.15, 0.30]):
        tau_idx = list(tau_values).index(tau)
        for a in C2_IDX:
            A = kosmann_data[f'A_antisym_{tau_idx}_{a}']
            antisym_err = np.max(np.abs(A + A.T))
            frob_norm = np.sqrt(np.sum(A**2))
            print(f"  tau={tau:.2f}, a={a}: ||A+A^T||={antisym_err:.2e}, ||A||_F={frob_norm:.6f}")

    # ================================================================
    # VALIDATION 13: K_a anti-Hermiticity check
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 13: K_a Hermiticity properties in eigenbasis")
    print("Check: Is K_a Hermitian, anti-Hermitian, or mixed?")
    print("=" * 80)

    for idx, tau in enumerate([0.15, 0.30]):
        tau_idx = list(tau_values).index(tau)
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{tau_idx}_{a}']
            h_err = np.max(np.abs(K - K.conj().T))
            ah_err = np.max(np.abs(K + K.conj().T))
            print(f"  tau={tau:.2f}, a={a}: ||K-K^dag||={h_err:.4e}, ||K+K^dag||={ah_err:.4e}")

    # ================================================================
    # VALIDATION 14: Cross-check V matrix symmetry
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 14: V_nm = sum |<n|K_a|m>|^2 symmetry")
    print("V should be real, non-negative, and symmetric")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        V = np.zeros((16, 16), dtype=complex)
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2

        imag_max = np.max(np.abs(np.imag(V)))
        V_real = np.real(V)
        sym_err = np.max(np.abs(V_real - V_real.T))
        min_val = np.min(V_real)

        print(f"  tau={tau:.2f}: imag_max={imag_max:.2e}, sym_err={sym_err:.2e}, min_val={min_val:.4e}")

    # ================================================================
    # VALIDATION 15: Monotonic growth of coupling (Section III.3)
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 15: Monotonic growth of V(gap,nearest)")
    print("Synthesis claims: V grows from 0.070 (tau=0.10) to 0.131 (tau=0.50)")
    print("=" * 80)

    prev_V = 0
    monotonic = True
    for idx, tau in enumerate(tau_values):
        if tau == 0:
            continue

        evals = kosmann_data[f'eigenvalues_{idx}']
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        abs_e = np.abs(evals)
        sorted_idx_local = np.argsort(abs_e)

        levels_local = []
        tol = 1e-4
        current_val = abs_e[sorted_idx_local[0]]
        current_group = [sorted_idx_local[0]]
        for i in range(1, len(sorted_idx_local)):
            if abs(abs_e[sorted_idx_local[i]] - current_val) < tol:
                current_group.append(sorted_idx_local[i])
            else:
                levels_local.append((current_val, np.array(current_group)))
                current_val = abs_e[sorted_idx_local[i]]
                current_group = [sorted_idx_local[i]]
        levels_local.append((current_val, np.array(current_group)))

        gap_idx = levels_local[0][1]
        near_idx = levels_local[1][1]
        V_gn = np.max(V[np.ix_(gap_idx, near_idx)])

        if V_gn < prev_V and tau > 0.1:
            monotonic = False
        prev_V = V_gn

        print(f"  tau={tau:.2f}: V(gap,nearest) = {V_gn:.6f}")

    print(f"  Monotonic? {'YES' if monotonic else 'NO'}")

    # ================================================================
    # VALIDATION 16: Check if K_a^{nm}=0 is representation-theoretic
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION 16: Group-theoretic origin of V(gap,gap)=0")
    print("Check: individual K_a matrix elements between gap-edge modes")
    print("=" * 80)

    for idx, tau in enumerate([0.15, 0.30, 0.50]):
        tau_idx = list(tau_values).index(tau)
        evals = kosmann_data[f'eigenvalues_{tau_idx}']
        abs_e = np.abs(evals)
        sorted_idx_local = np.argsort(abs_e)

        # Gap-edge: 2 modes with smallest |lambda|
        gap_pair = sorted_idx_local[:2]
        e1, e2 = evals[gap_pair[0]], evals[gap_pair[1]]

        print(f"\n  tau={tau:.2f}: gap-edge eigenvalues = ({e1:+.6f}, {e2:+.6f})")

        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{tau_idx}_{a}']
            # K is in eigenbasis, so K[n,m] = <n|K_a|m>
            print(f"    K_{a}: <gap0|K|gap0>={K[gap_pair[0],gap_pair[0]]:.4e}, "
                  f"<gap0|K|gap1>={K[gap_pair[0],gap_pair[1]]:.4e}, "
                  f"<gap1|K|gap0>={K[gap_pair[1],gap_pair[0]]:.4e}, "
                  f"<gap1|K|gap1>={K[gap_pair[1],gap_pair[1]]:.4e}")

            # Check: is the gap pair {+lambda_min, -lambda_min}?
            # The selection rule might be: K_a connects +E to -E (odd under E -> -E)
            # so diagonal elements (same E) vanish, and off-diagonal (E to -E) don't

        # Check off-diagonal: is it that K_a is anti-diagonal in the +-lambda_min pair?
        # If so, |K_{00}|^2 + |K_{01}|^2 gives V(gap0, gap0) and V(gap0, gap1)
        # The sum over a of |K_{00}|^2 = V(gap0,gap0) = 0 would mean K_{00}=0 for all a

    print("\n" + "=" * 80)
    print("VALIDATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
