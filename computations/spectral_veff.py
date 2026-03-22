"""
SPECTRAL EFFECTIVE POTENTIAL V_eff(s) ON (SU(3), g_s)
=====================================================

Computes the effective potential for the Jensen shape parameter s
using the Dirac spectrum from tier1_dirac_spectrum.py.

Two contributions:
  1. Classical: V_class(s) = -R(g_s)/(16*pi*G) ~ R_scalar(g_s) / normalization
     The Ricci scalar R(g_s) of the Jensen-deformed metric.

  2. One-loop quantum: V_1loop(s) = -(1/2) * sum_n d_n * f(lambda_n^2(s) / Lambda^2)
     where d_n = dim(p,q)^2 * 16 is the Peter-Weyl multiplicity times spinor dim,
     f is a cutoff function, and Lambda is the UV cutoff.

     Three regularization schemes:
       (a) Zeta function: V_zeta = (1/2) * zeta'_D(0;s) = (1/2) sum_n d_n ln|lambda_n|
       (b) Heat kernel: V_heat(s,t) = -(1/2) sum_n d_n exp(-t * lambda_n^2)
       (c) Smooth cutoff: V_smooth(s,Lambda) = -(1/2) sum_n d_n * g(lambda_n^2/Lambda^2)
           with g(x) = x*exp(-x) (exponential suppression)

     ALSO: spectral action S(s) = sum_n d_n * f(lambda_n^2/Lambda^2)
     with f(x) = exp(-x) (Chamseddine-Connes).

The PHYSICAL prediction is whether V_eff(s) has a minimum.
If so, at what s_0? What is the Dirac spectrum at s_0?

Author: Feynman-Theorist Agent
Date: 2026-02-12
"""

import numpy as np
import sys
import os

# Import from tier1_dirac_spectrum
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, collect_spectrum, validate_connection,
    U1_IDX, SU2_IDX, C2_IDX
)


# =============================================================================
# MODULE 1: RICCI SCALAR ON (SU(3), g_s)
# =============================================================================

def compute_curvature_tensor(Gamma, ft):
    """
    Compute the Riemann curvature tensor in the ON frame for a Lie group.

    For left-invariant ON frame on a Lie group, the curvature is:
      R^d_{cab} = Gamma^d_{ca,b} - Gamma^d_{cb,a}     <- ZERO (constant coefficients)
                 + Gamma^e_{ca} Gamma^d_{eb} - Gamma^e_{cb} Gamma^d_{ea}
                 - f_tilde^e_{ab} Gamma^d_{ec}         <- structure constant term

    Since the connection coefficients are constant in the left-invariant frame,
    the partial derivative terms vanish. The curvature reduces to:

      R^d_{cab} = sum_e [Gamma^e_{ca} Gamma^d_{eb} - Gamma^e_{cb} Gamma^d_{ea}]
                  - sum_e f_tilde^e_{ab} Gamma^d_{ec}

    Convention: R^d_{cab} = < e^d, R(e_a, e_b) e_c >
    Ricci: Ric_{cb} = R^a_{cab} = sum_a R^a_{cab}
    Scalar: R = sum_a Ric_{aa}

    Args:
        Gamma: (8,8,8) connection, Gamma[d,a,c] = Gamma^d_{ac}
        ft: (8,8,8) ON frame structure constants, ft[a,b,c] = f_tilde^c_{ab}

    Returns:
        Riem: (8,8,8,8) curvature tensor R[d,c,a,b] = R^d_{cab}
    """
    n = Gamma.shape[0]
    Riem = np.zeros((n, n, n, n), dtype=np.float64)

    for d in range(n):
        for c in range(n):
            for a in range(n):
                for b in range(n):
                    val = 0.0
                    for e in range(n):
                        # Quadratic Gamma terms
                        # Gamma^e_{ac} = Gamma[e,a,c]
                        # Gamma^d_{eb} = Gamma[d,e,b]
                        val += Gamma[e, a, c] * Gamma[d, e, b]
                        val -= Gamma[e, b, c] * Gamma[d, e, a]
                        # Structure constant term: -f_tilde^e_{ab} Gamma^d_{ec}
                        val -= ft[a, b, e] * Gamma[d, e, c]
                    Riem[d, c, a, b] = val

    return Riem


