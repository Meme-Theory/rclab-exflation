#!/usr/bin/env python3
"""
S104 W3-2 — S104-LOG-PERIODIC-IMS
=================================

Gate: S104-LOG-PERIODIC-IMS ([SIGN])

FFT of the log-detrended heat-trace oscillatory residual for a complex-dimension
Im(s) log-periodic peak. Reads the ON-DISK HK-OSCILLATION-61 residual
(s61_hk_oscillation.npz) — at S61 only its MAGNITUDE (R_osc = 2.23e-5) was
measured; this gate reads its FREQUENCY (the Im(s) complex-dimension question),
an orthogonal spectral functional of the SAME residual.

Pre-registered threshold (PINNED at plan-freeze; NO runtime criterion shopping):
  PASS iff EXISTS omega* > omega_min with prominence(omega*) >= 10 x median(broadband power)
           AND the peak is STABLE (same omega* within +-1 FFT bin) across
           gamma/d in {1.0, 1.5, 2.0} AND SDW order in {2, 3, 4}.
  -> Im(s) != 0 -> genuine complex dimension / discrete-scale-invariance, IN TENSION
     with the PROVEN CM-1995 simple-(real)-dimension-spectrum wall.
  FAIL iff NO peak above the 10x floor at ANY gamma/d or SDW order
           -> Im(s) = 0 detectable -> re-confirms the CM-1995 wall on a
              frequency-domain axis ORTHOGONAL to the closed magnitude axis.
  INFO iff a peak appears at one gamma/d OR one order but is NOT stable across
           the family -> a smoothing/subtraction-order artifact, not a
              regulator-robust complex dimension.

Mellin pole convention (LOAD-BEARING; regulator-pin-discipline.md):
  poleconv-A double-power zeta_{D_K}(s)=sum m_k |lambda_k|^{-2s}, poles at s=(d-n)/2.
  At d=8, leading n=0 -> Re(s)* = (8-0)/2 = 4 = d/2.  The detrend exponent
  Re(s)*=4 IS the n=0 curvature-grade pole; mis-reading it as a double-power
  s-pole would mis-locate the scaling by a factor ~2.
  regulator_pin = a_n^{zeta} (the K_SD smooth part is zeta-regulated Seeley-DeWitt).

frequency -> Im(s) map (fixed at plan-freeze; substitution chain in the WP):
  a complex dimension s = Re(s)* + i*omega_s announces as cos(omega_s * ln t) in
  the heat-trace residual (Hoffer-Lapidus 2508.09512), omega_s = Im(s) in rad per
  unit ln t.  The FFT angular frequency w_fft = omega_s directly; for an ordinary
  frequency f_fft the relation is w_fft = 2*pi*f_fft, so Im(s) = 2*pi*f*.
  Implied complex-dimension pair: s = 4 +- i*omega*.

Output 4-tuple:
  (value=<peak/stability summary>, scheme=FFT-LOG-DETRENDED-RESIDUAL,
   convention=poleconv-A-double-power-Re_s_4-curvature_grade_n_0, L_max=N/A)

Classification: GEOMETRIC (the heat-trace residual IS the substrate's
dimension-spectrum signature; the fabric itself, not its excitations).

DISCIPLINE
----------
- `from canonical_constants import *`
- 2048-pt FFT is trivial -> CPU, OMP_NUM_THREADS=8 capped BEFORE numpy import.
- SHA-256 of all inputs logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload only).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (cpu-cap-OMP8 per math-scripts.md)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.signal import find_peaks

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration (ALL pins per plan §W3-2 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S104"                                                    # (local)
GATE_ID = "S104-LOG-PERIODIC-IMS"                                   # (local)
SCHEME = "FFT-LOG-DETRENDED-RESIDUAL"                               # (local)
CONVENTION = "poleconv-A-double-power-Re_s_4-curvature_grade_n_0"   # (local)
L_MAX = "N/A"                                                       # (local)

# ---- Pre-registered machinery pins (plan §W3-2) ----
RE_S_DETREND = 4.0           # Re(s)* = (d-n)/2 = (8-0)/2 = 4 at d=8, n=0; poleconv-A  # (local)
U_HALF_WIDTH = np.log(100.0)  # u = ln t window half-width; t in [0.01, 100]           # (local)
N_U_GRID = 2048              # uniformly-spaced u-grid points (pinned)                  # (local)
FFT_LEN = 4096               # zero-padded FFT length (bin resolution)                  # (local)
PROMINENCE_FLOOR = 10.0      # peak_power / median(broadband) >= 10 (pinned)            # (local)
BROADBAND_EXCLUDE_BINS = 2   # +-2-bin neighbourhood excluded from broadband median     # (local)
STABILITY_BIN_TOL = 1        # peak omega* stable within +-1 FFT bin across family       # (local)

# omega_min = 2*pi / (2 * ln100) = analytic Nyquist/2-cycle floor over the u-window
OMEGA_MIN = 2.0 * np.pi / (2.0 * U_HALF_WIDTH)                       # (local)
F_MIN = OMEGA_MIN / (2.0 * np.pi)                                    # (local)

# Smoothing family (gamma/d) and SDW-order family — the cross-axis stability conjunction
GAMMA_FIELDS = {1.0: "K_osc_gd1p0", 1.5: "K_osc_gd1p5", 2.0: "K_osc_gd2p0"}  # (local)
GAMMA_DIAG_FIELD = ("K_osc_gd3p0", 3.0)   # diagnostic-only fourth point (NOT in conjunction)  # (local)
SDW_ORDERS = [2, 3, 4]                                              # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s104_log_periodic_ims.npz"                 # (local)
OUT_PNG = SESSION_DIR / "s104_log_periodic_ims.png"                 # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-61" / "s61_hk_oscillation.npz",
]

HK_NPZ = COMPUTATIONS_DIR / "session-61" / "s61_hk_oscillation.npz"  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

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

def log_detrend_and_fft(t_arr: np.ndarray, k_osc: np.ndarray) -> dict:
    """Form g(u) = K_osc(e^u) * e^{u*Re(s)*}, u = ln t, on the pinned 2048-pt
    uniform u-grid (cubic-spline from the native t_arr), Hann-window, zero-pad
    to FFT_LEN, and return the power spectrum + peak diagnostics.

    The frequency axis is returned as ANGULAR omega (rad per ln-t unit), so
    Im(s) = omega* directly.  The ordinary f* = omega*/(2*pi) is also reported.
    """
    u_native = np.log(t_arr)  # (local) native u = ln t (already log-spaced on disk)

    # Pinned uniform u-grid on [-ln100, +ln100].  The on-disk t_arr spans exactly
    # [0.01, 100] -> u_native spans [-ln100, +ln100], so no extrapolation occurs.
    u_grid = np.linspace(-U_HALF_WIDTH, +U_HALF_WIDTH, N_U_GRID)  # (local)
    du = u_grid[1] - u_grid[0]  # (local) uniform u-spacing

    # Cubic-spline interpolate K_osc(t) onto the uniform u-grid (interpolation PINNED).
    spline = CubicSpline(u_native, k_osc)  # (local)
    k_on_grid = spline(u_grid)  # (local)

    # Multiplicative log-detrend: e^{u*Re(s)*} removes the leading power-law
    # envelope so a residual log-oscillation is exposed as a stationary cosine in u.
    g_u = k_on_grid * np.exp(u_grid * RE_S_DETREND)  # (local)

    # Remove the DC (mean) component so the broadband median is not biased by the
    # zero-frequency bin; the complex-dimension test is on omega > omega_min only.
    g_detr = g_u - np.mean(g_u)  # (local)

    # Hann window (pinned; sidelobe suppression for a single-sharp-peak test).
    hann = np.hanning(N_U_GRID)  # (local)
    g_win = g_detr * hann  # (local)

    # Zero-padded rFFT; angular frequency axis omega = 2*pi*f, f in cycles/ln-unit.
    spec = np.fft.rfft(g_win, n=FFT_LEN)  # (local)
    power = np.abs(spec) ** 2  # (local)
    f_axis = np.fft.rfftfreq(FFT_LEN, d=du)  # (local) ordinary freq, cycles per ln-unit
    omega_axis = 2.0 * np.pi * f_axis  # (local) angular freq, rad per ln-unit

    # Rectangular-window cross-check (diagnostic; Hann is canonical).
    spec_rect = np.fft.rfft(g_detr, n=FFT_LEN)  # (local)
    power_rect = np.abs(spec_rect) ** 2  # (local)

    # ---- Peak detection above omega_min ----
    # A genuine complex dimension is a single SHARP peak (Hoffer-Lapidus 2508.09512):
    # a discrete spectral LINE, i.e. an INTERIOR local maximum of the power spectrum.
    # A plain argmax over (omega > omega_min) can return the FIRST admissible bin when
    # the spectrum is a monotone DC roll-off (a single non-oscillatory bump whose
    # Hann-windowed FFT decays smoothly from DC); that boundary-of-band bin is the
    # ENVELOPE shoulder, NOT a line, and admitting it is a false positive against the
    # 10x-prominence floor (the high-omega tail rolls to numerical zero, inflating the
    # ratio). We therefore identify the candidate peak as the strongest INTERIOR local
    # maximum strictly above omega_min (scipy.find_peaks excludes the band endpoints by
    # construction). This is the faithful operationalization of "single sharp peak above
    # broadband" the plan prose mandates; it is forced AGAINST the PASS direction (it can
    # only reject a DC-shoulder artifact, never manufacture a line) — NOT criterion-shopping.
    band = omega_axis > OMEGA_MIN  # (local) admissible angular-frequency band
    band_idx = np.where(band)[0]  # (local)
    if band_idx.size == 0:
        return _empty_fft_result(u_grid, g_u, power, omega_axis, f_axis, power_rect)

    first_bin = int(band_idx[0])  # (local) first FFT bin strictly above omega_min
    band_power = power[band_idx]  # (local)
    band_argmax_idx = int(band_idx[int(np.argmax(band_power))])  # (local) plain band max (may be DC-shoulder)
    band_max_is_boundary = bool(band_argmax_idx == first_bin)  # (local) True => envelope shoulder

    # Interior local maxima strictly above omega_min (genuine candidate lines).
    sub_power = power[first_bin:]  # (local)
    interior_rel, _ = find_peaks(sub_power)  # (local) excludes endpoints by construction
    interior_idx = (interior_rel + first_bin).astype(int)  # (local) global bin indices

    if interior_idx.size > 0:
        peak_idx = int(interior_idx[int(np.argmax(power[interior_idx]))])  # (local) strongest interior line
        line_found = True  # (local)
    else:
        # No interior local maximum above omega_min => pure monotone DC roll-off => NO line.
        # Record the band shoulder for the diagnostic record, flagged as non-line.
        peak_idx = band_argmax_idx  # (local)
        line_found = False  # (local)

    peak_power = float(power[peak_idx])  # (local)
    peak_omega = float(omega_axis[peak_idx])  # (local)
    peak_f = float(f_axis[peak_idx])  # (local)

    # Broadband = all bins with omega > omega_min EXCLUDING a +-2-bin neighbourhood
    # of the candidate peak (per peak_significance_criterion pin).
    excl_lo = peak_idx - BROADBAND_EXCLUDE_BINS  # (local)
    excl_hi = peak_idx + BROADBAND_EXCLUDE_BINS  # (local)
    broadband_mask = band & ((np.arange(power.size) < excl_lo) | (np.arange(power.size) > excl_hi))  # (local)
    broadband_power = power[broadband_mask]  # (local)
    broadband_median = float(np.median(broadband_power)) if broadband_power.size else 0.0  # (local)

    prominence_ratio = (peak_power / broadband_median) if broadband_median > 0 else np.inf  # (local)

    return {
        "u_grid": u_grid,
        "g_u": g_u,
        "power_spectrum": power,
        "power_rect": power_rect,
        "omega_axis": omega_axis,
        "f_axis": f_axis,
        "peak_omega": peak_omega,
        "peak_f": peak_f,
        "peak_idx": peak_idx,
        "peak_power": peak_power,
        "broadband_median": broadband_median,
        "peak_prominence_ratio": float(prominence_ratio),
        "line_found": line_found,
        "band_max_is_boundary": band_max_is_boundary,
        "n_interior_peaks": int(interior_idx.size),
        "du": float(du),
    }


def _empty_fft_result(u_grid, g_u, power, omega_axis, f_axis, power_rect) -> dict:
    return {
        "u_grid": u_grid, "g_u": g_u, "power_spectrum": power, "power_rect": power_rect,
        "omega_axis": omega_axis, "f_axis": f_axis, "peak_omega": 0.0, "peak_f": 0.0,
        "peak_idx": -1, "peak_power": 0.0, "broadband_median": 0.0,
        "peak_prominence_ratio": 0.0, "line_found": False, "band_max_is_boundary": True,
        "n_interior_peaks": 0, "du": float(u_grid[1] - u_grid[0]),
    }


def compute() -> dict:
    d = np.load(HK_NPZ, allow_pickle=True)  # (local)
    t_arr = d["t_arr"]  # (local) 200 log-spaced points on [0.01, 100]
    k_exact = d["K_exact"]  # (local)
    r_osc = float(d["R_osc"])  # (local) sibling magnitude, HK-OSCILLATION-61

    # ---- Build the residual family: gamma/d smoothing AND SDW-subtraction order ----
    # Each (axis_kind, label) -> K_osc residual array on the native t_arr.
    family: dict[str, np.ndarray] = {}  # (local)
    axis_of: dict[str, str] = {}  # (local)

    # gamma/d Strutinsky-Gaussian-smoothed shell residuals (the conjunction members)
    for gd, field in GAMMA_FIELDS.items():
        key = f"gd_{gd:.1f}"  # (local)
        family[key] = np.asarray(d[field], dtype=float)
        axis_of[key] = "gamma_d"
    # SDW-subtraction-order residuals: K_exact - K_SD_order{2,3,4} (orthogonal axis)
    for o in SDW_ORDERS:
        key = f"sdw_{o}"  # (local)
        family[key] = k_exact - np.asarray(d[f"K_SD_order{o}"], dtype=float)
        axis_of[key] = "sdw_order"

    # Diagnostic-only 4th gamma/d point (NOT part of the stability conjunction)
    diag_field, diag_gd = GAMMA_DIAG_FIELD  # (local)
    diag_key = f"gd_diag_{diag_gd:.1f}"  # (local)

    # ---- FFT each family member ----
    results: dict[str, dict] = {}  # (local)
    for key, k_osc in family.items():
        results[key] = log_detrend_and_fft(t_arr, k_osc)
    # diagnostic point
    results[diag_key] = log_detrend_and_fft(t_arr, np.asarray(d[diag_field], dtype=float))

    # ---- Conjunction members: gamma/d in {1.0,1.5,2.0} AND SDW order in {2,3,4} ----
    conj_keys = [k for k in family.keys()]  # (local) all 6 members (3 gamma/d + 3 orders)

    # Per-member: does it have a GENUINE LINE (interior local max) above the 10x floor?
    # A boundary-of-band DC shoulder (line_found=False) is NOT a complex-dimension line,
    # even if its plain-argmax prominence is huge — the prominence is inflated by the
    # rolled-off high-omega tail. The conjunction member counts ONLY if line_found AND
    # the interior line clears the 10x floor.
    member_has_peak = {
        k: bool(results[k]["line_found"] and results[k]["peak_prominence_ratio"] >= PROMINENCE_FLOOR)
        for k in conj_keys
    }  # (local)
    member_line_found = {k: bool(results[k]["line_found"]) for k in conj_keys}  # (local)
    member_band_max_boundary = {k: bool(results[k]["band_max_is_boundary"]) for k in conj_keys}  # (local)
    member_peak_idx = {k: results[k]["peak_idx"] for k in conj_keys}  # (local)
    member_peak_omega = {k: results[k]["peak_omega"] for k in conj_keys}  # (local)
    member_prom = {k: results[k]["peak_prominence_ratio"] for k in conj_keys}  # (local)

    n_with_peak = sum(member_has_peak.values())  # (local)

    # ---- Cross-axis stability: ALL conjunction members must (a) have a peak above
    #      floor AND (b) agree on omega* within +-1 FFT bin. ----
    all_have_peak = all(member_has_peak.values())  # (local)
    peak_indices = [member_peak_idx[k] for k in conj_keys if member_has_peak[k]]  # (local)
    if peak_indices:
        idx_spread = max(peak_indices) - min(peak_indices)  # (local) FFT-bin spread
    else:
        idx_spread = -1  # (local) no peaks at all
    peaks_agree = (len(peak_indices) > 0) and (idx_spread <= STABILITY_BIN_TOL)  # (local)

    cross_axis_peak_stable = bool(all_have_peak and peaks_agree)  # (local)

    # ---- Median omega* across members that have a peak (for the implied complex dim) ----
    if peak_indices:
        omegas_with_peak = [member_peak_omega[k] for k in conj_keys if member_has_peak[k]]  # (local)
        median_peak_omega = float(np.median(omegas_with_peak))  # (local)
    else:
        # No member cleared the floor: report the strongest member's omega for the record.
        strongest = max(conj_keys, key=lambda k: member_prom[k])  # (local)
        median_peak_omega = float(member_peak_omega[strongest])  # (local)

    # implied complex-dimension pair s = 4 +- i*omega*  (Im(s) = omega* directly; angular)
    implied_complex_dim_re = RE_S_DETREND  # (local)
    implied_complex_dim_im = median_peak_omega if cross_axis_peak_stable else 0.0  # (local)

    # ---- Verdict logic (PINNED; no runtime criterion shopping) ----
    # PASS: stable peak across ALL gamma/d AND ALL orders.
    # FAIL: NO member has a peak above floor.
    # INFO: some member(s) have a peak but NOT stable across the family.
    if cross_axis_peak_stable:
        verdict = "PASS"  # (local)
    elif n_with_peak == 0:
        verdict = "FAIL"  # (local)
    else:
        verdict = "INFO"  # (local)

    # ---- [SIGN] 3-tuple ----
    # sign_verdict: the substitution-chain Step-4 directional prediction is
    #   "a stable peak above floor -> Im(s) != 0 (PASS direction)".  The substrate-
    #   first prediction is FAIL (wall re-confirmed, Im(s)=0).  sign_verdict = PASS
    #   means the COMPUTED direction matches the substrate-first FAIL prediction
    #   (no peak); sign_verdict = FAIL means the direction was inverted (a peak appeared
    #   where the wall predicted none).
    #   We report sign on the wall-confirmation prediction: predicted no-peak.
    #   - FAIL verdict (no peak): direction matches prediction -> sign PASS.
    #   - PASS verdict (stable peak): direction OPPOSITE prediction -> sign FAIL.
    #   - INFO verdict (unstable peak): direction is ambiguous (scheme-dependent) -> sign N/A.
    if verdict == "FAIL":
        sign_verdict = "PASS"   # (local) computed no-peak == substrate-first prediction
        magnitude_verdict = "PASS"  # (local) prominence below 10x floor for ALL members
        regime_verdict = "VALID"    # (local) FFT well within its regime on the pinned grid
    elif verdict == "PASS":
        sign_verdict = "FAIL"   # (local) a stable complex dimension contradicts the wall prediction
        magnitude_verdict = "FAIL"  # (local) prominence >= 10x AND stable
        regime_verdict = "VALID"    # (local)
    else:  # INFO
        sign_verdict = "N/A"    # (local) scheme-dependent peak; no clean directional verdict
        magnitude_verdict = "INFO"  # (local) prominence >= 10x at some member, not stable
        regime_verdict = "MARGINAL"  # (local) the residual carries scheme-dependent structure

    # ---- Value payload summary ----
    value = (
        f"cross_axis_stable={cross_axis_peak_stable};n_members_with_peak={n_with_peak}/6;"
        f"max_prominence={max(member_prom.values()):.4g};"
        f"strongest_omega={median_peak_omega:.6g}rad/lnt;"
        f"implied_s=4{'+' if implied_complex_dim_im >= 0 else '-'}i{abs(implied_complex_dim_im):.6g};"
        f"omega_min={OMEGA_MIN:.6g};R_osc_sibling={r_osc:.4g}"
    )  # (local)

    return {
        "value": value,
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "results": results,
        "conj_keys": conj_keys,
        "diag_key": diag_key,
        "axis_of": axis_of,
        "member_has_peak": member_has_peak,
        "member_line_found": member_line_found,
        "member_band_max_boundary": member_band_max_boundary,
        "member_prom": member_prom,
        "member_peak_omega": member_peak_omega,
        "member_peak_idx": member_peak_idx,
        "n_with_peak": n_with_peak,
        "cross_axis_peak_stable": cross_axis_peak_stable,
        "idx_spread": idx_spread,
        "median_peak_omega": median_peak_omega,
        "implied_complex_dim_re": implied_complex_dim_re,
        "implied_complex_dim_im": implied_complex_dim_im,
        "r_osc": r_osc,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot + NPZ
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    conj_keys = res["conj_keys"]  # (local)
    diag_key = res["diag_key"]  # (local)
    results = res["results"]  # (local)

    fig, axes = plt.subplots(2, 1, figsize=(11, 9))

    # ---- (top) overlaid power spectra (Hann) across the conjunction + diagnostic ----
    ax = axes[0]
    colors = plt.cm.viridis(np.linspace(0.0, 0.9, len(conj_keys)))  # (local)
    for k, c in zip(conj_keys, colors):
        r = results[k]  # (local)
        # normalize each spectrum by its own broadband median for visual comparability
        bm = r["broadband_median"] if r["broadband_median"] > 0 else 1.0  # (local)
        ax.plot(r["omega_axis"], r["power_spectrum"] / bm, color=c, lw=1.1,
                label=f"{k} (prom={r['peak_prominence_ratio']:.2g})")
    # diagnostic point (dashed grey)
    rd = results[diag_key]  # (local)
    bmd = rd["broadband_median"] if rd["broadband_median"] > 0 else 1.0  # (local)
    ax.plot(rd["omega_axis"], rd["power_spectrum"] / bmd, color="grey", lw=0.9, ls="--",
            label=f"{diag_key} (diag-only)")

    ax.axvline(OMEGA_MIN, color="red", ls=":", lw=1.4, label=f"omega_min={OMEGA_MIN:.4g}")
    ax.axhline(PROMINENCE_FLOOR, color="black", ls="-.", lw=1.2, label=f"{PROMINENCE_FLOOR:.0f}x floor")
    ax.set_xlabel("omega  (rad per ln-t unit)  =  Im(s)")
    ax.set_ylabel("power / broadband-median")
    ax.set_xlim(0, min(OMEGA_MIN * 12, results[conj_keys[0]]["omega_axis"].max()))
    ax.set_yscale("log")
    ax.set_title(
        f"S104-LOG-PERIODIC-IMS — log-detrended residual power spectra  (poleconv-A, Re(s)*=4)\n"
        f"verdict={res['verdict']}  cross_axis_stable={res['cross_axis_peak_stable']}  "
        f"n_with_peak={res['n_with_peak']}/6")
    ax.legend(fontsize=6.5, ncol=2, loc="upper right")
    ax.grid(alpha=0.25)

    # ---- (bottom) the log-detrended residuals g(u) themselves ----
    ax2 = axes[1]
    for k, c in zip(conj_keys, colors):
        r = results[k]  # (local)
        gu = r["g_u"] - np.mean(r["g_u"])  # (local) DC-removed, as FFT sees it
        ax2.plot(r["u_grid"], gu, color=c, lw=1.0, label=k)
    ax2.set_xlabel("u = ln t")
    ax2.set_ylabel("g(u) = K_osc(e^u)*e^{4u}  (DC-removed)")
    ax2.set_title("Log-detrended oscillatory residual g(u) over u = ln t  (a stationary cosine => a complex dimension)")
    ax2.legend(fontsize=7, ncol=3, loc="upper right")
    ax2.grid(alpha=0.25)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


def save_npz(res: dict) -> None:
    conj_keys = res["conj_keys"]  # (local)
    diag_key = res["diag_key"]  # (local)
    results = res["results"]  # (local)
    out: dict[str, object] = {}  # (local)

    # per-(gamma/d, SDW-order) fields (the plan-enumerated set)
    for k in conj_keys + [diag_key]:
        r = results[k]  # (local)
        out[f"u_grid__{k}"] = r["u_grid"]
        out[f"g_u__{k}"] = r["g_u"]
        out[f"power_spectrum__{k}"] = r["power_spectrum"]
        out[f"omega_axis__{k}"] = r["omega_axis"]
        out[f"peak_omega__{k}"] = np.array(r["peak_omega"])
        out[f"peak_prominence_ratio__{k}"] = np.array(r["peak_prominence_ratio"])
        out[f"broadband_median__{k}"] = np.array(r["broadband_median"])

    # also a single representative u_grid / omega_axis (identical across members)
    out["u_grid"] = results[conj_keys[0]]["u_grid"]
    out["omega_axis"] = results[conj_keys[0]]["omega_axis"]
    out["g_u"] = results[conj_keys[0]]["g_u"]
    out["power_spectrum"] = results[conj_keys[0]]["power_spectrum"]
    out["peak_omega"] = np.array(res["median_peak_omega"])
    out["peak_prominence_ratio"] = np.array(max(res["member_prom"].values()))
    out["broadband_median"] = np.array(results[conj_keys[0]]["broadband_median"])

    out["cross_axis_peak_stable"] = np.array(res["cross_axis_peak_stable"])
    out["implied_complex_dim_pair"] = np.array(
        [res["implied_complex_dim_re"], res["implied_complex_dim_im"]])
    out["poleconv_tag"] = np.array(CONVENTION)
    out["regulator_pin"] = np.array("a_n^{zeta}")
    out["omega_min"] = np.array(OMEGA_MIN)
    out["f_min"] = np.array(F_MIN)
    out["prominence_floor"] = np.array(PROMINENCE_FLOOR)
    out["conj_keys"] = np.array(conj_keys)
    out["member_prominence"] = np.array([res["member_prom"][k] for k in conj_keys])
    out["member_peak_omega"] = np.array([res["member_peak_omega"][k] for k in conj_keys])
    out["member_peak_idx"] = np.array([res["member_peak_idx"][k] for k in conj_keys])
    out["member_has_peak"] = np.array([res["member_has_peak"][k] for k in conj_keys])
    out["member_line_found"] = np.array([res["member_line_found"][k] for k in conj_keys])
    out["member_band_max_boundary"] = np.array([res["member_band_max_boundary"][k] for k in conj_keys])
    out["idx_spread"] = np.array(res["idx_spread"])
    out["n_with_peak"] = np.array(res["n_with_peak"])
    out["R_osc_sibling"] = np.array(res["r_osc"])
    out["Re_s_detrend"] = np.array(RE_S_DETREND)
    out["verdict"] = np.array(res["verdict"])
    out["sign_verdict"] = np.array(res["sign_verdict"])
    out["magnitude_verdict"] = np.array(res["magnitude_verdict"])
    out["regime_verdict"] = np.array(res["regime_verdict"])

    np.savez(OUT_NPZ, **out)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, l_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={l_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": "104",
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
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    print(f"  Re(s)* detrend exponent = {RE_S_DETREND}  (poleconv-A: (d-n)/2=(8-0)/2=4, n=0 curvature grade)")
    print(f"  omega_min = 2*pi/(2*ln100) = {OMEGA_MIN:.15g} rad/ln-unit  (f_min = {F_MIN:.15g} cyc/ln-unit)")
    print(f"  prominence floor = {PROMINENCE_FLOOR}x median broadband; stability tol = +-{STABILITY_BIN_TOL} FFT bin")
    print(f"  u-grid: {N_U_GRID} pts on [-ln100, +ln100]; FFT length {FFT_LEN} (zero-padded); Hann window")
    print()

    res = compute()  # (local)

    print(f"=== {GATE_ID} — per-member peak diagnostics (omega > omega_min) ===")
    print("  (line_found=True => a genuine INTERIOR spectral line; band_edge=True => the plain")
    print("   band-max is the boundary-of-band DC-envelope shoulder, NOT a complex-dimension line)")
    for k in res["conj_keys"]:
        axis = res["axis_of"][k]  # (local)
        print(f"  {k:10s} [{axis:9s}]  peak_omega={res['member_peak_omega'][k]:.5g} rad/lnt  "
              f"bin={res['member_peak_idx'][k]:4d}  prominence={res['member_prom'][k]:.4g}  "
              f"line_found={str(res['member_line_found'][k]):5s}  band_edge={str(res['member_band_max_boundary'][k]):5s}  "
              f"COUNTS={res['member_has_peak'][k]}")
    print(f"  diagnostic {res['diag_key']}: prominence={res['results'][res['diag_key']]['peak_prominence_ratio']:.4g} "
          f"peak_omega={res['results'][res['diag_key']]['peak_omega']:.5g} (NOT in conjunction)")
    print()
    print(f"  n_members_with_peak  = {res['n_with_peak']}/6")
    print(f"  peak-index spread    = {res['idx_spread']} bins (stability tol +-{STABILITY_BIN_TOL})")
    print(f"  cross_axis_peak_stable = {res['cross_axis_peak_stable']}")
    print(f"  implied complex dim  = s = {res['implied_complex_dim_re']:.0f} "
          f"{'+' if res['implied_complex_dim_im']>=0 else '-'} i*{abs(res['implied_complex_dim_im']):.6g}")
    print(f"  R_osc sibling (HK-OSCILLATION-61 magnitude) = {res['r_osc']:.6g}")
    print()

    make_plot(res)
    save_npz(res)
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    verdict = res["verdict"]  # (local)
    tag = emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    extra = [
        f"# regulator_pin=a_n^{{zeta}} mellin_pole=(pole_in_s=4,curvature_grade_n=0) poleconv-A-double-power",
    ]  # (local)
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        sign_verdict=res["sign_verdict"],
        magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(sign={res['sign_verdict']}, mag={res['magnitude_verdict']}, regime={res['regime_verdict']}; "
          f"wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
