#!/usr/bin/env python3
"""
S48 LEGGETT-MODE-48: Inter-Sector Relative-Phase Oscillation Frequency
=======================================================================

In a multi-band superconductor with bands i = B1, B2, B3, the order
parameter is a vector (Delta_1 e^{i phi_1}, Delta_2 e^{i phi_2},
Delta_3 e^{i phi_3}).  The overall phase phi = (n_1 phi_1 + n_2 phi_2
+ n_3 phi_3)/n_total is the Nambu-Goldstone mode (massless, absorbed
by the Anderson-Higgs mechanism).  The RELATIVE phases
    theta_12 = phi_1 - phi_2,   theta_23 = phi_2 - phi_3
are massive: the Leggett modes.  Their frequencies are set by the
inter-sector Josephson coupling V(i,j).

Physical framework (Landau perspective):
    The free energy in the relative-phase sector reads:
        F_phase = -sum_{i<j} J_{ij} cos(phi_i - phi_j)
    where J_{ij} = V(i,j) |Delta_i| |Delta_j| is the Josephson
    coupling energy.  The mass matrix for small oscillations about
    the ground state phi_i = 0 (all phases aligned) is:
        M_{ij} = d^2 F / (d phi_i d phi_j)
    evaluated at phi_i = 0 for all i.

    For the 3-band case (B1, B2, B3):
        M = [[J12+J13, -J12, -J13],
             [-J12, J12+J23, -J23],
             [-J13, -J23, J13+J23]]
    This matrix has a zero eigenvalue (the Goldstone mode, overall
    phase rotation) and two positive eigenvalues (the Leggett modes).

    The Leggett frequencies are:
        omega_L^2 = eigenvalue / I
    where I_i = n_i / (2 Delta_i^2) is the superfluid moment of
    inertia per band, with n_i the normal-state DOS at the Fermi
    energy (here: the BCS-active DOS rho_i).

    More precisely, the kinetic energy of phase oscillations is:
        T = (1/2) sum_i rho_i * (dphi_i/dt)^2
    so the eigenvalue problem is the generalized one:
        M * phi_vec = omega^2 * diag(rho_i) * phi_vec

Method:
    1. Load V matrix, BCS gaps, and DOS from S35/S46 data
    2. Construct the 3x3 Josephson mass matrix M
    3. Construct the 3x3 inertia matrix diag(rho_i)
    4. Solve the generalized eigenvalue problem M v = omega^2 rho v
    5. Identify the Goldstone (omega = 0) and the two Leggett modes
    6. Scan over tau in [0.05, 0.35] to track omega_L(tau)
    7. Compare omega_L to 2*Delta_B3 (pair-breaking threshold)

Three V-matrix variants are checked:
    (a) V_8x8 from S35 (most conservative, direct from Dirac spectrum)
    (b) V_constrained from S46 (rank-1 constrained for self-consistency)
    (c) V_raw from S46 (unconstrained BCS kernel)

Gate: LEGGETT-MODE-48
    PASS if omega_L < 2*Delta_B3 at fold (sharp resonance)
    INFO if omega_L > 2*Delta_B3 but computable (damped resonance)
    FAIL if V(B2,B3) = 0 or omega_L = 0 everywhere

Author: Landau-Condensed-Matter-Theorist (Session 48, Wave 3-A)
Date: 2026-03-17

References:
    Leggett, PRL 14, 536 (1966) — original Leggett mode prediction
    S35 s35_thouless_multiband.npz — V matrix, E_branch, rho_i
    S46 s46_qtheory_selfconsistent.npz — self-consistent gaps, V_constrained
    W2-D (this session) — quick estimate: omega_L = 0.284 M_KK
    Landau Paper on Fermi liquid theory — quasiparticle framework
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
from scipy.interpolate import CubicSpline

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, E_cond, Delta_B3 as Delta_B3_canon,
    E_B1, E_B2_mean, E_B3_mean,
    rho_B2_per_mode, omega_PV, Gamma_Langer_BCS,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# MODULE 1: LOAD DATA AND INTERPOLATE
# =============================================================================

def load_all_data():
    """Load V matrices, BCS gaps, and DOS from S35 and S46 archives."""
    d35 = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'),
                  allow_pickle=True)
    d46 = np.load(os.path.join(SCRIPT_DIR, 's46_qtheory_selfconsistent.npz'),
                  allow_pickle=True)

    # ----- V matrices (three variants) -----
    # (a) S35 branch-averaged: V_branch_3x3[i,j] sums V_8x8 over
    #     modes within sector i and j.  Note the S35 matrix is NOT
    #     symmetric — it reports sum_k |V_{k,modes_in_j}| per mode
    #     in sector i.  We symmetrise.
    V_branch_raw = d35['V_branch_3x3']
    V_branch = 0.5 * (V_branch_raw + V_branch_raw.T)

    # (b) S46 rank-1 constrained
    V_constrained = d46['V_mat_constrained']

    # (c) S46 unconstrained raw
    V_raw = d46['V_mat_raw']

    # Extract inter-sector elements
    # Ordering: [B1, B2, B3] = indices [0, 1, 2]

    # ----- Tau-dependent BCS gaps -----
    tau_scan = d46['tau_scan']
    Delta_B1_arr = d46['Delta_B1_sc']
    Delta_B2_arr = d46['Delta_B2_sc']
    Delta_B3_arr = d46['Delta_B3_sc']
    E_B1_arr = d46['E_B1_sc']
    E_B2_arr = d46['E_B2_sc']
    E_B3_arr = d46['E_B3_sc']

    # Build cubic spline interpolants
    cs_D1 = CubicSpline(tau_scan, Delta_B1_arr)
    cs_D2 = CubicSpline(tau_scan, Delta_B2_arr)
    cs_D3 = CubicSpline(tau_scan, Delta_B3_arr)
    cs_E1 = CubicSpline(tau_scan, E_B1_arr)
    cs_E2 = CubicSpline(tau_scan, E_B2_arr)
    cs_E3 = CubicSpline(tau_scan, E_B3_arr)

    # ----- DOS at fold (S35) -----
    rho_B1 = float(d35['rho_B1'])
    rho_B2 = float(d35['rho_B2'])
    rho_B3 = float(d35['rho_B3'])

    # Also the step-function DOS (different regularisation)
    rho_B1_step = float(d35['rho_B1_step'])
    rho_B2_step = float(d35['rho_B2_step'])
    rho_B3_step = float(d35['rho_B3_step'])

    return {
        'V_branch': V_branch,
        'V_constrained': V_constrained,
        'V_raw': V_raw,
        'tau_scan': tau_scan,
        'cs_D1': cs_D1, 'cs_D2': cs_D2, 'cs_D3': cs_D3,
        'cs_E1': cs_E1, 'cs_E2': cs_E2, 'cs_E3': cs_E3,
        'rho_B1': rho_B1, 'rho_B2': rho_B2, 'rho_B3': rho_B3,
        'rho_B1_step': rho_B1_step,
        'rho_B2_step': rho_B2_step,
        'rho_B3_step': rho_B3_step,
        # Multiplicities for DOS scaling
        'n_B1': 1, 'n_B2': 4, 'n_B3': 3,
    }


# =============================================================================
# MODULE 2: JOSEPHSON MASS MATRIX AND LEGGETT MODES
# =============================================================================

def josephson_mass_matrix(V_mat, Delta_vec):
    """
    Construct the 3x3 Josephson coupling (phase stiffness) matrix.

    The Josephson energy between bands i and j is:
        E_J = -J_{ij} cos(phi_i - phi_j)
    where J_{ij} = V(i,j) * |Delta_i| * |Delta_j|.

    The mass matrix for small oscillations about phi_i = 0:
        M_{ii} = sum_{j != i} J_{ij}
        M_{ij} = -J_{ij}       (i != j)

    Parameters:
        V_mat: (3,3) inter-sector coupling matrix
        Delta_vec: (3,) gap amplitudes [Delta_B1, Delta_B2, Delta_B3]

    Returns:
        M: (3,3) phase stiffness matrix
        J: (3,3) Josephson coupling matrix (J_{ij} = V_{ij} |D_i| |D_j|)
    """
    n = len(Delta_vec)
    J = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                J[i, j] = V_mat[i, j] * np.abs(Delta_vec[i]) * np.abs(Delta_vec[j])

    M = np.zeros((n, n))
    for i in range(n):
        M[i, i] = np.sum(J[i, :])  # sum over j != i (diagonal J = 0)
        for j in range(n):
            if i != j:
                M[i, j] = -J[i, j]

    return M, J


def leggett_frequencies(M, rho_vec):
    """
    Solve the generalised eigenvalue problem for Leggett modes.

        M v = omega^2 * diag(rho) * v

    The kinetic energy of phase oscillations is:
        T = (1/2) sum_i rho_i (d phi_i / dt)^2
    which defines the inertia matrix I = diag(rho).

    The generalised eigenvalue problem:
        omega^2 = eigenvalue of I^{-1} M

    One eigenvalue is zero (Goldstone mode).
    The remaining N-1 eigenvalues give the Leggett frequencies.

    Parameters:
        M: (3,3) phase stiffness matrix
        rho_vec: (3,) DOS for each sector [rho_B1, rho_B2, rho_B3]

    Returns:
        omega_sq: (3,) eigenvalues sorted ascending (first ~ 0)
        eigvecs: (3,3) normalised eigenvectors (columns)
        omega_L: (2,) Leggett mode frequencies (sqrt of positive eigenvalues)
    """
    # I^{-1} M: this is the dynamical matrix
    I_inv = np.diag(1.0 / rho_vec)
    A = I_inv @ M

    evals, evecs = np.linalg.eig(A)

    # Sort by real part (Goldstone mode has eigenvalue ~ 0)
    idx = np.argsort(np.real(evals))
    evals = np.real(evals[idx])
    evecs = evecs[:, idx]

    # Leggett frequencies: omega = sqrt(eigenvalue) for positive eigenvalues
    omega_L = []
    for ev in evals:
        if ev > 1e-15:
            omega_L.append(np.sqrt(ev))
        else:
            omega_L.append(0.0)

    return evals, evecs, np.array(omega_L)


def leggett_frequencies_generalised(M, rho_vec):
    """
    Alternative: solve via scipy generalised eigenvalue solver.
    More numerically stable for ill-conditioned inertia matrices.

    M v = omega^2 * I * v
    """
    from scipy.linalg import eigh
    I_mat = np.diag(rho_vec)

    # eigh for symmetric generalised problem
    # Returns eigenvalues in ascending order
    evals, evecs = eigh(M, I_mat)

    omega = np.zeros_like(evals)
    for i, ev in enumerate(evals):
        if ev > 1e-15:
            omega[i] = np.sqrt(ev)

    return evals, evecs, omega


# =============================================================================
# MODULE 3: TAU SCAN
# =============================================================================

def compute_dos_at_tau(tau, data, method='spline'):
    """
    Compute the sector DOS at a given tau.

    The DOS is rho_i = n_i / (2 * BW_i) where BW_i is the bandwidth
    of sector i and n_i is the number of modes.  However, the S35 DOS
    values (rho_B1=3.94, rho_B2=14.67, rho_B3=0.48) are at tau=0.19
    and include Lorentzian broadening.

    For the tau scan, we scale rho_i by the inverse bandwidth change.
    Bandwidth is proportional to max(lambda^2) - min(lambda^2) within
    the sector, where lambda^2 are the eigenvalues of the Dirac
    operator squared.

    Since the eigenvalue splittings grow with tau (Jensen deformation
    increases), the bandwidth widens and the DOS decreases.

    APPROXIMATION: We use the fact that the BCS gap equation involves
    rho_i * V_{ij}, and V_{ij} is computed at tau = 0.19.  For a
    first estimate of the tau dependence, we scale:
        rho_i(tau) ~ rho_i(0.19) * (E_i(0.19) / E_i(tau))
    This is crude but captures the dominant trend (modes spread with tau).

    For a more rigorous treatment, one would need to recompute the
    full Dirac spectrum at each tau, but the self-consistent BCS
    gaps from S46 already fold in the tau dependence.
    """
    # At fold values
    rho_fold = np.array([data['rho_B1'], data['rho_B2'], data['rho_B3']])

    if method == 'constant':
        return rho_fold

    # Scale by inverse energy shift
    E_fold = np.array([
        float(data['cs_E1'](tau_fold)),
        float(data['cs_E2'](tau_fold)),
        float(data['cs_E3'](tau_fold)),
    ])
    E_tau = np.array([
        float(data['cs_E1'](tau)),
        float(data['cs_E2'](tau)),
        float(data['cs_E3'](tau)),
    ])

    # rho ~ 1/E in the simplest Weyl-like scaling
    # This is approximate but captures that the B3 DOS drops as
    # its modes move to higher energy
    rho_tau = rho_fold * (E_fold / E_tau)

    return rho_tau


def tau_scan_leggett(data, tau_values, V_label='constrained'):
    """
    Scan Leggett mode frequencies across tau values.

    At each tau:
        1. Interpolate Delta_i(tau) from S46 splines
        2. Estimate rho_i(tau) by DOS scaling
        3. Use the V matrix (fixed, computed at fold)
        4. Solve the Leggett eigenvalue problem
        5. Record omega_L1, omega_L2, and pair-breaking thresholds

    The V matrix is treated as tau-independent because:
        - The coupling V(i,j) depends on the Dirac eigenstates (Peter-Weyl)
          which are geometric and slowly varying
        - The dominant tau dependence comes through Delta_i(tau)
          and rho_i(tau), not V(i,j)
    """
    if V_label == 'constrained':
        V_mat = data['V_constrained']
    elif V_label == 'branch':
        V_mat = data['V_branch']
    elif V_label == 'raw':
        V_mat = data['V_raw']
    else:
        raise ValueError(f"Unknown V_label: {V_label}")

    results = {
        'tau': [],
        'omega_L1': [],   # lower Leggett mode
        'omega_L2': [],   # upper Leggett mode
        'Delta_B1': [],
        'Delta_B2': [],
        'Delta_B3': [],
        'rho_B1': [],
        'rho_B2': [],
        'rho_B3': [],
        'J_12': [],
        'J_13': [],
        'J_23': [],
        'threshold_B3': [],  # 2*Delta_B3 (pair-breaking)
        'threshold_B1': [],  # 2*Delta_B1
        'eigvecs': [],
        'goldstone_val': [],
    }

    for tau in tau_values:
        # Gaps
        D1 = float(data['cs_D1'](tau))
        D2 = float(data['cs_D2'](tau))
        D3 = float(data['cs_D3'](tau))
        Delta_vec = np.array([D1, D2, D3])

        # DOS
        rho_vec = compute_dos_at_tau(tau, data, method='spline')

        # Mass matrix
        M, J = josephson_mass_matrix(V_mat, Delta_vec)

        # Solve generalised eigenvalue problem
        evals, evecs, omega = leggett_frequencies_generalised(M, rho_vec)

        results['tau'].append(tau)
        results['omega_L1'].append(omega[1])  # first Leggett (lower)
        results['omega_L2'].append(omega[2])  # second Leggett (upper)
        results['Delta_B1'].append(D1)
        results['Delta_B2'].append(D2)
        results['Delta_B3'].append(D3)
        results['rho_B1'].append(rho_vec[0])
        results['rho_B2'].append(rho_vec[1])
        results['rho_B3'].append(rho_vec[2])
        results['J_12'].append(J[0, 1])
        results['J_13'].append(J[0, 2])
        results['J_23'].append(J[1, 2])
        results['threshold_B3'].append(2.0 * D3)
        results['threshold_B1'].append(2.0 * D1)
        results['eigvecs'].append(evecs)
        results['goldstone_val'].append(evals[0])

    # Convert to arrays
    for key in results:
        if key != 'eigvecs':
            results[key] = np.array(results[key])

    return results


# =============================================================================
# MODULE 4: DAMPING ANALYSIS
# =============================================================================

def leggett_damping_analysis(omega_L, Delta_vec, rho_vec, V_mat):
    """
    Assess the damping of the Leggett mode.

    The Leggett mode is sharp (undamped) only if omega_L lies BELOW
    all pair-breaking continua: omega_L < 2*Delta_min.

    If omega_L > 2*Delta_i for any sector i, the mode can decay into
    quasiparticle pairs in sector i.  The decay rate is:

        Gamma / omega_L ~ (V_{ij} rho_j / omega_L) * Im[chi_pair(omega_L)]

    where Im[chi_pair] ~ sqrt(omega_L^2 - 4*Delta_i^2) / omega_L
    in the BCS density of states above the gap edge.

    Returns:
        sharp: bool (True if omega_L < 2*Delta_min)
        Gamma_estimates: dict of damping rate estimates per channel
        Q_factor: quality factor omega_L / Gamma
    """
    Delta_min = np.min(Delta_vec)
    pair_threshold = 2.0 * Delta_min

    sharp = omega_L < pair_threshold

    Gamma_total = 0.0
    channels = {}

    for i in range(len(Delta_vec)):
        threshold_i = 2.0 * Delta_vec[i]
        if omega_L > threshold_i:
            # BCS coherence factor: Im[chi] ~ sqrt(omega^2 - 4*Delta^2) / omega
            # at omega just above threshold
            excess = np.sqrt(omega_L**2 - threshold_i**2) / omega_L

            # Coupling strength: sum_j V(i,j) * rho_j * Delta_j
            coupling = 0.0
            for j in range(len(Delta_vec)):
                if j != i:
                    coupling += V_mat[i, j] * rho_vec[j] * Delta_vec[j]

            # Rough estimate: Gamma ~ pi * coupling * excess
            # This is the imaginary part of the self-energy
            Gamma_i = np.pi * coupling * excess
            channels[f'B{i+1}'] = {
                'threshold': threshold_i,
                'excess': excess,
                'coupling': coupling,
                'Gamma': Gamma_i,
            }
            Gamma_total += Gamma_i
        else:
            channels[f'B{i+1}'] = {
                'threshold': threshold_i,
                'excess': 0.0,
                'coupling': 0.0,
                'Gamma': 0.0,
            }

    Q = omega_L / Gamma_total if Gamma_total > 0 else np.inf

    return {
        'sharp': sharp,
        'pair_threshold': pair_threshold,
        'channels': channels,
        'Gamma_total': Gamma_total,
        'Q_factor': Q,
    }


# =============================================================================
# MODULE 5: COMPARISON WITH W2-D QUICK ESTIMATE
# =============================================================================

def verify_w2d_estimate(data):
    """
    Cross-check the W2-D quick estimate:
        omega_L^2 = 2 V(B2,B3) (Delta_B2/rho_B3 + Delta_B3/rho_B2)
                  = 0.081
        omega_L = 0.284 M_KK

    This formula corresponds to the 2-band Leggett mode for B2-B3 only.
    The full 3-band calculation includes the B1-B2 and B1-B3 channels.
    """
    V_B2B3 = data['V_constrained'][1, 2]  # 0.0294
    D2 = float(data['cs_D2'](tau_fold))
    D3 = float(data['cs_D3'](tau_fold))
    rho_B2 = data['rho_B2']
    rho_B3 = data['rho_B3']

    # W2-D formula (2-band approximation, B2-B3 only)
    omega_sq_w2d = 2.0 * V_B2B3 * (D2 / rho_B3 + D3 / rho_B2)
    omega_w2d = np.sqrt(omega_sq_w2d)

    # Also with S35 V_8x8 value (more conservative)
    V_B2B3_s35 = 0.5 * (data['V_branch'][1, 2] + data['V_branch'][2, 1])
    omega_sq_s35 = 2.0 * V_B2B3_s35 * (D2 / rho_B3 + D3 / rho_B2)
    omega_s35 = np.sqrt(omega_sq_s35)

    return {
        'omega_w2d_constrained': omega_w2d,
        'omega_sq_w2d_constrained': omega_sq_w2d,
        'omega_w2d_s35': omega_s35,
        'omega_sq_w2d_s35': omega_sq_s35,
        'V_B2B3_constrained': V_B2B3,
        'V_B2B3_s35': V_B2B3_s35,
        'D2': D2,
        'D3': D3,
        'rho_B2': rho_B2,
        'rho_B3': rho_B3,
    }


# =============================================================================
# MODULE 6: EIGENVECTOR ANALYSIS (LANDAU PERSPECTIVE)
# =============================================================================

def analyse_mode_character(eigvecs, rho_vec, labels=('B1', 'B2', 'B3')):
    """
    Characterise the physical content of each Leggett eigenmode.

    The Goldstone mode should be proportional to rho_vec (all phases
    rotate uniformly, weighted by condensate fraction).

    The Leggett modes are the orthogonal complement: they represent
    relative phase oscillations between sectors.

    For each mode, we compute:
        - The participation ratio (how many sectors contribute)
        - The dominant oscillation pattern (which sectors are antiphase)
    """
    n = len(labels)
    modes = []
    for k in range(n):
        v = eigvecs[:, k]
        # Normalise by |v|
        v_norm = v / np.max(np.abs(v))

        # Participation ratio
        w = np.abs(v)**2
        w = w / np.sum(w)
        PR = 1.0 / np.sum(w**2)

        # Identify antiphase partners
        pos = [labels[i] for i in range(n) if v_norm[i] > 0.1]
        neg = [labels[i] for i in range(n) if v_norm[i] < -0.1]

        modes.append({
            'eigvec': v,
            'eigvec_norm': v_norm,
            'weights': w,
            'PR': PR,
            'positive': pos,
            'negative': neg,
        })

    return modes


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("  S48 LEGGETT-MODE-48: Full BdG Leggett Mode Calculation")
    print("  Landau-Condensed-Matter-Theorist")
    print("=" * 78)

    # =========================================================================
    # STEP 0: Load data
    # =========================================================================
    print("\n--- STEP 0: Load Data ---")
    data = load_all_data()

    print(f"  V_constrained (S46):")
    for i, label in enumerate(['B1', 'B2', 'B3']):
        for j, lab2 in enumerate(['B1', 'B2', 'B3']):
            print(f"    V({label},{lab2}) = {data['V_constrained'][i,j]:.6f}")

    print(f"\n  V_branch (S35, symmetrised):")
    for i, label in enumerate(['B1', 'B2', 'B3']):
        for j, lab2 in enumerate(['B1', 'B2', 'B3']):
            print(f"    V({label},{lab2}) = {data['V_branch'][i,j]:.6f}")

    print(f"\n  DOS at fold:")
    print(f"    rho_B1 = {data['rho_B1']:.6f}")
    print(f"    rho_B2 = {data['rho_B2']:.6f}")
    print(f"    rho_B3 = {data['rho_B3']:.6f}")

    print(f"\n  BCS gaps at fold (from S46 splines):")
    D1_fold = float(data['cs_D1'](tau_fold))
    D2_fold = float(data['cs_D2'](tau_fold))
    D3_fold = float(data['cs_D3'](tau_fold))
    print(f"    Delta_B1 = {D1_fold:.6f}")
    print(f"    Delta_B2 = {D2_fold:.6f}")
    print(f"    Delta_B3 = {D3_fold:.6f}")

    # =========================================================================
    # STEP 1: Verify W2-D quick estimate
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 1: Cross-Check W2-D Quick Estimate")
    print(f"{'='*78}")

    w2d = verify_w2d_estimate(data)

    print(f"\n  W2-D formula: omega_L^2 = 2 V(B2,B3) (Delta_B2/rho_B3 + Delta_B3/rho_B2)")
    print(f"  With V_constrained = {w2d['V_B2B3_constrained']:.6f}:")
    print(f"    omega_L^2 = {w2d['omega_sq_w2d_constrained']:.6f}")
    print(f"    omega_L   = {w2d['omega_w2d_constrained']:.6f} M_KK")
    print(f"  With V_branch (S35) = {w2d['V_B2B3_s35']:.6f}:")
    print(f"    omega_L^2 = {w2d['omega_sq_w2d_s35']:.6f}")
    print(f"    omega_L   = {w2d['omega_w2d_s35']:.6f} M_KK")
    print(f"  W2-D reported: omega_L = 0.284.  Discrepancy = "
          f"{abs(w2d['omega_w2d_constrained'] - 0.284):.4f}")

    # =========================================================================
    # STEP 2: Full 3-band Leggett calculation at fold
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 2: Full 3-Band Leggett Modes at Fold (tau = {tau_fold})")
    print(f"{'='*78}")

    Delta_fold = np.array([D1_fold, D2_fold, D3_fold])
    rho_fold = np.array([data['rho_B1'], data['rho_B2'], data['rho_B3']])

    for V_label, V_name in [('constrained', 'V_constrained (S46)'),
                             ('branch', 'V_branch (S35)'),
                             ('raw', 'V_raw (S46)')]:
        if V_label == 'constrained':
            V_mat = data['V_constrained']
        elif V_label == 'branch':
            V_mat = data['V_branch']
        else:
            V_mat = data['V_raw']

        M, J = josephson_mass_matrix(V_mat, Delta_fold)
        evals, evecs, omega = leggett_frequencies_generalised(M, rho_fold)

        print(f"\n  --- {V_name} ---")
        print(f"  Josephson couplings:")
        print(f"    J(B1,B2) = V * |D1| * |D2| = {J[0,1]:.6f}")
        print(f"    J(B1,B3) = V * |D1| * |D3| = {J[0,2]:.6f}")
        print(f"    J(B2,B3) = V * |D2| * |D3| = {J[1,2]:.6f}")

        print(f"  Phase stiffness matrix M:")
        for i in range(3):
            print(f"    [{M[i,0]:10.6f} {M[i,1]:10.6f} {M[i,2]:10.6f}]")

        print(f"  Eigenvalues omega^2: [{evals[0]:.6e}, {evals[1]:.6f}, {evals[2]:.6f}]")
        print(f"  Frequencies omega:   [{omega[0]:.6f}, {omega[1]:.6f}, {omega[2]:.6f}]")

        # Mode character
        modes = analyse_mode_character(evecs, rho_fold)
        for k in range(3):
            label = 'Goldstone' if k == 0 else f'Leggett-{k}'
            print(f"  Mode {k} ({label}):")
            print(f"    omega = {omega[k]:.6f} M_KK")
            print(f"    eigenvector (normalised): {modes[k]['eigvec_norm']}")
            print(f"    sector weights: B1={modes[k]['weights'][0]:.4f}, "
                  f"B2={modes[k]['weights'][1]:.4f}, B3={modes[k]['weights'][2]:.4f}")
            print(f"    PR = {modes[k]['PR']:.4f}")
            if modes[k]['positive'] and modes[k]['negative']:
                print(f"    Pattern: {'+'.join(modes[k]['positive'])} vs "
                      f"{'+'.join(modes[k]['negative'])}")

    # =========================================================================
    # STEP 3: Pair-breaking threshold comparison at fold
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 3: Pair-Breaking Threshold Analysis at Fold")
    print(f"{'='*78}")

    # Use constrained V as primary
    V_mat_primary = data['V_constrained']
    M, J = josephson_mass_matrix(V_mat_primary, Delta_fold)
    evals, evecs, omega = leggett_frequencies_generalised(M, rho_fold)

    omega_L1 = omega[1]  # lower Leggett
    omega_L2 = omega[2]  # upper Leggett

    thresh_B3 = 2.0 * D3_fold
    thresh_B1 = 2.0 * D1_fold
    thresh_B2 = 2.0 * D2_fold

    print(f"\n  Leggett mode 1: omega_L1 = {omega_L1:.6f} M_KK")
    print(f"  Leggett mode 2: omega_L2 = {omega_L2:.6f} M_KK")
    print(f"\n  Pair-breaking thresholds:")
    print(f"    2*Delta_B3 = {thresh_B3:.6f} M_KK")
    print(f"    2*Delta_B1 = {thresh_B1:.6f} M_KK")
    print(f"    2*Delta_B2 = {thresh_B2:.6f} M_KK")

    print(f"\n  Leggett-1 vs thresholds:")
    print(f"    omega_L1 / (2*Delta_B3) = {omega_L1 / thresh_B3:.4f}  "
          f"({'BELOW (sharp)' if omega_L1 < thresh_B3 else 'ABOVE (damped)'})")
    print(f"    omega_L1 / (2*Delta_B1) = {omega_L1 / thresh_B1:.4f}  "
          f"({'BELOW' if omega_L1 < thresh_B1 else 'ABOVE'})")
    print(f"    omega_L1 / (2*Delta_B2) = {omega_L1 / thresh_B2:.4f}  "
          f"({'BELOW' if omega_L1 < thresh_B2 else 'ABOVE'})")

    print(f"\n  Leggett-2 vs thresholds:")
    print(f"    omega_L2 / (2*Delta_B3) = {omega_L2 / thresh_B3:.4f}  "
          f"({'BELOW (sharp)' if omega_L2 < thresh_B3 else 'ABOVE (damped)'})")
    print(f"    omega_L2 / (2*Delta_B1) = {omega_L2 / thresh_B1:.4f}  "
          f"({'BELOW' if omega_L2 < thresh_B1 else 'ABOVE'})")

    # Damping analysis
    damping1 = leggett_damping_analysis(omega_L1, Delta_fold, rho_fold, V_mat_primary)
    damping2 = leggett_damping_analysis(omega_L2, Delta_fold, rho_fold, V_mat_primary)

    print(f"\n  Damping analysis (Leggett-1):")
    print(f"    Sharp mode: {damping1['sharp']}")
    print(f"    Pair threshold (min): {damping1['pair_threshold']:.6f}")
    for ch_name, ch_data in damping1['channels'].items():
        if ch_data['Gamma'] > 0:
            print(f"    Channel {ch_name}: Gamma = {ch_data['Gamma']:.6f}, "
                  f"threshold = {ch_data['threshold']:.6f}")
    print(f"    Gamma_total = {damping1['Gamma_total']:.6f}")
    print(f"    Q factor = {damping1['Q_factor']:.2f}")

    print(f"\n  Damping analysis (Leggett-2):")
    print(f"    Sharp mode: {damping2['sharp']}")
    for ch_name, ch_data in damping2['channels'].items():
        if ch_data['Gamma'] > 0:
            print(f"    Channel {ch_name}: Gamma = {ch_data['Gamma']:.6f}, "
                  f"threshold = {ch_data['threshold']:.6f}")
    print(f"    Gamma_total = {damping2['Gamma_total']:.6f}")
    print(f"    Q factor = {damping2['Q_factor']:.2f}")

    # =========================================================================
    # STEP 4: Tau scan
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 4: Tau Scan of Leggett Frequencies")
    print(f"{'='*78}")

    tau_values = np.array([0.05, 0.10, 0.13, 0.15, 0.19, 0.25, 0.30, 0.35])

    # Filter to valid tau range of splines
    tau_min_valid = data['tau_scan'][0]
    tau_max_valid = data['tau_scan'][-1]
    tau_values = tau_values[(tau_values >= tau_min_valid) &
                            (tau_values <= tau_max_valid)]

    print(f"\n  Tau range: [{tau_values[0]:.2f}, {tau_values[-1]:.2f}]")
    print(f"  Spline domain: [{tau_min_valid:.4f}, {tau_max_valid:.4f}]")

    # Scan with all three V matrices
    results_all = {}
    for V_label in ['constrained', 'branch', 'raw']:
        results_all[V_label] = tau_scan_leggett(data, tau_values, V_label)

    # Print table for primary (constrained)
    res = results_all['constrained']

    print(f"\n  {'tau':>5s} | {'omega_L1':>8s} | {'omega_L2':>8s} | {'2D_B3':>8s} | "
          f"{'L1/2D3':>7s} | {'D_B1':>8s} | {'D_B2':>8s} | {'D_B3':>8s} | "
          f"{'rho_B1':>8s} | {'rho_B2':>8s} | {'rho_B3':>8s}")
    print(f"  {'-'*5}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*7}-+-{'-'*8}-+-"
          f"{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}-+-{'-'*8}")

    for i in range(len(tau_values)):
        t = res['tau'][i]
        oL1 = res['omega_L1'][i]
        oL2 = res['omega_L2'][i]
        thr = res['threshold_B3'][i]
        ratio = oL1 / thr if thr > 0 else np.inf
        print(f"  {t:5.2f} | {oL1:8.5f} | {oL2:8.5f} | {thr:8.5f} | "
              f"{ratio:7.4f} | {res['Delta_B1'][i]:8.5f} | "
              f"{res['Delta_B2'][i]:8.5f} | {res['Delta_B3'][i]:8.5f} | "
              f"{res['rho_B1'][i]:8.4f} | {res['rho_B2'][i]:8.4f} | "
              f"{res['rho_B3'][i]:8.4f}")

    # Check if omega_L approaches zero anywhere
    min_L1 = np.min(res['omega_L1'])
    min_L1_tau = res['tau'][np.argmin(res['omega_L1'])]
    print(f"\n  Minimum omega_L1 = {min_L1:.6f} at tau = {min_L1_tau:.2f}")
    print(f"  omega_L1 approaches zero: {'YES' if min_L1 < 0.01 else 'NO'}")

    # Check if omega_L ever dips below threshold
    below_threshold = res['omega_L1'] < res['threshold_B3']
    if np.any(below_threshold):
        tau_below = res['tau'][below_threshold]
        print(f"  omega_L1 < 2*Delta_B3 at tau = {tau_below}")
        print(f"  Sharp resonance window: tau in [{tau_below[0]:.2f}, {tau_below[-1]:.2f}]")
    else:
        print(f"  omega_L1 > 2*Delta_B3 at ALL tau values (always damped)")

    # =========================================================================
    # STEP 5: V-matrix sensitivity
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 5: Sensitivity to V-Matrix Choice")
    print(f"{'='*78}")

    fold_idx = np.argmin(np.abs(tau_values - tau_fold))

    print(f"\n  At tau = {tau_fold}:")
    for V_label in ['constrained', 'branch', 'raw']:
        oL1 = results_all[V_label]['omega_L1'][fold_idx]
        oL2 = results_all[V_label]['omega_L2'][fold_idx]
        thr = results_all[V_label]['threshold_B3'][fold_idx]
        print(f"    V_{V_label:12s}: omega_L1 = {oL1:.5f}, "
              f"omega_L2 = {oL2:.5f}, "
              f"omega_L1/(2D_B3) = {oL1/thr:.4f}")

    # =========================================================================
    # STEP 6: Comparison with other energy scales
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 6: Energy Scale Hierarchy at Fold")
    print(f"{'='*78}")

    print(f"\n  omega_L1           = {omega_L1:.5f} M_KK")
    print(f"  omega_L2           = {omega_L2:.5f} M_KK")
    print(f"  omega_PV           = {omega_PV:.5f} M_KK  (pair vibration)")
    print(f"  Gamma_Langer       = {Gamma_Langer_BCS:.5f} M_KK  (Langer decay rate)")
    print(f"  2*Delta_B3         = {thresh_B3:.5f} M_KK  (B3 pair-breaking)")
    print(f"  2*Delta_B1         = {thresh_B1:.5f} M_KK  (B1 pair-breaking)")
    print(f"  2*Delta_B2         = {thresh_B2:.5f} M_KK  (B2 pair-breaking)")
    print(f"  |E_cond|           = {abs(E_cond):.5f} M_KK")

    print(f"\n  Ratios:")
    print(f"    omega_L1 / omega_PV       = {omega_L1/omega_PV:.4f}")
    print(f"    omega_L1 / Gamma_Langer   = {omega_L1/Gamma_Langer_BCS:.4f}")
    print(f"    omega_L2 / omega_L1       = {omega_L2/omega_L1:.4f}")

    # =========================================================================
    # STEP 7: Analytic structure of the Leggett eigenvalue problem
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 7: Analytic Structure (Landau Perspective)")
    print(f"{'='*78}")

    # The 3-band Leggett problem has a known structure.
    # With J_13 ~ 0 (K_7 selection rule), the problem simplifies.
    J_12 = V_mat_primary[0, 1] * D1_fold * D2_fold
    J_13 = V_mat_primary[0, 2] * D1_fold * D3_fold
    J_23 = V_mat_primary[1, 2] * D2_fold * D3_fold

    print(f"\n  Josephson couplings (constrained V):")
    print(f"    J_12 = {J_12:.6f}  (B1-B2, dominant)")
    print(f"    J_23 = {J_23:.6f}  (B2-B3)")
    print(f"    J_13 = {J_13:.6f}  (B1-B3)")
    print(f"    J_12/J_23 = {J_12/J_23:.2f}")
    print(f"    J_13/J_23 = {J_13/J_23:.4f}")

    # In the limit J_13 -> 0, the problem factorises:
    # Mode 1 (Goldstone): all in phase
    # Mode 2: B1 oscillates against B2 (large J_12)
    # Mode 3: B3 oscillates against B2 (smaller J_23)
    # The coupling of B3 to the B1-B2 system is through B2 only.

    # Approximate Leggett frequencies in the J_13 = 0 limit:
    # For B1-B2: omega^2 ~ J_12 * (1/rho_B1 + 1/rho_B2)
    # For B2-B3: omega^2 ~ J_23 * (1/rho_B2 + 1/rho_B3)
    rB1, rB2, rB3 = rho_fold

    omega_sq_approx_12 = J_12 * (1.0/rB1 + 1.0/rB2)
    omega_sq_approx_23 = J_23 * (1.0/rB2 + 1.0/rB3)
    omega_approx_12 = np.sqrt(omega_sq_approx_12) if omega_sq_approx_12 > 0 else 0.0
    omega_approx_23 = np.sqrt(omega_sq_approx_23) if omega_sq_approx_23 > 0 else 0.0

    print(f"\n  Approximate (J_13 = 0 limit, 2-band decoupled):")
    print(f"    omega_(B1-B2) = sqrt(J_12 * (1/rho_1 + 1/rho_2)) = {omega_approx_12:.6f}")
    print(f"    omega_(B2-B3) = sqrt(J_23 * (1/rho_2 + 1/rho_3)) = {omega_approx_23:.6f}")
    print(f"  Full 3-band:")
    print(f"    omega_L1 = {omega_L1:.6f}")
    print(f"    omega_L2 = {omega_L2:.6f}")
    print(f"  Coupling correction: {abs(omega_L1 - min(omega_approx_12, omega_approx_23))/min(omega_approx_12, omega_approx_23)*100:.2f}%")

    # =========================================================================
    # STEP 8: Gate Evaluation
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 8: Gate Evaluation — LEGGETT-MODE-48")
    print(f"{'='*78}")

    # Gate criteria:
    # PASS if omega_L < 2*Delta_B3 at fold (sharp resonance)
    # INFO if omega_L > 2*Delta_B3 but computable (damped resonance)
    # FAIL if V(B2,B3) = 0 or omega_L = 0 everywhere

    # Check V(B2,B3) nonzero
    V_B2B3_nonzero = abs(data['V_constrained'][1, 2]) > 1e-10
    omega_L_nonzero = omega_L1 > 1e-10

    print(f"\n  V(B2,B3) = {data['V_constrained'][1,2]:.6f} (nonzero: {V_B2B3_nonzero})")
    print(f"  omega_L1 = {omega_L1:.6f} (nonzero: {omega_L_nonzero})")
    print(f"  2*Delta_B3 = {thresh_B3:.6f}")
    print(f"  omega_L1 < 2*Delta_B3: {omega_L1 < thresh_B3}")

    if not V_B2B3_nonzero or not omega_L_nonzero:
        gate = "FAIL"
        gate_detail = "V(B2,B3) = 0 or omega_L = 0"
    elif omega_L1 < thresh_B3:
        gate = "PASS"
        gate_detail = (f"omega_L1 = {omega_L1:.5f} < 2*Delta_B3 = {thresh_B3:.5f} "
                       f"(sharp resonance, ratio = {omega_L1/thresh_B3:.4f})")
    else:
        gate = "INFO"
        gate_detail = (f"omega_L1 = {omega_L1:.5f} > 2*Delta_B3 = {thresh_B3:.5f} "
                       f"(damped resonance, ratio = {omega_L1/thresh_B3:.4f}, "
                       f"Q = {damping1['Q_factor']:.1f})")

    print(f"\n  GATE LEGGETT-MODE-48: {gate}")
    print(f"  Detail: {gate_detail}")

    # Also check across tau scan
    any_sharp = np.any(results_all['constrained']['omega_L1'] <
                       results_all['constrained']['threshold_B3'])
    print(f"\n  Sharp resonance at ANY tau: {any_sharp}")
    if any_sharp:
        mask = (results_all['constrained']['omega_L1'] <
                results_all['constrained']['threshold_B3'])
        sharp_taus = results_all['constrained']['tau'][mask]
        print(f"  Sharp resonance window: tau = {sharp_taus}")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  SAVING DATA")
    print(f"{'='*78}")

    npz_path = os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz')

    save_dict = {
        # Fold values
        'tau_fold': tau_fold,
        'omega_L1_fold': omega_L1,
        'omega_L2_fold': omega_L2,
        'Delta_fold': Delta_fold,
        'rho_fold': rho_fold,
        'J_12_fold': J_12,
        'J_23_fold': J_23,
        'J_13_fold': J_13,
        'threshold_B3_fold': thresh_B3,
        'threshold_B1_fold': thresh_B1,
        'threshold_B2_fold': thresh_B2,

        # Damping
        'damping_sharp_L1': damping1['sharp'],
        'Gamma_L1': damping1['Gamma_total'],
        'Q_factor_L1': damping1['Q_factor'],
        'damping_sharp_L2': damping2['sharp'],
        'Gamma_L2': damping2['Gamma_total'],
        'Q_factor_L2': damping2['Q_factor'],

        # Tau scan (constrained V)
        'tau_scan': results_all['constrained']['tau'],
        'omega_L1_scan': results_all['constrained']['omega_L1'],
        'omega_L2_scan': results_all['constrained']['omega_L2'],
        'threshold_B3_scan': results_all['constrained']['threshold_B3'],
        'threshold_B1_scan': results_all['constrained']['threshold_B1'],
        'Delta_B1_scan': results_all['constrained']['Delta_B1'],
        'Delta_B2_scan': results_all['constrained']['Delta_B2'],
        'Delta_B3_scan': results_all['constrained']['Delta_B3'],
        'rho_B1_scan': results_all['constrained']['rho_B1'],
        'rho_B2_scan': results_all['constrained']['rho_B2'],
        'rho_B3_scan': results_all['constrained']['rho_B3'],
        'J_12_scan': results_all['constrained']['J_12'],
        'J_23_scan': results_all['constrained']['J_23'],
        'goldstone_check': results_all['constrained']['goldstone_val'],

        # V-matrix sensitivity at fold
        'omega_L1_V_constrained': omega_L1,
        'omega_L1_V_branch': results_all['branch']['omega_L1'][fold_idx],
        'omega_L1_V_raw': results_all['raw']['omega_L1'][fold_idx],

        # Analytic approximations
        'omega_approx_B1B2': omega_approx_12,
        'omega_approx_B2B3': omega_approx_23,

        # W2-D cross-check
        'omega_w2d_constrained': w2d['omega_w2d_constrained'],
        'omega_w2d_s35': w2d['omega_w2d_s35'],

        # Eigenvectors at fold (constrained V)
        'eigvecs_fold': evecs,
        'evals_fold': evals,

        # Gate
        'gate_name': np.array(['LEGGETT-MODE-48']),
        'gate_verdict': np.array([gate]),
        'gate_detail': np.array([gate_detail]),
    }

    np.savez(npz_path, **save_dict)
    print(f"  Saved: {npz_path}")

    # =========================================================================
    # FIGURES
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  GENERATING FIGURES")
    print(f"{'='*78}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # --- Panel A: Leggett frequencies vs tau ---
    ax = axes[0, 0]
    tau_arr = results_all['constrained']['tau']

    ax.plot(tau_arr, results_all['constrained']['omega_L1'],
            'o-', color='#1565C0', linewidth=2, markersize=6,
            label=r'$\omega_{L1}$ (lower Leggett)')
    ax.plot(tau_arr, results_all['constrained']['omega_L2'],
            's-', color='#C62828', linewidth=2, markersize=6,
            label=r'$\omega_{L2}$ (upper Leggett)')
    ax.plot(tau_arr, results_all['constrained']['threshold_B3'],
            '--', color='#2E7D32', linewidth=2,
            label=r'$2\Delta_{B3}$ (pair-breaking)')
    ax.plot(tau_arr, results_all['constrained']['threshold_B1'],
            ':', color='#FF8F00', linewidth=2,
            label=r'$2\Delta_{B1}$')
    ax.axvline(x=tau_fold, color='gray', linestyle=':', alpha=0.5)
    ax.text(tau_fold + 0.005, ax.get_ylim()[0] + 0.02, 'fold', fontsize=9,
            color='gray')

    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel(r'$\omega$ ($M_{KK}$ units)', fontsize=13)
    ax.set_title('(A) Leggett mode frequencies vs deformation', fontsize=12)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(alpha=0.3)

    # --- Panel B: V-matrix sensitivity at fold ---
    ax = axes[0, 1]
    V_labels_plot = ['V_constrained\n(S46)', 'V_branch\n(S35)', 'V_raw\n(S46)']
    omega_L1_variants = [
        results_all['constrained']['omega_L1'][fold_idx],
        results_all['branch']['omega_L1'][fold_idx],
        results_all['raw']['omega_L1'][fold_idx],
    ]
    omega_L2_variants = [
        results_all['constrained']['omega_L2'][fold_idx],
        results_all['branch']['omega_L2'][fold_idx],
        results_all['raw']['omega_L2'][fold_idx],
    ]

    x_pos = np.arange(len(V_labels_plot))
    width = 0.35
    ax.bar(x_pos - width/2, omega_L1_variants, width, color='#1565C0',
           label=r'$\omega_{L1}$', edgecolor='black', linewidth=0.5)
    ax.bar(x_pos + width/2, omega_L2_variants, width, color='#C62828',
           label=r'$\omega_{L2}$', edgecolor='black', linewidth=0.5)
    ax.axhline(y=thresh_B3, color='#2E7D32', linestyle='--', linewidth=2,
               label=r'$2\Delta_{B3}$')
    ax.axhline(y=thresh_B1, color='#FF8F00', linestyle=':', linewidth=2,
               label=r'$2\Delta_{B1}$')
    ax.set_xticks(x_pos)
    ax.set_xticklabels(V_labels_plot, fontsize=9)
    ax.set_ylabel(r'$\omega$ ($M_{KK}$ units)', fontsize=13)
    ax.set_title(f'(B) V-matrix sensitivity at fold ($\\tau$ = {tau_fold})', fontsize=12)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(alpha=0.3, axis='y')

    # --- Panel C: Josephson couplings and gaps vs tau ---
    ax = axes[1, 0]
    ax2 = ax.twinx()

    ax.plot(tau_arr, results_all['constrained']['J_12'], 'o-',
            color='#1565C0', linewidth=2, markersize=5, label=r'$J_{12}$')
    ax.plot(tau_arr, results_all['constrained']['J_23'], 's-',
            color='#C62828', linewidth=2, markersize=5, label=r'$J_{23}$')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel('Josephson coupling $J_{ij}$', fontsize=12, color='black')
    ax.legend(fontsize=9, loc='upper left')

    ax2.plot(tau_arr, results_all['constrained']['Delta_B2'], '--',
             color='#7B1FA2', linewidth=1.5, label=r'$\Delta_{B2}$')
    ax2.plot(tau_arr, results_all['constrained']['Delta_B1'], ':',
             color='#FF8F00', linewidth=1.5, label=r'$\Delta_{B1}$')
    ax2.plot(tau_arr, results_all['constrained']['Delta_B3'], '-.',
             color='#2E7D32', linewidth=1.5, label=r'$\Delta_{B3}$')
    ax2.set_ylabel(r'Gap $\Delta_i$', fontsize=12, color='#7B1FA2')
    ax2.legend(fontsize=8, loc='upper right')

    ax.set_title('(C) Josephson couplings and BCS gaps vs $\\tau$', fontsize=12)
    ax.grid(alpha=0.3)

    # --- Panel D: Energy scale hierarchy ---
    ax = axes[1, 1]
    scale_names = [
        r'$\omega_{L1}$',
        r'$\omega_{L2}$',
        r'$2\Delta_{B3}$',
        r'$\Gamma_{\rm Langer}$',
        r'$2\Delta_{B1}$',
        r'$\omega_{\rm PV}$',
        r'$2\Delta_{B2}$',
        r'$|E_{\rm cond}|$',
    ]
    scale_values = [
        omega_L1, omega_L2, thresh_B3,
        Gamma_Langer_BCS, thresh_B1, omega_PV,
        thresh_B2, abs(E_cond),
    ]
    sorted_idx = np.argsort(scale_values)
    scale_names_sorted = [scale_names[i] for i in sorted_idx]
    scale_values_sorted = [scale_values[i] for i in sorted_idx]

    colors_bar = []
    for i in sorted_idx:
        if i < 2:
            colors_bar.append('#1565C0')  # Leggett modes
        elif i == 2:
            colors_bar.append('#2E7D32')  # B3 threshold
        elif i == 3:
            colors_bar.append('#9E9E9E')  # Langer
        else:
            colors_bar.append('#FF8F00')  # Other thresholds

    ax.barh(range(len(scale_values_sorted)), scale_values_sorted,
            color=colors_bar, edgecolor='black', linewidth=0.5)
    ax.set_yticks(range(len(scale_names_sorted)))
    ax.set_yticklabels(scale_names_sorted, fontsize=10)
    ax.set_xlabel(r'Energy scale ($M_{KK}$ units)', fontsize=12)
    ax.set_title(f'(D) Energy hierarchy at fold — GATE: {gate}', fontsize=12)
    ax.grid(alpha=0.3, axis='x')

    plt.tight_layout()
    fig_path = os.path.join(SCRIPT_DIR, 's48_leggett_mode.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  LEGGETT-MODE-48 SUMMARY")
    print(f"{'='*78}")

    print(f"\n  GATE: {gate}")
    print(f"  Detail: {gate_detail}")
    print(f"\n  Key results:")
    print(f"    omega_L1 = {omega_L1:.5f} M_KK (lower Leggett mode)")
    print(f"    omega_L2 = {omega_L2:.5f} M_KK (upper Leggett mode)")
    print(f"    2*Delta_B3 = {thresh_B3:.5f} M_KK (pair-breaking)")
    print(f"    omega_L1 / (2*Delta_B3) = {omega_L1/thresh_B3:.4f}")
    print(f"    Q(L1) = {damping1['Q_factor']:.1f}")
    print(f"\n  3-band structure:")
    print(f"    B1-B2 channel dominates (J_12 = {J_12:.5f})")
    print(f"    B2-B3 channel secondary (J_23 = {J_23:.5f})")
    print(f"    B1-B3 channel forbidden by K_7 selection rule (J_13 = {J_13:.6f})")
    print(f"\n  Physical interpretation:")
    if gate == 'PASS':
        print(f"    The Leggett mode is a sharp resonance below the pair-breaking")
        print(f"    continuum. It represents a well-defined collective excitation")
        print(f"    of the multi-sector condensate — the relative phase oscillation")
        print(f"    between B2 and B3 condensates.")
    elif gate == 'INFO':
        print(f"    The Leggett mode sits above the B3 pair-breaking continuum.")
        print(f"    It is therefore a DAMPED resonance that can decay into B3")
        print(f"    quasiparticle pairs. The Q factor = {damping1['Q_factor']:.1f} indicates")
        if damping1['Q_factor'] > 5:
            print(f"    a moderately well-defined mode (underdamped).")
        elif damping1['Q_factor'] > 1:
            print(f"    a weakly damped mode.")
        else:
            print(f"    an overdamped mode (no oscillatory behaviour).")
    print(f"\n  Comparison with W2-D: omega_L_quick = {w2d['omega_w2d_constrained']:.5f}, "
          f"full = {omega_L1:.5f}")


if __name__ == '__main__':
    main()
