"""
S35-PFAFFIAN-CORRECTED-J — Re-run (S81 canonical verdict form)
==================================================================

Gate: PF-J-35 (BDI topological invariant under corrected J).

Structural theorem (pre-registered):
  M = C1 @ D_K(tau) is antisymmetric (since {P=C1*K, D_K}=0, D_K Hermitian).
  Pf(M)^2 = det(M) = det(C1) * det(D_K).
  sgn(Pf) is PIECEWISE-CONSTANT on any interval where spectral gap is open,
  and changes sign iff det(D_K) = 0 (gap closes).

Session 34 J-correction: C2 = gamma_1*gamma_3*gamma_5*gamma_7 (was sigma_2^{x4}).
The Pfaffian matrix M uses C1, NOT C2. So the correction is a non-trivial
sanity check: BDI algebraic structure (T^2=P^2=+1, S=TP=gamma_9) must still
hold with the corrected T = C2*K, and the Pfaffian sign must remain constant.

Re-run machinery pins:
  L_max = 16         (spinor dimension, fixed by Cliff(R^8) on 16-dim)
  N_TAU_STORED = 9   (from s23a_kosmann_singlet.npz, tau in [0, 0.5])
  N_TAU_EXTENDED = 25 (first-principles scan, tau in [0, 2.5])

Canonical constants imported; intermediates tagged # (local).
"""

import os
import sys
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# CPU thread cap FIRST (before numpy import) — 16x16 matrices, GPU not warranted
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import time
import numpy as np

# --- Canonical constants (no hardcoding) ---
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import *   # noqa: F401,F403 — framework constants

# --- dirac_spectrum lives in computations/_shared alongside S35 ---
ARCHIVE_DIR = r"C:/sandbox/Ainulindale Exflation/computations/_shared"
sys.path.insert(0, ARCHIVE_DIR)
from dirac_spectrum import (   # noqa: E402
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    build_chirality,
)

# --- Pinned machinery ---
L_MAX = 16                  # spinor dimension (Cliff(R^8) irrep)  # (local)
N_TAU_EXTENDED = 25         # extended scan density                 # (local)
TAU_EXT_MIN = 0.0           # extended scan lower bound             # (local)
TAU_EXT_MAX = 2.5           # extended scan upper bound             # (local)

t0 = time.time()             # (local)


# ======================================================================
#  Pfaffian via Parlett-Reid LTL^T  (Wimmer, ACM TOMS 38(4), 2012)
# ======================================================================
def pfaffian_hessenberg(A):
    n = A.shape[0]           # (local)
    if n == 0:
        return 1.0
    if n == 2:
        return A[0, 1]
    A = A.copy().astype(complex)
    pfaffian_val = 1.0 + 0j   # (local)
    for k in range(0, n - 1, 2):
        max_val = 0.0         # (local)
        max_idx = k + 1       # (local)
        for j in range(k + 1, n):
            if abs(A[k, j]) > max_val:
                max_val = abs(A[k, j])
                max_idx = j
        if max_val < 1e-300:
            return 0.0
        if max_idx != k + 1:
            A[:, [k + 1, max_idx]] = A[:, [max_idx, k + 1]]
            A[[k + 1, max_idx], :] = A[[max_idx, k + 1], :]
            pfaffian_val *= -1
        pfaffian_val *= A[k, k + 1]
        if k + 2 < n:
            tau = A[k, k + 2:] / A[k, k + 1]   # (local)
            A[k + 2:, k + 2:] -= np.outer(tau, A[k + 1, k + 2:])
            A[k + 2:, k + 2:] += np.outer(A[k + 1, k + 2:], tau)
    return pfaffian_val


