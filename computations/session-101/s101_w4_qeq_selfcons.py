#!/usr/bin/env python3
"""
S101 W4-1  S101-W1-QEQ-SELFCONS -- KV oscillation-energy SELF-CONSISTENCY:
does d ln q_dev / d ln|H| -> 1 EMERGE as a BACK-REACTION (not a fixed-backbone drive)?
===============================================================================

Gate: S101-W1-QEQ-SELFCONS ([SIGN])

Pre-registered threshold (plan session-101-plan-w4.md  §W4-1; thresholds
inherited BINDING from the S100a-W1-2 rubric per workshop delta-ZERO
landing-list (v), s100a-w1-hparity-scope-workshop.md:768):
  operator:  |slope_selfcons - 1| <= 0.05  AND  domain_used_frac >= 0.95
             slope_selfcons = OLS slope of ln q_dev vs ln|H| over the FULL
             post-fold tail, q_dev = cycle-RMS of (q - q_eq).
  PASS  iff |slope_selfcons - 1| <= 0.05 with domain_used_frac >= 0.95
        (n=2 tracking-law slope-1 leg DERIVED, unforced, from KV
        oscillation-energy self-consistency; q ~ H closure stops being an
        imposed INPUT; clause (f) of the H-parity candidate realized).
  INFO  iff 0.05 < |slope_selfcons - 1| <= 0.5  (partial self-consistency;
        Paper 35 §V refinement ladder), OR domain_used_frac in [0.50,0.95).
  FAIL  iff |slope_selfcons - 1| > 0.5  (last dynamical route to unforced
        n=2 closed; tracking law irreducibly closure-conditional).
  NON-GATING annotation (ii): a PASS must realize slope 1 SPECIFICALLY through
        q_amp ~ |H| (non-analytic-even cell). slope_amp from the
        successive-extrema envelope must separately confirm; a PASS realized
        any other way (secular q-bar drift mimicking slope 1) flags
        NEW-AMPLITUDE-ANOMALY in the value string (S102 gate candidate).

DISTINCTION FROM THE PREDECESSOR (S100a-W1-2-QEQ-DRIVE, FAIL, slope 2.0556):
  Predecessor: H(tau) READ from arr_H_bare_t (a FROZEN external backbone); the
  well-center q_eq(H) = kappa2*H^2 is an ANALYTIC-EVEN drive on a FIXED
  backbone -> measured slope 2.0556 = the H^2 parity wall (clause (f) shows
  |H|=sqrt(H^2) is non-analytic-even and structurally unavailable to ANY
  fixed-backbone equilibrium drive). This is the equilibrium-sector theorem.

  THIS gate: H is NOT a fixed input. The Sec.6.3 closure
  H^2 = (kappa^2/3) rho_q makes H emerge SELF-CONSISTENTLY from the
  cycle-averaged q-oscillation energy rho_q = (1/2) k_curv q_amp^2. The
  oscillation amplitude decays because the substrate's OWN emergent
  background (a, sourced by rho_q) dilutes the oscillation energy. Rapid
  oscillation about q*=0 averages to w=0 dust => rho_q ~ a^-3 => a ~ t^{2/3},
  H = (2/3) t^-1 => q_amp ~ t^-1 ~ |H| (slope 1). This is BACK-REACTION,
  carried by the amplitude variable alone -- the unique non-analytic-even
  cell the H-parity theorem (clause (f) carve-out) leaves open.

SUBSTITUTION CHAIN (numbers substituted where pinned; plan §W4-1 item 7)
-----------------------------------------------------------------------
  Claim: "On the self-consistent q-dominated background, q_amp ~ |H| (slope 1),
          through the amplitude variable ONLY."

  Def 1: q_osc(t) = q(t) - q_eq,  q_eq = q* = 0 (interior equilibrium,
         s99_w2 q_star = 0.0); well curvature k_curv = +3586.531
         (s100a_w1_qeq_drive.npz key 'k_curv'; backbone S99-W1/W2).
  Def 2: rho_q = <E_q>_cycle = (1/2) k_curv q_amp^2  (cycle-averaged
         oscillation energy; adiabatic invariant E = (1/2)q_dot^2 +
         (1/2)k_curv q^2; averaging valid for omega_q >> |H|:
         omega_q = sqrt(k_curv) = 59.888, |H| ~ O(0.07-0.31) on tail,
         |H|/omega_q ~ 0.004 << 1).
  Def 3: Sec.6.3 closure (q-domination regime):  H^2 = (kappa^2/3) rho_q
         (S_SA sector normalized by a_0^{zeta} = 6440.0; the closure
         normalization is a MULTIPLICATIVE pre-factor -> cancels in the
         log-derivative, math-scripts.md multiplicative-normalization theorem).
  Def 4: KV self-consistency [Volovik Paper 25 §V Eqs. (5.5a-b)]: rapid
         oscillation about the well averages to w = 0 dust => rho_q ~ a^-3
         on the self-consistent background => a ~ t^{2/3}, H = (2/3) t^-1.

  Substitute:  (1/2) k_curv q_amp^2(t) = rho_q(t) ~ a^-3(t) ~ t^-2
  Simplify:    q_amp(t) ~ t^-1 ;  H(t) = (2/3) t^-1  => t^-1 = (3/2)H
               q_amp ~ |H|        [|H| = sqrt(H^2): even under t->-t, non-analytic at H=0]
  Canonical:   d ln q_amp / d ln|H| = 1.

  Direction:   slope-1 EMERGES from self-consistent back-reaction (amplitude
               variable alone), parity-CONSISTENT (clause (f): |H| occupies the
               non-analytic-even cell). NOT available to any analytic
               equilibrium drive q_eq(H) on a fixed backbone (S100a-W1-2 FAIL:
               leading power H^2, measured slope 2.0556).
  Conclusion:  PASS requires |slope_selfcons - 1| <= 0.05 (domain_used_frac
               >= 0.95) AND slope_amp ~ 1 (q_amp ~ |H| confirmed). A PASS that
               does not realize slope 1 via q_amp ~ |H| flags
               NEW-AMPLITUDE-ANOMALY (annotation ii).

METHOD (plan §W4-1 item 5; ODE only, no diagonalization)
--------------------------------------------------------
  Integrate the COUPLED self-consistent system in cosmic time t, state
  y = [q, q_dot, ln a]:
      q_ddot = -3 H q_dot - k_curv (q - q_eq)      (q* = 0)
      d(ln a)/dt = H
      H = sqrt( (kappa^2/3) rho_q )                (Sec.6.3 closure)
      rho_q = mechanical energy E = (1/2)q_dot^2 + (1/2)k_curv q^2
              (instantaneous E; its cycle average IS (1/2)k_curv q_amp^2;
               H built from instantaneous E carries fast ripple that the
               cycle-RMS coarse-grain removes -- the gated slope uses the
               coarse-grained q_dev, NOT instantaneous E).
  Post-fold ICs: q0, q_dot0 from s99_w2 window start (transient_end_idx) --
  the q_boundary lineage. kappa^2/3 normalization is FIXED to reproduce the
  S99 backbone H at the window start (slope-INVARIANT pre-factor; cross-checked
  by a x10 re-run). Re-grid the t-solution onto a 999-pt tau-grid matching the
  backbone convention, take the FULL post-fold tail (final 50%), and:
    - q_dev  = cycle-RMS of (q - q_eq) over a sliding 1-oscillation window
               -> slope_selfcons = OLS(ln q_dev, ln|H|)            [GATED]
    - q_amp  = successive-extrema envelope (no Hilbert transform)
               -> slope_amp      = OLS(ln q_amp, ln|H|)            [DIAGNOSTIC, ann.(ii)]

DISCIPLINE
----------
- from canonical_constants import * (MANDATORY first import)
- every intermediate tagged # (local)
- CPU scalar ODE (OMP_NUM_THREADS=8 capped before numpy import); matrix-free
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+)
- verdict via emit_verdict knowledge-MCP tool (script PRINTS payload only)
- regulator pin a_0^{zeta} (a_0_FW_zeta = 6440.0) enters the S_SA sector norm
- TAU0-OPERATOR-CANONICITY L4 lift HAS landed -> s84 cache full-confidence;
  this gate does not consume the s84 cache, so the A19 conditional row is N/A.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # plan GPU_path pin: numpy cpu-cap-OMP8
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402  (a_0_FW_zeta, tau_fold, ...)

import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

import numpy as np                       # noqa: E402
from scipy.integrate import solve_ivp    # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
import matplotlib                        # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt          # noqa: E402

# ---------------------------------------------------------------------------
# Paths + pre-registration (plan session-101-plan-w4.md §W4-1; FROZEN)
# ---------------------------------------------------------------------------
SESSION_DIR = _Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "101"                                    # (local)
GATE_ID = "S101-W1-QEQ-SELFCONS"                   # (local)
SCHEME = "FW"                                      # (local)
CONVENTION = "SUBSTRATE-NATURAL-BINDING"           # (local) matches predecessor
L_MAX = "N/A"                                      # (local) ODE+closure; no spectral truncation

PASS_BAND = 0.05            # (local) plan strict_PASS_boundary: |slope-1| <= 0.05
INFO_BAND = 0.5            # (local) plan INFO band ceiling: (0.05, 0.5]
TARGET_SLOPE = 1.0          # (local) the n=2 tracking-law slope-1 leg
F_VALID = 0.95              # (local) gate-verdicts.md auto-shortening band: VALID + plan domain_used_frac>=0.95
F_MARGINAL = 0.50           # (local) gate-verdicts.md auto-shortening band: MARGINAL
ODE_RTOL = 1e-10            # (local) plan machinery pin (ODE)
ODE_ATOL = 1e-12            # (local) plan machinery pin (ODE)
K_CURV_PLAN_PIN = 3586.5    # (local) plan-block pin (5 sf print of npz k_curv); XC-3
OMEGA_PLAN_PIN = 59.888     # (local) plan omega_q_tau cross-check target
KAPPA_INV_TOL = 1e-3        # (local) closure-normalization invariance (multiplicative cancellation)
N_TAU_GRID = 999            # (local) plan N_eval: match S99/S100a backbone grid convention

NPZ_DRIVE = COMPUTATIONS_DIR / "session-100a" / "s100a_w1_qeq_drive.npz"        # k_curv, omega
NPZ_W1 = COMPUTATIONS_DIR / "session-99" / "s99_w1_q_nonratio_observable.npz"   # backbone (tau, H)
NPZ_W2 = COMPUTATIONS_DIR / "session-99" / "s99_w2_relaxation_closure.npz"      # q_boundary ICs, q_star, K_CURV
OUT_NPZ = SESSION_DIR / "s101_w4_qeq_selfcons.npz"
OUT_PNG = SESSION_DIR / "s101_w4_qeq_selfcons.png"

# audit_sha256 inputs: script + canonical + pinmap (over these on-disk files)
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    NPZ_DRIVE,
    NPZ_W1,
    NPZ_W2,
]


# ---------------------------------------------------------------------------
# SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: _Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict):
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Regression helper
# ---------------------------------------------------------------------------
def loglog_fit(q: np.ndarray, H: np.ndarray, mask: np.ndarray):
    """OLS of ln q on ln|H| over mask & q>0 & H finite. Returns slope, icpt, r2, n_used, m."""
    Hab = np.abs(H)                                                      # (local)
    m = mask & (q > 0.0) & (Hab > 0.0) & np.isfinite(q) & np.isfinite(Hab)  # (local)
    n_used = int(m.sum())                                               # (local)
    if n_used < 3:
        return np.nan, np.nan, np.nan, n_used, m
    x = np.log(Hab[m]); y = np.log(q[m])                                # (local)
    A = np.vstack([x, np.ones_like(x)]).T                               # (local)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)                        # (local)
    yhat = A @ coef                                                     # (local)
    ss_res = float(np.sum((y - yhat) ** 2))                             # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))                       # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan                # (local)
    return float(coef[0]), float(coef[1]), r2, n_used, m


def cycle_rms(q: np.ndarray, t: np.ndarray, period: float) -> np.ndarray:
    """Coarse-grained RMS of q over a sliding 1-oscillation-period window.
    Deterministic (no Hilbert transform). For a pure sinusoid of amplitude A,
    RMS = A/sqrt(2); the slope of ln(RMS) equals the slope of ln(amplitude)
    (constant 1/sqrt(2) factor cancels in the log-derivative)."""
    n = len(t)                                                          # (local)
    out = np.empty(n)                                                   # (local)
    for i in range(n):
        lo = t[i] - 0.5 * period                                       # (local)
        hi = t[i] + 0.5 * period                                       # (local)
        j0 = np.searchsorted(t, lo, side="left")                       # (local)
        j1 = np.searchsorted(t, hi, side="right")                      # (local)
        if j1 - j0 < 2:
            out[i] = abs(q[i])
        else:
            out[i] = float(np.sqrt(np.mean(q[j0:j1] ** 2)))            # (local)
    return out


def envelope_extrema(q: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Successive-extrema envelope interpolation (DIAGNOSTIC, annotation ii).
    Find local maxima of |q| (sign changes of d|q|), interpolate |q| at those
    extrema onto the full grid. No Hilbert transform."""
    aq = np.abs(q)                                                      # (local)
    # interior local maxima of |q|
    idx = np.where((aq[1:-1] >= aq[:-2]) & (aq[1:-1] >= aq[2:]))[0] + 1  # (local)
    if len(idx) < 2:
        return aq.copy()
    # ensure endpoints anchored
    if idx[0] != 0:
        idx = np.concatenate(([0], idx))
    if idx[-1] != len(q) - 1:
        idx = np.concatenate((idx, [len(q) - 1]))
    env = np.interp(t, t[idx], aq[idx])                                 # (local)
    return env


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    dD = np.load(NPZ_DRIVE, allow_pickle=True)  # (local) s100a drive npz (k_curv, omega)
    d1 = np.load(NPZ_W1, allow_pickle=True)     # (local) backbone npz
    d2 = np.load(NPZ_W2, allow_pickle=True)     # (local) relaxation-closure npz

    # --- backbone grid + H (the S99-W1 backbone; comparison reference) ----
    tau = np.asarray(d1["arr_tau"], dtype=float)          # (local) 999-pt tau grid
    H_backbone = np.asarray(d1["arr_H_bare_t"], dtype=float)  # (local) S99 backbone H(tau)
    n_total = len(tau)                                    # (local)
    tau0, tauf = float(tau[0]), float(tau[-1])            # (local)

    # --- substrate parameters (runtime-read + cross-checked) --------------
    k_curv = float(dD["k_curv"])                          # (local) +3586.5311811081065
    k_curv_w2 = float(d2["K_CURV"])                       # (local) XC: same value in W2
    q_eq = float(d2["q_star"])                            # (local) interior equilibrium = 0.0
    q_boundary = float(d2["q_boundary"])                  # (local) -0.6719754908120351
    omega_npz = float(dD["omega"])                        # (local) 59.88765 (= sqrt k_curv)

    omega_q = float(np.sqrt(k_curv))                      # (local) realized osc freq, sqrt convention (s97)
    period = 2.0 * np.pi / omega_q                        # (local) oscillation period in time units
    ODE_MAXSTEP = 1.0 / (20.0 * omega_q)                  # (local) plan: resolve the 59.888 osc

    # --- XC-3: npz k_curv vs plan-block pin -------------------------------
    xc3_dev = abs(k_curv - K_CURV_PLAN_PIN)               # (local)
    xc3_ok = xc3_dev <= 0.05                              # (local)
    # --- XC-omega: realized freq vs plan pin + npz omega ------------------
    xc_omega_dev_plan = abs(omega_q - OMEGA_PLAN_PIN)     # (local) A-V2 cross-check target
    xc_omega_dev_npz = abs(omega_q - omega_npz)           # (local)
    xc_omega_ok = (xc_omega_dev_plan <= 1e-2) and (xc_omega_dev_npz <= 1e-6)  # (local)
    # --- XC-kcurv: drive npz vs relaxation npz k_curv ---------------------
    xc_kcurv_dev = abs(k_curv - k_curv_w2)                # (local)
    xc_kcurv_ok = xc_kcurv_dev <= 1e-9                    # (local)

    # --- post-fold ICs: q_boundary lineage (s99_w2 window start) ----------
    # window start = transient_end_idx (arr_win[0]); arr_u = q, arr_ud = q_dot
    te = int(d2["transient_end_idx"])                     # (local) 499
    u_arr = np.asarray(d2["arr_u"], dtype=float)          # (local) q lineage
    ud_arr = np.asarray(d2["arr_ud"], dtype=float)        # (local) q_dot lineage
    q0 = float(u_arr[te])                                 # (local) post-fold q IC
    qd0 = float(ud_arr[te])                               # (local) post-fold q_dot IC

    # --- Sec.6.3 closure normalization (kappa^2/3) ------------------------
    # H^2 = (kappa^2/3) rho_q,  rho_q = (1/2)q_dot^2 + (1/2)k_curv(q-q_eq)^2.
    # The normalization C3 = kappa^2/3 is a MULTIPLICATIVE pre-factor; the
    # slope d ln q_dev/d ln|H| is C3-INVARIANT (math-scripts.md multiplicative-
    # normalization-cancellation theorem: log-derivative annihilates a
    # K-independent multiplicative pre-factor). DIAGNOSTIC pin: choose C3 so
    # that H from the closure at the IC matches the S99 backbone H at window
    # start -> the self-consistent run starts on the backbone. a_0^{zeta}
    # enters the S_SA sector normalization (regulator pin); here it scales
    # rho_q's zero-point reference and is absorbed into C3 by the same
    # cancellation. Re-run at 10*C3 verifies slope-invariance.
    E_ic = 0.5 * qd0**2 + 0.5 * k_curv * (q0 - q_eq) ** 2  # (local) IC oscillation energy
    H_ic_target = float(H_backbone[te])                   # (local) backbone H at window start
    C3 = H_ic_target**2 / E_ic                            # (local) kappa^2/3 (slope-INVARIANT)

    # --- self-consistent coupled ODE in cosmic time t ---------------------
    # state y = [q, q_dot, ln a]; t is cosmic time (dimensionless backbone units)
    def H_of_state(q, qd):
        E = 0.5 * qd * qd + 0.5 * k_curv * (q - q_eq) ** 2   # (local) instantaneous energy = rho_q
        return float(np.sqrt(C3 * E)) if E > 0.0 else 0.0

    def rhs_factory(C3_loc):
        def rhs(t, y):
            q, qd, lna = y                                  # (local)
            E = 0.5 * qd * qd + 0.5 * k_curv * (q - q_eq) ** 2  # (local)
            H = np.sqrt(C3_loc * E) if E > 0.0 else 0.0     # (local) Sec.6.3 closure
            qdd = -3.0 * H * qd - k_curv * (q - q_eq)       # (local) q-oscillator + back-reaction friction
            return [qd, qdd, H]                             # (local) d ln a/dt = H
        return rhs

    # integration time span: the time over which a ~ t^{2/3} accumulates the
    # same e-fold range as the backbone tail. Integrate generously in t, then
    # re-grid onto a 999-pt tau-grid via ln a (tau IS the backbone clock; on a
    # self-consistent a~t^{2/3} background ln a is monotone, providing the map).
    # t_end set so ln a spans >= backbone ln(a_max/a_min). Use the backbone's
    # own a-range as the target.
    a_bb = np.asarray(d1["arr_a_bare_t"], dtype=float)     # (local) backbone a(tau)
    lnA_span_target = float(np.log(a_bb.max() / a_bb.min()))  # (local) backbone e-folds

    # estimate t_end from a ~ t^{2/3}: choose t span giving the target ln a.
    # Start integration at t0_int = 1.0 (sets the time origin; cancels in slope).
    t0_int = 1.0                                           # (local)
    # H(t0) ~ (2/3) t0^-1 on the attractor => t scale ~ (2/3)/H_ic
    t_scale = (2.0 / 3.0) / max(H_ic_target, 1e-12)        # (local)
    # generous t_end: enough to dilute amplitude over several e-folds
    t_end = t0_int + 60.0 * t_scale                        # (local) generous; auto-clipped on re-grid
    n_t = 200000                                           # (local) dense t-grid (cheap scalar ODE)
    t_eval = np.linspace(t0_int, t_end, n_t)               # (local)

    y0 = [q0, qd0, 0.0]                                    # (local) ln a = 0 at t0_int
    sol = solve_ivp(rhs_factory(C3), (t0_int, t_end), y0,
                    method="LSODA", rtol=ODE_RTOL, atol=ODE_ATOL,
                    max_step=ODE_MAXSTEP, t_eval=t_eval, dense_output=False)  # (local)
    solver_ok = bool(sol.success)                          # (local)

    t = sol.t                                              # (local)
    q_t = sol.y[0]                                         # (local)
    qd_t = sol.y[1]                                        # (local)
    lna_t = sol.y[2]                                       # (local)
    H_t = np.array([H_of_state(q_t[i], qd_t[i]) for i in range(len(t))])  # (local) self-consistent H(t)

    # coefficient-invariance probe: re-run at 10*C3 (slope must be unchanged)
    C3x = 10.0 * C3                                        # (local)
    H_ic_x = np.sqrt(C3x * E_ic)                           # (local)
    t_scale_x = (2.0 / 3.0) / max(H_ic_x, 1e-12)           # (local)
    t_end_x = t0_int + 60.0 * t_scale_x                    # (local)
    t_eval_x = np.linspace(t0_int, t_end_x, n_t)           # (local)
    sol_x = solve_ivp(rhs_factory(C3x), (t0_int, t_end_x), y0,
                      method="LSODA", rtol=ODE_RTOL, atol=ODE_ATOL,
                      max_step=1.0 / (20.0 * omega_q), t_eval=t_eval_x,
                      dense_output=False)                  # (local)
    solver_ok = solver_ok and bool(sol_x.success)          # (local)
    tx = sol_x.t; qx_t = sol_x.y[0]; qdx_t = sol_x.y[1]    # (local)
    Hx_t = np.array([H_of_state(qx_t[i], qdx_t[i]) for i in range(len(tx))])  # (local)

    # --- re-grid onto a 999-pt tau-grid (the backbone clock) --------------
    # On the self-consistent a ~ t^{2/3} attractor, map cosmic time t onto the
    # backbone tau by matching e-fold (ln a). Build tau-grid as 999 uniform
    # points; the slope d ln q_dev/d ln|H| is grid-INDEPENDENT (both q_dev and
    # |H| are evaluated on the SAME grid), so the choice of re-grid is a
    # presentation choice, not a physics input. We coarse-grain in t (physical),
    # then sample the cycle-RMS/envelope at N_TAU_GRID uniform t-points.
    # tail = FULL post-fold final 50% of the t-window.
    # cycle-RMS deviation (GATED) and envelope (DIAGNOSTIC) on the dense t-grid:
    q_dev_t = cycle_rms(q_t - q_eq, t, period)             # (local) coarse-grained |dev|
    q_env_t = envelope_extrema(q_t - q_eq, t)              # (local) successive-extrema envelope

    # sample onto N_TAU_GRID uniform points (presentation grid)
    t_grid = np.linspace(t[0], t[-1], N_TAU_GRID)          # (local)
    H_g = np.interp(t_grid, t, H_t)                        # (local)
    qdev_g = np.interp(t_grid, t, q_dev_t)                 # (local)
    qenv_g = np.interp(t_grid, t, q_env_t)                 # (local)

    # tail = FULL final 50% of the (self-consistent) post-fold t-window
    t_half = t_grid[0] + 0.5 * (t_grid[-1] - t_grid[0])    # (local)
    tail_mask = t_grid >= t_half                           # (local)
    n_tail = int(tail_mask.sum())                          # (local) intended tail length

    # also restrict to the regime where the attractor is established:
    # require |H|/omega_q < 0.1 (adiabatic, cycle-averaging valid) on the tail.
    adia_ok_mask = (np.abs(H_g) / omega_q) < 0.1           # (local)
    gated_mask = tail_mask & adia_ok_mask                  # (local) the actually-used domain

    # --- GATED slope: ln q_dev vs ln|H| over the tail ---------------------
    slope_sc, icpt_sc, r2_sc, nu_sc, m_sc = loglog_fit(qdev_g, H_g, gated_mask)
    # --- DIAGNOSTIC slope: ln q_amp(envelope) vs ln|H| (annotation ii) ----
    slope_amp, icpt_amp, r2_amp, nu_amp, m_amp = loglog_fit(qenv_g, H_g, gated_mask)

    f_used = nu_sc / n_tail if n_tail > 0 else 0.0         # (local) domain_used_frac (GATED)
    lnH_range_tail = (float(np.log(np.max(np.abs(H_g[gated_mask])) /
                                   np.min(np.abs(H_g[gated_mask]))))
                      if nu_sc >= 2 else np.nan)           # (local)

    # --- coefficient-invariance (multiplicative-normalization cancellation) -
    q_dev_x = cycle_rms(qx_t - q_eq, tx, period)           # (local)
    t_grid_x = np.linspace(tx[0], tx[-1], N_TAU_GRID)      # (local)
    Hx_g = np.interp(t_grid_x, tx, Hx_t)                   # (local)
    qdevx_g = np.interp(t_grid_x, tx, q_dev_x)             # (local)
    tail_mask_x = t_grid_x >= (t_grid_x[0] + 0.5 * (t_grid_x[-1] - t_grid_x[0]))  # (local)
    gated_mask_x = tail_mask_x & ((np.abs(Hx_g) / omega_q) < 0.1)  # (local)
    slope_sc_x, _, _, _, _ = loglog_fit(qdevx_g, Hx_g, gated_mask_x)
    kappa_inv_dev = abs(slope_sc_x - slope_sc)             # (local)
    kappa_invariant = (kappa_inv_dev <= KAPPA_INV_TOL)     # (local)

    # --- amplitude-law consistency (annotation ii): slope_amp ~ slope_sc ~ 1 -
    amp_law_dev = abs(slope_amp - TARGET_SLOPE)            # (local)
    amp_sc_consistent = abs(slope_amp - slope_sc) <= 0.10  # (local) q_dev & q_amp agree
    # NEW-AMPLITUDE-ANOMALY only fires on a PASS where the envelope does NOT
    # track |H| (slope_amp far from 1) while the gated slope passes -- i.e.
    # slope 1 realized via secular q-bar drift, not q_amp ~ |H|.
    # evaluated below after magnitude verdict.

    # --- secular-drift diagnostic: is the mean q (not the amplitude) moving? -
    # coarse-grained mean of q over a sliding period; its slope vs |H| reveals
    # whether a q-bar drift is mimicking the amplitude law.
    qbar_t = np.array([float(np.mean((q_t - q_eq)[max(0, i - 50):i + 51]))
                       for i in range(len(t))])             # (local) running mean
    qbar_g = np.interp(t_grid, t, np.abs(qbar_t))           # (local)
    slope_qbar, _, _, _, _ = loglog_fit(qbar_g, H_g, gated_mask)

    # --- attractor check: does a ~ t^{2/3} establish? (w=0 dust) ----------
    # on the tail, fit ln a vs ln t -> exponent should approach 2/3.
    lna_g = np.interp(t_grid, t, lna_t)                    # (local) shifted ln a
    # rebuild absolute a from the integrated ln a (offset arbitrary; slope ok)
    mt = gated_mask & (t_grid > 0)                         # (local)
    if int(mt.sum()) >= 3:
        xt = np.log(t_grid[mt]); ya = lna_g[mt]            # (local)
        A2 = np.vstack([xt, np.ones_like(xt)]).T           # (local)
        cfa, *_ = np.linalg.lstsq(A2, ya, rcond=None)      # (local)
        a_exponent = float(cfa[0])                         # (local) -> 2/3 target
    else:
        a_exponent = np.nan                                # (local)
    a_exp_dev = abs(a_exponent - 2.0 / 3.0)                # (local)

    # --- H ~ (2/3) t^-1 check: slope of ln|H| vs ln t -> -1 ----------------
    if int(mt.sum()) >= 3:
        yh = np.log(np.abs(H_g[mt]))                       # (local)
        cfh, *_ = np.linalg.lstsq(np.vstack([np.log(t_grid[mt]),
                                             np.ones_like(t_grid[mt])]).T, yh, rcond=None)  # (local)
        H_t_exponent = float(cfh[0])                       # (local) -> -1 target
    else:
        H_t_exponent = np.nan                              # (local)

    # --- adiabaticity on the tail -----------------------------------------
    eps_ad = float(np.max(np.abs(H_g[gated_mask])) / omega_q) if nu_sc >= 1 else np.nan  # (local)
    adiabatic_ok = (eps_ad < 0.1) if np.isfinite(eps_ad) else False  # (local)

    # --- [SIGN] 3-tuple (pre-registered semantics) ------------------------
    # SIGN: self-consistent back-reaction co-tracks q-amplitude DOWN with H DOWN
    #       => predicted sign(slope) > 0 (q_dev shrinks as |H| shrinks).
    sign_verdict = "PASS" if (np.isfinite(slope_sc) and slope_sc > 0) else "FAIL"  # (local)
    # MAGNITUDE: |slope_sc - 1| vs PASS_BAND (0.05) / INFO_BAND (0.5)
    dev1 = abs(slope_sc - TARGET_SLOPE) if np.isfinite(slope_sc) else np.inf  # (local)
    if dev1 <= PASS_BAND:
        magnitude_verdict = "PASS"                         # (local)
    elif dev1 <= INFO_BAND:
        magnitude_verdict = "INFO"                         # (local)
    else:
        magnitude_verdict = "FAIL"                         # (local)
    # REGIME: auto-shortening bands on the FULL-tail fraction + solver health
    if (f_used >= F_VALID) and solver_ok:
        regime_verdict = "VALID"                           # (local)
    elif f_used >= F_MARGINAL:
        regime_verdict = "MARGINAL"                        # (local)
    else:
        regime_verdict = "BREAKDOWN"                       # (local)

    # composite collapse rule (gate-verdicts.md, verbatim)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                 # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                 # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                 # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                 # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                 # (local)
    else:
        composite = "PASS"                                 # (local)

    # NEW-AMPLITUDE-ANOMALY (annotation ii): only meaningful on a magnitude PASS
    new_amp_anomaly = (magnitude_verdict == "PASS") and (not amp_sc_consistent)  # (local)

    return dict(
        tau=tau, H_backbone=H_backbone, n_total=n_total,
        t=t, q_t=q_t, qd_t=qd_t, H_t=H_t, lna_t=lna_t,
        t_grid=t_grid, H_g=H_g, qdev_g=qdev_g, qenv_g=qenv_g, qbar_g=qbar_g,
        tail_mask=tail_mask, gated_mask=gated_mask, m_sc=m_sc, n_tail=n_tail,
        k_curv=k_curv, k_curv_w2=k_curv_w2, q_eq=q_eq, q_boundary=q_boundary,
        q0=q0, qd0=qd0, te=te, E_ic=E_ic, H_ic_target=H_ic_target, C3=C3,
        omega_q=omega_q, omega_npz=omega_npz, period=period, ode_maxstep=ODE_MAXSTEP,
        slope_sc=slope_sc, icpt_sc=icpt_sc, r2_sc=r2_sc, nu_sc=nu_sc,
        slope_amp=slope_amp, r2_amp=r2_amp, nu_amp=nu_amp,
        slope_sc_x=slope_sc_x, kappa_inv_dev=kappa_inv_dev, kappa_invariant=kappa_invariant,
        slope_qbar=slope_qbar, amp_law_dev=amp_law_dev, amp_sc_consistent=amp_sc_consistent,
        f_used=f_used, lnH_range_tail=lnH_range_tail,
        a_exponent=a_exponent, a_exp_dev=a_exp_dev, H_t_exponent=H_t_exponent,
        eps_ad=eps_ad, adiabatic_ok=adiabatic_ok,
        xc3_dev=xc3_dev, xc3_ok=xc3_ok,
        xc_omega_dev_plan=xc_omega_dev_plan, xc_omega_dev_npz=xc_omega_dev_npz, xc_omega_ok=xc_omega_ok,
        xc_kcurv_dev=xc_kcurv_dev, xc_kcurv_ok=xc_kcurv_ok,
        solver_ok=solver_ok, dev1=dev1, new_amp_anomaly=new_amp_anomaly,
        lnA_span_target=lnA_span_target,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        value=slope_sc,
    )


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(13.5, 9.5))     # (local)

    # (0,0) self-consistent q(t) + H(t)
    a = ax[0, 0]
    t = r["t"]                                            # (local)
    a.plot(t, r["q_t"] - r["q_eq"], "C3-", lw=0.5, label="q_osc(t) self-consistent")
    a.plot(t, np.interp(t, r["t_grid"], r["qdev_g"]),
           "k-", lw=1.2, label="cycle-RMS q_dev (GATED)")
    a.plot(t, r["H_t"], "C0-", lw=1.0, alpha=0.7, label="H(t) (Sec.6.3 closure)")
    a.set_xlabel("cosmic time t"); a.set_ylabel("q_osc, H")
    a.set_title("Self-consistent KV system: q drives H, H damps q (back-reaction)")
    a.legend(fontsize=7.5, loc="upper right")

    # (0,1) attractor: a ~ t^{2/3}, H ~ (2/3) t^-1
    b = ax[0, 1]
    tg = r["t_grid"]; mt = r["gated_mask"] & (tg > 0)     # (local)
    b.loglog(tg[mt], np.abs(r["H_g"][mt]), "C0.", ms=3, label="|H| (tail)")
    if np.isfinite(r["H_t_exponent"]):
        href = np.abs(r["H_g"][mt][0]) * (tg[mt] / tg[mt][0]) ** (-1.0)  # (local)
        b.loglog(tg[mt], href, "k--", lw=1.0, label="H ~ t^-1 (slope %.3f)" % r["H_t_exponent"])
    b.set_xlabel("ln t"); b.set_ylabel("ln|H|")
    b.set_title("Attractor: a-exponent = %.4f (target 2/3); H-t exponent = %.4f (target -1)"
                % (r["a_exponent"], r["H_t_exponent"]))
    b.legend(fontsize=7.5, loc="lower left")

    # (1,0) the GATED regression: ln q_dev vs ln|H|
    c = ax[1, 0]
    H_g = r["H_g"]; gm = r["gated_mask"]                  # (local)
    xg = np.log(np.abs(H_g[gm])); yg = np.log(r["qdev_g"][gm])  # (local)
    c.plot(xg, yg, "C3.", ms=3, label="q_dev (cycle-RMS), GATED")
    xl = np.linspace(xg.min(), xg.max(), 50)             # (local)
    c.plot(xl, r["slope_sc"] * xl + r["icpt_sc"], "C3-", lw=1.0,
           label="fit slope_selfcons = %.4f" % r["slope_sc"])
    # envelope diagnostic
    ye = np.log(r["qenv_g"][gm])                          # (local)
    c.plot(xg, ye, "C0.", ms=2, alpha=0.6, label="q_amp (envelope), DIAGNOSTIC")
    c.plot(xl, 1.0 * (xl - xl[0]) + yg.min(), "k:", lw=1.2, label="target slope = 1 (n=2 leg)")
    c.set_xlabel("ln|H|"); c.set_ylabel("ln q")
    c.set_title("GATED slope d ln q_dev/d ln|H| (amplitude-only, non-analytic-even cell)")
    c.legend(fontsize=7.5, loc="upper left")

    # (1,1) text panel
    d = ax[1, 1]; d.axis("off")
    txt = (
        "S101-W1-QEQ-SELFCONS  [SIGN]\n"
        "KV oscillation-energy self-consistency (Volovik Paper 25 §V 5.5a-b):\n"
        "  H^2 = (kappa^2/3) rho_q,  rho_q = (1/2)k_curv q_amp^2\n"
        "  rapid osc => w=0 dust => rho_q~a^-3 => a~t^{2/3}, H=(2/3)t^-1\n"
        "  => q_amp ~ t^-1 ~ |H|   (slope 1; non-analytic-even, clause f)\n\n"
        "slope_selfcons (GATED, q_dev) = %.6f   (target 1, band +/-0.05)\n"
        "|slope_selfcons - 1|          = %.6f   => magnitude %s\n"
        "slope_amp (DIAGNOSTIC, env)   = %.6f   (ann. ii; |amp-1|=%.4f)\n"
        "slope_qbar (secular-drift)    = %.6f   (anomaly guard)\n"
        "slope @ 10x closure-norm      = %.6f   (kappa-inv dev %.2e)\n"
        "a-exponent (t^p, w=0 dust)    = %.6f   (target 2/3, dev %.4f)\n"
        "H-t exponent                  = %.6f   (target -1)\n"
        "omega_q = sqrt(k_curv)        = %.4f   (plan pin 59.888)\n"
        "eps_ad = max|H|/omega_q       = %.3e  (adiabatic_ok=%s)\n"
        "domain_used_frac (GATED tail) = %.4f   => regime %s\n"
        "composite                     = %s%s\n\n"
        "Predecessor S100a-W1-2 (fixed-backbone drive): slope 2.0556 (H^2 wall).\n"
        "THIS gate: H is SELF-CONSISTENT (back-reaction), amplitude-only |H| cell."
        % (r["slope_sc"], r["dev1"], r["magnitude_verdict"],
           r["slope_amp"], r["amp_law_dev"], r["slope_qbar"],
           r["slope_sc_x"], r["kappa_inv_dev"],
           r["a_exponent"], r["a_exp_dev"], r["H_t_exponent"],
           r["omega_q"], r["eps_ad"], r["adiabatic_ok"],
           r["f_used"], r["regime_verdict"], r["composite"],
           "  [NEW-AMPLITUDE-ANOMALY]" if r["new_amp_anomaly"] else "")
    )
    d.text(0.02, 0.98, txt, va="top", ha="left", family="monospace", fontsize=8.0)

    fig.suptitle("S101 W4-1 -- KV oscillation-energy self-consistency: does d ln q/d ln|H|=1 EMERGE?",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Verdict payload (printed; the AGENT calls mcp__knowledge__emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }  # (local)
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
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    # per-gate identity keys embedded in the audit pinmap (sig_5 uniqueness)
    pins["_gate_id"] = GATE_ID
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_pass_band"] = str(PASS_BAND)
    pins["_info_band"] = str(INFO_BAND)
    pins["_ode"] = f"LSODA_rtol{ODE_RTOL}_atol{ODE_ATOL}_selfconsistent_Sec6.3_closure"
    audit_sha, content_sha = compute_dual_sha(
        _Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # ---- substitution chain with substituted numbers (stdout record) ------
    print("=== substitution chain (numbers substituted) ===")
    print(f"  Def1: q_eq = q* = {r['q_eq']:.4f} (interior equilibrium, s99_w2 q_star); k_curv = {r['k_curv']:+.4f}")
    print(f"  Def2: rho_q = (1/2)q_dot^2 + (1/2)k_curv(q-q*)^2;  omega_q = sqrt(k_curv) = {r['omega_q']:.4f} >> |H|")
    print(f"  Def3: Sec.6.3 closure H^2 = (kappa^2/3) rho_q;  C3 = kappa^2/3 = {r['C3']:.6e} (slope-INVARIANT pre-factor; a_0^{{zeta}}={a_0_FW_zeta})")
    print(f"  Def4: KV (Paper 25 §V): rapid osc -> w=0 dust -> rho_q~a^-3 -> a~t^{{2/3}}, H=(2/3)t^-1")
    print(f"  ICs (post-fold, s99_w2 window start te={r['te']}): q0 = {r['q0']:.6f}, q_dot0 = {r['qd0']:.6f}")
    print(f"  Substitute: (1/2)k_curv q_amp^2 ~ a^-3 ~ t^-2  =>  q_amp ~ t^-1 ~ |H|")
    print(f"  Canonical:  d ln q_amp/d ln|H| = 1")
    print(f"  REALIZED a-exponent = {r['a_exponent']:.6f} (target 2/3 = 0.6667, dev {r['a_exp_dev']:.4f})")
    print(f"  REALIZED slope_selfcons = {r['slope_sc']:.6f}  =>  n = 2 x {r['slope_sc']:.4f} = {2*r['slope_sc']:.4f}  (target n=2 needs slope 1)")
    print(f"  |slope_selfcons - 1| = {r['dev1']:.6f}  vs band {PASS_BAND} (PASS) / {INFO_BAND} (INFO)")
    print()
    print("=== cross-checks ===")
    print(f"  XC-3 k_curv npz vs plan pin |dev|             = {r['xc3_dev']:.6f}  ok={r['xc3_ok']}")
    print(f"  XC-omega realized sqrt(k_curv) vs plan 59.888 = {r['xc_omega_dev_plan']:.6f} (vs npz {r['xc_omega_dev_npz']:.2e})  ok={r['xc_omega_ok']}")
    print(f"  XC-kcurv drive-npz vs relax-npz k_curv |dev|  = {r['xc_kcurv_dev']:.3e}  ok={r['xc_kcurv_ok']}")
    print(f"  XC-kappa-inv  slope(10*C3) - slope(C3)        = {r['kappa_inv_dev']:.3e}  invariant={r['kappa_invariant']}  (slope_x={r['slope_sc_x']:.6f})")
    print(f"  XC-attractor  a-exponent dev from 2/3         = {r['a_exp_dev']:.6f}  (H-t exponent = {r['H_t_exponent']:.4f}, target -1)")
    print(f"  DIAGNOSTIC slope_amp (envelope, ann.ii)       = {r['slope_amp']:.6f}  |amp-1|={r['amp_law_dev']:.4f}  amp_sc_consistent={r['amp_sc_consistent']}")
    print(f"  ANOMALY-GUARD slope_qbar (secular drift)      = {r['slope_qbar']:.6f}  NEW-AMPLITUDE-ANOMALY={r['new_amp_anomaly']}")
    print(f"  adiabaticity eps_ad = max|H|/omega_q          = {r['eps_ad']:.3e}  adiabatic_ok={r['adiabatic_ok']}")
    print(f"  domain_used_frac (GATED tail) = {r['f_used']:.4f}; solver_ok = {r['solver_ok']}; lnH_range_tail = {r['lnH_range_tail']:.4f}")
    print()

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        regulator_pin="a_0^{zeta}",
        value=r["value"], slope_selfcons=r["slope_sc"], dev_from_1=r["dev1"],
        slope_amp=r["slope_amp"], slope_qbar=r["slope_qbar"], slope_selfcons_x10=r["slope_sc_x"],
        r2_selfcons=r["r2_sc"], r2_amp=r["r2_amp"],
        amp_law_dev=r["amp_law_dev"], amp_sc_consistent=r["amp_sc_consistent"],
        kappa_inv_dev=r["kappa_inv_dev"], kappa_invariant=r["kappa_invariant"],
        new_amplitude_anomaly=r["new_amp_anomaly"],
        a_exponent=r["a_exponent"], a_exp_dev=r["a_exp_dev"], H_t_exponent=r["H_t_exponent"],
        k_curv=r["k_curv"], k_curv_w2=r["k_curv_w2"], k_curv_plan_pin=K_CURV_PLAN_PIN,
        q_eq=r["q_eq"], q_boundary=r["q_boundary"], q0_ic=r["q0"], qd0_ic=r["qd0"],
        te_window_start=r["te"], E_ic=r["E_ic"], H_ic_target=r["H_ic_target"], C3=r["C3"],
        omega_q=r["omega_q"], omega_npz=r["omega_npz"], period=r["period"], ode_maxstep=r["ode_maxstep"],
        target_slope=TARGET_SLOPE, pass_band=PASS_BAND, info_band=INFO_BAND,
        n_total=r["n_total"], n_tail=r["n_tail"], n_used_selfcons=r["nu_sc"],
        domain_used_frac=r["f_used"], lnH_range_tail=r["lnH_range_tail"],
        eps_ad=r["eps_ad"], adiabatic_ok=r["adiabatic_ok"],
        xc3_dev=r["xc3_dev"], xc3_ok=r["xc3_ok"],
        xc_omega_dev_plan=r["xc_omega_dev_plan"], xc_omega_dev_npz=r["xc_omega_dev_npz"], xc_omega_ok=r["xc_omega_ok"],
        xc_kcurv_dev=r["xc_kcurv_dev"], xc_kcurv_ok=r["xc_kcurv_ok"],
        solver_ok=r["solver_ok"], lnA_span_target=r["lnA_span_target"],
        a_0_FW_zeta_used=a_0_FW_zeta,
        arr_tau_backbone=r["tau"], arr_H_backbone=r["H_backbone"],
        arr_t_grid=r["t_grid"], arr_H_g=r["H_g"], arr_qdev_g=r["qdev_g"],
        arr_qenv_g=r["qenv_g"], arr_qbar_g=r["qbar_g"], tail_mask=r["tail_mask"], gated_mask=r["gated_mask"],
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], composite=r["composite"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(r)
    print(f"saved: {OUT_NPZ.name}, {OUT_PNG.name}")

    # value string: NUMBERS first
    anomaly_tag = "_NEW-AMPLITUDE-ANOMALY" if r["new_amp_anomaly"] else ""  # (local)
    n2 = 2.0 * r["slope_sc"] if np.isfinite(r["slope_sc"]) else float("nan")  # (local)
    value_str = (
        f"slope_selfcons={r['slope_sc']:.6f}_dev1={r['dev1']:.6f}"
        f"_slope_amp={r['slope_amp']:.6f}_slope_qbar={r['slope_qbar']:.6f}"
        f"_a_exp={r['a_exponent']:.6f}(t2/3)_Htexp={r['H_t_exponent']:.4f}"
        f"_kappa_inv={r['kappa_invariant']}_domfrac={r['f_used']:.4f}"
        f"_n2tracking={n2:.4f}_kcurv={r['k_curv']:+.2f}_omega={r['omega_q']:.3f}"
        f"_amp_sc_consistent={r['amp_sc_consistent']}{anomaly_tag}"
    )  # (local)

    tag = (f"(value={r['slope_sc']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    print_verdict_payload(
        r["composite"], value_str, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note=("KV self-consistency H^2=(kappa^2/3)rho_q SELF-CONSISTENT (NOT fixed-backbone): "
                        "rapid osc->w=0 dust->rho_q~a^-3->a~t^{2/3}->q_amp~|H| (slope 1, non-analytic-even "
                        "clause-f cell). Predecessor S100a-W1-2 fixed-backbone drive = slope 2.0556 (H^2 wall)."),
        extra_rows=[
            f"# regulator_pin=a_0^{{zeta}} (a_0_FW_zeta={a_0_FW_zeta}; enters S_SA sector norm of Sec.6.3 closure C3={r['C3']:.4e}) # {GATE_ID}",
            f"# domain_used_frac={r['f_used']:.4f} n_tail={r['n_tail']} FULL-post-fold-final-50pct-tail; a-exponent={r['a_exponent']:.4f}(target 2/3) H-t-exp={r['H_t_exponent']:.4f}(target -1) # {GATE_ID}",
            f"# amplitude-law(ann.ii): slope_amp={r['slope_amp']:.6f} slope_qbar={r['slope_qbar']:.6f} amp_sc_consistent={r['amp_sc_consistent']} new_amplitude_anomaly={r['new_amp_anomaly']} # {GATE_ID}",
            f"# TAU0-L4-lift LANDED: this gate does NOT consume s84 cache; A19 conditional row N/A # {GATE_ID}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0  # exit 0 on ANY valid verdict (math-scripts.md exit-code semantics)


if __name__ == "__main__":
    sys.exit(main())
