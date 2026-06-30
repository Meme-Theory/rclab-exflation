#!/usr/bin/env python3
"""
S101 W3 — S101-W3-PRONGB-WINDOWED — window-corrected prong-B shell-exponent closure
==================================================================================

Gate: S101-W3-PRONGB-WINDOWED ([VERIFY])

Pre-registered threshold (plan §W1-3, two BUNDLED conjuncts declared at plan-freeze):
  PASS = ( max over {5,6,7} x {A,B} of |exp_meas(tau_fold) - exp_exact_tau0(window)| < 0.25 )
       AND ( Hankel |c_-2|/max(|c_-1|,|c_0|) < 1e-8 at each s_A in {2.5, 3, 3.5} )
  FAIL = a Delta-cell >= 0.25 (genuine tau-deformation anomaly, window subtraction built in)
         OR a Hankel ratio >= 1e-8 (hidden double-pole off the integer mesh).
  INFO = split outcome (shell band PASS but Hankel breach, or vice versa) OR rank-deficient fit.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-100b/s100b_cf28_simple_pole_preflight.npz
        (fields: shell_A, shell_B, shell_fits, tau0_window_diag, evals_44_reconstructed, lineage)
  - computations/_shared/_analytic_zeta.py  (off-pole Hankel corridor machinery)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max_Delta|max_Hankel_ratio composite>, scheme=window-corrected-shell-exponent+off-pole-Hankel,
   convention=poleconv-DUAL-declared-SU3-algebra, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
The S100b prong-B clause (S100b-CF28-SIMPLE-POLE-PREFLIGHT, composite INFO verdict line 33)
measured the tau_fold shell-sum exponents on an L in [6,12] window and found them OFF the
asymptotic analytic exponents (7-2s for family A = double-power lambda^{-2s}; 7-s for family B
= single-power lambda^{-s}). The same script established the miss is a WINDOW property, not a
tau or pole-order property: the EXACT tau=0 cubic-point closed form, fitted on the IDENTICAL
window with the IDENTICAL log-log procedure, reproduces the miss in the same direction
(tau0_window_diag dev = 0.575 / 0.959 / 1.342 at s = 5 / 6 / 7).

This gate closes the clause under the window-corrected pre-registration: instead of comparing
exp_meas(tau_fold) to the ASYMPTOTIC exponent, compare it to the EXACT tau=0 exponent fitted
on the SAME window. The common window-truncation bias cancels in the DIFFERENCE
Delta(s,F) = |exp_meas(tau_fold; s,F) - exp_exact_tau0(window; s,F)|, leaving only the
tau-deformation residual. A bundled off-pole Hankel re-check (contour_laurent around
s_A in {2.5, 3, 3.5} via _analytic_zeta.analytic_zeta) confirms the finite truncation carries
no double-pole structure (c_-2 ~ machine zero) off the integer pole mesh. No new diagonalization
- the tau_fold shell profiles ride the s100b npz; the tau=0 side uses the same cubic-point closed
form; the Hankel leg uses the L=12 s84-cache spectrum already in _analytic_zeta.

Family-label discipline (load-bearing): the npz tau0_window_diag stores ONLY the family-A
exact-window exponent (its closed form raises lam2 = u^2+uv+v^2 = lambda^2 to ^{-s}, i.e.
lambda^{-2s} = the double-power family A). For a faithful identical-window Delta on BOTH
families, the family-B exact-window exponent is recomputed here with the IDENTICAL cubic-point
machinery but lam2^{-s/2} = lambda^{-s} (matching shell_B's single-power form). The family-A
recomputation is cross-checked bit-for-bit against the stored exp_tau0_window (anchor).

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- mp.dps = 50 (off-pole integrand precision pin, matches _analytic_zeta + the parent route-2).
- contour_laurent R = 0.1, nquad = 64 (matches the parent's route-2 contour pins exactly).
- SHA-256 of all input files logged in first 20 lines of stdout; dual-SHA (S84+) emitted.
- Verdict emitted via the emit_verdict knowledge-MCP tool (race-safe); script PRINTS the payload.
- a19_extra_row_rule: emission-time check on whether W1-1's L4 lift rows are present in
  s101_gate_verdicts.txt; ELSE (file absent / rows not present) carry the A19 UNTRUSTED-UPSTREAM
  extra-row patterned on the S100b rows. The verdict VALUE is identical either way.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — environment + path bootstrap (CPU cap BEFORE numpy; _shared on
# sys.path BEFORE the canonical import — matches the parent prong-B script)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
import re
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import tau_fold, d_spec  # explicit (provenance for the window/regime)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mpmath as mp

# off-pole Hankel corridor machinery (the L=12 s84-cache spectrum lives inside it)
from _analytic_zeta import analytic_zeta, zeta_D_direct  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S101"                                                  # (local)
GATE_ID = "S101-W3-PRONGB-WINDOWED"                               # (local)
SCHEME = "window-corrected-shell-exponent+off-pole-Hankel"        # (local)
CONVENTION = "poleconv-DUAL-declared-SU3-algebra"                 # (local)
L_MAX = 12                                                        # (local) window inherited from prong-B; NO new diagonalization

# Pre-registered pass/fail thresholds (define BEFORE running) ----------------
SHELL_BAND = 0.25            # (local) window-corrected shell-exponent band, absolute, strict <
HANKEL_RATIO_EPS = 1e-8      # (local) off-pole double-pole ratio threshold, strict <
S_NUMERALS = [5.0, 6.0, 7.0]            # (local) shell families' s-numerals
FAMILIES = ["A", "B"]                   # (local) A=double-power lambda^{-2s}; B=single-power lambda^{-s}
HANKEL_SA = [2.5, 3.0, 3.5]             # (local) off-pole Hankel s_A points (Conv.A; only 3.0 on a pole)
WINDOW_LFIT = np.arange(6, 13)          # (local) the L in [6,12] shell-fit window (matches parent prong_b/tau0_window_diag)
MP_DPS = 50                             # (local) off-pole integrand precision pin (parent route-2 + _analytic_zeta)
CONTOUR_R = 0.1                         # (local) route-2 contour radius pin (parent CONTOUR_R)
N_QUAD = 64                             # (local) trapezoid nodes pin (parent N_QUAD)

mp.mp.dps = MP_DPS

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s101_w3_prongb_windowed.npz"
OUT_PNG = SESSION_DIR / "s101_w3_prongb_windowed.png"
VERDICTS_FILE = SESSION_DIR / "s101_gate_verdicts.txt"           # (local) READ-ONLY here (a19 emission-time check); written by emit_verdict tool

PRONGB_NPZ = COMPUTATIONS_DIR / "session-100b" / "s100b_cf28_simple_pole_preflight.npz"
ANALYTIC_ZETA = SHARED_DIR / "_analytic_zeta.py"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PRONGB_NPZ,
    ANALYTIC_ZETA,
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
    pins: dict = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def loglog_slope(L_arr: np.ndarray, y_arr: np.ndarray) -> float:
    """OLS log-log slope, matching the parent's np.polyfit(log L, log y, 1)[0]."""
    return float(np.polyfit(np.log(L_arr), np.log(y_arr), 1)[0])


