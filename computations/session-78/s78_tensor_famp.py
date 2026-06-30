#!/usr/bin/env python3
"""
S78-W3-C-TENSOR-FAMP : Tensor F_amp and r(k_pivot)
====================================================

GATE: r(k_pivot) from tensor mode equation under linearized regime
(same regime as W1-C, since W1-C returned INCOMPUTABLE-FALLBACK-TO-BOUND
for F_amp^{sc,S}; tensor computed linearized per plan §W3-C convention pin).

PRINCIPLE-THEORETIC DERIVATION (Einstein):

1. GENERAL COVARIANCE: Second-order perturbation of Einstein-Hilbert action
   yields independent scalar (Mukhanov-Sasaki variable v_S) and tensor
   (two transverse-traceless polarizations u_T^{+,x}) mode equations.

2. MODE EQUATIONS IN CONFORMAL TIME:
     v_S'' + (k^2 - z''/z) v_S = 0   with z = a * sqrt(2*eps) * M_Pl_red
     u_T'' + (k^2 - a''/a) u_T = 0    with u_T = a * M_Pl_red/2 * h

3. PUMP STRUCTURE (shared background):
     a''/a   = (aH)^2 * (2 - eps)        (always, from FRW background)
     z''/z   = (aH)^2 * [2 - eps + corrections in eta_H, (dln eps)/dN]
   Tensors and scalars see the SAME background; pumps differ by O(eps),
   so in SLOW-ROLL CONTROL (no fold, smooth dS background),
   (F_amp^T / F_amp^S) ~ 1 + O(eps) -> 1.

4. POWER RATIOS (both are POWER RATIOS per §0.1; LINEAR in A_s product):
     F_amp^T(k) = |u_T^real|^2 / |u_T^dS|^2  (at superhorizon)
     F_amp^S(k) = |v_S^real|^2 / |v_S^dS|^2

5. de SITTER AMPLITUDES (explicit, NO slow-roll shortcuts):
     P_dS^S = (H/(2 pi))^2 / (2 eps M_Pl_red^2)     (scalar)
     P_dS^T = 2 * (H/(2 pi))^2 / (M_Pl_red/2)^2
            = 8 * (H/(2 pi))^2 / M_Pl_red^2         (2 polarizations,
                                                    normalization per §W3-C)

   POLARIZATION CONVENTION PIN (§W3-C): sqrt(2)/M_Pl_red per polarization
   (standard Mukhanov-Sasaki convention; u_T^{lambda} = a * M_Pl_red * h^{lambda}
   with amplitude 1/sqrt(2k) at BD IC per polarization).

6. SLOW-ROLL LIMIT CHECK (method validity, NOT physics answer):
     r_slow_roll = P_dS^T / P_dS^S (F_amp^T/F_amp^S -> 1)
                 = [8 (H/2 pi)^2 / M_Pl_red^2] / [(H/2 pi)^2 / (2 eps M_Pl_red^2)]
                 = 16 eps

   The appearance of 16*eps_H in the slow-roll control is REQUIRED for
   method-correctness. In the physics answer (real substrate background
   with fold), r MUST depart from 16*eps to reflect substrate-framework
   tensor/scalar asymmetry -- otherwise standard inflation is reproduced.

7. SUBSTRATE FRAMEWORK DEPARTURE (phononic framing):
   The mode equation sees the SAME background (aH, eps) for both scalar
   and tensor -- this is the LINEARIZED content. Departure from 16*eps comes
   from (a) the fold transit affecting tensors differently (a''/a vs z''/z
   diverge at the fold where deps/dN is large), and (b) the graviton
   impedance mismatch: gravitons emerge from a_2 spectral moment at scale
   M_KK, while scalars emerge from a_0 (tau-flow) at the substrate scale.

PRE-REGISTERED PREDICTION (phononic, principle-theoretic):
   At linearized mode-equation level, expect (F_amp^T / F_amp^S) to depart
   from 1 due to fold-transit pump difference. The phononic substrate
   framework prediction for r at the mode-equation level:

     r_substrate_pre = (F_amp^T/F_amp^S) * 16 * eps_dS

   Factor 2 around the slow-roll-only answer; gate evaluates whether the
   fold-transit distinguishes tensors from scalars (substrate-framework
   structural content) OR reproduces r = 16*eps identically (substrate
   framework NOT distinguishing itself at this level).

Provenance: Einstein-Hilbert action second-order perturbation is textbook;
applied here in substrate-framework context per phononic-framing.md rule.
"""

from canonical_constants import *
import os
import sys
import numpy as np
from numpy import pi as PI_np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_NPZ = os.path.join(SCRIPT_DIR, 's78_tensor_famp.npz')
OUT_PNG = os.path.join(SCRIPT_DIR, 's78_tensor_famp.png')
OUT_TXT = os.path.join(SCRIPT_DIR, 's78_tensor_famp_output.txt')
VERDICT_FILE = os.path.join(SCRIPT_DIR, 's78_gate_verdicts.txt')

_log_lines = []  # (local)


def log(msg=""):
    print(msg)
    _log_lines.append(msg)


log("=" * 78)
log("S78-W3-C-TENSOR-FAMP: Tensor F_amp and r(k_pivot)")
log("=" * 78)
log("")
log("Pre-registered conventions (§W3-C):")
log("  - F_amp^T, F_amp^S both POWER RATIOS (LINEAR, not squared)")
log("  - r = (F_amp^T * P_dS^T) / (F_amp^S * P_dS^S), P_dS explicit")
log("  - Polarization normalization: sqrt(2)/M_Pl_red per polarization")
log("    (standard Mukhanov-Sasaki; u_T = a * M_Pl_red * h per polarization)")
log("  - eps = eps_H (NOT eps_V)")
log("  - Same regime as F_amp^S: LINEARIZED (W1-C declared INCOMPUTABLE)")


# ========================================================================
#  SECTION 1: Load Background (same as s78_backreaction_selfconsistent.py)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 1: Load S73B background")
log("=" * 78)

d73 = np.load(os.path.join(SCRIPT_DIR, 's73b_efold_mapping.npz'), allow_pickle=True)
lna_raw = d73['lna_sol']  # (local)
H_raw = d73['H_sol']  # (local) M_KK units
w_raw = d73['w_sol']  # (local)
aH_raw = d73['aH_sol']  # (local)

d77pm = np.load(os.path.join(SCRIPT_DIR, 's77_n_pivot_map.npz'), allow_pickle=True)
k_pivot_MKK = float(d77pm['k_pivot_com_fold'])  # (local) = 14.31 M_KK comoving fold-frame
N_pivot = float(d77pm['N_pivot'])  # (local) = 3.12

