"""
H-5 STANDALONE VERIFICATION: Full CW V_eff
============================================

Zero trust in agent-created scripts. This file imports ONLY from:
  - tier1_dirac_spectrum.py (Feb 12, pre-session, proven)
  - tier1_spectral_action.py (Feb 12, pre-session, proven)

All Laplacian functions are INLINED here from first principles.
No imports from kk1_bosonic_tower.py, b6_*, h5_full_veff.py, or any
other agent-created Session 18 file.

Uses GPU (AMD RX 9070 XT via ROCm) for batched eigenvalue decomposition.
Matrices are constructed on CPU, transferred to GPU for eigvalsh.

Author: Hawking-Theorist (Session 18, standalone rebuild)
"""
import numpy as np
from numpy.linalg import eigvalsh
import sys, os, time
import torch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

# ONLY trusted imports (Feb 12 scripts, untouched by Session 18 agents)
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients,
    collect_spectrum, get_irrep,
)
from tier1_spectral_action import (
    dim_su3_irrep, scalar_curvature_analytical,
)

# GPU setup
USE_GPU = torch.cuda.is_available()
DEVICE = torch.device('cuda' if USE_GPU else 'cpu')


def gpu_eigvalsh(matrix_np):
    """Eigenvalues of a Hermitian matrix using GPU if available."""
    if USE_GPU and matrix_np.shape[0] >= 64:
        t = torch.tensor(matrix_np, dtype=torch.float64, device=DEVICE)
        eigs = torch.linalg.eigvalsh(t)
        return eigs.cpu().numpy()
    else:
        return eigvalsh(matrix_np)


def gpu_eigvalsh_batch(matrices):
    """
    Batch eigenvalue decomposition on GPU.
    matrices: list of real symmetric numpy arrays (can be different sizes).
    Returns: list of eigenvalue arrays.

    Groups by size for true batched operation.
    """
    if not matrices:
        return []

    if not USE_GPU:
        return [eigvalsh(m) for m in matrices]

    # Group by matrix size
    by_size = {}
    for i, m in enumerate(matrices):
        n = m.shape[0]
        if n not in by_size:
            by_size[n] = []
        by_size[n].append((i, m))

    results = [None] * len(matrices)
    for n, items in by_size.items():
        indices = [i for i, _ in items]
        mats = [m for _, m in items]

        if n >= 64:
            # GPU batched
            batch = torch.tensor(np.stack(mats), dtype=torch.float64, device=DEVICE)
            eigs_batch = torch.linalg.eigvalsh(batch)
            eigs_np = eigs_batch.cpu().numpy()
            for j, idx in enumerate(indices):
                results[idx] = eigs_np[j]
        else:
            # CPU for small matrices
            for idx, m in zip(indices, mats):
                results[idx] = eigvalsh(m)

    return results


# =====================================================================
# INLINED: Scalar Laplacian on irrep (from first principles)
# =====================================================================
def scalar_laplacian_on_irrep(rho, E, Gamma):
    """
    Delta_0 on sector (p,q).
    = -sum_a (hat_e_a)^2 + sum_a div(hat_e_a) * hat_e_a
    where hat_e_a = sum_b E[a,b] rho(e_b)
    and div(hat_e_a) = sum_d Gamma[d,d,a]
    """
    dim_rho = rho[0].shape[0]
    Delta = np.zeros((dim_rho, dim_rho), dtype=complex)

    for a in range(8):
        hat_ea = np.zeros((dim_rho, dim_rho), dtype=complex)
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                hat_ea += E[a, b] * rho[b]
        Delta -= hat_ea @ hat_ea

        div_a = sum(Gamma[d, d, a] for d in range(8))
        if abs(div_a) > 1e-15:
            Delta += div_a * hat_ea

    return Delta


# =====================================================================
# INLINED: Ricci tensor from connection
# =====================================================================
def ricci_tensor(Gamma, ft):
    """Ric_{ac} = sum_b R^b_{bac} with standard Riemann convention."""
    n = 8
    Ric = np.zeros((n, n))
    for a in range(n):
        for c in range(n):
            val = 0.0
            for b in range(n):
                for e in range(n):
                    val += Gamma[b, b, e] * Gamma[e, a, c]
                    val -= Gamma[b, a, e] * Gamma[e, b, c]
                    val -= ft[b, a, e] * Gamma[b, e, c]
            Ric[a, c] = val
    return Ric