def ricci_scalar(Gamma, ft):
    """
    Compute the Ricci scalar R(g_s) from the connection.

    R = sum_{a,b} R^a_{bab} (contraction on first and third indices)

    In ON frame, this is just a trace.

    Args:
        Gamma: (8,8,8) connection coefficients
        ft: (8,8,8) ON frame structure constants

    Returns:
        R: scalar curvature (float)
    """
    Riem = compute_curvature_tensor(Gamma, ft)
    # Ricci tensor: Ric_{cb} = R^a_{cab} = sum_a Riem[a,c,a,b]
    n = Gamma.shape[0]
    R = 0.0
    for a in range(n):
        for b in range(n):
            R += Riem[a, b, a, b]
    return R


def ricci_scalar_fast(Gamma, ft):
    """
    Faster computation using numpy operations.

    R = sum_{a,b} R^a_{bab}
    R^a_{bab} = sum_e [Gamma^e_{ab} Gamma^a_{eb} - Gamma^e_{bb} Gamma^a_{ea}]
                - sum_e ft^e_{ab} Gamma^a_{eb}
    """
    n = Gamma.shape[0]
    # R^a_{bab} = sum_e Gamma[e,a,b]*Gamma[a,e,b] - Gamma[e,b,b]*Gamma[a,e,a]
    #            - ft[a,b,e]*Gamma[a,e,b]

    R = 0.0
    for a in range(n):
        for b in range(n):
            for e in range(n):
                R += Gamma[e, a, b] * Gamma[a, e, b]
                R -= Gamma[e, b, b] * Gamma[a, e, a]
                R -= ft[a, b, e] * Gamma[a, e, b]
    return R


# =============================================================================
# MODULE 2: SPECTRAL ACTION / EFFECTIVE POTENTIAL
# =============================================================================

def compute_eigenvalue_data(s, gens, f_abc, gammas, max_pq_sum=3):
    """
    Compute Dirac eigenvalues and their multiplicities at deformation s.

    Returns eigenvalues as |lambda| (absolute values), with Peter-Weyl
    multiplicities d_n = dim(p,q)^2 (the squared dimension gives the
    multiplicity in the full L^2 spectrum; the factor of 16 from spinor
    dimension is already in the eigenvalue counting from the D_pi matrix).

    Actually: in the Peter-Weyl decomposition,
      L^2(SU(3), S) = bigoplus_{(p,q)} V_{(p,q)} tensor V_{(p,q)}^* tensor S
    Each eigenvalue of D_{(p,q)} (a (dim_pq * 16) x (dim_pq * 16) matrix)
    appears with multiplicity dim(p,q) in the full spectrum.

    So the total degeneracy of eigenvalue lambda from sector (p,q) is:
      d_lambda = dim(p,q) * (multiplicity within D_{(p,q)})

    For our computation, we already get eigenvalues of D_{(p,q)} (with their
    internal multiplicities), and the Peter-Weyl multiplicity is dim(p,q).

    Args:
        s: Jensen parameter
        gens, f_abc, gammas: infrastructure

    Returns:
        eigenvalues: list of (|lambda|, total_multiplicity)
        R_scalar: Ricci scalar at this s
    """
    # Build geometric infrastructure
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    # Ricci scalar
    R_s = ricci_scalar_fast(Gamma, ft)

    # Dirac spectrum
    all_evals, eval_data = collect_spectrum(
        s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
    )

    # Convert to (|lambda|, multiplicity) list
    # all_evals is list of (complex_eigenvalue, pw_multiplicity)
    eigen_data = []
    for ev, mult in all_evals:
        abs_ev = abs(ev)
        if abs_ev > 1e-12:  # skip zero modes
            eigen_data.append((abs_ev, mult))

    return eigen_data, R_s


