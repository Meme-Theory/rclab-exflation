#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S112 W3-2 CF-S112-FLOQUET3-HPAR-TIGHTEN — physical-Veff settled-envelope delta_tau_amp
=====================================================================================

Gate: CF-S112-FLOQUET3-HPAR-TIGHTEN  ([CHAIN] with directional ring-down-envelope claim)

Pre-registered threshold (plan §W3-2):
  metric = |h_par_derived - 8.3e-4| / 8.3e-4
  PASS iff metric <= 0.10 ;  INFO iff 0.10 < metric <= 1.0 ;  FAIL iff metric > 1.0.
  h_par_derived = delta_tau_amp * (d ln E^2/d tau)  with  (d ln E^2/d tau) = s_near1 = 0.14979505...
  (the CACHED relic-mode spectral leg, s111 npz; NOT re-derived).

WHAT THIS GATE REPLACES
-----------------------
S111-CF-FLOQUET3 (INFO, h_par_derived=2.759e-4, metric=0.668, factor-3.01-low, regime=MARGINAL)
reconstructed delta_tau_amp via a SINGLE one-period Hubble-friction decay
  delta_tau_amp = A_launch * exp(-gamma * T_ring) = 1.4236 * 1.294e-3 = 1.842e-3,
a HEURISTIC forced by the s76-flagged runaway of the BARE V_eff parameterization (the s73b
trajectory runs tau -> -99.885, unphysical; there is NO minimum to ring around). This gate replaces
that heuristic by integrating the FULL coupled modulus+Friedmann ODE
  tau_ddot + 3 H tau_dot + dV_eff/dtau = 0 ,   H^2 = (1/3)[ (1/2) tau_dot^2 + V_eff(tau) ]
with V_eff = the S66 Volovik-tracking effective potential (DILUTION-CC, S66), which has a GENUINE
minimum at tau_fold (the tracking-vacuum equilibrium rho_vac ~ M_Pl^2 H^2 supplies the restoring
stiffness the bare V_KK lacks). The modulus then rings DOWN to a steady residual envelope
delta_tau_amp rather than running away. delta_tau_amp is read as the late-time settled ring-down
envelope, h_par assembled, and compared to the guard-floor 8.3e-4 at the 10% band.

PHYSICS (substrate-first):
  PHONONIC. tau IS the Jensen deformation parameter (Level-2 moduli-deformation substrate-IS). The
  Mach-13.75 supersonic transit through the van Hove fold is IMPULSIVE; the substrate FREEZES
  diabatically (the Ordered Veil: S_ent=0, R_therm=5251.82, the GGE never thermalizes). What remains
  is a residual modulus ring-down: tau(t) launched from tau_fold with the transit velocity v_launch,
  overshooting and ringing back, DAMPED by Hubble friction 3 H tau_dot. The ring-down IS the periodic
  drive on the relic modes (the Mathieu source); h_par = delta_tau_amp * (d ln E^2/d tau) is its
  fractional depth. The S66 Volovik-tracking V_eff is the substrate's OWN emergent effective
  potential (vacuum-tracking thermodynamics), not an externally-imposed inflaton potential -- the
  LCDM "reheating/preheating" vocabulary is INAPPLICABLE (this is GGE-relic ring-down, not slow-roll).

  NON-BLOCKING: the §VII.BP DEAD verdict (no discrete time crystal) is UNAFFECTED by any verdict --
  it requires only h_par << the DTC threshold 14/193 = 0.07253886 (S111-CF-FLOQUET2, QQ-exact), which
  every reading (1.4e-4 to 2.8e-4, and any settled-V_eff value in the same decade) satisfies
  emphatically. PASS/INFO/FAIL here is corridor-narrowing, not status-changing.

