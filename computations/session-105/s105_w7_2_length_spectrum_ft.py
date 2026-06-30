#!/usr/bin/env python3
"""
S105 W7-2 — S105-W7-2-LENGTH-SPECTRUM-FT — first measured length spectrum of the
Jensen-deformed substrate
==============================================================================

Gate: S105-W7-2-LENGTH-SPECTRUM-FT ([VERIFY])

Pre-registered threshold (plan §W7-2, strict_PASS_boundary):
  PASS iff n_stable_peaks >= 3 (each SNR >= 6.0 above the smooth-subtraction
          residual floor AND window-halving position drift <= delta_L)
          AND the tau=0 control peaks land on the W7-1 coroot lattice within delta_L.
  FAIL iff the tau=0 synthetic control FAILS (its peaks do NOT land on the W7-1
          coroot lattice within delta_L) -> pipeline defect.
  INFO iff fewer than 3 stable peaks at tau_fold while the tau=0 control still
          validates (resolution-limited by the L_max=12 cache ceiling).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (READ-ONLY)
  - computations/_shared/canonical_constants.py                 (feeds audit_sha256)
  - script bytes                                                (feeds BOTH SHAs)

Output 4-tuple:
  (value=<n_stable_peaks + control verdict>, scheme=STRUTINSKY-WEYL-SUBTRACT,
   convention=PW-dim-weighted-PRIMARY, L_max=12)

Classification: GEOMETRIC.

METHODOLOGY
-----------
The substrate IS the eigenvalue density rho(lambda) of D_K at tau_fold=0.190 (a
Level-1 single-tau-slice observable). The oscillatory residual rho_osc(lambda),
after the smooth Weyl/Seeley-Dewitt part is removed, IS the spectral fingerprint
of the fabric's closed internal relay orbits: by Poisson summation / wave-trace,
the oscillation at conjugate length L_gamma = 2*pi*(FFT freq in lambda) is sourced
by a periodic geodesic of length L_gamma on the Jensen-deformed internal geometry.
The length spectrum is the geometric side of the substrate's own trace formula.
The arrow is D_K eigenvalues -> oscillatory density -> FT -> closed-geodesic length
spectrum; the lengths are READ OUT of the spectrum, never imposed.

COUNTING-CHOICE PIN (load-bearing; plan substitution_chain):
  PRIMARY  = Peter-Weyl dim-weighted (each block eigenvalue weighted by an extra
             dim(p,q): the regular-representation multiplicity in L^2(SU(3))).
             Weyl exponent ~8 (the d=8 dimension-spectrum reading); its Poisson
             dual is the coroot lattice (matching W7-1). PASS basis.
  DIAGNOSTIC = block-level (each sector's 16*dim eigenvalues counted once).
             Weyl exponent ~5 (per-sector reading). Reported, NOT the PASS basis.

REGULATOR PIN: a_n^{zeta} (the smooth Seeley-Dewitt part cites a_0_FW_zeta..
  a_8_FW_zeta, zeta-regulated; MANDATORY per regulator-pin-discipline.md). The
  in-script Weyl polynomial fit over the pinned 20th-70th percentile quantile band
  is the operative smooth-staircase estimator (the a_n^{zeta} moments are per-branch
  L_max=3 zeta moments, cited as the regulator-class anchor, NOT a clean L=12
  staircase); the smooth subtraction is the zeta-regulated Weyl part by this pin.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- torch.fft for the FFT (GPU path); numpy for cache I/O; scipy for peak-find + smoothing
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the emit_verdict knowledge-MCP tool (race-safe): the
  script PRINTS the payload (print_verdict_payload); the AGENT calls emit_verdict.
  The script does NOT write s105_gate_verdicts.txt directly.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403,E402
# Explicit names used (documents the regulator pin a_n^{zeta} consumption):
from canonical_constants import (
    tau_fold,
    a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta, a_6_FW_zeta, a_8_FW_zeta,
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
from scipy.ndimage import gaussian_filter1d
from scipy.signal import find_peaks

try:
    import torch
    _HAVE_TORCH = True  # (local)
except Exception:  # pragma: no cover
    _HAVE_TORCH = False  # (local)

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

SESSION = "S105"                                    # (local)
GATE_ID = "S105-W7-2-LENGTH-SPECTRUM-FT"            # (local)
SCHEME = "STRUTINSKY-WEYL-SUBTRACT"                 # (local)
CONVENTION = "PW-dim-weighted-PRIMARY"              # (local)
L_MAX = 12                                          # (local)

# Pre-registered machinery pins (plan §W7-2 machinery_pin_map)
SNR_FLOOR = 6.0                                     # (local) SNR floor (plan tolerance)
N_STABLE_PEAKS_PASS = 3                             # (local) >=3 stable peaks => PASS basis
QUANTILE_LO = 20.0                                  # (local) smooth-fit quantile band lo (pct)
QUANTILE_HI = 70.0                                  # (local) smooth-fit quantile band hi (pct)
N_FFT_GRID = 2048                                   # (local) FFT grid points (plan step_size)
WEYL_POLY_DEG = 10                                  # (local) Weyl smooth polynomial degree
GAUSS_WIDTH_FACTOR = 3.0                            # (local) Gaussian window = 3x mean level spacing
GAUSS_WIDTH_FACTOR_HALF = 1.5                       # (local) window-halving cross-check (1.5x)
C_OFF_TAU0 = 0.75                                   # (local) tau=0 bi-invariant Dirac-square floor |lambda|^2(0,0)=0.75 (W7-1 explore: R_scalar/8 spin-connection const; spread 1.7e-15 EXACT)
P_MAX_CONTROL = 60                                  # (local) tau=0 control irrep truncation (exp(-decay) negligible)

# Output destinations
OUT_NPZ = SESSION_DIR / "s105_w7_2_length_spectrum_ft.npz"
OUT_PNG = SESSION_DIR / "s105_w7_2_length_spectrum_ft.png"

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block
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
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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
# Section 5 — Group-theory helpers (SU(3))
# ---------------------------------------------------------------------------
def casimir_pq(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C2(p,q) = (p^2+q^2+pq+3p+3q)/3 (canonical normalization)."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def dim_pq(p: int, q: int) -> int:
    """SU(3) irrep dimension dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# ---------------------------------------------------------------------------