def spectral_action_heat(eigen_data, t):
    """
    Heat kernel regularized spectral action:
      S_heat(s, t) = sum_n d_n * exp(-t * lambda_n^2)

    This is the partition function Z = Tr exp(-t D^2) at "time" t = 1/Lambda^2.

    Small t (high cutoff): dominated by large eigenvalues -> UV.
    Large t (low cutoff): dominated by small eigenvalues -> IR.

    Args:
        eigen_data: list of (|lambda|, multiplicity)
        t: "time" parameter (= 1/Lambda^2)

    Returns:
        S: spectral action value
    """
    S = 0.0
    for lam, mult in eigen_data:
        S += mult * np.exp(-t * lam**2)
    return S


def spectral_action_smooth(eigen_data, Lambda):
    """
    Smooth cutoff spectral action (Chamseddine-Connes):
      S_CC(s, Lambda) = sum_n d_n * f(lambda_n^2 / Lambda^2)

    with f(x) = exp(-x).

    This is equivalent to spectral_action_heat with t = 1/Lambda^2.

    Args:
        eigen_data: list of (|lambda|, multiplicity)
        Lambda: UV cutoff scale

    Returns:
        S: spectral action value
    """
    return spectral_action_heat(eigen_data, 1.0 / Lambda**2)


def one_loop_potential_zeta(eigen_data, mu=1.0):
    """
    Zeta function regularized one-loop effective potential:
      V_zeta(s) = (1/2) * sum_n d_n * ln(lambda_n^2 / mu^2)

    Note: this is the NEGATIVE of the standard convention used by Hawking
    in his message (-(1/2) sum ln lambda^2). The sign convention is:
      V = +(1/2) zeta'(0) = +(1/2) sum d_n ln|lambda_n|
    A LARGER value of V is energetically disfavored.
    The MINIMUM of V determines s_0.

    The subtlety: mu is a renormalization scale. V(s) - V(s_ref) is
    mu-independent (the mu-dependent part cancels in the difference).

    Args:
        eigen_data: list of (|lambda|, multiplicity)
        mu: renormalization scale

    Returns:
        V: one-loop potential
    """
    V = 0.0
    for lam, mult in eigen_data:
        if lam > 1e-12:
            V += mult * np.log(lam**2 / mu**2)
    return 0.5 * V


def one_loop_potential_heat(eigen_data, t):
    """
    Heat-kernel regularized one-loop effective potential:
      V_heat(s, t) = -(1/2) * (d/dt) Tr exp(-t D^2)
                   = (1/2) * sum_n d_n * lambda_n^2 * exp(-t * lambda_n^2)

    This is the expectation value of D^2 in the heat kernel ensemble.
    The minimum gives the shape that minimizes the "vacuum energy."

    Args:
        eigen_data: list of (|lambda|, multiplicity)
        t: "time" parameter

    Returns:
        V: one-loop potential
    """
    V = 0.0
    for lam, mult in eigen_data:
        V += mult * lam**2 * np.exp(-t * lam**2)
    return 0.5 * V


# =============================================================================
# MODULE 3: COMBINED EFFECTIVE POTENTIAL
# =============================================================================

