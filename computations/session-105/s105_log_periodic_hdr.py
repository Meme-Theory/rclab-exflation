#!/usr/bin/env python3
"""
S105 W5-1 — S105-W5-1-LOG-PERIODIC-HDR
======================================

Gate: S105-W5-1-LOG-PERIODIC-HDR ([SIGN])

Log-periodic HDR (higher-dynamic-range) re-scan of the heat-trace oscillatory
residual for a complex-dimension Im(s) line. This wave recomputes K(t) =
Tr e^{-t D_K^2} and the Strutinsky-split oscillatory residual K_osc(t) DIRECTLY
from the s84 L=12 fold spectrum (90 Peter-Weyl (p,q) sectors, 166,896 block
eigenvalues, ~32M with full PW multiplicity dim_SU3(p,q)) -- vs the S104 source,
which was the S61 on-disk residual (only 200 t-points over a 992-mode S61
spectrum). It then runs the IDENTICAL pinned S104 STAGE-B pipeline (e^{4u}
detrend, Hann window, 2048-pt uniform-u grid, 10x prominence floor,
interior-local-maximum guard, +-1-bin cross-axis stability over the
gamma/d x SDW-order family) at the higher dynamic range.

Every STAGE-B parameter is BYTE-FOR-BYTE the S104 pre-registration
(computations/session-104/s104_log_periodic_ims.py). The ONLY declared deltas
are (a) the source spectrum (s84 L=12 cache vs the S61 residual) and (b) the
native t-grid density (1024 vs 200). This makes the re-run structurally distinct
from iterate-until-PASS (PROHIBITED_ACTIONS Class 6) by construction: it is the
SAME pre-registered criterion applied to a higher-dynamic-range input, NOT a
re-tuning of the criterion to chase PASS.

Substrate-first prediction (substitution chain, plan §(7)):
  The Jensen deformation of SU(3) at tau_fold = 0.190 is NOT exactly self-similar,
  so the fabric's dimension spectrum carries no discrete-scale-invariance line.
  CM-1995 (PROVEN) establishes Sd = {0,2,4,6,8} subset R (simple, REAL) for
  (A_K, H_K, D_K) => no s with Im(s) != 0. Predicted verdict: FAIL (the CM-1995
  simple-real-dimension-spectrum wall re-confirmed on a frequency-domain axis at
  higher dynamic range; corridor-closing outcome). A PASS would FALSIFY the
  substrate-first prediction and FORCE a CM-1995 reconciliation.

STAGE A -- heat-trace + Strutinsky build (the DYNAMIC-RANGE UPGRADE):
  K(t) = sum_{(p,q)} dim_SU3(p,q) * sum_i exp(-t * |lambda_i|^2)   [PW-weighted regular-rep trace]
  K_SD smooth part, two orthogonal families:
    (i) SDW-order o in {2,3,4}: K~(t) = sum_{n in {0,..,2o}} a_n^{zeta} * t^{(n-8)/2}
        (zeta-regulated Seeley-DeWitt, d=8; a_n^{zeta} from canonical a_{0,2,4,6,8}_FW_zeta; CLASS=FULL)
    (ii) gamma/d in {1.0,1.5,2.0} (+ 3.0 diagnostic): Gaussian-Strutinsky-smoothed DOS
        Laplace transform (self-normalizing; IDENTICAL prescription to S61 Section 6)
  K_osc(t) = K(t) - K~(t).
  Cross-check: rebuilt R_osc = ||K_osc||/||K~|| reproduces the S61 sibling
  R_osc = 2.23e-5 to within an OOM (consistency anchor, NOT a PASS conjunct).

STAGE B -- detrend -> FFT -> prominence -> cross-axis stability (IDENTICAL TO S104):
  g(u) = K_osc(e^u) * e^{u*Re(s)*}, Re(s)* = 4 (poleconv-A, (pole_in_s=4, curvature_grade_n=0)),
  cubic-spline onto the 2048-pt uniform u-grid on [-ln100, +ln100], DC-remove,
  Hann-window, zero-pad to FFT_LEN=4096, rFFT, strongest INTERIOR local maximum
  strictly above omega_min (find_peaks; band-edge DC-shoulder guard), prominence =
  peak_power / median(broadband, +-2-bin excluded). PASS member iff line_found AND
  prominence >= 10x. Cross-axis stability: ALL 6 members (3 gamma/d + 3 SDW orders)
  have a peak AND agree on omega* within +-1 FFT bin.

Mellin pole convention (LOAD-BEARING; regulator-pin-discipline.md):
  poleconv-A double-power zeta_{D_K}(s) = sum m_k |lambda_k|^{-2s}, poles at s=(d-n)/2.
  At d=8, leading n=0 -> Re(s)* = (8-0)/2 = 4 = d/2.  regulator_pin = a_n^{zeta}.

frequency -> Im(s) map: a complex dimension s = Re(s)* + i*omega_s announces as
  cos(omega_s * ln t) in the residual (Hoffer-Lapidus 2508.09512); the FFT angular
  frequency w_fft = omega_s = Im(s) directly. Implied pair: s = 4 +- i*omega*.

Output 4-tuple:
  (value=<peak/stability summary>, scheme=FFT-LOG-DETRENDED-RESIDUAL-HDR,
   convention=poleconv-A-double-power-Re_s_4-curvature_grade_n_0, L_max=12)

Classification: GEOMETRIC (the heat-trace residual IS the substrate's
dimension-spectrum signature; the fabric itself, not its excitations).

DISCIPLINE
----------
- `from canonical_constants import *`
- CPU-cap-OMP8 (the 2048-pt FFT is trivial; the heat-trace exp-sum is a
  vectorized numpy broadcast, ~1.7e8 evals, chunked over sectors).
- SHA-256 of all inputs logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict emitted via emit_verdict knowledge-MCP tool (script PRINTS payload only).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap BEFORE numpy import (cpu-cap-OMP8 per math-scripts.md)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared"))
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit names for the SDW smooth part + tau anchor
    a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta, a_6_FW_zeta, a_8_FW_zeta, tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
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
# Section 3 -- Paths + pre-registration (ALL pins per plan §W5-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S105"                                                    # (local)
GATE_ID = "S105-W5-1-LOG-PERIODIC-HDR"                              # (local)
SCHEME = "FFT-LOG-DETRENDED-RESIDUAL-HDR"                           # (local)
CONVENTION = "poleconv-A-double-power-Re_s_4-curvature_grade_n_0"   # (local)
L_MAX = "12"                                                        # (local) s84 cache L=12

# ---- STAGE A: heat-trace + Strutinsky build (the DYNAMIC-RANGE UPGRADE) ----
N_T = 1024                    # native heat-trace t-grid points (DECLARED dynamic-range delta vs S61's 200)  # (local)
T_LO = 0.01                   # t-window IDENTICAL to S61/S104 (geometric) -> ω_min = π/ln(100) unchanged    # (local)
T_HI = 100.0                  # (local)
SDW_ORDERS = [2, 3, 4]        # SDW-subtraction-order family (IDENTICAL to S104); order o keeps a_n^ζ up to n=2o  # (local)
GAMMA_RATIOS = [1.0, 1.5, 2.0]    # γ/d Strutinsky-Gaussian smoother widths (IDENTICAL to S104 conjunction members)  # (local)
GAMMA_DIAG = 3.0              # 4th γ/d point, DIAGNOSTIC ONLY (NOT in the stability conjunction), IDENTICAL to S104  # (local)
R_OSC_ANCHOR = 2.23e-5        # S61 HK-OSCILLATION-61 sibling; rebuilt R_osc must agree to <=1 OOM (consistency, NOT PASS conjunct)  # (local)

# a_n^{zeta} Strutinsky smooth-part coefficients (CLASS=FULL physical zeta-regulated SDW; canonical pins)
A_N_ZETA = {0: a_0_FW_zeta, 2: a_2_FW_zeta, 4: a_4_FW_zeta, 6: a_6_FW_zeta, 8: a_8_FW_zeta}  # (local)
D_DIM = 8                     # SU(3) internal dimension (d=8); SDW powers t^{(n-d)/2}  # (local)

# ---- STAGE B: detrend -> FFT -> prominence -> cross-axis stability (IDENTICAL TO S104) ----
RE_S_DETREND = 4.0           # Re(s)* = (d-n)/2 = (8-0)/2 = 4 at d=8, n=0; poleconv-A  (IDENTICAL to S104)  # (local)
U_HALF_WIDTH = np.log(100.0)  # u = ln t window half-width; t in [0.01, 100]  (IDENTICAL to S104)            # (local)
N_U_GRID = 2048              # uniformly-spaced u-grid points (IDENTICAL to S104)                            # (local)
FFT_LEN = 4096               # zero-padded FFT length (IDENTICAL to S104)                                    # (local)
PROMINENCE_FLOOR = 10.0      # peak_power / median(broadband) >= 10 (IDENTICAL to S104)                      # (local)
BROADBAND_EXCLUDE_BINS = 2   # +-2-bin neighbourhood excluded from broadband median (IDENTICAL to S104)      # (local)
STABILITY_BIN_TOL = 1        # peak ω* stable within +-1 FFT bin across family (IDENTICAL to S104)            # (local)

# ω_min = 2π / (2 ln100) = analytic 2-cycle floor over the u-window (IDENTICAL to S104)
OMEGA_MIN = 2.0 * np.pi / (2.0 * U_HALF_WIDTH)                       # (local)  = π/ln(100) = 0.6821881769209206
F_MIN = OMEGA_MIN / (2.0 * np.pi)                                    # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s105_log_periodic_hdr.npz"                 # (local)
OUT_PNG = SESSION_DIR / "s105_log_periodic_hdr.png"                 # (local)

S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"   # (local) HDR source
S61_NPZ = COMPUTATIONS_DIR / "session-61" / "s61_hk_oscillation.npz"                # (local) cross-check overlap
S104_PIPELINE = COMPUTATIONS_DIR / "session-104" / "s104_log_periodic_ims.py"       # (local) pinned STAGE-B reference

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S84_CACHE,
    S104_PIPELINE,
    S61_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
# Section 5A -- STAGE A: PW-weighted heat trace + Strutinsky split (HDR build)
# ---------------------------------------------------------------------------

def dim_su3(p: int, q: int) -> int:
    """dim_SU3(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def build_heat_trace(sector_evals: dict, t_arr: np.ndarray):
    """PW-weighted regular-representation heat trace
    K(t) = sum_{(p,q)} dim_SU3(p,q) * sum_i exp(-t * |lambda_i|^2)
    over the s84 L=12 cache. Chunked over sectors (each sector is a vectorized
    exp-sum); transient never exceeds one sector's (n_block x N_T) matrix.
    Returns K(t), plus the flat (lambda^2, weight) mode list for the
    Gaussian-Strutinsky DOS smoother.
    """
    K = np.zeros(t_arr.size, dtype=np.float64)  # (local)
    lam2_list = []  # (local) per-block lambda^2 values
    w_list = []     # (local) per-block PW multiplicity weight (= dim_SU3(p,q))
    n_block_total = 0  # (local)
    pw_total = 0       # (local)
    for (p, q), entry in sector_evals.items():
        dim_pq = int(entry["dim"])              # (local) dim_SU3(p,q) from inner 'dim' field
        # sanity: the inner 'dim' must equal the closed-form dim_SU3
        assert dim_pq == dim_su3(p, q), f"dim mismatch sector ({p},{q}): {dim_pq} != {dim_su3(p,q)}"
        abs_evals = np.asarray(entry["abs_evals"], dtype=np.float64)  # (local) |lambda_i|, size dim*16
        lam2 = abs_evals ** 2  # (local)
        # vectorized exp-sum for this sector, weighted by PW multiplicity dim_pq
        # K += dim_pq * sum_i exp(-t * lam2_i)
        # exp(-outer(lam2, t)) is (n_block, N_T); sum over modes axis 0
        contrib = dim_pq * np.exp(-np.outer(lam2, t_arr)).sum(axis=0)  # (local)
        K += contrib
        lam2_list.append(lam2)
        w_list.append(np.full(lam2.size, float(dim_pq)))
        n_block_total += lam2.size
        pw_total += dim_pq * lam2.size
    lam2_all = np.concatenate(lam2_list)  # (local) all 166,896 block lambda^2
    w_all = np.concatenate(w_list)        # (local) matching PW weights
    return K, lam2_all, w_all, n_block_total, pw_total


def build_SDW_smooth(t_arr: np.ndarray, order: int) -> np.ndarray:
    """Zeta-regulated Seeley-DeWitt smooth part (CLASS=FULL):
    K~(t) = sum_{n in {0,2,...,2*order}} a_n^{zeta} * t^{(n-d)/2}, d=8.
    Order o keeps a_n^zeta up to n=2o. n=0 -> t^{-4}, n=2 -> t^{-3}, ...,
    n=8 -> t^{0}. This is the canonical small-t Weyl asymptotic form; the
    a_n^{zeta} are the canonical per-branch L_max=3 spectral moments
    (a_{0,2,4,6,8}_FW_zeta). poleconv-A: pole_in_s=(d-n)/2, curvature_grade_n=n.
    """
    Kt = np.zeros(t_arr.size, dtype=np.float64)  # (local)
    n_max = 2 * order  # (local) order 2 -> n up to 4 ; order 3 -> 6 ; order 4 -> 8
    for n in range(0, n_max + 1, 2):
        if n not in A_N_ZETA:
            continue
        Kt += A_N_ZETA[n] * t_arr ** ((n - D_DIM) / 2.0)
    return Kt


def build_gaussian_strutinsky_smooth(lam2_all: np.ndarray, w_all: np.ndarray,
                                     t_arr: np.ndarray, gamma_ratio: float) -> np.ndarray:
    """Gaussian-Strutinsky-smoothed DOS Laplace transform (self-normalizing;
    IDENTICAL prescription to S61 Section 6 -- the smooth part is the broadened
    level density transformed back to the heat-trace domain). gamma = gamma_ratio
    * mean level spacing in lambda^2; the smoothed density rho_smooth(E) is the
    Gaussian-broadened sum of weighted deltas at E = lambda^2; then
    K_smooth(t) = integral rho_smooth(E) * exp(-E*t) dE.
    """
    # Unique lambda^2 values with summed PW weights (DOS support points)
    E_unique, inv = np.unique(lam2_all, return_inverse=True)  # (local)
    w_unique = np.zeros(E_unique.size, dtype=np.float64)       # (local)
    np.add.at(w_unique, inv, w_all)                            # (local) sum PW weights per unique E
    # mean level spacing in lambda^2 space (over the unique support)
    if E_unique.size > 1:
        mean_spacing = float(np.mean(np.diff(np.sort(E_unique))))  # (local)
    else:
        mean_spacing = 1.0  # (local)
    gamma = gamma_ratio * mean_spacing  # (local)
    # E-grid: span the support +- 5 gamma (IDENTICAL to S61)
    E_min = max(0.0, E_unique.min() - 5.0 * gamma)  # (local)
    E_max = E_unique.max() + 5.0 * gamma            # (local)
    N_E = 4000  # (local) E-grid resolution (S61 used 2000 over 992 modes; HDR doubles for the larger support)
    E_grid = np.linspace(E_min, E_max, N_E)  # (local)
    dE = E_grid[1] - E_grid[0]               # (local)
    # smoothed density rho_smooth(E) = sum_j w_j * Gaussian(E - E_j; gamma)
    # vectorized over the unique support (chunk to bound transient memory)
    rho_smooth = np.zeros(N_E, dtype=np.float64)  # (local)
    norm = 1.0 / (np.sqrt(2.0 * np.pi) * gamma)   # (local)
    CHUNK = 4096  # (local)
    for j0 in range(0, E_unique.size, CHUNK):
        Ej = E_unique[j0:j0 + CHUNK][:, None]      # (local) (chunk,1)
        wj = w_unique[j0:j0 + CHUNK][:, None]      # (local)
        rho_smooth += (wj * np.exp(-(E_grid[None, :] - Ej) ** 2 / (2.0 * gamma ** 2))).sum(axis=0)
    rho_smooth *= norm
    # K_smooth(t) = integral rho_smooth(E) exp(-E t) dE
    K_smooth = (rho_smooth[None, :] * np.exp(-np.outer(t_arr, E_grid))).sum(axis=1) * dE  # (local)
    return K_smooth


# ---------------------------------------------------------------------------
# Section 5B -- STAGE B: log-detrend -> FFT -> prominence (BYTE-FOR-BYTE S104)
# ---------------------------------------------------------------------------

def log_detrend_and_fft(t_arr: np.ndarray, k_osc: np.ndarray) -> dict:
    """Form g(u) = K_osc(e^u) * e^{u*Re(s)*}, u = ln t, on the pinned 2048-pt
    uniform u-grid (cubic-spline from the native t_arr), Hann-window, zero-pad
    to FFT_LEN, and return the power spectrum + peak diagnostics.

    [IDENTICAL TO S104 s104_log_periodic_ims.py log_detrend_and_fft]
    The frequency axis is returned as ANGULAR omega (rad per ln-t unit), so
    Im(s) = omega* directly.  The ordinary f* = omega*/(2*pi) is also reported.
    """
    u_native = np.log(t_arr)  # (local) native u = ln t (geometric grid on disk)

    # Pinned uniform u-grid on [-ln100, +ln100]. The native t_arr spans exactly
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
    # 10x-prominence floor. We identify the candidate peak as the strongest INTERIOR
    # local maximum strictly above omega_min (find_peaks excludes band endpoints by
    # construction). It is forced AGAINST the PASS direction (it can only reject a
    # DC-shoulder artifact, never manufacture a line) -- NOT criterion-shopping.
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


# ---------------------------------------------------------------------------
# Section 5C -- driver: assemble family + cross-axis stability (S104 verdict logic)
# ---------------------------------------------------------------------------

def compute() -> dict:
    # ---- STAGE A: load s84 cache + build PW-weighted heat trace ----
    d = np.load(S84_CACHE, allow_pickle=True)  # (local)
    sector_evals = d["sector_evals"].item()    # (local) dict (p,q) -> {'dim','level','abs_evals'}
    t_arr = np.geomspace(T_LO, T_HI, N_T)      # (local) native geometric t-grid (1024 pts)

    K_exact, lam2_all, w_all, n_block, pw_total = build_heat_trace(sector_evals, t_arr)  # (local)

    # ---- Build the residual family: SDW-subtraction-order AND gamma/d Gaussian-Strutinsky ----
    family: dict[str, np.ndarray] = {}  # (local) member -> K_osc residual on native t_arr
    axis_of: dict[str, str] = {}        # (local)
    smooth_of: dict[str, np.ndarray] = {}  # (local) member -> K~ smooth part (for R_osc + plot)

    # SDW-order residuals: K_exact - K_SD_order{2,3,4} (the a_n^{zeta} smooth axis)
    for o in SDW_ORDERS:
        key = f"sdw_{o}"  # (local)
        Ksd = build_SDW_smooth(t_arr, o)  # (local)
        family[key] = K_exact - Ksd
        smooth_of[key] = Ksd
        axis_of[key] = "sdw_order"

    # gamma/d Gaussian-Strutinsky-smoothed shell residuals (the self-normalizing axis)
    for gd in GAMMA_RATIOS:
        key = f"gd_{gd:.1f}"  # (local)
        Ksm = build_gaussian_strutinsky_smooth(lam2_all, w_all, t_arr, gd)  # (local)
        family[key] = K_exact - Ksm
        smooth_of[key] = Ksm
        axis_of[key] = "gamma_d"

    # Diagnostic-only 4th gamma/d point (NOT part of the stability conjunction)
    diag_key = f"gd_diag_{GAMMA_DIAG:.1f}"  # (local)
    Ksm_diag = build_gaussian_strutinsky_smooth(lam2_all, w_all, t_arr, GAMMA_DIAG)  # (local)
    family_diag = K_exact - Ksm_diag  # (local)
    smooth_of[diag_key] = Ksm_diag

    # ---- R_osc consistency cross-check (NOT a PASS conjunct) ----
    # Match the S61 definition: R_osc = |K_osc(t=1)/K_exact(t=1)| at gamma/d=1.5.
    idx_t1 = int(np.argmin(np.abs(t_arr - 1.0)))  # (local)
    K_osc_gd15 = family["gd_1.5"]  # (local)
    R_osc_rebuilt = abs(K_osc_gd15[idx_t1] / K_exact[idx_t1]) if K_exact[idx_t1] != 0 else np.inf  # (local)
    # OOM agreement vs the S61 sibling (consistency anchor)
    if R_osc_rebuilt > 0 and np.isfinite(R_osc_rebuilt):
        oom_diff = abs(np.log10(R_osc_rebuilt) - np.log10(R_OSC_ANCHOR))  # (local)
    else:
        oom_diff = np.inf  # (local)
    r_osc_consistent = bool(oom_diff <= 1.0)  # (local) <=1 OOM agreement

    # ---- FFT each family member (STAGE B; IDENTICAL S104 pipeline) ----
    results: dict[str, dict] = {}  # (local)
    for key, k_osc in family.items():
        results[key] = log_detrend_and_fft(t_arr, k_osc)
    results[diag_key] = log_detrend_and_fft(t_arr, family_diag)

    # ---- Conjunction members: gamma/d in {1.0,1.5,2.0} AND SDW order in {2,3,4} ----
    conj_keys = list(family.keys())  # (local) all 6 members (3 gamma/d + 3 orders)

    # Per-member: GENUINE LINE (interior local max) above the 10x floor?
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

    # ---- Cross-axis stability: ALL conjunction members (a) have a peak above floor
    #      AND (b) agree on omega* within +-1 FFT bin. (IDENTICAL S104) ----
    all_have_peak = all(member_has_peak.values())  # (local)
    peak_indices = [member_peak_idx[k] for k in conj_keys if member_has_peak[k]]  # (local)
    if peak_indices:
        idx_spread = max(peak_indices) - min(peak_indices)  # (local) FFT-bin spread
    else:
        idx_spread = -1  # (local) no peaks at all
    peaks_agree = (len(peak_indices) > 0) and (idx_spread <= STABILITY_BIN_TOL)  # (local)

    cross_axis_peak_stable = bool(all_have_peak and peaks_agree)  # (local)

    # ---- Median omega* across members that have a peak (implied complex dim) ----
    if peak_indices:
        omegas_with_peak = [member_peak_omega[k] for k in conj_keys if member_has_peak[k]]  # (local)
        median_peak_omega = float(np.median(omegas_with_peak))  # (local)
    else:
        strongest = max(conj_keys, key=lambda k: member_prom[k])  # (local)
        median_peak_omega = float(member_peak_omega[strongest])  # (local)

    implied_complex_dim_re = RE_S_DETREND  # (local)
    implied_complex_dim_im = median_peak_omega if cross_axis_peak_stable else 0.0  # (local)

    # ---- Verdict logic (PINNED; IDENTICAL S104; no runtime criterion shopping) ----
    if cross_axis_peak_stable:
        verdict = "PASS"  # (local)
    elif n_with_peak == 0:
        verdict = "FAIL"  # (local)
    else:
        verdict = "INFO"  # (local)

    # ---- [SIGN] 3-tuple (IDENTICAL S104 mapping) ----
    # sign_verdict reports the wall-confirmation prediction (predicted no-peak):
    #   FAIL verdict (no peak): direction matches prediction -> sign PASS.
    #   PASS verdict (stable peak): direction OPPOSITE prediction -> sign FAIL.
    #   INFO verdict (unstable peak): direction ambiguous (scheme-dependent) -> sign N/A.
    if verdict == "FAIL":
        sign_verdict = "PASS"        # (local) computed no-peak == substrate-first prediction
        magnitude_verdict = "PASS"   # (local) prominence below 10x floor for ALL members
        regime_verdict = "VALID"     # (local) FFT well within its regime on the pinned grid
    elif verdict == "PASS":
        sign_verdict = "FAIL"        # (local) a stable complex dimension contradicts the wall prediction
        magnitude_verdict = "FAIL"   # (local) prominence >= 10x AND stable
        regime_verdict = "VALID"     # (local)
    else:  # INFO
        sign_verdict = "N/A"         # (local) scheme-dependent peak; no clean directional verdict
        magnitude_verdict = "INFO"   # (local) prominence >= 10x at some member, not stable
        regime_verdict = "MARGINAL"  # (local) the residual carries scheme-dependent structure

    # ---- Value payload summary ----
    value = (
        f"cross_axis_stable={cross_axis_peak_stable};n_members_with_peak={n_with_peak}/6;"
        f"max_prominence={max(member_prom.values()):.4g};"
        f"strongest_omega={median_peak_omega:.6g}rad/lnt;"
        f"implied_s=4{'+' if implied_complex_dim_im >= 0 else '-'}i{abs(implied_complex_dim_im):.6g};"
        f"omega_min={OMEGA_MIN:.6g};R_osc_rebuilt={R_osc_rebuilt:.4g};"
        f"R_osc_sibling={R_OSC_ANCHOR:.4g};R_osc_consistent={r_osc_consistent};"
        f"n_block={n_block};pw_modes={pw_total}"
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
        "smooth_of": smooth_of,
        "K_exact": K_exact,
        "t_arr": t_arr,
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
        "R_osc_rebuilt": float(R_osc_rebuilt),
        "R_osc_anchor": R_OSC_ANCHOR,
        "r_osc_oom_diff": float(oom_diff),
        "r_osc_consistent": r_osc_consistent,
        "n_block": n_block,
        "pw_total": pw_total,
    }


# ---------------------------------------------------------------------------
# Section 6 -- Plot + NPZ
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
        bm = r["broadband_median"] if r["broadband_median"] > 0 else 1.0  # (local)
        ax.plot(r["omega_axis"], r["power_spectrum"] / bm, color=c, lw=1.1,
                label=f"{k} (prom={r['peak_prominence_ratio']:.2g}, line={r['line_found']})")
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
        f"S105-W5-1-LOG-PERIODIC-HDR -- log-detrended residual power spectra (poleconv-A, Re(s)*=4)\n"
        f"HDR source: s84 L=12 ({res['n_block']} block / {res['pw_total']} PW)  "
        f"verdict={res['verdict']}  cross_axis_stable={res['cross_axis_peak_stable']}  "
        f"n_with_peak={res['n_with_peak']}/6")
    ax.legend(fontsize=6.0, ncol=2, loc="upper right")
    ax.grid(alpha=0.25)

    # ---- (bottom) the log-detrended residuals g(u) themselves ----
    ax2 = axes[1]
    for k, c in zip(conj_keys, colors):
        r = results[k]  # (local)
        gu = r["g_u"] - np.mean(r["g_u"])  # (local) DC-removed, as FFT sees it
        ax2.plot(r["u_grid"], gu, color=c, lw=1.0, label=k)
    ax2.set_xlabel("u = ln t")
    ax2.set_ylabel("g(u) = K_osc(e^u)*e^{4u}  (DC-removed)")
    ax2.set_title("Log-detrended oscillatory residual g(u) over u = ln t (a stationary cosine => a complex dimension)")
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

    for k in conj_keys + [diag_key]:
        r = results[k]  # (local)
        out[f"u_grid__{k}"] = r["u_grid"]
        out[f"g_u__{k}"] = r["g_u"]
        out[f"power_spectrum__{k}"] = r["power_spectrum"]
        out[f"omega_axis__{k}"] = r["omega_axis"]
        out[f"peak_omega__{k}"] = np.array(r["peak_omega"])
        out[f"peak_prominence_ratio__{k}"] = np.array(r["peak_prominence_ratio"])
        out[f"broadband_median__{k}"] = np.array(r["broadband_median"])
        out[f"line_found__{k}"] = np.array(r["line_found"])

    out["u_grid"] = results[conj_keys[0]]["u_grid"]
    out["omega_axis"] = results[conj_keys[0]]["omega_axis"]
    out["g_u"] = results[conj_keys[0]]["g_u"]
    out["power_spectrum"] = results[conj_keys[0]]["power_spectrum"]
    out["peak_omega"] = np.array(res["median_peak_omega"])
    out["peak_prominence_ratio"] = np.array(max(res["member_prom"].values()))
    out["broadband_median"] = np.array(results[conj_keys[0]]["broadband_median"])

    out["t_arr"] = res["t_arr"]
    out["K_exact"] = res["K_exact"]
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
    out["R_osc_rebuilt"] = np.array(res["R_osc_rebuilt"])
    out["R_osc_anchor"] = np.array(res["R_osc_anchor"])
    out["R_osc_oom_diff"] = np.array(res["r_osc_oom_diff"])
    out["R_osc_consistent"] = np.array(res["r_osc_consistent"])
    out["n_block_eigenvalues"] = np.array(res["n_block"])
    out["pw_weighted_modes"] = np.array(res["pw_total"])
    out["Re_s_detrend"] = np.array(RE_S_DETREND)
    out["N_T"] = np.array(N_T)
    out["verdict"] = np.array(res["verdict"])
    out["sign_verdict"] = np.array(res["sign_verdict"])
    out["magnitude_verdict"] = np.array(res["magnitude_verdict"])
    out["regime_verdict"] = np.array(res["regime_verdict"])
    # a_n^{zeta} pins used in the SDW smooth part (audit trail)
    out["a_n_zeta_used"] = np.array([A_N_ZETA[0], A_N_ZETA[2], A_N_ZETA[4], A_N_ZETA[6], A_N_ZETA[8]])

    np.savez(OUT_NPZ, **out)