# Section 6 — Length-spectrum FT pipeline (the load-bearing transform)
# ---------------------------------------------------------------------------
def build_density(lams: np.ndarray, weights: np.ndarray, n_grid: int):
    """Histogram the weighted eigenvalue list onto a uniform lambda-grid.

    Returns (grid, rho_raw, d_lambda). rho_raw is the weighted count per bin
    (the substrate's spectral density, mode-counted with the chosen multiplicity).
    """
    lo, hi = float(lams.min()), float(lams.max())  # (local)
    grid = np.linspace(lo, hi, n_grid)  # (local)
    dl = grid[1] - grid[0]  # (local)
    idx = np.clip(((lams - lo) / dl).astype(np.int64), 0, n_grid - 1)  # (local)
    rho = np.zeros(n_grid, dtype=np.float64)  # (local)
    np.add.at(rho, idx, weights)
    return grid, rho, dl


def strutinsky_weyl_subtract(grid, rho_raw, lams, gauss_factor, poly_deg,
                             q_lo, q_hi):
    """Strutinsky smoothing + Weyl-polynomial smooth subtraction.

    (1) Gaussian-smooth the raw density with width = gauss_factor x mean level
        spacing in the quantile band (the Strutinsky gamma convention).
    (2) Fit a Weyl polynomial (zeta-regulated smooth staircase derivative,
        regulator pin a_n^{zeta}) of degree poly_deg over the interior quantile
        band [q_lo, q_hi]-percentile of lambda.
    (3) Oscillatory residual = smoothed density - Weyl polynomial.

    Returns (rho_smoothed, rho_weyl, rho_osc, sigma_lambda, band_mask).

    STRUTINSKY-WIDTH ANCHORING: the dense L=12 spectrum has unique-level spacing
    (~2.6e-5) far below the grid resolution dl (~2.2e-3) and below float precision
    (many degenerate eigenvalues). The raw "mean level spacing" therefore gives a
    degenerate (sub-bin) window. The operative Strutinsky width for a BINNED density
    is anchored to the GRID resolution: sigma_lambda = gauss_factor * dl_grid (a few
    grid bins). This smooths bin-noise into a continuous density while preserving the
    geodesic-length oscillations (period in lambda = 2*pi/L ~ 0.63 for L~O(10),
    spanning ~280 bins >> sigma). The gauss_factor (3x for full, 1.5x for the
    window-halving cross-check) then genuinely varies the smoothing width, making the
    cross-check non-vacuous. We also report the raw-spacing-based width for the record.
    """
    s = np.sort(lams)  # (local)
    l1, l2 = np.percentile(s, [q_lo, q_hi])  # (local)
    band = (s >= l1) & (s <= l2)  # (local)
    uniq = np.unique(s[band])  # (local)
    raw_mean_spacing = float(np.mean(np.diff(uniq))) if uniq.size > 1 else (l2 - l1) / max(uniq.size, 1)  # (local)
    dl = grid[1] - grid[0]  # (local)
    # Strutinsky width anchored to grid resolution (a few bins); never sub-bin-degenerate.
    sigma_lambda = gauss_factor * dl  # (local)
    sigma_pts = max(sigma_lambda / dl, 1.0)  # (local) = gauss_factor bins
    rho_smoothed = gaussian_filter1d(rho_raw, sigma_pts, mode="nearest")  # (local)
    # Weyl polynomial fit over the interior quantile band of the GRID.
    # Normalize the abscissa to [-1,1] for conditioning (poorly-conditioned otherwise).
    band_mask = (grid >= l1) & (grid <= l2)  # (local)
    g0, g1 = grid[band_mask].min(), grid[band_mask].max()  # (local)
    xs = (2.0 * (grid - g0) / (g1 - g0)) - 1.0  # (local) normalized abscissa
    coef = np.polyfit(xs[band_mask], rho_smoothed[band_mask], poly_deg)  # (local)
    rho_weyl = np.polyval(coef, xs)  # (local)
    rho_osc = rho_smoothed - rho_weyl  # (local)
    # zero the oscillatory residual OUTSIDE the band (the fit is only valid there)
    rho_osc = np.where(band_mask, rho_osc, 0.0)  # (local)
    return rho_smoothed, rho_weyl, rho_osc, sigma_lambda, band_mask


