#!/usr/bin/env python3
"""
s60_leggett_mass_n2.py — Leggett Mode Mass vs Pair Number
==========================================================
Gate: LEGGETT-MASS-N2-60

PHYSICS:
    The Leggett mode is the collective relative-phase oscillation between
    condensate sectors (B2, B1, B3). Its frequency omega_L defines the
    DM mass in the phonon-exflation framework. The question: how does
    omega_L depend on the total pair number N_pair?

    For a BCS condensate with N_pair pairs in 8 modes (4 B2 + 1 B1 + 3 B3),
    the canonical Fock space dimension is C(8, N_pair). We diagonalize the
    exact BCS Hamiltonian at each N_pair and identify the Leggett mode
    through its overlap with the relative sector-number operator:

        Q_sector = N_B2 - (4/3)*N_B3 - 4*N_B1

    (chosen to be orthogonal to the total number N = N_B2 + N_B1 + N_B3).

    The Leggett mode is the excited state with the largest matrix element
    <n|Q_sector|GS>.

    Pre-registered gate:
        PASS: omega_L(2)/omega_L(1) < 0.8  (mass decreases with N_pair)
        FAIL: omega_L(2)/omega_L(1) > 1.2  (mass increases)
        INFO: ratio in [0.8, 1.2]           (mass approximately stable)

METHOD:
    1. Load single-particle energies eps_k and pairing matrix V_bare from
       s54_ed_sweep.npz at the fold (tau = 0.19).
    2. Construct canonical BCS Hamiltonian for N_pair = 1, 2, 3, 4.
    3. Diagonalize each. Extract ground state and full excitation spectrum.
    4. Build sector-number operator Q_sector. Compute matrix elements
       <n|Q_sector|GS> for all excited states |n>.
    5. Identify the Leggett mode as the excitation with the largest
       |<n|Q_sector|GS>|.
    6. Report omega_L(N_pair) = E_Leggett(N_pair) - E_GS(N_pair).
    7. Cross-check: also identify via K_7 charge quantum number and
       verify consistency with S56/S59 values at N_pair=1.

Author: landau-condensed-matter-theorist
Session: S60 W3-3
"""

import sys
import os
import time
import numpy as np
from pathlib import Path
from itertools import combinations

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, E_cond, E_cond_ED_8mode,
    Delta_0_OES, Delta_0_GL,
    omega_L1 as omega_L1_canonical,
    omega_L2 as omega_L2_canonical,
    E_B1, E_B2_mean, E_B3_mean,
    N_dof_BCS,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

data_dir = Path(__file__).parent
archive_dir = Path(__file__).parent.parent / 'computations/_shared'
t_start = time.time()

N_MODES = 8  # (local)
# Sector assignments: B2 = modes 0-3, B1 = mode 4, B3 = modes 5-7
IDX_B2 = [0, 1, 2, 3]
IDX_B1 = [4]
IDX_B3 = [5, 6, 7]

print("=" * 78)
print("S60 LEGGETT-MASS-N2-60: Leggett Mode Mass vs Pair Number")
print("=" * 78)

# =============================================================================
# SECTION 1: LOAD DATA
# =============================================================================
print("\n--- Section 1: Load input data ---")

d54 = np.load(data_dir / 's54_ed_sweep.npz', allow_pickle=True)
fold_idx = int(d54['fold_idx'])
tau_values_54 = d54['tau_values']
tau_fold_val = tau_values_54[fold_idx]
E_sp_fold = d54['E_sp_sweep'][fold_idx].copy()  # 8 single-particle energies
V_bare = d54['V_bare_cont'].copy()               # 8x8 pairing matrix

# Load S56 Leggett fabric for baseline omega_L0
d56 = np.load(data_dir / 's56_leggett_fabric.npz', allow_pickle=True)
omega_L0_GL = float(d56['omega_L0_GL'])       # 0.138
omega_L0_S49_1 = float(d56['omega_L0_S49_1']) # 0.070
omega_L0_S49_2 = float(d56['omega_L0_S49_2']) # 0.107
epsilon_Leggett = float(d56['epsilon_Leggett'])  # 0.00248

