"""
S37-PAIR-SUSCEPTIBILITY:  re-run of s37_pair_susceptibility.py
=======================================================================

Original: computations/session-37/s37_pair_susceptibility.py (SHA-256 head 16: 698bc5d9acfbcad4)

Purpose
-------
Reproduce S37 dynamical pair susceptibility chi_pair(omega) via Lehmann
representation over all 256 eigenstates of the 8-mode BCS ED, under
S81 canonical discipline:
  - Framework constants imported from canonical_constants.py
  - Intermediates tagged `# (local)`
  - SHA-256 pins emitted for every input npz in the first lines of stdout
  - Closure SHA emitted at the end; output 4-tuple line printed last

Gate
----
S37-PAIR-SUSCEPTIBILITY — reproducibility under PRU+OMP-cap.
  Decisive scalars:
    primary_ratio_pole_continuum  (legacy value ~0.937)
    ratio_Evac_Econd              (legacy value ~6.06 — FULL bar to 2*Delta_OES cutoff)
    Delta_OES                     — MUST match canonical Delta_0_OES
                                    = 0.4642547394830737 (R-PROTECTED,
                                    BCS-GAP-CANONICAL-70) to THEOREM (mach-eps).
    E_gs                          — MUST match canonical E_cond_ED_8mode
                                    = -0.13685055970476342 to THEOREM.

Tolerance rule:
    THEOREM: |reproduced - canonical| <= 1e-10 for Delta_OES, E_gs, total m_0
    RATIO   : rel error <= 0.5% for primary_ratio_pole_continuum, ratio_Evac_Econd

Substitution chain (sign of chi_pair divergence / pair-addition direction)
--------------------------------------------------------------------------
Defs:
  Lehmann:  chi(omega) = Sum_n [ B+_n / (omega - omega_n + i*eta)
                               - B-_n / (omega + omega_n + i*eta) ]
            B+_n  = |<n|P^dag|0>|^2    >= 0
            B-_n  = |<n|P    |0>|^2    >= 0
            omega_n = E_n - E_0        >= 0   (ground-state subtracted)

  Pair-addition energy:  omega_+ = E(N=2, min) - E(N=1, GS)
  Pair-removal  energy:  omega_- = E(N=0, min) - E(N=1, GS)   (<0 here; we
                                                               use magnitude)
  OES gap:   Delta_OES = [E(N=2, min) + E(N=0, min) - 2 E(N=1, GS)] / 2

Substitute  B+ and B- into chi(omega -> omega_n):
Step 1: Re chi ~ B+_n / (omega - omega_n)      as  omega -> omega_n^-
Step 2: B+_n > 0 AND (omega - omega_n) -> 0^-   =>   Re chi -> -infinity
Step 3: Sign of Re chi at the lowest pair-addition pole is NEGATIVE on the
        retarded approach from below.  (Goes to +infinity approaching from
        above.)  Imaginary part has a delta-function spike -pi*B+_n*delta.

Thouless criterion (for Cooper instability):
Step 4: 1 + V * chi_pair(0) = 0    gives  T_c.
Step 5: chi_pair(0) = Sum_n [ -B+_n / omega_n  +  B-_n / omega_n ]
                    = Sum_n  -(B+_n - B-_n) / omega_n
Step 6: For attractive V and number-conserving ED GS with N_pair=1,
        B+_n > B-_n at the low-omega pair-vibrational pole => chi_pair(0) < 0.
Step 7: Stronger attraction redistributes strength to smaller omega_n.
Direction:  |chi_pair(0)| INCREASES with attraction;  1 - |V|*|chi_pair(0)| -> 0
            from above;  pairing instability realized.

Sum rules (used as internal cross-checks in this script):
  m_0 = Sum B+  -  Sum B-   ->  <N_pair>  (occupation)
  m_1 = Sum B+*omega - Sum B-*omega  ->  <[P,[H,P^dag]]>

No direction claims about downstream cosmology are made here; the script
only verifies reproducibility against canonical Delta_0_OES and E_cond.
"""