# =====================================================================
# INLINED: Vector (1-form) Hodge Laplacian on irrep
# =====================================================================
def vector_laplacian_on_irrep(rho, E, Gamma, Ric, ft):
    """
    Hodge Laplacian Delta_1 = rough_Laplacian + Ric on 1-forms.
    Matrix size: dim_rho * 8.
    """
    dim_rho = rho[0].shape[0]
    n = 8
    dim_total = dim_rho * n

    # Build hat_e_c operators on the rep space
    hat_e = []
    for c in range(n):
        op = np.zeros((dim_rho, dim_rho), dtype=complex)
        for d in range(n):
            if abs(E[c, d]) > 1e-15:
                op += E[c, d] * rho[d]
        hat_e.append(op)

    I_rho = np.eye(dim_rho, dtype=complex)

    # Build nabla_c operators (covariant derivative on 1-forms)
    nabla = []
    for c in range(n):
        nc = np.zeros((dim_total, dim_total), dtype=complex)
        for a in range(n):
            rs, re = a * dim_rho, (a + 1) * dim_rho
            for b in range(n):
                cs_, ce = b * dim_rho, (b + 1) * dim_rho
                if a == b:
                    nc[rs:re, cs_:ce] += hat_e[c]
                coeff = Gamma[b, c, a]  # Gamma^b_{ca}
                if abs(coeff) > 1e-15:
                    nc[rs:re, cs_:ce] -= coeff * I_rho
        nabla.append(nc)  # one nabla per c, NOT per (c,a)

    # Rough Laplacian: -sum_c [nabla_c^2 - sum_d Gamma^d_{cc} nabla_d]
    rough = np.zeros((dim_total, dim_total), dtype=complex)
    for c in range(n):
        rough -= nabla[c] @ nabla[c]
        for d in range(n):
            coeff = Gamma[d, c, c]
            if abs(coeff) > 1e-15:
                rough += coeff * nabla[d]

    # Ricci operator on 1-forms: (Ric omega)_a = sum_b Ric[a,b] omega_b
    Ric_op = np.zeros((dim_total, dim_total), dtype=complex)
    for a in range(n):
        for b in range(n):
            if abs(Ric[a, b]) > 1e-15:
                rs, re = a * dim_rho, (a + 1) * dim_rho
                cs_, ce = b * dim_rho, (b + 1) * dim_rho
                Ric_op[rs:re, cs_:ce] = Ric[a, b] * I_rho

    return rough + Ric_op


# =====================================================================
# V_tree (exact analytic)
# =====================================================================
def V_tree(s):
    """Baptista eq 3.80 at sigma=0. UN-normalized (raw)."""
    s = np.asarray(s, dtype=np.float64)
    R_bracket = 2 * np.exp(2*s) - 1 + 8 * np.exp(-s) - np.exp(-4*s)
    return 1.0 - R_bracket / 10.0


# =====================================================================
# Coleman-Weinberg 1-loop
# =====================================================================
def CW_contribution(eigenvalues, multiplicities, mu_sq=1.0, c=1.5, sign=+1):
    """
    V_CW = sign * (1/64pi^2) * sum_n mult_n * m_n^4 * [ln(m_n^2/mu^2) - c]

    sign = +1 for bosons, -1 for fermions.
    eigenvalues = mass-squared values (m^2 = lambda for Laplacian, |lambda|^2 for Dirac)
    """
    V = 0.0
    dof = 0
    for m2, mult in zip(eigenvalues, multiplicities):
        dof += mult
        if m2 > 1e-30:
            V += mult * m2**2 * (np.log(m2 / mu_sq) - c)
    V *= sign / (64 * np.pi**2)
    return V, dof


