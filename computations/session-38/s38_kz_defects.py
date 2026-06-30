"""
S38-KZ-DEFECTS:  re-run of s38_kz_defects.py
======================================================

Original: computations/session-38/s38_kz_defects.py (SHA-256 head 16: bd6dc37147c83bfa)

Purpose
-------
Reproduce the S38 KZ defect/excitation computation under S81 canonical
discipline:
  - Framework constants imported from canonical_constants.py
  - Intermediates tagged `# (local)`
  - SHA-256 pins emitted for every input npz in the first lines of stdout
  - Closure SHA emitted at the end; output 4-tuple line printed last

Gate
----
C-4 / KZ-COSMO — REFORMULATED: original n_defect*Vol(4D)>1 criterion is
ILL-POSED for 0D pairing. Reformulated as P_exc > 0.5.

Substitution chain (KZ exponent, sign of defect-density response)
-----------------------------------------------------------------
Defs:
  nu_exp = 0.5                                (BCS mean-field)
  z_exp  = 2.0                                (BCS dynamical)
  kz_exp = nu_exp / (1 + z_exp*nu_exp)        (KZ exponent)
  xi_KZ  = xi_0 * (tau_Q/tau_0)^{kz_exp}      (KZ scaling)
  adiab  = tau_Q / tau_0
Substitute:
  kz_exp = 0.5 / (1 + 2.0*0.5) = 0.5/2.0 = 0.25
Simplify:
  xi_KZ/xi_0 = adiab^{0.25}
  n_def_1d   = 1/xi_KZ
Direction:
  adiab < 1  =>  adiab^{0.25} < 1  =>  xi_KZ_formal < xi_0
  Physically xi_KZ cannot drop below xi_0 => floor at xi_0 (sudden-quench).
  Smaller xi_KZ raises n_def_1d; xi_KZ floor caps n_def_1d at 1/xi_0.
Therefore: tau_Q/tau_0 << 1 (adiab << 1) ⇒ SUDDEN QUENCH, P_exc = 1.
"""

import hashlib
import json
import os
import sys

import numpy as np

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

# --- canonical constants (MANDATORY S34+) ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                  # (local)
COMP_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))                # (local)
if COMP_DIR not in sys.path:
    sys.path.insert(0, COMP_DIR)
from canonical_constants import *  # noqa: E402,F401,F403

# We reference these canonical names explicitly:
#   tau_fold, xi_BCS, xi_GL, omega_PV, v_terminal, dt_transit, a_GL, b_GL,
#   E_cond, H_fold
# They are imported via `from canonical_constants import *`.

ARCHIVE_DIR = os.path.abspath(os.path.join(COMP_DIR, "..", "_shared"))  # (local)

# --- input SHA-256 pins (precomputed, 2026-04-17) ---
INPUT_PINS = {                                                            # (local)
    's36_tau_dynamics.npz':
        '257cb18ee5c65a7a34341b04cd461baa55075ce077dca407277dadc668623449',
    's37_instanton_action.npz':
        'b0b19cc9f2694ef4dafc8da70cfd9d373d16f33a89d87fa68759856397f520a1',
    's37_instanton_mc.npz':
        '21b69c8050ed5ff2d47f2969f68ab9cf1a2df15d294f8e1897538ebc867b33f7',
    's36_bdi_winding.npz':
        '9c245b33795e159bb11c6adaff7921f532a58bc1c40dc9856e0ffb86bcf599e3',
    's37_pair_susceptibility.npz':
        'a21910055a772ce7228e5b011815e71652ac1e1fd60bd344516c168e44268f61',
}


def sha256_of_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_pins():
    print('=' * 72)
    print('S38-KZ-DEFECTS: SHA-256 input pins')
    print('=' * 72)
    for name, expected in INPUT_PINS.items():
        path = os.path.join(ARCHIVE_DIR, name)
        actual = sha256_of_file(path)
        match = 'OK' if actual == expected else 'MISMATCH'
        print(f'  {name:<32s} {actual[:16]}...  [{match}]')
        if actual != expected:
            raise RuntimeError(
                f'SHA mismatch for {name}: expected {expected}, got {actual}'
            )
    print()


