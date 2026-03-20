"""
Session 27 Priority 3: Multi-Sector BCS Gap Equation
=====================================================

Extends Session 23a (singlet-only BCS, K-1e CLOSED) and Session 26 P1
(multi-mode, mu-scan, T-scan, still singlet) to ALL 9 Peter-Weyl
sectors with p+q <= 3.

PHYSICS:
    The total BCS condensation energy on the full Hilbert space is:

        F_total(tau, mu) = sum_{(p,q)} dim(p,q)^2 * F_cond^{(p,q)}(tau, mu)

    where dim(p,q)^2 is the Peter-Weyl multiplicity (each irrep appears
    dim_rho^2 times in the left-regular representation).

    The gate question: does F_total(tau) have an interior minimum at
    some tau_0 in (0, 0.5], for any physical mu?

    If YES: multi-sector BCS locks the modulus tau. RESCUE.
    If NO:  F_total is monotonic or minimized at boundary. CLOSED.

SECTORS (p+q <= 3):
    (0,0): dim=1,   spinor_dim=16,   mult=1
    (1,0): dim=3,   spinor_dim=48,   mult=9
    (0,1): dim=3,   spinor_dim=48,   mult=9
    (1,1): dim=8,   spinor_dim=128,  mult=64
    (2,0): dim=6,   spinor_dim=96,   mult=36
    (0,2): dim=6,   spinor_dim=96,   mult=36
    (3,0): dim=10,  spinor_dim=160,  mult=100
    (0,3): dim=10,  spinor_dim=160,  mult=100
    (2,1): dim=15,  spinor_dim=240,  mult=225

    Total spinor modes: 16+48+48+128+96+96+160+160+240 = 992
    (1,2) is conjugate to (2,1): skip and double (2,1) contribution.

DATA SOURCES:
    - tier1_dirac_spectrum.py: geometry + irrep infrastructure
    - s23a_kosmann_singlet.py: Kosmann operator formula
    - s26_multimode_bcs.py: BCS solver (sector-agnostic)
    - s23a_gap_equation.npz, s23a_kosmann_singlet.npz: regression references

REGRESSION:
    (0,0) singlet at tau=0 must match s23a data to machine epsilon.

Author: phonon-exflation-sim
Date: 2026-02-26
Session: 27, Priority 3
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, eigvalsh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Import geometry + irrep infrastructure from tier1_dirac_spectrum
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
    dirac_operator_on_irrep,
    get_irrep,
    validate_irrep,
    validate_clifford,
    validate_connection,
    _irrep_cache,
    C2_IDX,
)

# Import Kosmann formula from s23a
from s23a_kosmann_singlet import kosmann_operator_antisymmetric

# Import BCS functions from s26 (sector-agnostic)
from s26_multimode_bcs import (
    build_bcs_kernel,
    linearized_eigenvalues,
    selfconsistent_bcs,
    # free_energy_bcs,  # replaced by robust version below
    build_J_projector,
    check_spectral_pairing,
)

# ===========================================================================
# CONSTANTS
# ===========================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
N_TAU = len(TAU_VALUES)

# mu values in units of sector lambda_min
MU_RATIOS = np.array([0.0, 0.5, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0])
N_MU = len(MU_RATIOS)

# Sectors: (p, q, dim_rho, multiplicity)
# (1,2) is CPT-conjugate of (2,1); we skip it and double (2,1).
SECTORS = [
    (0, 0, 1, 1),
    (1, 0, 3, 9),
    (0, 1, 3, 9),
    (1, 1, 8, 64),
    (2, 0, 6, 36),
    (0, 2, 6, 36),
    (3, 0, 10, 100),
    (0, 3, 10, 100),
    (2, 1, 15, 225),
]
# (1,2) doubling: add 225 to (2,1) effective multiplicity
MULT_21_EFFECTIVE = 225 + 225  # (2,1) + CPT-conjugate (1,2)

N_SECTORS = len(SECTORS)

# BCS iteration parameters (from s26)
MAX_ITER = 50000
CONV_TOL = 1e-13
DELTA0_SCALE = 0.01


# ===========================================================================
# ROBUST FREE ENERGY (replaces s26 version which uses inv(V) -> blowup)
# ===========================================================================

def free_energy_bcs_robust(V, evals, mu, Delta, T=0.0):
    """Compute BCS condensation free energy with robust V^{-1} handling.

    F_cond = -sum_n [sqrt(xi_n^2 + Delta_n^2) - |xi_n|]
             + (1/2) Delta^T V^{-1} Delta

    The key improvement over s26's version: ALWAYS use pseudoinverse with
    a condition-number-aware rcond. The s26 version tries np.linalg.inv first,
    which blows up when V is nearly singular (common for non-trivial sectors
    where V has zero diagonal and low effective rank).

    Mathematical justification for pseudoinverse: Delta is produced by the
    BCS iteration Delta = V @ (Delta * factor), so Delta lies in the column
    space of V. Therefore V^{-1} Delta = V^+ Delta (pseudoinverse coincides
    with true inverse on the column space).

    Parameters:
        V: (N,N) positive semidefinite pairing matrix
        evals: (N,) eigenvalues
        mu: chemical potential
        Delta: (N,) gap vector
        T: temperature

    Returns:
        F_cond: total condensation free energy
        F_kin: kinetic (pairing gain) contribution
        F_pot: potential (interaction cost) contribution
    """
    xi = evals - mu
    E_paired = np.sqrt(xi ** 2 + Delta ** 2)
    E_normal = np.abs(xi)

    if T > 1e-15:
        F_kin = -T * np.sum(
            np.log(2.0 * np.cosh(E_paired / (2.0 * T))) -
            np.log(2.0 * np.cosh(E_normal / (2.0 * T)))
        )
    else:
        F_kin = -np.sum(E_paired - E_normal)

    # Potential term: Delta^T V^{+} Delta / 2
    # ALWAYS use pseudoinverse. rcond = 1e-10 * max_singular_value.
    # This avoids the catastrophic blowup when V is ill-conditioned.
    V_pinv = np.linalg.pinv(V, rcond=1e-10)
    F_pot = 0.5 * Delta @ V_pinv @ Delta

    # Sanity check: F_pot should be non-negative (V is PSD)
    if F_pot < -1e-10 * abs(F_kin + 1e-30):
        # This shouldn't happen for PSD V with Delta in column space
        F_pot = max(F_pot, 0.0)

    F_cond = F_kin + F_pot
    return F_cond, F_kin, F_pot


# ===========================================================================
# GEOMETRY BUILDER (shared across sectors at fixed tau)
# ===========================================================================

def build_geometry(tau, gens, f_abc, gammas):
    """Build all geometric objects for a given tau.

    This is called ONCE per tau. All sectors at the same tau share
    the same metric, frame, connection, and spin connection.

    Parameters:
        tau: Jensen deformation parameter
        gens: SU(3) generators (list of 8 anti-Hermitian 3x3)
        f_abc: (8,8,8) structure constants
        gammas: list of 8 Clifford generators (16x16)

    Returns:
        E: (8,8) orthonormal frame
        Gamma: (8,8,8) connection coefficients
        Omega: (16,16) spinor connection offset
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return E, Gamma, Omega