V_eff CONSTRUCTION (Volovik-tracking, minimum at tau_fold; NOT tuned to the PASS band)
--------------------------------------------------------------------------------------
  V_eff(tau) = V_KK(tau) + V_track(tau)
    V_KK(tau)   : the s52 spectral-action modulus potential, quadratic fit through the 3 s52
                  calibration points V_KK(0)=-46.6528, V_KK(fold)=-47.0760, V_KK(0.50)=-53.3794 M_KK^4.
                  V_KK is monotone-DECREASING through the fold (dV_KK/dtau|_fold < 0, V_KK''<0) -- this
                  is the source of the bare runaway.
    V_track(tau): the Volovik-tracking restoring term. The DILUTION-CC tracking-vacuum equilibrium
                  (rho_vac ~ M_Pl^2 H^2, S66) pins the modulus AT tau_fold; the restoring term is
                  therefore fixed by TWO substrate conditions, NOT by the PASS band:
                    (i)  dV_eff/dtau|_fold = 0   (tau_fold IS the tracking equilibrium minimum)
                    (ii) V_eff''(tau_fold) = M_mod * omega_tau^2   with the modulus ring-down
                         frequency omega_tau pinned to the substrate-canonical omega_q = 2.012813
                         (the relic-mode frequency near a=1; the SAME scale the S111 heuristic used
                         as a ring-down proxy -- now DERIVED from the V_eff curvature requirement,
                         not assumed). M_mod = G_mod_full = M_p^2 * G_DeWitt = 116.6319 M_KK^2 (s52).
                  V_track(tau) = -dV_KK/dtau|_fold * (tau - tau_fold)
                                 + (1/2)*(V_eff'' - V_KK'')*(tau - tau_fold)^2
                  so that V_eff'(tau_fold)=0 and V_eff''(tau_fold)=M_mod*omega_q^2 EXACTLY.
  This is a SUBSTRATE-PINNED construction: omega_tau = omega_q is the relic-mode anchor, NOT the
  delta_tau_amp PASS band. The gate then asks, HONESTLY, where the settled-envelope delta_tau_amp of
  THIS physical V_eff lands relative to the guard-floor target.

Output 4-tuple:
  (value=h_par_derived, scheme=FW, convention=RATIO-physical-Veff-settled-envelope-x-spectral-sensitivity, L_max=12)

Classification: PHONONIC
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Standard imports (OMP cap BEFORE numpy per computation-environment.md)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # 2-component ODE; CPU-cap per GPU_path=cpu-cap-OMP8
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 1b — Canonical constants (MANDATORY; _shared on path first, per S111 pattern)
# ---------------------------------------------------------------------------
_SHARED = str((Path(__file__).resolve().parent.parent / "_shared"))  # (local) computations/_shared
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)
from canonical_constants import tau_fold, G_DeWitt, M_KK  # noqa: E402  (framework constants)

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S112"                                                          # (local)
GATE_ID = "CF-S112-FLOQUET3-HPAR-TIGHTEN"                                 # (local)
SCHEME = "FW"                                                             # (local)
CONVENTION = "RATIO-physical-Veff-settled-envelope-x-spectral-sensitivity"  # (local)
L_MAX = 12                                                                # (local)

# Pre-registered bands (plan §W3-2)
PASS_BAND = 0.10                                                          # (local) |h_par-guard|/guard <= 0.10 => PASS
INFO_BAND = 1.0                                                           # (local) 0.10 < metric <= 1.0 => INFO

OUT_NPZ = SESSION_DIR / "s112_cf_floquet3_hpar_tighten.npz"
OUT_PNG = SESSION_DIR / "s112_cf_floquet3_hpar_tighten.png"

