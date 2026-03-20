"""
Session 28a Computation 7: Torsionful BCS Kernel (Gate E-4/S-1/L-4)
====================================================================

THE MAIN EVENT: Redo the BCS gap equation using D_can (canonical/torsionful
Dirac operator) eigenstates instead of D_K (Levi-Civita).

PHYSICS:
    Session 23a showed BCS condensation FAILS with D_K eigenstates:
        M_max(mu=0) = 0.077-0.154 (factor 7-13x below threshold M=1)
    This is the K-1e CLOSED.

    Session 27 T-1 showed D_can has a weaker spectral gap:
        gap_T / gap_K ranges from 0.22 to 0.67 across sectors

    The decisive question: does the D_can eigenbasis produce M_max > 1 at mu=0?

MATHEMATICAL FORMULATION:
    The BCS pairing matrix in the D_can eigenbasis is:

        V_nm^{can} = sum_{a in C^2} |<psi_n^{can}|K_a_full|psi_m^{can}>|^2

    where:
        |psi_n^{can}> are eigenvectors of D_can = M_Lie (NOT of D_K)
        K_a_full = I_{dim_rho} (x) K_a (same Kosmann operator, spinor factor)
        K_a = (1/8) sum_{r,s} [Gamma^s_{ra} - Gamma^r_{sa}] gamma_r gamma_s

    The K_a operator is defined from the Levi-Civita connection. It does NOT
    change when we switch from D_K to D_can. What changes is the basis:
    V_nm^{can} != V_nm^{LC} because the eigenstates are different.

    The linearized BCS kernel is:
        M_{nm} = V_nm^{can} * factor_m

    where factor_m = 1 / (2 * max(|lambda_m^{can} - mu|, eta)) at T=0.

    GATE: M_max > 1 at mu=0 in any sector => MAJOR PASS

INPUT:
    - s27_torsion_gap_gate.npz: D_can gap data (21 tau values, 4 sectors)
    - s27_multisector_bcs.npz: D_K BCS reference data (9 tau, 9 sectors)
    - tier1_dirac_spectrum.py: geometry infrastructure
    - s23a_kosmann_singlet.py: Kosmann operator formula
    - s26_multimode_bcs.py: BCS solver (sector-agnostic)

OUTPUT:
    - s28a_torsionful_bcs.npz
    - s28a_torsionful_bcs.png

Author: phonon-exflation-sim
Date: 2026-02-27
Session: 28a, Computation 7 (Group D)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, eigvalsh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# Import geometry + irrep infrastructure
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
    validate_clifford,
    validate_connection,
    _irrep_cache,
    C2_IDX,
)

# Import Kosmann formula from s23a
from s23a_kosmann_singlet import kosmann_operator_antisymmetric

# Import BCS solver functions from s26
from s26_multimode_bcs import (
    build_bcs_kernel,
    linearized_eigenvalues,
    selfconsistent_bcs,
    build_J_projector,
    check_spectral_pairing,
)

# Import M_Lie builder from s27
from s27_torsion_gap_gate import build_M_Lie

# Import robust free energy from s27_multisector_bcs
from s27_multisector_bcs import free_energy_bcs_robust


# ===========================================================================
# CONSTANTS
# ===========================================================================

# Use same tau grid as s27 torsion gate for maximum data reuse
TAU_VALUES = np.array([0.0, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
N_TAU = len(TAU_VALUES)

# mu values: focus on mu=0 (the decisive test) plus comparison points
MU_RATIOS = np.array([0.0, 0.5, 0.8, 1.0, 1.2])
N_MU = len(MU_RATIOS)

# Sectors to test: non-trivial sectors with p+q <= 3
# (0,0) singlet excluded: M_Lie = 0 for trivial rep, D_can has no spectrum
SECTORS = [
    (1, 0, 3, 9),      # fundamental
    (0, 1, 3, 9),      # anti-fundamental
    (1, 1, 8, 64),     # adjoint
    (2, 0, 6, 36),     # symmetric
    (0, 2, 6, 36),     # anti-symmetric
    (3, 0, 10, 100),   # (3,0)
    (0, 3, 10, 100),   # (0,3)
    (2, 1, 15, 225),   # (2,1)
]
N_SECTORS = len(SECTORS)

# BCS iteration parameters
MAX_ITER = 50000
CONV_TOL = 1e-13
DELTA0_SCALE = 0.01


# ===========================================================================
# GEOMETRY BUILDER
# ===========================================================================

def build_geometry(tau, gens, f_abc, gammas):
    """Build all geometric objects for a given tau.

    Returns E, Gamma_LC, Omega_LC for the Levi-Civita connection.
    D_can = M_Lie requires only E and rho (no Omega).
    K_a requires Gamma_LC.
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma_LC = connection_coefficients(ft)
    Omega_LC = spinor_connection_offset(Gamma_LC, gammas)
    return E, Gamma_LC, Omega_LC