# Load S59 canonical epsilon
d59 = np.load(data_dir / 's59_epsilon_canonical.npz', allow_pickle=True)
eps_canonical = float(d59['eps_canonical'])     # 0.003743
omega_L1_ED_constrained = float(d59['omega_L1_ED_constrained'])  # 0.06955
omega_L1_canonical_59 = float(d59['omega_L1_canonical'])  # 0.04923

print(f"  fold_idx = {fold_idx}, tau_fold = {tau_fold_val:.4f}")
print(f"  E_sp at fold: {E_sp_fold}")
print(f"  V_bare norm: {np.linalg.norm(V_bare):.6f}")
print(f"  omega_L0 (GL, S56): {omega_L0_GL:.4f} M_KK")
print(f"  omega_L0 (S49-1):   {omega_L0_S49_1:.4f} M_KK")
print(f"  omega_L1 (canonical, S59): {omega_L1_canonical_59:.5f} M_KK")
print(f"  epsilon_canonical (S59): {eps_canonical:.6f}")

# =============================================================================
# SECTION 2: BCS HAMILTONIAN CONSTRUCTION
# =============================================================================
print("\n--- Section 2: BCS Hamiltonian routines ---")


def build_fock_states(n_modes, n_pair):
    """All Fock states |s> with exactly n_pair occupied modes.

    Each state is an integer whose binary representation gives occupations.
    Returns array of state integers and their indices.
    """
    states = []
    for s in range(2**n_modes):
        if bin(s).count('1') == n_pair:
            states.append(s)
    return np.array(states, dtype=np.int64)


def build_canonical_H(E_sp, V, n_pair):
    """Build BCS Hamiltonian in the N-pair canonical subspace.

    H = sum_k 2*eps_k * n_k - sum_{k != k'} V_{kk'} P+_k P_{k'}

    where P+_k creates a pair on mode k, P_k annihilates.
    In the pair basis, this is a scattering Hamiltonian:
    diagonal = sum of 2*eps for occupied modes,
    off-diagonal = -V[k, k'] for pair-hopping k' -> k.
    """
    n_modes = len(E_sp)
    states = build_fock_states(n_modes, n_pair)
    dim = len(states)
    state_idx = {int(s): i for i, s in enumerate(states)}
    H = np.zeros((dim, dim))

    for i, state in enumerate(states):
        state = int(state)
        # Diagonal: single-particle energies of occupied pairs
        for k in range(n_modes):
            if state & (1 << k):
                H[i, i] += 2.0 * E_sp[k]

        # Off-diagonal: pair scattering k' -> k (P+_k P_{k'})
        for k in range(n_modes):
            for kp in range(n_modes):
                if k == kp:
                    continue
                if abs(V[k, kp]) < 1e-30:
                    continue
                # Requires mode kp occupied and mode k empty
                if (state & (1 << kp)) and not (state & (1 << k)):
                    new_state = (state ^ (1 << kp)) | (1 << k)
                    j = state_idx.get(new_state)
                    if j is not None:
                        H[j, i] -= V[k, kp]

    return H, states


def sector_occupation(state, sector_indices):
    """Count how many modes in the given sector are occupied in state."""
    count = 0  # (local)
    for k in sector_indices:
        if int(state) & (1 << k):
            count += 1
    return count


def build_sector_operator(states, n_modes, idx_B2, idx_B1, idx_B3):
    """Build the relative sector-number operator Q_sector.

    Q_sector = N_B2 - (N_B2_max/N_B3_max)*N_B3 - (N_B2_max/N_B1_max)*N_B1

    This is the operator conjugate to the relative phase between sectors.
    The Leggett mode is the excitation with the largest matrix element of Q.

    For identification purposes, we use the simpler form:
    Q = N_B2 - (4/3)*N_B3 - 4*N_B1
    which is orthogonal to total N in the sector-count space.

    Actually, the physically motivated operator is simply:
    Q_12 = N_B2 - (4)*N_B1  (relative B2-B1 number)
    and Q_23 = N_B2 - (4/3)*N_B3  (relative B2-B3 number)
    """
    dim = len(states)
    # Build N_sector operators
    N_B2_op = np.zeros((dim, dim))
    N_B1_op = np.zeros((dim, dim))
    N_B3_op = np.zeros((dim, dim))

    for i, s in enumerate(states):
        N_B2_op[i, i] = sector_occupation(s, idx_B2)
        N_B1_op[i, i] = sector_occupation(s, idx_B1)
        N_B3_op[i, i] = sector_occupation(s, idx_B3)

    return N_B2_op, N_B1_op, N_B3_op