# ---- Machinery pins (plan §W3-2 machinery_pin_map) ----
N_EVAL = 50000                                                           # (local) ODE trajectory grid
RTOL = 1e-9                                                              # (local) solve_ivp rtol
ATOL = 1e-12                                                             # (local) solve_ivp atol
H_POST_FOLD = 0.9753935187731557     # (local) post-fold Friedmann rate (s73b/s111 H_sol[0])
A_LAUNCH = 1.4236151017033278        # (local) nonlinear overshoot launch amplitude tau_max-tau_fold (s111)
V_LAUNCH = 26.544972625732246        # (local) launch velocity = v_terminal (canonical; s73b dtau_sol[0])
OMEGA_Q = 2.012813                   # (local) relic-mode frequency near a=1 (s111/inv12); modulus-freq anchor
DLNE2_DTAU = 0.14979505187425238     # (local) (d ln E^2/d tau) at near-a=1 relic mode -- CACHED spectral leg
DLNE2_DTAU_MEDIAN = 0.07533807832928088  # (local) median relic-band spectral sensitivity (range lower)
H_PAR_GUARD = 0.00083                # (local) S101-W1-QEQ-RELIC-ODDFLOOR guard-floor target (8.3e-4)
DTAU_AMP_S111 = 0.0018415220578406977    # (local) S111 one-period heuristic delta_tau_amp (REPLACED)
# Modulus kinetic metric (s52 unified action): G_mod_full = M_p^2 * G_DeWitt = 116.6319 M_KK^2
G_MOD_FULL = 23.3264 * G_DeWitt      # (local) M_p^2 (=23.3264 M_KK^2, s52) * G_DeWitt(=5.0 canonical)
# s52 V_KK calibration points (M_KK^4)
VKK_0 = -46.6528                     # (local) V_KK(tau=0), s52
VKK_FOLD = -47.0760                  # (local) V_KK(tau_fold), s52
VKK_50 = -53.3794                    # (local) V_KK(tau=0.50), s52

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-111" / "s111_cf_floquet3_dtau_amp_afterglow.npz",
    COMPUTATIONS_DIR / "session-73" / "s73b_efold_mapping.npz",
    COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
    COMPUTATIONS_DIR / "investigation-12" / "inv12_w3_2_floquet_ordered_veil_resonance.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Physical Volovik-tracking V_eff + coupled ODE
# ---------------------------------------------------------------------------
def build_Veff():
    """Build the S66 Volovik-tracking V_eff(tau) with a GENUINE minimum at tau_fold.

    V_eff(tau) = V_KK(tau) + V_track(tau)
      V_KK(tau)    = quadratic fit through s52 points (monotone-decreasing; the bare-runaway source)
      V_track(tau) = the Volovik-tracking restoring term, pinned by TWO substrate conditions:
                     (i)  dV_eff/dtau|_fold = 0    (tracking-vacuum equilibrium AT tau_fold, DILUTION-CC)
                     (ii) V_eff''(tau_fold) = M_mod * omega_q^2  (modulus ring-down freq = relic anchor)

    Returns (Veff, dVeff, Veff_min, omega_tau, Vpp_eff, dVKK_fold, VKK_pp).
    """
    tf = tau_fold  # (local) canonical 0.19
    # V_KK quadratic fit V_KK(t) = a t^2 + b t + c through (0, VKK_0), (tf, VKK_FOLD), (0.5, VKK_50)
    # Solve the 3x3 linear system.
    Amat = np.array([[0.0, 0.0, 1.0],
                     [tf * tf, tf, 1.0],
                     [0.25, 0.5, 1.0]])         # (local)
    bvec = np.array([VKK_0, VKK_FOLD, VKK_50])  # (local)
    a_q, b_q, c_q = np.linalg.solve(Amat, bvec)  # (local) V_KK quad coeffs

    def VKK(t):
        return a_q * t * t + b_q * t + c_q

    def dVKK(t):
        return 2.0 * a_q * t + b_q

    VKK_pp = 2.0 * a_q                          # (local) V_KK''(tau) constant for quad
    dVKK_fold = dVKK(tf)                         # (local) bare slope at fold (< 0; runaway source)

    # Tracking-equilibrium curvature: V_eff''(tau_fold) = M_mod * omega_q^2
    Vpp_eff = G_MOD_FULL * OMEGA_Q * OMEGA_Q     # (local) required V_eff'' at the minimum
    k_track = Vpp_eff - VKK_pp                    # (local) restoring stiffness from the tracking term

    # V_track(tau) = -dVKK_fold*(tau-tf) + (1/2)*k_track*(tau-tf)^2
    #   => V_eff'(tf) = dVKK(tf) - dVKK_fold + 0 = 0    (condition i)
    #   => V_eff''(tf) = VKK_pp + k_track = Vpp_eff      (condition ii)
    def Veff(t):
        dt = t - tf
        return VKK(t) - dVKK_fold * dt + 0.5 * k_track * dt * dt

    def dVeff(t):
        dt = t - tf
        return dVKK(t) - dVKK_fold + k_track * dt

    Veff_min = Veff(tf)                          # (local) V_eff at the minimum (for the shift)
    omega_tau = np.sqrt(Vpp_eff / G_MOD_FULL)    # (local) modulus ring-down frequency = sqrt(V''/M_mod)
    return Veff, dVeff, Veff_min, omega_tau, Vpp_eff, dVKK_fold, VKK_pp