def load_inputs():
    ad = ARCHIVE_DIR
    d36 = np.load(os.path.join(ad, 's36_tau_dynamics.npz'), allow_pickle=True)
    d37 = np.load(os.path.join(ad, 's37_instanton_action.npz'), allow_pickle=True)
    d37mc = np.load(os.path.join(ad, 's37_instanton_mc.npz'), allow_pickle=True)
    d36bdi = np.load(os.path.join(ad, 's36_bdi_winding.npz'), allow_pickle=True)
    d37ps = np.load(os.path.join(ad, 's37_pair_susceptibility.npz'), allow_pickle=True)
    return d36, d37, d37mc, d36bdi, d37ps


def main():
    verify_pins()

    d36, d37, d37mc, d36bdi, d37ps = load_inputs()

    # --- transit parameters ---
    # Source: s36 trajectory integration; cross-check against canonical.
    v_term_data = float(d36['an_S_full_v_terminal'])          # (local) ~-26.545
    dt_transit_data = float(d36['an_S_full_dt_transit'])      # (local) ~1.13e-3
    BCS_lo = float(d36['BCS_window_lo'])                      # (local) 0.175
    BCS_hi = float(d36['BCS_window_hi'])                      # (local) 0.205
    Delta_tau_win = float(d36['window_width'])                # (local) 0.030
    tau_fold_data = float(d36['tau_fold'])                    # (local) 0.19016
    H_fold_data = float(d36['an_S_full_H_fold'])              # (local) 586.5

    # Cross-check canonical vs stored (do not modify canonical here)
    assert abs(abs(v_term_data) - v_terminal) / v_terminal < 1e-6, \
        f'v_terminal drift: data={abs(v_term_data):.6f}, canonical={v_terminal:.6f}'
    assert abs(dt_transit_data - dt_transit) / dt_transit < 1e-6, \
        f'dt_transit drift: data={dt_transit_data:.6e}, canonical={dt_transit:.6e}'
    assert abs(tau_fold_data - tau_fold) / tau_fold < 1e-3, \
        f'tau_fold drift: data={tau_fold_data:.5f}, canonical={tau_fold:.5f}'
    assert abs(H_fold_data - H_fold) / H_fold < 1e-6, \
        f'H_fold drift: data={H_fold_data:.2f}, canonical={H_fold:.2f}'

    # --- gap/coherence inputs ---
    Delta_0_peak = float(d37['Delta_0_peak'])                 # (local) 0.7704
    xi_BCS_data = float(d37['xi_BCS'])                        # (local) 0.8083
    S_inst = float(d37['S_inst_D'])                           # (local) 0.0686
    a_GL_data = float(d37['a_A'])                             # (local) -0.5245
    b_GL_data = float(d37['b_A'])                             # (local)  0.4419
    E_cond_data = float(d37['E_cond_use'])                    # (local) -0.1557

    xi_GL_data = float(d37mc['xi_GL'])                        # (local) 0.9763
    L_sys = float(d37mc['L'])                                 # (local) 0.03
    L_over_xi_GL = float(d37mc['L_over_xi_GL'])               # (local) 0.031

    nu_winding_val = int(d36bdi['nu_winding'])                # (local) 0
    omega_PV_data = float(d37ps['omega_plus'])                # (local) 0.792
    E_vac_Econd_ratio = float(d37ps['ratio_Evac_Econd'])      # (local) 28.76

    # xi_BCS, xi_GL, omega_PV, a_GL, b_GL are in canonical; assert coherence.
    assert abs(xi_BCS_data - xi_BCS) / xi_BCS < 1e-6
    assert abs(xi_GL_data - xi_GL) / xi_GL < 1e-6
    assert abs(omega_PV_data - omega_PV) / omega_PV < 1e-6
    assert abs(a_GL_data - a_GL) / abs(a_GL) < 1e-6
    assert abs(b_GL_data - b_GL) / b_GL < 1e-6

    # --- KZ critical exponents (BCS mean-field) ---
    nu_exp = 0.5                                              # (local)
    z_exp = 2.0                                               # (local)
    kz_exp = nu_exp / (1.0 + z_exp * nu_exp)                  # (local) = 0.25

    # --- microscopic scales ---
    xi_0 = xi_BCS_data                                        # (local)
    tau_0_gap = 1.0 / Delta_0_peak                            # (local)
    tau_0_pv = 1.0 / omega_PV_data                            # (local)
    V_curvature = -2 * a_GL_data + 12 * b_GL_data * Delta_0_peak ** 2  # (local)
    tau_GL = (1.0 / np.sqrt(abs(V_curvature)) if V_curvature > 0
              else 1.0 / np.sqrt(abs(2 * a_GL_data)))         # (local)

    tau_0 = tau_0_gap                                         # (local) canonical choice

    # --- KZ correlation length ---
    tau_Q_natural = dt_transit_data                           # (local)
    adiabaticity = tau_Q_natural / tau_0                      # (local)
    xi_KZ_formula = xi_0 * adiabaticity ** kz_exp             # (local)
    if adiabaticity < 1:
        xi_KZ = xi_0                                          # (local) sudden-quench floor
    else:
        xi_KZ = xi_KZ_formula                                 # (local)

    # --- defect density ---
    n_defect_1d = 1.0 / xi_KZ                                 # (local) per unit tau
    N_defect_window = Delta_tau_win / xi_KZ                   # (local) in BCS window

    # --- Landau-Zener (per mode) / Schwinger analog ---
    delta_tau_half = Delta_tau_win / 2.0                      # (local)
    dDelta_dtau = Delta_0_peak / delta_tau_half               # (local)
    dDelta_dt = dDelta_dtau * abs(v_term_data)                # (local)
    lz_exponent = np.pi * Delta_0_peak ** 2 / (2 * dDelta_dt) # (local)
    P_LZ = float(np.exp(-lz_exponent))                        # (local)
    n_Bog_exp = np.pi * Delta_0_peak ** 2 / abs(dDelta_dt)    # (local)
    n_Bog = float(np.exp(-n_Bog_exp))                         # (local)

    # P_exc from KZ scaling:
    # P_exc = (tau_0/tau_Q)^{2 nu z / (1+z nu)} = (tau_0/tau_Q)^1 for BCS
    raw_P_exc = (tau_0 / tau_Q_natural) ** (
        2 * nu_exp * z_exp / (1 + z_exp * nu_exp)
    )                                                         # (local)
    P_exc_kz = float(min(raw_P_exc, 1.0))                     # (local) saturated

    # --- per-mode pair creation (match original) ---
    E_modes = np.array(
        [0.8453, 0.8453, 0.8453, 0.8453, 0.8191, 0.9782, 0.9782, 0.9782]
    )                                                         # (local)
    rho_modes = np.array(
        [14.023, 14.023, 14.023, 14.023, 1.0, 1.0, 1.0, 1.0]
    )                                                         # (local)
    E_exc_total = 0.0                                         # (local) accumulator
    for i in range(len(E_modes)):
        E_qp_i = np.sqrt(E_modes[i] ** 2 + Delta_0_peak ** 2) # (local)
        E_exc_total += E_qp_i * rho_modes[i]
    n_excited = int(len(E_modes))                             # (local) sudden-quench: all modes excited

    # --- BDI / instanton damping ---
    Gamma_inst = omega_PV_data * np.exp(-S_inst)              # (local)
    t_ann = 1.0 / Gamma_inst                                  # (local)
    t_Hubble = 1.0 / H_fold_data if H_fold_data > 0 else float('inf')  # (local)
    ratio_ann_H = t_ann / t_Hubble                            # (local)

    # --- verdict (REFORMULATED: 0D pair => excitation prob) ---
    P_EXC_THRESH = 0.5                                        # (local) reformulated threshold
    reformulated_pass = bool(P_exc_kz > P_EXC_THRESH)         # (local)

    gate_verdict_str = "ILL-POSED / REFORMULATED"             # (local) legacy header
    # S81 machine-readable verdict:
    verdict_tag = "PASS" if reformulated_pass else "FAIL"     # (local)

    # --- report ---
    print('-' * 72)
    print('CORE RESULTS')
    print('-' * 72)
    print(f'  nu_exp             = {nu_exp}')
    print(f'  z_exp              = {z_exp}')
    print(f'  kz_exp             = {kz_exp:.6f}')
    print(f'  xi_0 (= xi_BCS)    = {xi_0:.6f}')
    print(f'  tau_0 (=1/Delta_0) = {tau_0:.6f}')
    print(f'  tau_Q (= dt_transit)= {tau_Q_natural:.6e}')
    print(f'  adiabaticity       = {adiabaticity:.6e}')
    print(f'  xi_KZ_formula      = {xi_KZ_formula:.6e}')
    print(f'  xi_KZ (physical)   = {xi_KZ:.6e}')
    print(f'  n_defect_1d        = {n_defect_1d:.6e}')
    print(f'  N_defect (window)  = {N_defect_window:.6e}')
    print(f'  P_exc_kz           = {P_exc_kz:.6f}')
    print(f'  P_LZ               = {P_LZ:.6e}')
    print(f'  n_Bog              = {n_Bog:.6e}')
    print(f'  E_exc_total        = {E_exc_total:.6f}')
    print(f'  E_cond             = {E_cond_data:.6f}')
    print(f'  E_exc/|E_cond|     = {E_exc_total / abs(E_cond_data):.4f}')
    print(f'  BDI nu_winding     = {nu_winding_val}')
    print(f'  Gamma_inst         = {Gamma_inst:.6f}')
    print(f'  t_ann              = {t_ann:.6f}')
    print(f'  t_Hubble           = {t_Hubble:.6e}')
    print(f'  ratio_ann_H        = {ratio_ann_H:.3f}')
    print(f'  n_excited (modes)  = {n_excited}')
    print()
    print(f'  Reformulated gate: P_exc > {P_EXC_THRESH} ?  ->  {verdict_tag}')
    print(f'  Legacy verdict    : {gate_verdict_str}')
    print()

    # --- save artifact ---
    out_npz = os.path.join(SCRIPT_DIR, 's38_kz_defects.npz')  # (local)
    np.savez(
        out_npz,
        nu_exp=nu_exp,
        z_exp=z_exp,
        kz_exp=kz_exp,
        xi_0=xi_0,
        tau_0=tau_0,
        tau_Q=tau_Q_natural,
        adiabaticity=adiabaticity,
        xi_KZ=xi_KZ,
        xi_KZ_formula=xi_KZ_formula,
        n_defect_1d=n_defect_1d,
        N_defect_window=N_defect_window,
        P_exc_kz=P_exc_kz,
        P_LZ=P_LZ,
        n_Bog=n_Bog,
        n_excited_modes=n_excited,
        E_exc_total=E_exc_total,
        E_cond=E_cond_data,
        Gamma_inst=Gamma_inst,
        t_annihilation=t_ann,
        t_Hubble=t_Hubble,
        ratio_ann_H=ratio_ann_H,
        BDI_nu=nu_winding_val,
        dDelta_dt=dDelta_dt,
        lz_exponent=lz_exponent,
        gate_verdict=np.array([gate_verdict_str]),
        reformulated_pass=reformulated_pass,
    )

    # --- closure SHA: sha256 of ordered input-pin map (hex-sorted keys) ---
    pin_blob = json.dumps(INPUT_PINS, sort_keys=True).encode()  # (local)
    closure_sha = hashlib.sha256(pin_blob).hexdigest()         # (local)

    # --- output 4-tuple + closure (last non-verdict lines) ---
    value_out = P_exc_kz                                       # (local) decisive scalar
    scheme = 'BCS_meanfield_KZ'                                # (local)
    convention = '0D_pair_reformulated'                        # (local)
    L_max = 'N/A_KZ'                                           # (local)

    print('=' * 72)
    print('OUTPUT 4-TUPLE')
    print('=' * 72)
    print(f'value={value_out:.6f} scheme={scheme} convention={convention} L_max={L_max}')
    print(f'closure_sha256={closure_sha}')
    print('=' * 72)


if __name__ == '__main__':
    main()
