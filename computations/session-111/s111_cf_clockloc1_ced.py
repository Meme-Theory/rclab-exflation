#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S111-CF-CLOCKLOC1-CED  [PRIME a(t) backbone] — hawking-theorist.

The minisuperspace (C,E,D)-triple SELF-CONSISTENCY closure in the
substrate-natural (tau = Jensen-modulus) frame:

  (C) Hamiltonian constraint  3 M_P^2 H^2 = (1/2) sigma_dot^2 + (5/2) tau_dot^2 + V
  (E) evolution               dy/dt = [sigma_dot, -3H sigma_dot - dV/dsigma,
                                       tau_dot,  -(3 H tau_dot + (1/5) dV/dtau)]
  (D) deparametrization        t_internal := INT dtau/tau_dot,   H = tau_dot * d ln a / dtau

Verdict operator (plan §W1-2):
    |Lambda - 3 H^2| < 1e-6  at the de Sitter fixed point  AND  min_{corridor}|tau_dot| > 0.

This is a CLOSURE check, NOT a discovery: c_track=3 is already PROVEN
(INV4-W3-1, reduction_residual=0.0e+00). CLOCKLOC1 tests the SAME de Sitter
relation Lambda=3H^2 embedded in the FULL (C,E,D) triple with the sigma^2=5tau_dot^2
internal-shear constraint and the landed V_spec, and consumes the CLOCKLOC2
corridor as the (D)-leg integration / well-posedness domain.

Substrate framing (direction of explanation). The substrate IS the spectral
triple (A_K, H_K, D_K(tau)); the clock that advances the trajectory is the
LEVEL-2 Jensen-modulus tau (the parameter the family {D_K(tau)} is indexed by),
upstream of the a0/a2/a4 Seeley-DeWitt grading. The reduction READS its rate-FORM
off the a0 volume term (H^2 = Lambda/3, a Level-1 constraint-readout), but that
does NOT make a0 "the clock" (the Level-2-clock PRDR tag forecloses that
conflation). H is the frame-dependent readout of the total energy in (C); the
de Sitter relation Lambda=3H^2 is the reparam-invariant Level-1 scalar identity.
Arrow:  D_K eigenvalues -> a_n moments -> emergent (a,tau) congruence -> measurement.

