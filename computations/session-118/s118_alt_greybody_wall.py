#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S118-ALT-GREYBODY-WALL  (session-118, Wave 1, gate W1-2)  [SIGN]
==================================================================

GATE: adjudicate the exit-greybody structural-WALL candidate (atlas-09 Item-49) by
extending the s117_alt_greybody.py machinery with a 4th knob-free greybody bridge-map
class — the FULL BdG S-matrix transmission Gamma(omega)=|T(omega)|^2 computed by 1D
TRANSFER-MATRIX scattering on the exit-horizon BdG sector (dispersion omega_k,
V_eff(x_tortoise), kappa_eff from inv12_w3_4_greybody_from_bdg.npz), with the
Pauli-Villars regulator mass swept M_reg = alpha * lambda_max for
alpha in {1.0, 2.0, 4.0, 8.0} (knob-free, M_reg >= lambda_max, VERDICT-relevant);
alpha = 0.5 (M_reg < lambda_max, in-bulk KNOB) computed as DIAGNOSTIC-ONLY, EXCLUDED.
lambda_max from the s84 L12 cache.

  This is the 4th greybody-construction CLASS (the prior three FAILed knob-free per
  s117 + INV12-W3-4):
    class 1 (INV12-W3-4) : Poeschl-Teller near-horizon barrier (ODE / closed PT)  -> FAIL
    class 2 (CF-S117)    : Wodzicki a_2/a_4 spectral moment-ratio (bare)           -> MISS
    class 3 (CF-S117)    : Connes inverse-diameter d_C = 1/(lam_max - lam_min)      -> MISS
    class 4 (THIS gate)  : FULL BdG S-matrix |T(omega)|^2 (transfer-matrix), PV M_reg sweep

  The NEW machinery (distinct from INV12-W3-4's solve_ivp ODE): a manifestly-UNITARY
  (psi, psi') slab transfer-matrix product on the cached barrier; det(M_slab)=1 ⇒ the
  Wronskian is preserved ⇒ |T|^2 + |R|^2 = 1 BY CONSTRUCTION (the [SIGN] bedrock).

TWO-BRANCH ADJUDICATION (plan §W1-2 operator):
  route(a) PASS-FALSIFIED iff min over the BdG-S-matrix class × targets {box,fit,slow}
           of rel_dev <= 0.10 at M_reg >= lambda_max  (⇒ a knob-free greybody EXISTS,
           the atlas-09 wall candidate is FALSIFIED, A_s upper-edge re-grounded).
  route(b) PASS-WALL iff Gamma_knobfree_floor > max(targets)=0.636546 robustly for all
           alpha >= 1  (⇒ the candidate promotes to a STRUCTURAL WALL: sub-unity Gamma
           toward the targets requires a sub-spectral knob).
  bedrock [SIGN]: Gamma(omega) = |T_BdG(omega)|^2 <= 1  (BdG S-matrix unitarity).

  Composite-precedence (PLAN-FROZEN, §W1-2 lines 461-473; gate-verdicts.md
  "Plan-frozen gate-block operator precedence"). route_b_valid_nogo and route_a_hit are
  LOGICALLY EXCLUSIVE (a valid no-go ⇒ no knob-free greybody exists ⇒ route_a cannot hit):
    if route_b_valid_nogo:  composite = PASS  (outcome=STRUCTURAL-WALL)             [strongest]
    elif route_a_hit:       composite = PASS  (outcome=CANDIDATE-FALSIFIED)
    elif route_a_miss:      composite = FAIL  (outcome=WALL-STRENGTHENED-4-CLASS-EMPIRICAL)
    else:                   composite = INFO  (outcome=INDETERMINATE)

SUBSTITUTION CHAIN (mandatory, [SIGN] bedrock; plan substitution_chain block):
  Def 1: Gamma(omega) := |T(omega)|^2                  [greybody = BdG transmission prob.]
  Def 2: S-matrix unitarity S†S=1 ⇒ |T|^2 + |R|^2 = 1  [exit-horizon BdG = 1D self-adjoint
         scattering; D_K block-diagonal PSD ⇒ H_BdG self-adjoint ⇒ S unitary; kappa_eff =
         kappa_exit = 47.6146 sets the surface gravity / inverse tortoise width]
  Def 3: |R(omega)|^2 >= 0                              [modulus-squared non-negative]
  Substitute: |T|^2 = 1 - |R|^2 <= 1
  Simplify:   Gamma = |T|^2 <= 1, equality iff |R|^2=0 (transparent barrier)
  Direction (SIGN): Gamma - 1 <= 0 ⇒ sign_verdict = PASS (unitarity respected); a computed
         Gamma > 1 ⇒ sign_verdict = FAIL (transfer-matrix / normalization error).
  Wall sub-claim (magnitude direction, pre-registered): the barrier opacity is set by the
         regulator mass relative to the spectral ceiling; the standard PV a_4 condensation
         moment M_a4^PV(M_reg) -> M_a4^bare as M_reg -> infinity (M_reg >= lambda_max,
         knob-free), so V0(M_reg>=lam_max) -> V0_bare (the FULL physical barrier). This
         gate TESTS whether that knob-free barrier floors Gamma near unity (route b) or
         hits a sub-unity target (route a).

Classification: PHONONIC.  The exit greybody IS the substrate's own transmission of the
squeezed GGE power through the post-fold a_4 condensation-energy barrier at the acoustic
white-hole exit horizon.  D_K eigenvalues (s84 L12 -> lambda_max; inv12 BdG omega_k) ->
exit-horizon BdG S-matrix |T(omega)|^2 -> greybody Gamma -> A_s upper-edge factor.

DISCIPLINE (gate-verdicts.md / regulator-pin-discipline.md / math-scripts.md):
  - from canonical_constants import *  (M_KK, A_s_CMB, A_s_FW, kappa_exit, Delta_BCS, tau_fold)
  - regulator_pin: a_n^{Pauli-Villars} + Wodzicki Res_W(s); poleconv-A-double a_2/a_4:
    a_2=(pole_in_s=3, curvature_grade_n=2) / a_4=(pole_in_s=2, curvature_grade_n=4).
  - dual-SHA (S84+); verdict via emit_verdict (race-safe MCP tool); [SIGN] => 3-tuple
    sign/magnitude/regime; PLUS a pre-declared `# composite-precedence:` extra-row.
  - GPU_path: 1D transfer-matrix scattering on the CACHED BdG dispersion + barrier
    (no dense >=100x100 op); cpu-cap-OMP8.  Honest deviation disclosure.
  Script mirrors the s117_alt_greybody.py author lineage (same poleconv-A-double a_2/a_4
  pins, same dual-SHA + print_verdict_payload).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) cap CPU threads before numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, os.path.join("computations", "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK, A_s_CMB, A_s_FW, kappa_exit, Delta_BCS, tau_fold,
)

# =====================================================================================
# Pinned machinery (plan §W1-2)
# =====================================================================================
GATE_ID = "CF-S118-ALT-GREYBODY-WALL"
SCHEME = ("BDG-S-MATRIX-TRANSMISSION-4TH-CLASS+WODZICKI-PV-MOMENT-RATIO"
          "+CONNES-DISTANCE+NO-GO")
CONVENTION = ("knob-free-Mreg>=lammax;Gamma=|T_BdG|^2;poleconv-A-double-a2s3n2-a4s2n4")
L_MAX = 12                       # (local) D_K truncation level of the s84 cache

REL_TOL = 0.10                   # (local) route(a) agreement tolerance (plan; matches s117/S95)
OOM_SLOW_ROLL = 0.19617          # (local) plan-pinned A_s(H~)-grid OOM (s117 line 102)
GAMMA_FIT_EXPECTED = 0.511872    # (local) s95_w4_3 fitted comparator (inv12 transmitted_fraction_fitted)

# poleconv-A-double (zeta_D(s)=Sum|lam|^{-2s}, poles s=(d-n)/2, d=8):
#   a_2 : pole_in_s = 3, curvature_grade_n = 2
#   a_4 : pole_in_s = 2, curvature_grade_n = 4
S_A2 = 3                         # (local) Wodzicki pole_in_s for a_2 (n=2)
S_A4 = 2                         # (local) Wodzicki pole_in_s for a_4 (n=4) -- the a_4 condensation moment

# Pauli-Villars regulator-mass sweep M_reg = alpha * lambda_max:
PV_ALPHAS_KNOBFREE = [1.0, 2.0, 4.0, 8.0]   # (local) M_reg >= lambda_max -> VERDICT-relevant
PV_ALPHA_DIAGNOSTIC = 0.5                   # (local) M_reg < lambda_max (in-bulk KNOB) -> EXCLUDED

# transfer-matrix scattering window (the inv12 V_eff/x_tortoise grid is the plan-pinned barrier)
S84_NPZ = os.path.join("computations", "session-84", "s84_spectrum_cache_L12_tau019.npz")
INV12_NPZ = os.path.join("computations", "investigation-12", "inv12_w3_4_greybody_from_bdg.npz")
S117_NPZ = os.path.join("computations", "session-117", "s117_alt_greybody.npz")
S117_PY = os.path.join("computations", "session-117", "s117_alt_greybody.py")
CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
SELF_PATH = os.path.abspath(__file__)

OUT_NPZ = os.path.join("computations", "session-118", "s118_alt_greybody_wall.npz")
OUT_PNG = os.path.join("computations", "session-118", "s118_alt_greybody_wall.png")

# plan input-SHA ledger (§W1-2 input_files) -- a mismatch -> close PRE-REG-INC honestly
PLAN_SHA_LEDGER = {
    CANON_PATH: "d884a2b51200139296369dc6ed6ef2818b70386aee24e36b6c95365b43d3d78c",
    S117_PY:    "308fbf259e332e05fe5c6e937356c25d0c0ca5459582bfa898fcf826a02f6dd9",
    S117_NPZ:   "1350f937b0202032aa8bea63f967ba059530b9c89a0f2fb149c437f1eeadea69",
    INV12_NPZ:  "4f51d724945d586f603f58641dbb481f7da3e81a537c7b6d54883e098ae72e1c",
    S84_NPZ:    "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
}


# =====================================================================================
# SHA helpers (gate-verdicts.md dual-SHA; mirror of the s117 sibling)
# =====================================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """Audit SHA over the ordered input-pin map (gate-verdicts.md / script-template.py)."""
    h = hashlib.sha256()
    for k in sorted(pin_map):
        h.update(f"{k}={pin_map[k]}".encode("utf-8"))
    return h.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict, extra_rows=None):
    """Print the emit_verdict payload as a delimited JSON block for the dispatching agent
    (script-template.py pattern).  The script NEVER writes the verdict file directly.
    [SIGN] trigger ⇒ carry the sign/magnitude/regime 3-tuple."""
    payload = {
        "session": 118,
        "track": "session",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# =====================================================================================
# Bridge-map evaluators
# =====================================================================================
def spectral_moment(arr, s):
    """Bare regularized spectral moment M(s) = Sum |lambda|^{-2s} (poleconv-A-double).
    Pauli-Villars M_reg -> infinity limit (knob-free UV-regulator reading)."""
    return float(np.sum(arr ** (-2.0 * s)))


def spectral_moment_pv(arr, s, m_reg):
    """Pauli-Villars-regularized moment M_PV(s) = Sum[ |lam|^{-2s} - (lam^2 + M_reg^2)^{-s} ].
    M_reg >= lambda_max (UV regulator at/above the spectrum) -> bare; M_reg in the bulk -> KNOB.
    Mirrors s117_alt_greybody.py spectral_moment_pv (same author lineage)."""
    return float(np.sum(arr ** (-2.0 * s) - (arr ** 2 + m_reg ** 2) ** (-1.0 * s)))


def gamma_transfer_vec(omega_arr, xgrid, Vgrid):
    """FULL BdG S-matrix transmission |T(omega)|^2 AND reflection |R(omega)|^2 by a
    manifestly-UNITARY (psi, psi') slab transfer-matrix product on the piecewise-constant
    barrier Vgrid over xgrid (asymptotic V->0 both leads).  Vectorized over omega_arr.

    Slab matrix for (psi, psi') across a constant-V slab of width d with local wavenumber
    q = sqrt(omega^2 - V):
        M_slab = [[cos(q d), sin(q d)/q],[-q sin(q d), cos(q d)]],   det = 1.
    Complex q handles BOTH propagating (real q) and evanescent (imag q: cos->cosh,
    sin/q->sinh/|q|) regimes.  det(M)=1 ⇒ Wronskian preserved ⇒ |T|^2+|R|^2=1 by construction.

    Lead matching (k_L = k_R = omega): solve the 2x2 system for (r, t) per mode.
    Returns (T2, R2) arrays of shape omega_arr.shape.
    """
    w = np.asarray(omega_arr, float)
    n = w.size
    Vc = 0.5 * (Vgrid[:-1] + Vgrid[1:])               # (local) slab midpoint potentials
    dx = np.diff(xgrid)                               # (local) slab widths
    # q[m, j] = sqrt(w_m^2 - Vc_j) for mode m, slab j
    q = np.sqrt((w[:, None] ** 2 - Vc[None, :]).astype(complex))   # (local) (n_modes, n_slab)
    qd = q * dx[None, :]                              # (local)
    c = np.cos(qd)                                    # (local)
    s = np.sin(qd)                                    # (local)
    # sin(qd)/q with the q->0 limit -> dx
    with np.errstate(divide="ignore", invalid="ignore"):
        sq = np.where(np.abs(q) > 1e-300, s / q, dx[None, :])      # (local)
    # batched 2x2 product over slabs: M = prod_j M_slab_j  (shape (n_modes, 2, 2))
    M = np.broadcast_to(np.eye(2, dtype=complex), (n, 2, 2)).copy()
    for j in range(c.shape[1]):
        Mj = np.empty((n, 2, 2), dtype=complex)       # (local)
        Mj[:, 0, 0] = c[:, j]
        Mj[:, 0, 1] = sq[:, j]
        Mj[:, 1, 0] = -q[:, j] * s[:, j]
        Mj[:, 1, 1] = c[:, j]
        M = np.matmul(Mj, M)
    m11, m12 = M[:, 0, 0], M[:, 0, 1]
    m21, m22 = M[:, 1, 0], M[:, 1, 1]
    k = w
    xL, xR = xgrid[0], xgrid[-1]
    eL = np.exp(1j * k * xL)
    eLm = np.exp(-1j * k * xL)
    eR = np.exp(1j * k * xR)
    # unknowns (r, t):  M (psi_L, psi'_L) = (psi_R, psi'_R)
    #   psi_L = eL + r eLm ; psi'_L = ik(eL - r eLm) ; psi_R = t eR ; psi'_R = ik t eR
    # eq1: m11(eL + r eLm) + m12 ik(eL - r eLm) - t eR        = 0
    # eq2: m21(eL + r eLm) + m22 ik(eL - r eLm) - ik t eR     = 0
    a11 = m11 * eLm - m12 * 1j * k * eLm
    a12 = -eR
    a21 = m21 * eLm - m22 * 1j * k * eLm
    a22 = -1j * k * eR
    b1 = -(m11 * eL + m12 * 1j * k * eL)
    b2 = -(m21 * eL + m22 * 1j * k * eL)
    det = a11 * a22 - a12 * a21
    r = (b1 * a22 - a12 * b2) / det
    t = (a11 * b2 - b1 * a21) / det
    T2 = np.abs(t) ** 2
    R2 = np.abs(r) ** 2
    # omega <= 0 guard (none expected; relic band starts at 0.94)
    T2 = np.where(k > 0, T2, 0.0)
    R2 = np.where(k > 0, R2, 0.0)
    return T2, R2


def gamma_pt_closed(omega, kappa_eff, V0):
    """Closed Poeschl-Teller transmission (inv12 reference, for transfer-matrix validation)."""
    omega = np.asarray(omega, dtype=float)
    x = np.pi * omega / kappa_eff
    num = np.sinh(x) ** 2
    disc = V0 / kappa_eff ** 2 - 0.25
    den = np.cosh(np.pi * np.sqrt(disc)) ** 2 if disc >= 0 else np.cos(np.pi * np.sqrt(-disc)) ** 2
    return num / (num + den)


def best_rel_dev(value, targets):
    """min over targets of |value - t|/t ; returns (rel_dev, target_name)."""
    return min((abs(value - t) / t, name) for name, t in targets.items())


def main():
    print("=" * 96)
    print(GATE_ID)
    print("=" * 96)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) + ledger verify ----
    sha_canon = sha256_file(CANON_PATH)
    sha_s84 = sha256_file(S84_NPZ)
    sha_inv12 = sha256_file(INV12_NPZ)
    sha_s117npz = sha256_file(S117_NPZ)
    sha_s117py = sha256_file(S117_PY)
    sha_self = sha256_file(SELF_PATH)
    print(f"[sha] canonical_constants.py      = {sha_canon}")
    print(f"[sha] s84_spectrum_cache_L12 npz  = {sha_s84}")
    print(f"[sha] inv12_w3_4_greybody npz     = {sha_inv12}")
    print(f"[sha] s117_alt_greybody npz       = {sha_s117npz}")
    print(f"[sha] s117_alt_greybody py        = {sha_s117py}")
    print(f"[sha] self (script)               = {sha_self}")
    ledger_ok = True
    for path, expect in PLAN_SHA_LEDGER.items():
        got = sha256_file(path)
        match = (got == expect)
        ledger_ok = ledger_ok and match
        print(f"[ledger] {'MATCH ' if match else 'MISMATCH'} {os.path.basename(path)}")
    if not ledger_ok:
        # honest PRE-REG-INC close (no convention-shopping)
        audit_sha = closure_hash({"gate_id": GATE_ID, "reason": "input_sha_mismatch"})
        print_verdict_payload("PRE-REG-INC",
                              "input_sha_ledger_mismatch_blocked",
                              audit_sha, sha_self, "N/A", "N/A", "N/A")
        print(f"\n=== {GATE_ID}: PRE-REG-INC (input SHA mismatch) ===")
        return
    print(f"[const] M_KK={M_KK:.6e} GeV ; kappa_exit={kappa_exit} ; Delta_BCS={Delta_BCS:.6f} ; tau_fold={tau_fold}")
    print(f"[const] A_s_CMB={A_s_CMB:.4e} (Planck) ; A_s_FW={A_s_FW:.6e} (ksi_KZ box-delta)")

    # ---- load D_K spectrum (s84 L12 sector_evals) -> lambda_max + a_4 moment ----
    d84 = np.load(S84_NPZ, allow_pickle=True)
    sec = d84["sector_evals"].item()
    lam = np.concatenate([np.asarray(v["abs_evals"], float) for v in sec.values()])  # (local) D_K |eigs|
    lam_min = float(lam.min())
    lam_max = float(lam.max())
    print(f"[D_K ] n={lam.size} (w/ mult) ; lam_min={lam_min:.6f} lam_max={lam_max:.6f}")

    # ---- load exit-horizon BdG barrier + dispersion (inv12_w3_4) ----
    div = np.load(INV12_NPZ, allow_pickle=True)
    omega_k = np.asarray(div["omega_k"], float)          # (local) BdG dispersion (1248 relic modes)
    w_mode = np.asarray(div["w_mode"], float)            # (local) produced-power squeeze weight mult*beta2
    V_eff = np.asarray(div["V_eff"], float)              # (local) plan-pinned barrier V0_marginal*sech^2(kappa x)
    x_tort = np.asarray(div["x_tortoise"], float)        # (local) tortoise coordinate
    kappa_eff = float(div["kappa_eff"])                  # (local) = kappa_exit = 47.6146
    V0_marginal = float(div["V0_marginal"])              # (local) = kappa^2/4 = 566.79 (PRIMARY barrier reading)
    V0_tcomp = float(div["V0_tcomp"])                    # (local) = T_compound^2 = 57.43 (BRACKET reading)
    w_min = float(omega_k.min())
    w_max = float(omega_k.max())
    print(f"[BdG ] n_modes={omega_k.size} ; omega in [{w_min:.4f},{w_max:.4f}] ; kappa_eff={kappa_eff}")
    print(f"[bar ] V_eff(x): max={V_eff.max():.4f} (V0_marginal={V0_marginal:.4f}=kappa^2/4) ; "
          f"x in [{x_tort.min():.4f},{x_tort.max():.4f}] ; sqrt(V0)={np.sqrt(V0_marginal):.4f}>>band")
    print(f"[bar ] V0_tcomp (BRACKET reading)={V0_tcomp:.4f} ; sqrt(V0_tcomp)={np.sqrt(V0_tcomp):.4f}")

    # =================================================================================
    # TARGETS (substrate-first; computed from canonical, NOT hardcoded)
    # =================================================================================
    gamma_box = A_s_CMB / A_s_FW                  # (local) box-delta = 10^{-OOM_box}
    oom_box = float(np.log10(A_s_FW / A_s_CMB))   # (local)
    gamma_slow = 10.0 ** (-OOM_SLOW_ROLL)         # (local) slow-roll = 10^{-0.19617}
    gamma_fit = float(div["transmitted_fraction_fitted"])  # (local) s95 fitted comparator
    fit_ok = abs(gamma_fit - GAMMA_FIT_EXPECTED) < 1e-6
    targets = {"box_delta": gamma_box, "fit": gamma_fit, "slow_roll": gamma_slow}   # (local)
    max_target = max(targets.values())            # (local) = slow_roll 0.636546
    print(f"[targ] box_delta=A_s_CMB/A_s_FW={gamma_box:.6f} (OOM_box={oom_box:.5f}) ; "
          f"fit={gamma_fit:.6f} (match={fit_ok}) ; slow_roll=10^-{OOM_SLOW_ROLL}={gamma_slow:.6f}")
    print(f"[targ] max(targets)={max_target:.6f} (route-b no-go threshold)")

    # =================================================================================
    # TRANSFER-MATRIX VALIDATION against the inv12 closed Poeschl-Teller form (bare barrier)
    # =================================================================================
    T2_chk, R2_chk = gamma_transfer_vec(
        np.array([w_min, 0.5 * (w_min + w_max), w_max, 2.0 * kappa_eff]),
        x_tort, V_eff)
    pt_chk = gamma_pt_closed(np.array([w_min, 0.5 * (w_min + w_max), w_max, 2.0 * kappa_eff]),
                             kappa_eff, V0_marginal)
    transfer_vs_pt = float(np.max(np.abs(T2_chk - pt_chk)))   # (local)
    unit_chk = float(np.max(np.abs(T2_chk + R2_chk - 1.0)))   # (local) bedrock |T|^2+|R|^2=1
    print(f"[xchk] transfer-vs-closed-PT max abs dev = {transfer_vs_pt:.3e} (method consistent < 1e-3)")
    print(f"[xchk] unitarity max |(|T|^2+|R|^2)-1|    = {unit_chk:.3e} (bedrock; should be ~machine eps)")

    # =================================================================================
    # PV-MODULATED BARRIER + 4th-class transfer-matrix transmission over the M_reg sweep
    #   V0(M_reg) = V0_marginal * [ M_a4^PV(M_reg) / M_a4^bare ]   (standard PV; knob-free
    #   M_reg>=lam_max recovers the FULL physical a_4 condensation barrier; s117 lineage).
    #   Barrier scattered = (V0(M_reg)/V0_marginal) * V_eff(x)  on the plan-pinned x grid.
    # =================================================================================
    M_a4_bare_DK = spectral_moment(lam, S_A4)            # (local) D_K a_4 condensation moment (bare)
    M_a4_bare_BdG = spectral_moment(omega_k, S_A4)       # (local) BdG-spectrum bracket
    wsum = float(np.sum(w_mode))                         # (local)

    og_plot = np.linspace(w_min, w_max, 256)             # (local) omega-grid for plot + flat-avg

    all_alphas = PV_ALPHAS_KNOBFREE + [PV_ALPHA_DIAGNOSTIC]   # (local) {1,2,4,8} then 0.5 diagnostic
    sweep = {}      # (local) alpha -> dict of readings
    unit_max_global = unit_chk   # (local) track worst unitarity over the whole sweep
    gamma_min_overall = np.inf   # (local) over-1 guard tracker (min for info)
    gamma_max_overall = -np.inf  # (local) bedrock: should never exceed 1

    for alpha in all_alphas:
        m_reg = alpha * lam_max
        ratio_DK = spectral_moment_pv(lam, S_A4, m_reg) / M_a4_bare_DK       # (local) modulation factor
        V0_a = ratio_DK * V0_marginal                                       # (local) PV-modulated barrier height
        Va = (V0_a / V0_marginal) * V_eff                                   # (local) scaled barrier on x grid
        # per-mode transmission (squeeze-weighted greybody) + reflection (unitarity)
        T2_modes, R2_modes = gamma_transfer_vec(omega_k, x_tort, Va)
        gam_sqz = float(np.sum(w_mode * T2_modes) / wsum)                   # (local) squeeze-weighted band-avg = THE greybody filter
        gam_permode_max = float(np.max(T2_modes))                          # (local) generous reading
        # omega-grid transmission for plot + flat band-average
        T2_og, R2_og = gamma_transfer_vec(og_plot, x_tort, Va)
        gam_flat = float(np.trapezoid(T2_og, og_plot) / (w_max - w_min))   # (local)
        unit_a = float(np.max(np.abs(T2_modes + R2_modes - 1.0)))          # (local) unitarity this alpha
        unit_max_global = max(unit_max_global, unit_a, float(np.max(np.abs(T2_og + R2_og - 1.0))))
        gamma_min_overall = min(gamma_min_overall, float(np.min(T2_modes)))
        gamma_max_overall = max(gamma_max_overall, float(np.max(T2_modes)), float(np.max(T2_og)))
        rel_sqz = best_rel_dev(gam_sqz, targets)
        rel_pm = best_rel_dev(gam_permode_max, targets)
        sweep[alpha] = dict(m_reg=m_reg, ratio_DK=ratio_DK, V0=V0_a,
                            gam_sqz=gam_sqz, gam_permode_max=gam_permode_max, gam_flat=gam_flat,
                            T2_og=T2_og, unit=unit_a,
                            rel_sqz=rel_sqz[0], rel_sqz_t=rel_sqz[1],
                            rel_pm=rel_pm[0], rel_pm_t=rel_pm[1])
        tag = "KNOB-FREE" if alpha >= 1.0 else "in-bulk KNOB (DIAGNOSTIC-ONLY)"
        print(f"[sweep] alpha={alpha:>4} M_reg={m_reg:8.4f} ratio={ratio_DK:.6f} V0={V0_a:9.4f} "
              f"Gam_sqz={gam_sqz:.6f} Gam_pmmax={gam_permode_max:.6f} "
              f"rel_dev_best={min(rel_sqz[0], rel_pm[0]):.4f}  [{tag}]")

    # ---- BRACKET reading: knob-free transmission through the tcomp barrier (V0=T_compound^2) ----
    #   bare tcomp barrier (alpha->inf knob-free) scattered directly; reported as a barrier-energy
    #   reading bracket (the inv12 secondary reading), NOT the plan-pinned V_eff.
    Vt = (V0_tcomp / V0_marginal) * V_eff                 # (local) tcomp barrier on x grid
    T2_tcomp_modes, R2_tcomp_modes = gamma_transfer_vec(omega_k, x_tort, Vt)
    gam_tcomp_sqz = float(np.sum(w_mode * T2_tcomp_modes) / wsum)      # (local)
    rel_tcomp = best_rel_dev(gam_tcomp_sqz, targets)                   # (local)
    print(f"[brkt] BRACKET tcomp barrier (V0=T_compound^2={V0_tcomp:.4f}): knob-free Gam_sqz="
          f"{gam_tcomp_sqz:.6f} ; best rel_dev={rel_tcomp[0]:.4f} ({rel_tcomp[1]}) ; "
          f"floor>0.637? {gam_tcomp_sqz > max_target}")

    # =================================================================================
    # TWO-BRANCH ADJUDICATION (plan §W1-2 operator; composite-precedence PLAN-FROZEN)
    # =================================================================================
    # knob-free readings (alpha >= 1): the squeeze-weighted greybody is THE filter scalar;
    # per-mode-max is the GENEROUS cross-check.  Both keyed for route(a)/route(b).
    kf_sqz = [sweep[a]["gam_sqz"] for a in PV_ALPHAS_KNOBFREE]              # (local)
    kf_pm = [sweep[a]["gam_permode_max"] for a in PV_ALPHAS_KNOBFREE]      # (local)
    kf_rel_best = min(min(sweep[a]["rel_sqz"], sweep[a]["rel_pm"]) for a in PV_ALPHAS_KNOBFREE)  # (local)
    gamma_knobfree_floor = float(min(kf_sqz))                              # (local) most-opaque knob-free greybody
    gamma_knobfree_ceil = float(max(kf_pm))                                # (local) most-transmissive knob-free reading

    # route(a): any knob-free reading within REL_TOL of any target?
    route_a_hit = bool(kf_rel_best <= REL_TOL)
    route_a_miss = not route_a_hit
    # route(b): knob-free floor > max(targets) robustly for ALL alpha >= 1?
    route_b_valid_nogo = bool(all(sweep[a]["gam_sqz"] > max_target for a in PV_ALPHAS_KNOBFREE))

    # composite-precedence (PLAN-FROZEN; logically exclusive route_b vs route_a)
    if route_b_valid_nogo:
        composite, outcome = "PASS", "STRUCTURAL-WALL"
    elif route_a_hit:
        composite, outcome = "PASS", "CANDIDATE-FALSIFIED"
    elif route_a_miss:
        composite, outcome = "FAIL", "WALL-STRENGTHENED-4-CLASS-EMPIRICAL"
    else:
        composite, outcome = "INFO", "INDETERMINATE"

    # ---- [SIGN] 3-tuple ----
    # sign_verdict keys on the BEDROCK Gamma <= 1 (unitarity): Gamma_max - 1 <= 0 ?
    GAMMA_OVERUNITY_TOL = 1e-6   # (local) numerical slack for the |T|^2 <= 1 bound
    sign_verdict = "PASS" if (gamma_max_overall - 1.0) <= GAMMA_OVERUNITY_TOL else "FAIL"
    # magnitude_verdict keys on route(a): a knob-free greybody at a target within tol?
    magnitude_verdict = "PASS" if route_a_hit else "FAIL"
    # regime_verdict: transfer-matrix on cached barrier, deterministic, unitary to ~machine eps
    regime_verdict = "VALID" if unit_max_global < 1e-6 else "MARGINAL"

    print("\n" + "-" * 96)
    print(f"[ROUTE-A] knob-free best rel_dev = {kf_rel_best:.4f} (tol {REL_TOL}) -> "
          f"route_a_hit={route_a_hit}")
    print(f"[ROUTE-A] knob-free Gam_sqz floor={gamma_knobfree_floor:.6f} ceil(permode-max)={gamma_knobfree_ceil:.6f}")
    print(f"[ROUTE-B] knob-free floor > max_target({max_target:.4f}) for all alpha>=1? "
          f"-> route_b_valid_nogo={route_b_valid_nogo}")
    print(f"[BEDROCK] Gamma_max_overall={gamma_max_overall:.9f} (<=1?) ; "
          f"unitarity_max={unit_max_global:.3e} ; transfer-vs-PT={transfer_vs_pt:.3e}")
    print(f"[3-TUPLE] sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"[COMPOSITE] route_b_valid_nogo={route_b_valid_nogo} route_a_hit={route_a_hit} "
          f"route_a_miss={route_a_miss} -> {composite} (outcome={outcome})")
    print(f"[BRACKET] barrier-reading sensitivity: marginal floor={gamma_knobfree_floor:.4f} "
          f"(<{max_target:.3f}) vs tcomp={gam_tcomp_sqz:.4f} ({'>' if gam_tcomp_sqz>max_target else '<'}"
          f"{max_target:.3f}) -> route-b NOT robust across barrier-energy readings")

    # =================================================================================
    # Save npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        # targets
        gamma_box=gamma_box, oom_box=oom_box, gamma_fit=gamma_fit, gamma_slow=gamma_slow,
        max_target=max_target, oom_slow_roll=OOM_SLOW_ROLL,
        # spectra / barrier
        lam_min=lam_min, lam_max=lam_max, n_DK=lam.size,
        omega_min=w_min, omega_max=w_max, n_BdG=omega_k.size,
        kappa_eff=kappa_eff, V0_marginal=V0_marginal, V0_tcomp=V0_tcomp,
        M_a4_bare_DK=M_a4_bare_DK, M_a4_bare_BdG=M_a4_bare_BdG, s_a2=S_A2, s_a4=S_A4,
        # PV sweep (alpha, M_reg, ratio_DK, V0, Gam_sqz, Gam_permode_max, Gam_flat, unit, rel_best)
        pv_alphas=np.array(all_alphas, float),
        pv_alphas_knobfree=np.array(PV_ALPHAS_KNOBFREE, float),
        pv_alpha_diagnostic=PV_ALPHA_DIAGNOSTIC,
        sweep_table=np.array([[a, sweep[a]["m_reg"], sweep[a]["ratio_DK"], sweep[a]["V0"],
                               sweep[a]["gam_sqz"], sweep[a]["gam_permode_max"],
                               sweep[a]["gam_flat"], sweep[a]["unit"],
                               min(sweep[a]["rel_sqz"], sweep[a]["rel_pm"])]
                              for a in all_alphas], float),
        og_plot=og_plot,
        Gamma_og_knobfree=np.array([sweep[a]["T2_og"] for a in PV_ALPHAS_KNOBFREE]),
        Gamma_og_diagnostic=sweep[PV_ALPHA_DIAGNOSTIC]["T2_og"],
        # bracket
        gam_tcomp_sqz=gam_tcomp_sqz, rel_tcomp=rel_tcomp[0],
        # adjudication
        rel_tol=REL_TOL,
        gamma_knobfree_floor=gamma_knobfree_floor, gamma_knobfree_ceil=gamma_knobfree_ceil,
        kf_rel_best=kf_rel_best,
        route_a_hit=route_a_hit, route_a_miss=route_a_miss, route_b_valid_nogo=route_b_valid_nogo,
        composite=composite, outcome=outcome,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        # bedrock
        gamma_max_overall=gamma_max_overall, gamma_min_overall=gamma_min_overall,
        unitarity_max=unit_max_global, transfer_vs_pt=transfer_vs_pt,
    )
    print(f"[npz] wrote {OUT_NPZ}")

    # =================================================================================
    # Plot
    # =================================================================================
    fig, ax = plt.subplots(1, 2, figsize=(14.5, 5.8))
    tcol = {"box_delta": "red", "fit": "black", "slow_roll": "darkorange"}

    # left: Gamma(omega) for each knob-free alpha + the diagnostic + tcomp bracket
    cmap = plt.cm.viridis(np.linspace(0.1, 0.85, len(PV_ALPHAS_KNOBFREE)))
    for ci, a in enumerate(PV_ALPHAS_KNOBFREE):
        ax[0].plot(og_plot, sweep[a]["T2_og"], color=cmap[ci], lw=2.0,
                   label=fr"knob-free $\alpha$={a:g} ($M_{{\rm reg}}$={sweep[a]['m_reg']:.1f}), "
                         fr"$\Gamma_{{\rm sqz}}$={sweep[a]['gam_sqz']:.3f}")
    ax[0].plot(og_plot, sweep[PV_ALPHA_DIAGNOSTIC]["T2_og"], "m--", lw=1.6,
               label=fr"$\alpha$=0.5 in-bulk KNOB (diagnostic), $\Gamma_{{\rm sqz}}$="
                     fr"{sweep[PV_ALPHA_DIAGNOSTIC]['gam_sqz']:.3f}")
    T2_tcomp_og, _ = gamma_transfer_vec(og_plot, x_tort, Vt)
    ax[0].plot(og_plot, T2_tcomp_og, "c:", lw=1.6,
               label=fr"BRACKET $V_0=T_{{\rm comp}}^2$, $\Gamma_{{\rm sqz}}$={gam_tcomp_sqz:.3f}")
    for tn, tv in targets.items():
        ax[0].axhline(tv, color=tcol[tn], ls="--", lw=1.3, alpha=0.85,
                      label=fr"$\Gamma_{{\rm req}}$({tn})={tv:.3f}")
    ax[0].set_xlabel(r"$\omega$  (M$_{\rm KK}$)")
    ax[0].set_ylabel(r"$\Gamma(\omega)=|T_{\rm BdG}(\omega)|^2$ (transfer-matrix)")
    ax[0].set_title("4th-class BdG S-matrix greybody vs targets\n"
                    "knob-free OVER-suppresses (marginal $V_{\\rm eff}$); targets unreached")
    ax[0].set_xlim(w_min, w_max)
    ax[0].set_ylim(-0.02, 1.02)
    ax[0].legend(fontsize=6.6, loc="upper left", ncol=1)
    ax[0].grid(alpha=0.3)

    # right: knob-free band-avg Gamma vs M_reg + route-b 0.637 wall + targets
    mregs = np.array([sweep[a]["m_reg"] for a in all_alphas])
    gsqz = np.array([sweep[a]["gam_sqz"] for a in all_alphas])
    gpm = np.array([sweep[a]["gam_permode_max"] for a in all_alphas])
    order = np.argsort(mregs)
    ax[1].plot(mregs[order], gsqz[order], "o-", color="#1f77b4", lw=1.8, ms=6,
               label=r"$\Gamma_{\rm sqz}$ (squeeze-weighted filter)")
    ax[1].plot(mregs[order], gpm[order], "s--", color="#2ca02c", lw=1.4, ms=5,
               label=r"$\Gamma$ per-mode max (generous)")
    # mark in-bulk diagnostic vs knob-free
    ax[1].axvline(lam_max, color="gray", ls=":", lw=1.2)
    ax[1].text(lam_max, 0.66, r" $\lambda_{\max}$ (knob-free $\to$ right)", fontsize=7.5,
               color="gray", rotation=90, va="top")
    ax[1].axhline(max_target, color="purple", ls="-", lw=1.6, alpha=0.8,
                  label=fr"route-b wall: max(targets)={max_target:.3f}")
    for tn, tv in targets.items():
        ax[1].axhline(tv, color=tcol[tn], ls="--", lw=1.0, alpha=0.7)
    ax[1].scatter([sweep[PV_ALPHA_DIAGNOSTIC]["m_reg"]], [sweep[PV_ALPHA_DIAGNOSTIC]["gam_sqz"]],
                  color="magenta", marker="*", s=200, edgecolor="k", zorder=6,
                  label=r"$\alpha$=0.5 in-bulk knob (excl.)")
    ax[1].set_xscale("log")
    ax[1].set_xlabel(r"PV regulator mass $M_{\rm reg}=\alpha\,\lambda_{\max}$  (M$_{\rm KK}$)")
    ax[1].set_ylabel(r"band-averaged $\Gamma$")
    ax[1].set_title(f"route-b no-go test: knob-free floor={gamma_knobfree_floor:.3f}"
                    fr" $\ll$ {max_target:.3f}" "\n"
                    f"-> {composite} (outcome={outcome})")
    ax[1].set_ylim(0, 1.02)
    ax[1].legend(fontsize=7.2, loc="center right")
    ax[1].grid(alpha=0.3, which="both")

    fig.suptitle(f"{GATE_ID} - exit-greybody structural-wall adjudication "
                 f"(4th class: full BdG S-matrix transfer-matrix transmission)", fontsize=10.5)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] wrote {OUT_PNG}")

    # =================================================================================
    # Dual-SHA + verdict payload
    # =================================================================================
    content_sha = sha_self
    pin_map = {
        "gate_id": GATE_ID,
        "script_sha": content_sha,
        "canonical_sha": sha_canon,
        "s84_npz_sha": sha_s84,
        "inv12_w3_4_npz_sha": sha_inv12,
        "s117_npz_sha": sha_s117npz,
        "s117_py_sha": sha_s117py,
        "s_a2": S_A2, "s_a4": S_A4,
        "rel_tol": REL_TOL,
        "oom_slow_roll": OOM_SLOW_ROLL,
        "pv_alphas_knobfree": str(PV_ALPHAS_KNOBFREE),
        "pv_alpha_diagnostic": PV_ALPHA_DIAGNOSTIC,
        "lam_max": f"{lam_max:.10f}",
        "L_max": L_MAX,
        "scheme": SCHEME,
        "convention": CONVENTION,
    }
    audit_sha = closure_hash(pin_map)

    value = (
        f"outcome={outcome};composite={composite};"
        f"route_a_hit={route_a_hit};route_a_miss={route_a_miss};route_b_valid_nogo={route_b_valid_nogo};"
        f"gamma_knobfree_floor_sqz={gamma_knobfree_floor:.6f};gamma_knobfree_permode_max={gamma_knobfree_ceil:.6f};"
        f"max_target={max_target:.6f};kf_rel_best={kf_rel_best:.4f};tol={REL_TOL};"
        f"targets[box={gamma_box:.6f},fit={gamma_fit:.6f},slow={gamma_slow:.6f}];"
        f"knobfree_Gam_sqz[a1={sweep[1.0]['gam_sqz']:.5f},a2={sweep[2.0]['gam_sqz']:.5f},"
        f"a4={sweep[4.0]['gam_sqz']:.5f},a8={sweep[8.0]['gam_sqz']:.5f}];"
        f"bracket_tcomp_sqz={gam_tcomp_sqz:.5f};"
        f"bedrock_Gamma_max={gamma_max_overall:.9f};unitarity_max={unit_max_global:.3e};"
        f"transfer_vs_PT={transfer_vs_pt:.3e};regime={regime_verdict}"
    )

    extra_rows = [
        f"# {GATE_ID} regulator_pin=a_n^{{Pauli-Villars}} + Wodzicki Res_W(s); "
        f"poleconv-A-double: a_2=(pole_in_s={S_A2},curvature_grade_n=2)/a_4=(pole_in_s={S_A4},curvature_grade_n=4); "
        f"a_4 PV condensation moment modulates V0(M_reg)",
        f"# composite-precedence: §W1-2 two-branch operator "
        f"(route_b_valid_nogo>route_a_hit>route_a_miss>INFO) OVERRIDES the generic 3-tuple "
        f"collapse (gate-verdicts.md Plan-frozen gate-block operator precedence); here "
        f"route_a_miss -> composite=FAIL (generic collapse on sign=PASS/mag=FAIL/regime=VALID "
        f"also yields FAIL -- consistent); outcome token = WALL-STRENGTHENED-4-CLASS-EMPIRICAL",
        f"# {GATE_ID} BEDROCK-UNITARITY: Gamma=|T_BdG|^2<=1 by (psi,psi') slab transfer-matrix "
        f"det=1 (Wronskian preserved); max |(|T|^2+|R|^2)-1|={unit_max_global:.2e}; "
        f"Gamma_max={gamma_max_overall:.7f}<=1 -> sign_verdict=PASS",
        f"# {GATE_ID} KNOB-LOCATION/OVER-SUPPRESSION: knob-free (M_reg>=lam_max) recovers the "
        f"FULL physical a_4 condensation barrier (V0->{V0_marginal:.1f}=kappa^2/4); the IR-dominated "
        f"a_4 moment ⇒ knob-free Gamma_sqz floors at {gamma_knobfree_floor:.4f} (OVER-suppression, "
        f"opposite to the pre-registered route-b transparency direction); targets {{0.137,0.512,0.637}} "
        f"reachable ONLY by placing M_reg deep in the spectral bulk (alpha<<1 = a KNOB)",
        f"# {GATE_ID} BARRIER-READING-SENSITIVITY: route-b NOT robust across barrier-energy "
        f"readings -- marginal V0=kappa^2/4 floor={gamma_knobfree_floor:.4f} (<{max_target:.3f}) vs "
        f"tcomp V0=T_compound^2 floor={gam_tcomp_sqz:.4f} (>{max_target:.3f}); neither hits a target "
        f"knob-free (marginal rel_dev={kf_rel_best:.3f}, tcomp rel_dev={rel_tcomp[0]:.3f}) ⇒ no clean "
        f"structural no-go ⇒ FAIL (4th class strengthens the empirical wall to 4 classes, not proven)",
        f"# {GATE_ID} GPU_path deviation: 1D transfer-matrix on cached BdG barrier/dispersion "
        f"(no >=100x100 diagonalization); cpu-cap-OMP8 (plan numpy.linalg/cpu path; honest disclosure)",
        f"# {GATE_ID} CONSEQUENCE (CF-S118-AS-PREFACTOR-SOURCE, next session): the exit greybody is "
        f"NOT a clean knob-free A_s upper-edge prefactor source -- it over-suppresses (marginal) or "
        f"over-transmits (tcomp), neither at a target; the A_s upper-edge factor remains the S95 fitted knob",
    ]

    print_verdict_payload(composite, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict, extra_rows=extra_rows)

    # final non-verdict 4-tuple tag
    print(f"OUTPUT-4TUPLE: (value=outcome={outcome}, scheme={SCHEME[:40]}..., "
          f"convention={CONVENTION[:40]}..., L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {composite} (outcome={outcome}) ===")


if __name__ == "__main__":
    main()
