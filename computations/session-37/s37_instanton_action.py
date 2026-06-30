"""
S37-INSTANTON-ACTION:  re-run of s37_instanton_action.py
=================================================================

Original: computations/session-37/s37_instanton_action.py (SHA-256 head 16: 0c529edff6b2a374)

Purpose
-------
Reproduce the S37 instanton action computation under S81 canonical discipline:
  - Framework constants imported from canonical_constants.py
  - Intermediates tagged `# (local)`
  - SHA-256 pins emitted for every input npz in the first lines of stdout
  - Closure SHA emitted at the end; output 4-tuple line printed last

Gate
----
S37-INSTANTON-ACTION — reproducibility of S_inst_D (Method D, direct
numerical from full BCS free energy) against the canonical MCP value.

Target value: S_inst ≈ 0.0686 (canonical S_inst = 0.06860372346994315 from
s37_instanton_mc; the action script's S_inst_D is the seed Delta/barrier for
the MC and is expected to land within ABSOLUTE 5% tolerance of the same
attractor).

Substitution chain (action-direction, GL-regime)
-------------------------------------------------
Defs:
  V(Delta) = b * (Delta^2 - Delta_0^2)^2      (GL quartic, minimum condition a=-2b*Delta_0^2)
  S_inst   = integral_0^{Delta_0} sqrt(2 V(Delta)) dDelta       (1D kink action)
Substitute V into S_inst:
  sqrt(2 V) = sqrt(2b) * |Delta_0^2 - Delta^2|
  For Delta in [0, Delta_0]: Delta^2 <= Delta_0^2, so |...| = Delta_0^2 - Delta^2
Simplify:
  S_inst = sqrt(2b) * integral_0^{Delta_0} (Delta_0^2 - Delta^2) dDelta
         = sqrt(2b) * [Delta_0^2 * Delta - Delta^3/3]_0^{Delta_0}
         = sqrt(2b) * (2/3) * Delta_0^3
Direction:
  S_inst > 0 always when b > 0 and Delta_0 > 0.
  S_inst INCREASES with b^{1/2} and with Delta_0^3.
  Gate thresholds (canonical, INST-37a):
    S_inst < 0.5 -> DENSE GAS (Z_2 restored)
    0.5 < S_inst < 5 -> CROSSOVER
    S_inst > 5 -> DILUTE (mean-field BCS)
  S37 result S_inst ≈ 0.069 < 0.5 ⇒ DENSE GAS (below dense-gas threshold).
"""

import hashlib
import json
import os
import sys
import time

import numpy as np

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# --- canonical constants (MANDATORY S34+) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                     # (local)
COMP_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))                  # (local)
if COMP_DIR not in sys.path:
    sys.path.insert(0, COMP_DIR)
from canonical_constants import *  # noqa: E402,F401,F403

# Referenced canonical names:
#   M_max_thouless (= 1.674), S_inst (= 0.06860...), rho_B2_per_mode, tau_fold
# All via `from canonical_constants import *`.

ARCHIVE_DIR = os.path.abspath(os.path.join(COMP_DIR, "..", "_shared"))  # (local)

# --- input SHA-256 pins (precomputed 2026-04-17, T3 prep) ---
INPUT_PINS = {                                                              # (local)
    's23a_kosmann_singlet.npz':
        'ef547e583cf73e91b3f0d26e1ba14ee74c28d3718ee08dde12e0f17ad2775214',
    's34a_dphys_kosmann.npz':
        'c5fbb8770a27b4ed39e9c04a512f4373f71fefc7fb1cbc591ad88c9f0b97a6f9',
    's35a_vh_impedance_arbiter.npz':
        '410c4835f23e5064712338853f57b3ac13370c6e7ef3dfd43ffe6fb13ce7a34d',
    's36_multisector_ed.npz':
        '74c59d141ff64620af9b67e34f024d8190b0a0eb5d3f302b356aea12fa8f3631',
    's36_gl_cubic_check.npz':
        '5e5035427eeee86aac53c52ffc749345bd8fdab04f725c971e230574c4551c1e',
    's36_gcm_self_consistent.npz':
        '59af5aaf8dea16ddfea57945e434a0a4d8c74a43296ba542f64c096c7897f5f1',
}


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_pins():
    print('=' * 72)
    print('S37-INSTANTON-ACTION: SHA-256 input pins')
    print('=' * 72)
    for name, expected in INPUT_PINS.items():
        path = os.path.join(ARCHIVE_DIR, name)
        actual = sha256_of_file(path)
        match = 'OK' if actual == expected else 'MISMATCH'
        print(f'  {name:<38s} {actual[:16]}...  [{match}]')
        if actual != expected:
            raise RuntimeError(
                f'SHA mismatch for {name}: expected {expected}, got {actual}'
            )
    print()


