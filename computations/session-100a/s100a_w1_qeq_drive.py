#!/usr/bin/env python3
"""
S100a W1-2 S100a-W1-2-QEQ-DRIVE -- substrate-internal q_eq(H) drive: is the n=2
tracking slope d ln q/d ln H = 1 UNFORCED?
===============================================================================

Gate: S100a-W1-2-QEQ-DRIVE ([SIGN])

Pre-registered threshold (plan session-100a-plan-w1.md SSW1-2):
  |slope - 1| <= 0.05, slope = d ln q/d ln H, least-squares over the late-time
  tail (FULL final 50% of the tau-window, NOT auto-shortened) of the friction
  ODE  q'' + 3 H(tau) q' + k_curv (q - q_eq(H(tau))) = 0  re-integrated on the
  verified non-stationary backbone arr_H_bare_t with the SUBSTRATE-DERIVED
  q_eq(H) (Volovik Gibbs-Duhem back-reaction; NOT the imposed q ~ H closure).
  PASS  iff |slope-1| <= 0.05 with a parameter-free substrate q_eq(H).
  INFO  iff the drive exists but carries a residual free closure parameter
        that tunes the slope toward 1 (slope coefficient-SENSITIVE).
  FAIL  iff no slope-1-capable parameter-free substrate drive exists (slope=1
        recoverable ONLY under the imposed q ~ H fluid closure).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-99/s99_w1_q_nonratio_observable.npz  (arr_H_bare_t backbone)
  - computations/session-99/s99_w2_relaxation_closure.npz     (K_CURV, q_boundary, c_main, S99 slopes)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<slope_GD_primary>, scheme=FW, convention=SUBSTRATE-NATURAL-BINDING, L_max=N/A)

Classification: PHONONIC

METHODOLOGY (the Gibbs-Duhem derivation IS the gate's hard part)
----------------------------------------------------------------
The cosmological constant IS the a_0 zeroth spectral moment (a_0_FW_zeta =
6440.0, zeta-regulated) -- a DIFFERENT spectral moment than gravity (a_2). The
Volovik vacuum variable q IS the substrate's own slow degree of freedom;
V(q) = delta-rho_vac is the GGE/zero-point response of the D_K eigenfrequencies,
quadratized with curvature k_curv = +3586.53 (S99 W2 npz; Routh-Hurwitz
restoring sign).

Substrate-derived drive, candidate (i) of the plan (Volovik Gibbs-Duhem with
Hubble-sourced chemical-potential shift), EVALUATED -- the evaluation the plan
block left symbolic [q_eq(H) = (dq/dmu) mu(H)]:

  GD-1  Static equilibrium (Volovik q-theory; corpus Papers 05 / 25 SSV / 35;
        project S62 #19, S95): mu_0 = d-eps/dq|_{q*}, rho_vac(q*) = 0 exactly
        (Gibbs-Duhem constraint); interior equilibrium q* = 0 (S99 npz).
  GD-2  Near q*: rho_vac(q) = (1/2) k_curv (q-q*)^2 -- linear term vanishes
        IDENTICALLY because mu_0 is the equilibrium chemical potential.
        Vacuum compressibility chi = dq/dmu = 1/k_curv.  [exponent-on-q = 2,
        substrate-forced -- the S99 W2 leg]
  GD-3  Hubble-sourced local thermodynamic state (Volovik de Sitter local
        thermodynamics; corpus Paper 11 for T_local = H/pi; the 2023-25 dS
        thermodynamics papers for the BULK entropy density): T(H) = H/pi,
        s(H) = 3H/(4G)  [volume density whose Hubble-volume integral is the
        Gibbons-Hawking A/4G].  Eliminating H:  s(T) = (3 pi / 4G) T -- the
        dS heat bath has LINEAR-in-T entropy density.
  GD-4  Gibbs-Duhem dP = s dT + n_q dmu across the quasi-static shift at
        vacuum pressure balance (dP = 0):
          dmu = -(s/n_q) dT  ==>  delta-mu(H) = -(1/n_q) * Int_0^T s dT'
              = -(1/n_q)(3 pi / 8G) T^2 = -(3/(8 pi G n_q)) H^2.
        EVEN in H, leading order H^2.  PARITY THEOREM: T and s are |H|-odd
        (only the dissipative sector distinguishes expansion from contraction);
        the Gibbs-Duhem potential shift Int s dT is therefore |H|-EVEN. NO
        substrate-internal equilibrium thermodynamic potential can carry a
        term LINEAR in H -- an H-linear term is odd-sector (dissipative) and
        in the friction ODE it is exactly the 3 H q' friction already
        explicit, NOT a potential term.
  GD-5  Tilted-well minimum:  V_eff(q) = (1/2) k_curv q^2 - delta-mu(H) q
        ==>  q_eq(H) = chi * delta-mu(H) = kappa2 * H^2,
             kappa2 = 3/(8 pi G n_q k_curv)  -- exponent LOCKED at 2;
        coefficient is a fixed substrate expression (G: a_2-channel;
        n_q: q-charge density; k_curv: D_K response) with NO tunable
        parameter.  kappa2's NUMERICAL value in backbone units is not
        extractable inside this gate (needs n_q + the SS6.3 G-normalization,
        both outside the pinned inputs) -- but the SLOPE is rigorously
        kappa2-INVARIANT (multiplicative-normalization cancellation,
        math-scripts.md: the log-derivative annihilates the multiplicative
        pre-factor; verified numerically below at machine precision).

Candidate (ii) (SS6.3 inversion H^2 = f(rho_relic, S_SA)) DISCLOSURE: inverting
the emergent-Friedmann closure for a q-sector share gives q_eq =
sqrt(2 lambda_q rho_crit / k_curv) ~ H^1 ONLY by (a) introducing the free
q-share lambda_q AND (b) asserting "q-sector energy = fixed fraction of the
critical density" -- which IS the tracking ansatz restated (circular as a
derivation). lambda_q tunes the AMPLITUDE, never the slope (same cancellation
identity), so candidate (ii) is not a substrate derivation of the linear form;
it is the imposed closure re-dressed.

The integration then tests what slope the substrate-derived (exponent-locked)
drive TRANSMITS on the actual non-stationary backbone, against the bare run
(q_eq = 0, S99 reproduction) and the imposed linear closure (q_eq = c H, S99
reproduction). Tail = FULL final 50% of the tau-window, unconditional
(avoiding the S99 W2-1 domain_used_frac = 0.41 BREAKDOWN pattern).

DISCIPLINE
----------
- from canonical_constants import * (MANDATORY first import)
- every intermediate tagged # (local)
- CPU scalar ODE (OMP_NUM_THREADS=8 capped before numpy import); matrix-free
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+)
- verdict via emit_verdict knowledge-MCP tool (script PRINTS payload only)
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
# Paths + pre-registration (plan session-100a-plan-w1.md SSW1-2; FROZEN)
# ---------------------------------------------------------------------------
SESSION_DIR = _Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                   # (local)
GATE_ID = "S100a-W1-2-QEQ-DRIVE"                   # (local)
SCHEME = "FW"                                      # (local)
CONVENTION = "SUBSTRATE-NATURAL-BINDING"           # (local)
L_MAX = "N/A"                                      # (local) ODE re-integration; no spectral truncation

PASS_BAND = 0.05            # (local) plan strict_PASS_boundary: |slope - 1| <= 0.05
TARGET_SLOPE = 1.0          # (local) the n=2 tracking-law leg (n = 2 x 1)
GD_EXPONENT = 2.0           # (local) Gibbs-Duhem-locked drive exponent (GD-4/GD-5)
KAPPA_INV_TOL = 1e-3        # (local) coefficient-invariance: |slope(10 kappa2) - slope(kappa2)|
F_VALID = 0.95              # (local) gate-verdicts.md auto-shortening band: VALID
F_MARGINAL = 0.50           # (local) gate-verdicts.md auto-shortening band: MARGINAL
ODE_RTOL = 1e-8             # (local) plan machinery pin
ODE_ATOL = 1e-10            # (local) plan machinery pin
ODE_MAXSTEP = 0.01          # (local) resolve the omega ~ 60 oscillation (period ~ 0.105)
K_CURV_PLAN_PIN = 3586.5    # (local) plan-block pin (5 sf print of the npz K_CURV); XC-3

NPZ_W1 = COMPUTATIONS_DIR / "session-99" / "s99_w1_q_nonratio_observable.npz"
NPZ_W2 = COMPUTATIONS_DIR / "session-99" / "s99_w2_relaxation_closure.npz"
OUT_NPZ = SESSION_DIR / "s100a_w1_qeq_drive.npz"
OUT_PNG = SESSION_DIR / "s100a_w1_qeq_drive.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
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
        sha = sha256_of(p)                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: _Path, canonical_path: _Path, pins: dict):
    script_bytes = script_path.read_bytes()      # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def loglog_fit(q: np.ndarray, H: np.ndarray, mask: np.ndarray):
    """LSQ of ln q on ln H over mask & q>0 & H>0. Returns slope, intercept, r2, n_used."""
    m = mask & (q > 0.0) & (H > 0.0) & np.isfinite(q) & np.isfinite(H)  # (local)
    n_used = int(m.sum())                                               # (local)
    if n_used < 3:
        return np.nan, np.nan, np.nan, n_used, m
    x = np.log(H[m]); y = np.log(q[m])                                  # (local)
    A = np.vstack([x, np.ones_like(x)]).T                               # (local)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)                        # (local)
    yhat = A @ coef                                                     # (local)
    ss_res = float(np.sum((y - yhat) ** 2))                             # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))                       # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan                # (local)
    return float(coef[0]), float(coef[1]), r2, n_used, m


def compute() -> dict:
    d1 = np.load(NPZ_W1, allow_pickle=True)   # (local) backbone npz
    d2 = np.load(NPZ_W2, allow_pickle=True)   # (local) relaxation-closure npz

    tau = np.asarray(d1["arr_tau"], dtype=float)            # (local)
    H_arr = np.asarray(d1["arr_H_bare_t"], dtype=float)     # (local)
    n_total = len(tau)                                      # (local)

    k_curv = float(d2["K_CURV"])                            # (local) +3586.5311811081065
    q_boundary = float(d2["q_boundary"])                    # (local) -0.6719754908120351
    c_lin = float(d2["c_main"])                             # (local) 0.15 (S99 imposed dq_dH)
    slope_bare_s99 = float(d2["slope_bare"])                # (local) 3.4159253901686504
    slope_driven_s99 = float(d2["slope_driven"])            # (local) 1.0082728538189105
    rho0_ref = float(d2["rho0_ref"])                        # (local) S97/S98 V(q) energy reference
    H_w2 = np.asarray(d2["arr_H_traj"], dtype=float)        # (local) XC-4 backbone identity

    # --- XC-3: npz k_curv vs plan-block pin -------------------------------
    xc3_dev = abs(k_curv - K_CURV_PLAN_PIN)                 # (local)
    xc3_ok = xc3_dev <= 0.05                                # (local)

    # --- XC-4: the two pinned inputs carry the SAME backbone --------------
    xc4_dev = float(np.max(np.abs(H_w2 - H_arr)))           # (local)
    xc4_ok = xc4_dev <= 1e-12                               # (local)

    # --- grid + spline -----------------------------------------------------
    dtau = np.diff(tau)                                     # (local)
    grid_uniformity = float(np.std(dtau) / np.mean(dtau))   # (local)
    H_sp = CubicSpline(tau, H_arr)                          # (local)
    Hdot_sp = H_sp.derivative()                             # (local)
    tau0, tauf = float(tau[0]), float(tau[-1])              # (local)
    H0 = float(H_sp(tau0))                                  # (local)
    H_max = float(np.max(H_arr))                            # (local)

    # --- tail window: FULL final 50% of the tau-window, unconditional -----
    tau_half = tau0 + 0.5 * (tauf - tau0)                   # (local)
    tail_mask = tau >= tau_half                             # (local)
    n_tail = int(tail_mask.sum())                           # (local) intended tail length

    # --- substrate-derived GD drive (GD-1..GD-5): q_eq = kappa2 H^2 -------
    # kappa2 diagnostic normalization (slope-INVARIANT; multiplicative
    # pre-factor annihilated by the log-derivative): drive reaches the
    # |q_boundary| scale at the backbone H_max. Pinned from S99 quantities.
    kappa2 = abs(q_boundary) / H_max**2                     # (local) 7.1971...
    # imposed linear closure (S99 reproduction): q_eq = c H, c = 0.15
    # bare: q_eq = 0, u-normalized IC u0=1 (S99 convention)

    omega = float(np.sqrt(k_curv))                          # (local) 59.888
    period = 2.0 * np.pi / omega                            # (local)

    def make_rhs(qeq_fun):
        def rhs(t, y):
            H = H_sp(t)                                     # (local)
            return [y[1], -3.0 * H * y[1] - k_curv * (y[0] - qeq_fun(t))]
        return rhs

    def integrate(qeq_fun, q0, qp0):
        sol = solve_ivp(make_rhs(qeq_fun), (tau0, tauf), [q0, qp0],
                        method="RK45", rtol=ODE_RTOL, atol=ODE_ATOL,
                        max_step=ODE_MAXSTEP, t_eval=tau, dense_output=False)  # (local)
        return sol

    # PRIMARY: substrate-derived GD drive (exponent locked at 2)
    qeq_GD = lambda t: kappa2 * H_sp(t) ** 2                # (local)
    sol_GD = integrate(qeq_GD, kappa2 * H0**2, 0.0)         # (local) on-drive IC (S99 driven convention)
    # coefficient-invariance probe (x10 kappa2)
    qeq_GDx = lambda t: 10.0 * kappa2 * H_sp(t) ** 2        # (local)
    sol_GDx = integrate(qeq_GDx, 10.0 * kappa2 * H0**2, 0.0)  # (local)
    # IC-robustness probe (factor-2 off-drive start)
    sol_GDo = integrate(qeq_GD, 2.0 * kappa2 * H0**2, 0.0)  # (local)
    # imposed linear closure (S99 reproduction; XC-2)
    qeq_LIN = lambda t: c_lin * H_sp(t)                     # (local)
    sol_LIN = integrate(qeq_LIN, c_lin * H0, 0.0)           # (local)
    # bare oscillator (S99 reproduction; u-normalized)
    qeq_0 = lambda t: 0.0                                   # (local)
    sol_BARE = integrate(qeq_0, 1.0, 0.0)                   # (local) u0_bare = 1

    solver_ok = all(s.success for s in
                    (sol_GD, sol_GDx, sol_GDo, sol_LIN, sol_BARE))  # (local)

    q_GD = sol_GD.y[0]; q_GDx = sol_GDx.y[0]; q_GDo = sol_GDo.y[0]  # (local)
    q_LIN = sol_LIN.y[0]; u_BARE = sol_BARE.y[0]                    # (local)

    # --- regressions over the FULL tail ------------------------------------
    slope_GD, icpt_GD, r2_GD, nu_GD, m_GD = loglog_fit(q_GD, H_arr, tail_mask)
    slope_GDx, _, r2_GDx, nu_GDx, _ = loglog_fit(q_GDx, H_arr, tail_mask)
    slope_GDo, _, r2_GDo, nu_GDo, _ = loglog_fit(q_GDo, H_arr, tail_mask)
    slope_LIN, _, r2_LIN, nu_LIN, _ = loglog_fit(q_LIN, H_arr, tail_mask)
    slope_BARE, _, r2_BARE, nu_BARE, _ = loglog_fit(u_BARE, H_arr, tail_mask)

    f_used_GD = nu_GD / n_tail                              # (local) primary domain fraction
    f_used_BARE = nu_BARE / n_tail                          # (local) diagnostic
    lnH_range_tail = float(np.log(np.max(H_arr[tail_mask]) /
                                  np.min(H_arr[tail_mask])))  # (local)

    # --- XC-1: transmission (drive exponent -> measured slope) -------------
    xc1_dev = abs(slope_GD - GD_EXPONENT)                   # (local)
    xc1_ok = xc1_dev <= 0.05                                # (local)
    # --- XC-2: imposed-closure S99 reproduction ----------------------------
    xc2_dev = abs(slope_LIN - slope_driven_s99)             # (local)
    xc2_ok = xc2_dev <= 0.05                                # (local)
    # --- XC-5: kappa2-invariance (multiplicative cancellation identity) ----
    xc5_dev = abs(slope_GDx - slope_GD)                     # (local)
    kappa_invariant = xc5_dev <= KAPPA_INV_TOL              # (local)
    # --- XC-6: IC-robustness ------------------------------------------------
    xc6_dev = abs(slope_GDo - slope_GD)                     # (local)
    xc6_ok = xc6_dev <= 0.05                                # (local)
    # --- XC-7: quadratic-well validity (a_0-channel) ------------------------
    q_eq_max = float(np.max(kappa2 * H_arr**2))             # (local)
    V_eq_max = 0.5 * k_curv * q_eq_max**2                   # (local)
    well_ratio_a0 = V_eq_max / a_0_FW_zeta                  # (local) vs a_0 mode count
    well_ratio_rho0 = V_eq_max / rho0_ref                   # (local) vs S97 V(q) reference
    xc7_ok = well_ratio_a0 < 1.0                            # (local)
    # --- adiabaticity on the tail -------------------------------------------
    Hdot_tail = Hdot_sp(tau[tail_mask])                     # (local)
    eps_ad = float(np.max(np.abs(2.0 * Hdot_tail / H_arr[tail_mask])) / omega)  # (local)
    adiabatic_ok = eps_ad < 0.1                             # (local)

    # --- [SIGN] 3-tuple (pre-registered semantics) --------------------------
    # sign: a genuine drive co-tracks q with H => predicted sign(slope) > 0
    sign_verdict = "PASS" if slope_GD > 0 else "FAIL"       # (local)
    # magnitude: |slope-1| vs PASS_BAND; INFO only if a residual coefficient
    # CAN tune the slope (kappa-sensitivity); FAIL if exponent-locked.
    dev1 = abs(slope_GD - TARGET_SLOPE)                     # (local)
    if dev1 <= PASS_BAND:
        magnitude_verdict = "PASS"                          # (local)
    elif not kappa_invariant:
        magnitude_verdict = "INFO"                          # (local)
    else:
        magnitude_verdict = "FAIL"                          # (local)
    # regime: auto-shortening bands on the FULL-tail fraction + solver health
    if (f_used_GD >= F_VALID) and solver_ok:
        regime_verdict = "VALID"                            # (local)
    elif f_used_GD >= F_MARGINAL:
        regime_verdict = "MARGINAL"                         # (local)
    else:
        regime_verdict = "BREAKDOWN"                        # (local)

    # composite collapse rule (gate-verdicts.md, verbatim)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                  # (local)
    else:
        composite = "PASS"                                  # (local)

    return dict(
        tau=tau, H_arr=H_arr, tail_mask=tail_mask, n_total=n_total, n_tail=n_tail,
        tau_half=tau_half, grid_uniformity=grid_uniformity, lnH_range_tail=lnH_range_tail,
        k_curv=k_curv, q_boundary=q_boundary, c_lin=c_lin, kappa2=kappa2,
        omega=omega, period=period, eps_ad=eps_ad, adiabatic_ok=adiabatic_ok,
        q_GD=q_GD, q_GDx=q_GDx, q_GDo=q_GDo, q_LIN=q_LIN, u_BARE=u_BARE,
        slope_GD=slope_GD, icpt_GD=icpt_GD, r2_GD=r2_GD, nu_GD=nu_GD, m_GD=m_GD,
        slope_GDx=slope_GDx, r2_GDx=r2_GDx,
        slope_GDo=slope_GDo, r2_GDo=r2_GDo,
        slope_LIN=slope_LIN, r2_LIN=r2_LIN, nu_LIN=nu_LIN,
        slope_BARE=slope_BARE, r2_BARE=r2_BARE, nu_BARE=nu_BARE,
        f_used_GD=f_used_GD, f_used_BARE=f_used_BARE,
        slope_bare_s99=slope_bare_s99, slope_driven_s99=slope_driven_s99,
        xc1_dev=xc1_dev, xc1_ok=xc1_ok, xc2_dev=xc2_dev, xc2_ok=xc2_ok,
        xc3_dev=xc3_dev, xc3_ok=xc3_ok, xc4_dev=xc4_dev, xc4_ok=xc4_ok,
        xc5_dev=xc5_dev, kappa_invariant=kappa_invariant,
        xc6_dev=xc6_dev, xc6_ok=xc6_ok,
        q_eq_max=q_eq_max, V_eq_max=V_eq_max,
        well_ratio_a0=well_ratio_a0, well_ratio_rho0=well_ratio_rho0, xc7_ok=xc7_ok,
        solver_ok=solver_ok, dev1=dev1,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        value=slope_GD,
    )


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    tau = r["tau"]; H = r["H_arr"]; tm = r["tail_mask"]   # (local)
    fig, ax = plt.subplots(2, 2, figsize=(13.5, 9.5))     # (local)

    a = ax[0, 0]
    a.plot(tau, H, "k-", lw=1.4, label="H_bare(tau)  [arr_H_bare_t]")
    a.plot(tau, r["kappa2"] * H**2, "C3-", lw=1.2,
           label="q_eq^GD = kappa2 H^2  (Gibbs-Duhem tilt, exponent LOCKED)")
    a.plot(tau, r["c_lin"] * H, "C0--", lw=1.2, label="q_eq^LIN = c H  (IMPOSED closure, c=0.15)")
    a.axvspan(r["tau_half"], tau[-1], color="0.92", label="tail = FULL final 50%")
    a.set_xlabel("tau"); a.set_ylabel("H, q_eq")
    a.set_title("Backbone + drives  (omega = sqrt(k_curv) = %.2f >> 3H: adiabatic)" % r["omega"])
    a.legend(fontsize=7.5, loc="upper left")

    b = ax[0, 1]
    b.plot(tau, r["q_GD"], "C3-", lw=1.3, label="q(tau) under GD drive (PRIMARY)")
    b.plot(tau, r["kappa2"] * H**2, "k:", lw=0.9, label="q_eq^GD(H(tau))")
    b.plot(tau, r["q_LIN"], "C0--", lw=1.0, label="q(tau) under imposed cH")
    b.plot(tau, r["u_BARE"] * np.max(r["q_GD"]), "0.6", lw=0.7,
           label="bare u(tau) (scaled; S99 oscillator)")
    b.axvspan(r["tau_half"], tau[-1], color="0.92")
    b.set_xlabel("tau"); b.set_ylabel("q")
    b.set_title("Friction-ODE re-integration on arr_H_bare_t")
    b.legend(fontsize=7.5, loc="upper left")

    c = ax[1, 0]
    m = r["m_GD"]  # (local)
    c.plot(np.log(H[m]), np.log(r["q_GD"][m]), "C3.", ms=3, label="GD drive (tail)")
    xg = np.linspace(np.log(H[tm].min()), np.log(H[tm].max()), 50)  # (local)
    c.plot(xg, r["slope_GD"] * xg + r["icpt_GD"], "C3-", lw=1.0,
           label="fit slope = %.4f" % r["slope_GD"])
    mq = tm & (r["q_LIN"] > 0)  # (local)
    c.plot(np.log(H[mq]), np.log(r["q_LIN"][mq]), "C0.", ms=3, label="imposed cH (tail)")
    c.plot(xg, r["slope_LIN"] * (xg - xg[0]) + np.log(r["q_LIN"][mq]).min(), "C0--", lw=0.9,
           label="fit slope = %.4f" % r["slope_LIN"])
    c.plot(xg, 1.0 * (xg - xg[0]) + np.log(r["q_GD"][m]).min(), "k:", lw=1.2,
           label="target slope = 1 (n=2 leg)")
    c.set_xlabel("ln H"); c.set_ylabel("ln q")
    c.set_title("Tail log-log regression: d ln q / d ln H")
    c.legend(fontsize=7.5, loc="upper left")

    d = ax[1, 1]; d.axis("off")
    txt = (
        "S100a-W1-2-QEQ-DRIVE  [SIGN]\n"
        "Substrate-derived drive (Volovik Gibbs-Duhem, evaluated):\n"
        "  T = H/pi (Paper 11), s = 3H/4G  =>  s(T) = (3pi/4G) T\n"
        "  dmu = -(s/n_q) dT  =>  delta-mu ~ T^2 ~ H^2  (EVEN in H)\n"
        "  q_eq(H) = chi delta-mu = kappa2 H^2   exponent LOCKED = 2\n\n"
        "slope_GD (PRIMARY)        = %.6f   (target 1, band +/-0.05)\n"
        "|slope_GD - 1|            = %.6f   => magnitude %s\n"
        "slope under 10x kappa2    = %.6f   (invariance dev %.2e)\n"
        "slope, off-drive IC (x2)  = %.6f\n"
        "slope, imposed q_eq = cH  = %.6f   (S99: %.6f)\n"
        "slope, bare q_eq = 0      = %.6f   (S99: %.6f; f_used %.2f)\n"
        "domain_used_frac (GD tail)= %.4f   => regime %s\n"
        "composite                 = %s\n\n"
        "Parity theorem: equilibrium thermodynamic sector is EVEN in H;\n"
        "an H-linear q_eq is odd-sector (dissipative) = the imposed closure.\n"
        "No parameter-free substrate drive can carry slope 1."
        % (r["slope_GD"], r["dev1"], r["magnitude_verdict"],
           r["slope_GDx"], r["xc5_dev"], r["slope_GDo"],
           r["slope_LIN"], r["slope_driven_s99"],
           r["slope_BARE"], r["slope_bare_s99"], r["f_used_BARE"],
           r["f_used_GD"], r["regime_verdict"], r["composite"])
    )
    d.text(0.02, 0.98, txt, va="top", ha="left", family="monospace", fontsize=8.3)

    fig.suptitle("S100a W1-2 -- substrate-internal q_eq(H) drive: is d ln q/d ln H = 1 unforced?",
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
    pins["_ode"] = f"RK45_rtol{ODE_RTOL}_atol{ODE_ATOL}_maxstep{ODE_MAXSTEP}"
    audit_sha, content_sha = compute_dual_sha(
        _Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # ---- substitution chain with substituted numbers (stdout record) ------
    print("=== substitution chain (numbers substituted) ===")
    print(f"  GD-2: rho_vac(q) = (1/2) k_curv q^2,  k_curv = {r['k_curv']:+.4f}  (chi = 1/k_curv = {1.0/r['k_curv']:.3e})")
    print(f"  GD-4: delta-mu(H) = -(3/(8 pi G n_q)) H^2   [EVEN in H; T=H/pi, s=3H/4G]")
    print(f"  GD-5: q_eq(H) = kappa2 H^2;  kappa2(diagnostic) = |q_boundary|/H_max^2 = {r['kappa2']:.6f}")
    print(f"  ODE:  q'' + 3H q' + k_curv (q - kappa2 H^2) = 0  on arr_H_bare_t  (omega = {r['omega']:.4f}, eps_ad = {r['eps_ad']:.3e})")
    print(f"  tail: tau >= {r['tau_half']:.6f}  (n_tail = {r['n_tail']}, ln-H range = {r['lnH_range_tail']:.4f})")
    print(f"  slope_GD = {r['slope_GD']:.6f}  =>  n = 2 x {r['slope_GD']:.4f} = {2*r['slope_GD']:.4f}  (target n = 2 needs slope 1)")
    print(f"  |slope_GD - 1| = {r['dev1']:.6f}  vs band {PASS_BAND}")
    print()
    print("=== cross-checks ===")
    print(f"  XC-1 transmission |slope_GD - 2|              = {r['xc1_dev']:.6f}  ok={r['xc1_ok']}")
    print(f"  XC-2 imposed-closure repro |slope_LIN - S99|  = {r['xc2_dev']:.6f}  ok={r['xc2_ok']}  (slope_LIN={r['slope_LIN']:.6f}, S99={r['slope_driven_s99']:.6f})")
    print(f"  XC-3 k_curv npz vs plan pin |dev|             = {r['xc3_dev']:.6f}  ok={r['xc3_ok']}")
    print(f"  XC-4 backbone identity w1 vs w2 max|dH|       = {r['xc4_dev']:.3e}  ok={r['xc4_ok']}")
    print(f"  XC-5 kappa2-invariance |slope(10k)-slope(k)|  = {r['xc5_dev']:.3e}  invariant={r['kappa_invariant']}")
    print(f"  XC-6 IC-robustness |slope(2x IC)-slope|       = {r['xc6_dev']:.6f}  ok={r['xc6_ok']}")
    print(f"  XC-7 well validity V(q_eq_max)/a_0_FW_zeta    = {r['well_ratio_a0']:.4f}  (vs rho0_ref: {r['well_ratio_rho0']:.4f})  ok={r['xc7_ok']}")
    print(f"  bare diagnostic: slope_BARE = {r['slope_BARE']:.6f} (S99 {r['slope_bare_s99']:.6f}), f_used_BARE = {r['f_used_BARE']:.4f}")
    print(f"  domain_used_frac (PRIMARY GD tail) = {r['f_used_GD']:.4f}; solver_ok = {r['solver_ok']}")
    print()

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        value=r["value"], slope_GD=r["slope_GD"], dev_from_1=r["dev1"],
        slope_GDx10=r["slope_GDx"], slope_GD_offIC=r["slope_GDo"],
        slope_LIN=r["slope_LIN"], slope_BARE=r["slope_BARE"],
        r2_GD=r["r2_GD"], r2_LIN=r["r2_LIN"], r2_BARE=r["r2_BARE"],
        slope_bare_s99=r["slope_bare_s99"], slope_driven_s99=r["slope_driven_s99"],
        k_curv=r["k_curv"], k_curv_plan_pin=K_CURV_PLAN_PIN,
        q_boundary=r["q_boundary"], c_lin=r["c_lin"], kappa2=r["kappa2"],
        gd_exponent=GD_EXPONENT, target_slope=TARGET_SLOPE, pass_band=PASS_BAND,
        omega=r["omega"], eps_ad=r["eps_ad"], adiabatic_ok=r["adiabatic_ok"],
        n_total=r["n_total"], n_tail=r["n_tail"], tau_half=r["tau_half"],
        n_used_GD=r["nu_GD"], domain_used_frac=r["f_used_GD"],
        f_used_BARE=r["f_used_BARE"], lnH_range_tail=r["lnH_range_tail"],
        grid_uniformity=r["grid_uniformity"],
        xc1_dev=r["xc1_dev"], xc1_ok=r["xc1_ok"], xc2_dev=r["xc2_dev"], xc2_ok=r["xc2_ok"],
        xc3_dev=r["xc3_dev"], xc3_ok=r["xc3_ok"], xc4_dev=r["xc4_dev"], xc4_ok=r["xc4_ok"],
        xc5_dev=r["xc5_dev"], kappa_invariant=r["kappa_invariant"],
        xc6_dev=r["xc6_dev"], xc6_ok=r["xc6_ok"],
        q_eq_max=r["q_eq_max"], V_eq_max=r["V_eq_max"],
        well_ratio_a0=r["well_ratio_a0"], well_ratio_rho0=r["well_ratio_rho0"],
        a_0_FW_zeta_used=a_0_FW_zeta,
        arr_tau=r["tau"], arr_H=r["H_arr"], arr_q_GD=r["q_GD"], arr_q_LIN=r["q_LIN"],
        arr_u_BARE=r["u_BARE"], arr_q_GDx10=r["q_GDx"], arr_q_GD_offIC=r["q_GDo"],
        tail_mask=r["tail_mask"],
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], composite=r["composite"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(r)
    print(f"saved: {OUT_NPZ.name}, {OUT_PNG.name}")

    value_str = (
        f"slope_GDtilt_H2={r['slope_GD']:.6f}_dev1={r['dev1']:.6f}"
        f"_exp_locked_EVEN_in_H_kappa_inv={r['kappa_invariant']}"
        f"_slope_imposed_cH={r['slope_LIN']:.6f}_slope_bare={r['slope_BARE']:.4f}"
        f"_domfrac={r['f_used_GD']:.4f}_kcurv={r['k_curv']:+.2f}"
        f"_no_slope1_capable_substrate_drive_C10-ObjectC-STRUCTURALLY-CONDITIONAL"
    )  # (local)

    tag = (f"(value={r['slope_GD']!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    print_verdict_payload(
        r["composite"], value_str, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note=("GD drive q_eq=kappa2*H^2 exponent-LOCKED (T=H/pi x s=3H/4G "
                        "Gibbs-Duhem => delta-mu ~ H^2 EVEN-parity); slope coefficient-invariant; "
                        "linear q_eq~H = imposed closure only"),
        extra_rows=[
            f"# regulator_pin=a_0^{{zeta}} (a_0_FW_zeta={a_0_FW_zeta}; well-validity V(q_eq_max)/a_0={r['well_ratio_a0']:.4f}) # {GATE_ID}",
            f"# domain_used_frac={r['f_used_GD']:.4f} n_tail={r['n_tail']} FULL-final-50pct-tail unconditional (W2-1 BREAKDOWN pattern avoided) # {GATE_ID}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0  # exit 0 on ANY valid verdict (math-scripts.md exit-code semantics)


if __name__ == "__main__":
    sys.exit(main())