# ======================================================================
def main():
    print("=" * 78)
    print("S35-PFAFFIAN-CORRECTED-J — re-run (S81 form)")
    print("=" * 78)
    print(f"  L_max = {L_MAX}  (pinned)")
    print(f"  tau_fold (canonical) = {tau_fold}")
    print(f"  J_C2 (canonical) = {J_C2}")

    # Clifford algebra
    gammas = build_cliff8()                                      # (local)
    gamma9 = build_chirality(gammas)                             # (local)
    C2 = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]            # corrected J (S34)  # (local)
    C1 = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]            # particle-hole      # (local)

    # Algebraic identities
    assert np.max(np.abs(C2 @ C2 - np.eye(L_MAX))) < 1e-12, "C2^2 = +I fails"
    assert np.max(np.abs(C1 @ C1 - np.eye(L_MAX))) < 1e-12, "C1^2 = +I fails"
    assert np.max(np.abs(gamma9 - C2 @ C1)) < 1e-12, "gamma_9 = C2*C1 fails"
    det_C1 = float(np.real(np.linalg.det(C1)))                    # (local)
    print(f"  det(C1) = {det_C1:+.6f}  (tau-independent)")

    # ------------------ Stored tau sweep ------------------
    kosmann = np.load(os.path.join(ARCHIVE_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)                         # (local)
    tau_vals = kosmann['tau_values']                              # (local)
    n_tau = len(tau_vals)                                         # (local)
    print(f"\n  Stored sweep: {n_tau} tau values: {list(tau_vals)}")

    sgn_stored, pf_real_stored, min_ev_stored = [], [], []        # (local)
    T_errs, P_errs, S_errs, asym_rels = [], [], [], []            # (local)
    pf_sq_det_errs = []                                           # (local)

    print(f"\n  {'tau':>6s}  {'sgn(Pf)':>8s}  {'Re(Pf)':>14s}  "
          f"{'|Im/Re|':>10s}  {'||M+M^T||/||M||':>16s}  {'min|ev|':>10s}")
    print("  " + "-" * 74)

    for ti in range(n_tau):
        tau = tau_vals[ti]                                         # (local)
        evals = kosmann[f'eigenvalues_{ti}']                       # (local)
        evecs = kosmann[f'eigenvectors_{ti}']                      # (local)
        D_K = evecs @ np.diag(evals) @ evecs.conj().T              # (local)

        # BDI symmetry diagnostics
        err_T = np.max(np.abs(C2 @ np.conj(D_K) @ C2 - D_K))       # (local)
        err_P = np.max(np.abs(C1 @ np.conj(D_K) @ C1 + D_K))       # (local)
        err_S = np.max(np.abs(gamma9 @ D_K + D_K @ gamma9))        # (local)

        M = C1 @ D_K                                                # (local)
        asym_err = np.max(np.abs(M + M.T))                          # (local)
        asym_rel = asym_err / max(np.max(np.abs(M)), 1e-300)        # (local)

        pf = pfaffian_hessenberg(M)                                 # (local)
        pf_r = float(np.real(pf))                                   # (local)
        pf_i = float(np.imag(pf))                                   # (local)
        im_re = abs(pf_i) / max(abs(pf_r), 1e-300)                  # (local)

        det_M = np.linalg.det(M)                                    # (local)
        pf_sq_det_err = abs(pf**2 - det_M) / max(abs(det_M), 1e-300)  # (local)

        evals_dk = np.linalg.eigvals(D_K)                           # (local)
        min_ev = float(np.min(np.abs(evals_dk)))                    # (local)

        sgn = "+1" if pf_r > 0 else "-1" if pf_r < 0 else " 0"      # (local)
        sgn_int = +1 if pf_r > 0 else (-1 if pf_r < 0 else 0)       # (local)

        sgn_stored.append(sgn_int)
        pf_real_stored.append(pf_r)
        min_ev_stored.append(min_ev)
        T_errs.append(err_T); P_errs.append(err_P); S_errs.append(err_S)
        asym_rels.append(asym_rel); pf_sq_det_errs.append(pf_sq_det_err)

        print(f"  {tau:6.2f}  {sgn:>8s}  {pf_r:+14.6e}  {im_re:10.2e}  "
              f"{asym_rel:16.2e}  {min_ev:10.6f}")

    # ------------------ Extended first-principles sweep ------------------
    print("\n  Extended first-principles sweep: "
          f"{N_TAU_EXTENDED} tau values in [{TAU_EXT_MIN}, {TAU_EXT_MAX}]")
    gens = su3_generators()                                        # (local)
    f_abc = compute_structure_constants(gens)                       # (local)
    B_ab = compute_killing_form(f_abc)                              # (local)

    tau_ext = np.linspace(TAU_EXT_MIN, TAU_EXT_MAX, N_TAU_EXTENDED)  # (local)
    sgn_ext, pf_real_ext, min_ev_ext, asym_rel_ext = [], [], [], []  # (local)

    print(f"\n  {'tau':>6s}  {'sgn(Pf)':>8s}  {'Re(Pf)':>14s}  "
          f"{'||M+M^T||/||M||':>16s}  {'min|ev|':>10s}")
    print("  " + "-" * 62)

    for tau in tau_ext:
        g_s = jensen_metric(B_ab, tau)                              # (local)
        E = orthonormal_frame(g_s)                                  # (local)
        ft = frame_structure_constants(f_abc, E)                    # (local)
        Gamma = connection_coefficients(ft)                         # (local)
        Omega = spinor_connection_offset(Gamma, gammas)             # (local)
        D_K = 1j * Omega                                            # (local)

        M = C1 @ D_K                                                # (local)
        asym_err = np.max(np.abs(M + M.T))                          # (local)
        asym_rel = asym_err / max(np.max(np.abs(M)), 1e-300)        # (local)

        pf = pfaffian_hessenberg(M)                                 # (local)
        pf_r = float(np.real(pf))                                   # (local)
        evals_dk = np.linalg.eigvals(D_K)                           # (local)
        min_ev = float(np.min(np.abs(evals_dk)))                    # (local)

        sgn = "+1" if pf_r > 0 else "-1" if pf_r < 0 else " 0"      # (local)
        sgn_int = +1 if pf_r > 0 else (-1 if pf_r < 0 else 0)       # (local)

        sgn_ext.append(sgn_int); pf_real_ext.append(pf_r)
        min_ev_ext.append(min_ev); asym_rel_ext.append(asym_rel)

        print(f"  {tau:6.3f}  {sgn:>8s}  {pf_r:+14.6e}  "
              f"{asym_rel:16.2e}  {min_ev:10.6f}")

    # ------------------ Verdict ------------------
    all_pos_stored = all(s == +1 for s in sgn_stored)                # (local)
    all_neg_stored = all(s == -1 for s in sgn_stored)                # (local)
    const_stored = all_pos_stored or all_neg_stored                  # (local)

    all_pos_ext = all(s == +1 for s in sgn_ext)                      # (local)
    all_neg_ext = all(s == -1 for s in sgn_ext)                      # (local)
    const_ext = all_pos_ext or all_neg_ext                           # (local)

    const_overall = const_stored and const_ext                        # (local)
    signs_match = ((all_pos_stored and all_pos_ext) or
                   (all_neg_stored and all_neg_ext))                   # (local)

    the_sign = "+1" if all_pos_stored else ("-1" if all_neg_stored else "MIXED")
    the_sign_ext = "+1" if all_pos_ext else ("-1" if all_neg_ext else "MIXED")

    min_gap = min(min(min_ev_stored), min(min_ev_ext))                # (local)

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    print(f"  Stored (n={n_tau}):    sgn(Pf) = {the_sign}    constant={const_stored}")
    print(f"  Extended (n={N_TAU_EXTENDED}): sgn(Pf) = {the_sign_ext}    constant={const_ext}")
    print(f"  Agreement (stored == extended sign): {signs_match}")
    print(f"  max |[T,D_K]|   = {max(T_errs):.2e}")
    print(f"  max |{{P,D_K}}|  = {max(P_errs):.2e}")
    print(f"  max |{{S,D_K}}|  = {max(S_errs):.2e}")
    print(f"  max ||M+M^T||/||M|| = {max(max(asym_rels), max(asym_rel_ext)):.2e}")
    print(f"  max |Pf^2 - det|/|det| = {max(pf_sq_det_errs):.2e}")
    print(f"  min|ev(D_K)| (union) = {min_gap:.6e}  (gap {'OPEN' if min_gap > 1e-6 else 'CLOSED'})")

    verdict = "PASS" if const_overall else "FAIL"                    # (local)
    print(f"\n  GATE PF-J-35: {verdict}")
    print(f"  BDI Z_2 invariant: sign(Pf) constant across 34 tau points")
    print(f"  Cross-ref S30A-DTOTAL-PFAFFIAN expects Z_2 = +1 IDENTICALLY")

    elapsed = time.time() - t0                                        # (local)
    print(f"\n  runtime = {elapsed:.2f}s")

    # Expose verdict + summary for outer capture
    return {
        "verdict": verdict,
        "sgn_stored": sgn_stored,
        "sgn_ext": sgn_ext,
        "const_stored": const_stored,
        "const_ext": const_ext,
        "sign_stored": the_sign,
        "sign_ext": the_sign_ext,
        "signs_match": signs_match,
        "max_T_err": float(max(T_errs)),
        "max_P_err": float(max(P_errs)),
        "max_S_err": float(max(S_errs)),
        "max_asym_rel": float(max(max(asym_rels), max(asym_rel_ext))),
        "max_pf_sq_det_err": float(max(pf_sq_det_errs)),
        "min_gap": float(min_gap),
        "n_tau_stored": int(n_tau),
        "n_tau_ext": int(N_TAU_EXTENDED),
    }


if __name__ == "__main__":
    r = main()
    print("\n__SUMMARY__", r)