# ===========================================================================
# D_CAN EIGENSYSTEM
# ===========================================================================

def compute_Dcan_eigensystem(p, q, gens, f_abc, gammas, E):
    """Build and diagonalize D_can = M_Lie for sector (p,q).

    D_can is anti-Hermitian. We diagonalize H = 1j * D_can (Hermitian).

    Parameters:
        p, q: irrep labels
        gens, f_abc: SU(3) algebra data
        gammas: Clifford generators
        E: (8,8) orthonormal frame

    Returns:
        evals_can: (N,) real eigenvalues of 1j * D_can, sorted ascending
        evecs_can: (N, N) unitary, columns = eigenvectors
        dim_rho: dimension of irrep
    """
    rho, dim_rho = get_irrep(p, q, gens, f_abc)

    # Build M_Lie = D_can
    M_Lie = build_M_Lie(rho, E, gammas)

    # Verify anti-Hermiticity
    ah_err = np.max(np.abs(M_Lie + M_Lie.conj().T))
    if ah_err > 1e-10:
        print(f"    WARNING: D_can anti-Hermiticity error = {ah_err:.2e} for ({p},{q})")

    # Diagonalize H = 1j * M_Lie (Hermitian)
    H = 1j * M_Lie
    h_err = np.max(np.abs(H - H.conj().T))
    if h_err > 1e-10:
        print(f"    WARNING: H Hermiticity error = {h_err:.2e} for ({p},{q})")

    evals_can, evecs_can = eigh(H)

    return evals_can, evecs_can, dim_rho


def compute_DK_eigensystem(p, q, gens, f_abc, gammas, E, Gamma_LC, Omega_LC):
    """Build and diagonalize D_K for sector (p,q) -- for comparison.

    Returns:
        evals_K: (N,) real eigenvalues of 1j * D_K, sorted ascending
        evecs_K: (N, N) unitary
        dim_rho: dimension of irrep
    """
    rho, dim_rho = get_irrep(p, q, gens, f_abc)
    D_K = dirac_operator_on_irrep(rho, E, gammas, Omega_LC)
    H = 1j * D_K
    evals_K, evecs_K = eigh(H)
    return evals_K, evecs_K, dim_rho


# ===========================================================================
# KOSMANN PAIRING MATRIX IN D_CAN EIGENBASIS
# ===========================================================================