# =============================================================================
# SECTION 3: DIAGONALIZE AT EACH N_pair
# =============================================================================
print("\n--- Section 3: Exact diagonalization at N_pair = 1, 2, 3, 4 ---")

N_PAIR_VALUES = [1, 2, 3, 4]
results = {}

for n_pair in N_PAIR_VALUES:
    from math import comb
    dim = comb(N_MODES, n_pair)
    print(f"\n  N_pair = {n_pair}: dim(Fock) = C({N_MODES},{n_pair}) = {dim}")

    H, states = build_canonical_H(E_sp_fold, V_bare, n_pair)
    evals, evecs = np.linalg.eigh(H)

    E_GS = evals[0]
    psi_GS = evecs[:, 0]

    # Excitation spectrum
    excitations = evals - E_GS

    print(f"    E_GS = {E_GS:.6f}")
    print(f"    First 6 excitations: {excitations[:min(6, dim)]}")

    # Build sector operators
    N_B2_op, N_B1_op, N_B3_op = build_sector_operator(
        states, N_MODES, IDX_B2, IDX_B1, IDX_B3
    )
    N_total_op = N_B2_op + N_B1_op + N_B3_op  # should be n_pair * identity

    # Verify total number conservation
    N_total_check = psi_GS @ N_total_op @ psi_GS
    print(f"    <GS|N_total|GS> = {N_total_check:.6f} (should be {n_pair})")

    # Ground state sector occupations
    n_B2_GS = psi_GS @ N_B2_op @ psi_GS
    n_B1_GS = psi_GS @ N_B1_op @ psi_GS
    n_B3_GS = psi_GS @ N_B3_op @ psi_GS
    print(f"    <N_B2> = {n_B2_GS:.4f}, <N_B1> = {n_B1_GS:.4f}, <N_B3> = {n_B3_GS:.4f}")

    # Build sector-difference operators for Leggett identification
    # The Leggett mode couples to relative number fluctuations between sectors.
    # We use three operators:
    #   Q_12 = N_B2 - (N_B2_max)*N_B1  (B2-B1 relative)
    #   Q_23 = N_B2 - (4/3)*N_B3       (B2-B3 relative)
    #   Q_13 = N_B1 - (1/3)*N_B3       (B1-B3 relative)
    # The Leggett mode has the largest matrix element in one of these.

    # More physically: use the Leggett operator L = N_B2/4 - N_B3/3
    # which measures the asymmetry between the two non-trivial sectors,
    # normalized per mode count.
    Q_Leggett = N_B2_op / 4.0 - N_B3_op / 3.0
    # Also: the B2-B1 operator (the primary Leggett channel in MgB2 analogy)
    Q_21 = N_B2_op - 4.0 * N_B1_op

    # Compute matrix elements <n|Q|GS> for all excited states
    Q_L_me = np.zeros(dim)
    Q_21_me = np.zeros(dim)
    for n in range(dim):
        psi_n = evecs[:, n]
        Q_L_me[n] = abs(psi_n @ Q_Leggett @ psi_GS)
        Q_21_me[n] = abs(psi_n @ Q_21 @ psi_GS)

    # The GS itself has <GS|Q|GS> which is just the expectation value, not zero
    # For excited states, the matrix element <n|Q|GS> is the transition amplitude
    Q_L_me[0] = 0.0  # Exclude ground state
    Q_21_me[0] = 0.0

    # Find the Leggett mode: largest |<n|Q_Leggett|GS>| among excited states
    # Use the combined response: sum of both operators
    Q_combined_me = np.sqrt(Q_L_me**2 + Q_21_me**2)

    idx_Leggett = np.argmax(Q_combined_me[1:]) + 1  # skip GS
    omega_Leggett = excitations[idx_Leggett]
    Q_Leggett_me_val = Q_combined_me[idx_Leggett]

    # Also check if there's a second Leggett mode
    Q_sorted_idx = np.argsort(-Q_combined_me[1:]) + 1
    idx_L2 = Q_sorted_idx[1] if len(Q_sorted_idx) > 1 else None
    omega_L2 = excitations[idx_L2] if idx_L2 is not None else None

    print(f"    Leggett mode identification:")
    print(f"      Primary Leggett: excitation #{idx_Leggett}, "
          f"omega_L = {omega_Leggett:.6f}, |<n|Q|GS>| = {Q_Leggett_me_val:.6f}")
    if idx_L2 is not None:
        print(f"      Second Leggett:  excitation #{idx_L2}, "
              f"omega_L2 = {omega_L2:.6f}, |<n|Q|GS>| = {Q_combined_me[idx_L2]:.6f}")

    # Store results
    results[n_pair] = {
        'dim': dim,
        'evals': evals,
        'excitations': excitations,
        'E_GS': E_GS,
        'psi_GS': psi_GS,
        'n_B2': n_B2_GS,
        'n_B1': n_B1_GS,
        'n_B3': n_B3_GS,
        'idx_Leggett': idx_Leggett,
        'omega_Leggett': omega_Leggett,
        'Q_me': Q_Leggett_me_val,
        'idx_L2': idx_L2,
        'omega_L2': omega_L2,
        'Q_L_me': Q_L_me,
        'Q_21_me': Q_21_me,
        'Q_combined_me': Q_combined_me,
    }

