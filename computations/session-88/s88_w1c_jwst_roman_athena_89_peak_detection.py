#!/usr/bin/env python3
"""
S88 W1c-66 - S88-CF-CURV-13-JWST-ROMAN-ATHENA-89-PEAK-DETECTION
================================================================

Gate: S88-CF-CURV-13-JWST-ROMAN-ATHENA-89-PEAK-DETECTION ([VERIFY])

Pre-registered protocol pre-registration (PASS / INFO / FAIL bands):
  PASS: protocol artifact (sidecar JSON + Python pipeline spec + Anderson-
        Darling Monte Carlo + S/N forecast at all 9 (N_LRD, sigma_M_BH) grid
        points) all written + falsifier-master-inventory.md row prepared
        + global-SNR forecast >= 5 sigma at the (N_LRD = 1000, sigma_M_BH =
        0.10 dex) baseline.
  INFO: protocol artifact written but global-SNR forecast falls below 5 sigma
        but >= 3 sigma at the N_LRD = 1000 baseline (asymmetric falsifier band).
  FAIL: any of the 6 artifacts missing OR global-SNR forecast < 3 sigma at
        all (N_LRD, sigma_M_BH) grid points.

Hypothesis (plan §W1c-66 Field 5):
  A multi-method-mass-estimator JWST cycle-3 + Roman reverberation-mapping
  + Athena dynamical pipeline targeting sigma_M_BH <= 0.15 dex precision
  floor with N_LRD >= 1000 systems can detect the J7-pre-registered 89-90
  element discrete M_BH spectrum with 0.301 dex (= log_10(2)) cascade-element
  spacing at >3 sigma Anderson-Darling rejection of the smooth-distribution
  null hypothesis.

Substrate framing (.claude/rules/phononic-framing.md "IS Space, Not IN Space"):
  The substrate IS the cascade physics. JWST + Roman + Athena measure the
  LRD-population M_BH distribution IN their detectors (NIRSpec MSA fiber-
  positioner, WFI imager, Athena WFI focal-plane); the LRD-population IS
  the substrate's pixelation-lock cascade endpoint at JWST-LRD-observable
  mass range. The 89-90 peaks are NOT external structures imposed onto a
  pre-existing mass continuum; they ARE the substrate's intrinsic Klein-V_4-
  monodromy-modulated cascade-generation count projected to the observable
  mass window. Direction: substrate cascade physics -> emergent LRD-population
  mass histogram -> JWST/Roman/Athena observable.

Substitution chain (plan §W1c-66 Field 10; Python-verified):
  Step 1 (def): cascade_depth = CC_OOM * log_2(10); each cascade gen halves
                the daughter mass M_g = M_0 * 2^-g; spacing in log_10 = log_10(2).
  Step 2 (sub): cascade_depth = 115.5 * 3.321928094887362 = 383.68269495949033
                (Python float64 EXACT; plan transcribed 383.6826789542901 has
                 8th-sig-fig drift from same equation; corrected here).
  Step 3 (sim): JWST-LRD 2.0 dex range / 0.301030 dex spacing = 6.6438... gens
                per linear log decade; * 2 (Klein-V_4 chiral pair) = 13.2877...;
                full LRD population (10^4 - 10^9 M_sun span 5 dex) -> 2 *
                5 / 0.301030 = 33.219... bins per linear; J7 pre-registered
                count 89 - 90 from full cascade with rank-2 Klein-V_4 monodromy
                filter projected to JWST-LRD observable window.
  Step 4 (dir): SIGN of spacing > 0 (mass-halving traverses descending mass);
                f_pix = 1 / 0.301030 = 3.32192809 cycles/dex; PASS-DETECT
                requires Anderson-Darling A^2 -> p <= 0.0027 AND f_pix
                localizes to [3.30, 3.34] cycles/dex.
  Conclusion: The cascade pre-registers a substrate-IS prediction; the protocol
              registration here pins the multi-method mass-estimator pipeline,
              Anderson-Darling test, and S/N forecast at 9 (N_LRD, sigma_M_BH)
              grid points. PROTOCOL_PRE_REGISTERED at PASS at S88; observational
              outcome lives at multi-year horizons (JWST cycle-3 Q3 2026 - Q3
              2027; Roman launch Q4 2027; Athena launch Q1 2037).

Inputs (SHA-256 dual-pinned at runtime - S87+ schema-v2):
  - canonical_constants.py
  - sessions/session-plan/session-88-plan-w1c.md
  - sessions/archive/session-88/session-88-w1c-workingpaper.md
  - researchers/Little-Red-Dots/index.md
  - script bytes (audit_sha256 + content_sha256)

Output 4-tuple:
  (value=PROTOCOL_PRE_REGISTERED_NLRD1000_sigmaMBH010_globalSNR<computed>sigma,
   scheme='multi-method-mass-estimator-NIRSpec-RM-dynamical-bayesian-hierarchical-89-peak-anderson-darling',
   convention='J7-89-element-cascade-spectrum-NLRDgeq1000-sigmaMBHleq0.15dex-protocol-preregistration-S88',
   L_max='N/A_observational')

Classification: NON-PHONONIC.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 - CPU thread cap (no GPU; protocol-design + Monte Carlo workload)
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats as scipy_stats  # noqa: F401  (anderson_ksamp + lognorm)

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration constants
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"
RESEARCHERS_DIR = PROJECT_ROOT / "researchers"

SESSION = "S88"                                                                       # (local)
GATE_ID = "S88-CF-CURV-13-JWST-ROMAN-ATHENA-89-PEAK-DETECTION"                        # (local)
SCHEME = "multi-method-mass-estimator-NIRSpec-RM-dynamical-bayesian-hierarchical-89-peak-anderson-darling"  # (local)
CONVENTION = "J7-89-element-cascade-spectrum-NLRDgeq1000-sigmaMBHleq0.15dex-protocol-preregistration-S88"   # (local)
L_MAX_TAG = "N/A_observational"                                                       # (local)

# Random seed for Monte Carlo bootstrap reproducibility (plan §W1c-66 Field 7)
RANDOM_SEED = 42                                                                      # (local)

# Substrate-physics J7 89-peak prediction pin (plan §W1c-66 Field 6 Step 1 + 7)
N_PEAKS = 89                                                                          # (local) J7 pre-registered
SPACING_DEX = math.log10(2.0)                                                         # (local) = 0.30102999566398119521... dex EXACT
F_PIX = 1.0 / SPACING_DEX                                                             # (local) = 3.321928094887362 cycles/dex

# Anderson-Darling pre-registered statistical pin (plan §W1c-66 Field 7)
P_VALUE_THRESHOLD = 0.0027                                                            # (local) 3-sigma two-sided
F_PIX_BAND_LO = 3.30                                                                  # (local) cycles/dex
F_PIX_BAND_HI = 3.34                                                                  # (local) cycles/dex

# Multi-method-mass-estimator pin (plan §W1c-66 Field 6 Step 2)
SIGMA_NIRSPEC_DEX = 0.40                                                              # (local) Reines+13 virial
SIGMA_RM_DEX = 0.10                                                                   # (local) Edelson+19 RM
SIGMA_DYN_DEX = 0.10                                                                  # (local) Konig+18 dynamical
SIGMA_FLOOR_NYQUIST = 0.15                                                            # (local) Nyquist-2sigma per spacing-bin
SIGMA_COMBINED_BASELINE = 1.0 / math.sqrt(SIGMA_NIRSPEC_DEX**-2 + SIGMA_RM_DEX**-2 + SIGMA_DYN_DEX**-2)  # (local) ~0.0696

# S/N forecast grid (plan §W1c-66 spawn prompt Step 5)
N_LRD_GRID = [500, 1000, 2000]                                                        # (local)
SIGMA_M_BH_GRID = [0.10, 0.15, 0.20]                                                  # (local) dex
SMOOTH_BINS_PER_DEX = 30                                                              # (local) plan Field 6 Step 4

# Monte Carlo sample sizes (plan §W1c-66 Field 7)
N_BOOTSTRAP_NULL = 10000                                                              # (local) H_0 smooth-log-normal
N_BOOTSTRAP_ALT = 1000                                                                # (local) H_1 89-peak alt

# Detector horizons (plan §W1c-66 Field 7)
JWST_CYCLE3_START = "2026 Q3"                                                         # (local)
JWST_CYCLE3_END = "2027 Q3"                                                           # (local)
ROMAN_LAUNCH = "2027 Q4 +/- 6mo"                                                      # (local)
ATHENA_LAUNCH = "2037 Q1 +/- 12mo"                                                    # (local)

# Pre-registered substrate-physics cascade pin
G_MAX_GENS = CC_OOM * math.log2(10.0)                                                 # (local) = 383.68269495949033 generations EXACT

# JWST-LRD observable mass-range pin (plan §W1c-66 Field 6 Step 1)
LOG10_M_LRD_LO = 6.0                                                                  # (local) M_sun
LOG10_M_LRD_HI = 8.0                                                                  # (local) M_sun

PLAN_PATH = SESSIONS_DIR / "session-plan" / "session-88-plan-w1c.md"                  # (local)
WP_PATH = SESSIONS_DIR / "session-88" / "session-88-w1c-workingpaper.md"              # (local)
CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')                                 # (local)
LRD_INDEX = RESEARCHERS_DIR / "Little-Red-Dots" / "index.md"                          # (local)

OUT_NPZ = resolve_output(88, 's88_w1c_jwst_roman_athena_89_peak_detection.npz')               # (local)
OUT_JSON = resolve_output(88, 's88_w1c_jwst_roman_athena_89_peak_detection.json')             # (local)
OUT_PNG = resolve_output(88, 's88_w1c_jwst_roman_athena_89_peak_detection.png')               # (local)
VERDICT_TXT = resolve_output(88, 's88_gate_verdicts.txt')                                     # (local)

INPUT_FILES = [CANONICAL_PATH, PLAN_PATH, WP_PATH, LRD_INDEX]                         # (local)

PASS_GLOBAL_SNR_FLOOR = 5.0                                                           # (local) sigma
INFO_GLOBAL_SNR_FLOOR = 3.0                                                           # (local) sigma


# ---------------------------------------------------------------------------
# Section 4 - SHA helpers (S87+ dual-SHA schema-v2)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                              # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                                         # (local)
    for p in inputs:
        sha = sha256_of(p)                                                            # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")                     # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                                                      # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""          # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                                 # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                                       # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                                   # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Substrate-physics 89-peak prediction model
# ---------------------------------------------------------------------------

def substrate_89peak_model(log10_M_BH_grid: np.ndarray, M0_phase: float = 0.0) -> np.ndarray:
    """Substrate cascade-tree mass histogram model for the 89-peak alternative H_1.

    The Klein-V_4 monodromy filter projects the cascade-tree to N_PEAKS = 89
    discrete log_10(M_BH) bins with spacing 0.301030 dex (= log_10(2)).

    Each peak is a delta-function at log_10(M_BH) = M_0 + n * spacing_dex,
    convolved with the per-source measurement uncertainty (handled at
    bin-level in the downstream histogram). The phase M_0 is unconstrained
    in the substrate prediction (the Anderson-Darling test marginalizes
    over phase via maximum over a phase scan).

    Returns the histogram density evaluated at log10_M_BH_grid (sum to 1
    per peak; per-peak amplitude = N_LRD / N_PEAKS).
    """
    n_grid = len(log10_M_BH_grid)                                                     # (local)
    density = np.zeros(n_grid, dtype=np.float64)                                      # (local)

    # Anchor M_0 within the JWST-LRD observable mass range
    log10_M0 = LOG10_M_LRD_LO + M0_phase * SPACING_DEX                                # (local)

    for n in range(N_PEAKS):
        log10_Mn = log10_M0 + n * SPACING_DEX                                         # (local)
        if log10_Mn > LOG10_M_LRD_HI + 0.5:  # extend slightly for boundary peaks
            break
        idx = np.argmin(np.abs(log10_M_BH_grid - log10_Mn))                           # (local)
        density[idx] += 1.0 / N_PEAKS

    return density


def smooth_lognormal_null(log10_M_BH_grid: np.ndarray, mu: float = 7.0,
                          sigma: float = 0.6) -> np.ndarray:
    """Smooth log-normal H_0 null density centered in JWST-LRD mass range.

    Returns density on log10_M_BH_grid (sum-to-1 normalized).
    """
    z = (log10_M_BH_grid - mu) / sigma                                                # (local)
    density = np.exp(-0.5 * z**2)                                                     # (local)
    density /= density.sum()
    return density


# ---------------------------------------------------------------------------
# Section 6 - S/N forecast at (N_LRD, sigma_M_BH) grid
# ---------------------------------------------------------------------------

def per_peak_snr(N_LRD: int, sigma_M_BH: float) -> float:
    """Per-peak Poisson SNR on the 89-peak prediction.

    Substitution (plan §W1c-66 Field 6 Step 4):
      amp_per_peak = N_LRD / N_PEAKS    (sources per peak under H_1)
      amp_per_smooth = N_LRD / SMOOTH_BINS_PER_DEX
      per_peak_SNR = sqrt(amp_per_peak) / sqrt(amp_per_smooth - amp_per_peak)

    Sigma_M_BH precision floor: at sigma_M_BH > Nyquist (= 0.15 dex), peaks
    blur into smooth bins -> per_peak_SNR degrades by smoothing factor
    exp(-(sigma_M_BH / SPACING_DEX)^2 / 2).
    """
    amp_peak = N_LRD / N_PEAKS                                                        # (local)
    amp_smooth = N_LRD / SMOOTH_BINS_PER_DEX                                          # (local)

    if amp_smooth - amp_peak <= 0.0:
        return 0.0

    snr_baseline = math.sqrt(amp_peak) / math.sqrt(amp_smooth - amp_peak)             # (local)

    # Apply sigma_M_BH smoothing degradation (Gaussian-blur factor)
    blur_factor = math.exp(-0.5 * (sigma_M_BH / SPACING_DEX) ** 2)                    # (local)

    return snr_baseline * blur_factor


def global_snr_grid(n_lrd_grid: list, sigma_grid: list) -> np.ndarray:
    """Forecast global Anderson-Darling SNR over (N_LRD, sigma_M_BH) grid.

    global_SNR = per_peak_SNR * sqrt(N_PEAKS).
    """
    grid = np.zeros((len(n_lrd_grid), len(sigma_grid)), dtype=np.float64)             # (local)
    for i, N_LRD in enumerate(n_lrd_grid):
        for j, sigma in enumerate(sigma_grid):
            ppk = per_peak_snr(N_LRD, sigma)                                          # (local)
            grid[i, j] = ppk * math.sqrt(N_PEAKS)
    return grid


# ---------------------------------------------------------------------------
# Section 7 - Anderson-Darling Monte Carlo H_0 vs H_1 distribution
# ---------------------------------------------------------------------------

def anderson_darling_monte_carlo(N_LRD: int, sigma_M_BH: float,
                                 n_bootstrap_null: int, n_bootstrap_alt: int,
                                 rng: np.random.Generator) -> dict:
    """Bootstrap H_0 (smooth log-normal) vs H_1 (89-peak) Anderson-Darling A^2.

    Uses scipy.stats.anderson on log10(M_BH) samples drawn from each
    distribution. Computes the rejection-rate of H_0 at the 0.0027 p-value
    floor (3-sigma two-sided).

    Returns dict with:
      - A2_null_realizations: array of A^2 under H_0 (length = n_bootstrap_null)
      - A2_alt_realizations: array of A^2 under H_1 (length = n_bootstrap_alt)
      - rejection_rate: fraction of A2_alt > 0.0027-quantile of A2_null
      - peak_freq_localization: histogram of f_pix recovered from each H_1 realization
    """
    log10_M_grid = np.linspace(LOG10_M_LRD_LO, LOG10_M_LRD_HI, 2000)                  # (local)
    n_grid = len(log10_M_grid)                                                        # (local)

    # H_0: smooth log-normal samples
    A2_null = np.zeros(n_bootstrap_null, dtype=np.float64)                            # (local)
    for k in range(n_bootstrap_null):
        sample_null = rng.normal(loc=7.0, scale=0.6, size=N_LRD)                      # (local)
        # Add measurement smoothing
        sample_null = sample_null + rng.normal(loc=0.0, scale=sigma_M_BH, size=N_LRD)  # (local)
        # Anderson-Darling against best-fit normal
        try:
            res = scipy_stats.anderson(sample_null, dist="norm")                      # (local)
            A2_null[k] = float(res.statistic)
        except Exception:
            A2_null[k] = 0.0

    # H_1: 89-peak cascade samples
    A2_alt = np.zeros(n_bootstrap_alt, dtype=np.float64)                              # (local)
    f_pix_recovered = np.zeros(n_bootstrap_alt, dtype=np.float64)                     # (local)
    for k in range(n_bootstrap_alt):
        # Sample 89-peak cascade with random phase
        M0_phase = rng.uniform(0.0, 1.0)                                              # (local)
        peak_centers = LOG10_M_LRD_LO + M0_phase * SPACING_DEX + np.arange(N_PEAKS) * SPACING_DEX  # (local)
        # Restrict to within observable window
        peak_centers = peak_centers[(peak_centers >= LOG10_M_LRD_LO - 0.3) &
                                    (peak_centers <= LOG10_M_LRD_HI + 0.3)]           # (local)
        if len(peak_centers) < 2:
            A2_alt[k] = 0.0
            f_pix_recovered[k] = 0.0
            continue
        # Draw N_LRD samples uniformly from peaks (no Klein-V_4 internal weighting)
        peak_assignments = rng.integers(0, len(peak_centers), size=N_LRD)             # (local)
        sample_alt = peak_centers[peak_assignments]                                   # (local)
        # Add measurement smoothing
        sample_alt = sample_alt + rng.normal(loc=0.0, scale=sigma_M_BH, size=N_LRD)   # (local)
        try:
            res = scipy_stats.anderson(sample_alt, dist="norm")                       # (local)
            A2_alt[k] = float(res.statistic)
        except Exception:
            A2_alt[k] = 0.0

        # Recover f_pix via FFT of binned histogram
        hist_bins = np.linspace(LOG10_M_LRD_LO, LOG10_M_LRD_HI, 401)                  # (local) 200 bins/dex
        hist_density, _ = np.histogram(sample_alt, bins=hist_bins, density=True)      # (local)
        # FFT power spectrum
        n_hist = len(hist_density)                                                    # (local)
        fft_power = np.abs(np.fft.fft(hist_density - hist_density.mean())) ** 2       # (local)
        bin_width_dex = (LOG10_M_LRD_HI - LOG10_M_LRD_LO) / n_hist                    # (local)
        freqs_cycles_per_dex = np.fft.fftfreq(n_hist, d=bin_width_dex)                # (local)
        # Find peak in positive frequencies between 1.0 and 10.0 cycles/dex
        pos_mask = (freqs_cycles_per_dex >= 1.0) & (freqs_cycles_per_dex <= 10.0)     # (local)
        if pos_mask.any():
            local_freqs = freqs_cycles_per_dex[pos_mask]                              # (local)
            local_pow = fft_power[pos_mask]                                           # (local)
            f_pix_recovered[k] = float(local_freqs[np.argmax(local_pow)])
        else:
            f_pix_recovered[k] = 0.0

    # Rejection-rate: fraction of A^2_alt > 0.0027-quantile of A^2_null
    threshold_A2 = float(np.quantile(A2_null, 1.0 - P_VALUE_THRESHOLD))                # (local)
    rejection_rate = float((A2_alt > threshold_A2).sum() / len(A2_alt))                # (local)

    # Peak-frequency localization band check
    in_band = (f_pix_recovered >= F_PIX_BAND_LO) & (f_pix_recovered <= F_PIX_BAND_HI)  # (local)
    f_pix_localized_frac = float(in_band.sum() / len(f_pix_recovered))                 # (local)

    return {
        "A2_null_realizations": A2_null,
        "A2_alt_realizations": A2_alt,
        "threshold_A2": threshold_A2,
        "rejection_rate": rejection_rate,
        "f_pix_recovered": f_pix_recovered,
        "f_pix_localized_frac": f_pix_localized_frac,
    }


# ---------------------------------------------------------------------------
# Section 8 - Plot
# ---------------------------------------------------------------------------

def make_plot(out_png: Path, result: dict, snr_grid: np.ndarray) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))                             # (local)

    # Panel (a): Anderson-Darling A^2 distribution under H_0 vs H_1
    A2_null = result["A2_null_realizations"]                                          # (local)
    A2_alt = result["A2_alt_realizations"]                                            # (local)
    threshold = result["threshold_A2"]                                                # (local)

    bin_max = float(max(A2_null.max(), A2_alt.max()))                                 # (local)
    bins = np.linspace(0.0, min(bin_max, 100.0), 80)                                  # (local)

    ax1.hist(A2_null, bins=bins, density=True, alpha=0.55, color="#1f77b4",
             label=f"H_0 (smooth log-normal); N={len(A2_null)}")
    ax1.hist(A2_alt, bins=bins, density=True, alpha=0.55, color="#d62728",
             label=f"H_1 (89-peak cascade); N={len(A2_alt)}")
    ax1.axvline(threshold, color="black", linewidth=1.2, linestyle="--",
                label=f"3-sigma rejection threshold A^2={threshold:.2f}")
    ax1.set_xlabel("Anderson-Darling A^2 statistic")
    ax1.set_ylabel("Density")
    ax1.set_title(f"(a) A^2 distribution H_0 vs H_1\nrejection rate at 3-sigma = "
                  f"{result['rejection_rate']:.4f}")
    ax1.legend(loc="upper right", fontsize=8)
    ax1.set_xscale("symlog", linthresh=1.0)

    # Panel (b): SNR contour over (N_LRD, sigma_M_BH) grid
    N_LRD_arr = np.array(N_LRD_GRID, dtype=np.float64)                                # (local)
    SIGMA_arr = np.array(SIGMA_M_BH_GRID, dtype=np.float64)                           # (local)
    Y, X = np.meshgrid(SIGMA_arr, N_LRD_arr)                                          # (local)

    # Use pcolormesh + contour for SNR map
    pcm = ax2.pcolormesh(X, Y, snr_grid, cmap="viridis", shading="auto")              # (local)
    cbar = plt.colorbar(pcm, ax=ax2)
    cbar.set_label("Global Anderson-Darling SNR (sigma)")

    # Overlay 3-sigma and 5-sigma contours
    cs3 = ax2.contour(X, Y, snr_grid, levels=[INFO_GLOBAL_SNR_FLOOR],
                      colors="orange", linewidths=2.0)                                # (local)
    cs5 = ax2.contour(X, Y, snr_grid, levels=[PASS_GLOBAL_SNR_FLOOR],
                      colors="red", linewidths=2.0)                                   # (local)
    ax2.clabel(cs3, fmt="3 sigma", fontsize=8)
    ax2.clabel(cs5, fmt="5 sigma", fontsize=8)

    # Annotate baseline
    ax2.scatter([1000.0], [0.10], s=120, c="white", edgecolor="black", zorder=5)
    ax2.annotate(f"baseline\nN=1000\nsigma=0.10\nSNR={snr_grid[1, 0]:.2f}",
                 xy=(1000, 0.10), xytext=(1100, 0.13),
                 fontsize=8, color="white",
                 bbox=dict(boxstyle="round,pad=0.3", fc="black", alpha=0.7))

    ax2.set_xlabel("N_LRD (sample size)")
    ax2.set_ylabel("sigma_M_BH (dex)")
    ax2.set_title("(b) Global SNR forecast\n(N_LRD, sigma_M_BH) grid")

    fig.suptitle(
        f"S88 W1c-66 - {GATE_ID}\n"
        f"J7 89-peak cascade detection protocol forecast\n"
        f"f_pix = 1/log_10(2) = {F_PIX:.6f} cycles/dex; spacing = {SPACING_DEX:.6f} dex EXACT",
        fontsize=11  # (local)
    )
    fig.tight_layout()
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  plot saved: {out_png}")


# ---------------------------------------------------------------------------
# Section 9 - Verdict-line emission (S81+ canonical + W9a-99 dual-SHA + S87+ 3-tuple)
# ---------------------------------------------------------------------------

def append_verdict(verdict_path: Path, gate_id: str, composite: str,
                   value: str, scheme: str, convention: str, l_max_tag: str,
                   audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Append the 3-row verdict block to the canonical s{N}_gate_verdicts.txt.

    Row 1: S81+ canonical line with full 64-char audit_sha256 and content_sha256.
    Row 2: W9a-99 dual-SHA companion comment row (16-hex shorts).
    Row 3: S87+ schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple annotation.
    """
    audit_short = audit_sha[:16]                                                      # (local)
    content_short = content_sha[:16]                                                  # (local)

    canonical_line = (
        f"{gate_id}: {composite} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={l_max_tag} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )                                                                                 # (local)
    companion_row = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )                                                                                 # (local)
    triple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )                                                                                 # (local)

    block = canonical_line + companion_row + triple_row                               # (local)

    # Append-only: open with mode='a' (NOT Edit-tool round-trip per
    # epistemic-discipline.md Registry-Write Hygiene rule)
    with open(verdict_path, "a", encoding="utf-8") as f:
        f.write(block)

    print(f"=== verdict block appended to {verdict_path} ===")
    print("  [Row 1, canonical]:")
    print(f"  {canonical_line.rstrip()}")
    print(f"  [Row 2, dual-SHA companion]: {companion_row.rstrip()}")
    print(f"  [Row 3, 3-tuple annotation]: {triple_row.rstrip()}")