def combined_veff(s, gens, f_abc, gammas, max_pq_sum=3,
                  kappa_class=1.0, Lambda=None, t_heat=None, mu_zeta=1.0,
                  method='zeta'):
    """
    Compute the combined V_eff(s) = V_classical(s) + V_quantum(s).

    V_classical = -kappa_class * R(g_s)
       (the Einstein-Hilbert term favors NEGATIVE curvature = large R;
        for SU(3), R > 0 always, so V_class > 0 for kappa_class > 0.
        The minimum of V_class alone is at s=0 (bi-invariant = max symmetry).

    V_quantum depends on method:
      'zeta': V_zeta(s) = (1/2) sum d_n ln(lambda_n^2/mu^2)
      'heat': V_heat(s,t) = (1/2) sum d_n lambda_n^2 exp(-t lambda_n^2)
      'spectral': -spectral_action(s,Lambda) = -sum d_n exp(-lambda_n^2/Lambda^2)

    The competition between V_class (wants s=0) and V_quantum (wants nonzero s
    if the spectral weight is optimized) determines s_0.

    Args:
        s: Jensen parameter
        gens, f_abc, gammas: infrastructure
        max_pq_sum: max irrep to include
        kappa_class: weight of classical term
        Lambda: cutoff for smooth/spectral method
        t_heat: time param for heat method
        mu_zeta: renorm scale for zeta method
        method: 'zeta', 'heat', or 'spectral'

    Returns:
        V_total, V_class, V_quant, R_scalar
    """
    eigen_data, R_s = compute_eigenvalue_data(s, gens, f_abc, gammas, max_pq_sum)

    V_class = -kappa_class * R_s

    if method == 'zeta':
        V_quant = one_loop_potential_zeta(eigen_data, mu=mu_zeta)
    elif method == 'heat':
        if t_heat is None:
            t_heat = 1.0
        V_quant = one_loop_potential_heat(eigen_data, t_heat)
    elif method == 'spectral':
        if Lambda is None:
            Lambda = 1.0
        V_quant = -spectral_action_smooth(eigen_data, Lambda)
    else:
        raise ValueError(f"Unknown method: {method}")

    return V_class + V_quant, V_class, V_quant, R_s


# =============================================================================
# MODULE 4: s-SWEEP AND ANALYSIS
# =============================================================================

def sweep_veff(s_values, gens, f_abc, gammas, max_pq_sum=3,
               kappa_class=1.0, Lambda=1.0, method='zeta'):
    """
    Sweep V_eff over a range of s values.

    Returns structured data for plotting and analysis.
    """
    results = []
    for i, s in enumerate(s_values):
        # Clear irrep cache for each s to avoid stale data
        import tier1_dirac_spectrum as t1
        t1._irrep_cache = {}

        V_tot, V_cl, V_qu, R_s = combined_veff(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum,
            kappa_class=kappa_class, Lambda=Lambda, method=method
        )
        results.append({
            's': s,
            'V_total': V_tot,
            'V_classical': V_cl,
            'V_quantum': V_qu,
            'R_scalar': R_s
        })
        print(f"  s={s:.4f}: R={R_s:.4f}, V_cl={V_cl:.4f}, "
              f"V_qu={V_qu:.4f}, V_tot={V_tot:.4f}")

    return results


def find_minimum(results):
    """
    Find the minimum of V_total in the sweep data.

    Returns the s value and V_total at the minimum, plus neighbors for
    parabolic interpolation.
    """
    V_vals = [r['V_total'] for r in results]
    s_vals = [r['s'] for r in results]

    idx_min = np.argmin(V_vals)
    s_min = s_vals[idx_min]
    V_min = V_vals[idx_min]

    # Parabolic interpolation if not at boundary
    if 0 < idx_min < len(results) - 1:
        s1, s2, s3 = s_vals[idx_min-1], s_vals[idx_min], s_vals[idx_min+1]
        V1, V2, V3 = V_vals[idx_min-1], V_vals[idx_min], V_vals[idx_min+1]
        # Parabola through three points: s_opt = s2 - 0.5*(s2-s1)^2*(V2-V3) - (s2-s3)^2*(V2-V1)
        #                                          / ((s2-s1)*(V2-V3) - (s2-s3)*(V2-V1))
        num = (s2-s1)**2 * (V2-V3) - (s2-s3)**2 * (V2-V1)
        den = (s2-s1) * (V2-V3) - (s2-s3) * (V2-V1)
        if abs(den) > 1e-15:
            s_opt = s2 - 0.5 * num / den
            return s_opt, V_min, True
        else:
            return s_min, V_min, False
    else:
        return s_min, V_min, False