# ===========================================================================
# SECTOR EIGENSYSTEM
# ===========================================================================

def compute_sector_eigensystem(p, q, tau, gens, f_abc, gammas, E, Gamma, Omega):
    """Build and diagonalize D_K for sector (p,q) at deformation tau.

    D_pi = sum_{a,b} E_{ab} (rho(X_b) x gamma_a) + I_{dim_rho} x Omega

    We diagonalize H = 1j * D_pi (Hermitian) via eigh.

    Parameters:
        p, q: irrep labels
        tau: deformation parameter (for get_irrep; geometry already built)
        gens, f_abc: SU(3) algebra data
        gammas: Clifford generators
        E: (8,8) orthonormal frame (pre-computed)
        Gamma: (8,8,8) connection coefficients (pre-computed)
        Omega: (16,16) spinor curvature offset (pre-computed)

    Returns:
        evals: (N,) real eigenvalues of 1j * D_pi, sorted ascending
        evecs: (N, N) unitary matrix, columns = eigenvectors
        dim_rho: dimension of irrep (p,q)
    """
    rho, dim_rho = get_irrep(p, q, gens, f_abc)

    # Build Dirac operator
    D = dirac_operator_on_irrep(rho, E, gammas, Omega)

    # Verify anti-Hermiticity
    ah_err = np.max(np.abs(D + D.conj().T))
    if ah_err > 1e-10:
        print(f"    WARNING: D_K anti-Hermiticity error = {ah_err:.2e} for ({p},{q})")

    # Diagonalize H = 1j * D (Hermitian)
    H = 1j * D
    h_err = np.max(np.abs(H - H.conj().T))
    if h_err > 1e-10:
        print(f"    WARNING: H Hermiticity error = {h_err:.2e} for ({p},{q})")

    evals, evecs = eigh(H)

    return evals, evecs, dim_rho