def integrate_coupled_ode(Veff, dVeff, Veff_min, t_end):
    """Integrate tau_ddot + 3 H tau_dot + dV_eff/dtau = 0 with H^2 = (1/3)[(1/2)tau_dot^2 + V_eff_shifted].

    Substrate units. V_eff is SHIFTED so the Friedmann energy density is non-negative at the minimum:
    V_eff_shift(tau) = V_eff(tau) - V_eff(tau_fold) >= 0 near the minimum (the tracking-vacuum
    DILUTION-CC subtracts the constant vacuum piece; rho_vac/rho_obs=1.032, Gamma_eff=0.99970).
    The Friedmann rate is calibrated so that at LAUNCH (tau=tau_fold, tau_dot=v_launch) H equals the
    physical post-fold rate H_POST_FOLD (the s73b/s111 value) -- this fixes the overall energy scale
    consistently with the prior gate's Friedmann normalization.
    """
    tf = tau_fold  # (local)
    # Friedmann normalization: at launch KE = (1/2) v_launch^2, V_eff_shift(tf)=0, so
    # rho_launch = (1/2) v_launch^2. Calibrate the Friedmann constant kappa so H_launch = H_POST_FOLD:
    #   H^2 = kappa * rho ;  H_POST_FOLD^2 = kappa * (1/2) v_launch^2  =>  kappa = H_POST_FOLD^2 / ((1/2) v_launch^2)
    rho_launch = 0.5 * V_LAUNCH * V_LAUNCH       # (local) launch energy density (KE dominated)
    kappa = (H_POST_FOLD * H_POST_FOLD) / rho_launch  # (local) Friedmann constant (substrate units)

    def H_of(tau, dtau):
        rho = 0.5 * dtau * dtau + (Veff(tau) - Veff_min)  # (local) shifted energy density
        rho = max(rho, 0.0)                                # (local) guard tiny negative round-off
        return np.sqrt(kappa * rho)

    def rhs(t, y):
        tau, dtau = y  # (local)
        H = H_of(tau, dtau)  # (local)
        ddtau = -3.0 * H * dtau - dVeff(tau)  # (local) modulus EOM with Hubble friction
        return [dtau, ddtau]

    t_eval = np.linspace(0.0, t_end, N_EVAL)  # (local)
    sol = solve_ivp(rhs, (0.0, t_end), [tf, V_LAUNCH], method="LSODA",
                    t_eval=t_eval, rtol=RTOL, atol=ATOL, max_step=t_end / 2000.0)
    return sol, kappa