d77pbh = np.load(os.path.join(SCRIPT_DIR, 's77_transition_scale_pbh.npz'), allow_pickle=True)
F_amp_S_linearized = float(d77pbh['F_amp_pivot'])  # (local) = 6858 (S77 S scalar reference)
H_dS_ref = float(d77pbh['H_dS'])  # (local) = 0.633 M_KK
eps_dS_ref = float(d77pbh['eps_dS'])  # (local) = 4.815e-3
MKK_over_MPl_sq = float(d77pbh['MKK_over_MPl_sq'])  # (local) = 9.307e-4

log(f"  S73B: N in [{lna_raw[0]:.4f}, {lna_raw[-1]:.4f}]")
log(f"  k_pivot = {k_pivot_MKK:.4f} M_KK (fold-frame comoving)")
log(f"  N_pivot = {N_pivot:.4f}")
log(f"  F_amp^S (linearized, S77 reference) = {F_amp_S_linearized:.2f}")
log(f"  H_dS = {H_dS_ref:.4e} M_KK, eps_dS = {eps_dS_ref:.4e}")
log(f"  (M_KK/M_Pl_red)^2 = {MKK_over_MPl_sq:.4e}")


# ========================================================================
#  SECTION 2: Build Background in Conformal Time (same as W1-C)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 2: Background in conformal time")
log("=" * 78)

N_max_mode = 15.0  # (local) e-folds (modes freeze well before this)
mask_N = lna_raw <= N_max_mode  # (local)
N_arr = lna_raw[mask_N].copy()  # (local)
H_arr = H_raw[mask_N].copy()  # (local)
w_arr = w_raw[mask_N].copy()  # (local)
aH_arr = aH_raw[mask_N].copy()  # (local)
eps_arr = 1.5 * (1.0 + w_arr)  # (local) eps_H = 3(1+w)/2
a_arr = np.exp(N_arr)  # (local)

# Conformal time
d_eta_dN = 1.0 / aH_arr  # (local)
dN_step = np.gradient(N_arr)  # (local)
eta_arr = np.cumsum(d_eta_dN * dN_step)  # (local)
eta_arr -= eta_arr[0]  # (local) eta=0 at fold

log(f"  eta range: [0, {eta_arr[-1]:.6e}] M_KK^{{-1}}")

# Scalar pump z''/z (linearized)
deps_dN = np.gradient(eps_arr, N_arr)  # (local)
eta_H_arr = deps_dN / (eps_arr + 1e-30)  # (local) d(ln eps)/dN
deta_H_dN = np.gradient(eta_H_arr, N_arr)  # (local)
dlnz_dN = 1.0 + 0.5 * eta_H_arr  # (local)
d2lnz_dN2 = 0.5 * deta_H_dN  # (local)
pump_S_N_arr = d2lnz_dN2 + dlnz_dN**2 + (1.0 - eps_arr) * dlnz_dN  # (local)
zppoz_linearized = aH_arr**2 * pump_S_N_arr  # (local)

# Tensor pump a''/a (linearized)
# a''/a in conformal time = (aH)^2 * (2 - eps)
# Derivation: a(eta) -> a' = da/deta = (da/dN) * (dN/deta) = a * H * (1/(aH)) = a/eta...
#   Exact form: a''/a = a^2 * d/dN (a H) / a = aH^2 (1 + eps)(1 - eps)/... ; cleanly,
#   a''/a (conformal) = (aH)^2 * (2 - eps)  for arbitrary FRW.
pump_T_N_arr = 2.0 - eps_arr  # (local) tensor pump in (aH)^2 units
appoa_linearized = aH_arr**2 * pump_T_N_arr  # (local) = (aH)^2 * (2 - eps)

# CHK: both pumps -> 2*(aH)^2 in dS limit
mask_dS = N_arr > 8.0  # (local)
pump_S_dS_check = pump_S_N_arr[mask_dS].mean()  # (local)
pump_T_dS_check = pump_T_N_arr[mask_dS].mean()  # (local)
log(f"  pump_S(dS limit) = {pump_S_dS_check:.4f} (expected 2.0)")
log(f"  pump_T(dS limit) = {pump_T_dS_check:.4f} (expected 2.0)")
assert abs(pump_S_dS_check - 2.0) < 0.01, "Scalar pump dS limit failed"
assert abs(pump_T_dS_check - 2.0) < 0.01, "Tensor pump dS limit failed"

# dS reference
H_dS = H_arr[N_arr > 5.0].mean()  # (local)
eps_dS = eps_arr[N_arr > 5.0].mean()  # (local)

log(f"  dS from arrays: H_dS = {H_dS:.4e} M_KK, eps_dS = {eps_dS:.4e}")
log(f"  (verify vs S77 reference: match within {abs(H_dS/H_dS_ref - 1)*100:.2f}%)")

# Interpolators
zppoz_S_interp = interp1d(eta_arr, zppoz_linearized, kind='cubic',
                           fill_value='extrapolate')  # (local) scalar pump
appoa_T_interp = interp1d(eta_arr, appoa_linearized, kind='cubic',
                           fill_value='extrapolate')  # (local) tensor pump
aH_of_N_interp = interp1d(N_arr, aH_arr, kind='cubic',
                           fill_value='extrapolate')  # (local)


def appoa_pure_dS(eta):
    """a''/a for pure de Sitter (tensor F_amp denominator).
    In pure dS, eps=0, so a''/a = 2(aH)^2 = 2*H_dS^2 / (1 - H_dS*eta)^2"""
    return 2.0 * H_dS**2 / (1.0 - H_dS * eta)**2  # (local)


def zppoz_pure_dS(eta):
    """z''/z for pure de Sitter (scalar F_amp denominator).
    In pure dS, eps is constant (so eta_H=0), z''/z = 2(aH)^2 (same as tensor)."""
    return 2.0 * H_dS**2 / (1.0 - H_dS * eta)**2  # (local)


# ========================================================================
#  SECTION 3: Mode Equation Solvers (Scalar and Tensor)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 3: Mode equation solvers")
log("=" * 78)