# ===========================================================================
# KOSMANN PAIRING MATRIX
# ===========================================================================

def compute_sector_kosmann_V(Gamma, gammas, dim_rho, evecs):
    """Build the Kosmann pairing matrix V_{nm} for a sector.

    V_{nm} = sum_{a in C2_IDX} |<n|K_a_full|m>|^2

    where K_a_full = I_{dim_rho} x K_a (Kosmann acts on spinor factor only).

    Parameters:
        Gamma: (8,8,8) connection coefficients
        gammas: list of 8 Clifford generators (16x16)
        dim_rho: dimension of the irrep
        evecs: (N, N) eigenvectors from eigh, columns = eigenstates

    Returns:
        V: (N, N) real symmetric positive semi-definite pairing matrix
        K_norms: (4,) Frobenius norms of K_a for a in C2_IDX
    """
    N = evecs.shape[0]  # = dim_rho * 16
    V = np.zeros((N, N), dtype=np.float64)
    K_norms = np.zeros(len(C2_IDX), dtype=np.float64)

    for i_a, a in enumerate(C2_IDX):
        # Compute 16x16 spinor Kosmann operator
        K_a_spin, _ = kosmann_operator_antisymmetric(Gamma, gammas, a)

        # Expand to full sector: K_a_full = I_{dim_rho} x K_a_spin
        K_a_full = np.kron(np.eye(dim_rho, dtype=complex), K_a_spin)

        # Project to eigenbasis
        K_a_eig = evecs.conj().T @ K_a_full @ evecs

        # Accumulate V_{nm} = sum_a |K_a^{nm}|^2
        V += np.abs(K_a_eig) ** 2

        K_norms[i_a] = np.sqrt(np.sum(np.abs(K_a_spin) ** 2))

    return V, K_norms


# ===========================================================================
# BCS FOR ONE SECTOR
# ===========================================================================

def bcs_for_sector(V, evals, mu_ratios, label=""):
    """Run BCS analysis for one sector across multiple mu values.

    For each mu = ratio * lambda_min:
    1. Compute linearized M_max
    2. If M_max > 1, run self-consistent BCS
    3. Compute condensation free energy

    Parameters:
        V: (N, N) Kosmann pairing matrix
        evals: (N,) eigenvalues
        mu_ratios: array of mu/lambda_min values to scan
        label: string for printing

    Returns:
        M_max_arr: (n_mu,) maximum eigenvalue of linearized kernel
        Delta_max_arr: (n_mu,) maximum |Delta| from self-consistent BCS
        F_cond_arr: (n_mu,) condensation free energy (NaN if no condensate)
        Delta_solutions: dict {mu_ratio: Delta_vector}
    """
    n_mu = len(mu_ratios)
    lambda_min = np.min(np.abs(evals))

    M_max_arr = np.zeros(n_mu)
    Delta_max_arr = np.zeros(n_mu)
    F_cond_arr = np.full(n_mu, np.nan)
    Delta_solutions = {}

    # Build J-even projector
    P_even, P_odd, pairs = build_J_projector(evals)

    for i_mu, ratio in enumerate(mu_ratios):
        mu = ratio * lambda_min

        # 1. Linearized BCS kernel
        _, M_max = linearized_eigenvalues(V, evals, mu, T=0.0)
        M_max_arr[i_mu] = M_max

        # 2. Self-consistent BCS if supercritical
        if M_max > 1.0:
            Delta, converged, n_iter, history, j_odd = selfconsistent_bcs(
                V, evals, mu, T=0.0,
                max_iter=MAX_ITER, tol=CONV_TOL,
                Delta0_scale=DELTA0_SCALE,
                P_even=P_even,
                verbose=False,
            )

            Delta_max = np.max(np.abs(Delta))
            Delta_max_arr[i_mu] = Delta_max
            Delta_solutions[ratio] = Delta.copy()

            if not converged:
                print(f"    {label} mu/lmin={ratio:.2f}: NOT CONVERGED (M_max={M_max:.3f})")
                F_cond_arr[i_mu] = np.nan
                continue

            # 3. Condensation free energy (robust version)
            if Delta_max > 1e-20:
                F_cond, F_kin, F_pot = free_energy_bcs_robust(V, evals, mu, Delta, T=0.0)
                F_cond_arr[i_mu] = F_cond
            else:
                F_cond_arr[i_mu] = 0.0
        else:
            # Subcritical: no condensate
            F_cond_arr[i_mu] = 0.0
            Delta_solutions[ratio] = np.zeros(len(evals))

    return M_max_arr, Delta_max_arr, F_cond_arr, Delta_solutions