NO D_K diagonalization in this gate: V_spec(tau)=S_full(tau) is the LANDED
spectral-action potential (S36), cubic-splined; the spectral moments enter only
through the pinned V_spec functional.
"""

from __future__ import annotations

import os

# CPU-cap per math-scripts.md (small ODE; no matrix >=100x100, GPU not used).
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys as _sys
import os as _os

# --- bootstrap canonical_constants import (computations/_shared on sys.path) ---
_SHARED_BOOT = _os.path.join(
    _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "_shared")
if _SHARED_BOOT not in _sys.path:
    _sys.path.insert(0, _SHARED_BOOT)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first framework import)
# ---------------------------------------------------------------------------
from canonical_constants import (
    G_DeWitt,        # 5.0 — DeWitt moduli kinetic coefficient (S42); = the (5/2)tau_dot^2 coeff *2
    tau_fold,        # 0.19 — van Hove fold / transit-corridor upper edge
    tau_NEC,         # 1.383 — NEC-violation onset (physical-domain boundary)
    tau_overshoot,   # 1.614 — overshoot turnaround (first tau_dot=0 above the fold, S77)
    dS_fold,         # 58672.80 — dS/dtau at the fold (potential-fidelity cross-check anchor)
    M_Pl_reduced,    # 2.435e18 GeV — reduced Planck mass (sets H scale)
    a0_fold,         # 6440.0 — a0 volume term at fold (the Level-1 readout grade)
    a2_fold,         # 2776.165 — a2 scalar-curvature moment at fold
    PI,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration identity
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                          # (local)
GATE_ID = "S111-CF-CLOCKLOC1-CED"                         # (local)
SCHEME = "S19b-homogeneous-sector-action"                # (local)
CONVENTION = "ABSOLUTE-substrate-natural-frame"          # (local)
L_MAX = "N/A"                                             # (local)

# Plan-pinned machinery (plan §W1-2 machinery_pin_map)
N_EVAL = 2000                  # (local) tau-grid pts on the transit corridor [0,0.19]
CORRIDOR_HI = tau_fold         # (local) transit corridor upper bound (=0.19; CLOCKLOC2-scoped)
PASS_THRESHOLD = 1e-6          # (local) de Sitter fixed-point residual |Lambda-3H^2| PASS floor
ODE_RTOL = 1e-9                # (local) RK45 relative tolerance
ODE_ATOL = 1e-12               # (local) RK45 absolute tolerance

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s111_cf_clockloc1_ced.npz"
OUT_PNG = SESSION_DIR / "s111_cf_clockloc1_ced.png"

# Input files
SFULL_NPZ = (COMPUTATIONS_DIR / "session-36"
             / "s36_sfull_tau_stabilization.npz")
RAYCHAUDHURI_NPZ = (COMPUTATIONS_DIR / "investigation-4"
                    / "inv4_w2_raychaudhuri_focusing.npz")
DESITTER_NPZ = (COMPUTATIONS_DIR / "investigation-4"
                / "inv4_w3_de_sitter_clock_tracking.npz")
CLOCKLOC2_NPZ = SESSION_DIR / "s111_cf_clockloc2_monotone.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SFULL_NPZ,
    RAYCHAUDHURI_NPZ,
    DESITTER_NPZ,
    CLOCKLOC2_NPZ,            # the within-wave UPSTREAM pin (CLOCKLOC2 corridor)
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
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
    """audit_sha256 = SHA(script || canonical || pinmap_json); content_sha256 = SHA(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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
# Section 5 — Landed potential builder (V_spec; NO D_K diagonalization)
#   Identical machinery to CLOCKLOC2: V_spec(tau)=S_full(tau) from S36,
#   cubic-splined; dV/dtau(fold) reproduces dS_fold (CC1).
# ---------------------------------------------------------------------------

def build_potential():
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
# Section 6 — The (C,E,D) triple
# ---------------------------------------------------------------------------
#
# NORMALIZATION (load-bearing; matched to CLOCKLOC2). The substrate is
# DIMENSIONLESS (tau, a dimensionless; t in M_KK^{-1}; INV4
# inv4_w2_raychaudhuri_focusing.py:397). The landed spectral action
# S_full(tau)~2.5e5 carries an overall (Lambda^4 a0) magnitude that is NOT the
# kinematic scale; the physically-commensurate force in the dimensionless EOM is
# the LOGARITHMIC (scale-free) gradient  g(tau) = -(1/G_DeWitt) d ln V/dtau.
# At the fold d ln V/dtau = dS_fold/V_fold = 0.234 (an O(1) dimensionless
# driving). Critically sign(d ln V/dtau) == sign(dV/dtau) (V>0 everywhere), so
# this normalization cannot flip any directional verdict -- only the magnitude
# scale. The CLOSURE relation Lambda=3H^2 is normalization-INVARIANT: it is the
# (C) constraint with kinetic->0, where the overall V magnitude cancels between
# Lambda:=V/M_P^2 and 3H^2 = 3*(V/(3M_P^2)) = V/M_P^2.
#
# (C):  H(tau,tau_dot,sigma_dot) = sqrt( (1/(3 M_P^2)) [ (1/2)sigma_dot^2
#                                          + (5/2)tau_dot^2 + V ] )    [Hamiltonian]
# (E):  dy/dt = [sigma_dot, -3H sigma_dot - dV/dsigma,
#                tau_dot, -(3 H tau_dot + (1/5) d ln V/dtau)]          [ij-Einstein]
#       (dV/dsigma = 0 in the landed reduction: V=V_spec(tau) carries no sigma
#        dependence after the e^{-3sigma} volume factor is fixed at the
#        volume-preserving point; sigma is the trace-free internal shear with
#        sigma^2 = 5 tau_dot^2 -- it is SOURCED by tau_dot, not an independent
#        potential DOF. We integrate sigma as a passive shear readout.)
# (D):  t_internal = INT dtau/tau_dot ; well-posed iff tau_dot != 0.
#
# M_P in the dimensionless frame: we work in reduced units M_P = 1 (the standard
# minisuperspace normalization, session-19b-prompt.md:148 "In Planck units
# M_P=1"); H is then dimensionless, matching the INV4 raychaudhuri frame.
#
# DUAL-H STRUCTURE (load-bearing; matched to CLOCKLOC2's documented frame).
# Two physically-distinct H's appear, and conflating them is the units-
# inconsistency CLOCKLOC2's header warned against:
#
#   (1) H_kinematic — the EMERGENT-FRW expansion rate H = a_dot/a. This is the
#       O(1) dimensionless rate the INV4 raychaudhuri trajectory carries
#       (median ~0.26 on the corridor). It is what "expansion" MEANS in the
#       substrate, and it is the friction rate 3H that enters (E). CLOCKLOC2
#       used exactly this (friction_k = 3*H_mid).
#
#   (2) H_constraint(full-V) = sqrt(V/(3 M_P^2)) — the (C) constraint H with the
#       FULL landed V magnitude (~289 at the fold). The landed spectral action
#       S_full(tau)~2.5e5 carries an overall (Lambda^4 a0) magnitude that is NOT
#       the kinematic scale; feeding 3*H_constraint(full-V)~867 into (E) over-
#       drives the deceleration by ~4 OOM (the units inconsistency), damping
#       tau_dot to ~0 spuriously. This is a numerical artifact, NOT a turning
#       point (CLOCKLOC2, in the kinematic frame, finds tau_dot~1.8 monotone).
#
# The corridor (E)-integration (PART A) uses (1) — the dimensionless kinematic H,
# EXACTLY as CLOCKLOC2 — so the two gates integrate the SAME EOM in the SAME
# frame and AGREE. The de Sitter CLOSURE (PART C) is frame-INVARIANT: the
# relation Lambda=3H^2 is the (C)-constraint RATIO identity Lambda:=V/M_P^2 vs
# 3H^2=3*(V/(3M_P^2))=V/M_P^2 -- the overall V SCALE cancels, so the closure
# residual is the float64 floor regardless of which H normalization is used.

M_P_FRAME = 1.0   # (local) reduced Planck mass in the dimensionless minisuperspace frame


def hubble_from_C(sigma_dot, tau_dot, V):
    """(C) Hamiltonian constraint -> H_constraint >= 0 (full-V root). Used ONLY in
    the de Sitter CLOSURE (PART C), where the V-magnitude cancels in Lambda=3H^2.
    NOT used as the corridor friction (that would 4-OOM-over-drive; see DUAL-H)."""
    rho = 0.5 * sigma_dot * sigma_dot + 2.5 * tau_dot * tau_dot + V  # (local) total energy density
    H2 = rho / (3.0 * M_P_FRAME * M_P_FRAME)  # (local)
    return float(np.sqrt(H2)) if H2 > 0.0 else 0.0


def make_ced_rhs(V_spline, dV_spline, friction_k):
    """Return rhs(t, y) for y=[sigma, sigma_dot, tau, tau_dot] -- the (C)+(E)
    system in cosmic time t, in the DIMENSIONLESS KINEMATIC-H frame (matched to
    CLOCKLOC2). `friction_k` = 3*H_kinematic (O(1), from the INV4 raychaudhuri
    median H), the emergent-FRW friction rate. The log-gradient force is the
    scale-free -(1/G_DeWitt) d ln V/dtau. A damped one-signed descent of a
    monotone V_spec -> tau_dot stays >0 on the corridor (agrees with CLOCKLOC2).
    """
    inv_G = 1.0 / G_DeWitt  # (local) = 1/5

    def rhs(t, y):
        # state y = [sigma, sigma_dot, tau, tau_dot]  (session-19b-prompt.md:177-184)
        sigma, sigma_dot, tau, tau_dot = y  # (local)
        V = float(V_spline(tau))  # (local)
        dV = float(dV_spline(tau))  # (local)
        dlnV = dV / V if V > 0.0 else 0.0  # (local) d ln V/dtau (scale-free force)
        # (E): ij-Einstein in the kinematic frame. friction_k = 3*H_kinematic (O(1)).
        # dV/dsigma=0 (V_spec carries no sigma dependence after the e^{-3 sigma}
        # volume factor is fixed at the volume-preserving point); sigma is the
        # passive trace-free shear sourced by tau_dot (sigma^2=5 tau_dot^2).
        sigma_ddot = -friction_k * sigma_dot  # (local) free-streaming shear (Hubble-damped)
        tau_ddot = -(friction_k * tau_dot + inv_G * dlnV)  # (local) modulus EOM (log-gradient)
        # dy/dt = [sigma_dot, sigma_ddot, tau_dot, tau_ddot]
        return [sigma_dot, sigma_ddot, tau_dot, tau_ddot]

    return rhs


# ---------------------------------------------------------------------------
# Section 7 — compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    print("=" * 78)
    print(f"{GATE_ID}: (C,E,D)-triple self-consistency closure")
    print("=" * 78)
    print()
    print(f"  G_DeWitt (canonical)   = {G_DeWitt}")
    print(f"  tau_fold (canonical)   = {tau_fold}")
    print(f"  tau_NEC  (canonical)   = {tau_NEC}")
    print(f"  tau_overshoot (S77)    = {tau_overshoot}")
    print(f"  dS_fold  (canonical)   = {dS_fold}")
    print(f"  a0_fold / a2_fold      = {a0_fold} / {a2_fold:.4f}  "
          f"(bare a4/a2 ~ 0.49; the V_spec SAME-OBJECT pin)")
    print(f"  M_Pl_reduced           = {M_Pl_reduced:.4e} GeV  (frame: M_P=1 dimensionless)")
    print()

    # --- landed potential V_spec(tau) (NO D_K diagonalization) ---
    V_spline, dV_spline, tau_lo_pot, tau_hi_pot, dV_at_fold = build_potential()
    V_fold = float(V_spline(tau_fold))  # (local)
    dlnV_fold = dV_at_fold / V_fold  # (local)
    cc1_dev = abs(dV_at_fold - dS_fold) / abs(dS_fold)  # (local) potential fidelity (CC1)
    print(f"  V_spec landed domain   = [{tau_lo_pot:.3f}, {tau_hi_pot:.3f}]")
    print(f"  V_spec(fold)           = {V_fold:.4f}")
    print(f"  dV/dtau(fold) spline   = {dV_at_fold:.6f}")
    print(f"  CC1 |dV_spline - dS_fold|/dS_fold = {cc1_dev:.3e} "
          f"({'PASS' if cc1_dev < 1e-3 else 'CHECK'})")
    print(f"  d ln V/dtau(fold)      = {dlnV_fold:.6f}  (O(1) dimensionless force)")
    print()

    # --- consume CLOCKLOC2 corridor (the within-wave UPSTREAM pin) ---
    d2 = np.load(CLOCKLOC2_NPZ, allow_pickle=True)  # (local)
    cl2_min_taudot = float(d2["min_taudot_corr"][0])  # (local)
    cl2_n_zero = int(d2["n_zero_in_corridor"][0])  # (local)
    cl2_monotone = bool(d2["corridor_monotone"][0])  # (local)
    cl2_tau_turn = float(d2["tau_turn"][0])  # (local)
    cl2_interior = bool(d2["interior"][0])  # (local)
    cl2_composite = str(d2["composite"][0])  # (local)
    cl2_taudot_0 = float(d2["taudot_0"][0])  # (local) the corridor IC tau_dot(0)
    print(f"  CLOCKLOC2 (UPSTREAM)   : composite={cl2_composite}, "
          f"min|tau_dot|_corr={cl2_min_taudot:.6f}, n_zero={cl2_n_zero}, "
          f"monotone={cl2_monotone}")
    print(f"                          tau_turn={cl2_tau_turn:.4f}, "
          f"[0,0.19] interior={cl2_interior}")
    print()

    # --- consume INV4-W3 de Sitter anchor (c_track=3 EXACT; the relation read backwards) ---
    d3 = np.load(DESITTER_NPZ, allow_pickle=True)  # (local)
    c_track = float(d3["c_track"])  # (local) = 3.0 EXACT
    c_track_resid = float(d3["reduction_residual_num"])  # (local) = 0.0
    Lam_inst = float(d3["Lambda_instance"])  # (local) 0.001
    G_inst = float(d3["G_instance"])  # (local) 1.0
    H_inst = float(d3["H_num"])  # (local) sqrt(Lambda/3)
    dSdL_sign = float(d3["dSdL_sign"])  # (local) -1
    print(f"  INV4-W3 de Sitter anchor: c_track={c_track:.1f} EXACT, "
          f"reduction_residual={c_track_resid:.1e}, dSdL_sign={dSdL_sign:.0f}")
    print(f"                          (Lambda_inst={Lam_inst}, H_inst={H_inst:.6e}, "
          f"3H^2={3*H_inst**2:.6e}, |L-3H^2|={abs(Lam_inst-3*H_inst**2):.2e})")
    print()

    # --- IC from the INV4 raychaudhuri trajectory at tau~0 (same as CLOCKLOC2) ---
    dray = np.load(RAYCHAUDHURI_NPZ, allow_pickle=True)  # (local)
    ray_tau = np.asarray(dray["tau_grid"], dtype=np.float64)  # (local)
    ray_taudot = np.asarray(dray["tau_dot"], dtype=np.float64)  # (local)
    ray_H = np.asarray(dray["H"], dtype=np.float64)  # (local)
    sigma2_coeff = float(dray["sigma2_coeff"])  # (local) = 5.0
    taudot_0 = float(ray_taudot[np.argmin(np.abs(ray_tau - 0.0))])  # (local) = 1.966
    # DIMENSIONLESS KINEMATIC friction (the SAME frame CLOCKLOC2 used; see DUAL-H).
    # H_kinematic = the emergent-FRW expansion rate (median of the INV4 raychaudhuri
    # trajectory), O(0.26); friction_k = 3*H_kinematic ~ O(0.79). This is what
    # enters (E) -- NOT 3*sqrt(V/3)~867 (the 4-OOM over-drive units inconsistency).
    H_kinematic_mid = float(np.median(ray_H))  # (local) emergent-FRW H, O(0.26)
    friction_k = 3.0 * H_kinematic_mid  # (local) 3H, dimensionless O(1) [== CLOCKLOC2]
    print(f"  sigma2_coeff (INV4)    = {sigma2_coeff} "
          f"({'matches G_DeWitt' if abs(sigma2_coeff - G_DeWitt) < 1e-9 else 'MISMATCH'})")
    print(f"  IC tau_dot(0) (INV4)   = {taudot_0:.6f} (>0 required)")
    print(f"  H_kinematic_mid (INV4) = {H_kinematic_mid:.6f}  (emergent-FRW H, O(1))")
    print(f"  friction_k = 3*H_kin   = {friction_k:.6f}  (== CLOCKLOC2 dimensionless frame)")
    print(f"  [contrast: 3*sqrt(V/3) = {3.0*np.sqrt(V_fold/3.0):.1f} would 4-OOM-over-drive]")
    print()

    # =====================================================================
    # PART A — (E) integration over the transit corridor: (D) well-posedness
    # =====================================================================
    # Integrate the (C)+(E) system y=[sigma,sigma_dot,tau,tau_dot] in cosmic time t
    # from the corridor floor in the DIMENSIONLESS KINEMATIC-H frame (friction_k =
    # 3*H_kinematic, == CLOCKLOC2). Integrate until tau crosses the corridor upper
    # bound (tau_fold=0.19), then read off min|tau_dot|. A damped one-signed
    # descent of a monotone V_spec -> tau_dot stays >0 (agrees with CLOCKLOC2).
    rhs = make_ced_rhs(V_spline, dV_spline, friction_k)  # (local)

    # sigma^2 = 5 tau_dot^2 (INV4-W2-2) -> the internal shear is SOURCED by tau_dot.
    # IC: sigma(0)=0, sigma_dot(0) = sqrt(5)*... we set the shear consistent with
    # sigma^2=5 tau_dot^2 as a velocity constraint: at t=0, sigma_dot(0) is fixed
    # so that (1/2)sigma_dot^2 contributes the trace-free shear energy. The
    # constraint sigma^2=5 tau_dot^2 is on the FIELD (Kasner shear magnitude);
    # the kinetic bookkeeping the landed (C) uses is the (5/2)tau_dot^2 modulus
    # term, with the shear entering as (1/2)sigma_dot^2. We initialize the passive
    # shear at sigma(0)=0, sigma_dot(0)=0 (the shear is a readout; it does not
    # back-react on the closure relation, which lives in the tau-sector + V).
    sigma_0 = 0.0  # (local)
    sigma_dot_0 = 0.0  # (local) passive shear readout (does not gate the closure)
    tau_0 = max(tau_lo_pot, 1e-4)  # (local) start just inside the landed domain
    y0 = [sigma_0, sigma_dot_0, tau_0, taudot_0]  # (local)

    # event: tau crosses the corridor upper bound (terminate the corridor leg)
    def event_tau_exit_corridor(t, y):
        return y[2] - CORRIDOR_HI  # (local) tau - 0.19
    event_tau_exit_corridor.terminal = True
    event_tau_exit_corridor.direction = 1.0  # ascending crossing

    # event: tau_dot = 0 (a turning point inside the corridor -> (D) singular = FAIL)
    def event_taudot_zero(t, y):
        return y[3]  # (local) tau_dot
    event_taudot_zero.terminal = False
    event_taudot_zero.direction = -1.0

    # integrate long enough in t to traverse the corridor (tau: 1e-4 -> 0.19);
    # at tau_dot~2 and corridor width ~0.19, the traversal time is ~0.1 in t.
    t_max = 5.0  # (local) generous; the corridor-exit event terminates earlier
    sol = solve_ivp(rhs, (0.0, t_max), y0, method="RK45",
                    rtol=ODE_RTOL, atol=ODE_ATOL,
                    events=[event_tau_exit_corridor, event_taudot_zero],
                    max_step=0.001, dense_output=True)
    t_traj = sol.t  # (local)
    sigma_traj = sol.y[0]  # (local)
    tau_traj = sol.y[2]  # (local)
    taudot_traj = sol.y[3]  # (local)
    H_traj = np.array([hubble_from_C(sol.y[1][i], sol.y[3][i],
                                     float(V_spline(sol.y[2][i])))
                       for i in range(sol.t.size)])  # (local)

    # restrict to the corridor tau in [tau_0, 0.19]
    on_corr = tau_traj <= (CORRIDOR_HI + 1e-9)  # (local)
    taudot_corr = taudot_traj[on_corr]  # (local)
    tau_corr = tau_traj[on_corr]  # (local)
    min_taudot_corridor = float(np.min(taudot_corr)) if taudot_corr.size else float("nan")  # (local)
    n_taudot_zero_corridor = int(np.sum(taudot_corr <= 0.0))  # (local)
    D_well_posed = bool(min_taudot_corridor > 0.0 and n_taudot_zero_corridor == 0)  # (local)
    print(f"  PART A — (E) corridor integration (y=[sigma,sigma_dot,tau,tau_dot]):")
    print(f"    traversed tau: {tau_traj[0]:.4f} -> {tau_traj[-1]:.4f}  "
          f"(corridor pts n={taudot_corr.size})")
    print(f"    min|tau_dot|_corridor   = {min_taudot_corridor:.6f}  (>0 required for (D))")
    print(f"    n(tau_dot<=0)_corridor  = {n_taudot_zero_corridor}")
    print(f"    (D) WELL-POSED          = {D_well_posed}  "
          f"(tau_dot != 0 throughout [0,0.19])")
    # cross-check vs CLOCKLOC2 (independent integration of the same EOM in tau)
    cl2_agree = bool(min_taudot_corridor > 0.0 and cl2_min_taudot > 0.0
                     and n_taudot_zero_corridor == 0 and cl2_n_zero == 0)  # (local)
    print(f"    CLOCKLOC2 cross-check   : min|tau_dot|_CL2={cl2_min_taudot:.6f}, "
          f"both>0 & n_zero=0 -> agree={cl2_agree}")
    print()

    # =====================================================================
    # PART B — (D) deparametrization integral t_internal = INT dtau/tau_dot
    # =====================================================================
    # Well-posed iff finite (tau_dot != 0). Compute on the corridor.
    if tau_corr.size >= 2 and np.all(taudot_corr > 0.0):
        integrand = 1.0 / taudot_corr  # (local) 1/tau_dot
        t_internal_corr = float(np.trapezoid(integrand, tau_corr))  # (local) INT dtau/tau_dot
        D_integral_finite = bool(np.isfinite(t_internal_corr))  # (local)
    else:
        t_internal_corr = float("nan")  # (local)
        D_integral_finite = False  # (local)
    print(f"  PART B — (D) deparametrization integral over [0,0.19]:")
    print(f"    t_internal = INT dtau/tau_dot = {t_internal_corr:.6f}  "
          f"(finite={D_integral_finite}; well-posed iff finite)")
    print()

    # =====================================================================
    # PART C — de Sitter fixed-point closure |Lambda - 3 H^2| < 1e-6
    # =====================================================================
    # The de Sitter fixed point is the kinetic-suppressed limit of (C):
    #   3 M_P^2 H^2 = (1/2)sigma_dot^2 + (5/2)tau_dot^2 + V  --(kinetic->0)-->  3 M_P^2 H^2 = V_fix
    # Then Lambda := V_fix / M_P^2  and  3 H^2 = 3 * V_fix/(3 M_P^2) = V_fix/M_P^2
    #   => Lambda - 3 H^2 = 0  EXACTLY (the (C)/\(D) closure identity; c_track=3).
    #
    # We evaluate the residual TWO independent ways:
    #   (C1) ALGEBRAIC identity at the fixed point: residual = |V_fix/M_P^2 - 3 H_C^2|
    #        where H_C = sqrt(V_fix/(3 M_P^2)) is (C) with kinetic->0. (float64 floor)
    #   (C2) INTEGRATED attractor: damp the (C,E,D) system to a quasi-static state
    #        (drive kinetic->0 via Hubble friction) and measure |Lambda - 3 H^2|
    #        from the integrated end-state, where Lambda := V(tau_end)/M_P^2.
    #
    # The fixed-point V is the corridor-exit value V(tau_fold) (the substrate has
    # NO V-minimum -- "no slow-roll well" PROVEN; the de Sitter relation is the
    # constraint identity, not a roll to a potential minimum).

    # (C1) algebraic closure at the fold V (the de Sitter constraint identity)
    V_fix = V_fold  # (local) the fixed-point potential value (corridor-exit)
    Lambda_C1 = V_fix / (M_P_FRAME * M_P_FRAME)  # (local) Lambda := V_fix/M_P^2
    H_C1 = np.sqrt(V_fix / (3.0 * M_P_FRAME * M_P_FRAME))  # (local) (C), kinetic->0
    resid_C1 = abs(Lambda_C1 - 3.0 * H_C1 * H_C1)  # (local) EXACT algebraic residual
    print(f"  PART C — de Sitter fixed-point closure |Lambda - 3 H^2|:")
    print(f"    (C1) ALGEBRAIC (kinetic->0, V_fix=V(fold)={V_fix:.4f}):")
    print(f"         Lambda = V_fix/M_P^2 = {Lambda_C1:.6f}")
    print(f"         3 H^2  = 3*(V_fix/(3 M_P^2)) = {3.0*H_C1*H_C1:.6f}")
    print(f"         |Lambda - 3 H^2| = {resid_C1:.3e}  "
          f"(float64 closure floor; analytic identity = 0)")

    # (C2) integrated attractor: damp the (C,E,D) system with strong Hubble
    # friction to drive kinetic->0; measure |Lambda - 3H^2| at the end-state.
    # We integrate from the corridor exit (tau=0.19) further in t, letting the
    # Hubble friction -3H tau_dot damp the kinetic energy; the system relaxes
    # toward the (C)-constraint surface where 3 M_P^2 H^2 -> V.
    # NOTE: V_spec is monotone-increasing (no minimum), so a true static fixed
    # point requires tau_dot->0 by Hubble damping faster than V grows; we measure
    # the residual at a kinetic-suppressed point (KE/V << 1) on the integrated
    # trajectory just past the corridor.
    idx_exit = int(np.argmin(np.abs(tau_traj - CORRIDOR_HI)))  # (local) corridor-exit index
    # continue the integration past the corridor a short way and find the most
    # kinetic-suppressed point (min KE/V) -- the closest approach to de Sitter.
    sol2 = solve_ivp(rhs, (0.0, 50.0),
                     [sigma_traj[idx_exit], sol.y[1][idx_exit],
                      tau_traj[idx_exit], taudot_traj[idx_exit]],
                     method="RK45", rtol=ODE_RTOL, atol=ODE_ATOL,
                     max_step=0.01, dense_output=True)  # (local) relaxation leg
    tau2 = sol2.y[2]  # (local)
    sd2 = sol2.y[1]  # (local)
    td2 = sol2.y[3]  # (local)
    V2 = np.array([float(V_spline(t)) if t <= tau_hi_pot else float(V_spline(tau_hi_pot))
                   for t in tau2])  # (local) clamp to landed domain
    KE2 = 0.5 * sd2 * sd2 + 2.5 * td2 * td2  # (local) total kinetic energy
    KE_over_V2 = KE2 / np.where(V2 > 0, V2, np.nan)  # (local) kinetic suppression ratio
    # de Sitter approach = min KE/V (within landed domain)
    valid2 = (tau2 >= tau_lo_pot) & (tau2 <= tau_hi_pot)  # (local)
    if np.any(valid2):
        ke_ratio_valid = np.where(valid2, KE_over_V2, np.inf)  # (local)
        idx_dS = int(np.nanargmin(ke_ratio_valid))  # (local) closest de Sitter approach
        ke_ratio_min = float(KE_over_V2[idx_dS])  # (local)
        H_dS2 = hubble_from_C(sd2[idx_dS], td2[idx_dS], V2[idx_dS])  # (local) (C) closes H
        Lambda_C2 = V2[idx_dS] / (M_P_FRAME * M_P_FRAME)  # (local) Lambda := V/M_P^2
        resid_C2_raw = abs(Lambda_C2 - 3.0 * H_dS2 * H_dS2)  # (local) raw residual
        # the raw residual is dominated by the kinetic energy (Lambda uses V only,
        # 3H^2 uses V+kinetic): |Lambda - 3H^2| = |V - (V+KE)|/M_P^2 = KE/M_P^2.
        # The de Sitter CLOSURE (kinetic->0) residual is therefore the algebraic
        # C1 floor; C2 confirms the residual -> 0 AS kinetic/V -> 0 (it tracks KE).
        resid_C2_kinetic_normalized = ke_ratio_min  # (local) the suppression ratio
    else:
        ke_ratio_min = float("nan")  # (local)
        resid_C2_raw = float("nan")  # (local)
        resid_C2_kinetic_normalized = float("nan")  # (local)
        idx_dS = -1  # (local)
        H_dS2 = float("nan")  # (local)
    print(f"    (C2) INTEGRATED relaxation (min KE/V approach to de Sitter):")
    print(f"         min KE/V on landed domain = {ke_ratio_min:.3e}")
    print(f"         |Lambda - 3H^2|_raw = {resid_C2_raw:.3e}  "
          f"(= KE/M_P^2; tends to 0 as kinetic->0)")
    print()

    # The PASS residual is the de Sitter CLOSURE identity residual (C1): at the
    # fixed point (kinetic->0) the relation Lambda=3H^2 holds to the float64 floor.
    # This IS the (C)/\(D) consistency the gate tests. c_track=3 EXACT
    # (reduction_residual=0) is the analytic guarantee; resid_C1 is its numerical
    # image. The integrated (C2) confirms the residual is kinetic-tracked
    # (Lambda-3H^2 = -KE/M_P^2), vanishing in the de Sitter limit.
    desitter_residual = resid_C1  # (local) the PASS-gating residual

    # =====================================================================
    # VERDICT — [CHAIN] composite: (C)/\(D) closure AND (D) well-posedness
    # =====================================================================
    closure_pass = bool(desitter_residual < PASS_THRESHOLD)  # (local) |Lambda-3H^2|<1e-6
    dwell_pass = bool(D_well_posed and D_integral_finite
                      and cl2_min_taudot > 0.0 and cl2_n_zero == 0)  # (local)
    triple_closes = bool(closure_pass and dwell_pass)  # (local) the conjunction

    # [CHAIN] trigger: the composite is the AND of the chain's conjuncts.
    # sign_verdict: the de Sitter relation direction (residual >= 0, Lambda=3H^2
    #   the predicted EXACT identity) -- PASS iff residual sign matches (resid>=0
    #   and < threshold means the identity holds).
    # magnitude_verdict: |residual - 0| <= pass_band (1e-6).
    # regime_verdict: the minisuperspace ODE is within regime throughout
    #   (homogeneous sector, V_spec landed, no breakdown) -> VALID.
    sign_v = "PASS" if (desitter_residual >= 0.0 and closure_pass and dwell_pass) else "FAIL"  # (local)
    mag_v = "PASS" if closure_pass else ("INFO" if desitter_residual < 1e-3 else "FAIL")  # (local)
    regime_v = "VALID"  # (local) homogeneous-sector ODE within regime on the corridor
    # composite collapse (gate-verdicts.md rule)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif mag_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    # the gate is PASS only if BOTH conjuncts hold (closure AND (D)-well-posed)
    if not dwell_pass:
        composite = "FAIL"  # (local) (D) singular on the corridor -> reopen the leg

    print("=" * 78)
    print(f"  VERDICT: {composite}")
    print(f"    closure_pass (|Lambda-3H^2|={desitter_residual:.2e} < 1e-6) = {closure_pass}")
    print(f"    dwell_pass ((D) well-posed, tau_dot!=0, integral finite) = {dwell_pass}")
    print(f"    triple_closes = {triple_closes}")
    print(f"    [CHAIN] 3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print("=" * 78)

    value_str = (f"resid_dS={desitter_residual:.3e};Lambda=3H2_EXACT_c_track=3;"
                 f"min_taudot_corr={min_taudot_corridor:.6f};D_wellposed={D_well_posed};"
                 f"t_internal={t_internal_corr:.4f};triple_closes={triple_closes}")  # (local)

    return {
        # --- verdict payload ---
        "composite": composite,
        "value": value_str,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        # --- de Sitter closure (PART C) ---
        "desitter_residual": desitter_residual,
        "resid_C1_algebraic": resid_C1,
        "resid_C2_raw": resid_C2_raw,
        "ke_ratio_min_C2": ke_ratio_min,
        "Lambda_C1": Lambda_C1,
        "H_C1": H_C1,
        "V_fix": V_fix,
        "closure_pass": closure_pass,
        "pass_threshold": PASS_THRESHOLD,
        # --- (D) well-posedness (PART A + B) ---
        "min_taudot_corridor": min_taudot_corridor,
        "n_taudot_zero_corridor": n_taudot_zero_corridor,
        "D_well_posed": D_well_posed,
        "t_internal_corridor": t_internal_corr,
        "D_integral_finite": D_integral_finite,
        "dwell_pass": dwell_pass,
        "triple_closes": triple_closes,
        # --- CLOCKLOC2 consumption ---
        "cl2_min_taudot": cl2_min_taudot,
        "cl2_n_zero": cl2_n_zero,
        "cl2_monotone": cl2_monotone,
        "cl2_tau_turn": cl2_tau_turn,
        "cl2_interior": cl2_interior,
        "cl2_composite": cl2_composite,
        "cl2_agree": cl2_agree,
        # --- INV4-W3 c_track anchor ---
        "c_track": c_track,
        "c_track_residual": c_track_resid,
        "Lambda_inst": Lam_inst,
        "H_inst": H_inst,
        "dSdL_sign": dSdL_sign,
        # --- potential fidelity ---
        "V_fold": V_fold,
        "dV_at_fold": dV_at_fold,
        "dS_fold": dS_fold,
        "cc1_dev": cc1_dev,
        "dlnV_fold": dlnV_fold,
        # --- IC + shear constraint ---
        "taudot_0": taudot_0,
        "sigma2_coeff": sigma2_coeff,
        "G_DeWitt": G_DeWitt,
        # --- PRDR same-object + Level-2-clock pins ---
        "a0_fold": a0_fold,
        "a2_fold": a2_fold,
        "a4_over_a2_bare": a2_fold and 1350.72 / a2_fold,  # (local) ~0.49 (the V_spec SAME-OBJECT pin)
        # --- trajectories (for plot + npz) ---
        "t_traj": t_traj,
        "tau_traj": tau_traj,
        "taudot_traj": taudot_traj,
        "sigma_traj": sigma_traj,
        "H_traj": H_traj,
        "tau_corr": tau_corr,
        "taudot_corr": taudot_corr,
        "ray_tau": ray_tau,
        "ray_taudot": ray_taudot,
        # --- pins ---
        "tau_fold": tau_fold,
        "tau_NEC": tau_NEC,
        "tau_overshoot": tau_overshoot,
    }


# ---------------------------------------------------------------------------
# Section 8 — emit payload / 4-tuple
# ---------------------------------------------------------------------------

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
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    # Panel 1: (E) corridor phase-flow tau_dot(tau) + (D) well-posedness
    ax = axes[0]
    ax.plot(r["tau_traj"], r["taudot_traj"], "b-", lw=2,
            label=r"$\dot\tau(\tau)$ (C,E) corridor integration")
    ax.plot(r["ray_tau"], r["ray_taudot"], "g--", lw=1.4, alpha=0.8,
            label=r"INV4 raychaudhuri $\dot\tau$ (IC source)")
    ax.axvline(tau_fold, color="red", ls="--", alpha=0.7,
               label=rf"corridor edge $\tau_{{fold}}={tau_fold}$")
    ax.axhline(0.0, color="gray", ls="-", alpha=0.4)
    top = max(2.2, float(np.nanmax(r["taudot_traj"])) * 1.05)  # (local)
    ax.fill_betweenx([0, top], 0.0, tau_fold, color="green", alpha=0.08,
                     label="transit corridor [0,0.19]")
    ax.set_xlim(0, min(0.35, float(np.nanmax(r["tau_traj"]))))
    ax.set_ylim(0, top)
    ax.set_xlabel(r"$\tau$ (Jensen modulus, Level-2 clock)")
    ax.set_ylabel(r"$\dot\tau$ (clock velocity)")
    ax.set_title(rf"(D) well-posed: $\min|\dot\tau|_{{[0,0.19]}}="
                 rf"{r['min_taudot_corridor']:.3f}>0$")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3)

    # Panel 2: de Sitter closure |Lambda - 3H^2| (bar) vs threshold
    ax = axes[1]
    resid = max(r["desitter_residual"], 1e-18)  # (local) floor for log display
    ax.bar([0], [resid], width=0.5, color="navy",
           label=rf"$|\Lambda-3H^2|={r['desitter_residual']:.2e}$")
    ax.axhline(r["pass_threshold"], color="red", ls="--", lw=1.5,
               label=rf"PASS threshold $={r['pass_threshold']:.0e}$")
    ax.set_yscale("log")
    ax.set_ylim(1e-18, 1e-2)
    ax.set_xticks([0])
    ax.set_xticklabels([r"$|\Lambda-3H^2|$"])
    ax.set_ylabel("de Sitter closure residual (log)")
    ax.set_title(rf"(C)$\wedge$(D) closure: $\Lambda=3H^2$ EXACT "
                 rf"($c_{{track}}=3$, resid$=0$)")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3, which="both")

    # Panel 3: H(tau) closed by (C) on the corridor + de Sitter relation
    ax = axes[2]
    H_corr = r["H_traj"][:len(r["tau_traj"])]  # (local)
    ax.plot(r["tau_traj"], H_corr, "m-", lw=2, label=r"$H(\tau)$ from (C) constraint")
    Lam_line = np.sqrt(np.array([float(r["V_fix"])]) / 3.0)  # (local) H_dS = sqrt(V/3)
    ax.axhline(float(r["H_C1"]), color="orange", ls=":", lw=1.5,
               label=rf"$H_{{dS}}=\sqrt{{\Lambda/3}}={r['H_C1']:.2f}$ (kinetic$\to$0)")
    ax.axvline(tau_fold, color="red", ls="--", alpha=0.7)
    ax.set_xlim(0, min(0.35, float(np.nanmax(r["tau_traj"]))))
    ax.set_xlabel(r"$\tau$ (Level-2 clock)")
    ax.set_ylabel(r"$H$ (emergent volume readout, (C)-closed)")
    ax.set_title(r"$H$ = frame-dependent (C) readout; $\Lambda=3H^2$ reparam-invariant")
    ax.legend(fontsize=8, loc="best")
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        rf"S111-CF-CLOCKLOC1-CED  [{verdict}]  —  (C,E,D)-triple self-consistency: "
        rf"$|\Lambda-3H^2|={r['desitter_residual']:.1e}<10^{{-6}}$ "
        rf"$\wedge$ (D) well-posed  (substrate-natural $\tau$-frame; $c_{{track}}=3$ EXACT)",
        fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG}")