# =============================================================================
# SECTION 4: MASS RATIO AND GATE
# =============================================================================
print("\n--- Section 4: Mass ratio and gate verdict ---")

omega_L_1 = results[1]['omega_Leggett']
omega_L_2 = results[2]['omega_Leggett']
omega_L_3 = results[3]['omega_Leggett']
omega_L_4 = results[4]['omega_Leggett']

ratio_21 = omega_L_2 / omega_L_1
ratio_31 = omega_L_3 / omega_L_1
ratio_41 = omega_L_4 / omega_L_1

delta_m_21 = omega_L_2 - omega_L_1
delta_m_31 = omega_L_3 - omega_L_1
delta_m_41 = omega_L_4 - omega_L_1

print(f"\n  Leggett mode frequencies:")
print(f"    omega_L(1) = {omega_L_1:.6f} M_KK  (N_pair=1, dim={results[1]['dim']})")
print(f"    omega_L(2) = {omega_L_2:.6f} M_KK  (N_pair=2, dim={results[2]['dim']})")
print(f"    omega_L(3) = {omega_L_3:.6f} M_KK  (N_pair=3, dim={results[3]['dim']})")
print(f"    omega_L(4) = {omega_L_4:.6f} M_KK  (N_pair=4, dim={results[4]['dim']})")

print(f"\n  Mass ratios:")
print(f"    omega_L(2)/omega_L(1) = {ratio_21:.6f}")
print(f"    omega_L(3)/omega_L(1) = {ratio_31:.6f}")
print(f"    omega_L(4)/omega_L(1) = {ratio_41:.6f}")

print(f"\n  Mass shifts:")
print(f"    delta_m(2-1) = {delta_m_21:.6f} M_KK")
print(f"    delta_m(3-1) = {delta_m_31:.6f} M_KK")
print(f"    delta_m(4-1) = {delta_m_41:.6f} M_KK")

# Gate verdict (from task pre-registration)
if ratio_21 < 0.8:
    gate_verdict = "PASS"
    gate_detail = f"omega_L(2)/omega_L(1) = {ratio_21:.4f} < 0.8: mass decreases with N_pair"
elif ratio_21 > 1.2:
    gate_verdict = "FAIL"
    gate_detail = f"omega_L(2)/omega_L(1) = {ratio_21:.4f} > 1.2: mass increases with N_pair"