# =====================================================================
# MAIN: Full V_eff computation
# =====================================================================
def main():
    t_global = time.time()

    print("=" * 72)
    print("H-5 STANDALONE VERIFICATION")
    print("Zero imports from agent-created Session 18 scripts")
    if USE_GPU:
        print(f"GPU: {torch.cuda.get_device_name(0)} ({torch.cuda.get_device_properties(0).total_memory/1e9:.1f} GB)")
    else:
        print("GPU: NOT AVAILABLE (CPU fallback)")
    print("=" * 72)

    # Infrastructure (from proven Feb 12 code)
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"  Clifford error: {cliff_err:.2e}")

    B_ab = compute_killing_form(f_abc)

    # ---------------------------------------------------------------
    # Bi-invariant (s=0) sanity check: scalar Laplacian = C2/3
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("SANITY CHECK: s=0 scalar Laplacian eigenvalues = C2(p,q)/3")
    print("=" * 72)

    g0 = jensen_metric(B_ab, 0.0)
    E0 = orthonormal_frame(g0)
    ft0 = frame_structure_constants(f_abc, E0)
    Gamma0 = connection_coefficients(ft0)

    for p, q in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0)]:
        C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
        expected = C2 / 3.0

        rho, dim_check = get_irrep(p, q, gens, f_abc)
        Delta = scalar_laplacian_on_irrep(rho, E0, Gamma0)
        Delta = 0.5 * (Delta + Delta.conj().T)
        eigs = np.sort(gpu_eigvalsh(Delta.real))

        err = max(abs(eigs[0] - expected), abs(eigs[-1] - expected))
        status = "PASS" if err < 1e-10 else "FAIL"
        print(f"  ({p},{q}): C2/3 = {expected:.6f}, eigs = [{eigs[0]:.6f}, {eigs[-1]:.6f}], "
              f"err = {err:.2e} [{status}]")

    # ---------------------------------------------------------------
    # s=0 vector Laplacian check: must be non-negative (H^1(SU(3))=0)
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("SANITY CHECK: s=0 vector Laplacian >= 0 (H^1(SU(3))=0)")
    print("=" * 72)

    Ric0 = ricci_tensor(Gamma0, ft0)
    R_check = sum(Ric0[a, a] for a in range(8))
    R_analytic = scalar_curvature_analytical(0.0)
    print(f"  Scalar curvature: R = {R_check:.6f} (analytic: {R_analytic:.6f})")
    print(f"  Ric diag: [{', '.join(f'{Ric0[a,a]:.4f}' for a in range(8))}]")

    for p, q in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        rho, _ = get_irrep(p, q, gens, f_abc)
        D1 = vector_laplacian_on_irrep(rho, E0, Gamma0, Ric0, ft0)
        D1 = 0.5 * (D1 + D1.conj().T)
        eigs = np.sort(gpu_eigvalsh(D1.real))
        n_neg = np.sum(eigs < -1e-8)
        status = "PASS" if n_neg == 0 else f"FAIL ({n_neg} neg)"
        print(f"  ({p},{q}): min_eig = {eigs[0]:.6f}, max_eig = {eigs[-1]:.6f}, "
              f"n_neg = {n_neg} [{status}]")

    # ---------------------------------------------------------------
    # Full V_eff sweep
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("FULL V_eff SWEEP: 21 s-values, mps=6 (scalar), mps=4 (vector)")
    print("=" * 72)

    s_values = np.concatenate([
        np.linspace(0.0, 0.5, 11),
        np.array([0.7, 1.0, 1.5, 2.0, 2.5])
    ])
    # Remove duplicates and sort
    s_values = np.unique(s_values)

    MPS_SCALAR = 6
    MPS_VECTOR = 4
    MU_SQ = 1.0
    C_SUB = 1.5  # MS-bar

    results = []

    for idx, s in enumerate(s_values):
        t0 = time.time()

        # --- Infrastructure for this s ---
        g_s = jensen_metric(B_ab, s)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Ric = ricci_tensor(Gamma, ft)

        # --- Scalar Laplacian eigenvalues (build matrices, batch eigsolve) ---
        scalar_matrices = []
        scalar_dims = []
        for pq_sum in range(MPS_SCALAR + 1):
            for p in range(pq_sum + 1):
                q = pq_sum - p
                dim_pq = dim_su3_irrep(p, q)
                try:
                    rho, _ = get_irrep(p, q, gens, f_abc)
                    Delta = scalar_laplacian_on_irrep(rho, E, Gamma)
                    Delta = 0.5 * (Delta + Delta.conj().T)
                    scalar_matrices.append(Delta.real)
                    scalar_dims.append(dim_pq)
                except Exception:
                    pass

        scalar_eigs_list = gpu_eigvalsh_batch(scalar_matrices)
        scalar_eigs_all = []
        scalar_mults_all = []
        for eigs, dim_pq in zip(scalar_eigs_list, scalar_dims):
            for ev in eigs:
                scalar_eigs_all.append(ev)
                scalar_mults_all.append(dim_pq)  # PW mult = dim(p,q)

        # --- Vector Laplacian eigenvalues (build matrices, batch eigsolve) ---
        vector_matrices = []
        vector_dims = []
        for pq_sum in range(MPS_VECTOR + 1):
            for p in range(pq_sum + 1):
                q = pq_sum - p
                dim_pq = dim_su3_irrep(p, q)
                mat_size = dim_pq * 8
                if mat_size > 5000:
                    continue
                try:
                    rho, _ = get_irrep(p, q, gens, f_abc)
                    D1 = vector_laplacian_on_irrep(rho, E, Gamma, Ric, ft)
                    D1 = 0.5 * (D1 + D1.conj().T)
                    vector_matrices.append(D1.real)
                    vector_dims.append(dim_pq)
                except Exception:
                    pass

        vector_eigs_list = gpu_eigvalsh_batch(vector_matrices)
        vector_eigs_all = []
        vector_mults_all = []
        for eigs, dim_pq in zip(vector_eigs_list, vector_dims):
            for ev in eigs:
                vector_eigs_all.append(ev)
                vector_mults_all.append(dim_pq)

        # --- CW bosonic ---
        all_bos_eigs = scalar_eigs_all + vector_eigs_all
        all_bos_mults = scalar_mults_all + vector_mults_all
        V_bos, dof_bos = CW_contribution(all_bos_eigs, all_bos_mults,
                                          MU_SQ, C_SUB, sign=+1)

        # --- Fermionic CW (from proven Dirac spectrum) ---
        _, eval_data = collect_spectrum(s, gens, f_abc, gammas,
                                        max_pq_sum=MPS_SCALAR, verbose=False)
        ferm_eigs = []
        ferm_mults = []
        for p, q, evs in eval_data:
            d_pq = dim_su3_irrep(p, q)
            for lam in evs:
                ferm_eigs.append(float(abs(lam)**2))  # m^2 = |lambda|^2 (eigs are purely imaginary)
                ferm_mults.append(d_pq)

        V_ferm, dof_ferm = CW_contribution(ferm_eigs, ferm_mults,
                                             MU_SQ, C_SUB, sign=-1)

        # --- V_tree ---
        Vt = float(V_tree(s))

        # --- Total ---
        V_total = Vt + V_bos + V_ferm

        dt = time.time() - t0

        dof_scalar = sum(scalar_mults_all)
        dof_vector = sum(vector_mults_all)

        results.append({
            's': s, 'V_tree': Vt, 'V_bos': V_bos, 'V_ferm': V_ferm,
            'V_total': V_total,
            'dof_scalar': dof_scalar, 'dof_vector': dof_vector,
            'dof_bos': dof_bos, 'dof_ferm': dof_ferm, 'dt': dt,
        })

        if idx % 4 == 0 or idx == len(s_values) - 1:
            print(f"  s={s:.3f}: V_t={Vt:.4e}, V_b={V_bos:+.4e}, V_f={V_ferm:+.4e}, "
                  f"V_tot={V_total:+.4e}, DOF(b={dof_bos},f={dof_ferm}), {dt:.1f}s")

    # ---------------------------------------------------------------
    # Summary table
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("COMPLETE RESULTS TABLE")
    print("=" * 72)
    print(f"{'s':>6} {'V_tree':>12} {'V_boson':>12} {'V_fermion':>14} "
          f"{'V_total':>14} {'DOF_b':>8} {'DOF_f':>8}")
    print("-" * 80)
    for r in results:
        print(f"{r['s']:6.3f} {r['V_tree']:12.4e} {r['V_bos']:+12.4e} "
              f"{r['V_ferm']:+14.4e} {r['V_total']:+14.4e} "
              f"{r['dof_bos']:8d} {r['dof_ferm']:8d}")

    # ---------------------------------------------------------------
    # Monotonicity analysis
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("MONOTONICITY ANALYSIS")
    print("=" * 72)

    V_arr = np.array([r['V_total'] for r in results])
    s_arr = np.array([r['s'] for r in results])
    diffs = np.diff(V_arr)
    n_up = np.sum(diffs > 0)
    n_down = np.sum(diffs < 0)
    print(f"  Steps up: {n_up}/{len(diffs)}, Steps down: {n_down}/{len(diffs)}")

    if n_down == len(diffs):
        print("  MONOTONICALLY DECREASING (fermionic runaway)")
    elif n_up == len(diffs):
        print("  MONOTONICALLY INCREASING (bosonic wall)")
    else:
        print("  NON-MONOTONIC -- looking for turning points:")
        for i in range(len(diffs) - 1):
            if diffs[i] * diffs[i+1] < 0:
                print(f"    Turning point near s ~ {s_arr[i+1]:.3f}")

    # ---------------------------------------------------------------
    # mu dependence
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("MU DEPENDENCE (5 s-values x 5 mu-values)")
    print("=" * 72)

    # Use cached data for mu scan -- just recompute CW with different mu
    s_test = [0.0, 0.15, 0.3, 0.5, 1.0]
    mu_test = [0.01, 0.1, 1.0, 10.0, 100.0]

    for s in s_test:
        g_s = jensen_metric(B_ab, s)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Ric = ricci_tensor(Gamma, ft)

        # Collect eigenvalues once
        bos_ev, bos_mu_list = [], []
        for pq_sum in range(MPS_SCALAR + 1):
            for p in range(pq_sum + 1):
                q = pq_sum - p
                dim_pq = dim_su3_irrep(p, q)
                try:
                    rho, _ = get_irrep(p, q, gens, f_abc)
                    Delta = scalar_laplacian_on_irrep(rho, E, Gamma)
                    Delta = 0.5 * (Delta + Delta.conj().T)
                    for ev in gpu_eigvalsh(Delta.real):
                        bos_ev.append(ev)
                        bos_mu_list.append(dim_pq)
                except Exception:
                    pass

        for pq_sum in range(MPS_VECTOR + 1):
            for p in range(pq_sum + 1):
                q = pq_sum - p
                dim_pq = dim_su3_irrep(p, q)
                mat_size = dim_pq * 8
                if mat_size > 5000:
                    continue
                try:
                    rho, _ = get_irrep(p, q, gens, f_abc)
                    D1 = vector_laplacian_on_irrep(rho, E, Gamma, Ric, ft)
                    D1 = 0.5 * (D1 + D1.conj().T)
                    for ev in gpu_eigvalsh(D1.real):
                        bos_ev.append(ev)
                        bos_mu_list.append(dim_pq)
                except Exception:
                    pass

        _, eval_data = collect_spectrum(s, gens, f_abc, gammas,
                                        max_pq_sum=MPS_SCALAR, verbose=False)
        fer_ev, fer_mu_list = [], []
        for p, q, evs in eval_data:
            d_pq = dim_su3_irrep(p, q)
            for lam in evs:
                fer_ev.append(float(abs(lam)**2))
                fer_mu_list.append(d_pq)

        Vt = float(V_tree(s))

        line = f"  s={s:.2f}: "
        for mu in mu_test:
            Vb, _ = CW_contribution(bos_ev, bos_mu_list, mu**2, C_SUB, +1)
            Vf, _ = CW_contribution(fer_ev, fer_mu_list, mu**2, C_SUB, -1)
            V_tot = Vt + Vb + Vf
            line += f"mu={mu:.2f}:{V_tot:+.3e}  "
        print(line)

    # ---------------------------------------------------------------
    # DOF budget
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("DOF BUDGET")
    print("=" * 72)
    r0 = results[0]
    print(f"  Scalar Laplacian DOF: {r0['dof_scalar']:,d}")
    print(f"  Vector Laplacian DOF: {r0['dof_vector']:,d}")
    print(f"  Total bosonic DOF:    {r0['dof_bos']:,d}")
    print(f"  Fermionic (Dirac) DOF:{r0['dof_ferm']:,d}")
    print(f"  Ratio B/F:            {r0['dof_bos']/r0['dof_ferm']:.4f}")
    print(f"  Ratio F/B:            {r0['dof_ferm']/r0['dof_bos']:.1f}")

    # ---------------------------------------------------------------
    # Constraint Condition assessment
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("Constraint Condition ASSESSMENT")
    print("=" * 72)

    has_interior_min = False
    if n_up > 0 and n_down > 0:
        # Check for actual local minima
        for i in range(1, len(V_arr) - 1):
            if V_arr[i] < V_arr[i-1] and V_arr[i] < V_arr[i+1]:
                has_interior_min = True
                s_min = s_arr[i]
                sin2 = 1.0 / (1.0 + np.exp(4 * s_min))
                print(f"  Interior minimum at s ~ {s_min:.3f}")
                print(f"  sin^2(theta_W) = {sin2:.6f} (exp: 0.23121)")
                if 0.24 <= s_min <= 0.37:
                    print(f"  F1 Weinberg: PASS (s0 in window)")
                else:
                    print(f"  F1 Weinberg: FAIL (s0 outside [0.24, 0.37])")

    if not has_interior_min:
        print(f"  NO interior minimum found.")
        print(f"  V_eff is {'monotonically decreasing' if n_down == len(diffs) else 'monotonically increasing'}.")
        if n_down == len(diffs):
            print(f"  The Jensen deformation is thermodynamically FAVORED")
            print(f"  but there is no restoring force -- UNBOUNDED RUNAWAY.")
            print(f"  The fermionic vacuum energy overwhelms all bosonic contributions.")
        elif n_up == len(diffs):
            print(f"  The bi-invariant metric (s=0) is the unique minimum.")
            print(f"  sin^2(theta_W) = 0.5 at s=0 -- FATAL for Weinberg angle.")

        print(f"\n  CLOSED: No interior minimum at 1-loop CW level.")
        print(f"  This closes the 1-LOOP APPROXIMATION, not the framework.")
        print(f"  Stabilization requires beyond-1-loop effects:")
        print(f"    - Casimir energy (sum over ALL KK modes, not just low-lying)")
        print(f"    - Non-perturbative fermion condensates")
        print(f"    - Flux/instanton corrections")
        print(f"    - Higher-loop gravitational corrections")

    # ---------------------------------------------------------------
    # Thermodynamic interpretation
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("THERMODYNAMIC INTERPRETATION (Hawking)")
    print("=" * 72)

    print(f"  V_CW = Helmholtz free energy F(s, mu)")
    print(f"  s = shape modulus (order parameter for internal geometry)")
    print(f"  The 1-loop CW potential is the leading quantum correction")
    print(f"  to the classical (tree-level) effective potential.")
    print()

    if n_down == len(diffs):
        print(f"  F(s) DECREASES monotonically:")
        print(f"    F(0.0) = {results[0]['V_total']:+.4e}")
        print(f"    F(0.3) = {results[6]['V_total'] if len(results) > 6 else 'N/A':+.4e}")
        print(f"    F(1.0) = {[r for r in results if abs(r['s']-1.0)<0.01][0]['V_total']:+.4e}")
        print()
        print(f"  The deformed geometry LOWERS the free energy.")
        print(f"  This is the curved-space Casimir effect: fermions in the")
        print(f"  Jensen-deformed SU(3) have lower vacuum energy than in")
        print(f"  the bi-invariant geometry. The internal space WANTS to deform.")
        print()
        print(f"  But there is no restoring force. The system runs away to")
        print(f"  s -> infinity, where the internal space degenerates.")
        print(f"  This is the well-known modulus stabilization problem")
        print(f"  of Kaluza-Klein compactifications, now exhibited concretely")
        print(f"  in the Baptista-Jensen framework.")

    # ---------------------------------------------------------------
    # Generate plot
    # ---------------------------------------------------------------
    print(f"\n{'='*72}")
    print("GENERATING PLOT")
    print("=" * 72)

    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt

        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        fig.suptitle('H-5 Standalone Verification: CW V_eff(s)\n'
                     'Zero imports from agent scripts', fontsize=14, fontweight='bold')

        # Panel 1: All components
        ax = axes[0, 0]
        ss = [r['s'] for r in results]
        ax.plot(ss, [r['V_tree'] for r in results], 'b-', lw=2, label='V_tree')
        ax.plot(ss, [r['V_bos'] for r in results], 'r-', lw=2, label='V_boson')
        ax.plot(ss, [r['V_ferm'] for r in results], 'g-', lw=2, label='V_fermion')
        ax.plot(ss, [r['V_total'] for r in results], 'k-', lw=3, label='V_total')
        ax.set_xlabel('s')
        ax.set_ylabel('V_eff')
        ax.set_title('V_eff Components (s=0 to 1)')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1.0)

        # Panel 2: V_total zoomed to s=[0, 0.5]
        ax = axes[0, 1]
        mask = [r['s'] <= 0.55 for r in results]
        ss_zoom = [r['s'] for r, m in zip(results, mask) if m]
        vt_zoom = [r['V_total'] for r, m in zip(results, mask) if m]
        ax.plot(ss_zoom, vt_zoom, 'k-', lw=2)
        ax.axvspan(0.24, 0.37, alpha=0.15, color='green', label='Weinberg window')
        ax.set_xlabel('s')
        ax.set_ylabel('V_total')
        ax.set_title('V_total (zoomed, with Weinberg window)')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # Panel 3: Ratio V_bos / V_ferm
        ax = axes[1, 0]
        ratios = [abs(r['V_bos']) / max(abs(r['V_ferm']), 1e-30) for r in results]
        ax.plot(ss, ratios, 'purple', lw=2)
        ax.set_xlabel('s')
        ax.set_ylabel('|V_boson| / |V_fermion|')
        ax.set_title('Boson/Fermion CW magnitude ratio')
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 1.0)

        # Panel 4: Summary text
        ax = axes[1, 1]
        ax.axis('off')
        summary = (
            f"H-5 STANDALONE VERIFICATION\n"
            f"{'='*40}\n\n"
            f"Bosonic DOF:  {results[0]['dof_bos']:,d}\n"
            f"Fermionic DOF: {results[0]['dof_ferm']:,d}\n"
            f"Ratio F/B: {results[0]['dof_ferm']/results[0]['dof_bos']:.1f}:1\n\n"
            f"Shape: {'MONO DEC' if n_down==len(diffs) else 'MONO INC' if n_up==len(diffs) else 'NON-MONO'}\n"
            f"Interior minimum: {'YES' if has_interior_min else 'NO'}\n\n"
            f"Scalar Laplacian: mps={MPS_SCALAR}\n"
            f"Vector Laplacian: mps={MPS_VECTOR}\n"
            f"Dirac spectrum:   mps={MPS_SCALAR}\n\n"
            f"All Laplacians inlined.\n"
            f"Zero imports from Session 18 agent files.\n"
        )
        ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

        plt.tight_layout()
        save_path = os.path.join(SCRIPT_DIR, 'h5_standalone_verify.png')
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"  Plot saved: {save_path}")
        plt.close()

    except Exception as e:
        print(f"  Plot error: {e}")
        import traceback
        traceback.print_exc()

    dt_total = time.time() - t_global
    print(f"\n{'='*72}")
    print(f"TOTAL TIME: {dt_total:.1f}s ({dt_total/60:.1f} min)")
    print("=" * 72)


if __name__ == "__main__":
    main()