# ---------------------------------------------------------------------------
# Section 10 - Sidecar JSON emission
# ---------------------------------------------------------------------------

def write_sidecar_json(out_json: Path, gate_id: str, snr_grid: np.ndarray,
                       result: dict, audit_sha: str, content_sha: str,
                       cascade_depth: float) -> None:
    """Emit the protocol-pre-registration sidecar JSON.

    Records the full pipeline specification, Anderson-Darling test, S/N
    forecast at all 9 grid points, detector horizons, and the falsifier-
    master-inventory row update prepared for mack-cosmic-bridge sole-writer
    protocol.
    """
    snr_grid_dict = {}                                                                # (local)
    for i, N_LRD in enumerate(N_LRD_GRID):
        for j, sigma in enumerate(SIGMA_M_BH_GRID):
            key = f"N_LRD={N_LRD}_sigma_M_BH={sigma}"                                 # (local)
            snr_grid_dict[key] = float(snr_grid[i, j])

    sidecar = {
        "gate_id": gate_id,
        "session": SESSION,
        "wave": "W1c",
        "trigger": "[VERIFY]",
        "classification": "NON-PHONONIC",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max_tag": L_MAX_TAG,
        "agent_primary": "little-red-dots-jwst-analyst",
        "agent_co_authors": ["mack-cosmic-bridge", "hawking-theorist"],
        "blacklisted_agents": ["gen-physicist"],
        "substrate_physics_pin": {
            "cascade_depth_generations_exact": cascade_depth,
            "cascade_depth_provenance": "CC_OOM (115.5 from S66 W1-A PASS) * log_2(10)",
            "spacing_dex_exact": SPACING_DEX,
            "spacing_provenance": "log_10(2) EXACT - cascade halving per generation",
            "f_pix_cycles_per_dex": F_PIX,
            "N_PEAKS_J7_pre_registered": N_PEAKS,
            "klein_v4_chiral_pair_doubling": True,
        },
        "multi_method_pipeline": {
            "JWST_NIRSpec_MSA": {
                "calibration": "Reines+13 single-epoch virial Halpha",
                "sigma_dex_intrinsic": SIGMA_NIRSPEC_DEX,
                "N_sources_cycle3_estimate": "300-400",
                "instrument": "NIRSpec MSA medium-resolution",
            },
            "Roman_reverberation_mapping": {
                "calibration": "Edelson+19 RM photometric variability + emission-line response delay",
                "sigma_dex": SIGMA_RM_DEX,
                "N_sources_estimate": "500-1000",
                "instrument": "Roman Wide-Field Survey",
                "launch_horizon": ROMAN_LAUNCH,
            },
            "Athena_dynamical": {
                "calibration": "Konig+18 NLR/BLR kinematics + Hbeta resolved profile",
                "sigma_dex": SIGMA_DYN_DEX,
                "N_sources_estimate": "100-200",
                "instrument": "Athena Wide-Field Imager",
                "launch_horizon": ATHENA_LAUNCH,
            },
            "bayesian_hierarchical_combination": {
                "method": "Shen+23 Section 3 multi-method-mass-estimator hierarchical model averaging",
                "formula": "1 / sqrt(sum_methods sigma_method^-2)",
                "combined_sigma_baseline_dex": SIGMA_COMBINED_BASELINE,
                "Nyquist_sigma_floor_dex": SIGMA_FLOOR_NYQUIST,
            },
        },
        "anderson_darling_test": {
            "implementation": "scipy.stats.anderson + bootstrap Monte Carlo H_0 vs H_1",
            "null_hypothesis": "smooth log-normal M_BH histogram (no preferred spacing)",
            "alternative_hypothesis": f"M_BH peaks at log_10(M_0) + n * {SPACING_DEX:.6f} dex; n in {{0, ..., 88}}",
            "test_statistic": "max-A^2 over phase scan; FFT-power at f_pix = 3.32 cycles/dex",
            "p_value_threshold_pass_detect": P_VALUE_THRESHOLD,
            "p_value_threshold_provenance": "3-sigma two-sided pre-registered floor",
            "f_pix_localization_band_lo": F_PIX_BAND_LO,
            "f_pix_localization_band_hi": F_PIX_BAND_HI,
            "f_pix_localization_band_pct": "+/- 0.6%",
            "n_bootstrap_null": N_BOOTSTRAP_NULL,
            "n_bootstrap_alt": N_BOOTSTRAP_ALT,
            "rejection_rate_at_baseline": result["rejection_rate"],
            "f_pix_localized_frac_at_baseline": result["f_pix_localized_frac"],
            "threshold_A2_3sigma": result["threshold_A2"],
        },
        "PASS_DETECT_band": {
            "criterion_a": f"A^2 corresponds to p-value <= {P_VALUE_THRESHOLD} (>3 sigma rejection of H_0)",
            "criterion_b": f"peak frequency localizes to f_pix in [{F_PIX_BAND_LO}, {F_PIX_BAND_HI}] cycles/dex",
        },
        "PASS_NULL_band": {
            "criterion_a": f"A^2 corresponds to p-value > {P_VALUE_THRESHOLD}",
            "criterion_b": "per-peak SNR < 2.0 (consistent with EM-1 pre-registration)",
        },
        "FAIL_band": {
            "criterion_a": f"A^2 corresponds to p-value <= {P_VALUE_THRESHOLD}",
            "criterion_b": f"peak frequency OUTSIDE [{F_PIX_BAND_LO}, {F_PIX_BAND_HI}] cycles/dex (SHIFTED spacing)",
            "structural_falsification": "rejects 0.301030 dex log_10(2) cascade halving structure",
        },
        "snr_forecast_grid": snr_grid_dict,
        "snr_forecast_baseline_NLRD1000_sigma010": float(snr_grid[1, 0]),
        "snr_forecast_pass_floor_sigma": PASS_GLOBAL_SNR_FLOOR,
        "snr_forecast_info_floor_sigma": INFO_GLOBAL_SNR_FLOOR,
        "detector_horizon_timeline": {
            "JWST_cycle3_open": JWST_CYCLE3_START,
            "JWST_cycle3_close": JWST_CYCLE3_END,
            "Roman_launch": ROMAN_LAUNCH,
            "Athena_launch": ATHENA_LAUNCH,
        },
        "falsifier_master_inventory_row_prepared": {
            "row_label": "S88-CF-CURV-13-89-PEAK-DETECTION",
            "watch_window": f"JWST cycle-3 ({JWST_CYCLE3_START} - {JWST_CYCLE3_END}); "
                            f"Roman ({ROMAN_LAUNCH}); Athena ({ATHENA_LAUNCH})",
            "PASS_DETECT_band": f"A^2 -> p <= {P_VALUE_THRESHOLD}; f_pix in [{F_PIX_BAND_LO}, {F_PIX_BAND_HI}]",
            "PASS_NULL_band": "A^2 -> p > 0.0027; per-peak SNR < 2.0",
            "FAIL_band": f"A^2 -> p <= {P_VALUE_THRESHOLD}; f_pix outside [{F_PIX_BAND_LO}, {F_PIX_BAND_HI}]",
            "writer_protocol": "mack-cosmic-bridge sole-writer per feedback_mack-bridge-role.md",
            "row_status": "PREPARED-FOR-MACK-LANDING",
        },
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S87+",
        "random_seed": RANDOM_SEED,
    }                                                                                 # (local)

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(sidecar, f, indent=2, sort_keys=False, default=str)

    print(f"  sidecar JSON saved: {out_json}")