def settled_envelope(t, tau, tf, omega_tau, gamma):
    """Read delta_tau_amp = the LATE-TIME settled ring-down envelope.

    The modulus delta = tau - tau_fold is launched from tau_fold with the transit velocity, overshoots
    (the nonlinear A_overshoot ~ A_launch transient), turns around, and rings DOWN under Hubble friction
    toward the minimum. The plan defines delta_tau_amp as "the late-time settled ring-down envelope (the
    asymptotic |tau - tau_fold| oscillation amplitude AFTER the transient decays)". The reading is
    therefore taken at the LATE-TIME END of the pinned integration window (t_end = 30*T_ring), NOT at the
    launch transient:

      delta_tau_amp = (1/2) * (max - min) of delta over the FINAL full ring-down period
                      [t_end - T_ring, t_end]

    This is a deterministic, window-end definition (NO epoch-shopping): the half-amplitude of the LAST
    complete oscillation the modulus executes before the integration window closes. It is the residual
    amplitude with which the modulus is still ringing once the launch transient has decayed -- the
    amplitude that drives the relic modes during the settled ring-down epoch (the Mathieu source operates
    during the settled phase, NOT at the impulsive transient launch). The overshoot transient is reported
    separately (A_overshoot) and is explicitly EXCLUDED from the settled-envelope read.
    """
    delta = tau - tf  # (local)
    # Damped-oscillator ring-down period
    disc = omega_tau * omega_tau - gamma * gamma  # (local)
    omega_d = np.sqrt(disc) if disc > 0 else omega_tau  # (local)
    T_ring = 2.0 * np.pi / omega_d                # (local)
    # --- launch transient (overshoot), reported separately, EXCLUDED from the settled read ---
    i_peak = int(np.argmax(np.abs(delta[: max(2, N_EVAL // 4)])))  # (local)
    A_overshoot = abs(delta[i_peak])              # (local) nonlinear overshoot (~ A_launch)
    decay_one_period = np.exp(-gamma * T_ring)    # (local) one-period decay (the S111 heuristic factor)
    # --- LATE-TIME settled envelope: half-amplitude of the FINAL full ring-down period ---
    t_end = t[-1]                                  # (local) integration window end (= 30*T_ring)
    mask_final = (t >= t_end - T_ring) & (t <= t_end)  # (local) last complete period
    if np.count_nonzero(mask_final) >= 3:
        d_fin = delta[mask_final]                  # (local)
        env_ode = 0.5 * (np.max(d_fin) - np.min(d_fin))  # (local) settled half-amplitude (canonical)
    else:
        # fallback: analytic damped-oscillator envelope at t_end from the linear launch amplitude
        env_ode = (V_LAUNCH / omega_d) * np.exp(-gamma * t_end)  # (local)
    return env_ode, A_overshoot, decay_one_period, T_ring, omega_d


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # --- Build the physical Volovik-tracking V_eff ---
    Veff, dVeff, Veff_min, omega_tau, Vpp_eff, dVKK_fold, VKK_pp = build_Veff()
    gamma = 1.5 * H_POST_FOLD  # (local) Hubble friction: 3H tau_dot => gamma = 3H/2

    print("=== Physical Volovik-tracking V_eff (minimum at tau_fold) ===")
    print(f"  tau_fold = {tau_fold}")
    print(f"  V_KK''(tau)            = {VKK_pp:.4f} M_KK^2  (bare; < 0 => no minimum, runaway source)")
    print(f"  dV_KK/dtau|_fold       = {dVKK_fold:.4f} M_KK^3 (bare slope; the runaway force)")
    print(f"  M_mod (G_mod_full)     = {G_MOD_FULL:.4f} M_KK^2 (= M_p^2 * G_DeWitt, s52)")
    print(f"  V_eff''(tau_fold)      = {Vpp_eff:.4f} M_KK^4 (= M_mod * omega_q^2; tracking-pinned)")
    print(f"  omega_tau (sqrt V''/M) = {omega_tau:.6f} M_KK  (= omega_q = {OMEGA_Q}: "
          f"{np.isclose(omega_tau, OMEGA_Q, rtol=1e-9)})")
    print(f"  dV_eff/dtau|_fold      = {dVeff(tau_fold):.3e} (== 0 by construction: "
          f"{np.isclose(dVeff(tau_fold), 0.0, atol=1e-9)})")
    print(f"  gamma = 3H/2           = {gamma:.6f} M_KK  (H_post_fold={H_POST_FOLD})")
    disc0 = omega_tau * omega_tau - gamma * gamma  # (local)
    print(f"  discriminant w^2-g^2   = {disc0:.6f} => {'UNDERDAMPED' if disc0 > 0 else 'OVERDAMPED'}")
    print()

    # --- Integrate the coupled ODE to the late-time settled envelope ---
    # T_settle ~ 30 ring-down periods (plan: ~30*T_ring ~ 136 M_KK^-1)
    omega_d0 = np.sqrt(disc0) if disc0 > 0 else omega_tau  # (local)
    T_ring0 = 2.0 * np.pi / omega_d0                # (local)
    t_end = 30.0 * T_ring0                          # (local) integration window
    print(f"=== Coupled-ODE integration (tau_ddot + 3H tau_dot + dV_eff/dtau = 0) ===")
    print(f"  T_ring = {T_ring0:.4f} M_KK^-1 ; integration window t_end = 30*T_ring = {t_end:.4f} M_KK^-1")
    sol, kappa = integrate_coupled_ode(Veff, dVeff, Veff_min, t_end)
    print(f"  solve_ivp success={sol.success}, n_steps={sol.t.size}, method=LSODA, rtol={RTOL}, atol={ATOL}")
    print(f"  Friedmann kappa = {kappa:.6e} (calibrated so H_launch = H_post_fold)")
    tau_traj = sol.y[0]   # (local)
    dtau_traj = sol.y[1]  # (local)
    print(f"  tau trajectory: launch={tau_traj[0]:.4f}, max={tau_traj.max():.4f}, "
          f"min={tau_traj.min():.4f}, final={tau_traj[-1]:.6f} (settles toward tau_fold={tau_fold})")

    # --- Read the settled ring-down envelope delta_tau_amp ---
    env_ode, A_overshoot, decay_one_period, T_ring, omega_d = settled_envelope(
        sol.t, tau_traj, tau_fold, omega_tau, gamma)
    delta_tau_amp = float(env_ode)  # (local) settled residual ring-down amplitude (canonical)
    print()
    print("=== Settled ring-down envelope ===")
    print(f"  nonlinear overshoot A_overshoot = {A_overshoot:.6f} (cf. A_launch={A_LAUNCH:.4f})")
    print(f"  decay/period exp(-gamma T_ring)  = {decay_one_period:.6e}")
    print(f"  settled delta_tau_amp (ODE)      = {delta_tau_amp:.6e}")
    print(f"    cf. S111 one-period heuristic  = {DTAU_AMP_S111:.6e} "
          f"(ratio {delta_tau_amp / DTAU_AMP_S111:.3f})")
    print(f"  linearization delta/tau_fold     = {delta_tau_amp / tau_fold:.4f} (OK iff << 1)")

    # --- Assemble h_par and evaluate the gate ---
    h_par_derived = delta_tau_amp * DLNE2_DTAU      # (local) PRIMARY (near-a=1 spectral leg)
    h_par_median = delta_tau_amp * DLNE2_DTAU_MEDIAN  # (local) range lower (median band sensitivity)
    metric = abs(h_par_derived - H_PAR_GUARD) / H_PAR_GUARD  # (local) verdict metric
    print()
    print("=== h_par assembly + gate ===")
    print(f"  h_par_derived = delta_tau_amp * dlnE2_dtau = {delta_tau_amp:.6e} * {DLNE2_DTAU:.6f} "
          f"= {h_par_derived:.6e}")
    print(f"  h_par_median (range lower)                 = {h_par_median:.6e}")
    print(f"  guard-floor target h_par                   = {H_PAR_GUARD:.6e} (S101-W1-QEQ-RELIC-ODDFLOOR)")
    print(f"  metric = |h_par_derived - guard|/guard     = {metric:.6f} (PASS<=0.10, INFO<=1.0)")
    # PASS band cross-check on delta_tau_amp
    dtau_pass_lo = H_PAR_GUARD * (1 - PASS_BAND) / DLNE2_DTAU  # (local)
    dtau_pass_hi = H_PAR_GUARD * (1 + PASS_BAND) / DLNE2_DTAU  # (local)
    print(f"  PASS band on delta_tau_amp: [{dtau_pass_lo:.4e}, {dtau_pass_hi:.4e}] "
          f"(unity target {H_PAR_GUARD / DLNE2_DTAU:.4e})")

    # --- 3-tuple (sign / magnitude / regime) ---
    # sign: predicted direction is that the physical settled V_eff RAISES delta_tau_amp vs the
    #   one-period heuristic (h_par increases with delta_tau_amp, +0.14980 > 0). sign=PASS iff the
    #   settled value moves in the predicted direction (settled >= one-period heuristic) AND h_par
    #   stays positive (correct sign of the modulation depth).
    sign_pass = (delta_tau_amp >= DTAU_AMP_S111) and (h_par_derived > 0)  # (local)
    sign_verdict = "PASS" if sign_pass else "FAIL"  # (local)
    # magnitude
    if metric <= PASS_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif metric <= INFO_BAND:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # regime: linearization validity (delta_tau_amp/tau_fold << 1) over the ring-down window.
    lin_ratio = delta_tau_amp / tau_fold  # (local)
    # breach fraction: fraction of the integration window where |delta|/tau_fold > 0.5 (linearization
    # breakdown for the Mathieu normal-form expansion). The overshoot transient breaches; the settled
    # ring-down does not.
    breach = np.count_nonzero(np.abs(tau_traj - tau_fold) / tau_fold > 0.5) / tau_traj.size  # (local)
    if breach <= 0.05:
        regime_verdict = "VALID"  # (local)
    elif breach <= 0.50:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)
    print(f"  linearization ratio delta/tau_fold = {lin_ratio:.4f}; breach_frac (|delta|/tf>0.5) = {breach:.4f}")

    # --- Composite collapse (gate-verdicts.md generic rule) ---
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        verdict = "INFO"  # (local)
    else:
        verdict = "PASS"  # (local)

    print()
    print(f"  sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict} => composite={verdict}")
    # DTC non-blocking cross-check
    dtc_thresh = 14.0 / 193.0  # (local) S111-CF-FLOQUET2 QQ-exact DTC threshold
    print(f"  [NON-BLOCKING] h_par_derived={h_par_derived:.4e} << DTC threshold 14/193={dtc_thresh:.6f}: "
          f"{h_par_derived < dtc_thresh} (§VII.BP DEAD UNAFFECTED)")

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        # canonical results
        delta_tau_amp=delta_tau_amp, h_par_derived=h_par_derived, h_par_median=h_par_median,
        metric=metric, verdict=str(verdict),
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        # V_eff construction
        omega_tau=omega_tau, Vpp_eff=Vpp_eff, VKK_pp=VKK_pp, dVKK_fold=dVKK_fold,
        G_mod_full=G_MOD_FULL, kappa=kappa, gamma=gamma, omega_d=omega_d, T_ring=T_ring,
        # envelope read
        A_overshoot=A_overshoot, decay_one_period=decay_one_period,
        lin_ratio=lin_ratio, breach_frac=breach,
        # comparison anchors
        h_par_guard=H_PAR_GUARD, dtau_amp_S111=DTAU_AMP_S111, dlnE2_dtau=DLNE2_DTAU,
        dlnE2_dtau_median=DLNE2_DTAU_MEDIAN, A_launch=A_LAUNCH, v_launch=V_LAUNCH,
        H_post_fold=H_POST_FOLD, omega_q=OMEGA_Q,
        dtau_pass_lo=dtau_pass_lo, dtau_pass_hi=dtau_pass_hi,
        PASS_BAND=PASS_BAND, INFO_BAND=INFO_BAND, dtc_thresh=dtc_thresh,
        # trajectory
        traj_t=sol.t, traj_tau=tau_traj, traj_dtau=dtau_traj,
        t_end=t_end, ode_success=bool(sol.success),
    )
    print(f"\n  saved: {OUT_NPZ.name}")

    # --- Plot ---
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    # (a) modulus trajectory + ring-down envelope
    ax = axes[0]
    ax.plot(sol.t, tau_traj - tau_fold, color="navy", lw=0.9, label=r"$\tau(t)-\tau_{\rm fold}$ (coupled ODE)")
    ax.axhline(0.0, color="gray", ls="-", lw=0.6)
    ax.axhline(delta_tau_amp, color="crimson", ls="--", lw=1.3,
               label=rf"settled $\delta\tau_{{\rm amp}}={delta_tau_amp:.2e}$")
    ax.axhline(-delta_tau_amp, color="crimson", ls="--", lw=1.3)
    ax.axhline(DTAU_AMP_S111, color="darkorange", ls=":", lw=1.2,
               label=rf"S111 one-period $={DTAU_AMP_S111:.2e}$")
    ax.axhspan(dtau_pass_lo, dtau_pass_hi, color="green", alpha=0.12,
               label=rf"PASS band $\delta\tau_{{\rm amp}}$")
    ax.set_xlabel(r"$t$  (M$_{\rm KK}^{-1}$)")
    ax.set_ylabel(r"$\tau - \tau_{\rm fold}$")
    ax.set_title(rf"Volovik-tracking $V_{{\rm eff}}$ modulus ring-down ($\omega_\tau={omega_tau:.3f}$, $Q=${omega_d/(2*gamma):.2f})")
    ax.legend(fontsize=7, loc="upper right")
    # (b) h_par bar comparison
    ax = axes[1]
    labels = ["S111\none-period", "this gate\nsettled-ODE", "guard-floor\ntarget"]  # (local)
    vals = [DTAU_AMP_S111 * DLNE2_DTAU, h_par_derived, H_PAR_GUARD]  # (local)
    colors = ["darkorange", "navy", "crimson"]  # (local)
    ax.bar(labels, vals, color=colors, alpha=0.75)
    ax.axhspan(H_PAR_GUARD * (1 - PASS_BAND), H_PAR_GUARD * (1 + PASS_BAND), color="green", alpha=0.15,
               label="10% PASS band")
    ax.axhline(dtc_thresh, color="black", ls="--", lw=1.0, label=rf"DTC threshold $14/193={dtc_thresh:.3f}$")
    ax.set_ylabel(r"$h_{\rm par}$")
    ax.set_yscale("log")
    ax.set_title(rf"$h_{{\rm par}}$: settled-ODE $={h_par_derived:.3e}$, metric $={metric:.3f}$ ({verdict})")
    ax.legend(fontsize=7)
    fig.suptitle(f"{GATE_ID}: physical-Veff settled-envelope h_par tighten", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"  saved: {OUT_PNG.name}")

    # --- Emit 4-tuple + verdict payload ---
    tag = emit_4tuple(h_par_derived, SCHEME, CONVENTION, L_MAX)
    print()
    print(tag)
    extra = [
        f"# composite-precedence: generic-collapse per gate-verdicts.md; sign={sign_verdict} "
        f"magnitude={magnitude_verdict} regime={regime_verdict}",
        f"# delta_tau_amp_settled={delta_tau_amp:.6e} (ODE; replaces S111 one-period {DTAU_AMP_S111:.4e}); "
        f"V_eff''={Vpp_eff:.2f}=M_mod*omega_q^2, omega_tau={omega_tau:.5f}, Q={omega_d/(2*gamma):.4f}",
        f"# regulator_pin=N/A (delta_tau_amp is a modulus ring-down ODE amplitude, NOT a Seeley-DeWitt "
        f"a_n residue; dlnE2_dtau is an eigenvalue log-derivative on the cached L12 spectrum)",
        f"# NON-BLOCKING: h_par={h_par_derived:.4e} << DTC 14/193={dtc_thresh:.5f}; §VII.BP DEAD UNAFFECTED",
    ]
    payload = print_verdict_payload(
        verdict, h_par_derived, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        companion_note=f"metric={metric:.4f} vs guard 8.3e-4; delta_tau_amp_settled={delta_tau_amp:.4e}",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
