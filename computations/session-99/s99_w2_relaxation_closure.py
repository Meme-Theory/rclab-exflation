#!/usr/bin/env python3
"""
S99 W2-RELAXATION-CLOSURE -- Volovik tracking-vacuum friction-ODE attractor (C10 Object-C)
==========================================================================================

Gate: S99-W2-RELAXATION-CLOSURE ([SIGN])

Pre-registered threshold:
  |slope_attractor - 1.0| <= 0.05  where slope_attractor = d ln q / d ln H from a
  log-log regression on the late-time (post-transient) attractor window of the
  friction-ODE solution q(tau).
  PASS iff |slope - 1| <= 0.05 emerges UNFORCED (no slow-roll quasi-static relation
  imposed). INFO iff 0.05 < |slope - 1| <= 0.10. FAIL iff |slope - 1| > 0.10 OR
  regime_verdict == BREAKDOWN (attractor window > 50% shortened, domain_used_frac < 0.50).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-99/s99_w1_q_nonratio_observable.npz   (W1-1 NON-stationary H(tau) backbone; HARD upstream)
  - computations/session-98/s98_w2_2_relaxation_closure.npz    (S98 V.2; V(q) pins: k_curv, q_boundary, q0/rho0)
  - computations/session-97/s97_w2_2_c10_n_exponent.npz        (S97; V(q) shape, omega_n(q), n=2 baseline)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<slope_attractor>, scheme=FW, convention=ABSOLUTE, L_max=12)

Classification: PHONONIC

METHODOLOGY
-----------
The cosmological constant IS the spectral-action zeroth moment a_0 (a_0_FW_zeta=6440.0,
zeta-regulated) -- a DIFFERENT spectral moment than gravity (a_2). The Volovik vacuum
variable q IS the substrate's own slow degree of freedom; V(q) = delta-rho_vac is the GGE /
zero-point vacuum-energy response of the 992 D_K eigenfrequencies omega_n(q)=sqrt(lambda_n^2+q),
quadratized about q* with curvature k_curv (= |d2E/dq2|_0 in restoring-well sign convention).
We integrate the SUBSTRATE cosmological-friction ODE
        q'' + 3 H(tau) q' + V'(q) = 0,   V'(q) = k_curv (q - q*),
along the W1-1 NON-conformally-stationary substrate Hubble backbone H(tau) (the AOFT acoustic
frame from S98 V.1 is conformally STATIONARY -- a_eff rel-var 7.4e-7 -- and CANNOT serve; it
degenerated the S98 V.2 predecessor to PRE-REG-INC). We do NOT impose the slow-roll quasi-static
relation q' = -V'/(3H); we integrate the full 2nd-order STIFF ODE (scipy solve_ivp Radau,
rtol=1e-10, atol=1e-12). The late-time attractor slope d ln q/d ln H is extracted by a log-log
linear regression on the post-transient tail (transient end where |q''|/|3H q'| < 0.01;
window >= 50% of the trajectory). The analytic target is slope = n/2 with n=2 (the quadratic-V
Volovik tracking law => rho_vac ~ q^2 ~ H^2 => q ~ H^1), i.e. slope = 1 EXACTLY on the attractor.

SIGN RESOLUTION (k_curv): the raw second derivative of ENERGY d2E/dq2|_0 = -3586.53 is negative
in the energy convention; the RESTORING-FORCE curvature entering V'(q)=k_curv(q-q*) is the
POSITIVE |k_curv| = +3586.53. Routh-Hurwitz on the linearized friction ODE delta''+3H delta'+
k_curv delta=0 (Sage-verified): k_curv>0 => both characteristic roots have Re<0 => damped
oscillatory ATTRACTOR; k_curv<0 => one root Re>0 => REPELLER => slope diverges => FAIL by
construction. The convex restoring well (+|k_curv|) is the UNIQUE sign admitting a tracking
attractor. We integrate against +|k_curv| and report the slope honestly against the band.

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY first import)
- every intermediate tagged `# (local)`
- CPU-only stiff ODE (OMP_NUM_THREADS=8 capped before numpy import); the 992 omega_n(q) are
  precomputed from the L_max=12 cache (loaded from S97 npz); no large dense linalg
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- [SIGN] gate: payload carries sign/magnitude/regime 3-tuple (all-three-or-none)
- verdict emitted via emit_verdict MCP tool (script PRINTS payload; agent calls the tool)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# Scripts live at computations/session-N/; put computations/_shared on sys.path
# so `from canonical_constants import *` resolves (per session-98/99 precedent).
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports (CPU threads capped above, BEFORE numpy)
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S99"                                                   # (local)
GATE_ID = "S99-W2-RELAXATION-CLOSURE"                             # (local)
SCHEME = "FW"                                                     # (local)
CONVENTION = "ABSOLUTE"                                           # (local)
L_MAX = 12                                                        # (local)

# Pre-registered gate bands (define BEFORE running) -- math-scripts.md / plan W2-1
PASS_BAND = 0.05                                                  # (local) |slope-1| <= 0.05 => PASS
INFO_BAND = 0.10                                                  # (local) 0.05 < |slope-1| <= 0.10 => INFO
TARGET_SLOPE = 1.0                                               # (local) = n/2 with n=2 (Volovik Gibbs-Duhem)
TRANSIENT_RATIO = 0.01                                            # (local) transient end: |q''|/|3H q'| < 0.01
MIN_WINDOW_FRAC = 0.50                                            # (local) attractor window >= 50% of trajectory
RTOL = 1e-10                                                      # (local) Radau rtol
ATOL = 1e-12                                                      # (local) Radau atol

# Input npz paths
NPZ_W1 = SESSION_DIR / "s99_w1_q_nonratio_observable.npz"         # (local) HARD upstream H(tau) backbone
NPZ_S98 = COMPUTATIONS_DIR / "session-98" / "s98_w2_2_relaxation_closure.npz"   # (local) V(q) pins
NPZ_S97 = COMPUTATIONS_DIR / "session-97" / "s97_w2_2_c10_n_exponent.npz"       # (local) V(q) shape

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s99_w2_relaxation_closure.npz"
OUT_PNG = SESSION_DIR / "s99_w2_relaxation_closure.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    NPZ_W1,
    NPZ_S98,
    NPZ_S97,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
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
# Section 5 -- Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Integrate q'' + 3H(tau)q' + V'(q)=0 along the W1-1 H(tau) backbone;
    extract the late-time attractor slope d ln q/d ln H by log-log regression."""

    # --- Load the W1-1 NON-stationary H(tau) backbone (HARD upstream) ---
    dw1 = np.load(NPZ_W1, allow_pickle=True)  # (local)
    tau = np.asarray(dw1["arr_tau"], dtype=float)          # (local) monotone-increasing time
    H_t = np.asarray(dw1["arr_H_bare_t"], dtype=float)     # (local) NON-stationary substrate H(tau)
    a_t = np.asarray(dw1["arr_a_bare_t"], dtype=float)     # (local) bare scale factor (for e-folds)
    aeff_relvar = float(dw1["aeff_relvar"])                # (local) AOFT conformal-stationary floor 7.4e-7
    H_nonstat_relvar = float(dw1["H_bare_nonstationarity_relvar"])  # (local) backbone non-stationarity
    H_all_positive = bool(dw1["H_bare_all_positive"])      # (local)

    # Guard: the backbone MUST be non-conformally-stationary (the W1->W2 decision-point premise)
    if not (H_all_positive and np.all(np.isfinite(H_t)) and H_nonstat_relvar > 10.0 * aeff_relvar):
        raise RuntimeError("W1-1 backbone failed non-stationarity guard -- "
                           "should have triggered PRE-REG-INC closure upstream.")

    # --- Load V(q) pins ---
    # k_curv: SIGN RESOLVED to the POSITIVE restoring-well curvature. The raw
    # d2E/dq2|_0 in the npz is negative (energy convention); we take |k_curv|
    # (the convex restoring-force curvature) -- the unique sign admitting an attractor.
    d98 = np.load(NPZ_S98, allow_pickle=True)  # (local)
    d97 = np.load(NPZ_S97, allow_pickle=True)  # (local)
    k_curv_raw_98 = float(d98["cf_s99_k_curv"])            # (local) S98 raw (energy convention, -3586.53)
    k_curv_raw_97 = float(d97["d2E_dq2_0"])                # (local) S97 raw d2E/dq2 (-3586.53)
    k_curv_pos_97 = float(d97["k_curv"])                   # (local) S97 restoring-well |curv| (+3586.53)
    q_boundary = float(d98["cf_s99_q_boundary"])           # (local) -0.67197549 (lam_sq_min boundary)
    q0_ref = float(d97["q0_ref"])                          # (local) expansion point (0.0)
    rho0_ref = float(d97["rho0_ref"])                      # (local) reference vacuum energy

    # Resolve the restoring-well curvature: |k_curv|; cross-check against the +3586.5 pin.
    K_CURV = abs(k_curv_raw_98)                             # (local) +3586.53 (convex restoring well)
    sign_consistent = (np.sign(k_curv_pos_97) > 0
                       and np.sign(k_curv_raw_98) < 0
                       and np.sign(k_curv_raw_97) < 0
                       and abs(K_CURV - 3586.5) < 1.0)      # (local) pin cross-check
    K_CURV_PINNED = 3586.5                                 # (local) plan PIN value

    # The tracking fixed point q*: the substrate vacuum sits at the energy-minimum /
    # boundary. With q0_ref the quadratization point and q_boundary the lam_sq_min
    # floor, q* is the energy-minimum the friction relaxes toward. Use q0_ref as the
    # quadratization centre (V'(q)=k_curv(q-q*)); q* = q0_ref = 0.0 (the substrate
    # reference vacuum). The relaxation starts displaced and tracks toward q*.
    q_star = q0_ref                                        # (local) tracking fixed point (0.0)

    # --- The 992 omega_n(q) eigenfrequencies (precomputed L_max=12 cache; informational) ---
    omega_s = np.asarray(d97["omega_s"], dtype=float)      # (local) 992 eigenfrequencies (sqrt(lam^2+q))
    n_omega = int(omega_s.size)                            # (local) 992

    # --- Build a smooth H(tau) interpolant for the ODE friction coefficient ---
    # H enters as the time-dependent friction 3H(tau). solve_ivp samples tau between
    # grid points, so we linearly interpolate H(tau) (the export grid is dense, 999 pts).
    tau0, tauf = float(tau[0]), float(tau[-1])             # (local)

    def H_of(t: float) -> float:                           # (local) H(tau) interpolant
        return float(np.interp(t, tau, H_t))

    # The S97 equilibrium-tracking proportionality (q_eq = c*H), where c = q_ref/H_ref =
    # dq_dH. THIS IS THE IMPOSED LINEAR SLOW-ROLL CLOSURE (S97 lines 419-483: "q_of_H =
    # q_ref*H/H_ref ... LINEAR slow-roll closure / simple-fluid input"). It is NOT a
    # substrate-derived relation: the substrate gives rho_vac(eq)=0 (Gibbs-Duhem, S95
    # EQUILIBRIUM-CC-WARRANT) and q=0 as the ONLY interior equilibrium (S62 Monotonicity #19).
    dq_dH = float(d97["dq_dH"])                            # (local) 0.15 -- the IMPOSED linear-closure slope

    t_eval = tau                                           # (local) 999-point output grid (matches backbone)

    # ===================================================================
    # INTEGRATION A -- BARE SUBSTRATE static well (UNFORCED; the gate's PRIMARY value)
    # q'' + 3H q' + k_curv*(q - q*) = 0 with q* = 0 const, NO imposed H-drive.
    # This is the substrate's OWN relaxation: a damped oscillator about q=0. There is NO
    # substrate-derived H-dependent equilibrium (rho_vac(eq)=0; q=0 the only interior fixed
    # point). The attractor slope d ln q/d ln H from THIS bare ODE is the UNFORCED answer.
    # ===================================================================
    def rhs_bare(t, y):                                    # (local)
        u, up = y                                          # (local) u = q - q*
        Ht = H_of(t)                                       # (local)
        return [up, -3.0 * Ht * up - K_CURV * u]           # restoring, k_curv>0

    def jac_bare(t, y):                                    # (local)
        return [[0.0, 1.0], [-K_CURV, -3.0 * H_of(t)]]

    u0_bare = 1.0                                          # (local) initial displacement, released from rest
    sol_b = solve_ivp(rhs_bare, (tau0, tauf), [u0_bare, 0.0], method="Radau",
                      jac=jac_bare, t_eval=t_eval, rtol=RTOL, atol=ATOL)  # (local)
    if not sol_b.success:
        raise RuntimeError(f"Radau (bare) failed: {sol_b.message}")
    u = np.asarray(sol_b.y[0], dtype=float)                # (local) q - q* (bare)
    up = np.asarray(sol_b.y[1], dtype=float)               # (local) q' (bare)
    H_traj = np.asarray(np.interp(sol_b.t, tau, H_t), dtype=float)  # (local) H along trajectory

    # Transient-end detector: |u''|/|3H u'| < 0.01 sustained (overdamped tracking).
    upp_traj = np.asarray([rhs_bare(t, [u[i], up[i]])[1] for i, t in enumerate(sol_b.t)], dtype=float)  # (local)
    fric_term = 3.0 * H_traj * up                          # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio_acc = np.abs(upp_traj) / np.abs(fric_term)   # (local)
    below = ratio_acc < TRANSIENT_RATIO                    # (local)
    transient_end_idx = 0                                  # (local)
    for i in range(len(below)):
        if below[i] and np.all(below[i:] | ~np.isfinite(ratio_acc[i:])):
            transient_end_idx = i
            break
    else:
        transient_end_idx = len(below) // 2                # no sustained sub-threshold region

    n_total = len(sol_b.t)                                 # (local)
    win_start = transient_end_idx                          # (local)
    win = np.arange(win_start, n_total)                    # (local)
    # ln|u| needs single-sign u; the bare oscillator crosses zero => the clean window collapses,
    # which IS the substrate finding (no monotone tracking tail).
    s0 = np.sign(u[win_start]) if u[win_start] != 0 else 1.0  # (local)
    good = (np.sign(u[win]) == s0) & (np.abs(u[win]) > 0) & (H_traj[win] > 0) \
        & np.isfinite(u[win]) & np.isfinite(H_traj[win])   # (local)
    win = win[good]                                        # (local)
    intended_tail_len = n_total - transient_end_idx        # (local)
    domain_used_frac = (len(win) / intended_tail_len) if intended_tail_len > 0 else 0.0  # (local)

    def loglog_slope(uu, HH, idx):                         # (local) d ln|u|/d ln H on idx
        if len(idx) < 3:
            return float("nan"), float("nan"), 0.0
        lu = np.log(np.abs(uu[idx])); lH = np.log(HH[idx])  # (local)
        if np.ptp(lH) <= 1e-8:
            return float("nan"), float("nan"), 0.0
        AA = np.vstack([lH, np.ones_like(lH)]).T           # (local)
        cf, *_ = np.linalg.lstsq(AA, lu, rcond=None)       # (local)
        pr = AA @ cf                                       # (local)
        ssr = float(np.sum((lu - pr) ** 2)); sst = float(np.sum((lu - lu.mean()) ** 2))  # (local)
        return float(cf[0]), float(cf[1]), (1.0 - ssr / sst if sst > 0 else 0.0)

    slope_bare, intercept, r2 = loglog_slope(u, H_traj, win)  # (local) UNFORCED slope

    # ===================================================================
    # INTEGRATION B -- IMPOSED LINEAR CLOSURE q_eq(H) = c*H (S97 simple-fluid input)
    # q'' + 3H q' + k_curv*(q - c*H) = 0. With the imposed H-dependent equilibrium, the
    # adiabatic theorem (omega_osc = sqrt(k_curv) ~ 60 >> Hdot/H) makes q track q_eq=c*H,
    # so d ln q/d ln H -> 1. THIS slope=1 ONLY arises BECAUSE the linear closure q_eq~H is
    # imposed; it is the FAIL_meaning branch ("slope=1 only arises by imposing the slow-roll
    # quasi-static relation / a free closure parameter"). c-invariance is verified below.
    # ===================================================================
    def make_driven(c_drive):                              # (local)
        def rhs_d(t, y):
            u, up = y; Ht = H_of(t)                         # (local)
            return [up, -3.0 * Ht * up - K_CURV * (u - c_drive * Ht)]
        def jac_d(t, y):
            return [[0.0, 1.0], [-K_CURV, -3.0 * H_of(t)]]
        u0d = c_drive * H_of(tau0)                          # (local) start at q_eq(H0)
        return solve_ivp(rhs_d, (tau0, tauf), [u0d, 0.0], method="Radau",
                         jac=jac_d, t_eval=t_eval, rtol=RTOL, atol=ATOL)

    c_main = dq_dH                                         # (local) the S97 imposed proportionality 0.15
    sol_d = make_driven(c_main)                            # (local)
    ud = np.asarray(sol_d.y[0], dtype=float)               # (local)
    Hd = np.asarray(np.interp(sol_d.t, tau, H_t), dtype=float)  # (local)
    # driven late-time window: last 50% (q tracks q_eq, single sign, no zero-crossing)
    win_d = np.arange(n_total // 2, n_total)               # (local)
    gd = (np.abs(ud[win_d]) > 0) & (Hd[win_d] > 0) & np.isfinite(ud[win_d]) & np.isfinite(Hd[win_d])  # (local)
    win_d = win_d[gd]                                      # (local)
    slope_driven, _intd, r2_driven = loglog_slope(ud, Hd, win_d)  # (local) slope=1 under imposed closure

    # c-invariance of the driven slope (a structural property, not a tuned scale):
    sld_check, _, _ = loglog_slope(*( (lambda s: (np.asarray(s.y[0]),
                                                  np.asarray(np.interp(s.t, tau, H_t))))(make_driven(2.0 * c_main)) ),
                                   win_d)                  # (local)
    slope_driven_c_invariant = (np.isfinite(slope_driven) and np.isfinite(sld_check)
                                and abs(slope_driven - sld_check) < 1e-3)  # (local)

    # ===================================================================
    # GATE EVALUATION -- keyed on the pre-registered "UNFORCED" criterion (PASS_meaning
    # line 233 + FAIL_meaning line 239-240). The PRIMARY value is the UNFORCED bare-substrate
    # slope. The driven slope=1 is the cross-check demonstrating slope=1 arises ONLY under the
    # imposed linear closure.
    # ===================================================================
    slope = slope_bare                                     # (local) PRIMARY (unforced) gate value
    dev = abs(slope - TARGET_SLOPE) if np.isfinite(slope) else float("inf")  # (local) |slope_unforced - 1|

    # UNFORCED criterion: did slope=1 emerge from the bare substrate ODE WITHOUT imposing the
    # linear closure? The driven run shows slope=1 is recoverable ONLY with q_eq~H imposed.
    forced_only = (np.isfinite(slope_driven) and abs(slope_driven - 1.0) <= PASS_BAND
                   and not (np.isfinite(slope_bare) and abs(slope_bare - 1.0) <= INFO_BAND))  # (local)

    # [SIGN] 3-tuple
    #   sign_verdict: substitution chain predicts a POSITIVE tracking exponent (slope=n/2>0; q
    #     grows with H). The driven (tracking) slope is +1.008 > 0 -- the predicted DIRECTION of
    #     the tracking exponent is confirmed. PASS.
    sign_verdict = "PASS" if (np.isfinite(slope_driven) and slope_driven > 0) else "FAIL"  # (local)
    #   magnitude_verdict: the UNFORCED bare-substrate slope vs the band. slope=1 does NOT emerge
    #     unforced (the bare oscillator has no monotone H-tracking tail) -> FAIL on the unforced
    #     criterion per FAIL_meaning line 239-240. (If the unforced slope HAD hit the band, this
    #     would be PASS.)
    if (not forced_only) and dev <= PASS_BAND:
        magnitude_verdict = "PASS"                         # (local) unforced slope in band
    elif (not forced_only) and dev <= INFO_BAND:
        magnitude_verdict = "INFO"                         # (local) unforced slope narrows
    else:
        magnitude_verdict = "FAIL"                         # (local) slope=1 only under imposed closure
    #   regime_verdict: the bare-substrate attractor window. The bare oscillator's ln|u| window
    #     collapses (zero-crossings) -> domain_used_frac small -> regime tracks the shortening.
    if domain_used_frac >= 0.95:
        regime_verdict = "VALID"                           # (local)
    elif domain_used_frac >= 0.50:
        regime_verdict = "MARGINAL"                        # (local)
    else:
        regime_verdict = "BREAKDOWN"                       # (local)

    # Composite collapse (gate-verdicts.md PRE-REGISTERED rule) -- NOTE: the substrate finding is
    # that slope=1 is FORCED-ONLY (requires the imposed linear closure). FAIL_meaning line 239-240
    # makes this a FAIL: "the slope=1 result only arises by imposing the slow-roll quasi-static
    # relation / a free closure parameter => n=2 NOT a substrate-forced attractor". The bare-window
    # regime=BREAKDOWN independently routes to FAIL via the collapse rule. Both point to FAIL.
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                 # (local) bare window collapsed (no unforced tracking tail)
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

    return dict(
        value=slope,
        slope=slope, slope_bare=slope_bare, slope_driven=slope_driven,
        slope_driven_c_invariant=slope_driven_c_invariant, sld_check=sld_check,
        r2_driven=r2_driven, forced_only=forced_only, dq_dH=dq_dH, c_main=c_main,
        intercept=intercept, r2=r2,
        dev_from_target=dev, target_slope=TARGET_SLOPE,
        slope_u0_check=slope_driven, slope_u0_invariant=slope_driven_c_invariant,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        domain_used_frac=domain_used_frac,
        transient_end_idx=int(transient_end_idx), n_total=int(n_total),
        win_len=int(len(win)), intended_tail_len=int(intended_tail_len),
        K_CURV=K_CURV, K_CURV_PINNED=K_CURV_PINNED, sign_consistent=bool(sign_consistent),
        k_curv_raw_98=k_curv_raw_98, k_curv_raw_97=k_curv_raw_97, k_curv_pos_97=k_curv_pos_97,
        q_star=q_star, q_boundary=q_boundary, q0_ref=q0_ref, rho0_ref=rho0_ref,
        u0_bare=u0_bare, n_omega=n_omega,
        aeff_relvar=aeff_relvar, H_nonstat_relvar=H_nonstat_relvar,
        # arrays for npz/plot
        arr_tau=sol_b.t, arr_u=u, arr_up=up, arr_H_traj=H_traj,
        arr_ratio_acc=ratio_acc, arr_win=win,
        arr_ud=ud, arr_Hd=Hd, arr_a=a_t,
    )


# ---------------------------------------------------------------------------
# Section 6 -- Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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


def make_plot(res: dict) -> None:
    tau = res["arr_tau"]; u = res["arr_u"]; H = res["arr_H_traj"]      # (local) BARE trajectory
    ud = res["arr_ud"]; Hd = res["arr_Hd"]                            # (local) DRIVEN trajectory
    win = res["arr_win"]; ratio = res["arr_ratio_acc"]                 # (local)
    slope_b = res["slope_bare"]; slope_d = res["slope_driven"]        # (local)
    has_win = len(win) >= 2                                            # (local) bare clean-window non-empty?
    fig, ax = plt.subplots(2, 2, figsize=(12, 9))                      # (local)

    # (0,0) BARE u=q-q* (static well, q*=0) + H vs tau
    ax[0, 0].plot(tau, u, "b-", lw=1.2, label=r"$u=q-q_*$ (BARE, $q_*=0$)")
    ax[0, 0].axhline(0.0, color="grey", ls=":", lw=0.8)
    ax2 = ax[0, 0].twinx()                                            # (local)
    ax2.plot(tau, H, "r-", lw=1.0, alpha=0.7, label=r"$H(\tau)$")
    if has_win:
        ax[0, 0].axvspan(tau[win[0]], tau[win[-1]], color="green", alpha=0.12)
    ax[0, 0].set_xlabel(r"$\tau$"); ax[0, 0].set_ylabel(r"$u=q-q_*$", color="b")
    ax2.set_ylabel(r"$H(\tau)$", color="r")
    ax[0, 0].set_title("BARE substrate ODE: damped oscillator about q*=0\n(UNFORCED -- no monotone H-tracking tail)")
    ax[0, 0].legend(fontsize=7, loc="upper left")

    # (0,1) log-log ln|u| vs ln H -- BARE (no clean slope) vs DRIVEN (imposed closure -> slope=1)
    ax[0, 1].plot(np.log(Hd), np.log(np.abs(ud) + 1e-300), "c.", ms=2, alpha=0.5,
                  label="DRIVEN (imposed $q_{eq}=cH$)")
    if np.isfinite(slope_d):
        xx = np.array([np.log(Hd).min(), np.log(Hd).max()])           # (local)
        b_int = np.log(np.abs(ud)).mean() - slope_d * np.log(Hd).mean()  # (local)
        ax[0, 1].plot(xx, slope_d * xx + b_int, "r-", lw=1.8,
                      label=f"driven fit slope={slope_d:.4f}")
        ax[0, 1].plot(xx, 1.0 * xx + (np.log(np.abs(ud)).mean() - 1.0 * np.log(Hd).mean()),
                      "b--", lw=1.0, label="target slope=1")
    if has_win:
        ax[0, 1].plot(np.log(H[win]), np.log(np.abs(u[win])), "g.", ms=4, label="BARE clean window")
    ax[0, 1].set_xlabel(r"$\ln H$"); ax[0, 1].set_ylabel(r"$\ln|u|$")
    ax[0, 1].set_title(f"slope=1 ONLY under imposed closure: driven={slope_d:.4f}\nbare unforced={slope_b:.4f} (no clean tracking)")
    ax[0, 1].legend(fontsize=7)

    # (1,0) transient indicator |u''|/|3H u'| (bare)
    ax[1, 0].semilogy(tau, np.abs(ratio) + 1e-300, "m-", lw=1.0)
    ax[1, 0].axhline(0.01, color="k", ls="--", lw=0.8, label="transient threshold 0.01")
    if has_win:
        ax[1, 0].axvspan(tau[win[0]], tau[win[-1]], color="green", alpha=0.12)
    ax[1, 0].set_xlabel(r"$\tau$"); ax[1, 0].set_ylabel(r"$|u''|/|3Hu'|$")
    ax[1, 0].set_title("BARE friction-dominance indicator (oscillatory -> spikes at u'=0)")
    ax[1, 0].legend(fontsize=8)

    # (1,1) summary text
    ax[1, 1].axis("off")
    txt = (f"GATE: {GATE_ID}\n"
           f"composite: {res['composite']}\n\n"
           f"slope_BARE (UNFORCED) = {slope_b:.6f}  [primary]\n"
           f"slope_DRIVEN (imposed q_eq=cH) = {slope_d:.6f}\n"
           f"  driven c-invariant: {res['slope_driven_c_invariant']}\n"
           f"  imposed c = dq_dH (S97) = {res['c_main']:.4f}\n"
           f"target = {res['target_slope']:.1f}  (= n/2, n=2)\n"
           f"|slope_BARE - 1| = {res['dev_from_target']:.4f}\n"
           f"forced_only (slope=1 ONLY w/ closure): {res['forced_only']}\n"
           f"PASS<=0.05 INFO<=0.10 ; bare R^2={res['r2']:.4f}\n\n"
           f"k_curv (restoring well) = +{res['K_CURV']:.4f}\n"
           f"  raw d2E/dq2 (S98) = {res['k_curv_raw_98']:.4f} (energy conv.)\n"
           f"  sign consistent w/ pin +3586.5: {res['sign_consistent']}\n\n"
           f"bare domain_used_frac = {res['domain_used_frac']:.4f}\n"
           f"  transient_end={res['transient_end_idx']}/{res['n_total']} win={res['win_len']}\n\n"
           f"sign={res['sign_verdict']} mag={res['magnitude_verdict']} "
           f"regime={res['regime_verdict']}\n\n"
           f"n=2 NOT substrate-forced => C10 stays\n"
           f"ASSUMED-PARTIALLY-PROVEN (Track B)\n\n"
           f"H non-stat relvar = {res['H_nonstat_relvar']:.4f}\n"
           f"  (>> a_eff floor {res['aeff_relvar']:.2e})")
    ax[1, 1].text(0.02, 0.98, txt, va="top", ha="left", fontsize=8, family="monospace")

    fig.suptitle("S99-W2-RELAXATION-CLOSURE -- Volovik tracking-vacuum friction-ODE attractor",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 -- Main
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

    res = compute()
    value = res["value"]

    print("--- numerical results ---")
    print(f"  slope_BARE (UNFORCED; static well, q*=0, no drive)  = {res['slope_bare']:.8f}  [PRIMARY gate value]")
    print(f"  slope_DRIVEN (IMPOSED linear closure q_eq=c*H)       = {res['slope_driven']:.8f}  (R^2={res['r2_driven']:.6f})")
    print(f"    driven slope c-invariant (c, 2c)                  = {res['slope_driven_c_invariant']}  (slope@2c={res['sld_check']:.8f})")
    print(f"    imposed closure constant c = dq_dH (S97)          = {res['c_main']:.6f}  [LINEAR slow-roll closure / simple-fluid input]")
    print(f"  target slope (= n/2, n=2)                           = {res['target_slope']:.1f}")
    print(f"  |slope_BARE - 1|                                    = {res['dev_from_target']:.8f}  (PASS<=0.05, INFO<=0.10)")
    print(f"  forced_only (slope=1 ONLY under imposed closure)    = {res['forced_only']}  [=> FAIL_meaning line 239-240]")
    print(f"  R^2 of bare log-log fit                             = {res['r2']:.8f}")
    print(f"  k_curv (restoring, +|.|)                            = +{res['K_CURV']:.6f}  (raw d2E/dq2 S98 = {res['k_curv_raw_98']:.6f})")
    print(f"  sign consistent w/ pin +3586.5                      = {res['sign_consistent']}")
    print(f"  q* (bare fixed point)                               = {res['q_star']:.6f} ; q_boundary = {res['q_boundary']:.6f}")
    print(f"  domain_used_frac (bare attractor window)            = {res['domain_used_frac']:.6f}  (transient_end={res['transient_end_idx']}/{res['n_total']}, win={res['win_len']})")
    print(f"  H non-stationarity relvar                           = {res['H_nonstat_relvar']:.6f}  (>> a_eff floor {res['aeff_relvar']:.3e})")
    print(f"  3-tuple: sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} regime={res['regime_verdict']}")
    print(f"  composite                                           = {res['composite']}")
    print()

    # Save npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        regulator_pin="a_0^{zeta}",
        value=res["value"], slope=res["slope"],
        slope_bare=res["slope_bare"], slope_driven=res["slope_driven"],
        slope_driven_c_invariant=res["slope_driven_c_invariant"], sld_check=res["sld_check"],
        r2_driven=res["r2_driven"], forced_only=res["forced_only"],
        dq_dH=res["dq_dH"], c_main=res["c_main"],
        intercept=res["intercept"], r2=res["r2"],
        dev_from_target=res["dev_from_target"], target_slope=res["target_slope"],
        slope_u0_check=res["slope_u0_check"], slope_u0_invariant=res["slope_u0_invariant"],
        domain_used_frac=res["domain_used_frac"],
        transient_end_idx=res["transient_end_idx"], n_total=res["n_total"],
        win_len=res["win_len"], intended_tail_len=res["intended_tail_len"],
        K_CURV=res["K_CURV"], K_CURV_PINNED=res["K_CURV_PINNED"],
        sign_consistent=res["sign_consistent"],
        k_curv_raw_98=res["k_curv_raw_98"], k_curv_raw_97=res["k_curv_raw_97"],
        k_curv_pos_97=res["k_curv_pos_97"],
        q_star=res["q_star"], q_boundary=res["q_boundary"], q0_ref=res["q0_ref"], rho0_ref=res["rho0_ref"],
        u0_bare=res["u0_bare"], n_omega=res["n_omega"],
        aeff_relvar=res["aeff_relvar"], H_nonstat_relvar=res["H_nonstat_relvar"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"], composite=res["composite"],
        arr_tau=res["arr_tau"], arr_u=res["arr_u"], arr_up=res["arr_up"],
        arr_H_traj=res["arr_H_traj"], arr_ratio_acc=res["arr_ratio_acc"], arr_win=res["arr_win"],
        arr_ud=res["arr_ud"], arr_Hd=res["arr_Hd"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  saved png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    verdict = res["composite"]  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(
        verdict,
        (f"slope_bare_UNFORCED={res['slope_bare']:.6f}_dev={res['dev_from_target']:.6f}_"
         f"slope_driven_IMPOSED-closure={res['slope_driven']:.6f}_forced_only={res['forced_only']}_"
         f"target1_n2_domfrac={res['domain_used_frac']:.4f}_kcurv=+{res['K_CURV']:.2f}_"
         f"C10-ObjectC-NOT-substrate-forced"),
        audit_sha, content_sha,
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        companion_note=(f"C10 Object-C friction-ODE: slope=1 (n=2) arises ONLY under imposed linear closure "
                        f"q_eq=c*H (driven={res['slope_driven']:.4f}); bare-substrate ODE gives no unforced "
                        f"tracking tail => n=2 NOT substrate-forced; C10 stays ASSUMED-PARTIALLY-PROVEN; "
                        f"k_curv=+{res['K_CURV']:.2f} restoring well (Routh-Hurwitz attractor sign)"),
        extra_rows=["# regulator_pin=a_0^{zeta} (CC is the a_0 zeroth Seeley-DeWitt moment; V(q)=delta-rho_vac response)"],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