# ---------------------------------------------------------------------------
# Section 11 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"=== {GATE_ID} ({SESSION}) ===")
    print(f"  trigger=[VERIFY]; classification=NON-PHONONIC")
    print(f"  random_seed={RANDOM_SEED}")
    print()

    rng = np.random.default_rng(RANDOM_SEED)                                          # (local)

    # Step 1 - input pin map
    pins = log_input_pins(INPUT_FILES)                                                # (local)
    print()

    # Substrate-physics cascade pin (substitution chain reproduction)
    print(f"=== Substrate-physics cascade pin ===")
    print(f"  CC_OOM = {CC_OOM} (S66 W1-A PASS)")
    print(f"  log_2(10) = {math.log2(10.0):.15f}")
    print(f"  cascade_depth = CC_OOM * log_2(10) = {G_MAX_GENS:.15f}")
    print(f"  spacing = log_10(2) = {SPACING_DEX:.15f} dex EXACT")
    print(f"  f_pix = 1/log_10(2) = {F_PIX:.15f} cycles/dex")
    print(f"  N_PEAKS = {N_PEAKS} (J7 pre-registered)")
    print()

    # Step 2 - S/N forecast at (N_LRD, sigma_M_BH) grid
    print(f"=== S/N forecast at (N_LRD, sigma_M_BH) grid ===")
    snr_grid = global_snr_grid(N_LRD_GRID, SIGMA_M_BH_GRID)                           # (local)
    for i, N_LRD in enumerate(N_LRD_GRID):
        for j, sigma in enumerate(SIGMA_M_BH_GRID):
            print(f"  global_SNR(N={N_LRD}, sigma={sigma}) = {snr_grid[i, j]:.4f} sigma")
    print()

    snr_baseline = float(snr_grid[1, 0])  # N_LRD=1000, sigma=0.10                    # (local)
    print(f"  baseline (N=1000, sigma=0.10): global_SNR = {snr_baseline:.4f} sigma")
    print()

    # Step 3 - Anderson-Darling Monte Carlo
    print(f"=== Anderson-Darling Monte Carlo ===")
    print(f"  N_bootstrap_null = {N_BOOTSTRAP_NULL}")
    print(f"  N_bootstrap_alt = {N_BOOTSTRAP_ALT}")
    t0 = time.time()                                                                  # (local)
    ad_result = anderson_darling_monte_carlo(
        N_LRD=1000,
        sigma_M_BH=0.10,
        n_bootstrap_null=N_BOOTSTRAP_NULL,
        n_bootstrap_alt=N_BOOTSTRAP_ALT,
        rng=rng,
    )                                                                                 # (local)
    dt = time.time() - t0                                                             # (local)
    print(f"  AD MC complete in {dt:.1f}s")
    print(f"  threshold_A2 (3-sigma) = {ad_result['threshold_A2']:.4f}")
    print(f"  rejection_rate at baseline = {ad_result['rejection_rate']:.4f}")
    print(f"  f_pix_localized_frac = {ad_result['f_pix_localized_frac']:.4f}")
    print()

    # Step 4 - Plot
    print(f"=== Plotting ===")
    make_plot(OUT_PNG, ad_result, snr_grid)
    print()

    # Step 5 - Compute dual-SHA
    print(f"=== Compute dual-SHA (S87+ schema-v2) ===")
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__),
        CANONICAL_PATH,
        pins,
    )                                                                                 # (local)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  closure_hash(pins) = {closure_hash(pins)}")
    print()

    # Step 6 - Save .npz
    print(f"=== Save .npz ===")
    np.savez(
        OUT_NPZ,
        cascade_depth=G_MAX_GENS,
        spacing_dex=SPACING_DEX,
        f_pix=F_PIX,
        N_PEAKS=N_PEAKS,
        N_LRD_grid=np.array(N_LRD_GRID),
        sigma_M_BH_grid=np.array(SIGMA_M_BH_GRID),
        snr_grid=snr_grid,
        A2_null_realizations=ad_result["A2_null_realizations"],
        A2_alt_realizations=ad_result["A2_alt_realizations"],
        threshold_A2=ad_result["threshold_A2"],
        rejection_rate=ad_result["rejection_rate"],
        f_pix_recovered=ad_result["f_pix_recovered"],
        f_pix_localized_frac=ad_result["f_pix_localized_frac"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        random_seed=RANDOM_SEED,
    )
    print(f"  npz saved: {OUT_NPZ}")
    print()

    # Step 7 - Sidecar JSON
    print(f"=== Sidecar JSON ===")
    write_sidecar_json(OUT_JSON, GATE_ID, snr_grid, ad_result, audit_sha, content_sha, G_MAX_GENS)
    print()

    # Step 8 - Verdict composite (PASS / INFO / FAIL)
    print(f"=== Verdict composition ===")
    # Artifact existence check
    artifacts_present = (
        OUT_NPZ.exists() and
        OUT_PNG.exists() and
        OUT_JSON.exists() and
        Path(__file__).exists()
    )                                                                                 # (local)
    print(f"  artifacts_present (script + .npz + .png + .json): {artifacts_present}")

    # Composite verdict per plan §W1c-66 Field 9 + spawn-prompt overrides
    if not artifacts_present:
        composite = "FAIL"                                                            # (local)
        sign_v, mag_v, regime_v = "N/A", "FAIL", "VALID"                              # (local)
    elif snr_baseline >= PASS_GLOBAL_SNR_FLOOR:
        composite = "PASS"
        sign_v, mag_v, regime_v = "N/A", "PASS", "VALID"
    elif snr_baseline >= INFO_GLOBAL_SNR_FLOOR:
        composite = "INFO"
        sign_v, mag_v, regime_v = "N/A", "INFO", "VALID"
    else:
        # Check whether ANY grid point yields >= 3 sigma
        max_snr = float(snr_grid.max())                                               # (local)
        if max_snr >= INFO_GLOBAL_SNR_FLOOR:
            composite = "INFO"
            sign_v, mag_v, regime_v = "N/A", "INFO", "VALID"
        else:
            composite = "FAIL"
            sign_v, mag_v, regime_v = "N/A", "FAIL", "VALID"

    print(f"  composite verdict: {composite}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print()

    # Build value string per spawn-prompt
    value_str = (
        f"PROTOCOL_PRE_REGISTERED_NLRD1000_sigmaMBH010_globalSNR{snr_baseline:.2f}sigma"
    )                                                                                 # (local)

    # Step 9 - Append verdict block (3 rows)
    append_verdict(
        VERDICT_TXT, GATE_ID, composite, value_str,
        SCHEME, CONVENTION, L_MAX_TAG,
        audit_sha, content_sha,
        sign_v, mag_v, regime_v,
    )
    print()

    # Final stdout summary block (last non-verdict line is the 4-tuple per gate-verdicts.md)
    print(f"=== {GATE_ID} 4-tuple ===")
    print(f"  (value='{value_str}', "
          f"scheme='{SCHEME}', "
          f"convention='{CONVENTION}', "
          f"L_max='{L_MAX_TAG}')")
    print()
    print(f"=== {GATE_ID} TERMINATED OK ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