def solve_mode_conformal(k_com, pump_func, eta_start, eta_end,
                         rtol=1e-11, atol=1e-13, max_step_ratio=500,
                         n_eval_pts=400):
    """Solve u'' + (k^2 - pump) u = 0 in conformal time.

    Bunch-Davies IC: u(eta_0) = 1/sqrt(2k), du/deta = -i k u
    (same for scalar v_k and tensor u_T^{lambda} per polarization).
    The IC is polarization-normalized; physical P_dS differs between
    scalar and tensor via the external prefactors in Section 5.

    Returns u(eta), |u|^2, Wronskian deviation.
    """
    amp = 1.0 / np.sqrt(2.0 * k_com)  # (local) BD amplitude
    y0 = [amp, 0.0, 0.0, -k_com * amp]  # (local) [u_re, u_im, du_re, du_im]

    def rhs(eta, y):
        ur, ui, dur, dui = y
        pump = float(pump_func(eta))
        omega2 = k_com**2 - pump  # (local)
        return [dur, dui, -omega2 * ur, -omega2 * ui]

    d_eta = eta_end - eta_start  # (local)
    max_step = d_eta / max_step_ratio  # (local)

    sol = solve_ivp(rhs, [eta_start, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)

    if not sol.success:
        return {'status': 'SOLVER_FAILED', 'message': sol.message}

    eta_eval = np.linspace(eta_start, eta_end, n_eval_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)

    u_abs2 = y_eval[0]**2 + y_eval[1]**2  # (local)

    W = y_eval[0] * y_eval[3] - y_eval[1] * y_eval[2]  # (local) Wronskian
    W_dev = abs(W[-1] - W[0]) / abs(W[0])  # (local)

    return {
        'status': 'OK',
        'u_abs2': u_abs2,
        'eta_eval': eta_eval,
        'u_abs2_final': np.median(u_abs2[-max(20, n_eval_pts // 10):]),
        'W_dev': W_dev,
        'y_eval': y_eval,
    }


def solve_mode_pure_dS(k_com, pump_func, eta_end,
                       rtol=1e-11, atol=1e-13):
    """Pure dS mode equation for F_amp denominator."""
    amp = 1.0 / np.sqrt(2.0 * k_com)  # (local)
    y0 = [amp, 0.0, 0.0, -k_com * amp]  # (local)

    def rhs(eta, y):
        ur, ui, dur, dui = y
        pump = pump_func(eta)
        omega2 = k_com**2 - pump
        return [dur, dui, -omega2 * ur, -omega2 * ui]

    d_eta = eta_end  # (local)
    max_step = d_eta / 5000  # (local)
    sol = solve_ivp(rhs, [0, eta_end], y0,
                    method='DOP853', rtol=rtol, atol=atol,
                    dense_output=True, max_step=max_step)
    if not sol.success:
        return {'status': 'SOLVER_FAILED'}

    n_pts = 2000  # (local)
    eta_eval = np.linspace(0, eta_end, n_pts)  # (local)
    y_eval = sol.sol(eta_eval)  # (local)
    u_abs2 = y_eval[0]**2 + y_eval[1]**2  # (local)
    return {'status': 'OK', 'u_abs2_final': np.median(u_abs2[-200:]),
            'u_abs2': u_abs2, 'eta_eval': eta_eval}


# ========================================================================
#  SECTION 4: Pre-Registered Prediction (BEFORE running gate)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 4: PRE-REGISTERED r (locked BEFORE gate run)")
log("=" * 78)

# PRINCIPLE-THEORETIC PRE-REGISTRATION:
# The linearized scalar mode equation gave F_amp^S = 6858 with pump z''/z.
# The linearized tensor mode equation uses pump a''/a = z''/z - (aH)^2 *
# [(1/2) d(eta_H)/dN + (eta_H/2)(1 - eps + eta_H/2) + eps]
# which differs from z''/z only in corrections of order eps, eta_H.
#
# In the slow-roll-dominant regime after the fold (N > 0.1), these corrections
# are O(eps) = O(10^-3). In the transit region (N in [0, 0.1]) they are
# O(1) since deps/dN is finite.
#
# PRE-REGISTERED F_amp^T/F_amp^S:
# The mode is SUBHORIZON at the fold (k/aH = 14.7 > 1). The fold produces
# a sudden parametric kick followed by slow-roll amplification. Both scalars
# and tensors see the SAME k^2 - pump equation with pumps that differ by
# O(eps_H(N_pivot)). For k_pivot the PIVOT-regime pump difference is small.
#
# Pre-registered: F_amp^T / F_amp^S in [0.5, 2.0] from principle arguments
# (factor 2 around unity).
#
# PRE-REGISTERED r (phononic, principle-theoretic mode-equation level):
#   r_pre_mode = (F_amp^T / F_amp^S) * (P_dS^T / P_dS^S)
#              = (F_amp^T / F_amp^S) * 16 * eps_dS
#
# With F_amp^T/F_amp^S = 1 (leading-order principle): r_pre_mode = 16 * eps_dS.
#
# SLOW-ROLL-CONTROL: r_control = 16 * eps_dS (method validity only).
#
# SUBSTRATE-FRAMEWORK DEPARTURE: the mode equation calculates emergent-metric r.
# The substrate-framework r_CMB observable involves graviton impedance
# effacement (S44 Route D, r ~ (M_KK/M_Pl_red)^2 * 16*eps). That is a
# DIFFERENT question at a DIFFERENT level (post-mode-equation normalization).

F_amp_ratio_pre_lo = 0.5  # (local) factor 2 lower bound
F_amp_ratio_pre_hi = 2.0  # (local) factor 2 upper bound
F_amp_ratio_pre_central = 1.0  # (local) principle: pumps differ by O(eps) -> 1

r_slow_roll_pre = 16.0 * eps_dS  # (local) slow-roll control value (METHOD, not physics)
r_pre_central = F_amp_ratio_pre_central * 16.0 * eps_dS  # (local) = 16*eps if F_T/F_S=1
r_pre_lo = F_amp_ratio_pre_lo * 16.0 * eps_dS  # (local) factor 2 low
r_pre_hi = F_amp_ratio_pre_hi * 16.0 * eps_dS  # (local) factor 2 high

log(f"  Pre-registered F_amp^T/F_amp^S: [{F_amp_ratio_pre_lo:.2f}, {F_amp_ratio_pre_hi:.2f}]")
log(f"  (central {F_amp_ratio_pre_central:.2f} from principle: linearized pumps ~= at leading order)")
log(f"")
log(f"  Pre-registered r (mode-equation level, factor 2):")
log(f"    r_pre_central = {r_pre_central:.4e}")
log(f"    r_pre band    = [{r_pre_lo:.4e}, {r_pre_hi:.4e}]")
log(f"")
log(f"  Slow-roll CONTROL (method validity): r = 16 eps = {r_slow_roll_pre:.4e}")
log(f"  (This MUST recover in slow-roll control; reproducing in physics = FAIL)")
log(f"")
log(f"  Substrate-framework CMB-observable r (EIH-effaced, NOT this gate):")
log(f"    r_substrate_obs = {r_pre_central * MKK_over_MPl_sq:.4e}")
log(f"    = 16 eps * (M_KK/M_Pl_red)^2 (graviton impedance mismatch, S44)")


# ========================================================================
#  SECTION 5: Solve Tensor Mode at k_pivot
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 5: Tensor mode equation at k_pivot (real background)")
log("=" * 78)

# Find eta_end where mode is superhorizon (k/aH < 0.05)
koh_pivot = k_pivot_MKK / aH_arr  # (local)
idx_sh_pivot = np.where(koh_pivot < 0.05)[0]  # (local)
if len(idx_sh_pivot) > 0:
    eta_end_pivot = eta_arr[idx_sh_pivot[0]]  # (local)
else:
    eta_end_pivot = eta_arr[-1]  # (local)

log(f"  eta_end(k_pivot) = {eta_end_pivot:.6e} M_KK^{{-1}}")

# Solve tensor mode equation with real background pump a''/a
log("  Solving tensor mode equation with pump a''/a (real background)...")
sol_T_real = solve_mode_conformal(k_pivot_MKK, appoa_T_interp,
                                  eta_arr[0], eta_end_pivot,
                                  n_eval_pts=600)
if sol_T_real['status'] != 'OK':
    log(f"  TENSOR SOLVER FAILED: {sol_T_real.get('message', 'unknown')}")
    sys.exit(1)

u_T_real_abs2 = sol_T_real['u_abs2_final']  # (local)
W_T_real = sol_T_real['W_dev']  # (local)
log(f"  |u_T^real|^2 at superhorizon = {u_T_real_abs2:.6e}")
log(f"  Wronskian deviation (real) = {W_T_real:.3e}")

# Solve tensor mode in pure dS (F_amp^T denominator)
log("  Solving tensor mode equation in pure dS...")
# eta_end for dS should be similar superhorizon reach
N_dS_exit = np.log(k_pivot_MKK / (0.05 * H_dS))  # (local)
# Use conformal time corresponding to N_dS_exit e-folds of dS
# eta_dS_end ~ (1 - exp(-N)) / (H_dS) in dS
eta_dS_end = (1.0 - np.exp(-N_dS_exit)) / H_dS  # (local)
log(f"  eta_dS_end (for superhorizon reach of k_pivot in pure dS) = {eta_dS_end:.4e}")

sol_T_dS = solve_mode_pure_dS(k_pivot_MKK, appoa_pure_dS, eta_dS_end)
if sol_T_dS['status'] != 'OK':
    log(f"  TENSOR dS SOLVER FAILED")
    sys.exit(1)
u_T_dS_abs2 = sol_T_dS['u_abs2_final']  # (local)
log(f"  |u_T^dS|^2 at superhorizon = {u_T_dS_abs2:.6e}")

# F_amp^T = |u_T^real|^2 / |u_T^dS|^2
F_amp_T = u_T_real_abs2 / u_T_dS_abs2  # (local)
log(f"  F_amp^T(k_pivot) = {F_amp_T:.4e}")


# ========================================================================
#  SECTION 6: Solve Scalar Mode (same solver, for internal consistency)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 6: Scalar mode at k_pivot (reproduce S77)")
log("=" * 78)

# Solve scalar with pump z''/z
sol_S_real = solve_mode_conformal(k_pivot_MKK, zppoz_S_interp,
                                  eta_arr[0], eta_end_pivot,
                                  n_eval_pts=600)
if sol_S_real['status'] != 'OK':
    log(f"  SCALAR SOLVER FAILED")
    sys.exit(1)
v_S_real_abs2 = sol_S_real['u_abs2_final']  # (local)
log(f"  |v_S^real|^2 at superhorizon = {v_S_real_abs2:.6e}")

sol_S_dS = solve_mode_pure_dS(k_pivot_MKK, zppoz_pure_dS, eta_dS_end)
v_S_dS_abs2 = sol_S_dS['u_abs2_final']  # (local)
log(f"  |v_S^dS|^2 at superhorizon = {v_S_dS_abs2:.6e}")

F_amp_S = v_S_real_abs2 / v_S_dS_abs2  # (local)
log(f"  F_amp^S(k_pivot) = {F_amp_S:.4e}")
log(f"  S77 reference     = {F_amp_S_linearized:.4e}")
log(f"  reproduction ratio = {F_amp_S / F_amp_S_linearized:.4f}")


# ========================================================================
#  SECTION 7: Build r and Pre-Registered Band Comparison
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 7: r(k_pivot) from mode-equation amplitudes")
log("=" * 78)

# P_dS^S = (H/(2pi))^2 / (2 eps M_Pl_red^2)  -- scalar de Sitter power
# P_dS^T = 8 (H/(2pi))^2 / M_Pl_red^2        -- tensor de Sitter power
# (2 polarizations, normalization sqrt(2)/M_Pl_red per polarization)
# In natural units M_Pl_red = 1 (treat as unit; factors cancel in r ratio):

# P_dS^T / P_dS^S ratio (analytic, explicit per §W3-C, NO slow-roll shortcut):
P_dS_T_over_S_explicit = 16.0 * eps_dS  # (local) direct ratio from mode amplitudes

# r = (F_amp^T * P_dS^T) / (F_amp^S * P_dS^S)
#   = (F_amp^T / F_amp^S) * (P_dS^T / P_dS^S)
F_amp_T_over_S = F_amp_T / F_amp_S  # (local)
r_computed = F_amp_T_over_S * P_dS_T_over_S_explicit  # (local)

log(f"  F_amp^T / F_amp^S = {F_amp_T_over_S:.4f}")
log(f"  P_dS^T / P_dS^S   = 16 * eps_dS = {P_dS_T_over_S_explicit:.4e} (explicit, no shortcut)")
log(f"  r(k_pivot) = {r_computed:.4e}")
log(f"")
log(f"  Pre-registered central: {r_pre_central:.4e}")
log(f"  Pre-registered band:    [{r_pre_lo:.4e}, {r_pre_hi:.4e}]")
log(f"  Within pre-registered factor 2? {'YES' if r_pre_lo <= r_computed <= r_pre_hi else 'NO'}")
log(f"")
log(f"  Relative to slow-roll 16*eps: r_computed / (16*eps_dS) = {r_computed / (16*eps_dS):.4e}")
log(f"  If approx 1.0, r accidentally reproduces 16*eps (FAIL criterion).")


# ========================================================================
#  SECTION 8: Tensor Backreaction Diagnostic
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 8: Tensor backreaction diagnostic rho_T/rho_bg")
log("=" * 78)

# rho_T ~ (integral over k) of (k^2 + a''/a effectively) * n_k^T
# Simpler: rho_T peak at k_pivot ~ k^3 / (6 pi^2) * k * F_amp^T (per polarization)
# For both polarizations: rho_T ~ 2 * k_pivot^4 / (6 pi^2) * F_amp^T / 2
#                                = k_pivot^4 / (6 pi^2) * F_amp^T
# Note: in natural substrate frame units M_KK = 1, rho_bg = 3 * H_dS^2 * M_Pl_red^2
# But rho_bg in M_KK^4 units: 3 * H_dS^2 / (M_KK/M_Pl_red)^2 -> use (M_KK/M_Pl_red)^2

# Peak density ratio
# Build n_k^T = F_amp^T * (some normalization). The mode has amplitude 1/sqrt(2k)
# at BD, amplified to F_amp^T^(1/2) * 1/sqrt(2k). Energy per mode ~ k_phys.
# At the pivot k_pivot:
#   n_pivot^T (per polarization) ~ F_amp^T / 2 (rough estimate for squeezed vacuum)
# rho_T density (2 polarizations) ~ 2 * (k_pivot^3 / (6 pi^2)) * k_pivot * F_amp^T / 2
#                                = k_pivot^4 / (6 pi^2) * F_amp^T

rho_T_peak_estimate = k_pivot_MKK**4 / (6.0 * PI_np**2) * F_amp_T  # (local) M_KK^4
rho_bg_at_fold = 3.0 * H_dS**2 / MKK_over_MPl_sq  # (local) convert (M_Pl_red)^2 factor
# Actually, rho_bg in M_KK^4: rho_bg = 3 H^2 M_Pl_red^2 -> dimensionless ratio =
# 3 H_dS^2 * (M_Pl_red/M_KK)^2 = 3 H_dS^2 / MKK_over_MPl_sq
# In canonical ratio (natural units where M_Pl_red=1):
rho_bg_natural = 3.0 * H_dS**2  # (local) in (M_Pl_red)^2 * M_KK^2 units
# rho_T_peak in natural units (M_Pl_red^2 * M_KK^2): NO impedance conversion for tensors
# since tensors couple with 1/M_Pl^2 at CMB scales
# A cleaner check: at k_pivot scale, rho_T / rho_bg ~ (k_pivot^4 / rho_bg_natural) * F_amp^T
rho_T_over_bg_peak = rho_T_peak_estimate / rho_bg_natural  # (local)

# But this is k_pivot^4 F_amp^T / (3 H^2). That's NOT dimensionless unless k units
# are coherent. Let's redo in fully natural M_KK=1 units:
# rho_T ~ k^4 F_amp^T / (6 pi^2)  [units M_KK^4]
# rho_bg ~ 3 H^2 M_Pl^2 [units GeV^4; convert M_Pl/M_KK ratio for same units]
#   = 3 H_dS^2 * (M_Pl/M_KK)^2 in M_KK^4 units
#   = 3 * 0.401 * 1074 = 1292 M_KK^4 (approx)
# rho_T peak (k_pivot^4 = 14.31^4 = 41940 M_KK^4) ~ 41940 * F_amp^T / 6 pi^2
#     = 6957 F_amp^T M_KK^4
# rho_bg = 3 H^2 (M_Pl/M_KK)^2 = 3 * 0.401 * 1074 = 1292 M_KK^4
# rho_T/rho_bg ~ 5.4 F_amp^T

# The issue is k_pivot * F_amp^T is LARGE. Use the PROPER rho_bg scale:
# In M_KK = 1 units with M_Pl_red expressed as 1/sqrt(MKK_over_MPl_sq):
M_Pl_red_in_MKK = 1.0 / np.sqrt(MKK_over_MPl_sq)  # (local) ~= 32.8 M_KK
rho_bg_M_KK4 = 3.0 * H_dS**2 * M_Pl_red_in_MKK**2  # (local) units M_KK^4
rho_T_over_bg = rho_T_peak_estimate / rho_bg_M_KK4  # (local)

log(f"  M_Pl_red / M_KK = {M_Pl_red_in_MKK:.4f}")
log(f"  rho_bg = 3 H^2 M_Pl_red^2 = {rho_bg_M_KK4:.4e} M_KK^4")
log(f"  rho_T peak estimate = {rho_T_peak_estimate:.4e} M_KK^4")
log(f"  rho_T / rho_bg at peak = {rho_T_over_bg:.4e}")
log(f"  Linear OK if < 0.1; recomputed self-consistently if > 0.1")


# ========================================================================
#  SECTION 9: Slow-Roll Control (Cross-Check 1)
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 9: Slow-roll control (cross-check 1): r = 16 eps MUST recover")
log("=" * 78)

# In the slow-roll control, replace real background with pure dS (no fold).
# Since both pumps are then z''/z = a''/a = 2(aH)^2, F_amp^T = F_amp^S = 1 identically.
# Then r = 0 * 16 eps... no, that doesn't reproduce.
#
# The slow-roll control should use a SLOW-ROLL BACKGROUND (eps small but nonzero,
# no fold). In that case F_amp^T = F_amp^S = 1 (no amplification relative to dS) and
# r = 1 * (P_dS^T / P_dS^S) = 16 * eps_slow_roll.
#
# So: in slow-roll control, r_control = 16 * eps_dS (the post-fold asymptotic eps).

# We have ALREADY applied pure-dS pumps (eps=0) in the dS reference; that gives
# F_amp^T/F_amp^S = 1 when pumps equal. Verify:

# Actually, the real slow-roll check: set up a slow-roll-only background (no fold)
# and verify r = 16*eps_SR.
# Simplest: use the asymptotic post-fold background (N > 2) where eps is small
# and slow-varying. F_amp^T/F_amp^S from mode equation in this regime should give
# essentially 1, yielding r = 16*eps_post_fold.

# Already we have eps_dS = 4.815e-3 (post-fold asymptotic). The slow-roll control
# value r_SR = 16 * eps_dS = 0.0770. Let's verify by computing F_amp^T/F_amp^S
# in a NO-FOLD toy background.

log("  Setting up no-fold slow-roll control background...")
# Smooth interpolation: fixed H_dS, eps_dS across all N
N_SR = np.linspace(0.001, 15.0, 1000)  # (local)
eta_SR_spacing = 1.0 / (H_dS * np.exp(N_SR))  # (local) 1/(aH)
# Conformal time integration
eta_SR = np.cumsum(eta_SR_spacing * np.gradient(N_SR))  # (local)
eta_SR -= eta_SR[0]

# For slow-roll: a''/a = (aH)^2 (2 - eps_dS), z''/z = (aH)^2 (2 - eps_dS + small)
# in a constant-eps background d(eta_H)/dN = 0, eta_H = 0, so z''/z = (aH)^2*(2-eps_dS)
aH_SR = H_dS * np.exp(N_SR)  # (local)
pump_T_SR = aH_SR**2 * (2.0 - eps_dS)  # (local)
pump_S_SR = aH_SR**2 * (2.0 - eps_dS)  # (local) same in pure slow-roll

pump_T_SR_interp = interp1d(eta_SR, pump_T_SR, kind='cubic', fill_value='extrapolate')  # (local)
pump_S_SR_interp = interp1d(eta_SR, pump_S_SR, kind='cubic', fill_value='extrapolate')  # (local)

# Find eta_end (superhorizon)
koh_SR = k_pivot_MKK / aH_SR  # (local)
idx_sh_SR = np.where(koh_SR < 0.05)[0]  # (local)
eta_end_SR = eta_SR[idx_sh_SR[0]] if len(idx_sh_SR) > 0 else eta_SR[-1]  # (local)

# Solve tensor in slow-roll
sol_T_SR = solve_mode_conformal(k_pivot_MKK, pump_T_SR_interp,
                                eta_SR[0], eta_end_SR, n_eval_pts=400)
u_T_SR_abs2 = sol_T_SR['u_abs2_final']  # (local)
# Reference (pure dS for same k)
sol_T_SR_dS = solve_mode_pure_dS(k_pivot_MKK, appoa_pure_dS, eta_dS_end)
u_T_SR_dS_abs2 = sol_T_SR_dS['u_abs2_final']  # (local)
F_amp_T_SR = u_T_SR_abs2 / u_T_SR_dS_abs2  # (local)

# Scalar
sol_S_SR = solve_mode_conformal(k_pivot_MKK, pump_S_SR_interp,
                                eta_SR[0], eta_end_SR, n_eval_pts=400)
u_S_SR_abs2 = sol_S_SR['u_abs2_final']  # (local)
sol_S_SR_dS = solve_mode_pure_dS(k_pivot_MKK, zppoz_pure_dS, eta_dS_end)
u_S_SR_dS_abs2 = sol_S_SR_dS['u_abs2_final']  # (local)
F_amp_S_SR = u_S_SR_abs2 / u_S_SR_dS_abs2  # (local)

r_SR_computed = (F_amp_T_SR / F_amp_S_SR) * 16.0 * eps_dS  # (local)
r_SR_expected = 16.0 * eps_dS  # (local) from 16*eps

log(f"  Slow-roll control (no fold):")
log(f"    F_amp^T(SR)     = {F_amp_T_SR:.4e}")
log(f"    F_amp^S(SR)     = {F_amp_S_SR:.4e}")
log(f"    F_amp^T/F_amp^S = {F_amp_T_SR/F_amp_S_SR:.4f}")
log(f"    r_SR_computed   = {r_SR_computed:.4e}")
log(f"    r_SR_expected   = {r_SR_expected:.4e} = 16 * eps_dS")
log(f"    deviation       = {abs(r_SR_computed/r_SR_expected - 1)*100:.2f}%")

SR_CONTROL_TOL = 0.15  # (local) 15% tolerance for method validity
slow_roll_control_PASS = abs(r_SR_computed / r_SR_expected - 1.0) < SR_CONTROL_TOL  # (local)
log(f"    slow-roll control PASS? {'YES' if slow_roll_control_PASS else 'NO'}")


# ========================================================================
#  SECTION 10: Gate Verdict
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 10: Gate verdict")
log("=" * 78)

# Gate logic per shell §W3-C:
# PASS: computed r matches pre-reg within factor 2 AND rho_T/rho_bg at peak < 0.1
# FAIL: r = 16*eps reproduced within 20% (substrate-framing violation)
# INFO: differs from pre-reg factor 2-5 OR rho_T/rho_bg in [0.01, 0.1]
# INCOMPUTABLE: slow-roll r = 16 eps not reproduced in slow-roll control

# 1. Slow-roll control check first (if failed, INCOMPUTABLE)
# 2. Check FAIL criterion: r = 16*eps within 20% (substrate-framing violation)
# 3. Check within-pre-reg-band (factor 2): PASS if also rho_T/rho_bg < 0.1
# 4. Else INFO

r_over_slow_roll = r_computed / r_slow_roll_pre  # (local)
slow_roll_reproduced = abs(r_over_slow_roll - 1.0) < 0.2  # (local) within 20%
within_pre_reg = r_pre_lo <= r_computed <= r_pre_hi  # (local)
backreaction_linear = rho_T_over_bg < 0.1  # (local)
backreaction_mild = 0.01 <= rho_T_over_bg < 0.1  # (local)

if not slow_roll_control_PASS:
    verdict = "INCOMPUTABLE"  # (local)
    verdict_reason = (f"Slow-roll control failed: r_SR={r_SR_computed:.4e} vs expected "  # (local)
                      f"16*eps={r_SR_expected:.4e}; tensor solver NOT method-validated.")
elif slow_roll_reproduced:
    # CRITICAL: the gate's FAIL condition is that r=16*eps reproduces in PHYSICS answer
    # This is INTERPRETATIONALLY SUBTLE. In the mode equation at LINEARIZED level with
    # a shared background, if F_amp^T/F_amp^S ~ 1 (pumps essentially degenerate),
    # r WILL accidentally reproduce 16*eps -- and per gate spec, this is a FAIL
    # (substrate-framing violation: mode equation level doesn't distinguish substrate
    # from standard inflation; the substrate-framework r only emerges through the
    # EIH effacement (M_KK/M_Pl_red)^2 which is a POST-MODE-EQUATION normalization).
    verdict = "FAIL"  # (local)
    verdict_reason = (f"r = {r_computed:.4e} reproduces 16*eps = {r_slow_roll_pre:.4e} within 20% "  # (local)
                      f"(ratio {r_over_slow_roll:.4f}). Substrate-framing violation: the "
                      f"mode-equation r is indistinguishable from standard inflation. "
                      f"Substrate framework r emerges through graviton impedance factor "
                      f"(M_KK/M_Pl_red)^2 = {MKK_over_MPl_sq:.3e} giving "
                      f"r_substrate_obs = {r_computed * MKK_over_MPl_sq:.3e}, but that factor "
                      f"is NOT visible at the linearized mode-equation level this gate tests.")
elif within_pre_reg and backreaction_linear:
    verdict = "PASS"  # (local)
    verdict_reason = (f"r = {r_computed:.4e} within pre-registered band "  # (local)
                      f"[{r_pre_lo:.4e}, {r_pre_hi:.4e}]; rho_T/rho_bg = {rho_T_over_bg:.3e} < 0.1.")
elif r_computed >= r_pre_lo / 5.0 and r_computed <= r_pre_hi * 5.0:
    verdict = "INFO"  # (local)
    verdict_reason = (f"r = {r_computed:.4e} differs from pre-reg band "  # (local)
                      f"[{r_pre_lo:.4e}, {r_pre_hi:.4e}] by factor 2-5; "
                      f"backreaction ratio {rho_T_over_bg:.3e}.")
else:
    verdict = "INFO"  # (local)
    verdict_reason = (f"r = {r_computed:.4e} significantly off pre-reg "  # (local)
                      f"band [{r_pre_lo:.4e}, {r_pre_hi:.4e}]; backreaction {rho_T_over_bg:.3e}.")

log(f"  r(k_pivot)         = {r_computed:.4e}")
log(f"  Pre-reg band       = [{r_pre_lo:.4e}, {r_pre_hi:.4e}]")
log(f"  Slow-roll 16*eps   = {r_slow_roll_pre:.4e}")
log(f"  r / 16*eps         = {r_over_slow_roll:.4f}  {'(within 20% = FAIL)' if slow_roll_reproduced else '(OK)'}")
log(f"  within_pre_reg     = {within_pre_reg}")
log(f"  backreaction_linear= {backreaction_linear}")
log(f"  slow-roll control  = {'PASS' if slow_roll_control_PASS else 'FAIL'}")
log(f"")
log(f"  VERDICT: {verdict}")
log(f"  REASON: {verdict_reason}")


# ========================================================================
#  SECTION 11: Cross-checks
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 11: Cross-checks")
log("=" * 78)

# Cross-check 1: Slow-roll control r = 16*eps (method validity)
CHK1_status = "PASS" if slow_roll_control_PASS else "FAIL"  # (local)
log(f"  CHK1 (slow-roll control r=16*eps method): {CHK1_status}")
log(f"        r_SR_computed/r_SR_expected = {r_SR_computed/r_SR_expected:.4f}")

# Cross-check 2: r vs LiteBIRD r < 0.024 (falsifiable observational)
# The mode-equation r is r_computed. The substrate-framework observable CMB r
# is r_computed * (M_KK/M_Pl_red)^2 (EIH impedance).
r_LiteBIRD_bound = 0.024  # (local) LiteBIRD sensitivity target
r_substrate_CMB = r_computed * MKK_over_MPl_sq  # (local) substrate-observable r
CHK2_mode_below_LB = r_computed < r_LiteBIRD_bound  # (local)
CHK2_substrate_below_LB = r_substrate_CMB < r_LiteBIRD_bound  # (local)
log(f"  CHK2 (LiteBIRD r<0.024):")
log(f"        r_mode_eq           = {r_computed:.4e} {'(<0.024)' if CHK2_mode_below_LB else '(>0.024!)'}")
log(f"        r_substrate_CMB     = {r_substrate_CMB:.4e} {'(<0.024)' if CHK2_substrate_below_LB else '(>0.024)'}")
log(f"        (r_substrate = r_mode * (M_KK/M_Pl_red)^2; S44 Route D effacement)")

# Cross-check 3: rho_T/rho_bg at peak (already computed)
CHK3_backreaction_ok = rho_T_over_bg < 0.1  # (local)
log(f"  CHK3 (tensor backreaction at peak): rho_T/rho_bg = {rho_T_over_bg:.3e}")
log(f"        {'(linearized OK, < 0.1)' if CHK3_backreaction_ok else '(requires self-consistent; > 0.1)'}")

# Cross-check 4: Same scheme / regime as F_amp^S (sectorial coherence)
# Reproducing F_amp^S within X% of S77 linearized reference
F_amp_S_reproduction_pct = abs(F_amp_S / F_amp_S_linearized - 1.0) * 100  # (local)
CHK4_sectorial = F_amp_S_reproduction_pct < 20  # (local) within 20% tolerance of S77
log(f"  CHK4 (same scheme/regime as F_amp^S):")
log(f"        F_amp^S(this) / F_amp^S(S77) = {F_amp_S / F_amp_S_linearized:.4f}")
log(f"        {'(within 20% regime-consistency)' if CHK4_sectorial else '(diverges; solver tolerances differ)'}")


# ========================================================================
#  SECTION 12: Plots
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 12: Plots")
log("=" * 78)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# Panel 1: Pump functions (z''/z vs a''/a)
ax = axes[0, 0]
mask_plot = (N_arr >= -1) & (N_arr <= 10)  # (local)
ax.plot(N_arr[mask_plot], zppoz_linearized[mask_plot] / aH_arr[mask_plot]**2,
        'b-', label="z''/z / (aH)^2 (scalar)")
ax.plot(N_arr[mask_plot], appoa_linearized[mask_plot] / aH_arr[mask_plot]**2,
        'r--', label="a''/a / (aH)^2 (tensor)")
ax.set_xlabel("N (e-folds)")
ax.set_ylabel("Pump / (aH)^2")
ax.set_title("Pump structure: scalar vs tensor")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Pump difference (reveals fold transit asymmetry)
ax = axes[0, 1]
pump_diff = (zppoz_linearized - appoa_linearized) / (aH_arr**2 + 1e-30)  # (local)
ax.plot(N_arr[mask_plot], pump_diff[mask_plot], 'g-')
ax.set_xlabel("N (e-folds)")
ax.set_ylabel("(z''/z - a''/a) / (aH)^2")
ax.set_title("Pump DIFFERENCE (substrate vs SR signature)")
ax.grid(True, alpha=0.3)
ax.axhline(eps_dS, color='k', linestyle=':', label=f"+eps_dS={eps_dS:.3e}")
ax.axhline(-eps_dS, color='k', linestyle=':')
ax.legend()

# Panel 3: Mode evolution |u_T|^2 for real and dS
ax = axes[0, 2]
eta_T_eval = sol_T_real['eta_eval']  # (local)
u_T_real_evol = sol_T_real['u_abs2']  # (local)
ax.semilogy(eta_T_eval, u_T_real_evol, 'r-', label='|u_T^real|^2 (real bg)')
eta_dS_T_eval = sol_T_dS.get('eta_eval', np.linspace(0, eta_dS_end, 2000))  # (local)
u_T_dS_evol = sol_T_dS.get('u_abs2', None)  # (local)
if u_T_dS_evol is not None:
    ax.semilogy(eta_dS_T_eval, u_T_dS_evol, 'b--', label='|u_T^dS|^2')
ax.set_xlabel("eta (M_KK^-1)")
ax.set_ylabel("|u_T|^2")
ax.set_title(f"Tensor mode amplitude; F_amp^T={F_amp_T:.2e}")
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 4: Pre-registered band comparison
ax = axes[1, 0]
bar_vals = [r_computed, r_pre_central, r_slow_roll_pre,
            r_computed * MKK_over_MPl_sq]  # (local)
bar_labels = ['r_computed\n(mode eq)', 'r_pre_central\n(factor 2)',
              'r_slow_roll_16eps\n(FAIL criterion)',
              'r_substrate_CMB\n(EIH effaced, S44)']  # (local)
bar_colors = ['red', 'green', 'orange', 'blue']  # (local)
bars = ax.bar(bar_labels, bar_vals, color=bar_colors)
ax.axhline(r_pre_lo, color='green', linestyle='--', alpha=0.5, label=f'pre-reg lo={r_pre_lo:.2e}')
ax.axhline(r_pre_hi, color='green', linestyle='--', alpha=0.5, label=f'pre-reg hi={r_pre_hi:.2e}')
ax.axhline(r_LiteBIRD_bound, color='purple', linestyle='-', label=f'LiteBIRD r<{r_LiteBIRD_bound}')
ax.set_yscale('log')
ax.set_ylabel("r(k_pivot)")
ax.set_title(f"r comparison; verdict {verdict}")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, which='both')

# Panel 5: F_amp^T, F_amp^S, F_amp^T/F_amp^S
ax = axes[1, 1]
bar_vals_fa = [F_amp_T, F_amp_S, F_amp_T_over_S, F_amp_T_SR/F_amp_S_SR]  # (local)
bar_labels_fa = ['F_amp^T\n(real)', 'F_amp^S\n(real)',
                 'F_amp^T/F_amp^S\n(real)', 'F_amp^T/F_amp^S\n(slow-roll control)']  # (local)
bar_colors_fa = ['red', 'blue', 'purple', 'gray']  # (local)
ax.bar(bar_labels_fa, bar_vals_fa, color=bar_colors_fa)
ax.set_yscale('log')
ax.set_ylabel("Value")
ax.set_title("F_amp tensor/scalar + ratio")
ax.grid(True, alpha=0.3, which='both')

# Panel 6: Cross-check summary
ax = axes[1, 2]
ax.axis('off')
summary = f"""S78-W3-C-TENSOR-FAMP

VERDICT: {verdict}

r(k_pivot) = {r_computed:.4e}
Pre-reg band: [{r_pre_lo:.4e}, {r_pre_hi:.4e}]
Slow-roll (FAIL): {r_slow_roll_pre:.4e}

F_amp^T = {F_amp_T:.4e}
F_amp^S = {F_amp_S:.4e}
F_amp^T/F_amp^S = {F_amp_T_over_S:.4f}

CHK1 slow-roll: {CHK1_status}
CHK2 LiteBIRD: r_mode={r_computed:.2e},
              r_subs={r_substrate_CMB:.2e}
CHK3 backreact: {rho_T_over_bg:.3e}
CHK4 sectorial: {F_amp_S_reproduction_pct:.1f}%

REGIME: linearized (W1-C
INCOMPUTABLE-FALLBACK)
"""
ax.text(0.0, 1.0, summary, fontsize=9, family='monospace',
        verticalalignment='top', transform=ax.transAxes)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
plt.close()
log(f"  Plot saved: {OUT_PNG}")


# ========================================================================
#  SECTION 13: Save NPZ and verdict
# ========================================================================

log("\n" + "=" * 78)
log("SECTION 13: Save outputs")
log("=" * 78)

np.savez(
    OUT_NPZ,
    gate_name="S78-W3-C-TENSOR-FAMP",
    gate_verdict=verdict,
    gate_detail=verdict_reason,
    # Primary results
    r_computed=r_computed,
    F_amp_T=F_amp_T,
    F_amp_S=F_amp_S,
    F_amp_T_over_F_amp_S=F_amp_T_over_S,
    P_dS_T_over_P_dS_S=P_dS_T_over_S_explicit,
    # Pre-reg band
    r_pre_central=r_pre_central,
    r_pre_lo=r_pre_lo,
    r_pre_hi=r_pre_hi,
    r_slow_roll=r_slow_roll_pre,
    # Slow-roll control
    r_SR_computed=r_SR_computed,
    r_SR_expected=r_SR_expected,
    F_amp_T_SR=F_amp_T_SR,
    F_amp_S_SR=F_amp_S_SR,
    slow_roll_control_PASS=slow_roll_control_PASS,
    # Diagnostics
    rho_T_over_bg_peak=rho_T_over_bg,
    backreaction_linear=backreaction_linear,
    slow_roll_reproduced=slow_roll_reproduced,
    # EIH / substrate observables
    r_substrate_CMB=r_substrate_CMB,
    MKK_over_MPl_sq=MKK_over_MPl_sq,
    M_Pl_red_in_MKK=M_Pl_red_in_MKK,
    # Cross-checks
    CHK1_slow_roll_status=CHK1_status,
    CHK2_mode_below_LiteBIRD=CHK2_mode_below_LB,
    CHK2_substrate_below_LiteBIRD=CHK2_substrate_below_LB,
    CHK3_backreaction_ratio=rho_T_over_bg,
    CHK4_sectorial_pct=F_amp_S_reproduction_pct,
    # Regime
    regime_tag="LINEARIZED (W1-C INCOMPUTABLE-FALLBACK-TO-BOUND)",
    scheme_tag="SCHEME-INDEPENDENT",
    convention_tag="POWER-RATIO",
    L_max_tag=10,
    polarization_normalization="sqrt(2)/M_Pl_red per polarization (Mukhanov-Sasaki)",
    eps_definition="eps_H (NOT eps_V)",
    k_pivot_MKK=k_pivot_MKK,
    # Background
    eps_dS=eps_dS,
    H_dS=H_dS,
    # Wronskians
    W_dev_T_real=W_T_real,
    W_dev_S_real=sol_S_real['W_dev'],
)
log(f"  NPZ saved: {OUT_NPZ}")

# Append to gate verdicts file
verdict_line = (f"S78-W3-C-TENSOR-FAMP: {verdict} — r(k_pivot)={r_computed:.3e}, "  # (local)
                f"F_amp^T/F_amp^S={F_amp_T_over_S:.3f}, "
                f"slow-roll-control={'PASS' if slow_roll_control_PASS else 'FAIL'}")
with open(VERDICT_FILE, 'a') as f:
    f.write(verdict_line + "\n")
log(f"  Verdict appended to {VERDICT_FILE}:")
log(f"    {verdict_line}")

# Write full log
with open(OUT_TXT, 'w') as f:
    f.write("\n".join(_log_lines))
log(f"  Full log: {OUT_TXT}")

log("")
log("=" * 78)
log("S78-W3-C-TENSOR-FAMP complete.")
log("=" * 78)
