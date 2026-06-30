#!/usr/bin/env python3
"""
S86 W5b — S86-W5B-C15-ii-BASELINE
==================================

Gate ID:        S86-W5B-C15-ii-BASELINE
Trigger:        [VERIFY]
Classification: PHONONIC (substrate's own H trajectory under substrate-IC; the
                integration is a substrate-dynamics ODE, not a metric-projected
                one).

TASK
----
Forward-integrate the SR-LO H trajectory:
    dH/dN = - eps_H * H
from N = N_initial = N_pivot + 55 to N = N_pivot under the substrate IC, where
eps_H = eps_H_canon (held constant at SR-LO leading approximation), and emit
H(N_pivot) per pivot with a verdict against the pre-registered band.

Pre-registered (plan §W5b-1.ii §9):
    PASS iff:
      (a) numerical H(N_pivot) within +/- 5% of analytic H_initial * exp(-eps_H_canon * 55)
      (b) cross-check 1 residual |H_num - H_analytic|/|H_analytic| < rtol pin (1e-8)
      (c) both pivots reported (PRE-REG-BOTH default; C15(i) not landed at dispatch time)
    FAIL iff:
      - any pivot outside +/- 5% band, OR
      - any pivot CC1 residual exceeds rtol by more than 1 OOM, OR
      - ODE solver returns success = False
    INFO not used (binary VERIFY).

Substrate-framing (per .claude/rules/phononic-framing.md "IS Space, Not IN Space"):
    H is the substrate's own Hubble parameter at each fold-counter N. The trajectory
    IS the substrate's eps_H-driven evolution under SR-LO; eps_H is a Seeley-DeWitt-
    encoded substrate observable (a spectral-action moment of D_K), NOT an inflaton-
    field roll rate. The BASELINE column established here is the no-running, free-
    streaming reference that W5a P3's full coupled (eps, eta, alpha_s, xi^2) ODE must
    reduce to in the (eta, alpha_s, xi^2) -> 0 limit.

§10 substitution chain (plan; verified at compute time):
  Step 1 (definitions):
    N           : fold counter, N=0 at fold, N>0 toward present (W5a P3 convention)
    N_pivot     : 3.12 (substrate-zeta) OR 55 (MS); BOTH reported per spawn-prompt
    N_initial   : N_pivot + 55 e-folds
    eps_H_canon : constant SR-LO value = 0.020 (S85 W1a-1 anchor; same EPS_0 W5a P3)
    H(N)        : substrate Hubble parameter at fold-counter N
    H_initial   : H(N_initial), substrate IC at the upper integration bound

  Step 2 (substitute SR-LO eps_H = const into ODE):
    dH/dN = -eps_H_canon * H
    Separable: dH/H = -eps_H_canon dN
    Integrate: ln(H(N)/H_initial) = -eps_H_canon * (N - N_initial)
    Exponentiate: H(N) = H_initial * exp(-eps_H_canon * (N - N_initial))

  Step 3 (simplify at N = N_pivot, where N_pivot - N_initial = -55):
    H(N_pivot) = H_initial * exp(-eps_H_canon * (-55))
               = H_initial * exp(+55 * eps_H_canon)
               = H_initial * exp(+1.10)
               = H_initial * 3.0041660239

  Step 4 (read off direction):
    eps_H_canon > 0 AND we integrate BACKWARD in N from N_initial to N_pivot
    (from later-fold N=N_pivot+55 to earlier-fold N=N_pivot, since N increases
    toward present in the W5a P3 convention).
    => exp(+55 * eps_H_canon) > 1 => H(N_pivot) > H_initial
    Physical: H is LARGER at earlier N (smaller N) and DECREASES as N grows.

Cross-checks:
  CC1 (analytic identity): H(N_pivot)_numerical agrees with H_initial *
      exp(-eps_H_canon * (N_pivot - N_initial)) to better than rtol pin (1e-8).
  CC2 (W5a P3 reduction limit): W5a P3 LCDM trajectory eps_lcdm[N] is the
      W5a P3 SR-flow under (eta_0=0.005, alpha_s_0=0, xi^2_0=0) IC. Strict
      (eta, alpha_s, xi^2) -> 0 limit would give eps(N) constant at eps_0=0.02;
      W5a P3 LCDM has eta_0=0.005 ≠ 0 so eps_lcdm DRIFTS from 0.02 to 4.45e-3.
      Reconstruct H_W5aP3_lcdm(N)/H_initial = exp(-int_{N_initial}^{N} eps_lcdm dN'),
      compute at N_pivot, and report the deviation vs BASELINE constant-eps_H.
      The deviation IS the eta-driven correction (NOT a violation of agreement).

Inputs (S84+ dual-SHA):
  - computations/_shared/canonical_constants.py
  - computations/session-86/s86_w5a_p3_sector_1_z_factor.npz (CC2 reference; W5a P3
    LCDM trajectory at (eta_0=0.005, alpha_s_0=0, xi^2_0=0) IC)
  - computations/session-86/s86_w5b_c15_ii_baseline.py (this file)

Output 4-tuples (one verdict line per session bookkeeping; both pivot values
within the value field):
    (value="<H_at_3.12>;<H_at_55>" (M_KK natural units),
     scheme=RK45_rtol1e-8,
     convention=both-pivots-PRE-REG-BOTH,
     L_max=10)

Author: transit-dynamics-theorist (S86 W5b runtime)
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

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp, simpson
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------- Project paths -----------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

# Canonical constants (used in pin map; ODE itself uses local SR-LO eps_H)
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    dt_transit,
    w0_FW,
)

# ----------------------------- Gate identity -----------------------------

SESSION = "S86"
GATE_ID = "S86-W5B-C15-ii-BASELINE"
SCHEME = "RK45_rtol1e-8"
CONVENTION = "both-pivots-PRE-REG-BOTH"   # C15(i) not landed; PRE-REG-BOTH default
L_MAX = 10                                 # (local) substrate-IC derivation pin

CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')
SCRIPT_PATH = Path(__file__).resolve()
W5A_P3_NPZ_PATH = resolve_output(86, 's86_w5a_p3_sector_1_z_factor.npz')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')
NPZ_PATH = resolve_output(86, 's86_w5b_c15_ii_baseline.npz')
PNG_PATH = resolve_output(86, 's86_w5b_c15_ii_baseline.png')

# ----------------------------- Pre-registered IC + machinery pins -----------------------------
# Plan §W5b-1.ii §7 PRDR machinery-enumeration

EPS_H_CANON = 0.020         # (local) S85 W1a-1 baseline anchor; matches W5a P3 EPS_0
                            # NOT registered in canonical_constants.py as 'eps_H_canon';
                            # only related entries: eps_H_HP1_norm=16.198, eps_H_W6=0.02163.
                            # 0.020 is the SR-LO BASELINE pin used by W5a P3 for
                            # consistency. Cross-check 2 will quantify the difference
                            # between this constant-eps_H BASELINE and W5a P3's
                            # eta-driven LCDM trajectory.

H_INITIAL = 1.0             # (local) M_KK natural units. Substrate-natural normalization
                            # used because C15(i) has not landed; under PRE-REG-BOTH both
                            # pivots use the same H_initial. The pivot-specific H_initial
                            # would otherwise be derived from C15(i)'s selection rule.

PIVOTS = {
    "MS_canonical": 55.0,
    "substrate_native_zeta": 3.12,
}  # (local) per spawn-prompt: report BOTH if C15(i) PRE-REG-BOTH

N_OFFSET = 55.0              # (local) plan §W5b-1.ii: N_initial = N_pivot + 55

# ODE integration pins (plan §7)
RTOL = 1.0e-8                # (local) plan §7
ATOL = 1.0e-10               # (local) plan §7
MAX_STEP = 0.1               # (local) e-folds; plan §7
INTEGRATION_METHOD = "RK45"  # (local) plan §7

# Pass/fail bands (plan §9)
PASS_BAND_REL = 0.05         # (local) ABSOLUTE 5% on |H_num-H_analytic|/|H_analytic|
CC1_RTOL_TOLERANCE_OOM = 1.0  # (local) plan §9: "exceeds rtol by more than 1 OOM"
CC1_RTOL_PIN = RTOL          # (local) THEOREM-grade tolerance for CC1


# ----------------------------- SHA helpers (S84+ dual-SHA schema) -----------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: ABSENT")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    machinery_pin_map: dict,
) -> tuple[str, str]:
    """audit_sha256 = SHA(script + canonical + sorted-pins-json + machinery-json).
    content_sha256 = SHA(script_only)."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    machinery_json = json.dumps(
        machinery_pin_map, separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(machinery_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict_line(
    gate_id: str,
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
) -> None:
    """W9a-99 dual-SHA schema + 16-hex companion comment row."""
    line = (
        f"{gate_id}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ----------------------------- ODE: dH/dN = -eps_H * H -----------------------------

def rhs_baseline(N: float, y: np.ndarray) -> list[float]:
    """SR-LO (constant eps_H) substrate H trajectory: dH/dN = -eps_H_canon * H.

    State vector y = [H]. eps_H is held constant at EPS_H_CANON (BASELINE definition;
    no eta, alpha_s, or xi^2 sources).
    """
    H = y[0]  # (local)
    dH_dN = -EPS_H_CANON * H  # (local)
    return [dH_dN]


# ----------------------------- Cross-check 2: W5a P3 LCDM trajectory reduction -----------------------------

def reconstruct_H_from_W5aP3_lcdm(N_eval: np.ndarray, eps_lcdm: np.ndarray,
                                   N_initial: float, N_pivot: float,
                                   H_initial: float) -> float:
    """Reconstruct H(N_pivot) using the W5a P3 LCDM eps trajectory.

    Under the (eta, alpha_s, xi^2) -> 0 limit, the BASELINE eps_H is constant.
    W5a P3 LCDM IC has eta_0=0.005 (NOT zero); so eps_lcdm[N] DRIFTS from 0.02
    toward 4.45e-3 over 55 e-folds, not constant. The W5a P3 LCDM trajectory is
    therefore the (alpha_s, xi^2) -> 0 limit only (eta still active).

    H(N_pivot) under W5a P3 eps_lcdm trajectory:
      ln(H(N_pivot)/H_initial) = -int_{N_initial}^{N_pivot} eps_H(N') dN'
                               = +int_{N_pivot}^{N_initial} eps_H(N') dN'  [flip limits]

    We integrate eps_lcdm over the window [N_pivot, N_initial] and exponentiate.
    """
    # Restrict to the interval [N_pivot, N_initial] within W5a P3 N_eval grid
    mask = (N_eval >= N_pivot) & (N_eval <= N_initial)  # (local)
    N_window = N_eval[mask]  # (local)
    eps_window = eps_lcdm[mask]  # (local)
    if len(N_window) < 3:
        return float("nan")
    # Simpson's rule over the dense W5a P3 grid (0.01 e-fold resolution)
    integral = simpson(y=eps_window, x=N_window)  # (local) int_{N_pivot}^{N_initial} eps_lcdm dN
    # H(N_pivot) = H_initial * exp(+integral) (positive because we flipped limits)
    return H_initial * np.exp(+integral)


# ----------------------------- Verdict logic -----------------------------

def classify(per_pivot_results: dict) -> str:
    """Plan §9 classifier.

    PASS iff for ALL pivots:
      (a) |H_num - H_analytic| / |H_analytic| <= PASS_BAND_REL (5%)
      (b) CC1 residual < rtol pin * 10^CC1_RTOL_TOLERANCE_OOM
      (c) ODE success = True
    FAIL iff any of the above fails for any pivot.
    """
    cc1_threshold = CC1_RTOL_PIN * (10 ** CC1_RTOL_TOLERANCE_OOM)  # (local)
    for pname, r in per_pivot_results.items():
        if not r["ode_success"]:
            return "FAIL"
        if r["band_rel_dev"] > PASS_BAND_REL:
            return "FAIL"
        if r["cc1_residual"] > cc1_threshold:
            return "FAIL"
    return "PASS"


# ----------------------------- Main -----------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # Banner
    print(f"=== {GATE_ID} - runtime ===")
    print(f"  session: {SESSION}")
    print(f"  scheme: {SCHEME}")
    print(f"  convention: {CONVENTION}")
    print(f"  L_max: {L_MAX}")
    print()

    # Input pins (first 20 lines per gate-verdicts.md)
    pins = log_input_pins([CANONICAL_PATH, W5A_P3_NPZ_PATH, SCRIPT_PATH])
    print()

    # Constants pin echo
    print(f"=== Canonical constants used (W5a P3 anchor) ===")
    print(f"  tau_fold       = {tau_fold!r}")
    print(f"  M_KK           = {M_KK!r}")
    print(f"  dt_transit     = {dt_transit!r}")
    print(f"  w0_FW          = {w0_FW!r}")
    print(f"  EPS_H_CANON    = {EPS_H_CANON!r}    (S85 W1a-1; matches W5a P3 EPS_0)")
    print(f"  H_INITIAL      = {H_INITIAL!r} (M_KK natural units; substrate-natural)")
    print()

    # Substitution chain echo (math-is-hard discipline)
    print(f"=== Substitution chain (plan §10 verified) ===")
    print(f"  Step 2 ODE:  dH/dN = -eps_H_canon * H")
    print(f"  Step 3 sol:  H(N_pivot) = H_initial * exp(-eps_H_canon * (N_pivot - N_initial))")
    print(f"            =  H_initial * exp(+55 * eps_H_canon)")
    H_analytic_universal = H_INITIAL * np.exp(+N_OFFSET * EPS_H_CANON)  # (local)
    print(f"  Step 3 num:  H_analytic = {H_INITIAL} * exp(+55 * {EPS_H_CANON}) = {H_analytic_universal:.10f}")
    print(f"  Step 4 dir:  eps_H>0, integrating backward in N => H(N_pivot) > H_initial.")
    print()

    # Load W5a P3 reference
    print(f"=== Loading W5a P3 reference for CC2 ===")
    w5a_data = np.load(W5A_P3_NPZ_PATH, allow_pickle=True)
    N_eval_w5a = np.asarray(w5a_data["N_eval"])  # (local)
    eps_lcdm_w5a = np.asarray(w5a_data["eps_lcdm"])  # (local)
    print(f"  N_eval shape: {N_eval_w5a.shape}, range [{N_eval_w5a[0]:.3f}, {N_eval_w5a[-1]:.3f}]")
    print(f"  eps_lcdm[N=0]={eps_lcdm_w5a[0]:.6f}, eps_lcdm[N=55]={eps_lcdm_w5a[5500]:.6f}")
    print()

    # ----------------------------- ODE integration per pivot -----------------------------
    print(f"=== ODE forward integration per pivot ===")
    per_pivot_results: dict[str, dict] = {}  # (local)
    n_eval_pts_per_pivot = 551  # (local) ~0.1 e-fold resolution over 55 e-folds

    for pivot_name, N_pivot in PIVOTS.items():
        N_initial = N_pivot + N_OFFSET  # (local)
        # scipy backward-in-N integration: t_span=(N_initial, N_pivot) with N_initial > N_pivot
        # solve_ivp handles this automatically (the direction is inferred from t_span order)
        N_eval_grid = np.linspace(N_initial, N_pivot, n_eval_pts_per_pivot)  # (local)
        sol = solve_ivp(
            rhs_baseline,
            t_span=(N_initial, N_pivot),
            y0=[H_INITIAL],
            method=INTEGRATION_METHOD,
            rtol=RTOL,
            atol=ATOL,
            max_step=MAX_STEP,
            t_eval=N_eval_grid,
            dense_output=True,
        )
        ode_success = bool(sol.success)  # (local)
        if ode_success:
            H_at_pivot_num = float(sol.y[0, -1])  # (local) value at N_pivot (last grid point)
        else:
            H_at_pivot_num = float("nan")

        # Analytic limit (CC1 reference)
        H_at_pivot_analytic = H_INITIAL * np.exp(-EPS_H_CANON * (N_pivot - N_initial))  # (local)

        # CC1 residual: |H_num - H_analytic| / |H_analytic|
        if np.isfinite(H_at_pivot_num) and abs(H_at_pivot_analytic) > 0:
            cc1_residual = abs(H_at_pivot_num - H_at_pivot_analytic) / abs(H_at_pivot_analytic)  # (local)
        else:
            cc1_residual = float("inf")

        # Band residual against analytic (the PASS criterion is that numerical agrees with
        # analytic; both share the same H_initial, so band_rel_dev == cc1_residual under
        # this BASELINE design. The two conditions stack: 5% band + 1e-8 rtol pin.)
        band_rel_dev = cc1_residual  # (local)

        # CC2: W5a P3 LCDM trajectory comparison
        H_at_pivot_W5aP3_lcdm = reconstruct_H_from_W5aP3_lcdm(
            N_eval_w5a, eps_lcdm_w5a, N_initial, N_pivot, H_INITIAL
        )  # (local)
        # Note: W5a P3 N_span ends at 60.0; N_initial=58.12 (for substrate-zeta pivot)
        # is within range, but N_initial=110 (for MS pivot) is NOT in the W5a P3 grid.
        # For the MS pivot, the CC2 reduction must use available data only; we'll compute
        # over [N_pivot, min(N_initial, 60.0)] and note the truncation.
        if N_initial > N_eval_w5a[-1]:
            # Truncated CC2: integrate eps_lcdm over [N_pivot, 60.0] and supplement with
            # the analytic constant-eps extrapolation over [60.0, N_initial]. This is a
            # diagnostic, not a strict reduction-test (W5a P3 grid was sized for 60 e-folds).
            eps_lcdm_at_60 = eps_lcdm_w5a[-1]  # (local)
            extra_window = N_initial - N_eval_w5a[-1]  # (local)
            extra_integral = eps_lcdm_at_60 * extra_window  # (local) constant-eps extrap
            mask = (N_eval_w5a >= N_pivot) & (N_eval_w5a <= N_eval_w5a[-1])  # (local)
            integral_truncated = simpson(y=eps_lcdm_w5a[mask], x=N_eval_w5a[mask])  # (local)
            H_at_pivot_W5aP3_lcdm = H_INITIAL * np.exp(+integral_truncated + extra_integral)
            cc2_truncated = True  # (local)
        else:
            cc2_truncated = False  # (local)

        if np.isfinite(H_at_pivot_W5aP3_lcdm) and abs(H_at_pivot_analytic) > 0:
            cc2_relative_deviation = abs(H_at_pivot_num - H_at_pivot_W5aP3_lcdm) / abs(H_at_pivot_num)  # (local)
        else:
            cc2_relative_deviation = float("nan")

        per_pivot_results[pivot_name] = {
            "N_pivot": N_pivot,
            "N_initial": N_initial,
            "H_initial": H_INITIAL,
            "H_at_pivot_num": H_at_pivot_num,
            "H_at_pivot_analytic": H_at_pivot_analytic,
            "H_at_pivot_W5aP3_lcdm": H_at_pivot_W5aP3_lcdm,
            "cc1_residual": cc1_residual,
            "cc2_relative_deviation": cc2_relative_deviation,
            "cc2_truncated": cc2_truncated,
            "ode_success": ode_success,
            "ode_message": str(sol.message),
            "band_rel_dev": band_rel_dev,
            "N_eval_grid": N_eval_grid,
            "H_traj": sol.y[0, :].copy(),
        }

        print(f"  pivot '{pivot_name}': N_pivot={N_pivot}, N_initial={N_initial}")
        print(f"    H(N_pivot)_num      = {H_at_pivot_num:.12f}")
        print(f"    H(N_pivot)_analytic = {H_at_pivot_analytic:.12f}")
        print(f"    CC1 residual        = {cc1_residual:.3e}  (target < {CC1_RTOL_PIN * (10**CC1_RTOL_TOLERANCE_OOM):.0e})")
        print(f"    band_rel_dev        = {band_rel_dev:.3e}  (PASS band < {PASS_BAND_REL})")
        print(f"    CC2 H_W5aP3_lcdm    = {H_at_pivot_W5aP3_lcdm:.12f}")
        print(f"    CC2 rel_dev         = {cc2_relative_deviation:.3e}  ({'truncated' if cc2_truncated else 'in-grid'})")
        print(f"    ODE success         = {ode_success}; msg = {sol.message}")
        print()

    # Verdict
    verdict = classify(per_pivot_results)  # (local)
    print(f"=== Verdict: {verdict} ===")

    # ----------------------------- Plot -----------------------------
    print(f"=== Writing plot to {PNG_PATH.name} ===")
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    colors = {"MS_canonical": "tab:blue", "substrate_native_zeta": "tab:red"}  # (local)
    for pname, r in per_pivot_results.items():
        ax.plot(r["N_eval_grid"], r["H_traj"], color=colors[pname], lw=2,
                label=f"{pname} (N_pivot={r['N_pivot']}, N_initial={r['N_initial']})")
        ax.axvline(r["N_pivot"], color=colors[pname], linestyle=":", alpha=0.5)
    ax.set_xlabel("N (e-folds, substrate fold-counter; N=0 at fold, N>0 toward present)")
    ax.set_ylabel(r"$H(N)$ in $M_{KK}$ natural units (H_initial = 1)")
    ax.set_title(f"S86 W5b C15(ii) BASELINE — substrate H(N) trajectory under SR-LO constant eps_H = {EPS_H_CANON}")
    ax.legend(loc="best")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  saved: {PNG_PATH.name}")
    print()

    # ----------------------------- Save NPZ -----------------------------
    print(f"=== Writing NPZ to {NPZ_PATH.name} ===")
    npz_kwargs: dict = {}  # (local)
    # Concatenate per-pivot arrays with prefix
    for pname, r in per_pivot_results.items():
        npz_kwargs[f"N_eval_{pname}"] = np.asarray(r["N_eval_grid"])
        npz_kwargs[f"H_traj_{pname}"] = np.asarray(r["H_traj"])
        npz_kwargs[f"H_at_pivot_num_{pname}"] = np.asarray(r["H_at_pivot_num"])
        npz_kwargs[f"H_at_pivot_analytic_{pname}"] = np.asarray(r["H_at_pivot_analytic"])
        npz_kwargs[f"H_at_pivot_W5aP3_lcdm_{pname}"] = np.asarray(r["H_at_pivot_W5aP3_lcdm"])
        npz_kwargs[f"cc1_residual_{pname}"] = np.asarray(r["cc1_residual"])
        npz_kwargs[f"cc2_relative_deviation_{pname}"] = np.asarray(r["cc2_relative_deviation"])
        npz_kwargs[f"cc2_truncated_{pname}"] = np.asarray(r["cc2_truncated"])
    npz_kwargs["EPS_H_CANON"] = np.asarray(EPS_H_CANON)
    npz_kwargs["H_INITIAL"] = np.asarray(H_INITIAL)
    npz_kwargs["N_OFFSET"] = np.asarray(N_OFFSET)
    npz_kwargs["pivot_names"] = np.asarray(list(PIVOTS.keys()))
    npz_kwargs["pivot_values"] = np.asarray(list(PIVOTS.values()))
    np.savez_compressed(NPZ_PATH, **npz_kwargs)
    print(f"  saved: {NPZ_PATH.name}")
    print()

    # ----------------------------- Verdict line -----------------------------
    machinery_pin_map = {
        "L_max": L_MAX,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "rtol": RTOL,
        "atol": ATOL,
        "max_step": MAX_STEP,
        "method": INTEGRATION_METHOD,
        "PASS_band_rel": PASS_BAND_REL,
        "CC1_rtol_pin": CC1_RTOL_PIN,
        "CC1_rtol_tolerance_oom": CC1_RTOL_TOLERANCE_OOM,
        "EPS_H_CANON": EPS_H_CANON,
        "H_INITIAL": H_INITIAL,
        "N_OFFSET": N_OFFSET,
        "pivots": PIVOTS,
        "n_eval_pts_per_pivot": n_eval_pts_per_pivot,
        "GPU_path": "CPU OMP_NUM_THREADS=8",
        "random_seed": "n/a (deterministic ODE)",
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(
        SCRIPT_PATH, CANONICAL_PATH, pins, machinery_pin_map
    )

    # Build value_str: both pivots
    h_312 = per_pivot_results["substrate_native_zeta"]["H_at_pivot_num"]  # (local)
    h_55 = per_pivot_results["MS_canonical"]["H_at_pivot_num"]  # (local)
    value_str = f'"H_at_3.12={h_312:.10f};H_at_55={h_55:.10f}"'  # (local)

    append_verdict_line(GATE_ID, verdict, value_str, audit_sha, content_sha)
    print(f"=== Verdict line appended ===")
    print(f"  {GATE_ID}: {verdict} -- value={value_str}")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print()

    # 4-tuple final non-verdict line
    print(f"4-tuple: (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"runtime: {time.time() - t0:.2f} s")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