def tau_fold_measured_exponents(shell_A: dict, shell_B: dict) -> dict:
    """exp_meas(tau_fold; s, F) reproduced from the stored tau_fold shell partial sums.

    Family A = shell_A (lambda^{-2s} double-power); family B = shell_B (lambda^{-s} single-power).
    Reproduces shell_fits.exp_A_meas / exp_B_meas bit-for-bit (anchor cross-check below).
    """
    out = {}  # (local)
    for s in S_NUMERALS:
        key = str(s)  # (local) JSON keys are "5.0"/"6.0"/"7.0"
        yA = np.array([shell_A[key][str(int(L))] for L in WINDOW_LFIT])  # (local)
        yB = np.array([shell_B[key][str(int(L))] for L in WINDOW_LFIT])  # (local)
        out[s] = {"A": loglog_slope(WINDOW_LFIT, yA),
                  "B": loglog_slope(WINDOW_LFIT, yB),
                  "yA": yA, "yB": yB}
    return out


def tau0_exact_window_exponents() -> dict:
    """exp_exact_tau0(window; s, F): the EXACT tau=0 cubic-point closed form fitted on the
    IDENTICAL L in [6,12] window with the IDENTICAL log-log procedure.

    Cubic-point shell at u+v = N = L+2: lam2 = u^2+uv+v^2 (the Casimir = lambda^2);
    multiplicity weight wt = 4 (uv)^2 N^2.
      Family A: lam2^{-s}     = lambda^{-2s}  (double-power) -> reproduces stored exp_tau0_window
      Family B: lam2^{-s/2}   = lambda^{-s}   (single-power) -> matches shell_B's lambda^{-s}
    """
    out = {}  # (local)
    for s in S_NUMERALS:
        shA = []  # (local)
        shB = []  # (local)
        shapes = []  # (local) (kept for diagnostics; per-L shell magnitudes)
        for L in WINDOW_LFIT:
            N = int(L) + 2                                       # (local) u+v = p+q+2
            u = np.arange(1, N, dtype=np.float64)                # (local)
            v = N - u                                            # (local)
            lam2 = u * u + u * v + v * v                         # (local) = lambda^2
            wt = 4.0 * (u * v) ** 2 * N ** 2                     # (local) cubic-point multiplicity weight
            valA = float(np.sum(wt * lam2 ** (-s)))              # (local) lambda^{-2s}
            valB = float(np.sum(wt * lam2 ** (-s / 2.0)))        # (local) lambda^{-s}
            shA.append(valA)
            shB.append(valB)
            shapes.append((valA, valB))
        out[s] = {"A": loglog_slope(WINDOW_LFIT, np.array(shA)),
                  "B": loglog_slope(WINDOW_LFIT, np.array(shB)),
                  "shA": np.array(shA), "shB": np.array(shB)}
    return out