else:
    gate_verdict = "INFO"
    gate_detail = f"omega_L(2)/omega_L(1) = {ratio_21:.4f} in [0.8, 1.2]: mass approximately stable"

print(f"\n  Gate: LEGGETT-MASS-N2-60")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# =============================================================================
# SECTION 5: CROSS-CHECKS
# =============================================================================
print("\n--- Section 5: Cross-checks ---")

# Cross-check 1: Compare N=1 omega_L to S59 canonical value
print(f"\n  Cross-check 1: N=1 Leggett frequency comparison")
print(f"    omega_L(1) [this script]  = {omega_L_1:.6f}")
print(f"    omega_L1 (S59 canonical)  = {omega_L1_canonical_59:.6f}")
print(f"    omega_L0 (S56 GL)         = {omega_L0_GL:.6f}")
# Note: omega_L(1) from ED and omega_L0 from the Leggett formula are
# different quantities. The ED gives the full excitation energy in the
# N_pair=1 canonical subspace. The formula gives the long-wavelength
# collective mode gap. They need not match exactly.

# Cross-check 2: Condensation energy vs canonical value
E_cond_N1 = results[1]['E_GS'] - 2.0 * E_sp_fold[0]  # relative to non-interacting GS
E_cond_N2_nonint = sum(2.0 * E_sp_fold[i] for i in range(2))  # lowest 2 modes
E_cond_N2 = results[2]['E_GS'] - E_cond_N2_nonint
print(f"\n  Cross-check 2: Condensation energies")
print(f"    E_cond(N=1) = {E_cond_N1:.6f} (canonical: {E_cond:.6f})")
print(f"    E_cond(N=2) = {E_cond_N2:.6f}")

# Cross-check 3: Hermiticity of Hamiltonians
for n_pair in N_PAIR_VALUES:
    H, states = build_canonical_H(E_sp_fold, V_bare, n_pair)
    asym = np.linalg.norm(H - H.T) / np.linalg.norm(H)
    print(f"    ||H - H^T||/||H|| at N={n_pair}: {asym:.2e}")

# Cross-check 4: Sum rule for sector operator matrix elements
# sum_n |<n|Q|GS>|^2 = <GS|Q^2|GS> - <GS|Q|GS>^2 (variance)
for n_pair in N_PAIR_VALUES:
    r = results[n_pair]
    dim = r['dim']
    me_sq_sum = sum(r['Q_combined_me'][n]**2 for n in range(1, dim))
    # Compute variance directly
    H_n, states_n = build_canonical_H(E_sp_fold, V_bare, n_pair)
    evals_n, evecs_n = np.linalg.eigh(H_n)
    N_B2_op, N_B1_op, N_B3_op = build_sector_operator(
        states_n, N_MODES, IDX_B2, IDX_B1, IDX_B3
    )
    Q_op = N_B2_op / 4.0 - N_B3_op / 3.0
    Q_21_op = N_B2_op - 4.0 * N_B1_op
    Q_comb_sq = Q_op @ Q_op + Q_21_op @ Q_21_op
    psi0 = evecs_n[:, 0]
    variance = psi0 @ Q_comb_sq @ psi0 - (psi0 @ Q_op @ psi0)**2 - (psi0 @ Q_21_op @ psi0)**2
    print(f"    N={n_pair}: sum|<n|Q|GS>|^2 = {me_sq_sum:.6f}, "
          f"Var(Q) = {variance:.6f}")

# Cross-check 5: Sector occupation scaling with N_pair
print(f"\n  Cross-check 5: Sector occupation scaling")
print(f"    N_pair | <N_B2> | <N_B1> | <N_B3> | f_B2")
for n_pair in N_PAIR_VALUES:
    r = results[n_pair]
    f_B2 = r['n_B2'] / n_pair
    print(f"    {n_pair:6d} | {r['n_B2']:.4f} | {r['n_B1']:.4f} | "
          f"{r['n_B3']:.4f} | {f_B2:.4f}")

# =============================================================================
# SECTION 6: EXTENDED ANALYSIS — Leggett mode identification quality
# =============================================================================
print("\n--- Section 6: Leggett mode identification quality ---")

