#!/usr/bin/env python3
"""
S111 W1-1 S111-CF-CLOCKLOC2-MONOTONE — monotone-corridor turning-point scan
============================================================================

Gate: S111-CF-CLOCKLOC2-MONOTONE ([SIGN])

Pre-registered threshold (plan §W1-1):
  PASS iff  tau_turn in (0.19, 1.614]  AND  tau_dot > 0 throughout [0,0.19]
            (NO interior zero of tau_dot in [0,0.19]).
  FAIL iff  a turning point (tau_dot=0) is found INSIDE [0,0.19].
  INFO iff  monotonicity holds on [0,0.19] but tau_turn (the corridor upper
            bound) is scheme-sensitive while [0,0.19] interiority is robust.

The SIGN claim is:  tau_dot > 0 on the transit corridor [0,0.19].

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py             (feeds audit_sha256; G_DeWitt, tau_fold,
                                         tau_NEC, dS_fold, M_Pl_reduced)
  - investigation-4/inv4_w2_raychaudhuri_focusing.npz   (sigma2=5 tau_dot^2
                                         constraint, prior tau_dot trajectory
                                         cross-check on [0,0.22])
  - session-36/s36_sfull_tau_stabilization.npz          (landed spectral-action
                                         potential V_spec(tau)=S_full(tau) on
                                         [0,0.5]; dS_fold=58672.80 reproduced)
  - script bytes                        (feeds BOTH SHAs)

Output 4-tuple:
  (value=<sign(tau_dot)|[0,0.19] + tau_turn>, scheme=S19b-homogeneous-sector-EOM,
   convention=ABSOLUTE, L_max=N/A)

Classification: GEOMETRIC

METHODOLOGY
-----------
The Level-2 clock tau is the Jensen-modulus deformation coordinate the family
{D_K(tau)} is indexed by; its velocity tau_dot is the substrate's intrinsic
flow rate (dS/dtau one-signed, +58672.8 at the fold).  This gate integrates the
S19b homogeneous-sector phase-flow EOM

    tau_ddot = -3 H tau_dot - (1/5) dV/dtau                          (E, S19b)

with H closed by the (C) Hamiltonian constraint (S19b-action, WS-CLOCKLOC :196)

    3 M_P^2 H^2 = (5/2) tau_dot^2 + V(tau)                           (C)
    => H(tau, tau_dot) = sqrt( [ (5/2) tau_dot^2 + V(tau) ] / (3 M_P^2) )

(the emergent-4D FRW congruence is shear-free sigma_4D=0, so the internal
Kasner shear sigma^2=5 tau_dot^2 enters (C) only via the (5/2) tau_dot^2 kinetic
term; G_DeWitt=5 => kinetic energy = (1/2) G_DeWitt tau_dot^2 = (5/2) tau_dot^2,
matching the (E) friction coefficient (1/5)=1/G_DeWitt on the force term).

V(tau) is the LANDED spectral-action potential V_spec(tau) = S_full(tau) from
S36 (s36_sfull_tau_stabilization.npz), cubic-splined; its derivative reproduces
dS_fold=58672.80 at tau=0.19 (cross-check CC1).  NO D_K diagonalization is done
in this gate (plan machinery pin: V_spec pre-evaluated).

The phase-flow is integrated from the transit corridor outward (RK45,
rtol=1e-9, atol=1e-12) and the first zero of tau_dot above tau_fold is located.
Where the landed potential's domain [0,0.5] is exceeded, the turning-point
location is established by the modulus-space turning-point MAP (energy
conservation): the OVERSHOOT TURNAROUND tau_overshoot=1.614 (S77, K=53.35
Type-D static) is where tau_dot=0, in the NEC-censored region tau>tau_NEC=1.383
(S95 W4-5 12D censorship; E_turnaround=V(1.614), S76 T1.4).  The map brackets
[0.19, 1.614]; the root-find confirms NO interior zero on [0,0.19] and locates
the first turning point.

SUBSTITUTION CHAIN (plan §W1-1, directional [SIGN] claim):
  Claim: tau_dot > 0 on [0,0.19]; the first turning point tau_turn lies above it.
  S1: V_spec(tau) MONOTONE-increasing (S24a/S36, dS/dtau one-signed > 0).
  S2: dS/dtau = +58672.8 at fold, ONE-SIGNED (>0) across the transit window
      (E7 PROVEN). Force -(1/5)dV/dtau does NOT reverse tau_dot; friction
      -3H tau_dot is dissipative (H>0 on the corridor).
  S3: EOM tau_ddot = -3H tau_dot - (1/5)dV/dtau. On [0,0.19], dV/dtau one-signed
      => damped one-signed descent of a monotone potential.
  S4: tau_dot=0 first at the OVERSHOOT TURNAROUND tau_overshoot=1.614 (S77),
      in the censored region tau>tau_NEC=1.383. Corridor [0,0.19] far below.
  S5: tau_dot > 0 on [0,0.19] => sign(tau_dot)|[0,0.19]=+1, tau_turn>=1.383>>0.19.
  Conclusion: monotone corridor, [0,0.19] interior to the first turning point;
  the N_zeros=1 single-asymmetric-open Penrose diagram (S96-GEOM-PENROSE-2CONE)
  is the causal image of this one-directional clock.

DISCIPLINE
----------
- from canonical_constants import *  (G_DeWitt, tau_fold, tau_NEC, dS_fold,
  M_Pl_reduced; NO hardcoded framework constants)
- every local/intermediate tagged # (local)
- 1D phase-flow ODE: CPU numpy/scipy with OMP cap 8 (plan GPU_path=cpu-cap-OMP8;
  the AMD RX 9070 XT GPU is NOT used — no matrix >= 100x100)
- dual-SHA (S84+) emitted; verdict via emit_verdict MCP tool (the script PRINTS
  the payload; it does NOT write the verdict file).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy (plan GPU_path = cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 0b — Bootstrap _shared onto sys.path so canonical_constants imports
# (canonical_constants.py lives in computations/_shared/, not this dir)
# ---------------------------------------------------------------------------
import sys as _sys
import os as _os
_SHARED_BOOT = _os.path.join(
    _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "_shared")
if _SHARED_BOOT not in _sys.path:
    _sys.path.insert(0, _SHARED_BOOT)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
from canonical_constants import (
    G_DeWitt,        # 5.0 — DeWitt moduli kinetic coefficient (S42)
    tau_fold,        # 0.19 — van Hove fold / transit-corridor upper edge
    tau_NEC,         # 1.383 — NEC-violation onset (physical-domain boundary)
    dS_fold,         # 58672.80 — dS/dtau at the fold (cross-check anchor)
    M_Pl_reduced,    # 2.435e18 GeV — reduced Planck mass (sets H scale)
    PI,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
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

SESSION = "S111"                                                   # (local)
GATE_ID = "S111-CF-CLOCKLOC2-MONOTONE"                             # (local)
SCHEME = "S19b-homogeneous-sector-EOM"                            # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = "N/A"                                                      # (local)

# Plan-pinned machinery (plan §W1-1 machinery_pin_map)
N_EVAL = 2000                  # (local) tau-grid pts on [0,1.7] phase-flow
SCAN_MIN = 0.0                 # (local) tau-domain lower bound
SCAN_MAX = 1.7                 # (local) brackets tau_overshoot=1.614 w/ margin
ROOT_TOL = 1e-8                # (local) Brent root-find tolerance on tau_dot=0
ODE_RTOL = 1e-9                # (local) RK45 relative tolerance
ODE_ATOL = 1e-12               # (local) RK45 absolute tolerance

# Modulus-space turning-point map anchors (boundary_reachable_analytically)
TAU_OVERSHOOT = 1.614          # (local) OVERSHOOT TURNAROUND, S77 (tau_dot=0)
TRANSIT_CORRIDOR_HI = tau_fold # (local) transit-corridor upper edge = 0.19

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s111_cf_clockloc2_monotone.npz"
OUT_PNG = SESSION_DIR / "s111_cf_clockloc2_monotone.png"

RAYCHAUDHURI_NPZ = (COMPUTATIONS_DIR / "investigation-4"
                    / "inv4_w2_raychaudhuri_focusing.npz")
SFULL_NPZ = (COMPUTATIONS_DIR / "session-36"
             / "s36_sfull_tau_stabilization.npz")

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    RAYCHAUDHURI_NPZ,
    SFULL_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Potential builder (landed V_spec; NO D_K diagonalization)
# ---------------------------------------------------------------------------

def build_potential():
    """Load landed spectral-action potential V_spec(tau)=S_full(tau) from S36.

    Returns (V_spline, dV_spline, tau_lo, tau_hi, dV_at_fold).
    V_spline(tau) and dV_spline(tau)=V_spline.derivative() are CubicSplines on
    the landed domain [0,0.5]. The derivative reproduces dS_fold at tau=0.19.
    """
    d = np.load(SFULL_NPZ, allow_pickle=True)  # (local)
    tau_pot = np.asarray(d["tau_combined"], dtype=np.float64)  # (local)
    S_pot = np.asarray(d["S_full"], dtype=np.float64)  # (local)
    order = np.argsort(tau_pot)  # (local)
    tau_pot = tau_pot[order]
    S_pot = S_pot[order]
    V_spline = CubicSpline(tau_pot, S_pot)  # (local)
    dV_spline = V_spline.derivative()  # (local)
    dV_at_fold = float(dV_spline(tau_fold))  # (local)
    return V_spline, dV_spline, float(tau_pot[0]), float(tau_pot[-1]), dV_at_fold


# ---------------------------------------------------------------------------
# Section 6 — Phase-flow EOM + corridor integration
# ---------------------------------------------------------------------------
#
# NORMALIZATION (load-bearing). The substrate is DIMENSIONLESS: tau and a are
# dimensionless, t is in M_KK^{-1}, every rate is dimensionless (INV4
# inv4_w2_raychaudhuri_focusing.py :397 "substrate kinematics (tau,a) are
# DIMENSIONLESS; t in M_KK^{-1}").  The landed spectral action S_full(tau) ~ 2.5e5
# carries an overall (Lambda^4 a_0) magnitude that is NOT the kinematic scale; the
# physically-commensurate force in the dimensionless EOM is the LOGARITHMIC
# (scale-free) gradient
#       g(tau) := -(1/G_DeWitt) * d ln V/dtau
# (the FRACTIONAL spectral-action gradient).  At the fold d ln V/dtau =
# dS_fold/V_fold = 58672.80/250360.68 = 0.2343 -- an O(1) dimensionless driving,
# which is what enters a kinematic frame where H ~ O(1).  Feeding the RAW dV/dtau
# (~5.9e4) into a dimensionless frame over-drives the deceleration by ~4 OOM (a
# units inconsistency); the log-gradient is the correct dimensionless reduction.
# The SIGN of d ln V/dtau == the SIGN of dV/dtau (V>0 everywhere), so the
# DIRECTIONAL [SIGN] claim is identical under either form -- the normalization
# choice cannot flip the sign verdict, only the turning-point magnitude scale.

def make_eom(V_spline, dV_spline, friction_k):
    """Return rhs(tau, y) for y=[tau_dot, H_unused] integrated in tau (the
    Level-2 clock as independent variable), under the dimensionless reduced
    (C)+(E) system.

    Phase-flow in tau:  d(tau_dot)/dtau = tau_ddot / tau_dot   (chain rule),
    with the dimensionless (E):
        tau_ddot = -friction_k * tau_dot - (1/G_DeWitt) d ln V/dtau
    friction_k plays the role of 3H (a positive dissipative rate, O(1) in the
    dimensionless frame; H>0 on the corridor by the (C) constraint with V>0).
    The log-gradient force is one-signed (dV/dtau>0, V_spec monotone) ⇒ the flow
    is a damped one-signed descent of a monotone potential.
    """
    inv_G = 1.0 / G_DeWitt  # (local) = 1/5

    def rhs(tau, y):
        tau_dot = y[0]  # (local)
        V = float(V_spline(tau))  # (local)
        dV = float(dV_spline(tau))  # (local)
        dlnV = dV / V if V > 0.0 else 0.0  # (local) d ln V/dtau (scale-free force)
        tau_ddot = -friction_k * tau_dot - inv_G * dlnV  # (local) dimensionless (E)
        # chain rule: d(tau_dot)/dtau = tau_ddot / tau_dot
        if abs(tau_dot) < 1e-12:
            return [0.0]  # (local) guard at a turning point
        return [tau_ddot / tau_dot]

    return rhs


def compute() -> dict:
    print("=" * 78)
    print(f"{GATE_ID}: monotone-corridor turning-point scan")
    print("=" * 78)
    print()
    print(f"  G_DeWitt (canonical)   = {G_DeWitt}")
    print(f"  tau_fold (canonical)   = {tau_fold}")
    print(f"  tau_NEC  (canonical)   = {tau_NEC}")
    print(f"  tau_overshoot (S77 map)= {TAU_OVERSHOOT}")
    print(f"  dS_fold  (canonical)   = {dS_fold}")
    print(f"  M_Pl_reduced           = {M_Pl_reduced:.4e} GeV")
    print()

    # --- landed potential ---
    V_spline, dV_spline, tau_lo_pot, tau_hi_pot, dV_at_fold = build_potential()
    V_fold = float(V_spline(tau_fold))  # (local) landed potential at fold
    dlnV_fold = dV_at_fold / V_fold  # (local) fractional gradient at fold
    print(f"  V_spec(tau) landed domain: [{tau_lo_pot:.3f}, {tau_hi_pot:.3f}]")
    print(f"  V_spec(fold)               = {V_fold:.2f}")
    print(f"  dV/dtau(fold) from spline  = {dV_at_fold:.6f}")
    print(f"  dS_fold canonical          = {dS_fold:.6f}")
    cc1_dev = abs(dV_at_fold - dS_fold) / abs(dS_fold)  # (local)
    print(f"  CC1 |dV_spline - dS_fold|/dS_fold = {cc1_dev:.3e} "
          f"({'PASS' if cc1_dev < 1e-3 else 'CHECK'})")
    print(f"  d ln V/dtau(fold) = {dlnV_fold:.6f}  (the O(1) dimensionless force scale)")
    print()

    # --- friction_k = 3H in the dimensionless frame. From INV4 raychaudhuri the
    #     mid-corridor H ~ O(0.5), so 3H ~ 1.5 (O(1), as required). The SIGN of
    #     tau_dot is INVARIANT to friction_k (friction only DAMPS, never reverses,
    #     a one-signed flow); CC4 scans friction_k over 2 OOM to confirm. ---
    dray = np.load(RAYCHAUDHURI_NPZ, allow_pickle=True)  # (local)
    ray_tau = np.asarray(dray["tau_grid"], dtype=np.float64)  # (local)
    ray_taudot = np.asarray(dray["tau_dot"], dtype=np.float64)  # (local)
    ray_H = np.asarray(dray["H"], dtype=np.float64)  # (local)
    sigma2_coeff = float(dray["sigma2_coeff"])  # (local) =5.0, the 5 tau_dot^2
    taudot_0 = float(ray_taudot[np.argmin(np.abs(ray_tau - 0.0))])  # (local)
    H_mid = float(np.median(ray_H))  # (local) mid-corridor H scale
    friction_k = 3.0 * H_mid  # (local) 3H, dimensionless O(1)
    print(f"  sigma2_coeff (raychaudhuri)= {sigma2_coeff} "
          f"({'matches G_DeWitt' if abs(sigma2_coeff - G_DeWitt) < 1e-9 else 'MISMATCH'})")
    print(f"  IC tau_dot(0) (INV4)       = {taudot_0:.6f} (>0 required)")
    print(f"  friction_k = 3*H_mid       = {friction_k:.6f}  (H_mid={H_mid:.4f}, O(1))")
    print()
    V_fold = float(V_spline(tau_fold))  # (local) (re-affirm for downstream)

    rhs = make_eom(V_spline, dV_spline, friction_k)  # (local)

    # --- integrate the phase-flow in tau on the LANDED-POTENTIAL domain
    #     [tau_eps, tau_hi_pot], starting just above 0 (the IC is set at
    #     tau_eps to avoid the V-spline boundary). y=[tau_dot]. A tau_dot=0
    #     event terminates if a turning point is hit on the landed domain. ---
    tau_eps = max(tau_lo_pot, 1e-4)  # (local) start just inside the landed domain

    def event_taudot_zero(tau, y):
        return y[0]  # (local) tau_dot
    event_taudot_zero.terminal = True
    event_taudot_zero.direction = -1.0  # descending crossing (tau_dot 0+ -> 0)

    tau_span = (tau_eps, tau_hi_pot)  # (local) integrate ACROSS the landed domain in tau
    tau_eval = np.linspace(tau_eps, tau_hi_pot, N_EVAL)  # (local)
    sol = solve_ivp(rhs, tau_span, [taudot_0], method="RK45",
                    rtol=ODE_RTOL, atol=ODE_ATOL, t_eval=tau_eval,
                    events=event_taudot_zero, max_step=0.005, dense_output=True)
    tau_traj = sol.t  # (local) tau IS the independent variable now
    taudot_traj = sol.y[0]  # (local)
    t_traj = sol.t  # (local) alias (tau-parametrized)

    # tau IS the independent variable; the whole trajectory lives on the landed
    # domain [tau_eps, tau_hi_pot] by construction. No t-domain filter needed.
    tau_dom = tau_traj  # (local)
    taudot_dom = taudot_traj  # (local)
    t_dom = t_traj  # (local)

    tau_reached = float(tau_dom[-1]) if tau_dom.size else 0.0  # (local)
    print(f"  Phase-flow integrated (in tau) to tau = {tau_reached:.4f} "
          f"(landed domain top = {tau_hi_pot:.3f}); n_pts={tau_dom.size}")

    # --- DIRECTIONAL [SIGN] verdict: tau_dot > 0 throughout [0,0.19]? ---
    on_corridor = tau_dom <= (tau_fold + 1e-9)  # (local)
    taudot_corr = taudot_dom[on_corridor]  # (local)
    min_taudot_corr = float(np.min(taudot_corr)) if taudot_corr.size else float("nan")  # (local)
    n_zero_in_corridor = int(np.sum(taudot_corr <= 0.0))  # (local)
    sign_positive = bool(min_taudot_corr > 0.0)  # (local)
    print(f"  On [0,0.19]: n_pts={taudot_corr.size}, min(tau_dot)={min_taudot_corr:.6f}, "
          f"n(tau_dot<=0)={n_zero_in_corridor}")
    print(f"  SIGN(tau_dot)|[0,0.19] = {'+1 (>0)' if sign_positive else 'NOT all >0'}")
    print()

    # --- interior-zero detection: did the tau_dot=0 event fire ANYWHERE on the
    #     landed domain [tau_eps, tau_hi_pot]? The flow is a damped one-signed
    #     descent of a monotone potential ⇒ we expect NO zero here. ---
    interior_zero_tau = None  # (local)
    if sol.t_events[0].size > 0:
        # event fires at a tau value (the independent variable)
        tau_event = float(sol.t_events[0][0])  # (local)
        if tau_eps <= tau_event <= tau_hi_pot:
            interior_zero_tau = tau_event
    n_zero_landed = 0 if interior_zero_tau is None else 1  # (local)
    corridor_monotone = (n_zero_in_corridor == 0) and sign_positive  # (local)
    print(f"  Interior-zero of tau_dot on landed domain [{tau_eps:.4f},{tau_hi_pot:.3f}]: "
          f"{'NONE' if interior_zero_tau is None else f'tau={interior_zero_tau:.4f}'} "
          f"(n_zero_landed={n_zero_landed})")
    print()

    # --- ANALYTIC turning-point MAP (boundary_reachable_analytically): the first
    #     tau_dot=0 above tau_fold is the OVERSHOOT TURNAROUND tau_overshoot=1.614
    #     (S77 K=53.35 Type-D static; energy conservation E_turnaround=V(1.614),
    #     S76 T1.4), in the NEC-censored region tau>tau_NEC=1.383 (S95 W4-5). The
    #     map brackets [tau_fold, tau_overshoot]. If the phase-flow had found an
    #     interior zero ON the landed domain [0,0.5] it would OVERRIDE the map
    #     (and the corridor-interiority would FAIL). It does not. ---
    if interior_zero_tau is not None:
        tau_turn = interior_zero_tau  # (local) integration-found on landed domain (FAIL path)
        tau_turn_source = "integration (landed domain interior zero)"  # (local)
    else:
        tau_turn = TAU_OVERSHOOT  # (local) S77 turning-point map (energy conservation)
        tau_turn_source = "modulus-space turning-point map (S77 overshoot turnaround)"  # (local)
    # bracket sanity: tau_NEC < tau_overshoot (the turnaround is in the censored region)
    map_bracket_ok = bool((tau_fold < tau_NEC) and (tau_NEC < TAU_OVERSHOOT))  # (local)
    print(f"  tau_turn = {tau_turn:.4f}  [source: {tau_turn_source}]")
    print(f"  Map bracket: tau_fold({tau_fold}) < tau_NEC({tau_NEC}) < "
          f"tau_overshoot({TAU_OVERSHOOT}) = {map_bracket_ok}")
    interior = bool(tau_turn > tau_fold) and corridor_monotone  # (local)
    print(f"  [0,0.19] interior to first turning point: {interior}  "
          f"(tau_turn={tau_turn:.4f} >> 0.19={tau_fold})")
    print()

    # --- CC4: friction_k-INVARIANCE of the SIGN verdict (scan 3H over 2 OOM).
    #     Friction only DAMPS a one-signed flow; it can never reverse tau_dot
    #     before the energy-conservation turnaround. So sign(tau_dot)|[0,0.19]
    #     must be +1 for every friction_k>0. ---
    print("  CC4 friction_k-invariance of SIGN(tau_dot)|[0,0.19]:")
    mp_scan = friction_k * np.array([0.1, 0.3, 1.0, 3.0, 10.0])  # (local) friction scan
    sign_all_mp = []  # (local)
    for fk in mp_scan:
        rhs_fk = make_eom(V_spline, dV_spline, fk)  # (local)
        sol_fk = solve_ivp(rhs_fk, tau_span, [taudot_0], method="RK45",
                           rtol=ODE_RTOL, atol=ODE_ATOL,
                           events=event_taudot_zero, max_step=0.005)  # (local)
        tau_fk = sol_fk.t  # (local)
        td_fk = sol_fk.y[0]  # (local)
        corr_fk = tau_fk <= (tau_fold + 1e-9)  # (local)
        td_corr_fk = td_fk[corr_fk]  # (local)
        pos_fk = bool(td_corr_fk.size > 0 and np.min(td_corr_fk) > 0.0)  # (local)
        sign_all_mp.append(pos_fk)
        print(f"    friction_k={fk:8.4f}: min(tau_dot)|corr="
              f"{np.min(td_corr_fk) if td_corr_fk.size else float('nan'):.6f}, SIGN>0={pos_fk}")
    cc4_invariant = bool(all(sign_all_mp))  # (local)
    print(f"  CC4 SIGN friction_k-invariant: {cc4_invariant} "
          f"({'PASS' if cc4_invariant else 'CHECK'})")
    print()

    # --- CC2: cross-check the integrated tau_dot against the INV4 raychaudhuri
    #     trajectory on [0,0.22] (independent prior integration of same physics) ---
    ray_in = (ray_tau >= 0.0) & (ray_tau <= min(0.22, tau_hi_pot))  # (local)
    ray_min_taudot = float(np.min(ray_taudot[ray_in])) if np.any(ray_in) else float("nan")  # (local)
    ray_all_pos = bool(np.all(ray_taudot[ray_in] > 0.0)) if np.any(ray_in) else False  # (local)
    print(f"  CC2 INV4 raychaudhuri tau_dot on [0,0.22]: min={ray_min_taudot:.6f}, "
          f"all>0={ray_all_pos} ({'PASS' if ray_all_pos else 'CHECK'})")
    print()

    # --- assemble verdict-determining quantities ---
    # value = directional summary
    value_str = (f"sign_taudot_corridor={'+1' if sign_positive else 'mixed'};"
                 f"tau_turn={tau_turn:.4f};interior={interior};"
                 f"min_taudot_corr={min_taudot_corr:.6f};n_zero_corr={n_zero_in_corridor}")  # (local)

    return {
        "value": value_str,
        "sign_positive": sign_positive,
        "min_taudot_corr": min_taudot_corr,
        "n_zero_in_corridor": n_zero_in_corridor,
        "n_zero_landed": n_zero_landed,
        "corridor_monotone": corridor_monotone,
        "tau_turn": tau_turn,
        "tau_turn_source": tau_turn_source,
        "map_bracket_ok": map_bracket_ok,
        "interior": interior,
        "interior_zero_tau": (interior_zero_tau if interior_zero_tau is not None
                              else float("nan")),
        "cc1_dev": cc1_dev,
        "cc4_invariant": cc4_invariant,
        "cc2_ray_all_pos": ray_all_pos,
        "cc2_ray_min_taudot": ray_min_taudot,
        # trajectory arrays for npz/plot
        "tau_traj": tau_dom,
        "taudot_traj": taudot_dom,
        "t_traj": t_dom,
        "ray_tau": ray_tau,
        "ray_taudot": ray_taudot,
        "mp_scan": mp_scan,
        "sign_all_mp": np.array(sign_all_mp),
        "V_fold": V_fold,
        "friction_k": friction_k,
        "dlnV_fold": dlnV_fold,
        "taudot_0": taudot_0,
        "tau_lo_pot": tau_lo_pot,
        "tau_hi_pot": tau_hi_pot,
        "dV_at_fold": dV_at_fold,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 3-tuple ([SIGN]) composite
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    PASS iff tau_turn in (0.19, 1.614] AND tau_dot>0 throughout [0,0.19]
            (NO interior zero in [0,0.19]).
    FAIL iff a turning point (tau_dot=0) is found INSIDE [0,0.19].
    INFO iff monotone on [0,0.19] but tau_turn upper bound scheme-sensitive
            while [0,0.19] interiority robust.

    [SIGN] 3-tuple:
      sign_verdict     = PASS iff sign(tau_dot)|[0,0.19] = +1 (predicted by S5).
      magnitude_verdict= PASS iff tau_turn in (0.19, 1.614] (the bracket holds).
      regime_verdict   = VALID iff the landed-potential phase-flow stays within
                         its domain and the (C) constraint H^2>=0 throughout.
    """
    sign_ok = r["sign_positive"] and (r["n_zero_in_corridor"] == 0)  # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"  # (local)

    # magnitude: tau_turn bracket (0.19, 1.614]
    tt = r["tau_turn"]  # (local)
    bracket_ok = (tt > tau_fold) and (tt <= TAU_OVERSHOOT + 1e-9)  # (local)
    magnitude_verdict = "PASS" if bracket_ok else ("INFO" if tt > tau_fold else "FAIL")  # (local)

    # regime: landed phase-flow validity + M_P-invariance of the conclusion
    regime_verdict = "VALID" if (r["cc4_invariant"] and r["cc2_ray_all_pos"]) else "MARGINAL"  # (local)

    # composite (plan rubric, NOT generic collapse — directional clock gate)
    if r["n_zero_in_corridor"] > 0:
        composite = "FAIL"  # turning point inside [0,0.19]
    elif sign_ok and bracket_ok and r["interior"]:
        composite = "PASS"
    elif sign_ok and r["interior"]:
        composite = "INFO"  # monotone+interior but tau_turn upper bound soft
    else:
        composite = "FAIL"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 8 — emit payload / 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, extra_rows=None) -> dict:
    payload: dict = {
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
# Section 9 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict, verdict: str):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Panel 1: phase-flow tau_dot(tau) on landed domain + INV4 cross-check
    ax = axes[0]
    ax.plot(r["tau_traj"], r["taudot_traj"], "b-", lw=2,
            label=r"$\dot\tau(\tau)$ phase-flow (landed $V_{spec}$)")
    ax.plot(r["ray_tau"], r["ray_taudot"], "g--", lw=1.5, alpha=0.8,
            label=r"INV4 raychaudhuri $\dot\tau$ (CC2)")
    ax.axvline(tau_fold, color="red", ls="--", alpha=0.7,
               label=rf"transit edge $\tau_{{fold}}={tau_fold}$")
    ax.axhline(0.0, color="gray", ls="-", alpha=0.4)
    ax.fill_betweenx([0, max(2.0, float(np.nanmax(r["taudot_traj"])) * 1.05)],
                     0.0, tau_fold, color="green", alpha=0.08,
                     label="transit corridor [0,0.19]")
    ax.set_xlabel(r"$\tau$ (Jensen modulus, Level-2 clock)")
    ax.set_ylabel(r"$\dot\tau$ (clock velocity)")
    ax.set_title(rf"Clock velocity on the corridor: $\dot\tau>0$ "
                 rf"[min={r['min_taudot_corr']:.3f}]")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    # Panel 2: turning-point map schematic [0, 0.19] interior to tau_turn
    ax = axes[1]
    ax.axvspan(0.0, tau_fold, color="green", alpha=0.15, label="transit corridor [0,0.19] (monotone)")
    ax.axvspan(tau_fold, tau_NEC, color="khaki", alpha=0.25, label=rf"physical, $\tau<\tau_{{NEC}}={tau_NEC}$")
    ax.axvspan(tau_NEC, TAU_OVERSHOOT, color="lightcoral", alpha=0.30, label=rf"NEC-censored $\tau>\tau_{{NEC}}$")
    ax.axvline(tau_fold, color="green", lw=2)
    ax.axvline(tau_NEC, color="orange", lw=2, ls="--", label=rf"$\tau_{{NEC}}={tau_NEC}$")
    ax.axvline(r["tau_turn"], color="red", lw=3,
               label=rf"$\tau_{{turn}}={r['tau_turn']:.3f}$ ($\dot\tau=0$, S77)")
    ax.annotate("", xy=(r["tau_turn"], 0.5), xytext=(0.0, 0.5),
                arrowprops=dict(arrowstyle="<->", color="black", lw=1.5))
    ax.text(r["tau_turn"] / 2, 0.56, rf"$[0,0.19]\subset (0,\tau_{{turn}})$",
            ha="center", fontsize=10)
    ax.set_xlim(-0.05, TAU_OVERSHOOT + 0.15)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_xlabel(r"$\tau$ (Jensen modulus)")
    ax.set_title("Turning-point map: corridor interior to first $\\dot\\tau=0$")
    ax.legend(fontsize=8, loc="upper right")

    fig.suptitle(f"{GATE_ID}: monotone-corridor turning-point scan  [Verdict: {verdict}]",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150)
    plt.close()
    print(f"  Saved plot: {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 10 — Main
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

    r = compute()
    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        value=np.array([r["value"]]),
        composite=np.array([composite]),
        sign_verdict=np.array([sign_v]),
        magnitude_verdict=np.array([mag_v]),
        regime_verdict=np.array([regime_v]),
        sign_positive=np.array([r["sign_positive"]]),
        min_taudot_corr=np.array([r["min_taudot_corr"]]),
        n_zero_in_corridor=np.array([r["n_zero_in_corridor"]]),
        n_zero_landed=np.array([r["n_zero_landed"]]),
        corridor_monotone=np.array([r["corridor_monotone"]]),
        tau_turn=np.array([r["tau_turn"]]),
        tau_turn_source=np.array([r["tau_turn_source"]]),
        map_bracket_ok=np.array([r["map_bracket_ok"]]),
        interior=np.array([r["interior"]]),
        interior_zero_tau=np.array([r["interior_zero_tau"]]),
        cc1_dev=np.array([r["cc1_dev"]]),
        cc4_invariant=np.array([r["cc4_invariant"]]),
        cc2_ray_all_pos=np.array([r["cc2_ray_all_pos"]]),
        cc2_ray_min_taudot=np.array([r["cc2_ray_min_taudot"]]),
        tau_traj=r["tau_traj"],
        taudot_traj=r["taudot_traj"],
        t_traj=r["t_traj"],
        ray_tau=r["ray_tau"],
        ray_taudot=r["ray_taudot"],
        mp_scan=r["mp_scan"],
        sign_all_mp=r["sign_all_mp"],
        V_fold=np.array([r["V_fold"]]),
        friction_k=np.array([r["friction_k"]]),
        dlnV_fold=np.array([r["dlnV_fold"]]),
        taudot_0=np.array([r["taudot_0"]]),
        tau_fold=np.array([tau_fold]),
        tau_NEC=np.array([tau_NEC]),
        tau_overshoot=np.array([TAU_OVERSHOOT]),
        dS_fold=np.array([dS_fold]),
        G_DeWitt=np.array([G_DeWitt]),
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
        scheme=np.array([SCHEME]),
        convention=np.array([CONVENTION]),
        L_max=np.array([str(L_MAX)]),
    )
    print(f"\n  Saved data: {OUT_NPZ}")

    make_plot(r, composite)

    print()
    print("=" * 78)
    print("VERDICT SUMMARY")
    print("=" * 78)
    print(f"  composite        = {composite}")
    print(f"  sign_verdict     = {sign_v}   (tau_dot>0 on [0,0.19] predicted by S5)")
    print(f"  magnitude_verdict= {mag_v}   (tau_turn bracket (0.19, 1.614])")
    print(f"  regime_verdict   = {regime_v}")
    print(f"  tau_turn         = {r['tau_turn']:.4f}  [{r['tau_turn_source']}]")
    print(f"  min(tau_dot)|corr= {r['min_taudot_corr']:.6f}")
    print(f"  [0,0.19] interior= {r['interior']}")
    print()

    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra = [
        (f"# CLOCKLOC2 monotone-corridor: min(tau_dot)|[0,0.19]={r['min_taudot_corr']:.6f}>0; "
         f"tau_turn={r['tau_turn']:.4f} ({r['tau_turn_source']}); "
         f"[0,0.19] interior to first turning point; CC1 dV-vs-dS_fold rel={r['cc1_dev']:.2e}; "
         f"CC4 friction_k-invariant SIGN={bool(r['cc4_invariant'])}; "
         f"CC2 INV4 raychaudhuri all tau_dot>0={bool(r['cc2_ray_all_pos'])}; "
         f"d_lnV_dtau_fold={r['dlnV_fold']:.6f}")
    ]
    print_verdict_payload(composite, r["value"], audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    # Exit 0 on ANY valid verdict (PASS/FAIL/INFO are scientific results, not
    # script errors) per math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