def length_fft(grid, rho_osc, dl):
    """Gaussian-windowed FFT of the oscillatory residual in lambda.

    Geometric-side length: L_gamma = 2*pi*(FFT frequency in lambda).
    Uses torch.fft (GPU) when available; numpy.fft otherwise.

    Returns (L_axis, amp) for the positive-frequency half-spectrum.
    """
    n = grid.size  # (local)
    # apply a Hann taper on top of the band-limited residual to suppress edge ringing
    win = np.hanning(n)  # (local)
    sig = rho_osc * win  # (local)
    if _HAVE_TORCH:
        t = torch.tensor(sig, dtype=torch.float64)  # (local)
        ft = torch.fft.rfft(t).abs().cpu().numpy()  # (local)
    else:
        ft = np.abs(np.fft.rfft(sig))  # (local)
    freq = np.fft.rfftfreq(n, d=dl)  # (local) cycles per unit lambda
    L_axis = 2.0 * np.pi * freq  # (local) conjugate length
    return L_axis, ft


def extract_peaks(L_axis, amp, snr_floor, L_min_phys):
    """Find peaks with SNR >= snr_floor above the median-absolute-deviation floor.

    SNR is amplitude / robust-noise-floor (1.4826*MAD of the amplitude spectrum,
    excluding the DC/near-DC bins below L_min_phys).
    Returns a structured list [(L, amp, snr), ...] sorted by amplitude desc.
    """
    valid = L_axis >= L_min_phys  # (local) drop DC + sub-resolution lengths
    amp_v = amp.copy()  # (local)
    amp_v[~valid] = 0.0
    # robust noise floor from the valid amplitude spectrum
    med = np.median(amp[valid])  # (local)
    mad = np.median(np.abs(amp[valid] - med))  # (local)
    noise = 1.4826 * mad if mad > 0 else (np.std(amp[valid]) or 1.0)  # (local)
    height = snr_floor * noise  # (local)
    # require peaks separated by at least delta_L in L (one FFT bin in L is L_axis[1])
    dL_bin = L_axis[1] - L_axis[0] if L_axis.size > 1 else 1.0  # (local)
    distance = max(int(round((2.0 * np.pi / 5.5) / dL_bin)), 1)  # (local) ~delta_L spacing
    pk, _ = find_peaks(amp_v, height=height, distance=distance)  # (local)
    out = []  # (local)
    for i in pk:
        out.append((float(L_axis[i]), float(amp[i]), float(amp[i] / noise)))
    out.sort(key=lambda r: r[1], reverse=True)
    return out, float(noise), float(height)


def run_pipeline(lams, weights, n_grid, gauss_factor, poly_deg, q_lo, q_hi,
                 snr_floor):
    """Full pipeline: density -> Strutinsky-Weyl subtract -> windowed FFT -> peaks."""
    grid, rho_raw, dl = build_density(lams, weights, n_grid)
    rho_sm, rho_weyl, rho_osc, sigma_lambda, band_mask = strutinsky_weyl_subtract(
        grid, rho_raw, lams, gauss_factor, poly_deg, q_lo, q_hi
    )
    L_axis, amp = length_fft(grid, rho_osc, dl)
    lam_max = float(lams.max())  # (local)
    delta_L = 2.0 * np.pi / lam_max  # (local) resolution budget
    L_min_phys = delta_L  # (local) ignore lengths below one resolution element
    peaks, noise, height = extract_peaks(L_axis, amp, snr_floor, L_min_phys)
    return {
        "grid": grid, "rho_raw": rho_raw, "rho_smoothed": rho_sm,
        "rho_weyl": rho_weyl, "rho_osc": rho_osc, "sigma_lambda": sigma_lambda,
        "L_axis": L_axis, "amp": amp, "delta_L": delta_L, "lam_max": lam_max,
        "peaks": peaks, "noise": noise, "height": height,
    }


def lambda_range_robustness(lams, weights, ref_peaks, n_grid, gauss_factor,
                            poly_deg, q_lo, q_hi, snr_floor, delta_L,
                            bands=((0, 75), (10, 85), (25, 100))):
    """Discriminator: a GENUINE closed-geodesic peak has a lambda-range-INDEPENDENT
    position; a truncation/aliasing artifact moves or vanishes when the spectral
    lambda-window is changed. Re-run the pipeline on lambda sub-bands (percentile
    windows of the spectrum) and check which reference peaks recur within delta_L
    in EVERY sub-band. This is the strong physical complement to the smoothing
    window-halving test (which only varies the Strutinsky gamma, not the spectral
    support). Returns the count of ref peaks robust across all sub-bands + detail.
    """
    s = np.sort(lams)  # (local)
    sub_peak_sets = []  # (local)
    for lo_pct, hi_pct in bands:
        lo, hi = np.percentile(s, [lo_pct, hi_pct])  # (local)
        m = (lams >= lo) & (lams <= hi)  # (local)
        if m.sum() < 100:
            continue
        sub = run_pipeline(lams[m], weights[m], n_grid, gauss_factor, poly_deg,
                           q_lo, q_hi, snr_floor)  # (local)
        sub_peak_sets.append(np.array([p[0] for p in sub["peaks"] if p[2] >= snr_floor]))
    robust = []  # (local)
    for L, amp, snr, drift in ref_peaks:
        if all(s_set.size > 0 and np.min(np.abs(s_set - L)) <= delta_L for s_set in sub_peak_sets):
            robust.append((L, amp, snr))
    return len(robust), robust, len(sub_peak_sets)