for n_pair in N_PAIR_VALUES:
    r = results[n_pair]
    dim = r['dim']
    # Ratio of largest to second-largest matrix element
    sorted_me = np.sort(r['Q_combined_me'][1:])[::-1]
    if len(sorted_me) >= 2 and sorted_me[1] > 1e-12:
        selectivity = sorted_me[0] / sorted_me[1]
    else:
        selectivity = np.inf
    print(f"  N_pair={n_pair}: selectivity = {selectivity:.4f} "
          f"(|<L|Q|GS>|/|<L2|Q|GS>| — larger = cleaner identification)")
    print(f"    Top 3 excitations by |<n|Q|GS>|:")
    top3_idx = np.argsort(-r['Q_combined_me'][1:])[:3] + 1
    for rank, idx in enumerate(top3_idx):
        print(f"      #{rank+1}: excitation {idx}, dE = {r['excitations'][idx]:.6f}, "
              f"|<n|Q|GS>| = {r['Q_combined_me'][idx]:.6f}")

# =============================================================================
# SECTION 7: TAU DEPENDENCE (optional: mass ratio at multiple tau values)
# =============================================================================
print("\n--- Section 7: Mass ratio at selected tau values ---")

# Test at 5 tau values around the fold to check robustness
tau_test_indices = [fold_idx - 4, fold_idx - 2, fold_idx,
                    fold_idx + 2, fold_idx + 4]
tau_test_indices = [max(0, min(i, len(tau_values_54)-1)) for i in tau_test_indices]

omega_L_tau = {np: [] for np in [1, 2]}
tau_test_vals = []

for t_idx in tau_test_indices:
    E_sp_t = d54['E_sp_sweep'][t_idx].copy()
    tau_t = tau_values_54[t_idx]
    tau_test_vals.append(tau_t)

    for n_pair in [1, 2]:
        H_t, states_t = build_canonical_H(E_sp_t, V_bare, n_pair)
        evals_t, evecs_t = np.linalg.eigh(H_t)
        N_B2_t, N_B1_t, N_B3_t = build_sector_operator(
            states_t, N_MODES, IDX_B2, IDX_B1, IDX_B3
        )
        Q_L_t = N_B2_t / 4.0 - N_B3_t / 3.0
        Q_21_t = N_B2_t - 4.0 * N_B1_t
        psi0_t = evecs_t[:, 0]

        Q_me_t = np.zeros(len(states_t))
        for n in range(len(states_t)):
            psi_n = evecs_t[:, n]
            q1 = abs(psi_n @ Q_L_t @ psi0_t)
            q2 = abs(psi_n @ Q_21_t @ psi0_t)
            Q_me_t[n] = np.sqrt(q1**2 + q2**2)
        Q_me_t[0] = 0.0

        idx_L = np.argmax(Q_me_t[1:]) + 1
        omega_L_tau[n_pair].append(evals_t[idx_L] - evals_t[0])

print(f"  tau    | omega_L(1) | omega_L(2) | ratio(2/1)")
for i, tau_t in enumerate(tau_test_vals):
    oL1 = omega_L_tau[1][i]
    oL2 = omega_L_tau[2][i]
    r = oL2 / oL1 if oL1 > 1e-12 else np.inf
    print(f"  {tau_t:.4f} | {oL1:.6f}   | {oL2:.6f}   | {r:.4f}")

# =============================================================================
# SECTION 8: SAVE DATA
# =============================================================================
print("\n--- Section 8: Save results ---")

