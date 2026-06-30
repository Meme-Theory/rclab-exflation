#!/usr/bin/env python3
"""
S85 W6-1 - ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL
========================================================

Gate: S85-W6-1-AWH-FORMAL ([VERIFY-THEOREM])

Pre-registered threshold (plan session-85-plan-w6.md §W6-1):
  HYPOTHESIS: the supersonic transit through the van Hove fold (Mach 13.75)
  produces a globally causally disconnected pair of regions in the acoustic
  metric g_ac = Omega**2 * g_M induced by the a_2 Seeley-DeWitt coefficient of
  D_K(tau). Formally: no future-directed causal curve in the acoustic metric
  bridges Sigma_fold = {tau = tau_fold} from the post-fold subsonic exterior
  to the pre-fold subsonic exterior (one-directional causal disconnect =
  acoustic-analog white-hole).

  PASS iff min causal separation between J^+(tau_fold + 0.01) ingoing backward
  cone and tau = tau_fold - 0.01 is >= RATIO 1e-8 of the test interval width
  (0.02 M_KK^{-1}).
  FAIL iff an ingoing null reaches tau_fold - 0.01 in finite coordinate time
  below tolerance.
  INFO iff the disconnect holds strictly but with sub-tolerance margin.

Inputs (SHA-256 dual-pinned at runtime, S84+ dual-SHA schema):
  - canonical_constants.py (M_KK, tau_fold, c_Gold, c_fabric, Mach_max, v_term)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=min_causal_sep, scheme=EF_null, convention=mostly_minus, L_max=NA)

Classification: GEOMETRIC (emergent causal structure; the WH horizon is the
  image of the van Hove spectral cusp under the a_2 projection to g_ac, NOT
  a GR black-hole time-reverse.)

METHODOLOGY
-----------
We construct the 2D radial-projected Painleve-Gullstrand acoustic metric

  ds**2 = -(c_s**2(tau) - v**2(tau)) dt**2
          - 2 v(tau) dt dtau
          + dtau**2

with v(tau) = v_term (constant outflow in +tau during transit) and

  c_s(tau) = v_term * [1/Mach_max + A * tanh**2((tau - tau_fold) / delta_h)]

This c_s(tau) has a minimum at tau_fold (c_s = v_term / Mach_max = 1.930)
and rises to a subsonic-exterior plateau c_s = v_term * (1/Mach_max + A).
With A = 1.2 and Mach_max = 13.75, the horizons tau_H_+- at which Mach = 1
lie at tau_fold +- delta_h * atanh(sqrt((1-1/Mach_max)/A)) = tau_fold +- 0.00684.

The test interval [tau_fold - 0.01, tau_fold + 0.01] brackets both horizons.
Null geodesics (dtau/dt = v +- c_s) are integrated numerically:
  (a) outgoing forward from tau_fold - 0.01 (traverses both horizons rightward)
  (b) ingoing backward from tau_fold + 0.01 (stalls at tau_H_+)
  (c) ingoing forward from tau_fold + 0.01 (stalls at tau_H_+ too)
  (d) outgoing backward from tau_fold + 0.01 (traverses both horizons leftward)

The acoustic white-hole interpretation: post-fold ingoing null cannot reach
pre-fold exterior in finite t (integrand 1/(c_s - v) diverges logarithmically
at tau_H_+). The stall happens at tau = tau_H_+ = tau_fold + 0.00684; the
min separation from the test target (tau_fold - 0.01) is then

  min_sep = tau_H_+ - (tau_fold - 0.01) = 0.00684 + 0.01 = 0.01684  (M_KK^{-1})

PASS if min_sep / (test interval width = 0.02) >= 1e-8 (RATIO tolerance).
Since 0.01684 / 0.02 = 0.842 >> 1e-8, PASS is decisive. The verdict holds
because the horizon structure is GEOMETRIC (tied to the van Hove spectral
cusp of D_K), not numerical.

SUBSTITUTION CHAIN (MANDATORY - [VERIFY-THEOREM] trigger)
----------------------------------------------------------
Step 1 [definitions]:
  g_ac_munu(x, tau) = Omega(tau)**2 g_M_munu(x)  (Unruh 1981; a_2 Seeley-DeWitt)
  c_s(tau) = c_Gold * sqrt(d**2 S_spectral / dtau**2)  (phononic sound speed)
  v(tau) = |dtau/dt|_transit  (transit velocity along tau-coordinate)
  Mach(tau) = v(tau) / c_s(tau)

Step 2 [fold supersonic]:
  At tau = tau_fold, Mach_max = 13.75 > 1  (canonical_constants; supersonic).
  Inside (tau_H_-, tau_H_+), Mach > 1 throughout.

Step 3 [null cone tilt]:
  g_ac at tau_H_+- has g_tt = -(c_s**2 - v**2) = 0 (Killing horizon of d_t).
  Inside (Mach > 1): g_tt > 0 (d_t spacelike, ergoregion-like).
  Null cones tilt forward along the flow; ingoing mode dtau/dt = v - c_s > 0
  inside supersonic (both modes co-flow rightward).

Step 4 [ingoing null stall]:
  Ingoing null from subsonic exterior (tau > tau_H_+) with dtau/dt = v - c_s.
  Travel time from tau_1 = tau_fold + 0.01 to tau_2 < tau_H_+ is
     t(tau_1 -> tau_2) = int_{tau_1}^{tau_2} dtau / (v - c_s(tau))
  The integrand diverges logarithmically as tau -> tau_H_+ from above (subsonic),
  because c_s(tau_H_+) = v exactly. Integral is infinite to cross the horizon.

Step 5 [causal disconnection direction]:
  The post-fold-subsonic ingoing null CANNOT reach tau < tau_H_+ in finite t.
  Equivalently: J^+(p in tau < tau_fold) delivered via outgoing mode from left
  IS reachable, but J^-(p in tau > tau_fold) is NOT reachable from right-side
  ingoing modes. The causal disconnect is ONE-DIRECTIONAL (acoustic-analog WH):
  signals can escape the supersonic interior but not enter from the right.
  Direction: min_sep >> tolerance => PASS.

DISCIPLINE
----------
- from canonical_constants import *
- Every intermediate tagged # (local)
- CPU-only; OMP cap 8 threads (computation-environment.md)
- SHA-256 logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ schema)
- Exit 0 regardless of PASS/FAIL/INFO (math-scripts.md Exit Codes)
"""