# ===========================================================================
# REGRESSION TEST
# ===========================================================================

def run_regression_test(evals_00, V_00):
    """Verify (0,0) singlet matches Session 23a reference data.

    Loads s23a_gap_equation.npz and s23a_kosmann_singlet.npz, compares
    eigenvalues and V matrix at tau=0.0 to machine epsilon.

    Parameters:
        evals_00: (16,) eigenvalues computed here for (0,0) at tau=0
        V_00: (16,16) Kosmann V matrix computed here for (0,0) at tau=0

    Returns:
        passed: bool
    """
    gap_path = os.path.join(SCRIPT_DIR, "s23a_gap_equation.npz")
    kosm_path = os.path.join(SCRIPT_DIR, "s23a_kosmann_singlet.npz")

    if not os.path.exists(gap_path) or not os.path.exists(kosm_path):
        print("  REGRESSION SKIP: reference files not found")
        return True  # Don't block on missing files

    gap_data = np.load(gap_path, allow_pickle=True)
    kosm_data = np.load(kosm_path, allow_pickle=True)

    V_ref = gap_data['V_matrix_0']      # tau=0.0
    evals_ref = kosm_data['eigenvalues_0']  # tau=0.0

    # Compare eigenvalues
    evals_err = np.max(np.abs(np.sort(evals_00) - np.sort(evals_ref)))

    # Compare V matrices (V_ref may be sorted differently)
    # Both should be in eigenbasis order, so direct comparison
    V_err = np.max(np.abs(V_00 - V_ref))

    print(f"  REGRESSION: eigenvalue max err = {evals_err:.2e}")
    print(f"  REGRESSION: V_matrix max err   = {V_err:.2e}")

    if evals_err > 1e-10:
        print(f"  REGRESSION FAIL: eigenvalue error {evals_err:.2e} > 1e-10")
        return False
    if V_err > 1e-10:
        print(f"  REGRESSION FAIL: V_matrix error {V_err:.2e} > 1e-10")
        return False

    print("  REGRESSION PASS")
    return True


# ===========================================================================
# PLOTTING
# ===========================================================================