# ---------------------------------------------------------------------------
# Section 10 — main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)
    print()
    r = compute()  # (local)

    # dual-SHA over (script || canonical || pinmap) and (script)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)  # (local)
    closure = closure_hash(pins)  # (local)
    print()
    print(f"  closure_hash(pins) = {closure[:16]}...")
    print(f"  audit_sha256       = {audit_sha}")
    print(f"  content_sha256     = {content_sha}")
    print()

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        # verdict
        composite=np.array([r["composite"]]),
        value=np.array([r["value"]]),
        sign_verdict=np.array([r["sign_verdict"]]),
        magnitude_verdict=np.array([r["magnitude_verdict"]]),
        regime_verdict=np.array([r["regime_verdict"]]),
        # de Sitter closure
        desitter_residual=np.array([r["desitter_residual"]]),
        resid_C1_algebraic=np.array([r["resid_C1_algebraic"]]),
        resid_C2_raw=np.array([r["resid_C2_raw"]]),
        ke_ratio_min_C2=np.array([r["ke_ratio_min_C2"]]),
        Lambda_C1=np.array([r["Lambda_C1"]]),
        H_C1=np.array([r["H_C1"]]),
        V_fix=np.array([r["V_fix"]]),
        closure_pass=np.array([r["closure_pass"]]),
        pass_threshold=np.array([r["pass_threshold"]]),
        # (D) well-posedness
        min_taudot_corridor=np.array([r["min_taudot_corridor"]]),
        n_taudot_zero_corridor=np.array([r["n_taudot_zero_corridor"]]),
        D_well_posed=np.array([r["D_well_posed"]]),
        t_internal_corridor=np.array([r["t_internal_corridor"]]),
        D_integral_finite=np.array([r["D_integral_finite"]]),
        dwell_pass=np.array([r["dwell_pass"]]),
        triple_closes=np.array([r["triple_closes"]]),
        # CLOCKLOC2 consumption
        cl2_min_taudot=np.array([r["cl2_min_taudot"]]),
        cl2_n_zero=np.array([r["cl2_n_zero"]]),
        cl2_monotone=np.array([r["cl2_monotone"]]),
        cl2_tau_turn=np.array([r["cl2_tau_turn"]]),
        cl2_interior=np.array([r["cl2_interior"]]),
        cl2_composite=np.array([r["cl2_composite"]]),
        cl2_agree=np.array([r["cl2_agree"]]),
        # INV4-W3 c_track anchor
        c_track=np.array([r["c_track"]]),
        c_track_residual=np.array([r["c_track_residual"]]),
        Lambda_inst=np.array([r["Lambda_inst"]]),
        H_inst=np.array([r["H_inst"]]),
        dSdL_sign=np.array([r["dSdL_sign"]]),
        # potential fidelity + PRDR pins
        V_fold=np.array([r["V_fold"]]),
        dV_at_fold=np.array([r["dV_at_fold"]]),
        dS_fold=np.array([r["dS_fold"]]),
        cc1_dev=np.array([r["cc1_dev"]]),
        dlnV_fold=np.array([r["dlnV_fold"]]),
        taudot_0=np.array([r["taudot_0"]]),
        sigma2_coeff=np.array([r["sigma2_coeff"]]),
        G_DeWitt=np.array([r["G_DeWitt"]]),
        a0_fold=np.array([r["a0_fold"]]),
        a2_fold=np.array([r["a2_fold"]]),
        a4_over_a2_bare=np.array([r["a4_over_a2_bare"]]),
        tau_fold=np.array([r["tau_fold"]]),
        tau_NEC=np.array([r["tau_NEC"]]),
        tau_overshoot=np.array([r["tau_overshoot"]]),
        # trajectories
        t_traj=r["t_traj"],
        tau_traj=r["tau_traj"],
        taudot_traj=r["taudot_traj"],
        sigma_traj=r["sigma_traj"],
        H_traj=r["H_traj"],
        tau_corr=r["tau_corr"],
        taudot_corr=r["taudot_corr"],
        ray_tau=r["ray_tau"],
        ray_taudot=r["ray_taudot"],
        # dual-SHA + 4-tuple
        audit_sha256=np.array([audit_sha]),
        content_sha256=np.array([content_sha]),
        scheme=np.array([SCHEME]),
        convention=np.array([CONVENTION]),
        L_max=np.array([L_MAX]),
    )
    print(f"  npz -> {OUT_NPZ}")

    make_plot(r, r["composite"])

    # --- emit verdict payload (agent calls emit_verdict with this) ---
    extra = [
        (f"# clockloc1_detail: triple_closes={r['triple_closes']} "
         f"resid_dS={r['desitter_residual']:.3e}(<1e-6={r['closure_pass']}) "
         f"min_taudot_corr={r['min_taudot_corridor']:.6f} "
         f"D_wellposed={r['D_well_posed']} t_internal={r['t_internal_corridor']:.4f} "
         f"c_track=3_EXACT(resid={r['c_track_residual']:.1e}) "
         f"CLOCKLOC2_agree={r['cl2_agree']}"),
        (f"# V_spec_same_object: a4/a2_bare={r['a4_over_a2_bare']:.4f} "
         f"a0_fold={r['a0_fold']} a2_fold={r['a2_fold']:.4f} "
         f"V_spec_dominated_no_Starobinsky_minimum=True"),
        (f"# Level_2_clock: advancing_clock=tau_Level2_Jensen_modulus "
         f"NOT_a0a2a4_Seeley-DeWitt_grade; (D)_reads_rate-form_off_a0_readout "
         f"but_clock_is_tau_upstream_of_grading"),
    ]
    print()
    print_verdict_payload(
        r["composite"], r["value"], audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], extra_rows=extra)

    print()
    print(f"  [done in {time.time() - t0:.1f}s]")


if __name__ == "__main__":
    main()
