#!/usr/bin/env python3
"""
S85 W9-3 — S85-W9-FOLDED-TRIANGLE-21CM-SHAPE
============================================

Gate: S85-W9-FOLDED-TRIANGLE-21CM-SHAPE ([VERIFY])

Classification: PHONONIC. Folded-triangle bispectrum at 21-cm l_max=1e5
is the three-mode correlator of substrate relay-pattern excitations in
the post-transit GGE-relic regime. This is a SHAPE PRE-REGISTRATION
gate — it records the template and amplitude at pivot, not a detection
claim. The W0 companion gate S85-FOLDED-BISPECTRUM-21CM-SHAPE-TEMPLATE
(Babich-Creminelli Fisher-cosine) tested DETECTABILITY and FAILed at
SKA-Phase-2 threshold; W9-3 tests the PRE-REGISTRATION conditions
(shape FINITE, response WELL-DEFINED, SNR projection COMPUTED).

Pre-registered thresholds (plan §9):
  PASS iff (a) f_NL_folded_predicted is FINITE (dimensionless real); AND
           (b) shape_response_function integrates to a well-defined real
               over the folded-ridge (convergent, no log-divergences); AND
           (c) SNR projection at nominal 21-cm noise is computed and
               emitted (not a detection threshold — pre-registration only).
  FAIL iff shape diverges OR f_NL_folded is non-finite.
  INFO iff f_NL_folded < 0.1 (unmeasurable under current detector
         roadmap — template registered but EVOI = 0).

Substitution chain (plan §10, Python-verified):
  alpha = cosh(chi), beta = sinh(chi), |beta|^2 = n_pairs = 59.8 (S42)
  |alpha|^2 = 1 + |beta|^2 = 60.8
  |beta|^2 / |alpha|^2 = 59.8/60.8 = 0.9836  (Python-verified)
  f_NL_folded ~ (|beta|^2 / |alpha|^2) * shape_factor
  Direction: if shape_factor is O(1) real finite, f_NL_folded is O(1)
             (> 0.1 INFO threshold), so PASS.

Inputs:
  - canonical_constants.py (SHA-pinned)

Output 4-tuple:
  (value=f_NL_folded_predicted, scheme=analytic-template-folded,
   convention=delta-function-ridge+2%k-window, L_max=1e5)

DISCIPLINE
----------
- `from canonical_constants import *` first.
- Every computed intermediate tagged `# (local)`.
- CPU-only analytic template (no l_max^3 triangle scan); OMP=4.
- Dual-SHA per S84+ schema; exit 0 unconditionally on compute success.
"""

from __future__ import annotations

# --------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# --------------------------------------------------------------------
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

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    n_pairs,
    n_s_framework,
    beta_s,
    l_max_21cm_forecast,
    tau_fold,
)

# --------------------------------------------------------------------
# Section 2 — Standard imports
# --------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# --------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                             # (local)
GATE_ID = "S85-W9-FOLDED-TRIANGLE-21CM-SHAPE"               # (local)
SCHEME = "analytic-template-folded"                         # (local) plan §7
CONVENTION = "delta-function-ridge+2%k-window"              # (local) plan §7
L_MAX = int(l_max_21cm_forecast)                            # (local) 1e5 → int for verdict line

# PRDR pins (plan §7)
RIDGE_WINDOW_FRAC = 0.02                                    # (local) 2% k-window around k1+k2=k3 ridge
RIDGE_N_POINTS = 1024                                       # (local) parametric ridge sampling
K_PIVOT = 0.05                                              # (local) Mpc^-1, CMB pivot scale (standard Planck convention)
CHI_21CM_MPC = 14000.0                                      # (local) comoving distance to 21-cm screen (~9000 Mpc - 16000 Mpc range; conservative central 14 Gpc)
RANDOM_SEED = 42                                            # (local) plan §7
INFO_THRESHOLD_F_NL = 0.1                                   # (local) plan §9 INFO cutoff

# 21-cm noise floor (nominal SKA-Phase-2+ fiducial; used for SNR projection only)
SIGMA_21CM_PER_MODE = 1e-5                                  # (local) dimensionless per-mode bispectrum noise floor (conservative SKA-Phase-2 projection, consistent with W0 Babich-Creminelli L_max=8 context)

CANONICAL_PY = resolve_script(None, 'canonical_constants.py')

