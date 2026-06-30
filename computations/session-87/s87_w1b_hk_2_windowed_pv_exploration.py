#!/usr/bin/env python3
"""
S87 W1b-HK-2 — Windowed Pauli-Villars Exploration
=================================================

Gate: S87-W1B-HK-2-WINDOWED-PV-EXPLORATION  (trigger: [VERIFY] [SIGN])

Pre-registered threshold (3 schemes; per spawn-prompt and plan §W1b-HK-2):
  PASS for any scheme: (R_PV − R_SD > 0) AND (|R_PV − R_SD| ∈ [1e-6, 1e+6])
  FAIL for all schemes: every alternative produces sign < 0 OR magnitude >> 1e+6
  INFO: at least 1 scheme recovers sign but magnitude in [1e+6, 1e+9]

Hypothesis tested
-----------------
W1b-1 closed FAIL: canonical Pauli-Villars at M_KK gave R_PV = 6.996e+04 vs
R_SD = 1.767e+06; sign INVERTED from plan-predicted +1 (R_PV − R_SD =
−1.697e+06). The corridor "PV at canonical M_KK is small-positive
refinement of SD" closed.

THIS gate tests three structurally distinct PV schemes (pre-registered;
NO post-hoc additions allowed) at L=12, M=M_KK_dimless=1:

  Scheme A — Smooth-window:    R_PV^A = sum_k m_k * lambda_k^{-3} * [1 - w(lambda_k/M)]
                               with w(x) = (1 + erf(x))/2 — soft erf-window UV taper
  Scheme B — Exponential cutoff: R_PV^B = sum_k m_k * lambda_k^{-3} * exp(-lambda_k^2 / M^2)
                                 Gaussian UV suppression at scale M
  Scheme C — Higher-order PV:  R_PV^C = sum_k m_k * [lambda_k^{-3}
                                                       - 2 (lambda_k^2 + M^2)^{-3/2}
                                                       + (lambda_k^2 + 4 M^2)^{-3/2}]
                               second-order PV difference (cancels UV divergence
                               to higher order than the bare PV of W1b-1)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (eigenvalue cache)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<dict_of_per_scheme_R_PV_minus_R_SD>, scheme=<scheme_name>,
   convention=substrate-mass-scale-M_KK, L_max=12)

Classification: GEOMETRIC (substrate spectral-mode regulator-class exploration;
post-execution windowed PV recovery test for the §VII.U Mellin-Dirichlet pole.)

METHODOLOGY
-----------
Loads the L_max=12 master spectrum cache (`s84_spectrum_cache_L12_tau019.npz`),
extracts 166,896 distinct |lambda_k| with irrep multiplicities m_k, computes
the three pre-registered alternative PV-scheme moments at M = M_KK_dimless = 1,
and compares each against R_SD = 1.767131e+06 (W1b-1 continuum-SD anchor at
the s=3 Mellin-Dirichlet pole).

DISCIPLINE
----------
- `from canonical_constants import *` (M_KK, tau_fold imported)
- Every local/intermediate tagged `# (local)`
- CPU path: OMP_NUM_THREADS=8 set BEFORE numpy import (per
  `computation-environment.md` CPU-fallback discipline)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 3-tuple Schema-v2 annotation emitted (S87+ schema-v2 second companion row)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to `s87_gate_verdicts.txt` ATOMICALLY (single
  open("a") write — no read-modify-write, no truncate-and-rewrite)

Substrate framing
-----------------
The PV scheme set tested here is a substrate operation on the finite-L
eigenvalue projection of D_K at tau=tau_fold — NOT a continuum-QFT
regulator imported from a curved-spacetime container. The fabric IS its
finite-L spectrum {lambda_k, m_k}_{level<=L=12}; the windowed-PV
operations re-weight the truncated mode catalog by an admissible
suppression kernel at the substrate scale M_KK = 1 (in dimensionless
eigenvalue units). Direction of explanation: D_K -> eigenvalues
{lambda_k} -> windowed PV weight w_k(lambda_k/M) -> spectral moment R_PV
-> emergent §VII.U residue at substrate-distance-1 pole. R_SD is the
L -> infinity asymptotic of the bare moment, not an externally imported
continuum value.
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 0 — CPU thread cap (MUST precede numpy import)
# -----------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# -----------------------------------------------------------------------------
# Section 2 — Standard imports
# -----------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.special import erf as scipy_erf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S87"                                                       # (local)
GATE_ID = "S87-W1B-HK-2-WINDOWED-PV-EXPLORATION"                      # (local)
SCHEME = "windowed-PV-3-scheme-comparison"                            # (local)
CONVENTION = "substrate-mass-scale-M_KK"                              # (local)
L_MAX = 12                                                            # (local)

# Pre-registered band thresholds (per spawn-prompt; NO post-hoc edits)
PASS_LO = 1.0e-6                                                      # (local) lower edge of PASS magnitude band
PASS_HI = 1.0e+6                                                      # (local) upper edge of PASS magnitude band
INFO_HI = 1.0e+9                                                      # (local) upper edge of INFO magnitude band

# PV mass scale: substrate dimensionless M_KK = 1 (eigenvalues are in
# dimensionless M_KK units throughout the framework's spectral cache).
M_KK_DIMLESS = 1.0                                                    # (local)

# R_SD anchor from W1b-1 (continuum SD residue; pinned upstream).
R_SD_ANCHOR = 1.767131e+06                                            # (local) W1b-1 anchor

# Output destinations
OUT_NPZ = resolve_output(87, 's87_w1b_hk_2_windowed_pv_exploration.npz')
OUT_PNG = resolve_output(87, 's87_w1b_hk_2_windowed_pv_exploration.png')
VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')

CACHE_L12 = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = [CANONICAL_PY, CACHE_L12]

# -----------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema; W9a-99 split)
# -----------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    """audit_sha256 = SHA( script || canonical || pinmap_json );
       content_sha256 = SHA( script ).
    """
    script_bytes = b""           # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""        # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")              # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()    # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Section 5 — Spectrum loading (sectors -> flat (lambda, m_k) arrays)
# -----------------------------------------------------------------------------

def load_spectrum(L_max_target: int):
    """Load |lambda_k| with irrep multiplicity m_k from the L=12 master cache,
    truncated to sectors with level <= L_max_target.

    Returns (lambdas, mults) as 1D float64 arrays.
    """
    data = np.load(CACHE_L12, allow_pickle=True)
    sec = data["sector_evals"].item()  # (local)
    lams = []                          # (local)
    mults = []                         # (local)
    for (p, q), v in sec.items():
        if v["level"] > L_max_target:
            continue
        ev = np.asarray(v["abs_evals"], dtype=np.float64)  # (local)
        m = int(v["dim"])                                   # (local)
        lams.append(ev)
        mults.append(np.full_like(ev, m, dtype=np.float64))
    lambdas = np.concatenate(lams)  # (local)
    mks = np.concatenate(mults)     # (local)
    # Drop zero / near-zero eigenvalues (substrate kernel modes that would
    # diverge under lambda^{-3}); pre-existing W1b-1 cache has min ~ 0.82.
    nonzero_mask = lambdas > 1e-12   # (local)
    lambdas = lambdas[nonzero_mask]
    mks = mks[nonzero_mask]
    return lambdas, mks


# -----------------------------------------------------------------------------
# Section 6 — Three pre-registered windowed-PV schemes
# -----------------------------------------------------------------------------

def scheme_A_smooth_window(lambdas, mks, M):
    """R_PV^A = sum_k m_k * lambda_k^{-3} * [1 - w(lambda_k / M)]
       with w(x) = (1 + erf(x)) / 2.

    Substrate framing: erf-based smooth window — every term is non-negative;
    UV modes (lambda_k >> M) are suppressed exponentially via 1 - erf =
    erfc; IR modes (lambda_k ~ M) carry weight ~ 0.12; lowest-lambda modes
    dominate.
    """
    x = lambdas / M                                              # (local)
    w = 0.5 * (1.0 + scipy_erf(x))                               # (local)
    weights = 1.0 - w                                            # (local)
    R = float(np.sum(mks * np.power(lambdas, -3.0) * weights))   # (local)
    return R


def scheme_B_exp_cutoff(lambdas, mks, M):
    """R_PV^B = sum_k m_k * lambda_k^{-3} * exp(-lambda_k^2 / M^2).

    Substrate framing: Gaussian UV suppression on D_K^2 spectrum.
    Mathematically equivalent (up to normalization) to a heat-kernel
    truncation at t = 1/M^2, restricted to s = 3 weight.
    """
    suppression = np.exp(-(lambdas * lambdas) / (M * M))         # (local)
    R = float(np.sum(mks * np.power(lambdas, -3.0) * suppression))  # (local)
    return R


def scheme_C_higher_order_pv(lambdas, mks, M):
    """R_PV^C = sum_k m_k * [ lambda_k^{-3}
                              - 2 (lambda_k^2 +    M^2)^{-3/2}
                              +   (lambda_k^2 + 4 M^2)^{-3/2} ].

    Substrate framing: second-order PV — cancels two leading UV divergences
    (single subtraction at M, plus second mass-shifted subtraction at 2M)
    instead of one (W1b-1's bare PV cancels only the leading UV term).
    """
    bare = np.power(lambdas, -3.0)                                       # (local)
    pv1 = np.power(lambdas * lambdas + M * M, -1.5)                      # (local)
    pv2 = np.power(lambdas * lambdas + 4.0 * M * M, -1.5)                # (local)
    bracket = bare - 2.0 * pv1 + pv2                                     # (local)
    R = float(np.sum(mks * bracket))                                     # (local)
    return R


# -----------------------------------------------------------------------------
# Section 7 — Compute (orchestrate per-scheme evaluation + verdict mapping)
# -----------------------------------------------------------------------------

def compute_per_scheme(lambdas, mks, M, R_SD):
    """Evaluate each pre-registered scheme; return per-scheme dict."""
    results = {}  # (local)

    R_A = scheme_A_smooth_window(lambdas, mks, M)
    R_B = scheme_B_exp_cutoff(lambdas, mks, M)
    R_C = scheme_C_higher_order_pv(lambdas, mks, M)

    for name, R in [("A_smooth_window", R_A),
                    ("B_exp_cutoff", R_B),
                    ("C_higher_order_pv", R_C)]:
        residual = R - R_SD                                       # (local)
        sign = 1 if residual > 0 else (-1 if residual < 0 else 0)  # (local)
        magnitude = abs(residual)                                  # (local)

        # Per-scheme PASS / INFO / FAIL classification
        # PASS: sign>0 AND magnitude in [PASS_LO, PASS_HI]
        # INFO: sign>0 AND magnitude in [PASS_HI, INFO_HI] (sign recovered, magnitude loose)
        # FAIL: sign<=0 OR magnitude > INFO_HI
        if sign > 0 and PASS_LO <= magnitude <= PASS_HI:
            scheme_verdict = "PASS"
        elif sign > 0 and PASS_HI < magnitude <= INFO_HI:
            scheme_verdict = "INFO"
        else:
            scheme_verdict = "FAIL"

        results[name] = {
            "R_PV": R,
            "residual": residual,
            "sign": sign,
            "magnitude": magnitude,
            "scheme_verdict": scheme_verdict,
        }
    return results


def collapse_composite(per_scheme):
    """Composite gate verdict over the 3 pre-registered schemes.

    Per spawn-prompt:
      - PASS: any scheme PASSes
      - INFO: at least 1 scheme INFO and none PASS
      - FAIL: every scheme FAILS
    """
    scheme_verdicts = [v["scheme_verdict"] for v in per_scheme.values()]  # (local)
    if "PASS" in scheme_verdicts:
        return "PASS"
    if "INFO" in scheme_verdicts:
        return "INFO"
    return "FAIL"


def per_scheme_3tuple(per_scheme, composite):
    """Map per-scheme results to (sign, magnitude, regime) Schema-v2 verdicts.

    sign_verdict     = PASS iff at least one scheme has sign > 0; else FAIL.
    magnitude_verdict = PASS iff at least one scheme is in [PASS_LO, PASS_HI];
                        INFO iff at least one scheme is in [PASS_HI, INFO_HI]
                        and none in PASS band; FAIL otherwise.
    regime_verdict   = VALID always (M_KK_dimless = 1 lies inside [0.82, 5.42]
                        eigenvalue range for L=12; same regime check as W1b-1).
    """
    any_sign_pos = any(v["sign"] > 0 for v in per_scheme.values())  # (local)
    sign_verdict = "PASS" if any_sign_pos else "FAIL"

    if any(v["scheme_verdict"] == "PASS" for v in per_scheme.values()):
        magnitude_verdict = "PASS"
    elif any(v["scheme_verdict"] == "INFO" for v in per_scheme.values()):
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    regime_verdict = "VALID"

    return sign_verdict, magnitude_verdict, regime_verdict


# -----------------------------------------------------------------------------
# Section 8 — Append verdict (atomic, S84+ dual-SHA + S87+ Schema-v2 3-tuple)
# -----------------------------------------------------------------------------

def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v):
    """Append the canonical line + dual-SHA companion + Schema-v2 3-tuple
    annotation.  Each row is its own atomic single-line append.
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_dualsha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    companion_3tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion_dualsha)
        fp.write(companion_3tuple)


