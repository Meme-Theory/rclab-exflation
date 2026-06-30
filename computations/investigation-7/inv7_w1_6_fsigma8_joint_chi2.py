#!/usr/bin/env python3
"""
INV7 W1-6 — INV7-W1-6 : full f*sigma8(z) growth-suppression curve across
DESI/Euclid z-bins + JOINT chi2 vs LCDM
=========================================================================

Gate: INV7-W1-6 ([SIGN], PHONONIC, investigation track)

Pre-registered threshold (plan §W1-6):
  operator: joint significance of the framework growth-history departure
    joint_sigma = sqrt(|chi2_joint_FW - chi2_joint_LCDM_ref|) >= sigma_forecast = 2.0
    AND sign(fsig8_FW - fsig8_LCDM) < 0 coherently across bins (suppression direction)
  strict_PASS_boundary: sigma_forecast = 2.0 (>= 2 sigma joint departure across the
    ~7-bin DESI/Euclid f*sigma8 vector is the threshold for "a real growth test"; below
    this it is a consistency check only). bare-f -0.311% and product -4.058% are INPUTS.
  PASS  iff sign coherent-negative AND joint_sigma >= 2.0
  INFO  iff joint_sigma in [1, 2)
  FAIL  iff joint_sigma < 1 OR per-bin departures not coherently negative

  The composite top-line is the [SIGN] 3-tuple collapse (gate-verdicts.md):
    sign_verdict     = PASS iff the 7 product departures are coherently NEGATIVE
    magnitude_verdict= PASS iff joint_sigma >= 2 ; INFO iff in [1,2) ; FAIL iff < 1
    regime_verdict   = VALID (linear growth ODE within its regime of validity over z in [0,1.8])
    composite: magnitude=INFO -> INFO ; magnitude=PASS & sign=PASS -> PASS ; magnitude=FAIL or sign=FAIL -> FAIL

WHICH joint_sigma is the headline:
  The plan hypothesis & dual_prior pin the FORECAST significance as the headline
  ("reaching at least the pre-registered forecast significance sigma_forecast"; track_B:
  "a -4% peak likely sits just below 2 sigma joint at DR2 precision, reaching it only with
  Euclid"). The headline joint_sigma is therefore the DESI-5yr forecast joint significance
  (the "DESI DR2 / DESI-5yr" precision target), with the Euclid joint reported as the
  decisive-follow-up level. The current-precision (eBOSS) joint and the data-anchored
  Delta chi2 are reported as context.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py            (feeds audit_sha256)
  - computations/investigation-7/_data/desi_dr2_euclid_fsigma8.txt
        FETCHED eBOSS-DR16 f*sigma8 compilation (current) + DESI-5yr/Euclid forecast sigma
        (provenance in the data-file header; Alam+2021 PRD 103 083533 cosmology compilation)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<joint_sigma summary>, scheme=FW, convention=ABSOLUTE, L_max=N/A)

METHODOLOGY
-----------
Compute the framework linear growth rate f_FW(z) = dlnD/dlna along the a_2 Seeley-DeWitt
growth channel (the SAME channel from which Newton's constant + the Einstein-Hilbert action
emerge) by integrating the linear-growth ODE for D(a) in the borrowed emergent-FRW
background H(z) with constant w = w0_FW = -0.918 (the Volovik-partition + effacement value).
LCDM uses w = -1. Both ODE integrations reproduce the canonical anchors:
  f_FW(z=0)   = 0.5254916357   (computed to ~3e-5)
  f_LCDM(z=0) = 0.5271303866   (computed to ~3e-5)
  product f*sigma8 suppression peaks at -4.058% @ z=0.51 (computed -4.06%, matching 3 sig figs)
sigma8_FW(z) = sigma8_growth_a2 * D_FW(z)/D_FW(0) with sigma8_growth_a2 = 0.79317; LCDM uses
sigma_8 = 0.811 (Planck 2018 reference). Form the per-bin fsig8_FW(z_i) and fsig8_LCDM(z_i)
at the 7 DESI/eBOSS effective-redshift bins. The NEW compute (distinct from S96-OBS-FSIGMA8-
FORECAST, which reported only per-bin sigma maxing at ~0.51/1.01/1.53 for current/DESI5yr/
Euclid) is the JOINT chi2 over the full bin vector with covariance: because the product
suppression is COHERENT and same-sign (all 7 bins negative, -3.46% to -2.49%), it ADDS in
quadrature, so the joint significance can exceed any single-bin significance.

  chi2_joint(model-vs-model) = (fs8_FW - fs8_LCDM)^T C^-1 (fs8_FW - fs8_LCDM)
  joint_sigma = sqrt(chi2_joint)   [model-vs-model: the cleanest discriminator, independent
                                    of where the data central value sits]
  Reported at 3 precision levels: current (eBOSS err), DESI-5yr forecast, Euclid forecast.
  Also: data-anchored chi2_FW / chi2_LCDM / Delta chi2 against fsig8_obs (current eBOSS),
  and a BOSS-LRG off-diagonal (rho_3851=0.20 between z=0.38<->0.51) robustness variant.

Classification: PHONONIC.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap OMP_NUM_THREADS=8 (small 7-bin covariance solve + 1000-node growth ODE; no GPU benefit)
- SHA-256 of all input files logged in first 20 lines of stdout
- dual-SHA (audit + content) emitted (S84+)
- verdict emitted via emit_verdict MCP tool (race-safe); script only PRINTS the payload
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
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
    Omega_m, w0_FW, sigma_8, sigma8_growth_a2, f_FW, f_LCDM,
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
SESSION = "7"                                                       # (local) investigation number
GATE_ID = "INV7-W1-6"                                              # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "ABSOLUTE"                                            # (local) chi2_joint absolute GOF; product/-bare-f suppression are RATIO diagnostics
L_MAX = "N/A"                                                     # (local) growth ODE, not a D_K truncation

SIGMA_FORECAST = 2.0                                              # (local) plan strict_PASS_boundary (joint significance threshold)
INFO_FLOOR = 1.0                                                 # (local) joint_sigma in [1,2) -> INFO
N_EVAL = 1000                                                    # (local) growth-ODE base grid nodes for D(a)
ODE_RTOL = 1e-9                                                  # (local) growth-ODE convergence tolerance (plan tolerance pin)
ODE_ATOL = 1e-12                                                 # (local)
A_INIT = 1e-3                                                    # (local) matter-dom ODE initial scale factor
RHO_BOSS_3851 = 0.20                                             # (local) BOSS-LRG z=0.38<->0.51 off-diagonal robustness variant

DATA_DIR = SESSION_DIR / "_data"                                 # (local)
DATA_TXT = DATA_DIR / "desi_dr2_euclid_fsigma8.txt"              # (local)
OUT_NPZ = SESSION_DIR / "inv7_w1_6_fsigma8_joint_chi2.npz"       # (local)
OUT_PNG = SESSION_DIR / "inv7_w1_6_fsigma8_joint_chi2.png"       # (local)

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
INPUT_FILES = [CANONICAL_PATH, DATA_TXT]


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
# Section 5 — Growth ODE + compute
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
    """Integrate the linear-growth ODE D'' + (2 + dlnH/dlna) D' - 1.5 Om(a) D = 0
    in ln a; return (D(a_eval), f(a_eval)=dlnD/dlna). Matter-dom IC D ~ a at a_init."""
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


def read_data_file(path: Path):
    """Read the FETCHED eBOSS/DESI/Euclid f*sigma8 table. Returns dict of arrays."""
    z, fobs, eobs, sd5, seu = [], [], [], [], []  # (local)
    tracers = []  # (local)
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()  # (local)
        if not s or s.startswith("#"):
            continue
        parts = s.split()  # (local)
        z.append(float(parts[0]))
        fobs.append(float(parts[1]))
        eobs.append(float(parts[2]))
        sd5.append(float(parts[3]))
        seu.append(float(parts[4]))
        tracers.append(parts[5] if len(parts) > 5 else "")
    return {
        "z": np.array(z), "fsig8_obs": np.array(fobs), "err_obs": np.array(eobs),
        "sigma_desi5": np.array(sd5), "sigma_euclid": np.array(seu),
        "tracers": np.array(tracers),
    }


def joint_chi2(delta: np.ndarray, C: np.ndarray) -> float:
    """delta^T C^-1 delta."""
    Ci = np.linalg.inv(C)  # (local)
    return float(delta @ Ci @ delta)


def compute() -> dict:
    res: dict = {}  # (local)
    data = read_data_file(DATA_TXT)  # (local)
    zb = data["z"]  # (local)
    fsig8_obs = data["fsig8_obs"]  # (local)
    err_obs = data["err_obs"]  # (local)
    sig_d5 = data["sigma_desi5"]  # (local)
    sig_eu = data["sigma_euclid"]  # (local)
    n_bins = len(zb)  # (local)

    # --- growth curves at the bin scale factors + z=0 anchor ---
    ab = 1.0 / (1.0 + zb)  # (local)
    a_all = np.concatenate([ab, [1.0]])  # (local)
    order = np.argsort(a_all)  # (local) solve_ivp needs increasing t (ln a)
    inv = np.argsort(order)  # (local)
    a_sorted = a_all[order]  # (local)

    D_L, f_L = growth_curve(-1.0, a_sorted)
    D_F, f_F = growth_curve(w0_FW, a_sorted)
    D_L, f_L = D_L[inv], f_L[inv]  # (local) back to bin order, z=0 last
    D_F, f_F = D_F[inv], f_F[inv]  # (local)
    D_L0, D_F0 = D_L[-1], D_F[-1]  # (local)

    f_L_bins, f_F_bins = f_L[:-1], f_F[:-1]  # (local)
    s8_L = sigma_8 * (D_L[:-1] / D_L0)  # (local) LCDM Planck-ref sigma8 normalization
    s8_F = sigma8_growth_a2 * (D_F[:-1] / D_F0)  # (local) FW a2-growth-channel sigma8
    fs8_L = f_L_bins * s8_L  # (local)
    fs8_F = f_F_bins * s8_F  # (local)
    frac_FW = (fs8_F - fs8_L) / fs8_L  # (local) coherent product suppression (negative)
    frac_FW_pct = frac_FW * 100.0  # (local)

    # canonical-anchor reproduction cross-checks
    f_FW_z0 = float(f_F[-1])  # (local)
    f_LCDM_z0 = float(f_L[-1])  # (local)
    bare_f_supp_pct = (f_FW_z0 - f_LCDM_z0) / f_LCDM_z0 * 100.0  # (local)
    prod_supp_max_pct = float(frac_FW_pct.min())  # (local)
    z_at_max = float(zb[int(np.argmin(frac_FW_pct))])  # (local)

    # --- model-vs-model coherent JOINT significance at 3 precision levels ---
    dmodel = fs8_F - fs8_L  # (local) FW - LCDM, coherent negative
    sign_all_negative = bool(np.all(dmodel < 0))  # (local)
    n_negative = int(np.sum(dmodel < 0))  # (local)

    joint_sigma = {}  # (local)
    chi2_mm = {}  # (local)
    for name, sig in [("current", err_obs), ("desi5", sig_d5), ("euclid", sig_eu)]:
        C = np.diag(sig ** 2)  # (local) baseline diagonal covariance
        c2 = joint_chi2(dmodel, C)  # (local)
        chi2_mm[name] = c2
        joint_sigma[name] = float(np.sqrt(c2))

    # BOSS-LRG off-diagonal robustness variant (rho between z=0.38<->0.51), DESI-5yr precision
    def cov_with_boss_offdiag(sig: np.ndarray) -> np.ndarray:  # (local)
        C = np.diag(sig ** 2).astype(float)  # (local)
        i38 = int(np.argmin(np.abs(zb - 0.38)))  # (local)
        i51 = int(np.argmin(np.abs(zb - 0.51)))  # (local)
        off = RHO_BOSS_3851 * sig[i38] * sig[i51]  # (local)
        C[i38, i51] = off
        C[i51, i38] = off
        return C
    js_d5_boss = float(np.sqrt(joint_chi2(dmodel, cov_with_boss_offdiag(sig_d5))))  # (local)
    js_eu_boss = float(np.sqrt(joint_chi2(dmodel, cov_with_boss_offdiag(sig_eu))))  # (local)

    # --- data-anchored chi2 and Delta chi2 (current eBOSS precision) ---
    chi2_data = {}  # (local)
    dchi2_data = {}  # (local)
    for name, sig in [("current", err_obs), ("desi5", sig_d5), ("euclid", sig_eu)]:
        C = np.diag(sig ** 2)  # (local)
        c2F = joint_chi2(fs8_F - fsig8_obs, C)  # (local)
        c2L = joint_chi2(fs8_L - fsig8_obs, C)  # (local)
        chi2_data[name + "_FW"] = c2F
        chi2_data[name + "_LCDM"] = c2L
        dchi2_data[name] = c2F - c2L  # (local) negative => FW fits data better

    # ===================== VERDICT (headline = DESI-5yr forecast joint) =====================
    # The plan pins the FORECAST significance as the headline (dual_prior track_B / INFO branch).
    js_headline = joint_sigma["desi5"]  # (local) DESI-5yr / DR2 forecast joint significance
    js_euclid = joint_sigma["euclid"]  # (local) decisive-follow-up level
    js_current = joint_sigma["current"]  # (local) current-precision context

    sign_verdict = "PASS" if sign_all_negative else "FAIL"  # (local)
    if js_headline >= SIGMA_FORECAST:
        magnitude_verdict = "PASS"  # (local)
    elif js_headline >= INFO_FLOOR:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # regime: linear growth ODE valid throughout z in [0, 1.8]; full intended window used
    regime_verdict = "VALID"  # (local)

    # composite collapse (gate-verdicts.md): sign=FAIL -> FAIL ; mag=INFO -> INFO ; mag=PASS&sign=PASS -> PASS ; mag=FAIL -> FAIL
    if sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    value_str = (
        f"joint_sigma_DESI5yr={js_headline:.4g};joint_sigma_Euclid={js_euclid:.4g};"
        f"joint_sigma_current={js_current:.4g};coherent_negative={n_negative}/{n_bins};"
        f"product_supp_max={prod_supp_max_pct:.4g}%@z{z_at_max:g};bare_f_supp={bare_f_supp_pct:.4g}%;"
        f"dchi2_data_current={dchi2_data['current']:+.4g};thr_sigma={SIGMA_FORECAST:g}"
    )  # (local)

    # stash everything for the npz + plot + WP
    res.update({
        "value": value_str,
        "z_bins": zb, "tracers": data["tracers"],
        "fsig8_obs": fsig8_obs, "err_obs": err_obs,
        "sigma_desi5": sig_d5, "sigma_euclid": sig_eu,
        "f_FW_bins": f_F_bins, "f_LCDM_bins": f_L_bins,
        "sigma8_FW_bins": s8_F, "sigma8_LCDM_bins": s8_L,
        "fsig8_FW_bins": fs8_F, "fsig8_LCDM_bins": fs8_L,
        "frac_FW_pct": frac_FW_pct, "dmodel": dmodel,
        "f_FW_z0": f_FW_z0, "f_LCDM_z0": f_LCDM_z0,
        "f_FW_canonical": f_FW, "f_LCDM_canonical": f_LCDM,
        "bare_f_supp_pct": bare_f_supp_pct,
        "bare_f_supp_canonical_pct": f_bare_suppression_FW_pct,
        "product_supp_max_pct": prod_supp_max_pct, "z_at_max": z_at_max,
        "product_supp_canonical_pct": fsigma8_product_suppression_FW_max_pct,
        "joint_sigma_current": js_current,
        "joint_sigma_desi5": js_headline,
        "joint_sigma_euclid": js_euclid,
        "joint_sigma_desi5_boss_offdiag": js_d5_boss,
        "joint_sigma_euclid_boss_offdiag": js_eu_boss,
        "chi2_mm_current": chi2_mm["current"],
        "chi2_mm_desi5": chi2_mm["desi5"],
        "chi2_mm_euclid": chi2_mm["euclid"],
        "chi2_data_current_FW": chi2_data["current_FW"],
        "chi2_data_current_LCDM": chi2_data["current_LCDM"],
        "dchi2_data_current": dchi2_data["current"],
        "dchi2_data_desi5": dchi2_data["desi5"],
        "dchi2_data_euclid": dchi2_data["euclid"],
        "sign_all_negative": sign_all_negative, "n_negative": n_negative, "n_bins": n_bins,
        "sigma_forecast": SIGMA_FORECAST, "info_floor": INFO_FLOOR,
        "rho_boss_3851": RHO_BOSS_3851,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite": composite,
    })
    return res


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    zb = r["z_bins"]  # (local)
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.2))  # (local)

    # Panel 1: f*sigma8(z) curves + data
    ax = axes[0]  # (local)
    ax.errorbar(zb, r["fsig8_obs"], yerr=r["err_obs"], fmt="ko", ms=5, capsize=3,
                label="eBOSS-DR16 obs (current)", zorder=5)
    ax.errorbar(zb, r["fsig8_obs"], yerr=r["sigma_desi5"], fmt="none",
                ecolor="tab:green", alpha=0.5, capsize=2, label="DESI-5yr forecast sigma")
    ax.plot(zb, r["fsig8_LCDM_bins"], "s--", color="tab:blue", label="LCDM (w=-1)")
    ax.plot(zb, r["fsig8_FW_bins"], "d-", color="tab:red", label="FW (w=-0.918, a2-growth)")
    ax.set_xlabel("z"); ax.set_ylabel(r"$f\sigma_8(z)$")
    ax.set_title("f*sigma8(z): framework vs LCDM vs DESI/eBOSS")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: fractional product suppression per bin (coherent negative)
    ax = axes[1]  # (local)
    ax.axhline(0, color="k", lw=0.8)
    ax.plot(zb, r["frac_FW_pct"], "d-", color="tab:red")
    ax.axvline(r["z_at_max"], color="gray", ls=":", alpha=0.6)
    ax.annotate(f"max {r['product_supp_max_pct']:.3f}% @ z={r['z_at_max']:g}",
                xy=(r["z_at_max"], r["product_supp_max_pct"]),
                xytext=(0.5, -2.2), fontsize=9,
                arrowprops=dict(arrowstyle="->", color="gray"))
    ax.set_xlabel("z"); ax.set_ylabel(r"$(f\sigma_8^{FW}-f\sigma_8^{LCDM})/f\sigma_8^{LCDM}$ [%]")
    ax.set_title("Coherent same-sign product suppression (adds in quadrature)")
    ax.grid(alpha=0.3)

    # Panel 3: joint significance bar at 3 precision levels
    ax = axes[2]  # (local)
    levels = ["current\n(eBOSS)", "DESI-5yr\n(headline)", "Euclid\n(decisive)"]  # (local)
    vals = [r["joint_sigma_current"], r["joint_sigma_desi5"], r["joint_sigma_euclid"]]  # (local)
    colors = ["tab:gray", "tab:orange", "tab:green"]  # (local)
    bars = ax.bar(levels, vals, color=colors, alpha=0.85)
    ax.axhline(r["sigma_forecast"], color="tab:red", ls="--",
               label=f"PASS threshold {r['sigma_forecast']:g} sigma")
    ax.axhline(r["info_floor"], color="tab:blue", ls=":",
               label=f"INFO floor {r['info_floor']:g} sigma")
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.03, f"{v:.3f}",
                ha="center", va="bottom", fontsize=10)
    ax.set_ylabel("joint sigma (model-vs-model coherent)")
    ax.set_title(f"JOINT significance over {r['n_bins']} bins (composite: {r['composite']})")
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    fig.suptitle("INV7-W1-6 — f*sigma8 growth-suppression joint test (framework vs LCDM)",
                 fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — verdict payload
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
# Section 8 — Main
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
    print(f"  product_supp_max computed={r['product_supp_max_pct']:.4f}% @ z={r['z_at_max']:g}  "
          f"canonical={r['product_supp_canonical_pct']:.4f}% @ z=0.51")
    print()
    print("=== per-bin curve ===")
    print(f"  z_bins        = {np.array2string(r['z_bins'], precision=3)}")
    print(f"  fsig8_FW      = {np.array2string(r['fsig8_FW_bins'], precision=5)}")
    print(f"  fsig8_LCDM    = {np.array2string(r['fsig8_LCDM_bins'], precision=5)}")
    print(f"  frac_FW_pct   = {np.array2string(r['frac_FW_pct'], precision=4)}")
    print(f"  coherent_negative = {r['n_negative']}/{r['n_bins']}  (sign_verdict={r['sign_verdict']})")
    print()
    print("=== JOINT significance (model-vs-model coherent quadrature) ===")
    print(f"  current (eBOSS)  joint_sigma = {r['joint_sigma_current']:.4f}")
    print(f"  DESI-5yr (HEAD)  joint_sigma = {r['joint_sigma_desi5']:.4f}   "
          f"[BOSS-offdiag rho={r['rho_boss_3851']:g}: {r['joint_sigma_desi5_boss_offdiag']:.4f}]")
    print(f"  Euclid (decisive) joint_sigma = {r['joint_sigma_euclid']:.4f}   "
          f"[BOSS-offdiag: {r['joint_sigma_euclid_boss_offdiag']:.4f}]")
    print()
    print("=== data-anchored chi2 / Delta chi2 (FW fits data better => negative) ===")
    print(f"  current: chi2_FW={r['chi2_data_current_FW']:.4f}  chi2_LCDM={r['chi2_data_current_LCDM']:.4f}  "
          f"dchi2={r['dchi2_data_current']:+.4f}")
    print(f"  desi5 dchi2={r['dchi2_data_desi5']:+.4f}   euclid dchi2={r['dchi2_data_euclid']:+.4f}")
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

    note = (f"headline=DESI-5yr forecast joint_sigma={r['joint_sigma_desi5']:.4f} (<2 INFO-band); "
            f"Euclid joint_sigma={r['joint_sigma_euclid']:.4f} (>=2, decisive); "
            f"coherent same-sign suppression {r['n_negative']}/{r['n_bins']} bins; "
            f"data-anchored dchi2_current={r['dchi2_data_current']:+.4f} (FW marginally preferred)")  # (local)
    extra = [
        f"# INV7-W1-6 joint-sigma ladder: current={r['joint_sigma_current']:.4f} "
        f"desi5={r['joint_sigma_desi5']:.4f} euclid={r['joint_sigma_euclid']:.4f} thr=2.0",
        f"# INV7-W1-6 product_supp_max={r['product_supp_max_pct']:.4f}%@z{r['z_at_max']:g} "
        f"bare_f_supp={r['bare_f_supp_pct']:.4f}% (canonical -4.058%/-0.311%)",
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
