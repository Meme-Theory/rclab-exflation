"""
Session 23a: Einstein-Theorist Validation Part 2 — Deep structural checks
"""
import numpy as np
from scipy.linalg import eigh

import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    kosmann_data = np.load(os.path.join(SCRIPT_DIR, "s23a_kosmann_singlet.npz"), allow_pickle=True)
    gap_data = np.load(os.path.join(SCRIPT_DIR, "s23a_gap_equation.npz"), allow_pickle=True)
    tau_values = gap_data['tau_values']
    C2_IDX = [3, 4, 5, 6]

    # ================================================================
    # VALIDATION A: BdG vs mu=0 linearized -- are they different?
    # ================================================================
    print("=" * 80)
    print("VALIDATION A: BdG (E_n+E_m denominator) vs mu=0 linearized (2*|xi|)")
    print("The synthesis Table II.2 shows both. Check consistency.")
    print("=" * 80)

    print(f"\n{'tau':>6s}  {'M_max(mu=0)':>14s}  {'M_max(BdG+)':>14s}  {'Ratio':>8s}")
    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        lambda_min = np.min(np.abs(evals))

        # mu=0: xi_m = evals_m, |xi_m| = |evals_m|
        abs_xi = np.maximum(np.abs(evals), 0.01 * lambda_min)
        M_mu0 = np.zeros((16, 16))
        for m in range(16):
            M_mu0[:, m] = V[:, m] / (2.0 * abs_xi[m])
        M_max_mu0 = np.max(np.linalg.eigvalsh(M_mu0))

        # BdG: use only positive eigenvalues, denominator E_n + E_m
        pos_mask = evals > 0
        pos_idx = np.where(pos_mask)[0]
        V_pos = V[np.ix_(pos_idx, pos_idx)]
        E_pos = evals[pos_idx]
        N_pos = len(E_pos)
        M_bdg = np.zeros((N_pos, N_pos))
        for n in range(N_pos):
            for m in range(N_pos):
                M_bdg[n, m] = V_pos[n, m] / (E_pos[n] + E_pos[m])
        M_max_bdg = np.max(np.linalg.eigvalsh(M_bdg))

        ratio = M_max_mu0 / M_max_bdg if M_max_bdg > 0 else 0
        print(f"  {tau:.2f}  {M_max_mu0:14.6f}  {M_max_bdg:14.6f}  {ratio:8.4f}")

    # ================================================================
    # VALIDATION B: Synthesis Table II.2 numerical check
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION B: Synthesis Table II.2 exact values")
    print("Synthesis says BdG: 0.077-0.149, mu=0: 0.077-0.155")
    print("=" * 80)

    # BdG range
    bdg_M_values = []
    mu0_M_values = []

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)

        lambda_min = np.min(np.abs(evals))

        # mu=0
        abs_xi = np.maximum(np.abs(evals), 0.01 * lambda_min)
        M_mu0 = np.zeros((16, 16))
        for m in range(16):
            M_mu0[:, m] = V[:, m] / (2.0 * abs_xi[m])
        mu0_M_values.append(np.max(np.linalg.eigvalsh(M_mu0)))

        # BdG
        pos_mask = evals > 0
        pos_idx = np.where(pos_mask)[0]
        V_pos = V[np.ix_(pos_idx, pos_idx)]
        E_pos = evals[pos_idx]
        N_pos = len(E_pos)
        M_bdg = np.zeros((N_pos, N_pos))
        for n in range(N_pos):
            for m in range(N_pos):
                M_bdg[n, m] = V_pos[n, m] / (E_pos[n] + E_pos[m])
        bdg_M_values.append(np.max(np.linalg.eigvalsh(M_bdg)))

    print(f"\n  BdG range: {min(bdg_M_values):.4f} to {max(bdg_M_values):.4f}")
    print(f"  Synthesis claims: 0.077 to 0.149")
    print(f"  mu=0 range: {min(mu0_M_values):.4f} to {max(mu0_M_values):.4f}")
    print(f"  Synthesis claims: 0.077 to 0.155")

    # Factor below critical for BdG
    bdg_factors = [1.0/m for m in bdg_M_values]
    print(f"\n  BdG factor below critical: {min(bdg_factors):.1f}x to {max(bdg_factors):.1f}x")
    print(f"  Synthesis claims: 6.7x to 12.9x")

    # ================================================================
    # VALIDATION C: The "factor ~9x" claim
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION C: 'Factor ~9x' claim at tau=0.30")
    print("=" * 80)

    idx_030 = 5
    evals = kosmann_data[f'eigenvalues_{idx_030}']
    V = np.zeros((16, 16))
    for a in C2_IDX:
        K = kosmann_data[f'K_a_matrix_{idx_030}_{a}']
        V += np.abs(K) ** 2
    V = np.real(V)
    V = 0.5 * (V + V.T)
    lambda_min = np.min(np.abs(evals))

    # mu=0 M_max
    abs_xi = np.maximum(np.abs(evals), 0.01 * lambda_min)
    M_mu0 = np.zeros((16, 16))
    for m in range(16):
        M_mu0[:, m] = V[:, m] / (2.0 * abs_xi[m])
    M_max_mu0 = np.max(np.linalg.eigvalsh(M_mu0))
    factor_mu0 = 1.0 / M_max_mu0

    # BdG M_max
    pos_mask = evals > 0
    pos_idx = np.where(pos_mask)[0]
    V_pos = V[np.ix_(pos_idx, pos_idx)]
    E_pos = evals[pos_idx]
    N_pos = len(E_pos)
    M_bdg = np.zeros((N_pos, N_pos))
    for n in range(N_pos):
        for m in range(N_pos):
            M_bdg[n, m] = V_pos[n, m] / (E_pos[n] + E_pos[m])
    M_max_bdg = np.max(np.linalg.eigvalsh(M_bdg))
    factor_bdg = 1.0 / M_max_bdg

    print(f"  tau=0.30:")
    print(f"    M_max(mu=0) = {M_max_mu0:.6f}, factor = {factor_mu0:.1f}x")
    print(f"    M_max(BdG+) = {M_max_bdg:.6f}, factor = {factor_bdg:.1f}x")
    print(f"  Synthesis says 'factor ~9x' -- this is approximate.")
    print(f"  More precisely: {factor_mu0:.1f}x (mu=0) or {factor_bdg:.1f}x (BdG)")

    # ================================================================
    # VALIDATION D: s22b vs s23a formulas
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION D: s22b used SYMMETRIC (L_X g), s23a uses ANTISYMMETRIC")
    print("Check: does s23a's antisymmetric Kosmann give different norms?")
    print("=" * 80)

    # s23a stores both K (antisymmetric) and S (symmetric) norms
    for idx, tau in enumerate(tau_values):
        K_norms = kosmann_data[f'K_norms_{idx}']
        S_norms = kosmann_data[f'S_norms_{idx}']
        K_c2 = np.sqrt(np.sum(K_norms[C2_IDX]**2))
        S_c2 = np.sqrt(np.sum(S_norms[C2_IDX]**2))

        print(f"  tau={tau:.2f}: ||K_anti|| = {K_c2:.6f}, ||S_sym|| = {S_c2:.6f}")

    # ================================================================
    # VALIDATION E: ||K_a|| norm range for the synthesis claim
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION E: Per-direction K_a norms (C2 directions)")
    print("Synthesis claims: 0.77-0.88 per direction")
    print("=" * 80)

    all_K_c2 = []
    for idx, tau in enumerate(tau_values):
        K_norms = kosmann_data[f'K_norms_{idx}']
        for a in C2_IDX:
            all_K_c2.append(K_norms[a])

    print(f"  Range of ||K_a|| per C2 direction across all tau: "
          f"{min(all_K_c2):.4f} to {max(all_K_c2):.4f}")
    print(f"  Synthesis claims: 0.77 to 0.88")

    # Total C2 norms
    all_totals = []
    for idx, tau in enumerate(tau_values):
        K_norms = kosmann_data[f'K_norms_{idx}']
        total = np.sqrt(np.sum(K_norms[C2_IDX]**2))
        all_totals.append(total)

    print(f"  Range of total ||K|| over C2: {min(all_totals):.4f} to {max(all_totals):.4f}")
    print(f"  Synthesis claims: 0.77-1.76")

    # ================================================================
    # VALIDATION F: Self-consistent iteration stored results
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION F: Self-consistent Delta from stored data")
    print("Synthesis claims: Delta ~ machine zero at mu=0")
    print("=" * 80)

    for idx, tau in enumerate(tau_values):
        Delta = gap_data[f'Delta_sc_{idx}']
        D_norm = np.linalg.norm(Delta)
        converged = bool(gap_data[f'sc_converged_{idx}'])
        n_iter = int(gap_data[f'sc_niter_{idx}'])
        print(f"  tau={tau:.2f}: |Delta|={D_norm:.4e}, converged={converged}, "
              f"n_iter={n_iter}")

    # ================================================================
    # VALIDATION G: Check the V_nm matrix has correct structure
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION G: V_nm matrix trace and spectral properties at tau=0.30")
    print("=" * 80)

    idx_030 = 5
    V = gap_data[f'V_matrix_{idx_030}']
    evals_V = np.linalg.eigvalsh(V)
    print(f"  V matrix shape: {V.shape}")
    print(f"  V trace: {np.trace(V):.6e}")
    print(f"  V rank (>1e-10): {np.sum(np.abs(evals_V) > 1e-10)}")
    print(f"  V eigenvalues: {np.sort(evals_V)[::-1][:8]}")
    print(f"  V min: {np.min(V):.6e}")
    print(f"  V max: {np.max(V):.6e}")
    print(f"  V symmetry error: {np.max(np.abs(V - V.T)):.2e}")

    # Check: V = sum |K|^2, so V must be PSD
    print(f"  V is PSD? {np.all(evals_V >= -1e-15)}")

    # ================================================================
    # VALIDATION H: Cross-check the matrix elements <n|K_a|m>
    # for gap-nearest coupling
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION H: Detailed gap-nearest coupling at tau=0.30")
    print("Synthesis claims: V(gap,nearest) ~ 0.07-0.13 'uniform across degenerate modes'")
    print("=" * 80)

    evals_030 = kosmann_data[f'eigenvalues_{idx_030}']
    abs_e = np.abs(evals_030)
    sorted_idx = np.argsort(abs_e)

    # Build levels
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

    print(f"  Gap modes: {gap_idx}, eigenvalues: {evals_030[gap_idx]}")
    print(f"  Near modes: {near_idx}, eigenvalues: {evals_030[near_idx]}")

    V_030 = gap_data[f'V_matrix_{idx_030}']
    V_gn = V_030[np.ix_(gap_idx, near_idx)]
    print(f"\n  V(gap, nearest) full matrix:")
    print(f"  {V_gn}")
    print(f"\n  Is it 'uniform across degenerate modes'?")
    nonzero = V_gn[V_gn > 0.01]
    if len(nonzero) > 0:
        print(f"    Nonzero elements: {nonzero}")
        print(f"    Std/Mean: {np.std(nonzero)/np.mean(nonzero):.4f} (0 = perfectly uniform)")
    # The matrix has a specific pattern - check it
    print(f"\n  Pattern analysis:")
    for i in range(V_gn.shape[0]):
        row = V_gn[i]
        print(f"    Row {i} (gap mode {gap_idx[i]}, E={evals_030[gap_idx[i]]:+.4f}): "
              f"{row}")

    # ================================================================
    # VALIDATION I: Verify the claimed "7-13x below threshold"
    # ================================================================
    print("\n" + "=" * 80)
    print("VALIDATION I: Factor below critical across all tau")
    print("Synthesis claims: 6.7-12.9x (BdG), 6.5-12.9x (mu=0)")
    print("=" * 80)

    mu0_factors = []
    bdg_factors = []

    for idx, tau in enumerate(tau_values):
        evals = kosmann_data[f'eigenvalues_{idx}']
        V = np.zeros((16, 16))
        for a in C2_IDX:
            K = kosmann_data[f'K_a_matrix_{idx}_{a}']
            V += np.abs(K) ** 2
        V = np.real(V)
        V = 0.5 * (V + V.T)
        lambda_min = np.min(np.abs(evals))

        # mu=0
        abs_xi = np.maximum(np.abs(evals), 0.01 * lambda_min)
        M_mu0 = np.zeros((16, 16))
        for m in range(16):
            M_mu0[:, m] = V[:, m] / (2.0 * abs_xi[m])
        M_max_mu0 = np.max(np.linalg.eigvalsh(M_mu0))
        mu0_factors.append(1.0/M_max_mu0)

        # BdG
        pos_mask = evals > 0
        pos_idx = np.where(pos_mask)[0]
        V_pos = V[np.ix_(pos_idx, pos_idx)]
        E_pos = evals[pos_idx]
        N_pos = len(E_pos)
        M_bdg = np.zeros((N_pos, N_pos))
        for n in range(N_pos):
            for m in range(N_pos):
                M_bdg[n, m] = V_pos[n, m] / (E_pos[n] + E_pos[m])
        bdg_factors.append(1.0 / np.max(np.linalg.eigvalsh(M_bdg)))

        print(f"  tau={tau:.2f}: factor(mu=0)={mu0_factors[-1]:.1f}x, "
              f"factor(BdG)={bdg_factors[-1]:.1f}x")

    print(f"\n  mu=0 factor range: {min(mu0_factors):.1f}x to {max(mu0_factors):.1f}x")
    print(f"  BdG factor range: {min(bdg_factors):.1f}x to {max(bdg_factors):.1f}x")
    print(f"  Synthesis BdG: 6.7-12.9x, mu=0: 6.5-12.9x")

    print("\n" + "=" * 80)
    print("VALIDATION PART 2 COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
