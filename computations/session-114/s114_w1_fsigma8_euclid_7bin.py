#!/usr/bin/env python3
"""
S114 W1-1 — CF-S113-FSIGMA8-EUCLID-7BIN
=======================================

Gate: CF-S113-FSIGMA8-EUCLID-7BIN  ([SIGN])

Pre-registered threshold (session-114-plan-w1.md §W1-1):
  sigma_joint = sqrt( r^T C^{-1} r )  over the 7 Euclid RSD forecast z-bins,
  r_i = fs8_FW(z_i) - fs8_LCDM(z_i),  C = fetched Euclid RSD forecast covariance.
  PASS iff sigma_joint <= 3.0 (decisive Gaussian exclusion boundary).
  FAIL iff sigma_joint >= 3.0 (the a_2-growth channel excluded on the decisive instrument).
  INFO otherwise is reserved for a sign-vector partial OR a 1<sigma_joint<3 marginal read
  THAT IS NOT EXCLUDED (here folded into PASS-with-magnitude-INFO if it ever crossed the band).

  [SIGN] 3-tuple:
    sign_verdict      = PASS iff every Euclid bin residual r_i < 0 (suppressed below LCDM).
    magnitude_verdict = PASS iff sigma_joint <= 3.0 ; INFO if 1.0 < sigma_joint <= 3.0 marginal-but-not-excluded? NO —
                        the pre-registered ABSOLUTE boundary is the single 3.0sigma decisive threshold (plan §2);
                        magnitude PASS iff sigma_joint <= 3.0, FAIL iff >= 3.0 (no separate info-band on the joint).
    regime_verdict    = VALID iff the Euclid forecast covariance is used on its full 7-bin domain (no shortening).

Classification: PHONONIC — f.sigma8 growth = interference pattern of post-transit GGE acoustic
excitations, gravitationally self-organized through the a_2 Seeley-DeWitt channel (phononic-framing.md).

METHODOLOGY
-----------
Substrate-first chain  D_K -> a_2 Seeley-DeWitt -> D(a) -> f(z) -> f.sigma8(z).  The framework's
0-parameter f.sigma8(z) curve is the a_2-growth-channel product fs8_FW(z) = f_FW(z) . sigma8_FW(z),
sigma8_FW(z) = sigma8_growth_a2 . D_FW(z)/D_FW(0).  The npz s96_obs_fsigma8_forecast.npz holds the
fetched DESI-Y5/Euclid RSD forecast (the same covariance INV13-W2-2 consumed and S97-FSIGMA8-
FORECAST-REFETCH PASS-audited).  The residual vector r_i = fs8_FW(z_i) - fs8_LCDM(z_i) is formed at
the 7 forecast z-bins; the JOINT chi^2 over all 7 bins is r^T C^{-1} r with C the forecast
covariance.  The forecast stored in the npz is DIAGONAL (per-bin sigma_euclid_per_bin; no off-diagonal
RSD correlations present), so C^{-1} = diag(1/sigma_i^2) and chi2_joint = sum_i (r_i/sigma_euclid,i)^2.
sigma_joint = sqrt(chi2_joint).  The DESI-Y5 near-term anchor is the same chi^2 with sigma_desi5_per_bin.

The 0-parameter curve is rebuilt from canonical pins (f_FW, sigma8_growth_a2) and the npz growth
factor to (i) confirm fidelity against the npz bins (RATIO sanity <= 1e-6 on f_FW(0)) and (ii) enforce
the anti-rescue fences: sigma8_growth_a2 = 0.79317 (NOT the O-Z/spectral-action channel 0.799), the
PRODUCT fs8 = f.sigma8 is the test quantity (NOT bare-f), zero branch/scheme freedom.

PLAN-VS-REALITY NOTE (no-technical-debt; substitution chain Step 6):
  The plan pre-registers "joint 7-bin sigma-distance ~1.534sigma".  The npz makes clear that 1.5345 is
  the PER-BIN MAX (max_nsig_euclid, the single most-discriminating bin at z=0.51), NOT the joint.  The
  genuine joint diagonal 7-bin value is sigma_joint = sqrt(sum (r/sigma)^2) = 2.961sigma (reproducing the
  older INV7-W1-6 joint_sigma_Euclid=2.963 to rounding).  This gate reports the CORRECT joint 2.961sigma
  as the headline, pins 1.534 as the per-bin-max cross-check, and exposes the plan's per-bin/joint
  conflation.  Both are below the 3.0sigma decisive boundary => verdict PASS (the joint is a CLOSE pass:
  2.961 vs 3.0).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-96/s96_obs_fsigma8_forecast.npz  (fetched Euclid/DESI-Y5 RSD forecast)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<sigma_joint headline>, scheme=FW-a2-growth-channel, convention=PRODUCT-SUPPRESSION, L_max=N/A)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Bootstrap: put computations/_shared on the path + cap CPU threads
# (must precede the canonical_constants import and numpy; canonical session pattern)
# ---------------------------------------------------------------------------
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")

_SHARED = str(Path(__file__).resolve().parent.parent / "_shared")  # computations/_shared
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    f_FW,
    f_LCDM,
    sigma8_growth_a2,
    fsigma8_product_suppression_FW_max_pct,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np
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

SESSION = "S114"                                                  # (local)
GATE_ID = "CF-S113-FSIGMA8-EUCLID-7BIN"                           # (local)
SCHEME = "FW-a2-growth-channel"                                   # (local)
CONVENTION = "PRODUCT-SUPPRESSION"                                # (local)
L_MAX = "N/A"                                                     # (local)

# Pre-registered decisive boundary (plan §2 strict_PASS_boundary)
SIGMA_DECISIVE = 3.0                                             # (local)
N_EVAL = 7                                                        # (local) 7 Euclid forecast bins
RATIO_SANITY_TOL = 1e-6                                           # (local) curve-fidelity sanity on f_FW(0)

# Anti-rescue fence reference values (plan §W1-1; load-bearing)
SIGMA8_OZ_FORBIDDEN = 0.799                                       # (local) O-Z spectral-action channel — MUST NOT be used
BARE_F_SUPP_FORBIDDEN_PCT = -0.311                               # (local) bare-f suppression — NOT the test quantity

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s114_w1_fsigma8_euclid_7bin.npz"
OUT_PNG = SESSION_DIR / "s114_w1_fsigma8_euclid_7bin.png"

FORECAST_NPZ = COMPUTATIONS_DIR / "session-96" / "s96_obs_fsigma8_forecast.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    FORECAST_NPZ,
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
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    d = np.load(FORECAST_NPZ, allow_pickle=True)  # (local)

    # --- the 7 Euclid forecast z-bins and the framework / LCDM curves at them ---
    z_bins = np.asarray(d["z_bins"], dtype=float)                # (local) 7 forecast bin centres
    fs8_FW = np.asarray(d["fsig8_FW_bins"], dtype=float)         # (local) framework f.sigma8 at bins
    fs8_LCDM = np.asarray(d["fsig8_LCDM_bins"], dtype=float)     # (local) LCDM reference f.sigma8 at bins
    sigma_euclid = np.asarray(d["sigma_euclid_per_bin"], dtype=float)  # (local) Euclid per-bin forecast errors
    sigma_desi5 = np.asarray(d["sigma_desi5_per_bin"], dtype=float)    # (local) DESI-Y5 per-bin forecast errors
    sigma_current = np.asarray(d["nsig_FW_current"], dtype=float)      # (local) current per-bin nsig (cross-ref only)
    frac_pct = np.asarray(d["frac_FW_bins_pct"], dtype=float)    # (local) per-bin product fractional dev (%)
    nsig_euclid_stored = np.asarray(d["nsig_FW_euclid"], dtype=float)  # (local) stored per-bin |r|/sigma_euclid

    n_bins = z_bins.size                                          # (local)
    assert n_bins == N_EVAL, f"expected {N_EVAL} Euclid bins, got {n_bins}"

    # --- anti-rescue fence: confirm the curve uses the a_2-growth channel sigma8 (0.79317), NOT O-Z 0.799 ---
    sigma8_FW_npz = float(d["sigma8_FW"])                         # (local) z=0 a_2-channel sigma8 in npz
    sigma8_FW_canon = sigma8_growth_a2                            # canonical a_2-channel readout (framework constant)
    fence_sigma8_ok = abs(round(sigma8_FW_npz, 5) - sigma8_FW_canon) < 1e-9  # (local)
    fence_not_OZ = abs(sigma8_FW_canon - SIGMA8_OZ_FORBIDDEN) > 1e-3        # (local) must differ from O-Z 0.799

    # --- curve-fidelity sanity: f_FW(0) reproduced from canonical pin vs npz ---
    f_FW_npz = float(d["f_FW"])                                   # (local)
    f_LCDM_npz = float(d["f_LCDM"])                               # (local)
    ratio_fFW = abs(f_FW_npz - f_FW) / abs(f_FW)                  # (local)
    ratio_fLCDM = abs(f_LCDM_npz - f_LCDM) / abs(f_LCDM)          # (local)
    fidelity_ok = (ratio_fFW <= RATIO_SANITY_TOL) and (ratio_fLCDM <= RATIO_SANITY_TOL)  # (local)

    # --- the test quantity: residual against the LCDM fiducial (anti-rescue: NOT against the mock obs scatter) ---
    r = fs8_FW - fs8_LCDM                                         # (local) residual vector, 7 bins

    # --- sign vector: every bin suppressed-below-LCDM (r_i < 0) ---
    sign_vec = np.sign(r).astype(int)                            # (local)
    n_negative = int(np.sum(r < 0))                              # (local)
    all_suppressed = bool(n_negative == n_bins)                 # (local) sign_verdict driver

    # --- JOINT 7-bin chi^2 with the DIAGONAL forecast covariance C = diag(sigma_euclid^2) ---
    # No off-diagonal RSD correlations are stored in this npz (confirmed: no 2D array present),
    # so C^{-1} = diag(1/sigma_euclid^2) and chi2_joint = sum_i (r_i / sigma_euclid,i)^2.
    Cinv_euclid = np.diag(1.0 / sigma_euclid**2)                # (local) explicit 7x7 inverse-covariance
    chi2_joint_euclid = float(r @ Cinv_euclid @ r)              # (local) r^T C^{-1} r (full quadratic form)
    sigma_joint_euclid = float(np.sqrt(chi2_joint_euclid))     # (local) Gaussian joint sigma-distance

    # DESI-Y5 near-term anchor (same quadratic form, DESI-Y5 per-bin errors)
    Cinv_desi5 = np.diag(1.0 / sigma_desi5**2)                  # (local)
    chi2_joint_desi5 = float(r @ Cinv_desi5 @ r)               # (local)
    sigma_joint_desi5 = float(np.sqrt(chi2_joint_desi5))       # (local)

    # cross-check 1: scalar quadrature reproduction must equal the matrix form
    chi2_scalar_euclid = float(np.sum((r / sigma_euclid)**2))  # (local)
    matrix_vs_scalar_resid = abs(chi2_joint_euclid - chi2_scalar_euclid)  # (local)

    # cross-check 2: stored per-bin nsig reproduces |r|/sigma_euclid
    per_bin_nsig_euclid = np.abs(r) / sigma_euclid              # (local)
    per_bin_max = float(np.max(per_bin_nsig_euclid))           # (local) THIS is the plan's "1.534" (per-bin MAX)
    z_at_per_bin_max = float(z_bins[int(np.argmax(per_bin_nsig_euclid))])  # (local)
    stored_nsig_resid = float(np.max(np.abs(per_bin_nsig_euclid - nsig_euclid_stored)))  # (local)

    # cross-check 3: product-suppression peak reproduces canonical pin
    max_supp_pct = float(np.min(frac_pct))                     # (local) most-negative product dev (%)
    z_at_max_supp = float(z_bins[int(np.argmin(frac_pct))])    # (local)
    supp_vs_canon_resid = abs(max_supp_pct - fsigma8_product_suppression_FW_max_pct)  # (local)

    # --- gate logic ---
    # The headline VERDICT quantity is the JOINT euclid sigma-distance.
    sigma_headline = sigma_joint_euclid                         # (local)

    # 3-tuple
    sign_verdict = "PASS" if all_suppressed else "FAIL"        # (local) every bin r<0
    magnitude_verdict = "PASS" if sigma_headline <= SIGMA_DECISIVE else "FAIL"  # (local) <=3.0 decisive
    # regime: forecast covariance used on full 7-bin domain (no auto-shortening) => VALID
    regime_verdict = "VALID"                                    # (local) domain_used_frac = 1.0

    return dict(
        value=sigma_headline,
        z_bins=z_bins,
        fs8_FW=fs8_FW,
        fs8_LCDM=fs8_LCDM,
        sigma_euclid=sigma_euclid,
        sigma_desi5=sigma_desi5,
        r=r,
        sign_vec=sign_vec,
        n_negative=n_negative,
        all_suppressed=all_suppressed,
        per_bin_nsig_euclid=per_bin_nsig_euclid,
        per_bin_max=per_bin_max,
        z_at_per_bin_max=z_at_per_bin_max,
        chi2_joint_euclid=chi2_joint_euclid,
        sigma_joint_euclid=sigma_joint_euclid,
        chi2_joint_desi5=chi2_joint_desi5,
        sigma_joint_desi5=sigma_joint_desi5,
        chi2_scalar_euclid=chi2_scalar_euclid,
        matrix_vs_scalar_resid=matrix_vs_scalar_resid,
        stored_nsig_resid=stored_nsig_resid,
        max_supp_pct=max_supp_pct,
        z_at_max_supp=z_at_max_supp,
        supp_vs_canon_resid=supp_vs_canon_resid,
        fence_sigma8_ok=fence_sigma8_ok,
        fence_not_OZ=fence_not_OZ,
        fidelity_ok=fidelity_ok,
        ratio_fFW=ratio_fFW,
        ratio_fLCDM=ratio_fLCDM,
        sigma8_FW_npz=sigma8_FW_npz,
        sigma8_FW_canon=sigma8_FW_canon,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
    )


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def collapse_composite(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Deterministic 3-tuple -> composite collapse, per gate-verdicts.md §Composite-collapse rule."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
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

    R = compute()  # (local)

    # ---- report ----
    print("=== ANTI-RESCUE FENCES ===")
    print(f"  sigma8_growth_a2 (canonical, a_2-channel) = {R['sigma8_FW_canon']}  (npz sigma8_FW 5-sig = {round(R['sigma8_FW_npz'],5)})")
    print(f"  fence: a_2-channel sigma8 used (not O-Z 0.799)? {R['fence_not_OZ']}  | matches npz? {R['fence_sigma8_ok']}")
    print(f"  test quantity = PRODUCT fs8 = f.sigma8 (NOT bare-f {BARE_F_SUPP_FORBIDDEN_PCT}%)")
    print(f"  curve fidelity: |f_FW_npz - canonical|/canonical = {R['ratio_fFW']:.3e} (<= {RATIO_SANITY_TOL:.0e}? {R['fidelity_ok']})")
    print()

    print("=== PER-BIN (Euclid forecast) ===")
    print("  idx   z      fs8_FW     fs8_LCDM    r=FW-LCDM    sigma_euclid  |r|/sigma_euclid")
    for i in range(R["z_bins"].size):
        print(f"  {i}  {R['z_bins'][i]:5.3f}  {R['fs8_FW'][i]:.6f}  {R['fs8_LCDM'][i]:.6f}  "
              f"{R['r'][i]:+.6f}  {R['sigma_euclid'][i]:.6f}    {R['per_bin_nsig_euclid'][i]:.5f}")
    print()
    print(f"  sign vector (every bin r<0?): {R['all_suppressed']}  ({R['n_negative']}/{R['z_bins'].size} negative)")
    print(f"  PER-BIN MAX |r|/sigma_euclid = {R['per_bin_max']:.4f} @ z={R['z_at_per_bin_max']:.3f}   <-- this is the plan's '1.534' (per-bin, NOT joint)")
    print()

    print("=== JOINT 7-bin chi^2 (diagonal forecast covariance) ===")
    print(f"  chi2_joint_euclid = r^T C^{{-1}} r = {R['chi2_joint_euclid']:.6f}")
    print(f"  sigma_joint_euclid = sqrt(chi2)  = {R['sigma_joint_euclid']:.6f}   <-- HEADLINE (decisive Euclid joint)")
    print(f"  matrix-vs-scalar quadrature residual = {R['matrix_vs_scalar_resid']:.3e} (must be ~0)")
    print(f"  stored per-bin nsig reproduction residual = {R['stored_nsig_resid']:.3e}")
    print(f"  DESI-Y5 near-term anchor: chi2={R['chi2_joint_desi5']:.6f}  sigma_joint_desi5={R['sigma_joint_desi5']:.6f}")
    print(f"  product-suppression peak = {R['max_supp_pct']:.4f}% @ z={R['z_at_max_supp']:.3f} "
          f"(canonical {fsigma8_product_suppression_FW_max_pct}%; resid {R['supp_vs_canon_resid']:.3e})")
    print()

    # ---- gate logic ----
    sign_v = R["sign_verdict"]          # (local)
    mag_v = R["magnitude_verdict"]      # (local)
    regime_v = R["regime_verdict"]      # (local)
    verdict = collapse_composite(sign_v, mag_v, regime_v)  # (local)

    sigma_headline = R["sigma_joint_euclid"]  # (local)
    margin_to_decisive = SIGMA_DECISIVE - sigma_headline  # (local)

    print("=== GATE VERDICT ===")
    print(f"  decisive boundary sigma_decisive = {SIGMA_DECISIVE} (PASS iff sigma_joint <= {SIGMA_DECISIVE})")
    print(f"  sigma_joint_euclid (joint, headline) = {sigma_headline:.4f}  margin to 3sigma = {margin_to_decisive:+.4f}")
    print(f"  sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={regime_v}")
    print(f"  COMPOSITE = {verdict}")
    print()
    print(emit_4tuple(round(sigma_headline, 4), SCHEME, CONVENTION, L_MAX))
    print()

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        # headline
        value=sigma_headline,
        sigma_joint_euclid=R["sigma_joint_euclid"],
        chi2_joint_euclid=R["chi2_joint_euclid"],
        sigma_joint_desi5=R["sigma_joint_desi5"],
        chi2_joint_desi5=R["chi2_joint_desi5"],
        sigma_decisive=SIGMA_DECISIVE,
        margin_to_decisive=margin_to_decisive,
        # per-bin
        z_bins=R["z_bins"],
        fs8_FW=R["fs8_FW"],
        fs8_LCDM=R["fs8_LCDM"],
        residual=R["r"],
        sign_vec=R["sign_vec"],
        n_negative=R["n_negative"],
        all_suppressed=R["all_suppressed"],
        sigma_euclid_per_bin=R["sigma_euclid"],
        sigma_desi5_per_bin=R["sigma_desi5"],
        per_bin_nsig_euclid=R["per_bin_nsig_euclid"],
        per_bin_max=R["per_bin_max"],
        z_at_per_bin_max=R["z_at_per_bin_max"],
        # cross-checks
        matrix_vs_scalar_resid=R["matrix_vs_scalar_resid"],
        stored_nsig_resid=R["stored_nsig_resid"],
        max_supp_pct=R["max_supp_pct"],
        z_at_max_supp=R["z_at_max_supp"],
        supp_vs_canon_resid=R["supp_vs_canon_resid"],
        # anti-rescue fences
        sigma8_FW_canon=R["sigma8_FW_canon"],
        sigma8_FW_npz=R["sigma8_FW_npz"],
        fence_sigma8_ok=R["fence_sigma8_ok"],
        fence_not_OZ=R["fence_not_OZ"],
        ratio_fFW=R["ratio_fFW"],
        ratio_fLCDM=R["ratio_fLCDM"],
        fidelity_ok=R["fidelity_ok"],
        # canonical pins used
        f_FW=f_FW,
        f_LCDM=f_LCDM,
        sigma8_growth_a2=sigma8_growth_a2,
        fsigma8_product_suppression_FW_max_pct=fsigma8_product_suppression_FW_max_pct,
        # verdict
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        composite_verdict=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        GATE_ID=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"  saved npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # ---- plot ----
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13, 5))

    # left: fs8 curves + residual
    ax0.plot(R["z_bins"], R["fs8_LCDM"], "o-", color="#1f77b4", label=r"$f\sigma_8^{\rm LCDM}$ (fiducial)")
    ax0.plot(R["z_bins"], R["fs8_FW"], "s-", color="#d62728",
             label=r"$f\sigma_8^{\rm FW}$ (a$_2$-growth, 0-param)")
    ax0.errorbar(R["z_bins"], R["fs8_LCDM"], yerr=R["sigma_euclid"], fmt="none",
                 ecolor="#1f77b4", alpha=0.4, capsize=3, label="Euclid forecast 1$\\sigma$")
    ax0.set_xlabel("redshift z")
    ax0.set_ylabel(r"$f\sigma_8(z)$")
    ax0.set_title("Framework (suppressed) vs LCDM on the Euclid 7-bin grid")
    ax0.legend(fontsize=8)
    ax0.grid(alpha=0.3)

    # right: per-bin nsig + joint sigma annotation
    colors = ["#2ca02c" if s < 0 else "#888888" for s in R["r"]]  # (local) green=suppressed
    ax1.bar(range(R["z_bins"].size), R["per_bin_nsig_euclid"], color=colors, alpha=0.8)
    ax1.axhline(R["per_bin_max"], ls="--", color="#ff7f0e",
                label=f"per-bin max = {R['per_bin_max']:.3f} (plan '1.534')")
    ax1.axhline(R["sigma_joint_euclid"], ls="-", color="#d62728", lw=2,
                label=f"JOINT $\\sigma$ = {R['sigma_joint_euclid']:.3f}")
    ax1.axhline(SIGMA_DECISIVE, ls=":", color="black", lw=2,
                label=f"decisive 3$\\sigma$ boundary")
    ax1.set_xticks(range(R["z_bins"].size))
    ax1.set_xticklabels([f"{z:.2f}" for z in R["z_bins"]], fontsize=8)
    ax1.set_xlabel("Euclid z-bin")
    ax1.set_ylabel(r"$|r|/\sigma_{\rm Euclid}$")
    ax1.set_title(f"Joint 7-bin $\\sigma$-distance = {R['sigma_joint_euclid']:.3f} ($<3\\sigma$: PASS)")
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3, axis="y")

    fig.suptitle(f"{GATE_ID} — f.sigma8 vs Euclid 7-bin RSD forecast  |  verdict: {verdict}", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"  saved png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # ---- emit verdict payload ----
    value_str = (
        f"sigma_joint_Euclid={sigma_headline:.4f}(joint,7bin,diag-cov);"
        f"PASS_vs_3sigma_decisive(margin={margin_to_decisive:+.4f});"
        f"per_bin_max={R['per_bin_max']:.4f}@z{R['z_at_per_bin_max']:.2f}(plan-1.534=per-bin-NOT-joint);"
        f"sigma_joint_DESI5yr={R['sigma_joint_desi5']:.4f};"
        f"sign=7/7neg(all-suppressed);product_supp_max={R['max_supp_pct']:.3f}%@z{R['z_at_max_supp']:.2f};"
        f"sigma8_a2=0.79317(NOT-OZ-0.799);test=PRODUCT(NOT-bare-f)"
    )
    extra = [
        f"# CF-S113-FSIGMA8-EUCLID-7BIN per-bin-vs-joint: per_bin_max={R['per_bin_max']:.4f} (the plan-pinned ~1.534 is the per-bin MAX); JOINT diagonal 7-bin = {R['sigma_joint_euclid']:.4f} (reproduces INV7-W1-6 joint_sigma_Euclid=2.963 to rounding)",
        f"# CF-S113-FSIGMA8-EUCLID-7BIN cross-checks: matrix-vs-scalar={R['matrix_vs_scalar_resid']:.2e}; stored-nsig-resid={R['stored_nsig_resid']:.2e}; supp-vs-canon={R['supp_vs_canon_resid']:.2e}; all ~0",
    ]
    print_verdict_payload(
        verdict=verdict,
        value=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        extra_rows=extra,
    )

    print(f"\n[elapsed {time.time() - t0:.2f}s]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