def contour_laurent(fev, s_star: float, R: float = CONTOUR_R, nquad: int = N_QUAD):
    """Trapezoid Fourier extraction of (c_-2, c_-1, c_0) on |s - s*| = R.

    EXACT copy of the parent s100b route-2 machinery (CONTOUR_R = 0.1, N_QUAD = 64):
      c_-2 = (R^2/n) sum_k f(s*+Rz_k) z_k^2 ;  c_-1 = (R/n) sum_k f z_k ;  c_0 = (1/n) sum_k f
    For a finite-L truncation the function is a finite Dirichlet sum (no genuine pole), so
    c_-2 -> machine zero (quadrature noise); ratio |c_-2|/max(|c_-1|,|c_0|) << 1e-8 confirms
    no hidden double pole off the integer mesh.
    """
    cm2 = mp.mpc(0)  # (local)
    cm1 = mp.mpc(0)  # (local)
    c0 = mp.mpc(0)   # (local)
    Rm = mp.mpf(str(R))  # (local)
    for kk in range(nquad):
        th = 2 * mp.pi * kk / nquad                              # (local)
        z = mp.mpc(mp.cos(th), mp.sin(th))                       # (local)
        fz = fev(mp.mpf(str(s_star)) + Rm * z)                   # (local)
        cm2 += fz * z ** 2
        cm1 += fz * z
        c0 += fz
    cm2 = cm2 * (Rm ** 2) / nquad
    cm1 = cm1 * Rm / nquad
    c0 = c0 / nquad
    return cm2, cm1, c0