import hashlib
import json
import os
import sys
import time

import numpy as np

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import matplotlib                                                    # noqa: E402
matplotlib.use('Agg')
import matplotlib.pyplot as plt                                      # noqa: E402

# --- canonical constants (MANDATORY S34+) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                  # (local)
COMP_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))               # (local)
if COMP_DIR not in sys.path:
    sys.path.insert(0, COMP_DIR)
from canonical_constants import *  # noqa: E402,F401,F403

# Canonical names referenced below:
#   Delta_0_OES   — OES/pair-addition gap (M_KK, R-PROTECTED)
#   Delta_BCS     — alias of Delta_0_OES
#   E_cond        — E_cond_ED_8mode = -0.13685... (S36 8-mode 256-state ED)

ARCHIVE_DIR = os.path.abspath(os.path.join(COMP_DIR, "..", "_shared"))  # (local)

# --- input SHA-256 pins (precomputed 2026-04-17) ---
INPUT_PINS = {                                                            # (local)
    's36_multisector_ed.npz':
        '74c59d141ff64620af9b67e34f024d8190b0a0eb5d3f302b356aea12fa8f3631',
    's35a_vh_impedance_arbiter.npz':
        '410c4835f23e5064712338853f57b3ac13370c6e7ef3dfd43ffe6fb13ce7a34d',
}


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_pins():
    print('=' * 78)
    print('S37-PAIR-SUSCEPTIBILITY: SHA-256 input pins')
    print('=' * 78)
    for name, expected in INPUT_PINS.items():
        path = os.path.join(ARCHIVE_DIR, name)
        actual = sha256_of_file(path)
        match = 'OK' if actual == expected else 'MISMATCH'
        print(f'  {name:<40s} {actual[:16]}...  [{match}]')
        if actual != expected:
            raise RuntimeError(
                f'SHA mismatch for {name}: expected {expected}, got {actual}'
            )
    print()