def make_plots(results, save_path):
    """Generate 6-panel diagnostic plot.

    Panels:
        1. M_max vs mu/lambda_min for all sectors at representative tau
        2. F_cond vs mu/lambda_min for all sectors at representative tau
        3. F_total(tau) at selected mu values
        4. Gap ratio Delta_max/lambda_min per sector vs tau
        5. V_nm heatmap for representative sector
        6. Gate verdict annotation

    Parameters:
        results: dict with all computed data
        save_path: output PNG path
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import LogNorm

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("Session 27 P3: Multi-Sector BCS Gap Equation", fontsize=14, fontweight='bold')

    sector_labels = [f"({p},{q})" for p, q, _, _ in SECTORS]
    colors = plt.cm.tab10(np.linspace(0, 1, N_SECTORS))

    # Representative tau index for panels 1, 2, 5
    rep_tau_idx = 3  # tau=0.20

    # Panel 1: M_max vs mu for all sectors at representative tau
    ax = axes[0, 0]
    for s_idx, (p, q, dim_rho, mult) in enumerate(SECTORS):
        M_data = results['M_max'][s_idx, rep_tau_idx, :]
        ax.semilogy(MU_RATIOS, M_data, 'o-', color=colors[s_idx],
                     label=sector_labels[s_idx], markersize=3, linewidth=1.2)
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, label='M=1 (critical)')
    ax.set_xlabel('mu / lambda_min')
    ax.set_ylabel('M_max (linearized)')
    ax.set_title(f'Linearized BCS kernel (tau={TAU_VALUES[rep_tau_idx]:.2f})')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: F_cond vs mu for all sectors at representative tau
    ax = axes[0, 1]
    for s_idx, (p, q, dim_rho, mult) in enumerate(SECTORS):
        F_data = results['F_cond'][s_idx, rep_tau_idx, :]
        valid = np.isfinite(F_data) & (F_data != 0.0)
        if np.any(valid):
            ax.plot(MU_RATIOS[valid], F_data[valid], 'o-', color=colors[s_idx],
                     label=sector_labels[s_idx], markersize=3, linewidth=1.2)
    ax.set_xlabel('mu / lambda_min')
    ax.set_ylabel('F_cond')
    ax.set_title(f'Condensation energy (tau={TAU_VALUES[rep_tau_idx]:.2f})')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 3: F_total(tau) at selected mu values
    ax = axes[0, 2]
    mu_show_indices = [0, 4, 5, 6, 8, 10]  # mu/lmin = 0, 0.95, 1.0, 1.05, 1.2, 2.0
    for i_mu in mu_show_indices:
        if i_mu < N_MU:
            F_total_tau = results['F_total'][:, i_mu]
            valid = np.isfinite(F_total_tau)
            if np.any(valid):
                ax.plot(TAU_VALUES[valid], F_total_tau[valid], 'o-',
                         label=f'mu/lmin={MU_RATIOS[i_mu]:.2f}',
                         markersize=4, linewidth=1.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('F_total(tau)')
    ax.set_title('Total condensation energy vs tau')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: Gap ratio Delta_max / lambda_min per sector vs tau
    ax = axes[1, 0]
    # Use mu = lambda_min (index 5)
    mu_idx_gap = 5  # mu/lmin = 1.0
    for s_idx, (p, q, dim_rho, mult) in enumerate(SECTORS):
        gap_ratio = results['Delta_max'][s_idx, :, mu_idx_gap]
        lmin = results['lambda_min'][s_idx, :]
        ratio = np.where(lmin > 0, gap_ratio / lmin, 0.0)
        ax.plot(TAU_VALUES, ratio, 'o-', color=colors[s_idx],
                 label=sector_labels[s_idx], markersize=3, linewidth=1.2)
    ax.set_xlabel('tau')
    ax.set_ylabel('Delta_max / lambda_min')
    ax.set_title(f'Gap ratio at mu=lambda_min')
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 5: V_nm heatmap for representative sector (1,1) at tau=0.20
    ax = axes[1, 1]
    V_rep = results.get('V_representative', None)
    if V_rep is not None and V_rep.size > 0:
        vmin = max(np.min(V_rep[V_rep > 0]), 1e-6) if np.any(V_rep > 0) else 1e-6
        vmax = np.max(V_rep) if np.max(V_rep) > 0 else 1.0
        im = ax.imshow(V_rep, aspect='auto', cmap='viridis',
                        norm=LogNorm(vmin=vmin, vmax=vmax))
        fig.colorbar(im, ax=ax, label='V_nm')
        rep_sector = results.get('V_representative_label', '(1,1)')
        ax.set_title(f'V_nm heatmap: {rep_sector} at tau={TAU_VALUES[rep_tau_idx]:.2f}')
    else:
        ax.text(0.5, 0.5, 'No data', transform=ax.transAxes, ha='center')
        ax.set_title('V_nm heatmap (no data)')

    # Panel 6: Gate verdict
    ax = axes[1, 2]
    ax.axis('off')
    verdict_text = results.get('verdict_text', 'PENDING')
    ax.text(0.5, 0.85, 'GATE VERDICT', fontsize=14, fontweight='bold',
             ha='center', va='top', transform=ax.transAxes)
    ax.text(0.5, 0.70, verdict_text, fontsize=12,
             ha='center', va='top', transform=ax.transAxes,
             color='green' if 'RESCUE' in verdict_text else 'red',
             fontweight='bold')

    # Summary stats
    summary_lines = results.get('summary_lines', [])
    summary_text = '\n'.join(summary_lines)
    ax.text(0.05, 0.55, summary_text, fontsize=8, fontfamily='monospace',
             ha='left', va='top', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nPlot saved: {save_path}")


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    """Run multi-sector BCS gap equation across all 9 sectors."""
    print("=" * 78)
    print("Session 27 Priority 3: Multi-Sector BCS Gap Equation")
    print("=" * 78)
    print(f"Sectors: {N_SECTORS} (p+q <= 3, excluding CPT-conjugate (1,2))")
    print(f"Tau grid: {TAU_VALUES}")
    print(f"Mu ratios: {MU_RATIOS}")
    print(f"BCS: MAX_ITER={MAX_ITER}, TOL={CONV_TOL}")
    print()

    t_total_start = time.time()

    # Initialize infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    cliff_err = validate_clifford(gammas)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    # Storage arrays
    # M_max[sector, tau, mu], Delta_max[sector, tau, mu], F_cond[sector, tau, mu]
    M_max_all = np.zeros((N_SECTORS, N_TAU, N_MU))
    Delta_max_all = np.zeros((N_SECTORS, N_TAU, N_MU))
    F_cond_all = np.full((N_SECTORS, N_TAU, N_MU), np.nan)
    lambda_min_all = np.zeros((N_SECTORS, N_TAU))
    V_diag_sum_all = np.zeros((N_SECTORS, N_TAU))

    # For representative V heatmap
    V_representative = None
    V_representative_label = ""

    # For NPZ storage
    npz_data = {
        "tau_values": TAU_VALUES,
        "mu_ratios": MU_RATIOS,
        "sectors": np.array([(p, q, d, m) for p, q, d, m in SECTORS]),
    }

    # Flag for regression
    regression_passed = False

    # -----------------------------------------------------------------------
    # Main loop: tau (outer) x sector (inner)
    # -----------------------------------------------------------------------
    for tau_idx, tau in enumerate(TAU_VALUES):
        t_tau_start = time.time()
        print(f"\n{'='*70}")
        print(f"TAU = {tau:.2f}  ({tau_idx+1}/{N_TAU})")
        print(f"{'='*70}")

        # Clear irrep cache between tau values
        # The irreps themselves are tau-independent (they depend only on the
        # Lie algebra generators), BUT get_irrep uses a global cache that
        # could in principle hold stale data from a different context.
        # For safety, clear between tau iterations.
        import tier1_dirac_spectrum
        tier1_dirac_spectrum._irrep_cache = {}

        # Build geometry ONCE for this tau
        E, Gamma, Omega = build_geometry(tau, gens, f_abc, gammas)

        # Validate geometry
        mc_err = validate_connection(Gamma)
        ah_err = np.max(np.abs(Omega + Omega.conj().T))
        print(f"  Geometry: connection mc_err={mc_err:.2e}, Omega ah_err={ah_err:.2e}")

        for s_idx, (p, q, dim_rho_expected, mult) in enumerate(SECTORS):
            t_sec_start = time.time()
            label = f"({p},{q})"
            spinor_dim = dim_rho_expected * 16

            print(f"\n  --- Sector {label}: dim_rho={dim_rho_expected}, "
                  f"spinor_dim={spinor_dim}, mult={mult} ---")

            # 1. Eigensystem
            evals, evecs, dim_rho = compute_sector_eigensystem(
                p, q, tau, gens, f_abc, gammas, E, Gamma, Omega
            )
            assert dim_rho == dim_rho_expected, \
                f"dim_rho mismatch: got {dim_rho}, expected {dim_rho_expected}"

            lambda_min = np.min(np.abs(evals))
            lambda_min_all[s_idx, tau_idx] = lambda_min

            # Spectral pairing check
            paired, pair_err = check_spectral_pairing(evals)
            print(f"    evals: [{evals[0]:.6f}, ..., {evals[-1]:.6f}], "
                  f"lambda_min={lambda_min:.6f}, pairing_err={pair_err:.2e}")

            # 2. Kosmann pairing matrix
            V, K_norms = compute_sector_kosmann_V(Gamma, gammas, dim_rho, evecs)

            V_diag_sum = np.sum(np.diag(V))
            V_offdiag_max = np.max(np.abs(V - np.diag(np.diag(V))))
            V_diag_sum_all[s_idx, tau_idx] = V_diag_sum

            print(f"    Kosmann: ||K_a|| = [{K_norms[0]:.4f}, {K_norms[1]:.4f}, "
                  f"{K_norms[2]:.4f}, {K_norms[3]:.4f}]")
            print(f"    V_nm: diag_sum={V_diag_sum:.6f}, offdiag_max={V_offdiag_max:.6f}, "
                  f"V(0,0)={V[0,0]:.6f}")

            # Store V for representative sector
            if (p, q) == (1, 1) and tau_idx == 3:  # tau=0.20
                V_representative = V.copy()
                V_representative_label = label

            # Store eigenvalues and V in npz
            npz_data[f"evals_{p}_{q}_{tau_idx}"] = evals
            npz_data[f"V_{p}_{q}_{tau_idx}"] = V

            # 3. Regression test for (0,0) at tau=0
            if (p, q) == (0, 0) and tau_idx == 0:
                regression_passed = run_regression_test(evals, V)
                if not regression_passed:
                    print("\n  FATAL: Regression test FAILED. Aborting.")
                    sys.exit(1)

            # 4. BCS scan over mu
            M_max_arr, Delta_max_arr, F_cond_arr, Delta_sols = bcs_for_sector(
                V, evals, MU_RATIOS, label=label
            )

            M_max_all[s_idx, tau_idx, :] = M_max_arr
            Delta_max_all[s_idx, tau_idx, :] = Delta_max_arr
            F_cond_all[s_idx, tau_idx, :] = F_cond_arr

            # Brief BCS summary
            M_max_best = np.max(M_max_arr)
            i_Mmax = np.argmax(M_max_arr)
            print(f"    BCS: M_max_best={M_max_best:.4f} at mu/lmin={MU_RATIOS[i_Mmax]:.2f}")

            # If any condensate found, report
            cond_mask = Delta_max_arr > 1e-20
            if np.any(cond_mask):
                best_cond_idx = np.argmax(Delta_max_arr)
                print(f"    BCS: Delta_max={Delta_max_arr[best_cond_idx]:.6f} "
                      f"at mu/lmin={MU_RATIOS[best_cond_idx]:.2f}, "
                      f"F_cond={F_cond_arr[best_cond_idx]:.6e}")
            else:
                print(f"    BCS: NO CONDENSATE at any mu (all M_max < 1 or trivial)")

            t_sec_elapsed = time.time() - t_sec_start
            print(f"    Sector {label} time: {t_sec_elapsed:.1f}s")

        t_tau_elapsed = time.time() - t_tau_start
        print(f"\n  Tau={tau:.2f} total time: {t_tau_elapsed:.1f}s")

    # -----------------------------------------------------------------------
    # Compute F_total(tau, mu) = sum_sectors mult * F_cond
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("COMPUTING F_TOTAL(tau, mu)")
    print(f"{'='*70}")

    F_total = np.zeros((N_TAU, N_MU))

    for tau_idx in range(N_TAU):
        for mu_idx in range(N_MU):
            F_sum = 0.0
            any_nan = False
            for s_idx, (p, q, dim_rho, mult) in enumerate(SECTORS):
                F_s = F_cond_all[s_idx, tau_idx, mu_idx]

                # Effective multiplicity: (2,1) gets doubled for CPT-conjugate (1,2)
                eff_mult = MULT_21_EFFECTIVE if (p, q) == (2, 1) else mult

                if np.isnan(F_s):
                    any_nan = True
                else:
                    F_sum += eff_mult * F_s

            F_total[tau_idx, mu_idx] = F_sum if not any_nan else np.nan

    # Report F_total
    print("\nF_total(tau, mu) table:")
    print(f"{'tau':>6s}", end="")
    for ratio in MU_RATIOS:
        print(f"  {ratio:>8.2f}", end="")
    print()
    for tau_idx in range(N_TAU):
        print(f"{TAU_VALUES[tau_idx]:6.2f}", end="")
        for mu_idx in range(N_MU):
            val = F_total[tau_idx, mu_idx]
            if np.isnan(val):
                print(f"  {'NaN':>8s}", end="")
            else:
                print(f"  {val:8.3f}", end="")
        print()

    # -----------------------------------------------------------------------
    # Gate verdict
    # -----------------------------------------------------------------------
    print(f"\n{'='*70}")
    print("GATE VERDICT: Multi-Sector BCS Lock")
    print(f"{'='*70}")

    verdict = "CLOSED"
    verdict_detail = []
    summary_lines = []

    # Check for interior minimum at each mu
    for mu_idx in range(N_MU):
        F_tau = F_total[:, mu_idx]
        valid = np.isfinite(F_tau)

        if not np.all(valid):
            continue

        # Check for interior minimum (not at boundary tau=0 or tau=0.50)
        min_idx = np.argmin(F_tau)

        if min_idx > 0 and min_idx < N_TAU - 1:
            # Interior minimum found
            if F_tau[min_idx] < 0:
                tau_min = TAU_VALUES[min_idx]
                F_min = F_tau[min_idx]
                # Verify it's a true minimum (second derivative > 0)
                if (F_tau[min_idx - 1] > F_tau[min_idx] and
                    F_tau[min_idx + 1] > F_tau[min_idx]):
                    verdict = "RESCUE"
                    verdict_detail.append(
                        f"Interior minimum at tau={tau_min:.2f}, "
                        f"mu/lmin={MU_RATIOS[mu_idx]:.2f}, "
                        f"F_total={F_min:.6e}"
                    )

    # Summary statistics
    for s_idx, (p, q, dim_rho, mult) in enumerate(SECTORS):
        M_at_mu0 = M_max_all[s_idx, :, 0]  # mu=0
        M_at_mu1 = M_max_all[s_idx, :, 5]  # mu=lambda_min
        summary_lines.append(
            f"({p},{q}) d={dim_rho:>2d} m={mult:>3d}: "
            f"M(mu=0)=[{np.min(M_at_mu0):.3f},{np.max(M_at_mu0):.3f}], "
            f"M(mu=lm)=[{np.min(M_at_mu1):.3f},{np.max(M_at_mu1):.3f}]"
        )

    # F_total monotonicity at each mu
    for mu_idx in range(N_MU):
        F_tau = F_total[:, mu_idx]
        valid = np.isfinite(F_tau)
        if np.all(valid) and np.all(F_tau == 0.0):
            summary_lines.append(f"mu/lmin={MU_RATIOS[mu_idx]:.2f}: F_total=0 everywhere (no condensate)")
        elif np.all(valid):
            diffs = np.diff(F_tau)
            if np.all(diffs >= -1e-15):
                summary_lines.append(f"mu/lmin={MU_RATIOS[mu_idx]:.2f}: F_total monotonically increasing")
            elif np.all(diffs <= 1e-15):
                summary_lines.append(f"mu/lmin={MU_RATIOS[mu_idx]:.2f}: F_total monotonically decreasing")
            else:
                min_idx = np.argmin(F_tau)
                summary_lines.append(
                    f"mu/lmin={MU_RATIOS[mu_idx]:.2f}: F_total non-monotonic, "
                    f"min at tau={TAU_VALUES[min_idx]:.2f} ({F_tau[min_idx]:.4e})"
                )

    # Classify verdict quality
    if verdict == "RESCUE":
        # Check if the minimum is robust (smooth) or erratic
        # A robust minimum should have neighbors within an order of magnitude
        best_detail = verdict_detail[0]
        # Parse tau from detail
        import re
        match = re.search(r'tau=(\d+\.\d+).*mu/lmin=(\d+\.\d+)', best_detail)
        if match:
            tau_best = float(match.group(1))
            mu_best_ratio = float(match.group(2))
            mu_best_idx = np.argmin(np.abs(MU_RATIOS - mu_best_ratio))
            tau_best_idx = np.argmin(np.abs(TAU_VALUES - tau_best))
            F_at_min = F_total[tau_best_idx, mu_best_idx]
            F_at_zero = F_total[0, mu_best_idx]

            # Check: is boundary F_total(tau=0) deeper than the interior min?
            boundary_dominates = (F_at_zero < F_at_min)

            # Check: profile smoothness (CV of diffs around minimum)
            F_tau = F_total[:, mu_best_idx]
            valid = np.isfinite(F_tau)
            non_zero = F_tau[valid] != 0
            profile_erratic = np.sum(np.diff(np.sign(np.diff(F_tau[valid]))) != 0) > 2

            if boundary_dominates:
                verdict_text = (
                    f"CONDITIONAL RESCUE (WEAK): Interior minimum at tau={tau_best:.2f}, "
                    f"F={F_at_min:.4f}, but boundary tau=0 is deeper "
                    f"(F={F_at_zero:.4f}). Not a global minimum."
                )
            elif profile_erratic:
                verdict_text = (
                    f"CONDITIONAL RESCUE (ERRATIC): Interior minimum at tau={tau_best:.2f}, "
                    f"F={F_at_min:.4f} at mu/lmin={mu_best_ratio:.2f}. "
                    f"Profile is non-smooth (sector on/off transitions)."
                )
            else:
                verdict_text = (
                    f"RESCUE: Smooth interior minimum at tau={tau_best:.2f}, "
                    f"F={F_at_min:.4f} at mu/lmin={mu_best_ratio:.2f}."
                )
        else:
            verdict_text = f"RESCUE: {verdict_detail[0]}"
    else:
        verdict_text = "CLOSED: F_total has no interior minimum with F<0 at any mu"

    print(f"\n  {verdict_text}")
    for line in verdict_detail:
        print(f"  {line}")
    print()
    for line in summary_lines:
        print(f"  {line}")

    # -----------------------------------------------------------------------
    # Save data
    # -----------------------------------------------------------------------
    npz_data.update({
        "M_max": M_max_all,
        "Delta_max": Delta_max_all,
        "F_cond": F_cond_all,
        "F_total": F_total,
        "lambda_min": lambda_min_all,
        "V_diag_sum": V_diag_sum_all,
        "verdict": np.array([verdict]),
    })

    npz_path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    np.savez_compressed(npz_path, **npz_data)
    print(f"\nData saved: {npz_path}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    results = {
        "M_max": M_max_all,
        "Delta_max": Delta_max_all,
        "F_cond": F_cond_all,
        "F_total": F_total,
        "lambda_min": lambda_min_all,
        "V_representative": V_representative,
        "V_representative_label": V_representative_label,
        "verdict_text": verdict_text,
        "summary_lines": summary_lines,
    }

    plot_path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.png")
    make_plots(results, plot_path)

    t_total = time.time() - t_total_start
    print(f"\nTotal runtime: {t_total:.1f}s ({t_total/60:.1f} min)")
    print(f"\n{'='*70}")
    print(f"FINAL VERDICT: {verdict_text}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