save_dict = {
    # Input parameters
    'tau_fold': tau_fold_val,
    'fold_idx': fold_idx,
    'E_sp_fold': E_sp_fold,
    'V_bare': V_bare,
    'N_modes': N_MODES,

    # Results for each N_pair
    'N_pair_values': np.array(N_PAIR_VALUES),
    'omega_L': np.array([results[n]['omega_Leggett'] for n in N_PAIR_VALUES]),
    'omega_L2_mode': np.array([results[n]['omega_L2'] if results[n]['omega_L2'] is not None else 0.0
                                for n in N_PAIR_VALUES]),
    'E_GS': np.array([results[n]['E_GS'] for n in N_PAIR_VALUES]),
    'n_B2': np.array([results[n]['n_B2'] for n in N_PAIR_VALUES]),
    'n_B1': np.array([results[n]['n_B1'] for n in N_PAIR_VALUES]),
    'n_B3': np.array([results[n]['n_B3'] for n in N_PAIR_VALUES]),
    'Q_me_Leggett': np.array([results[n]['Q_me'] for n in N_PAIR_VALUES]),
    'dim_Fock': np.array([results[n]['dim'] for n in N_PAIR_VALUES]),
    'idx_Leggett': np.array([results[n]['idx_Leggett'] for n in N_PAIR_VALUES]),

    # Key ratios
    'ratio_21': ratio_21,
    'ratio_31': ratio_31,
    'ratio_41': ratio_41,
    'delta_m_21': delta_m_21,
    'delta_m_31': delta_m_31,
    'delta_m_41': delta_m_41,

    # Tau sweep
    'tau_test_values': np.array(tau_test_vals),
    'omega_L_tau_N1': np.array(omega_L_tau[1]),
    'omega_L_tau_N2': np.array(omega_L_tau[2]),

    # Reference values
    'omega_L0_GL_S56': omega_L0_GL,
    'omega_L0_S49_1': omega_L0_S49_1,
    'omega_L1_canonical_S59': omega_L1_canonical_59,
    'eps_canonical': eps_canonical,

    # Gate
    'gate_name': 'LEGGETT-MASS-N2-60',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
}

outpath = data_dir / 's60_leggett_mass_n2.npz'
np.savez(outpath, **save_dict)
print(f"  Saved: {outpath}")

