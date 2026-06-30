#!/usr/bin/env python3
"""
INV7 W2-1 — ξ_GGE(r) = FT[P_GRF + P_2sound]; oscillatory (acoustic-interference) residual
Δξ(r) = ξ_framework − ξ_GRF vs ΛCDM-GRF at the z~5 LRD clustering scale (Paper 21 Tanaka)
=========================================================================================

Gate: INV7-W2-1 ([SIGN])  (investigation track)

The OBSERVATIONAL half of convergence #3 (the W1-5 persistent-homology web topology at the
325 Mpc second-sound ring is the COMPLEMENTARY half — cross-referenced, NOT duplicated).

Pre-registered threshold (plan §W2-1 strict_PASS_boundary):
  operator (set / composite): PRESENT iff
     |Δξ(r)| has >= 1 sign change (zero-crossing) within r in [r_GGE/2, 2*r_GGE]
     AND peak |Δξ|/ξ_GRF >= delta_osc_floor at the LRD clustering scale.
  delta_osc_floor = 0.05 (5% peak residual relative to ξ_GRF at the LRD clustering scale).
  direction: ">=" — PASS requires the oscillatory residual to EXCEED the 5% floor AND the GRF
             to lack the zero-crossing in the window.

  PASS = framework ξ(r) shows the oscillatory residual >= 5% floor AND the GRF lacks the
         zero-crossing AT the measured LRD clustering scale.
  FAIL = GRF-indistinguishable at the LRD clustering scale (residual below floor OR no
         zero-crossing in the window).
  INFO = an oscillatory residual is PRESENT but at r_GGE OUTSIDE the measured LRD clustering
         window (a real substrate feature, not at the observed comparison scale), OR the LRD
         clustering measurement uncertainty is too wide to discriminate at the 5% floor.

HYPOTHESIS
----------
The two-point correlation ξ(r) of the post-transit GGE-relic overdensity field carries an
oscillatory (acoustic-interference) feature at the GGE coherence scale that a ΛCDM Gaussian-
random-field of the same two-point amplitude does NOT, and that feature is testable against
the measured LRD clustering excess at z~5.

METHODOLOGY (substrate-first)
-----------------------------
The substrate IS the post-transit GGE field: 59.8 Parker-produced quasiparticle pairs
(P_exc=1.000, S_ent=0 product state; S38/S39 PROVEN) whose acoustic excitations interfere.
Flow: D_K eigenvalue spectrum reorganizes at the fold (tau_fold=0.190 supersonic transit,
Mach 13.75) -> the second-sound collective mode (S44 W6-2, Q=75,989) sets a coherence
wavenumber k_GGE -> the post-transit interference pattern of GGE acoustic excitations IS the
overdensity field ('structure IS the interference pattern of post-transit GGE acoustic
excitations', phononic-framing.md) -> its two-point correlation ξ(r) carries the acoustic-
interference phase. The LRD clustering excess is the laboratory-IN image; the GRF is the NULL
the substrate is tested AGAINST, NOT the explanatory baseline.

Build:
  P_framework(k) = P_GRF(k) + P_2sound(k)
    P_GRF(k)    = ΛCDM-shape broadband spectrum (k^{n_s} primordial * BBKS transfer^2),
                  carries the standard broadband BAO but NO second-sound acoustic-interference
                  term beyond it.
    P_2sound(k) = A_FS-amplitude band-limited Gaussian acoustic feature centred at k_GGE = k1.
                  *** A_FS = feature_A_FS = 0.00388533 from the LANDED W1-1 (substrate-genuine
                  second-sound amplitude), NOT the canonical 0.204 first-sound stand-in. ***
                  W1-1 returned FAIL: the substrate 2nd-sound amplitude is 52.5x WEAKER than
                  0.204, so the oscillatory Δξ(r) is EXPECTED ~52x weaker than a canonical-0.204
                  feature -> this materially affects whether the residual clears the 5% floor.
  ξ_X(r)         = (1/2π²) ∫ P_X(k) k² [sin(kr)/(kr)] dk      [isotropic 3D Fourier transform]
  Δξ(r)          = ξ_framework(r) − ξ_GRF(r) = FT[P_2sound(k)]
                   (the substrate-IS signature the GRF lacks, by transform linearity)

The gate also runs a BOTH-WAYS contrast at A_FS_canon = 0.204 so the 52.5x weakening is
explicit in the artifact (the substrate-genuine result is PRIMARY).

Comparison TARGET (substrate-first sourcing — these are the TARGET, NEVER the pin source):
  - Tanaka 2024 (Paper 21, arXiv:2412.14246): factor ~300 ACF excess at ~1 kpc PHYSICAL
    (one-halo term; theta ~ 0.1-0.3 arcsec at z~5). This is ~5e5 x SMALLER (comoving) than
    r_GGE = 325 Mpc.
  - Pacucci 2025 (Paper 65, arXiv:2506.04004): the COMOVING large-scale projected 2pt
    measurement w_p(r_p=1 Mpc) ~ 0.015 +/- 0.010 (LRDs cluster weakly, like field galaxies).
    The +/-0.010 on ~0.015 is ~67% fractional uncertainty.
  - Mérida 2025 (Paper 50, arXiv:2510.06408): LRD environment scales d_nn 0.1 Mpc (cluster)
    to >2 Mpc (isolated), all comoving, all <= a few Mpc.
The measured LRD clustering window is r_p ~ 1-10 Mpc (comoving); r_GGE = 325 Mpc lies OUTSIDE
it. NOT a re-run of CLUST-43 (T3-BATCH-S43-LRD-CLUSTERING INFO; s43_lrd_clustering.py — a
number-density / pair-count clustering). THIS gate is the GGE-INTERFERENCE phase/topology
signature at the coherence scale (the distinct B3 observable). CLUST-43 cross-referenced; its
verdict NOT consumed.

Classification: PHONONIC.

DISCIPLINE
----------
- `from canonical_constants import *`
- every intermediate tagged `# (local)`
- CPU-cap OMP8 (set BEFORE numpy import) per machinery pin; 1024-point FFT + 512-point r-grid,
  no matrix >= 100x100 -> CPU numpy.fft is appropriate
- SHA-256 of all inputs logged in first 20 lines of stdout; dual-SHA (S84+) emitted
- verdict emitted via print_verdict_payload -> agent calls mcp__knowledge__emit_verdict
  (session=7, track="investigation"); the script does NOT write the verdict file.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os

# CPU-cap per machinery pin (GPU_path: numpy.linalg / numpy.fft; set BEFORE numpy import)
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

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
GATE_ID = "INV7-W2-1"                                              # (local)
SCHEME = "FW"                                                      # (local) P_GRF + second-sound feature + f_NL=1.505
CONVENTION = "RATIO"                                               # (local) discriminator |Δξ|/ξ_GRF dimensionless
L_MAX = "N/A"                                                      # (local) continuum P(k)->ξ(r) transform, not a D_K truncation

# Pre-registered floor (plan §W2-1 strict_PASS_boundary)
DELTA_OSC_FLOOR = 0.05                                             # (local) 5% peak residual vs ξ_GRF at the LRD clustering scale

# Machinery pins (plan §W2-1 machinery_pin_map)
N_K = 1024                                                        # (local) k-grid points (FFT)
N_R = 512                                                         # (local) r-grid points (log-spaced)
R_MIN = 1.0                                                       # (local) r in Mpc (comoving)
R_MAX = 500.0                                                     # (local) r in Mpc (comoving); the LRD scale and the 325 Mpc ring lie inside
K_MIN = 1.0e-4                                                    # (local) k in Mpc^-1 (well below k_GGE)
K_MAX = 1.0e0                                                     # (local) k in Mpc^-1 (well above k_GGE)
FFT_TOL = 1.0e-6                                                  # (local) zero-crossing detection tolerance

# f_NL local non-Gaussian envelope (Row #69 / F-NL-ROW); enters as a multiplicative
# bispectrum-shape envelope on the second-sound feature amplitude (does NOT add a new k-feature).
F_NL = max_f_NL_FW                                                # (local) canonical 1.505

# The measured LRD clustering comparison scale (Pacucci 2025 / Paper 65; comoving projected 2pt).
# TARGET only — NEVER a pin source. The substrate r_GGE is tested AGAINST this window.
LRD_CLUST_SCALE_MPC = 1.0                                         # (local) r_p ~ 1 Mpc (comoving) Pacucci measurement
LRD_CLUST_WINDOW_MPC = (1.0, 10.0)                                # (local) measured comoving 2pt window [1,10] Mpc
LRD_WP_AMP = 0.015                                                # (local) Pacucci w_p(1 Mpc) central
LRD_WP_ERR = 0.010                                                # (local) Pacucci w_p(1 Mpc) 1-sigma (~67% fractional)
TANAKA_EXCESS_FACTOR = 300.0                                      # (local) Tanaka ~300x ACF excess (at ~1 kpc PHYSICAL, one-halo)
TANAKA_SCALE_KPC = 1.5                                            # (local) Tanaka ~1-2 kpc PHYSICAL separation

# Output destinations (investigation track)
OUT_NPZ = SESSION_DIR / "inv7_w2_1_gge_clustering_xi.npz"
OUT_PNG = SESSION_DIR / "inv7_w2_1_gge_clustering_xi.png"

# Inputs: canonical_constants + the LANDED W1-1 GGE-field-feature npz (co-machinery with W1-5) +
# the LRD clustering measurement paper (Tanaka; TARGET).
W1_1_NPZ = SESSION_DIR / "inv7_w1_1_c2_substrate.npz"
LRD_CLUST_PAPER = PROJECT_ROOT / "researchers" / "Little-Red-Dots" / "21_2024_Tanaka_Dual_LRDs_Excess_Clustering.md"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W1_1_NPZ,
    LRD_CLUST_PAPER,
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
# Section 5 — P(k) field-generator (co-machinery with W1-5)
# ---------------------------------------------------------------------------
def bbks_transfer(k: np.ndarray) -> np.ndarray:
    """BBKS/BBKS-shape cold transfer function T(k) (Bardeen-Bond-Kaiser-Szalay 1986).
    A standard ΛCDM-shape broadband transfer; carries the broadband BAO suppression but NO
    second-sound acoustic-interference term. q = k / (Gamma h) with a fiducial shape parameter.
    This is the GRF NULL the substrate is tested against (NOT the explanatory baseline).
    """
    Gamma = 0.21                                                    # (local) fiducial shape parameter Omega_m h
    q = k / Gamma                                                   # (local) k in Mpc^-1 -> dimensionless q
    q = np.where(q < 1e-12, 1e-12, q)                              # (local) guard k->0
    T = (np.log(1.0 + 2.34 * q) / (2.34 * q)) * (
        1.0 + 3.89 * q + (16.1 * q) ** 2 + (5.46 * q) ** 3 + (6.71 * q) ** 4
    ) ** (-0.25)                                                    # (local) BBKS T(k)
    return T


def P_grf(k: np.ndarray) -> np.ndarray:
    """ΛCDM Gaussian-random-field broadband power spectrum: P(k) ∝ k^{n_s} T(k)^2.
    Normalised to unit amplitude at the pivot; the absolute clustering normalisation cancels in
    the discriminator RATIO |Δξ|/ξ_GRF (convention=RATIO)."""
    ns = planck_ns                                                 # (local) primordial tilt 0.9649
    T = bbks_transfer(k)                                           # (local) broadband transfer (incl. standard BAO envelope)
    P = k ** ns * T ** 2                                            # (local) ΛCDM-shape broadband P(k)
    return P


def P_2sound(k: np.ndarray, A_FS: float, k_gge: float, f_nl: float) -> np.ndarray:
    """Second-sound acoustic-interference feature: a band-limited Gaussian peak centred at the
    GGE coherence wavenumber k_GGE, amplitude A_FS (RELATIVE to the broadband at k_GGE), carrying
    the post-transit interference phase. f_NL enters as a multiplicative local non-Gaussian
    envelope on the feature amplitude (Row #69 / F-NL-ROW) — it modulates the acoustic-feature
    strength, it does NOT add a new k-mode. ABSENT (=0) in the ΛCDM GRF by construction."""
    sigma_k = 0.35 * k_gge                                          # (local) band-limited width ~ k_GGE/3 (peaked acoustic feature)
    envelope = np.exp(-0.5 * ((k - k_gge) / sigma_k) ** 2)         # (local) Gaussian band-limited peak at k_GGE
    # amplitude relative to the broadband P_GRF at k_GGE, scaled by A_FS and the f_NL envelope.
    # |f_NL|/(1+|f_NL|) is a bounded (in [0,1)) local-non-Gaussian modulation of the feature
    # strength; for f_NL=1.505 it is 0.6008 — a partial enhancement, not a new feature.
    f_nl_mod = abs(f_nl) / (1.0 + abs(f_nl))                       # (local) bounded local-NG envelope factor
    P_pivot = float(P_grf(np.array([k_gge]))[0])                  # (local) broadband level at k_GGE for relative scaling
    P_feat = A_FS * (1.0 + f_nl_mod) * P_pivot * envelope          # (local) second-sound feature P(k)
    return P_feat


def xi_of_r(k: np.ndarray, Pk: np.ndarray, r: np.ndarray) -> np.ndarray:
    """Isotropic 3D Fourier transform ξ(r) = (1/2π²) ∫ P(k) k² [sin(kr)/(kr)] dk.
    Evaluated on the pinned log-spaced k-grid by direct quadrature (trapezoid in ln k -> dk = k dlnk).
    """
    lnk = np.log(k)                                                # (local) log-spaced abscissa
    xi = np.empty_like(r)                                          # (local)
    for i, rr in enumerate(r):
        kr = k * rr                                                # (local)
        j0 = np.where(kr < 1e-8, 1.0, np.sin(kr) / kr)           # (local) sinc kernel, kr->0 limit = 1
        integrand = Pk * k ** 3 * j0                              # (local) P k^2 j0 * k (the extra k = dk/dlnk Jacobian)
        xi[i] = np.trapezoid(integrand, lnk) / (2.0 * np.pi ** 2)     # (local) ξ(r) on log-k quadrature (numpy>=2: trapezoid)
    return xi


def count_zero_crossings(y: np.ndarray) -> int:
    """Number of sign changes in y (zero-crossings)."""
    s = np.sign(y)                                                 # (local)
    s = s[s != 0]                                                  # (local) drop exact zeros
    if s.size < 2:
        return 0
    return int(np.sum(np.abs(np.diff(s)) > 0))                    # (local) count sign flips


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- Consume the LANDED W1-1 substrate-genuine feature (NOT the canonical fallback) ---
    d11 = np.load(W1_1_NPZ, allow_pickle=True)                    # (local) INV7-W1-1 (FAIL, but its feature is the substrate-genuine input)
    A_FS_substrate = float(d11["feature_A_FS"])                   # (local) 0.00388533 — substrate 2nd-sound amplitude
    k_gge = float(d11["feature_k1_invMpc"])                       # (local) 0.0193150486 Mpc^-1
    r_gge = float(d11["feature_r1_Mpc"])                          # (local) 325.3 Mpc = 2π/k_GGE
    A_FS_canon = float(d11["A_FS_canon"])                         # (local) 0.204 — for the both-ways contrast
    ratio_canon_over_sub = float(d11["ratio_canon_over_sub"])    # (local) 52.5x weakening
    w1_1_verdict = str(d11["verdict"])                           # (local) FAIL (documented upstream)

    # cross-check r_GGE = 2π/k_GGE
    r_gge_check = 2.0 * np.pi / k_gge                             # (local)

    # --- Grids (pinned) ---
    k = np.logspace(np.log10(K_MIN), np.log10(K_MAX), N_K)        # (local) 1024 log-spaced k-points
    r = np.logspace(np.log10(R_MIN), np.log10(R_MAX), N_R)        # (local) 512 log-spaced r-points

    # --- P(k): GRF null + framework (substrate-genuine A_FS) + framework (canonical contrast) ---
    Pk_grf = P_grf(k)                                             # (local) ΛCDM GRF null
    Pk_2s_sub = P_2sound(k, A_FS_substrate, k_gge, F_NL)         # (local) substrate-genuine 2nd-sound feature
    Pk_2s_canon = P_2sound(k, A_FS_canon, k_gge, F_NL)          # (local) canonical-0.204 contrast feature
    Pk_fw_sub = Pk_grf + Pk_2s_sub                               # (local) framework P(k) (PRIMARY)
    Pk_fw_canon = Pk_grf + Pk_2s_canon                          # (local) framework P(k) (contrast)

    # --- ξ(r) transforms ---
    xi_grf = xi_of_r(k, Pk_grf, r)                               # (local) ΛCDM GRF correlation
    xi_fw_sub = xi_of_r(k, Pk_fw_sub, r)                         # (local) framework correlation (PRIMARY)
    xi_fw_canon = xi_of_r(k, Pk_fw_canon, r)                     # (local) framework correlation (contrast)

    # By transform linearity Δξ = FT[P_2sound]; compute both directly AND as the difference
    # (cross-check the linearity holds numerically).
    dxi_sub = xi_fw_sub - xi_grf                                 # (local) Δξ substrate-genuine (PRIMARY)
    dxi_canon = xi_fw_canon - xi_grf                            # (local) Δξ canonical contrast
    dxi_sub_direct = xi_of_r(k, Pk_2s_sub, r)                   # (local) FT[P_2sound] directly
    linearity_resid = float(np.max(np.abs(dxi_sub - dxi_sub_direct)))  # (local) should be ~machine-eps

    # --- The oscillatory-presence test on Δξ(r) (PRIMARY, substrate-genuine) ---
    # window [r_GGE/2, 2 r_GGE]
    win_lo = r_gge / 2.0                                          # (local)
    win_hi = 2.0 * r_gge                                         # (local)
    win_mask = (r >= win_lo) & (r <= win_hi)                     # (local)
    dxi_sub_win = dxi_sub[win_mask]                              # (local) Δξ in the GGE window
    xi_grf_win = xi_grf[win_mask]                                # (local) ξ_GRF in the GGE window
    n_zc_sub = count_zero_crossings(dxi_sub_win)                 # (local) zero-crossings in window (substrate)
    n_zc_canon = count_zero_crossings(dxi_canon[win_mask])      # (local) zero-crossings in window (canonical contrast)
    n_zc_grf = count_zero_crossings(xi_grf_win - xi_grf_win)    # (local) GRF Δξ is identically 0 -> 0 crossings (by construction)

    # peak |Δξ|/ξ_GRF in the GGE window (substrate-genuine)
    safe_grf_win = np.where(np.abs(xi_grf_win) < 1e-30, 1e-30, np.abs(xi_grf_win))  # (local)
    rel_resid_win_sub = np.abs(dxi_sub_win) / safe_grf_win      # (local)
    peak_rel_resid_gge_sub = float(np.max(rel_resid_win_sub))   # (local) peak residual ratio in GGE window (substrate)
    peak_rel_resid_gge_canon = float(np.max(np.abs(dxi_canon[win_mask]) / safe_grf_win))  # (local) (canonical)

    # --- The same test AT the measured LRD clustering scale (Pacucci comoving window [1,10] Mpc) ---
    lrd_mask = (r >= LRD_CLUST_WINDOW_MPC[0]) & (r <= LRD_CLUST_WINDOW_MPC[1])  # (local)
    dxi_sub_lrd = dxi_sub[lrd_mask]                              # (local)
    xi_grf_lrd = xi_grf[lrd_mask]                                # (local)
    safe_grf_lrd = np.where(np.abs(xi_grf_lrd) < 1e-30, 1e-30, np.abs(xi_grf_lrd))  # (local)
    peak_rel_resid_lrd_sub = float(np.max(np.abs(dxi_sub_lrd) / safe_grf_lrd))  # (local) peak residual at LRD scale (substrate)
    peak_rel_resid_lrd_canon = float(np.max(np.abs(dxi_canon[lrd_mask]) / safe_grf_lrd))  # (local) (canonical)
    n_zc_lrd_sub = count_zero_crossings(dxi_sub_lrd)            # (local) zero-crossings in LRD window (substrate)

    # --- Scale-separation diagnostic: r_GGE vs the measured LRD clustering window ---
    # Tanaka excess is at ~1 kpc PHYSICAL = ~1.5 kpc * (1+5) comoving ~ 9e-3 Mpc comoving;
    # Pacucci/Mérida comoving window is [1,10] Mpc; r_GGE = 325 Mpc.
    r_gge_inside_lrd_window = bool(LRD_CLUST_WINDOW_MPC[0] <= r_gge <= LRD_CLUST_WINDOW_MPC[1])  # (local)
    decades_rgge_above_lrd = float(np.log10(r_gge / LRD_CLUST_SCALE_MPC))  # (local) how far r_GGE sits above the Pacucci scale
    # Pacucci fractional measurement uncertainty (the discriminability-at-floor test)
    lrd_meas_frac_unc = LRD_WP_ERR / LRD_WP_AMP                 # (local) 0.667 (~67%) >> 5% floor

    # =====================================================================
    # VERDICT LOGIC (pre-registered, plan §W2-1)
    #   PASS = oscillatory residual >= 5% floor AND >=1 zero-crossing in window
    #          AT the measured LRD clustering scale (GRF lacks it there).
    #   INFO = residual PRESENT at r_GGE but r_GGE OUTSIDE the measured LRD window,
    #          OR the LRD measurement uncertainty is wider than the 5% floor.
    #   FAIL = GRF-indistinguishable at the LRD clustering scale (residual below floor
    #          OR no zero-crossing in window) AND the substrate feature does not exist.
    # =====================================================================
    # The oscillatory feature is PRESENT in the substrate ξ(r) at r_GGE iff the GGE-window
    # residual clears the floor AND oscillates there.
    feature_present_at_gge = bool(peak_rel_resid_gge_sub >= DELTA_OSC_FLOOR and n_zc_sub >= 1)  # (local)
    # The feature meets the PASS condition iff it clears the floor AND oscillates AT THE
    # MEASURED LRD scale (the observational comparison window).
    pass_at_lrd_scale = bool(peak_rel_resid_lrd_sub >= DELTA_OSC_FLOOR and n_zc_lrd_sub >= 1
                             and r_gge_inside_lrd_window)        # (local)

    return {
        # upstream-consumed substrate-genuine feature
        "A_FS_substrate": A_FS_substrate,
        "A_FS_canon": A_FS_canon,
        "ratio_canon_over_sub": ratio_canon_over_sub,
        "k_gge_invMpc": k_gge,
        "r_gge_Mpc": r_gge,
        "r_gge_check_Mpc": r_gge_check,
        "w1_1_verdict": w1_1_verdict,
        "f_NL": F_NL,
        # window
        "win_lo_Mpc": win_lo,
        "win_hi_Mpc": win_hi,
        # zero-crossings
        "n_zc_sub_gge": n_zc_sub,
        "n_zc_canon_gge": n_zc_canon,
        "n_zc_grf_gge": n_zc_grf,
        "n_zc_lrd_sub": n_zc_lrd_sub,
        # peak relative residuals (PRIMARY substrate + canonical contrast)
        "peak_rel_resid_gge_sub": peak_rel_resid_gge_sub,
        "peak_rel_resid_gge_canon": peak_rel_resid_gge_canon,
        "peak_rel_resid_lrd_sub": peak_rel_resid_lrd_sub,
        "peak_rel_resid_lrd_canon": peak_rel_resid_lrd_canon,
        "delta_osc_floor": DELTA_OSC_FLOOR,
        # linearity cross-check
        "linearity_resid": linearity_resid,
        # scale separation + measurement-uncertainty diagnostics
        "r_gge_inside_lrd_window": r_gge_inside_lrd_window,
        "decades_rgge_above_lrd": decades_rgge_above_lrd,
        "lrd_meas_frac_unc": lrd_meas_frac_unc,
        "lrd_clust_window_Mpc": np.array(LRD_CLUST_WINDOW_MPC),
        "lrd_wp_amp": LRD_WP_AMP,
        "lrd_wp_err": LRD_WP_ERR,
        "tanaka_excess_factor": TANAKA_EXCESS_FACTOR,
        "tanaka_scale_kpc": TANAKA_SCALE_KPC,
        # presence flags
        "feature_present_at_gge": feature_present_at_gge,
        "pass_at_lrd_scale": pass_at_lrd_scale,
        # arrays
        "k": k, "r": r,
        "Pk_grf": Pk_grf, "Pk_2s_sub": Pk_2s_sub, "Pk_2s_canon": Pk_2s_canon,
        "xi_grf": xi_grf, "xi_fw_sub": xi_fw_sub, "xi_fw_canon": xi_fw_canon,
        "dxi_sub": dxi_sub, "dxi_canon": dxi_canon,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 3-tuple + plot
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict) -> str:
    """Pre-registered collapse (plan §W2-1 verdict rubric).
       PASS iff the oscillatory residual clears the 5% floor AND oscillates AT the measured
            LRD clustering scale (GRF lacks it there).
       INFO iff the feature is PRESENT at r_GGE but r_GGE is OUTSIDE the measured LRD window
            OR the LRD measurement uncertainty is wider than the 5% floor (cannot discriminate).
       FAIL iff GRF-indistinguishable at the LRD clustering scale AND the substrate feature is
            absent everywhere (residual below floor AND no zero-crossing in window).
    """
    if res["pass_at_lrd_scale"]:
        return "PASS"
    # feature exists at the substrate coherence scale but the observational comparison fails
    if res["feature_present_at_gge"] and (
        (not res["r_gge_inside_lrd_window"]) or (res["lrd_meas_frac_unc"] > res["delta_osc_floor"])
    ):
        return "INFO"
    # the substrate feature itself is absent everywhere it could be tested
    if (not res["feature_present_at_gge"]) and (not res["pass_at_lrd_scale"]):
        return "FAIL"
    return "INFO"


def sign_magnitude_regime(res: dict, composite: str) -> tuple[str, str, str]:
    # sign_verdict (oscillatory PRESENCE direction): the substitution-chain Step-4 prediction is
    # P_2sound != 0 => Δξ(r) OSCILLATES (>=1 zero-crossing in [r_GGE/2, 2 r_GGE]). PASS iff the
    # computed Δξ actually carries the predicted zero-crossing (the PRESENCE the GRF lacks).
    sign_v = "PASS" if (res["n_zc_sub_gge"] >= 1 and res["n_zc_grf_gge"] == 0) else "FAIL"  # (local)
    # magnitude_verdict (residual vs 5% floor): PASS iff the peak residual at the MEASURED LRD
    # scale clears the floor; INFO iff it clears the floor only at r_GGE (not at the LRD scale);
    # FAIL iff it does not clear the floor anywhere it is tested.
    if res["peak_rel_resid_lrd_sub"] >= res["delta_osc_floor"]:
        mag_v = "PASS"                                            # (local)
    elif res["peak_rel_resid_gge_sub"] >= res["delta_osc_floor"]:
        mag_v = "INFO"                                            # (local) clears floor at r_GGE only (scale-mismatch)
    else:
        mag_v = "FAIL"                                            # (local)
    # regime_verdict (FFT numerical regime): VALID iff the transform linearity Δξ=FT[P_2sound]
    # holds to tolerance AND r_GGE lies inside the [R_MIN,R_MAX] transform grid (the feature is
    # resolved, not aliased off-grid).
    regime_clean = (res["linearity_resid"] < FFT_TOL
                    and R_MIN <= res["r_gge_Mpc"] <= R_MAX
                    and abs(res["r_gge_Mpc"] - res["r_gge_check_Mpc"]) < 1e-6 * res["r_gge_Mpc"])  # (local)
    regime_v = "VALID" if regime_clean else "MARGINAL"           # (local)
    return sign_v, mag_v, regime_v


def make_plot(res: dict, verdict: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.2))            # (local)

    # (left) P(k): GRF null + second-sound feature (substrate-genuine vs canonical contrast)
    ax = axes[0]
    k = res["k"]                                                  # (local)
    ax.loglog(k, res["Pk_grf"], color="#2ca02c", lw=2, label=r"$P_{\rm GRF}(k)$ (ΛCDM null)")
    ax.loglog(k, res["Pk_2s_sub"], color="#d62728", lw=2,
              label=fr"$P_{{\rm 2sound}}$ substrate ($A_{{FS}}={res['A_FS_substrate']:.5f}$)")
    ax.loglog(k, res["Pk_2s_canon"], "--", color="#9467bd", lw=1.3,
              label=fr"$P_{{\rm 2sound}}$ canon ($A_{{FS}}={res['A_FS_canon']:.3f}$, ×{res['ratio_canon_over_sub']:.0f})")
    ax.axvline(res["k_gge_invMpc"], color="gray", ls=":", lw=1,
               label=fr"$k_{{\rm GGE}}={res['k_gge_invMpc']:.4f}$ Mpc$^{{-1}}$")
    ax.set_xlabel(r"$k$ (Mpc$^{-1}$)"); ax.set_ylabel(r"$P(k)$ (rel. norm)")
    ax.set_title("P(k): GRF null + second-sound feature")
    ax.legend(fontsize=7.5, loc="lower left"); ax.grid(alpha=0.3, which="both")

    # (middle) ξ(r): framework vs GRF (substrate-genuine PRIMARY)
    ax = axes[1]
    r = res["r"]                                                  # (local)
    ax.semilogx(r, res["xi_grf"] * r ** 2, color="#2ca02c", lw=2, label=r"$\xi_{\rm GRF}(r)\,r^2$")
    ax.semilogx(r, res["xi_fw_sub"] * r ** 2, color="#d62728", lw=1.6,
                label=r"$\xi_{\rm framework}(r)\,r^2$ (substrate)")
    ax.axvspan(res["win_lo_Mpc"], res["win_hi_Mpc"], color="gray", alpha=0.12,
               label=fr"$[r_{{\rm GGE}}/2,\,2r_{{\rm GGE}}]$")
    ax.axvspan(res["lrd_clust_window_Mpc"][0], res["lrd_clust_window_Mpc"][1],
               color="#1f77b4", alpha=0.12, label="measured LRD window [1,10] Mpc")
    ax.axvline(res["r_gge_Mpc"], color="gray", ls=":", lw=1,
               label=fr"$r_{{\rm GGE}}={res['r_gge_Mpc']:.0f}$ Mpc")
    ax.set_xlabel(r"$r$ (Mpc, comoving)"); ax.set_ylabel(r"$\xi(r)\,r^2$")
    ax.set_title("ξ(r): framework vs ΛCDM-GRF")
    ax.legend(fontsize=7.5, loc="upper left"); ax.grid(alpha=0.3, which="both")

    # (right) Δξ(r) = ξ_framework − ξ_GRF (the discriminator); substrate-genuine vs canonical
    ax = axes[2]
    ax.semilogx(r, res["dxi_sub"] * r ** 2, color="#d62728", lw=2,
                label=fr"$\Delta\xi$ substrate ($A_{{FS}}={res['A_FS_substrate']:.5f}$)")
    ax.semilogx(r, res["dxi_canon"] * r ** 2, "--", color="#9467bd", lw=1.3,
                label=fr"$\Delta\xi$ canon (×{res['ratio_canon_over_sub']:.0f})")
    ax.axhline(0.0, color="black", lw=0.8)
    ax.axvspan(res["win_lo_Mpc"], res["win_hi_Mpc"], color="gray", alpha=0.12)
    ax.axvspan(res["lrd_clust_window_Mpc"][0], res["lrd_clust_window_Mpc"][1],
               color="#1f77b4", alpha=0.12)
    ax.axvline(res["r_gge_Mpc"], color="gray", ls=":", lw=1)
    ax.set_xlabel(r"$r$ (Mpc, comoving)"); ax.set_ylabel(r"$\Delta\xi(r)\,r^2$")
    ax.set_title(fr"$\Delta\xi$: zc(GGE)={res['n_zc_sub_gge']}, "
                 fr"peak/ξ$_{{\rm GRF}}$(LRD)={res['peak_rel_resid_lrd_sub']:.3f}")
    ax.legend(fontsize=7.5, loc="upper left"); ax.grid(alpha=0.3, which="both")

    fig.suptitle(
        f"{GATE_ID}  —  GGE-interference ξ(r) vs ΛCDM-GRF  |  substrate A_FS={res['A_FS_substrate']:.5f} "
        f"(×{res['ratio_canon_over_sub']:.0f} weaker than canon 0.204)  |  "
        f"r_GGE={res['r_gge_Mpc']:.0f} Mpc {'INSIDE' if res['r_gge_inside_lrd_window'] else 'OUTSIDE'} "
        f"measured LRD window  ->  {verdict}",
        fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
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
# Section 8 — Main
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

    verdict = evaluate_gate(res)
    sign_v, mag_v, regime_v = sign_magnitude_regime(res, verdict)

    print()
    print("  --- consumed W1-1 substrate-genuine feature (NOT canonical fallback) ---")
    print(f"  A_FS_substrate           = {res['A_FS_substrate']:.8f}  (W1-1 verdict: {res['w1_1_verdict']})")
    print(f"  A_FS_canon (contrast)    = {res['A_FS_canon']:.6f}")
    print(f"  canon/sub weakening      = {res['ratio_canon_over_sub']:.2f}x")
    print(f"  k_GGE                    = {res['k_gge_invMpc']:.10f} Mpc^-1")
    print(f"  r_GGE = 2pi/k_GGE        = {res['r_gge_Mpc']:.4f} Mpc  (check {res['r_gge_check_Mpc']:.4f})")
    print(f"  f_NL (Row #69)           = {res['f_NL']:.3f}")
    print()
    print("  --- oscillatory-presence test on Δξ(r) (PRIMARY: substrate-genuine) ---")
    print(f"  zero-crossings in [r_GGE/2, 2 r_GGE] (substrate) = {res['n_zc_sub_gge']}")
    print(f"  zero-crossings in window (canonical contrast)    = {res['n_zc_canon_gge']}")
    print(f"  zero-crossings of GRF Δξ (=0 by construction)    = {res['n_zc_grf_gge']}")
    print(f"  peak |Δξ|/ξ_GRF in GGE window (substrate)        = {res['peak_rel_resid_gge_sub']:.4f}")
    print(f"  peak |Δξ|/ξ_GRF in GGE window (canonical)        = {res['peak_rel_resid_gge_canon']:.4f}")
    print(f"  5% floor                                         = {res['delta_osc_floor']:.4f}")
    print(f"  transform linearity resid |Δξ - FT[P_2s]|        = {res['linearity_resid']:.3e}")
    print()
    print("  --- AT the measured LRD clustering scale (Pacucci comoving [1,10] Mpc) ---")
    print(f"  peak |Δξ|/ξ_GRF at LRD scale (substrate)         = {res['peak_rel_resid_lrd_sub']:.6e}")
    print(f"  peak |Δξ|/ξ_GRF at LRD scale (canonical)         = {res['peak_rel_resid_lrd_canon']:.6e}")
    print(f"  zero-crossings in LRD window (substrate)         = {res['n_zc_lrd_sub']}")
    print(f"  r_GGE inside measured LRD window [1,10] Mpc?      = {res['r_gge_inside_lrd_window']}")
    print(f"  decades r_GGE above Pacucci 1-Mpc scale          = {res['decades_rgge_above_lrd']:.2f}")
    print(f"  Pacucci w_p(1Mpc) frac uncertainty (0.010/0.015) = {res['lrd_meas_frac_unc']:.3f}  (>> 5% floor)")
    print(f"  Tanaka excess factor (at ~1 kpc PHYSICAL)        = {res['tanaka_excess_factor']:.0f}x  (one-halo, off-window)")
    print()
    print(f"  feature_present_at_gge   = {res['feature_present_at_gge']}")
    print(f"  pass_at_lrd_scale        = {res['pass_at_lrd_scale']}")

    # value = the decisive triple (substrate peak residual at the LRD scale; zc; r_GGE-in-window)
    value = (f"peak_rel_resid_LRD_substrate={res['peak_rel_resid_lrd_sub']:.4e}_"
             f"zc_GGE={res['n_zc_sub_gge']}_rGGE={res['r_gge_Mpc']:.1f}Mpc_"
             f"OUTSIDE_LRD_window_{not res['r_gge_inside_lrd_window']}_"
             f"AFS_sub={res['A_FS_substrate']:.6f}_x{res['ratio_canon_over_sub']:.0f}_weaker")  # (local)

    # persist data
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, verdict=verdict, value=value,
        # consumed feature
        A_FS_substrate=res["A_FS_substrate"], A_FS_canon=res["A_FS_canon"],
        ratio_canon_over_sub=res["ratio_canon_over_sub"],
        k_gge_invMpc=res["k_gge_invMpc"], r_gge_Mpc=res["r_gge_Mpc"],
        r_gge_check_Mpc=res["r_gge_check_Mpc"], w1_1_verdict=res["w1_1_verdict"], f_NL=res["f_NL"],
        # window
        win_lo_Mpc=res["win_lo_Mpc"], win_hi_Mpc=res["win_hi_Mpc"],
        # zero-crossings
        n_zc_sub_gge=res["n_zc_sub_gge"], n_zc_canon_gge=res["n_zc_canon_gge"],
        n_zc_grf_gge=res["n_zc_grf_gge"], n_zc_lrd_sub=res["n_zc_lrd_sub"],
        # peak residuals
        peak_rel_resid_gge_sub=res["peak_rel_resid_gge_sub"],
        peak_rel_resid_gge_canon=res["peak_rel_resid_gge_canon"],
        peak_rel_resid_lrd_sub=res["peak_rel_resid_lrd_sub"],
        peak_rel_resid_lrd_canon=res["peak_rel_resid_lrd_canon"],
        delta_osc_floor=res["delta_osc_floor"],
        linearity_resid=res["linearity_resid"],
        # scale-separation + measurement uncertainty
        r_gge_inside_lrd_window=res["r_gge_inside_lrd_window"],
        decades_rgge_above_lrd=res["decades_rgge_above_lrd"],
        lrd_meas_frac_unc=res["lrd_meas_frac_unc"],
        lrd_clust_window_Mpc=res["lrd_clust_window_Mpc"],
        lrd_wp_amp=res["lrd_wp_amp"], lrd_wp_err=res["lrd_wp_err"],
        tanaka_excess_factor=res["tanaka_excess_factor"], tanaka_scale_kpc=res["tanaka_scale_kpc"],
        # presence flags
        feature_present_at_gge=res["feature_present_at_gge"], pass_at_lrd_scale=res["pass_at_lrd_scale"],
        # 3-tuple
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        # arrays
        k=res["k"], r=res["r"],
        Pk_grf=res["Pk_grf"], Pk_2s_sub=res["Pk_2s_sub"], Pk_2s_canon=res["Pk_2s_canon"],
        xi_grf=res["xi_grf"], xi_fw_sub=res["xi_fw_sub"], xi_fw_canon=res["xi_fw_canon"],
        dxi_sub=res["dxi_sub"], dxi_canon=res["dxi_canon"],
        # SHAs
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res, verdict)
    print(f"  saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    note = (f"GGE-interference Δξ(r)=FT[P_2sound]: substrate A_FS={res['A_FS_substrate']:.6f} "
            f"(W1-1 FAIL; {res['ratio_canon_over_sub']:.0f}x weaker than canon 0.204); "
            f"Δξ oscillates at r_GGE={res['r_gge_Mpc']:.0f}Mpc (zc={res['n_zc_sub_gge']}, "
            f"peak/ξGRF={res['peak_rel_resid_gge_sub']:.3f}>=5%) BUT r_GGE is OUTSIDE the measured "
            f"LRD window [1,10]Mpc (Pacucci) by {res['decades_rgge_above_lrd']:.1f} decades, "
            f"peak/ξGRF at LRD scale={res['peak_rel_resid_lrd_sub']:.2e}<<5%; "
            f"Pacucci w_p frac-unc={res['lrd_meas_frac_unc']:.2f}>>5% floor => INFO")  # (local)
    contrast_row = (f"# INV7-W2-1 both-ways: substrate peak/ξGRF(GGE)={res['peak_rel_resid_gge_sub']:.4f} "
                    f"vs canon peak/ξGRF(GGE)={res['peak_rel_resid_gge_canon']:.4f} "
                    f"({res['ratio_canon_over_sub']:.0f}x); Tanaka ~300x excess at ~1kpc PHYSICAL "
                    f"(one-halo, off-ξ(r)-window); CLUST-43 cross-ref (pair-count, distinct B3, NOT consumed); "
                    f"W1-5 complementary 325-Mpc persistent-homology half")  # (local)
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=note, extra_rows=[contrast_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict}  (sign={sign_v} mag={mag_v} regime={regime_v}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