# ---------------------------------------------------------------------------
# Section 7 — tau=0 synthetic control (pipeline-correctness check)
# ---------------------------------------------------------------------------
def coroot_lengths(m_max: int = 3):
    """Predicted bi-invariant SU(3) closed-geodesic lengths (W7-1 coroot lattice).

    Leading Casimir quadratic form Q(p,q) = n^T M n, M = (1/3)[[1,1/2],[1/2,1]].
    Wave-trace conjugation: E = lambda^2 = 4*pi^2 * n^T (M/4pi^2) n, so the dual
    (real-space) metric is g = 4*pi^2 * M^{-1}; closed-geodesic length of lattice
    vector m is L(m) = sqrt(m^T g m) = 2*pi*sqrt(m^T M^{-1} m). FT-in-lambda peaks
    land at these L by Poisson summation (cos(lambda*|v|) oscillation).

    Returns sorted unique lengths (the coroot-lattice length spectrum) and the
    primitive (shortest) length.
    """
    M = (1.0 / 3.0) * np.array([[1.0, 0.5], [0.5, 1.0]])  # (local) Casimir form
    Minv = np.linalg.inv(M)  # (local)
    lengths = []  # (local)
    for m1 in range(-m_max, m_max + 1):
        for m2 in range(-m_max, m_max + 1):
            if m1 == 0 and m2 == 0:
                continue
            m = np.array([m1, m2], dtype=np.float64)  # (local)
            lengths.append(2.0 * np.pi * float(np.sqrt(m @ Minv @ m)))
    lengths = np.array(sorted(lengths))  # (local)
    uniq = []  # (local)
    for L in lengths:
        if not uniq or abs(L - uniq[-1]) > 1e-6:
            uniq.append(float(L))
    return np.array(uniq), float(uniq[0])


def build_tau0_control_spectrum(c_off, p_max):
    """tau=0 bi-invariant closed spectrum: |lambda|^2 = C2(p,q) + c_off, PW-weighted.

    Mimics the cache reconstruction: each (p,q) contributes the scalar Dirac
    eigenvalue lambda = sqrt(C2+c_off) with Peter-Weyl multiplicity dim(p,q)^2
    (irrep appears dim times in L^2; rep dimension dim) times spinor rank 16.
    """
    lams = []  # (local)
    w = []  # (local)
    for p in range(p_max + 1):
        for q in range(p_max + 1):
            if p + q > p_max:
                continue
            lam = float(np.sqrt(casimir_pq(p, q) + c_off))  # (local)
            mult = (dim_pq(p, q) ** 2) * 16.0  # (local) PW-weighted x spinor
            lams.append(lam)
            w.append(mult)
    return np.array(lams), np.array(w)


# ---------------------------------------------------------------------------
# Section 8 — Cache loading + counting choices
# ---------------------------------------------------------------------------
def load_cache_spectra():
    """Load the s84 L=12 cache; return PRIMARY (PW-weighted) and DIAGNOSTIC
    (block-level) (lambda, weight) arrays.

    Cache: sector_evals dict {(p,q): {dim, level, abs_evals}}. abs_evals is the
    FULL Dirac block V_{(p,q)} (x) C^16 (length = 16*dim; spinor rank 16 applied;
    Peter-Weyl regular-rep multiplicity NOT yet applied). 90 sectors, max p+q=12,
    sector (4,4) ABSENT.

    PRIMARY (PW-weighted): each block eigenvalue weighted by an extra dim(p,q)
      (the regular-representation multiplicity in L^2(SU(3))). Weyl exponent ~8.
    DIAGNOSTIC (block-level): each block eigenvalue counted once. Weyl exponent ~5.

    Sector (4,4) reconstruction: (4,4) is missing. Its bottom-up contribution is
    bounded — dim(4,4)=125, C2(4,4)=24, so its eigenvalues sit at high |lambda|
    (~sqrt(24+c_off) range, partially above the cache lambda_max). We BOUND its
    contribution by NOT reconstructing it (the cache is the substrate-IS data at
    L=12; the single missing high-(p,q) sector shifts the high-lambda tail only,
    where the Weyl fit + window already down-weight). The 89-of-90-present
    completeness is recorded; the omission is a sub-percent perturbation on the
    full L^2 multiplicity (dim(4,4)^2*16 = 250000 of 31,956,720 PW total = 0.78%).
    """
    d = np.load(CACHE_PATH, allow_pickle=True)
    se = d["sector_evals"].item()  # (local)
    block_lams = []  # (local)
    block_w = []  # (local)
    pw_lams = []  # (local)
    pw_w = []  # (local)
    n_sectors = 0  # (local)
    has_44 = (4, 4) in se  # (local)
    for (p, q), v in se.items():
        a = np.asarray(v["abs_evals"], dtype=np.float64)  # (local)
        dim = int(v["dim"])  # (local)
        if a.size == 0:
            continue
        n_sectors += 1
        # DIAGNOSTIC: block-level, weight 1 each
        block_lams.append(a)
        block_w.append(np.ones_like(a))
        # PRIMARY: PW-weighted, each block eigenvalue weighted by dim (extra L^2 mult)
        pw_lams.append(a)
        pw_w.append(np.full_like(a, float(dim)))
    block_lams = np.concatenate(block_lams)  # (local)
    block_w = np.concatenate(block_w)  # (local)
    pw_lams = np.concatenate(pw_lams)  # (local)
    pw_w = np.concatenate(pw_w)  # (local)
    info = {
        "n_sectors": n_sectors, "has_44": has_44,
        "n_block": int(block_lams.size),
        "pw_total_weight": float(pw_w.sum()),
        "lam_min": float(block_lams.min()), "lam_max": float(block_lams.max()),
    }
    return (pw_lams, pw_w), (block_lams, block_w), info


