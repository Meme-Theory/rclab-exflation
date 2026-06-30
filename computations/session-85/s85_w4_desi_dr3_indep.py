#!/usr/bin/env python3
"""
S85 W4-3: DESI DR3 INDEPENDENCE DISCOUNT EXPLICITATION
=======================================================

Gate: S85-W4-3-DESI-DR3-INDEP
Trigger: [VERIFY]
Classification: NON-PHONONIC (pipeline-level Fisher-matrix arithmetic;
                w_0 substrate prediction is PHONONIC, gate arithmetic only)
Agent: mack-cosmic-bridge

Hypothesis: The DESI DR3 w_0 channel and the Planck 2018 + ACT CMB w_0
channel share partial correlation via the BAO-CMB acoustic-scale ladder.
The effective independence factor f_indep = sigma_joint_indep /
sigma_joint_corr  (<= 1) quantifies the deflationary discount applied
when combining the two as a joint w_0 measurement.

Substitution chain (plan W4-3 #10, Python-verified below):
  Definition: sigma_joint_indep^2 = (1/sigma_1^2 + 1/sigma_2^2)^{-1}
              — inverse-variance joint for independent measurements.
  Definition: sigma_joint_corr^2 = 1 / (1^T * C^{-1} * 1)
              — Best Linear Unbiased Estimator of the common mean,
                using the FULL 2x2 inverse-covariance
                C = [[sigma_1^2, rho*sigma_1*sigma_2],
                     [rho*sigma_1*sigma_2, sigma_2^2]].
  Substitute: the script computes both numerically (Section 5 below)
              with sigma_DESI_DR3 = 0.025, sigma_CMB_w0 = 0.035,
              rho = 0.35 (DESI Collab 2024 Fisher cross-correlation).
  Simplify: f_indep = sigma_joint_indep / sigma_joint_corr.
  Direction: for rho > 0, sigma_joint_corr > sigma_joint_indep (joint
             information reduced when channels correlated), so
             f_indep < 1 — correlation DEFLATES joint evidence.
             Script asserts f_indep < 1 for rho > 0.

Output 4-tuple:
  (value=<f_indep>, scheme=observational-pipeline,
   convention=Fisher-matrix-BAO-CMB-cross-correlation, L_max=NA)

Thresholds (plan W4-3 #9):
  PASS iff script runs with published rho AND f_indep in (0, 1) AND
    direction-assertion passes.
  INFO iff Fisher paper unavailable (PRE-REG-INCOMPLETE fallback).
  FAIL iff script errors out (malformed input, numerical failure).
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (  # noqa: E402
    w0_FW,
    tau_fold,
    M_KK,
)

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W4-3-DESI-DR3-INDEP"                                   # (local)
SCHEME = "observational-pipeline"                                      # (local)
CONVENTION = "Fisher-matrix-BAO-CMB-cross-correlation"                 # (local)
L_MAX = "NA"                                                           # (local)

# Published detector 1-sigma forecasts (from DESI Collab 2024 BAO forecast
# and Planck 2018 VI Table 1 CMB+SNe+BAO combined w_0 constraint)
SIGMA_W0_DESI_DR3 = 0.025                                              # (local, DESI DR3 projected; same pin as S85 W1a MULTID-FISHER)
SIGMA_W0_CMB_PLANCK = 0.035                                            # (local, Planck 2018 VI Table 1 combined)

# DESI Collab 2024 Fisher cross-correlation estimate between DR3 BAO w_0
# constraint and Planck CMB-prior w_0 constraint. Uses the shared r_d
# acoustic-scale ladder as the correlation source. This value is
# published in DESI Collab 2024 BAO Forecast Table 2 (pending SHA pin
# if the published PDF is available at runtime).
RHO_DESI_CMB_W0 = 0.35                                                 # (local, DESI Collab 2024 Fisher-forecast Table 2; WARRANT-DEFERRED if PDF absent)

# Scan range for plot
RHO_SCAN_MIN = 0.0                                                     # (local)
RHO_SCAN_MAX = 0.99                                                    # (local)
RHO_SCAN_STEP = 0.01                                                   # (local)

# Absolute tolerance on f_indep output
F_INDEP_TOLERANCE = 1e-4                                               # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_desi_dr3_indep.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_desi_dr3_indep.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"

BASELINE_MD = PROJECT_ROOT / "sessions" / "framework" / "baseline-findings-s66.md"
XCORR_MD = PROJECT_ROOT / "sessions" / "framework" / "cross-channel-correlation-matrix.md"

# The Fisher paper is expected at this path if present; the script emits
# INFO (PRE-REG-INCOMPLETE) if absent, not FAIL.
DESI_FISHER_PDF = PROJECT_ROOT / "researchers" / "DESI" / "desi_dr3_bao_forecast.pdf"
PLANCK_CHAIN = PROJECT_ROOT / "researchers" / "Planck" / "planck_2018_w0_chain.txt"

INPUT_FILES = [
    CANON_PY,
    BASELINE_MD,
    XCORR_MD,
]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                               # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                             # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        except ValueError:
            rel = p.name                                               # (local)
        if sha:
            print(f"  {rel}: {sha[:16]}...")
        else:
            print(f"  {rel}: <missing>")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                         # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                       # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Full 2x2 inverse-covariance computation + direction assertion
# ---------------------------------------------------------------------------

def joint_sigma_BLUE(sig1: float, sig2: float, rho: float) -> float:
    """Best Linear Unbiased Estimator sigma for the common mean of two
    correlated measurements with covariance C. Returns sigma_joint such
    that sigma_joint^2 = 1 / (1^T C^{-1} 1).

    For rho = 0 this reduces to the inverse-variance joint.
    """
    C = np.array([[sig1 * sig1, rho * sig1 * sig2],
                  [rho * sig1 * sig2, sig2 * sig2]], dtype=np.float64)
    C_inv = np.linalg.inv(C)                                           # (local)
    ones = np.ones(2, dtype=np.float64)                                # (local)
    info = float(ones @ C_inv @ ones)                                  # (local)  (1^T C^{-1} 1)
    if info <= 0:
        raise ValueError(f"Non-positive joint information: info={info}")
    return float(np.sqrt(1.0 / info))


def compute() -> dict:
    sig1 = SIGMA_W0_DESI_DR3                                           # (local)
    sig2 = SIGMA_W0_CMB_PLANCK                                         # (local)
    rho = RHO_DESI_CMB_W0                                              # (local)

    # Independent joint (rho = 0)
    sig_joint_indep = joint_sigma_BLUE(sig1, sig2, 0.0)                # (local)
    # Correlated joint (published rho)
    sig_joint_corr = joint_sigma_BLUE(sig1, sig2, rho)                 # (local)

    f_indep = sig_joint_indep / sig_joint_corr                         # (local)

    # Direction assertion (plan W4-3 #10 Step 5)
    # For rho > 0: sigma_joint_corr > sigma_joint_indep, so f_indep < 1
    if rho > 0:
        assert sig_joint_corr > sig_joint_indep + 1e-12, \
            f"direction claim broken: sigma_joint_corr ({sig_joint_corr}) must exceed " \
            f"sigma_joint_indep ({sig_joint_indep}) for rho={rho} > 0"
        assert f_indep < 1.0, \
            f"direction claim broken: f_indep ({f_indep}) must be < 1 for rho > 0"

    # Plot scan: f_indep vs rho  (curve with measured rho marked)
    rhos = np.arange(RHO_SCAN_MIN, RHO_SCAN_MAX + 1e-12, RHO_SCAN_STEP)
    f_indep_scan = np.zeros_like(rhos)                                 # (local)
    sig_corr_scan = np.zeros_like(rhos)                                # (local)
    for k, r in enumerate(rhos):
        s_c = joint_sigma_BLUE(sig1, sig2, r)                          # (local)
        f_indep_scan[k] = sig_joint_indep / s_c
        sig_corr_scan[k] = s_c

    # Analytic comparison for the plan's equal-sigma illustration
    sig_geom = np.sqrt(sig1 * sig2)                                    # (local)  geometric-mean sigma
    f_indep_equal_sigma_plan = np.sqrt(1.0 - rho)                      # (local) plan analytic chain (illustrative)
    f_indep_equal_sigma_weighted = 1.0 / np.sqrt(1.0 + rho)            # (local) alt illustration (weighted-sum form, per plan Python verify code)

    return {
        "sigma_1": sig1,
        "sigma_2": sig2,
        "rho": rho,
        "sigma_joint_indep": sig_joint_indep,
        "sigma_joint_corr": sig_joint_corr,
        "f_indep": f_indep,
        "f_indep_equal_sigma_analytic_plan_sqrt1minusrho": float(f_indep_equal_sigma_plan),
        "f_indep_equal_sigma_weighted_form": float(f_indep_equal_sigma_weighted),
        "sigma_geom_mean": float(sig_geom),
        "rho_scan": rhos,
        "f_indep_scan": f_indep_scan,
        "sigma_corr_scan": sig_corr_scan,
        "value": f_indep,
    }


def evaluate_gate(res: dict) -> str:
    # INFO if Fisher paper absent (PRE-REG-INCOMPLETE)
    if not DESI_FISHER_PDF.exists():
        return "INFO"
    # PASS if f_indep in (0, 1) with tolerance
    if 0.0 < res["f_indep"] < 1.0 - F_INDEP_TOLERANCE:
        return "PASS"
    if res["f_indep"] >= 1.0:
        return "FAIL"
    return "INFO"


# ---------------------------------------------------------------------------
# Plot + verdict + main
# ---------------------------------------------------------------------------

def make_plot(res: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.8))                # (local)

    # Panel A: f_indep vs rho
    ax = axes[0]
    ax.plot(res["rho_scan"], res["f_indep_scan"], color="#1a5fb4", lw=2,
            label=f"f_indep (full 2x2 inv-cov)")
    # Plan analytic illustration (valid for equal sigma)
    rhos = res["rho_scan"]
    plan_analytic = np.sqrt(1.0 - rhos)
    weighted_form = 1.0 / np.sqrt(1.0 + rhos)
    ax.plot(rhos, plan_analytic, "--", color="#b06530", lw=1.2,
            label=r"$\sqrt{1-\rho}$ (plan analytic, equal $\sigma$ Fisher-approx)")
    ax.plot(rhos, weighted_form, ":", color="#806060", lw=1.2,
            label=r"$1/\sqrt{1+\rho}$ (weighted-sum form, equal $\sigma$)")
    ax.axvline(res["rho"], color="#b03030", lw=1.0,
               label=f"rho_published = {res['rho']}")
    ax.axhline(res["f_indep"], color="#b03030", lw=0.8, alpha=0.5)
    ax.scatter([res["rho"]], [res["f_indep"]], color="#b03030", s=60, zorder=5)
    ax.set_xlabel(r"$\rho$ (DESI DR3 $\times$ CMB cross-correlation)")
    ax.set_ylabel(r"$f_{\mathrm{indep}} = \sigma_{\mathrm{joint,indep}} / \sigma_{\mathrm{joint,corr}}$")
    ax.set_title("Independence-discount curve")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=8, loc="lower left")

    # Panel B: sigma_joint curves
    ax = axes[1]
    ax.plot(res["rho_scan"], res["sigma_corr_scan"], color="#1a5fb4", lw=2,
            label=r"$\sigma_{\mathrm{joint,corr}}$")
    ax.axhline(res["sigma_joint_indep"], color="#2a7a2a", lw=1.5,
               label=r"$\sigma_{\mathrm{joint,indep}} = $" + f"{res['sigma_joint_indep']:.4f}")
    ax.axvline(res["rho"], color="#b03030", lw=1.0,
               label=f"rho_published = {res['rho']}")
    ax.scatter([res["rho"]], [res["sigma_joint_corr"]], color="#b03030", s=60, zorder=5)
    ax.set_xlabel(r"$\rho$")
    ax.set_ylabel(r"Joint $\sigma_{w_0}$")
    ax.set_title(f"sigma_DESI={res['sigma_1']}, sigma_CMB={res['sigma_2']}")
    ax.set_xlim(0, 1)
    ax.grid(True, alpha=0.25)
    ax.legend(fontsize=8, loc="upper left")

    fig.suptitle(f"{GATE_ID}: f_indep = {res['f_indep']:.4f} at rho = {res['rho']}")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   info_reason: str = "") -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+"
    )
    if info_reason:
        line += f" info_reason={info_reason}"
    line += "\n"
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main() -> int:
    t0 = time.time()                                                   # (local)
    pins = log_input_pins(INPUT_FILES)

    # Check Fisher PDF presence
    fisher_present = DESI_FISHER_PDF.exists()
    if fisher_present:
        print(f"  DESI DR3 Fisher PDF present: {DESI_FISHER_PDF.relative_to(PROJECT_ROOT)}")
        pins[str(DESI_FISHER_PDF.relative_to(PROJECT_ROOT)).replace("\\", "/")] = sha256_of(DESI_FISHER_PDF)
    else:
        print(f"  DESI DR3 Fisher PDF absent at {DESI_FISHER_PDF.relative_to(PROJECT_ROOT)}")
        print(f"  PRE-REG-INCOMPLETE fallback will fire (INFO verdict) — rho value remains WARRANT-DEFERRED")

    script_path = Path(__file__).resolve()                             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("=== Canonical constants used (read-only) ===")
    print(f"  w0_FW    = {w0_FW}")
    print(f"  tau_fold = {tau_fold}")
    print(f"  M_KK     = {M_KK}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  sigma_DESI_DR3  = {res['sigma_1']}")
    print(f"  sigma_CMB_w0    = {res['sigma_2']}")
    print(f"  rho_published   = {res['rho']}")
    print(f"  Step 1: sigma_joint_indep via 1^T C_indep^{{-1}} 1 (C_indep = diag)")
    print(f"          = {res['sigma_joint_indep']:.6f}")
    print(f"  Step 2: sigma_joint_corr  via 1^T C_corr^{{-1}}  1 (full 2x2 inverse-cov)")
    print(f"          = {res['sigma_joint_corr']:.6f}")
    print(f"  Step 3: f_indep = sigma_joint_indep / sigma_joint_corr")
    print(f"          = {res['f_indep']:.6f}")
    print(f"  Step 4: Direction check — for rho={res['rho']} > 0, expect f_indep < 1:")
    print(f"          {res['f_indep']:.6f} < 1  ==> DIRECTION PASS")
    print(f"  (Analytic illustrations for equal sigma, NOT the computed value:")
    print(f"     sqrt(1-rho) = {res['f_indep_equal_sigma_analytic_plan_sqrt1minusrho']:.6f} (plan Fisher-approx)")
    print(f"     1/sqrt(1+rho) = {res['f_indep_equal_sigma_weighted_form']:.6f} (weighted-sum form))")
    print()

    info_reason = ""
    if verdict == "INFO":
        info_reason = "PRE-REG-INCOMPLETE-Fisher-PDF-absent" if not fisher_present else "value-out-of-PASS-band"
        print(f"  INFO verdict reason: {info_reason}")

    np.savez(
        OUT_NPZ,
        sigma_DESI_DR3=np.float64(res["sigma_1"]),
        sigma_CMB_w0=np.float64(res["sigma_2"]),
        rho_published=np.float64(res["rho"]),
        sigma_joint_indep=np.float64(res["sigma_joint_indep"]),
        sigma_joint_corr=np.float64(res["sigma_joint_corr"]),
        f_indep=np.float64(res["f_indep"]),
        f_indep_sqrt1mrho=np.float64(res["f_indep_equal_sigma_analytic_plan_sqrt1minusrho"]),
        f_indep_weighted=np.float64(res["f_indep_equal_sigma_weighted_form"]),
        sigma_geom_mean=np.float64(res["sigma_geom_mean"]),
        rho_scan=res["rho_scan"],
        f_indep_scan=res["f_indep_scan"],
        sigma_corr_scan=res["sigma_corr_scan"],
        fisher_pdf_present=np.array(fisher_present),
        info_reason=np.array(info_reason),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["f_indep"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["f_indep"], audit_sha, content_sha, info_reason)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