# ---------------------------------------------------------------------------
# Section 7 -- Verdict payload + 4-tuple
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, l_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={l_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": "105",
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
# Section 8 -- Main
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

    print(f"  STAGE A (HDR source): s84 L=12 cache, tau_fold={tau_fold}, N_T={N_T} geometric on [{T_LO},{T_HI}]")
    print(f"  a_n^zeta SDW pins: a0={A_N_ZETA[0]:.6g} a2={A_N_ZETA[2]:.6g} a4={A_N_ZETA[4]:.6g} "
          f"a6={A_N_ZETA[6]:.6g} a8={A_N_ZETA[8]:.6g}")
    print(f"  Re(s)* detrend exponent = {RE_S_DETREND}  (poleconv-A: (d-n)/2=(8-0)/2=4, n=0 curvature grade)")
    print(f"  omega_min = 2*pi/(2*ln100) = {OMEGA_MIN:.15g} rad/ln-unit  (f_min = {F_MIN:.15g} cyc/ln-unit)")
    print(f"  prominence floor = {PROMINENCE_FLOOR}x median broadband; stability tol = +-{STABILITY_BIN_TOL} FFT bin")
    print(f"  u-grid: {N_U_GRID} pts on [-ln100, +ln100]; FFT length {FFT_LEN} (zero-padded); Hann window")
    print()

    res = compute()  # (local)

    print(f"=== {GATE_ID} -- STAGE A heat-trace summary ===")
    print(f"  block eigenvalues   = {res['n_block']}")
    print(f"  PW-weighted modes   = {res['pw_total']}")
    print(f"  K(t_min={res['t_arr'][0]:.4f}) = {res['K_exact'][0]:.6g}  "
          f"K(t=1) = {res['K_exact'][int(np.argmin(np.abs(res['t_arr']-1.0)))]:.6g}  "
          f"K(t_max={res['t_arr'][-1]:.2f}) = {res['K_exact'][-1]:.6g}")
    print(f"  R_osc rebuilt (gd=1.5, t=1) = {res['R_osc_rebuilt']:.6g}  "
          f"vs S61 sibling {res['R_osc_anchor']:.6g}  "
          f"(|dOOM|={res['r_osc_oom_diff']:.3g}, consistent<=1OOM: {res['r_osc_consistent']})")
    print()

    print(f"=== {GATE_ID} -- per-member peak diagnostics (omega > omega_min) ===")
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
        f"# regulator_pin=a_n^{{zeta}} mellin_pole=(pole_in_s=4,curvature_grade_n=0) poleconv-A-double-power CLASS=FULL",
        f"# HDR_source=s84_L12 n_block={res['n_block']} pw_modes={res['pw_total']} N_T={N_T} (vs S104 S61-residual 992-mode/200-t)",
        f"# R_osc_rebuilt={res['R_osc_rebuilt']:.6g} R_osc_sibling={res['R_osc_anchor']:.6g} consistent_le1OOM={res['r_osc_consistent']}",
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