def compute_kosmann_V_in_basis(Gamma_LC, gammas, dim_rho, evecs):
    """Build the Kosmann pairing matrix V_{nm} in a given eigenbasis.

    V_{nm} = sum_{a in C2_IDX} |<n|K_a_full|m>|^2

    K_a_full = I_{dim_rho} (x) K_a (Kosmann acts on spinor factor only).
    K_a is computed from Gamma_LC (Levi-Civita connection) regardless
    of which Dirac operator's eigenbasis we use.

    Parameters:
        Gamma_LC: (8,8,8) Levi-Civita connection coefficients
        gammas: Clifford generators
        dim_rho: dimension of the irrep
        evecs: (N, N) unitary matrix (columns = eigenstates, any basis)

    Returns:
        V: (N, N) real symmetric PSD pairing matrix
        K_norms: (4,) Frobenius norms of K_a for a in C2_IDX
    """
    N = evecs.shape[0]
    V = np.zeros((N, N), dtype=np.float64)
    K_norms = np.zeros(len(C2_IDX), dtype=np.float64)

    for i_a, a in enumerate(C2_IDX):
        # Compute 16x16 spinor Kosmann operator from LC connection
        K_a_spin, _ = kosmann_operator_antisymmetric(Gamma_LC, gammas, a)

        # Expand to full sector: K_a_full = I_{dim_rho} (x) K_a_spin
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

    Reuses the s26 BCS infrastructure. For each mu:
    1. Compute linearized M_max
    2. If M_max > 1, run self-consistent BCS
    3. Compute condensation free energy

    Parameters:
        V: (N, N) Kosmann pairing matrix
        evals: (N,) eigenvalues
        mu_ratios: array of mu/lambda_min values
        label: string for printing

    Returns:
        M_max_arr: (n_mu,) max eigenvalue of linearized kernel
        Delta_max_arr: (n_mu,) max |Delta| from self-consistent BCS
        F_cond_arr: (n_mu,) condensation free energy
    """
    n_mu = len(mu_ratios)
    lambda_min = np.min(np.abs(evals))

    M_max_arr = np.zeros(n_mu)
    Delta_max_arr = np.zeros(n_mu)
    F_cond_arr = np.full(n_mu, np.nan)

    # Build J-even projector
    P_even, P_odd, pairs = build_J_projector(evals)

    for i_mu, ratio in enumerate(mu_ratios):
        mu = ratio * lambda_min if lambda_min > 1e-15 else 0.0

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

            if not converged:
                print(f"    {label} mu/lmin={ratio:.2f}: NOT CONVERGED")
                F_cond_arr[i_mu] = np.nan
                continue

            # 3. Condensation free energy
            if Delta_max > 1e-20:
                F_cond, _, _ = free_energy_bcs_robust(V, evals, mu, Delta, T=0.0)
                F_cond_arr[i_mu] = F_cond
            else:
                F_cond_arr[i_mu] = 0.0
        else:
            F_cond_arr[i_mu] = 0.0
            Delta_max_arr[i_mu] = 0.0

    return M_max_arr, Delta_max_arr, F_cond_arr


# ===========================================================================
# REGRESSION: Compare D_K results to s27 reference
# ===========================================================================

def regression_DK_check(evals_K, V_K, p, q, tau_idx, tau):
    """Verify D_K eigensystem matches s27_multisector_bcs.npz reference.

    Parameters:
        evals_K: eigenvalues from D_K diagonalization
        V_K: Kosmann V matrix in D_K eigenbasis
        p, q: sector labels
        tau_idx: index into s27 tau grid
        tau: tau value

    Returns:
        passed: bool
    """
    s27_path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    if not os.path.exists(s27_path):
        print(f"    REGRESSION SKIP: {s27_path} not found")
        return True

    s27 = np.load(s27_path, allow_pickle=True)
    s27_taus = s27['tau_values']

    # Find matching tau in s27 grid
    s27_tau_idx = np.argmin(np.abs(s27_taus - tau))
    if abs(s27_taus[s27_tau_idx] - tau) > 0.001:
        return True  # No matching tau, skip

    key_evals = f"evals_{p}_{q}_{s27_tau_idx}"
    key_V = f"V_{p}_{q}_{s27_tau_idx}"

    if key_evals not in s27.files or key_V not in s27.files:
        return True

    evals_ref = s27[key_evals]
    V_ref = s27[key_V]

    eval_err = np.max(np.abs(np.sort(evals_K) - np.sort(evals_ref)))
    V_err = np.max(np.abs(V_K - V_ref))

    if eval_err > 1e-8 or V_err > 1e-8:
        print(f"    REGRESSION FAIL: ({p},{q}) tau={tau:.2f}: "
              f"eval_err={eval_err:.2e}, V_err={V_err:.2e}")
        return False

    return True


# ===========================================================================
# CROSS-VALIDATION: V_can != V_K
# ===========================================================================

def verify_basis_difference(V_can, V_K, evals_can, evals_K, label):
    """Verify that V_can and V_K are genuinely different.

    This is a critical sanity check: if V_can == V_K, then either:
    (a) the eigenbases are identical (which would mean D_can == D_K, false)
    (b) there is a code bug (using the same basis for both)

    Returns:
        V_diff: max |V_can - V_K|
        eval_diff: max |evals_can - evals_K|
    """
    # Eigenvalue comparison (sizes should match)
    eval_diff = np.max(np.abs(np.sort(evals_can) - np.sort(evals_K)))

    # V matrix comparison
    V_diff = np.max(np.abs(V_can - V_K))

    return V_diff, eval_diff


# ===========================================================================
# PLOTTING
# ===========================================================================

def make_plots(results, save_path):
    """Generate 6-panel diagnostic plot for the torsionful BCS gate.

    Panels:
        1. M_max(mu=0) comparison: D_can vs D_K across sectors and tau
        2. M_max(mu=0) enhancement ratio: M_can / M_K
        3. Spectral gap comparison: D_can vs D_K
        4. M_max vs mu for best sector at best tau
        5. V_nm diagonal comparison: D_can vs D_K for representative sector
        6. Gate verdict annotation
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("Session 28a: Torsionful BCS Gate (E-4/S-1/L-4)",
                 fontsize=14, fontweight='bold')

    sector_labels = [f"({p},{q})" for p, q, _, _ in SECTORS]
    colors = plt.cm.tab10(np.linspace(0, 1, N_SECTORS))

    # Panel 1: M_max(mu=0) for D_can (solid) vs D_K (dashed)
    ax = axes[0, 0]
    for s_idx in range(N_SECTORS):
        M_can = results['M_max_can'][s_idx, :, 0]  # mu=0
        M_K = results['M_max_K'][s_idx, :, 0]
        valid_can = np.isfinite(M_can)
        valid_K = np.isfinite(M_K)
        ax.semilogy(TAU_VALUES[valid_can], M_can[valid_can], 'o-',
                     color=colors[s_idx], markersize=3, linewidth=1.2,
                     label=f'{sector_labels[s_idx]}')
        ax.semilogy(TAU_VALUES[valid_K], M_K[valid_K], 's--',
                     color=colors[s_idx], markersize=3, linewidth=0.8, alpha=0.5)
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, linewidth=2,
               label='M=1 (critical)')
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max (mu=0)')
    ax.set_title('M_max at mu=0: D_can (solid) vs D_K (dashed)')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 2: Enhancement ratio M_can / M_K at mu=0
    ax = axes[0, 1]
    for s_idx in range(N_SECTORS):
        M_can = results['M_max_can'][s_idx, :, 0]
        M_K = results['M_max_K'][s_idx, :, 0]
        ratio = np.where((M_K > 1e-15) & np.isfinite(M_can) & np.isfinite(M_K),
                         M_can / M_K, np.nan)
        valid = np.isfinite(ratio)
        if np.any(valid):
            ax.plot(TAU_VALUES[valid], ratio[valid], 'o-',
                     color=colors[s_idx], markersize=3, linewidth=1.2,
                     label=sector_labels[s_idx])
    ax.axhline(1.0, color='black', linestyle=':', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('M_max(D_can) / M_max(D_K)')
    ax.set_title('Enhancement ratio at mu=0')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 3: Spectral gap comparison
    ax = axes[0, 2]
    for s_idx in range(N_SECTORS):
        gap_can = results['lambda_min_can'][s_idx, :]
        gap_K = results['lambda_min_K'][s_idx, :]
        valid_can = np.isfinite(gap_can) & (gap_can > 0)
        valid_K = np.isfinite(gap_K) & (gap_K > 0)
        if np.any(valid_can):
            ax.plot(TAU_VALUES[valid_can], gap_can[valid_can], 'o-',
                     color=colors[s_idx], markersize=3, linewidth=1.2,
                     label=f'{sector_labels[s_idx]}')
        if np.any(valid_K):
            ax.plot(TAU_VALUES[valid_K], gap_K[valid_K], 's--',
                     color=colors[s_idx], markersize=3, linewidth=0.8, alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('lambda_min')
    ax.set_title('Spectral gap: D_can (solid) vs D_K (dashed)')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 4: M_max vs mu for all sectors at best tau
    ax = axes[1, 0]
    best_tau_idx = results.get('best_tau_idx', N_TAU // 2)
    for s_idx in range(N_SECTORS):
        M_data = results['M_max_can'][s_idx, best_tau_idx, :]
        valid = np.isfinite(M_data)
        if np.any(valid):
            ax.semilogy(MU_RATIOS[valid], M_data[valid], 'o-',
                         color=colors[s_idx], markersize=4, linewidth=1.2,
                         label=sector_labels[s_idx])
    ax.axhline(1.0, color='red', linestyle='--', alpha=0.7, linewidth=2)
    ax.set_xlabel('mu / lambda_min_can')
    ax.set_ylabel('M_max')
    ax.set_title(f'M_max vs mu (D_can, tau={TAU_VALUES[best_tau_idx]:.2f})')
    ax.legend(fontsize=6, ncol=2)
    ax.grid(True, alpha=0.3)

    # Panel 5: V_nm diagonal sums: D_can vs D_K
    ax = axes[1, 1]
    x = np.arange(N_SECTORS)
    width = 0.35
    V_diag_can = results.get('V_diag_sum_can', np.zeros((N_SECTORS, N_TAU)))
    V_diag_K = results.get('V_diag_sum_K', np.zeros((N_SECTORS, N_TAU)))
    rep_tau = best_tau_idx
    bars1 = ax.bar(x - width/2, V_diag_can[:, rep_tau], width,
                    label='D_can basis', color='steelblue')
    bars2 = ax.bar(x + width/2, V_diag_K[:, rep_tau], width,
                    label='D_K basis', color='coral')
    ax.set_xlabel('Sector')
    ax.set_ylabel('Tr(V)')
    ax.set_title(f'V_nm diagonal sum at tau={TAU_VALUES[rep_tau]:.2f}')
    ax.set_xticks(x)
    ax.set_xticklabels(sector_labels, fontsize=7)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 6: Gate verdict
    ax = axes[1, 2]
    ax.axis('off')
    verdict_text = results.get('verdict_text', 'PENDING')
    verdict_color = 'green' if 'MAJOR PASS' in verdict_text else (
        'orange' if 'MINOR PASS' in verdict_text else 'red')
    ax.text(0.5, 0.90, 'GATE E-4/S-1/L-4', fontsize=14, fontweight='bold',
             ha='center', va='top', transform=ax.transAxes)
    ax.text(0.5, 0.78, 'Torsionful BCS', fontsize=12,
             ha='center', va='top', transform=ax.transAxes)
    ax.text(0.5, 0.65, verdict_text, fontsize=11,
             ha='center', va='top', transform=ax.transAxes,
             color=verdict_color, fontweight='bold',
             bbox=dict(boxstyle='round', facecolor='lightyellow', edgecolor=verdict_color))

    summary_lines = results.get('summary_lines', [])
    summary_text = '\n'.join(summary_lines[:15])
    ax.text(0.05, 0.52, summary_text, fontsize=7, fontfamily='monospace',
             ha='left', va='top', transform=ax.transAxes)

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nPlot saved: {save_path}")


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    """Run the torsionful BCS gate computation."""
    print("=" * 78)
    print("SESSION 28a COMPUTATION 7: TORSIONFUL BCS GATE (E-4/S-1/L-4)")
    print("=" * 78)
    print(f"Sectors: {N_SECTORS} (p+q <= 3, excluding singlet)")
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
    # [sector, tau, mu]
    M_max_can = np.zeros((N_SECTORS, N_TAU, N_MU))
    M_max_K = np.zeros((N_SECTORS, N_TAU, N_MU))
    Delta_max_can = np.zeros((N_SECTORS, N_TAU, N_MU))
    F_cond_can = np.full((N_SECTORS, N_TAU, N_MU), np.nan)

    lambda_min_can = np.zeros((N_SECTORS, N_TAU))
    lambda_min_K = np.zeros((N_SECTORS, N_TAU))
    V_diag_sum_can = np.zeros((N_SECTORS, N_TAU))
    V_diag_sum_K = np.zeros((N_SECTORS, N_TAU))

    # Cross-validation: V_can != V_K
    V_diff_max = np.zeros((N_SECTORS, N_TAU))
    eval_diff_max = np.zeros((N_SECTORS, N_TAU))

    # Enhancement ratio: M_can / M_K at mu=0
    enhancement = np.zeros((N_SECTORS, N_TAU))

    # NPZ storage
    npz_data = {
        "tau_values": TAU_VALUES,
        "mu_ratios": MU_RATIOS,
        "sectors": np.array([(p, q, d, m) for p, q, d, m in SECTORS]),
    }

    # -----------------------------------------------------------------------
    # Main loop: tau (outer) x sector (inner)
    # -----------------------------------------------------------------------
    for tau_idx, tau in enumerate(TAU_VALUES):
        t_tau_start = time.time()
        print(f"\n{'='*70}")
        print(f"TAU = {tau:.2f}  ({tau_idx+1}/{N_TAU})")
        print(f"{'='*70}")

        # Clear irrep cache between tau values
        import tier1_dirac_spectrum
        tier1_dirac_spectrum._irrep_cache = {}

        # Build geometry ONCE for this tau
        E, Gamma_LC, Omega_LC = build_geometry(tau, gens, f_abc, gammas)

        mc_err = validate_connection(Gamma_LC)
        ah_err = np.max(np.abs(Omega_LC + Omega_LC.conj().T))
        print(f"  Geometry: connection mc_err={mc_err:.2e}, Omega ah_err={ah_err:.2e}")

        for s_idx, (p, q, dim_rho_expected, mult) in enumerate(SECTORS):
            t_sec_start = time.time()
            label = f"({p},{q})"
            spinor_dim = dim_rho_expected * 16

            print(f"\n  --- Sector {label}: dim_rho={dim_rho_expected}, "
                  f"spinor_dim={spinor_dim} ---")

            # 1. D_can eigensystem
            evals_can, evecs_can, dim_rho = compute_Dcan_eigensystem(
                p, q, gens, f_abc, gammas, E
            )
            assert dim_rho == dim_rho_expected

            lmin_can = np.min(np.abs(evals_can))
            lambda_min_can[s_idx, tau_idx] = lmin_can

            # Spectral pairing check for D_can
            paired_can, pair_err_can = check_spectral_pairing(evals_can)
            print(f"    D_can: lambda_min={lmin_can:.6f}, "
                  f"pairing_err={pair_err_can:.2e}")

            # 2. D_K eigensystem (for comparison)
            evals_K, evecs_K, _ = compute_DK_eigensystem(
                p, q, gens, f_abc, gammas, E, Gamma_LC, Omega_LC
            )
            lmin_K = np.min(np.abs(evals_K))
            lambda_min_K[s_idx, tau_idx] = lmin_K

            # Gap ratio
            if lmin_K > 1e-15:
                gap_ratio = lmin_can / lmin_K
            else:
                gap_ratio = float('nan')
            print(f"    D_K:   lambda_min={lmin_K:.6f}, gap_ratio={gap_ratio:.4f}")

            # 3. Kosmann V in D_can eigenbasis
            V_can, K_norms = compute_kosmann_V_in_basis(
                Gamma_LC, gammas, dim_rho, evecs_can
            )
            V_diag_sum_can[s_idx, tau_idx] = np.sum(np.diag(V_can))

            # 4. Kosmann V in D_K eigenbasis (for comparison)
            V_K, _ = compute_kosmann_V_in_basis(
                Gamma_LC, gammas, dim_rho, evecs_K
            )
            V_diag_sum_K[s_idx, tau_idx] = np.sum(np.diag(V_K))

            # 5. Cross-validation: verify bases are different
            V_diff, eval_diff = verify_basis_difference(
                V_can, V_K, evals_can, evals_K, label
            )
            V_diff_max[s_idx, tau_idx] = V_diff
            eval_diff_max[s_idx, tau_idx] = eval_diff

            if tau > 0.001:
                # At tau>0, D_can != D_K, so V_can should differ from V_K
                if V_diff < 1e-10:
                    print(f"    WARNING: V_can ~ V_K (diff={V_diff:.2e}). "
                          f"Possible bug!")
                else:
                    print(f"    Cross-check: V_diff={V_diff:.4e}, "
                          f"eval_diff={eval_diff:.4e} (GOOD: bases differ)")
            else:
                # At tau=0, both connections are same for bi-invariant metric
                # D_can = M_Lie, D_K = M_Lie + Omega_LC. Even at tau=0, Omega_LC != 0.
                print(f"    tau=0: V_diff={V_diff:.4e}, eval_diff={eval_diff:.4e}")

            # 6. D_K regression check against s27 data
            regression_DK_check(evals_K, V_K, p, q, tau_idx, tau)

            # Store V and evals in npz
            npz_data[f"evals_can_{p}_{q}_{tau_idx}"] = evals_can
            npz_data[f"evals_K_{p}_{q}_{tau_idx}"] = evals_K
            npz_data[f"V_can_{p}_{q}_{tau_idx}"] = V_can
            npz_data[f"V_K_{p}_{q}_{tau_idx}"] = V_K

            # 7. BCS analysis: D_can eigenbasis
            M_arr_can, D_arr_can, F_arr_can = bcs_for_sector(
                V_can, evals_can, MU_RATIOS, label=f"{label} D_can"
            )
            M_max_can[s_idx, tau_idx, :] = M_arr_can
            Delta_max_can[s_idx, tau_idx, :] = D_arr_can
            F_cond_can[s_idx, tau_idx, :] = F_arr_can

            # 8. BCS analysis: D_K eigenbasis (reference)
            M_arr_K, _, _ = bcs_for_sector(
                V_K, evals_K, MU_RATIOS, label=f"{label} D_K"
            )
            M_max_K[s_idx, tau_idx, :] = M_arr_K

            # 9. Enhancement ratio at mu=0
            if M_arr_K[0] > 1e-15:
                enhancement[s_idx, tau_idx] = M_arr_can[0] / M_arr_K[0]
            else:
                enhancement[s_idx, tau_idx] = float('nan')

            print(f"    BCS D_can: M_max(mu=0)={M_arr_can[0]:.6f}, "
                  f"M_max(mu=lmin)={M_arr_can[3]:.6f}")
            print(f"    BCS D_K:   M_max(mu=0)={M_arr_K[0]:.6f}, "
                  f"M_max(mu=lmin)={M_arr_K[3]:.6f}")
            print(f"    Enhancement(mu=0): {enhancement[s_idx, tau_idx]:.4f}x")

            # 10. If supercritical at mu=0, report condensate
            if M_arr_can[0] > 1.0:
                print(f"    *** SUPERCRITICAL at mu=0! Delta_max={D_arr_can[0]:.6f}, "
                      f"F_cond={F_arr_can[0]:.6e} ***")

            t_sec = time.time() - t_sec_start
            print(f"    Time: {t_sec:.1f}s")

        t_tau = time.time() - t_tau_start
        print(f"\n  Tau={tau:.2f} total: {t_tau:.1f}s")

    # -----------------------------------------------------------------------
    # Analysis and Gate Verdict
    # -----------------------------------------------------------------------
    print(f"\n{'='*78}")
    print("GATE ANALYSIS: E-4/S-1/L-4 Torsionful BCS")
    print(f"{'='*78}")

    # Find best M_max(mu=0) across all sectors and tau
    M_mu0_can = M_max_can[:, :, 0]  # [sector, tau]
    best_s, best_t = np.unravel_index(np.argmax(M_mu0_can), M_mu0_can.shape)
    best_M_can = M_mu0_can[best_s, best_t]
    best_sector = SECTORS[best_s]
    best_tau = TAU_VALUES[best_t]

    # Corresponding D_K value
    best_M_K = M_max_K[best_s, best_t, 0]

    print(f"\n  Best M_max(mu=0) in D_can basis:")
    print(f"    Sector ({best_sector[0]},{best_sector[1]}), tau={best_tau:.2f}")
    print(f"    M_max(D_can) = {best_M_can:.6f}")
    print(f"    M_max(D_K)   = {best_M_K:.6f}")
    print(f"    Enhancement  = {best_M_can/best_M_K:.4f}x")

    # Per-sector summary table
    print(f"\n  Per-sector M_max(mu=0) summary:")
    print(f"  {'Sector':>8s} {'M_can_min':>10s} {'M_can_max':>10s} "
          f"{'M_K_min':>10s} {'M_K_max':>10s} {'Enhance':>8s}")
    print(f"  {'-'*60}")

    summary_lines = []
    for s_idx, (p, q, dim_rho, mult) in enumerate(SECTORS):
        M_can = M_mu0_can[s_idx, :]
        M_K = M_max_K[s_idx, :, 0]
        enh = enhancement[s_idx, :]
        valid_enh = enh[np.isfinite(enh)]
        enh_str = f"{np.mean(valid_enh):.3f}" if len(valid_enh) > 0 else "N/A"

        line = (f"  ({p},{q}){' '*(5-len(f'({p},{q})'))} "
                f"{np.min(M_can):10.6f} {np.max(M_can):10.6f} "
                f"{np.min(M_K):10.6f} {np.max(M_K):10.6f} {enh_str:>8s}x")
        print(line)
        summary_lines.append(
            f"({p},{q}) M_can=[{np.min(M_can):.4f},{np.max(M_can):.4f}] "
            f"M_K=[{np.min(M_K):.4f},{np.max(M_K):.4f}] "
            f"enh={enh_str}x"
        )

    # Detailed table for best sector
    print(f"\n  Detailed: sector ({best_sector[0]},{best_sector[1]}) across tau")
    print(f"  {'tau':>6s} {'gap_can':>8s} {'gap_K':>8s} {'ratio':>7s} "
          f"{'M_can(0)':>9s} {'M_K(0)':>9s} {'enh':>6s} "
          f"{'M_can(lm)':>10s} {'M_K(lm)':>10s}")
    for t_idx in range(N_TAU):
        gc = lambda_min_can[best_s, t_idx]
        gk = lambda_min_K[best_s, t_idx]
        r = gc/gk if gk > 1e-15 else float('nan')
        mc0 = M_max_can[best_s, t_idx, 0]
        mk0 = M_max_K[best_s, t_idx, 0]
        e = enhancement[best_s, t_idx]
        mc_lm = M_max_can[best_s, t_idx, 3]  # mu = lambda_min
        mk_lm = M_max_K[best_s, t_idx, 3]
        print(f"  {TAU_VALUES[t_idx]:6.2f} {gc:8.5f} {gk:8.5f} {r:7.4f} "
              f"{mc0:9.6f} {mk0:9.6f} {e:6.3f} {mc_lm:10.6f} {mk_lm:10.6f}")

    # M_max at mu = lambda_min_can comparison
    print(f"\n  M_max(mu=lambda_min) in D_can basis:")
    M_mu_lm_can = M_max_can[:, :, 3]  # mu = lambda_min index
    M_mu_lm_K = M_max_K[:, :, 3]
    best_s_lm, best_t_lm = np.unravel_index(np.argmax(M_mu_lm_can), M_mu_lm_can.shape)
    print(f"    Best: sector ({SECTORS[best_s_lm][0]},{SECTORS[best_s_lm][1]}), "
          f"tau={TAU_VALUES[best_t_lm]:.2f}")
    print(f"    M_max(D_can) = {M_mu_lm_can[best_s_lm, best_t_lm]:.6f}")
    print(f"    M_max(D_K)   = {M_mu_lm_K[best_s_lm, best_t_lm]:.6f}")

    # Enhancement ratio at mu=lambda_min
    enh_lm = np.where(M_mu_lm_K > 1e-15,
                       M_mu_lm_can / M_mu_lm_K, np.nan)
    valid_enh_lm = enh_lm[np.isfinite(enh_lm)]
    if len(valid_enh_lm) > 0:
        print(f"    Enhancement range: [{np.min(valid_enh_lm):.3f}, "
              f"{np.max(valid_enh_lm):.3f}]")

    # -----------------------------------------------------------------------
    # Gate Verdict
    # -----------------------------------------------------------------------
    print(f"\n{'='*78}")
    print("GATE VERDICT: E-4/S-1/L-4 (Torsionful BCS)")
    print(f"{'='*78}")

    # Check for MAJOR PASS: M_max(mu=0) > 1 in any sector
    major_pass = best_M_can > 1.0

    # Check for MINOR PASS: enhancement > 2 at mu=lambda_min
    minor_pass_cond = np.any(enh_lm[np.isfinite(enh_lm)] > 2.0) if len(valid_enh_lm) > 0 else False

    if major_pass:
        verdict = "MAJOR PASS"
        verdict_text = (
            f"MAJOR PASS: M_max(mu=0) = {best_M_can:.4f} > 1 in "
            f"sector ({best_sector[0]},{best_sector[1]}) at tau={best_tau:.2f}. "
            f"Torsion resolves the mu obstruction!"
        )
    elif minor_pass_cond:
        verdict = "MINOR PASS"
        max_enh = np.nanmax(enh_lm)
        verdict_text = (
            f"MINOR PASS: M_max(mu=0) = {best_M_can:.4f} < 1 "
            f"(still subcritical), but enhancement at mu=lambda_min "
            f"is {max_enh:.2f}x (> 2x threshold). Torsion helps but "
            f"does not fully resolve."
        )
    else:
        verdict = "CLOSED"
        mean_enh = np.nanmean(enhancement) if np.any(np.isfinite(enhancement)) else 0
        verdict_text = (
            f"CLOSED: M_max(mu=0) = {best_M_can:.4f} << 1. "
            f"Mean enhancement = {mean_enh:.3f}x. "
            f"Torsion does not help BCS condensation."
        )

    print(f"\n  {verdict_text}")
    summary_lines.insert(0, verdict_text)

    # -----------------------------------------------------------------------
    # Save data
    # -----------------------------------------------------------------------
    npz_data.update({
        "M_max_can": M_max_can,
        "M_max_K": M_max_K,
        "Delta_max_can": Delta_max_can,
        "F_cond_can": F_cond_can,
        "lambda_min_can": lambda_min_can,
        "lambda_min_K": lambda_min_K,
        "V_diag_sum_can": V_diag_sum_can,
        "V_diag_sum_K": V_diag_sum_K,
        "enhancement": enhancement,
        "V_diff_max": V_diff_max,
        "eval_diff_max": eval_diff_max,
        "verdict": np.array([verdict]),
    })

    npz_path = os.path.join(SCRIPT_DIR, "s28a_torsionful_bcs.npz")
    np.savez_compressed(npz_path, **npz_data)
    print(f"\nData saved: {npz_path}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    results = {
        "M_max_can": M_max_can,
        "M_max_K": M_max_K,
        "lambda_min_can": lambda_min_can,
        "lambda_min_K": lambda_min_K,
        "V_diag_sum_can": V_diag_sum_can,
        "V_diag_sum_K": V_diag_sum_K,
        "enhancement": enhancement,
        "best_tau_idx": best_t,
        "verdict_text": verdict_text,
        "summary_lines": summary_lines,
    }

    plot_path = os.path.join(SCRIPT_DIR, "s28a_torsionful_bcs.png")
    make_plots(results, plot_path)

    t_total = time.time() - t_total_start
    print(f"\nTotal runtime: {t_total:.1f}s ({t_total/60:.1f} min)")
    print(f"\n{'='*78}")
    print(f"FINAL VERDICT: {verdict_text}")
    print(f"{'='*78}")

    return verdict


if __name__ == "__main__":
    main()