def plot_veff(results, save_path=None):
    """
    Plot V_eff(s) and its components.
    """
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print("  matplotlib not available; skipping plot.")
        return

    s_vals = [r['s'] for r in results]
    V_total = [r['V_total'] for r in results]
    V_class = [r['V_classical'] for r in results]
    V_quant = [r['V_quantum'] for r in results]
    R_vals = [r['R_scalar'] for r in results]

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: V_total
    ax = axes[0, 0]
    ax.plot(s_vals, V_total, 'b-o', markersize=4, label='V_total')
    idx_min = np.argmin(V_total)
    ax.axvline(x=s_vals[idx_min], color='red', linestyle='--', alpha=0.5,
               label=f's_min = {s_vals[idx_min]:.3f}')
    ax.axvline(x=0.15, color='green', linestyle=':', alpha=0.5, label='s = 0.15')
    ax.axvline(x=np.log((1+np.sqrt(5))/2)/3, color='orange', linestyle=':',
               alpha=0.5, label=f's = ln(phi)/3 = {np.log((1+np.sqrt(5))/2)/3:.4f}')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('V_eff(s)')
    ax.set_title('Total Effective Potential')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 2: Components
    ax = axes[0, 1]
    ax.plot(s_vals, V_class, 'r-s', markersize=3, label='V_classical')
    ax.plot(s_vals, V_quant, 'g-^', markersize=3, label='V_quantum')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('V(s)')
    ax.set_title('Classical vs Quantum')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Ricci scalar
    ax = axes[1, 0]
    ax.plot(s_vals, R_vals, 'k-o', markersize=4)
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('R(g_s)')
    ax.set_title('Ricci Scalar')
    ax.grid(True, alpha=0.3)

    # Panel 4: Normalized V_total (shifted so min = 0)
    ax = axes[1, 1]
    V_shifted = np.array(V_total) - min(V_total)
    ax.plot(s_vals, V_shifted, 'b-o', markersize=4)
    ax.axvline(x=s_vals[idx_min], color='red', linestyle='--', alpha=0.5)
    ax.axvline(x=0.15, color='green', linestyle=':', alpha=0.5, label='s = 0.15')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('V_eff(s) - V_min')
    ax.set_title('Normalized Potential Well')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"  Plot saved to {save_path}")
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, 'veff_spectral.png')
        plt.savefig(path, dpi=150)
        print(f"  Plot saved to {path}")
    plt.close()


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 80)
    print("SPECTRAL EFFECTIVE POTENTIAL V_eff(s) ON (SU(3), g_s)")
    print("=" * 80)

    # Infrastructure
    print("\n[1] Building infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    max_pq = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    print(f"  max_pq_sum = {max_pq}")

    # --- Part A: Ricci scalar sweep (classical potential) ---
    print(f"\n[2] Computing Ricci scalar R(g_s) vs s...")
    s_fine = np.linspace(0.0, 2.0, 41)
    R_data = []
    for s in s_fine:
        B_ab = compute_killing_form(f_abc)
        g_s = jensen_metric(B_ab, s)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        R_s = ricci_scalar_fast(Gamma, ft)
        R_data.append((s, R_s))
        if s < 0.01 or abs(s - 0.15) < 0.03 or abs(s - 1.0) < 0.03 or s > 1.9:
            print(f"  s={s:.3f}: R = {R_s:.6f}")

    # Validate: at s=0 (bi-invariant), R should be a known value
    # For SU(3) with Killing metric B, R = dim(G)/4 = 8/4 = 2 when
    # g = |B|. Actually R = (1/4) * sum_a f_{abc}^2 / g_aa...
    # Let's just report it.
    R_biinv = R_data[0][1]
    print(f"\n  Bi-invariant (s=0) Ricci scalar: R = {R_biinv:.6f}")
    print(f"  R monotonic? {all(R_data[i][1] <= R_data[i+1][1] for i in range(len(R_data)-1))}")

    # --- Part B: Zeta-function V_eff sweep ---
    print(f"\n[3] Computing V_eff(s) with ZETA regularization (kappa_class=1.0)...")
    s_sweep = np.linspace(0.0, 2.0, 21)

    import tier1_dirac_spectrum as t1

    # Sweep with kappa = 0 (pure quantum)
    print("\n  --- Pure quantum potential (kappa=0) ---")
    results_quant = []
    for s in s_sweep:
        t1._irrep_cache = {}
        eigen_data, R_s = compute_eigenvalue_data(s, gens, f_abc, gammas, max_pq)
        V_zeta = one_loop_potential_zeta(eigen_data, mu=1.0)
        results_quant.append({'s': s, 'V_total': V_zeta, 'V_classical': 0,
                              'V_quantum': V_zeta, 'R_scalar': R_s})
        print(f"    s={s:.3f}: V_zeta={V_zeta:.4f}, R={R_s:.4f}")

    s_min_q, V_min_q, interp_q = find_minimum(results_quant)
    print(f"\n  Pure quantum minimum: s_0 = {s_min_q:.4f} (interpolated={interp_q})")

    # Sweep with several kappa values
    for kappa in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        print(f"\n  --- kappa_class = {kappa:.1f} ---")
        results_k = []
        for s in s_sweep:
            t1._irrep_cache = {}
            eigen_data, R_s = compute_eigenvalue_data(s, gens, f_abc, gammas, max_pq)
            V_cl = -kappa * R_s
            V_qu = one_loop_potential_zeta(eigen_data, mu=1.0)
            V_tot = V_cl + V_qu
            results_k.append({'s': s, 'V_total': V_tot, 'V_classical': V_cl,
                              'V_quantum': V_qu, 'R_scalar': R_s})

        s_min_k, V_min_k, interp_k = find_minimum(results_k)
        print(f"    Minimum: s_0 = {s_min_k:.4f}, V_min = {V_min_k:.4f} (interp={interp_k})")

    # --- Part C: Heat-kernel spectral action sweep ---
    print(f"\n[4] Computing SPECTRAL ACTION S(s, Lambda) for multiple cutoffs...")

    for Lambda_val in [0.5, 1.0, 2.0, 5.0]:
        print(f"\n  --- Lambda = {Lambda_val:.1f} ---")
        S_data = []
        for s in s_sweep:
            t1._irrep_cache = {}
            eigen_data, R_s = compute_eigenvalue_data(s, gens, f_abc, gammas, max_pq)
            S_val = spectral_action_smooth(eigen_data, Lambda_val)
            S_data.append((s, S_val))
            print(f"    s={s:.3f}: S = {S_val:.6f}")

        # Find extremum of spectral action
        S_vals = [x[1] for x in S_data]
        idx_max = np.argmax(S_vals)
        idx_min = np.argmin(S_vals)
        print(f"    Max S at s={S_data[idx_max][0]:.3f} (S={S_data[idx_max][1]:.4f})")
        print(f"    Min S at s={S_data[idx_min][0]:.3f} (S={S_data[idx_min][1]:.4f})")

    # --- Part D: Full V_eff with best kappa ---
    print(f"\n[5] Full V_eff sweep with kappa_class=1.0, zeta regularization...")
    t1._irrep_cache = {}
    results_full = sweep_veff(s_sweep, gens, f_abc, gammas, max_pq_sum=max_pq,
                               kappa_class=1.0, method='zeta')

    s_min_full, V_min_full, interp_full = find_minimum(results_full)
    print(f"\n  V_eff minimum: s_0 = {s_min_full:.4f}, V_min = {V_min_full:.4f}")
    print(f"  Interpolated: {interp_full}")

    # Key reference values
    phi = (1 + np.sqrt(5)) / 2
    s_phi = np.log(phi) / 3
    print(f"\n  Reference s values:")
    print(f"    s = 0.15 (gauge coupling match)")
    print(f"    s = ln(phi)/3 = {s_phi:.4f} (Einstein algebraic phi)")
    print(f"    s_0 = {s_min_full:.4f} (V_eff minimum)")
    print(f"    |s_0 - 0.15| = {abs(s_min_full - 0.15):.4f}")
    print(f"    |s_0 - s_phi| = {abs(s_min_full - s_phi):.4f}")

    # --- Part E: Plot ---
    print(f"\n[6] Generating plot...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    plot_veff(results_full, save_path=os.path.join(script_dir, 'veff_spectral.png'))

    # --- Part F: Eigenvalue ratios at the minimum ---
    print(f"\n[7] Checking phi at s_0 = {s_min_full:.4f}...")
    t1._irrep_cache = {}
    all_evals_min, eval_data_min = collect_spectrum(
        s_min_full, gens, f_abc, gammas, max_pq_sum=max_pq, verbose=False
    )

    # Extract absolute values
    abs_vals = sorted(set(round(abs(ev), 10) for ev, _ in all_evals_min if abs(ev) > 1e-10))
    abs_vals = np.array(abs_vals)

    phi_p = 1.53158
    print(f"\n  First 20 eigenvalues at s_0:")
    for i, v in enumerate(abs_vals[:20]):
        print(f"    [{i:2d}] |lambda| = {v:.6f}")

    # Check pairwise ratios for phi
    n = min(20, len(abs_vals))
    phi_hits = []
    for i in range(n):
        for j in range(i+1, n):
            r = abs_vals[j] / abs_vals[i]
            if abs(r - phi_p) < 0.03:
                phi_hits.append((i, j, r, abs_vals[i], abs_vals[j]))

    print(f"\n  Phi-near pairwise ratios at s_0 (3% tol): {len(phi_hits)}")
    for i, j, r, vi, vj in sorted(phi_hits, key=lambda x: abs(x[2] - phi_p))[:10]:
        err_ppm = abs(r - phi_p) / phi_p * 1e6
        print(f"    [{i}]/[{j}]: {vj:.6f}/{vi:.6f} = {r:.6f} ({err_ppm:.1f} ppm from phi)")

    # --- Summary ---
    print(f"\n{'='*80}")
    print("SUMMARY")
    print("=" * 80)
    print(f"  Classical potential V_class = -kappa * R(g_s):")
    print(f"    R(s=0) = {R_biinv:.4f} (bi-invariant)")
    print(f"    R MONOTONIC with s: {'YES' if all(R_data[i][1] <= R_data[i+1][1] for i in range(len(R_data)-1)) else 'NO'}")
    print(f"    V_class wants s=0 (maximum symmetry)")
    print(f"")
    print(f"  Quantum potential V_quant = (1/2) sum d_n ln(lambda_n^2/mu^2):")
    print(f"    Pure quantum minimum: s_0 = {s_min_q:.4f}")
    print(f"")
    print(f"  Combined V_eff (kappa=1.0):")
    print(f"    Minimum: s_0 = {s_min_full:.4f}")
    print(f"    Distance from s=0.15: {abs(s_min_full - 0.15):.4f}")
    print(f"    Distance from ln(phi)/3: {abs(s_min_full - s_phi):.4f}")
    print(f"")
    print(f"  Phi-near pairs at s_0: {len(phi_hits)}")
    if phi_hits:
        best = min(phi_hits, key=lambda x: abs(x[2] - phi_p))
        print(f"  Closest to phi: ratio = {best[2]:.6f} ({abs(best[2]-phi_p)/phi_p*1e6:.1f} ppm)")

    print(f"\n{'='*80}")
    print("COMPUTATION COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