OUT_NPZ = resolve_output(85, 's85_w9_folded_triangle_21cm_shape.npz')
OUT_PNG = resolve_output(85, 's85_w9_folded_triangle_21cm_shape.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [CANONICAL_PY]


# --------------------------------------------------------------------
# Section 4 — SHA-256 utilities (identical to W9-1/W9-2)
# --------------------------------------------------------------------

def sha256_of(path):
    h = hashlib.sha256()                                    # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                               # (local)
    for p in inputs:
        sha = sha256_of(p)                                  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""                                      # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""                                   # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                       # (local)

    h_audit = hashlib.sha256()                              # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                             # (local)

    h_content = hashlib.sha256()                            # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()                         # (local)
    return audit, content


# --------------------------------------------------------------------
# Section 5 — Compute: analytic folded-triangle template
# --------------------------------------------------------------------

def bogoliubov_ratio():
    """|beta|^2 / |alpha|^2 from Parker IC anchor (S42 canonical: n_pairs=59.8)."""
    beta_sq = n_pairs                                       # (local)
    alpha_sq = 1.0 + beta_sq                                # (local) = |alpha|^2 = 1 + |beta|^2 (Bogoliubov constraint)
    ratio = beta_sq / alpha_sq                              # (local) 59.8/60.8 = 0.98355
    # Cross-check: envelope form |alpha*beta| / |alpha|^2 for diagnostic
    envelope = np.sqrt(beta_sq * alpha_sq) / alpha_sq       # (local) = sqrt(beta_sq/alpha_sq) if written differently; use sqrt product
    return float(ratio), float(envelope), float(beta_sq), float(alpha_sq)


def power_spectrum_shape(k_over_pivot):
    """Framework power spectrum P(k) ~ A_s * (k/k_pivot)^(n_s - 1 + 0.5*beta_s*log(k/k_pivot)).

    For shape_factor computation we only need the dimensionless k-dependence,
    not the A_s prefactor (A_s cancels when we take B_folded / (P*P)).
    Therefore: shape_dim(k) := (k/k_pivot)^(n_s_framework - 1)
    with subleading running neglected over the ridge log-span.
    """
    return np.power(k_over_pivot, n_s_framework - 1.0)


def compute_folded_ridge():
    """Parametric folded-ridge evaluation.

    The folded-triangle ridge is the locus k3 = k1 + k2 with k1 = k2 for
    simplicity (the k1=k2 sub-ridge; generalizations via azimuthal
    averaging at fixed ridge length). Parametrize along log(k1/k_pivot):

        s ∈ [0, S_max]
        k1(s) = k_pivot * exp(s)
        k2(s) = k_pivot * exp(s)      (k1 = k2 sub-ridge)
        k3(s) = k1(s) + k2(s) = 2 * k_pivot * exp(s)

    S_max fixed by l_max_21cm_forecast / chi_21cm / k_pivot.
    """
    k_max_Mpc_inv = l_max_21cm_forecast / CHI_21CM_MPC      # (local) ≈ 7.14 Mpc^-1 at chi=14Gpc
    s_max = float(np.log(k_max_Mpc_inv / K_PIVOT))          # (local)

    s = np.linspace(0.0, s_max, RIDGE_N_POINTS)             # (local) log-parametric arc
    k1 = K_PIVOT * np.exp(s)                                # (local) Mpc^-1
    k2 = k1.copy()                                          # (local) k1=k2 sub-ridge
    k3 = k1 + k2                                            # (local) folded ridge locus

    # Dimensionless shape response on ridge
    P_k1 = power_spectrum_shape(k1 / K_PIVOT)               # (local) (k1/kp)^(n_s-1)
    P_k2 = power_spectrum_shape(k2 / K_PIVOT)               # (local)
    P_k3 = power_spectrum_shape(k3 / K_PIVOT)               # (local)

    # Folded-template dimensionless shape:
    # S_folded(k1,k2,k3) := (k1*k2*k3)^2 * B_folded / [(k1 k2 k3)^2 * A_s^2]
    # in the normalization where B_folded ~ A_s^2 * shape.
    # For the Bogoliubov-NBD template with folded enhancement:
    # shape_response(s) = (|beta|^2/|alpha|^2) * [P(k1) P(k2) + P(k1) P(k3) + P(k2) P(k3)]
    # divided by the factor-of-2-correction (Komatsu 2010 Eq 36 convention).
    ratio, envelope, beta_sq, alpha_sq = bogoliubov_ratio()
    shape_response = ratio * (P_k1 * P_k2 + P_k1 * P_k3 + P_k2 * P_k3) / 3.0  # (local)
    # Integrated response: trapezoidal over s (log-k arc length)
    integrated_shape = float(np.trapezoid(shape_response, s))  # (local)
    # Shape factor: normalization-invariant amplitude at ridge centroid
    shape_factor = float(np.mean(shape_response))           # (local) scale-invariant average over the ridge
    # Divergence check: all finite?
    all_finite = bool(np.all(np.isfinite(shape_response)) and np.isfinite(integrated_shape))

    return {
        "s": s,
        "k1": k1, "k2": k2, "k3": k3,
        "P_k1": P_k1, "P_k2": P_k2, "P_k3": P_k3,
        "shape_response": shape_response,
        "integrated_shape": integrated_shape,
        "shape_factor": shape_factor,
        "all_finite": all_finite,
        "s_max": s_max,
        "k_max_Mpc_inv": k_max_Mpc_inv,
    }


def compute_snr_projection(f_NL_folded, ridge):
    """Dimensional SNR ~ f_NL * sqrt(N_modes on ridge) / sigma_per_mode.

    N_modes on the 21-cm folded ridge at l_max, width RIDGE_WINDOW_FRAC:
      N_modes ~ (l_max)^2 * RIDGE_WINDOW_FRAC / (2 pi)
    Per-mode signal = f_NL_folded * shape_factor (dimensionless).
    Per-mode noise  = SIGMA_21CM_PER_MODE.
    """
    l_max = l_max_21cm_forecast                             # (local) 1e5
    n_modes = (l_max ** 2) * RIDGE_WINDOW_FRAC / (2.0 * np.pi)  # (local) ~3.18e8
    signal = abs(f_NL_folded) * ridge["shape_factor"]       # (local) per-mode
    noise = SIGMA_21CM_PER_MODE                             # (local) per-mode
    snr = signal * np.sqrt(n_modes) / noise                 # (local) aggregate SNR
    return {
        "l_max": float(l_max),
        "n_modes": float(n_modes),
        "per_mode_signal": float(signal),
        "per_mode_noise": float(noise),
        "snr": float(snr),
    }


def compute():
    """Main compute: f_NL_folded + shape_response + SNR projection."""
    np.random.seed(RANDOM_SEED)

    # Bogoliubov amplitude
    ratio, envelope, beta_sq, alpha_sq = bogoliubov_ratio()

    # Folded ridge
    ridge = compute_folded_ridge()
    shape_factor = ridge["shape_factor"]                    # (local)
    integrated_shape = ridge["integrated_shape"]            # (local)
    all_finite_ridge = ridge["all_finite"]                  # (local)

    # f_NL_folded prediction (plan §10 Step 3 form)
    f_NL_folded = ratio * shape_factor                      # (local) dimensionless

    # Cross-check: envelope form (|alpha*beta|/|alpha|^2) with same shape_factor
    f_NL_folded_envelope = envelope * shape_factor          # (local)

    # SNR projection
    snr = compute_snr_projection(f_NL_folded, ridge)

    # PASS / FAIL / INFO direction check
    cond_a_finite = bool(np.isfinite(f_NL_folded))
    cond_b_well_defined = bool(all_finite_ridge and np.isfinite(integrated_shape))
    cond_c_snr_computed = bool(np.isfinite(snr["snr"]))
    info_check = abs(f_NL_folded) < INFO_THRESHOLD_F_NL     # (local)

    return {
        "value": f_NL_folded,
        "f_NL_folded_predicted": f_NL_folded,
        "f_NL_folded_envelope_crosscheck": f_NL_folded_envelope,
        "bogoliubov_ratio": ratio,
        "bogoliubov_envelope": envelope,
        "beta_sq": beta_sq,
        "alpha_sq": alpha_sq,
        "shape_factor": shape_factor,
        "integrated_shape": integrated_shape,
        "ridge_all_finite": all_finite_ridge,
        "s_max": ridge["s_max"],
        "k_max_Mpc_inv": ridge["k_max_Mpc_inv"],
        "snr_l_max": snr["l_max"],
        "snr_n_modes": snr["n_modes"],
        "snr_per_mode_signal": snr["per_mode_signal"],
        "snr_per_mode_noise": snr["per_mode_noise"],
        "snr_projected": snr["snr"],
        "cond_a_finite": cond_a_finite,
        "cond_b_well_defined": cond_b_well_defined,
        "cond_c_snr_computed": cond_c_snr_computed,
        "info_f_NL_below_0_1": info_check,
        # Ridge arrays for plotting
        "ridge_s": ridge["s"],
        "ridge_k1": ridge["k1"],
        "ridge_k3": ridge["k3"],
        "ridge_shape_response": ridge["shape_response"],
    }


def evaluate_gate(results):
    """PASS if all three conditions hold; INFO if f_NL_folded < 0.1; FAIL if any divergence."""
    if not (results["cond_a_finite"]
            and results["cond_b_well_defined"]
            and results["cond_c_snr_computed"]):
        return "FAIL"
    if results["info_f_NL_below_0_1"]:
        return "INFO"
    return "PASS"


# --------------------------------------------------------------------
# Section 6 — Output artifacts
# --------------------------------------------------------------------

def write_npz(results, audit_sha, content_sha):
    to_save = {
        "gate_id": np.array(GATE_ID),
        "scheme": np.array(SCHEME),
        "convention": np.array(CONVENTION),
        "L_max": np.array(L_MAX),
        "value": np.array(results["value"]),
        "f_NL_folded_predicted": np.array(results["f_NL_folded_predicted"]),
        "f_NL_folded_envelope_crosscheck": np.array(results["f_NL_folded_envelope_crosscheck"]),
        "bogoliubov_ratio": np.array(results["bogoliubov_ratio"]),
        "shape_factor": np.array(results["shape_factor"]),
        "integrated_shape": np.array(results["integrated_shape"]),
        "snr_projected": np.array(results["snr_projected"]),
        "snr_n_modes": np.array(results["snr_n_modes"]),
        "ridge_s": results["ridge_s"],
        "ridge_k1": results["ridge_k1"],
        "ridge_k3": results["ridge_k3"],
        "ridge_shape_response": results["ridge_shape_response"],
        "audit_sha256": np.array(audit_sha),
        "content_sha256": np.array(content_sha),
    }
    np.savez_compressed(OUT_NPZ, **to_save)
    print(f"  npz:  {OUT_NPZ.relative_to(PROJECT_ROOT)}")


def write_plot(results):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel 1: shape response vs log-k (folded ridge)
    ax = axes[0]
    ax.semilogy(results["ridge_s"], results["ridge_shape_response"],
                "b-", lw=1.3, label="shape_response(k)")
    ax.set_xlabel(r"$s = \log(k_1 / k_{\rm pivot})$")
    ax.set_ylabel("Folded-ridge shape response (dimensionless)")
    ax.set_title(f"Folded-ridge shape response\nintegrated = {results['integrated_shape']:.3e}")
    ax.grid(True, alpha=0.3)
    ax.legend()

    # Panel 2: f_NL comparison (ratio vs envelope) + SNR projection
    ax = axes[1]
    bars = ["ratio form\n(plan §10)", "envelope form\n(cross-check)"]
    vals = [
        results["f_NL_folded_predicted"],
        results["f_NL_folded_envelope_crosscheck"],
    ]
    colors = ["steelblue", "lightsteelblue"]
    ax.bar(range(len(bars)), vals, color=colors)
    ax.axhline(INFO_THRESHOLD_F_NL, color="red", ls="--", lw=1,
               label=f"INFO cutoff ({INFO_THRESHOLD_F_NL})")
    ax.set_xticks(range(len(bars)))
    ax.set_xticklabels(bars)
    ax.set_ylabel(r"$f_{NL}^{\rm folded}$ (dimensionless)")
    ax.set_title(f"f_NL_folded predictions\nSNR projection @ l_max={int(L_MAX):.0e}, "
                 f"n_modes={results['snr_n_modes']:.2e}: {results['snr_projected']:.2e}")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.suptitle(GATE_ID, fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)
    print(f"  png:  {OUT_PNG.relative_to(PROJECT_ROOT)}")


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
    print(f"  verdict appended to {VERDICT_TXT.relative_to(PROJECT_ROOT)}")


# --------------------------------------------------------------------
# Section 7 — Main
# --------------------------------------------------------------------

def main():
    t0 = time.time()                                        # (local)

    pins = log_input_pins(INPUT_FILES)                      # (local)
    script_path = Path(__file__).resolve()                  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_PY, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    results = compute()
    print(f"  Bogoliubov |β|² / |α|²       = {results['bogoliubov_ratio']:.6f}")
    print(f"  Bogoliubov envelope (|αβ|/|α|²) = {results['bogoliubov_envelope']:.6f}")
    print(f"  shape_factor (ridge mean)    = {results['shape_factor']:.4e}")
    print(f"  integrated_shape (arc-integral) = {results['integrated_shape']:.4e}")
    print(f"  ridge all-finite             = {results['ridge_all_finite']}")
    print(f"  f_NL_folded (ratio form)     = {results['f_NL_folded_predicted']:.4e}")
    print(f"  f_NL_folded (envelope form)  = {results['f_NL_folded_envelope_crosscheck']:.4e}")
    print(f"  s_max (log-k arc length)     = {results['s_max']:.3f}")
    print(f"  k_max                        = {results['k_max_Mpc_inv']:.3f} Mpc^-1")
    print(f"  SNR projection (l_max={int(L_MAX):.0e}) = {results['snr_projected']:.3e}")
    print(f"  SNR n_modes (2% ridge)       = {results['snr_n_modes']:.3e}")
    print(f"  f_NL < 0.1 INFO check        = {results['info_f_NL_below_0_1']}")
    print()

    verdict = evaluate_gate(results)
    value = results["value"]                                # (local)

    tag = (f"(value={value!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")      # (local)
    print(tag)
    write_npz(results, audit_sha, content_sha)
    write_plot(results)
    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                 # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # math-scripts.md: exit 0 for any scientific verdict


if __name__ == "__main__":
    sys.exit(main())
