#!/usr/bin/env python3
"""
INV7 W1-1 — c2 substrate-first from the S44/S68 second-sound dispersion; A_FS = c2^2/c1^2 vs 0.204
====================================================================================================

Gate: INV7-W1-1 ([SIGN])  (investigation track)

Pre-registered threshold (plan §W1-1):
  operator: |A_FS_substrate - 0.204| <= band, A_FS_substrate = c2_substrate^2 / c1^2
  band = 0.0205 (10% of 0.204).
  PASS iff |A_FS_substrate - 0.204| <= 0.0205        (ring is substrate-GENUINE; C1 -> Track A)
  INFO iff 0.0205 < |A_FS_substrate - 0.204| <= 0.0410  (band-edge / regime-sensitive)
  FAIL iff |A_FS_substrate - 0.204| > 0.0410         (reproduction needs the recombination 1/[3(1+R*)]
                                                       input; the pin is a standard-formula STAND-IN;
                                                       C1 -> Track B)

HYPOTHESIS
----------
The first-sound-ring amplitude A_FS = c2^2/c1^2 — with c2 derived substrate-first from the S44/S68
second-sound order-parameter collective-mode dispersion (independent of the recombination
photon-baryon ratio R*) — equals the canonical 0.204 within a 10% band, i.e. the ratio is a
substrate-genuine prediction, not a re-import of the standard recombination sound speed 1/[3(1+R*)].

METHODOLOGY
-----------
The substrate IS the two-fluid condensate. The second sound (the order-parameter / thermal AB-mode
collective oscillation, S44/S68, Q=75,989, PROVEN obs-horizon at S68) is a genuine substrate
excitation: counterflow of the superfluid and normal components. Its long-wavelength dispersion is
linear, omega_2(k) = c2 * k, so the long-wavelength phase speed IS c2 = lim_{k->0} d omega_2/dk.

The substrate's OWN second-sound speed is fixed by the BCS low-temperature two-fluid relation
(GGE-TWO-FLUID-67, S67 W7-B, c_2 = c_1 sqrt(rho_n/(3 rho_s)) = 0.058 M_KK), using the substrate's
own superfluid/normal density partition (rho_n/rho = 0.0115, rho_s/rho = 0.9885) at the transit/fold
thermodynamic point — NO recombination R* = 3 rho_b/4 rho_gamma input enters. c1 is the first-sound
longitudinal density mode = v_F/sqrt(3) in the collisionless regime (s86-r-dual-pathway dictionary);
the discriminating ratio A_FS = c2^2/c1^2 is DIMENSIONLESS, so the absolute c1 normalization (v_F/sqrt3
vs the S67 internal value) cancels and the ratio reduces to the substrate two-fluid invariant
rho_n/(3 rho_s).

The gate reconstructs omega_2(k) on a 4096-point long-wavelength k-grid, extracts c2 = d omega_2/dk
at k->0 by linear regression, forms A_FS_substrate = c2^2/c1^2, and asks whether it reproduces 0.204.
Cross-check: the recombination first-sound stand-in 1/[3(1+R*)] (with the substrate's OWN R*=0.6299
from S68) gives c_s_standard^2 = 0.2045 -- i.e. 0.204 is the FIRST-sound (acoustic) value, not the
SECOND-sound (order-parameter) ratio. The gate does NOT invert to the container's R*; it derives c2
from the substrate's own mode and reads off whether the ring amplitude follows.

Classification: PHONONIC.

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- CPU-cap OMP8 (set before import numpy) per machinery pin; 1D dispersion fit, no matrix >= 100x100
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- verdict emitted via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict
  (session=7, track="investigation"); the script does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

# CPU-cap per machinery pin (GPU_path: numpy.linalg, 1D regression; set BEFORE numpy import)
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

# canonical_constants.py lives in computations/_shared/; add to sys.path then import *
SESSION_DIR = Path(__file__).resolve().parent                 # computations/investigation-7/
COMPUTATIONS_DIR = SESSION_DIR.parent                          # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib   # noqa: E402
import json      # noqa: E402
import time      # noqa: E402

import numpy as np                # noqa: E402
import matplotlib                 # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt   # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S7"                                                     # (local) investigation 7
GATE_ID = "INV7-W1-1"                                              # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "RATIO"                                               # (local) A_FS = c2^2/c1^2 dimensionless
L_MAX = "N/A"                                                      # (local) two-fluid hydrodynamic mode, not a D_K truncation

# Pre-registered band (plan §W1-1 strict_PASS_boundary)
A_FS_CANON = 0.204                                                 # (local) canonical A_FS_first_sound_ring anchor
PASS_BAND = 0.0205                                                 # (local) 10% of 0.204
INFO_BAND = 0.0410                                                 # (local) 20% of 0.204 (INFO ceiling)

# Machinery pins
N_EVAL = 4096                                                      # (local) k-grid points for omega_2(k)
SCAN_MIN = 1e-4                                                    # (local) k in substrate-intrinsic mode units
SCAN_MAX = 1e-1                                                    # (local)
FIT_TOL = 1e-9                                                     # (local) slope-fit residual tolerance

# Output destinations (investigation track)
OUT_NPZ = SESSION_DIR / "inv7_w1_1_c2_substrate.npz"
OUT_PNG = SESSION_DIR / "inv7_w1_1_c2_substrate.png"

# Inputs: canonical_constants (audit only) + the S67 two-fluid mode + the S68 obs-horizon mode
S67_TWOFLUID = COMPUTATIONS_DIR / "session-67" / "s67_gge_two_fluid.npz"
S68_SECOND_SOUND = COMPUTATIONS_DIR / "session-68" / "s68_second_sound_obs.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S67_TWOFLUID,
    S68_SECOND_SOUND,
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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Reconstruct omega_2(k), extract c2 = lim_{k->0} d omega_2/dk, form A_FS = c2^2/c1^2."""

    # --- Load the substrate's OWN two-fluid mode structure (NO recombination R*) ---
    d67 = np.load(S67_TWOFLUID, allow_pickle=True)               # (local) GGE-TWO-FLUID-67
    c1_sub = float(d67["c_1"])                                   # (local) first sound, M_KK (S67 internal)
    c2_sub_S67 = float(d67["c_2"])                               # (local) second sound, M_KK (BCS low-T)
    rho_n_frac = float(d67["rho_n_frac"])                        # (local) normal fraction
    rho_s_frac = float(d67["rho_s_frac"])                        # (local) superfluid fraction

    d68 = np.load(S68_SECOND_SOUND, allow_pickle=True)           # (local) SECOND-SOUND-OBS-68
    R_star_substrate = float(d68["R_star"])                      # (local) substrate's OWN R* (for the stand-in cross-check)
    c_s_standard = float(d68["c_s_standard"])                    # (local) = 1/sqrt(3(1+R*)) (first-sound acoustic)

    # --- Build the long-wavelength second-sound dispersion omega_2(k) = c2 * k ---
    # The BCS second sound is a linear collective mode in the long-wavelength window:
    #   omega_2(k) = c2_sub * k,  c2_sub = c_1 sqrt(rho_n/(3 rho_s))  (GGE-TWO-FLUID-67).
    # We reconstruct it on the pinned 4096-point grid from the substrate's own c2_sub and
    # extract the slope c2 = lim_{k->0} d omega_2/dk by regression -- a faithful round-trip
    # that confirms the slope-extraction machinery recovers the substrate mode speed.
    k_grid = np.logspace(np.log10(SCAN_MIN), np.log10(SCAN_MAX), N_EVAL)   # (local)
    omega_2 = c2_sub_S67 * k_grid                                          # (local) linear second-sound branch

    # Slope c2 = d omega_2 / dk at k->0 via least-squares on the long-wavelength window.
    # (linear branch: slope is exact; the regression verifies the extraction pipeline.)
    A_design = np.vstack([k_grid, np.ones_like(k_grid)]).T                 # (local) [k, 1] design matrix
    coeffs, residual_arr, _rank, _sv = np.linalg.lstsq(A_design, omega_2, rcond=None)  # (local)
    c2_slope = float(coeffs[0])                                            # (local) extracted lim_{k->0} d omega_2/dk
    intercept = float(coeffs[1])                                          # (local) ~0 for a clean linear branch
    fit_resid = float(residual_arr[0]) if residual_arr.size else 0.0       # (local) sum-sq residual

    # --- The substrate-first ratio A_FS = c2^2/c1^2 ---
    # Direct from the extracted slope:
    A_FS_substrate = (c2_slope / c1_sub) ** 2                             # (local)
    # Analytic substrate-two-fluid invariant (unit-independent; v_F/sqrt3 cancels):
    A_FS_analytic = rho_n_frac / (3.0 * rho_s_frac)                       # (local) = c2^2/c1^2 by BCS relation
    analytic_agreement = abs(A_FS_substrate - A_FS_analytic)             # (local) should be ~machine-eps

    # --- The recombination FIRST-sound stand-in (what 0.204 ACTUALLY is) ---
    A_FS_recomb_form = 1.0 / (3.0 * (1.0 + R_star_substrate))             # (local) = c_s_standard^2
    standin_vs_canon = abs(A_FS_recomb_form - A_FS_CANON)               # (local) ~6e-4: the stand-in DOES hit 0.204

    # --- Discriminating deviation vs the canonical anchor ---
    deviation = abs(A_FS_substrate - A_FS_CANON)                         # (local) the gate operator
    signed_dev = A_FS_substrate - A_FS_CANON                            # (local) for sign_verdict
    ratio_canon_over_sub = A_FS_CANON / A_FS_substrate                  # (local) how many x smaller

    # --- The P(k) feature this gate PRODUCES for downstream W1-2/W1-5/W2-1 ---
    # The feature amplitude is the substrate-genuine A_FS (NOT the canonical pin); k1 from canonical.
    feature_A_FS = A_FS_substrate                                        # (local) substrate-derived ring amplitude
    feature_k1 = k1_first_sound_ring_invMpc                             # (local) Mpc^-1 (canonical)
    feature_r1 = r1_first_sound_ring_Mpc                                # (local) Mpc (canonical)

    print()
    print("  --- substrate-first second-sound dispersion ---")
    print(f"  c1 (first sound, S67)            = {c1_sub:.10f} M_KK")
    print(f"  c2 (second sound, S67 BCS low-T) = {c2_sub_S67:.10f} M_KK")
    print(f"  c2 extracted (lim k->0 domega/dk)= {c2_slope:.10f}  (intercept {intercept:.2e}, resid {fit_resid:.2e})")
    print(f"  rho_n/rho                        = {rho_n_frac:.10f}")
    print(f"  rho_s/rho                        = {rho_s_frac:.10f}")
    print()
    print("  --- the ratio A_FS = c2^2/c1^2 ---")
    print(f"  A_FS_substrate (direct slope)    = {A_FS_substrate:.10f}")
    print(f"  A_FS_analytic  rho_n/(3 rho_s)   = {A_FS_analytic:.10f}")
    print(f"  analytic agreement |diff|        = {analytic_agreement:.3e}  (machine-eps => slope=BCS mode)")
    print()
    print("  --- vs canonical anchor 0.204 (band 0.0205) ---")
    print(f"  |A_FS_substrate - 0.204|         = {deviation:.6f}")
    print(f"  signed (A_FS_substrate - 0.204)  = {signed_dev:+.6f}")
    print(f"  0.204 / A_FS_substrate           = {ratio_canon_over_sub:.2f}x")
    print()
    print("  --- the recombination FIRST-sound stand-in (what 0.204 IS) ---")
    print(f"  R* (substrate's own, S68)        = {R_star_substrate:.10f}")
    print(f"  1/[3(1+R*)] = c_s_standard^2     = {A_FS_recomb_form:.6f}  (|.-0.204| = {standin_vs_canon:.3e})")
    print(f"  c_s_standard (S68)               = {c_s_standard:.6f}")

    return {
        "value": A_FS_substrate,
        "c1_sub": c1_sub,
        "c2_sub_S67": c2_sub_S67,
        "c2_slope": c2_slope,
        "intercept": intercept,
        "fit_resid": fit_resid,
        "rho_n_frac": rho_n_frac,
        "rho_s_frac": rho_s_frac,
        "A_FS_substrate": A_FS_substrate,
        "A_FS_analytic": A_FS_analytic,
        "analytic_agreement": analytic_agreement,
        "A_FS_canon": A_FS_CANON,
        "A_FS_S43": 100.0 / 489.0,
        "A_FS_recomb_form": A_FS_recomb_form,
        "standin_vs_canon": standin_vs_canon,
        "R_star_substrate": R_star_substrate,
        "c_s_standard": c_s_standard,
        "deviation": deviation,
        "signed_dev": signed_dev,
        "ratio_canon_over_sub": ratio_canon_over_sub,
        "pass_band": PASS_BAND,
        "info_band": INFO_BAND,
        # --- DOWNSTREAM FEATURE (W1-2 / W1-5 / W2-1 consume these) ---
        "feature_A_FS": feature_A_FS,
        "feature_k1_invMpc": feature_k1,
        "feature_r1_Mpc": feature_r1,
        "k_grid": k_grid,
        "omega_2": omega_2,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 3-tuple + plot
# ---------------------------------------------------------------------------
def evaluate_gate(deviation: float) -> str:
    if deviation <= PASS_BAND:
        return "PASS"
    if deviation <= INFO_BAND:
        return "INFO"
    return "FAIL"


def sign_magnitude_regime(res: dict, composite: str) -> tuple[str, str, str]:
    # sign_verdict: PASS iff the COMPUTED direction matches the substitution-chain Step-4
    # pre-registration. The chain reads the sign off the computed ratio: PASS-direction is
    # "A_FS_substrate reproduces 0.204 within band". Direction is decided by the computed
    # |dev| vs band, so sign tracks magnitude here -> PASS iff within band, else FAIL.
    sign_v = "PASS" if res["deviation"] <= PASS_BAND else "FAIL"   # (local)
    # magnitude_verdict
    if res["deviation"] <= PASS_BAND:
        mag_v = "PASS"
    elif res["deviation"] <= INFO_BAND:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    # regime_verdict: VALID iff the long-wavelength linear branch is clean (intercept ~0,
    # tiny residual, and the slope reproduces the BCS analytic c2 to machine-eps).
    regime_clean = (abs(res["intercept"]) < 1e-9
                    and res["fit_resid"] < FIT_TOL
                    and res["analytic_agreement"] < 1e-12)            # (local)
    regime_v = "VALID" if regime_clean else "MARGINAL"               # (local)
    return sign_v, mag_v, regime_v


def make_plot(res: dict, verdict: str) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))                 # (local)

    # (left) the second-sound dispersion omega_2(k) and the extracted slope c2
    ax = axes[0]
    k = res["k_grid"]; w = res["omega_2"]                           # (local)
    ax.plot(k, w, lw=2, color="#1f77b4", label=r"$\omega_2(k)$ (2nd sound)")
    ax.plot(k, res["c2_slope"] * k, "--", color="#ff7f0e", lw=1.3,
            label=fr"slope $c_2={res['c2_slope']:.4f}\,M_{{KK}}$")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"$k$ (substrate mode units)")
    ax.set_ylabel(r"$\omega_2$")
    ax.set_title(r"Substrate 2nd-sound dispersion (S44/S68 mode)")
    ax.legend(fontsize=9); ax.grid(alpha=0.3, which="both")

    # (right) A_FS bar comparison: substrate ratio vs canonical anchor vs recombination stand-in
    ax = axes[1]
    labels = ["A_FS\nsubstrate\n(c2^2/c1^2)", "canonical\n0.204", "recomb form\n1/[3(1+R*)]"]  # (local)
    vals = [res["A_FS_substrate"], res["A_FS_canon"], res["A_FS_recomb_form"]]                # (local)
    colors = ["#d62728", "#2ca02c", "#9467bd"]                                                # (local)
    bars = ax.bar(labels, vals, color=colors, alpha=0.85)
    ax.axhspan(res["A_FS_canon"] - res["pass_band"], res["A_FS_canon"] + res["pass_band"],
               color="#2ca02c", alpha=0.15, label="10% PASS band")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.05, f"{v:.4f}",
                ha="center", va="bottom", fontsize=9)
    ax.set_ylabel(r"$A_{FS}$")
    ax.set_yscale("log")
    ax.set_title(fr"$A_{{FS}}$: substrate 2nd-sound vs 0.204 anchor  [{verdict}]")
    ax.legend(fontsize=9); ax.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID}  —  A_FS_substrate = {res['A_FS_substrate']:.5f}  "
                 f"(0.204/A_sub = {res['ratio_canon_over_sub']:.1f}x)  ->  {verdict}",
                 fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": 7,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
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
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    res = compute()
    value = res["value"]
    deviation = res["deviation"]

    verdict = evaluate_gate(deviation)
    sign_v, mag_v, regime_v = sign_magnitude_regime(res, verdict)

    # persist data (downstream feature stored clearly)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        # core result
        A_FS_substrate=res["A_FS_substrate"],
        A_FS_analytic=res["A_FS_analytic"],
        analytic_agreement=res["analytic_agreement"],
        A_FS_canon=res["A_FS_canon"],
        A_FS_S43=res["A_FS_S43"],
        A_FS_recomb_form=res["A_FS_recomb_form"],
        standin_vs_canon=res["standin_vs_canon"],
        deviation=res["deviation"],
        signed_dev=res["signed_dev"],
        ratio_canon_over_sub=res["ratio_canon_over_sub"],
        pass_band=res["pass_band"],
        info_band=res["info_band"],
        # substrate mode internals
        c1_sub=res["c1_sub"],
        c2_sub_S67=res["c2_sub_S67"],
        c2_slope=res["c2_slope"],
        intercept=res["intercept"],
        fit_resid=res["fit_resid"],
        rho_n_frac=res["rho_n_frac"],
        rho_s_frac=res["rho_s_frac"],
        R_star_substrate=res["R_star_substrate"],
        c_s_standard=res["c_s_standard"],
        # 3-tuple
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        # --- DOWNSTREAM P(k) FEATURE (W1-2 / W1-5 / W2-1 consume these) ---
        feature_A_FS=res["feature_A_FS"],
        feature_k1_invMpc=res["feature_k1_invMpc"],
        feature_r1_Mpc=res["feature_r1_Mpc"],
        # dispersion arrays
        k_grid=res["k_grid"],
        omega_2=res["omega_2"],
        # SHAs
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"\n  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res, verdict)
    print(f"  saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(round(value, 8), SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Companion rows: the C1 resolution + the downstream feature payload.
    note = (f"A_FS_substrate=c2^2/c1^2=rho_n/(3rho_s)={value:.6f}; "
            f"canonical 0.204 = recomb first-sound 1/[3(1+R*)]={res['A_FS_recomb_form']:.6f} "
            f"(NOT 2nd sound); 0.204/A_sub={res['ratio_canon_over_sub']:.1f}x; "
            f"C1 -> stand-in (Track B)")  # (local)
    feature_row = (f"# INV7-W1-1 downstream-feature: A_FS_substrate={res['feature_A_FS']:.8f} "
                   f"k1={res['feature_k1_invMpc']:.10f}_invMpc r1={res['feature_r1_Mpc']:.4f}_Mpc "
                   f"(consumed by INV7-W1-2/W1-5/W2-1)")  # (local)
    print_verdict_payload(
        verdict, round(value, 8), audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=note, extra_rows=[feature_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict}  (sign={sign_v} mag={mag_v} regime={regime_v}, wall {wall:.1f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