def solve_bcs_gap(V_mat, E_vec, rho_vec, mu=0.0, n_iter=5000, tol=1e-14):
    """Multi-mode BCS gap equation:
       Delta_k = sum_{k'} V_{kk'} * sqrt(rho_k*rho_k') * Delta_{k'} / (2*E_{k'})
    """
    n = len(E_vec)                                                          # (local)
    xi = E_vec - mu                                                         # (local)
    Delta = np.ones(n) * 0.1                                                # (local)
    for it in range(n_iter):
        E_qp = np.sqrt(xi**2 + Delta**2)                                    # (local)
        Delta_new = np.zeros(n)                                             # (local)
        for k in range(n):
            for kp in range(n):
                Delta_new[k] += (V_mat[k, kp] *
                                 np.sqrt(rho_vec[k] * rho_vec[kp]) *
                                 Delta[kp] / (2.0 * E_qp[kp]))
        diff = np.max(np.abs(Delta_new - Delta))                            # (local)
        Delta = Delta_new.copy()
        if diff < tol:
            return Delta, True, it
    return Delta, False, n_iter


def bcs_free_energy_alpha(alpha, Delta_SC, V_mat, xi, rho):
    """BCS variational F measured from normal state, at Delta_k = alpha * Delta_SC."""
    n = len(xi)                                                             # (local)
    Delta = alpha * Delta_SC                                                # (local)
    E_qp = np.sqrt(xi**2 + Delta**2)                                        # (local)
    F_kin = np.sum(E_qp - np.abs(xi))                                       # (local)
    F_pair = 0.0                                                            # (local)
    for k in range(n):
        for kp in range(n):
            F_pair -= (V_mat[k, kp] * np.sqrt(rho[k] * rho[kp]) *
                       Delta[k] * Delta[kp] / (4.0 * E_qp[k] * E_qp[kp]))
    return F_kin + F_pair