def compute() -> dict:
    # --- Load the prong-B npz (no new diagonalization) ---
    d = np.load(PRONGB_NPZ, allow_pickle=True)  # (local)
    shell_A = json.loads(d["shell_A"].item())   # (local) tau_fold double-power partial sums
    shell_B = json.loads(d["shell_B"].item())   # (local) tau_fold single-power partial sums
    shell_fits = json.loads(d["shell_fits"].item())        # (local) stored tau_fold exponents (anchor)
    tau0_diag = json.loads(d["tau0_window_diag"].item())   # (local) stored family-A exact-window exponent (anchor)
    lineage = json.loads(d["lineage"].item())              # (local) (2,2)/(4,3) reconstruction homology errors (a19 lineage)
    window_artifact_flag = bool(d["window_artifact"][0])   # (local) S100b finding: True

    # ========== LEG 1: window-corrected shell exponents ==========
    meas = tau_fold_measured_exponents(shell_A, shell_B)  # (local)
    t0 = tau0_exact_window_exponents()                    # (local)

    # Anchor cross-checks (bit-for-bit reproduction of stored numbers) ---------
    anchor_meas_max = 0.0  # (local) max|reproduced - stored| over tau_fold measured exponents
    anchor_t0A_max = 0.0   # (local) max|reproduced - stored| over tau=0 family-A window exponent
    for s in S_NUMERALS:
        key = str(s)  # (local)
        anchor_meas_max = max(anchor_meas_max,
                              abs(meas[s]["A"] - float(shell_fits[key]["exp_A_meas"])),
                              abs(meas[s]["B"] - float(shell_fits[key]["exp_B_meas"])))
        anchor_t0A_max = max(anchor_t0A_max,
                             abs(t0[s]["A"] - float(tau0_diag[key]["exp_tau0_window"])))

    # Delta(s, F) = |exp_meas(tau_fold) - exp_exact_tau0(window)| ---------------
    delta_table = {}  # (local)
    max_delta = 0.0   # (local)
    max_delta_cell = None  # (local)
    for s in S_NUMERALS:
        for F in FAMILIES:
            dd = abs(meas[s][F] - t0[s][F])  # (local)
            delta_table[(s, F)] = {
                "exp_meas_tau_fold": meas[s][F],
                "exp_exact_tau0_window": t0[s][F],
                "delta": dd,
                "in_band": bool(dd < SHELL_BAND),
            }
            if dd > max_delta:
                max_delta = dd
                max_delta_cell = (s, F)

    shell_pass = bool(max_delta < SHELL_BAND)  # (local)

    # rank-deficiency check on each window fit (INFO branch guard) --------------
    # window has 7 points (L=6..12); a 1-D OLS slope needs >= 2 distinct log-L; always satisfied,
    # but flag any non-finite / non-positive shell value that would corrupt the log.
    fit_rank_ok = True  # (local)
    for s in S_NUMERALS:
        for arr in (meas[s]["yA"], meas[s]["yB"], t0[s]["shA"], t0[s]["shB"]):
            if not (np.all(np.isfinite(arr)) and np.all(arr > 0)):
                fit_rank_ok = False

    # ========== LEG 2 (BUNDLED): off-pole Hankel pole-order re-check ==========
    fev = lambda s: mp.mpc(analytic_zeta(complex(s), L_MAX))  # (local) wraps the off-pole continuation
    hankel_table = {}  # (local)
    max_hankel_ratio = 0.0  # (local)
    max_hankel_cell = None  # (local)
    for sa in HANKEL_SA:
        cm2, cm1, c0 = contour_laurent(fev, sa)  # (local)
        acm2 = float(abs(cm2)); acm1 = float(abs(cm1)); ac0 = float(abs(c0))  # (local)
        denom = max(acm1, ac0, 1e-30)  # (local)
        ratio = acm2 / denom           # (local)
        # off-pole sanity: analytic_zeta(sa) must equal the direct truncated Dirichlet form
        direct = complex(zeta_D_direct(complex(sa), L_MAX))  # (local)
        contin = complex(analytic_zeta(complex(sa), L_MAX))  # (local)
        offpole_rel = abs(contin - direct) / max(abs(direct), 1e-300)  # (local)
        hankel_table[sa] = {
            "c_m2_abs": acm2, "c_m1_abs": acm1, "c_0_abs": ac0,
            "ratio": ratio, "in_band": bool(ratio < HANKEL_RATIO_EPS),
            "offpole_rel_dev": offpole_rel,
            "c_m2_re": float(cm2.real), "c_m2_im": float(cm2.imag),
            "c_m1_re": float(cm1.real), "c_m1_im": float(cm1.imag),
            "c_0_re": float(c0.real), "c_0_im": float(c0.imag),
        }
        if ratio > max_hankel_ratio:
            max_hankel_ratio = ratio
            max_hankel_cell = sa

    hankel_pass = bool(max_hankel_ratio < HANKEL_RATIO_EPS)  # (local)

    # ========== composite verdict ==========
    if not fit_rank_ok:
        verdict = "INFO"  # (local) rank-deficient fit guard
    elif shell_pass and hankel_pass:
        verdict = "PASS"  # (local)
    elif shell_pass != hankel_pass:
        verdict = "INFO"  # (local) split outcome: one conjunct closes, the other routes as a named residual
    else:
        verdict = "FAIL"  # (local) both conjuncts breach

    # value payload (no single-quote chars; the emit_verdict tool wraps value='...')
    value = (f"maxDelta={max_delta:.3f}@s{int(max_delta_cell[0])}{max_delta_cell[1]}"
             f"<{SHELL_BAND}|maxHankel={max_hankel_ratio:.2e}@sA{max_hankel_cell}"
             f"<{HANKEL_RATIO_EPS:.0e}|shell={'PASS' if shell_pass else 'FAIL'}"
             f"|hankel={'PASS' if hankel_pass else 'FAIL'}")  # (local)

    return {
        "value": value,
        "verdict": verdict,
        "max_delta": max_delta,
        "max_delta_cell": max_delta_cell,
        "shell_pass": shell_pass,
        "max_hankel_ratio": max_hankel_ratio,
        "max_hankel_cell": max_hankel_cell,
        "hankel_pass": hankel_pass,
        "delta_table": delta_table,
        "hankel_table": hankel_table,
        "meas": meas,
        "t0": t0,
        "anchor_meas_max": anchor_meas_max,
        "anchor_t0A_max": anchor_t0A_max,
        "fit_rank_ok": fit_rank_ok,
        "window_artifact_flag": window_artifact_flag,
        "lineage": lineage,
    }