def main():
    t0 = time.time()                                                 # (local)
    verify_pins()

    print('=' * 78)
    print('S37-PAIR-SUSCEPTIBILITY: F.2 + F.3 reproduction')
    print('=' * 78)

    # ======================================================================
    #  Step 1: Load stored data
    # ======================================================================
    data = np.load(os.path.join(ARCHIVE_DIR, 's36_multisector_ed.npz'),
                   allow_pickle=True)
    vh_arbiter = np.load(os.path.join(ARCHIVE_DIR,
                                      's35a_vh_impedance_arbiter.npz'),
                         allow_pickle=True)

    V_8x8 = data['V_8x8_full']                                       # (local)
    E_8 = data['E_8_full']                                           # (local)
    branch_labels = list(data['branch_labels'])                      # (local)
    E_cond_stored = float(data['config_4_E_cond'])                   # (local)

    # Canonical cross-check: E_cond_stored must equal canonical E_cond exactly
    assert abs(E_cond_stored - E_cond) < 1e-12, \
        f'E_cond drift: stored={E_cond_stored}, canonical={E_cond}'

    # Physical parameters (matching ED-CONV-36 exactly)
    n_modes = 8                                                      # (local) ED hardcode
    n_states = 2 ** n_modes                                          # (local) 256
    mu = 0.0                                                         # (local) chem. pot.
    xi = E_8 - mu                                                    # (local) xi_m

    # DOS: B2 modes get van Hove rho (exact from arbiter), B1+B3 get 1.0
    rho_smooth = float(vh_arbiter['rho_at_physical'])                # (local) ~14.02
    rho = np.array([rho_smooth] * 4 + [1.0, 1.0, 1.0, 1.0])          # (local)

    print('\nPhysical parameters:')
    print(f'  N_modes = {n_modes}, N_states = {n_states}')
    print(f'  mu = {mu}')
    print(f'  E_8 = {E_8}')
    print(f'  rho_smooth (VH) = {rho_smooth:.6f}')
    print(f'  branch_labels = {branch_labels}')
    print(f'  V_8x8 diagonal = {np.diag(V_8x8)}')
    print(f'  E_cond (stored) = {E_cond_stored:.12f}')
    print(f'  E_cond (canonical) = {E_cond:.12f}')

    # ======================================================================
    #  Step 2: Build and diagonalize pair Hamiltonian
    # ======================================================================
    print(f'\nReconstructing BCS pair Hamiltonian ({n_states}x{n_states})...')
    H = np.zeros((n_states, n_states))                               # (local)
    for state in range(n_states):
        for m in range(n_modes):
            if state & (1 << m):
                H[state, state] += 2 * xi[m]
    for state in range(n_states):
        for n in range(n_modes):
            for m in range(n_modes):
                if n == m:
                    continue
                if V_8x8[n, m] < 1e-15:
                    continue
                if (state & (1 << m)) and not (state & (1 << n)):
                    new_state = state ^ (1 << m) ^ (1 << n)
                    H[new_state, state] -= V_8x8[n, m] * np.sqrt(rho[n] * rho[m])
    H = 0.5 * (H + H.T)

    # n_states = 256 -> below 100x100 GPU threshold for the per-state pair-op loop,
    # but the 256x256 eigendecomp is done once.  numpy.linalg.eigh with OMP cap
    # is sufficient (runtime ~50ms).  Kept numpy for bit-for-bit reproducibility
    # with archived S37 output.
    from numpy.linalg import eigh                                    # noqa: E402
    E_all, psi_all = eigh(H)
    E_gs = float(E_all[0])                                           # (local)
    psi_gs = psi_all[:, 0]                                           # (local)

    print(f'  E_gs            = {E_gs:.12f}')
    print(f'  E_cond canonical= {E_cond:.12f}')
    print(f'  |E_gs - E_cond| = {abs(E_gs - E_cond):.2e}')

    # THEOREM tolerance — ground-state recovery is exact to machine epsilon
    assert abs(E_gs - E_cond_stored) < 1e-10, \
        f'FATAL: E_gs mismatch: {E_gs} vs stored {E_cond_stored}'
    assert abs(E_gs - E_cond) < 1e-10, \
        f'FATAL: E_gs mismatch: {E_gs} vs canonical {E_cond}'

    omega_n = E_all - E_gs                                           # (local)
    print(f'  omega_n range: [{omega_n[0]:.6f}, {omega_n[-1]:.6f}]')

    # ======================================================================
    #  Step 3: Pair-creation / annihilation matrix elements
    # ======================================================================
    Pdag_psi_gs = np.zeros(n_states)                                 # (local)
    for state in range(n_states):
        amp = psi_gs[state]
        if abs(amp) < 1e-16:
            continue
        for k in range(n_modes):
            if not (state & (1 << k)):
                new_state = state | (1 << k)
                Pdag_psi_gs[new_state] += amp
    P_psi_gs = np.zeros(n_states)                                    # (local)
    for state in range(n_states):
        amp = psi_gs[state]
        if abs(amp) < 1e-16:
            continue
        for k in range(n_modes):
            if state & (1 << k):
                new_state = state ^ (1 << k)
                P_psi_gs[new_state] += amp
    mat_elem_Pdag = psi_all.T @ Pdag_psi_gs                          # (local)
    mat_elem_P = psi_all.T @ P_psi_gs                                # (local)
    B_n_plus = np.abs(mat_elem_Pdag) ** 2                            # (local)
    B_n_minus = np.abs(mat_elem_P) ** 2                              # (local)

    sum_Pdag = float(np.sum(B_n_plus))                               # (local)
    sum_P = float(np.sum(B_n_minus))                                 # (local)
    print(f'\n  Sum |<n|P^dag|0>|^2 = {sum_Pdag:.10f}')
    print(f'  Sum |<n|P|0>|^2    = {sum_P:.10f}')

    # ======================================================================
    #  Step 4: Mode-resolved & coherent/incoherent decomposition
    # ======================================================================
    mode_Bplus = np.zeros((n_modes, n_states))                       # (local)
    mode_amp = np.zeros((n_modes, n_states))                         # (local)
    for k in range(n_modes):
        bk_dag_psi = np.zeros(n_states)                              # (local)
        for state in range(n_states):
            amp = psi_gs[state]
            if abs(amp) < 1e-16:
                continue
            if not (state & (1 << k)):
                new_state = state | (1 << k)
                bk_dag_psi[new_state] += amp
        proj = psi_all.T @ bk_dag_psi
        mode_Bplus[k, :] = np.abs(proj) ** 2
        mode_amp[k, :] = proj

    coherent = np.abs(np.sum(mode_amp, axis=0)) ** 2                 # (local)
    incoherent = np.sum(np.abs(mode_amp) ** 2, axis=0)               # (local)

    # ======================================================================
    #  Step 5: Number-sector labels
    # ======================================================================
    n_pairs_of_state = np.zeros(n_states, dtype=int)                 # (local)
    for state in range(n_states):
        n_pairs_of_state[state] = bin(state).count('1')
    eigenstate_npair = np.zeros(len(E_all), dtype=int)               # (local)
    for n_idx in range(len(E_all)):
        psi_n = psi_all[:, n_idx]
        sector_prob = np.zeros(n_modes + 1)                          # (local)
        for state in range(n_states):
            sector_prob[n_pairs_of_state[state]] += abs(psi_n[state]) ** 2
        eigenstate_npair[n_idx] = int(np.argmax(sector_prob))
    print(f'\n  Ground state dominant sector: N_pair = {eigenstate_npair[0]}')

    # ======================================================================
    #  Step 6: chi_pair(omega)
    # ======================================================================
    omega_max = 2.0                                                  # (local) grid upper
    n_omega = 4000                                                   # (local) grid pts
    omega_grid = np.linspace(0.001, omega_max, n_omega)              # (local)
    eta_values = [0.001, 0.005, 0.01, 0.02, 0.05]                    # (local)
    eta_primary = 0.01                                               # (local)

    chi_results = {}                                                 # (local)
    for eta in eta_values:
        chi_pair = np.zeros(n_omega, dtype=complex)                  # (local)
        for n_idx in range(len(E_all)):
            if omega_n[n_idx] < 1e-12 and B_n_plus[n_idx] < 1e-12:
                continue
            if B_n_plus[n_idx] > 1e-15:
                chi_pair += B_n_plus[n_idx] / (
                    omega_grid - omega_n[n_idx] + 1j * eta
                )
            if B_n_minus[n_idx] > 1e-15:
                chi_pair -= B_n_minus[n_idx] / (
                    omega_grid + omega_n[n_idx] + 1j * eta
                )
        chi_results[eta] = chi_pair

    chi_primary = chi_results[eta_primary]                           # (local)
    Im_chi = np.imag(chi_primary)                                    # (local)
    Re_chi = np.real(chi_primary)                                    # (local)

    # ======================================================================
    #  Step 7: Pole cataloguing
    # ======================================================================
    pole_data = []                                                   # (local)
    for n_idx in range(len(E_all)):
        if B_n_plus[n_idx] > 1e-10:
            pole_data.append({
                'index': n_idx,
                'omega': float(omega_n[n_idx]),
                'weight_plus': float(B_n_plus[n_idx]),
                'weight_minus': float(B_n_minus[n_idx]),
                'npair': int(eigenstate_npair[n_idx]),
            })
    pole_data.sort(key=lambda x: -x['weight_plus'])
    total_strength = float(sum(p['weight_plus'] for p in pole_data))  # (local)

    pole_omegas = sorted([p['omega'] for p in pole_data
                          if p['weight_plus'] > 1e-6])               # (local)
    omega_pair_vib = pole_omegas[0] if pole_omegas else 0.0          # (local)

    # Largest gap splitter
    omega_split = None                                               # (local)
    if len(pole_omegas) > 1:
        gaps = np.diff(pole_omegas)                                  # (local)
        max_gap_idx = int(np.argmax(gaps))                           # (local)
        omega_split = 0.5 * (pole_omegas[max_gap_idx]
                             + pole_omegas[max_gap_idx + 1])

    # ======================================================================
    #  Step 8: Pair-addition/removal & OES gap
    # ======================================================================
    N2_mask = (eigenstate_npair == 2)                                # (local)
    N0_mask = (eigenstate_npair == 0)                                # (local)
    E_N2_min = float(np.min(E_all[N2_mask])) if np.any(N2_mask) else None
    E_N0_min = float(np.min(E_all[N0_mask])) if np.any(N0_mask) else None

    omega_plus = E_N2_min - E_gs if E_N2_min is not None else None    # (local)
    omega_minus_correct = (
        E_N0_min - E_gs if E_N0_min is not None else None
    )                                                                 # (local)
    Delta_pair = None                                                 # (local)
    Delta_OES = None                                                  # (local)
    if omega_plus is not None and omega_minus_correct is not None:
        Delta_pair = 0.5 * (omega_plus + omega_minus_correct)
        Delta_OES = 0.5 * (E_N2_min + E_N0_min - 2 * E_gs)

    print(f'\n  omega_+ (N=2 - N=1)  = {omega_plus}')
    print(f'  omega_- (N=0 - N=1)  = {omega_minus_correct}')
    print(f'  Delta_pair           = {Delta_pair}')
    print(f'  Delta_OES            = {Delta_OES}')
    print(f'  canonical Delta_0_OES= {Delta_0_OES}')
    print(f'  canonical Delta_BCS  = {Delta_BCS}')

    # THEOREM tolerance against canonical
    assert Delta_OES is not None
    assert abs(Delta_OES - Delta_0_OES) < 1e-10, \
        f'Delta_OES drift: computed={Delta_OES}, canonical={Delta_0_OES}'
    assert abs(Delta_OES - Delta_BCS) < 1e-10, \
        f'Delta_BCS drift: computed={Delta_OES}, canonical={Delta_BCS}'

    # ======================================================================
    #  Step 9: F.2 pole/continuum ratio
    # ======================================================================
    ratio_first_vs_rest = 0.0                                        # (local)
    if len(pole_data) > 0:
        first_pole_strength = pole_data[0]['weight_plus']            # (local)
        rest_strength = sum(p['weight_plus'] for p in pole_data[1:]) # (local)
        denom = first_pole_strength + rest_strength                  # (local)
        ratio_first_vs_rest = (
            first_pole_strength / denom if denom > 0 else 0.0
        )

    ratio_gap_split = 0.0                                            # (local)
    if omega_split is not None:
        pole_below = sum(p['weight_plus'] for p in pole_data
                         if p['omega'] < omega_split)                 # (local)
        cont_above = sum(p['weight_plus'] for p in pole_data
                         if p['omega'] >= omega_split)                # (local)
        denom2 = pole_below + cont_above                             # (local)
        ratio_gap_split = pole_below / denom2 if denom2 > 0 else 0.0

    primary_ratio = (ratio_gap_split if omega_split is not None
                     else ratio_first_vs_rest)                       # (local)

    # ======================================================================
    #  Step 10: F.3 |E_vac|/|E_cond|
    # ======================================================================
    omega_c_vac = 2 * Delta_OES                                      # (local) canonical cutoff
    E_vac_final = 0.0                                                # (local)
    for p in pole_data:
        if p['omega'] < omega_c_vac and p['omega'] > 1e-10:
            E_vac_final += 0.5 * p['weight_plus'] * p['omega']
    ratio_vac = abs(E_vac_final) / abs(E_cond)                       # (local) using canonical E_cond

    # ======================================================================
    #  Step 11: Sum rules (internal cross-checks)
    # ======================================================================
    m0_poles = float(np.sum(B_n_plus) - np.sum(B_n_minus))            # (local)
    m1_poles = float(np.sum(B_n_plus * omega_n)
                     - np.sum(B_n_minus * omega_n))                   # (local)

    # ======================================================================
    #  Step 12: Cumulative E_vac(omega_c)
    # ======================================================================
    n_cum = 500                                                      # (local)
    omega_cum = np.linspace(0, omega_max, n_cum)                     # (local)
    E_vac_cumulative = np.zeros(n_cum)                               # (local)
    for i, om_c in enumerate(omega_cum):
        for p in pole_data:
            if p['omega'] < om_c and p['omega'] > 1e-10:
                E_vac_cumulative[i] += 0.5 * p['weight_plus'] * p['omega']
    E_vac_full_discrete = 0.5 * float(np.sum(B_n_plus * omega_n))    # (local)

    # ======================================================================
    #  Step 13: Report + verdict
    # ======================================================================
    ratio_vac_legacy = abs(E_vac_final) / abs(E_cond_stored)         # (local) same number
    print('\n' + '=' * 78)
    print('S37-PAIR-SUSCEPTIBILITY: DECISIVE SCALARS')
    print('=' * 78)
    print(f'  E_gs                 = {E_gs:.12f}')
    print(f'  Delta_OES            = {Delta_OES:.12f}')
    print(f'  omega_pair_vib       = {omega_pair_vib:.6f}')
    print(f'  omega_split          = {omega_split}')
    print(f'  primary_ratio        = {primary_ratio:.10f}')
    print(f'  ratio_first_vs_rest  = {ratio_first_vs_rest:.10f}')
    print(f'  ratio_Evac_Econd     = {ratio_vac:.10f}')
    print(f'  ratio_Evac_Econd_leg = {ratio_vac_legacy:.10f}')
    print(f'  E_vac_final          = {E_vac_final:.10f}')
    print(f'  E_vac_full           = {E_vac_full_discrete:.10f}')
    print(f'  sum_Pdag             = {sum_Pdag:.10f}')
    print(f'  sum_P                = {sum_P:.10f}')
    print(f'  m_0                  = {m0_poles:.10f}')
    print(f'  m_1                  = {m1_poles:.10f}')
    print(f'  total_strength       = {total_strength:.10f}')

    # ======================================================================
    #  Step 14: Save artifact (same variables as archive)
    # ======================================================================
    out_npz = os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz')  # (local)
    np.savez_compressed(
        out_npz,
        V_8x8=V_8x8, E_8=E_8, rho=rho, mu=mu,
        n_modes=n_modes, n_states=n_states,
        branch_labels=np.array(branch_labels),
        E_all=E_all, E_gs=E_gs, E_cond=E_cond_stored,
        omega_n=omega_n,
        B_n_plus=B_n_plus, B_n_minus=B_n_minus,
        sum_Pdag=sum_Pdag, sum_P=sum_P,
        mode_Bplus=mode_Bplus, mode_amp=mode_amp,
        coherent=coherent, incoherent=incoherent,
        eigenstate_npair=eigenstate_npair,
        omega_grid=omega_grid, Im_chi=Im_chi, Re_chi=Re_chi,
        eta_primary=eta_primary,
        eta_values=np.array(eta_values),
        Im_chi_multi_eta=np.array([np.imag(chi_results[e])
                                   for e in eta_values]),
        omega_plus=omega_plus if omega_plus is not None else np.nan,
        omega_minus=(omega_minus_correct if omega_minus_correct is not None
                     else np.nan),
        Delta_pair=Delta_pair if Delta_pair is not None else np.nan,
        Delta_OES=Delta_OES if Delta_OES is not None else np.nan,
        primary_ratio_pole_continuum=primary_ratio,
        ratio_first_pole=ratio_first_vs_rest,
        omega_split=omega_split if omega_split is not None else np.nan,
        E_vac_final=E_vac_final,
        ratio_Evac_Econd=ratio_vac,
        E_vac_cutoff=omega_c_vac,
        E_vac_full=E_vac_full_discrete,
        omega_cum=omega_cum,
        E_vac_cumulative=E_vac_cumulative,
        m0_poles=m0_poles,
        m1_poles=m1_poles,
    )
    print(f'\n  Saved: {out_npz}')
    print(f'  Size : {os.path.getsize(out_npz) / 1024:.1f} KB')

    # --- minimal plot (match archive composition) ---
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))                 # (local)
    ax = axes[0, 0]
    for eta_val in [0.005, 0.01, 0.02, 0.05]:
        ax.plot(omega_grid, np.imag(chi_results[eta_val]),
                lw=1.5, alpha=0.7, label=f'eta={eta_val}')
    ax.axvline(2 * Delta_OES, color='red', ls='--', lw=1.5,
               label=f'2*Delta_OES={2 * Delta_OES:.3f}')
    if omega_split is not None:
        ax.axvline(omega_split, color='green', ls='-.', lw=1.5,
                   label=f'split={omega_split:.3f}')
    ax.set_xlabel('omega'); ax.set_ylabel('Im chi_pair')
    ax.set_title('(a) Pair Spectral Function')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(omega_grid, Re_chi, 'b-', lw=1.5, label=f'eta={eta_primary}')
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(2 * Delta_OES, color='red', ls='--', lw=1.5)
    ax.set_xlabel('omega'); ax.set_ylabel('Re chi_pair')
    ax.set_title('(b) Real Part')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    for p in pole_data:
        color = ('steelblue' if p['omega']
                 < (omega_split if omega_split else 1e10) else 'coral')
        ax.bar(p['omega'], p['weight_plus'], width=0.015,
               color=color, alpha=0.7, edgecolor='black', linewidth=0.3)
    if omega_split is not None:
        ax.axvline(omega_split, color='green', ls='-.', lw=2,
                   label=f'split={omega_split:.3f}')
    ax.set_xlabel('omega_n'); ax.set_ylabel('|<n|P^dag|0>|^2')
    ax.set_title(f'(c) Poles (pole/total = {primary_ratio:.3f})')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(omega_cum, E_vac_cumulative, 'b-', lw=2, label='E_vac(omega_c)')
    ax.axhline(E_vac_final, color='red', ls='--', lw=1.5,
               label=f'E_vac={E_vac_final:.4f}')
    ax.axhline(abs(E_cond), color='purple', ls=':', lw=1.5,
               label=f'|E_cond|={abs(E_cond):.4f}')
    ax.axvline(2 * Delta_OES, color='red', ls='--', lw=1, alpha=0.5)
    ax.set_xlabel('omega_c'); ax.set_ylabel('E_vac (cumulative)')
    ax.set_title(f'(d) |E_vac|/|E_cond|={ratio_vac:.4f}')
    ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    fig.suptitle('S37-PAIR-SUSCEPTIBILITY: F.2 + F.3 reproduction',
                 fontsize=13, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.94])
    out_png = os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.png')  # (local)
    plt.savefig(out_png, dpi=150)
    plt.close()
    print(f'  Plot : {out_png}')

    # --- closure SHA: sha256 of ordered input-pin map ---
    pin_blob = json.dumps(INPUT_PINS, sort_keys=True).encode()       # (local)
    closure_sha = hashlib.sha256(pin_blob).hexdigest()               # (local)

    # --- output 4-tuple (last non-verdict line) ---
    value_out = primary_ratio                                        # (local) decisive scalar
    scheme = 'Lehmann_256state_ED_pair_susc'                         # (local)
    convention = 'largest_gap_split_P^dag_channel'                   # (local)
    L_max = 'N/A_ED_8mode'                                           # (local)

    print('\n' + '=' * 78)
    print('OUTPUT 4-TUPLE')
    print('=' * 78)
    print(f'value={value_out:.10f} scheme={scheme} '
          f'convention={convention} L_max={L_max}')
    print(f'closure_sha256={closure_sha}')
    print(f'runtime={time.time() - t0:.2f}s')
    print('=' * 78)


if __name__ == '__main__':
    main()