# =============================================================================
# SECTION 9: PLOTS
# =============================================================================
print("\n--- Section 9: Plots ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

# Panel 1: Leggett frequency vs N_pair
ax1 = fig.add_subplot(gs[0, 0])
n_pairs_arr = np.array(N_PAIR_VALUES)
omega_L_arr = np.array([results[n]['omega_Leggett'] for n in N_PAIR_VALUES])
omega_L2_arr = np.array([results[n]['omega_L2'] if results[n]['omega_L2'] is not None else np.nan
                          for n in N_PAIR_VALUES])

ax1.plot(n_pairs_arr, omega_L_arr, 'o-', color='C0', markersize=10, linewidth=2,
         label=r'$\omega_L^{(1)}$ (primary Leggett)')
ax1.plot(n_pairs_arr, omega_L2_arr, 's--', color='C1', markersize=8, linewidth=1.5,
         label=r'$\omega_L^{(2)}$ (second Leggett)')
ax1.axhline(omega_L0_GL, color='gray', linestyle=':', alpha=0.5,
            label=f'S56 GL: {omega_L0_GL:.3f}')
ax1.axhline(omega_L1_canonical_59, color='gray', linestyle='--', alpha=0.5,
            label=f'S59 canonical: {omega_L1_canonical_59:.4f}')
ax1.set_xlabel(r'$N_{\rm pair}$', fontsize=14)
ax1.set_ylabel(r'$\omega_L$ [M$_{\rm KK}$]', fontsize=14)
ax1.set_title(r'Leggett Mode Frequency vs $N_{\rm pair}$', fontsize=14)
ax1.legend(fontsize=9, loc='best')
ax1.set_xticks(N_PAIR_VALUES)

# Panel 2: Mass ratio vs N_pair
ax2 = fig.add_subplot(gs[0, 1])
ratios = omega_L_arr / omega_L_arr[0]
ax2.plot(n_pairs_arr, ratios, 'o-', color='C2', markersize=10, linewidth=2)
ax2.axhline(1.0, color='k', linestyle='-', alpha=0.3)
ax2.axhline(0.8, color='green', linestyle='--', alpha=0.5, label='PASS threshold (< 0.8)')
ax2.axhline(1.2, color='red', linestyle='--', alpha=0.5, label='FAIL threshold (> 1.2)')
ax2.fill_between([0.5, 4.5], 0.8, 1.2, color='yellow', alpha=0.1, label='INFO region')
ax2.set_xlabel(r'$N_{\rm pair}$', fontsize=14)
ax2.set_ylabel(r'$\omega_L(N)/\omega_L(1)$', fontsize=14)
ax2.set_title('Mass Ratio (Gate: LEGGETT-MASS-N2-60)', fontsize=14)
ax2.legend(fontsize=9, loc='best')
ax2.set_xticks(N_PAIR_VALUES)
ax2.set_xlim(0.5, 4.5)

# Panel 3: Sector occupations vs N_pair
ax3 = fig.add_subplot(gs[1, 0])
n_B2_arr = np.array([results[n]['n_B2'] for n in N_PAIR_VALUES])
n_B1_arr = np.array([results[n]['n_B1'] for n in N_PAIR_VALUES])
n_B3_arr = np.array([results[n]['n_B3'] for n in N_PAIR_VALUES])
ax3.bar(n_pairs_arr - 0.2, n_B2_arr, width=0.2, color='C0', label='B2')
ax3.bar(n_pairs_arr, n_B1_arr, width=0.2, color='C1', label='B1')
ax3.bar(n_pairs_arr + 0.2, n_B3_arr, width=0.2, color='C2', label='B3')
ax3.set_xlabel(r'$N_{\rm pair}$', fontsize=14)
ax3.set_ylabel(r'$\langle N_{\rm sector} \rangle$', fontsize=14)
ax3.set_title('Sector Occupation vs $N_{\\rm pair}$', fontsize=14)
ax3.legend(fontsize=10)
ax3.set_xticks(N_PAIR_VALUES)

# Panel 4: Mass ratio vs tau
ax4 = fig.add_subplot(gs[1, 1])
oL1_tau = np.array(omega_L_tau[1])
oL2_tau = np.array(omega_L_tau[2])
ratio_tau = oL2_tau / oL1_tau
ax4.plot(tau_test_vals, ratio_tau, 'o-', color='C3', markersize=8, linewidth=2)
ax4.axhline(0.8, color='green', linestyle='--', alpha=0.5)
ax4.axhline(1.2, color='red', linestyle='--', alpha=0.5)
ax4.axvline(tau_fold_val, color='gray', linestyle=':', alpha=0.5, label=f'fold')
ax4.fill_between(tau_test_vals, 0.8, 1.2, color='yellow', alpha=0.1)
ax4.set_xlabel(r'$\tau$', fontsize=14)
ax4.set_ylabel(r'$\omega_L(2)/\omega_L(1)$', fontsize=14)
ax4.set_title(r'Mass Ratio vs $\tau$', fontsize=14)
ax4.legend(fontsize=10)

fig.suptitle('LEGGETT-MASS-N2-60: Leggett Mode Mass vs Pair Number\n'
             f'Gate: {gate_verdict}', fontsize=16, fontweight='bold')

plt.savefig(data_dir / 's60_leggett_mass_n2.png', dpi=150, bbox_inches='tight')
print(f"  Saved: {data_dir / 's60_leggett_mass_n2.png'}")

# =============================================================================
# SECTION 10: FINAL SUMMARY
# =============================================================================
elapsed = time.time() - t_start
print(f"\n{'=' * 78}")
print(f"FINAL SUMMARY — LEGGETT-MASS-N2-60")
print(f"{'=' * 78}")
print(f"  Gate: {gate_verdict}")
print(f"  {gate_detail}")
print(f"")
print(f"  omega_L(1) = {omega_L_1:.6f} M_KK")
print(f"  omega_L(2) = {omega_L_2:.6f} M_KK")
print(f"  omega_L(3) = {omega_L_3:.6f} M_KK")
print(f"  omega_L(4) = {omega_L_4:.6f} M_KK")
print(f"  ratio(2/1) = {ratio_21:.4f}")
print(f"  ratio(3/1) = {ratio_31:.4f}")
print(f"  ratio(4/1) = {ratio_41:.4f}")
print(f"")
print(f"  Elapsed: {elapsed:.1f}s")
print(f"{'=' * 78}")