# ---------------------------------------------------------------------------
# Section 6 — a19 emission-time extra-row rule
# ---------------------------------------------------------------------------

def build_a19_extra_rows(lineage: dict) -> list:
    """Pre-registered emission-time check (plan §W1-3 a19_extra_row_rule).

    IF W1-1's L4 lift rows are already present in s101_gate_verdicts.txt at this gate's
    emission -> cite the prong-B lineage full-confidence (s84 RE-LABEL covers the W3-1
    prong-B 1.91e-14/4.13e-14 lineage). ELSE -> carry the A19 UNTRUSTED-UPSTREAM extra-row
    patterned on the S100b rows. The verdict VALUE is identical either way (annotation only).
    """
    w1_1_present = False  # (local)
    if VERDICTS_FILE.exists():
        txt = VERDICTS_FILE.read_text(encoding="utf-8", errors="replace")  # (local)
        # W1-1 L4 lift lands the s84 RE-LABEL + the s100b lift extra-rows under S101-TAU0-OPERATOR-CANONICITY
        w1_1_present = bool(re.search(r"^S101-TAU0-OPERATOR-CANONICITY:\s*(PASS|FAIL|INFO)",
                                      txt, re.MULTILINE))
    # lineage homology errors (the prong-B reconstruction provenance)
    le_22 = lineage.get("(2, 2)", {}).get("max_abs_diff", float("nan"))  # (local)
    le_43 = lineage.get("(4, 3)", {}).get("max_abs_diff", float("nan"))  # (local)
    if w1_1_present:
        row = ("# a19_lineage=FULL-CONFIDENCE: W1-1 L4 lift rows present in "
               "s101_gate_verdicts.txt (S101-TAU0-OPERATOR-CANONICITY landed); s84 RE-LABEL "
               f"covers the prong-B (2,2)/(4,3) reconstruction lineage "
               f"max_abs_diff={le_22:.2e}/{le_43:.2e} (hom-exact); s84-cache IS the LC spectrum")
    else:
        row = ("# a19_lineage=UNTRUSTED-UPSTREAM: W1-1 L4 lift rows NOT yet in "
               "s101_gate_verdicts.txt at emission; prong-B (2,2)/(4,3) reconstruction lineage "
               f"max_abs_diff={le_22:.2e}/{le_43:.2e} (hom-exact) cited pending the s84 RE-LABEL "
               "(cross-wave pin 1; annotation only, NOT a verdict modifier)")
    return [row], w1_1_present


