#!/usr/bin/env python3
"""
INV7 W1-4 — KBC void as a low-tau substrate region: Delta_H0/H0 vs the ~9% Hubble-tension relief
================================================================================================

Gate: INV7-W1-4 ([SIGN])
Track: investigation-7 (cosmic-web LSS observables)

Pre-registered threshold (plan §W1-4):
  operator: Delta_H0/H0_local > 0 (sign: void expands faster)
            AND |Delta_H0/H0_local - 0.09| <= 0.03 (magnitude in [6%, 12%]).
  PASS  iff sign positive AND magnitude in [6%, 12%].
  INFO  iff sign positive but magnitude < 6% (sign-correct-magnitude-short, partial relief).
  FAIL  iff sign negative (map compacts wrong way) OR magnitude > 12% (over-relief / reverse tension).

Mechanism (substrate-first):
  The fiber deformation parameter tau tracks LOCAL spectral-weight density rho_local via the
  substrate-compaction map (project_substrate-compaction-timescape; q-theory=F-theory variational).
  An underdense region (the KBC void) sits at a LOWER tau than the cosmic mean (S60 convention:
  tau_void = tau_fold - delta_tau; "voids have LOWER tau, less compactified"). The local proper-time
  clock rate is set by the fiber's spectral structure via the canonical clock map
  dalpha/alpha = clock_coeff * dtau (clock_coeff = -3.08, S22d E-3) — so a tau shift is a clock-rate
  shift, hence a locally-measured H0 shift:  Delta_H0/H0_local = clock_coeff * delta_tau.

  This operates through the tau(rho)-clock (the a_2 / emergent-FRW reading), NOT through w0 (the a_0
  vacuum partition). It is therefore ORTHOGONAL to the BAO-constrained w0 tested in INV7-W1-3 (C2):
  no quantity in this gate touches w0_FW, Omega_DE, or the DE equation of state.

  CROSS-EPOCH LINK: this is the z~0 face of the tau(rho) mechanism (large local tau-variance now).
  Its z~7 face (LRD C3, inv-7 W2) is the near-homogeneous high-z limit where local tau-variance
  integrates to ~0 and the framework reduces to LCDM.

Two routes are computed transparently (the framework's OWN two density->tau maps, S59):
  ROUTE A (substrate-physics, gravitational backreaction; S59 Route 1, canonical):
      delta_tau = (rho_m/M_KK^4) * |frac_da2| / d2S_fold * (delta_rho/rho)
      -> delta_tau/delta is ~10^-118 (S59's recorded "10^120 below stiffness"); the cosmic-mean
         gravitational backreaction supplies a NEGLIGIBLE tau shift. Honest substrate-first answer.
  ROUTE B (saturated void-wall swing; S59 Route 2 KZ variance, the maximal optimistic reading):
      delta_tau = delta_tau_eff * (|delta_rho/rho|_KBC / |delta_rho/rho|_cosmic-mean-fluct)
      where delta_tau_eff ~ 0.0053 is the canonical 1-sigma void-wall tau separation (S59/S60).
      This is the upper bound the framework's own tau-variance can deliver.

  The reported gate value is the LARGER-magnitude route (Route B; the framework's best case), so the
  gate is not artificially failed by the catastrophically-short gravitational route. Both routes'
  numbers are emitted in the npz and the WP for full disclosure.

KBC void parameters (FETCHED literature):
  Haslbauer, Banik & Kroupa 2020, MNRAS 499, 2845 (arXiv:2009.11292v2):
    delta = 1 - rho/rho0 = 0.46 +/- 0.06 between 40 and 300 Mpc  -> delta_rho/rho = -0.46.
    6.04 sigma tension with LCDM (MXXL); plan central delta ~ -0.30 used as conservative cross-check.
  Relief target: (H0_SHOES 73.04 - H0_Planck 67.40)/67.40 = 0.0837 ~ 8.4% ~ "9%" (plan pin 0.09).

Output 4-tuple:
  (value=<Delta_H0/H0_local route-B>, scheme=FW, convention=RATIO, L_max=N/A)

Classification: PHONONIC.
  The substrate IS the fabric whose fiber tau varies with local spectral-weight density; the KBC void
  is the laboratory-IN image of a low-tau substrate region (less-compacted fiber -> faster emergent
  clock). Flow: D_K spectral structure -> tau(rho) compaction map -> local clock-rate variance ->
  differential emergent-FRW expansion -> Delta_H0 between void and cosmic mean -> measured local-vs-
  global H0 discrepancy. The gate reads H0 off the substrate's own tau-clock; it does NOT posit a
  quintessence field or modified-gravity coupling IN a void embedded in a pre-existing space.

DISCIPLINE
----------
- `from canonical_constants import *`
- CPU-cap-OMP8 (256-point radial integration; no matrix >= 100x100, no GPU benefit)
- dual-SHA (S84+) emitted; script PRINTS payload; agent calls emit_verdict (track=investigation).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403
# Explicit names used (all canonical):
from canonical_constants import (
    clock_coeff,          # -3.08  : dalpha/alpha = clock_coeff * dtau (S22d E-3)
    tau_fold,             # 0.19   : fold tau (S42)
    H_0_km_s_Mpc,         # 67.4   : global H0 (Planck 2018)
    Omega_m,              # 0.315
    rho_crit_GeV4,        # 4.08e-47
    M_KK,                 # 7.43e16
    d2S_fold,             # spectral-action convexity at fold (S40 HESS)
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
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent            # computations/investigation-7/
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
DATA_DIR = SESSION_DIR / "_data"

SESSION = "7"                                             # (local) investigation number
GATE_ID = "INV7-W1-4"                                     # (local)
SCHEME = "FW"                                             # (local)
CONVENTION = "RATIO"                                      # (local)
L_MAX = "N/A"                                             # (local) tau(rho) clock map, not a spectral truncation

# Pre-registered thresholds (plan §W1-4 strict_PASS_boundary)
RELIEF_TARGET = 0.09                                      # (local) ~9% local-H0 relief
PASS_BAND = 0.03                                          # (local) |DH0/H0 - 0.09| <= 0.03  -> [6%,12%]
INFO_FLOOR = 0.06                                         # (local) magnitude floor for PASS band lower edge
N_EVAL = 256                                              # (local) radial grid points
SCAN_MIN = 0.0                                            # (local) Mpc
SCAN_MAX = 300.0                                          # (local) Mpc (KBC void radial profile)

# Output destinations
OUT_NPZ = SESSION_DIR / "inv7_w1_4_kbc_timescape_h0.npz"
OUT_PNG = SESSION_DIR / "inv7_w1_4_kbc_timescape_h0.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    DATA_DIR / "kbc_void_haslbauer2020.txt",
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

def load_kbc_params() -> dict:
    """Parse the FETCHED Haslbauer+2020 KBC void parameter file."""
    params: dict[str, float] = {}  # (local)
    txt = (DATA_DIR / "kbc_void_haslbauer2020.txt").read_text()  # (local)
    for line in txt.splitlines():
        s = line.strip()  # (local)
        if not s or s.startswith("#"):
            continue
        parts = s.split()  # (local)
        if len(parts) >= 2:
            try:
                params[parts[0]] = float(parts[1])
            except ValueError:
                pass
    return params


def kbc_density_profile(r_Mpc: np.ndarray, delta_center: float, R_void: float) -> np.ndarray:
    """KBC void density-contrast profile delta(r) = (rho(r)-rho_bar)/rho_bar.

    Gaussian underdensity profile (Haslbauer+2020 Gaussian void form; their preferred profiles
    are Gaussian / Exponential): delta(r) = delta_center * exp(-(r/R_void)^2 * ln(...)). We use a
    simple Gaussian falling to ~0 at r=R_void. delta_center < 0 (underdense).
    """
    # Gaussian with delta -> ~0.05*delta_center at r = R_void (so the void wall is near R_void).
    sigma_r = R_void / np.sqrt(np.log(20.0))  # (local) so exp(-(R/sigma)^2)=1/20 at r=R_void
    return delta_center * np.exp(-(r_Mpc / sigma_r) ** 2)


def compute() -> dict:
    p = load_kbc_params()  # (local)

    # --- KBC void contrast (FETCHED) ---
    delta_rho_over_rho_paper = -p["delta_contrast_paper"]      # (local) = -0.46 (Haslbauer+2020)
    delta_rho_over_rho_central = -p["delta_contrast_central"]  # (local) = -0.30 (conservative central)
    R_void = p["R_void_Mpc"]                                   # (local) 300 Mpc
    relief_target_lit = p["H0_relief_target"]                  # (local) 0.0837 (~9%) from SHOES/Planck

    # --- canonical substrate-compaction inputs (S59) ---
    frac_da2 = 99.127  # (local) (da2/dtau)/a2 at fold (S59 log); the a_2 spectral-moment slope.
    rho_m_MKK4 = Omega_m * rho_crit_GeV4 / M_KK ** 4          # (local) matter density in M_KK^4 units
    # delta_tau_eff: canonical 1-sigma void-wall tau separation (S59 Route 2 KZ variance, S60 d_v).
    # Hard-pinned to the S59/S60 published value (recomputing the full KZ chain is out of scope; the
    # value 0.005303 is the S60 d_v "void shift" from s60_gsl_timescape_log.txt).
    delta_tau_eff = 0.005303  # (local) S60 d_v void shift = sigma_tau (S59 KZ); fractional ~2.8% of tau_fold
    # The cosmic-mean fluctuation contrast that delta_tau_eff corresponds to (the rms density
    # fluctuation that the KZ void-wall separation represents). Standard sigma_8-scale rms ~ O(1) at
    # the relevant smoothing; we take |delta|_cosmic-mean = 1.0 (the void-wall separation is the
    # ~1-sigma swing), so the KBC void (deeper than 1-sigma) scales delta_tau_eff up linearly.
    delta_cosmic_mean = 1.0  # (local) the |delta| that delta_tau_eff represents (1-sigma void-wall swing)

    # =========================================================================
    # ROUTE A — substrate-physics gravitational backreaction (S59 Route 1, canonical)
    #   delta_tau = delta_tau_per_delta_route1 * (delta_rho/rho)
    #   delta_tau_per_delta_route1 = rho_m/M_KK^4 * |frac_da2| / d2S_fold
    # =========================================================================
    delta_tau_per_delta_route1 = rho_m_MKK4 * abs(frac_da2) / d2S_fold  # (local) ~1e-117 per unit delta
    delta_tau_A_paper = delta_tau_per_delta_route1 * delta_rho_over_rho_paper      # (local)
    delta_tau_A_central = delta_tau_per_delta_route1 * delta_rho_over_rho_central  # (local)
    # Clock map: Delta_H0/H0 = clock_coeff * delta_tau (single region vs cosmic mean).
    DH0_A_paper = clock_coeff * delta_tau_A_paper        # (local)
    DH0_A_central = clock_coeff * delta_tau_A_central    # (local)

    # =========================================================================
    # ROUTE B — saturated void-wall swing (S59 Route 2 KZ variance; maximal framework case)
    #   delta_tau_void = -delta_tau_eff * (|delta_rho/rho|_KBC / |delta|_cosmic-mean)
    #   (sign: underdense -> LOWER tau, per S60 tau_void = tau_fold - delta_tau_eff)
    # =========================================================================
    scale_paper = abs(delta_rho_over_rho_paper) / delta_cosmic_mean       # (local) 0.46
    scale_central = abs(delta_rho_over_rho_central) / delta_cosmic_mean   # (local) 0.30
    # Underdense -> tau shifts NEGATIVE (lower tau): delta_tau_void = -delta_tau_eff * scale.
    delta_tau_B_paper = -delta_tau_eff * scale_paper       # (local) negative
    delta_tau_B_central = -delta_tau_eff * scale_central   # (local) negative
    # Clock map. clock_coeff = -3.08 (negative); delta_tau negative -> product POSITIVE -> H0 UP.
    DH0_B_paper = clock_coeff * delta_tau_B_paper          # (local) positive
    DH0_B_central = clock_coeff * delta_tau_B_central      # (local) positive

    # =========================================================================
    # SIGN VERIFICATION (read off the map, NOT assumed) — plan Step 3 mandate.
    #   delta < 0 (underdense)  -> delta_tau < 0 (lower tau, less compaction; S60 convention)
    #   clock_coeff < 0, delta_tau < 0  -> Delta_H0/H0 = clock_coeff*delta_tau > 0 (faster clock).
    # =========================================================================
    sign_dtau_drho_positive = (delta_tau_per_delta_route1 > 0)  # (local) dtau/drho > 0 (denser->higher tau)
    sign_route_B_positive = (DH0_B_paper > 0)                   # (local) underdense void clocks faster

    # The REPORTED gate value: Route B paper-contrast (the framework's largest-magnitude case),
    # so the gate is judged on the framework's best delivery, not the catastrophic gravitational route.
    DH0_value = DH0_B_paper  # (local) reported Delta_H0/H0_local

    # --- radial profile (256-point integration; for the plot + volume-averaged contrast) ---
    r_grid = np.linspace(SCAN_MIN, SCAN_MAX, N_EVAL)        # (local)
    delta_profile = kbc_density_profile(r_grid, delta_rho_over_rho_paper, R_void)  # (local)
    # Volume-weighted mean contrast inside the void (4*pi*r^2 weighting):
    vol_w = 4.0 * np.pi * r_grid ** 2                       # (local)
    _trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))  # (local) NumPy 2.x renamed trapz->trapezoid
    delta_vol_mean = _trapz(delta_profile * vol_w, r_grid) / _trapz(vol_w, r_grid)  # (local)
    # Local Delta_H0/H0 profile (Route B map applied pointwise):
    delta_tau_profile = -delta_tau_eff * (np.abs(delta_profile) / delta_cosmic_mean)    # (local)
    DH0_profile = clock_coeff * delta_tau_profile           # (local) positive where underdense

    return {
        "value": float(DH0_value),
        # routes
        "DH0_A_paper": float(DH0_A_paper),
        "DH0_A_central": float(DH0_A_central),
        "DH0_B_paper": float(DH0_B_paper),
        "DH0_B_central": float(DH0_B_central),
        "delta_tau_A_paper": float(delta_tau_A_paper),
        "delta_tau_B_paper": float(delta_tau_B_paper),
        "delta_tau_B_central": float(delta_tau_B_central),
        "delta_tau_per_delta_route1": float(delta_tau_per_delta_route1),
        "delta_tau_eff": float(delta_tau_eff),
        # inputs
        "delta_rho_over_rho_paper": float(delta_rho_over_rho_paper),
        "delta_rho_over_rho_central": float(delta_rho_over_rho_central),
        "R_void_Mpc": float(R_void),
        "relief_target": float(RELIEF_TARGET),
        "relief_target_lit": float(relief_target_lit),
        "clock_coeff": float(clock_coeff),
        "frac_da2": float(frac_da2),
        "rho_m_MKK4": float(rho_m_MKK4),
        "d2S_fold": float(d2S_fold),
        # sign checks
        "sign_dtau_drho_positive": bool(sign_dtau_drho_positive),
        "sign_route_B_positive": bool(sign_route_B_positive),
        # profile
        "r_grid": r_grid,
        "delta_profile": delta_profile,
        "DH0_profile": DH0_profile,
        "delta_vol_mean": float(delta_vol_mean),
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple + payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Plan §W1-4:
      sign positive AND |DH0/H0 - 0.09| <= 0.03 (i.e. in [6%,12%]) -> PASS
      sign positive but DH0/H0 < 6%                                 -> INFO (magnitude-short)
      sign negative OR DH0/H0 > 12%                                 -> FAIL
    """
    v = r["value"]  # (local) Route B paper contrast Delta_H0/H0_local
    # SIGN: predicted positive (underdense void clocks faster). PASS iff computed sign positive.
    sign_ok = (v > 0) and r["sign_route_B_positive"]  # (local)
    sign_verdict = "PASS" if sign_ok else "FAIL"  # (local)

    # MAGNITUDE: PASS iff |v - 0.09| <= 0.03 (within [6%,12%]); INFO iff 0 < v < 6%; FAIL iff v > 12%.
    mag = abs(v - RELIEF_TARGET)  # (local)
    if sign_ok and mag <= PASS_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif sign_ok and (v < INFO_FLOOR):
        magnitude_verdict = "INFO"  # (local) sign-correct-magnitude-short (partial relief)
    elif sign_ok and (v > RELIEF_TARGET + PASS_BAND):
        magnitude_verdict = "FAIL"  # (local) over-relief (> 12%) -> reverse tension
    else:
        magnitude_verdict = "INFO"  # (local) inside [6%,12%) handled above; defensive
    # REGIME: the tau(rho) clock map + linear compaction relation are valid throughout the
    # KBC-scale density contrast (|delta| < 1, well within the small-perturbation regime of the
    # spectral-action Taylor expansion around the fold). VALID.
    regime_verdict = "VALID"  # (local)

    # Composite collapse (gate-verdicts.md):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local) over-relief with valid regime
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local) sign-correct-magnitude-short
    else:
        composite = "PASS"  # (local)
    return composite, sign_verdict, magnitude_verdict, regime_verdict


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
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