# -----------------------------------------------------------------------------
# Section 9 — Plot (3-panel: R_PV bars + residual bars + sign/PASS-band map)
# -----------------------------------------------------------------------------

def make_plot(per_scheme, composite_verdict, R_SD, out_path):
    """3-panel: A = R_PV per scheme (log-y); B = residual (R_PV - R_SD)
    per scheme with PASS band overlay; C = magnitude vs threshold lines.
    """
    names = list(per_scheme.keys())  # (local)
    labels = ["A: smooth-window", "B: exp-cutoff", "C: higher-order PV"]  # (local)
    R_vals = [per_scheme[n]["R_PV"] for n in names]                       # (local)
    residuals = [per_scheme[n]["residual"] for n in names]                # (local)
    magnitudes = [per_scheme[n]["magnitude"] for n in names]              # (local)
    schemes_v = [per_scheme[n]["scheme_verdict"] for n in names]          # (local)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Panel A — R_PV (log scale)
    ax = axes[0]
    colors_A = ["tab:blue", "tab:orange", "tab:green"]                  # (local)
    ax.bar(labels, [abs(r) for r in R_vals], color=colors_A)
    ax.axhline(R_SD, color="red", linestyle="--", label=f"R_SD = {R_SD:.3e}")
    ax.set_yscale("log")
    ax.set_ylabel("|R_PV| (log scale)")
    ax.set_title("Panel A — Per-scheme R_PV vs R_SD anchor")
    ax.legend(fontsize=8)
    ax.tick_params(axis="x", rotation=15)

    # Panel B — Residual R_PV - R_SD (signed; shaded PASS band)
    ax = axes[1]
    colors_B = ["tab:green" if v == "PASS"
                else ("tab:orange" if v == "INFO" else "tab:red")
                for v in schemes_v]                                      # (local)
    ax.bar(labels, residuals, color=colors_B)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axhspan(PASS_LO, PASS_HI, alpha=0.15, color="green",
               label=f"PASS band [{PASS_LO:.0e}, {PASS_HI:.0e}]")
    ax.set_ylabel("R_PV − R_SD (signed)")
    ax.set_title(f"Panel B — Residual; composite = {composite_verdict}")
    ax.legend(fontsize=8)
    ax.tick_params(axis="x", rotation=15)
    ax.set_yscale("symlog", linthresh=1e+3)

    # Panel C — Magnitude with PASS / INFO ceiling lines
    ax = axes[2]
    ax.bar(labels, magnitudes, color=colors_A)
    ax.axhline(PASS_LO, color="green", linestyle=":", label=f"PASS_LO={PASS_LO:.0e}")
    ax.axhline(PASS_HI, color="green", linestyle="--", label=f"PASS_HI={PASS_HI:.0e}")
    ax.axhline(INFO_HI, color="orange", linestyle="--", label=f"INFO_HI={INFO_HI:.0e}")
    ax.set_yscale("log")
    ax.set_ylabel("|R_PV − R_SD| (log scale)")
    ax.set_title("Panel C — Magnitude vs PASS / INFO ceilings")
    ax.legend(fontsize=8)
    ax.tick_params(axis="x", rotation=15)

    fig.suptitle(
        f"{GATE_ID} — windowed PV exploration "
        f"(L_max={L_MAX}, M=M_KK_dimless=1, R_SD={R_SD:.3e})",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(out_path, dpi=120)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Section 10 — Main
# -----------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins (first 20 lines of stdout)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Compute S84+ dual SHAs
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Load spectrum at L=12
    print(f"=== loading spectrum cache (L_max_target={L_MAX}) ===")
    lambdas, mks = load_spectrum(L_max_target=L_MAX)
    n_distinct = int(lambdas.shape[0])                                  # (local)
    sum_m = float(np.sum(mks))                                          # (local)
    lam_min = float(lambdas.min())                                      # (local)
    lam_max = float(lambdas.max())                                      # (local)
    print(f"  n_distinct |lambda|: {n_distinct}")
    print(f"  sum m_k (irrep mult): {sum_m:.6e}")
    print(f"  |lambda| range: [{lam_min:.4f}, {lam_max:.4f}]")
    print()

    # 3. Compute per-scheme R_PV at M_KK_dimless = 1
    print(f"=== evaluating 3 pre-registered schemes at M={M_KK_DIMLESS} ===")
    per_scheme = compute_per_scheme(lambdas, mks, M_KK_DIMLESS, R_SD_ANCHOR)
    for name, r in per_scheme.items():
        print(f"  scheme {name}:")
        print(f"    R_PV     = {r['R_PV']:.6e}")
        print(f"    residual = {r['residual']:.6e}  (sign = {r['sign']:+d})")
        print(f"    |residual| = {r['magnitude']:.6e}")
        print(f"    scheme_verdict = {r['scheme_verdict']}")
    print()

    # 4. Composite + Schema-v2 3-tuple
    composite = collapse_composite(per_scheme)
    sign_v, mag_v, reg_v = per_scheme_3tuple(per_scheme, composite)
    print(f"=== composite verdict: {composite} ===")
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {reg_v}")
    print()

    # 5. Save data (keep arrays + per-scheme summary)
    save_dict = {
        "L_max": L_MAX,
        "M_KK_dimless": M_KK_DIMLESS,
        "R_SD_anchor": R_SD_ANCHOR,
        "PASS_LO": PASS_LO,
        "PASS_HI": PASS_HI,
        "INFO_HI": INFO_HI,
        "n_distinct_lambda": n_distinct,
        "sum_m": sum_m,
        "lambda_min": lam_min,
        "lambda_max": lam_max,
        "scheme_A_R_PV": per_scheme["A_smooth_window"]["R_PV"],
        "scheme_A_residual": per_scheme["A_smooth_window"]["residual"],
        "scheme_A_sign": per_scheme["A_smooth_window"]["sign"],
        "scheme_A_magnitude": per_scheme["A_smooth_window"]["magnitude"],
        "scheme_A_verdict": per_scheme["A_smooth_window"]["scheme_verdict"],
        "scheme_B_R_PV": per_scheme["B_exp_cutoff"]["R_PV"],
        "scheme_B_residual": per_scheme["B_exp_cutoff"]["residual"],
        "scheme_B_sign": per_scheme["B_exp_cutoff"]["sign"],
        "scheme_B_magnitude": per_scheme["B_exp_cutoff"]["magnitude"],
        "scheme_B_verdict": per_scheme["B_exp_cutoff"]["scheme_verdict"],
        "scheme_C_R_PV": per_scheme["C_higher_order_pv"]["R_PV"],
        "scheme_C_residual": per_scheme["C_higher_order_pv"]["residual"],
        "scheme_C_sign": per_scheme["C_higher_order_pv"]["sign"],
        "scheme_C_magnitude": per_scheme["C_higher_order_pv"]["magnitude"],
        "scheme_C_verdict": per_scheme["C_higher_order_pv"]["scheme_verdict"],
        "composite_verdict": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    np.savez(OUT_NPZ, **save_dict)
    print(f"data saved: {OUT_NPZ.name} ({OUT_NPZ.stat().st_size} bytes)")

    # 6. Plot
    make_plot(per_scheme, composite, R_SD_ANCHOR, OUT_PNG)
    print(f"plot saved: {OUT_PNG.name} ({OUT_PNG.stat().st_size} bytes)")

    # 7. Build value string for verdict line
    value_str = (
        f"A_resid={per_scheme['A_smooth_window']['residual']:.4e};"
        f"B_resid={per_scheme['B_exp_cutoff']['residual']:.4e};"
        f"C_resid={per_scheme['C_higher_order_pv']['residual']:.4e};"
        f"composite={composite};A={per_scheme['A_smooth_window']['scheme_verdict']};"
        f"B={per_scheme['B_exp_cutoff']['scheme_verdict']};"
        f"C={per_scheme['C_higher_order_pv']['scheme_verdict']}"
    )

    # 8. Emit 4-tuple + atomic-append verdict
    tag = (f"(value={value_str!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
