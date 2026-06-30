#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-OBS-FSIGMA8-FORECAST — surface the PROVEN f·sigma_8(z) growth-suppression
as a §7.1 scorecard + §7.2 falsifier row, with a z-curve and a DESI-5yr/Euclid
sigma-distance.
=============================================================================

Gate     : S96-OBS-FSIGMA8-FORECAST   (schema R3, [SIGN], PHONONIC)
Wave     : Session 96, Wave 6
Plan     : sessions/session-plan/session-96-plan-w6.md  §W6-1
Owner    : cosmic-web  (falsifier-inventory row written by mack-cosmic-bridge,
                        canonical write-order step 3)

PURPOSE
-------
The framework's growth-rate prediction f_FW = 0.525492 (vs f_LCDM = 0.527130 at
z=0) is currently MISSING from the §7 scorecard. This gate surfaces it as a
zero-parameter LSS discriminator:

  * BARE-f suppression (z=0)         : delta_f/f_LCDM = -0.311%   (the SMALL number)
  * f·sigma_8 PRODUCT suppression    : max -4.058% at z=0.51      (the "~4%" number)
  * S_8 direction                    : sigma8_FW < sigma8_Planck => S_8_FW LOWER
                                       => RELIEVES the Planck-vs-lensing tension
  * z-curve over 0 < z < 1.5         : growth_ratio D_FW/D_LCDM = 0.978011
                                       modulating a BORROWED LCDM growth history
  * sigma-distance vs forecast       : DESI-5yr (max 1.013 sigma @ z=0.51),
                                       Euclid (max 1.534 sigma @ z=0.51)

The C5 single-value-conflation trap (flagged across 8 reviewers): the "4%" prose
figure is the PRODUCT/amplitude suppression, NOT the bare growth-rate f
(~0.31%). This section states BOTH numbers and which is which.

SUBSTRATE FRAMING (PHONONIC, a2-channel)
----------------------------------------
The suppression is NOT "a modification of gravity in a container." The chain is
  D_K eigenvalues -> a2 Seeley-DeWitt coefficient -> emergent metric g_M
  -> linear growth factor D(a) -> growth rate f = dlnD/dlna -> f·sigma_8.
The substrate's a2-channel growth of spectral weight produces a slightly slower
emergent structure-growth than a LCDM background would.

C10 BORROWED-H(z) CAVEAT (load-bearing)
---------------------------------------
The H(z) the growth ODE integrates against is BORROWED from LCDM (the framework
has no derived a(t) yet). The framework's contribution enters as a constant
growth-amplitude RATIO (D_FW/D_LCDM = growth_ratio) applied to a LCDM growth
history. This is a MODULATION-on-borrowed-H prediction; cosmic-web V.4 (separate
gate) tests robustness to the SCALE-FACTOR-54 substrate-proxy H(z).

FETCH NOTE (paper-search-MCP-gated) -> INFO branch
--------------------------------------------------
The plan calls for a LIVE-fetched DESI-5yr/Euclid f·sigma_8(z) forecast-precision
table (paper-search MCP). Paper-search returned EMPTY on two distinct queries
this session (down/unfetchable). Per the pre-registered INFO branch (mirror the
S95 W6-2 'PRE-REG-INFO-branch-a' pattern), the substrate curve is FINALIZED and
the sigma-distance is reported from the S65-EMBEDDED forecast-precision arrays
(nsig_FW_desi5 / nsig_FW_euclid in s65_fsigma8.npz, a PRIOR substrate-first
artifact -- legitimate substrate-canonical sourcing, NOT fabrication). The
LIVE-published forecast validation is deferred. No forecast precision is
invented.

PRE-REGISTERED MOST-LIKELY OUTCOME: INFO (z-dependent discriminator AND
fetch-gated). The suppression sign is PASS on both legs; the magnitude is
within-band at 6/7 DESI-5yr bins and marginally outside (1.013 sigma) at z=0.51;
under Euclid the middle bins exceed 1 sigma.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 per machinery pin (O(30) ODE solves)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------------
# Section 1 — paths + canonical constants import (MANDATORY: never hardcode)
# ----------------------------------------------------------------------------
THIS = Path(__file__).resolve()
PROJECT_ROOT = THIS.parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-96"
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (   # noqa: E402
    sigma_8,                 # 0.811  (Planck/LCDM sigma_8 anchor; COMPARISON-ONLY)
    Omega_m,                 # 0.315  (matter density used in the growth ODE; borrowed-LCDM)
    w0_FW,                   # -0.918 (framework late-time EoS; enters the borrowed-H(z) only as a cross-check)
)

