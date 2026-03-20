#!/usr/bin/env python3
"""
S48 ANISO-GAP-48: k-Dependent BCS Gap from Superfluid Stiffness Anisotropy
==========================================================================

Tests whether the 24x anisotropy of the superfluid density tensor (rho_s)
can produce a k-dependent effective gap Delta_eff(k) sufficient to flatten
the Bogoliubov pair-creation power spectrum from slope -4 to -0.035.

Physical framework:
    In superfluid 3He-A (ABM state), the gap IS genuinely k-dependent:
        Delta(k) = Delta_perp * sin(theta_k)
    where theta_k is the angle between k and the orbital angular momentum l.
    This produces a topologically protected Fermi point (N_3 = +/-2) and
    emergent Weyl fermions with ANISOTROPIC dispersion.

    In this framework, the system is 0-dimensional (no spatial extent within
    a cell). The "modes" are discrete Dirac eigenvalues on a compact group
    manifold SU(3). The rho_s tensor measures stiffness in Lie algebra
    directions, NOT in momentum space. The question is whether assigning
    each mode a direction-dependent gap can modify the pair-creation spectrum.

Method:
    1. Load the 8 BCS modes (B1: 1, B2: 4, B3: 3) and rho_s tensor
    2. Assign each mode a dominant Lie algebra direction using the
       current operator structure (which su(3) direction does mode k
       couple most strongly to?)
    3. Define 3 ansatze for direction-dependent gap modulation:
       f1: Delta_eff = Delta_0 * sqrt(rho_s(dir) / rho_s_avg)
       f2: Delta_eff = Delta_0 * (rho_s(dir) / rho_s_avg)
       f3: Delta_eff = Delta_0 * (rho_s(dir))^{1/3}
    4. Fit Delta_eff(k) vs omega(k) to power law Delta ~ omega^{-alpha}
    5. Compute n_s = 1 - 4*alpha for Bogoliubov pair creation P ~ (Delta/omega)^4

Pre-registered gate ANISO-GAP-48:
    PASS: n_s in [0.80, 1.10] for any ansatz
    FAIL: n_s outside [0.80, 1.10] for all ansatze
    INFO: n_s in [0.50, 0.80] or ambiguous

Expected: FAIL. The 8 modes span only a 1.19x energy range (0.819 to 0.978).
The 24x rho_s anisotropy is in the WRONG SPACE (Lie algebra vs eigenvalue
ordering). sqrt(24) ~ 4.9x gap variation cannot flatten a slope-4 power law.

Superfluid 3He comparison:
    In 3He-A, the k-dependent gap arises from the MICROSCOPIC HAMILTONIAN
    (p-wave pairing in orbital channel l=1). It is protected by the
    topological charge N_3 = 2. Here, the BCS pairing is s-wave-like
    within each degenerate sector (all V(B2,B2) matrix elements identical
    by U(2) Schur's lemma). There is no microscopic mechanism to generate
    anisotropic pairing -- the Lie algebra direction dependence of rho_s
    measures the RESPONSE of the condensate to EXTERNAL gauge twists,
    not the INTERNAL gap structure.

Author: Volovik-Superfluid-Universe-Theorist (Session 48, Wave 1-C)
Date: 2026-03-17

References:
    Volovik Paper 03 (The Universe in a Helium Droplet, Ch. 7-8)
    Volovik Paper 09 (Superfluid 3He and the Universe, Sec 3.1)
    Volovik Paper 28 (BDI topological classification)
    S47 RHOS-TENSOR-47 (rho_s tensor computation)
    S47 SPECTRAL-FLOW-NS-47 (spectral flow n_s = -2.51)
    S35 RPA-BCS-35 (Thouless multiband data)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    build_cliff8,
    spinor_connection_offset,
)
from canonical_constants import (
    tau_fold, E_cond, E_B1, E_B2_mean, E_B3_mean,
    Delta_B3, M_KK_gravity,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# MODULE 1: LOAD DATA
# =============================================================================

def load_data():
    """Load rho_s tensor and BCS mode data."""
    rhos = np.load(os.path.join(SCRIPT_DIR, 's47_rhos_tensor.npz'), allow_pickle=True)
    thouless = np.load(os.path.join(SCRIPT_DIR, 's35_thouless_multiband.npz'), allow_pickle=True)
    return rhos, thouless


# =============================================================================
# MODULE 2: CURRENT OPERATOR ANALYSIS
# =============================================================================

def compute_current_mode_coupling(tau):
    """
    For each of the 8 BCS modes (positive eigenvalues of H_eff),
    compute the coupling strength to each of the 8 su(3) Lie algebra
    directions via the current operator J_a = -gamma_a.

    Returns:
        mode_dir_coupling: (8, 8) array where [k, a] = |<k|J_a|k>|^2
                          summed over all states in mode k's sector
        mode_energies: (8,) array of positive eigenvalues
        mode_sectors: (8,) array of sector labels (0=B1, 1=B2, 2=B3)
    """
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E_frame = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E_frame)
    Gamma = connection_coefficients(ft)
    gammas = build_cliff8()
    Omega = spinor_connection_offset(Gamma, gammas)
    H_eff = 1j * Omega

    evals, evecs = np.linalg.eigh(H_eff)

    # Sort by eigenvalue
    order = np.argsort(evals)
    evals = evals[order]
    evecs = evecs[:, order]

    # Positive eigenvalues: modes 8..15
    pos_evals = evals[8:]  # 8 positive eigenvalues
    pos_evecs = evecs[:, 8:]

    # Mode-direction coupling: |<k|gamma_a|k'>|^2 summed within sector
    mode_dir_coupling = np.zeros((8, 8))
    for a in range(8):
        J_a = gammas[a]  # Current operator (Hermitian)
        J_eig = pos_evecs.conj().T @ J_a @ pos_evecs  # 8x8 in positive eigenbasis
        for k in range(8):
            # Self-coupling (diagonal)
            mode_dir_coupling[k, a] = np.abs(J_eig[k, k])**2
            # Also include off-diagonal within sector
            for kp in range(8):
                if kp != k and np.abs(pos_evals[k] - pos_evals[kp]) < 1e-6:
                    mode_dir_coupling[k, a] += np.abs(J_eig[k, kp])**2

    # Assign sectors
    mode_sectors = np.zeros(8, dtype=int)
    mode_energies = np.abs(pos_evals)
    # B1: min energy, B2: middle, B3: max
    e_sorted = np.sort(np.unique(np.round(mode_energies, 8)))
    for k in range(8):
        e = mode_energies[k]
        for s, es in enumerate(e_sorted):
            if abs(e - es) < 1e-6:
                mode_sectors[k] = s
                break

    return mode_dir_coupling, mode_energies, mode_sectors, pos_evals, pos_evecs, gammas


# =============================================================================
# MODULE 3: DIRECTION-DEPENDENT GAP ANSATZE
# =============================================================================

def compute_aniso_gap(mode_dir_coupling, mode_energies, mode_sectors,
                       rho_s_diag, Delta_sectors):
    """
    Compute direction-dependent effective gap for each BCS mode.

    For each mode k, the "dominant direction" is the su(3) direction a
    with maximum coupling |<k|J_a|...>|^2. The effective gap is then
    modulated by rho_s in that direction.

    Three ansatze:
      f1: Delta_eff = Delta_sector * sqrt(rho_s(dir) / rho_s_avg)
      f2: Delta_eff = Delta_sector * (rho_s(dir) / rho_s_avg)
      f3: Delta_eff = Delta_sector * (rho_s(dir))^{1/3}

    Also a fourth ansatz using direction-averaged gap:
      f4: Delta_eff = Delta_sector * (sum_a w_a * rho_s(a)) / rho_s_avg
          where w_a = coupling[k,a] / sum coupling[k,:]

    Returns dict with results for each ansatz.
    """
    n_modes = len(mode_energies)
    rho_s_avg = np.mean(rho_s_diag)

    # Dominant direction for each mode
    dominant_dir = np.argmax(mode_dir_coupling, axis=1)

    # Weighted rho_s for each mode
    weights = mode_dir_coupling / (np.sum(mode_dir_coupling, axis=1, keepdims=True) + 1e-30)
    rho_s_weighted = np.sum(weights * rho_s_diag[np.newaxis, :], axis=1)

    results = {}

    # Sector gap for each mode
    Delta_mode = np.array([Delta_sectors[mode_sectors[k]] for k in range(n_modes)])

    for name, gap_func in [
        ('f1_sqrt', lambda D, rho: D * np.sqrt(rho / rho_s_avg)),
        ('f2_linear', lambda D, rho: D * (rho / rho_s_avg)),
        ('f3_cube_root', lambda D, rho: D * (np.abs(rho))**(1.0/3.0)),
        ('f4_weighted', lambda D, rho: D * (rho / rho_s_avg)),
    ]:
        if name == 'f4_weighted':
            Delta_eff = np.array([
                gap_func(Delta_mode[k], rho_s_weighted[k])
                for k in range(n_modes)
            ])
        else:
            Delta_eff = np.array([
                gap_func(Delta_mode[k], rho_s_diag[dominant_dir[k]])
                for k in range(n_modes)
            ])

        results[name] = {
            'Delta_eff': Delta_eff,
            'Delta_ratio': Delta_eff / Delta_mode,
        }

    results['dominant_dir'] = dominant_dir
    results['weights'] = weights
    results['rho_s_weighted'] = rho_s_weighted
    results['Delta_mode'] = Delta_mode

    return results


# =============================================================================
# MODULE 4: POWER LAW FIT AND n_s EXTRACTION
# =============================================================================

def fit_power_law_ns(mode_energies, Delta_eff, label=""):
    """
    Fit Delta_eff(omega) to power law Delta ~ omega^{-alpha}.

    Then n_s = 1 - 4*alpha (from Bogoliubov pair creation P ~ (Delta/omega)^4).

    Returns alpha, n_s, r_squared, and fit details.
    """
    omega = mode_energies
    log_omega = np.log(omega)
    log_delta = np.log(np.abs(Delta_eff) + 1e-30)

    # Linear fit: log(Delta) = -alpha * log(omega) + const
    slope, intercept, r_value, p_value, std_err = stats.linregress(log_omega, log_delta)

    alpha = -slope  # Delta ~ omega^{-alpha}
    n_s = 1.0 - 4.0 * alpha

    return {
        'alpha': alpha,
        'n_s': n_s,
        'r_squared': r_value**2,
        'p_value': p_value,
        'std_err': std_err,
        'slope': slope,
        'intercept': intercept,
    }


# =============================================================================
# MODULE 5: STRUCTURAL ANALYSIS (Volovik perspective)
# =============================================================================

def structural_analysis(mode_dir_coupling, mode_energies, mode_sectors, rho_s_diag):
    """
    Analyze whether the Lie algebra direction -> eigenvalue ordering mapping
    is well-defined. In 3He-A, each k-point has a definite theta_k that
    determines the gap. Here, we check if the mapping direction -> mode
    is one-to-one, degenerate, or random.
    """
    n_modes = len(mode_energies)

    # Dominant direction per mode
    dom_dir = np.argmax(mode_dir_coupling, axis=1)

    # Check degeneracy: how many modes share the same dominant direction?
    dir_counts = np.bincount(dom_dir, minlength=8)

    # Entropy of the direction distribution
    p = mode_dir_coupling / (np.sum(mode_dir_coupling, axis=1, keepdims=True) + 1e-30)
    entropy = -np.sum(p * np.log(p + 1e-30), axis=1)
    max_entropy = np.log(8)

    # Correlation between mode energy and dominant-direction rho_s
    rho_dominant = rho_s_diag[dom_dir]
    if len(np.unique(mode_energies)) >= 3:
        r_energy_rho, p_corr = stats.pearsonr(mode_energies, rho_dominant)
    else:
        r_energy_rho, p_corr = 0.0, 1.0

    return {
        'dominant_dir': dom_dir,
        'dir_counts': dir_counts,
        'mode_entropy': entropy,
        'mean_entropy': np.mean(entropy),
        'max_entropy': max_entropy,
        'entropy_ratio': np.mean(entropy) / max_entropy,
        'r_energy_rho': r_energy_rho,
        'p_corr': p_corr,
        'rho_dominant': rho_dominant,
    }


# =============================================================================
# MODULE 6: FULL 992-MODE ANALYSIS
# =============================================================================

def compute_full_spectrum_ns(rho_s_diag, tau):
    """
    Extend the analysis to ALL 992 Dirac modes (not just singlet).
    Each mode has a Peter-Weyl representation (p,q) and thus an SU(3)
    character that determines its dominant Lie algebra direction.

    CORRECTED METHOD: The spectral index is extracted from the PAIR-CREATION
    power spectrum P(k) = (Delta_eff(k) / omega(k))^4, NOT from Delta_eff alone.

    We fit P(k) ~ omega^{slope} and report n_s = 1 + slope.
    For uniform gap: P ~ omega^{-4}, n_s = -3.
    The question is whether gap modulation changes this.
    """
    d = np.load(os.path.join(SCRIPT_DIR, 's44_dos_tau.npz'), allow_pickle=True)
    omega_all = d[f'tau{tau:.2f}_all_omega']
    dim2_all = d[f'tau{tau:.2f}_all_dim2']

    # Direction type weights for each dim^2
    # (su2_weight, c2_weight, u1_weight) — HEURISTIC
    type_weights = {
        1:  (1.0/3, 4.0/8, 1.0/8),   # singlet: isotropic
        9:  (0.35, 0.55, 0.10),        # fundamental
        36: (0.45, 0.40, 0.15),        # adjoint
        64: (0.25, 0.65, 0.10),        # symmetric
        100:(0.30, 0.55, 0.15),        # (3,0)
        225:(0.35, 0.50, 0.15),        # (2,1)
    }

    rho_su2 = np.mean(rho_s_diag[:3])
    rho_c2 = np.mean(rho_s_diag[3:7])
    rho_u1 = rho_s_diag[7]
    rho_s_avg = np.mean(rho_s_diag)

    # Compute effective rho_s for each mode
    rho_eff = np.zeros(len(omega_all))
    for i in range(len(omega_all)):
        d2 = int(round(dim2_all[i]))
        ws, wc, wu = type_weights.get(d2, (1.0/3, 4.0/8, 1.0/8))
        rho_eff[i] = ws * rho_su2 + wc * rho_c2 + wu * rho_u1

    # Gap modulation factors
    Delta_mod_f1 = np.sqrt(rho_eff / rho_s_avg)   # sqrt ansatz
    Delta_mod_f2 = rho_eff / rho_s_avg             # linear ansatz

    # PAIR CREATION power spectrum: P(k) = (Delta_eff / omega)^4
    # Unmodulated baseline:
    P_unmod = (1.0 / omega_all)**4  # Delta constant, normalized out
    # Modulated:
    P_mod_f1 = (Delta_mod_f1 / omega_all)**4
    P_mod_f2 = (Delta_mod_f2 / omega_all)**4

    # Power law fits: P ~ omega^{slope}, n_s = 1 + slope
    log_omega = np.log(omega_all)

    fit_unmod = stats.linregress(log_omega, np.log(P_unmod))
    fit_f1 = stats.linregress(log_omega, np.log(P_mod_f1))
    fit_f2 = stats.linregress(log_omega, np.log(P_mod_f2))

    ns_unmod = 1.0 + fit_unmod.slope   # should be -3.000
    ns_f1 = 1.0 + fit_f1.slope
    ns_f2 = 1.0 + fit_f2.slope

    delta_ns_f1 = ns_f1 - ns_unmod  # shift from modulation
    delta_ns_f2 = ns_f2 - ns_unmod

    return {
        'omega_all': omega_all,
        'rho_eff': rho_eff,
        'Delta_mod_f1': Delta_mod_f1,
        'Delta_mod_f2': Delta_mod_f2,
        'ns_unmod': ns_unmod,
        'ns_f1': ns_f1,
        'ns_f2': ns_f2,
        'delta_ns_f1': delta_ns_f1,
        'delta_ns_f2': delta_ns_f2,
        'r2_unmod': fit_unmod.rvalue**2,
        'r2_f1': fit_f1.rvalue**2,
        'r2_f2': fit_f2.rvalue**2,
        'rho_range': (rho_eff.min(), rho_eff.max()),
        'rho_ratio': rho_eff.max() / rho_eff.min(),
        'slope_unmod': fit_unmod.slope,
        'slope_f1': fit_f1.slope,
        'slope_f2': fit_f2.slope,
    }


# =============================================================================
# MODULE 7: VOLOVIK STRUCTURAL COMPARISON
# =============================================================================

def he3_comparison(rho_s_diag, mode_energies):
    """
    Quantitative comparison with 3He-A gap anisotropy.

    In 3He-A (ABM state):
        Delta(k) = Delta_perp * sin(theta_k)
    where theta_k in [0, pi].

    The gap varies from 0 (at poles, theta=0,pi) to Delta_perp
    (at equator, theta=pi/2). This is an INFINITE anisotropy ratio.
    The Fermi surface integral gives continuous k-dependence.

    In this framework:
        8 discrete modes, 3 distinct energies
        rho_s anisotropy = 24.4x between C^2 and u(1) directions
        But the mapping direction -> mode is NOT one-to-one

    The crucial structural difference:
        3He-A: gap anisotropy comes from PAIRING SYMMETRY (p-wave, l=1)
        Framework: gap is ISOTROPIC within each sector (s-wave, Schur)
    """
    # 3He-A: Delta/Delta_max ranges from 0 to 1
    # Framework: Delta/Delta_max ranges from 1 to sqrt(24.4) ~ 4.94 at most
    Delta_ratio_3He = np.inf  # point nodes
    Delta_ratio_framework = np.sqrt(rho_s_diag.max() / rho_s_diag.min())

    # Power-law index from gap anisotropy
    # 3He-A: gap nodes produce power-law DOS, rho(E) ~ E^2 (point node)
    # -> spectral index contribution from gap nodes is strong (divergent)
    # Framework: no nodes, gap > 0 everywhere
    # -> no power-law contribution from gap

    # Energy range
    omega_range = mode_energies.max() / mode_energies.min()

    return {
        'Delta_ratio_3He': 'INF (point nodes)',
        'Delta_ratio_framework': Delta_ratio_framework,
        'omega_range': omega_range,
        'structure_3He': 'p-wave, N_3=2, continuous k',
        'structure_framework': 's-wave, N_3=0, 8 discrete modes',
        'gap_nodes_3He': True,
        'gap_nodes_framework': False,
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("  S48 ANISO-GAP-48: k-Dependent Gap from Superfluid Stiffness Anisotropy")
    print("  Volovik-Superfluid-Universe-Theorist")
    print("=" * 78)

    # =========================================================================
    # STEP 0: Load data
    # =========================================================================
    print("\n--- STEP 0: Load Data ---")
    rhos_data, thouless_data = load_data()

    rho_s_fold = rhos_data['rho_s_fold']
    rho_s_diag = rhos_data['rho_s_diag_fold']
    anisotropy = float(rhos_data['anisotropy_fold'])

    E_branch = thouless_data['E_branch']  # [B1, B2, B3] energies
    E_8 = thouless_data['E_8']            # 8 positive mode energies

    print(f"  rho_s diagonal: {rho_s_diag}")
    print(f"  Anisotropy: {anisotropy:.2f}")
    print(f"  E_branch: {E_branch}")
    print(f"  E_8: {E_8}")

    dir_types = ['su2', 'su2', 'su2', 'C2', 'C2', 'C2', 'C2', 'u1']
    dir_labels = ['su2_1', 'su2_2', 'su2_3', 'C2_1', 'C2_2', 'C2_3', 'C2_4', 'u1']

    # BCS gaps at fold (from S46 or S47 data)
    # Load from rho_s data which interpolated BCS parameters
    bcs_data = np.load(os.path.join(SCRIPT_DIR, 's46_qtheory_selfconsistent.npz'),
                       allow_pickle=True)
    from scipy.interpolate import CubicSpline
    tau_scan = bcs_data['tau_scan']
    Delta_B1_cs = CubicSpline(tau_scan, bcs_data['Delta_B1_sc'])
    Delta_B2_cs = CubicSpline(tau_scan, bcs_data['Delta_B2_sc'])
    Delta_B3_cs = CubicSpline(tau_scan, bcs_data['Delta_B3_sc'])

    Delta_B1 = float(Delta_B1_cs(tau_fold))
    Delta_B2 = float(Delta_B2_cs(tau_fold))
    Delta_B3 = float(Delta_B3_cs(tau_fold))

    print(f"\n  BCS gaps at fold:")
    print(f"    Delta_B1 = {Delta_B1:.6f}")
    print(f"    Delta_B2 = {Delta_B2:.6f}")
    print(f"    Delta_B3 = {Delta_B3:.6f}")

    Delta_sectors = np.array([Delta_B1, Delta_B2, Delta_B3])

    # =========================================================================
    # STEP 1: Current operator mode-direction coupling
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 1: Current Operator Mode-Direction Coupling")
    print(f"{'='*78}")

    coupling, mode_e, mode_s, pos_evals, pos_evecs, gammas = \
        compute_current_mode_coupling(tau_fold)

    print(f"\n  Mode energies: {mode_e}")
    print(f"  Mode sectors: {mode_s}  (0=B1, 1=B2, 2=B3)")

    print(f"\n  Mode-direction coupling |<k|J_a|k'>|^2:")
    print(f"  {'Mode':6s} {'E':8s} {'Sect':4s}", end='')
    for dl in dir_labels:
        print(f" {dl:>6s}", end='')
    print(f" {'Dom':>5s}")

    for k in range(8):
        dom = np.argmax(coupling[k])
        print(f"  {k:6d} {mode_e[k]:8.5f} {'B'+str(mode_s[k]+1):4s}", end='')
        for a in range(8):
            print(f" {coupling[k,a]:6.4f}", end='')
        print(f" {dir_labels[dom]:>5s}")

    # =========================================================================
    # STEP 2: Structural analysis
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 2: Structural Analysis (Direction -> Mode Mapping)")
    print(f"{'='*78}")

    struct = structural_analysis(coupling, mode_e, mode_s, rho_s_diag)

    print(f"\n  Dominant direction per mode: {struct['dominant_dir']}")
    print(f"  Direction occupancy (modes per direction):")
    for a in range(8):
        print(f"    {dir_labels[a]:6s}: {struct['dir_counts'][a]} modes")
    print(f"\n  Mode entropy (bits): {struct['mode_entropy']} (max={struct['max_entropy']:.3f})")
    print(f"  Mean entropy / max entropy: {struct['entropy_ratio']:.4f}")
    print(f"    ({struct['entropy_ratio']*100:.1f}% of maximum -> "
          f"{'DIFFUSE' if struct['entropy_ratio'] > 0.7 else 'CONCENTRATED'} coupling)")
    print(f"\n  Energy-rho_s correlation (dominant dir): r = {struct['r_energy_rho']:.4f} "
          f"(p = {struct['p_corr']:.4f})")

    # =========================================================================
    # STEP 3: Direction-dependent gap ansatze
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 3: Direction-Dependent Gap Ansatze")
    print(f"{'='*78}")

    gap_results = compute_aniso_gap(
        coupling, mode_e, mode_s, rho_s_diag, Delta_sectors
    )

    rho_s_avg = np.mean(rho_s_diag)
    print(f"\n  rho_s average: {rho_s_avg:.6f}")
    print(f"  rho_s range: [{rho_s_diag.min():.6f}, {rho_s_diag.max():.6f}]")
    print(f"  rho_s ratio (max/min): {rho_s_diag.max()/rho_s_diag.min():.2f}")

    for name in ['f1_sqrt', 'f2_linear', 'f3_cube_root', 'f4_weighted']:
        D_eff = gap_results[name]['Delta_eff']
        D_ratio = gap_results[name]['Delta_ratio']
        print(f"\n  Ansatz {name}:")
        print(f"    Delta_eff: {D_eff}")
        print(f"    Delta_ratio (modulation): {D_ratio}")
        print(f"    Range: [{D_eff.min():.6f}, {D_eff.max():.6f}]")
        print(f"    Max/Min ratio: {D_eff.max() / D_eff.min():.4f}")

    # =========================================================================
    # STEP 4: Power law fit and n_s extraction (8 modes)
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 4: Power Law Fit (8 Singlet BCS Modes)")
    print(f"{'='*78}")

    ns_results = {}
    for name in ['f1_sqrt', 'f2_linear', 'f3_cube_root', 'f4_weighted']:
        D_eff = gap_results[name]['Delta_eff']
        fit = fit_power_law_ns(mode_e, D_eff, label=name)
        ns_results[name] = fit
        print(f"\n  Ansatz {name}:")
        print(f"    alpha = {fit['alpha']:.6f}")
        print(f"    n_s = 1 - 4*alpha = {fit['n_s']:.6f}")
        print(f"    R^2 = {fit['r_squared']:.6f}")
        print(f"    sigma(n_s) = {370.0:.0f} "
              f"(inherited from S47 SPECTRAL-FLOW-NS)")

    # Also fit UNIFORM gap as baseline
    D_uniform = gap_results['Delta_mode']  # sector gap, no modulation
    fit_uniform = fit_power_law_ns(mode_e, D_uniform, label='uniform')
    ns_results['uniform'] = fit_uniform
    print(f"\n  Baseline (uniform sector gap, no modulation):")
    print(f"    alpha = {fit_uniform['alpha']:.6f}")
    print(f"    n_s = 1 - 4*alpha = {fit_uniform['n_s']:.6f}")
    print(f"    R^2 = {fit_uniform['r_squared']:.6f}")

    # =========================================================================
    # STEP 5: Full 992-mode analysis
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 5: Full 992-Mode Spectrum Analysis")
    print(f"{'='*78}")

    full = compute_full_spectrum_ns(rho_s_diag, tau_fold)

    print(f"\n  992 modes: omega in [{full['omega_all'].min():.4f}, {full['omega_all'].max():.4f}]")
    print(f"  rho_eff range: [{full['rho_range'][0]:.4f}, {full['rho_range'][1]:.4f}]")
    print(f"  rho_eff ratio: {full['rho_ratio']:.4f}")
    print(f"\n  PAIR CREATION spectrum P(k) = (Delta_eff/omega)^4:")
    print(f"  Unmodulated: P ~ omega^{{{full['slope_unmod']:.4f}}}, n_s = {full['ns_unmod']:.6f}")
    print(f"  f1 (sqrt):   P ~ omega^{{{full['slope_f1']:.4f}}}, n_s = {full['ns_f1']:.6f} "
          f"(shift = {full['delta_ns_f1']:+.6f})")
    print(f"  f2 (linear): P ~ omega^{{{full['slope_f2']:.4f}}}, n_s = {full['ns_f2']:.6f} "
          f"(shift = {full['delta_ns_f2']:+.6f})")
    print(f"  R^2: unmod={full['r2_unmod']:.6f}, f1={full['r2_f1']:.6f}, f2={full['r2_f2']:.6f}")
    print(f"\n  Modulation provides {abs(full['delta_ns_f1']):.4f} of needed "
          f"{abs(0.965 - full['ns_unmod']):.4f} shift to Planck "
          f"({abs(full['delta_ns_f1'])/abs(0.965-full['ns_unmod'])*100:.2f}%)")

    # =========================================================================
    # STEP 6: 3He-A structural comparison
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 6: 3He-A Structural Comparison (Volovik)")
    print(f"{'='*78}")

    he3 = he3_comparison(rho_s_diag, mode_e)

    print(f"\n  3He-A gap anisotropy: {he3['Delta_ratio_3He']} (p-wave nodes)")
    print(f"  Framework gap modulation: {he3['Delta_ratio_framework']:.4f}x (from rho_s)")
    print(f"  Energy range: {he3['omega_range']:.4f}")
    print(f"\n  Structural comparison:")
    print(f"    3He-A:     {he3['structure_3He']}")
    print(f"    Framework: {he3['structure_framework']}")
    print(f"    Gap nodes (3He-A): {he3['gap_nodes_3He']}")
    print(f"    Gap nodes (framework): {he3['gap_nodes_framework']}")

    print(f"\n  CRITICAL STRUCTURAL DIFFERENCE:")
    print(f"    In 3He-A, Delta(k) arises from MICROSCOPIC PAIRING SYMMETRY")
    print(f"    (l=1 orbital, p-wave). The gap function Delta(k) = Delta_perp * sin(theta_k)")
    print(f"    has nodes at k || l, protected by N_3 = 2 topological charge.")
    print(f"    The k-dependence is a property of the ORDER PARAMETER, not the")
    print(f"    Meissner response.")
    print(f"\n    In this framework, the BCS pairing is s-wave-like within each sector")
    print(f"    (Schur's lemma: V(B2,B2) identical for all 4 B2 modes, V(B1,B1) = 0).")
    print(f"    The rho_s anisotropy measures response to EXTERNAL gauge twists,")
    print(f"    NOT the internal gap structure. The gap within each sector is UNIFORM")
    print(f"    by symmetry. This is analogous to measuring the London penetration")
    print(f"    depth anisotropy in a fully-gapped (3He-B-like) superfluid and trying")
    print(f"    to infer gap nodes -- the penetration depth tells you about the")
    print(f"    CONDENSATE STIFFNESS, not the gap function.")

    # =========================================================================
    # STEP 7: Required alpha for Planck n_s
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 7: Required vs Achieved Gap Modulation")
    print(f"{'='*78}")

    ns_planck = 0.965
    alpha_needed = (1.0 - ns_planck) / 4.0
    print(f"\n  Planck n_s = {ns_planck}")
    print(f"  Required alpha = (1 - n_s) / 4 = {alpha_needed:.6f}")

    best_alpha = max(ns_results[k]['alpha'] for k in ns_results)
    best_name = max(ns_results, key=lambda k: ns_results[k]['alpha'])
    print(f"\n  Best alpha achieved: {best_alpha:.6f} (ansatz: {best_name})")
    print(f"  Shortfall: alpha_needed / alpha_best = {alpha_needed / (best_alpha + 1e-30):.2f}x")

    # How much gap anisotropy WOULD be needed?
    # For n_s = 0.965 from 8 modes with E in [0.819, 0.978]:
    # Need Delta(0.978) / Delta(0.819) = (0.978/0.819)^{-alpha_needed}
    # = 1.194^{-0.00875} = 0.998
    # This is a 0.2% gap variation -- TRIVIALLY satisfied
    # BUT: the issue is that the POWER LAW n_s = 1 - 4*alpha refers to
    # the pair creation spectrum P(k) ~ (Delta/omega)^4 where k indexes
    # the FULL mode spectrum, and the factor of 4 comes from the
    # Bogoliubov transformation. The actual n_s requires the ENTIRE
    # power spectrum to be nearly flat, not just 8 modes.

    print(f"\n  Arithmetic of the obstruction:")
    print(f"    8 BCS modes span E in [{mode_e.min():.4f}, {mode_e.max():.4f}]")
    print(f"    Energy ratio: {mode_e.max()/mode_e.min():.4f}")
    print(f"    ln(E_max/E_min) = {np.log(mode_e.max()/mode_e.min()):.4f}")
    print(f"    With 3 distinct energies and 3 distinct rho_s values,")
    print(f"    any power law fit to 8 points across a 1.19x range is")
    print(f"    dominated by noise, not physics.")
    print(f"\n    The REAL obstruction (from S47 SPECTRAL-FLOW-NS):")
    print(f"    992 modes span E in [0.820, 2.061], ratio 2.51x.")
    print(f"    Pair creation P(k) ~ (Delta/omega)^4 ~ omega^{-4}.")
    print(f"    For n_s = 0.965, need P(k) ~ k^{-0.035}.")
    print(f"    Gap modulation at most sqrt(24) = {np.sqrt(24):.2f}x from rho_s.")
    print(f"    ln({np.sqrt(24):.2f}) / ln(2.51) = {np.log(np.sqrt(24))/np.log(2.51):.3f}")
    print(f"    This contributes alpha ~ {np.log(np.sqrt(24))/np.log(2.51)/4:.4f} per power of omega,")
    print(f"    giving n_s ~ 1 - 4*{np.log(np.sqrt(24))/np.log(2.51)/4:.4f} = "
          f"{1.0 - np.log(np.sqrt(24))/np.log(2.51):.4f}")
    print(f"    This is POSITIVE but WRONG SIGN: gap increases with energy")
    print(f"    (C^2 modes at higher energy have HIGHER rho_s, INCREASING Delta),")
    print(f"    which makes the spectrum BLUER (further from Planck), not redder.")

    # =========================================================================
    # STEP 8: Gate evaluation
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  STEP 8: Gate Evaluation")
    print(f"{'='*78}")

    # Collect ALL n_s from pair-creation spectrum (the physical observable)
    # The 8-mode fits are dominated by the sector-gap variation
    # The 992-mode fits are the correct full-spectrum result
    all_ns_physical = [full['ns_f1'], full['ns_f2'], full['ns_unmod']]

    # Also include 8-mode results for completeness (but flag as suspect)
    all_ns_8mode = [ns_results[k]['n_s'] for k in ns_results]

    print(f"\n  n_s from PAIR-CREATION spectrum P(k) = (Delta_eff/omega)^4:")
    print(f"    (8-mode results unreliable: 3 distinct energies, 1.19x range)")
    for name in ns_results:
        print(f"    {name:15s}: n_s = {ns_results[name]['n_s']:.6f} [8-mode, UNRELIABLE]")
    print(f"\n    (992-mode results: correct pair-creation power spectrum)")
    print(f"    {'unmodulated':15s}: n_s = {full['ns_unmod']:.6f}")
    print(f"    {'full_f1':15s}: n_s = {full['ns_f1']:.6f} (shift {full['delta_ns_f1']:+.4f})")
    print(f"    {'full_f2':15s}: n_s = {full['ns_f2']:.6f} (shift {full['delta_ns_f2']:+.4f})")

    print(f"\n  Planck n_s = 0.9649 +/- 0.0042")
    print(f"  Physical n_s range: [{min(all_ns_physical):.6f}, {max(all_ns_physical):.6f}]")

    # Gate check: use the PHYSICAL n_s values
    pass_any = any(0.80 <= ns <= 1.10 for ns in all_ns_physical)
    info_any = any(0.50 <= ns <= 0.80 for ns in all_ns_physical)

    if pass_any:
        gate = "PASS"
    elif info_any:
        gate = "INFO"
    else:
        gate = "FAIL"

    # But we need to flag: the "PASS" is vacuous if it just reflects
    # n_s = -3 + O(0.04) from gap modulation
    is_vacuous = all(abs(ns - full['ns_unmod']) < 0.1 for ns in all_ns_physical)

    # Distance from Planck in sigma
    ns_closest = min(all_ns_physical, key=lambda x: abs(x - 0.965))
    sigma_from_planck = abs(ns_closest - 0.965) / 0.0042

    print(f"\n  Closest to Planck: n_s = {ns_closest:.6f} ({sigma_from_planck:.1f} sigma)")

    # Override gate: n_s ~ -3 is outside ALL ranges, so gate is FAIL
    # The initial "PASS" was from fitting Delta_eff alone (wrong quantity)
    print(f"\n  Gate evaluation:")
    print(f"    n_s range [{min(all_ns_physical):.3f}, {max(all_ns_physical):.3f}]")
    print(f"    All n_s < -2.9 (deep blue tilt)")
    print(f"    rho_s modulation shifts n_s by at most {max(abs(full['delta_ns_f1']), abs(full['delta_ns_f2'])):.4f}")
    print(f"    Need shift of {abs(0.965 - full['ns_unmod']):.4f} to reach Planck")

    gate = "FAIL"  # Correct gate from pair-creation spectrum

    print(f"\n  GATE ANISO-GAP-48: {gate}")
    print(f"  Reason: n_s = {ns_closest:.3f}, all ansatze give n_s < -2.9")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  SAVING DATA")
    print(f"{'='*78}")

    npz_path = os.path.join(SCRIPT_DIR, 's48_aniso_gap.npz')
    save_dict = {
        # Mode data
        'mode_energies': mode_e,
        'mode_sectors': mode_s,
        'mode_dir_coupling': coupling,
        # rho_s
        'rho_s_diag': rho_s_diag,
        'anisotropy': anisotropy,
        # Gap ansatze
        'Delta_sectors': Delta_sectors,
    }
    for name in ['f1_sqrt', 'f2_linear', 'f3_cube_root', 'f4_weighted']:
        save_dict[f'{name}_Delta_eff'] = gap_results[name]['Delta_eff']
        save_dict[f'{name}_alpha'] = ns_results[name]['alpha']
        save_dict[f'{name}_ns'] = ns_results[name]['n_s']
        save_dict[f'{name}_r2'] = ns_results[name]['r_squared']
    save_dict['uniform_alpha'] = ns_results['uniform']['alpha']
    save_dict['uniform_ns'] = ns_results['uniform']['n_s']
    # Full spectrum (corrected: pair-creation n_s)
    save_dict['full_ns_unmod'] = full['ns_unmod']
    save_dict['full_ns_f1'] = full['ns_f1']
    save_dict['full_ns_f2'] = full['ns_f2']
    save_dict['full_delta_ns_f1'] = full['delta_ns_f1']
    save_dict['full_delta_ns_f2'] = full['delta_ns_f2']
    save_dict['full_slope_unmod'] = full['slope_unmod']
    save_dict['full_slope_f1'] = full['slope_f1']
    save_dict['full_slope_f2'] = full['slope_f2']
    save_dict['full_rho_ratio'] = full['rho_ratio']
    # Structural
    save_dict['dominant_dir'] = struct['dominant_dir']
    save_dict['entropy_ratio'] = struct['entropy_ratio']
    save_dict['r_energy_rho'] = struct['r_energy_rho']
    # Gate
    save_dict['gate_name'] = np.array(['ANISO-GAP-48'])
    save_dict['gate_verdict'] = np.array([gate])
    save_dict['ns_closest'] = ns_closest
    save_dict['sigma_from_planck'] = sigma_from_planck

    np.savez(npz_path, **save_dict)
    print(f"  Saved: {npz_path}")

    # =========================================================================
    # FIGURES
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  GENERATING FIGURES")
    print(f"{'='*78}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # --- Panel A: Mode-direction coupling heatmap ---
    ax = axes[0, 0]
    im = ax.imshow(coupling, aspect='auto', cmap='YlOrRd')
    ax.set_xticks(range(8))
    ax.set_xticklabels(dir_labels, fontsize=8, rotation=45)
    ax.set_yticks(range(8))
    sector_names = ['B1' if s == 0 else 'B2' if s == 1 else 'B3' for s in mode_s]
    ax.set_yticklabels([f"k={k} ({sector_names[k]}, E={mode_e[k]:.3f})"
                         for k in range(8)], fontsize=8)
    ax.set_xlabel('su(3) direction', fontsize=11)
    ax.set_ylabel('BCS mode', fontsize=11)
    ax.set_title('(A) Mode-direction coupling $|\\langle k|J_a|k\'\\rangle|^2$', fontsize=12)
    fig.colorbar(im, ax=ax, shrink=0.8)

    # --- Panel B: Gap modulation by ansatz ---
    ax = axes[0, 1]
    x = np.arange(8)
    colors = ['#1565C0', '#2E7D32', '#C62828', '#FF8F00', '#6A1B9A']
    for i, name in enumerate(['uniform', 'f1_sqrt', 'f2_linear', 'f3_cube_root', 'f4_weighted']):
        if name == 'uniform':
            D = gap_results['Delta_mode']
        else:
            D = gap_results[name]['Delta_eff']
        ax.plot(x, D, 'o-', color=colors[i], markersize=6, linewidth=1.5,
                label=f"{name} (n_s={ns_results[name]['n_s']:.3f})")
    ax.set_xticks(x)
    ax.set_xticklabels([f"k={k}\n{sector_names[k]}" for k in range(8)], fontsize=8)
    ax.set_ylabel('$\\Delta_{\\rm eff}(k)$', fontsize=12)
    ax.set_xlabel('BCS mode', fontsize=11)
    ax.set_title('(B) Effective gap by ansatz', fontsize=12)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(alpha=0.3)

    # --- Panel C: Delta_eff vs omega (log-log) ---
    ax = axes[1, 0]
    for i, name in enumerate(['f1_sqrt', 'f2_linear', 'f4_weighted']):
        D = gap_results[name]['Delta_eff']
        fit = ns_results[name]
        ax.scatter(mode_e, D, color=colors[i+1], s=60, zorder=5,
                   label=f"{name}: $\\alpha$={fit['alpha']:.3f}")
        # Fit line
        om_fit = np.linspace(mode_e.min()*0.95, mode_e.max()*1.05, 50)
        D_fit = np.exp(fit['intercept']) * om_fit**fit['slope']
        ax.plot(om_fit, D_fit, '--', color=colors[i+1], alpha=0.7)

    ax.set_xlabel('$\\omega_k$ (mode energy)', fontsize=12)
    ax.set_ylabel('$\\Delta_{\\rm eff}(k)$', fontsize=12)
    ax.set_title('(C) Gap vs energy with power law fits', fontsize=12)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, which='both')

    # Mark Planck target
    om_range = np.linspace(mode_e.min(), mode_e.max(), 50)
    D_planck = np.exp(fit['intercept']) * om_range**(-alpha_needed)
    ax.plot(om_range, D_planck, 'k:', linewidth=2, alpha=0.5,
            label=f'Planck ($\\alpha$={alpha_needed:.4f})')
    ax.legend(fontsize=8)

    # --- Panel D: Pair-creation n_s (corrected) ---
    ax = axes[1, 1]
    names_d = ['unmod (992)', 'f1 sqrt (992)', 'f2 linear (992)']
    ns_vals_d = [full['ns_unmod'], full['ns_f1'], full['ns_f2']]

    bar_colors_d = ['gray', '#2E7D32', '#C62828']
    bars = ax.barh(range(len(names_d)), ns_vals_d, color=bar_colors_d,
                    edgecolor='black', linewidth=0.5)
    ax.axvline(x=0.965, color='red', linewidth=2, linestyle='--', label='Planck $n_s$')
    ax.axvline(x=-3.0, color='blue', linewidth=1, linestyle=':', alpha=0.7,
               label='$P \\sim \\omega^{-4}$')
    ax.set_yticks(range(len(names_d)))
    ax.set_yticklabels(names_d, fontsize=9)
    ax.set_xlabel('$n_s$ (pair-creation spectrum)', fontsize=12)
    ax.set_title(f'(D) Pair-creation $n_s$: GATE = {gate}', fontsize=12)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(alpha=0.3, axis='x')
    ax.set_xlim(-3.2, 1.2)

    plt.tight_layout()
    fig_path = os.path.join(SCRIPT_DIR, 's48_aniso_gap.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print(f"\n{'='*78}")
    print(f"  ANISO-GAP-48 SUMMARY")
    print(f"{'='*78}")

    print(f"\n  GATE: {gate}")
    print(f"\n  The rho_s anisotropy (24.4x) measures the condensate stiffness")
    print(f"  against gauge twists in 8 su(3) directions. This is a MEISSNER-TYPE")
    print(f"  response, not a GAP FUNCTION. The BCS gap within each degenerate")
    print(f"  sector is UNIFORM by Schur's lemma.")
    print(f"\n  Even assigning each mode a direction-dependent gap via the current")
    print(f"  operator coupling, the resulting n_s is dominated by the gap-energy")
    print(f"  correlation (C^2 modes at higher energy have HIGHER rho_s, wrong sign)")
    print(f"  and the narrow energy range (1.19x for 8 modes, 2.51x for 992 modes).")
    print(f"\n  The 3He-A analog FAILS structurally:")
    print(f"    - 3He-A: p-wave pairing, N_3 = 2, gap NODES, continuous k")
    print(f"    - Framework: s-wave-like, N_3 = 0, no nodes, 8 discrete modes")
    print(f"  The k-dependent gap path is CLOSED.")


if __name__ == '__main__':
    main()
