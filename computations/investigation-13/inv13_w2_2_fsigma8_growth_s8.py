#!/usr/bin/env python3
"""
INV13 W2-2 — INV13-W2-2-FSIGMA8-GROWTH-S8 : GGE growth-suppression f*sigma8(z)
curve + S8-tension band test on a dense DESI/Euclid-aligned z-grid
=============================================================================

Gate: INV13-W2-2-FSIGMA8-GROWTH-S8 ([SIGN], PHONONIC, investigation track)

Pre-registered threshold (plan §W2-2):
  operator (set/sign/bindability):
    (i)  magnitude axis: S8_FW in [0.76, 0.83]  (band membership; lensing-lower
         KiDS/DES ~0.76 to Planck-upper ~0.83 -- the S8-tension window the
         prediction aims to sit between)
    (ii) [SIGN] axis: delta(f*sigma8)(z) < 0 for ALL z in [0, 1.5]  (strict
         growth SUPPRESSION, not enhancement)
    (iii) DESI/Euclid bindability: exists a z-bin where
          |delta(f*sigma8)(z)| / sigma_DESI5yr(z) >= 1.0
          (Row #71 gives 1.013 @ z=0.51).
  strict_PASS_boundary:
    S8 band [0.76, 0.83]; sign delta(f*sigma8) < 0 for all z; bindability ratio
    max_z |delta| / sigma_DESI5yr >= 1.0.
  PASS  iff S8_FW in band  AND sign-PASS (all delta<0)  AND >=1 bindable z-bin
  FAIL  iff S8_FW out of band  OR  sign FAIL (any delta>=0)
  INFO  iff S8_FW in band AND sign-PASS but z-shape un-bindable (no bin >= sigma)

  The composite top-line is the [SIGN] 3-tuple collapse (gate-verdicts.md):
    sign_verdict     = PASS iff delta(f*sigma8)(z) < 0 at EVERY z-grid point
    magnitude_verdict= PASS iff S8_FW in [0.76,0.83]
                       INFO if narrowly outside by < info_pad
                       FAIL otherwise
    regime_verdict   = VALID iff the linear growth ODE is within its regime of
                       validity over the full z in [0,1.5] window (domain_used_frac>=0.95);
                       the bindability sub-test does NOT auto-shorten the domain.
    composite: regime=BREAKDOWN -> FAIL ; sign=FAIL -> FAIL ;
               mag=FAIL & regime=VALID -> FAIL ; mag=INFO -> INFO ; else PASS

WHAT IS NEW (distinct from S96-OBS-FSIGMA8-FORECAST and INV7-W1-6):
  S96 reported per-bin sigma-distances (max 0.51/1.01/1.53 current/DESI5yr/Euclid) on a
  7-bin grid; INV7-W1-6 reported the model-vs-model JOINT chi2 significance. THIS gate
  targets the S8 BAND MEMBERSHIP + per-z bindability on a DENSE 16-point z-grid (Dz=0.1,
  z in [0,1.5]) aligned to DESI ELG/LRG/QSO + Euclid spectroscopic bins -- the deliverable
  is the DESI/Euclid-bindable z-shape and the S8-tension placement, NOT a single joint sigma.
  The K_pivot-localization corollary (NON-gating) is reported: a clustering-scale growth
  success while n_s fails at the CMB pivot would localize a possible n_s failure to the
  K_pivot mapping (seed G3), not the GGE physics.

CRITICAL SOURCING DISCIPLINE (load-bearing, per plan + canonical_constants cross-note):
  The growth normalization is sigma8_growth_a2 = 0.79317 -- the a2 Seeley-DeWitt
  STRUCTURE-GROWTH channel readout that FEEDS fsigma8 forecasts (linear growth
  f=dlnD/dlna). It is NOT the headline sigma8_OZ_50 = 0.799 (the O-Z/spectral-action
  channel). The two are channel-distinct substrate-IS readouts ~0.7% apart and MUST NOT
  be conflated; the ~0.7% spread is NOT a single-channel uncertainty band.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py            (feeds audit_sha256)
  - computations/session-96/s96_obs_fsigma8_forecast.npz   (Row #71 source: max_frac_FW_pct,
        the 7-bin z-shape + DESI-5yr/Euclid per-bin sigma forecast)
  - computations/session-96/s96_obs_first_sound_ring.npz   (Row #72: A_FS, k1, the companion
        first-sound BAO ring + sigma_Pk_DESI_Y5_BAO_scale)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<S8_FW + suppression summary>, scheme=GGE-acoustic-growth-a2, convention=RATIO, L_max=N/A)

METHODOLOGY
-----------
STEP 1 -- anchor linear growth at the structure-growth channel:
  sigma8(z=0)_FW = sigma8_growth_a2 = 0.79317 (NOT the headline 0.799).
STEP 2 -- integrate the linear-growth ODE D'' + (2 + dlnH/dlna)D' - 1.5 Om(a)D = 0 in ln a
  (matter-dom IC) in the borrowed emergent-FRW background H(z): FW uses constant
  w = w0_FW = -0.918 (Volovik-partition + effacement), LCDM uses w = -1. This is the
  SAME a2 Seeley-DeWitt growth channel + the SAME ODE form as INV7-W1-6 (consistency).
  Reproduces the canonical anchors f_FW(0)=0.5254916, f_LCDM(0)=0.5271304, product
  suppression peak -4.058% @ z=0.51.
STEP 3 -- form the f*sigma8(z) curve on a DENSE 16-point z-grid:
  sigma8_FW(z)   = sigma8_growth_a2 * D_FW(z)/D_FW(0)
  sigma8_LCDM(z) = sigma_8 (=0.811) * D_LCDM(z)/D_LCDM(0)
  fsig8_FW(z)    = f_FW(z) * sigma8_FW(z)   ;   fsig8_LCDM(z) = f_LCDM(z) * sigma8_LCDM(z)
  delta(z)       = fsig8_FW(z)/fsig8_LCDM(z) - 1   (the fractional product suppression)
  S8_FW          = sigma8_growth_a2 * sqrt(Omega_m / 0.3)   (clustering amplitude)
TEST:
  (i)  S8_FW in [0.76, 0.83] (magnitude / band)
  (ii) delta(z) < 0 for all z (sign)
  (iii) bindability: interpolate the S96 DESI-5yr/Euclid per-bin sigma onto the dense grid;
       max_z |delta(z)| / sigma_DESI5yr(z) >= 1.0

Classification: PHONONIC.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap OMP_NUM_THREADS=8 BEFORE import numpy (1D growth ODE on 16-pt z-grid; no GPU benefit)
- SHA-256 of all input files logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- verdict emitted via emit_verdict MCP tool (race-safe); script only PRINTS the payload
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import); CPU thread cap FIRST
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    Omega_m, w0_FW, sigma_8, sigma8_growth_a2, sigma8_OZ_50, f_FW, f_LCDM,
    fsigma8_product_suppression_FW_max_pct, f_bare_suppression_FW_pct,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "13"                                                    # (local) investigation number
GATE_ID = "INV13-W2-2-FSIGMA8-GROWTH-S8"                          # (local)
SCHEME = "GGE-acoustic-growth-a2"                                 # (local) a2 Seeley-DeWitt growth channel
CONVENTION = "RATIO"                                              # (local) delta(fsig8)=fsig8_FW/fsig8_LCDM-1 fractional; S8 dimensionless
L_MAX = "N/A"                                                     # (local) growth ODE, not a D_K truncation

# --- pre-registered thresholds (plan §W2-2) ---
S8_BAND_LO = 0.76                                                 # (local) lensing-lower KiDS/DES ~0.76
S8_BAND_HI = 0.83                                                 # (local) Planck-upper ~0.83
S8_INFO_PAD = 0.01                                                # (local) narrow-miss INFO pad on band edges
BINDABILITY_THR = 1.0                                            # (local) max_z |delta|/sigma_DESI5yr >= 1.0
S8_REF_OM_NORM = 0.3                                             # (local) S8 = sigma8 * sqrt(Om/0.3) standard normalization
DOMAIN_FRAC_VALID = 0.95                                         # (local) regime VALID iff >=95% of intended window used
DOMAIN_FRAC_MARGINAL = 0.50                                      # (local) MARGINAL band floor

# external S8 observational anchors (methodological cross-check; NOT substrate-derived)
S8_PLANCK = 0.832                                                # (local) Planck 2018 TT,TE,EE+lowE+lensing S8
S8_KIDS = 0.759                                                  # (local) KiDS-1000 cosmic shear S8
S8_DES = 0.776                                                   # (local) DES-Y3 3x2pt S8

# --- z-grid + growth-ODE machinery (plan machinery_pin_map) ---
N_Z = 16                                                         # (local) z-grid points across z in [0,1.5]
Z_LO, Z_HI = 0.0, 1.5                                            # (local) clustering-scale growth window
ODE_RTOL = 1e-9                                                  # (local) growth-ODE convergence tolerance (plan tolerance pin)
ODE_ATOL = 1e-12                                                 # (local)
A_INIT = 1e-3                                                    # (local) matter-dom ODE initial scale factor
N_EVAL = 1000                                                    # (local) growth-ODE base grid nodes (max_step control)
K_BAND = (0.1, 0.3)                                             # (local) clustering scale [h/Mpc] where sigma8 lives (reported)

OUT_NPZ = SESSION_DIR / "inv13_w2_2_fsigma8_growth_s8.npz"       # (local)
OUT_PNG = SESSION_DIR / "inv13_w2_2_fsigma8_growth_s8.png"       # (local)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
FSIGMA8_NPZ = COMPUTATIONS_DIR / "session-96" / "s96_obs_fsigma8_forecast.npz"  # (local) Row #71
FIRST_SOUND_NPZ = COMPUTATIONS_DIR / "session-96" / "s96_obs_first_sound_ring.npz"  # (local) Row #72
INPUT_FILES = [CANONICAL_PATH, FSIGMA8_NPZ, FIRST_SOUND_NPZ]


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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
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
# Section 5 — Growth ODE (SAME form as INV7-W1-6 for cross-investigation consistency)
# ---------------------------------------------------------------------------

def _Hsq_over_H0sq(a: np.ndarray, w: float) -> np.ndarray:
    """E^2(a) = H^2/H0^2 for flat wCDM with constant w (borrowed emergent-FRW)."""
    Ode = 1.0 - Omega_m  # (local)
    return Omega_m * a ** -3 + Ode * a ** (-3.0 * (1.0 + w))  # (local)


def _dlnH_dlna(a: np.ndarray, w: float) -> np.ndarray:
    """d ln H / d ln a for flat wCDM constant w."""
    Ode = 1.0 - Omega_m  # (local)
    num = (-3.0 * Omega_m * a ** -3
           + (-3.0 * (1.0 + w)) * Ode * a ** (-3.0 * (1.0 + w)))  # (local)
    return 0.5 * num / _Hsq_over_H0sq(a, w)  # (local)


def growth_curve(w: float, a_eval: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Integrate D'' + (2 + dlnH/dlna)D' - 1.5 Om(a)D = 0 in ln a;
    return (D(a_eval), f(a_eval)=dlnD/dlna). Matter-dom IC D~a at a_init.
    a_eval MUST be sorted increasing (solve_ivp constraint)."""
    def rhs(lna, y):  # (local)
        a = np.exp(lna)  # (local)
        D, Dp = y  # (local)
        Om_a = Omega_m * a ** -3 / _Hsq_over_H0sq(a, w)  # (local)
        ddD = -(2.0 + _dlnH_dlna(a, w)) * Dp + 1.5 * Om_a * D  # (local)
        return [Dp, ddD]
    lna0 = np.log(A_INIT)  # (local)
    y0 = [A_INIT, A_INIT]  # (local) D~a, dD/dlna~a in matter dom
    lna_eval = np.log(a_eval)  # (local)
    sol = solve_ivp(rhs, [lna0, 0.0], y0, t_eval=lna_eval,
                    rtol=ODE_RTOL, atol=ODE_ATOL, method="RK45",
                    max_step=(0.0 - lna0) / N_EVAL)  # (local)
    D = sol.y[0]  # (local)
    Dp = sol.y[1]  # (local)
    f = Dp / D  # (local)
    return D, f


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    res: dict = {}  # (local)

    # ---- upstream Row #71 (z-shape + DESI/Euclid per-bin sigma forecast) ----
    fs8 = np.load(FSIGMA8_NPZ, allow_pickle=True)  # (local)
    z_bins_up = np.asarray(fs8["z_bins"], dtype=float)            # (local) 7 DESI/eBOSS eff-z bins
    sigma_desi5_bins = np.asarray(fs8["sigma_desi5_per_bin"], dtype=float)  # (local)
    sigma_euclid_bins = np.asarray(fs8["sigma_euclid_per_bin"], dtype=float)  # (local)
    frac_FW_bins_pct_up = np.asarray(fs8["frac_FW_bins_pct"], dtype=float)   # (local) the z-DEPENDENT -4.058% peak shape
    max_frac_FW_pct_up = float(fs8["max_frac_FW_pct"])           # (local) -4.058 canonical
    z_at_max_up = float(fs8["z_at_max_frac"])                    # (local) 0.51
    S8_FW_up = float(fs8["S8_FW"])                               # (local) 0.8128 upstream
    S8_LCDM_up = float(fs8["S8_LCDM"])                           # (local) 0.8310 upstream

    # ---- companion Row #72 (first-sound ring; the live BAO LSS imprint) ----
    fsr = np.load(FIRST_SOUND_NPZ, allow_pickle=True)  # (local)
    A_FS_up = float(fsr["A_FS"])                                 # (local) 0.204
    k1_ring_up = float(fsr["k1_ring"])                           # (local) 0.0193 Mpc^-1
    sigma_pk_desi_y5 = float(fsr["sigma_exp_DESI_Y5"])           # (local) 0.023529 fractional P(k) err

    # ---- dense z-grid ----
    # z[0]=0.0 IS the z=0 point (a=1.0), so the growth normalization D(z=0) is read directly
    # off the first grid entry -- no separate appended anchor (which would duplicate a=1.0 and
    # break solve_ivp's strictly-increasing t_eval requirement).
    z = np.linspace(Z_LO, Z_HI, N_Z)                             # (local) 16 pts, Dz=0.1; z[0]=0
    a = 1.0 / (1.0 + z)                                          # (local) a[0]=1.0
    order = np.argsort(a)                                        # (local) solve_ivp needs increasing ln a
    inv = np.argsort(order)                                      # (local)
    a_sorted = a[order]                                          # (local) strictly increasing (z grid is strictly increasing -> a strictly decreasing -> sorted unique)

    D_L, f_L = growth_curve(-1.0, a_sorted)
    D_F, f_F = growth_curve(w0_FW, a_sorted)
    D_L, f_L = D_L[inv], f_L[inv]                                # (local) back to grid order (z increasing)
    D_F, f_F = D_F[inv], f_F[inv]                                # (local)
    iz0 = int(np.argmin(z))                                      # (local) index of z=0 (a=1.0)
    D_L0, D_F0 = D_L[iz0], D_F[iz0]                              # (local) z=0 normalization

    f_L_z, f_F_z = f_L, f_F                                      # (local) full grid (z=0 included)
    s8_L_z = sigma_8 * (D_L / D_L0)                              # (local) LCDM Planck-ref sigma8(z)
    s8_F_z = sigma8_growth_a2 * (D_F / D_F0)                     # (local) FW a2-growth-channel sigma8(z)
    fs8_L_z = f_L_z * s8_L_z                                     # (local) f*sigma8 LCDM
    fs8_F_z = f_F_z * s8_F_z                                     # (local) f*sigma8 FW
    delta_z = fs8_F_z / fs8_L_z - 1.0                            # (local) fractional product suppression
    delta_z_pct = delta_z * 100.0                                # (local)

    # ---- canonical-anchor reproduction cross-checks ----
    # z=0 is grid index iz0 (a=1.0), NOT the last entry: read the bare f(z=0) there.
    f_FW_z0 = float(f_F[iz0])                                    # (local)
    f_LCDM_z0 = float(f_L[iz0])                                  # (local)
    bare_f_supp_pct = (f_FW_z0 - f_LCDM_z0) / f_LCDM_z0 * 100.0  # (local)

    # ---- [SIGN] axis: every delta(z) < 0 ----
    all_negative = bool(np.all(delta_z < 0.0))                  # (local)
    n_negative = int(np.sum(delta_z < 0.0))                     # (local)
    sign_verdict = "PASS" if all_negative else "FAIL"           # (local)

    # ---- magnitude axis: S8_FW band membership ----
    # S8 = sigma8 * sqrt(Omega_m / 0.3). The clustering amplitude uses the z=0 growth-channel sigma8.
    S8_FW = sigma8_growth_a2 * np.sqrt(Omega_m / S8_REF_OM_NORM)  # (local)
    S8_LCDM = sigma_8 * np.sqrt(Omega_m / S8_REF_OM_NORM)        # (local)
    S8_OZ = sigma8_OZ_50 * np.sqrt(Omega_m / S8_REF_OM_NORM)     # (local) headline-channel S8 (reported, NOT gating)
    in_band = bool(S8_BAND_LO <= S8_FW <= S8_BAND_HI)           # (local)
    # narrow-miss INFO pad
    in_band_padded = bool((S8_BAND_LO - S8_INFO_PAD) <= S8_FW <= (S8_BAND_HI + S8_INFO_PAD))  # (local)
    if in_band:
        magnitude_verdict = "PASS"  # (local)
    elif in_band_padded:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    S8_below_planck = bool(S8_FW < S8_LCDM)                      # (local) relief direction
    S8_dist_to_hi = S8_BAND_HI - S8_FW                          # (local)
    S8_dist_to_lo = S8_FW - S8_BAND_LO                          # (local)
    S8_vs_planck_pct = (S8_FW - S8_PLANCK) / S8_PLANCK * 100.0   # (local)
    S8_vs_kids_pct = (S8_FW - S8_KIDS) / S8_KIDS * 100.0         # (local)
    # fractional position in band: 0 at lensing edge, 1 at Planck edge
    band_frac_position = (S8_FW - S8_BAND_LO) / (S8_BAND_HI - S8_BAND_LO)  # (local)

    # ---- bindability: interpolate S96 per-bin sigma onto the dense grid ----
    # The DESI-5yr/Euclid sigma are defined at the 7 upstream eff-z bins; linear-interp
    # (clamped at the endpoints) onto the dense grid for the per-z bindability ratio.
    sig_d5_dense = np.interp(z, z_bins_up, sigma_desi5_bins)     # (local)
    sig_eu_dense = np.interp(z, z_bins_up, sigma_euclid_bins)    # (local)
    # SUBSTITUTION-CHAIN-CONSISTENT bindability (reproduces upstream Row #71 nsig_FW_desi5=1.013):
    #   sigma_desi5_per_bin is an ABSOLUTE fsig8 1-sigma forecast error (in fsig8 units; verified:
    #     it equals err_obs/2, the DESI-5yr downscale of the eBOSS absolute error, NOT a fractional
    #     sigma). Therefore the numerator MUST be the ABSOLUTE deviation |Delta fsig8(z)|, NOT the
    #     fractional |delta_z|. Dividing |delta_z| (fractional) by sigma_abs would silently treat
    #     sigma as fractional and inflate the ratio by ~1/fsig8 (~2.1x) -- the mnemonic-vs-exact
    #     trap (math-scripts.md). The absolute form is the canonical-consistent discriminator.
    abs_delta_fs8 = np.abs(fs8_F_z - fs8_L_z)                   # (local) absolute fsig8 deviation [fsig8 units]
    bind_ratio_d5 = abs_delta_fs8 / sig_d5_dense               # (local) |Dfsig8| / sigma_abs (== upstream nsig)
    bind_ratio_eu = abs_delta_fs8 / sig_eu_dense               # (local)
    max_bind_d5 = float(np.max(bind_ratio_d5))                  # (local)
    max_bind_eu = float(np.max(bind_ratio_eu))                  # (local)
    z_at_max_bind_d5 = float(z[int(np.argmax(bind_ratio_d5))])  # (local)
    n_bindable_d5 = int(np.sum(bind_ratio_d5 >= BINDABILITY_THR))  # (local)
    n_bindable_eu = int(np.sum(bind_ratio_eu >= BINDABILITY_THR))  # (local)
    bindable = bool(max_bind_d5 >= BINDABILITY_THR)             # (local) DESI-5yr is the headline survey

    # ---- regime axis: linear growth ODE validity over the full intended window ----
    # The ODE is linear-growth (valid throughout 0<=z<=1.5); the full intended z-window is
    # used (no auto-shortening on the growth axis). domain_used_frac = 1.0.
    domain_used_frac = 1.0                                      # (local) full z in [0,1.5] integrated
    if domain_used_frac >= DOMAIN_FRAC_VALID:
        regime_verdict = "VALID"  # (local)
    elif domain_used_frac >= DOMAIN_FRAC_MARGINAL:
        regime_verdict = "MARGINAL"  # (local)
    else:
        regime_verdict = "BREAKDOWN"  # (local)

    # ---- composite collapse (gate-verdicts.md deterministic rule) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # The PASS rubric ALSO requires bindability. If S8-in-band + sign-PASS but un-bindable,
    # the plan rubric INFO_meaning routes to INFO (viable but non-discriminating z-shape).
    if composite == "PASS" and not bindable:
        composite = "INFO"  # (local) in-band + sign-PASS but un-bindable z-shape
        magnitude_verdict_note = "in-band-sign-PASS-but-un-bindable"  # (local)
    else:
        magnitude_verdict_note = ""  # (local)

    # ---- K_pivot-localization corollary (NON-gating, reported only) ----
    # A clustering-scale growth success while n_s fails at the CMB pivot would localize a
    # possible n_s failure to the K_pivot mapping (seed G3), NOT the GGE growth physics.
    # The corollary holds IFF this gate is a growth success (composite in {PASS,INFO}) at a
    # scale (k~0.1-0.3 h/Mpc) distinct from the CMB pivot.
    kpivot_localization_available = bool(composite in ("PASS", "INFO") and all_negative)  # (local)

    value_str = (
        f"S8_FW={S8_FW:.4f}(band[{S8_BAND_LO},{S8_BAND_HI}]:{'IN' if in_band else 'OUT'});"
        f"S8_LCDM={S8_LCDM:.4f};sign={n_negative}/{len(delta_z)}neg;"
        f"supp_range=[{delta_z_pct.min():.3f}%,{delta_z_pct.max():.3f}%];"
        f"product_supp_max={max_frac_FW_pct_up:.4g}%@z{z_at_max_up:g};"
        f"bind_DESI5yr_max={max_bind_d5:.3f}@z{z_at_max_bind_d5:g}({n_bindable_d5}bins);"
        f"bind_Euclid_max={max_bind_eu:.3f}({n_bindable_eu}bins);"
        f"S8_vs_Planck={S8_vs_planck_pct:+.2f}%;band_pos={band_frac_position:.2f}"
    )  # (local)

    res.update({
        "value": value_str,
        # z-grid + curves
        "z_grid": z, "a_grid": a,
        "f_FW_z": f_F_z, "f_LCDM_z": f_L_z,
        "sigma8_FW_z": s8_F_z, "sigma8_LCDM_z": s8_L_z,
        "fsig8_FW_z": fs8_F_z, "fsig8_LCDM_z": fs8_L_z,
        "delta_z": delta_z, "delta_z_pct": delta_z_pct,
        # canonical-anchor reproduction
        "f_FW_z0": f_FW_z0, "f_LCDM_z0": f_LCDM_z0,
        "f_FW_canonical": f_FW, "f_LCDM_canonical": f_LCDM,
        "bare_f_supp_pct": bare_f_supp_pct,
        "bare_f_supp_canonical_pct": f_bare_suppression_FW_pct,
        "product_supp_max_pct_canonical": fsigma8_product_suppression_FW_max_pct,
        "product_supp_max_pct_upstream": max_frac_FW_pct_up,
        "z_at_product_max_upstream": z_at_max_up,
        # upstream z-shape + sigma (for plot + bindability)
        "z_bins_upstream": z_bins_up,
        "frac_FW_bins_pct_upstream": frac_FW_bins_pct_up,
        "sigma_desi5_bins": sigma_desi5_bins,
        "sigma_euclid_bins": sigma_euclid_bins,
        "sig_d5_dense": sig_d5_dense, "sig_eu_dense": sig_eu_dense,
        # S8
        "S8_FW": S8_FW, "S8_LCDM": S8_LCDM, "S8_OZ_headline": S8_OZ,
        "S8_FW_upstream": S8_FW_up, "S8_LCDM_upstream": S8_LCDM_up,
        "sigma8_growth_a2": sigma8_growth_a2, "sigma8_OZ_50": sigma8_OZ_50,
        "sigma_8_LCDM_ref": sigma_8, "Omega_m": Omega_m,
        "S8_band_lo": S8_BAND_LO, "S8_band_hi": S8_BAND_HI,
        "S8_planck": S8_PLANCK, "S8_kids": S8_KIDS, "S8_des": S8_DES,
        "S8_in_band": in_band, "S8_below_planck": S8_below_planck,
        "S8_dist_to_hi": S8_dist_to_hi, "S8_dist_to_lo": S8_dist_to_lo,
        "S8_vs_planck_pct": S8_vs_planck_pct, "S8_vs_kids_pct": S8_vs_kids_pct,
        "band_frac_position": band_frac_position,
        # bindability
        "bind_ratio_d5": bind_ratio_d5, "bind_ratio_eu": bind_ratio_eu,
        "max_bind_d5": max_bind_d5, "max_bind_eu": max_bind_eu,
        "z_at_max_bind_d5": z_at_max_bind_d5,
        "n_bindable_d5": n_bindable_d5, "n_bindable_eu": n_bindable_eu,
        "bindable": bindable, "bindability_thr": BINDABILITY_THR,
        # companion Row #72 first-sound ring
        "A_FS_ring": A_FS_up, "k1_ring": k1_ring_up, "sigma_pk_desi_y5": sigma_pk_desi_y5,
        # corollary
        "kpivot_localization_available": kpivot_localization_available,
        "k_band_lo": K_BAND[0], "k_band_hi": K_BAND[1],
        # sign / counts / verdict
        "all_negative": all_negative, "n_negative": n_negative, "n_z": len(delta_z),
        "domain_used_frac": domain_used_frac,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "magnitude_verdict_note": magnitude_verdict_note,
        "regime_verdict": regime_verdict, "composite": composite,
    })
    return res


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    z = r["z_grid"]  # (local)
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))  # (local)

    # Panel 1: f*sigma8(z) curves on the dense grid + upstream DESI-5yr error bars
    ax = axes[0]  # (local)
    ax.plot(z, r["fsig8_LCDM_z"], "s--", color="tab:blue", ms=4, label=r"$\Lambda$CDM ($w=-1$)")
    ax.plot(z, r["fsig8_FW_z"], "d-", color="tab:red", ms=4, label=r"FW ($w=-0.918$, a$_2$-growth)")
    # overlay upstream 7-bin DESI-5yr forecast sigma (on the LCDM curve, illustrative)
    zb = r["z_bins_upstream"]  # (local)
    fs8_lcdm_at_bins = np.interp(zb, z, r["fsig8_LCDM_z"])  # (local)
    ax.errorbar(zb, fs8_lcdm_at_bins, yerr=r["sigma_desi5_bins"], fmt="none",
                ecolor="tab:green", alpha=0.6, capsize=3, label="DESI-5yr forecast $\\sigma$")
    ax.set_xlabel("z"); ax.set_ylabel(r"$f\sigma_8(z)$")
    ax.set_title(r"$f\sigma_8(z)$ on dense 16-pt grid: FW vs $\Lambda$CDM")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: per-z fractional product suppression (sign axis) + bindability threshold band
    ax = axes[1]  # (local)
    ax.axhline(0, color="k", lw=0.8)
    ax.plot(z, r["delta_z_pct"], "d-", color="tab:red", label="FW suppression $\\delta(z)$")
    # shaded DESI-5yr +/- 1 sigma bindability envelope (as a fractional band)
    ax.fill_between(z, -r["sig_d5_dense"] * 100.0, r["sig_d5_dense"] * 100.0,
                    color="tab:green", alpha=0.15, label="DESI-5yr $\\pm1\\sigma$ band")
    z_at = r["z_at_max_bind_d5"]  # (local)
    ax.axvline(z_at, color="gray", ls=":", alpha=0.6)
    ax.annotate(f"max bind {r['max_bind_d5']:.3f}$\\sigma$ @ z={z_at:g}",
                xy=(z_at, r["delta_z_pct"][int(np.argmax(r['bind_ratio_d5']))]),
                xytext=(0.55, -3.5), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="gray"))
    ax.set_xlabel("z"); ax.set_ylabel(r"$(f\sigma_8^{FW}-f\sigma_8^{\Lambda})/f\sigma_8^{\Lambda}$ [%]")
    ax.set_title(f"Growth suppression (sign={r['sign_verdict']}, {r['n_negative']}/{r['n_z']} neg)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 3: S8 placement vs Planck/lensing band
    ax = axes[2]  # (local)
    # band
    ax.axhspan(r["S8_band_lo"], r["S8_band_hi"], color="tab:olive", alpha=0.12,
               label=f"target band [{r['S8_band_lo']}, {r['S8_band_hi']}]")
    ax.axhline(r["S8_planck"], color="tab:purple", ls="--", lw=1.3, label=f"Planck $S_8\\approx${r['S8_planck']}")
    ax.axhline(r["S8_kids"], color="tab:cyan", ls="--", lw=1.3, label=f"KiDS $S_8\\approx${r['S8_kids']}")
    ax.axhline(r["S8_des"], color="tab:blue", ls=":", lw=1.0, alpha=0.7, label=f"DES $S_8\\approx${r['S8_des']}")
    labels = [r"FW (a$_2$ growth)", r"$\Lambda$CDM (Planck)", "FW (O-Z headline)"]  # (local)
    vals = [r["S8_FW"], r["S8_LCDM"], r["S8_OZ_headline"]]  # (local)
    colors = ["tab:red", "tab:blue", "tab:orange"]  # (local)
    bars = ax.bar(labels, vals, color=colors, alpha=0.85, width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.003, f"{v:.4f}",
                ha="center", va="bottom", fontsize=9)
    ax.set_ylim(0.74, 0.85)
    ax.set_ylabel(r"$S_8 = \sigma_8\sqrt{\Omega_m/0.3}$")
    ax.set_title(f"$S_8$ placement (mag={r['magnitude_verdict']}, composite={r['composite']})")
    ax.legend(fontsize=7, loc="lower left"); ax.grid(alpha=0.3, axis="y")

    fig.suptitle(r"INV13-W2-2 — GGE growth-suppression $f\sigma_8(z)$ + $S_8$-tension band test",
                 fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "track": "investigation",
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
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # canonical-anchor reproduction report
    print("=== canonical-anchor reproduction (cross-check) ===")
    print(f"  f_FW(z=0)   computed={r['f_FW_z0']:.10f}  canonical={r['f_FW_canonical']:.10f}  "
          f"diff={r['f_FW_z0'] - r['f_FW_canonical']:+.2e}")
    print(f"  f_LCDM(z=0) computed={r['f_LCDM_z0']:.10f}  canonical={r['f_LCDM_canonical']:.10f}  "
          f"diff={r['f_LCDM_z0'] - r['f_LCDM_canonical']:+.2e}")
    print(f"  bare_f_supp computed={r['bare_f_supp_pct']:.4f}%  canonical={r['bare_f_supp_canonical_pct']:.4f}%")
    print(f"  product_supp_max upstream={r['product_supp_max_pct_upstream']:.4f}% @ z={r['z_at_product_max_upstream']:g}  "
          f"canonical={r['product_supp_max_pct_canonical']:.4f}%")
    print(f"  S8_FW computed={r['S8_FW']:.4f}  upstream={r['S8_FW_upstream']:.4f}  "
          f"diff={r['S8_FW'] - r['S8_FW_upstream']:+.2e}")
    print(f"  S8_LCDM computed={r['S8_LCDM']:.4f}  upstream={r['S8_LCDM_upstream']:.4f}  "
          f"diff={r['S8_LCDM'] - r['S8_LCDM_upstream']:+.2e}")
    print()
    print("=== SOURCING DISCIPLINE (channel-distinct sigma8) ===")
    print(f"  growth normalization sigma8_growth_a2 = {r['sigma8_growth_a2']:.5f}  (a2 channel; FEEDS fsigma8 -- USED)")
    print(f"  headline sigma8_OZ_50               = {r['sigma8_OZ_50']:.5f}  (O-Z channel; HEADLINE -- NOT used for growth)")
    print(f"  inter-channel spread = {abs(r['sigma8_OZ_50']-r['sigma8_growth_a2'])/r['sigma8_growth_a2']*100:.3f}%  (NOT a single-channel band)")
    print()
    print("=== dense f*sigma8(z) curve (16-pt grid) ===")
    print(f"  z_grid       = {np.array2string(r['z_grid'], precision=2)}")
    print(f"  fsig8_FW     = {np.array2string(r['fsig8_FW_z'], precision=4)}")
    print(f"  fsig8_LCDM   = {np.array2string(r['fsig8_LCDM_z'], precision=4)}")
    print(f"  delta_z_pct  = {np.array2string(r['delta_z_pct'], precision=3)}")
    print(f"  coherent_negative = {r['n_negative']}/{r['n_z']}  (sign_verdict={r['sign_verdict']})")
    print()
    print("=== S8-tension placement ===")
    print(f"  S8_FW = {r['S8_FW']:.4f}  band [{r['S8_band_lo']},{r['S8_band_hi']}]: {'IN' if r['S8_in_band'] else 'OUT'} "
          f"(dist to upper {r['S8_dist_to_hi']:+.4f}, to lower {r['S8_dist_to_lo']:+.4f})")
    print(f"  S8_LCDM = {r['S8_LCDM']:.4f} ; S8 below Planck? {r['S8_below_planck']}")
    print(f"  S8_FW vs Planck(0.832): {r['S8_vs_planck_pct']:+.2f}% ; vs KiDS(0.759): {r['S8_vs_kids_pct']:+.2f}%")
    print(f"  band fractional position (0=lensing edge, 1=Planck edge): {r['band_frac_position']:.2f}")
    print(f"  magnitude_verdict = {r['magnitude_verdict']} {('('+r['magnitude_verdict_note']+')') if r['magnitude_verdict_note'] else ''}")
    print()
    print("=== DESI/Euclid bindability ===")
    print(f"  DESI-5yr max bind ratio = {r['max_bind_d5']:.3f} @ z={r['z_at_max_bind_d5']:g}  "
          f"({r['n_bindable_d5']} bins >= {r['bindability_thr']:g})")
    print(f"  Euclid   max bind ratio = {r['max_bind_eu']:.3f}  ({r['n_bindable_eu']} bins >= {r['bindability_thr']:g})")
    print(f"  bindable (DESI-5yr headline)? {r['bindable']}")
    print()
    print("=== K_pivot-localization corollary (NON-gating) ===")
    print(f"  available? {r['kpivot_localization_available']}  "
          f"(growth success at k~{r['k_band_lo']}-{r['k_band_hi']} h/Mpc, distinct from CMB pivot)")
    print(f"  companion Row #72 first-sound ring: A_FS={r['A_FS_ring']:.3f} @ k1={r['k1_ring']:.4f} Mpc^-1")
    print()

    make_plot(r)
    print(f"  plot  -> {OUT_PNG.name}")

    np.savez(OUT_NPZ, **{k: v for k, v in r.items() if k != "value"},
             value=r["value"])
    print(f"  data  -> {OUT_NPZ.name}")
    print()

    verdict = r["composite"]  # (local)
    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    note = (f"S8_FW={r['S8_FW']:.4f} in-band[{r['S8_band_lo']},{r['S8_band_hi']}]={r['S8_in_band']} "
            f"(below Planck {r['S8_vs_planck_pct']:+.2f}%, above KiDS {r['S8_vs_kids_pct']:+.2f}%, "
            f"band-pos {r['band_frac_position']:.2f}); suppression sign-PASS {r['n_negative']}/{r['n_z']} neg; "
            f"DESI-5yr bindable={r['bindable']} (max {r['max_bind_d5']:.3f}sigma@z{r['z_at_max_bind_d5']:g})")  # (local)
    extra = [
        f"# INV13-W2-2 supp envelope: delta_z in [{r['delta_z_pct'].min():.3f}%,{r['delta_z_pct'].max():.3f}%] "
        f"product_max={r['product_supp_max_pct_upstream']:.4f}%@z{r['z_at_product_max_upstream']:g} "
        f"bare_f={r['bare_f_supp_pct']:.4f}% (canonical -4.058%/-0.311%)",
        f"# INV13-W2-2 S8: FW={r['S8_FW']:.4f} LCDM={r['S8_LCDM']:.4f} OZ-headline={r['S8_OZ_headline']:.4f} "
        f"(growth sigma8={r['sigma8_growth_a2']:.5f} USED, NOT OZ {r['sigma8_OZ_50']:.5f}); "
        f"bindable_DESI5yr={r['n_bindable_d5']}bins Euclid={r['n_bindable_eu']}bins; "
        f"Kpivot-localization-available={r['kpivot_localization_available']}",
    ]  # (local)
    print_verdict_payload(verdict, r["value"], audit_sha, content_sha,
                          sign_verdict=r["sign_verdict"],
                          magnitude_verdict=r["magnitude_verdict"],
                          regime_verdict=r["regime_verdict"],
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(sign={r['sign_verdict']} mag={r['magnitude_verdict']} regime={r['regime_verdict']}; "
          f"wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
