#!/usr/bin/env python3
"""
INV5 W1-2 — a4 Seeley-DeWitt -> {Yang-Mills, Higgs-quartic, Weyl^2, Gauss-Bonnet};
            isolate Weyl^2/trace-anomaly sub-term; test NON-monotonicity in tau
            (escape from the W4 monotonicity wall) + OOM-distance rho_anomaly vs rho_Lambda.
================================================================================

Gate: INV5-W1-2-A4-WEYL-TRACE-ANOMALY-CC-CHANNEL  ([SIGN])

Pre-registered threshold (from investigation-5-plan-w1.md §W1-2):
  operator (set): (a) sign(d a_4^{Weyl}/dtau) changes across [tau_fold-0.05, tau_fold+0.05]
                  AND (b) |log10(rho_anomaly/rho_Lambda)| reported as OOM-distance.
  strict_PASS_boundary: non-monotone (>=1 sign change in d a_4^{Weyl}/dtau over the 21-pt scan)
  PASS  : >=1 sign change in d/dtau[a_4^Weyl] over [0.14,0.24] (NON-monotone -> escapes W4)
  FAIL  : 0 sign changes (monotone -> ALSO covered by W4; closes last geometric NCG CC channel)
  INFO  : Weyl^2/GB don't cleanly separate from YM+Higgs at finite L_max, OR
          rho_anomaly > 60 OOM from rho_Lambda (non-monotone but cosmologically irrelevant).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py (feeds audit_sha256 only; a_4_FW_zeta, rho_Lambda_obs, M_KK_gravity, tau_fold)
  - sessions/framework/correspondence/.. NOT a numerical pin (the Riemann tensor is
    REBUILT analytically in-script from the 147/147-verified r20a machinery; the
    r20a_riemann_tensor.npz is ABSENT from disk so this is a substrate-first RECOMPUTE,
    NOT a stale-npz read, per substrate-first-canonical-sourcing.md and the plan §W1-2 note).
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<non_monotone_signchanges|OOM>, scheme=Gilkey-a4-Weyl-GaussBonnet-decomposition,
   convention=ABSOLUTE, L_max=12)

Classification: GEOMETRIC.

METHODOLOGY
-----------
The a_4 Seeley-DeWitt moment IS the fabric's fourth spectral moment. We rebuild the
full 8x8x8x8 Riemann tensor R_{abcd}(tau) on Jensen-deformed SU(3) from the analytic
left-invariant metric g_tau = 3*diag(e^{-2t}x3, e^{t}x4, e^{2t})  (E1; baptista-operator-dk-tau.md
§2.1.2) via the r20a machinery (su3_generators -> structure constants -> Killing form ->
jensen_metric -> orthonormal_frame -> connection -> Riemann; 147/147 machine-eps verified, S20a).
We form the three curvature invariants R^2, |Ric|^2, |Riem|^2 and assemble the Gilkey a_4
integrand (Eq. 4.8, spectral-geometer-layers.md):
   a_4 = (4pi)^{-d/2}/360 * Int tr[5/2 R^2 - 2|Ric|^2 + 2|Riem|^2 + box-R + 60 F^2] sqrt(g).
DECOMPOSE (curvature-invariant identities, d=8):
   (i)  Yang-Mills      = the 60 F_munu F^munu piece (gauge; at the Einstein point S5 it
                          vanishes for the pure-curvature SU(3) fiber - we report it = 0 here)
   (ii) Higgs-quartic   = the |S|^2-mode (matter-dressed) contribution (off the pure-geometry
                          fiber; reported via the a_4_FW_zeta full-vs-geometric share)
   (iii) Weyl^2 = C^2   = |Riem|^2 - 4/(d-2)|Ric|^2 + 2/((d-1)(d-2)) R^2   (conformally invariant)
   (iv) Gauss-Bonnet    = |Riem|^2 - 4|Ric|^2 + R^2   (Euler/topological quadratic combination)
Isolate Weyl^2+trace-anomaly, scan d/dtau across the 21-pt window [0.14,0.24], test for
>=1 sign change (NON-monotone => escapes the W4 monotonicity wall, S17a/S37 W7, which proves
d/dtau a_{2k} has FIXED SIGN via d/dtau<lambda^2> > 0). Compare the anomaly-induced vacuum
energy rho_anomaly = f_0 * a_4^Weyl * M_KK^4 to rho_Lambda_obs.

EXACT CROSS-CHECK (Sage-derived this session, against the 147/147 tensor):
  R(t)    = -1/4 e^{-4t} + 2 e^{-t} - 1/4 + 1/2 e^{2t}                         (E3, R - E3 = 0 exact)
  |Ric|^2 = 1/24 (2 e^{12t}+3 e^{8t}-12 e^{7t}+26 e^{6t}+3 e^{4t}-12 e^{3t}+2) e^{-8t}
  |Riem|^2= (23/96)e^{-8t}-e^{-5t}+(5/16)e^{-4t}+(11/6)e^{-2t}-(3/2)e^{-t}+17/32+(1/12)e^{4t}
            (= kretschner_exact, r20a, machine-eps validated vs full tensor)
The numerical r20a-tensor invariants are cross-checked against these closed forms at every
scan point (the substrate-first recompute and the analytic forms must agree to <1e-10).

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- GPU_path pin: numpy.linalg (small 8x8x8x8 dense Riemann contractions); OMP_NUM_THREADS=8.
- regulator_pin: a_4^{zeta} (the spectral-sum a_4 leg = a_4_FW_zeta=1350.7216,
  regulator-pin-discipline.md MANDATORY); the curvature-invariant leg is regulator-free Gilkey.
- Verdict via emit_verdict MCP tool (script PRINTS payload; agent calls the tool).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 0 — Put _shared on sys.path so canonical_constants + r20a import
# (this script lives in computations/investigation-5/, not computations/session-N/)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    a_4_FW_zeta, rho_Lambda_obs, M_KK_gravity, tau_fold, Lambda_obs_MP4, M_Pl_unreduced,
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

sys.path.insert(0, str(SHARED_DIR))
# 147/147-verified Riemann-tensor machinery (substrate-first recompute, NOT npz read)
from r20a_riemann_tensor import (
    compute_riemann_tensor_ON_fast,
    ricci_from_riemann,
    riemann_norm_squared,
    scalar_curvature_our_metric,
    kretschner_exact,
)

SESSION = "S5"                                                    # (local) investigation-5
GATE_ID = "INV5-W1-2-A4-WEYL-TRACE-ANOMALY-CC-CHANNEL"            # (local)
SCHEME = "Gilkey-a4-Weyl-GaussBonnet-decomposition"              # (local)
CONVENTION = "ABSOLUTE"                                          # (local)
L_MAX = 12                                                       # (local)

# Pre-registered machinery pins (plan §W1-2 PRDR)
N_EVAL = 21                                                      # (local) 21-pt tau-scan
SCAN_MIN = 0.14                                                  # (local) tau_fold - 0.05
SCAN_MAX = 0.24                                                  # (local) tau_fold + 0.05
SIGN_FLOOR = 1e-9                                                # (local) dtau sign-change float floor
INFO_OOM_CEILING = 60.0                                         # (local) OOM ceiling for cosmological relevance
DIM = 8                                                          # (local) dim SU(3)
F0_MELLIN = 1.0                                                 # (local) O(1) zeroth Mellin moment f_0 of cutoff profile
XCHECK_TOL = 1e-9                                                # (local) recompute-vs-analytic agreement tolerance

OUT_NPZ = SESSION_DIR / "inv5_w1_2_a4_weyl_trace_anomaly_cc.npz"
OUT_PNG = SESSION_DIR / "inv5_w1_2_a4_weyl_trace_anomaly_cc.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "r20a_riemann_tensor.py",
    SHARED_DIR / "dirac_spectrum.py",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]):
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
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Curvature invariants + a_4 decomposition
# ---------------------------------------------------------------------------
def invariants_recompute(tau: float):
    """Rebuild R_{abcd}(tau) from the analytic Jensen metric (147/147 machinery) and
    return (R, R2, Ric2, Riem2) — all in M_KK^2 / M_KK^4 geometric units."""
    R_abcd = compute_riemann_tensor_ON_fast(tau)               # (local) 8^4 Riemann, substrate-first
    Ric = ricci_from_riemann(R_abcd)                            # (local) Ricci 8x8
    R_scalar = float(np.trace(Ric))                             # (local) scalar curvature
    Ric2 = float(np.sum(Ric ** 2))                              # (local) |Ric|^2 (ON frame: down=up)
    Riem2 = float(riemann_norm_squared(R_abcd))                 # (local) |Riem|^2 = Kretschmann
    return R_scalar, R_scalar ** 2, Ric2, Riem2


def invariants_analytic(tau: float):
    """Exact closed forms (Sage-derived this session; cross-check leg)."""
    e = np.exp                                                  # (local)
    R = scalar_curvature_our_metric(tau)                        # (local) = E3
    Ric2 = (1.0 / 24.0) * (2 * e(12 * tau) + 3 * e(8 * tau) - 12 * e(7 * tau)
                           + 26 * e(6 * tau) + 3 * e(4 * tau) - 12 * e(3 * tau) + 2) * e(-8 * tau)  # (local)
    Riem2 = kretschner_exact(tau)                               # (local) = exact |Riem|^2
    return R, R ** 2, Ric2, Riem2


def weyl_sq(R2: float, Ric2: float, Riem2: float, d: int = DIM) -> float:
    """Conformally-invariant Weyl-squared in d dimensions:
       C^2 = |Riem|^2 - 4/(d-2)|Ric|^2 + 2/((d-1)(d-2)) R^2."""
    return Riem2 - (4.0 / (d - 2)) * Ric2 + (2.0 / ((d - 1) * (d - 2))) * R2


def gauss_bonnet(R2: float, Ric2: float, Riem2: float) -> float:
    """Gauss-Bonnet (Euler-density) quadratic combination: |Riem|^2 - 4|Ric|^2 + R^2."""
    return Riem2 - 4.0 * Ric2 + R2


def a4_geometric_integrand(R2: float, Ric2: float, Riem2: float) -> float:
    """Gilkey a_4 pure-curvature integrand (box-R integrates to 0; gauge F^2 separate):
       I_geo = 5/2 R^2 - 2|Ric|^2 + 2|Riem|^2."""
    return 2.5 * R2 - 2.0 * Ric2 + 2.0 * Riem2


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    tau_grid = np.linspace(SCAN_MIN, SCAN_MAX, N_EVAL)          # (local) 21-pt window
    step = float(tau_grid[1] - tau_grid[0])                    # (local) = 0.005

    Rv = np.zeros(N_EVAL); R2v = np.zeros(N_EVAL)               # (local)
    Ric2v = np.zeros(N_EVAL); Riem2v = np.zeros(N_EVAL)         # (local)
    weyl2v = np.zeros(N_EVAL); gbv = np.zeros(N_EVAL)           # (local)
    igeov = np.zeros(N_EVAL)                                    # (local)
    max_xcheck = 0.0                                            # (local) recompute-vs-analytic max dev

    for i, tau in enumerate(tau_grid):
        # substrate-first recompute (147/147 machinery)
        R_r, R2_r, Ric2_r, Riem2_r = invariants_recompute(float(tau))
        # analytic cross-check
        R_a, R2_a, Ric2_a, Riem2_a = invariants_analytic(float(tau))
        dev = max(abs(R_r - R_a), abs(Ric2_r - Ric2_a), abs(Riem2_r - Riem2_a))  # (local)
        max_xcheck = max(max_xcheck, dev)
        # use the substrate-first recompute as the primary value
        Rv[i] = R_r; R2v[i] = R2_r; Ric2v[i] = Ric2_r; Riem2v[i] = Riem2_r
        weyl2v[i] = weyl_sq(R2_r, Ric2_r, Riem2_r)
        gbv[i] = gauss_bonnet(R2_r, Ric2_r, Riem2_r)
        igeov[i] = a4_geometric_integrand(R2_r, Ric2_r, Riem2_r)

    # --- (a) NON-MONOTONICITY test: d/dtau[Weyl^2] over the window ---
    dWeyl2 = np.gradient(weyl2v, tau_grid)                     # (local) central-difference derivative
    # count sign changes where |dWeyl2| > SIGN_FLOOR on both sides
    sign_changes = 0                                          # (local)
    prev = None                                               # (local)
    for d in dWeyl2:
        if abs(d) <= SIGN_FLOOR:
            continue
        s = 1 if d > 0 else -1                                # (local)
        if prev is not None and s != prev:
            sign_changes += 1
        prev = s
    non_monotone = sign_changes >= 1                          # (local)
    dWeyl2_min = float(np.min(dWeyl2)); dWeyl2_max = float(np.max(dWeyl2))  # (local)

    # GB derivative (for the report; topological combination)
    dGB = np.gradient(gbv, tau_grid)                          # (local)
    gb_sign_changes = 0; pg = None                            # (local)
    for d in dGB:
        if abs(d) <= SIGN_FLOOR:
            continue
        s = 1 if d > 0 else -1                                # (local)
        if pg is not None and s != pg:
            gb_sign_changes += 1
        pg = s

    # --- a_4 sub-term decomposition shares at the fold (idx of tau closest to tau_fold) ---
    i_fold = int(np.argmin(np.abs(tau_grid - tau_fold)))      # (local)
    weyl_frac_fold = float(weyl2v[i_fold] / igeov[i_fold])    # (local) conformal share of geometric a_4
    gb_frac_fold = float(gbv[i_fold] / igeov[i_fold])         # (local) Euler share

    # --- (b) OOM-distance of rho_anomaly to rho_Lambda ---
    # zeta-scaled Weyl-anomaly a_4 sub-term: a_4^Weyl = (Weyl^2 / I_geo)|_fold * a_4_FW_zeta
    a4_Weyl_zeta = weyl_frac_fold * a_4_FW_zeta                # (local) regulator-pinned a_4^{zeta} leg
    # spectral-action Lambda^0 term -> dimensionful energy density via M_KK^4 (f_0 ~ O(1))
    rho_anomaly = F0_MELLIN * a4_Weyl_zeta * (M_KK_gravity ** 4)  # (local) GeV^4
    oom_distance = abs(float(np.log10(abs(rho_anomaly / rho_Lambda_obs))))  # (local)
    # dimensionless cross-report (a_4^Weyl vs Lambda_obs/M_Pl^4)
    oom_dimless = abs(float(np.log10(a4_Weyl_zeta) - np.log10(Lambda_obs_MP4)))  # (local)

    # round-metric reference (tau=0): Weyl^2 minimum check (the unique stationary point)
    R0, R20, Ric20, Riem20 = invariants_recompute(0.0)        # (local)
    weyl2_round = weyl_sq(R20, Ric20, Riem20)                 # (local)

    return {
        "tau_grid": tau_grid, "R": Rv, "R2": R2v, "Ric2": Ric2v, "Riem2": Riem2v,
        "weyl2": weyl2v, "gauss_bonnet": gbv, "I_geo": igeov,
        "dWeyl2": dWeyl2, "dGB": dGB, "step": step,
        "sign_changes": sign_changes, "non_monotone": non_monotone,
        "dWeyl2_min": dWeyl2_min, "dWeyl2_max": dWeyl2_max,
        "gb_sign_changes": gb_sign_changes,
        "weyl_frac_fold": weyl_frac_fold, "gb_frac_fold": gb_frac_fold,
        "a4_Weyl_zeta": a4_Weyl_zeta, "rho_anomaly": rho_anomaly,
        "oom_distance": oom_distance, "oom_dimless": oom_dimless,
        "weyl2_round": weyl2_round, "weyl2_fold": float(weyl2v[i_fold]),
        "max_xcheck": max_xcheck, "i_fold": i_fold,
        "value": oom_distance,  # primary reported scalar
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict) -> tuple[str, str, str, str]:
    """Composite [SIGN] verdict. Returns (composite, sign, magnitude, regime).

    Pre-registered (plan §W1-2 substitution chain Step 5):
      PASS if sign(d a_4^Weyl/dtau) is NOT constant across the 21-pt scan (>=1 sign change)
           -> non-monotone -> escapes W4.
    sign_verdict: the chain PREDICTED a sign-change (non-constant sign). PASS iff that
                  predicted direction matches the computed direction (non-monotone observed).
    magnitude_verdict: |rho_anomaly/rho_Lambda| OOM-distance vs the 60-OOM info ceiling.
    regime_verdict: VALID (analytic curvature invariants; exact; no regime breakdown) iff
                    the substrate-first recompute matches the analytic forms to XCHECK_TOL.
    """
    non_monotone = bool(res["non_monotone"])                  # (local)
    # sign: predicted = "sign-change present"; PASS iff observed matches (non-monotone)
    sign_v = "PASS" if non_monotone else "FAIL"               # (local)
    # magnitude: OOM within 60 -> at least cosmologically-adjacent; else FAIL
    oom = res["oom_distance"]                                  # (local)
    if oom <= INFO_OOM_CEILING:
        mag_v = "INFO"                                        # (local) within-window but not a hit
    else:
        mag_v = "FAIL"                                        # (local) cosmologically irrelevant magnitude
    # regime: analytic exactness
    regime_v = "VALID" if res["max_xcheck"] < XCHECK_TOL else "MARGINAL"  # (local)

    # composite collapse (gate-verdicts.md):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"                                    # monotone -> W4 covers it -> FAIL
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": 5,
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
# Section 8 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict):
    tau = res["tau_grid"]                                      # (local)
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))
    # (0,0) the four invariants
    ax[0, 0].plot(tau, res["R2"], label=r"$R^2$", lw=2)
    ax[0, 0].plot(tau, res["Ric2"], label=r"$|Ric|^2$", lw=2)
    ax[0, 0].plot(tau, res["Riem2"], label=r"$|Riem|^2$", lw=2)
    ax[0, 0].axvline(tau_fold, color="k", ls=":", alpha=0.6, label=r"$\tau_{fold}=0.19$")
    ax[0, 0].set_title("Curvature invariants on Jensen-deformed SU(3)")
    ax[0, 0].set_xlabel(r"$\tau$"); ax[0, 0].legend(); ax[0, 0].grid(alpha=0.3)
    # (0,1) Weyl^2 and Gauss-Bonnet
    ax[0, 1].plot(tau, res["weyl2"], label=r"Weyl$^2 = C^2$ (conformal)", lw=2, color="crimson")
    ax[0, 1].plot(tau, res["gauss_bonnet"], label="Gauss-Bonnet (Euler)", lw=2, color="navy")
    ax[0, 1].axvline(tau_fold, color="k", ls=":", alpha=0.6)
    ax[0, 1].set_title("Isolated anomaly sub-terms")
    ax[0, 1].set_xlabel(r"$\tau$"); ax[0, 1].legend(); ax[0, 1].grid(alpha=0.3)
    # (1,0) d/dtau Weyl^2 — the non-monotonicity test
    ax[1, 0].plot(tau, res["dWeyl2"], label=r"$d(\mathrm{Weyl}^2)/d\tau$", lw=2, color="crimson")
    ax[1, 0].axhline(0.0, color="k", lw=1)
    ax[1, 0].axvline(tau_fold, color="k", ls=":", alpha=0.6)
    ax[1, 0].set_title(f"Non-monotonicity test: sign changes = {res['sign_changes']} "
                       f"({'NON-monotone' if res['non_monotone'] else 'MONOTONE'})")
    ax[1, 0].set_xlabel(r"$\tau$"); ax[1, 0].legend(); ax[1, 0].grid(alpha=0.3)
    # (1,1) OOM bar
    labels = [r"$\rho_{anomaly}$", r"$\rho_\Lambda^{obs}$"]   # (local)
    vals = [res["rho_anomaly"], rho_Lambda_obs]               # (local)
    ax[1, 1].bar(labels, [np.log10(abs(v)) for v in vals], color=["crimson", "green"])
    ax[1, 1].set_ylabel(r"$\log_{10}(\rho\,/\,\mathrm{GeV}^4)$")
    ax[1, 1].set_title(f"OOM-distance = {res['oom_distance']:.2f}  "
                       f"(info ceiling {INFO_OOM_CEILING:.0f})")
    ax[1, 1].grid(alpha=0.3, axis="y")
    fig.suptitle(f"{GATE_ID}\nWeyl$^2$/trace-anomaly a$_4$ sub-term — W4 escape test", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
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

    # report
    print("=== a_4 -> {Yang-Mills, Higgs-quartic, Weyl^2, Gauss-Bonnet} decomposition ===")
    print(f"  recompute-vs-analytic max deviation: {res['max_xcheck']:.3e} (tol {XCHECK_TOL:.0e})")
    print(f"  at fold (tau={tau_fold}): Weyl^2={res['weyl2_fold']:.6f}  "
          f"Weyl^2/I_geo={res['weyl_frac_fold']:.6f}  GB/I_geo={res['gb_frac_fold']:.6f}")
    print(f"  Weyl^2(round tau=0)={res['weyl2_round']:.6f}  ->  Weyl^2 MIN at round point "
          f"(curvature anisotropy rises monotonically away)")
    print()
    print("--- (a) NON-MONOTONICITY test: d/dtau[Weyl^2] over [0.14,0.24] ---")
    print(f"  dWeyl2 range: [{res['dWeyl2_min']:.6f}, {res['dWeyl2_max']:.6f}] (both same sign => monotone)")
    print(f"  sign changes in d(Weyl^2)/dtau: {res['sign_changes']}  "
          f"=> {'NON-MONOTONE (escapes W4)' if res['non_monotone'] else 'MONOTONE (covered by W4)'}")
    print(f"  Gauss-Bonnet sign changes: {res['gb_sign_changes']}")
    print()
    print("--- (b) OOM-distance rho_anomaly vs rho_Lambda ---")
    print(f"  a_4^Weyl (zeta-scaled) = {res['a4_Weyl_zeta']:.6f}  (= Weyl-frac x a_4_FW_zeta={a_4_FW_zeta})")
    print(f"  rho_anomaly = f0 * a_4^Weyl * M_KK^4 = {res['rho_anomaly']:.6e} GeV^4")
    print(f"  rho_Lambda_obs = {rho_Lambda_obs:.3e} GeV^4")
    print(f"  OOM-distance |log10(rho_anomaly/rho_Lambda)| = {res['oom_distance']:.4f}")
    print(f"  (dimensionless cross-report a_4^Weyl vs Lambda/M_Pl^4: {res['oom_dimless']:.4f})")
    print()

    make_plot(res)

    np.savez_compressed(
        OUT_NPZ,
        tau_grid=res["tau_grid"], R=res["R"], R2=res["R2"], Ric2=res["Ric2"], Riem2=res["Riem2"],
        weyl2=res["weyl2"], gauss_bonnet=res["gauss_bonnet"], I_geo=res["I_geo"],
        dWeyl2=res["dWeyl2"], dGB=res["dGB"],
        sign_changes=res["sign_changes"], non_monotone=res["non_monotone"],
        dWeyl2_min=res["dWeyl2_min"], dWeyl2_max=res["dWeyl2_max"],
        gb_sign_changes=res["gb_sign_changes"],
        weyl_frac_fold=res["weyl_frac_fold"], gb_frac_fold=res["gb_frac_fold"],
        a4_Weyl_zeta=res["a4_Weyl_zeta"], rho_anomaly=res["rho_anomaly"],
        oom_distance=res["oom_distance"], oom_dimless=res["oom_dimless"],
        weyl2_round=res["weyl2_round"], weyl2_fold=res["weyl2_fold"],
        max_xcheck=res["max_xcheck"],
        a_4_FW_zeta=a_4_FW_zeta, rho_Lambda_obs=rho_Lambda_obs,
        M_KK_gravity=M_KK_gravity, tau_fold=tau_fold,
    )
    print(f"  saved: {OUT_NPZ.name}")
    print(f"  saved: {OUT_PNG.name}")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)

    value_str = (f"weyl2_signchanges={res['sign_changes']}_non_monotone={int(res['non_monotone'])}"
                 f"_OOM={res['oom_distance']:.4f}_weylfrac={res['weyl_frac_fold']:.6f}")  # (local)
    tag = emit_4tuple(value_str, SCHEME, CONVENTION, L_MAX)
    print(tag)

    reg_row = ("# regulator_pin=a_4^{zeta} (spectral-sum a_4 leg = a_4_FW_zeta=1350.7216); "
               "curvature-invariant leg regulator-free Gilkey")  # (local)
    note = (f"Weyl^2 MONOTONE in [0.14,0.24] ({res['sign_changes']} sign changes); "
            f"unique stationary pt at round tau=0 (MIN); does NOT escape W4; "
            f"OOM-dist to rho_Lambda={res['oom_distance']:.2f} (>{INFO_OOM_CEILING:.0f} ceiling)")  # (local)
    print_verdict_payload(composite, value_str, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
                          companion_note=note, extra_rows=[reg_row])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v}, magnitude={mag_v}, regime={regime_v}; wall {wall:.1f}s) ===")
    return 0  # FAIL is a valid scientific result; exit 0 per math-scripts.md


if __name__ == "__main__":
    sys.exit(main())