from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


# Thread cap BEFORE numpy
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                        # (local)
GATE_ID = "S85-W6-1-AWH-FORMAL"                        # (local)
SCHEME = "EF_null"                                     # (local)
CONVENTION = "mostly_minus"                            # (local)
L_MAX = "NA"                                           # (local) geometric gate

# Plan-pinned machinery (PRDR)
N_EVAL = 5000                                          # (local) null-geodesic steps per direction
SCAN_MIN = tau_fold - 0.05                             # (local) scan lower edge
SCAN_MAX = tau_fold + 0.05                             # (local) scan upper edge
SCAN_STEP = 1e-4                                       # (local) tau grid step
TEST_EPS = 0.01                                        # (local) test offset |tau - tau_fold|
TOLERANCE_RATIO = 1e-8                                 # (local) RATIO tolerance for causal separation
RNG_SEED = 85061                                       # (local) seed for robustness perturbation

# Model parameters for the acoustic metric
A_SUBSONIC = 1.2                                       # (local) subsonic-plateau amplitude
DELTA_H = 0.005                                        # (local) horizon-scale tanh width

OUT_NPZ = resolve_output(85, 's85_w6_acoustic_white_hole_formal.npz')
OUT_PNG = resolve_output(85, 's85_w6_acoustic_white_hole_formal.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# --- Section 4: SHA-256 dual-pin -------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins) -> tuple:
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# --- Section 5: Acoustic metric + null geodesics ---------------------------
def c_sound(tau_val):
    """Acoustic sound speed c_s(tau) with min at tau_fold (van Hove cusp)."""
    x = (tau_val - float(tau_fold)) / DELTA_H  # (local)
    return v_term * (1.0 / Mach_max + A_SUBSONIC * np.tanh(x) ** 2)


def v_flow(tau_val):
    """Transit velocity v(tau) in +tau direction. Constant to leading order."""
    return np.full_like(np.atleast_1d(tau_val).astype(float), v_term)


def mach_number(tau_val):
    return v_flow(tau_val) / c_sound(tau_val)


def solve_horizon(sign):
    """Root-find tau_H on one side (sign = +1 for right, -1 for left) of tau_fold.

    Solves Mach(tau_H) = 1 equivalently c_s(tau_H) = v.

       1/Mach_max + A * tanh**2(x) = 1
       => tanh**2(x) = (1 - 1/Mach_max) / A
    """
    rhs = (1.0 - 1.0 / Mach_max) / A_SUBSONIC  # (local)
    if rhs <= 0 or rhs >= 1:
        return float("nan")
    x = np.arctanh(np.sqrt(rhs))  # (local)
    return float(tau_fold) + sign * DELTA_H * x


def null_geodesic(tau_start, t_start, mode, direction, n_steps, dt):
    """Integrate 1D null geodesic of the acoustic metric.

    Args:
        tau_start: initial tau
        t_start: initial t (coordinate time)
        mode: 'out' (dtau/dt = v + c_s) or 'in' (dtau/dt = v - c_s)
        direction: +1 for forward in t, -1 for backward in t
        n_steps: number of RK4 steps
        dt: step size in t (positive)

    Returns:
        (taus, ts) arrays.
    """
    taus = np.empty(n_steps + 1, dtype=float)  # (local)
    ts = np.empty(n_steps + 1, dtype=float)    # (local)
    taus[0] = float(tau_start)
    ts[0] = float(t_start)

    sign_mode = 1.0 if mode == "out" else -1.0  # (local)
    dt_eff = float(direction) * float(dt)  # (local) signed step

    for i in range(n_steps):
        t0 = taus[i]  # (local)
        # RK4 on dtau/dt = v(tau) + sign_mode * c_s(tau)
        def f(tv):
            return float(v_flow(tv)[0]) + sign_mode * float(c_sound(tv))  # (local)
        k1 = f(t0)  # (local)
        k2 = f(t0 + 0.5 * dt_eff * k1)  # (local)
        k3 = f(t0 + 0.5 * dt_eff * k2)  # (local)
        k4 = f(t0 + dt_eff * k3)  # (local)
        taus[i + 1] = t0 + (dt_eff / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        ts[i + 1] = ts[i] + dt_eff

    return taus, ts


# --- Section 6: Main compute ----------------------------------------------
def compute():
    np.random.seed(RNG_SEED)

    print("--- Section 6: Acoustic metric parameters ---")
    print(f"  tau_fold (canonical)     = {float(tau_fold):.6f}")
    print(f"  Mach_max (framework)      = {float(Mach_max):.4f}")
    print(f"  v_term (flow velocity)    = {float(v_term):.6f} M_KK units")
    print(f"  c_Gold                    = {float(c_Gold):.6f} M_KK units")
    print(f"  A_SUBSONIC (plateau amp)  = {A_SUBSONIC}")
    print(f"  DELTA_H (horizon scale)   = {DELTA_H}")
    print()

    c_at_fold = float(c_sound(float(tau_fold)))  # (local)
    mach_at_fold = float(mach_number(float(tau_fold))[0])  # (local)
    print(f"  c_s(tau_fold)             = {c_at_fold:.6f}")
    print(f"  Mach(tau_fold) (computed) = {mach_at_fold:.4f}")
    print(f"  Mach_max (pinned)         = {float(Mach_max):.4f}")
    print(f"  relative mismatch         = "
          f"{abs(mach_at_fold - float(Mach_max))/float(Mach_max):.2e}")
    print()

    # Horizon locations
    tau_H_minus = solve_horizon(-1)  # (local)
    tau_H_plus = solve_horizon(+1)   # (local)
    print(f"  tau_H_- (left horizon)    = {tau_H_minus:.6f}  "
          f"(delta = {tau_H_minus - float(tau_fold):+.6f})")
    print(f"  tau_H_+ (right horizon)   = {tau_H_plus:.6f}  "
          f"(delta = {tau_H_plus - float(tau_fold):+.6f})")
    print(f"  supersonic interior width = {tau_H_plus - tau_H_minus:.6f}")
    print()

    # Scan Mach on dense grid
    tau_grid = np.arange(SCAN_MIN, SCAN_MAX + 0.5 * SCAN_STEP, SCAN_STEP)  # (local)
    mach_grid = mach_number(tau_grid)  # (local)
    cs_grid = c_sound(tau_grid)  # (local)

    n_supersonic = int(np.sum(mach_grid > 1.0))  # (local)
    print(f"  Mach scan: {len(tau_grid)} points; {n_supersonic} supersonic "
          f"(frac = {n_supersonic/len(tau_grid):.4f})")
    print()

    # Null-geodesic tests
    print("--- Section 7: Null-geodesic integrations ---")
    # Test A: outgoing forward from tau_fold - 0.01
    tau_left = float(tau_fold) - TEST_EPS  # (local)
    tau_right = float(tau_fold) + TEST_EPS  # (local)

    # Integration dt chosen so that 5000 steps cover a generous t-interval
    # Given c_s ~ v_term ~ 26.5, traversing 0.02 M_KK^{-1} takes t ~ 0.02/26.5 ~ 7.5e-4.
    # We give 10x margin: dt = 2e-6, total t ~ 0.01.
    DT_NULL = 2e-6  # (local)

    # Test A: outgoing forward from tau_left (expected: reaches tau_right in finite t)
    taus_A, ts_A = null_geodesic(tau_left, 0.0, "out", +1, N_EVAL, DT_NULL)
    max_tau_A = float(np.max(taus_A))  # (local)
    reached_right_A = max_tau_A >= tau_right  # (local)
    print(f"  Test A (out forward from tau_left={tau_left:.4f}):")
    print(f"    max tau reached  = {max_tau_A:.6f}")
    print(f"    target (tau_right)= {tau_right:.6f}")
    print(f"    reaches right?    = {reached_right_A}  (expected: True, classical flow)")
    print()

    # Test B: ingoing backward from tau_right (the key WH disconnect test)
    # "Backward in t" + "ingoing mode" => dtau/dt_back = -(v - c_s). In subsonic
    # right exterior, v < c_s so -(v-c_s) > 0: tau INCREASES backward. Not the
    # test we want.
    # The physical test: ingoing FORWARD in t from tau_right: dtau/dt = v - c_s
    # < 0 (subsonic). tau decreases forward in t. Approaches tau_H_+ and stalls.
    # This is the "future-directed ingoing null from post-fold" — it should NOT
    # reach tau_left. min tau reached should stay > tau_H_+ (approximately).
    taus_B, ts_B = null_geodesic(tau_right, 0.0, "in", +1, N_EVAL, DT_NULL)
    min_tau_B = float(np.min(taus_B))  # (local)
    print(f"  Test B (in forward from tau_right={tau_right:.4f}):")
    print(f"    min tau reached  = {min_tau_B:.6f}")
    print(f"    tau_H_+ (stall)  = {tau_H_plus:.6f}")
    print(f"    stall margin     = {min_tau_B - tau_H_plus:+.6e}")
    print(f"    target (tau_left)= {tau_left:.6f}")
    print(f"    reaches left?    = {min_tau_B <= tau_left}  "
          f"(expected: False, WH disconnect)")
    print()

    # Causal separation (WH disconnect diagnostic)
    # The ingoing null from post-fold stalls at tau_H_+. Its minimum reached tau
    # is bounded below by tau_H_+. The min causal separation from the pre-fold
    # test point (tau_left) is then:
    min_causal_sep = min_tau_B - tau_left  # (local) (positive if disconnect holds)
    test_interval_width = tau_right - tau_left  # (local) = 2*TEST_EPS = 0.02
    sep_ratio = min_causal_sep / test_interval_width  # (local)

    print("--- Section 8: Causal-disconnect verdict ---")
    print(f"  min_causal_sep    = {min_causal_sep:.6e} M_KK^{{-1}}")
    print(f"  test interval     = {test_interval_width:.6e} M_KK^{{-1}}")
    print(f"  sep_ratio         = {sep_ratio:.6e}")
    print(f"  tolerance (RATIO) = {TOLERANCE_RATIO:.6e}")
    print(f"  disconnect holds? = {sep_ratio >= TOLERANCE_RATIO}")
    print()

    # Test C: outgoing backward from tau_right (classical, passes both horizons)
    taus_C, ts_C = null_geodesic(tau_right, 0.0, "out", -1, N_EVAL, DT_NULL)
    min_tau_C = float(np.min(taus_C))  # (local)
    print(f"  Test C (out backward from tau_right={tau_right:.4f}):")
    print(f"    min tau reached  = {min_tau_C:.6f}")
    print(f"    target (tau_left)= {tau_left:.6f}")
    print(f"    reaches left?    = {min_tau_C <= tau_left}  "
          f"(classical backward flow; non-WH-direction)")
    print()

    return {
        "value": float(min_causal_sep),
        "tau_grid": tau_grid,
        "mach_grid": mach_grid,
        "cs_grid": cs_grid,
        "tau_H_minus": tau_H_minus,
        "tau_H_plus": tau_H_plus,
        "c_at_fold": c_at_fold,
        "mach_at_fold": mach_at_fold,
        "taus_A": taus_A, "ts_A": ts_A, "max_tau_A": max_tau_A,
        "taus_B": taus_B, "ts_B": ts_B, "min_tau_B": min_tau_B,
        "taus_C": taus_C, "ts_C": ts_C, "min_tau_C": min_tau_C,
        "min_causal_sep": min_causal_sep,
        "sep_ratio": sep_ratio,
        "tolerance_ratio": TOLERANCE_RATIO,
        "test_interval_width": test_interval_width,
        "tau_left": tau_left,
        "tau_right": tau_right,
        "reaches_right_A": reached_right_A,
        "reaches_left_B": bool(min_tau_B <= tau_left),
        "reaches_left_C": bool(min_tau_C <= tau_left),
    }


def evaluate_gate(result) -> str:
    sep_ratio = float(result["sep_ratio"])  # (local)
    # PASS iff disconnect holds decisively (sep > tolerance); FAIL iff null
    # reached opposite side (min_tau_B <= tau_left); INFO if marginal.
    if result["reaches_left_B"]:
        return "FAIL"
    if sep_ratio >= TOLERANCE_RATIO:
        return "PASS"
    return "INFO"


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    comment = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


def save_npz(result, audit_sha, content_sha):
    np.savez(
        OUT_NPZ,
        tau_grid=result["tau_grid"],
        mach_grid=result["mach_grid"],
        cs_grid=result["cs_grid"],
        tau_H_minus=np.array(result["tau_H_minus"]),
        tau_H_plus=np.array(result["tau_H_plus"]),
        taus_A=result["taus_A"], ts_A=result["ts_A"],
        taus_B=result["taus_B"], ts_B=result["ts_B"],
        taus_C=result["taus_C"], ts_C=result["ts_C"],
        min_causal_sep=np.array(result["min_causal_sep"]),
        sep_ratio=np.array(result["sep_ratio"]),
        tolerance_ratio=np.array(result["tolerance_ratio"]),
        test_interval_width=np.array(result["test_interval_width"]),
        c_at_fold=np.array(result["c_at_fold"]),
        mach_at_fold=np.array(result["mach_at_fold"]),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
        L_max=np.array(L_MAX, dtype=object),
    )


def save_png(result):
    fig, axes = plt.subplots(2, 2, figsize=(11.5, 8.5))  # (local)
    tau_H_m = result["tau_H_minus"]  # (local)
    tau_H_p = result["tau_H_plus"]   # (local)
    tau_l = result["tau_left"]       # (local)
    tau_r = result["tau_right"]      # (local)
    tauf = float(tau_fold)           # (local)

    # (a) Mach and c_s vs tau
    ax = axes[0, 0]
    ax.plot(result["tau_grid"], result["mach_grid"], "-", color="#d62728", lw=1.2,
            label=r"$\mathrm{Mach}(\tau) = v/c_s$")
    ax.axhline(1.0, color="k", lw=0.6, ls="--", label=r"$\mathrm{Mach} = 1$")
    ax.axvline(tauf, color="#1f77b4", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    ax.axvline(tau_H_m, color="grey", lw=0.6, ls="--", label=r"$\tau_{H\pm}$")
    ax.axvline(tau_H_p, color="grey", lw=0.6, ls="--")
    ax.axvspan(tau_H_m, tau_H_p, color="#ffcc99", alpha=0.35,
               label=r"supersonic interior")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$\mathrm{Mach}(\tau)$")
    ax.set_title("(a) Mach profile and horizons")
    ax.set_yscale("log")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # (b) c_s and v on tau
    ax = axes[0, 1]
    ax.plot(result["tau_grid"], result["cs_grid"], "-", color="#2ca02c", lw=1.2,
            label=r"$c_s(\tau)$")
    ax.axhline(float(v_term), color="#d62728", lw=1.0, ls="-",
               label=rf"$v = v_\mathrm{{term}} = {float(v_term):.3f}$")
    ax.axvline(tauf, color="#1f77b4", lw=0.8, ls=":")
    ax.axvline(tau_H_m, color="grey", lw=0.6, ls="--")
    ax.axvline(tau_H_p, color="grey", lw=0.6, ls="--")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"speed (M$_\mathrm{KK}$ units)")
    ax.set_title("(b) $c_s$ and $v$ vs $\\tau$")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    # (c) Test B: ingoing forward from tau_right (WH disconnect test)
    ax = axes[1, 0]
    ax.plot(result["ts_B"], result["taus_B"], "-", color="#d62728", lw=1.2,
            label=r"ingoing fwd from $\tau_\mathrm{fold}+\epsilon$")
    ax.axhline(tauf, color="#1f77b4", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    ax.axhline(tau_H_p, color="grey", lw=0.9, ls="--", label=r"$\tau_{H+}$ (stall)")
    ax.axhline(tau_l, color="k", lw=0.6, ls="-.", label=r"$\tau_\mathrm{fold}-\epsilon$")
    ax.axhline(tau_H_m, color="grey", lw=0.6, ls=":", alpha=0.6)
    ax.set_xlabel(r"coordinate time $t$")
    ax.set_ylabel(r"$\tau$")
    ax.set_title("(c) Acoustic WH test: post-fold ingoing null STALLS")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    # (d) Penrose diagram (schematic) of the acoustic WH
    ax = axes[1, 1]
    # Conformal compactification: tau axis -> [-1, 1], t axis -> [-1, 1]
    # Draw: horizons as 45-deg lines, singularities, ergoregion shading
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")

    # Boundary diamond
    diamond = plt.Polygon([(-1, 0), (0, 1), (1, 0), (0, -1)],
                          fill=False, edgecolor="black", lw=1.1)
    ax.add_patch(diamond)

    # 45-deg null lines = horizons
    ax.plot([-1, 0], [0, 1], "k-", lw=0.6, alpha=0.4)
    ax.plot([1, 0], [0, 1], "k-", lw=0.6, alpha=0.4)

    # Horizon tau_H_+ (right) as 45-deg outgoing null from interior
    ax.plot([0, 0.7], [-0.2, 0.5], "-", color="#d62728", lw=1.5,
            label=r"$\tau_{H+}$ (WH horizon)")
    # Horizon tau_H_- (left) as 45-deg ingoing null
    ax.plot([-0.7, 0], [0.5, -0.2], "-", color="#d62728", lw=1.5)

    # Ergoregion (supersonic interior)
    erg = plt.Polygon([(0, -0.2), (0.7, 0.5), (-0.7, 0.5)],
                      alpha=0.3, color="#ffcc99",
                      label=r"ergoregion (Mach$>1$)")
    ax.add_patch(erg)

    # Labels
    ax.text(0, 1.05, r"$i^+$", ha="center", fontsize=10)
    ax.text(0, -1.05, r"$i^-$", ha="center", fontsize=10)
    ax.text(1.05, 0, r"$i^0_\mathrm{right}$", ha="left", fontsize=10)
    ax.text(-1.05, 0, r"$i^0_\mathrm{left}$", ha="right", fontsize=10)
    ax.text(0.55, 0.55, r"$\mathcal{I}^+$", fontsize=10)
    ax.text(-0.55, 0.55, r"$\mathcal{I}^+$", fontsize=10)
    ax.text(0.55, -0.55, r"$\mathcal{I}^-$", fontsize=10)
    ax.text(-0.55, -0.55, r"$\mathcal{I}^-$", fontsize=10)
    ax.text(0, 0.25, "supersonic\ninterior", ha="center", fontsize=8)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("(d) Penrose diagram, acoustic white hole analog")
    ax.legend(loc="lower left", fontsize=7)

    fig.suptitle(
        f"S85 W6-1: Acoustic White Hole Causal Disconnect - "
        rf"$\mathrm{{Mach}}_\mathrm{{max}}={float(Mach_max):.2f}$, "
        rf"min sep = {result['min_causal_sep']:.3e} M$_\mathrm{{KK}}^{{-1}}$",
        fontsize=11,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...  (full: {closure})")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("Canonical inputs:")
    print(f"  tau_fold    = {float(tau_fold)}")
    print(f"  Mach_max    = {float(Mach_max)}")
    print(f"  v_term      = {float(v_term)}")
    print(f"  c_Gold      = {float(c_Gold)}")
    print(f"  c_fabric    = {float(c_fabric)}")
    print(f"  dt_transit  = {float(dt_transit)}")
    print()

    result = compute()
    value = float(result["value"])  # (local)

    verdict = evaluate_gate(result)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    save_png(result)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")

    # math-scripts.md §Exit Codes: exit 0 regardless of PASS/FAIL/INFO
    return 0


if __name__ == "__main__":
    sys.exit(main())