# ---------------------------------------------------------------------------
# Section 9 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
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
# Section 10 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    print(f"  torch FFT available: {_HAVE_TORCH}")
    print(f"  regulator pin: a_n^zeta = "
          f"({a_0_FW_zeta}, {a_2_FW_zeta}, {a_4_FW_zeta}, {a_6_FW_zeta}, {a_8_FW_zeta})")
    print(f"  tau_fold = {tau_fold}")

    # ---- Load cache spectra (PRIMARY + DIAGNOSTIC counting) ----
    (pw_lams, pw_w), (blk_lams, blk_w), cinfo = load_cache_spectra()
    print(f"\n=== s84 L=12 cache ===")
    print(f"  sectors present: {cinfo['n_sectors']} (max p+q=12; (4,4) present: {cinfo['has_44']})")
    print(f"  block-level entries: {cinfo['n_block']}")
    print(f"  PW-weighted total: {cinfo['pw_total_weight']:.0f}")
    print(f"  lambda range: [{cinfo['lam_min']:.6f}, {cinfo['lam_max']:.6f}]")

    # ---- Weyl-exponent diagnostic (10-60 band = transcript 7.817/5.022 anchor) ----
    def weyl_exp(lams, w, lo, hi):
        # weighted staircase: expand by weight (integerized) for exponent fit on the band
        s = np.sort(lams)  # (local)
        # cumulative weighted count via argsort
        order = np.argsort(lams)  # (local)
        cw = np.cumsum(w[order])  # (local)
        ls = lams[order]  # (local)
        l1, l2 = np.percentile(ls, [lo, hi])  # (local)
        m = (ls >= l1) & (ls <= l2) & (cw > 0)  # (local)
        A = np.polyfit(np.log(ls[m]), np.log(cw[m]), 1)  # (local)
        return float(A[0])
    exp_pw_1060 = weyl_exp(pw_lams, pw_w, 10, 60)  # (local)
    exp_blk_1060 = weyl_exp(blk_lams, blk_w, 10, 60)  # (local)
    exp_pw_2070 = weyl_exp(pw_lams, pw_w, QUANTILE_LO, QUANTILE_HI)  # (local)
    exp_blk_2070 = weyl_exp(blk_lams, blk_w, QUANTILE_LO, QUANTILE_HI)  # (local)
    print(f"\n=== Weyl exponents (counting-choice pin) ===")
    print(f"  PRIMARY  (PW-weighted)  exp[10-60]={exp_pw_1060:.3f}  exp[20-70]={exp_pw_2070:.3f}  (target ~8; transcript 7.817 at 10-60)")
    print(f"  DIAGNOSTIC (block-level) exp[10-60]={exp_blk_1060:.3f}  exp[20-70]={exp_blk_2070:.3f}  (target ~5; transcript 5.022)")
    primary_gt_diag = exp_pw_2070 > exp_blk_2070  # (local) PRIMARY > DIAGNOSTIC (substitution-chain direction)
    print(f"  PRIMARY exp > DIAGNOSTIC exp : {primary_gt_diag}  (substitution-chain Step-4 direction)")

    # ---- PRIMARY pipeline at tau_fold ----
    print(f"\n=== PRIMARY (PW-weighted) length-spectrum FT at tau_fold={tau_fold} ===")
    res_pw = run_pipeline(pw_lams, pw_w, N_FFT_GRID, GAUSS_WIDTH_FACTOR,
                          WEYL_POLY_DEG, QUANTILE_LO, QUANTILE_HI, SNR_FLOOR)
    print(f"  delta_L = 2pi/lambda_max = {res_pw['delta_L']:.4f}")
    print(f"  Gaussian window sigma_lambda = {res_pw['sigma_lambda']:.4f}")
    print(f"  noise floor (1.4826*MAD) = {res_pw['noise']:.3e}; SNR>={SNR_FLOOR} height = {res_pw['height']:.3e}")
    print(f"  PRIMARY peaks (L, amp, SNR):")
    for L, amp, snr in res_pw["peaks"][:12]:
        print(f"    L={L:.4f}  amp={amp:.3e}  SNR={snr:.2f}")

    # ---- Window-halving cross-check (PRIMARY) ----
    print(f"\n=== Window-halving cross-check (PRIMARY; sigma -> sigma/2) ===")
    res_pw_half = run_pipeline(pw_lams, pw_w, N_FFT_GRID, GAUSS_WIDTH_FACTOR_HALF,
                               WEYL_POLY_DEG, QUANTILE_LO, QUANTILE_HI, SNR_FLOOR)
    delta_L = res_pw["delta_L"]  # (local)
    # match full-window peaks to half-window peaks; a stable peak drifts <= delta_L
    half_L = np.array([p[0] for p in res_pw_half["peaks"]]) if res_pw_half["peaks"] else np.array([])  # (local)
    stable_peaks = []  # (local)
    for L, amp, snr in res_pw["peaks"]:
        if snr < SNR_FLOOR:
            continue
        if half_L.size == 0:
            continue
        drift = float(np.min(np.abs(half_L - L)))  # (local)
        if drift <= delta_L:
            stable_peaks.append((L, amp, snr, drift))
    print(f"  full-window SNR>={SNR_FLOOR} peaks: {sum(1 for p in res_pw['peaks'] if p[2] >= SNR_FLOOR)}")
    print(f"  window-stable (drift <= delta_L={delta_L:.4f}) peaks: {len(stable_peaks)}")
    for L, amp, snr, drift in stable_peaks[:12]:
        print(f"    L={L:.4f}  amp={amp:.3e}  SNR={snr:.2f}  drift={drift:.4f}")
    n_stable_peaks = len(stable_peaks)  # (local)

    # ---- lambda-range robustness (genuine geodesic vs truncation artifact) ----
    print(f"\n=== lambda-range robustness (PRIMARY; sub-band recurrence) ===")
    n_robust, robust_peaks, n_subbands = lambda_range_robustness(
        pw_lams, pw_w, stable_peaks, N_FFT_GRID, GAUSS_WIDTH_FACTOR,
        WEYL_POLY_DEG, QUANTILE_LO, QUANTILE_HI, SNR_FLOOR, delta_L
    )
    dominant_L = stable_peaks[0][0] if stable_peaks else float("nan")  # (local) strongest peak
    print(f"  sub-bands tested: {n_subbands}; window-stable peaks recurring in ALL sub-bands "
          f"(within delta_L={delta_L:.4f}): {n_robust}")
    print(f"  dominant (strongest-amplitude) stable peak: L={dominant_L:.4f}")
    for L, amp, snr in robust_peaks[:8]:
        print(f"    robust L={L:.4f}  amp={amp:.3e}  SNR={snr:.2f}")

    # ---- tau=0 synthetic control ----
    print(f"\n=== tau=0 synthetic control (pipeline-correctness check) ===")
    coroot_L, primitive_L = coroot_lengths(m_max=3)
    print(f"  predicted coroot-lattice lengths (shortest 6): {np.round(coroot_L[:6], 4).tolist()}")
    print(f"  primitive coroot length = {primitive_L:.4f}  (= 4*pi = {4*np.pi:.4f})")
    c0_lams, c0_w = build_tau0_control_spectrum(C_OFF_TAU0, P_MAX_CONTROL)
    # match the control to the same FFT discipline; its native lambda_max is larger,
    # so its delta_L is finer — the control validates on its OWN resolution budget.
    res_c0 = run_pipeline(c0_lams, c0_w, N_FFT_GRID, GAUSS_WIDTH_FACTOR,
                          WEYL_POLY_DEG, QUANTILE_LO, QUANTILE_HI, SNR_FLOOR)
    delta_L_c0 = res_c0["delta_L"]  # (local)
    print(f"  control lambda_max = {res_c0['lam_max']:.4f}; delta_L_control = {delta_L_c0:.4f}")
    print(f"  control peaks (L, amp, SNR):")
    for L, amp, snr in res_c0["peaks"][:8]:
        print(f"    L={L:.4f}  amp={amp:.3e}  SNR={snr:.2f}")
    # does the control's strongest peak land on the coroot lattice within delta_L?
    control_peaks_L = np.array([p[0] for p in res_c0["peaks"] if p[2] >= SNR_FLOOR])  # (local)
    control_on_lattice = False  # (local)
    control_match_detail = []  # (local)
    if control_peaks_L.size > 0:
        # the fundamental geometric length is the primitive coroot length; its harmonics
        # are integer multiples. Check the strongest control peak lands on primitive or a harmonic.
        strongest = control_peaks_L[0]  # (local) peaks already amp-sorted
        # nearest harmonic of the primitive length
        n_harm = max(int(round(strongest / primitive_L)), 1)  # (local)
        pred = n_harm * primitive_L  # (local)
        dev = abs(strongest - pred)  # (local)
        control_on_lattice = dev <= delta_L_c0
        control_match_detail.append((float(strongest), int(n_harm), float(pred), float(dev)))
        print(f"  strongest control peak L={strongest:.4f} -> harmonic n={n_harm} of primitive "
              f"(pred {pred:.4f}); deviation {dev:.4f} {'<=' if control_on_lattice else '>'} delta_L={delta_L_c0:.4f}")
    print(f"  CONTROL ON LATTICE: {control_on_lattice}")

    # ---- Verdict logic (plan §W7-2 PRE-REGISTERED rubric — strict_PASS_boundary) ----
    # The PRE-REGISTERED criterion (frozen at plan-freeze) is:
    #   PASS iff n_stable_peaks >= 3 (SNR>=6 AND window-halving position drift <= delta_L)
    #           AND tau=0 control peaks on the W7-1 coroot lattice within delta_L.
    #   FAIL iff the tau=0 control FAILS (peaks NOT on lattice) -> pipeline defect.
    #   INFO iff control OK but < 3 stable peaks (resolution-limited by L_max=12).
    # The lambda-range robustness count (n_robust) is a DIAGNOSTIC added post-hoc; it is
    # NOT in the pre-registered criterion and does NOT change the verdict (adding it as a
    # PASS gate after seeing results would be Class-3 post-hoc pre-registration editing per
    # v3-closure-recovery.md). It is DISCLOSED transparently: n_robust=0 means the dominant
    # tau_fold peaks (L~124) are truncation-INFLUENCED (spectral-window-dependent under the
    # compressed L_max=12 lambda-support [0.82,5.42], delta_L=1.16 coarse) rather than clean
    # range-independent closed-geodesic lengths. The window-halving (Gaussian-sigma) test the
    # plan pinned cannot detect spectral-window truncation; the lambda-range test can, and
    # flags the resolution limitation honestly for W7-3/W7-4.
    if not control_on_lattice:
        verdict = "FAIL"  # (local)
        value = (f"control_OFF_lattice_pipeline_defect_n_stable={n_stable_peaks}_"
                 f"primitiveL={primitive_L:.4f}")  # (local)
    elif n_stable_peaks >= N_STABLE_PEAKS_PASS:
        verdict = "PASS"  # (local)
        value = (f"n_stable_peaks={n_stable_peaks}_>=3_SNR>=6_window-halving-stable_"
                 f"control_on_coroot_lattice_primitiveL={primitive_L:.4f}_deltaL={delta_L:.4f}_"
                 f"DIAGNOSTIC_n_lambda-range-robust={n_robust}_dominantL={dominant_L:.2f}_"
                 f"tau_fold-peaks-truncation-influenced-L_max=12")  # (local)
    else:
        verdict = "INFO"  # (local)
        value = (f"n_stable_peaks={n_stable_peaks}_<3_resolution-limited_L_max=12_"
                 f"dominantL={dominant_L:.2f}_"
                 f"control_VALIDATES_on_coroot_lattice_deltaL={delta_L:.4f}")  # (local)
    print(f"\n=== VERDICT: {verdict} (PRE-REGISTERED criterion: window-halving + control) ===")
    print(f"  value = {value}")
    print(f"  DIAGNOSTIC (not a verdict gate): lambda-range-robust peaks = {n_robust} "
          f"=> dominant L~{dominant_L:.1f} is truncation-influenced (L_max=12 coarse delta_L={delta_L:.2f})")

    # ---- Plot ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    # (a) PRIMARY density + Weyl smooth
    ax = axes[0, 0]
    ax.plot(res_pw["grid"], res_pw["rho_smoothed"], lw=0.8, label="rho_smoothed (PW)")
    ax.plot(res_pw["grid"], res_pw["rho_weyl"], lw=1.2, ls="--", label="Weyl smooth (a_n^zeta)")
    ax.set_xlabel("lambda (M_KK-natural)"); ax.set_ylabel("rho(lambda)")
    ax.set_title(f"PRIMARY (PW-weighted) density at tau_fold={tau_fold}; Weyl exp~{exp_pw_1060:.2f}")
    ax.legend(fontsize=8)
    # (b) PRIMARY oscillatory residual
    ax = axes[0, 1]
    ax.plot(res_pw["grid"], res_pw["rho_osc"], lw=0.7, color="C3")
    ax.set_xlabel("lambda"); ax.set_ylabel("rho_osc(lambda)")
    ax.set_title("PRIMARY oscillatory residual (geodesic-length carrier)")
    # (c) PRIMARY length spectrum
    ax = axes[1, 0]
    ax.plot(res_pw["L_axis"], res_pw["amp"], lw=0.9, color="C0")
    ax.axhline(res_pw["height"], ls=":", color="grey", label=f"SNR={SNR_FLOOR} floor")
    for L, amp, snr, drift in stable_peaks[:6]:
        ax.axvline(L, ls="--", color="C3", alpha=0.5)
        ax.annotate(f"{L:.2f}", (L, amp), fontsize=7)
    ax.set_xlim(0, min(res_pw["L_axis"].max(), 60))
    ax.set_xlabel("L_gamma = 2pi*freq(lambda)"); ax.set_ylabel("|FT|")
    ax.set_title(f"MEASURED length spectrum (tau_fold); {n_stable_peaks} stable peaks; delta_L={delta_L:.3f}")
    ax.legend(fontsize=8)
    # (d) tau=0 control length spectrum + coroot lattice
    ax = axes[1, 1]
    ax.plot(res_c0["L_axis"], res_c0["amp"], lw=0.9, color="C2")
    for L in coroot_L[:8]:
        ax.axvline(L, ls="--", color="C1", alpha=0.6)
    ax.axvline(primitive_L, ls="-", color="C1", lw=1.5, label=f"primitive coroot {primitive_L:.2f}=4pi")
    ax.set_xlim(0, min(res_c0["L_axis"].max(), 100))
    ax.set_xlabel("L_gamma"); ax.set_ylabel("|FT|")
    ax.set_title(f"tau=0 CONTROL vs coroot lattice; on-lattice={control_on_lattice}")
    ax.legend(fontsize=8)
    fig.suptitle(f"{GATE_ID}: substrate length spectrum (geometric side of the trace formula)", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"\n  plot -> {OUT_PNG}")

    # ---- Save data (forward-pinned to W7-3/W7-4) ----
    primary_peaks_arr = np.array([[p[0], p[1], p[2]] for p in res_pw["peaks"]], dtype=np.float64) if res_pw["peaks"] else np.zeros((0, 3))  # (local)
    stable_peaks_arr = np.array([[p[0], p[1], p[2], p[3]] for p in stable_peaks], dtype=np.float64) if stable_peaks else np.zeros((0, 4))  # (local)
    diag_res = run_pipeline(blk_lams, blk_w, N_FFT_GRID, GAUSS_WIDTH_FACTOR,
                            WEYL_POLY_DEG, QUANTILE_LO, QUANTILE_HI, SNR_FLOOR)  # (local) DIAGNOSTIC for the record
    diag_peaks_arr = np.array([[p[0], p[1], p[2]] for p in diag_res["peaks"]], dtype=np.float64) if diag_res["peaks"] else np.zeros((0, 3))  # (local)
    np.savez(
        OUT_NPZ,
        # PRIMARY measured length spectrum (forward-pinned to W7-3/W7-4)
        primary_peaks=primary_peaks_arr,         # [L, amp, SNR]
        stable_peaks=stable_peaks_arr,           # [L, amp, SNR, drift] window-stable PASS basis
        n_stable_peaks=n_stable_peaks,
        # lambda-range robustness (genuine geodesic vs truncation artifact)
        n_lambda_range_robust=n_robust,
        lambda_range_robust_peaks=np.array([[p[0], p[1], p[2]] for p in robust_peaks], dtype=np.float64) if robust_peaks else np.zeros((0, 3)),
        dominant_L=dominant_L,                   # strongest-amplitude stable peak (deformed primitive-orbit length)
        L_axis_primary=res_pw["L_axis"],
        amp_primary=res_pw["amp"],
        delta_L=res_pw["delta_L"],               # resolution budget (inherited by W7-3/W7-4)
        lam_max=res_pw["lam_max"],
        sigma_lambda=res_pw["sigma_lambda"],
        snr_floor=SNR_FLOOR,
        noise_floor=res_pw["noise"],
        # DIAGNOSTIC (block-level)
        diagnostic_peaks=diag_peaks_arr,
        weyl_exp_primary_1060=exp_pw_1060,
        weyl_exp_block_1060=exp_blk_1060,
        weyl_exp_primary_2070=exp_pw_2070,
        weyl_exp_block_2070=exp_blk_2070,
        # tau=0 control
        coroot_lengths=coroot_L,
        primitive_coroot_length=primitive_L,
        control_peaks=np.array([[p[0], p[1], p[2]] for p in res_c0["peaks"]], dtype=np.float64) if res_c0["peaks"] else np.zeros((0, 3)),
        control_on_lattice=control_on_lattice,
        control_delta_L=delta_L_c0,
        control_match_detail=np.array(control_match_detail, dtype=np.float64) if control_match_detail else np.zeros((0, 4)),
        # provenance
        tau_fold=tau_fold,
        c_off_tau0=C_OFF_TAU0,
        verdict=verdict,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        regulator_pin="a_n^zeta",
    )
    print(f"  data  -> {OUT_NPZ}")

    # ---- Dual-SHA + 4-tuple ----
    audit_sha, content_sha = compute_dual_sha(Path(__file__), SHARED_DIR / "canonical_constants.py", pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print(f"  4-tuple: (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  elapsed: {time.time()-t0:.1f}s")

    # regulator-pin companion row (regulator-pin-discipline.md MANDATORY)
    extra = [
        f"# regulator_pin=a_n^zeta (a_0={a_0_FW_zeta},a_2={a_2_FW_zeta},a_4={a_4_FW_zeta},"
        f"a_6={a_6_FW_zeta},a_8={a_8_FW_zeta}); STRUTINSKY-WEYL-SUBTRACT smooth part",
        f"# PRIMARY=PW-dim-weighted (Weyl exp[10-60]={exp_pw_1060:.3f}~8); "
        f"DIAGNOSTIC=block-level (exp[10-60]={exp_blk_1060:.3f}~5); n_stable_peaks={n_stable_peaks}; "
        f"control_on_coroot_lattice={control_on_lattice} (primitive L=4pi={primitive_L:.4f})",
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra)
    return 0


if __name__ == "__main__":
    sys.exit(main())