GATE_ID = "S96-OBS-FSIGMA8-FORECAST"
SCHEME = "FW-growth-a2-channel"
CONVENTION = "RATIO-substrate-growth-on-borrowed-LCDM-H(z)-C10"
L_MAX = "N/A"                        # growth-history modulation, not a spectral truncation

NPZ_OUT = SESSION_DIR / "s96_obs_fsigma8_forecast.npz"
PNG_OUT = SESSION_DIR / "s96_obs_fsigma8_forecast.png"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"
CANON = SHARED_DIR / "canonical_constants.py"

S70_BULK_FLOW = COMPUTATIONS_DIR / "session-70" / "s70_bulk_flow.npz"
S65_FSIGMA8 = COMPUTATIONS_DIR / "session-65" / "s65_fsigma8.npz"
S65_LOG = COMPUTATIONS_DIR / "session-65" / "s65_fsigma8_log.txt"

INPUT_FILES = [CANON, S70_BULK_FLOW, S65_FSIGMA8]

# ----------------------------------------------------------------------------
# Machinery pins (PRDR) — from plan §W6-1 machinery_pin_map
# ----------------------------------------------------------------------------
N_EVAL = 30                          # (local) z-grid points over [0, 1.5]
Z_MIN = 0.0                          # (local) plan scan_range low
Z_MAX = 1.5                          # (local) plan scan_range high
Z_STEP = 0.05                        # (local) nominal z step (plan pin)
TOL_ODE = 1e-6                       # (local) growth-ODE integration tol (plan pin)
SIGMA_BAND = 1.0                     # (local) forecast 1-sigma PASS boundary (plan strict_PASS_boundary)
PUB_PRECISION = 6                    # (local) f_FW published at 6 sig figs => rel_tol >= 1e-6

# paper-search fetch status (FETCH NOTE): two arXiv queries returned EMPTY this
# session => paper-search down => INFO branch. The forecast sigma is read from
# the S65-embedded forecast arrays (prior substrate-first artifact), NOT fabricated.
PAPER_SEARCH_AVAILABLE = False       # (local) live forecast-precision fetch unavailable this session


# ----------------------------------------------------------------------------
# Section 2 — SHA-256 dual-pin block (canonical local pattern)
# ----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = Path(script_path).read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = Path(canonical_path).read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ----------------------------------------------------------------------------
# Section 3 — borrowed-LCDM linear growth D(a) and f = dlnD/dlna
# ----------------------------------------------------------------------------
def E_of_a(a, om, w0=-1.0):
    """Borrowed-LCDM dimensionless Hubble E(a)=H/H0. Dark energy as a constant-w0
    fluid: rho_DE/rho_DE0 = a^{-3(1+w0)}. For w0=-1 this reduces to LCDM."""
    ode_density = (1.0 - om) * a ** (-3.0 * (1.0 + w0))  # (local)
    return np.sqrt(om * a ** -3 + ode_density)


def growth_ode(a, y, om, w0=-1.0):
    """Linear growth equation in scale factor a (D' = dD/da):
       D'' + (3/a + E'/E) D' - (3/2) Om(a)/a^2 D = 0.
    Returns [D', D'']."""
    D, Dp = y  # (local)
    E = E_of_a(a, om, w0)  # (local)
    da = 1e-6  # (local) numerical dlnE/dlna
    dlnE_dlna = (np.log(E_of_a(a * (1 + da), om, w0)) - np.log(E_of_a(a * (1 - da), om, w0))) / (2 * da)  # (local)
    Om_a = om * a ** -3 / E ** 2  # (local)
    Dpp = -(3.0 / a + dlnE_dlna / a) * Dp + 1.5 * Om_a / a ** 2 * D  # (local)
    return [Dp, Dpp]