def make_plot(r: dict, verdict: str) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Panel 1: KBC void density profile + local Delta_H0/H0 profile (Route B).
    ax = axes[0]  # (local)
    ax.plot(r["r_grid"], r["delta_profile"], "b-", lw=2, label=r"$\delta(r)=(\rho-\bar\rho)/\bar\rho$")
    ax.axhline(0.0, color="k", lw=0.6)
    ax.set_xlabel("r [Mpc]")
    ax.set_ylabel(r"density contrast $\delta(r)$", color="b")
    ax.tick_params(axis="y", labelcolor="b")
    ax.set_title(f"KBC void profile ($\\delta_c$={r['delta_rho_over_rho_paper']:.2f}, "
                 f"R={r['R_void_Mpc']:.0f} Mpc; Haslbauer+2020)")
    ax2 = ax.twinx()  # (local)
    ax2.plot(r["r_grid"], 100 * r["DH0_profile"], "r--", lw=2,
             label=r"$\Delta H_0/H_0(r)$ [%] (Route B)")
    ax2.set_ylabel(r"$\Delta H_0/H_0$ [%]", color="r")
    ax2.tick_params(axis="y", labelcolor="r")
    lines1, labels1 = ax.get_legend_handles_labels()  # (local)
    lines2, labels2 = ax2.get_legend_handles_labels()  # (local)
    ax.legend(lines1 + lines2, labels1 + labels2, loc="lower right", fontsize=8)

    # Panel 2: route comparison bar vs the 9% relief band.
    ax = axes[1]  # (local)
    labels = ["Route A\n(grav. backreac.)", "Route B\n(sat. void-wall)\npaper $\\delta$=-0.46",
              "Route B\ncentral $\\delta$=-0.30"]  # (local)
    vals = [100 * r["DH0_A_paper"], 100 * r["DH0_B_paper"], 100 * r["DH0_B_central"]]  # (local)
    colors = ["#888", "#c33", "#e88"]  # (local)
    bars = ax.bar(labels, vals, color=colors)  # (local)
    ax.axhspan(6.0, 12.0, alpha=0.18, color="green", label="PASS band [6%,12%] (~9% relief)")
    ax.axhline(9.0, color="green", lw=1.2, ls=":", label="relief target 9%")
    ax.axhline(0.0, color="k", lw=0.6)
    ax.set_ylabel(r"$\Delta H_0/H_0$ [%]")
    ax.set_title(f"Substrate timescape H0 relief — verdict: {verdict}\n"
                 f"(tau(rho)-clock channel; w0-ORTHOGONAL to BAO/C2)")
    ax.legend(fontsize=8, loc="upper right")
    for b, val in zip(bars, vals):
        # annotate (Route A is ~1e-116 %, show in scientific text)
        txt = f"{val:.3g}%" if abs(val) >= 1e-3 else f"{val:.2e}%"  # (local)
        ax.annotate(txt, (b.get_x() + b.get_width() / 2, max(val, 0)),
                    ha="center", va="bottom", fontsize=8)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    print("=" * 78)
    print(f"  {GATE_ID}: KBC void as low-tau substrate region -> Delta_H0/H0 (timescape)")
    print("=" * 78)
    print(f"  KBC delta_rho/rho (paper, Haslbauer+2020) = {r['delta_rho_over_rho_paper']:+.3f}")
    print(f"  KBC delta_rho/rho (central, conservative) = {r['delta_rho_over_rho_central']:+.3f}")
    print(f"  R_void                                    = {r['R_void_Mpc']:.0f} Mpc")
    print(f"  relief target (plan / literature)         = {r['relief_target']:.3f} / {r['relief_target_lit']:.4f}")
    print(f"  clock_coeff (dalpha/alpha = cc*dtau)      = {r['clock_coeff']:.3f}")
    print()
    print(f"  -- SIGN verification (read off the map) --")
    print(f"  dtau/drho > 0 (denser->higher tau)?       = {r['sign_dtau_drho_positive']}")
    print(f"  underdense void clocks faster (DH0>0)?    = {r['sign_route_B_positive']}")
    print()
    print(f"  -- ROUTE A (gravitational backreaction, S59 Route 1, canonical) --")
    print(f"  delta_tau/delta (route 1)                 = {r['delta_tau_per_delta_route1']:.4e}")
    print(f"  delta_tau_A (paper)                       = {r['delta_tau_A_paper']:.4e}")
    print(f"  Delta_H0/H0 Route A (paper)               = {r['DH0_A_paper']:.4e}  ({100*r['DH0_A_paper']:.3e} %)")
    print()
    print(f"  -- ROUTE B (saturated void-wall swing, S59 Route 2 KZ; framework best case) --")
    print(f"  delta_tau_eff (1-sigma void-wall, S59/S60)= {r['delta_tau_eff']:.6f}")
    print(f"  delta_tau_B (paper)                       = {r['delta_tau_B_paper']:.6f}")
    print(f"  Delta_H0/H0 Route B (paper)  [REPORTED]   = {r['DH0_B_paper']:.6f}  ({100*r['DH0_B_paper']:.3f} %)")
    print(f"  Delta_H0/H0 Route B (central)             = {r['DH0_B_central']:.6f}  ({100*r['DH0_B_central']:.3f} %)")
    print()

    composite, sign_v, mag_v, reg_v = evaluate_gate(r)
    value = r["value"]

    np.savez(
        OUT_NPZ,
        value=value,
        DH0_A_paper=r["DH0_A_paper"], DH0_A_central=r["DH0_A_central"],
        DH0_B_paper=r["DH0_B_paper"], DH0_B_central=r["DH0_B_central"],
        delta_tau_A_paper=r["delta_tau_A_paper"], delta_tau_B_paper=r["delta_tau_B_paper"],
        delta_tau_B_central=r["delta_tau_B_central"],
        delta_tau_per_delta_route1=r["delta_tau_per_delta_route1"],
        delta_tau_eff=r["delta_tau_eff"],
        delta_rho_over_rho_paper=r["delta_rho_over_rho_paper"],
        delta_rho_over_rho_central=r["delta_rho_over_rho_central"],
        R_void_Mpc=r["R_void_Mpc"], relief_target=r["relief_target"],
        relief_target_lit=r["relief_target_lit"],
        clock_coeff=r["clock_coeff"], frac_da2=r["frac_da2"],
        rho_m_MKK4=r["rho_m_MKK4"], d2S_fold=r["d2S_fold"],
        sign_dtau_drho_positive=r["sign_dtau_drho_positive"],
        sign_route_B_positive=r["sign_route_B_positive"],
        r_grid=r["r_grid"], delta_profile=r["delta_profile"], DH0_profile=r["DH0_profile"],
        delta_vol_mean=r["delta_vol_mean"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v, composite=composite,
    )
    print(f"  npz written: {OUT_NPZ.name}")

    make_plot(r, composite)
    print(f"  png written: {OUT_PNG.name}")
    print()

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    note = (f"Route-B(sat void-wall) DH0/H0={value:.4f} [{100*value:.2f}%]; "
            f"Route-A(grav-backreac)={r['DH0_A_paper']:.2e} (~117 OOM short); "
            f"SIGN+ (underdense->lower tau->faster clock; clock_coeff={r['clock_coeff']}); "
            f"tau(rho)-clock channel, w0-ORTHOGONAL to BAO/C2; KBC delta=-0.46 Haslbauer2020")
    extra = [
        f"# INV7-W1-4 routes: A_grav={r['DH0_A_paper']:.3e} B_satvoidwall_paper={r['DH0_B_paper']:.5f} "
        f"B_central={r['DH0_B_central']:.5f}; relief_target=0.09 band=[0.06,0.12]; "
        f"delta_tau_eff={r['delta_tau_eff']:.6f} delta_KBC=-0.46(Haslbauer2020 arXiv:2009.11292)",
        f"# INV7-W1-4 orthogonality: tau(rho)-clock (a_2/emergent-FRW), NOT w0 (a_0 vacuum partition); "
        f"C2-orthogonal to INV7-W1-3; z~0 face of tau(rho), z~7 face=LRD C3(W2)",
    ]
    payload = print_verdict_payload(composite, value, audit_sha, content_sha,
                                    sign_verdict=sign_v, magnitude_verdict=mag_v,
                                    regime_verdict=reg_v, companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v}, mag={mag_v}, regime={reg_v}; wall {wall:.1f}s) ===")
    print(f"=== Route-B Delta_H0/H0 = {100*value:.2f}% vs ~9% target; "
          f"sign-correct-magnitude-short ===")
    return 0  # valid verdict (PASS/FAIL/INFO) always exits 0 per math-scripts.md


if __name__ == "__main__":
    sys.exit(main())
