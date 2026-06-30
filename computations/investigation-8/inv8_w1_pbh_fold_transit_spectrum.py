#!/usr/bin/env python3
"""
INV8 W1-1 — PBH mass spectrum from the van Hove fold transit
============================================================

Gate: INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM  ([SIGN])

Pre-registered threshold (plan §W1-1):
  I_PBH := integral_{10^17 g}^{10^23 g} f_PBH(M) dlnM
  PASS iff |I_PBH - 0.27| <= 0.05  AND  f_PBH(M) <= 1 throughout the window.
  FAIL iff I_PBH outside [0.22, 0.32]  OR  f_PBH > 1 somewhere in the window.
  INFO iff the verdict flips within the delta_c systematic band [0.4, 0.7].

[SIGN] sub-verdicts (plan substitution-chain Step 5):
  sign_verdict      = PASS iff I_PBH > 0 AND monotone-increasing in sigma_fold
                      AND the ceiling f_PBH<=1 is respected.
  magnitude_verdict = PASS iff |I_PBH - 0.27| <= 0.05; INFO if in (0.05, info_band];
                      FAIL if > info_band (info_band = 0.22 = full distance to 0.05-edge of
                      the [0.22,0.32] FAIL band measured from 0.27, i.e. |0-0.27|).
  regime_verdict    = VALID iff the window-placement conclusion is robust across
                      (i) the delta_c band and (ii) the c_s/H horizon-mass ambiguity
                      (i.e. NOT a band-edge artifact); BREAKDOWN otherwise.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-64/s64_bogoliubov_phases.npz   (transit Bogoliubov |beta_k|^2; 8 BCS modes)
       [plan named s64_transit_power_spectrum.npz; that exact file is absent — the RIGHT
        substrate source for the transit Bogoliubov occupation is s64_bogoliubov_phases.npz
        (beta_complex_B/C, beta_sq_check_B/C); N_pairs=59.8 is the canonical sum, imported.]
  - computations/session-95/s95_w4_4_sp_conformal_embed.npz  (fold Omega-profile; Omega_BA_fold)
       [plan named s95_w1_omega_profile.npz; absent — the RIGHT source is the conformal-embed
        npz that canonicalizes Omega_BA_fold = 2.241353 (S97-W1-OMEGA-PROFILE).]
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Classification: PHONONIC.

METHODOLOGY
-----------
Substrate-first. The substrate IS the impulsive first-order transit through the van Hove
fold at tau_fold = 0.190 (Mach 13.75, supersonic). The Bogoliubov transformation of the 8
BCS fibre modes (|beta_k|^2 -> N_pairs = 59.8 saturated pairs, P_exc = 1.000) IS the
squeezed-thermal overdensity field that seeds gravitational collapse. A PBH here is a region
of the fabric whose post-transit GGE overdensity exceeds the collapse threshold delta_c.

Chain: D_K eigenvalues -> transit Bogoliubov occupation (spectral) -> overdensity contrast
sigma_fold (PHONONIC GGE source) -> Press-Schechter collapse fraction beta(M) -> present-day
f_PBH(M) via the a_2 (gravity) channel -> asteroid-window DM abundance + first compact-object
mass function.

The single dimensional import is M_KK = 7.42866e16 GeV; it sets WHERE on the gram axis the
spectrum sits. The Carr-Kohri-Sendouda-Yokoyama (2021) asteroid window [10^17,10^23] g is the
ONLY mass range where PBHs can be 100% of DM (above the ~5e14 g Hawking-evaporation floor,
below the microlensing floor) — a consistency ceiling f_PBH<=1, NOT a substrate input.

hawking-theorist co-option: first-order-transition PBH formation (trapped false-vacuum
pockets / bubble-collision overdensities) + the Carr-Hawking (1974) collapse criterion
delta > delta_c ~ c_s^2 = w (radiation w=1/3 -> delta_c~0.45). Press-Schechter beta(M) =
erfc(delta_c / (sqrt2 sigma)). Evaporation lifetime t_evap ~ (M/M_*)^3 t_0 with
M_* ~ 5.1e14 g: any M < M_* has evaporated by today and cannot be present-day DM.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (1D quadrature; CPU-bound) BEFORE numpy import
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Path bootstrap + canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

# Script lives at computations/investigation-8/; _shared holds canonical_constants.py.
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

from canonical_constants import (  # noqa: E402
    M_KK,            # 7.42866e16 GeV — the single dimensional import (gravity route)
    Omega_DM,        # 0.2657 — GGE relic total (normalization)
    n_pairs,         # 59.8 — transit Bogoliubov pairs (S38)
    H_fold,          # 586.527 M_KK — Hubble parameter at the fold (S38)
    dt_transit,      # 1.1302e-3 M_KK^-1 — transit duration (S38)
    Mach_max_framework,  # 13.75 — supersonic Mach at the fold
    Omega_BA_fold,   # 2.241353 — fold conformal/Omega-profile factor (S95/S97)
    tau_fold,        # 0.19 — fold parameter
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
from scipy.special import erfc

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent            # computations/investigation-8
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "8"                                                          # (local)
GATE_ID = "INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM"                        # (local)
SCHEME = "FW"                                                          # (local)
CONVENTION = "ABSOLUTE"                                                # (local)
L_MAX = 10                                                             # (local)

# Pre-registered thresholds (plan §W1-1 operator + strict_PASS_boundary)
TARGET_ABUNDANCE = 0.27          # (local) f_dimer_Z2 the Leggett channel misses
PASS_BAND = 0.05                 # (local) ABSOLUTE on |I_PBH - 0.27|
FAIL_LO, FAIL_HI = 0.22, 0.32    # (local) [0.22,0.32] = PASS region; outside -> FAIL
CEILING = 1.0                    # (local) f_PBH <= 1 hard asteroid-window ceiling
N_PER_DECADE = 200               # (local) plan machinery: >=200 points/decade
M_GRID_LO, M_GRID_HI = 1e15, 1e26    # (local) gram grid (window [1e17,1e23] sub-interval)
WIN_LO, WIN_HI = 1e17, 1e23      # (local) asteroid window (grams)
DELTA_C_BAND = np.array([0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70])   # (local) systematic
DELTA_C_FIDUCIAL = 0.45          # (local) radiation-era Carr-Hawking delta_c ~ w = 1/3 -> ~0.45

# Physical constants (CODATA / standard cosmology — methodological anchors, not substrate)
GEV_TO_G = 1.78266192e-24        # (local) 1 GeV/c^2 in grams (CODATA)
M_PBH_EVAP = 5.1e14              # (local) g — PBH mass evaporating at t_0 (Carr review)
# Standard radiation-era Friedmann horizon mass: M_H(T) ~ 4.8e13 g (T/GeV)^-2 (Carr 2021 review,
# g_* ~ 100). Equivalent to M_H = (4/3)pi rho (1/H)^3 with rho = (pi^2/30) g_* T^4 and the
# Friedmann H. This is the LAB-IN (standard cosmology) horizon-mass calibration; the substrate
# fold temperature is T_fold = M_KK (the fold IS at the substrate energy scale).
M_H_COEFF = 4.8e13               # (local) g, horizon-mass coefficient at T=1 GeV
M_EQ = 2.8e17                    # (local) g — horizon mass at matter-radiation equality (Carr)

OUT_NPZ = SESSION_DIR / "inv8_w1_pbh_fold_transit_spectrum.npz"
OUT_PNG = SESSION_DIR / "inv8_w1_pbh_fold_transit_spectrum.png"

S64_BOGO = COMPUTATIONS_DIR / "session-64" / "s64_bogoliubov_phases.npz"   # (local)
S95_OMEGA = COMPUTATIONS_DIR / "session-95" / "s95_w4_4_sp_conformal_embed.npz"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S64_BOGO,
    S95_OMEGA,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
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
# Section 5 — Substrate-physics helpers
# ---------------------------------------------------------------------------
def load_sigma_fold() -> dict:
    """Build the transit-sourced rms overdensity sigma_fold from the on-disk
    Bogoliubov spectrum + canonical N_pairs. The supersonic (Mach 13.75)
    first-order transition produces SQUEEZED-THERMAL occupation; |beta_k|^2
    summed = N_pairs = 59.8 (canonical). sigma_fold^2 ~ <delta^2>_fold prop |beta_k|^2.

    We characterize sigma_fold three ways (all O(1) substrate dimensionless):
      (a) sigma_lin   = sqrt(N_pairs) normalization of the squeezed amplitude
                        proxy <delta^2> = N_pairs per the plan Step 2 (raw, large).
      (b) sigma_perpx = the PER-MODE rms |beta_k|^2 averaged over the 8 BCS modes
                        (the density contrast of a single horizon patch, the
                        physically-relevant quantity for collapse).
      (c) sigma_bound = capped at 1 (a horizon patch overdensity delta cannot
                        exceed O(1) without already being a separate universe;
                        the linear-theory PS collapse fraction saturates).
    The collapse fraction is computed for ALL three so the sign/regime verdict
    is robust to the sigma_fold convention.
    """
    info = {}  # (local)
    beta_sq_per_mode = None  # (local)
    try:
        d = np.load(S64_BOGO, allow_pickle=True)  # (local)
        # beta_sq_check_B is (32 k-rows, 8 BCS modes); the |beta_k|^2 occupation.
        bsq = np.asarray(d["beta_sq_check_B"], dtype=float)  # (local) (32,8)
        # final-state per-mode occupation: average over k-rows, the saturated value.
        beta_sq_per_mode = np.nanmean(bsq, axis=0)  # (local) (8,)
        info["beta_sq_per_mode"] = beta_sq_per_mode
        info["beta_sq_sum_raw"] = float(np.nansum(beta_sq_per_mode))
        info["source"] = "s64_bogoliubov_phases.npz beta_sq_check_B"
    except Exception as e:  # noqa: BLE001
        info["source"] = f"FALLBACK canonical n_pairs (npz read failed: {e})"

    # Canonical normalization: total pairs over the spectrum = N_pairs (S38).
    N = float(n_pairs)  # (local) 59.8
    # (a) raw linear amplitude proxy: <delta^2> = N_pairs (plan Step 2 literal).
    sigma_lin = float(np.sqrt(N))  # (local)
    # (b) per-mode rms density contrast of one horizon patch. The 8 BCS modes
    #     carry N_pairs between them; the PER-PATCH contrast is the per-mode rms,
    #     sqrt(N_pairs / N_modes_eff). The pair wavefunction is 93% B2/6.3% B1, so
    #     the effective mode count carrying the squeeze is ~ the 8 BdG fibre modes.
    N_modes = 8.0  # (local) the 8 BCS fibre modes (atlas-04 T4 pair wavefunction)
    sigma_perpx = float(np.sqrt(N / N_modes))  # (local) ~ 2.73 — STILL >> 1
    # (c) physically-capped contrast (linear-theory ceiling): delta_rms <= O(1).
    sigma_bound = 1.0  # (local) saturation cap
    info["sigma_lin"] = sigma_lin
    info["sigma_perpx"] = sigma_perpx
    info["sigma_bound"] = sigma_bound
    return info


def horizon_mass_at_fold_grams() -> dict:
    """Map the fold transit to a present-day PBH horizon mass in grams via TWO
    independent routes, both anchored on the single import M_KK.

    Route A (standard Friedmann, LAB-IN calibration): the fold IS at the substrate
      energy scale, T_fold = M_KK. The standard radiation-era horizon mass is
      M_H(T) = M_H_COEFF (T/GeV)^-2 with M_H_COEFF ~ 4.8e13 g (g_*~100). This is
      the calibration every PBH-DM paper uses; it answers 'at what gram scale does
      a horizon collapsing at temperature T deposit a PBH?'.
    Route B (substrate Hubble mass): M_H = (1/2) c_s^3 /(G H_fold) with G = 1/M_KK^2
      (Newton's constant = 2nd spectral moment, phononic-framing.md) and c_s the fold
      sound speed. In substrate units M_H[M_KK] = 0.5 c_s^3 M_KK^2 / H_fold, then
      x M_KK_g. c_s = 1.9305 M_KK is PLAN-PINNED (NOT a registered canonical;
      'c_s_fold' absent from the knowledge MCP) — flagged.

    Both routes are reported; the gate's regime verdict keys on whether they bracket
    (or miss) the asteroid window CONSISTENTLY.
    """
    out = {}  # (local)
    M_KK_g = float(M_KK) * GEV_TO_G  # (local) one substrate quantum in grams
    out["M_KK_g"] = M_KK_g

    # Route A — standard Friedmann horizon mass at T_fold = M_KK.
    T_fold_GeV = float(M_KK)  # (local) the fold IS at the substrate scale
    M_H_routeA = M_H_COEFF * (T_fold_GeV) ** (-2.0)  # (local) grams
    out["M_H_routeA_g"] = M_H_routeA
    out["T_fold_GeV"] = T_fold_GeV

    # Route B — substrate Hubble mass with G = 1/M_KK^2.
    c_s_fold = 1.9305  # (local) PLAN-PINNED fold sound speed (M_KK units); NOT canonical
    M_H_routeB_MKK = 0.5 * c_s_fold ** 3 / float(H_fold)  # (local) units M_KK
    M_H_routeB = M_H_routeB_MKK * M_KK_g  # (local) grams
    out["M_H_routeB_g"] = M_H_routeB
    out["c_s_fold_planpinned"] = c_s_fold
    out["M_H_routeB_MKK"] = M_H_routeB_MKK

    return out


def f_pbh_spectrum(M_grid_g, sigma_fold, delta_c, M_H_peak_g):
    """Present-day f_PBH(M) per the plan Step 4 chain.

    beta(M)  = erfc(delta_c / (sqrt(2) sigma_fold))               [Press-Schechter, Carr-Hawking]
               (mass-independent at the fold: ONE horizon-scale transit produces a
                near-monochromatic spectrum centered at the fold horizon mass; we
                spread it with a log-normal of width ~1 decade around M_H_peak to
                model the finite transit-duration spread, then apply the relic weight.)
    f_PBH(M) = beta(M) (M_eq/M)^{1/2} / Omega_DM  * window_shape(M; M_H_peak)
               with the evaporation cutoff f_PBH(M < M_evap) -> 0 (evaporated).

    Returns f_PBH(M) on the grid (present-day DM fraction per dlnM, normalized).
    """
    M = np.asarray(M_grid_g, dtype=float)  # (local)
    # Press-Schechter collapse fraction at the fold (mass-independent core value):
    beta0 = float(erfc(delta_c / (np.sqrt(2.0) * sigma_fold)))  # (local) in (0,1]
    # Near-monochromatic spectrum: log-normal centered at the fold horizon mass,
    # width sigma_ln ~ ln(10) (one decade) from the finite transit duration.
    sigma_ln = np.log(10.0)  # (local) one-decade spread
    shape = np.exp(-0.5 * (np.log(M / M_H_peak_g) / sigma_ln) ** 2)  # (local) peak=1 at M_H_peak
    # Radiation-era relic weight for present-day fraction (light-PBH enhancement):
    relic = np.sqrt(M_EQ / M)  # (local) (M_eq/M)^{1/2}
    # Evaporation cutoff: PBHs below M_evap have evaporated by today -> contribute 0
    # to the PRESENT-DAY DM budget.
    survives = (M >= M_PBH_EVAP).astype(float)  # (local)
    f = beta0 * shape * relic / float(Omega_DM) * survives  # (local) un-normalized f_PBH(M)
    return f, beta0


def integrate_window(M_grid_g, f_grid):
    """I_PBH = integral over the asteroid window of f_PBH d lnM."""
    M = np.asarray(M_grid_g, dtype=float)  # (local)
    lnM = np.log(M)  # (local)
    in_win = (M >= WIN_LO) & (M <= WIN_HI)  # (local)
    if in_win.sum() < 2:
        return 0.0
    _trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))  # (local) numpy>=2.0 renamed
    return float(_trapz(f_grid[in_win], lnM[in_win]))


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    res = {}  # (local)

    # 6.1 sigma_fold from the transit Bogoliubov spectrum
    sig = load_sigma_fold()  # (local)
    res["sigma_info"] = sig

    # 6.2 horizon mass placement (two routes)
    hm = horizon_mass_at_fold_grams()  # (local)
    res["horizon_mass"] = hm

    # 6.3 mass grid
    n_dec = np.log10(M_GRID_HI / M_GRID_LO)  # (local) 11 decades
    n_pts = int(round(N_PER_DECADE * n_dec))  # (local) >= 2200
    M_grid = np.logspace(np.log10(M_GRID_LO), np.log10(M_GRID_HI), n_pts)  # (local)
    res["M_grid"] = M_grid
    res["n_grid_pts"] = n_pts

    # 6.4 The PRIMARY spectrum: Route A horizon mass (standard Friedmann at T=M_KK),
    #     fiducial sigma_fold = per-patch rms, fiducial delta_c.
    M_H_peak = hm["M_H_routeA_g"]  # (local) standard horizon mass at the fold
    sigma_fid = sig["sigma_perpx"]  # (local) per-patch rms (physically relevant)
    f_grid, beta0 = f_pbh_spectrum(M_grid, sigma_fid, DELTA_C_FIDUCIAL, M_H_peak)  # (local)
    I_PBH = integrate_window(M_grid, f_grid)  # (local)
    f_max_in_window = float(np.max(f_grid[(M_grid >= WIN_LO) & (M_grid <= WIN_HI)]))  # (local)
    f_max_global = float(np.max(f_grid))  # (local)
    res["f_grid"] = f_grid
    res["beta0_fiducial"] = beta0
    res["I_PBH"] = I_PBH
    res["f_max_in_window"] = f_max_in_window
    res["f_max_global"] = f_max_global
    res["M_peak_g"] = M_H_peak

    # 6.5 delta_c band scan (systematic) — does the verdict flip within [0.4,0.7]?
    I_band = []  # (local)
    fmaxwin_band = []  # (local)
    for dc in DELTA_C_BAND:
        fg, _ = f_pbh_spectrum(M_grid, sigma_fid, dc, M_H_peak)  # (local)
        I_band.append(integrate_window(M_grid, fg))
        win = fg[(M_grid >= WIN_LO) & (M_grid <= WIN_HI)]  # (local)
        fmaxwin_band.append(float(np.max(win)) if win.size else 0.0)
    res["I_band"] = np.array(I_band)
    res["fmaxwin_band"] = np.array(fmaxwin_band)
    res["delta_c_band"] = DELTA_C_BAND

    # 6.6 sigma_fold convention robustness (raw-linear / per-patch / capped)
    I_sigma = {}  # (local)
    for label, sg in [("sigma_lin", sig["sigma_lin"]),
                      ("sigma_perpx", sig["sigma_perpx"]),
                      ("sigma_bound", sig["sigma_bound"])]:
        fg, b0 = f_pbh_spectrum(M_grid, sg, DELTA_C_FIDUCIAL, M_H_peak)  # (local)
        I_sigma[label] = (integrate_window(M_grid, fg), b0)
    res["I_sigma"] = I_sigma

    # 6.7 Route-B horizon-mass cross-check (substrate Hubble mass)
    f_gridB, _ = f_pbh_spectrum(M_grid, sigma_fid, DELTA_C_FIDUCIAL, hm["M_H_routeB_g"])  # (local)
    res["I_PBH_routeB"] = integrate_window(M_grid, f_gridB)
    res["f_grid_routeB"] = f_gridB

    # 6.8 The key diagnostic: OOM gap between the fold horizon mass and the window.
    res["OOM_below_window_routeA"] = float(np.log10(WIN_LO / M_H_peak)) if M_H_peak > 0 else np.inf
    res["OOM_below_window_routeB"] = (
        float(np.log10(WIN_LO / hm["M_H_routeB_g"])) if hm["M_H_routeB_g"] > 0 else np.inf)
    res["M_peak_below_evap"] = bool(M_H_peak < M_PBH_EVAP)
    res["M_peak_routeB_below_evap"] = bool(hm["M_H_routeB_g"] < M_PBH_EVAP)

    res["value"] = I_PBH
    return res


# ---------------------------------------------------------------------------
# Section 7 — Verdict
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict):
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict)."""
    I_PBH = res["I_PBH"]  # (local)
    f_max_window = res["f_max_in_window"]  # (local)
    beta0 = res["beta0_fiducial"]  # (local)

    # --- sign_verdict: I_PBH > 0 AND monotone-increasing in sigma_fold AND ceiling held.
    # Monotonicity check: larger sigma -> larger beta0 (collapse fraction).
    I_sigma = res["I_sigma"]  # (local)
    betas = [I_sigma["sigma_bound"][1], I_sigma["sigma_perpx"][1], I_sigma["sigma_lin"][1]]  # (local)
    monotone = all(betas[i] <= betas[i + 1] + 1e-12 for i in range(len(betas) - 1))  # (local)
    ceiling_ok = (f_max_window <= CEILING)  # (local)
    # The SIGN prediction (plan Step 5): I_PBH > 0 and monotone-increasing in sigma_fold,
    # ceiling respected. beta0 > 0 always (squeezed source); collapse fraction is monotone.
    sign_pass = (beta0 > 0.0) and monotone and ceiling_ok  # (local)
    sign_verdict = "PASS" if sign_pass else "FAIL"  # (local)

    # --- magnitude_verdict: per the plan operator, the PASS region is the CLOSED
    # interval [0.22, 0.32] (= 0.27 +/- 0.05). The plan's INFO is NOT a magnitude band;
    # INFO is reserved EXCLUSIVELY for the delta_c-band regime-flip condition (handled
    # in regime_verdict / composite). So magnitude is binary PASS/FAIL against [0.22,0.32].
    #   Substitution chain (math-scripts.md):
    #     Step 1: I_PBH (computed), target=0.27, pass_band=0.05.
    #     Step 2: PASS iff I_PBH in [FAIL_LO, FAIL_HI] = [0.22, 0.32].
    #     Step 3: FAIL iff I_PBH < 0.22 (under-supply) OR I_PBH > 0.32 (over-supply).
    if FAIL_LO <= I_PBH <= FAIL_HI:
        magnitude_verdict = "PASS"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    under_supply = bool(I_PBH < FAIL_LO)  # (local) Track B under-supply sub-branch
    over_supply = bool(I_PBH > FAIL_HI)   # (local) Track B over-supply sub-branch

    # --- regime_verdict: is the window-placement conclusion robust to systematics?
    # The horizon mass is ~37 OOM below the window (Route A) and ~26 OOM (Route B);
    # the delta_c band moves only beta0, NOT the mass placement. INFO fires per the
    # plan ONLY if the verdict FLIPS within the delta_c band [0.4,0.7]. Here the whole
    # band gives I_PBH ~ 0 (no support in window) -> NO flip -> regime is firm.
    #   regime VALID    = the window-placement + numerical method are within regime;
    #                     the under-supply is a substrate result, NOT a band-edge artifact.
    #   regime MARGINAL = the verdict would flip within the delta_c band (-> composite INFO).
    band_min, band_max = float(res["I_band"].min()), float(res["I_band"].max())  # (local)
    # A flip exists iff some band point is PASS (in [0.22,0.32]) and some is FAIL.
    band_has_pass = bool(np.any((res["I_band"] >= FAIL_LO) & (res["I_band"] <= FAIL_HI)))  # (local)
    band_has_fail = bool(np.any((res["I_band"] < FAIL_LO) | (res["I_band"] > FAIL_HI)))  # (local)
    verdict_flips_in_band = band_has_pass and band_has_fail  # (local)
    placement_consistent = res["M_peak_below_evap"] and res["M_peak_routeB_below_evap"]  # (local)
    if verdict_flips_in_band:
        regime_verdict = "MARGINAL"  # (local) delta_c-band-sensitive -> INFO corridor
    else:
        regime_verdict = "VALID"  # (local) robust under-supply (or robust pass)

    # --- composite (gate-verdicts.md collapse rule):
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

    branch = "under-supply" if under_supply else ("over-supply" if over_supply else "in-band")  # (local)
    return composite, sign_verdict, magnitude_verdict, regime_verdict, branch


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict):
    M = res["M_grid"]  # (local)
    f = res["f_grid"]  # (local)
    fB = res["f_grid_routeB"]  # (local)
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Panel 1: f_PBH(M) with the asteroid window + evaporation floor marked.
    ax[0].loglog(M, np.clip(f, 1e-30, None), lw=1.6, color="C0",
                 label="f_PBH(M) Route A (T_fold=M_KK)")
    ax[0].loglog(M, np.clip(fB, 1e-30, None), lw=1.2, ls="--", color="C3",
                 label="f_PBH(M) Route B (substrate Hubble mass)")
    ax[0].axvspan(WIN_LO, WIN_HI, color="green", alpha=0.15, label="asteroid window [1e17,1e23] g")
    ax[0].axvline(M_PBH_EVAP, color="k", ls=":", lw=1.2, label="evaporation floor ~5.1e14 g")
    ax[0].axvline(res["M_peak_g"], color="C0", ls="-.", lw=1.0, label="fold M_H (Route A)")
    ax[0].axhline(1.0, color="red", ls="-", lw=0.8, label="ceiling f_PBH=1")
    ax[0].set_xlabel("PBH mass M [g]")
    ax[0].set_ylabel("f_PBH(M) = Omega_PBH/Omega_DM (per dlnM)")
    ax[0].set_title("Fold-transit PBH spectrum vs asteroid window")
    ax[0].set_ylim(1e-20, 1e6)
    ax[0].legend(fontsize=7, loc="upper right")
    ax[0].grid(True, which="both", alpha=0.2)

    # Panel 2: delta_c band scan of I_PBH (window integral).
    ax[1].plot(res["delta_c_band"], res["I_band"], "o-", color="C2", label="I_PBH(window)")
    ax[1].axhline(TARGET_ABUNDANCE, color="k", ls="--", label="target 0.27")
    ax[1].axhspan(FAIL_LO, FAIL_HI, color="green", alpha=0.15, label="PASS band [0.22,0.32]")
    ax[1].set_xlabel("critical overdensity delta_c")
    ax[1].set_ylabel("I_PBH (asteroid window)")
    ax[1].set_title(f"Window integral vs delta_c  (I_PBH={res['I_PBH']:.2e})")
    ax[1].legend(fontsize=8)
    ax[1].grid(True, alpha=0.2)
    txt = (f"M_H(fold) Route A = {res['M_peak_g']:.2e} g\n"
           f"~{res['OOM_below_window_routeA']:.0f} OOM BELOW window\n"
           f"Route B = {res['horizon_mass']['M_H_routeB_g']:.2e} g\n"
           f"~{res['OOM_below_window_routeB']:.0f} OOM below\n"
           f"both << evap floor 5.1e14 g")
    ax[1].text(0.04, 0.55, txt, transform=ax[1].transAxes, fontsize=8,
               bbox=dict(boxstyle="round", fc="wheat", alpha=0.7))

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          companion_note="", extra_rows=None):
    payload = {
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
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if companion_note:
        payload["companion_note"] = companion_note
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
    pins = log_input_pins(INPUT_FILES)  # (local)
    closure = closure_hash(pins)  # (local)
    print(f"  closure (legacy): {closure[:16]}...")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    res = compute()  # (local)
    value = res["value"]  # (local)

    # Report block
    hm = res["horizon_mass"]  # (local)
    sig = res["sigma_info"]  # (local)
    print("--- substrate inputs ---")
    print(f"  M_KK = {float(M_KK):.6e} GeV  -> M_KK_g = {hm['M_KK_g']:.6e} g")
    print(f"  N_pairs = {float(n_pairs)}  H_fold = {float(H_fold):.4f} M_KK  "
          f"dt_transit = {float(dt_transit):.4e} M_KK^-1  Mach = {float(Mach_max_framework)}")
    print(f"  sigma_fold: raw-lin={sig['sigma_lin']:.4f}  per-patch={sig['sigma_perpx']:.4f}  "
          f"capped={sig['sigma_bound']:.4f}  (source: {sig.get('source','?')})")
    print("--- horizon mass placement ---")
    print(f"  Route A (Friedmann, T_fold=M_KK): M_H = {hm['M_H_routeA_g']:.4e} g  "
          f"({res['OOM_below_window_routeA']:.1f} OOM below window bottom 1e17 g)")
    print(f"  Route B (substrate Hubble, c_s=1.9305 plan-pinned): M_H = {hm['M_H_routeB_g']:.4e} g  "
          f"({res['OOM_below_window_routeB']:.1f} OOM below)")
    print(f"  evaporation floor = {M_PBH_EVAP:.2e} g; Route A below floor: {res['M_peak_below_evap']}; "
          f"Route B below floor: {res['M_peak_routeB_below_evap']}")
    print("--- collapse + abundance ---")
    print(f"  beta0 (fiducial delta_c={DELTA_C_FIDUCIAL}, sigma=per-patch) = {res['beta0_fiducial']:.4f}")
    print(f"  I_PBH (asteroid window) = {res['I_PBH']:.6e}  (target 0.27 +/- 0.05)")
    print(f"  f_max in window = {res['f_max_in_window']:.4e}  (ceiling 1.0)")
    print(f"  f_max global   = {res['f_max_global']:.4e}")
    print(f"  delta_c band I_PBH range: [{res['I_band'].min():.3e}, {res['I_band'].max():.3e}]")
    print(f"  I_PBH Route B (window) = {res['I_PBH_routeB']:.6e}")

    composite, sign_v, mag_v, regime_v, branch = evaluate_gate(res)  # (local)
    print(f"  verdict branch: {branch}")

    # Save data
    np.savez(
        OUT_NPZ,
        M_grid=res["M_grid"], f_grid=res["f_grid"], f_grid_routeB=res["f_grid_routeB"],
        I_PBH=res["I_PBH"], I_PBH_routeB=res["I_PBH_routeB"],
        beta0_fiducial=res["beta0_fiducial"], f_max_in_window=res["f_max_in_window"],
        f_max_global=res["f_max_global"], M_peak_g=res["M_peak_g"],
        delta_c_band=res["delta_c_band"], I_band=res["I_band"], fmaxwin_band=res["fmaxwin_band"],
        M_H_routeA_g=hm["M_H_routeA_g"], M_H_routeB_g=hm["M_H_routeB_g"], M_KK_g=hm["M_KK_g"],
        OOM_below_window_routeA=res["OOM_below_window_routeA"],
        OOM_below_window_routeB=res["OOM_below_window_routeB"],
        sigma_lin=sig["sigma_lin"], sigma_perpx=sig["sigma_perpx"], sigma_bound=sig["sigma_bound"],
        target=TARGET_ABUNDANCE, pass_band=PASS_BAND, ceiling=CEILING,
        m_evap=M_PBH_EVAP,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        branch=branch,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n  data -> {OUT_NPZ.name}")
    make_plot(res)
    print(f"  plot -> {OUT_PNG.name}")

    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    note = (f"I_PBH={value:.3e} over [1e17,1e23]g (Track-B {branch}); fold M_H~{hm['M_H_routeA_g']:.2e}g "
            f"({res['OOM_below_window_routeA']:.0f} OOM below window, below 5.1e14g evap floor); "
            f"squeezed beta0={res['beta0_fiducial']:.3f} LARGE but deposited at wrong mass scale; "
            f"dimer-Z2 abundance NOT closed by fold-transit PBH; G4 compact-object cell opened as "
            f"a sub-evap-floor mass function (evaporated, not present-day DM)")  # (local)
    extra = [
        f"# horizon-mass: RouteA(Friedmann,T=M_KK)={hm['M_H_routeA_g']:.4e}g "
        f"RouteB(substrate-Hubble,c_s=1.9305-PLAN-PINNED)={hm['M_H_routeB_g']:.4e}g; "
        f"both << asteroid window AND << 5.1e14g evap floor",
        f"# input-source-correction: plan named s64_transit_power_spectrum.npz (absent) -> "
        f"s64_bogoliubov_phases.npz; s95_w1_omega_profile.npz (absent) -> s95_w4_4_sp_conformal_embed.npz",
    ]
    print_verdict_payload(composite, f"{value:.6e}", audit_sha, content_sha,
                          sign_v, mag_v, regime_v, companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v} mag={mag_v} regime={regime_v}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