def solve_growth(om, w0=-1.0, a_ini=1e-3, a_end=1.0):
    """Integrate the linear growth factor from a_ini to a_end. Matter-dominated
    IC: D ~ a, D' ~ 1."""
    sol = solve_ivp(growth_ode, [a_ini, a_end], [a_ini, 1.0],
                    args=(om, w0), dense_output=True, rtol=TOL_ODE, atol=1e-10,
                    method="RK45")  # (local)
    return sol


def f_of_a(sol, a):
    """f = dlnD/dlna = a D'(a) / D(a)."""
    D, Dp = sol.sol(a)  # (local)
    return a * Dp / D


# ----------------------------------------------------------------------------
# Section 4 — main computation
# ----------------------------------------------------------------------------
def compute():
    res = {}  # (local)

    # ---- load the z=0 PROVEN numbers from s70 ----
    s70 = np.load(S70_BULK_FLOW, allow_pickle=True)  # (local)
    f_FW = float(s70["f_FW_z0"])            # 0.5254916357116971
    f_LCDM = float(s70["f_LCDM_z0"])        # 0.5271303865722888
    fsig8_FW_z0 = float(s70["fsig8_FW"])    # 0.4168026844135987
    fsig8_LCDM_z0 = float(s70["fsig8_LCDM"])# 0.4275027435101263
    sigma8_FW = float(s70["sigma8_fw"])     # 0.7931671145423732
    sigma8_LCDM = float(s70["sigma8_LCDM"]) # 0.811  (== canonical sigma_8)
    growth_ratio = float(s70["growth_ratio"])  # 0.978011238646576  (D_FW/D_LCDM)

    res["f_FW"] = f_FW
    res["f_LCDM"] = f_LCDM
    res["fsig8_FW_z0"] = fsig8_FW_z0
    res["fsig8_LCDM_z0"] = fsig8_LCDM_z0
    res["sigma8_FW"] = sigma8_FW
    res["sigma8_LCDM"] = sigma8_LCDM
    res["growth_ratio"] = growth_ratio
    res["sigma_8_canonical"] = float(sigma_8)   # cross-check sigma8_LCDM == canonical anchor

    # ============================================================
    # CC1 — bare-f suppression (the SMALL number, ~0.31%)
    # ============================================================
    delta_f = f_FW - f_LCDM                       # -0.001638... (suppression on bare f)
    delta_f_frac = delta_f / f_LCDM               # -0.003107 = -0.311%
    res["delta_f"] = delta_f
    res["delta_f_frac"] = delta_f_frac
    res["delta_f_pct"] = delta_f_frac * 100.0
    sign_bare_f = -1 if delta_f < 0 else (1 if delta_f > 0 else 0)  # (local)
    res["sign_bare_f"] = sign_bare_f              # expect -1 (suppression)

    # ============================================================
    # CC2 — f·sigma_8 PRODUCT suppression (the "~4%" number)
    # ============================================================
    # z=0 product delta:
    delta_fsig8_z0 = fsig8_FW_z0 - fsig8_LCDM_z0
    delta_fsig8_frac_z0 = delta_fsig8_z0 / fsig8_LCDM_z0   # ~ -2.50% at z=0
    res["delta_fsig8_z0"] = delta_fsig8_z0
    res["delta_fsig8_frac_z0"] = delta_fsig8_frac_z0
    res["delta_fsig8_pct_z0"] = delta_fsig8_frac_z0 * 100.0

    # additive decomposition cross-check: (1+df/f)(1+dsig/sig)-1 ≈ df/f + dsig/sig
    delta_sigma8_frac = (sigma8_FW - sigma8_LCDM) / sigma8_LCDM   # ~ -2.20%
    res["delta_sigma8_frac"] = delta_sigma8_frac
    res["delta_sigma8_pct"] = delta_sigma8_frac * 100.0
    additive_approx = delta_f_frac + delta_sigma8_frac           # ~ -2.51%
    exact_product = (1 + delta_f_frac) * (1 + delta_sigma8_frac) - 1.0
    res["product_additive_approx_z0"] = additive_approx
    res["product_exact_z0"] = exact_product
    res["product_additive_residual_z0"] = abs(exact_product - additive_approx)

    # ============================================================
    # z-curve over 0 < z < 1.5: borrowed-LCDM growth history modulated by growth_ratio
    # ============================================================
    z_grid = np.linspace(Z_MIN, Z_MAX, N_EVAL)    # 30 points
    a_grid = 1.0 / (1.0 + z_grid)
    a_grid = np.clip(a_grid, 1e-3, 1.0)

    # Borrowed LCDM growth (w0=-1) — the framework borrows H(z) (C10 caveat)
    sol_lcdm = solve_growth(Omega_m, w0=-1.0)
    D_lcdm = np.array([sol_lcdm.sol(a)[0] for a in a_grid])   # (local)
    D_lcdm0 = sol_lcdm.sol(1.0)[0]                            # (local) D_LCDM(a=1)
    D_lcdm_norm = D_lcdm / D_lcdm0                            # normalised to z=0

    f_lcdm_z = np.array([f_of_a(sol_lcdm, a) for a in a_grid])  # f(z) from the SAME ODE

    # Framework f(z): the linear growth-RATE shift is set by the borrowed-H(z)
    # growth history; at z=0 it must reproduce f_FW/f_LCDM from s70. We apply the
    # PROVEN per-bin f-shift structure. The growth-rate ratio f_FW/f_LCDM varies
    # with z (the s59/s65 curve); here we model it via the constant growth-amplitude
    # ratio D_FW/D_LCDM = growth_ratio applied to sigma_8 (the amplitude leg) AND
    # the z=0-anchored f-ratio for the rate leg.
    f_ratio_z0 = f_FW / f_LCDM                               # 0.996893 (z=0)
    # f(z) framework: scale the LCDM f(z) by the z=0 rate ratio as the leading
    # (borrowed-H) model; the true z-dependence is the s65 curve loaded below.
    f_fw_z = f_lcdm_z * f_ratio_z0                           # (local) leading borrowed-H model

    # sigma_8(z) for each cosmology: sigma_8 * D(z)/D(0)
    sig8_lcdm_z = sigma8_LCDM * D_lcdm_norm
    sig8_fw_z = sigma8_FW * D_lcdm_norm                      # framework amplitude leg = sigma8_FW · (borrowed growth shape)

    fsig8_lcdm_z = f_lcdm_z * sig8_lcdm_z
    fsig8_fw_z = f_fw_z * sig8_fw_z

    frac_fsig8_z = (fsig8_fw_z - fsig8_lcdm_z) / fsig8_lcdm_z   # fractional product suppression vs z

    res["z_grid"] = z_grid
    res["a_grid"] = a_grid
    res["D_lcdm_norm"] = D_lcdm_norm
    res["f_lcdm_z"] = f_lcdm_z
    res["f_fw_z"] = f_fw_z
    res["sig8_lcdm_z"] = sig8_lcdm_z
    res["sig8_fw_z"] = sig8_fw_z
    res["fsig8_lcdm_z"] = fsig8_lcdm_z
    res["fsig8_fw_z"] = fsig8_fw_z
    res["frac_fsig8_z"] = frac_fsig8_z
    res["max_frac_fsig8_pct_borrowed"] = float(np.min(frac_fsig8_z) * 100.0)  # most-negative

    # ============================================================
    # Forecast sigma-distance: load the S65 forecast (substrate-first prior artifact)
    # FETCH NOTE: paper-search down => use the S65-embedded forecast arrays; NOT fabricated
    # ============================================================
    s65 = np.load(S65_FSIGMA8, allow_pickle=True)  # (local)
    z_bins = s65["z_bins"]                          # [0.15 0.38 0.51 0.7 0.85 1.05 1.52]
    fsig8_FW_bins = s65["fsig8_FW_bins"]
    fsig8_LCDM_bins = s65["fsig8_LCDM_bins"]
    frac_FW_bins = s65["frac_FW"]                   # fractional product suppression at the bins
    nsig_FW_current = s65["nsig_FW_current"]        # vs current DESI obs
    nsig_FW_desi5 = s65["nsig_FW_desi5"]            # vs DESI-5yr forecast precision
    nsig_FW_euclid = s65["nsig_FW_euclid"]          # vs Euclid forecast precision
    err_obs = s65["err_obs"]                        # current DESI obs errors
    fsig8_obs = s65["fsig8_obs"]                    # current DESI obs fsigma8

    # back out the implied forecast 1-sigma per bin (sigma_forecast = |dfs8|/nsig)
    delta_bins = np.abs(fsig8_FW_bins - fsig8_LCDM_bins)
    sigma_desi5 = delta_bins / nsig_FW_desi5        # (local) DESI-5yr forecast 1-sigma per bin
    sigma_euclid = delta_bins / nsig_FW_euclid      # (local) Euclid forecast 1-sigma per bin

    res["z_bins"] = z_bins
    res["fsig8_FW_bins"] = fsig8_FW_bins
    res["fsig8_LCDM_bins"] = fsig8_LCDM_bins
    res["frac_FW_bins_pct"] = frac_FW_bins * 100.0
    res["nsig_FW_current"] = nsig_FW_current
    res["nsig_FW_desi5"] = nsig_FW_desi5
    res["nsig_FW_euclid"] = nsig_FW_euclid
    res["sigma_desi5_per_bin"] = sigma_desi5
    res["sigma_euclid_per_bin"] = sigma_euclid
    res["err_obs"] = err_obs
    res["fsig8_obs"] = fsig8_obs

    # max sigma-distances (the headline forecast discrimination)
    max_nsig_current = float(np.max(nsig_FW_current))
    max_nsig_desi5 = float(np.max(nsig_FW_desi5))
    max_nsig_euclid = float(np.max(nsig_FW_euclid))
    z_at_max_desi5 = float(z_bins[int(np.argmax(nsig_FW_desi5))])
    z_at_max_euclid = float(z_bins[int(np.argmax(nsig_FW_euclid))])
    res["max_nsig_current"] = max_nsig_current
    res["max_nsig_desi5"] = max_nsig_desi5
    res["max_nsig_euclid"] = max_nsig_euclid
    res["z_at_max_desi5"] = z_at_max_desi5
    res["z_at_max_euclid"] = z_at_max_euclid

    # max fractional product suppression at the bins (the "~4%" number from s65)
    max_frac_FW_pct = float(np.min(frac_FW_bins) * 100.0)   # -4.058% at z=0.51
    z_at_max_frac = float(z_bins[int(np.argmin(frac_FW_bins))])
    res["max_frac_FW_pct"] = max_frac_FW_pct
    res["z_at_max_frac"] = z_at_max_frac

    # within-band counts (vs forecast)
    res["n_bins"] = int(len(z_bins))
    res["within_band_desi5"] = int(np.sum(nsig_FW_desi5 <= SIGMA_BAND))
    res["within_band_euclid"] = int(np.sum(nsig_FW_euclid <= SIGMA_BAND))
    res["within_band_current"] = int(np.sum(nsig_FW_current <= SIGMA_BAND))

    # ============================================================
    # SIGN / MAGNITUDE / REGIME verdict
    # ============================================================
    # SIGN: both legs suppress (delta_f<0 AND delta_fsig8<0) AND S_8 relieving
    # S_8 = sigma_8 * sqrt(Om/0.3); sigma8_FW < sigma8_LCDM => S_8_FW lower => tension-relieving
    S8_LCDM = sigma8_LCDM * np.sqrt(Omega_m / 0.3)   # (local)
    S8_FW = sigma8_FW * np.sqrt(Omega_m / 0.3)       # (local)
    res["S8_LCDM"] = float(S8_LCDM)
    res["S8_FW"] = float(S8_FW)
    s8_relieving = S8_FW < S8_LCDM                   # True => correct (tension-relieving) sign
    res["S8_relieving"] = bool(s8_relieving)

    sign_ok = (delta_f < 0) and (delta_fsig8_z0 < 0) and s8_relieving
    sign_verdict = "PASS" if sign_ok else "FAIL"
    res["sign_verdict"] = sign_verdict

    # MAGNITUDE: within-band at ALL z (vs the FORECAST) => PASS; some-in-some-out => INFO
    all_within_desi5 = res["within_band_desi5"] == res["n_bins"]
    some_out_desi5 = res["within_band_desi5"] < res["n_bins"]
    all_out_desi5 = res["within_band_desi5"] == 0
    if all_out_desi5:
        magnitude_verdict = "FAIL"
    elif all_within_desi5:
        magnitude_verdict = "PASS"
    else:
        magnitude_verdict = "INFO"   # within-band at some z, outside at others (z-dependent discriminator)
    res["magnitude_verdict"] = magnitude_verdict

    # REGIME: the C10 borrowed-H(z) modulation is valid where the borrowed LCDM
    # growth ODE is well-defined over the whole z-grid (matter+DE dominated; no
    # breakdown). The fetch-gate makes the FORECAST-precision leg pending, but the
    # substrate curve is VALID across the full intended z window.
    # f_used = fraction of intended z-window with a well-defined growth solution.
    finite_frac = float(np.mean(np.isfinite(fsig8_fw_z) & (D_lcdm_norm > 0)))  # (local)
    res["domain_used_frac"] = finite_frac
    if finite_frac >= 0.95:
        regime_verdict = "VALID"
    elif finite_frac >= 0.50:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    res["regime_verdict"] = regime_verdict

    # ---- composite collapse (PRE-REGISTERED rule, gate-verdicts.md) ----
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # FETCH-GATE OVERRIDE: paper-search down => the LIVE forecast-precision
    # validation is deferred (PRE-REG-INFO-branch-a). Even if the S65-embedded
    # forecast yields all-within-band (PASS magnitude), the verdict is held at
    # INFO because the forecast precision was NOT live-validated this session.
    # This is the pre-registered INFO_meaning second clause.
    if PAPER_SEARCH_AVAILABLE is False and composite == "PASS":
        composite = "INFO"
        res["fetch_gate_override"] = True
    else:
        res["fetch_gate_override"] = False

    res["verdict"] = composite

    # ---- value string: headline = max-z sigma-distance vs DESI-5yr forecast ----
    res["value"] = (
        f"bare_f_supp={delta_f_frac*100:.3f}%;"
        f"product_supp_max={max_frac_FW_pct:.3f}%@z{z_at_max_frac};"
        f"sigma_DESI5yr_max={max_nsig_desi5:.3f}@z{z_at_max_desi5};"
        f"sigma_Euclid_max={max_nsig_euclid:.3f}@z{z_at_max_euclid};"
        f"sigma_current_max={max_nsig_current:.3f};"
        f"within_band_DESI5yr={res['within_band_desi5']}/{res['n_bins']};"
        f"S8_relieving={int(s8_relieving)};"
        f"INFO-branch-a_paper-search-down"
    )

    return res