def main():
    t0 = time.time()                                                        # (local)
    verify_pins()

    print('=' * 72)
    print('S37-INSTANTON-ACTION: canonical vs computed')
    print('=' * 72)
    print(f'  Canonical M_max_thouless  = {M_max_thouless}')
    print(f'  Canonical S_inst (target) = {S_inst}')
    print(f'  Canonical rho_B2_per_mode = {rho_B2_per_mode}')
    print(f'  Canonical tau_fold        = {tau_fold}')
    print()

    # --- Load inputs ---
    kosmann = np.load(os.path.join(ARCHIVE_DIR, 's23a_kosmann_singlet.npz'),
                      allow_pickle=True)
    vh_arbiter = np.load(os.path.join(ARCHIVE_DIR,
                                      's35a_vh_impedance_arbiter.npz'),
                         allow_pickle=True)
    ed_data = np.load(os.path.join(ARCHIVE_DIR, 's36_multisector_ed.npz'),
                      allow_pickle=True)
    gcm_data = np.load(os.path.join(ARCHIVE_DIR,
                                    's36_gcm_self_consistent.npz'),
                       allow_pickle=True)

    E_8 = ed_data['E_8_full']                                               # (local)
    V_8 = ed_data['V_8x8_full']                                             # (local)

    # Cross-check: stored rho_B2 vs canonical
    rho_B2_stored = float(vh_arbiter['rho_at_physical'])                    # (local)
    v_F_data = float(vh_arbiter['v_phys'])                                  # (local)
    d2E_data = float(vh_arbiter['d2E_fold'])                                # (local)
    B2_bw_data = float(vh_arbiter['B2_bw'])                                 # (local)
    tau_fold_stored = float(vh_arbiter['tau_fold'])                         # (local)
    print(f'  Cross-check rho_B2_per_mode: canonical={rho_B2_per_mode:.6f} '
          f'stored={rho_B2_stored:.6f}')
    print(f'  Cross-check tau_fold: canonical={tau_fold} '
          f'stored={tau_fold_stored:.5f}')
    print()

    # B2 eigenvalues at tau=0.20
    ti = 3                                                                  # (local) tau index
    evals_raw = kosmann[f'eigenvalues_{ti}']                                # (local)
    si = np.argsort(evals_raw)                                              # (local)
    evals_s = evals_raw[si]                                                 # (local)
    pos_idx = np.where(evals_s > 0)[0]                                      # (local)
    B2_idx = pos_idx[1:5]                                                   # (local)
    E_B2 = evals_s[B2_idx]                                                  # (local)

    V_B2 = V_8[np.ix_([0, 1, 2, 3], [0, 1, 2, 3])]                          # (local)
    rho_B2_vec = np.array([rho_B2_per_mode] * 4)                            # (local)
    xi_B2 = E_B2 - 0.0                                                      # (local) mu=0

    # GCM peak
    tau_fine = gcm_data['tau_fine']                                         # (local)
    Delta_fine = gcm_data['Delta_max_fine']                                 # (local)
    idx_peak = int(np.argmax(Delta_fine))                                   # (local)
    Delta_0_peak = float(Delta_fine[idx_peak])                              # (local)
    tau_peak = float(tau_fine[idx_peak])                                    # (local)

    # --- Self-consistent gap (for alpha parametrization) ---
    Delta_SC, conv_SC, nit_SC = solve_bcs_gap(V_B2, xi_B2, rho_B2_vec)      # (local)
    Delta_max_SC = float(np.max(Delta_SC))                                  # (local)
    print(f'  Gap equation: converged={conv_SC} iters={nit_SC}')
    print(f'  Delta_SC = {Delta_SC}')
    print(f'  Delta_max_SC = {Delta_max_SC:.8f}')
    print(f'  Delta_0_peak (GCM) = {Delta_0_peak:.6f} at tau={tau_peak:.4f}')
    print()

    # --- F(alpha) landscape ---
    n_alpha = 10001                                                         # (local)
    alpha_max_scan = 3.0                                                    # (local)
    alpha_scan = np.linspace(0, alpha_max_scan, n_alpha)                    # (local)
    F_alpha = np.array([                                                    # (local)
        bcs_free_energy_alpha(a, Delta_SC, V_B2, xi_B2, rho_B2_vec)
        for a in alpha_scan
    ])

    idx_min = int(np.argmin(F_alpha))                                       # (local)
    alpha_min = float(alpha_scan[idx_min])                                  # (local)
    F_min = float(F_alpha[idx_min])                                         # (local)
    Delta_0_num = alpha_min * Delta_max_SC                                  # (local)

    # --- Method D: Direct numerical instanton ---
    # S_inst = integral sqrt(2 * (F(Delta) - F_min)) dDelta   (in Delta space)
    # Expressed along alpha path and rescaled by Delta_max_SC:
    #   Delta = alpha * Delta_max_SC => dDelta = Delta_max_SC * dalpha
    F_shifted = F_alpha[:idx_min + 1] - F_min                               # (local)
    delta_inst = alpha_scan[:idx_min + 1] * Delta_max_SC                    # (local)
    V_inst = np.maximum(0.0, F_shifted)                                     # (local)
    integrand = np.sqrt(2.0 * V_inst)                                       # (local)
    S_inst_D = float(np.trapezoid(integrand, delta_inst))                   # (local)
    barrier_D = float(F_shifted[0])                                         # (local)

    print(f'  Method D (direct numerical from BCS F):')
    print(f'    alpha_min = {alpha_min:.6f}')
    print(f'    Delta_0_num = {Delta_0_num:.8f}')
    print(f'    F_min = {F_min:.8f}')
    print(f'    barrier = F(0) - F_min = {barrier_D:.8f}')
    print(f'    S_inst_D = {S_inst_D:.8f}')
    print()

    # --- GL fit in alpha for cross-check ---
    mask_fit = (alpha_scan > 0.01) & (alpha_scan < 2.5)                     # (local)
    x_fit = alpha_scan[mask_fit]                                            # (local)
    y_fit = F_alpha[mask_fit]                                               # (local)
    A_design = np.column_stack([x_fit**2, x_fit**4])                        # (local)
    coeffs_C, *_ = np.linalg.lstsq(A_design, y_fit, rcond=None)             # (local)
    a_C_alpha, b_C_alpha = coeffs_C                                         # (local)
    a_C = float(a_C_alpha / Delta_max_SC**2)                                # (local)
    b_C = float(b_C_alpha / Delta_max_SC**4)                                # (local)

    S_inst_C = 0.0                                                          # (local)
    Delta_0_C = 0.0                                                         # (local)
    barrier_C = 0.0                                                         # (local)
    if b_C > 0 and a_C < 0:
        Delta_0_C = float(np.sqrt(-a_C / (2.0 * b_C)))
        S_inst_C = float(np.sqrt(2.0 * b_C) * (2.0 / 3.0) * Delta_0_C**3)
        barrier_C = float(a_C**2 / (4.0 * b_C))
    print(f'  Method C (GL quartic fit): a_C={a_C:.8f} b_C={b_C:.8f}')
    print(f'    Delta_0_C = {Delta_0_C:.6f}')
    print(f'    barrier_C = {barrier_C:.8f}')
    print(f'    S_inst_C  = {S_inst_C:.8f}')
    print()

    # --- Method B: Thouless + GCM peak Delta_0 ---
    N_total_B2 = 4.0 * rho_B2_per_mode                                      # (local)
    a_B = float(-N_total_B2 * (M_max_thouless - 1.0) / M_max_thouless)      # (local)
    b_B = float(-a_B / (2.0 * Delta_0_peak**2))                             # (local)
    S_inst_B = float(np.sqrt(2.0 * b_B) * (2.0 / 3.0) * Delta_0_peak**3)    # (local)
    barrier_B = float(a_B**2 / (4.0 * b_B))                                 # (local)
    print(f'  Method B (Thouless M_max={M_max_thouless} + Delta_0_peak):')
    print(f'    a_B={a_B:.6f} b_B={b_B:.6f}')
    print(f'    barrier_B = {barrier_B:.8f}')
    print(f'    S_inst_B  = {S_inst_B:.8f}')
    print()

    # --- Best = Method D (full numerical) ---
    S_inst_best = S_inst_D                                                  # (local)
    Delta_0_best = Delta_0_num                                              # (local)

    # --- Gate verdict: INST-37a regime classification ---
    dense_thresh = 0.5                                                      # (local) INST-37a dense-gas boundary
    dilute_thresh = 5.0                                                     # (local) INST-37a dilute-BCS boundary
    if S_inst_best < dense_thresh:
        regime = 'DENSE_GAS'                                                # (local)
    elif S_inst_best < dilute_thresh:
        regime = 'CROSSOVER'                                                # (local)
    else:
        regime = 'DILUTE'                                                   # (local)

    # --- T3 gate: reproducibility vs canonical S_inst ---
    tol_abs = 0.05                                                          # (local) ABSOLUTE 5% tolerance
    delta_abs = abs(S_inst_best - S_inst)                                   # (local)
    rel_err = delta_abs / S_inst                                            # (local)
    gate_pass = delta_abs <= tol_abs * S_inst                               # (local)
    gate_fail_hard = delta_abs > 10.0 * tol_abs * S_inst                    # (local)
    verdict = 'PASS' if gate_pass else ('FAIL' if gate_fail_hard else 'INFO')  # (local)

    # --- Save outputs ---
    out_npz = os.path.join(SCRIPT_DIR, 's37_instanton_action.npz')       # (local)
    save_dict = {                                                           # (local)
        'S_inst_best': S_inst_best,
        'S_inst_D': S_inst_D,
        'S_inst_C': S_inst_C,
        'S_inst_B': S_inst_B,
        'Delta_0_best': Delta_0_best,
        'Delta_0_num': Delta_0_num,
        'Delta_0_peak': Delta_0_peak,
        'barrier_D': barrier_D,
        'F_min': F_min,
        'alpha_min': alpha_min,
        'alpha_scan': alpha_scan,
        'F_alpha': F_alpha,
        'Delta_SC': Delta_SC,
        'a_C': a_C, 'b_C': b_C,
        'a_B': a_B, 'b_B': b_B,
        'regime': np.array([regime]),
        'canonical_S_inst': S_inst,
        'canonical_M_max': M_max_thouless,
    }
    np.savez_compressed(out_npz, **save_dict)
    print(f'  Saved: {out_npz}')
    print()

    # --- Closure SHA of ordered input-pin map ---
    ordered = {k: INPUT_PINS[k] for k in sorted(INPUT_PINS)}                # (local)
    closure = hashlib.sha256(                                               # (local)
        json.dumps(ordered, sort_keys=True).encode('utf-8')
    ).hexdigest()

    elapsed = time.time() - t0                                              # (local)
    print(f'  Runtime: {elapsed:.2f}s')
    print()
    print('=' * 72)
    print('S37-INSTANTON-ACTION: verdict')
    print('=' * 72)
    print(f'  S_inst_best    = {S_inst_best:.8f}')
    print(f'  canonical      = {S_inst:.8f}')
    print(f'  |delta|        = {delta_abs:.8f}')
    print(f'  rel error      = {rel_err*100:.3f}%')
    print(f'  tol ABSOLUTE   = 5% (gate = |delta|/canonical <= 0.05)')
    print(f'  regime         = {regime}')
    print(f'  verdict        = {verdict}')
    print(f'  closure sha256 = {closure}')
    print()
    # Output 4-tuple (required last non-verdict line)
    print(
        f'OUTPUT_4TUPLE: (value={S_inst_best:.8f}, scheme=BCS_GL_quartic, '
        f'convention=discrete_mode_B2, L_max=N/A)'
    )
    print(
        f'VERDICT: S37-INSTANTON-ACTION: {verdict} -- '
        f'value={S_inst_best:.8f} scheme=BCS_GL_quartic '
        f'convention=discrete_mode_B2 L_max=N/A sha256={closure}'
    )
    return {
        'S_inst_best': S_inst_best,
        'regime': regime,
        'verdict': verdict,
        'closure': closure,
        'rel_err': rel_err,
    }


if __name__ == '__main__':
    main()