# ---------------------------------------------------------------------------
# Section 7 — verdict payload printer (template-conform; emit via MCP tool)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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
# Section 8 — plot
# ---------------------------------------------------------------------------

def make_plot(res: dict):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: Delta(s, F) bars vs +/-0.25 band
    labels = []  # (local)
    deltas = []  # (local)
    colors = []  # (local)
    for s in S_NUMERALS:
        for F in FAMILIES:
            labels.append(f"s={int(s)}\n{F}")
            dd = res["delta_table"][(s, F)]["delta"]  # (local)
            deltas.append(dd)
            colors.append("#2a7" if dd < SHELL_BAND else "#c33")
    x = np.arange(len(labels))  # (local)
    ax1.bar(x, deltas, color=colors, width=0.6)
    ax1.axhline(SHELL_BAND, color="k", ls="--", lw=1.3, label=f"band = {SHELL_BAND}")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels, fontsize=9)
    ax1.set_ylabel(r"$\Delta(s,F)=|{\rm exp}_{\rm meas}(\tau_{\rm fold})-{\rm exp}_{\rm exact}^{\tau=0}({\rm window})|$")
    ax1.set_title(f"Window-corrected shell exponents (max $\\Delta$={res['max_delta']:.3f})")
    ax1.set_ylim(0, max(SHELL_BAND * 1.25, max(deltas) * 1.3))
    ax1.legend(loc="upper right", fontsize=9)
    ax1.grid(axis="y", alpha=0.3)

    # Panel 2: Hankel double-pole ratio vs 1e-8 (log scale)
    sa_labels = [f"$s_A$={sa}" + ("\n(pole)" if abs(sa - 3.0) < 1e-9 else "") for sa in HANKEL_SA]  # (local)
    ratios = [res["hankel_table"][sa]["ratio"] for sa in HANKEL_SA]  # (local)
    ratios_floor = [max(r, 1e-99) for r in ratios]  # (local) for log plot
    xb = np.arange(len(HANKEL_SA))  # (local)
    ax2.bar(xb, ratios_floor, color="#37a", width=0.5)
    ax2.axhline(HANKEL_RATIO_EPS, color="k", ls="--", lw=1.3, label=f"threshold = {HANKEL_RATIO_EPS:.0e}")
    ax2.set_yscale("log")
    ax2.set_xticks(xb)
    ax2.set_xticklabels(sa_labels, fontsize=9)
    ax2.set_ylabel(r"$|c_{-2}|/\max(|c_{-1}|,|c_0|)$")
    ax2.set_title("Off-pole Hankel double-pole ratio (finite truncation: no pole)")
    ax2.legend(loc="upper right", fontsize=9)
    ax2.grid(axis="y", alpha=0.3)

    fig.suptitle(f"{GATE_ID} — window-corrected prong-B closure  "
                 f"[shell {'PASS' if res['shell_pass'] else 'FAIL'} / "
                 f"Hankel {'PASS' if res['hankel_pass'] else 'FAIL'}]", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — npz save
# ---------------------------------------------------------------------------

def save_npz(res: dict):
    # per-cell Delta table (flat arrays)
    cells = [(s, F) for s in S_NUMERALS for F in FAMILIES]  # (local)
    s_arr = np.array([c[0] for c in cells])                # (local)
    F_arr = np.array([c[1] for c in cells])                # (local)
    exp_meas = np.array([res["delta_table"][c]["exp_meas_tau_fold"] for c in cells])      # (local)
    exp_t0 = np.array([res["delta_table"][c]["exp_exact_tau0_window"] for c in cells])    # (local)
    delta_arr = np.array([res["delta_table"][c]["delta"] for c in cells])                 # (local)
    inband_arr = np.array([res["delta_table"][c]["in_band"] for c in cells])              # (local)

    # Hankel Laurent triples
    sa_arr = np.array(HANKEL_SA)  # (local)
    cm2_abs = np.array([res["hankel_table"][sa]["c_m2_abs"] for sa in HANKEL_SA])  # (local)
    cm1_abs = np.array([res["hankel_table"][sa]["c_m1_abs"] for sa in HANKEL_SA])  # (local)
    c0_abs = np.array([res["hankel_table"][sa]["c_0_abs"] for sa in HANKEL_SA])    # (local)
    ratio_arr = np.array([res["hankel_table"][sa]["ratio"] for sa in HANKEL_SA])   # (local)
    hk_inband = np.array([res["hankel_table"][sa]["in_band"] for sa in HANKEL_SA]) # (local)
    offpole_rel = np.array([res["hankel_table"][sa]["offpole_rel_dev"] for sa in HANKEL_SA])  # (local)
    cm2_re = np.array([res["hankel_table"][sa]["c_m2_re"] for sa in HANKEL_SA])  # (local)
    cm2_im = np.array([res["hankel_table"][sa]["c_m2_im"] for sa in HANKEL_SA])  # (local)
    cm1_re = np.array([res["hankel_table"][sa]["c_m1_re"] for sa in HANKEL_SA])  # (local)
    cm1_im = np.array([res["hankel_table"][sa]["c_m1_im"] for sa in HANKEL_SA])  # (local)
    c0_re = np.array([res["hankel_table"][sa]["c_0_re"] for sa in HANKEL_SA])    # (local)
    c0_im = np.array([res["hankel_table"][sa]["c_0_im"] for sa in HANKEL_SA])    # (local)

    np.savez(
        OUT_NPZ,
        # shell leg
        s_numeral=s_arr, family=F_arr,
        exp_meas_tau_fold=exp_meas, exp_exact_tau0_window=exp_t0,
        delta=delta_arr, delta_in_band=inband_arr,
        shell_band=np.array([SHELL_BAND]),
        max_delta=np.array([res["max_delta"]]),
        max_delta_cell=np.array([f"s{int(res['max_delta_cell'][0])}{res['max_delta_cell'][1]}"], dtype=object),
        shell_pass=np.array([res["shell_pass"]]),
        anchor_meas_max=np.array([res["anchor_meas_max"]]),
        anchor_t0A_max=np.array([res["anchor_t0A_max"]]),
        fit_rank_ok=np.array([res["fit_rank_ok"]]),
        window_artifact_flag=np.array([res["window_artifact_flag"]]),
        # Hankel leg
        hankel_s_A=sa_arr,
        hankel_c_m2_abs=cm2_abs, hankel_c_m1_abs=cm1_abs, hankel_c_0_abs=c0_abs,
        hankel_ratio=ratio_arr, hankel_in_band=hk_inband, hankel_offpole_rel=offpole_rel,
        hankel_c_m2_re=cm2_re, hankel_c_m2_im=cm2_im,
        hankel_c_m1_re=cm1_re, hankel_c_m1_im=cm1_im,
        hankel_c_0_re=c0_re, hankel_c_0_im=c0_im,
        hankel_ratio_eps=np.array([HANKEL_RATIO_EPS]),
        max_hankel_ratio=np.array([res["max_hankel_ratio"]]),
        max_hankel_cell=np.array([res["max_hankel_cell"]]),
        hankel_pass=np.array([res["hankel_pass"]]),
        # pins / meta
        verdict=np.array([res["verdict"]], dtype=object),
        value=np.array([res["value"]], dtype=object),
        pins=np.array([json.dumps({
            "L_max": L_MAX, "shell_band": SHELL_BAND, "hankel_ratio_eps": HANKEL_RATIO_EPS,
            "s_numerals": S_NUMERALS, "families": FAMILIES, "hankel_sA": HANKEL_SA,
            "window_Lfit": [int(L) for L in WINDOW_LFIT], "mp_dps": MP_DPS,
            "contour_R": CONTOUR_R, "n_quad": N_QUAD,
            "scheme": SCHEME, "convention": CONVENTION, "tau_fold": float(tau_fold),
            "d_spec": int(d_spec),
        })], dtype=object),
    )


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
    print(f"  tau_fold={float(tau_fold)} d_spec={int(d_spec)} L_max={L_MAX} (window inherited; no new diagonalization)")
    print()

    res = compute()

    # --- report ---
    print(f"=== LEG 1: window-corrected shell exponents (band < {SHELL_BAND}) ===")
    print(f"  anchor cross-check: max|reproduced - stored tau_fold exp| = {res['anchor_meas_max']:.2e} "
          f"(bit-exact expected)")
    print(f"  anchor cross-check: max|reproduced - stored tau0 family-A window exp| = {res['anchor_t0A_max']:.2e} "
          f"(bit-exact expected)")
    for s in S_NUMERALS:
        for F in FAMILIES:
            c = res["delta_table"][(s, F)]  # (local)
            print(f"  s={int(s)} {F}: exp_meas(tau_fold)={c['exp_meas_tau_fold']:+.6f}  "
                  f"exp_exact(tau0,window)={c['exp_exact_tau0_window']:+.6f}  "
                  f"Delta={c['delta']:.6f}  [{'in' if c['in_band'] else 'OUT'}]")
    print(f"  max Delta = {res['max_delta']:.6f} @ s{int(res['max_delta_cell'][0])}{res['max_delta_cell'][1]}  "
          f"vs {SHELL_BAND}  -> shell {'PASS' if res['shell_pass'] else 'FAIL'}")
    print()
    print(f"=== LEG 2 (BUNDLED): off-pole Hankel double-pole re-check (ratio < {HANKEL_RATIO_EPS:.0e}) ===")
    for sa in HANKEL_SA:
        h = res["hankel_table"][sa]  # (local)
        on_pole = " [a2 pole]" if abs(sa - 3.0) < 1e-9 else ""  # (local)
        print(f"  s_A={sa}{on_pole}: |c_-2|={h['c_m2_abs']:.3e}  |c_-1|={h['c_m1_abs']:.3e}  "
              f"|c_0|={h['c_0_abs']:.3e}  ratio={h['ratio']:.3e}  [{'in' if h['in_band'] else 'OUT'}]  "
              f"(offpole_rel={h['offpole_rel_dev']:.1e})")
    print(f"  max Hankel ratio = {res['max_hankel_ratio']:.3e} @ s_A={res['max_hankel_cell']}  "
          f"vs {HANKEL_RATIO_EPS:.0e}  -> Hankel {'PASS' if res['hankel_pass'] else 'FAIL'}")
    print()

    # --- save artifacts ---
    save_npz(res)
    make_plot(res)
    print(f"  npz -> {OUT_NPZ.name}")
    print(f"  png -> {OUT_PNG.name}")
    print()

    # --- a19 emission-time extra-row ---
    a19_rows, w1_1_present = build_a19_extra_rows(res["lineage"])
    print(f"  a19 emission-time check: W1-1 L4 lift rows present = {w1_1_present} "
          f"-> {'FULL-CONFIDENCE' if w1_1_present else 'UNTRUSTED-UPSTREAM (annotation only)'}")

    verdict = res["verdict"]  # (local)

    # 3-tuple: the substitution chain pre-registers a DIRECTIONAL prediction
    # (Delta stays strictly below the band; window subtraction built in -> in-regime).
    # Map the directional content into the schema-v2 3-tuple (per gate-verdicts.md + orchestrator override).
    if verdict == "PASS":
        sign_v = "PASS"        # (local) direction matches: max Delta < band AND ratio < eps, as predicted
        mag_v = "PASS"         # (local) |max Delta| within band with margin
        regime_v = "VALID"     # (local) common window bias subtracted in-difference; comparison in-regime
    elif verdict == "FAIL":
        # which conjunct breached sets the sign reading
        sign_v = "FAIL"        # (local) a predicted-below quantity went above its threshold
        mag_v = "FAIL"         # (local)
        regime_v = "VALID"     # (local) regime still well-defined (window subtraction built in); FAIL is genuine anomaly
    else:  # INFO (split or rank-deficient)
        sign_v = "FAIL" if not (res["shell_pass"] and res["hankel_pass"]) else "PASS"  # (local)
        mag_v = "INFO"         # (local) one conjunct in band, the other out -> band-region split
        regime_v = "MARGINAL"  # (local) split outcome: regime informative but not clean PASS

    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    print_verdict_payload(verdict, res["value"], audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
                          extra_rows=a19_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # exit 0 regardless of scientific verdict (FAIL is a valid result; math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