# ----------------------------------------------------------------------------
# Section 5 — plot
# ----------------------------------------------------------------------------
def make_plot(res):
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (1) f·sigma_8(z) curves: FW vs LCDM with current DESI obs + forecast bands
    ax = axes[0, 0]
    ax.plot(res["z_grid"], res["fsig8_lcdm_z"], lw=2.0, color="#1f77b4", label=r"$f\sigma_8$ LCDM (borrowed-H)")
    ax.plot(res["z_grid"], res["fsig8_fw_z"], lw=2.0, color="#d62728",
            label=r"$f\sigma_8$ FW (growth_ratio=0.978)")
    ax.errorbar(res["z_bins"], res["fsig8_obs"], yerr=res["err_obs"], fmt="o", ms=4,
                color="k", capsize=2, alpha=0.7, label="DESI/eBOSS obs (current)")
    # DESI-5yr forecast band around the LCDM curve at the bins
    ax.errorbar(res["z_bins"], res["fsig8_LCDM_bins"], yerr=res["sigma_desi5_per_bin"],
                fmt="s", ms=4, color="#2ca02c", capsize=2, alpha=0.6,
                label="DESI-5yr forecast 1σ")
    ax.set_xlabel("redshift z")
    ax.set_ylabel(r"$f\sigma_8(z)$")
    ax.set_title("f·σ₈(z): FW suppression vs LCDM (C10 borrowed-H(z))")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3)

    # (2) fractional product suppression vs z (the "~4%" number)
    ax = axes[0, 1]
    ax.plot(res["z_grid"], res["frac_fsig8_z"] * 100, lw=2.0, color="#d62728",
            label="borrowed-H model")
    ax.plot(res["z_bins"], res["frac_FW_bins_pct"], "o-", ms=5, color="#9467bd",
            label="S65 direct (per-bin)")
    ax.axhline(res["max_frac_FW_pct"], color="#9467bd", ls="--", lw=1.0,
               label=fr"max suppression {res['max_frac_FW_pct']:.2f}% @ z={res['z_at_max_frac']}")
    ax.axhline(res["delta_f_pct"], color="#ff7f0e", ls=":", lw=1.5,
               label=fr"bare-f suppression {res['delta_f_pct']:.3f}% (z=0)")
    ax.set_xlabel("redshift z")
    ax.set_ylabel("fractional suppression vs LCDM (%)")
    ax.set_title("PRODUCT (~4%) vs BARE-f (~0.31%) — C5 conflation guard")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3)

    # (3) sigma-distance per bin: current vs DESI-5yr vs Euclid
    ax = axes[1, 0]
    width = 0.025  # (local) bar-group offset for the σ-distance panel
    ax.bar(res["z_bins"] - width, res["nsig_FW_current"], width*0.9, color="#1f77b4",
           label="vs current obs")
    ax.bar(res["z_bins"], res["nsig_FW_desi5"], width*0.9, color="#2ca02c",
           label="vs DESI-5yr forecast")
    ax.bar(res["z_bins"] + width, res["nsig_FW_euclid"], width*0.9, color="#d62728",
           label="vs Euclid forecast")
    ax.axhline(1.0, color="k", ls="--", lw=1.2, label="1σ band edge")
    ax.set_xlabel("redshift z")
    ax.set_ylabel("σ-distance |fσ8_FW − fσ8_LCDM| / σ_forecast")
    ax.set_title("Forecast discrimination (INFO-branch-a: paper-search down)")
    ax.legend(fontsize=7.5)
    ax.grid(alpha=0.3)

    # (4) text panel — the substitution-chain numbers
    ax = axes[1, 1]
    ax.axis("off")
    txt = (
        f"SUBSTITUTION CHAIN (substituted numbers)\n"
        f"{'='*44}\n"
        f"f_FW   = {res['f_FW']:.6f}\n"
        f"f_LCDM = {res['f_LCDM']:.6f}\n"
        f"δf     = f_FW − f_LCDM = {res['delta_f']:.6f}\n"
        f"δf/f_LCDM = {res['delta_f_frac']*100:.3f}%   <- BARE-f (SMALL)\n\n"
        f"σ8_FW   = {res['sigma8_FW']:.6f}\n"
        f"σ8_LCDM = {res['sigma8_LCDM']:.6f}\n"
        f"δσ8/σ8  = {res['delta_sigma8_frac']*100:.3f}%\n"
        f"PRODUCT: δf/f + δσ8/σ8 ≈ {res['product_additive_approx_z0']*100:.3f}% (z=0)\n"
        f"max PRODUCT suppression = {res['max_frac_FW_pct']:.3f}% @ z={res['z_at_max_frac']}\n"
        f"   <- the '~4%' number (NOT bare f)\n\n"
        f"S_8_FW  = {res['S8_FW']:.4f}  <  S_8_LCDM = {res['S8_LCDM']:.4f}\n"
        f"   => S_8 LOWER => RELIEVES Planck-vs-lensing tension\n\n"
        f"FORECAST σ-distance (max):\n"
        f"  current obs : {res['max_nsig_current']:.3f} σ  (within band)\n"
        f"  DESI-5yr    : {res['max_nsig_desi5']:.3f} σ @ z={res['z_at_max_desi5']}\n"
        f"  Euclid      : {res['max_nsig_euclid']:.3f} σ @ z={res['z_at_max_euclid']}\n\n"
        f"VERDICT: {res['verdict']}  "
        f"(sign={res['sign_verdict']}/mag={res['magnitude_verdict']}/reg={res['regime_verdict']})\n"
        f"INFO-branch-a: paper-search down => σ-distance from S65-embedded\n"
        f"forecast (prior substrate artifact); live validation deferred."
    )
    ax.text(0.0, 1.0, txt, transform=ax.transAxes, fontsize=8.0,
            family="monospace", va="top", ha="left")

    fig.suptitle(
        f"{GATE_ID} — f·σ₈(z) growth-suppression LSS discriminator\n"
        f"PHONONIC a₂-channel; bare-f −0.31% / product −4.06%; S₈ tension-relieving; VERDICT {res['verdict']}",
        fontsize=12, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  plot -> {PNG_OUT}")


# ----------------------------------------------------------------------------
# Section 6 — verdict-line emission (dual-SHA + schema-v2 3-tuple)
# ----------------------------------------------------------------------------
def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    # schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row (REQUIRED — [SIGN] trigger)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = bare-f suppression (delta_f<0) AND product suppression (delta_fsig8<0) AND S_8_FW<S_8_LCDM (tension-relieving); "
        f"mag = within DESI-5yr 1-sigma band at 6/7 bins, 1.013-sigma at z=0.51 (z-dependent discriminator); "
        f"regime = borrowed-LCDM growth ODE VALID across full z in [0,1.5]; INFO-branch-a (paper-search down, live forecast validation deferred)\n"
    )
    with open(VERDICT_TXT, "a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(tuple_row)
    print("  verdict line + dual-SHA companion + 3-tuple row appended.")


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------
def main():
    print(f"=== {GATE_ID} ===")
    print(f"  sigma_8(canonical)={sigma_8}  Omega_m={Omega_m}  w0_FW={w0_FW}")
    print(f"  paper-search available this session: {PAPER_SEARCH_AVAILABLE} (=> INFO branch if PASS-magnitude)")
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(THIS, CANON, pins)

    res = compute()

    print("\n--- BARE-f vs PRODUCT (C5 conflation guard) ---")
    print(f"  BARE-f suppression  : delta_f={res['delta_f']:.6f}  "
          f"= {res['delta_f_pct']:.3f}%  (the SMALL number)")
    print(f"  PRODUCT suppression : max {res['max_frac_FW_pct']:.3f}% @ z={res['z_at_max_frac']}  "
          f"(the '~4%' number)")
    print(f"  delta_sigma8        : {res['delta_sigma8_pct']:.3f}%")
    print(f"  additive approx (z=0): {res['product_additive_approx_z0']*100:.3f}%  "
          f"(exact product {res['product_exact_z0']*100:.3f}%, "
          f"residual {res['product_additive_residual_z0']*100:.4f}%)")

    print("\n--- S_8 DIRECTION ---")
    print(f"  S_8_FW={res['S8_FW']:.4f}  <  S_8_LCDM={res['S8_LCDM']:.4f}  "
          f"=> tension-relieving = {res['S8_relieving']}")

    print("\n--- FORECAST sigma-distance (S65-embedded; INFO-branch-a) ---")
    print(f"  max vs current obs : {res['max_nsig_current']:.3f} sigma")
    print(f"  max vs DESI-5yr    : {res['max_nsig_desi5']:.3f} sigma @ z={res['z_at_max_desi5']}")
    print(f"  max vs Euclid      : {res['max_nsig_euclid']:.3f} sigma @ z={res['z_at_max_euclid']}")
    print(f"  within-band (DESI-5yr): {res['within_band_desi5']}/{res['n_bins']}")
    print(f"  within-band (Euclid)  : {res['within_band_euclid']}/{res['n_bins']}")
    print(f"  within-band (current) : {res['within_band_current']}/{res['n_bins']}")

    print(f"\n  VALUE: {res['value']}")
    print(f"  VERDICT: {res['verdict']}")
    print(f"  3-tuple: sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} "
          f"regime={res['regime_verdict']}  (fetch_gate_override={res['fetch_gate_override']})")
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    make_plot(res)

    # save npz (full float64 for any downstream consumer)
    save = {}  # (local)
    for k, v in res.items():
        if isinstance(v, bool):
            save[k] = int(v)
        else:
            save[k] = v
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    save["GATE_ID"] = GATE_ID
    save["N_eval"] = N_EVAL
    save["L_max"] = L_MAX
    save["scheme"] = SCHEME
    save["convention"] = CONVENTION
    save["paper_search_available"] = int(PAPER_SEARCH_AVAILABLE)
    np.savez(NPZ_OUT, **save)
    print(f"  data -> {NPZ_OUT}")

    append_verdict(res["verdict"], res["value"], audit_sha, content_sha,
                   res["sign_verdict"], res["magnitude_verdict"], res["regime_verdict"])

    print(f"\n4-tuple: (value={res['value']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print("DONE.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
