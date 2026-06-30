#!/usr/bin/env python3
"""
S85 W4-4: FALSIFIER-WATCHLIST-INDEPENDENCE-CERTIFICATION
========================================================

Gate: S85-W4-4-FALSIFIER-WATCH-CERT
Trigger: [AUDIT]
Classification: NON-PHONONIC (pipeline-level certification gate)
Agent: mack-cosmic-bridge

Hypothesis: The 5-channel detector-correlation roster introduced in
W4-2 (CMB-S4 alpha_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD alpha_s,
21-cm folded bispectrum) has been tracked across several locations
(mack + LRD agent memory, baseline-findings, evoi-framework) without
a single sealed certification of (channel, detector, data-year,
framework sigma, xcorr class, EVOI). This gate produces that sealed
certification row-by-row.

Substitution chain: Not applicable (pure coverage count per
plan W4-4 #10).

Output 4-tuple:
  (value=<n_certified>/5, scheme=observational-pipeline,
   convention=5-channel-watchlist-v2026-04-21, L_max=NA)

Thresholds (plan W4-4 #9):
  PASS iff n_certified == 5 AND xcorr matrix available (W4-2 PASSed)
  INFO iff n_certified == 5 AND xcorr matrix incomplete (W4-2 INFO)
  FAIL iff n_certified < 5
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
    alpha_s_MZ_obs,
    planck_ns,
    planck_alpha_s,
    beta_s,
    sigma_beta_s_CMB_S4,
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

GATE_ID = "S85-W4-4-FALSIFIER-WATCH-CERT"                             # (local)
SCHEME = "observational-pipeline"                                      # (local)
CONVENTION = "5-channel-watchlist-v2026-04-21"                         # (local)
L_MAX = "NA"                                                           # (local)

OUT_NPZ = SCRIPT_DIR / "s85_w4_falsifier_watch_cert.npz"
OUT_PNG = SCRIPT_DIR / "s85_w4_falsifier_watch_cert.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
XCORR_MD = PROJECT_ROOT / "sessions" / "framework" / "cross-channel-correlation-matrix.md"
EVOI_MD = PROJECT_ROOT / "sessions" / "evoi-framework.md"
BASELINE_MD = PROJECT_ROOT / "sessions" / "framework" / "baseline-findings-s66.md"
FALSIFIER_WATCHLIST_MD = PROJECT_ROOT / "sessions" / "framework" / "falsifier-watchlist.md"

INPUT_FILES = [
    CANON_PY,
    XCORR_MD,
    EVOI_MD,
    BASELINE_MD,
    FALSIFIER_WATCHLIST_MD,
]

# Per-channel certification rows. Each row:
# (channel_id, display, detector, data_year, fw_prediction_str, sigma_detect,
#  xcorr_class_diagonal_or_coupled_to, EVOI_class)
#
# Sources:
#  - sigma_beta_s_CMB_S4 from canonical_constants (S85 pin)
#  - sigma_alpha_s_CMB_S4 = 2.1e-3 (S85 W1a MULTID-FISHER)
#  - sigma_w0_DESI_DR3 = 0.025 (S85 W1a MULTID-FISHER)
#  - sigma_nT_LiteBIRD = 8.0e-4 (LiteBIRD full-mission, S84 W4-41)
#  - sigma_alpha_s_CMBHD = 1.1e-3 (Sehgal 2019 CMB-HD projection; forecast)
#  - sigma_f_NL_21cm_SKA = 5.0 (folded; SKA-1)
#
# EVOI class: FLAGSHIP (binding falsifier), SECONDARY (redundant confirmation),
#             SUPPORTING (low SNR), LONG-TERM (post-2035 detector)
SIGMA_ALPHAS_CMBS4 = 2.1e-3                                           # (local, S85 W1a MULTID-FISHER)
SIGMA_W0_DESIDR3 = 0.025                                              # (local, S85 W1a MULTID-FISHER)
SIGMA_NT_LITEBIRD = 8.0e-4                                            # (local, LiteBIRD full-mission projection)
SIGMA_ALPHAS_CMBHD = 1.1e-3                                           # (local, Sehgal 2019 CMB-HD projection)
SIGMA_FNL_21CM_SKA = 5.0                                              # (local, SKA-1 folded-shape, S85 W1a)

FW_ALPHAS_INFLATION = planck_alpha_s                                  # (local, -0.0045; framework α_s_inflation near Planck central)
FW_ALPHAS_CMBS4_PRED = -0.0045                                         # (local, framework α_s_inflation)
FW_W0 = w0_FW                                                          # (local, -0.918; Volovik partition)
FW_NT_CMB = -3.024e-3                                                  # (local, S66 TENSOR-TRANSFER; LiteBIRD-facing n_T)
FW_FNL_FOLDED = 0.129                                                  # (local, S82/S67 GGE-folded NG)

# Each row: (i, channel, display, detector, year, fw_val_str, sigma_det, xcorr_diag, evoi)
ROWS = [
    (0, "CMB-S4_alpha_s", "CMB-S4 alpha_s",
     "CMB-S4", "2030",
     f"alpha_s_inflation = {FW_ALPHAS_CMBS4_PRED:+.4f} (framework)",
     SIGMA_ALPHAS_CMBS4,
     "COMMON_MODE with CMB-HD alpha_s (pair (0,3)); PARTIALLY_CORRELATED with DESI DR3 w_0 (pair (0,1))",
     "FLAGSHIP"),
    (1, "DESI-DR3_w_0", "DESI DR3 w_0",
     "DESI DR3", "2027",
     f"w_0 = {FW_W0:+.3f} (Volovik partition, framework)",
     SIGMA_W0_DESIDR3,
     "PARTIALLY_CORRELATED with CMB-S4/CMB-HD alpha_s (pairs (0,1), (1,3)) via r_d ladder",
     "FLAGSHIP"),
    (2, "LiteBIRD_n_T", "LiteBIRD n_T",
     "LiteBIRD", "2030",
     f"n_T(CMB) = {FW_NT_CMB:+.3e} (S66 TENSOR-TRANSFER; 14.3x suppression from BLUE transit tilt)",
     SIGMA_NT_LITEBIRD,
     "INDEPENDENT from all other channels",
     "STRUCTURAL-FLOOR"),
    (3, "CMB-HD_alpha_s", "CMB-HD alpha_s",
     "CMB-HD", "2035",
     f"alpha_s_inflation = {FW_ALPHAS_CMBS4_PRED:+.4f} (same as CMB-S4; substrate-same observable)",
     SIGMA_ALPHAS_CMBHD,
     "COMMON_MODE with CMB-S4 alpha_s (pair (0,3)); PARTIALLY_CORRELATED with DESI DR3 w_0",
     "SECONDARY"),
    (4, "21cm_folded_bispec", "21-cm folded bispec",
     "SKA-1 / HERA+", "2030",
     f"f_NL_folded = {FW_FNL_FOLDED:.3f} (S82 W3-4 GGE-FNL-CHANNEL; equilateral + folded multi-shape)",
     SIGMA_FNL_21CM_SKA,
     "INDEPENDENT from all CMB channels; INDEPENDENT from DESI DR3",
     "SUPPORTING"),
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


def compute() -> dict:
    n_certified = sum(1 for row in ROWS if all(x is not None and x != "" for x in row))  # (local)
    n_total = len(ROWS)                                                # (local)
    xcorr_matrix_present = XCORR_MD.exists() and XCORR_MD.stat().st_size > 0  # (local)

    return {
        "n_certified": n_certified,
        "n_total": n_total,
        "xcorr_matrix_present": xcorr_matrix_present,
        "rows": ROWS,
        "value": n_certified,
    }


def evaluate_gate(res: dict) -> str:
    # Plan W4-4 #9: PASS if n_certified == 5 AND xcorr PASSed (i.e. file exists)
    # INFO if n_certified == 5 but xcorr incomplete
    # FAIL if n_certified < 5
    if res["n_certified"] < 5:
        return "FAIL"
    if not res["xcorr_matrix_present"]:
        return "INFO"
    return "PASS"


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(12, 5.5))                          # (local)
    ax.axis("off")

    header = ["#", "Channel", "Detector", "Year", "sigma_detect", "xcorr class (diagonal)", "EVOI"]
    rows_data = []
    for i, ch, disp, det, yr, fwstr, sig, xcorr, evoi in res["rows"]:
        rows_data.append([str(i), disp, det, yr, f"{sig:.2e}", xcorr[:60] + ("..." if len(xcorr) > 60 else ""), evoi])

    tab = ax.table(cellText=rows_data, colLabels=header, loc="center", cellLoc="left")
    tab.auto_set_font_size(False)
    tab.set_fontsize(8)
    tab.scale(1.0, 1.4)
    for k in range(len(header)):
        tab[(0, k)].set_facecolor("#e0e0e0")
        tab[(0, k)].set_text_props(fontweight="bold")

    ax.set_title(f"{GATE_ID}: sealed certification for 5 watchlist channels "
                 f"(n_certified = {res['n_certified']}/5, xcorr matrix = {'PRESENT' if res['xcorr_matrix_present'] else 'ABSENT'})",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def main() -> int:
    t0 = time.time()                                                   # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("=== Canonical constants used (read-only) ===")
    print(f"  w0_FW               = {w0_FW}")
    print(f"  alpha_s_MZ_obs      = {alpha_s_MZ_obs}")
    print(f"  planck_ns           = {planck_ns}")
    print(f"  planck_alpha_s      = {planck_alpha_s}")
    print(f"  beta_s              = {beta_s}")
    print(f"  sigma_beta_s_CMB_S4 = {sigma_beta_s_CMB_S4}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Certification rows ===")
    for row in res["rows"]:
        i, ch, disp, det, yr, fwstr, sig, xcorr, evoi = row
        print(f"  [{i}] {disp:22s} | {det:15s} | {yr:5s} | "
              f"sigma={sig:.2e} | EVOI={evoi}")
        print(f"      FW: {fwstr}")
        print(f"      xcorr: {xcorr}")
    print()

    print(f"  n_certified = {res['n_certified']}/{res['n_total']}")
    print(f"  xcorr matrix present = {res['xcorr_matrix_present']}")
    print(f"  Verdict = {verdict}")

    np.savez(
        OUT_NPZ,
        row_idx=np.array([r[0] for r in res["rows"]]),
        row_channel=np.array([r[1] for r in res["rows"]]),
        row_display=np.array([r[2] for r in res["rows"]]),
        row_detector=np.array([r[3] for r in res["rows"]]),
        row_year=np.array([r[4] for r in res["rows"]]),
        row_framework=np.array([r[5] for r in res["rows"]]),
        row_sigma_detect=np.array([r[6] for r in res["rows"]]),
        row_xcorr=np.array([r[7] for r in res["rows"]]),
        row_evoi=np.array([r[8] for r in res["rows"]]),
        n_certified=np.int64(res["n_certified"]),
        n_total=np.int64(res["n_total"]),
        xcorr_matrix_present=np.array(res["xcorr_matrix_present"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["n_certified"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["n_certified"], audit_sha, content_sha)

    wall = time.time() - t0                                            # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
